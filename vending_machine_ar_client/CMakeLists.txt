cmake_minimum_required(VERSION 2.8.3)
project(vending_machine_ar_client)

find_package(catkin REQUIRED)

catkin_python_setup()

catkin_package()

install(PROGRAMS scripts/vending_machine_ar_client_node.py
        DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION})

install(DIRECTORY launch
        DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION})

if(CATKIN_ENABLE_TESTING)
    find_package(rostest REQUIRED)
    add_rostest(test/rostest/test_vm_client/test_vm_client.test)
endif()