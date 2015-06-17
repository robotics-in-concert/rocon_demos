#!/usr/bin/env python

import sys
import rospy
import concert_ping_logger

if __name__ == '__main__':
    rospy.init_node('concert_ping')

    argv = sys.argv

    robot = argv[1]

    cpl = concert_ping_logger.ConcertPing(robot)
    cpl.loginfo("Initialised")
    cpl.spin()
    cpl.loginfo("Bye Bye")
