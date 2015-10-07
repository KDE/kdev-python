class pyqtSignal():
 def connect(self, targetSignal): pass
 def emit(self, *args): pass
from QtCore import *

from QtWidgets import *

import datetime

class QNdefFilter():
    """"""
    def __init__(self):
        '''void QNdefFilter.__init__()'''
    def __init__(self, other):
        '''void QNdefFilter.__init__(QNdefFilter other)'''
    def recordAt(self, i):
        '''QNdefFilter.Record QNdefFilter.recordAt(int i)'''
        return QNdefFilter.Record()
    def __len__(self):
        ''' QNdefFilter.__len__()'''
        return ()
    def recordCount(self):
        '''int QNdefFilter.recordCount()'''
        return int()
    def appendRecord(self, typeNameFormat, type, min = 1, max = 1):
        '''void QNdefFilter.appendRecord(QNdefRecord.TypeNameFormat typeNameFormat, QByteArray type, int min = 1, int max = 1)'''
    def appendRecord(self, record):
        '''void QNdefFilter.appendRecord(QNdefFilter.Record record)'''
    def orderMatch(self):
        '''bool QNdefFilter.orderMatch()'''
        return bool()
    def setOrderMatch(self, on):
        '''void QNdefFilter.setOrderMatch(bool on)'''
    def clear(self):
        '''void QNdefFilter.clear()'''
    class Record():
        """"""
        maximum = None # int - member
        minimum = None # int - member
        type = None # QByteArray - member
        typeNameFormat = None # QNdefRecord.TypeNameFormat - member
        def __init__(self):
            '''void QNdefFilter.Record.__init__()'''
        def __init__(self):
            '''QNdefFilter.Record QNdefFilter.Record.__init__()'''
            return QNdefFilter.Record()


class QNdefMessage():
    """"""
    def __init__(self):
        '''void QNdefMessage.__init__()'''
    def __init__(self, record):
        '''void QNdefMessage.__init__(QNdefRecord record)'''
    def __init__(self, message):
        '''void QNdefMessage.__init__(QNdefMessage message)'''
    def __init__(self, records):
        '''void QNdefMessage.__init__(list-of-QNdefRecord records)'''
    def __ne__(self, other):
        '''bool QNdefMessage.__ne__(QNdefMessage other)'''
        return bool()
    def fromByteArray(self, message):
        '''static QNdefMessage QNdefMessage.fromByteArray(QByteArray message)'''
        return QNdefMessage()
    def __delitem__(self, i):
        '''void QNdefMessage.__delitem__(int i)'''
    def __setitem__(self, i, value):
        '''void QNdefMessage.__setitem__(int i, QNdefRecord value)'''
    def __getitem__(self, i):
        '''QNdefRecord QNdefMessage.__getitem__(int i)'''
        return QNdefRecord()
    def __len__(self):
        '''int QNdefMessage.__len__()'''
        return int()
    def toByteArray(self):
        '''QByteArray QNdefMessage.toByteArray()'''
        return QByteArray()
    def __eq__(self, other):
        '''bool QNdefMessage.__eq__(QNdefMessage other)'''
        return bool()


class QNdefRecord():
    """"""
    # Enum QNdefRecord.TypeNameFormat
    Empty = 0
    NfcRtd = 0
    Mime = 0
    Uri = 0
    ExternalRtd = 0
    Unknown = 0

    def __init__(self):
        '''void QNdefRecord.__init__()'''
    def __init__(self, other):
        '''void QNdefRecord.__init__(QNdefRecord other)'''
    def __hash__(self):
        '''int QNdefRecord.__hash__()'''
        return int()
    def __ne__(self, other):
        '''bool QNdefRecord.__ne__(QNdefRecord other)'''
        return bool()
    def __eq__(self, other):
        '''bool QNdefRecord.__eq__(QNdefRecord other)'''
        return bool()
    def isEmpty(self):
        '''bool QNdefRecord.isEmpty()'''
        return bool()
    def payload(self):
        '''QByteArray QNdefRecord.payload()'''
        return QByteArray()
    def setPayload(self, payload):
        '''void QNdefRecord.setPayload(QByteArray payload)'''
    def id(self):
        '''QByteArray QNdefRecord.id()'''
        return QByteArray()
    def setId(self, id):
        '''void QNdefRecord.setId(QByteArray id)'''
    def type(self):
        '''QByteArray QNdefRecord.type()'''
        return QByteArray()
    def setType(self, type):
        '''void QNdefRecord.setType(QByteArray type)'''
    def typeNameFormat(self):
        '''QNdefRecord.TypeNameFormat QNdefRecord.typeNameFormat()'''
        return QNdefRecord.TypeNameFormat()
    def setTypeNameFormat(self, typeNameFormat):
        '''void QNdefRecord.setTypeNameFormat(QNdefRecord.TypeNameFormat typeNameFormat)'''


