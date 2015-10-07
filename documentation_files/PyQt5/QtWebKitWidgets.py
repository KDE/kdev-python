class pyqtSignal():
 def connect(self, targetSignal): pass
 def emit(self, *args): pass
from QtCore import *

from QtWidgets import *

import datetime

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
        '''bool QGraphicsWebView.findText(str subString, QWebPage.FindFlags options = 0)'''
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
    def setContent(self, data, mimeType = str(), baseUrl = QUrl()):
        '''void QGraphicsWebView.setContent(QByteArray data, str mimeType = str(), QUrl baseUrl = QUrl())'''
    def setHtml(self, html, baseUrl = QUrl()):
        '''void QGraphicsWebView.setHtml(str html, QUrl baseUrl = QUrl())'''
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
        '''str QGraphicsWebView.title()'''
        return str()
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


class QWebHitTestResult():
    """"""
    def __init__(self):
        '''void QWebHitTestResult.__init__()'''
    def __init__(self, other):
        '''void QWebHitTestResult.__init__(QWebHitTestResult other)'''
    def linkTitleString(self):
        '''str QWebHitTestResult.linkTitleString()'''
        return str()
    def mediaUrl(self):
        '''QUrl QWebHitTestResult.mediaUrl()'''
        return QUrl()
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
        '''str QWebHitTestResult.alternateText()'''
        return str()
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
        '''str QWebHitTestResult.linkText()'''
        return str()
    def title(self):
        '''str QWebHitTestResult.title()'''
        return str()
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

    # Enum QWebFrame.ValueOwnership
    QtOwnership = 0
    ScriptOwnership = 0
    AutoOwnership = 0

    def scrollToAnchor(self, anchor):
        '''void QWebFrame.scrollToAnchor(str anchor)'''
    pageChanged = pyqtSignal() # void pageChanged() - signal
    loadFinished = pyqtSignal() # void loadFinished(bool) - signal
    loadStarted = pyqtSignal() # void loadStarted() - signal
    contentsSizeChanged = pyqtSignal() # void contentsSizeChanged(const QSizeamp;) - signal
    def findFirstElement(self, selectorQuery):
        '''QWebElement QWebFrame.findFirstElement(str selectorQuery)'''
        return QWebElement()
    def findAllElements(self, selectorQuery):
        '''QWebElementCollection QWebFrame.findAllElements(str selectorQuery)'''
        return QWebElementCollection()
    def documentElement(self):
        '''QWebElement QWebFrame.documentElement()'''
        return QWebElement()
    def setFocus(self):
        '''void QWebFrame.setFocus()'''
    def hasFocus(self):
        '''bool QWebFrame.hasFocus()'''
        return bool()
    def render(self, clip = QRegion()):
        '''QPainter QWebFrame.render(QRegion clip = QRegion())'''
        return QPainter()
    def render(self, layer, clip = QRegion()):
        '''QPainter QWebFrame.render(QWebFrame.RenderLayers layer, QRegion clip = QRegion())'''
        return QPainter()
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
        return {str():list()}
    iconChanged = pyqtSignal() # void iconChanged() - signal
    initialLayoutCompleted = pyqtSignal() # void initialLayoutCompleted() - signal
    urlChanged = pyqtSignal() # void urlChanged(const QUrlamp;) - signal
    titleChanged = pyqtSignal() # void titleChanged(const QStringamp;) - signal
    javaScriptWindowObjectCleared = pyqtSignal() # void javaScriptWindowObjectCleared() - signal
    def print_(self, printer):
        '''void QWebFrame.print_(QPrinter printer)'''
    def evaluateJavaScript(self, scriptSource):
        '''QVariant QWebFrame.evaluateJavaScript(str scriptSource)'''
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
        '''str QWebFrame.frameName()'''
        return str()
    def icon(self):
        '''QIcon QWebFrame.icon()'''
        return QIcon()
    def url(self):
        '''QUrl QWebFrame.url()'''
        return QUrl()
    def setUrl(self, url):
        '''void QWebFrame.setUrl(QUrl url)'''
    def title(self):
        '''str QWebFrame.title()'''
        return str()
    def toPlainText(self):
        '''str QWebFrame.toPlainText()'''
        return str()
    def toHtml(self):
        '''str QWebFrame.toHtml()'''
        return str()
    def addToJavaScriptWindowObject(self, name, object, ownership = None):
        '''void QWebFrame.addToJavaScriptWindowObject(str name, QObject object, QWebFrame.ValueOwnership ownership = QWebFrame.QtOwnership)'''
    def setContent(self, data, mimeType = None, baseUrl = QUrl()):
        '''void QWebFrame.setContent(QByteArray data, str mimeType = '', QUrl baseUrl = QUrl())'''
    def setHtml(self, html, baseUrl = QUrl()):
        '''void QWebFrame.setHtml(str html, QUrl baseUrl = QUrl())'''
    def load(self, url):
        '''void QWebFrame.load(QUrl url)'''
    def load(self, request, operation = None, body = QByteArray()):
        '''void QWebFrame.load(QNetworkRequest request, QNetworkAccessManager.Operation operation = QNetworkAccessManager.GetOperation, QByteArray body = QByteArray())'''
    def page(self):
        '''QWebPage QWebFrame.page()'''
        return QWebPage()
    class RenderLayers():
        """"""
        def __init__(self):
            '''QWebFrame.RenderLayers QWebFrame.RenderLayers.__init__()'''
            return QWebFrame.RenderLayers()
        def __init__(self):
            '''int QWebFrame.RenderLayers.__init__()'''
            return int()
        def __init__(self):
            '''void QWebFrame.RenderLayers.__init__()'''
        def __bool__(self):
            '''int QWebFrame.RenderLayers.__bool__()'''
            return int()
        def __ne__(self, f):
            '''bool QWebFrame.RenderLayers.__ne__(QWebFrame.RenderLayers f)'''
            return bool()
        def __eq__(self, f):
            '''bool QWebFrame.RenderLayers.__eq__(QWebFrame.RenderLayers f)'''
            return bool()
        def __invert__(self):
            '''QWebFrame.RenderLayers QWebFrame.RenderLayers.__invert__()'''
            return QWebFrame.RenderLayers()
        def __and__(self, mask):
            '''QWebFrame.RenderLayers QWebFrame.RenderLayers.__and__(int mask)'''
            return QWebFrame.RenderLayers()
        def __xor__(self, f):
            '''QWebFrame.RenderLayers QWebFrame.RenderLayers.__xor__(QWebFrame.RenderLayers f)'''
            return QWebFrame.RenderLayers()
        def __xor__(self, f):
            '''QWebFrame.RenderLayers QWebFrame.RenderLayers.__xor__(int f)'''
            return QWebFrame.RenderLayers()
        def __or__(self, f):
            '''QWebFrame.RenderLayers QWebFrame.RenderLayers.__or__(QWebFrame.RenderLayers f)'''
            return QWebFrame.RenderLayers()
        def __or__(self, f):
            '''QWebFrame.RenderLayers QWebFrame.RenderLayers.__or__(int f)'''
            return QWebFrame.RenderLayers()
        def __int__(self):
            '''int QWebFrame.RenderLayers.__int__()'''
            return int()
        def __ixor__(self, f):
            '''QWebFrame.RenderLayers QWebFrame.RenderLayers.__ixor__(QWebFrame.RenderLayers f)'''
            return QWebFrame.RenderLayers()
        def __ior__(self, f):
            '''QWebFrame.RenderLayers QWebFrame.RenderLayers.__ior__(QWebFrame.RenderLayers f)'''
            return QWebFrame.RenderLayers()
        def __iand__(self, mask):
            '''QWebFrame.RenderLayers QWebFrame.RenderLayers.__iand__(int mask)'''
            return QWebFrame.RenderLayers()


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
    # Enum QWebPage.VisibilityState
    VisibilityStateVisible = 0
    VisibilityStateHidden = 0
    VisibilityStatePrerender = 0
    VisibilityStateUnloaded = 0

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
    FindAtWordBeginningsOnly = 0
    TreatMedialCapitalAsWordBeginning = 0
    FindBeginsInSelection = 0

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
    OpenLinkInThisWindow = 0
    DownloadMediaToDisk = 0
    CopyMediaUrlToClipboard = 0
    ToggleMediaControls = 0
    ToggleMediaLoop = 0
    ToggleMediaPlayPause = 0
    ToggleMediaMute = 0
    ToggleVideoFullscreen = 0

    # Enum QWebPage.NavigationType
    NavigationTypeLinkClicked = 0
    NavigationTypeFormSubmitted = 0
    NavigationTypeBackOrForward = 0
    NavigationTypeReload = 0
    NavigationTypeFormResubmitted = 0
    NavigationTypeOther = 0

    def __init__(self, parent = None):
        '''void QWebPage.__init__(QObject parent = None)'''
    def setVisibilityState(self):
        '''QWebPage.VisibilityState QWebPage.setVisibilityState()'''
        return QWebPage.VisibilityState()
    def visibilityState(self):
        '''QWebPage.VisibilityState QWebPage.visibilityState()'''
        return QWebPage.VisibilityState()
    featurePermissionRequestCanceled = pyqtSignal() # void featurePermissionRequestCanceled(QWebFrame*,QWebPage::Feature) - signal
    featurePermissionRequested = pyqtSignal() # void featurePermissionRequested(QWebFrame*,QWebPage::Feature) - signal
    viewportChangeRequested = pyqtSignal() # void viewportChangeRequested() - signal
    applicationCacheQuotaExceeded = pyqtSignal() # void applicationCacheQuotaExceeded(QWebSecurityOrigin*,quint64,quint64) - signal
    def supportsContentType(self, mimeType):
        '''bool QWebPage.supportsContentType(str mimeType)'''
        return bool()
    def supportedContentTypes(self):
        '''list-of-str QWebPage.supportedContentTypes()'''
        return [str()]
    def setFeaturePermission(self, frame, feature, policy):
        '''void QWebPage.setFeaturePermission(QWebFrame frame, QWebPage.Feature feature, QWebPage.PermissionPolicy policy)'''
    def setActualVisibleContentRect(self, rect):
        '''void QWebPage.setActualVisibleContentRect(QRect rect)'''
    def viewportAttributesForSize(self, availableSize):
        '''QWebPage.ViewportAttributes QWebPage.viewportAttributesForSize(QSize availableSize)'''
        return QWebPage.ViewportAttributes()
    def selectedHtml(self):
        '''str QWebPage.selectedHtml()'''
        return str()
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
    restoreFrameStateRequested = pyqtSignal() # void restoreFrameStateRequested(QWebFrame*) - signal
    saveFrameStateRequested = pyqtSignal() # void saveFrameStateRequested(QWebFrame*,QWebHistoryItem*) - signal
    databaseQuotaExceeded = pyqtSignal() # void databaseQuotaExceeded(QWebFrame*,QString) - signal
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
        '''str QWebPage.userAgentForUrl(QUrl url)'''
        return str()
    def javaScriptConsoleMessage(self, message, lineNumber, sourceID):
        '''void QWebPage.javaScriptConsoleMessage(str message, int lineNumber, str sourceID)'''
    def javaScriptPrompt(self, originatingFrame, msg, defaultValue, result):
        '''bool QWebPage.javaScriptPrompt(QWebFrame originatingFrame, str msg, str defaultValue, str result)'''
        return bool()
    def javaScriptConfirm(self, originatingFrame, msg):
        '''bool QWebPage.javaScriptConfirm(QWebFrame originatingFrame, str msg)'''
        return bool()
    def javaScriptAlert(self, originatingFrame, msg):
        '''void QWebPage.javaScriptAlert(QWebFrame originatingFrame, str msg)'''
    def chooseFile(self, originatingFrame, oldFile):
        '''str QWebPage.chooseFile(QWebFrame originatingFrame, str oldFile)'''
        return str()
    def acceptNavigationRequest(self, frame, request, type):
        '''bool QWebPage.acceptNavigationRequest(QWebFrame frame, QNetworkRequest request, QWebPage.NavigationType type)'''
        return bool()
    def createPlugin(self, classid, url, paramNames, paramValues):
        '''QObject QWebPage.createPlugin(str classid, QUrl url, list-of-str paramNames, list-of-str paramValues)'''
        return QObject()
    def createWindow(self, type):
        '''QWebPage QWebPage.createWindow(QWebPage.WebWindowType type)'''
        return QWebPage()
    microFocusChanged = pyqtSignal() # void microFocusChanged() - signal
    downloadRequested = pyqtSignal() # void downloadRequested(const QNetworkRequestamp;) - signal
    unsupportedContent = pyqtSignal() # void unsupportedContent(QNetworkReply*) - signal
    menuBarVisibilityChangeRequested = pyqtSignal() # void menuBarVisibilityChangeRequested(bool) - signal
    statusBarVisibilityChangeRequested = pyqtSignal() # void statusBarVisibilityChangeRequested(bool) - signal
    toolBarVisibilityChangeRequested = pyqtSignal() # void toolBarVisibilityChangeRequested(bool) - signal
    linkClicked = pyqtSignal() # void linkClicked(const QUrlamp;) - signal
    printRequested = pyqtSignal() # void printRequested(QWebFrame*) - signal
    windowCloseRequested = pyqtSignal() # void windowCloseRequested() - signal
    scrollRequested = pyqtSignal() # void scrollRequested(int,int,const QRectamp;) - signal
    repaintRequested = pyqtSignal() # void repaintRequested(const QRectamp;) - signal
    geometryChangeRequested = pyqtSignal() # void geometryChangeRequested(const QRectamp;) - signal
    frameCreated = pyqtSignal() # void frameCreated(QWebFrame*) - signal
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
        '''bool QWebPage.findText(str subString, QWebPage.FindFlags options = 0)'''
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
        '''str QWebPage.selectedText()'''
        return str()
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
            '''QSizeF QWebPage.ViewportAttributes.size()'''
            return QSizeF()
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
        suggestedFileNames = None # list-of-str - member
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
        errorString = None # str - member
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
        contentType = None # str - member
        encoding = None # str - member
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
        fileNames = None # list-of-str - member
        def __init__(self):
            '''void QWebPage.ChooseMultipleFilesExtensionReturn.__init__()'''
        def __init__(self):
            '''QWebPage.ChooseMultipleFilesExtensionReturn QWebPage.ChooseMultipleFilesExtensionReturn.__init__()'''
            return QWebPage.ChooseMultipleFilesExtensionReturn()


