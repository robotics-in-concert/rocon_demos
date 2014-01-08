#!/usr/bin/env python
#
# License: BSD
#   https://raw.github.com/robotics-in-concert/rocon_demos/license/LICENSE
#

import random
import rospy
import std_msgs.msg as std_msgs
import waiterbot_msgs.msg as waiterbot_msgs
import kobuki_msgs.msg as kobuki_msgs

class DummyCancel(object):
    """
        Signals tray empty when robot arrives with the drinks at the delivery place
    """

    def __init__(self):

        # publish green button press
        self._pub_red_button = rospy.Publisher('/mobile_base/events/digital_input', kobuki_msgs.DigitalInputEvent, latch=True)
        self._process_cnt = 0
        self._waiting_time = self._get_waiting_time()
    def spin(self):
        while not rospy.is_shutdown():
            if self._process_cnt == self._waiting_time:
                m = kobuki_msgs.DigitalInputEvent()
                rospy.loginfo("Pressing Red button")
                m.values = [True, False, False, False]
                self._pub_red_button.publish(m)
                rospy.sleep(0.5)

                rospy.loginfo("Releasing Red button")
                m.values = [True, True, False, False]
                self._pub_red_button.publish(m)
                rospy.sleep(0.5)
                
                self._waiting_time = self._get_waiting_time()
                self._process_cnt = 0
            else:
                pass
                
            self._process_cnt = self._process_cnt+1
            rospy.sleep(1)
            pass
            
    def _get_waiting_time(self):
        waiting_time = random.randint(1,30)+30
        rospy.loginfo("waitting time is [%d] untill to press red button"%waiting_time)
        return waiting_time
        pass
        


if __name__ == '__main__':
  rospy.init_node('dummy_red_button')
  red_button = DummyCancel()
  red_button.spin()

