#!/usr/bin/env python
#
# License: BSD
#   https://raw.github.com/robotics-in-concert/rocon_demos/license/LICENSE
#

import rospy
import cafe_msgs.msg as cafe_msgs

class RemoteOrderManager(object):

    def __init__(self): 
        self.orders = {}

    def _init_rosapis(self):
        self.publisher = {}
        self.publisher['remote_order_status'] = rospy.Publisher('/cafe/remote_order_status', cafe_msgs.RemoteOrderStatus, latch=True)
        self.publisher['remote_order_list'] = rospy.Publisher('/cafe/remote_order_list', cafe_msgs.RemoteOrderList, latch=True)

        self.subscriber = {}
        self.subscriber['remote_order'] = rospy.Subscriber('/cafe/remote_order', cafe_msgs.RemoteOrder, self.process_remote_order)
        self.subscriber['remote_order_update'] = rospy.Subscriber('/cafe/remote_order_update', cafe_msgs.RemoteOrderUpdate, self.process_remote_order_update)

    def process_remote_order(self, msg):
        pass

    def process_remote_order_update(self, msg):
        pass

    def loginfo(self, msg):
        rospy.loginfo('Remote Order Manager : ' + str(msg))

