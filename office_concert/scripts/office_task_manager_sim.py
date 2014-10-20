#!/usr/bin/env python
import rospy
import threading
import random
import time
import uuid

##ros msg
import actionlib
from simple_delivery_msgs.msg import *

class DummyTaskManager(object):
    def __init__(self, robot_name, action_name ):
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
        
        self.action_name = action_name
        self.publishers = {}
        self.subscribers = {}
        self.order_list = {}
        self.waiter_client = None
        
        self.waiter_client = actionlib.SimpleActionClient("/" + robot_name+"/"+self.action_name,RobotDeliveryOrderAction)

        self.subscribers['send_order'] = rospy.Subscriber('send_order', DeliveryOrder, self._update)
        self.publishers['delivery_status'] = rospy.Publisher('delivery_status', DeliveryStatus)
        

        pass
    def _update(self, data):
        if self.waiter_client is None:
            return
        rospy.loginfo('receive order, waitting action server')
        self.waiter_client.wait_for_server()
        rospy.loginfo('action server opened')
        self.order_list[data.order_id] = data
        locataions = []
        for  receiver in data.receivers:
            locataions.append(receiver.location)
        goal = RobotDeliveryOrderGoal(locations = locataions, order_id = data.order_id)
        self.waiter_client.send_goal(goal, done_cb = self.delivery_done_cb, feedback_cb = self.delivery_feedback_cb)
        
        rospy.loginfo('send goal: %s' % str(locataions))

        pass

    def delivery_done_cb(self, data1, data2):
        rospy.loginfo('------------------------')
        rospy.loginfo('delivery done!!!')
        rospy.loginfo(data2)

    def delivery_feedback_cb(self, data):
        rospy.loginfo('Location:[%s] OrderID:[%s] DeliveryStatus:[%s] ' % (str(data.delivery_status.target_goal), 
                                                                                        str(data.delivery_status.order_id), 
                                                                                        str(self.delivery_status[data.delivery_status.status])))
        self.publishers['delivery_status'].publish(data.delivery_status) 
    
    def spin(self):
        rospy.loginfo("dummy task manager start!")
        rospy.spin()
    
if __name__ == '__main__':
    
    try:
        # Initialize ros node
        rospy.init_node('dummy_task_manager')
        waiter_name = ''
        if rospy.has_param('~waiter_name'):
            waiter_name = rospy.get_param('~waiter_name')
        else:
            rospy.loginfo("waiter name uses default name, young.")
            waiter_name = 'young'
        
        waiter_name = rospy.get_param("~waiter_name")

        rospy.loginfo("waiter name: [%s]" % waiter_name)
        dummy = DummyTaskManager(waiter_name,"delivery_order")
        rospy.loginfo('Initialized')
        dummy.spin()
        rospy.loginfo("Bye Bye")

    except rospy.ROSInterruptException:
        pass
