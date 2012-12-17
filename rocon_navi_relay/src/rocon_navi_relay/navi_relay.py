#!/usr/bin/env python
#
# License: BSD
#   https://raw.github.com/robotics-in-concert/rocon_demo/rocon_navi_relay/LICENSE
#
##############################################################################
# Imports
##############################################################################

import threading
import roslib
roslib.load_manifest('rocon_navi_relay')
import rospy
import actionlib
#import tf
#from geometry_msgs.msg import Twist
#from std_msgs.msg import String
import geometry_msgs.msg as geometry_msgs
import demo_msgs.msg as demo_msgs
import move_base_msgs.msg as move_base_msgs

##############################################################################
# NaviRelay
##############################################################################


class Job(threading.Thread):

    def __init__(self, action_client, result_publisher, task_id, pose, current_task_id):
        threading.Thread.__init__(self)
        self._current_task_id = task_id
        self._result_publisher = result_publisher
        self._action_client = action_client
        self._response = demo_msgs.ResponseMoveRobot()
        self._response.task_id = task_id
        self._response.status = False
        rospy.loginfo("Sending robot to [%s,%s]" % (pose.position.x, pose.position.y))
        goal = move_base_msgs.MoveBaseGoal()
        goal.target_pose.header.frame_id = '/map'
        goal.target_pose.header.stamp = rospy.Time.now()
        goal.target_pose.pose = pose
        self._action_client.send_goal(goal)

    def run(self):
        self._action_client.wait_for_result()
        unused_result = self._action_client.get_result()  # use this result
        self._response.status = True
        self._result_publisher.publish(self._response)
        self._current_task_id = None


class NaviRelay(object):
    def __init__(self):
        self._current_task_id = None
        self.subscribers = {}
        self.subscribers['command'] = rospy.Subscriber('command', demo_msgs.RequestMoveRobot, self._process_command)
        self.publishers = {}
        self.publishers['result'] = rospy.Publisher('result', demo_msgs.ResponseMoveRobot)
        self.actionclient = {}
        self.actionclient['move_base'] = actionlib.SimpleActionClient('move_base', move_base_msgs.MoveBaseAction)
        self.actionclient['move_base'].wait_for_server()
        self._initialise_navigation

    def _initialise_navigation(self):
        initial_x = rospy.get_param('~initial_x', 0.0)
        initial_y = rospy.get_param('~initial_y', 0.0)
        initial_a = rospy.get_param('~initial_a', 0.0)
        pwcs = geometry_msgs.PoseWithCovarianceStamped()
        pwcs.pose.pose.position.x = initial_x
        pwcs.pose.pose.position.y = initial_y
        #pwcs.pose.pose.quaternion = tf.transformations
        #initialpose_publisher = rospy.Publisher('/initialpose', demo_msgs.ResponseMoveRobot)
        #while initialpose_publisher.get_num_connections() == 0:
        #    rospy.sleep(1.0)
        #initialpose_publisher.publish(pwcs)

    def spin(self):
        rospy.spin()

    def _process_command(self, msg):
        if self._current_task_id is not None:
            result = demo_msgs.ResponseMoveRobot()
            result.task_id = msg.task_id
            result.status = False
            self.publishers['result'].publish(result)
        else:
            job = Job(self.actionclient['move_base'], self.publishers['result'], msg.task_id, msg.pose, self._current_task_id)
            job.start()

    def log(self, msg):
        #self.pub['status'].publish(msg)
        rospy.loginfo("NaviRelay : " + str(msg))
