class pyqtSignal():
 def connect(self, targetSignal): pass
 def emit(self, *args): pass
from QtCore import *

from QtWidgets import *

import datetime

class QMaskGenerator(QObject):
    """"""
    def __init__(self, parent = None):
        '''void QMaskGenerator.__init__(QObject parent = None)'''
    def nextMask(self):
        '''abstract int QMaskGenerator.nextMask()'''
        return int()
    def seed(self):
        '''abstract bool QMaskGenerator.seed()'''
        return bool()


class QWebSocket(QObject):
    """"""
    def __init__(self, origin = None, version = None, parent = None):
        '''void QWebSocket.__init__(str origin = '', QWebSocketProtocol.Version version = QWebSocketProtocol.Version13, QObject parent = None)'''
    sslErrors = pyqtSignal() # void sslErrors(const QListlt;QSslErrorgt;amp;) - signal
    bytesWritten = pyqtSignal() # void bytesWritten(qint64) - signal
    pong = pyqtSignal() # void pong(quint64,const QByteArrayamp;) - signal
    binaryMessageReceived = pyqtSignal() # void binaryMessageReceived(const QByteArrayamp;) - signal
    textMessageReceived = pyqtSignal() # void textMessageReceived(const QStringamp;) - signal
    binaryFrameReceived = pyqtSignal() # void binaryFrameReceived(const QByteArrayamp;,bool) - signal
    textFrameReceived = pyqtSignal() # void textFrameReceived(const QStringamp;,bool) - signal
    readChannelFinished = pyqtSignal() # void readChannelFinished() - signal
    proxyAuthenticationRequired = pyqtSignal() # void proxyAuthenticationRequired(const QNetworkProxyamp;,QAuthenticator*) - signal
    stateChanged = pyqtSignal() # void stateChanged(QAbstractSocket::SocketState) - signal
    disconnected = pyqtSignal() # void disconnected() - signal
    connected = pyqtSignal() # void connected() - signal
    aboutToClose = pyqtSignal() # void aboutToClose() - signal
    def ping(self, payload = QByteArray()):
        '''void QWebSocket.ping(QByteArray payload = QByteArray())'''
    def open(self, url):
        '''void QWebSocket.open(QUrl url)'''
    def close(self, closeCode = None, reason = str()):
        '''void QWebSocket.close(QWebSocketProtocol.CloseCode closeCode = QWebSocketProtocol.CloseCodeNormal, str reason = str())'''
    def sslConfiguration(self):
        '''QSslConfiguration QWebSocket.sslConfiguration()'''
        return QSslConfiguration()
    def setSslConfiguration(self, sslConfiguration):
        '''void QWebSocket.setSslConfiguration(QSslConfiguration sslConfiguration)'''
    def ignoreSslErrors(self, errors):
        '''void QWebSocket.ignoreSslErrors(list-of-QSslError errors)'''
    def ignoreSslErrors(self):
        '''void QWebSocket.ignoreSslErrors()'''
    def sendBinaryMessage(self, data):
        '''int QWebSocket.sendBinaryMessage(QByteArray data)'''
        return int()
    def sendTextMessage(self, message):
        '''int QWebSocket.sendTextMessage(str message)'''
        return int()
    def closeReason(self):
        '''str QWebSocket.closeReason()'''
        return str()
    def closeCode(self):
        '''QWebSocketProtocol.CloseCode QWebSocket.closeCode()'''
        return QWebSocketProtocol.CloseCode()
    def origin(self):
        '''str QWebSocket.origin()'''
        return str()
    def requestUrl(self):
        '''QUrl QWebSocket.requestUrl()'''
        return QUrl()
    def resourceName(self):
        '''str QWebSocket.resourceName()'''
        return str()
    def version(self):
        '''QWebSocketProtocol.Version QWebSocket.version()'''
        return QWebSocketProtocol.Version()
    def state(self):
        '''QAbstractSocket.SocketState QWebSocket.state()'''
        return QAbstractSocket.SocketState()
    def setPauseMode(self, pauseMode):
        '''void QWebSocket.setPauseMode(QAbstractSocket.PauseModes pauseMode)'''
    def resume(self):
        '''void QWebSocket.resume()'''
    def setReadBufferSize(self, size):
        '''void QWebSocket.setReadBufferSize(int size)'''
    def readBufferSize(self):
        '''int QWebSocket.readBufferSize()'''
        return int()
    def maskGenerator(self):
        '''QMaskGenerator QWebSocket.maskGenerator()'''
        return QMaskGenerator()
    def setMaskGenerator(self, maskGenerator):
        '''void QWebSocket.setMaskGenerator(QMaskGenerator maskGenerator)'''
    def setProxy(self, networkProxy):
        '''void QWebSocket.setProxy(QNetworkProxy networkProxy)'''
    def proxy(self):
        '''QNetworkProxy QWebSocket.proxy()'''
        return QNetworkProxy()
    def peerPort(self):
        '''int QWebSocket.peerPort()'''
        return int()
    def peerName(self):
        '''str QWebSocket.peerName()'''
        return str()
    def peerAddress(self):
        '''QHostAddress QWebSocket.peerAddress()'''
        return QHostAddress()
    def pauseMode(self):
        '''QAbstractSocket.PauseModes QWebSocket.pauseMode()'''
        return QAbstractSocket.PauseModes()
    def localPort(self):
        '''int QWebSocket.localPort()'''
        return int()
    def localAddress(self):
        '''QHostAddress QWebSocket.localAddress()'''
        return QHostAddress()
    def isValid(self):
        '''bool QWebSocket.isValid()'''
        return bool()
    def flush(self):
        '''bool QWebSocket.flush()'''
        return bool()
    def errorString(self):
        '''str QWebSocket.errorString()'''
        return str()
    def error(self):
        '''QAbstractSocket.SocketError QWebSocket.error()'''
        return QAbstractSocket.SocketError()
    error = pyqtSignal() # void error(QAbstractSocket::SocketError) - signal
    def abort(self):
        '''void QWebSocket.abort()'''


