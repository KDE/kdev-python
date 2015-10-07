class pyqtSignal():
 def connect(self, targetSignal): pass
 def emit(self, *args): pass
from QtCore import *

from QtWidgets import *

import datetime

class QXmlNamespaceSupport():
    """"""
    def __init__(self):
        '''void QXmlNamespaceSupport.__init__()'''
    def reset(self):
        '''void QXmlNamespaceSupport.reset()'''
    def popContext(self):
        '''void QXmlNamespaceSupport.popContext()'''
    def pushContext(self):
        '''void QXmlNamespaceSupport.pushContext()'''
    def prefixes(self):
        '''list-of-str QXmlNamespaceSupport.prefixes()'''
        return [str()]
    def prefixes(self):
        '''str QXmlNamespaceSupport.prefixes()'''
        return str()
    def processName(self):
        '''str QXmlNamespaceSupport.processName()'''
        return str()
    def splitName(self):
        '''str QXmlNamespaceSupport.splitName()'''
        return str()
    def uri(self):
        '''str QXmlNamespaceSupport.uri()'''
        return str()
    def prefix(self):
        '''str QXmlNamespaceSupport.prefix()'''
        return str()
    def setPrefix(self):
        '''str QXmlNamespaceSupport.setPrefix()'''
        return str()


class QXmlAttributes():
    """"""
    def __init__(self):
        '''void QXmlAttributes.__init__()'''
    def __init__(self):
        '''QXmlAttributes QXmlAttributes.__init__()'''
        return QXmlAttributes()
    def __len__(self):
        ''' QXmlAttributes.__len__()'''
        return ()
    def count(self):
        '''int QXmlAttributes.count()'''
        return int()
    def append(self, qName, uri, localPart, value):
        '''void QXmlAttributes.append(str qName, str uri, str localPart, str value)'''
    def clear(self):
        '''void QXmlAttributes.clear()'''
    def value(self, index):
        '''str QXmlAttributes.value(int index)'''
        return str()
    def value(self, qName):
        '''str QXmlAttributes.value(str qName)'''
        return str()
    def value(self, uri, localName):
        '''str QXmlAttributes.value(str uri, str localName)'''
        return str()
    def type(self, index):
        '''str QXmlAttributes.type(int index)'''
        return str()
    def type(self, qName):
        '''str QXmlAttributes.type(str qName)'''
        return str()
    def type(self, uri, localName):
        '''str QXmlAttributes.type(str uri, str localName)'''
        return str()
    def uri(self, index):
        '''str QXmlAttributes.uri(int index)'''
        return str()
    def qName(self, index):
        '''str QXmlAttributes.qName(int index)'''
        return str()
    def localName(self, index):
        '''str QXmlAttributes.localName(int index)'''
        return str()
    def length(self):
        '''int QXmlAttributes.length()'''
        return int()
    def index(self, qName):
        '''int QXmlAttributes.index(str qName)'''
        return int()
    def index(self, uri, localPart):
        '''int QXmlAttributes.index(str uri, str localPart)'''
        return int()


class QXmlInputSource():
    """"""
    EndOfData = None # int - member
    EndOfDocument = None # int - member
    def __init__(self):
        '''void QXmlInputSource.__init__()'''
    def __init__(self, dev):
        '''void QXmlInputSource.__init__(QIODevice dev)'''
    def __init__(self):
        '''QXmlInputSource QXmlInputSource.__init__()'''
        return QXmlInputSource()
    def fromRawData(self, data, beginning = False):
        '''str QXmlInputSource.fromRawData(QByteArray data, bool beginning = False)'''
        return str()
    def reset(self):
        '''void QXmlInputSource.reset()'''
    def next(self):
        '''str QXmlInputSource.next()'''
        return str()
    def data(self):
        '''str QXmlInputSource.data()'''
        return str()
    def fetchData(self):
        '''void QXmlInputSource.fetchData()'''
    def setData(self, dat):
        '''void QXmlInputSource.setData(str dat)'''
    def setData(self, dat):
        '''void QXmlInputSource.setData(QByteArray dat)'''


class QXmlParseException():
    """"""
    def __init__(self, name = str(), column = None, line = None, publicId = str(), systemId = str()):
        '''void QXmlParseException.__init__(str name = str(), int column = -1, int line = -1, str publicId = str(), str systemId = str())'''
    def __init__(self, other):
        '''void QXmlParseException.__init__(QXmlParseException other)'''
    def message(self):
        '''str QXmlParseException.message()'''
        return str()
    def systemId(self):
        '''str QXmlParseException.systemId()'''
        return str()
    def publicId(self):
        '''str QXmlParseException.publicId()'''
        return str()
    def lineNumber(self):
        '''int QXmlParseException.lineNumber()'''
        return int()
    def columnNumber(self):
        '''int QXmlParseException.columnNumber()'''
        return int()


