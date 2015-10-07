class pyqtSignal():
 def connect(self, targetSignal): pass
 def emit(self, *args): pass
from QtCore import *

from QtWidgets import *

import datetime

class QWebEngineCertificateError():
    """"""
    # Enum QWebEngineCertificateError.Error
    SslPinnedKeyNotInCertificateChain = 0
    CertificateCommonNameInvalid = 0
    CertificateDateInvalid = 0
    CertificateAuthorityInvalid = 0
    CertificateContainsErrors = 0
    CertificateNoRevocationMechanism = 0
    CertificateUnableToCheckRevocation = 0
    CertificateRevoked = 0
    CertificateInvalid = 0
    CertificateWeakSignatureAlgorithm = 0
    CertificateNonUniqueName = 0
    CertificateWeakKey = 0
    CertificateNameConstraintViolation = 0

    def errorDescription(self):
        '''str QWebEngineCertificateError.errorDescription()'''
        return str()
    def isOverridable(self):
        '''bool QWebEngineCertificateError.isOverridable()'''
        return bool()
    def url(self):
        '''QUrl QWebEngineCertificateError.url()'''
        return QUrl()
    def error(self):
        '''QWebEngineCertificateError.Error QWebEngineCertificateError.error()'''
        return QWebEngineCertificateError.Error()


class QWebEngineHistoryItem():
    """"""
    def __init__(self, other):
        '''void QWebEngineHistoryItem.__init__(QWebEngineHistoryItem other)'''
    def isValid(self):
        '''bool QWebEngineHistoryItem.isValid()'''
        return bool()
    def iconUrl(self):
        '''QUrl QWebEngineHistoryItem.iconUrl()'''
        return QUrl()
    def lastVisited(self):
        '''QDateTime QWebEngineHistoryItem.lastVisited()'''
        return QDateTime()
    def title(self):
        '''str QWebEngineHistoryItem.title()'''
        return str()
    def url(self):
        '''QUrl QWebEngineHistoryItem.url()'''
        return QUrl()
    def originalUrl(self):
        '''QUrl QWebEngineHistoryItem.originalUrl()'''
        return QUrl()


class QWebEngineHistory():
    """"""
    def __len__(self):
        ''' QWebEngineHistory.__len__()'''
        return ()
    def count(self):
        '''int QWebEngineHistory.count()'''
        return int()
    def currentItemIndex(self):
        '''int QWebEngineHistory.currentItemIndex()'''
        return int()
    def itemAt(self, i):
        '''QWebEngineHistoryItem QWebEngineHistory.itemAt(int i)'''
        return QWebEngineHistoryItem()
    def forwardItem(self):
        '''QWebEngineHistoryItem QWebEngineHistory.forwardItem()'''
        return QWebEngineHistoryItem()
    def currentItem(self):
        '''QWebEngineHistoryItem QWebEngineHistory.currentItem()'''
        return QWebEngineHistoryItem()
    def backItem(self):
        '''QWebEngineHistoryItem QWebEngineHistory.backItem()'''
        return QWebEngineHistoryItem()
    def goToItem(self, item):
        '''void QWebEngineHistory.goToItem(QWebEngineHistoryItem item)'''
    def forward(self):
        '''void QWebEngineHistory.forward()'''
    def back(self):
        '''void QWebEngineHistory.back()'''
    def canGoForward(self):
        '''bool QWebEngineHistory.canGoForward()'''
        return bool()
    def canGoBack(self):
        '''bool QWebEngineHistory.canGoBack()'''
        return bool()
    def forwardItems(self, maxItems):
        '''list-of-QWebEngineHistoryItem QWebEngineHistory.forwardItems(int maxItems)'''
        return [QWebEngineHistoryItem()]
    def backItems(self, maxItems):
        '''list-of-QWebEngineHistoryItem QWebEngineHistory.backItems(int maxItems)'''
        return [QWebEngineHistoryItem()]
    def items(self):
        '''list-of-QWebEngineHistoryItem QWebEngineHistory.items()'''
        return [QWebEngineHistoryItem()]
    def clear(self):
        '''void QWebEngineHistory.clear()'''


