class pyqtSignal():
 def connect(self, targetSignal): pass
 def emit(self, *args): pass
from QtCore import *

from QtWidgets import *

import datetime

class QWebChannel(QObject):
    """"""
    def __init__(self, parent = None):
        '''void QWebChannel.__init__(QObject parent = None)'''
    def disconnectFrom(self, transport):
        '''void QWebChannel.disconnectFrom(QWebChannelAbstractTransport transport)'''
    def connectTo(self, transport):
        '''void QWebChannel.connectTo(QWebChannelAbstractTransport transport)'''
    blockUpdatesChanged = pyqtSignal() # void blockUpdatesChanged(bool) - signal
    def setBlockUpdates(self, block):
        '''void QWebChannel.setBlockUpdates(bool block)'''
    def blockUpdates(self):
        '''bool QWebChannel.blockUpdates()'''
        return bool()
    def deregisterObject(self, object):
        '''void QWebChannel.deregisterObject(QObject object)'''
    def registerObject(self, id, object):
        '''void QWebChannel.registerObject(str id, QObject object)'''
    def registeredObjects(self):
        '''dict-of-QString-QObject QWebChannel.registeredObjects()'''
        return {str():QObject()}
    def registerObjects(self, objects):
        '''void QWebChannel.registerObjects(dict-of-QString-QObject objects)'''


class QWebChannelAbstractTransport(QObject):
    """"""
    def __init__(self, parent = None):
        '''void QWebChannelAbstractTransport.__init__(QObject parent = None)'''
    messageReceived = pyqtSignal() # void messageReceived(const QJsonObjectamp;,QWebChannelAbstractTransport*) - signal
    def sendMessage(self, message):
        '''abstract void QWebChannelAbstractTransport.sendMessage(dict-of-str-QJsonValue message)'''


