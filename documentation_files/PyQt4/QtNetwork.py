class pyqtSignal():
 def connect(self, targetSignal): pass
 def emit(self, *args): pass
from QtCore import *

class QNetworkCacheMetaData():
    """"""
    def __init__(self):
        '''void QNetworkCacheMetaData.__init__()'''
    def __init__(self, other):
        '''void QNetworkCacheMetaData.__init__(QNetworkCacheMetaData other)'''
    def setAttributes(self, attributes):
        '''void QNetworkCacheMetaData.setAttributes(dict-of-QNetworkRequest.Attribute-QVariant attributes)'''
    def attributes(self):
        '''dict-of-QNetworkRequest.Attribute-QVariant QNetworkCacheMetaData.attributes()'''
        return dict-of-QNetworkRequest.Attribute-QVariant()
    def setSaveToDisk(self, allow):
        '''void QNetworkCacheMetaData.setSaveToDisk(bool allow)'''
    def saveToDisk(self):
        '''bool QNetworkCacheMetaData.saveToDisk()'''
        return bool()
    def setExpirationDate(self, dateTime):
        '''void QNetworkCacheMetaData.setExpirationDate(QDateTime dateTime)'''
    def expirationDate(self):
        '''QDateTime QNetworkCacheMetaData.expirationDate()'''
        return QDateTime()
    def setLastModified(self, dateTime):
        '''void QNetworkCacheMetaData.setLastModified(QDateTime dateTime)'''
    def lastModified(self):
        '''QDateTime QNetworkCacheMetaData.lastModified()'''
        return QDateTime()
    def setRawHeaders(self, headers):
        '''void QNetworkCacheMetaData.setRawHeaders(list-of-tuple-of-QByteArray-QByteArray headers)'''
    def rawHeaders(self):
        '''list-of-tuple-of-QByteArray-QByteArray QNetworkCacheMetaData.rawHeaders()'''
        return [tuple-of-QByteArray-QByteArray()]
    def setUrl(self, url):
        '''void QNetworkCacheMetaData.setUrl(QUrl url)'''
    def url(self):
        '''QUrl QNetworkCacheMetaData.url()'''
        return QUrl()
    def isValid(self):
        '''bool QNetworkCacheMetaData.isValid()'''
        return bool()
    def __ne__(self, other):
        '''bool QNetworkCacheMetaData.__ne__(QNetworkCacheMetaData other)'''
        return bool()
    def __eq__(self, other):
        '''bool QNetworkCacheMetaData.__eq__(QNetworkCacheMetaData other)'''
        return bool()


class QAbstractNetworkCache(QObject):
    """"""
    def __init__(self, parent = None):
        '''void QAbstractNetworkCache.__init__(QObject parent = None)'''
    def clear(self):
        '''abstract void QAbstractNetworkCache.clear()'''
    def insert(self, device):
        '''abstract void QAbstractNetworkCache.insert(QIODevice device)'''
    def prepare(self, metaData):
        '''abstract QIODevice QAbstractNetworkCache.prepare(QNetworkCacheMetaData metaData)'''
        return QIODevice()
    def cacheSize(self):
        '''abstract int QAbstractNetworkCache.cacheSize()'''
        return int()
    def remove(self, url):
        '''abstract bool QAbstractNetworkCache.remove(QUrl url)'''
        return bool()
    def data(self, url):
        '''abstract QIODevice QAbstractNetworkCache.data(QUrl url)'''
        return QIODevice()
    def updateMetaData(self, metaData):
        '''abstract void QAbstractNetworkCache.updateMetaData(QNetworkCacheMetaData metaData)'''
    def metaData(self, url):
        '''abstract QNetworkCacheMetaData QAbstractNetworkCache.metaData(QUrl url)'''
        return QNetworkCacheMetaData()


class QAbstractSocket(QIODevice):
    """"""
    # Enum QAbstractSocket.SocketOption
    LowDelayOption = 0
    KeepAliveOption = 0
    MulticastTtlOption = 0
    MulticastLoopbackOption = 0

    # Enum QAbstractSocket.SocketState
    UnconnectedState = 0
    HostLookupState = 0
    ConnectingState = 0
    ConnectedState = 0
    BoundState = 0
    ListeningState = 0
    ClosingState = 0

    # Enum QAbstractSocket.SocketError
    ConnectionRefusedError = 0
    RemoteHostClosedError = 0
    HostNotFoundError = 0
    SocketAccessError = 0
    SocketResourceError = 0
    SocketTimeoutError = 0
    DatagramTooLargeError = 0
    NetworkError = 0
    AddressInUseError = 0
    SocketAddressNotAvailableError = 0
    UnsupportedSocketOperationError = 0
    UnfinishedSocketOperationError = 0
    ProxyAuthenticationRequiredError = 0
    SslHandshakeFailedError = 0
    ProxyConnectionRefusedError = 0
    ProxyConnectionClosedError = 0
    ProxyConnectionTimeoutError = 0
    ProxyNotFoundError = 0
    ProxyProtocolError = 0
    UnknownSocketError = 0

    # Enum QAbstractSocket.NetworkLayerProtocol
    IPv4Protocol = 0
    IPv6Protocol = 0
    UnknownNetworkLayerProtocol = 0

    # Enum QAbstractSocket.SocketType
    TcpSocket = 0
    UdpSocket = 0
    UnknownSocketType = 0

    def __init__(self, socketType, parent):
        '''void QAbstractSocket.__init__(QAbstractSocket.SocketType socketType, QObject parent)'''
    def socketOption(self, option):
        '''QVariant QAbstractSocket.socketOption(QAbstractSocket.SocketOption option)'''
        return QVariant()
    def setSocketOption(self, option, value):
        '''void QAbstractSocket.setSocketOption(QAbstractSocket.SocketOption option, QVariant value)'''
    def setPeerName(self, name):
        '''void QAbstractSocket.setPeerName(QString name)'''
    def setPeerAddress(self, address):
        '''void QAbstractSocket.setPeerAddress(QHostAddress address)'''
    def setPeerPort(self, port):
        '''void QAbstractSocket.setPeerPort(int port)'''
    def setLocalAddress(self, address):
        '''void QAbstractSocket.setLocalAddress(QHostAddress address)'''
    def setLocalPort(self, port):
        '''void QAbstractSocket.setLocalPort(int port)'''
    def setSocketError(self, socketError):
        '''void QAbstractSocket.setSocketError(QAbstractSocket.SocketError socketError)'''
    def setSocketState(self, state):
        '''void QAbstractSocket.setSocketState(QAbstractSocket.SocketState state)'''
    def writeData(self, data):
        '''int QAbstractSocket.writeData(str data)'''
        return int()
    def readLineData(self, maxlen):
        '''str QAbstractSocket.readLineData(int maxlen)'''
        return str()
    def readData(self, maxlen):
        '''str QAbstractSocket.readData(int maxlen)'''
        return str()
    def disconnectFromHostImplementation(self):
        '''void QAbstractSocket.disconnectFromHostImplementation()'''
    def connectToHostImplementation(self, hostName, port, mode = None):
        '''void QAbstractSocket.connectToHostImplementation(QString hostName, int port, QIODevice.OpenMode mode = QIODevice.ReadWrite)'''
    proxyAuthenticationRequired = pyqtSignal() # void proxyAuthenticationRequired(const QNetworkProxyamp;,QAuthenticator *) - signal
    stateChanged = pyqtSignal() # void stateChanged(QAbstractSocket::SocketState) - signal
    disconnected = pyqtSignal() # void disconnected() - signal
    connected = pyqtSignal() # void connected() - signal
    hostFound = pyqtSignal() # void hostFound() - signal
    def proxy(self):
        '''QNetworkProxy QAbstractSocket.proxy()'''
        return QNetworkProxy()
    def setProxy(self, networkProxy):
        '''void QAbstractSocket.setProxy(QNetworkProxy networkProxy)'''
    def waitForDisconnected(self, msecs = 30000):
        '''bool QAbstractSocket.waitForDisconnected(int msecs = 30000)'''
        return bool()
    def waitForBytesWritten(self, msecs = 30000):
        '''bool QAbstractSocket.waitForBytesWritten(int msecs = 30000)'''
        return bool()
    def waitForReadyRead(self, msecs = 30000):
        '''bool QAbstractSocket.waitForReadyRead(int msecs = 30000)'''
        return bool()
    def waitForConnected(self, msecs = 30000):
        '''bool QAbstractSocket.waitForConnected(int msecs = 30000)'''
        return bool()
    def flush(self):
        '''bool QAbstractSocket.flush()'''
        return bool()
    def atEnd(self):
        '''bool QAbstractSocket.atEnd()'''
        return bool()
    def isSequential(self):
        '''bool QAbstractSocket.isSequential()'''
        return bool()
    def close(self):
        '''void QAbstractSocket.close()'''
    def error(self):
        '''QAbstractSocket.SocketError QAbstractSocket.error()'''
        return QAbstractSocket.SocketError()
    error = pyqtSignal() # void error(QAbstractSocket::SocketError) - signal
    def state(self):
        '''QAbstractSocket.SocketState QAbstractSocket.state()'''
        return QAbstractSocket.SocketState()
    def socketType(self):
        '''QAbstractSocket.SocketType QAbstractSocket.socketType()'''
        return QAbstractSocket.SocketType()
    def setSocketDescriptor(self, socketDescriptor, state = None, mode = None):
        '''bool QAbstractSocket.setSocketDescriptor(int socketDescriptor, QAbstractSocket.SocketState state = QAbstractSocket.ConnectedState, QIODevice.OpenMode mode = QIODevice.ReadWrite)'''
        return bool()
    def socketDescriptor(self):
        '''int QAbstractSocket.socketDescriptor()'''
        return int()
    def abort(self):
        '''void QAbstractSocket.abort()'''
    def setReadBufferSize(self, size):
        '''void QAbstractSocket.setReadBufferSize(int size)'''
    def readBufferSize(self):
        '''int QAbstractSocket.readBufferSize()'''
        return int()
    def peerName(self):
        '''QString QAbstractSocket.peerName()'''
        return QString()
    def peerAddress(self):
        '''QHostAddress QAbstractSocket.peerAddress()'''
        return QHostAddress()
    def peerPort(self):
        '''int QAbstractSocket.peerPort()'''
        return int()
    def localAddress(self):
        '''QHostAddress QAbstractSocket.localAddress()'''
        return QHostAddress()
    def localPort(self):
        '''int QAbstractSocket.localPort()'''
        return int()
    def canReadLine(self):
        '''bool QAbstractSocket.canReadLine()'''
        return bool()
    def bytesToWrite(self):
        '''int QAbstractSocket.bytesToWrite()'''
        return int()
    def bytesAvailable(self):
        '''int QAbstractSocket.bytesAvailable()'''
        return int()
    def isValid(self):
        '''bool QAbstractSocket.isValid()'''
        return bool()
    def disconnectFromHost(self):
        '''void QAbstractSocket.disconnectFromHost()'''
    def connectToHost(self, hostName, port, mode = None):
        '''void QAbstractSocket.connectToHost(QString hostName, int port, QIODevice.OpenMode mode = QIODevice.ReadWrite)'''
    def connectToHost(self, address, port, mode = None):
        '''void QAbstractSocket.connectToHost(QHostAddress address, int port, QIODevice.OpenMode mode = QIODevice.ReadWrite)'''


class QAuthenticator():
    """"""
    def __init__(self):
        '''void QAuthenticator.__init__()'''
    def __init__(self, other):
        '''void QAuthenticator.__init__(QAuthenticator other)'''
    def setOption(self, opt, value):
        '''void QAuthenticator.setOption(QString opt, QVariant value)'''
    def options(self):
        '''dict-of-QString-QVariant QAuthenticator.options()'''
        return dict-of-QString-QVariant()
    def option(self, opt):
        '''QVariant QAuthenticator.option(QString opt)'''
        return QVariant()
    def isNull(self):
        '''bool QAuthenticator.isNull()'''
        return bool()
    def realm(self):
        '''QString QAuthenticator.realm()'''
        return QString()
    def setPassword(self, password):
        '''void QAuthenticator.setPassword(QString password)'''
    def password(self):
        '''QString QAuthenticator.password()'''
        return QString()
    def setUser(self, user):
        '''void QAuthenticator.setUser(QString user)'''
    def user(self):
        '''QString QAuthenticator.user()'''
        return QString()
    def __ne__(self, other):
        '''bool QAuthenticator.__ne__(QAuthenticator other)'''
        return bool()
    def __eq__(self, other):
        '''bool QAuthenticator.__eq__(QAuthenticator other)'''
        return bool()


class QFtp(QObject):
    """"""
    # Enum QFtp.TransferType
    Binary = 0
    Ascii = 0

    # Enum QFtp.TransferMode
    Active = 0
    Passive = 0

    # Enum QFtp.Command
    None_ = 0
    SetTransferMode = 0
    SetProxy = 0
    ConnectToHost = 0
    Login = 0
    Close = 0
    List = 0
    Cd = 0
    Get = 0
    Put = 0
    Remove = 0
    Mkdir = 0
    Rmdir = 0
    Rename = 0
    RawCommand = 0

    # Enum QFtp.Error
    NoError = 0
    UnknownError = 0
    HostNotFound = 0
    ConnectionRefused = 0
    NotConnected = 0

    # Enum QFtp.State
    Unconnected = 0
    HostLookup = 0
    Connecting = 0
    Connected = 0
    LoggedIn = 0
    Closing = 0

    def __init__(self, parent = None):
        '''void QFtp.__init__(QObject parent = None)'''
    done = pyqtSignal() # void done(bool) - signal
    commandFinished = pyqtSignal() # void commandFinished(int,bool) - signal
    commandStarted = pyqtSignal() # void commandStarted(int) - signal
    rawCommandReply = pyqtSignal() # void rawCommandReply(int,const QStringamp;) - signal
    dataTransferProgress = pyqtSignal() # void dataTransferProgress(qint64,qint64) - signal
    readyRead = pyqtSignal() # void readyRead() - signal
    listInfo = pyqtSignal() # void listInfo(const QUrlInfoamp;) - signal
    stateChanged = pyqtSignal() # void stateChanged(int) - signal
    def abort(self):
        '''void QFtp.abort()'''
    def errorString(self):
        '''QString QFtp.errorString()'''
        return QString()
    def error(self):
        '''QFtp.Error QFtp.error()'''
        return QFtp.Error()
    def state(self):
        '''QFtp.State QFtp.state()'''
        return QFtp.State()
    def clearPendingCommands(self):
        '''void QFtp.clearPendingCommands()'''
    def hasPendingCommands(self):
        '''bool QFtp.hasPendingCommands()'''
        return bool()
    def currentCommand(self):
        '''QFtp.Command QFtp.currentCommand()'''
        return QFtp.Command()
    def currentDevice(self):
        '''QIODevice QFtp.currentDevice()'''
        return QIODevice()
    def currentId(self):
        '''int QFtp.currentId()'''
        return int()
    def readAll(self):
        '''QByteArray QFtp.readAll()'''
        return QByteArray()
    def read(self, maxlen):
        '''str QFtp.read(int maxlen)'''
        return str()
    def bytesAvailable(self):
        '''int QFtp.bytesAvailable()'''
        return int()
    def rawCommand(self, command):
        '''int QFtp.rawCommand(QString command)'''
        return int()
    def rename(self, oldname, newname):
        '''int QFtp.rename(QString oldname, QString newname)'''
        return int()
    def rmdir(self, dir):
        '''int QFtp.rmdir(QString dir)'''
        return int()
    def mkdir(self, dir):
        '''int QFtp.mkdir(QString dir)'''
        return int()
    def remove(self, file):
        '''int QFtp.remove(QString file)'''
        return int()
    def put(self, data, file, type = None):
        '''int QFtp.put(QByteArray data, QString file, QFtp.TransferType type = QFtp.Binary)'''
        return int()
    def put(self, device, file, type = None):
        '''int QFtp.put(QIODevice device, QString file, QFtp.TransferType type = QFtp.Binary)'''
        return int()
    def get(self, file, device = None, type = None):
        '''int QFtp.get(QString file, QIODevice device = None, QFtp.TransferType type = QFtp.Binary)'''
        return int()
    def cd(self, directory):
        '''int QFtp.cd(QString directory)'''
        return int()
    def list(self, directory = QString()):
        '''int QFtp.list(QString directory = QString())'''
        return int()
    def setTransferMode(self, mode):
        '''int QFtp.setTransferMode(QFtp.TransferMode mode)'''
        return int()
    def close(self):
        '''int QFtp.close()'''
        return int()
    def login(self, user = QString(), password = QString()):
        '''int QFtp.login(QString user = QString(), QString password = QString())'''
        return int()
    def connectToHost(self, host, port = 21):
        '''int QFtp.connectToHost(QString host, int port = 21)'''
        return int()
    def setProxy(self, host, port):
        '''int QFtp.setProxy(QString host, int port)'''
        return int()


