#!/usr/bin/env python
#
# License: BSD
#   https://raw.github.com/robotics-in-concert/rocon_demos/license/LICENSE
#

import rospy
import waiterbot_msgs.msg

class DummyWaiter(object):

    def __init__(self):
        self._sub_drink_order = rospy.Subscriber("drink_order", waiterbot_msgs.msg.DrinkOrder,self._process_drink_order)
        self._pub_drink_order_feedback = rospy.Publisher("drink_order_feedback", waiterbot_msgs.msg.DrinkOrderFeedback)

        self._command_string = ["GO_TO_VM", "GO_TO_ORIGIN"]

    def _process_drink_order(self, msg):
        self.log("Received command : " + str(self._command_string[msg.command-1]))

        self.log("Sending accept message")
        self._send_feedback(waiterbot_msgs.msg.DrinkOrderFeedback.ACCEPTED, "")
    
        self.log("Navigating...")
        rospy.sleep(2.0)
        self.log("Send Arrival message")

        arrival_feedback = None

        if msg.command == waiterbot_msgs.msg.GO_TO_VM:
            arrival_feedback = waiterbot_msgs.msg.DrinkOrderFeedback.VM_ARRIVAL
        else:
            arrival_feedback = waiterbot_msgs.msg.DrinkOrderFeedback.ORIGIN_ARRIVAL
            
        self._send_feedback(arrival_feedback, "")

    def _send_feedback(self, feedback, message):
        self._pub_drink_order_feedback(feedback, message)
        

    def log(self, msg):
        rospy.loginfo("Dummy Waiter : " +str(msg))

    def spin(self):
        rospy.spin()
