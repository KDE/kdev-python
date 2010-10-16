#!/usr/bin/env python2.6

import ast
from xml.dom.minidom import Document
import types
import sys

class KDevelopNodeVisitor(ast.NodeVisitor):
    xmlrepr = Document()
    basenode = None
    currentnode = None
    nodecnt = 0
    childNodeMap = {}
    
    def __init__(self, *arg, **args):
        super(KDevelopNodeVisitor, self).__init__(*arg, **args)
        self.basenode = self.xmlrepr.createElement("pythonast")
        self.xmlrepr.appendChild(self.basenode)
        self.currentnode = self.basenode
        
    def generic_visit(self, node):
        self.nodecnt += 1
        
        #self.childNodeMap[self.nodecnt] = node
        self.childNodeMap[node] = self.nodecnt
        
        node_xmlrepr = self.xmlrepr.createElement(node.__class__.__name__ + "Ast")
        node_xmlrepr.setAttribute('nodecnt', str(self.nodecnt))
        self.currentnode.appendChild(node_xmlrepr)
        
        save_currentnode = self.currentnode
        self.currentnode = node_xmlrepr
        
        fields = list(node._attributes)
        fields.extend(list(node._fields))
        
        searching_locally = []
        for field in fields:
            value = getattr(node, field)
            if type(value) not in [types.IntType, types.StringType, types.FloatType, types.BooleanType]:
                continue
            node_xmlrepr.setAttribute(field.lower(), str(value))

        super(KDevelopNodeVisitor, self).generic_visit(node)
        
        key = 'None'
        for field in fields:
            multiple_keys = []
            value = getattr(node, field)
            if type(value) not in [types.IntType, types.StringType, types.FloatType, types.BooleanType]:
                if type(value) == types.ListType:
                    for currentValue in value:
                        try:
                            multiple_keys.append(str(self.childNodeMap[currentValue]))
                        except KeyError:
                            multiple_keys.append('None')
                    key = ','.join(multiple_keys)
                    node_xmlrepr.setAttribute("NRLST_" + field.lower(), str(key))
                else:
                    try:
                        key = self.childNodeMap[value]
                    except KeyError:
                        key = 'None'
                    node_xmlrepr.setAttribute("NR_" + field.lower(), str(key))
                
                
        self.currentnode = save_currentnode

f = open(sys.argv[1]).read()
v = KDevelopNodeVisitor()
v.visit(ast.parse(f))
print v.xmlrepr.toprettyxml(indent = "    ")
