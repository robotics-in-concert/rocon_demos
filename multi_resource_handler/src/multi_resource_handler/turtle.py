
import rospy
from geometry_msgs.msg import Twist

class Turtle(object):

    def __init__(self,name,status):
        self.name = name
        self.status = status

        self.pub = {}
        self.pub['move_turtle'] = rospy.Publisher(self.name+'/cmd_vel',Twist)

    def set_task(self,id):
        self.task_id = id
        self.status = True

    def goto(self,loc):
        print "Goto " + str(loc)
        t = Twist()
        t.angular.z = 1.0
        self.pub['move_turtle'].publish(t)
        rospy.sleep(1.0)

    def release(self):
        self.task_id = None
        self.status = False
