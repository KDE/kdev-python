#!/usr/bin/env python

class DocumentationManager():
    def __init__(self, moduleName, parser):
        self.moduleName = moduleName
        self.parser = parser
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
    
    def processData(self):
        pass
    
    def parse(self):
        self.data = self.parser.parse()

