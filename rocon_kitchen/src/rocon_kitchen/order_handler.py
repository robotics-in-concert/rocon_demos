
import rospy
import threading
import demo_msgs.msg as demo_msgs

START = 0
WAIT_FOR_ROBOT = 1
ROBOT_ASSIGNED = 2
ROBOT_NOT_ASSIGNED = 3
ROBOT_READY = 4

class OrderHandler(threading.Thread):

    def __init__(self,location,task_id,beverage):

        self.location = location
        self.task_id = task_id
        self.beverage = beverage
        self.status = START

    def run(self):
        self.log("order has been placed")

        while self.status == ROBOT_ASSIGNED:
            self.request_robot()
            self.wait_for_state(ROBOT_ASSIGNED,NOT_ASSIGNED)

        self.call_robot()
        self.wait_for_state(ROBOT_READY,ROBOT_NOT_READY)

        # Set drink and..
        self.send_robot()
        self.wait_for_state(ROBOT_DONE,ROBOT_FAIL)

        if self.status == ROBOT_DONE:
            self.log("Delivery Status : Success!") 
        else:
            self.log("Delivery Status : Fail!")
    
    def request_robot(self)
        self.pub['request_robot'].publish(RequestRobot(self.task_id))
        self.status = WAIT_FOR_ROBOT

    def wait_for_state(self,state_1,state_2):
        while not rospy.is_shutdown() and (self.status == state_1 or self.status == state_2):
            rospy.sleep(1.0)

    def call_robot(self):
        self.pub['goto'].publish(MRHGoto(self.task_id,"kitchen"))
        self.status = WAIT_FOR_ROBOT

    def send_robot(self):
        self.pub['goto'].publish(MRHGoto(self.task_id,self.location))

    def process_response_goto(self,msg):
        if msg.status == True:
            self.status = ROBOT_READY
            self.log("Robot Ready")

    def process_response_robot(self,msg):
        if msg.ready = True:
            self.log("Robot assigned")
            self.status = ROBOT_ASSIGNED
        else:
            self.log("Robot is not assigned")
            self.status = ROBOT_NOT_ASSIGNED

    def log(self,msg):
        rospy.loginfo("Kitchen["+self.task_id+"] : " + str(msg))
