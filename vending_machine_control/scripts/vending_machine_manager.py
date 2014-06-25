#!/usr/bin/env python
#
# License: BSD
#   https://raw.github.com/robotics-in-concert/rocon_demos/license/LICENSE
#

import rospy
import vending_machine_control

if __name__ == '__main__':
  rospy.init_node('vending_machine_manager')
  vm_manager = vending_machine_control.VendingMachineManager()
  vm_manager.spin()
