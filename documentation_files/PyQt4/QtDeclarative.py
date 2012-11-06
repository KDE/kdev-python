class pyqtSignal():
 def connect(self, targetSignal): pass
 def emit(self, *args): pass
from QtCore import *

class QDeclarativeComponent(QObject):
    """"""
    # Enum QDeclarativeComponent.Status
    Null = 0
    Ready = 0
    Loading = 0
    Error = 0

    def __init__(self, parent = None):
        '''QDeclarativeEngine QDeclarativeComponent.__init__(QObject parent = None)'''
        return QDeclarativeEngine()
    def __init__(self, fileName, parent = None):
        '''QDeclarativeEngine QDeclarativeComponent.__init__(QString fileName, QObject parent = None)'''
        return QDeclarativeEngine()
    def __init__(self, url, parent = None):
        '''QDeclarativeEngine QDeclarativeComponent.__init__(QUrl url, QObject parent = None)'''
        return QDeclarativeEngine()
    progressChanged = pyqtSignal() # void progressChanged(qreal) - signal
    statusChanged = pyqtSignal() # void statusChanged(QDeclarativeComponent::Status) - signal
    def creationContext(self):
        '''QDeclarativeContext QDeclarativeComponent.creationContext()'''
        return QDeclarativeContext()
    def setData(self, baseUrl):
        '''QByteArray QDeclarativeComponent.setData(QUrl baseUrl)'''
        return QByteArray()
    def loadUrl(self, url):
        '''void QDeclarativeComponent.loadUrl(QUrl url)'''
    def completeCreate(self):
        '''void QDeclarativeComponent.completeCreate()'''
    def beginCreate(self):
        '''QDeclarativeContext QDeclarativeComponent.beginCreate()'''
        return QDeclarativeContext()
    def create(self, context = None):
        '''QObject QDeclarativeComponent.create(QDeclarativeContext context = None)'''
        return QObject()
    def url(self):
        '''QUrl QDeclarativeComponent.url()'''
        return QUrl()
    def progress(self):
        '''float QDeclarativeComponent.progress()'''
        return float()
    def errors(self):
        '''list-of-QDeclarativeError QDeclarativeComponent.errors()'''
        return [QDeclarativeError()]
    def isLoading(self):
        '''bool QDeclarativeComponent.isLoading()'''
        return bool()
    def isError(self):
        '''bool QDeclarativeComponent.isError()'''
        return bool()
    def isReady(self):
        '''bool QDeclarativeComponent.isReady()'''
        return bool()
    def isNull(self):
        '''bool QDeclarativeComponent.isNull()'''
        return bool()
    def status(self):
        '''QDeclarativeComponent.Status QDeclarativeComponent.status()'''
        return QDeclarativeComponent.Status()


class QDeclarativeContext(QObject):
    """"""
    def __init__(self, engine, parent = None):
        '''void QDeclarativeContext.__init__(QDeclarativeEngine engine, QObject parent = None)'''
    def __init__(self, context, parent = None):
        '''void QDeclarativeContext.__init__(QDeclarativeContext context, QObject parent = None)'''
    def baseUrl(self):
        '''QUrl QDeclarativeContext.baseUrl()'''
        return QUrl()
    def setBaseUrl(self):
        '''QUrl QDeclarativeContext.setBaseUrl()'''
        return QUrl()
    def resolvedUrl(self):
        '''QUrl QDeclarativeContext.resolvedUrl()'''
        return QUrl()
    def setContextProperty(self):
        '''QObject QDeclarativeContext.setContextProperty()'''
        return QObject()
    def setContextProperty(self):
        '''QVariant QDeclarativeContext.setContextProperty()'''
        return QVariant()
    def contextProperty(self):
        '''QString QDeclarativeContext.contextProperty()'''
        return QString()
    def setContextObject(self):
        '''QObject QDeclarativeContext.setContextObject()'''
        return QObject()
    def contextObject(self):
        '''QObject QDeclarativeContext.contextObject()'''
        return QObject()
    def parentContext(self):
        '''QDeclarativeContext QDeclarativeContext.parentContext()'''
        return QDeclarativeContext()
    def engine(self):
        '''QDeclarativeEngine QDeclarativeContext.engine()'''
        return QDeclarativeEngine()
    def isValid(self):
        '''bool QDeclarativeContext.isValid()'''
        return bool()


