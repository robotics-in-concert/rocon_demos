#!/usr/bin/env python
# -*- coding:utf-8 -*-


import rospy
import smach
import smach_ros
import time

import commandset

import actionlib

from std_msgs.msg import *
from cafe_msgs.msg import *


#client program
########################################################
#todo



#################################################################
global goal_handle_list; goal_handle_list = []

def PushGoalHandleList(goal_handle):
	global goal_handle_list
	goal_handle_list.append(goal_handle)

def PopGoalHandleList(goal_handle):
	global goal_handle_list
	goal_handle_list.remove(goal_handle)

def GoalCB(data):
	PushGoalHandleList(data)
	Recv(data)
#################################################################



########################################################
#Recv	
def Recv(data):
	order = data.get_goal().order
	#print order	

	#feedback = UserOrderFeedback()
	#feedback.status = Status.GO_TO_KITCHEN

	#print "feedback: ", feedback, type(feedback)
	#print "Status.GO_TO_KITCHEN: ", Status.GO_TO_KITCHEN, type(Status.GO_TO_KITCHEN)
	
	#global user_device_action_server;	
	#user_device_action_server.publish_feedback(feedback)
	#user_device_action_server.accept_new_goal()
	
	cmdset = commandset.CCmdSet("NewOrderEvent",'EVENT_MESSAGE')
	cmdset.setInt('table_id',order.table_id)
	cmdset.setString('robot_name',order.robot_name)	
	cmdset.setString('goal_id',data.get_goal_id().id)
	cmdset.setInt('status',order.status)	
	
	strMenu = ""
	for k in order.menus:
		strMenu+= "/"
		strMenu+= str(k.name)+"_"
		strMenu+= str(k.size)+"_"
		strMenu+= str(k.qty)
	
	cmdset.setString('menus',strMenu)	

	EventProc(cmdset)
		
	"""
	cmdset = None
	if data._connection_header['topic'] == '/user_device_order_sub':
		cmdset = commandset.CCmdSet('NewOrderEvent','EVENT_MESSAGE','user_device', 'task_coordinator')	
		print "Call Recv Function- cmdset.m_cmdname: [%s]"%cmdset.m_cmdname

	
	elif data._connection_header['topic'] == '/food_preparation_order_sub': 
		pass	
		#cmdset = commandset.CCmdSet('FoodPreParationCompleteEvent','EVENT_MESSAGE','kitchen_manager', 'task_coordinator')
		#print "Call Recv Function- cmdset.m_cmdname: [%s]"%cmdset.m_cmdname	
	
	elif data._connection_header['topic'].count('/delivery_robot_') :

		if data.status == "Preparation Complete":
			cmdset = commandset.CCmdSet('FoodPreParationCompleteEvent','EVENT_MESSAGE',robot_name, 'task_coordinator')	
		else:
			robot_name = "robot_"+data._connection_header['topic'].split('_')[3]
			cmdset = commandset.CCmdSet('ArrivalEvent','EVENT_MESSAGE',robot_name, 'task_coordinator')	
	
		print "Call Recv Function- cmdset.m_cmdname: [%s]"%cmdset.m_cmdname		
	
	if cmdset != None:
	
		cmdset.setInt('UserID',data.user_id)
		cmdset.setInt('TableID',data.table_id)	
		cmdset.setInt('RobotID',data.robot_id)	
		cmdset.setString('Status',data.status)	

		EventProc(cmdset)
	"""
	pass

#Event proc
def EventProc(cmdset):
	##MessageRecvSrv
	if MessageRecvSrv_EvtList.keys().count(cmdset.m_cmdname):
		callSrvCBFlag = False
		
		if cmdset.m_cmdname == 'NewOrderEvent':
			callSrvCBFlag = True
		else:
			pass
		
		if callSrvCBFlag:		
			print "Call CallbackFunc ",cmdset.m_cmdname
			for i in range(len(MessageRecvSrv_CBList)):
				MessageRecvSrv_CBList[i](cmdset)
	

				
	##DeliverySrv			
	if DeliverySrv_EvtList.keys().count(cmdset.m_cmdname):
		callSrvCBFlag = False
		#cmdset.printCmdSet()

		if cmdset.m_cmdname == 'DeliveryOrderEvent' :
			callSrvCBFlag = True 
		
		else:
			pass
		
		if callSrvCBFlag:		
			print "Call CallbackFunc ",cmdset.m_cmdname
			for i in range(len(DeliverySrv_CBList)):
				DeliverySrv_CBList[i](cmdset)
	
	
	pass


