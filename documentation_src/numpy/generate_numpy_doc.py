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

def escape_docstring(string):
    if string:
        return string.replace('"""', '\\"\\"\\"')
    else:
        return string


global in_class
in_class = 0

def make_documentation(class_or_module):
    global in_class
    result = ""
    for item_name in dir(class_or_module):
        if item_name in ['__abstractmethods__', '__class__']:
            continue
        if item_name[:1] == '_':
            # skip private properties and stuff like __get__
            continue
        item = getattr(class_or_module, item_name)
        if type(item) in [types.FunctionType, types.BuiltinFunctionType, types.UnboundMethodType] \
           or str(type(item)) in ['<type \'method_descriptor\'>', '<type \'wrapper_descriptor\'>', '<type \'numpy.ufunc\'>']:
            parameters = try_parse_func_docstring(item.__doc__, item_name)
            parameters = parameters if parameters is not None else []
            if in_class > 0:
                parameters.insert(0, 'self')
            result += "def %s(%s):\n" % ( str(item_name), ','.join(parameters) )
            result += indent('"""%s"""\n\n' % remove_indent(escape_docstring(item.__doc__)))
        elif type(item) == types.TypeType:
            result += "class %s:\n" % item_name
            in_class += 1
            result += indent(make_documentation(item)) + "\n"
            in_class -= 1
        else:
            try:
                if type(item) in [types.TypeType, types.ClassType]:
                    default_value = str(item.__name__ + "()")
                else:
                    default_value = str(type(item)())
                if default_value == "":
                    raise TypeError()
                if default_value.find('<') != -1:
                    raise TypeError()
            except TypeError:
                default_value = "None"
            result += "%s = %s\n" % (item_name, default_value)
    if result == "":
        result = "pass"
    return result

def sanitizeParamName(name):
    return name.replace(' ', '').replace('\t', '').replace('\\', '') \
               .replace('.', '_').replace('[', '').replace(']', '') \
               .replace('*', '').replace('-', '_')

def try_parse_func_docstring(docstring, funcname):
    if type(docstring) == types.StringType:
        indent = 0
        atLineBeginning = True
        paramListBegin = paramListEnd = False
        atPartBeginning = 2
        for offset in xrange(0, len(docstring)):
            if docstring[offset] == "\n":
                indent = 0
            if docstring[offset] in [' ', '\t'] and atLineBeginning:
                indent += 1
            else:
                atLineBeginning = False
            
            if docstring[offset:offset+len("Parameters")] == "Parameters":
                paramListBegin = offset
            if paramListBegin is not False and docstring[offset] == "\n" and atPartBeginning != 0:
                atPartBeginning -= 1
            if docstring[offset:offset+len("---")] == "---" and atPartBeginning == 0:
                paramListEnd = offset
                break
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
                        parameter_name = sanitizeParamName(name)
                        try:
                            t = int(parameter_name[0])
                            parameter_name = '_' + parameter_name
                        except:
                            pass
                        if parameter_name.find('...') != -1:
                            parameter_name = 'more'
                        parameter_name = parameter_name.replace('`', '')
                        parameter_name_list.append(parameter_name)
            return parameter_name_list
        else:
            try:
                firstType = docstring.split("\n")[0].split('.')[-1]
                if firstType.find(funcname) == -1:
                    raise IndexError()
                firstType = firstType.split('->')[0]
                firstType = firstType.split('(')[1:]
                firstType = ')'.join('('.join(firstType).split(')')[:-1])
                paramList = firstType.split(',')
                cleanedParamList = []
                for item in paramList:
                    if item.find('...') == -1:
                        cleanedParamList.append(item)
                return [sanitizeParamName(x) for x in cleanedParamList]
            except IndexError:
                return []
    else:
        return []

if __name__ == '__main__':
    print make_documentation(numpy)