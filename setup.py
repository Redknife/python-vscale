#!/usr/bin/env python
import os
try:
    from setuptools import setup
except ImportError:
    from ez_setup import use_setuptools
    use_setuptools()
    from setuptools import setup

long_description = """This library provides access to Vscale API"""

if os.path.isfile("README.md"):
    with open('README.md') as file:
        long_description = file.read()

setup(
    name='python-vscale',
    version='1.0',
    description='vscale.io API',
    author='Rogachev Sergey ( https://github.com/redknife )',
    author_email='redknife183@gmail.com',
    url='https://github.com/Redknife/python-vscale',
    packages=['vscale'],
    install_requires=['requests>=2.8.1'],
    setup_requires=['nose>=1.3.7',
                    'coverage>=4.0.3',
                    'responses==0.5.0'],
    license='MIT',
    long_description=long_description
)