class pyqtSignal():
 def connect(self, targetSignal): pass
 def emit(self, *args): pass
from QtCore import *

class QDBusAbstractAdaptor(QObject):
    """"""
    def __init__(self, parent):
        '''void QDBusAbstractAdaptor.__init__(QObject parent)'''
    def autoRelaySignals(self):
        '''bool QDBusAbstractAdaptor.autoRelaySignals()'''
        return bool()
    def setAutoRelaySignals(self, enable):
        '''void QDBusAbstractAdaptor.setAutoRelaySignals(bool enable)'''


class QDBusAbstractInterface(QObject):
    """"""
    def __init__(self, service, path, interface, connection, parent):
        '''void QDBusAbstractInterface.__init__(QString service, QString path, str interface, QDBusConnection connection, QObject parent)'''
    def disconnectNotify(self, signal):
        '''void QDBusAbstractInterface.disconnectNotify(SIGNAL() signal)'''
    def connectNotify(self, signal):
        '''void QDBusAbstractInterface.connectNotify(SIGNAL() signal)'''
    def asyncCallWithArgumentList(self, method, args):
        '''QDBusPendingCall QDBusAbstractInterface.asyncCallWithArgumentList(QString method, list-of-QVariant args)'''
        return QDBusPendingCall()
    def asyncCall(self, method, arg1 = QVariant(), arg2 = QVariant(), arg3 = QVariant(), arg4 = QVariant(), arg5 = QVariant(), arg6 = QVariant(), arg7 = QVariant(), arg8 = QVariant()):
        '''QDBusPendingCall QDBusAbstractInterface.asyncCall(QString method, QVariant arg1 = QVariant(), QVariant arg2 = QVariant(), QVariant arg3 = QVariant(), QVariant arg4 = QVariant(), QVariant arg5 = QVariant(), QVariant arg6 = QVariant(), QVariant arg7 = QVariant(), QVariant arg8 = QVariant())'''
        return QDBusPendingCall()
    def callWithCallback(self, method, args, receiver, returnMethod, errorMethod):
        '''bool QDBusAbstractInterface.callWithCallback(QString method, list-of-QVariant args, QObject receiver, SLOT() returnMethod, SLOT() errorMethod)'''
        return bool()
    def callWithCallback(self, method, args, returnMethod, errorMethod):
        '''object QDBusAbstractInterface.callWithCallback(QString method, list-of-QVariant args, callable returnMethod, callable errorMethod)'''
        return object()
    def callWithCallback(self, method, args, receiver, slot):
        '''bool QDBusAbstractInterface.callWithCallback(QString method, list-of-QVariant args, QObject receiver, SLOT() slot)'''
        return bool()
    def callWithCallback(self, method, args, slot):
        '''object QDBusAbstractInterface.callWithCallback(QString method, list-of-QVariant args, callable slot)'''
        return object()
    def callWithArgumentList(self, mode, method, args):
        '''QDBusMessage QDBusAbstractInterface.callWithArgumentList(QDBus.CallMode mode, QString method, list-of-QVariant args)'''
        return QDBusMessage()
    def call(self, method, arg1 = QVariant(), arg2 = QVariant(), arg3 = QVariant(), arg4 = QVariant(), arg5 = QVariant(), arg6 = QVariant(), arg7 = QVariant(), arg8 = QVariant()):
        '''QDBusMessage QDBusAbstractInterface.call(QString method, QVariant arg1 = QVariant(), QVariant arg2 = QVariant(), QVariant arg3 = QVariant(), QVariant arg4 = QVariant(), QVariant arg5 = QVariant(), QVariant arg6 = QVariant(), QVariant arg7 = QVariant(), QVariant arg8 = QVariant())'''
        return QDBusMessage()
    def call(self, mode, method, arg1 = QVariant(), arg2 = QVariant(), arg3 = QVariant(), arg4 = QVariant(), arg5 = QVariant(), arg6 = QVariant(), arg7 = QVariant(), arg8 = QVariant()):
        '''QDBusMessage QDBusAbstractInterface.call(QDBus.CallMode mode, QString method, QVariant arg1 = QVariant(), QVariant arg2 = QVariant(), QVariant arg3 = QVariant(), QVariant arg4 = QVariant(), QVariant arg5 = QVariant(), QVariant arg6 = QVariant(), QVariant arg7 = QVariant(), QVariant arg8 = QVariant())'''
        return QDBusMessage()
    def timeout(self):
        '''int QDBusAbstractInterface.timeout()'''
        return int()
    def setTimeout(self, timeout):
        '''void QDBusAbstractInterface.setTimeout(int timeout)'''
    def lastError(self):
        '''QDBusError QDBusAbstractInterface.lastError()'''
        return QDBusError()
    def interface(self):
        '''QString QDBusAbstractInterface.interface()'''
        return QString()
    def path(self):
        '''QString QDBusAbstractInterface.path()'''
        return QString()
    def service(self):
        '''QString QDBusAbstractInterface.service()'''
        return QString()
    def connection(self):
        '''QDBusConnection QDBusAbstractInterface.connection()'''
        return QDBusConnection()
    def isValid(self):
        '''bool QDBusAbstractInterface.isValid()'''
        return bool()