class QNdefNfcIconRecord(QNdefRecord):
    """"""
    def __init__(self):
        '''void QNdefNfcIconRecord.__init__()'''
    def __init__(self, other):
        '''void QNdefNfcIconRecord.__init__(QNdefRecord other)'''
    def __init__(self):
        '''QNdefNfcIconRecord QNdefNfcIconRecord.__init__()'''
        return QNdefNfcIconRecord()
    def data(self):
        '''QByteArray QNdefNfcIconRecord.data()'''
        return QByteArray()
    def setData(self, data):
        '''void QNdefNfcIconRecord.setData(QByteArray data)'''


class QNdefNfcSmartPosterRecord(QNdefRecord):
    """"""
    # Enum QNdefNfcSmartPosterRecord.Action
    UnspecifiedAction = 0
    DoAction = 0
    SaveAction = 0
    EditAction = 0

    def __init__(self):
        '''void QNdefNfcSmartPosterRecord.__init__()'''
    def __init__(self, other):
        '''void QNdefNfcSmartPosterRecord.__init__(QNdefNfcSmartPosterRecord other)'''
    def __init__(self, other):
        '''void QNdefNfcSmartPosterRecord.__init__(QNdefRecord other)'''
    def setTypeInfo(self, type):
        '''void QNdefNfcSmartPosterRecord.setTypeInfo(QByteArray type)'''
    def typeInfo(self):
        '''QByteArray QNdefNfcSmartPosterRecord.typeInfo()'''
        return QByteArray()
    def setSize(self, size):
        '''void QNdefNfcSmartPosterRecord.setSize(int size)'''
    def size(self):
        '''int QNdefNfcSmartPosterRecord.size()'''
        return int()
    def setIcons(self, icons):
        '''void QNdefNfcSmartPosterRecord.setIcons(list-of-QNdefNfcIconRecord icons)'''
    def removeIcon(self, icon):
        '''bool QNdefNfcSmartPosterRecord.removeIcon(QNdefNfcIconRecord icon)'''
        return bool()
    def removeIcon(self, type):
        '''bool QNdefNfcSmartPosterRecord.removeIcon(QByteArray type)'''
        return bool()
    def addIcon(self, icon):
        '''void QNdefNfcSmartPosterRecord.addIcon(QNdefNfcIconRecord icon)'''
    def addIcon(self, type, data):
        '''void QNdefNfcSmartPosterRecord.addIcon(QByteArray type, QByteArray data)'''
    def iconRecords(self):
        '''list-of-QNdefNfcIconRecord QNdefNfcSmartPosterRecord.iconRecords()'''
        return [QNdefNfcIconRecord()]
    def iconRecord(self, index):
        '''QNdefNfcIconRecord QNdefNfcSmartPosterRecord.iconRecord(int index)'''
        return QNdefNfcIconRecord()
    def icon(self, mimetype = QByteArray()):
        '''QByteArray QNdefNfcSmartPosterRecord.icon(QByteArray mimetype = QByteArray())'''
        return QByteArray()
    def iconCount(self):
        '''int QNdefNfcSmartPosterRecord.iconCount()'''
        return int()
    def setAction(self, act):
        '''void QNdefNfcSmartPosterRecord.setAction(QNdefNfcSmartPosterRecord.Action act)'''
    def action(self):
        '''QNdefNfcSmartPosterRecord.Action QNdefNfcSmartPosterRecord.action()'''
        return QNdefNfcSmartPosterRecord.Action()
    def setUri(self, url):
        '''void QNdefNfcSmartPosterRecord.setUri(QNdefNfcUriRecord url)'''
    def setUri(self, url):
        '''void QNdefNfcSmartPosterRecord.setUri(QUrl url)'''
    def uriRecord(self):
        '''QNdefNfcUriRecord QNdefNfcSmartPosterRecord.uriRecord()'''
        return QNdefNfcUriRecord()
    def uri(self):
        '''QUrl QNdefNfcSmartPosterRecord.uri()'''
        return QUrl()
    def setTitles(self, titles):
        '''void QNdefNfcSmartPosterRecord.setTitles(list-of-QNdefNfcTextRecord titles)'''
    def removeTitle(self, text):
        '''bool QNdefNfcSmartPosterRecord.removeTitle(QNdefNfcTextRecord text)'''
        return bool()
    def removeTitle(self, locale):
        '''bool QNdefNfcSmartPosterRecord.removeTitle(str locale)'''
        return bool()
    def addTitle(self, text):
        '''bool QNdefNfcSmartPosterRecord.addTitle(QNdefNfcTextRecord text)'''
        return bool()
    def addTitle(self, text, locale, encoding):
        '''bool QNdefNfcSmartPosterRecord.addTitle(str text, str locale, QNdefNfcTextRecord.Encoding encoding)'''
        return bool()
    def titleRecords(self):
        '''list-of-QNdefNfcTextRecord QNdefNfcSmartPosterRecord.titleRecords()'''
        return [QNdefNfcTextRecord()]
    def titleRecord(self, index):
        '''QNdefNfcTextRecord QNdefNfcSmartPosterRecord.titleRecord(int index)'''
        return QNdefNfcTextRecord()
    def title(self, locale = str()):
        '''str QNdefNfcSmartPosterRecord.title(str locale = str())'''
        return str()
    def titleCount(self):
        '''int QNdefNfcSmartPosterRecord.titleCount()'''
        return int()
    def hasTypeInfo(self):
        '''bool QNdefNfcSmartPosterRecord.hasTypeInfo()'''
        return bool()
    def hasSize(self):
        '''bool QNdefNfcSmartPosterRecord.hasSize()'''
        return bool()
    def hasIcon(self, mimetype = QByteArray()):
        '''bool QNdefNfcSmartPosterRecord.hasIcon(QByteArray mimetype = QByteArray())'''
        return bool()
    def hasAction(self):
        '''bool QNdefNfcSmartPosterRecord.hasAction()'''
        return bool()
    def hasTitle(self, locale = str()):
        '''bool QNdefNfcSmartPosterRecord.hasTitle(str locale = str())'''
        return bool()
    def setPayload(self, payload):
        '''void QNdefNfcSmartPosterRecord.setPayload(QByteArray payload)'''


