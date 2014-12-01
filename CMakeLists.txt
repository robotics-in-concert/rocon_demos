cmake_minimum_required(VERSION 2.8.3)
project(demo_concert)

find_package(catkin REQUIRED)

catkin_package()
catkin_add_env_hooks(25.demo-concert SHELLS sh DIRECTORY ${CMAKE_CURRENT_SOURCE_DIR}/env-hooks)
