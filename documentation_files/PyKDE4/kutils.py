class pyqtSignal():
 def connect(self, targetSignal): pass
 def emit(self, *args): pass
from QtCore import *

class KSettings():
    """"""
    class Dispatcher():
        """"""
        def syncConfiguration(self):
            '''static void KSettings.Dispatcher.syncConfiguration()'''
        def reparseConfiguration(self, componentName):
            '''static void KSettings.Dispatcher.reparseConfiguration(QString componentName)'''
        def componentNames(self):
            '''static list-of-QString KSettings.Dispatcher.componentNames()'''
            return [QString()]
        def configForComponentName(self, componentName):
            '''static unknown-type KSettings.Dispatcher.configForComponentName(QString componentName)'''
            return unknown-type()
        def registerComponent(self, componentData, recv, slot):
            '''static void KSettings.Dispatcher.registerComponent(KComponentData componentData, QObject recv, str slot)'''
    class PluginPage(KCModule):
        """"""
        def __init__(self, componentData, parent = None, args = QVariantList()):
            '''void KSettings.PluginPage.__init__(KComponentData componentData, QWidget parent = None, list-of-QVariant args = QVariantList())'''
        def defaults(self):
            '''void KSettings.PluginPage.defaults()'''
        def save(self):
            '''void KSettings.PluginPage.save()'''
        def load(self):
            '''void KSettings.PluginPage.load()'''
        def pluginSelector(self):
            '''KPluginSelector KSettings.PluginPage.pluginSelector()'''
            return KPluginSelector()
    class Dialog(KCMultiDialog):
        """"""
        def __init__(self, parent = None):
            '''void KSettings.Dialog.__init__(QWidget parent = None)'''
        def __init__(self, components, parent = None):
            '''void KSettings.Dialog.__init__(QStringList components, QWidget parent = None)'''
        pluginSelectionChanged = pyqtSignal() # void pluginSelectionChanged() - signal
        def showEvent(self):
            '''QShowEvent KSettings.Dialog.showEvent()'''
            return QShowEvent()
        def pluginInfos(self):
            '''list-of-KPluginInfo KSettings.Dialog.pluginInfos()'''
            return [KPluginInfo()]
        def allowComponentSelection(self):
            '''bool KSettings.Dialog.allowComponentSelection()'''
            return bool()
        def setAllowComponentSelection(self, allowSelection):
            '''void KSettings.Dialog.setAllowComponentSelection(bool allowSelection)'''
        def setComponentBlacklist(self, blacklist):
            '''void KSettings.Dialog.setComponentBlacklist(QStringList blacklist)'''
        def setKCMArguments(self, arguments):
            '''void KSettings.Dialog.setKCMArguments(QStringList arguments)'''
        def addPluginInfos(self, plugininfos):
            '''void KSettings.Dialog.addPluginInfos(list-of-KPluginInfo plugininfos)'''


class KCMultiDialog(KPageDialog):
    """"""
    def __init__(self, parent = None):
        '''void KCMultiDialog.__init__(QWidget parent = None)'''
    def __init__(self, pageWidget, parent, flags = 0):
        '''void KCMultiDialog.__init__(KPageWidget pageWidget, QWidget parent, Qt.WindowFlags flags = 0)'''
    def setButtons(self, buttonMask):
        '''void KCMultiDialog.setButtons(KDialog.ButtonCodes buttonMask)'''
    def slotHelpClicked(self):
        '''void KCMultiDialog.slotHelpClicked()'''
    def slotOkClicked(self):
        '''void KCMultiDialog.slotOkClicked()'''
    def slotApplyClicked(self):
        '''void KCMultiDialog.slotApplyClicked()'''
    def slotUser1Clicked(self):
        '''void KCMultiDialog.slotUser1Clicked()'''
    def slotDefaultClicked(self):
        '''void KCMultiDialog.slotDefaultClicked()'''
    configCommitted = pyqtSignal() # void configCommitted() - signal
    configCommitted = pyqtSignal() # void configCommitted(const QByteArrayamp;) - signal
    def clear(self):
        '''void KCMultiDialog.clear()'''
    def addModule(self, module, args = QStringList()):
        '''KPageWidgetItem KCMultiDialog.addModule(QString module, QStringList args = QStringList())'''
        return KPageWidgetItem()
    def addModule(self, moduleinfo, parent = None, args = QStringList()):
        '''KPageWidgetItem KCMultiDialog.addModule(KCModuleInfo moduleinfo, KPageWidgetItem parent = None, QStringList args = QStringList())'''
        return KPageWidgetItem()


