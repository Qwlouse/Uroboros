#!/usr/bin/python
# coding=utf-8
from __future__ import division, print_function, unicode_literals
import sys


def locate_module(module_name):
    if module_name in [name.strip('_') for name in sys.builtin_module_names]:
        return '__builtin__'

    return "filename"