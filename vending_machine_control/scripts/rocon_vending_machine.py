#!/usr/bin/env python
#
# License: BSD
#   https://raw.github.com/robotics-in-concert/concert_apps/license/LICENSE
#
##############################################################################
# Imports
##############################################################################

import rospy
import rocon_vending_machine

##############################################################################
# Main
##############################################################################

if __name__ == '__main__':

  rospy.init_node('rocon_vending_machine')
  vm = rocon_vending_machine.VendingMachine()
  vm.spin()
