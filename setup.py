#!/usr/bin/env python

from setuptools import setup

setup(
    name='altmetric',
    version='1.0',
    description='Altmetric API v1 wrapper for Python.',
    long_description=open('README.rst').read(),
    author='Lars Holm Nielsen',
    url='https://github.com/lnielsen-cern/python-altmetric',
    packages=['altmetric'],
    download_url='http://pypi.python.org/pypi/altmetric/',
    keywords='altmetric api wrapper export',
    zip_safe=True,
    install_requires=['simplejson', 'requests'],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)
