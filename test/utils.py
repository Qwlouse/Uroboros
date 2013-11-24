#!/usr/bin/python
# coding=utf-8
from __future__ import division, print_function, unicode_literals


def ensure_uncompiled_source(filename):
    if filename.endswith('.pyc') or filename.endswith('.pyo'):
        filename = filename[:-1]

    #assert filename.endswith('py'), "error: %s" % filename
    return filename