class pyqtSignal():
 def connect(self, targetSignal): pass
 def emit(self, *args): pass
from QtCore import *

from QtWidgets import *

import datetime

class QJSEngine(QObject):
    """"""
    def __init__(self):
        '''void QJSEngine.__init__()'''
    def __init__(self, parent):
        '''void QJSEngine.__init__(QObject parent)'''
    def installTranslatorFunctions(self, object = None):
        '''void QJSEngine.installTranslatorFunctions(QJSValue object = QJSValue(QJSValue.UndefinedValue))'''
    def collectGarbage(self):
        '''void QJSEngine.collectGarbage()'''
    def newQObject(self, object):
        '''QJSValue QJSEngine.newQObject(QObject object)'''
        return QJSValue()
    def newArray(self, length = 0):
        '''QJSValue QJSEngine.newArray(int length = 0)'''
        return QJSValue()
    def newObject(self):
        '''QJSValue QJSEngine.newObject()'''
        return QJSValue()
    def evaluate(self, program, fileName = str(), lineNumber = 1):
        '''QJSValue QJSEngine.evaluate(str program, str fileName = str(), int lineNumber = 1)'''
        return QJSValue()
    def globalObject(self):
        '''QJSValue QJSEngine.globalObject()'''
        return QJSValue()


class QJSValue():
    """"""
    # Enum QJSValue.SpecialValue
    NullValue = 0
    UndefinedValue = 0

    def __init__(self, value = None):
        '''void QJSValue.__init__(QJSValue.SpecialValue value = QJSValue.UndefinedValue)'''
    def __init__(self, other):
        '''void QJSValue.__init__(QJSValue other)'''
    def callAsConstructor(self, args = None):
        '''QJSValue QJSValue.callAsConstructor(list-of-QJSValue args = QListlt;QJSValuegt;())'''
        return QJSValue()
    def callWithInstance(self, instance, args = None):
        '''QJSValue QJSValue.callWithInstance(QJSValue instance, list-of-QJSValue args = QListlt;QJSValuegt;())'''
        return QJSValue()
    def call(self, args = None):
        '''QJSValue QJSValue.call(list-of-QJSValue args = QListlt;QJSValuegt;())'''
        return QJSValue()
    def isCallable(self):
        '''bool QJSValue.isCallable()'''
        return bool()
    def deleteProperty(self, name):
        '''bool QJSValue.deleteProperty(str name)'''
        return bool()
    def hasOwnProperty(self, name):
        '''bool QJSValue.hasOwnProperty(str name)'''
        return bool()
    def hasProperty(self, name):
        '''bool QJSValue.hasProperty(str name)'''
        return bool()
    def setProperty(self, name, value):
        '''void QJSValue.setProperty(str name, QJSValue value)'''
    def setProperty(self, arrayIndex, value):
        '''void QJSValue.setProperty(int arrayIndex, QJSValue value)'''
    def property(self, name):
        '''QJSValue QJSValue.property(str name)'''
        return QJSValue()
    def property(self, arrayIndex):
        '''QJSValue QJSValue.property(int arrayIndex)'''
        return QJSValue()
    def setPrototype(self, prototype):
        '''void QJSValue.setPrototype(QJSValue prototype)'''
    def prototype(self):
        '''QJSValue QJSValue.prototype()'''
        return QJSValue()
    def strictlyEquals(self, other):
        '''bool QJSValue.strictlyEquals(QJSValue other)'''
        return bool()
    def equals(self, other):
        '''bool QJSValue.equals(QJSValue other)'''
        return bool()
    def toDateTime(self):
        '''QDateTime QJSValue.toDateTime()'''
        return QDateTime()
    def toQObject(self):
        '''QObject QJSValue.toQObject()'''
        return QObject()
    def toVariant(self):
        '''QVariant QJSValue.toVariant()'''
        return QVariant()
    def toBool(self):
        '''bool QJSValue.toBool()'''
        return bool()
    def toUInt(self):
        '''int QJSValue.toUInt()'''
        return int()
    def toInt(self):
        '''int QJSValue.toInt()'''
        return int()
    def toNumber(self):
        '''float QJSValue.toNumber()'''
        return float()
    def toString(self):
        '''str QJSValue.toString()'''
        return str()
    def isError(self):
        '''bool QJSValue.isError()'''
        return bool()
    def isArray(self):
        '''bool QJSValue.isArray()'''
        return bool()
    def isRegExp(self):
        '''bool QJSValue.isRegExp()'''
        return bool()
    def isDate(self):
        '''bool QJSValue.isDate()'''
        return bool()
    def isObject(self):
        '''bool QJSValue.isObject()'''
        return bool()
    def isQObject(self):
        '''bool QJSValue.isQObject()'''
        return bool()
    def isVariant(self):
        '''bool QJSValue.isVariant()'''
        return bool()
    def isUndefined(self):
        '''bool QJSValue.isUndefined()'''
        return bool()
    def isString(self):
        '''bool QJSValue.isString()'''
        return bool()
    def isNull(self):
        '''bool QJSValue.isNull()'''
        return bool()
    def isNumber(self):
        '''bool QJSValue.isNumber()'''
        return bool()
    def isBool(self):
        '''bool QJSValue.isBool()'''
        return bool()


