#!/usr/bin/env python
import rospy
import threading
import random
import time

##ros msg
import actionlib
from cafe_msgs.msg import *

global pub
def executeDeliveruSrv(robot_name,data):
	global robot_list;
	print data.user_id, data.table_id, data.robot_id, data.status
	robot_list[robot_name]["status"] = "Delivery"
	robot_list[robot_name]["order"] = data
	
	delivery_timeout = random.randrange(0,30)+30
	i = 0
	while i< delivery_timeout:
			i+=1
			rospy.sleep(1)
			print "[%s]"%robot_name, "Delivery %d/%d"%(i,delivery_timeout)	
	## arrive	
	robot_list[robot_name]["order"].status = "Arrive"
	robot_list[robot_name]["pub"].publish(robot_list[robot_name]["order"])
	
	robot_list[robot_name]["status"] = "WaitingCompletion"
	robot_list[robot_name]["order"].status = "WaitingCompletion"
	
	while robot_list[robot_name]["status"] != "Completion":
		print "[%s]"%robot_name, "Waitting user"
		time.sleep(1)
		pass
	
		
def Recv(data):
	
	if data._connection_header['topic'] == '/delivery_robot_init_pub':
		pass
		#global robot_num
		#robot_num = data.data
	
	elif data._connection_header['topic'].count("_pub") != 0:
		
		robot_name = "robot_"+data._connection_header['topic'].split('_')[3]
		print robot_name, type(robot_name)
		if data.status == "Delivery":
			#todo
			#make threading function about robot delivery service			
			Threadfunc = threading.Thread(target=executeDeliveruSrv, args=(robot_name,data))
			Threadfunc.start()
		else:
			pass
	else:
		pass
		

def ExecuteCB(data):
	#print data, type(data), dir(data)
	#print type(data._connection_header)
	print data.order.robot_name
	global waiter_server; 
	robot_name = data.order.robot_name
	_as = waiter_server[data.order.robot_name]
	_feedback = DeliverOrderFeedback()
	_result = DeliverOrderResult()

	
	#Go to kitchen 	
	k = 0;
	timeout = random.randrange(5,10)
	while k < timeout and not rospy.is_shutdown():
		k+=1
		rospy.sleep(1)
		print robot_name, "GO_TO_KITCHEN, [%d/%d]"%(k,timeout)
	
	_feedback.status = Status.ARRIVE_KITCHEN	
	_as.publish_feedback(_feedback)	
	
	
	_feedback.status = Status.WAITING_FOR_KITCHEN	
	_as.publish_feedback(_feedback)	
	
	
	#wait for kitchen 	
	k = 0;
	timeout = random.randrange(1,3)
	while k < timeout and not rospy.is_shutdown():
		k+=1
		rospy.sleep(1)
		print robot_name, "WAITING_FOR_KITCHEN, [%d/%d]"%(k,timeout)
	
	_feedback.status = Status.IN_DELIVERY	
	_as.publish_feedback(_feedback)	
	
	
	#in delivery  	
	k = 0;
	timeout = random.randrange(20,30)
	while k < timeout and not rospy.is_shutdown():
		k+=1
		rospy.sleep(1)
		print robot_name, "IN_DELIVERY, [%d/%d]"%(k,timeout)
	
	_feedback.status = Status.ARRIVE_TABLE	
	_as.publish_feedback(_feedback)		
	print robot_name, "ARRIVE_TABLE"
	
	
	_feedback.status = Status.WAITING_FOR_USER_CONFIRMATION	
	_as.publish_feedback(_feedback)
	
	
	k = 0;
	timeout = random.randrange(10,15)
	while k < timeout and not rospy.is_shutdown():
		k+=1
		rospy.sleep(1)
		print robot_name, "WAITING FOR USER CONFIRMATION, [%d/%d]"%(k,timeout)
	
	_feedback.status = Status.COMPLETE_DELIEVERY	
	_as.publish_feedback(_feedback)
	print robot_name, "COMPLETE_DELIEVERY"
	
	_feedback.status = Status.RETURNING_TO_DOCK	
	_as.publish_feedback(_feedback)
	
	k = 0;
	timeout = random.randrange(20,30)
	while k < timeout and not rospy.is_shutdown():
		k+=1
		rospy.sleep(1)
		print robot_name, "RETURNING TO DOCK, [%d/%d]"%(k,timeout)
	
	_feedback.status = Status.END_DELIEVERY_ORDER
	_as.publish_feedback(_feedback)
	print robot_name, "END_DELIEVERY_ORDER"
	_as.set_succeeded(_result)
	
if __name__ == '__main__':
    
	try:
		global robot_num
		robot_num = 5
		
		rospy.init_node('delivery_robot')
		#rospy.Subscriber("delivery_robot_init_pub",Int32,Recv)
		
		#while robot_num == 0:
		#	pass

	
		
		
		global waiter_server; waiter_server = {}
		for k in range(robot_num):
			robot_cnt = k+1	
			robot_name = "waiter_%d/delivery_order"%robot_cnt
			print "Create action server robot_name: ",robot_name
			waiter_server[robot_name] = (actionlib.SimpleActionServer(robot_name,DeliverOrderAction,execute_cb = ExecuteCB))
			waiter_server[robot_name].start()

		"""
		for k in range(robot_num):
			robot_name = "robot_"+str(k+1)
			robot_list[robot_name]="Idle" 
		
		for k in range(robot_num):
			robot_name = "robot_"+str(k+1)
			
			robot_pub_topic = "delivery_"+robot_name+"+order_sub"
			robot_list[robot_name]=dict(state = "Idle", pub=rospy.Publisher(robot_pub_topic, Order))

			robot_sub_topic = "delivery_"+robot_name+"+order_pub"
			rospy.Subscriber(robot_sub_topic,Order, Recv)
		"""
		
		while not rospy.is_shutdown():
			pass
	
	except rospy.ROSInterruptException:
		pass
