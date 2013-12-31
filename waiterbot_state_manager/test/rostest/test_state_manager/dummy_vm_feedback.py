#!/usr/bin/env python
#
# License: BSD
#   https://raw.github.com/robotics-in-concert/rocon_demos/license/LICENSE
#

import rospy
import std_msgs.msg as std_msgs

class DummyVMFeedback(object):
    """
        Simulation of the vending machine feedback processor (colour light signal)
    """

    def __init__(self):
        # Vending machine feedback processor communication
        self._sub_vm_feedback_enable = rospy.Subscriber('vm_feedback_proc/enable', std_msgs.Bool,
                                                        self._vmFeedbackEnableCB)
        self._processing_enabled = False
        self._pub_vm_feedback_result = rospy.Publisher('vm_feedback_proc/result', std_msgs.Bool, latch=True)
        self._recognition_time = rospy.Duration(rospy.get_param("recognition_time", 1.0))
        self._recognition_start = rospy.Time.now()

    def _vmFeedbackEnableCB(self, msg):
        self._processing_enabled = msg.data
        if self._processing_enabled:
            self._recognition_start = rospy.Time.now()
            rospy.loginfo("DummyVMFeedback: Signal processing enabled.")
        else:
            rospy.loginfo("DummyVMFeedback: Signal processing disabled.")

    def spin(self):
        while not rospy.is_shutdown():
            if self._processing_enabled:
                rospy.loginfo("DummyVMFeedback: Processing light signal.")
                msg = std_msgs.Bool()
                if (rospy.Time.now() - self._recognition_start) > self._recognition_time:
                    rospy.loginfo("DummyVMFeedback: Light signal recognised!")
                    msg.data = True
                     # reset time to allow publishing continuous successful signal recognitions
                    self._recognition_start = rospy.Time.now()
                else:
                    msg.data = False
                self._pub_vm_feedback_result.publish(msg)
                rospy.sleep(0.1)
            else:
                rospy.loginfo("DummyVMFeedback: Idling.")
                rospy.sleep(1.0)


if __name__ == '__main__':
  rospy.init_node('dummy_vm_feedback')
  vm_feedback = DummyVMFeedback()
  vm_feedback.spin()

