#!/usr/bin/python
# coding=utf-8

from __future__ import division, print_function, unicode_literals

from b import ba
from b import bb
from b import bc  # package has precedence

import b.ba as bba
import b.bb as bbb
import b.bc as bbc  # package has precedence

for m in [ba, bb, bc, bba, bbb, bbc]:
    print(m)