class QHostAddress():
    """"""
    # Enum QHostAddress.SpecialAddress
    Null = 0
    Broadcast = 0
    LocalHost = 0
    LocalHostIPv6 = 0
    Any = 0
    AnyIPv6 = 0

    def __init__(self):
        '''void QHostAddress.__init__()'''
    def __init__(self, address):
        '''void QHostAddress.__init__(QHostAddress.SpecialAddress address)'''
    def __init__(self, ip4Addr):
        '''void QHostAddress.__init__(int ip4Addr)'''
    def __init__(self, address):
        '''void QHostAddress.__init__(QString address)'''
    def __init__(self, ip6Addr):
        '''void QHostAddress.__init__(16-tuple-of-int ip6Addr)'''
    def __init__(self, copy):
        '''void QHostAddress.__init__(QHostAddress copy)'''
    def parseSubnet(self, subnet):
        '''static tuple-of-QHostAddress-int QHostAddress.parseSubnet(QString subnet)'''
        return tuple-of-QHostAddress-int()
    def isInSubnet(self, subnet, netmask):
        '''bool QHostAddress.isInSubnet(QHostAddress subnet, int netmask)'''
        return bool()
    def isInSubnet(self, subnet):
        '''bool QHostAddress.isInSubnet(tuple-of-QHostAddress-int subnet)'''
        return bool()
    def __hash__(self):
        '''int QHostAddress.__hash__()'''
        return int()
    def clear(self):
        '''void QHostAddress.clear()'''
    def isNull(self):
        '''bool QHostAddress.isNull()'''
        return bool()
    def __ne__(self, address):
        '''bool QHostAddress.__ne__(QHostAddress address)'''
        return bool()
    def __ne__(self, address):
        '''bool QHostAddress.__ne__(QHostAddress.SpecialAddress address)'''
        return bool()
    def __eq__(self, address):
        '''bool QHostAddress.__eq__(QHostAddress address)'''
        return bool()
    def __eq__(self, address):
        '''bool QHostAddress.__eq__(QHostAddress.SpecialAddress address)'''
        return bool()
    def setScopeId(self, id):
        '''void QHostAddress.setScopeId(QString id)'''
    def scopeId(self):
        '''QString QHostAddress.scopeId()'''
        return QString()
    def toString(self):
        '''QString QHostAddress.toString()'''
        return QString()
    def toIPv6Address(self):
        '''16-tuple-of-int QHostAddress.toIPv6Address()'''
        return 16-tuple-of-int()
    def toIPv4Address(self):
        '''int QHostAddress.toIPv4Address()'''
        return int()
    def protocol(self):
        '''QAbstractSocket.NetworkLayerProtocol QHostAddress.protocol()'''
        return QAbstractSocket.NetworkLayerProtocol()
    def setAddress(self, ip4Addr):
        '''void QHostAddress.setAddress(int ip4Addr)'''
    def setAddress(self, address):
        '''bool QHostAddress.setAddress(QString address)'''
        return bool()
    def setAddress(self, ip6Addr):
        '''void QHostAddress.setAddress(16-tuple-of-int ip6Addr)'''


class QHostInfo():
    """"""
    # Enum QHostInfo.HostInfoError
    NoError = 0
    HostNotFound = 0
    UnknownError = 0

    def __init__(self, id = None):
        '''void QHostInfo.__init__(int id = -1)'''
    def __init__(self, d):
        '''void QHostInfo.__init__(QHostInfo d)'''
    def localDomainName(self):
        '''static QString QHostInfo.localDomainName()'''
        return QString()
    def localHostName(self):
        '''static QString QHostInfo.localHostName()'''
        return QString()
    def fromName(self, name):
        '''static QHostInfo QHostInfo.fromName(QString name)'''
        return QHostInfo()
    def abortHostLookup(self, lookupId):
        '''static void QHostInfo.abortHostLookup(int lookupId)'''
    def lookupHost(self, name, receiver, member):
        '''static int QHostInfo.lookupHost(QString name, QObject receiver, SLOT(QHostInfo)SLOT() member)'''
        return int()
    def lookupHost(self, name, receiver):
        '''static int QHostInfo.lookupHost(QString name, callable receiver)'''
        return int()
    def lookupId(self):
        '''int QHostInfo.lookupId()'''
        return int()
    def setLookupId(self, id):
        '''void QHostInfo.setLookupId(int id)'''
    def setErrorString(self, errorString):
        '''void QHostInfo.setErrorString(QString errorString)'''
    def errorString(self):
        '''QString QHostInfo.errorString()'''
        return QString()
    def setError(self, error):
        '''void QHostInfo.setError(QHostInfo.HostInfoError error)'''
    def error(self):
        '''QHostInfo.HostInfoError QHostInfo.error()'''
        return QHostInfo.HostInfoError()
    def setAddresses(self, addresses):
        '''void QHostInfo.setAddresses(list-of-QHostAddress addresses)'''
    def addresses(self):
        '''list-of-QHostAddress QHostInfo.addresses()'''
        return [QHostAddress()]
    def setHostName(self, name):
        '''void QHostInfo.setHostName(QString name)'''
    def hostName(self):
        '''QString QHostInfo.hostName()'''
        return QString()


class QHttpHeader():
    """"""
    def __init__(self):
        '''void QHttpHeader.__init__()'''
    def __init__(self, header):
        '''void QHttpHeader.__init__(QHttpHeader header)'''
    def __init__(self, str):
        '''void QHttpHeader.__init__(QString str)'''
    def setValid(self):
        '''bool QHttpHeader.setValid()'''
        return bool()
    def parse(self, str):
        '''bool QHttpHeader.parse(QString str)'''
        return bool()
    def parseLine(self, line, number):
        '''bool QHttpHeader.parseLine(QString line, int number)'''
        return bool()
    def minorVersion(self):
        '''abstract int QHttpHeader.minorVersion()'''
        return int()
    def majorVersion(self):
        '''abstract int QHttpHeader.majorVersion()'''
        return int()
    def isValid(self):
        '''bool QHttpHeader.isValid()'''
        return bool()
    def toString(self):
        '''QString QHttpHeader.toString()'''
        return QString()
    def setContentType(self, type):
        '''void QHttpHeader.setContentType(QString type)'''
    def contentType(self):
        '''QString QHttpHeader.contentType()'''
        return QString()
    def hasContentType(self):
        '''bool QHttpHeader.hasContentType()'''
        return bool()
    def setContentLength(self, len):
        '''void QHttpHeader.setContentLength(int len)'''
    def contentLength(self):
        '''int QHttpHeader.contentLength()'''
        return int()
    def hasContentLength(self):
        '''bool QHttpHeader.hasContentLength()'''
        return bool()
    def removeAllValues(self, key):
        '''void QHttpHeader.removeAllValues(QString key)'''
    def removeValue(self, key):
        '''void QHttpHeader.removeValue(QString key)'''
    def allValues(self, key):
        '''QStringList QHttpHeader.allValues(QString key)'''
        return QStringList()
    def value(self, key):
        '''QString QHttpHeader.value(QString key)'''
        return QString()
    def keys(self):
        '''QStringList QHttpHeader.keys()'''
        return QStringList()
    def hasKey(self, key):
        '''bool QHttpHeader.hasKey(QString key)'''
        return bool()
    def values(self):
        '''list-of-tuple-of-QString-QString QHttpHeader.values()'''
        return [tuple-of-QString-QString()]
    def addValue(self, key, value):
        '''void QHttpHeader.addValue(QString key, QString value)'''
    def setValues(self, values):
        '''void QHttpHeader.setValues(list-of-tuple-of-QString-QString values)'''
    def setValue(self, key, value):
        '''void QHttpHeader.setValue(QString key, QString value)'''


class QHttpResponseHeader(QHttpHeader):
    """"""
    def __init__(self):
        '''void QHttpResponseHeader.__init__()'''
    def __init__(self, header):
        '''void QHttpResponseHeader.__init__(QHttpResponseHeader header)'''
    def __init__(self, str):
        '''void QHttpResponseHeader.__init__(QString str)'''
    def __init__(self, code, text = QString(), major = 1, minor = 1):
        '''void QHttpResponseHeader.__init__(int code, QString text = QString(), int major = 1, int minor = 1)'''
    def parseLine(self, line, number):
        '''bool QHttpResponseHeader.parseLine(QString line, int number)'''
        return bool()
    def toString(self):
        '''QString QHttpResponseHeader.toString()'''
        return QString()
    def minorVersion(self):
        '''int QHttpResponseHeader.minorVersion()'''
        return int()
    def majorVersion(self):
        '''int QHttpResponseHeader.majorVersion()'''
        return int()
    def reasonPhrase(self):
        '''QString QHttpResponseHeader.reasonPhrase()'''
        return QString()
    def statusCode(self):
        '''int QHttpResponseHeader.statusCode()'''
        return int()
    def setStatusLine(self, code, text = QString(), major = 1, minor = 1):
        '''void QHttpResponseHeader.setStatusLine(int code, QString text = QString(), int major = 1, int minor = 1)'''


class QHttpRequestHeader(QHttpHeader):
    """"""
    def __init__(self):
        '''void QHttpRequestHeader.__init__()'''
    def __init__(self, method, path, major = 1, minor = 1):
        '''void QHttpRequestHeader.__init__(QString method, QString path, int major = 1, int minor = 1)'''
    def __init__(self, header):
        '''void QHttpRequestHeader.__init__(QHttpRequestHeader header)'''
    def __init__(self, str):
        '''void QHttpRequestHeader.__init__(QString str)'''
    def parseLine(self, line, number):
        '''bool QHttpRequestHeader.parseLine(QString line, int number)'''
        return bool()
    def toString(self):
        '''QString QHttpRequestHeader.toString()'''
        return QString()
    def minorVersion(self):
        '''int QHttpRequestHeader.minorVersion()'''
        return int()
    def majorVersion(self):
        '''int QHttpRequestHeader.majorVersion()'''
        return int()
    def path(self):
        '''QString QHttpRequestHeader.path()'''
        return QString()
    def method(self):
        '''QString QHttpRequestHeader.method()'''
        return QString()
    def setRequest(self, method, path, major = 1, minor = 1):
        '''void QHttpRequestHeader.setRequest(QString method, QString path, int major = 1, int minor = 1)'''


class QHttp(QObject):
    """"""
    # Enum QHttp.Error
    NoError = 0
    UnknownError = 0
    HostNotFound = 0
    ConnectionRefused = 0
    UnexpectedClose = 0
    InvalidResponseHeader = 0
    WrongContentLength = 0
    Aborted = 0
    AuthenticationRequiredError = 0
    ProxyAuthenticationRequiredError = 0

    # Enum QHttp.State
    Unconnected = 0
    HostLookup = 0
    Connecting = 0
    Sending = 0
    Reading = 0
    Connected = 0
    Closing = 0

    # Enum QHttp.ConnectionMode
    ConnectionModeHttp = 0
    ConnectionModeHttps = 0

    def __init__(self, parent = None):
        '''void QHttp.__init__(QObject parent = None)'''
    def __init__(self, hostName, port = 80, parent = None):
        '''void QHttp.__init__(QString hostName, int port = 80, QObject parent = None)'''
    def __init__(self, hostname, mode, port = 0, parent = None):
        '''void QHttp.__init__(QString hostname, QHttp.ConnectionMode mode, int port = 0, QObject parent = None)'''
    sslErrors = pyqtSignal() # void sslErrors(const QListlt;QSslErrorgt;amp;) - signal
    authenticationRequired = pyqtSignal() # void authenticationRequired(const QStringamp;,quint16,QAuthenticator *) - signal
    proxyAuthenticationRequired = pyqtSignal() # void proxyAuthenticationRequired(const QNetworkProxyamp;,QAuthenticator *) - signal
    done = pyqtSignal() # void done(bool) - signal
    requestFinished = pyqtSignal() # void requestFinished(int,bool) - signal
    requestStarted = pyqtSignal() # void requestStarted(int) - signal
    dataReadProgress = pyqtSignal() # void dataReadProgress(int,int) - signal
    dataSendProgress = pyqtSignal() # void dataSendProgress(int,int) - signal
    readyRead = pyqtSignal() # void readyRead(const QHttpResponseHeaderamp;) - signal
    responseHeaderReceived = pyqtSignal() # void responseHeaderReceived(const QHttpResponseHeaderamp;) - signal
    stateChanged = pyqtSignal() # void stateChanged(int) - signal
    def ignoreSslErrors(self):
        '''void QHttp.ignoreSslErrors()'''
    def abort(self):
        '''void QHttp.abort()'''
    def errorString(self):
        '''QString QHttp.errorString()'''
        return QString()
    def error(self):
        '''QHttp.Error QHttp.error()'''
        return QHttp.Error()
    def state(self):
        '''QHttp.State QHttp.state()'''
        return QHttp.State()
    def clearPendingRequests(self):
        '''void QHttp.clearPendingRequests()'''
    def hasPendingRequests(self):
        '''bool QHttp.hasPendingRequests()'''
        return bool()
    def lastResponse(self):
        '''QHttpResponseHeader QHttp.lastResponse()'''
        return QHttpResponseHeader()
    def currentRequest(self):
        '''QHttpRequestHeader QHttp.currentRequest()'''
        return QHttpRequestHeader()
    def currentDestinationDevice(self):
        '''QIODevice QHttp.currentDestinationDevice()'''
        return QIODevice()
    def currentSourceDevice(self):
        '''QIODevice QHttp.currentSourceDevice()'''
        return QIODevice()
    def currentId(self):
        '''int QHttp.currentId()'''
        return int()
    def readAll(self):
        '''QByteArray QHttp.readAll()'''
        return QByteArray()
    def read(self, maxlen):
        '''str QHttp.read(int maxlen)'''
        return str()
    def bytesAvailable(self):
        '''int QHttp.bytesAvailable()'''
        return int()
    def close(self):
        '''int QHttp.close()'''
        return int()
    def request(self, header, data = None, to = None):
        '''int QHttp.request(QHttpRequestHeader header, QIODevice data = None, QIODevice to = None)'''
        return int()
    def request(self, header, data, to = None):
        '''int QHttp.request(QHttpRequestHeader header, QByteArray data, QIODevice to = None)'''
        return int()
    def head(self, path):
        '''int QHttp.head(QString path)'''
        return int()
    def post(self, path, data, to = None):
        '''int QHttp.post(QString path, QIODevice data, QIODevice to = None)'''
        return int()
    def post(self, path, data, to = None):
        '''int QHttp.post(QString path, QByteArray data, QIODevice to = None)'''
        return int()
    def get(self, path, to = None):
        '''int QHttp.get(QString path, QIODevice to = None)'''
        return int()
    def setProxy(self, host, port, user = QString(), password = QString()):
        '''int QHttp.setProxy(QString host, int port, QString user = QString(), QString password = QString())'''
        return int()
    def setProxy(self, proxy):
        '''int QHttp.setProxy(QNetworkProxy proxy)'''
        return int()
    def setUser(self, userName, password = QString()):
        '''int QHttp.setUser(QString userName, QString password = QString())'''
        return int()
    def setSocket(self, socket):
        '''int QHttp.setSocket(QTcpSocket socket)'''
        return int()
    def setHost(self, hostName, port = 80):
        '''int QHttp.setHost(QString hostName, int port = 80)'''
        return int()
    def setHost(self, hostname, mode, port = 0):
        '''int QHttp.setHost(QString hostname, QHttp.ConnectionMode mode, int port = 0)'''
        return int()


