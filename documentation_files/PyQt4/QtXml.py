class pyqtSignal():
 def connect(self, targetSignal): pass
 def emit(self, *args): pass
from QtCore import *

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
    def setInvalidDataPolicy(self, policy):
        '''static void QDomImplementation.setInvalidDataPolicy(QDomImplementation.InvalidDataPolicy policy)'''
    def invalidDataPolicy(self):
        '''static QDomImplementation.InvalidDataPolicy QDomImplementation.invalidDataPolicy()'''
        return QDomImplementation.InvalidDataPolicy()
    def isNull(self):
        '''bool QDomImplementation.isNull()'''
        return bool()
    def createDocument(self, nsURI, qName, doctype):
        '''QDomDocument QDomImplementation.createDocument(QString nsURI, QString qName, QDomDocumentType doctype)'''
        return QDomDocument()
    def createDocumentType(self, qName, publicId, systemId):
        '''QDomDocumentType QDomImplementation.createDocumentType(QString qName, QString publicId, QString systemId)'''
        return QDomDocumentType()
    def hasFeature(self, feature, version):
        '''bool QDomImplementation.hasFeature(QString feature, QString version)'''
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
    def nextSiblingElement(self, tagName = QString()):
        '''QDomElement QDomNode.nextSiblingElement(QString tagName = QString())'''
        return QDomElement()
    def previousSiblingElement(self, tagName = QString()):
        '''QDomElement QDomNode.previousSiblingElement(QString tagName = QString())'''
        return QDomElement()
    def lastChildElement(self, tagName = QString()):
        '''QDomElement QDomNode.lastChildElement(QString tagName = QString())'''
        return QDomElement()
    def firstChildElement(self, tagName = QString()):
        '''QDomElement QDomNode.firstChildElement(QString tagName = QString())'''
        return QDomElement()
    def save(self):
        '''int QDomNode.save()'''
        return int()
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
        '''QDomNode QDomNode.namedItem(QString name)'''
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
        '''void QDomNode.setPrefix(QString pre)'''
    def prefix(self):
        '''QString QDomNode.prefix()'''
        return QString()
    def setNodeValue(self):
        '''QString QDomNode.setNodeValue()'''
        return QString()
    def nodeValue(self):
        '''QString QDomNode.nodeValue()'''
        return QString()
    def hasAttributes(self):
        '''bool QDomNode.hasAttributes()'''
        return bool()
    def localName(self):
        '''QString QDomNode.localName()'''
        return QString()
    def namespaceURI(self):
        '''QString QDomNode.namespaceURI()'''
        return QString()
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
        '''QString QDomNode.nodeName()'''
        return QString()
    def isSupported(self, feature, version):
        '''bool QDomNode.isSupported(QString feature, QString version)'''
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
    def at(self, index):
        '''QDomNode QDomNodeList.at(int index)'''
        return QDomNode()
    def __len__(self):
        '''None QDomNodeList.__len__()'''
        return None()
    def count(self):
        '''int QDomNodeList.count()'''
        return int()
    def length(self):
        '''int QDomNodeList.length()'''
        return int()
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
        '''QString QDomDocumentType.internalSubset()'''
        return QString()
    def systemId(self):
        '''QString QDomDocumentType.systemId()'''
        return QString()
    def publicId(self):
        '''QString QDomDocumentType.publicId()'''
        return QString()
    def notations(self):
        '''QDomNamedNodeMap QDomDocumentType.notations()'''
        return QDomNamedNodeMap()
    def entities(self):
        '''QDomNamedNodeMap QDomDocumentType.entities()'''
        return QDomNamedNodeMap()
    def name(self):
        '''QString QDomDocumentType.name()'''
        return QString()


