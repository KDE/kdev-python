#!/usr/bin/env python2.6

import ast
from xml.dom.minidom import Document
import types

class NodeContainer():
    identifier = 0
    node = None
    
    def __init__(self, node):
        self.node = node

class KDevelopNodeVisitor(ast.NodeVisitor):
    xmlrepr = Document()
    basenode = None
    currentnode = None
    nodecnt = 0
    searching = []
    
    def __init__(self, *arg, **args):
        super(KDevelopNodeVisitor, self).__init__(*arg, **args)
        self.basenode = self.xmlrepr.createElement("pythonast")
        self.xmlrepr.appendChild(self.basenode)
        self.currentnode = self.basenode
        
    def generic_visit(self, node):
        self.nodecnt += 1
        
        node_xmlrepr = self.xmlrepr.createElement(node.__class__.__name__ + "Node")
        node_xmlrepr.setAttribute('nodecnt', str(self.nodecnt))
        self.currentnode.appendChild(node_xmlrepr)
        
        save_currentnode = self.currentnode
        self.currentnode = node_xmlrepr
        
        fields = list(node._attributes)
        fields.extend(list(node._fields))
        
        searching_locally = []
        for field in fields:
            value = getattr(node, field)
            if type(value) not in [types.IntType, types.StringType]:
                search = NodeContainer(value)
                self.searching.append(search)
                continue
            node_xmlrepr.setAttribute(field.lower(), str(value))

        super(KDevelopNodeVisitor, self).generic_visit(node)
        
        for field in fields:
            value = getattr(node, field)
        
        self.currentnode = save_currentnode

f = open('/home/sven/test.py').read()
v = KDevelopNodeVisitor()
v.visit(ast.parse(f))
print v.xmlrepr.toprettyxml(indent = "  ")