class QJSValueIterator():
    """"""
    def __init__(self, value):
        '''void QJSValueIterator.__init__(QJSValue value)'''
    def value(self):
        '''QJSValue QJSValueIterator.value()'''
        return QJSValue()
    def name(self):
        '''str QJSValueIterator.name()'''
        return str()
    def next(self):
        '''bool QJSValueIterator.next()'''
        return bool()
    def hasNext(self):
        '''bool QJSValueIterator.hasNext()'''
        return bool()


class QQmlAbstractUrlInterceptor():
    """"""
    # Enum QQmlAbstractUrlInterceptor.DataType
    QmlFile = 0
    JavaScriptFile = 0
    QmldirFile = 0
    UrlString = 0

    def __init__(self):
        '''void QQmlAbstractUrlInterceptor.__init__()'''
    def __init__(self):
        '''QQmlAbstractUrlInterceptor QQmlAbstractUrlInterceptor.__init__()'''
        return QQmlAbstractUrlInterceptor()
    def intercept(self, path, type):
        '''abstract QUrl QQmlAbstractUrlInterceptor.intercept(QUrl path, QQmlAbstractUrlInterceptor.DataType type)'''
        return QUrl()


class QQmlEngine(QJSEngine):
    """"""
    # Enum QQmlEngine.ObjectOwnership
    CppOwnership = 0
    JavaScriptOwnership = 0

    def __init__(self, parent = None):
        '''void QQmlEngine.__init__(QObject parent = None)'''
    warnings = pyqtSignal() # void warnings(const QListlt;QQmlErrorgt;amp;) - signal
    quit = pyqtSignal() # void quit() - signal
    def event(self):
        '''QEvent QQmlEngine.event()'''
        return QEvent()
    def objectOwnership(self):
        '''static QObject QQmlEngine.objectOwnership()'''
        return QObject()
    def setObjectOwnership(self):
        '''static QQmlEngine.ObjectOwnership QQmlEngine.setObjectOwnership()'''
        return QQmlEngine.ObjectOwnership()
    def setContextForObject(self):
        '''static QQmlContext QQmlEngine.setContextForObject()'''
        return QQmlContext()
    def contextForObject(self):
        '''static QObject QQmlEngine.contextForObject()'''
        return QObject()
    def setOutputWarningsToStandardError(self):
        '''bool QQmlEngine.setOutputWarningsToStandardError()'''
        return bool()
    def outputWarningsToStandardError(self):
        '''bool QQmlEngine.outputWarningsToStandardError()'''
        return bool()
    def setBaseUrl(self):
        '''QUrl QQmlEngine.setBaseUrl()'''
        return QUrl()
    def baseUrl(self):
        '''QUrl QQmlEngine.baseUrl()'''
        return QUrl()
    def offlineStoragePath(self):
        '''str QQmlEngine.offlineStoragePath()'''
        return str()
    def setOfflineStoragePath(self, dir):
        '''void QQmlEngine.setOfflineStoragePath(str dir)'''
    def incubationController(self):
        '''QQmlIncubationController QQmlEngine.incubationController()'''
        return QQmlIncubationController()
    def setIncubationController(self):
        '''QQmlIncubationController QQmlEngine.setIncubationController()'''
        return QQmlIncubationController()
    def removeImageProvider(self, id):
        '''void QQmlEngine.removeImageProvider(str id)'''
    def imageProvider(self, id):
        '''QQmlImageProviderBase QQmlEngine.imageProvider(str id)'''
        return QQmlImageProviderBase()
    def addImageProvider(self, id):
        '''QQmlImageProviderBase QQmlEngine.addImageProvider(str id)'''
        return QQmlImageProviderBase()
    def networkAccessManager(self):
        '''QNetworkAccessManager QQmlEngine.networkAccessManager()'''
        return QNetworkAccessManager()
    def networkAccessManagerFactory(self):
        '''QQmlNetworkAccessManagerFactory QQmlEngine.networkAccessManagerFactory()'''
        return QQmlNetworkAccessManagerFactory()
    def setNetworkAccessManagerFactory(self):
        '''QQmlNetworkAccessManagerFactory QQmlEngine.setNetworkAccessManagerFactory()'''
        return QQmlNetworkAccessManagerFactory()
    def importPlugin(self, filePath, uri, errors):
        '''bool QQmlEngine.importPlugin(str filePath, str uri, list-of-QQmlError errors)'''
        return bool()
    def addNamedBundle(self, name, fileName):
        '''bool QQmlEngine.addNamedBundle(str name, str fileName)'''
        return bool()
    def addPluginPath(self, dir):
        '''void QQmlEngine.addPluginPath(str dir)'''
    def setPluginPathList(self, paths):
        '''void QQmlEngine.setPluginPathList(list-of-str paths)'''
    def pluginPathList(self):
        '''list-of-str QQmlEngine.pluginPathList()'''
        return [str()]
    def addImportPath(self, dir):
        '''void QQmlEngine.addImportPath(str dir)'''
    def setImportPathList(self, paths):
        '''void QQmlEngine.setImportPathList(list-of-str paths)'''
    def importPathList(self):
        '''list-of-str QQmlEngine.importPathList()'''
        return [str()]
    def trimComponentCache(self):
        '''void QQmlEngine.trimComponentCache()'''
    def clearComponentCache(self):
        '''void QQmlEngine.clearComponentCache()'''
    def rootContext(self):
        '''QQmlContext QQmlEngine.rootContext()'''
        return QQmlContext()


