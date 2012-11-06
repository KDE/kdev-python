class pyqtSignal():
 def connect(self, targetSignal): pass
 def emit(self, *args): pass
from QtCore import *

class QAbstractMessageHandler(QObject):
    """"""
    def __init__(self, parent = None):
        '''void QAbstractMessageHandler.__init__(QObject parent = None)'''
    def handleMessage(self, type, description, identifier, sourceLocation):
        '''abstract void QAbstractMessageHandler.handleMessage(QtMsgType type, QString description, QUrl identifier, QSourceLocation sourceLocation)'''
    def message(self, type, description, identifier = QUrl(), sourceLocation = QSourceLocation()):
        '''void QAbstractMessageHandler.message(QtMsgType type, QString description, QUrl identifier = QUrl(), QSourceLocation sourceLocation = QSourceLocation())'''


class QAbstractUriResolver(QObject):
    """"""
    def __init__(self, parent = None):
        '''void QAbstractUriResolver.__init__(QObject parent = None)'''
    def resolve(self, relative, baseURI):
        '''abstract QUrl QAbstractUriResolver.resolve(QUrl relative, QUrl baseURI)'''
        return QUrl()


class QXmlNodeModelIndex():
    """"""
    # Enum QXmlNodeModelIndex.DocumentOrder
    Precedes = 0
    Is = 0
    Follows = 0

    # Enum QXmlNodeModelIndex.NodeKind
    Attribute = 0
    Comment = 0
    Document = 0
    Element = 0
    Namespace = 0
    ProcessingInstruction = 0
    Text = 0

    def __init__(self):
        '''void QXmlNodeModelIndex.__init__()'''
    def __init__(self, other):
        '''void QXmlNodeModelIndex.__init__(QXmlNodeModelIndex other)'''
    def __hash__(self):
        '''int QXmlNodeModelIndex.__hash__()'''
        return int()
    def isNull(self):
        '''bool QXmlNodeModelIndex.isNull()'''
        return bool()
    def additionalData(self):
        '''int QXmlNodeModelIndex.additionalData()'''
        return int()
    def model(self):
        '''QAbstractXmlNodeModel QXmlNodeModelIndex.model()'''
        return QAbstractXmlNodeModel()
    def internalPointer(self):
        '''object QXmlNodeModelIndex.internalPointer()'''
        return object()
    def data(self):
        '''int QXmlNodeModelIndex.data()'''
        return int()
    def __ne__(self, other):
        '''bool QXmlNodeModelIndex.__ne__(QXmlNodeModelIndex other)'''
        return bool()
    def __eq__(self, other):
        '''bool QXmlNodeModelIndex.__eq__(QXmlNodeModelIndex other)'''
        return bool()