class QDomDocument(QDomNode):
    """"""
    def __init__(self):
        '''void QDomDocument.__init__()'''
    def __init__(self, name):
        '''void QDomDocument.__init__(QString name)'''
    def __init__(self, doctype):
        '''void QDomDocument.__init__(QDomDocumentType doctype)'''
    def __init__(self, x):
        '''void QDomDocument.__init__(QDomDocument x)'''
    def toByteArray(self, indent = 1):
        '''QByteArray QDomDocument.toByteArray(int indent = 1)'''
        return QByteArray()
    def toString(self, indent = 1):
        '''QString QDomDocument.toString(int indent = 1)'''
        return QString()
    def setContent(self, data, namespaceProcessing, errorMsg, errorLine, errorColumn):
        '''bool QDomDocument.setContent(QByteArray data, bool namespaceProcessing, QString errorMsg, int errorLine, int errorColumn)'''
        return bool()
    def setContent(self, text, namespaceProcessing, errorMsg, errorLine, errorColumn):
        '''bool QDomDocument.setContent(QString text, bool namespaceProcessing, QString errorMsg, int errorLine, int errorColumn)'''
        return bool()
    def setContent(self, dev, namespaceProcessing, errorMsg, errorLine, errorColumn):
        '''bool QDomDocument.setContent(QIODevice dev, bool namespaceProcessing, QString errorMsg, int errorLine, int errorColumn)'''
        return bool()
    def setContent(self, source, namespaceProcessing, errorMsg, errorLine, errorColumn):
        '''bool QDomDocument.setContent(QXmlInputSource source, bool namespaceProcessing, QString errorMsg, int errorLine, int errorColumn)'''
        return bool()
    def setContent(self, buffer, errorMsg, errorLine, errorColumn):
        '''bool QDomDocument.setContent(QByteArray buffer, QString errorMsg, int errorLine, int errorColumn)'''
        return bool()
    def setContent(self, text, errorMsg, errorLine, errorColumn):
        '''bool QDomDocument.setContent(QString text, QString errorMsg, int errorLine, int errorColumn)'''
        return bool()
    def setContent(self, dev, errorMsg, errorLine, errorColumn):
        '''bool QDomDocument.setContent(QIODevice dev, QString errorMsg, int errorLine, int errorColumn)'''
        return bool()
    def setContent(self, source, reader, errorMsg, errorLine, errorColumn):
        '''bool QDomDocument.setContent(QXmlInputSource source, QXmlReader reader, QString errorMsg, int errorLine, int errorColumn)'''
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
        '''QDomElement QDomDocument.elementById(QString elementId)'''
        return QDomElement()
    def elementsByTagNameNS(self, nsURI, localName):
        '''QDomNodeList QDomDocument.elementsByTagNameNS(QString nsURI, QString localName)'''
        return QDomNodeList()
    def createAttributeNS(self, nsURI, qName):
        '''QDomAttr QDomDocument.createAttributeNS(QString nsURI, QString qName)'''
        return QDomAttr()
    def createElementNS(self, nsURI, qName):
        '''QDomElement QDomDocument.createElementNS(QString nsURI, QString qName)'''
        return QDomElement()
    def importNode(self, importedNode, deep):
        '''QDomNode QDomDocument.importNode(QDomNode importedNode, bool deep)'''
        return QDomNode()
    def elementsByTagName(self, tagname):
        '''QDomNodeList QDomDocument.elementsByTagName(QString tagname)'''
        return QDomNodeList()
    def createEntityReference(self, name):
        '''QDomEntityReference QDomDocument.createEntityReference(QString name)'''
        return QDomEntityReference()
    def createAttribute(self, name):
        '''QDomAttr QDomDocument.createAttribute(QString name)'''
        return QDomAttr()
    def createProcessingInstruction(self, target, data):
        '''QDomProcessingInstruction QDomDocument.createProcessingInstruction(QString target, QString data)'''
        return QDomProcessingInstruction()
    def createCDATASection(self, data):
        '''QDomCDATASection QDomDocument.createCDATASection(QString data)'''
        return QDomCDATASection()
    def createComment(self, data):
        '''QDomComment QDomDocument.createComment(QString data)'''
        return QDomComment()
    def createTextNode(self, data):
        '''QDomText QDomDocument.createTextNode(QString data)'''
        return QDomText()
    def createDocumentFragment(self):
        '''QDomDocumentFragment QDomDocument.createDocumentFragment()'''
        return QDomDocumentFragment()
    def createElement(self, tagName):
        '''QDomElement QDomDocument.createElement(QString tagName)'''
        return QDomElement()


