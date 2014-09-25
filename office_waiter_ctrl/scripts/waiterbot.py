#!/usr/bin/env python
#
# License: BSD
#   https://raw.github.com/robotics-in-concert/rocon_demos/license/LICENSE
#

import rospy
import office_waiter_ctrl 

if __name__ == '__main__':
    rospy.init_node('office_waiterbot')
    state_manager = office_waiter_ctrl.StateManager()
    state_manager.loginfo("Initialized")
    state_manager.spin()
    state_manager.loginfo("Bye Bye")
