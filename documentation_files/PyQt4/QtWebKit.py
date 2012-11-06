class pyqtSignal():
 def connect(self, targetSignal): pass
 def emit(self, *args): pass
from QtCore import *

class QGraphicsWebView(QGraphicsWidget):
    """"""
    def __init__(self, parent = None):
        '''void QGraphicsWebView.__init__(QGraphicsItem parent = None)'''
    def setRenderHint(self, hint, enabled = True):
        '''void QGraphicsWebView.setRenderHint(QPainter.RenderHint hint, bool enabled = True)'''
    def setRenderHints(self, hints):
        '''void QGraphicsWebView.setRenderHints(QPainter.RenderHints hints)'''
    def renderHints(self):
        '''QPainter.RenderHints QGraphicsWebView.renderHints()'''
        return QPainter.RenderHints()
    def setTiledBackingStoreFrozen(self, frozen):
        '''void QGraphicsWebView.setTiledBackingStoreFrozen(bool frozen)'''
    def isTiledBackingStoreFrozen(self):
        '''bool QGraphicsWebView.isTiledBackingStoreFrozen()'''
        return bool()
    def setResizesToContents(self, enabled):
        '''void QGraphicsWebView.setResizesToContents(bool enabled)'''
    def resizesToContents(self):
        '''bool QGraphicsWebView.resizesToContents()'''
        return bool()
    def sceneEvent(self):
        '''QEvent QGraphicsWebView.sceneEvent()'''
        return QEvent()
    def focusNextPrevChild(self, next):
        '''bool QGraphicsWebView.focusNextPrevChild(bool next)'''
        return bool()
    def inputMethodEvent(self):
        '''QInputMethodEvent QGraphicsWebView.inputMethodEvent()'''
        return QInputMethodEvent()
    def focusOutEvent(self):
        '''QFocusEvent QGraphicsWebView.focusOutEvent()'''
        return QFocusEvent()
    def focusInEvent(self):
        '''QFocusEvent QGraphicsWebView.focusInEvent()'''
        return QFocusEvent()
    def dropEvent(self):
        '''QGraphicsSceneDragDropEvent QGraphicsWebView.dropEvent()'''
        return QGraphicsSceneDragDropEvent()
    def dragMoveEvent(self):
        '''QGraphicsSceneDragDropEvent QGraphicsWebView.dragMoveEvent()'''
        return QGraphicsSceneDragDropEvent()
    def dragLeaveEvent(self):
        '''QGraphicsSceneDragDropEvent QGraphicsWebView.dragLeaveEvent()'''
        return QGraphicsSceneDragDropEvent()
    def dragEnterEvent(self):
        '''QGraphicsSceneDragDropEvent QGraphicsWebView.dragEnterEvent()'''
        return QGraphicsSceneDragDropEvent()
    def contextMenuEvent(self):
        '''QGraphicsSceneContextMenuEvent QGraphicsWebView.contextMenuEvent()'''
        return QGraphicsSceneContextMenuEvent()
    def keyReleaseEvent(self):
        '''QKeyEvent QGraphicsWebView.keyReleaseEvent()'''
        return QKeyEvent()
    def keyPressEvent(self):
        '''QKeyEvent QGraphicsWebView.keyPressEvent()'''
        return QKeyEvent()
    def wheelEvent(self):
        '''QGraphicsSceneWheelEvent QGraphicsWebView.wheelEvent()'''
        return QGraphicsSceneWheelEvent()
    def hoverLeaveEvent(self):
        '''QGraphicsSceneHoverEvent QGraphicsWebView.hoverLeaveEvent()'''
        return QGraphicsSceneHoverEvent()
    def hoverMoveEvent(self):
        '''QGraphicsSceneHoverEvent QGraphicsWebView.hoverMoveEvent()'''
        return QGraphicsSceneHoverEvent()
    def mouseMoveEvent(self):
        '''QGraphicsSceneMouseEvent QGraphicsWebView.mouseMoveEvent()'''
        return QGraphicsSceneMouseEvent()
    def mouseReleaseEvent(self):
        '''QGraphicsSceneMouseEvent QGraphicsWebView.mouseReleaseEvent()'''
        return QGraphicsSceneMouseEvent()
    def mouseDoubleClickEvent(self):
        '''QGraphicsSceneMouseEvent QGraphicsWebView.mouseDoubleClickEvent()'''
        return QGraphicsSceneMouseEvent()
    def mousePressEvent(self):
        '''QGraphicsSceneMouseEvent QGraphicsWebView.mousePressEvent()'''
        return QGraphicsSceneMouseEvent()
    linkClicked = pyqtSignal() # void linkClicked(const QUrlamp;) - signal
    statusBarMessage = pyqtSignal() # void statusBarMessage(const QStringamp;) - signal
    iconChanged = pyqtSignal() # void iconChanged() - signal
    titleChanged = pyqtSignal() # void titleChanged(const QStringamp;) - signal
    urlChanged = pyqtSignal() # void urlChanged(const QUrlamp;) - signal
    loadProgress = pyqtSignal() # void loadProgress(int) - signal
    loadFinished = pyqtSignal() # void loadFinished(bool) - signal
    loadStarted = pyqtSignal() # void loadStarted() - signal
    def reload(self):
        '''void QGraphicsWebView.reload()'''
    def forward(self):
        '''void QGraphicsWebView.forward()'''
    def back(self):
        '''void QGraphicsWebView.back()'''
    def stop(self):
        '''void QGraphicsWebView.stop()'''
    def inputMethodQuery(self, query):
        '''QVariant QGraphicsWebView.inputMethodQuery(Qt.InputMethodQuery query)'''
        return QVariant()
    def sizeHint(self, which, constraint):
        '''QSizeF QGraphicsWebView.sizeHint(Qt.SizeHint which, QSizeF constraint)'''
        return QSizeF()
    def event(self):
        '''QEvent QGraphicsWebView.event()'''
        return QEvent()
    def itemChange(self, change, value):
        '''QVariant QGraphicsWebView.itemChange(QGraphicsItem.GraphicsItemChange change, QVariant value)'''
        return QVariant()
    def paint(self, painter, option, widget = None):
        '''void QGraphicsWebView.paint(QPainter painter, QStyleOptionGraphicsItem option, QWidget widget = None)'''
    def updateGeometry(self):
        '''void QGraphicsWebView.updateGeometry()'''
    def setGeometry(self, rect):
        '''void QGraphicsWebView.setGeometry(QRectF rect)'''
    def findText(self, subString, options = 0):
        '''bool QGraphicsWebView.findText(QString subString, QWebPage.FindFlags options = 0)'''
        return bool()
    def triggerPageAction(self, action, checked = False):
        '''void QGraphicsWebView.triggerPageAction(QWebPage.WebAction action, bool checked = False)'''
    def pageAction(self, action):
        '''QAction QGraphicsWebView.pageAction(QWebPage.WebAction action)'''
        return QAction()
    def settings(self):
        '''QWebSettings QGraphicsWebView.settings()'''
        return QWebSettings()
    def history(self):
        '''QWebHistory QGraphicsWebView.history()'''
        return QWebHistory()
    def setContent(self, data, mimeType = QString(), baseUrl = QUrl()):
        '''void QGraphicsWebView.setContent(QByteArray data, QString mimeType = QString(), QUrl baseUrl = QUrl())'''
    def setHtml(self, html, baseUrl = QUrl()):
        '''void QGraphicsWebView.setHtml(QString html, QUrl baseUrl = QUrl())'''
    def load(self, url):
        '''void QGraphicsWebView.load(QUrl url)'''
    def load(self, request, operation = None, body = QByteArray()):
        '''void QGraphicsWebView.load(QNetworkRequest request, QNetworkAccessManager.Operation operation = QNetworkAccessManager.GetOperation, QByteArray body = QByteArray())'''
    def isModified(self):
        '''bool QGraphicsWebView.isModified()'''
        return bool()
    def setZoomFactor(self):
        '''float QGraphicsWebView.setZoomFactor()'''
        return float()
    def zoomFactor(self):
        '''float QGraphicsWebView.zoomFactor()'''
        return float()
    def icon(self):
        '''QIcon QGraphicsWebView.icon()'''
        return QIcon()
    def title(self):
        '''QString QGraphicsWebView.title()'''
        return QString()
    def setUrl(self):
        '''QUrl QGraphicsWebView.setUrl()'''
        return QUrl()
    def url(self):
        '''QUrl QGraphicsWebView.url()'''
        return QUrl()
    def setPage(self):
        '''QWebPage QGraphicsWebView.setPage()'''
        return QWebPage()
    def page(self):
        '''QWebPage QGraphicsWebView.page()'''
        return QWebPage()