#RegEventProc
def RegEventProc(SrvName, cb):
	if SrvName.count('MessageRecvSrv'): 
		MessageRecvSrv_CBList.append(cb)

	elif SrvName.count('DeliverySrv'): 
		DeliverySrv_CBList.append(cb)

	else:
		pass

#######################################################################################################
##Define Service
#######################################################################################################
##MessageRecvSrv ############################################################

MessageRecvSrv_CBList = []
MessageRecvSrv_EvtList = {'NewOrderEvent':'GlobalEvent'}

global MessageRecvSrv_GlobalEvtFlag; MessageRecvSrv_GlobalEvtFlag = False
global MessageRecvSrv_cmdset; MessageRecvSrv_cmdset = commandset.CCmdSet()
global MessageRecvSrv_OrderList; MessageRecvSrv_OrderList = []

class MessageRecvSrv_Init(smach.State):
	def __init__(self):
		smach.State.__init__(self, outcomes=['success','retry','failure'])
	
	def execute(self, userdata):
		time.sleep(1)
		return 'success'

	
class MessageRecvSrv_Idle(smach.State):
	m_cmdsetList = []
	
	def __init__(self):
		smach.State.__init__(self, outcomes = ['call_order_event','call_status_event', 'retry','failure'])
		RegEventProc(self.__class__.__name__, self.listener)
		
	def listener(self,cmdset):
		if cmdset.m_cmdname ==  'NewOrderEvent':
			self.m_cmdsetList.append(cmdset) 	
		
		elif cmdset.m_cmdname ==  'StatusEvent':
			self.m_cmdsetList.append(cmdset) 	
		pass
	
	def execute(self, userdata):
		global MessageRecvSrv_cmdset
		
		while  not rospy.is_shutdown():
			while len(self.m_cmdsetList) == 0:
					time.sleep(0.01)		
					pass
			cmdset = self.m_cmdsetList.pop(0)

			if cmdset.m_cmdname == 'NewOrderEvent':
				MessageRecvSrv_cmdset = cmdset				
				return 'call_order_event'

			elif cmdset.m_cmdname == 'StatusEvent':
				MessageRecvSrv_cmdset = cmdset
				return 'call_status_event'

		
