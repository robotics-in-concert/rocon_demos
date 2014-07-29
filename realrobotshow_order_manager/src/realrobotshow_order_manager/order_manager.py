#!/usr/bin/env python
#
# License: BSD
#   https://raw.github.com/robotics-in-concert/rocon_demos/license/LICENSE
#

import rospy
import actionlib

import simple_delivery_msgs.msg

class OrderManager(object):

    def __init__(self): 
        self.as_name = 'kitchen_order'
        self.ac_name = 'deliver_order'
        self._as = actionlib.SimpleActionServer(self.as_name, 
                                                          simple_delivery_msgs.msg.DeliverOrderAction, 
                                                          execute_cb=self.execute_cb, 
                                                          auto_start = False)
        self._as.start()
        self.ac = actionlib.SimpleActionClient(self.ac_name, simple_delivery_msgs.msg.DeliverOrderAction)

    def execute_cb(self, goal):
        self.loginfo('execute_cb')
        self.loginfo(goal)
        deliver_goal = simple_delivery_msgs.msg.DeliverOrderGoal(location = str(goal.location))
        self.ac.send_goal(deliver_goal, done_cb = self.done_cb, feedback_cb = self.feedback_cb)
        self.loginfo('robot delivery service start!!!')
        self.ac.wait_for_result()


    def feedback_cb(self, data):
        #self.loginfo(data.status)
        feedback = simple_delivery_msgs.msg.DeliverOrderFeedback()
        feedback.status = data.status
        self._as.publish_feedback(data)

    def done_cb(self, msg, result):
        self.loginfo('done_cb')
        self.loginfo('result success: %s' % result.success)
        self.loginfo('result message: %s' % result.message)

        result = simple_delivery_msgs.msg.DeliverOrderResult()
        result.message = result.message
        result.success = result.success
        self._as.set_succeeded(result)

    def update(self):
        self.loginfo('update')

    def spin(self):
        # Publishes the empty latch topic
        while not rospy.is_shutdown():
            rospy.sleep(30)

    def loginfo(self, msg):
        rospy.loginfo('Order Manager : ' + str(msg))

    def logwarn(self, msg):
        rospy.logwarn('Order Manager : ' + str(msg))