class QWebDatabase():
    """"""
    def __init__(self, other):
        '''void QWebDatabase.__init__(QWebDatabase other)'''
    def removeAllDatabases(self):
        '''static void QWebDatabase.removeAllDatabases()'''
    def removeDatabase(self, db):
        '''static void QWebDatabase.removeDatabase(QWebDatabase db)'''
    def origin(self):
        '''QWebSecurityOrigin QWebDatabase.origin()'''
        return QWebSecurityOrigin()
    def fileName(self):
        '''QString QWebDatabase.fileName()'''
        return QString()
    def size(self):
        '''int QWebDatabase.size()'''
        return int()
    def expectedSize(self):
        '''int QWebDatabase.expectedSize()'''
        return int()
    def displayName(self):
        '''QString QWebDatabase.displayName()'''
        return QString()
    def name(self):
        '''QString QWebDatabase.name()'''
        return QString()


class QWebElement():
    """"""
    # Enum QWebElement.StyleResolveStrategy
    InlineStyle = 0
    CascadedStyle = 0
    ComputedStyle = 0

    def __init__(self):
        '''void QWebElement.__init__()'''
    def __init__(self):
        '''QWebElement QWebElement.__init__()'''
        return QWebElement()
    def render(self, painter):
        '''void QWebElement.render(QPainter painter)'''
    def render(self, painter, clip):
        '''void QWebElement.render(QPainter painter, QRect clip)'''
    def setStyleProperty(self, name, value):
        '''void QWebElement.setStyleProperty(QString name, QString value)'''
    def styleProperty(self, name, strategy):
        '''QString QWebElement.styleProperty(QString name, QWebElement.StyleResolveStrategy strategy)'''
        return QString()
    def evaluateJavaScript(self, scriptSource):
        '''QVariant QWebElement.evaluateJavaScript(QString scriptSource)'''
        return QVariant()
    def removeAllChildren(self):
        '''void QWebElement.removeAllChildren()'''
    def removeFromDocument(self):
        '''void QWebElement.removeFromDocument()'''
    def takeFromDocument(self):
        '''QWebElement QWebElement.takeFromDocument()'''
        return QWebElement()
    def clone(self):
        '''QWebElement QWebElement.clone()'''
        return QWebElement()
    def replace(self, markup):
        '''void QWebElement.replace(QString markup)'''
    def replace(self, element):
        '''void QWebElement.replace(QWebElement element)'''
    def encloseWith(self, markup):
        '''void QWebElement.encloseWith(QString markup)'''
    def encloseWith(self, element):
        '''void QWebElement.encloseWith(QWebElement element)'''
    def encloseContentsWith(self, element):
        '''void QWebElement.encloseContentsWith(QWebElement element)'''
    def encloseContentsWith(self, markup):
        '''void QWebElement.encloseContentsWith(QString markup)'''
    def prependOutside(self, markup):
        '''void QWebElement.prependOutside(QString markup)'''
    def prependOutside(self, element):
        '''void QWebElement.prependOutside(QWebElement element)'''
    def appendOutside(self, markup):
        '''void QWebElement.appendOutside(QString markup)'''
    def appendOutside(self, element):
        '''void QWebElement.appendOutside(QWebElement element)'''
    def prependInside(self, markup):
        '''void QWebElement.prependInside(QString markup)'''
    def prependInside(self, element):
        '''void QWebElement.prependInside(QWebElement element)'''
    def appendInside(self, markup):
        '''void QWebElement.appendInside(QString markup)'''
    def appendInside(self, element):
        '''void QWebElement.appendInside(QWebElement element)'''
    def webFrame(self):
        '''QWebFrame QWebElement.webFrame()'''
        return QWebFrame()
    def document(self):
        '''QWebElement QWebElement.document()'''
        return QWebElement()
    def previousSibling(self):
        '''QWebElement QWebElement.previousSibling()'''
        return QWebElement()
    def nextSibling(self):
        '''QWebElement QWebElement.nextSibling()'''
        return QWebElement()
    def lastChild(self):
        '''QWebElement QWebElement.lastChild()'''
        return QWebElement()
    def firstChild(self):
        '''QWebElement QWebElement.firstChild()'''
        return QWebElement()
    def parent(self):
        '''QWebElement QWebElement.parent()'''
        return QWebElement()
    def namespaceUri(self):
        '''QString QWebElement.namespaceUri()'''
        return QString()
    def localName(self):
        '''QString QWebElement.localName()'''
        return QString()
    def prefix(self):
        '''QString QWebElement.prefix()'''
        return QString()
    def tagName(self):
        '''QString QWebElement.tagName()'''
        return QString()
    def geometry(self):
        '''QRect QWebElement.geometry()'''
        return QRect()
    def setFocus(self):
        '''void QWebElement.setFocus()'''
    def hasFocus(self):
        '''bool QWebElement.hasFocus()'''
        return bool()
    def toggleClass(self, name):
        '''void QWebElement.toggleClass(QString name)'''
    def removeClass(self, name):
        '''void QWebElement.removeClass(QString name)'''
    def addClass(self, name):
        '''void QWebElement.addClass(QString name)'''
    def hasClass(self, name):
        '''bool QWebElement.hasClass(QString name)'''
        return bool()
    def classes(self):
        '''QStringList QWebElement.classes()'''
        return QStringList()
    def attributeNames(self, namespaceUri = QString()):
        '''QStringList QWebElement.attributeNames(QString namespaceUri = QString())'''
        return QStringList()
    def hasAttributes(self):
        '''bool QWebElement.hasAttributes()'''
        return bool()
    def removeAttributeNS(self, namespaceUri, name):
        '''void QWebElement.removeAttributeNS(QString namespaceUri, QString name)'''
    def removeAttribute(self, name):
        '''void QWebElement.removeAttribute(QString name)'''
    def hasAttributeNS(self, namespaceUri, name):
        '''bool QWebElement.hasAttributeNS(QString namespaceUri, QString name)'''
        return bool()
    def hasAttribute(self, name):
        '''bool QWebElement.hasAttribute(QString name)'''
        return bool()
    def attributeNS(self, namespaceUri, name, defaultValue = QString()):
        '''QString QWebElement.attributeNS(QString namespaceUri, QString name, QString defaultValue = QString())'''
        return QString()
    def attribute(self, name, defaultValue = QString()):
        '''QString QWebElement.attribute(QString name, QString defaultValue = QString())'''
        return QString()
    def setAttributeNS(self, namespaceUri, name, value):
        '''void QWebElement.setAttributeNS(QString namespaceUri, QString name, QString value)'''
    def setAttribute(self, name, value):
        '''void QWebElement.setAttribute(QString name, QString value)'''
    def toInnerXml(self):
        '''QString QWebElement.toInnerXml()'''
        return QString()
    def setInnerXml(self, markup):
        '''void QWebElement.setInnerXml(QString markup)'''
    def toOuterXml(self):
        '''QString QWebElement.toOuterXml()'''
        return QString()
    def setOuterXml(self, markup):
        '''void QWebElement.setOuterXml(QString markup)'''
    def toPlainText(self):
        '''QString QWebElement.toPlainText()'''
        return QString()
    def setPlainText(self, text):
        '''void QWebElement.setPlainText(QString text)'''
    def findFirst(self, selectorQuery):
        '''QWebElement QWebElement.findFirst(QString selectorQuery)'''
        return QWebElement()
    def findAll(self, selectorQuery):
        '''QWebElementCollection QWebElement.findAll(QString selectorQuery)'''
        return QWebElementCollection()
    def isNull(self):
        '''bool QWebElement.isNull()'''
        return bool()
    def __ne__(self, o):
        '''bool QWebElement.__ne__(QWebElement o)'''
        return bool()
    def __eq__(self, o):
        '''bool QWebElement.__eq__(QWebElement o)'''
        return bool()


class QWebElementCollection():
    """"""
    def __init__(self):
        '''void QWebElementCollection.__init__()'''
    def __init__(self, contextElement, query):
        '''void QWebElementCollection.__init__(QWebElement contextElement, QString query)'''
    def __init__(self):
        '''QWebElementCollection QWebElementCollection.__init__()'''
        return QWebElementCollection()
    def toList(self):
        '''list-of-QWebElement QWebElementCollection.toList()'''
        return [QWebElement()]
    def last(self):
        '''QWebElement QWebElementCollection.last()'''
        return QWebElement()
    def first(self):
        '''QWebElement QWebElementCollection.first()'''
        return QWebElement()
    def __getitem__(self, i):
        '''QWebElement QWebElementCollection.__getitem__(int i)'''
        return QWebElement()
    def at(self, i):
        '''QWebElement QWebElementCollection.at(int i)'''
        return QWebElement()
    def __len__(self):
        '''None QWebElementCollection.__len__()'''
        return None()
    def count(self):
        '''int QWebElementCollection.count()'''
        return int()
    def append(self, collection):
        '''void QWebElementCollection.append(QWebElementCollection collection)'''
    def __iadd__(self, other):
        '''QWebElementCollection QWebElementCollection.__iadd__(QWebElementCollection other)'''
        return QWebElementCollection()
    def __add__(self, other):
        '''QWebElementCollection QWebElementCollection.__add__(QWebElementCollection other)'''
        return QWebElementCollection()