class KCModuleInfo():
    """"""
    def __init__(self, desktopFile):
        '''void KCModuleInfo.__init__(QString desktopFile)'''
    def __init__(self, moduleInfo):
        '''void KCModuleInfo.__init__(unknown-type moduleInfo)'''
    def __init__(self, rhs):
        '''void KCModuleInfo.__init__(KCModuleInfo rhs)'''
    def __init__(self):
        '''void KCModuleInfo.__init__()'''
    def weight(self):
        '''int KCModuleInfo.weight()'''
        return int()
    def handle(self):
        '''QString KCModuleInfo.handle()'''
        return QString()
    def library(self):
        '''QString KCModuleInfo.library()'''
        return QString()
    def docPath(self):
        '''QString KCModuleInfo.docPath()'''
        return QString()
    def icon(self):
        '''QString KCModuleInfo.icon()'''
        return QString()
    def comment(self):
        '''QString KCModuleInfo.comment()'''
        return QString()
    def service(self):
        '''unknown-type KCModuleInfo.service()'''
        return unknown-type()
    def moduleName(self):
        '''QString KCModuleInfo.moduleName()'''
        return QString()
    def keywords(self):
        '''QStringList KCModuleInfo.keywords()'''
        return QStringList()
    def fileName(self):
        '''QString KCModuleInfo.fileName()'''
        return QString()
    def __ne__(self, rhs):
        '''bool KCModuleInfo.__ne__(KCModuleInfo rhs)'''
        return bool()
    def __eq__(self, rhs):
        '''bool KCModuleInfo.__eq__(KCModuleInfo rhs)'''
        return bool()


class KCModuleLoader():
    """"""
    # Enum KCModuleLoader.ErrorReporting
    __kdevpythondocumentation_builtin_None = 0
    Inline = 0
    Dialog = 0
    Both = 0

    def reportError(self, report, text, details, parent):
        '''static KCModule KCModuleLoader.reportError(KCModuleLoader.ErrorReporting report, QString text, QString details, QWidget parent)'''
        return KCModule()
    def showLastLoaderError(self, parent):
        '''static void KCModuleLoader.showLastLoaderError(QWidget parent)'''
    def unloadModule(self, mod):
        '''static void KCModuleLoader.unloadModule(KCModuleInfo mod)'''
    def loadModule(self, module, report, parent = None, args = QStringList()):
        '''static KCModule KCModuleLoader.loadModule(KCModuleInfo module, KCModuleLoader.ErrorReporting report, QWidget parent = None, QStringList args = QStringList())'''
        return KCModule()
    def loadModule(self, module, report, parent = None, args = QStringList()):
        '''static KCModule KCModuleLoader.loadModule(QString module, KCModuleLoader.ErrorReporting report, QWidget parent = None, QStringList args = QStringList())'''
        return KCModule()


