#!/usr/bin/env python

import types
import xml.etree.ElementTree as etree

class Class():
    def __init__(self, name):
        self.name = name
        self.children = []
        self.baseClasses = []
    
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
        classNode = etree.Element("Class", name = self.name, inherits = ' '.join(self.baseClasses))
        for child in self.children:
            classNode.append(child.toXml())
        return classNode
    
class Function():
    def __init__(self, name):
        self.name = name
        self.arguments = []
        self.container = None
    
    def setReturnType(self, returnType):
        self.returnType = returnType
    
    def addArgument(self, argObject):
        self.arguments.append(argObject)
    
    def toXml(self):
        functionNode = etree.Element("Function", name = self.name)
        for arg in self.arguments:
            functionNode.append(arg.toXml())
        functionNode.append(etree.Element("Argument", dir = "out", typename = self.returnType))
        return functionNode
    
    def toString(self):
        return etree.tostring(self.toXml())

class Argument():
    def __init__(self, name):
        self.name = name
        self.type = None
    
    def setType(self, type):
        self.type = type
    
    def toXml(self):
        return etree.Element("Argument", name = self.name, typename = self.type)

class Module():
    def __init__(self, name):
        self.name = name
        self.children = []
    
    def toXml(self):
        root = etree.Element("root")
        for child in self.children:
            root.append(child.toXml())
        return root

class Member():
    def __init__(self, name):
        self.name = name
        self.type = None
    
    def setType(self, type):
        self.type = type
        
    def toXml(self):
        return etree.Element("Member", name = self.name, typename = self.type)
        
        