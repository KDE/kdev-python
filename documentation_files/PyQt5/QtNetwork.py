class pyqtSignal():
 def connect(self, targetSignal): pass
 def emit(self, *args): pass
from QtCore import *

from QtWidgets import *

import datetime

class QNetworkCacheMetaData():
    """"""
    def __init__(self):
        '''void QNetworkCacheMetaData.__init__()'''
    def __init__(self, other):
        '''void QNetworkCacheMetaData.__init__(QNetworkCacheMetaData other)'''
    def swap(self, other):
        '''void QNetworkCacheMetaData.swap(QNetworkCacheMetaData other)'''
    def setAttributes(self, attributes):
        '''void QNetworkCacheMetaData.setAttributes(dict-of-QNetworkRequest.Attribute-object attributes)'''
    def attributes(self):
        '''dict-of-QNetworkRequest.Attribute-object QNetworkCacheMetaData.attributes()'''
        return {QNetworkRequest.Attribute():object()}
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
    # Enum QAbstractSocket.PauseMode
    PauseNever = 0
    PauseOnSslErrors = 0

    # Enum QAbstractSocket.BindFlag
    DefaultForPlatform = 0
    ShareAddress = 0
    DontShareAddress = 0
    ReuseAddressHint = 0

    # Enum QAbstractSocket.SocketOption
    LowDelayOption = 0
    KeepAliveOption = 0
    MulticastTtlOption = 0
    MulticastLoopbackOption = 0
    TypeOfServiceOption = 0
    SendBufferSizeSocketOption = 0
    ReceiveBufferSizeSocketOption = 0

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
    OperationError = 0
    SslInternalError = 0
    SslInvalidUserDataError = 0
    TemporaryError = 0
    UnknownSocketError = 0

    # Enum QAbstractSocket.NetworkLayerProtocol
    IPv4Protocol = 0
    IPv6Protocol = 0
    AnyIPProtocol = 0
    UnknownNetworkLayerProtocol = 0

    # Enum QAbstractSocket.SocketType
    TcpSocket = 0
    UdpSocket = 0
    UnknownSocketType = 0

    def __init__(self, socketType, parent):
        '''void QAbstractSocket.__init__(QAbstractSocket.SocketType socketType, QObject parent)'''
    def bind(self, address, port = 0, mode = None):
        '''bool QAbstractSocket.bind(QHostAddress address, int port = 0, QAbstractSocket.BindMode mode = QAbstractSocket.DefaultForPlatform)'''
        return bool()
    def bind(self, port = 0, mode = None):
        '''bool QAbstractSocket.bind(int port = 0, QAbstractSocket.BindMode mode = QAbstractSocket.DefaultForPlatform)'''
        return bool()
    def setPauseMode(self, pauseMode):
        '''void QAbstractSocket.setPauseMode(QAbstractSocket.PauseModes pauseMode)'''
    def pauseMode(self):
        '''QAbstractSocket.PauseModes QAbstractSocket.pauseMode()'''
        return QAbstractSocket.PauseModes()
    def resume(self):
        '''void QAbstractSocket.resume()'''
    def socketOption(self, option):
        '''QVariant QAbstractSocket.socketOption(QAbstractSocket.SocketOption option)'''
        return QVariant()
    def setSocketOption(self, option, value):
        '''void QAbstractSocket.setSocketOption(QAbstractSocket.SocketOption option, QVariant value)'''
    def setPeerName(self, name):
        '''void QAbstractSocket.setPeerName(str name)'''
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
    proxyAuthenticationRequired = pyqtSignal() # void proxyAuthenticationRequired(const QNetworkProxyamp;,QAuthenticator*) - signal
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
    def socketDescriptor(self):
        '''sip.voidptr QAbstractSocket.socketDescriptor()'''
        return sip.voidptr()
    def setSocketDescriptor(self, socketDescriptor, state = None, mode = None):
        '''bool QAbstractSocket.setSocketDescriptor(sip.voidptr socketDescriptor, QAbstractSocket.SocketState state = QAbstractSocket.ConnectedState, QIODevice.OpenMode mode = QIODevice.ReadWrite)'''
        return bool()
    def abort(self):
        '''void QAbstractSocket.abort()'''
    def setReadBufferSize(self, size):
        '''void QAbstractSocket.setReadBufferSize(int size)'''
    def readBufferSize(self):
        '''int QAbstractSocket.readBufferSize()'''
        return int()
    def peerName(self):
        '''str QAbstractSocket.peerName()'''
        return str()
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
    def connectToHost(self, hostName, port, mode = None, protocol = None):
        '''void QAbstractSocket.connectToHost(str hostName, int port, QIODevice.OpenMode mode = QIODevice.ReadWrite, QAbstractSocket.NetworkLayerProtocol protocol = QAbstractSocket.AnyIPProtocol)'''
    def connectToHost(self, address, port, mode = None):
        '''void QAbstractSocket.connectToHost(QHostAddress address, int port, QIODevice.OpenMode mode = QIODevice.ReadWrite)'''
    class BindMode():
        """"""
        def __init__(self):
            '''QAbstractSocket.BindMode QAbstractSocket.BindMode.__init__()'''
            return QAbstractSocket.BindMode()
        def __init__(self):
            '''int QAbstractSocket.BindMode.__init__()'''
            return int()
        def __init__(self):
            '''void QAbstractSocket.BindMode.__init__()'''
        def __bool__(self):
            '''int QAbstractSocket.BindMode.__bool__()'''
            return int()
        def __ne__(self, f):
            '''bool QAbstractSocket.BindMode.__ne__(QAbstractSocket.BindMode f)'''
            return bool()
        def __eq__(self, f):
            '''bool QAbstractSocket.BindMode.__eq__(QAbstractSocket.BindMode f)'''
            return bool()
        def __invert__(self):
            '''QAbstractSocket.BindMode QAbstractSocket.BindMode.__invert__()'''
            return QAbstractSocket.BindMode()
        def __and__(self, mask):
            '''QAbstractSocket.BindMode QAbstractSocket.BindMode.__and__(int mask)'''
            return QAbstractSocket.BindMode()
        def __xor__(self, f):
            '''QAbstractSocket.BindMode QAbstractSocket.BindMode.__xor__(QAbstractSocket.BindMode f)'''
            return QAbstractSocket.BindMode()
        def __xor__(self, f):
            '''QAbstractSocket.BindMode QAbstractSocket.BindMode.__xor__(int f)'''
            return QAbstractSocket.BindMode()
        def __or__(self, f):
            '''QAbstractSocket.BindMode QAbstractSocket.BindMode.__or__(QAbstractSocket.BindMode f)'''
            return QAbstractSocket.BindMode()
        def __or__(self, f):
            '''QAbstractSocket.BindMode QAbstractSocket.BindMode.__or__(int f)'''
            return QAbstractSocket.BindMode()
        def __int__(self):
            '''int QAbstractSocket.BindMode.__int__()'''
            return int()
        def __ixor__(self, f):
            '''QAbstractSocket.BindMode QAbstractSocket.BindMode.__ixor__(QAbstractSocket.BindMode f)'''
            return QAbstractSocket.BindMode()
        def __ior__(self, f):
            '''QAbstractSocket.BindMode QAbstractSocket.BindMode.__ior__(QAbstractSocket.BindMode f)'''
            return QAbstractSocket.BindMode()
        def __iand__(self, mask):
            '''QAbstractSocket.BindMode QAbstractSocket.BindMode.__iand__(int mask)'''
            return QAbstractSocket.BindMode()
    class PauseModes():
        """"""
        def __init__(self):
            '''QAbstractSocket.PauseModes QAbstractSocket.PauseModes.__init__()'''
            return QAbstractSocket.PauseModes()
        def __init__(self):
            '''int QAbstractSocket.PauseModes.__init__()'''
            return int()
        def __init__(self):
            '''void QAbstractSocket.PauseModes.__init__()'''
        def __bool__(self):
            '''int QAbstractSocket.PauseModes.__bool__()'''
            return int()
        def __ne__(self, f):
            '''bool QAbstractSocket.PauseModes.__ne__(QAbstractSocket.PauseModes f)'''
            return bool()
        def __eq__(self, f):
            '''bool QAbstractSocket.PauseModes.__eq__(QAbstractSocket.PauseModes f)'''
            return bool()
        def __invert__(self):
            '''QAbstractSocket.PauseModes QAbstractSocket.PauseModes.__invert__()'''
            return QAbstractSocket.PauseModes()
        def __and__(self, mask):
            '''QAbstractSocket.PauseModes QAbstractSocket.PauseModes.__and__(int mask)'''
            return QAbstractSocket.PauseModes()
        def __xor__(self, f):
            '''QAbstractSocket.PauseModes QAbstractSocket.PauseModes.__xor__(QAbstractSocket.PauseModes f)'''
            return QAbstractSocket.PauseModes()
        def __xor__(self, f):
            '''QAbstractSocket.PauseModes QAbstractSocket.PauseModes.__xor__(int f)'''
            return QAbstractSocket.PauseModes()
        def __or__(self, f):
            '''QAbstractSocket.PauseModes QAbstractSocket.PauseModes.__or__(QAbstractSocket.PauseModes f)'''
            return QAbstractSocket.PauseModes()
        def __or__(self, f):
            '''QAbstractSocket.PauseModes QAbstractSocket.PauseModes.__or__(int f)'''
            return QAbstractSocket.PauseModes()
        def __int__(self):
            '''int QAbstractSocket.PauseModes.__int__()'''
            return int()
        def __ixor__(self, f):
            '''QAbstractSocket.PauseModes QAbstractSocket.PauseModes.__ixor__(QAbstractSocket.PauseModes f)'''
            return QAbstractSocket.PauseModes()
        def __ior__(self, f):
            '''QAbstractSocket.PauseModes QAbstractSocket.PauseModes.__ior__(QAbstractSocket.PauseModes f)'''
            return QAbstractSocket.PauseModes()
        def __iand__(self, mask):
            '''QAbstractSocket.PauseModes QAbstractSocket.PauseModes.__iand__(int mask)'''
            return QAbstractSocket.PauseModes()