class QDomNamedNodeMap():
    """"""
    def __init__(self):
        '''void QDomNamedNodeMap.__init__()'''
    def __init__(self):
        '''QDomNamedNodeMap QDomNamedNodeMap.__init__()'''
        return QDomNamedNodeMap()
    def contains(self, name):
        '''bool QDomNamedNodeMap.contains(QString name)'''
        return bool()
    def isEmpty(self):
        '''bool QDomNamedNodeMap.isEmpty()'''
        return bool()
    def size(self):
        '''int QDomNamedNodeMap.size()'''
        return int()
    def __len__(self):
        '''None QDomNamedNodeMap.__len__()'''
        return None()
    def count(self):
        '''int QDomNamedNodeMap.count()'''
        return int()
    def length(self):
        '''int QDomNamedNodeMap.length()'''
        return int()
    def removeNamedItemNS(self, nsURI, localName):
        '''QDomNode QDomNamedNodeMap.removeNamedItemNS(QString nsURI, QString localName)'''
        return QDomNode()
    def setNamedItemNS(self, newNode):
        '''QDomNode QDomNamedNodeMap.setNamedItemNS(QDomNode newNode)'''
        return QDomNode()
    def namedItemNS(self, nsURI, localName):
        '''QDomNode QDomNamedNodeMap.namedItemNS(QString nsURI, QString localName)'''
        return QDomNode()
    def item(self, index):
        '''QDomNode QDomNamedNodeMap.item(int index)'''
        return QDomNode()
    def removeNamedItem(self, name):
        '''QDomNode QDomNamedNodeMap.removeNamedItem(QString name)'''
        return QDomNode()
    def setNamedItem(self, newNode):
        '''QDomNode QDomNamedNodeMap.setNamedItem(QDomNode newNode)'''
        return QDomNode()
    def namedItem(self, name):
        '''QDomNode QDomNamedNodeMap.namedItem(QString name)'''
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
        '''QString QDomCharacterData.setData()'''
        return QString()
    def data(self):
        '''QString QDomCharacterData.data()'''
        return QString()
    def length(self):
        '''int QDomCharacterData.length()'''
        return int()
    def replaceData(self, offset, count, arg):
        '''void QDomCharacterData.replaceData(int offset, int count, QString arg)'''
    def deleteData(self, offset, count):
        '''void QDomCharacterData.deleteData(int offset, int count)'''
    def insertData(self, offset, arg):
        '''void QDomCharacterData.insertData(int offset, QString arg)'''
    def appendData(self, arg):
        '''void QDomCharacterData.appendData(QString arg)'''
    def substringData(self, offset, count):
        '''QString QDomCharacterData.substringData(int offset, int count)'''
        return QString()


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
        '''QString QDomAttr.setValue()'''
        return QString()
    def value(self):
        '''QString QDomAttr.value()'''
        return QString()
    def ownerElement(self):
        '''QDomElement QDomAttr.ownerElement()'''
        return QDomElement()
    def specified(self):
        '''bool QDomAttr.specified()'''
        return bool()
    def name(self):
        '''QString QDomAttr.name()'''
        return QString()


