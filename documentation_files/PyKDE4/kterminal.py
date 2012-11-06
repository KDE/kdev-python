class pyqtSignal():
 def connect(self, targetSignal): pass
 def emit(self, *args): pass
from QtCore import *

class TerminalInterface():
    """"""
    def __init__(self):
        '''void TerminalInterface.__init__()'''
    def __init__(self):
        '''TerminalInterface TerminalInterface.__init__()'''
        return TerminalInterface()
    def sendInput(self, text):
        '''abstract void TerminalInterface.sendInput(QString text)'''
    def showShellInDir(self, dir):
        '''abstract void TerminalInterface.showShellInDir(QString dir)'''
    def startProgram(self, program, args):
        '''abstract void TerminalInterface.startProgram(QString program, QStringList args)'''


class TerminalInterfaceV2(TerminalInterface):
    """"""
    def __init__(self):
        '''void TerminalInterfaceV2.__init__()'''
    def __init__(self):
        '''TerminalInterfaceV2 TerminalInterfaceV2.__init__()'''
        return TerminalInterfaceV2()
    def foregroundProcessName(self):
        '''abstract QString TerminalInterfaceV2.foregroundProcessName()'''
        return QString()
    def foregroundProcessId(self):
        '''abstract int TerminalInterfaceV2.foregroundProcessId()'''
        return int()
    def terminalProcessId(self):
        '''abstract int TerminalInterfaceV2.terminalProcessId()'''
        return int()


class KTerminal():
    """"""
    def __init__(self, part):
        '''void KTerminal.__init__(KParts.Part part)'''
    def __init__(self):
        '''KTerminal KTerminal.__init__()'''
        return KTerminal()
    def terminalInterfaceV2(self):
        '''TerminalInterfaceV2 KTerminal.terminalInterfaceV2()'''
        return TerminalInterfaceV2()
    def terminalInterface(self):
        '''TerminalInterface KTerminal.terminalInterface()'''
        return TerminalInterface()


