cmake_minimum_required(VERSION 2.8.3)
project(realrobotshow_ctrl)

find_package(catkin REQUIRED COMPONENTS
  waiterbot_bringup rospy
)

catkin_python_setup()
catkin_package()
