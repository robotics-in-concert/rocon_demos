##############################################################################
# Sources
##############################################################################

file(GLOB SOURCES RELATIVE ${CMAKE_CURRENT_SOURCE_DIR} *.cpp)
set_source_files_properties(histogram_analytics.cpp PROPERTIES COMPILE_FLAGS "-std=c++0x")

##############################################################################
# Builds
##############################################################################

add_library(colour_signal_utils ${SOURCES})
#set_target_properties(colour_signal_utils PROPERTIES COMPILE_FLAGS "-std=c++0x")