class QNdefNfcTextRecord(QNdefRecord):
    """"""
    # Enum QNdefNfcTextRecord.Encoding
    Utf8 = 0
    Utf16 = 0

    def __init__(self):
        '''void QNdefNfcTextRecord.__init__()'''
    def __init__(self, other):
        '''void QNdefNfcTextRecord.__init__(QNdefRecord other)'''
    def __init__(self):
        '''QNdefNfcTextRecord QNdefNfcTextRecord.__init__()'''
        return QNdefNfcTextRecord()
    def setEncoding(self, encoding):
        '''void QNdefNfcTextRecord.setEncoding(QNdefNfcTextRecord.Encoding encoding)'''
    def encoding(self):
        '''QNdefNfcTextRecord.Encoding QNdefNfcTextRecord.encoding()'''
        return QNdefNfcTextRecord.Encoding()
    def setText(self, text):
        '''void QNdefNfcTextRecord.setText(str text)'''
    def text(self):
        '''str QNdefNfcTextRecord.text()'''
        return str()
    def setLocale(self, locale):
        '''void QNdefNfcTextRecord.setLocale(str locale)'''
    def locale(self):
        '''str QNdefNfcTextRecord.locale()'''
        return str()


class QNdefNfcUriRecord(QNdefRecord):
    """"""
    def __init__(self):
        '''void QNdefNfcUriRecord.__init__()'''
    def __init__(self, other):
        '''void QNdefNfcUriRecord.__init__(QNdefRecord other)'''
    def __init__(self):
        '''QNdefNfcUriRecord QNdefNfcUriRecord.__init__()'''
        return QNdefNfcUriRecord()
    def setUri(self, uri):
        '''void QNdefNfcUriRecord.setUri(QUrl uri)'''
    def uri(self):
        '''QUrl QNdefNfcUriRecord.uri()'''
        return QUrl()


