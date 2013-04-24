#!/usr/bin/env python
# -*- coding:utf-8 -*-
import time

#
import commandset

#
import rospy

import smach_ros
import smach

import actionlib
from cafe_msgs.msg import *


#client program
########################################################
class CActionClientCallBack():
	m_robot_name = ""
	m_goal_id = ""
	m_called_last_feedback = False
	m_repair_cnt = 0
	def	__init__(self,robot_name,goal_id):
		
		self.m_robot_name = robot_name
		self.m_goal_id = goal_id
		self.m_called_last_feedback = False
		self.m_repair_cnt = 0
		
		#_tempstr = "Create ActionClientCallBack: ["+ self.m_robot_name+"] ["+ self.m_goal_id+"]"
		#rospy.loginfo(_tempstr)
		
		pass
			
	def done_cb(self,status,result):
		
		while self.m_called_last_feedback == False and not rospy.is_shutdown():
			_tempstr = "Waiting feedback cb[ "+self.m_robot_name+"] ["+self.m_goal_id +"]"
			rospy.logwarn(_tempstr)
			rospy.sleep(0.1)
			
			if self.m_repair_cnt > 60:
				_tempstr = "Last Feedback don't called and Repair[ "+self.m_robot_name+"] ["+self.m_goal_id +"]"
				rospy.logerr(_tempstr)
				break;
			else:
				self.m_repair_cnt +=1
				
		self.m_called_last_feedback = False
		
		arg={}
		arg["robot_name"] = self.m_robot_name
		arg["goal_id"] = self.m_goal_id							
		
		#_tempstr = "Call Done Function[ "+self.m_robot_name+"] ["+self.m_goal_id +"]"
		#rospy.loginfo(_tempstr)
		
		Recv(None,"DoneCB",arg)
		
	def active_cb(self,):
		arg={}
		arg["robot_name"] = self.m_robot_name	
		arg["goal_id"] = self.m_goal_id					
		Recv(None,"ActiveCB",arg)
	
	def feedback_cb(self,data):
		#if data.status == Status.END_DELIVERY_ORDER:
			#_tempstr = "Before Call Last FeedBack Function[ "+self.m_robot_name+"] ["+self.m_goal_id +"]"
			#rospy.loginfo(_tempstr)
			
		arg={}
		arg["robot_name"] = self.m_robot_name
		arg["goal_id"] = self.m_goal_id							
		Recv(data,"FeedbackCB",arg)
		
		if data.status == Status.END_DELIVERY_ORDER:
			self.m_called_last_feedback = True
			#_tempstr = "After Call Last FeedBack Function[ "+self.m_robot_name+"] ["+self.m_goal_id +"]"
			#rospy.loginfo(_tempstr)


#################################################################
global goal_handle_list; goal_handle_list = {}
global active_goal_handle_list; active_goal_handle_list = {}

def PushGoalHandleList(goal_handle):
	global goal_handle_list
	goal_handle.set_accepted()
	goal_id = goal_handle.get_goal_id().id
	goal_handle_list[goal_id] = goal_handle

def PopGoalHandleList(goal_id):
	global goal_handle_list
	goal_handle_list.pop(goal_id)

def GetGoalHandle(goal_id):
	global goal_handle_list
	return goal_handle_list[goal_id]

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
		robot_name = arg["robot_name"]
		goal_id	= arg["goal_id"]
				
		cmdset = commandset.CCmdSet("StatusEvent",'EVENT_MESSAGE')
		cmdset.setString('goal_id',goal_id)
		cmdset.setString('robot_name',robot_name)
		cmdset.setInt('status',data.status)
		
	elif FuncType == "ActiveCB":
		robot_name = arg["robot_name"]
		goal_id	= arg["goal_id"]

	elif FuncType == "DoneCB":
		robot_name = arg["robot_name"]
		goal_id	= arg["goal_id"]

		cmdset = commandset.CCmdSet("StatusEvent",'EVENT_MESSAGE')
		cmdset.setString('goal_id',goal_id)
		cmdset.setString('robot_name',robot_name)
		cmdset.setInt('status',Status.IDLE)
	
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
			for i in range(len(MessageRecvSrv_CBList)):
				MessageRecvSrv_CBList[i](cmdset)
	

				
	##DeliverySrv			
	if DeliverySrv_EvtList.keys().count(cmdset.m_cmdname):
		callSrvCBFlag = False
		if cmdset.m_cmdname == 'DeliveryOrderEvent' :
			callSrvCBFlag = True 
		else:
			pass
		if callSrvCBFlag:		
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
global MessageRecvSrv_RemappingList; MessageRecvSrv_RemappingList = {}

