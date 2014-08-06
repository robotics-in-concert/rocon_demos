cmake_minimum_required(VERSION 2.8.3)
project(turtlebot_gazebo_concert)

find_package(catkin REQUIRED)

catkin_package(
)

install(
  PROGRAMS 
    scripts/segbot_pond
    scripts/segbot_stroll
  DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION}
)

foreach(dir concert rapps services solutions)
  install(DIRECTORY ${dir}
    DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION})
endforeach()
                                                                                                                   
                                                                                                                   

