#!/usr/bin/env python
#
# License: BSD
#   https://raw.github.com/robotics-in-concert/rocon_demos/license/LICENSE
#

import threading

import rospy
import actionlib

import kobuki_utils
from waiterbot_bringup import ButtonControl

import yocs_msgs.msg  as yocs_msgs
import std_msgs.msg as std_msgs
import kobuki_msgs.msg as kobuki_msgs
from simple_delivery_msgs.msg import DeliveryStatus, DeliveryOrder, Receiver, RobotDeliveryOrderAction, RobotDeliveryOrderGoal, RobotDeliveryOrderResult

DELIVERY_ACTION = 'delivery_order'
LOC_ACTION = 'localize'
NAV_ACTION = 'navigate_to'
DOC_ACTION = 'docking_interactor'
SUB_BUTTON = '~digital_inputs'

STATUS = 'robot_status'

STATE_IDLE = 'IDLE'
STATE_WAKEUP = 'WAKEUP'
STATE_LOCALIZE = 'LOCALIZE'
STATE_REGISTER_DOCK = 'REGISTER_DOCK'
STATE_GOTO_PICKUP = 'GOTO_PICKUP'
STATE_AT_PICKUP = 'AT_PICKUP'
STATE_GOTO_TARGET = 'GOTO_TARGET'
STATE_AT_TARGET = 'AT_TARGET'
STATE_RETURN = 'RETURN'
STATE_RESET = 'RESET'
STATE_ON_ERROR = 'ON_ERROR'