class QDBusArgument():
    """"""
    def __init__(self):
        '''void QDBusArgument.__init__()'''
    def __init__(self, other):
        '''void QDBusArgument.__init__(QDBusArgument other)'''
    def __init__(self, arg, id = None):
        '''void QDBusArgument.__init__(object arg, int id = QMetaType.Int)'''
    def endMapEntry(self):
        '''void QDBusArgument.endMapEntry()'''
    def beginMapEntry(self):
        '''void QDBusArgument.beginMapEntry()'''
    def endMap(self):
        '''void QDBusArgument.endMap()'''
    def beginMap(self, kid, vid):
        '''void QDBusArgument.beginMap(int kid, int vid)'''
    def endArray(self):
        '''void QDBusArgument.endArray()'''
    def beginArray(self, id):
        '''void QDBusArgument.beginArray(int id)'''
    def endStructure(self):
        '''void QDBusArgument.endStructure()'''
    def beginStructure(self):
        '''void QDBusArgument.beginStructure()'''
    def add(self, arg, id = None):
        '''None QDBusArgument.add(object arg, int id = QMetaType.Int)'''
        return None()


class QDBus():
    """"""
    # Enum QDBus.CallMode
    NoBlock = 0
    Block = 0
    BlockWithGui = 0
    AutoDetect = 0