class QAuthenticator():
    """"""
    def __init__(self):
        '''void QAuthenticator.__init__()'''
    def __init__(self, other):
        '''void QAuthenticator.__init__(QAuthenticator other)'''
    def setOption(self, opt, value):
        '''void QAuthenticator.setOption(str opt, QVariant value)'''
    def options(self):
        '''dict-of-str-object QAuthenticator.options()'''
        return {str():object()}
    def option(self, opt):
        '''QVariant QAuthenticator.option(str opt)'''
        return QVariant()
    def isNull(self):
        '''bool QAuthenticator.isNull()'''
        return bool()
    def realm(self):
        '''str QAuthenticator.realm()'''
        return str()
    def setPassword(self, password):
        '''void QAuthenticator.setPassword(str password)'''
    def password(self):
        '''str QAuthenticator.password()'''
        return str()
    def setUser(self, user):
        '''void QAuthenticator.setUser(str user)'''
    def user(self):
        '''str QAuthenticator.user()'''
        return str()
    def __ne__(self, other):
        '''bool QAuthenticator.__ne__(QAuthenticator other)'''
        return bool()
    def __eq__(self, other):
        '''bool QAuthenticator.__eq__(QAuthenticator other)'''
        return bool()


class QDnsDomainNameRecord():
    """"""
    def __init__(self):
        '''void QDnsDomainNameRecord.__init__()'''
    def __init__(self, other):
        '''void QDnsDomainNameRecord.__init__(QDnsDomainNameRecord other)'''
    def value(self):
        '''str QDnsDomainNameRecord.value()'''
        return str()
    def timeToLive(self):
        '''int QDnsDomainNameRecord.timeToLive()'''
        return int()
    def name(self):
        '''str QDnsDomainNameRecord.name()'''
        return str()
    def swap(self, other):
        '''void QDnsDomainNameRecord.swap(QDnsDomainNameRecord other)'''


class QDnsHostAddressRecord():
    """"""
    def __init__(self):
        '''void QDnsHostAddressRecord.__init__()'''
    def __init__(self, other):
        '''void QDnsHostAddressRecord.__init__(QDnsHostAddressRecord other)'''
    def value(self):
        '''QHostAddress QDnsHostAddressRecord.value()'''
        return QHostAddress()
    def timeToLive(self):
        '''int QDnsHostAddressRecord.timeToLive()'''
        return int()
    def name(self):
        '''str QDnsHostAddressRecord.name()'''
        return str()
    def swap(self, other):
        '''void QDnsHostAddressRecord.swap(QDnsHostAddressRecord other)'''


class QDnsMailExchangeRecord():
    """"""
    def __init__(self):
        '''void QDnsMailExchangeRecord.__init__()'''
    def __init__(self, other):
        '''void QDnsMailExchangeRecord.__init__(QDnsMailExchangeRecord other)'''
    def timeToLive(self):
        '''int QDnsMailExchangeRecord.timeToLive()'''
        return int()
    def preference(self):
        '''int QDnsMailExchangeRecord.preference()'''
        return int()
    def name(self):
        '''str QDnsMailExchangeRecord.name()'''
        return str()
    def exchange(self):
        '''str QDnsMailExchangeRecord.exchange()'''
        return str()
    def swap(self, other):
        '''void QDnsMailExchangeRecord.swap(QDnsMailExchangeRecord other)'''


class QDnsServiceRecord():
    """"""
    def __init__(self):
        '''void QDnsServiceRecord.__init__()'''
    def __init__(self, other):
        '''void QDnsServiceRecord.__init__(QDnsServiceRecord other)'''
    def weight(self):
        '''int QDnsServiceRecord.weight()'''
        return int()
    def timeToLive(self):
        '''int QDnsServiceRecord.timeToLive()'''
        return int()
    def target(self):
        '''str QDnsServiceRecord.target()'''
        return str()
    def priority(self):
        '''int QDnsServiceRecord.priority()'''
        return int()
    def port(self):
        '''int QDnsServiceRecord.port()'''
        return int()
    def name(self):
        '''str QDnsServiceRecord.name()'''
        return str()
    def swap(self, other):
        '''void QDnsServiceRecord.swap(QDnsServiceRecord other)'''


class QDnsTextRecord():
    """"""
    def __init__(self):
        '''void QDnsTextRecord.__init__()'''
    def __init__(self, other):
        '''void QDnsTextRecord.__init__(QDnsTextRecord other)'''
    def values(self):
        '''list-of-QByteArray QDnsTextRecord.values()'''
        return [QByteArray()]
    def timeToLive(self):
        '''int QDnsTextRecord.timeToLive()'''
        return int()
    def name(self):
        '''str QDnsTextRecord.name()'''
        return str()
    def swap(self, other):
        '''void QDnsTextRecord.swap(QDnsTextRecord other)'''


