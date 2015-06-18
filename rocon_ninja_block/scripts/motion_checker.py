#!/usr/bin/env python
#
# License: BSD
#   https://raw.github.com/robotics-in-concert/rocon_devices/license/LICENSE
#
#################################################################################

# sys
import time
# ros
import rospy
import actionlib
from std_msgs.msg import String
from diagnostic_msgs.msg import KeyValue
from rocon_ninja_block.msg import *


class MotionChecker():

    def __init__(self, time_interval=30, monitoring_list=[]):
        self.subcriber = {}
        self.subcriber['ninja_block_data'] = rospy.Subscriber("ninja_block_data", NBDevice, self._update)

        self.check_motion_as = actionlib.SimpleActionServer('check_motion', CheckMotionAction, execute_cb=self._check_motion, auto_start=False)

        self.last_detected_times = {}

        self.thre_time_interval = time_interval
        self.monitoring_list = monitoring_list
        self._init_monitoring_list()
        self.check_motion_as.start()

    def _init_monitoring_list(self):
        for item in self.monitoring_list:
            self._loginfo("Checking item: [%s]" % str(item))
            self.last_detected_times[item] = rospy.Time(0)


    def _update(self, msg):
        device_name = msg.name
        if device_name in self.last_detected_times.keys():
            self.last_detected_times[device_name] = rospy.Time.now()
            self._loginfo('Detecting: ' + device_name + ' - ' + str(rospy.Time.now()))

    def _check_motion(self, msg):
        detected_item_list = []
        for monitoring_item in self.last_detected_times.keys():
            diff = rospy.Time.now() - self.last_detected_times[monitoring_item]
            if diff > rospy.Duration(60 * self.thre_time_interval):
                key_value = KeyValue(monitoring_item, str(False))
            else:
                key_value = KeyValue(monitoring_item, str(True))
            detected_item_list.append(key_value)

        result = CheckMotionResult(True, detected_item_list)
        self.check_motion_as.set_succeeded(result)
        self._loginfo('Checking: ' + str(detected_item_list))

    def _loginfo(self, msg):
        rospy.loginfo('[Motion checker] ' + msg)

    def _spin(self):
        while not rospy.is_shutdown():
            rospy.sleep(0.1)

if __name__ == '__main__':
    rospy.init_node('motion_checker')
    time_interval = 30
    monitoring_list = ['motion_detector']

    time_interval = rospy.get_param('~time_interval', 30)
    monitoring_list = rospy.get_param('~monitoring_list', [])

    mc = MotionChecker(time_interval=time_interval, monitoring_list=monitoring_list)
    mc._spin()

    print 'Motion Checker Bye Bye'