class QDBusConnection():
    """"""
    # Enum QDBusConnection.ConnectionCapability
    UnixFileDescriptorPassing = 0

    # Enum QDBusConnection.UnregisterMode
    UnregisterNode = 0
    UnregisterTree = 0

    # Enum QDBusConnection.RegisterOption
    ExportAdaptors = 0
    ExportScriptableSlots = 0
    ExportScriptableSignals = 0
    ExportScriptableProperties = 0
    ExportScriptableInvokables = 0
    ExportScriptableContents = 0
    ExportNonScriptableSlots = 0
    ExportNonScriptableSignals = 0
    ExportNonScriptableProperties = 0
    ExportNonScriptableInvokables = 0
    ExportNonScriptableContents = 0
    ExportAllSlots = 0
    ExportAllSignals = 0
    ExportAllProperties = 0
    ExportAllInvokables = 0
    ExportAllContents = 0
    ExportAllSignal = 0
    ExportChildObjects = 0

    # Enum QDBusConnection.BusType
    SessionBus = 0
    SystemBus = 0
    ActivationBus = 0

    def __init__(self, name):
        '''void QDBusConnection.__init__(QString name)'''
    def __init__(self, other):
        '''void QDBusConnection.__init__(QDBusConnection other)'''
    def sender(self):
        '''static QDBusConnection QDBusConnection.sender()'''
        return QDBusConnection()
    def systemBus(self):
        '''static QDBusConnection QDBusConnection.systemBus()'''
        return QDBusConnection()
    def sessionBus(self):
        '''static QDBusConnection QDBusConnection.sessionBus()'''
        return QDBusConnection()
    def localMachineId(self):
        '''static QByteArray QDBusConnection.localMachineId()'''
        return QByteArray()
    def disconnectFromPeer(self, name):
        '''static void QDBusConnection.disconnectFromPeer(QString name)'''
    def disconnectFromBus(self, name):
        '''static void QDBusConnection.disconnectFromBus(QString name)'''
    def connectToPeer(self, address, name):
        '''static QDBusConnection QDBusConnection.connectToPeer(QString address, QString name)'''
        return QDBusConnection()
    def connectToBus(self, type, name):
        '''static QDBusConnection QDBusConnection.connectToBus(QDBusConnection.BusType type, QString name)'''
        return QDBusConnection()
    def connectToBus(self, address, name):
        '''static QDBusConnection QDBusConnection.connectToBus(QString address, QString name)'''
        return QDBusConnection()
    def interface(self):
        '''QDBusConnectionInterface QDBusConnection.interface()'''
        return QDBusConnectionInterface()
    def unregisterService(self, serviceName):
        '''bool QDBusConnection.unregisterService(QString serviceName)'''
        return bool()
    def registerService(self, serviceName):
        '''bool QDBusConnection.registerService(QString serviceName)'''
        return bool()
    def objectRegisteredAt(self, path):
        '''QObject QDBusConnection.objectRegisteredAt(QString path)'''
        return QObject()
    def unregisterObject(self, path, mode = None):
        '''void QDBusConnection.unregisterObject(QString path, QDBusConnection.UnregisterMode mode = QDBusConnection.UnregisterNode)'''
    def registerObject(self, path, object, options = None):
        '''bool QDBusConnection.registerObject(QString path, QObject object, QDBusConnection.RegisterOptions options = QDBusConnection.ExportAdaptors)'''
        return bool()
    def disconnect(self, service, path, interface, name, receiver, slot):
        '''bool QDBusConnection.disconnect(QString service, QString path, QString interface, QString name, QObject receiver, SLOT() slot)'''
        return bool()
    def disconnect(self, service, path, interface, name, slot):
        '''object QDBusConnection.disconnect(QString service, QString path, QString interface, QString name, callable slot)'''
        return object()
    def disconnect(self, service, path, interface, name, signature, receiver, slot):
        '''bool QDBusConnection.disconnect(QString service, QString path, QString interface, QString name, QString signature, QObject receiver, SLOT() slot)'''
        return bool()
    def disconnect(self, service, path, interface, name, signature, slot):
        '''object QDBusConnection.disconnect(QString service, QString path, QString interface, QString name, QString signature, callable slot)'''
        return object()
    def disconnect(self, service, path, interface, name, argumentMatch, signature, receiver, slot):
        '''bool QDBusConnection.disconnect(QString service, QString path, QString interface, QString name, QStringList argumentMatch, QString signature, QObject receiver, SLOT() slot)'''
        return bool()
    def disconnect(self, service, path, interface, name, argumentMatch, signature, slot):
        '''object QDBusConnection.disconnect(QString service, QString path, QString interface, QString name, QStringList argumentMatch, QString signature, callable slot)'''
        return object()
    def connect(self, service, path, interface, name, receiver, slot):
        '''bool QDBusConnection.connect(QString service, QString path, QString interface, QString name, QObject receiver, SLOT() slot)'''
        return bool()
    def connect(self, service, path, interface, name, slot):
        '''object QDBusConnection.connect(QString service, QString path, QString interface, QString name, callable slot)'''
        return object()
    def connect(self, service, path, interface, name, signature, receiver, slot):
        '''bool QDBusConnection.connect(QString service, QString path, QString interface, QString name, QString signature, QObject receiver, SLOT() slot)'''
        return bool()
    def connect(self, service, path, interface, name, signature, slot):
        '''object QDBusConnection.connect(QString service, QString path, QString interface, QString name, QString signature, callable slot)'''
        return object()
    def connect(self, service, path, interface, name, argumentMatch, signature, receiver, slot):
        '''bool QDBusConnection.connect(QString service, QString path, QString interface, QString name, QStringList argumentMatch, QString signature, QObject receiver, SLOT() slot)'''
        return bool()
    def connect(self, service, path, interface, name, argumentMatch, signature, slot):
        '''object QDBusConnection.connect(QString service, QString path, QString interface, QString name, QStringList argumentMatch, QString signature, callable slot)'''
        return object()
    def asyncCall(self, message, timeout = None):
        '''QDBusPendingCall QDBusConnection.asyncCall(QDBusMessage message, int timeout = -1)'''
        return QDBusPendingCall()
    def call(self, message, mode = None, timeout = None):
        '''QDBusMessage QDBusConnection.call(QDBusMessage message, QDBus.CallMode mode = QDBus.Block, int timeout = -1)'''
        return QDBusMessage()
    def callWithCallback(self, message, receiver, returnMethod, errorMethod, timeout = None):
        '''bool QDBusConnection.callWithCallback(QDBusMessage message, QObject receiver, SLOT() returnMethod, SLOT() errorMethod, int timeout = -1)'''
        return bool()
    def callWithCallback(self, message, returnMethod, errorMethod, timeout = None):
        '''object QDBusConnection.callWithCallback(QDBusMessage message, callable returnMethod, callable errorMethod, int timeout = -1)'''
        return object()
    def callWithCallback(self, message, receiver, slot, timeout = None):
        '''bool QDBusConnection.callWithCallback(QDBusMessage message, QObject receiver, SLOT() slot, int timeout = -1)'''
        return bool()
    def callWithCallback(self, message, slot, timeout = None):
        '''object QDBusConnection.callWithCallback(QDBusMessage message, callable slot, int timeout = -1)'''
        return object()
    def send(self, message):
        '''bool QDBusConnection.send(QDBusMessage message)'''
        return bool()
    def connectionCapabilities(self):
        '''QDBusConnection.ConnectionCapabilities QDBusConnection.connectionCapabilities()'''
        return QDBusConnection.ConnectionCapabilities()
    def name(self):
        '''QString QDBusConnection.name()'''
        return QString()
    def lastError(self):
        '''QDBusError QDBusConnection.lastError()'''
        return QDBusError()
    def baseService(self):
        '''QString QDBusConnection.baseService()'''
        return QString()
    def isConnected(self):
        '''bool QDBusConnection.isConnected()'''
        return bool()
    class RegisterOptions():
        """"""
        def __init__(self):
            '''QDBusConnection.RegisterOptions QDBusConnection.RegisterOptions.__init__()'''
            return QDBusConnection.RegisterOptions()
        def __init__(self):
            '''int QDBusConnection.RegisterOptions.__init__()'''
            return int()
        def __init__(self):
            '''void QDBusConnection.RegisterOptions.__init__()'''
        def __bool__(self):
            '''int QDBusConnection.RegisterOptions.__bool__()'''
            return int()
        def __ne__(self, f):
            '''bool QDBusConnection.RegisterOptions.__ne__(QDBusConnection.RegisterOptions f)'''
            return bool()
        def __eq__(self, f):
            '''bool QDBusConnection.RegisterOptions.__eq__(QDBusConnection.RegisterOptions f)'''
            return bool()
        def __invert__(self):
            '''QDBusConnection.RegisterOptions QDBusConnection.RegisterOptions.__invert__()'''
            return QDBusConnection.RegisterOptions()
        def __and__(self, mask):
            '''QDBusConnection.RegisterOptions QDBusConnection.RegisterOptions.__and__(int mask)'''
            return QDBusConnection.RegisterOptions()
        def __xor__(self, f):
            '''QDBusConnection.RegisterOptions QDBusConnection.RegisterOptions.__xor__(QDBusConnection.RegisterOptions f)'''
            return QDBusConnection.RegisterOptions()
        def __xor__(self, f):
            '''QDBusConnection.RegisterOptions QDBusConnection.RegisterOptions.__xor__(int f)'''
            return QDBusConnection.RegisterOptions()
        def __or__(self, f):
            '''QDBusConnection.RegisterOptions QDBusConnection.RegisterOptions.__or__(QDBusConnection.RegisterOptions f)'''
            return QDBusConnection.RegisterOptions()
        def __or__(self, f):
            '''QDBusConnection.RegisterOptions QDBusConnection.RegisterOptions.__or__(int f)'''
            return QDBusConnection.RegisterOptions()
        def __int__(self):
            '''int QDBusConnection.RegisterOptions.__int__()'''
            return int()
        def __ixor__(self, f):
            '''QDBusConnection.RegisterOptions QDBusConnection.RegisterOptions.__ixor__(QDBusConnection.RegisterOptions f)'''
            return QDBusConnection.RegisterOptions()
        def __ior__(self, f):
            '''QDBusConnection.RegisterOptions QDBusConnection.RegisterOptions.__ior__(QDBusConnection.RegisterOptions f)'''
            return QDBusConnection.RegisterOptions()
        def __iand__(self, mask):
            '''QDBusConnection.RegisterOptions QDBusConnection.RegisterOptions.__iand__(int mask)'''
            return QDBusConnection.RegisterOptions()
    class ConnectionCapabilities():
        """"""
        def __init__(self):
            '''QDBusConnection.ConnectionCapabilities QDBusConnection.ConnectionCapabilities.__init__()'''
            return QDBusConnection.ConnectionCapabilities()
        def __init__(self):
            '''int QDBusConnection.ConnectionCapabilities.__init__()'''
            return int()
        def __init__(self):
            '''void QDBusConnection.ConnectionCapabilities.__init__()'''
        def __bool__(self):
            '''int QDBusConnection.ConnectionCapabilities.__bool__()'''
            return int()
        def __ne__(self, f):
            '''bool QDBusConnection.ConnectionCapabilities.__ne__(QDBusConnection.ConnectionCapabilities f)'''
            return bool()
        def __eq__(self, f):
            '''bool QDBusConnection.ConnectionCapabilities.__eq__(QDBusConnection.ConnectionCapabilities f)'''
            return bool()
        def __invert__(self):
            '''QDBusConnection.ConnectionCapabilities QDBusConnection.ConnectionCapabilities.__invert__()'''
            return QDBusConnection.ConnectionCapabilities()
        def __and__(self, mask):
            '''QDBusConnection.ConnectionCapabilities QDBusConnection.ConnectionCapabilities.__and__(int mask)'''
            return QDBusConnection.ConnectionCapabilities()
        def __xor__(self, f):
            '''QDBusConnection.ConnectionCapabilities QDBusConnection.ConnectionCapabilities.__xor__(QDBusConnection.ConnectionCapabilities f)'''
            return QDBusConnection.ConnectionCapabilities()
        def __xor__(self, f):
            '''QDBusConnection.ConnectionCapabilities QDBusConnection.ConnectionCapabilities.__xor__(int f)'''
            return QDBusConnection.ConnectionCapabilities()
        def __or__(self, f):
            '''QDBusConnection.ConnectionCapabilities QDBusConnection.ConnectionCapabilities.__or__(QDBusConnection.ConnectionCapabilities f)'''
            return QDBusConnection.ConnectionCapabilities()
        def __or__(self, f):
            '''QDBusConnection.ConnectionCapabilities QDBusConnection.ConnectionCapabilities.__or__(int f)'''
            return QDBusConnection.ConnectionCapabilities()
        def __int__(self):
            '''int QDBusConnection.ConnectionCapabilities.__int__()'''
            return int()
        def __ixor__(self, f):
            '''QDBusConnection.ConnectionCapabilities QDBusConnection.ConnectionCapabilities.__ixor__(QDBusConnection.ConnectionCapabilities f)'''
            return QDBusConnection.ConnectionCapabilities()
        def __ior__(self, f):
            '''QDBusConnection.ConnectionCapabilities QDBusConnection.ConnectionCapabilities.__ior__(QDBusConnection.ConnectionCapabilities f)'''
            return QDBusConnection.ConnectionCapabilities()
        def __iand__(self, mask):
            '''QDBusConnection.ConnectionCapabilities QDBusConnection.ConnectionCapabilities.__iand__(int mask)'''
            return QDBusConnection.ConnectionCapabilities()


