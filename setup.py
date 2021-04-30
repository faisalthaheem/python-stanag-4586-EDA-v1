"""
 Copyright (c) 2021 Faisal Thaheem (https://github.com/faisalthaheem/python-stanag-4586-EDA-v1)
 License GNU GENERAL PUBLIC LICENSE Version 3, 29 June 2007
"""

from setuptools import find_packages, setup

setup(
    name='stanag4586edav1',
    packages=find_packages(include=['stanag4586edav1']),
    version='0.1.0',
    description='Python Stanag 4586 Edition A v1',
    author='Faisal Thaheem',
    license='GPLV3',
    install_requires=[],
    setup_requires=['pytest-runner'],
    tests_require=['pytest'],
    test_suite='tests',
)