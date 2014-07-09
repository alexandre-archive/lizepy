#!/usr/bin/env python
# -*- coding: utf-8 -*-

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup(
    name='lizepy',
    version='0.4.0',
    author='Alexandre Vicenzi',
    author_email='vicenzi.alexandre@gmail.com',
    packages=['lizepy'],
    url='https://github.com/alexandrevicenzi/lizepy',
    license='MIT',
    description='Python library for Telize JSON IP and GeoIP REST API',
)