class QXmlReader():
    """"""
    def __init__(self):
        '''void QXmlReader.__init__()'''
    def __init__(self):
        '''QXmlReader QXmlReader.__init__()'''
        return QXmlReader()
    def parse(self, input):
        '''abstract bool QXmlReader.parse(QXmlInputSource input)'''
        return bool()
    def parse(self, input):
        '''abstract bool QXmlReader.parse(QXmlInputSource input)'''
        return bool()
    def declHandler(self):
        '''abstract QXmlDeclHandler QXmlReader.declHandler()'''
        return QXmlDeclHandler()
    def setDeclHandler(self, handler):
        '''abstract void QXmlReader.setDeclHandler(QXmlDeclHandler handler)'''
    def lexicalHandler(self):
        '''abstract QXmlLexicalHandler QXmlReader.lexicalHandler()'''
        return QXmlLexicalHandler()
    def setLexicalHandler(self, handler):
        '''abstract void QXmlReader.setLexicalHandler(QXmlLexicalHandler handler)'''
    def errorHandler(self):
        '''abstract QXmlErrorHandler QXmlReader.errorHandler()'''
        return QXmlErrorHandler()
    def setErrorHandler(self, handler):
        '''abstract void QXmlReader.setErrorHandler(QXmlErrorHandler handler)'''
    def contentHandler(self):
        '''abstract QXmlContentHandler QXmlReader.contentHandler()'''
        return QXmlContentHandler()
    def setContentHandler(self, handler):
        '''abstract void QXmlReader.setContentHandler(QXmlContentHandler handler)'''
    def DTDHandler(self):
        '''abstract QXmlDTDHandler QXmlReader.DTDHandler()'''
        return QXmlDTDHandler()
    def setDTDHandler(self, handler):
        '''abstract void QXmlReader.setDTDHandler(QXmlDTDHandler handler)'''
    def entityResolver(self):
        '''abstract QXmlEntityResolver QXmlReader.entityResolver()'''
        return QXmlEntityResolver()
    def setEntityResolver(self, handler):
        '''abstract void QXmlReader.setEntityResolver(QXmlEntityResolver handler)'''
    def hasProperty(self, name):
        '''abstract bool QXmlReader.hasProperty(str name)'''
        return bool()
    def setProperty(self, name, value):
        '''abstract void QXmlReader.setProperty(str name, sip.voidptr value)'''
    def property(self, name, ok):
        '''abstract sip.voidptr QXmlReader.property(str name, bool ok)'''
        return sip.voidptr()
    def hasFeature(self, name):
        '''abstract bool QXmlReader.hasFeature(str name)'''
        return bool()
    def setFeature(self, name, value):
        '''abstract void QXmlReader.setFeature(str name, bool value)'''
    def feature(self, name, ok):
        '''abstract bool QXmlReader.feature(str name, bool ok)'''
        return bool()


class QXmlSimpleReader(QXmlReader):
    """"""
    def __init__(self):
        '''void QXmlSimpleReader.__init__()'''
    def parseContinue(self):
        '''bool QXmlSimpleReader.parseContinue()'''
        return bool()
    def parse(self, input):
        '''bool QXmlSimpleReader.parse(QXmlInputSource input)'''
        return bool()
    def parse(self, input, incremental):
        '''bool QXmlSimpleReader.parse(QXmlInputSource input, bool incremental)'''
        return bool()
    def declHandler(self):
        '''QXmlDeclHandler QXmlSimpleReader.declHandler()'''
        return QXmlDeclHandler()
    def setDeclHandler(self, handler):
        '''void QXmlSimpleReader.setDeclHandler(QXmlDeclHandler handler)'''
    def lexicalHandler(self):
        '''QXmlLexicalHandler QXmlSimpleReader.lexicalHandler()'''
        return QXmlLexicalHandler()
    def setLexicalHandler(self, handler):
        '''void QXmlSimpleReader.setLexicalHandler(QXmlLexicalHandler handler)'''
    def errorHandler(self):
        '''QXmlErrorHandler QXmlSimpleReader.errorHandler()'''
        return QXmlErrorHandler()
    def setErrorHandler(self, handler):
        '''void QXmlSimpleReader.setErrorHandler(QXmlErrorHandler handler)'''
    def contentHandler(self):
        '''QXmlContentHandler QXmlSimpleReader.contentHandler()'''
        return QXmlContentHandler()
    def setContentHandler(self, handler):
        '''void QXmlSimpleReader.setContentHandler(QXmlContentHandler handler)'''
    def DTDHandler(self):
        '''QXmlDTDHandler QXmlSimpleReader.DTDHandler()'''
        return QXmlDTDHandler()
    def setDTDHandler(self, handler):
        '''void QXmlSimpleReader.setDTDHandler(QXmlDTDHandler handler)'''
    def entityResolver(self):
        '''QXmlEntityResolver QXmlSimpleReader.entityResolver()'''
        return QXmlEntityResolver()
    def setEntityResolver(self, handler):
        '''void QXmlSimpleReader.setEntityResolver(QXmlEntityResolver handler)'''
    def hasProperty(self, name):
        '''bool QXmlSimpleReader.hasProperty(str name)'''
        return bool()
    def setProperty(self, name, value):
        '''void QXmlSimpleReader.setProperty(str name, sip.voidptr value)'''
    def property(self, name, ok):
        '''sip.voidptr QXmlSimpleReader.property(str name, bool ok)'''
        return sip.voidptr()
    def hasFeature(self, name):
        '''bool QXmlSimpleReader.hasFeature(str name)'''
        return bool()
    def setFeature(self, name, value):
        '''void QXmlSimpleReader.setFeature(str name, bool value)'''
    def feature(self, name, ok):
        '''bool QXmlSimpleReader.feature(str name, bool ok)'''
        return bool()


class QXmlLocator():
    """"""
    def __init__(self):
        '''void QXmlLocator.__init__()'''
    def __init__(self):
        '''QXmlLocator QXmlLocator.__init__()'''
        return QXmlLocator()
    def lineNumber(self):
        '''abstract int QXmlLocator.lineNumber()'''
        return int()
    def columnNumber(self):
        '''abstract int QXmlLocator.columnNumber()'''
        return int()


class QXmlContentHandler():
    """"""
    def __init__(self):
        '''void QXmlContentHandler.__init__()'''
    def __init__(self):
        '''QXmlContentHandler QXmlContentHandler.__init__()'''
        return QXmlContentHandler()
    def errorString(self):
        '''abstract str QXmlContentHandler.errorString()'''
        return str()
    def skippedEntity(self, name):
        '''abstract bool QXmlContentHandler.skippedEntity(str name)'''
        return bool()
    def processingInstruction(self, target, data):
        '''abstract bool QXmlContentHandler.processingInstruction(str target, str data)'''
        return bool()
    def ignorableWhitespace(self, ch):
        '''abstract bool QXmlContentHandler.ignorableWhitespace(str ch)'''
        return bool()
    def characters(self, ch):
        '''abstract bool QXmlContentHandler.characters(str ch)'''
        return bool()
    def endElement(self, namespaceURI, localName, qName):
        '''abstract bool QXmlContentHandler.endElement(str namespaceURI, str localName, str qName)'''
        return bool()
    def startElement(self, namespaceURI, localName, qName, atts):
        '''abstract bool QXmlContentHandler.startElement(str namespaceURI, str localName, str qName, QXmlAttributes atts)'''
        return bool()
    def endPrefixMapping(self, prefix):
        '''abstract bool QXmlContentHandler.endPrefixMapping(str prefix)'''
        return bool()
    def startPrefixMapping(self, prefix, uri):
        '''abstract bool QXmlContentHandler.startPrefixMapping(str prefix, str uri)'''
        return bool()
    def endDocument(self):
        '''abstract bool QXmlContentHandler.endDocument()'''
        return bool()
    def startDocument(self):
        '''abstract bool QXmlContentHandler.startDocument()'''
        return bool()
    def setDocumentLocator(self, locator):
        '''abstract void QXmlContentHandler.setDocumentLocator(QXmlLocator locator)'''


