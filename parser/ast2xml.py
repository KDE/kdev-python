#!/usr/bin/env python

import ast
from io import BytesIO
import base64

import sys

plain_types = (type(0), type(""), type(b""), type(0.0), type(False), type(None))
list_type = type([])

class XmlElement:
    def __init__(self, buf, name, attrs):
        self.buf = buf
        self.name = name
        self.attrs = attrs

    def writestr(self, s):
        self.buf.write(s.encode("utf-8"))

    def __enter__(self):
        self.writestr(f'<{self.name}')
        for k, v in self.attrs.items():
            self.writestr(f' {k}="{v}"')
        self.writestr('>')
        return self

    def __exit__(self, type, value, tb):
        self.writestr(f"</{self.name}>")


class XmlStreamWriter:
    def __init__(self, f):
        self.buf = f
        self.buf.write(b'<?xml version="1.0"?>')

    def __enter__(self):
        return self

    def __exit__(self, type, value, tb):
        pass

    def element(self, name, attrs=dict()):
        return XmlElement(self.buf, name, attrs)


class ASTSerializer(ast.NodeVisitor):
    def __init__(self, xf):
        self.xf = xf

    def generic_visit(self, node):
        if node is None:
            return
        name = type(node).__name__
        attrs = {k: getattr(node, k) for k in node._fields} if hasattr(node, "_fields") else dict()
        if hasattr(node, "col_offset"):
            attrs["col_offset"] = node.col_offset
            attrs["lineno"] = node.lineno
            attrs["end_col_offset"] = node.end_col_offset
            attrs["end_lineno"] = node.end_lineno
        if name == "Constant":
            attrs["constant_type"] = type(node.value).__name__
            if type(node.value) == str:
                attrs["value"] = base64.b64encode(attrs["value"].encode("utf-8")).decode("ascii")
            if type(node.value) == bytes:
                attrs["value"] = base64.b64encode(attrs["value"]).decode("ascii")
        if name == "BinOp":
            attrs["op"] = type(node.op).__name__
        if name == "BoolOp":
            attrs["op"] = type(node.op).__name__
        if name == "UnaryOp":
            attrs["op"] = type(node.op).__name__
        plain_attrs = {k: str(v) for k, v in attrs.items() if type(v) in plain_types and v is not None}
        non_plain_attrs = {k: v for k, v in attrs.items() if type(v) not in plain_types and v is not None}
        with self.xf.element(name, plain_attrs) as elem:
            for attr, attr_val in non_plain_attrs.items():
                if attr == "ctx":
                    continue
                if type(attr_val) == list_type:
                    with self.xf.element(attr) as list_name_elem:
                        for entry in attr_val:
                            self.generic_visit(entry)
                elif attr_val is None:
                    pass
                elif type(attr_val).__name__ == "ellipsis":
                    pass
                elif issubclass(type(attr_val), ast.AST):
                    with self.xf.element(attr) as name_elem:
                        self.generic_visit(attr_val)
                else:
                    print(attr, attr_val, type(attr_val))
                    assert False

def doParse(code):
    try:
        m = ast.parse(code)
        m = ast.fix_missing_locations(m)
    except SyntaxError as syntaxError:
        return f"""SyntaxError
{syntaxError.filename}
{syntaxError.lineno}
{syntaxError.offset}
{syntaxError.msg}
"""
    except Exception as err:
        import traceback
        print(traceback.format_exc())
        return f"InternalError: {str(err)}, {type(err)}"

    f = BytesIO()
    #from lxml import etree
    #with etree.xmlfile(f) as xf:
    with XmlStreamWriter(f) as xf:
        v = ASTSerializer(xf)
        v.visit(m)

    return f.getvalue().decode('utf-8')

if __name__ == "__main__":
    with open(sys.argv[1], "r") as fp:
        text = fp.read()

    print(doParse(text))
