#!/usr/bin/python
# coding=utf-8
"""
This file conflicts with the builtin package 'time'.
It is here to serve as a test for the locator.
It should not be found though, because builtins take precedence over files.
"""
from __future__ import division, print_function, unicode_literals

assert False