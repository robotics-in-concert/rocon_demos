cmake_minimum_required(VERSION 2.8.3)
project(rocon_vending_machine)

find_package(catkin REQUIRED COMPONENTS actionlib_msgs
                                        message_generation
                                        std_msgs
                                        rospy)

catkin_python_setup()

add_message_files(DIRECTORY msg
                  FILES DrinkType.msg
                        ErrorCodes.msg)

add_action_files(DIRECTORY action
                 FILES DrinkOrder.action)

generate_messages(DEPENDENCIES actionlib_msgs
                               std_msgs)

catkin_package(CATKIN_DEPENDS actionlib_msgs
                              message_runtime
                              std_msgs)

install(PROGRAMS scripts/rocon_vending_machine
        DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION})

#############
## Testing ##
#############

## Add gtest based cpp test target and link libraries
# catkin_add_gtest(${PROJECT_NAME}-test test/test_vending_machine_control.cpp)
# if(TARGET ${PROJECT_NAME}-test)
#   target_link_libraries(${PROJECT_NAME}-test ${PROJECT_NAME})
# endif()

## Add folders to be run by python nosetests
# catkin_add_nosetests(test)
