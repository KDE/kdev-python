#!/usr/bin/env python

import numpy
import types
import re

def indent(text):
    result = ""
    for line in text.split('\n'):
        result += "    " + line + "\n"
    return result

def get_indent(string):
    string = string.split("\n")[0]
    indent = 0
    for char in string:
        if char in [' ', '\t']:
            indent += 1
        else:
            return indent
    return 0

def remove_indent(string):
    if type(string) == types.StringType:
        string = string.split("\n")
        max_remove_indent = get_indent(string[0])
        result = ""
        for line in string:
            for offset in xrange(0, len(line)):
                if line[offset] not in [' ', '\t'] or offset > max_remove_indent:
                    result += line[offset:] + "\n"
                    break
        return result
    else:
        return string

def make_documentation(class_or_module):
    result = ""
    for item_name in dir(class_or_module):
        if item_name in ['__abstractmethods__', '__class__']:
            continue
        if item_name[:1] == '_' and item_name[:2] != '__':
            # skip private properties
            continue
        item = getattr(class_or_module, item_name)
        if type(item) in [types.FunctionType, types.BuiltinFunctionType, types.UnboundMethodType]:
            parameters = try_parse_func_docstring(item.__doc__)
            result += "def %s(%s):\n" % ( item_name, ','.join(parameters) )
            result += indent('"""%s"""\n\n' % remove_indent(item.__doc__))
        elif type(item) == types.TypeType:
            result += "class %s:\n" % item_name
            result += indent(make_documentation(item)) + "\n"
        else:
            #if item.__doc__ is not None:
                #result += '"""%s"""\n' % item.__doc__
            try:
                default_value = str(type(item)())
            except TypeError:
                default_value = "None"
            result += "%s = %s\n" % (item_name, default_value)
    return result

def try_parse_func_docstring(docstring):
    if type(docstring) == types.StringType:
        indent = 0
        atLineBeginning = True
        paramListBegin = paramListEnd = 0
        for offset in xrange(0, len(docstring)):
            if docstring[offset] == "\n":
                indent = 0
            if docstring[offset] in [' ', '\t'] and atLineBeginning:
                indent += 1
            else:
                atLineBeginning = False
            if docstring[offset:offset+len("Parameters")] == "Parameters":
                paramListBegin = offset
            if docstring[offset:offset+len("Returns")] == "Returns":
                paramListEnd = offset
        relevantPart = docstring[paramListBegin:paramListEnd].split("\n")[2:]
        if len(relevantPart):
            firstIndent = get_indent(relevantPart[0])
            parameter_name_list = []
            for line_index in xrange(0, len(relevantPart)):
                if get_indent(relevantPart[line_index]) == firstIndent:
                    s = relevantPart[line_index].split(' : ')
                    if len(s) == 2:
                        name = s[0]
                        type_string = s[1]
                        doc_for_param = None # TODO extract this, and display it in some way... or not
                        parameter_name_list.append(name.replace(' ', '').replace('\t', ''))
            return parameter_name_list
        else:
            return []
    else:
        return []

if __name__ == '__main__':
    print make_documentation(numpy)