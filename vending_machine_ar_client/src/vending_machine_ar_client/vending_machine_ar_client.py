#
# License: BSD
#   https://raw.github.com/robotics-in-concert/rocon_demos/license/LICENSE
#

import actionlib
import actionlib_msgs.msg as actionlib_msgs
import ar_track_alvar.msg as ar_track_alvar_msgs
import rospy
import vending_machine_msgs.msg as vending_machine_msgs
from vending_machine_control import utils
import std_msgs.msg as std_msgs

class VendingMachineARClient(object):
    """
        Client for vending machine manager processing orders using AR markers
        
        Each recognised marker is turned into one order (action goal)
    """

    def __init__(self):
        '''
            Action interface
        '''
        action_server_name = 'vending_machine_manager/drink_ordering'
        self._client = actionlib.SimpleActionClient(action_server_name,
                                                   vending_machine_msgs.DrinkOrderAction)
        if not self._client.wait_for_server(rospy.Duration(2.0)):
            raise EnvironmentError("Couldn't not connect to vending machine manager ('" + action_server_name + "')")

        self._goal_sent = False
        self._ready_for_next_order = False
        self._time_last_order_processed = rospy.Time.now()
        self._sub_marker = rospy.Subscriber('ar_pose_marker', ar_track_alvar_msgs.AlvarMarkers, self._ARMarkerCB)
        self._order_idle_time = rospy.Duration(rospy.get_param("~order_idle_time", 1.0))

    def _ARMarkerCB(self, msg):
        '''
            parse marker message and prepare a goal
        '''
        if self._client and not self._goal_sent:
            if (rospy.Time.now() - self._time_last_order_processed) > self._order_idle_time:
                if len(msg.markers) > 0:
                    goal = vending_machine_msgs.DrinkOrderGoal()
                    for marker in msg.markers:
                        drink_type = vending_machine_msgs.DrinkType()
                        if marker.id == vending_machine_msgs.DrinkType.COKE:
                            drink_type.drink_type = vending_machine_msgs.DrinkType.COKE
                        elif marker.id == vending_machine_msgs.DrinkType.CIDER:
                            drink_type.drink_type = vending_machine_msgs.DrinkType.CIDER
                        elif marker.id == vending_machine_msgs.DrinkType.MAX:
                            drink_type.drink_type = vending_machine_msgs.DrinkType.MAX
                        else:
                            rospy.logwarn("Unknown drink ID '" + str(marker.id) + "'. Skipping order.")
                            return
                        goal.drink_types.append(drink_type)
                        goal.drink_amounts.append(1)
                        rospy.loginfo("Added drink '" + utils.getDrinkName(drink_type.drink_type) + "' to order.")
                    self._client.send_goal(goal)
                    self._goal_sent = True
                else:
                    rospy.logdebug("Received empty marker list.")
            else:
                rospy.logdebug("Waiting a bit before processing next order.")
        else:
            rospy.logdebug("Vending machine client not yet connected or ready.")

    def spin(self):
        while not rospy.is_shutdown():
            if self._goal_sent:
                if self._client.get_state() == actionlib_msgs.GoalStatus.SUCCEEDED:
                    self._time_last_order_processed = rospy.Time.now()
                    self._goal_sent = False
                    rospy.loginfo("AR ordering client: Order processed.")
            rospy.sleep(0.5)
