#!/usr/bin/env python
#
# License: BSD
#   https://raw.github.com/robotics-in-concert/rocon_demos/license/LICENSE
#

import rospy
import cafe_msgs.msg as cafe_msgs
import rocon_device_msgs.msg as rocon_device_msgs


class HueManager():
    #common
    MAX_ORDER_NUM = 3
    #bulbid
    TABLE_BULB_ID = 1
    KITCHEN_BULB_ID = 2
    TABLE_BULB_ID = 3

    #order status
    IDLE = 0
    GO_TO_KITCHEN = 1
    ARRIVE_KITCHEN = 2
    WAITING_FOR_KITCHEN = 3
    IN_DELIVERY = 4
    ARRIVE_TABLE = 5
    WAITING_FOR_USER_CONFIRMATION = 6
    COMPLETE_DELIVERY = 7
    RETURNING_TO_DOCK = 8
    END_DELIVERY_ORDER = 9
    ERROR = 10

    #color
    COLOR_H_RED = 65534
    COLOR_H_GREEN = 25500
    COLOR_H_BLUE = 46920
    MAX_SAT = 255
    MAX_BRI = 255
    MAX_HUE = 65535

    def __init__(self):
        self.subscriber = {}
        self.publisher = {}
        self.hues = {}
        self.hues_init = False
        self.local_order_num = 0
        self.remote_order_num = 0
        self.total_order_num = 0
        self.subscriber['list_order'] = rospy.Subscriber('list_order', cafe_msgs.OrderList, self.local_order_update)
        self.subscriber['remote_order_list'] = rospy.Subscriber('remote_order_list', cafe_msgs.RemoteOrderList, self.remote_order_update)
        self.subscriber['hue_order'] = rospy.Subscriber('hue_list', rocon_device_msgs.HueArray, self.hue_update)

        self.publisher['set_hue_hsv'] = rospy.Publisher('set_hue_color_hsv', rocon_device_msgs.Hue)
        self.publisher['set_hue_mode'] = rospy.Publisher('set_hue_color_mode', rocon_device_msgs.Hue)
        pass

    def hue_update(self, data):
        if not self.hues_init and len(data.hue_list):
            self.loginfo("Yes Hue...")
            self.hues_init = True
            for hue in data.hue_list:
                hue.state.sat = 0
                hue.state.bri = 125
                self.publisher['set_hue_hsv'].publish(hue)
            return
        elif not len(data.hue_list):
            self.hues_init = False
            self.hues = {}
            return
        for hue in data.hue_list:
            self.hues[hue.light_id] = hue

    def hue_color_update(self):

        if self.KITCHEN_BULB_ID in self.hues:
            self.total_order_num = self.remote_order_num + self.local_order_num
            if self.total_order_num > self.MAX_ORDER_NUM:
                self.total_order_num = self.MAX_ORDER_NUM
            
            if self.total_order_num is 1:
                self.hues[self.KITCHEN_BULB_ID].state.hue = self.COLOR_H_GREEN
                self.hues[self.KITCHEN_BULB_ID].state.sat = self.MAX_SAT
                self.hues[self.KITCHEN_BULB_ID].state.bri = self.MAX_BRI
            elif self.total_order_num is 2:
                self.hues[self.KITCHEN_BULB_ID].state.hue = self.COLOR_H_BLUE
                self.hues[self.KITCHEN_BULB_ID].state.sat = self.MAX_SAT
                self.hues[self.KITCHEN_BULB_ID].state.bri = self.MAX_BRI
            elif self.total_order_num > 2:
                self.hues[self.KITCHEN_BULB_ID].state.hue = self.COLOR_H_RED
                self.hues[self.KITCHEN_BULB_ID].state.sat = self.MAX_SAT
                self.hues[self.KITCHEN_BULB_ID].state.bri = self.MAX_BRI
               
            else:
                self.hues[self.KITCHEN_BULB_ID].state.hue = self.COLOR_H_BLUE
                self.hues[self.KITCHEN_BULB_ID].state.sat = 0
                self.hues[self.KITCHEN_BULB_ID].state.bri = 0
            self.publisher['set_hue_hsv'].publish(self.hues[self.KITCHEN_BULB_ID])
                        
    def remote_order_update(self, data):
        on_remote_ordering = []
        for order in data.remote_orders:
            if order.status is self.IDLE or order.status is self.GO_TO_KITCHEN:
                on_remote_ordering.append(order)
        self.remote_order_num = len(on_remote_ordering)
        self.hue_color_update()

        pass
    def local_order_update(self, data):
        on_local_ordering = []
        for order in data.orders:
            if order.status is self.IDLE or order.status is self.GO_TO_KITCHEN:
                on_local_ordering.append(order)
        self.local_order_num = len(on_local_ordering)
        self.hue_color_update()

    def loginfo(self, msg):
        rospy.loginfo('Hue Manager : ' + str(msg))

    def spin(self):
        while not rospy.is_shutdown():
            rospy.sleep(1)
