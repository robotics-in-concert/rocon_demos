
import rospy
import demo_msgs.msg as demo_msgs
from std_msgs.msg import String
from .order_handler import *


class Kitchen(object):
    
    def __init__(self):
        self.task = {}
        self.task_id = 0

        self.pub = {}
        self.pub['status'] = rospy.Publisher('~status',String)
        self.pub['request_robot'] = rospy.Publisher('/mrh/request_robot',demo_msgs.RequestRobot)
        self.pub['request_goto'] = rospy.Publisher('/mrh/request_goto',demo_msgs.RequestGoto)
        self.pub['release_robot'] = rospy.Publisher('/mrh/release_robot',demo_msgs.ReleaseRobot)

        self.sub = {}
        self.sub['order'] = rospy.Subscriber('~order',demo_msgs.Order,self.process_order)
#        self.sub['command'] = rospy.Subscriber('~command',demo_msgs.Command,self.processCommand)

        self.sub['response_robot'] = rospy.Subscriber('/mrh/response_robot',demo_msgs.ResponseRobot,self.process_response_robot)
        self.sub['response_goto'] = rospy.Subscriber('/mrh/response_goto',demo_msgs.ResponseGoto,self.process_response_goto)


    def spin(self):
        rospy.spin()

    def process_order(self,msg):
        self.log('Got order : ' + str(msg))

        #   Start Order Thread
        self.task_id = self.task_id + 1
        order = OrderHandler(msg.location,msg.beverage,self.task_id,self.pub)
        self.task[self.task_id] = order
        order.start()


    def process_response_robot(self,msg):
        self.task[msg.task_id].process_response_robot(msg)

    def process_response_goto(self,msg):
        self.task[msg.task_id].process_response_goto(msg)


    def log(self,msg):
        self.pub['status'].publish(msg)
        rospy.loginfo("Kitchen : " + str(msg))
