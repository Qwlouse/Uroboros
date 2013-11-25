#!/usr/bin/python
# coding=utf-8
from __future__ import division, print_function, unicode_literals
import os
import unittest

from locator import locate_module
from test import utils
from test.testfiles import simple_imports, from_imports


BUILTIN_MODULES = ['array', 'ast', 'binascii', 'bisect', 'codecs',
                   'collections', 'errno', 'fcntl', 'functools', 'gc', 'grp',
                   'hashlib', 'imp', 'itertools', 'locale', 'marshal', 'math',
                   'operator', 'posix', 'pwd', 'random', 'select', 'signal',
                   'socket', 'spwd', 'sre', 'ssl', 'struct', 'symtable', 'sys',
                   'syslog', 'thread', 'time', 'unicodedata', 'warnings',
                   'weakref', 'xxsubtype', 'zipimport', 'zlib']

BUILTIN_MODULES_WITH_UNDERSCORES = ['__main__', '_ast', '_bisect', '_codecs',
                                    '_collections', '_functools', '_hashlib',
                                    '_locale', '_random', '_socket', '_sre',
                                    '_ssl', '_struct', '_symtable', '_warnings',
                                    '_weakref']

THIRD_PARTY_MODULES = [
    ("unittest", utils.ensure_uncompiled_source(unittest.__file__)),
]

THIS_PATH = os.path.dirname(__file__)

LOCAL_MODULES = [
    (('utils', THIS_PATH),
     (utils.ensure_uncompiled_source(utils.__file__), True)),
    (('testfiles.simple_imports', THIS_PATH),
     (utils.ensure_uncompiled_source(simple_imports.__file__), True)),
    (('testfiles.from_imports', THIS_PATH),
     (utils.ensure_uncompiled_source(from_imports.__file__), True)),
]


class LocatorTest(unittest.TestCase):
    def test_locate_builtin_modules(self):
        for module_name in BUILTIN_MODULES:
            self.assertEqual(locate_module(module_name, THIS_PATH),
                             ('__builtin__', False))

    def test_locate_builtin_modules_that_start_with_underscore(self):
        for module_name in BUILTIN_MODULES_WITH_UNDERSCORES:
            self.assertEqual(locate_module(module_name, THIS_PATH),
                             ('__builtin__', False))

    def test_locate_3rd_party_modules_returns_filename(self):
        for modname, filename in THIRD_PARTY_MODULES:
            self.assertEqual(locate_module(modname, THIS_PATH),
                             (filename, False))

    def test_locate_local_files(self):
        for (modname, path), (location, local) in LOCAL_MODULES:
            self.assertEqual(locate_module(modname, path), (location, local))