class QWebSocketCorsAuthenticator():
    """"""
    def __init__(self, origin):
        '''void QWebSocketCorsAuthenticator.__init__(str origin)'''
    def __init__(self, other):
        '''void QWebSocketCorsAuthenticator.__init__(QWebSocketCorsAuthenticator other)'''
    def allowed(self):
        '''bool QWebSocketCorsAuthenticator.allowed()'''
        return bool()
    def setAllowed(self, allowed):
        '''void QWebSocketCorsAuthenticator.setAllowed(bool allowed)'''
    def origin(self):
        '''str QWebSocketCorsAuthenticator.origin()'''
        return str()
    def swap(self, other):
        '''void QWebSocketCorsAuthenticator.swap(QWebSocketCorsAuthenticator other)'''


class QWebSocketProtocol():
    """"""
    # Enum QWebSocketProtocol.CloseCode
    CloseCodeNormal = 0
    CloseCodeGoingAway = 0
    CloseCodeProtocolError = 0
    CloseCodeDatatypeNotSupported = 0
    CloseCodeReserved1004 = 0
    CloseCodeMissingStatusCode = 0
    CloseCodeAbnormalDisconnection = 0
    CloseCodeWrongDatatype = 0
    CloseCodePolicyViolated = 0
    CloseCodeTooMuchData = 0
    CloseCodeMissingExtension = 0
    CloseCodeBadOperation = 0
    CloseCodeTlsHandshakeFailed = 0

    # Enum QWebSocketProtocol.Version
    VersionUnknown = 0
    Version0 = 0
    Version4 = 0
    Version5 = 0
    Version6 = 0
    Version7 = 0
    Version8 = 0
    Version13 = 0
    VersionLatest = 0



