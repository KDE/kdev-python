#!/usr/bin/env python2.6
# -*- coding: utf-8 -*-

#
# This file is part of KDevelop
# Copyright 2010 Sven Brauch <svenbrauch@googlemail.com>
# Licensed under the GNU GPL
#

import ast
from xml.dom.minidom import Document
from lxml import etree
import types
import sys

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
            if type(value) not in [types.IntType, types.StringType, types.FloatType, types.BooleanType]:
                continue
            node_xmlrepr.set(field.lower(), str(value))

        super(KDevelopNodeVisitor, self).generic_visit(node)
        
        key = ''
        for field in fields:
            multiple_keys = []
            value = getattr(node, field)
            if type(value) not in [types.IntType, types.StringType, types.FloatType, types.BooleanType]:
                if type(value) == types.ListType:
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
    v.visit(ast.parse(f))
except Exception as e:
    sys.stderr.write(str(e.lineno) + ':::' + str(e.offset))
    sys.stderr.write(":::" + str(type(e)).replace('<type \'exceptions.', '').replace('\'>', '') + ':::' + str(e.msg) + ": \"" + str(e.text).replace("\n", "") + "\"")
else:
    sys.stdout.write(etree.tostring(v.basenode, xml_declaration=True, pretty_print=True, encoding='UTF-8'))
