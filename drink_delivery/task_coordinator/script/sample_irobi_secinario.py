#!/usr/bin/env python
# -*- coding:utf-8 -*-

import rospy
import smach
import smach_ros
import time

#client program
##############################################################################
import socket
import threading
import struct

NAME = "SampleApp"
HOST = "192.168.0.116"
PORT = 6001  
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))

global g_cmdID; g_cmdID = 0
g_ResCmdSetList = []

global g_EvtCmdSet
g_EvtCmdSetList = []


#############################################
class CCmdSet():
    global DISCRIMINATOR,VERSION
        
    DISCRIMINATOR = 0x9530ed04
    VERSION = 0x00020002
    
    from xml.dom.minidom import Document
    
    
    #member var
    #header
    m_cmdname=''
    m_msgtype=''
    m_senderID=''
    m_receiverID=''
    m_resrcID = 0
    m_usertag='' 
    m_status= 0
    m_timeout= 0
    m_contentID=''
    m_cmdID=0

    #body
    m_params = []
    
    #doc,riml,header,body,params
    doc = Document()

    # Create the <riml> base element
    riml = doc.createElement("riml")
    doc.appendChild(riml)

    # Create the main <header>, <body> <params>element
    header = doc.createElement("header")
    riml.appendChild(header)

    body = doc.createElement("body")
    riml.appendChild(body)

    params = doc.createElement("params")
    body.appendChild(params)

    def __init__(self,cmdname = "",msgtype="",senderID="",receiverID="", resrcID = 0,usertag="",status = 0,timeout = 0, contentID='',cmdID =0):
        from xml.dom.minidom import Document
        # Create the <riml> base element

        self.doc = Document()
    
        self.riml = self.doc.createElement("riml")
        self.doc.appendChild(self.riml)

        # Create the main <header>, <body> <params>element
        self.header = self.doc.createElement("header")
        self.riml.appendChild(self.header)

        self.body = self.doc.createElement("body")
        self.riml.appendChild(self.body)

        self.params = self.doc.createElement("params")
        self.body.appendChild(self.params)

        self.m_cmdname = cmdname
        self.m_msgtype = msgtype
        self.m_senderID = senderID
        self.m_receiverID = receiverID
        self.m_resrcID = resrcID
        self.m_usertag = usertag
        self.m_status = status
        self.m_timeout = timeout
        self.m_contentID = contentID
        self.m_cmdID = cmdID

        # Create the main <header> element
        verTag = self.doc.createElement("ver")
        cmdnameTag = self.doc.createElement("cmdname")
        msgtypeTag = self.doc.createElement("msgtype")
        senderIDTag = self.doc.createElement("senderID")
        receiverIDTag = self.doc.createElement("receiverID")
        resrcIDTag = self.doc.createElement("resrcID")
        usertagTag = self.doc.createElement("usertag")
        statusTag = self.doc.createElement("status")
        timeoutTag = self.doc.createElement("timeout")
        contentIDTag = self.doc.createElement("contentID")
        cmdIDTag = self.doc.createElement("cmdID")

        self.header.appendChild(verTag)
        self.header.appendChild(cmdnameTag)
        self.header.appendChild(msgtypeTag)
        self.header.appendChild(senderIDTag)
        self.header.appendChild(receiverIDTag)
        self.header.appendChild(resrcIDTag)
        self.header.appendChild(usertagTag)
        self.header.appendChild(statusTag)
        self.header.appendChild(timeoutTag)
        self.header.appendChild(contentIDTag)
        self.header.appendChild(cmdIDTag)

        ptext = self.doc.createTextNode("1.11.0000")
        verTag.appendChild(ptext)

        ptext = self.doc.createTextNode(self.m_cmdname)
        cmdnameTag.appendChild(ptext)
                
        ptext = self.doc.createTextNode(self.m_msgtype)
        msgtypeTag.appendChild(ptext)

        ptext = self.doc.createTextNode(self.m_senderID)
        senderIDTag.appendChild(ptext)

        ptext = self.doc.createTextNode(self.m_receiverID)
        receiverIDTag.appendChild(ptext)

        ptext = self.doc.createTextNode(str(self.m_resrcID))
        resrcIDTag.appendChild(ptext)

        ptext = self.doc.createTextNode(str(self.m_usertag))
        usertagTag.appendChild(ptext)

        ptext = self.doc.createTextNode(str(self.m_status))
        statusTag.appendChild(ptext)

        ptext = self.doc.createTextNode(str(self.m_timeout))
        timeoutTag.appendChild(ptext)

        ptext = self.doc.createTextNode(str(self.m_contentID))
        contentIDTag.appendChild(ptext)

        ptext = self.doc.createTextNode(str(self.m_cmdID))
        cmdIDTag.appendChild(ptext)


    def __del__(self):
        #print  "Delete CmdSet Class"
        pass

    def setInt(self,Name,Value):
       
        paramTag = self.doc.createElement("param")
        self.params.appendChild(paramTag)

        nameTag = self.doc.createElement("name")
        paramTag.appendChild(nameTag)
        ptext = self.doc.createTextNode(str(Name))
        nameTag.appendChild(ptext)

        typeTag = self.doc.createElement("type")
        paramTag.appendChild(typeTag)
        ptext = self.doc.createTextNode("int")
        typeTag.appendChild(ptext)

        valueTag = self.doc.createElement("value")
        paramTag.appendChild(valueTag)
        ptext = self.doc.createTextNode(str(Value))
        valueTag.appendChild(ptext)

    def setBool(self,Name,Value):
        paramTag = self.doc.createElement("param")
        self.params.appendChild(paramTag)

        nameTag = self.doc.createElement("name")
        paramTag.appendChild(nameTag)
        ptext = self.doc.createTextNode(str(Name))
        nameTag.appendChild(ptext)

        typeTag = self.doc.createElement("type")
        paramTag.appendChild(typeTag)
        ptext = self.doc.createTextNode("bool")
        typeTag.appendChild(ptext)

        valueTag = self.doc.createElement("value")
        paramTag.appendChild(valueTag)
        ptext = self.doc.createTextNode(str(Value))
        valueTag.appendChild(ptext)
        
    def setString(self,Name,Value):
        paramTag = self.doc.createElement("param")
        self.params.appendChild(paramTag)

        nameTag = self.doc.createElement("name")
        paramTag.appendChild(nameTag)
        ptext = self.doc.createTextNode(str(Name))
        nameTag.appendChild(ptext)

        typeTag = self.doc.createElement("type")
        paramTag.appendChild(typeTag)
        ptext = self.doc.createTextNode("string")
        typeTag.appendChild(ptext)

        valueTag = self.doc.createElement("value")
        paramTag.appendChild(valueTag)
        ptext = self.doc.createTextNode(str(Value))
        valueTag.appendChild(ptext)

    def setUInt(self,Name,Value):
        paramTag = self.doc.createElement("param")
        self.params.appendChild(paramTag)

        nameTag = self.doc.createElement("name")
        paramTag.appendChild(nameTag)
        ptext = self.doc.createTextNode(str(Name))
        nameTag.appendChild(ptext)

        typeTag = self.doc.createElement("type")
        paramTag.appendChild(typeTag)
        ptext = self.doc.createTextNode("unsigned int")
        typeTag.appendChild(ptext)

        valueTag = self.doc.createElement("value")
        paramTag.appendChild(valueTag)
        ptext = self.doc.createTextNode(str(Value))
        valueTag.appendChild(ptext)

    def setFloat(self,Name,Value):
        paramTag = self.doc.createElement("param")
        self.params.appendChild(paramTag)

        nameTag = self.doc.createElement("name")
        paramTag.appendChild(nameTag)
        ptext = self.doc.createTextNode(str(Name))
        nameTag.appendChild(ptext)

        typeTag = self.doc.createElement("type")
        paramTag.appendChild(typeTag)
        ptext = self.doc.createTextNode("float")
        typeTag.appendChild(ptext)

        valueTag = self.doc.createElement("value")
        paramTag.appendChild(valueTag)
        ptext = self.doc.createTextNode(str(Value))
        valueTag.appendChild(ptext)

    def printCmdSet(self):
        print self.doc.toprettyxml(indent="  ",encoding="euc-kr")

    def getCmdSet(self):
        #print self.doc.toprettyxml(indent="  ",encoding="euc-kr")
        DataLength = len(self.doc.toxml(encoding="euc-kr"))
        buffer = struct.pack('I I I %ds'%DataLength, DISCRIMINATOR, VERSION, DataLength,self.doc.toxml())
        return buffer

    def parse(self,data):
        from xml.dom.minidom import parseString
        global doc
        s = unicode(data,'euc-kr').encode('utf-8')  # euc-kr -> utf-8 
        s = s.replace("encoding=\"euc-kr\"", r"")
        doc = parseString(s)

        headerTag = doc.getElementsByTagName('header')[0]
        if headerTag.childNodes.length == 11:

            i=0
            while i < headerTag.childNodes.length:
  
                NodeName = headerTag.childNodes[i].nodeName
                if headerTag.childNodes[i].firstChild != None:
                        NodeValue = headerTag.childNodes[i].firstChild.nodeValue
                else:
                        NodeValue = 'None'

                if NodeName == "ver":
                        ver = NodeValue
                elif NodeName == "cmdname":
                        self.m_cmdname = NodeValue
                elif NodeName == "msgtype":
                        self.m_msgtype = NodeValue 
                elif NodeName == "senderID":
                        self.m_senderID = NodeValue
                elif NodeName == "receiverID":
                        self.m_receiverID = NodeValue
                elif NodeName == "usertag":
                       self.m_usertag = (NodeValue )
                elif NodeName == "status":
                        self.m_status = (NodeValue )
                elif NodeName == "timeout":
                        self.m_timeout = (NodeValue )
                elif NodeName == "contentID":
                        self.m_contentID = NodeValue
		elif NodeName == "cmdID":
                        self.m_cmdID = (NodeValue )
                else:
                        pass
                i+=1

        bodyTag = doc.getElementsByTagName('body')[0]

        if bodyTag.childNodes.length > 0:
            paramList = bodyTag.getElementsByTagName('param')
            i=0
            if paramList.length > 0:
                    i=0
                    while i < paramList.length:
                        nameTag = paramList[i].getElementsByTagName('name')
                        typeTag = paramList[i].getElementsByTagName('type')
                        valueTag = paramList[i].getElementsByTagName('value')


			#if headerTag.childNodes[i].firstChild != None:
	                  #      NodeValue = headerTag.childNodes[i].firstChild.nodeValue
	                #else:
	                  #      NodeValue = 'None'

			param = {}
			param['name'] = nameTag[0].firstChild.nodeValue
			param['type'] = typeTag[0].firstChild.nodeValue
			
			if valueTag[0].firstChild != None:
				if  typeTag[0].firstChild.nodeValue == 'int':
					param['value'] =  int(valueTag[0].firstChild.nodeValue)
				elif  typeTag[0].firstChild.nodeValue == 'bool':
					param['value'] = bool(valueTag[0].firstChild.nodeValue)
				elif  typeTag[0].firstChild.nodeValue == 'string':
					param['value'] =  str(valueTag[0].firstChild.nodeValue.encode('utf-8'))
				elif  typeTag[0].firstChild.nodeValue == 'float':
					param['value'] =  float(valueTag[0].firstChild.nodeValue)
				elif  typeTag[0].firstChild.nodeValue == 'unsigned int':
					param['value'] =  int(valueTag[0].firstChild.nodeValue)
				else:
					param['value'] =  valueTag[0].firstChild.nodeValue
			else:
				param['value'] = None

			self.m_params.append(param)
                        i+=1

    def getValue(self,name):
	Value = None
	for i in self.m_params:
		if i['name'] == name:
        		Value = i['value']
        return Value

    def getType(self,name):
	Type = None
	for i in self.m_params:
		if i['name'] == name:
        		Type = i['type']
        return Type

    def getArgList(self):
        ArgList = []
	for i in self.m_params:
		ArgList.append(i['name'])
	return ArgList

        

def Connect():
	print "Call Rapix Connect function"
	global g_cmdID	
	g_cmdID +=1
	cmdset = CCmdSet("WhoIam","REQUEST_MESSAGE",NAME,"RVM",0," ",0,0," ",g_cmdID)	
	s.send(cmdset.getCmdSet())

