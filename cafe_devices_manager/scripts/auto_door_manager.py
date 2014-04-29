#!/usr/bin/env python
#
# License: BSD
#   https://raw.github.com/robotics-in-concert/rocon_demos/license/LICENSE
#

import rospy
import cafe_devices_manager

if __name__ == '__main__':

    rospy.init_node('cafe_auto_door_manager')
    manager = cafe_devices_manager.AutoDoorManager()
    manager.set_table_id(rospy.get_param('~table_id',1))
    manager.spin()
