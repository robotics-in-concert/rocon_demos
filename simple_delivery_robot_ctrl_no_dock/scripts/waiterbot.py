#!/usr/bin/env python
#
# License: BSD
#   https://raw.github.com/robotics-in-concert/rocon_demos/license/LICENSE
#

import rospy
import simple_delivery_robot_ctrl_no_dock 

if __name__ == '__main__':
    rospy.init_node('simple_delivery_robot_ctrl_no_dock')
    state_manager = simple_delivery_robot_ctrl_no_dock.StateManager()
    state_manager.loginfo("Initialized")
    state_manager.spin()
    state_manager.loginfo("Bye Bye")
