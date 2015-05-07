#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#
# This file is part of KDevelop
# Copyright 2010 Sven Brauch <svenbrauch@googlemail.com>
# Licensed under the GNU GPL
#

# This script once was used for parsing documents; that implementation is long gone.
# It's just kept for looking at the AST created by some code quickly; you can do this:
# echo 'foo = baz.bar(3, "str")' |./pythonpythonparser.py
# or similar to quickly see the AST for that code.

import ast
from xml.dom.minidom import Document
from lxml import etree
import types
import sys
import re

class KDevelopNodeVisitor(ast.NodeVisitor):
    basenode = etree.Element("pythonast")
    currentnode = None
    nodecnt = 0
    childNodeMap = {}
    
    def __init__(self, *arg, **args):
        super(KDevelopNodeVisitor, self).__init__(*arg, **args)
        self.currentnode = self.basenode
    
    def generic_visit(self, node):
        self.nodecnt += 1
        
        #self.childNodeMap[self.nodecnt] = node
        self.childNodeMap[node] = self.nodecnt
        
        node_xmlrepr = etree.Element(node.__class__.__name__ + "Ast")
        node_xmlrepr.set('nodecnt', str(self.nodecnt))
        self.currentnode.append(node_xmlrepr)
        
        save_currentnode = self.currentnode
        self.currentnode = node_xmlrepr
        
        fields = list(node._attributes)
        fields.extend(list(node._fields))
        
        searching_locally = []
        for field in fields:
            value = getattr(node, field)
            if type(value) not in [type(0), type(""), type(0.0), type(False)]:
                continue
            try:
                node_xmlrepr.set(field.lower(), str(value))
            except:
                sys.stderr.write("Warning: Invalid string literal replaced by empty string!\n")
                node_xmlrepr.set(field.lower(), "")


        super(KDevelopNodeVisitor, self).generic_visit(node)
        
        key = ''
        for field in fields:
            multiple_keys = []
            value = getattr(node, field)
            if type(value) not in [type(0), type(""), type(0.0), type(False)]:
                if type(value) == type([]):
                    for currentValue in value:
                        try:
                            multiple_keys.append(str(self.childNodeMap[currentValue]))
                        except KeyError:
                            sys.stderr.write("Warning: missing key on node " + str(node) + "\n")
                            multiple_keys.append('')
                    key = ','.join(multiple_keys)
                    node_xmlrepr.set("NRLST_" + field.lower(), str(key))
                else:
                    try:
                        key = self.childNodeMap[value]
                    except KeyError:
                        key = ''
                    node_xmlrepr.set("NR_" + field.lower(), str(key))
                
                
        self.currentnode = save_currentnode

f = sys.stdin.read()
v = KDevelopNodeVisitor()
try:
    parsetree = ast.parse(f)
except Exception as e:
    try:
        sys.stderr.write(str(e.lineno) + ':::' + str(e.offset))
        sys.stderr.write(":::" + str(type(e)).replace('<type \'exceptions.', '').replace('\'>', '') + ':::' + str(e.msg) + ": \"" + str(e.text).replace("\n", "") + "\"")
    except:
        sys.stderr.write('?:::?:::'+str(e)+':::?')
else:
    v.visit(parsetree)
    print(str(etree.tostring(v.basenode, xml_declaration=True, pretty_print=True, encoding='UTF-8')).replace('\\n', '\n'))