class QDBusConnectionInterface(QDBusAbstractInterface):
    """"""
    # Enum QDBusConnectionInterface.RegisterServiceReply
    ServiceNotRegistered = 0
    ServiceRegistered = 0
    ServiceQueued = 0

    # Enum QDBusConnectionInterface.ServiceReplacementOptions
    DontAllowReplacement = 0
    AllowReplacement = 0

    # Enum QDBusConnectionInterface.ServiceQueueOptions
    DontQueueService = 0
    QueueService = 0
    ReplaceExistingService = 0

    def disconnectNotify(self):
        '''SIGNAL() QDBusConnectionInterface.disconnectNotify()'''
        return SIGNAL()()
    def connectNotify(self):
        '''SIGNAL() QDBusConnectionInterface.connectNotify()'''
        return SIGNAL()()
    callWithCallbackFailed = pyqtSignal() # void callWithCallbackFailed(const QDBusErroramp;,const QDBusMessageamp;) - signal
    serviceOwnerChanged = pyqtSignal() # void serviceOwnerChanged(const QStringamp;,const QStringamp;,const QStringamp;) - signal
    serviceUnregistered = pyqtSignal() # void serviceUnregistered(const QStringamp;) - signal
    serviceRegistered = pyqtSignal() # void serviceRegistered(const QStringamp;) - signal
    def startService(self, name):
        '''QDBusReply QDBusConnectionInterface.startService(QString name)'''
        return QDBusReply()
    def serviceUid(self, serviceName):
        '''QDBusReply QDBusConnectionInterface.serviceUid(QString serviceName)'''
        return QDBusReply()
    def servicePid(self, serviceName):
        '''QDBusReply QDBusConnectionInterface.servicePid(QString serviceName)'''
        return QDBusReply()
    def registerService(self, serviceName, qoption = None, roption = None):
        '''QDBusReply QDBusConnectionInterface.registerService(QString serviceName, QDBusConnectionInterface.ServiceQueueOptions qoption = QDBusConnectionInterface.DontQueueService, QDBusConnectionInterface.ServiceReplacementOptions roption = QDBusConnectionInterface.DontAllowReplacement)'''
        return QDBusReply()
    def unregisterService(self, serviceName):
        '''QDBusReply QDBusConnectionInterface.unregisterService(QString serviceName)'''
        return QDBusReply()
    def serviceOwner(self, name):
        '''QDBusReply QDBusConnectionInterface.serviceOwner(QString name)'''
        return QDBusReply()
    def isServiceRegistered(self, serviceName):
        '''QDBusReply QDBusConnectionInterface.isServiceRegistered(QString serviceName)'''
        return QDBusReply()
    def registeredServiceNames(self):
        '''QDBusReply QDBusConnectionInterface.registeredServiceNames()'''
        return QDBusReply()