def Recv():
	print "Start Recv Thread"
	
	global ThreadRecvFlag; ThreadRecvFlag= True
        while ThreadRecvFlag:   
		try:     
			data = s.recv(12)
			if len(data) != 12:
				data += s.recv(12-len(data))
		except Exception:
			print "Exception!!!!!!!!!!!!!!!!!!!!!data = s.recv(12)"
			continue

		try:
			buffer = struct.unpack('I I I',data)
		except Exception:
			print "Exception!!!!!!!!!!!!!!!!!!!!!buffer = struct.unpack('I I I',data)"
			continue

 	
		nDisc = buffer[0]
		nVer = buffer[1]
		nDataLen = buffer[2]

		#print "nDisc: ", nDisc, " nVer: ", nVer ," nDataLen: ", nDataLen

		if nDisc != 2503011588 or nVer != 131075 or nDataLen == 0: 
			continue
		
		try:
			data = s.recv(nDataLen)
			if len(data) != nDataLen:
				print 'More Receive Data'
				data += s.recv(nDataLen-len(data))
		except Exception:
			print "Exception!!!!!!!!!!!!!!!!!!!!!data = s.recv(nDataLen)"
			continue
		try:
			buffer = struct.unpack('%ds'%nDataLen,data)
		except Exception:
			print "Exception!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!buffer = struct.unpack('%ds'%nDataLen,data)"
			continue
		
		nData = buffer[0]
		cmdset = CCmdSet()
		cmdset.parse(nData)

		print "MSGT: [", cmdset.m_msgtype, " ] Name: [",cmdset.m_cmdname,"] REC: [",cmdset.m_receiverID,"] SEND: [",cmdset.m_senderID,"] CMD: [",cmdset.m_cmdID,"]"

		if cmdset.m_msgtype == "RESPONSE_MESSAGE":
			g_ResCmdSetList.append(cmdset)
			
		elif cmdset.m_msgtype == "EVENT_MESSAGE":
			EventProc(cmdset)
			
	    	#print "Data: ", nData
		
	s.close()
	print "Stop Recv Thread"

def EventProc(cmdset):
	##reg service######################################################
	##RemoteSrv
	if RemoteSrv_EvtList.keys().count(cmdset.m_cmdname):	

		callSrvCVFlag = False		
		if cmdset.m_cmdname ==  'RemoteControllerButtonEvent' and cmdset.getValue('ButtonID') == 11 and cmdset.getValue('Status') == 1: 
			callSrvCVFlag = True		
		elif cmdset.m_cmdname ==  'RemoteControllerButtonEvent' and cmdset.getValue('ButtonID') == 12 and cmdset.getValue('Status') == 1: 
			callSrvCVFlag = True		
		elif cmdset.m_cmdname ==  'RemoteControllerButtonEvent' and cmdset.getValue('ButtonID') == 13 and cmdset.getValue('Status') == 1: 
			callSrvCVFlag = True		
		elif cmdset.m_cmdname ==  'RemoteControllerButtonEvent' and cmdset.getValue('ButtonID') == 14 and cmdset.getValue('Status') == 1:
			callSrvCVFlag = True	
		elif cmdset.m_cmdname ==  'RemoteControllerButtonEvent' and cmdset.getValue('ButtonID') == 11 and cmdset.getValue('Status') == 0:
			callSrvCVFlag = True	
		elif cmdset.m_cmdname ==  'RemoteControllerButtonEvent' and cmdset.getValue('ButtonID') == 12 and cmdset.getValue('Status') == 0: 
			callSrvCVFlag = True		
		elif cmdset.m_cmdname ==  'RemoteControllerButtonEvent' and cmdset.getValue('ButtonID') == 13 and cmdset.getValue('Status') == 0: 
			callSrvCVFlag = True		
		elif cmdset.m_cmdname ==  'RemoteControllerButtonEvent' and cmdset.getValue('ButtonID') == 14 and cmdset.getValue('Status') == 0:
			callSrvCVFlag = True		

		if callSrvCVFlag:		
			print cmdset.m_cmdname, len(RemoteSrv_CBList)
			for i in range(len(RemoteSrv_CBList)):
				RemoteSrv_CBList[i](cmdset)
	##reg service######################################################
	##VideoChatSrv
	
	elif VideoChatSrv_EvtList.keys().count(cmdset.m_cmdname):	
		callSrvCVFlag = False
		if cmdset.m_cmdname ==  'ServiceStatusEvent' and cmdset.getValue('ServiceName') == "VideoChat" and cmdset.getValue('Status') == 1: 
			callSrvCVFlag = True				
		elif cmdset.m_cmdname ==  'ServiceStatusEvent' and cmdset.getValue('ServiceName') == "VideoChat" and cmdset.getValue('Status') == 0: 
			callSrvCVFlag = True
		elif cmdset.m_cmdname ==  'StartRecObject': 
			callSrvCVFlag = True
		else: 
			callSrvCVFlag = False
		
		#Call Reg event function
		if callSrvCVFlag:		
			print cmdset.m_cmdname, len(VideoChatSrv_CBList)
			for i in range(len(VideoChatSrv_CBList)):
				VideoChatSrv_CBList[i](cmdset)
	##reg service######################################################
	##TouchSrv
	
	elif TouchSrv_EvtList.keys().count(cmdset.m_cmdname):	
		callSrvCVFlag = False
		if cmdset.m_cmdname ==  'TouchSensorEvent' and cmdset.getValue('ButtonID') == 0 and cmdset.getValue('Status') == 1: 
			callSrvCVFlag = True
		elif cmdset.m_cmdname ==  'TouchSensorEvent' and cmdset.getValue('ButtonID') == 1 and cmdset.getValue('Status') == 1 :
			callSrvCVFlag = True
		elif cmdset.m_cmdname ==  'TouchSensorEvent' and cmdset.getValue('ButtonID') == 2 and cmdset.getValue('Status') == 1:
			callSrvCVFlag = True
		elif cmdset.m_cmdname ==  'TouchSensorEvent' and cmdset.getValue('ButtonID') == 3 and cmdset.getValue('Status') == 1:
			callSrvCVFlag = True
		elif cmdset.m_cmdname ==  'TouchSensorEvent' and cmdset.getValue('ButtonID') == 4 and cmdset.getValue('Status') == 1 :
			callSrvCVFlag = True
		elif cmdset.m_cmdname ==  'TouchSensorEvent' and cmdset.getValue('ButtonID') == 5 and cmdset.getValue('Status') ==1:
			callSrvCVFlag = True
		
		#Call Reg event function
		if callSrvCVFlag:		
			print cmdset.m_cmdname, len(TouchSrv_CBList)
			for i in range(len(TouchSrv_CBList)):
				TouchSrv_CBList[i](cmdset)
	
	#pass
	else:	
		pass

def RegEventProc(SrvName, cb):

	if SrvName.count('RemoteSrv'): 
		RemoteSrv_CBList.append(cb)
	elif  SrvName.count('VideoChatSrv'):    
		VideoChatSrv_CBList.append(cb)
	elif  SrvName.count('TouchSrv'):    
		TouchSrv_CBList.append(cb)
	else:
		pass

##############################################################################
#######################################################################################################
##Define State
#######################################################################################################     



##RemoteSrv ############################################################
RemoteSrv_EvtList = {}
RemoteSrv_CBList = []

RemoteSrv_EvtList = {'RemoteControllerButtonEvent':'GlobalEvent'}
RemoteSrv_GlobalEvtFlag = False

class RemoteSrv_Init(smach.State):
	def __init__(self):
		smach.State.__init__(self, outcomes=['success','retry','failure'])
		RegEventProc(self.__class__.__name__, self.listener)
	
	def listener(self,cmdset):
		
		#print ' RemoteSrv_Init'
		pass

	def execute(self, userdata):
		time.sleep(1)
		return 'success'

class RemoteSrv_Idle(smach.State):
	
	m_cmdsetList =[]
	
	def __init__(self):
		smach.State.__init__(self, outcomes = ['forward','backward','rightturn','leftturn', 'stop','retry','failure'])
		RegEventProc(self.__class__.__name__, self.listener)
	
	def listener(self,cmdset):		
		global RemoteSrv_GlobalEvtFlag
		if RemoteSrv_EvtList.keys().count(cmdset.m_cmdname) and RemoteSrv_EvtList[cmdset.m_cmdname] == "GlobalEvent" :				
			#here 			
			if cmdset.m_cmdname ==  'RemoteControllerButtonEvent' and cmdset.getValue('ButtonID') == 11 and cmdset.getValue('Status') == 1: 
				self.m_cmdsetList.append(cmdset)
			elif cmdset.m_cmdname ==  'RemoteControllerButtonEvent' and cmdset.getValue('ButtonID') == 12 and cmdset.getValue('Status') == 1 :
				self.m_cmdsetList.append(cmdset)
			elif cmdset.m_cmdname ==  'RemoteControllerButtonEvent' and cmdset.getValue('ButtonID') == 13 and cmdset.getValue('Status') == 1:
				self.m_cmdsetList.append(cmdset)
			elif cmdset.m_cmdname ==  'RemoteControllerButtonEvent' and cmdset.getValue('ButtonID') == 14 and cmdset.getValue('Status') == 1:
				self.m_cmdsetList.append(cmdset)
			elif cmdset.m_cmdname ==  'RemoteControllerButtonEvent' and cmdset.getValue('ButtonID') == 11 and cmdset.getValue('Status') == 0 :
				self.m_cmdsetList.append(cmdset)
			elif cmdset.m_cmdname ==  'RemoteControllerButtonEvent' and cmdset.getValue('ButtonID') == 12 and cmdset.getValue('Status') ==0:
				self.m_cmdsetList.append(cmdset)
			elif cmdset.m_cmdname ==  'RemoteControllerButtonEvent' and cmdset.getValue('ButtonID') == 13 and cmdset.getValue('Status') == 0:
				self.m_cmdsetList.append(cmdset)
			elif cmdset.m_cmdname ==  'RemoteControllerButtonEvent' and cmdset.getValue('ButtonID') == 14 and cmdset.getValue('Status') == 0:
				self.m_cmdsetList.append(cmdset)
		pass

	def execute(self, userdata):
		global RemoteSrv_GlobalEvtFlag
		while True:		
			
			while len(self.m_cmdsetList) == 0:
				time.sleep(0.001)		
				pass
			cmdset = self.m_cmdsetList.pop(0)
	
				


			if cmdset.m_cmdname ==  'RemoteControllerButtonEvent' and cmdset.getValue('ButtonID') == 11 and cmdset.getValue('Status') == 1: 
					RemoteSrv_GlobalEvtFlag = False
					return 'forward'
			
			elif cmdset.m_cmdname ==  'RemoteControllerButtonEvent' and cmdset.getValue('ButtonID') == 12 and cmdset.getValue('Status') == 1: 
					RemoteSrv_GlobalEvtFlag = False
					return 'backward'		

			elif cmdset.m_cmdname ==  'RemoteControllerButtonEvent' and cmdset.getValue('ButtonID') == 13 and cmdset.getValue('Status') == 1: 
					RemoteSrv_GlobalEvtFlag = False
					return 'leftturn'

			elif cmdset.m_cmdname ==  'RemoteControllerButtonEvent' and cmdset.getValue('ButtonID') == 14 and cmdset.getValue('Status') == 1: 
					RemoteSrv_GlobalEvtFlag = False
					return 'rightturn'

			elif cmdset.m_cmdname ==  'RemoteControllerButtonEvent' and cmdset.getValue('ButtonID') == 11 and cmdset.getValue('Status') == 0: 
					RemoteSrv_GlobalEvtFlag = False
					return 'stop'

			elif cmdset.m_cmdname ==  'RemoteControllerButtonEvent' and cmdset.getValue('ButtonID') == 12 and cmdset.getValue('Status') == 0: 
					RemoteSrv_GlobalEvtFlag = False
					return 'stop'

			elif cmdset.m_cmdname ==  'RemoteControllerButtonEvent' and cmdset.getValue('ButtonID') == 13 and cmdset.getValue('Status') == 0: 
					RemoteSrv_GlobalEvtFlag = False
					return 'stop'

			elif cmdset.m_cmdname ==  'RemoteControllerButtonEvent' and cmdset.getValue('ButtonID') == 14 and cmdset.getValue('Status') == 0: 
					RemoteSrv_GlobalEvtFlag = False
					return 'stop'
		
			time.sleep(0.001)


