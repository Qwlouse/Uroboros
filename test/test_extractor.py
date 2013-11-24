#!/usr/bin/python
# coding=utf-8
from __future__ import division, print_function, unicode_literals

import unittest

from extractor import extract_imports


class ExtractorTest(unittest.TestCase):
    def test_extract_simple_imports(self):
        statements = [
            ("", []),
            ("#import justacomment", []),
            ("'import justastring'", []),
            ("import __future__", []),  # ignore
            ("import __future__ as __past__", []),  # ignore
            ("import __future__, re", [(1, 're', None)]),
            ("import re", [(1, 're', None)]),
            ("import time", [(1, 'time', None)]),
            ("import numpy as np", [(1, 'numpy', 'np')]),
            ("import sys, os, copy", [(1, 'sys', None),
                                      (1, 'os', None),
                                      (1, 'copy', None)]),
            ("import time as tme, copy as cpy", [(1, 'time', 'tme'),
                                                 (1, 'copy', 'cpy')])

        ]
        for stmt, modules in statements:
            imports = extract_imports(stmt)
            self.assertEqual(imports, modules)

    def test_extract_simple_imports_from_file(self):
        from .testfiles import simple_imports
        with open(simple_imports.__file__, 'r') as f:
            source = f.read()
        imports = extract_imports(source)
        self.assertEqual(imports, simple_imports.EXPECTED)
