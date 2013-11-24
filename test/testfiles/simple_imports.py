#!/usr/bin/python
# coding=utf-8
"""
This is the docstring for this file. So nothing in here should count as an
import:
import foo
import bar as baz
"""

import __future__

import sys
import os, copy, time

import numpy as np

import time as tme, copy as cpy

import hashlib,\
       math as m


EXPECTED = [
    #(10, '__future__', None) # future imports should be ignored
    (12, None, 'sys', None),
    (13, None, 'os', None),
    (13, None, 'copy', None),
    (13, None, 'time', None),
    (15, None, 'numpy', 'np'),
    (17, None, 'time', 'tme'),
    (17, None, 'copy', 'cpy'),
    (19, None, 'hashlib', None),
    (19, None, 'math', 'm')          # the line containing the import counts
]
