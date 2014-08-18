#!/usr/bin/env python
#
# License: BSD
#   https://raw.github.com/robotics-in-concert/rocon_demos/license/LICENSE
#

import rospy
import cafe_devices_manager

if __name__ == '__main__':

    rospy.init_node('cafe_hue_manager')
    manager = cafe_devices_manager.HueManager()
    manager.spin()
