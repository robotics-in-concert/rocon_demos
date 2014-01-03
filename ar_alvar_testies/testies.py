#!/usr/bin/env python
#       
# License: BSD
#   https://raw.github.com/robotics-in-concert/rocon_multimaster/master/rocon_gateway/LICENSE 
#

##############################################################################
# Imports
##############################################################################

import math
import rospy
import rocon_utilities.console as console
import visualization_msgs.msg as visualization_msgs

# Can't turn it much - different error params?
# Sometimes jumps x-values near the edges -> due to bad z calculations on the fringe (out by 50cm!)
  # should be able to easily filter these out
# a and b disappear near the edges, but I still get readings

##############################################################################
# Functions
##############################################################################

class Marker:
    def __init__(self, id, x, y, z):
        self.id = id
        self.update(x, y, z)
    
    def update(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
        self.distance = x*x + z*z

global left_marker, right_marker
global baseline

baseline = 0.26
left_marker = Marker(id=3, x=0, y=0, z=0)
right_marker = Marker(id=0, x=0, y=0, z=0)

def print_pythags_results(left_marker, right_marker):
    global baseline
    b = baseline/2 + (left_marker.distance*left_marker.distance - right_marker.distance*right_marker.distance)/(2*baseline)
    try:
        a = math.sqrt(left_marker.distance*left_marker.distance - b*b)
    except ValueError:
        print("Value error: %s, %s" % (left_marker.distance, b))
        return  # left_marker not initialised fully yet, so negative sqrt
    print(console.cyan + "           a" + console.reset + " : " + console.yellow + "%s" % a + console.reset)
    print(console.cyan + "           b" + console.reset + " : " + console.yellow + "%s" % b + console.reset)

def print_pose_results(left_marker, right_marker):
    # angle between the robot and the first marker
    alpha = math.atan2(left_marker.x, left_marker.z)
    alpha_degrees = alpha*180.0/math.pi
    # alpha + beta is angle between the robot and the second marker 
    beta = math.atan2(right_marker.x, right_marker.z)
    beta_degrees = beta*180.0/math.pi
    # theta is the angle between the wall and the perpendicular in front of the robot
    theta = math.atan2((left_marker.z - right_marker.z), (right_marker.x - left_marker.x))
    theta_degrees = theta*180.0/math.pi

    print(console.cyan + "       alpha" + console.reset + " : " + console.yellow + "%s" % alpha_degrees + " degrees" + console.reset)
    print(console.cyan + "        beta" + console.reset + " : " + console.yellow + "%s" % beta_degrees + " degrees" + console.reset)
    print(console.cyan + "       theta" + console.reset + " : " + console.yellow + "%s" % theta_degrees + " degrees" + console.reset)
    
    # M1 = (left_marker.x, left_marker.z)
    # M2 = (right_marker.x, right_marker.z)
    # M3 = M1 + (M2 - M1)/2   # midpoint of M1, M2
    # Target stop position relative to marker mid point (40cm perpendicularly out)
    # M4 = (-0.4*sin(theta), -0.4*cos(theta))
    # Target stop position
    # M5 = M3 + M4
    target_x = left_marker.x + (right_marker.x - left_marker.x)/2 - 0.4*math.sin(theta)
    target_z = left_marker.z + (right_marker.z - left_marker.z)/2 - 0.4*math.cos(theta)
    target_heading = math.atan2(target_x, target_z)
    target_heading_degrees = target_heading*180.0/math.pi
    
    print(console.cyan + "      target" + console.reset + " : " + console.yellow + "(x=%s, z=%s, heading=%s)" % (target_x, target_z, target_heading_degrees) + console.reset)

def callback(data):
    global left_marker, right_marker
    if data.id == 0:
        right_marker.update(data.pose.position.x, data.pose.position.y, data.pose.position.z)
    else:
        left_marker.update(data.pose.position.x, data.pose.position.y, data.pose.position.z)
    print(console.cyan + "l: [x, y, z]" + console.reset + " : " + console.yellow + "[%s, %s, %s]" % (left_marker.x, left_marker.y, left_marker.z) + console.reset)
    print(console.cyan + "l: d" + console.reset + "         : " + console.yellow + "%s" % left_marker.distance + console.reset)
    print(console.cyan + "r: [x, y, z]" + console.reset + " : " + console.yellow + "[%s, %s, %s]" % (right_marker.x, right_marker.y, right_marker.z) + console.reset)
    print(console.cyan + "r: d" + console.reset + "         : " + console.yellow + "%s" % right_marker.distance + console.reset)
    print_pythags_results(left_marker, right_marker)
    print_pose_results(left_marker, right_marker)

##############################################################################
# Main
##############################################################################

if __name__ == '__main__':
    #visualization_msgs/Marker
    rospy.init_node('roles_and_apps')
    subscriber = rospy.Subscriber('/visualization_marker', visualization_msgs.Marker, callback)
    rospy.spin()