#!/usr/bin/env python
#
# License: BSD
#   https://raw.github.com/robotics-in-concert/concert_apps/license/LICENSE
#

import rospy
import vending_machine_control

if __name__ == '__main__':
  rospy.init_node('vending_machine_control')
  vm = vending_machine_control.VendingMachine()
  vm.spin()