class QHttpPart():
    """"""
    def __init__(self):
        '''void QHttpPart.__init__()'''
    def __init__(self, other):
        '''void QHttpPart.__init__(QHttpPart other)'''
    def setBodyDevice(self, device):
        '''void QHttpPart.setBodyDevice(QIODevice device)'''
    def setBody(self, body):
        '''void QHttpPart.setBody(QByteArray body)'''
    def setRawHeader(self, headerName, headerValue):
        '''void QHttpPart.setRawHeader(QByteArray headerName, QByteArray headerValue)'''
    def setHeader(self, header, value):
        '''void QHttpPart.setHeader(QNetworkRequest.KnownHeaders header, QVariant value)'''
    def __ne__(self, other):
        '''bool QHttpPart.__ne__(QHttpPart other)'''
        return bool()
    def __eq__(self, other):
        '''bool QHttpPart.__eq__(QHttpPart other)'''
        return bool()


class QHttpMultiPart(QObject):
    """"""
    # Enum QHttpMultiPart.ContentType
    MixedType = 0
    RelatedType = 0
    FormDataType = 0
    AlternativeType = 0

    def __init__(self, parent = None):
        '''void QHttpMultiPart.__init__(QObject parent = None)'''
    def __init__(self, contentType, parent = None):
        '''void QHttpMultiPart.__init__(QHttpMultiPart.ContentType contentType, QObject parent = None)'''
    def setBoundary(self, boundary):
        '''void QHttpMultiPart.setBoundary(QByteArray boundary)'''
    def boundary(self):
        '''QByteArray QHttpMultiPart.boundary()'''
        return QByteArray()
    def setContentType(self, contentType):
        '''void QHttpMultiPart.setContentType(QHttpMultiPart.ContentType contentType)'''
    def append(self, httpPart):
        '''void QHttpMultiPart.append(QHttpPart httpPart)'''


class QLocalServer(QObject):
    """"""
    def __init__(self, parent = None):
        '''void QLocalServer.__init__(QObject parent = None)'''
    def incomingConnection(self, socketDescriptor):
        '''void QLocalServer.incomingConnection(sip.voidptr socketDescriptor)'''
    newConnection = pyqtSignal() # void newConnection() - signal
    def removeServer(self, name):
        '''static bool QLocalServer.removeServer(QString name)'''
        return bool()
    def waitForNewConnection(self, msecs = 0, timedOut = None):
        '''bool QLocalServer.waitForNewConnection(int msecs = 0, bool timedOut)'''
        return bool()
    def setMaxPendingConnections(self, numConnections):
        '''void QLocalServer.setMaxPendingConnections(int numConnections)'''
    def serverError(self):
        '''QAbstractSocket.SocketError QLocalServer.serverError()'''
        return QAbstractSocket.SocketError()
    def fullServerName(self):
        '''QString QLocalServer.fullServerName()'''
        return QString()
    def serverName(self):
        '''QString QLocalServer.serverName()'''
        return QString()
    def nextPendingConnection(self):
        '''QLocalSocket QLocalServer.nextPendingConnection()'''
        return QLocalSocket()
    def maxPendingConnections(self):
        '''int QLocalServer.maxPendingConnections()'''
        return int()
    def listen(self, name):
        '''bool QLocalServer.listen(QString name)'''
        return bool()
    def isListening(self):
        '''bool QLocalServer.isListening()'''
        return bool()
    def hasPendingConnections(self):
        '''bool QLocalServer.hasPendingConnections()'''
        return bool()
    def errorString(self):
        '''QString QLocalServer.errorString()'''
        return QString()
    def close(self):
        '''void QLocalServer.close()'''


class QLocalSocket(QIODevice):
    """"""
    # Enum QLocalSocket.LocalSocketState
    UnconnectedState = 0
    ConnectingState = 0
    ConnectedState = 0
    ClosingState = 0

    # Enum QLocalSocket.LocalSocketError
    ConnectionRefusedError = 0
    PeerClosedError = 0
    ServerNotFoundError = 0
    SocketAccessError = 0
    SocketResourceError = 0
    SocketTimeoutError = 0
    DatagramTooLargeError = 0
    ConnectionError = 0
    UnsupportedSocketOperationError = 0
    UnknownSocketError = 0

    def __init__(self, parent = None):
        '''void QLocalSocket.__init__(QObject parent = None)'''
    def writeData(self):
        '''str QLocalSocket.writeData()'''
        return str()
    def readData(self, maxlen):
        '''str QLocalSocket.readData(int maxlen)'''
        return str()
    stateChanged = pyqtSignal() # void stateChanged(QLocalSocket::LocalSocketState) - signal
    disconnected = pyqtSignal() # void disconnected() - signal
    connected = pyqtSignal() # void connected() - signal
    def waitForReadyRead(self, msecs = 30000):
        '''bool QLocalSocket.waitForReadyRead(int msecs = 30000)'''
        return bool()
    def waitForDisconnected(self, msecs = 30000):
        '''bool QLocalSocket.waitForDisconnected(int msecs = 30000)'''
        return bool()
    def waitForConnected(self, msecs = 30000):
        '''bool QLocalSocket.waitForConnected(int msecs = 30000)'''
        return bool()
    def waitForBytesWritten(self, msecs = 30000):
        '''bool QLocalSocket.waitForBytesWritten(int msecs = 30000)'''
        return bool()
    def state(self):
        '''QLocalSocket.LocalSocketState QLocalSocket.state()'''
        return QLocalSocket.LocalSocketState()
    def socketDescriptor(self):
        '''sip.voidptr QLocalSocket.socketDescriptor()'''
        return sip.voidptr()
    def setSocketDescriptor(self, socketDescriptor, state = None, mode = None):
        '''bool QLocalSocket.setSocketDescriptor(sip.voidptr socketDescriptor, QLocalSocket.LocalSocketState state = QLocalSocket.ConnectedState, QIODevice.OpenMode mode = QIODevice.ReadWrite)'''
        return bool()
    def setReadBufferSize(self, size):
        '''void QLocalSocket.setReadBufferSize(int size)'''
    def readBufferSize(self):
        '''int QLocalSocket.readBufferSize()'''
        return int()
    def isValid(self):
        '''bool QLocalSocket.isValid()'''
        return bool()
    def flush(self):
        '''bool QLocalSocket.flush()'''
        return bool()
    def error(self):
        '''QLocalSocket.LocalSocketError QLocalSocket.error()'''
        return QLocalSocket.LocalSocketError()
    error = pyqtSignal() # void error(QLocalSocket::LocalSocketError) - signal
    def close(self):
        '''void QLocalSocket.close()'''
    def canReadLine(self):
        '''bool QLocalSocket.canReadLine()'''
        return bool()
    def bytesToWrite(self):
        '''int QLocalSocket.bytesToWrite()'''
        return int()
    def bytesAvailable(self):
        '''int QLocalSocket.bytesAvailable()'''
        return int()
    def isSequential(self):
        '''bool QLocalSocket.isSequential()'''
        return bool()
    def abort(self):
        '''void QLocalSocket.abort()'''
    def fullServerName(self):
        '''QString QLocalSocket.fullServerName()'''
        return QString()
    def serverName(self):
        '''QString QLocalSocket.serverName()'''
        return QString()
    def disconnectFromServer(self):
        '''void QLocalSocket.disconnectFromServer()'''
    def connectToServer(self, name, mode = None):
        '''void QLocalSocket.connectToServer(QString name, QIODevice.OpenMode mode = QIODevice.ReadWrite)'''


class QNetworkAccessManager(QObject):
    """"""
    # Enum QNetworkAccessManager.NetworkAccessibility
    UnknownAccessibility = 0
    NotAccessible = 0
    Accessible = 0

    # Enum QNetworkAccessManager.Operation
    HeadOperation = 0
    GetOperation = 0
    PutOperation = 0
    PostOperation = 0
    DeleteOperation = 0
    CustomOperation = 0

    def __init__(self, parent = None):
        '''void QNetworkAccessManager.__init__(QObject parent = None)'''
    def networkAccessibleChanged(self, accessible):
        '''void QNetworkAccessManager.networkAccessibleChanged(QNetworkAccessManager.NetworkAccessibility accessible)'''
    def networkAccessible(self):
        '''QNetworkAccessManager.NetworkAccessibility QNetworkAccessManager.networkAccessible()'''
        return QNetworkAccessManager.NetworkAccessibility()
    def setNetworkAccessible(self, accessible):
        '''void QNetworkAccessManager.setNetworkAccessible(QNetworkAccessManager.NetworkAccessibility accessible)'''
    def activeConfiguration(self):
        '''QNetworkConfiguration QNetworkAccessManager.activeConfiguration()'''
        return QNetworkConfiguration()
    def configuration(self):
        '''QNetworkConfiguration QNetworkAccessManager.configuration()'''
        return QNetworkConfiguration()
    def setConfiguration(self, config):
        '''void QNetworkAccessManager.setConfiguration(QNetworkConfiguration config)'''
    def sendCustomRequest(self, request, verb, data = None):
        '''QNetworkReply QNetworkAccessManager.sendCustomRequest(QNetworkRequest request, QByteArray verb, QIODevice data = None)'''
        return QNetworkReply()
    def deleteResource(self, request):
        '''QNetworkReply QNetworkAccessManager.deleteResource(QNetworkRequest request)'''
        return QNetworkReply()
    def setCache(self, cache):
        '''void QNetworkAccessManager.setCache(QAbstractNetworkCache cache)'''
    def cache(self):
        '''QAbstractNetworkCache QNetworkAccessManager.cache()'''
        return QAbstractNetworkCache()
    def setProxyFactory(self, factory):
        '''void QNetworkAccessManager.setProxyFactory(QNetworkProxyFactory factory)'''
    def proxyFactory(self):
        '''QNetworkProxyFactory QNetworkAccessManager.proxyFactory()'''
        return QNetworkProxyFactory()
    def createRequest(self, op, request, device = None):
        '''QNetworkReply QNetworkAccessManager.createRequest(QNetworkAccessManager.Operation op, QNetworkRequest request, QIODevice device = None)'''
        return QNetworkReply()
    sslErrors = pyqtSignal() # void sslErrors(QNetworkReply *,const QListlt;QSslErrorgt;amp;) - signal
    finished = pyqtSignal() # void finished(QNetworkReply *) - signal
    authenticationRequired = pyqtSignal() # void authenticationRequired(QNetworkReply *,QAuthenticator *) - signal
    proxyAuthenticationRequired = pyqtSignal() # void proxyAuthenticationRequired(const QNetworkProxyamp;,QAuthenticator *) - signal
    def put(self, request, data):
        '''QNetworkReply QNetworkAccessManager.put(QNetworkRequest request, QIODevice data)'''
        return QNetworkReply()
    def put(self, request, data):
        '''QNetworkReply QNetworkAccessManager.put(QNetworkRequest request, QByteArray data)'''
        return QNetworkReply()
    def put(self, request, multiPart):
        '''QNetworkReply QNetworkAccessManager.put(QNetworkRequest request, QHttpMultiPart multiPart)'''
        return QNetworkReply()
    def post(self, request, data):
        '''QNetworkReply QNetworkAccessManager.post(QNetworkRequest request, QIODevice data)'''
        return QNetworkReply()
    def post(self, request, data):
        '''QNetworkReply QNetworkAccessManager.post(QNetworkRequest request, QByteArray data)'''
        return QNetworkReply()
    def post(self, request, multiPart):
        '''QNetworkReply QNetworkAccessManager.post(QNetworkRequest request, QHttpMultiPart multiPart)'''
        return QNetworkReply()
    def get(self, request):
        '''QNetworkReply QNetworkAccessManager.get(QNetworkRequest request)'''
        return QNetworkReply()
    def head(self, request):
        '''QNetworkReply QNetworkAccessManager.head(QNetworkRequest request)'''
        return QNetworkReply()
    def setCookieJar(self, cookieJar):
        '''void QNetworkAccessManager.setCookieJar(QNetworkCookieJar cookieJar)'''
    def cookieJar(self):
        '''QNetworkCookieJar QNetworkAccessManager.cookieJar()'''
        return QNetworkCookieJar()
    def setProxy(self, proxy):
        '''void QNetworkAccessManager.setProxy(QNetworkProxy proxy)'''
    def proxy(self):
        '''QNetworkProxy QNetworkAccessManager.proxy()'''
        return QNetworkProxy()


class QNetworkConfigurationManager(QObject):
    """"""
    # Enum QNetworkConfigurationManager.Capability
    CanStartAndStopInterfaces = 0
    DirectConnectionRouting = 0
    SystemSessionSupport = 0
    ApplicationLevelRoaming = 0
    ForcedRoaming = 0
    DataStatistics = 0
    NetworkSessionRequired = 0

    def __init__(self, parent = None):
        '''void QNetworkConfigurationManager.__init__(QObject parent = None)'''
    updateCompleted = pyqtSignal() # void updateCompleted() - signal
    onlineStateChanged = pyqtSignal() # void onlineStateChanged(bool) - signal
    configurationChanged = pyqtSignal() # void configurationChanged(const QNetworkConfigurationamp;) - signal
    configurationRemoved = pyqtSignal() # void configurationRemoved(const QNetworkConfigurationamp;) - signal
    configurationAdded = pyqtSignal() # void configurationAdded(const QNetworkConfigurationamp;) - signal
    def isOnline(self):
        '''bool QNetworkConfigurationManager.isOnline()'''
        return bool()
    def updateConfigurations(self):
        '''void QNetworkConfigurationManager.updateConfigurations()'''
    def configurationFromIdentifier(self, identifier):
        '''QNetworkConfiguration QNetworkConfigurationManager.configurationFromIdentifier(QString identifier)'''
        return QNetworkConfiguration()
    def allConfigurations(self, flags = 0):
        '''list-of-QNetworkConfiguration QNetworkConfigurationManager.allConfigurations(QNetworkConfiguration.StateFlags flags = 0)'''
        return [QNetworkConfiguration()]
    def defaultConfiguration(self):
        '''QNetworkConfiguration QNetworkConfigurationManager.defaultConfiguration()'''
        return QNetworkConfiguration()
    def capabilities(self):
        '''QNetworkConfigurationManager.Capabilities QNetworkConfigurationManager.capabilities()'''
        return QNetworkConfigurationManager.Capabilities()
    class Capabilities():
        """"""
        def __init__(self):
            '''QNetworkConfigurationManager.Capabilities QNetworkConfigurationManager.Capabilities.__init__()'''
            return QNetworkConfigurationManager.Capabilities()
        def __init__(self):
            '''int QNetworkConfigurationManager.Capabilities.__init__()'''
            return int()
        def __init__(self):
            '''void QNetworkConfigurationManager.Capabilities.__init__()'''
        def __bool__(self):
            '''int QNetworkConfigurationManager.Capabilities.__bool__()'''
            return int()
        def __ne__(self, f):
            '''bool QNetworkConfigurationManager.Capabilities.__ne__(QNetworkConfigurationManager.Capabilities f)'''
            return bool()
        def __eq__(self, f):
            '''bool QNetworkConfigurationManager.Capabilities.__eq__(QNetworkConfigurationManager.Capabilities f)'''
            return bool()
        def __invert__(self):
            '''QNetworkConfigurationManager.Capabilities QNetworkConfigurationManager.Capabilities.__invert__()'''
            return QNetworkConfigurationManager.Capabilities()
        def __and__(self, mask):
            '''QNetworkConfigurationManager.Capabilities QNetworkConfigurationManager.Capabilities.__and__(int mask)'''
            return QNetworkConfigurationManager.Capabilities()
        def __xor__(self, f):
            '''QNetworkConfigurationManager.Capabilities QNetworkConfigurationManager.Capabilities.__xor__(QNetworkConfigurationManager.Capabilities f)'''
            return QNetworkConfigurationManager.Capabilities()
        def __xor__(self, f):
            '''QNetworkConfigurationManager.Capabilities QNetworkConfigurationManager.Capabilities.__xor__(int f)'''
            return QNetworkConfigurationManager.Capabilities()
        def __or__(self, f):
            '''QNetworkConfigurationManager.Capabilities QNetworkConfigurationManager.Capabilities.__or__(QNetworkConfigurationManager.Capabilities f)'''
            return QNetworkConfigurationManager.Capabilities()
        def __or__(self, f):
            '''QNetworkConfigurationManager.Capabilities QNetworkConfigurationManager.Capabilities.__or__(int f)'''
            return QNetworkConfigurationManager.Capabilities()
        def __int__(self):
            '''int QNetworkConfigurationManager.Capabilities.__int__()'''
            return int()
        def __ixor__(self, f):
            '''QNetworkConfigurationManager.Capabilities QNetworkConfigurationManager.Capabilities.__ixor__(QNetworkConfigurationManager.Capabilities f)'''
            return QNetworkConfigurationManager.Capabilities()
        def __ior__(self, f):
            '''QNetworkConfigurationManager.Capabilities QNetworkConfigurationManager.Capabilities.__ior__(QNetworkConfigurationManager.Capabilities f)'''
            return QNetworkConfigurationManager.Capabilities()
        def __iand__(self, mask):
            '''QNetworkConfigurationManager.Capabilities QNetworkConfigurationManager.Capabilities.__iand__(int mask)'''
            return QNetworkConfigurationManager.Capabilities()


