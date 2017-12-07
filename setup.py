#!/usr/bin/env/python
# -*- coding: utf-8 -*-

from setuptools import setup

setup(
	name = 'tinyplot',
	version = '0.1.0dev',
	description = 'A tiny tool for building two-dimensional plots',
	author = 'The tinyplot developers',
	packages = ['tinyplot'],
	url = 'https://gitlab.com/vladklokun/plotscript',
	install_requires = [
		'setuptools>=38.0.2',
		'matplotlib>=2.1.0',
		'numpy>=1.13.3'
	],
)