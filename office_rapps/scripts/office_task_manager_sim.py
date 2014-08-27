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


        self.action_name = action_name

        self.publishers = {}
        self.subscribers = {}
        self.order_list = {}
        self.waiter_client = None
        
        self.waiter_client = actionlib.SimpleActionClient(robot_name+"/"+self.action_name,RobotDeliveryOrderAction)

        self.subscribers['send_order'] = rospy.Subscriber('send_order', DeliveryOrder, self._update)
        self.publishers['order_status'] = rospy.Publisher('order_status', DeliveryOrder)
        

        pass
    def _update(self, data):
        if self.waiter_client is None:
            return
        rospy.loginfo('receive order, waitting action server')
        self.waiter_client.wait_for_server()
        rospy.loginfo('action server opened')
        self.order_list[data.id] = data
        locataions = []
        for  receiver in data.receivers:
            locataions.append(receiver.location)
        goal = RobotDeliveryOrderGoal(locations = locataions)
        self.waiter_client.send_goal(goal, done_cb = self.delivery_done_cb, feedback_cb = self.delivery_feedback_cb)
        
        rospy.loginfo('send goal: %s' % str(locataions))

        pass

    def delivery_done_cb(self, data1, data2):
        print 'delivery done!!!'
        print '-----------'
        print data2
        pass

    def delivery_feedback_cb(self, data):
        rospy.loginfo('Location:[%s] Robotstatus:[%s] Orderstatus:[%s] ' % (str(data.location), 
                                                                                        str(self.robot_status[data.robot_status]), 
                                                                                        str(self.order_status[data.order_status])))
    
    def spin(self):
        rospy.loginfo("dummy task manager start!")
        rospy.spin()
    
if __name__ == '__main__':
    
    try:
        # Initialize ros node
        rospy.init_node('dummy_task_manager')
        dummy = DummyTaskManager("adams","delivery_order")
        rospy.loginfo('Initialized')
        dummy.spin()
        rospy.loginfo("Bye Bye")

    except rospy.ROSInterruptException:
        pass