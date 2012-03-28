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
    
    def debug_trace(self, *args):
        '''Set a tracepoint in the Python debugger that works with Qt'''
        try:
            from PyQt4.QtCore import pyqtRemoveInputHook
            pyqtRemoveInputHook()
        except ImportError:
            pass
        self.set_trace(sys._getframe().f_back)
    
    def _runscript(self, filename):
        import signal
        signal.signal(signal.SIGINT, self.debug_trace)
        Pdb._runscript(self, filename)
        self._user_requested_quit = 1

if __name__ == '__main__':
    import pdb
    pdb.Pdb = kdevPdb
    pdb.main()