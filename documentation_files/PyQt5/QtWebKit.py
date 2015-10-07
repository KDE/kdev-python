class pyqtSignal():
 def connect(self, targetSignal): pass
 def emit(self, *args): pass
from QtCore import *

from QtWidgets import *

import datetime

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
        '''str QWebDatabase.fileName()'''
        return str()
    def size(self):
        '''int QWebDatabase.size()'''
        return int()
    def expectedSize(self):
        '''int QWebDatabase.expectedSize()'''
        return int()
    def displayName(self):
        '''str QWebDatabase.displayName()'''
        return str()
    def name(self):
        '''str QWebDatabase.name()'''
        return str()


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
        '''void QWebElement.setStyleProperty(str name, str value)'''
    def styleProperty(self, name, strategy):
        '''str QWebElement.styleProperty(str name, QWebElement.StyleResolveStrategy strategy)'''
        return str()
    def evaluateJavaScript(self, scriptSource):
        '''QVariant QWebElement.evaluateJavaScript(str scriptSource)'''
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
        '''void QWebElement.replace(str markup)'''
    def replace(self, element):
        '''void QWebElement.replace(QWebElement element)'''
    def encloseWith(self, markup):
        '''void QWebElement.encloseWith(str markup)'''
    def encloseWith(self, element):
        '''void QWebElement.encloseWith(QWebElement element)'''
    def encloseContentsWith(self, element):
        '''void QWebElement.encloseContentsWith(QWebElement element)'''
    def encloseContentsWith(self, markup):
        '''void QWebElement.encloseContentsWith(str markup)'''
    def prependOutside(self, markup):
        '''void QWebElement.prependOutside(str markup)'''
    def prependOutside(self, element):
        '''void QWebElement.prependOutside(QWebElement element)'''
    def appendOutside(self, markup):
        '''void QWebElement.appendOutside(str markup)'''
    def appendOutside(self, element):
        '''void QWebElement.appendOutside(QWebElement element)'''
    def prependInside(self, markup):
        '''void QWebElement.prependInside(str markup)'''
    def prependInside(self, element):
        '''void QWebElement.prependInside(QWebElement element)'''
    def appendInside(self, markup):
        '''void QWebElement.appendInside(str markup)'''
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
        '''str QWebElement.namespaceUri()'''
        return str()
    def localName(self):
        '''str QWebElement.localName()'''
        return str()
    def prefix(self):
        '''str QWebElement.prefix()'''
        return str()
    def tagName(self):
        '''str QWebElement.tagName()'''
        return str()
    def geometry(self):
        '''QRect QWebElement.geometry()'''
        return QRect()
    def setFocus(self):
        '''void QWebElement.setFocus()'''
    def hasFocus(self):
        '''bool QWebElement.hasFocus()'''
        return bool()
    def toggleClass(self, name):
        '''void QWebElement.toggleClass(str name)'''
    def removeClass(self, name):
        '''void QWebElement.removeClass(str name)'''
    def addClass(self, name):
        '''void QWebElement.addClass(str name)'''
    def hasClass(self, name):
        '''bool QWebElement.hasClass(str name)'''
        return bool()
    def classes(self):
        '''list-of-str QWebElement.classes()'''
        return [str()]
    def attributeNames(self, namespaceUri = str()):
        '''list-of-str QWebElement.attributeNames(str namespaceUri = str())'''
        return [str()]
    def hasAttributes(self):
        '''bool QWebElement.hasAttributes()'''
        return bool()
    def removeAttributeNS(self, namespaceUri, name):
        '''void QWebElement.removeAttributeNS(str namespaceUri, str name)'''
    def removeAttribute(self, name):
        '''void QWebElement.removeAttribute(str name)'''
    def hasAttributeNS(self, namespaceUri, name):
        '''bool QWebElement.hasAttributeNS(str namespaceUri, str name)'''
        return bool()
    def hasAttribute(self, name):
        '''bool QWebElement.hasAttribute(str name)'''
        return bool()
    def attributeNS(self, namespaceUri, name, defaultValue = str()):
        '''str QWebElement.attributeNS(str namespaceUri, str name, str defaultValue = str())'''
        return str()
    def attribute(self, name, defaultValue = str()):
        '''str QWebElement.attribute(str name, str defaultValue = str())'''
        return str()
    def setAttributeNS(self, namespaceUri, name, value):
        '''void QWebElement.setAttributeNS(str namespaceUri, str name, str value)'''
    def setAttribute(self, name, value):
        '''void QWebElement.setAttribute(str name, str value)'''
    def toInnerXml(self):
        '''str QWebElement.toInnerXml()'''
        return str()
    def setInnerXml(self, markup):
        '''void QWebElement.setInnerXml(str markup)'''
    def toOuterXml(self):
        '''str QWebElement.toOuterXml()'''
        return str()
    def setOuterXml(self, markup):
        '''void QWebElement.setOuterXml(str markup)'''
    def toPlainText(self):
        '''str QWebElement.toPlainText()'''
        return str()
    def setPlainText(self, text):
        '''void QWebElement.setPlainText(str text)'''
    def findFirst(self, selectorQuery):
        '''QWebElement QWebElement.findFirst(str selectorQuery)'''
        return QWebElement()
    def findAll(self, selectorQuery):
        '''QWebElementCollection QWebElement.findAll(str selectorQuery)'''
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
        '''void QWebElementCollection.__init__(QWebElement contextElement, str query)'''
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
        ''' QWebElementCollection.__len__()'''
        return ()
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
        '''str QWebHistoryItem.title()'''
        return str()
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
        ''' QWebHistory.__len__()'''
        return ()
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
        '''abstract void QWebHistoryInterface.addHistoryEntry(str url)'''
    def historyContains(self, url):
        '''abstract bool QWebHistoryInterface.historyContains(str url)'''
        return bool()
    def defaultInterface(self):
        '''static QWebHistoryInterface QWebHistoryInterface.defaultInterface()'''
        return QWebHistoryInterface()
    def setDefaultInterface(self, defaultInterface):
        '''static void QWebHistoryInterface.setDefaultInterface(QWebHistoryInterface defaultInterface)'''


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
        '''abstract QObject QWebPluginFactory.create(str mimeType, QUrl url, list-of-str argumentNames, list-of-str argumentValues)'''
        return QObject()
    def refreshPlugins(self):
        '''void QWebPluginFactory.refreshPlugins()'''
    def plugins(self):
        '''abstract list-of-QWebPluginFactory.Plugin QWebPluginFactory.plugins()'''
        return [QWebPluginFactory.Plugin()]
    class Plugin():
        """"""
        description = None # str - member
        mimeTypes = None # list-of-QWebPluginFactory.MimeType - member
        name = None # str - member
        def __init__(self):
            '''void QWebPluginFactory.Plugin.__init__()'''
        def __init__(self):
            '''QWebPluginFactory.Plugin QWebPluginFactory.Plugin.__init__()'''
            return QWebPluginFactory.Plugin()
    class MimeType():
        """"""
        description = None # str - member
        fileExtensions = None # list-of-str - member
        name = None # str - member
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
    class ExtensionReturn():
        """"""
        def __init__(self):
            '''void QWebPluginFactory.ExtensionReturn.__init__()'''
        def __init__(self):
            '''QWebPluginFactory.ExtensionReturn QWebPluginFactory.ExtensionReturn.__init__()'''
            return QWebPluginFactory.ExtensionReturn()
    class ExtensionOption():
        """"""
        def __init__(self):
            '''void QWebPluginFactory.ExtensionOption.__init__()'''
        def __init__(self):
            '''QWebPluginFactory.ExtensionOption QWebPluginFactory.ExtensionOption.__init__()'''
            return QWebPluginFactory.ExtensionOption()


