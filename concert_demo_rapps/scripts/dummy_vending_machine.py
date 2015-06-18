#!/usr/bin/env python
import rospy
import std_msgs.msg as std_msgs

class VendingMachineManagerSim(object):

    def __init__(self):
        self._sub_drink_order = rospy.Subscriber('/drink_order', std_msgs.Int8, self._process_drink_order)
        self._pub_order_result = rospy.Publisher('/order_result', std_msgs.Int8, queue_size=10)

    def _process_drink_order(self, msg):
        self.loginfo('Received order %s'%str(msg))
        rospy.sleep(2.0)
        self.loginfo('Return True always')
        self._pub_order_result(msg)

    def loginfo(self, msg):
        rospy.loginfo('VM Sim : %s'%str(msg))

    def spin(self):
        rospy.spin()

if __name__ == '__main__':
    rospy.init_node('vending_machine_sim')
    vm = VendingMachineManagerSim()
    vm.spin()
