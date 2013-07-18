#!/usr/bin/env python
# -*- coding:utf-8 -*-
from setuptools import setup

setup(
    name='gallery-file-upload',
    version='0.1',
    description='Gallery File Upload based on jQuery File Upload integration for Opps CMS',
    classifiers=classifiers,
    author='Rael Max',
    author_email='contato@raelmax.com',
    download_url="https://github.com/raelmax/gallery-file-upload/tarball/master",
    include_package_data=True,
    package_data={
        'fileupload': ['templates/*', 'templatetags/*', 'static/*']
    }
)
