#!/usr/bin/env python

from distutils.core import setup
from catkin_pkg.python_setup import generate_distutils_setup

d = generate_distutils_setup(
   packages=['grasping_type_inference'],
   package_dir={'': 'src'}
)

setup(**d)