class QDeclarativeEngine(QObject):
    """"""
    # Enum QDeclarativeEngine.ObjectOwnership
    CppOwnership = 0
    JavaScriptOwnership = 0

    def __init__(self, parent = None):
        '''void QDeclarativeEngine.__init__(QObject parent = None)'''
    warnings = pyqtSignal() # void warnings(const QListlt;QDeclarativeErrorgt;amp;) - signal
    quit = pyqtSignal() # void quit() - signal
    def objectOwnership(self):
        '''static QObject QDeclarativeEngine.objectOwnership()'''
        return QObject()
    def setObjectOwnership(self):
        '''static QDeclarativeEngine.ObjectOwnership QDeclarativeEngine.setObjectOwnership()'''
        return QDeclarativeEngine.ObjectOwnership()
    def setContextForObject(self):
        '''static QDeclarativeContext QDeclarativeEngine.setContextForObject()'''
        return QDeclarativeContext()
    def contextForObject(self):
        '''static QObject QDeclarativeEngine.contextForObject()'''
        return QObject()
    def setOutputWarningsToStandardError(self):
        '''bool QDeclarativeEngine.setOutputWarningsToStandardError()'''
        return bool()
    def outputWarningsToStandardError(self):
        '''bool QDeclarativeEngine.outputWarningsToStandardError()'''
        return bool()
    def setBaseUrl(self):
        '''QUrl QDeclarativeEngine.setBaseUrl()'''
        return QUrl()
    def baseUrl(self):
        '''QUrl QDeclarativeEngine.baseUrl()'''
        return QUrl()
    def offlineStoragePath(self):
        '''QString QDeclarativeEngine.offlineStoragePath()'''
        return QString()
    def setOfflineStoragePath(self, dir):
        '''void QDeclarativeEngine.setOfflineStoragePath(QString dir)'''
    def removeImageProvider(self, id):
        '''void QDeclarativeEngine.removeImageProvider(QString id)'''
    def imageProvider(self, id):
        '''QDeclarativeImageProvider QDeclarativeEngine.imageProvider(QString id)'''
        return QDeclarativeImageProvider()
    def addImageProvider(self, id):
        '''QDeclarativeImageProvider QDeclarativeEngine.addImageProvider(QString id)'''
        return QDeclarativeImageProvider()
    def networkAccessManager(self):
        '''QNetworkAccessManager QDeclarativeEngine.networkAccessManager()'''
        return QNetworkAccessManager()
    def networkAccessManagerFactory(self):
        '''QDeclarativeNetworkAccessManagerFactory QDeclarativeEngine.networkAccessManagerFactory()'''
        return QDeclarativeNetworkAccessManagerFactory()
    def setNetworkAccessManagerFactory(self):
        '''QDeclarativeNetworkAccessManagerFactory QDeclarativeEngine.setNetworkAccessManagerFactory()'''
        return QDeclarativeNetworkAccessManagerFactory()
    def importPlugin(self, filePath, uri, errorString):
        '''bool QDeclarativeEngine.importPlugin(QString filePath, QString uri, QString errorString)'''
        return bool()
    def addPluginPath(self, dir):
        '''void QDeclarativeEngine.addPluginPath(QString dir)'''
    def setPluginPathList(self, paths):
        '''void QDeclarativeEngine.setPluginPathList(QStringList paths)'''
    def pluginPathList(self):
        '''QStringList QDeclarativeEngine.pluginPathList()'''
        return QStringList()
    def addImportPath(self, dir):
        '''void QDeclarativeEngine.addImportPath(QString dir)'''
    def setImportPathList(self, paths):
        '''void QDeclarativeEngine.setImportPathList(QStringList paths)'''
    def importPathList(self):
        '''QStringList QDeclarativeEngine.importPathList()'''
        return QStringList()
    def clearComponentCache(self):
        '''void QDeclarativeEngine.clearComponentCache()'''
    def rootContext(self):
        '''QDeclarativeContext QDeclarativeEngine.rootContext()'''
        return QDeclarativeContext()