class QQmlApplicationEngine(QQmlEngine):
    """"""
    def __init__(self, parent = None):
        '''void QQmlApplicationEngine.__init__(QObject parent = None)'''
    def __init__(self, url, parent = None):
        '''void QQmlApplicationEngine.__init__(QUrl url, QObject parent = None)'''
    def __init__(self, filePath, parent = None):
        '''void QQmlApplicationEngine.__init__(str filePath, QObject parent = None)'''
    objectCreated = pyqtSignal() # void objectCreated(QObject*,const QUrlamp;) - signal
    def loadData(self, data, url = QUrl()):
        '''void QQmlApplicationEngine.loadData(QByteArray data, QUrl url = QUrl())'''
    def load(self, url):
        '''void QQmlApplicationEngine.load(QUrl url)'''
    def load(self, filePath):
        '''void QQmlApplicationEngine.load(str filePath)'''
    def rootObjects(self):
        '''list-of-QObject QQmlApplicationEngine.rootObjects()'''
        return [QObject()]


class QQmlComponent(QObject):
    """"""
    # Enum QQmlComponent.Status
    Null = 0
    Ready = 0
    Loading = 0
    Error = 0

    # Enum QQmlComponent.CompilationMode
    PreferSynchronous = 0
    Asynchronous = 0

    def __init__(self, parent = None):
        '''QQmlEngine QQmlComponent.__init__(QObject parent = None)'''
        return QQmlEngine()
    def __init__(self, fileName, parent = None):
        '''QQmlEngine QQmlComponent.__init__(str fileName, QObject parent = None)'''
        return QQmlEngine()
    def __init__(self, fileName, mode, parent = None):
        '''QQmlEngine QQmlComponent.__init__(str fileName, QQmlComponent.CompilationMode mode, QObject parent = None)'''
        return QQmlEngine()
    def __init__(self, url, parent = None):
        '''QQmlEngine QQmlComponent.__init__(QUrl url, QObject parent = None)'''
        return QQmlEngine()
    def __init__(self, url, mode, parent = None):
        '''QQmlEngine QQmlComponent.__init__(QUrl url, QQmlComponent.CompilationMode mode, QObject parent = None)'''
        return QQmlEngine()
    def __init__(self, parent = None):
        '''void QQmlComponent.__init__(QObject parent = None)'''
    progressChanged = pyqtSignal() # void progressChanged(qreal) - signal
    statusChanged = pyqtSignal() # void statusChanged(QQmlComponent::Status) - signal
    def setData(self, baseUrl):
        '''QByteArray QQmlComponent.setData(QUrl baseUrl)'''
        return QByteArray()
    def loadUrl(self, url):
        '''void QQmlComponent.loadUrl(QUrl url)'''
    def loadUrl(self, url, mode):
        '''void QQmlComponent.loadUrl(QUrl url, QQmlComponent.CompilationMode mode)'''
    def creationContext(self):
        '''QQmlContext QQmlComponent.creationContext()'''
        return QQmlContext()
    def completeCreate(self):
        '''void QQmlComponent.completeCreate()'''
    def beginCreate(self):
        '''QQmlContext QQmlComponent.beginCreate()'''
        return QQmlContext()
    def create(self, context = None):
        '''QObject QQmlComponent.create(QQmlContext context = None)'''
        return QObject()
    def create(self, context = None, forContext = None):
        '''QQmlIncubator QQmlComponent.create(QQmlContext context = None, QQmlContext forContext = None)'''
        return QQmlIncubator()
    def url(self):
        '''QUrl QQmlComponent.url()'''
        return QUrl()
    def progress(self):
        '''float QQmlComponent.progress()'''
        return float()
    def errors(self):
        '''list-of-QQmlError QQmlComponent.errors()'''
        return [QQmlError()]
    def isLoading(self):
        '''bool QQmlComponent.isLoading()'''
        return bool()
    def isError(self):
        '''bool QQmlComponent.isError()'''
        return bool()
    def isReady(self):
        '''bool QQmlComponent.isReady()'''
        return bool()
    def isNull(self):
        '''bool QQmlComponent.isNull()'''
        return bool()
    def status(self):
        '''QQmlComponent.Status QQmlComponent.status()'''
        return QQmlComponent.Status()