class QNearFieldManager(QObject):
    """"""
    # Enum QNearFieldManager.TargetAccessMode
    NoTargetAccess = 0
    NdefReadTargetAccess = 0
    NdefWriteTargetAccess = 0
    TagTypeSpecificTargetAccess = 0

    def __init__(self, parent = None):
        '''void QNearFieldManager.__init__(QObject parent = None)'''
    targetLost = pyqtSignal() # void targetLost(QNearFieldTarget*) - signal
    targetDetected = pyqtSignal() # void targetDetected(QNearFieldTarget*) - signal
    def unregisterNdefMessageHandler(self, handlerId):
        '''bool QNearFieldManager.unregisterNdefMessageHandler(int handlerId)'''
        return bool()
    def registerNdefMessageHandler(self, slot):
        '''int QNearFieldManager.registerNdefMessageHandler(slot slot)'''
        return int()
    def registerNdefMessageHandler(self, typeNameFormat, type, slot):
        '''int QNearFieldManager.registerNdefMessageHandler(QNdefRecord.TypeNameFormat typeNameFormat, QByteArray type, slot slot)'''
        return int()
    def registerNdefMessageHandler(self, filter, slot):
        '''int QNearFieldManager.registerNdefMessageHandler(QNdefFilter filter, slot slot)'''
        return int()
    def stopTargetDetection(self):
        '''void QNearFieldManager.stopTargetDetection()'''
    def startTargetDetection(self):
        '''bool QNearFieldManager.startTargetDetection()'''
        return bool()
    def targetAccessModes(self):
        '''QNearFieldManager.TargetAccessModes QNearFieldManager.targetAccessModes()'''
        return QNearFieldManager.TargetAccessModes()
    def setTargetAccessModes(self, accessModes):
        '''void QNearFieldManager.setTargetAccessModes(QNearFieldManager.TargetAccessModes accessModes)'''
    def isAvailable(self):
        '''bool QNearFieldManager.isAvailable()'''
        return bool()
    class TargetAccessModes():
        """"""
        def __init__(self):
            '''QNearFieldManager.TargetAccessModes QNearFieldManager.TargetAccessModes.__init__()'''
            return QNearFieldManager.TargetAccessModes()
        def __init__(self):
            '''int QNearFieldManager.TargetAccessModes.__init__()'''
            return int()
        def __init__(self):
            '''void QNearFieldManager.TargetAccessModes.__init__()'''
        def __bool__(self):
            '''int QNearFieldManager.TargetAccessModes.__bool__()'''
            return int()
        def __ne__(self, f):
            '''bool QNearFieldManager.TargetAccessModes.__ne__(QNearFieldManager.TargetAccessModes f)'''
            return bool()
        def __eq__(self, f):
            '''bool QNearFieldManager.TargetAccessModes.__eq__(QNearFieldManager.TargetAccessModes f)'''
            return bool()
        def __invert__(self):
            '''QNearFieldManager.TargetAccessModes QNearFieldManager.TargetAccessModes.__invert__()'''
            return QNearFieldManager.TargetAccessModes()
        def __and__(self, mask):
            '''QNearFieldManager.TargetAccessModes QNearFieldManager.TargetAccessModes.__and__(int mask)'''
            return QNearFieldManager.TargetAccessModes()
        def __xor__(self, f):
            '''QNearFieldManager.TargetAccessModes QNearFieldManager.TargetAccessModes.__xor__(QNearFieldManager.TargetAccessModes f)'''
            return QNearFieldManager.TargetAccessModes()
        def __xor__(self, f):
            '''QNearFieldManager.TargetAccessModes QNearFieldManager.TargetAccessModes.__xor__(int f)'''
            return QNearFieldManager.TargetAccessModes()
        def __or__(self, f):
            '''QNearFieldManager.TargetAccessModes QNearFieldManager.TargetAccessModes.__or__(QNearFieldManager.TargetAccessModes f)'''
            return QNearFieldManager.TargetAccessModes()
        def __or__(self, f):
            '''QNearFieldManager.TargetAccessModes QNearFieldManager.TargetAccessModes.__or__(int f)'''
            return QNearFieldManager.TargetAccessModes()
        def __int__(self):
            '''int QNearFieldManager.TargetAccessModes.__int__()'''
            return int()
        def __ixor__(self, f):
            '''QNearFieldManager.TargetAccessModes QNearFieldManager.TargetAccessModes.__ixor__(QNearFieldManager.TargetAccessModes f)'''
            return QNearFieldManager.TargetAccessModes()
        def __ior__(self, f):
            '''QNearFieldManager.TargetAccessModes QNearFieldManager.TargetAccessModes.__ior__(QNearFieldManager.TargetAccessModes f)'''
            return QNearFieldManager.TargetAccessModes()
        def __iand__(self, mask):
            '''QNearFieldManager.TargetAccessModes QNearFieldManager.TargetAccessModes.__iand__(int mask)'''
            return QNearFieldManager.TargetAccessModes()