class QDeclarativeError():
    """"""
    def __init__(self):
        '''void QDeclarativeError.__init__()'''
    def __init__(self):
        '''QDeclarativeError QDeclarativeError.__init__()'''
        return QDeclarativeError()
    def toString(self):
        '''QString QDeclarativeError.toString()'''
        return QString()
    def setColumn(self):
        '''int QDeclarativeError.setColumn()'''
        return int()
    def column(self):
        '''int QDeclarativeError.column()'''
        return int()
    def setLine(self):
        '''int QDeclarativeError.setLine()'''
        return int()
    def line(self):
        '''int QDeclarativeError.line()'''
        return int()
    def setDescription(self):
        '''QString QDeclarativeError.setDescription()'''
        return QString()
    def description(self):
        '''QString QDeclarativeError.description()'''
        return QString()
    def setUrl(self):
        '''QUrl QDeclarativeError.setUrl()'''
        return QUrl()
    def url(self):
        '''QUrl QDeclarativeError.url()'''
        return QUrl()
    def isValid(self):
        '''bool QDeclarativeError.isValid()'''
        return bool()


class QDeclarativeExpression(QObject):
    """"""
    def __init__(self):
        '''void QDeclarativeExpression.__init__()'''
    def __init__(self, parent = None):
        '''QString QDeclarativeExpression.__init__(QObject parent = None)'''
        return QString()
    valueChanged = pyqtSignal() # void valueChanged() - signal
    def evaluate(self, valueIsUndefined):
        '''QVariant QDeclarativeExpression.evaluate(bool valueIsUndefined)'''
        return QVariant()
    def error(self):
        '''QDeclarativeError QDeclarativeExpression.error()'''
        return QDeclarativeError()
    def clearError(self):
        '''void QDeclarativeExpression.clearError()'''
    def hasError(self):
        '''bool QDeclarativeExpression.hasError()'''
        return bool()
    def scopeObject(self):
        '''QObject QDeclarativeExpression.scopeObject()'''
        return QObject()
    def setSourceLocation(self, fileName, line):
        '''void QDeclarativeExpression.setSourceLocation(QString fileName, int line)'''
    def lineNumber(self):
        '''int QDeclarativeExpression.lineNumber()'''
        return int()
    def sourceFile(self):
        '''QString QDeclarativeExpression.sourceFile()'''
        return QString()
    def setNotifyOnValueChanged(self):
        '''bool QDeclarativeExpression.setNotifyOnValueChanged()'''
        return bool()
    def notifyOnValueChanged(self):
        '''bool QDeclarativeExpression.notifyOnValueChanged()'''
        return bool()
    def setExpression(self):
        '''QString QDeclarativeExpression.setExpression()'''
        return QString()
    def expression(self):
        '''QString QDeclarativeExpression.expression()'''
        return QString()
    def context(self):
        '''QDeclarativeContext QDeclarativeExpression.context()'''
        return QDeclarativeContext()
    def engine(self):
        '''QDeclarativeEngine QDeclarativeExpression.engine()'''
        return QDeclarativeEngine()


class QDeclarativeExtensionPlugin(QObject):
    """"""
    def __init__(self, parent = None):
        '''void QDeclarativeExtensionPlugin.__init__(QObject parent = None)'''
    def initializeEngine(self, engine, uri):
        '''void QDeclarativeExtensionPlugin.initializeEngine(QDeclarativeEngine engine, str uri)'''
    def registerTypes(self, uri):
        '''abstract void QDeclarativeExtensionPlugin.registerTypes(str uri)'''


class QDeclarativeImageProvider():
    """"""
    # Enum QDeclarativeImageProvider.ImageType
    Image = 0
    Pixmap = 0

    def __init__(self, type):
        '''void QDeclarativeImageProvider.__init__(QDeclarativeImageProvider.ImageType type)'''
    def __init__(self):
        '''QDeclarativeImageProvider QDeclarativeImageProvider.__init__()'''
        return QDeclarativeImageProvider()
    def requestPixmap(self, id, size, requestedSize):
        '''QPixmap QDeclarativeImageProvider.requestPixmap(QString id, QSize size, QSize requestedSize)'''
        return QPixmap()
    def requestImage(self, id, size, requestedSize):
        '''QImage QDeclarativeImageProvider.requestImage(QString id, QSize size, QSize requestedSize)'''
        return QImage()
    def imageType(self):
        '''QDeclarativeImageProvider.ImageType QDeclarativeImageProvider.imageType()'''
        return QDeclarativeImageProvider.ImageType()


