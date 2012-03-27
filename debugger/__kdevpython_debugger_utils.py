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
    
def format_locals(locals):
    for key, value in locals.iteritems():
        if key == '__kdevpython_debugger_utils':
            continue
        value = str(value).replace('\n', r'\n')
        if len(value) > 120:
            value = value[:120] + "..."
        print "%s => %s" % (key, value)
    
import signal, pdb
# Support "Ctrl+C"
signal.signal(signal.SIGINT, debug_trace)