class QXmlErrorHandler():
    """"""
    def __init__(self):
        '''void QXmlErrorHandler.__init__()'''
    def __init__(self):
        '''QXmlErrorHandler QXmlErrorHandler.__init__()'''
        return QXmlErrorHandler()
    def errorString(self):
        '''abstract str QXmlErrorHandler.errorString()'''
        return str()
    def fatalError(self, exception):
        '''abstract bool QXmlErrorHandler.fatalError(QXmlParseException exception)'''
        return bool()
    def error(self, exception):
        '''abstract bool QXmlErrorHandler.error(QXmlParseException exception)'''
        return bool()
    def warning(self, exception):
        '''abstract bool QXmlErrorHandler.warning(QXmlParseException exception)'''
        return bool()


class QXmlDTDHandler():
    """"""
    def __init__(self):
        '''void QXmlDTDHandler.__init__()'''
    def __init__(self):
        '''QXmlDTDHandler QXmlDTDHandler.__init__()'''
        return QXmlDTDHandler()
    def errorString(self):
        '''abstract str QXmlDTDHandler.errorString()'''
        return str()
    def unparsedEntityDecl(self, name, publicId, systemId, notationName):
        '''abstract bool QXmlDTDHandler.unparsedEntityDecl(str name, str publicId, str systemId, str notationName)'''
        return bool()
    def notationDecl(self, name, publicId, systemId):
        '''abstract bool QXmlDTDHandler.notationDecl(str name, str publicId, str systemId)'''
        return bool()


class QXmlEntityResolver():
    """"""
    def __init__(self):
        '''void QXmlEntityResolver.__init__()'''
    def __init__(self):
        '''QXmlEntityResolver QXmlEntityResolver.__init__()'''
        return QXmlEntityResolver()
    def errorString(self):
        '''abstract str QXmlEntityResolver.errorString()'''
        return str()
    def resolveEntity(self, publicId, systemId, ret):
        '''abstract bool QXmlEntityResolver.resolveEntity(str publicId, str systemId, QXmlInputSource ret)'''
        return bool()


class QXmlLexicalHandler():
    """"""
    def __init__(self):
        '''void QXmlLexicalHandler.__init__()'''
    def __init__(self):
        '''QXmlLexicalHandler QXmlLexicalHandler.__init__()'''
        return QXmlLexicalHandler()
    def errorString(self):
        '''abstract str QXmlLexicalHandler.errorString()'''
        return str()
    def comment(self, ch):
        '''abstract bool QXmlLexicalHandler.comment(str ch)'''
        return bool()
    def endCDATA(self):
        '''abstract bool QXmlLexicalHandler.endCDATA()'''
        return bool()
    def startCDATA(self):
        '''abstract bool QXmlLexicalHandler.startCDATA()'''
        return bool()
    def endEntity(self, name):
        '''abstract bool QXmlLexicalHandler.endEntity(str name)'''
        return bool()
    def startEntity(self, name):
        '''abstract bool QXmlLexicalHandler.startEntity(str name)'''
        return bool()
    def endDTD(self):
        '''abstract bool QXmlLexicalHandler.endDTD()'''
        return bool()
    def startDTD(self, name, publicId, systemId):
        '''abstract bool QXmlLexicalHandler.startDTD(str name, str publicId, str systemId)'''
        return bool()


class QXmlDeclHandler():
    """"""
    def __init__(self):
        '''void QXmlDeclHandler.__init__()'''
    def __init__(self):
        '''QXmlDeclHandler QXmlDeclHandler.__init__()'''
        return QXmlDeclHandler()
    def errorString(self):
        '''abstract str QXmlDeclHandler.errorString()'''
        return str()
    def externalEntityDecl(self, name, publicId, systemId):
        '''abstract bool QXmlDeclHandler.externalEntityDecl(str name, str publicId, str systemId)'''
        return bool()
    def internalEntityDecl(self, name, value):
        '''abstract bool QXmlDeclHandler.internalEntityDecl(str name, str value)'''
        return bool()
    def attributeDecl(self, eName, aName, type, valueDefault, value):
        '''abstract bool QXmlDeclHandler.attributeDecl(str eName, str aName, str type, str valueDefault, str value)'''
        return bool()


