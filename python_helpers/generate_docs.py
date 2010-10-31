#!/usr/bin/env python

import pydoc

modules = ['random']
code = ''

current_name = []

import types
import pydoc
import subprocess

import re

import os

modules_done = []

import sys

from PyQt4.QtCore import pyqtWrapperType

def dbg(s):
    sys.stderr.write(s)
    sys.stderr.write("\n")

def walk_directory(path):
    modules_found = []
    for root, dirs, files in os.walk(path):
        for current_file in files:
            if not ( current_file.endswith('.so') or current_file.endswith('.py') ) or current_file.startswith('__init__'):
                continue
            module_path = root.replace(path, '').replace('/', '.') + '.' + current_file.replace('.so', '').replace('.py', '')
            if module_path.startswith('.'):
                module_path = module_path[1:]
            modules_found.append(module_path)
    dbg("Modules found: " + str(modules_found))
    return modules_found

def indent(moar = 0):
    ret = ''
    for i in xrange(0, len(current_name) + moar - 1):
        ret += "    "
    return ret

def removeIndent(line):
    m = re.search(r'^ *', line)
    return line[:m.start()] + line[m.end():]

validMethodTypes = [types.UnboundMethodType, types.FunctionType, types.BuiltinFunctionType]
validModuleTypes = [pyqtWrapperType, types.FunctionType]

def process(obj):
    try:
        if obj.__name__.startswith('_'):
            raise AttributeError
    except:
        #dbg("Aborting, name starts with __")
        return
    
    try:
        current_name.append(obj.__name__)
    except:
        current_name.append('<atom>')
    #dbg(" ++ Process called with argument " + str(obj))
    
    if type(obj) == types.ModuleType or type(obj) in validModuleTypes:
        properties = dir(obj)
        #print obj, properties, type(obj)
        if type(obj) == types.ModuleType:
            print indent() + "class " + obj.__name__.replace('<','').replace('>','') + "():"
            print indent(1) + "pass"
            
        for current_property in properties:
            current_property = getattr(obj, current_property)
            if type(current_property) in validMethodTypes:
                #dbg(" >> Processing property: " + str(current_property))
                process(current_property)
            if type(current_property) in validModuleTypes:
                dbg(" MODULE: " + str(current_property))
                for item in dir(current_property):
                    if type(current_property) in validMethodTypes:
                        process(getattr(current_property, item))
            else:
                pass
                #dbg(" -- Skipped property of invalid type " + str(type(current_property)))
        
    if type(obj) in validMethodTypes:
        dbg(" ++ Generating documentation for " + str(obj))
        dbg(" ++ [" + '.'.join(current_name) + "]")
        documentation = subprocess.Popen(['/usr/bin/pydoc', '.'.join(current_name)], stdout = subprocess.PIPE).stdout.read()
        lines = documentation.split("\n")
        
        split = lines[2].split("=")
        try:
            if split[1][:2] == ' _':
                current_name.pop()
                return
        except:
            pass
        print indent() + "# Generated Documentation for ", ''.join(split[:1])
        if not '='.join(split[1:]): 
            dbg("Skipping invalid function")
            current_name.pop()
            return
        lines[2] = "def" + '='.join(split[1:])
        
        split = lines[2].split('method of')
        lines[2] = 'method of'.join(split[:1]) + ":"
        
        documentation = "\n".join(lines[3:])
        
        lines[2] = lines[2].replace('{', "''' ").replace('}', " '''").replace('function <lambda>', 'lambda_func').replace('<', '"').replace('>', '"').replace('...', "args='<unknown>'")
        
        print indent() + lines[2]
        print indent(1) + '"""'
        for line in lines[3:]:
            print indent(1) + removeIndent(line)
        print indent(1) + '"""'
        print indent(1) + "pass \n\n"
    
    current_name.pop()

root_path = ''
exclude_packages = ['_sane', 'sane', 'this', 'Pyrex.Plex.test_tm']
current_file = None
result_basepath = 'results/'
for module in walk_directory('/usr/lib/python2.6/'):
    module = module.replace("\n", "").replace('site-packages.', '')
    module_parts = module.split('.')
    try:
        current_file = open(result_basepath + module.replace('.', '/'), 'w')
    except IOError:
        path = result_basepath
        for part in module_parts:
            path += part + '/'
            if not os.path.exists(path):
                os.mkdir(path)
        current_file = open(result_basepath + module.replace('.', '/'), 'w')
        
    dbg(" >> Processing MODULE: " + module)
    if module in exclude_packages or module.find('test') != -1: # exclude tests and stuff
        continue
    try:
        current_m = __import__(root_path + module)
    except:
        dbg("Could not import module " + module)
        continue

    get_attributes = module.split('.')
    
    for attrib in get_attributes:
        try:
            current_m = getattr(current_m, attrib)
            dbg(" ##### " + str(root_path + module) + " > " + str(current_m) + " (" + str(attrib) + ")")
        except AttributeError:
            continue
    
    dbg(" >>> CALL :: " + module)
    process(current_m)
    dbg(" <<< RETURN")
