#!/usr/bin/env python
import rospy
import threading
import random
import time
import uuid

##ros msg
import actionlib
from simple_delivery_msgs.msg import *
from std_msgs.msg import *

class DummyOrderApp():
    def __init__(self, location):
        self.location = location
        self.delivery_status = {}
        self.delivery_status[DeliveryStatus.IDLE] = 'IDLE'
        self.delivery_status[DeliveryStatus.GO_TO_FRONTDESK] = 'GO_TO_FRONTDESK'
        self.delivery_status[DeliveryStatus.ARRIVAL_AT_FRONTDESK] = 'ARRIVAL_AT_FRONTDESK'
        self.delivery_status[DeliveryStatus.WAITING_FOR_FRONTDESK] = 'WAITING_FOR_FRONTDESK'
        self.delivery_status[DeliveryStatus.GO_TO_RECEIVER] = 'GO_TO_RECEIVER'
        self.delivery_status[DeliveryStatus.ARRIVAL_AT_RECEIVER] = 'ARRIVAL_AT_RECEIVER'
        self.delivery_status[DeliveryStatus.WAITING_CONFIRM_RECEIVER] = 'WAITING_CONFIRM_RECEIVER'
        self.delivery_status[DeliveryStatus.COMPLETE_DELIVERY] = 'COMPLETE_DELIVERY'
        self.delivery_status[DeliveryStatus.COMPLETE_ALL_DELIVERY] = 'COMPLETE_ALL_DELIVERY'
        self.delivery_status[DeliveryStatus.RETURN_TO_DOCK] = 'RETURN_TO_DOCK'
        self.delivery_status[DeliveryStatus.COMPLETE_RETURN] = 'COMPLETE_RETURN'
        self.delivery_status[DeliveryStatus.ERROR] = 'ERROR'

        self.publishers = {}
        self.subscribers = {}
        self.publishers['send_order'] = rospy.Publisher('/send_order', DeliveryOrder,latch=True)
        self.subscribers['delivery_status'] = rospy.Subscriber('/delivery_status', DeliveryStatus, self.delivery_status_update)

    def delivery_status_update(self, data):
        rospy.loginfo('Location:[%s] OrderID:[%s] DeliveryStatus:[%s] ' % (str(data.target_goal), 
                                                                                        str(data.order_id), 
                                                                                        str(self.delivery_status[data.status])))

    def spin(self):
        rospy.loginfo("dummy order app start!")
        while not rospy.is_shutdown():
            rospy.sleep(10)

    def set_target_location(self, target_location):
        self.location = target_location
        rospy.loginfo("target location: [%s]" % self.location)

    def send_dummy_order(self):
        order = DeliveryOrder()
        order.order_id = str(uuid.uuid4())
        
        receiver = Receiver()
        receiver.location = str(self.location)
        receiver.qty = 1
        order.receivers.append(receiver)

        # for location in range(1,5):
        #     receiver = Receiver()
        #     receiver.location = 'table'+str(location)
        #     receiver.qty = 1
        #     order.receivers.append(receiver)

        self.publishers['send_order'].publish(order)
        rospy.loginfo('send dummy order: %s' % str(order))
if __name__ == '__main__':
    
    try:
        # Initialize ros node
        rospy.init_node('dummy_order_app')
        
        rospy.loginfo('Initialized')
        
        target_location = rospy.get_param('~target_location', 'table4')

        dummy = DummyOrderApp(target_location)
        

        dummy.send_dummy_order()
        dummy.spin()
        rospy.loginfo("Bye Bye")

    except rospy.ROSInterruptException:
        pass