class QWebHitTestResult():
    """"""
    def __init__(self):
        '''void QWebHitTestResult.__init__()'''
    def __init__(self, other):
        '''void QWebHitTestResult.__init__(QWebHitTestResult other)'''
    def element(self):
        '''QWebElement QWebHitTestResult.element()'''
        return QWebElement()
    def linkElement(self):
        '''QWebElement QWebHitTestResult.linkElement()'''
        return QWebElement()
    def enclosingBlockElement(self):
        '''QWebElement QWebHitTestResult.enclosingBlockElement()'''
        return QWebElement()
    def boundingRect(self):
        '''QRect QWebHitTestResult.boundingRect()'''
        return QRect()
    def frame(self):
        '''QWebFrame QWebHitTestResult.frame()'''
        return QWebFrame()
    def isContentSelected(self):
        '''bool QWebHitTestResult.isContentSelected()'''
        return bool()
    def isContentEditable(self):
        '''bool QWebHitTestResult.isContentEditable()'''
        return bool()
    def pixmap(self):
        '''QPixmap QWebHitTestResult.pixmap()'''
        return QPixmap()
    def imageUrl(self):
        '''QUrl QWebHitTestResult.imageUrl()'''
        return QUrl()
    def alternateText(self):
        '''QString QWebHitTestResult.alternateText()'''
        return QString()
    def linkTargetFrame(self):
        '''QWebFrame QWebHitTestResult.linkTargetFrame()'''
        return QWebFrame()
    def linkTitle(self):
        '''QUrl QWebHitTestResult.linkTitle()'''
        return QUrl()
    def linkUrl(self):
        '''QUrl QWebHitTestResult.linkUrl()'''
        return QUrl()
    def linkText(self):
        '''QString QWebHitTestResult.linkText()'''
        return QString()
    def title(self):
        '''QString QWebHitTestResult.title()'''
        return QString()
    def pos(self):
        '''QPoint QWebHitTestResult.pos()'''
        return QPoint()
    def isNull(self):
        '''bool QWebHitTestResult.isNull()'''
        return bool()


class QWebFrame(QObject):
    """"""
    # Enum QWebFrame.RenderLayer
    ContentsLayer = 0
    ScrollBarLayer = 0
    PanIconLayer = 0
    AllLayers = 0

    pageChanged = pyqtSignal() # void pageChanged() - signal
    def scrollToAnchor(self, anchor):
        '''void QWebFrame.scrollToAnchor(QString anchor)'''
    loadFinished = pyqtSignal() # void loadFinished(bool) - signal
    loadStarted = pyqtSignal() # void loadStarted() - signal
    contentsSizeChanged = pyqtSignal() # void contentsSizeChanged(const QSizeamp;) - signal
    def findFirstElement(self, selectorQuery):
        '''QWebElement QWebFrame.findFirstElement(QString selectorQuery)'''
        return QWebElement()
    def findAllElements(self, selectorQuery):
        '''QWebElementCollection QWebFrame.findAllElements(QString selectorQuery)'''
        return QWebElementCollection()
    def documentElement(self):
        '''QWebElement QWebFrame.documentElement()'''
        return QWebElement()
    def setFocus(self):
        '''void QWebFrame.setFocus()'''
    def hasFocus(self):
        '''bool QWebFrame.hasFocus()'''
        return bool()
    def scrollBarGeometry(self, orientation):
        '''QRect QWebFrame.scrollBarGeometry(Qt.Orientation orientation)'''
        return QRect()
    def baseUrl(self):
        '''QUrl QWebFrame.baseUrl()'''
        return QUrl()
    def requestedUrl(self):
        '''QUrl QWebFrame.requestedUrl()'''
        return QUrl()
    def securityOrigin(self):
        '''QWebSecurityOrigin QWebFrame.securityOrigin()'''
        return QWebSecurityOrigin()
    def setZoomFactor(self, factor):
        '''void QWebFrame.setZoomFactor(float factor)'''
    def zoomFactor(self):
        '''float QWebFrame.zoomFactor()'''
        return float()
    def setScrollPosition(self, pos):
        '''void QWebFrame.setScrollPosition(QPoint pos)'''
    def scrollPosition(self):
        '''QPoint QWebFrame.scrollPosition()'''
        return QPoint()
    def scroll(self):
        '''int QWebFrame.scroll()'''
        return int()
    def metaData(self):
        '''dict-of-QString-list-of-QString QWebFrame.metaData()'''
        return dict-of-QString-list-of-QString()
    iconChanged = pyqtSignal() # void iconChanged() - signal
    initialLayoutCompleted = pyqtSignal() # void initialLayoutCompleted() - signal
    urlChanged = pyqtSignal() # void urlChanged(const QUrlamp;) - signal
    titleChanged = pyqtSignal() # void titleChanged(const QStringamp;) - signal
    javaScriptWindowObjectCleared = pyqtSignal() # void javaScriptWindowObjectCleared() - signal
    def print_(self, printer):
        '''void QWebFrame.print_(QPrinter printer)'''
    def evaluateJavaScript(self, scriptSource):
        '''QVariant QWebFrame.evaluateJavaScript(QString scriptSource)'''
        return QVariant()
    def event(self):
        '''QEvent QWebFrame.event()'''
        return QEvent()
    def hitTestContent(self, pos):
        '''QWebHitTestResult QWebFrame.hitTestContent(QPoint pos)'''
        return QWebHitTestResult()
    def contentsSize(self):
        '''QSize QWebFrame.contentsSize()'''
        return QSize()
    def geometry(self):
        '''QRect QWebFrame.geometry()'''
        return QRect()
    def pos(self):
        '''QPoint QWebFrame.pos()'''
        return QPoint()
    def textSizeMultiplier(self):
        '''float QWebFrame.textSizeMultiplier()'''
        return float()
    def setTextSizeMultiplier(self, factor):
        '''void QWebFrame.setTextSizeMultiplier(float factor)'''
    def render(self, painter, clip):
        '''void QWebFrame.render(QPainter painter, QRegion clip)'''
    def render(self, painter):
        '''void QWebFrame.render(QPainter painter)'''
    def render(self, layer, clip = QRegion()):
        '''QPainter QWebFrame.render(QWebFrame.RenderLayer layer, QRegion clip = QRegion())'''
        return QPainter()
    def scrollBarMaximum(self, orientation):
        '''int QWebFrame.scrollBarMaximum(Qt.Orientation orientation)'''
        return int()
    def scrollBarMinimum(self, orientation):
        '''int QWebFrame.scrollBarMinimum(Qt.Orientation orientation)'''
        return int()
    def scrollBarValue(self, orientation):
        '''int QWebFrame.scrollBarValue(Qt.Orientation orientation)'''
        return int()
    def setScrollBarValue(self, orientation, value):
        '''void QWebFrame.setScrollBarValue(Qt.Orientation orientation, int value)'''
    def setScrollBarPolicy(self, orientation, policy):
        '''void QWebFrame.setScrollBarPolicy(Qt.Orientation orientation, Qt.ScrollBarPolicy policy)'''
    def scrollBarPolicy(self, orientation):
        '''Qt.ScrollBarPolicy QWebFrame.scrollBarPolicy(Qt.Orientation orientation)'''
        return Qt.ScrollBarPolicy()
    def childFrames(self):
        '''list-of-QWebFrame QWebFrame.childFrames()'''
        return [QWebFrame()]
    def parentFrame(self):
        '''QWebFrame QWebFrame.parentFrame()'''
        return QWebFrame()
    def frameName(self):
        '''QString QWebFrame.frameName()'''
        return QString()
    def icon(self):
        '''QIcon QWebFrame.icon()'''
        return QIcon()
    def url(self):
        '''QUrl QWebFrame.url()'''
        return QUrl()
    def setUrl(self, url):
        '''void QWebFrame.setUrl(QUrl url)'''
    def title(self):
        '''QString QWebFrame.title()'''
        return QString()
    def renderTreeDump(self):
        '''QString QWebFrame.renderTreeDump()'''
        return QString()
    def toPlainText(self):
        '''QString QWebFrame.toPlainText()'''
        return QString()
    def toHtml(self):
        '''QString QWebFrame.toHtml()'''
        return QString()
    def addToJavaScriptWindowObject(self, name, object):
        '''void QWebFrame.addToJavaScriptWindowObject(QString name, QObject object)'''
    def setContent(self, data, mimeType = QString(), baseUrl = QUrl()):
        '''void QWebFrame.setContent(QByteArray data, QString mimeType = QString(), QUrl baseUrl = QUrl())'''
    def setHtml(self, html, baseUrl = QUrl()):
        '''void QWebFrame.setHtml(QString html, QUrl baseUrl = QUrl())'''
    def load(self, url):
        '''void QWebFrame.load(QUrl url)'''
    def load(self, request, operation = None, body = QByteArray()):
        '''void QWebFrame.load(QNetworkRequest request, QNetworkAccessManager.Operation operation = QNetworkAccessManager.GetOperation, QByteArray body = QByteArray())'''
    def page(self):
        '''QWebPage QWebFrame.page()'''
        return QWebPage()


