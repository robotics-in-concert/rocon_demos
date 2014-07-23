#!/usr/bin/env python
#
# License: BSD
#   https://raw.github.com/robotics-in-concert/rocon_demos/license/LICENSE
#

import rospy
import actionlib

import simple_delivery_msgs.msg

class KitchenFrontend(object):

    def __init__(self): 
        self.ac = actionlib.SimpleActionClient('kitchen_order', 
                                                          simple_delivery_msgs.msg.DeliverOrderAction)

    def kitchen_order(self, order_location):
        self.goal = simple_delivery_msgs.msg.DeliverOrderGoal(location = str(order_location))
        self.ac.send_goal(self.goal, done_cb = self.done_cb, feedback_cb = self.feedback_cb)
        self.loginfo('kitchen_order')

    def feedback_cb(self, data):
        self.loginfo('feedback_cb')
        self.loginfo(data)

    def done_cb(self, data, data2):
        self.loginfo('done_cb')
        self.loginfo(data)
        self.loginfo(data2)

    def update(self):
        self.loginfo('update')

    def spin(self):
        # Publishes the empty latch topic
        self.ac.wait_for_server()
        self.kitchen_order(3)
        self.ac.wait_for_result()
        

    def loginfo(self, msg):
        rospy.loginfo('Kitchen Frontend : ' + str(msg))

    def logwarn(self, msg):
        rospy.logwarn('Kitchen Frontend : ' + str(msg))


if __name__ == '__main__':

    rospy.init_node('dummy_kitchen_frontend')

    kitchen = KitchenFrontend()

    kitchen.loginfo('Initialized')
    kitchen.spin()
    kitchen.loginfo('Bye Bye')