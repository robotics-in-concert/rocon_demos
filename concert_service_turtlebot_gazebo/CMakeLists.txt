cmake_minimum_required(VERSION 2.8.3)
project(concert_service_turtlebot_gazebo)

find_package(catkin REQUIRED COMPONENTS
  concert_service_gazebo
)

catkin_python_setup()

catkin_package()

install(PROGRAMS
  scripts/turtlebot_gazebo_manager
  DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION}
)

install(DIRECTORY launch
  DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION}
)

install(DIRECTORY services
  DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION}
)
