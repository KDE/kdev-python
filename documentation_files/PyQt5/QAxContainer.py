class pyqtSignal():
 def connect(self, targetSignal): pass
 def emit(self, *args): pass
from QtCore import *

from QtWidgets import *

import datetime

class QAxBase():
    """"""
    def __init__(self):
        '''void QAxBase.__init__()'''
    def __init__(self):
        '''QAxBase QAxBase.__init__()'''
        return QAxBase()
    def disableEventSink(self):
        '''void QAxBase.disableEventSink()'''
    def disableClassInfo(self):
        '''void QAxBase.disableClassInfo()'''
    def disableMetaObject(self):
        '''void QAxBase.disableMetaObject()'''
    def setControl(self):
        '''str QAxBase.setControl()'''
        return str()
    def clear(self):
        '''void QAxBase.clear()'''
    exception = pyqtSignal() # void exception(int,const QStringamp;,const QStringamp;,const QStringamp;) - signal
    propertyChanged = pyqtSignal() # void propertyChanged(const QStringamp;) - signal
    signal = pyqtSignal() # void signal(const QStringamp;,int,void*) - signal
    def asVariant(self):
        '''QVariant QAxBase.asVariant()'''
        return QVariant()
    def verbs(self):
        '''list-of-str QAxBase.verbs()'''
        return [str()]
    def isNull(self):
        '''bool QAxBase.isNull()'''
        return bool()
    def setPropertyWritable(self):
        '''bool QAxBase.setPropertyWritable()'''
        return bool()
    def propertyWritable(self):
        '''str QAxBase.propertyWritable()'''
        return str()
    def generateDocumentation(self):
        '''str QAxBase.generateDocumentation()'''
        return str()
    def setPropertyBag(self):
        '''dict-of-str-object QAxBase.setPropertyBag()'''
        return {str():object()}
    def propertyBag(self):
        '''dict-of-str-object QAxBase.propertyBag()'''
        return {str():object()}
    def querySubObject(self):
        '''list-of-QVariant QAxBase.querySubObject()'''
        return [QVariant()]
    def querySubObject(self, value1 = QVariant(), value2 = QVariant(), value3 = QVariant(), value4 = QVariant(), value5 = QVariant(), value6 = QVariant(), value7 = QVariant(), value8 = QVariant()):
        '''str QAxBase.querySubObject(QVariant value1 = QVariant(), QVariant value2 = QVariant(), QVariant value3 = QVariant(), QVariant value4 = QVariant(), QVariant value5 = QVariant(), QVariant value6 = QVariant(), QVariant value7 = QVariant(), QVariant value8 = QVariant())'''
        return str()
    def dynamicCall(self):
        '''list-of-QVariant QAxBase.dynamicCall()'''
        return [QVariant()]
    def dynamicCall(self, value1 = QVariant(), value2 = QVariant(), value3 = QVariant(), value4 = QVariant(), value5 = QVariant(), value6 = QVariant(), value7 = QVariant(), value8 = QVariant()):
        '''str QAxBase.dynamicCall(QVariant value1 = QVariant(), QVariant value2 = QVariant(), QVariant value3 = QVariant(), QVariant value4 = QVariant(), QVariant value5 = QVariant(), QVariant value6 = QVariant(), QVariant value7 = QVariant(), QVariant value8 = QVariant())'''
        return str()
    def control(self):
        '''str QAxBase.control()'''
        return str()


class QAxObject(QObject, QAxBase):
    """"""
    def __init__(self, parent = None):
        '''void QAxObject.__init__(QObject parent = None)'''
    def __init__(self, parent = None):
        '''str QAxObject.__init__(QObject parent = None)'''
        return str()
    def connectNotify(self):
        '''QMetaMethod QAxObject.connectNotify()'''
        return QMetaMethod()
    def doVerb(self):
        '''str QAxObject.doVerb()'''
        return str()


class QAxWidget(QWidget, QAxBase):
    """"""
    def __init__(self, parent = None, flags = 0):
        '''void QAxWidget.__init__(QWidget parent = None, Qt.WindowFlags flags = 0)'''
    def __init__(self, parent = None, flags = 0):
        '''str QAxWidget.__init__(QWidget parent = None, Qt.WindowFlags flags = 0)'''
        return str()
    def connectNotify(self):
        '''QMetaMethod QAxWidget.connectNotify()'''
        return QMetaMethod()
    def translateKeyEvent(self):
        '''int QAxWidget.translateKeyEvent()'''
        return int()
    def resizeEvent(self):
        '''QResizeEvent QAxWidget.resizeEvent()'''
        return QResizeEvent()
    def changeEvent(self):
        '''QEvent QAxWidget.changeEvent()'''
        return QEvent()
    def createHostWindow(self):
        '''bool QAxWidget.createHostWindow()'''
        return bool()
    def minimumSizeHint(self):
        '''QSize QAxWidget.minimumSizeHint()'''
        return QSize()
    def sizeHint(self):
        '''QSize QAxWidget.sizeHint()'''
        return QSize()
    def doVerb(self):
        '''str QAxWidget.doVerb()'''
        return str()
    def clear(self):
        '''void QAxWidget.clear()'''