class QAbstractXmlNodeModel():
    """"""
    # Enum QAbstractXmlNodeModel.SimpleAxis
    Parent = 0
    FirstChild = 0
    PreviousSibling = 0
    NextSibling = 0

    def __init__(self):
        '''void QAbstractXmlNodeModel.__init__()'''
    def createIndex(self, data):
        '''QXmlNodeModelIndex QAbstractXmlNodeModel.createIndex(int data)'''
        return QXmlNodeModelIndex()
    def createIndex(self, data, additionalData):
        '''QXmlNodeModelIndex QAbstractXmlNodeModel.createIndex(int data, int additionalData)'''
        return QXmlNodeModelIndex()
    def createIndex(self, pointer, additionalData = 0):
        '''QXmlNodeModelIndex QAbstractXmlNodeModel.createIndex(object pointer, int additionalData = 0)'''
        return QXmlNodeModelIndex()
    def attributes(self, element):
        '''abstract list-of-QXmlNodeModelIndex QAbstractXmlNodeModel.attributes(QXmlNodeModelIndex element)'''
        return [QXmlNodeModelIndex()]
    def nextFromSimpleAxis(self, axis, origin):
        '''abstract QXmlNodeModelIndex QAbstractXmlNodeModel.nextFromSimpleAxis(QAbstractXmlNodeModel.SimpleAxis axis, QXmlNodeModelIndex origin)'''
        return QXmlNodeModelIndex()
    def sourceLocation(self, index):
        '''QSourceLocation QAbstractXmlNodeModel.sourceLocation(QXmlNodeModelIndex index)'''
        return QSourceLocation()
    def nodesByIdref(self, NCName):
        '''abstract list-of-QXmlNodeModelIndex QAbstractXmlNodeModel.nodesByIdref(QXmlName NCName)'''
        return [QXmlNodeModelIndex()]
    def elementById(self, NCName):
        '''abstract QXmlNodeModelIndex QAbstractXmlNodeModel.elementById(QXmlName NCName)'''
        return QXmlNodeModelIndex()
    def namespaceBindings(self, n):
        '''abstract list-of-QXmlName QAbstractXmlNodeModel.namespaceBindings(QXmlNodeModelIndex n)'''
        return [QXmlName()]
    def typedValue(self, n):
        '''abstract QVariant QAbstractXmlNodeModel.typedValue(QXmlNodeModelIndex n)'''
        return QVariant()
    def stringValue(self, n):
        '''abstract QString QAbstractXmlNodeModel.stringValue(QXmlNodeModelIndex n)'''
        return QString()
    def name(self, ni):
        '''abstract QXmlName QAbstractXmlNodeModel.name(QXmlNodeModelIndex ni)'''
        return QXmlName()
    def root(self, n):
        '''abstract QXmlNodeModelIndex QAbstractXmlNodeModel.root(QXmlNodeModelIndex n)'''
        return QXmlNodeModelIndex()
    def compareOrder(self, ni1, ni2):
        '''abstract QXmlNodeModelIndex.DocumentOrder QAbstractXmlNodeModel.compareOrder(QXmlNodeModelIndex ni1, QXmlNodeModelIndex ni2)'''
        return QXmlNodeModelIndex.DocumentOrder()
    def kind(self, ni):
        '''abstract QXmlNodeModelIndex.NodeKind QAbstractXmlNodeModel.kind(QXmlNodeModelIndex ni)'''
        return QXmlNodeModelIndex.NodeKind()
    def documentUri(self, ni):
        '''abstract QUrl QAbstractXmlNodeModel.documentUri(QXmlNodeModelIndex ni)'''
        return QUrl()
    def baseUri(self, ni):
        '''abstract QUrl QAbstractXmlNodeModel.baseUri(QXmlNodeModelIndex ni)'''
        return QUrl()


class QXmlItem():
    """"""
    def __init__(self):
        '''void QXmlItem.__init__()'''
    def __init__(self, other):
        '''void QXmlItem.__init__(QXmlItem other)'''
    def __init__(self, node):
        '''void QXmlItem.__init__(QXmlNodeModelIndex node)'''
    def __init__(self, atomicValue):
        '''void QXmlItem.__init__(QVariant atomicValue)'''
    def toNodeModelIndex(self):
        '''QXmlNodeModelIndex QXmlItem.toNodeModelIndex()'''
        return QXmlNodeModelIndex()
    def toAtomicValue(self):
        '''QVariant QXmlItem.toAtomicValue()'''
        return QVariant()
    def isAtomicValue(self):
        '''bool QXmlItem.isAtomicValue()'''
        return bool()
    def isNode(self):
        '''bool QXmlItem.isNode()'''
        return bool()
    def isNull(self):
        '''bool QXmlItem.isNull()'''
        return bool()


class QAbstractXmlReceiver():
    """"""
    def __init__(self):
        '''void QAbstractXmlReceiver.__init__()'''
    def endOfSequence(self):
        '''abstract void QAbstractXmlReceiver.endOfSequence()'''
    def startOfSequence(self):
        '''abstract void QAbstractXmlReceiver.startOfSequence()'''
    def namespaceBinding(self, name):
        '''abstract void QAbstractXmlReceiver.namespaceBinding(QXmlName name)'''
    def atomicValue(self, value):
        '''abstract void QAbstractXmlReceiver.atomicValue(QVariant value)'''
    def processingInstruction(self, target, value):
        '''abstract void QAbstractXmlReceiver.processingInstruction(QXmlName target, QString value)'''
    def endDocument(self):
        '''abstract void QAbstractXmlReceiver.endDocument()'''
    def startDocument(self):
        '''abstract void QAbstractXmlReceiver.startDocument()'''
    def characters(self, value):
        '''abstract void QAbstractXmlReceiver.characters(QStringRef value)'''
    def comment(self, value):
        '''abstract void QAbstractXmlReceiver.comment(QString value)'''
    def attribute(self, name, value):
        '''abstract void QAbstractXmlReceiver.attribute(QXmlName name, QStringRef value)'''
    def endElement(self):
        '''abstract void QAbstractXmlReceiver.endElement()'''
    def startElement(self, name):
        '''abstract void QAbstractXmlReceiver.startElement(QXmlName name)'''


