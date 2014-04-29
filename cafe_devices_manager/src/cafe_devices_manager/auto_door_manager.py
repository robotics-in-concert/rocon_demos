#!/usr/bin/env python
#
# License: BSD
#   https://raw.github.com/robotics-in-concert/rocon_demos/license/LICENSE
#

import rospy
import cafe_msgs.msg as cafe_msgs


class AutoDoorManager():
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

    def __init__(self):
        self.subscriber = {}
        self.publisher = {}
        self.door_status = False
        self.table_id = 1
        self.subscriber['list_order'] = rospy.Subscriber('list_order', cafe_msgs.OrderList, self.update)

    def set_table_id(self, table_id):
        self.table_id = table_id

    def update(self, data):
        in_delivery = []
        for order in data.orders:
            if order.status is self.IN_DELIVERY or order.status is self.RETURNING_TO_DOCK and order.table_id is self.table_id:
                in_delivery.append(order)

        if len(in_delivery) and not self.door_status:
            print "open the door"
            """
            publish the open msg
            """
            self.door_status = True
        elif not len(in_delivery) and self.door_status:
            print "close the door"
            self.door_status = False
            """
            publish the close msg
            """

    def spin(self):
        """
        door closed first time
        """
        while not rospy.is_shutdown():
            rospy.sleep(1)
