#!/usr/bin/env python

import ast
from lxml import etree
from io import BytesIO

plain_types = (type(0), type(""), type(0.0), type(False), type(None))
list_type = type([])

class ASTSerializer(ast.NodeVisitor):
    def __init__(self, xf):
        self.xf = xf

    def generic_visit(self, node):
        print("visiting node", node)
        name = type(node).__name__
        attrs = {k: getattr(node, k) for k in node._fields}
        plain_attrs = {k: str(v) for k, v in attrs.items() if type(v) in plain_types}
        other_attrs = {k: v for k, v in attrs.items() if type(v) not in plain_types}
        print("\tplain attrs:", plain_attrs)
        print("\tother attrs:", other_attrs)
        with xf.element(name, **plain_attrs) as elem:
            for attrName, attrValue in other_attrs.items():
                with xf.element(attrName):
                    if type(attrValue) == list_type:
                        print("visiting list name", attrName)
                        print(attrValue)
                        for node in attrValue:
                            self.generic_visit(node)
                    else:
                        self.generic_visit(attrValue)


m = ast.parse("""
a = 3
b = 5
def func(x: int, *args, **kwargs):
    c = x
    if 3 < 5 < 7:
        yield
    if c is not None:
        return {x: v for x, v in c}
""")

f = BytesIO()
with etree.xmlfile(f) as xf:
    v = ASTSerializer(xf)
    v.visit(m)
print(f.getvalue().decode('utf-8'))
