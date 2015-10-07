class pyqtSignal():
 def connect(self, targetSignal): pass
 def emit(self, *args): pass
from QtCore import *

from QtWidgets import *

import datetime

class QQuickWidget(QWidget):
    """"""
    # Enum QQuickWidget.Status
    Null = 0
    Ready = 0
    Loading = 0
    Error = 0

    # Enum QQuickWidget.ResizeMode
    SizeViewToRootObject = 0
    SizeRootObjectToView = 0

    def __init__(self, parent = None):
        '''void QQuickWidget.__init__(QWidget parent = None)'''
    def __init__(self, engine, parent):
        '''void QQuickWidget.__init__(QQmlEngine engine, QWidget parent)'''
    def __init__(self, source, parent = None):
        '''void QQuickWidget.__init__(QUrl source, QWidget parent = None)'''
    def quickWindow(self):
        '''QQuickWindow QQuickWidget.quickWindow()'''
        return QQuickWindow()
    def setClearColor(self, color):
        '''void QQuickWidget.setClearColor(QColor color)'''
    def grabFramebuffer(self):
        '''QImage QQuickWidget.grabFramebuffer()'''
        return QImage()
    def dropEvent(self):
        '''QDropEvent QQuickWidget.dropEvent()'''
        return QDropEvent()
    def dragLeaveEvent(self):
        '''QDragLeaveEvent QQuickWidget.dragLeaveEvent()'''
        return QDragLeaveEvent()
    def dragMoveEvent(self):
        '''QDragMoveEvent QQuickWidget.dragMoveEvent()'''
        return QDragMoveEvent()
    def dragEnterEvent(self):
        '''QDragEnterEvent QQuickWidget.dragEnterEvent()'''
        return QDragEnterEvent()
    def focusOutEvent(self, event):
        '''void QQuickWidget.focusOutEvent(QFocusEvent event)'''
    def focusInEvent(self, event):
        '''void QQuickWidget.focusInEvent(QFocusEvent event)'''
    def event(self):
        '''QEvent QQuickWidget.event()'''
        return QEvent()
    def wheelEvent(self):
        '''QWheelEvent QQuickWidget.wheelEvent()'''
        return QWheelEvent()
    def hideEvent(self):
        '''QHideEvent QQuickWidget.hideEvent()'''
        return QHideEvent()
    def showEvent(self):
        '''QShowEvent QQuickWidget.showEvent()'''
        return QShowEvent()
    def mouseDoubleClickEvent(self):
        '''QMouseEvent QQuickWidget.mouseDoubleClickEvent()'''
        return QMouseEvent()
    def mouseMoveEvent(self):
        '''QMouseEvent QQuickWidget.mouseMoveEvent()'''
        return QMouseEvent()
    def mouseReleaseEvent(self):
        '''QMouseEvent QQuickWidget.mouseReleaseEvent()'''
        return QMouseEvent()
    def mousePressEvent(self):
        '''QMouseEvent QQuickWidget.mousePressEvent()'''
        return QMouseEvent()
    def keyReleaseEvent(self):
        '''QKeyEvent QQuickWidget.keyReleaseEvent()'''
        return QKeyEvent()
    def keyPressEvent(self):
        '''QKeyEvent QQuickWidget.keyPressEvent()'''
        return QKeyEvent()
    def timerEvent(self):
        '''QTimerEvent QQuickWidget.timerEvent()'''
        return QTimerEvent()
    def resizeEvent(self):
        '''QResizeEvent QQuickWidget.resizeEvent()'''
        return QResizeEvent()
    sceneGraphError = pyqtSignal() # void sceneGraphError(QQuickWindow::SceneGraphError,const QStringamp;) - signal
    statusChanged = pyqtSignal() # void statusChanged(QQuickWidget::Status) - signal
    def setSource(self):
        '''QUrl QQuickWidget.setSource()'''
        return QUrl()
    def format(self):
        '''QSurfaceFormat QQuickWidget.format()'''
        return QSurfaceFormat()
    def setFormat(self, format):
        '''void QQuickWidget.setFormat(QSurfaceFormat format)'''
    def initialSize(self):
        '''QSize QQuickWidget.initialSize()'''
        return QSize()
    def sizeHint(self):
        '''QSize QQuickWidget.sizeHint()'''
        return QSize()
    def errors(self):
        '''list-of-QQmlError QQuickWidget.errors()'''
        return [QQmlError()]
    def status(self):
        '''QQuickWidget.Status QQuickWidget.status()'''
        return QQuickWidget.Status()
    def setResizeMode(self):
        '''QQuickWidget.ResizeMode QQuickWidget.setResizeMode()'''
        return QQuickWidget.ResizeMode()
    def resizeMode(self):
        '''QQuickWidget.ResizeMode QQuickWidget.resizeMode()'''
        return QQuickWidget.ResizeMode()
    def rootObject(self):
        '''QQuickItem QQuickWidget.rootObject()'''
        return QQuickItem()
    def rootContext(self):
        '''QQmlContext QQuickWidget.rootContext()'''
        return QQmlContext()
    def engine(self):
        '''QQmlEngine QQuickWidget.engine()'''
        return QQmlEngine()
    def source(self):
        '''QUrl QQuickWidget.source()'''
        return QUrl()


