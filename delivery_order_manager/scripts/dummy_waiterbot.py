#!/usr/bin/env python
#
# License: BSD
#   https://raw.github.com/robotics-in-concert/rocon_demos/license/LICENSE
#

#system
import random
#ros
import rospy
import actionlib
#ros message
import simple_delivery_msgs.msg

class Waiterbot(object):

    def __init__(self): 
        self.as_name = 'deliver_order'
        self._as = actionlib.SimpleActionServer(self.as_name, 
                                                        simple_delivery_msgs.msg.DeliverOrderAction, 
                                                        execute_cb=self.execute_cb, 
                                                        auto_start = False)
        self._as.start()

    def execute_cb(self, goal):
        self.loginfo('execute_cb')
        self.loginfo("table is %s" % str(goal.location))
        
        for k in range(1, 5):
            feedback = simple_delivery_msgs.msg.DeliverOrderFeedback()
            feedback.status = 'robot status is %s' % str(k)
            self._as.publish_feedback(feedback)
            self.loginfo("send feed back: %s" % feedback.status)
            rospy.sleep(1)

        result = simple_delivery_msgs.msg.DeliverOrderResult()
        result.message = "delivery over"
        result.success = True
        self._as.set_succeeded(result)

    def spin(self):
        # Publishes the empty latch topic
        while not rospy.is_shutdown():
            rospy.sleep(30)

    def loginfo(self, msg):
        rospy.loginfo('Waiterbot : ' + str(msg))

    def logwarn(self, msg):
        rospy.logwarn('Waiterbot : ' + str(msg))


if __name__ == '__main__':

    rospy.init_node('dummy_waiterbot')
    waiterbot = Waiterbot()
    waiterbot.loginfo('Initialized')
    waiterbot.spin()
    waiterbot.loginfo('Bye Bye')