class QWebHistoryItem():
    """"""
    def __init__(self, other):
        '''void QWebHistoryItem.__init__(QWebHistoryItem other)'''
    def isValid(self):
        '''bool QWebHistoryItem.isValid()'''
        return bool()
    def setUserData(self, userData):
        '''void QWebHistoryItem.setUserData(QVariant userData)'''
    def userData(self):
        '''QVariant QWebHistoryItem.userData()'''
        return QVariant()
    def icon(self):
        '''QIcon QWebHistoryItem.icon()'''
        return QIcon()
    def lastVisited(self):
        '''QDateTime QWebHistoryItem.lastVisited()'''
        return QDateTime()
    def title(self):
        '''QString QWebHistoryItem.title()'''
        return QString()
    def url(self):
        '''QUrl QWebHistoryItem.url()'''
        return QUrl()
    def originalUrl(self):
        '''QUrl QWebHistoryItem.originalUrl()'''
        return QUrl()


class QWebHistory():
    """"""
    def setMaximumItemCount(self, count):
        '''void QWebHistory.setMaximumItemCount(int count)'''
    def maximumItemCount(self):
        '''int QWebHistory.maximumItemCount()'''
        return int()
    def currentItemIndex(self):
        '''int QWebHistory.currentItemIndex()'''
        return int()
    def __len__(self):
        '''None QWebHistory.__len__()'''
        return None()
    def count(self):
        '''int QWebHistory.count()'''
        return int()
    def itemAt(self, i):
        '''QWebHistoryItem QWebHistory.itemAt(int i)'''
        return QWebHistoryItem()
    def forwardItem(self):
        '''QWebHistoryItem QWebHistory.forwardItem()'''
        return QWebHistoryItem()
    def currentItem(self):
        '''QWebHistoryItem QWebHistory.currentItem()'''
        return QWebHistoryItem()
    def backItem(self):
        '''QWebHistoryItem QWebHistory.backItem()'''
        return QWebHistoryItem()
    def goToItem(self, item):
        '''void QWebHistory.goToItem(QWebHistoryItem item)'''
    def forward(self):
        '''void QWebHistory.forward()'''
    def back(self):
        '''void QWebHistory.back()'''
    def canGoForward(self):
        '''bool QWebHistory.canGoForward()'''
        return bool()
    def canGoBack(self):
        '''bool QWebHistory.canGoBack()'''
        return bool()
    def forwardItems(self, maxItems):
        '''list-of-QWebHistoryItem QWebHistory.forwardItems(int maxItems)'''
        return [QWebHistoryItem()]
    def backItems(self, maxItems):
        '''list-of-QWebHistoryItem QWebHistory.backItems(int maxItems)'''
        return [QWebHistoryItem()]
    def items(self):
        '''list-of-QWebHistoryItem QWebHistory.items()'''
        return [QWebHistoryItem()]
    def clear(self):
        '''void QWebHistory.clear()'''


class QWebHistoryInterface(QObject):
    """"""
    def __init__(self, parent = None):
        '''void QWebHistoryInterface.__init__(QObject parent = None)'''
    def addHistoryEntry(self, url):
        '''abstract void QWebHistoryInterface.addHistoryEntry(QString url)'''
    def historyContains(self, url):
        '''abstract bool QWebHistoryInterface.historyContains(QString url)'''
        return bool()
    def defaultInterface(self):
        '''static QWebHistoryInterface QWebHistoryInterface.defaultInterface()'''
        return QWebHistoryInterface()
    def setDefaultInterface(self, defaultInterface):
        '''static void QWebHistoryInterface.setDefaultInterface(QWebHistoryInterface defaultInterface)'''


class QWebInspector(QWidget):
    """"""
    def __init__(self, parent = None):
        '''void QWebInspector.__init__(QWidget parent = None)'''
    def closeEvent(self, event):
        '''void QWebInspector.closeEvent(QCloseEvent event)'''
    def hideEvent(self, event):
        '''void QWebInspector.hideEvent(QHideEvent event)'''
    def showEvent(self, event):
        '''void QWebInspector.showEvent(QShowEvent event)'''
    def resizeEvent(self, event):
        '''void QWebInspector.resizeEvent(QResizeEvent event)'''
    def event(self):
        '''QEvent QWebInspector.event()'''
        return QEvent()
    def sizeHint(self):
        '''QSize QWebInspector.sizeHint()'''
        return QSize()
    def page(self):
        '''QWebPage QWebInspector.page()'''
        return QWebPage()
    def setPage(self, page):
        '''void QWebInspector.setPage(QWebPage page)'''


