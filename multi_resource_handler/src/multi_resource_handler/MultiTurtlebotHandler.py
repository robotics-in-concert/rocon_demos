
import rospy
import demo_msgs.msg as demo_msgs
from .turtle import *

class MultiTurtlebotHandler(object):

    def __init__(self):
        self.sub = {}
        self.sub['request_robot'] = rospy.Subscriber('/mrh/request_robot',demo_msgs.RequestRobot,self.process_request_robot)
        self.sub['request_goto'] = rospy.Subscriber('/mrh/request_goto',demo_msgs.RequestGoto,self.process_request_goto)
        self.sub['release_robot'] =rospy.Subscriber('/mrh/release_robot',demo_msgs.ReleaseRobot,self.process_release_robot)

        self.pub = {}
        self.pub['response_robot'] = rospy.Publisher('/mrh/response_robot',demo_msgs.ResponseRobot)
        self.pub['response_goto'] = rospy.Publisher('/mrh/response_goto',demo_msgs.ResponseGoto)

        self.turtle = {}
        self.turtle['adam'] = Turtle('adam',True)
        self.turtle['bach'] = Turtle('bach',False)
        self.turtle['chopin'] = Turtle('chopin',False)
        self.turtle['donizetti'] = Turtle('donizetti',True)

        self.task = {}

    def spin(self):
        rospy.spin()

    def process_request_robot(self,msg):
        self.log("Robot requested")

        for i,t in self.turtle.items():
            if t.status == False:
                t.set_task(msg.task_id)
                self.task[msg.task_id] = t
                self.pub['response_robot'].publish(demo_msgs.ResponseRobot(msg.task_id,True))
                self.log(str(t.name) + " is assigned for " + str(msg.task_id))
                return

        self.pub['response_robot'].publish(demo_msgs.ResponseRobot(msg.task_id,False))


    def process_request_goto(self,msg):
        self.task[msg.task_id].goto(msg.location)
        self.log("Robot has arrived to "+ str(msg.location))
        self.pub['response_goto'].publish(demo_msgs.ResponseGoto(msg.task_id,True))

    def process_release_robot(self,msg):
        self.task[msg.task_id].release()
        self.task[msg.task_id] = None

    def log(self,msg):
        rospy.loginfo("Multi Handler : " + str(msg))