class MessageRecvSrv_CallOrderEvent(smach.State):
	m_IsRunning = [True]
	m_OrderID = 0 
	def __init__(self):
		smach.State.__init__(self, outcomes = ['success','retry','failure'])
		RegEventProc(self.__class__.__name__, self.listener)
	
	def listener(self,cmdset):
		
		global MessageRecvSrv_GlobalEvtFlag
		if cmdset.m_cmdname ==  'NewOrderEvent':
			MessageRecvSrv_GlobalEvtFlag = True	 	
		elif cmdset.m_cmdname ==  'StatusEvent':
			MessageRecvSrv_GlobalEvtFlag = True	
		pass
		
	def execute(self,userdata):
		global MessageRecvSrv_cmdset
		global MessageRecvSrv_OrderList	
		global kitchen_mgr_pub
		#print "MessageRecvSrv_PushOrder Start"

		"""
		global MessageRecvSrv_GlobalEvtFlag	
		ResultCode = 'retry'

		if MessageRecvSrv_GlobalEvtFlag == True:			
			MessageRecvSrv_GlobalEvtFlag = False
			MessageRecvSrv = 'failure'
			return ResultCode
		"""
		
		#assgine Order ID
		self.m_OrderID+=1
		MessageRecvSrv_cmdset.setInt("order_id",self.m_OrderID)
		
		#send message delivery order queue
		MessageRecvSrv_cmdset.setCmdName("DeliveryOrderEvent")
		#EventProc(MessageRecvSrv_cmdset)
		
		#send message to kitchen mgr
		o = Order()
		o.table_id = MessageRecvSrv_cmdset.getValue('table_id')
		
		#parsing menuse
		menus = []		
		strMenu = MessageRecvSrv_cmdset.getValue("menus")

		for k in strMenu.split('/'):
			if len(k) != 0:
				m = Menu()
				m.name = str(k.split('_')[0])
				m.size = int(k.split('_')[1])
				m.qty = int(k.split('_')[2])
				menus.append(m)
				
		o.menus = menus
		o.robot_name = "None"
		o.order_id = MessageRecvSrv_cmdset.getValue('order_id')
		
		MessageRecvSrv_OrderList.append(o)

		order_list = OrderList()
		order_list.orders = MessageRecvSrv_OrderList

		kitchen_mgr_pub.publish(MessageRecvSrv_OrderList)

		return 'success'
		
		
		#send event
		
		##Action
		#self.m_IsRunning =[True]	
		#Ret = {}
		#Thread_GotoDirEx = threading.Thread(target=GotoDirEx, args=(self.m_IsRunning,Ret, 1, 65535, True))
		#Thread_GotoDirEx.start()		
		#while self.m_IsRunning[0] == True:
		#	if RemoteSrv_GlobalEvtFlag == True:				
		#		RemoteSrv_GlobalEvtFlag = False
		#		ResultCode =  'failure'
		#		return ResultCode
		#	pass		
		#while Thread_GotoDirEx.isAlive():
		#	pass
		#
		#if Ret['ResultCode'] == 0:
		#	ResultCode = 'success'
		#else:
		#	ResultCode = 'failure'
	
class MessageRecvSrv_CallStatusEvent(smach.State):
	m_IsRunning = [True]
	
	def __init__(self):
		smach.State.__init__(self, outcomes = ['success','retry','failure'])
		RegEventProc(self.__class__.__name__, self.listener)
	
	def listener(self,cmdset):
		global MessageRecvSrv_GlobalEvtFlag
		if cmdset.m_cmdname ==  'NewOrderEvent':
			MessageRecvSrv_GlobalEvtFlag = True	 	
		elif cmdset.m_cmdname ==  'StatusEvent':
			MessageRecvSrv_GlobalEvtFlag = True	
		pass
		
	def execute(self,userdata):
		#print "MessageRecvSrv_CallStatusEvent Start"

		"""
		global MessageRecvSrv_GlobalEvtFlag	
		ResultCode = 'retry'

		if MessageRecvSrv_GlobalEvtFlag == True:			
			MessageRecvSrv_GlobalEvtFlag = False
			MessageRecvSrv = 'failure'
			return ResultCode
		"""
		##Receive Status
		
		##Robot Status update

		##Send order status
		

		return 'success'
		
			
##DeliverySrv ############################################################

DeliverySrv_CBList = []
DeliverySrv_EvtList = {'DeliveryOrderEvent':'GlobalEvent'}
DeliverySrv_GlobalEvtFlag = False

global DeliverySrv_cmdset; DeliverySrv_cmdset = commandset.CCmdSet()
global DeliverySrv_RobotStatusList; DeliverySrv_RobotStatusList = {}

global robot_num; robot_num = 5	
for k in range(robot_num):
	robot_name = "robot_"+str(k+1)
	DeliverySrv_RobotStatusList[robot_name]="Idle" 

	
class DeliverySrv_Init(smach.State):
	def __init__(self):
		smach.State.__init__(self, outcomes=['success','retry','failure'])
	
	def execute(self, userdata):
		time.sleep(1)
		return 'success'

	
