#!/usr/bin/env python
#
# License: BSD
#   https://raw.github.com/robotics-in-concert/rocon_demos/license/LICENSE
#

import rospy
import ces_dummy_scripts

if __name__ == '__main__':
    rospy.init_node('dummy_ces_waiter_node')
    dummy_waiter = ces_dummy_scripts.DummyWaiter() 
    dummy_waiter.spin()