class KCModuleProxy(QWidget):
    """"""
    def __init__(self, info, parent = None, args = QStringList()):
        '''void KCModuleProxy.__init__(KCModuleInfo info, QWidget parent = None, QStringList args = QStringList())'''
    def __init__(self, serviceName, parent = None, args = QStringList()):
        '''void KCModuleProxy.__init__(QString serviceName, QWidget parent = None, QStringList args = QStringList())'''
    def __init__(self, service, parent = None, args = QStringList()):
        '''void KCModuleProxy.__init__(unknown-type service, QWidget parent = None, QStringList args = QStringList())'''
    def showEvent(self):
        '''QShowEvent KCModuleProxy.showEvent()'''
        return QShowEvent()
    quickHelpChanged = pyqtSignal() # void quickHelpChanged() - signal
    childClosed = pyqtSignal() # void childClosed() - signal
    def deleteClient(self):
        '''void KCModuleProxy.deleteClient()'''
    def defaults(self):
        '''void KCModuleProxy.defaults()'''
    def minimumSizeHint(self):
        '''QSize KCModuleProxy.minimumSizeHint()'''
        return QSize()
    def dbusPath(self):
        '''QString KCModuleProxy.dbusPath()'''
        return QString()
    def dbusService(self):
        '''QString KCModuleProxy.dbusService()'''
        return QString()
    def moduleInfo(self):
        '''KCModuleInfo KCModuleProxy.moduleInfo()'''
        return KCModuleInfo()
    def realModule(self):
        '''KCModule KCModuleProxy.realModule()'''
        return KCModule()
    def changed(self):
        '''bool KCModuleProxy.changed()'''
        return bool()
    changed = pyqtSignal() # void changed(bool) - signal
    changed = pyqtSignal() # void changed(KCModuleProxy *) - signal
    def componentData(self):
        '''KComponentData KCModuleProxy.componentData()'''
        return KComponentData()
    def useRootOnlyMessage(self):
        '''bool KCModuleProxy.useRootOnlyMessage()'''
        return bool()
    def rootOnlyMessage(self):
        '''QString KCModuleProxy.rootOnlyMessage()'''
        return QString()
    def buttons(self):
        '''KCModule.Buttons KCModuleProxy.buttons()'''
        return KCModule.Buttons()
    def aboutData(self):
        '''KAboutData KCModuleProxy.aboutData()'''
        return KAboutData()
    def quickHelp(self):
        '''QString KCModuleProxy.quickHelp()'''
        return QString()
    def save(self):
        '''void KCModuleProxy.save()'''
    def load(self):
        '''void KCModuleProxy.load()'''


class KEmoticons(QObject):
    """"""
    def __init__(self):
        '''void KEmoticons.__init__()'''
    def parseMode(self):
        '''static KEmoticonsTheme.ParseMode KEmoticons.parseMode()'''
        return KEmoticonsTheme.ParseMode()
    def setParseMode(self, mode):
        '''static void KEmoticons.setParseMode(KEmoticonsTheme.ParseMode mode)'''
    def installTheme(self, archiveName):
        '''QStringList KEmoticons.installTheme(QString archiveName)'''
        return QStringList()
    def newTheme(self, name, service):
        '''KEmoticonsTheme KEmoticons.newTheme(QString name, unknown-type service)'''
        return KEmoticonsTheme()
    def setTheme(self, theme):
        '''static void KEmoticons.setTheme(KEmoticonsTheme theme)'''
    def setTheme(self, theme):
        '''static void KEmoticons.setTheme(QString theme)'''
    def themeList(self):
        '''static QStringList KEmoticons.themeList()'''
        return QStringList()
    def currentThemeName(self):
        '''static QString KEmoticons.currentThemeName()'''
        return QString()
    def theme(self):
        '''KEmoticonsTheme KEmoticons.theme()'''
        return KEmoticonsTheme()
    def theme(self, name):
        '''KEmoticonsTheme KEmoticons.theme(QString name)'''
        return KEmoticonsTheme()


