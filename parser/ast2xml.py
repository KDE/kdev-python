#!/usr/bin/env python

import ast
from lxml import etree
from io import BytesIO

import sys

plain_types = (type(0), type(""), type(0.0), type(False), type(None))
list_type = type([])

class ASTSerializer(ast.NodeVisitor):
    def __init__(self, xf):
        self.xf = xf

    def generic_visit(self, node):
        name = type(node).__name__
        attrs = {k: getattr(node, k) for k in node._fields} if hasattr(node, "_fields") else dict()
        plain_attrs = {k: str(v) for k, v in attrs.items() if type(v) in plain_types}
        other_attrs = {k: v for k, v in attrs.items() if type(v) not in plain_types}
        with xf.element(name, **plain_attrs) as elem:
            for attrName, attrValue in other_attrs.items():
                with xf.element(attrName):
                    if type(attrValue) == list_type:
                        for node in attrValue:
                            self.generic_visit(node)
                    else:
                        self.generic_visit(attrValue)


with open(sys.argv[1], "r") as fp:
    text = fp.read()

m = ast.parse(text)

f = BytesIO()
with etree.xmlfile(f) as xf:
    v = ASTSerializer(xf)
    v.visit(m)
print(f.getvalue().decode('utf-8'))