class QDnsLookup(QObject):
    """"""
    # Enum QDnsLookup.Type
    A = 0
    AAAA = 0
    ANY = 0
    CNAME = 0
    MX = 0
    NS = 0
    PTR = 0
    SRV = 0
    TXT = 0

    # Enum QDnsLookup.Error
    NoError = 0
    ResolverError = 0
    OperationCancelledError = 0
    InvalidRequestError = 0
    InvalidReplyError = 0
    ServerFailureError = 0
    ServerRefusedError = 0
    NotFoundError = 0

    def __init__(self, parent = None):
        '''void QDnsLookup.__init__(QObject parent = None)'''
    def __init__(self, type, name, parent = None):
        '''void QDnsLookup.__init__(QDnsLookup.Type type, str name, QObject parent = None)'''
    def __init__(self, type, name, nameserver, parent = None):
        '''void QDnsLookup.__init__(QDnsLookup.Type type, str name, QHostAddress nameserver, QObject parent = None)'''
    nameserverChanged = pyqtSignal() # void nameserverChanged(const QHostAddressamp;) - signal
    def setNameserver(self, nameserver):
        '''void QDnsLookup.setNameserver(QHostAddress nameserver)'''
    def nameserver(self):
        '''QHostAddress QDnsLookup.nameserver()'''
        return QHostAddress()
    typeChanged = pyqtSignal() # void typeChanged(QDnsLookup::Type) - signal
    nameChanged = pyqtSignal() # void nameChanged(const QStringamp;) - signal
    finished = pyqtSignal() # void finished() - signal
    def lookup(self):
        '''void QDnsLookup.lookup()'''
    def abort(self):
        '''void QDnsLookup.abort()'''
    def textRecords(self):
        '''list-of-QDnsTextRecord QDnsLookup.textRecords()'''
        return [QDnsTextRecord()]
    def serviceRecords(self):
        '''list-of-QDnsServiceRecord QDnsLookup.serviceRecords()'''
        return [QDnsServiceRecord()]
    def pointerRecords(self):
        '''list-of-QDnsDomainNameRecord QDnsLookup.pointerRecords()'''
        return [QDnsDomainNameRecord()]
    def nameServerRecords(self):
        '''list-of-QDnsDomainNameRecord QDnsLookup.nameServerRecords()'''
        return [QDnsDomainNameRecord()]
    def mailExchangeRecords(self):
        '''list-of-QDnsMailExchangeRecord QDnsLookup.mailExchangeRecords()'''
        return [QDnsMailExchangeRecord()]
    def hostAddressRecords(self):
        '''list-of-QDnsHostAddressRecord QDnsLookup.hostAddressRecords()'''
        return [QDnsHostAddressRecord()]
    def canonicalNameRecords(self):
        '''list-of-QDnsDomainNameRecord QDnsLookup.canonicalNameRecords()'''
        return [QDnsDomainNameRecord()]
    def setType(self):
        '''QDnsLookup.Type QDnsLookup.setType()'''
        return QDnsLookup.Type()
    def type(self):
        '''QDnsLookup.Type QDnsLookup.type()'''
        return QDnsLookup.Type()
    def setName(self, name):
        '''void QDnsLookup.setName(str name)'''
    def name(self):
        '''str QDnsLookup.name()'''
        return str()
    def isFinished(self):
        '''bool QDnsLookup.isFinished()'''
        return bool()
    def errorString(self):
        '''str QDnsLookup.errorString()'''
        return str()
    def error(self):
        '''QDnsLookup.Error QDnsLookup.error()'''
        return QDnsLookup.Error()


class QHostAddress():
    """"""
    # Enum QHostAddress.SpecialAddress
    Null = 0
    Broadcast = 0
    LocalHost = 0
    LocalHostIPv6 = 0
    AnyIPv4 = 0
    AnyIPv6 = 0
    Any = 0

    def __init__(self):
        '''void QHostAddress.__init__()'''
    def __init__(self, address):
        '''void QHostAddress.__init__(QHostAddress.SpecialAddress address)'''
    def __init__(self, ip4Addr):
        '''void QHostAddress.__init__(int ip4Addr)'''
    def __init__(self, address):
        '''void QHostAddress.__init__(str address)'''
    def __init__(self, ip6Addr):
        '''void QHostAddress.__init__(16-tuple-of-int ip6Addr)'''
    def __init__(self, copy):
        '''void QHostAddress.__init__(QHostAddress copy)'''
    def parseSubnet(self, subnet):
        '''static tuple-of-QHostAddress-int QHostAddress.parseSubnet(str subnet)'''
        return tuple-of-QHostAddress-int()
    def isLoopback(self):
        '''bool QHostAddress.isLoopback()'''
        return bool()
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
        '''void QHostAddress.setScopeId(str id)'''
    def scopeId(self):
        '''str QHostAddress.scopeId()'''
        return str()
    def toString(self):
        '''str QHostAddress.toString()'''
        return str()
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
        '''bool QHostAddress.setAddress(str address)'''
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
        '''static str QHostInfo.localDomainName()'''
        return str()
    def localHostName(self):
        '''static str QHostInfo.localHostName()'''
        return str()
    def fromName(self, name):
        '''static QHostInfo QHostInfo.fromName(str name)'''
        return QHostInfo()
    def abortHostLookup(self, lookupId):
        '''static void QHostInfo.abortHostLookup(int lookupId)'''
    def lookupHost(self, name, slot):
        '''static int QHostInfo.lookupHost(str name, callable-or-signal slot)'''
        return int()
    def lookupId(self):
        '''int QHostInfo.lookupId()'''
        return int()
    def setLookupId(self, id):
        '''void QHostInfo.setLookupId(int id)'''
    def setErrorString(self, errorString):
        '''void QHostInfo.setErrorString(str errorString)'''
    def errorString(self):
        '''str QHostInfo.errorString()'''
        return str()
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
        '''void QHostInfo.setHostName(str name)'''
    def hostName(self):
        '''str QHostInfo.hostName()'''
        return str()


