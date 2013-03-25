cmake_minimum_required(VERSION 2.4.6)
include($ENV{ROS_ROOT}/core/rosbuild/rosbuild.cmake)
include(FindPkgConfig)
rosbuild_init()

# Build tools
execute_process(COMMAND cmake -E chdir ${PROJECT_SOURCE_DIR} make -f Makefile.webtools
                RESULT_VARIABLE _make_failed)

if(_make_failed)
    message(FATAL_ERROR "Build of Webtools failed")
endif(_make_failed)