class RemoteSrv_Forward(smach.State):

	m_IsRunning = [True]

	def __init__(self):
		smach.State.__init__(self, outcomes = ['success','retry','failure'])
		RegEventProc(self.__class__.__name__, self.listener)
	
	def listener(self,cmdset):
		global RemoteSrv_GlobalEvtFlag
		
		if RemoteSrv_EvtList.keys().count(cmdset.m_cmdname) and RemoteSrv_EvtList[cmdset.m_cmdname] == "GlobalEvent" :
			if cmdset.m_cmdname ==  'RemoteControllerButtonEvent' and cmdset.getValue('ButtonID') == 11 and cmdset.getValue('Status') == 1: 
				RemoteSrv_GlobalEvtFlag = True
			elif cmdset.m_cmdname ==  'RemoteControllerButtonEvent' and cmdset.getValue('ButtonID') == 12 and cmdset.getValue('Status') == 1: 
				RemoteSrv_GlobalEvtFlag = True
			elif cmdset.m_cmdname ==  'RemoteControllerButtonEvent' and cmdset.getValue('ButtonID') == 13 and cmdset.getValue('Status') == 1: 
				RemoteSrv_GlobalEvtFlag = True
			elif cmdset.m_cmdname ==  'RemoteControllerButtonEvent' and cmdset.getValue('ButtonID') == 14 and cmdset.getValue('Status') == 1: 
				RemoteSrv_GlobalEvtFlag = True
			elif cmdset.m_cmdname ==  'RemoteControllerButtonEvent' and cmdset.getValue('ButtonID') == 11 and cmdset.getValue('Status') == 0: 
				RemoteSrv_GlobalEvtFlag = True
			elif cmdset.m_cmdname ==  'RemoteControllerButtonEvent' and cmdset.getValue('ButtonID') == 12 and cmdset.getValue('Status') == 0: 
				RemoteSrv_GlobalEvtFlag = True
			elif cmdset.m_cmdname ==  'RemoteControllerButtonEvent' and cmdset.getValue('ButtonID') == 13 and cmdset.getValue('Status') == 0: 
				RemoteSrv_GlobalEvtFlag = True
			elif cmdset.m_cmdname ==  'RemoteControllerButtonEvent' and cmdset.getValue('ButtonID') == 14 and cmdset.getValue('Status') == 0: 
				RemoteSrv_GlobalEvtFlag = True
		pass


	def execute(self, userdata):
		global RemoteSrv_GlobalEvtFlag
		ResultCode = 'retry'
		if RemoteSrv_GlobalEvtFlag == True:			
			RemoteSrv_GlobalEvtFlag = False
			ResultCode = 'failure'
			return ResultCode

		self.m_IsRunning =[True]
		Ret = {}
		Thread_GotoDirEx = threading.Thread(target=GotoDirEx, args=(self.m_IsRunning,Ret, 1, 65535, True))
		Thread_GotoDirEx.start()		
		while self.m_IsRunning[0] == True:
			if RemoteSrv_GlobalEvtFlag == True:				
				RemoteSrv_GlobalEvtFlag = False
				ResultCode =  'failure'
				return ResultCode
			pass		
		while Thread_GotoDirEx.isAlive():
			pass
	
		if Ret['ResultCode'] == 0:
			ResultCode = 'success'
		else:
			ResultCode = 'failure'


		return ResultCode

class RemoteSrv_Backward(smach.State):
	m_IsRunning = [True]
		
	def __init__(self):
		smach.State.__init__(self, outcomes = ['success','retry','failure'])
		RegEventProc(self.__class__.__name__, self.listener)
	
	def listener(self,cmdset):
		global RemoteSrv_GlobalEvtFlag	
		if RemoteSrv_EvtList.keys().count(cmdset.m_cmdname) and RemoteSrv_EvtList[cmdset.m_cmdname] == "GlobalEvent" :
			if cmdset.m_cmdname ==  'RemoteControllerButtonEvent' and cmdset.getValue('ButtonID') == 11 and cmdset.getValue('Status') == 1: 
				RemoteSrv_GlobalEvtFlag = True
			elif cmdset.m_cmdname ==  'RemoteControllerButtonEvent' and cmdset.getValue('ButtonID') == 12 and cmdset.getValue('Status') == 1: 
				RemoteSrv_GlobalEvtFlag = True
			elif cmdset.m_cmdname ==  'RemoteControllerButtonEvent' and cmdset.getValue('ButtonID') == 13 and cmdset.getValue('Status') == 1: 
				RemoteSrv_GlobalEvtFlag = True
			elif cmdset.m_cmdname ==  'RemoteControllerButtonEvent' and cmdset.getValue('ButtonID') == 14 and cmdset.getValue('Status') == 1: 
				RemoteSrv_GlobalEvtFlag = True
			elif cmdset.m_cmdname ==  'RemoteControllerButtonEvent' and cmdset.getValue('ButtonID') == 11 and cmdset.getValue('Status') == 0: 
				RemoteSrv_GlobalEvtFlag = True
			elif cmdset.m_cmdname ==  'RemoteControllerButtonEvent' and cmdset.getValue('ButtonID') == 12 and cmdset.getValue('Status') == 0: 
				RemoteSrv_GlobalEvtFlag = True
			elif cmdset.m_cmdname ==  'RemoteControllerButtonEvent' and cmdset.getValue('ButtonID') == 13 and cmdset.getValue('Status') == 0: 
				RemoteSrv_GlobalEvtFlag = True
			elif cmdset.m_cmdname ==  'RemoteControllerButtonEvent' and cmdset.getValue('ButtonID') == 14 and cmdset.getValue('Status') == 0: 
				RemoteSrv_GlobalEvtFlag = True
		pass


	def execute(self, userdata):
		global RemoteSrv_GlobalEvtFlag
		ResultCode = 'retry'
		if RemoteSrv_GlobalEvtFlag == True:			
			RemoteSrv_GlobalEvtFlag = False
			ResultCode = 'failure'
			return ResultCode

		self.m_IsRunning =[True]
		Ret = {}
		Thread_GotoDirEx = threading.Thread(target=GotoDirEx, args=(self.m_IsRunning,Ret, 2, 65535, True))
		Thread_GotoDirEx.start()		
		while self.m_IsRunning[0] == True:
			if RemoteSrv_GlobalEvtFlag == True:				
				RemoteSrv_GlobalEvtFlag = False
				ResultCode =  'failure'
				return ResultCode
			pass		
		while Thread_GotoDirEx.isAlive():
			pass
	
		if Ret['ResultCode'] == 0:
			ResultCode = 'success'
		else:
			ResultCode = 'failure'

		return ResultCode

class RemoteSrv_Leftturn(smach.State):
	m_IsRunning = [True]
		
	def __init__(self):
		smach.State.__init__(self, outcomes = ['success','retry','failure'])
		RegEventProc(self.__class__.__name__, self.listener)
	
	def listener(self,cmdset):
		global RemoteSrv_GlobalEvtFlag	
		if RemoteSrv_EvtList.keys().count(cmdset.m_cmdname) and RemoteSrv_EvtList[cmdset.m_cmdname] == "GlobalEvent" :
			if cmdset.m_cmdname ==  'RemoteControllerButtonEvent' and cmdset.getValue('ButtonID') == 11 and cmdset.getValue('Status') == 1: 
				RemoteSrv_GlobalEvtFlag = True
			elif cmdset.m_cmdname ==  'RemoteControllerButtonEvent' and cmdset.getValue('ButtonID') == 12 and cmdset.getValue('Status') == 1: 
				RemoteSrv_GlobalEvtFlag = True
			elif cmdset.m_cmdname ==  'RemoteControllerButtonEvent' and cmdset.getValue('ButtonID') == 13 and cmdset.getValue('Status') == 1: 
				RemoteSrv_GlobalEvtFlag = True
			elif cmdset.m_cmdname ==  'RemoteControllerButtonEvent' and cmdset.getValue('ButtonID') == 14 and cmdset.getValue('Status') == 1: 
				RemoteSrv_GlobalEvtFlag = True
			elif cmdset.m_cmdname ==  'RemoteControllerButtonEvent' and cmdset.getValue('ButtonID') == 11 and cmdset.getValue('Status') == 0: 
				RemoteSrv_GlobalEvtFlag = True
			elif cmdset.m_cmdname ==  'RemoteControllerButtonEvent' and cmdset.getValue('ButtonID') == 12 and cmdset.getValue('Status') == 0: 
				RemoteSrv_GlobalEvtFlag = True
			elif cmdset.m_cmdname ==  'RemoteControllerButtonEvent' and cmdset.getValue('ButtonID') == 13 and cmdset.getValue('Status') == 0: 
				RemoteSrv_GlobalEvtFlag = True
			elif cmdset.m_cmdname ==  'RemoteControllerButtonEvent' and cmdset.getValue('ButtonID') == 14 and cmdset.getValue('Status') == 0: 
				RemoteSrv_GlobalEvtFlag = True
		pass


	def execute(self, userdata):
		global RemoteSrv_GlobalEvtFlag
		ResultCode = 'retry'
		if RemoteSrv_GlobalEvtFlag == True:			
			RemoteSrv_GlobalEvtFlag = False
			ResultCode = 'failure'
			return ResultCode

		self.m_IsRunning =[True]
		Ret = {}
		Thread_GotoDirEx = threading.Thread(target=GotoDirEx, args=(self.m_IsRunning,Ret, 3, 65535, True))
		Thread_GotoDirEx.start()		
		while self.m_IsRunning[0] == True:
			if RemoteSrv_GlobalEvtFlag == True:				
				RemoteSrv_GlobalEvtFlag = False
				ResultCode =  'failure'
				return ResultCode
			pass		
		while Thread_GotoDirEx.isAlive():
			pass
	
		if Ret['ResultCode'] == 0:
			ResultCode = 'success'
		else:
			ResultCode = 'failure'

		return ResultCode

class RemoteSrv_Rightturn(smach.State):
	m_IsRunning = [True]
		
	def __init__(self):
		smach.State.__init__(self, outcomes = ['success','retry','failure'])
		RegEventProc(self.__class__.__name__, self.listener)
	
	def listener(self,cmdset):
		global RemoteSrv_GlobalEvtFlag	
		if RemoteSrv_EvtList.keys().count(cmdset.m_cmdname) and RemoteSrv_EvtList[cmdset.m_cmdname] == "GlobalEvent" :
			if cmdset.m_cmdname ==  'RemoteControllerButtonEvent' and cmdset.getValue('ButtonID') == 11 and cmdset.getValue('Status') == 1: 
				RemoteSrv_GlobalEvtFlag = True
			elif cmdset.m_cmdname ==  'RemoteControllerButtonEvent' and cmdset.getValue('ButtonID') == 12 and cmdset.getValue('Status') == 1: 
				RemoteSrv_GlobalEvtFlag = True
			elif cmdset.m_cmdname ==  'RemoteControllerButtonEvent' and cmdset.getValue('ButtonID') == 13 and cmdset.getValue('Status') == 1: 
				RemoteSrv_GlobalEvtFlag = True
			elif cmdset.m_cmdname ==  'RemoteControllerButtonEvent' and cmdset.getValue('ButtonID') == 14 and cmdset.getValue('Status') == 1: 
				RemoteSrv_GlobalEvtFlag = True
			elif cmdset.m_cmdname ==  'RemoteControllerButtonEvent' and cmdset.getValue('ButtonID') == 11 and cmdset.getValue('Status') == 0: 
				RemoteSrv_GlobalEvtFlag = True
			elif cmdset.m_cmdname ==  'RemoteControllerButtonEvent' and cmdset.getValue('ButtonID') == 12 and cmdset.getValue('Status') == 0: 
				RemoteSrv_GlobalEvtFlag = True
			elif cmdset.m_cmdname ==  'RemoteControllerButtonEvent' and cmdset.getValue('ButtonID') == 13 and cmdset.getValue('Status') == 0: 
				RemoteSrv_GlobalEvtFlag = True
			elif cmdset.m_cmdname ==  'RemoteControllerButtonEvent' and cmdset.getValue('ButtonID') == 14 and cmdset.getValue('Status') == 0: 
				RemoteSrv_GlobalEvtFlag = True
		pass


	def execute(self, userdata):
		global RemoteSrv_GlobalEvtFlag
		ResultCode = 'retry'
		if RemoteSrv_GlobalEvtFlag == True:			
			RemoteSrv_GlobalEvtFlag = False
			ResultCode = 'failure'
			return ResultCode

		self.m_IsRunning =[True]
		Ret = {}
		Thread_GotoDirEx = threading.Thread(target=GotoDirEx, args=(self.m_IsRunning,Ret, 4, 65535, True))
		Thread_GotoDirEx.start()		
		while self.m_IsRunning[0] == True:
			if RemoteSrv_GlobalEvtFlag == True:				
				RemoteSrv_GlobalEvtFlag = False
				ResultCode =  'failure'
				return ResultCode
			pass		
		while Thread_GotoDirEx.isAlive():
			pass

		if Ret['ResultCode'] == 0:
			ResultCode = 'success'
		else:
			ResultCode = 'failure'

		return ResultCode