class QDBusError():
    """"""
    # Enum QDBusError.ErrorType
    NoError = 0
    Other = 0
    Failed = 0
    NoMemory = 0
    ServiceUnknown = 0
    NoReply = 0
    BadAddress = 0
    NotSupported = 0
    LimitsExceeded = 0
    AccessDenied = 0
    NoServer = 0
    Timeout = 0
    NoNetwork = 0
    AddressInUse = 0
    Disconnected = 0
    InvalidArgs = 0
    UnknownMethod = 0
    TimedOut = 0
    InvalidSignature = 0
    UnknownInterface = 0
    InternalError = 0
    UnknownObject = 0
    InvalidService = 0
    InvalidObjectPath = 0
    InvalidInterface = 0
    InvalidMember = 0

    def __init__(self, other):
        '''void QDBusError.__init__(QDBusError other)'''
    def errorString(self, error):
        '''static QString QDBusError.errorString(QDBusError.ErrorType error)'''
        return QString()
    def isValid(self):
        '''bool QDBusError.isValid()'''
        return bool()
    def message(self):
        '''QString QDBusError.message()'''
        return QString()
    def name(self):
        '''QString QDBusError.name()'''
        return QString()
    def type(self):
        '''QDBusError.ErrorType QDBusError.type()'''
        return QDBusError.ErrorType()


class QDBusObjectPath():
    """"""
    def __init__(self):
        '''void QDBusObjectPath.__init__()'''
    def __init__(self, path):
        '''void QDBusObjectPath.__init__(QString path)'''
    def __init__(self):
        '''QDBusObjectPath QDBusObjectPath.__init__()'''
        return QDBusObjectPath()
    def __ge__(self, rhs):
        '''bool QDBusObjectPath.__ge__(QDBusObjectPath rhs)'''
        return bool()
    def __eq__(self, rhs):
        '''bool QDBusObjectPath.__eq__(QDBusObjectPath rhs)'''
        return bool()
    def __ne__(self, rhs):
        '''bool QDBusObjectPath.__ne__(QDBusObjectPath rhs)'''
        return bool()
    def __lt__(self, rhs):
        '''bool QDBusObjectPath.__lt__(QDBusObjectPath rhs)'''
        return bool()
    def __hash__(self):
        '''int QDBusObjectPath.__hash__()'''
        return int()
    def setPath(self, path):
        '''void QDBusObjectPath.setPath(QString path)'''
    def path(self):
        '''QString QDBusObjectPath.path()'''
        return QString()


