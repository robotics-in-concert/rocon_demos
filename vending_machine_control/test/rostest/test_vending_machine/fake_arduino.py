#!/usr/bin/env python
#
# License: BSD
#   https://raw.github.com/robotics-in-concert/rocon_demos/license/LICENSE
#

import rospy
import std_msgs.msg as std_msgs

class FakeArduino(object):
    """
        Fake Arduino - simulating the low-level VM control
    """
    def __init__(self):
        self._drink_dispensed = True
        self._sub_drink_order = rospy.Subscriber("~drink_order", std_msgs.Int8, self._orderCB)
        self._pub_order_result = rospy.Publisher("~order_result", std_msgs.Int8)

        self._vm_dispensing_time = rospy.get_param('~vm_dispensing_time', 4.0)
        self._drink_order = -1

    def _orderCB(self, msg):
        if msg.data == 1:
            self._drink_order = 1;
        elif msg.data == 2:
            self._drink_order = 2;
        else:
            self._drink_order = -1;
        self._drink_dispensed = True;

    def spin(self):
        while not rospy.is_shutdown():
            if self._drink_dispensed:
                rospy.sleep(self._vm_dispensing_time)
                order_result_msg = std_msgs.Int8()
                order_result_msg.data = self._drink_order;
                self._pub_order_result.publish(order_result_msg)
                self._drink_dispensed = False
            rospy.sleep(1.0)

if __name__ == '__main__':
  rospy.init_node('vending_machine')
  vm = FakeArduino()
  vm.spin()