class RemoteSrv_Stop(smach.State):
	m_IsRunning = [True]
		
	def __init__(self):
		smach.State.__init__(self, outcomes = ['success','retry','failure'])
		RegEventProc(self.__class__.__name__, self.listener)
	
	def listener(self,cmdset):
		global RemoteSrv_GlobalEvtFlag	
		if RemoteSrv_EvtList.keys().count(cmdset.m_cmdname) and RemoteSrv_EvtList[cmdset.m_cmdname] == "GlobalEvent" :
			if cmdset.m_cmdname ==  'RemoteControllerButtonEvent' and cmdset.getValue('ButtonID') == 11 and cmdset.getValue('Status') == 1: 
				RemoteSrv_GlobalEvtFlag = True
			elif cmdset.m_cmdname ==  'RemoteControllerButtonEvent' and cmdset.getValue('ButtonID') == 12 and cmdset.getValue('Status') == 1: 
				RemoteSrv_GlobalEvtFlag = True
			elif cmdset.m_cmdname ==  'RemoteControllerButtonEvent' and cmdset.getValue('ButtonID') == 13 and cmdset.getValue('Status') == 1: 
				RemoteSrv_GlobalEvtFlag = True
			elif cmdset.m_cmdname ==  'RemoteControllerButtonEvent' and cmdset.getValue('ButtonID') == 14 and cmdset.getValue('Status') == 1: 
				RemoteSrv_GlobalEvtFlag = True
			elif cmdset.m_cmdname ==  'RemoteControllerButtonEvent' and cmdset.getValue('ButtonID') == 11 and cmdset.getValue('Status') == 0: 
				RemoteSrv_GlobalEvtFlag = True
			elif cmdset.m_cmdname ==  'RemoteControllerButtonEvent' and cmdset.getValue('ButtonID') == 12 and cmdset.getValue('Status') == 0: 
				RemoteSrv_GlobalEvtFlag = True
			elif cmdset.m_cmdname ==  'RemoteControllerButtonEvent' and cmdset.getValue('ButtonID') == 13 and cmdset.getValue('Status') == 0: 
				RemoteSrv_GlobalEvtFlag = True
			elif cmdset.m_cmdname ==  'RemoteControllerButtonEvent' and cmdset.getValue('ButtonID') == 14 and cmdset.getValue('Status') == 0: 
				RemoteSrv_GlobalEvtFlag = True
		pass

	def execute(self, userdata):
		global RemoteSrv_GlobalEvtFlag
		ResultCode = 'retry'
		if RemoteSrv_GlobalEvtFlag == True:			
			RemoteSrv_GlobalEvtFlag = False
			ResultCode = 'failure'
			return ResultCode

		#ResultCode =Stop()		
		self.m_IsRunning =[True]
		Ret = {}
		Thread_Stop = threading.Thread(target=Stop, args=(self.m_IsRunning,Ret, True))
		Thread_Stop.start()		
		while self.m_IsRunning[0] == True:
			if RemoteSrv_GlobalEvtFlag == True:				
				RemoteSrv_GlobalEvtFlag = False
				ResultCode =  'failure'
				return ResultCode
			pass		
		
		while Thread_Stop.isAlive():
			pass

		if Ret['ResultCode'] == 0:
			ResultCode = 'success'
		else:
			ResultCode = 'failure'
		return ResultCode

##VideoChatSrv ############################################################
#global var

VideoChatSrv_EvtList = {}
VideoChatSrv_CBList = []

VideoChatSrv_EvtList = {'ServiceStatusEvent':'GlobalEvent', 'StartRecObject':'LocalEvent'}
VideoChatSrv_GlobalEvtFlag = False


global VideoChatSrv_IsVideoChatSrv; VideoChatSrv_IsVideoChatSrv= False
global VideoChatSrv_nID;VideoChatSrv_nID = 1

# defien state Init
class VideoChatSrv_Init(smach.State):
	m_IsRunning = [True]	

	def __init__(self):
		smach.State.__init__(self, outcomes=['success','retry','failure'])
		RegEventProc(self.__class__.__name__, self.listener)
	
	def listener(self,cmdset):
		#print 'VideoChatSrv_Init'
		pass

	def execute(self, userdata):
		global VideoChatSrv_nID;VideoChatSrv_nID = 1
		global VideoChatSrv_IsVideoChatSrv; VideoChatSrv_IsVideoChatSrv  = False
		global VideoChatSrv_GlobalEvtFlag; VideoChatSrv_GlobalEvtFlag  = False
		time.sleep(1)
		return 'success'

class VideoChatSrv_Idle(smach.State):

	m_cmdsetList =[]
	
	def __init__(self):
		smach.State.__init__(self, outcomes =  ['StartVideoChatSrv','success','retry','failure'])
		RegEventProc(self.__class__.__name__, self.listener)
	
	def listener(self,cmdset):
		global VideoChatSrv_GlobalEvtFlag

		if VideoChatSrv_EvtList.keys().count(cmdset.m_cmdname) and VideoChatSrv_EvtList[cmdset.m_cmdname] == "GlobalEvent" :				
			#here 			
			if cmdset.m_cmdname ==  'ServiceStatusEvent' and cmdset.getValue('ServiceName') == "VideoChat" and cmdset.getValue('Status') == 1: 	
				self.m_cmdsetList.append(cmdset)
			elif cmdset.m_cmdname ==  'ServiceStatusEvent' and cmdset.getValue('ServiceName') == "VideoChat" and cmdset.getValue('Status') == 0: 	
				self.m_cmdsetList.append(cmdset)

		pass
	
	def execute(self, userdata):
		global VideoChatSrv_nID;VideoChatSrv_nID = 1
		global VideoChatSrv_IsVideoChatSrv; 
		global VideoChatSrv_GlobalEvtFlag
		while True:		
			while len(self.m_cmdsetList) == 0:
				time.sleep(0.001)		
				pass
			cmdset = self.m_cmdsetList.pop(0)

			if cmdset.m_cmdname ==  'ServiceStatusEvent':
				ServiceName = cmdset.getValue('ServiceName')
				Status = cmdset.getValue('Status')
				if ServiceName == 'VideoChat' and Status == 1 :
					

					#SetRecObjectGroup())################################################
					self.m_IsRunning =[True]
					Ret = {}
					Thread_SetRecObjectGroup = threading.Thread(target=SetRecObjectGroup, args=(self.m_IsRunning,Ret, True))
					Thread_SetRecObjectGroup.start()		
					while self.m_IsRunning[0] == True:
						pass		
					while Thread_SetRecObjectGroup.isAlive():
						pass	
					##############################################################################


					#PlayTTS(str(nID)+'. arrive',5)################################################
					self.m_IsRunning =[True]
					Ret = {}
					Thread_PlayTTS = threading.Thread(target=PlayTTS, args=(self.m_IsRunning,Ret, 'Retun to the Docking station',5, True))
					Thread_PlayTTS.start()		
					while self.m_IsRunning[0] == True:
						pass		
					while Thread_PlayTTS.isAlive():
						pass	
					##############################################################################



					#ResultCode = GotoID(VideoChatSrv_nID,True)	################################################		
		
					self.m_IsRunning =[True]
					Ret = {}	
					Thread_GotoID = threading.Thread(target=GotoID, args=(self.m_IsRunning,Ret, VideoChatSrv_nID, True))
					Thread_GotoID.start()	
					while self.m_IsRunning[0] == True:
						pass		
					while Thread_GotoID.isAlive():
						pass	
					ResultCode = Ret["ResultCode"]
					##############################################################################
					
					

					if ResultCode == 0:
						
						#PlayTTS(str(VideoChatSrv_nID)+'. arrive',5))################################################
						self.m_IsRunning =[True]
						Ret = {}
						Thread_PlayTTS = threading.Thread(target=PlayTTS, args=(self.m_IsRunning,Ret, str(VideoChatSrv_nID)+'. arrive',5, True))
						Thread_PlayTTS.start()		
						while self.m_IsRunning[0] == True:
							pass		
						while Thread_PlayTTS.isAlive():
							pass	
						##############################################################################
						
						#PlayTTS(str(nID)+'. arrive',5)################################################
						self.m_IsRunning =[True]
						Ret = {}
						Thread_PlayTTS = threading.Thread(target=PlayTTS, args=(self.m_IsRunning,Ret, 'Start VideoChat service',5, True))
						Thread_PlayTTS.start()		
						while self.m_IsRunning[0] == True:
							pass		
						while Thread_PlayTTS.isAlive():
							pass	
						##############################################################################

						
						VideoChatSrv_IsVideoChatSrv= True
						VideoChatSrv_GlobalEvtFlag = False
						return 'StartVideoChatSrv'

					else:
						#PlayTTS(str(VideoChatSrv_nID)+'. fail',5)################################################
						self.m_IsRunning =[True]
						Ret = {}
						Thread_PlayTTS = threading.Thread(target=PlayTTS, args=(self.m_IsRunning,Ret, str(VideoChatSrv_nID)+'. fail',5, True))
						Thread_PlayTTS.start()		
						while self.m_IsRunning[0] == True:
							pass		
						while Thread_PlayTTS.isAlive():
							pass		
						##############################################################################
						
						VideoChatSrv_IsVideoChatSrv= False
						VideoChatSrv_GlobalEvtFlag = False
						return 'retry'

				elif ServiceName == 'VideoChat' and Status == 0 :

					if VideoChatSrv_IsVideoChatSrv ==False:
						#PlayTTS(str(nID)+'. arrive',5)
						self.m_IsRunning =[True]
						Ret = {}
						Thread_PlayTTS = threading.Thread(target=PlayTTS, args=(self.m_IsRunning,Ret, 'Not ready to start VideoChat service',5, True))
						Thread_PlayTTS.start()		
						while self.m_IsRunning[0] == True:
							pass		
						while Thread_PlayTTS.isAlive():
							pass	
					else:
						
						#PlayTTS(str(nID)+'. arrive',5)################################################
						self.m_IsRunning =[True]
						Ret = {}
						Thread_PlayTTS = threading.Thread(target=PlayTTS, args=(self.m_IsRunning,Ret, 'Stop VideoChat service',5, True))
						Thread_PlayTTS.start()		
						while self.m_IsRunning[0] == True:
							pass		
						while Thread_PlayTTS.isAlive():
							pass	
						##############################################################################


						#PlayTTS(str(nID)+'. arrive',5)################################################
						self.m_IsRunning =[True]
						Ret = {}
						Thread_PlayTTS = threading.Thread(target=PlayTTS, args=(self.m_IsRunning,Ret, 'Retun to the Docking station',5, True))
						Thread_PlayTTS.start()		
						while self.m_IsRunning[0] == True:
							pass		
						while Thread_PlayTTS.isAlive():
							pass	
						##############################################################################

						#ResultCode = GotoID(VideoChatSrv_nID,True)	################################################	
						self.m_IsRunning =[True]
						Ret = {}	
						Thread_GotoID = threading.Thread(target=GotoID, args=(self.m_IsRunning,Ret, VideoChatSrv_nID, True))
						Thread_GotoID.start()	
						while self.m_IsRunning[0] == True:
							pass		
						while Thread_GotoID.isAlive():
							pass	

						ResultCode = Ret["ResultCode"]
				
						##############################################################################

						if ResultCode == 0:
							#PlayTTS(str(nID)+'. arrive',5)
							self.m_IsRunning =[True]
							Ret = {}
							Thread_PlayTTS = threading.Thread(target=PlayTTS, args=(self.m_IsRunning,Ret, str(VideoChatSrv_nID)+'. arrive',5, True))
							Thread_PlayTTS.start()		
							while self.m_IsRunning[0] == True:
								pass		
							while Thread_PlayTTS.isAlive():
								pass	

							##############################################################################

							VideoChatSrv_IsVideoChatSrv= False
							VideoChatSrv_GlobalEvtFlag = False
							return 'retry'

						else:
							#PlayTTS(str(VideoChatSrv_nID)+'. fail',5)
							self.m_IsRunning =[True]
							Ret = {}
							Thread_PlayTTS = threading.Thread(target=PlayTTS, args=(self.m_IsRunning,Ret, str(VideoChatSrv_nID)+'. fail',5, True))
							Thread_PlayTTS.start()		
							while self.m_IsRunning[0] == True:
								pass		
							while Thread_PlayTTS.isAlive():
								pass		
							##############################################################################

							VideoChatSrv_IsVideoChatSrv= False
							VideoChatSrv_GlobalEvtFlag = False
							return 'retry'

			time.sleep(0.001)