class QDBusSignature():
    """"""
    def __init__(self):
        '''void QDBusSignature.__init__()'''
    def __init__(self, signature):
        '''void QDBusSignature.__init__(QString signature)'''
    def __init__(self):
        '''QDBusSignature QDBusSignature.__init__()'''
        return QDBusSignature()
    def __ge__(self, rhs):
        '''bool QDBusSignature.__ge__(QDBusSignature rhs)'''
        return bool()
    def __eq__(self, rhs):
        '''bool QDBusSignature.__eq__(QDBusSignature rhs)'''
        return bool()
    def __ne__(self, rhs):
        '''bool QDBusSignature.__ne__(QDBusSignature rhs)'''
        return bool()
    def __lt__(self, rhs):
        '''bool QDBusSignature.__lt__(QDBusSignature rhs)'''
        return bool()
    def __hash__(self):
        '''int QDBusSignature.__hash__()'''
        return int()
    def setSignature(self, signature):
        '''void QDBusSignature.setSignature(QString signature)'''
    def signature(self):
        '''QString QDBusSignature.signature()'''
        return QString()


class QDBusVariant():
    """"""
    def __init__(self):
        '''void QDBusVariant.__init__()'''
    def __init__(self, variant):
        '''void QDBusVariant.__init__(QVariant variant)'''
    def __init__(self):
        '''QDBusVariant QDBusVariant.__init__()'''
        return QDBusVariant()
    def __ne__(self, v2):
        '''bool QDBusVariant.__ne__(QDBusVariant v2)'''
        return bool()
    def __eq__(self, v2):
        '''bool QDBusVariant.__eq__(QDBusVariant v2)'''
        return bool()
    def setVariant(self, variant):
        '''void QDBusVariant.setVariant(QVariant variant)'''
    def variant(self):
        '''QVariant QDBusVariant.variant()'''
        return QVariant()


class QDBusInterface(QDBusAbstractInterface):
    """"""
    def __init__(self, service, path, interface = QString(), connection = None, parent = None):
        '''void QDBusInterface.__init__(QString service, QString path, QString interface = QString(), QDBusConnection connection = QDBusConnection.sessionBus(), QObject parent = None)'''


class QDBusMessage():
    """"""
    # Enum QDBusMessage.MessageType
    InvalidMessage = 0
    MethodCallMessage = 0
    ReplyMessage = 0
    ErrorMessage = 0
    SignalMessage = 0

    def __init__(self):
        '''void QDBusMessage.__init__()'''
    def __init__(self, other):
        '''void QDBusMessage.__init__(QDBusMessage other)'''
    def __lshift__(self, arg):
        '''QDBusMessage QDBusMessage.__lshift__(QVariant arg)'''
        return QDBusMessage()
    def arguments(self):
        '''list-of-QVariant QDBusMessage.arguments()'''
        return [QVariant()]
    def setArguments(self, arguments):
        '''void QDBusMessage.setArguments(list-of-QVariant arguments)'''
    def autoStartService(self):
        '''bool QDBusMessage.autoStartService()'''
        return bool()
    def setAutoStartService(self, enable):
        '''void QDBusMessage.setAutoStartService(bool enable)'''
    def isDelayedReply(self):
        '''bool QDBusMessage.isDelayedReply()'''
        return bool()
    def setDelayedReply(self, enable):
        '''void QDBusMessage.setDelayedReply(bool enable)'''
    def isReplyRequired(self):
        '''bool QDBusMessage.isReplyRequired()'''
        return bool()
    def signature(self):
        '''QString QDBusMessage.signature()'''
        return QString()
    def type(self):
        '''QDBusMessage.MessageType QDBusMessage.type()'''
        return QDBusMessage.MessageType()
    def errorMessage(self):
        '''QString QDBusMessage.errorMessage()'''
        return QString()
    def errorName(self):
        '''QString QDBusMessage.errorName()'''
        return QString()
    def member(self):
        '''QString QDBusMessage.member()'''
        return QString()
    def interface(self):
        '''QString QDBusMessage.interface()'''
        return QString()
    def path(self):
        '''QString QDBusMessage.path()'''
        return QString()
    def service(self):
        '''QString QDBusMessage.service()'''
        return QString()
    def createErrorReply(self, name, msg):
        '''QDBusMessage QDBusMessage.createErrorReply(QString name, QString msg)'''
        return QDBusMessage()
    def createErrorReply(self, error):
        '''QDBusMessage QDBusMessage.createErrorReply(QDBusError error)'''
        return QDBusMessage()
    def createErrorReply(self, type, msg):
        '''QDBusMessage QDBusMessage.createErrorReply(QDBusError.ErrorType type, QString msg)'''
        return QDBusMessage()
    def createReply(self, arguments = None):
        '''QDBusMessage QDBusMessage.createReply(list-of-QVariant arguments = QListlt;QVariantgt;())'''
        return QDBusMessage()
    def createReply(self, argument):
        '''QDBusMessage QDBusMessage.createReply(QVariant argument)'''
        return QDBusMessage()
    def createError(self, name, msg):
        '''static QDBusMessage QDBusMessage.createError(QString name, QString msg)'''
        return QDBusMessage()
    def createError(self, error):
        '''static QDBusMessage QDBusMessage.createError(QDBusError error)'''
        return QDBusMessage()
    def createError(self, type, msg):
        '''static QDBusMessage QDBusMessage.createError(QDBusError.ErrorType type, QString msg)'''
        return QDBusMessage()
    def createMethodCall(self, service, path, interface, method):
        '''static QDBusMessage QDBusMessage.createMethodCall(QString service, QString path, QString interface, QString method)'''
        return QDBusMessage()
    def createSignal(self, path, interface, name):
        '''static QDBusMessage QDBusMessage.createSignal(QString path, QString interface, QString name)'''
        return QDBusMessage()


