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
STATE_READY          = 'Ready'
STATE_ON_DELIVERY    = 'ON_DELIVERY'
STATE_ERROR          = 'ERROR'

# INIT
# GOTO KITCHEN
# READY
# ON_SERVING
# ERROR

class StateManager(object):
    
    _kitchen_action_name = 'deliver_order'

    def __init__(self):
        self._init_variables()
        self._init_handles()

    def _init_variables(self):
        self._state = None
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

        if self._state == STATE_INITIALIZATION:
            if green:
                self._state_initialization()

    def _process_localized(self, msg): 
        self._initialized = True
        


    def _process_delver_order(self, goal):
        self.loginfo('Received Goal ' + str(goal))

    def spin(self):

        r = rospy.Rate(10)
        while not rospy.is_shutdown():
            if self._state == STATE_INITIALIZATION:
                self._state_initialization()
            elif self._state == STATE_GOTO_KITCHEN:
                self._state_goto_kitchen()
            elif self._state == STATE_READY:
                self._state_ready()


            r.sleep()
                
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
            self._state = STATE_GOTO_KITCHEN
            self._init_requested = False

    def _state_goto_kitchen(self):

        # Request Semantic Location Navigator To go Kitchen
        self.loginfo('Moving To kitchen')
        
        # When it arrives...
        self._state = STATE_READY

    def _state_ready(self):
        self.loginfo('Ready to serve')