#define state Wondering		
class VideoChatSrv_Wondering(smach.State):
	
	m_IsRunning = [True]
	
	def __init__(self):
		smach.State.__init__(self, outcomes = ['success', 'retry','failure'])
		RegEventProc(self.__class__.__name__, self.listener)
	
	def listener(self,cmdset):
		global VideoChatSrv_GlobalEvtFlag
		#print 'VideoChatSrv_Wondering'
		if VideoChatSrv_EvtList.keys().count(cmdset.m_cmdname) and VideoChatSrv_EvtList[cmdset.m_cmdname] == "GlobalEvent" :
			if cmdset.m_cmdname ==  'ServiceStatusEvent' and cmdset.getValue('ServiceName') == "VideoChat" and cmdset.getValue('Status') == 1: 
				VideoChatSrv_GlobalEvtFlag = True
			elif cmdset.m_cmdname ==  'ServiceStatusEvent' and cmdset.getValue('ServiceName') == "VideoChat" and cmdset.getValue('Status') == 0: 
				VideoChatSrv_GlobalEvtFlag = True
		pass

	def execute(self, userdata):
		global VideoChatSrv_GlobalEvtFlag
		ResultCode = 'retry'
		if VideoChatSrv_GlobalEvtFlag == True:			
			VideoChatSrv_GlobalEvtFlag = False
			ResultCode = 'failure'
			return ResultCode
	 	
		global VideoChatSrv_nID
        	VideoChatSrv_nID = VideoChatSrv_nID+1
		if(VideoChatSrv_nID > 5):
			VideoChatSrv_nID = 2

		#ResultCode = GotoID(VideoChatSrv_nID,True)
		self.m_IsRunning =[True]
		Ret = {}	
		Thread_GotoID = threading.Thread(target=GotoID, args=(self.m_IsRunning,Ret, VideoChatSrv_nID,  True))
		Thread_GotoID.start()	
		while self.m_IsRunning[0] == True  :
			if VideoChatSrv_GlobalEvtFlag == True:				
				VideoChatSrv_GlobalEvtFlag = False
				ResultCode =  'failure'
				return ResultCode		
		
			pass
		while Thread_GotoID.isAlive():
			pass	
		
		ResultCode = Ret["ResultCode"]

		ResultCode = 0

		if ResultCode == 0:
			#PlayTTS(str(VideoChatSrv_nID)+ u'. Arrive',5,True)
			
			self.m_IsRunning =[True]
			Ret = {}
			Thread_PlayTTS = threading.Thread(target=PlayTTS, args=(self.m_IsRunning,Ret, str(VideoChatSrv_nID)+'. arrive',5, True))
			Thread_PlayTTS.start()		
			while self.m_IsRunning[0] == True:
				if VideoChatSrv_GlobalEvtFlag == True:				
					VideoChatSrv_GlobalEvtFlag = False
					ResultCode =  'failure'
					return ResultCode			
				pass		
			while Thread_PlayTTS.isAlive():
				pass
			
			return "success"
	
		else:
			#PlayTTS(str(VideoChatSrv_nID)+u'. failure',5,True)
			self.m_IsRunning =[True]
			Ret = {}
			Thread_PlayTTS = threading.Thread(target=PlayTTS, args=(self.m_IsRunning,Ret, str(VideoChatSrv_nID)+'. failure',5, True))
			Thread_PlayTTS.start()		
			while self.m_IsRunning[0] == True:
				if VideoChatSrv_GlobalEvtFlag == True:				
					VideoChatSrv_GlobalEvtFlag = False
					ResultCode =  'failure'
					return ResultCode
				pass		
			while Thread_PlayTTS.isAlive():
				pass

			return "retry"
				

class VideoChatSrv_FindUser(smach.State):
		
	m_cmdset = None
	m_IsRunning = [True]	
	
	def __init__(self):
		smach.State.__init__(self, outcomes = ['success', 'retry','failure'])
		RegEventProc(self.__class__.__name__, self.listener)
	
	def listener(self,cmdset):
		#print 'VideoChatSrv_FindUser'

		global VideoChatSrv_GlobalEvtFlag
		if VideoChatSrv_EvtList.keys().count(cmdset.m_cmdname) and VideoChatSrv_EvtList[cmdset.m_cmdname] == "GlobalEvent" :
			if cmdset.m_cmdname ==  'ServiceStatusEvent' and cmdset.getValue('ServiceName') == "VideoChat" and cmdset.getValue('Status') == 1: 
				VideoChatSrv_GlobalEvtFlag = True
			elif cmdset.m_cmdname ==  'ServiceStatusEvent' and cmdset.getValue('ServiceName') == "VideoChat" and cmdset.getValue('Status') == 0: 
				VideoChatSrv_GlobalEvtFlag = True

		self.m_cmdset  = cmdset
		pass


	def execute(self, userdata):
		global VideoChatSrv_GlobalEvtFlag	
		ResultCode =  'retry'
		self.m_cmdset = None			

		if VideoChatSrv_GlobalEvtFlag == True:				
			VideoChatSrv_GlobalEvtFlag = False
			ResultCode =  'failure'
			return ResultCode

		#Todo face recognition
		FaceDetectedFlag = False
		
		#PlayTTS(str(VideoChatSrv_nID)+u'. failure',5,True)
		self.m_IsRunning =[True]
		Ret = {}
		Thread_PlayTTS = threading.Thread(target=PlayTTS, args=(self.m_IsRunning,Ret, 'Start Finding User',5, False))
		Thread_PlayTTS.start()		
		while self.m_IsRunning[0] == True:
			if VideoChatSrv_GlobalEvtFlag == True:				
				VideoChatSrv_GlobalEvtFlag = False
				ResultCode =  'failure'
				return ResultCode
			pass		
		while Thread_PlayTTS.isAlive():
			pass

		#StartFaceRecognition()
		self.m_IsRunning =[True]
		Ret = {}	
		Thread_StartFaceRecognition = threading.Thread(target=StartFaceRecognition, args=(self.m_IsRunning,Ret, True))
		Thread_StartFaceRecognition.start()	
		while self.m_IsRunning[0] == True:
			if VideoChatSrv_GlobalEvtFlag == True:				
				VideoChatSrv_GlobalEvtFlag = False
				ResultCode =  'failure'
				return ResultCode		
			pass	
		while Thread_StartFaceRecognition.isAlive():
			pass

		ResultCode = Ret["ResultCode"]
		
		#Todo Idle face recognition
		i = 0
			
		while i <=10000:
			if VideoChatSrv_GlobalEvtFlag == True:				
				VideoChatSrv_GlobalEvtFlag = False
				ResultCode =  'failure'
				return ResultCode		

			if self.m_cmdset == None:
				time.sleep(0.001)			
			else:
				cmdset = self.m_cmdset
				self.m_cmdset = None
				if cmdset.m_cmdname == "StartRecObject":
					FaceDetectedFlag = True
					break					
			i+=1

		#StopFaceRecognition()
		self.m_IsRunning =[True]
		Ret = {}	
		Thread_StopFaceRecognition = threading.Thread(target=StopFaceRecognition, args=(self.m_IsRunning,Ret,))
		Thread_StopFaceRecognition.start()	
		while self.m_IsRunning[0] == True:
			if VideoChatSrv_GlobalEvtFlag == True:				
				VideoChatSrv_GlobalEvtFlag = False
				ResultCode =  'failure'
				return ResultCode
			pass
		while Thread_StopFaceRecognition.isAlive():
			pass
	



		if FaceDetectedFlag ==True:
			#PlayTTS(u'success. Find the face',5, True)
			self.m_IsRunning =[True]
			Ret = {}
			Thread_PlayTTS = threading.Thread(target=PlayTTS, args=(self.m_IsRunning,Ret,'success. Find the face',5, True))
			Thread_PlayTTS.start()		
			while self.m_IsRunning[0] == True:
				if VideoChatSrv_GlobalEvtFlag == True:				
					VideoChatSrv_GlobalEvtFlag = False
					ResultCode =  'failure'
					return ResultCode
				pass		
			while Thread_PlayTTS.isAlive():
				pass
			
			return  'success'
			
		elif FaceDetectedFlag == False:
			#PlayTTS(u'Retry. go to the other place',5, True)
			self.m_IsRunning =[True]
			Ret = {}
			Thread_PlayTTS = threading.Thread(target=PlayTTS, args=(self.m_IsRunning,Ret,'. Retry. go to the other place',5, True))
			Thread_PlayTTS.start()		
			while self.m_IsRunning[0] == True:
				if VideoChatSrv_GlobalEvtFlag == True:				
					VideoChatSrv_GlobalEvtFlag = False
					ResultCode =  'failure'
					return ResultCode
				pass		
			while Thread_PlayTTS.isAlive():
				pass

			return 'retry'
	

# define state VideoChat
class VideoChatSrv_VideoChat(smach.State):
	m_cmdset = None
	m_IsRunning = [True]	
	
	def __init__(self):
		smach.State.__init__(self, outcomes=['success','retry','failure'])
		RegEventProc(self.__class__.__name__, self.listener)
	
	def listener(self,cmdset):
		#print 'VideoChatSrv_VideoChat'
		global VideoChatSrv_GlobalEvtFlag

		if VideoChatSrv_EvtList.keys().count(cmdset.m_cmdname) and VideoChatSrv_EvtList[cmdset.m_cmdname] == "GlobalEvent" :
			if cmdset.m_cmdname ==  'ServiceStatusEvent' and cmdset.getValue('ServiceName') == "VideoChat" and cmdset.getValue('Status') == 1: 
				VideoChatSrv_GlobalEvtFlag = True
			elif cmdset.m_cmdname ==  'ServiceStatusEvent' and cmdset.getValue('ServiceName') == "VideoChat" and cmdset.getValue('Status') == 0: 
				VideoChatSrv_GlobalEvtFlag = True


		self. m_cmdset = cmdset
		pass

	def execute(self, userdata):
		global VideoChatSrv_GlobalEvtFlag
		if VideoChatSrv_GlobalEvtFlag == True:				
			VideoChatSrv_GlobalEvtFlag = False
			ResultCode =  'failure'
			return ResultCode
		
		#PlayTTS('Start Video Chat',5,True)
		self.m_IsRunning =[True]
		Ret = {}
		Thread_PlayTTS = threading.Thread(target=PlayTTS, args=(self.m_IsRunning,Ret, 'Start Video Chat',5,True))
		Thread_PlayTTS.start()		
		while self.m_IsRunning[0] == True:
			pass
			if VideoChatSrv_GlobalEvtFlag == True:				
					VideoChatSrv_GlobalEvtFlag = False
					ResultCode =  'failure'
					return ResultCode		
		while Thread_PlayTTS.isAlive():
			pass		

		while True:
			while self. m_cmdset == None:
				time.sleep(0.001)


			if VideoChatSrv_GlobalEvtFlag == True:				
				VideoChatSrv_GlobalEvtFlag = False
				ResultCode =  'failure'
				return ResultCode
			pass
	
##AlarmSrv############################################################
class AlarmSrv_Init(smach.State):
	def __init__(self):
		smach.State.__init__(self, outcomes=['success','retry','failure'])
		print 'Create AlarmSrv_Init'	
	def __del__(self):
		print 'Delete AlarmSrv_Init'	
	def execute(self, userdata):
			time.sleep(1)
			return 'success'
		

class AlarmSrv_Alarm(smach.State):
	def __init__(self):
		smach.State.__init__(self, outcomes = ['success', 'retry','failure'])
		print 'Create AlarmSrv_Alarm'
	def __del__(self):
		print 'Delete AlarmSrv_Alarm'
	def execute(self, userdata):
		time.sleep(10)
		#PlayTTS('Wake up',5)
		return 'success'
	

###NavigationSrv###########################################################
class NavigationSrv_Init(smach.State):
	def __init__(self):
		smach.State.__init__(self, outcomes=['success','retry','failure'])
	
	def execute(self, userdata):
		time.sleep(1)
		return 'success'

class NavigationSrv_Idle(smach.State):
	def __init__(self):
		smach.State.__init__(self, outcomes = ['success', 'retry','failure'])
	def execute(self, userdata):
		time.sleep(5)
		return 'success'

##TouchSrv ############################################################
TouchSrv_EvtList = {}
TouchSrv_CBList = []

TouchSrv_EvtList = {'TouchSensorEvent':'GlobalEvent'}
TouchSrv_GlobalEvtFlag = False


class TouchSrv_Init(smach.State):
	def __init__(self):
		smach.State.__init__(self, outcomes=['success','retry','failure'])
	
	def execute(self, userdata):
		time.sleep(1)
		return 'success'