class QWebPage(QObject):
    """"""
    # Enum QWebPage.Feature
    Notifications = 0
    Geolocation = 0

    # Enum QWebPage.PermissionPolicy
    PermissionUnknown = 0
    PermissionGrantedByUser = 0
    PermissionDeniedByUser = 0

    # Enum QWebPage.ErrorDomain
    QtNetwork = 0
    Http = 0
    WebKit = 0

    # Enum QWebPage.Extension
    ChooseMultipleFilesExtension = 0
    ErrorPageExtension = 0

    # Enum QWebPage.WebWindowType
    WebBrowserWindow = 0
    WebModalDialog = 0

    # Enum QWebPage.LinkDelegationPolicy
    DontDelegateLinks = 0
    DelegateExternalLinks = 0
    DelegateAllLinks = 0

    # Enum QWebPage.FindFlag
    FindBackward = 0
    FindCaseSensitively = 0
    FindWrapsAroundDocument = 0
    HighlightAllOccurrences = 0

    # Enum QWebPage.WebAction
    NoWebAction = 0
    OpenLink = 0
    OpenLinkInNewWindow = 0
    OpenFrameInNewWindow = 0
    DownloadLinkToDisk = 0
    CopyLinkToClipboard = 0
    OpenImageInNewWindow = 0
    DownloadImageToDisk = 0
    CopyImageToClipboard = 0
    Back = 0
    Forward = 0
    Stop = 0
    Reload = 0
    Cut = 0
    Copy = 0
    Paste = 0
    Undo = 0
    Redo = 0
    MoveToNextChar = 0
    MoveToPreviousChar = 0
    MoveToNextWord = 0
    MoveToPreviousWord = 0
    MoveToNextLine = 0
    MoveToPreviousLine = 0
    MoveToStartOfLine = 0
    MoveToEndOfLine = 0
    MoveToStartOfBlock = 0
    MoveToEndOfBlock = 0
    MoveToStartOfDocument = 0
    MoveToEndOfDocument = 0
    SelectNextChar = 0
    SelectPreviousChar = 0
    SelectNextWord = 0
    SelectPreviousWord = 0
    SelectNextLine = 0
    SelectPreviousLine = 0
    SelectStartOfLine = 0
    SelectEndOfLine = 0
    SelectStartOfBlock = 0
    SelectEndOfBlock = 0
    SelectStartOfDocument = 0
    SelectEndOfDocument = 0
    DeleteStartOfWord = 0
    DeleteEndOfWord = 0
    SetTextDirectionDefault = 0
    SetTextDirectionLeftToRight = 0
    SetTextDirectionRightToLeft = 0
    ToggleBold = 0
    ToggleItalic = 0
    ToggleUnderline = 0
    InspectElement = 0
    InsertParagraphSeparator = 0
    InsertLineSeparator = 0
    SelectAll = 0
    ReloadAndBypassCache = 0
    PasteAndMatchStyle = 0
    RemoveFormat = 0
    ToggleStrikethrough = 0
    ToggleSubscript = 0
    ToggleSuperscript = 0
    InsertUnorderedList = 0
    InsertOrderedList = 0
    Indent = 0
    Outdent = 0
    AlignCenter = 0
    AlignJustified = 0
    AlignLeft = 0
    AlignRight = 0
    StopScheduledPageRefresh = 0
    CopyImageUrlToClipboard = 0

    # Enum QWebPage.NavigationType
    NavigationTypeLinkClicked = 0
    NavigationTypeFormSubmitted = 0
    NavigationTypeBackOrForward = 0
    NavigationTypeReload = 0
    NavigationTypeFormResubmitted = 0
    NavigationTypeOther = 0

    def __init__(self, parent = None):
        '''void QWebPage.__init__(QObject parent = None)'''
    featurePermissionRequestCanceled = pyqtSignal() # void featurePermissionRequestCanceled(QWebFrame *,QWebPage::Feature) - signal
    featurePermissionRequested = pyqtSignal() # void featurePermissionRequested(QWebFrame *,QWebPage::Feature) - signal
    viewportChangeRequested = pyqtSignal() # void viewportChangeRequested() - signal
    applicationCacheQuotaExceeded = pyqtSignal() # void applicationCacheQuotaExceeded(QWebSecurityOrigin *,quint64) - signal
    def supportsContentType(self, mimeType):
        '''bool QWebPage.supportsContentType(QString mimeType)'''
        return bool()
    def supportedContentTypes(self):
        '''QStringList QWebPage.supportedContentTypes()'''
        return QStringList()
    def setFeaturePermission(self, frame, feature, policy):
        '''void QWebPage.setFeaturePermission(QWebFrame frame, QWebPage.Feature feature, QWebPage.PermissionPolicy policy)'''
    def setActualVisibleContentRect(self, rect):
        '''void QWebPage.setActualVisibleContentRect(QRect rect)'''
    def viewportAttributesForSize(self, availableSize):
        '''QWebPage.ViewportAttributes QWebPage.viewportAttributesForSize(QSize availableSize)'''
        return QWebPage.ViewportAttributes()
    def selectedHtml(self):
        '''QString QWebPage.selectedHtml()'''
        return QString()
    def hasSelection(self):
        '''bool QWebPage.hasSelection()'''
        return bool()
    def shouldInterruptJavaScript(self):
        '''bool QWebPage.shouldInterruptJavaScript()'''
        return bool()
    def setPreferredContentsSize(self, size):
        '''void QWebPage.setPreferredContentsSize(QSize size)'''
    def preferredContentsSize(self):
        '''QSize QWebPage.preferredContentsSize()'''
        return QSize()
    def frameAt(self, pos):
        '''QWebFrame QWebPage.frameAt(QPoint pos)'''
        return QWebFrame()
    restoreFrameStateRequested = pyqtSignal() # void restoreFrameStateRequested(QWebFrame *) - signal
    saveFrameStateRequested = pyqtSignal() # void saveFrameStateRequested(QWebFrame *,QWebHistoryItem *) - signal
    databaseQuotaExceeded = pyqtSignal() # void databaseQuotaExceeded(QWebFrame *,QString) - signal
    contentsChanged = pyqtSignal() # void contentsChanged() - signal
    def createStandardContextMenu(self):
        '''QMenu QWebPage.createStandardContextMenu()'''
        return QMenu()
    def isContentEditable(self):
        '''bool QWebPage.isContentEditable()'''
        return bool()
    def setContentEditable(self, editable):
        '''void QWebPage.setContentEditable(bool editable)'''
    def userAgentForUrl(self, url):
        '''QString QWebPage.userAgentForUrl(QUrl url)'''
        return QString()
    def javaScriptConsoleMessage(self, message, lineNumber, sourceID):
        '''void QWebPage.javaScriptConsoleMessage(QString message, int lineNumber, QString sourceID)'''
    def javaScriptPrompt(self, originatingFrame, msg, defaultValue, result):
        '''bool QWebPage.javaScriptPrompt(QWebFrame originatingFrame, QString msg, QString defaultValue, QString result)'''
        return bool()
    def javaScriptPrompt(self, originatingFrame, msg, defaultValue, result):
        '''bool QWebPage.javaScriptPrompt(QWebFrame originatingFrame, QString msg, QString defaultValue, QString result)'''
        return bool()
    def javaScriptConfirm(self, originatingFrame, msg):
        '''bool QWebPage.javaScriptConfirm(QWebFrame originatingFrame, QString msg)'''
        return bool()
    def javaScriptAlert(self, originatingFrame, msg):
        '''void QWebPage.javaScriptAlert(QWebFrame originatingFrame, QString msg)'''
    def chooseFile(self, originatingFrame, oldFile):
        '''QString QWebPage.chooseFile(QWebFrame originatingFrame, QString oldFile)'''
        return QString()
    def acceptNavigationRequest(self, frame, request, type):
        '''bool QWebPage.acceptNavigationRequest(QWebFrame frame, QNetworkRequest request, QWebPage.NavigationType type)'''
        return bool()
    def createPlugin(self, classid, url, paramNames, paramValues):
        '''QObject QWebPage.createPlugin(QString classid, QUrl url, QStringList paramNames, QStringList paramValues)'''
        return QObject()
    def createWindow(self, type):
        '''QWebPage QWebPage.createWindow(QWebPage.WebWindowType type)'''
        return QWebPage()
    microFocusChanged = pyqtSignal() # void microFocusChanged() - signal
    downloadRequested = pyqtSignal() # void downloadRequested(const QNetworkRequestamp;) - signal
    unsupportedContent = pyqtSignal() # void unsupportedContent(QNetworkReply *) - signal
    menuBarVisibilityChangeRequested = pyqtSignal() # void menuBarVisibilityChangeRequested(bool) - signal
    statusBarVisibilityChangeRequested = pyqtSignal() # void statusBarVisibilityChangeRequested(bool) - signal
    toolBarVisibilityChangeRequested = pyqtSignal() # void toolBarVisibilityChangeRequested(bool) - signal
    linkClicked = pyqtSignal() # void linkClicked(const QUrlamp;) - signal
    printRequested = pyqtSignal() # void printRequested(QWebFrame *) - signal
    windowCloseRequested = pyqtSignal() # void windowCloseRequested() - signal
    scrollRequested = pyqtSignal() # void scrollRequested(int,int,const QRectamp;) - signal
    repaintRequested = pyqtSignal() # void repaintRequested(const QRectamp;) - signal
    geometryChangeRequested = pyqtSignal() # void geometryChangeRequested(const QRectamp;) - signal
    frameCreated = pyqtSignal() # void frameCreated(QWebFrame *) - signal
    selectionChanged = pyqtSignal() # void selectionChanged() - signal
    statusBarMessage = pyqtSignal() # void statusBarMessage(const QStringamp;) - signal
    linkHovered = pyqtSignal() # void linkHovered(const QStringamp;,const QStringamp;,const QStringamp;) - signal
    loadStarted = pyqtSignal() # void loadStarted() - signal
    loadProgress = pyqtSignal() # void loadProgress(int) - signal
    loadFinished = pyqtSignal() # void loadFinished(bool) - signal
    def supportsExtension(self, extension):
        '''bool QWebPage.supportsExtension(QWebPage.Extension extension)'''
        return bool()
    def extension(self, extension, option = None, output = None):
        '''bool QWebPage.extension(QWebPage.Extension extension, QWebPage.ExtensionOption option = None, QWebPage.ExtensionReturn output = None)'''
        return bool()
    def updatePositionDependentActions(self, pos):
        '''void QWebPage.updatePositionDependentActions(QPoint pos)'''
    def swallowContextMenuEvent(self, event):
        '''bool QWebPage.swallowContextMenuEvent(QContextMenuEvent event)'''
        return bool()
    def palette(self):
        '''QPalette QWebPage.palette()'''
        return QPalette()
    def setPalette(self, palette):
        '''void QWebPage.setPalette(QPalette palette)'''
    def linkDelegationPolicy(self):
        '''QWebPage.LinkDelegationPolicy QWebPage.linkDelegationPolicy()'''
        return QWebPage.LinkDelegationPolicy()
    def setLinkDelegationPolicy(self, policy):
        '''void QWebPage.setLinkDelegationPolicy(QWebPage.LinkDelegationPolicy policy)'''
    def forwardUnsupportedContent(self):
        '''bool QWebPage.forwardUnsupportedContent()'''
        return bool()
    def setForwardUnsupportedContent(self, forward):
        '''void QWebPage.setForwardUnsupportedContent(bool forward)'''
    def findText(self, subString, options = 0):
        '''bool QWebPage.findText(QString subString, QWebPage.FindFlags options = 0)'''
        return bool()
    def inputMethodQuery(self, property):
        '''QVariant QWebPage.inputMethodQuery(Qt.InputMethodQuery property)'''
        return QVariant()
    def focusNextPrevChild(self, next):
        '''bool QWebPage.focusNextPrevChild(bool next)'''
        return bool()
    def event(self):
        '''QEvent QWebPage.event()'''
        return QEvent()
    def setViewportSize(self, size):
        '''void QWebPage.setViewportSize(QSize size)'''
    def viewportSize(self):
        '''QSize QWebPage.viewportSize()'''
        return QSize()
    def triggerAction(self, action, checked = False):
        '''void QWebPage.triggerAction(QWebPage.WebAction action, bool checked = False)'''
    def action(self, action):
        '''QAction QWebPage.action(QWebPage.WebAction action)'''
        return QAction()
    def selectedText(self):
        '''QString QWebPage.selectedText()'''
        return QString()
    def bytesReceived(self):
        '''int QWebPage.bytesReceived()'''
        return int()
    def totalBytes(self):
        '''int QWebPage.totalBytes()'''
        return int()
    def pluginFactory(self):
        '''QWebPluginFactory QWebPage.pluginFactory()'''
        return QWebPluginFactory()
    def setPluginFactory(self, factory):
        '''void QWebPage.setPluginFactory(QWebPluginFactory factory)'''
    def networkAccessManager(self):
        '''QNetworkAccessManager QWebPage.networkAccessManager()'''
        return QNetworkAccessManager()
    def setNetworkAccessManager(self, manager):
        '''void QWebPage.setNetworkAccessManager(QNetworkAccessManager manager)'''
    def undoStack(self):
        '''QUndoStack QWebPage.undoStack()'''
        return QUndoStack()
    def isModified(self):
        '''bool QWebPage.isModified()'''
        return bool()
    def view(self):
        '''QWidget QWebPage.view()'''
        return QWidget()
    def setView(self, view):
        '''void QWebPage.setView(QWidget view)'''
    def settings(self):
        '''QWebSettings QWebPage.settings()'''
        return QWebSettings()
    def history(self):
        '''QWebHistory QWebPage.history()'''
        return QWebHistory()
    def currentFrame(self):
        '''QWebFrame QWebPage.currentFrame()'''
        return QWebFrame()
    def mainFrame(self):
        '''QWebFrame QWebPage.mainFrame()'''
        return QWebFrame()
    class ViewportAttributes():
        """"""
        def __init__(self):
            '''void QWebPage.ViewportAttributes.__init__()'''
        def __init__(self, other):
            '''void QWebPage.ViewportAttributes.__init__(QWebPage.ViewportAttributes other)'''
        def size(self):
            '''QSize QWebPage.ViewportAttributes.size()'''
            return QSize()
        def isValid(self):
            '''bool QWebPage.ViewportAttributes.isValid()'''
            return bool()
        def isUserScalable(self):
            '''bool QWebPage.ViewportAttributes.isUserScalable()'''
            return bool()
        def devicePixelRatio(self):
            '''float QWebPage.ViewportAttributes.devicePixelRatio()'''
            return float()
        def maximumScaleFactor(self):
            '''float QWebPage.ViewportAttributes.maximumScaleFactor()'''
            return float()
        def minimumScaleFactor(self):
            '''float QWebPage.ViewportAttributes.minimumScaleFactor()'''
            return float()
        def initialScaleFactor(self):
            '''float QWebPage.ViewportAttributes.initialScaleFactor()'''
            return float()
    class ChooseMultipleFilesExtensionOption(QWebPage.ExtensionOption):
        """"""
        parentFrame = None # QWebFrame - member
        suggestedFileNames = None # QStringList - member
        def __init__(self):
            '''void QWebPage.ChooseMultipleFilesExtensionOption.__init__()'''
        def __init__(self):
            '''QWebPage.ChooseMultipleFilesExtensionOption QWebPage.ChooseMultipleFilesExtensionOption.__init__()'''
            return QWebPage.ChooseMultipleFilesExtensionOption()
    class FindFlags():
        """"""
        def __init__(self):
            '''QWebPage.FindFlags QWebPage.FindFlags.__init__()'''
            return QWebPage.FindFlags()
        def __init__(self):
            '''int QWebPage.FindFlags.__init__()'''
            return int()
        def __init__(self):
            '''void QWebPage.FindFlags.__init__()'''
        def __bool__(self):
            '''int QWebPage.FindFlags.__bool__()'''
            return int()
        def __ne__(self, f):
            '''bool QWebPage.FindFlags.__ne__(QWebPage.FindFlags f)'''
            return bool()
        def __eq__(self, f):
            '''bool QWebPage.FindFlags.__eq__(QWebPage.FindFlags f)'''
            return bool()
        def __invert__(self):
            '''QWebPage.FindFlags QWebPage.FindFlags.__invert__()'''
            return QWebPage.FindFlags()
        def __and__(self, mask):
            '''QWebPage.FindFlags QWebPage.FindFlags.__and__(int mask)'''
            return QWebPage.FindFlags()
        def __xor__(self, f):
            '''QWebPage.FindFlags QWebPage.FindFlags.__xor__(QWebPage.FindFlags f)'''
            return QWebPage.FindFlags()
        def __xor__(self, f):
            '''QWebPage.FindFlags QWebPage.FindFlags.__xor__(int f)'''
            return QWebPage.FindFlags()
        def __or__(self, f):
            '''QWebPage.FindFlags QWebPage.FindFlags.__or__(QWebPage.FindFlags f)'''
            return QWebPage.FindFlags()
        def __or__(self, f):
            '''QWebPage.FindFlags QWebPage.FindFlags.__or__(int f)'''
            return QWebPage.FindFlags()
        def __int__(self):
            '''int QWebPage.FindFlags.__int__()'''
            return int()
        def __ixor__(self, f):
            '''QWebPage.FindFlags QWebPage.FindFlags.__ixor__(QWebPage.FindFlags f)'''
            return QWebPage.FindFlags()
        def __ior__(self, f):
            '''QWebPage.FindFlags QWebPage.FindFlags.__ior__(QWebPage.FindFlags f)'''
            return QWebPage.FindFlags()
        def __iand__(self, mask):
            '''QWebPage.FindFlags QWebPage.FindFlags.__iand__(int mask)'''
            return QWebPage.FindFlags()
    class ErrorPageExtensionOption(QWebPage.ExtensionOption):
        """"""
        domain = None # QWebPage.ErrorDomain - member
        error = None # int - member
        errorString = None # QString - member
        frame = None # QWebFrame - member
        url = None # QUrl - member
        def __init__(self):
            '''void QWebPage.ErrorPageExtensionOption.__init__()'''
        def __init__(self):
            '''QWebPage.ErrorPageExtensionOption QWebPage.ErrorPageExtensionOption.__init__()'''
            return QWebPage.ErrorPageExtensionOption()
    class ErrorPageExtensionReturn(QWebPage.ExtensionReturn):
        """"""
        baseUrl = None # QUrl - member
        content = None # QByteArray - member
        contentType = None # QString - member
        encoding = None # QString - member
        def __init__(self):
            '''void QWebPage.ErrorPageExtensionReturn.__init__()'''
        def __init__(self):
            '''QWebPage.ErrorPageExtensionReturn QWebPage.ErrorPageExtensionReturn.__init__()'''
            return QWebPage.ErrorPageExtensionReturn()
    class ExtensionOption():
        """"""
        def __init__(self):
            '''void QWebPage.ExtensionOption.__init__()'''
        def __init__(self):
            '''QWebPage.ExtensionOption QWebPage.ExtensionOption.__init__()'''
            return QWebPage.ExtensionOption()
    class ExtensionReturn():
        """"""
        def __init__(self):
            '''void QWebPage.ExtensionReturn.__init__()'''
        def __init__(self):
            '''QWebPage.ExtensionReturn QWebPage.ExtensionReturn.__init__()'''
            return QWebPage.ExtensionReturn()
    class ChooseMultipleFilesExtensionReturn(QWebPage.ExtensionReturn):
        """"""
        fileNames = None # QStringList - member
        def __init__(self):
            '''void QWebPage.ChooseMultipleFilesExtensionReturn.__init__()'''
        def __init__(self):
            '''QWebPage.ChooseMultipleFilesExtensionReturn QWebPage.ChooseMultipleFilesExtensionReturn.__init__()'''
            return QWebPage.ChooseMultipleFilesExtensionReturn()