class QXmlDefaultHandler(QXmlContentHandler, QXmlErrorHandler, QXmlDTDHandler, QXmlEntityResolver, QXmlLexicalHandler, QXmlDeclHandler):
    """"""
    def __init__(self):
        '''void QXmlDefaultHandler.__init__()'''
    def errorString(self):
        '''str QXmlDefaultHandler.errorString()'''
        return str()
    def externalEntityDecl(self, name, publicId, systemId):
        '''bool QXmlDefaultHandler.externalEntityDecl(str name, str publicId, str systemId)'''
        return bool()
    def internalEntityDecl(self, name, value):
        '''bool QXmlDefaultHandler.internalEntityDecl(str name, str value)'''
        return bool()
    def attributeDecl(self, eName, aName, type, valueDefault, value):
        '''bool QXmlDefaultHandler.attributeDecl(str eName, str aName, str type, str valueDefault, str value)'''
        return bool()
    def comment(self, ch):
        '''bool QXmlDefaultHandler.comment(str ch)'''
        return bool()
    def endCDATA(self):
        '''bool QXmlDefaultHandler.endCDATA()'''
        return bool()
    def startCDATA(self):
        '''bool QXmlDefaultHandler.startCDATA()'''
        return bool()
    def endEntity(self, name):
        '''bool QXmlDefaultHandler.endEntity(str name)'''
        return bool()
    def startEntity(self, name):
        '''bool QXmlDefaultHandler.startEntity(str name)'''
        return bool()
    def endDTD(self):
        '''bool QXmlDefaultHandler.endDTD()'''
        return bool()
    def startDTD(self, name, publicId, systemId):
        '''bool QXmlDefaultHandler.startDTD(str name, str publicId, str systemId)'''
        return bool()
    def resolveEntity(self, publicId, systemId, ret):
        '''bool QXmlDefaultHandler.resolveEntity(str publicId, str systemId, QXmlInputSource ret)'''
        return bool()
    def unparsedEntityDecl(self, name, publicId, systemId, notationName):
        '''bool QXmlDefaultHandler.unparsedEntityDecl(str name, str publicId, str systemId, str notationName)'''
        return bool()
    def notationDecl(self, name, publicId, systemId):
        '''bool QXmlDefaultHandler.notationDecl(str name, str publicId, str systemId)'''
        return bool()
    def fatalError(self, exception):
        '''bool QXmlDefaultHandler.fatalError(QXmlParseException exception)'''
        return bool()
    def error(self, exception):
        '''bool QXmlDefaultHandler.error(QXmlParseException exception)'''
        return bool()
    def warning(self, exception):
        '''bool QXmlDefaultHandler.warning(QXmlParseException exception)'''
        return bool()
    def skippedEntity(self, name):
        '''bool QXmlDefaultHandler.skippedEntity(str name)'''
        return bool()
    def processingInstruction(self, target, data):
        '''bool QXmlDefaultHandler.processingInstruction(str target, str data)'''
        return bool()
    def ignorableWhitespace(self, ch):
        '''bool QXmlDefaultHandler.ignorableWhitespace(str ch)'''
        return bool()
    def characters(self, ch):
        '''bool QXmlDefaultHandler.characters(str ch)'''
        return bool()
    def endElement(self, namespaceURI, localName, qName):
        '''bool QXmlDefaultHandler.endElement(str namespaceURI, str localName, str qName)'''
        return bool()
    def startElement(self, namespaceURI, localName, qName, atts):
        '''bool QXmlDefaultHandler.startElement(str namespaceURI, str localName, str qName, QXmlAttributes atts)'''
        return bool()
    def endPrefixMapping(self, prefix):
        '''bool QXmlDefaultHandler.endPrefixMapping(str prefix)'''
        return bool()
    def startPrefixMapping(self, prefix, uri):
        '''bool QXmlDefaultHandler.startPrefixMapping(str prefix, str uri)'''
        return bool()
    def endDocument(self):
        '''bool QXmlDefaultHandler.endDocument()'''
        return bool()
    def startDocument(self):
        '''bool QXmlDefaultHandler.startDocument()'''
        return bool()
    def setDocumentLocator(self, locator):
        '''void QXmlDefaultHandler.setDocumentLocator(QXmlLocator locator)'''


class QDomImplementation():
    """"""
    # Enum QDomImplementation.InvalidDataPolicy
    AcceptInvalidChars = 0
    DropInvalidChars = 0
    ReturnNullNode = 0

    def __init__(self):
        '''void QDomImplementation.__init__()'''
    def __init__(self):
        '''QDomImplementation QDomImplementation.__init__()'''
        return QDomImplementation()
    def isNull(self):
        '''bool QDomImplementation.isNull()'''
        return bool()
    def setInvalidDataPolicy(self, policy):
        '''static void QDomImplementation.setInvalidDataPolicy(QDomImplementation.InvalidDataPolicy policy)'''
    def invalidDataPolicy(self):
        '''static QDomImplementation.InvalidDataPolicy QDomImplementation.invalidDataPolicy()'''
        return QDomImplementation.InvalidDataPolicy()
    def createDocument(self, nsURI, qName, doctype):
        '''QDomDocument QDomImplementation.createDocument(str nsURI, str qName, QDomDocumentType doctype)'''
        return QDomDocument()
    def createDocumentType(self, qName, publicId, systemId):
        '''QDomDocumentType QDomImplementation.createDocumentType(str qName, str publicId, str systemId)'''
        return QDomDocumentType()
    def hasFeature(self, feature, version):
        '''bool QDomImplementation.hasFeature(str feature, str version)'''
        return bool()
    def __ne__(self):
        '''QDomImplementation QDomImplementation.__ne__()'''
        return QDomImplementation()
    def __eq__(self):
        '''QDomImplementation QDomImplementation.__eq__()'''
        return QDomImplementation()


