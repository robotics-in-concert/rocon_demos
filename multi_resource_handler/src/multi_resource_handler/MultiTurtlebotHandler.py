
import roslib; roslib.load_manifest('multi_resource_handler')
import rospy
from demo_msgs.msg import *
from .turtle import *

class MultiTurtlebotHandler(object):

    def __init__(self):
        self.sub = {}
        self.sub['request_robot'] = rospy.Subscriber('/mrh/request_robot',RequestRobot,self.process_request_robot)
        self.sub['request_goto'] = rospy.Subscriber('/mrh/request_goto',RequestGoto,self.process_request_goto)
        self.sub['release_robot'] =rospy.Subscriber('/mrh/release_robot',ReleaseRobot,self.process_release_robot)

        self.pub = {}
        self.pub['response_robot'] = rospy.Publisher('/mrh/response_robot',ResponseRobot)
        self.pub['response_goto'] = rospy.Publisher('/mrh/response_goto',ResponseGoto)

        self.turtle = {}
#        self.turtle['adam'] = Turtle('turtle1',False)
        self.turtle['bach'] = Turtle('turtle1',False)
        self.turtle['chopin'] = Turtle('turtle2',False)

        self.task = {}

        self.location = {}
        self.location['station'] = rospy.get_param('~station',[0, 0]) 
        self.location['kitchen'] = rospy.get_param('~kitchen',[-1.1724, 2.3408]) 
        self.location['customer1'] = rospy.get_param('~customer1',[-3.60909,-0.09575])
        self.location['customer2'] = rospy.get_param('~customer2',[-2.9145,1.6521])

    def spin(self):
        rospy.spin()

    def process_request_robot(self,msg):
        self.log("Robot requested")

        for i,t in self.turtle.items():
            if t.status == False:
                t.set_task(msg.task_id)
                self.task[msg.task_id] = t
                self.pub['response_robot'].publish(ResponseRobot(msg.task_id,True))
                self.log(str(t.name) + " is assigned for " + str(msg.task_id))
                return

        self.pub['response_robot'].publish(ResponseRobot(msg.task_id,False))


    def process_request_goto(self,msg):

        location = None
        if msg.location not in self.location:
            location = self.location['customer1']
        else:
            location = self.location[msg.location]
        self.log("Request move the robot to " + str(location))
            
        self.task[msg.task_id].goto(location)

        self.log("Robot has arrived to "+ str(msg.location))
        self.pub['response_goto'].publish(ResponseGoto(msg.task_id,True))

    def process_release_robot(self,msg):
        self.task[msg.task_id].release()
        self.task[msg.task_id] = None

    def process_response_move_robot(self,msg):
        self.task[msg.task_id].process_response_move_robot(msg)

    def log(self,msg):
        rospy.loginfo("Multi Handler : " + str(msg))
