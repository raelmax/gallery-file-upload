#!/usr/bin/env python
# -*- coding:utf-8 -*-
from setuptools import setup

classifiers = ["Development Status :: 4 - Beta",
               "Intended Audience :: Developers",
               "License :: OSI Approved :: MIT License",
               "Operating System :: OS Independent",
               "Framework :: Django",
               'Programming Language :: Python',
               "Programming Language :: Python :: 2.7",
               "Operating System :: OS Independent",
               "Topic :: Internet :: WWW/HTTP :: Dynamic Content",
               'Topic :: Software Development :: Libraries :: Python Modules']

long_description = open('README.md').read()

setup(
    name='gallery-file-upload',
    version='0.1',
    long_description=long_description,
    classifiers=classifiers,
    keywords='Django Gallery File Upload',
    author='Rael Max',
    author_email='contato@raelmax.com',
    download_url="https://github.com/raelmax/gallery-file-upload/tarball/master",
    include_package_data=True,
    package_data={
        'fileupload': ['templates/*', 'templatetags/*', 'static/*']
    }
)