class StateManager(object):

    def __init__(self): 
        self._init_states()
        self._init_handles()
        self._init_variables()

    def _init_variables(self):
        self._current_state = STATE_ON_ERROR
        self._initialized = False

        self._resource_path = rospy.get_param('~resource_path')
        self._nav_retry = rospy.get_param('~nav_retry', 3)
        self._nav_timeout= rospy.get_param('~nav_timeout', 300.0)
        self._nav_near_distance = rospy.get_param('~nav_near_distance', 5.0)
        self._pickup_location = rospy.get_param('~pickup_location','frontdesk')
        self._debug_mode = rospy.get_param('~debug', False)

        self._cancel_requested = False

        self._previouse_red_button_time = None
        self._red_count = 0

        self._previouse_green_button_time = None
        self._green_count = 0

    def _init_states(self):
        self._states = {}
        self._states[STATE_WAKEUP] = (self._wakeup, STATE_LOCALIZE, STATE_ON_ERROR)
        self._states[STATE_LOCALIZE] = (self._localize, STATE_REGISTER_DOCK, STATE_ON_ERROR)
        self._states[STATE_REGISTER_DOCK] = (self._register_dock, STATE_GOTO_PICKUP, STATE_ON_ERROR)
        self._states[STATE_GOTO_PICKUP] = (self._goto, STATE_AT_PICKUP, STATE_ON_ERROR)
        self._states[STATE_AT_PICKUP] = (self._wait_for_button, STATE_GOTO_TARGET, STATE_ON_ERROR)
        self._states[STATE_GOTO_TARGET] = (self._goto, STATE_AT_TARGET, STATE_ON_ERROR)
        self._states[STATE_AT_TARGET] = (self._wait_for_button, STATE_GOTO_TARGET, STATE_RETURN)
        self._states[STATE_RETURN] = (self._return, STATE_IDLE, STATE_ON_ERROR)

    def _init_handles(self):    
        self._as = {}
        self._ac = {}
        self._sub = {}
        self._pub = {}

        # Robot Status publishser
        self._pub[STATUS] = rospy.Publisher(STATUS, std_msgs.String, queue_size=2)

        # Setting up action server to receive order from manager
        self._as[DELIVERY_ACTION] = actionlib.SimpleActionServer(DELIVERY_ACTION, RobotDeliveryOrderAction, auto_start=False)
        self._as[DELIVERY_ACTION].register_goal_callback(self._process_delivery_order)
        self._as[DELIVERY_ACTION].register_preempt_callback(self._process_delivery_order_preempt)


        self.loginfo('Wait for Localise manager to be up')
        self._ac[LOC_ACTION] = actionlib.SimpleActionClient(LOC_ACTION, yocs_msgs.LocalizeAction)
        self._ac[LOC_ACTION].wait_for_server()

        self.loginfo('Wait for Docking interactor to be up')
        self._ac[DOC_ACTION] = actionlib.SimpleActionClient(DOC_ACTION, yocs_msgs.DockingInteractorAction)
        self._ac[DOC_ACTION].wait_for_server()

        # Setting up navigator action client to navigate around the map
        self.loginfo('Wait for Navigator server to be up')
        self._ac[NAV_ACTION] = actionlib.SimpleActionClient(NAV_ACTION, yocs_msgs.NavigateToAction)
        self._ac[NAV_ACTION].wait_for_server()

        # Led Controller
        self._led_controller = kobuki_utils.LedBlinker()

        # Button Controller
        self._button_controller = ButtonControl(self._process_button)

    def _process_button(self, green, red):
        self.loginfo("Button Pressed. Green[%s] Red[%s]"%(str(green),str(red)))

        if green:
            now = rospy.Time.now()
            
            if not self._previouse_green_button_time:
                self._green_count = 1
            else:
                di = now - self._previouse_green_button_time
                if di.to_sec() < 5:
                    self._green_count = self._green_count + 1
                else:
                    self._green_count = 1

            if self._current_state == STATE_ON_ERROR and self._green_count == 3:
                self._current_state = STATE_RESET
            else:
                if self._wait_for_button:
                    self._wait_for_button = False
        if red:
            now = rospy.Time.now()

            if not self._previouse_red_button_time:
                self._red_count = 1
            else:
                di = now - self._previouse_red_button_time
                if di.to_sec() < 5:
                    self._red_count = self._red_count + 1
                else:
                    self._red_count = 1
            
                if self._red_count == 3:
                    self._cancel_requested = True
                    self._red_count = 0
                self._previouse_red_button_time = now

    def _process_delivery_order(self):
        self.loginfo("Received Goal")

        if self._current_state != STATE_IDLE:
            message = 'Robot is under operation. Ignore the order!'
            self.logwarn(message)
            goal = self._as[DELIVERY_ACTION].accept_new_goal()
            r = RobotDeliveryOrderResult()
            r.message = message
            r.success= False
            r.order_id = goal.order_id
        else:
            goal = self._as[DELIVERY_ACTION].accept_new_goal()  
            self.loginfo(str(goal))
            self._order_process_thread = threading.Thread(target=self._execute_delivery, args=(goal))
            self._order_process_thread.start()

    def _process_delivery_order_preempt(self):
        self.loginfo("Preempt requested")
        self.loginfo("It does not do anything for now")

    def _state_reset(self):
        """
            Reset variables, set led ok, and set idle mode
        """
        self._current_state = STATE_IDLE
        self._led_controller.set_on_ok()

    def _state_on_error(self):
        self._led_controller.set_on_error()
        rospy.sleep(1.0)
    
    def spin(self):
        r = rospy.Rate(10)
        self._current_state = STATE_IDLE
        self._as[DELIVERY_ACTION].start()
        self._led_controller.start()
        self._led_controller.set_on_ok()

        t = 1
        while not rospy.is_shutdown():