class QNearFieldShareManager(QObject):
    """"""
    # Enum QNearFieldShareManager.ShareMode
    NoShare = 0
    NdefShare = 0
    FileShare = 0

    # Enum QNearFieldShareManager.ShareError
    NoError = 0
    UnknownError = 0
    InvalidShareContentError = 0
    ShareCanceledError = 0
    ShareInterruptedError = 0
    ShareRejectedError = 0
    UnsupportedShareModeError = 0
    ShareAlreadyInProgressError = 0
    SharePermissionDeniedError = 0

    def __init__(self, parent = None):
        '''void QNearFieldShareManager.__init__(QObject parent = None)'''
    error = pyqtSignal() # void error(QNearFieldShareManager::ShareError) - signal
    shareModesChanged = pyqtSignal() # void shareModesChanged(QNearFieldShareManager::ShareModes) - signal
    targetDetected = pyqtSignal() # void targetDetected(QNearFieldShareTarget*) - signal
    def shareError(self):
        '''QNearFieldShareManager.ShareError QNearFieldShareManager.shareError()'''
        return QNearFieldShareManager.ShareError()
    def shareModes(self):
        '''QNearFieldShareManager.ShareModes QNearFieldShareManager.shareModes()'''
        return QNearFieldShareManager.ShareModes()
    def setShareModes(self, modes):
        '''void QNearFieldShareManager.setShareModes(QNearFieldShareManager.ShareModes modes)'''
    def supportedShareModes(self):
        '''static QNearFieldShareManager.ShareModes QNearFieldShareManager.supportedShareModes()'''
        return QNearFieldShareManager.ShareModes()
    class ShareModes():
        """"""
        def __init__(self):
            '''QNearFieldShareManager.ShareModes QNearFieldShareManager.ShareModes.__init__()'''
            return QNearFieldShareManager.ShareModes()
        def __init__(self):
            '''int QNearFieldShareManager.ShareModes.__init__()'''
            return int()
        def __init__(self):
            '''void QNearFieldShareManager.ShareModes.__init__()'''
        def __bool__(self):
            '''int QNearFieldShareManager.ShareModes.__bool__()'''
            return int()
        def __ne__(self, f):
            '''bool QNearFieldShareManager.ShareModes.__ne__(QNearFieldShareManager.ShareModes f)'''
            return bool()
        def __eq__(self, f):
            '''bool QNearFieldShareManager.ShareModes.__eq__(QNearFieldShareManager.ShareModes f)'''
            return bool()
        def __invert__(self):
            '''QNearFieldShareManager.ShareModes QNearFieldShareManager.ShareModes.__invert__()'''
            return QNearFieldShareManager.ShareModes()
        def __and__(self, mask):
            '''QNearFieldShareManager.ShareModes QNearFieldShareManager.ShareModes.__and__(int mask)'''
            return QNearFieldShareManager.ShareModes()
        def __xor__(self, f):
            '''QNearFieldShareManager.ShareModes QNearFieldShareManager.ShareModes.__xor__(QNearFieldShareManager.ShareModes f)'''
            return QNearFieldShareManager.ShareModes()
        def __xor__(self, f):
            '''QNearFieldShareManager.ShareModes QNearFieldShareManager.ShareModes.__xor__(int f)'''
            return QNearFieldShareManager.ShareModes()
        def __or__(self, f):
            '''QNearFieldShareManager.ShareModes QNearFieldShareManager.ShareModes.__or__(QNearFieldShareManager.ShareModes f)'''
            return QNearFieldShareManager.ShareModes()
        def __or__(self, f):
            '''QNearFieldShareManager.ShareModes QNearFieldShareManager.ShareModes.__or__(int f)'''
            return QNearFieldShareManager.ShareModes()
        def __int__(self):
            '''int QNearFieldShareManager.ShareModes.__int__()'''
            return int()
        def __ixor__(self, f):
            '''QNearFieldShareManager.ShareModes QNearFieldShareManager.ShareModes.__ixor__(QNearFieldShareManager.ShareModes f)'''
            return QNearFieldShareManager.ShareModes()
        def __ior__(self, f):
            '''QNearFieldShareManager.ShareModes QNearFieldShareManager.ShareModes.__ior__(QNearFieldShareManager.ShareModes f)'''
            return QNearFieldShareManager.ShareModes()
        def __iand__(self, mask):
            '''QNearFieldShareManager.ShareModes QNearFieldShareManager.ShareModes.__iand__(int mask)'''
            return QNearFieldShareManager.ShareModes()