class QHttpPart():
    """"""
    def __init__(self):
        '''void QHttpPart.__init__()'''
    def __init__(self, other):
        '''void QHttpPart.__init__(QHttpPart other)'''
    def swap(self, other):
        '''void QHttpPart.swap(QHttpPart other)'''
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
    # Enum QLocalServer.SocketOption
    UserAccessOption = 0
    GroupAccessOption = 0
    OtherAccessOption = 0
    WorldAccessOption = 0

    def __init__(self, parent = None):
        '''void QLocalServer.__init__(QObject parent = None)'''
    def socketOptions(self):
        '''QLocalServer.SocketOptions QLocalServer.socketOptions()'''
        return QLocalServer.SocketOptions()
    def setSocketOptions(self, options):
        '''void QLocalServer.setSocketOptions(QLocalServer.SocketOptions options)'''
    def incomingConnection(self, socketDescriptor):
        '''void QLocalServer.incomingConnection(sip.voidptr socketDescriptor)'''
    newConnection = pyqtSignal() # void newConnection() - signal
    def removeServer(self, name):
        '''static bool QLocalServer.removeServer(str name)'''
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
        '''str QLocalServer.fullServerName()'''
        return str()
    def serverName(self):
        '''str QLocalServer.serverName()'''
        return str()
    def nextPendingConnection(self):
        '''QLocalSocket QLocalServer.nextPendingConnection()'''
        return QLocalSocket()
    def maxPendingConnections(self):
        '''int QLocalServer.maxPendingConnections()'''
        return int()
    def listen(self, name):
        '''bool QLocalServer.listen(str name)'''
        return bool()
    def listen(self, socketDescriptor):
        '''bool QLocalServer.listen(sip.voidptr socketDescriptor)'''
        return bool()
    def isListening(self):
        '''bool QLocalServer.isListening()'''
        return bool()
    def hasPendingConnections(self):
        '''bool QLocalServer.hasPendingConnections()'''
        return bool()
    def errorString(self):
        '''str QLocalServer.errorString()'''
        return str()
    def close(self):
        '''void QLocalServer.close()'''
    class SocketOptions():
        """"""
        def __init__(self):
            '''QLocalServer.SocketOptions QLocalServer.SocketOptions.__init__()'''
            return QLocalServer.SocketOptions()
        def __init__(self):
            '''int QLocalServer.SocketOptions.__init__()'''
            return int()
        def __init__(self):
            '''void QLocalServer.SocketOptions.__init__()'''
        def __bool__(self):
            '''int QLocalServer.SocketOptions.__bool__()'''
            return int()
        def __ne__(self, f):
            '''bool QLocalServer.SocketOptions.__ne__(QLocalServer.SocketOptions f)'''
            return bool()
        def __eq__(self, f):
            '''bool QLocalServer.SocketOptions.__eq__(QLocalServer.SocketOptions f)'''
            return bool()
        def __invert__(self):
            '''QLocalServer.SocketOptions QLocalServer.SocketOptions.__invert__()'''
            return QLocalServer.SocketOptions()
        def __and__(self, mask):
            '''QLocalServer.SocketOptions QLocalServer.SocketOptions.__and__(int mask)'''
            return QLocalServer.SocketOptions()
        def __xor__(self, f):
            '''QLocalServer.SocketOptions QLocalServer.SocketOptions.__xor__(QLocalServer.SocketOptions f)'''
            return QLocalServer.SocketOptions()
        def __xor__(self, f):
            '''QLocalServer.SocketOptions QLocalServer.SocketOptions.__xor__(int f)'''
            return QLocalServer.SocketOptions()
        def __or__(self, f):
            '''QLocalServer.SocketOptions QLocalServer.SocketOptions.__or__(QLocalServer.SocketOptions f)'''
            return QLocalServer.SocketOptions()
        def __or__(self, f):
            '''QLocalServer.SocketOptions QLocalServer.SocketOptions.__or__(int f)'''
            return QLocalServer.SocketOptions()
        def __int__(self):
            '''int QLocalServer.SocketOptions.__int__()'''
            return int()
        def __ixor__(self, f):
            '''QLocalServer.SocketOptions QLocalServer.SocketOptions.__ixor__(QLocalServer.SocketOptions f)'''
            return QLocalServer.SocketOptions()
        def __ior__(self, f):
            '''QLocalServer.SocketOptions QLocalServer.SocketOptions.__ior__(QLocalServer.SocketOptions f)'''
            return QLocalServer.SocketOptions()
        def __iand__(self, mask):
            '''QLocalServer.SocketOptions QLocalServer.SocketOptions.__iand__(int mask)'''
            return QLocalServer.SocketOptions()


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
    OperationError = 0
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
        '''str QLocalSocket.fullServerName()'''
        return str()
    def setServerName(self, name):
        '''void QLocalSocket.setServerName(str name)'''
    def serverName(self):
        '''str QLocalSocket.serverName()'''
        return str()
    def open(self, mode = None):
        '''bool QLocalSocket.open(QIODevice.OpenMode mode = QIODevice.ReadWrite)'''
        return bool()
    def disconnectFromServer(self):
        '''void QLocalSocket.disconnectFromServer()'''
    def connectToServer(self, name, mode = None):
        '''void QLocalSocket.connectToServer(str name, QIODevice.OpenMode mode = QIODevice.ReadWrite)'''
    def connectToServer(self, mode = None):
        '''void QLocalSocket.connectToServer(QIODevice.OpenMode mode = QIODevice.ReadWrite)'''


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
    def supportedSchemesImplementation(self):
        '''list-of-str QNetworkAccessManager.supportedSchemesImplementation()'''
        return [str()]
    def connectToHost(self, hostName, port = 80):
        '''void QNetworkAccessManager.connectToHost(str hostName, int port = 80)'''
    def connectToHostEncrypted(self, hostName, port = 443, sslConfiguration = None):
        '''void QNetworkAccessManager.connectToHostEncrypted(str hostName, int port = 443, QSslConfiguration sslConfiguration = QSslConfiguration.defaultConfiguration())'''
    def supportedSchemes(self):
        '''list-of-str QNetworkAccessManager.supportedSchemes()'''
        return [str()]
    def clearAccessCache(self):
        '''void QNetworkAccessManager.clearAccessCache()'''
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
    preSharedKeyAuthenticationRequired = pyqtSignal() # void preSharedKeyAuthenticationRequired(QNetworkReply*,QSslPreSharedKeyAuthenticator*) - signal
    networkAccessibleChanged = pyqtSignal() # void networkAccessibleChanged(QNetworkAccessManager::NetworkAccessibility) - signal
    sslErrors = pyqtSignal() # void sslErrors(QNetworkReply*,const QListlt;QSslErrorgt;amp;) - signal
    encrypted = pyqtSignal() # void encrypted(QNetworkReply*) - signal
    finished = pyqtSignal() # void finished(QNetworkReply*) - signal
    authenticationRequired = pyqtSignal() # void authenticationRequired(QNetworkReply*,QAuthenticator*) - signal
    proxyAuthenticationRequired = pyqtSignal() # void proxyAuthenticationRequired(const QNetworkProxyamp;,QAuthenticator*) - signal
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
        '''QNetworkConfiguration QNetworkConfigurationManager.configurationFromIdentifier(str identifier)'''
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
    BearerEVDO = 0
    BearerLTE = 0
    Bearer3G = 0
    Bearer4G = 0

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
    def swap(self, other):
        '''void QNetworkConfiguration.swap(QNetworkConfiguration other)'''
    def isValid(self):
        '''bool QNetworkConfiguration.isValid()'''
        return bool()
    def name(self):
        '''str QNetworkConfiguration.name()'''
        return str()
    def children(self):
        '''list-of-QNetworkConfiguration QNetworkConfiguration.children()'''
        return [QNetworkConfiguration()]
    def isRoamingAvailable(self):
        '''bool QNetworkConfiguration.isRoamingAvailable()'''
        return bool()
    def identifier(self):
        '''str QNetworkConfiguration.identifier()'''
        return str()
    def bearerTypeFamily(self):
        '''QNetworkConfiguration.BearerType QNetworkConfiguration.bearerTypeFamily()'''
        return QNetworkConfiguration.BearerType()
    def bearerTypeName(self):
        '''str QNetworkConfiguration.bearerTypeName()'''
        return str()
    def bearerType(self):
        '''QNetworkConfiguration.BearerType QNetworkConfiguration.bearerType()'''
        return QNetworkConfiguration.BearerType()
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
    def normalize(self, url):
        '''void QNetworkCookie.normalize(QUrl url)'''
    def hasSameIdentifier(self, other):
        '''bool QNetworkCookie.hasSameIdentifier(QNetworkCookie other)'''
        return bool()
    def swap(self, other):
        '''void QNetworkCookie.swap(QNetworkCookie other)'''
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
        '''void QNetworkCookie.setPath(str path)'''
    def path(self):
        '''str QNetworkCookie.path()'''
        return str()
    def setDomain(self, domain):
        '''void QNetworkCookie.setDomain(str domain)'''
    def domain(self):
        '''str QNetworkCookie.domain()'''
        return str()
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
    def validateCookie(self, cookie, url):
        '''bool QNetworkCookieJar.validateCookie(QNetworkCookie cookie, QUrl url)'''
        return bool()
    def allCookies(self):
        '''list-of-QNetworkCookie QNetworkCookieJar.allCookies()'''
        return [QNetworkCookie()]
    def setAllCookies(self, cookieList):
        '''void QNetworkCookieJar.setAllCookies(list-of-QNetworkCookie cookieList)'''
    def deleteCookie(self, cookie):
        '''bool QNetworkCookieJar.deleteCookie(QNetworkCookie cookie)'''
        return bool()
    def updateCookie(self, cookie):
        '''bool QNetworkCookieJar.updateCookie(QNetworkCookie cookie)'''
        return bool()
    def insertCookie(self, cookie):
        '''bool QNetworkCookieJar.insertCookie(QNetworkCookie cookie)'''
        return bool()
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
        '''QNetworkCacheMetaData QNetworkDiskCache.fileMetaData(str fileName)'''
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
        '''void QNetworkDiskCache.setCacheDirectory(str cacheDir)'''
    def cacheDirectory(self):
        '''str QNetworkDiskCache.cacheDirectory()'''
        return str()