class QNetworkConfiguration():
    """"""
    # Enum QNetworkConfiguration.BearerType
    BearerUnknown = 0
    BearerEthernet = 0
    BearerWLAN = 0
    Bearer2G = 0
    BearerCDMA2000 = 0
    BearerWCDMA = 0
    BearerHSPA = 0
    BearerBluetooth = 0
    BearerWiMAX = 0

    # Enum QNetworkConfiguration.StateFlag
    Undefined = 0
    Defined = 0
    Discovered = 0
    Active = 0

    # Enum QNetworkConfiguration.Purpose
    UnknownPurpose = 0
    PublicPurpose = 0
    PrivatePurpose = 0
    ServiceSpecificPurpose = 0

    # Enum QNetworkConfiguration.Type
    InternetAccessPoint = 0
    ServiceNetwork = 0
    UserChoice = 0
    Invalid = 0

    def __init__(self):
        '''void QNetworkConfiguration.__init__()'''
    def __init__(self, other):
        '''void QNetworkConfiguration.__init__(QNetworkConfiguration other)'''
    def isValid(self):
        '''bool QNetworkConfiguration.isValid()'''
        return bool()
    def name(self):
        '''QString QNetworkConfiguration.name()'''
        return QString()
    def children(self):
        '''list-of-QNetworkConfiguration QNetworkConfiguration.children()'''
        return [QNetworkConfiguration()]
    def isRoamingAvailable(self):
        '''bool QNetworkConfiguration.isRoamingAvailable()'''
        return bool()
    def identifier(self):
        '''QString QNetworkConfiguration.identifier()'''
        return QString()
    def bearerTypeName(self):
        '''QString QNetworkConfiguration.bearerTypeName()'''
        return QString()
    def bearerType(self):
        '''QNetworkConfiguration.BearerType QNetworkConfiguration.bearerType()'''
        return QNetworkConfiguration.BearerType()
    def bearerName(self):
        '''QString QNetworkConfiguration.bearerName()'''
        return QString()
    def purpose(self):
        '''QNetworkConfiguration.Purpose QNetworkConfiguration.purpose()'''
        return QNetworkConfiguration.Purpose()
    def type(self):
        '''QNetworkConfiguration.Type QNetworkConfiguration.type()'''
        return QNetworkConfiguration.Type()
    def state(self):
        '''QNetworkConfiguration.StateFlags QNetworkConfiguration.state()'''
        return QNetworkConfiguration.StateFlags()
    def __ne__(self, cp):
        '''bool QNetworkConfiguration.__ne__(QNetworkConfiguration cp)'''
        return bool()
    def __eq__(self, cp):
        '''bool QNetworkConfiguration.__eq__(QNetworkConfiguration cp)'''
        return bool()
    class StateFlags():
        """"""
        def __init__(self):
            '''QNetworkConfiguration.StateFlags QNetworkConfiguration.StateFlags.__init__()'''
            return QNetworkConfiguration.StateFlags()
        def __init__(self):
            '''int QNetworkConfiguration.StateFlags.__init__()'''
            return int()
        def __init__(self):
            '''void QNetworkConfiguration.StateFlags.__init__()'''
        def __bool__(self):
            '''int QNetworkConfiguration.StateFlags.__bool__()'''
            return int()
        def __ne__(self, f):
            '''bool QNetworkConfiguration.StateFlags.__ne__(QNetworkConfiguration.StateFlags f)'''
            return bool()
        def __eq__(self, f):
            '''bool QNetworkConfiguration.StateFlags.__eq__(QNetworkConfiguration.StateFlags f)'''
            return bool()
        def __invert__(self):
            '''QNetworkConfiguration.StateFlags QNetworkConfiguration.StateFlags.__invert__()'''
            return QNetworkConfiguration.StateFlags()
        def __and__(self, mask):
            '''QNetworkConfiguration.StateFlags QNetworkConfiguration.StateFlags.__and__(int mask)'''
            return QNetworkConfiguration.StateFlags()
        def __xor__(self, f):
            '''QNetworkConfiguration.StateFlags QNetworkConfiguration.StateFlags.__xor__(QNetworkConfiguration.StateFlags f)'''
            return QNetworkConfiguration.StateFlags()
        def __xor__(self, f):
            '''QNetworkConfiguration.StateFlags QNetworkConfiguration.StateFlags.__xor__(int f)'''
            return QNetworkConfiguration.StateFlags()
        def __or__(self, f):
            '''QNetworkConfiguration.StateFlags QNetworkConfiguration.StateFlags.__or__(QNetworkConfiguration.StateFlags f)'''
            return QNetworkConfiguration.StateFlags()
        def __or__(self, f):
            '''QNetworkConfiguration.StateFlags QNetworkConfiguration.StateFlags.__or__(int f)'''
            return QNetworkConfiguration.StateFlags()
        def __int__(self):
            '''int QNetworkConfiguration.StateFlags.__int__()'''
            return int()
        def __ixor__(self, f):
            '''QNetworkConfiguration.StateFlags QNetworkConfiguration.StateFlags.__ixor__(QNetworkConfiguration.StateFlags f)'''
            return QNetworkConfiguration.StateFlags()
        def __ior__(self, f):
            '''QNetworkConfiguration.StateFlags QNetworkConfiguration.StateFlags.__ior__(QNetworkConfiguration.StateFlags f)'''
            return QNetworkConfiguration.StateFlags()
        def __iand__(self, mask):
            '''QNetworkConfiguration.StateFlags QNetworkConfiguration.StateFlags.__iand__(int mask)'''
            return QNetworkConfiguration.StateFlags()


class QNetworkCookie():
    """"""
    # Enum QNetworkCookie.RawForm
    NameAndValueOnly = 0
    Full = 0

    def __init__(self, name = QByteArray(), value = QByteArray()):
        '''void QNetworkCookie.__init__(QByteArray name = QByteArray(), QByteArray value = QByteArray())'''
    def __init__(self, other):
        '''void QNetworkCookie.__init__(QNetworkCookie other)'''
    def setHttpOnly(self, enable):
        '''void QNetworkCookie.setHttpOnly(bool enable)'''
    def isHttpOnly(self):
        '''bool QNetworkCookie.isHttpOnly()'''
        return bool()
    def __ne__(self, other):
        '''bool QNetworkCookie.__ne__(QNetworkCookie other)'''
        return bool()
    def __eq__(self, other):
        '''bool QNetworkCookie.__eq__(QNetworkCookie other)'''
        return bool()
    def parseCookies(self, cookieString):
        '''static list-of-QNetworkCookie QNetworkCookie.parseCookies(QByteArray cookieString)'''
        return [QNetworkCookie()]
    def toRawForm(self, form = None):
        '''QByteArray QNetworkCookie.toRawForm(QNetworkCookie.RawForm form = QNetworkCookie.Full)'''
        return QByteArray()
    def setValue(self, value):
        '''void QNetworkCookie.setValue(QByteArray value)'''
    def value(self):
        '''QByteArray QNetworkCookie.value()'''
        return QByteArray()
    def setName(self, cookieName):
        '''void QNetworkCookie.setName(QByteArray cookieName)'''
    def name(self):
        '''QByteArray QNetworkCookie.name()'''
        return QByteArray()
    def setPath(self, path):
        '''void QNetworkCookie.setPath(QString path)'''
    def path(self):
        '''QString QNetworkCookie.path()'''
        return QString()
    def setDomain(self, domain):
        '''void QNetworkCookie.setDomain(QString domain)'''
    def domain(self):
        '''QString QNetworkCookie.domain()'''
        return QString()
    def setExpirationDate(self, date):
        '''void QNetworkCookie.setExpirationDate(QDateTime date)'''
    def expirationDate(self):
        '''QDateTime QNetworkCookie.expirationDate()'''
        return QDateTime()
    def isSessionCookie(self):
        '''bool QNetworkCookie.isSessionCookie()'''
        return bool()
    def setSecure(self, enable):
        '''void QNetworkCookie.setSecure(bool enable)'''
    def isSecure(self):
        '''bool QNetworkCookie.isSecure()'''
        return bool()


class QNetworkCookieJar(QObject):
    """"""
    def __init__(self, parent = None):
        '''void QNetworkCookieJar.__init__(QObject parent = None)'''
    def setAllCookies(self, cookieList):
        '''void QNetworkCookieJar.setAllCookies(list-of-QNetworkCookie cookieList)'''
    def allCookies(self):
        '''list-of-QNetworkCookie QNetworkCookieJar.allCookies()'''
        return [QNetworkCookie()]
    def setCookiesFromUrl(self, cookieList, url):
        '''bool QNetworkCookieJar.setCookiesFromUrl(list-of-QNetworkCookie cookieList, QUrl url)'''
        return bool()
    def cookiesForUrl(self, url):
        '''list-of-QNetworkCookie QNetworkCookieJar.cookiesForUrl(QUrl url)'''
        return [QNetworkCookie()]


class QNetworkDiskCache(QAbstractNetworkCache):
    """"""
    def __init__(self, parent = None):
        '''void QNetworkDiskCache.__init__(QObject parent = None)'''
    def expire(self):
        '''int QNetworkDiskCache.expire()'''
        return int()
    def clear(self):
        '''void QNetworkDiskCache.clear()'''
    def fileMetaData(self, fileName):
        '''QNetworkCacheMetaData QNetworkDiskCache.fileMetaData(QString fileName)'''
        return QNetworkCacheMetaData()
    def insert(self, device):
        '''void QNetworkDiskCache.insert(QIODevice device)'''
    def prepare(self, metaData):
        '''QIODevice QNetworkDiskCache.prepare(QNetworkCacheMetaData metaData)'''
        return QIODevice()
    def remove(self, url):
        '''bool QNetworkDiskCache.remove(QUrl url)'''
        return bool()
    def data(self, url):
        '''QIODevice QNetworkDiskCache.data(QUrl url)'''
        return QIODevice()
    def updateMetaData(self, metaData):
        '''void QNetworkDiskCache.updateMetaData(QNetworkCacheMetaData metaData)'''
    def metaData(self, url):
        '''QNetworkCacheMetaData QNetworkDiskCache.metaData(QUrl url)'''
        return QNetworkCacheMetaData()
    def cacheSize(self):
        '''int QNetworkDiskCache.cacheSize()'''
        return int()
    def setMaximumCacheSize(self, size):
        '''void QNetworkDiskCache.setMaximumCacheSize(int size)'''
    def maximumCacheSize(self):
        '''int QNetworkDiskCache.maximumCacheSize()'''
        return int()
    def setCacheDirectory(self, cacheDir):
        '''void QNetworkDiskCache.setCacheDirectory(QString cacheDir)'''
    def cacheDirectory(self):
        '''QString QNetworkDiskCache.cacheDirectory()'''
        return QString()


class QNetworkAddressEntry():
    """"""
    def __init__(self):
        '''void QNetworkAddressEntry.__init__()'''
    def __init__(self, other):
        '''void QNetworkAddressEntry.__init__(QNetworkAddressEntry other)'''
    def setPrefixLength(self, length):
        '''void QNetworkAddressEntry.setPrefixLength(int length)'''
    def prefixLength(self):
        '''int QNetworkAddressEntry.prefixLength()'''
        return int()
    def __ne__(self, other):
        '''bool QNetworkAddressEntry.__ne__(QNetworkAddressEntry other)'''
        return bool()
    def __eq__(self, other):
        '''bool QNetworkAddressEntry.__eq__(QNetworkAddressEntry other)'''
        return bool()
    def setBroadcast(self, newBroadcast):
        '''void QNetworkAddressEntry.setBroadcast(QHostAddress newBroadcast)'''
    def broadcast(self):
        '''QHostAddress QNetworkAddressEntry.broadcast()'''
        return QHostAddress()
    def setNetmask(self, newNetmask):
        '''void QNetworkAddressEntry.setNetmask(QHostAddress newNetmask)'''
    def netmask(self):
        '''QHostAddress QNetworkAddressEntry.netmask()'''
        return QHostAddress()
    def setIp(self, newIp):
        '''void QNetworkAddressEntry.setIp(QHostAddress newIp)'''
    def ip(self):
        '''QHostAddress QNetworkAddressEntry.ip()'''
        return QHostAddress()