class QNearFieldShareTarget(QObject):
    """"""
    shareFinished = pyqtSignal() # void shareFinished() - signal
    error = pyqtSignal() # void error(QNearFieldShareManager::ShareError) - signal
    def shareError(self):
        '''QNearFieldShareManager.ShareError QNearFieldShareTarget.shareError()'''
        return QNearFieldShareManager.ShareError()
    def isShareInProgress(self):
        '''bool QNearFieldShareTarget.isShareInProgress()'''
        return bool()
    def cancel(self):
        '''void QNearFieldShareTarget.cancel()'''
    def share(self, message):
        '''bool QNearFieldShareTarget.share(QNdefMessage message)'''
        return bool()
    def share(self, files):
        '''bool QNearFieldShareTarget.share(list-of-QFileInfo files)'''
        return bool()
    def shareModes(self):
        '''QNearFieldShareManager.ShareModes QNearFieldShareTarget.shareModes()'''
        return QNearFieldShareManager.ShareModes()


class QNearFieldTarget(QObject):
    """"""
    # Enum QNearFieldTarget.Error
    NoError = 0
    UnknownError = 0
    UnsupportedError = 0
    TargetOutOfRangeError = 0
    NoResponseError = 0
    ChecksumMismatchError = 0
    InvalidParametersError = 0
    NdefReadError = 0
    NdefWriteError = 0

    # Enum QNearFieldTarget.AccessMethod
    UnknownAccess = 0
    NdefAccess = 0
    TagTypeSpecificAccess = 0
    LlcpAccess = 0

    # Enum QNearFieldTarget.Type
    ProprietaryTag = 0
    NfcTagType1 = 0
    NfcTagType2 = 0
    NfcTagType3 = 0
    NfcTagType4 = 0
    MifareTag = 0

    def __init__(self, parent = None):
        '''void QNearFieldTarget.__init__(QObject parent = None)'''
    error = pyqtSignal() # void error(QNearFieldTarget::Error,const QNearFieldTarget::RequestIdamp;) - signal
    requestCompleted = pyqtSignal() # void requestCompleted(const QNearFieldTarget::RequestIdamp;) - signal
    ndefMessagesWritten = pyqtSignal() # void ndefMessagesWritten() - signal
    ndefMessageRead = pyqtSignal() # void ndefMessageRead(const QNdefMessageamp;) - signal
    disconnected = pyqtSignal() # void disconnected() - signal
    def handleResponse(self, id, response):
        '''bool QNearFieldTarget.handleResponse(QNearFieldTarget.RequestId id, QByteArray response)'''
        return bool()
    def setResponseForRequest(self, id, response, emitRequestCompleted = True):
        '''void QNearFieldTarget.setResponseForRequest(QNearFieldTarget.RequestId id, QVariant response, bool emitRequestCompleted = True)'''
    def requestResponse(self, id):
        '''QVariant QNearFieldTarget.requestResponse(QNearFieldTarget.RequestId id)'''
        return QVariant()
    def waitForRequestCompleted(self, id, msecs = 5000):
        '''bool QNearFieldTarget.waitForRequestCompleted(QNearFieldTarget.RequestId id, int msecs = 5000)'''
        return bool()
    def sendCommands(self, commands):
        '''QNearFieldTarget.RequestId QNearFieldTarget.sendCommands(list-of-QByteArray commands)'''
        return QNearFieldTarget.RequestId()
    def sendCommand(self, command):
        '''QNearFieldTarget.RequestId QNearFieldTarget.sendCommand(QByteArray command)'''
        return QNearFieldTarget.RequestId()
    def writeNdefMessages(self, messages):
        '''QNearFieldTarget.RequestId QNearFieldTarget.writeNdefMessages(list-of-QNdefMessage messages)'''
        return QNearFieldTarget.RequestId()
    def readNdefMessages(self):
        '''QNearFieldTarget.RequestId QNearFieldTarget.readNdefMessages()'''
        return QNearFieldTarget.RequestId()
    def hasNdefMessage(self):
        '''bool QNearFieldTarget.hasNdefMessage()'''
        return bool()
    def isProcessingCommand(self):
        '''bool QNearFieldTarget.isProcessingCommand()'''
        return bool()
    def accessMethods(self):
        '''abstract QNearFieldTarget.AccessMethods QNearFieldTarget.accessMethods()'''
        return QNearFieldTarget.AccessMethods()
    def type(self):
        '''abstract QNearFieldTarget.Type QNearFieldTarget.type()'''
        return QNearFieldTarget.Type()
    def url(self):
        '''QUrl QNearFieldTarget.url()'''
        return QUrl()
    def uid(self):
        '''abstract QByteArray QNearFieldTarget.uid()'''
        return QByteArray()
    class RequestId():
        """"""
        def __init__(self):
            '''void QNearFieldTarget.RequestId.__init__()'''
        def __init__(self, other):
            '''void QNearFieldTarget.RequestId.__init__(QNearFieldTarget.RequestId other)'''
        def __ge__(self, other):
            '''bool QNearFieldTarget.RequestId.__ge__(QNearFieldTarget.RequestId other)'''
            return bool()
        def __ne__(self, other):
            '''bool QNearFieldTarget.RequestId.__ne__(QNearFieldTarget.RequestId other)'''
            return bool()
        def __eq__(self, other):
            '''bool QNearFieldTarget.RequestId.__eq__(QNearFieldTarget.RequestId other)'''
            return bool()
        def __lt__(self, other):
            '''bool QNearFieldTarget.RequestId.__lt__(QNearFieldTarget.RequestId other)'''
            return bool()
        def refCount(self):
            '''int QNearFieldTarget.RequestId.refCount()'''
            return int()
        def isValid(self):
            '''bool QNearFieldTarget.RequestId.isValid()'''
            return bool()
    class AccessMethods():
        """"""
        def __init__(self):
            '''QNearFieldTarget.AccessMethods QNearFieldTarget.AccessMethods.__init__()'''
            return QNearFieldTarget.AccessMethods()
        def __init__(self):
            '''int QNearFieldTarget.AccessMethods.__init__()'''
            return int()
        def __init__(self):
            '''void QNearFieldTarget.AccessMethods.__init__()'''
        def __bool__(self):
            '''int QNearFieldTarget.AccessMethods.__bool__()'''
            return int()
        def __ne__(self, f):
            '''bool QNearFieldTarget.AccessMethods.__ne__(QNearFieldTarget.AccessMethods f)'''
            return bool()
        def __eq__(self, f):
            '''bool QNearFieldTarget.AccessMethods.__eq__(QNearFieldTarget.AccessMethods f)'''
            return bool()
        def __invert__(self):
            '''QNearFieldTarget.AccessMethods QNearFieldTarget.AccessMethods.__invert__()'''
            return QNearFieldTarget.AccessMethods()
        def __and__(self, mask):
            '''QNearFieldTarget.AccessMethods QNearFieldTarget.AccessMethods.__and__(int mask)'''
            return QNearFieldTarget.AccessMethods()
        def __xor__(self, f):
            '''QNearFieldTarget.AccessMethods QNearFieldTarget.AccessMethods.__xor__(QNearFieldTarget.AccessMethods f)'''
            return QNearFieldTarget.AccessMethods()
        def __xor__(self, f):
            '''QNearFieldTarget.AccessMethods QNearFieldTarget.AccessMethods.__xor__(int f)'''
            return QNearFieldTarget.AccessMethods()
        def __or__(self, f):
            '''QNearFieldTarget.AccessMethods QNearFieldTarget.AccessMethods.__or__(QNearFieldTarget.AccessMethods f)'''
            return QNearFieldTarget.AccessMethods()
        def __or__(self, f):
            '''QNearFieldTarget.AccessMethods QNearFieldTarget.AccessMethods.__or__(int f)'''
            return QNearFieldTarget.AccessMethods()
        def __int__(self):
            '''int QNearFieldTarget.AccessMethods.__int__()'''
            return int()
        def __ixor__(self, f):
            '''QNearFieldTarget.AccessMethods QNearFieldTarget.AccessMethods.__ixor__(QNearFieldTarget.AccessMethods f)'''
            return QNearFieldTarget.AccessMethods()
        def __ior__(self, f):
            '''QNearFieldTarget.AccessMethods QNearFieldTarget.AccessMethods.__ior__(QNearFieldTarget.AccessMethods f)'''
            return QNearFieldTarget.AccessMethods()
        def __iand__(self, mask):
            '''QNearFieldTarget.AccessMethods QNearFieldTarget.AccessMethods.__iand__(int mask)'''
            return QNearFieldTarget.AccessMethods()


