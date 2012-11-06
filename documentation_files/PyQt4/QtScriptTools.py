class pyqtSignal():
 def connect(self, targetSignal): pass
 def emit(self, *args): pass
from QtCore import *

class QScriptEngineDebugger(QObject):
    """"""
    # Enum QScriptEngineDebugger.DebuggerState
    RunningState = 0
    SuspendedState = 0

    # Enum QScriptEngineDebugger.DebuggerAction
    InterruptAction = 0
    ContinueAction = 0
    StepIntoAction = 0
    StepOverAction = 0
    StepOutAction = 0
    RunToCursorAction = 0
    RunToNewScriptAction = 0
    ToggleBreakpointAction = 0
    ClearDebugOutputAction = 0
    ClearErrorLogAction = 0
    ClearConsoleAction = 0
    FindInScriptAction = 0
    FindNextInScriptAction = 0
    FindPreviousInScriptAction = 0
    GoToLineAction = 0

    # Enum QScriptEngineDebugger.DebuggerWidget
    ConsoleWidget = 0
    StackWidget = 0
    ScriptsWidget = 0
    LocalsWidget = 0
    CodeWidget = 0
    CodeFinderWidget = 0
    BreakpointsWidget = 0
    DebugOutputWidget = 0
    ErrorLogWidget = 0

    def __init__(self, parent = None):
        '''void QScriptEngineDebugger.__init__(QObject parent = None)'''
    def state(self):
        '''QScriptEngineDebugger.DebuggerState QScriptEngineDebugger.state()'''
        return QScriptEngineDebugger.DebuggerState()
    evaluationResumed = pyqtSignal() # void evaluationResumed() - signal
    evaluationSuspended = pyqtSignal() # void evaluationSuspended() - signal
    def action(self, action):
        '''QAction QScriptEngineDebugger.action(QScriptEngineDebugger.DebuggerAction action)'''
        return QAction()
    def widget(self, widget):
        '''QWidget QScriptEngineDebugger.widget(QScriptEngineDebugger.DebuggerWidget widget)'''
        return QWidget()
    def createStandardMenu(self, parent = None):
        '''QMenu QScriptEngineDebugger.createStandardMenu(QWidget parent = None)'''
        return QMenu()
    def createStandardToolBar(self, parent = None):
        '''QToolBar QScriptEngineDebugger.createStandardToolBar(QWidget parent = None)'''
        return QToolBar()
    def standardWindow(self):
        '''QMainWindow QScriptEngineDebugger.standardWindow()'''
        return QMainWindow()
    def setAutoShowStandardWindow(self, autoShow):
        '''void QScriptEngineDebugger.setAutoShowStandardWindow(bool autoShow)'''
    def autoShowStandardWindow(self):
        '''bool QScriptEngineDebugger.autoShowStandardWindow()'''
        return bool()
    def detach(self):
        '''void QScriptEngineDebugger.detach()'''
    def attachTo(self, engine):
        '''void QScriptEngineDebugger.attachTo(QScriptEngine engine)'''


