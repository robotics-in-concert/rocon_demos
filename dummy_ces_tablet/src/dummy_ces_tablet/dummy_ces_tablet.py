#!/usr/bin/env python
#
# License: BSD
#   https://raw.github.com/robotics-in-concert/rocon_demos/license/LICENSE
#

import rospy
import waiterbot_msgs.msg 
import std_srvs.srv 

class DummyTablet(object):
    def __init__(self):
        self._srv_start = rospy.Service('start_order', std_srvs.srv.Empty, self.process_start_service)
        self._pub_drink_order = rospy.Publisher('drink_order', waiterbot_msgs.msg.DrinkOrder) 
        self._sub_drink_order_feedback = rospy.Subscriber('drink_order_feedback',waiterbot_msgs.msg.DrinkOrderFeedback, self.process_drink_order_feedback)

    def process_start_service(self, req):
        
        #  send go to vm command
        rospy.loginfo("Sending goto VM command")
        self.send_command(1)
            
        #  wait for vm arrival feedback
        rospy.loginfo("Waiting for feedback message")
        self.wait_for_feedback(waiterbot_msgs.msg.DrinkOrderFeedback.VM_ARRIVAL)

        #  send go to origin command
        rospy.loginfo("Sending goto origin command")
        self.send_command(2)

        #  wait for origin arrival feedback
        rospy.loginfo("Waiting for feedback message")
        self.wait_for_feedback(waiterbot_msgs.msg.DrinkOrderFeedback.ORIGIN_ARRIVAL)

        rospy.loginfo("Done!")

        return std_srvs.srv.EmptyResponse()

    def send_command(self, command):
        m = waiterbot_msgs.msg.DrinkOrder(command)
        self._pub_drink_order.publish(m)

    def wait_for_feedback(self, feedback):

        self.waited_feedback = feedback
        self.is_received = False

        while not rospy.is_shutdown() and not self.is_received:
            rospy.sleep(0.1)
            
    def process_drink_order_feedback(self, msg):
        if msg.feedback == self.waited_feedback:
            self.is_received = True
        else:
            rospy.loginfo("Feedback : " + str(msg.feedback))
            rospy.loginfo("Message  : " + str(msg.message))


    def spin(self):
        rospy.loginfo("Initialized")
        rospy.spin()