class TouchSrv_Idle(smach.State):
	m_cmdsetList =[]
	
	def __init__(self):
		smach.State.__init__(self, outcomes = ['righthand','lefthand','righthead','lefthead','rightwheel','leftwheel', 'retry','failure'])
		RegEventProc(self.__class__.__name__, self.listener)

	def listener(self,cmdset):	
		
		if TouchSrv_EvtList.keys().count(cmdset.m_cmdname) and TouchSrv_EvtList[cmdset.m_cmdname] == "GlobalEvent" :				
			#here 			
			if cmdset.m_cmdname ==  'TouchSensorEvent' and cmdset.getValue('ButtonID') == 0 and cmdset.getValue('Status') == 1: 
				self.m_cmdsetList.append(cmdset)
			elif cmdset.m_cmdname ==  'TouchSensorEvent' and cmdset.getValue('ButtonID') == 1 and cmdset.getValue('Status') == 1 :
				self.m_cmdsetList.append(cmdset)
			elif cmdset.m_cmdname ==  'TouchSensorEvent' and cmdset.getValue('ButtonID') == 2 and cmdset.getValue('Status') == 1:
				self.m_cmdsetList.append(cmdset)
			elif cmdset.m_cmdname ==  'TouchSensorEvent' and cmdset.getValue('ButtonID') == 3 and cmdset.getValue('Status') == 1:
				self.m_cmdsetList.append(cmdset)
			elif cmdset.m_cmdname ==  'TouchSensorEvent' and cmdset.getValue('ButtonID') == 4 and cmdset.getValue('Status') == 1 :
				self.m_cmdsetList.append(cmdset)
			elif cmdset.m_cmdname ==  'TouchSensorEvent' and cmdset.getValue('ButtonID') == 5 and cmdset.getValue('Status') ==1:
				self.m_cmdsetList.append(cmdset)
		pass
			
	def execute(self, userdata):
		global TouchSrv_GlobalEvtFlag
		while True:		
			
			while len(self.m_cmdsetList) == 0:
				time.sleep(0.001)		
				pass
			cmdset = self.m_cmdsetList.pop(0)

			if cmdset.m_cmdname ==  'TouchSensorEvent' and cmdset.getValue('ButtonID') == 0 and cmdset.getValue('Status') == 1: 
					TouchSrv_GlobalEvtFlag = False
					return 'lefthead'
			
			elif cmdset.m_cmdname ==  'TouchSensorEvent' and cmdset.getValue('ButtonID') == 1 and cmdset.getValue('Status') == 1: 
					TouchSrv_GlobalEvtFlag = False
					return 'righthead'		

			elif cmdset.m_cmdname ==  'TouchSensorEvent' and cmdset.getValue('ButtonID') == 2 and cmdset.getValue('Status') == 1: 
					TouchSrv_GlobalEvtFlag = False
					return 'leftwheel'

			elif cmdset.m_cmdname ==  'TouchSensorEvent' and cmdset.getValue('ButtonID') == 3 and cmdset.getValue('Status') == 1: 
					TouchSrv_GlobalEvtFlag = False
					return 'rightwheel'

			elif cmdset.m_cmdname ==  'TouchSensorEvent' and cmdset.getValue('ButtonID') == 4 and cmdset.getValue('Status') == 1: 
					TouchSrv_GlobalEvtFlag = False
					return 'lefthand'

			elif cmdset.m_cmdname ==  'TouchSensorEvent' and cmdset.getValue('ButtonID') == 5 and cmdset.getValue('Status') == 1: 
					TouchSrv_GlobalEvtFlag = False
					return 'righthand'

		
			time.sleep(0.001)


class TouchSrv_RightHand(smach.State):
	m_IsRunning = [True]
	
	def __init__(self):
		smach.State.__init__(self, outcomes = ['success','retry','failure'])
		RegEventProc(self.__class__.__name__, self.listener)
	def listener(self,cmdset):
		global TouchSrv_GlobalEvtFlag	
		
		if TouchSrv_EvtList.keys().count(cmdset.m_cmdname) and TouchSrv_EvtList[cmdset.m_cmdname] == "GlobalEvent" :				
			#here 			
			if cmdset.m_cmdname ==  'TouchSensorEvent' and cmdset.getValue('ButtonID') == 0 and cmdset.getValue('Status') == 1: 
				TouchSrv_GlobalEvtFlag = True
			elif cmdset.m_cmdname ==  'TouchSensorEvent' and cmdset.getValue('ButtonID') == 1 and cmdset.getValue('Status') == 1 :
				TouchSrv_GlobalEvtFlag = True
			elif cmdset.m_cmdname ==  'TouchSensorEvent' and cmdset.getValue('ButtonID') == 2 and cmdset.getValue('Status') == 1:
				TouchSrv_GlobalEvtFlag = True
			elif cmdset.m_cmdname ==  'TouchSensorEvent' and cmdset.getValue('ButtonID') == 3 and cmdset.getValue('Status') == 1:
				TouchSrv_GlobalEvtFlag = True
			elif cmdset.m_cmdname ==  'TouchSensorEvent' and cmdset.getValue('ButtonID') == 4 and cmdset.getValue('Status') == 1 :
				TouchSrv_GlobalEvtFlag = True
			elif cmdset.m_cmdname ==  'TouchSensorEvent' and cmdset.getValue('ButtonID') == 5 and cmdset.getValue('Status') ==1:
				TouchSrv_GlobalEvtFlag = True
		pass
	def execute(self,userdata):
		global TouchSrv_GlobalEvtFlag	
		ResultCode = 'retry'
		if TouchSrv_GlobalEvtFlag == True:			
			TouchSrv_GlobalEvtFlag = False
			ResultCode = 'failure'
			return ResultCode	
		
		#ResultCode =PlayTTS()		
		self.m_IsRunning =[True]
		Ret = {}
		Thread_PlayTTS = threading.Thread(target=PlayTTS, args=(self.m_IsRunning,Ret,'Right Hand', 5, True))
		Thread_PlayTTS.start()		
		
		while self.m_IsRunning[0] == True:
			if TouchSrv_GlobalEvtFlag == True:				
				TouchSrv_GlobalEvtFlag = False
				ResultCode =  'failure'
				return ResultCode
			pass		
		
		while Thread_PlayTTS.isAlive():
			pass
		
		if Ret['ResultCode'] == 0:
			ResultCode = 'success'
		else:
			ResultCode = 'failure'
		return ResultCode

class TouchSrv_LeftHand(smach.State):
	m_IsRunning = [True]
	
	def __init__(self):
		smach.State.__init__(self, outcomes = ['success','retry','failure'])
		RegEventProc(self.__class__.__name__, self.listener)
	def listener(self,cmdset):
		global TouchSrv_GlobalEvtFlag	
		
		if TouchSrv_EvtList.keys().count(cmdset.m_cmdname) and TouchSrv_EvtList[cmdset.m_cmdname] == "GlobalEvent" :				
			#here 			
			if cmdset.m_cmdname ==  'TouchSensorEvent' and cmdset.getValue('ButtonID') == 0 and cmdset.getValue('Status') == 1: 
				TouchSrv_GlobalEvtFlag = True
			elif cmdset.m_cmdname ==  'TouchSensorEvent' and cmdset.getValue('ButtonID') == 1 and cmdset.getValue('Status') == 1 :
				TouchSrv_GlobalEvtFlag = True
			elif cmdset.m_cmdname ==  'TouchSensorEvent' and cmdset.getValue('ButtonID') == 2 and cmdset.getValue('Status') == 1:
				TouchSrv_GlobalEvtFlag = True
			elif cmdset.m_cmdname ==  'TouchSensorEvent' and cmdset.getValue('ButtonID') == 3 and cmdset.getValue('Status') == 1:
				TouchSrv_GlobalEvtFlag = True
			elif cmdset.m_cmdname ==  'TouchSensorEvent' and cmdset.getValue('ButtonID') == 4 and cmdset.getValue('Status') == 1 :
				TouchSrv_GlobalEvtFlag = True
			elif cmdset.m_cmdname ==  'TouchSensorEvent' and cmdset.getValue('ButtonID') == 5 and cmdset.getValue('Status') ==1:
				TouchSrv_GlobalEvtFlag = True
		pass
	def execute(self,userdata):
		global TouchSrv_GlobalEvtFlag	
		ResultCode = 'retry'
		if TouchSrv_GlobalEvtFlag == True:			
			TouchSrv_GlobalEvtFlag = False
			ResultCode = 'failure'
			return ResultCode	
		
		#ResultCode =PlayTTS()		
		self.m_IsRunning =[True]
		Ret = {}
		Thread_PlayTTS = threading.Thread(target=PlayTTS, args=(self.m_IsRunning,Ret,'Left Hand', 5, True))
		Thread_PlayTTS.start()		
		
		while self.m_IsRunning[0] == True:
			if TouchSrv_GlobalEvtFlag == True:				
				TouchSrv_GlobalEvtFlag = False
				ResultCode =  'failure'
				return ResultCode
			pass		
		
		while Thread_PlayTTS.isAlive():
			pass
		
		if Ret['ResultCode'] == 0:
			ResultCode = 'success'
		else:
			ResultCode = 'failure'
		return ResultCode


class TouchSrv_RightHead(smach.State):
	m_IsRunning = [True]
	
	def __init__(self):
		smach.State.__init__(self, outcomes = ['success','retry','failure'])
		RegEventProc(self.__class__.__name__, self.listener)
	def listener(self,cmdset):
		global TouchSrv_GlobalEvtFlag	
		
		if TouchSrv_EvtList.keys().count(cmdset.m_cmdname) and TouchSrv_EvtList[cmdset.m_cmdname] == "GlobalEvent" :				
			#here 			
			if cmdset.m_cmdname ==  'TouchSensorEvent' and cmdset.getValue('ButtonID') == 0 and cmdset.getValue('Status') == 1: 
				TouchSrv_GlobalEvtFlag = True
			elif cmdset.m_cmdname ==  'TouchSensorEvent' and cmdset.getValue('ButtonID') == 1 and cmdset.getValue('Status') == 1 :
				TouchSrv_GlobalEvtFlag = True
			elif cmdset.m_cmdname ==  'TouchSensorEvent' and cmdset.getValue('ButtonID') == 2 and cmdset.getValue('Status') == 1:
				TouchSrv_GlobalEvtFlag = True
			elif cmdset.m_cmdname ==  'TouchSensorEvent' and cmdset.getValue('ButtonID') == 3 and cmdset.getValue('Status') == 1:
				TouchSrv_GlobalEvtFlag = True
			elif cmdset.m_cmdname ==  'TouchSensorEvent' and cmdset.getValue('ButtonID') == 4 and cmdset.getValue('Status') == 1 :
				TouchSrv_GlobalEvtFlag = True
			elif cmdset.m_cmdname ==  'TouchSensorEvent' and cmdset.getValue('ButtonID') == 5 and cmdset.getValue('Status') ==1:
				TouchSrv_GlobalEvtFlag = True
		pass
	def execute(self,userdata):
		global TouchSrv_GlobalEvtFlag	
		ResultCode = 'retry'
		if TouchSrv_GlobalEvtFlag == True:			
			TouchSrv_GlobalEvtFlag = False
			ResultCode = 'failure'
			return ResultCode	
		
		#ResultCode =PlayTTS()		
		self.m_IsRunning =[True]
		Ret = {}
		Thread_PlayTTS = threading.Thread(target=PlayTTS, args=(self.m_IsRunning,Ret,'Right Head ', 5, True))
		Thread_PlayTTS.start()		
		
		while self.m_IsRunning[0] == True:
			if TouchSrv_GlobalEvtFlag == True:				
				TouchSrv_GlobalEvtFlag = False
				ResultCode =  'failure'
				return ResultCode
			pass		
		
		while Thread_PlayTTS.isAlive():
			pass
		
		if Ret['ResultCode'] == 0:
			ResultCode = 'success'
		else:
			ResultCode = 'failure'
		return ResultCode

