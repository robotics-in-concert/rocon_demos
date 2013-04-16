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

class CActionClientCallBack():
	m_name = ""
	m_goal_id = ""
	m_RobotStatusList = {}

	def	__init__(self,name,RobotStatusList,goal_id):

		self.m_name = name
		self.m_RobotStatusList = RobotStatusList
		self.m_goal_id = goal_id
		
		pass
			
	def done_cb(self,status,result):
		arg={}
		arg["name"] = self.m_name
		arg["goal_id"] = self.m_goal_id	
		arg["RobotStatusList"] = self.m_RobotStatusList								
		Recv(None,"DoneCB",arg)

	def active_cb(self,):
		arg={}
		arg["name"] = self.m_name
		arg["goal_id"] = self.m_goal_id	
		arg["RobotStatusList"] = self.m_RobotStatusList								
		Recv(None,"ActiveCB",arg)

	
	def feedback_cb(self,data):
		arg={}
		arg["name"] = self.m_name
		arg["goal_id"] = self.m_goal_id	
		arg["RobotStatusList"] = self.m_RobotStatusList								
		Recv(data,"FeedbackCB",arg)


#################################################################
global goal_handle_list; goal_handle_list = {}

def PushGoalHandleList(goal_handle):
	global goal_handle_list
	goal_handle.set_accepted()
	goal_id = goal_handle.get_goal_id().id
	goal_handle_list[goal_id] = goal_handle

def PopGoalHandleList(goal_id):
	global goal_handle_list
	return goal_handle_list.pop(goal_id)
	
def GoalCB(data):
	PushGoalHandleList(data)
	Recv(data,"GoalCB")
#################################################################



########################################################
#Recv	
def Recv(data = None, FuncType = "None", arg = {}):	
	
	cmdset = None
	 
	if FuncType == "GoalCB":
		order = data.get_goal().order
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
		
	elif FuncType == "FeedbackCB":
		name = arg["name"]
		goal_id	= arg["goal_id"]
		RobotStatusList	= arg["RobotStatusList"]
		
		print name, "feedback_cb: ", data
		
		if  data.status == Status.IDLE:
			RobotStatusList[name] = "IDLE"	
		elif data.status == Status.GO_TO_KITCHEN:
			RobotStatusList[name] = "GO_TO_KITCHEN"	
		elif data.status == Status.ARRIVE_KITCHEN:
			RobotStatusList[name] = "ARRIVE_KITCHEN"		
		elif data.status == Status.WAITING_FOR_KITCHEN:
			RobotStatusList[name] = "WAITING_FOR_KITCHEN"	
		elif data.status == Status.IN_DELIVERY:
			RobotStatusList[name] = "IN_DELIVERY"
		elif data.status == Status.ARRIVE_TABLE:
			RobotStatusList[name] = "ARRIVE_TABLE"
		elif data.status == Status.WAITING_FOR_USER_CONFIRMATION:
			RobotStatusList[name] = "WAITING_FOR_USER_CONFIRMATION"
		elif data.status == Status.COMPLETE_DELIEVERY:
			RobotStatusList[name] = "COMPLETE_DELIEVERY"
		elif data.status == Status.RETURNING_TO_DOCK:
			RobotStatusList[name] = "RETURNING_TO_DOCK"
		elif data.status == Status.END_DELIEVERY_ORDER:
			RobotStatusList[name] = "END_DELIEVERY_ORDER"
		elif data.status == Status.ERROR:
			RobotStatusList[name] = "ERROR"
		else:
			RobotStatusList[name] = "ERROR"
		

	elif FuncType == "ActiveCB":
		name = arg["name"]
		goal_id	= arg["goal_id"]
		RobotStatusList	= arg["RobotStatusList"]
		print "active_cb", name

	
	elif FuncType == "DoneCB":
		name = arg["name"]
		goal_id	= arg["goal_id"]
		RobotStatusList	= arg["RobotStatusList"]
		
		while RobotStatusList[name] != "END_DELIEVERY_ORDER":
			print name, "waiting the last feedback callback"
			rospy.sleep(0.1)
		
		RobotStatusList[name] = "IDLE"
		
		print "done_cb", name, RobotStatusList
		
		cmdset = commandset.CCmdSet("StatusEvent",'EVENT_MESSAGE')
		cmdset.setString('goal_id',goal_id)
		cmdset.setString('status',"IDLE")	

	if cmdset != None:	
		EventProc(cmdset)	

#Event proc
def EventProc(cmdset):
	##MessageRecvSrv
	if MessageRecvSrv_EvtList.keys().count(cmdset.m_cmdname):
		callSrvCBFlag = False
		
		if cmdset.m_cmdname == 'NewOrderEvent':
			callSrvCBFlag = True
		
		elif cmdset.m_cmdname == 'StatusEvent':
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
			print "Call CallbackFunc ", cmdset.m_cmdname
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
MessageRecvSrv_EvtList = {'NewOrderEvent':'GlobalEvent', "StatusEvent":"GlobalEvent"}

