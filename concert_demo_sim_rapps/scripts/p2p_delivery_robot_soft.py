#!/usr/bin/env python
import rospy
import threading
import random
import time

# ros msg
import actionlib
from simple_delivery_msgs.msg import *

from move_base_msgs.msg import *
from geometry_msgs.msg import PoseStamped
import yocs_msgs.msg as yocs_msgs
from ar_track_alvar_msgs.msg import *
from visualization_msgs.msg import *

class P2PDeliveryRobot(object):

    def __init__(self, robot_name, action_name):
        self.name = robot_name
        self.action_name = action_name

        self.command_base = actionlib.SimpleActionClient('move_base', MoveBaseAction)
        self.loginfo('Wait for movebase')
        self.command_base.wait_for_server()
        self.delivery_server = actionlib.SimpleActionServer(self.action_name, P2PDeliveryOrderAction, self.execute_callback, auto_start=False)

        self.locations = {}
        self.locations_init = False

        self.global_markers = {}
        self.global_markers_init = False

        self.pub = {}
        self.pub['robot_status'] = rospy.Publisher('robot_status', RobotStatus, queue_size=10, latch=True)

        self.sub = {}
        self.sub['location_list'] = rospy.Subscriber('location_list', yocs_msgs.WaypointList, self.process_waypoints)
        self.sub['global_marker_list'] = rospy.Subscriber('global_marker_list', AlvarMarkers, self.process_global_markers)

        self.battery_status = 100

    def execute_callback(self, goal):
        time_start = 5
        time_end = 6
        order_id = goal.order_id
        caller = goal.sender
        recipient = goal.receiver
        message = goal.message

        self.loginfo('Order Received [%s -> %s]'%(caller, recipient))

        # Go to the caller, and return feedback arrive caller
        self.go_to(order_id, target_goal=caller, status=P2PDeliveryStatus.GO_TO_PICKUP, message="Go to caller")

        # Arrival at caller
        self.feedback(order_id, caller, P2PDeliveryStatus.ARRIVAL_AT_PICKUP, "Arrived at caller")
        self.pub['robot_status'].publish(RobotStatus(P2PDeliveryStatus.ARRIVAL_AT_PICKUP, self.battery_status))

        # Wait for Caller's confirmation
        self.process_status(time_range=[time_start, time_end], order_id=order_id, target_goal=caller, status=P2PDeliveryStatus.WAITING_FOR_PICKUP_CONFIRM, message=message)

        # Go to receiver
        self.go_to(order_id=order_id, target_goal=recipient, status=P2PDeliveryStatus.GO_TO_RECEIVER, message="Go to recipient")

        # arrival at receiver
        self.feedback(order_id, recipient, P2PDeliveryStatus.ARRIVAL_AT_RECEIVER, "Arrival at receiver")
        self.pub['robot_status'].publish(RobotStatus(P2PDeliveryStatus.ARRIVAL_AT_RECEIVER, self.battery_status))

        # Wait for Receiver's confirmation
        self.process_status(time_range=[time_start, time_end], order_id=order_id, target_goal=recipient, status=P2PDeliveryStatus.WAITING_FOR_RECEIVER_CONFIRM, message=message)

        # Complete Delivery
        self.feedback(order_id, recipient, P2PDeliveryStatus.COMPLETE_DELIVERY, "COMPLETE_DELIVERY")
        self.pub['robot_status'].publish(RobotStatus(P2PDeliveryStatus.COMPLETE_DELIVERY, self.battery_status))

        # Complete all delivery
        #self.feedback(order_id, recipient, P2PDeliveryStatus.COMPLETE_ALL_DELIVERY, "COMPLETE_ALL_DELIVERY")
        #self.publisher['robot_status'].publish(RobotStatus(P2PDeliveryStatus.COMPLETE_ALL_DELIVERY, self.battery_status))

        # Returning to Docking
        self.go_to(order_id=order_id, target_goal='docking', status=P2PDeliveryStatus.RETURN_TO_DOCK, message="RETURN_TO_DOCK")
        self.loginfo("IDLE")
        rospy.sleep(1)

        result = P2PDeliveryOrderResult(order_id, True, "Success!")
        self.delivery_server.set_succeeded(result)

    def spin(self):
        self.loginfo('Waiting for locations and global markers')
        while not self.locations_init or not self.global_markers_init:
            rospy.sleep(2.0)
            self.loginfo('Waiting for locations and global markers')

        self.delivery_server.start()
        self.loginfo('Delivery robot has been started')
        self.pub['robot_status'].publish(RobotStatus(DeliveryStatus.IDLE, self.battery_status))
        rospy.spin()

    def process_status(self, time_range, order_id, target_goal, status,  message):
        k = 0
        timeout = random.randrange(time_range[0], time_range[1])
        while k < timeout and not rospy.is_shutdown():
            k += 1
            rospy.sleep(1)
            self.loginfo("%s, [%d/%d]" % (message, k, timeout))

        self.feedback(order_id, target_goal, status,  message)
        self.pub['robot_status'].publish(RobotStatus(status, self.battery_status))

    def go_to(self, order_id, target_goal, status, message):
        self.feedback(order_id, target_goal, status, message)
        self.pub['robot_status'].publish(RobotStatus(status, self.battery_status))

        goal = MoveBaseGoal(self.locations[target_goal])
        self.command_base.send_goal(goal)
        self.command_base.wait_for_result()
        resp = self.command_base.get_result()
        return True

    def feedback(self, order_id, target_goal, status, message):
        feedback = P2PDeliveryOrderFeedback()
        feedback.delivery_status.order_id = order_id
        feedback.delivery_status.target_goal = target_goal
        feedback.delivery_status.status = status

        self.delivery_server.publish_feedback(feedback)
        #self.loginfo("%s - %s"(target_goal, message)

    def loginfo(self, msg):
        rospy.loginfo("%s : %s"%(self.name, str(msg)))

    def process_waypoints(self, msg):
        for p in msg.waypoints:
            pose_stamped = PoseStamped()
            pose_stamped.pose = p.pose
            pose_stamped.header = p.header
            self.locations[p.name] = pose_stamped

        if not self.locations_init:
            self.loginfo('received waypoint locations')
            self.locations_init = True

    def process_global_markers(self, msg):
        for m in msg.markers:
            self.global_markers[m.id] = m.pose

        if not self.global_markers_init:
            self.loginfo('received global markers')
            self.global_markers_init = True


if __name__ == '__main__':
    try:
        # Initialize ros node
        rospy.init_node('delivery_robot')
        rospy.loginfo(rospy.get_name())
        volume = rospy.get_param('~volume' , 75)
        rospy.loginfo("delivery robot sound volume: " + str(volume))

        waiter = P2PDeliveryRobot(rospy.get_name(), "p2p_delivery_order")
        rospy.loginfo('Initialized')
        waiter.spin()
        rospy.loginfo("Bye Bye")

    except rospy.ROSInterruptException:
        pass
