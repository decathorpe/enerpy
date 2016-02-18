#!/usr/bin/env python3

import os
from setuptools import setup

# Utility function to read the README file.
# Used for the long_description.  It's nice, because now 1) we have a top level
# README file and 2) it's easier to type in the README file than to put a raw
# string in below ...
def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "enerpy",
    version = "0.3.1",
    author = "Fabio Valentini",
    author_email = "decathorpe (at) gmail (dot) com",
    description = ("Gaussian error propagation and basic statistics library functions"),
    license = "GPLv2",
    keywords = "math statistics",
    url = "http://github.com/decathorpe/enerpy",
    packages=['enerpy'],
    long_description=read('README.md'),
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Topic :: Utilities",
        "License :: OSI Approved :: GPLv2",
    ],
)

