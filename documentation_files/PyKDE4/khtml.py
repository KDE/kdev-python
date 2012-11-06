class pyqtSignal():
 def connect(self, targetSignal): pass
 def emit(self, *args): pass
from QtCore import *

class DOM():
    """"""
    def strcasecmp(self, a, b):
        '''static bool DOM.strcasecmp(DOM.DOMString a, DOM.DOMString b)'''
        return bool()
    def strcasecmp(self, a, b):
        '''static bool DOM.strcasecmp(DOM.DOMString a, str b)'''
        return bool()
    def strcmp(self, a, b):
        '''static bool DOM.strcmp(DOM.DOMString a, DOM.DOMString b)'''
        return bool()
    class CSSCharsetRule(DOM.CSSRule):
        """"""
        def __init__(self):
            '''void DOM.CSSCharsetRule.__init__()'''
        def __init__(self, other):
            '''void DOM.CSSCharsetRule.__init__(DOM.CSSCharsetRule other)'''
        def __init__(self, other):
            '''void DOM.CSSCharsetRule.__init__(DOM.CSSRule other)'''
        def setEncoding(self):
            '''DOM.DOMString DOM.CSSCharsetRule.setEncoding()'''
            return DOM.DOMString()
        def encoding(self):
            '''DOM.DOMString DOM.CSSCharsetRule.encoding()'''
            return DOM.DOMString()
    class HTMLStyleElement(DOM.HTMLElement):
        """"""
        def __init__(self):
            '''void DOM.HTMLStyleElement.__init__()'''
        def __init__(self, other):
            '''void DOM.HTMLStyleElement.__init__(DOM.HTMLStyleElement other)'''
        def __init__(self, other):
            '''void DOM.HTMLStyleElement.__init__(DOM.Node other)'''
        def sheet(self):
            '''DOM.StyleSheet DOM.HTMLStyleElement.sheet()'''
            return DOM.StyleSheet()
        def setType(self):
            '''DOM.DOMString DOM.HTMLStyleElement.setType()'''
            return DOM.DOMString()
        def type(self):
            '''DOM.DOMString DOM.HTMLStyleElement.type()'''
            return DOM.DOMString()
        def setMedia(self):
            '''DOM.DOMString DOM.HTMLStyleElement.setMedia()'''
            return DOM.DOMString()
        def media(self):
            '''DOM.DOMString DOM.HTMLStyleElement.media()'''
            return DOM.DOMString()
        def setDisabled(self):
            '''bool DOM.HTMLStyleElement.setDisabled()'''
            return bool()
        def disabled(self):
            '''bool DOM.HTMLStyleElement.disabled()'''
            return bool()
    class CSSStyleSheet(DOM.StyleSheet):
        """"""
        def __init__(self):
            '''void DOM.CSSStyleSheet.__init__()'''
        def __init__(self, other):
            '''void DOM.CSSStyleSheet.__init__(DOM.CSSStyleSheet other)'''
        def __init__(self, other):
            '''void DOM.CSSStyleSheet.__init__(DOM.StyleSheet other)'''
        def charset(self):
            '''DOM.DOMString DOM.CSSStyleSheet.charset()'''
            return DOM.DOMString()
        def deleteRule(self, index):
            '''void DOM.CSSStyleSheet.deleteRule(int index)'''
        def insertRule(self, rule, index):
            '''int DOM.CSSStyleSheet.insertRule(DOM.DOMString rule, int index)'''
            return int()
        def cssRules(self):
            '''DOM.CSSRuleList DOM.CSSStyleSheet.cssRules()'''
            return DOM.CSSRuleList()
        def ownerRule(self):
            '''DOM.CSSRule DOM.CSSStyleSheet.ownerRule()'''
            return DOM.CSSRule()
    class HTMLDivElement(DOM.HTMLElement):
        """"""
        def __init__(self):
            '''void DOM.HTMLDivElement.__init__()'''
        def __init__(self, other):
            '''void DOM.HTMLDivElement.__init__(DOM.HTMLDivElement other)'''
        def __init__(self, other):
            '''void DOM.HTMLDivElement.__init__(DOM.Node other)'''
        def setAlign(self):
            '''DOM.DOMString DOM.HTMLDivElement.setAlign()'''
            return DOM.DOMString()
        def align(self):
            '''DOM.DOMString DOM.HTMLDivElement.align()'''
            return DOM.DOMString()
    class HTMLIFrameElement(DOM.HTMLElement):
        """"""
        def __init__(self):
            '''void DOM.HTMLIFrameElement.__init__()'''
        def __init__(self, other):
            '''void DOM.HTMLIFrameElement.__init__(DOM.HTMLIFrameElement other)'''
        def __init__(self, other):
            '''void DOM.HTMLIFrameElement.__init__(DOM.Node other)'''
        def contentDocument(self):
            '''DOM.Document DOM.HTMLIFrameElement.contentDocument()'''
            return DOM.Document()
        def setWidth(self):
            '''DOM.DOMString DOM.HTMLIFrameElement.setWidth()'''
            return DOM.DOMString()
        def width(self):
            '''DOM.DOMString DOM.HTMLIFrameElement.width()'''
            return DOM.DOMString()
        def setSrc(self):
            '''DOM.DOMString DOM.HTMLIFrameElement.setSrc()'''
            return DOM.DOMString()
        def src(self):
            '''DOM.DOMString DOM.HTMLIFrameElement.src()'''
            return DOM.DOMString()
        def setScrolling(self):
            '''DOM.DOMString DOM.HTMLIFrameElement.setScrolling()'''
            return DOM.DOMString()
        def scrolling(self):
            '''DOM.DOMString DOM.HTMLIFrameElement.scrolling()'''
            return DOM.DOMString()
        def setName(self):
            '''DOM.DOMString DOM.HTMLIFrameElement.setName()'''
            return DOM.DOMString()
        def name(self):
            '''DOM.DOMString DOM.HTMLIFrameElement.name()'''
            return DOM.DOMString()
        def setMarginWidth(self):
            '''DOM.DOMString DOM.HTMLIFrameElement.setMarginWidth()'''
            return DOM.DOMString()
        def marginWidth(self):
            '''DOM.DOMString DOM.HTMLIFrameElement.marginWidth()'''
            return DOM.DOMString()
        def setMarginHeight(self):
            '''DOM.DOMString DOM.HTMLIFrameElement.setMarginHeight()'''
            return DOM.DOMString()
        def marginHeight(self):
            '''DOM.DOMString DOM.HTMLIFrameElement.marginHeight()'''
            return DOM.DOMString()
        def setLongDesc(self):
            '''DOM.DOMString DOM.HTMLIFrameElement.setLongDesc()'''
            return DOM.DOMString()
        def longDesc(self):
            '''DOM.DOMString DOM.HTMLIFrameElement.longDesc()'''
            return DOM.DOMString()
        def setHeight(self):
            '''DOM.DOMString DOM.HTMLIFrameElement.setHeight()'''
            return DOM.DOMString()
        def height(self):
            '''DOM.DOMString DOM.HTMLIFrameElement.height()'''
            return DOM.DOMString()
        def setFrameBorder(self):
            '''DOM.DOMString DOM.HTMLIFrameElement.setFrameBorder()'''
            return DOM.DOMString()
        def frameBorder(self):
            '''DOM.DOMString DOM.HTMLIFrameElement.frameBorder()'''
            return DOM.DOMString()
        def setAlign(self):
            '''DOM.DOMString DOM.HTMLIFrameElement.setAlign()'''
            return DOM.DOMString()
        def align(self):
            '''DOM.DOMString DOM.HTMLIFrameElement.align()'''
            return DOM.DOMString()
    class NodeIterator():
        """"""
        def __init__(self):
            '''void DOM.NodeIterator.__init__()'''
        def __init__(self, other):
            '''void DOM.NodeIterator.__init__(DOM.NodeIterator other)'''
        def isNull(self):
            '''bool DOM.NodeIterator.isNull()'''
            return bool()
        def detach(self):
            '''void DOM.NodeIterator.detach()'''
        def previousNode(self):
            '''DOM.Node DOM.NodeIterator.previousNode()'''
            return DOM.Node()
        def nextNode(self):
            '''DOM.Node DOM.NodeIterator.nextNode()'''
            return DOM.Node()
        def expandEntityReferences(self):
            '''bool DOM.NodeIterator.expandEntityReferences()'''
            return bool()
        def filter(self):
            '''DOM.NodeFilter DOM.NodeIterator.filter()'''
            return DOM.NodeFilter()
        def whatToShow(self):
            '''int DOM.NodeIterator.whatToShow()'''
            return int()
        def root(self):
            '''DOM.Node DOM.NodeIterator.root()'''
            return DOM.Node()
    class DOMImplementation():
        """"""
        def __init__(self):
            '''void DOM.DOMImplementation.__init__()'''
        def __init__(self, other):
            '''void DOM.DOMImplementation.__init__(DOM.DOMImplementation other)'''
        def isNull(self):
            '''bool DOM.DOMImplementation.isNull()'''
            return bool()
        def createHTMLDocument(self, title):
            '''DOM.HTMLDocument DOM.DOMImplementation.createHTMLDocument(DOM.DOMString title)'''
            return DOM.HTMLDocument()
        def createCSSStyleSheet(self, title, media):
            '''DOM.CSSStyleSheet DOM.DOMImplementation.createCSSStyleSheet(DOM.DOMString title, DOM.DOMString media)'''
            return DOM.CSSStyleSheet()
        def getInterface(self, feature):
            '''DOM.DOMImplementation DOM.DOMImplementation.getInterface(DOM.DOMString feature)'''
            return DOM.DOMImplementation()
        def createDocument(self, namespaceURI, qualifiedName, doctype):
            '''DOM.Document DOM.DOMImplementation.createDocument(DOM.DOMString namespaceURI, DOM.DOMString qualifiedName, DOM.DocumentType doctype)'''
            return DOM.Document()
        def createDocumentType(self, qualifiedName, publicId, systemId):
            '''DOM.DocumentType DOM.DOMImplementation.createDocumentType(DOM.DOMString qualifiedName, DOM.DOMString publicId, DOM.DOMString systemId)'''
            return DOM.DocumentType()
        def hasFeature(self, feature, version):
            '''bool DOM.DOMImplementation.hasFeature(DOM.DOMString feature, DOM.DOMString version)'''
            return bool()
    class HTMLOptGroupElement(DOM.HTMLElement):
        """"""
        def __init__(self):
            '''void DOM.HTMLOptGroupElement.__init__()'''
        def __init__(self, other):
            '''void DOM.HTMLOptGroupElement.__init__(DOM.HTMLOptGroupElement other)'''
        def __init__(self, other):
            '''void DOM.HTMLOptGroupElement.__init__(DOM.Node other)'''
        def setLabel(self):
            '''DOM.DOMString DOM.HTMLOptGroupElement.setLabel()'''
            return DOM.DOMString()
        def label(self):
            '''DOM.DOMString DOM.HTMLOptGroupElement.label()'''
            return DOM.DOMString()
        def setDisabled(self):
            '''bool DOM.HTMLOptGroupElement.setDisabled()'''
            return bool()
        def disabled(self):
            '''bool DOM.HTMLOptGroupElement.disabled()'''
            return bool()
    class Rect():
        """"""
        def __init__(self):
            '''void DOM.Rect.__init__()'''
        def __init__(self, other):
            '''void DOM.Rect.__init__(DOM.Rect other)'''
        def isNull(self):
            '''bool DOM.Rect.isNull()'''
            return bool()
        def left(self):
            '''DOM.CSSPrimitiveValue DOM.Rect.left()'''
            return DOM.CSSPrimitiveValue()
        def bottom(self):
            '''DOM.CSSPrimitiveValue DOM.Rect.bottom()'''
            return DOM.CSSPrimitiveValue()
        def right(self):
            '''DOM.CSSPrimitiveValue DOM.Rect.right()'''
            return DOM.CSSPrimitiveValue()
        def top(self):
            '''DOM.CSSPrimitiveValue DOM.Rect.top()'''
            return DOM.CSSPrimitiveValue()
    class HTMLFrameElement(DOM.HTMLElement):
        """"""
        def __init__(self):
            '''void DOM.HTMLFrameElement.__init__()'''
        def __init__(self, other):
            '''void DOM.HTMLFrameElement.__init__(DOM.HTMLFrameElement other)'''
        def __init__(self, other):
            '''void DOM.HTMLFrameElement.__init__(DOM.Node other)'''
        def contentDocument(self):
            '''DOM.Document DOM.HTMLFrameElement.contentDocument()'''
            return DOM.Document()
        def setSrc(self):
            '''DOM.DOMString DOM.HTMLFrameElement.setSrc()'''
            return DOM.DOMString()
        def src(self):
            '''DOM.DOMString DOM.HTMLFrameElement.src()'''
            return DOM.DOMString()
        def setScrolling(self):
            '''DOM.DOMString DOM.HTMLFrameElement.setScrolling()'''
            return DOM.DOMString()
        def scrolling(self):
            '''DOM.DOMString DOM.HTMLFrameElement.scrolling()'''
            return DOM.DOMString()
        def setNoResize(self):
            '''bool DOM.HTMLFrameElement.setNoResize()'''
            return bool()
        def noResize(self):
            '''bool DOM.HTMLFrameElement.noResize()'''
            return bool()
        def setName(self):
            '''DOM.DOMString DOM.HTMLFrameElement.setName()'''
            return DOM.DOMString()
        def name(self):
            '''DOM.DOMString DOM.HTMLFrameElement.name()'''
            return DOM.DOMString()
        def setMarginWidth(self):
            '''DOM.DOMString DOM.HTMLFrameElement.setMarginWidth()'''
            return DOM.DOMString()
        def marginWidth(self):
            '''DOM.DOMString DOM.HTMLFrameElement.marginWidth()'''
            return DOM.DOMString()
        def setMarginHeight(self):
            '''DOM.DOMString DOM.HTMLFrameElement.setMarginHeight()'''
            return DOM.DOMString()
        def marginHeight(self):
            '''DOM.DOMString DOM.HTMLFrameElement.marginHeight()'''
            return DOM.DOMString()
        def setLongDesc(self):
            '''DOM.DOMString DOM.HTMLFrameElement.setLongDesc()'''
            return DOM.DOMString()
        def longDesc(self):
            '''DOM.DOMString DOM.HTMLFrameElement.longDesc()'''
            return DOM.DOMString()
        def setFrameBorder(self):
            '''DOM.DOMString DOM.HTMLFrameElement.setFrameBorder()'''
            return DOM.DOMString()
        def frameBorder(self):
            '''DOM.DOMString DOM.HTMLFrameElement.frameBorder()'''
            return DOM.DOMString()
    class HTMLMapElement(DOM.HTMLElement):
        """"""
        def __init__(self):
            '''void DOM.HTMLMapElement.__init__()'''
        def __init__(self, other):
            '''void DOM.HTMLMapElement.__init__(DOM.HTMLMapElement other)'''
        def __init__(self, other):
            '''void DOM.HTMLMapElement.__init__(DOM.Node other)'''
        def setName(self):
            '''DOM.DOMString DOM.HTMLMapElement.setName()'''
            return DOM.DOMString()
        def name(self):
            '''DOM.DOMString DOM.HTMLMapElement.name()'''
            return DOM.DOMString()
        def areas(self):
            '''DOM.HTMLCollection DOM.HTMLMapElement.areas()'''
            return DOM.HTMLCollection()
    class HTMLBRElement(DOM.HTMLElement):
        """"""
        def __init__(self):
            '''void DOM.HTMLBRElement.__init__()'''
        def __init__(self, other):
            '''void DOM.HTMLBRElement.__init__(DOM.HTMLBRElement other)'''
        def __init__(self, other):
            '''void DOM.HTMLBRElement.__init__(DOM.Node other)'''
        def setClear(self):
            '''DOM.DOMString DOM.HTMLBRElement.setClear()'''
            return DOM.DOMString()
        def clear(self):
            '''DOM.DOMString DOM.HTMLBRElement.clear()'''
            return DOM.DOMString()
    class HTMLFrameSetElement(DOM.HTMLElement):
        """"""
        def __init__(self):
            '''void DOM.HTMLFrameSetElement.__init__()'''
        def __init__(self, other):
            '''void DOM.HTMLFrameSetElement.__init__(DOM.HTMLFrameSetElement other)'''
        def __init__(self, other):
            '''void DOM.HTMLFrameSetElement.__init__(DOM.Node other)'''
        def setRows(self):
            '''DOM.DOMString DOM.HTMLFrameSetElement.setRows()'''
            return DOM.DOMString()
        def rows(self):
            '''DOM.DOMString DOM.HTMLFrameSetElement.rows()'''
            return DOM.DOMString()
        def setCols(self):
            '''DOM.DOMString DOM.HTMLFrameSetElement.setCols()'''
            return DOM.DOMString()
        def cols(self):
            '''DOM.DOMString DOM.HTMLFrameSetElement.cols()'''
            return DOM.DOMString()
    class CSSUnknownRule(DOM.CSSRule):
        """"""
        def __init__(self):
            '''void DOM.CSSUnknownRule.__init__()'''
        def __init__(self, other):
            '''void DOM.CSSUnknownRule.__init__(DOM.CSSUnknownRule other)'''
        def __init__(self, other):
            '''void DOM.CSSUnknownRule.__init__(DOM.CSSRule other)'''
    class KeyboardEvent(DOM.UIEvent):
        """"""
        # Enum DOM.KeyboardEvent.KeyLocation
        DOM_KEY_LOCATION_STANDARD = 0
        DOM_KEY_LOCATION_LEFT = 0
        DOM_KEY_LOCATION_RIGHT = 0
        DOM_KEY_LOCATION_NUMPAD = 0
    
        def __init__(self):
            '''void DOM.KeyboardEvent.__init__()'''
        def __init__(self, other):
            '''void DOM.KeyboardEvent.__init__(DOM.KeyboardEvent other)'''
        def __init__(self, other):
            '''void DOM.KeyboardEvent.__init__(DOM.Event other)'''
        def initKeyboardEvent(self, typeArg, canBubbleArg, cancelableArg, viewArg, keyIdentifierArg, keyLocationArg, modifiersList):
            '''void DOM.KeyboardEvent.initKeyboardEvent(DOM.DOMString typeArg, bool canBubbleArg, bool cancelableArg, DOM.AbstractView viewArg, DOM.DOMString keyIdentifierArg, int keyLocationArg, DOM.DOMString modifiersList)'''
        def getModifierState(self, keyIdentifierArg):
            '''bool DOM.KeyboardEvent.getModifierState(DOM.DOMString keyIdentifierArg)'''
            return bool()
        def metaKey(self):
            '''bool DOM.KeyboardEvent.metaKey()'''
            return bool()
        def altKey(self):
            '''bool DOM.KeyboardEvent.altKey()'''
            return bool()
        def shiftKey(self):
            '''bool DOM.KeyboardEvent.shiftKey()'''
            return bool()
        def ctrlKey(self):
            '''bool DOM.KeyboardEvent.ctrlKey()'''
            return bool()
        def keyLocation(self):
            '''int DOM.KeyboardEvent.keyLocation()'''
            return int()
        def keyIdentifier(self):
            '''DOM.DOMString DOM.KeyboardEvent.keyIdentifier()'''
            return DOM.DOMString()
    class CSSNamespaceRule(DOM.CSSRule):
        """"""
        def __init__(self):
            '''void DOM.CSSNamespaceRule.__init__()'''
        def __init__(self, other):
            '''void DOM.CSSNamespaceRule.__init__(DOM.CSSNamespaceRule other)'''
        def __init__(self, other):
            '''void DOM.CSSNamespaceRule.__init__(DOM.CSSRule other)'''
        def prefix(self):
            '''DOM.DOMString DOM.CSSNamespaceRule.prefix()'''
            return DOM.DOMString()
        def namespaceURI(self):
            '''DOM.DOMString DOM.CSSNamespaceRule.namespaceURI()'''
            return DOM.DOMString()
    class HTMLButtonElement(DOM.HTMLElement):
        """"""
        def __init__(self):
            '''void DOM.HTMLButtonElement.__init__()'''
        def __init__(self, other):
            '''void DOM.HTMLButtonElement.__init__(DOM.HTMLButtonElement other)'''
        def __init__(self, other):
            '''void DOM.HTMLButtonElement.__init__(DOM.Node other)'''
        def focus(self):
            '''void DOM.HTMLButtonElement.focus()'''
        def blur(self):
            '''void DOM.HTMLButtonElement.blur()'''
        def setValue(self):
            '''DOM.DOMString DOM.HTMLButtonElement.setValue()'''
            return DOM.DOMString()
        def value(self):
            '''DOM.DOMString DOM.HTMLButtonElement.value()'''
            return DOM.DOMString()
        def type(self):
            '''DOM.DOMString DOM.HTMLButtonElement.type()'''
            return DOM.DOMString()
        def setTabIndex(self):
            '''int DOM.HTMLButtonElement.setTabIndex()'''
            return int()
        def tabIndex(self):
            '''int DOM.HTMLButtonElement.tabIndex()'''
            return int()
        def setName(self):
            '''DOM.DOMString DOM.HTMLButtonElement.setName()'''
            return DOM.DOMString()
        def name(self):
            '''DOM.DOMString DOM.HTMLButtonElement.name()'''
            return DOM.DOMString()
        def setDisabled(self):
            '''bool DOM.HTMLButtonElement.setDisabled()'''
            return bool()
        def disabled(self):
            '''bool DOM.HTMLButtonElement.disabled()'''
            return bool()
        def setAccessKey(self):
            '''DOM.DOMString DOM.HTMLButtonElement.setAccessKey()'''
            return DOM.DOMString()
        def accessKey(self):
            '''DOM.DOMString DOM.HTMLButtonElement.accessKey()'''
            return DOM.DOMString()
        def form(self):
            '''DOM.HTMLFormElement DOM.HTMLButtonElement.form()'''
            return DOM.HTMLFormElement()
    class RangeException():
        """"""
        # Enum DOM.RangeException.RangeExceptionCode
        BAD_BOUNDARYPOINTS_ERR = 0
        INVALID_NODE_TYPE_ERR = 0
        _EXCEPTION_OFFSET = 0
        _EXCEPTION_MAX = 0
    
        code = None # int - member
        def __init__(self, _code):
            '''void DOM.RangeException.__init__(int _code)'''
        def __init__(self, other):
            '''void DOM.RangeException.__init__(DOM.RangeException other)'''
        def isRangeExceptionCode(self, exceptioncode):
            '''static bool DOM.RangeException.isRangeExceptionCode(int exceptioncode)'''
            return bool()
        def codeAsString(self):
            '''DOM.DOMString DOM.RangeException.codeAsString()'''
            return DOM.DOMString()
        def codeAsString(self, rangeCode):
            '''static DOM.DOMString DOM.RangeException.codeAsString(int rangeCode)'''
            return DOM.DOMString()
    class EventException():
        """"""
        # Enum DOM.EventException.EventExceptionCode
        UNSPECIFIED_EVENT_TYPE_ERR = 0
        _EXCEPTION_OFFSET = 0
        _EXCEPTION_MAX = 0
    
        code = None # int - member
        def __init__(self, _code):
            '''void DOM.EventException.__init__(int _code)'''
        def __init__(self, other):
            '''void DOM.EventException.__init__(DOM.EventException other)'''
        def isEventExceptionCode(self, exceptioncode):
            '''static bool DOM.EventException.isEventExceptionCode(int exceptioncode)'''
            return bool()
        def codeAsString(self):
            '''DOM.DOMString DOM.EventException.codeAsString()'''
            return DOM.DOMString()
        def codeAsString(self, cssCode):
            '''static DOM.DOMString DOM.EventException.codeAsString(int cssCode)'''
            return DOM.DOMString()
    class Entity(DOM.Node):
        """"""
        def __init__(self):
            '''void DOM.Entity.__init__()'''
        def __init__(self, other):
            '''void DOM.Entity.__init__(DOM.Entity other)'''
        def __init__(self, other):
            '''void DOM.Entity.__init__(DOM.Node other)'''
        def notationName(self):
            '''DOM.DOMString DOM.Entity.notationName()'''
            return DOM.DOMString()
        def systemId(self):
            '''DOM.DOMString DOM.Entity.systemId()'''
            return DOM.DOMString()
        def publicId(self):
            '''DOM.DOMString DOM.Entity.publicId()'''
            return DOM.DOMString()
    class CSSValue():
        """"""
        # Enum DOM.CSSValue.UnitTypes
        CSS_INHERIT = 0
        CSS_PRIMITIVE_VALUE = 0
        CSS_VALUE_LIST = 0
        CSS_CUSTOM = 0
        CSS_INITIAL = 0
        CSS_SVG_VALUE = 0
    
        def __init__(self):
            '''void DOM.CSSValue.__init__()'''
        def __init__(self, other):
            '''void DOM.CSSValue.__init__(DOM.CSSValue other)'''
        def isNull(self):
            '''bool DOM.CSSValue.isNull()'''
            return bool()
        def isCSSPrimitiveValue(self):
            '''bool DOM.CSSValue.isCSSPrimitiveValue()'''
            return bool()
        def isCSSValueList(self):
            '''bool DOM.CSSValue.isCSSValueList()'''
            return bool()
        def cssValueType(self):
            '''int DOM.CSSValue.cssValueType()'''
            return int()
        def setCssText(self):
            '''DOM.DOMString DOM.CSSValue.setCssText()'''
            return DOM.DOMString()
        def cssText(self):
            '''DOM.DOMString DOM.CSSValue.cssText()'''
            return DOM.DOMString()
    class HTMLPreElement(DOM.HTMLElement):
        """"""
        def __init__(self):
            '''void DOM.HTMLPreElement.__init__()'''
        def __init__(self, other):
            '''void DOM.HTMLPreElement.__init__(DOM.HTMLPreElement other)'''
        def __init__(self, other):
            '''void DOM.HTMLPreElement.__init__(DOM.Node other)'''
        def setWidth(self):
            '''int DOM.HTMLPreElement.setWidth()'''
            return int()
        def width(self):
            '''int DOM.HTMLPreElement.width()'''
            return int()
    class HTMLTitleElement(DOM.HTMLElement):
        """"""
        def __init__(self):
            '''void DOM.HTMLTitleElement.__init__()'''
        def __init__(self, other):
            '''void DOM.HTMLTitleElement.__init__(DOM.HTMLTitleElement other)'''
        def __init__(self, other):
            '''void DOM.HTMLTitleElement.__init__(DOM.Node other)'''
        def setText(self):
            '''DOM.DOMString DOM.HTMLTitleElement.setText()'''
            return DOM.DOMString()
        def text(self):
            '''DOM.DOMString DOM.HTMLTitleElement.text()'''
            return DOM.DOMString()
    class EntityReference(DOM.Node):
        """"""
        def __init__(self):
            '''void DOM.EntityReference.__init__()'''
        def __init__(self, other):
            '''void DOM.EntityReference.__init__(DOM.EntityReference other)'''
        def __init__(self, other):
            '''void DOM.EntityReference.__init__(DOM.Node other)'''
    class TreeWalker():
        """"""
        def __init__(self):
            '''void DOM.TreeWalker.__init__()'''
        def __init__(self, other):
            '''void DOM.TreeWalker.__init__(DOM.TreeWalker other)'''
        def isNull(self):
            '''bool DOM.TreeWalker.isNull()'''
            return bool()
        def nextNode(self):
            '''DOM.Node DOM.TreeWalker.nextNode()'''
            return DOM.Node()
        def previousNode(self):
            '''DOM.Node DOM.TreeWalker.previousNode()'''
            return DOM.Node()
        def nextSibling(self):
            '''DOM.Node DOM.TreeWalker.nextSibling()'''
            return DOM.Node()
        def previousSibling(self):
            '''DOM.Node DOM.TreeWalker.previousSibling()'''
            return DOM.Node()
        def lastChild(self):
            '''DOM.Node DOM.TreeWalker.lastChild()'''
            return DOM.Node()
        def firstChild(self):
            '''DOM.Node DOM.TreeWalker.firstChild()'''
            return DOM.Node()
        def parentNode(self):
            '''DOM.Node DOM.TreeWalker.parentNode()'''
            return DOM.Node()
        def setCurrentNode(self, _currentNode):
            '''void DOM.TreeWalker.setCurrentNode(DOM.Node _currentNode)'''
        def currentNode(self):
            '''DOM.Node DOM.TreeWalker.currentNode()'''
            return DOM.Node()
        def expandEntityReferences(self):
            '''bool DOM.TreeWalker.expandEntityReferences()'''
            return bool()
        def filter(self):
            '''DOM.NodeFilter DOM.TreeWalker.filter()'''
            return DOM.NodeFilter()
        def whatToShow(self):
            '''int DOM.TreeWalker.whatToShow()'''
            return int()
        def root(self):
            '''DOM.Node DOM.TreeWalker.root()'''
            return DOM.Node()
    class HTMLMenuElement(DOM.HTMLElement):
        """"""
        def __init__(self):
            '''void DOM.HTMLMenuElement.__init__()'''
        def __init__(self, other):
            '''void DOM.HTMLMenuElement.__init__(DOM.HTMLMenuElement other)'''
        def __init__(self, other):
            '''void DOM.HTMLMenuElement.__init__(DOM.Node other)'''
        def setCompact(self):
            '''bool DOM.HTMLMenuElement.setCompact()'''
            return bool()
        def compact(self):
            '''bool DOM.HTMLMenuElement.compact()'''
            return bool()
    class HTMLFieldSetElement(DOM.HTMLElement):
        """"""
        def __init__(self):
            '''void DOM.HTMLFieldSetElement.__init__()'''
        def __init__(self, other):
            '''void DOM.HTMLFieldSetElement.__init__(DOM.HTMLFieldSetElement other)'''
        def __init__(self, other):
            '''void DOM.HTMLFieldSetElement.__init__(DOM.Node other)'''
        def form(self):
            '''DOM.HTMLFormElement DOM.HTMLFieldSetElement.form()'''
            return DOM.HTMLFormElement()
    class UIEvent(DOM.Event):
        """"""
        def __init__(self):
            '''void DOM.UIEvent.__init__()'''
        def __init__(self, other):
            '''void DOM.UIEvent.__init__(DOM.UIEvent other)'''
        def __init__(self, other):
            '''void DOM.UIEvent.__init__(DOM.Event other)'''
        def initUIEvent(self, typeArg, canBubbleArg, cancelableArg, viewArg, detailArg):
            '''void DOM.UIEvent.initUIEvent(DOM.DOMString typeArg, bool canBubbleArg, bool cancelableArg, DOM.AbstractView viewArg, int detailArg)'''
        def which(self):
            '''int DOM.UIEvent.which()'''
            return int()
        def layerY(self):
            '''int DOM.UIEvent.layerY()'''
            return int()
        def layerX(self):
            '''int DOM.UIEvent.layerX()'''
            return int()
        def pageY(self):
            '''int DOM.UIEvent.pageY()'''
            return int()
        def pageX(self):
            '''int DOM.UIEvent.pageX()'''
            return int()
        def charCode(self):
            '''int DOM.UIEvent.charCode()'''
            return int()
        def keyCode(self):
            '''int DOM.UIEvent.keyCode()'''
            return int()
        def detail(self):
            '''int DOM.UIEvent.detail()'''
            return int()
        def view(self):
            '''DOM.AbstractView DOM.UIEvent.view()'''
            return DOM.AbstractView()
    class Range():
        """"""
        # Enum DOM.Range.CompareHow
        START_TO_START = 0
        START_TO_END = 0
        END_TO_END = 0
        END_TO_START = 0
    
        def __init__(self):
            '''void DOM.Range.__init__()'''
        def __init__(self, rootContainer):
            '''void DOM.Range.__init__(DOM.Document rootContainer)'''
        def __init__(self, other):
            '''void DOM.Range.__init__(DOM.Range other)'''
        def __init__(self, startContainer, startOffset, endContainer, endOffset):
            '''void DOM.Range.__init__(DOM.Node startContainer, int startOffset, DOM.Node endContainer, int endOffset)'''
        def isNull(self):
            '''bool DOM.Range.isNull()'''
            return bool()
        def isDetached(self):
            '''bool DOM.Range.isDetached()'''
            return bool()
        def detach(self):
            '''void DOM.Range.detach()'''
        def createContextualFragment(self, html):
            '''DOM.DocumentFragment DOM.Range.createContextualFragment(DOM.DOMString html)'''
            return DOM.DocumentFragment()
        def toHTML(self):
            '''DOM.DOMString DOM.Range.toHTML()'''
            return DOM.DOMString()
        def toString(self):
            '''DOM.DOMString DOM.Range.toString()'''
            return DOM.DOMString()
        def cloneRange(self):
            '''DOM.Range DOM.Range.cloneRange()'''
            return DOM.Range()
        def surroundContents(self, newParent):
            '''void DOM.Range.surroundContents(DOM.Node newParent)'''
        def insertNode(self, newNode):
            '''void DOM.Range.insertNode(DOM.Node newNode)'''
        def cloneContents(self):
            '''DOM.DocumentFragment DOM.Range.cloneContents()'''
            return DOM.DocumentFragment()
        def extractContents(self):
            '''DOM.DocumentFragment DOM.Range.extractContents()'''
            return DOM.DocumentFragment()
        def deleteContents(self):
            '''void DOM.Range.deleteContents()'''
        def boundaryPointsValid(self):
            '''bool DOM.Range.boundaryPointsValid()'''
            return bool()
        def compareBoundaryPoints(self, how, sourceRange):
            '''int DOM.Range.compareBoundaryPoints(DOM.Range.CompareHow how, DOM.Range sourceRange)'''
            return int()
        def selectNodeContents(self, refNode):
            '''void DOM.Range.selectNodeContents(DOM.Node refNode)'''
        def selectNode(self, refNode):
            '''void DOM.Range.selectNode(DOM.Node refNode)'''
        def collapse(self, toStart):
            '''void DOM.Range.collapse(bool toStart)'''
        def setEndAfter(self, refNode):
            '''void DOM.Range.setEndAfter(DOM.Node refNode)'''
        def setEndBefore(self, refNode):
            '''void DOM.Range.setEndBefore(DOM.Node refNode)'''
        def setStartAfter(self, refNode):
            '''void DOM.Range.setStartAfter(DOM.Node refNode)'''
        def setStartBefore(self, refNode):
            '''void DOM.Range.setStartBefore(DOM.Node refNode)'''
        def setEnd(self, refNode, offset):
            '''void DOM.Range.setEnd(DOM.Node refNode, int offset)'''
        def setStart(self, refNode, offset):
            '''void DOM.Range.setStart(DOM.Node refNode, int offset)'''
        def commonAncestorContainer(self):
            '''DOM.Node DOM.Range.commonAncestorContainer()'''
            return DOM.Node()
        def collapsed(self):
            '''bool DOM.Range.collapsed()'''
            return bool()
        def endOffset(self):
            '''int DOM.Range.endOffset()'''
            return int()
        def endContainer(self):
            '''DOM.Node DOM.Range.endContainer()'''
            return DOM.Node()
        def startOffset(self):
            '''int DOM.Range.startOffset()'''
            return int()
        def startContainer(self):
            '''DOM.Node DOM.Range.startContainer()'''
            return DOM.Node()
    class HTMLParagraphElement(DOM.HTMLElement):
        """"""
        def __init__(self):
            '''void DOM.HTMLParagraphElement.__init__()'''
        def __init__(self, other):
            '''void DOM.HTMLParagraphElement.__init__(DOM.HTMLParagraphElement other)'''
        def __init__(self, other):
            '''void DOM.HTMLParagraphElement.__init__(DOM.Node other)'''
        def setAlign(self):
            '''DOM.DOMString DOM.HTMLParagraphElement.setAlign()'''
            return DOM.DOMString()
        def align(self):
            '''DOM.DOMString DOM.HTMLParagraphElement.align()'''
            return DOM.DOMString()
    class HTMLCollection():
        """"""
        def __init__(self):
            '''void DOM.HTMLCollection.__init__()'''
        def __init__(self, other):
            '''void DOM.HTMLCollection.__init__(DOM.HTMLCollection other)'''
        def nextNamedItem(self, name):
            '''DOM.Node DOM.HTMLCollection.nextNamedItem(DOM.DOMString name)'''
            return DOM.Node()
        def nextItem(self):
            '''DOM.Node DOM.HTMLCollection.nextItem()'''
            return DOM.Node()
        def firstItem(self):
            '''DOM.Node DOM.HTMLCollection.firstItem()'''
            return DOM.Node()
        def isNull(self):
            '''bool DOM.HTMLCollection.isNull()'''
            return bool()
        def base(self):
            '''DOM.Node DOM.HTMLCollection.base()'''
            return DOM.Node()
        def namedItem(self, name):
            '''DOM.Node DOM.HTMLCollection.namedItem(DOM.DOMString name)'''
            return DOM.Node()
        def item(self, index):
            '''DOM.Node DOM.HTMLCollection.item(int index)'''
            return DOM.Node()
        def length(self):
            '''int DOM.HTMLCollection.length()'''
            return int()
    class AbstractView():
        """"""
        def __init__(self):
            '''void DOM.AbstractView.__init__()'''
        def __init__(self, other):
            '''void DOM.AbstractView.__init__(DOM.AbstractView other)'''
        def isNull(self):
            '''bool DOM.AbstractView.isNull()'''
            return bool()
        def getComputedStyle(self, elt, pseudoElt):
            '''DOM.CSSStyleDeclaration DOM.AbstractView.getComputedStyle(DOM.Element elt, DOM.DOMString pseudoElt)'''
            return DOM.CSSStyleDeclaration()
        def document(self):
            '''DOM.Document DOM.AbstractView.document()'''
            return DOM.Document()
    class HTMLHtmlElement(DOM.HTMLElement):
        """"""
        def __init__(self):
            '''void DOM.HTMLHtmlElement.__init__()'''
        def __init__(self, other):
            '''void DOM.HTMLHtmlElement.__init__(DOM.HTMLHtmlElement other)'''
        def __init__(self, other):
            '''void DOM.HTMLHtmlElement.__init__(DOM.Node other)'''
        def setVersion(self):
            '''DOM.DOMString DOM.HTMLHtmlElement.setVersion()'''
            return DOM.DOMString()
        def version(self):
            '''DOM.DOMString DOM.HTMLHtmlElement.version()'''
            return DOM.DOMString()
    class HTMLTableColElement(DOM.HTMLElement):
        """"""
        def __init__(self):
            '''void DOM.HTMLTableColElement.__init__()'''
        def __init__(self, other):
            '''void DOM.HTMLTableColElement.__init__(DOM.HTMLTableColElement other)'''
        def __init__(self, other):
            '''void DOM.HTMLTableColElement.__init__(DOM.Node other)'''
        def setWidth(self):
            '''DOM.DOMString DOM.HTMLTableColElement.setWidth()'''
            return DOM.DOMString()
        def width(self):
            '''DOM.DOMString DOM.HTMLTableColElement.width()'''
            return DOM.DOMString()
        def setVAlign(self):
            '''DOM.DOMString DOM.HTMLTableColElement.setVAlign()'''
            return DOM.DOMString()
        def vAlign(self):
            '''DOM.DOMString DOM.HTMLTableColElement.vAlign()'''
            return DOM.DOMString()
        def setSpan(self):
            '''int DOM.HTMLTableColElement.setSpan()'''
            return int()
        def span(self):
            '''int DOM.HTMLTableColElement.span()'''
            return int()
        def setChOff(self):
            '''DOM.DOMString DOM.HTMLTableColElement.setChOff()'''
            return DOM.DOMString()
        def chOff(self):
            '''DOM.DOMString DOM.HTMLTableColElement.chOff()'''
            return DOM.DOMString()
        def setCh(self):
            '''DOM.DOMString DOM.HTMLTableColElement.setCh()'''
            return DOM.DOMString()
        def ch(self):
            '''DOM.DOMString DOM.HTMLTableColElement.ch()'''
            return DOM.DOMString()
        def setAlign(self):
            '''DOM.DOMString DOM.HTMLTableColElement.setAlign()'''
            return DOM.DOMString()
        def align(self):
            '''DOM.DOMString DOM.HTMLTableColElement.align()'''
            return DOM.DOMString()
    class EventListener(DOM.DomShared):
        """"""
        def __init__(self):
            '''void DOM.EventListener.__init__()'''
        def __init__(self):
            '''DOM.EventListener DOM.EventListener.__init__()'''
            return DOM.EventListener()
        def eventListenerType(self):
            '''DOM.DOMString DOM.EventListener.eventListenerType()'''
            return DOM.DOMString()
        def handleEvent(self, evt):
            '''void DOM.EventListener.handleEvent(DOM.Event evt)'''
    class Comment(DOM.CharacterData):
        """"""
        def __init__(self):
            '''void DOM.Comment.__init__()'''
        def __init__(self, other):
            '''void DOM.Comment.__init__(DOM.Comment other)'''
        def __init__(self, other):
            '''void DOM.Comment.__init__(DOM.Node other)'''
    class Node():
        """"""
        # Enum DOM.Node.DocumentPosition
        DOCUMENT_POSITION_DISCONNECTED = 0
        DOCUMENT_POSITION_PRECEDING = 0
        DOCUMENT_POSITION_FOLLOWING = 0
        DOCUMENT_POSITION_CONTAINS = 0
        DOCUMENT_POSITION_CONTAINED_BY = 0
        DOCUMENT_POSITION_IMPLEMENTATION_SPECIFIC = 0
    
        # Enum DOM.Node.NodeType
        ELEMENT_NODE = 0
        ATTRIBUTE_NODE = 0
        TEXT_NODE = 0
        CDATA_SECTION_NODE = 0
        ENTITY_REFERENCE_NODE = 0
        ENTITY_NODE = 0
        PROCESSING_INSTRUCTION_NODE = 0
        COMMENT_NODE = 0
        DOCUMENT_NODE = 0
        DOCUMENT_TYPE_NODE = 0
        DOCUMENT_FRAGMENT_NODE = 0
        NOTATION_NODE = 0
        XPATH_NAMESPACE_NODE = 0
    
        def __init__(self):
            '''void DOM.Node.__init__()'''
        def __init__(self, other):
            '''void DOM.Node.__init__(DOM.Node other)'''
        def getRect(self):
            '''QRect DOM.Node.getRect()'''
            return QRect()
        def getCursor(self, offset, _x, _y, height):
            '''void DOM.Node.getCursor(int offset, int _x, int _y, int height)'''
        def applyChanges(self):
            '''void DOM.Node.applyChanges()'''
        def toHTML(self):
            '''QString DOM.Node.toHTML()'''
            return QString()
        def index(self):
            '''int DOM.Node.index()'''
            return int()
        def isNull(self):
            '''bool DOM.Node.isNull()'''
            return bool()
        def elementId(self):
            '''int DOM.Node.elementId()'''
            return int()
        def compareDocumentPosition(self, other):
            '''int DOM.Node.compareDocumentPosition(DOM.Node other)'''
            return int()
        def setTextContent(self, text):
            '''void DOM.Node.setTextContent(DOM.DOMString text)'''
        def textContent(self):
            '''DOM.DOMString DOM.Node.textContent()'''
            return DOM.DOMString()
        def dispatchEvent(self, evt):
            '''bool DOM.Node.dispatchEvent(DOM.Event evt)'''
            return bool()
        def removeEventListener(self, type, listener, useCapture):
            '''void DOM.Node.removeEventListener(DOM.DOMString type, DOM.EventListener listener, bool useCapture)'''
        def addEventListener(self, type, listener, useCapture):
            '''void DOM.Node.addEventListener(DOM.DOMString type, DOM.EventListener listener, bool useCapture)'''
        def hasAttributes(self):
            '''bool DOM.Node.hasAttributes()'''
            return bool()
        def localName(self):
            '''DOM.DOMString DOM.Node.localName()'''
            return DOM.DOMString()
        def setPrefix(self, prefix):
            '''void DOM.Node.setPrefix(DOM.DOMString prefix)'''
        def prefix(self):
            '''DOM.DOMString DOM.Node.prefix()'''
            return DOM.DOMString()
        def namespaceURI(self):
            '''DOM.DOMString DOM.Node.namespaceURI()'''
            return DOM.DOMString()
        def isSupported(self, feature, version):
            '''bool DOM.Node.isSupported(DOM.DOMString feature, DOM.DOMString version)'''
            return bool()
        def normalize(self):
            '''void DOM.Node.normalize()'''
        def cloneNode(self, deep):
            '''DOM.Node DOM.Node.cloneNode(bool deep)'''
            return DOM.Node()
        def hasChildNodes(self):
            '''bool DOM.Node.hasChildNodes()'''
            return bool()
        def appendChild(self, newChild):
            '''DOM.Node DOM.Node.appendChild(DOM.Node newChild)'''
            return DOM.Node()
        def removeChild(self, oldChild):
            '''DOM.Node DOM.Node.removeChild(DOM.Node oldChild)'''
            return DOM.Node()
        def replaceChild(self, newChild, oldChild):
            '''DOM.Node DOM.Node.replaceChild(DOM.Node newChild, DOM.Node oldChild)'''
            return DOM.Node()
        def insertBefore(self, newChild, refChild):
            '''DOM.Node DOM.Node.insertBefore(DOM.Node newChild, DOM.Node refChild)'''
            return DOM.Node()
        def ownerDocument(self):
            '''DOM.Document DOM.Node.ownerDocument()'''
            return DOM.Document()
        def attributes(self):
            '''DOM.NamedNodeMap DOM.Node.attributes()'''
            return DOM.NamedNodeMap()
        def nextSibling(self):
            '''DOM.Node DOM.Node.nextSibling()'''
            return DOM.Node()
        def previousSibling(self):
            '''DOM.Node DOM.Node.previousSibling()'''
            return DOM.Node()
        def lastChild(self):
            '''DOM.Node DOM.Node.lastChild()'''
            return DOM.Node()
        def firstChild(self):
            '''DOM.Node DOM.Node.firstChild()'''
            return DOM.Node()
        def childNodes(self):
            '''DOM.NodeList DOM.Node.childNodes()'''
            return DOM.NodeList()
        def parentNode(self):
            '''DOM.Node DOM.Node.parentNode()'''
            return DOM.Node()
        def nodeType(self):
            '''int DOM.Node.nodeType()'''
            return int()
        def setNodeValue(self):
            '''DOM.DOMString DOM.Node.setNodeValue()'''
            return DOM.DOMString()
        def nodeValue(self):
            '''DOM.DOMString DOM.Node.nodeValue()'''
            return DOM.DOMString()
        def nodeName(self):
            '''DOM.DOMString DOM.Node.nodeName()'''
            return DOM.DOMString()
        def __ne__(self, other):
            '''bool DOM.Node.__ne__(DOM.Node other)'''
            return bool()
        def __eq__(self, other):
            '''bool DOM.Node.__eq__(DOM.Node other)'''
            return bool()
    class HTMLTextAreaElement(DOM.HTMLElement):
        """"""
        def __init__(self):
            '''void DOM.HTMLTextAreaElement.__init__()'''
        def __init__(self, other):
            '''void DOM.HTMLTextAreaElement.__init__(DOM.HTMLTextAreaElement other)'''
        def __init__(self, other):
            '''void DOM.HTMLTextAreaElement.__init__(DOM.Node other)'''
        def textLength(self):
            '''int DOM.HTMLTextAreaElement.textLength()'''
            return int()
        def setSelectionRange(self, start, end):
            '''void DOM.HTMLTextAreaElement.setSelectionRange(int start, int end)'''
        def setSelectionEnd(self, offset):
            '''void DOM.HTMLTextAreaElement.setSelectionEnd(int offset)'''
        def selectionEnd(self):
            '''int DOM.HTMLTextAreaElement.selectionEnd()'''
            return int()
        def setSelectionStart(self, offset):
            '''void DOM.HTMLTextAreaElement.setSelectionStart(int offset)'''
        def selectionStart(self):
            '''int DOM.HTMLTextAreaElement.selectionStart()'''
            return int()
        def select(self):
            '''void DOM.HTMLTextAreaElement.select()'''
        def focus(self):
            '''void DOM.HTMLTextAreaElement.focus()'''
        def blur(self):
            '''void DOM.HTMLTextAreaElement.blur()'''
        def setValue(self):
            '''DOM.DOMString DOM.HTMLTextAreaElement.setValue()'''
            return DOM.DOMString()
        def value(self):
            '''DOM.DOMString DOM.HTMLTextAreaElement.value()'''
            return DOM.DOMString()
        def type(self):
            '''DOM.DOMString DOM.HTMLTextAreaElement.type()'''
            return DOM.DOMString()
        def setTabIndex(self):
            '''int DOM.HTMLTextAreaElement.setTabIndex()'''
            return int()
        def tabIndex(self):
            '''int DOM.HTMLTextAreaElement.tabIndex()'''
            return int()
        def setRows(self):
            '''int DOM.HTMLTextAreaElement.setRows()'''
            return int()
        def rows(self):
            '''int DOM.HTMLTextAreaElement.rows()'''
            return int()
        def setReadOnly(self):
            '''bool DOM.HTMLTextAreaElement.setReadOnly()'''
            return bool()
        def readOnly(self):
            '''bool DOM.HTMLTextAreaElement.readOnly()'''
            return bool()
        def setName(self):
            '''DOM.DOMString DOM.HTMLTextAreaElement.setName()'''
            return DOM.DOMString()
        def name(self):
            '''DOM.DOMString DOM.HTMLTextAreaElement.name()'''
            return DOM.DOMString()
        def setDisabled(self):
            '''bool DOM.HTMLTextAreaElement.setDisabled()'''
            return bool()
        def disabled(self):
            '''bool DOM.HTMLTextAreaElement.disabled()'''
            return bool()
        def setCols(self):
            '''int DOM.HTMLTextAreaElement.setCols()'''
            return int()
        def cols(self):
            '''int DOM.HTMLTextAreaElement.cols()'''
            return int()
        def setAccessKey(self):
            '''DOM.DOMString DOM.HTMLTextAreaElement.setAccessKey()'''
            return DOM.DOMString()
        def accessKey(self):
            '''DOM.DOMString DOM.HTMLTextAreaElement.accessKey()'''
            return DOM.DOMString()
        def form(self):
            '''DOM.HTMLFormElement DOM.HTMLTextAreaElement.form()'''
            return DOM.HTMLFormElement()
        def setDefaultValue(self):
            '''DOM.DOMString DOM.HTMLTextAreaElement.setDefaultValue()'''
            return DOM.DOMString()
        def defaultValue(self):
            '''DOM.DOMString DOM.HTMLTextAreaElement.defaultValue()'''
            return DOM.DOMString()
    class HTMLBodyElement(DOM.HTMLElement):
        """"""
        def __init__(self):
            '''void DOM.HTMLBodyElement.__init__()'''
        def __init__(self, other):
            '''void DOM.HTMLBodyElement.__init__(DOM.HTMLBodyElement other)'''
        def __init__(self, other):
            '''void DOM.HTMLBodyElement.__init__(DOM.Node other)'''
        def setVLink(self):
            '''DOM.DOMString DOM.HTMLBodyElement.setVLink()'''
            return DOM.DOMString()
        def vLink(self):
            '''DOM.DOMString DOM.HTMLBodyElement.vLink()'''
            return DOM.DOMString()
        def setText(self):
            '''DOM.DOMString DOM.HTMLBodyElement.setText()'''
            return DOM.DOMString()
        def text(self):
            '''DOM.DOMString DOM.HTMLBodyElement.text()'''
            return DOM.DOMString()
        def setLink(self):
            '''DOM.DOMString DOM.HTMLBodyElement.setLink()'''
            return DOM.DOMString()
        def link(self):
            '''DOM.DOMString DOM.HTMLBodyElement.link()'''
            return DOM.DOMString()
        def setBgColor(self):
            '''DOM.DOMString DOM.HTMLBodyElement.setBgColor()'''
            return DOM.DOMString()
        def bgColor(self):
            '''DOM.DOMString DOM.HTMLBodyElement.bgColor()'''
            return DOM.DOMString()
        def setBackground(self):
            '''DOM.DOMString DOM.HTMLBodyElement.setBackground()'''
            return DOM.DOMString()
        def background(self):
            '''DOM.DOMString DOM.HTMLBodyElement.background()'''
            return DOM.DOMString()
        def setALink(self):
            '''DOM.DOMString DOM.HTMLBodyElement.setALink()'''
            return DOM.DOMString()
        def aLink(self):
            '''DOM.DOMString DOM.HTMLBodyElement.aLink()'''
            return DOM.DOMString()
    class HTMLImageElement(DOM.HTMLElement):
        """"""
        def __init__(self):
            '''void DOM.HTMLImageElement.__init__()'''
        def __init__(self, other):
            '''void DOM.HTMLImageElement.__init__(DOM.HTMLImageElement other)'''
        def __init__(self, other):
            '''void DOM.HTMLImageElement.__init__(DOM.Node other)'''
        def y(self):
            '''int DOM.HTMLImageElement.y()'''
            return int()
        def x(self):
            '''int DOM.HTMLImageElement.x()'''
            return int()
        def setWidth(self):
            '''int DOM.HTMLImageElement.setWidth()'''
            return int()
        def width(self):
            '''int DOM.HTMLImageElement.width()'''
            return int()
        def setVspace(self):
            '''int DOM.HTMLImageElement.setVspace()'''
            return int()
        def vspace(self):
            '''int DOM.HTMLImageElement.vspace()'''
            return int()
        def setUseMap(self):
            '''DOM.DOMString DOM.HTMLImageElement.setUseMap()'''
            return DOM.DOMString()
        def useMap(self):
            '''DOM.DOMString DOM.HTMLImageElement.useMap()'''
            return DOM.DOMString()
        def setSrc(self):
            '''DOM.DOMString DOM.HTMLImageElement.setSrc()'''
            return DOM.DOMString()
        def src(self):
            '''DOM.DOMString DOM.HTMLImageElement.src()'''
            return DOM.DOMString()
        def setLongDesc(self):
            '''DOM.DOMString DOM.HTMLImageElement.setLongDesc()'''
            return DOM.DOMString()
        def longDesc(self):
            '''DOM.DOMString DOM.HTMLImageElement.longDesc()'''
            return DOM.DOMString()
        def setIsMap(self):
            '''bool DOM.HTMLImageElement.setIsMap()'''
            return bool()
        def isMap(self):
            '''bool DOM.HTMLImageElement.isMap()'''
            return bool()
        def setHspace(self):
            '''int DOM.HTMLImageElement.setHspace()'''
            return int()
        def hspace(self):
            '''int DOM.HTMLImageElement.hspace()'''
            return int()
        def setHeight(self):
            '''int DOM.HTMLImageElement.setHeight()'''
            return int()
        def height(self):
            '''int DOM.HTMLImageElement.height()'''
            return int()
        def border(self):
            '''int DOM.HTMLImageElement.border()'''
            return int()
        def setBorder(self):
            '''DOM.DOMString DOM.HTMLImageElement.setBorder()'''
            return DOM.DOMString()
        def setBorder(self):
            '''int DOM.HTMLImageElement.setBorder()'''
            return int()
        def getBorder(self):
            '''DOM.DOMString DOM.HTMLImageElement.getBorder()'''
            return DOM.DOMString()
        def setAlt(self):
            '''DOM.DOMString DOM.HTMLImageElement.setAlt()'''
            return DOM.DOMString()
        def alt(self):
            '''DOM.DOMString DOM.HTMLImageElement.alt()'''
            return DOM.DOMString()
        def setAlign(self):
            '''DOM.DOMString DOM.HTMLImageElement.setAlign()'''
            return DOM.DOMString()
        def align(self):
            '''DOM.DOMString DOM.HTMLImageElement.align()'''
            return DOM.DOMString()
        def setName(self):
            '''DOM.DOMString DOM.HTMLImageElement.setName()'''
            return DOM.DOMString()
        def name(self):
            '''DOM.DOMString DOM.HTMLImageElement.name()'''
            return DOM.DOMString()
    class HTMLElement(DOM.Element):
        """"""
        def __init__(self):
            '''void DOM.HTMLElement.__init__()'''
        def __init__(self, other):
            '''void DOM.HTMLElement.__init__(DOM.HTMLElement other)'''
        def __init__(self, other):
            '''void DOM.HTMLElement.__init__(DOM.Node other)'''
        def assignOther(self, other, elementId):
            '''void DOM.HTMLElement.assignOther(DOM.Node other, int elementId)'''
        def addCSSProperty(self, property, value):
            '''void DOM.HTMLElement.addCSSProperty(DOM.DOMString property, DOM.DOMString value)'''
        def removeCSSProperty(self, property):
            '''void DOM.HTMLElement.removeCSSProperty(DOM.DOMString property)'''
        def setContentEditable(self, enabled):
            '''void DOM.HTMLElement.setContentEditable(DOM.DOMString enabled)'''
        def contentEditable(self):
            '''DOM.DOMString DOM.HTMLElement.contentEditable()'''
            return DOM.DOMString()
        def isContentEditable(self):
            '''bool DOM.HTMLElement.isContentEditable()'''
            return bool()
        def all(self):
            '''DOM.HTMLCollection DOM.HTMLElement.all()'''
            return DOM.HTMLCollection()
        def children(self):
            '''DOM.HTMLCollection DOM.HTMLElement.children()'''
            return DOM.HTMLCollection()
        def setInnerText(self, text):
            '''void DOM.HTMLElement.setInnerText(DOM.DOMString text)'''
        def innerText(self):
            '''DOM.DOMString DOM.HTMLElement.innerText()'''
            return DOM.DOMString()
        def setInnerHTML(self, html):
            '''void DOM.HTMLElement.setInnerHTML(DOM.DOMString html)'''
        def innerHTML(self):
            '''DOM.DOMString DOM.HTMLElement.innerHTML()'''
            return DOM.DOMString()
        def setClassName(self):
            '''DOM.DOMString DOM.HTMLElement.setClassName()'''
            return DOM.DOMString()
        def className(self):
            '''DOM.DOMString DOM.HTMLElement.className()'''
            return DOM.DOMString()
        def setDir(self):
            '''DOM.DOMString DOM.HTMLElement.setDir()'''
            return DOM.DOMString()
        def dir(self):
            '''DOM.DOMString DOM.HTMLElement.dir()'''
            return DOM.DOMString()
        def setLang(self):
            '''DOM.DOMString DOM.HTMLElement.setLang()'''
            return DOM.DOMString()
        def lang(self):
            '''DOM.DOMString DOM.HTMLElement.lang()'''
            return DOM.DOMString()
        def setTitle(self):
            '''DOM.DOMString DOM.HTMLElement.setTitle()'''
            return DOM.DOMString()
        def title(self):
            '''DOM.DOMString DOM.HTMLElement.title()'''
            return DOM.DOMString()
        def setId(self):
            '''DOM.DOMString DOM.HTMLElement.setId()'''
            return DOM.DOMString()
        def id(self):
            '''DOM.DOMString DOM.HTMLElement.id()'''
            return DOM.DOMString()
    class HTMLLIElement(DOM.HTMLElement):
        """"""
        def __init__(self):
            '''void DOM.HTMLLIElement.__init__()'''
        def __init__(self, other):
            '''void DOM.HTMLLIElement.__init__(DOM.HTMLLIElement other)'''
        def __init__(self, other):
            '''void DOM.HTMLLIElement.__init__(DOM.Node other)'''
        def setValue(self):
            '''int DOM.HTMLLIElement.setValue()'''
            return int()
        def value(self):
            '''int DOM.HTMLLIElement.value()'''
            return int()
        def setType(self):
            '''DOM.DOMString DOM.HTMLLIElement.setType()'''
            return DOM.DOMString()
        def type(self):
            '''DOM.DOMString DOM.HTMLLIElement.type()'''
            return DOM.DOMString()
    class CSSRuleList():
        """"""
        def __init__(self):
            '''void DOM.CSSRuleList.__init__()'''
        def __init__(self, other):
            '''void DOM.CSSRuleList.__init__(DOM.CSSRuleList other)'''
        def isNull(self):
            '''bool DOM.CSSRuleList.isNull()'''
            return bool()
        def item(self, index):
            '''DOM.CSSRule DOM.CSSRuleList.item(int index)'''
            return DOM.CSSRule()
        def length(self):
            '''int DOM.CSSRuleList.length()'''
            return int()
    class HTMLOListElement(DOM.HTMLElement):
        """"""
        def __init__(self):
            '''void DOM.HTMLOListElement.__init__()'''
        def __init__(self, other):
            '''void DOM.HTMLOListElement.__init__(DOM.HTMLOListElement other)'''
        def __init__(self, other):
            '''void DOM.HTMLOListElement.__init__(DOM.Node other)'''
        def setType(self):
            '''DOM.DOMString DOM.HTMLOListElement.setType()'''
            return DOM.DOMString()
        def type(self):
            '''DOM.DOMString DOM.HTMLOListElement.type()'''
            return DOM.DOMString()
        def setStart(self):
            '''int DOM.HTMLOListElement.setStart()'''
            return int()
        def start(self):
            '''int DOM.HTMLOListElement.start()'''
            return int()
        def setCompact(self):
            '''bool DOM.HTMLOListElement.setCompact()'''
            return bool()
        def compact(self):
            '''bool DOM.HTMLOListElement.compact()'''
            return bool()
    class StyleSheet():
        """"""
        def __init__(self):
            '''void DOM.StyleSheet.__init__()'''
        def __init__(self, other):
            '''void DOM.StyleSheet.__init__(DOM.StyleSheet other)'''
        def isNull(self):
            '''bool DOM.StyleSheet.isNull()'''
            return bool()
        def isCSSStyleSheet(self):
            '''bool DOM.StyleSheet.isCSSStyleSheet()'''
            return bool()
        def baseUrl(self):
            '''KUrl DOM.StyleSheet.baseUrl()'''
            return KUrl()
        def media(self):
            '''DOM.MediaList DOM.StyleSheet.media()'''
            return DOM.MediaList()
        def title(self):
            '''DOM.DOMString DOM.StyleSheet.title()'''
            return DOM.DOMString()
        def href(self):
            '''DOM.DOMString DOM.StyleSheet.href()'''
            return DOM.DOMString()
        def parentStyleSheet(self):
            '''DOM.StyleSheet DOM.StyleSheet.parentStyleSheet()'''
            return DOM.StyleSheet()
        def ownerNode(self):
            '''DOM.Node DOM.StyleSheet.ownerNode()'''
            return DOM.Node()
        def setDisabled(self):
            '''bool DOM.StyleSheet.setDisabled()'''
            return bool()
        def disabled(self):
            '''bool DOM.StyleSheet.disabled()'''
            return bool()
        def type(self):
            '''DOM.DOMString DOM.StyleSheet.type()'''
            return DOM.DOMString()
    class CDATASection(DOM.Text):
        """"""
        def __init__(self):
            '''void DOM.CDATASection.__init__()'''
        def __init__(self, other):
            '''void DOM.CDATASection.__init__(DOM.CDATASection other)'''
        def __init__(self, other):
            '''void DOM.CDATASection.__init__(DOM.Node other)'''
    class HTMLTableSectionElement(DOM.HTMLElement):
        """"""
        def __init__(self):
            '''void DOM.HTMLTableSectionElement.__init__()'''
        def __init__(self, other):
            '''void DOM.HTMLTableSectionElement.__init__(DOM.HTMLTableSectionElement other)'''
        def __init__(self, other):
            '''void DOM.HTMLTableSectionElement.__init__(DOM.Node other)'''
        def deleteRow(self, index):
            '''void DOM.HTMLTableSectionElement.deleteRow(int index)'''
        def insertRow(self, index):
            '''DOM.HTMLElement DOM.HTMLTableSectionElement.insertRow(int index)'''
            return DOM.HTMLElement()
        def rows(self):
            '''DOM.HTMLCollection DOM.HTMLTableSectionElement.rows()'''
            return DOM.HTMLCollection()
        def setVAlign(self):
            '''DOM.DOMString DOM.HTMLTableSectionElement.setVAlign()'''
            return DOM.DOMString()
        def vAlign(self):
            '''DOM.DOMString DOM.HTMLTableSectionElement.vAlign()'''
            return DOM.DOMString()
        def setChOff(self):
            '''DOM.DOMString DOM.HTMLTableSectionElement.setChOff()'''
            return DOM.DOMString()
        def chOff(self):
            '''DOM.DOMString DOM.HTMLTableSectionElement.chOff()'''
            return DOM.DOMString()
        def setCh(self):
            '''DOM.DOMString DOM.HTMLTableSectionElement.setCh()'''
            return DOM.DOMString()
        def ch(self):
            '''DOM.DOMString DOM.HTMLTableSectionElement.ch()'''
            return DOM.DOMString()
        def setAlign(self):
            '''DOM.DOMString DOM.HTMLTableSectionElement.setAlign()'''
            return DOM.DOMString()
        def align(self):
            '''DOM.DOMString DOM.HTMLTableSectionElement.align()'''
            return DOM.DOMString()
    class HTMLHeadElement(DOM.HTMLElement):
        """"""
        def __init__(self):
            '''void DOM.HTMLHeadElement.__init__()'''
        def __init__(self, other):
            '''void DOM.HTMLHeadElement.__init__(DOM.HTMLHeadElement other)'''
        def __init__(self, other):
            '''void DOM.HTMLHeadElement.__init__(DOM.Node other)'''
        def setProfile(self):
            '''DOM.DOMString DOM.HTMLHeadElement.setProfile()'''
            return DOM.DOMString()
        def profile(self):
            '''DOM.DOMString DOM.HTMLHeadElement.profile()'''
            return DOM.DOMString()
    class HTMLLegendElement(DOM.HTMLElement):
        """"""
        def __init__(self):
            '''void DOM.HTMLLegendElement.__init__()'''
        def __init__(self, other):
            '''void DOM.HTMLLegendElement.__init__(DOM.HTMLLegendElement other)'''
        def __init__(self, other):
            '''void DOM.HTMLLegendElement.__init__(DOM.Node other)'''
        def setAlign(self):
            '''DOM.DOMString DOM.HTMLLegendElement.setAlign()'''
            return DOM.DOMString()
        def align(self):
            '''DOM.DOMString DOM.HTMLLegendElement.align()'''
            return DOM.DOMString()
        def setAccessKey(self):
            '''DOM.DOMString DOM.HTMLLegendElement.setAccessKey()'''
            return DOM.DOMString()
        def accessKey(self):
            '''DOM.DOMString DOM.HTMLLegendElement.accessKey()'''
            return DOM.DOMString()
        def form(self):
            '''DOM.HTMLFormElement DOM.HTMLLegendElement.form()'''
            return DOM.HTMLFormElement()
    class Document(DOM.Node):
        """"""
        def __init__(self):
            '''void DOM.Document.__init__()'''
        def __init__(self):
            '''bool DOM.Document.__init__()'''
            return bool()
        def __init__(self, other):
            '''void DOM.Document.__init__(DOM.Document other)'''
        def __init__(self, other):
            '''void DOM.Document.__init__(DOM.Node other)'''
        def querySelectorAll(self, query):
            '''DOM.NodeList DOM.Document.querySelectorAll(DOM.DOMString query)'''
            return DOM.NodeList()
        def querySelector(self, query):
            '''DOM.Element DOM.Document.querySelector(DOM.DOMString query)'''
            return DOM.Element()
        def updateRendering(self):
            '''void DOM.Document.updateRendering()'''
        def queryCommandValue(self, command):
            '''DOM.DOMString DOM.Document.queryCommandValue(DOM.DOMString command)'''
            return DOM.DOMString()
        def queryCommandSupported(self, command):
            '''bool DOM.Document.queryCommandSupported(DOM.DOMString command)'''
            return bool()
        def queryCommandState(self, command):
            '''bool DOM.Document.queryCommandState(DOM.DOMString command)'''
            return bool()
        def queryCommandIndeterm(self, command):
            '''bool DOM.Document.queryCommandIndeterm(DOM.DOMString command)'''
            return bool()
        def queryCommandEnabled(self, command):
            '''bool DOM.Document.queryCommandEnabled(DOM.DOMString command)'''
            return bool()
        def execCommand(self, command, userInterface, value):
            '''bool DOM.Document.execCommand(DOM.DOMString command, bool userInterface, DOM.DOMString value)'''
            return bool()
        def toString(self):
            '''DOM.DOMString DOM.Document.toString()'''
            return DOM.DOMString()
        def completeURL(self, url):
            '''DOM.DOMString DOM.Document.completeURL(DOM.DOMString url)'''
            return DOM.DOMString()
        def setDesignMode(self, enable):
            '''void DOM.Document.setDesignMode(bool enable)'''
        def designMode(self):
            '''bool DOM.Document.designMode()'''
            return bool()
        def loadXML(self, source):
            '''void DOM.Document.loadXML(DOM.DOMString source)'''
        def load(self, uri):
            '''void DOM.Document.load(DOM.DOMString uri)'''
        def abort(self):
            '''void DOM.Document.abort()'''
        def setAsync(self):
            '''bool DOM.Document.setAsync()'''
            return bool()
        def async(self):
            '''bool DOM.Document.async()'''
            return bool()
        def getOverrideStyle(self, elt, pseudoElt):
            '''DOM.CSSStyleDeclaration DOM.Document.getOverrideStyle(DOM.Element elt, DOM.DOMString pseudoElt)'''
            return DOM.CSSStyleDeclaration()
        def view(self):
            '''KHTMLView DOM.Document.view()'''
            return KHTMLView()
        def removeStyleSheet(self, sheet):
            '''void DOM.Document.removeStyleSheet(DOM.StyleSheet sheet)'''
        def addStyleSheet(self, sheet):
            '''void DOM.Document.addStyleSheet(DOM.StyleSheet sheet)'''
        def setSelectedStylesheetSet(self, aString):
            '''void DOM.Document.setSelectedStylesheetSet(DOM.DOMString aString)'''
        def selectedStylesheetSet(self):
            '''DOM.DOMString DOM.Document.selectedStylesheetSet()'''
            return DOM.DOMString()
        def preferredStylesheetSet(self):
            '''DOM.DOMString DOM.Document.preferredStylesheetSet()'''
            return DOM.DOMString()
        def styleSheets(self):
            '''DOM.StyleSheetList DOM.Document.styleSheets()'''
            return DOM.StyleSheetList()
        def defaultView(self):
            '''DOM.AbstractView DOM.Document.defaultView()'''
            return DOM.AbstractView()
        def createEvent(self, eventType):
            '''DOM.Event DOM.Document.createEvent(DOM.DOMString eventType)'''
            return DOM.Event()
        def createTreeWalker(self, root, whatToShow, filter, entityReferenceExpansion):
            '''DOM.TreeWalker DOM.Document.createTreeWalker(DOM.Node root, int whatToShow, DOM.NodeFilter filter, bool entityReferenceExpansion)'''
            return DOM.TreeWalker()
        def createNodeIterator(self, root, whatToShow, filter, entityReferenceExpansion):
            '''DOM.NodeIterator DOM.Document.createNodeIterator(DOM.Node root, int whatToShow, DOM.NodeFilter filter, bool entityReferenceExpansion)'''
            return DOM.NodeIterator()
        def createRange(self):
            '''DOM.Range DOM.Document.createRange()'''
            return DOM.Range()
        def isHTMLDocument(self):
            '''bool DOM.Document.isHTMLDocument()'''
            return bool()
        def importNode(self, importedNode, deep):
            '''DOM.Node DOM.Document.importNode(DOM.Node importedNode, bool deep)'''
            return DOM.Node()
        def getElementsByClassName(self, className):
            '''DOM.NodeList DOM.Document.getElementsByClassName(DOM.DOMString className)'''
            return DOM.NodeList()
        def getElementsByTagNameNS(self, namespaceURI, localName):
            '''DOM.NodeList DOM.Document.getElementsByTagNameNS(DOM.DOMString namespaceURI, DOM.DOMString localName)'''
            return DOM.NodeList()
        def getElementsByTagName(self, tagname):
            '''DOM.NodeList DOM.Document.getElementsByTagName(DOM.DOMString tagname)'''
            return DOM.NodeList()
        def getElementById(self, elementId):
            '''DOM.Element DOM.Document.getElementById(DOM.DOMString elementId)'''
            return DOM.Element()
        def createEntityReference(self, name):
            '''DOM.EntityReference DOM.Document.createEntityReference(DOM.DOMString name)'''
            return DOM.EntityReference()
        def createAttributeNS(self, namespaceURI, qualifiedName):
            '''DOM.Attr DOM.Document.createAttributeNS(DOM.DOMString namespaceURI, DOM.DOMString qualifiedName)'''
            return DOM.Attr()
        def createAttribute(self, name):
            '''DOM.Attr DOM.Document.createAttribute(DOM.DOMString name)'''
            return DOM.Attr()
        def createProcessingInstruction(self, target, data):
            '''DOM.ProcessingInstruction DOM.Document.createProcessingInstruction(DOM.DOMString target, DOM.DOMString data)'''
            return DOM.ProcessingInstruction()
        def createCDATASection(self, data):
            '''DOM.CDATASection DOM.Document.createCDATASection(DOM.DOMString data)'''
            return DOM.CDATASection()
        def createComment(self, data):
            '''DOM.Comment DOM.Document.createComment(DOM.DOMString data)'''
            return DOM.Comment()
        def createTextNode(self, data):
            '''DOM.Text DOM.Document.createTextNode(DOM.DOMString data)'''
            return DOM.Text()
        def createDocumentFragment(self):
            '''DOM.DocumentFragment DOM.Document.createDocumentFragment()'''
            return DOM.DocumentFragment()
        def createElementNS(self, namespaceURI, qualifiedName):
            '''DOM.Element DOM.Document.createElementNS(DOM.DOMString namespaceURI, DOM.DOMString qualifiedName)'''
            return DOM.Element()
        def createElement(self, tagName):
            '''DOM.Element DOM.Document.createElement(DOM.DOMString tagName)'''
            return DOM.Element()
        def documentElement(self):
            '''DOM.Element DOM.Document.documentElement()'''
            return DOM.Element()
        def implementation(self):
            '''DOM.DOMImplementation DOM.Document.implementation()'''
            return DOM.DOMImplementation()
        def doctype(self):
            '''DOM.DocumentType DOM.Document.doctype()'''
            return DOM.DocumentType()
    class RGBColor():
        """"""
        def __init__(self):
            '''void DOM.RGBColor.__init__()'''
        def __init__(self, c):
            '''void DOM.RGBColor.__init__(QColor c)'''
        def __init__(self, color):
            '''void DOM.RGBColor.__init__(int color)'''
        def __init__(self, other):
            '''void DOM.RGBColor.__init__(DOM.RGBColor other)'''
        def color(self):
            '''int DOM.RGBColor.color()'''
            return int()
        def blue(self):
            '''DOM.CSSPrimitiveValue DOM.RGBColor.blue()'''
            return DOM.CSSPrimitiveValue()
        def green(self):
            '''DOM.CSSPrimitiveValue DOM.RGBColor.green()'''
            return DOM.CSSPrimitiveValue()
        def red(self):
            '''DOM.CSSPrimitiveValue DOM.RGBColor.red()'''
            return DOM.CSSPrimitiveValue()
    class HTMLParamElement(DOM.HTMLElement):
        """"""
        def __init__(self):
            '''void DOM.HTMLParamElement.__init__()'''
        def __init__(self, other):
            '''void DOM.HTMLParamElement.__init__(DOM.HTMLParamElement other)'''
        def __init__(self, other):
            '''void DOM.HTMLParamElement.__init__(DOM.Node other)'''
        def setValueType(self):
            '''DOM.DOMString DOM.HTMLParamElement.setValueType()'''
            return DOM.DOMString()
        def valueType(self):
            '''DOM.DOMString DOM.HTMLParamElement.valueType()'''
            return DOM.DOMString()
        def setValue(self):
            '''DOM.DOMString DOM.HTMLParamElement.setValue()'''
            return DOM.DOMString()
        def value(self):
            '''DOM.DOMString DOM.HTMLParamElement.value()'''
            return DOM.DOMString()
        def setType(self):
            '''DOM.DOMString DOM.HTMLParamElement.setType()'''
            return DOM.DOMString()
        def type(self):
            '''DOM.DOMString DOM.HTMLParamElement.type()'''
            return DOM.DOMString()
        def setName(self):
            '''DOM.DOMString DOM.HTMLParamElement.setName()'''
            return DOM.DOMString()
        def name(self):
            '''DOM.DOMString DOM.HTMLParamElement.name()'''
            return DOM.DOMString()
    class CSSPageRule(DOM.CSSRule):
        """"""
        def __init__(self):
            '''void DOM.CSSPageRule.__init__()'''
        def __init__(self, other):
            '''void DOM.CSSPageRule.__init__(DOM.CSSPageRule other)'''
        def __init__(self, other):
            '''void DOM.CSSPageRule.__init__(DOM.CSSRule other)'''
        def style(self):
            '''DOM.CSSStyleDeclaration DOM.CSSPageRule.style()'''
            return DOM.CSSStyleDeclaration()
        def setSelectorText(self):
            '''DOM.DOMString DOM.CSSPageRule.setSelectorText()'''
            return DOM.DOMString()
        def selectorText(self):
            '''DOM.DOMString DOM.CSSPageRule.selectorText()'''
            return DOM.DOMString()
    class HTMLLayerElement(DOM.HTMLElement):
        """"""
        def __init__(self):
            '''void DOM.HTMLLayerElement.__init__()'''
        def __init__(self, other):
            '''void DOM.HTMLLayerElement.__init__(DOM.HTMLLayerElement other)'''
        def __init__(self, other):
            '''void DOM.HTMLLayerElement.__init__(DOM.Node other)'''
        def layers(self):
            '''DOM.HTMLCollection DOM.HTMLLayerElement.layers()'''
            return DOM.HTMLCollection()
        def setBgColor(self):
            '''DOM.DOMString DOM.HTMLLayerElement.setBgColor()'''
            return DOM.DOMString()
        def bgColor(self):
            '''DOM.DOMString DOM.HTMLLayerElement.bgColor()'''
            return DOM.DOMString()
        def setVisibility(self):
            '''DOM.DOMString DOM.HTMLLayerElement.setVisibility()'''
            return DOM.DOMString()
        def visibility(self):
            '''DOM.DOMString DOM.HTMLLayerElement.visibility()'''
            return DOM.DOMString()
        def setLeft(self):
            '''int DOM.HTMLLayerElement.setLeft()'''
            return int()
        def left(self):
            '''int DOM.HTMLLayerElement.left()'''
            return int()
        def setTop(self):
            '''int DOM.HTMLLayerElement.setTop()'''
            return int()
        def top(self):
            '''int DOM.HTMLLayerElement.top()'''
            return int()
    class ProcessingInstruction(DOM.Node):
        """"""
        def __init__(self):
            '''void DOM.ProcessingInstruction.__init__()'''
        def __init__(self, other):
            '''void DOM.ProcessingInstruction.__init__(DOM.ProcessingInstruction other)'''
        def __init__(self, other):
            '''void DOM.ProcessingInstruction.__init__(DOM.Node other)'''
        def sheet(self):
            '''DOM.StyleSheet DOM.ProcessingInstruction.sheet()'''
            return DOM.StyleSheet()
        def setData(self):
            '''DOM.DOMString DOM.ProcessingInstruction.setData()'''
            return DOM.DOMString()
        def data(self):
            '''DOM.DOMString DOM.ProcessingInstruction.data()'''
            return DOM.DOMString()
        def target(self):
            '''DOM.DOMString DOM.ProcessingInstruction.target()'''
            return DOM.DOMString()
    class HTMLAppletElement(DOM.HTMLElement):
        """"""
        def __init__(self):
            '''void DOM.HTMLAppletElement.__init__()'''
        def __init__(self, other):
            '''void DOM.HTMLAppletElement.__init__(DOM.HTMLAppletElement other)'''
        def __init__(self, other):
            '''void DOM.HTMLAppletElement.__init__(DOM.Node other)'''
        def setWidth(self):
            '''DOM.DOMString DOM.HTMLAppletElement.setWidth()'''
            return DOM.DOMString()
        def width(self):
            '''DOM.DOMString DOM.HTMLAppletElement.width()'''
            return DOM.DOMString()
        def vspace(self):
            '''DOM.DOMString DOM.HTMLAppletElement.vspace()'''
            return DOM.DOMString()
        def setVspace(self):
            '''int DOM.HTMLAppletElement.setVspace()'''
            return int()
        def setVspace(self):
            '''DOM.DOMString DOM.HTMLAppletElement.setVspace()'''
            return DOM.DOMString()
        def getVspace(self):
            '''int DOM.HTMLAppletElement.getVspace()'''
            return int()
        def setObject(self):
            '''DOM.DOMString DOM.HTMLAppletElement.setObject()'''
            return DOM.DOMString()
        def object(self):
            '''DOM.DOMString DOM.HTMLAppletElement.object()'''
            return DOM.DOMString()
        def setName(self):
            '''DOM.DOMString DOM.HTMLAppletElement.setName()'''
            return DOM.DOMString()
        def name(self):
            '''DOM.DOMString DOM.HTMLAppletElement.name()'''
            return DOM.DOMString()
        def hspace(self):
            '''DOM.DOMString DOM.HTMLAppletElement.hspace()'''
            return DOM.DOMString()
        def setHspace(self):
            '''int DOM.HTMLAppletElement.setHspace()'''
            return int()
        def setHspace(self, value):
            '''void DOM.HTMLAppletElement.setHspace(DOM.DOMString value)'''
        def getHspace(self):
            '''int DOM.HTMLAppletElement.getHspace()'''
            return int()
        def setHeight(self):
            '''DOM.DOMString DOM.HTMLAppletElement.setHeight()'''
            return DOM.DOMString()
        def height(self):
            '''DOM.DOMString DOM.HTMLAppletElement.height()'''
            return DOM.DOMString()
        def setCodeBase(self, value):
            '''void DOM.HTMLAppletElement.setCodeBase(DOM.DOMString value)'''
        def codeBase(self):
            '''DOM.DOMString DOM.HTMLAppletElement.codeBase()'''
            return DOM.DOMString()
        def setCode(self):
            '''DOM.DOMString DOM.HTMLAppletElement.setCode()'''
            return DOM.DOMString()
        def code(self):
            '''DOM.DOMString DOM.HTMLAppletElement.code()'''
            return DOM.DOMString()
        def setArchive(self):
            '''DOM.DOMString DOM.HTMLAppletElement.setArchive()'''
            return DOM.DOMString()
        def archive(self):
            '''DOM.DOMString DOM.HTMLAppletElement.archive()'''
            return DOM.DOMString()
        def setAlt(self):
            '''DOM.DOMString DOM.HTMLAppletElement.setAlt()'''
            return DOM.DOMString()
        def alt(self):
            '''DOM.DOMString DOM.HTMLAppletElement.alt()'''
            return DOM.DOMString()
        def setAlign(self):
            '''DOM.DOMString DOM.HTMLAppletElement.setAlign()'''
            return DOM.DOMString()
        def align(self):
            '''DOM.DOMString DOM.HTMLAppletElement.align()'''
            return DOM.DOMString()
    class CSSPrimitiveValue(DOM.CSSValue):
        """"""
        # Enum DOM.CSSPrimitiveValue.UnitTypes
        CSS_UNKNOWN = 0
        CSS_NUMBER = 0
        CSS_PERCENTAGE = 0
        CSS_EMS = 0
        CSS_EXS = 0
        CSS_PX = 0
        CSS_CM = 0
        CSS_MM = 0
        CSS_IN = 0
        CSS_PT = 0
        CSS_PC = 0
        CSS_DEG = 0
        CSS_RAD = 0
        CSS_GRAD = 0
        CSS_MS = 0
        CSS_S = 0
        CSS_HZ = 0
        CSS_KHZ = 0
        CSS_DIMENSION = 0
        CSS_STRING = 0
        CSS_URI = 0
        CSS_IDENT = 0
        CSS_ATTR = 0
        CSS_COUNTER = 0
        CSS_RECT = 0
        CSS_RGBCOLOR = 0
        CSS_DPI = 0
        CSS_DPCM = 0
        CSS_PAIR = 0
        CSS_HTML_RELATIVE = 0
    
        def __init__(self):
            '''void DOM.CSSPrimitiveValue.__init__()'''
        def __init__(self, other):
            '''void DOM.CSSPrimitiveValue.__init__(DOM.CSSPrimitiveValue other)'''
        def __init__(self, other):
            '''void DOM.CSSPrimitiveValue.__init__(DOM.CSSValue other)'''
        def getRGBColorValue(self):
            '''DOM.RGBColor DOM.CSSPrimitiveValue.getRGBColorValue()'''
            return DOM.RGBColor()
        def getRectValue(self):
            '''DOM.Rect DOM.CSSPrimitiveValue.getRectValue()'''
            return DOM.Rect()
        def getCounterValue(self):
            '''DOM.Counter DOM.CSSPrimitiveValue.getCounterValue()'''
            return DOM.Counter()
        def getStringValue(self):
            '''DOM.DOMString DOM.CSSPrimitiveValue.getStringValue()'''
            return DOM.DOMString()
        def setStringValue(self, stringType, stringValue):
            '''void DOM.CSSPrimitiveValue.setStringValue(int stringType, DOM.DOMString stringValue)'''
        def getFloatValue(self, unitType):
            '''float DOM.CSSPrimitiveValue.getFloatValue(int unitType)'''
            return float()
        def setFloatValue(self, unitType, floatValue):
            '''void DOM.CSSPrimitiveValue.setFloatValue(int unitType, float floatValue)'''
        def primitiveType(self):
            '''int DOM.CSSPrimitiveValue.primitiveType()'''
            return int()
    class HTMLIsIndexElement(DOM.HTMLElement):
        """"""
        def __init__(self):
            '''void DOM.HTMLIsIndexElement.__init__()'''
        def __init__(self, other):
            '''void DOM.HTMLIsIndexElement.__init__(DOM.HTMLIsIndexElement other)'''
        def __init__(self, other):
            '''void DOM.HTMLIsIndexElement.__init__(DOM.Node other)'''
        def setPrompt(self):
            '''DOM.DOMString DOM.HTMLIsIndexElement.setPrompt()'''
            return DOM.DOMString()
        def prompt(self):
            '''DOM.DOMString DOM.HTMLIsIndexElement.prompt()'''
            return DOM.DOMString()
        def form(self):
            '''DOM.HTMLFormElement DOM.HTMLIsIndexElement.form()'''
            return DOM.HTMLFormElement()
    class CSSStyleDeclaration():
        """"""
        def __init__(self):
            '''void DOM.CSSStyleDeclaration.__init__()'''
        def __init__(self, other):
            '''void DOM.CSSStyleDeclaration.__init__(DOM.CSSStyleDeclaration other)'''
        def isNull(self):
            '''bool DOM.CSSStyleDeclaration.isNull()'''
            return bool()
        def item(self, index):
            '''DOM.DOMString DOM.CSSStyleDeclaration.item(int index)'''
            return DOM.DOMString()
        def setProperty(self, propertyName, value, priority):
            '''void DOM.CSSStyleDeclaration.setProperty(DOM.DOMString propertyName, DOM.DOMString value, DOM.DOMString priority)'''
        def getPropertyPriority(self, propertyName):
            '''DOM.DOMString DOM.CSSStyleDeclaration.getPropertyPriority(DOM.DOMString propertyName)'''
            return DOM.DOMString()
        def removeProperty(self, propertyName):
            '''DOM.DOMString DOM.CSSStyleDeclaration.removeProperty(DOM.DOMString propertyName)'''
            return DOM.DOMString()
        def getPropertyCSSValue(self, propertyName):
            '''DOM.CSSValue DOM.CSSStyleDeclaration.getPropertyCSSValue(DOM.DOMString propertyName)'''
            return DOM.CSSValue()
        def getPropertyValue(self, propertyName):
            '''DOM.DOMString DOM.CSSStyleDeclaration.getPropertyValue(DOM.DOMString propertyName)'''
            return DOM.DOMString()
        def parentRule(self):
            '''DOM.CSSRule DOM.CSSStyleDeclaration.parentRule()'''
            return DOM.CSSRule()
        def length(self):
            '''int DOM.CSSStyleDeclaration.length()'''
            return int()
        def setCssText(self):
            '''DOM.DOMString DOM.CSSStyleDeclaration.setCssText()'''
            return DOM.DOMString()
        def cssText(self):
            '''DOM.DOMString DOM.CSSStyleDeclaration.cssText()'''
            return DOM.DOMString()
    class DomShared():
        """"""
        def __init__(self):
            '''void DOM.DomShared.__init__()'''
        def __init__(self):
            '''DOM.DomShared DOM.DomShared.__init__()'''
            return DOM.DomShared()
        def refCount(self):
            '''int DOM.DomShared.refCount()'''
            return int()
        def hasOneRef(self):
            '''bool DOM.DomShared.hasOneRef()'''
            return bool()
        def deref(self):
            '''void DOM.DomShared.deref()'''
        def ref(self):
            '''void DOM.DomShared.ref()'''
        def deleteMe(self):
            '''bool DOM.DomShared.deleteMe()'''
            return bool()
    class Counter():
        """"""
        def __init__(self):
            '''void DOM.Counter.__init__()'''
        def __init__(self, other):
            '''void DOM.Counter.__init__(DOM.Counter other)'''
        def isNull(self):
            '''bool DOM.Counter.isNull()'''
            return bool()
        def separator(self):
            '''DOM.DOMString DOM.Counter.separator()'''
            return DOM.DOMString()
        def listStyle(self):
            '''DOM.DOMString DOM.Counter.listStyle()'''
            return DOM.DOMString()
        def identifier(self):
            '''DOM.DOMString DOM.Counter.identifier()'''
            return DOM.DOMString()
    class Element(DOM.Node):
        """"""
        def __init__(self):
            '''void DOM.Element.__init__()'''
        def __init__(self, other):
            '''void DOM.Element.__init__(DOM.Node other)'''
        def __init__(self, other):
            '''void DOM.Element.__init__(DOM.Element other)'''
        def querySelectorAll(self, query):
            '''DOM.NodeList DOM.Element.querySelectorAll(DOM.DOMString query)'''
            return DOM.NodeList()
        def querySelector(self, query):
            '''DOM.Element DOM.Element.querySelector(DOM.DOMString query)'''
            return DOM.Element()
        def khtmlMalformedPrefix(self, name):
            '''static bool DOM.Element.khtmlMalformedPrefix(DOM.DOMString name)'''
            return bool()
        def khtmlMalformedQualifiedName(self, name):
            '''static bool DOM.Element.khtmlMalformedQualifiedName(DOM.DOMString name)'''
            return bool()
        def khtmlValidQualifiedName(self, name):
            '''static bool DOM.Element.khtmlValidQualifiedName(DOM.DOMString name)'''
            return bool()
        def khtmlValidPrefix(self, name):
            '''static bool DOM.Element.khtmlValidPrefix(DOM.DOMString name)'''
            return bool()
        def khtmlValidAttrName(self, name):
            '''static bool DOM.Element.khtmlValidAttrName(DOM.DOMString name)'''
            return bool()
        def form(self):
            '''DOM.Element DOM.Element.form()'''
            return DOM.Element()
        def isHTMLElement(self):
            '''bool DOM.Element.isHTMLElement()'''
            return bool()
        def childElementCount(self):
            '''int DOM.Element.childElementCount()'''
            return int()
        def nextElementSibling(self):
            '''DOM.Element DOM.Element.nextElementSibling()'''
            return DOM.Element()
        def previousElementSibling(self):
            '''DOM.Element DOM.Element.previousElementSibling()'''
            return DOM.Element()
        def lastElementChild(self):
            '''DOM.Element DOM.Element.lastElementChild()'''
            return DOM.Element()
        def firstElementChild(self):
            '''DOM.Element DOM.Element.firstElementChild()'''
            return DOM.Element()
        def style(self):
            '''DOM.CSSStyleDeclaration DOM.Element.style()'''
            return DOM.CSSStyleDeclaration()
        def hasAttributeNS(self, namespaceURI, localName):
            '''bool DOM.Element.hasAttributeNS(DOM.DOMString namespaceURI, DOM.DOMString localName)'''
            return bool()
        def hasAttribute(self, name):
            '''bool DOM.Element.hasAttribute(DOM.DOMString name)'''
            return bool()
        def setAttributeNodeNS(self, newAttr):
            '''DOM.Attr DOM.Element.setAttributeNodeNS(DOM.Attr newAttr)'''
            return DOM.Attr()
        def getAttributeNodeNS(self, namespaceURI, localName):
            '''DOM.Attr DOM.Element.getAttributeNodeNS(DOM.DOMString namespaceURI, DOM.DOMString localName)'''
            return DOM.Attr()
        def removeAttributeNS(self, namespaceURI, localName):
            '''void DOM.Element.removeAttributeNS(DOM.DOMString namespaceURI, DOM.DOMString localName)'''
        def setAttributeNS(self, namespaceURI, qualifiedName, value):
            '''void DOM.Element.setAttributeNS(DOM.DOMString namespaceURI, DOM.DOMString qualifiedName, DOM.DOMString value)'''
        def getAttributeNS(self, namespaceURI, localName):
            '''DOM.DOMString DOM.Element.getAttributeNS(DOM.DOMString namespaceURI, DOM.DOMString localName)'''
            return DOM.DOMString()
        def getElementsByClassName(self, className):
            '''DOM.NodeList DOM.Element.getElementsByClassName(DOM.DOMString className)'''
            return DOM.NodeList()
        def getElementsByTagNameNS(self, namespaceURI, localName):
            '''DOM.NodeList DOM.Element.getElementsByTagNameNS(DOM.DOMString namespaceURI, DOM.DOMString localName)'''
            return DOM.NodeList()
        def getElementsByTagName(self, name):
            '''DOM.NodeList DOM.Element.getElementsByTagName(DOM.DOMString name)'''
            return DOM.NodeList()
        def removeAttributeNode(self, oldAttr):
            '''DOM.Attr DOM.Element.removeAttributeNode(DOM.Attr oldAttr)'''
            return DOM.Attr()
        def setAttributeNode(self, newAttr):
            '''DOM.Attr DOM.Element.setAttributeNode(DOM.Attr newAttr)'''
            return DOM.Attr()
        def getAttributeNode(self, name):
            '''DOM.Attr DOM.Element.getAttributeNode(DOM.DOMString name)'''
            return DOM.Attr()
        def removeAttribute(self, name):
            '''void DOM.Element.removeAttribute(DOM.DOMString name)'''
        def setAttribute(self, name, value):
            '''void DOM.Element.setAttribute(DOM.DOMString name, DOM.DOMString value)'''
        def getAttribute(self, name):
            '''DOM.DOMString DOM.Element.getAttribute(DOM.DOMString name)'''
            return DOM.DOMString()
        def tagName(self):
            '''DOM.DOMString DOM.Element.tagName()'''
            return DOM.DOMString()
    class MutationEvent(DOM.Event):
        """"""
        # Enum DOM.MutationEvent.attrChangeType
        MODIFICATION = 0
        ADDITION = 0
        REMOVAL = 0
    
        def __init__(self):
            '''void DOM.MutationEvent.__init__()'''
        def __init__(self, other):
            '''void DOM.MutationEvent.__init__(DOM.MutationEvent other)'''
        def __init__(self, other):
            '''void DOM.MutationEvent.__init__(DOM.Event other)'''
        def initMutationEvent(self, typeArg, canBubbleArg, cancelableArg, relatedNodeArg, prevValueArg, newValueArg, attrNameArg, attrChangeArg):
            '''void DOM.MutationEvent.initMutationEvent(DOM.DOMString typeArg, bool canBubbleArg, bool cancelableArg, DOM.Node relatedNodeArg, DOM.DOMString prevValueArg, DOM.DOMString newValueArg, DOM.DOMString attrNameArg, int attrChangeArg)'''
        def attrChange(self):
            '''int DOM.MutationEvent.attrChange()'''
            return int()
        def attrName(self):
            '''DOM.DOMString DOM.MutationEvent.attrName()'''
            return DOM.DOMString()
        def newValue(self):
            '''DOM.DOMString DOM.MutationEvent.newValue()'''
            return DOM.DOMString()
        def prevValue(self):
            '''DOM.DOMString DOM.MutationEvent.prevValue()'''
            return DOM.DOMString()
        def relatedNode(self):
            '''DOM.Node DOM.MutationEvent.relatedNode()'''
            return DOM.Node()
    class HTMLAreaElement(DOM.HTMLElement):
        """"""
        def __init__(self):
            '''void DOM.HTMLAreaElement.__init__()'''
        def __init__(self, other):
            '''void DOM.HTMLAreaElement.__init__(DOM.HTMLAreaElement other)'''
        def __init__(self, other):
            '''void DOM.HTMLAreaElement.__init__(DOM.Node other)'''
        def setTarget(self):
            '''DOM.DOMString DOM.HTMLAreaElement.setTarget()'''
            return DOM.DOMString()
        def target(self):
            '''DOM.DOMString DOM.HTMLAreaElement.target()'''
            return DOM.DOMString()
        def setTabIndex(self):
            '''int DOM.HTMLAreaElement.setTabIndex()'''
            return int()
        def tabIndex(self):
            '''int DOM.HTMLAreaElement.tabIndex()'''
            return int()
        def setShape(self):
            '''DOM.DOMString DOM.HTMLAreaElement.setShape()'''
            return DOM.DOMString()
        def shape(self):
            '''DOM.DOMString DOM.HTMLAreaElement.shape()'''
            return DOM.DOMString()
        def setNoHref(self):
            '''bool DOM.HTMLAreaElement.setNoHref()'''
            return bool()
        def noHref(self):
            '''bool DOM.HTMLAreaElement.noHref()'''
            return bool()
        def setHref(self):
            '''DOM.DOMString DOM.HTMLAreaElement.setHref()'''
            return DOM.DOMString()
        def href(self):
            '''DOM.DOMString DOM.HTMLAreaElement.href()'''
            return DOM.DOMString()
        def setCoords(self):
            '''DOM.DOMString DOM.HTMLAreaElement.setCoords()'''
            return DOM.DOMString()
        def coords(self):
            '''DOM.DOMString DOM.HTMLAreaElement.coords()'''
            return DOM.DOMString()
        def setAlt(self):
            '''DOM.DOMString DOM.HTMLAreaElement.setAlt()'''
            return DOM.DOMString()
        def alt(self):
            '''DOM.DOMString DOM.HTMLAreaElement.alt()'''
            return DOM.DOMString()
        def setAccessKey(self):
            '''DOM.DOMString DOM.HTMLAreaElement.setAccessKey()'''
            return DOM.DOMString()
        def accessKey(self):
            '''DOM.DOMString DOM.HTMLAreaElement.accessKey()'''
            return DOM.DOMString()
    class HTMLOptionElement(DOM.HTMLElement):
        """"""
        def __init__(self):
            '''void DOM.HTMLOptionElement.__init__()'''
        def __init__(self, other):
            '''void DOM.HTMLOptionElement.__init__(DOM.HTMLOptionElement other)'''
        def __init__(self, other):
            '''void DOM.HTMLOptionElement.__init__(DOM.Node other)'''
        def setValue(self):
            '''DOM.DOMString DOM.HTMLOptionElement.setValue()'''
            return DOM.DOMString()
        def value(self):
            '''DOM.DOMString DOM.HTMLOptionElement.value()'''
            return DOM.DOMString()
        def setSelected(self):
            '''bool DOM.HTMLOptionElement.setSelected()'''
            return bool()
        def selected(self):
            '''bool DOM.HTMLOptionElement.selected()'''
            return bool()
        def setLabel(self):
            '''DOM.DOMString DOM.HTMLOptionElement.setLabel()'''
            return DOM.DOMString()
        def label(self):
            '''DOM.DOMString DOM.HTMLOptionElement.label()'''
            return DOM.DOMString()
        def setDisabled(self):
            '''bool DOM.HTMLOptionElement.setDisabled()'''
            return bool()
        def disabled(self):
            '''bool DOM.HTMLOptionElement.disabled()'''
            return bool()
        def setIndex(self):
            '''int DOM.HTMLOptionElement.setIndex()'''
            return int()
        def index(self):
            '''int DOM.HTMLOptionElement.index()'''
            return int()
        def text(self):
            '''DOM.DOMString DOM.HTMLOptionElement.text()'''
            return DOM.DOMString()
        def setDefaultSelected(self):
            '''bool DOM.HTMLOptionElement.setDefaultSelected()'''
            return bool()
        def defaultSelected(self):
            '''bool DOM.HTMLOptionElement.defaultSelected()'''
            return bool()
        def form(self):
            '''DOM.HTMLFormElement DOM.HTMLOptionElement.form()'''
            return DOM.HTMLFormElement()
    class HTMLTableCellElement(DOM.HTMLElement):
        """"""
        def __init__(self):
            '''void DOM.HTMLTableCellElement.__init__()'''
        def __init__(self, other):
            '''void DOM.HTMLTableCellElement.__init__(DOM.HTMLTableCellElement other)'''
        def __init__(self, other):
            '''void DOM.HTMLTableCellElement.__init__(DOM.Node other)'''
        def setWidth(self):
            '''DOM.DOMString DOM.HTMLTableCellElement.setWidth()'''
            return DOM.DOMString()
        def width(self):
            '''DOM.DOMString DOM.HTMLTableCellElement.width()'''
            return DOM.DOMString()
        def setVAlign(self):
            '''DOM.DOMString DOM.HTMLTableCellElement.setVAlign()'''
            return DOM.DOMString()
        def vAlign(self):
            '''DOM.DOMString DOM.HTMLTableCellElement.vAlign()'''
            return DOM.DOMString()
        def setScope(self):
            '''DOM.DOMString DOM.HTMLTableCellElement.setScope()'''
            return DOM.DOMString()
        def scope(self):
            '''DOM.DOMString DOM.HTMLTableCellElement.scope()'''
            return DOM.DOMString()
        def setRowSpan(self):
            '''int DOM.HTMLTableCellElement.setRowSpan()'''
            return int()
        def rowSpan(self):
            '''int DOM.HTMLTableCellElement.rowSpan()'''
            return int()
        def setNoWrap(self):
            '''bool DOM.HTMLTableCellElement.setNoWrap()'''
            return bool()
        def noWrap(self):
            '''bool DOM.HTMLTableCellElement.noWrap()'''
            return bool()
        def setHeight(self):
            '''DOM.DOMString DOM.HTMLTableCellElement.setHeight()'''
            return DOM.DOMString()
        def height(self):
            '''DOM.DOMString DOM.HTMLTableCellElement.height()'''
            return DOM.DOMString()
        def setHeaders(self):
            '''DOM.DOMString DOM.HTMLTableCellElement.setHeaders()'''
            return DOM.DOMString()
        def headers(self):
            '''DOM.DOMString DOM.HTMLTableCellElement.headers()'''
            return DOM.DOMString()
        def setColSpan(self):
            '''int DOM.HTMLTableCellElement.setColSpan()'''
            return int()
        def colSpan(self):
            '''int DOM.HTMLTableCellElement.colSpan()'''
            return int()
        def setChOff(self):
            '''DOM.DOMString DOM.HTMLTableCellElement.setChOff()'''
            return DOM.DOMString()
        def chOff(self):
            '''DOM.DOMString DOM.HTMLTableCellElement.chOff()'''
            return DOM.DOMString()
        def setCh(self):
            '''DOM.DOMString DOM.HTMLTableCellElement.setCh()'''
            return DOM.DOMString()
        def ch(self):
            '''DOM.DOMString DOM.HTMLTableCellElement.ch()'''
            return DOM.DOMString()
        def setBgColor(self):
            '''DOM.DOMString DOM.HTMLTableCellElement.setBgColor()'''
            return DOM.DOMString()
        def bgColor(self):
            '''DOM.DOMString DOM.HTMLTableCellElement.bgColor()'''
            return DOM.DOMString()
        def setAxis(self):
            '''DOM.DOMString DOM.HTMLTableCellElement.setAxis()'''
            return DOM.DOMString()
        def axis(self):
            '''DOM.DOMString DOM.HTMLTableCellElement.axis()'''
            return DOM.DOMString()
        def setAlign(self):
            '''DOM.DOMString DOM.HTMLTableCellElement.setAlign()'''
            return DOM.DOMString()
        def align(self):
            '''DOM.DOMString DOM.HTMLTableCellElement.align()'''
            return DOM.DOMString()
        def setAbbr(self):
            '''DOM.DOMString DOM.HTMLTableCellElement.setAbbr()'''
            return DOM.DOMString()
        def abbr(self):
            '''DOM.DOMString DOM.HTMLTableCellElement.abbr()'''
            return DOM.DOMString()
        def setCellIndex(self):
            '''int DOM.HTMLTableCellElement.setCellIndex()'''
            return int()
        def cellIndex(self):
            '''int DOM.HTMLTableCellElement.cellIndex()'''
            return int()
    class CharacterData(DOM.Node):
        """"""
        def __init__(self):
            '''void DOM.CharacterData.__init__()'''
        def __init__(self, other):
            '''void DOM.CharacterData.__init__(DOM.CharacterData other)'''
        def __init__(self, other):
            '''void DOM.CharacterData.__init__(DOM.Node other)'''
        def replaceData(self, offset, count, arg):
            '''void DOM.CharacterData.replaceData(int offset, int count, DOM.DOMString arg)'''
        def deleteData(self, offset, count):
            '''void DOM.CharacterData.deleteData(int offset, int count)'''
        def insertData(self, offset, arg):
            '''void DOM.CharacterData.insertData(int offset, DOM.DOMString arg)'''
        def appendData(self, arg):
            '''void DOM.CharacterData.appendData(DOM.DOMString arg)'''
        def substringData(self, offset, count):
            '''DOM.DOMString DOM.CharacterData.substringData(int offset, int count)'''
            return DOM.DOMString()
        def length(self):
            '''int DOM.CharacterData.length()'''
            return int()
        def setData(self):
            '''DOM.DOMString DOM.CharacterData.setData()'''
            return DOM.DOMString()
        def data(self):
            '''DOM.DOMString DOM.CharacterData.data()'''
            return DOM.DOMString()
    class MediaList():
        """"""
        def __init__(self):
            '''void DOM.MediaList.__init__()'''
        def __init__(self, other):
            '''void DOM.MediaList.__init__(DOM.MediaList other)'''
        def isNull(self):
            '''bool DOM.MediaList.isNull()'''
            return bool()
        def appendMedium(self, newMedium):
            '''void DOM.MediaList.appendMedium(DOM.DOMString newMedium)'''
        def deleteMedium(self, oldMedium):
            '''void DOM.MediaList.deleteMedium(DOM.DOMString oldMedium)'''
        def item(self, index):
            '''DOM.DOMString DOM.MediaList.item(int index)'''
            return DOM.DOMString()
        def length(self):
            '''int DOM.MediaList.length()'''
            return int()
        def setMediaText(self, value):
            '''void DOM.MediaList.setMediaText(DOM.DOMString value)'''
        def mediaText(self):
            '''DOM.DOMString DOM.MediaList.mediaText()'''
            return DOM.DOMString()
    class DocumentFragment(DOM.Node):
        """"""
        def __init__(self):
            '''void DOM.DocumentFragment.__init__()'''
        def __init__(self, other):
            '''void DOM.DocumentFragment.__init__(DOM.DocumentFragment other)'''
        def __init__(self, other):
            '''void DOM.DocumentFragment.__init__(DOM.Node other)'''
        def querySelectorAll(self, query):
            '''DOM.NodeList DOM.DocumentFragment.querySelectorAll(DOM.DOMString query)'''
            return DOM.NodeList()
        def querySelector(self, query):
            '''DOM.Element DOM.DocumentFragment.querySelector(DOM.DOMString query)'''
            return DOM.Element()
    class HTMLTableCaptionElement(DOM.HTMLElement):
        """"""
        def __init__(self):
            '''void DOM.HTMLTableCaptionElement.__init__()'''
        def __init__(self, other):
            '''void DOM.HTMLTableCaptionElement.__init__(DOM.HTMLTableCaptionElement other)'''
        def __init__(self, other):
            '''void DOM.HTMLTableCaptionElement.__init__(DOM.Node other)'''
        def setAlign(self):
            '''DOM.DOMString DOM.HTMLTableCaptionElement.setAlign()'''
            return DOM.DOMString()
        def align(self):
            '''DOM.DOMString DOM.HTMLTableCaptionElement.align()'''
            return DOM.DOMString()
    class HTMLLabelElement(DOM.HTMLElement):
        """"""
        def __init__(self):
            '''void DOM.HTMLLabelElement.__init__()'''
        def __init__(self, other):
            '''void DOM.HTMLLabelElement.__init__(DOM.HTMLLabelElement other)'''
        def __init__(self, other):
            '''void DOM.HTMLLabelElement.__init__(DOM.Node other)'''
        def setHtmlFor(self):
            '''DOM.DOMString DOM.HTMLLabelElement.setHtmlFor()'''
            return DOM.DOMString()
        def htmlFor(self):
            '''DOM.DOMString DOM.HTMLLabelElement.htmlFor()'''
            return DOM.DOMString()
        def setAccessKey(self):
            '''DOM.DOMString DOM.HTMLLabelElement.setAccessKey()'''
            return DOM.DOMString()
        def accessKey(self):
            '''DOM.DOMString DOM.HTMLLabelElement.accessKey()'''
            return DOM.DOMString()
    class NodeList():
        """"""
        def __init__(self):
            '''void DOM.NodeList.__init__()'''
        def __init__(self, other):
            '''void DOM.NodeList.__init__(DOM.NodeList other)'''
        def isNull(self):
            '''bool DOM.NodeList.isNull()'''
            return bool()
        def item(self, index):
            '''DOM.Node DOM.NodeList.item(int index)'''
            return DOM.Node()
        def length(self):
            '''int DOM.NodeList.length()'''
            return int()
    class HTMLMetaElement(DOM.HTMLElement):
        """"""
        def __init__(self):
            '''void DOM.HTMLMetaElement.__init__()'''
        def __init__(self, other):
            '''void DOM.HTMLMetaElement.__init__(DOM.HTMLMetaElement other)'''
        def __init__(self, other):
            '''void DOM.HTMLMetaElement.__init__(DOM.Node other)'''
        def setScheme(self):
            '''DOM.DOMString DOM.HTMLMetaElement.setScheme()'''
            return DOM.DOMString()
        def scheme(self):
            '''DOM.DOMString DOM.HTMLMetaElement.scheme()'''
            return DOM.DOMString()
        def setName(self):
            '''DOM.DOMString DOM.HTMLMetaElement.setName()'''
            return DOM.DOMString()
        def name(self):
            '''DOM.DOMString DOM.HTMLMetaElement.name()'''
            return DOM.DOMString()
        def setHttpEquiv(self):
            '''DOM.DOMString DOM.HTMLMetaElement.setHttpEquiv()'''
            return DOM.DOMString()
        def httpEquiv(self):
            '''DOM.DOMString DOM.HTMLMetaElement.httpEquiv()'''
            return DOM.DOMString()
        def setContent(self):
            '''DOM.DOMString DOM.HTMLMetaElement.setContent()'''
            return DOM.DOMString()
        def content(self):
            '''DOM.DOMString DOM.HTMLMetaElement.content()'''
            return DOM.DOMString()
    class NamedNodeMap():
        """"""
        def __init__(self):
            '''void DOM.NamedNodeMap.__init__()'''
        def __init__(self, other):
            '''void DOM.NamedNodeMap.__init__(DOM.NamedNodeMap other)'''
        def isNull(self):
            '''bool DOM.NamedNodeMap.isNull()'''
            return bool()
        def removeNamedItemNS(self, namespaceURI, localName):
            '''DOM.Node DOM.NamedNodeMap.removeNamedItemNS(DOM.DOMString namespaceURI, DOM.DOMString localName)'''
            return DOM.Node()
        def setNamedItemNS(self, arg):
            '''DOM.Node DOM.NamedNodeMap.setNamedItemNS(DOM.Node arg)'''
            return DOM.Node()
        def getNamedItemNS(self, namespaceURI, localName):
            '''DOM.Node DOM.NamedNodeMap.getNamedItemNS(DOM.DOMString namespaceURI, DOM.DOMString localName)'''
            return DOM.Node()
        def item(self, index):
            '''DOM.Node DOM.NamedNodeMap.item(int index)'''
            return DOM.Node()
        def removeNamedItem(self, name):
            '''DOM.Node DOM.NamedNodeMap.removeNamedItem(DOM.DOMString name)'''
            return DOM.Node()
        def setNamedItem(self, arg):
            '''DOM.Node DOM.NamedNodeMap.setNamedItem(DOM.Node arg)'''
            return DOM.Node()
        def getNamedItem(self, name):
            '''DOM.Node DOM.NamedNodeMap.getNamedItem(DOM.DOMString name)'''
            return DOM.Node()
        def length(self):
            '''int DOM.NamedNodeMap.length()'''
            return int()
    class HTMLLinkElement(DOM.HTMLElement):
        """"""
        def __init__(self):
            '''void DOM.HTMLLinkElement.__init__()'''
        def __init__(self, other):
            '''void DOM.HTMLLinkElement.__init__(DOM.HTMLLinkElement other)'''
        def __init__(self, other):
            '''void DOM.HTMLLinkElement.__init__(DOM.Node other)'''
        def sheet(self):
            '''DOM.StyleSheet DOM.HTMLLinkElement.sheet()'''
            return DOM.StyleSheet()
        def setType(self):
            '''DOM.DOMString DOM.HTMLLinkElement.setType()'''
            return DOM.DOMString()
        def type(self):
            '''DOM.DOMString DOM.HTMLLinkElement.type()'''
            return DOM.DOMString()
        def setTarget(self):
            '''DOM.DOMString DOM.HTMLLinkElement.setTarget()'''
            return DOM.DOMString()
        def target(self):
            '''DOM.DOMString DOM.HTMLLinkElement.target()'''
            return DOM.DOMString()
        def setRev(self):
            '''DOM.DOMString DOM.HTMLLinkElement.setRev()'''
            return DOM.DOMString()
        def rev(self):
            '''DOM.DOMString DOM.HTMLLinkElement.rev()'''
            return DOM.DOMString()
        def setRel(self):
            '''DOM.DOMString DOM.HTMLLinkElement.setRel()'''
            return DOM.DOMString()
        def rel(self):
            '''DOM.DOMString DOM.HTMLLinkElement.rel()'''
            return DOM.DOMString()
        def setMedia(self):
            '''DOM.DOMString DOM.HTMLLinkElement.setMedia()'''
            return DOM.DOMString()
        def media(self):
            '''DOM.DOMString DOM.HTMLLinkElement.media()'''
            return DOM.DOMString()
        def setHreflang(self):
            '''DOM.DOMString DOM.HTMLLinkElement.setHreflang()'''
            return DOM.DOMString()
        def hreflang(self):
            '''DOM.DOMString DOM.HTMLLinkElement.hreflang()'''
            return DOM.DOMString()
        def setHref(self):
            '''DOM.DOMString DOM.HTMLLinkElement.setHref()'''
            return DOM.DOMString()
        def href(self):
            '''DOM.DOMString DOM.HTMLLinkElement.href()'''
            return DOM.DOMString()
        def setCharset(self):
            '''DOM.DOMString DOM.HTMLLinkElement.setCharset()'''
            return DOM.DOMString()
        def charset(self):
            '''DOM.DOMString DOM.HTMLLinkElement.charset()'''
            return DOM.DOMString()
        def setDisabled(self):
            '''bool DOM.HTMLLinkElement.setDisabled()'''
            return bool()
        def disabled(self):
            '''bool DOM.HTMLLinkElement.disabled()'''
            return bool()
    class CustomNodeFilter(DOM.DomShared):
        """"""
        def __init__(self):
            '''void DOM.CustomNodeFilter.__init__()'''
        def __init__(self):
            '''DOM.CustomNodeFilter DOM.CustomNodeFilter.__init__()'''
            return DOM.CustomNodeFilter()
        def customNodeFilterType(self):
            '''DOM.DOMString DOM.CustomNodeFilter.customNodeFilterType()'''
            return DOM.DOMString()
        def isNull(self):
            '''bool DOM.CustomNodeFilter.isNull()'''
            return bool()
        def acceptNode(self, n):
            '''int DOM.CustomNodeFilter.acceptNode(DOM.Node n)'''
            return int()
    class HTMLAnchorElement(DOM.HTMLElement):
        """"""
        def __init__(self):
            '''void DOM.HTMLAnchorElement.__init__()'''
        def __init__(self, other):
            '''void DOM.HTMLAnchorElement.__init__(DOM.HTMLAnchorElement other)'''
        def __init__(self, other):
            '''void DOM.HTMLAnchorElement.__init__(DOM.Node other)'''
        def focus(self):
            '''void DOM.HTMLAnchorElement.focus()'''
        def blur(self):
            '''void DOM.HTMLAnchorElement.blur()'''
        def setType(self):
            '''DOM.DOMString DOM.HTMLAnchorElement.setType()'''
            return DOM.DOMString()
        def type(self):
            '''DOM.DOMString DOM.HTMLAnchorElement.type()'''
            return DOM.DOMString()
        def setTarget(self):
            '''DOM.DOMString DOM.HTMLAnchorElement.setTarget()'''
            return DOM.DOMString()
        def target(self):
            '''DOM.DOMString DOM.HTMLAnchorElement.target()'''
            return DOM.DOMString()
        def setTabIndex(self):
            '''int DOM.HTMLAnchorElement.setTabIndex()'''
            return int()
        def tabIndex(self):
            '''int DOM.HTMLAnchorElement.tabIndex()'''
            return int()
        def setShape(self):
            '''DOM.DOMString DOM.HTMLAnchorElement.setShape()'''
            return DOM.DOMString()
        def shape(self):
            '''DOM.DOMString DOM.HTMLAnchorElement.shape()'''
            return DOM.DOMString()
        def setRev(self):
            '''DOM.DOMString DOM.HTMLAnchorElement.setRev()'''
            return DOM.DOMString()
        def rev(self):
            '''DOM.DOMString DOM.HTMLAnchorElement.rev()'''
            return DOM.DOMString()
        def setRel(self):
            '''DOM.DOMString DOM.HTMLAnchorElement.setRel()'''
            return DOM.DOMString()
        def rel(self):
            '''DOM.DOMString DOM.HTMLAnchorElement.rel()'''
            return DOM.DOMString()
        def setName(self):
            '''DOM.DOMString DOM.HTMLAnchorElement.setName()'''
            return DOM.DOMString()
        def name(self):
            '''DOM.DOMString DOM.HTMLAnchorElement.name()'''
            return DOM.DOMString()
        def setHreflang(self):
            '''DOM.DOMString DOM.HTMLAnchorElement.setHreflang()'''
            return DOM.DOMString()
        def hreflang(self):
            '''DOM.DOMString DOM.HTMLAnchorElement.hreflang()'''
            return DOM.DOMString()
        def setHref(self):
            '''DOM.DOMString DOM.HTMLAnchorElement.setHref()'''
            return DOM.DOMString()
        def href(self):
            '''DOM.DOMString DOM.HTMLAnchorElement.href()'''
            return DOM.DOMString()
        def setCoords(self):
            '''DOM.DOMString DOM.HTMLAnchorElement.setCoords()'''
            return DOM.DOMString()
        def coords(self):
            '''DOM.DOMString DOM.HTMLAnchorElement.coords()'''
            return DOM.DOMString()
        def setCharset(self):
            '''DOM.DOMString DOM.HTMLAnchorElement.setCharset()'''
            return DOM.DOMString()
        def charset(self):
            '''DOM.DOMString DOM.HTMLAnchorElement.charset()'''
            return DOM.DOMString()
        def setAccessKey(self):
            '''DOM.DOMString DOM.HTMLAnchorElement.setAccessKey()'''
            return DOM.DOMString()
        def accessKey(self):
            '''DOM.DOMString DOM.HTMLAnchorElement.accessKey()'''
            return DOM.DOMString()
    class HTMLHeadingElement(DOM.HTMLElement):
        """"""
        def __init__(self):
            '''void DOM.HTMLHeadingElement.__init__()'''
        def __init__(self, other):
            '''void DOM.HTMLHeadingElement.__init__(DOM.HTMLHeadingElement other)'''
        def __init__(self, other):
            '''void DOM.HTMLHeadingElement.__init__(DOM.Node other)'''
        def setAlign(self):
            '''DOM.DOMString DOM.HTMLHeadingElement.setAlign()'''
            return DOM.DOMString()
        def align(self):
            '''DOM.DOMString DOM.HTMLHeadingElement.align()'''
            return DOM.DOMString()
    class Notation(DOM.Node):
        """"""
        def __init__(self):
            '''void DOM.Notation.__init__()'''
        def __init__(self, other):
            '''void DOM.Notation.__init__(DOM.Notation other)'''
        def __init__(self, other):
            '''void DOM.Notation.__init__(DOM.Node other)'''
        def systemId(self):
            '''DOM.DOMString DOM.Notation.systemId()'''
            return DOM.DOMString()
        def publicId(self):
            '''DOM.DOMString DOM.Notation.publicId()'''
            return DOM.DOMString()
    class CSSStyleRule(DOM.CSSRule):
        """"""
        def __init__(self):
            '''void DOM.CSSStyleRule.__init__()'''
        def __init__(self, other):
            '''void DOM.CSSStyleRule.__init__(DOM.CSSStyleRule other)'''
        def __init__(self, other):
            '''void DOM.CSSStyleRule.__init__(DOM.CSSRule other)'''
        def style(self):
            '''DOM.CSSStyleDeclaration DOM.CSSStyleRule.style()'''
            return DOM.CSSStyleDeclaration()
        def setSelectorText(self):
            '''DOM.DOMString DOM.CSSStyleRule.setSelectorText()'''
            return DOM.DOMString()
        def selectorText(self):
            '''DOM.DOMString DOM.CSSStyleRule.selectorText()'''
            return DOM.DOMString()
    class CSSException():
        """"""
        # Enum DOM.CSSException.ExceptionCode
        SYNTAX_ERR = 0
        INVALID_MODIFICATION_ERR = 0
        _EXCEPTION_OFFSET = 0
        _EXCEPTION_MAX = 0
    
        code = None # int - member
        def __init__(self, _code):
            '''void DOM.CSSException.__init__(int _code)'''
        def __init__(self, other):
            '''void DOM.CSSException.__init__(DOM.CSSException other)'''
        def isCSSExceptionCode(self, exceptioncode):
            '''static bool DOM.CSSException.isCSSExceptionCode(int exceptioncode)'''
            return bool()
        def codeAsString(self):
            '''DOM.DOMString DOM.CSSException.codeAsString()'''
            return DOM.DOMString()
        def codeAsString(self, cssCode):
            '''static DOM.DOMString DOM.CSSException.codeAsString(int cssCode)'''
            return DOM.DOMString()
    class HTMLScriptElement(DOM.HTMLElement):
        """"""
        def __init__(self):
            '''void DOM.HTMLScriptElement.__init__()'''
        def __init__(self, other):
            '''void DOM.HTMLScriptElement.__init__(DOM.HTMLScriptElement other)'''
        def __init__(self, other):
            '''void DOM.HTMLScriptElement.__init__(DOM.Node other)'''
        def setType(self):
            '''DOM.DOMString DOM.HTMLScriptElement.setType()'''
            return DOM.DOMString()
        def type(self):
            '''DOM.DOMString DOM.HTMLScriptElement.type()'''
            return DOM.DOMString()
        def setSrc(self):
            '''DOM.DOMString DOM.HTMLScriptElement.setSrc()'''
            return DOM.DOMString()
        def src(self):
            '''DOM.DOMString DOM.HTMLScriptElement.src()'''
            return DOM.DOMString()
        def setDefer(self):
            '''bool DOM.HTMLScriptElement.setDefer()'''
            return bool()
        def defer(self):
            '''bool DOM.HTMLScriptElement.defer()'''
            return bool()
        def setCharset(self):
            '''DOM.DOMString DOM.HTMLScriptElement.setCharset()'''
            return DOM.DOMString()
        def charset(self):
            '''DOM.DOMString DOM.HTMLScriptElement.charset()'''
            return DOM.DOMString()
        def setEvent(self):
            '''DOM.DOMString DOM.HTMLScriptElement.setEvent()'''
            return DOM.DOMString()
        def event(self):
            '''DOM.DOMString DOM.HTMLScriptElement.event()'''
            return DOM.DOMString()
        def setHtmlFor(self):
            '''DOM.DOMString DOM.HTMLScriptElement.setHtmlFor()'''
            return DOM.DOMString()
        def htmlFor(self):
            '''DOM.DOMString DOM.HTMLScriptElement.htmlFor()'''
            return DOM.DOMString()
        def setText(self):
            '''DOM.DOMString DOM.HTMLScriptElement.setText()'''
            return DOM.DOMString()
        def text(self):
            '''DOM.DOMString DOM.HTMLScriptElement.text()'''
            return DOM.DOMString()
    class HTMLSelectElement(DOM.HTMLElement):
        """"""
        def __init__(self):
            '''void DOM.HTMLSelectElement.__init__()'''
        def __init__(self, other):
            '''void DOM.HTMLSelectElement.__init__(DOM.HTMLSelectElement other)'''
        def __init__(self, other):
            '''void DOM.HTMLSelectElement.__init__(DOM.Node other)'''
        def focus(self):
            '''void DOM.HTMLSelectElement.focus()'''
        def blur(self):
            '''void DOM.HTMLSelectElement.blur()'''
        def remove(self, index):
            '''void DOM.HTMLSelectElement.remove(int index)'''
        def add(self, element, before):
            '''void DOM.HTMLSelectElement.add(DOM.HTMLElement element, DOM.HTMLElement before)'''
        def setTabIndex(self):
            '''int DOM.HTMLSelectElement.setTabIndex()'''
            return int()
        def tabIndex(self):
            '''int DOM.HTMLSelectElement.tabIndex()'''
            return int()
        def setSize(self):
            '''int DOM.HTMLSelectElement.setSize()'''
            return int()
        def size(self):
            '''int DOM.HTMLSelectElement.size()'''
            return int()
        def setName(self):
            '''DOM.DOMString DOM.HTMLSelectElement.setName()'''
            return DOM.DOMString()
        def name(self):
            '''DOM.DOMString DOM.HTMLSelectElement.name()'''
            return DOM.DOMString()
        def setMultiple(self):
            '''bool DOM.HTMLSelectElement.setMultiple()'''
            return bool()
        def multiple(self):
            '''bool DOM.HTMLSelectElement.multiple()'''
            return bool()
        def setDisabled(self):
            '''bool DOM.HTMLSelectElement.setDisabled()'''
            return bool()
        def disabled(self):
            '''bool DOM.HTMLSelectElement.disabled()'''
            return bool()
        def options(self):
            '''DOM.HTMLCollection DOM.HTMLSelectElement.options()'''
            return DOM.HTMLCollection()
        def form(self):
            '''DOM.HTMLFormElement DOM.HTMLSelectElement.form()'''
            return DOM.HTMLFormElement()
        def length(self):
            '''int DOM.HTMLSelectElement.length()'''
            return int()
        def setValue(self):
            '''DOM.DOMString DOM.HTMLSelectElement.setValue()'''
            return DOM.DOMString()
        def value(self):
            '''DOM.DOMString DOM.HTMLSelectElement.value()'''
            return DOM.DOMString()
        def setSelectedIndex(self):
            '''int DOM.HTMLSelectElement.setSelectedIndex()'''
            return int()
        def selectedIndex(self):
            '''int DOM.HTMLSelectElement.selectedIndex()'''
            return int()
        def type(self):
            '''DOM.DOMString DOM.HTMLSelectElement.type()'''
            return DOM.DOMString()
    class StyleSheetList():
        """"""
        def __init__(self):
            '''void DOM.StyleSheetList.__init__()'''
        def __init__(self, other):
            '''void DOM.StyleSheetList.__init__(DOM.StyleSheetList other)'''
        def isNull(self):
            '''bool DOM.StyleSheetList.isNull()'''
            return bool()
        def item(self, index):
            '''DOM.StyleSheet DOM.StyleSheetList.item(int index)'''
            return DOM.StyleSheet()
        def length(self):
            '''int DOM.StyleSheetList.length()'''
            return int()
    class HTMLBaseFontElement(DOM.HTMLElement):
        """"""
        def __init__(self):
            '''void DOM.HTMLBaseFontElement.__init__()'''
        def __init__(self, other):
            '''void DOM.HTMLBaseFontElement.__init__(DOM.HTMLBaseFontElement other)'''
        def __init__(self, other):
            '''void DOM.HTMLBaseFontElement.__init__(DOM.Node other)'''
        def size(self):
            '''DOM.DOMString DOM.HTMLBaseFontElement.size()'''
            return DOM.DOMString()
        def setSize(self):
            '''int DOM.HTMLBaseFontElement.setSize()'''
            return int()
        def setSize(self):
            '''DOM.DOMString DOM.HTMLBaseFontElement.setSize()'''
            return DOM.DOMString()
        def getSize(self):
            '''int DOM.HTMLBaseFontElement.getSize()'''
            return int()
        def setFace(self):
            '''DOM.DOMString DOM.HTMLBaseFontElement.setFace()'''
            return DOM.DOMString()
        def face(self):
            '''DOM.DOMString DOM.HTMLBaseFontElement.face()'''
            return DOM.DOMString()
        def setColor(self):
            '''DOM.DOMString DOM.HTMLBaseFontElement.setColor()'''
            return DOM.DOMString()
        def color(self):
            '''DOM.DOMString DOM.HTMLBaseFontElement.color()'''
            return DOM.DOMString()
    class HTMLFormElement(DOM.HTMLElement):
        """"""
        def __init__(self):
            '''void DOM.HTMLFormElement.__init__()'''
        def __init__(self, other):
            '''void DOM.HTMLFormElement.__init__(DOM.HTMLFormElement other)'''
        def __init__(self, other):
            '''void DOM.HTMLFormElement.__init__(DOM.Node other)'''
        def reset(self):
            '''void DOM.HTMLFormElement.reset()'''
        def submit(self):
            '''void DOM.HTMLFormElement.submit()'''
        def setTarget(self):
            '''DOM.DOMString DOM.HTMLFormElement.setTarget()'''
            return DOM.DOMString()
        def target(self):
            '''DOM.DOMString DOM.HTMLFormElement.target()'''
            return DOM.DOMString()
        def setMethod(self):
            '''DOM.DOMString DOM.HTMLFormElement.setMethod()'''
            return DOM.DOMString()
        def method(self):
            '''DOM.DOMString DOM.HTMLFormElement.method()'''
            return DOM.DOMString()
        def setEnctype(self):
            '''DOM.DOMString DOM.HTMLFormElement.setEnctype()'''
            return DOM.DOMString()
        def enctype(self):
            '''DOM.DOMString DOM.HTMLFormElement.enctype()'''
            return DOM.DOMString()
        def setAction(self):
            '''DOM.DOMString DOM.HTMLFormElement.setAction()'''
            return DOM.DOMString()
        def action(self):
            '''DOM.DOMString DOM.HTMLFormElement.action()'''
            return DOM.DOMString()
        def setAcceptCharset(self):
            '''DOM.DOMString DOM.HTMLFormElement.setAcceptCharset()'''
            return DOM.DOMString()
        def acceptCharset(self):
            '''DOM.DOMString DOM.HTMLFormElement.acceptCharset()'''
            return DOM.DOMString()
        def setName(self):
            '''DOM.DOMString DOM.HTMLFormElement.setName()'''
            return DOM.DOMString()
        def name(self):
            '''DOM.DOMString DOM.HTMLFormElement.name()'''
            return DOM.DOMString()
        def length(self):
            '''int DOM.HTMLFormElement.length()'''
            return int()
        def elements(self):
            '''DOM.HTMLCollection DOM.HTMLFormElement.elements()'''
            return DOM.HTMLCollection()
    class HTMLModElement(DOM.HTMLElement):
        """"""
        def __init__(self):
            '''void DOM.HTMLModElement.__init__()'''
        def __init__(self, other):
            '''void DOM.HTMLModElement.__init__(DOM.HTMLModElement other)'''
        def __init__(self, other):
            '''void DOM.HTMLModElement.__init__(DOM.Node other)'''
        def setDateTime(self):
            '''DOM.DOMString DOM.HTMLModElement.setDateTime()'''
            return DOM.DOMString()
        def dateTime(self):
            '''DOM.DOMString DOM.HTMLModElement.dateTime()'''
            return DOM.DOMString()
        def setCite(self):
            '''DOM.DOMString DOM.HTMLModElement.setCite()'''
            return DOM.DOMString()
        def cite(self):
            '''DOM.DOMString DOM.HTMLModElement.cite()'''
            return DOM.DOMString()
    class LinkStyle():
        """"""
        def __init__(self):
            '''void DOM.LinkStyle.__init__()'''
        def __init__(self, other):
            '''void DOM.LinkStyle.__init__(DOM.LinkStyle other)'''
        def isNull(self):
            '''bool DOM.LinkStyle.isNull()'''
            return bool()
        def sheet(self):
            '''DOM.StyleSheet DOM.LinkStyle.sheet()'''
            return DOM.StyleSheet()
    class HTMLFontElement(DOM.HTMLElement):
        """"""
        def __init__(self):
            '''void DOM.HTMLFontElement.__init__()'''
        def __init__(self, other):
            '''void DOM.HTMLFontElement.__init__(DOM.HTMLFontElement other)'''
        def __init__(self, other):
            '''void DOM.HTMLFontElement.__init__(DOM.Node other)'''
        def setSize(self):
            '''DOM.DOMString DOM.HTMLFontElement.setSize()'''
            return DOM.DOMString()
        def size(self):
            '''DOM.DOMString DOM.HTMLFontElement.size()'''
            return DOM.DOMString()
        def setFace(self):
            '''DOM.DOMString DOM.HTMLFontElement.setFace()'''
            return DOM.DOMString()
        def face(self):
            '''DOM.DOMString DOM.HTMLFontElement.face()'''
            return DOM.DOMString()
        def setColor(self):
            '''DOM.DOMString DOM.HTMLFontElement.setColor()'''
            return DOM.DOMString()
        def color(self):
            '''DOM.DOMString DOM.HTMLFontElement.color()'''
            return DOM.DOMString()
    class CSSMediaRule(DOM.CSSRule):
        """"""
        def __init__(self):
            '''void DOM.CSSMediaRule.__init__()'''
        def __init__(self, other):
            '''void DOM.CSSMediaRule.__init__(DOM.CSSMediaRule other)'''
        def __init__(self, other):
            '''void DOM.CSSMediaRule.__init__(DOM.CSSRule other)'''
        def deleteRule(self, index):
            '''void DOM.CSSMediaRule.deleteRule(int index)'''
        def insertRule(self, rule, index):
            '''int DOM.CSSMediaRule.insertRule(DOM.DOMString rule, int index)'''
            return int()
        def cssRules(self):
            '''DOM.CSSRuleList DOM.CSSMediaRule.cssRules()'''
            return DOM.CSSRuleList()
        def media(self):
            '''DOM.MediaList DOM.CSSMediaRule.media()'''
            return DOM.MediaList()
    class HTMLHRElement(DOM.HTMLElement):
        """"""
        def __init__(self):
            '''void DOM.HTMLHRElement.__init__()'''
        def __init__(self, other):
            '''void DOM.HTMLHRElement.__init__(DOM.HTMLHRElement other)'''
        def __init__(self, other):
            '''void DOM.HTMLHRElement.__init__(DOM.Node other)'''
        def setWidth(self):
            '''DOM.DOMString DOM.HTMLHRElement.setWidth()'''
            return DOM.DOMString()
        def width(self):
            '''DOM.DOMString DOM.HTMLHRElement.width()'''
            return DOM.DOMString()
        def setSize(self):
            '''DOM.DOMString DOM.HTMLHRElement.setSize()'''
            return DOM.DOMString()
        def size(self):
            '''DOM.DOMString DOM.HTMLHRElement.size()'''
            return DOM.DOMString()
        def setNoShade(self):
            '''bool DOM.HTMLHRElement.setNoShade()'''
            return bool()
        def noShade(self):
            '''bool DOM.HTMLHRElement.noShade()'''
            return bool()
        def setAlign(self):
            '''DOM.DOMString DOM.HTMLHRElement.setAlign()'''
            return DOM.DOMString()
        def align(self):
            '''DOM.DOMString DOM.HTMLHRElement.align()'''
            return DOM.DOMString()
    class HTMLObjectElement(DOM.HTMLElement):
        """"""
        def __init__(self):
            '''void DOM.HTMLObjectElement.__init__()'''
        def __init__(self, other):
            '''void DOM.HTMLObjectElement.__init__(DOM.HTMLObjectElement other)'''
        def __init__(self, other):
            '''void DOM.HTMLObjectElement.__init__(DOM.Node other)'''
        def contentDocument(self):
            '''DOM.Document DOM.HTMLObjectElement.contentDocument()'''
            return DOM.Document()
        def setWidth(self):
            '''DOM.DOMString DOM.HTMLObjectElement.setWidth()'''
            return DOM.DOMString()
        def width(self):
            '''DOM.DOMString DOM.HTMLObjectElement.width()'''
            return DOM.DOMString()
        def vspace(self):
            '''DOM.DOMString DOM.HTMLObjectElement.vspace()'''
            return DOM.DOMString()
        def setVspace(self):
            '''int DOM.HTMLObjectElement.setVspace()'''
            return int()
        def setVspace(self):
            '''DOM.DOMString DOM.HTMLObjectElement.setVspace()'''
            return DOM.DOMString()
        def getVspace(self):
            '''int DOM.HTMLObjectElement.getVspace()'''
            return int()
        def setUseMap(self):
            '''DOM.DOMString DOM.HTMLObjectElement.setUseMap()'''
            return DOM.DOMString()
        def useMap(self):
            '''DOM.DOMString DOM.HTMLObjectElement.useMap()'''
            return DOM.DOMString()
        def setType(self):
            '''DOM.DOMString DOM.HTMLObjectElement.setType()'''
            return DOM.DOMString()
        def type(self):
            '''DOM.DOMString DOM.HTMLObjectElement.type()'''
            return DOM.DOMString()
        def setTabIndex(self):
            '''int DOM.HTMLObjectElement.setTabIndex()'''
            return int()
        def tabIndex(self):
            '''int DOM.HTMLObjectElement.tabIndex()'''
            return int()
        def setStandby(self):
            '''DOM.DOMString DOM.HTMLObjectElement.setStandby()'''
            return DOM.DOMString()
        def standby(self):
            '''DOM.DOMString DOM.HTMLObjectElement.standby()'''
            return DOM.DOMString()
        def setName(self):
            '''DOM.DOMString DOM.HTMLObjectElement.setName()'''
            return DOM.DOMString()
        def name(self):
            '''DOM.DOMString DOM.HTMLObjectElement.name()'''
            return DOM.DOMString()
        def hspace(self):
            '''DOM.DOMString DOM.HTMLObjectElement.hspace()'''
            return DOM.DOMString()
        def setHspace(self):
            '''int DOM.HTMLObjectElement.setHspace()'''
            return int()
        def setHspace(self):
            '''DOM.DOMString DOM.HTMLObjectElement.setHspace()'''
            return DOM.DOMString()
        def getHspace(self):
            '''int DOM.HTMLObjectElement.getHspace()'''
            return int()
        def setHeight(self):
            '''DOM.DOMString DOM.HTMLObjectElement.setHeight()'''
            return DOM.DOMString()
        def height(self):
            '''DOM.DOMString DOM.HTMLObjectElement.height()'''
            return DOM.DOMString()
        def setDeclare(self):
            '''bool DOM.HTMLObjectElement.setDeclare()'''
            return bool()
        def declare(self):
            '''bool DOM.HTMLObjectElement.declare()'''
            return bool()
        def setData(self):
            '''DOM.DOMString DOM.HTMLObjectElement.setData()'''
            return DOM.DOMString()
        def data(self):
            '''DOM.DOMString DOM.HTMLObjectElement.data()'''
            return DOM.DOMString()
        def setCodeType(self):
            '''DOM.DOMString DOM.HTMLObjectElement.setCodeType()'''
            return DOM.DOMString()
        def codeType(self):
            '''DOM.DOMString DOM.HTMLObjectElement.codeType()'''
            return DOM.DOMString()
        def setCodeBase(self):
            '''DOM.DOMString DOM.HTMLObjectElement.setCodeBase()'''
            return DOM.DOMString()
        def codeBase(self):
            '''DOM.DOMString DOM.HTMLObjectElement.codeBase()'''
            return DOM.DOMString()
        def setBorder(self):
            '''DOM.DOMString DOM.HTMLObjectElement.setBorder()'''
            return DOM.DOMString()
        def border(self):
            '''DOM.DOMString DOM.HTMLObjectElement.border()'''
            return DOM.DOMString()
        def setArchive(self):
            '''DOM.DOMString DOM.HTMLObjectElement.setArchive()'''
            return DOM.DOMString()
        def archive(self):
            '''DOM.DOMString DOM.HTMLObjectElement.archive()'''
            return DOM.DOMString()
        def setAlign(self):
            '''DOM.DOMString DOM.HTMLObjectElement.setAlign()'''
            return DOM.DOMString()
        def align(self):
            '''DOM.DOMString DOM.HTMLObjectElement.align()'''
            return DOM.DOMString()
        def setCode(self):
            '''DOM.DOMString DOM.HTMLObjectElement.setCode()'''
            return DOM.DOMString()
        def code(self):
            '''DOM.DOMString DOM.HTMLObjectElement.code()'''
            return DOM.DOMString()
        def form(self):
            '''DOM.HTMLFormElement DOM.HTMLObjectElement.form()'''
            return DOM.HTMLFormElement()
    class Text(DOM.CharacterData):
        """"""
        def __init__(self):
            '''void DOM.Text.__init__()'''
        def __init__(self, other):
            '''void DOM.Text.__init__(DOM.Text other)'''
        def __init__(self, other):
            '''void DOM.Text.__init__(DOM.Node other)'''
        def splitText(self, offset):
            '''DOM.Text DOM.Text.splitText(int offset)'''
            return DOM.Text()
    class HTMLBlockquoteElement(DOM.HTMLElement):
        """"""
        def __init__(self):
            '''void DOM.HTMLBlockquoteElement.__init__()'''
        def __init__(self, other):
            '''void DOM.HTMLBlockquoteElement.__init__(DOM.HTMLBlockquoteElement other)'''
        def __init__(self, other):
            '''void DOM.HTMLBlockquoteElement.__init__(DOM.Node other)'''
        def setCite(self):
            '''DOM.DOMString DOM.HTMLBlockquoteElement.setCite()'''
            return DOM.DOMString()
        def cite(self):
            '''DOM.DOMString DOM.HTMLBlockquoteElement.cite()'''
            return DOM.DOMString()
    class DOMString():
        """"""
        def __init__(self):
            '''void DOM.DOMString.__init__()'''
        def __init__(self, str, len):
            '''void DOM.DOMString.__init__(QChar str, int len)'''
        def __init__(self):
            '''QString DOM.DOMString.__init__()'''
            return QString()
        def __init__(self, str):
            '''void DOM.DOMString.__init__(str str)'''
        def __init__(self, str, len):
            '''void DOM.DOMString.__init__(str str, int len)'''
        def __init__(self, str):
            '''void DOM.DOMString.__init__(DOM.DOMString str)'''
        def format(self, format, *args):
            '''static DOM.DOMString DOM.DOMString.format(str format, ... *args)'''
            return DOM.DOMString()
        def startsWith(self, str):
            '''bool DOM.DOMString.startsWith(DOM.DOMString str)'''
            return bool()
        def endsWith(self, str):
            '''bool DOM.DOMString.endsWith(DOM.DOMString str)'''
            return bool()
        def isEmpty(self):
            '''bool DOM.DOMString.isEmpty()'''
            return bool()
        def isNull(self):
            '''bool DOM.DOMString.isNull()'''
            return bool()
        def copy(self):
            '''DOM.DOMString DOM.DOMString.copy()'''
            return DOM.DOMString()
        def number(self, f):
            '''static DOM.DOMString DOM.DOMString.number(float f)'''
            return DOM.DOMString()
        def percentage(self, _percentage):
            '''bool DOM.DOMString.percentage(int _percentage)'''
            return bool()
        def toFloat(self, ok):
            '''float DOM.DOMString.toFloat(bool ok)'''
            return float()
        def toInt(self, ok):
            '''int DOM.DOMString.toInt(bool ok)'''
            return int()
        def string(self):
            '''QString DOM.DOMString.string()'''
            return QString()
        def characters(self):
            '''QChar DOM.DOMString.characters()'''
            return QChar()
        def unicode(self):
            '''QChar DOM.DOMString.unicode()'''
            return QChar()
        def upper(self):
            '''DOM.DOMString DOM.DOMString.upper()'''
            return DOM.DOMString()
        def lower(self):
            '''DOM.DOMString DOM.DOMString.lower()'''
            return DOM.DOMString()
        def split(self, pos):
            '''DOM.DOMString DOM.DOMString.split(int pos)'''
            return DOM.DOMString()
        def remove(self, pos, len = 1):
            '''void DOM.DOMString.remove(int pos, int len = 1)'''
        def truncate(self, len):
            '''void DOM.DOMString.truncate(int len)'''
        def length(self):
            '''int DOM.DOMString.length()'''
            return int()
        def substring(self, pos, len = None):
            '''DOM.DOMString DOM.DOMString.substring(int pos, int len = UINT_MAX)'''
            return DOM.DOMString()
        def reverseFind(self, c, start = None):
            '''int DOM.DOMString.reverseFind(QChar c, int start = -1)'''
            return int()
        def find(self, c, start = 0):
            '''int DOM.DOMString.find(QChar c, int start = 0)'''
            return int()
        def __getitem__(self, i):
            '''QChar DOM.DOMString.__getitem__(int i)'''
            return QChar()
        def insert(self, str, pos):
            '''void DOM.DOMString.insert(DOM.DOMString str, int pos)'''
        def __add__(self, str):
            '''DOM.DOMString DOM.DOMString.__add__(DOM.DOMString str)'''
            return DOM.DOMString()
        def __iadd__(self, str):
            '''DOM.DOMString DOM.DOMString.__iadd__(DOM.DOMString str)'''
            return DOM.DOMString()
    class CSSRule():
        """"""
        # Enum DOM.CSSRule.RuleType
        UNKNOWN_RULE = 0
        STYLE_RULE = 0
        CHARSET_RULE = 0
        IMPORT_RULE = 0
        MEDIA_RULE = 0
        FONT_FACE_RULE = 0
        PAGE_RULE = 0
        NAMESPACE_RULE = 0
        QUIRKS_RULE = 0
    
        def __init__(self):
            '''void DOM.CSSRule.__init__()'''
        def __init__(self, other):
            '''void DOM.CSSRule.__init__(DOM.CSSRule other)'''
        def assignOther(self, other, thisType):
            '''void DOM.CSSRule.assignOther(DOM.CSSRule other, DOM.CSSRule.RuleType thisType)'''
        def isNull(self):
            '''bool DOM.CSSRule.isNull()'''
            return bool()
        def parentRule(self):
            '''DOM.CSSRule DOM.CSSRule.parentRule()'''
            return DOM.CSSRule()
        def parentStyleSheet(self):
            '''DOM.CSSStyleSheet DOM.CSSRule.parentStyleSheet()'''
            return DOM.CSSStyleSheet()
        def setCssText(self):
            '''DOM.DOMString DOM.CSSRule.setCssText()'''
            return DOM.DOMString()
        def cssText(self):
            '''DOM.DOMString DOM.CSSRule.cssText()'''
            return DOM.DOMString()
        def type(self):
            '''int DOM.CSSRule.type()'''
            return int()
    class Event():
        """"""
        # Enum DOM.Event.PhaseType
        CAPTURING_PHASE = 0
        AT_TARGET = 0
        BUBBLING_PHASE = 0
    
        def __init__(self):
            '''void DOM.Event.__init__()'''
        def __init__(self, other):
            '''void DOM.Event.__init__(DOM.Event other)'''
        def isNull(self):
            '''bool DOM.Event.isNull()'''
            return bool()
        def initEvent(self, eventTypeArg, canBubbleArg, cancelableArg):
            '''void DOM.Event.initEvent(DOM.DOMString eventTypeArg, bool canBubbleArg, bool cancelableArg)'''
        def preventDefault(self):
            '''void DOM.Event.preventDefault()'''
        def stopPropagation(self):
            '''void DOM.Event.stopPropagation()'''
        def timeStamp(self):
            '''int DOM.Event.timeStamp()'''
            return int()
        def cancelable(self):
            '''bool DOM.Event.cancelable()'''
            return bool()
        def bubbles(self):
            '''bool DOM.Event.bubbles()'''
            return bool()
        def eventPhase(self):
            '''int DOM.Event.eventPhase()'''
            return int()
        def currentTarget(self):
            '''DOM.Node DOM.Event.currentTarget()'''
            return DOM.Node()
        def target(self):
            '''DOM.Node DOM.Event.target()'''
            return DOM.Node()
        def type(self):
            '''DOM.DOMString DOM.Event.type()'''
            return DOM.DOMString()
    class CSSValueList(DOM.CSSValue):
        """"""
        def __init__(self):
            '''void DOM.CSSValueList.__init__()'''
        def __init__(self, other):
            '''void DOM.CSSValueList.__init__(DOM.CSSValueList other)'''
        def __init__(self, other):
            '''void DOM.CSSValueList.__init__(DOM.CSSValue other)'''
        def item(self, index):
            '''DOM.CSSValue DOM.CSSValueList.item(int index)'''
            return DOM.CSSValue()
        def length(self):
            '''int DOM.CSSValueList.length()'''
            return int()
    class HTMLTableRowElement(DOM.HTMLElement):
        """"""
        def __init__(self):
            '''void DOM.HTMLTableRowElement.__init__()'''
        def __init__(self, other):
            '''void DOM.HTMLTableRowElement.__init__(DOM.HTMLTableRowElement other)'''
        def __init__(self, other):
            '''void DOM.HTMLTableRowElement.__init__(DOM.Node other)'''
        def deleteCell(self, index):
            '''void DOM.HTMLTableRowElement.deleteCell(int index)'''
        def insertCell(self, index):
            '''DOM.HTMLElement DOM.HTMLTableRowElement.insertCell(int index)'''
            return DOM.HTMLElement()
        def setVAlign(self):
            '''DOM.DOMString DOM.HTMLTableRowElement.setVAlign()'''
            return DOM.DOMString()
        def vAlign(self):
            '''DOM.DOMString DOM.HTMLTableRowElement.vAlign()'''
            return DOM.DOMString()
        def setChOff(self):
            '''DOM.DOMString DOM.HTMLTableRowElement.setChOff()'''
            return DOM.DOMString()
        def chOff(self):
            '''DOM.DOMString DOM.HTMLTableRowElement.chOff()'''
            return DOM.DOMString()
        def setCh(self):
            '''DOM.DOMString DOM.HTMLTableRowElement.setCh()'''
            return DOM.DOMString()
        def ch(self):
            '''DOM.DOMString DOM.HTMLTableRowElement.ch()'''
            return DOM.DOMString()
        def setBgColor(self):
            '''DOM.DOMString DOM.HTMLTableRowElement.setBgColor()'''
            return DOM.DOMString()
        def bgColor(self):
            '''DOM.DOMString DOM.HTMLTableRowElement.bgColor()'''
            return DOM.DOMString()
        def setAlign(self):
            '''DOM.DOMString DOM.HTMLTableRowElement.setAlign()'''
            return DOM.DOMString()
        def align(self):
            '''DOM.DOMString DOM.HTMLTableRowElement.align()'''
            return DOM.DOMString()
        def setCells(self):
            '''DOM.HTMLCollection DOM.HTMLTableRowElement.setCells()'''
            return DOM.HTMLCollection()
        def cells(self):
            '''DOM.HTMLCollection DOM.HTMLTableRowElement.cells()'''
            return DOM.HTMLCollection()
        def setSectionRowIndex(self):
            '''int DOM.HTMLTableRowElement.setSectionRowIndex()'''
            return int()
        def sectionRowIndex(self):
            '''int DOM.HTMLTableRowElement.sectionRowIndex()'''
            return int()
        def setRowIndex(self):
            '''int DOM.HTMLTableRowElement.setRowIndex()'''
            return int()
        def rowIndex(self):
            '''int DOM.HTMLTableRowElement.rowIndex()'''
            return int()
    class TextEvent(DOM.UIEvent):
        """"""
        def __init__(self):
            '''void DOM.TextEvent.__init__()'''
        def __init__(self, other):
            '''void DOM.TextEvent.__init__(DOM.TextEvent other)'''
        def __init__(self, other):
            '''void DOM.TextEvent.__init__(DOM.Event other)'''
        def initTextEvent(self, typeArg, canBubbleArg, cancelableArg, viewArg, dataArg):
            '''void DOM.TextEvent.initTextEvent(DOM.DOMString typeArg, bool canBubbleArg, bool cancelableArg, DOM.AbstractView viewArg, DOM.DOMString dataArg)'''
    class HTMLDocument(DOM.Document):
        """"""
        def __init__(self):
            '''void DOM.HTMLDocument.__init__()'''
        def __init__(self, parent):
            '''void DOM.HTMLDocument.__init__(KHTMLView parent)'''
        def __init__(self, other):
            '''void DOM.HTMLDocument.__init__(DOM.HTMLDocument other)'''
        def __init__(self, other):
            '''void DOM.HTMLDocument.__init__(DOM.Node other)'''
        def all(self):
            '''DOM.HTMLCollection DOM.HTMLDocument.all()'''
            return DOM.HTMLCollection()
        def lastModified(self):
            '''DOM.DOMString DOM.HTMLDocument.lastModified()'''
            return DOM.DOMString()
        def completeURL(self, url):
            '''DOM.DOMString DOM.HTMLDocument.completeURL(DOM.DOMString url)'''
            return DOM.DOMString()
        def getElementsByName(self, elementName):
            '''DOM.NodeList DOM.HTMLDocument.getElementsByName(DOM.DOMString elementName)'''
            return DOM.NodeList()
        def writeln(self, text):
            '''void DOM.HTMLDocument.writeln(DOM.DOMString text)'''
        def write(self, text):
            '''void DOM.HTMLDocument.write(DOM.DOMString text)'''
        def close(self):
            '''void DOM.HTMLDocument.close()'''
        def open(self):
            '''void DOM.HTMLDocument.open()'''
        def setCookie(self):
            '''DOM.DOMString DOM.HTMLDocument.setCookie()'''
            return DOM.DOMString()
        def cookie(self):
            '''DOM.DOMString DOM.HTMLDocument.cookie()'''
            return DOM.DOMString()
        def anchors(self):
            '''DOM.HTMLCollection DOM.HTMLDocument.anchors()'''
            return DOM.HTMLCollection()
        def scripts(self):
            '''DOM.HTMLCollection DOM.HTMLDocument.scripts()'''
            return DOM.HTMLCollection()
        def layers(self):
            '''DOM.HTMLCollection DOM.HTMLDocument.layers()'''
            return DOM.HTMLCollection()
        def forms(self):
            '''DOM.HTMLCollection DOM.HTMLDocument.forms()'''
            return DOM.HTMLCollection()
        def links(self):
            '''DOM.HTMLCollection DOM.HTMLDocument.links()'''
            return DOM.HTMLCollection()
        def applets(self):
            '''DOM.HTMLCollection DOM.HTMLDocument.applets()'''
            return DOM.HTMLCollection()
        def images(self):
            '''DOM.HTMLCollection DOM.HTMLDocument.images()'''
            return DOM.HTMLCollection()
        def setBody(self):
            '''DOM.HTMLElement DOM.HTMLDocument.setBody()'''
            return DOM.HTMLElement()
        def body(self):
            '''DOM.HTMLElement DOM.HTMLDocument.body()'''
            return DOM.HTMLElement()
        def URL(self):
            '''DOM.DOMString DOM.HTMLDocument.URL()'''
            return DOM.DOMString()
        def domain(self):
            '''DOM.DOMString DOM.HTMLDocument.domain()'''
            return DOM.DOMString()
        def referrer(self):
            '''DOM.DOMString DOM.HTMLDocument.referrer()'''
            return DOM.DOMString()
        def setTitle(self):
            '''DOM.DOMString DOM.HTMLDocument.setTitle()'''
            return DOM.DOMString()
        def title(self):
            '''DOM.DOMString DOM.HTMLDocument.title()'''
            return DOM.DOMString()
    class HTMLInputElement(DOM.HTMLElement):
        """"""
        def __init__(self):
            '''void DOM.HTMLInputElement.__init__()'''
        def __init__(self, other):
            '''void DOM.HTMLInputElement.__init__(DOM.HTMLInputElement other)'''
        def __init__(self, other):
            '''void DOM.HTMLInputElement.__init__(DOM.Node other)'''
        def setSelectionRange(self, start, end):
            '''void DOM.HTMLInputElement.setSelectionRange(int start, int end)'''
        def setSelectionEnd(self, offset):
            '''void DOM.HTMLInputElement.setSelectionEnd(int offset)'''
        def selectionEnd(self):
            '''int DOM.HTMLInputElement.selectionEnd()'''
            return int()
        def setSelectionStart(self, offset):
            '''void DOM.HTMLInputElement.setSelectionStart(int offset)'''
        def selectionStart(self):
            '''int DOM.HTMLInputElement.selectionStart()'''
            return int()
        def click(self):
            '''void DOM.HTMLInputElement.click()'''
        def select(self):
            '''void DOM.HTMLInputElement.select()'''
        def focus(self):
            '''void DOM.HTMLInputElement.focus()'''
        def blur(self):
            '''void DOM.HTMLInputElement.blur()'''
        def setValue(self):
            '''DOM.DOMString DOM.HTMLInputElement.setValue()'''
            return DOM.DOMString()
        def value(self):
            '''DOM.DOMString DOM.HTMLInputElement.value()'''
            return DOM.DOMString()
        def setUseMap(self):
            '''DOM.DOMString DOM.HTMLInputElement.setUseMap()'''
            return DOM.DOMString()
        def useMap(self):
            '''DOM.DOMString DOM.HTMLInputElement.useMap()'''
            return DOM.DOMString()
        def setType(self):
            '''DOM.DOMString DOM.HTMLInputElement.setType()'''
            return DOM.DOMString()
        def type(self):
            '''DOM.DOMString DOM.HTMLInputElement.type()'''
            return DOM.DOMString()
        def setTabIndex(self):
            '''int DOM.HTMLInputElement.setTabIndex()'''
            return int()
        def tabIndex(self):
            '''int DOM.HTMLInputElement.tabIndex()'''
            return int()
        def setSrc(self):
            '''DOM.DOMString DOM.HTMLInputElement.setSrc()'''
            return DOM.DOMString()
        def src(self):
            '''DOM.DOMString DOM.HTMLInputElement.src()'''
            return DOM.DOMString()
        def getSize(self):
            '''int DOM.HTMLInputElement.getSize()'''
            return int()
        def setSize(self):
            '''DOM.DOMString DOM.HTMLInputElement.setSize()'''
            return DOM.DOMString()
        def setSize(self):
            '''int DOM.HTMLInputElement.setSize()'''
            return int()
        def size(self):
            '''DOM.DOMString DOM.HTMLInputElement.size()'''
            return DOM.DOMString()
        def setReadOnly(self):
            '''bool DOM.HTMLInputElement.setReadOnly()'''
            return bool()
        def readOnly(self):
            '''bool DOM.HTMLInputElement.readOnly()'''
            return bool()
        def setName(self):
            '''DOM.DOMString DOM.HTMLInputElement.setName()'''
            return DOM.DOMString()
        def name(self):
            '''DOM.DOMString DOM.HTMLInputElement.name()'''
            return DOM.DOMString()
        def setMaxLength(self):
            '''int DOM.HTMLInputElement.setMaxLength()'''
            return int()
        def maxLength(self):
            '''int DOM.HTMLInputElement.maxLength()'''
            return int()
        def setDisabled(self):
            '''bool DOM.HTMLInputElement.setDisabled()'''
            return bool()
        def disabled(self):
            '''bool DOM.HTMLInputElement.disabled()'''
            return bool()
        def setIndeterminate(self):
            '''bool DOM.HTMLInputElement.setIndeterminate()'''
            return bool()
        def indeterminate(self):
            '''bool DOM.HTMLInputElement.indeterminate()'''
            return bool()
        def setChecked(self):
            '''bool DOM.HTMLInputElement.setChecked()'''
            return bool()
        def checked(self):
            '''bool DOM.HTMLInputElement.checked()'''
            return bool()
        def setAlt(self):
            '''DOM.DOMString DOM.HTMLInputElement.setAlt()'''
            return DOM.DOMString()
        def alt(self):
            '''DOM.DOMString DOM.HTMLInputElement.alt()'''
            return DOM.DOMString()
        def setAlign(self):
            '''DOM.DOMString DOM.HTMLInputElement.setAlign()'''
            return DOM.DOMString()
        def align(self):
            '''DOM.DOMString DOM.HTMLInputElement.align()'''
            return DOM.DOMString()
        def setAccessKey(self):
            '''DOM.DOMString DOM.HTMLInputElement.setAccessKey()'''
            return DOM.DOMString()
        def accessKey(self):
            '''DOM.DOMString DOM.HTMLInputElement.accessKey()'''
            return DOM.DOMString()
        def setAccept(self):
            '''DOM.DOMString DOM.HTMLInputElement.setAccept()'''
            return DOM.DOMString()
        def accept(self):
            '''DOM.DOMString DOM.HTMLInputElement.accept()'''
            return DOM.DOMString()
        def form(self):
            '''DOM.HTMLFormElement DOM.HTMLInputElement.form()'''
            return DOM.HTMLFormElement()
        def setDefaultChecked(self):
            '''bool DOM.HTMLInputElement.setDefaultChecked()'''
            return bool()
        def defaultChecked(self):
            '''bool DOM.HTMLInputElement.defaultChecked()'''
            return bool()
        def setDefaultValue(self):
            '''DOM.DOMString DOM.HTMLInputElement.setDefaultValue()'''
            return DOM.DOMString()
        def defaultValue(self):
            '''DOM.DOMString DOM.HTMLInputElement.defaultValue()'''
            return DOM.DOMString()
    class HTMLDirectoryElement(DOM.HTMLElement):
        """"""
        def __init__(self):
            '''void DOM.HTMLDirectoryElement.__init__()'''
        def __init__(self, other):
            '''void DOM.HTMLDirectoryElement.__init__(DOM.HTMLDirectoryElement other)'''
        def __init__(self, other):
            '''void DOM.HTMLDirectoryElement.__init__(DOM.Node other)'''
        def setCompact(self):
            '''bool DOM.HTMLDirectoryElement.setCompact()'''
            return bool()
        def compact(self):
            '''bool DOM.HTMLDirectoryElement.compact()'''
            return bool()
    class CSSImportRule(DOM.CSSRule):
        """"""
        def __init__(self):
            '''void DOM.CSSImportRule.__init__()'''
        def __init__(self, other):
            '''void DOM.CSSImportRule.__init__(DOM.CSSImportRule other)'''
        def __init__(self, other):
            '''void DOM.CSSImportRule.__init__(DOM.CSSRule other)'''
        def styleSheet(self):
            '''DOM.CSSStyleSheet DOM.CSSImportRule.styleSheet()'''
            return DOM.CSSStyleSheet()
        def media(self):
            '''DOM.MediaList DOM.CSSImportRule.media()'''
            return DOM.MediaList()
        def href(self):
            '''DOM.DOMString DOM.CSSImportRule.href()'''
            return DOM.DOMString()
    class HTMLQuoteElement(DOM.HTMLElement):
        """"""
        def __init__(self):
            '''void DOM.HTMLQuoteElement.__init__()'''
        def __init__(self, other):
            '''void DOM.HTMLQuoteElement.__init__(DOM.HTMLQuoteElement other)'''
        def __init__(self, other):
            '''void DOM.HTMLQuoteElement.__init__(DOM.Node other)'''
        def setCite(self):
            '''DOM.DOMString DOM.HTMLQuoteElement.setCite()'''
            return DOM.DOMString()
        def cite(self):
            '''DOM.DOMString DOM.HTMLQuoteElement.cite()'''
            return DOM.DOMString()
    class DocumentStyle():
        """"""
        def __init__(self):
            '''void DOM.DocumentStyle.__init__()'''
        def __init__(self, other):
            '''void DOM.DocumentStyle.__init__(DOM.DocumentStyle other)'''
        def isNull(self):
            '''bool DOM.DocumentStyle.isNull()'''
            return bool()
        def setSelectedStylesheetSet(self, aString):
            '''void DOM.DocumentStyle.setSelectedStylesheetSet(DOM.DOMString aString)'''
        def selectedStylesheetSet(self):
            '''DOM.DOMString DOM.DocumentStyle.selectedStylesheetSet()'''
            return DOM.DOMString()
        def preferredStylesheetSet(self):
            '''DOM.DOMString DOM.DocumentStyle.preferredStylesheetSet()'''
            return DOM.DOMString()
        def styleSheets(self):
            '''DOM.StyleSheetList DOM.DocumentStyle.styleSheets()'''
            return DOM.StyleSheetList()
    class HTMLUListElement(DOM.HTMLElement):
        """"""
        def __init__(self):
            '''void DOM.HTMLUListElement.__init__()'''
        def __init__(self, other):
            '''void DOM.HTMLUListElement.__init__(DOM.HTMLUListElement other)'''
        def __init__(self, other):
            '''void DOM.HTMLUListElement.__init__(DOM.Node other)'''
        def setType(self):
            '''DOM.DOMString DOM.HTMLUListElement.setType()'''
            return DOM.DOMString()
        def type(self):
            '''DOM.DOMString DOM.HTMLUListElement.type()'''
            return DOM.DOMString()
        def setCompact(self):
            '''bool DOM.HTMLUListElement.setCompact()'''
            return bool()
        def compact(self):
            '''bool DOM.HTMLUListElement.compact()'''
            return bool()
    class Attr(DOM.Node):
        """"""
        def __init__(self):
            '''void DOM.Attr.__init__()'''
        def __init__(self, other):
            '''void DOM.Attr.__init__(DOM.Node other)'''
        def __init__(self, other):
            '''void DOM.Attr.__init__(DOM.Attr other)'''
        def ownerElement(self):
            '''DOM.Element DOM.Attr.ownerElement()'''
            return DOM.Element()
        def setValue(self):
            '''DOM.DOMString DOM.Attr.setValue()'''
            return DOM.DOMString()
        def value(self):
            '''DOM.DOMString DOM.Attr.value()'''
            return DOM.DOMString()
        def specified(self):
            '''bool DOM.Attr.specified()'''
            return bool()
        def name(self):
            '''DOM.DOMString DOM.Attr.name()'''
            return DOM.DOMString()
    class DocumentType(DOM.Node):
        """"""
        def __init__(self):
            '''void DOM.DocumentType.__init__()'''
        def __init__(self, other):
            '''void DOM.DocumentType.__init__(DOM.DocumentType other)'''
        def __init__(self, other):
            '''void DOM.DocumentType.__init__(DOM.Node other)'''
        def internalSubset(self):
            '''DOM.DOMString DOM.DocumentType.internalSubset()'''
            return DOM.DOMString()
        def systemId(self):
            '''DOM.DOMString DOM.DocumentType.systemId()'''
            return DOM.DOMString()
        def publicId(self):
            '''DOM.DOMString DOM.DocumentType.publicId()'''
            return DOM.DOMString()
        def notations(self):
            '''DOM.NamedNodeMap DOM.DocumentType.notations()'''
            return DOM.NamedNodeMap()
        def entities(self):
            '''DOM.NamedNodeMap DOM.DocumentType.entities()'''
            return DOM.NamedNodeMap()
        def name(self):
            '''DOM.DOMString DOM.DocumentType.name()'''
            return DOM.DOMString()
    class HTMLTableElement(DOM.HTMLElement):
        """"""
        def __init__(self):
            '''void DOM.HTMLTableElement.__init__()'''
        def __init__(self, other):
            '''void DOM.HTMLTableElement.__init__(DOM.HTMLTableElement other)'''
        def __init__(self, other):
            '''void DOM.HTMLTableElement.__init__(DOM.Node other)'''
        def deleteRow(self, index):
            '''void DOM.HTMLTableElement.deleteRow(int index)'''
        def insertRow(self, index):
            '''DOM.HTMLElement DOM.HTMLTableElement.insertRow(int index)'''
            return DOM.HTMLElement()
        def deleteCaption(self):
            '''void DOM.HTMLTableElement.deleteCaption()'''
        def createCaption(self):
            '''DOM.HTMLElement DOM.HTMLTableElement.createCaption()'''
            return DOM.HTMLElement()
        def deleteTFoot(self):
            '''void DOM.HTMLTableElement.deleteTFoot()'''
        def createTFoot(self):
            '''DOM.HTMLElement DOM.HTMLTableElement.createTFoot()'''
            return DOM.HTMLElement()
        def deleteTHead(self):
            '''void DOM.HTMLTableElement.deleteTHead()'''
        def createTHead(self):
            '''DOM.HTMLElement DOM.HTMLTableElement.createTHead()'''
            return DOM.HTMLElement()
        def setWidth(self):
            '''DOM.DOMString DOM.HTMLTableElement.setWidth()'''
            return DOM.DOMString()
        def width(self):
            '''DOM.DOMString DOM.HTMLTableElement.width()'''
            return DOM.DOMString()
        def setSummary(self):
            '''DOM.DOMString DOM.HTMLTableElement.setSummary()'''
            return DOM.DOMString()
        def summary(self):
            '''DOM.DOMString DOM.HTMLTableElement.summary()'''
            return DOM.DOMString()
        def setRules(self):
            '''DOM.DOMString DOM.HTMLTableElement.setRules()'''
            return DOM.DOMString()
        def rules(self):
            '''DOM.DOMString DOM.HTMLTableElement.rules()'''
            return DOM.DOMString()
        def setFrame(self):
            '''DOM.DOMString DOM.HTMLTableElement.setFrame()'''
            return DOM.DOMString()
        def frame(self):
            '''DOM.DOMString DOM.HTMLTableElement.frame()'''
            return DOM.DOMString()
        def setCellSpacing(self):
            '''DOM.DOMString DOM.HTMLTableElement.setCellSpacing()'''
            return DOM.DOMString()
        def cellSpacing(self):
            '''DOM.DOMString DOM.HTMLTableElement.cellSpacing()'''
            return DOM.DOMString()
        def setCellPadding(self):
            '''DOM.DOMString DOM.HTMLTableElement.setCellPadding()'''
            return DOM.DOMString()
        def cellPadding(self):
            '''DOM.DOMString DOM.HTMLTableElement.cellPadding()'''
            return DOM.DOMString()
        def setBorder(self):
            '''DOM.DOMString DOM.HTMLTableElement.setBorder()'''
            return DOM.DOMString()
        def border(self):
            '''DOM.DOMString DOM.HTMLTableElement.border()'''
            return DOM.DOMString()
        def setBgColor(self):
            '''DOM.DOMString DOM.HTMLTableElement.setBgColor()'''
            return DOM.DOMString()
        def bgColor(self):
            '''DOM.DOMString DOM.HTMLTableElement.bgColor()'''
            return DOM.DOMString()
        def setAlign(self):
            '''DOM.DOMString DOM.HTMLTableElement.setAlign()'''
            return DOM.DOMString()
        def align(self):
            '''DOM.DOMString DOM.HTMLTableElement.align()'''
            return DOM.DOMString()
        def tBodies(self):
            '''DOM.HTMLCollection DOM.HTMLTableElement.tBodies()'''
            return DOM.HTMLCollection()
        def rows(self):
            '''DOM.HTMLCollection DOM.HTMLTableElement.rows()'''
            return DOM.HTMLCollection()
        def setTFoot(self):
            '''DOM.HTMLTableSectionElement DOM.HTMLTableElement.setTFoot()'''
            return DOM.HTMLTableSectionElement()
        def tFoot(self):
            '''DOM.HTMLTableSectionElement DOM.HTMLTableElement.tFoot()'''
            return DOM.HTMLTableSectionElement()
        def setTHead(self):
            '''DOM.HTMLTableSectionElement DOM.HTMLTableElement.setTHead()'''
            return DOM.HTMLTableSectionElement()
        def tHead(self):
            '''DOM.HTMLTableSectionElement DOM.HTMLTableElement.tHead()'''
            return DOM.HTMLTableSectionElement()
        def setCaption(self):
            '''DOM.HTMLTableCaptionElement DOM.HTMLTableElement.setCaption()'''
            return DOM.HTMLTableCaptionElement()
        def caption(self):
            '''DOM.HTMLTableCaptionElement DOM.HTMLTableElement.caption()'''
            return DOM.HTMLTableCaptionElement()
    class HTMLBaseElement(DOM.HTMLElement):
        """"""
        def __init__(self):
            '''void DOM.HTMLBaseElement.__init__()'''
        def __init__(self, other):
            '''void DOM.HTMLBaseElement.__init__(DOM.HTMLBaseElement other)'''
        def __init__(self, other):
            '''void DOM.HTMLBaseElement.__init__(DOM.Node other)'''
        def setTarget(self):
            '''DOM.DOMString DOM.HTMLBaseElement.setTarget()'''
            return DOM.DOMString()
        def target(self):
            '''DOM.DOMString DOM.HTMLBaseElement.target()'''
            return DOM.DOMString()
        def setHref(self):
            '''DOM.DOMString DOM.HTMLBaseElement.setHref()'''
            return DOM.DOMString()
        def href(self):
            '''DOM.DOMString DOM.HTMLBaseElement.href()'''
            return DOM.DOMString()
    class HTMLDListElement(DOM.HTMLElement):
        """"""
        def __init__(self):
            '''void DOM.HTMLDListElement.__init__()'''
        def __init__(self, other):
            '''void DOM.HTMLDListElement.__init__(DOM.HTMLDListElement other)'''
        def __init__(self, other):
            '''void DOM.HTMLDListElement.__init__(DOM.Node other)'''
        def setCompact(self):
            '''bool DOM.HTMLDListElement.setCompact()'''
            return bool()
        def compact(self):
            '''bool DOM.HTMLDListElement.compact()'''
            return bool()
    class MouseEvent(DOM.UIEvent):
        """"""
        def __init__(self):
            '''void DOM.MouseEvent.__init__()'''
        def __init__(self, other):
            '''void DOM.MouseEvent.__init__(DOM.MouseEvent other)'''
        def __init__(self, other):
            '''void DOM.MouseEvent.__init__(DOM.Event other)'''
        def initMouseEvent(self, typeArg, canBubbleArg, cancelableArg, viewArg, detailArg, screenXArg, screenYArg, clientXArg, clientYArg, ctrlKeyArg, altKeyArg, shiftKeyArg, metaKeyArg, buttonArg, relatedTargetArg):
            '''void DOM.MouseEvent.initMouseEvent(DOM.DOMString typeArg, bool canBubbleArg, bool cancelableArg, DOM.AbstractView viewArg, int detailArg, int screenXArg, int screenYArg, int clientXArg, int clientYArg, bool ctrlKeyArg, bool altKeyArg, bool shiftKeyArg, bool metaKeyArg, int buttonArg, DOM.Node relatedTargetArg)'''
        def relatedTarget(self):
            '''DOM.Node DOM.MouseEvent.relatedTarget()'''
            return DOM.Node()
        def button(self):
            '''int DOM.MouseEvent.button()'''
            return int()
        def metaKey(self):
            '''bool DOM.MouseEvent.metaKey()'''
            return bool()
        def altKey(self):
            '''bool DOM.MouseEvent.altKey()'''
            return bool()
        def shiftKey(self):
            '''bool DOM.MouseEvent.shiftKey()'''
            return bool()
        def ctrlKey(self):
            '''bool DOM.MouseEvent.ctrlKey()'''
            return bool()
        def clientY(self):
            '''int DOM.MouseEvent.clientY()'''
            return int()
        def clientX(self):
            '''int DOM.MouseEvent.clientX()'''
            return int()
        def screenY(self):
            '''int DOM.MouseEvent.screenY()'''
            return int()
        def screenX(self):
            '''int DOM.MouseEvent.screenX()'''
            return int()
    class DOMException():
        """"""
        # Enum DOM.DOMException.ExceptionCode
        INDEX_SIZE_ERR = 0
        DOMSTRING_SIZE_ERR = 0
        HIERARCHY_REQUEST_ERR = 0
        WRONG_DOCUMENT_ERR = 0
        INVALID_CHARACTER_ERR = 0
        NO_DATA_ALLOWED_ERR = 0
        NO_MODIFICATION_ALLOWED_ERR = 0
        NOT_FOUND_ERR = 0
        NOT_SUPPORTED_ERR = 0
        INUSE_ATTRIBUTE_ERR = 0
        INVALID_STATE_ERR = 0
        SYNTAX_ERR = 0
        INVALID_MODIFICATION_ERR = 0
        NAMESPACE_ERR = 0
        INVALID_ACCESS_ERR = 0
        VALIDATION_ERR = 0
        TYPE_MISMATCH_ERR = 0
        SECURITY_ERR = 0
        NETWORK_ERR = 0
        ABORT_ERR = 0
        URL_MISMATCH_ERR = 0
        QUOTA_EXCEEDED_ERR = 0
        TIMEOUT_ERR = 0
        NOT_READABLE_ERR = 0
        DATA_CLONE_ERR = 0
        ENCODING_ERR = 0
    
        code = None # int - member
        def __init__(self, _code):
            '''void DOM.DOMException.__init__(int _code)'''
        def __init__(self, other):
            '''void DOM.DOMException.__init__(DOM.DOMException other)'''
        def isDOMExceptionCode(self, exceptioncode):
            '''static bool DOM.DOMException.isDOMExceptionCode(int exceptioncode)'''
            return bool()
        def codeAsString(self):
            '''DOM.DOMString DOM.DOMException.codeAsString()'''
            return DOM.DOMString()
        def codeAsString(self, code):
            '''static DOM.DOMString DOM.DOMException.codeAsString(int code)'''
            return DOM.DOMString()
    class NodeFilter():
        """"""
        # Enum DOM.NodeFilter.ShowCode
        SHOW_ALL = 0
        SHOW_ELEMENT = 0
        SHOW_ATTRIBUTE = 0
        SHOW_TEXT = 0
        SHOW_CDATA_SECTION = 0
        SHOW_ENTITY_REFERENCE = 0
        SHOW_ENTITY = 0
        SHOW_PROCESSING_INSTRUCTION = 0
        SHOW_COMMENT = 0
        SHOW_DOCUMENT = 0
        SHOW_DOCUMENT_TYPE = 0
        SHOW_DOCUMENT_FRAGMENT = 0
        SHOW_NOTATION = 0
    
        # Enum DOM.NodeFilter.AcceptCode
        FILTER_ACCEPT = 0
        FILTER_REJECT = 0
        FILTER_SKIP = 0
    
        def __init__(self):
            '''void DOM.NodeFilter.__init__()'''
        def __init__(self, other):
            '''void DOM.NodeFilter.__init__(DOM.NodeFilter other)'''
        def createCustom(self, custom):
            '''static DOM.NodeFilter DOM.NodeFilter.createCustom(DOM.CustomNodeFilter custom)'''
            return DOM.NodeFilter()
        def customNodeFilter(self):
            '''DOM.CustomNodeFilter DOM.NodeFilter.customNodeFilter()'''
            return DOM.CustomNodeFilter()
        def setCustomNodeFilter(self, custom):
            '''void DOM.NodeFilter.setCustomNodeFilter(DOM.CustomNodeFilter custom)'''
        def isNull(self):
            '''bool DOM.NodeFilter.isNull()'''
            return bool()
        def acceptNode(self, n):
            '''int DOM.NodeFilter.acceptNode(DOM.Node n)'''
            return int()
    class CSSFontFaceRule(DOM.CSSRule):
        """"""
        def __init__(self):
            '''void DOM.CSSFontFaceRule.__init__()'''
        def __init__(self, other):
            '''void DOM.CSSFontFaceRule.__init__(DOM.CSSFontFaceRule other)'''
        def __init__(self, other):
            '''void DOM.CSSFontFaceRule.__init__(DOM.CSSRule other)'''
        def style(self):
            '''DOM.CSSStyleDeclaration DOM.CSSFontFaceRule.style()'''
            return DOM.CSSStyleDeclaration()


