#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys


from setuptools import setup


APP_NAME = 'dirsnap'
APP_SCRIPT = './_dirsnap'
VERSION = '0.0.2'

required = ['requests']

settings = dict()

# Publish Helper.
if sys.argv[-1] == 'publish':
    os.system('python setup.py sdist upload')
    sys.exit()

settings.update(
    name=APP_NAME,
    version=VERSION,
    description='Takes a snapshot of a directory, uploads to a public URL.',
    long_description=open('README.rst').read(),
    author='Kenneth Reitz',
    author_email='me@kennethreitz.com',
    url='https://github.com/kennethreitz/dirsnap',
    packages= ['dirsnap',],
    install_requires=required,
    license='BSD',
    classifiers=(
        # 'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python',
        # 'Programming Language :: Python :: 2.5',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
    ),
    entry_points={
        'console_scripts': [
            'dirsnap = dirsnap.cli:main',
        ],
    }
)



setup(**settings)
