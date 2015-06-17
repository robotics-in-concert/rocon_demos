
import rospy
from datetime import datetime

class RobotOrderLogger(object):

    def __init__(self, file_name='robot_order.log', mode='a'):
        self._file_name = file_name
        self._file = open(file_name, mode)

    def close(self):
        self._file.write("------\n")
        self._file.close()

    def log_start(self, goal):
        s = "[%s][%s] Received Order ID : %s, Location : %s Menus : %s\n"%(datetime.now(), rospy.Time.now(), goal.order_id, goal.locations, goal.menus)
        self._file.write(s)
        
    def log_result(self, r):
        s = "[%s][%s] Finished Order [%s][%s][%s]\n"%(datetime.now(), rospy.Time.now(), r.order_id, r.success, r.message)
        self._file.write(s)
    
    def log(self, msg):
        s = "[%s][%s] %s\n"%(datetime.now(), rospy.Time.now(), str(msg))
        self._file.write(s)
