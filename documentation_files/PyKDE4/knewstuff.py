class pyqtSignal():
 def connect(self, targetSignal): pass
 def emit(self, *args): pass
from QtCore import *

class KNS():
    """"""
    def standardAction(self, what, receiver, slot, parent, name = None):
        '''static KAction KNS.standardAction(QString what, QObject receiver, str slot, KActionCollection parent, str name = None)'''
        return KAction()
    class KTranslatable():
        """"""
        def __init__(self):
            '''void KNS.KTranslatable.__init__()'''
        def __init__(self, string):
            '''void KNS.KTranslatable.__init__(QString string)'''
        def __init__(self):
            '''KNS.KTranslatable KNS.KTranslatable.__init__()'''
            return KNS.KTranslatable()
        def isEmpty(self):
            '''bool KNS.KTranslatable.isEmpty()'''
            return bool()
        def isTranslated(self):
            '''bool KNS.KTranslatable.isTranslated()'''
            return bool()
        def stringmap(self):
            '''dict-of-QString-QString KNS.KTranslatable.stringmap()'''
            return dict-of-QString-QString()
        def language(self):
            '''QString KNS.KTranslatable.language()'''
            return QString()
        def languages(self):
            '''QStringList KNS.KTranslatable.languages()'''
            return QStringList()
        def strings(self):
            '''QStringList KNS.KTranslatable.strings()'''
            return QStringList()
        def translated(self, lang):
            '''QString KNS.KTranslatable.translated(QString lang)'''
            return QString()
        def representation(self):
            '''QString KNS.KTranslatable.representation()'''
            return QString()
        def addString(self, lang, string):
            '''void KNS.KTranslatable.addString(QString lang, QString string)'''
    class Author():
        """"""
        def __init__(self):
            '''void KNS.Author.__init__()'''
        def __init__(self, other):
            '''void KNS.Author.__init__(KNS.Author other)'''
        def homepage(self):
            '''QString KNS.Author.homepage()'''
            return QString()
        def setHomepage(self, homepage):
            '''void KNS.Author.setHomepage(QString homepage)'''
        def jabber(self):
            '''QString KNS.Author.jabber()'''
            return QString()
        def setJabber(self, jabber):
            '''void KNS.Author.setJabber(QString jabber)'''
        def email(self):
            '''QString KNS.Author.email()'''
            return QString()
        def setEmail(self, email):
            '''void KNS.Author.setEmail(QString email)'''
        def name(self):
            '''QString KNS.Author.name()'''
            return QString()
        def setName(self, name):
            '''void KNS.Author.setName(QString name)'''
    class Category():
        """"""
        def __init__(self):
            '''void KNS.Category.__init__()'''
        def icon(self):
            '''KUrl KNS.Category.icon()'''
            return KUrl()
        def setIcon(self, icon):
            '''void KNS.Category.setIcon(KUrl icon)'''
        def description(self):
            '''KNS.KTranslatable KNS.Category.description()'''
            return KNS.KTranslatable()
        def setDescription(self, type):
            '''void KNS.Category.setDescription(KNS.KTranslatable type)'''
        def name(self):
            '''KNS.KTranslatable KNS.Category.name()'''
            return KNS.KTranslatable()
        def setName(self, name):
            '''void KNS.Category.setName(KNS.KTranslatable name)'''
        def id(self):
            '''QString KNS.Category.id()'''
            return QString()
        def setId(self, id):
            '''void KNS.Category.setId(QString id)'''
    class Button(KPushButton):
        """"""
        def __init__(self, what, providerList, resourceType, parent):
            '''void KNS.Button.__init__(QString what, QString providerList, QString resourceType, QWidget parent)'''
        def __init__(self, parent):
            '''void KNS.Button.__init__(QWidget parent)'''
        def showDialog(self):
            '''void KNS.Button.showDialog()'''
        dialogFinished = pyqtSignal() # void dialogFinished() - signal
        aboutToShowDialog = pyqtSignal() # void aboutToShowDialog() - signal
        def setButtonText(self, what):
            '''void KNS.Button.setButtonText(QString what)'''
        def setResourceType(self, resourceType):
            '''void KNS.Button.setResourceType(QString resourceType)'''
        def setProviderList(self, providerList):
            '''void KNS.Button.setProviderList(QString providerList)'''
    class Installation():
        """"""
        # Enum KNS.Installation.Scope
        ScopeUser = 0
        ScopeSystem = 0
    
        # Enum KNS.Installation.Policy
        CheckNever = 0
        CheckIfPossible = 0
        CheckAlways = 0
    
        def __init__(self):
            '''void KNS.Installation.__init__()'''
        def customName(self):
            '''bool KNS.Installation.customName()'''
            return bool()
        def scope(self):
            '''KNS.Installation.Scope KNS.Installation.scope()'''
            return KNS.Installation.Scope()
        def signaturePolicy(self):
            '''KNS.Installation.Policy KNS.Installation.signaturePolicy()'''
            return KNS.Installation.Policy()
        def checksumPolicy(self):
            '''KNS.Installation.Policy KNS.Installation.checksumPolicy()'''
            return KNS.Installation.Policy()
        def isRemote(self):
            '''bool KNS.Installation.isRemote()'''
            return bool()
        def absoluteInstallPath(self):
            '''QString KNS.Installation.absoluteInstallPath()'''
            return QString()
        def installPath(self):
            '''QString KNS.Installation.installPath()'''
            return QString()
        def targetDir(self):
            '''QString KNS.Installation.targetDir()'''
            return QString()
        def standardResourceDir(self):
            '''QString KNS.Installation.standardResourceDir()'''
            return QString()
        def uninstallCommand(self):
            '''QString KNS.Installation.uninstallCommand()'''
            return QString()
        def command(self):
            '''QString KNS.Installation.command()'''
            return QString()
        def uncompression(self):
            '''QString KNS.Installation.uncompression()'''
            return QString()
        def setCustomName(self, customname):
            '''void KNS.Installation.setCustomName(bool customname)'''
        def setSignaturePolicy(self, policy):
            '''void KNS.Installation.setSignaturePolicy(KNS.Installation.Policy policy)'''
        def setChecksumPolicy(self, policy):
            '''void KNS.Installation.setChecksumPolicy(KNS.Installation.Policy policy)'''
        def setScope(self, scope):
            '''void KNS.Installation.setScope(KNS.Installation.Scope scope)'''
        def setAbsoluteInstallPath(self, dir):
            '''void KNS.Installation.setAbsoluteInstallPath(QString dir)'''
        def setInstallPath(self, dir):
            '''void KNS.Installation.setInstallPath(QString dir)'''
        def setTargetDir(self, dir):
            '''void KNS.Installation.setTargetDir(QString dir)'''
        def setStandardResourceDir(self, dir):
            '''void KNS.Installation.setStandardResourceDir(QString dir)'''
        def setUninstallCommand(self, command):
            '''void KNS.Installation.setUninstallCommand(QString command)'''
        def setCommand(self, command):
            '''void KNS.Installation.setCommand(QString command)'''
        def setUncompression(self, uncompression):
            '''void KNS.Installation.setUncompression(QString uncompression)'''
    class Engine():
        """"""
        def __init__(self, parent = None):
            '''void KNS.Engine.__init__(QWidget parent = None)'''
        def init(self, config):
            '''bool KNS.Engine.init(QString config)'''
            return bool()
        def uploadDialog(self, file):
            '''void KNS.Engine.uploadDialog(QString file)'''
        def downloadDialog(self):
            '''void KNS.Engine.downloadDialog()'''
        def downloadDialog(self, receiver, slot):
            '''void KNS.Engine.downloadDialog(QObject receiver, str slot)'''
        def upload(self, file):
            '''static KNS.Entry KNS.Engine.upload(QString file)'''
            return KNS.Entry()
        def uploadDialogModal(self, file):
            '''KNS.Entry KNS.Engine.uploadDialogModal(QString file)'''
            return KNS.Entry()
        def download(self):
            '''static list-of-KNS.Entry KNS.Engine.download()'''
            return [KNS.Entry()]
        def downloadDialogModal(self, parent = None):
            '''list-of-KNS.Entry KNS.Engine.downloadDialogModal(QWidget parent = None)'''
            return [KNS.Entry()]
    class Entry():
        """"""
        # Enum KNS.Entry.Source
        Cache = 0
        Online = 0
        Registry = 0
    
        # Enum KNS.Entry.Status
        Invalid = 0
        Downloadable = 0
        Installed = 0
        Updateable = 0
        Deleted = 0
    
        def __init__(self):
            '''void KNS.Entry.__init__()'''
        def __init__(self, other):
            '''void KNS.Entry.__init__(KNS.Entry other)'''
        def idNumber(self):
            '''int KNS.Entry.idNumber()'''
            return int()
        def setIdNumber(self, number):
            '''void KNS.Entry.setIdNumber(int number)'''
        def source(self):
            '''KNS.Entry.Source KNS.Entry.source()'''
            return KNS.Entry.Source()
        def setSource(self, source):
            '''void KNS.Entry.setSource(KNS.Entry.Source source)'''
        def status(self):
            '''KNS.Entry.Status KNS.Entry.status()'''
            return KNS.Entry.Status()
        def setStatus(self, status):
            '''void KNS.Entry.setStatus(KNS.Entry.Status status)'''
        def signature(self):
            '''QString KNS.Entry.signature()'''
            return QString()
        def checksum(self):
            '''QString KNS.Entry.checksum()'''
            return QString()
        def setSignature(self, signature):
            '''void KNS.Entry.setSignature(QString signature)'''
        def setChecksum(self, checksum):
            '''void KNS.Entry.setChecksum(QString checksum)'''
        def downloads(self):
            '''int KNS.Entry.downloads()'''
            return int()
        def setDownloads(self, downloads):
            '''void KNS.Entry.setDownloads(int downloads)'''
        def rating(self):
            '''int KNS.Entry.rating()'''
            return int()
        def setRating(self, rating):
            '''void KNS.Entry.setRating(int rating)'''
        def uninstalledFiles(self):
            '''QStringList KNS.Entry.uninstalledFiles()'''
            return QStringList()
        def installedFiles(self):
            '''QStringList KNS.Entry.installedFiles()'''
            return QStringList()
        def setUnInstalledFiles(self, files):
            '''void KNS.Entry.setUnInstalledFiles(QStringList files)'''
        def setInstalledFiles(self, files):
            '''void KNS.Entry.setInstalledFiles(QStringList files)'''
        def preview(self):
            '''KNS.KTranslatable KNS.Entry.preview()'''
            return KNS.KTranslatable()
        def setPreview(self, url):
            '''void KNS.Entry.setPreview(KNS.KTranslatable url)'''
        def payload(self):
            '''KNS.KTranslatable KNS.Entry.payload()'''
            return KNS.KTranslatable()
        def setPayload(self, url):
            '''void KNS.Entry.setPayload(KNS.KTranslatable url)'''
        def releaseDate(self):
            '''QDate KNS.Entry.releaseDate()'''
            return QDate()
        def setReleaseDate(self, releasedate):
            '''void KNS.Entry.setReleaseDate(QDate releasedate)'''
        def release(self):
            '''int KNS.Entry.release()'''
            return int()
        def setRelease(self, release):
            '''void KNS.Entry.setRelease(int release)'''
        def version(self):
            '''QString KNS.Entry.version()'''
            return QString()
        def setVersion(self, version):
            '''void KNS.Entry.setVersion(QString version)'''
        def summary(self):
            '''KNS.KTranslatable KNS.Entry.summary()'''
            return KNS.KTranslatable()
        def setSummary(self, summary):
            '''void KNS.Entry.setSummary(KNS.KTranslatable summary)'''
        def license(self):
            '''QString KNS.Entry.license()'''
            return QString()
        def setLicense(self, license):
            '''void KNS.Entry.setLicense(QString license)'''
        def author(self):
            '''KNS.Author KNS.Entry.author()'''
            return KNS.Author()
        def setAuthor(self, author):
            '''void KNS.Entry.setAuthor(KNS.Author author)'''
        def category(self):
            '''QString KNS.Entry.category()'''
            return QString()
        def setCategory(self, category):
            '''void KNS.Entry.setCategory(QString category)'''
        def name(self):
            '''KNS.KTranslatable KNS.Entry.name()'''
            return KNS.KTranslatable()
        def setName(self, name):
            '''void KNS.Entry.setName(KNS.KTranslatable name)'''