class QWebEnginePage(QObject):
    """"""
    # Enum QWebEnginePage.NavigationType
    NavigationTypeLinkClicked = 0
    NavigationTypeTyped = 0
    NavigationTypeFormSubmitted = 0
    NavigationTypeBackForward = 0
    NavigationTypeReload = 0
    NavigationTypeOther = 0

    # Enum QWebEnginePage.JavaScriptConsoleMessageLevel
    InfoMessageLevel = 0
    WarningMessageLevel = 0
    ErrorMessageLevel = 0

    # Enum QWebEnginePage.FileSelectionMode
    FileSelectOpen = 0
    FileSelectOpenMultiple = 0

    # Enum QWebEnginePage.Feature
    Geolocation = 0
    MediaAudioCapture = 0
    MediaVideoCapture = 0
    MediaAudioVideoCapture = 0

    # Enum QWebEnginePage.PermissionPolicy
    PermissionUnknown = 0
    PermissionGrantedByUser = 0
    PermissionDeniedByUser = 0

    # Enum QWebEnginePage.WebWindowType
    WebBrowserWindow = 0
    WebBrowserTab = 0
    WebDialog = 0

    # Enum QWebEnginePage.FindFlag
    FindBackward = 0
    FindCaseSensitively = 0

    # Enum QWebEnginePage.WebAction
    NoWebAction = 0
    Back = 0
    Forward = 0
    Stop = 0
    Reload = 0
    Cut = 0
    Copy = 0
    Paste = 0
    Undo = 0
    Redo = 0
    SelectAll = 0
    ReloadAndBypassCache = 0
    PasteAndMatchStyle = 0

    def __init__(self, parent = None):
        '''void QWebEnginePage.__init__(QObject parent = None)'''
    def __init__(self, profile, parent = None):
        '''void QWebEnginePage.__init__(QWebEngineProfile profile, QObject parent = None)'''
    def acceptNavigationRequest(self, url, type, isMainFrame):
        '''bool QWebEnginePage.acceptNavigationRequest(QUrl url, QWebEnginePage.NavigationType type, bool isMainFrame)'''
        return bool()
    def setWebChannel(self):
        '''QWebChannel QWebEnginePage.setWebChannel()'''
        return QWebChannel()
    def webChannel(self):
        '''QWebChannel QWebEnginePage.webChannel()'''
        return QWebChannel()
    def scripts(self):
        '''QWebEngineScriptCollection QWebEnginePage.scripts()'''
        return QWebEngineScriptCollection()
    def profile(self):
        '''QWebEngineProfile QWebEnginePage.profile()'''
        return QWebEngineProfile()
    def certificateError(self, certificateError):
        '''bool QWebEnginePage.certificateError(QWebEngineCertificateError certificateError)'''
        return bool()
    def javaScriptConsoleMessage(self, level, message, lineNumber, sourceID):
        '''void QWebEnginePage.javaScriptConsoleMessage(QWebEnginePage.JavaScriptConsoleMessageLevel level, str message, int lineNumber, str sourceID)'''
    def javaScriptPrompt(self, securityOrigin, msg, defaultValue, result):
        '''bool QWebEnginePage.javaScriptPrompt(QUrl securityOrigin, str msg, str defaultValue, str result)'''
        return bool()
    def javaScriptConfirm(self, securityOrigin, msg):
        '''bool QWebEnginePage.javaScriptConfirm(QUrl securityOrigin, str msg)'''
        return bool()
    def javaScriptAlert(self, securityOrigin, msg):
        '''void QWebEnginePage.javaScriptAlert(QUrl securityOrigin, str msg)'''
    def chooseFiles(self, mode, oldFiles, acceptedMimeTypes):
        '''list-of-str QWebEnginePage.chooseFiles(QWebEnginePage.FileSelectionMode mode, list-of-str oldFiles, list-of-str acceptedMimeTypes)'''
        return [str()]
    def createWindow(self, type):
        '''QWebEnginePage QWebEnginePage.createWindow(QWebEnginePage.WebWindowType type)'''
        return QWebEnginePage()
    iconUrlChanged = pyqtSignal() # void iconUrlChanged(const QUrlamp;) - signal
    urlChanged = pyqtSignal() # void urlChanged(const QUrlamp;) - signal
    titleChanged = pyqtSignal() # void titleChanged(const QStringamp;) - signal
    proxyAuthenticationRequired = pyqtSignal() # void proxyAuthenticationRequired(const QUrlamp;,QAuthenticator*,const QStringamp;) - signal
    authenticationRequired = pyqtSignal() # void authenticationRequired(const QUrlamp;,QAuthenticator*) - signal
    featurePermissionRequestCanceled = pyqtSignal() # void featurePermissionRequestCanceled(const QUrlamp;,QWebEnginePage::Feature) - signal
    featurePermissionRequested = pyqtSignal() # void featurePermissionRequested(const QUrlamp;,QWebEnginePage::Feature) - signal
    windowCloseRequested = pyqtSignal() # void windowCloseRequested() - signal
    geometryChangeRequested = pyqtSignal() # void geometryChangeRequested(const QRectamp;) - signal
    selectionChanged = pyqtSignal() # void selectionChanged() - signal
    linkHovered = pyqtSignal() # void linkHovered(const QStringamp;) - signal
    loadFinished = pyqtSignal() # void loadFinished(bool) - signal
    loadProgress = pyqtSignal() # void loadProgress(int) - signal
    loadStarted = pyqtSignal() # void loadStarted() - signal
    def settings(self):
        '''QWebEngineSettings QWebEnginePage.settings()'''
        return QWebEngineSettings()
    def runJavaScript(self, scriptSource):
        '''void QWebEnginePage.runJavaScript(str scriptSource)'''
    def runJavaScript(self, scriptSource, resultCallback):
        '''void QWebEnginePage.runJavaScript(str scriptSource, callable resultCallback)'''
    def setZoomFactor(self, factor):
        '''void QWebEnginePage.setZoomFactor(float factor)'''
    def zoomFactor(self):
        '''float QWebEnginePage.zoomFactor()'''
        return float()
    def iconUrl(self):
        '''QUrl QWebEnginePage.iconUrl()'''
        return QUrl()
    def requestedUrl(self):
        '''QUrl QWebEnginePage.requestedUrl()'''
        return QUrl()
    def url(self):
        '''QUrl QWebEnginePage.url()'''
        return QUrl()
    def setUrl(self, url):
        '''void QWebEnginePage.setUrl(QUrl url)'''
    def title(self):
        '''str QWebEnginePage.title()'''
        return str()
    def toPlainText(self, resultCallback):
        '''void QWebEnginePage.toPlainText(callable resultCallback)'''
    def toHtml(self, resultCallback):
        '''void QWebEnginePage.toHtml(callable resultCallback)'''
    def setContent(self, data, mimeType = str(), baseUrl = QUrl()):
        '''void QWebEnginePage.setContent(QByteArray data, str mimeType = str(), QUrl baseUrl = QUrl())'''
    def setHtml(self, html, baseUrl = QUrl()):
        '''void QWebEnginePage.setHtml(str html, QUrl baseUrl = QUrl())'''
    def load(self, url):
        '''void QWebEnginePage.load(QUrl url)'''
    def setFeaturePermission(self, securityOrigin, feature, policy):
        '''void QWebEnginePage.setFeaturePermission(QUrl securityOrigin, QWebEnginePage.Feature feature, QWebEnginePage.PermissionPolicy policy)'''
    def createStandardContextMenu(self):
        '''QMenu QWebEnginePage.createStandardContextMenu()'''
        return QMenu()
    def findText(self, subString, options = 0, resultCallback = 0):
        '''void QWebEnginePage.findText(str subString, QWebEnginePage.FindFlags options = 0, callable resultCallback = 0)'''
    def event(self):
        '''QEvent QWebEnginePage.event()'''
        return QEvent()
    def triggerAction(self, action, checked = False):
        '''void QWebEnginePage.triggerAction(QWebEnginePage.WebAction action, bool checked = False)'''
    def action(self, action):
        '''QAction QWebEnginePage.action(QWebEnginePage.WebAction action)'''
        return QAction()
    def selectedText(self):
        '''str QWebEnginePage.selectedText()'''
        return str()
    def hasSelection(self):
        '''bool QWebEnginePage.hasSelection()'''
        return bool()
    def view(self):
        '''QWidget QWebEnginePage.view()'''
        return QWidget()
    def setView(self, view):
        '''void QWebEnginePage.setView(QWidget view)'''
    def history(self):
        '''QWebEngineHistory QWebEnginePage.history()'''
        return QWebEngineHistory()
    class FindFlags():
        """"""
        def __init__(self):
            '''QWebEnginePage.FindFlags QWebEnginePage.FindFlags.__init__()'''
            return QWebEnginePage.FindFlags()
        def __init__(self):
            '''int QWebEnginePage.FindFlags.__init__()'''
            return int()
        def __init__(self):
            '''void QWebEnginePage.FindFlags.__init__()'''
        def __bool__(self):
            '''int QWebEnginePage.FindFlags.__bool__()'''
            return int()
        def __ne__(self, f):
            '''bool QWebEnginePage.FindFlags.__ne__(QWebEnginePage.FindFlags f)'''
            return bool()
        def __eq__(self, f):
            '''bool QWebEnginePage.FindFlags.__eq__(QWebEnginePage.FindFlags f)'''
            return bool()
        def __invert__(self):
            '''QWebEnginePage.FindFlags QWebEnginePage.FindFlags.__invert__()'''
            return QWebEnginePage.FindFlags()
        def __and__(self, mask):
            '''QWebEnginePage.FindFlags QWebEnginePage.FindFlags.__and__(int mask)'''
            return QWebEnginePage.FindFlags()
        def __xor__(self, f):
            '''QWebEnginePage.FindFlags QWebEnginePage.FindFlags.__xor__(QWebEnginePage.FindFlags f)'''
            return QWebEnginePage.FindFlags()
        def __xor__(self, f):
            '''QWebEnginePage.FindFlags QWebEnginePage.FindFlags.__xor__(int f)'''
            return QWebEnginePage.FindFlags()
        def __or__(self, f):
            '''QWebEnginePage.FindFlags QWebEnginePage.FindFlags.__or__(QWebEnginePage.FindFlags f)'''
            return QWebEnginePage.FindFlags()
        def __or__(self, f):
            '''QWebEnginePage.FindFlags QWebEnginePage.FindFlags.__or__(int f)'''
            return QWebEnginePage.FindFlags()
        def __int__(self):
            '''int QWebEnginePage.FindFlags.__int__()'''
            return int()
        def __ixor__(self, f):
            '''QWebEnginePage.FindFlags QWebEnginePage.FindFlags.__ixor__(QWebEnginePage.FindFlags f)'''
            return QWebEnginePage.FindFlags()
        def __ior__(self, f):
            '''QWebEnginePage.FindFlags QWebEnginePage.FindFlags.__ior__(QWebEnginePage.FindFlags f)'''
            return QWebEnginePage.FindFlags()
        def __iand__(self, mask):
            '''QWebEnginePage.FindFlags QWebEnginePage.FindFlags.__iand__(int mask)'''
            return QWebEnginePage.FindFlags()


