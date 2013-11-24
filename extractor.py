#!/usr/bin/python
# coding=utf-8
from __future__ import division, print_function, unicode_literals
import ast


class ImportExtractor(ast.NodeVisitor):
    def __init__(self):
        self.imports = []

    def visit_Import(self, node):
        lineno = node.lineno
        #col_offset = node.col_offset
        import_aliases = [(lineno, a.name, None, a.asname) for a in node.names
                          if a.name != '__future__']  # ignore import __future__
        self.imports.extend(import_aliases)
        super(ImportExtractor, self).generic_visit(node)

    def visit_ImportFrom(self, node):
        lineno = node.lineno
        module = '.' * node.level + (node.module or '')
        if module != '__future__':
            # ignore import __future__
            #col_offset = node.col_offset
            import_aliases = [(lineno, module, a.name, a.asname)
                              for a in node.names]
            self.imports.extend(import_aliases)

        super(ImportExtractor, self).generic_visit(node)


def extract_imports(source):
    tree = ast.parse(source)
    extractor = ImportExtractor()
    extractor.visit(tree)
    return extractor.imports