class QQmlContext(QObject):
    """"""
    def __init__(self, engine, parent = None):
        '''void QQmlContext.__init__(QQmlEngine engine, QObject parent = None)'''
    def __init__(self, parentContext, parent = None):
        '''void QQmlContext.__init__(QQmlContext parentContext, QObject parent = None)'''
    def baseUrl(self):
        '''QUrl QQmlContext.baseUrl()'''
        return QUrl()
    def setBaseUrl(self):
        '''QUrl QQmlContext.setBaseUrl()'''
        return QUrl()
    def resolvedUrl(self):
        '''QUrl QQmlContext.resolvedUrl()'''
        return QUrl()
    def nameForObject(self):
        '''QObject QQmlContext.nameForObject()'''
        return QObject()
    def setContextProperty(self):
        '''QObject QQmlContext.setContextProperty()'''
        return QObject()
    def setContextProperty(self):
        '''QVariant QQmlContext.setContextProperty()'''
        return QVariant()
    def contextProperty(self):
        '''str QQmlContext.contextProperty()'''
        return str()
    def setContextObject(self):
        '''QObject QQmlContext.setContextObject()'''
        return QObject()
    def contextObject(self):
        '''QObject QQmlContext.contextObject()'''
        return QObject()
    def parentContext(self):
        '''QQmlContext QQmlContext.parentContext()'''
        return QQmlContext()
    def engine(self):
        '''QQmlEngine QQmlContext.engine()'''
        return QQmlEngine()
    def isValid(self):
        '''bool QQmlContext.isValid()'''
        return bool()


class QQmlImageProviderBase():
    """"""
    # Enum QQmlImageProviderBase.Flag
    ForceAsynchronousImageLoading = 0

    # Enum QQmlImageProviderBase.ImageType
    Image = 0
    Pixmap = 0
    Texture = 0

    def __init__(self):
        '''QQmlImageProviderBase QQmlImageProviderBase.__init__()'''
        return QQmlImageProviderBase()
    def flags(self):
        '''abstract QQmlImageProviderBase.Flags QQmlImageProviderBase.flags()'''
        return QQmlImageProviderBase.Flags()
    def imageType(self):
        '''abstract QQmlImageProviderBase.ImageType QQmlImageProviderBase.imageType()'''
        return QQmlImageProviderBase.ImageType()
    class Flags():
        """"""
        def __init__(self):
            '''QQmlImageProviderBase.Flags QQmlImageProviderBase.Flags.__init__()'''
            return QQmlImageProviderBase.Flags()
        def __init__(self):
            '''int QQmlImageProviderBase.Flags.__init__()'''
            return int()
        def __init__(self):
            '''void QQmlImageProviderBase.Flags.__init__()'''
        def __bool__(self):
            '''int QQmlImageProviderBase.Flags.__bool__()'''
            return int()
        def __ne__(self, f):
            '''bool QQmlImageProviderBase.Flags.__ne__(QQmlImageProviderBase.Flags f)'''
            return bool()
        def __eq__(self, f):
            '''bool QQmlImageProviderBase.Flags.__eq__(QQmlImageProviderBase.Flags f)'''
            return bool()
        def __invert__(self):
            '''QQmlImageProviderBase.Flags QQmlImageProviderBase.Flags.__invert__()'''
            return QQmlImageProviderBase.Flags()
        def __and__(self, mask):
            '''QQmlImageProviderBase.Flags QQmlImageProviderBase.Flags.__and__(int mask)'''
            return QQmlImageProviderBase.Flags()
        def __xor__(self, f):
            '''QQmlImageProviderBase.Flags QQmlImageProviderBase.Flags.__xor__(QQmlImageProviderBase.Flags f)'''
            return QQmlImageProviderBase.Flags()
        def __xor__(self, f):
            '''QQmlImageProviderBase.Flags QQmlImageProviderBase.Flags.__xor__(int f)'''
            return QQmlImageProviderBase.Flags()
        def __or__(self, f):
            '''QQmlImageProviderBase.Flags QQmlImageProviderBase.Flags.__or__(QQmlImageProviderBase.Flags f)'''
            return QQmlImageProviderBase.Flags()
        def __or__(self, f):
            '''QQmlImageProviderBase.Flags QQmlImageProviderBase.Flags.__or__(int f)'''
            return QQmlImageProviderBase.Flags()
        def __int__(self):
            '''int QQmlImageProviderBase.Flags.__int__()'''
            return int()
        def __ixor__(self, f):
            '''QQmlImageProviderBase.Flags QQmlImageProviderBase.Flags.__ixor__(QQmlImageProviderBase.Flags f)'''
            return QQmlImageProviderBase.Flags()
        def __ior__(self, f):
            '''QQmlImageProviderBase.Flags QQmlImageProviderBase.Flags.__ior__(QQmlImageProviderBase.Flags f)'''
            return QQmlImageProviderBase.Flags()
        def __iand__(self, mask):
            '''QQmlImageProviderBase.Flags QQmlImageProviderBase.Flags.__iand__(int mask)'''
            return QQmlImageProviderBase.Flags()