class QDomNode():
    """"""
    # Enum QDomNode.EncodingPolicy
    EncodingFromDocument = 0
    EncodingFromTextStream = 0

    # Enum QDomNode.NodeType
    ElementNode = 0
    AttributeNode = 0
    TextNode = 0
    CDATASectionNode = 0
    EntityReferenceNode = 0
    EntityNode = 0
    ProcessingInstructionNode = 0
    CommentNode = 0
    DocumentNode = 0
    DocumentTypeNode = 0
    DocumentFragmentNode = 0
    NotationNode = 0
    BaseNode = 0
    CharacterDataNode = 0

    def __init__(self):
        '''void QDomNode.__init__()'''
    def __init__(self):
        '''QDomNode QDomNode.__init__()'''
        return QDomNode()
    def columnNumber(self):
        '''int QDomNode.columnNumber()'''
        return int()
    def lineNumber(self):
        '''int QDomNode.lineNumber()'''
        return int()
    def nextSiblingElement(self, taName = str()):
        '''QDomElement QDomNode.nextSiblingElement(str taName = str())'''
        return QDomElement()
    def previousSiblingElement(self, tagName = str()):
        '''QDomElement QDomNode.previousSiblingElement(str tagName = str())'''
        return QDomElement()
    def lastChildElement(self, tagName = str()):
        '''QDomElement QDomNode.lastChildElement(str tagName = str())'''
        return QDomElement()
    def firstChildElement(self, tagName = str()):
        '''QDomElement QDomNode.firstChildElement(str tagName = str())'''
        return QDomElement()
    def save(self):
        '''QDomNode.EncodingPolicy QDomNode.save()'''
        return QDomNode.EncodingPolicy()
    def toComment(self):
        '''QDomComment QDomNode.toComment()'''
        return QDomComment()
    def toCharacterData(self):
        '''QDomCharacterData QDomNode.toCharacterData()'''
        return QDomCharacterData()
    def toProcessingInstruction(self):
        '''QDomProcessingInstruction QDomNode.toProcessingInstruction()'''
        return QDomProcessingInstruction()
    def toNotation(self):
        '''QDomNotation QDomNode.toNotation()'''
        return QDomNotation()
    def toEntity(self):
        '''QDomEntity QDomNode.toEntity()'''
        return QDomEntity()
    def toText(self):
        '''QDomText QDomNode.toText()'''
        return QDomText()
    def toEntityReference(self):
        '''QDomEntityReference QDomNode.toEntityReference()'''
        return QDomEntityReference()
    def toElement(self):
        '''QDomElement QDomNode.toElement()'''
        return QDomElement()
    def toDocumentType(self):
        '''QDomDocumentType QDomNode.toDocumentType()'''
        return QDomDocumentType()
    def toDocument(self):
        '''QDomDocument QDomNode.toDocument()'''
        return QDomDocument()
    def toDocumentFragment(self):
        '''QDomDocumentFragment QDomNode.toDocumentFragment()'''
        return QDomDocumentFragment()
    def toCDATASection(self):
        '''QDomCDATASection QDomNode.toCDATASection()'''
        return QDomCDATASection()
    def toAttr(self):
        '''QDomAttr QDomNode.toAttr()'''
        return QDomAttr()
    def clear(self):
        '''void QDomNode.clear()'''
    def isNull(self):
        '''bool QDomNode.isNull()'''
        return bool()
    def namedItem(self, name):
        '''QDomNode QDomNode.namedItem(str name)'''
        return QDomNode()
    def isComment(self):
        '''bool QDomNode.isComment()'''
        return bool()
    def isCharacterData(self):
        '''bool QDomNode.isCharacterData()'''
        return bool()
    def isProcessingInstruction(self):
        '''bool QDomNode.isProcessingInstruction()'''
        return bool()
    def isNotation(self):
        '''bool QDomNode.isNotation()'''
        return bool()
    def isEntity(self):
        '''bool QDomNode.isEntity()'''
        return bool()
    def isText(self):
        '''bool QDomNode.isText()'''
        return bool()
    def isEntityReference(self):
        '''bool QDomNode.isEntityReference()'''
        return bool()
    def isElement(self):
        '''bool QDomNode.isElement()'''
        return bool()
    def isDocumentType(self):
        '''bool QDomNode.isDocumentType()'''
        return bool()
    def isDocument(self):
        '''bool QDomNode.isDocument()'''
        return bool()
    def isDocumentFragment(self):
        '''bool QDomNode.isDocumentFragment()'''
        return bool()
    def isCDATASection(self):
        '''bool QDomNode.isCDATASection()'''
        return bool()
    def isAttr(self):
        '''bool QDomNode.isAttr()'''
        return bool()
    def setPrefix(self, pre):
        '''void QDomNode.setPrefix(str pre)'''
    def prefix(self):
        '''str QDomNode.prefix()'''
        return str()
    def setNodeValue(self):
        '''str QDomNode.setNodeValue()'''
        return str()
    def nodeValue(self):
        '''str QDomNode.nodeValue()'''
        return str()
    def hasAttributes(self):
        '''bool QDomNode.hasAttributes()'''
        return bool()
    def localName(self):
        '''str QDomNode.localName()'''
        return str()
    def namespaceURI(self):
        '''str QDomNode.namespaceURI()'''
        return str()
    def ownerDocument(self):
        '''QDomDocument QDomNode.ownerDocument()'''
        return QDomDocument()
    def attributes(self):
        '''QDomNamedNodeMap QDomNode.attributes()'''
        return QDomNamedNodeMap()
    def nextSibling(self):
        '''QDomNode QDomNode.nextSibling()'''
        return QDomNode()
    def previousSibling(self):
        '''QDomNode QDomNode.previousSibling()'''
        return QDomNode()
    def lastChild(self):
        '''QDomNode QDomNode.lastChild()'''
        return QDomNode()
    def firstChild(self):
        '''QDomNode QDomNode.firstChild()'''
        return QDomNode()
    def childNodes(self):
        '''QDomNodeList QDomNode.childNodes()'''
        return QDomNodeList()
    def parentNode(self):
        '''QDomNode QDomNode.parentNode()'''
        return QDomNode()
    def nodeType(self):
        '''QDomNode.NodeType QDomNode.nodeType()'''
        return QDomNode.NodeType()
    def nodeName(self):
        '''str QDomNode.nodeName()'''
        return str()
    def isSupported(self, feature, version):
        '''bool QDomNode.isSupported(str feature, str version)'''
        return bool()
    def normalize(self):
        '''void QDomNode.normalize()'''
    def cloneNode(self, deep = True):
        '''QDomNode QDomNode.cloneNode(bool deep = True)'''
        return QDomNode()
    def hasChildNodes(self):
        '''bool QDomNode.hasChildNodes()'''
        return bool()
    def appendChild(self, newChild):
        '''QDomNode QDomNode.appendChild(QDomNode newChild)'''
        return QDomNode()
    def removeChild(self, oldChild):
        '''QDomNode QDomNode.removeChild(QDomNode oldChild)'''
        return QDomNode()
    def replaceChild(self, newChild, oldChild):
        '''QDomNode QDomNode.replaceChild(QDomNode newChild, QDomNode oldChild)'''
        return QDomNode()
    def insertAfter(self, newChild, refChild):
        '''QDomNode QDomNode.insertAfter(QDomNode newChild, QDomNode refChild)'''
        return QDomNode()
    def insertBefore(self, newChild, refChild):
        '''QDomNode QDomNode.insertBefore(QDomNode newChild, QDomNode refChild)'''
        return QDomNode()
    def __ne__(self):
        '''QDomNode QDomNode.__ne__()'''
        return QDomNode()
    def __eq__(self):
        '''QDomNode QDomNode.__eq__()'''
        return QDomNode()