class QNetworkAddressEntry():
    """"""
    def __init__(self):
        '''void QNetworkAddressEntry.__init__()'''
    def __init__(self, other):
        '''void QNetworkAddressEntry.__init__(QNetworkAddressEntry other)'''
    def swap(self, other):
        '''void QNetworkAddressEntry.swap(QNetworkAddressEntry other)'''
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
    def swap(self, other):
        '''void QNetworkInterface.swap(QNetworkInterface other)'''
    def humanReadableName(self):
        '''str QNetworkInterface.humanReadableName()'''
        return str()
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
        '''static QNetworkInterface QNetworkInterface.interfaceFromName(str name)'''
        return QNetworkInterface()
    def addressEntries(self):
        '''list-of-QNetworkAddressEntry QNetworkInterface.addressEntries()'''
        return [QNetworkAddressEntry()]
    def hardwareAddress(self):
        '''str QNetworkInterface.hardwareAddress()'''
        return str()
    def flags(self):
        '''QNetworkInterface.InterfaceFlags QNetworkInterface.flags()'''
        return QNetworkInterface.InterfaceFlags()
    def name(self):
        '''str QNetworkInterface.name()'''
        return str()
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
    def __init__(self, type, hostName = None, port = 0, user = None, password = None):
        '''void QNetworkProxy.__init__(QNetworkProxy.ProxyType type, str hostName = '', int port = 0, str user = '', str password = '')'''
    def __init__(self, other):
        '''void QNetworkProxy.__init__(QNetworkProxy other)'''
    def setRawHeader(self, headerName, value):
        '''void QNetworkProxy.setRawHeader(QByteArray headerName, QByteArray value)'''
    def rawHeader(self, headerName):
        '''QByteArray QNetworkProxy.rawHeader(QByteArray headerName)'''
        return QByteArray()
    def rawHeaderList(self):
        '''list-of-QByteArray QNetworkProxy.rawHeaderList()'''
        return [QByteArray()]
    def hasRawHeader(self, headerName):
        '''bool QNetworkProxy.hasRawHeader(QByteArray headerName)'''
        return bool()
    def setHeader(self, header, value):
        '''void QNetworkProxy.setHeader(QNetworkRequest.KnownHeaders header, QVariant value)'''
    def header(self, header):
        '''QVariant QNetworkProxy.header(QNetworkRequest.KnownHeaders header)'''
        return QVariant()
    def swap(self, other):
        '''void QNetworkProxy.swap(QNetworkProxy other)'''
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
        '''str QNetworkProxy.hostName()'''
        return str()
    def setHostName(self, hostName):
        '''void QNetworkProxy.setHostName(str hostName)'''
    def password(self):
        '''str QNetworkProxy.password()'''
        return str()
    def setPassword(self, password):
        '''void QNetworkProxy.setPassword(str password)'''
    def user(self):
        '''str QNetworkProxy.user()'''
        return str()
    def setUser(self, userName):
        '''void QNetworkProxy.setUser(str userName)'''
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
    def __init__(self, hostname, port, protocolTag = None, type = None):
        '''void QNetworkProxyQuery.__init__(str hostname, int port, str protocolTag = '', QNetworkProxyQuery.QueryType type = QNetworkProxyQuery.TcpSocket)'''
    def __init__(self, bindPort, protocolTag = None, type = None):
        '''void QNetworkProxyQuery.__init__(int bindPort, str protocolTag = '', QNetworkProxyQuery.QueryType type = QNetworkProxyQuery.TcpServer)'''
    def __init__(self, networkConfiguration, requestUrl, queryType = None):
        '''void QNetworkProxyQuery.__init__(QNetworkConfiguration networkConfiguration, QUrl requestUrl, QNetworkProxyQuery.QueryType queryType = QNetworkProxyQuery.UrlRequest)'''
    def __init__(self, networkConfiguration, hostname, port, protocolTag = None, type = None):
        '''void QNetworkProxyQuery.__init__(QNetworkConfiguration networkConfiguration, str hostname, int port, str protocolTag = '', QNetworkProxyQuery.QueryType type = QNetworkProxyQuery.TcpSocket)'''
    def __init__(self, networkConfiguration, bindPort, protocolTag = None, type = None):
        '''void QNetworkProxyQuery.__init__(QNetworkConfiguration networkConfiguration, int bindPort, str protocolTag = '', QNetworkProxyQuery.QueryType type = QNetworkProxyQuery.TcpServer)'''
    def __init__(self, other):
        '''void QNetworkProxyQuery.__init__(QNetworkProxyQuery other)'''
    def swap(self, other):
        '''void QNetworkProxyQuery.swap(QNetworkProxyQuery other)'''
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
        '''void QNetworkProxyQuery.setProtocolTag(str protocolTag)'''
    def protocolTag(self):
        '''str QNetworkProxyQuery.protocolTag()'''
        return str()
    def setLocalPort(self, port):
        '''void QNetworkProxyQuery.setLocalPort(int port)'''
    def localPort(self):
        '''int QNetworkProxyQuery.localPort()'''
        return int()
    def setPeerHostName(self, hostname):
        '''void QNetworkProxyQuery.setPeerHostName(str hostname)'''
    def peerHostName(self):
        '''str QNetworkProxyQuery.peerHostName()'''
        return str()
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
    NetworkSessionFailedError = 0
    BackgroundRequestNotAllowedError = 0
    ContentConflictError = 0
    ContentGoneError = 0
    InternalServerError = 0
    OperationNotImplementedError = 0
    ServiceUnavailableError = 0
    UnknownServerError = 0

    def __init__(self, parent = None):
        '''void QNetworkReply.__init__(QObject parent = None)'''
    def ignoreSslErrorsImplementation(self):
        '''list-of-QSslError QNetworkReply.ignoreSslErrorsImplementation()'''
        return [QSslError()]
    def setSslConfigurationImplementation(self):
        '''QSslConfiguration QNetworkReply.setSslConfigurationImplementation()'''
        return QSslConfiguration()
    def sslConfigurationImplementation(self):
        '''QSslConfiguration QNetworkReply.sslConfigurationImplementation()'''
        return QSslConfiguration()
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
        '''void QNetworkReply.setError(QNetworkReply.NetworkError errorCode, str errorString)'''
    def setRequest(self, request):
        '''void QNetworkReply.setRequest(QNetworkRequest request)'''
    def setOperation(self, operation):
        '''void QNetworkReply.setOperation(QNetworkAccessManager.Operation operation)'''
    def writeData(self, data):
        '''int QNetworkReply.writeData(str data)'''
        return int()
    preSharedKeyAuthenticationRequired = pyqtSignal() # void preSharedKeyAuthenticationRequired(QSslPreSharedKeyAuthenticator*) - signal
    downloadProgress = pyqtSignal() # void downloadProgress(qint64,qint64) - signal
    uploadProgress = pyqtSignal() # void uploadProgress(qint64,qint64) - signal
    sslErrors = pyqtSignal() # void sslErrors(const QListlt;QSslErrorgt;amp;) - signal
    encrypted = pyqtSignal() # void encrypted() - signal
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
    BackgroundRequestAttribute = 0
    SpdyAllowedAttribute = 0
    SpdyWasUsedAttribute = 0
    EmitAllUploadProgressSignalsAttribute = 0
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
    UserAgentHeader = 0
    ServerHeader = 0

    def __init__(self, url = QUrl()):
        '''void QNetworkRequest.__init__(QUrl url = QUrl())'''
    def __init__(self, other):
        '''void QNetworkRequest.__init__(QNetworkRequest other)'''
    def swap(self, other):
        '''void QNetworkRequest.swap(QNetworkRequest other)'''
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
    def attribute(self, code, defaultValue = None):
        '''QVariant QNetworkRequest.attribute(QNetworkRequest.Attribute code, QVariant defaultValue = None)'''
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
    # Enum QNetworkSession.UsagePolicy
    NoPolicy = 0
    NoBackgroundTrafficPolicy = 0

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
    usagePoliciesChanged = pyqtSignal() # void usagePoliciesChanged(QNetworkSession::UsagePolicies) - signal
    def usagePolicies(self):
        '''QNetworkSession.UsagePolicies QNetworkSession.usagePolicies()'''
        return QNetworkSession.UsagePolicies()
    def disconnectNotify(self, signal):
        '''void QNetworkSession.disconnectNotify(QMetaMethod signal)'''
    def connectNotify(self, signal):
        '''void QNetworkSession.connectNotify(QMetaMethod signal)'''
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
        '''void QNetworkSession.setSessionProperty(str key, QVariant value)'''
    def sessionProperty(self, key):
        '''QVariant QNetworkSession.sessionProperty(str key)'''
        return QVariant()
    def errorString(self):
        '''str QNetworkSession.errorString()'''
        return str()
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
    class UsagePolicies():
        """"""
        def __init__(self):
            '''QNetworkSession.UsagePolicies QNetworkSession.UsagePolicies.__init__()'''
            return QNetworkSession.UsagePolicies()
        def __init__(self):
            '''int QNetworkSession.UsagePolicies.__init__()'''
            return int()
        def __init__(self):
            '''void QNetworkSession.UsagePolicies.__init__()'''
        def __bool__(self):
            '''int QNetworkSession.UsagePolicies.__bool__()'''
            return int()
        def __ne__(self, f):
            '''bool QNetworkSession.UsagePolicies.__ne__(QNetworkSession.UsagePolicies f)'''
            return bool()
        def __eq__(self, f):
            '''bool QNetworkSession.UsagePolicies.__eq__(QNetworkSession.UsagePolicies f)'''
            return bool()
        def __invert__(self):
            '''QNetworkSession.UsagePolicies QNetworkSession.UsagePolicies.__invert__()'''
            return QNetworkSession.UsagePolicies()
        def __and__(self, mask):
            '''QNetworkSession.UsagePolicies QNetworkSession.UsagePolicies.__and__(int mask)'''
            return QNetworkSession.UsagePolicies()
        def __xor__(self, f):
            '''QNetworkSession.UsagePolicies QNetworkSession.UsagePolicies.__xor__(QNetworkSession.UsagePolicies f)'''
            return QNetworkSession.UsagePolicies()
        def __xor__(self, f):
            '''QNetworkSession.UsagePolicies QNetworkSession.UsagePolicies.__xor__(int f)'''
            return QNetworkSession.UsagePolicies()
        def __or__(self, f):
            '''QNetworkSession.UsagePolicies QNetworkSession.UsagePolicies.__or__(QNetworkSession.UsagePolicies f)'''
            return QNetworkSession.UsagePolicies()
        def __or__(self, f):
            '''QNetworkSession.UsagePolicies QNetworkSession.UsagePolicies.__or__(int f)'''
            return QNetworkSession.UsagePolicies()
        def __int__(self):
            '''int QNetworkSession.UsagePolicies.__int__()'''
            return int()
        def __ixor__(self, f):
            '''QNetworkSession.UsagePolicies QNetworkSession.UsagePolicies.__ixor__(QNetworkSession.UsagePolicies f)'''
            return QNetworkSession.UsagePolicies()
        def __ior__(self, f):
            '''QNetworkSession.UsagePolicies QNetworkSession.UsagePolicies.__ior__(QNetworkSession.UsagePolicies f)'''
            return QNetworkSession.UsagePolicies()
        def __iand__(self, mask):
            '''QNetworkSession.UsagePolicies QNetworkSession.UsagePolicies.__iand__(int mask)'''
            return QNetworkSession.UsagePolicies()


