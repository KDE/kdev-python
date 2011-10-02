#!/usr/bin/env python

from api.docmanager import DocumentationManager
from api.structure import *
from documentationparser import DocumentationParser
import os, sys
import subprocess

os.chdir("library")

class LibraryDocumentationManager(DocumentationManager):
    def downloadDocumentationData(self):
        try: os.mkdir("src")
        except OSError: pass
        os.chdir("src")
        subprocess.call(["/usr/bin/env", "wget", "-r", "--progress=dot", "--level", "1", "http://docs.python.org/_sources/library/"])
        os.chdir("docs.python.org/_sources/library")
        subprocess.call("cp -v *.txt ../../../", shell = True)
        os.chdir("../../../")
        print "Deleting old files..."
        subprocess.call(["rm", "-Rf", "docs.python.org"])

manager = LibraryDocumentationManager("src/random.txt", "random", DocumentationParser)
manager.runCommand(sys.argv)