class QNetworkInterface():
    """"""
    # Enum QNetworkInterface.InterfaceFlag
    IsUp = 0
    IsRunning = 0
    CanBroadcast = 0
    IsLoopBack = 0
    IsPointToPoint = 0
    CanMulticast = 0

    def __init__(self):
        '''void QNetworkInterface.__init__()'''
    def __init__(self, other):
        '''void QNetworkInterface.__init__(QNetworkInterface other)'''
    def humanReadableName(self):
        '''QString QNetworkInterface.humanReadableName()'''
        return QString()
    def index(self):
        '''int QNetworkInterface.index()'''
        return int()
    def allAddresses(self):
        '''static list-of-QHostAddress QNetworkInterface.allAddresses()'''
        return [QHostAddress()]
    def allInterfaces(self):
        '''static list-of-QNetworkInterface QNetworkInterface.allInterfaces()'''
        return [QNetworkInterface()]
    def interfaceFromIndex(self, index):
        '''static QNetworkInterface QNetworkInterface.interfaceFromIndex(int index)'''
        return QNetworkInterface()
    def interfaceFromName(self, name):
        '''static QNetworkInterface QNetworkInterface.interfaceFromName(QString name)'''
        return QNetworkInterface()
    def addressEntries(self):
        '''list-of-QNetworkAddressEntry QNetworkInterface.addressEntries()'''
        return [QNetworkAddressEntry()]
    def hardwareAddress(self):
        '''QString QNetworkInterface.hardwareAddress()'''
        return QString()
    def flags(self):
        '''QNetworkInterface.InterfaceFlags QNetworkInterface.flags()'''
        return QNetworkInterface.InterfaceFlags()
    def name(self):
        '''QString QNetworkInterface.name()'''
        return QString()
    def isValid(self):
        '''bool QNetworkInterface.isValid()'''
        return bool()
    class InterfaceFlags():
        """"""
        def __init__(self):
            '''QNetworkInterface.InterfaceFlags QNetworkInterface.InterfaceFlags.__init__()'''
            return QNetworkInterface.InterfaceFlags()
        def __init__(self):
            '''int QNetworkInterface.InterfaceFlags.__init__()'''
            return int()
        def __init__(self):
            '''void QNetworkInterface.InterfaceFlags.__init__()'''
        def __bool__(self):
            '''int QNetworkInterface.InterfaceFlags.__bool__()'''
            return int()
        def __ne__(self, f):
            '''bool QNetworkInterface.InterfaceFlags.__ne__(QNetworkInterface.InterfaceFlags f)'''
            return bool()
        def __eq__(self, f):
            '''bool QNetworkInterface.InterfaceFlags.__eq__(QNetworkInterface.InterfaceFlags f)'''
            return bool()
        def __invert__(self):
            '''QNetworkInterface.InterfaceFlags QNetworkInterface.InterfaceFlags.__invert__()'''
            return QNetworkInterface.InterfaceFlags()
        def __and__(self, mask):
            '''QNetworkInterface.InterfaceFlags QNetworkInterface.InterfaceFlags.__and__(int mask)'''
            return QNetworkInterface.InterfaceFlags()
        def __xor__(self, f):
            '''QNetworkInterface.InterfaceFlags QNetworkInterface.InterfaceFlags.__xor__(QNetworkInterface.InterfaceFlags f)'''
            return QNetworkInterface.InterfaceFlags()
        def __xor__(self, f):
            '''QNetworkInterface.InterfaceFlags QNetworkInterface.InterfaceFlags.__xor__(int f)'''
            return QNetworkInterface.InterfaceFlags()
        def __or__(self, f):
            '''QNetworkInterface.InterfaceFlags QNetworkInterface.InterfaceFlags.__or__(QNetworkInterface.InterfaceFlags f)'''
            return QNetworkInterface.InterfaceFlags()
        def __or__(self, f):
            '''QNetworkInterface.InterfaceFlags QNetworkInterface.InterfaceFlags.__or__(int f)'''
            return QNetworkInterface.InterfaceFlags()
        def __int__(self):
            '''int QNetworkInterface.InterfaceFlags.__int__()'''
            return int()
        def __ixor__(self, f):
            '''QNetworkInterface.InterfaceFlags QNetworkInterface.InterfaceFlags.__ixor__(QNetworkInterface.InterfaceFlags f)'''
            return QNetworkInterface.InterfaceFlags()
        def __ior__(self, f):
            '''QNetworkInterface.InterfaceFlags QNetworkInterface.InterfaceFlags.__ior__(QNetworkInterface.InterfaceFlags f)'''
            return QNetworkInterface.InterfaceFlags()
        def __iand__(self, mask):
            '''QNetworkInterface.InterfaceFlags QNetworkInterface.InterfaceFlags.__iand__(int mask)'''
            return QNetworkInterface.InterfaceFlags()


class QNetworkProxy():
    """"""
    # Enum QNetworkProxy.Capability
    TunnelingCapability = 0
    ListeningCapability = 0
    UdpTunnelingCapability = 0
    CachingCapability = 0
    HostNameLookupCapability = 0

    # Enum QNetworkProxy.ProxyType
    DefaultProxy = 0
    Socks5Proxy = 0
    NoProxy = 0
    HttpProxy = 0
    HttpCachingProxy = 0
    FtpCachingProxy = 0

    def __init__(self):
        '''void QNetworkProxy.__init__()'''
    def __init__(self, type, hostName = QString(), port = 0, user = QString(), password = QString()):
        '''void QNetworkProxy.__init__(QNetworkProxy.ProxyType type, QString hostName = QString(), int port = 0, QString user = QString(), QString password = QString())'''
    def __init__(self, other):
        '''void QNetworkProxy.__init__(QNetworkProxy other)'''
    def capabilities(self):
        '''QNetworkProxy.Capabilities QNetworkProxy.capabilities()'''
        return QNetworkProxy.Capabilities()
    def setCapabilities(self, capab):
        '''void QNetworkProxy.setCapabilities(QNetworkProxy.Capabilities capab)'''
    def __ne__(self, other):
        '''bool QNetworkProxy.__ne__(QNetworkProxy other)'''
        return bool()
    def __eq__(self, other):
        '''bool QNetworkProxy.__eq__(QNetworkProxy other)'''
        return bool()
    def isTransparentProxy(self):
        '''bool QNetworkProxy.isTransparentProxy()'''
        return bool()
    def isCachingProxy(self):
        '''bool QNetworkProxy.isCachingProxy()'''
        return bool()
    def applicationProxy(self):
        '''static QNetworkProxy QNetworkProxy.applicationProxy()'''
        return QNetworkProxy()
    def setApplicationProxy(self, proxy):
        '''static void QNetworkProxy.setApplicationProxy(QNetworkProxy proxy)'''
    def port(self):
        '''int QNetworkProxy.port()'''
        return int()
    def setPort(self, port):
        '''void QNetworkProxy.setPort(int port)'''
    def hostName(self):
        '''QString QNetworkProxy.hostName()'''
        return QString()
    def setHostName(self, hostName):
        '''void QNetworkProxy.setHostName(QString hostName)'''
    def password(self):
        '''QString QNetworkProxy.password()'''
        return QString()
    def setPassword(self, password):
        '''void QNetworkProxy.setPassword(QString password)'''
    def user(self):
        '''QString QNetworkProxy.user()'''
        return QString()
    def setUser(self, userName):
        '''void QNetworkProxy.setUser(QString userName)'''
    def type(self):
        '''QNetworkProxy.ProxyType QNetworkProxy.type()'''
        return QNetworkProxy.ProxyType()
    def setType(self, type):
        '''void QNetworkProxy.setType(QNetworkProxy.ProxyType type)'''
    class Capabilities():
        """"""
        def __init__(self):
            '''QNetworkProxy.Capabilities QNetworkProxy.Capabilities.__init__()'''
            return QNetworkProxy.Capabilities()
        def __init__(self):
            '''int QNetworkProxy.Capabilities.__init__()'''
            return int()
        def __init__(self):
            '''void QNetworkProxy.Capabilities.__init__()'''
        def __bool__(self):
            '''int QNetworkProxy.Capabilities.__bool__()'''
            return int()
        def __ne__(self, f):
            '''bool QNetworkProxy.Capabilities.__ne__(QNetworkProxy.Capabilities f)'''
            return bool()
        def __eq__(self, f):
            '''bool QNetworkProxy.Capabilities.__eq__(QNetworkProxy.Capabilities f)'''
            return bool()
        def __invert__(self):
            '''QNetworkProxy.Capabilities QNetworkProxy.Capabilities.__invert__()'''
            return QNetworkProxy.Capabilities()
        def __and__(self, mask):
            '''QNetworkProxy.Capabilities QNetworkProxy.Capabilities.__and__(int mask)'''
            return QNetworkProxy.Capabilities()
        def __xor__(self, f):
            '''QNetworkProxy.Capabilities QNetworkProxy.Capabilities.__xor__(QNetworkProxy.Capabilities f)'''
            return QNetworkProxy.Capabilities()
        def __xor__(self, f):
            '''QNetworkProxy.Capabilities QNetworkProxy.Capabilities.__xor__(int f)'''
            return QNetworkProxy.Capabilities()
        def __or__(self, f):
            '''QNetworkProxy.Capabilities QNetworkProxy.Capabilities.__or__(QNetworkProxy.Capabilities f)'''
            return QNetworkProxy.Capabilities()
        def __or__(self, f):
            '''QNetworkProxy.Capabilities QNetworkProxy.Capabilities.__or__(int f)'''
            return QNetworkProxy.Capabilities()
        def __int__(self):
            '''int QNetworkProxy.Capabilities.__int__()'''
            return int()
        def __ixor__(self, f):
            '''QNetworkProxy.Capabilities QNetworkProxy.Capabilities.__ixor__(QNetworkProxy.Capabilities f)'''
            return QNetworkProxy.Capabilities()
        def __ior__(self, f):
            '''QNetworkProxy.Capabilities QNetworkProxy.Capabilities.__ior__(QNetworkProxy.Capabilities f)'''
            return QNetworkProxy.Capabilities()
        def __iand__(self, mask):
            '''QNetworkProxy.Capabilities QNetworkProxy.Capabilities.__iand__(int mask)'''
            return QNetworkProxy.Capabilities()


class QNetworkProxyQuery():
    """"""
    # Enum QNetworkProxyQuery.QueryType
    TcpSocket = 0
    UdpSocket = 0
    TcpServer = 0
    UrlRequest = 0

    def __init__(self):
        '''void QNetworkProxyQuery.__init__()'''
    def __init__(self, requestUrl, type = None):
        '''void QNetworkProxyQuery.__init__(QUrl requestUrl, QNetworkProxyQuery.QueryType type = QNetworkProxyQuery.UrlRequest)'''
    def __init__(self, hostname, port, protocolTag = QString(), type = None):
        '''void QNetworkProxyQuery.__init__(QString hostname, int port, QString protocolTag = QString(), QNetworkProxyQuery.QueryType type = QNetworkProxyQuery.TcpSocket)'''
    def __init__(self, bindPort, protocolTag = QString(), type = None):
        '''void QNetworkProxyQuery.__init__(int bindPort, QString protocolTag = QString(), QNetworkProxyQuery.QueryType type = QNetworkProxyQuery.TcpServer)'''
    def __init__(self, networkConfiguration, requestUrl, queryType = None):
        '''void QNetworkProxyQuery.__init__(QNetworkConfiguration networkConfiguration, QUrl requestUrl, QNetworkProxyQuery.QueryType queryType = QNetworkProxyQuery.UrlRequest)'''
    def __init__(self, networkConfiguration, hostname, port, protocolTag = QString(), type = None):
        '''void QNetworkProxyQuery.__init__(QNetworkConfiguration networkConfiguration, QString hostname, int port, QString protocolTag = QString(), QNetworkProxyQuery.QueryType type = QNetworkProxyQuery.TcpSocket)'''
    def __init__(self, networkConfiguration, bindPort, protocolTag = QString(), type = None):
        '''void QNetworkProxyQuery.__init__(QNetworkConfiguration networkConfiguration, int bindPort, QString protocolTag = QString(), QNetworkProxyQuery.QueryType type = QNetworkProxyQuery.TcpServer)'''
    def __init__(self, other):
        '''void QNetworkProxyQuery.__init__(QNetworkProxyQuery other)'''
    def setNetworkConfiguration(self, networkConfiguration):
        '''void QNetworkProxyQuery.setNetworkConfiguration(QNetworkConfiguration networkConfiguration)'''
    def networkConfiguration(self):
        '''QNetworkConfiguration QNetworkProxyQuery.networkConfiguration()'''
        return QNetworkConfiguration()
    def setUrl(self, url):
        '''void QNetworkProxyQuery.setUrl(QUrl url)'''
    def url(self):
        '''QUrl QNetworkProxyQuery.url()'''
        return QUrl()
    def setProtocolTag(self, protocolTag):
        '''void QNetworkProxyQuery.setProtocolTag(QString protocolTag)'''
    def protocolTag(self):
        '''QString QNetworkProxyQuery.protocolTag()'''
        return QString()
    def setLocalPort(self, port):
        '''void QNetworkProxyQuery.setLocalPort(int port)'''
    def localPort(self):
        '''int QNetworkProxyQuery.localPort()'''
        return int()
    def setPeerHostName(self, hostname):
        '''void QNetworkProxyQuery.setPeerHostName(QString hostname)'''
    def peerHostName(self):
        '''QString QNetworkProxyQuery.peerHostName()'''
        return QString()
    def setPeerPort(self, port):
        '''void QNetworkProxyQuery.setPeerPort(int port)'''
    def peerPort(self):
        '''int QNetworkProxyQuery.peerPort()'''
        return int()
    def setQueryType(self, type):
        '''void QNetworkProxyQuery.setQueryType(QNetworkProxyQuery.QueryType type)'''
    def queryType(self):
        '''QNetworkProxyQuery.QueryType QNetworkProxyQuery.queryType()'''
        return QNetworkProxyQuery.QueryType()
    def __ne__(self, other):
        '''bool QNetworkProxyQuery.__ne__(QNetworkProxyQuery other)'''
        return bool()
    def __eq__(self, other):
        '''bool QNetworkProxyQuery.__eq__(QNetworkProxyQuery other)'''
        return bool()


class QNetworkProxyFactory():
    """"""
    def __init__(self):
        '''void QNetworkProxyFactory.__init__()'''
    def __init__(self):
        '''QNetworkProxyFactory QNetworkProxyFactory.__init__()'''
        return QNetworkProxyFactory()
    def setUseSystemConfiguration(self, enable):
        '''static void QNetworkProxyFactory.setUseSystemConfiguration(bool enable)'''
    def systemProxyForQuery(self, query = QNetworkProxyQuery()):
        '''static list-of-QNetworkProxy QNetworkProxyFactory.systemProxyForQuery(QNetworkProxyQuery query = QNetworkProxyQuery())'''
        return [QNetworkProxy()]
    def proxyForQuery(self, query):
        '''static list-of-QNetworkProxy QNetworkProxyFactory.proxyForQuery(QNetworkProxyQuery query)'''
        return [QNetworkProxy()]
    def setApplicationProxyFactory(self, factory):
        '''static void QNetworkProxyFactory.setApplicationProxyFactory(QNetworkProxyFactory factory)'''
    def queryProxy(self, query = QNetworkProxyQuery()):
        '''abstract list-of-QNetworkProxy QNetworkProxyFactory.queryProxy(QNetworkProxyQuery query = QNetworkProxyQuery())'''
        return [QNetworkProxy()]


