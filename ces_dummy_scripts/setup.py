#!/usr/bin/env python

from distutils.core import setup
from catkin_pkg.python_setup import generate_distutils_setup

d = generate_distutils_setup(packages=['ces_dummy_scripts'],
                             package_dir={'': 'src'},
                             requires=['rospy','std_srvs', 'waiterbot_msgs','kobuki_msgs'])

setup(**d)