#            self._states[self._current_state]()
            t = (t % 5) + 1
        
            if t == 1:
                self._log()
            r.sleep()
        self._led_controller.stop()

    def _log(self):
        self._pub[STATUS].publish(str(self._current_state))

    def loginfo(self, msg):
        rospy.loginfo('Robot State Manager : %s'%str(msg))

    def logwarn(self, msg):
        rospy.logwarn('Robot State Manager : %s'%str(msg))

    def _execute_delivery(self, goal):
        self._current_state = STATE_WAKEUP

        locations = []
        locations.append(self._pickup_location)
        locations.extend(goal.locations)

        location_index = 0
        while not rospy.is_shutdown() and not self._cancel_requested and self._current_state != STATE_IDLE:
            state_func, next_state1, next_state2 = self._states[self._current_state]

            if self._current_state == STATE_GOTO_TARGET or self._current_state == STATE_GPICKUPP:
                success, message = state_func(locations[location_index])
                location_index = location_index + 1
            else:
                success, message = state_func()

            if self._current_state == STATE_AT_TARGET:
                self._current_state = next_state1 if len(goal.locations) > location_index else next_state2
            else:
                self._current_state = next_state1 if success else next_state2
            self._send_delivery_order_feedback(success, message)

        if self._cancel_requested:
            self.logwarn('Order process has been cancelled..')
            self._current_state = STATE_ON_ERROR
            
    def _wakeup(self):
        """
          Wake up process. Request docking interactor to get out from dock and register dock ar on robot frame
        """ 
        goal = yocs_msgs.DockingInteractorGoal()
        goal.command = yocs_msgs.DockingInteractorGoal.WAKE_UP
        goal.distance = 0.5
        self._ac[DOC_ACTION].send_goal(goal)
        self._ac[DOC_ACTION].wait_for_result()

        r = self._ac[DOC_ACTION].get_result()

        if r.success:
            return True, "Wake up!"
        else:
            return False, "Failed to wake up..."
                
    def _localize(self):
        """
          Request localizer to locate the robot. and request docking interactor to regist dock ar on global frame
        """
        goal = yocs_msgs.LocalizeGoal()
        goal.command = yocs_msgs.LocalizeGoal.SPIN_AND_LOCALIZE
        self._ac[LOC_ACTION].send_goal(goal)
        self._ac[LOC_ACTION].wait_for_result()
        r = self._ac[LOC_ACTION].get_result()

        if r.success:
            return True, "Localization Success!"
        else:
            return False, "Failed to localize,,,"

    def _register_dock(self):
        """
        Request Docking Interactor to register docking location on global frame
        """
        goal = yocs_msgs.DockingInteractorGoal()
        goal.command = yocs_msgs.DockingInteractorGoal.REGISTER_DOCK_IN_GLOBAL_FRAME
        self._ac[DOC_ACTION].send_goal(goal)
        self._ac[DOC_ACTION].wait_for_result()
        r = self._ac[DOC_ACTION].get_result()
        
        if r.success:
            message = 'Dock Location has been set'
            return True, message
        else:
            message = 'Failed to Localize...'
            return False, message

    def _wait_for_button(self):
        """
            Wait for front desk confirmation.
        """
        if self._debug_mode:
            rospy.sleep(3.0)
            return True, "Debug mode button press simulated"
                   
        self._wait_for_button = True
        while not rospy.is_shutdown() and self._wait_for_button:
            rospy.sleep(0.5)
        return True, "Button Pressed"

    def _goto(self, loc):
        """
            Request navigator to go to target location
        """
        goal = yocs_msgs.NavigateToGoal()
        goal.location = loc
        goal.approach_type = yocs_msgs.NavigateToGoal.APPROACH_ON
        goal.timeout = self._nav_timeout
        goal.num_retry = self._nav_retry

        self.loginfo('Sending Robot to %s'%str(self._pickup_location))
        self._ac[NAV_ACTION].send_goal(goal, feedback_cb=self._nav_feedback)
        self._ac[NAV_ACTION].wait_for_result()

        r = self._ac[NAV_ACTION].get_result()
        if r.success:
            return True, "Arrived %s!"%str(loc)
        else:
            return False, "Failed to go %s!"%str(loc)

    def _return(self):
        """
            Request docking interactor to return to the docking station
        """
        goal = yocs_msgs.DockingInteractorGoal()
        goal.command = yocs_msgs.DockingInteractorGoal.RETURN_TO_DOCK
        self._ac[DOC_ACTION].send_goal(goal, feedback_cb=self._dock_feedback)
        self._ac[DOC_ACTION].wait_for_result()

        r = self._ac[DOC_ACTION].get_result()

        if r.success:
            return True, "ZzzzZzzz!"
        else:
            return False, "Failed to wake up..."

    def _nav_feedback(self, feedback):
        self.loginfo(str("Distance : %s, Remain Time : %s, Message : %s"%(str(feedback.distance),str(feedback.remain_time),str(feedback.message))))

    def _dock_feedback(self, feedback):
        
        if feedback.level == feedback.INFO:
            self.loginfo(feedback.message)
        elif feedback.level == feedback.DEBUG:
            self.logdebug(feedback.message)
        else:
            self.logwarn(feedback.message)
