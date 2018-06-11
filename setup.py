#!/usr/bin/env python

from setuptools import setup
import os
import re

with open(os.path.join('pycket', '__init__.py')) as f:
    version = re.search(r"^__version__ = ['\"]([^'\"]*)['\"]", f.read(), re.M).group(1)

setup(
    name='pycket',
    version=version,
    description="Extract data from packet of bits",
    long_description=open('README.md').read(),
    author='Nicolas Hennion',
    author_email='nicolas@nicolargo.com',
    url='https://github.com/nicolargo/pycket',
    license="MIT",
    keywords="packet bits",
    packages=['pycket'],
    include_package_data=True,
    # data_files=data_files,
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)
