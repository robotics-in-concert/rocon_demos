#!/usr/bin/env python

import rospy
import actionlib
from rocon_demo_msgs.msg import Notice
import std_msgs.msg as std_msgs
from naoqi_msgs.msg import BodyPoseAction, BodyPoseGoal

class NaoNoticer(object):

    def __init__(self):

        self._pub = {}
        self._pub['speech'] = rospy.Publisher('/speech', std_msgs.String)

        self._pose_client = actionlib.SimpleActionClient("/body_pose", BodyPoseAction)
        if not self._pose_client.wait_for_server(rospy.Duration(3.0)):
            rospy.logfatal("Could not connect to required \"body_pose\" action server, is the pose_manager node running?");
            rospy.signal_shutdown();

        self._pose_table = {}
        self._pose_table[Notice.INFO] = "init"
        self._pose_table[Notice.WARN] = "hello"
        self._pose_table[Notice.ERROR] = "crouch"

        self._sub_notice = rospy.Subscriber('/notice', Notice, self._process_notice)

    def _process_notice(self, msg):
        self._pub['speech'].publish(msg.message)    

        if msg.level == Notice.ERROR:
            goal = BodyPoseGoal()
            goal.pose_name = "crouch"
            self._pose_client.send_goal_and_wait(goal)
            goal.pose_name = "init"
            self._pose_client.send_goal_and_wait(goal)
        else:
            goal = BodyPoseGoal()
            goal.pose_name = self._pose_table[msg.level]
            self._pose_client.send_goal_and_wait(goal)
    
    def loginfo(self, msg):
        rospy.loginfo("%s : %s"%(rospy.get_name(), str(msg)))

    def spin(self):
        rospy.spin()

if __name__ == '__main__':
    rospy.init_node('notice_nao')
    nn = NaoNoticer() 
    nn.loginfo("Initialised")
    nn.spin()
    nn.loginfo("Bye Bye")
