###############################################################################
# Subdirectories
###############################################################################

add_subdirectory(lib)
add_subdirectory(demos)


###############################################################################
# Macro
###############################################################################

macro(colour_signal_add_node name)
  add_executable(colour_signal_${name} ${name}.cpp)
  set_target_properties(colour_signal_${name} PROPERTIES OUTPUT_NAME ${name})
  target_link_libraries(colour_signal_${name} colour_signal_utils)
  target_link_libraries(colour_signal_${name} ${catkin_LIBRARIES} ${OpenCV_LIBRARIES})
  install(TARGETS colour_signal_${name} RUNTIME DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION})
endmacro()

###############################################################################
# Nodes
###############################################################################

colour_signal_add_node(node)
colour_signal_add_node(fake_publisher)
