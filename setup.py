#!/usr/bin/env python

import os
from setuptools import setup

setup(
    name='simcluster',
    author='Your Name Here!',
    author_email='your.name@example.com',  # so people can pester you ;)
    version='0.1',
    # Python packages to install (i.e. the directory name)
    packages=['simcluster', 'simcluster.tests'],
    package_data={'simcluster.tests': ['refs/*.npy']},
    # This is the full name of the script "simcluster"; this will be installed to a bin/ directory
    scripts=[os.path.join('scripts', 'simcluster')]
)
