###############################################################################
# Subdirectories
###############################################################################

add_subdirectory(lib)
add_subdirectory(demos)

###############################################################################
# Nodes
###############################################################################

add_executable(colour_signal_node node.cpp)
target_link_libraries(colour_signal_node colour_signal_utils)
target_link_libraries(colour_signal_node ${catkin_LIBRARIES})

install(TARGETS colour_signal_node RUNTIME DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION})