class TouchSrv_LeftHead(smach.State):
	m_IsRunning = [True]
	
	def __init__(self):
		smach.State.__init__(self, outcomes = ['success','retry','failure'])
		RegEventProc(self.__class__.__name__, self.listener)
	def listener(self,cmdset):
		global TouchSrv_GlobalEvtFlag	
		
		if TouchSrv_EvtList.keys().count(cmdset.m_cmdname) and TouchSrv_EvtList[cmdset.m_cmdname] == "GlobalEvent" :				
			#here 			
			if cmdset.m_cmdname ==  'TouchSensorEvent' and cmdset.getValue('ButtonID') == 0 and cmdset.getValue('Status') == 1: 
				TouchSrv_GlobalEvtFlag = True
			elif cmdset.m_cmdname ==  'TouchSensorEvent' and cmdset.getValue('ButtonID') == 1 and cmdset.getValue('Status') == 1 :
				TouchSrv_GlobalEvtFlag = True
			elif cmdset.m_cmdname ==  'TouchSensorEvent' and cmdset.getValue('ButtonID') == 2 and cmdset.getValue('Status') == 1:
				TouchSrv_GlobalEvtFlag = True
			elif cmdset.m_cmdname ==  'TouchSensorEvent' and cmdset.getValue('ButtonID') == 3 and cmdset.getValue('Status') == 1:
				TouchSrv_GlobalEvtFlag = True
			elif cmdset.m_cmdname ==  'TouchSensorEvent' and cmdset.getValue('ButtonID') == 4 and cmdset.getValue('Status') == 1 :
				TouchSrv_GlobalEvtFlag = True
			elif cmdset.m_cmdname ==  'TouchSensorEvent' and cmdset.getValue('ButtonID') == 5 and cmdset.getValue('Status') ==1:
				TouchSrv_GlobalEvtFlag = True
		pass
	def execute(self,userdata):
		global TouchSrv_GlobalEvtFlag	
		ResultCode = 'retry'
		if TouchSrv_GlobalEvtFlag == True:			
			TouchSrv_GlobalEvtFlag = False
			ResultCode = 'failure'
			return ResultCode	
		
		#ResultCode =PlayTTS()		
		self.m_IsRunning =[True]
		Ret = {}
		Thread_PlayTTS = threading.Thread(target=PlayTTS, args=(self.m_IsRunning,Ret,'Left Head ', 5, True))
		Thread_PlayTTS.start()		
		
		while self.m_IsRunning[0] == True:
			if TouchSrv_GlobalEvtFlag == True:				
				TouchSrv_GlobalEvtFlag = False
				ResultCode =  'failure'
				return ResultCode
			pass		
		
		while Thread_PlayTTS.isAlive():
			pass
		
		if Ret['ResultCode'] == 0:
			ResultCode = 'success'
		else:
			ResultCode = 'failure'
		return ResultCode



class TouchSrv_RightWheel(smach.State):
	m_IsRunning = [True]
	
	def __init__(self):
		smach.State.__init__(self, outcomes = ['success','retry','failure'])
		RegEventProc(self.__class__.__name__, self.listener)
	def listener(self,cmdset):
		global TouchSrv_GlobalEvtFlag	
		
		if TouchSrv_EvtList.keys().count(cmdset.m_cmdname) and TouchSrv_EvtList[cmdset.m_cmdname] == "GlobalEvent" :				
			#here 			
			if cmdset.m_cmdname ==  'TouchSensorEvent' and cmdset.getValue('ButtonID') == 0 and cmdset.getValue('Status') == 1: 
				TouchSrv_GlobalEvtFlag = True
			elif cmdset.m_cmdname ==  'TouchSensorEvent' and cmdset.getValue('ButtonID') == 1 and cmdset.getValue('Status') == 1 :
				TouchSrv_GlobalEvtFlag = True
			elif cmdset.m_cmdname ==  'TouchSensorEvent' and cmdset.getValue('ButtonID') == 2 and cmdset.getValue('Status') == 1:
				TouchSrv_GlobalEvtFlag = True
			elif cmdset.m_cmdname ==  'TouchSensorEvent' and cmdset.getValue('ButtonID') == 3 and cmdset.getValue('Status') == 1:
				TouchSrv_GlobalEvtFlag = True
			elif cmdset.m_cmdname ==  'TouchSensorEvent' and cmdset.getValue('ButtonID') == 4 and cmdset.getValue('Status') == 1 :
				TouchSrv_GlobalEvtFlag = True
			elif cmdset.m_cmdname ==  'TouchSensorEvent' and cmdset.getValue('ButtonID') == 5 and cmdset.getValue('Status') ==1:
				TouchSrv_GlobalEvtFlag = True
		pass
	def execute(self,userdata):
		global TouchSrv_GlobalEvtFlag	
		ResultCode = 'retry'
		if TouchSrv_GlobalEvtFlag == True:			
			TouchSrv_GlobalEvtFlag = False
			ResultCode = 'failure'
			return ResultCode	
		
		#ResultCode =PlayTTS()		
		self.m_IsRunning =[True]
		Ret = {}
		Thread_PlayTTS = threading.Thread(target=PlayTTS, args=(self.m_IsRunning,Ret,'Right Wheel ', 5, True))
		Thread_PlayTTS.start()		
		
		while self.m_IsRunning[0] == True:
			if TouchSrv_GlobalEvtFlag == True:				
				TouchSrv_GlobalEvtFlag = False
				ResultCode =  'failure'
				return ResultCode
			pass		
		
		while Thread_PlayTTS.isAlive():
			pass
		
		if Ret['ResultCode'] == 0:
			ResultCode = 'success'
		else:
			ResultCode = 'failure'
		return ResultCode



class TouchSrv_LeftWheel(smach.State):
	m_IsRunning = [True]
	
	def __init__(self):
		smach.State.__init__(self, outcomes = ['success','retry','failure'])
		RegEventProc(self.__class__.__name__, self.listener)
	def listener(self,cmdset):
		global TouchSrv_GlobalEvtFlag	
		
		if TouchSrv_EvtList.keys().count(cmdset.m_cmdname) and TouchSrv_EvtList[cmdset.m_cmdname] == "GlobalEvent" :				
			#here 			
			if cmdset.m_cmdname ==  'TouchSensorEvent' and cmdset.getValue('ButtonID') == 0 and cmdset.getValue('Status') == 1: 
				TouchSrv_GlobalEvtFlag = True
			elif cmdset.m_cmdname ==  'TouchSensorEvent' and cmdset.getValue('ButtonID') == 1 and cmdset.getValue('Status') == 1 :
				TouchSrv_GlobalEvtFlag = True
			elif cmdset.m_cmdname ==  'TouchSensorEvent' and cmdset.getValue('ButtonID') == 2 and cmdset.getValue('Status') == 1:
				TouchSrv_GlobalEvtFlag = True
			elif cmdset.m_cmdname ==  'TouchSensorEvent' and cmdset.getValue('ButtonID') == 3 and cmdset.getValue('Status') == 1:
				TouchSrv_GlobalEvtFlag = True
			elif cmdset.m_cmdname ==  'TouchSensorEvent' and cmdset.getValue('ButtonID') == 4 and cmdset.getValue('Status') == 1 :
				TouchSrv_GlobalEvtFlag = True
			elif cmdset.m_cmdname ==  'TouchSensorEvent' and cmdset.getValue('ButtonID') == 5 and cmdset.getValue('Status') ==1:
				TouchSrv_GlobalEvtFlag = True
		pass
	def execute(self,userdata):
		global TouchSrv_GlobalEvtFlag	
		ResultCode = 'retry'
		if TouchSrv_GlobalEvtFlag == True:			
			TouchSrv_GlobalEvtFlag = False
			ResultCode = 'failure'
			return ResultCode	
		
		#ResultCode =PlayTTS()		
		self.m_IsRunning =[True]
		Ret = {}
		Thread_PlayTTS = threading.Thread(target=PlayTTS, args=(self.m_IsRunning,Ret,'Left Wheel ', 5, True))
		Thread_PlayTTS.start()		
		
		while self.m_IsRunning[0] == True:
			if TouchSrv_GlobalEvtFlag == True:				
				TouchSrv_GlobalEvtFlag = False
				ResultCode =  'failure'
				return ResultCode
			pass		
		
		while Thread_PlayTTS.isAlive():
			pass
		
		if Ret['ResultCode'] == 0:
			ResultCode = 'success'
		else:
			ResultCode = 'failure'
		return ResultCode



##VoiceSrv ############################################################
class VoiceSrv_Init(smach.State):
	def __init__(self):
		smach.State.__init__(self, outcomes=['success','retry','failure'])
	
	def execute(self, userdata):
		time.sleep(1)
		return 'success'

class VoiceSrv_Idle(smach.State):
	def __init__(self):
		smach.State.__init__(self, outcomes = ['success', 'retry','failure'])
	def execute(self, userdata):
		time.sleep(5)
		return 'success'




##ReactionSrv ############################################################
class ReactionSrv_Init(smach.State):
	def __init__(self):
		smach.State.__init__(self, outcomes=['success','retry','failure'])
	
	def execute(self, userdata):
		time.sleep(1)
		return 'success'

	
class ReactionSrv_Idle(smach.State):
	def __init__(self):
		smach.State.__init__(self, outcomes = ['success', 'retry','failure'])
	def execute(self, userdata):
		time.sleep(5)
		return 'success'

	
			

#######################################################################################################
#######################################################################################################
##Define Action
#######################################################################################################       
#define GotoID
def GotoID(IsRunning, Return, ID,SyncFlag = False):
	ResultCode = 'failure'
	
	if ID != 0 :
		#to do goto id
		rospy.loginfo('Moving.......')
		global g_cmdID;
		g_cmdID +=1
		cmdID = g_cmdID

		#cmdset = CCmdSet("GotoID","REQUEST_MESSAGE",NAME,"RBCODE",0," ",0,0," ",cmdID)
		#cmdset.setInt('ID',ID)
		#test
		cmdset = CCmdSet("GotoDirEx","REQUEST_MESSAGE",NAME,"RBCODE",0," ",0,0," ",cmdID)
		cmdset.setInt('Direction',3)
		cmdset.setInt('Degree',270)
		s.send(cmdset.getCmdSet())
		
		#receive   
		waitFlag = SyncFlag
		while waitFlag and IsRunning[0] :
			for i in g_ResCmdSetList:
				if int(i.m_cmdID) == cmdID:
					waitFlag = False

					ArgList = i.getArgList()
					for idx in range(len(ArgList)):
						Return[ArgList[idx]] = cmdset.getValue(ArgList[idx])			
	
					g_ResCmdSetList.remove(i)
		#receive 
	else:
		ResultCode = "failure"
	
	IsRunning[0] = False
	

def GotoDirEx(IsRunning, Return, Direction, Degree, SyncFlag = False):
	ResultCode = 'failure'
	
	if Direction >0 and Direction < 5 :
		#to do goto id
		rospy.loginfo('Moving.......')
		global g_cmdID;
		g_cmdID +=1
		cmdID = g_cmdID

		cmdset = CCmdSet("GotoDirEx","REQUEST_MESSAGE",NAME,"RBCODE",0," ",0,0," ",cmdID)
		cmdset.setInt('Direction',Direction)
		cmdset.setInt('Degree',Degree)
		s.send(cmdset.getCmdSet())

		#receive   
		waitFlag = SyncFlag
		while waitFlag and IsRunning[0] :
			for i in g_ResCmdSetList:
				if int(i.m_cmdID) == cmdID:
					waitFlag = False			

					ArgList = i.getArgList()
					for idx in range(len(ArgList)):
						Return[ArgList[idx]] = cmdset.getValue(ArgList[idx])			
		
					g_ResCmdSetList.remove(i)
		ResultCode = "success"
		#receive

	else:
		ResultCode = "failure"
	
	IsRunning[0] = False	

def Stop(IsRunning,Return,  SyncFlag = False):
	ResultCode = 'failure'
	global g_cmdID;
	g_cmdID +=1
	cmdID = g_cmdID

	cmdset = CCmdSet("Stop","REQUEST_MESSAGE",NAME,"RBCODE",0," ",0,0," ",cmdID)
	s.send(cmdset.getCmdSet())
		
	#receive   
	waitFlag = SyncFlag
	while waitFlag and IsRunning[0] :
		for i in g_ResCmdSetList:
			if int(i.m_cmdID) == cmdID:
				waitFlag = False				

				ArgList = i.getArgList()
				for idx in range(len(ArgList)):
					Return[ArgList[idx]] = cmdset.getValue(ArgList[idx])			
	
				g_ResCmdSetList.remove(i)
	#receive 
	IsRunning[0] = False
	
#define PlayTTS
def PlayTTS(IsRunning, Return,  Text, SpeechType,SyncFlag = False):
	#Todo
	ResultCode = 'failure'
	nTextLength = len(Text)
	nSpeechType = int(SpeechType)
	
	if nTextLength <= 0:
		ResultCode = "failure"
		return 'failure'
	
	elif nSpeechType< 0 or nSpeechType> 10:
		ResultCode = "failure"
		
	else:
		#Todo plat tts
		TTSText = 'Text: '+Text
		rospy.loginfo(TTSText)
		global g_cmdID;
		g_cmdID +=1
		cmdID = g_cmdID

		cmdset = CCmdSet("PlayTTS","REQUEST_MESSAGE",NAME,"RBCODE",0,"",0,0,"",g_cmdID)
		cmdset.setString('Text',Text.encode('utf-8'))
		cmdset.setInt('SpeechType',SpeechType)
    		s.send(cmdset.getCmdSet())

		
		#receive   
		waitFlag = SyncFlag
		while waitFlag and IsRunning[0] :
			for i in g_ResCmdSetList:
				if int(i.m_cmdID) == cmdID:
					waitFlag = False		

					ArgList = i.getArgList()
					for idx in range(len(ArgList)):
						Return[ArgList[idx]] = cmdset.getValue(ArgList[idx])				
					
					g_ResCmdSetList.remove(i)
		#receive

		ResultCode = "success"

	IsRunning[0] = False

