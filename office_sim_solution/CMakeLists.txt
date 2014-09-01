cmake_minimum_required(VERSION 2.8.3)
project(office_sim_solution)

find_package(catkin REQUIRED)

catkin_package()

foreach(dir concert rapps services solutions)
  install(DIRECTORY ${dir}
    DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION})
endforeach()
                                                                                                                   
                                                                                                                   