class QDomElement(QDomNode):
    """"""
    def __init__(self):
        '''void QDomElement.__init__()'''
    def __init__(self, x):
        '''void QDomElement.__init__(QDomElement x)'''
    def text(self):
        '''QString QDomElement.text()'''
        return QString()
    def nodeType(self):
        '''QDomNode.NodeType QDomElement.nodeType()'''
        return QDomNode.NodeType()
    def attributes(self):
        '''QDomNamedNodeMap QDomElement.attributes()'''
        return QDomNamedNodeMap()
    def setTagName(self, name):
        '''void QDomElement.setTagName(QString name)'''
    def tagName(self):
        '''QString QDomElement.tagName()'''
        return QString()
    def hasAttributeNS(self, nsURI, localName):
        '''bool QDomElement.hasAttributeNS(QString nsURI, QString localName)'''
        return bool()
    def elementsByTagNameNS(self, nsURI, localName):
        '''QDomNodeList QDomElement.elementsByTagNameNS(QString nsURI, QString localName)'''
        return QDomNodeList()
    def setAttributeNodeNS(self, newAttr):
        '''QDomAttr QDomElement.setAttributeNodeNS(QDomAttr newAttr)'''
        return QDomAttr()
    def attributeNodeNS(self, nsURI, localName):
        '''QDomAttr QDomElement.attributeNodeNS(QString nsURI, QString localName)'''
        return QDomAttr()
    def removeAttributeNS(self, nsURI, localName):
        '''void QDomElement.removeAttributeNS(QString nsURI, QString localName)'''
    def setAttributeNS(self, nsURI, qName, value):
        '''void QDomElement.setAttributeNS(QString nsURI, QString qName, QString value)'''
    def setAttributeNS(self, nsURI, qName, value):
        '''void QDomElement.setAttributeNS(QString nsURI, QString qName, int value)'''
    def setAttributeNS(self, nsURI, qName, value):
        '''void QDomElement.setAttributeNS(QString nsURI, QString qName, int value)'''
    def setAttributeNS(self, nsURI, qName, value):
        '''void QDomElement.setAttributeNS(QString nsURI, QString qName, float value)'''
    def setAttributeNS(self, nsURI, qName, value):
        '''void QDomElement.setAttributeNS(QString nsURI, QString qName, int value)'''
    def attributeNS(self, nsURI, localName, defaultValue = QString()):
        '''QString QDomElement.attributeNS(QString nsURI, QString localName, QString defaultValue = QString())'''
        return QString()
    def hasAttribute(self, name):
        '''bool QDomElement.hasAttribute(QString name)'''
        return bool()
    def elementsByTagName(self, tagname):
        '''QDomNodeList QDomElement.elementsByTagName(QString tagname)'''
        return QDomNodeList()
    def removeAttributeNode(self, oldAttr):
        '''QDomAttr QDomElement.removeAttributeNode(QDomAttr oldAttr)'''
        return QDomAttr()
    def setAttributeNode(self, newAttr):
        '''QDomAttr QDomElement.setAttributeNode(QDomAttr newAttr)'''
        return QDomAttr()
    def attributeNode(self, name):
        '''QDomAttr QDomElement.attributeNode(QString name)'''
        return QDomAttr()
    def removeAttribute(self, name):
        '''void QDomElement.removeAttribute(QString name)'''
    def setAttribute(self, name, value):
        '''void QDomElement.setAttribute(QString name, QString value)'''
    def setAttribute(self, name, value):
        '''void QDomElement.setAttribute(QString name, int value)'''
    def setAttribute(self, name, value):
        '''void QDomElement.setAttribute(QString name, int value)'''
    def setAttribute(self, name, value):
        '''void QDomElement.setAttribute(QString name, float value)'''
    def setAttribute(self, name, value):
        '''void QDomElement.setAttribute(QString name, int value)'''
    def attribute(self, name, defaultValue = QString()):
        '''QString QDomElement.attribute(QString name, QString defaultValue = QString())'''
        return QString()


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
        '''QString QDomNotation.systemId()'''
        return QString()
    def publicId(self):
        '''QString QDomNotation.publicId()'''
        return QString()


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
        '''QString QDomEntity.notationName()'''
        return QString()
    def systemId(self):
        '''QString QDomEntity.systemId()'''
        return QString()
    def publicId(self):
        '''QString QDomEntity.publicId()'''
        return QString()


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
        '''void QDomProcessingInstruction.setData(QString d)'''
    def data(self):
        '''QString QDomProcessingInstruction.data()'''
        return QString()
    def target(self):
        '''QString QDomProcessingInstruction.target()'''
        return QString()


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
        '''QStringList QXmlNamespaceSupport.prefixes()'''
        return QStringList()
    def prefixes(self):
        '''QString QXmlNamespaceSupport.prefixes()'''
        return QString()
    def processName(self):
        '''QString QXmlNamespaceSupport.processName()'''
        return QString()
    def splitName(self):
        '''QString QXmlNamespaceSupport.splitName()'''
        return QString()
    def uri(self):
        '''QString QXmlNamespaceSupport.uri()'''
        return QString()
    def prefix(self):
        '''QString QXmlNamespaceSupport.prefix()'''
        return QString()
    def setPrefix(self):
        '''QString QXmlNamespaceSupport.setPrefix()'''
        return QString()


