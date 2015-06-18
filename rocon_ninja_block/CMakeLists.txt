##############################################################################
# CMake
##############################################################################

cmake_minimum_required(VERSION 2.8.3)
project(rocon_ninja_block)

##############################################################################
# Catkin
##############################################################################
find_package(catkin REQUIRED COMPONENTS
    message_generation std_msgs diagnostic_msgs actionlib_msgs roslint)

catkin_python_setup()

## Generate actions in the 'action' folder
add_action_files(
  DIRECTORY action
  FILES
  CheckMotion.action
  GetDeviceList.action
)

## Generate msgs in the 'msg' folder
add_message_files(
  DIRECTORY msg
  FILES
  NBDevice.msg
  NBDeviceList.msg
  )

add_service_files(
  DIRECTORY srv
  FILES
  GetNBDeviceList.srv
)

generate_messages(
  DEPENDENCIES
  std_msgs  # Or other packages containing msgs
  diagnostic_msgs
  actionlib_msgs
)

catkin_package(CATKIN_DEPENDS message_runtime std_msgs actionlib_msgs)

file(GLOB_RECURSE ${PROJECT_NAME}_MODULE_SOURCES RELATIVE ${PROJECT_SOURCE_DIR} src/*.py)
file(GLOB_RECURSE ${PROJECT_NAME}_SCRIPT_SOURCES RELATIVE ${PROJECT_SOURCE_DIR} scripts/*)
roslint_python(${${PROJECT_NAME}_MODULE_SOURCES} ${${PROJECT_NAME}_SCRIPT_SOURCES})

##############################################################################
# Installs
##############################################################################
