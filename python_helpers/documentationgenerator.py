#!/usr/bin/env python
# -*- Coding: utf-8 -*-

import types
from PyQt4.QtCore import pyqtWrapperType

import subprocess

import os, sys

import re

def dbg(*args):
    for arg in args:
        sys.stdout.write(str(arg) + ' ')
    sys.stdout.write('\n')

def removeIndent(line):
    m = re.search(r'^ *', line)
    return line[:m.start()] + line[m.end():]

class DocumentationGenerator():
    validMethodTypes = [types.UnboundMethodType, types.FunctionType, types.BuiltinFunctionType]
    validModuleTypes = [pyqtWrapperType, types.FunctionType, types.ModuleType, types.ClassType]
    
    current_file = None
    open_files = dict()
    
    exclude_packages = ['_sane', 'sane', 'this', 'Pyrex.Plex.test_tm']
    
    def walk_directory(self, path):
        modules_found = []
        for root, dirs, files in os.walk(path):
            for current_file in files:
                if not ( current_file.endswith('.so') or current_file.endswith('.py') ) or current_file.startswith('__init__'):
                    continue
                module_path = root.replace(path, '').replace('/', '.') + '.' + current_file.replace('.so', '').replace('.py', '')
                module_path = module_path.replace('site-packages.', '')
                
                if module_path.startswith('.'):
                    module_path = module_path[1:]
                
                if module_path in self.exclude_packages or module_path.find('test') != -1:
                    continue
                
                modules_found.append(module_path)
        dbg("Modules found: " + str(modules_found))
        return modules_found
    
    def run(self, basepath):
        for module_name in self.walk_directory(basepath):
            try:
                current_m = __import__(module_name)
            except:
                dbg("Could not import module " + module_name)
                continue
            self.walk_module(current_m, module_name)
    
    def walk_module(self, module, module_name):
        dbg("CHECKMODULE> ", module_name, module, type(module))
        if type(module) in self.validModuleTypes:
            properties = dir(module)
            for current_property_name in properties:
                if current_property_name.startswith('_'):
                    continue
                
                current_property = getattr(module, current_property_name)
                current_type = type(current_property)
                dbg("CHECK> ", module_name, module, current_property, current_type)
                if current_type in self.validModuleTypes:
                    dbg("RECURSIVE_CHECK> ", module_name, current_property_name)
                    self.walk_module(current_property_name, module_name + '.' + current_property_name)
                if current_type in self.validMethodTypes:
                    self.generate_documentation_for(module_name + '.' + current_property_name)
        self.generate_documentation_for(module_name)
    
    def write_docfile(self, *args):
        for item in args:
            self.current_file.write(str(item))
        self.current_file.write('\n')
    
    def get_docfile(self, module_name):
        pathspec = module_name.split('.')[:-1]
        relative_path = 'results/' + '/'.join(pathspec) + '.py'
        dbg("PATH> ", relative_path, " (from ", module_name, ")")
        try:
            self.current_file = self.open_files[relative_path]
            return self.current_file
        except KeyError:
            pass
        try:
            self.current_file = open(relative_path, 'w')
            self.open_files[relative_path] = self.current_file
            return self.current_file
        except IOError:
            pass
        try:
            path = 'results/'
            for part in pathspec:
                path += part + '/'
                if not os.path.exists(path):
                    dbg("CREATE> ", path)
                    os.mkdir(path)
            dbg("CREATE> ", relative_path)
            self.current_file = open(relative_path, 'w')
            self.open_files[relative_path] = self.current_file
            return self.current_file
        except IOError:
            raise IOError('Could not create valid docfile')
        
    def close_files(self):
        for key, f in self.open_files.iteritems():
            f.close()
    
    def indent(self, moar = 0):
        ret = ''
        for i in xrange(0, moar):
            ret += "    "
        return ret
    
    def generate_documentation_for(self, module_name):
        dbg("PYDOC> ", module_name)
        documentation = subprocess.Popen(['/usr/bin/pydoc', module_name], stdout = subprocess.PIPE).stdout.read()
        lines = documentation.split("\n")
        
        docfile = self.get_docfile(module_name)
        
        split = lines[2].split("=")
        try:
            if split[1][:2] == ' _':
                return
        except:
            pass
        if not '='.join(split[1:]): 
            dbg("SKIP> Skipping invalid function")
            dbg("SKIP> Failed to get documentation for", module_name)
            return
        if '='.join(split[1:]).find('class ') != -1:
            dbg("SKIP_CLS> skipping class", module_name)
            return
        lines[2] = "def" + '='.join(split[1:])
        
        split = lines[2].split('method of')
        lines[2] = 'method of'.join(split[:1]) + ":"
        
        documentation = "\n".join(lines[3:])
        
        lines[2] = lines[2].replace('{', "''' ").replace('}', " '''").replace('function <lambda>', 'lambda_func').replace('<', '"').replace('>', '"').replace('...', "args='<unknown>'")
        
        self.write_docfile(self.indent() + "# Generated Documentation for ", ''.join(split[:1]))
        self.write_docfile(self.indent() + lines[2])
        self.write_docfile(self.indent(1) + '"""')
        for line in lines[3:]:
            self.write_docfile(self.indent(1) + removeIndent(line))
        self.write_docfile(self.indent(1) + '"""')
        self.write_docfile(self.indent(1) + "pass \n\n")

try:
    generator = DocumentationGenerator()
    generator.run('/usr/lib/python2.6/')
except Exception as e:
    print e
finally:
    generator.close_files()