
import roslib; roslib.load_manifest('rocon_kitchen')
import rospy
from demo_msgs.msg import *
from std_msgs.msg import String
from .order_handler import *


class Kitchen(object):
    
    def __init__(self):
        self.task = {}
        self.task_id = 0

        self.pub = {}
        r = RequestRobot()
        self.pub['status'] = rospy.Publisher('~status',String)
        self.pub['request_robot'] = rospy.Publisher('/mrh/request_robot',RequestRobot)
        self.pub['request_goto'] = rospy.Publisher('/mrh/request_goto',RequestGoto)
        self.pub['release_robot'] = rospy.Publisher('/mrh/release_robot',ReleaseRobot)

        self.sub = {}
        self.sub['order'] = rospy.Subscriber('order',Order,self.process_order)
#        self.sub['command'] = rospy.Subscriber('~command',Command,self.processCommand)

        self.sub['response_robot'] = rospy.Subscriber('/mrh/response_robot',ResponseRobot,self.process_response_robot)
        self.sub['response_goto'] = rospy.Subscriber('/mrh/response_goto',ResponseGoto,self.process_response_goto)

        # For Kitchen Frontend 
        self.pub['list_tasks'] = rospy.Publisher('/kitchen/list_tasks',ListTasks)
        self.pub['request_drink'] = rospy.Publisher('/kitchen/request_drink',RequestDrink)
        self.sub['response_drink'] = rospy.Subscriber('/kitchen/response_drink',ResponseDrink,self.process_response_drink)


    def spin(self):
        while not rospy.is_shutdown():
            tasks = ListTasks()

            for i, tk in self.task.items():
                t = Task()
                t.task_id = tk.task_id
                t.status = tk.front_status
                tasks.tasks.append(t)
            self.pub['list_tasks'].publish(tasks)
            rospy.sleep(0.5)

    def process_order(self,msg):
        self.log('Got order : ' + str(msg))

        #   Start Order Thread
        self.task_id = self.task_id + 1
        order = OrderHandler(msg.location,msg.beverage,self.task_id,self.pub,self.done)
        self.task[self.task_id] = order
        order.start()

    def done(self,task_id):
#        self.log("DONE")
        del self.task[task_id]

    def process_response_robot(self,msg):
        self.task[msg.task_id].process_response_robot(msg)

    def process_response_goto(self,msg):
        self.task[msg.task_id].process_response_goto(msg)

    def process_response_drink(self,msg):
        self.task[msg.task_id].process_response_drink(msg)


    def log(self,msg):
        self.pub['status'].publish(msg)
        rospy.loginfo("Kitchen : " + str(msg))
