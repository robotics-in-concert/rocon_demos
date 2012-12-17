
import rospy
import threading
from demo_msgs.msg import *

START = 0
WAIT_FOR_ROBOT = 1
ROBOT_ASSIGNED = 2
ROBOT_NOT_ASSIGNED = 3
ROBOT_READY = 4
ROBOT_NOT_READY = 5
ROBOT_DONE = 6
ROBOT_FAIL = 7

DRINK_READY = 8
DRINK_NOT_READY = 9

class OrderHandler(threading.Thread):

    def __init__(self,location,beverage,task_id,pub,done):

        threading.Thread.__init__(self)
        self.location = location
        self.task_id = task_id
        self.beverage = beverage
        self.status = START
        self.front_status = "WAIT"
        self.done = done

        self.pub = pub

    def run(self):
        self.log("order has been placed task id = " + str(self.task_id))

        while not rospy.is_shutdown() and self.status != ROBOT_ASSIGNED:
            self.log("Request Robot")
            self.request_robot()
            self.wait_for_state(ROBOT_ASSIGNED,ROBOT_NOT_ASSIGNED)
        self.log("Robot ready")
        self.log("Calling robot to Kitchen")
        self.call_robot()
        self.log("Waiting for robot to come kitchen")
        self.wait_for_state(ROBOT_READY,ROBOT_NOT_READY)

        # Set drink and..
        self.log("Waiting for Drink")
        self.request_drink()
        self.wait_for_state(DRINK_READY,DRINK_NOT_READY)
        self.log("Sending robot to the location : " +str(self.location))
        self.send_robot()
        self.wait_for_state(ROBOT_READY,ROBOT_FAIL)
        rospy.sleep(5.0)
        self.send_back_to_station()
        self.wait_for_state(ROBOT_READY,ROBOT_FAIL)
        self.log("Releasing Robot")
        rospy.sleep(1.0)
        self.release_robot()

        if self.status == ROBOT_READY:
            self.log("Delivery Status : Success!") 
        else:
            self.log("Delivery Status : Fail!")

        self.done(self.task_id)

    def request_robot(self):
        self.pub['request_robot'].publish(RequestRobot(self.task_id))
        self.status = WAIT_FOR_ROBOT

    def wait_for_state(self,state_1,state_2):
        while not rospy.is_shutdown():
            if self.status == state_1 or self.status == state_2:
                break
            rospy.sleep(1.0)

    def call_robot(self):
        self.pub['request_goto'].publish(RequestGoto(self.task_id,"kitchen"))
        self.status = WAIT_FOR_ROBOT

    def request_drink(self):
        self.pub['request_drink'].publish(RequestDrink(self.task_id,self.beverage))

    def send_back_to_station(self):
        self.pub['request_goto'].publish(RequestGoto(self.task_id,"station"))
        self.status = WAIT_FOR_ROBOT

    def send_robot(self):
        self.pub['request_goto'].publish(RequestGoto(self.task_id,self.location))
        self.status = WAIT_FOR_ROBOT

    def release_robot(self):
        self.pub['release_robot'].publish(ReleaseRobot(self.task_id))

    def process_response_goto(self,msg):
        if msg.status == True:
            self.status = ROBOT_READY

    def process_response_robot(self,msg):
        if msg.ready == True:
            self.log("Robot assigned")
            self.status = ROBOT_ASSIGNED
        else:
            self.log("Robot is not assigned")
            self.status = ROBOT_NOT_ASSIGNED

    def process_response_drink(self,ready):
        self.status = DRINK_READY

    def log(self,msg):
        self.front_status = msg
        rospy.loginfo("Kitchen["+str(self.task_id)+"] : " + str(msg))
