cmake_minimum_required(VERSION 2.8.3)
project(turtlebot_concert)

find_package(catkin REQUIRED)

catkin_package()

foreach(dir solution)
  install(DIRECTORY ${dir}
    DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION})
endforeach()
                                                                                                                   
                                                                                                                   

