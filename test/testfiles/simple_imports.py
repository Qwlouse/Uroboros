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
    (12, 'sys', None),
    (13, 'os', None),
    (13, 'copy', None),
    (13, 'time', None),
    (15, 'numpy', 'np'),
    (17, 'time', 'tme'),
    (17, 'copy', 'cpy'),
    (19, 'hashlib', None),
    (19, 'math', 'm')          # the line containing the import counts
]