class DeliverySrv_Idle(smach.State):
	m_cmdsetList =[]
	
	def __init__(self):
		smach.State.__init__(self, outcomes = ['check_robot', 'retry','failure'])
		RegEventProc(self.__class__.__name__, self.listener)
		
	def listener(self,cmdset):
		
		if cmdset.m_cmdname == 'DeliveryOrderEvent':
			self.m_cmdsetList.append(cmdset) 
			
		print "DeliverySrv Push order: ",len(self.m_cmdsetList)	
		pass
		
	def execute(self, userdata):
		while True and not rospy.is_shutdown() :
			while len(self.m_cmdsetList) == 0:
					time.sleep(0.01)		
					pass
			cmdset = self.m_cmdsetList.pop(0)
			print "DeliverySrv Pop order: ",len(self.m_cmdsetList)
			
			if cmdset.m_cmdname == 'DeliveryOrderEvent':
				global DeliverySrv_cmdset
				DeliverySrv_cmdset = cmdset				
				return 'check_robot'	



class DeliverySrv_CheckRobot(smach.State):
	m_IsRunning = [True]
	
	def __init__(self):
		smach.State.__init__(self, outcomes = ['success', 'retry','failure'])
		RegEventProc(self.__class__.__name__, self.listener)
		
	def listener(self,cmdset):
		global DeliverySrv_GlobalEvtFlag
		if cmdset.m_cmdname ==  'DeliveryOrderEvent':
			DeliverySrv_GlobalEvtFlag = True	
		
			

	def execute(self, userdata):
		
		"""
		global DeliverySrv_GlobalEvtFlag	
		ResultCode = 'retry'

		if DeliverySrv_GlobalEvtFlag == True:			
			DeliverySrv_GlobalEvtFlag = False
			DeliverySrv = 'failure'
			return ResultCode			
		"""
		global robot_num
		global DeliverySrv_RobotStatusList

		checkRobotStatusFlag = True	
		while checkRobotStatusFlag:
			print "DeliverySrv_RobotStatusList", DeliverySrv_RobotStatusList
			for k in range(robot_num):
				robot_name = "robot_"+str(k+1)
				if DeliverySrv_RobotStatusList[robot_name] == "Idle":
					DeliverySrv_RobotStatusList[robot_name] = "GO_TO_KITCHEN" 	
					userdata.robot_name = robot_name
					checkRobotStatusFlag = False
					break;
			rospy.sleep(1)
		
		print "DeliverySrv_RobotStatusList", DeliverySrv_RobotStatusList
		return 'pushorder'	


class DeliverySrv_PushOrder(smach.State):
	m_IsRunning = [True]
	
	def __init__(self):
		smach.State.__init__(self, outcomes = ['success','retry','failure'],input_keys = ["robot_name"])
		RegEventProc(self.__class__.__name__, self.listener)
	
	def listener(self,cmdset):
		global DeliverySrv_GlobalEvtFlag
		
		if cmdset.m_cmdname ==  'RobotDeliveryOrderEvent' and cmdset.getValue('Status') == "Delivery":
			DeliverySrv_GlobalEvtFlag = True	
		pass
		
	def execute(self,userdata):
		#print "DeliverySrv_PushOrder State Start"
		
		"""
		global DeliverySrv_GlobalEvtFlag	
		ResultCode = 'retry'

		if DeliverySrv_GlobalEvtFlag == True:			
			DeliverySrv_GlobalEvtFlag = False
			DeliverySrv = 'failure'
			return ResultCode
		"""			
		
		global DeliverySrv_cmdset	
		
		#user event		
		robot_name = userdata.robot_name
		robot_delivery_order = Order()
		cmdset = DeliverySrv_cmdset
		cmdset.setInt("RobotID",int(robot_name.split("_")[1]))
		cmdset.setString("Status","Call")
		
		robot_delivery_order.user_id = cmdset.getValue('UserID')
		robot_delivery_order.table_id = cmdset.getValue('TableID')
		robot_delivery_order.robot_id = cmdset.getValue('RobotID')
		robot_delivery_order.status = cmdset.getValue('Status')
		
		print robot_delivery_order.user_id, robot_delivery_order.table_id, robot_delivery_order.robot_id, robot_delivery_order.status

		robot_pub_topic = "delivery_order_"+robot_name+"_pub"
		robot_pub_list[robot_name].publish(robot_delivery_order)
			
		return 'success'
	
