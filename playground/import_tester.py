#!/usr/bin/python
# coding=utf-8

from __future__ import division, print_function, unicode_literals

import sys       # builtin
import a         # file
import b         # package
import c         # package has precedence over file
import warnings  # !2.7: builtin has precedence!
                 # !3.2: package has precedence!
import time      # builtin has precedence over file
import numpy     # file has precedence over 3rd party module
import nose      # package has precedence over 3rd party module

import playground.c as pc # package has precedence over file
import playground.warnings as pwarn  # package
import playground.time as ptime      # file


for m in [sys, a, b, c, warnings, time, numpy, nose, pc, pwarn, ptime]:
    print(m)
