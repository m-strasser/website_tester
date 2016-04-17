#!/usr/bin/env python
# -*- coding: utf-8 -*-

# This file is part of website_tester.
# https://github.com/m-strasser/website_tester

# Licensed under the GPL license:
# http://www.opensource.org/licenses/GPL-license
# Copyright (c) 2016, Michael Strasser <mst1409@gmx.at>

from setuptools import setup, find_packages
from website_tester import __version__

tests_require = [
    'mock',
    'nose',
    'coverage',
    'yanc',
    'preggy',
    'tox',
    'ipdb',
    'coveralls',
    'sphinx',
]

setup(
    name='website_tester',
    version=__version__,
    description='Automatically check if your websites are up & running correctly.',
    long_description='''
Automatically check if your websites are up & running correctly.
''',
    keywords='webtesting web-testing website-testing',
    author='Michael Strasser',
    author_email='mst1409@gmx.at',
    url='https://github.com/m-strasser/website_tester',
    license='GPL',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GPL License',
        'Natural Language :: English',
        'Operating System :: Unix',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Operating System :: OS Independent',
    ],
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        # add your dependencies here
        # remember to use 'package-name>=x.y.z,<x.y+1.0' notation (this way you get bugfixes)
    ],
    extras_require={
        'tests': tests_require,
    },
    entry_points={
        'console_scripts': [
            # add cli scripts here in this form:
            # 'website_tester=website_tester.cli:main',
        ],
    },
)
