#!/usr/bin/env python
#
# License: BSD
#   https://raw.github.com/robotics-in-concert/rocon_demos/license/LICENSE
#
import rospy
import simple_delivery_msgs.msg as simple_delivery_msgs
import diagnostic_msgs.msg as diagnostic_msgs
import yocs_msgs.msg as yocs_msgs
import kobuki_msgs.msg as kobuki_msgs
import std_msgs.msg as std_msgs
import actionlib
import copy
import kobuki_utils
from kobuki_utils import play_sound
from waiterbot_bringup import ButtonControl

DELIVERY_ACTION = 'delivery_order'
DOC_ACTION = 'docking_interactor'
LOC_ACTION = 'localize'
NAV_ACTION = 'navigate_to'
STATUS = 'robot_status'
DIAGNOSTIC = '/diagnostics_agg'

STATE_IN_DOCK        = 'IN_DOCK'
STATE_WAKEUP         = 'WAKE_UP'
STATE_LOCALISE       = 'LOCALISE'
STATE_REGISTER_DOCK  = 'REGISTER_DOCK'
STATE_GOTO_PICKUP    = 'GOTO_PICKUP'
STATE_AT_PICKUP      = 'AT_PICKUP'
STATE_GOTO_TABLE     = 'GOTO_TABLE'
STATE_AT_TABLE       = 'AT_TABLE'
STATE_BACKTO_BASE    = 'BACKTO_BASE'
STATE_ON_ERROR       = 'ON_ERROR'
STATE_RESET          = 'RESET'
STATE_CALL_AUTODOCK  = 'CALL_AUTODOCK'

# INIT
# GOTO KITCHEN
# AT_KITCHEN
# GOTO_TABLE
# AT_TABLE
# BACKTO_KITCHEN
# REINITIALIZATION
# ERROR