class QWebPluginFactory(QObject):
    """"""
    # Enum QWebPluginFactory.Extension

    def __init__(self, parent = None):
        '''void QWebPluginFactory.__init__(QObject parent = None)'''
    def supportsExtension(self, extension):
        '''bool QWebPluginFactory.supportsExtension(QWebPluginFactory.Extension extension)'''
        return bool()
    def extension(self, extension, option = None, output = None):
        '''bool QWebPluginFactory.extension(QWebPluginFactory.Extension extension, QWebPluginFactory.ExtensionOption option = None, QWebPluginFactory.ExtensionReturn output = None)'''
        return bool()
    def create(self, mimeType, url, argumentNames, argumentValues):
        '''abstract QObject QWebPluginFactory.create(QString mimeType, QUrl url, QStringList argumentNames, QStringList argumentValues)'''
        return QObject()
    def refreshPlugins(self):
        '''void QWebPluginFactory.refreshPlugins()'''
    def plugins(self):
        '''abstract list-of-QWebPluginFactory.Plugin QWebPluginFactory.plugins()'''
        return [QWebPluginFactory.Plugin()]
    class ExtensionOption():
        """"""
        def __init__(self):
            '''void QWebPluginFactory.ExtensionOption.__init__()'''
        def __init__(self):
            '''QWebPluginFactory.ExtensionOption QWebPluginFactory.ExtensionOption.__init__()'''
            return QWebPluginFactory.ExtensionOption()
    class ExtensionReturn():
        """"""
        def __init__(self):
            '''void QWebPluginFactory.ExtensionReturn.__init__()'''
        def __init__(self):
            '''QWebPluginFactory.ExtensionReturn QWebPluginFactory.ExtensionReturn.__init__()'''
            return QWebPluginFactory.ExtensionReturn()
    class Plugin():
        """"""
        description = None # QString - member
        mimeTypes = None # list-of-QWebPluginFactory.MimeType - member
        name = None # QString - member
        def __init__(self):
            '''void QWebPluginFactory.Plugin.__init__()'''
        def __init__(self):
            '''QWebPluginFactory.Plugin QWebPluginFactory.Plugin.__init__()'''
            return QWebPluginFactory.Plugin()
    class MimeType():
        """"""
        description = None # QString - member
        fileExtensions = None # QStringList - member
        name = None # QString - member
        def __init__(self):
            '''void QWebPluginFactory.MimeType.__init__()'''
        def __init__(self):
            '''QWebPluginFactory.MimeType QWebPluginFactory.MimeType.__init__()'''
            return QWebPluginFactory.MimeType()
        def __ne__(self, other):
            '''bool QWebPluginFactory.MimeType.__ne__(QWebPluginFactory.MimeType other)'''
            return bool()
        def __eq__(self, other):
            '''bool QWebPluginFactory.MimeType.__eq__(QWebPluginFactory.MimeType other)'''
            return bool()