class QQmlError():
    """"""
    def __init__(self):
        '''void QQmlError.__init__()'''
    def __init__(self):
        '''QQmlError QQmlError.__init__()'''
        return QQmlError()
    def setObject(self):
        '''QObject QQmlError.setObject()'''
        return QObject()
    def object(self):
        '''QObject QQmlError.object()'''
        return QObject()
    def toString(self):
        '''str QQmlError.toString()'''
        return str()
    def setColumn(self):
        '''int QQmlError.setColumn()'''
        return int()
    def column(self):
        '''int QQmlError.column()'''
        return int()
    def setLine(self):
        '''int QQmlError.setLine()'''
        return int()
    def line(self):
        '''int QQmlError.line()'''
        return int()
    def setDescription(self):
        '''str QQmlError.setDescription()'''
        return str()
    def description(self):
        '''str QQmlError.description()'''
        return str()
    def setUrl(self):
        '''QUrl QQmlError.setUrl()'''
        return QUrl()
    def url(self):
        '''QUrl QQmlError.url()'''
        return QUrl()
    def isValid(self):
        '''bool QQmlError.isValid()'''
        return bool()


class QQmlExpression(QObject):
    """"""
    def __init__(self):
        '''void QQmlExpression.__init__()'''
    def __init__(self, parent = None):
        '''str QQmlExpression.__init__(QObject parent = None)'''
        return str()
    def __init__(self, context = None, scope = None, parent = None):
        '''QQmlScriptString QQmlExpression.__init__(QQmlContext context = None, QObject scope = None, QObject parent = None)'''
        return QQmlScriptString()
    valueChanged = pyqtSignal() # void valueChanged() - signal
    def evaluate(self, valueIsUndefined):
        '''QVariant QQmlExpression.evaluate(bool valueIsUndefined)'''
        return QVariant()
    def error(self):
        '''QQmlError QQmlExpression.error()'''
        return QQmlError()
    def clearError(self):
        '''void QQmlExpression.clearError()'''
    def hasError(self):
        '''bool QQmlExpression.hasError()'''
        return bool()
    def scopeObject(self):
        '''QObject QQmlExpression.scopeObject()'''
        return QObject()
    def setSourceLocation(self, fileName, line, column = 0):
        '''void QQmlExpression.setSourceLocation(str fileName, int line, int column = 0)'''
    def columnNumber(self):
        '''int QQmlExpression.columnNumber()'''
        return int()
    def lineNumber(self):
        '''int QQmlExpression.lineNumber()'''
        return int()
    def sourceFile(self):
        '''str QQmlExpression.sourceFile()'''
        return str()
    def setNotifyOnValueChanged(self):
        '''bool QQmlExpression.setNotifyOnValueChanged()'''
        return bool()
    def notifyOnValueChanged(self):
        '''bool QQmlExpression.notifyOnValueChanged()'''
        return bool()
    def setExpression(self):
        '''str QQmlExpression.setExpression()'''
        return str()
    def expression(self):
        '''str QQmlExpression.expression()'''
        return str()
    def context(self):
        '''QQmlContext QQmlExpression.context()'''
        return QQmlContext()
    def engine(self):
        '''QQmlEngine QQmlExpression.engine()'''
        return QQmlEngine()


class QQmlExtensionPlugin(QObject):
    """"""
    def __init__(self, parent = None):
        '''void QQmlExtensionPlugin.__init__(QObject parent = None)'''
    def baseUrl(self):
        '''QUrl QQmlExtensionPlugin.baseUrl()'''
        return QUrl()
    def initializeEngine(self, engine, uri):
        '''void QQmlExtensionPlugin.initializeEngine(QQmlEngine engine, str uri)'''
    def registerTypes(self, uri):
        '''abstract void QQmlExtensionPlugin.registerTypes(str uri)'''


