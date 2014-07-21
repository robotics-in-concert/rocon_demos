#!/usr/bin/env python
#
# License: BSD
#   https://raw.github.com/robotics-in-concert/rocon_demos/license/LICENSE
#

import rospy
import realrobotshow_ctrl 

if __name__ == '__main__':
  rospy.init_node('delivery_robot_manager')
  state_manager = realrobotshow_ctrl.StateManager()
  state_manager.spin()

