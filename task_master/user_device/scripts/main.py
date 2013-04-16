#!/usr/bin/env python
import rospy
import std_msgs

import threading
import random

import actionlib
from cafe_msgs.msg import *

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
    
def done_cb(status,result):
	print "done_cb: status", status ,type(status)
	print "done_cb: result", result ,type(result)
	
	pass
	
def active_cb():
	print "active_cb: "
	pass
	
def feedback_cb(data):
	print "feedback_cb: ", data  ,type(data)
	pass
	
if __name__ == '__main__':
    
	try:
		print "=========================Main start==============================="
		rospy.init_node('user_deivce')
		
		client = []
		i = 0
		while not rospy.is_shutdown():
		
			print i, "Send Goal"
		
			client.append(actionlib.SimpleActionClient('send_order',UserOrderAction))
			client[i].wait_for_server()
	
			new_order = Order()

			new_order.table_id = random.randrange(1,7)
			new_order.menus = generateMenus()
			new_order.robot_name = ""				
			new_order.order_id = 0
			new_order.status = Status.IDLE
			goal=UserOrderGoal(order=new_order) 		
		
			client[i].send_goal(goal,done_cb,active_cb, feedback_cb)
			i+=1
			
			k = 0;
			timeout = random.randrange(10,15)
			while k < timeout and not rospy.is_shutdown():
				k+=1
				rospy.sleep(1)
				print "Next New Generation, [%d/%d]"%(k,timeout)	
		
		print "=========================Main end==============================="
		

	except rospy.ROSInterruptException:
		pass
