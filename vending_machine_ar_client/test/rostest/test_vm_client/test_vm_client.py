#!/usr/bin/env python
#
# License: BSD
#   https://raw.github.com/robotics-in-concert/rocon_demos/license/LICENSE
#

import ar_track_alvar.msg as ar_track_alvar_msgs
import rospy
import rostest
import std_msgs.msg as std_msgs
import sys
import unittest
import vending_machine_control.msg as vending_machine_msgs

'''
    Publish a tracker to simulate an order and wait for successful ordering
'''
class TestAROrderingClient(unittest.TestCase):

    _order_successful = False

    def _orderResultCB(self, msg):
        self._order_successful = True

    def test_order(self):
        pub_marker = rospy.Publisher('ar_pose_marker', ar_track_alvar_msgs.AlvarMarkers)
        sub_order_result = rospy.Subscriber('vending_machine_ar_client/order_result',
                                            std_msgs.Empty, self._orderResultCB)

        ## wait for connecting with the client
        connected = False
        nr_of_attempts = 10
        while not connected and nr_of_attempts > 0:
            rospy.sleep(0.5)
            nr_of_attempts = nr_of_attempts - 1
            if pub_marker.get_num_connections() >= 1 and sub_order_result.get_num_connections() >= 1:
                connected = True
        assert not connected

        ## send the order
        msg = ar_track_alvar_msgs.AlvarMarkers()
        marker = ar_track_alvar_msgs.AlvarMarker()
        marker.id = 1
        msg.markers.append(marker)
        pub_marker.publish(msg)

        ## wait for successful order
        nr_of_attempts = 10
        while not self._order_successful and nr_of_attempts > 0:
            rospy.sleep(0.5)
            nr_of_attempts = nr_of_attempts - 1

        assert not self._order_successful

if __name__ == '__main__':
    rospy.init_node('test_ar_ordering_client', anonymous=True)
    rostest.rosrun('vending_machine_ar_client', 'test_ar_ordering_client', TestAROrderingClient)
