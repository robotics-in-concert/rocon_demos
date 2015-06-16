#!/usr/bin/env python

import rospy
import random
import rocon_demo_msgs.msg as rocon_demo_msgs

def commander():
    pub = rospy.Publisher('/notice', rocon_demo_msgs.Notice, queue_size=10)

    n = rocon_demo_msgs.Notice()
    while not rospy.is_shutdown():
        response = str(raw_input("> Command : "))
        n.message = str(response)
        n.level = random.randint(0,2)
        print("--- Typed : %s"%str(n))
        pub.publish(n)
    print("Bye Bye")

if __name__ == '__main__':
    try:
        rospy.init_node('notice_request')
        commander()
    except rospy.ROSInterruptException: pass
