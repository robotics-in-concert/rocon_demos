#!/usr/bin/env python
#
# License: BSD
#   https://raw.github.com/robotics-in-concert/rocon_demos/license/LICENSE
#

import rospy
import dummy_ces_tablet

if __name__ == '__main__':
    rospy.init_node('dummy_ces_tablet_node')
    dummy_ces_tablet = dummy_ces_tablet.DummyTablet() 
    dummy_ces_tablet.spin()
