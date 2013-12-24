cmake_minimum_required(VERSION 2.8.3)
project(vending_machine_control)

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

install(PROGRAMS scripts/vending_machine.py
        DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION})

install(DIRECTORY launch
        DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION})

if(CATKIN_ENABLE_TESTING)
    find_package(rostest REQUIRED)
#    catkin_add_nosetests(test)
    add_rostest(test/rostest/test_vending_machine/test_vending_machine.test)
endif()
