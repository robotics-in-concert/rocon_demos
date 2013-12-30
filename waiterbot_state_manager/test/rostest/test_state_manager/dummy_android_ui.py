#!/usr/bin/env python
#
# License: BSD
#   https://raw.github.com/robotics-in-concert/rocon_demos/license/LICENSE
#

import rospy
import std_msgs.msg as std_msgs

class DummyAndroidUI(object):
    """
        Android UI simulation
    """
    def __init__(self):
        self._pub_drink_order = rospy.Publisher('android_ui/drink_order', std_msgs.UInt16MultiArray, latch=True)
        self._sub_drink_ar = rospy.Subscriber('android_ui/drink_ar', std_msgs.UInt16, self._drinkARCB)
        self._ar_marker = None
        self._ar_marker_received = False
        self._sub_drinks_dispensed = rospy.Subscriber('android_ui/drinks_dispensed', std_msgs.Empty,
                                                      self._drinksDispensedCB)
        self._drinks_dispensed = False
        self._state_drink_order = "StateDrinkOrder"
        self._state_waiting_for_ar = "StateWaitingForAR"
        self._state_drinks_ready = "StateDrinksReady"
        self._current_state = self._state_drink_order

    def _drinkARCB(self, msg):
        self._ar_marker = msg.data
        self._ar_marker_received = True

    def _drinksDispensedCB(self):
        self._drinks_dispensed = True

    def spin(self):
        while not rospy.is_shutdown():
            rospy.loginfo("DummyAndroidUI: Now in state '" + self._current_state + "'")

            if self._current_state == self._state_drink_order:
                msg = std_msgs.UInt16MultiArray()
                msg.data.append(1) # order one coke
                self._pub_drink_order.publish(msg)
                self._current_state = self._state_waiting_for_ar
            elif self._current_state == self._state_waiting_for_ar:
                if self._ar_marker_received:
                    rospy.loginfo("DummyAndroidUI: Showing AR marker '" + str(self._ar_marker) + "'.")
                    self._ar_marker_received = False
                elif self._drinks_dispensed:
                    rospy.loginfo("DummyAndroidUI: All drinks have been dispensed.")
                    self._current_state = self._state_drinks_ready
                    self._drinks_dispensed = False
            elif self._current_state == self._state_drinks_ready:
                    rospy.loginfo("DummyAndroidUI: Tray empty. Ready for next order.")
                    self._current_state = self._state_drink_order

            rospy.sleep(0.1)

if __name__ == '__main__':
  rospy.init_node('dummy_android_ui')
  android_ui = DummyAndroidUI()
  android_ui.spin()