class QNetworkReply(QIODevice):
    """"""
    # Enum QNetworkReply.NetworkError
    NoError = 0
    ConnectionRefusedError = 0
    RemoteHostClosedError = 0
    HostNotFoundError = 0
    TimeoutError = 0
    OperationCanceledError = 0
    SslHandshakeFailedError = 0
    UnknownNetworkError = 0
    ProxyConnectionRefusedError = 0
    ProxyConnectionClosedError = 0
    ProxyNotFoundError = 0
    ProxyTimeoutError = 0
    ProxyAuthenticationRequiredError = 0
    UnknownProxyError = 0
    ContentAccessDenied = 0
    ContentOperationNotPermittedError = 0
    ContentNotFoundError = 0
    AuthenticationRequiredError = 0
    UnknownContentError = 0
    ProtocolUnknownError = 0
    ProtocolInvalidOperationError = 0
    ProtocolFailure = 0
    ContentReSendError = 0
    TemporaryNetworkFailureError = 0

    def __init__(self, parent = None):
        '''void QNetworkReply.__init__(QObject parent = None)'''
    def rawHeaderPairs(self):
        '''list-of-tuple-of-QByteArray-QByteArray QNetworkReply.rawHeaderPairs()'''
        return [tuple-of-QByteArray-QByteArray()]
    def isRunning(self):
        '''bool QNetworkReply.isRunning()'''
        return bool()
    def isFinished(self):
        '''bool QNetworkReply.isFinished()'''
        return bool()
    def setFinished(self, finished):
        '''void QNetworkReply.setFinished(bool finished)'''
    def setAttribute(self, code, value):
        '''void QNetworkReply.setAttribute(QNetworkRequest.Attribute code, QVariant value)'''
    def setRawHeader(self, headerName, value):
        '''void QNetworkReply.setRawHeader(QByteArray headerName, QByteArray value)'''
    def setHeader(self, header, value):
        '''void QNetworkReply.setHeader(QNetworkRequest.KnownHeaders header, QVariant value)'''
    def setUrl(self, url):
        '''void QNetworkReply.setUrl(QUrl url)'''
    def setError(self, errorCode, errorString):
        '''void QNetworkReply.setError(QNetworkReply.NetworkError errorCode, QString errorString)'''
    def setRequest(self, request):
        '''void QNetworkReply.setRequest(QNetworkRequest request)'''
    def setOperation(self, operation):
        '''void QNetworkReply.setOperation(QNetworkAccessManager.Operation operation)'''
    def writeData(self, data):
        '''int QNetworkReply.writeData(str data)'''
        return int()
    downloadProgress = pyqtSignal() # void downloadProgress(qint64,qint64) - signal
    uploadProgress = pyqtSignal() # void uploadProgress(qint64,qint64) - signal
    sslErrors = pyqtSignal() # void sslErrors(const QListlt;QSslErrorgt;amp;) - signal
    finished = pyqtSignal() # void finished() - signal
    metaDataChanged = pyqtSignal() # void metaDataChanged() - signal
    def ignoreSslErrors(self):
        '''void QNetworkReply.ignoreSslErrors()'''
    def ignoreSslErrors(self, errors):
        '''void QNetworkReply.ignoreSslErrors(list-of-QSslError errors)'''
    def setSslConfiguration(self, configuration):
        '''void QNetworkReply.setSslConfiguration(QSslConfiguration configuration)'''
    def sslConfiguration(self):
        '''QSslConfiguration QNetworkReply.sslConfiguration()'''
        return QSslConfiguration()
    def attribute(self, code):
        '''QVariant QNetworkReply.attribute(QNetworkRequest.Attribute code)'''
        return QVariant()
    def rawHeader(self, headerName):
        '''QByteArray QNetworkReply.rawHeader(QByteArray headerName)'''
        return QByteArray()
    def rawHeaderList(self):
        '''list-of-QByteArray QNetworkReply.rawHeaderList()'''
        return [QByteArray()]
    def hasRawHeader(self, headerName):
        '''bool QNetworkReply.hasRawHeader(QByteArray headerName)'''
        return bool()
    def header(self, header):
        '''QVariant QNetworkReply.header(QNetworkRequest.KnownHeaders header)'''
        return QVariant()
    def url(self):
        '''QUrl QNetworkReply.url()'''
        return QUrl()
    def error(self):
        '''QNetworkReply.NetworkError QNetworkReply.error()'''
        return QNetworkReply.NetworkError()
    error = pyqtSignal() # void error(QNetworkReply::NetworkError) - signal
    def request(self):
        '''QNetworkRequest QNetworkReply.request()'''
        return QNetworkRequest()
    def operation(self):
        '''QNetworkAccessManager.Operation QNetworkReply.operation()'''
        return QNetworkAccessManager.Operation()
    def manager(self):
        '''QNetworkAccessManager QNetworkReply.manager()'''
        return QNetworkAccessManager()
    def setReadBufferSize(self, size):
        '''void QNetworkReply.setReadBufferSize(int size)'''
    def readBufferSize(self):
        '''int QNetworkReply.readBufferSize()'''
        return int()
    def isSequential(self):
        '''bool QNetworkReply.isSequential()'''
        return bool()
    def close(self):
        '''void QNetworkReply.close()'''
    def abort(self):
        '''abstract void QNetworkReply.abort()'''


class QNetworkRequest():
    """"""
    # Enum QNetworkRequest.Priority
    HighPriority = 0
    NormalPriority = 0
    LowPriority = 0

    # Enum QNetworkRequest.LoadControl
    Automatic = 0
    Manual = 0

    # Enum QNetworkRequest.CacheLoadControl
    AlwaysNetwork = 0
    PreferNetwork = 0
    PreferCache = 0
    AlwaysCache = 0

    # Enum QNetworkRequest.Attribute
    HttpStatusCodeAttribute = 0
    HttpReasonPhraseAttribute = 0
    RedirectionTargetAttribute = 0
    ConnectionEncryptedAttribute = 0
    CacheLoadControlAttribute = 0
    CacheSaveControlAttribute = 0
    SourceIsFromCacheAttribute = 0
    DoNotBufferUploadDataAttribute = 0
    HttpPipeliningAllowedAttribute = 0
    HttpPipeliningWasUsedAttribute = 0
    CustomVerbAttribute = 0
    CookieLoadControlAttribute = 0
    AuthenticationReuseAttribute = 0
    CookieSaveControlAttribute = 0
    User = 0
    UserMax = 0

    # Enum QNetworkRequest.KnownHeaders
    ContentTypeHeader = 0
    ContentLengthHeader = 0
    LocationHeader = 0
    LastModifiedHeader = 0
    CookieHeader = 0
    SetCookieHeader = 0
    ContentDispositionHeader = 0

    def __init__(self, url = QUrl()):
        '''void QNetworkRequest.__init__(QUrl url = QUrl())'''
    def __init__(self, other):
        '''void QNetworkRequest.__init__(QNetworkRequest other)'''
    def setPriority(self, priority):
        '''void QNetworkRequest.setPriority(QNetworkRequest.Priority priority)'''
    def priority(self):
        '''QNetworkRequest.Priority QNetworkRequest.priority()'''
        return QNetworkRequest.Priority()
    def originatingObject(self):
        '''QObject QNetworkRequest.originatingObject()'''
        return QObject()
    def setOriginatingObject(self, object):
        '''void QNetworkRequest.setOriginatingObject(QObject object)'''
    def __ne__(self, other):
        '''bool QNetworkRequest.__ne__(QNetworkRequest other)'''
        return bool()
    def __eq__(self, other):
        '''bool QNetworkRequest.__eq__(QNetworkRequest other)'''
        return bool()
    def setSslConfiguration(self, configuration):
        '''void QNetworkRequest.setSslConfiguration(QSslConfiguration configuration)'''
    def sslConfiguration(self):
        '''QSslConfiguration QNetworkRequest.sslConfiguration()'''
        return QSslConfiguration()
    def setAttribute(self, code, value):
        '''void QNetworkRequest.setAttribute(QNetworkRequest.Attribute code, QVariant value)'''
    def attribute(self, code, defaultValue = QVariant()):
        '''QVariant QNetworkRequest.attribute(QNetworkRequest.Attribute code, QVariant defaultValue = QVariant())'''
        return QVariant()
    def setRawHeader(self, headerName, value):
        '''void QNetworkRequest.setRawHeader(QByteArray headerName, QByteArray value)'''
    def rawHeader(self, headerName):
        '''QByteArray QNetworkRequest.rawHeader(QByteArray headerName)'''
        return QByteArray()
    def rawHeaderList(self):
        '''list-of-QByteArray QNetworkRequest.rawHeaderList()'''
        return [QByteArray()]
    def hasRawHeader(self, headerName):
        '''bool QNetworkRequest.hasRawHeader(QByteArray headerName)'''
        return bool()
    def setHeader(self, header, value):
        '''void QNetworkRequest.setHeader(QNetworkRequest.KnownHeaders header, QVariant value)'''
    def header(self, header):
        '''QVariant QNetworkRequest.header(QNetworkRequest.KnownHeaders header)'''
        return QVariant()
    def setUrl(self, url):
        '''void QNetworkRequest.setUrl(QUrl url)'''
    def url(self):
        '''QUrl QNetworkRequest.url()'''
        return QUrl()


class QNetworkSession(QObject):
    """"""
    # Enum QNetworkSession.SessionError
    UnknownSessionError = 0
    SessionAbortedError = 0
    RoamingError = 0
    OperationNotSupportedError = 0
    InvalidConfigurationError = 0

    # Enum QNetworkSession.State
    Invalid = 0
    NotAvailable = 0
    Connecting = 0
    Connected = 0
    Closing = 0
    Disconnected = 0
    Roaming = 0

    def __init__(self, connConfig, parent = None):
        '''void QNetworkSession.__init__(QNetworkConfiguration connConfig, QObject parent = None)'''
    def disconnectNotify(self, signal):
        '''void QNetworkSession.disconnectNotify(SIGNAL() signal)'''
    def connectNotify(self, signal):
        '''void QNetworkSession.connectNotify(SIGNAL() signal)'''
    newConfigurationActivated = pyqtSignal() # void newConfigurationActivated() - signal
    preferredConfigurationChanged = pyqtSignal() # void preferredConfigurationChanged(const QNetworkConfigurationamp;,bool) - signal
    closed = pyqtSignal() # void closed() - signal
    opened = pyqtSignal() # void opened() - signal
    stateChanged = pyqtSignal() # void stateChanged(QNetworkSession::State) - signal
    def reject(self):
        '''void QNetworkSession.reject()'''
    def accept(self):
        '''void QNetworkSession.accept()'''
    def ignore(self):
        '''void QNetworkSession.ignore()'''
    def migrate(self):
        '''void QNetworkSession.migrate()'''
    def stop(self):
        '''void QNetworkSession.stop()'''
    def close(self):
        '''void QNetworkSession.close()'''
    def open(self):
        '''void QNetworkSession.open()'''
    def waitForOpened(self, msecs = 30000):
        '''bool QNetworkSession.waitForOpened(int msecs = 30000)'''
        return bool()
    def activeTime(self):
        '''int QNetworkSession.activeTime()'''
        return int()
    def bytesReceived(self):
        '''int QNetworkSession.bytesReceived()'''
        return int()
    def bytesWritten(self):
        '''int QNetworkSession.bytesWritten()'''
        return int()
    def setSessionProperty(self, key, value):
        '''void QNetworkSession.setSessionProperty(QString key, QVariant value)'''
    def sessionProperty(self, key):
        '''QVariant QNetworkSession.sessionProperty(QString key)'''
        return QVariant()
    def errorString(self):
        '''QString QNetworkSession.errorString()'''
        return QString()
    def error(self):
        '''QNetworkSession.SessionError QNetworkSession.error()'''
        return QNetworkSession.SessionError()
    error = pyqtSignal() # void error(QNetworkSession::SessionError) - signal
    def state(self):
        '''QNetworkSession.State QNetworkSession.state()'''
        return QNetworkSession.State()
    def interface(self):
        '''QNetworkInterface QNetworkSession.interface()'''
        return QNetworkInterface()
    def configuration(self):
        '''QNetworkConfiguration QNetworkSession.configuration()'''
        return QNetworkConfiguration()
    def isOpen(self):
        '''bool QNetworkSession.isOpen()'''
        return bool()


class QSsl():
    """"""
    # Enum QSsl.SslOption
    SslOptionDisableEmptyFragments = 0
    SslOptionDisableSessionTickets = 0
    SslOptionDisableCompression = 0
    SslOptionDisableServerNameIndication = 0
    SslOptionDisableLegacyRenegotiation = 0

    # Enum QSsl.SslProtocol
    UnknownProtocol = 0
    SslV3 = 0
    SslV2 = 0
    TlsV1 = 0
    AnyProtocol = 0
    TlsV1SslV3 = 0
    SecureProtocols = 0

    # Enum QSsl.AlternateNameEntryType
    EmailEntry = 0
    DnsEntry = 0

    # Enum QSsl.KeyAlgorithm
    Rsa = 0
    Dsa = 0

    # Enum QSsl.EncodingFormat
    Pem = 0
    Der = 0

    # Enum QSsl.KeyType
    PrivateKey = 0
    PublicKey = 0

    class SslOptions():
        """"""
        def __init__(self):
            '''QSsl.SslOptions QSsl.SslOptions.__init__()'''
            return QSsl.SslOptions()
        def __init__(self):
            '''int QSsl.SslOptions.__init__()'''
            return int()
        def __init__(self):
            '''void QSsl.SslOptions.__init__()'''
        def __bool__(self):
            '''int QSsl.SslOptions.__bool__()'''
            return int()
        def __ne__(self, f):
            '''bool QSsl.SslOptions.__ne__(QSsl.SslOptions f)'''
            return bool()
        def __eq__(self, f):
            '''bool QSsl.SslOptions.__eq__(QSsl.SslOptions f)'''
            return bool()
        def __invert__(self):
            '''QSsl.SslOptions QSsl.SslOptions.__invert__()'''
            return QSsl.SslOptions()
        def __and__(self, mask):
            '''QSsl.SslOptions QSsl.SslOptions.__and__(int mask)'''
            return QSsl.SslOptions()
        def __xor__(self, f):
            '''QSsl.SslOptions QSsl.SslOptions.__xor__(QSsl.SslOptions f)'''
            return QSsl.SslOptions()
        def __xor__(self, f):
            '''QSsl.SslOptions QSsl.SslOptions.__xor__(int f)'''
            return QSsl.SslOptions()
        def __or__(self, f):
            '''QSsl.SslOptions QSsl.SslOptions.__or__(QSsl.SslOptions f)'''
            return QSsl.SslOptions()
        def __or__(self, f):
            '''QSsl.SslOptions QSsl.SslOptions.__or__(int f)'''
            return QSsl.SslOptions()
        def __int__(self):
            '''int QSsl.SslOptions.__int__()'''
            return int()
        def __ixor__(self, f):
            '''QSsl.SslOptions QSsl.SslOptions.__ixor__(QSsl.SslOptions f)'''
            return QSsl.SslOptions()
        def __ior__(self, f):
            '''QSsl.SslOptions QSsl.SslOptions.__ior__(QSsl.SslOptions f)'''
            return QSsl.SslOptions()
        def __iand__(self, mask):
            '''QSsl.SslOptions QSsl.SslOptions.__iand__(int mask)'''
            return QSsl.SslOptions()


class QSslCertificate():
    """"""
    # Enum QSslCertificate.SubjectInfo
    Organization = 0
    CommonName = 0
    LocalityName = 0
    OrganizationalUnitName = 0
    CountryName = 0
    StateOrProvinceName = 0

    def __init__(self, device, format = None):
        '''void QSslCertificate.__init__(QIODevice device, QSsl.EncodingFormat format = QSsl.Pem)'''
    def __init__(self, data = QByteArray(), format = None):
        '''void QSslCertificate.__init__(QByteArray data = QByteArray(), QSsl.EncodingFormat format = QSsl.Pem)'''
    def __init__(self, other):
        '''void QSslCertificate.__init__(QSslCertificate other)'''
    def handle(self):
        '''int QSslCertificate.handle()'''
        return int()
    def fromData(self, data, format = None):
        '''static list-of-QSslCertificate QSslCertificate.fromData(QByteArray data, QSsl.EncodingFormat format = QSsl.Pem)'''
        return [QSslCertificate()]
    def fromDevice(self, device, format = None):
        '''static list-of-QSslCertificate QSslCertificate.fromDevice(QIODevice device, QSsl.EncodingFormat format = QSsl.Pem)'''
        return [QSslCertificate()]
    def fromPath(self, path, format = None, syntax = None):
        '''static list-of-QSslCertificate QSslCertificate.fromPath(QString path, QSsl.EncodingFormat format = QSsl.Pem, QRegExp.PatternSyntax syntax = QRegExp.FixedString)'''
        return [QSslCertificate()]
    def toDer(self):
        '''QByteArray QSslCertificate.toDer()'''
        return QByteArray()
    def toPem(self):
        '''QByteArray QSslCertificate.toPem()'''
        return QByteArray()
    def publicKey(self):
        '''QSslKey QSslCertificate.publicKey()'''
        return QSslKey()
    def expiryDate(self):
        '''QDateTime QSslCertificate.expiryDate()'''
        return QDateTime()
    def effectiveDate(self):
        '''QDateTime QSslCertificate.effectiveDate()'''
        return QDateTime()
    def alternateSubjectNames(self):
        '''dict-of-QSsl.AlternateNameEntryType-list-of-QString QSslCertificate.alternateSubjectNames()'''
        return dict-of-QSsl.AlternateNameEntryType-list-of-QString()
    def subjectInfo(self, info):
        '''QString QSslCertificate.subjectInfo(QSslCertificate.SubjectInfo info)'''
        return QString()
    def subjectInfo(self, tag):
        '''QString QSslCertificate.subjectInfo(QByteArray tag)'''
        return QString()
    def issuerInfo(self, info):
        '''QString QSslCertificate.issuerInfo(QSslCertificate.SubjectInfo info)'''
        return QString()
    def issuerInfo(self, tag):
        '''QString QSslCertificate.issuerInfo(QByteArray tag)'''
        return QString()
    def digest(self, algorithm = None):
        '''QByteArray QSslCertificate.digest(QCryptographicHash.Algorithm algorithm = QCryptographicHash.Md5)'''
        return QByteArray()
    def serialNumber(self):
        '''QByteArray QSslCertificate.serialNumber()'''
        return QByteArray()
    def version(self):
        '''QByteArray QSslCertificate.version()'''
        return QByteArray()
    def clear(self):
        '''void QSslCertificate.clear()'''
    def isValid(self):
        '''bool QSslCertificate.isValid()'''
        return bool()
    def isNull(self):
        '''bool QSslCertificate.isNull()'''
        return bool()
    def __ne__(self, other):
        '''bool QSslCertificate.__ne__(QSslCertificate other)'''
        return bool()
    def __eq__(self, other):
        '''bool QSslCertificate.__eq__(QSslCertificate other)'''
        return bool()


