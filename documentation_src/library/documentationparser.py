#!/usr/bin/env python2.7
# -*- Coding:utf-8 -*-
import sys

from api.structure import *

accept_commands = ["data::", "function::", "method::", "class::", "module::"]

class DocumentationParser():
    last_class = None
    last_module = None
    def __init__(self, filename):
        self.filename = filename
        with open(self.filename, 'r') as f:
            self.text = f.read()
        self.text = self.text.replace("...", "more")
        self.handlers = {
            "data::" : self.save_data,
            "function::" : self.save_function,
            "method::" : self.save_function,
            "class::" : self.save_class,
            "module::" : self.save_module
        }
    
    def resolve_path(self, path):
        if not path:
            module = self.last_module
            class_ = self.last_class
        elif len(path) == 1:
            module = self.last_module
            class_ = path[0]
        elif len(path) == 2:
            module = path[0]
            class_ = path[1]
        else:
            raise ValueError("Don't know what to do with that descriptor: " + str(path))
        return module, class_
    
    def save_class(self, identifier, documentation):
        identifier = identifier.split(".")
        path = identifier[:-1]
        identifier = identifier[-1]
        module, class_ = self.resolve_path(path)
        self.last_class = Class(class_)
        self.last_module.addChild(self.last_class)
    
    def save_module(self, identifier, documentation):
        assert self.last_module == None
        self.last_module = Module(identifier)
    
    def save_function(self, identifier, documentation):
        identifier = identifier.split(".")
        path = identifier[:-1]
        identifier = identifier[-1]
        module, class_ = self.resolve_path(path)
        func = Function(identifier)
        if class_ is None:
            self.last_module.addChild(func)
        else:
            self.last_class.addMethod(func)
    
    def save_data(self, identifier, documentation):
        identifier = identifier.split(".")
        path = identifier[:-1]
        identifier = identifier[-1]
        module, class_ = self.resolve_path(path)
        data = Member(identifier)
        if class_ is None:
            self.last_module.addChild(data)
        else:
            self.last_class.addMember(data)
    
    def tokenize(self):
        cmdstring = '.. '
        endcmdstring = '::'
        size = len(self.text)
        i = 0
        current_indent = 0
        next_indent = 0
        try:
            while i < size:
                c = self.text[i]
                if self.text[i-len(cmdstring):i] == cmdstring:
                    # go until the end command token
                    start = i
                    errcnt = 0
                    while self.text[i-len(endcmdstring):i] != endcmdstring:
                        if self.text[i].isspace():
                            errcnt += 1;
                        i += 1
                        if errcnt > 1:
                            break
                    else:
                        yield "COMMAND", self.text[start:i]
                elif self.text[i] == "\n":
                    i += 1
                    yield "NEWLINE", next_indent - current_indent
                    current_indent = next_indent
                    next_indent = 0
                    while self.text[i].isspace():
                        if self.text[i] == "\n":
                            yield "NEWLINE", 0
                        else:
                            next_indent += 1
                        i += 1
                    yield "CONTENT", self.text[i]
                else:
                    yield "CONTENT", self.text[i]
                i += 1
        except IndexError:
            pass
            #print "Reached EOF while reading expression \"..." + self.text[i-20:i] + "\" (this is okay)"
            
    
    def readLine(self, tokenStream, token):
        token = tokenStream.next()
        accumulatedContent = ""
        while token[0] == "CONTENT" and token[1] not in accept_commands:
            accumulatedContent += token[1]
            token = tokenStream.next()
        return accumulatedContent, token
    
    def readBlock(self, tokenStream, token):
        indent = 1
        accumulatedContent = ""
        while indent > 0:
            line = self.readLine(tokenStream, token)
            if line[1][0] != "NEWLINE":
                return accumulatedContent, line[1]
            indent += line[1][1]
            accumulatedContent += line[0] + "\n"
            #print " [d]", indent, line
        return accumulatedContent, line[1]
    
    def parse(self):
        tokenStream = self.tokenize()
        try:
            token = tokenStream.next()
            while True:
                if token[0] == "COMMAND":
                    commandName = token[1]
                    args, token = self.readLine(tokenStream, token)
                    #print commandName, args
                    documentation, token = self.readBlock(tokenStream, token)
                    if commandName in self.handlers:
                        try:
                            self.handlers[commandName](args, documentation)
                        except Exception as e:
                            print "Error calling handler:", e
                            print "Arguments:", commandName, args, documentation
                    else:
                        print "Skipping command name:", commandName
                else:
                    token = tokenStream.next()
        except StopIteration:
            return self.last_module