class QQmlFileSelector(QObject):
    """"""
    def __init__(self, engine, parent = None):
        '''void QQmlFileSelector.__init__(QQmlEngine engine, QObject parent = None)'''
    def get(self):
        '''static QQmlEngine QQmlFileSelector.get()'''
        return QQmlEngine()
    def setExtraSelectors(self, strings):
        '''void QQmlFileSelector.setExtraSelectors(list-of-str strings)'''
    def setSelector(self, selector):
        '''void QQmlFileSelector.setSelector(QFileSelector selector)'''


class QQmlIncubator():
    """"""
    # Enum QQmlIncubator.Status
    Null = 0
    Ready = 0
    Loading = 0
    Error = 0

    # Enum QQmlIncubator.IncubationMode
    Asynchronous = 0
    AsynchronousIfNested = 0
    Synchronous = 0

    def __init__(self, mode = None):
        '''void QQmlIncubator.__init__(QQmlIncubator.IncubationMode mode = QQmlIncubator.Asynchronous)'''
    def setInitialState(self):
        '''QObject QQmlIncubator.setInitialState()'''
        return QObject()
    def statusChanged(self):
        '''QQmlIncubator.Status QQmlIncubator.statusChanged()'''
        return QQmlIncubator.Status()
    def object(self):
        '''QObject QQmlIncubator.object()'''
        return QObject()
    def status(self):
        '''QQmlIncubator.Status QQmlIncubator.status()'''
        return QQmlIncubator.Status()
    def incubationMode(self):
        '''QQmlIncubator.IncubationMode QQmlIncubator.incubationMode()'''
        return QQmlIncubator.IncubationMode()
    def errors(self):
        '''list-of-QQmlError QQmlIncubator.errors()'''
        return [QQmlError()]
    def isLoading(self):
        '''bool QQmlIncubator.isLoading()'''
        return bool()
    def isError(self):
        '''bool QQmlIncubator.isError()'''
        return bool()
    def isReady(self):
        '''bool QQmlIncubator.isReady()'''
        return bool()
    def isNull(self):
        '''bool QQmlIncubator.isNull()'''
        return bool()
    def forceCompletion(self):
        '''void QQmlIncubator.forceCompletion()'''
    def clear(self):
        '''void QQmlIncubator.clear()'''


class QQmlIncubationController():
    """"""
    def __init__(self):
        '''void QQmlIncubationController.__init__()'''
    def incubatingObjectCountChanged(self):
        '''int QQmlIncubationController.incubatingObjectCountChanged()'''
        return int()
    def incubateFor(self, msecs):
        '''void QQmlIncubationController.incubateFor(int msecs)'''
    def incubatingObjectCount(self):
        '''int QQmlIncubationController.incubatingObjectCount()'''
        return int()
    def engine(self):
        '''QQmlEngine QQmlIncubationController.engine()'''
        return QQmlEngine()


class QQmlListReference():
    """"""
    def __init__(self):
        '''void QQmlListReference.__init__()'''
    def __init__(self, property, engine = None):
        '''QObject QQmlListReference.__init__(str property, QQmlEngine engine = None)'''
        return QObject()
    def __init__(self):
        '''QQmlListReference QQmlListReference.__init__()'''
        return QQmlListReference()
    def count(self):
        '''int QQmlListReference.count()'''
        return int()
    def clear(self):
        '''bool QQmlListReference.clear()'''
        return bool()
    def at(self):
        '''int QQmlListReference.at()'''
        return int()
    def append(self):
        '''QObject QQmlListReference.append()'''
        return QObject()
    def isReadable(self):
        '''bool QQmlListReference.isReadable()'''
        return bool()
    def isManipulable(self):
        '''bool QQmlListReference.isManipulable()'''
        return bool()
    def canCount(self):
        '''bool QQmlListReference.canCount()'''
        return bool()
    def canClear(self):
        '''bool QQmlListReference.canClear()'''
        return bool()
    def canAt(self):
        '''bool QQmlListReference.canAt()'''
        return bool()
    def canAppend(self):
        '''bool QQmlListReference.canAppend()'''
        return bool()
    def listElementType(self):
        '''QMetaObject QQmlListReference.listElementType()'''
        return QMetaObject()
    def object(self):
        '''QObject QQmlListReference.object()'''
        return QObject()
    def isValid(self):
        '''bool QQmlListReference.isValid()'''
        return bool()


class QQmlNetworkAccessManagerFactory():
    """"""
    def __init__(self):
        '''void QQmlNetworkAccessManagerFactory.__init__()'''
    def __init__(self):
        '''QQmlNetworkAccessManagerFactory QQmlNetworkAccessManagerFactory.__init__()'''
        return QQmlNetworkAccessManagerFactory()
    def create(self, parent):
        '''abstract QNetworkAccessManager QQmlNetworkAccessManagerFactory.create(QObject parent)'''
        return QNetworkAccessManager()


