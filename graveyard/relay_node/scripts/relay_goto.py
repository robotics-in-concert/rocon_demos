#!/usr/bin/env python       
import roslib; roslib.load_manifest('relay_node')
import rospy
from demo_msgs.msg import *

def callback(data): 
    pub.publish(data)	

if __name__ == '__main__': 
    rospy.init_node('relay') 
    pub = rospy.Publisher('out', Goto) 
    sub = rospy.Subscriber('in', Goto, callback) 
    rospy.spin() 
