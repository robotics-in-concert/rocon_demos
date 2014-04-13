cmake_minimum_required(VERSION 2.8.3)
project(cafe_remote_order_manager)

find_package(catkin REQUIRED COMPONENTS
  cafe_msgs
  rospy
)

catkin_python_setup()

catkin_package()
