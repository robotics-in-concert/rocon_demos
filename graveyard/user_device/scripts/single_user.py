#!/usr/bin/env python
import rospy
import std_msgs

import threading
import random

import actionlib
from cafe_msgs.msg import *
from std_srvs.srv import *

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
    rospy.loginfo( "done_cb: status : " + str(status) + " result: " + str(result))
    pass
    
def active_cb():
    rospy.loginfo("active_cb: ")
    pass
    
def feedback_cb(data):
    rospy.loginfo("feedback_cb: %s",str(data.status))
    pass
    

class FakeUser(object):

    def __init__(self,name):
        self.name = name
        self.action_client = actionlib.SimpleActionClient('send_order',UserOrderAction)
        self.add_ordersrv = rospy.Service('add_order',Empty,self.add_order)

    def spin(self):
        rospy.loginfo("Waiting for Task Coordinator")
        self.action_client.wait_for_server()
        rospy.loginfo("Server Ready!")

        order = self.create_order()
        self.send_order(order)

        rospy.spin()

    def add_order(self,req):
        order = self.create_order()       
        self.send_order(order)            

        return EmptyResponse()
    
    def create_order(self):
        new_order = Order()

        new_order.table_id = random.randrange(1,9)
        new_order.menus = generateMenus()
        new_order.robot_name = ""                
        new_order.status = Status.IDLE
        
        return new_order

    def send_order(self,order):

        goal = UserOrderGoal(order=order)
        self.action_client.send_goal(goal,done_cb,active_cb,feedback_cb)


    
if __name__ == '__main__':
    
    try:
        rospy.init_node('user_deivce')

        user = FakeUser(rospy.get_name())
        rospy.loginfo('Initialized')
        user.spin()
        rospy.loginfo('Bye Bye')
       
    except rospy.ROSInterruptException:
        pass                                  
