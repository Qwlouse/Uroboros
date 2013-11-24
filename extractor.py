#!/usr/bin/python
# coding=utf-8
from __future__ import division, print_function, unicode_literals
import ast


class ImportExtractor(ast.NodeVisitor):
    def __init__(self):
        self.imports = []

    def visit_Import(self, node):
        self.imports.extend(a.name for a in node.names)
        super(ImportExtractor, self).generic_visit(node)


def extract_imports(source):
    tree = ast.parse(source)
    extractor = ImportExtractor()
    extractor.visit(tree)
    return extractor.imports