class QSimpleXmlNodeModel(QAbstractXmlNodeModel):
    """"""
    def __init__(self, namePool):
        '''void QSimpleXmlNodeModel.__init__(QXmlNamePool namePool)'''
    def nodesByIdref(self, idref):
        '''list-of-QXmlNodeModelIndex QSimpleXmlNodeModel.nodesByIdref(QXmlName idref)'''
        return [QXmlNodeModelIndex()]
    def elementById(self, id):
        '''QXmlNodeModelIndex QSimpleXmlNodeModel.elementById(QXmlName id)'''
        return QXmlNodeModelIndex()
    def stringValue(self, node):
        '''QString QSimpleXmlNodeModel.stringValue(QXmlNodeModelIndex node)'''
        return QString()
    def namespaceBindings(self):
        '''QXmlNodeModelIndex QSimpleXmlNodeModel.namespaceBindings()'''
        return QXmlNodeModelIndex()
    def namePool(self):
        '''QXmlNamePool QSimpleXmlNodeModel.namePool()'''
        return QXmlNamePool()
    def baseUri(self, node):
        '''QUrl QSimpleXmlNodeModel.baseUri(QXmlNodeModelIndex node)'''
        return QUrl()


class QSourceLocation():
    """"""
    def __init__(self):
        '''void QSourceLocation.__init__()'''
    def __init__(self, other):
        '''void QSourceLocation.__init__(QSourceLocation other)'''
    def __init__(self, u, line = None, column = None):
        '''void QSourceLocation.__init__(QUrl u, int line = -1, int column = -1)'''
    def __hash__(self):
        '''int QSourceLocation.__hash__()'''
        return int()
    def isNull(self):
        '''bool QSourceLocation.isNull()'''
        return bool()
    def setUri(self, newUri):
        '''void QSourceLocation.setUri(QUrl newUri)'''
    def uri(self):
        '''QUrl QSourceLocation.uri()'''
        return QUrl()
    def setLine(self, newLine):
        '''void QSourceLocation.setLine(int newLine)'''
    def line(self):
        '''int QSourceLocation.line()'''
        return int()
    def setColumn(self, newColumn):
        '''void QSourceLocation.setColumn(int newColumn)'''
    def column(self):
        '''int QSourceLocation.column()'''
        return int()
    def __ne__(self, other):
        '''bool QSourceLocation.__ne__(QSourceLocation other)'''
        return bool()
    def __eq__(self, other):
        '''bool QSourceLocation.__eq__(QSourceLocation other)'''
        return bool()


class QXmlSerializer(QAbstractXmlReceiver):
    """"""
    def __init__(self, query, outputDevice):
        '''void QXmlSerializer.__init__(QXmlQuery query, QIODevice outputDevice)'''
    def codec(self):
        '''QTextCodec QXmlSerializer.codec()'''
        return QTextCodec()
    def setCodec(self, codec):
        '''void QXmlSerializer.setCodec(QTextCodec codec)'''
    def outputDevice(self):
        '''QIODevice QXmlSerializer.outputDevice()'''
        return QIODevice()
    def endOfSequence(self):
        '''void QXmlSerializer.endOfSequence()'''
    def startOfSequence(self):
        '''void QXmlSerializer.startOfSequence()'''
    def endDocument(self):
        '''void QXmlSerializer.endDocument()'''
    def startDocument(self):
        '''void QXmlSerializer.startDocument()'''
    def atomicValue(self, value):
        '''void QXmlSerializer.atomicValue(QVariant value)'''
    def processingInstruction(self, name, value):
        '''void QXmlSerializer.processingInstruction(QXmlName name, QString value)'''
    def attribute(self, name, value):
        '''void QXmlSerializer.attribute(QXmlName name, QStringRef value)'''
    def endElement(self):
        '''void QXmlSerializer.endElement()'''
    def startElement(self, name):
        '''void QXmlSerializer.startElement(QXmlName name)'''
    def comment(self, value):
        '''void QXmlSerializer.comment(QString value)'''
    def characters(self, value):
        '''void QXmlSerializer.characters(QStringRef value)'''
    def namespaceBinding(self, nb):
        '''void QXmlSerializer.namespaceBinding(QXmlName nb)'''


