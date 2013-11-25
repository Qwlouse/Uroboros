#!/usr/bin/python
# coding=utf-8
from __future__ import division, print_function, unicode_literals
import imp
import os
import sys

BUILTINS = set(name for name in sys.builtin_module_names)

BUILTINS = BUILTINS.union(set(name.strip('_') for name in BUILTINS
                              if not name.startswith('__')))


def _postprocess_location(filename):
    if os.path.isdir(filename):
        filename = os.path.join(filename, '__init__.py')
    return filename


def locate_module(module_name, path=''):
    if module_name in BUILTINS:
        return '__builtin__', False

    try:
        f, filename, (suffix, mode, type) = imp.find_module(module_name)
        if f:
            f.close()
        return _postprocess_location(filename), False
    except ImportError:
        pass

    # that means we have a local import at hand!
    # TODO: figure out what we have to consider