#define StartFaceRecognition
def StartFaceRecognition(IsRunning,  Return,  SyncFlag = False):
	ResultCode = 'failure'
	global g_cmdID;
	g_cmdID +=1
	cmdID = g_cmdID
	#cmdset = CCmdSet("StartFaceRecognition","REQUEST_MESSAGE",NAME,"RBCODE",0,"",0,0,"",g_cmdID)
	cmdset = CCmdSet("StartRecObject","REQUEST_MESSAGE",NAME,"RBCODE",0,"",0,0,"",g_cmdID)
	s.send(cmdset.getCmdSet())
	
	#receive   
	waitFlag = SyncFlag
	while waitFlag and IsRunning[0] :
		for i in g_ResCmdSetList:
			if int(i.m_cmdID) == cmdID:
				waitFlag = False					

				ArgList = i.getArgList()
				for idx in range(len(ArgList)):
					Return[ArgList[idx]] = cmdset.getValue(ArgList[idx])				

				g_ResCmdSetList.remove(i)
	#receive
	IsRunning[0] = False

#define StopFaceRecognition
def StopFaceRecognition(IsRunning, Return,  SyncFlag = False):
	ResultCode = 'failure'
	global g_cmdID;
	g_cmdID +=1
	cmdID = g_cmdID
	#cmdset = CCmdSet("StopFaceRecognition","REQUEST_MESSAGE",NAME,"RBCODE",0,"",0,0,"",g_cmdID)
	cmdset = CCmdSet("StopRecObject","REQUEST_MESSAGE",NAME,"RBCODE",0,"",0,0,"",g_cmdID)
	s.send(cmdset.getCmdSet())

	#receive   
	waitFlag = SyncFlag
	while waitFlag and IsRunning[0] :
		for i in g_ResCmdSetList:
			if int(i.m_cmdID) == cmdID:
				waitFlag = False					

				ArgList = i.getArgList()
				for idx in range(len(ArgList)):
					Return[ArgList[idx]] = cmdset.getValue(ArgList[idx])			

				g_ResCmdSetList.remove(i)
	#receive 
	IsRunning[0] = False


#define StopFaceRecognition
def SetRecObjectGroup(IsRunning,  Return, SyncFlag = False):
	ResultCode = 'failure'
	global g_cmdID;
	g_cmdID +=1
	cmdID = g_cmdID
	cmdset = CCmdSet("SetRecObjectGroup","REQUEST_MESSAGE",NAME,"RBCODE",0,"",0,0,"",g_cmdID)
	cmdset.setString('GroupID','birth')
	s.send(cmdset.getCmdSet())
	
	#receive   
	waitFlag = SyncFlag
	while waitFlag and IsRunning[0] :
		for i in g_ResCmdSetList:
			if int(i.m_cmdID) == cmdID:
				waitFlag = False					

				ArgList = i.getArgList()
				for idx in range(len(ArgList)):
					Return[ArgList[idx]] = cmdset.getValue(ArgList[idx])			

				g_ResCmdSetList.remove(i)
	#receive 
	IsRunning[0] = False


#######################################################################################################
##Main
####################################################################################################### 

# main
def main():
	print "============================Main start============================"
	Connect()
	ThreadRecv = threading.Thread(target=Recv, args=())
	ThreadRecv.start()

        import signal, time
       
	def handler(signum, f):
		print "KeyBoard Interrupt: ", signal.SIGINT
                global ThreadRecvFlag; ThreadRecvFlag= False
                signal.signal(signal.SIGINT, h)

	h = signal.signal(signal.SIGINT, handler)
	rospy.init_node('smach_example_state_machine')

	# Create a SMACH state machine
	
	sm_top = smach.Concurrence(outcomes=['end'], default_outcome = 'end',  outcome_map = {'end': 
																		{'VideoChatSrv':'end',
																		#'AlarmSrv':'end',
																		#'NavigationSrv':'end',
																		'TouchSrv':'end',
																		#'VoiceSrv':'end',
																		'RemoteSrv':'end'}})
																		#'ReactionSrv':'end'}})

	# Open the container
	with sm_top :
	# Add states to the container
		sm_VideoChatSrv = smach.StateMachine(outcomes=['end'])
		#sm_AlarmSrv = smach.StateMachine(outcomes=['end'])
		#sm_NavigationSrv = smach.StateMachine(outcomes=['end'])
		sm_TouchSrv = smach.StateMachine(outcomes=['end'])
		#sm_VoiceSrv = smach.StateMachine(outcomes=['end'])
		sm_RemoteSrv = smach.StateMachine(outcomes=['end'])
		#sm_ReactionSrv = smach.StateMachine(outcomes=['end'])


		#define Sub Service State
		with sm_VideoChatSrv:
			smach.StateMachine.add('VideoChatSrv_Init', VideoChatSrv_Init(), transitions={'success':'VideoChatSrv_Idle', 'failure':'end', 'retry':'VideoChatSrv_Init'})

			smach.StateMachine.add('VideoChatSrv_Wondering', VideoChatSrv_Wondering(), transitions={'success':'VideoChatSrv_FindUser', 'failure':'VideoChatSrv_Idle','retry':'VideoChatSrv_Wondering'})
			smach.StateMachine.add('VideoChatSrv_FindUser', VideoChatSrv_FindUser(), transitions={'success':'VideoChatSrv_VideoChat', 'failure':'VideoChatSrv_Idle','retry':'VideoChatSrv_Wondering'})
			smach.StateMachine.add('VideoChatSrv_VideoChat', VideoChatSrv_VideoChat(), transitions={'success':'VideoChatSrv_Idle', 'failure':'VideoChatSrv_Idle','retry':'VideoChatSrv_VideoChat'})
		
			smach.StateMachine.add('VideoChatSrv_Idle', VideoChatSrv_Idle(), transitions={'StartVideoChatSrv':'VideoChatSrv_Wondering', 'success':'VideoChatSrv_Idle', 'retry':'VideoChatSrv_Idle', 'failure':'VideoChatSrv_Init'})

		#with sm_AlarmSrv:
		#	smach.StateMachine.add('AlarmSrv_Init', AlarmSrv_Init(), transitions={'success':'AlarmSrv_Alarm', 'failure':'end', 'retry':'AlarmSrv_Init'})
		#	smach.StateMachine.add('AlarmSrv_Alarm', AlarmSrv_Alarm(), transitions={'success':'AlarmSrv_Init', 'failure':'end', 'retry':'AlarmSrv_Alarm'})
		  
		#with sm_NavigationSrv:
		#	smach.StateMachine.add('NavigationSrv_Init', NavigationSrv_Init(), transitions={'success':'NavigationSrv_Idle', 'failure':'end', 'retry':'NavigationSrv_Init'})
		#	smach.StateMachine.add('NavigationSrv_Idle', NavigationSrv_Idle(), transitions={'success':'NavigationSrv_Init', 'failure':'end', 'retry':'NavigationSrv_Idle'})
		
		with sm_TouchSrv:
			smach.StateMachine.add('TouchSrv_Init', TouchSrv_Init(), transitions={'success':'TouchSrv_Idle', 'failure':'end', 'retry':'TouchSrv_Init'})

			smach.StateMachine.add('TouchSrv_RightHand', TouchSrv_RightHand(), transitions={'success':'TouchSrv_Idle', 'failure':'TouchSrv_Idle', 'retry':'TouchSrv_RightHand'})
			smach.StateMachine.add('TouchSrv_LeftHand', TouchSrv_LeftHand(), transitions={'success':'TouchSrv_Idle', 'failure':'TouchSrv_Idle', 'retry':'TouchSrv_LeftHand'})
			smach.StateMachine.add('TouchSrv_RightHead', TouchSrv_RightHead(), transitions={'success':'TouchSrv_Idle', 'failure':'TouchSrv_Idle', 'retry':'TouchSrv_RightHead'})
			smach.StateMachine.add('TouchSrv_LeftHead', TouchSrv_LeftHead(), transitions={'success':'TouchSrv_Idle', 'failure':'TouchSrv_Idle', 'retry':'TouchSrv_LeftHead'})
			smach.StateMachine.add('TouchSrv_RightWheel', TouchSrv_RightWheel(), transitions={'success':'TouchSrv_Idle', 'failure':'TouchSrv_Idle', 'retry':'TouchSrv_RightWheel'})
			smach.StateMachine.add('TouchSrv_LeftWheel', TouchSrv_LeftWheel(), transitions={'success':'TouchSrv_Idle', 'failure':'TouchSrv_Idle', 'retry':'TouchSrv_LeftWheel'})
		
			smach.StateMachine.add('TouchSrv_Idle', TouchSrv_Idle(), transitions={'righthand':'TouchSrv_RightHand',
																'lefthand':'TouchSrv_LeftHand',
																'righthead':'TouchSrv_RightHead', 
																'lefthead':'TouchSrv_LeftHead', 
																'rightwheel':'TouchSrv_RightWheel', 
																'leftwheel':'TouchSrv_LeftWheel', 
																'failure':'end', 
																'retry':'TouchSrv_Init'})

		#with sm_VoiceSrv:
		#	smach.StateMachine.add('VoiceSrv_Init', VoiceSrv_Init(), transitions={'success':'VoiceSrv_Idle', 'failure':'end', 'retry':'VoiceSrv_Init'})
		#	smach.StateMachine.add('VoiceSrv_Idle', VoiceSrv_Idle(), transitions={'success':'VoiceSrv_Init', 'failure':'end', 'retry':'VoiceSrv_Idle'})
		
		with sm_RemoteSrv:
			smach.StateMachine.add('RemoteSrv_Init', RemoteSrv_Init(), transitions={'success':'RemoteSrv_Idle', 'failure':'end', 'retry':'RemoteSrv_Init'})
			
			smach.StateMachine.add('RemoteSrv_Forward', RemoteSrv_Forward(), transitions={'success':'RemoteSrv_Idle', 'failure':'RemoteSrv_Idle', 'retry':'RemoteSrv_Forward'})
			smach.StateMachine.add('RemoteSrv_Backward', RemoteSrv_Backward(), transitions={'success':'RemoteSrv_Idle', 'failure':'RemoteSrv_Idle', 'retry':'RemoteSrv_Backward'})
			smach.StateMachine.add('RemoteSrv_Rightturn', RemoteSrv_Rightturn(), transitions={'success':'RemoteSrv_Idle', 'failure':'RemoteSrv_Idle', 'retry':'RemoteSrv_Rightturn'})
			smach.StateMachine.add('RemoteSrv_Leftturn', RemoteSrv_Leftturn(), transitions={'success':'RemoteSrv_Idle', 'failure':'RemoteSrv_Idle', 'retry':'RemoteSrv_Leftturn'})
			smach.StateMachine.add('RemoteSrv_Stop', RemoteSrv_Stop(), transitions={'success':'RemoteSrv_Idle', 'failure':'RemoteSrv_Idle', 'retry':'RemoteSrv_Stop'})

			smach.StateMachine.add('RemoteSrv_Idle', RemoteSrv_Idle(), transitions={'forward':'RemoteSrv_Forward', 
																	'backward':'RemoteSrv_Backward',
																	 'rightturn':'RemoteSrv_Rightturn',
																	 'leftturn':'RemoteSrv_Leftturn',
																	 'stop':'RemoteSrv_Stop',
																	 'retry':'RemoteSrv_Idle',
																	 'failure':'RemoteSrv_Init'})
			
		#with sm_ReactionSrv:
		#	smach.StateMachine.add('ReactionSrv_Init', ReactionSrv_Init(), transitions={'success':'ReactionSrv_Idle', 'failure':'end', 'retry':'ReactionSrv_Init'})
		#	smach.StateMachine.add('ReactionSrv_Idle', ReactionSrv_Idle(), transitions={'success':'ReactionSrv_Init', 'failure':'end', 'retry':'ReactionSrv_Idle'})

		
		smach.Concurrence.add('VideoChatSrv', sm_VideoChatSrv)
		#smach.Concurrence.add('AlarmSrv', sm_AlarmSrv)
		#smach.Concurrence.add('NavigationSrv', sm_NavigationSrv)
		smach.Concurrence.add('TouchSrv', sm_TouchSrv )
		#smach.Concurrence.add('VoiceSrv', sm_VoiceSrv )
		smach.Concurrence.add('RemoteSrv', sm_RemoteSrv )
		#smach.Concurrence.add('ReactionSrv', sm_ReactionSrv )

	#sis = smach_ros.IntrospectionServer('sm_top', sm_top, '/SM_TOP')
	#sis.start()

	# Execute SMACH plan
	outcome = sm_top.execute()
	
	rospy.spin()
	#sis.stop()
	
	print "======================Main end================================="
	while True:
		pass

if __name__ == '__main__':
    main()

