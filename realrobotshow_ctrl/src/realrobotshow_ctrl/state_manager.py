#!/usr/bin/env python
#
# License: BSD
#   https://raw.github.com/robotics-in-concert/rocon_demos/license/LICENSE
#
import rospy
import simple_delivery_msgs
import kobuki_msgs
import actionlib

import .utils

STATE_INITIALIZATION = 'Initialization'
STATE_GOTO_KITCHEN   = 'GOTO_KITCHEN'
STATE_AT_KITCHEN     = 'AT_KITCHEN'
STATE_GOTO_TABLE     = 'GOTO_TABLE'
STATE_AT_TABLE       = 'AT_TABLE'
STATE_ERROR          = 'ERROR'

# INIT
# GOTO KITCHEN
# AT_KITCHEN
# GOTO_TABLE
# AT_TABLE
# ERROR

class StateManager(object):
    
    _kitchen_action_name = 'deliver_order'

    def __init__(self):
        self._init_variables()
        self._init_handles()

    def _init_states(self):
        self._states[STATE_INITIALIZATION] = self._state_initialization
        self._states[STATE_GOTO_KITCHEN] = self._state_goto_kitchen
        self._states[STATE_AT_KITCHEN] = self._state_at_kitchen
        self._states[STATE_GOTO_TABLE] = self._state_goto_table
        self._states[STATE_AT_TABLE]   = self._state_at_table
        self._states[STATE_ERROR]      = self._state_on_error

    def _init_variables(self):
        self._current_state = None
        self._initialized = False
        self._previous_button = None  
        self._init_requested = False

    def _init_handles(self):
        # order handle
        self._deliver_order_handler = actionlib.SimpleActionServer(self._kitchen_action_name, simple_delivery_msgs.msg.DeliverOrderAction, execute_cb=self._process_delver_order, auto_start=False)

        self._sub = {}
        self._pub = {}
        
        # Button
        self._sub['digital_inputs'] = rospy.Subscriber('~digital_inputs', kobuki_msgs.DigitalInputEvent, self._process_button)  # Waiterbot buttons.

        # Localize manager
        self._pub['localize'] = rospy.Publisher('~localize', std_msgs.Empty)
        self._sub['localized'] = rospy.Subscriber('~localized', std_msgs.Empty, self._process_localized)

        # semantic navigation handler
        self._navigator_handler = actionlib.SimpleActionClient('~navigator', yocs_msgs.NavigateTo)

        self.loginfo('Wait for Sematic Navigator Server to be up')
        self._navigator_handler.wait_for_server()

    def _process_button(self, msg):
        # 0 = GREEN 1 = RED

        if not self._process_button:
            self._previous_button = copy.deepcopy(msg)
            return

        green, red = check_button_event(self._previous_button, msg)

        if green:
            if not self._current_state:
                self._current_state = STATE_INITIALIZATION

    def _process_localized(self, msg): 
        self._initialized = True
        
    def _process_delver_order(self, goal):
        self.loginfo('Received Goal ' + str(goal))
        r = simple_delivery_msgs.DeliverOrderResult()

        if self._current_state != STATE_AT_KITCHEN
            message = 'Robot is not at kitchen. Ignore the order!'
            self.logwarn(message)

            r = simple_delivery_msgs.DeliverOrderResult()
            r.message = message
            r.success = False
            self._deliver_order_handler.set_succeeded(r)

        rospy.sleep(2)
        r.message = 'Not Yet Implemented'
        r.success = False
        self._deliver_order_handler.set_succeeded(r)

        # request semantic navigator to go requested table
        # self._current_state = STATE_GOTO_TABLE

    def spin(self):
        r = rospy.Rate(10)
        self._deliver_order_handler.start()

        while not rospy.is_shutdown():
            self._states[self._current_state]()
            self._logging()
            r.sleep()

    def _logging(self):
        self.loginfo(self._current_state)
                
    def loginfo(self, msg):
        rospy.loginfo('Robot State Manager : ' + str(msg))

    def _state_initialization(self):
        if not self._init_requested:
            self._initialized = False
            self._pub['localize'].publish() 
            self.loginfo('Localization Request sent')
            self._init_requested = True
    
        if _initialized:
            self.loginfo('Robot Localized')
            self.loginfo('Moving To kitchen')

            # Request navigator to go kitchen

            self._current_state = STATE_GOTO_KITCHEN
            self._init_requested = False

    def _state_goto_kitchen(self):
        # Wait for arriving
        # When it arrives...
        self._current_state = STATE_KITCHEN

    def _state_at_kitchen(self):
        # Wait for order
        # Delivery Order Action will change the state
        pass

    def _state_goto_table(self):
        # Wait for arriving
        # When it arrives...
        self._current_state = STATE_AT_TABLE

    def _state_at_table(self):
        # Wait for Customer's confirmation

    def _state_on_error(self):
        # When it fails while navigation....