#######################################################################################################
##Define Action
####################################################################################################### 


#######################################################################################################
##Main
####################################################################################################### 

def main():
	print "=========================Main start==============================="

	rospy.init_node('task_coordinator', anonymous = True)	
	####################################################
	global user_device_action_server
	user_device_action_server =  actionlib.ActionServer('send_order',UserOrderAction,GoalCB)
	
	global kitchen_mgr_pub
	kitchen_mgr_pub = rospy.Publisher('fake_orderlist',OrderList,latch = True)
	####################################################
	

	
	####################################################
	#init
	global robot_num; 
	robot_num = 3
	#robot_init_pub.publish(robot_num)
	
	waiter_1_client = actionlib.SimpleActionClient('waiter_1/delivery_order',DeliveryOrderAction)
	waiter_2_client = actionlib.SimpleActionClient('waiter_2/delivery_order',UserOrderAction)
	waiter_3_client = actionlib.SimpleActionClient('waiter_3/delivery_order',UserOrderAction)
	
	####################################################
			
	sm_top = smach.Concurrence(outcomes=['end'], default_outcome = 'end',  outcome_map = {'end':
												{'MessageRecvSrv':'end',
												'DeliverySrv':'end',
												}})
	with sm_top:
		sm_MessageRecvSrv = smach.StateMachine(outcomes = ['end'])
		sm_DeliverySrv = smach.StateMachine(outcomes = ['end'])		
		
		with sm_MessageRecvSrv:
			smach.StateMachine.add('MessageRecvSrv_Init', MessageRecvSrv_Init(), 
														transitions={'success':'MessageRecvSrv_Idle', 
																	'failure':'end', 
																	'retry':'MessageRecvSrv_Init'})
			
			
			smach.StateMachine.add('MessageRecvSrv_CallOrderEvent', MessageRecvSrv_CallOrderEvent(), 
														transitions={'success':'MessageRecvSrv_Idle', 
																	'failure':'end', 
																	'retry':'MessageRecvSrv_CallOrderEvent'})		

			smach.StateMachine.add('MessageRecvSrv_CallStatusEvent', MessageRecvSrv_CallStatusEvent(), 
														transitions={'success':'MessageRecvSrv_Idle', 
																	'failure':'end', 
																	'retry':'MessageRecvSrv_CallStatusEvent'})	
			
			
			smach.StateMachine.add('MessageRecvSrv_Idle', MessageRecvSrv_Idle(), 
														transitions={'call_order_event':'MessageRecvSrv_CallOrderEvent',
																'call_status_event':'MessageRecvSrv_CallStatusEvent',
																'failure':'end', 
																'retry':'MessageRecvSrv_Init'})
			pass
		with sm_DeliverySrv:
			
			smach.StateMachine.add('DeliverySrv_Init', DeliverySrv_Init(), 
														transitions={'success':'DeliverySrv_Idle', 'failure':'end', 'retry':'DeliverySrv_Init'})
			
			smach.StateMachine.add('DeliverySrv_CheckRobot', DeliverySrv_CheckRobot(), 
														transitions={'success':'DeliverySrv_Idle', 'failure':'end', 'retry':'DeliverySrv_CheckRobot'},
														)		
			
			smach.StateMachine.add('DeliverySrv_Idle', DeliverySrv_Idle(), 
														transitions={'check_robot':'DeliverySrv_CheckRobot',
																'failure':'end', 
																'retry':'DeliverySrv_Init'})			
			pass
		
		smach.Concurrence.add('MessageRecvSrv', sm_MessageRecvSrv)
		smach.Concurrence.add('DeliverySrv', sm_DeliverySrv)				
		
	outcome = sm_top.execute()



	print "=========================Main end================================="



if __name__ == '__main__':
    main()

