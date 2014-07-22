#!/usr/bin/env python
#
# License: BSD
#   https://raw.github.com/robotics-in-concert/rocon_demos/license/LICENSE
#

import rospy
import delivery_order_manager


if __name__ == '__main__':

    rospy.init_node('delivery_order_manager')

    manager = delivery_order_manager.OrderManager()

    manager.loginfo('Initialized')
    manager.spin()
    manager.loginfo('Bye Bye')
