#!/usr/bin/env python
import rospy
import std_msgs

import threading
import random

import actionlib
from cafe_msgs.msg import *

class CActionClientCallBack():
	m_user_id = ""
	
	def __init__(self, user_id):
		self.m_user_id = user_id
    	
	def done_cb(self,status,result):

		_tempstr = "User%d"%self.m_user_id + " done_cb"
		rospy.loginfo(_tempstr)

		pass
	
	def active_cb(self,):

		_tempstr = "User%d"%self.m_user_id + " active_cb"
		rospy.loginfo(_tempstr)

		pass

	def feedback_cb(self,data):
		status = ""
		if  data.status == Status.IDLE:
			status = "IDLE"	
		elif data.status == Status.GO_TO_KITCHEN:
			status = "GO_TO_KITCHEN"	
		elif data.status == Status.ARRIVE_KITCHEN:
			status = "ARRIVE_KITCHEN"		
		elif data.status == Status.WAITING_FOR_KITCHEN:
			status = "WAITING_FOR_KITCHEN"	
		elif data.status == Status.IN_DELIVERY:
			status = "IN_DELIVERY"
		elif data.status == Status.ARRIVE_TABLE:
			status = "ARRIVE_TABLE"
		elif data.status == Status.WAITING_FOR_USER_CONFIRMATION:
			status = "WAITING_FOR_USER_CONFIRMATION"
		elif data.status == Status.COMPLETE_DELIVERY:
			status = "COMPLETE_DELIVERY"
		elif data.status == Status.RETURNING_TO_DOCK:
			status = "RETURNING_TO_DOCK"
		elif data.status == Status.END_DELIVERY_ORDER:
			status = "END_DELIVERY_ORDER"
		elif data.status == Status.ERROR:
			status = "ERROR"
		else:
			status = "ERROR"
		


		_tempstr = "User%d"%self.m_user_id+ " feedback_cb: "+str(status)
		rospy.loginfo(_tempstr)

		pass


MENU_NAME = ["Cafe Latte", 
			"Capuccino", 
			"DDal Ba", 
			"Coke", 
			"Americano", 
			"Koreano", 
			"Kobukino", 
			"Sul tang mool"]
def generateMenus():
    
	menus = []

	for i in range(1,4):
		m = Menu()
		m.name = random.choice(MENU_NAME)
		m.size = random.randint(1,3)
		m.qty = random.randint(1,5)
		menus.append(m)
	return menus 

	
if __name__ == '__main__':
    
	try:
		print "=========================Main start==============================="
		rospy.init_node('user_deivce')
		
		client = {}
		user_id = 0
		while not rospy.is_shutdown():
		
			print user_id, "User send goal"
		
			_tempstr = str(user_id)+" User send goal"
			rospy.loginfo(_tempstr)
	
			client[user_id] = (actionlib.SimpleActionClient('send_order',UserOrderAction))
			client[user_id].wait_for_server()
	
			new_order = Order()

			new_order.table_id = random.randrange(1,8)
			new_order.menus = generateMenus()
			new_order.robot_name = ""				
			new_order.order_id = 0
			new_order.status = Status.IDLE
			goal=UserOrderGoal(order=new_order) 		

			pActionClientCB = CActionClientCallBack(user_id)			
			client[user_id].send_goal(goal,pActionClientCB.done_cb,
											pActionClientCB.active_cb, 
											pActionClientCB.feedback_cb)
			user_id+=1
			k = 0;
			timeout = random.randrange(10,15)
			while k < timeout and not rospy.is_shutdown():
				k+=1
				rospy.sleep(1)
				_tempstr = "Next New Generation, [%d/%d]"%(k,timeout)	
				rospy.loginfo(_tempstr)
					
		print "=========================Main end==============================="
		

	except rospy.ROSInterruptException:
		pass
