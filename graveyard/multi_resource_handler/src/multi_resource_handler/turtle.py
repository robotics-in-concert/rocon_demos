
import roslib; roslib.load_manifest('multi_resource_handler')
import rospy
from demo_msgs.msg import *
from geometry_msgs.msg import Twist

class Turtle(object):

    def __init__(self,name,status):
        self.name = name
        self.status = status
        self.wait = False

        self.pub = {}
        self.pub['request_move_turtle'] = rospy.Publisher(self.name+'/request_move',RequestMoveRobot)

        self.sub = {}
        self.sub['response_move_turtle'] = rospy.Subscriber(self.name + '/response_move',ResponseMoveRobot,self.process_response_move_robot)


    def set_task(self,id):
        self.task_id = id
        self.status = True

    def goto(self,loc):
        rmr = RequestMoveRobot()
        rmr.task_id = self.task_id
        rmr.pose.position.x = loc[0]
        rmr.pose.position.y = loc[1]
        rmr.pose.position.z = 0 
        rmr.pose.orientation.x = 0
        rmr.pose.orientation.y = 0
        rmr.pose.orientation.z = 0
        rmr.pose.orientation.w = 1
        
        self.pub['request_move_turtle'].publish(rmr)

        self.wait = True
        while not rospy.is_shutdown() and self.wait == True:
            rospy.sleep(0.2)

    def process_response_move_robot(self,msg):
        self.wait = False

    def release(self):
        self.task_id = None
        self.status = False