class QXmlAttributes():
    """"""
    def __init__(self):
        '''void QXmlAttributes.__init__()'''
    def __init__(self):
        '''QXmlAttributes QXmlAttributes.__init__()'''
        return QXmlAttributes()
    def __len__(self):
        '''None QXmlAttributes.__len__()'''
        return None()
    def count(self):
        '''int QXmlAttributes.count()'''
        return int()
    def append(self, qName, uri, localPart, value):
        '''void QXmlAttributes.append(QString qName, QString uri, QString localPart, QString value)'''
    def clear(self):
        '''void QXmlAttributes.clear()'''
    def value(self, index):
        '''QString QXmlAttributes.value(int index)'''
        return QString()
    def value(self, qName):
        '''QString QXmlAttributes.value(QString qName)'''
        return QString()
    def value(self, uri, localName):
        '''QString QXmlAttributes.value(QString uri, QString localName)'''
        return QString()
    def type(self, index):
        '''QString QXmlAttributes.type(int index)'''
        return QString()
    def type(self, qName):
        '''QString QXmlAttributes.type(QString qName)'''
        return QString()
    def type(self, uri, localName):
        '''QString QXmlAttributes.type(QString uri, QString localName)'''
        return QString()
    def uri(self, index):
        '''QString QXmlAttributes.uri(int index)'''
        return QString()
    def qName(self, index):
        '''QString QXmlAttributes.qName(int index)'''
        return QString()
    def localName(self, index):
        '''QString QXmlAttributes.localName(int index)'''
        return QString()
    def length(self):
        '''int QXmlAttributes.length()'''
        return int()
    def index(self, qName):
        '''int QXmlAttributes.index(QString qName)'''
        return int()
    def index(self, uri, localPart):
        '''int QXmlAttributes.index(QString uri, QString localPart)'''
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
        '''QString QXmlInputSource.fromRawData(QByteArray data, bool beginning = False)'''
        return QString()
    def reset(self):
        '''void QXmlInputSource.reset()'''
    def next(self):
        '''QChar QXmlInputSource.next()'''
        return QChar()
    def data(self):
        '''QString QXmlInputSource.data()'''
        return QString()
    def fetchData(self):
        '''void QXmlInputSource.fetchData()'''
    def setData(self, dat):
        '''void QXmlInputSource.setData(QString dat)'''
    def setData(self, dat):
        '''void QXmlInputSource.setData(QByteArray dat)'''


class QXmlParseException():
    """"""
    def __init__(self, name = QString(), column = None, line = None, publicId = QString(), systemId = QString()):
        '''void QXmlParseException.__init__(QString name = QString(), int column = -1, int line = -1, QString publicId = QString(), QString systemId = QString())'''
    def __init__(self, other):
        '''void QXmlParseException.__init__(QXmlParseException other)'''
    def message(self):
        '''QString QXmlParseException.message()'''
        return QString()
    def systemId(self):
        '''QString QXmlParseException.systemId()'''
        return QString()
    def publicId(self):
        '''QString QXmlParseException.publicId()'''
        return QString()
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
        '''abstract bool QXmlReader.hasProperty(QString name)'''
        return bool()
    def setProperty(self, name, value):
        '''abstract void QXmlReader.setProperty(QString name, sip.voidptr value)'''
    def property(self, name, ok):
        '''abstract sip.voidptr QXmlReader.property(QString name, bool ok)'''
        return sip.voidptr()
    def hasFeature(self, name):
        '''abstract bool QXmlReader.hasFeature(QString name)'''
        return bool()
    def setFeature(self, name, value):
        '''abstract void QXmlReader.setFeature(QString name, bool value)'''
    def feature(self, name, ok):
        '''abstract bool QXmlReader.feature(QString name, bool ok)'''
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
        '''bool QXmlSimpleReader.hasProperty(QString name)'''
        return bool()
    def setProperty(self, name, value):
        '''void QXmlSimpleReader.setProperty(QString name, sip.voidptr value)'''
    def property(self, name, ok):
        '''sip.voidptr QXmlSimpleReader.property(QString name, bool ok)'''
        return sip.voidptr()
    def hasFeature(self, name):
        '''bool QXmlSimpleReader.hasFeature(QString name)'''
        return bool()
    def setFeature(self, name, value):
        '''void QXmlSimpleReader.setFeature(QString name, bool value)'''
    def feature(self, name, ok):
        '''bool QXmlSimpleReader.feature(QString name, bool ok)'''
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
        '''abstract QString QXmlContentHandler.errorString()'''
        return QString()
    def skippedEntity(self, name):
        '''abstract bool QXmlContentHandler.skippedEntity(QString name)'''
        return bool()
    def processingInstruction(self, target, data):
        '''abstract bool QXmlContentHandler.processingInstruction(QString target, QString data)'''
        return bool()
    def ignorableWhitespace(self, ch):
        '''abstract bool QXmlContentHandler.ignorableWhitespace(QString ch)'''
        return bool()
    def characters(self, ch):
        '''abstract bool QXmlContentHandler.characters(QString ch)'''
        return bool()
    def endElement(self, namespaceURI, localName, qName):
        '''abstract bool QXmlContentHandler.endElement(QString namespaceURI, QString localName, QString qName)'''
        return bool()
    def startElement(self, namespaceURI, localName, qName, atts):
        '''abstract bool QXmlContentHandler.startElement(QString namespaceURI, QString localName, QString qName, QXmlAttributes atts)'''
        return bool()
    def endPrefixMapping(self, prefix):
        '''abstract bool QXmlContentHandler.endPrefixMapping(QString prefix)'''
        return bool()
    def startPrefixMapping(self, prefix, uri):
        '''abstract bool QXmlContentHandler.startPrefixMapping(QString prefix, QString uri)'''
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
        '''abstract QString QXmlErrorHandler.errorString()'''
        return QString()
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
        '''abstract QString QXmlDTDHandler.errorString()'''
        return QString()
    def unparsedEntityDecl(self, name, publicId, systemId, notationName):
        '''abstract bool QXmlDTDHandler.unparsedEntityDecl(QString name, QString publicId, QString systemId, QString notationName)'''
        return bool()
    def notationDecl(self, name, publicId, systemId):
        '''abstract bool QXmlDTDHandler.notationDecl(QString name, QString publicId, QString systemId)'''
        return bool()


