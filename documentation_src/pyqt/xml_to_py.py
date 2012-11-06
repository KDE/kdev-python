#!/usr/bin/env python2.7
# This file is part of KDevelop
# Copyright 2011 by Victor Varvariuc <victor.varvariuc@gmail.com>, Sven Brauch <svenbrauch@googlemail.com>

import sys
from xml.dom import minidom


class NoDefaultValue():
    '''Unique object for marking absence of a default value for a function argument.'''

def indentCode(code, level):
    '''Indent given source code.'''
    return '\n'.join('    ' * level + line for line in code.splitlines())

def getNodeNames(node):
    '''Return node name. Chop the beginning of the name if it starts with parent's prefix:
    QWidget.RenderFlags.__init__ -> __init__'''
    name = node.attributes['name'].value
    parentNode = node.parentNode
    if parentNode.nodeName == 'Enum': # for unem members name prefix is not enum's name, but its parent's
       parentNode = parentNode.parentNode
    
    parentName = []
    while parentNode.nodeName == 'Class':
        parentName.append(parentNode.attributes['name'].value)
        parentNode = parentNode.parentNode
    parentName = list(reversed(parentName))
    parentName = '.'.join(parentName) + '.'
    
    if name.startswith(parentName):
        return name[len(parentName):], name
    return name, name


def parseEnum(enumNode):
    '''Parse Enum node and return its source code.'''
    enumMembers = []
    enumName, enumFullName = getNodeNames(enumNode)
    for node in enumNode.childNodes:
        if node.nodeType == node.ELEMENT_NODE:
            if node.nodeName == 'EnumMember':
                #print getNodeNames(node)
                enumMemberName = getNodeNames(node)[0]
                if enumMemberName == 'None':
                    enumMemberName = '__kdevpythondocumentation_builtin_None'
                enumMembers.append(enumMemberName)
            else:
                print 'Unknown sub-node in Enum %s: %s' % (enumFullName, node.nodeName)
    text = '# Enum %s\n' % enumFullName
    for enumMember in enumMembers:
        text += '%s = 0\n' % enumMember
    return text


def parseFunction(functionNode):
    '''Parse Function node and return its code.'''
    params = []
    retType = 'void'
    funcName, funcFullName = getNodeNames(functionNode)
    for node in functionNode.childNodes:
        if node.nodeType == node.ELEMENT_NODE:
            if not node.hasAttribute('typename'):
                node.attributes['typename'] = 'unknown'
            if node.nodeName == 'Argument':
                argType = node.attributes['typename'].value
                try:
                    argName = '*args' if argType == '...' else node.attributes['name'].value
                except KeyError: # no `name` attribute - it's function return value type
                    retType = argType
                else:
                    try: # some arguments have default values
                        defaultValue = node.attributes['default'].value
                    except KeyError:
                        defaultValue = NoDefaultValue
                    params.append((argType, argName, defaultValue))
            else:
                print 'Unhandled sub-node type in function %s: %s' % (funcFullName, node.nodeName)

    descr = 'abstract ' if 'abstract' in functionNode.attributes.keys() else ''
    descr += 'static ' if 'static' in functionNode.attributes.keys() else ''

    namesUsed = set(['self', 'exec', 'print', 'from', 'in', 'def', 'if', 'for',
                     'while', 'return', 'raise', 'pass', 'global', 'del']) # reserved words which cannot be used as argument names
    if funcFullName in namesUsed:
        funcFullName += '_'
    
    # function parameters in description
    paramsStr = []
    for p in params:
        paramsStr.append('{} {}'.format(*p) if p[2] is NoDefaultValue else '{} {} = {}'.format(*p))
    descr += '%s %s(%s)' % (retType, funcFullName, ', '.join(paramsStr))

    # function parameters in function defintion
    paramsStr = ['self'] if functionNode.parentNode.nodeName == 'Class' else [] # add `self` first parameter for methods
    hadDefault = False # there has been a default argument previously
    for _, argName, defaultValue in params:
        while argName in namesUsed: # some function arguments have same names...
            print 'Adjusting arg name: `%s` in `%s`' % (argName, funcFullName) # http://www.riverbankcomputing.co.uk/static/Docs/PyQt4/html/qdatetime.html#QDateTime-5
            argName = argName + '_'
        namesUsed.add(argName)
        if defaultValue is NoDefaultValue and not hadDefault:
            paramsStr.append(argName)
        else:
            if defaultValue is NoDefaultValue or not defaultValue.replace('(','').replace(')','').isalnum():
                defaultValue = "None"
            paramsStr.append('{} = {}'.format(argName, defaultValue))
            hadDefault = True

    text = "def %s(%s):\n    '''%s'''\n" % (funcName, ', '.join(paramsStr), descr)
    if retType == 'void':
        return text # do not print `return None` statement
    if retType.startswith('list-of-'):
        retType = '[' + retType[8:] + '()]'
    else:
        retType += '()'

    return text + '    return %s' % retType