class QQmlParserStatus():
    """"""
    def __init__(self):
        '''void QQmlParserStatus.__init__()'''
    def __init__(self):
        '''QQmlParserStatus QQmlParserStatus.__init__()'''
        return QQmlParserStatus()
    def componentComplete(self):
        '''abstract void QQmlParserStatus.componentComplete()'''
    def classBegin(self):
        '''abstract void QQmlParserStatus.classBegin()'''


class QQmlProperty():
    """"""
    # Enum QQmlProperty.Type
    Invalid = 0
    Property = 0
    SignalProperty = 0

    # Enum QQmlProperty.PropertyTypeCategory
    InvalidCategory = 0
    List = 0
    Object = 0
    Normal = 0

    def __init__(self):
        '''void QQmlProperty.__init__()'''
    def __init__(self):
        '''QObject QQmlProperty.__init__()'''
        return QObject()
    def __init__(self):
        '''QQmlContext QQmlProperty.__init__()'''
        return QQmlContext()
    def __init__(self):
        '''QQmlEngine QQmlProperty.__init__()'''
        return QQmlEngine()
    def __init__(self):
        '''str QQmlProperty.__init__()'''
        return str()
    def __init__(self):
        '''QQmlContext QQmlProperty.__init__()'''
        return QQmlContext()
    def __init__(self):
        '''QQmlEngine QQmlProperty.__init__()'''
        return QQmlEngine()
    def __init__(self):
        '''QQmlProperty QQmlProperty.__init__()'''
        return QQmlProperty()
    def __ne__(self):
        '''QQmlProperty QQmlProperty.__ne__()'''
        return QQmlProperty()
    def method(self):
        '''QMetaMethod QQmlProperty.method()'''
        return QMetaMethod()
    def property(self):
        '''QMetaProperty QQmlProperty.property()'''
        return QMetaProperty()
    def index(self):
        '''int QQmlProperty.index()'''
        return int()
    def object(self):
        '''QObject QQmlProperty.object()'''
        return QObject()
    def isResettable(self):
        '''bool QQmlProperty.isResettable()'''
        return bool()
    def isDesignable(self):
        '''bool QQmlProperty.isDesignable()'''
        return bool()
    def isWritable(self):
        '''bool QQmlProperty.isWritable()'''
        return bool()
    def connectNotifySignal(self, slot):
        '''bool QQmlProperty.connectNotifySignal(slot slot)'''
        return bool()
    def connectNotifySignal(self, dest, method):
        '''bool QQmlProperty.connectNotifySignal(QObject dest, int method)'''
        return bool()
    def needsNotifySignal(self):
        '''bool QQmlProperty.needsNotifySignal()'''
        return bool()
    def hasNotifySignal(self):
        '''bool QQmlProperty.hasNotifySignal()'''
        return bool()
    def reset(self):
        '''bool QQmlProperty.reset()'''
        return bool()
    def write(self):
        '''QVariant QQmlProperty.write()'''
        return QVariant()
    def write(self):
        '''static QVariant QQmlProperty.write()'''
        return QVariant()
    def write(self):
        '''static QQmlContext QQmlProperty.write()'''
        return QQmlContext()
    def write(self):
        '''static QQmlEngine QQmlProperty.write()'''
        return QQmlEngine()
    def read(self):
        '''QVariant QQmlProperty.read()'''
        return QVariant()
    def read(self):
        '''static str QQmlProperty.read()'''
        return str()
    def read(self):
        '''static QQmlContext QQmlProperty.read()'''
        return QQmlContext()
    def read(self):
        '''static QQmlEngine QQmlProperty.read()'''
        return QQmlEngine()
    def name(self):
        '''str QQmlProperty.name()'''
        return str()
    def propertyTypeName(self):
        '''str QQmlProperty.propertyTypeName()'''
        return str()
    def propertyTypeCategory(self):
        '''QQmlProperty.PropertyTypeCategory QQmlProperty.propertyTypeCategory()'''
        return QQmlProperty.PropertyTypeCategory()
    def propertyType(self):
        '''int QQmlProperty.propertyType()'''
        return int()
    def isSignalProperty(self):
        '''bool QQmlProperty.isSignalProperty()'''
        return bool()
    def isProperty(self):
        '''bool QQmlProperty.isProperty()'''
        return bool()
    def isValid(self):
        '''bool QQmlProperty.isValid()'''
        return bool()
    def type(self):
        '''QQmlProperty.Type QQmlProperty.type()'''
        return QQmlProperty.Type()
    def __eq__(self):
        '''QQmlProperty QQmlProperty.__eq__()'''
        return QQmlProperty()
    def __hash__(self):
        '''int QQmlProperty.__hash__()'''
        return int()


