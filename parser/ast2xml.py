#!/usr/bin/env python

import ast
from lxml import etree
from io import BytesIO

import sys

plain_types = (type(0), type(""), type(b""), type(0.0), type(False), type(None))
list_type = type([])

class ASTSerializer(ast.NodeVisitor):
    def __init__(self, xf):
        self.xf = xf

    def generic_visit(self, node):
        name = type(node).__name__
        attrs = {k: getattr(node, k) for k in node._fields} if hasattr(node, "_fields") else dict()
        if hasattr(node, "col_offset"):
            attrs["col_offset"] = node.col_offset
            attrs["lineno"] = node.lineno
        if name == "Constant":
            attrs["constant_type"] = type(node.value).__name__
        if name == "BinOp":
            attrs["op"] = type(node.op).__name__
        plain_attrs = {k: str(v) for k, v in attrs.items() if type(v) in plain_types}
        non_plain_attrs = {k: v for k, v in attrs.items() if type(v) not in plain_types}
        with xf.element(name, **plain_attrs) as elem:
            for attr, attr_val in non_plain_attrs.items():
                if attr == "ctx":
                    continue
                if type(attr_val) == list_type:
                    with xf.element(attr) as list_name_elem:
                        for entry in attr_val:
                            self.generic_visit(entry)
                elif attr_val is None:
                    pass
                elif issubclass(type(attr_val), ast.AST) or type(attr_val).__name__ == "ellipsis":
                    with xf.element(attr) as name_elem:
                        self.generic_visit(attr_val)
                else:
                    print(attr, attr_val, type(attr_val))
                    assert False

with open(sys.argv[1], "r") as fp:
    text = fp.read()

m = ast.parse(text)
m = ast.fix_missing_locations(m)

f = BytesIO()
with etree.xmlfile(f) as xf:
    v = ASTSerializer(xf)
    v.visit(m)
print(f.getvalue().decode('utf-8'))
