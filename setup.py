# -*- coding: utf-8 -*-
import os, shutil
from distutils.command.clean import clean as Clean

from setuptools import setup, find_packages
import re, ast

# get version from __version__ variable in erpnext_ytd/__init__.py
_version_re = re.compile(r'__version__\s+=\s+(.*)')

with open('erpnext_ytd/__init__.py', 'rb') as f:
	version = str(ast.literal_eval(_version_re.search(
		f.read().decode('utf-8')).group(1)))

with open('requirements.txt') as f:
	install_requires = f.read().strip().split('\n')

setup(
	name='erpnext_ytd',
	version=version,
	description='Employee Salary Year to Date',
	author='Oshane Bailey',
	author_email='oshane@alteroo.com',
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