class QQmlPropertyMap(QObject):
    """"""
    def __init__(self, parent = None):
        '''void QQmlPropertyMap.__init__(QObject parent = None)'''
    def updateValue(self, key, input):
        '''QVariant QQmlPropertyMap.updateValue(str key, QVariant input)'''
        return QVariant()
    valueChanged = pyqtSignal() # void valueChanged(const QStringamp;,const QVariantamp;) - signal
    def __getitem__(self, key):
        '''QVariant QQmlPropertyMap.__getitem__(str key)'''
        return QVariant()
    def contains(self, key):
        '''bool QQmlPropertyMap.contains(str key)'''
        return bool()
    def isEmpty(self):
        '''bool QQmlPropertyMap.isEmpty()'''
        return bool()
    def __len__(self):
        ''' QQmlPropertyMap.__len__()'''
        return ()
    def size(self):
        '''int QQmlPropertyMap.size()'''
        return int()
    def count(self):
        '''int QQmlPropertyMap.count()'''
        return int()
    def keys(self):
        '''list-of-str QQmlPropertyMap.keys()'''
        return [str()]
    def clear(self, key):
        '''void QQmlPropertyMap.clear(str key)'''
    def insert(self, key, value):
        '''void QQmlPropertyMap.insert(str key, QVariant value)'''
    def value(self, key):
        '''QVariant QQmlPropertyMap.value(str key)'''
        return QVariant()


class QQmlPropertyValueSource():
    """"""
    def __init__(self):
        '''void QQmlPropertyValueSource.__init__()'''
    def __init__(self):
        '''QQmlPropertyValueSource QQmlPropertyValueSource.__init__()'''
        return QQmlPropertyValueSource()
    def setTarget(self):
        '''abstract QQmlProperty QQmlPropertyValueSource.setTarget()'''
        return QQmlProperty()


class QQmlScriptString():
    """"""
    def __init__(self):
        '''void QQmlScriptString.__init__()'''
    def __init__(self):
        '''QQmlScriptString QQmlScriptString.__init__()'''
        return QQmlScriptString()
    def __ne__(self):
        '''QQmlScriptString QQmlScriptString.__ne__()'''
        return QQmlScriptString()
    def __eq__(self):
        '''QQmlScriptString QQmlScriptString.__eq__()'''
        return QQmlScriptString()
    def booleanLiteral(self, ok):
        '''bool QQmlScriptString.booleanLiteral(bool ok)'''
        return bool()
    def numberLiteral(self, ok):
        '''float QQmlScriptString.numberLiteral(bool ok)'''
        return float()
    def stringLiteral(self):
        '''str QQmlScriptString.stringLiteral()'''
        return str()
    def isNullLiteral(self):
        '''bool QQmlScriptString.isNullLiteral()'''
        return bool()
    def isUndefinedLiteral(self):
        '''bool QQmlScriptString.isUndefinedLiteral()'''
        return bool()
    def isEmpty(self):
        '''bool QQmlScriptString.isEmpty()'''
        return bool()


def qmlRegisterUncreatableType(uri, major, minor, qmlName, reason):
    '''static type qmlRegisterUncreatableType(str uri, int major, int minor, str qmlName, str reason)'''
    return type()

def qmlRegisterUncreatableType(revision, uri, major, minor, qmlName, reason):
    '''static type qmlRegisterUncreatableType(int revision, str uri, int major, int minor, str qmlName, str reason)'''
    return type()

def qmlRegisterType(url, uri, major, minor, qmlName):
    '''static int qmlRegisterType(QUrl url, str uri, int major, int minor, str qmlName)'''
    return int()

def qmlRegisterType(attachedProperties = 0):
    '''static type qmlRegisterType(type attachedProperties = 0)'''
    return type()

def qmlRegisterType(uri, major, minor, qmlName, attachedProperties = 0):
    '''static type qmlRegisterType(str uri, int major, int minor, str qmlName, type attachedProperties = 0)'''
    return type()

def qmlRegisterType(revision, uri, major, minor, qmlName, attachedProperties = 0):
    '''static type qmlRegisterType(int revision, str uri, int major, int minor, str qmlName, type attachedProperties = 0)'''
    return type()

def qmlRegisterSingletonType(url, uri, major, minor, qmlName):
    '''static int qmlRegisterSingletonType(QUrl url, str uri, int major, int minor, str qmlName)'''
    return int()

def qmlRegisterSingletonType(uri, major, minor, typeName, factory):
    '''static type qmlRegisterSingletonType(str uri, int major, int minor, str typeName, callable factory)'''
    return type()

def qmlRegisterRevision(revision, uri, major, minor, attachedProperties = 0):
    '''static type qmlRegisterRevision(int revision, str uri, int major, int minor, type attachedProperties = 0)'''
    return type()

def qmlAttachedPropertiesObject(object, create = True):
    '''static type qmlAttachedPropertiesObject(QObject object, bool create = True)'''
    return type()

def qjsEngine():
    '''static QObject qjsEngine()'''
    return QObject()