class QWebSecurityOrigin():
    """"""
    # Enum QWebSecurityOrigin.SubdomainSetting
    AllowSubdomains = 0
    DisallowSubdomains = 0

    def __init__(self, url):
        '''void QWebSecurityOrigin.__init__(QUrl url)'''
    def __init__(self, other):
        '''void QWebSecurityOrigin.__init__(QWebSecurityOrigin other)'''
    def removeAccessWhitelistEntry(self, scheme, host, subdomainSetting):
        '''void QWebSecurityOrigin.removeAccessWhitelistEntry(str scheme, str host, QWebSecurityOrigin.SubdomainSetting subdomainSetting)'''
    def addAccessWhitelistEntry(self, scheme, host, subdomainSetting):
        '''void QWebSecurityOrigin.addAccessWhitelistEntry(str scheme, str host, QWebSecurityOrigin.SubdomainSetting subdomainSetting)'''
    def setApplicationCacheQuota(self, quota):
        '''void QWebSecurityOrigin.setApplicationCacheQuota(int quota)'''
    def localSchemes(self):
        '''static list-of-str QWebSecurityOrigin.localSchemes()'''
        return [str()]
    def removeLocalScheme(self, scheme):
        '''static void QWebSecurityOrigin.removeLocalScheme(str scheme)'''
    def addLocalScheme(self, scheme):
        '''static void QWebSecurityOrigin.addLocalScheme(str scheme)'''
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
        '''str QWebSecurityOrigin.host()'''
        return str()
    def scheme(self):
        '''str QWebSecurityOrigin.scheme()'''
        return str()
    def allOrigins(self):
        '''static list-of-QWebSecurityOrigin QWebSecurityOrigin.allOrigins()'''
        return [QWebSecurityOrigin()]