class QWebSocketServer(QObject):
    """"""
    # Enum QWebSocketServer.SslMode
    SecureMode = 0
    NonSecureMode = 0

    def __init__(self, serverName, secureMode, parent = None):
        '''void QWebSocketServer.__init__(str serverName, QWebSocketServer.SslMode secureMode, QObject parent = None)'''
    closed = pyqtSignal() # void closed() - signal
    sslErrors = pyqtSignal() # void sslErrors(const QListlt;QSslErrorgt;amp;) - signal
    peerVerifyError = pyqtSignal() # void peerVerifyError(const QSslErroramp;) - signal
    newConnection = pyqtSignal() # void newConnection() - signal
    originAuthenticationRequired = pyqtSignal() # void originAuthenticationRequired(QWebSocketCorsAuthenticator*) - signal
    serverError = pyqtSignal() # void serverError(QWebSocketProtocol::CloseCode) - signal
    acceptError = pyqtSignal() # void acceptError(QAbstractSocket::SocketError) - signal
    def serverUrl(self):
        '''QUrl QWebSocketServer.serverUrl()'''
        return QUrl()
    def supportedVersions(self):
        '''list-of-QWebSocketProtocol.Version QWebSocketServer.supportedVersions()'''
        return [QWebSocketProtocol.Version()]
    def sslConfiguration(self):
        '''QSslConfiguration QWebSocketServer.sslConfiguration()'''
        return QSslConfiguration()
    def setSslConfiguration(self, sslConfiguration):
        '''void QWebSocketServer.setSslConfiguration(QSslConfiguration sslConfiguration)'''
    def proxy(self):
        '''QNetworkProxy QWebSocketServer.proxy()'''
        return QNetworkProxy()
    def setProxy(self, networkProxy):
        '''void QWebSocketServer.setProxy(QNetworkProxy networkProxy)'''
    def serverName(self):
        '''str QWebSocketServer.serverName()'''
        return str()
    def setServerName(self, serverName):
        '''void QWebSocketServer.setServerName(str serverName)'''
    def resumeAccepting(self):
        '''void QWebSocketServer.resumeAccepting()'''
    def pauseAccepting(self):
        '''void QWebSocketServer.pauseAccepting()'''
    def errorString(self):
        '''str QWebSocketServer.errorString()'''
        return str()
    def error(self):
        '''QWebSocketProtocol.CloseCode QWebSocketServer.error()'''
        return QWebSocketProtocol.CloseCode()
    def nextPendingConnection(self):
        '''QWebSocket QWebSocketServer.nextPendingConnection()'''
        return QWebSocket()
    def hasPendingConnections(self):
        '''bool QWebSocketServer.hasPendingConnections()'''
        return bool()
    def socketDescriptor(self):
        '''int QWebSocketServer.socketDescriptor()'''
        return int()
    def setSocketDescriptor(self, socketDescriptor):
        '''bool QWebSocketServer.setSocketDescriptor(int socketDescriptor)'''
        return bool()
    def secureMode(self):
        '''QWebSocketServer.SslMode QWebSocketServer.secureMode()'''
        return QWebSocketServer.SslMode()
    def serverAddress(self):
        '''QHostAddress QWebSocketServer.serverAddress()'''
        return QHostAddress()
    def serverPort(self):
        '''int QWebSocketServer.serverPort()'''
        return int()
    def maxPendingConnections(self):
        '''int QWebSocketServer.maxPendingConnections()'''
        return int()
    def setMaxPendingConnections(self, numConnections):
        '''void QWebSocketServer.setMaxPendingConnections(int numConnections)'''
    def isListening(self):
        '''bool QWebSocketServer.isListening()'''
        return bool()
    def close(self):
        '''void QWebSocketServer.close()'''
    def listen(self, address = None, port = 0):
        '''bool QWebSocketServer.listen(QHostAddress address = QHostAddress.Any, int port = 0)'''
        return bool()


