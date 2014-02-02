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
    # step 1: Builtins
    if module_name in BUILTINS:
        return '__builtin__', False

    # step 2: local files and packages
    modparts = module_name.split('.')
    current_dir = os.path.abspath(path)
    found = True
    for modpart in modparts[:-1]:
        dirname = os.path.join(current_dir, modpart)
        if os.path.exists(dirname) and os.path.isdir(dirname) and\
                os.path.exists(os.path.join(dirname, '__init__.py')):
            current_dir = dirname
        else:
            found = False
            break

    if found:
        filename = os.path.abspath(os.path.join(current_dir, modparts[-1],
                                                '__init__.py'))
        if os.path.exists(filename):
            return _postprocess_location(filename), True

        filename = os.path.join(current_dir, modparts[-1] + '.py')
        if os.path.exists(filename):
            return _postprocess_location(filename), True



    # step 3: 3rd party modules
    try:
        f, filename, _ = imp.find_module(module_name)
        if f:
            f.close()
        #local = filename.startswith(path)
        return _postprocess_location(filename), False
    except ImportError:
        pass