class QXmlFormatter(QXmlSerializer):
    """"""
    def __init__(self, query, outputDevice):
        '''void QXmlFormatter.__init__(QXmlQuery query, QIODevice outputDevice)'''
    def setIndentationDepth(self, depth):
        '''void QXmlFormatter.setIndentationDepth(int depth)'''
    def indentationDepth(self):
        '''int QXmlFormatter.indentationDepth()'''
        return int()
    def endOfSequence(self):
        '''void QXmlFormatter.endOfSequence()'''
    def startOfSequence(self):
        '''void QXmlFormatter.startOfSequence()'''
    def endDocument(self):
        '''void QXmlFormatter.endDocument()'''
    def startDocument(self):
        '''void QXmlFormatter.startDocument()'''
    def atomicValue(self, value):
        '''void QXmlFormatter.atomicValue(QVariant value)'''
    def processingInstruction(self, name, value):
        '''void QXmlFormatter.processingInstruction(QXmlName name, QString value)'''
    def attribute(self, name, value):
        '''void QXmlFormatter.attribute(QXmlName name, QStringRef value)'''
    def endElement(self):
        '''void QXmlFormatter.endElement()'''
    def startElement(self, name):
        '''void QXmlFormatter.startElement(QXmlName name)'''
    def comment(self, value):
        '''void QXmlFormatter.comment(QString value)'''
    def characters(self, value):
        '''void QXmlFormatter.characters(QStringRef value)'''


class QXmlName():
    """"""
    def __init__(self):
        '''void QXmlName.__init__()'''
    def __init__(self, namePool, localName, namespaceUri = QString(), prefix = QString()):
        '''void QXmlName.__init__(QXmlNamePool namePool, QString localName, QString namespaceUri = QString(), QString prefix = QString())'''
    def __init__(self):
        '''QXmlName QXmlName.__init__()'''
        return QXmlName()
    def __hash__(self):
        '''int QXmlName.__hash__()'''
        return int()
    def fromClarkName(self, clarkName, namePool):
        '''static QXmlName QXmlName.fromClarkName(QString clarkName, QXmlNamePool namePool)'''
        return QXmlName()
    def isNCName(self, candidate):
        '''static bool QXmlName.isNCName(QString candidate)'''
        return bool()
    def isNull(self):
        '''bool QXmlName.isNull()'''
        return bool()
    def __ne__(self, other):
        '''bool QXmlName.__ne__(QXmlName other)'''
        return bool()
    def __eq__(self, other):
        '''bool QXmlName.__eq__(QXmlName other)'''
        return bool()
    def toClarkName(self, query):
        '''QString QXmlName.toClarkName(QXmlNamePool query)'''
        return QString()
    def localName(self, query):
        '''QString QXmlName.localName(QXmlNamePool query)'''
        return QString()
    def prefix(self, query):
        '''QString QXmlName.prefix(QXmlNamePool query)'''
        return QString()
    def namespaceUri(self, query):
        '''QString QXmlName.namespaceUri(QXmlNamePool query)'''
        return QString()


class QXmlNamePool():
    """"""
    def __init__(self):
        '''void QXmlNamePool.__init__()'''
    def __init__(self, other):
        '''void QXmlNamePool.__init__(QXmlNamePool other)'''


