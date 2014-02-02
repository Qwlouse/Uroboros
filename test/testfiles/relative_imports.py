#!/usr/bin/python
# coding=utf-8
"""
This is a file to be analysed for imports by the extractor during the unittests.
It imports a lot of modules using local imports and
EXPECTED is a list of the expected outputs of the extractor for this file.
"""
from __future__ import division, print_function, unicode_literals

from .simple_imports import EXPECTED as simple_expected

from ..utils import ensure_uncompiled_source

from ..testfiles.from_imports import EXPECTED as from_expected


EXPECTED = [
    (10, '.simple_imports', 'EXPECTED', 'simple_expected'),
    (12, '..utils', 'ensure_uncompiled_source', None),
    (14, '..testfiles.from_imports', 'EXPECTED', 'from_expected'),
]