class QWebSettings():
    """"""
    # Enum QWebSettings.ThirdPartyCookiePolicy
    AlwaysAllowThirdPartyCookies = 0
    AlwaysBlockThirdPartyCookies = 0
    AllowThirdPartyWithExistingCookies = 0

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
    CSSRegionsEnabled = 0
    CSSGridLayoutEnabled = 0
    ScrollAnimatorEnabled = 0
    CaretBrowsingEnabled = 0
    NotificationsEnabled = 0
    WebAudioEnabled = 0
    Accelerated2dCanvasEnabled = 0

    # Enum QWebSettings.FontFamily
    StandardFont = 0
    FixedFont = 0
    SerifFont = 0
    SansSerifFont = 0
    CursiveFont = 0
    FantasyFont = 0

    def cssMediaType(self):
        '''str QWebSettings.cssMediaType()'''
        return str()
    def setCSSMediaType(self):
        '''str QWebSettings.setCSSMediaType()'''
        return str()
    def thirdPartyCookiePolicy(self):
        '''QWebSettings.ThirdPartyCookiePolicy QWebSettings.thirdPartyCookiePolicy()'''
        return QWebSettings.ThirdPartyCookiePolicy()
    def setThirdPartyCookiePolicy(self):
        '''QWebSettings.ThirdPartyCookiePolicy QWebSettings.setThirdPartyCookiePolicy()'''
        return QWebSettings.ThirdPartyCookiePolicy()
    def enablePersistentStorage(self, path = str()):
        '''static void QWebSettings.enablePersistentStorage(str path = str())'''
    def clearMemoryCaches(self):
        '''static void QWebSettings.clearMemoryCaches()'''
    def localStoragePath(self):
        '''str QWebSettings.localStoragePath()'''
        return str()
    def setLocalStoragePath(self, path):
        '''void QWebSettings.setLocalStoragePath(str path)'''
    def offlineWebApplicationCacheQuota(self):
        '''static int QWebSettings.offlineWebApplicationCacheQuota()'''
        return int()
    def setOfflineWebApplicationCacheQuota(self, maximumSize):
        '''static void QWebSettings.setOfflineWebApplicationCacheQuota(int maximumSize)'''
    def offlineWebApplicationCachePath(self):
        '''static str QWebSettings.offlineWebApplicationCachePath()'''
        return str()
    def setOfflineWebApplicationCachePath(self, path):
        '''static void QWebSettings.setOfflineWebApplicationCachePath(str path)'''
    def defaultTextEncoding(self):
        '''str QWebSettings.defaultTextEncoding()'''
        return str()
    def setDefaultTextEncoding(self, encoding):
        '''void QWebSettings.setDefaultTextEncoding(str encoding)'''
    def offlineStorageDefaultQuota(self):
        '''static int QWebSettings.offlineStorageDefaultQuota()'''
        return int()
    def setOfflineStorageDefaultQuota(self, maximumSize):
        '''static void QWebSettings.setOfflineStorageDefaultQuota(int maximumSize)'''
    def offlineStoragePath(self):
        '''static str QWebSettings.offlineStoragePath()'''
        return str()
    def setOfflineStoragePath(self, path):
        '''static void QWebSettings.setOfflineStoragePath(str path)'''
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
        '''static str QWebSettings.iconDatabasePath()'''
        return str()
    def setIconDatabasePath(self, location):
        '''static void QWebSettings.setIconDatabasePath(str location)'''
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
        '''str QWebSettings.fontFamily(QWebSettings.FontFamily which)'''
        return str()
    def setFontFamily(self, which, family):
        '''void QWebSettings.setFontFamily(QWebSettings.FontFamily which, str family)'''
    def globalSettings(self):
        '''static QWebSettings QWebSettings.globalSettings()'''
        return QWebSettings()


def qWebKitMinorVersion():
    '''static int qWebKitMinorVersion()'''
    return int()

def qWebKitMajorVersion():
    '''static int qWebKitMajorVersion()'''
    return int()

def qWebKitVersion():
    '''static str qWebKitVersion()'''
    return str()

