#!/usr/bin/env python

from api.docmanager import DocumentationManager
from api.structure import *
import subprocess

class LibraryDocumentationManager(DocumentationManager):
    def downloadDocumentationData(self):
        subprocess.Popen(["/usr/bin/env", "wget", "-r", "--progress=dot", "-O", "src", "http://docs.python.org/_sources/library/"])