class QXmlEntityResolver():
    """"""
    def __init__(self):
        '''void QXmlEntityResolver.__init__()'''
    def __init__(self):
        '''QXmlEntityResolver QXmlEntityResolver.__init__()'''
        return QXmlEntityResolver()
    def errorString(self):
        '''abstract QString QXmlEntityResolver.errorString()'''
        return QString()
    def resolveEntity(self, publicId, systemId, ret):
        '''abstract bool QXmlEntityResolver.resolveEntity(QString publicId, QString systemId, QXmlInputSource ret)'''
        return bool()


class QXmlLexicalHandler():
    """"""
    def __init__(self):
        '''void QXmlLexicalHandler.__init__()'''
    def __init__(self):
        '''QXmlLexicalHandler QXmlLexicalHandler.__init__()'''
        return QXmlLexicalHandler()
    def errorString(self):
        '''abstract QString QXmlLexicalHandler.errorString()'''
        return QString()
    def comment(self, ch):
        '''abstract bool QXmlLexicalHandler.comment(QString ch)'''
        return bool()
    def endCDATA(self):
        '''abstract bool QXmlLexicalHandler.endCDATA()'''
        return bool()
    def startCDATA(self):
        '''abstract bool QXmlLexicalHandler.startCDATA()'''
        return bool()
    def endEntity(self, name):
        '''abstract bool QXmlLexicalHandler.endEntity(QString name)'''
        return bool()
    def startEntity(self, name):
        '''abstract bool QXmlLexicalHandler.startEntity(QString name)'''
        return bool()
    def endDTD(self):
        '''abstract bool QXmlLexicalHandler.endDTD()'''
        return bool()
    def startDTD(self, name, publicId, systemId):
        '''abstract bool QXmlLexicalHandler.startDTD(QString name, QString publicId, QString systemId)'''
        return bool()


class QXmlDeclHandler():
    """"""
    def __init__(self):
        '''void QXmlDeclHandler.__init__()'''
    def __init__(self):
        '''QXmlDeclHandler QXmlDeclHandler.__init__()'''
        return QXmlDeclHandler()
    def errorString(self):
        '''abstract QString QXmlDeclHandler.errorString()'''
        return QString()
    def externalEntityDecl(self, name, publicId, systemId):
        '''abstract bool QXmlDeclHandler.externalEntityDecl(QString name, QString publicId, QString systemId)'''
        return bool()
    def internalEntityDecl(self, name, value):
        '''abstract bool QXmlDeclHandler.internalEntityDecl(QString name, QString value)'''
        return bool()
    def attributeDecl(self, eName, aName, type, valueDefault, value):
        '''abstract bool QXmlDeclHandler.attributeDecl(QString eName, QString aName, QString type, QString valueDefault, QString value)'''
        return bool()


