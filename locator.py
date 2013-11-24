#!/usr/bin/python
# coding=utf-8
from __future__ import division, print_function, unicode_literals
import sys

BUILTINS = set(name for name in sys.builtin_module_names)

BUILTINS = BUILTINS.union(set(name.strip('_') for name in BUILTINS
                              if not name.startswith('__')))


def locate_module(module_name):
    if module_name in BUILTINS:
        return '__builtin__'

    return "filename"