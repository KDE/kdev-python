#!/usr/bin/env python2.6

import re

f = open('classes')
contents = f.read()
f.close()

r = re.findall(r'class KDEVPYTHONPARSER_EXPORT (?P<astname>\w+)Ast', contents)
r.sort()
for item in r:
    funcname = 'visit' + item
    astname = item + 'Ast'
    #print 'virtual void ' + funcname + '(' + astname + '* node);'
    #print 'virtual void ' + funcname + '(' + astname + '* node) { Q_UNUSED(node); };'
    #print 'case Ast::' + astname + 'Type:\t\t\t' + 'AstVisitor::' + funcname + '(dynamic_cast<' + astname + '>(node)); break;'
    print 'else if ( name == "' + astname.lower() +'" ) ast = new ' + astname + '();'