class QXmlQuery():
    """"""
    # Enum QXmlQuery.QueryLanguage
    XQuery10 = 0
    XSLT20 = 0

    def __init__(self):
        '''void QXmlQuery.__init__()'''
    def __init__(self, other):
        '''void QXmlQuery.__init__(QXmlQuery other)'''
    def __init__(self, np):
        '''void QXmlQuery.__init__(QXmlNamePool np)'''
    def __init__(self, queryLanguage, pool = QXmlNamePool()):
        '''void QXmlQuery.__init__(QXmlQuery.QueryLanguage queryLanguage, QXmlNamePool pool = QXmlNamePool())'''
    def queryLanguage(self):
        '''QXmlQuery.QueryLanguage QXmlQuery.queryLanguage()'''
        return QXmlQuery.QueryLanguage()
    def networkAccessManager(self):
        '''QNetworkAccessManager QXmlQuery.networkAccessManager()'''
        return QNetworkAccessManager()
    def setNetworkAccessManager(self, newManager):
        '''void QXmlQuery.setNetworkAccessManager(QNetworkAccessManager newManager)'''
    def initialTemplateName(self):
        '''QXmlName QXmlQuery.initialTemplateName()'''
        return QXmlName()
    def setInitialTemplateName(self, name):
        '''void QXmlQuery.setInitialTemplateName(QXmlName name)'''
    def setInitialTemplateName(self, name):
        '''void QXmlQuery.setInitialTemplateName(QString name)'''
    def setFocus(self, item):
        '''void QXmlQuery.setFocus(QXmlItem item)'''
    def setFocus(self, documentURI):
        '''bool QXmlQuery.setFocus(QUrl documentURI)'''
        return bool()
    def setFocus(self, document):
        '''bool QXmlQuery.setFocus(QIODevice document)'''
        return bool()
    def setFocus(self, focus):
        '''bool QXmlQuery.setFocus(QString focus)'''
        return bool()
    def uriResolver(self):
        '''QAbstractUriResolver QXmlQuery.uriResolver()'''
        return QAbstractUriResolver()
    def setUriResolver(self, resolver):
        '''void QXmlQuery.setUriResolver(QAbstractUriResolver resolver)'''
    def evaluateToString(self):
        '''QString QXmlQuery.evaluateToString()'''
        return QString()
    def evaluateToStringList(self):
        '''QStringList QXmlQuery.evaluateToStringList()'''
        return QStringList()
    def evaluateTo(self, result):
        '''void QXmlQuery.evaluateTo(QXmlResultItems result)'''
    def evaluateTo(self, callback):
        '''bool QXmlQuery.evaluateTo(QAbstractXmlReceiver callback)'''
        return bool()
    def evaluateTo(self, target):
        '''bool QXmlQuery.evaluateTo(QStringList target)'''
        return bool()
    def evaluateTo(self, target):
        '''bool QXmlQuery.evaluateTo(QIODevice target)'''
        return bool()
    def evaluateTo(self, output):
        '''bool QXmlQuery.evaluateTo(QString output)'''
        return bool()
    def isValid(self):
        '''bool QXmlQuery.isValid()'''
        return bool()
    def bindVariable(self, name, value):
        '''void QXmlQuery.bindVariable(QXmlName name, QXmlItem value)'''
    def bindVariable(self, name):
        '''QIODevice QXmlQuery.bindVariable(QXmlName name)'''
        return QIODevice()
    def bindVariable(self, name, query):
        '''void QXmlQuery.bindVariable(QXmlName name, QXmlQuery query)'''
    def bindVariable(self, localName, value):
        '''void QXmlQuery.bindVariable(QString localName, QXmlItem value)'''
    def bindVariable(self, localName):
        '''QIODevice QXmlQuery.bindVariable(QString localName)'''
        return QIODevice()
    def bindVariable(self, localName, query):
        '''void QXmlQuery.bindVariable(QString localName, QXmlQuery query)'''
    def namePool(self):
        '''QXmlNamePool QXmlQuery.namePool()'''
        return QXmlNamePool()
    def setQuery(self, sourceCode, documentUri = QUrl()):
        '''void QXmlQuery.setQuery(QString sourceCode, QUrl documentUri = QUrl())'''
    def setQuery(self, sourceCode, documentUri = QUrl()):
        '''void QXmlQuery.setQuery(QIODevice sourceCode, QUrl documentUri = QUrl())'''
    def setQuery(self, queryURI, baseUri = QUrl()):
        '''void QXmlQuery.setQuery(QUrl queryURI, QUrl baseUri = QUrl())'''
    def messageHandler(self):
        '''QAbstractMessageHandler QXmlQuery.messageHandler()'''
        return QAbstractMessageHandler()
    def setMessageHandler(self, messageHandler):
        '''void QXmlQuery.setMessageHandler(QAbstractMessageHandler messageHandler)'''