class QSsl():
    """"""
    # Enum QSsl.SslOption
    SslOptionDisableEmptyFragments = 0
    SslOptionDisableSessionTickets = 0
    SslOptionDisableCompression = 0
    SslOptionDisableServerNameIndication = 0
    SslOptionDisableLegacyRenegotiation = 0
    SslOptionDisableSessionSharing = 0
    SslOptionDisableSessionPersistence = 0

    # Enum QSsl.SslProtocol
    UnknownProtocol = 0
    SslV3 = 0
    SslV2 = 0
    TlsV1_0 = 0
    TlsV1_0OrLater = 0
    TlsV1_1 = 0
    TlsV1_1OrLater = 0
    TlsV1_2 = 0
    TlsV1_2OrLater = 0
    AnyProtocol = 0
    TlsV1SslV3 = 0
    SecureProtocols = 0

    # Enum QSsl.AlternativeNameEntryType
    EmailEntry = 0
    DnsEntry = 0

    # Enum QSsl.KeyAlgorithm
    Opaque = 0
    Rsa = 0
    Dsa = 0
    Ec = 0

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
    DistinguishedNameQualifier = 0
    SerialNumber = 0
    EmailAddress = 0

    def __init__(self, device, format = None):
        '''void QSslCertificate.__init__(QIODevice device, QSsl.EncodingFormat format = QSsl.Pem)'''
    def __init__(self, data = QByteArray(), format = None):
        '''void QSslCertificate.__init__(QByteArray data = QByteArray(), QSsl.EncodingFormat format = QSsl.Pem)'''
    def __init__(self, other):
        '''void QSslCertificate.__init__(QSslCertificate other)'''
    def importPkcs12(self, device, key, certificate, caCertificates = None, passPhrase = QByteArray()):
        '''static bool QSslCertificate.importPkcs12(QIODevice device, QSslKey key, QSslCertificate certificate, list-of-QSslCertificate caCertificates = None, QByteArray passPhrase = QByteArray())'''
        return bool()
    def __hash__(self):
        '''int QSslCertificate.__hash__()'''
        return int()
    def isSelfSigned(self):
        '''bool QSslCertificate.isSelfSigned()'''
        return bool()
    def verify(self, certificateChain, hostName = str()):
        '''static list-of-QSslError QSslCertificate.verify(list-of-QSslCertificate certificateChain, str hostName = str())'''
        return [QSslError()]
    def toText(self):
        '''str QSslCertificate.toText()'''
        return str()
    def extensions(self):
        '''list-of-QSslCertificateExtension QSslCertificate.extensions()'''
        return [QSslCertificateExtension()]
    def issuerInfoAttributes(self):
        '''list-of-QByteArray QSslCertificate.issuerInfoAttributes()'''
        return [QByteArray()]
    def subjectInfoAttributes(self):
        '''list-of-QByteArray QSslCertificate.subjectInfoAttributes()'''
        return [QByteArray()]
    def isBlacklisted(self):
        '''bool QSslCertificate.isBlacklisted()'''
        return bool()
    def swap(self, other):
        '''void QSslCertificate.swap(QSslCertificate other)'''
    def handle(self):
        '''sip.voidptr QSslCertificate.handle()'''
        return sip.voidptr()
    def fromData(self, data, format = None):
        '''static list-of-QSslCertificate QSslCertificate.fromData(QByteArray data, QSsl.EncodingFormat format = QSsl.Pem)'''
        return [QSslCertificate()]
    def fromDevice(self, device, format = None):
        '''static list-of-QSslCertificate QSslCertificate.fromDevice(QIODevice device, QSsl.EncodingFormat format = QSsl.Pem)'''
        return [QSslCertificate()]
    def fromPath(self, path, format = None, syntax = None):
        '''static list-of-QSslCertificate QSslCertificate.fromPath(str path, QSsl.EncodingFormat format = QSsl.Pem, QRegExp.PatternSyntax syntax = QRegExp.FixedString)'''
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
    def subjectAlternativeNames(self):
        '''dict-of-QSsl.AlternativeNameEntryType-list-of-str QSslCertificate.subjectAlternativeNames()'''
        return {QSsl.AlternativeNameEntryType():list()}
    def subjectInfo(self, info):
        '''list-of-str QSslCertificate.subjectInfo(QSslCertificate.SubjectInfo info)'''
        return [str()]
    def subjectInfo(self, attribute):
        '''list-of-str QSslCertificate.subjectInfo(QByteArray attribute)'''
        return [str()]
    def issuerInfo(self, info):
        '''list-of-str QSslCertificate.issuerInfo(QSslCertificate.SubjectInfo info)'''
        return [str()]
    def issuerInfo(self, attribute):
        '''list-of-str QSslCertificate.issuerInfo(QByteArray attribute)'''
        return [str()]
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
    def isNull(self):
        '''bool QSslCertificate.isNull()'''
        return bool()
    def __ne__(self, other):
        '''bool QSslCertificate.__ne__(QSslCertificate other)'''
        return bool()
    def __eq__(self, other):
        '''bool QSslCertificate.__eq__(QSslCertificate other)'''
        return bool()


