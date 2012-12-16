#!/usr/bin/env python       
import roslib; roslib.load_manifest('multi_resource_handler')
import rospy
from multi_resource_handler.MultiTurtlebotHandler import *

if __name__ == '__main__':

    rospy.init_node('multi_turtlebot_handler')
    mrh = MultiTurtlebotHandler()
    rospy.loginfo("Initialized")
    mrh.spin()
    rospy.loginfo("Done")
