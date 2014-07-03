#!/usr/bin/env python
# -*- coding: utf-8 -*-

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup(
    name='lizepy',
    version='0.3.2',
    author='Alexandre Vicenzi',
    author_email='vicenzi.alexandre@gmail.com',
    packages=['lizepy'],
    url='https://github.com/alexandrevicenzi/lizepy',
    license='LICENSE',
    description='Python lib for Telize JSON IP and GeoIP REST API',
)