class QWebSecurityOrigin():
    """"""
    def __init__(self, other):
        '''void QWebSecurityOrigin.__init__(QWebSecurityOrigin other)'''
    def setApplicationCacheQuota(self, quota):
        '''void QWebSecurityOrigin.setApplicationCacheQuota(int quota)'''
    def localSchemes(self):
        '''static QStringList QWebSecurityOrigin.localSchemes()'''
        return QStringList()
    def removeLocalScheme(self, scheme):
        '''static void QWebSecurityOrigin.removeLocalScheme(QString scheme)'''
    def addLocalScheme(self, scheme):
        '''static void QWebSecurityOrigin.addLocalScheme(QString scheme)'''
    def databases(self):
        '''list-of-QWebDatabase QWebSecurityOrigin.databases()'''
        return [QWebDatabase()]
    def setDatabaseQuota(self, quota):
        '''void QWebSecurityOrigin.setDatabaseQuota(int quota)'''
    def databaseQuota(self):
        '''int QWebSecurityOrigin.databaseQuota()'''
        return int()
    def databaseUsage(self):
        '''int QWebSecurityOrigin.databaseUsage()'''
        return int()
    def port(self):
        '''int QWebSecurityOrigin.port()'''
        return int()
    def host(self):
        '''QString QWebSecurityOrigin.host()'''
        return QString()
    def scheme(self):
        '''QString QWebSecurityOrigin.scheme()'''
        return QString()
    def allOrigins(self):
        '''static list-of-QWebSecurityOrigin QWebSecurityOrigin.allOrigins()'''
        return [QWebSecurityOrigin()]


class QWebSettings():
    """"""
    # Enum QWebSettings.FontSize
    MinimumFontSize = 0
    MinimumLogicalFontSize = 0
    DefaultFontSize = 0
    DefaultFixedFontSize = 0

    # Enum QWebSettings.WebGraphic
    MissingImageGraphic = 0
    MissingPluginGraphic = 0
    DefaultFrameIconGraphic = 0
    TextAreaSizeGripCornerGraphic = 0
    InputSpeechButtonGraphic = 0
    SearchCancelButtonGraphic = 0
    SearchCancelButtonPressedGraphic = 0

    # Enum QWebSettings.WebAttribute
    AutoLoadImages = 0
    JavascriptEnabled = 0
    JavaEnabled = 0
    PluginsEnabled = 0
    PrivateBrowsingEnabled = 0
    JavascriptCanOpenWindows = 0
    JavascriptCanCloseWindows = 0
    JavascriptCanAccessClipboard = 0
    DeveloperExtrasEnabled = 0
    LinksIncludedInFocusChain = 0
    ZoomTextOnly = 0
    PrintElementBackgrounds = 0
    OfflineStorageDatabaseEnabled = 0
    OfflineWebApplicationCacheEnabled = 0
    LocalStorageDatabaseEnabled = 0
    LocalStorageEnabled = 0
    LocalContentCanAccessRemoteUrls = 0
    DnsPrefetchEnabled = 0
    XSSAuditingEnabled = 0
    AcceleratedCompositingEnabled = 0
    SpatialNavigationEnabled = 0
    LocalContentCanAccessFileUrls = 0
    TiledBackingStoreEnabled = 0
    FrameFlatteningEnabled = 0
    SiteSpecificQuirksEnabled = 0
    WebGLEnabled = 0
    HyperlinkAuditingEnabled = 0

    # Enum QWebSettings.FontFamily
    StandardFont = 0
    FixedFont = 0
    SerifFont = 0
    SansSerifFont = 0
    CursiveFont = 0
    FantasyFont = 0

    def enablePersistentStorage(self, path = QString()):
        '''static void QWebSettings.enablePersistentStorage(QString path = QString())'''
    def clearMemoryCaches(self):
        '''static void QWebSettings.clearMemoryCaches()'''
    def localStoragePath(self):
        '''QString QWebSettings.localStoragePath()'''
        return QString()
    def setLocalStoragePath(self, path):
        '''void QWebSettings.setLocalStoragePath(QString path)'''
    def offlineWebApplicationCacheQuota(self):
        '''static int QWebSettings.offlineWebApplicationCacheQuota()'''
        return int()
    def setOfflineWebApplicationCacheQuota(self, maximumSize):
        '''static void QWebSettings.setOfflineWebApplicationCacheQuota(int maximumSize)'''
    def offlineWebApplicationCachePath(self):
        '''static QString QWebSettings.offlineWebApplicationCachePath()'''
        return QString()
    def setOfflineWebApplicationCachePath(self, path):
        '''static void QWebSettings.setOfflineWebApplicationCachePath(QString path)'''
    def defaultTextEncoding(self):
        '''QString QWebSettings.defaultTextEncoding()'''
        return QString()
    def setDefaultTextEncoding(self, encoding):
        '''void QWebSettings.setDefaultTextEncoding(QString encoding)'''
    def offlineStorageDefaultQuota(self):
        '''static int QWebSettings.offlineStorageDefaultQuota()'''
        return int()
    def setOfflineStorageDefaultQuota(self, maximumSize):
        '''static void QWebSettings.setOfflineStorageDefaultQuota(int maximumSize)'''
    def offlineStoragePath(self):
        '''static QString QWebSettings.offlineStoragePath()'''
        return QString()
    def setOfflineStoragePath(self, path):
        '''static void QWebSettings.setOfflineStoragePath(QString path)'''
    def setObjectCacheCapacities(self, cacheMinDeadCapacity, cacheMaxDead, totalCapacity):
        '''static void QWebSettings.setObjectCacheCapacities(int cacheMinDeadCapacity, int cacheMaxDead, int totalCapacity)'''
    def maximumPagesInCache(self):
        '''static int QWebSettings.maximumPagesInCache()'''
        return int()
    def setMaximumPagesInCache(self, pages):
        '''static void QWebSettings.setMaximumPagesInCache(int pages)'''
    def webGraphic(self, type):
        '''static QPixmap QWebSettings.webGraphic(QWebSettings.WebGraphic type)'''
        return QPixmap()
    def setWebGraphic(self, type, graphic):
        '''static void QWebSettings.setWebGraphic(QWebSettings.WebGraphic type, QPixmap graphic)'''
    def iconForUrl(self, url):
        '''static QIcon QWebSettings.iconForUrl(QUrl url)'''
        return QIcon()
    def clearIconDatabase(self):
        '''static void QWebSettings.clearIconDatabase()'''
    def iconDatabasePath(self):
        '''static QString QWebSettings.iconDatabasePath()'''
        return QString()
    def setIconDatabasePath(self, location):
        '''static void QWebSettings.setIconDatabasePath(QString location)'''
    def userStyleSheetUrl(self):
        '''QUrl QWebSettings.userStyleSheetUrl()'''
        return QUrl()
    def setUserStyleSheetUrl(self, location):
        '''void QWebSettings.setUserStyleSheetUrl(QUrl location)'''
    def resetAttribute(self, attr):
        '''void QWebSettings.resetAttribute(QWebSettings.WebAttribute attr)'''
    def testAttribute(self, attr):
        '''bool QWebSettings.testAttribute(QWebSettings.WebAttribute attr)'''
        return bool()
    def setAttribute(self, attr, on):
        '''void QWebSettings.setAttribute(QWebSettings.WebAttribute attr, bool on)'''
    def resetFontSize(self, type):
        '''void QWebSettings.resetFontSize(QWebSettings.FontSize type)'''
    def fontSize(self, type):
        '''int QWebSettings.fontSize(QWebSettings.FontSize type)'''
        return int()
    def setFontSize(self, type, size):
        '''void QWebSettings.setFontSize(QWebSettings.FontSize type, int size)'''
    def resetFontFamily(self, which):
        '''void QWebSettings.resetFontFamily(QWebSettings.FontFamily which)'''
    def fontFamily(self, which):
        '''QString QWebSettings.fontFamily(QWebSettings.FontFamily which)'''
        return QString()
    def setFontFamily(self, which, family):
        '''void QWebSettings.setFontFamily(QWebSettings.FontFamily which, QString family)'''
    def globalSettings(self):
        '''static QWebSettings QWebSettings.globalSettings()'''
        return QWebSettings()


