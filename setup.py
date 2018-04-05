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
    version='3.6',
    description='Pylsy is a simple library that draws tables in the Terminal.',
    long_description=open('README.md').read(),
    author='leviathan1995',
    author_email='leviathan0992@gmail.com',
    url='https://github.com/Leviathan1995/Pylsy',
    license='MIT',
    test_suite='pylsy.tests',
)
