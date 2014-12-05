#!/usr/bin/env python

from distutils.core import setup
from catkin_pkg.python_setup import generate_distutils_setup

d = generate_distutils_setup(
    packages=['vm_delivery_robot_ctrl'],
    package_dir={'': 'src'},
)

setup(**d)