class QDBusPendingCall():
    """"""
    def __init__(self, other):
        '''void QDBusPendingCall.__init__(QDBusPendingCall other)'''
    def fromCompletedCall(self, message):
        '''static QDBusPendingCall QDBusPendingCall.fromCompletedCall(QDBusMessage message)'''
        return QDBusPendingCall()
    def fromError(self, error):
        '''static QDBusPendingCall QDBusPendingCall.fromError(QDBusError error)'''
        return QDBusPendingCall()


class QDBusPendingCallWatcher(QObject, QDBusPendingCall):
    """"""
    def __init__(self, call, parent = None):
        '''void QDBusPendingCallWatcher.__init__(QDBusPendingCall call, QObject parent = None)'''
    finished = pyqtSignal() # void finished(QDBusPendingCallWatcher *) - signal
    def waitForFinished(self):
        '''void QDBusPendingCallWatcher.waitForFinished()'''
    def isFinished(self):
        '''bool QDBusPendingCallWatcher.isFinished()'''
        return bool()


class QDBusServiceWatcher(QObject):
    """"""
    # Enum QDBusServiceWatcher.WatchModeFlag
    WatchForRegistration = 0
    WatchForUnregistration = 0
    WatchForOwnerChange = 0

    def __init__(self, parent = None):
        '''void QDBusServiceWatcher.__init__(QObject parent = None)'''
    def __init__(self, service, connection, watchMode = None, parent = None):
        '''void QDBusServiceWatcher.__init__(QString service, QDBusConnection connection, QDBusServiceWatcher.WatchMode watchMode = QDBusServiceWatcher.WatchForOwnerChange, QObject parent = None)'''
    serviceOwnerChanged = pyqtSignal() # void serviceOwnerChanged(const QStringamp;,const QStringamp;,const QStringamp;) - signal
    serviceUnregistered = pyqtSignal() # void serviceUnregistered(const QStringamp;) - signal
    serviceRegistered = pyqtSignal() # void serviceRegistered(const QStringamp;) - signal
    def setConnection(self, connection):
        '''void QDBusServiceWatcher.setConnection(QDBusConnection connection)'''
    def connection(self):
        '''QDBusConnection QDBusServiceWatcher.connection()'''
        return QDBusConnection()
    def setWatchMode(self, mode):
        '''void QDBusServiceWatcher.setWatchMode(QDBusServiceWatcher.WatchMode mode)'''
    def watchMode(self):
        '''QDBusServiceWatcher.WatchMode QDBusServiceWatcher.watchMode()'''
        return QDBusServiceWatcher.WatchMode()
    def removeWatchedService(self, service):
        '''bool QDBusServiceWatcher.removeWatchedService(QString service)'''
        return bool()
    def addWatchedService(self, newService):
        '''void QDBusServiceWatcher.addWatchedService(QString newService)'''
    def setWatchedServices(self, services):
        '''void QDBusServiceWatcher.setWatchedServices(QStringList services)'''
    def watchedServices(self):
        '''QStringList QDBusServiceWatcher.watchedServices()'''
        return QStringList()
    class WatchMode():
        """"""
        def __init__(self):
            '''QDBusServiceWatcher.WatchMode QDBusServiceWatcher.WatchMode.__init__()'''
            return QDBusServiceWatcher.WatchMode()
        def __init__(self):
            '''int QDBusServiceWatcher.WatchMode.__init__()'''
            return int()
        def __init__(self):
            '''void QDBusServiceWatcher.WatchMode.__init__()'''
        def __bool__(self):
            '''int QDBusServiceWatcher.WatchMode.__bool__()'''
            return int()
        def __ne__(self, f):
            '''bool QDBusServiceWatcher.WatchMode.__ne__(QDBusServiceWatcher.WatchMode f)'''
            return bool()
        def __eq__(self, f):
            '''bool QDBusServiceWatcher.WatchMode.__eq__(QDBusServiceWatcher.WatchMode f)'''
            return bool()
        def __invert__(self):
            '''QDBusServiceWatcher.WatchMode QDBusServiceWatcher.WatchMode.__invert__()'''
            return QDBusServiceWatcher.WatchMode()
        def __and__(self, mask):
            '''QDBusServiceWatcher.WatchMode QDBusServiceWatcher.WatchMode.__and__(int mask)'''
            return QDBusServiceWatcher.WatchMode()
        def __xor__(self, f):
            '''QDBusServiceWatcher.WatchMode QDBusServiceWatcher.WatchMode.__xor__(QDBusServiceWatcher.WatchMode f)'''
            return QDBusServiceWatcher.WatchMode()
        def __xor__(self, f):
            '''QDBusServiceWatcher.WatchMode QDBusServiceWatcher.WatchMode.__xor__(int f)'''
            return QDBusServiceWatcher.WatchMode()
        def __or__(self, f):
            '''QDBusServiceWatcher.WatchMode QDBusServiceWatcher.WatchMode.__or__(QDBusServiceWatcher.WatchMode f)'''
            return QDBusServiceWatcher.WatchMode()
        def __or__(self, f):
            '''QDBusServiceWatcher.WatchMode QDBusServiceWatcher.WatchMode.__or__(int f)'''
            return QDBusServiceWatcher.WatchMode()
        def __int__(self):
            '''int QDBusServiceWatcher.WatchMode.__int__()'''
            return int()
        def __ixor__(self, f):
            '''QDBusServiceWatcher.WatchMode QDBusServiceWatcher.WatchMode.__ixor__(QDBusServiceWatcher.WatchMode f)'''
            return QDBusServiceWatcher.WatchMode()
        def __ior__(self, f):
            '''QDBusServiceWatcher.WatchMode QDBusServiceWatcher.WatchMode.__ior__(QDBusServiceWatcher.WatchMode f)'''
            return QDBusServiceWatcher.WatchMode()
        def __iand__(self, mask):
            '''QDBusServiceWatcher.WatchMode QDBusServiceWatcher.WatchMode.__iand__(int mask)'''
            return QDBusServiceWatcher.WatchMode()