class KEmoticonsProvider(QObject):
    """"""
    # Enum KEmoticonsProvider.AddEmoticonOption
    DoNotCopy = 0
    Copy = 0

    def __init__(self, parent = None):
        '''void KEmoticonsProvider.__init__(QObject parent = None)'''
    def removeEmoticonIndex(self, path, emoList):
        '''void KEmoticonsProvider.removeEmoticonIndex(QString path, QStringList emoList)'''
    def addEmoticonIndex(self, path, emoList):
        '''void KEmoticonsProvider.addEmoticonIndex(QString path, QStringList emoList)'''
    def removeEmoticonsMap(self, key):
        '''void KEmoticonsProvider.removeEmoticonsMap(QString key)'''
    def addEmoticonsMap(self, key, value):
        '''void KEmoticonsProvider.addEmoticonsMap(QString key, QStringList value)'''
    def clearEmoticonsMap(self):
        '''void KEmoticonsProvider.clearEmoticonsMap()'''
    def createNew(self):
        '''void KEmoticonsProvider.createNew()'''
    def emoticonsMap(self):
        '''dict-of-QString-QStringList KEmoticonsProvider.emoticonsMap()'''
        return dict-of-QString-QStringList()
    def fileName(self):
        '''QString KEmoticonsProvider.fileName()'''
        return QString()
    def themePath(self):
        '''QString KEmoticonsProvider.themePath()'''
        return QString()
    def setThemeName(self, name):
        '''void KEmoticonsProvider.setThemeName(QString name)'''
    def themeName(self):
        '''QString KEmoticonsProvider.themeName()'''
        return QString()
    def save(self):
        '''void KEmoticonsProvider.save()'''
    def addEmoticon(self, emo, text, option = None):
        '''bool KEmoticonsProvider.addEmoticon(QString emo, QString text, KEmoticonsProvider.AddEmoticonOption option = KEmoticonsProvider.DoNotCopy)'''
        return bool()
    def removeEmoticon(self, emo):
        '''bool KEmoticonsProvider.removeEmoticon(QString emo)'''
        return bool()
    def loadTheme(self, path):
        '''bool KEmoticonsProvider.loadTheme(QString path)'''
        return bool()
    class Emoticon():
        """"""
        matchText = None # QString - member
        matchTextEscaped = None # QString - member
        picHTMLCode = None # QString - member
        picPath = None # QString - member
        def __init__(self):
            '''void KEmoticonsProvider.Emoticon.__init__()'''
        def __init__(self):
            '''KEmoticonsProvider.Emoticon KEmoticonsProvider.Emoticon.__init__()'''
            return KEmoticonsProvider.Emoticon()
        def __ge__(self, e):
            '''bool KEmoticonsProvider.Emoticon.__ge__(KEmoticonsProvider.Emoticon e)'''
            return bool()
        def __lt__(self, e):
            '''bool KEmoticonsProvider.Emoticon.__lt__(KEmoticonsProvider.Emoticon e)'''
            return bool()