def parseClass(classNode):
    '''Parse Class node and return its api python code.'''
    className, classFullName = getNodeNames(classNode)
    try:
        parentClasses = classNode.attributes['inherits'].value.split()
    except KeyError:
        parentClasses = []
    text = 'class %s(%s):\n    """"""\n' % (className, ', '.join(parentClasses))
    for node in classNode.childNodes:
        if node.nodeType == node.ELEMENT_NODE:
            if node.nodeName == 'Member':
                text += '    %s = None # %s - member\n' % (getNodeNames(node)[0], node.attributes['typename'].value)
            elif node.nodeName == 'Function':
                name = getNodeNames(node)[0]
                if name not in ('exec', 'print'): # skip these invalid for Python names
                    text += indentCode(parseFunction(node), 1) + '\n'
            elif node.nodeName == 'Enum':
                text += indentCode(parseEnum(node), 1) + '\n\n'
            elif node.nodeName == 'Class':
                text += indentCode(parseClass(node), 1) + '\n'
            elif node.nodeName == 'Signal':
                text += '    %s = pyqtSignal() # %s - signal\n' % (getNodeNames(node)[0], node.attributes['sig'].value)
            else:
                print 'Unhandled sub-node type in class %s: %s' % (classFullName, node.nodeName)
    return text


def convertXmlToPy(inFilePath):
    print '\nConverting .xml PyQt4 module (%s) to .py' % inFilePath

    print 'Parsing xml...'
    dom = minidom.parse(inFilePath)

    module = dom.firstChild
    assert module.nodeName == 'Module'
    moduleName = module.attributes['name'].value
    print 'Module name:', moduleName

    outFilePath = moduleName + '.py'
    stats = {}

    with open(outFilePath, 'w') as file:
        file.write('class pyqtSignal():\n def connect(self, targetSignal): pass\n def emit(self, *args): pass\n')
        file.write('from QtCore import *\n\n')
        for node in module.childNodes:
            if node.nodeType != node.ELEMENT_NODE:
                continue # skip non element nodes
            nodeName = node.nodeName
            stats[nodeName] = stats.setdefault(nodeName, 0) + 1 # stats
            if nodeName == 'Class':
                file.write(parseClass(node) + '\n\n')
            elif nodeName == 'Function':
                if not 'extends' in node.attributes.keys(): # skip module level functions, which extend unpresent here class
                    file.write(parseFunction(node) + '\n\n')
            elif nodeName == 'Member':
                file.write('%s = None # %s member\n\n' % (getNodeNames(node)[0], node.attributes['typename'].value))
            elif nodeName == 'Enum':
                file.write(parseEnum(node) + '\n\n')
            else:
                print 'Unhandled node type in the module:', nodeName

    print 'Stats:', stats


files = sys.argv[1:] # ['QtGui', 'QtCore'] # modules to convert

for fileName in files:
    convertXmlToPy(fileName)