class QWebEngineSettings():
    """"""
    # Enum QWebEngineSettings.FontSize
    MinimumFontSize = 0
    MinimumLogicalFontSize = 0
    DefaultFontSize = 0
    DefaultFixedFontSize = 0

    # Enum QWebEngineSettings.WebAttribute
    AutoLoadImages = 0
    JavascriptEnabled = 0
    JavascriptCanOpenWindows = 0
    JavascriptCanAccessClipboard = 0
    LinksIncludedInFocusChain = 0
    LocalStorageEnabled = 0
    LocalContentCanAccessRemoteUrls = 0
    XSSAuditingEnabled = 0
    SpatialNavigationEnabled = 0
    LocalContentCanAccessFileUrls = 0
    HyperlinkAuditingEnabled = 0
    ScrollAnimatorEnabled = 0
    ErrorPageEnabled = 0

    # Enum QWebEngineSettings.FontFamily
    StandardFont = 0
    FixedFont = 0
    SerifFont = 0
    SansSerifFont = 0
    CursiveFont = 0
    FantasyFont = 0

    def defaultTextEncoding(self):
        '''str QWebEngineSettings.defaultTextEncoding()'''
        return str()
    def setDefaultTextEncoding(self, encoding):
        '''void QWebEngineSettings.setDefaultTextEncoding(str encoding)'''
    def resetAttribute(self, attr):
        '''void QWebEngineSettings.resetAttribute(QWebEngineSettings.WebAttribute attr)'''
    def testAttribute(self, attr):
        '''bool QWebEngineSettings.testAttribute(QWebEngineSettings.WebAttribute attr)'''
        return bool()
    def setAttribute(self, attr, on):
        '''void QWebEngineSettings.setAttribute(QWebEngineSettings.WebAttribute attr, bool on)'''
    def resetFontSize(self, type):
        '''void QWebEngineSettings.resetFontSize(QWebEngineSettings.FontSize type)'''
    def fontSize(self, type):
        '''int QWebEngineSettings.fontSize(QWebEngineSettings.FontSize type)'''
        return int()
    def setFontSize(self, type, size):
        '''void QWebEngineSettings.setFontSize(QWebEngineSettings.FontSize type, int size)'''
    def resetFontFamily(self, which):
        '''void QWebEngineSettings.resetFontFamily(QWebEngineSettings.FontFamily which)'''
    def fontFamily(self, which):
        '''str QWebEngineSettings.fontFamily(QWebEngineSettings.FontFamily which)'''
        return str()
    def setFontFamily(self, which, family):
        '''void QWebEngineSettings.setFontFamily(QWebEngineSettings.FontFamily which, str family)'''
    def globalSettings(self):
        '''static QWebEngineSettings QWebEngineSettings.globalSettings()'''
        return QWebEngineSettings()
    def defaultSettings(self):
        '''static QWebEngineSettings QWebEngineSettings.defaultSettings()'''
        return QWebEngineSettings()


