#
# License: BSD
#   https://raw.github.com/robotics-in-concert/rocon_demos/license/LICENSE
#

import rospy
import kobuki_msgs.msg as kobuki_msgs
import std_msgs.msg as std_msgs
import waiterbot_msgs.msg as waiterbot_msgs

class StateManager(object):
    """
        Waiterbot state manager
        
        Handles the various states of the Waiterbot
    """

#    __slots__ = ['state_customer_ordering', 'state_goto_vm', 'state_vm_ordering', 'state_goto_customer']

    def __init__(self):
        self._initVariables()
        self._getRosParams()
        self._initialiseRosComms()
        self._initStates()

    '''
        Initialise all used variables
    '''
    def _initVariables(self):
        self._drink_order = []
        self._order_received = False
        self._tray_empty = False
        self.goto_goal_published = False
        self.goto_goal_reached = False
        self._confirm_button_pressed = False
        self._vm_feedback_proc_enabled = False
        self._drink_dispensed = False
        self._drinks_dispensed = False
        self._vm_feedback_on_time = rospy.Time.now()

    '''
        ROS parameters
    '''
    def _getRosParams(self):
        self._vm_feedback_signal_duration = rospy.Duration(rospy.get_param('~vm_feedback_signal_duration', 2.0))

    '''
        ROS Comms
    '''
    def _initialiseRosComms(self):
        # Android UI communication
        self._sub_drink_order = rospy.Subscriber('android_ui/drink_order', std_msgs.UInt16MultiArray,
                                                 self._drinkOrderCB)
        self._pub_drink_ar = rospy.Publisher('android_ui/drink_ar', std_msgs.UInt16, latch=True)
        self._pub_drinks_dispensed = rospy.Publisher('android_ui/drinks_dispensed', std_msgs.Empty, latch=True)
        self._pub_tray_empty = rospy.Publisher('android_ui/tray_empty', std_msgs.Empty, latch=True)
        # Waiterbot navigation controller communication
        self._pub_nav_ctrl_goal = rospy.Publisher('waiterbot_nav_control/goto', waiterbot_msgs.NavCtrlGoTo, latch=True)
        self._sub_nav_ctrl_status = rospy.Subscriber('waiterbot_nav_control/status', waiterbot_msgs.NavCtrlStatus,
                                                     self._navCtrlStatusCB)

        # Vending machine feedback processor communication
        self._pub_vm_feedback_enable = rospy.Publisher('vm_feedback_proc/enable', std_msgs.Bool, latch=True)
        self._sub_vm_feedback_result = rospy.Subscriber('vm_feedback_proc/result', std_msgs.Bool,
                                                        self._vmFeedbackResultCB)

        # Debug/monitoring output
        self._pub_state_manager_debug = rospy.Publisher('~debug', std_msgs.String, latch=True)

        # Button monitoring
        self._sub_buttons = rospy.Subscriber('kobuki/digital_input_events', kobuki_msgs.DigitalInputEvent,
                                             self._buttonCB)
        self._pub_cancel_order = rospy.Publisher('~order_cancelled', std_msgs.Empty, latch=True)

    def _drinkOrderCB(self, msg):
        if not self._order_received:
            for order in msg.data:
                self._drink_order.append(order)
            rospy.loginfo('State Manager: Received drink order: ' + str(self._drink_order))
            self._drink_order.reverse() # inverting to compensate the later use of pop() to get correct order
            self._order_received = True

    def _navCtrlStatusCB(self, msg):
        if self.goto_goal_published:
            if self._current_state == self._state_goto_vm:
                if msg.status_code == waiterbot_msgs.NavCtrlStatus.VM_ARRIVAL:
                    self.goto_goal_reached = True
                    self._publishDebugMsg('State Manager: Reached vending machine.')
            elif self._current_state == self._state_goto_customer:
                if msg.status_code == waiterbot_msgs.NavCtrlStatus.ORIGIN_ARRIVAL:
                    self.goto_goal_reached = True
                    self._publishDebugMsg('State Manager: Reached customer.')
            if msg.status_code == waiterbot_msgs.NavCtrlStatus.ERROR:
                self._publishDebugMsg('State Manager: Navigation control reported an error.')
                self._current_state = self._state_reset
                self._publishCurrentStateChange()

    def _vmFeedbackResultCB(self, msg):
        if msg.data and not self._drink_dispensed:
            self._vm_feedback_on_time = rospy.Time.now()
            self._drink_dispensed = True

    def _buttonCB(self, msg):
        # green button aka confirm button pressed
        if not msg.values[0]:
            self._confirm_button_pressed = True
            self._publishDebugMsg('State Manager: Confirm button pressed.')
        else:
            self._confirm_button_pressed = False

        # red button aka cancel button pressed
        if not msg.values[1]:
            self._publishDebugMsg('State Manager: Confirm button pressed.')
            self._current_state = self._state_reset
            self._publishCurrentStateChange()

    '''
        States
    '''
    def _initStates(self):
        self._state_customer_ordering = "StateCustomerOrdering"
        self._state_goto_vm = "StateGoToVM"
        self._state_vm_ordering = "StateVmOrdering"
        self._state_goto_customer = "StateGoToCustomer"
        self._state_reset = "StateReset"
        self._current_state = self._state_customer_ordering

    def _stateCustomerOrdering(self):
        ''' Waits for receiving the drink order from the Android UI '''

        if self._order_received:  # only store new order, if old one has been processed
            self._current_state = self._state_goto_vm
            self._publishCurrentStateChange()

    def _stateGoToVM(self):
        ''' Triggers navigation control to move the robot to the vending machine '''

        if not self.goto_goal_published:
            msg = waiterbot_msgs.NavCtrlGoTo()
            msg.goal = waiterbot_msgs.NavCtrlGoTo.GO_TO_VM
            self._pub_nav_ctrl_goal.publish(msg)
            self.goto_goal_published = True

        if self.goto_goal_reached:
            self.goto_goal_published = False
            self.goto_goal_reached = False
            self._current_state = self._state_vm_ordering
            self._publishCurrentStateChange()

    def _stateVMOrdering(self):
        '''
            Triggers the process for dispensing the ordered drinks by communicating with the vending machine
            through the Android UI and receives notification about successful drink dispenses from
            the light signal processor
        '''

        # activate the VM feedback processor
        if not self._vm_feedback_proc_enabled:
            self._vm_feedback_proc_enabled = True
            msg = std_msgs.Bool()
            msg.data = True
            self._pub_vm_feedback_enable.publish(msg)
            # send the first order
            drink_order_msg = std_msgs.UInt16()
            drink_order_msg. data = self._drink_order.pop()
            self._pub_drink_ar.publish(drink_order_msg)

        if self._drink_dispensed:
            # send remaining orders
            if len(self._drink_order) > 0:
                # Since the colour signal detection fluctuates, we wait for a certain time before considering it valid. 
                if (rospy.Time.now() - self._vm_feedback_on_time) > self._vm_feedback_signal_duration:
                    drink_order_msg = std_msgs.UInt16()
                    drink_order_msg. data = self._drink_order.pop()
                    self._pub_drink_ar.publish(drink_order_msg)
                    self._drink_dispensed = False
            elif len(self._drink_order) == 0:
                self._drinks_dispensed = True

        if self._drinks_dispensed:
            self._drink_dispensed = False
            self._drinks_dispensed = False
            self._order_received = False # reset, since all ordered drinks have been dispensed

            # disable VM feedback processing
            msg = std_msgs.Bool()
            msg.data = False
            self._pub_vm_feedback_enable.publish(msg)
            self._vm_feedback_proc_enabled = False

            # notify the Android UI about processed order
            empty_msg = std_msgs.Empty()
            self._pub_drinks_dispensed.publish(empty_msg)

            self._current_state = self._state_goto_customer
            self._publishCurrentStateChange()

    def _stateGoToCustomer(self):
        ''' Triggers navigation control to move the robot to the customer's place '''

        if not self.goto_goal_published:
            msg = waiterbot_msgs.NavCtrlGoTo()
            msg.goal = waiterbot_msgs.NavCtrlGoTo.GO_TO_ORIGIN
            self._pub_nav_ctrl_goal.publish(msg)
            self.goto_goal_published = True

        if self._confirm_button_pressed:
            self.goto_goal_reached = True
            empty_msg = std_msgs.Empty()
            self._pub_tray_empty.publish(empty_msg)
            rospy.loginfo('State Manager: Robot tray has been emptied.')

        if self.goto_goal_reached and self._confirm_button_pressed:
            self.goto_goal_reached = False
            self.goto_goal_published = False
            self._confirm_button_pressed = False
            self._current_state = self._state_customer_ordering
            self._publishCurrentStateChange()

    def _stateReset(self):
        if self._vm_feedback_proc_enabled:
            # disable VM feedback processing
            msg = std_msgs.Bool()
            msg.data = False
            self._pub_vm_feedback_enable.publish(msg)
            self._vm_feedback_proc_enabled = False
        empty_msg = std_msgs.Empty()
        self._pub_cancel_order.publish(empty_msg)
        self._initVariables()
        self._current_state = self._state_customer_ordering
        self._publishCurrentStateChange()


    def spin(self):
        while not rospy.is_shutdown():
            if self._current_state == self._state_reset:
                self._stateReset()
            elif self._current_state == self._state_customer_ordering:
                self._stateCustomerOrdering()
            elif self._current_state == self._state_goto_vm:
                self._stateGoToVM()
            elif self._current_state == self._state_vm_ordering:
                self._stateVMOrdering()
            elif self._current_state == self._state_goto_customer:
                self._stateGoToCustomer()
            else:
                rospy.logerror("State Manager: State not valid! Exiting ...")
                return
            self._publishCurrentState()
            rospy.sleep(0.5)

    '''
        Utils
    '''
    def _publishCurrentState(self):
        msg = std_msgs.String()
        msg.data = "Current state: " + self._current_state + "."
        self._pub_state_manager_debug.publish(msg)
        rospy.loginfo('State Manager: ' + msg.data)

    def _publishCurrentStateChange(self):
        msg = std_msgs.String()
        msg.data = "Changing to state '" + self._current_state + "'."
        self._pub_state_manager_debug.publish(msg)
        rospy.loginfo('State Manager: ' + msg.data)

    def _publishDebugMsg(self, msg):
        string_msg = std_msgs.String()
        string_msg.data = msg
        self._pub_state_manager_debug.publish(string_msg)
        rospy.loginfo('State Manager: ' + string_msg.data)
