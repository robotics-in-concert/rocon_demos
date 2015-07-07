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
from room_checker_msgs.msg import *
import rocon_device_msgs.msg as rocon_device_msgs


class EmptyRoomChecker():

    def __init__(self, time_interval=5, room_list=[]):
        self.subcriber = {}
        self.subcriber['devices'] = rospy.Subscriber("/devices", rocon_device_msgs.Devices, self._update)
        # create empty room
        # self.publisher['empty_room']
        self.check_motion_as = actionlib.SimpleActionServer('check_empty_room', CheckEmptyRoomAction, execute_cb=self._check_empty_room, auto_start=False)
        self.last_detected_times = {}
        self.thre_time_interval = time_interval
        self.room_list = {}

        self._init_room_list(room_list)
        self.check_motion_as.start()

    def _init_room_list(self, rooms_list):
        self.room_list = self._rooms_list2dict(rooms_list)
        for item in self.room_list.values():
            self._loginfo("Checking room: [%s]" % str(item))
            self.last_detected_times[item] = rospy.Time(0)

    def _rooms_list2dict(self, rooms_list):
        rooms_dict = {}
        for room in rooms_list:
            room_name = room.keys()[0]
            room_motion_sensor_label = room[room_name]
            rooms_dict[room_motion_sensor_label] = room_name
        return rooms_dict

    def _update(self, msg):
        devices = msg.devices
        for dev in devices:
            if dev.label in self.room_list.keys():
                device_name = self.room_list[dev.label]
                device_uuid = dev.uuid
                if device_name in self.last_detected_times.keys():
                    self.last_detected_times[device_name] = rospy.Time.now()
                    self._loginfo('Detecting: ' + device_name + ' - ' + str(rospy.Time.now()))
            # else:
            #     self._loginfo('Invalid handling sensor. Please check parameters: [' + dev.label + ']')

    def _check_empty_room(self, msg):
        detected_item_list = []
        for monitoring_item in self.last_detected_times.keys():
            diff = rospy.Time.now() - self.last_detected_times[monitoring_item]
            if diff > rospy.Duration(60 * self.thre_time_interval):
                key_value = KeyValue(monitoring_item, str(False))
            else:
                key_value = KeyValue(monitoring_item, str(True))
            detected_item_list.append(key_value)

        result = CheckEmptyRoomResult(True, detected_item_list)
        self.check_motion_as.set_succeeded(result)
        self._loginfo('Checking: ' + str(detected_item_list))

    def _loginfo(self, msg):
        rospy.loginfo('[Room Checker] ' + msg)

    def _spin(self):
        while not rospy.is_shutdown():
            rospy.sleep(0.1)

if __name__ == '__main__':
    rospy.init_node('empty_room_checker_with_smartthings')
    time_interval = 5
    room_list = []
    time_interval = rospy.get_param('~time_interval', 5)
    room_list = rospy.get_param('~rooms', [])

    erc = EmptyRoomChecker(time_interval=time_interval, room_list=room_list)
    erc._spin()

    print 'Room Checker Bye Bye'
