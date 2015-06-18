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
        self.publisher = {}
        self.subcriber['ninja_block_data'] = rospy.Subscriber("ninja_block_data", NBDevice, self._update)
        self.publisher['rf233_sensor_event'] = rospy.Publisher("rf233_sensor_event", String, latch=False, queue_size=10)

    def _init_monitoring_list(self):
        for item in self.monitoring_list:
            self._loginfo("Checking item: [%s]" % str(item))
            self.last_detected_times[item] = rospy.Time(0)

    def _update(self, msg):
        if msg.type == NBDevice.RF233:
            device_name = str(msg.name)
            self.publisher['rf233_sensor_event'].publish(device_name)
            self._loginfo("%s detecting" % device_name)

    def _loginfo(self, msg):
        rospy.loginfo('[RF233 Sensor checker] ' + msg)

    def _spin(self):
        while not rospy.is_shutdown():
            rospy.sleep(0.1)

if __name__ == '__main__':
    rospy.init_node('rf233_sensors_checker')
    time_interval = 30
    monitoring_list = ['motion_detector']

    time_interval = rospy.get_param('~time_interval', 30)
    monitoring_list = rospy.get_param('~monitoring_list', [])

    mc = MotionChecker(time_interval=time_interval, monitoring_list=monitoring_list)
    mc._spin()

    print 'Motion Checker Bye Bye'
