#!/usr/bin/env python
# -*- coding: utf-8 -*-
try:
    # Use setuptools if available, for install_requires (among other things).
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup(
    name='Pylsy',
    packages=['pylsy'],
    install_requires=['wcwidth'],
    version='2.4',
    description='Pylsy is a simple library that draws tables in the Terminal.',
    author='leviathan',
    author_email='leviathan1995@outlook.com',
    url='https://github.com/Leviathan1995/Pylsy',
    test_suite='pylsy.tests',
)
