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
    def __init__(self):
        self.robot_status = {}
        self.robot_status[RobotDeliveryOrderFeedback.ROBOT_IDLE] = 'ROBOT_IDLE'
        self.robot_status[RobotDeliveryOrderFeedback.GO_TO_FRONTDESK] = 'GO_TO_FRONTDESK'
        self.robot_status[RobotDeliveryOrderFeedback.ARRIVAL_AT_FRONTDESK] = 'ARRIVAL_AT_FRONTDESK'
        self.robot_status[RobotDeliveryOrderFeedback.WAITING_FOR_FRONTDESK] = 'WAITING_FOR_FRONTDESK'
        self.robot_status[RobotDeliveryOrderFeedback.IN_DELIVER] = 'IN_DELIVER'
        self.robot_status[RobotDeliveryOrderFeedback.COMPLETE_ALL_DELIVERY] = 'COMPLETE_ALL_DELIVERY'
        self.robot_status[RobotDeliveryOrderFeedback.RETURN_TO_DOCK] = 'RETURN_TO_DOCK'
        self.robot_status[RobotDeliveryOrderFeedback.COMPELTE_RETURN] = 'COMPELTE_RETURN'
        self.robot_status[RobotDeliveryOrderFeedback.UNKNOWN] = 'UNKNOWN'
        
        self.order_status = {}
        self.order_status[Receiver.DELIVERY_IDLE] = 'DELIVERY_IDLE'
        self.order_status[Receiver.GO_TO_RECEIVER] = 'GO_TO_RECEIVER'
        self.order_status[Receiver.ARRIVAL_AT_RECEIVER] = 'ARRIVAL_AT_RECEIVER'
        self.order_status[Receiver.WAITING_CONFIRM_RECEIVER] = 'WAITING_CONFIRM_RECEIVER'
        self.order_status[Receiver.COMPLETE_DELIVERY] = 'COMPLETE_DELIVERY'
        self.order_status[Receiver.UNKNOWN] = 'UNKNOWN'

        self.publishers = {}
        self.subscribers = {}
        self.publishers['send_order'] = rospy.Publisher('send_order', DeliveryOrder,latch=True)
        self.subscribers['order_status'] = rospy.Subscriber('order_status', DeliveryOrder, self.order_status_update)
        pass

    def order_status_update(self, data):
        print 'location:[%s] order status: [%s] robot status: [%s] ' % (str(data.location), 
                                                                                   str(self.order_status[data.order_status]), 
                                                                                   str(self.robot_status[data.robot_status]))

    def spin(self):
        rospy.loginfo("dummy order app start!")
        while not rospy.is_shutdown():
            
            rospy.sleep(10)
    def send_dummy_order(self):
        order = DeliveryOrder()
        order.id = str(uuid.uuid4())
        for location in range(1,2):
            receiver = Receiver()
            receiver.location = 'table'+str(location)
            receiver.qty = 1
            order_status = Receiver.DELIVERY_IDLE
            order.receivers.append(receiver)

        self.publishers['send_order'].publish(order)
        rospy.loginfo('send dummy order: %s' % str(order))
if __name__ == '__main__':
    
    try:
        # Initialize ros node
        rospy.init_node('dummy_order_app')
        dummy = DummyOrderApp()
        rospy.loginfo('Initialized')
        dummy.send_dummy_order()
        dummy.spin()
        rospy.loginfo("Bye Bye")

    except rospy.ROSInterruptException:
        pass