class QWebEngineView(QWidget):
    """"""
    def __init__(self, parent = None):
        '''void QWebEngineView.__init__(QWidget parent = None)'''
    def event(self):
        '''QEvent QWebEngineView.event()'''
        return QEvent()
    def contextMenuEvent(self):
        '''QContextMenuEvent QWebEngineView.contextMenuEvent()'''
        return QContextMenuEvent()
    def createWindow(self, type):
        '''QWebEngineView QWebEngineView.createWindow(QWebEnginePage.WebWindowType type)'''
        return QWebEngineView()
    iconUrlChanged = pyqtSignal() # void iconUrlChanged(const QUrlamp;) - signal
    urlChanged = pyqtSignal() # void urlChanged(const QUrlamp;) - signal
    selectionChanged = pyqtSignal() # void selectionChanged() - signal
    titleChanged = pyqtSignal() # void titleChanged(const QStringamp;) - signal
    loadFinished = pyqtSignal() # void loadFinished(bool) - signal
    loadProgress = pyqtSignal() # void loadProgress(int) - signal
    loadStarted = pyqtSignal() # void loadStarted() - signal
    def reload(self):
        '''void QWebEngineView.reload()'''
    def forward(self):
        '''void QWebEngineView.forward()'''
    def back(self):
        '''void QWebEngineView.back()'''
    def stop(self):
        '''void QWebEngineView.stop()'''
    def settings(self):
        '''QWebEngineSettings QWebEngineView.settings()'''
        return QWebEngineSettings()
    def sizeHint(self):
        '''QSize QWebEngineView.sizeHint()'''
        return QSize()
    def findText(self, subString, options = 0, resultCallback = 0):
        '''void QWebEngineView.findText(str subString, QWebEnginePage.FindFlags options = 0, callable resultCallback = 0)'''
    def setZoomFactor(self, factor):
        '''void QWebEngineView.setZoomFactor(float factor)'''
    def zoomFactor(self):
        '''float QWebEngineView.zoomFactor()'''
        return float()
    def triggerPageAction(self, action, checked = False):
        '''void QWebEngineView.triggerPageAction(QWebEnginePage.WebAction action, bool checked = False)'''
    def pageAction(self, action):
        '''QAction QWebEngineView.pageAction(QWebEnginePage.WebAction action)'''
        return QAction()
    def selectedText(self):
        '''str QWebEngineView.selectedText()'''
        return str()
    def hasSelection(self):
        '''bool QWebEngineView.hasSelection()'''
        return bool()
    def iconUrl(self):
        '''QUrl QWebEngineView.iconUrl()'''
        return QUrl()
    def url(self):
        '''QUrl QWebEngineView.url()'''
        return QUrl()
    def setUrl(self, url):
        '''void QWebEngineView.setUrl(QUrl url)'''
    def title(self):
        '''str QWebEngineView.title()'''
        return str()
    def history(self):
        '''QWebEngineHistory QWebEngineView.history()'''
        return QWebEngineHistory()
    def setContent(self, data, mimeType = str(), baseUrl = QUrl()):
        '''void QWebEngineView.setContent(QByteArray data, str mimeType = str(), QUrl baseUrl = QUrl())'''
    def setHtml(self, html, baseUrl = QUrl()):
        '''void QWebEngineView.setHtml(str html, QUrl baseUrl = QUrl())'''
    def load(self, url):
        '''void QWebEngineView.load(QUrl url)'''
    def setPage(self, page):
        '''void QWebEngineView.setPage(QWebEnginePage page)'''
    def page(self):
        '''QWebEnginePage QWebEngineView.page()'''
        return QWebEnginePage()