class QSslCertificateExtension():
    """"""
    def __init__(self):
        '''void QSslCertificateExtension.__init__()'''
    def __init__(self, other):
        '''void QSslCertificateExtension.__init__(QSslCertificateExtension other)'''
    def isSupported(self):
        '''bool QSslCertificateExtension.isSupported()'''
        return bool()
    def isCritical(self):
        '''bool QSslCertificateExtension.isCritical()'''
        return bool()
    def value(self):
        '''QVariant QSslCertificateExtension.value()'''
        return QVariant()
    def name(self):
        '''str QSslCertificateExtension.name()'''
        return str()
    def oid(self):
        '''str QSslCertificateExtension.oid()'''
        return str()
    def swap(self, other):
        '''void QSslCertificateExtension.swap(QSslCertificateExtension other)'''


class QSslConfiguration():
    """"""
    # Enum QSslConfiguration.NextProtocolNegotiationStatus
    NextProtocolNegotiationNone = 0
    NextProtocolNegotiationNegotiated = 0
    NextProtocolNegotiationUnsupported = 0

    NextProtocolHttp1_1 = None # str - member
    NextProtocolSpdy3_0 = None # str - member
    def __init__(self):
        '''void QSslConfiguration.__init__()'''
    def __init__(self, other):
        '''void QSslConfiguration.__init__(QSslConfiguration other)'''
    def supportedEllipticCurves(self):
        '''static list-of-QSslEllipticCurve QSslConfiguration.supportedEllipticCurves()'''
        return [QSslEllipticCurve()]
    def setEllipticCurves(self, curves):
        '''void QSslConfiguration.setEllipticCurves(list-of-QSslEllipticCurve curves)'''
    def ellipticCurves(self):
        '''list-of-QSslEllipticCurve QSslConfiguration.ellipticCurves()'''
        return [QSslEllipticCurve()]
    def systemCaCertificates(self):
        '''static list-of-QSslCertificate QSslConfiguration.systemCaCertificates()'''
        return [QSslCertificate()]
    def supportedCiphers(self):
        '''static list-of-QSslCipher QSslConfiguration.supportedCiphers()'''
        return [QSslCipher()]
    def sessionProtocol(self):
        '''QSsl.SslProtocol QSslConfiguration.sessionProtocol()'''
        return QSsl.SslProtocol()
    def nextProtocolNegotiationStatus(self):
        '''QSslConfiguration.NextProtocolNegotiationStatus QSslConfiguration.nextProtocolNegotiationStatus()'''
        return QSslConfiguration.NextProtocolNegotiationStatus()
    def nextNegotiatedProtocol(self):
        '''QByteArray QSslConfiguration.nextNegotiatedProtocol()'''
        return QByteArray()
    def allowedNextProtocols(self):
        '''list-of-QByteArray QSslConfiguration.allowedNextProtocols()'''
        return [QByteArray()]
    def setAllowedNextProtocols(self, protocols):
        '''void QSslConfiguration.setAllowedNextProtocols(list-of-QByteArray protocols)'''
    def sessionTicketLifeTimeHint(self):
        '''int QSslConfiguration.sessionTicketLifeTimeHint()'''
        return int()
    def setSessionTicket(self, sessionTicket):
        '''void QSslConfiguration.setSessionTicket(QByteArray sessionTicket)'''
    def sessionTicket(self):
        '''QByteArray QSslConfiguration.sessionTicket()'''
        return QByteArray()
    def setLocalCertificateChain(self, localChain):
        '''void QSslConfiguration.setLocalCertificateChain(list-of-QSslCertificate localChain)'''
    def localCertificateChain(self):
        '''list-of-QSslCertificate QSslConfiguration.localCertificateChain()'''
        return [QSslCertificate()]
    def swap(self, other):
        '''void QSslConfiguration.swap(QSslConfiguration other)'''
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
    def __init__(self, name):
        '''void QSslCipher.__init__(str name)'''
    def __init__(self, name, protocol):
        '''void QSslCipher.__init__(str name, QSsl.SslProtocol protocol)'''
    def __init__(self, other):
        '''void QSslCipher.__init__(QSslCipher other)'''
    def swap(self, other):
        '''void QSslCipher.swap(QSslCipher other)'''
    def protocol(self):
        '''QSsl.SslProtocol QSslCipher.protocol()'''
        return QSsl.SslProtocol()
    def protocolString(self):
        '''str QSslCipher.protocolString()'''
        return str()
    def encryptionMethod(self):
        '''str QSslCipher.encryptionMethod()'''
        return str()
    def authenticationMethod(self):
        '''str QSslCipher.authenticationMethod()'''
        return str()
    def keyExchangeMethod(self):
        '''str QSslCipher.keyExchangeMethod()'''
        return str()
    def usedBits(self):
        '''int QSslCipher.usedBits()'''
        return int()
    def supportedBits(self):
        '''int QSslCipher.supportedBits()'''
        return int()
    def name(self):
        '''str QSslCipher.name()'''
        return str()
    def isNull(self):
        '''bool QSslCipher.isNull()'''
        return bool()
    def __ne__(self, other):
        '''bool QSslCipher.__ne__(QSslCipher other)'''
        return bool()
    def __eq__(self, other):
        '''bool QSslCipher.__eq__(QSslCipher other)'''
        return bool()


class QSslEllipticCurve():
    """"""
    def __init__(self):
        '''void QSslEllipticCurve.__init__()'''
    def __init__(self):
        '''QSslEllipticCurve QSslEllipticCurve.__init__()'''
        return QSslEllipticCurve()
    def __eq__(self, rhs):
        '''bool QSslEllipticCurve.__eq__(QSslEllipticCurve rhs)'''
        return bool()
    def __ne__(self, rhs):
        '''bool QSslEllipticCurve.__ne__(QSslEllipticCurve rhs)'''
        return bool()
    def __hash__(self):
        '''int QSslEllipticCurve.__hash__()'''
        return int()
    def isTlsNamedCurve(self):
        '''bool QSslEllipticCurve.isTlsNamedCurve()'''
        return bool()
    def isValid(self):
        '''bool QSslEllipticCurve.isValid()'''
        return bool()
    def longName(self):
        '''str QSslEllipticCurve.longName()'''
        return str()
    def shortName(self):
        '''str QSslEllipticCurve.shortName()'''
        return str()
    def fromLongName(self, name):
        '''static QSslEllipticCurve QSslEllipticCurve.fromLongName(str name)'''
        return QSslEllipticCurve()
    def fromShortName(self, name):
        '''static QSslEllipticCurve QSslEllipticCurve.fromShortName(str name)'''
        return QSslEllipticCurve()


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
    def __hash__(self):
        '''int QSslError.__hash__()'''
        return int()
    def swap(self, other):
        '''void QSslError.swap(QSslError other)'''
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
        '''str QSslError.errorString()'''
        return str()
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
    def __init__(self, handle, type = None):
        '''void QSslKey.__init__(sip.voidptr handle, QSsl.KeyType type = QSsl.PrivateKey)'''
    def __init__(self, other):
        '''void QSslKey.__init__(QSslKey other)'''
    def swap(self, other):
        '''void QSslKey.swap(QSslKey other)'''
    def __ne__(self, key):
        '''bool QSslKey.__ne__(QSslKey key)'''
        return bool()
    def __eq__(self, key):
        '''bool QSslKey.__eq__(QSslKey key)'''
        return bool()
    def handle(self):
        '''sip.voidptr QSslKey.handle()'''
        return sip.voidptr()
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


