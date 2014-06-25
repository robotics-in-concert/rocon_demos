cmake_minimum_required(VERSION 2.8.3)
project(vending_machine_control)

find_package(catkin REQUIRED COMPONENTS vending_machine_msgs)

catkin_python_setup()

catkin_package()

install(PROGRAMS scripts/vending_machine_manager.py
        DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION})

install(DIRECTORY launch
        DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION})

if(CATKIN_ENABLE_TESTING)
    find_package(rostest REQUIRED)
#    catkin_add_nosetests(test)
    add_rostest(test/rostest/test_vending_machine/test_vending_machine.test)
endif()
