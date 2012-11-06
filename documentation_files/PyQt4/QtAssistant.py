class pyqtSignal():
 def connect(self, targetSignal): pass
 def emit(self, *args): pass
from QtCore import *

class QAssistantClient(QObject):
    """"""
    def __init__(self, path, parent = None):
        '''void QAssistantClient.__init__(QString path, QObject parent = None)'''
    error = pyqtSignal() # void error(const QStringamp;) - signal
    assistantClosed = pyqtSignal() # void assistantClosed() - signal
    assistantOpened = pyqtSignal() # void assistantOpened() - signal
    def showPage(self, page):
        '''void QAssistantClient.showPage(QString page)'''
    def closeAssistant(self):
        '''void QAssistantClient.closeAssistant()'''
    def openAssistant(self):
        '''void QAssistantClient.openAssistant()'''
    def setArguments(self, arguments):
        '''void QAssistantClient.setArguments(QStringList arguments)'''
    def isOpen(self):
        '''bool QAssistantClient.isOpen()'''
        return bool()


