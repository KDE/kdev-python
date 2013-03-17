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
import inspect

def debugmsg(message):
    sys.stderr.write(message + "\n")
    sys.stderr.flush()

def structseq_to_py(seq, name="INSERT_NAME"):
    """Turns a "structseq" object to a python pseudoclass."""
    sseq = str(seq)
    sseq = '('.join(sseq.split('(')[1:])
    sseq = ')'.join(sseq.split(')')[:1])
    print("class {0}:".format(name))
    for item in sseq.split(','):
        item = item.strip()
        key, value = item.split('=')
        print(indent("{0} = {1}".format(key, value)))

def indent(code, depth=4):
    code = code.split('\n')
    code = [" "*depth + line for line in code]
    return '\n'.join(code)

def clearIndent(code):
    code = code.split('\n')
    code = [line.strip() for line in code]
    return '\n'.join(code)

def syntaxValid(code):
    try:
        compile(code, "<no file>", 'exec')
    except SyntaxError:
        return False
    return True

def sanitize(expr):
    replace = {
        '*':'', '[':'', ']':'',
        'from':'_from', 'class':'_class', '-':'_', 'lambda':'_lambda',
        '\\':'ESC', ' ':'', "<":'"', ">":'"', "self,":"", "self":"",
        ",,":",", '...':'more_args'
    }
    result = expr
    for before, after in replace.iteritems():
        result = result.replace(before, after)
    result = result.replace("=,", "=[],").replace("=)", "=[])")
    return result

def strict_sanitize(expr):
    expr = sanitize(expr)
    expr = expr.replace("=()", "")
    expr = expr.replace('(', '').replace(')', '')
    return expr

def isSpace(char):
    return char == ' ' or char == '\t'

def removeAtCorner(string, char, direction):
    i = 0
    assert direction in ['<', '>']
    if direction == '>':
        iterator = range(0, len(string))
        def r(s, a): return s[a-1:]
    if direction == '<':
        iterator = [len(string)-x-1 for x in range(0, len(string))]
        def r(s, a): return s[:a+1]

    atBeginning = True
    for i in iterator:
        if isSpace(string[i]) and atBeginning:
            continue
        elif string[i] == char:
            atBeginning = False
        else:
            return r(string, i)
    return str()

likely_substitutions = {
    "integer": "int",
    "string": "str",
    "long": "int",
    "dictionary": "dict",
    "double": "float",
}

def parse_synopsis(funcdef):
    """Parse a function description in the following format:
    module.func(param1, param2, [optional_param1 = default1, [optional_param2 = default2]]) -> return_type
    This tries to be as error-prone as possible in order to convert everything into a valid parameter list."""
    # first, take the parts before and after the arrow:
    s = funcdef.split(' -> ')
    definition = s[0]
    returnType = s[1] if len(s) > 1 else "None"
    # Sometimes, people do fancy stuff in the return type, like "... -> ndarray or None if arg is False"
    # Thus, we only use the first word... well.
    returnType = strict_sanitize(returnType.split(' ')[0])
    if returnType in likely_substitutions:
        returnType = likely_substitutions[returnType]
    if returnType != 'None':
        returnType += "()"
    # Okay, now the fun part: parse the parameter list
    paramList = ')'.join('('.join(definition.split('(')[1:]).split(')')[:-1])
    paramList = paramList.split(',')
    resultingParamList = []
    atDefault = False
    for param in paramList:
        defaultValue = None
        # extract the name of the param
        param = param.replace(' ', '').replace('\t', '')
        # check for default values
        if removeAtCorner(param, '[', '>') != removeAtCorner(param, ' ', '>') or param.find('=') != -1:
            # default parameter list starts  or continues with this parameter
            atDefault = True
        if atDefault:
            if param.find('=') != -1:
                # default value was provided; clean trailing "[" and "]" chars
                defaultValue = removeAtCorner(removeAtCorner(param.split('=')[1], ']', '<'), '[', '<')
                param = param.split('=')[0]
            else:
                # just write anything, otherwise it's syntactically invalid
                defaultValue = "None"
        if removeAtCorner(param, '[', '<') != removeAtCorner(param, ' ', '<'):
            # default parameter list starts or continues after this parameter
            atDefault = True
        param = strict_sanitize(param)
        if param == '':
            continue
        if defaultValue:
            resultingParamList.append("{0}={1}".format(param, defaultValue))
        else:
            resultingParamList.append(param)
    return ', '.join(resultingParamList), returnType


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
        debugmsg("Processing module {0}".format(self.module.__name__))
        for member, value in inspect.getmembers(self.module):
            dumper = dumperForObject(value, member, self)
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
        try:
            arguments = inspect.getargspec(self.function)
            arglist = list()
            for index, argument in enumerate(arguments.args):
                if len(arguments.args) - index - 1 > len(arguments.defaults):
                    # no default value -> normal argument
                    arglist.append(argument)
                else:
                    # there's a default value
                    defaultIndex = index - (len(arguments.args) - len(arguments.defaults))
                    print(index, defaultIndex, arguments.args, arguments.defaults)
                    arglist.append("{0}={1}".format(argument, arguments.defaults[defaultIndex]))
            arglist = ', '.join(arglist)
        except TypeError:
            # not a python function, can't inspect it. try guessing argspec from docstring
            arglist = None
        try:
            docstring = self.function.__doc__.split('\n')[0]
            synArglist, returnValue = parse_synopsis(docstring)
        except:
            synArglist = ""
            returnValue = "None"
        if arglist is None:
            arglist = synArglist
        funcname = self.function.__name__
        if funcname[0].isdigit():
            funcname = '_' + funcname
        self.root.emit("def {0}({1}):".format(funcname, arglist))
        self.root.increaseIndent()
        self.root.emit('"""{0}"""'.format(self.function.__doc__))
        self.root.emit("return {0}".format(returnValue))
        self.root.decreaseIndent()

class ClassDumper:
    def __init__(self, klass, root):
        self.klass = klass
        self.root = root

    def dump(self):
        debugmsg("Generating documentation for class {0}".format(self.klass.__name__))
        self.root.emit("class {0}:".format(self.klass.__name__))
        self.root.increaseIndent()
        for member, value in inspect.getmembers(self.klass):
            if type(value) == type:
                continue
            dumper = dumperForObject(value, member, self.root)
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
        debugmsg("Usage: introspect.py <python_module_name>")
        exit(1)
    dumper.dump()
    debugmsg("All done -- looks good so far.")
