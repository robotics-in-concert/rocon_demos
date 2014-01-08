#!/usr/bin/env python
#
# License: BSD
#   https://raw.github.com/robotics-in-concert/rocon_demos/license/LICENSE
#

import rospy
import std_msgs.msg as std_msgs
import waiterbot_msgs.msg as waiterbot_msgs
import kobuki_msgs.msg as kobuki_msgs

class DummyTrayEmpty(object):
    """
        Signals tray empty when robot arrives with the drinks at the delivery place
    """

    def __init__(self):

        # listen to navigation feedback
        self._sub_nav_status = rospy.Subscriber('waiterbot_nav_control/status', waiterbot_msgs.NavCtrlStatus,
                                                        self._NavCtrlStatusCB)
        # publish green button press
        self._pub_green_button = rospy.Publisher('/mobile_base/events/digital_input', kobuki_msgs.DigitalInputEvent, latch=True)
        
        self._nav_ctrl_status_code =-1
        self._process_cnt = 0
        

    def _NavCtrlStatusCB(self, msg):
        self._nav_ctrl_status_code = msg.status_code

    def spin(self):
        while not rospy.is_shutdown():
            if self._nav_ctrl_status_code == waiterbot_msgs.NavCtrlStatus.VM_ARRIVAL:
                rospy.loginfo("VM_ARRIVAL")
                self._nav_ctrl_status_code = -1
                rospy.loginfo("RESET_STATUS")
                pass
 
            elif self._nav_ctrl_status_code == waiterbot_msgs.NavCtrlStatus.ORIGIN_ARRIVAL:
                rospy.loginfo("ORIGIN_ARRIVAL")
                rospy.sleep(1.0)
                
                m = kobuki_msgs.DigitalInputEvent()
                rospy.loginfo("Pressing Green button")
                m.values = [False, True, False, False]
                
                self._pub_green_button.publish(m)
                rospy.sleep(0.5)
                rospy.loginfo("Releasing Green button")
                m.values = [True, True, False, False]
                self._pub_green_button.publish(m)
                rospy.sleep(0.5)
                
                self._nav_ctrl_status_code = -1
                rospy.loginfo("RESET_STATUS")
                self._process_cnt=self._process_cnt+1
                pass
 
            else:
                rospy.sleep(0.2)
                pass

            """
                rospy.loginfo("DummyVMFeedback: Processing light signal.")
                msg = std_msgs.Bool()
                if self._new_order and (rospy.Time.now() - self._order_time) > self._recognition_time:
                    rospy.loginfo("DummyVMFeedback: Light signal recognised!")
                    msg.data = True
                    self._new_order = False
                else:
                    msg.data = False
                self._pub_vm_feedback_result.publish(msg)
                rospy.sleep(0.1)
            else:
                rospy.loginfo("DummyVMFeedback: Idling.")
                rospy.sleep(1.0)
            """


if __name__ == '__main__':
  rospy.init_node('dummy_green_button')
  green_button = DummyTrayEmpty()
  green_button.spin()

