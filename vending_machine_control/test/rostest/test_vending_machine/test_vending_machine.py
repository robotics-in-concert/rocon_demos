#!/usr/bin/env python
#
# License: BSD
#   https://raw.github.com/robotics-in-concert/concert_apps/license/LICENSE
#

import sys
import actionlib
import rospy
import rostest
import unittest
import vending_machine_control.msg as vending_machine_msgs


class TestVendingMachine(unittest.TestCase):
    ## test 1 == 1
    def test_order(self):
        client = actionlib.SimpleActionClient('vending_machine_manager/drink_ordering',
                                              vending_machine_msgs.DrinkOrderAction)
        assert client.wait_for_server(rospy.Duration(5.0))

        goal = vending_machine_msgs.DrinkOrderGoal()
        drink_type = vending_machine_msgs.DrinkType()
        drink_type.drink_type = vending_machine_msgs.DrinkType.COKE
        goal.drink_types.append(drink_type)
        goal.drink_amounts.append(2)
        drink_type = vending_machine_msgs.DrinkType()
        drink_type.drink_type = vending_machine_msgs.DrinkType.CIDER
        goal.drink_types.append(drink_type)
        goal.drink_amounts.append(1)
        drink_type = vending_machine_msgs.DrinkType()
        drink_type.drink_type = vending_machine_msgs.DrinkType.MAX
        goal.drink_types.append(drink_type)
        goal.drink_amounts.append(1)
        client.send_goal(goal)

        assert client.wait_for_result(rospy.Duration(10.0))

        print client.get_result()

if __name__ == '__main__':
    rospy.init_node('test_vending_machine', anonymous=True)
    rostest.unitrun('vending_machine_control', 'test_vending_machine', TestVendingMachine)
