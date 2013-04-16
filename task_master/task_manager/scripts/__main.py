#!/usr/bin/env python
# -*- coding:utf-8 -*-


import rospy
import time

import threading
import random

import actionlib

from std_msgs.msg import *
from cafe_msgs.msg import *

global goal_handle_list;goal_handle_list = []

def Recv(data):
	print "Add goal_handle_list length: ", len(goal_handle_list)
	goal_handle_list.append(data)
	
	
	print "////////////////////////////////////////////////////////////"
	print "get_goal_id(): ",data.get_goal_id().id
	#print "get_goal(): ",data.get_goal(), type(data.get_goal())
	print "get_goal_status(): ",data.get_goal_status().status
	data.set_accepted()
	print "get_goal_status(): ",data.get_goal_status().status
	#print "get_goal_id(): ",data.get_goal_id(), type(get_goal_id())
	
	#print "data type: ",type(data)
	#print "data dir: ",dir(data)


def FakeFeedbackFunc():
	
	while True and not rospy.is_shutdown():
		SendCnt = 0
		while True and not rospy.is_shutdown():
			print "goal_handle_list length: ", len(goal_handle_list)
			
			if len(goal_handle_list) != 0:
				for k in goal_handle_list:
					print "FakeFeedbackFunc: ",k.get_goal_id().id, type(k.get_goal_id())
					feedback = UserOrderFeedback()
					feedback.status = Status.GO_TO_KITCHEN
					k.publish_feedback(feedback)
					SendCnt += 1
		
			if SendCnt > 10:
				print "Send Result"
				break
			rospy.sleep(5)		

		for k in goal_handle_list:
			print "FakeResultFunc: ",k.get_goal_id().id, type(k.get_goal_id())
			result = UserOrderResult()
			result.result = str(k.get_goal_id().id)
			k.set_succeeded(result)
			goal_handle_list.remove(k)		
			print "Pop goal_handle_list length: ", len(goal_handle_list)
		
		
		for k in goal_handle_list:
			print k, "goal_handle_list: ", k, type(k)	
	
if __name__ == '__main__':
    
	try:	
		print "=========================Main start==============================="
		
		ThreadFakeFeedbackFunc = threading.Thread(target=FakeFeedbackFunc, args=())
		ThreadFakeFeedbackFunc.start()
			
		rospy.init_node('task_coordinator', anonymous = True)	
		####################################################
		#user_device_p = rospy.Publisher('user_device_p', Order)
		#rospy.Subscriber("user_device_order_sub",Order, Recv)
		#global user_device_action_server;
		user_device_action_server =  actionlib.ActionServer('send_order',UserOrderAction,Recv)
		#user_device_action_server.register_goal_callback(Recv)
		#user_device_action_server.start()
		####################################################
		
		while not rospy.is_shutdown():
			rospy.sleep(1)
			pass

		print "=========================Main end==============================="
	
	
	
	except rospy.ROSInterruptException:
		pass