class StateManager(object):
    
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
    _retry_sound = 'navi_failed.wav'
    _reset_sound = 'try_again.wav'
    _navi_failed_sound = 'retry.wav'
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
        self._states[STATE_IN_DOCK]         = self._state_in_dock
        self._states[STATE_WAKEUP]          = self._state_wakeup
        self._states[STATE_LOCALISE]        = self._state_localise
        self._states[STATE_REGISTER_DOCK]   = self._state_register_dock
        self._states[STATE_GOTO_PICKUP]     = self._state_goto_pickup
        self._states[STATE_AT_PICKUP]       = self._state_at_pickup
        self._states[STATE_GOTO_TABLE]      = self._state_goto_table
        self._states[STATE_AT_TABLE]        = self._state_at_table
        self._states[STATE_BACKTO_BASE]     = self._state_backto_base
        self._states[STATE_ON_ERROR]        = self._state_on_error
        self._states[STATE_RESET]           = self._state_reset
        self._states[STATE_CALL_AUTODOCK]   = self._state_call_autodock

    def _init_variables(self):
        self._delivery_order_received = False
        self._delivery_locations = []
        self._delivery_location_index = 0
        self._delivery_order_id = 0

        self._order_in_progress = False

        self._dock_interactor_requested = False
        self._dock_interactor_finished = False

        self._localise_requested = False

        self._navigator_requested = False
        self._target_location = ""


        self._pickup_confirm = False
        self._customer_confirm = False
            
        self._previous_red_button_time = None
        self._red_count = 0
        self._robot_battery_status = 0

        self._nav_base_timeout = rospy.get_param('~nav_base_timeout', 300.0)
        self._nav_pickup_timeout = rospy.get_param('~nav_pickup_timeout', 300.0)
        
        self._nav_table_timeout = rospy.get_param('~nav_table_timeout', 300.0)
        self._nav_retry         = rospy.get_param('~nav_retry', 3)
        self._nav_table_distance = rospy.get_param('~nav_table_distance', 0.5)
        self._resource_path = rospy.get_param('~resource_path')
        self._volume  = rospy.get_param('~volume', 100)
        self.loginfo("Resource path : %s"% self._resource_path)


    def _init_handles(self):
        # order handle
        self._deliver_order_handler = actionlib.SimpleActionServer(DELIVERY_ACTION, simple_delivery_msgs.RobotDeliveryOrderAction, auto_start=False)
        self._deliver_order_handler.register_goal_callback(self._process_deliver_order)
        self._deliver_order_handler.register_preempt_callback(self._process_deliver_order_preempt)

        self._sub = {}
        self._pub = {}

        # Debug        
        self._pub[STATUS] = rospy.Publisher(STATUS, simple_delivery_msgs.RobotStatus, queue_size=2)
        self._sub[DIAGNOSTIC] = rospy.Subscriber(DIAGNOSTIC, diagnostic_msgs.DiagnosticArray, self._process_diagnostics)
        
        # Localize manager
        self.loginfo('Wait for Localise manager to be up')
        self._ac = {}
        self._ac[LOC_ACTION] = actionlib.SimpleActionClient(LOC_ACTION, yocs_msgs.LocalizeAction)
        self._ac[LOC_ACTION].wait_for_server()

        # semantic navigation handler
        self._ac[NAV_ACTION] = actionlib.SimpleActionClient(NAV_ACTION, yocs_msgs.NavigateToAction)

        self.loginfo('Wait for Sematic Navigator Server to be up')
        self._ac[NAV_ACTION].wait_for_server()

        self._ac[DOC_ACTION] = actionlib.SimpleActionClient(DOC_ACTION, yocs_msgs.DockingInteractorAction)
        self.loginfo('Wait for Docking Interactor Server to be up')
        self._ac[DOC_ACTION].wait_for_server()

        # Led Controller
        self._led_controller = kobuki_utils.LedBlinker()

        # Button Controller
        self._button_controller = ButtonControl('/mobile_base/events/digital_input', self._process_button)

    def _process_diagnostics(self, msg):
        for s in msg.status:
            if s.name == '/Power System/Battery':
                charge = 0
                capa = 0
                for v in s.values:
                    if v.key == 'Charge (Ah)':
                        charge = v.value
                    elif v.key == 'Capacity (Ah)':
                        capa = v.value
                battery_percent = 100 * float(charge) / float(capa);
                self._robot_battery_status = battery_percent
                break


    def _process_button(self, green, red):
        self.loginfo("Button Pressed. Green[%s] Red[%s]"%(str(green),str(red)))

        if green:
            if not self._current_state:
                self._current_state = STATE_ON_ERROR
        
            if self._current_state == STATE_ON_ERROR:
                self._current_state = STATE_CALL_AUTODOCK

            if self._current_state == STATE_AT_PICKUP:
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
        if self._current_state != STATE_IN_DOCK:
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
        self._current_state = STATE_IN_DOCK
        self._deliver_order_handler.start()
        self._led_controller.start()
        self.play_sound(self._init_sound)

        t = 2
        while not rospy.is_shutdown():
            self._states[self._current_state]()
            t = (t % 5) + 1

            if t == 1:
                self._logging()
            r.sleep()

    def _logging(self):
        #self.loginfo(self._current_state)

        feedback = simple_delivery_msgs.RobotDeliveryOrderFeedback()
        feedback.delivery_status = simple_delivery_msgs.DeliveryStatus()

        if self._current_state == STATE_IN_DOCK:
            feedback.delivery_status.status = simple_delivery_msgs.DeliveryStatus.IDLE
        elif self._current_state == STATE_WAKEUP or self._current_state == STATE_LOCALISE or self._current_state == STATE_REGISTER_DOCK or self._current_state == STATE_GOTO_PICKUP:
            feedback.delivery_status.status = simple_delivery_msgs.DeliveryStatus.GO_TO_FRONTDESK
        elif self._current_state == STATE_AT_PICKUP:
            feedback.delivery_status.status = simple_delivery_msgs.DeliveryStatus.WAITING_FOR_FRONTDESK
        elif self._current_state == STATE_GOTO_TABLE:
            feedback.delivery_status.status = simple_delivery_msgs.DeliveryStatus.GO_TO_RECEIVER
        elif self._current_state == STATE_AT_TABLE:
            feedback.delivery_status.status = simple_delivery_msgs.DeliveryStatus.WAITING_CONFIRM_RECEIVER
        elif self._current_state == STATE_BACKTO_BASE:
            feedback.delivery_status.status = simple_delivery_msgs.DeliveryStatus.RETURN_TO_DOCK
        #elif self._current_state == STATE_:
        #    feedback.delivery_status.status = simple_delivery_msgs.DeliveryStatus.COMPLETE_RETURN
        elif self._current_state == STATE_ON_ERROR:
            feedback.delivery_status.status = simple_delivery_msgs.DeliveryStatus.ERROR
        else:
            feedback.delivery_status.status = simple_delivery_msgs.DeliveryStatus.ERROR
        if self._order_in_progress:
            feedback.delivery_status.order_id = self._delivery_order_id
            feedback.delivery_status.target_goal = self._target_location
            self._deliver_order_handler.publish_feedback(feedback)
        self._pub[STATUS].publish(feedback.delivery_status.status, self._robot_battery_status)
                
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
        self._ac[NAV_ACTION].send_goal(goal, done_cb=self._navigator_done, feedback_cb=self._navigator_feedback)
        self._navigator_finished = False 

    def _navigator_done(self, status, result):
        self.loginfo("Navigator Result : %s, Message : %s"%(result.success,result.message)) 
        
        if result.success == False:
            self.play_sound(self._navi_failed_sound)
            self._current_state = STATE_RESET
        else:
            self._navigator_finished = True
        
    def _navigator_feedback(self, feedback):
        self._navigator_feed = str("Distance : %s, Remain Time : %s, Message : %s"%(str(feedback.distance),str(feedback.remain_time),str(feedback.message)))
        #self.loginfo("Navigator : " + str(self._navigator_feed))
        
        if feedback.status == yocs_msgs.NavigateToFeedback.STATUS_RETRY:
            self.play_sound(self._retry_sound)


    def _state_in_dock(self):
        if self._delivery_order_received:
            self._delivery_order_received = False
            self._order_in_progress = True
            self._current_state = STATE_WAKEUP

    def _state_wakeup(self):
        if not self._dock_interactor_requested:
            goal = yocs_msgs.DockingInteractorGoal()
            goal.command = yocs_msgs.DockingInteractorGoal.WAKE_UP
            goal.distance = 0.8
            self._ac[DOC_ACTION].send_goal(goal, done_cb=self._dock_interactor_done)
            self._dock_interactor_requested = True
            self.loginfo("Wake up!")

        if self._dock_interactor_finished:
            self._dock_interactor_finished = False
            self._dock_interactor_requested = False
            self._current_state = STATE_LOCALISE
            
    def _dock_interactor_done(self, status, result):
        self.loginfo("Docking Interactor result : %s, Message : %s"%(result.success,result.message))

        if result.success == False:
            self.play_sound(self._retry_sound)
            self._current_state = STATE_RESET
        else:
            self._dock_interactor_finished = True

    def _state_localise(self):
        if not self._localise_requested:
            self._localised = False
            goal = yocs_msgs.LocalizeGoal()
            goal.command = yocs_msgs.LocalizeGoal.STAND_AND_LOCALIZE
            self._ac[LOC_ACTION].send_goal(goal, done_cb=self._localize_done)
            self.loginfo('Localisation Request sent')
            self._localise_requested = True

        if self._localised:
            self.loginfo('Robot localised')
            self.loginfo('Register Dock in the global frame')
            self._current_state = STATE_REGISTER_DOCK
            
    def _localize_done(self, status, result):
        self.loginfo("Localize result : %s, Message : %s"%(result.success,result.message))

        if result.success:
            self._localised = True 
        else:
            self._current_state = STATE_RESET

    def _state_register_dock(self):
        if not self._dock_interactor_requested:
            goal = yocs_msgs.DockingInteractorGoal()
            goal.command = yocs_msgs.DockingInteractorGoal.REGISTER_DOCK_IN_GLOBAL_FRAME
            goal.distance = 0.5
            self._ac[DOC_ACTION].send_goal(goal, done_cb=self._dock_interactor_done)
            self._dock_interactor_requested = True

        if self._dock_interactor_finished:
            self._dock_interactor_requested = False
            self._dock_interactor_finished = False
            self.loginfo('Dock has been registered in global frame')
            self._led_controller.set_on_ok()

            self._current_state = STATE_GOTO_PICKUP
            #self._current_state = STATE_BACKTO_BASE

    def  _state_goto_pickup(self):
        if not self._navigator_requested:
            self.play_sound(self._order_received_sound)
            self._request_navigator(self._pickup_location, yocs_msgs.NavigateToGoal.APPROACH_ON, self._nav_retry, self._nav_pickup_timeout, 0.0)
            self._navigator_requested = True

        if self._navigator_finished:
            self._navigator_requested = False
            self.loginfo('At pickup')
        
            self._current_state = STATE_AT_PICKUP
            # play_sound at pickup
            self.play_sound(self._at_pickup_sound)
    
    def _state_at_pickup(self):
        # Wait for pickup's confirmation
        if self._pickup_confirm== True:
            self._pickup_confirm = False
            self.play_sound(self._confirm_sound)

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
            self.play_sound(self._at_table_sound)
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
            self.play_sound(self._enjoy_meal_sound)

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
                feedback = simple_delivery_msgs.RobotDeliveryOrderFeedback()
                feedback.delivery_status = simple_delivery_msgs.DeliveryStatus()
                feedback.delivery_status.status = simple_delivery_msgs.DeliveryStatus.COMPLETE_ALL_DELIVERY
                feedback.delivery_status.order_id = self._delivery_order_id
                feedback.delivery_status.target_goal= self._target_location
                self._deliver_order_handler.publish_feedback(feedback)
                self._current_state = STATE_BACKTO_BASE

    def _state_backto_base(self):
        if not self._dock_interactor_requested:
            goal = yocs_msgs.DockingInteractorGoal()
            goal.command = yocs_msgs.DockingInteractorGoal.RETURN_TO_DOCK
            goal.distance = 0.5
            self._ac[DOC_ACTION].send_goal(goal, done_cb=self._dock_interactor_done)
            self._dock_interactor_requested = True
            self.loginfo("Returning back to base!")

        if self._dock_interactor_finished:
            self._dock_interactor_finished = False
            self._dock_interactor_requested = False
            self._current_state = STATE_IN_DOCK
            self._order_in_progress = False
            message = 'Delivery Success!'

            r = simple_delivery_msgs.RobotDeliveryOrderResult()
            r.order_id = self._delivery_order_id
            r.message = message
            r.success = True
            self._deliver_order_handler.set_succeeded(r)
            self.loginfo("Done!!!")

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
        self._ac[NAV_ACTION].cancel_all_goals()
        self._ac[DOC_ACTION].cancel_all_goals()
        self._ac[LOC_ACTION].cancel_all_goals()
        self._init_variables()
        self.play_sound(self._reset_sound)
        self._current_state = STATE_ON_ERROR

    def _state_call_autodock(self):
        if not self._dock_interactor_requested:
            goal = yocs_msgs.DockingInteractorGoal()
            goal.command = yocs_msgs.DockingInteractorGoal.CALL_AUTODOCK
            self._ac[DOC_ACTION].send_goal(goal, done_cb=self._dock_interactor_done)
            self._dock_interactor_requested = True
            self.loginfo("Calling auto dock!")

        if self._dock_interactor_finished:
            self._dock_interactor_finished = False
            self._dock_interactor_requested = False
            self._current_state = STATE_IN_DOCK
            self.loginfo("Done!!!")








    def play_sound(self, sound):
        play_sound(self._resource_path, sound, self._volume)
