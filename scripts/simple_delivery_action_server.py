#!/usr/bin/env python
import rospy
import actionlib
import threading
import random
import time

# ros msg
import simple_delivery_msgs.msg as simple_delivery_msgs


class SimpleDeliveryActionServer(object):

    def __init__(self):
        self.simple_as_handler = actionlib.SimpleActionServer('simple_delivery_order',
                                                              simple_delivery_msgs.RobotDeliveryOrderAction,
                                                              auto_start=False)
        self.simple_as_handler.register_goal_callback(self._process_deliver_order)
        self.simple_as_handler.register_preempt_callback(self._process_deliver_order_preempt)

    def _process_deliver_order(self):
        goal = self.simple_as_handler.accept_new_goal()
        rospy.loginfo("SimpleDeliveryActionServer: " + str(goal))

        r = simple_delivery_msgs.RobotDeliveryOrderResult()
        r.message = "Received Goal and Return Result"
        r.success = True
        self.simple_as_handler.set_succeeded(r)

    def _process_deliver_order_preempt(self):
        pass

    def spin(self):
        self.simple_as_handler.start()
        while not rospy.is_shutdown():
            rospy.sleep(0.2)

if __name__ == '__main__':
    try:
        # Initialize ros node
        rospy.init_node('simple_delivery_action_server')

        _as = SimpleDeliveryActionServer()
        rospy.loginfo('Initialized')
        _as.spin()
        rospy.loginfo("Bye Bye")

    except rospy.ROSInterruptException:
        pass
