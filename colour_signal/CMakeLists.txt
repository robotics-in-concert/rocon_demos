##############################################################################
# Cmake
##############################################################################

cmake_minimum_required(VERSION 2.8.3)
project(colour_signal)

##############################################################################
# Dependencies
##############################################################################

find_package(catkin REQUIRED COMPONENTS roscpp ecl_command_line std_msgs ecl_exceptions)
find_package(OpenCV REQUIRED)

include_directories(include ${catkin_INCLUDE_DIRS} ${OpenCV_INCLUDE_DIRS})

##############################################################################
# Package
##############################################################################

catkin_package(
        INCLUDE_DIRS include
        DEPENDS OpenCV
        LIBRARIES ${PROJECT_NAME}
        CATKIN_DEPENDS roscpp
        )

##############################################################################
# Project Configuration
##############################################################################

add_subdirectory(include)
add_subdirectory(src)
