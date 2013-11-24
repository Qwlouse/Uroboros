#!/usr/bin/python
# coding=utf-8
from __future__ import division, print_function, unicode_literals

import unittest

from extractor import extract_imports

SIMPLE_IMPORT_STATEMENTS = \
    [("", []),
     ("#import justacomment", []),
     ("'import justastring'", []),
     ("import __future__", []),
     ("import __future__ as __past__", []),
     ("import __future__, re", [(1, 're', None, None)]),
     ("import re", [(1, 're', None, None)]),
     ("import time", [(1, 'time', None, None)]),
     ("import numpy as np", [(1, 'numpy', None, 'np')]),
     ("import sys, os, copy", [(1, 'sys', None, None),
                               (1, 'os', None, None),
                               (1, 'copy', None, None)]),
     ("import time as tme, copy as cpy", [(1, 'time', None, 'tme'),
                                          (1, 'copy', None, 'cpy')])
     ]


FROM_IMPORT_STATEMENTS = \
    [("from __future__ import division", []),
     ("from __future__ import division, print_function", []),
     ("from __future__ import division as div", []),

     ("from copy import deepcopy", [(1, 'copy', 'deepcopy', None)]),
     ("from copy import copy, deepcopy", [(1, 'copy', 'copy', None),
                                          (1, 'copy', 'deepcopy', None)]),
     ("from os import path as p", [(1, 'os', 'path', 'p')]),

     ("from foo.bar import baz", [(1, 'foo.bar', 'baz', None)]),
     ("from foo.bar import baz as zab", [(1, 'foo.bar', 'baz', 'zab')]),

     ("from .stuff import math", [(1, '.stuff', 'math', None)]),
     ("from .stuff import copy as cpy", [(1, '.stuff', 'copy', 'cpy')]),
     ("from ..stuff import foo as bar", [(1, '..stuff', 'foo', 'bar')]),
     ("from .. import stuff as stf", [(1, '..', 'stuff', 'stf')]),
     ("from ..foo.bar import baz as zab", [(1, '..foo.bar', 'baz', 'zab')]),


     ]


class ExtractorTest(unittest.TestCase):
    def test_extract_simple_imports(self):
        for stmt, modules in SIMPLE_IMPORT_STATEMENTS:
            imports = extract_imports(stmt)
            self.assertEqual(imports, modules)

    def test_extract_simple_imports_from_file(self):
        from .testfiles import simple_imports
        with open(simple_imports.__file__, 'r') as f:
            source = f.read()
        imports = extract_imports(source)
        self.assertEqual(imports, simple_imports.EXPECTED)

    def test_extract_from_imports(self):
        for stmt, modules in FROM_IMPORT_STATEMENTS:
            imports = extract_imports(stmt)
            self.assertEqual(imports, modules)

