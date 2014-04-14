#!/usr/bin/env python
#
# License: BSD
#   https://raw.github.com/robotics-in-concert/rocon_demos/license/LICENSE
#

import rospy
import cafe_msgs.msg as cafe_msgs
import threading

class RemoteOrderManager(object):

    def __init__(self): 
        self.orders = {}
        self._init_rosapis()
        self.lock = threading.Lock()

    def _init_rosapis(self):
        self.publisher = {}
        self.publisher['remote_order_status'] = rospy.Publisher('/cafe/remote_order_status', cafe_msgs.RemoteOrderStatus)
        self.publisher['remote_order_list'] = rospy.Publisher('/cafe/remote_order_list', cafe_msgs.RemoteOrderList, latch=True)

        self.subscriber = {}
        self.subscriber['remote_order'] = rospy.Subscriber('/cafe/remote_order', cafe_msgs.RemoteOrder, self.process_remote_order)
        self.subscriber['remote_order_update'] = rospy.Subscriber('/cafe/remote_order_update', cafe_msgs.RemoteOrderUpdate, self.process_remote_order_update)

    def process_remote_order(self, msg):
        self.loginfo('Message Received')
        
        # TODO: it uses name as order unique id. If it receives an order with the same name, it just drops it. And no way to respond back
        if msg.name in self.orders:
            self.logwarn('order from [%s] is in preparation already. Dropping the new order..'%msg.name)
            return
        self.lock.acquire()
        self.orders[msg.name] = msg
        self.orders[msg.name].status = cafe_msgs.RemoteOrderStatus.ORDER_RECEIVED
        self.update()
        self.loginfo('Order from [%s] has been placed'%msg.name)
        self.publisher['remote_order_status'].publish(self.orders[msg.name].status)
        self.lock.release()

    def process_remote_order_update(self, msg):
        self.loginfo('Update Received')
        if not msg.name in self.orders:
            self.logwarn('order from [%s] is not placed yet. Dropping the update..'%msg.name) 
            return
            
        self.lock.acquire()
        self.orders[msg.name].status = msg.status
        self.orders[msg.name].estimated_arrival = msg.estimated_arrival
        self.publisher['remote_order_status'].publish(self.orders[msg.name].status)

        if msg.status == cafe_msgs.RemoteOrderStatus.ORDER_PICKED_UP:
            del self.orders[msg.name]
            self.loginfo('Order from [%s] has been picked up. Clearing..'%msg.name)

        self.update()
        self.lock.release()
    
    def update(self):
        order_list = self.orders.values()
        self.publisher['remote_order_list'].publish(order_list)

    def spin(self):
        # Publishes the empty latch topic
        self.publisher['remote_order_list'].publish(cafe_msgs.RemoteOrderList())
        rospy.spin()

    def loginfo(self, msg):
        rospy.loginfo('Remote Order Manager : ' + str(msg))

    def logwarn(self, msg):
        rospy.logwarn('Remote Order Manager : ' + str(msg))
