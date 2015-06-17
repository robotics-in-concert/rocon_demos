cmake_minimum_required(VERSION 2.8.3)
project(concert_ping_logger)

find_package(catkin REQUIRED COMPONENTS
  rospy
  concert_master
)

catkin_python_setup()

catkin_package()