class QSslConfiguration():
    """"""
    def __init__(self):
        '''void QSslConfiguration.__init__()'''
    def __init__(self, other):
        '''void QSslConfiguration.__init__(QSslConfiguration other)'''
    def testSslOption(self, option):
        '''bool QSslConfiguration.testSslOption(QSsl.SslOption option)'''
        return bool()
    def setSslOption(self, option, on):
        '''void QSslConfiguration.setSslOption(QSsl.SslOption option, bool on)'''
    def __ne__(self, other):
        '''bool QSslConfiguration.__ne__(QSslConfiguration other)'''
        return bool()
    def __eq__(self, other):
        '''bool QSslConfiguration.__eq__(QSslConfiguration other)'''
        return bool()
    def setDefaultConfiguration(self, configuration):
        '''static void QSslConfiguration.setDefaultConfiguration(QSslConfiguration configuration)'''
    def defaultConfiguration(self):
        '''static QSslConfiguration QSslConfiguration.defaultConfiguration()'''
        return QSslConfiguration()
    def setCaCertificates(self, certificates):
        '''void QSslConfiguration.setCaCertificates(list-of-QSslCertificate certificates)'''
    def caCertificates(self):
        '''list-of-QSslCertificate QSslConfiguration.caCertificates()'''
        return [QSslCertificate()]
    def setCiphers(self, ciphers):
        '''void QSslConfiguration.setCiphers(list-of-QSslCipher ciphers)'''
    def ciphers(self):
        '''list-of-QSslCipher QSslConfiguration.ciphers()'''
        return [QSslCipher()]
    def setPrivateKey(self, key):
        '''void QSslConfiguration.setPrivateKey(QSslKey key)'''
    def privateKey(self):
        '''QSslKey QSslConfiguration.privateKey()'''
        return QSslKey()
    def sessionCipher(self):
        '''QSslCipher QSslConfiguration.sessionCipher()'''
        return QSslCipher()
    def peerCertificateChain(self):
        '''list-of-QSslCertificate QSslConfiguration.peerCertificateChain()'''
        return [QSslCertificate()]
    def peerCertificate(self):
        '''QSslCertificate QSslConfiguration.peerCertificate()'''
        return QSslCertificate()
    def setLocalCertificate(self, certificate):
        '''void QSslConfiguration.setLocalCertificate(QSslCertificate certificate)'''
    def localCertificate(self):
        '''QSslCertificate QSslConfiguration.localCertificate()'''
        return QSslCertificate()
    def setPeerVerifyDepth(self, depth):
        '''void QSslConfiguration.setPeerVerifyDepth(int depth)'''
    def peerVerifyDepth(self):
        '''int QSslConfiguration.peerVerifyDepth()'''
        return int()
    def setPeerVerifyMode(self, mode):
        '''void QSslConfiguration.setPeerVerifyMode(QSslSocket.PeerVerifyMode mode)'''
    def peerVerifyMode(self):
        '''QSslSocket.PeerVerifyMode QSslConfiguration.peerVerifyMode()'''
        return QSslSocket.PeerVerifyMode()
    def setProtocol(self, protocol):
        '''void QSslConfiguration.setProtocol(QSsl.SslProtocol protocol)'''
    def protocol(self):
        '''QSsl.SslProtocol QSslConfiguration.protocol()'''
        return QSsl.SslProtocol()
    def isNull(self):
        '''bool QSslConfiguration.isNull()'''
        return bool()


class QSslCipher():
    """"""
    def __init__(self):
        '''void QSslCipher.__init__()'''
    def __init__(self, name, protocol):
        '''void QSslCipher.__init__(QString name, QSsl.SslProtocol protocol)'''
    def __init__(self, other):
        '''void QSslCipher.__init__(QSslCipher other)'''
    def protocol(self):
        '''QSsl.SslProtocol QSslCipher.protocol()'''
        return QSsl.SslProtocol()
    def protocolString(self):
        '''QString QSslCipher.protocolString()'''
        return QString()
    def encryptionMethod(self):
        '''QString QSslCipher.encryptionMethod()'''
        return QString()
    def authenticationMethod(self):
        '''QString QSslCipher.authenticationMethod()'''
        return QString()
    def keyExchangeMethod(self):
        '''QString QSslCipher.keyExchangeMethod()'''
        return QString()
    def usedBits(self):
        '''int QSslCipher.usedBits()'''
        return int()
    def supportedBits(self):
        '''int QSslCipher.supportedBits()'''
        return int()
    def name(self):
        '''QString QSslCipher.name()'''
        return QString()
    def isNull(self):
        '''bool QSslCipher.isNull()'''
        return bool()
    def __ne__(self, other):
        '''bool QSslCipher.__ne__(QSslCipher other)'''
        return bool()
    def __eq__(self, other):
        '''bool QSslCipher.__eq__(QSslCipher other)'''
        return bool()


class QSslError():
    """"""
    # Enum QSslError.SslError
    UnspecifiedError = 0
    NoError = 0
    UnableToGetIssuerCertificate = 0
    UnableToDecryptCertificateSignature = 0
    UnableToDecodeIssuerPublicKey = 0
    CertificateSignatureFailed = 0
    CertificateNotYetValid = 0
    CertificateExpired = 0
    InvalidNotBeforeField = 0
    InvalidNotAfterField = 0
    SelfSignedCertificate = 0
    SelfSignedCertificateInChain = 0
    UnableToGetLocalIssuerCertificate = 0
    UnableToVerifyFirstCertificate = 0
    CertificateRevoked = 0
    InvalidCaCertificate = 0
    PathLengthExceeded = 0
    InvalidPurpose = 0
    CertificateUntrusted = 0
    CertificateRejected = 0
    SubjectIssuerMismatch = 0
    AuthorityIssuerSerialNumberMismatch = 0
    NoPeerCertificate = 0
    HostNameMismatch = 0
    NoSslSupport = 0
    CertificateBlacklisted = 0

    def __init__(self):
        '''void QSslError.__init__()'''
    def __init__(self, error):
        '''void QSslError.__init__(QSslError.SslError error)'''
    def __init__(self, error, certificate):
        '''void QSslError.__init__(QSslError.SslError error, QSslCertificate certificate)'''
    def __init__(self, other):
        '''void QSslError.__init__(QSslError other)'''
    def __ne__(self, other):
        '''bool QSslError.__ne__(QSslError other)'''
        return bool()
    def __eq__(self, other):
        '''bool QSslError.__eq__(QSslError other)'''
        return bool()
    def certificate(self):
        '''QSslCertificate QSslError.certificate()'''
        return QSslCertificate()
    def errorString(self):
        '''QString QSslError.errorString()'''
        return QString()
    def error(self):
        '''QSslError.SslError QSslError.error()'''
        return QSslError.SslError()


class QSslKey():
    """"""
    def __init__(self):
        '''void QSslKey.__init__()'''
    def __init__(self, encoded, algorithm, encoding = None, type = None, passPhrase = QByteArray()):
        '''void QSslKey.__init__(QByteArray encoded, QSsl.KeyAlgorithm algorithm, QSsl.EncodingFormat encoding = QSsl.Pem, QSsl.KeyType type = QSsl.PrivateKey, QByteArray passPhrase = QByteArray())'''
    def __init__(self, device, algorithm, encoding = None, type = None, passPhrase = QByteArray()):
        '''void QSslKey.__init__(QIODevice device, QSsl.KeyAlgorithm algorithm, QSsl.EncodingFormat encoding = QSsl.Pem, QSsl.KeyType type = QSsl.PrivateKey, QByteArray passPhrase = QByteArray())'''
    def __init__(self, other):
        '''void QSslKey.__init__(QSslKey other)'''
    def __ne__(self, key):
        '''bool QSslKey.__ne__(QSslKey key)'''
        return bool()
    def __eq__(self, key):
        '''bool QSslKey.__eq__(QSslKey key)'''
        return bool()
    def handle(self):
        '''int QSslKey.handle()'''
        return int()
    def toDer(self, passPhrase = QByteArray()):
        '''QByteArray QSslKey.toDer(QByteArray passPhrase = QByteArray())'''
        return QByteArray()
    def toPem(self, passPhrase = QByteArray()):
        '''QByteArray QSslKey.toPem(QByteArray passPhrase = QByteArray())'''
        return QByteArray()
    def algorithm(self):
        '''QSsl.KeyAlgorithm QSslKey.algorithm()'''
        return QSsl.KeyAlgorithm()
    def type(self):
        '''QSsl.KeyType QSslKey.type()'''
        return QSsl.KeyType()
    def length(self):
        '''int QSslKey.length()'''
        return int()
    def clear(self):
        '''void QSslKey.clear()'''
    def isNull(self):
        '''bool QSslKey.isNull()'''
        return bool()


class QTcpSocket(QAbstractSocket):
    """"""
    def __init__(self, parent = None):
        '''void QTcpSocket.__init__(QObject parent = None)'''


class QSslSocket(QTcpSocket):
    """"""
    # Enum QSslSocket.PeerVerifyMode
    VerifyNone = 0
    QueryPeer = 0
    VerifyPeer = 0
    AutoVerifyPeer = 0

    # Enum QSslSocket.SslMode
    UnencryptedMode = 0
    SslClientMode = 0
    SslServerMode = 0

    def __init__(self, parent = None):
        '''void QSslSocket.__init__(QObject parent = None)'''
    def setPeerVerifyName(self, hostName):
        '''void QSslSocket.setPeerVerifyName(QString hostName)'''
    def peerVerifyName(self):
        '''QString QSslSocket.peerVerifyName()'''
        return QString()
    def socketOption(self, option):
        '''QVariant QSslSocket.socketOption(QAbstractSocket.SocketOption option)'''
        return QVariant()
    def setSocketOption(self, option, value):
        '''void QSslSocket.setSocketOption(QAbstractSocket.SocketOption option, QVariant value)'''
    encryptedBytesWritten = pyqtSignal() # void encryptedBytesWritten(qint64) - signal
    peerVerifyError = pyqtSignal() # void peerVerifyError(const QSslErroramp;) - signal
    def setSslConfiguration(self, config):
        '''void QSslSocket.setSslConfiguration(QSslConfiguration config)'''
    def sslConfiguration(self):
        '''QSslConfiguration QSslSocket.sslConfiguration()'''
        return QSslConfiguration()
    def encryptedBytesToWrite(self):
        '''int QSslSocket.encryptedBytesToWrite()'''
        return int()
    def encryptedBytesAvailable(self):
        '''int QSslSocket.encryptedBytesAvailable()'''
        return int()
    def setReadBufferSize(self, size):
        '''void QSslSocket.setReadBufferSize(int size)'''
    def setPeerVerifyDepth(self, depth):
        '''void QSslSocket.setPeerVerifyDepth(int depth)'''
    def peerVerifyDepth(self):
        '''int QSslSocket.peerVerifyDepth()'''
        return int()
    def setPeerVerifyMode(self, mode):
        '''void QSslSocket.setPeerVerifyMode(QSslSocket.PeerVerifyMode mode)'''
    def peerVerifyMode(self):
        '''QSslSocket.PeerVerifyMode QSslSocket.peerVerifyMode()'''
        return QSslSocket.PeerVerifyMode()
    def writeData(self, data):
        '''int QSslSocket.writeData(str data)'''
        return int()
    def readData(self, maxlen):
        '''str QSslSocket.readData(int maxlen)'''
        return str()
    def disconnectFromHostImplementation(self):
        '''void QSslSocket.disconnectFromHostImplementation()'''
    def connectToHostImplementation(self, hostName, port, openMode):
        '''void QSslSocket.connectToHostImplementation(QString hostName, int port, QIODevice.OpenMode openMode)'''
    modeChanged = pyqtSignal() # void modeChanged(QSslSocket::SslMode) - signal
    encrypted = pyqtSignal() # void encrypted() - signal
    def ignoreSslErrors(self):
        '''void QSslSocket.ignoreSslErrors()'''
    def ignoreSslErrors(self, errors):
        '''void QSslSocket.ignoreSslErrors(list-of-QSslError errors)'''
    def startServerEncryption(self):
        '''void QSslSocket.startServerEncryption()'''
    def startClientEncryption(self):
        '''void QSslSocket.startClientEncryption()'''
    def supportsSsl(self):
        '''static bool QSslSocket.supportsSsl()'''
        return bool()
    def sslErrors(self):
        '''list-of-QSslError QSslSocket.sslErrors()'''
        return [QSslError()]
    sslErrors = pyqtSignal() # void sslErrors(const QListlt;QSslErrorgt;amp;) - signal
    def waitForDisconnected(self, msecs = 30000):
        '''bool QSslSocket.waitForDisconnected(int msecs = 30000)'''
        return bool()
    def waitForBytesWritten(self, msecs = 30000):
        '''bool QSslSocket.waitForBytesWritten(int msecs = 30000)'''
        return bool()
    def waitForReadyRead(self, msecs = 30000):
        '''bool QSslSocket.waitForReadyRead(int msecs = 30000)'''
        return bool()
    def waitForEncrypted(self, msecs = 30000):
        '''bool QSslSocket.waitForEncrypted(int msecs = 30000)'''
        return bool()
    def waitForConnected(self, msecs = 30000):
        '''bool QSslSocket.waitForConnected(int msecs = 30000)'''
        return bool()
    def systemCaCertificates(self):
        '''static list-of-QSslCertificate QSslSocket.systemCaCertificates()'''
        return [QSslCertificate()]
    def defaultCaCertificates(self):
        '''static list-of-QSslCertificate QSslSocket.defaultCaCertificates()'''
        return [QSslCertificate()]
    def setDefaultCaCertificates(self, certificates):
        '''static void QSslSocket.setDefaultCaCertificates(list-of-QSslCertificate certificates)'''
    def addDefaultCaCertificate(self, certificate):
        '''static void QSslSocket.addDefaultCaCertificate(QSslCertificate certificate)'''
    def addDefaultCaCertificates(self, path, format = None, syntax = None):
        '''static bool QSslSocket.addDefaultCaCertificates(QString path, QSsl.EncodingFormat format = QSsl.Pem, QRegExp.PatternSyntax syntax = QRegExp.FixedString)'''
        return bool()
    def addDefaultCaCertificates(self, certificates):
        '''static void QSslSocket.addDefaultCaCertificates(list-of-QSslCertificate certificates)'''
    def caCertificates(self):
        '''list-of-QSslCertificate QSslSocket.caCertificates()'''
        return [QSslCertificate()]
    def setCaCertificates(self, certificates):
        '''void QSslSocket.setCaCertificates(list-of-QSslCertificate certificates)'''
    def addCaCertificate(self, certificate):
        '''void QSslSocket.addCaCertificate(QSslCertificate certificate)'''
    def addCaCertificates(self, path, format = None, syntax = None):
        '''bool QSslSocket.addCaCertificates(QString path, QSsl.EncodingFormat format = QSsl.Pem, QRegExp.PatternSyntax syntax = QRegExp.FixedString)'''
        return bool()
    def addCaCertificates(self, certificates):
        '''void QSslSocket.addCaCertificates(list-of-QSslCertificate certificates)'''
    def supportedCiphers(self):
        '''static list-of-QSslCipher QSslSocket.supportedCiphers()'''
        return [QSslCipher()]
    def defaultCiphers(self):
        '''static list-of-QSslCipher QSslSocket.defaultCiphers()'''
        return [QSslCipher()]
    def setDefaultCiphers(self, ciphers):
        '''static void QSslSocket.setDefaultCiphers(list-of-QSslCipher ciphers)'''
    def setCiphers(self, ciphers):
        '''void QSslSocket.setCiphers(list-of-QSslCipher ciphers)'''
    def setCiphers(self, ciphers):
        '''void QSslSocket.setCiphers(QString ciphers)'''
    def ciphers(self):
        '''list-of-QSslCipher QSslSocket.ciphers()'''
        return [QSslCipher()]
    def privateKey(self):
        '''QSslKey QSslSocket.privateKey()'''
        return QSslKey()
    def setPrivateKey(self, key):
        '''void QSslSocket.setPrivateKey(QSslKey key)'''
    def setPrivateKey(self, fileName, algorithm = None, format = None, passPhrase = QByteArray()):
        '''void QSslSocket.setPrivateKey(QString fileName, QSsl.KeyAlgorithm algorithm = QSsl.Rsa, QSsl.EncodingFormat format = QSsl.Pem, QByteArray passPhrase = QByteArray())'''
    def sessionCipher(self):
        '''QSslCipher QSslSocket.sessionCipher()'''
        return QSslCipher()
    def peerCertificateChain(self):
        '''list-of-QSslCertificate QSslSocket.peerCertificateChain()'''
        return [QSslCertificate()]
    def peerCertificate(self):
        '''QSslCertificate QSslSocket.peerCertificate()'''
        return QSslCertificate()
    def localCertificate(self):
        '''QSslCertificate QSslSocket.localCertificate()'''
        return QSslCertificate()
    def setLocalCertificate(self, certificate):
        '''void QSslSocket.setLocalCertificate(QSslCertificate certificate)'''
    def setLocalCertificate(self, path, format = None):
        '''void QSslSocket.setLocalCertificate(QString path, QSsl.EncodingFormat format = QSsl.Pem)'''
    def abort(self):
        '''void QSslSocket.abort()'''
    def flush(self):
        '''bool QSslSocket.flush()'''
        return bool()
    def atEnd(self):
        '''bool QSslSocket.atEnd()'''
        return bool()
    def close(self):
        '''void QSslSocket.close()'''
    def canReadLine(self):
        '''bool QSslSocket.canReadLine()'''
        return bool()
    def bytesToWrite(self):
        '''int QSslSocket.bytesToWrite()'''
        return int()
    def bytesAvailable(self):
        '''int QSslSocket.bytesAvailable()'''
        return int()
    def setProtocol(self, protocol):
        '''void QSslSocket.setProtocol(QSsl.SslProtocol protocol)'''
    def protocol(self):
        '''QSsl.SslProtocol QSslSocket.protocol()'''
        return QSsl.SslProtocol()
    def isEncrypted(self):
        '''bool QSslSocket.isEncrypted()'''
        return bool()
    def mode(self):
        '''QSslSocket.SslMode QSslSocket.mode()'''
        return QSslSocket.SslMode()
    def setSocketDescriptor(self, socketDescriptor, state = None, mode = None):
        '''bool QSslSocket.setSocketDescriptor(int socketDescriptor, QAbstractSocket.SocketState state = QAbstractSocket.ConnectedState, QIODevice.OpenMode mode = QIODevice.ReadWrite)'''
        return bool()
    def connectToHostEncrypted(self, hostName, port, mode = None):
        '''void QSslSocket.connectToHostEncrypted(QString hostName, int port, QIODevice.OpenMode mode = QIODevice.ReadWrite)'''
    def connectToHostEncrypted(self, hostName, port, sslPeerName, mode = None):
        '''void QSslSocket.connectToHostEncrypted(QString hostName, int port, QString sslPeerName, QIODevice.OpenMode mode = QIODevice.ReadWrite)'''