class QWebView(QWidget):
    """"""
    def __init__(self, parent = None):
        '''void QWebView.__init__(QWidget parent = None)'''
    def selectedHtml(self):
        '''QString QWebView.selectedHtml()'''
        return QString()
    def hasSelection(self):
        '''bool QWebView.hasSelection()'''
        return bool()
    def setRenderHint(self, hint, enabled = True):
        '''void QWebView.setRenderHint(QPainter.RenderHint hint, bool enabled = True)'''
    def setRenderHints(self, hints):
        '''void QWebView.setRenderHints(QPainter.RenderHints hints)'''
    def renderHints(self):
        '''QPainter.RenderHints QWebView.renderHints()'''
        return QPainter.RenderHints()
    def setZoomFactor(self, factor):
        '''void QWebView.setZoomFactor(float factor)'''
    def zoomFactor(self):
        '''float QWebView.zoomFactor()'''
        return float()
    def focusNextPrevChild(self, next):
        '''bool QWebView.focusNextPrevChild(bool next)'''
        return bool()
    def inputMethodEvent(self):
        '''QInputMethodEvent QWebView.inputMethodEvent()'''
        return QInputMethodEvent()
    def focusOutEvent(self):
        '''QFocusEvent QWebView.focusOutEvent()'''
        return QFocusEvent()
    def focusInEvent(self):
        '''QFocusEvent QWebView.focusInEvent()'''
        return QFocusEvent()
    def dropEvent(self):
        '''QDropEvent QWebView.dropEvent()'''
        return QDropEvent()
    def dragMoveEvent(self):
        '''QDragMoveEvent QWebView.dragMoveEvent()'''
        return QDragMoveEvent()
    def dragLeaveEvent(self):
        '''QDragLeaveEvent QWebView.dragLeaveEvent()'''
        return QDragLeaveEvent()
    def dragEnterEvent(self):
        '''QDragEnterEvent QWebView.dragEnterEvent()'''
        return QDragEnterEvent()
    def keyReleaseEvent(self):
        '''QKeyEvent QWebView.keyReleaseEvent()'''
        return QKeyEvent()
    def keyPressEvent(self):
        '''QKeyEvent QWebView.keyPressEvent()'''
        return QKeyEvent()
    def wheelEvent(self):
        '''QWheelEvent QWebView.wheelEvent()'''
        return QWheelEvent()
    def contextMenuEvent(self):
        '''QContextMenuEvent QWebView.contextMenuEvent()'''
        return QContextMenuEvent()
    def mouseReleaseEvent(self):
        '''QMouseEvent QWebView.mouseReleaseEvent()'''
        return QMouseEvent()
    def mouseDoubleClickEvent(self):
        '''QMouseEvent QWebView.mouseDoubleClickEvent()'''
        return QMouseEvent()
    def mousePressEvent(self):
        '''QMouseEvent QWebView.mousePressEvent()'''
        return QMouseEvent()
    def mouseMoveEvent(self):
        '''QMouseEvent QWebView.mouseMoveEvent()'''
        return QMouseEvent()
    def changeEvent(self):
        '''QEvent QWebView.changeEvent()'''
        return QEvent()
    def paintEvent(self, ev):
        '''void QWebView.paintEvent(QPaintEvent ev)'''
    def resizeEvent(self, e):
        '''void QWebView.resizeEvent(QResizeEvent e)'''
    def createWindow(self, type):
        '''QWebView QWebView.createWindow(QWebPage.WebWindowType type)'''
        return QWebView()
    urlChanged = pyqtSignal() # void urlChanged(const QUrlamp;) - signal
    iconChanged = pyqtSignal() # void iconChanged() - signal
    selectionChanged = pyqtSignal() # void selectionChanged() - signal
    linkClicked = pyqtSignal() # void linkClicked(const QUrlamp;) - signal
    statusBarMessage = pyqtSignal() # void statusBarMessage(const QStringamp;) - signal
    titleChanged = pyqtSignal() # void titleChanged(const QStringamp;) - signal
    loadFinished = pyqtSignal() # void loadFinished(bool) - signal
    loadProgress = pyqtSignal() # void loadProgress(int) - signal
    loadStarted = pyqtSignal() # void loadStarted() - signal
    def print_(self, printer):
        '''void QWebView.print_(QPrinter printer)'''
    def reload(self):
        '''void QWebView.reload()'''
    def forward(self):
        '''void QWebView.forward()'''
    def back(self):
        '''void QWebView.back()'''
    def stop(self):
        '''void QWebView.stop()'''
    def event(self):
        '''QEvent QWebView.event()'''
        return QEvent()
    def findText(self, subString, options = 0):
        '''bool QWebView.findText(QString subString, QWebPage.FindFlags options = 0)'''
        return bool()
    def textSizeMultiplier(self):
        '''float QWebView.textSizeMultiplier()'''
        return float()
    def setTextSizeMultiplier(self, factor):
        '''void QWebView.setTextSizeMultiplier(float factor)'''
    def sizeHint(self):
        '''QSize QWebView.sizeHint()'''
        return QSize()
    def inputMethodQuery(self, property):
        '''QVariant QWebView.inputMethodQuery(Qt.InputMethodQuery property)'''
        return QVariant()
    def isModified(self):
        '''bool QWebView.isModified()'''
        return bool()
    def triggerPageAction(self, action, checked = False):
        '''void QWebView.triggerPageAction(QWebPage.WebAction action, bool checked = False)'''
    def pageAction(self, action):
        '''QAction QWebView.pageAction(QWebPage.WebAction action)'''
        return QAction()
    def selectedText(self):
        '''QString QWebView.selectedText()'''
        return QString()
    def icon(self):
        '''QIcon QWebView.icon()'''
        return QIcon()
    def url(self):
        '''QUrl QWebView.url()'''
        return QUrl()
    def setUrl(self, url):
        '''void QWebView.setUrl(QUrl url)'''
    def title(self):
        '''QString QWebView.title()'''
        return QString()
    def settings(self):
        '''QWebSettings QWebView.settings()'''
        return QWebSettings()
    def history(self):
        '''QWebHistory QWebView.history()'''
        return QWebHistory()
    def setContent(self, data, mimeType = QString(), baseUrl = QUrl()):
        '''void QWebView.setContent(QByteArray data, QString mimeType = QString(), QUrl baseUrl = QUrl())'''
    def setHtml(self, html, baseUrl = QUrl()):
        '''void QWebView.setHtml(QString html, QUrl baseUrl = QUrl())'''
    def load(self, url):
        '''void QWebView.load(QUrl url)'''
    def load(self, request, operation = None, body = QByteArray()):
        '''void QWebView.load(QNetworkRequest request, QNetworkAccessManager.Operation operation = QNetworkAccessManager.GetOperation, QByteArray body = QByteArray())'''
    def setPage(self, page):
        '''void QWebView.setPage(QWebPage page)'''
    def page(self):
        '''QWebPage QWebView.page()'''
        return QWebPage()


def qWebKitMinorVersion():
    '''static int qWebKitMinorVersion()'''
    return int()

def qWebKitMajorVersion():
    '''static int qWebKitMajorVersion()'''
    return int()

def qWebKitVersion():
    '''static QString qWebKitVersion()'''
    return QString()

