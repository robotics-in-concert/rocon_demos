###############################################################################
# Macro
###############################################################################

macro(colour_signal_add_utility name)
  add_executable(colour_signal_${name} ${name}.cpp)
  set_target_properties(colour_signal_${name} PROPERTIES OUTPUT_NAME ${name})
  target_link_libraries(colour_signal_${name} colour_signal_utils)
  target_link_libraries(colour_signal_${name} ${catkin_LIBRARIES} ${OpenCV_LIBRARIES})
  install(TARGETS colour_signal_${name} RUNTIME DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION})
endmacro()

###############################################################################
# Setup
###############################################################################

colour_signal_add_utility(histograms)
colour_signal_add_utility(hues)