class QTcpServer(QObject):
    """"""
    def __init__(self, parent = None):
        '''void QTcpServer.__init__(QObject parent = None)'''
    newConnection = pyqtSignal() # void newConnection() - signal
    def addPendingConnection(self, socket):
        '''void QTcpServer.addPendingConnection(QTcpSocket socket)'''
    def incomingConnection(self, handle):
        '''void QTcpServer.incomingConnection(int handle)'''
    def proxy(self):
        '''QNetworkProxy QTcpServer.proxy()'''
        return QNetworkProxy()
    def setProxy(self, networkProxy):
        '''void QTcpServer.setProxy(QNetworkProxy networkProxy)'''
    def errorString(self):
        '''QString QTcpServer.errorString()'''
        return QString()
    def serverError(self):
        '''QAbstractSocket.SocketError QTcpServer.serverError()'''
        return QAbstractSocket.SocketError()
    def nextPendingConnection(self):
        '''QTcpSocket QTcpServer.nextPendingConnection()'''
        return QTcpSocket()
    def hasPendingConnections(self):
        '''bool QTcpServer.hasPendingConnections()'''
        return bool()
    def waitForNewConnection(self, msecs = 0, timedOut = None):
        '''bool QTcpServer.waitForNewConnection(int msecs = 0, bool timedOut)'''
        return bool()
    def setSocketDescriptor(self, socketDescriptor):
        '''bool QTcpServer.setSocketDescriptor(int socketDescriptor)'''
        return bool()
    def socketDescriptor(self):
        '''int QTcpServer.socketDescriptor()'''
        return int()
    def serverAddress(self):
        '''QHostAddress QTcpServer.serverAddress()'''
        return QHostAddress()
    def serverPort(self):
        '''int QTcpServer.serverPort()'''
        return int()
    def maxPendingConnections(self):
        '''int QTcpServer.maxPendingConnections()'''
        return int()
    def setMaxPendingConnections(self, numConnections):
        '''void QTcpServer.setMaxPendingConnections(int numConnections)'''
    def isListening(self):
        '''bool QTcpServer.isListening()'''
        return bool()
    def close(self):
        '''void QTcpServer.close()'''
    def listen(self, address = None, port = 0):
        '''bool QTcpServer.listen(QHostAddress address = QHostAddress.Any, int port = 0)'''
        return bool()


class QUdpSocket(QAbstractSocket):
    """"""
    # Enum QUdpSocket.BindFlag
    DefaultForPlatform = 0
    ShareAddress = 0
    DontShareAddress = 0
    ReuseAddressHint = 0

    def __init__(self, parent = None):
        '''void QUdpSocket.__init__(QObject parent = None)'''
    def setMulticastInterface(self, iface):
        '''void QUdpSocket.setMulticastInterface(QNetworkInterface iface)'''
    def multicastInterface(self):
        '''QNetworkInterface QUdpSocket.multicastInterface()'''
        return QNetworkInterface()
    def leaveMulticastGroup(self, groupAddress):
        '''bool QUdpSocket.leaveMulticastGroup(QHostAddress groupAddress)'''
        return bool()
    def leaveMulticastGroup(self, groupAddress, iface):
        '''bool QUdpSocket.leaveMulticastGroup(QHostAddress groupAddress, QNetworkInterface iface)'''
        return bool()
    def joinMulticastGroup(self, groupAddress):
        '''bool QUdpSocket.joinMulticastGroup(QHostAddress groupAddress)'''
        return bool()
    def joinMulticastGroup(self, groupAddress, iface):
        '''bool QUdpSocket.joinMulticastGroup(QHostAddress groupAddress, QNetworkInterface iface)'''
        return bool()
    def writeDatagram(self, data, host, port):
        '''int QUdpSocket.writeDatagram(str data, QHostAddress host, int port)'''
        return int()
    def writeDatagram(self, datagram, host, port):
        '''int QUdpSocket.writeDatagram(QByteArray datagram, QHostAddress host, int port)'''
        return int()
    def readDatagram(self, maxlen, host, port):
        '''str QUdpSocket.readDatagram(int maxlen, QHostAddress host, int port)'''
        return str()
    def pendingDatagramSize(self):
        '''int QUdpSocket.pendingDatagramSize()'''
        return int()
    def hasPendingDatagrams(self):
        '''bool QUdpSocket.hasPendingDatagrams()'''
        return bool()
    def bind(self, address, port):
        '''bool QUdpSocket.bind(QHostAddress address, int port)'''
        return bool()
    def bind(self, port = 0):
        '''bool QUdpSocket.bind(int port = 0)'''
        return bool()
    def bind(self, address, port, mode):
        '''bool QUdpSocket.bind(QHostAddress address, int port, QUdpSocket.BindMode mode)'''
        return bool()
    def bind(self, port, mode):
        '''bool QUdpSocket.bind(int port, QUdpSocket.BindMode mode)'''
        return bool()
    class BindMode():
        """"""
        def __init__(self):
            '''QUdpSocket.BindMode QUdpSocket.BindMode.__init__()'''
            return QUdpSocket.BindMode()
        def __init__(self):
            '''int QUdpSocket.BindMode.__init__()'''
            return int()
        def __init__(self):
            '''void QUdpSocket.BindMode.__init__()'''
        def __bool__(self):
            '''int QUdpSocket.BindMode.__bool__()'''
            return int()
        def __ne__(self, f):
            '''bool QUdpSocket.BindMode.__ne__(QUdpSocket.BindMode f)'''
            return bool()
        def __eq__(self, f):
            '''bool QUdpSocket.BindMode.__eq__(QUdpSocket.BindMode f)'''
            return bool()
        def __invert__(self):
            '''QUdpSocket.BindMode QUdpSocket.BindMode.__invert__()'''
            return QUdpSocket.BindMode()
        def __and__(self, mask):
            '''QUdpSocket.BindMode QUdpSocket.BindMode.__and__(int mask)'''
            return QUdpSocket.BindMode()
        def __xor__(self, f):
            '''QUdpSocket.BindMode QUdpSocket.BindMode.__xor__(QUdpSocket.BindMode f)'''
            return QUdpSocket.BindMode()
        def __xor__(self, f):
            '''QUdpSocket.BindMode QUdpSocket.BindMode.__xor__(int f)'''
            return QUdpSocket.BindMode()
        def __or__(self, f):
            '''QUdpSocket.BindMode QUdpSocket.BindMode.__or__(QUdpSocket.BindMode f)'''
            return QUdpSocket.BindMode()
        def __or__(self, f):
            '''QUdpSocket.BindMode QUdpSocket.BindMode.__or__(int f)'''
            return QUdpSocket.BindMode()
        def __int__(self):
            '''int QUdpSocket.BindMode.__int__()'''
            return int()
        def __ixor__(self, f):
            '''QUdpSocket.BindMode QUdpSocket.BindMode.__ixor__(QUdpSocket.BindMode f)'''
            return QUdpSocket.BindMode()
        def __ior__(self, f):
            '''QUdpSocket.BindMode QUdpSocket.BindMode.__ior__(QUdpSocket.BindMode f)'''
            return QUdpSocket.BindMode()
        def __iand__(self, mask):
            '''QUdpSocket.BindMode QUdpSocket.BindMode.__iand__(int mask)'''
            return QUdpSocket.BindMode()


class QUrlInfo():
    """"""
    # Enum QUrlInfo.PermissionSpec
    ReadOwner = 0
    WriteOwner = 0
    ExeOwner = 0
    ReadGroup = 0
    WriteGroup = 0
    ExeGroup = 0
    ReadOther = 0
    WriteOther = 0
    ExeOther = 0

    def __init__(self):
        '''void QUrlInfo.__init__()'''
    def __init__(self, ui):
        '''void QUrlInfo.__init__(QUrlInfo ui)'''
    def __init__(self, name, permissions, owner, group, size, lastModified, lastRead, isDir, isFile, isSymLink, isWritable, isReadable, isExecutable):
        '''void QUrlInfo.__init__(QString name, int permissions, QString owner, QString group, int size, QDateTime lastModified, QDateTime lastRead, bool isDir, bool isFile, bool isSymLink, bool isWritable, bool isReadable, bool isExecutable)'''
    def __init__(self, url, permissions, owner, group, size, lastModified, lastRead, isDir, isFile, isSymLink, isWritable, isReadable, isExecutable):
        '''void QUrlInfo.__init__(QUrl url, int permissions, QString owner, QString group, int size, QDateTime lastModified, QDateTime lastRead, bool isDir, bool isFile, bool isSymLink, bool isWritable, bool isReadable, bool isExecutable)'''
    def __ne__(self, i):
        '''bool QUrlInfo.__ne__(QUrlInfo i)'''
        return bool()
    def __eq__(self, i):
        '''bool QUrlInfo.__eq__(QUrlInfo i)'''
        return bool()
    def setLastRead(self, dt):
        '''void QUrlInfo.setLastRead(QDateTime dt)'''
    def equal(self, i1, i2, sortBy):
        '''static bool QUrlInfo.equal(QUrlInfo i1, QUrlInfo i2, int sortBy)'''
        return bool()
    def lessThan(self, i1, i2, sortBy):
        '''static bool QUrlInfo.lessThan(QUrlInfo i1, QUrlInfo i2, int sortBy)'''
        return bool()
    def greaterThan(self, i1, i2, sortBy):
        '''static bool QUrlInfo.greaterThan(QUrlInfo i1, QUrlInfo i2, int sortBy)'''
        return bool()
    def isExecutable(self):
        '''bool QUrlInfo.isExecutable()'''
        return bool()
    def isReadable(self):
        '''bool QUrlInfo.isReadable()'''
        return bool()
    def isWritable(self):
        '''bool QUrlInfo.isWritable()'''
        return bool()
    def isSymLink(self):
        '''bool QUrlInfo.isSymLink()'''
        return bool()
    def isFile(self):
        '''bool QUrlInfo.isFile()'''
        return bool()
    def isDir(self):
        '''bool QUrlInfo.isDir()'''
        return bool()
    def lastRead(self):
        '''QDateTime QUrlInfo.lastRead()'''
        return QDateTime()
    def lastModified(self):
        '''QDateTime QUrlInfo.lastModified()'''
        return QDateTime()
    def size(self):
        '''int QUrlInfo.size()'''
        return int()
    def group(self):
        '''QString QUrlInfo.group()'''
        return QString()
    def owner(self):
        '''QString QUrlInfo.owner()'''
        return QString()
    def permissions(self):
        '''int QUrlInfo.permissions()'''
        return int()
    def name(self):
        '''QString QUrlInfo.name()'''
        return QString()
    def isValid(self):
        '''bool QUrlInfo.isValid()'''
        return bool()
    def setLastModified(self, dt):
        '''void QUrlInfo.setLastModified(QDateTime dt)'''
    def setPermissions(self, p):
        '''void QUrlInfo.setPermissions(int p)'''
    def setReadable(self, b):
        '''void QUrlInfo.setReadable(bool b)'''
    def setWritable(self, b):
        '''void QUrlInfo.setWritable(bool b)'''
    def setSize(self, size):
        '''void QUrlInfo.setSize(int size)'''
    def setGroup(self, s):
        '''void QUrlInfo.setGroup(QString s)'''
    def setOwner(self, s):
        '''void QUrlInfo.setOwner(QString s)'''
    def setSymLink(self, b):
        '''void QUrlInfo.setSymLink(bool b)'''
    def setFile(self, b):
        '''void QUrlInfo.setFile(bool b)'''
    def setDir(self, b):
        '''void QUrlInfo.setDir(bool b)'''
    def setName(self, name):
        '''void QUrlInfo.setName(QString name)'''


