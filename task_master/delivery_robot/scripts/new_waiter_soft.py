#!/usr/bin/env python
import rospy
import threading
import random
import time

##ros msg
import actionlib
from cafe_msgs.msg import *
from move_base_msgs.msg import *
from geometry_msgs.msg import PoseStamped
from semantic_region_handler.msg import *
from ar_track_alvar.msg import *

class WaiterSoftBot(object):
    def __init__(self,robot_name,action_name):
        self.name = robot_name
        self.action_name = action_name
        self.waiter_server = actionlib.SimpleActionServer(self.action_name,DeliverOrderAction, execute_cb = self.execute_callback,auto_start=False)

        self.command_base = actionlib.SimpleActionClient('move_base',MoveBaseAction)
        rospy.loginfo('Wait for movebase...')
        self.command_base.wait_for_server()


        self.subscriber = {}
        self.subscriber['table_list'] = rospy.Subscriber('table_post_list',TablePoseList,self.process_table_pose)
        self.subscriber['ar_list'] = rospy.Subscriber('ar_list',AlvarMarkers,self.process_alvar_markers)

        self.table_poses = {}   
        self.table_init = False

        self.ar_poses = {}   
        self.ar_init = False
        
    def spin(self):
        self.waiter_server.start() 
        rospy.loginfo("Waiterbot has been Started")
        rospy.spin()

    def process_table_pose(self,msg):

        if not self.table_init:
          rospy.loginfo('table_pose message received')
          
          for table in msg.tables:
            pose_stamped = PoseStamped()
            pose_stamped.pose = table.pose_cov_stamped.pose.pose 
            pose_stamped.header = table.pose_stamped.header
            self.table_poses[table.name] = pose_stamped 
          
          self.table_init = True

    def process_alvar_markers(self,msg):

        if not self.ar_init:
          rospy.loginfo('ar marker message received')

          for m in msg.markers:
            self.ar_poses[m.id] = m.pose

          self.ar_init = True


    def process_status(self,time_range,message,feedback_status):

        feedback = DeliverOrderFeedback()
        feedback.status = feedback_status
        self.waiter_server.publish_feedback(feedback)

        k = 0;
        timeout = random.randrange(time_range[0],time_range[1])
        while k < timeout and not rospy.is_shutdown():
            k += 1
            rospy.sleep(1)
            rospy.loginfo(self.name + " : " +  message +", [%d/%d]"%(k,timeout))
        
    def feedback(self,message,feedback_status):
        rospy.loginfo(self.name + " : " + message)
        feedback = DeliverOrderFeedback()
        feedback.status = feedback_status
        self.waiter_server.publish_feedback(feedback)

    def execute_callback(self,data):
        #print data, type(data), dir(data)
        #print type(data._connection_header)
        rospy.loginfo("Order Received : Robotname = %s",data.order.robot_name)

        #Go to kitchen, and return feedback ARRIVE_KITCHEN
        self.go_to('kitchen',message = "GO TO KITCHEN",feedback_status = Status.GO_TO_KITCHEN)

        # feedback arrive kitchen
        self.feedback('ARRIVE KITCHEN',Status.ARRIVE_KITCHEN)

        # Wait for kitchen
        self.process_status(time_range=[1,3],message="WAITING_FOR_KITCHEN",feedback_status=Status.WAITING_FOR_KITCHEN)
        
        #In delivery      
        self.go_to('table'+data.order.table_id,message="IN DELIVERY",feedback_status = Status.IN_DELIVERY)

        # feedback arrive table
        self.feedback('ARRIVE TABLE',Status.ARRIVE_TABLE)

        # Waiting for user confirmation
        self.process_status(time_range=[10,15],message="WAITING FOR USER CONFIRMATION",feedback_status=Status.WAITING_FOR_USER_CONFIRMATION)

        # Complete Delivery 
        self.feedback('COMPLETE DELIVERY',Status.COMPLETE_DELIEVERY)

        # Returning to Docking
        self.go_to('dock',message="Returning to dock",feedback = Status.RETURNING_TO_DOCK)
        #self.process_status(time_range=[5,10],message="RETURNING TO DOCK", feedback_status=Status.END_DELIEVERY_ORDER)

        # Finishing delivery
        self.feedback('END DELIVERY',Status.END_DELIEVERY_ORDER)
		
        rospy.sleep(1)
        
        # Closing off the delivery 
        result = DeliverOrderResult("Success!")
        self.waiter_server.set_succeeded(result)

    def go_to(self,target_goal,message,feedback_status):
        rospy.loginfo(self.name + " : " + message)

        feedback = DeliverOrderFeedback()
        feedback.status = feedback_status
        self.waiter_server.publish_feedback(feedback)

        goal = MoveBaseGoal(self.poses[target_goal])
        self.command_base.send_goal(goal)
        resp = self.command_base.wait_for_result()

        result = resp.get_result()
        return True
      
    
if __name__ == '__main__':
    
    try:
        # Initialize ros node
        rospy.init_node('waiterbot')

        waiter = WaiterSoftBot(rospy.get_name(),"delivery_order")
        rospy.loginfo('Initialized')

        waiter.spin()
        rospy.loginfo("Bye Bye")

    except rospy.ROSInterruptException:
        pass

