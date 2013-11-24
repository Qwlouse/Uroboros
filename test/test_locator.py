#!/usr/bin/python
# coding=utf-8
from __future__ import division, print_function, unicode_literals
import unittest


from locator import locate_module


def ensure_uncompiled_source(filename):
    if filename.endswith('.pyc') or filename.endswith('.pyo'):
        filename = filename[:-1]

    #assert filename.endswith('py'), "error: %s" % filename
    return filename

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


class LocatorTest(unittest.TestCase):
    def test_locate_builtin_modules(self):
        for module_name in BUILTIN_MODULES:
            self.assertEqual(locate_module(module_name), '__builtin__')

    def test_locate_builtin_modules_that_start_with_underscore(self):
        for module_name in BUILTIN_MODULES_WITH_UNDERSCORES:
            self.assertEqual(locate_module(module_name), '__builtin__')