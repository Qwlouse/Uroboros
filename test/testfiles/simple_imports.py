#!/usr/bin/python
# coding=utf-8
"""
This is a file to be analysed for imports by the extractor during the unittests.
It imports a lot of modules using the "import ..." form, and
EXPECTED is a list of the expected outputs of the extractor for this file.

This is the docstring for this file. So nothing in here should count as an
import:
import foo
import bar as baz
"""

import __future__

import sys
import os, copy, time

import time as tme, copy as cpy

import hashlib,\
       math as m


EXPECTED = [
    #(10, '__future__', None) # future imports should be ignored
    (16, None, 'sys', None),
    (17, None, 'os', None),
    (17, None, 'copy', None),
    (17, None, 'time', None),
    (19, None, 'time', 'tme'),
    (19, None, 'copy', 'cpy'),
    (21, None, 'hashlib', None),
    (21, None, 'math', 'm')          # the line containing the import counts
]

EXPECTED_LOCATIONS = [
    (16, 'sys', '__builtin__'),
    (17, 'os', '__builtin__'),
    (17, 'copy', '__builtin__'),
    (17, 'time', '__builtin__'),
    (19, 'time', '__builtin__'),
    (19, 'copy', '__builtin__'),
    (21, 'hashlib', '__builtin__'),
    (21, 'math', '__builtin__')
]