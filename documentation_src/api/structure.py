#!/usr/bin/env python

import types
from lxml import etree

class Class():
    def __init__(self, name):
        self.name = name
        self.children = []
        self.baseClasses = []
    
    def __repr__(self):
        return "<Class ('%s') : %s>" % ( self.name, str(self.baseClasses) )
    
    def setInheritsFrom(self, nameOrList):
        if type(nameOrList) == types.ListType:
            self.baseClasses.extend(nameOrList)
        else:
            self.baseClasses.append(nameOrList)
    
    def addMethod(self, functionObject):
        self.children.append(functionObject)
    
    def addMember(self, member):
        self.children.append(member)
    
    def toXml(self):
        classNode = etree.Element("Class", name = str(self.name), inherits = ' '.join(self.baseClasses))
        for child in self.children:
            classNode.append(child.toXml())
        return classNode
    
class Function():
    def __init__(self, name):
        self.name = name
        self.arguments = []
        self.returnType = "None"
    
    def __repr__(self):
        return "<Function ('%s', %s) :: %s>" % ( self.name, str(self.arguments), self.returnType )
    
    def setReturnType(self, returnType):
        self.returnType = returnType
    
    def addArgument(self, argObject):
        self.arguments.append(argObject)
    
    def toXml(self):
        functionNode = etree.Element("Function", name = str(self.name))
        for arg in self.arguments:
            functionNode.append(arg.toXml())
        functionNode.append(etree.Element("Argument", dir = "out", typename = str(self.returnType)))
        return functionNode

class Argument():
    def __init__(self, name):
        self.name = name
        self.type = "None"
        self.defaultValue = None
    
    def __repr__(self):
        return "<Argument ('%s' = %s)>" % ( self.name, str(self.defaultValue) )
    
    def setType(self, type):
        self.type = type
    
    def setDefaultValue(self, defaultValue):
        self.defaultValue = str(defaultValue)
    
    def toXml(self):
        return etree.Element("Argument", name = str(self.name), typename = str(self.type))

class Module():
    def __init__(self, name):
        self.name = name
        self.children = []
    
    def __repr__(self):
        return "<Module ('%s')>" % ( self.name )
    
    def addChild(self, arg):
        self.children.append(arg)
    
    def toXml(self):
        root = etree.Element("root")
        for child in self.children:
            root.append(child.toXml())
        return root
    
    def toString(self):
        return etree.tostring(self.toXml(), pretty_print = True)

class Member():
    def __init__(self, name):
        self.name = name
        self.type = "None"
    
    def __repr__(self):
        return "<Member ('%s')>" % ( self.name )
    
    def setType(self, type):
        self.type = type
        
    def toXml(self):
        return etree.Element("Member", name = str(self.name), typename = str(self.type))
        
        