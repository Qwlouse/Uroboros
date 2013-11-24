#!/usr/bin/python
# coding=utf-8
"""
This module contains the extract_imports method to get all the import statements
from a python source file, by walking through the AST for that file.
"""
from __future__ import division, print_function, unicode_literals
import ast


#noinspection PyPep8Naming
class ImportExtractor(ast.NodeVisitor):
    def __init__(self):
        self.imports = []

    def visit_Import(self, node):
        line_nr = node.lineno
        import_aliases = [(line_nr, None, a.name, a.asname) for a in node.names
                          if a.name != '__future__']  # ignore import __future__
        self.imports.extend(import_aliases)
        super(ImportExtractor, self).generic_visit(node)

    def visit_ImportFrom(self, node):
        line_nr = node.lineno
        module = '.' * node.level + (node.module or '')
        if module != '__future__':
            import_aliases = [(line_nr, module, a.name, a.asname)
                              for a in node.names]
            self.imports.extend(import_aliases)

        super(ImportExtractor, self).generic_visit(node)


def extract_imports(source):
    """
    Extract all import statements from given sourcecode. For every found import
    it will return one tuple of the form (line_nr, parent, importee, alias):

    "1: from parent import importee as alias" => (1, parent, importee, alias)
    "2: import importee as alias"             => (2, None,   importee, alias)

    All statements importing from __future__ are ignored.

    :param source: python sourcecode as string
    :return: list of tuples of the form (line_nr, parent, importee, alias)
    """
    tree = ast.parse(source)
    extractor = ImportExtractor()
    extractor.visit(tree)
    return extractor.imports
