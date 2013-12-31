#!/usr/bin/env python
#
# License: BSD
#   https://raw.github.com/robotics-in-concert/rocon_demos/license/LICENSE
#

import rospy
import ces_dummy_scripts

if __name__ == '__main__':
    rospy.init_node('dummy_waiter')

    d = ces_dummy_scripts.DummyWaiter()
    rospy.loginfo("Waiter : Initialized")
    d.spin()

