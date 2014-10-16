#!/usr/bin/env python
#
# License: BSD
#   https://raw.github.com/robotics-in-concert/rocon_demos/license/LICENSE
#
import rospy
import simple_delivery_msgs.msg as simple_delivery_msgs
import yocs_msgs.msg as yocs_msgs
import kobuki_msgs.msg as kobuki_msgs
import std_msgs.msg as std_msgs
import actionlib
import copy
import kobuki_utils
from kobuki_utils import play_sound
from waiterbot_bringup import ButtonControl

DELIVERY_ACTION = 'delivery_order'
LOC_ACTION = 'localize'
NAV_ACTION = 'navigate_to'

STATE_INITIALIZATION = 'INITIALIZATION'
STATE_GOTO_BASE      = 'GOTO_BASE'
STATE_AT_BASE        = 'AT_BASE'
STATE_GOTO_KITCHEN   = 'GOTO_KITCHEN'
STATE_AT_KITCHEN     = 'AT_KITCHEN'
STATE_GOTO_TABLE     = 'GOTO_TABLE'
STATE_AT_TABLE       = 'AT_TABLE'
STATE_BACKTO_BASE    = 'BACKTO_BASE'
STATE_REINITIALIZATION = 'REINITIALIZATION'
STATE_ON_ERROR       = 'ON_ERROR'
STATE_RESET          = 'RESET'

# INIT
# GOTO KITCHEN
# AT_KITCHEN
# GOTO_TABLE
# AT_TABLE
# BACKTO_KITCHEN
# REINITIALIZATION
# ERROR

