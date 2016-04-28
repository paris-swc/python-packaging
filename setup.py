#!/usr/bin/env python

from setuptools import setup

setup(
    name='simcluster',
    author='Your Name Here!',
    author_email='your.name@example.com',  # so people can pester you ;)
    version='0.1',
    py_modules=['simcluster'],  # Python modules to install (without the .py in the filename)
    scripts=['simcluster']  # This is the full name of the script "simcluster"; this will be installed to a bin/ directory
)