#!/usr/bin/python
# coding=utf-8
from __future__ import division, print_function, unicode_literals
import imp
import os
import sys

BUILTINS = set(name for name in sys.builtin_module_names)

BUILTINS = BUILTINS.union(set(name.strip('_') for name in BUILTINS
                              if not name.startswith('__')))


def locate_module(module_name, path=''):
    if module_name in BUILTINS:
        return '__builtin__', False

    f, filename, (suffix, mode, type) = imp.find_module(module_name)

    if os.path.isdir(filename):
        filename = os.path.join(filename, '__init__.py')

    return filename, False