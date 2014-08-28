#!/usr/bin/env python
#
# License: BSD
#   https://raw.github.com/robotics-in-concert/rocon_demos/license/LICENSE
#

import rospy
import office_hue_manager

if __name__ == '__main__':

    rospy.init_node('office_hue_manager')
    manager = office_hue_manager.HueManager()
    manager.spin()
