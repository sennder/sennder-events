# -*- coding: utf-8 -*-
import os
from setuptools import setup, find_packages


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


VERSION = '0.0.2'

setup(
    name='sennder-events',
    version=VERSION,
    description="Sennder Events.",
    long_description=read('README.md'),
    classifiers=[
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Development Status :: 3 - Alpha',
        'Operating System :: OS Independent',
    ],
    keywords='',
    author='Konstantin Schubert',
    author_email='konstantin.schubert@sennder.com',
    packages=find_packages(exclude=("tests",)),
    install_requires=[
        'requests>=2.13,<2.14',
        'djangorestframework>=3.5.4,<3.6',
    ],
    include_package_data=True,
    zip_safe=True,
)