class MessageRecvSrv_Init(smach.State):
	def __init__(self):
		smach.State.__init__(self, outcomes=['success','retry','failure'])
	
	def execute(self, userdata):
		time.sleep(0.1)
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
		
		while not rospy.is_shutdown():
			while len(self.m_cmdsetList) == 0 and not rospy.is_shutdown():
					time.sleep(0.01)		
					pass
			cmdset = self.m_cmdsetList.pop(0)

			if cmdset.m_cmdname == 'NewOrderEvent':
				MessageRecvSrv_cmdset = cmdset.copyCmdset()
				return 'call_order_event'

			elif cmdset.m_cmdname == 'StatusEvent':
				MessageRecvSrv_cmdset = cmdset.copyCmdset()
				return 'call_status_event'

		return 'failure'

		
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
		global MessageRecvSrv_RemappingList
		global kitchen_mgr_pub
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

		cmdset = MessageRecvSrv_cmdset.copyCmdset()
		
		cmdset.setInt("order_id",self.m_OrderID)
		goal_id = cmdset.getValue("goal_id")
		
		
		MessageRecvSrv_RemappingList[goal_id] = self.m_OrderID
		
		#send message delivery order queue
		cmdset.setCmdName("DeliveryOrderEvent")
		EventProc(cmdset)
		
		#send message to kitchen mgr
		o = Order()
		o.table_id = cmdset.getValue('table_id')
		
		#parsing menuse
		menus = []		
		strMenu = cmdset.getValue("menus")

		for k in strMenu.split('/'):
			if len(k) != 0:
				m = Menu()
				m.name = str(k.split('_')[0])
				m.size = int(k.split('_')[1])
				m.qty = int(k.split('_')[2])
				menus.append(m)
				
		o.menus = menus
		o.robot_name = "None"
		o.order_id = cmdset.getValue('order_id')
		
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
		global MessageRecvSrv_RemappingList
		global kitchen_mgr_pub
		global robot_status_list
		"""
		global MessageRecvSrv_GlobalEvtFlag	
		ResultCode = 'retry'

		if MessageRecvSrv_GlobalEvtFlag == True:			
			MessageRecvSrv_GlobalEvtFlag = False
			MessageRecvSrv = 'failure'
			return ResultCode
		"""
		##Receive Status
		
		cmdset = MessageRecvSrv_cmdset.copyCmdset()
		
		robot_name = cmdset.getValue("robot_name")
		goal_id  = cmdset.getValue("goal_id")
		status = cmdset.getValue("status")
		
		_tempstr = "Call Status Event ["+robot_name+"] ["+goal_id+"] ["+str(status)+"]"
		rospy.loginfo(_tempstr)
		
		#set robot status
		if  status == Status.IDLE:
			robot_status_list[robot_name] = "IDLE"	
		elif status == Status.GO_TO_KITCHEN:
			robot_status_list[robot_name] = "GO_TO_KITCHEN"	
		elif status == Status.ARRIVE_KITCHEN:
			robot_status_list[robot_name] = "ARRIVE_KITCHEN"		
		elif status == Status.WAITING_FOR_KITCHEN:
			robot_status_list[robot_name] = "WAITING_FOR_KITCHEN"	
		elif status == Status.IN_DELIVERY:
			robot_status_list[robot_name] = "IN_DELIVERY"
		elif status == Status.ARRIVE_TABLE:
			robot_status_list[robot_name] = "ARRIVE_TABLE"
		elif status == Status.WAITING_FOR_USER_CONFIRMATION:
			robot_status_list[robot_name] = "WAITING_FOR_USER_CONFIRMATION"
		elif status == Status.COMPLETE_DELIVERY:
			robot_status_list[robot_name] = "COMPLETE_DELIVERY"
		elif status == Status.RETURNING_TO_DOCK:
			robot_status_list[robot_name] = "RETURNING_TO_DOCK"
		elif status == Status.END_DELIVERY_ORDER:
			robot_status_list[robot_name] = "END_DELIVERY_ORDER"
		elif status == Status.ERROR:
			robot_status_list[robot_name] = "ERROR"
		else:
			robot_status_list[robot_name] = "ERROR"	
	
		
		if (status == Status.GO_TO_KITCHEN or 
			status == Status.ARRIVE_KITCHEN or 
			status == Status.WAITING_FOR_KITCHEN):
			
			#Send result to user device
			goal_handle = GetGoalHandle(goal_id)
			_feedback = UserOrderFeedback()
			_feedback.status = status
			goal_handle.publish_feedback(_feedback)
			
			
			#send data to kitchen mgr
				##get order id
			order_id = MessageRecvSrv_RemappingList[goal_id]
				##set order status as order id
			for k in MessageRecvSrv_OrderList:
				if k.order_id == order_id:
					k.status = status
					break
				#send order list
			order_list = OrderList()
			order_list.orders = MessageRecvSrv_OrderList
			kitchen_mgr_pub.publish(MessageRecvSrv_OrderList)
			
			pass
			
		elif status == Status.IN_DELIVERY:
			#Pop order list	
			order_id = MessageRecvSrv_RemappingList.pop(goal_id)
			for k in MessageRecvSrv_OrderList:
				if k.order_id == order_id:
					MessageRecvSrv_OrderList.remove(k)
					break
				#send order list	
			order_list = OrderList()
			order_list.orders = MessageRecvSrv_OrderList
			kitchen_mgr_pub.publish(MessageRecvSrv_OrderList)
			
			#Send result to user device
			goal_handle = GetGoalHandle(goal_id)
			_feedback = UserOrderFeedback()
			_feedback.status = status
			goal_handle.publish_feedback(_feedback)
			pass
			
		elif (status == Status.ARRIVE_TABLE or
			status == Status.WAITING_FOR_USER_CONFIRMATION or
			status == Status.COMPLETE_DELIVERY or
			status == Status.RETURNING_TO_DOCK or
			status == Status.END_DELIVERY_ORDER):	

			#Send result to user device
			goal_handle = GetGoalHandle(goal_id)
			_feedback = UserOrderFeedback()
			_feedback.status = status
			goal_handle.publish_feedback(_feedback)
				
			pass
			
		elif status == Status.IDLE:
			#Send result to user device
			goal_handle = GetGoalHandle(goal_id)
			_result = UserOrderResult()
			goal_handle.set_succeeded(_result)
						
			#Pop Goal Handle
			PopGoalHandleList(goal_id)
			
		else:
			pass
		
		
		return 'success'			
		
			
