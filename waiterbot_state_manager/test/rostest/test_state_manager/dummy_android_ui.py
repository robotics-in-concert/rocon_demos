#!/usr/bin/env python
#
# License: BSD
#   https://raw.github.com/robotics-in-concert/rocon_demos/license/LICENSE
#

import argparse
import numpy
import sys

import rospy
import std_msgs.msg as std_msgs

class DummyAndroidUI(object):
    """
        Android UI simulation
    """
    def __init__(self, drink_order):
        self._pub_drink_order = rospy.Publisher('android_ui/drink_order', std_msgs.UInt16MultiArray, latch=True)
        self._sub_drink_ar = rospy.Subscriber('android_ui/drink_ar', std_msgs.UInt16, self._drinkARCB)
        self._sub_drinks_dispensed = rospy.Subscriber('android_ui/drinks_dispensed', std_msgs.Empty,
                                                      self._drinksDispensedCB)
        self._pub_tray_empty = rospy.Subscriber('android_ui/tray_empty', std_msgs.Empty, self._trayEmptyCB)
        self._ar_marker = None
        self._ar_marker_received = False
        self._drinks_pickup_time = rospy.Duration(rospy.get_param("drinks_pickup_time", 2.0))
        self._drink_order = []
        i = int()
        for i in str(drink_order):
            self._drink_order.append(i)
        rospy.loginfo("DummyAndroidUI: Will order drinks " + str(self._drink_order) + ".")
        self._drinks_dispensed = False
        self._tray_empty = False
        self._state_drink_order = "StateDrinkOrder"
        self._state_waiting_for_ar = "StateWaitingForAR"
        self._state_drinks_ready = "StateDrinksReady"
        self._current_state = self._state_drink_order

    def _drinkARCB(self, msg):
        self._ar_marker = msg.data
        self._ar_marker_received = True

    def _drinksDispensedCB(self, msg):
        self._drinks_dispensed = True

    def _trayEmptyCB(self, msg):
        self._tray_empty = True

    def spin(self):
        while not rospy.is_shutdown():
            if self._current_state == self._state_drink_order:
                msg = std_msgs.UInt16MultiArray()
                for drink in self._drink_order:
                    msg.data.append(numpy.uint16(drink))
                self._pub_drink_order.publish(msg)
                rospy.loginfo("DummyAndroidUI: Drink order published.")
                self._current_state = self._state_waiting_for_ar
            elif self._current_state == self._state_waiting_for_ar:
                if self._ar_marker_received:
                    self._ar_marker_received = False
                    rospy.loginfo("DummyAndroidUI: Showing AR marker '" + str(self._ar_marker) + "'.")
                elif self._drinks_dispensed:
                    self._drinks_dispensed = False
                    rospy.loginfo("DummyAndroidUI: All drinks have been dispensed.")
                    self._current_state = self._state_drinks_ready
                else:
                    rospy.loginfo("DummyAndroidUI: Waiting for AR markers ...")
                    rospy.sleep(1.0)
            elif self._current_state == self._state_drinks_ready:
                if self._tray_empty:
                    self._tray_empty = False
                    rospy.loginfo("DummyAndroidUI: Customer(s) picked up all drinks. Drink delivery done.")
                    break
                else:
                    rospy.loginfo("DummyAndroidUI: Waiting for customer(s) to pick up the drinks.")
                    rospy.sleep(1.0)
            else:
                rospy.logerror("DummyAndroidUI: Invalid state. Exiting.")
                break

if __name__ == '__main__':
    rospy.init_node('dummy_android_ui')

    parser = argparse.ArgumentParser(description='Android drink ordering UI simulation')
    help_str = 'list of integer representing the drink order - each digit in the whole number represents one drink'
    parser.add_argument('drink_order', type=int, help=help_str)
    rosargs = rospy.myargv(sys.argv)
    args = parser.parse_args(rosargs[1:])

    android_ui = DummyAndroidUI(args.drink_order)
    android_ui.spin()
