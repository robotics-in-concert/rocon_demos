#!/usr/bin/env python
#
# License: BSD
#   https://raw.github.com/robotics-in-concert/rocon_demos/license/LICENSE
#

import rospy
import waiterbot_state_manager

if __name__ == '__main__':
  rospy.init_node('waiterbot_state_manager')
  state_manager = waiterbot_state_manager.StateManager()
  state_manager.spin()