class QWebView(QWidget):
    """"""
    def __init__(self, parent = None):
        '''void QWebView.__init__(QWidget parent = None)'''
    def selectedHtml(self):
        '''str QWebView.selectedHtml()'''
        return str()
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
        '''bool QWebView.findText(str subString, QWebPage.FindFlags options = 0)'''
        return bool()
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
        '''str QWebView.selectedText()'''
        return str()
    def icon(self):
        '''QIcon QWebView.icon()'''
        return QIcon()
    def url(self):
        '''QUrl QWebView.url()'''
        return QUrl()
    def setUrl(self, url):
        '''void QWebView.setUrl(QUrl url)'''
    def title(self):
        '''str QWebView.title()'''
        return str()
    def settings(self):
        '''QWebSettings QWebView.settings()'''
        return QWebSettings()
    def history(self):
        '''QWebHistory QWebView.history()'''
        return QWebHistory()
    def setContent(self, data, mimeType = None, baseUrl = QUrl()):
        '''void QWebView.setContent(QByteArray data, str mimeType = '', QUrl baseUrl = QUrl())'''
    def setHtml(self, html, baseUrl = QUrl()):
        '''void QWebView.setHtml(str html, QUrl baseUrl = QUrl())'''
    def load(self, url):
        '''void QWebView.load(QUrl url)'''
    def load(self, request, operation = None, body = QByteArray()):
        '''void QWebView.load(QNetworkRequest request, QNetworkAccessManager.Operation operation = QNetworkAccessManager.GetOperation, QByteArray body = QByteArray())'''
    def setPage(self, page):
        '''void QWebView.setPage(QWebPage page)'''
    def page(self):
        '''QWebPage QWebView.page()'''
        return QWebPage()