class QDeclarativeParserStatus():
    """"""
    def __init__(self):
        '''void QDeclarativeParserStatus.__init__()'''
    def __init__(self):
        '''QDeclarativeParserStatus QDeclarativeParserStatus.__init__()'''
        return QDeclarativeParserStatus()
    def componentComplete(self):
        '''abstract void QDeclarativeParserStatus.componentComplete()'''
    def classBegin(self):
        '''abstract void QDeclarativeParserStatus.classBegin()'''


class QDeclarativeItem(QGraphicsObject, QDeclarativeParserStatus):
    """"""
    # Enum QDeclarativeItem.TransformOrigin
    TopLeft = 0
    Top = 0
    TopRight = 0
    Left = 0
    Center = 0
    Right = 0
    BottomLeft = 0
    Bottom = 0
    BottomRight = 0

    def __init__(self, parent = None):
        '''void QDeclarativeItem.__init__(QDeclarativeItem parent = None)'''
    def geometryChanged(self, newGeometry, oldGeometry):
        '''void QDeclarativeItem.geometryChanged(QRectF newGeometry, QRectF oldGeometry)'''
    def inputMethodQuery(self, query):
        '''QVariant QDeclarativeItem.inputMethodQuery(Qt.InputMethodQuery query)'''
        return QVariant()
    def inputMethodEvent(self):
        '''QInputMethodEvent QDeclarativeItem.inputMethodEvent()'''
        return QInputMethodEvent()
    def keyReleaseEvent(self, event):
        '''void QDeclarativeItem.keyReleaseEvent(QKeyEvent event)'''
    def keyPressEvent(self, event):
        '''void QDeclarativeItem.keyPressEvent(QKeyEvent event)'''
    def componentComplete(self):
        '''void QDeclarativeItem.componentComplete()'''
    def classBegin(self):
        '''void QDeclarativeItem.classBegin()'''
    def heightValid(self):
        '''bool QDeclarativeItem.heightValid()'''
        return bool()
    def setImplicitHeight(self):
        '''float QDeclarativeItem.setImplicitHeight()'''
        return float()
    def widthValid(self):
        '''bool QDeclarativeItem.widthValid()'''
        return bool()
    def setImplicitWidth(self):
        '''float QDeclarativeItem.setImplicitWidth()'''
        return float()
    def itemChange(self):
        '''QVariant QDeclarativeItem.itemChange()'''
        return QVariant()
    def event(self):
        '''QEvent QDeclarativeItem.event()'''
        return QEvent()
    def sceneEvent(self):
        '''QEvent QDeclarativeItem.sceneEvent()'''
        return QEvent()
    def isComponentComplete(self):
        '''bool QDeclarativeItem.isComponentComplete()'''
        return bool()
    def setKeepMouseGrab(self):
        '''bool QDeclarativeItem.setKeepMouseGrab()'''
        return bool()
    def keepMouseGrab(self):
        '''bool QDeclarativeItem.keepMouseGrab()'''
        return bool()
    def hasFocus(self):
        '''bool QDeclarativeItem.hasFocus()'''
        return bool()
    def paint(self):
        '''QWidget QDeclarativeItem.paint()'''
        return QWidget()
    def boundingRect(self):
        '''QRectF QDeclarativeItem.boundingRect()'''
        return QRectF()
    def setSmooth(self):
        '''bool QDeclarativeItem.setSmooth()'''
        return bool()
    def smooth(self):
        '''bool QDeclarativeItem.smooth()'''
        return bool()
    def setTransformOrigin(self):
        '''QDeclarativeItem.TransformOrigin QDeclarativeItem.setTransformOrigin()'''
        return QDeclarativeItem.TransformOrigin()
    def transformOrigin(self):
        '''QDeclarativeItem.TransformOrigin QDeclarativeItem.transformOrigin()'''
        return QDeclarativeItem.TransformOrigin()
    def implicitHeight(self):
        '''float QDeclarativeItem.implicitHeight()'''
        return float()
    def setHeight(self):
        '''float QDeclarativeItem.setHeight()'''
        return float()
    def implicitWidth(self):
        '''float QDeclarativeItem.implicitWidth()'''
        return float()
    def setWidth(self):
        '''float QDeclarativeItem.setWidth()'''
        return float()
    def setBaselineOffset(self):
        '''float QDeclarativeItem.setBaselineOffset()'''
        return float()
    def baselineOffset(self):
        '''float QDeclarativeItem.baselineOffset()'''
        return float()
    def setClip(self):
        '''bool QDeclarativeItem.setClip()'''
        return bool()
    def clip(self):
        '''bool QDeclarativeItem.clip()'''
        return bool()
    def childrenRect(self):
        '''QRectF QDeclarativeItem.childrenRect()'''
        return QRectF()
    def setParentItem(self, parent):
        '''void QDeclarativeItem.setParentItem(QDeclarativeItem parent)'''
    def parentItem(self):
        '''QDeclarativeItem QDeclarativeItem.parentItem()'''
        return QDeclarativeItem()