class KEmoticonsTheme():
    """"""
    # Enum KEmoticonsTheme.TokenType
    Undefined = 0
    Image = 0
    Text = 0

    # Enum KEmoticonsTheme.ParseModeEnum
    DefaultParse = 0
    StrictParse = 0
    RelaxedParse = 0
    SkipHTML = 0

    def __init__(self):
        '''void KEmoticonsTheme.__init__()'''
    def __init__(self, ket):
        '''void KEmoticonsTheme.__init__(KEmoticonsTheme ket)'''
    def __init__(self, p):
        '''void KEmoticonsTheme.__init__(KEmoticonsProvider p)'''
    def isNull(self):
        '''bool KEmoticonsTheme.isNull()'''
        return bool()
    def createNew(self):
        '''void KEmoticonsTheme.createNew()'''
    def emoticonsMap(self):
        '''dict-of-QString-QStringList KEmoticonsTheme.emoticonsMap()'''
        return dict-of-QString-QStringList()
    def fileName(self):
        '''QString KEmoticonsTheme.fileName()'''
        return QString()
    def themePath(self):
        '''QString KEmoticonsTheme.themePath()'''
        return QString()
    def setThemeName(self, name):
        '''void KEmoticonsTheme.setThemeName(QString name)'''
    def themeName(self):
        '''QString KEmoticonsTheme.themeName()'''
        return QString()
    def save(self):
        '''void KEmoticonsTheme.save()'''
    def addEmoticon(self, emo, text, option = None):
        '''bool KEmoticonsTheme.addEmoticon(QString emo, QString text, KEmoticonsProvider.AddEmoticonOption option = KEmoticonsProvider.DoNotCopy)'''
        return bool()
    def removeEmoticon(self, emo):
        '''bool KEmoticonsTheme.removeEmoticon(QString emo)'''
        return bool()
    def loadTheme(self, path):
        '''bool KEmoticonsTheme.loadTheme(QString path)'''
        return bool()
    def tokenize(self, message, mode = None):
        '''list-of-KEmoticonsTheme.Token KEmoticonsTheme.tokenize(QString message, KEmoticonsTheme.ParseMode mode = KEmoticonsTheme.DefaultParse)'''
        return [KEmoticonsTheme.Token()]
    def parseEmoticons(self, text, mode = None, exclude = QStringList()):
        '''QString KEmoticonsTheme.parseEmoticons(QString text, KEmoticonsTheme.ParseMode mode = KEmoticonsTheme.DefaultParse, QStringList exclude = QStringList())'''
        return QString()
    class ParseMode():
        """"""
        def __init__(self):
            '''KEmoticonsTheme.ParseMode KEmoticonsTheme.ParseMode.__init__()'''
            return KEmoticonsTheme.ParseMode()
        def __init__(self):
            '''int KEmoticonsTheme.ParseMode.__init__()'''
            return int()
        def __init__(self):
            '''void KEmoticonsTheme.ParseMode.__init__()'''
        def __bool__(self):
            '''int KEmoticonsTheme.ParseMode.__bool__()'''
            return int()
        def __ne__(self, f):
            '''bool KEmoticonsTheme.ParseMode.__ne__(KEmoticonsTheme.ParseMode f)'''
            return bool()
        def __eq__(self, f):
            '''bool KEmoticonsTheme.ParseMode.__eq__(KEmoticonsTheme.ParseMode f)'''
            return bool()
        def __invert__(self):
            '''KEmoticonsTheme.ParseMode KEmoticonsTheme.ParseMode.__invert__()'''
            return KEmoticonsTheme.ParseMode()
        def __and__(self, mask):
            '''KEmoticonsTheme.ParseMode KEmoticonsTheme.ParseMode.__and__(int mask)'''
            return KEmoticonsTheme.ParseMode()
        def __xor__(self, f):
            '''KEmoticonsTheme.ParseMode KEmoticonsTheme.ParseMode.__xor__(KEmoticonsTheme.ParseMode f)'''
            return KEmoticonsTheme.ParseMode()
        def __xor__(self, f):
            '''KEmoticonsTheme.ParseMode KEmoticonsTheme.ParseMode.__xor__(int f)'''
            return KEmoticonsTheme.ParseMode()
        def __or__(self, f):
            '''KEmoticonsTheme.ParseMode KEmoticonsTheme.ParseMode.__or__(KEmoticonsTheme.ParseMode f)'''
            return KEmoticonsTheme.ParseMode()
        def __or__(self, f):
            '''KEmoticonsTheme.ParseMode KEmoticonsTheme.ParseMode.__or__(int f)'''
            return KEmoticonsTheme.ParseMode()
        def __int__(self):
            '''int KEmoticonsTheme.ParseMode.__int__()'''
            return int()
        def __ixor__(self, f):
            '''KEmoticonsTheme.ParseMode KEmoticonsTheme.ParseMode.__ixor__(KEmoticonsTheme.ParseMode f)'''
            return KEmoticonsTheme.ParseMode()
        def __ior__(self, f):
            '''KEmoticonsTheme.ParseMode KEmoticonsTheme.ParseMode.__ior__(KEmoticonsTheme.ParseMode f)'''
            return KEmoticonsTheme.ParseMode()
        def __iand__(self, mask):
            '''KEmoticonsTheme.ParseMode KEmoticonsTheme.ParseMode.__iand__(int mask)'''
            return KEmoticonsTheme.ParseMode()
    class Token():
        """"""
        picHTMLCode = None # QString - member
        picPath = None # QString - member
        text = None # QString - member
        type = None # KEmoticonsTheme.TokenType - member
        def __init__(self):
            '''void KEmoticonsTheme.Token.__init__()'''
        def __init__(self, t, m):
            '''void KEmoticonsTheme.Token.__init__(KEmoticonsTheme.TokenType t, QString m)'''
        def __init__(self, t, m, p, html):
            '''void KEmoticonsTheme.Token.__init__(KEmoticonsTheme.TokenType t, QString m, QString p, QString html)'''
        def __init__(self):
            '''KEmoticonsTheme.Token KEmoticonsTheme.Token.__init__()'''
            return KEmoticonsTheme.Token()


