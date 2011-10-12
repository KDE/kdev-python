#!/usr/bin/env python

import os
from lxml import etree

import structure
import subprocess

from os import path

def indent(code):
    l = []
    for line in code.split("\n"):
        l.append("\t" + line)
    return "\n".join(l) + "\n"

def sanitize(expr):
    replace = {
        '*':'', '[':'', ']':'',
        'from':'_from', 'class':'_class', '-':'_',
        '\\':'ESC', ' ':'', "<":'"', ">":'"', "self,":"", "self":"",
        ",,":","
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
    return ""

def parse_synopsis(funcdef):
    """Parse a function description in the following format:
    module.func(param1, param2, [optional_param1 = default1, [optional_param2 = default2]]) -> return_type
    This tries to be as error-prone as possible in order to convert everything into a valid parameter list."""
    # first, take the parts before and after the arrow:
    s = funcdef.split(' -> ')
    definition = s[0]
    returnType = s[1] if len(s) > 1 else "__unknown"
    # Sometimes, people do fancy stuff in the return type, like "... -> ndarray or None if arg is False"
    # Thus, we only use the first word... well.
    returnType = strict_sanitize(returnType.split(' ')[0])
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
                defaultValue = "__unknown"
        if removeAtCorner(param, '[', '<') != removeAtCorner(param, ' ', '<'):
            # default parameter list starts or continues after this parameter
            atDefault = True
        param = strict_sanitize(param)
        if param == '':
            continue
        arg = structure.Argument(param)
        arg.defaultValue = defaultValue
        resultingParamList.append(arg)
    return resultingParamList, returnType

class DocumentationManager():
    def __init__(self, sourceDirectory, moduleName, parser, fileList):
        self.moduleName = moduleName
        self.callParserWithArgs = fileList
        self.data = None
        self.sourceDirectory = sourceDirectory
        self.originalDirectory = moduleName
        self.originalXmlDirectory = moduleName + "_xml"
        self.modifiedDirectory = moduleName + "_modified"
        self.modifiedXmlDirectory = moduleName + "_xml_modified"
        self.parserClass = parser
    
    def downloadDocumentationData(self):
        raise NotImplementedError()
    
    def restoreImmediateState(self):
        self.applyPatch(self.moduleName, self.originalDirectory, self.modifiedDirectory)
    
    def restoreXmlState(self):
        self.applyPatch(self.moduleName + "_xml", self.originalXmlDirectory, self.modifiedXmlDirectory)
    
    def saveImmediateState(self):
        self.makePatch(self.moduleName, self.originalDirectory, self.modifiedDirectory)
    
    def saveXmlState(self):
        self.makePatch(self.moduleName + "_xml", self.originalXmlDirectory, self.modifiedXmlDirectory)
    
    def makePatch(self, patchfile, originalDirectory, modifiedDirectory):
        print "Generating patchfile %s.diff." % patchfile
        subprocess.call("diff --recursive --context %s %s/ > %s.diff" % (originalDirectory, modifiedDirectory, patchfile), shell = True)
    
    def applyPatch(self, patchfile, originalDirectory, modifiedDirectory):
        print "Applying patchfile %s.diff to directory %s." % ( patchfile, originalDirectory )
        if path.exists(modifiedDirectory):
            print "%s already exists, please delete it manually if you want to lose your changes there!" % modifiedDirectory
            print "Not doing anything."
            return
        # first, copy the original files
        subprocess.call(["cp", "-R", originalDirectory, "ORIGINAL"])
        # then patch it
        subprocess.call("cat %s.diff |patch -p0" % patchfile, shell = True)
        # then swap the two directories
        subprocess.call(["mv", originalDirectory, modifiedDirectory])
        subprocess.call(["mv", "ORIGINAL", originalDirectory])
        print "Updated data written to directory %s." % modifiedDirectory
    
    def runCommand(self, cmdline):
        try:
            command = cmdline[1]
        except IndexError:
            raise ValueError("Invalid command line")
        if command == "saveSource":
            self.saveImmediateState()
        elif command == "restoreSource":
            self.restoreImmediateState()
        elif command == "saveXml":
            self.saveXmlState()
        elif command == "restoreXml":
            self.restoreXmlState()
        elif command == "download":
            self.downloadDocumentationData()
        elif command == "parseSourcefiles":
            try:
                os.mkdir("xml")
            except OSError:
                pass
            for currentFile in self.callParserWithArgs:
                parser = self.parserClass(currentFile)
                xmltree = parser.parse().toXml()
                with open("xml/" + currentFile + ".xml", 'w') as fileptr:
                    fileptr.write(xmltree.toString())
        else:
            raise ValueError("Unknown command: %s" % command)