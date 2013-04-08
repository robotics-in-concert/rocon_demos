cmake_minimum_required(VERSION 2.8.3)
project(cafe_msgs)

## Find catkin macros and libraries
## if COMPONENTS list like find_package(catkin REQUIRED COMPONENTS xyz)
## is used, also find other catkin packages
find_package(catkin REQUIRED COMPONENTS std_msgs actionlib_msgs message_generation)

#######################################
## Declare ROS messages and services ##
#######################################

# Generate messages in the 'msg' folder
add_message_files(
  DIRECTORY msg
  FILES
  Menu.msg
  OrderList.msg
  Order.msg
  Status.msg
)

## Generate services in the 'srv' folder
# add_service_files(
#   FILES
#   Service1.srv
#   Service2.srv
# )

## Generate actions in the 'action' folder
add_action_files(
  DIRECTORY action
  FILES
  DeliverOrder.action
  UserOrder.action
)

# Generate added messages and services with any dependencies listed here
generate_messages(
  DEPENDENCIES
  std_msgs  # Or other packages containing msgs
  actionlib_msgs
)

###################################
## catkin specific configuration ##
###################################
## The catkin_package macro generates cmake config files for your package
## Declare things to be passed to dependent projects
## LIBRARIES: libraries you create in this project that dependent projects also need
## CATKIN_DEPENDS: catkin_packages dependent projects also need
## DEPENDS: system dependencies of this project that dependent projects also need
catkin_package(
  CATKIN_DEPENDS message_runtime std_msgs actionlib_msgs
)