class QDomNodeList():
    """"""
    def __init__(self):
        '''void QDomNodeList.__init__()'''
    def __init__(self):
        '''QDomNodeList QDomNodeList.__init__()'''
        return QDomNodeList()
    def isEmpty(self):
        '''bool QDomNodeList.isEmpty()'''
        return bool()
    def size(self):
        '''int QDomNodeList.size()'''
        return int()
    def __len__(self):
        ''' QDomNodeList.__len__()'''
        return ()
    def count(self):
        '''int QDomNodeList.count()'''
        return int()
    def length(self):
        '''int QDomNodeList.length()'''
        return int()
    def at(self, index):
        '''QDomNode QDomNodeList.at(int index)'''
        return QDomNode()
    def item(self, index):
        '''QDomNode QDomNodeList.item(int index)'''
        return QDomNode()
    def __ne__(self):
        '''QDomNodeList QDomNodeList.__ne__()'''
        return QDomNodeList()
    def __eq__(self):
        '''QDomNodeList QDomNodeList.__eq__()'''
        return QDomNodeList()


class QDomDocumentType(QDomNode):
    """"""
    def __init__(self):
        '''void QDomDocumentType.__init__()'''
    def __init__(self, x):
        '''void QDomDocumentType.__init__(QDomDocumentType x)'''
    def nodeType(self):
        '''QDomNode.NodeType QDomDocumentType.nodeType()'''
        return QDomNode.NodeType()
    def internalSubset(self):
        '''str QDomDocumentType.internalSubset()'''
        return str()
    def systemId(self):
        '''str QDomDocumentType.systemId()'''
        return str()
    def publicId(self):
        '''str QDomDocumentType.publicId()'''
        return str()
    def notations(self):
        '''QDomNamedNodeMap QDomDocumentType.notations()'''
        return QDomNamedNodeMap()
    def entities(self):
        '''QDomNamedNodeMap QDomDocumentType.entities()'''
        return QDomNamedNodeMap()
    def name(self):
        '''str QDomDocumentType.name()'''
        return str()


class QDomDocument(QDomNode):
    """"""
    def __init__(self):
        '''void QDomDocument.__init__()'''
    def __init__(self, name):
        '''void QDomDocument.__init__(str name)'''
    def __init__(self, doctype):
        '''void QDomDocument.__init__(QDomDocumentType doctype)'''
    def __init__(self, x):
        '''void QDomDocument.__init__(QDomDocument x)'''
    def toByteArray(self, indent = 1):
        '''QByteArray QDomDocument.toByteArray(int indent = 1)'''
        return QByteArray()
    def toString(self, indent = 1):
        '''str QDomDocument.toString(int indent = 1)'''
        return str()
    def setContent(self, text, namespaceProcessing, errorMsg, errorLine, errorColumn):
        '''bool QDomDocument.setContent(QByteArray text, bool namespaceProcessing, str errorMsg, int errorLine, int errorColumn)'''
        return bool()
    def setContent(self, text, namespaceProcessing, errorMsg, errorLine, errorColumn):
        '''bool QDomDocument.setContent(str text, bool namespaceProcessing, str errorMsg, int errorLine, int errorColumn)'''
        return bool()
    def setContent(self, dev, namespaceProcessing, errorMsg, errorLine, errorColumn):
        '''bool QDomDocument.setContent(QIODevice dev, bool namespaceProcessing, str errorMsg, int errorLine, int errorColumn)'''
        return bool()
    def setContent(self, source, namespaceProcessing, errorMsg, errorLine, errorColumn):
        '''bool QDomDocument.setContent(QXmlInputSource source, bool namespaceProcessing, str errorMsg, int errorLine, int errorColumn)'''
        return bool()
    def setContent(self, text, errorMsg, errorLine, errorColumn):
        '''bool QDomDocument.setContent(QByteArray text, str errorMsg, int errorLine, int errorColumn)'''
        return bool()
    def setContent(self, text, errorMsg, errorLine, errorColumn):
        '''bool QDomDocument.setContent(str text, str errorMsg, int errorLine, int errorColumn)'''
        return bool()
    def setContent(self, dev, errorMsg, errorLine, errorColumn):
        '''bool QDomDocument.setContent(QIODevice dev, str errorMsg, int errorLine, int errorColumn)'''
        return bool()
    def setContent(self, source, reader, errorMsg, errorLine, errorColumn):
        '''bool QDomDocument.setContent(QXmlInputSource source, QXmlReader reader, str errorMsg, int errorLine, int errorColumn)'''
        return bool()
    def nodeType(self):
        '''QDomNode.NodeType QDomDocument.nodeType()'''
        return QDomNode.NodeType()
    def documentElement(self):
        '''QDomElement QDomDocument.documentElement()'''
        return QDomElement()
    def implementation(self):
        '''QDomImplementation QDomDocument.implementation()'''
        return QDomImplementation()
    def doctype(self):
        '''QDomDocumentType QDomDocument.doctype()'''
        return QDomDocumentType()
    def elementById(self, elementId):
        '''QDomElement QDomDocument.elementById(str elementId)'''
        return QDomElement()
    def elementsByTagNameNS(self, nsURI, localName):
        '''QDomNodeList QDomDocument.elementsByTagNameNS(str nsURI, str localName)'''
        return QDomNodeList()
    def createAttributeNS(self, nsURI, qName):
        '''QDomAttr QDomDocument.createAttributeNS(str nsURI, str qName)'''
        return QDomAttr()
    def createElementNS(self, nsURI, qName):
        '''QDomElement QDomDocument.createElementNS(str nsURI, str qName)'''
        return QDomElement()
    def importNode(self, importedNode, deep):
        '''QDomNode QDomDocument.importNode(QDomNode importedNode, bool deep)'''
        return QDomNode()
    def elementsByTagName(self, tagname):
        '''QDomNodeList QDomDocument.elementsByTagName(str tagname)'''
        return QDomNodeList()
    def createEntityReference(self, name):
        '''QDomEntityReference QDomDocument.createEntityReference(str name)'''
        return QDomEntityReference()
    def createAttribute(self, name):
        '''QDomAttr QDomDocument.createAttribute(str name)'''
        return QDomAttr()
    def createProcessingInstruction(self, target, data):
        '''QDomProcessingInstruction QDomDocument.createProcessingInstruction(str target, str data)'''
        return QDomProcessingInstruction()
    def createCDATASection(self, data):
        '''QDomCDATASection QDomDocument.createCDATASection(str data)'''
        return QDomCDATASection()
    def createComment(self, data):
        '''QDomComment QDomDocument.createComment(str data)'''
        return QDomComment()
    def createTextNode(self, data):
        '''QDomText QDomDocument.createTextNode(str data)'''
        return QDomText()
    def createDocumentFragment(self):
        '''QDomDocumentFragment QDomDocument.createDocumentFragment()'''
        return QDomDocumentFragment()
    def createElement(self, tagName):
        '''QDomElement QDomDocument.createElement(str tagName)'''
        return QDomElement()


