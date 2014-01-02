cmake_minimum_required(VERSION 2.8.3)
project(waiterbot_state_manager)

find_package(catkin REQUIRED)

catkin_python_setup()

catkin_package()

install(PROGRAMS scripts/state_manager_node.py
        DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION})

install(DIRECTORY launch
        DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION})

#if(CATKIN_ENABLE_TESTING)
#    find_package(rostest REQUIRED)
#    add_rostest(test/rostest/test_state_manager/test_state_manager.test)
#endif()