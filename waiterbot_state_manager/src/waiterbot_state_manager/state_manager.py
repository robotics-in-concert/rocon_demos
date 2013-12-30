#
# License: BSD
#   https://raw.github.com/robotics-in-concert/rocon_demos/license/LICENSE
#

import rospy
import std_msgs.msg as std_msgs
import waiterbot_msgs.msg as waiterbot_msgs

class StateManager(object):
    """
        Waiterbot state manager
        
        Handles the various states of the Waiterbot
    """

#    __slots__ = ['state_customer_ordering', 'state_goto_vm', 'state_vm_ordering', 'state_goto_customer']

    def __init__(self):
        self._initialiseRosComms()
        self._initStates()

    '''
        ROS Comms
    '''
    def _initialiseRosComms(self):
        ''' Android UI communication '''
        self._sub_drink_order = rospy.Subscriber('android_ui/drink_order', std_msgs.UInt16MultiArray,
                                                 self._drinkOrderCB)
        self._pub_drink_ar = rospy.Publisher('android_ui/drink_ar', std_msgs.UInt16, latch=True)
        self._pub_drinks_dispensed = rospy.Publisher('android_ui/drinks_dispensed', std_msgs.Empty, latch=True)
        self._drink_order = None
        self._order_received = False
        ''' Waiterbot navigation controller communication '''
        self._pub_nav_ctrl_goal = rospy.Publisher('waiterbot_nav_control/goto', waiterbot_msgs.NavCtrlGoTo, latch=True)
        self._sub_nav_ctrl_status = rospy.Subscriber('waiterbot_nav_control/status', waiterbot_msgs.NavCtrlStatus,
                                                     self._navCtrlStatusCB)
        self.goto_goal_published = False
        self.goto_goal_reached = False

        ''' Vending machine feedback processor communication '''
        self._pub_vm_feedback_enable = rospy.Publisher('vm_feedback_proc/enable', std_msgs.Bool, latch=True)
        self._sub_vm_feedback_result = rospy.Subscriber('vm_feedback_proc/result', std_msgs.Bool,
                                                        self._vmFeedbackResultCB)
        ''' Debug/monitoring output '''
        self._pub_state_manager_debug = rospy.Publisher('~debug', std_msgs.String)

    def _drinkOrderCB(self, msg):
        self._drink_order = msg.data
        self._order_received = True

    def _navCtrlStatusCB(self, msg):
        if self.goto_goal_published:
            if self._current_state == self._state_goto_vm:
                if msg.status_code == waiterbot_msgs.NavCtrlStatus.VM_ARRIVAL:
                    self.goto_goal_reached = True
            elif self._current_state == self._state_goto_vm:
                if msg.status_code == waiterbot_msgs.NavCtrlStatus.ORIGIN_ARRIVAL:
                    self.goto_goal_reached = True

    def _vmFeedbackResultCB(self, msg):
        pass

    '''
        States
    '''
    def _initStates(self):
        self._state_customer_ordering = "StateCustomerOrdering"
        self._state_goto_vm = "StateGoToVM"
        self._state_vm_ordering = "StateVmOrdering"
        self._state_goto_customer = "StateGoToCustomer"
        self._current_state = self._state_customer_ordering

    def _stateCustomerOrdering(self):
        ''' Waits for receiving the drink order from the Android UI '''

        if self._order_received:
            self._order_received = False
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
            Triggers the process for dispensing the ordered drink by communicating with the vending machine
            through the Android UI and light signal processor
        '''

        if True:
            self._current_state = self._state_goto_customer
            self._publishCurrentStateChange()

    def _stateGoToCustomer(self):
        ''' Triggers navigation control to move the robot to the customer's place '''

        if True:
            self._current_state = self._state_customer_ordering
            self._publishCurrentStateChange()

    def spin(self):
        while not rospy.is_shutdown():
            if self._current_state == self._state_customer_ordering:
                self._stateCustomerOrdering()
            elif self._current_state == self._state_goto_vm:
                self._stateGoToVM()
            elif self._current_state == self._state_vm_ordering:
                self._stateVMOrdering()
            elif self._current_state == self._state_goto_customer:
                self._stateGoToCustomer()
            else:
                rospy.logerror("State not valid! Exiting ...")
                return
            self._publishCurrentState()
            rospy.sleep(0.1)

    '''
        Utils
    '''
    def _publishCurrentState(self):
        msg = std_msgs.String()
        msg.data = "Current state: " + self._current_state + "."
        self._pub_state_manager_debug.publish(msg)

    def _publishCurrentStateChange(self):
        msg = std_msgs.String()
        msg.data = "Changing to state '" + self._current_state + "'."
        self._pub_state_manager_debug.publish(msg)