class QSslPreSharedKeyAuthenticator():
    """"""
    def __init__(self):
        '''void QSslPreSharedKeyAuthenticator.__init__()'''
    def __init__(self, authenticator):
        '''void QSslPreSharedKeyAuthenticator.__init__(QSslPreSharedKeyAuthenticator authenticator)'''
    def __eq__(self, rhs):
        '''bool QSslPreSharedKeyAuthenticator.__eq__(QSslPreSharedKeyAuthenticator rhs)'''
        return bool()
    def __ne__(self, rhs):
        '''bool QSslPreSharedKeyAuthenticator.__ne__(QSslPreSharedKeyAuthenticator rhs)'''
        return bool()
    def maximumPreSharedKeyLength(self):
        '''int QSslPreSharedKeyAuthenticator.maximumPreSharedKeyLength()'''
        return int()
    def preSharedKey(self):
        '''QByteArray QSslPreSharedKeyAuthenticator.preSharedKey()'''
        return QByteArray()
    def setPreSharedKey(self, preSharedKey):
        '''void QSslPreSharedKeyAuthenticator.setPreSharedKey(QByteArray preSharedKey)'''
    def maximumIdentityLength(self):
        '''int QSslPreSharedKeyAuthenticator.maximumIdentityLength()'''
        return int()
    def identity(self):
        '''QByteArray QSslPreSharedKeyAuthenticator.identity()'''
        return QByteArray()
    def setIdentity(self, identity):
        '''void QSslPreSharedKeyAuthenticator.setIdentity(QByteArray identity)'''
    def identityHint(self):
        '''QByteArray QSslPreSharedKeyAuthenticator.identityHint()'''
        return QByteArray()
    def swap(self, authenticator):
        '''void QSslPreSharedKeyAuthenticator.swap(QSslPreSharedKeyAuthenticator authenticator)'''


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
    def sslLibraryBuildVersionString(self):
        '''static str QSslSocket.sslLibraryBuildVersionString()'''
        return str()
    def sslLibraryBuildVersionNumber(self):
        '''static int QSslSocket.sslLibraryBuildVersionNumber()'''
        return int()
    def sessionProtocol(self):
        '''QSsl.SslProtocol QSslSocket.sessionProtocol()'''
        return QSsl.SslProtocol()
    def localCertificateChain(self):
        '''list-of-QSslCertificate QSslSocket.localCertificateChain()'''
        return [QSslCertificate()]
    def setLocalCertificateChain(self, localChain):
        '''void QSslSocket.setLocalCertificateChain(list-of-QSslCertificate localChain)'''
    def sslLibraryVersionString(self):
        '''static str QSslSocket.sslLibraryVersionString()'''
        return str()
    def sslLibraryVersionNumber(self):
        '''static int QSslSocket.sslLibraryVersionNumber()'''
        return int()
    def disconnectFromHost(self):
        '''void QSslSocket.disconnectFromHost()'''
    def connectToHost(self, hostName, port, mode = None, protocol = None):
        '''void QSslSocket.connectToHost(str hostName, int port, QIODevice.OpenMode mode = QIODevice.ReadWrite, QAbstractSocket.NetworkLayerProtocol protocol = QAbstractSocket.AnyIPProtocol)'''
    def resume(self):
        '''void QSslSocket.resume()'''
    def setPeerVerifyName(self, hostName):
        '''void QSslSocket.setPeerVerifyName(str hostName)'''
    def peerVerifyName(self):
        '''str QSslSocket.peerVerifyName()'''
        return str()
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
    preSharedKeyAuthenticationRequired = pyqtSignal() # void preSharedKeyAuthenticationRequired(QSslPreSharedKeyAuthenticator*) - signal
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
        '''static bool QSslSocket.addDefaultCaCertificates(str path, QSsl.EncodingFormat format = QSsl.Pem, QRegExp.PatternSyntax syntax = QRegExp.FixedString)'''
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
        '''bool QSslSocket.addCaCertificates(str path, QSsl.EncodingFormat format = QSsl.Pem, QRegExp.PatternSyntax syntax = QRegExp.FixedString)'''
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
        '''void QSslSocket.setCiphers(str ciphers)'''
    def ciphers(self):
        '''list-of-QSslCipher QSslSocket.ciphers()'''
        return [QSslCipher()]
    def privateKey(self):
        '''QSslKey QSslSocket.privateKey()'''
        return QSslKey()
    def setPrivateKey(self, key):
        '''void QSslSocket.setPrivateKey(QSslKey key)'''
    def setPrivateKey(self, fileName, algorithm = None, format = None, passPhrase = QByteArray()):
        '''void QSslSocket.setPrivateKey(str fileName, QSsl.KeyAlgorithm algorithm = QSsl.Rsa, QSsl.EncodingFormat format = QSsl.Pem, QByteArray passPhrase = QByteArray())'''
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
        '''void QSslSocket.setLocalCertificate(str path, QSsl.EncodingFormat format = QSsl.Pem)'''
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
        '''bool QSslSocket.setSocketDescriptor(sip.voidptr socketDescriptor, QAbstractSocket.SocketState state = QAbstractSocket.ConnectedState, QIODevice.OpenMode mode = QIODevice.ReadWrite)'''
        return bool()
    def connectToHostEncrypted(self, hostName, port, mode = None, protocol = None):
        '''void QSslSocket.connectToHostEncrypted(str hostName, int port, QIODevice.OpenMode mode = QIODevice.ReadWrite, QAbstractSocket.NetworkLayerProtocol protocol = QAbstractSocket.AnyIPProtocol)'''
    def connectToHostEncrypted(self, hostName, port, sslPeerName, mode = None, protocol = None):
        '''void QSslSocket.connectToHostEncrypted(str hostName, int port, str sslPeerName, QIODevice.OpenMode mode = QIODevice.ReadWrite, QAbstractSocket.NetworkLayerProtocol protocol = QAbstractSocket.AnyIPProtocol)'''


class QTcpServer(QObject):
    """"""
    def __init__(self, parent = None):
        '''void QTcpServer.__init__(QObject parent = None)'''
    acceptError = pyqtSignal() # void acceptError(QAbstractSocket::SocketError) - signal
    newConnection = pyqtSignal() # void newConnection() - signal
    def addPendingConnection(self, socket):
        '''void QTcpServer.addPendingConnection(QTcpSocket socket)'''
    def incomingConnection(self, handle):
        '''void QTcpServer.incomingConnection(sip.voidptr handle)'''
    def resumeAccepting(self):
        '''void QTcpServer.resumeAccepting()'''
    def pauseAccepting(self):
        '''void QTcpServer.pauseAccepting()'''
    def proxy(self):
        '''QNetworkProxy QTcpServer.proxy()'''
        return QNetworkProxy()
    def setProxy(self, networkProxy):
        '''void QTcpServer.setProxy(QNetworkProxy networkProxy)'''
    def errorString(self):
        '''str QTcpServer.errorString()'''
        return str()
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
        '''bool QTcpServer.setSocketDescriptor(sip.voidptr socketDescriptor)'''
        return bool()
    def socketDescriptor(self):
        '''sip.voidptr QTcpServer.socketDescriptor()'''
        return sip.voidptr()
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