class QDeclarativeListReference():
    """"""
    def __init__(self):
        '''void QDeclarativeListReference.__init__()'''
    def __init__(self, property, engine = None):
        '''QObject QDeclarativeListReference.__init__(str property, QDeclarativeEngine engine = None)'''
        return QObject()
    def __init__(self):
        '''QDeclarativeListReference QDeclarativeListReference.__init__()'''
        return QDeclarativeListReference()
    def count(self):
        '''int QDeclarativeListReference.count()'''
        return int()
    def clear(self):
        '''bool QDeclarativeListReference.clear()'''
        return bool()
    def at(self):
        '''int QDeclarativeListReference.at()'''
        return int()
    def append(self):
        '''QObject QDeclarativeListReference.append()'''
        return QObject()
    def canCount(self):
        '''bool QDeclarativeListReference.canCount()'''
        return bool()
    def canClear(self):
        '''bool QDeclarativeListReference.canClear()'''
        return bool()
    def canAt(self):
        '''bool QDeclarativeListReference.canAt()'''
        return bool()
    def canAppend(self):
        '''bool QDeclarativeListReference.canAppend()'''
        return bool()
    def listElementType(self):
        '''QMetaObject QDeclarativeListReference.listElementType()'''
        return QMetaObject()
    def object(self):
        '''QObject QDeclarativeListReference.object()'''
        return QObject()
    def isValid(self):
        '''bool QDeclarativeListReference.isValid()'''
        return bool()


class QDeclarativeNetworkAccessManagerFactory():
    """"""
    def __init__(self):
        '''void QDeclarativeNetworkAccessManagerFactory.__init__()'''
    def __init__(self):
        '''QDeclarativeNetworkAccessManagerFactory QDeclarativeNetworkAccessManagerFactory.__init__()'''
        return QDeclarativeNetworkAccessManagerFactory()
    def create(self, parent):
        '''abstract QNetworkAccessManager QDeclarativeNetworkAccessManagerFactory.create(QObject parent)'''
        return QNetworkAccessManager()


