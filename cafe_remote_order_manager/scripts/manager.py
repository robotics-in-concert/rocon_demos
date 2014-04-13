#!/usr/bin/env python
#
# License: BSD
#   https://raw.github.com/robotics-in-concert/rocon_demos/license/LICENSE
#

import rospy
import cafe_remote_order_manager


if __name__ == '__main__':

    rospy.init_node('cafe_remote_order_manager')

    manager = cafe_remote_order_manager.RemoteOrderManager()

    manager.loginfo('Initialized')
    manager.spin()
    manager.loginfo('Bye Bye')
