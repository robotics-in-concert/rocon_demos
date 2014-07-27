cmake_minimum_required(VERSION 2.8.3)
project(map_saver)

find_package(catkin REQUIRED COMPONENTS
  map_server
  map_store
  rospy
)

catkin_python_setup()
catkin_package()

install(PROGRAMS
  scripts/map_saver.py
  DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION}
)