class KHTMLPart(KParts.ReadOnlyPart):
    """"""
    # Enum KHTMLPart.PageSecurity
    NotCrypted = 0
    Encrypted = 0
    Mixed = 0

    # Enum KHTMLPart.FormNotification
    NoNotification = 0
    Before = 0
    Only = 0
    Unused = 0

    # Enum KHTMLPart.FindOptions
    FindLinksOnly = 0
    FindNoPopups = 0

    # Enum KHTMLPart.CaretDisplayPolicy
    CaretVisible = 0
    CaretInvisible = 0
    CaretBlink = 0

    # Enum KHTMLPart.DNSPrefetch
    DNSPrefetchDisabled = 0
    DNSPrefetchEnabled = 0
    DNSPrefetchOnlyWWWAndSLD = 0

    # Enum KHTMLPart.GUIProfile
    DefaultGUI = 0
    BrowserViewGUI = 0

    def __init__(self, parentWidget = None, parent = None, prof = None):
        '''void KHTMLPart.__init__(QWidget parentWidget = None, QObject parent = None, KHTMLPart.GUIProfile prof = KHTMLPart.DefaultGUI)'''
    def __init__(self, view, parent = None, prof = None):
        '''void KHTMLPart.__init__(KHTMLView view, QObject parent = None, KHTMLPart.GUIProfile prof = KHTMLPart.DefaultGUI)'''
    def forcePermitLocalImages(self):
        '''bool KHTMLPart.forcePermitLocalImages()'''
        return bool()
    def setForcePermitLocalImages(self, enable):
        '''void KHTMLPart.setForcePermitLocalImages(bool enable)'''
    def updateZoomFactor(self):
        '''void KHTMLPart.updateZoomFactor()'''
    def startingJob(self):
        '''KIO.Job KHTMLPart.startingJob()'''
        return KIO.Job()
    def slotFinished(self):
        '''KJob KHTMLPart.slotFinished()'''
        return KJob()
    def submitFormProxy(self, action, url, formData, target, contentType = QString(), boundary = QString()):
        '''void KHTMLPart.submitFormProxy(str action, QString url, QByteArray formData, QString target, QString contentType = QString(), QString boundary = QString())'''
    def setCaretVisible(self, show):
        '''void KHTMLPart.setCaretVisible(bool show)'''
    def setEditable(self, enable):
        '''void KHTMLPart.setEditable(bool enable)'''
    def setCaretMode(self, enable):
        '''void KHTMLPart.setCaretMode(bool enable)'''
    def stopAnimations(self):
        '''void KHTMLPart.stopAnimations()'''
    def setActiveNode(self, node):
        '''void KHTMLPart.setActiveNode(DOM.Node node)'''
    def mayPrefetchHostname(self, name):
        '''bool KHTMLPart.mayPrefetchHostname(QString name)'''
        return bool()
    def timerEvent(self):
        '''QTimerEvent KHTMLPart.timerEvent()'''
        return QTimerEvent()
    def doCloseStream(self):
        '''bool KHTMLPart.doCloseStream()'''
        return bool()
    def doWriteStream(self, data):
        '''bool KHTMLPart.doWriteStream(QByteArray data)'''
        return bool()
    def doOpenStream(self, mimeType):
        '''bool KHTMLPart.doOpenStream(QString mimeType)'''
        return bool()
    def setPluginPageQuestionAsked(self, mimetype):
        '''void KHTMLPart.setPluginPageQuestionAsked(QString mimetype)'''
    def pluginPageQuestionAsked(self, mimetype):
        '''bool KHTMLPart.pluginPageQuestionAsked(QString mimetype)'''
        return bool()
    def createPart(self, parentWidget, parent, mimetype, serviceName, serviceTypes, params):
        '''KParts.ReadOnlyPart KHTMLPart.createPart(QWidget parentWidget, QObject parent, QString mimetype, QString serviceName, QStringList serviceTypes, QStringList params)'''
        return KParts.ReadOnlyPart()
    def urlSelected(self, url, button, state, _target, args = None, browserArgs = None):
        '''bool KHTMLPart.urlSelected(QString url, int button, int state, QString _target, KParts.OpenUrlArguments args = KParts.OpenUrlArguments(), KParts.BrowserArguments browserArgs = KParts.BrowserArguments())'''
        return bool()
    def openFile(self):
        '''bool KHTMLPart.openFile()'''
        return bool()
    def guiActivateEvent(self, event):
        '''void KHTMLPart.guiActivateEvent(KParts.GUIActivateEvent event)'''
    def customEvent(self, event):
        '''void KHTMLPart.customEvent(QEvent event)'''
    def htmlError(self, errorCode, text, reqUrl):
        '''void KHTMLPart.htmlError(int errorCode, QString text, KUrl reqUrl)'''
    def completeURL(self, url):
        '''KUrl KHTMLPart.completeURL(QString url)'''
        return KUrl()
    configurationChanged = pyqtSignal() # void configurationChanged() - signal
    formSubmitNotification = pyqtSignal() # void formSubmitNotification(const char *,const QStringamp;,const QByteArrayamp;,const QStringamp;,const QStringamp;,const QStringamp;) - signal
    caretPositionChanged = pyqtSignal() # void caretPositionChanged(const DOM::Nodeamp;,long) - signal
    docCreated = pyqtSignal() # void docCreated() - signal
    nodeActivated = pyqtSignal() # void nodeActivated(const DOM::Nodeamp;) - signal
    selectionChanged = pyqtSignal() # void selectionChanged() - signal
    popupMenu = pyqtSignal() # void popupMenu(const QStringamp;,const QPointamp;) - signal
    onURL = pyqtSignal() # void onURL(const QStringamp;) - signal
    def inProgress(self):
        '''bool KHTMLPart.inProgress()'''
        return bool()
    def setSuppressedPopupIndicator(self, enable, originPart = None):
        '''void KHTMLPart.setSuppressedPopupIndicator(bool enable, KHTMLPart originPart = None)'''
    def isModified(self):
        '''bool KHTMLPart.isModified()'''
        return bool()
    def toplevelURL(self):
        '''KUrl KHTMLPart.toplevelURL()'''
        return KUrl()
    def formNotification(self):
        '''KHTMLPart.FormNotification KHTMLPart.formNotification()'''
        return KHTMLPart.FormNotification()
    def setFormNotification(self, fn):
        '''void KHTMLPart.setFormNotification(KHTMLPart.FormNotification fn)'''
    def setAlwaysHonourDoctype(self, b = True):
        '''void KHTMLPart.setAlwaysHonourDoctype(bool b = True)'''
    def restored(self):
        '''bool KHTMLPart.restored()'''
        return bool()
    def isPointInsideSelection(self, x, y):
        '''bool KHTMLPart.isPointInsideSelection(int x, int y)'''
        return bool()
    def preloadScript(self, url, script):
        '''void KHTMLPart.preloadScript(QString url, QString script)'''
    def preloadStyleSheet(self, url, stylesheet):
        '''void KHTMLPart.preloadStyleSheet(QString url, QString stylesheet)'''
    def lastModified(self):
        '''QString KHTMLPart.lastModified()'''
        return QString()
    def pageReferrer(self):
        '''QString KHTMLPart.pageReferrer()'''
        return QString()
    def referrer(self):
        '''QString KHTMLPart.referrer()'''
        return QString()
    def jsDefaultStatusBarText(self):
        '''QString KHTMLPart.jsDefaultStatusBarText()'''
        return QString()
    def jsStatusBarText(self):
        '''QString KHTMLPart.jsStatusBarText()'''
        return QString()
    def setJSDefaultStatusBarText(self, text):
        '''void KHTMLPart.setJSDefaultStatusBarText(QString text)'''
    def setJSStatusBarText(self, text):
        '''void KHTMLPart.setJSStatusBarText(QString text)'''
    def findFramePart(self, f):
        '''KParts.ReadOnlyPart KHTMLPart.findFramePart(QString f)'''
        return KParts.ReadOnlyPart()
    def frameExists(self, frameName):
        '''bool KHTMLPart.frameExists(QString frameName)'''
        return bool()
    def currentFrame(self):
        '''KParts.ReadOnlyPart KHTMLPart.currentFrame()'''
        return KParts.ReadOnlyPart()
    def findFrame(self, f):
        '''KHTMLPart KHTMLPart.findFrame(QString f)'''
        return KHTMLPart()
    def frames(self):
        '''list-of-KParts.ReadOnlyPart KHTMLPart.frames()'''
        return [KParts.ReadOnlyPart()]
    def frameNames(self):
        '''QStringList KHTMLPart.frameNames()'''
        return QStringList()
    def parentPart(self):
        '''KHTMLPart KHTMLPart.parentPart()'''
        return KHTMLPart()
    def settings(self):
        '''KHTMLSettings KHTMLPart.settings()'''
        return KHTMLSettings()
    def nonSharedNodeUnderMouse(self):
        '''DOM.Node KHTMLPart.nonSharedNodeUnderMouse()'''
        return DOM.Node()
    def nodeUnderMouse(self):
        '''DOM.Node KHTMLPart.nodeUnderMouse()'''
        return DOM.Node()
    def restoreState(self, stream):
        '''void KHTMLPart.restoreState(QDataStream stream)'''
    def saveState(self, stream):
        '''void KHTMLPart.saveState(QDataStream stream)'''
    def partManager(self):
        '''KParts.PartManager KHTMLPart.partManager()'''
        return KParts.PartManager()
    def hide(self):
        '''void KHTMLPart.hide()'''
    def show(self):
        '''void KHTMLPart.show()'''
    def selectAll(self):
        '''void KHTMLPart.selectAll()'''
    def hasSelection(self):
        '''bool KHTMLPart.hasSelection()'''
        return bool()
    def setSelection(self):
        '''DOM.Range KHTMLPart.setSelection()'''
        return DOM.Range()
    def selection(self):
        '''DOM.Range KHTMLPart.selection()'''
        return DOM.Range()
    def selection(self, startNode, startOffset, endNode, endOffset):
        '''void KHTMLPart.selection(DOM.Node startNode, int startOffset, DOM.Node endNode, int endOffset)'''
    def selectedTextAsHTML(self):
        '''QString KHTMLPart.selectedTextAsHTML()'''
        return QString()
    def selectedText(self):
        '''QString KHTMLPart.selectedText()'''
        return QString()
    def fontScaleFactor(self):
        '''int KHTMLPart.fontScaleFactor()'''
        return int()
    def setFontScaleFactor(self, percent):
        '''void KHTMLPart.setFontScaleFactor(int percent)'''
    def zoomFactor(self):
        '''int KHTMLPart.zoomFactor()'''
        return int()
    def setZoomFactor(self, percent):
        '''void KHTMLPart.setZoomFactor(int percent)'''
    def findTextNext(self, reverse = False):
        '''bool KHTMLPart.findTextNext(bool reverse = False)'''
        return bool()
    def findTextBegin(self):
        '''void KHTMLPart.findTextBegin()'''
    def findText(self):
        '''void KHTMLPart.findText()'''
    def findText(self, str, options, parent = None, findDialog = None):
        '''void KHTMLPart.findText(QString str, int options, QWidget parent = None, KFindDialog findDialog = None)'''
    def urlCursor(self):
        '''QCursor KHTMLPart.urlCursor()'''
        return QCursor()
    def setURLCursor(self, c):
        '''void KHTMLPart.setURLCursor(QCursor c)'''
    def prevAnchor(self):
        '''bool KHTMLPart.prevAnchor()'''
        return bool()
    def nextAnchor(self):
        '''bool KHTMLPart.nextAnchor()'''
        return bool()
    def gotoAnchor(self, name):
        '''bool KHTMLPart.gotoAnchor(QString name)'''
        return bool()
    def setFixedFont(self, name):
        '''void KHTMLPart.setFixedFont(QString name)'''
    def setStandardFont(self, name):
        '''void KHTMLPart.setStandardFont(QString name)'''
    def setUserStyleSheet(self, url):
        '''void KHTMLPart.setUserStyleSheet(KUrl url)'''
    def setUserStyleSheet(self, styleSheet):
        '''void KHTMLPart.setUserStyleSheet(QString styleSheet)'''
    def encoding(self):
        '''QString KHTMLPart.encoding()'''
        return QString()
    def setEncoding(self, name, override = False):
        '''bool KHTMLPart.setEncoding(QString name, bool override = False)'''
        return bool()
    def paint(self):
        '''bool KHTMLPart.paint()'''
        return bool()
    def end(self):
        '''void KHTMLPart.end()'''
    def write(self, str, len = None):
        '''void KHTMLPart.write(str str, int len = -1)'''
    def write(self, str):
        '''void KHTMLPart.write(QString str)'''
    def begin(self, url = KUrl(), xOffset = 0, yOffset = 0):
        '''void KHTMLPart.begin(KUrl url = KUrl(), int xOffset = 0, int yOffset = 0)'''
    def scheduleRedirection(self, delay, url, lockHistory = True):
        '''void KHTMLPart.scheduleRedirection(int delay, QString url, bool lockHistory = True)'''
    def backgroundURL(self):
        '''KUrl KHTMLPart.backgroundURL()'''
        return KUrl()
    def baseURL(self):
        '''KUrl KHTMLPart.baseURL()'''
        return KUrl()
    def setCaretDisplayPolicyNonFocused(self, policy):
        '''void KHTMLPart.setCaretDisplayPolicyNonFocused(KHTMLPart.CaretDisplayPolicy policy)'''
    def caretDisplayPolicyNonFocused(self):
        '''KHTMLPart.CaretDisplayPolicy KHTMLPart.caretDisplayPolicyNonFocused()'''
        return KHTMLPart.CaretDisplayPolicy()
    def setCaretPosition(self, node, offset, extendSelection = False):
        '''void KHTMLPart.setCaretPosition(DOM.Node node, int offset, bool extendSelection = False)'''
    def isEditable(self):
        '''bool KHTMLPart.isEditable()'''
        return bool()
    def isCaretMode(self):
        '''bool KHTMLPart.isCaretMode()'''
        return bool()
    def onlyLocalReferences(self):
        '''bool KHTMLPart.onlyLocalReferences()'''
        return bool()
    def dnsPrefetch(self):
        '''KHTMLPart.DNSPrefetch KHTMLPart.dnsPrefetch()'''
        return KHTMLPart.DNSPrefetch()
    def setDNSPrefetch(self, pmode):
        '''void KHTMLPart.setDNSPrefetch(KHTMLPart.DNSPrefetch pmode)'''
    def setOnlyLocalReferences(self, enable):
        '''void KHTMLPart.setOnlyLocalReferences(bool enable)'''
    def autoloadImages(self):
        '''bool KHTMLPart.autoloadImages()'''
        return bool()
    def setAutoloadImages(self, enable):
        '''void KHTMLPart.setAutoloadImages(bool enable)'''
    def pluginsEnabled(self):
        '''bool KHTMLPart.pluginsEnabled()'''
        return bool()
    def setPluginsEnabled(self, enable):
        '''void KHTMLPart.setPluginsEnabled(bool enable)'''
    def javaEnabled(self):
        '''bool KHTMLPart.javaEnabled()'''
        return bool()
    def setJavaEnabled(self, enable):
        '''void KHTMLPart.setJavaEnabled(bool enable)'''
    def dndEnabled(self):
        '''bool KHTMLPart.dndEnabled()'''
        return bool()
    def setDNDEnabled(self, b):
        '''void KHTMLPart.setDNDEnabled(bool b)'''
    def executeScript(self, n, script):
        '''QVariant KHTMLPart.executeScript(DOM.Node n, QString script)'''
        return QVariant()
    def executeScript(self, script):
        '''QVariant KHTMLPart.executeScript(QString script)'''
        return QVariant()
    def metaRefreshEnabled(self):
        '''bool KHTMLPart.metaRefreshEnabled()'''
        return bool()
    def setMetaRefreshEnabled(self, enable):
        '''void KHTMLPart.setMetaRefreshEnabled(bool enable)'''
    def statusMessagesEnabled(self):
        '''bool KHTMLPart.statusMessagesEnabled()'''
        return bool()
    def setStatusMessagesEnabled(self, enable):
        '''void KHTMLPart.setStatusMessagesEnabled(bool enable)'''
    def jScriptEnabled(self):
        '''bool KHTMLPart.jScriptEnabled()'''
        return bool()
    def setJScriptEnabled(self, enable):
        '''void KHTMLPart.setJScriptEnabled(bool enable)'''
    def view(self):
        '''KHTMLView KHTMLPart.view()'''
        return KHTMLView()
    def browserHostExtension(self):
        '''KParts.BrowserHostExtension KHTMLPart.browserHostExtension()'''
        return KParts.BrowserHostExtension()
    def browserExtension(self):
        '''KParts.BrowserExtension KHTMLPart.browserExtension()'''
        return KParts.BrowserExtension()
    def activeNode(self):
        '''DOM.Node KHTMLPart.activeNode()'''
        return DOM.Node()
    def documentSource(self):
        '''QString KHTMLPart.documentSource()'''
        return QString()
    def document(self):
        '''DOM.Document KHTMLPart.document()'''
        return DOM.Document()
    def htmlDocument(self):
        '''DOM.HTMLDocument KHTMLPart.htmlDocument()'''
        return DOM.HTMLDocument()
    def showError(self, job):
        '''void KHTMLPart.showError(KJob job)'''
    def closeUrl(self):
        '''bool KHTMLPart.closeUrl()'''
        return bool()
    def openUrl(self, url):
        '''bool KHTMLPart.openUrl(KUrl url)'''
        return bool()


