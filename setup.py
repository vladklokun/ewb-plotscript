#!/usr/bin/unv/ python
# -*- coding: utf-8 -*-

import io
import os
import sys

from setuptools import find_packages, setup

# Package metadata
NAME = 'tinyplot'
DESCRIPTION = 'A tiny tool for building two-dimensional plots'
URL = 'https://gitlab.com/vladklokun/plotscript'
AUTHOR = 'The tinyplot developers'
VERSION = '0.1.0'

# Package requirements
REQUIRED = [
	'matplotlib',
	'numpy',
]

setup(
	name = NAME,
	version = VERSION
	description = DESCRIPTION,
	author = AUTHOR,
	packages = find_packages(exclude = ('tests',))
	url = URL,
	install_requires = REQUIRED,
)