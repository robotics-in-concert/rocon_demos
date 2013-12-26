#!/usr/bin/env python
# -*- coding:utf-8 -*-
#############################################
class CCmdSet():
  
    from xml.dom.minidom import Document
   
    #member var
    #header
    m_ver = "1.11.0000"
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
    doc = None

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
        pTag = self.doc.getElementsByTagName('param')
        for k in pTag:
            if Name == k.getElementsByTagName('name')[0].firstChild.nodeValue:
                k.getElementsByTagName('value')[0].firstChild.nodeValue = Value
                
                for l in self.m_params:
                    if l['name'] == Name:
                        l['value'] = str(Value)
                return

        params = self.doc.getElementsByTagName('params')[0]    

        paramTag = self.doc.createElement("param")
        params.appendChild(paramTag)

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
        

        param = {}
        param['name'] = Name
        param['type'] = "int"
        param['value'] = str(Value)
        self.m_params.append(param)
        

    def setBool(self,Name,Value):
        pTag = self.doc.getElementsByTagName('param')
        for k in pTag:
            if Name == k.getElementsByTagName('name')[0].firstChild.nodeValue:
                k.getElementsByTagName('value')[0].firstChild.nodeValue = Value
                for l in self.m_params:
                    if l['name'] == Name:
                        l['value'] = str(Value)
                return

        params = self.doc.getElementsByTagName('params')[0]    

        paramTag = self.doc.createElement("param")
        params.appendChild(paramTag)

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
        

        param = {}
        param['name'] = Name
        param['type'] = "bool"
        param['value'] = str(Value)
        self.m_params.append(param)
        


    def setString(self,Name,Value):
        pTag = self.doc.getElementsByTagName('param')
        for k in pTag:
            if Name == k.getElementsByTagName('name')[0].firstChild.nodeValue:
                k.getElementsByTagName('value')[0].firstChild.nodeValue = Value
                for l in self.m_params:
                    if l['name'] == Name:
                        l['value'] = str(Value)
                
                return

        params = self.doc.getElementsByTagName('params')[0]    

        paramTag = self.doc.createElement("param")
        params.appendChild(paramTag)

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
        

        param = {}
        param['name'] = Name
        param['type'] = "string"
        param['value'] = str(Value)
        self.m_params.append(param)
        

    def setUInt(self,Name,Value):
        pTag = self.doc.getElementsByTagName('param')
        for k in pTag:
            if Name == k.getElementsByTagName('name')[0].firstChild.nodeValue:
                k.getElementsByTagName('value')[0].firstChild.nodeValue = Value
                for l in self.m_params:
                    if l['name'] == Name:
                        l['value'] = str(Value)
                
                return

        params = self.doc.getElementsByTagName('params')[0]    

        paramTag = self.doc.createElement("param")
        params.appendChild(paramTag)

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
        

        param = {}
        param['name'] = Name
        param['type'] = "unsigned int"
        param['value'] = str(Value)
        self.m_params.append(param)
        

    def setFloat(self,Name,Value):
        

        pTag = self.doc.getElementsByTagName('param')
        for k in pTag:
            if Name == k.getElementsByTagName('name')[0].firstChild.nodeValue:
                k.getElementsByTagName('value')[0].firstChild.nodeValue = Value
                for l in self.m_params:
                    if l['name'] == Name:
                        l['value'] = str(Value)
                return

        params = self.doc.getElementsByTagName('params')[0]    

        paramTag = self.doc.createElement("param")
        params.appendChild(paramTag)

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

        param = {}
        param['name'] = Name
        param['type'] = "float"
        param['value'] = str(Value)
        self.m_params.append(param)
        
        
        
    def printCmdSet(self):
        print self.doc.toprettyxml(indent="  ",encoding="euc-kr")

    def getCmdSet(self):
    	return self.doc.toxml(encoding="euc-kr")
        #print self.doc.toprettyxml(indent="  ",encoding="euc-kr")
        #DataLength = len(self.doc.toxml(encoding="euc-kr"))
        #buffer = struct.pack('I I I %ds'%DataLength, DISCRIMINATOR, VERSION, DataLength,self.doc.toxml())
        #return buffer

    def parse(self,data):
        from xml.dom.minidom import parseString
        #doc = self.doc
        s = unicode(data,'euc-kr').encode('utf-8')  # euc-kr -> utf-8 
        s = s.replace("encoding=\"euc-kr\"", r"")
 
        self.doc = parseString(s)
        
        headerTag = self.doc.getElementsByTagName('header')[0]
        if headerTag.childNodes.length == 11:

            i=0
            while i < headerTag.childNodes.length:
  
                NodeName = headerTag.childNodes[i].nodeName
                if headerTag.childNodes[i].firstChild != None:
                        NodeValue = headerTag.childNodes[i].firstChild.nodeValue
                else:
                        NodeValue = None

                if NodeName == "ver":
                        self.m_ver = NodeValue
                        self.setHeaderParam("ver",NodeValue)
                elif NodeName == "cmdname":
                        self.m_cmdname = NodeValue
                        self.setHeaderParam("cmdname",NodeValue)
                elif NodeName == "msgtype":
                        self.m_msgtype = NodeValue
                        self.setHeaderParam("msgtype",NodeValue)
                elif NodeName == "senderID":
                        self.m_senderID = NodeValue
                        self.setHeaderParam("senderID",NodeValue)
                elif NodeName == "receiverID":
                        self.m_receiverID = NodeValue
                        self.setHeaderParam("receiverID",NodeValue)
                elif NodeName == "usertag":
                       self.m_usertag = (NodeValue )
                       self.setHeaderParam("usertag",NodeValue)
                elif NodeName == "status":
                        self.m_status = (NodeValue )
                        self.setHeaderParam("status",NodeValue)
                elif NodeName == "timeout":
                        self.m_timeout = (NodeValue )
                        self.setHeaderParam("timeout",NodeValue)
                elif NodeName == "contentID":
                        self.m_contentID = NodeValue
                        self.setHeaderParam("contentID",NodeValue)
                elif NodeName == "cmdID":
                        self.m_cmdID = (NodeValue )
                        self.setHeaderParam("cmdID",NodeValue)
                else:
                        pass
                i+=1

        bodyTag = self.doc.getElementsByTagName('body')[0]


        if bodyTag.childNodes.length > 0:
			paramList = bodyTag.getElementsByTagName('param')
			if paramList.length > 0:
				i=0
				while i < paramList.length:
					nameTag = paramList[i].getElementsByTagName('name')
					typeTag = paramList[i].getElementsByTagName('type')
					valueTag = paramList[i].getElementsByTagName('value')

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

					if len(self.m_params) == 0:
						self.m_params.append(param)
					else:
						k = 0
						appendFlag = False
						while k < (len(self.m_params)):
							if self.m_params[k]['name'] == param['name']:
								self.m_params[k]['type'] = param['type']
								self.m_params[k]['value'] = param['value']
								break;
							k+=1
						if k == len(self.m_params):  
							self.m_params.append(param)
					i+=1

    def setHeaderParam(self,param, value):

                if param == "ver":
                        self.m_ver = value
                elif param == "cmdname":
                        self.m_cmdname = value
                elif param == "msgtype":
                        self.m_msgtype = value
                elif param == "senderID":
                        self.m_senderID = value
                elif param == "receiverID":
                        self.m_receiverID = value
                elif param == "usertag":
                        self.m_usertag = value 
                elif param == "status":
                        self.m_status = value
                elif param == "timeout":
                        self.m_timeout = value
                elif param == "contentID":
                        self.m_contentID = value
                elif param == "cmdID":
                        self.m_cmdID = value
                else:
                        pass

		pTag = self.doc.getElementsByTagName(param)[0]
                if value != None:
                    pTag.firstChild.replaceWholeText(value)
		
    def setCmdName(self,value):
		self.m_cmdname=value
		pTag = self.doc.getElementsByTagName('cmdname')[0]
		pTag.firstChild.replaceWholeText(value)

    def setSenderID(self,value):
		self.m_senderID=value
		pTag = self.doc.getElementsByTagName('senderID')[0]
		pTag.firstChild.replaceWholeText(value)

    def setReceiverID(self,value):
		self.m_receiverID=value
		pTag = self.doc.getElementsByTagName('receiverID')[0]
		pTag.firstChild.replaceWholeText(value)

    def setMsgType(self,value):
		self.m_msgtype=value
		pTag = self.doc.getElementsByTagName('msgtype')[0]
		pTag.firstChild.replaceWholeText(value)
         
    def getValue(self,name):
                #self.parse(self.getCmdSet())
		Value = None
		for i in self.m_params:
			if i['name'] == name:
				if i['type'] == 'int':
					Value = int(i['value'])

				elif i['type'] == 'bool':
					Value = bool(i['value'])

				elif i['type'] == 'float':
					Value = float(i['value'])

				elif i['type'] == 'str':
					Value = str(i['value'])

				elif i['type'] == 'unsigned int':
					Value = int(i['value'])
				else:					
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

    def copyCmdset(self):
                data = self.getCmdSet()
                cmdset = CCmdSet()
                params = []
                cmdset.m_params = params
                cmdset.parse(data)
                return cmdset 