class KIdleTime(QObject):
    """"""
    timeoutReached = pyqtSignal() # void timeoutReached(int) - signal
    timeoutReached = pyqtSignal() # void timeoutReached(int,int) - signal
    resumingFromIdle = pyqtSignal() # void resumingFromIdle() - signal
    def stopCatchingResumeEvent(self):
        '''void KIdleTime.stopCatchingResumeEvent()'''
    def catchNextResumeEvent(self):
        '''void KIdleTime.catchNextResumeEvent()'''
    def removeAllIdleTimeouts(self):
        '''void KIdleTime.removeAllIdleTimeouts()'''
    def removeIdleTimeout(self, identifier):
        '''void KIdleTime.removeIdleTimeout(int identifier)'''
    def addIdleTimeout(self, msec):
        '''int KIdleTime.addIdleTimeout(int msec)'''
        return int()
    def simulateUserActivity(self):
        '''void KIdleTime.simulateUserActivity()'''
    def idleTimeouts(self):
        '''unknown-type KIdleTime.idleTimeouts()'''
        return unknown-type()
    def idleTime(self):
        '''int KIdleTime.idleTime()'''
        return int()
    def instance(self):
        '''static KIdleTime KIdleTime.instance()'''
        return KIdleTime()


class KPluginSelector(QWidget):
    """"""
    # Enum KPluginSelector.PluginLoadMethod
    ReadConfigFile = 0
    IgnoreConfigFile = 0

    def __init__(self, parent = None):
        '''void KPluginSelector.__init__(QWidget parent = None)'''
    configCommitted = pyqtSignal() # void configCommitted(const QByteArrayamp;) - signal
    changed = pyqtSignal() # void changed(bool) - signal
    def updatePluginsState(self):
        '''void KPluginSelector.updatePluginsState()'''
    def isDefault(self):
        '''bool KPluginSelector.isDefault()'''
        return bool()
    def defaults(self):
        '''void KPluginSelector.defaults()'''
    def save(self):
        '''void KPluginSelector.save()'''
    def load(self):
        '''void KPluginSelector.load()'''
    def addPlugins(self, componentName, categoryName = QString(), categoryKey = QString(), config = None):
        '''void KPluginSelector.addPlugins(QString componentName, QString categoryName = QString(), QString categoryKey = QString(), unknown-type config = KSharedConfig.Ptr())'''
    def addPlugins(self, instance, categoryName = QString(), categoryKey = QString(), config = None):
        '''void KPluginSelector.addPlugins(KComponentData instance, QString categoryName = QString(), QString categoryKey = QString(), unknown-type config = KSharedConfig.Ptr())'''
    def addPlugins(self, pluginInfoList, pluginLoadMethod = None, categoryName = QString(), categoryKey = QString(), config = None):
        '''void KPluginSelector.addPlugins(list-of-KPluginInfo pluginInfoList, KPluginSelector.PluginLoadMethod pluginLoadMethod = KPluginSelector.ReadConfigFile, QString categoryName = QString(), QString categoryKey = QString(), unknown-type config = KSharedConfig.Ptr())'''


class KPrintPreview(KDialog):
    """"""
    def __init__(self, printer, parent = None):
        '''void KPrintPreview.__init__(QPrinter printer, QWidget parent = None)'''
    def isAvailable(self):
        '''static bool KPrintPreview.isAvailable()'''
        return bool()
    def showEvent(self, event):
        '''void KPrintPreview.showEvent(QShowEvent event)'''


