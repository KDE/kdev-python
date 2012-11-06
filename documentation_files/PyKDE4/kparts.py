class pyqtSignal():
 def connect(self, targetSignal): pass
 def emit(self, *args): pass
from QtCore import *

class KParts():
    """"""
    class PartSelectEvent(KParts.Event):
        """"""
        def __init__(self, selected, part, widget):
            '''void KParts.PartSelectEvent.__init__(bool selected, KParts.Part part, QWidget widget)'''
        def test(self, event):
            '''static bool KParts.PartSelectEvent.test(QEvent event)'''
            return bool()
        def widget(self):
            '''QWidget KParts.PartSelectEvent.widget()'''
            return QWidget()
        def part(self):
            '''KParts.Part KParts.PartSelectEvent.part()'''
            return KParts.Part()
        def selected(self):
            '''bool KParts.PartSelectEvent.selected()'''
            return bool()
    class HtmlExtension(QObject):
        """"""
        def __init__(self, parent):
            '''void KParts.HtmlExtension.__init__(KParts.ReadOnlyPart parent)'''
        def hasSelection(self):
            '''bool KParts.HtmlExtension.hasSelection()'''
            return bool()
        def baseUrl(self):
            '''abstract KUrl KParts.HtmlExtension.baseUrl()'''
            return KUrl()
        def childObject(self, obj):
            '''static KParts.HtmlExtension KParts.HtmlExtension.childObject(QObject obj)'''
            return KParts.HtmlExtension()
    class FileInfoExtension():
        """"""
        class QueryModes():
            """"""
            def __init__(self):
                '''KParts.FileInfoExtension.QueryModes KParts.FileInfoExtension.QueryModes.__init__()'''
                return KParts.FileInfoExtension.QueryModes()
            def __init__(self):
                '''int KParts.FileInfoExtension.QueryModes.__init__()'''
                return int()
            def __init__(self):
                '''void KParts.FileInfoExtension.QueryModes.__init__()'''
            def __bool__(self):
                '''int KParts.FileInfoExtension.QueryModes.__bool__()'''
                return int()
            def __ne__(self, f):
                '''bool KParts.FileInfoExtension.QueryModes.__ne__(KParts.FileInfoExtension.QueryModes f)'''
                return bool()
            def __eq__(self, f):
                '''bool KParts.FileInfoExtension.QueryModes.__eq__(KParts.FileInfoExtension.QueryModes f)'''
                return bool()
            def __invert__(self):
                '''KParts.FileInfoExtension.QueryModes KParts.FileInfoExtension.QueryModes.__invert__()'''
                return KParts.FileInfoExtension.QueryModes()
            def __and__(self, mask):
                '''KParts.FileInfoExtension.QueryModes KParts.FileInfoExtension.QueryModes.__and__(int mask)'''
                return KParts.FileInfoExtension.QueryModes()
            def __xor__(self, f):
                '''KParts.FileInfoExtension.QueryModes KParts.FileInfoExtension.QueryModes.__xor__(KParts.FileInfoExtension.QueryModes f)'''
                return KParts.FileInfoExtension.QueryModes()
            def __xor__(self, f):
                '''KParts.FileInfoExtension.QueryModes KParts.FileInfoExtension.QueryModes.__xor__(int f)'''
                return KParts.FileInfoExtension.QueryModes()
            def __or__(self, f):
                '''KParts.FileInfoExtension.QueryModes KParts.FileInfoExtension.QueryModes.__or__(KParts.FileInfoExtension.QueryModes f)'''
                return KParts.FileInfoExtension.QueryModes()
            def __or__(self, f):
                '''KParts.FileInfoExtension.QueryModes KParts.FileInfoExtension.QueryModes.__or__(int f)'''
                return KParts.FileInfoExtension.QueryModes()
            def __int__(self):
                '''int KParts.FileInfoExtension.QueryModes.__int__()'''
                return int()
            def __ixor__(self, f):
                '''KParts.FileInfoExtension.QueryModes KParts.FileInfoExtension.QueryModes.__ixor__(KParts.FileInfoExtension.QueryModes f)'''
                return KParts.FileInfoExtension.QueryModes()
            def __ior__(self, f):
                '''KParts.FileInfoExtension.QueryModes KParts.FileInfoExtension.QueryModes.__ior__(KParts.FileInfoExtension.QueryModes f)'''
                return KParts.FileInfoExtension.QueryModes()
            def __iand__(self, mask):
                '''KParts.FileInfoExtension.QueryModes KParts.FileInfoExtension.QueryModes.__iand__(int mask)'''
                return KParts.FileInfoExtension.QueryModes()
    class Plugin():
        """"""
        class PluginInfo():
            """"""
            m_absXMLFileName = None # QString - member
            m_document = None # QDomDocument - member
            m_relXMLFileName = None # QString - member
            def __init__(self):
                '''void KParts.Plugin.PluginInfo.__init__()'''
            def __init__(self):
                '''KParts.Plugin.PluginInfo KParts.Plugin.PluginInfo.__init__()'''
                return KParts.Plugin.PluginInfo()
    class HtmlSettingsInterface():
        """"""
        # Enum KParts.HtmlSettingsInterface.JSWindowFocusPolicy
        JSWindowFocusAllow = 0
        JSWindowFocusIgnore = 0
    
        # Enum KParts.HtmlSettingsInterface.JSWindowResizePolicy
        JSWindowResizeAllow = 0
        JSWindowResizeIgnore = 0
    
        # Enum KParts.HtmlSettingsInterface.JSWindowMovePolicy
        JSWindowMoveAllow = 0
        JSWindowMoveIgnore = 0
    
        # Enum KParts.HtmlSettingsInterface.JSWindowStatusPolicy
        JSWindowStatusAllow = 0
        JSWindowStatusIgnore = 0
    
        # Enum KParts.HtmlSettingsInterface.JSWindowOpenPolicy
        JSWindowOpenAllow = 0
        JSWindowOpenAsk = 0
        JSWindowOpenDeny = 0
        JSWindowOpenSmart = 0
    
        # Enum KParts.HtmlSettingsInterface.JavaScriptAdvice
        JavaScriptDunno = 0
        JavaScriptAccept = 0
        JavaScriptReject = 0
    
        # Enum KParts.HtmlSettingsInterface.HtmlSettingsType
        AutoLoadImages = 0
        DnsPrefetchEnabled = 0
        JavaEnabled = 0
        JavascriptEnabled = 0
        MetaRefreshEnabled = 0
        PluginsEnabled = 0
        PrivateBrowsingEnabled = 0
        OfflineStorageDatabaseEnabled = 0
        OfflineWebApplicationCacheEnabled = 0
        LocalStorageEnabled = 0
        UserDefinedStyleSheetURL = 0
    
        def __init__(self):
            '''void KParts.HtmlSettingsInterface.__init__()'''
        def __init__(self):
            '''KParts.HtmlSettingsInterface KParts.HtmlSettingsInterface.__init__()'''
            return KParts.HtmlSettingsInterface()
        def splitDomainAdvice(self, text, domain, javaAdvice, javaScriptAdvice):
            '''static void KParts.HtmlSettingsInterface.splitDomainAdvice(QString text, QString domain, KParts.HtmlSettingsInterface.JavaScriptAdvice javaAdvice, KParts.HtmlSettingsInterface.JavaScriptAdvice javaScriptAdvice)'''
        def javascriptAdviceToText(self, advice):
            '''static str KParts.HtmlSettingsInterface.javascriptAdviceToText(KParts.HtmlSettingsInterface.JavaScriptAdvice advice)'''
            return str()
        def textToJavascriptAdvice(self, text):
            '''static KParts.HtmlSettingsInterface.JavaScriptAdvice KParts.HtmlSettingsInterface.textToJavascriptAdvice(QString text)'''
            return KParts.HtmlSettingsInterface.JavaScriptAdvice()
        def setHtmlSettingsProperty(self, type, value):
            '''abstract bool KParts.HtmlSettingsInterface.setHtmlSettingsProperty(KParts.HtmlSettingsInterface.HtmlSettingsType type, QVariant value)'''
            return bool()
        def htmlSettingsProperty(self, type):
            '''abstract QVariant KParts.HtmlSettingsInterface.htmlSettingsProperty(KParts.HtmlSettingsInterface.HtmlSettingsType type)'''
            return QVariant()
    class ReadWritePart(KParts.ReadOnlyPart):
        """"""
        def __init__(self, parent = None):
            '''void KParts.ReadWritePart.__init__(QObject parent = None)'''
        def saveToUrl(self):
            '''bool KParts.ReadWritePart.saveToUrl()'''
            return bool()
        def saveFile(self):
            '''abstract bool KParts.ReadWritePart.saveFile()'''
            return bool()
        def waitSaveComplete(self):
            '''bool KParts.ReadWritePart.waitSaveComplete()'''
            return bool()
        def save(self):
            '''bool KParts.ReadWritePart.save()'''
            return bool()
        def setModified(self, modified):
            '''void KParts.ReadWritePart.setModified(bool modified)'''
        def setModified(self):
            '''void KParts.ReadWritePart.setModified()'''
        def saveAs(self, url):
            '''bool KParts.ReadWritePart.saveAs(KUrl url)'''
            return bool()
        def closeUrl(self):
            '''bool KParts.ReadWritePart.closeUrl()'''
            return bool()
        def closeUrl(self, promptToSave):
            '''bool KParts.ReadWritePart.closeUrl(bool promptToSave)'''
            return bool()
        def queryClose(self):
            '''bool KParts.ReadWritePart.queryClose()'''
            return bool()
        def isModified(self):
            '''bool KParts.ReadWritePart.isModified()'''
            return bool()
        def setReadWrite(self, readwrite = True):
            '''void KParts.ReadWritePart.setReadWrite(bool readwrite = True)'''
        def isReadWrite(self):
            '''bool KParts.ReadWritePart.isReadWrite()'''
            return bool()
    class BrowserOpenOrSaveQuestion():
        """"""
        # Enum KParts.BrowserOpenOrSaveQuestion.Result
        Save = 0
        Open = 0
        Embed = 0
        Cancel = 0
    
        # Enum KParts.BrowserOpenOrSaveQuestion.Feature
        BasicFeatures = 0
        ServiceSelection = 0
    
        def __init__(self, parent, url, mimeType):
            '''void KParts.BrowserOpenOrSaveQuestion.__init__(QWidget parent, KUrl url, QString mimeType)'''
        def __init__(self):
            '''KParts.BrowserOpenOrSaveQuestion KParts.BrowserOpenOrSaveQuestion.__init__()'''
            return KParts.BrowserOpenOrSaveQuestion()
        def selectedService(self):
            '''unknown-type KParts.BrowserOpenOrSaveQuestion.selectedService()'''
            return unknown-type()
        def askEmbedOrSave(self, flags = 0):
            '''KParts.BrowserOpenOrSaveQuestion.Result KParts.BrowserOpenOrSaveQuestion.askEmbedOrSave(int flags = 0)'''
            return KParts.BrowserOpenOrSaveQuestion.Result()
        def askOpenOrSave(self):
            '''KParts.BrowserOpenOrSaveQuestion.Result KParts.BrowserOpenOrSaveQuestion.askOpenOrSave()'''
            return KParts.BrowserOpenOrSaveQuestion.Result()
        def setFeatures(self, features):
            '''void KParts.BrowserOpenOrSaveQuestion.setFeatures(KParts.BrowserOpenOrSaveQuestion.Features features)'''
        def setSuggestedFileName(self, suggestedFileName):
            '''void KParts.BrowserOpenOrSaveQuestion.setSuggestedFileName(QString suggestedFileName)'''
    class PartBase(KXMLGUIClient):
        """"""
        # Enum KParts.PartBase.PluginLoadingMode
        DoNotLoadPlugins = 0
        LoadPlugins = 0
        LoadPluginsIfEnabled = 0
    
        def __init__(self):
            '''void KParts.PartBase.__init__()'''
        def setPluginInterfaceVersion(self, version):
            '''void KParts.PartBase.setPluginInterfaceVersion(int version)'''
        def loadPlugins(self, parent, parentGUIClient, componentData):
            '''void KParts.PartBase.loadPlugins(QObject parent, KXMLGUIClient parentGUIClient, KComponentData componentData)'''
        def setComponentData(self, componentData):
            '''void KParts.PartBase.setComponentData(KComponentData componentData)'''
        def setComponentData(self, componentData, loadPlugins):
            '''void KParts.PartBase.setComponentData(KComponentData componentData, bool loadPlugins)'''
        def partObject(self):
            '''QObject KParts.PartBase.partObject()'''
            return QObject()
        def setPartObject(self, object):
            '''void KParts.PartBase.setPartObject(QObject object)'''
    class BrowserInterface(QObject):
        """"""
        def __init__(self, parent):
            '''void KParts.BrowserInterface.__init__(QObject parent)'''
        def callMethod(self, name, argument):
            '''void KParts.BrowserInterface.callMethod(str name, QVariant argument)'''
    class BrowserExtension():
        """"""
        class PopupFlags():
            """"""
            def __init__(self):
                '''KParts.BrowserExtension.PopupFlags KParts.BrowserExtension.PopupFlags.__init__()'''
                return KParts.BrowserExtension.PopupFlags()
            def __init__(self):
                '''int KParts.BrowserExtension.PopupFlags.__init__()'''
                return int()
            def __init__(self):
                '''void KParts.BrowserExtension.PopupFlags.__init__()'''
            def __bool__(self):
                '''int KParts.BrowserExtension.PopupFlags.__bool__()'''
                return int()
            def __ne__(self, f):
                '''bool KParts.BrowserExtension.PopupFlags.__ne__(KParts.BrowserExtension.PopupFlags f)'''
                return bool()
            def __eq__(self, f):
                '''bool KParts.BrowserExtension.PopupFlags.__eq__(KParts.BrowserExtension.PopupFlags f)'''
                return bool()
            def __invert__(self):
                '''KParts.BrowserExtension.PopupFlags KParts.BrowserExtension.PopupFlags.__invert__()'''
                return KParts.BrowserExtension.PopupFlags()
            def __and__(self, mask):
                '''KParts.BrowserExtension.PopupFlags KParts.BrowserExtension.PopupFlags.__and__(int mask)'''
                return KParts.BrowserExtension.PopupFlags()
            def __xor__(self, f):
                '''KParts.BrowserExtension.PopupFlags KParts.BrowserExtension.PopupFlags.__xor__(KParts.BrowserExtension.PopupFlags f)'''
                return KParts.BrowserExtension.PopupFlags()
            def __xor__(self, f):
                '''KParts.BrowserExtension.PopupFlags KParts.BrowserExtension.PopupFlags.__xor__(int f)'''
                return KParts.BrowserExtension.PopupFlags()
            def __or__(self, f):
                '''KParts.BrowserExtension.PopupFlags KParts.BrowserExtension.PopupFlags.__or__(KParts.BrowserExtension.PopupFlags f)'''
                return KParts.BrowserExtension.PopupFlags()
            def __or__(self, f):
                '''KParts.BrowserExtension.PopupFlags KParts.BrowserExtension.PopupFlags.__or__(int f)'''
                return KParts.BrowserExtension.PopupFlags()
            def __int__(self):
                '''int KParts.BrowserExtension.PopupFlags.__int__()'''
                return int()
            def __ixor__(self, f):
                '''KParts.BrowserExtension.PopupFlags KParts.BrowserExtension.PopupFlags.__ixor__(KParts.BrowserExtension.PopupFlags f)'''
                return KParts.BrowserExtension.PopupFlags()
            def __ior__(self, f):
                '''KParts.BrowserExtension.PopupFlags KParts.BrowserExtension.PopupFlags.__ior__(KParts.BrowserExtension.PopupFlags f)'''
                return KParts.BrowserExtension.PopupFlags()
            def __iand__(self, mask):
                '''KParts.BrowserExtension.PopupFlags KParts.BrowserExtension.PopupFlags.__iand__(int mask)'''
                return KParts.BrowserExtension.PopupFlags()
    class SelectorInterface():
        """"""
        # Enum KParts.SelectorInterface.QueryMethod
        __kdevpythondocumentation_builtin_None = 0
        EntireContent = 0
        SelectedContent = 0
    
        def __init__(self):
            '''void KParts.SelectorInterface.__init__()'''
        def __init__(self):
            '''KParts.SelectorInterface KParts.SelectorInterface.__init__()'''
            return KParts.SelectorInterface()
        def querySelectorAll(self, query, method):
            '''abstract list-of-KParts.SelectorInterface.Element KParts.SelectorInterface.querySelectorAll(QString query, KParts.SelectorInterface.QueryMethod method)'''
            return [KParts.SelectorInterface.Element()]
        def querySelector(self, query, method):
            '''abstract KParts.SelectorInterface.Element KParts.SelectorInterface.querySelector(QString query, KParts.SelectorInterface.QueryMethod method)'''
            return KParts.SelectorInterface.Element()
        def supportedQueryMethods(self):
            '''KParts.SelectorInterface.QueryMethods KParts.SelectorInterface.supportedQueryMethods()'''
            return KParts.SelectorInterface.QueryMethods()
    class FileInfoExtension(QObject):
        """"""
        # Enum KParts.FileInfoExtension.QueryMode
        __kdevpythondocumentation_builtin_None = 0
        AllItems = 0
        SelectedItems = 0
    
        def __init__(self, parent):
            '''void KParts.FileInfoExtension.__init__(KParts.ReadOnlyPart parent)'''
        def queryFor(self, mode):
            '''abstract KFileItemList KParts.FileInfoExtension.queryFor(KParts.FileInfoExtension.QueryMode mode)'''
            return KFileItemList()
        def supportedQueryModes(self):
            '''KParts.FileInfoExtension.QueryModes KParts.FileInfoExtension.supportedQueryModes()'''
            return KParts.FileInfoExtension.QueryModes()
        def hasSelection(self):
            '''bool KParts.FileInfoExtension.hasSelection()'''
            return bool()
        def childObject(self, obj):
            '''static KParts.FileInfoExtension KParts.FileInfoExtension.childObject(QObject obj)'''
            return KParts.FileInfoExtension()
    class Event(QEvent):
        """"""
        def __init__(self, eventName):
            '''void KParts.Event.__init__(str eventName)'''
        def test(self, event):
            '''static bool KParts.Event.test(QEvent event)'''
            return bool()
        def test(self, event, name):
            '''static bool KParts.Event.test(QEvent event, str name)'''
            return bool()
        def eventName(self):
            '''str KParts.Event.eventName()'''
            return str()
    class MainWindow(KXmlGuiWindow, KParts.PartBase):
        """"""
        def __init__(self, parent = None, f = 0):
            '''void KParts.MainWindow.__init__(QWidget parent = None, Qt.WindowFlags f = 0)'''
        def __init__(self, parent, name = None, f = 0):
            '''void KParts.MainWindow.__init__(QWidget parent, str name = None, Qt.WindowFlags f = 0)'''
        def createShellGUI(self, create = True):
            '''void KParts.MainWindow.createShellGUI(bool create = True)'''
        def saveNewToolbarConfig(self):
            '''void KParts.MainWindow.saveNewToolbarConfig()'''
        def slotSetStatusBarText(self):
            '''QString KParts.MainWindow.slotSetStatusBarText()'''
            return QString()
        def createGUI(self, part):
            '''void KParts.MainWindow.createGUI(KParts.Part part)'''
        def configureToolbars(self):
            '''void KParts.MainWindow.configureToolbars()'''
    class BrowserExtension(QObject):
        """"""
        # Enum KParts.BrowserExtension.PopupFlag
        DefaultPopupItems = 0
        ShowNavigationItems = 0
        ShowUp = 0
        ShowReload = 0
        ShowBookmark = 0
        ShowCreateDirectory = 0
        ShowTextSelectionItems = 0
        NoDeletion = 0
        IsLink = 0
        ShowUrlOperations = 0
        ShowProperties = 0
    
        def __init__(self, parent):
            '''void KParts.BrowserExtension.__init__(KParts.ReadOnlyPart parent)'''
        def itemsRemoved(self, items):
            '''void KParts.BrowserExtension.itemsRemoved(KFileItemList items)'''
        def setPageSecurity(self):
            '''int KParts.BrowserExtension.setPageSecurity()'''
            return int()
        def requestFocus(self, part):
            '''void KParts.BrowserExtension.requestFocus(KParts.ReadOnlyPart part)'''
        def resizeTopLevelWidget(self, w, h):
            '''void KParts.BrowserExtension.resizeTopLevelWidget(int w, int h)'''
        def moveTopLevelWidget(self, x, y):
            '''void KParts.BrowserExtension.moveTopLevelWidget(int x, int y)'''
        def addWebSideBar(self, url, name):
            '''void KParts.BrowserExtension.addWebSideBar(KUrl url, QString name)'''
        def mouseOverInfo(self, item):
            '''void KParts.BrowserExtension.mouseOverInfo(KFileItem item)'''
        def selectionInfo(self, items):
            '''void KParts.BrowserExtension.selectionInfo(KFileItemList items)'''
        def selectionInfo(self, text):
            '''void KParts.BrowserExtension.selectionInfo(QString text)'''
        def selectionInfo(self, urls):
            '''void KParts.BrowserExtension.selectionInfo(KUrl.List urls)'''
        def infoMessage(self):
            '''QString KParts.BrowserExtension.infoMessage()'''
            return QString()
        def speedProgress(self, bytesPerSecond):
            '''void KParts.BrowserExtension.speedProgress(int bytesPerSecond)'''
        def loadingProgress(self, percent):
            '''void KParts.BrowserExtension.loadingProgress(int percent)'''
        def createNewWindow(self, url, arguments = None, browserArguments = None, windowArgs = None, part = None):
            '''void KParts.BrowserExtension.createNewWindow(KUrl url, KParts.OpenUrlArguments arguments = KParts.OpenUrlArguments(), KParts.BrowserArguments browserArguments = KParts.BrowserArguments(), KParts.WindowArgs windowArgs = KParts.WindowArgs(), KParts.ReadOnlyPart part)'''
        def setIconUrl(self, url):
            '''void KParts.BrowserExtension.setIconUrl(KUrl url)'''
        def setLocationBarUrl(self, url):
            '''void KParts.BrowserExtension.setLocationBarUrl(QString url)'''
        def openUrlNotify(self):
            '''void KParts.BrowserExtension.openUrlNotify()'''
        def openUrlRequestDelayed(self, url, arguments, browserArguments):
            '''void KParts.BrowserExtension.openUrlRequestDelayed(KUrl url, KParts.OpenUrlArguments arguments, KParts.BrowserArguments browserArguments)'''
        def openUrlRequest(self, url, arguments = None, browserArguments = None):
            '''void KParts.BrowserExtension.openUrlRequest(KUrl url, KParts.OpenUrlArguments arguments = KParts.OpenUrlArguments(), KParts.BrowserArguments browserArguments = KParts.BrowserArguments())'''
        def setActionText(self, name, text):
            '''void KParts.BrowserExtension.setActionText(str name, QString text)'''
        def enableAction(self, name, enabled):
            '''void KParts.BrowserExtension.enableAction(str name, bool enabled)'''
        def pasteRequest(self):
            '''void KParts.BrowserExtension.pasteRequest()'''
        def childObject(self, obj):
            '''static KParts.BrowserExtension KParts.BrowserExtension.childObject(QObject obj)'''
            return KParts.BrowserExtension()
        def actionSlotMapPtr(self):
            '''static dict-of-QByteArray-QByteArray KParts.BrowserExtension.actionSlotMapPtr()'''
            return dict-of-QByteArray-QByteArray()
        def actionSlotMap(self):
            '''static dict-of-QByteArray-QByteArray KParts.BrowserExtension.actionSlotMap()'''
            return dict-of-QByteArray-QByteArray()
        def actionText(self, name):
            '''QString KParts.BrowserExtension.actionText(str name)'''
            return QString()
        def isActionEnabled(self, name):
            '''bool KParts.BrowserExtension.isActionEnabled(str name)'''
            return bool()
        def browserInterface(self):
            '''KParts.BrowserInterface KParts.BrowserExtension.browserInterface()'''
            return KParts.BrowserInterface()
        def setBrowserInterface(self, impl):
            '''void KParts.BrowserExtension.setBrowserInterface(KParts.BrowserInterface impl)'''
        def setURLDropHandlingEnabled(self, enable):
            '''void KParts.BrowserExtension.setURLDropHandlingEnabled(bool enable)'''
        def isURLDropHandlingEnabled(self):
            '''bool KParts.BrowserExtension.isURLDropHandlingEnabled()'''
            return bool()
        def restoreState(self, stream):
            '''void KParts.BrowserExtension.restoreState(QDataStream stream)'''
        def saveState(self, stream):
            '''void KParts.BrowserExtension.saveState(QDataStream stream)'''
        def yOffset(self):
            '''int KParts.BrowserExtension.yOffset()'''
            return int()
        def xOffset(self):
            '''int KParts.BrowserExtension.xOffset()'''
            return int()
        def browserArguments(self):
            '''KParts.BrowserArguments KParts.BrowserExtension.browserArguments()'''
            return KParts.BrowserArguments()
        def setBrowserArguments(self, args):
            '''void KParts.BrowserExtension.setBrowserArguments(KParts.BrowserArguments args)'''
    class SelectorInterface():
        """"""
        class QueryMethods():
            """"""
            def __init__(self):
                '''KParts.SelectorInterface.QueryMethods KParts.SelectorInterface.QueryMethods.__init__()'''
                return KParts.SelectorInterface.QueryMethods()
            def __init__(self):
                '''int KParts.SelectorInterface.QueryMethods.__init__()'''
                return int()
            def __init__(self):
                '''void KParts.SelectorInterface.QueryMethods.__init__()'''
            def __bool__(self):
                '''int KParts.SelectorInterface.QueryMethods.__bool__()'''
                return int()
            def __ne__(self, f):
                '''bool KParts.SelectorInterface.QueryMethods.__ne__(KParts.SelectorInterface.QueryMethods f)'''
                return bool()
            def __eq__(self, f):
                '''bool KParts.SelectorInterface.QueryMethods.__eq__(KParts.SelectorInterface.QueryMethods f)'''
                return bool()
            def __invert__(self):
                '''KParts.SelectorInterface.QueryMethods KParts.SelectorInterface.QueryMethods.__invert__()'''
                return KParts.SelectorInterface.QueryMethods()
            def __and__(self, mask):
                '''KParts.SelectorInterface.QueryMethods KParts.SelectorInterface.QueryMethods.__and__(int mask)'''
                return KParts.SelectorInterface.QueryMethods()
            def __xor__(self, f):
                '''KParts.SelectorInterface.QueryMethods KParts.SelectorInterface.QueryMethods.__xor__(KParts.SelectorInterface.QueryMethods f)'''
                return KParts.SelectorInterface.QueryMethods()
            def __xor__(self, f):
                '''KParts.SelectorInterface.QueryMethods KParts.SelectorInterface.QueryMethods.__xor__(int f)'''
                return KParts.SelectorInterface.QueryMethods()
            def __or__(self, f):
                '''KParts.SelectorInterface.QueryMethods KParts.SelectorInterface.QueryMethods.__or__(KParts.SelectorInterface.QueryMethods f)'''
                return KParts.SelectorInterface.QueryMethods()
            def __or__(self, f):
                '''KParts.SelectorInterface.QueryMethods KParts.SelectorInterface.QueryMethods.__or__(int f)'''
                return KParts.SelectorInterface.QueryMethods()
            def __int__(self):
                '''int KParts.SelectorInterface.QueryMethods.__int__()'''
                return int()
            def __ixor__(self, f):
                '''KParts.SelectorInterface.QueryMethods KParts.SelectorInterface.QueryMethods.__ixor__(KParts.SelectorInterface.QueryMethods f)'''
                return KParts.SelectorInterface.QueryMethods()
            def __ior__(self, f):
                '''KParts.SelectorInterface.QueryMethods KParts.SelectorInterface.QueryMethods.__ior__(KParts.SelectorInterface.QueryMethods f)'''
                return KParts.SelectorInterface.QueryMethods()
            def __iand__(self, mask):
                '''KParts.SelectorInterface.QueryMethods KParts.SelectorInterface.QueryMethods.__iand__(int mask)'''
                return KParts.SelectorInterface.QueryMethods()
    class ScriptableExtension(QObject):
        """"""
        # Enum KParts.ScriptableExtension.ScriptLanguage
        ECMAScript = 0
        EnumLimit = 0
    
        def __init__(self, parent):
            '''void KParts.ScriptableExtension.__init__(QObject parent)'''
        def releaseValue(self, v):
            '''static QVariant KParts.ScriptableExtension.releaseValue(QVariant v)'''
            return QVariant()
        def acquireValue(self, v):
            '''static QVariant KParts.ScriptableExtension.acquireValue(QVariant v)'''
            return QVariant()
        def release(self, objid):
            '''void KParts.ScriptableExtension.release(int objid)'''
        def acquire(self, objid):
            '''void KParts.ScriptableExtension.acquire(int objid)'''
        def isScriptLanguageSupported(self, lang):
            '''bool KParts.ScriptableExtension.isScriptLanguageSupported(KParts.ScriptableExtension.ScriptLanguage lang)'''
            return bool()
        def evaluateScript(self, callerPrincipal, contextObjectId, code, language = None):
            '''QVariant KParts.ScriptableExtension.evaluateScript(KParts.ScriptableExtension callerPrincipal, int contextObjectId, QString code, KParts.ScriptableExtension.ScriptLanguage language = KParts.ScriptableExtension.ECMAScript)'''
            return QVariant()
        def setException(self, callerPrincipal, message):
            '''bool KParts.ScriptableExtension.setException(KParts.ScriptableExtension callerPrincipal, QString message)'''
            return bool()
        def enumerateProperties(self, callerPrincipal, objId, result):
            '''bool KParts.ScriptableExtension.enumerateProperties(KParts.ScriptableExtension callerPrincipal, int objId, QStringList result)'''
            return bool()
        def removeProperty(self, callerPrincipal, objId, propName):
            '''bool KParts.ScriptableExtension.removeProperty(KParts.ScriptableExtension callerPrincipal, int objId, QString propName)'''
            return bool()
        def put(self, callerPrincipal, objId, propName, value):
            '''bool KParts.ScriptableExtension.put(KParts.ScriptableExtension callerPrincipal, int objId, QString propName, QVariant value)'''
            return bool()
        def get(self, callerPrincipal, objId, propName):
            '''QVariant KParts.ScriptableExtension.get(KParts.ScriptableExtension callerPrincipal, int objId, QString propName)'''
            return QVariant()
        def hasProperty(self, callerPrincipal, objId, propName):
            '''bool KParts.ScriptableExtension.hasProperty(KParts.ScriptableExtension callerPrincipal, int objId, QString propName)'''
            return bool()
        def callAsConstructor(self, callerPrincipal, objId, args):
            '''QVariant KParts.ScriptableExtension.callAsConstructor(KParts.ScriptableExtension callerPrincipal, int objId, list-of-QVariant args)'''
            return QVariant()
        def callFunctionReference(self, callerPrincipal, objId, f, args):
            '''QVariant KParts.ScriptableExtension.callFunctionReference(KParts.ScriptableExtension callerPrincipal, int objId, QString f, list-of-QVariant args)'''
            return QVariant()
        def callAsFunction(self, callerPrincipal, objId, args):
            '''QVariant KParts.ScriptableExtension.callAsFunction(KParts.ScriptableExtension callerPrincipal, int objId, list-of-QVariant args)'''
            return QVariant()
        def enclosingObject(self):
            '''QVariant KParts.ScriptableExtension.enclosingObject()'''
            return QVariant()
        def rootObject(self):
            '''QVariant KParts.ScriptableExtension.rootObject()'''
            return QVariant()
        def host(self):
            '''KParts.ScriptableExtension KParts.ScriptableExtension.host()'''
            return KParts.ScriptableExtension()
        def setHost(self, host):
            '''void KParts.ScriptableExtension.setHost(KParts.ScriptableExtension host)'''
        def adapterFromLiveConnect(self, parentObj, oldApi):
            '''static KParts.ScriptableExtension KParts.ScriptableExtension.adapterFromLiveConnect(QObject parentObj, KParts.LiveConnectExtension oldApi)'''
            return KParts.ScriptableExtension()
        def childObject(self, obj):
            '''static KParts.ScriptableExtension KParts.ScriptableExtension.childObject(QObject obj)'''
            return KParts.ScriptableExtension()
    class BrowserOpenOrSaveQuestion():
        """"""
        class Features():
            """"""
            def __init__(self):
                '''KParts.BrowserOpenOrSaveQuestion.Features KParts.BrowserOpenOrSaveQuestion.Features.__init__()'''
                return KParts.BrowserOpenOrSaveQuestion.Features()
            def __init__(self):
                '''int KParts.BrowserOpenOrSaveQuestion.Features.__init__()'''
                return int()
            def __init__(self):
                '''void KParts.BrowserOpenOrSaveQuestion.Features.__init__()'''
            def __bool__(self):
                '''int KParts.BrowserOpenOrSaveQuestion.Features.__bool__()'''
                return int()
            def __ne__(self, f):
                '''bool KParts.BrowserOpenOrSaveQuestion.Features.__ne__(KParts.BrowserOpenOrSaveQuestion.Features f)'''
                return bool()
            def __eq__(self, f):
                '''bool KParts.BrowserOpenOrSaveQuestion.Features.__eq__(KParts.BrowserOpenOrSaveQuestion.Features f)'''
                return bool()
            def __invert__(self):
                '''KParts.BrowserOpenOrSaveQuestion.Features KParts.BrowserOpenOrSaveQuestion.Features.__invert__()'''
                return KParts.BrowserOpenOrSaveQuestion.Features()
            def __and__(self, mask):
                '''KParts.BrowserOpenOrSaveQuestion.Features KParts.BrowserOpenOrSaveQuestion.Features.__and__(int mask)'''
                return KParts.BrowserOpenOrSaveQuestion.Features()
            def __xor__(self, f):
                '''KParts.BrowserOpenOrSaveQuestion.Features KParts.BrowserOpenOrSaveQuestion.Features.__xor__(KParts.BrowserOpenOrSaveQuestion.Features f)'''
                return KParts.BrowserOpenOrSaveQuestion.Features()
            def __xor__(self, f):
                '''KParts.BrowserOpenOrSaveQuestion.Features KParts.BrowserOpenOrSaveQuestion.Features.__xor__(int f)'''
                return KParts.BrowserOpenOrSaveQuestion.Features()
            def __or__(self, f):
                '''KParts.BrowserOpenOrSaveQuestion.Features KParts.BrowserOpenOrSaveQuestion.Features.__or__(KParts.BrowserOpenOrSaveQuestion.Features f)'''
                return KParts.BrowserOpenOrSaveQuestion.Features()
            def __or__(self, f):
                '''KParts.BrowserOpenOrSaveQuestion.Features KParts.BrowserOpenOrSaveQuestion.Features.__or__(int f)'''
                return KParts.BrowserOpenOrSaveQuestion.Features()
            def __int__(self):
                '''int KParts.BrowserOpenOrSaveQuestion.Features.__int__()'''
                return int()
            def __ixor__(self, f):
                '''KParts.BrowserOpenOrSaveQuestion.Features KParts.BrowserOpenOrSaveQuestion.Features.__ixor__(KParts.BrowserOpenOrSaveQuestion.Features f)'''
                return KParts.BrowserOpenOrSaveQuestion.Features()
            def __ior__(self, f):
                '''KParts.BrowserOpenOrSaveQuestion.Features KParts.BrowserOpenOrSaveQuestion.Features.__ior__(KParts.BrowserOpenOrSaveQuestion.Features f)'''
                return KParts.BrowserOpenOrSaveQuestion.Features()
            def __iand__(self, mask):
                '''KParts.BrowserOpenOrSaveQuestion.Features KParts.BrowserOpenOrSaveQuestion.Features.__iand__(int mask)'''
                return KParts.BrowserOpenOrSaveQuestion.Features()
    class GUIActivateEvent(KParts.Event):
        """"""
        def __init__(self, activated):
            '''void KParts.GUIActivateEvent.__init__(bool activated)'''
        def test(self, event):
            '''static bool KParts.GUIActivateEvent.test(QEvent event)'''
            return bool()
        def activated(self):
            '''bool KParts.GUIActivateEvent.activated()'''
            return bool()
    class LiveConnectExtension(QObject):
        """"""
        # Enum KParts.LiveConnectExtension.Type
        TypeVoid = 0
        TypeBool = 0
        TypeFunction = 0
        TypeNumber = 0
        TypeObject = 0
        TypeString = 0
    
        def __init__(self, parent):
            '''void KParts.LiveConnectExtension.__init__(KParts.ReadOnlyPart parent)'''
        def childObject(self, obj):
            '''static KParts.LiveConnectExtension KParts.LiveConnectExtension.childObject(QObject obj)'''
            return KParts.LiveConnectExtension()
        def unregister(self, objid):
            '''void KParts.LiveConnectExtension.unregister(int objid)'''
        def call(self, objid, func, args, type, retobjid, value):
            '''bool KParts.LiveConnectExtension.call(int objid, QString func, QStringList args, KParts.LiveConnectExtension.Type type, int retobjid, QString value)'''
            return bool()
        def put(self, objid, field, value):
            '''bool KParts.LiveConnectExtension.put(int objid, QString field, QString value)'''
            return bool()
        def get(self, objid, field, type, retobjid, value):
            '''bool KParts.LiveConnectExtension.get(int objid, QString field, KParts.LiveConnectExtension.Type type, int retobjid, QString value)'''
            return bool()
    class TextExtension(QObject):
        """"""
        # Enum KParts.TextExtension.Format
        PlainText = 0
        HTML = 0
    
        def __init__(self, parent):
            '''void KParts.TextExtension.__init__(KParts.ReadOnlyPart parent)'''
        selectionChanged = pyqtSignal() # void selectionChanged() - signal
        def findText(self, string, options):
            '''bool KParts.TextExtension.findText(QString string, KFind.SearchOptions options)'''
            return bool()
        def pageText(self, format):
            '''QString KParts.TextExtension.pageText(KParts.TextExtension.Format format)'''
            return QString()
        def currentPage(self):
            '''int KParts.TextExtension.currentPage()'''
            return int()
        def pageCount(self):
            '''int KParts.TextExtension.pageCount()'''
            return int()
        def completeText(self, format):
            '''QString KParts.TextExtension.completeText(KParts.TextExtension.Format format)'''
            return QString()
        def selectedText(self, format):
            '''QString KParts.TextExtension.selectedText(KParts.TextExtension.Format format)'''
            return QString()
        def hasSelection(self):
            '''bool KParts.TextExtension.hasSelection()'''
            return bool()
        def childObject(self, obj):
            '''static KParts.TextExtension KParts.TextExtension.childObject(QObject obj)'''
            return KParts.TextExtension()
    class OpenUrlEvent(KParts.Event):
        """"""
        def __init__(self, part, url, args = None, browserArgs = None):
            '''void KParts.OpenUrlEvent.__init__(KParts.ReadOnlyPart part, KUrl url, KParts.OpenUrlArguments args = KParts.OpenUrlArguments(), KParts.BrowserArguments browserArgs = KParts.BrowserArguments())'''
        def test(self, event):
            '''static bool KParts.OpenUrlEvent.test(QEvent event)'''
            return bool()
        def browserArguments(self):
            '''KParts.BrowserArguments KParts.OpenUrlEvent.browserArguments()'''
            return KParts.BrowserArguments()
        def arguments(self):
            '''KParts.OpenUrlArguments KParts.OpenUrlEvent.arguments()'''
            return KParts.OpenUrlArguments()
        def url(self):
            '''KUrl KParts.OpenUrlEvent.url()'''
            return KUrl()
        def part(self):
            '''KParts.ReadOnlyPart KParts.OpenUrlEvent.part()'''
            return KParts.ReadOnlyPart()
    class Plugin(QObject, KXMLGUIClient):
        """"""
        def __init__(self, parent = None):
            '''void KParts.Plugin.__init__(QObject parent = None)'''
        def setComponentData(self, instance):
            '''void KParts.Plugin.setComponentData(KComponentData instance)'''
        def loadPlugin(self, parent, libname):
            '''static KParts.Plugin KParts.Plugin.loadPlugin(QObject parent, str libname)'''
            return KParts.Plugin()
        def loadPlugin(self, parent, libname):
            '''static KParts.Plugin KParts.Plugin.loadPlugin(QObject parent, QByteArray libname)'''
            return KParts.Plugin()
        def loadPlugin(self, parent, libname):
            '''static KParts.Plugin KParts.Plugin.loadPlugin(QObject parent, QString libname)'''
            return KParts.Plugin()
        def loadPlugin(self, parent, libname, keyword):
            '''static KParts.Plugin KParts.Plugin.loadPlugin(QObject parent, QString libname, QString keyword)'''
            return KParts.Plugin()
        def pluginInfos(self, instance):
            '''static list-of-KParts.Plugin.PluginInfo KParts.Plugin.pluginInfos(KComponentData instance)'''
            return [KParts.Plugin.PluginInfo()]
        def pluginObjects(self, parent):
            '''static list-of-KParts.Plugin KParts.Plugin.pluginObjects(QObject parent)'''
            return [KParts.Plugin()]
        def loadPlugins(self, parent, instance):
            '''static void KParts.Plugin.loadPlugins(QObject parent, KComponentData instance)'''
        def loadPlugins(self, parent, pluginInfos):
            '''static void KParts.Plugin.loadPlugins(QObject parent, list-of-KParts.Plugin.PluginInfo pluginInfos)'''
        def loadPlugins(self, parent, pluginInfos, instance):
            '''static void KParts.Plugin.loadPlugins(QObject parent, list-of-KParts.Plugin.PluginInfo pluginInfos, KComponentData instance)'''
        def loadPlugins(self, parent, parentGUIClient, instance, enableNewPluginsByDefault = True, interfaceVersionRequired = 0):
            '''static void KParts.Plugin.loadPlugins(QObject parent, KXMLGUIClient parentGUIClient, KComponentData instance, bool enableNewPluginsByDefault = True, int interfaceVersionRequired = 0)'''
        def localXMLFile(self):
            '''QString KParts.Plugin.localXMLFile()'''
            return QString()
        def xmlFile(self):
            '''QString KParts.Plugin.xmlFile()'''
            return QString()
    class BrowserRun(KRun):
        """"""
        # Enum KParts.BrowserRun.NonEmbeddableResult
        Handled = 0
        NotHandled = 0
        Delayed = 0
    
        # Enum KParts.BrowserRun.AskEmbedOrSaveFlags
        InlineDisposition = 0
        AttachmentDisposition = 0
    
        # Enum KParts.BrowserRun.AskSaveResult
        Save = 0
        Open = 0
        Cancel = 0
    
        def __init__(self, url, args, browserArgs, part, window, removeReferrer, trustedSource, hideErrorDialog = False):
            '''void KParts.BrowserRun.__init__(KUrl url, KParts.OpenUrlArguments args, KParts.BrowserArguments browserArgs, KParts.ReadOnlyPart part, QWidget window, bool removeReferrer, bool trustedSource, bool hideErrorDialog = False)'''
        def makeErrorUrl(self, error, errorText, initialUrl):
            '''static KUrl KParts.BrowserRun.makeErrorUrl(int error, QString errorText, QString initialUrl)'''
            return KUrl()
        def handleNonEmbeddable(self, mimeType, pSelectedService):
            '''KParts.BrowserRun.NonEmbeddableResult KParts.BrowserRun.handleNonEmbeddable(QString mimeType, unknown-type pSelectedService)'''
            return KParts.BrowserRun.NonEmbeddableResult()
        def saveUrlUsingKIO(self, srcUrl, destUrl, window, metaData):
            '''static void KParts.BrowserRun.saveUrlUsingKIO(KUrl srcUrl, KUrl destUrl, QWidget window, dict-of-QString-QString metaData)'''
        def saveUrl(self, url, suggestedFileName, window, args):
            '''static void KParts.BrowserRun.saveUrl(KUrl url, QString suggestedFileName, QWidget window, KParts.OpenUrlArguments args)'''
        def slotStatResult(self, job):
            '''void KParts.BrowserRun.slotStatResult(KJob job)'''
        def slotCopyToTempFileResult(self, job):
            '''void KParts.BrowserRun.slotCopyToTempFileResult(KJob job)'''
        def slotBrowserMimetype(self, job, type):
            '''void KParts.BrowserRun.slotBrowserMimetype(KIO.Job job, QString type)'''
        def slotBrowserScanFinished(self, job):
            '''void KParts.BrowserRun.slotBrowserScanFinished(KJob job)'''
        def handleError(self, job):
            '''void KParts.BrowserRun.handleError(KJob job)'''
        def init(self):
            '''void KParts.BrowserRun.init()'''
        def scanFile(self):
            '''void KParts.BrowserRun.scanFile()'''
        def isTextExecutable(self, mimeType):
            '''static bool KParts.BrowserRun.isTextExecutable(QString mimeType)'''
            return bool()
        def allowExecution(self, mimeType, url):
            '''static bool KParts.BrowserRun.allowExecution(QString mimeType, KUrl url)'''
            return bool()
        def simpleSave(self, url, suggestedFileName, window = None):
            '''static void KParts.BrowserRun.simpleSave(KUrl url, QString suggestedFileName, QWidget window = None)'''
        def save(self, url, suggestedFileName):
            '''void KParts.BrowserRun.save(KUrl url, QString suggestedFileName)'''
        def askEmbedOrSave(self, url, mimeType, suggestedFileName = QString(), flags = 0):
            '''static KParts.BrowserRun.AskSaveResult KParts.BrowserRun.askEmbedOrSave(KUrl url, QString mimeType, QString suggestedFileName = QString(), int flags = 0)'''
            return KParts.BrowserRun.AskSaveResult()
        def askSave(self, url, offer, mimeType, suggestedFileName = QString()):
            '''static KParts.BrowserRun.AskSaveResult KParts.BrowserRun.askSave(KUrl url, unknown-type offer, QString mimeType, QString suggestedFileName = QString())'''
            return KParts.BrowserRun.AskSaveResult()
        def serverSuggestsSave(self):
            '''bool KParts.BrowserRun.serverSuggestsSave()'''
            return bool()
        def contentDisposition(self):
            '''QString KParts.BrowserRun.contentDisposition()'''
            return QString()
        def hideErrorDialog(self):
            '''bool KParts.BrowserRun.hideErrorDialog()'''
            return bool()
        def url(self):
            '''KUrl KParts.BrowserRun.url()'''
            return KUrl()
        def part(self):
            '''KParts.ReadOnlyPart KParts.BrowserRun.part()'''
            return KParts.ReadOnlyPart()
        def browserArguments(self):
            '''KParts.BrowserArguments KParts.BrowserRun.browserArguments()'''
            return KParts.BrowserArguments()
        def arguments(self):
            '''KParts.OpenUrlArguments KParts.BrowserRun.arguments()'''
            return KParts.OpenUrlArguments()
    class PartManager(QObject):
        """"""
        # Enum KParts.PartManager.Reason
        ReasonLeftClick = 0
        ReasonMidClick = 0
        ReasonRightClick = 0
        NoReason = 0
    
        # Enum KParts.PartManager.SelectionPolicy
        Direct = 0
        TriState = 0
    
        def __init__(self, parent):
            '''void KParts.PartManager.__init__(QWidget parent)'''
        def __init__(self, topLevel, parent):
            '''void KParts.PartManager.__init__(QWidget topLevel, QObject parent)'''
        def slotManagedTopLevelWidgetDestroyed(self):
            '''void KParts.PartManager.slotManagedTopLevelWidgetDestroyed()'''
        def slotWidgetDestroyed(self):
            '''void KParts.PartManager.slotWidgetDestroyed()'''
        def slotObjectDestroyed(self):
            '''void KParts.PartManager.slotObjectDestroyed()'''
        def setActiveComponent(self, instance):
            '''void KParts.PartManager.setActiveComponent(KComponentData instance)'''
        activePartChanged = pyqtSignal() # void activePartChanged(KParts::Part *) - signal
        partRemoved = pyqtSignal() # void partRemoved(KParts::Part *) - signal
        partAdded = pyqtSignal() # void partAdded(KParts::Part *) - signal
        def reason(self):
            '''int KParts.PartManager.reason()'''
            return int()
        def removeManagedTopLevelWidget(self, topLevel):
            '''void KParts.PartManager.removeManagedTopLevelWidget(QWidget topLevel)'''
        def addManagedTopLevelWidget(self, topLevel):
            '''void KParts.PartManager.addManagedTopLevelWidget(QWidget topLevel)'''
        def parts(self):
            '''list-of-KParts.Part KParts.PartManager.parts()'''
            return [KParts.Part()]
        def selectedWidget(self):
            '''QWidget KParts.PartManager.selectedWidget()'''
            return QWidget()
        def selectedPart(self):
            '''KParts.Part KParts.PartManager.selectedPart()'''
            return KParts.Part()
        def setSelectedPart(self, part, widget = None):
            '''void KParts.PartManager.setSelectedPart(KParts.Part part, QWidget widget = None)'''
        def activeWidget(self):
            '''QWidget KParts.PartManager.activeWidget()'''
            return QWidget()
        def activePart(self):
            '''KParts.Part KParts.PartManager.activePart()'''
            return KParts.Part()
        def setActivePart(self, part, widget = None):
            '''void KParts.PartManager.setActivePart(KParts.Part part, QWidget widget = None)'''
        def replacePart(self, oldPart, newPart, setActive = True):
            '''void KParts.PartManager.replacePart(KParts.Part oldPart, KParts.Part newPart, bool setActive = True)'''
        def removePart(self, part):
            '''void KParts.PartManager.removePart(KParts.Part part)'''
        def addPart(self, part, setActive = True):
            '''void KParts.PartManager.addPart(KParts.Part part, bool setActive = True)'''
        def eventFilter(self, obj, ev):
            '''bool KParts.PartManager.eventFilter(QObject obj, QEvent ev)'''
            return bool()
        def activationButtonMask(self):
            '''int KParts.PartManager.activationButtonMask()'''
            return int()
        def setActivationButtonMask(self, buttonMask):
            '''void KParts.PartManager.setActivationButtonMask(int buttonMask)'''
        def ignoreScrollBars(self):
            '''bool KParts.PartManager.ignoreScrollBars()'''
            return bool()
        def setIgnoreScrollBars(self, ignore):
            '''void KParts.PartManager.setIgnoreScrollBars(bool ignore)'''
        def allowNestedParts(self):
            '''bool KParts.PartManager.allowNestedParts()'''
            return bool()
        def setAllowNestedParts(self, allow):
            '''void KParts.PartManager.setAllowNestedParts(bool allow)'''
        def selectionPolicy(self):
            '''KParts.PartManager.SelectionPolicy KParts.PartManager.selectionPolicy()'''
            return KParts.PartManager.SelectionPolicy()
        def setSelectionPolicy(self, policy):
            '''void KParts.PartManager.setSelectionPolicy(KParts.PartManager.SelectionPolicy policy)'''
    class PartActivateEvent(KParts.Event):
        """"""
        def __init__(self, activated, part, widget):
            '''void KParts.PartActivateEvent.__init__(bool activated, KParts.Part part, QWidget widget)'''
        def test(self, event):
            '''static bool KParts.PartActivateEvent.test(QEvent event)'''
            return bool()
        def widget(self):
            '''QWidget KParts.PartActivateEvent.widget()'''
            return QWidget()
        def part(self):
            '''KParts.Part KParts.PartActivateEvent.part()'''
            return KParts.Part()
        def activated(self):
            '''bool KParts.PartActivateEvent.activated()'''
            return bool()
    class ReadOnlyPart(KParts.Part):
        """"""
        def __init__(self, parent = None):
            '''void KParts.ReadOnlyPart.__init__(QObject parent = None)'''
        def setLocalFilePath(self, localFilePath):
            '''void KParts.ReadOnlyPart.setLocalFilePath(QString localFilePath)'''
        def localFilePath(self):
            '''QString KParts.ReadOnlyPart.localFilePath()'''
            return QString()
        def setUrl(self, url):
            '''void KParts.ReadOnlyPart.setUrl(KUrl url)'''
        def setLocalFileTemporary(self, temp):
            '''void KParts.ReadOnlyPart.setLocalFileTemporary(bool temp)'''
        def isLocalFileTemporary(self):
            '''bool KParts.ReadOnlyPart.isLocalFileTemporary()'''
            return bool()
        def guiActivateEvent(self, event):
            '''void KParts.ReadOnlyPart.guiActivateEvent(KParts.GUIActivateEvent event)'''
        def abortLoad(self):
            '''void KParts.ReadOnlyPart.abortLoad()'''
        def openFile(self):
            '''abstract bool KParts.ReadOnlyPart.openFile()'''
            return bool()
        canceled = pyqtSignal() # void canceled(const QStringamp;) - signal
        completed = pyqtSignal() # void completed() - signal
        completed = pyqtSignal() # void completed(bool) - signal
        started = pyqtSignal() # void started(KIO::Job *) - signal
        def closeStream(self):
            '''bool KParts.ReadOnlyPart.closeStream()'''
            return bool()
        def writeStream(self, data):
            '''bool KParts.ReadOnlyPart.writeStream(QByteArray data)'''
            return bool()
        def openStream(self, mimeType, url):
            '''bool KParts.ReadOnlyPart.openStream(QString mimeType, KUrl url)'''
            return bool()
        def arguments(self):
            '''KParts.OpenUrlArguments KParts.ReadOnlyPart.arguments()'''
            return KParts.OpenUrlArguments()
        def setArguments(self, arguments):
            '''void KParts.ReadOnlyPart.setArguments(KParts.OpenUrlArguments arguments)'''
        def browserExtension(self):
            '''KParts.BrowserExtension KParts.ReadOnlyPart.browserExtension()'''
            return KParts.BrowserExtension()
        def closeUrl(self):
            '''bool KParts.ReadOnlyPart.closeUrl()'''
            return bool()
        def url(self):
            '''KUrl KParts.ReadOnlyPart.url()'''
            return KUrl()
        def openUrl(self, url):
            '''bool KParts.ReadOnlyPart.openUrl(KUrl url)'''
            return bool()
        def showProgressInfo(self, show):
            '''void KParts.ReadOnlyPart.showProgressInfo(bool show)'''
        def isProgressInfoEnabled(self):
            '''bool KParts.ReadOnlyPart.isProgressInfoEnabled()'''
            return bool()
        def setProgressInfoEnabled(self, show):
            '''void KParts.ReadOnlyPart.setProgressInfoEnabled(bool show)'''
    class Part(QObject, KParts.PartBase):
        """"""
        def __init__(self, parent = None):
            '''void KParts.Part.__init__(QObject parent = None)'''
        def slotWidgetDestroyed(self):
            '''void KParts.Part.slotWidgetDestroyed()'''
        def loadPlugins(self):
            '''void KParts.Part.loadPlugins()'''
        def hostContainer(self, containerName):
            '''QWidget KParts.Part.hostContainer(QString containerName)'''
            return QWidget()
        def guiActivateEvent(self, event):
            '''void KParts.Part.guiActivateEvent(KParts.GUIActivateEvent event)'''
        def partSelectEvent(self, event):
            '''void KParts.Part.partSelectEvent(KParts.PartSelectEvent event)'''
        def partActivateEvent(self, event):
            '''void KParts.Part.partActivateEvent(KParts.PartActivateEvent event)'''
        def customEvent(self, event):
            '''void KParts.Part.customEvent(QEvent event)'''
        def setWidget(self, widget):
            '''void KParts.Part.setWidget(QWidget widget)'''
        setStatusBarText = pyqtSignal() # void setStatusBarText(const QStringamp;) - signal
        setWindowCaption = pyqtSignal() # void setWindowCaption(const QStringamp;) - signal
        def iconLoader(self):
            '''KIconLoader KParts.Part.iconLoader()'''
            return KIconLoader()
        def isSelectable(self):
            '''bool KParts.Part.isSelectable()'''
            return bool()
        def setSelectable(self, selectable):
            '''void KParts.Part.setSelectable(bool selectable)'''
        def hitTest(self, widget, globalPos):
            '''KParts.Part KParts.Part.hitTest(QWidget widget, QPoint globalPos)'''
            return KParts.Part()
        def setAutoDeletePart(self, autoDeletePart):
            '''void KParts.Part.setAutoDeletePart(bool autoDeletePart)'''
        def setAutoDeleteWidget(self, autoDeleteWidget):
            '''void KParts.Part.setAutoDeleteWidget(bool autoDeleteWidget)'''
        def manager(self):
            '''KParts.PartManager KParts.Part.manager()'''
            return KParts.PartManager()
        def setManager(self, manager):
            '''void KParts.Part.setManager(KParts.PartManager manager)'''
        def widget(self):
            '''QWidget KParts.Part.widget()'''
            return QWidget()
        def embed(self, parentWidget):
            '''void KParts.Part.embed(QWidget parentWidget)'''
    class BrowserHostExtension(QObject):
        """"""
        def __init__(self, parent):
            '''void KParts.BrowserHostExtension.__init__(KParts.ReadOnlyPart parent)'''
        def childObject(self, obj):
            '''static KParts.BrowserHostExtension KParts.BrowserHostExtension.childObject(QObject obj)'''
            return KParts.BrowserHostExtension()
        def openUrlInFrame(self, url, arguments, browserArguments):
            '''bool KParts.BrowserHostExtension.openUrlInFrame(KUrl url, KParts.OpenUrlArguments arguments, KParts.BrowserArguments browserArguments)'''
            return bool()
        def findFrameParent(self, callingPart, frame):
            '''KParts.BrowserHostExtension KParts.BrowserHostExtension.findFrameParent(KParts.ReadOnlyPart callingPart, QString frame)'''
            return KParts.BrowserHostExtension()
        def frames(self):
            '''list-of-KParts.ReadOnlyPart KParts.BrowserHostExtension.frames()'''
            return [KParts.ReadOnlyPart()]
        def frameNames(self):
            '''QStringList KParts.BrowserHostExtension.frameNames()'''
            return QStringList()
    class HistoryProvider(QObject):
        """"""
        def __init__(self, parent = None):
            '''void KParts.HistoryProvider.__init__(QObject parent = None)'''
        def exists(self):
            '''static bool KParts.HistoryProvider.exists()'''
            return bool()
        inserted = pyqtSignal() # void inserted(const QStringamp;) - signal
        updated = pyqtSignal() # void updated(const QStringListamp;) - signal
        cleared = pyqtSignal() # void cleared() - signal
        def clear(self):
            '''void KParts.HistoryProvider.clear()'''
        def remove(self, item):
            '''void KParts.HistoryProvider.remove(QString item)'''
        def insert(self, item):
            '''void KParts.HistoryProvider.insert(QString item)'''
        def contains(self, item):
            '''bool KParts.HistoryProvider.contains(QString item)'''
            return bool()
        def self(self):
            '''static KParts.HistoryProvider KParts.HistoryProvider.self()'''
            return KParts.HistoryProvider()
    class Factory(KPluginFactory):
        """"""
        def __init__(self, parent = None):
            '''void KParts.Factory.__init__(QObject parent = None)'''
        def createPartObject(self, parentWidget = None, parent = None, classname = None, args = QStringList()):
            '''abstract KParts.Part KParts.Factory.createPartObject(QWidget parentWidget = None, QObject parent = None, str classname = KParts::Part, QStringList args = QStringList())'''
            return KParts.Part()
        def partComponentDataFromLibrary(self, libraryName):
            '''static KComponentData KParts.Factory.partComponentDataFromLibrary(QString libraryName)'''
            return KComponentData()
        def partComponentData(self):
            '''KComponentData KParts.Factory.partComponentData()'''
            return KComponentData()
        def createPart(self, parentWidget = None, parent = None, classname = None, args = QStringList()):
            '''KParts.Part KParts.Factory.createPart(QWidget parentWidget = None, QObject parent = None, str classname = KParts::Part, QStringList args = QStringList())'''
            return KParts.Part()
    class StatusBarExtension(QObject):
        """"""
        def __init__(self, parent):
            '''void KParts.StatusBarExtension.__init__(KParts.ReadOnlyPart parent)'''
        def eventFilter(self, watched, ev):
            '''bool KParts.StatusBarExtension.eventFilter(QObject watched, QEvent ev)'''
            return bool()
        def childObject(self, obj):
            '''static KParts.StatusBarExtension KParts.StatusBarExtension.childObject(QObject obj)'''
            return KParts.StatusBarExtension()
        def setStatusBar(self, status):
            '''void KParts.StatusBarExtension.setStatusBar(KStatusBar status)'''
        def statusBar(self):
            '''KStatusBar KParts.StatusBarExtension.statusBar()'''
            return KStatusBar()
        def removeStatusBarItem(self, widget):
            '''void KParts.StatusBarExtension.removeStatusBarItem(QWidget widget)'''
        def addStatusBarItem(self, widget, stretch, permanent):
            '''void KParts.StatusBarExtension.addStatusBarItem(QWidget widget, int stretch, bool permanent)'''
    class BrowserArguments():
        """"""
        docState = None # QStringList - member
        frameName = None # QString - member
        postData = None # QByteArray - member
        softReload = None # bool - member
        trustedSource = None # bool - member
        def __init__(self):
            '''void KParts.BrowserArguments.__init__()'''
        def __init__(self, args):
            '''void KParts.BrowserArguments.__init__(KParts.BrowserArguments args)'''
    class WindowArgs():
        """"""
        def __init__(self):
            '''void KParts.WindowArgs.__init__()'''
        def __init__(self, args):
            '''void KParts.WindowArgs.__init__(KParts.WindowArgs args)'''
        def __init__(self, _geometry, _fullscreen, _menuBarVisible, _toolBarsVisible, _statusBarVisible, _resizable):
            '''void KParts.WindowArgs.__init__(QRect _geometry, bool _fullscreen, bool _menuBarVisible, bool _toolBarsVisible, bool _statusBarVisible, bool _resizable)'''
        def __init__(self, _x, _y, _width, _height, _fullscreen, _menuBarVisible, _toolBarsVisible, _statusBarVisible, _resizable):
            '''void KParts.WindowArgs.__init__(int _x, int _y, int _width, int _height, bool _fullscreen, bool _menuBarVisible, bool _toolBarsVisible, bool _statusBarVisible, bool _resizable)'''
        def scrollBarsVisible(self):
            '''bool KParts.WindowArgs.scrollBarsVisible()'''
            return bool()
        def setScrollBarsVisible(self, visible):
            '''void KParts.WindowArgs.setScrollBarsVisible(bool visible)'''
        def lowerWindow(self):
            '''bool KParts.WindowArgs.lowerWindow()'''
            return bool()
        def setLowerWindow(self, lower):
            '''void KParts.WindowArgs.setLowerWindow(bool lower)'''
        def isResizable(self):
            '''bool KParts.WindowArgs.isResizable()'''
            return bool()
        def setResizable(self, resizable):
            '''void KParts.WindowArgs.setResizable(bool resizable)'''
        def isStatusBarVisible(self):
            '''bool KParts.WindowArgs.isStatusBarVisible()'''
            return bool()
        def setStatusBarVisible(self, visible):
            '''void KParts.WindowArgs.setStatusBarVisible(bool visible)'''
        def toolBarsVisible(self):
            '''bool KParts.WindowArgs.toolBarsVisible()'''
            return bool()
        def setToolBarsVisible(self, visible):
            '''void KParts.WindowArgs.setToolBarsVisible(bool visible)'''
        def isMenuBarVisible(self):
            '''bool KParts.WindowArgs.isMenuBarVisible()'''
            return bool()
        def setMenuBarVisible(self, visible):
            '''void KParts.WindowArgs.setMenuBarVisible(bool visible)'''
        def isFullScreen(self):
            '''bool KParts.WindowArgs.isFullScreen()'''
            return bool()
        def setFullScreen(self, fs):
            '''void KParts.WindowArgs.setFullScreen(bool fs)'''
        def height(self):
            '''int KParts.WindowArgs.height()'''
            return int()
        def setHeight(self, h):
            '''void KParts.WindowArgs.setHeight(int h)'''
        def width(self):
            '''int KParts.WindowArgs.width()'''
            return int()
        def setWidth(self, w):
            '''void KParts.WindowArgs.setWidth(int w)'''
        def y(self):
            '''int KParts.WindowArgs.y()'''
            return int()
        def setY(self, y):
            '''void KParts.WindowArgs.setY(int y)'''
        def x(self):
            '''int KParts.WindowArgs.x()'''
            return int()
        def setX(self, x):
            '''void KParts.WindowArgs.setX(int x)'''
    class OpenUrlArguments():
        """"""
        def __init__(self):
            '''void KParts.OpenUrlArguments.__init__()'''
        def __init__(self, other):
            '''void KParts.OpenUrlArguments.__init__(KParts.OpenUrlArguments other)'''
        def metaData(self):
            '''dict-of-QString-QString KParts.OpenUrlArguments.metaData()'''
            return dict-of-QString-QString()
        def setActionRequestedByUser(self, userRequested):
            '''void KParts.OpenUrlArguments.setActionRequestedByUser(bool userRequested)'''
        def actionRequestedByUser(self):
            '''bool KParts.OpenUrlArguments.actionRequestedByUser()'''
            return bool()
        def setMimeType(self, mime):
            '''void KParts.OpenUrlArguments.setMimeType(QString mime)'''
        def mimeType(self):
            '''QString KParts.OpenUrlArguments.mimeType()'''
            return QString()
        def setYOffset(self, y):
            '''void KParts.OpenUrlArguments.setYOffset(int y)'''
        def yOffset(self):
            '''int KParts.OpenUrlArguments.yOffset()'''
            return int()
        def setXOffset(self, x):
            '''void KParts.OpenUrlArguments.setXOffset(int x)'''
        def xOffset(self):
            '''int KParts.OpenUrlArguments.xOffset()'''
            return int()
        def setReload(self, b):
            '''void KParts.OpenUrlArguments.setReload(bool b)'''
        def reload(self):
            '''bool KParts.OpenUrlArguments.reload()'''
            return bool()
    class SelectorInterface():
        """"""
        class Element():
            """"""
            def __init__(self):
                '''void KParts.SelectorInterface.Element.__init__()'''
            def __init__(self, other):
                '''void KParts.SelectorInterface.Element.__init__(KParts.SelectorInterface.Element other)'''
            def swap(self, other):
                '''void KParts.SelectorInterface.Element.swap(KParts.SelectorInterface.Element other)'''
            def hasAttribute(self, name):
                '''bool KParts.SelectorInterface.Element.hasAttribute(QString name)'''
                return bool()
            def attribute(self, name, defaultValue = QString()):
                '''QString KParts.SelectorInterface.Element.attribute(QString name, QString defaultValue = QString())'''
                return QString()
            def attributeNames(self):
                '''QStringList KParts.SelectorInterface.Element.attributeNames()'''
                return QStringList()
            def setAttribute(self, name, value):
                '''void KParts.SelectorInterface.Element.setAttribute(QString name, QString value)'''
            def tagName(self):
                '''QString KParts.SelectorInterface.Element.tagName()'''
                return QString()
            def setTagName(self, tag):
                '''void KParts.SelectorInterface.Element.setTagName(QString tag)'''
            def isNull(self):
                '''bool KParts.SelectorInterface.Element.isNull()'''
                return bool()


def qSwap(lhs, rhs):
    '''static void qSwap(KParts.SelectorInterface.Element lhs, KParts.SelectorInterface.Element rhs)'''


