#!/usr/bin/python
# coding=utf-8
"""
This is the docstring for this file. So nothing in here should count as an
import:
import foo
import bar as baz
"""
# future imports schould be ignored
from __future__ import division, print_function, unicode_literals

import sys
import os, copy, time

import numpy as np

import time as tme, copy as cpy


EXPECTED = [
    (12, 'sys', None),
    (13, 'os', None),
    (13, 'copy', None),
    (13, 'time', None),
    (15, 'numpy', 'np'),
    (17, 'time', 'tme'),
    (17, 'copy', 'cpy')
]