class QXmlResultItems():
    """"""
    def __init__(self):
        '''void QXmlResultItems.__init__()'''
    def current(self):
        '''QXmlItem QXmlResultItems.current()'''
        return QXmlItem()
    def next(self):
        '''QXmlItem QXmlResultItems.next()'''
        return QXmlItem()
    def hasError(self):
        '''bool QXmlResultItems.hasError()'''
        return bool()


class QXmlSchema():
    """"""
    def __init__(self):
        '''void QXmlSchema.__init__()'''
    def networkAccessManager(self):
        '''QNetworkAccessManager QXmlSchema.networkAccessManager()'''
        return QNetworkAccessManager()
    def setNetworkAccessManager(self, networkmanager):
        '''void QXmlSchema.setNetworkAccessManager(QNetworkAccessManager networkmanager)'''
    def uriResolver(self):
        '''QAbstractUriResolver QXmlSchema.uriResolver()'''
        return QAbstractUriResolver()
    def setUriResolver(self, resolver):
        '''void QXmlSchema.setUriResolver(QAbstractUriResolver resolver)'''
    def messageHandler(self):
        '''QAbstractMessageHandler QXmlSchema.messageHandler()'''
        return QAbstractMessageHandler()
    def setMessageHandler(self, handler):
        '''void QXmlSchema.setMessageHandler(QAbstractMessageHandler handler)'''
    def documentUri(self):
        '''QUrl QXmlSchema.documentUri()'''
        return QUrl()
    def namePool(self):
        '''QXmlNamePool QXmlSchema.namePool()'''
        return QXmlNamePool()
    def isValid(self):
        '''bool QXmlSchema.isValid()'''
        return bool()
    def load(self, source):
        '''bool QXmlSchema.load(QUrl source)'''
        return bool()
    def load(self, source, documentUri = QUrl()):
        '''bool QXmlSchema.load(QIODevice source, QUrl documentUri = QUrl())'''
        return bool()
    def load(self, data, documentUri = QUrl()):
        '''bool QXmlSchema.load(QByteArray data, QUrl documentUri = QUrl())'''
        return bool()


class QXmlSchemaValidator():
    """"""
    def __init__(self):
        '''void QXmlSchemaValidator.__init__()'''
    def __init__(self, schema):
        '''void QXmlSchemaValidator.__init__(QXmlSchema schema)'''
    def networkAccessManager(self):
        '''QNetworkAccessManager QXmlSchemaValidator.networkAccessManager()'''
        return QNetworkAccessManager()
    def setNetworkAccessManager(self, networkmanager):
        '''void QXmlSchemaValidator.setNetworkAccessManager(QNetworkAccessManager networkmanager)'''
    def uriResolver(self):
        '''QAbstractUriResolver QXmlSchemaValidator.uriResolver()'''
        return QAbstractUriResolver()
    def setUriResolver(self, resolver):
        '''void QXmlSchemaValidator.setUriResolver(QAbstractUriResolver resolver)'''
    def messageHandler(self):
        '''QAbstractMessageHandler QXmlSchemaValidator.messageHandler()'''
        return QAbstractMessageHandler()
    def setMessageHandler(self, handler):
        '''void QXmlSchemaValidator.setMessageHandler(QAbstractMessageHandler handler)'''
    def schema(self):
        '''QXmlSchema QXmlSchemaValidator.schema()'''
        return QXmlSchema()
    def namePool(self):
        '''QXmlNamePool QXmlSchemaValidator.namePool()'''
        return QXmlNamePool()
    def validate(self, source):
        '''bool QXmlSchemaValidator.validate(QUrl source)'''
        return bool()
    def validate(self, source, documentUri = QUrl()):
        '''bool QXmlSchemaValidator.validate(QIODevice source, QUrl documentUri = QUrl())'''
        return bool()
    def validate(self, data, documentUri = QUrl()):
        '''bool QXmlSchemaValidator.validate(QByteArray data, QUrl documentUri = QUrl())'''
        return bool()
    def setSchema(self, schema):
        '''void QXmlSchemaValidator.setSchema(QXmlSchema schema)'''


