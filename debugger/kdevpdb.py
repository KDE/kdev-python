from pdb import *

import sys

class kdevOutputFormatter():
    def __init__(self):
        from sys import stdout as __stdout
        self.__stdout = __stdout
    def write(self, data):
        self.__stdout.write("__KDEVPYTHON_BEGIN_DEBUGGER_OUTPUT>>>" + str(data) + "<<<__KDEVPYTHON_END___DEBUGGER_OUTPUT")

class kdevPdb(Pdb):
    def __init__(self):
        Pdb.__init__(self)
        self.stdout = kdevOutputFormatter()
        self.prompt = "__KDEVPYTHON_DEBUGGER_PROMPT"
    def _runscript(self, filename):
        Pdb._runscript(self, filename)
        self._user_requested_quit = 1

if __name__ == '__main__':
    import pdb
    pdb.Pdb = kdevPdb
    pdb.main()