class KHTMLSettings():
    """"""
    # Enum KHTMLSettings.KJSWindowFocusPolicy
    KJSWindowFocusAllow = 0
    KJSWindowFocusIgnore = 0

    # Enum KHTMLSettings.KJSWindowResizePolicy
    KJSWindowResizeAllow = 0
    KJSWindowResizeIgnore = 0

    # Enum KHTMLSettings.KJSWindowMovePolicy
    KJSWindowMoveAllow = 0
    KJSWindowMoveIgnore = 0

    # Enum KHTMLSettings.KJSWindowStatusPolicy
    KJSWindowStatusAllow = 0
    KJSWindowStatusIgnore = 0

    # Enum KHTMLSettings.KJSWindowOpenPolicy
    KJSWindowOpenAllow = 0
    KJSWindowOpenAsk = 0
    KJSWindowOpenDeny = 0
    KJSWindowOpenSmart = 0

    # Enum KHTMLSettings.KDNSPrefetch
    KDNSPrefetchDisabled = 0
    KDNSPrefetchOnlyWWWAndSLD = 0
    KDNSPrefetchEnabled = 0

    # Enum KHTMLSettings.KSmoothScrollingMode
    KSmoothScrollingDisabled = 0
    KSmoothScrollingWhenEfficient = 0
    KSmoothScrollingEnabled = 0

    # Enum KHTMLSettings.KAnimationAdvice
    KAnimationDisabled = 0
    KAnimationLoopOnce = 0
    KAnimationEnabled = 0

    # Enum KHTMLSettings.KJavaScriptAdvice
    KJavaScriptDunno = 0
    KJavaScriptAccept = 0
    KJavaScriptReject = 0

    def __init__(self):
        '''void KHTMLSettings.__init__()'''
    def adFilteredBy(self, url, isWhiteListed):
        '''QString KHTMLSettings.adFilteredBy(QString url, bool isWhiteListed)'''
        return QString()
    def jsPopupBlockerPassivePopup(self):
        '''bool KHTMLSettings.jsPopupBlockerPassivePopup()'''
        return bool()
    def setJSPopupBlockerPassivePopup(self, enabled):
        '''void KHTMLSettings.setJSPopupBlockerPassivePopup(bool enabled)'''
    def fallbackAccessKeysAssignments(self):
        '''list-of-tuple-of-QString-QChar KHTMLSettings.fallbackAccessKeysAssignments()'''
        return [tuple-of-QString-QChar()]
    def isAutoDelayedActionsEnabled(self):
        '''bool KHTMLSettings.isAutoDelayedActionsEnabled()'''
        return bool()
    def maxFormCompletionItems(self):
        '''int KHTMLSettings.maxFormCompletionItems()'''
        return int()
    def isFormCompletionEnabled(self):
        '''bool KHTMLSettings.isFormCompletionEnabled()'''
        return bool()
    def userStyleSheet(self):
        '''QString KHTMLSettings.userStyleSheet()'''
        return QString()
    def availableFamilies(self):
        '''static QString KHTMLSettings.availableFamilies()'''
        return QString()
    def settingsToCSS(self):
        '''QString KHTMLSettings.settingsToCSS()'''
        return QString()
    def adviceToStr(self, _advice):
        '''static str KHTMLSettings.adviceToStr(KHTMLSettings.KJavaScriptAdvice _advice)'''
        return str()
    def strToAdvice(self, _str):
        '''static KHTMLSettings.KJavaScriptAdvice KHTMLSettings.strToAdvice(QString _str)'''
        return KHTMLSettings.KJavaScriptAdvice()
    def windowFocusPolicy(self, hostname = QString()):
        '''KHTMLSettings.KJSWindowFocusPolicy KHTMLSettings.windowFocusPolicy(QString hostname = QString())'''
        return KHTMLSettings.KJSWindowFocusPolicy()
    def windowStatusPolicy(self, hostname = QString()):
        '''KHTMLSettings.KJSWindowStatusPolicy KHTMLSettings.windowStatusPolicy(QString hostname = QString())'''
        return KHTMLSettings.KJSWindowStatusPolicy()
    def windowResizePolicy(self, hostname = QString()):
        '''KHTMLSettings.KJSWindowResizePolicy KHTMLSettings.windowResizePolicy(QString hostname = QString())'''
        return KHTMLSettings.KJSWindowResizePolicy()
    def windowMovePolicy(self, hostname = QString()):
        '''KHTMLSettings.KJSWindowMovePolicy KHTMLSettings.windowMovePolicy(QString hostname = QString())'''
        return KHTMLSettings.KJSWindowMovePolicy()
    def windowOpenPolicy(self, hostname = QString()):
        '''KHTMLSettings.KJSWindowOpenPolicy KHTMLSettings.windowOpenPolicy(QString hostname = QString())'''
        return KHTMLSettings.KJSWindowOpenPolicy()
    def accessKeysEnabled(self):
        '''bool KHTMLSettings.accessKeysEnabled()'''
        return bool()
    def addAdFilter(self, url):
        '''void KHTMLSettings.addAdFilter(QString url)'''
    def isHideAdsEnabled(self):
        '''bool KHTMLSettings.isHideAdsEnabled()'''
        return bool()
    def isAdFilterEnabled(self):
        '''bool KHTMLSettings.isAdFilterEnabled()'''
        return bool()
    def isAdFiltered(self, url):
        '''bool KHTMLSettings.isAdFiltered(QString url)'''
        return bool()
    def isPluginsEnabled(self, hostname = QString()):
        '''bool KHTMLSettings.isPluginsEnabled(QString hostname = QString())'''
        return bool()
    def isJavaScriptErrorReportingEnabled(self, hostname = QString()):
        '''bool KHTMLSettings.isJavaScriptErrorReportingEnabled(QString hostname = QString())'''
        return bool()
    def isJavaScriptDebugEnabled(self, hostname = QString()):
        '''bool KHTMLSettings.isJavaScriptDebugEnabled(QString hostname = QString())'''
        return bool()
    def isJavaScriptEnabled(self, hostname = QString()):
        '''bool KHTMLSettings.isJavaScriptEnabled(QString hostname = QString())'''
        return bool()
    def isJavaEnabled(self, hostname = QString()):
        '''bool KHTMLSettings.isJavaEnabled(QString hostname = QString())'''
        return bool()
    def isBackRightClickEnabled(self):
        '''bool KHTMLSettings.isBackRightClickEnabled()'''
        return bool()
    def isOpenMiddleClickEnabled(self):
        '''bool KHTMLSettings.isOpenMiddleClickEnabled()'''
        return bool()
    def unfinishedImageFrame(self):
        '''bool KHTMLSettings.unfinishedImageFrame()'''
        return bool()
    def autoLoadImages(self):
        '''bool KHTMLSettings.autoLoadImages()'''
        return bool()
    def vLinkColor(self):
        '''QColor KHTMLSettings.vLinkColor()'''
        return QColor()
    def linkColor(self):
        '''QColor KHTMLSettings.linkColor()'''
        return QColor()
    def baseColor(self):
        '''QColor KHTMLSettings.baseColor()'''
        return QColor()
    def textColor(self):
        '''QColor KHTMLSettings.textColor()'''
        return QColor()
    def followSystemColors(self):
        '''bool KHTMLSettings.followSystemColors()'''
        return bool()
    def encoding(self):
        '''QString KHTMLSettings.encoding()'''
        return QString()
    def setJSErrorsEnabled(self, enabled):
        '''void KHTMLSettings.setJSErrorsEnabled(bool enabled)'''
    def jsErrorsEnabled(self):
        '''bool KHTMLSettings.jsErrorsEnabled()'''
        return bool()
    def mediumFontSize(self):
        '''int KHTMLSettings.mediumFontSize()'''
        return int()
    def minFontSize(self):
        '''int KHTMLSettings.minFontSize()'''
        return int()
    def setFixedFontName(self, n):
        '''void KHTMLSettings.setFixedFontName(QString n)'''
    def setStdFontName(self, n):
        '''void KHTMLSettings.setStdFontName(QString n)'''
    def fantasyFontName(self):
        '''QString KHTMLSettings.fantasyFontName()'''
        return QString()
    def cursiveFontName(self):
        '''QString KHTMLSettings.cursiveFontName()'''
        return QString()
    def sansSerifFontName(self):
        '''QString KHTMLSettings.sansSerifFontName()'''
        return QString()
    def serifFontName(self):
        '''QString KHTMLSettings.serifFontName()'''
        return QString()
    def fixedFontName(self):
        '''QString KHTMLSettings.fixedFontName()'''
        return QString()
    def stdFontName(self):
        '''QString KHTMLSettings.stdFontName()'''
        return QString()
    def dnsPrefetch(self):
        '''KHTMLSettings.KDNSPrefetch KHTMLSettings.dnsPrefetch()'''
        return KHTMLSettings.KDNSPrefetch()
    def smoothScrolling(self):
        '''KHTMLSettings.KSmoothScrollingMode KHTMLSettings.smoothScrolling()'''
        return KHTMLSettings.KSmoothScrollingMode()
    def showAnimations(self):
        '''KHTMLSettings.KAnimationAdvice KHTMLSettings.showAnimations()'''
        return KHTMLSettings.KAnimationAdvice()
    def autoSpellCheck(self):
        '''bool KHTMLSettings.autoSpellCheck()'''
        return bool()
    def allowTabulation(self):
        '''bool KHTMLSettings.allowTabulation()'''
        return bool()
    def hoverLink(self):
        '''bool KHTMLSettings.hoverLink()'''
        return bool()
    def underlineLink(self):
        '''bool KHTMLSettings.underlineLink()'''
        return bool()
    def changeCursor(self):
        '''bool KHTMLSettings.changeCursor()'''
        return bool()
    def init(self):
        '''void KHTMLSettings.init()'''
    def init(self, config, reset = True):
        '''void KHTMLSettings.init(KConfig config, bool reset = True)'''


