class pyqtSignal():
 def connect(self, targetSignal): pass
 def emit(self, *args): pass
from QtCore import *

class QTest():
    """"""
    # Enum QTest.MouseAction
    MousePress = 0
    MouseRelease = 0
    MouseClick = 0
    MouseDClick = 0
    MouseMove = 0

    # Enum QTest.KeyAction
    Press = 0
    Release = 0
    Click = 0

    def qWaitForWindowShown(self, window):
        '''static bool QTest.qWaitForWindowShown(QWidget window)'''
        return bool()
    def qWait(self, ms):
        '''static void QTest.qWait(int ms)'''
    def mouseEvent(self, action, widget, button, stateKey, pos, delay = None):
        '''static void QTest.mouseEvent(QTest.MouseAction action, QWidget widget, Qt.MouseButton button, Qt.KeyboardModifiers stateKey, QPoint pos, int delay = -1)'''
    def mouseRelease(self, widget, button, modifier = 0, pos = QPoint(), delay = None):
        '''static void QTest.mouseRelease(QWidget widget, Qt.MouseButton button, Qt.KeyboardModifiers modifier = 0, QPoint pos = QPoint(), int delay = -1)'''
    def mousePress(self, widget, button, modifier = 0, pos = QPoint(), delay = None):
        '''static void QTest.mousePress(QWidget widget, Qt.MouseButton button, Qt.KeyboardModifiers modifier = 0, QPoint pos = QPoint(), int delay = -1)'''
    def mouseMove(self, widget, pos = QPoint(), delay = None):
        '''static void QTest.mouseMove(QWidget widget, QPoint pos = QPoint(), int delay = -1)'''
    def mouseDClick(self, widget, button, modifier = 0, pos = QPoint(), delay = None):
        '''static void QTest.mouseDClick(QWidget widget, Qt.MouseButton button, Qt.KeyboardModifiers modifier = 0, QPoint pos = QPoint(), int delay = -1)'''
    def mouseClick(self, widget, button, modifier = 0, pos = QPoint(), delay = None):
        '''static void QTest.mouseClick(QWidget widget, Qt.MouseButton button, Qt.KeyboardModifiers modifier = 0, QPoint pos = QPoint(), int delay = -1)'''
    def keyRelease(self, widget, key, modifier = None, delay = None):
        '''static void QTest.keyRelease(QWidget widget, Qt.Key key, Qt.KeyboardModifiers modifier = Qt.NoModifier, int delay = -1)'''
    def keyRelease(self, widget, key, modifier = None, delay = None):
        '''static void QTest.keyRelease(QWidget widget, str key, Qt.KeyboardModifiers modifier = Qt.NoModifier, int delay = -1)'''
    def keyPress(self, widget, key, modifier = None, delay = None):
        '''static void QTest.keyPress(QWidget widget, Qt.Key key, Qt.KeyboardModifiers modifier = Qt.NoModifier, int delay = -1)'''
    def keyPress(self, widget, key, modifier = None, delay = None):
        '''static void QTest.keyPress(QWidget widget, str key, Qt.KeyboardModifiers modifier = Qt.NoModifier, int delay = -1)'''
    def keyEvent(self, action, widget, key, modifier = None, delay = None):
        '''static void QTest.keyEvent(QTest.KeyAction action, QWidget widget, Qt.Key key, Qt.KeyboardModifiers modifier = Qt.NoModifier, int delay = -1)'''
    def keyEvent(self, action, widget, ascii, modifier = None, delay = None):
        '''static void QTest.keyEvent(QTest.KeyAction action, QWidget widget, str ascii, Qt.KeyboardModifiers modifier = Qt.NoModifier, int delay = -1)'''
    def keyClicks(self, widget, sequence, modifier = None, delay = None):
        '''static void QTest.keyClicks(QWidget widget, QString sequence, Qt.KeyboardModifiers modifier = Qt.NoModifier, int delay = -1)'''
    def keyClick(self, widget, key, modifier = None, delay = None):
        '''static void QTest.keyClick(QWidget widget, Qt.Key key, Qt.KeyboardModifiers modifier = Qt.NoModifier, int delay = -1)'''
    def keyClick(self, widget, key, modifier = None, delay = None):
        '''static void QTest.keyClick(QWidget widget, str key, Qt.KeyboardModifiers modifier = Qt.NoModifier, int delay = -1)'''
    def qSleep(self, ms):
        '''static void QTest.qSleep(int ms)'''


