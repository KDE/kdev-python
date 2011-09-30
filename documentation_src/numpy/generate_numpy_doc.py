#!/usr/bin/env python

import numpy
import types
import re

def indent(text):
    result = ""
    for line in text.split('\n'):
        result += "    " + line + "\n"
    return result

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
            result += "def %s():\n" % item_name
            result += indent('"""%s"""\n\n' % item.__doc__)
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
        params_found = re.search("\n[\\s]*Parameters[\\s]*\n", docstring, re.U)
    else:
        params_found = None

if __name__ == '__main__':
    print make_documentation(numpy)