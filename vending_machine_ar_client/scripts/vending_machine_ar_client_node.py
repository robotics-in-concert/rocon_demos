#!/usr/bin/env python
#
# License: BSD
#   https://raw.github.com/robotics-in-concert/rocon_demos/license/LICENSE
#

import rospy
import vending_machine_ar_client

if __name__ == '__main__':
  rospy.init_node('vending_machine_ar_client')
  vm_client = vending_machine_ar_client.VendingMachineARClient()
  vm_client.spin()
