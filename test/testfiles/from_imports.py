#!/usr/bin/python
# coding=utf-8
from __future__ import division, print_function, unicode_literals

from os import path
from os.path import isdir
from os.path import exists, join
from re import match
from unittest import case

from os import path as pth
from os.path import join as j
from os.path import isdir as isd, exists as ex

EXPECTED = [
    (5, 'os', 'path', None),
    (6, 'os.path', 'isdir', None),
    (7, 'os.path', 'exists', None),
    (7, 'os.path', 'join', None),
    (8, 're', 'match', None),
    (9, 'unittest', 'case', None),

    (11, 'os', 'path', 'pth'),
    (12, 'os.path', 'join', 'j'),
    (13, 'os.path', 'isdir', 'isd'),
    (13, 'os.path', 'exists', 'ex')
]