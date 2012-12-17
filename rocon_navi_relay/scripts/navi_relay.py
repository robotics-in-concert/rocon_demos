#!/usr/bin/env python
#
# License: BSD
#   https://raw.github.com/robotics-in-concert/rocon_demo/rocon_navi_relay/LICENSE
#
##############################################################################
# Imports
##############################################################################

import roslib
roslib.load_manifest('rocon_navi_relay')
import rospy
from rocon_navi_relay import *

##############################################################################
# Main
##############################################################################

if __name__ == '__main__':

    rospy.init_node('rocon_navi_relay')
    navi_relay = NaviRelay()
    navi_relay.spin()
    