class QDeclarativeProperty():
    """"""
    # Enum QDeclarativeProperty.Type
    Invalid = 0
    Property = 0
    SignalProperty = 0

    # Enum QDeclarativeProperty.PropertyTypeCategory
    InvalidCategory = 0
    List = 0
    Object = 0
    Normal = 0

    def __init__(self):
        '''void QDeclarativeProperty.__init__()'''
    def __init__(self):
        '''QObject QDeclarativeProperty.__init__()'''
        return QObject()
    def __init__(self):
        '''QDeclarativeContext QDeclarativeProperty.__init__()'''
        return QDeclarativeContext()
    def __init__(self):
        '''QDeclarativeEngine QDeclarativeProperty.__init__()'''
        return QDeclarativeEngine()
    def __init__(self):
        '''QString QDeclarativeProperty.__init__()'''
        return QString()
    def __init__(self):
        '''QDeclarativeContext QDeclarativeProperty.__init__()'''
        return QDeclarativeContext()
    def __init__(self):
        '''QDeclarativeEngine QDeclarativeProperty.__init__()'''
        return QDeclarativeEngine()
    def __init__(self):
        '''QDeclarativeProperty QDeclarativeProperty.__init__()'''
        return QDeclarativeProperty()
    def __ne__(self):
        '''QDeclarativeProperty QDeclarativeProperty.__ne__()'''
        return QDeclarativeProperty()
    def __hash__(self):
        '''int QDeclarativeProperty.__hash__()'''
        return int()
    def method(self):
        '''QMetaMethod QDeclarativeProperty.method()'''
        return QMetaMethod()
    def property(self):
        '''QMetaProperty QDeclarativeProperty.property()'''
        return QMetaProperty()
    def index(self):
        '''int QDeclarativeProperty.index()'''
        return int()
    def object(self):
        '''QObject QDeclarativeProperty.object()'''
        return QObject()
    def isResettable(self):
        '''bool QDeclarativeProperty.isResettable()'''
        return bool()
    def isDesignable(self):
        '''bool QDeclarativeProperty.isDesignable()'''
        return bool()
    def isWritable(self):
        '''bool QDeclarativeProperty.isWritable()'''
        return bool()
    def connectNotifySignal(self, dest, slot):
        '''bool QDeclarativeProperty.connectNotifySignal(QObject dest, SLOT() slot)'''
        return bool()
    def connectNotifySignal(self, dest):
        '''bool QDeclarativeProperty.connectNotifySignal(callable dest)'''
        return bool()
    def connectNotifySignal(self, dest, method):
        '''bool QDeclarativeProperty.connectNotifySignal(QObject dest, int method)'''
        return bool()
    def needsNotifySignal(self):
        '''bool QDeclarativeProperty.needsNotifySignal()'''
        return bool()
    def hasNotifySignal(self):
        '''bool QDeclarativeProperty.hasNotifySignal()'''
        return bool()
    def reset(self):
        '''bool QDeclarativeProperty.reset()'''
        return bool()
    def write(self):
        '''QVariant QDeclarativeProperty.write()'''
        return QVariant()
    def write(self):
        '''static QVariant QDeclarativeProperty.write()'''
        return QVariant()
    def write(self):
        '''static QDeclarativeContext QDeclarativeProperty.write()'''
        return QDeclarativeContext()
    def write(self):
        '''static QDeclarativeEngine QDeclarativeProperty.write()'''
        return QDeclarativeEngine()
    def read(self):
        '''QVariant QDeclarativeProperty.read()'''
        return QVariant()
    def read(self):
        '''static QString QDeclarativeProperty.read()'''
        return QString()
    def read(self):
        '''static QDeclarativeContext QDeclarativeProperty.read()'''
        return QDeclarativeContext()
    def read(self):
        '''static QDeclarativeEngine QDeclarativeProperty.read()'''
        return QDeclarativeEngine()
    def name(self):
        '''QString QDeclarativeProperty.name()'''
        return QString()
    def propertyTypeName(self):
        '''str QDeclarativeProperty.propertyTypeName()'''
        return str()
    def propertyTypeCategory(self):
        '''QDeclarativeProperty.PropertyTypeCategory QDeclarativeProperty.propertyTypeCategory()'''
        return QDeclarativeProperty.PropertyTypeCategory()
    def propertyType(self):
        '''int QDeclarativeProperty.propertyType()'''
        return int()
    def isSignalProperty(self):
        '''bool QDeclarativeProperty.isSignalProperty()'''
        return bool()
    def isProperty(self):
        '''bool QDeclarativeProperty.isProperty()'''
        return bool()
    def isValid(self):
        '''bool QDeclarativeProperty.isValid()'''
        return bool()
    def type(self):
        '''QDeclarativeProperty.Type QDeclarativeProperty.type()'''
        return QDeclarativeProperty.Type()
    def __eq__(self):
        '''QDeclarativeProperty QDeclarativeProperty.__eq__()'''
        return QDeclarativeProperty()


class QDeclarativePropertyMap(QObject):
    """"""
    def __init__(self, parent = None):
        '''void QDeclarativePropertyMap.__init__(QObject parent = None)'''
    valueChanged = pyqtSignal() # void valueChanged(const QStringamp;,const QVariantamp;) - signal
    def __getitem__(self, key):
        '''QVariant QDeclarativePropertyMap.__getitem__(QString key)'''
        return QVariant()
    def contains(self, key):
        '''bool QDeclarativePropertyMap.contains(QString key)'''
        return bool()
    def isEmpty(self):
        '''bool QDeclarativePropertyMap.isEmpty()'''
        return bool()
    def size(self):
        '''int QDeclarativePropertyMap.size()'''
        return int()
    def __len__(self):
        '''None QDeclarativePropertyMap.__len__()'''
        return None()
    def count(self):
        '''int QDeclarativePropertyMap.count()'''
        return int()
    def keys(self):
        '''QStringList QDeclarativePropertyMap.keys()'''
        return QStringList()
    def clear(self, key):
        '''void QDeclarativePropertyMap.clear(QString key)'''
    def insert(self, key, value):
        '''void QDeclarativePropertyMap.insert(QString key, QVariant value)'''
    def value(self, key):
        '''QVariant QDeclarativePropertyMap.value(QString key)'''
        return QVariant()


