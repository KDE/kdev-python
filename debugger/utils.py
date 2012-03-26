# This file is imported from within the debugger
def debug_trace(*args):
    '''Set a tracepoint in the Python debugger that works with Qt'''
    try:
        from PyQt4.QtCore import pyqtRemoveInputHook
        pyqtRemoveInputHook()
    except ImportError:
        pass
    from pdb import set_trace
    set_trace()

import signal, pdb
# Support "Ctrl+C"
signal.signal(signal.SIGINT, debug_trace)