class QDBusUnixFileDescriptor():
    """"""
    def __init__(self):
        '''void QDBusUnixFileDescriptor.__init__()'''
    def __init__(self, fileDescriptor):
        '''void QDBusUnixFileDescriptor.__init__(int fileDescriptor)'''
    def __init__(self, other):
        '''void QDBusUnixFileDescriptor.__init__(QDBusUnixFileDescriptor other)'''
    def isSupported(self):
        '''static bool QDBusUnixFileDescriptor.isSupported()'''
        return bool()
    def setFileDescriptor(self, fileDescriptor):
        '''void QDBusUnixFileDescriptor.setFileDescriptor(int fileDescriptor)'''
    def fileDescriptor(self):
        '''int QDBusUnixFileDescriptor.fileDescriptor()'''
        return int()
    def isValid(self):
        '''bool QDBusUnixFileDescriptor.isValid()'''
        return bool()


class QDBusPendingReply(QDBusPendingCall):
    """"""
    def __init__(self):
        '''void QDBusPendingReply.__init__()'''
    def __init__(self, other):
        '''void QDBusPendingReply.__init__(QDBusPendingReply other)'''
    def __init__(self, call):
        '''void QDBusPendingReply.__init__(QDBusPendingCall call)'''
    def __init__(self, reply):
        '''void QDBusPendingReply.__init__(QDBusMessage reply)'''
    def value(self, type = None):
        '''object QDBusPendingReply.value(object type = None)'''
        return object()
    def waitForFinished(self):
        '''void QDBusPendingReply.waitForFinished()'''
    def reply(self):
        '''QDBusMessage QDBusPendingReply.reply()'''
        return QDBusMessage()
    def isValid(self):
        '''bool QDBusPendingReply.isValid()'''
        return bool()
    def isFinished(self):
        '''bool QDBusPendingReply.isFinished()'''
        return bool()
    def isError(self):
        '''bool QDBusPendingReply.isError()'''
        return bool()
    def error(self):
        '''QDBusError QDBusPendingReply.error()'''
        return QDBusError()
    def argumentAt(self, index):
        '''QVariant QDBusPendingReply.argumentAt(int index)'''
        return QVariant()


class QDBusReply():
    """"""
    def __init__(self, reply):
        '''void QDBusReply.__init__(QDBusMessage reply)'''
    def __init__(self, call):
        '''void QDBusReply.__init__(QDBusPendingCall call)'''
    def __init__(self, error):
        '''void QDBusReply.__init__(QDBusError error)'''
    def __init__(self, other):
        '''void QDBusReply.__init__(QDBusReply other)'''
    def value(self, type = None):
        '''object QDBusReply.value(object type = None)'''
        return object()
    def isValid(self):
        '''bool QDBusReply.isValid()'''
        return bool()
    def error(self):
        '''QDBusError QDBusReply.error()'''
        return QDBusError()