global MessageRecvSrv_GlobalEvtFlag; MessageRecvSrv_GlobalEvtFlag = False
global MessageRecvSrv_cmdset; MessageRecvSrv_cmdset = commandset.CCmdSet()
global MessageRecvSrv_OrderList; MessageRecvSrv_OrderList = []
global MessageRecvSrv_RemapingList; MessageRecvSrv_RemapingList = {}

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
		
		elif cmdset.m_cmdname == 'StatusEvent':
			self.m_cmdsetList.append(cmdset) 	
		pass
	
	def execute(self, userdata):
		global MessageRecvSrv_cmdset
		
		while  not rospy.is_shutdown():
			while len(self.m_cmdsetList) == 0 and not rospy.is_shutdown():
					time.sleep(0.01)		
					pass
			cmdset = self.m_cmdsetList.pop(0)

			if cmdset.m_cmdname == 'NewOrderEvent':
				MessageRecvSrv_cmdset = cmdset				
				return 'call_order_event'

			elif cmdset.m_cmdname == 'StatusEvent':
				MessageRecvSrv_cmdset = cmdset
				return 'call_status_event'

		print "MessageRecvSrv_Idle(smach.State):--------------------------------"
		return 'end'

		
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
		global MessageRecvSrv_RemapingList
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
		MessageRecvSrv_RemapingList[MessageRecvSrv_cmdset.getValue("goal_id")] = self.m_OrderID
		
		#send message delivery order queue
		MessageRecvSrv_cmdset.setCmdName("DeliveryOrderEvent")
		EventProc(MessageRecvSrv_cmdset)
		
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
		global MessageRecvSrv_cmdset
		global MessageRecvSrv_OrderList	
		global MessageRecvSrv_RemapingList
		global kitchen_mgr_pub
		
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
		status = MessageRecvSrv_cmdset.getValue("status")
		goal_id  = MessageRecvSrv_cmdset.getValue("goal_id")
		
		print "Call Status Event", goal_id,status

		if status != "IDLE":
		##Robot Status update
			pass
		else:
		##Robot Status update
			print "Call Status Event", goal_id,status
			#send data to user device
			goal_handle = PopGoalHandleList(goal_id)
			_result = UserOrderResult()
			goal_handle.set_succeeded(_result)
			
			#pop the order
			order_id = MessageRecvSrv_RemapingList.pop(goal_id)
			for k in MessageRecvSrv_OrderList:
				if k.order_id == order_id:
					MessageRecvSrv_OrderList.remove(k)
					break
					
			#send data to kitchen mgr
			order_list = OrderList()
			order_list.orders = MessageRecvSrv_OrderList

			kitchen_mgr_pub.publish(MessageRecvSrv_OrderList)		
			pass
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
		global DeliverySrv_cmdset
		
		while True and not rospy.is_shutdown() :
			while len(self.m_cmdsetList) == 0 and not rospy.is_shutdown():
					time.sleep(0.01)		
					pass
			cmdset = self.m_cmdsetList.pop(0)
			print "DeliverySrv Pop order: ",len(self.m_cmdsetList)
			
			if cmdset.m_cmdname == 'DeliveryOrderEvent':
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
		
		#cmdset -> Order
		o = Order()
		o.table_id = DeliverySrv_cmdset.getValue('table_id')
		#parsing menus
		menus = []		
		strMenu = DeliverySrv_cmdset.getValue("menus")
		for k in strMenu.split('/'):
			if len(k) != 0:
				m = Menu()
				m.name = str(k.split('_')[0])
				m.size = int(k.split('_')[1])
				m.qty = int(k.split('_')[2])
				menus.append(m)
						
		o.menus = menus
		o.robot_name = "None"
		o.order_id = DeliverySrv_cmdset.getValue('order_id')
		
		global RobotStatusList
		#check robot
		print RobotStatusList
				
		checkRobotStatusFlag = True	
		while checkRobotStatusFlag and not rospy.is_shutdown():
			for k in RobotStatusList.keys():
				if RobotStatusList[k] == "IDLE":
				
					RobotStatusList[k] = "GO_TO_KITCHEN" 	
					o.status = Status.GO_TO_KITCHEN
					o.robot_name = k
				
					goal=UserOrderGoal(order=o) 
					pActionClientCB = CActionClientCallBack(k,
															RobotStatusList,
															DeliverySrv_cmdset.getValue("goal_id"))
					
					waiter_client[k].send_goal(goal,pActionClientCB.done_cb,
													pActionClientCB.active_cb, 
													pActionClientCB.feedback_cb)
													
					checkRobotStatusFlag = False
				
					break;
			rospy.sleep(1)
		
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
	robot_num = 5

	global waiter_client; waiter_client = {}
	global RobotStatusList; RobotStatusList = {}


	for k in range(robot_num):
			robot_cnt = k+1	
			robot_name = "waiter_%d"%robot_cnt
			RobotStatusList[robot_name]="IDLE"
			print "Create action client robot_name: ",robot_name
			waiter_client[robot_name] = actionlib.SimpleActionClient(robot_name+"/delivery_order",
																	DeliverOrderAction)
			waiter_client[robot_name].wait_for_server()															

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

