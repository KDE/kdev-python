#!/usr/bin/env python

import os
from lxml import etree

class DocumentationManager():
    def __init__(self, sourcefile, moduleName, parser):
        self.moduleName = moduleName
        self.parser = parser(sourcefile)
        self.data = None
    
    def downloadDocumentationData(self):
        raise NotImplementedError()
    
    def applyImmediatePatches(self):
        pass
    
    def applyXmlPatches(self):
        pass
    
    def saveImmediateState(self):
        pass
    
    def saveXmlState(self):
        pass
    
    def parse(self):
        return self.parser.parse()
    
    def runCommand(self, cmdline):
        try:
            command = cmdline[1]
        except IndexError:
            raise ValueError("Invalid command line")
        if command == "download":
            self.downloadDocumentationData()
        if command == "parseSourcefiles":
            try:
                os.mkdir("xml")
            except OSError:
                pass
            xmltree = self.parse()
            with open("xml/" + self.moduleName + ".xml", 'w') as fileptr:
                fileptr.write(xmltree.toString())
        else:
            raise ValueError("Unknown command: %s" % command)