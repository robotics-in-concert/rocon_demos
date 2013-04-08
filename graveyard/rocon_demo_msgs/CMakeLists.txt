##############################################################################
# CMake
##############################################################################

cmake_minimum_required(VERSION 2.8.3)
project(rocon_demo_msgs)

##############################################################################
# Dependencies
##############################################################################

find_package(catkin REQUIRED COMPONENTS 
    genmsg 
    geometry_msgs 
)

##############################################################################
# Messgaes
##############################################################################

add_message_files(
  DIRECTORY msg
  FILES
  Command.msg
  Goto.msg
  ListTasks.msg
  Order.msg
  ReleaseRobot.msg
  RequestDrink.msg
  RequestGoto.msg
  RequestMoveRobot.msg
  RequestRobot.msg
  ResponseDrink.msg
  ResponseMoveRobot.msg
  ResponseRobot.msg
  Task.msg
)

generate_messages(DEPENDENCIES
    geometry_msgs
)

##############################################################################
# Package
##############################################################################

catkin_package()