class KNS3():
    """"""
    def standardActionUpload(self, what, parent, name = None):
        '''static SLOT() KNS3.standardActionUpload(QString what, KActionCollection parent, str name = None)'''
        return SLOT()()
    def standardActionUpload(self, what, parent, name = None):
        '''static callable KNS3.standardActionUpload(QString what, KActionCollection parent, str name = None)'''
        return callable()
    def standardAction(self, what, parent, name = None):
        '''static SLOT() KNS3.standardAction(QString what, KActionCollection parent, str name = None)'''
        return SLOT()()
    def standardAction(self, what, parent, name = None):
        '''static callable KNS3.standardAction(QString what, KActionCollection parent, str name = None)'''
        return callable()
    class DownloadManager(QObject):
        """"""
        # Enum KNS3.DownloadManager.SortOrder
        Newest = 0
        Alphabetical = 0
        Rating = 0
        Downloads = 0
    
        def __init__(self, parent = None):
            '''void KNS3.DownloadManager.__init__(QObject parent = None)'''
        def __init__(self, configFile, parent = None):
            '''void KNS3.DownloadManager.__init__(QString configFile, QObject parent = None)'''
        def uninstallEntry(self, entry):
            '''void KNS3.DownloadManager.uninstallEntry(KNS3.Entry entry)'''
        entryStatusChanged = pyqtSignal() # void entryStatusChanged(const KNS3::Entryamp;) - signal
        searchResult = pyqtSignal() # void searchResult(const KNS3::Entry::Listamp;) - signal
        def setSearchOrder(self, order):
            '''void KNS3.DownloadManager.setSearchOrder(KNS3.DownloadManager.SortOrder order)'''
        def setSearchTerm(self, searchTerm):
            '''void KNS3.DownloadManager.setSearchTerm(QString searchTerm)'''
        def installEntry(self, entry):
            '''void KNS3.DownloadManager.installEntry(KNS3.Entry entry)'''
        def checkForUpdates(self):
            '''void KNS3.DownloadManager.checkForUpdates()'''
        def search(self, page = 0, pageSize = 100):
            '''void KNS3.DownloadManager.search(int page = 0, int pageSize = 100)'''
    class UploadDialog(KDialog):
        """"""
        def __init__(self, parent = None):
            '''void KNS3.UploadDialog.__init__(QWidget parent = None)'''
        def __init__(self, configFile, parent = None):
            '''void KNS3.UploadDialog.__init__(QString configFile, QWidget parent = None)'''
        def setPreviewImageFile(self, number, file):
            '''void KNS3.UploadDialog.setPreviewImageFile(int number, KUrl file)'''
        def setPriceEnabled(self, enabled):
            '''void KNS3.UploadDialog.setPriceEnabled(bool enabled)'''
        def selectCategory(self, category):
            '''void KNS3.UploadDialog.selectCategory(QString category)'''
        def setPriceReason(self, reason):
            '''void KNS3.UploadDialog.setPriceReason(QString reason)'''
        def setPrice(self, price):
            '''void KNS3.UploadDialog.setPrice(float price)'''
        def setChangelog(self, changelog):
            '''void KNS3.UploadDialog.setChangelog(QString changelog)'''
        def setDescription(self, description):
            '''void KNS3.UploadDialog.setDescription(QString description)'''
        def setVersion(self, version):
            '''void KNS3.UploadDialog.setVersion(QString version)'''
        def accept(self):
            '''void KNS3.UploadDialog.accept()'''
        def setUploadName(self, name):
            '''void KNS3.UploadDialog.setUploadName(QString name)'''
        def setUploadFile(self, payloadFile):
            '''void KNS3.UploadDialog.setUploadFile(KUrl payloadFile)'''
    class Button(KPushButton):
        """"""
        def __init__(self, text, configFile, parent):
            '''void KNS3.Button.__init__(QString text, QString configFile, QWidget parent)'''
        def __init__(self, parent):
            '''void KNS3.Button.__init__(QWidget parent)'''
        def showDialog(self):
            '''void KNS3.Button.showDialog()'''
        dialogFinished = pyqtSignal() # void dialogFinished(const KNS3::Entry::Listamp;) - signal
        aboutToShowDialog = pyqtSignal() # void aboutToShowDialog() - signal
        def setButtonText(self, text):
            '''void KNS3.Button.setButtonText(QString text)'''
        def setConfigFile(self, configFile):
            '''void KNS3.Button.setConfigFile(QString configFile)'''
    class Entry():
        """"""
        # Enum KNS3.Entry.Status
        Invalid = 0
        Downloadable = 0
        Installed = 0
        Updateable = 0
        Deleted = 0
        Installing = 0
        Updating = 0
    
        def __init__(self, other):
            '''void KNS3.Entry.__init__(KNS3.Entry other)'''
        def providerId(self):
            '''QString KNS3.Entry.providerId()'''
            return QString()
        def id(self):
            '''QString KNS3.Entry.id()'''
            return QString()
        def version(self):
            '''QString KNS3.Entry.version()'''
            return QString()
        def summary(self):
            '''QString KNS3.Entry.summary()'''
            return QString()
        def license(self):
            '''QString KNS3.Entry.license()'''
            return QString()
        def status(self):
            '''KNS3.Entry.Status KNS3.Entry.status()'''
            return KNS3.Entry.Status()
        def uninstalledFiles(self):
            '''QStringList KNS3.Entry.uninstalledFiles()'''
            return QStringList()
        def installedFiles(self):
            '''QStringList KNS3.Entry.installedFiles()'''
            return QStringList()
        def category(self):
            '''QString KNS3.Entry.category()'''
            return QString()
        def name(self):
            '''QString KNS3.Entry.name()'''
            return QString()
    class DownloadWidget(QWidget):
        """"""
        def __init__(self, parent = None):
            '''void KNS3.DownloadWidget.__init__(QWidget parent = None)'''
        def __init__(self, configFile, parent = None):
            '''void KNS3.DownloadWidget.__init__(QString configFile, QWidget parent = None)'''
        def installedEntries(self):
            '''list-of-KNS3.Entry KNS3.DownloadWidget.installedEntries()'''
            return [KNS3.Entry()]
        def changedEntries(self):
            '''list-of-KNS3.Entry KNS3.DownloadWidget.changedEntries()'''
            return [KNS3.Entry()]
    class DownloadDialog(KDialog):
        """"""
        def __init__(self, parent = None):
            '''void KNS3.DownloadDialog.__init__(QWidget parent = None)'''
        def __init__(self, configFile, parent = None):
            '''void KNS3.DownloadDialog.__init__(QString configFile, QWidget parent = None)'''
        def installedEntries(self):
            '''list-of-KNS3.Entry KNS3.DownloadDialog.installedEntries()'''
            return [KNS3.Entry()]
        def changedEntries(self):
            '''list-of-KNS3.Entry KNS3.DownloadDialog.changedEntries()'''
            return [KNS3.Entry()]


