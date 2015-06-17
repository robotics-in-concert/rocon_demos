
import rospy
import datetime 

class RobotOrderLogger(object):

    def __init__(self, file_name='robot_order.log', mode='a'):
        self._file_name = file_name
        self._file = open(file_name, mode)

    def close(self):
        self._file.close()

    def log_start(self, goal):
        s = "[%s][%s] Received Order ID : %s, Location : %s\n"%(datetime.now(), rospy.Time.now(), goal.order_id, goal.locations)
        self._file.write(s)
        
    def log_result(self, r):_
        s = "[%s][%s] Finished Order [%s][%s][%s]"%(datetime.now(), rospy.Time.now(), r.order_id, r.success, r.message)
        self._file.write(s)
