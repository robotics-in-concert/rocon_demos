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


class WaiterSoftBot(object):

    def __init__(self, robot_name, action_name):
        self.name = robot_name
        self.action_name = action_name

        self.command_base = actionlib.SimpleActionClient('move_base', MoveBaseAction)
        rospy.loginfo('Wait for movebase...')
        self.command_base.wait_for_server()
        self.waiter_server = actionlib.SimpleActionServer(self.action_name, RobotDeliveryOrderAction, execute_cb=self.execute_callback, auto_start=False)

        self.subscriber = {}
        self.subscriber['table_list'] = rospy.Subscriber('table_pose_list', yocs_msgs.TableList, self.process_table_pose)
        self.subscriber['ar_list'] = rospy.Subscriber('marker_pose_list', AlvarMarkers, self.process_alvar_markers)

        self.table_poses = {}
        self.table_init = False

        self.ar_poses = {}
        self.ar_init = False

    def spin(self):
        self.waiter_server.start()
        rospy.loginfo("Waiterbot has been Started")
        rospy.spin()

    def process_table_pose(self, msg):
        if not self.table_init:
            rospy.loginfo('table_pose message received')

        for table in msg.tables:
            pose_stamped = PoseStamped()
            pose_stamped.pose = table.pose.pose.pose
            pose_stamped.header = table.pose.header
            self.table_poses[table.name] = pose_stamped
        self.table_init = True

    def process_alvar_markers(self, msg):
        if not self.ar_init:
            rospy.loginfo('ar marker message received')
        for m in msg.markers:
            self.ar_poses[m.id] = m.pose

        self.ar_init = True

    def process_status(self, time_range, order_id, target_goal, status,  message):
        k = 0
        timeout = random.randrange(time_range[0], time_range[1])
        while k < timeout and not rospy.is_shutdown():
            k += 1
            rospy.sleep(1)
            rospy.loginfo(self.name + " : " + message + ", [%d/%d]" % (k, timeout))

        self.feedback(order_id, target_goal, status,  message)

    def go_to(self, order_id, target_goal, status,  message):
        self.feedback(order_id, target_goal, status,  message)

        goal = MoveBaseGoal(self.table_poses[target_goal])
        self.command_base.send_goal(goal)
        self.command_base.wait_for_result()

        resp = self.command_base.get_result()
        return True

    def feedback(self, order_id, target_goal, status,  message):
        feedback = RobotDeliveryOrderFeedback()
        feedback.delivery_status.order_id = order_id
        feedback.delivery_status.target_goal = target_goal
        feedback.delivery_status.status = status

        self.waiter_server.publish_feedback(feedback)
        rospy.loginfo(target_goal + " : " + message)

    def execute_callback(self, data):
        time_start = 3
        time_end = 5
        order_id = data.order_id
        receivers = data.locations

        if self.table_init is False or self.ar_init is False:
            rospy.loginfo("Annotation data does not init, yet")
            result = RobotDeliveryOrderResult(order_id, False, "Failure!")
            self.waiter_server.set_succeeded(result)
            return

        rospy.loginfo("Order Received : Receivers = %s", data.locations)

        # Go to kitchen, and return feedback ARRIVE_KITCHEN
        self.go_to(order_id=order_id,
                   target_goal='pickup',
                   status=DeliveryStatus.GO_TO_FRONTDESK,
                   message="GO_TO_FRONTDESK")

        # Arrival at kitchen
        self.feedback(order_id, 'pickup', DeliveryStatus.ARRIVAL_AT_FRONTDESK, "ARRIVAL_AT_FRONTDESK")

        # Wait for kitchen
        self.process_status(time_range=[time_start, time_end],
                            order_id=order_id,
                            target_goal='pickup',
                            status=DeliveryStatus.WAITING_FOR_FRONTDESK,
                            message="WAITING_FOR_FRONTDESK")

        for receiver in receivers:
            target_goal =  str(receiver)
            # Go to receiver
            self.go_to(order_id=order_id,
                       target_goal=target_goal,
                       status=DeliveryStatus.GO_TO_RECEIVER,
                       message="GO_TO_RECEIVER")
            # Arrival at receiver
            self.feedback(order_id, target_goal, DeliveryStatus.ARRIVAL_AT_RECEIVER, "ARRIVAL_AT_RECEIVER")
            # Waiting confirm
            self.process_status(time_range=[time_start, time_end],
                                order_id=order_id,
                                target_goal=target_goal,
                                status=DeliveryStatus.WAITING_CONFIRM_RECEIVER,
                                message="WAITING_CONFIRM_RECEIVER")
            # Complete delivery
            self.feedback(order_id, target_goal, DeliveryStatus.COMPLETE_DELIVERY, "COMPLETE_DELIVERY")

        # Complete all delivery
        self.feedback(order_id, target_goal, DeliveryStatus.COMPLETE_ALL_DELIVERY, "COMPLETE_ALL_DELIVERY")
        # Returning to Docking
        self.go_to(order_id=order_id,
                   target_goal='docking',
                   status=DeliveryStatus.RETURN_TO_DOCK,
                   message="RETURN_TO_DOCK")

        # Complete return
        self.feedback(order_id, 'docking', DeliveryStatus.COMPLETE_RETURN, "COMPLETE_RETURN")
        rospy.loginfo(self.name + " : END_DELIVERY_ORDER")
        rospy.sleep(1)

        # Closing off the delivery
        self.feedback(order_id, 'docking', DeliveryStatus.IDLE, "IDLE")
        rospy.loginfo(self.name + " : IDLE")
        rospy.sleep(1)

        result = RobotDeliveryOrderResult(order_id, True, "Success!")
        self.waiter_server.set_succeeded(result)

if __name__ == '__main__':

    try:
        # Initialize ros node
        rospy.init_node('waiterbot')
        print rospy.get_name()
        waiter = WaiterSoftBot(rospy.get_name(), "delivery_order")
        rospy.loginfo('Initialized')

        waiter.spin()
        rospy.loginfo("Bye Bye")

    except rospy.ROSInterruptException:
        pass
