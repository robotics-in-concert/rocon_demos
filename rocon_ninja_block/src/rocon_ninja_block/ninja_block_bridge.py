#!/usr/bin/env python
#
# License: BSD
#   https://raw.github.com/robotics-in-concert/rocon_devices/license/LICENSE
#
#################################################################################
# sys
import threading
import socket
import sys
import time
import json
import uuid
import urllib

if sys.version_info[0] > 2:
    PY3K = True
else:
    PY3K = False
if PY3K:
    import http.client as httplib
else:
    import httplib

# web server
from flask import Flask
from flask import request

# ros
import rospy
import actionlib
from std_msgs.msg import String
from rocon_ninja_block.msg import *
from rocon_ninja_block.srv import *


class NinjaBlockBridge(Flask):

    def __init__(self, host="127.0.0.1", port=5555, public_key="", callback_url_host="127.0.0.1", callback_url_port=5555):
        self.app = Flask(__name__)

        self.host = host
        self.port = int(port)

        self.nb_cloud_host = 'api.ninja.is'
        self.public_key = public_key

        self.callback_url_host = callback_url_host
        self.callback_url_port = int(callback_url_port)
        self.callback_url = 'http://' + callback_url_host + ':' + str(self.callback_url_port)

        self.devices = {}
        self.publisher = {}
        self.subscriber = {}
        self.service = {}

        self.init_flask()
        self.init_ros()

    def start(self):
        self.server_thr = threading.Thread(target=self.app.run, kwargs={'host': self.host, 'port': self.port, 'debug': False})
        self.server_thr.start()
        self.loginfo('flask server start')
        self.init_device_list_info()
        self.device_list_as.start()
        while not rospy.is_shutdown():
            rospy.sleep(0.1)
        (result, e) = self.shutdown_server()
        self.loginfo(e)
        if result:
            self.server_thr.join(1)
        else:
            sys.exit()

    def init_ros(self):
        # ros node start
        self.device_list_as = actionlib.SimpleActionServer('get_device_list', GetDeviceListAction, execute_cb=self.get_device_list, auto_start=False)

        self.service['get_device_list'] = rospy.Service('get_device_list', GetNBDeviceList, self.get_device_list)

        self.publisher["ninja_block_data"] = rospy.Publisher("ninja_block_data", NBDevice, queue_size=10)

        self.subscriber["register_callback_url"] = rospy.Subscriber("register_callback_url", String, self.register_callback_url)
        self.subscriber["delete_callback_url"] = rospy.Subscriber("delete_callback_url", String, self.delete_callback_url)
        self.subscriber["get_callback_url"] = rospy.Subscriber("get_callback_url", String, self.get_callback_url)

    def init_flask(self):
        self.app.add_url_rule(rule='/index', view_func=self.index)
        self.app.add_url_rule(rule='/shutdown', view_func=self.shutdown)
        self.app.add_url_rule(rule='/device/<device_guid>', view_func=self.device, methods=['POST'])

    def index(self):
        return "This is index"

    def shutdown(self, methods=['GET']):
        self.loginfo('request shutdown')
        func = request.environ.get('werkzeug.server.shutdown')
        if func is None:
            raise RuntimeError('Not running with the Werkzeug Server')
        func()
        return "shutdown server"

    def home(self):
        return "Hello, World!"

    def callname(self, name):
        return 'call %s' % name

    def device(self, device_guid):
        for device in self.devices.device_list:
            if device.guid == device_guid:
                if device.subid:
                    if device.subid == request.json['DA']:
                        device.data = 'on'
                        device.time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
                        self.publisher["ninja_block_data"].publish(device)
                else:
                    device.data = str(request.json['DA'])
                    device.time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
                    self.publisher["ninja_block_data"].publish(device)
        return 'hello world'

    def init_device_list_info(self):
        (result, result_data) = self.https_request(mode='GET', address='/rest/v0/devices', kwargs={'user_access_token': self.public_key})
        nb_device_list = NBDeviceList()
        if result and 'data' in result_data.keys():
            devices = result_data['data']
            for device in devices.keys():
                if devices[device]['has_subdevice_count']:
                    for sub_device in devices[device]['subDevices'].keys():
                        nb_device = NBDevice()
                        nb_device.name = str(devices[device]['subDevices'][sub_device]['shortName'])
                        nb_device.type = NBDevice.RF233
                        nb_device.guid = str(device)
                        nb_device.subid = str(devices[device]['subDevices'][sub_device]['data'])
                        nb_device_list.device_list.append(nb_device)
                else:
                    nb_device = NBDevice()
                    nb_device.name = str(devices[device]['shortName'])
                    #nb_device.type = NBDevice.MAIN_DEVICE
                    nb_device.guid = str(device)
                    nb_device_list.device_list.append(nb_device)
        self.devices = nb_device_list

    def get_device_list(self, msg):
        (result, result_data) = self.https_request(mode='GET', address='/rest/v0/devices', kwargs={'user_access_token': self.public_key})
        nb_device_list = NBDeviceList()
        if result and 'data' in result_data.keys():
            print result
            devices = result_data['data']
            for device in devices.keys():
                if devices[device]['has_subdevice_count']:
                    for sub_device in devices[device]['subDevices'].keys():
                        nb_device = NBDevice()
                        nb_device.name = str(devices[device]['subDevices'][sub_device]['shortName'])
                        nb_device.type = NBDevice.RF233
                        nb_device.guid = str(device)
                        nb_device.subid = str(devices[device]['subDevices'][sub_device]['data'])
                        nb_device_list.device_list.append(nb_device)
                else:
                    nb_device = NBDevice()
                    nb_device.name = str(devices[device]['shortName'])
                    #nb_device.type = NBDevice.MAIN_DEVICE
                    nb_device.guid = str(device)
                    nb_device_list.device_list.append(nb_device)
        self.devices = nb_device_list

        result = GetDeviceListResult(True, nb_device_list)
        self.device_list_as.set_succeeded(result)

        return nb_device_list

    def register_callback_url(self, msg):
        device_guid = msg.data
        address = '/rest/v0/device/' + device_guid + '/callback'
        callback_url = self.callback_url + '/device/' + device_guid
        data = '{ "url" : "' + callback_url + '" }'
        headers = {'Content-Type': 'application/json', "Accept": "text/plain"}
        (result, result_data) = self.https_request(mode='POST',
                                                   data=data,
                                                   address=address,
                                                   kwargs={'user_access_token': self.public_key},
                                                   headers=headers)
        self.loginfo(result, result_data)

    def delete_callback_url(self, msg):
        device_guid = msg.data
        address = '/rest/v0/device/' + device_guid + '/callback'
        (result, result_data) = self.https_request(mode='DELETE', address=address, kwargs={'user_access_token': self.public_key})
        self.loginfo(result_data)

    def get_callback_url(self, msg):
        device_guid = msg.data
        address = '/rest/v0/device/' + device_guid + '/callback'
        (result, result_data) = self.https_request(mode='GET', address=address, kwargs={'user_access_token': self.public_key})
        self.loginfo(result_data)

    def loginfo(self, msg):
        rospy.loginfo("[Rocon NinjaBlock] " + msg)

    def https_request(self, mode='GET', address=None, data=None, headers={}, kwargs={}):
        """ Utility function for HTTPS GET/PUT requests for the API"""
        try:
            address_with_arg = address
            if kwargs and type(kwargs) is dict:
                arguments = urllib.urlencode(kwargs)
                address_with_arg += '?' + arguments
            connection = httplib.HTTPSConnection(self.nb_cloud_host)
            if mode == 'GET' or mode == 'DELETE':
                connection.request(mode, address_with_arg)
            if mode == 'PUT' or mode == 'POST':
                connection.request(mode, address_with_arg, data, headers)
            response = connection.getresponse()
            response_status = response.status
            if response_status == httplib.OK:
                result_data = response.read()
                if PY3K:
                    result = json.loads(str(result_data, encoding='utf-8'))
                else:
                    result = json.loads(result_data)
                return (True, result)
            else:
                return (False, None)
            connection.close()

        except socket.timeout, e:
            # time out error
            message = "Socket Timeout Error :%s" % str(e)
            return (False, message)
        except Exception, e:
            message = "Exception Error :%s" % str(e)
            return (False, message)

    def shutdown_server(self):
        try:
            address = 'http://' + self.host + ':' + str(self.port) + '/shutdown'
            connection = httplib.HTTPConnection(self.host + ':' + str(self.port))
            connection.request('GET', address)
            result = connection.getresponse()
            connection.close()
        except Exception, e:
            return (False, e)
        else:
            return (True, 'server shutdown success!!')
