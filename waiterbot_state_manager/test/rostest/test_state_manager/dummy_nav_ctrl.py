#!/usr/bin/env python
#
# License: BSD
#   https://raw.github.com/robotics-in-concert/rocon_demos/license/LICENSE
#

import rospy
import waiterbot_msgs.msg as waiterbot_msgs

class DummyNavCtrl(object):
    """
        Waiterbot navigation control simulation
    """
    def __init__(self):
        self._sub_nav_ctrl_goal = rospy.Subscriber('waiterbot_nav_control/goto', waiterbot_msgs.NavCtrlGoTo,
                                                   self._navCtrlGoToCB)
        self._pub_nav_ctrl_status = rospy.Publisher('waiterbot_nav_control/status', waiterbot_msgs.NavCtrlStatus,
                                                    latch=True)
        self._nav_goal = None
        self._nav_time = rospy.Duration(rospy.get_param("nav_time", 2.0))

    def _navCtrlGoToCB(self, msg):
        if msg.goal == waiterbot_msgs.NavCtrlGoTo.GO_TO_VM:
            self._nav_goal = waiterbot_msgs.NavCtrlGoTo.GO_TO_VM
            rospy.loginfo("DummyNavCtrl: Received order to go to the vending machine.")
        elif msg.goal == waiterbot_msgs.NavCtrlGoTo.GO_TO_ORIGIN:
            self._nav_goal = waiterbot_msgs.NavCtrlGoTo.GO_TO_ORIGIN
            rospy.loginfo("DummyNavCtrl: Received order to go to the origin.")

    def spin(self):
        while not rospy.is_shutdown():
            if self._nav_goal:
                rospy.loginfo("DummyNavCtrl: Moving to goal (waiting time = " + str(self._nav_time.to_sec()) + ").")
                rospy.sleep(self._nav_time)
                msg = waiterbot_msgs.NavCtrlStatus()
                if self._nav_goal == waiterbot_msgs.NavCtrlGoTo.GO_TO_VM:
                    msg.status_code = waiterbot_msgs.NavCtrlStatus.VM_ARRIVAL
                    rospy.loginfo("DummyNavCtrl: Arrived at the vending machine.")
                else:
                    msg.status_code = waiterbot_msgs.NavCtrlStatus.ORIGIN_ARRIVAL
                    rospy.loginfo("DummyNavCtrl: Arrived at the origin.")
                self._pub_nav_ctrl_status.publish(msg)
                self._nav_goal = None
                rospy.sleep(0.1)
            else:
                rospy.loginfo("DummyNavCtrl: Idling.")
                rospy.sleep(1.0)

if __name__ == '__main__':
  rospy.init_node('dummy_nav_ctrl')
  nav_ctrl = DummyNavCtrl()
  nav_ctrl.spin()
