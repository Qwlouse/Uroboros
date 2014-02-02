#!/usr/bin/python
# coding=utf-8
"""
This is a file to be analysed for imports by the extractor during the unittests.
It imports a lot of modules using the "from .. import ..." form, and
EXPECTED is a list of the expected outputs of the extractor for this file.
"""
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
    (10, 'os', 'path', None),
    (11, 'os.path', 'isdir', None),
    (12, 'os.path', 'exists', None),
    (12, 'os.path', 'join', None),
    (13, 're', 'match', None),
    (14, 'unittest', 'case', None),

    (16, 'os', 'path', 'pth'),
    (17, 'os.path', 'join', 'j'),
    (18, 'os.path', 'isdir', 'isd'),
    (18, 'os.path', 'exists', 'ex')
]