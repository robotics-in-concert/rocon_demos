#!/usr/bin/env python
# -*- coding:utf-8 -*-


import rospy
import time

import threading
import random

import actionlib

from std_msgs.msg import *
from cafe_msgs.msg import *
		
class CRobotCallBack():
	m_name = ""
	def	__init__(self,name):
		self.m_name = name
		pass
			
	def done_cb(self,status,result):
		print "done_cb: status", status ,type(status)
		print "done_cb: result", result ,type(result)
		RobotStatusList[self.m_name] = "IDLE"
		pass
	
	def active_cb(self,):
		print "active_cb: "
		pass
	
	def feedback_cb(self,data):	
		global RobotStatusList
		print self.m_name, "feedback_cb: ", data
		
		if  data.status == Status.IDLE:
			RobotStatusList[self.m_name] = "IDLE"
		elif data.status == Status.GO_TO_KITCHEN:
			RobotStatusList[self.m_name] = "GO_TO_KITCHEN"
		elif data.status == Status.ARRIVE_KITCHEN:
			RobotStatusList[self.m_name] = "ARRIVE_KITCHEN"
		elif data.status == Status.WAITING_FOR_KITCHEN:
			RobotStatusList[self.m_name] = "WAITING_FOR_KITCHEN"
		elif data.status == Status.IN_DELIVERY:
			RobotStatusList[self.m_name] = "IN_DELIVERY"
		elif data.status == Status.ARRIVE_TABLE:
			RobotStatusList[self.m_name] = "ARRIVE_TABLE"
		elif data.status == Status.WAITING_FOR_USER_CONFIRMATION:
			RobotStatusList[self.m_name] = "WAITING_FOR_USER_CONFIRMATION"
		elif data.status == Status.COMPLETE_DELIEVERY:
			RobotStatusList[self.m_name] = "COMPLETE_DELIEVERY"
		elif data.status == Status.RETURNING_TO_DOCK:
			RobotStatusList[self.m_name] = "RETURNING_TO_DOCK"
		elif data.status == Status.END_DELIEVERY_ORDER:
			RobotStatusList[self.m_name] = "END_DELIEVERY_ORDER"
		elif data.status == Status.ERROR:
			RobotStatusList[self.m_name] = "ERROR"
		else:
			RobotStatusList[self.m_name] = "ERROR"
		
			
		

			
MENU_NAME = ["Cafe Latte", "Capuccino", "DDal Ba", "Coke", "Americano", "Koreano", "Kobukino", "Sul tang mool"]
ROBOT_NAME = ["Kobuki", "Guimul", "KobukKobuk","Snail","Jola Bbareun Kobuki","Motorized Kobuki"]

def generateMenus():
    menus = []
    for i in range(1,4):
        m = Menu()
        m.name = random.choice(MENU_NAME)
        m.size = random.randint(1,3)
        m.qty = random.randint(1,500)
        menus.append(m)

    return menus 

def generateFakeOrder(order_num):
    o = Order()
    o.table_id = random.randint(0,10)
    o.menus = generateMenus()
    o.robot_name = None
    o.order_id = order_num
    return o
    
def OrderGenFunc():
	global OrderList;
	num_order = 0
	while not rospy.is_shutdown():
			num_order = num_order + 1
			order = generateFakeOrder(num_order)
			print "New Order Generation: %d/%d" %(num_order, len(OrderList))
			OrderList.append(order)
			k = 0;
			timeout = random.randrange(15,20)

			while k < timeout and not rospy.is_shutdown():
				k+=1
				rospy.sleep(1)
				print "Next New Generation, [%d/%d]"%(k,timeout)
			
if __name__ == '__main__':
    
	try:	
		print "=========================Main start==============================="
		
		rospy.init_node('task_coordinator', anonymous = True)	
		global OrderList; OrderList = []

		robot_num = 5	
		waiter_client = {}
		RobotStatusList = {}
		
		for k in range(robot_num):
			robot_cnt = k+1	
			robot_name = "waiter_%d/delivery_order"%robot_cnt
			RobotStatusList[robot_name]="Idle"
			print "Create action client robot_name: ",robot_name
			waiter_client[robot_name] = actionlib.SimpleActionClient(robot_name,DeliverOrderAction)

		for k in RobotStatusList.keys():
			waiter_client[k].wait_for_server()
		
		ThreadOrderGenFunc = threading.Thread(target=OrderGenFunc, args=())
		ThreadOrderGenFunc.start()

						

		
		#new order generation		
		while not rospy.is_shutdown():
			while len(OrderList) == 0 and not rospy.is_shutdown():
				rospy.sleep(0.1)

			o=OrderList[0]
			OrderList.remove(o)
			print RobotStatusList.values()
		
			#check robot		
			checkRobotStatusFlag = True	
			while checkRobotStatusFlag and not rospy.is_shutdown():
				for k in RobotStatusList.keys():
					if RobotStatusList[k] == "Idle":
					
						RobotStatusList[k] = "GO_TO_KITCHEN" 	
						o.status = Status.GO_TO_KITCHEN
						o.robot_name = k
					
						goal=UserOrderGoal(order=o) 
						pRobotCallBack = CRobotCallBack(k)
						
						waiter_client[k].send_goal(goal,pRobotCallBack.done_cb,
														pRobotCallBack.active_cb, 
														pRobotCallBack.feedback_cb)
														
						checkRobotStatusFlag = False
					
						break;
				rospy.sleep(1)

			
		
		
		
		
		#send Goal
		
		#ThreadFakeFeedbackFunc = threading.Thread(target=FakeFeedbackFunc, args=())
		#ThreadFakeFeedbackFunc.start()
			
		
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