class QQmlNdefRecord(QObject):
    """"""
    # Enum QQmlNdefRecord.TypeNameFormat
    Empty = 0
    NfcRtd = 0
    Mime = 0
    Uri = 0
    ExternalRtd = 0
    Unknown = 0

    def __init__(self, parent = None):
        '''void QQmlNdefRecord.__init__(QObject parent = None)'''
    def __init__(self, record, parent = None):
        '''void QQmlNdefRecord.__init__(QNdefRecord record, QObject parent = None)'''
    recordChanged = pyqtSignal() # void recordChanged() - signal
    typeNameFormatChanged = pyqtSignal() # void typeNameFormatChanged() - signal
    typeChanged = pyqtSignal() # void typeChanged() - signal
    def setRecord(self, record):
        '''void QQmlNdefRecord.setRecord(QNdefRecord record)'''
    def record(self):
        '''QNdefRecord QQmlNdefRecord.record()'''
        return QNdefRecord()
    def typeNameFormat(self):
        '''QQmlNdefRecord.TypeNameFormat QQmlNdefRecord.typeNameFormat()'''
        return QQmlNdefRecord.TypeNameFormat()
    def setTypeNameFormat(self, typeNameFormat):
        '''void QQmlNdefRecord.setTypeNameFormat(QQmlNdefRecord.TypeNameFormat typeNameFormat)'''
    def setType(self, t):
        '''void QQmlNdefRecord.setType(str t)'''
    def type(self):
        '''str QQmlNdefRecord.type()'''
        return str()


