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
    

"""
global pub

global order_list; order_list = {}

def Recv(data):
	order_list[data.user_id].status = 'Arrival' 
	

def NewOrderGeneration():   
	global order_list
	global pub
	global user_id
	user_id = user_id +1

	new_order = Order()
	new_order.user_id = user_id
	new_order.table_id = random.randrange(1,7)
	new_order.robot_id = -1
	new_order.status = 'Idle'
	pub.publish(new_order)
	order_list[user_id] = new_order
	print "New Order Generation[userID: %d][tableID: %d]"%(new_order.user_id,new_order.table_id)
	
	
	while new_order.status != 'Arrival' or rospy.is_shutdown():
		print "Arrival [userID: %d][tableID: %d]"%(new_order.user_id)
		rospy.sleep(1)
		pass
"""	
	
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
			i+=0
			
			
			k = 0;
			timeout = random.randrange(15,20)
			while k < timeout and not rospy.is_shutdown():
				k+=1
				rospy.sleep(1)
				print "Next New Generation, [%d/%d]"%(k,timeout)	
		
		while not rospy.is_shutdown():
			result = client[i].get_result()		
			print i, " result: ", result, type(result)
			rospy.sleep(3)

			
		print "=========================Main end==============================="
		
		"""
		global pub
		pub = rospy.Publisher('user_device_order_sub', Order)
		
		
		rospy.Subscriber("user_device_order_pub",Order,Recv)

		i = 0
		timeout = random.randrange(5,10)+5
		#timeout = 10
		while i< timeout or rospy.is_shutdown():
			i+=1
			rospy.sleep(1)
		
			ThreadNewOrderGenerator = threading.Thread(target=NewOrderGeneration, args=())
			ThreadNewOrderGenerator.start()
		
			print "Wait next order %d/%d"%(i,timeout)
		"""
		
	
	except rospy.ROSInterruptException:
		pass
