#!/usr/bin/env python2.7
# -*- Coding:utf-8 -*-
import sqlite3
import sys

conn = sqlite3.connect('documentation.db')
c = conn.cursor()
c.execute("CREATE TABLE IF NOT EXISTS modules (modulename text, documentation text)")
c.execute("CREATE TABLE IF NOT EXISTS classes (modulename text, classname text, documentation text)")
c.execute("CREATE TABLE IF NOT EXISTS methods (modulename text, classname text, methodname text, documentation text)")
c.execute("CREATE TABLE IF NOT EXISTS properties (modulename text, classname text, propertyname text, documentation text)")
c.execute("CREATE TABLE IF NOT EXISTS modulefunctions (modulename text, functionname text, documentation text)")
c.execute("CREATE TABLE IF NOT EXISTS moduleproperties (modulename text, propertyname text, documentation text)")

accept_commands = ["data::", "function::", "class::", "module::"]

class DocumentationParser():
    last_class = None
    last_module = None
    def __init__(self, filename):
    	self.filename = filename
    	with open(self.filename) as f:
            self.text = f.read()
        self.text = self.text.replace("...", "*more")
        self.handlers = {
            "data::" : self.save_data,
            "function::" : self.save_function,
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
        c.execute("""INSERT INTO classes (modulename, classname, documentation) VALUES (?, ?, ?)""",
                  (module.decode("utf-8"), class_.decode("utf-8"), documentation.decode("utf-8")))
    
    def save_module(self, identifier, documentation):
        c.execute("""INSERT INTO modules (modulename, documentation) VALUES (?, ?)""",
                  (identifier.decode("utf-8"), documentation.decode("utf-8")))
    
    def save_function(self, identifier, documentation):
        identifier = identifier.split(".")
        path = identifier[:-1]
        identifier = identifier[-1]
        module, class_ = self.resolve_path(path)
        if class_ is None:
            c.execute("""INSERT INTO modulefunctions (modulename, functionname, documentation)
                         VALUES (?, ?, ?)""", (module.decode("utf-8"), identifier.decode("utf-8"), documentation.decode("utf-8")))
        else:
            c.execute("""INSERT INTO methods (modulename, classname, methodname, documentation)
                         VALUES (?, ?, ?, ?)""", (module.decode("utf-8"), class_.decode("utf-8"),
                         identifier.decode("utf-8"), documentation.decode("utf-8")))
    
    def save_data(self, identifier, documentation):
        identifier = identifier.split(".")
        path = identifier[:-1]
        identifier = identifier[-1]
        module, class_ = self.resolve_path(path)
        if class_ is None:
            c.execute("""INSERT INTO moduleproperties ( modulename, propertyname, 
                       documentation ) VALUES (?, ?, ?)""", ( module.decode("utf-8"), 
                       identifier.decode("utf-8"), documentation.decode("utf-8")))
        else:
            c.execute("""INSERT INTO properties ( modulename, propertyname, classname,
                       documentation ) VALUES (?, ?, ?, ?)""", (module.decode("utf-8"), 
                       identifier.decode("utf-8"), class_.decode("utf-8"), documentation.decode("utf-8")))
    
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
            accumulatedContent += line[0]
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
                    documentation, token = self.readBlock(tokenStream, token)
                    if commandName == "module::":
                        self.last_module = args
                    if commandName == "class::":
                        self.last_class = args
                    if commandName in self.handlers:
                        try:
                            self.handlers[commandName](args, documentation)
                        except Exception as e:
                            print "Error calling handler:", e
                            print "Arguments:", commandName, args, documentation
                else:
                    token = tokenStream.next()
        except StopIteration:
            print "Done."

p = DocumentationParser(sys.argv[1])
p.parse()

conn.commit()
c.close()
conn.close()