class QWebEngineDownloadItem(QObject):
    """"""
    # Enum QWebEngineDownloadItem.DownloadState
    DownloadRequested = 0
    DownloadInProgress = 0
    DownloadCompleted = 0
    DownloadCancelled = 0
    DownloadInterrupted = 0

    downloadProgress = pyqtSignal() # void downloadProgress(qint64,qint64) - signal
    stateChanged = pyqtSignal() # void stateChanged(QWebEngineDownloadItem::DownloadState) - signal
    finished = pyqtSignal() # void finished() - signal
    def cancel(self):
        '''void QWebEngineDownloadItem.cancel()'''
    def accept(self):
        '''void QWebEngineDownloadItem.accept()'''
    def isFinished(self):
        '''bool QWebEngineDownloadItem.isFinished()'''
        return bool()
    def setPath(self, path):
        '''void QWebEngineDownloadItem.setPath(str path)'''
    def path(self):
        '''str QWebEngineDownloadItem.path()'''
        return str()
    def url(self):
        '''QUrl QWebEngineDownloadItem.url()'''
        return QUrl()
    def receivedBytes(self):
        '''int QWebEngineDownloadItem.receivedBytes()'''
        return int()
    def totalBytes(self):
        '''int QWebEngineDownloadItem.totalBytes()'''
        return int()
    def state(self):
        '''QWebEngineDownloadItem.DownloadState QWebEngineDownloadItem.state()'''
        return QWebEngineDownloadItem.DownloadState()
    def id(self):
        '''int QWebEngineDownloadItem.id()'''
        return int()