class QXmlDefaultHandler(QXmlContentHandler, QXmlErrorHandler, QXmlDTDHandler, QXmlEntityResolver, QXmlLexicalHandler, QXmlDeclHandler):
    """"""
    def __init__(self):
        '''void QXmlDefaultHandler.__init__()'''
    def errorString(self):
        '''QString QXmlDefaultHandler.errorString()'''
        return QString()
    def externalEntityDecl(self, name, publicId, systemId):
        '''bool QXmlDefaultHandler.externalEntityDecl(QString name, QString publicId, QString systemId)'''
        return bool()
    def internalEntityDecl(self, name, value):
        '''bool QXmlDefaultHandler.internalEntityDecl(QString name, QString value)'''
        return bool()
    def attributeDecl(self, eName, aName, type, valueDefault, value):
        '''bool QXmlDefaultHandler.attributeDecl(QString eName, QString aName, QString type, QString valueDefault, QString value)'''
        return bool()
    def comment(self, ch):
        '''bool QXmlDefaultHandler.comment(QString ch)'''
        return bool()
    def endCDATA(self):
        '''bool QXmlDefaultHandler.endCDATA()'''
        return bool()
    def startCDATA(self):
        '''bool QXmlDefaultHandler.startCDATA()'''
        return bool()
    def endEntity(self, name):
        '''bool QXmlDefaultHandler.endEntity(QString name)'''
        return bool()
    def startEntity(self, name):
        '''bool QXmlDefaultHandler.startEntity(QString name)'''
        return bool()
    def endDTD(self):
        '''bool QXmlDefaultHandler.endDTD()'''
        return bool()
    def startDTD(self, name, publicId, systemId):
        '''bool QXmlDefaultHandler.startDTD(QString name, QString publicId, QString systemId)'''
        return bool()
    def resolveEntity(self, publicId, systemId, ret):
        '''bool QXmlDefaultHandler.resolveEntity(QString publicId, QString systemId, QXmlInputSource ret)'''
        return bool()
    def unparsedEntityDecl(self, name, publicId, systemId, notationName):
        '''bool QXmlDefaultHandler.unparsedEntityDecl(QString name, QString publicId, QString systemId, QString notationName)'''
        return bool()
    def notationDecl(self, name, publicId, systemId):
        '''bool QXmlDefaultHandler.notationDecl(QString name, QString publicId, QString systemId)'''
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
        '''bool QXmlDefaultHandler.skippedEntity(QString name)'''
        return bool()
    def processingInstruction(self, target, data):
        '''bool QXmlDefaultHandler.processingInstruction(QString target, QString data)'''
        return bool()
    def ignorableWhitespace(self, ch):
        '''bool QXmlDefaultHandler.ignorableWhitespace(QString ch)'''
        return bool()
    def characters(self, ch):
        '''bool QXmlDefaultHandler.characters(QString ch)'''
        return bool()
    def endElement(self, namespaceURI, localName, qName):
        '''bool QXmlDefaultHandler.endElement(QString namespaceURI, QString localName, QString qName)'''
        return bool()
    def startElement(self, namespaceURI, localName, qName, atts):
        '''bool QXmlDefaultHandler.startElement(QString namespaceURI, QString localName, QString qName, QXmlAttributes atts)'''
        return bool()
    def endPrefixMapping(self, prefix):
        '''bool QXmlDefaultHandler.endPrefixMapping(QString prefix)'''
        return bool()
    def startPrefixMapping(self, prefix, uri):
        '''bool QXmlDefaultHandler.startPrefixMapping(QString prefix, QString uri)'''
        return bool()
    def endDocument(self):
        '''bool QXmlDefaultHandler.endDocument()'''
        return bool()
    def startDocument(self):
        '''bool QXmlDefaultHandler.startDocument()'''
        return bool()
    def setDocumentLocator(self, locator):
        '''void QXmlDefaultHandler.setDocumentLocator(QXmlLocator locator)'''


