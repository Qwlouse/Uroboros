#!/usr/bin/python
# coding=utf-8
from __future__ import division, print_function, unicode_literals

from .simple_imports import EXPECTED as simple_expected

from ..utils import ensure_uncompiled_source

from ..testfiles.from_imports import EXPECTED as from_expected


EXPECTED = [
    (5, '.simple_imports', 'EXPECTED', 'simple_expected'),
    (7, '..utils', 'ensure_uncompiled_source', None),
    (9, '..testfiles.from_imports', 'EXPECTED', 'from_expected'),
]