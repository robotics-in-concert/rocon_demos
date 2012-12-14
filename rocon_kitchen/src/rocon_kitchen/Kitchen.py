
import rospy
from demo_msgs.msg as demo_msgs
from std_msgs.msg import String


class Kitchen(object):
    
    def __init__(self):
        self.pub = {}
        self.pub['status'] = rospy.Publisher('~status',String)
        self.pub['goto'] = rospy.Publisher('/goto',demo_msgs.Goto)

        self.sub = {}
        self.sub['order'] = rospy.Subscriber('~order',demo_msgs.Order,self.processOrder)
        self.sub['command'] = rospy.Subscriber('~command',demo_msgs.Command,self.processCommand)

    def spin(self):

        """
        pub = rospy.Publisher('/command',Command)
        while not rospy.is_shutdown():
            c = Command()
            c.command ="Goto"
            c.param = "kitchen"
            rospy.sleep(4)
        """

    def processCommand(self,msg):
        self.log('Got Command : ' + str(msg))

    def processOrder(self,msg):
        self.log('Got order : ' + str(msg))
        self.log('Sending goto Message' + str(msg))

        go = demo_msgs.Goto()
        self.pub['goto'].publish(go)
        self.log('Message Sent')


    def log(self,msg):
        self.pub['status'].publish(msg)
        rospy.loginfo("Kitchen : " + str(msg))