class StateManager(object):
    
    _delivery_action_name = 'delivery_order'
    _navigator_action_name = 'navigate_to'
    _pickup_location = 'pickup'
    _base_location = 'base'
    _reinit_location = 'base_front'

    """
    _confirm_sound = 'kaku.wav'
    _retry_sound = 'moo.wav'
    _navi_failed_sound = 'angry_cat.wav'
    _order_received_sound = 'kaku.wav'
    _at_table_sound = 'lion.wav'
    _enjoy_meal_sound = 'meow.wav'
    _bab_sound = 'pab.wav'
    """ 
    _init_sound = 'init.wav'
    _confirm_sound = 'confirm.wav'
    _retry_sound = 'retry.wav'
    _navi_failed_sound = 'navi_failed.wav'
    _order_received_sound = 'order_received.wav'
    _at_table_sound = 'at_table.wav'
    _enjoy_meal_sound = 'enjoy_meal.wav'
    _at_base_sound = 'at_base.wav'
    _at_pickup_sound = 'at_pickup.wav'

    def __init__(self):
        self._init_variables()
        self._init_handles()
        self._init_states()

    def _init_states(self):
        self._states = {}
        self._states[STATE_INITIALIZATION] = self._state_initialization
        self._states[STATE_GOTO_BASE] = self._state_goto_base
        self._states[STATE_AT_BASE] = self._state_at_base
        self._states[STATE_GOTO_KITCHEN] = self._state_goto_kitchen
        self._states[STATE_AT_KITCHEN] = self._state_at_kitchen
        self._states[STATE_GOTO_TABLE] = self._state_goto_table
        self._states[STATE_AT_TABLE]   = self._state_at_table
        self._states[STATE_BACKTO_BASE]   = self._state_backto_base
        self._states[STATE_REINITIALIZATION] = self._state_initialization
        self._states[STATE_ON_ERROR] = self._state_on_error
        self._states[STATE_RESET] = self._state_reset

    def _init_variables(self):
        self._init_requested = False
        self._delivery_order_received = False
        self._delivery_locations = []
        self._delivery_location_index = 0
        self._delivery_order_id = 0
        self._pickup_confirm = False
        self._customer_confirm = False
        self._order_in_progress = False
            
        self._previous_red_button_time = None
        self._red_count = 0

        self._nav_base_timeout = rospy.get_param('~nav_base_timeout', 300.0)
        self._nav_pickup_timeout = rospy.get_param('~nav_pickup_timeout', 300.0)
        
        self._nav_table_timeout = rospy.get_param('~nav_table_timeout', 300.0)
        self._nav_retry         = rospy.get_param('~nav_retry', 3)
        self._nav_table_distance = rospy.get_param('~nav_table_distance', 0.5)
        self._resource_path = rospy.get_param('~resource_path')
        self.loginfo("Resource path : %s"% self._resource_path)


    def _init_handles(self):
        # order handle
        self._deliver_order_handler = actionlib.SimpleActionServer(DELIVERY_ACTION, simple_delivery_msgs.RobotDeliveryOrderAction, auto_start=False)
        self._deliver_order_handler.register_goal_callback(self._process_deliver_order)
        self._deliver_order_handler.register_preempt_callback(self._process_deliver_order_preempt)

        self._sub = {}
        self._pub = {}

        # Debug        
        self._pub['debug'] = rospy.Publisher('robot_status', std_msgs.String, queue_size=2)

        # Localize manager
        self.loginfo('Wait for Localise manager to be up')
        self._ac = {}
        self._ac[LOC_ACTION] = actionlib.SimpleActionClient(LOC_ACTION, yocs_msgs.LocalizeAction)
        self._ac[LOC_ACTION].wait_for_server()

        # semantic navigation handler
        self._navigator_handler = actionlib.SimpleActionClient(NAV_ACTION, yocs_msgs.NavigateToAction)

        self.loginfo('Wait for Sematic Navigator Server to be up')
        self._navigator_handler.wait_for_server()

        # Led Controller
        self._led_controller = kobuki_utils.LedBlinker()

        # Button Controller
        self._button_controller = ButtonControl('/mobile_base/events/digital_input', self._process_button)

    def _process_button(self, green, red):
        self.loginfo("Button Pressed. Green[%s] Red[%s]"%(str(green),str(red)))

        if green:
            if not self._current_state:
                self._current_state = STATE_INITIALIZATION
        
            if self._current_state == STATE_ON_ERROR:
                self._current_state = STATE_INITIALIZATION

            if self._current_state == STATE_AT_KITCHEN:
                self._pickup_confirm = True

            if self._current_state == STATE_AT_TABLE:
                self._customer_confirm = True

        if red:
            now = rospy.Time.now()

            if not self._previous_red_button_time:
                self._red_count = 1
            else:
                di = now - self._previous_red_button_time
                if di.to_sec() < 5:
                    self._red_count = self._red_count + 1
                else:
                    self._red_count = 1

                if self._red_count == 3:
                    self._current_state = STATE_RESET
                    self._red_count = 0
            self._previous_red_button_time = now

    def _process_deliver_order(self):
        self.loginfo('Received Goal')
        if self._current_state != STATE_AT_BASE:
            message = 'Robot is not at base. Ignore the order!'
            self.logwarn(message)
            goal = self._deliver_order_handler.accept_new_goal()
            r = simple_delivery_msgs.RobotDeliveryOrderResult()
            r.order_id = goal.order_id
            r.message = message
            r.success = False
            self._deliver_order_handler.set_succeeded(r)
        else:
            goal = self._deliver_order_handler.accept_new_goal()
            self.loginfo(str(goal))
            self._delivery_order_id = goal.order_id
            self._delivery_locations = goal.locations
            self._delivery_location_index = 0
            self._delivery_order_received = True

    def _process_deliver_order_preempt(self):
        self.loginfo("Delivery order preemption requested")
        self.loginfo("Do nothing for now")

    def spin(self):
        r = rospy.Rate(10)
        self._current_state = STATE_ON_ERROR
        self._deliver_order_handler.start()
        self._led_controller.start()
        play_sound(self._resource_path, self._init_sound)

        t = 2
        while not rospy.is_shutdown():
            self._states[self._current_state]()
            t = (t % 5) + 1

            if t == 1:
                self._logging()
            r.sleep()

    def _logging(self):
        #self.loginfo(self._current_state)
        self._pub['debug'].publish(str(self._current_state))

        if self._order_in_progress:
            feedback = simple_delivery_msgs.RobotDeliveryOrderFeedback()
            feedback.delivery_status = simple_delivery_msgs.DeliveryStatus()
            if self._current_state == STATE_AT_BASE:
                feedback.delivery_status.status = simple_delivery_msgs.DeliveryStatus.IDLE
            elif self._current_state == STATE_GOTO_KITCHEN:
                feedback.delivery_status.status = simple_delivery_msgs.DeliveryStatus.GO_TO_FRONTDESK
            elif self._current_state == STATE_AT_KITCHEN:
                feedback.delivery_status.status = simple_delivery_msgs.DeliveryStatus.WAITING_FOR_FRONTDESK
            elif self._current_state == STATE_GOTO_TABLE:
                feedback.delivery_status.status = simple_delivery_msgs.DeliveryStatus.GO_TO_RECEIVER
            elif self._current_state == STATE_AT_TABLE:
                feedback.delivery_status.status = simple_delivery_msgs.DeliveryStatus.WAITING_CONFIRM_RECEIVER
            elif self._current_state == STATE_BACKTO_BASE:
                feedback.delivery_status.status = simple_delivery_msgs.DeliveryStatus.RETURN_TO_DOCK
            elif self._current_state == STATE_REINITIALIZATION:
                feedback.delivery_status.status = simple_delivery_msgs.DeliveryStatus.COMPLETE_RETURN
            elif self._current_state == STATE_ON_ERROR:
                feedback.delivery_status.status = simple_delivery_msgs.DeliveryStatus.ERROR
            feedback.delivery_status.order_id = self._delivery_order_id
            feedback.delivery_status.target_goal = self._target_location
            self._deliver_order_handler.publish_feedback(feedback)
                
    def loginfo(self, msg):
        rospy.loginfo('Robot State Manager : ' + str(msg))

    def logwarn(self, msg):
        rospy.logwarn('Robot State Manager : ' + str(msg))

    def _request_navigator(self, location, approach_type, num_retry, timeout, distance):
        goal = yocs_msgs.NavigateToGoal()

        goal.location = location
        goal.approach_type = approach_type
        goal.num_retry = num_retry
        goal.timeout = float(timeout)
        goal.distance = distance
        self._target_location = location
        self._navigator_handler.send_goal(goal, done_cb=self._navigator_done, feedback_cb=self._navigator_feedback)
        self._navigator_finished = False 

    def _navigator_done(self, status, result):
        self.loginfo("Navigator Result : %s, Message : %s"%(result.success,result.message)) 
        
        if result.success == False:
            play_sound(self._resource_path, self._navi_failed_sound)
            self._current_state = STATE_RESET
        else:
            self._navigator_finished = True
        
    def _navigator_feedback(self, feedback):
        self._navigator_feed = str("Distance : %s, Remain Time : %s, Message : %s"%(str(feedback.distance),str(feedback.remain_time),str(feedback.message)))
        #self.loginfo("Navigator : " + str(self._navigator_feed))
        
        if feedback.status == yocs_msgs.NavigateToFeedback.STATUS_RETRY:
            play_sound(self._resource_path, self._retry_sound)


    def _state_initialization(self):
        if not self._init_requested:
            self._initialized = False
            goal = yocs_msgs.LocalizeGoal()
            goal.command = yocs_msgs.LocalizeGoal.STAND_AND_LOCALIZE
            self._ac[LOC_ACTION].send_goal(goal, done_cb=self._localize_done)
            self.loginfo('Localization Request sent')
            self._init_requested = True
            play_sound(self._resource_path, self._confirm_sound)
    
        if self._initialized:
            self.loginfo('Robot Localized')
            self.loginfo('Moving To base')

            self._request_navigator(self._base_location, yocs_msgs.NavigateToGoal.APPROACH_ON, self._nav_retry, self._nav_base_timeout, 0.0)
            # Request navigator to go kitchen
            self._current_state = STATE_GOTO_BASE
            self._init_requested = False
            self._led_controller.set_on_ok()

    def _localize_done(self, status, result):
        self.loginfo("Localize result : %s, Message : %s"%(result.success,result.message))

        if result.success:
            self._initialized = True 
        else:
            self._current_state = STATE_RESET

    def _state_goto_base(self):
        # Wait for arriving
        if self._navigator_finished:
            # When it arrives...
            self._current_state = STATE_AT_BASE
            self.loginfo("AT base")
            play_sound(self._resource_path, self._at_base_sound)

    def _state_at_base(self):
        if self._order_in_progress:
            self._order_in_progress = False
            message = 'Delivery Success!'
            r = simple_delivery_msgs.RobotDeliveryOrderResult()
            r.order_id = self._delivery_order_id
            r.message = message
            r.success = True
            self._deliver_order_handler.set_succeeded(r)

        if self._delivery_order_received:
            self._delivery_order_received = False
            self._order_in_progress = True
            self._request_navigator(self._pickup_location, yocs_msgs.NavigateToGoal.APPROACH_ON, self._nav_retry, self._nav_pickup_timeout, 0.0)
            self._current_state = STATE_GOTO_KITCHEN
            # Make a sound
            play_sound(self._resource_path, self._order_received_sound)

    def _state_goto_kitchen(self):
        # Wait for arriving
        if self._navigator_finished:
            self.loginfo("AT kitchen")
            # When it arrives...
            self._current_state = STATE_AT_KITCHEN
            play_sound(self._resource_path, self._at_pickup_sound)

    def _state_at_kitchen(self):
        # Wait for kitchen's confirmation
        if self._pickup_confirm== True:
            self._pickup_confirm = False
            play_sound(self._resource_path, self._confirm_sound)

            if len(self._delivery_locations) < self._delivery_location_index:
                self.loginfo("Error. Delivery Location is not set...%s"%str(self._delivery_locations))
                self._current_state = STATE_RESET
            else:
                self.loginfo('Moving To Table : %s'%self._delivery_locations[self._delivery_location_index])
                self._request_navigator(self._delivery_locations[self._delivery_location_index], yocs_msgs.NavigateToGoal.APPROACH_ON, 3, 300, 0.0)
                # Request navigator to go table 
                self._current_state = STATE_GOTO_TABLE

    def _state_goto_table(self):
        # Wait for arriving
        if self._navigator_finished:
            # When it arrives...
            self._current_state = STATE_AT_TABLE
            # arriving sound
            play_sound(self._resource_path, self._at_table_sound)
            feedback = simple_delivery_msgs.RobotDeliveryOrderFeedback()
            feedback.delivery_status = simple_delivery_msgs.DeliveryStatus()
            feedback.delivery_status.status = simple_delivery_msgs.DeliveryStatus.ARRIVAL_AT_RECEIVER
            feedback.delivery_status.order_id = self._delivery_order_id
            feedback.delivery_status.target_goal= self._target_location
            self._deliver_order_handler.publish_feedback(feedback)

    def _state_at_table(self):
        # Wait for Customer's confirmation
        if self._customer_confirm == True:
            self._customer_confirm = False
            play_sound(self._resource_path, self._enjoy_meal_sound)

            # If it goes to multiple delivery location..
            self._delivery_location_index = self._delivery_location_index + 1
            if self._delivery_location_index < len(self._delivery_locations):
                location = self._delivery_locations[self._delivery_location_index]
                self.loginfo('Moving to next destination[%s]'%str(location))
                self._request_navigator(location, yocs_msgs.NavigateToGoal.APPROACH_NEAR, 3, 300, self._nav_table_distance)
                feedback = simple_delivery_msgs.RobotDeliveryOrderFeedback()
                feedback.delivery_status = simple_delivery_msgs.DeliveryStatus()
                feedback.delivery_status.status = simple_delivery_msgs.DeliveryStatus.COMPLETE_DELIVERY
                feedback.delivery_status.order_id = self._delivery_order_id
                feedback.delivery_status.target_goal= self._target_location
                self._deliver_order_handler.publish_feedback(feedback)
                self._current_state = STATE_GOTO_TABLE
            else: # if it has finished delivery. moving back to base
                self.loginfo('Moving back to base')
                # Request navigator to go back to reinitialization positino 
                self._request_navigator(self._reinit_location, yocs_msgs.NavigateToGoal.APPROACH_ON, 3, 300, 0.0)

                feedback = simple_delivery_msgs.RobotDeliveryOrderFeedback()
                feedback.delivery_status = simple_delivery_msgs.DeliveryStatus()
                feedback.delivery_status.status = simple_delivery_msgs.DeliveryStatus.COMPLETE_ALL_DELIVERY
                feedback.delivery_status.order_id = self._delivery_order_id
                feedback.delivery_status.target_goal= self._target_location
                self._deliver_order_handler.publish_feedback(feedback)
                self._current_state = STATE_BACKTO_BASE

    def _state_backto_base(self):
        if self._navigator_finished:
            # When it arrives...
            self._current_state = STATE_REINITIALIZATION









    def _state_on_error(self):
        self._led_controller.set_on_error()
        rospy.sleep(1.0)

    def _state_reset(self):
        if self._order_in_progress:
            message = 'Delivery has cancelled!'
            r = simple_delivery_msgs.RobotDeliveryOrderResult()
            r.order_id = self._delivery_order_id
            r.message = message
            r.success = False
            self._deliver_order_handler.set_succeeded(r)
        self._navigator_handler.cancel_all_goals()
        self._init_variables()
        self._current_state = STATE_ON_ERROR

    def _blink_leds(self):
        self.last_blink_led = (self.last_blink_led % 2) + 1

        if self._current_state == STATE_ON_ERROR:
            led1_blink = self._off_led if self.last_blink_led == 1 else self._red_led
            led2_blink = self._red_led if self.last_blink_led == 1 else self._off_led
            self._pub['led1'].publish(led1_blink)
            self._pub['led2'].publish(led2_blink)
        else:
            led1_blink = self._off_led if self.last_blink_led == 1 else self._green_led 
            led2_blink = self._green_led if self.last_blink_led == 1 else self._off_led
            self._pub['led1'].publish(led1_blink)
            self._pub['led2'].publish(led2_blink)
