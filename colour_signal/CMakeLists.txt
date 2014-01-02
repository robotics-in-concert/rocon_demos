##############################################################################
# Cmake
##############################################################################

cmake_minimum_required(VERSION 2.8.3)
project(colour_signal)

##############################################################################
# Dependencies
##############################################################################

find_package(catkin REQUIRED COMPONENTS 
    roscpp
    roslib
    ecl_command_line
    std_msgs
    ecl_exceptions
    sensor_msgs
    cv_bridge
)

find_package(OpenCV REQUIRED)

include_directories(include ${catkin_INCLUDE_DIRS} ${OpenCV_INCLUDE_DIRS})

##############################################################################
# Package
##############################################################################

catkin_package(
        INCLUDE_DIRS include
        DEPENDS OpenCV
        LIBRARIES ${PROJECT_NAME}
        CATKIN_DEPENDS
            roscpp
            roslib
            ecl_command_line
            std_msgs
            ecl_exceptions
            sensor_msgs
            cv_bridge
        )

##############################################################################
# Project Configuration
##############################################################################

add_subdirectory(include)
add_subdirectory(src)

##############################################################################
# Installation
##############################################################################

install(DIRECTORY launch DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION})
install(DIRECTORY images DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION})
