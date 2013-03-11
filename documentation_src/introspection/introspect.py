#!/usr/bin/env python
# -*- Coding:utf-8 -*-

# Copyright 2013 by Sven Brauch <svenbrauch@googlemail.com>
# License: GNU GPL v3 or later
# The script output is not copyrighted, use it for whatever you want.

# WARNING: This script does things which can cause bad stuff to happen
# to your system in case you execute it on a module which has been
# engineered to be mailicious.
# I thus recommend to run this script as a user with minimal privileges
# (i.e. not as yourself), or even in a chroot.
# In any case, I'm not responsible for any damage caused by this script.

# This script will dump a SINGLE MODULE to a python "header" file.
# It will read one module, and give you one output file.
# Any submodules of the imported object (anything with type "module")
# will be ignored by this script, if you want to dump those,
# you will have to manually (or with a script) generate a directory
# structure and re-run this script.

import os
import sys
import types

def indent(code, depth=4):
    code = code.split('\n')
    code = [" "*depth + line for line in code]
    return '\n'.join(code)

def clearIndent(code):
    code = code.split('\n')
    code = [line.strip() for line in code]
    return '\n'.join(code)

class ModuleDumper:
    def __init__(self, module):
        self.module = module
        self.code = str()
        self.indentDepth = 0

    def increaseIndent(self):
        self.indentDepth += 4

    def decreaseIndent(self):
        self.indentDepth -= 4
        if self.indentDepth < 0:
            self.indentDepth = 0

    def emit(self, code):
        print(indent(code, self.indentDepth))

    def dump(self):
        for member in dir(self.module):
            dumper = dumperForObject(getattr(self.module, member), member, self)
            dumper.dump()

class ScalarDumper:
    def __init__(self, name, value, root):
        self.name = name
        self.value = value
        self.root = root

    def dump(self):
        value = type(self.value).__name__ + "()" if self.value is not None else "None"
        self.root.emit("{0} = {1}".format(self.name, value))

class FunctionDumper:
    def __init__(self, function, root):
        self.function = function
        self.root = root

    def dump(self):
        self.root.emit("def {0}():".format(self.function.__name__))
        self.root.increaseIndent()
        self.root.emit('"""' + self.function.__doc__ + '"""')
        self.root.emit("return None")
        self.root.decreaseIndent()

class ClassDumper:
    def __init__(self, klass, root):
        self.klass = klass
        self.root = root

    def dump(self):
        self.root.emit("class {0}:".format(self.klass.__name__))
        self.root.increaseIndent()
        for member in dir(self.klass):
            dumper = dumperForObject(getattr(self.klass, member), member, self.root)
            dumper.dump()
        self.root.decreaseIndent()

dumpers = {
    types.FunctionType: FunctionDumper,
    types.BuiltinFunctionType: FunctionDumper,
    types.BuiltinMethodType: FunctionDumper,
    type: ClassDumper
}
try:
    dumpers[types.ClassType] = ClassDumper # python 2
except:
    pass

def dumperForObject(object, memberName, root):
    try:
        return dumpers[type(object)](object, root)
    except:
        return ScalarDumper(memberName, object, root)

if __name__ == '__main__':
    try:
        dumper = ModuleDumper(__import__(sys.argv[1]))
    except IndexError:
        print("Usage: introspect.py <python_module_name>")
        exit(1)
    dumper.dump()