##DeliverySrv ############################################################
DeliverySrv_CBList = []
DeliverySrv_EvtList = {'DeliveryOrderEvent':'GlobalEvent'}

global DeliverySrv_GlobalEvtFlag; DeliverySrv_GlobalEvtFlag = False
global DeliverySrv_cmdset; DeliverySrv_cmdset = commandset.CCmdSet()
	
class DeliverySrv_Init(smach.State):
	def __init__(self):
		smach.State.__init__(self, outcomes=['success','retry','failure'])
	
	def execute(self, userdata):
		time.sleep(0.1)
		return 'success'

	
class DeliverySrv_Idle(smach.State):
	m_cmdsetList =[]
	
	def __init__(self):
		smach.State.__init__(self, outcomes = ['check_robot', 'retry','failure'])
		RegEventProc(self.__class__.__name__, self.listener)
		
	def listener(self,cmdset):
		
		if cmdset.m_cmdname == 'DeliveryOrderEvent':
			self.m_cmdsetList.append(cmdset) 	
		#_tempstr = "DeliverySrv Push order: ["+str(len(self.m_cmdsetList)) +"] ["+cmdset.getValue('goal_id')+"]"
		#rospy.loginfo(_tempstr)

		
	def execute(self, userdata):
		
		global DeliverySrv_cmdset
		while not rospy.is_shutdown() :
			while len(self.m_cmdsetList) == 0 and not rospy.is_shutdown():
					time.sleep(0.1)		
					pass
			cmdset = self.m_cmdsetList.pop(0)
			if cmdset.m_cmdname == 'DeliveryOrderEvent':
				DeliverySrv_cmdset = cmdset.copyCmdset()				
				return 'check_robot'
					
		return 'failure'
		
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
		global DeliverySrv_cmdset
		global robot_status_list
		
		"""
		global DeliverySrv_GlobalEvtFlag	
		ResultCode = 'retry'

		if DeliverySrv_GlobalEvtFlag == True:			
			DeliverySrv_GlobalEvtFlag = False
			DeliverySrv = 'failure'
			return ResultCode			
		"""
		
		#cmdset -> Order
		cmdset = DeliverySrv_cmdset.copyCmdset()
		goal_id = cmdset.getValue("goal_id")
	
		o = Order()
		o.table_id = cmdset.getValue('table_id')
		#parsing menus
		menus = []		
		strMenu = cmdset.getValue("menus")
		for k in strMenu.split('/'):
			if len(k) != 0:
				m = Menu()
				m.name = str(k.split('_')[0])
				m.size = int(k.split('_')[1])
				m.qty = int(k.split('_')[2])
				menus.append(m)
						
		o.menus = menus
		o.robot_name = "None"
		o.order_id = cmdset.getValue('order_id')

		#check robot
		checkRobotStatusFlag = True
		timeout = rospy.Duration(1)
		
		while checkRobotStatusFlag and not rospy.is_shutdown():
			
			for k in robot_status_list.keys():
				is_ready = robot_status_list[k] == "IDLE" and  waiter_client[k].wait_for_server(timeout)				
				if is_ready:
					robot_status_list[k] = "GO_TO_KITCHEN" 	
					o.status = Status.GO_TO_KITCHEN
					o.robot_name = k
					goal=UserOrderGoal(order=o)
					
					pActionClientCB = CActionClientCallBack(k,
															goal_id)
																					
					waiter_client[k].send_goal(goal,pActionClientCB.done_cb,
													pActionClientCB.active_cb, 
													pActionClientCB.feedback_cb)
									
					checkRobotStatusFlag = False				
					break;
				#else:
				#	_tempstr="robot action server is not connected or robot is in %s"%robot_status_list[k]
				#	rospy.logerr(_tempstr)
					
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
	user_device_action_server =  actionlib.ActionServer('send_order',UserOrderAction,GoalCB)
	####################################################
	
	####################################################
	global kitchen_mgr_pub
	kitchen_mgr_pub = rospy.Publisher('/list_order',OrderList,latch = True)
	####################################################
	
	####################################################
	#init
	global robot_num; robot_num = 1
	global waiter_client; waiter_client = {}
	global robot_status_list; robot_status_list = {}

	for k in range(robot_num):
			robot_cnt = k+1	
			robot_name = "waiter_%d"%robot_cnt
			robot_status_list[robot_name]="IDLE"
			
			_tempstr = "Create action client robot_name: " + robot_name
			rospy.loginfo(_tempstr)
			
			waiter_client[robot_name] = actionlib.SimpleActionClient(robot_name+"/delivery_order",
																	DeliverOrderAction)
			#waiter_client[robot_name].wait_for_server()															

	####################################################
			
	sm_top = smach.Concurrence(outcomes=['end'], default_outcome = 'end',  outcome_map = {'end':
												{'MessageRecvSrv':'end',
												'DeliverySrv':'end'
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
	
		with sm_DeliverySrv:
			smach.StateMachine.add('DeliverySrv_Init', DeliverySrv_Init(), 
														transitions={'success':'DeliverySrv_Idle', 
																	'failure':'end', 
																	'retry':'DeliverySrv_Init'})
			smach.StateMachine.add('DeliverySrv_CheckRobot', DeliverySrv_CheckRobot(), 
														transitions={'success':'DeliverySrv_Idle', 
																	'failure':'end', 
																	'retry':'DeliverySrv_CheckRobot'})		
			smach.StateMachine.add('DeliverySrv_Idle', DeliverySrv_Idle(), 
														transitions={'check_robot':'DeliverySrv_CheckRobot',
																	'failure':'end', 
																	'retry':'DeliverySrv_Init'})			
			
		
		smach.Concurrence.add('MessageRecvSrv', sm_MessageRecvSrv)
		smach.Concurrence.add('DeliverySrv', sm_DeliverySrv)				

	
	
	sis = smach_ros.IntrospectionServer('cafe_manager_viewer', sm_top, '/SM_ROOT')	
	sis.start()	
	outcome = sm_top.execute()
	rospy.spin()
	sis.stop()

	print "=========================Main end================================="

if __name__ == '__main__':
    main()