class QDeclarativePropertyValueSource():
    """"""
    def __init__(self):
        '''void QDeclarativePropertyValueSource.__init__()'''
    def __init__(self):
        '''QDeclarativePropertyValueSource QDeclarativePropertyValueSource.__init__()'''
        return QDeclarativePropertyValueSource()
    def setTarget(self):
        '''abstract QDeclarativeProperty QDeclarativePropertyValueSource.setTarget()'''
        return QDeclarativeProperty()


class QDeclarativeScriptString():
    """"""
    def __init__(self):
        '''void QDeclarativeScriptString.__init__()'''
    def __init__(self):
        '''QDeclarativeScriptString QDeclarativeScriptString.__init__()'''
        return QDeclarativeScriptString()
    def setScript(self):
        '''QString QDeclarativeScriptString.setScript()'''
        return QString()
    def script(self):
        '''QString QDeclarativeScriptString.script()'''
        return QString()
    def setScopeObject(self):
        '''QObject QDeclarativeScriptString.setScopeObject()'''
        return QObject()
    def scopeObject(self):
        '''QObject QDeclarativeScriptString.scopeObject()'''
        return QObject()
    def setContext(self):
        '''QDeclarativeContext QDeclarativeScriptString.setContext()'''
        return QDeclarativeContext()
    def context(self):
        '''QDeclarativeContext QDeclarativeScriptString.context()'''
        return QDeclarativeContext()


class QDeclarativeView(QGraphicsView):
    """"""
    # Enum QDeclarativeView.Status
    Null = 0
    Ready = 0
    Loading = 0
    Error = 0

    # Enum QDeclarativeView.ResizeMode
    SizeViewToRootObject = 0
    SizeRootObjectToView = 0

    def __init__(self, parent = None):
        '''void QDeclarativeView.__init__(QWidget parent = None)'''
    def __init__(self, source, parent = None):
        '''void QDeclarativeView.__init__(QUrl source, QWidget parent = None)'''
    def eventFilter(self, watched, e):
        '''bool QDeclarativeView.eventFilter(QObject watched, QEvent e)'''
        return bool()
    def timerEvent(self):
        '''QTimerEvent QDeclarativeView.timerEvent()'''
        return QTimerEvent()
    def paintEvent(self, event):
        '''void QDeclarativeView.paintEvent(QPaintEvent event)'''
    def resizeEvent(self):
        '''QResizeEvent QDeclarativeView.resizeEvent()'''
        return QResizeEvent()
    statusChanged = pyqtSignal() # void statusChanged(QDeclarativeView::Status) - signal
    sceneResized = pyqtSignal() # void sceneResized(QSize) - signal
    def initialSize(self):
        '''QSize QDeclarativeView.initialSize()'''
        return QSize()
    def sizeHint(self):
        '''QSize QDeclarativeView.sizeHint()'''
        return QSize()
    def errors(self):
        '''list-of-QDeclarativeError QDeclarativeView.errors()'''
        return [QDeclarativeError()]
    def status(self):
        '''QDeclarativeView.Status QDeclarativeView.status()'''
        return QDeclarativeView.Status()
    def setResizeMode(self):
        '''QDeclarativeView.ResizeMode QDeclarativeView.setResizeMode()'''
        return QDeclarativeView.ResizeMode()
    def resizeMode(self):
        '''QDeclarativeView.ResizeMode QDeclarativeView.resizeMode()'''
        return QDeclarativeView.ResizeMode()
    def rootObject(self):
        '''QGraphicsObject QDeclarativeView.rootObject()'''
        return QGraphicsObject()
    def rootContext(self):
        '''QDeclarativeContext QDeclarativeView.rootContext()'''
        return QDeclarativeContext()
    def engine(self):
        '''QDeclarativeEngine QDeclarativeView.engine()'''
        return QDeclarativeEngine()
    def setSource(self):
        '''QUrl QDeclarativeView.setSource()'''
        return QUrl()
    def source(self):
        '''QUrl QDeclarativeView.source()'''
        return QUrl()


class QPyDeclarativePropertyValueSource(QObject, QDeclarativePropertyValueSource):
    """"""
    def __init__(self, parent = None):
        '''void QPyDeclarativePropertyValueSource.__init__(QObject parent = None)'''


