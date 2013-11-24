#!/usr/bin/python
# coding=utf-8
from __future__ import division, print_function, unicode_literals

import unittest

from extractor import extract_imports


class ExtractorTest(unittest.TestCase):
    def test_extract_simple_imports(self):
        statements = [
            ("import re", ['re']),
            ("import time", ['time']),
            ("import numpy as np", ['numpy']),
            ("import sys, os, copy", ['sys', 'os', 'copy'])
        ]
        for stmt, modules in statements:
            imports = extract_imports(stmt)
            self.assertEqual(imports, modules)