class QDomNamedNodeMap():
    """"""
    def __init__(self):
        '''void QDomNamedNodeMap.__init__()'''
    def __init__(self):
        '''QDomNamedNodeMap QDomNamedNodeMap.__init__()'''
        return QDomNamedNodeMap()
    def contains(self, name):
        '''bool QDomNamedNodeMap.contains(str name)'''
        return bool()
    def isEmpty(self):
        '''bool QDomNamedNodeMap.isEmpty()'''
        return bool()
    def size(self):
        '''int QDomNamedNodeMap.size()'''
        return int()
    def __len__(self):
        ''' QDomNamedNodeMap.__len__()'''
        return ()
    def count(self):
        '''int QDomNamedNodeMap.count()'''
        return int()
    def length(self):
        '''int QDomNamedNodeMap.length()'''
        return int()
    def removeNamedItemNS(self, nsURI, localName):
        '''QDomNode QDomNamedNodeMap.removeNamedItemNS(str nsURI, str localName)'''
        return QDomNode()
    def setNamedItemNS(self, newNode):
        '''QDomNode QDomNamedNodeMap.setNamedItemNS(QDomNode newNode)'''
        return QDomNode()
    def namedItemNS(self, nsURI, localName):
        '''QDomNode QDomNamedNodeMap.namedItemNS(str nsURI, str localName)'''
        return QDomNode()
    def item(self, index):
        '''QDomNode QDomNamedNodeMap.item(int index)'''
        return QDomNode()
    def removeNamedItem(self, name):
        '''QDomNode QDomNamedNodeMap.removeNamedItem(str name)'''
        return QDomNode()
    def setNamedItem(self, newNode):
        '''QDomNode QDomNamedNodeMap.setNamedItem(QDomNode newNode)'''
        return QDomNode()
    def namedItem(self, name):
        '''QDomNode QDomNamedNodeMap.namedItem(str name)'''
        return QDomNode()
    def __ne__(self):
        '''QDomNamedNodeMap QDomNamedNodeMap.__ne__()'''
        return QDomNamedNodeMap()
    def __eq__(self):
        '''QDomNamedNodeMap QDomNamedNodeMap.__eq__()'''
        return QDomNamedNodeMap()


class QDomDocumentFragment(QDomNode):
    """"""
    def __init__(self):
        '''void QDomDocumentFragment.__init__()'''
    def __init__(self, x):
        '''void QDomDocumentFragment.__init__(QDomDocumentFragment x)'''
    def nodeType(self):
        '''QDomNode.NodeType QDomDocumentFragment.nodeType()'''
        return QDomNode.NodeType()


class QDomCharacterData(QDomNode):
    """"""
    def __init__(self):
        '''void QDomCharacterData.__init__()'''
    def __init__(self, x):
        '''void QDomCharacterData.__init__(QDomCharacterData x)'''
    def nodeType(self):
        '''QDomNode.NodeType QDomCharacterData.nodeType()'''
        return QDomNode.NodeType()
    def setData(self):
        '''str QDomCharacterData.setData()'''
        return str()
    def data(self):
        '''str QDomCharacterData.data()'''
        return str()
    def length(self):
        '''int QDomCharacterData.length()'''
        return int()
    def replaceData(self, offset, count, arg):
        '''void QDomCharacterData.replaceData(int offset, int count, str arg)'''
    def deleteData(self, offset, count):
        '''void QDomCharacterData.deleteData(int offset, int count)'''
    def insertData(self, offset, arg):
        '''void QDomCharacterData.insertData(int offset, str arg)'''
    def appendData(self, arg):
        '''void QDomCharacterData.appendData(str arg)'''
    def substringData(self, offset, count):
        '''str QDomCharacterData.substringData(int offset, int count)'''
        return str()


class QDomAttr(QDomNode):
    """"""
    def __init__(self):
        '''void QDomAttr.__init__()'''
    def __init__(self, x):
        '''void QDomAttr.__init__(QDomAttr x)'''
    def nodeType(self):
        '''QDomNode.NodeType QDomAttr.nodeType()'''
        return QDomNode.NodeType()
    def setValue(self):
        '''str QDomAttr.setValue()'''
        return str()
    def value(self):
        '''str QDomAttr.value()'''
        return str()
    def ownerElement(self):
        '''QDomElement QDomAttr.ownerElement()'''
        return QDomElement()
    def specified(self):
        '''bool QDomAttr.specified()'''
        return bool()
    def name(self):
        '''str QDomAttr.name()'''
        return str()


