class pyqtSignal():
 def connect(self, targetSignal): pass
 def emit(self, *args): pass
from QtCore import *

from QtWidgets import *

import datetime

class QSignalSpy(QObject):
    """"""
    def __init__(self, signal):
        '''void QSignalSpy.__init__(signal signal)'''
    def __delitem__(self, i):
        '''void QSignalSpy.__delitem__(int i)'''
    def __setitem__(self, i, value):
        '''void QSignalSpy.__setitem__(int i, list-of-QVariant value)'''
    def __getitem__(self, i):
        '''list-of-QVariant QSignalSpy.__getitem__(int i)'''
        return [QVariant()]
    def __len__(self):
        '''int QSignalSpy.__len__()'''
        return int()
    def wait(self, timeout = 5000):
        '''bool QSignalSpy.wait(int timeout = 5000)'''
        return bool()
    def signal(self):
        '''QByteArray QSignalSpy.signal()'''
        return QByteArray()
    def isValid(self):
        '''bool QSignalSpy.isValid()'''
        return bool()


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

    def touchEvent(self, widget, device):
        '''static QTest.QTouchEventSequence QTest.touchEvent(QWidget widget, QTouchDevice device)'''
        return QTest.QTouchEventSequence()
    def touchEvent(self, window, device):
        '''static QTest.QTouchEventSequence QTest.touchEvent(QWindow window, QTouchDevice device)'''
        return QTest.QTouchEventSequence()
    def qWaitForWindowExposed(self, window, timeout = 5000):
        '''static bool QTest.qWaitForWindowExposed(QWindow window, int timeout = 5000)'''
        return bool()
    def qWaitForWindowExposed(self, widget, timeout = 1000):
        '''static bool QTest.qWaitForWindowExposed(QWidget widget, int timeout = 1000)'''
        return bool()
    def qWaitForWindowActive(self, window, timeout = 5000):
        '''static bool QTest.qWaitForWindowActive(QWindow window, int timeout = 5000)'''
        return bool()
    def qWaitForWindowActive(self, widget, timeout = 1000):
        '''static bool QTest.qWaitForWindowActive(QWidget widget, int timeout = 1000)'''
        return bool()
    def qWait(self, ms):
        '''static void QTest.qWait(int ms)'''
    def waitForEvents(self):
        '''static void QTest.waitForEvents()'''
    def mouseEvent(self, action, widget, button, modifier, pos, delay = None):
        '''static void QTest.mouseEvent(QTest.MouseAction action, QWidget widget, Qt.MouseButton button, Qt.KeyboardModifiers modifier, QPoint pos, int delay = -1)'''
    def mouseEvent(self, action, window, button, modifier, pos, delay = None):
        '''static void QTest.mouseEvent(QTest.MouseAction action, QWindow window, Qt.MouseButton button, Qt.KeyboardModifiers modifier, QPoint pos, int delay = -1)'''
    def mouseRelease(self, widget, button, modifier = 0, pos = QPoint(), delay = None):
        '''static void QTest.mouseRelease(QWidget widget, Qt.MouseButton button, Qt.KeyboardModifiers modifier = 0, QPoint pos = QPoint(), int delay = -1)'''
    def mouseRelease(self, window, button, modifier = 0, pos = QPoint(), delay = None):
        '''static void QTest.mouseRelease(QWindow window, Qt.MouseButton button, Qt.KeyboardModifiers modifier = 0, QPoint pos = QPoint(), int delay = -1)'''
    def mousePress(self, widget, button, modifier = 0, pos = QPoint(), delay = None):
        '''static void QTest.mousePress(QWidget widget, Qt.MouseButton button, Qt.KeyboardModifiers modifier = 0, QPoint pos = QPoint(), int delay = -1)'''
    def mousePress(self, window, button, modifier = 0, pos = QPoint(), delay = None):
        '''static void QTest.mousePress(QWindow window, Qt.MouseButton button, Qt.KeyboardModifiers modifier = 0, QPoint pos = QPoint(), int delay = -1)'''
    def mouseMove(self, widget, pos = QPoint(), delay = None):
        '''static void QTest.mouseMove(QWidget widget, QPoint pos = QPoint(), int delay = -1)'''
    def mouseMove(self, window, pos = QPoint(), delay = None):
        '''static void QTest.mouseMove(QWindow window, QPoint pos = QPoint(), int delay = -1)'''
    def mouseDClick(self, widget, button, modifier = 0, pos = QPoint(), delay = None):
        '''static void QTest.mouseDClick(QWidget widget, Qt.MouseButton button, Qt.KeyboardModifiers modifier = 0, QPoint pos = QPoint(), int delay = -1)'''
    def mouseDClick(self, window, button, modifier = 0, pos = QPoint(), delay = None):
        '''static void QTest.mouseDClick(QWindow window, Qt.MouseButton button, Qt.KeyboardModifiers modifier = 0, QPoint pos = QPoint(), int delay = -1)'''
    def mouseClick(self, widget, button, modifier = 0, pos = QPoint(), delay = None):
        '''static void QTest.mouseClick(QWidget widget, Qt.MouseButton button, Qt.KeyboardModifiers modifier = 0, QPoint pos = QPoint(), int delay = -1)'''
    def mouseClick(self, window, button, modifier = 0, pos = QPoint(), delay = None):
        '''static void QTest.mouseClick(QWindow window, Qt.MouseButton button, Qt.KeyboardModifiers modifier = 0, QPoint pos = QPoint(), int delay = -1)'''
    def keyRelease(self, widget, key, modifier = None, delay = None):
        '''static void QTest.keyRelease(QWidget widget, Qt.Key key, Qt.KeyboardModifiers modifier = Qt.NoModifier, int delay = -1)'''
    def keyRelease(self, widget, key, modifier = None, delay = None):
        '''static void QTest.keyRelease(QWidget widget, str key, Qt.KeyboardModifiers modifier = Qt.NoModifier, int delay = -1)'''
    def keyRelease(self, window, key, modifier = None, delay = None):
        '''static void QTest.keyRelease(QWindow window, str key, Qt.KeyboardModifiers modifier = Qt.NoModifier, int delay = -1)'''
    def keyRelease(self, window, key, modifier = None, delay = None):
        '''static void QTest.keyRelease(QWindow window, Qt.Key key, Qt.KeyboardModifiers modifier = Qt.NoModifier, int delay = -1)'''
    def keyPress(self, widget, key, modifier = None, delay = None):
        '''static void QTest.keyPress(QWidget widget, Qt.Key key, Qt.KeyboardModifiers modifier = Qt.NoModifier, int delay = -1)'''
    def keyPress(self, widget, key, modifier = None, delay = None):
        '''static void QTest.keyPress(QWidget widget, str key, Qt.KeyboardModifiers modifier = Qt.NoModifier, int delay = -1)'''
    def keyPress(self, window, key, modifier = None, delay = None):
        '''static void QTest.keyPress(QWindow window, str key, Qt.KeyboardModifiers modifier = Qt.NoModifier, int delay = -1)'''
    def keyPress(self, window, key, modifier = None, delay = None):
        '''static void QTest.keyPress(QWindow window, Qt.Key key, Qt.KeyboardModifiers modifier = Qt.NoModifier, int delay = -1)'''
    def keyEvent(self, action, widget, key, modifier = None, delay = None):
        '''static void QTest.keyEvent(QTest.KeyAction action, QWidget widget, Qt.Key key, Qt.KeyboardModifiers modifier = Qt.NoModifier, int delay = -1)'''
    def keyEvent(self, action, widget, ascii, modifier = None, delay = None):
        '''static void QTest.keyEvent(QTest.KeyAction action, QWidget widget, str ascii, Qt.KeyboardModifiers modifier = Qt.NoModifier, int delay = -1)'''
    def keyEvent(self, action, window, ascii, modifier = None, delay = None):
        '''static void QTest.keyEvent(QTest.KeyAction action, QWindow window, str ascii, Qt.KeyboardModifiers modifier = Qt.NoModifier, int delay = -1)'''
    def keyEvent(self, action, window, key, modifier = None, delay = None):
        '''static void QTest.keyEvent(QTest.KeyAction action, QWindow window, Qt.Key key, Qt.KeyboardModifiers modifier = Qt.NoModifier, int delay = -1)'''
    def keyClicks(self, widget, sequence, modifier = None, delay = None):
        '''static void QTest.keyClicks(QWidget widget, str sequence, Qt.KeyboardModifiers modifier = Qt.NoModifier, int delay = -1)'''
    def keyClick(self, widget, key, modifier = None, delay = None):
        '''static void QTest.keyClick(QWidget widget, Qt.Key key, Qt.KeyboardModifiers modifier = Qt.NoModifier, int delay = -1)'''
    def keyClick(self, widget, key, modifier = None, delay = None):
        '''static void QTest.keyClick(QWidget widget, str key, Qt.KeyboardModifiers modifier = Qt.NoModifier, int delay = -1)'''
    def keyClick(self, window, key, modifier = None, delay = None):
        '''static void QTest.keyClick(QWindow window, Qt.Key key, Qt.KeyboardModifiers modifier = Qt.NoModifier, int delay = -1)'''
    def keyClick(self, window, key, modifier = None, delay = None):
        '''static void QTest.keyClick(QWindow window, str key, Qt.KeyboardModifiers modifier = Qt.NoModifier, int delay = -1)'''
    def qSleep(self, ms):
        '''static void QTest.qSleep(int ms)'''
    class QTouchEventSequence():
        """"""
        def __init__(self):
            '''QTest.QTouchEventSequence QTest.QTouchEventSequence.__init__()'''
            return QTest.QTouchEventSequence()
        def commit(self, processEvents = True):
            '''void QTest.QTouchEventSequence.commit(bool processEvents = True)'''
        def stationary(self, touchId):
            '''QTest.QTouchEventSequence QTest.QTouchEventSequence.stationary(int touchId)'''
            return QTest.QTouchEventSequence()
        def release(self, touchId, pt, window = None):
            '''QTest.QTouchEventSequence QTest.QTouchEventSequence.release(int touchId, QPoint pt, QWindow window = None)'''
            return QTest.QTouchEventSequence()
        def release(self, touchId, pt, widget):
            '''QTest.QTouchEventSequence QTest.QTouchEventSequence.release(int touchId, QPoint pt, QWidget widget)'''
            return QTest.QTouchEventSequence()
        def move(self, touchId, pt, window = None):
            '''QTest.QTouchEventSequence QTest.QTouchEventSequence.move(int touchId, QPoint pt, QWindow window = None)'''
            return QTest.QTouchEventSequence()
        def move(self, touchId, pt, widget):
            '''QTest.QTouchEventSequence QTest.QTouchEventSequence.move(int touchId, QPoint pt, QWidget widget)'''
            return QTest.QTouchEventSequence()
        def press(self, touchId, pt, window = None):
            '''QTest.QTouchEventSequence QTest.QTouchEventSequence.press(int touchId, QPoint pt, QWindow window = None)'''
            return QTest.QTouchEventSequence()
        def press(self, touchId, pt, widget):
            '''QTest.QTouchEventSequence QTest.QTouchEventSequence.press(int touchId, QPoint pt, QWidget widget)'''
            return QTest.QTouchEventSequence()


