#!/usr/bin/env python2.7
# This file is part of KDevelop
# Copyright 2011 by Victor Varvariuc <victor.varvariuc@gmail.com>

from xml.dom import minidom


def indentCode(code, level):
    return '\n'.join('    ' * level + line for line in code.splitlines())


def parseEnum(enumNode, enumName, className = ''):
    '''Parse Enum node and return its string representation.'''
    enumMembers = []
    for node in enumNode.childNodes:
        if node.nodeType == node.ELEMENT_NODE:
            if node.nodeName == 'EnumMember':
                enumMember = node.attributes['name'].value
                if enumMember.startswith(className + '.'):
                    enumMember = enumMember[len(className) + 1:]
                if enumMember == 'None':
                    enumMember = '__kdevpythondocumentation_builtin_None'
                enumMembers.append(enumMember)
            else:
                print 'Unknown node in Enum %s.%s: %s' % (className, enumName, node.nodeName)
    text = ''
    for enumMember in enumMembers:
        text += '%s = int() # %s.%s enum\n' % (enumMember, className, enumName)
    return text


def parseFunction(functionNode, funcName, className = ''):
    '''Parse Function node and return its string representation.'''
    params = []
    retType = 'None'
    namesUsed = []
    for node in functionNode.childNodes:
        if node.nodeType == node.ELEMENT_NODE:
            if node.nodeName == 'Argument':
                argType = node.attributes['typename'].value
                try:
                    argName = '*args' if argType == '...' else '_' + node.attributes['name'].value
                except KeyError:
                    retType = argType
                else:
                    if argName not in namesUsed:
                        params.append((argType, argName))
                    else:
                        print "adjusting arg name:", argName
                        argName = argName + '_'
                        params.append((argType, argName))
                    namesUsed.append(argName)
            else:
                print 'Unknown node in function %s.%s: %s' % (className, funcName, node.nodeName)

    descr = 'abstract ' if 'abstract' in functionNode.attributes.keys() else ''
    descr += '%s %s.%s(%s)' % (retType, className, funcName,
                ', '.join('%s %s' % p for p in params))

    if retType == 'None':
        pass # leave it like this
    elif retType.startswith('list-of-'):
        retType = '[' + retType[8:] + '()]'
    else:
        retType += '()'

    # prefix function arguments with '_' to deal with reserved Python keywords
    text = 'def %s(%s):\n    """%s"""\n    return %s' % (funcName, ', '.join(param[1] for param in params), descr, retType)
    return text


def parseClass(classNode):
    '''Parse Class node.'''
    try:
        parentClasses = classNode.attributes['inherits'].value.split()
    except KeyError:
        parentClasses = []
    className = classNode.attributes['name'].value
    text = 'class %s(%s):\n    """"""\n' % (className, ', '.join(parentClasses))
    for node in classNode.childNodes:
        if node.nodeType == node.ELEMENT_NODE:
            name = node.attributes['name'].value
            if name.startswith(className + '.'):
                name = name[len(className) + 1 :]
            if node.nodeName == 'Member':
                text += '    %s = None # %s member\n' % (name, node.attributes['typename'].value)
            elif node.nodeName == 'Function':
                if name not in ('exec', 'print'): # skip this invalid for Python name
                    text += indentCode(parseFunction(node, name, className), 1) + '\n'
            elif node.nodeName == 'Enum':
                text += indentCode(parseEnum(node, name, className), 1) + '\n\n'
            else:
                print 'Unknown node in class %s: %s' % (className, node.nodeName)
    return text


files = ['QtGuimod.xml', 'QtCoremod.xml']
for filename in files:
    dom = minidom.parse(filename)

    module = dom.firstChild
    assert module.nodeName == 'Module'
    moduleName = module.attributes['name'].value
    print 'Module name:', moduleName

    stats = {}

    with open(moduleName + '.py', 'w') as file:
        for node in module.childNodes:
            if node.nodeType != node.ELEMENT_NODE:
                continue # skip non element nodes
            nodeName = node.nodeName
            stats[nodeName] = stats.setdefault(nodeName, 0) + 1 # stats
            if nodeName == 'Class':
                file.write(parseClass(node) + '\n\n')
            elif nodeName == 'Function':
                file.write(parseFunction(node, node.attributes['name'].value) + '\n\n')
            elif nodeName == 'Member':
                file.write('%s = None # %s member\n\n' % (node.attributes['name'].value, node.attributes['typename'].value))
            else:
                print 'Unknown node:', nodeName

    print 'Stats:', stats