class QDomElement(QDomNode):
    """"""
    def __init__(self):
        '''void QDomElement.__init__()'''
    def __init__(self, x):
        '''void QDomElement.__init__(QDomElement x)'''
    def text(self):
        '''str QDomElement.text()'''
        return str()
    def nodeType(self):
        '''QDomNode.NodeType QDomElement.nodeType()'''
        return QDomNode.NodeType()
    def attributes(self):
        '''QDomNamedNodeMap QDomElement.attributes()'''
        return QDomNamedNodeMap()
    def setTagName(self, name):
        '''void QDomElement.setTagName(str name)'''
    def tagName(self):
        '''str QDomElement.tagName()'''
        return str()
    def hasAttributeNS(self, nsURI, localName):
        '''bool QDomElement.hasAttributeNS(str nsURI, str localName)'''
        return bool()
    def elementsByTagNameNS(self, nsURI, localName):
        '''QDomNodeList QDomElement.elementsByTagNameNS(str nsURI, str localName)'''
        return QDomNodeList()
    def setAttributeNodeNS(self, newAttr):
        '''QDomAttr QDomElement.setAttributeNodeNS(QDomAttr newAttr)'''
        return QDomAttr()
    def attributeNodeNS(self, nsURI, localName):
        '''QDomAttr QDomElement.attributeNodeNS(str nsURI, str localName)'''
        return QDomAttr()
    def removeAttributeNS(self, nsURI, localName):
        '''void QDomElement.removeAttributeNS(str nsURI, str localName)'''
    def setAttributeNS(self, nsURI, qName, value):
        '''void QDomElement.setAttributeNS(str nsURI, str qName, str value)'''
    def setAttributeNS(self, nsURI, qName, value):
        '''void QDomElement.setAttributeNS(str nsURI, str qName, int value)'''
    def setAttributeNS(self, nsURI, qName, value):
        '''void QDomElement.setAttributeNS(str nsURI, str qName, int value)'''
    def setAttributeNS(self, nsURI, qName, value):
        '''void QDomElement.setAttributeNS(str nsURI, str qName, float value)'''
    def setAttributeNS(self, nsURI, qName, value):
        '''void QDomElement.setAttributeNS(str nsURI, str qName, int value)'''
    def attributeNS(self, nsURI, localName, defaultValue = str()):
        '''str QDomElement.attributeNS(str nsURI, str localName, str defaultValue = str())'''
        return str()
    def hasAttribute(self, name):
        '''bool QDomElement.hasAttribute(str name)'''
        return bool()
    def elementsByTagName(self, tagname):
        '''QDomNodeList QDomElement.elementsByTagName(str tagname)'''
        return QDomNodeList()
    def removeAttributeNode(self, oldAttr):
        '''QDomAttr QDomElement.removeAttributeNode(QDomAttr oldAttr)'''
        return QDomAttr()
    def setAttributeNode(self, newAttr):
        '''QDomAttr QDomElement.setAttributeNode(QDomAttr newAttr)'''
        return QDomAttr()
    def attributeNode(self, name):
        '''QDomAttr QDomElement.attributeNode(str name)'''
        return QDomAttr()
    def removeAttribute(self, name):
        '''void QDomElement.removeAttribute(str name)'''
    def setAttribute(self, name, value):
        '''void QDomElement.setAttribute(str name, str value)'''
    def setAttribute(self, name, value):
        '''void QDomElement.setAttribute(str name, int value)'''
    def setAttribute(self, name, value):
        '''void QDomElement.setAttribute(str name, int value)'''
    def setAttribute(self, name, value):
        '''void QDomElement.setAttribute(str name, float value)'''
    def setAttribute(self, name, value):
        '''void QDomElement.setAttribute(str name, int value)'''
    def attribute(self, name, defaultValue = str()):
        '''str QDomElement.attribute(str name, str defaultValue = str())'''
        return str()


class QDomText(QDomCharacterData):
    """"""
    def __init__(self):
        '''void QDomText.__init__()'''
    def __init__(self, x):
        '''void QDomText.__init__(QDomText x)'''
    def nodeType(self):
        '''QDomNode.NodeType QDomText.nodeType()'''
        return QDomNode.NodeType()
    def splitText(self, offset):
        '''QDomText QDomText.splitText(int offset)'''
        return QDomText()


class QDomComment(QDomCharacterData):
    """"""
    def __init__(self):
        '''void QDomComment.__init__()'''
    def __init__(self, x):
        '''void QDomComment.__init__(QDomComment x)'''
    def nodeType(self):
        '''QDomNode.NodeType QDomComment.nodeType()'''
        return QDomNode.NodeType()


class QDomCDATASection(QDomText):
    """"""
    def __init__(self):
        '''void QDomCDATASection.__init__()'''
    def __init__(self, x):
        '''void QDomCDATASection.__init__(QDomCDATASection x)'''
    def nodeType(self):
        '''QDomNode.NodeType QDomCDATASection.nodeType()'''
        return QDomNode.NodeType()


class QDomNotation(QDomNode):
    """"""
    def __init__(self):
        '''void QDomNotation.__init__()'''
    def __init__(self, x):
        '''void QDomNotation.__init__(QDomNotation x)'''
    def nodeType(self):
        '''QDomNode.NodeType QDomNotation.nodeType()'''
        return QDomNode.NodeType()
    def systemId(self):
        '''str QDomNotation.systemId()'''
        return str()
    def publicId(self):
        '''str QDomNotation.publicId()'''
        return str()


class QDomEntity(QDomNode):
    """"""
    def __init__(self):
        '''void QDomEntity.__init__()'''
    def __init__(self, x):
        '''void QDomEntity.__init__(QDomEntity x)'''
    def nodeType(self):
        '''QDomNode.NodeType QDomEntity.nodeType()'''
        return QDomNode.NodeType()
    def notationName(self):
        '''str QDomEntity.notationName()'''
        return str()
    def systemId(self):
        '''str QDomEntity.systemId()'''
        return str()
    def publicId(self):
        '''str QDomEntity.publicId()'''
        return str()


class QDomEntityReference(QDomNode):
    """"""
    def __init__(self):
        '''void QDomEntityReference.__init__()'''
    def __init__(self, x):
        '''void QDomEntityReference.__init__(QDomEntityReference x)'''
    def nodeType(self):
        '''QDomNode.NodeType QDomEntityReference.nodeType()'''
        return QDomNode.NodeType()


class QDomProcessingInstruction(QDomNode):
    """"""
    def __init__(self):
        '''void QDomProcessingInstruction.__init__()'''
    def __init__(self, x):
        '''void QDomProcessingInstruction.__init__(QDomProcessingInstruction x)'''
    def nodeType(self):
        '''QDomNode.NodeType QDomProcessingInstruction.nodeType()'''
        return QDomNode.NodeType()
    def setData(self, d):
        '''void QDomProcessingInstruction.setData(str d)'''
    def data(self):
        '''str QDomProcessingInstruction.data()'''
        return str()
    def target(self):
        '''str QDomProcessingInstruction.target()'''
        return str()