class QWebEngineProfile(QObject):
    """"""
    # Enum QWebEngineProfile.PersistentCookiesPolicy
    NoPersistentCookies = 0
    AllowPersistentCookies = 0
    ForcePersistentCookies = 0

    # Enum QWebEngineProfile.HttpCacheType
    MemoryHttpCache = 0
    DiskHttpCache = 0

    def __init__(self, parent = None):
        '''void QWebEngineProfile.__init__(QObject parent = None)'''
    def __init__(self, name, parent = None):
        '''void QWebEngineProfile.__init__(str name, QObject parent = None)'''
    downloadRequested = pyqtSignal() # void downloadRequested(QWebEngineDownloadItem*) - signal
    def defaultProfile(self):
        '''static QWebEngineProfile QWebEngineProfile.defaultProfile()'''
        return QWebEngineProfile()
    def scripts(self):
        '''QWebEngineScriptCollection QWebEngineProfile.scripts()'''
        return QWebEngineScriptCollection()
    def settings(self):
        '''QWebEngineSettings QWebEngineProfile.settings()'''
        return QWebEngineSettings()
    def visitedLinksContainsUrl(self, url):
        '''bool QWebEngineProfile.visitedLinksContainsUrl(QUrl url)'''
        return bool()
    def clearVisitedLinks(self, urls):
        '''void QWebEngineProfile.clearVisitedLinks(list-of-QUrl urls)'''
    def clearAllVisitedLinks(self):
        '''void QWebEngineProfile.clearAllVisitedLinks()'''
    def setHttpCacheMaximumSize(self, maxSize):
        '''void QWebEngineProfile.setHttpCacheMaximumSize(int maxSize)'''
    def httpCacheMaximumSize(self):
        '''int QWebEngineProfile.httpCacheMaximumSize()'''
        return int()
    def setPersistentCookiesPolicy(self):
        '''QWebEngineProfile.PersistentCookiesPolicy QWebEngineProfile.setPersistentCookiesPolicy()'''
        return QWebEngineProfile.PersistentCookiesPolicy()
    def persistentCookiesPolicy(self):
        '''QWebEngineProfile.PersistentCookiesPolicy QWebEngineProfile.persistentCookiesPolicy()'''
        return QWebEngineProfile.PersistentCookiesPolicy()
    def setHttpCacheType(self):
        '''QWebEngineProfile.HttpCacheType QWebEngineProfile.setHttpCacheType()'''
        return QWebEngineProfile.HttpCacheType()
    def httpCacheType(self):
        '''QWebEngineProfile.HttpCacheType QWebEngineProfile.httpCacheType()'''
        return QWebEngineProfile.HttpCacheType()
    def setHttpUserAgent(self, userAgent):
        '''void QWebEngineProfile.setHttpUserAgent(str userAgent)'''
    def httpUserAgent(self):
        '''str QWebEngineProfile.httpUserAgent()'''
        return str()
    def setCachePath(self, path):
        '''void QWebEngineProfile.setCachePath(str path)'''
    def cachePath(self):
        '''str QWebEngineProfile.cachePath()'''
        return str()
    def setPersistentStoragePath(self, path):
        '''void QWebEngineProfile.setPersistentStoragePath(str path)'''
    def persistentStoragePath(self):
        '''str QWebEngineProfile.persistentStoragePath()'''
        return str()
    def isOffTheRecord(self):
        '''bool QWebEngineProfile.isOffTheRecord()'''
        return bool()
    def storageName(self):
        '''str QWebEngineProfile.storageName()'''
        return str()