class KHTMLView(QScrollArea):
    """"""
    # Enum KHTMLView.SmoothScrollingMode
    SSMDisabled = 0
    SSMWhenEfficient = 0
    SSMEnabled = 0

    def __init__(self, part, parent):
        '''void KHTMLView.__init__(KHTMLPart part, QWidget parent)'''
    def slotPaletteChanged(self):
        '''void KHTMLView.slotPaletteChanged()'''
    def setSmoothScrollingModeDefault(self, m):
        '''void KHTMLView.setSmoothScrollingModeDefault(KHTMLView.SmoothScrollingMode m)'''
    def timerEvent(self):
        '''QTimerEvent KHTMLView.timerEvent()'''
        return QTimerEvent()
    def doAutoScroll(self):
        '''void KHTMLView.doAutoScroll()'''
    def keyReleaseEvent(self, _ke):
        '''void KHTMLView.keyReleaseEvent(QKeyEvent _ke)'''
    def keyPressEvent(self, _ke):
        '''void KHTMLView.keyPressEvent(QKeyEvent _ke)'''
    def scrollContentsBy(self, dx, dy):
        '''void KHTMLView.scrollContentsBy(int dx, int dy)'''
    def eventFilter(self):
        '''QEvent KHTMLView.eventFilter()'''
        return QEvent()
    def viewportEvent(self, e):
        '''bool KHTMLView.viewportEvent(QEvent e)'''
        return bool()
    def widgetEvent(self):
        '''QEvent KHTMLView.widgetEvent()'''
        return QEvent()
    def closeEvent(self):
        '''QCloseEvent KHTMLView.closeEvent()'''
        return QCloseEvent()
    def dropEvent(self):
        '''QDropEvent KHTMLView.dropEvent()'''
        return QDropEvent()
    def dragEnterEvent(self):
        '''QDragEnterEvent KHTMLView.dragEnterEvent()'''
        return QDragEnterEvent()
    def wheelEvent(self):
        '''QWheelEvent KHTMLView.wheelEvent()'''
        return QWheelEvent()
    def mouseReleaseEvent(self):
        '''QMouseEvent KHTMLView.mouseReleaseEvent()'''
        return QMouseEvent()
    def mouseMoveEvent(self):
        '''QMouseEvent KHTMLView.mouseMoveEvent()'''
        return QMouseEvent()
    def mouseDoubleClickEvent(self):
        '''QMouseEvent KHTMLView.mouseDoubleClickEvent()'''
        return QMouseEvent()
    def focusOutEvent(self):
        '''QFocusEvent KHTMLView.focusOutEvent()'''
        return QFocusEvent()
    def focusInEvent(self):
        '''QFocusEvent KHTMLView.focusInEvent()'''
        return QFocusEvent()
    def mousePressEvent(self):
        '''QMouseEvent KHTMLView.mousePressEvent()'''
        return QMouseEvent()
    def focusNextPrevChild(self, next):
        '''bool KHTMLView.focusNextPrevChild(bool next)'''
        return bool()
    def hideEvent(self):
        '''QHideEvent KHTMLView.hideEvent()'''
        return QHideEvent()
    def showEvent(self):
        '''QShowEvent KHTMLView.showEvent()'''
        return QShowEvent()
    def resizeEvent(self, event):
        '''void KHTMLView.resizeEvent(QResizeEvent event)'''
    def paintEvent(self):
        '''QPaintEvent KHTMLView.paintEvent()'''
        return QPaintEvent()
    def event(self, event):
        '''bool KHTMLView.event(QEvent event)'''
        return bool()
    def clear(self):
        '''void KHTMLView.clear()'''
    findAheadActive = pyqtSignal() # void findAheadActive(bool) - signal
    repaintAccessKeys = pyqtSignal() # void repaintAccessKeys() - signal
    hideAccessKeys = pyqtSignal() # void hideAccessKeys() - signal
    zoomView = pyqtSignal() # void zoomView(int) - signal
    cleared = pyqtSignal() # void cleared() - signal
    finishedLayout = pyqtSignal() # void finishedLayout() - signal
    def layout(self):
        '''void KHTMLView.layout()'''
    def resizeContents(self, w, h):
        '''void KHTMLView.resizeContents(int w, int h)'''
    def smoothScrollingMode(self):
        '''KHTMLView.SmoothScrollingMode KHTMLView.smoothScrollingMode()'''
        return KHTMLView.SmoothScrollingMode()
    def setSmoothScrollingMode(self, m):
        '''void KHTMLView.setSmoothScrollingMode(KHTMLView.SmoothScrollingMode m)'''
    def zoomLevel(self):
        '''int KHTMLView.zoomLevel()'''
        return int()
    def setZoomLevel(self, percent):
        '''void KHTMLView.setZoomLevel(int percent)'''
    def repaintContents(self, r):
        '''void KHTMLView.repaintContents(QRect r)'''
    def repaintContents(self, x, y, w, h):
        '''void KHTMLView.repaintContents(int x, int y, int w, int h)'''
    def addChild(self, child, dx, dy):
        '''void KHTMLView.addChild(QWidget child, int dx, int dy)'''
    def updateContents(self, r):
        '''void KHTMLView.updateContents(QRect r)'''
    def updateContents(self, x, y, w, h):
        '''void KHTMLView.updateContents(int x, int y, int w, int h)'''
    def scrollBy(self, x, y):
        '''void KHTMLView.scrollBy(int x, int y)'''
    def viewportToContents(self, p):
        '''QPoint KHTMLView.viewportToContents(QPoint p)'''
        return QPoint()
    def viewportToContents(self, x, y, cx, cy):
        '''void KHTMLView.viewportToContents(int x, int y, int cx, int cy)'''
    def contentsToViewport(self, p):
        '''QPoint KHTMLView.contentsToViewport(QPoint p)'''
        return QPoint()
    def contentsToViewport(self, x, y, cx, cy):
        '''void KHTMLView.contentsToViewport(int x, int y, int cx, int cy)'''
    def setContentsPos(self, x, y):
        '''void KHTMLView.setContentsPos(int x, int y)'''
    def visibleHeight(self):
        '''int KHTMLView.visibleHeight()'''
        return int()
    def visibleWidth(self):
        '''int KHTMLView.visibleWidth()'''
        return int()
    def contentsY(self):
        '''int KHTMLView.contentsY()'''
        return int()
    def contentsX(self):
        '''int KHTMLView.contentsX()'''
        return int()
    def contentsHeight(self):
        '''int KHTMLView.contentsHeight()'''
        return int()
    def contentsWidth(self):
        '''int KHTMLView.contentsWidth()'''
        return int()
    def displayAccessKeys(self):
        '''void KHTMLView.displayAccessKeys()'''
    def print_(self, quick = False):
        '''void KHTMLView.print_(bool quick = False)'''
    def setHorizontalScrollBarPolicy(self, policy):
        '''void KHTMLView.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy policy)'''
    def setVerticalScrollBarPolicy(self, policy):
        '''void KHTMLView.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy policy)'''
    def marginHeight(self):
        '''int KHTMLView.marginHeight()'''
        return int()
    def setMarginHeight(self, y):
        '''void KHTMLView.setMarginHeight(int y)'''
    def marginWidth(self):
        '''int KHTMLView.marginWidth()'''
        return int()
    def setMarginWidth(self, x):
        '''void KHTMLView.setMarginWidth(int x)'''
    def frameWidth(self):
        '''int KHTMLView.frameWidth()'''
        return int()
    def part(self):
        '''KHTMLPart KHTMLView.part()'''
        return KHTMLPart()


