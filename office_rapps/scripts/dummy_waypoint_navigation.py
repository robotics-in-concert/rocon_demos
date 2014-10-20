#!/usr/bin/env python
import rospy
import yocs_msgs.msg as yocs_msg

class GocartBot(object):

    def __init__(self, name):
        self._name = name
        self._pub = {}
        self._pub['nav_ctrl_status'] = rospy.Publisher('nav_ctrl_status', yocs_msgs.NavigationControlStatus, queue_size=5)
        self._sub ={}
        self._sub['nav_ctrl'] = rospy.Subscriber('nav_ctrl', yocs_msgs.NavigationControl, self._process_nav_ctrl)

    def _process_nav_ctrl(self, msg):
        message = "Received command : %s"% str(msg)
        self.loginfo(message)
        s = yocs_msgs.NavigationControlStatus(0, message)
        self._pub['nav_ctrl_status'].publish(s)

    def spin(self):
        rospy.spin()

    def loginfo(self, msg):
        rospy.loginfo("%s : %s"%(self._name, str(msg)))

if __name__ == '__main__':

    try:
        rospy.init_node('dummy_gocart')

        gocart = GocartBot(rospy.get_name())
        gocart.loginfo("Initialized")
        gocart.spin()
        gocart.loginfo("Bye Bye")
    except rospy.ROSInterruptException:
        pass
