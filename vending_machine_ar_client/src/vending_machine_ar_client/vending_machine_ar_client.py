#
# License: BSD
#   https://raw.github.com/robotics-in-concert/rocon_demos/license/LICENSE
#

import actionlib
import actionlib_msgs.msg as actionlib_msgs
import ar_track_alvar.msg as ar_track_alvar_msgs
import rospy
import vending_machine_control.msg as vending_machine_msgs
import std_msgs.msg as std_msgs

class VendingMachineARClient(object):
    """
        Client for vending machine manager processing orders using AR markers
        
        Each recognised marker is turned into one order (action goal)
    """
    _client = None
    _goal_sent = False
    _last_order = None
    _ready_for_next_order = False
    ''' idle time in between orders to avoid multiple triggers of the same order '''
    _order_idle_time = rospy.Duration(1.0)
    _time_last_order_processed = None

    def __init__(self):
        '''
            Action interface
        '''
        action_server_name = 'vending_machine_manager/drink_ordering'
        self._client = actionlib.SimpleActionClient(action_server_name,
                                                   vending_machine_msgs.DrinkOrderAction)
        if not self._client.wait_for_server(rospy.Duration(2.0)):
            raise EnvironmentError("Couldn't not connect to vending machine manager ('" + action_server_name + "')")

        self._time_last_order_processed = rospy.Time.now()
        self._sub_marker = rospy.Subscriber('ar_pose_marker', ar_track_alvar_msgs.AlvarMarkers, self._ARMarkerCB)

    def _ARMarkerCB(self, msg):
        '''
            parse marker message and prepare a goal
        '''
        if self._client and not self._goal_sent:
            if (rospy.Time.now() - self._time_last_order_processed) > self._order_idle_time:
                if len(msg.markers) > 0:
                    goal = vending_machine_msgs.DrinkOrderGoal()
                    for marker in msg.markers:
                        if marker.id != 0:
                            drink_type = vending_machine_msgs.DrinkType()
                            if marker.id == vending_machine_msgs.DrinkType.COKE:
                                drink_type.drink_type = vending_machine_msgs.DrinkType.COKE
                            elif marker.id == vending_machine_msgs.DrinkType.CIDER:
                                drink_type.drink_type = vending_machine_msgs.DrinkType.CIDER
                            elif marker.id == vending_machine_msgs.DrinkType.MAX:
                                drink_type.drink_type = vending_machine_msgs.DrinkType.MAX
                            else:
                                rospy.logerror("Unknown drink ID '" + str(msg.id) + "'. Aborting order!")
                                return
                        else:
                            rospy.logwarn("Invalid drink ID (id = 0). Discarding message.")
                            return
                        goal.drink_types.append(drink_type)
                        goal.drink_amounts.append(1)
                    self._client.send_goal(goal)
                    self._goal_sent = True
                else:
                    rospy.logdebug("Received empty marker list.")
            else:
                rospy.logdebug("Waiting a bit before processing next order.")
        else:
            rospy.logwarn("Vending machine client not yet connected.")

    def spin(self):
        while not rospy.is_shutdown():
            if self._goal_sent:
                if self._client.get_state() == actionlib_msgs.GoalStatus.SUCCEEDED:
                    self._time_last_order_processed = rospy.Time.now()
                    self._goal_sent = False
            rospy.sleep(0.5)