class QWebEngineScript():
    """"""
    # Enum QWebEngineScript.ScriptWorldId
    MainWorld = 0
    ApplicationWorld = 0
    UserWorld = 0

    # Enum QWebEngineScript.InjectionPoint
    Deferred = 0
    DocumentReady = 0
    DocumentCreation = 0

    def __init__(self):
        '''void QWebEngineScript.__init__()'''
    def __init__(self, other):
        '''void QWebEngineScript.__init__(QWebEngineScript other)'''
    def swap(self, other):
        '''void QWebEngineScript.swap(QWebEngineScript other)'''
    def __ne__(self, other):
        '''bool QWebEngineScript.__ne__(QWebEngineScript other)'''
        return bool()
    def __eq__(self, other):
        '''bool QWebEngineScript.__eq__(QWebEngineScript other)'''
        return bool()
    def setRunsOnSubFrames(self, on):
        '''void QWebEngineScript.setRunsOnSubFrames(bool on)'''
    def runsOnSubFrames(self):
        '''bool QWebEngineScript.runsOnSubFrames()'''
        return bool()
    def setWorldId(self):
        '''int QWebEngineScript.setWorldId()'''
        return int()
    def worldId(self):
        '''int QWebEngineScript.worldId()'''
        return int()
    def setInjectionPoint(self):
        '''QWebEngineScript.InjectionPoint QWebEngineScript.setInjectionPoint()'''
        return QWebEngineScript.InjectionPoint()
    def injectionPoint(self):
        '''QWebEngineScript.InjectionPoint QWebEngineScript.injectionPoint()'''
        return QWebEngineScript.InjectionPoint()
    def setSourceCode(self):
        '''str QWebEngineScript.setSourceCode()'''
        return str()
    def sourceCode(self):
        '''str QWebEngineScript.sourceCode()'''
        return str()
    def setName(self):
        '''str QWebEngineScript.setName()'''
        return str()
    def name(self):
        '''str QWebEngineScript.name()'''
        return str()
    def isNull(self):
        '''bool QWebEngineScript.isNull()'''
        return bool()


class QWebEngineScriptCollection():
    """"""
    def toList(self):
        '''list-of-QWebEngineScript QWebEngineScriptCollection.toList()'''
        return [QWebEngineScript()]
    def clear(self):
        '''void QWebEngineScriptCollection.clear()'''
    def remove(self):
        '''QWebEngineScript QWebEngineScriptCollection.remove()'''
        return QWebEngineScript()
    def insert(self):
        '''QWebEngineScript QWebEngineScriptCollection.insert()'''
        return QWebEngineScript()
    def insert(self, list):
        '''void QWebEngineScriptCollection.insert(list-of-QWebEngineScript list)'''
    def findScripts(self, name):
        '''list-of-QWebEngineScript QWebEngineScriptCollection.findScripts(str name)'''
        return [QWebEngineScript()]
    def findScript(self, name):
        '''QWebEngineScript QWebEngineScriptCollection.findScript(str name)'''
        return QWebEngineScript()
    def contains(self, value):
        '''bool QWebEngineScriptCollection.contains(QWebEngineScript value)'''
        return bool()
    def __len__(self):
        ''' QWebEngineScriptCollection.__len__()'''
        return ()
    def count(self):
        '''int QWebEngineScriptCollection.count()'''
        return int()
    def isEmpty(self):
        '''bool QWebEngineScriptCollection.isEmpty()'''
        return bool()


