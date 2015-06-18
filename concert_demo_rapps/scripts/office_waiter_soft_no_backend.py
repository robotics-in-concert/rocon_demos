#!/usr/bin/env python
import rospy
import threading
import random
import time

##ros msg
import actionlib
#from cafe_msgs.msg import *
from simple_delivery_msgs.msg import *
#from semantic_region_handler.msg import *
#from ar_track_alvar.msg import *

class WaiterSoftBot(object):
    def __init__(self,robot_name,action_name):
        self.name = robot_name
        self.action_name = action_name
        self.waiter_server = actionlib.SimpleActionServer(self.action_name,RobotDeliveryOrderAction, execute_cb = self.execute_callback,auto_start=False)

        #self.subscriber = {}
        #self.subscriber['table_list'] = rospy.Subscriber('table_post_list',TablePoseList,self.process_table_pose)
        #self.subscriber['ar_list'] = rospy.Subscriber('ar_list',AlvarMarkers,self.process_alvar_markers)
        
    def spin(self):
        self.waiter_server.start() 
        rospy.loginfo("Waiterbot has been Started")
        rospy.spin()

    def process_table_pose(self,msg):
        rospy.loginfo('table_pose message received')

    def process_alvar_markers(self,msg):
        rospy.loginfo('ar marker message received')


    def process_status(self,time_range,message,robot_status):
        k = 0;
        timeout = random.randrange(time_range[0],time_range[1])
        while k < timeout and not rospy.is_shutdown():
            k += 1
            rospy.sleep(1)
            rospy.loginfo(self.name + " : " +  message +", [%d/%d]"%(k,timeout))
        
        feedback = RobotDeliveryOrderFeedback()
        feedback.robot_status = robot_status
        self.waiter_server.publish_feedback(feedback)
    def order_process_status(self,receiver_location,time_range,message,order_status):
        k = 0;
        timeout = random.randrange(time_range[0],time_range[1])
        while k < timeout and not rospy.is_shutdown():
            k += 1
            rospy.sleep(1)
            rospy.loginfo(receiver_location + " : " +  message +", [%d/%d]"%(k,timeout))
        
        feedback = RobotDeliveryOrderFeedback()
        feedback.order_status = order_status
        self.waiter_server.publish_feedback(feedback)

    def feedback(self, name, robot_status, order_status, message):
        feedback = RobotDeliveryOrderFeedback()
        feedback.location = name
        feedback.robot_status = robot_status
        feedback.order_status = order_status
        self.waiter_server.publish_feedback(feedback)
        rospy.loginfo(name + " : " +  message)

    def execute_callback(self,data):
        #print data, type(data), dir(data)
        #print type(data._connection_header)
        time_start = 1
        time_end = 6

        receivers = data.locations
        rospy.loginfo("Order Received : Receivers = %s",data.locations)

        #Go to kitchen, and return feedback ARRIVE_KITCHEN
        self.process_status(time_range=[time_start,time_end],message="GO_TO_FRONTDESK",robot_status=RobotDeliveryOrderFeedback.GO_TO_FRONTDESK)

        # Arrival at kitchen
        self.feedback(self.name, RobotDeliveryOrderFeedback.ARRIVAL_AT_FRONTDESK, Receiver.UNKNOWN, "ARRIVAL_AT_FRONTDESK")
        
        #Wait for kitchen
        self.process_status(time_range=[time_start,time_end],message="WAITING_FOR_FRONTDESK",robot_status=RobotDeliveryOrderFeedback.WAITING_FOR_FRONTDESK)
        
        #In delivery
        self.feedback(self.name, RobotDeliveryOrderFeedback.IN_DELIVER, Receiver.UNKNOWN, "IN_DELIVER")

        for receiver in receivers:
            # Delivery order idle
            self.feedback(receiver, RobotDeliveryOrderFeedback.UNKNOWN, Receiver.DELIVERY_IDLE, "DELIVERY_IDLE")
            # Go to receiver
            self.order_process_status(receiver_location=receiver,time_range=[time_start,time_end],message="GO_TO_RECEIVER",order_status=Receiver.GO_TO_RECEIVER)
            # Arrival at receiver
            self.feedback(receiver, RobotDeliveryOrderFeedback.UNKNOWN, Receiver.ARRIVAL_AT_RECEIVER, "ARRIVAL_AT_RECEIVER")
            # Waiting confirm
            self.order_process_status(receiver_location=receiver,time_range=[time_start,time_end],message="WAITING_CONFIRM_RECEIVER",order_status=Receiver.WAITING_CONFIRM_RECEIVER)
            # Complete delivery
            self.feedback(receiver, RobotDeliveryOrderFeedback.UNKNOWN, Receiver.COMPLETE_DELIVERY, "COMPLETE_DELIVERY")
        # Complete all delivery
        self.feedback(self.name, RobotDeliveryOrderFeedback.COMPLETE_ALL_DELIVERY, Receiver.UNKNOWN, "COMPLETE_ALL_DELIVERY")
        # Returning to Docking
        self.process_status(time_range=[time_start,time_end],message="RETURNING TO DOCK", robot_status=RobotDeliveryOrderFeedback.RETURN_TO_DOCK)
        
        # Complete return
        feedback = RobotDeliveryOrderFeedback()
        feedback.robot_status = RobotDeliveryOrderFeedback.COMPELTE_RETURN    
        self.waiter_server.publish_feedback(feedback)


        rospy.loginfo(self.name+ " : END_DELIVERY_ORDER")
		
        rospy.sleep(1)
        
        # Closing off the delivery 
        result = RobotDeliveryOrderResult(True,"Success!")
        self.waiter_server.set_succeeded(result)

    
if __name__ == '__main__':
    
    try:
        # Initialize ros node
        rospy.init_node('waiterbot')

        waiter = WaiterSoftBot(rospy.get_name(),"delivery_order")
        rospy.loginfo('Initialized')

        waiter.spin()
        rospy.loginfo("Bye Bye")

    except rospy.ROSInterruptException:
        pass

