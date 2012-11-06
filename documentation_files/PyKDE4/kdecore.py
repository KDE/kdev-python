class pyqtSignal():
 def connect(self, targetSignal): pass
 def emit(self, *args): pass
from QtCore import *

class KAboutPerson():
    """"""
    def __init__(self, name, task = KLocalizedString(), emailAddress = QByteArray(), webAddress = QByteArray()):
        '''void KAboutPerson.__init__(KLocalizedString name, KLocalizedString task = KLocalizedString(), QByteArray emailAddress = QByteArray(), QByteArray webAddress = QByteArray())'''
    def __init__(self, other):
        '''void KAboutPerson.__init__(KAboutPerson other)'''
    def __init__(self, name, task, emailAddress, webAddress, ocsUsername):
        '''void KAboutPerson.__init__(KLocalizedString name, KLocalizedString task, QByteArray emailAddress, QByteArray webAddress, QByteArray ocsUsername)'''
    def ocsUsername(self):
        '''QString KAboutPerson.ocsUsername()'''
        return QString()
    def webAddress(self):
        '''QString KAboutPerson.webAddress()'''
        return QString()
    def emailAddress(self):
        '''QString KAboutPerson.emailAddress()'''
        return QString()
    def task(self):
        '''QString KAboutPerson.task()'''
        return QString()
    def name(self):
        '''QString KAboutPerson.name()'''
        return QString()


class KAboutData():
    """"""
    # Enum KAboutData.NameFormat
    ShortName = 0
    FullName = 0

    # Enum KAboutData.LicenseKey
    License_Custom = 0
    License_File = 0
    License_Unknown = 0
    License_GPL = 0
    License_GPL_V2 = 0
    License_LGPL = 0
    License_LGPL_V2 = 0
    License_BSD = 0
    License_Artistic = 0
    License_QPL = 0
    License_QPL_V1_0 = 0
    License_GPL_V3 = 0
    License_LGPL_V3 = 0

    def __init__(self, appName, catalogName, programName, version, shortDescription = KLocalizedString(), licenseType = None, copyrightStatement = KLocalizedString(), otherText = KLocalizedString(), homePageAddress = QByteArray(), bugsEmailAddress = None):
        '''void KAboutData.__init__(QByteArray appName, QByteArray catalogName, KLocalizedString programName, QByteArray version, KLocalizedString shortDescription = KLocalizedString(), KAboutData.LicenseKey licenseType = KAboutData.License_Unknown, KLocalizedString copyrightStatement = KLocalizedString(), KLocalizedString otherText = KLocalizedString(), QByteArray homePageAddress = QByteArray(), QByteArray bugsEmailAddress = submit@bugs.kde.org)'''
    def __init__(self, other):
        '''void KAboutData.__init__(KAboutData other)'''
    def ocsProviderUrl(self):
        '''QString KAboutData.ocsProviderUrl()'''
        return QString()
    def setOcsProvider(self, providerUrl):
        '''KAboutData KAboutData.setOcsProvider(QByteArray providerUrl)'''
        return KAboutData()
    def unsetCustomAuthorText(self):
        '''KAboutData KAboutData.unsetCustomAuthorText()'''
        return KAboutData()
    def setCustomAuthorText(self, plainText, richText):
        '''KAboutData KAboutData.setCustomAuthorText(KLocalizedString plainText, KLocalizedString richText)'''
        return KAboutData()
    def customAuthorTextEnabled(self):
        '''bool KAboutData.customAuthorTextEnabled()'''
        return bool()
    def customAuthorRichText(self):
        '''QString KAboutData.customAuthorRichText()'''
        return QString()
    def customAuthorPlainText(self):
        '''QString KAboutData.customAuthorPlainText()'''
        return QString()
    def copyrightStatement(self):
        '''QString KAboutData.copyrightStatement()'''
        return QString()
    def licenses(self):
        '''list-of-KAboutLicense KAboutData.licenses()'''
        return [KAboutLicense()]
    def licenseName(self, formatName):
        '''QString KAboutData.licenseName(KAboutData.NameFormat formatName)'''
        return QString()
    def license(self):
        '''QString KAboutData.license()'''
        return QString()
    def otherText(self):
        '''QString KAboutData.otherText()'''
        return QString()
    def aboutTranslationTeam(self):
        '''static QString KAboutData.aboutTranslationTeam()'''
        return QString()
    def translators(self):
        '''list-of-KAboutPerson KAboutData.translators()'''
        return [KAboutPerson()]
    def credits(self):
        '''list-of-KAboutPerson KAboutData.credits()'''
        return [KAboutPerson()]
    def authors(self):
        '''list-of-KAboutPerson KAboutData.authors()'''
        return [KAboutPerson()]
    def internalBugAddress(self):
        '''str KAboutData.internalBugAddress()'''
        return str()
    def bugAddress(self):
        '''QString KAboutData.bugAddress()'''
        return QString()
    def homepage(self):
        '''QString KAboutData.homepage()'''
        return QString()
    def catalogName(self):
        '''QString KAboutData.catalogName()'''
        return QString()
    def shortDescription(self):
        '''QString KAboutData.shortDescription()'''
        return QString()
    def internalVersion(self):
        '''str KAboutData.internalVersion()'''
        return str()
    def version(self):
        '''QString KAboutData.version()'''
        return QString()
    def programLogo(self):
        '''QVariant KAboutData.programLogo()'''
        return QVariant()
    def programIconName(self):
        '''QString KAboutData.programIconName()'''
        return QString()
    def translateInternalProgramName(self):
        '''void KAboutData.translateInternalProgramName()'''
    def internalProgramName(self):
        '''str KAboutData.internalProgramName()'''
        return str()
    def organizationDomain(self):
        '''QString KAboutData.organizationDomain()'''
        return QString()
    def programName(self):
        '''QString KAboutData.programName()'''
        return QString()
    def productName(self):
        '''QString KAboutData.productName()'''
        return QString()
    def appName(self):
        '''QString KAboutData.appName()'''
        return QString()
    def setProductName(self, name):
        '''KAboutData KAboutData.setProductName(QByteArray name)'''
        return KAboutData()
    def setOrganizationDomain(self, domain):
        '''KAboutData KAboutData.setOrganizationDomain(QByteArray domain)'''
        return KAboutData()
    def setBugAddress(self, bugAddress):
        '''KAboutData KAboutData.setBugAddress(QByteArray bugAddress)'''
        return KAboutData()
    def setHomepage(self, homepage):
        '''KAboutData KAboutData.setHomepage(QByteArray homepage)'''
        return KAboutData()
    def setOtherText(self, otherText):
        '''KAboutData KAboutData.setOtherText(KLocalizedString otherText)'''
        return KAboutData()
    def setCopyrightStatement(self, copyrightStatement):
        '''KAboutData KAboutData.setCopyrightStatement(KLocalizedString copyrightStatement)'''
        return KAboutData()
    def addLicense(self, licenseKey):
        '''KAboutData KAboutData.addLicense(KAboutData.LicenseKey licenseKey)'''
        return KAboutData()
    def setLicense(self, licenseKey):
        '''KAboutData KAboutData.setLicense(KAboutData.LicenseKey licenseKey)'''
        return KAboutData()
    def setCatalogName(self, catalogName):
        '''KAboutData KAboutData.setCatalogName(QByteArray catalogName)'''
        return KAboutData()
    def setShortDescription(self, shortDescription):
        '''KAboutData KAboutData.setShortDescription(KLocalizedString shortDescription)'''
        return KAboutData()
    def setVersion(self, version):
        '''KAboutData KAboutData.setVersion(QByteArray version)'''
        return KAboutData()
    def setProgramLogo(self, image):
        '''KAboutData KAboutData.setProgramLogo(QVariant image)'''
        return KAboutData()
    def setProgramIconName(self, iconName):
        '''KAboutData KAboutData.setProgramIconName(QString iconName)'''
        return KAboutData()
    def setProgramName(self, programName):
        '''KAboutData KAboutData.setProgramName(KLocalizedString programName)'''
        return KAboutData()
    def setAppName(self, appName):
        '''KAboutData KAboutData.setAppName(QByteArray appName)'''
        return KAboutData()
    def addLicenseTextFile(self, file):
        '''KAboutData KAboutData.addLicenseTextFile(QString file)'''
        return KAboutData()
    def setLicenseTextFile(self, file):
        '''KAboutData KAboutData.setLicenseTextFile(QString file)'''
        return KAboutData()
    def addLicenseText(self, license):
        '''KAboutData KAboutData.addLicenseText(KLocalizedString license)'''
        return KAboutData()
    def setLicenseText(self, license):
        '''KAboutData KAboutData.setLicenseText(KLocalizedString license)'''
        return KAboutData()
    def setTranslator(self, name, emailAddress):
        '''KAboutData KAboutData.setTranslator(KLocalizedString name, KLocalizedString emailAddress)'''
        return KAboutData()
    def addCredit(self, name, task = KLocalizedString(), emailAddress = QByteArray(), webAddress = QByteArray()):
        '''KAboutData KAboutData.addCredit(KLocalizedString name, KLocalizedString task = KLocalizedString(), QByteArray emailAddress = QByteArray(), QByteArray webAddress = QByteArray())'''
        return KAboutData()
    def addCredit(self, name, task, emailAddress, webAddress, ocsUsername):
        '''KAboutData KAboutData.addCredit(KLocalizedString name, KLocalizedString task, QByteArray emailAddress, QByteArray webAddress, QByteArray ocsUsername)'''
        return KAboutData()
    def addAuthor(self, name, task = KLocalizedString(), emailAddress = QByteArray(), webAddress = QByteArray()):
        '''KAboutData KAboutData.addAuthor(KLocalizedString name, KLocalizedString task = KLocalizedString(), QByteArray emailAddress = QByteArray(), QByteArray webAddress = QByteArray())'''
        return KAboutData()
    def addAuthor(self, name, task, emailAddress, webAddress, ocsUsername):
        '''KAboutData KAboutData.addAuthor(KLocalizedString name, KLocalizedString task, QByteArray emailAddress, QByteArray webAddress, QByteArray ocsUsername)'''
        return KAboutData()


class KAboutLicense():
    """"""
    def __init__(self, other):
        '''void KAboutLicense.__init__(KAboutLicense other)'''
    def byKeyword(self, keyword):
        '''static KAboutLicense KAboutLicense.byKeyword(QString keyword)'''
        return KAboutLicense()
    def key(self):
        '''KAboutData.LicenseKey KAboutLicense.key()'''
        return KAboutData.LicenseKey()
    def name(self, formatName):
        '''QString KAboutLicense.name(KAboutData.NameFormat formatName)'''
        return QString()
    def text(self):
        '''QString KAboutLicense.text()'''
        return QString()


class KAuth():
    """"""
    class HelperSupport():
        """"""
        def helperMain(self, argc, argv, id, responder):
            '''static int KAuth.HelperSupport.helperMain(int argc, str argv, str id, QObject responder)'''
            return int()
        def isStopped(self):
            '''static bool KAuth.HelperSupport.isStopped()'''
            return bool()
        def progressStep(self, step):
            '''static void KAuth.HelperSupport.progressStep(int step)'''
        def progressStep(self, data):
            '''static void KAuth.HelperSupport.progressStep(dict-of-QString-QVariant data)'''
    class ActionWatcher(QObject):
        """"""
        statusChanged = pyqtSignal() # void statusChanged(int) - signal
        progressStep = pyqtSignal() # void progressStep(int) - signal
        progressStep = pyqtSignal() # void progressStep(const QVariantMapamp;) - signal
        actionPerformed = pyqtSignal() # void actionPerformed(const KAuth::ActionReplyamp;) - signal
        actionStarted = pyqtSignal() # void actionStarted() - signal
        def action(self):
            '''QString KAuth.ActionWatcher.action()'''
            return QString()
        def watcher(self, action):
            '''static KAuth.ActionWatcher KAuth.ActionWatcher.watcher(QString action)'''
            return KAuth.ActionWatcher()
    class Action():
        """"""
        # Enum KAuth.Action.AuthStatus
        Denied = 0
        Error = 0
        Invalid = 0
        Authorized = 0
        AuthRequired = 0
        UserCancelled = 0
    
        def __init__(self):
            '''void KAuth.Action.__init__()'''
        def __init__(self, action):
            '''void KAuth.Action.__init__(KAuth.Action action)'''
        def __init__(self, name):
            '''void KAuth.Action.__init__(QString name)'''
        def __init__(self, name, details):
            '''void KAuth.Action.__init__(QString name, QString details)'''
        def parentWidget(self):
            '''QWidget KAuth.Action.parentWidget()'''
            return QWidget()
        def setParentWidget(self, parent):
            '''void KAuth.Action.setParentWidget(QWidget parent)'''
        def earlyAuthorize(self):
            '''KAuth.Action.AuthStatus KAuth.Action.earlyAuthorize()'''
            return KAuth.Action.AuthStatus()
        def hasHelper(self):
            '''bool KAuth.Action.hasHelper()'''
            return bool()
        def __ne__(self, action):
            '''bool KAuth.Action.__ne__(KAuth.Action action)'''
            return bool()
        def __eq__(self, action):
            '''bool KAuth.Action.__eq__(KAuth.Action action)'''
            return bool()
        def stop(self):
            '''void KAuth.Action.stop()'''
        def stop(self, helperID):
            '''void KAuth.Action.stop(QString helperID)'''
        def executeActions(self, actions, deniedActions, helperId):
            '''static bool KAuth.Action.executeActions(list-of-KAuth.Action actions, list-of-KAuth.Action deniedActions, QString helperId)'''
            return bool()
        def executeActions(self, actions, deniedActions, helperId, parent):
            '''static bool KAuth.Action.executeActions(list-of-KAuth.Action actions, list-of-KAuth.Action deniedActions, QString helperId, QWidget parent)'''
            return bool()
        def executesAsync(self):
            '''bool KAuth.Action.executesAsync()'''
            return bool()
        def setExecutesAsync(self, async):
            '''void KAuth.Action.setExecutesAsync(bool async)'''
        def execute(self):
            '''KAuth.ActionReply KAuth.Action.execute()'''
            return KAuth.ActionReply()
        def execute(self, helperID):
            '''KAuth.ActionReply KAuth.Action.execute(QString helperID)'''
            return KAuth.ActionReply()
        def status(self):
            '''KAuth.Action.AuthStatus KAuth.Action.status()'''
            return KAuth.Action.AuthStatus()
        def authorize(self):
            '''KAuth.Action.AuthStatus KAuth.Action.authorize()'''
            return KAuth.Action.AuthStatus()
        def addArgument(self, key, value):
            '''void KAuth.Action.addArgument(QString key, QVariant value)'''
        def arguments(self):
            '''dict-of-QString-QVariant KAuth.Action.arguments()'''
            return dict-of-QString-QVariant()
        def setArguments(self, arguments):
            '''void KAuth.Action.setArguments(dict-of-QString-QVariant arguments)'''
        def watcher(self):
            '''KAuth.ActionWatcher KAuth.Action.watcher()'''
            return KAuth.ActionWatcher()
        def setHelperID(self, id):
            '''void KAuth.Action.setHelperID(QString id)'''
        def helperID(self):
            '''QString KAuth.Action.helperID()'''
            return QString()
        def isValid(self):
            '''bool KAuth.Action.isValid()'''
            return bool()
        def details(self):
            '''QString KAuth.Action.details()'''
            return QString()
        def setDetails(self, details):
            '''void KAuth.Action.setDetails(QString details)'''
        def setName(self, name):
            '''void KAuth.Action.setName(QString name)'''
        def name(self):
            '''QString KAuth.Action.name()'''
            return QString()
    class ActionReply():
        """"""
        # Enum KAuth.ActionReply.Error
        NoError = 0
        NoResponder = 0
        NoSuchAction = 0
        InvalidAction = 0
        AuthorizationDenied = 0
        UserCancelled = 0
        HelperBusy = 0
        DBusError = 0
    
        # Enum KAuth.ActionReply.Type
        KAuthError = 0
        HelperError = 0
        Success = 0
    
        AuthorizationDeniedReply = None # KAuth.ActionReply - member
        DBusErrorReply = None # KAuth.ActionReply - member
        HelperBusyReply = None # KAuth.ActionReply - member
        HelperErrorReply = None # KAuth.ActionReply - member
        InvalidActionReply = None # KAuth.ActionReply - member
        NoResponderReply = None # KAuth.ActionReply - member
        NoSuchActionReply = None # KAuth.ActionReply - member
        SuccessReply = None # KAuth.ActionReply - member
        UserCancelledReply = None # KAuth.ActionReply - member
        def __init__(self):
            '''void KAuth.ActionReply.__init__()'''
        def __init__(self, type):
            '''void KAuth.ActionReply.__init__(KAuth.ActionReply.Type type)'''
        def __init__(self, reply):
            '''void KAuth.ActionReply.__init__(KAuth.ActionReply reply)'''
        def __ne__(self, reply):
            '''bool KAuth.ActionReply.__ne__(KAuth.ActionReply reply)'''
            return bool()
        def __eq__(self, reply):
            '''bool KAuth.ActionReply.__eq__(KAuth.ActionReply reply)'''
            return bool()
        def deserialize(self, data):
            '''static KAuth.ActionReply KAuth.ActionReply.deserialize(QByteArray data)'''
            return KAuth.ActionReply()
        def serialized(self):
            '''QByteArray KAuth.ActionReply.serialized()'''
            return QByteArray()
        def setErrorDescription(self, error):
            '''void KAuth.ActionReply.setErrorDescription(QString error)'''
        def errorDescription(self):
            '''QString KAuth.ActionReply.errorDescription()'''
            return QString()
        def setErrorCode(self, errorCode):
            '''void KAuth.ActionReply.setErrorCode(int errorCode)'''
        def errorCode(self):
            '''int KAuth.ActionReply.errorCode()'''
            return int()
        def failed(self):
            '''bool KAuth.ActionReply.failed()'''
            return bool()
        def succeeded(self):
            '''bool KAuth.ActionReply.succeeded()'''
            return bool()
        def type(self):
            '''KAuth.ActionReply.Type KAuth.ActionReply.type()'''
            return KAuth.ActionReply.Type()
        def addData(self, key, value):
            '''void KAuth.ActionReply.addData(QString key, QVariant value)'''
        def data(self):
            '''dict-of-QString-QVariant KAuth.ActionReply.data()'''
            return dict-of-QString-QVariant()
        def setData(self, data):
            '''void KAuth.ActionReply.setData(dict-of-QString-QVariant data)'''


class KAuthorized():
    """"""
    def authorizeControlModules(self, menuIds):
        '''static QStringList KAuthorized.authorizeControlModules(QStringList menuIds)'''
        return QStringList()
    def authorizeControlModule(self, menuId):
        '''static bool KAuthorized.authorizeControlModule(QString menuId)'''
        return bool()
    def allowUrlAction(self, action, baseUrl, _destUrl):
        '''static void KAuthorized.allowUrlAction(QString action, KUrl baseUrl, KUrl _destUrl)'''
    def authorizeUrlAction(self, action, baseUrl, destUrl):
        '''static bool KAuthorized.authorizeUrlAction(QString action, KUrl baseUrl, KUrl destUrl)'''
        return bool()
    def authorizeKAction(self, action):
        '''static bool KAuthorized.authorizeKAction(QString action)'''
        return bool()
    def authorize(self, genericAction):
        '''static bool KAuthorized.authorize(QString genericAction)'''
        return bool()


class KAutoSaveFile(QFile):
    """"""
    def __init__(self, filename, parent = None):
        '''void KAutoSaveFile.__init__(KUrl filename, QObject parent = None)'''
    def __init__(self, parent = None):
        '''void KAutoSaveFile.__init__(QObject parent = None)'''
    def allStaleFiles(self, applicationName = QString()):
        '''static list-of-KAutoSaveFile KAutoSaveFile.allStaleFiles(QString applicationName = QString())'''
        return [KAutoSaveFile()]
    def staleFiles(self, filename, applicationName = QString()):
        '''static list-of-KAutoSaveFile KAutoSaveFile.staleFiles(KUrl filename, QString applicationName = QString())'''
        return [KAutoSaveFile()]
    def open(self, openmode):
        '''bool KAutoSaveFile.open(QIODevice.OpenMode openmode)'''
        return bool()
    def releaseLock(self):
        '''void KAutoSaveFile.releaseLock()'''
    def setManagedFile(self, filename):
        '''void KAutoSaveFile.setManagedFile(KUrl filename)'''
    def managedFile(self):
        '''KUrl KAutoSaveFile.managedFile()'''
        return KUrl()


class KAutostart(QObject):
    """"""
    # Enum KAutostart.StartPhase
    BaseDesktop = 0
    DesktopServices = 0
    Applications = 0

    # Enum KAutostart.Condition
    NoConditions = 0
    CheckCommand = 0
    CheckCondition = 0
    CheckAll = 0

    def __init__(self, entryName = QString(), parent = None):
        '''void KAutostart.__init__(QString entryName = QString(), QObject parent = None)'''
    def checkAllowedEnvironment(self, environment):
        '''bool KAutostart.checkAllowedEnvironment(QString environment)'''
        return bool()
    def startAfter(self):
        '''QString KAutostart.startAfter()'''
        return QString()
    def removeFromExcludedEnvironments(self, environment):
        '''void KAutostart.removeFromExcludedEnvironments(QString environment)'''
    def addToExcludedEnvironments(self, environment):
        '''void KAutostart.addToExcludedEnvironments(QString environment)'''
    def setExcludedEnvironments(self, environments):
        '''void KAutostart.setExcludedEnvironments(QStringList environments)'''
    def excludedEnvironments(self):
        '''QStringList KAutostart.excludedEnvironments()'''
        return QStringList()
    def removeFromAllowedEnvironments(self, environment):
        '''void KAutostart.removeFromAllowedEnvironments(QString environment)'''
    def addToAllowedEnvironments(self, environment):
        '''void KAutostart.addToAllowedEnvironments(QString environment)'''
    def setAllowedEnvironments(self, environments):
        '''void KAutostart.setAllowedEnvironments(QStringList environments)'''
    def allowedEnvironments(self):
        '''QStringList KAutostart.allowedEnvironments()'''
        return QStringList()
    def setStartPhase(self, phase):
        '''void KAutostart.setStartPhase(KAutostart.StartPhase phase)'''
    def startPhase(self):
        '''KAutostart.StartPhase KAutostart.startPhase()'''
        return KAutostart.StartPhase()
    def setCommandToCheck(self, exec_):
        '''void KAutostart.setCommandToCheck(QString exec)'''
    def commandToCheck(self):
        '''QString KAutostart.commandToCheck()'''
        return QString()
    def isServiceRegistered(self, entryName):
        '''static bool KAutostart.isServiceRegistered(QString entryName)'''
        return bool()
    def setVisibleName(self, entryName):
        '''void KAutostart.setVisibleName(QString entryName)'''
    def visibleName(self):
        '''QString KAutostart.visibleName()'''
        return QString()
    def setCommand(self, command):
        '''void KAutostart.setCommand(QString command)'''
    def command(self):
        '''QString KAutostart.command()'''
        return QString()
    def autostarts(self, environment = QString(), check = None):
        '''bool KAutostart.autostarts(QString environment = QString(), KAutostart.Conditions check = KAutostart.NoConditions)'''
        return bool()
    def setAutostarts(self, autostart):
        '''void KAutostart.setAutostarts(bool autostart)'''
    class Conditions():
        """"""
        def __init__(self):
            '''KAutostart.Conditions KAutostart.Conditions.__init__()'''
            return KAutostart.Conditions()
        def __init__(self):
            '''int KAutostart.Conditions.__init__()'''
            return int()
        def __init__(self):
            '''void KAutostart.Conditions.__init__()'''
        def __bool__(self):
            '''int KAutostart.Conditions.__bool__()'''
            return int()
        def __ne__(self, f):
            '''bool KAutostart.Conditions.__ne__(KAutostart.Conditions f)'''
            return bool()
        def __eq__(self, f):
            '''bool KAutostart.Conditions.__eq__(KAutostart.Conditions f)'''
            return bool()
        def __invert__(self):
            '''KAutostart.Conditions KAutostart.Conditions.__invert__()'''
            return KAutostart.Conditions()
        def __and__(self, mask):
            '''KAutostart.Conditions KAutostart.Conditions.__and__(int mask)'''
            return KAutostart.Conditions()
        def __xor__(self, f):
            '''KAutostart.Conditions KAutostart.Conditions.__xor__(KAutostart.Conditions f)'''
            return KAutostart.Conditions()
        def __xor__(self, f):
            '''KAutostart.Conditions KAutostart.Conditions.__xor__(int f)'''
            return KAutostart.Conditions()
        def __or__(self, f):
            '''KAutostart.Conditions KAutostart.Conditions.__or__(KAutostart.Conditions f)'''
            return KAutostart.Conditions()
        def __or__(self, f):
            '''KAutostart.Conditions KAutostart.Conditions.__or__(int f)'''
            return KAutostart.Conditions()
        def __int__(self):
            '''int KAutostart.Conditions.__int__()'''
            return int()
        def __ixor__(self, f):
            '''KAutostart.Conditions KAutostart.Conditions.__ixor__(KAutostart.Conditions f)'''
            return KAutostart.Conditions()
        def __ior__(self, f):
            '''KAutostart.Conditions KAutostart.Conditions.__ior__(KAutostart.Conditions f)'''
            return KAutostart.Conditions()
        def __iand__(self, mask):
            '''KAutostart.Conditions KAutostart.Conditions.__iand__(int mask)'''
            return KAutostart.Conditions()


class KCalendarSystem():
    """"""
    # Enum KCalendarSystem.WeekDayNameFormat
    ShortDayName = 0
    LongDayName = 0
    NarrowDayName = 0

    # Enum KCalendarSystem.MonthNameFormat
    ShortName = 0
    LongName = 0
    ShortNamePossessive = 0
    LongNamePossessive = 0
    NarrowName = 0

    # Enum KCalendarSystem.StringFormat
    ShortFormat = 0
    LongFormat = 0

    def __init__(self, locale = None):
        '''void KCalendarSystem.__init__(KLocale locale = None)'''
    def __init__(self, config, locale = None):
        '''void KCalendarSystem.__init__(unknown-type config, KLocale locale = None)'''
    def week(self, date, yearNum):
        '''int KCalendarSystem.week(QDate date, int yearNum)'''
        return int()
    def week(self, date, weekNumberSystem, yearNum):
        '''int KCalendarSystem.week(QDate date, KLocale.WeekNumberSystem weekNumberSystem, int yearNum)'''
        return int()
    def calendarSystemForCalendarType(self, calendarType):
        '''static KLocale.CalendarSystem KCalendarSystem.calendarSystemForCalendarType(QString calendarType)'''
        return KLocale.CalendarSystem()
    def applyShortYearWindow(self, inputYear):
        '''int KCalendarSystem.applyShortYearWindow(int inputYear)'''
        return int()
    def shortYearWindowStartYear(self):
        '''int KCalendarSystem.shortYearWindowStartYear()'''
        return int()
    def lastDayOfMonth(self, year, month):
        '''QDate KCalendarSystem.lastDayOfMonth(int year, int month)'''
        return QDate()
    def lastDayOfMonth(self, date = None):
        '''QDate KCalendarSystem.lastDayOfMonth(QDate date = QDate.currentDate())'''
        return QDate()
    def firstDayOfMonth(self, year, month):
        '''QDate KCalendarSystem.firstDayOfMonth(int year, int month)'''
        return QDate()
    def firstDayOfMonth(self, date = None):
        '''QDate KCalendarSystem.firstDayOfMonth(QDate date = QDate.currentDate())'''
        return QDate()
    def lastDayOfYear(self, year):
        '''QDate KCalendarSystem.lastDayOfYear(int year)'''
        return QDate()
    def lastDayOfYear(self, date = None):
        '''QDate KCalendarSystem.lastDayOfYear(QDate date = QDate.currentDate())'''
        return QDate()
    def firstDayOfYear(self, year):
        '''QDate KCalendarSystem.firstDayOfYear(int year)'''
        return QDate()
    def firstDayOfYear(self, date = None):
        '''QDate KCalendarSystem.firstDayOfYear(QDate date = QDate.currentDate())'''
        return QDate()
    def calendarSystem(self):
        '''KLocale.CalendarSystem KCalendarSystem.calendarSystem()'''
        return KLocale.CalendarSystem()
    def calendarSystem(self, calendarType):
        '''static KLocale.CalendarSystem KCalendarSystem.calendarSystem(QString calendarType)'''
        return KLocale.CalendarSystem()
    def calendarSystemsList(self):
        '''static list-of-KLocale.CalendarSystem KCalendarSystem.calendarSystemsList()'''
        return [KLocale.CalendarSystem()]
    def yearInEraString(self, date, format = None):
        '''QString KCalendarSystem.yearInEraString(QDate date, KCalendarSystem.StringFormat format = KCalendarSystem.ShortFormat)'''
        return QString()
    def daysDifference(self, fromDate, toDate):
        '''int KCalendarSystem.daysDifference(QDate fromDate, QDate toDate)'''
        return int()
    def monthsDifference(self, fromDate, toDate):
        '''int KCalendarSystem.monthsDifference(QDate fromDate, QDate toDate)'''
        return int()
    def yearsDifference(self, fromDate, toDate):
        '''int KCalendarSystem.yearsDifference(QDate fromDate, QDate toDate)'''
        return int()
    def dateDifference(self, fromDate, toDate, yearsDiff, monthsDiff, daysDiff, direction):
        '''void KCalendarSystem.dateDifference(QDate fromDate, QDate toDate, int yearsDiff, int monthsDiff, int daysDiff, int direction)'''
    def yearInEra(self, date):
        '''int KCalendarSystem.yearInEra(QDate date)'''
        return int()
    def eraYear(self, date, format = None):
        '''QString KCalendarSystem.eraYear(QDate date, KCalendarSystem.StringFormat format = KCalendarSystem.ShortFormat)'''
        return QString()
    def eraName(self, date, format = None):
        '''QString KCalendarSystem.eraName(QDate date, KCalendarSystem.StringFormat format = KCalendarSystem.ShortFormat)'''
        return QString()
    def getDate(self, date, year, month, day):
        '''void KCalendarSystem.getDate(QDate date, int year, int month, int day)'''
    def daysInWeekString(self, date):
        '''QString KCalendarSystem.daysInWeekString(QDate date)'''
        return QString()
    def daysInMonthString(self, pDate, format = None):
        '''QString KCalendarSystem.daysInMonthString(QDate pDate, KCalendarSystem.StringFormat format = KCalendarSystem.LongFormat)'''
        return QString()
    def daysInYearString(self, pDate, format = None):
        '''QString KCalendarSystem.daysInYearString(QDate pDate, KCalendarSystem.StringFormat format = KCalendarSystem.LongFormat)'''
        return QString()
    def weeksInYearString(self, pDate, format = None):
        '''QString KCalendarSystem.weeksInYearString(QDate pDate, KCalendarSystem.StringFormat format = KCalendarSystem.LongFormat)'''
        return QString()
    def monthsInYearString(self, pDate, format = None):
        '''QString KCalendarSystem.monthsInYearString(QDate pDate, KCalendarSystem.StringFormat format = KCalendarSystem.LongFormat)'''
        return QString()
    def weekNumberString(self, pDate, format = None):
        '''QString KCalendarSystem.weekNumberString(QDate pDate, KCalendarSystem.StringFormat format = KCalendarSystem.LongFormat)'''
        return QString()
    def dayOfWeekString(self, pDate):
        '''QString KCalendarSystem.dayOfWeekString(QDate pDate)'''
        return QString()
    def dayOfYearString(self, pDate, format = None):
        '''QString KCalendarSystem.dayOfYearString(QDate pDate, KCalendarSystem.StringFormat format = KCalendarSystem.LongFormat)'''
        return QString()
    def setDateIsoWeek(self, date, year, isoWeekNumber, dayOfIsoWeek):
        '''bool KCalendarSystem.setDateIsoWeek(QDate date, int year, int isoWeekNumber, int dayOfIsoWeek)'''
        return bool()
    def isValidIsoWeekDate(self, year, isoWeekNumber, dayOfIsoWeek):
        '''bool KCalendarSystem.isValidIsoWeekDate(int year, int isoWeekNumber, int dayOfIsoWeek)'''
        return bool()
    def setHasYear0(self, hasYear0):
        '''void KCalendarSystem.setHasYear0(bool hasYear0)'''
    def setMaxDaysInWeek(self, maxDays):
        '''void KCalendarSystem.setMaxDaysInWeek(int maxDays)'''
    def setMaxMonthsInYear(self, maxMonths):
        '''void KCalendarSystem.setMaxMonthsInYear(int maxMonths)'''
    def locale(self):
        '''KLocale KCalendarSystem.locale()'''
        return KLocale()
    def dateToJulianDay(self, year, month, day, jd):
        '''abstract bool KCalendarSystem.dateToJulianDay(int year, int month, int day, int jd)'''
        return bool()
    def julianDayToDate(self, jd, year, month, day):
        '''abstract bool KCalendarSystem.julianDayToDate(int jd, int year, int month, int day)'''
        return bool()
    def isProleptic(self):
        '''abstract bool KCalendarSystem.isProleptic()'''
        return bool()
    def isSolar(self):
        '''abstract bool KCalendarSystem.isSolar()'''
        return bool()
    def isLunisolar(self):
        '''abstract bool KCalendarSystem.isLunisolar()'''
        return bool()
    def isLunar(self):
        '''abstract bool KCalendarSystem.isLunar()'''
        return bool()
    def weekDayOfPray(self):
        '''abstract int KCalendarSystem.weekDayOfPray()'''
        return int()
    def weekStartDay(self):
        '''int KCalendarSystem.weekStartDay()'''
        return int()
    def readDate(self, str, ok):
        '''QDate KCalendarSystem.readDate(QString str, bool ok)'''
        return QDate()
    def readDate(self, dateString, dateFormat, ok):
        '''QDate KCalendarSystem.readDate(QString dateString, QString dateFormat, bool ok)'''
        return QDate()
    def readDate(self, str, flags, ok):
        '''QDate KCalendarSystem.readDate(QString str, KLocale.ReadDateFlags flags, bool ok)'''
        return QDate()
    def readDate(self, dateString, dateFormat, ok, formatStandard):
        '''QDate KCalendarSystem.readDate(QString dateString, QString dateFormat, bool ok, KLocale.DateTimeFormatStandard formatStandard)'''
        return QDate()
    def formatDate(self, fromDate, toFormat = None):
        '''QString KCalendarSystem.formatDate(QDate fromDate, KLocale.DateFormat toFormat = KLocale.LongDate)'''
        return QString()
    def formatDate(self, fromDate, toFormat, formatStandard = None):
        '''QString KCalendarSystem.formatDate(QDate fromDate, QString toFormat, KLocale.DateTimeFormatStandard formatStandard = KLocale.KdeFormat)'''
        return QString()
    def formatDate(self, fromDate, toFormat, digitSet, formatStandard = None):
        '''QString KCalendarSystem.formatDate(QDate fromDate, QString toFormat, KLocale.DigitSet digitSet, KLocale.DateTimeFormatStandard formatStandard = KLocale.KdeFormat)'''
        return QString()
    def formatDate(self, date, component, format = None, weekNumberSystem = None):
        '''QString KCalendarSystem.formatDate(QDate date, KLocale.DateTimeComponent component, KLocale.DateTimeComponentFormat format = KLocale.DefaultComponentFormat, KLocale.WeekNumberSystem weekNumberSystem = KLocale.DefaultWeekNumber)'''
        return QString()
    def dayStringToInteger(self, sNum, iLength):
        '''int KCalendarSystem.dayStringToInteger(QString sNum, int iLength)'''
        return int()
    def monthStringToInteger(self, sNum, iLength):
        '''int KCalendarSystem.monthStringToInteger(QString sNum, int iLength)'''
        return int()
    def yearStringToInteger(self, sNum, iLength):
        '''int KCalendarSystem.yearStringToInteger(QString sNum, int iLength)'''
        return int()
    def dayString(self, pDate, format = None):
        '''QString KCalendarSystem.dayString(QDate pDate, KCalendarSystem.StringFormat format = KCalendarSystem.LongFormat)'''
        return QString()
    def monthString(self, pDate, format = None):
        '''QString KCalendarSystem.monthString(QDate pDate, KCalendarSystem.StringFormat format = KCalendarSystem.LongFormat)'''
        return QString()
    def yearString(self, date, format = None):
        '''QString KCalendarSystem.yearString(QDate date, KCalendarSystem.StringFormat format = KCalendarSystem.LongFormat)'''
        return QString()
    def weekDayName(self, weekDay, format = None):
        '''abstract QString KCalendarSystem.weekDayName(int weekDay, KCalendarSystem.WeekDayNameFormat format = KCalendarSystem.LongDayName)'''
        return QString()
    def weekDayName(self, date, format = None):
        '''QString KCalendarSystem.weekDayName(QDate date, KCalendarSystem.WeekDayNameFormat format = KCalendarSystem.LongDayName)'''
        return QString()
    def monthName(self, month, year, format = None):
        '''abstract QString KCalendarSystem.monthName(int month, int year, KCalendarSystem.MonthNameFormat format = KCalendarSystem.LongName)'''
        return QString()
    def monthName(self, date, format = None):
        '''QString KCalendarSystem.monthName(QDate date, KCalendarSystem.MonthNameFormat format = KCalendarSystem.LongName)'''
        return QString()
    def isLeapYear(self, year):
        '''abstract bool KCalendarSystem.isLeapYear(int year)'''
        return bool()
    def isLeapYear(self, date):
        '''bool KCalendarSystem.isLeapYear(QDate date)'''
        return bool()
    def weekNumber(self, date, yearNum = None):
        '''int KCalendarSystem.weekNumber(QDate date, int yearNum = None)'''
        return int()
    def dayOfWeek(self, date):
        '''int KCalendarSystem.dayOfWeek(QDate date)'''
        return int()
    def dayOfYear(self, date):
        '''int KCalendarSystem.dayOfYear(QDate date)'''
        return int()
    def daysInWeek(self, date):
        '''int KCalendarSystem.daysInWeek(QDate date)'''
        return int()
    def daysInMonth(self, date):
        '''int KCalendarSystem.daysInMonth(QDate date)'''
        return int()
    def daysInMonth(self, year, month):
        '''int KCalendarSystem.daysInMonth(int year, int month)'''
        return int()
    def daysInYear(self, date):
        '''int KCalendarSystem.daysInYear(QDate date)'''
        return int()
    def daysInYear(self, year):
        '''int KCalendarSystem.daysInYear(int year)'''
        return int()
    def weeksInYear(self, date):
        '''int KCalendarSystem.weeksInYear(QDate date)'''
        return int()
    def weeksInYear(self, year):
        '''int KCalendarSystem.weeksInYear(int year)'''
        return int()
    def weeksInYear(self, year, weekNumberSystem):
        '''int KCalendarSystem.weeksInYear(int year, KLocale.WeekNumberSystem weekNumberSystem)'''
        return int()
    def monthsInYear(self, date):
        '''int KCalendarSystem.monthsInYear(QDate date)'''
        return int()
    def monthsInYear(self, year):
        '''int KCalendarSystem.monthsInYear(int year)'''
        return int()
    def addDays(self, date, ndays):
        '''QDate KCalendarSystem.addDays(QDate date, int ndays)'''
        return QDate()
    def addMonths(self, date, nmonths):
        '''QDate KCalendarSystem.addMonths(QDate date, int nmonths)'''
        return QDate()
    def addYears(self, date, nyears):
        '''QDate KCalendarSystem.addYears(QDate date, int nyears)'''
        return QDate()
    def day(self, date):
        '''int KCalendarSystem.day(QDate date)'''
        return int()
    def month(self, date):
        '''int KCalendarSystem.month(QDate date)'''
        return int()
    def year(self, date):
        '''int KCalendarSystem.year(QDate date)'''
        return int()
    def setYMD(self, date, y, m, d):
        '''bool KCalendarSystem.setYMD(QDate date, int y, int m, int d)'''
        return bool()
    def setDate(self, date, year, month, day):
        '''bool KCalendarSystem.setDate(QDate date, int year, int month, int day)'''
        return bool()
    def setDate(self, date, year, dayOfYear):
        '''bool KCalendarSystem.setDate(QDate date, int year, int dayOfYear)'''
        return bool()
    def setDate(self, date, eraName, yearInEra, month, day):
        '''bool KCalendarSystem.setDate(QDate date, QString eraName, int yearInEra, int month, int day)'''
        return bool()
    def isValid(self, year, month, day):
        '''abstract bool KCalendarSystem.isValid(int year, int month, int day)'''
        return bool()
    def isValid(self, date):
        '''bool KCalendarSystem.isValid(QDate date)'''
        return bool()
    def isValid(self, year, dayOfYear):
        '''bool KCalendarSystem.isValid(int year, int dayOfYear)'''
        return bool()
    def isValid(self, eraName, yearInEra, month, day):
        '''bool KCalendarSystem.isValid(QString eraName, int yearInEra, int month, int day)'''
        return bool()
    def latestValidDate(self):
        '''QDate KCalendarSystem.latestValidDate()'''
        return QDate()
    def earliestValidDate(self):
        '''QDate KCalendarSystem.earliestValidDate()'''
        return QDate()
    def epoch(self):
        '''QDate KCalendarSystem.epoch()'''
        return QDate()
    def calendarType(self):
        '''abstract QString KCalendarSystem.calendarType()'''
        return QString()
    def calendarType(self, calendarSystem):
        '''static QString KCalendarSystem.calendarType(KLocale.CalendarSystem calendarSystem)'''
        return QString()
    def calendarLabel(self, calendarType):
        '''static QString KCalendarSystem.calendarLabel(QString calendarType)'''
        return QString()
    def calendarLabel(self, calendarSystem, locale = None):
        '''static QString KCalendarSystem.calendarLabel(KLocale.CalendarSystem calendarSystem, KLocale locale = KGlobal.locale())'''
        return QString()
    def calendarLabel(self):
        '''QString KCalendarSystem.calendarLabel()'''
        return QString()
    def calendarSystems(self):
        '''static QStringList KCalendarSystem.calendarSystems()'''
        return QStringList()
    def create(self, calType = QLatin1Stringgregorian, locale = None):
        '''static KCalendarSystem KCalendarSystem.create(QString calType = QLatin1Stringgregorian, KLocale locale = None)'''
        return KCalendarSystem()
    def create(self, calType, config, locale = None):
        '''static KCalendarSystem KCalendarSystem.create(QString calType, unknown-type config, KLocale locale = None)'''
        return KCalendarSystem()
    def create(self, calendarSystem, locale = None):
        '''static KCalendarSystem KCalendarSystem.create(KLocale.CalendarSystem calendarSystem, KLocale locale = None)'''
        return KCalendarSystem()
    def create(self, calendarSystem, config, locale = None):
        '''static KCalendarSystem KCalendarSystem.create(KLocale.CalendarSystem calendarSystem, unknown-type config, KLocale locale = None)'''
        return KCalendarSystem()


class KGlobal():
    """"""
    # Enum KGlobal.CopyCatalogs
    DoCopyCatalogs = 0
    DontCopyCatalogs = 0

    def insertCatalog(self, catalog):
        '''static void KGlobal.insertCatalog(QString catalog)'''
    def findDirectChild_helper(self, parent, mo):
        '''static QObject KGlobal.findDirectChild_helper(QObject parent, QMetaObject mo)'''
        return QObject()
    def setLocale(self, copy = None):
        '''static KLocale KGlobal.setLocale(KGlobal.CopyCatalogs copy = KGlobal.DoCopyCatalogs)'''
        return KLocale()
    def caption(self):
        '''static QString KGlobal.caption()'''
        return QString()
    def setActiveComponent(self, d):
        '''static void KGlobal.setActiveComponent(KComponentData d)'''
    def activeComponent(self):
        '''static KComponentData KGlobal.activeComponent()'''
        return KComponentData()
    def setAllowQuit(self, allowQuit):
        '''static void KGlobal.setAllowQuit(bool allowQuit)'''
    def deref(self):
        '''static void KGlobal.deref()'''
    def ref(self):
        '''static void KGlobal.ref()'''
    def staticQString(self, str):
        '''static QString KGlobal.staticQString(str str)'''
        return QString()
    def staticQString(self, str):
        '''static QString KGlobal.staticQString(QString str)'''
        return QString()
    def umask(self):
        '''static int KGlobal.umask()'''
        return int()
    def hasLocale(self):
        '''static bool KGlobal.hasLocale()'''
        return bool()
    def locale(self):
        '''static KLocale KGlobal.locale()'''
        return KLocale()
    def config(self):
        '''static KSharedConfigPtr KGlobal.config()'''
        return KSharedConfigPtr()
    def dirs(self):
        '''static KStandardDirs KGlobal.dirs()'''
        return KStandardDirs()
    def hasMainComponent(self):
        '''static bool KGlobal.hasMainComponent()'''
        return bool()
    def mainComponent(self):
        '''static KComponentData KGlobal.mainComponent()'''
        return KComponentData()
    def charsets(self):
        '''static KCharsets KGlobal.charsets()'''
        return KCharsets()


class KCharsets():
    """"""
    def __init__(self):
        '''void KCharsets.__init__()'''
    def encodingForName(self, descriptiveName):
        '''QString KCharsets.encodingForName(QString descriptiveName)'''
        return QString()
    def descriptionForEncoding(self, encoding):
        '''QString KCharsets.descriptionForEncoding(QString encoding)'''
        return QString()
    def languageForEncoding(self, encoding):
        '''QString KCharsets.languageForEncoding(QString encoding)'''
        return QString()
    def encodingsByScript(self):
        '''list-of-QStringList KCharsets.encodingsByScript()'''
        return [QStringList()]
    def descriptiveEncodingNames(self):
        '''QStringList KCharsets.descriptiveEncodingNames()'''
        return QStringList()
    def availableEncodingNames(self):
        '''QStringList KCharsets.availableEncodingNames()'''
        return QStringList()
    def resolveEntities(self, text):
        '''static QString KCharsets.resolveEntities(QString text)'''
        return QString()
    def toEntity(self, ch):
        '''static QString KCharsets.toEntity(QChar ch)'''
        return QString()
    def fromEntity2(self, str, len):
        '''static QChar KCharsets.fromEntity2(QString str, int len)'''
        return QChar()
    def fromEntity(self, str):
        '''static QChar KCharsets.fromEntity(QString str)'''
        return QChar()
    def codecForName2(self, n, ok):
        '''QTextCodec KCharsets.codecForName2(QString n, bool ok)'''
        return QTextCodec()
    def codecForName(self, name):
        '''QTextCodec KCharsets.codecForName(QString name)'''
        return QTextCodec()


class KCmdLineOptions():
    """"""
    def __init__(self):
        '''void KCmdLineOptions.__init__()'''
    def __init__(self, options):
        '''void KCmdLineOptions.__init__(KCmdLineOptions options)'''
    def add(self, name, description = KLocalizedString(), defaultValue = QByteArray()):
        '''KCmdLineOptions KCmdLineOptions.add(QByteArray name, KLocalizedString description = KLocalizedString(), QByteArray defaultValue = QByteArray())'''
        return KCmdLineOptions()
    def add(self, options):
        '''KCmdLineOptions KCmdLineOptions.add(KCmdLineOptions options)'''
        return KCmdLineOptions()


class KCmdLineArgs():
    """"""
    # Enum KCmdLineArgs.StdCmdLineArg
    CmdLineArgQt = 0
    CmdLineArgKDE = 0
    CmdLineArgsMask = 0
    CmdLineArgNone = 0
    Reserved = 0

    def __init__(self, _options, _name, _id):
        '''void KCmdLineArgs.__init__(KCmdLineOptions _options, KLocalizedString _name, QByteArray _id)'''
    def allArguments(self):
        '''static QStringList KCmdLineArgs.allArguments()'''
        return QStringList()
    def aboutData(self):
        '''static KAboutData KCmdLineArgs.aboutData()'''
        return KAboutData()
    def isTempFileSet(self):
        '''static bool KCmdLineArgs.isTempFileSet()'''
        return bool()
    def addTempFileOption(self):
        '''static void KCmdLineArgs.addTempFileOption()'''
    def saveAppArgs(self):
        '''static QDataStream KCmdLineArgs.saveAppArgs()'''
        return QDataStream()
    def loadAppArgs(self):
        '''static QDataStream KCmdLineArgs.loadAppArgs()'''
        return QDataStream()
    def reset(self):
        '''static void KCmdLineArgs.reset()'''
    def clear(self):
        '''void KCmdLineArgs.clear()'''
    def setCwd(self, cwd):
        '''static void KCmdLineArgs.setCwd(QByteArray cwd)'''
    def makeURL(self, urlArg):
        '''static KUrl KCmdLineArgs.makeURL(QByteArray urlArg)'''
        return KUrl()
    def url(self, n):
        '''KUrl KCmdLineArgs.url(int n)'''
        return KUrl()
    def arg(self, n):
        '''QString KCmdLineArgs.arg(int n)'''
        return QString()
    def count(self):
        '''int KCmdLineArgs.count()'''
        return int()
    def isSet(self, option):
        '''bool KCmdLineArgs.isSet(QByteArray option)'''
        return bool()
    def getOptionList(self, option):
        '''QStringList KCmdLineArgs.getOptionList(QByteArray option)'''
        return QStringList()
    def getOption(self, option):
        '''QString KCmdLineArgs.getOption(QByteArray option)'''
        return QString()
    def enable_i18n(self):
        '''static void KCmdLineArgs.enable_i18n()'''
    def usageError(self, error):
        '''static void KCmdLineArgs.usageError(QString error)'''
    def usage(self, id = QByteArray()):
        '''static void KCmdLineArgs.usage(QByteArray id = QByteArray())'''
    def appName(self):
        '''static QString KCmdLineArgs.appName()'''
        return QString()
    def cwd(self):
        '''static QString KCmdLineArgs.cwd()'''
        return QString()
    def parsedArgs(self, id = QByteArray()):
        '''static KCmdLineArgs KCmdLineArgs.parsedArgs(QByteArray id = QByteArray())'''
        return KCmdLineArgs()
    def addCmdLineOptions(self, options, name = KLocalizedString(), id = QByteArray(), afterId = QByteArray()):
        '''static void KCmdLineArgs.addCmdLineOptions(KCmdLineOptions options, KLocalizedString name = KLocalizedString(), QByteArray id = QByteArray(), QByteArray afterId = QByteArray())'''
    def addStdCmdLineOptions(self, stdargs = None):
        '''static void KCmdLineArgs.addStdCmdLineOptions(KCmdLineArgs.StdCmdLineArgs stdargs = KCmdLineArgs.StdCmdLineArgs(KCmdLineArgs.CmdLineArgQt|KCmdLineArgs.CmdLineArgKDE))'''
    def init(self, argv, appname, catalog, programName, version, description = KLocalizedString(), stdargs = 3):
        '''static void KCmdLineArgs.init(list argv, QByteArray appname, QByteArray catalog, KLocalizedString programName, QByteArray version, KLocalizedString description = KLocalizedString(), int stdargs = 3)'''
    def init(self, argv, about, stdargs = 3):
        '''static void KCmdLineArgs.init(list argv, KAboutData about, int stdargs = 3)'''
    def init(self, about):
        '''static void KCmdLineArgs.init(KAboutData about)'''
    class StdCmdLineArgs():
        """"""
        def __init__(self):
            '''KCmdLineArgs.StdCmdLineArgs KCmdLineArgs.StdCmdLineArgs.__init__()'''
            return KCmdLineArgs.StdCmdLineArgs()
        def __init__(self):
            '''int KCmdLineArgs.StdCmdLineArgs.__init__()'''
            return int()
        def __init__(self):
            '''void KCmdLineArgs.StdCmdLineArgs.__init__()'''
        def __bool__(self):
            '''int KCmdLineArgs.StdCmdLineArgs.__bool__()'''
            return int()
        def __ne__(self, f):
            '''bool KCmdLineArgs.StdCmdLineArgs.__ne__(KCmdLineArgs.StdCmdLineArgs f)'''
            return bool()
        def __eq__(self, f):
            '''bool KCmdLineArgs.StdCmdLineArgs.__eq__(KCmdLineArgs.StdCmdLineArgs f)'''
            return bool()
        def __invert__(self):
            '''KCmdLineArgs.StdCmdLineArgs KCmdLineArgs.StdCmdLineArgs.__invert__()'''
            return KCmdLineArgs.StdCmdLineArgs()
        def __and__(self, mask):
            '''KCmdLineArgs.StdCmdLineArgs KCmdLineArgs.StdCmdLineArgs.__and__(int mask)'''
            return KCmdLineArgs.StdCmdLineArgs()
        def __xor__(self, f):
            '''KCmdLineArgs.StdCmdLineArgs KCmdLineArgs.StdCmdLineArgs.__xor__(KCmdLineArgs.StdCmdLineArgs f)'''
            return KCmdLineArgs.StdCmdLineArgs()
        def __xor__(self, f):
            '''KCmdLineArgs.StdCmdLineArgs KCmdLineArgs.StdCmdLineArgs.__xor__(int f)'''
            return KCmdLineArgs.StdCmdLineArgs()
        def __or__(self, f):
            '''KCmdLineArgs.StdCmdLineArgs KCmdLineArgs.StdCmdLineArgs.__or__(KCmdLineArgs.StdCmdLineArgs f)'''
            return KCmdLineArgs.StdCmdLineArgs()
        def __or__(self, f):
            '''KCmdLineArgs.StdCmdLineArgs KCmdLineArgs.StdCmdLineArgs.__or__(int f)'''
            return KCmdLineArgs.StdCmdLineArgs()
        def __int__(self):
            '''int KCmdLineArgs.StdCmdLineArgs.__int__()'''
            return int()
        def __ixor__(self, f):
            '''KCmdLineArgs.StdCmdLineArgs KCmdLineArgs.StdCmdLineArgs.__ixor__(KCmdLineArgs.StdCmdLineArgs f)'''
            return KCmdLineArgs.StdCmdLineArgs()
        def __ior__(self, f):
            '''KCmdLineArgs.StdCmdLineArgs KCmdLineArgs.StdCmdLineArgs.__ior__(KCmdLineArgs.StdCmdLineArgs f)'''
            return KCmdLineArgs.StdCmdLineArgs()
        def __iand__(self, mask):
            '''KCmdLineArgs.StdCmdLineArgs KCmdLineArgs.StdCmdLineArgs.__iand__(int mask)'''
            return KCmdLineArgs.StdCmdLineArgs()


class KComponentData():
    """"""
    # Enum KComponentData.MainComponentRegistration
    RegisterAsMainComponent = 0
    SkipMainComponentRegistration = 0

    def __init__(self):
        '''void KComponentData.__init__()'''
    def __init__(self):
        '''KComponentData KComponentData.__init__()'''
        return KComponentData()
    def __init__(self, componentName, catalogName = QByteArray(), registerAsMain = None):
        '''void KComponentData.__init__(QByteArray componentName, QByteArray catalogName = QByteArray(), KComponentData.MainComponentRegistration registerAsMain = KComponentData.RegisterAsMainComponent)'''
    def __init__(self, aboutData, registerAsMain = None):
        '''void KComponentData.__init__(KAboutData aboutData, KComponentData.MainComponentRegistration registerAsMain = KComponentData.RegisterAsMainComponent)'''
    def __init__(self, aboutData, registerAsMain = None):
        '''void KComponentData.__init__(KAboutData aboutData, KComponentData.MainComponentRegistration registerAsMain = KComponentData.RegisterAsMainComponent)'''
    def setAboutData(self, aboutData):
        '''void KComponentData.setAboutData(KAboutData aboutData)'''
    def setConfigName(self, name):
        '''void KComponentData.setConfigName(QString name)'''
    def catalogName(self):
        '''QString KComponentData.catalogName()'''
        return QString()
    def componentName(self):
        '''QString KComponentData.componentName()'''
        return QString()
    def aboutData(self):
        '''KAboutData KComponentData.aboutData()'''
        return KAboutData()
    def config(self):
        '''unknown-type KComponentData.config()'''
        return unknown-type()
    def dirs(self):
        '''KStandardDirs KComponentData.dirs()'''
        return KStandardDirs()
    def isValid(self):
        '''bool KComponentData.isValid()'''
        return bool()
    def __ne__(self, rhs):
        '''bool KComponentData.__ne__(KComponentData rhs)'''
        return bool()
    def __eq__(self):
        '''KComponentData KComponentData.__eq__()'''
        return KComponentData()


class KJob(QObject):
    """"""
    NoError = None # int - member
    KilledJobError = None # int - member
    UserDefinedError = None # int - member
    # Enum KJob.KillVerbosity
    Quietly = 0
    EmitResult = 0

    # Enum KJob.Capability
    NoCapabilities = 0
    Killable = 0
    Suspendable = 0

    # Enum KJob.Unit
    Bytes = 0
    Files = 0
    Directories = 0

    def __init__(self, parent = None):
        '''void KJob.__init__(QObject parent = None)'''
    def emitSpeed(self, speed):
        '''void KJob.emitSpeed(int speed)'''
    def emitPercent(self, processedAmount, totalAmount):
        '''void KJob.emitPercent(int processedAmount, int totalAmount)'''
    def emitResult(self):
        '''void KJob.emitResult()'''
    def setPercent(self, percentage):
        '''void KJob.setPercent(int percentage)'''
    def setTotalAmount(self, unit, amount):
        '''void KJob.setTotalAmount(KJob.Unit unit, int amount)'''
    def setProcessedAmount(self, unit, amount):
        '''void KJob.setProcessedAmount(KJob.Unit unit, int amount)'''
    def setErrorText(self, errorText):
        '''void KJob.setErrorText(QString errorText)'''
    def setError(self, errorCode):
        '''void KJob.setError(int errorCode)'''
    warning = pyqtSignal() # void warning(KJob *,const QStringamp;,const QStringamp; = QString()) - signal
    infoMessage = pyqtSignal() # void infoMessage(KJob *,const QStringamp;,const QStringamp; = QString()) - signal
    description = pyqtSignal() # void description(KJob *,const QStringamp;,const QPairlt;QString,QStringgt;amp; = qMakePair(QString(),QString()),const QPairlt;QString,QStringgt;amp; = qMakePair(QString(),QString())) - signal
    result = pyqtSignal() # void result(KJob *) - signal
    def isAutoDelete(self):
        '''bool KJob.isAutoDelete()'''
        return bool()
    def setAutoDelete(self, autodelete):
        '''void KJob.setAutoDelete(bool autodelete)'''
    def percent(self):
        '''int KJob.percent()'''
        return int()
    def totalAmount(self, unit):
        '''int KJob.totalAmount(KJob.Unit unit)'''
        return int()
    def processedAmount(self, unit):
        '''int KJob.processedAmount(KJob.Unit unit)'''
        return int()
    def errorString(self):
        '''QString KJob.errorString()'''
        return QString()
    def errorText(self):
        '''QString KJob.errorText()'''
        return QString()
    def error(self):
        '''int KJob.error()'''
        return int()
    def exec_(self):
        '''bool KJob.exec_()'''
        return bool()
    def setCapabilities(self, capabilities):
        '''void KJob.setCapabilities(KJob.Capabilities capabilities)'''
    def doResume(self):
        '''bool KJob.doResume()'''
        return bool()
    def doSuspend(self):
        '''bool KJob.doSuspend()'''
        return bool()
    def doKill(self):
        '''bool KJob.doKill()'''
        return bool()
    def resume(self):
        '''bool KJob.resume()'''
        return bool()
    def suspend(self):
        '''bool KJob.suspend()'''
        return bool()
    def kill(self, verbosity = None):
        '''bool KJob.kill(KJob.KillVerbosity verbosity = KJob.Quietly)'''
        return bool()
    def start(self):
        '''abstract void KJob.start()'''
    def isSuspended(self):
        '''bool KJob.isSuspended()'''
        return bool()
    def capabilities(self):
        '''KJob.Capabilities KJob.capabilities()'''
        return KJob.Capabilities()
    def uiDelegate(self):
        '''KJobUiDelegate KJob.uiDelegate()'''
        return KJobUiDelegate()
    def setUiDelegate(self, delegate):
        '''void KJob.setUiDelegate(KJobUiDelegate delegate)'''
    class Capabilities():
        """"""
        def __init__(self):
            '''KJob.Capabilities KJob.Capabilities.__init__()'''
            return KJob.Capabilities()
        def __init__(self):
            '''int KJob.Capabilities.__init__()'''
            return int()
        def __init__(self):
            '''void KJob.Capabilities.__init__()'''
        def __bool__(self):
            '''int KJob.Capabilities.__bool__()'''
            return int()
        def __ne__(self, f):
            '''bool KJob.Capabilities.__ne__(KJob.Capabilities f)'''
            return bool()
        def __eq__(self, f):
            '''bool KJob.Capabilities.__eq__(KJob.Capabilities f)'''
            return bool()
        def __invert__(self):
            '''KJob.Capabilities KJob.Capabilities.__invert__()'''
            return KJob.Capabilities()
        def __and__(self, mask):
            '''KJob.Capabilities KJob.Capabilities.__and__(int mask)'''
            return KJob.Capabilities()
        def __xor__(self, f):
            '''KJob.Capabilities KJob.Capabilities.__xor__(KJob.Capabilities f)'''
            return KJob.Capabilities()
        def __xor__(self, f):
            '''KJob.Capabilities KJob.Capabilities.__xor__(int f)'''
            return KJob.Capabilities()
        def __or__(self, f):
            '''KJob.Capabilities KJob.Capabilities.__or__(KJob.Capabilities f)'''
            return KJob.Capabilities()
        def __or__(self, f):
            '''KJob.Capabilities KJob.Capabilities.__or__(int f)'''
            return KJob.Capabilities()
        def __int__(self):
            '''int KJob.Capabilities.__int__()'''
            return int()
        def __ixor__(self, f):
            '''KJob.Capabilities KJob.Capabilities.__ixor__(KJob.Capabilities f)'''
            return KJob.Capabilities()
        def __ior__(self, f):
            '''KJob.Capabilities KJob.Capabilities.__ior__(KJob.Capabilities f)'''
            return KJob.Capabilities()
        def __iand__(self, mask):
            '''KJob.Capabilities KJob.Capabilities.__iand__(int mask)'''
            return KJob.Capabilities()


class KCompositeJob(KJob):
    """"""
    def __init__(self, parent = None):
        '''void KCompositeJob.__init__(QObject parent = None)'''
    def slotInfoMessage(self, job, plain, rich):
        '''void KCompositeJob.slotInfoMessage(KJob job, QString plain, QString rich)'''
    def slotResult(self, job):
        '''void KCompositeJob.slotResult(KJob job)'''
    def clearSubjobs(self):
        '''void KCompositeJob.clearSubjobs()'''
    def subjobs(self):
        '''list-of-KJob KCompositeJob.subjobs()'''
        return [KJob()]
    def hasSubjobs(self):
        '''bool KCompositeJob.hasSubjobs()'''
        return bool()
    def removeSubjob(self, job):
        '''bool KCompositeJob.removeSubjob(KJob job)'''
        return bool()
    def addSubjob(self, job):
        '''bool KCompositeJob.addSubjob(KJob job)'''
        return bool()


class KConfigBase():
    """"""
    # Enum KConfigBase.AccessMode
    NoAccess = 0
    ReadOnly = 0
    ReadWrite = 0

    # Enum KConfigBase.WriteConfigFlag
    Persistent = 0
    Global = 0
    Localized = 0
    Normal = 0

    def __init__(self):
        '''void KConfigBase.__init__()'''
    def __init__(self):
        '''KConfigBase KConfigBase.__init__()'''
        return KConfigBase()
    def isGroupImmutableImpl(self, aGroup):
        '''abstract bool KConfigBase.isGroupImmutableImpl(QByteArray aGroup)'''
        return bool()
    def deleteGroupImpl(self, group, flags = None):
        '''abstract void KConfigBase.deleteGroupImpl(QByteArray group, KConfigBase.WriteConfigFlags flags = KConfigBase.Normal)'''
    def groupImpl(self, b):
        '''abstract KConfigGroup KConfigBase.groupImpl(QByteArray b)'''
        return KConfigGroup()
    def hasGroupImpl(self, group):
        '''abstract bool KConfigBase.hasGroupImpl(QByteArray group)'''
        return bool()
    def isGroupImmutable(self, aGroup):
        '''bool KConfigBase.isGroupImmutable(QByteArray aGroup)'''
        return bool()
    def isGroupImmutable(self, aGroup):
        '''bool KConfigBase.isGroupImmutable(QString aGroup)'''
        return bool()
    def isGroupImmutable(self, aGroup):
        '''bool KConfigBase.isGroupImmutable(str aGroup)'''
        return bool()
    def isImmutable(self):
        '''abstract bool KConfigBase.isImmutable()'''
        return bool()
    def accessMode(self):
        '''abstract KConfigBase.AccessMode KConfigBase.accessMode()'''
        return KConfigBase.AccessMode()
    def markAsClean(self):
        '''abstract void KConfigBase.markAsClean()'''
    def sync(self):
        '''abstract void KConfigBase.sync()'''
    def deleteGroup(self, group, flags = None):
        '''void KConfigBase.deleteGroup(QByteArray group, KConfigBase.WriteConfigFlags flags = KConfigBase.Normal)'''
    def deleteGroup(self, group, flags = None):
        '''void KConfigBase.deleteGroup(QString group, KConfigBase.WriteConfigFlags flags = KConfigBase.Normal)'''
    def deleteGroup(self, group, flags = None):
        '''void KConfigBase.deleteGroup(str group, KConfigBase.WriteConfigFlags flags = KConfigBase.Normal)'''
    def group(self, group):
        '''KConfigGroup KConfigBase.group(QByteArray group)'''
        return KConfigGroup()
    def group(self, group):
        '''KConfigGroup KConfigBase.group(QString group)'''
        return KConfigGroup()
    def group(self, group):
        '''KConfigGroup KConfigBase.group(str group)'''
        return KConfigGroup()
    def hasGroup(self, group):
        '''bool KConfigBase.hasGroup(QString group)'''
        return bool()
    def hasGroup(self, group):
        '''bool KConfigBase.hasGroup(str group)'''
        return bool()
    def hasGroup(self, group):
        '''bool KConfigBase.hasGroup(QByteArray group)'''
        return bool()
    def groupList(self):
        '''abstract QStringList KConfigBase.groupList()'''
        return QStringList()
    class WriteConfigFlags():
        """"""
        def __init__(self):
            '''KConfigBase.WriteConfigFlags KConfigBase.WriteConfigFlags.__init__()'''
            return KConfigBase.WriteConfigFlags()
        def __init__(self):
            '''int KConfigBase.WriteConfigFlags.__init__()'''
            return int()
        def __init__(self):
            '''void KConfigBase.WriteConfigFlags.__init__()'''
        def __bool__(self):
            '''int KConfigBase.WriteConfigFlags.__bool__()'''
            return int()
        def __ne__(self, f):
            '''bool KConfigBase.WriteConfigFlags.__ne__(KConfigBase.WriteConfigFlags f)'''
            return bool()
        def __eq__(self, f):
            '''bool KConfigBase.WriteConfigFlags.__eq__(KConfigBase.WriteConfigFlags f)'''
            return bool()
        def __invert__(self):
            '''KConfigBase.WriteConfigFlags KConfigBase.WriteConfigFlags.__invert__()'''
            return KConfigBase.WriteConfigFlags()
        def __and__(self, mask):
            '''KConfigBase.WriteConfigFlags KConfigBase.WriteConfigFlags.__and__(int mask)'''
            return KConfigBase.WriteConfigFlags()
        def __xor__(self, f):
            '''KConfigBase.WriteConfigFlags KConfigBase.WriteConfigFlags.__xor__(KConfigBase.WriteConfigFlags f)'''
            return KConfigBase.WriteConfigFlags()
        def __xor__(self, f):
            '''KConfigBase.WriteConfigFlags KConfigBase.WriteConfigFlags.__xor__(int f)'''
            return KConfigBase.WriteConfigFlags()
        def __or__(self, f):
            '''KConfigBase.WriteConfigFlags KConfigBase.WriteConfigFlags.__or__(KConfigBase.WriteConfigFlags f)'''
            return KConfigBase.WriteConfigFlags()
        def __or__(self, f):
            '''KConfigBase.WriteConfigFlags KConfigBase.WriteConfigFlags.__or__(int f)'''
            return KConfigBase.WriteConfigFlags()
        def __int__(self):
            '''int KConfigBase.WriteConfigFlags.__int__()'''
            return int()
        def __ixor__(self, f):
            '''KConfigBase.WriteConfigFlags KConfigBase.WriteConfigFlags.__ixor__(KConfigBase.WriteConfigFlags f)'''
            return KConfigBase.WriteConfigFlags()
        def __ior__(self, f):
            '''KConfigBase.WriteConfigFlags KConfigBase.WriteConfigFlags.__ior__(KConfigBase.WriteConfigFlags f)'''
            return KConfigBase.WriteConfigFlags()
        def __iand__(self, mask):
            '''KConfigBase.WriteConfigFlags KConfigBase.WriteConfigFlags.__iand__(int mask)'''
            return KConfigBase.WriteConfigFlags()


class KConfig(KConfigBase):
    """"""
    # Enum KConfig.OpenFlag
    IncludeGlobals = 0
    CascadeConfig = 0
    SimpleConfig = 0
    NoCascade = 0
    NoGlobals = 0
    FullConfig = 0

    def __init__(self, file = QString(), mode = None, resourceType = config):
        '''void KConfig.__init__(QString file = QString(), KConfig.OpenFlags mode = KConfig.FullConfig, str resourceType = config)'''
    def __init__(self, componentData, file = QString(), mode = None, resourceType = config):
        '''void KConfig.__init__(KComponentData componentData, QString file = QString(), KConfig.OpenFlags mode = KConfig.FullConfig, str resourceType = config)'''
    def __init__(self, file, backend, resourceType = config):
        '''void KConfig.__init__(QString file, QString backend, str resourceType = config)'''
    def isGroupImmutableImpl(self, aGroup):
        '''bool KConfig.isGroupImmutableImpl(QByteArray aGroup)'''
        return bool()
    def deleteGroupImpl(self, group, flags = None):
        '''void KConfig.deleteGroupImpl(QByteArray group, KConfigBase.WriteConfigFlags flags = KConfigBase.Normal)'''
    def groupImpl(self, b):
        '''KConfigGroup KConfig.groupImpl(QByteArray b)'''
        return KConfigGroup()
    def hasGroupImpl(self, group):
        '''bool KConfig.hasGroupImpl(QByteArray group)'''
        return bool()
    def entryMap(self, aGroup = QString()):
        '''dict-of-QString-QString KConfig.entryMap(QString aGroup = QString())'''
        return dict-of-QString-QString()
    def groupList(self):
        '''QStringList KConfig.groupList()'''
        return QStringList()
    def forceGlobal(self):
        '''bool KConfig.forceGlobal()'''
        return bool()
    def setForceGlobal(self, force):
        '''void KConfig.setForceGlobal(bool force)'''
    def isImmutable(self):
        '''bool KConfig.isImmutable()'''
        return bool()
    def readDefaults(self):
        '''bool KConfig.readDefaults()'''
        return bool()
    def setReadDefaults(self, b):
        '''void KConfig.setReadDefaults(bool b)'''
    def setLocale(self, aLocale):
        '''bool KConfig.setLocale(QString aLocale)'''
        return bool()
    def locale(self):
        '''QString KConfig.locale()'''
        return QString()
    def addConfigSources(self, sources):
        '''void KConfig.addConfigSources(QStringList sources)'''
    def reparseConfiguration(self):
        '''void KConfig.reparseConfiguration()'''
    def checkUpdate(self, id, updateFile):
        '''void KConfig.checkUpdate(QString id, QString updateFile)'''
    def copyTo(self, file, config = None):
        '''KConfig KConfig.copyTo(QString file, KConfig config = None)'''
        return KConfig()
    def isConfigWritable(self, warnUser):
        '''bool KConfig.isConfigWritable(bool warnUser)'''
        return bool()
    def accessMode(self):
        '''KConfigBase.AccessMode KConfig.accessMode()'''
        return KConfigBase.AccessMode()
    def markAsClean(self):
        '''void KConfig.markAsClean()'''
    def sync(self):
        '''void KConfig.sync()'''
    def name(self):
        '''QString KConfig.name()'''
        return QString()
    def componentData(self):
        '''KComponentData KConfig.componentData()'''
        return KComponentData()
    class OpenFlags():
        """"""
        def __init__(self):
            '''KConfig.OpenFlags KConfig.OpenFlags.__init__()'''
            return KConfig.OpenFlags()
        def __init__(self):
            '''int KConfig.OpenFlags.__init__()'''
            return int()
        def __init__(self):
            '''void KConfig.OpenFlags.__init__()'''
        def __bool__(self):
            '''int KConfig.OpenFlags.__bool__()'''
            return int()
        def __ne__(self, f):
            '''bool KConfig.OpenFlags.__ne__(KConfig.OpenFlags f)'''
            return bool()
        def __eq__(self, f):
            '''bool KConfig.OpenFlags.__eq__(KConfig.OpenFlags f)'''
            return bool()
        def __invert__(self):
            '''KConfig.OpenFlags KConfig.OpenFlags.__invert__()'''
            return KConfig.OpenFlags()
        def __and__(self, mask):
            '''KConfig.OpenFlags KConfig.OpenFlags.__and__(int mask)'''
            return KConfig.OpenFlags()
        def __xor__(self, f):
            '''KConfig.OpenFlags KConfig.OpenFlags.__xor__(KConfig.OpenFlags f)'''
            return KConfig.OpenFlags()
        def __xor__(self, f):
            '''KConfig.OpenFlags KConfig.OpenFlags.__xor__(int f)'''
            return KConfig.OpenFlags()
        def __or__(self, f):
            '''KConfig.OpenFlags KConfig.OpenFlags.__or__(KConfig.OpenFlags f)'''
            return KConfig.OpenFlags()
        def __or__(self, f):
            '''KConfig.OpenFlags KConfig.OpenFlags.__or__(int f)'''
            return KConfig.OpenFlags()
        def __int__(self):
            '''int KConfig.OpenFlags.__int__()'''
            return int()
        def __ixor__(self, f):
            '''KConfig.OpenFlags KConfig.OpenFlags.__ixor__(KConfig.OpenFlags f)'''
            return KConfig.OpenFlags()
        def __ior__(self, f):
            '''KConfig.OpenFlags KConfig.OpenFlags.__ior__(KConfig.OpenFlags f)'''
            return KConfig.OpenFlags()
        def __iand__(self, mask):
            '''KConfig.OpenFlags KConfig.OpenFlags.__iand__(int mask)'''
            return KConfig.OpenFlags()


class KConfigGroup(KConfigBase):
    """"""
    def __init__(self):
        '''void KConfigGroup.__init__()'''
    def __init__(self, master, group):
        '''void KConfigGroup.__init__(KConfigBase master, QString group)'''
    def __init__(self, master, group):
        '''void KConfigGroup.__init__(KConfigBase master, str group)'''
    def __init__(self, master, group):
        '''void KConfigGroup.__init__(KSharedConfigPtr master, QString group)'''
    def __init__(self, master, group):
        '''void KConfigGroup.__init__(KSharedConfigPtr master, str group)'''
    def __init__(self):
        '''KConfigGroup KConfigGroup.__init__()'''
        return KConfigGroup()
    def isGroupImmutableImpl(self, aGroup):
        '''bool KConfigGroup.isGroupImmutableImpl(QByteArray aGroup)'''
        return bool()
    def deleteGroupImpl(self, group, flags):
        '''void KConfigGroup.deleteGroupImpl(QByteArray group, KConfigBase.WriteConfigFlags flags)'''
    def groupImpl(self, b):
        '''KConfigGroup KConfigGroup.groupImpl(QByteArray b)'''
        return KConfigGroup()
    def hasGroupImpl(self, group):
        '''bool KConfigGroup.hasGroupImpl(QByteArray group)'''
        return bool()
    def entryMap(self):
        '''dict-of-QString-QString KConfigGroup.entryMap()'''
        return dict-of-QString-QString()
    def hasDefault(self, key):
        '''bool KConfigGroup.hasDefault(QString key)'''
        return bool()
    def hasDefault(self, key):
        '''bool KConfigGroup.hasDefault(str key)'''
        return bool()
    def revertToDefault(self, key):
        '''void KConfigGroup.revertToDefault(QString key)'''
    def revertToDefault(self, key):
        '''void KConfigGroup.revertToDefault(str key)'''
    def isEntryImmutable(self, key):
        '''bool KConfigGroup.isEntryImmutable(QString key)'''
        return bool()
    def isEntryImmutable(self, key):
        '''bool KConfigGroup.isEntryImmutable(str key)'''
        return bool()
    def isImmutable(self):
        '''bool KConfigGroup.isImmutable()'''
        return bool()
    def hasKey(self, key):
        '''bool KConfigGroup.hasKey(QString key)'''
        return bool()
    def hasKey(self, key):
        '''bool KConfigGroup.hasKey(str key)'''
        return bool()
    def deleteEntry(self, pKey, pFlags = None):
        '''void KConfigGroup.deleteEntry(QString pKey, KConfigBase.WriteConfigFlags pFlags = KConfigBase.Normal)'''
    def deleteEntry(self, pKey, pFlags = None):
        '''void KConfigGroup.deleteEntry(str pKey, KConfigBase.WriteConfigFlags pFlags = KConfigBase.Normal)'''
    def writePathEntry(self, pKey, path, pFlags = None):
        '''void KConfigGroup.writePathEntry(QString pKey, QString path, KConfigBase.WriteConfigFlags pFlags = KConfigBase.Normal)'''
    def writePathEntry(self, pKey, path, pFlags = None):
        '''void KConfigGroup.writePathEntry(str pKey, QString path, KConfigBase.WriteConfigFlags pFlags = KConfigBase.Normal)'''
    def writePathEntry(self, pKey, value, pFlags = None):
        '''void KConfigGroup.writePathEntry(QString pKey, QStringList value, KConfigBase.WriteConfigFlags pFlags = KConfigBase.Normal)'''
    def writePathEntry(self, pKey, value, pFlags = None):
        '''void KConfigGroup.writePathEntry(str pKey, QStringList value, KConfigBase.WriteConfigFlags pFlags = KConfigBase.Normal)'''
    def writeXdgListEntry(self, pKey, value, pFlags = None):
        '''void KConfigGroup.writeXdgListEntry(QString pKey, QStringList value, KConfigBase.WriteConfigFlags pFlags = KConfigBase.Normal)'''
    def writeXdgListEntry(self, pKey, value, pFlags = None):
        '''void KConfigGroup.writeXdgListEntry(str pKey, QStringList value, KConfigBase.WriteConfigFlags pFlags = KConfigBase.Normal)'''
    def writeEntry(self, key, value, pFlags = None):
        '''void KConfigGroup.writeEntry(QString key, QVariant value, KConfigBase.WriteConfigFlags pFlags = KConfigBase.Normal)'''
    def writeEntry(self, key, value, pFlags = None):
        '''void KConfigGroup.writeEntry(str key, QVariant value, KConfigBase.WriteConfigFlags pFlags = KConfigBase.Normal)'''
    def writeEntry(self, key, value, pFlags = None):
        '''void KConfigGroup.writeEntry(QString key, QString value, KConfigBase.WriteConfigFlags pFlags = KConfigBase.Normal)'''
    def writeEntry(self, key, value, pFlags = None):
        '''void KConfigGroup.writeEntry(str key, QString value, KConfigBase.WriteConfigFlags pFlags = KConfigBase.Normal)'''
    def writeEntry(self, key, value, pFlags = None):
        '''void KConfigGroup.writeEntry(QString key, QByteArray value, KConfigBase.WriteConfigFlags pFlags = KConfigBase.Normal)'''
    def writeEntry(self, key, value, pFlags = None):
        '''void KConfigGroup.writeEntry(str key, QByteArray value, KConfigBase.WriteConfigFlags pFlags = KConfigBase.Normal)'''
    def writeEntry(self, key, value, pFlags = None):
        '''void KConfigGroup.writeEntry(QString key, str value, KConfigBase.WriteConfigFlags pFlags = KConfigBase.Normal)'''
    def writeEntry(self, key, value, pFlags = None):
        '''void KConfigGroup.writeEntry(str key, str value, KConfigBase.WriteConfigFlags pFlags = KConfigBase.Normal)'''
    def writeEntry(self, key, value, pFlags = None):
        '''void KConfigGroup.writeEntry(QString key, QStringList value, KConfigBase.WriteConfigFlags pFlags = KConfigBase.Normal)'''
    def writeEntry(self, key, value, pFlags = None):
        '''void KConfigGroup.writeEntry(str key, QStringList value, KConfigBase.WriteConfigFlags pFlags = KConfigBase.Normal)'''
    def writeEntry(self, key, value, pFlags = None):
        '''void KConfigGroup.writeEntry(QString key, list-of-QVariant value, KConfigBase.WriteConfigFlags pFlags = KConfigBase.Normal)'''
    def writeEntry(self, key, value, pFlags = None):
        '''void KConfigGroup.writeEntry(str key, list-of-QVariant value, KConfigBase.WriteConfigFlags pFlags = KConfigBase.Normal)'''
    def readEntryUntranslated(self, pKey, aDefault = QString()):
        '''QString KConfigGroup.readEntryUntranslated(QString pKey, QString aDefault = QString())'''
        return QString()
    def readEntryUntranslated(self, key, aDefault = QString()):
        '''QString KConfigGroup.readEntryUntranslated(str key, QString aDefault = QString())'''
        return QString()
    def readPathEntry(self, pKey, aDefault):
        '''QString KConfigGroup.readPathEntry(QString pKey, QString aDefault)'''
        return QString()
    def readPathEntry(self, key, aDefault):
        '''QString KConfigGroup.readPathEntry(str key, QString aDefault)'''
        return QString()
    def readPathEntry(self, pKey, aDefault):
        '''QStringList KConfigGroup.readPathEntry(QString pKey, QStringList aDefault)'''
        return QStringList()
    def readPathEntry(self, key, aDefault):
        '''QStringList KConfigGroup.readPathEntry(str key, QStringList aDefault)'''
        return QStringList()
    def readXdgListEntry(self, pKey, aDefault = QStringList()):
        '''QStringList KConfigGroup.readXdgListEntry(QString pKey, QStringList aDefault = QStringList())'''
        return QStringList()
    def readXdgListEntry(self, pKey, aDefault = QStringList()):
        '''QStringList KConfigGroup.readXdgListEntry(str pKey, QStringList aDefault = QStringList())'''
        return QStringList()
    def readEntry(self, key, aDefault):
        '''QVariant KConfigGroup.readEntry(QString key, QVariant aDefault)'''
        return QVariant()
    def readEntry(self, key, aDefault):
        '''QVariant KConfigGroup.readEntry(str key, QVariant aDefault)'''
        return QVariant()
    def readEntry(self, key, aDefault):
        '''QString KConfigGroup.readEntry(QString key, QString aDefault)'''
        return QString()
    def readEntry(self, key, aDefault):
        '''QString KConfigGroup.readEntry(str key, QString aDefault)'''
        return QString()
    def readEntry(self, key, aDefault = None):
        '''QString KConfigGroup.readEntry(QString key, str aDefault = None)'''
        return QString()
    def readEntry(self, key, aDefault = None):
        '''QString KConfigGroup.readEntry(str key, str aDefault = None)'''
        return QString()
    def readEntry(self, key, aDefault):
        '''list-of-QVariant KConfigGroup.readEntry(QString key, list-of-QVariant aDefault)'''
        return [QVariant()]
    def readEntry(self, key, aDefault):
        '''list-of-QVariant KConfigGroup.readEntry(str key, list-of-QVariant aDefault)'''
        return [QVariant()]
    def readEntry(self, key, aDefault):
        '''QStringList KConfigGroup.readEntry(QString key, QStringList aDefault)'''
        return QStringList()
    def readEntry(self, key, aDefault):
        '''QStringList KConfigGroup.readEntry(str key, QStringList aDefault)'''
        return QStringList()
    def deleteGroup(self, pFlags = None):
        '''void KConfigGroup.deleteGroup(KConfigBase.WriteConfigFlags pFlags = KConfigBase.Normal)'''
    def keyList(self):
        '''QStringList KConfigGroup.keyList()'''
        return QStringList()
    def groupList(self):
        '''QStringList KConfigGroup.groupList()'''
        return QStringList()
    def parent(self):
        '''KConfigGroup KConfigGroup.parent()'''
        return KConfigGroup()
    def reparent(self, parent, pFlags = None):
        '''void KConfigGroup.reparent(KConfigBase parent, KConfigBase.WriteConfigFlags pFlags = KConfigBase.Normal)'''
    def copyTo(self, other, pFlags = None):
        '''void KConfigGroup.copyTo(KConfigBase other, KConfigBase.WriteConfigFlags pFlags = KConfigBase.Normal)'''
    def changeGroup(self, group):
        '''void KConfigGroup.changeGroup(QString group)'''
    def changeGroup(self, group):
        '''void KConfigGroup.changeGroup(str group)'''
    def config(self):
        '''KConfig KConfigGroup.config()'''
        return KConfig()
    def accessMode(self):
        '''KConfigBase.AccessMode KConfigGroup.accessMode()'''
        return KConfigBase.AccessMode()
    def markAsClean(self):
        '''void KConfigGroup.markAsClean()'''
    def sync(self):
        '''void KConfigGroup.sync()'''
    def exists(self):
        '''bool KConfigGroup.exists()'''
        return bool()
    def name(self):
        '''QString KConfigGroup.name()'''
        return QString()
    def isValid(self):
        '''bool KConfigGroup.isValid()'''
        return bool()


class KConfigSkeletonItem():
    """"""
    def __init__(self, _group, _key):
        '''void KConfigSkeletonItem.__init__(QString _group, QString _key)'''
    def readImmutability(self, group):
        '''void KConfigSkeletonItem.readImmutability(KConfigGroup group)'''
    def isImmutable(self):
        '''bool KConfigSkeletonItem.isImmutable()'''
        return bool()
    def swapDefault(self):
        '''abstract void KConfigSkeletonItem.swapDefault()'''
    def setDefault(self):
        '''abstract void KConfigSkeletonItem.setDefault()'''
    def maxValue(self):
        '''QVariant KConfigSkeletonItem.maxValue()'''
        return QVariant()
    def minValue(self):
        '''QVariant KConfigSkeletonItem.minValue()'''
        return QVariant()
    def property(self):
        '''abstract QVariant KConfigSkeletonItem.property()'''
        return QVariant()
    def isEqual(self, p):
        '''abstract bool KConfigSkeletonItem.isEqual(QVariant p)'''
        return bool()
    def setProperty(self, p):
        '''abstract void KConfigSkeletonItem.setProperty(QVariant p)'''
    def readDefault(self):
        '''abstract KConfig KConfigSkeletonItem.readDefault()'''
        return KConfig()
    def writeConfig(self):
        '''abstract KConfig KConfigSkeletonItem.writeConfig()'''
        return KConfig()
    def readConfig(self):
        '''abstract KConfig KConfigSkeletonItem.readConfig()'''
        return KConfig()
    def whatsThis(self):
        '''QString KConfigSkeletonItem.whatsThis()'''
        return QString()
    def setWhatsThis(self, w):
        '''void KConfigSkeletonItem.setWhatsThis(QString w)'''
    def toolTip(self):
        '''QString KConfigSkeletonItem.toolTip()'''
        return QString()
    def setToolTip(self, t):
        '''void KConfigSkeletonItem.setToolTip(QString t)'''
    def label(self):
        '''QString KConfigSkeletonItem.label()'''
        return QString()
    def setLabel(self, l):
        '''void KConfigSkeletonItem.setLabel(QString l)'''
    def name(self):
        '''QString KConfigSkeletonItem.name()'''
        return QString()
    def setName(self, _name):
        '''void KConfigSkeletonItem.setName(QString _name)'''
    def key(self):
        '''QString KConfigSkeletonItem.key()'''
        return QString()
    def setKey(self, _key):
        '''void KConfigSkeletonItem.setKey(QString _key)'''
    def group(self):
        '''QString KConfigSkeletonItem.group()'''
        return QString()
    def setGroup(self, _group):
        '''void KConfigSkeletonItem.setGroup(QString _group)'''


class KCoreConfigSkeleton(QObject):
    """"""
    def __init__(self, configname = QString(), parent = None):
        '''void KCoreConfigSkeleton.__init__(QString configname = QString(), QObject parent = None)'''
    def __init__(self, config, parent = None):
        '''void KCoreConfigSkeleton.__init__(unknown-type config, QObject parent = None)'''
    def findItem(self, name):
        '''KConfigSkeletonItem KCoreConfigSkeleton.findItem(QString name)'''
        return KConfigSkeletonItem()
    def isImmutable(self, name):
        '''bool KCoreConfigSkeleton.isImmutable(QString name)'''
        return bool()
    def usrWriteConfig(self):
        '''void KCoreConfigSkeleton.usrWriteConfig()'''
    def usrReadConfig(self):
        '''void KCoreConfigSkeleton.usrReadConfig()'''
    def usrSetDefaults(self):
        '''void KCoreConfigSkeleton.usrSetDefaults()'''
    def usrUseDefaults(self, b):
        '''bool KCoreConfigSkeleton.usrUseDefaults(bool b)'''
        return bool()
    configChanged = pyqtSignal() # void configChanged() - signal
    def useDefaults(self, b):
        '''bool KCoreConfigSkeleton.useDefaults(bool b)'''
        return bool()
    def items(self):
        '''list-of-KConfigSkeletonItem KCoreConfigSkeleton.items()'''
        return [KConfigSkeletonItem()]
    def setSharedConfig(self, pConfig):
        '''void KCoreConfigSkeleton.setSharedConfig(unknown-type pConfig)'''
    def config(self):
        '''KConfig KCoreConfigSkeleton.config()'''
        return KConfig()
    def addItemIntList(self, name, reference, defaultValue = None, key = QString()):
        '''KCoreConfigSkeleton.ItemIntList KCoreConfigSkeleton.addItemIntList(QString name, list-of-int reference, list-of-int defaultValue = QListlt;intgt;(), QString key = QString())'''
        return KCoreConfigSkeleton.ItemIntList()
    def addItemStringList(self, name, reference, defaultValue = QStringList(), key = QString()):
        '''KCoreConfigSkeleton.ItemStringList KCoreConfigSkeleton.addItemStringList(QString name, QStringList reference, QStringList defaultValue = QStringList(), QString key = QString())'''
        return KCoreConfigSkeleton.ItemStringList()
    def addItemDateTime(self, name, reference, defaultValue = QDateTime(), key = QString()):
        '''KCoreConfigSkeleton.ItemDateTime KCoreConfigSkeleton.addItemDateTime(QString name, QDateTime reference, QDateTime defaultValue = QDateTime(), QString key = QString())'''
        return KCoreConfigSkeleton.ItemDateTime()
    def addItemSize(self, name, reference, defaultValue = QSize(), key = QString()):
        '''KCoreConfigSkeleton.ItemSize KCoreConfigSkeleton.addItemSize(QString name, QSize reference, QSize defaultValue = QSize(), QString key = QString())'''
        return KCoreConfigSkeleton.ItemSize()
    def addItemPoint(self, name, reference, defaultValue = QPoint(), key = QString()):
        '''KCoreConfigSkeleton.ItemPoint KCoreConfigSkeleton.addItemPoint(QString name, QPoint reference, QPoint defaultValue = QPoint(), QString key = QString())'''
        return KCoreConfigSkeleton.ItemPoint()
    def addItemRect(self, name, reference, defaultValue = QRect(), key = QString()):
        '''KCoreConfigSkeleton.ItemRect KCoreConfigSkeleton.addItemRect(QString name, QRect reference, QRect defaultValue = QRect(), QString key = QString())'''
        return KCoreConfigSkeleton.ItemRect()
    def addItemDouble(self, name, reference, defaultValue = 0, key = QString()):
        '''KCoreConfigSkeleton.ItemDouble KCoreConfigSkeleton.addItemDouble(QString name, float reference, float defaultValue = 0, QString key = QString())'''
        return KCoreConfigSkeleton.ItemDouble()
    def addItemUInt64(self, name, reference, defaultValue = 0, key = QString()):
        '''KCoreConfigSkeleton.ItemULongLong KCoreConfigSkeleton.addItemUInt64(QString name, int reference, int defaultValue = 0, QString key = QString())'''
        return KCoreConfigSkeleton.ItemULongLong()
    def addItemULongLong(self, name, reference, defaultValue = 0, key = QString()):
        '''KCoreConfigSkeleton.ItemULongLong KCoreConfigSkeleton.addItemULongLong(QString name, int reference, int defaultValue = 0, QString key = QString())'''
        return KCoreConfigSkeleton.ItemULongLong()
    def addItemInt64(self, name, reference, defaultValue = 0, key = QString()):
        '''KCoreConfigSkeleton.ItemLongLong KCoreConfigSkeleton.addItemInt64(QString name, int reference, int defaultValue = 0, QString key = QString())'''
        return KCoreConfigSkeleton.ItemLongLong()
    def addItemLongLong(self, name, reference, defaultValue = 0, key = QString()):
        '''KCoreConfigSkeleton.ItemLongLong KCoreConfigSkeleton.addItemLongLong(QString name, int reference, int defaultValue = 0, QString key = QString())'''
        return KCoreConfigSkeleton.ItemLongLong()
    def addItemUInt(self, name, reference, defaultValue = 0, key = QString()):
        '''KCoreConfigSkeleton.ItemUInt KCoreConfigSkeleton.addItemUInt(QString name, int reference, int defaultValue = 0, QString key = QString())'''
        return KCoreConfigSkeleton.ItemUInt()
    def addItemInt(self, name, reference, defaultValue = 0, key = QString()):
        '''KCoreConfigSkeleton.ItemInt KCoreConfigSkeleton.addItemInt(QString name, int reference, int defaultValue = 0, QString key = QString())'''
        return KCoreConfigSkeleton.ItemInt()
    def addItemBool(self, name, reference, defaultValue = False, key = QString()):
        '''KCoreConfigSkeleton.ItemBool KCoreConfigSkeleton.addItemBool(QString name, bool reference, bool defaultValue = False, QString key = QString())'''
        return KCoreConfigSkeleton.ItemBool()
    def addItemProperty(self, name, reference, defaultValue = QVariant(), key = QString()):
        '''KCoreConfigSkeleton.ItemProperty KCoreConfigSkeleton.addItemProperty(QString name, QVariant reference, QVariant defaultValue = QVariant(), QString key = QString())'''
        return KCoreConfigSkeleton.ItemProperty()
    def addItemPath(self, name, reference, defaultValue = QLatin1String, key = QString()):
        '''KCoreConfigSkeleton.ItemPath KCoreConfigSkeleton.addItemPath(QString name, QString reference, QString defaultValue = QLatin1String, QString key = QString())'''
        return KCoreConfigSkeleton.ItemPath()
    def addItemPassword(self, name, reference, defaultValue = QLatin1String, key = QString()):
        '''KCoreConfigSkeleton.ItemPassword KCoreConfigSkeleton.addItemPassword(QString name, QString reference, QString defaultValue = QLatin1String, QString key = QString())'''
        return KCoreConfigSkeleton.ItemPassword()
    def addItemString(self, name, reference, defaultValue = QLatin1String, key = QString()):
        '''KCoreConfigSkeleton.ItemString KCoreConfigSkeleton.addItemString(QString name, QString reference, QString defaultValue = QLatin1String, QString key = QString())'''
        return KCoreConfigSkeleton.ItemString()
    def addItem(self, name = QString()):
        '''KConfigSkeletonItem KCoreConfigSkeleton.addItem(QString name = QString())'''
        return KConfigSkeletonItem()
    def currentGroup(self):
        '''QString KCoreConfigSkeleton.currentGroup()'''
        return QString()
    def setCurrentGroup(self, group):
        '''void KCoreConfigSkeleton.setCurrentGroup(QString group)'''
    def writeConfig(self):
        '''void KCoreConfigSkeleton.writeConfig()'''
    def readConfig(self):
        '''void KCoreConfigSkeleton.readConfig()'''
    def setDefaults(self):
        '''void KCoreConfigSkeleton.setDefaults()'''
    class ItemEnum():
        """"""
        class Choice2():
            """"""
            label = None # QString - member
            name = None # QString - member
            toolTip = None # QString - member
            whatsThis = None # QString - member
            def __init__(self):
                '''void KCoreConfigSkeleton.ItemEnum.Choice2.__init__()'''
            def __init__(self):
                '''KCoreConfigSkeleton.ItemEnum.Choice2 KCoreConfigSkeleton.ItemEnum.Choice2.__init__()'''
                return KCoreConfigSkeleton.ItemEnum.Choice2()
    class ItemUrlList(KConfigSkeletonItem):
        """"""
        def __init__(self, _group, _key, reference, defaultValue = None):
            '''void KCoreConfigSkeleton.ItemUrlList.__init__(QString _group, QString _key, KUrl.List reference, KUrl.List defaultValue = KUrl.List())'''
        def swapDefault(self):
            '''void KCoreConfigSkeleton.ItemUrlList.swapDefault()'''
        def readDefault(self, config):
            '''void KCoreConfigSkeleton.ItemUrlList.readDefault(KConfig config)'''
        def setDefault(self):
            '''void KCoreConfigSkeleton.ItemUrlList.setDefault()'''
        def setDefaultValue(self, v):
            '''void KCoreConfigSkeleton.ItemUrlList.setDefaultValue(KUrl.List v)'''
        def value(self):
            '''KUrl.List KCoreConfigSkeleton.ItemUrlList.value()'''
            return KUrl.List()
        def setValue(self, v):
            '''void KCoreConfigSkeleton.ItemUrlList.setValue(KUrl.List v)'''
        def property(self):
            '''QVariant KCoreConfigSkeleton.ItemUrlList.property()'''
            return QVariant()
        def isEqual(self, p):
            '''bool KCoreConfigSkeleton.ItemUrlList.isEqual(QVariant p)'''
            return bool()
        def setProperty(self, p):
            '''void KCoreConfigSkeleton.ItemUrlList.setProperty(QVariant p)'''
        def writeConfig(self, config):
            '''void KCoreConfigSkeleton.ItemUrlList.writeConfig(KConfig config)'''
        def readConfig(self, config):
            '''void KCoreConfigSkeleton.ItemUrlList.readConfig(KConfig config)'''
    class ItemUInt(KConfigSkeletonItem):
        """"""
        def __init__(self, _group, _key, reference, defaultValue = 0):
            '''void KCoreConfigSkeleton.ItemUInt.__init__(QString _group, QString _key, int reference, int defaultValue = 0)'''
        def swapDefault(self):
            '''void KCoreConfigSkeleton.ItemUInt.swapDefault()'''
        def readDefault(self, config):
            '''void KCoreConfigSkeleton.ItemUInt.readDefault(KConfig config)'''
        def writeConfig(self, config):
            '''void KCoreConfigSkeleton.ItemUInt.writeConfig(KConfig config)'''
        def setDefault(self):
            '''void KCoreConfigSkeleton.ItemUInt.setDefault()'''
        def setDefaultValue(self, v):
            '''void KCoreConfigSkeleton.ItemUInt.setDefaultValue(int v)'''
        def value(self):
            '''int KCoreConfigSkeleton.ItemUInt.value()'''
            return int()
        def setValue(self, v):
            '''void KCoreConfigSkeleton.ItemUInt.setValue(int v)'''
        def setMaxValue(self):
            '''int KCoreConfigSkeleton.ItemUInt.setMaxValue()'''
            return int()
        def setMinValue(self):
            '''int KCoreConfigSkeleton.ItemUInt.setMinValue()'''
            return int()
        def maxValue(self):
            '''QVariant KCoreConfigSkeleton.ItemUInt.maxValue()'''
            return QVariant()
        def minValue(self):
            '''QVariant KCoreConfigSkeleton.ItemUInt.minValue()'''
            return QVariant()
        def property(self):
            '''QVariant KCoreConfigSkeleton.ItemUInt.property()'''
            return QVariant()
        def isEqual(self, p):
            '''bool KCoreConfigSkeleton.ItemUInt.isEqual(QVariant p)'''
            return bool()
        def setProperty(self, p):
            '''void KCoreConfigSkeleton.ItemUInt.setProperty(QVariant p)'''
        def readConfig(self, config):
            '''void KCoreConfigSkeleton.ItemUInt.readConfig(KConfig config)'''
    class ItemIntList(KConfigSkeletonItem):
        """"""
        def __init__(self, _group, _key, reference, defaultValue = None):
            '''void KCoreConfigSkeleton.ItemIntList.__init__(QString _group, QString _key, list-of-int reference, list-of-int defaultValue = QListlt;intgt;())'''
        def swapDefault(self):
            '''void KCoreConfigSkeleton.ItemIntList.swapDefault()'''
        def readDefault(self, config):
            '''void KCoreConfigSkeleton.ItemIntList.readDefault(KConfig config)'''
        def writeConfig(self, config):
            '''void KCoreConfigSkeleton.ItemIntList.writeConfig(KConfig config)'''
        def setDefault(self):
            '''void KCoreConfigSkeleton.ItemIntList.setDefault()'''
        def setDefaultValue(self, v):
            '''void KCoreConfigSkeleton.ItemIntList.setDefaultValue(list-of-int v)'''
        def value(self):
            '''list-of-int KCoreConfigSkeleton.ItemIntList.value()'''
            return [int()]
        def setValue(self, v):
            '''void KCoreConfigSkeleton.ItemIntList.setValue(list-of-int v)'''
        def property(self):
            '''QVariant KCoreConfigSkeleton.ItemIntList.property()'''
            return QVariant()
        def isEqual(self, p):
            '''bool KCoreConfigSkeleton.ItemIntList.isEqual(QVariant p)'''
            return bool()
        def setProperty(self, p):
            '''void KCoreConfigSkeleton.ItemIntList.setProperty(QVariant p)'''
        def readConfig(self, config):
            '''void KCoreConfigSkeleton.ItemIntList.readConfig(KConfig config)'''
    class ItemEnum(KCoreConfigSkeleton.ItemInt):
        """"""
        def __init__(self, _group, _key, reference, choices, defaultValue = 0):
            '''void KCoreConfigSkeleton.ItemEnum.__init__(QString _group, QString _key, int reference, list-of-KCoreConfigSkeleton.ItemEnum.Choice choices, int defaultValue = 0)'''
        def swapDefault(self):
            '''void KCoreConfigSkeleton.ItemEnum.swapDefault()'''
        def readDefault(self, config):
            '''void KCoreConfigSkeleton.ItemEnum.readDefault(KConfig config)'''
        def setDefault(self):
            '''void KCoreConfigSkeleton.ItemEnum.setDefault()'''
        def setDefaultValue(self, v):
            '''void KCoreConfigSkeleton.ItemEnum.setDefaultValue(int v)'''
        def value(self):
            '''int KCoreConfigSkeleton.ItemEnum.value()'''
            return int()
        def setValue(self, v):
            '''void KCoreConfigSkeleton.ItemEnum.setValue(int v)'''
        def writeConfig(self, config):
            '''void KCoreConfigSkeleton.ItemEnum.writeConfig(KConfig config)'''
        def readConfig(self, config):
            '''void KCoreConfigSkeleton.ItemEnum.readConfig(KConfig config)'''
        def choices2(self):
            '''list-of-KCoreConfigSkeleton.ItemEnum.Choice2 KCoreConfigSkeleton.ItemEnum.choices2()'''
            return [KCoreConfigSkeleton.ItemEnum.Choice2()]
        def choices(self):
            '''list-of-KCoreConfigSkeleton.ItemEnum.Choice KCoreConfigSkeleton.ItemEnum.choices()'''
            return [KCoreConfigSkeleton.ItemEnum.Choice()]
    class ItemBool(KConfigSkeletonItem):
        """"""
        def __init__(self, _group, _key, reference, defaultValue = True):
            '''void KCoreConfigSkeleton.ItemBool.__init__(QString _group, QString _key, bool reference, bool defaultValue = True)'''
        def swapDefault(self):
            '''void KCoreConfigSkeleton.ItemBool.swapDefault()'''
        def readDefault(self, config):
            '''void KCoreConfigSkeleton.ItemBool.readDefault(KConfig config)'''
        def writeConfig(self, config):
            '''void KCoreConfigSkeleton.ItemBool.writeConfig(KConfig config)'''
        def setDefault(self):
            '''void KCoreConfigSkeleton.ItemBool.setDefault()'''
        def setDefaultValue(self, v):
            '''void KCoreConfigSkeleton.ItemBool.setDefaultValue(bool v)'''
        def value(self):
            '''bool KCoreConfigSkeleton.ItemBool.value()'''
            return bool()
        def setValue(self, v):
            '''void KCoreConfigSkeleton.ItemBool.setValue(bool v)'''
        def property(self):
            '''QVariant KCoreConfigSkeleton.ItemBool.property()'''
            return QVariant()
        def isEqual(self, p):
            '''bool KCoreConfigSkeleton.ItemBool.isEqual(QVariant p)'''
            return bool()
        def setProperty(self, p):
            '''void KCoreConfigSkeleton.ItemBool.setProperty(QVariant p)'''
        def readConfig(self, config):
            '''void KCoreConfigSkeleton.ItemBool.readConfig(KConfig config)'''
    class ItemEnum():
        """"""
        class Choice():
            """"""
            label = None # QString - member
            name = None # QString - member
            whatsThis = None # QString - member
            def __init__(self):
                '''void KCoreConfigSkeleton.ItemEnum.Choice.__init__()'''
            def __init__(self):
                '''KCoreConfigSkeleton.ItemEnum.Choice KCoreConfigSkeleton.ItemEnum.Choice.__init__()'''
                return KCoreConfigSkeleton.ItemEnum.Choice()
    class ItemStringList(KConfigSkeletonItem):
        """"""
        def __init__(self, _group, _key, reference, defaultValue = QStringList()):
            '''void KCoreConfigSkeleton.ItemStringList.__init__(QString _group, QString _key, QStringList reference, QStringList defaultValue = QStringList())'''
        def swapDefault(self):
            '''void KCoreConfigSkeleton.ItemStringList.swapDefault()'''
        def readDefault(self, config):
            '''void KCoreConfigSkeleton.ItemStringList.readDefault(KConfig config)'''
        def writeConfig(self, config):
            '''void KCoreConfigSkeleton.ItemStringList.writeConfig(KConfig config)'''
        def setDefault(self):
            '''void KCoreConfigSkeleton.ItemStringList.setDefault()'''
        def setDefaultValue(self, v):
            '''void KCoreConfigSkeleton.ItemStringList.setDefaultValue(QStringList v)'''
        def value(self):
            '''QStringList KCoreConfigSkeleton.ItemStringList.value()'''
            return QStringList()
        def setValue(self, v):
            '''void KCoreConfigSkeleton.ItemStringList.setValue(QStringList v)'''
        def property(self):
            '''QVariant KCoreConfigSkeleton.ItemStringList.property()'''
            return QVariant()
        def isEqual(self, p):
            '''bool KCoreConfigSkeleton.ItemStringList.isEqual(QVariant p)'''
            return bool()
        def setProperty(self, p):
            '''void KCoreConfigSkeleton.ItemStringList.setProperty(QVariant p)'''
        def readConfig(self, config):
            '''void KCoreConfigSkeleton.ItemStringList.readConfig(KConfig config)'''
    class ItemRect(KConfigSkeletonItem):
        """"""
        def __init__(self, _group, _key, reference, defaultValue = QRect()):
            '''void KCoreConfigSkeleton.ItemRect.__init__(QString _group, QString _key, QRect reference, QRect defaultValue = QRect())'''
        def swapDefault(self):
            '''void KCoreConfigSkeleton.ItemRect.swapDefault()'''
        def readDefault(self, config):
            '''void KCoreConfigSkeleton.ItemRect.readDefault(KConfig config)'''
        def writeConfig(self, config):
            '''void KCoreConfigSkeleton.ItemRect.writeConfig(KConfig config)'''
        def setDefault(self):
            '''void KCoreConfigSkeleton.ItemRect.setDefault()'''
        def setDefaultValue(self, v):
            '''void KCoreConfigSkeleton.ItemRect.setDefaultValue(QRect v)'''
        def value(self):
            '''QRect KCoreConfigSkeleton.ItemRect.value()'''
            return QRect()
        def setValue(self, v):
            '''void KCoreConfigSkeleton.ItemRect.setValue(QRect v)'''
        def property(self):
            '''QVariant KCoreConfigSkeleton.ItemRect.property()'''
            return QVariant()
        def isEqual(self, p):
            '''bool KCoreConfigSkeleton.ItemRect.isEqual(QVariant p)'''
            return bool()
        def setProperty(self, p):
            '''void KCoreConfigSkeleton.ItemRect.setProperty(QVariant p)'''
        def readConfig(self, config):
            '''void KCoreConfigSkeleton.ItemRect.readConfig(KConfig config)'''
    class ItemUrl(KConfigSkeletonItem):
        """"""
        def __init__(self, _group, _key, reference, defaultValue = KUrl()):
            '''void KCoreConfigSkeleton.ItemUrl.__init__(QString _group, QString _key, KUrl reference, KUrl defaultValue = KUrl())'''
        def swapDefault(self):
            '''void KCoreConfigSkeleton.ItemUrl.swapDefault()'''
        def readDefault(self, config):
            '''void KCoreConfigSkeleton.ItemUrl.readDefault(KConfig config)'''
        def setDefault(self):
            '''void KCoreConfigSkeleton.ItemUrl.setDefault()'''
        def setDefaultValue(self, v):
            '''void KCoreConfigSkeleton.ItemUrl.setDefaultValue(KUrl v)'''
        def value(self):
            '''KUrl KCoreConfigSkeleton.ItemUrl.value()'''
            return KUrl()
        def setValue(self, v):
            '''void KCoreConfigSkeleton.ItemUrl.setValue(KUrl v)'''
        def property(self):
            '''QVariant KCoreConfigSkeleton.ItemUrl.property()'''
            return QVariant()
        def isEqual(self, p):
            '''bool KCoreConfigSkeleton.ItemUrl.isEqual(QVariant p)'''
            return bool()
        def setProperty(self, p):
            '''void KCoreConfigSkeleton.ItemUrl.setProperty(QVariant p)'''
        def readConfig(self, config):
            '''void KCoreConfigSkeleton.ItemUrl.readConfig(KConfig config)'''
        def writeConfig(self, config):
            '''void KCoreConfigSkeleton.ItemUrl.writeConfig(KConfig config)'''
    class ItemDateTime(KConfigSkeletonItem):
        """"""
        def __init__(self, _group, _key, reference, defaultValue = QDateTime()):
            '''void KCoreConfigSkeleton.ItemDateTime.__init__(QString _group, QString _key, QDateTime reference, QDateTime defaultValue = QDateTime())'''
        def swapDefault(self):
            '''void KCoreConfigSkeleton.ItemDateTime.swapDefault()'''
        def readDefault(self, config):
            '''void KCoreConfigSkeleton.ItemDateTime.readDefault(KConfig config)'''
        def writeConfig(self, config):
            '''void KCoreConfigSkeleton.ItemDateTime.writeConfig(KConfig config)'''
        def setDefault(self):
            '''void KCoreConfigSkeleton.ItemDateTime.setDefault()'''
        def setDefaultValue(self, v):
            '''void KCoreConfigSkeleton.ItemDateTime.setDefaultValue(QDateTime v)'''
        def value(self):
            '''QDateTime KCoreConfigSkeleton.ItemDateTime.value()'''
            return QDateTime()
        def setValue(self, v):
            '''void KCoreConfigSkeleton.ItemDateTime.setValue(QDateTime v)'''
        def property(self):
            '''QVariant KCoreConfigSkeleton.ItemDateTime.property()'''
            return QVariant()
        def isEqual(self, p):
            '''bool KCoreConfigSkeleton.ItemDateTime.isEqual(QVariant p)'''
            return bool()
        def setProperty(self, p):
            '''void KCoreConfigSkeleton.ItemDateTime.setProperty(QVariant p)'''
        def readConfig(self, config):
            '''void KCoreConfigSkeleton.ItemDateTime.readConfig(KConfig config)'''
    class ItemLongLong(KConfigSkeletonItem):
        """"""
        def __init__(self, _group, _key, reference, defaultValue = 0):
            '''void KCoreConfigSkeleton.ItemLongLong.__init__(QString _group, QString _key, int reference, int defaultValue = 0)'''
        def swapDefault(self):
            '''void KCoreConfigSkeleton.ItemLongLong.swapDefault()'''
        def readDefault(self, config):
            '''void KCoreConfigSkeleton.ItemLongLong.readDefault(KConfig config)'''
        def writeConfig(self, config):
            '''void KCoreConfigSkeleton.ItemLongLong.writeConfig(KConfig config)'''
        def setDefault(self):
            '''void KCoreConfigSkeleton.ItemLongLong.setDefault()'''
        def setDefaultValue(self, v):
            '''void KCoreConfigSkeleton.ItemLongLong.setDefaultValue(int v)'''
        def value(self):
            '''int KCoreConfigSkeleton.ItemLongLong.value()'''
            return int()
        def setValue(self, v):
            '''void KCoreConfigSkeleton.ItemLongLong.setValue(int v)'''
        def setMaxValue(self):
            '''int KCoreConfigSkeleton.ItemLongLong.setMaxValue()'''
            return int()
        def setMinValue(self):
            '''int KCoreConfigSkeleton.ItemLongLong.setMinValue()'''
            return int()
        def maxValue(self):
            '''QVariant KCoreConfigSkeleton.ItemLongLong.maxValue()'''
            return QVariant()
        def minValue(self):
            '''QVariant KCoreConfigSkeleton.ItemLongLong.minValue()'''
            return QVariant()
        def property(self):
            '''QVariant KCoreConfigSkeleton.ItemLongLong.property()'''
            return QVariant()
        def isEqual(self, p):
            '''bool KCoreConfigSkeleton.ItemLongLong.isEqual(QVariant p)'''
            return bool()
        def setProperty(self, p):
            '''void KCoreConfigSkeleton.ItemLongLong.setProperty(QVariant p)'''
        def readConfig(self, config):
            '''void KCoreConfigSkeleton.ItemLongLong.readConfig(KConfig config)'''
    class ItemInt(KConfigSkeletonItem):
        """"""
        def __init__(self, _group, _key, reference, defaultValue = 0):
            '''void KCoreConfigSkeleton.ItemInt.__init__(QString _group, QString _key, int reference, int defaultValue = 0)'''
        def swapDefault(self):
            '''void KCoreConfigSkeleton.ItemInt.swapDefault()'''
        def readDefault(self, config):
            '''void KCoreConfigSkeleton.ItemInt.readDefault(KConfig config)'''
        def writeConfig(self, config):
            '''void KCoreConfigSkeleton.ItemInt.writeConfig(KConfig config)'''
        def setDefault(self):
            '''void KCoreConfigSkeleton.ItemInt.setDefault()'''
        def setDefaultValue(self, v):
            '''void KCoreConfigSkeleton.ItemInt.setDefaultValue(int v)'''
        def value(self):
            '''int KCoreConfigSkeleton.ItemInt.value()'''
            return int()
        def setValue(self, v):
            '''void KCoreConfigSkeleton.ItemInt.setValue(int v)'''
        def setMaxValue(self):
            '''int KCoreConfigSkeleton.ItemInt.setMaxValue()'''
            return int()
        def setMinValue(self):
            '''int KCoreConfigSkeleton.ItemInt.setMinValue()'''
            return int()
        def maxValue(self):
            '''QVariant KCoreConfigSkeleton.ItemInt.maxValue()'''
            return QVariant()
        def minValue(self):
            '''QVariant KCoreConfigSkeleton.ItemInt.minValue()'''
            return QVariant()
        def property(self):
            '''QVariant KCoreConfigSkeleton.ItemInt.property()'''
            return QVariant()
        def isEqual(self, p):
            '''bool KCoreConfigSkeleton.ItemInt.isEqual(QVariant p)'''
            return bool()
        def setProperty(self, p):
            '''void KCoreConfigSkeleton.ItemInt.setProperty(QVariant p)'''
        def readConfig(self, config):
            '''void KCoreConfigSkeleton.ItemInt.readConfig(KConfig config)'''
    class ItemProperty(KConfigSkeletonItem):
        """"""
        def __init__(self, _group, _key, reference, defaultValue = 0):
            '''void KCoreConfigSkeleton.ItemProperty.__init__(QString _group, QString _key, QVariant reference, QVariant defaultValue = 0)'''
        def swapDefault(self):
            '''void KCoreConfigSkeleton.ItemProperty.swapDefault()'''
        def readDefault(self, config):
            '''void KCoreConfigSkeleton.ItemProperty.readDefault(KConfig config)'''
        def writeConfig(self, config):
            '''void KCoreConfigSkeleton.ItemProperty.writeConfig(KConfig config)'''
        def setDefault(self):
            '''void KCoreConfigSkeleton.ItemProperty.setDefault()'''
        def setDefaultValue(self, v):
            '''void KCoreConfigSkeleton.ItemProperty.setDefaultValue(QVariant v)'''
        def value(self):
            '''QVariant KCoreConfigSkeleton.ItemProperty.value()'''
            return QVariant()
        def setValue(self, v):
            '''void KCoreConfigSkeleton.ItemProperty.setValue(QVariant v)'''
        def property(self):
            '''QVariant KCoreConfigSkeleton.ItemProperty.property()'''
            return QVariant()
        def isEqual(self, p):
            '''bool KCoreConfigSkeleton.ItemProperty.isEqual(QVariant p)'''
            return bool()
        def setProperty(self, p):
            '''void KCoreConfigSkeleton.ItemProperty.setProperty(QVariant p)'''
        def readConfig(self, config):
            '''void KCoreConfigSkeleton.ItemProperty.readConfig(KConfig config)'''
    class ItemPathList(KCoreConfigSkeleton.ItemStringList):
        """"""
        def __init__(self, _group, _key, reference, defaultValue = QStringList()):
            '''void KCoreConfigSkeleton.ItemPathList.__init__(QString _group, QString _key, QStringList reference, QStringList defaultValue = QStringList())'''
        def writeConfig(self, config):
            '''void KCoreConfigSkeleton.ItemPathList.writeConfig(KConfig config)'''
        def readConfig(self, config):
            '''void KCoreConfigSkeleton.ItemPathList.readConfig(KConfig config)'''
    class ItemPath(KCoreConfigSkeleton.ItemString):
        """"""
        def __init__(self, _group, _key, reference, defaultValue = QString()):
            '''void KCoreConfigSkeleton.ItemPath.__init__(QString _group, QString _key, QString reference, QString defaultValue = QString())'''
        def swapDefault(self):
            '''void KCoreConfigSkeleton.ItemPath.swapDefault()'''
        def readDefault(self, config):
            '''void KCoreConfigSkeleton.ItemPath.readDefault(KConfig config)'''
        def setDefault(self):
            '''void KCoreConfigSkeleton.ItemPath.setDefault()'''
        def setDefaultValue(self, v):
            '''void KCoreConfigSkeleton.ItemPath.setDefaultValue(QString v)'''
        def value(self):
            '''QString KCoreConfigSkeleton.ItemPath.value()'''
            return QString()
        def setValue(self, v):
            '''void KCoreConfigSkeleton.ItemPath.setValue(QString v)'''
    class ItemPassword(KCoreConfigSkeleton.ItemString):
        """"""
        def __init__(self, _group, _key, reference, defaultValue = QLatin1String):
            '''void KCoreConfigSkeleton.ItemPassword.__init__(QString _group, QString _key, QString reference, QString defaultValue = QLatin1String)'''
        def swapDefault(self):
            '''void KCoreConfigSkeleton.ItemPassword.swapDefault()'''
        def readDefault(self, config):
            '''void KCoreConfigSkeleton.ItemPassword.readDefault(KConfig config)'''
        def setDefault(self):
            '''void KCoreConfigSkeleton.ItemPassword.setDefault()'''
        def setDefaultValue(self, v):
            '''void KCoreConfigSkeleton.ItemPassword.setDefaultValue(QString v)'''
        def value(self):
            '''QString KCoreConfigSkeleton.ItemPassword.value()'''
            return QString()
        def setValue(self, v):
            '''void KCoreConfigSkeleton.ItemPassword.setValue(QString v)'''
    class ItemString(KConfigSkeletonItem):
        """"""
        # Enum KCoreConfigSkeleton.ItemString.Type
        Normal = 0
        Password = 0
        Path = 0
    
        def __init__(self, _group, _key, reference, defaultValue = QLatin1String, type = None):
            '''void KCoreConfigSkeleton.ItemString.__init__(QString _group, QString _key, QString reference, QString defaultValue = QLatin1String, KCoreConfigSkeleton.ItemString.Type type = KCoreConfigSkeleton.ItemString.Normal)'''
        def swapDefault(self):
            '''void KCoreConfigSkeleton.ItemString.swapDefault()'''
        def readDefault(self, config):
            '''void KCoreConfigSkeleton.ItemString.readDefault(KConfig config)'''
        def setDefault(self):
            '''void KCoreConfigSkeleton.ItemString.setDefault()'''
        def setDefaultValue(self, v):
            '''void KCoreConfigSkeleton.ItemString.setDefaultValue(QString v)'''
        def value(self):
            '''QString KCoreConfigSkeleton.ItemString.value()'''
            return QString()
        def setValue(self, v):
            '''void KCoreConfigSkeleton.ItemString.setValue(QString v)'''
        def property(self):
            '''QVariant KCoreConfigSkeleton.ItemString.property()'''
            return QVariant()
        def isEqual(self, p):
            '''bool KCoreConfigSkeleton.ItemString.isEqual(QVariant p)'''
            return bool()
        def setProperty(self, p):
            '''void KCoreConfigSkeleton.ItemString.setProperty(QVariant p)'''
        def readConfig(self, config):
            '''void KCoreConfigSkeleton.ItemString.readConfig(KConfig config)'''
        def writeConfig(self, config):
            '''void KCoreConfigSkeleton.ItemString.writeConfig(KConfig config)'''
    class ItemPoint(KConfigSkeletonItem):
        """"""
        def __init__(self, _group, _key, reference, defaultValue = QPoint()):
            '''void KCoreConfigSkeleton.ItemPoint.__init__(QString _group, QString _key, QPoint reference, QPoint defaultValue = QPoint())'''
        def swapDefault(self):
            '''void KCoreConfigSkeleton.ItemPoint.swapDefault()'''
        def readDefault(self, config):
            '''void KCoreConfigSkeleton.ItemPoint.readDefault(KConfig config)'''
        def writeConfig(self, config):
            '''void KCoreConfigSkeleton.ItemPoint.writeConfig(KConfig config)'''
        def setDefault(self):
            '''void KCoreConfigSkeleton.ItemPoint.setDefault()'''
        def setDefaultValue(self, v):
            '''void KCoreConfigSkeleton.ItemPoint.setDefaultValue(QPoint v)'''
        def value(self):
            '''QPoint KCoreConfigSkeleton.ItemPoint.value()'''
            return QPoint()
        def setValue(self, v):
            '''void KCoreConfigSkeleton.ItemPoint.setValue(QPoint v)'''
        def property(self):
            '''QVariant KCoreConfigSkeleton.ItemPoint.property()'''
            return QVariant()
        def isEqual(self, p):
            '''bool KCoreConfigSkeleton.ItemPoint.isEqual(QVariant p)'''
            return bool()
        def setProperty(self, p):
            '''void KCoreConfigSkeleton.ItemPoint.setProperty(QVariant p)'''
        def readConfig(self, config):
            '''void KCoreConfigSkeleton.ItemPoint.readConfig(KConfig config)'''
    class ItemSize(KConfigSkeletonItem):
        """"""
        def __init__(self, _group, _key, reference, defaultValue = QSize()):
            '''void KCoreConfigSkeleton.ItemSize.__init__(QString _group, QString _key, QSize reference, QSize defaultValue = QSize())'''
        def swapDefault(self):
            '''void KCoreConfigSkeleton.ItemSize.swapDefault()'''
        def readDefault(self, config):
            '''void KCoreConfigSkeleton.ItemSize.readDefault(KConfig config)'''
        def writeConfig(self, config):
            '''void KCoreConfigSkeleton.ItemSize.writeConfig(KConfig config)'''
        def setDefault(self):
            '''void KCoreConfigSkeleton.ItemSize.setDefault()'''
        def setDefaultValue(self, v):
            '''void KCoreConfigSkeleton.ItemSize.setDefaultValue(QSize v)'''
        def value(self):
            '''QSize KCoreConfigSkeleton.ItemSize.value()'''
            return QSize()
        def setValue(self, v):
            '''void KCoreConfigSkeleton.ItemSize.setValue(QSize v)'''
        def property(self):
            '''QVariant KCoreConfigSkeleton.ItemSize.property()'''
            return QVariant()
        def isEqual(self, p):
            '''bool KCoreConfigSkeleton.ItemSize.isEqual(QVariant p)'''
            return bool()
        def setProperty(self, p):
            '''void KCoreConfigSkeleton.ItemSize.setProperty(QVariant p)'''
        def readConfig(self, config):
            '''void KCoreConfigSkeleton.ItemSize.readConfig(KConfig config)'''
    class ItemULongLong(KConfigSkeletonItem):
        """"""
        def __init__(self, _group, _key, reference, defaultValue = 0):
            '''void KCoreConfigSkeleton.ItemULongLong.__init__(QString _group, QString _key, int reference, int defaultValue = 0)'''
        def swapDefault(self):
            '''void KCoreConfigSkeleton.ItemULongLong.swapDefault()'''
        def readDefault(self, config):
            '''void KCoreConfigSkeleton.ItemULongLong.readDefault(KConfig config)'''
        def writeConfig(self, config):
            '''void KCoreConfigSkeleton.ItemULongLong.writeConfig(KConfig config)'''
        def setDefault(self):
            '''void KCoreConfigSkeleton.ItemULongLong.setDefault()'''
        def setDefaultValue(self, v):
            '''void KCoreConfigSkeleton.ItemULongLong.setDefaultValue(int v)'''
        def value(self):
            '''int KCoreConfigSkeleton.ItemULongLong.value()'''
            return int()
        def setValue(self, v):
            '''void KCoreConfigSkeleton.ItemULongLong.setValue(int v)'''
        def setMaxValue(self):
            '''int KCoreConfigSkeleton.ItemULongLong.setMaxValue()'''
            return int()
        def setMinValue(self):
            '''int KCoreConfigSkeleton.ItemULongLong.setMinValue()'''
            return int()
        def maxValue(self):
            '''QVariant KCoreConfigSkeleton.ItemULongLong.maxValue()'''
            return QVariant()
        def minValue(self):
            '''QVariant KCoreConfigSkeleton.ItemULongLong.minValue()'''
            return QVariant()
        def property(self):
            '''QVariant KCoreConfigSkeleton.ItemULongLong.property()'''
            return QVariant()
        def isEqual(self, p):
            '''bool KCoreConfigSkeleton.ItemULongLong.isEqual(QVariant p)'''
            return bool()
        def setProperty(self, p):
            '''void KCoreConfigSkeleton.ItemULongLong.setProperty(QVariant p)'''
        def readConfig(self, config):
            '''void KCoreConfigSkeleton.ItemULongLong.readConfig(KConfig config)'''
    class ItemDouble(KConfigSkeletonItem):
        """"""
        def __init__(self, _group, _key, reference, defaultValue = 0):
            '''void KCoreConfigSkeleton.ItemDouble.__init__(QString _group, QString _key, float reference, float defaultValue = 0)'''
        def swapDefault(self):
            '''void KCoreConfigSkeleton.ItemDouble.swapDefault()'''
        def readDefault(self, config):
            '''void KCoreConfigSkeleton.ItemDouble.readDefault(KConfig config)'''
        def writeConfig(self, config):
            '''void KCoreConfigSkeleton.ItemDouble.writeConfig(KConfig config)'''
        def setDefault(self):
            '''void KCoreConfigSkeleton.ItemDouble.setDefault()'''
        def setDefaultValue(self, v):
            '''void KCoreConfigSkeleton.ItemDouble.setDefaultValue(float v)'''
        def value(self):
            '''float KCoreConfigSkeleton.ItemDouble.value()'''
            return float()
        def setValue(self, v):
            '''void KCoreConfigSkeleton.ItemDouble.setValue(float v)'''
        def setMaxValue(self):
            '''float KCoreConfigSkeleton.ItemDouble.setMaxValue()'''
            return float()
        def setMinValue(self):
            '''float KCoreConfigSkeleton.ItemDouble.setMinValue()'''
            return float()
        def maxValue(self):
            '''QVariant KCoreConfigSkeleton.ItemDouble.maxValue()'''
            return QVariant()
        def minValue(self):
            '''QVariant KCoreConfigSkeleton.ItemDouble.minValue()'''
            return QVariant()
        def property(self):
            '''QVariant KCoreConfigSkeleton.ItemDouble.property()'''
            return QVariant()
        def isEqual(self, p):
            '''bool KCoreConfigSkeleton.ItemDouble.isEqual(QVariant p)'''
            return bool()
        def setProperty(self, p):
            '''void KCoreConfigSkeleton.ItemDouble.setProperty(QVariant p)'''
        def readConfig(self, config):
            '''void KCoreConfigSkeleton.ItemDouble.readConfig(KConfig config)'''


class KCurrencyCode():
    """"""
    # Enum KCurrencyCode.CurrencyStatus
    ActiveCurrency = 0
    SuspendedCurrency = 0
    ObsoleteCurrency = 0

    def __init__(self, isoCurrencyCode, language = QString()):
        '''void KCurrencyCode.__init__(QString isoCurrencyCode, QString language = QString())'''
    def __init__(self, currencyCodeFile, language = QString()):
        '''void KCurrencyCode.__init__(QFileInfo currencyCodeFile, QString language = QString())'''
    def __init__(self, rhs):
        '''void KCurrencyCode.__init__(KCurrencyCode rhs)'''
    def currencyCodeToName(self, currencyCode, language = QString()):
        '''static QString KCurrencyCode.currencyCodeToName(QString currencyCode, QString language = QString())'''
        return QString()
    def allCurrencyCodesList(self, currencyStatus):
        '''static QStringList KCurrencyCode.allCurrencyCodesList(KCurrencyCode.CurrencyStatusFlags currencyStatus)'''
        return QStringList()
    def isValid(self):
        '''bool KCurrencyCode.isValid()'''
        return bool()
    def isValid(self, currencyCode, currencyStatus):
        '''static bool KCurrencyCode.isValid(QString currencyCode, KCurrencyCode.CurrencyStatusFlags currencyStatus)'''
        return bool()
    def countriesUsingCurrency(self):
        '''QStringList KCurrencyCode.countriesUsingCurrency()'''
        return QStringList()
    def decimalPlaces(self):
        '''int KCurrencyCode.decimalPlaces()'''
        return int()
    def subunitsPerUnit(self):
        '''int KCurrencyCode.subunitsPerUnit()'''
        return int()
    def subunitSymbol(self):
        '''QString KCurrencyCode.subunitSymbol()'''
        return QString()
    def hasSubunitsInCirculation(self):
        '''bool KCurrencyCode.hasSubunitsInCirculation()'''
        return bool()
    def hasSubunits(self):
        '''bool KCurrencyCode.hasSubunits()'''
        return bool()
    def unambiguousSymbol(self):
        '''QString KCurrencyCode.unambiguousSymbol()'''
        return QString()
    def defaultSymbol(self):
        '''QString KCurrencyCode.defaultSymbol()'''
        return QString()
    def symbolList(self):
        '''QStringList KCurrencyCode.symbolList()'''
        return QStringList()
    def dateWithdrawn(self):
        '''QDate KCurrencyCode.dateWithdrawn()'''
        return QDate()
    def dateSuspended(self):
        '''QDate KCurrencyCode.dateSuspended()'''
        return QDate()
    def dateIntroduced(self):
        '''QDate KCurrencyCode.dateIntroduced()'''
        return QDate()
    def status(self):
        '''KCurrencyCode.CurrencyStatus KCurrencyCode.status()'''
        return KCurrencyCode.CurrencyStatus()
    def isoName(self):
        '''QString KCurrencyCode.isoName()'''
        return QString()
    def name(self):
        '''QString KCurrencyCode.name()'''
        return QString()
    def isoCurrencyCodeNumeric(self):
        '''QString KCurrencyCode.isoCurrencyCodeNumeric()'''
        return QString()
    def isoCurrencyCode(self):
        '''QString KCurrencyCode.isoCurrencyCode()'''
        return QString()
    class CurrencyStatusFlags():
        """"""
        def __init__(self):
            '''KCurrencyCode.CurrencyStatusFlags KCurrencyCode.CurrencyStatusFlags.__init__()'''
            return KCurrencyCode.CurrencyStatusFlags()
        def __init__(self):
            '''int KCurrencyCode.CurrencyStatusFlags.__init__()'''
            return int()
        def __init__(self):
            '''void KCurrencyCode.CurrencyStatusFlags.__init__()'''
        def __bool__(self):
            '''int KCurrencyCode.CurrencyStatusFlags.__bool__()'''
            return int()
        def __ne__(self, f):
            '''bool KCurrencyCode.CurrencyStatusFlags.__ne__(KCurrencyCode.CurrencyStatusFlags f)'''
            return bool()
        def __eq__(self, f):
            '''bool KCurrencyCode.CurrencyStatusFlags.__eq__(KCurrencyCode.CurrencyStatusFlags f)'''
            return bool()
        def __invert__(self):
            '''KCurrencyCode.CurrencyStatusFlags KCurrencyCode.CurrencyStatusFlags.__invert__()'''
            return KCurrencyCode.CurrencyStatusFlags()
        def __and__(self, mask):
            '''KCurrencyCode.CurrencyStatusFlags KCurrencyCode.CurrencyStatusFlags.__and__(int mask)'''
            return KCurrencyCode.CurrencyStatusFlags()
        def __xor__(self, f):
            '''KCurrencyCode.CurrencyStatusFlags KCurrencyCode.CurrencyStatusFlags.__xor__(KCurrencyCode.CurrencyStatusFlags f)'''
            return KCurrencyCode.CurrencyStatusFlags()
        def __xor__(self, f):
            '''KCurrencyCode.CurrencyStatusFlags KCurrencyCode.CurrencyStatusFlags.__xor__(int f)'''
            return KCurrencyCode.CurrencyStatusFlags()
        def __or__(self, f):
            '''KCurrencyCode.CurrencyStatusFlags KCurrencyCode.CurrencyStatusFlags.__or__(KCurrencyCode.CurrencyStatusFlags f)'''
            return KCurrencyCode.CurrencyStatusFlags()
        def __or__(self, f):
            '''KCurrencyCode.CurrencyStatusFlags KCurrencyCode.CurrencyStatusFlags.__or__(int f)'''
            return KCurrencyCode.CurrencyStatusFlags()
        def __int__(self):
            '''int KCurrencyCode.CurrencyStatusFlags.__int__()'''
            return int()
        def __ixor__(self, f):
            '''KCurrencyCode.CurrencyStatusFlags KCurrencyCode.CurrencyStatusFlags.__ixor__(KCurrencyCode.CurrencyStatusFlags f)'''
            return KCurrencyCode.CurrencyStatusFlags()
        def __ior__(self, f):
            '''KCurrencyCode.CurrencyStatusFlags KCurrencyCode.CurrencyStatusFlags.__ior__(KCurrencyCode.CurrencyStatusFlags f)'''
            return KCurrencyCode.CurrencyStatusFlags()
        def __iand__(self, mask):
            '''KCurrencyCode.CurrencyStatusFlags KCurrencyCode.CurrencyStatusFlags.__iand__(int mask)'''
            return KCurrencyCode.CurrencyStatusFlags()


class KDateTime():
    """"""
    # Enum KDateTime.Comparison
    Before = 0
    AtStart = 0
    Inside = 0
    AtEnd = 0
    After = 0
    Equal = 0
    Outside = 0
    StartsAt = 0
    EndsAt = 0

    # Enum KDateTime.TimeFormat
    ISODate = 0
    RFCDate = 0
    RFCDateDay = 0
    QtTextDate = 0
    LocalDate = 0
    RFC3339Date = 0

    # Enum KDateTime.SpecType
    Invalid = 0
    UTC = 0
    OffsetFromUTC = 0
    TimeZone = 0
    LocalZone = 0
    ClockTime = 0

    def __init__(self):
        '''void KDateTime.__init__()'''
    def __init__(self, date, spec = None):
        '''void KDateTime.__init__(QDate date, KDateTime.Spec spec = KDateTime.Spec(KDateTime.LocalZone))'''
    def __init__(self, date, time, spec = None):
        '''void KDateTime.__init__(QDate date, QTime time, KDateTime.Spec spec = KDateTime.Spec(KDateTime.LocalZone))'''
    def __init__(self, dt, spec):
        '''void KDateTime.__init__(QDateTime dt, KDateTime.Spec spec)'''
    def __init__(self, dt):
        '''void KDateTime.__init__(QDateTime dt)'''
    def __init__(self, other):
        '''void KDateTime.__init__(KDateTime other)'''
    def realCurrentLocalDateTime(self):
        '''static KDateTime KDateTime.realCurrentLocalDateTime()'''
        return KDateTime()
    def setSimulatedSystemTime(self, newTime):
        '''static void KDateTime.setSimulatedSystemTime(KDateTime newTime)'''
    def detach(self):
        '''void KDateTime.detach()'''
    def __ge__(self, other):
        '''bool KDateTime.__ge__(KDateTime other)'''
        return bool()
    def __gt__(self, other):
        '''bool KDateTime.__gt__(KDateTime other)'''
        return bool()
    def __le__(self, other):
        '''bool KDateTime.__le__(KDateTime other)'''
        return bool()
    def __lt__(self, other):
        '''bool KDateTime.__lt__(KDateTime other)'''
        return bool()
    def __ne__(self, other):
        '''bool KDateTime.__ne__(KDateTime other)'''
        return bool()
    def __eq__(self, other):
        '''bool KDateTime.__eq__(KDateTime other)'''
        return bool()
    def compare(self, other):
        '''KDateTime.Comparison KDateTime.compare(KDateTime other)'''
        return KDateTime.Comparison()
    def outOfRange(self):
        '''bool KDateTime.outOfRange()'''
        return bool()
    def setFromStringDefault(self, spec):
        '''static void KDateTime.setFromStringDefault(KDateTime.Spec spec)'''
    def fromString(self, string, format = None, negZero = None):
        '''static KDateTime KDateTime.fromString(QString string, KDateTime.TimeFormat format = KDateTime.ISODate, bool negZero)'''
        return KDateTime()
    def fromString(self, string, format, zones = None, offsetIfAmbiguous = True):
        '''static KDateTime KDateTime.fromString(QString string, QString format, KTimeZones zones = None, bool offsetIfAmbiguous = True)'''
        return KDateTime()
    def toString(self, format):
        '''QString KDateTime.toString(QString format)'''
        return QString()
    def toString(self, format = None):
        '''QString KDateTime.toString(KDateTime.TimeFormat format = KDateTime.ISODate)'''
        return QString()
    def currentLocalTime(self):
        '''static QTime KDateTime.currentLocalTime()'''
        return QTime()
    def currentLocalDate(self):
        '''static QDate KDateTime.currentLocalDate()'''
        return QDate()
    def currentDateTime(self, spec):
        '''static KDateTime KDateTime.currentDateTime(KDateTime.Spec spec)'''
        return KDateTime()
    def currentUtcDateTime(self):
        '''static KDateTime KDateTime.currentUtcDateTime()'''
        return KDateTime()
    def currentLocalDateTime(self):
        '''static KDateTime KDateTime.currentLocalDateTime()'''
        return KDateTime()
    def daysTo(self, other):
        '''int KDateTime.daysTo(KDateTime other)'''
        return int()
    def secsTo_long(self, other):
        '''int KDateTime.secsTo_long(KDateTime other)'''
        return int()
    def secsTo(self, other):
        '''int KDateTime.secsTo(KDateTime other)'''
        return int()
    def addYears(self, years):
        '''KDateTime KDateTime.addYears(int years)'''
        return KDateTime()
    def addMonths(self, months):
        '''KDateTime KDateTime.addMonths(int months)'''
        return KDateTime()
    def addDays(self, days):
        '''KDateTime KDateTime.addDays(int days)'''
        return KDateTime()
    def addSecs(self, secs):
        '''KDateTime KDateTime.addSecs(int secs)'''
        return KDateTime()
    def addMSecs(self, msecs):
        '''KDateTime KDateTime.addMSecs(int msecs)'''
        return KDateTime()
    def setSecondOccurrence(self, second):
        '''void KDateTime.setSecondOccurrence(bool second)'''
    def setTimeSpec(self, spec):
        '''void KDateTime.setTimeSpec(KDateTime.Spec spec)'''
    def setDateTime(self, dt):
        '''void KDateTime.setDateTime(QDateTime dt)'''
    def setTime(self, time):
        '''void KDateTime.setTime(QTime time)'''
    def setDate(self, date):
        '''void KDateTime.setDate(QDate date)'''
    def setDateOnly(self, dateOnly):
        '''void KDateTime.setDateOnly(bool dateOnly)'''
    def setTime_t(self, seconds):
        '''void KDateTime.setTime_t(int seconds)'''
    def toTime_t(self):
        '''int KDateTime.toTime_t()'''
        return int()
    def toTimeSpec(self, spec):
        '''KDateTime KDateTime.toTimeSpec(KDateTime.Spec spec)'''
        return KDateTime()
    def toTimeSpec(self, dt):
        '''KDateTime KDateTime.toTimeSpec(KDateTime dt)'''
        return KDateTime()
    def toZone(self, zone):
        '''KDateTime KDateTime.toZone(KTimeZone zone)'''
        return KDateTime()
    def toClockTime(self):
        '''KDateTime KDateTime.toClockTime()'''
        return KDateTime()
    def toLocalZone(self):
        '''KDateTime KDateTime.toLocalZone()'''
        return KDateTime()
    def toOffsetFromUtc(self):
        '''KDateTime KDateTime.toOffsetFromUtc()'''
        return KDateTime()
    def toOffsetFromUtc(self, utcOffset):
        '''KDateTime KDateTime.toOffsetFromUtc(int utcOffset)'''
        return KDateTime()
    def toUtc(self):
        '''KDateTime KDateTime.toUtc()'''
        return KDateTime()
    def isSecondOccurrence(self):
        '''bool KDateTime.isSecondOccurrence()'''
        return bool()
    def utcOffset(self):
        '''int KDateTime.utcOffset()'''
        return int()
    def isOffsetFromUtc(self):
        '''bool KDateTime.isOffsetFromUtc()'''
        return bool()
    def isUtc(self):
        '''bool KDateTime.isUtc()'''
        return bool()
    def isClockTime(self):
        '''bool KDateTime.isClockTime()'''
        return bool()
    def isLocalZone(self):
        '''bool KDateTime.isLocalZone()'''
        return bool()
    def timeType(self):
        '''KDateTime.SpecType KDateTime.timeType()'''
        return KDateTime.SpecType()
    def timeSpec(self):
        '''KDateTime.Spec KDateTime.timeSpec()'''
        return KDateTime.Spec()
    def timeZone(self):
        '''KTimeZone KDateTime.timeZone()'''
        return KTimeZone()
    def dateTime(self):
        '''QDateTime KDateTime.dateTime()'''
        return QDateTime()
    def time(self):
        '''QTime KDateTime.time()'''
        return QTime()
    def date(self):
        '''QDate KDateTime.date()'''
        return QDate()
    def isDateOnly(self):
        '''bool KDateTime.isDateOnly()'''
        return bool()
    def isValid(self):
        '''bool KDateTime.isValid()'''
        return bool()
    def isNull(self):
        '''bool KDateTime.isNull()'''
        return bool()
    class Spec():
        """"""
        def __init__(self):
            '''void KDateTime.Spec.__init__()'''
        def __init__(self, tz):
            '''void KDateTime.Spec.__init__(KTimeZone tz)'''
        def __init__(self, type, utcOffset = 0):
            '''void KDateTime.Spec.__init__(KDateTime.SpecType type, int utcOffset = 0)'''
        def __init__(self, spec):
            '''void KDateTime.Spec.__init__(KDateTime.Spec spec)'''
        def LocalZone(self):
            '''static KDateTime.Spec KDateTime.Spec.LocalZone()'''
            return KDateTime.Spec()
        def OffsetFromUTC(self, utcOffset):
            '''static KDateTime.Spec KDateTime.Spec.OffsetFromUTC(int utcOffset)'''
            return KDateTime.Spec()
        def ClockTime(self):
            '''static KDateTime.Spec KDateTime.Spec.ClockTime()'''
            return KDateTime.Spec()
        def UTC(self):
            '''static KDateTime.Spec KDateTime.Spec.UTC()'''
            return KDateTime.Spec()
        def equivalentTo(self, other):
            '''bool KDateTime.Spec.equivalentTo(KDateTime.Spec other)'''
            return bool()
        def __ne__(self, other):
            '''bool KDateTime.Spec.__ne__(KDateTime.Spec other)'''
            return bool()
        def __eq__(self, other):
            '''bool KDateTime.Spec.__eq__(KDateTime.Spec other)'''
            return bool()
        def setType(self, type, utcOffset = 0):
            '''void KDateTime.Spec.setType(KDateTime.SpecType type, int utcOffset = 0)'''
        def setType(self, tz):
            '''void KDateTime.Spec.setType(KTimeZone tz)'''
        def utcOffset(self):
            '''int KDateTime.Spec.utcOffset()'''
            return int()
        def isOffsetFromUtc(self):
            '''bool KDateTime.Spec.isOffsetFromUtc()'''
            return bool()
        def isUtc(self):
            '''bool KDateTime.Spec.isUtc()'''
            return bool()
        def isClockTime(self):
            '''bool KDateTime.Spec.isClockTime()'''
            return bool()
        def isLocalZone(self):
            '''bool KDateTime.Spec.isLocalZone()'''
            return bool()
        def type(self):
            '''KDateTime.SpecType KDateTime.Spec.type()'''
            return KDateTime.SpecType()
        def timeZone(self):
            '''KTimeZone KDateTime.Spec.timeZone()'''
            return KTimeZone()
        def isValid(self):
            '''bool KDateTime.Spec.isValid()'''
            return bool()


class KDEDModule(QObject):
    """"""
    def __init__(self, parent = None):
        '''void KDEDModule.__init__(QObject parent = None)'''
    windowUnregistered = pyqtSignal() # void windowUnregistered(qlonglong) - signal
    windowRegistered = pyqtSignal() # void windowRegistered(qlonglong) - signal
    moduleDeleted = pyqtSignal() # void moduleDeleted(KDEDModule *) - signal
    def moduleName(self):
        '''QString KDEDModule.moduleName()'''
        return QString()
    def setModuleName(self, name):
        '''void KDEDModule.setModuleName(QString name)'''


class KDesktopFile(KConfig):
    """"""
    def __init__(self, resourceType, fileName):
        '''void KDesktopFile.__init__(str resourceType, QString fileName)'''
    def __init__(self, fileName):
        '''void KDesktopFile.__init__(QString fileName)'''
    def resource(self):
        '''str KDesktopFile.resource()'''
        return str()
    def fileName(self):
        '''QString KDesktopFile.fileName()'''
        return QString()
    def copyTo(self, file):
        '''KDesktopFile KDesktopFile.copyTo(QString file)'''
        return KDesktopFile()
    def noDisplay(self):
        '''bool KDesktopFile.noDisplay()'''
        return bool()
    def sortOrder(self):
        '''QStringList KDesktopFile.sortOrder()'''
        return QStringList()
    def readDocPath(self):
        '''QString KDesktopFile.readDocPath()'''
        return QString()
    def tryExec(self):
        '''bool KDesktopFile.tryExec()'''
        return bool()
    def hasDeviceType(self):
        '''bool KDesktopFile.hasDeviceType()'''
        return bool()
    def hasMimeTypeType(self):
        '''bool KDesktopFile.hasMimeTypeType()'''
        return bool()
    def hasApplicationType(self):
        '''bool KDesktopFile.hasApplicationType()'''
        return bool()
    def hasLinkType(self):
        '''bool KDesktopFile.hasLinkType()'''
        return bool()
    def hasActionGroup(self, group):
        '''bool KDesktopFile.hasActionGroup(QString group)'''
        return bool()
    def actionGroup(self, group):
        '''KConfigGroup KDesktopFile.actionGroup(QString group)'''
        return KConfigGroup()
    def readActions(self):
        '''QStringList KDesktopFile.readActions()'''
        return QStringList()
    def readUrl(self):
        '''QString KDesktopFile.readUrl()'''
        return QString()
    def readDevice(self):
        '''QString KDesktopFile.readDevice()'''
        return QString()
    def readPath(self):
        '''QString KDesktopFile.readPath()'''
        return QString()
    def readGenericName(self):
        '''QString KDesktopFile.readGenericName()'''
        return QString()
    def readComment(self):
        '''QString KDesktopFile.readComment()'''
        return QString()
    def readName(self):
        '''QString KDesktopFile.readName()'''
        return QString()
    def readIcon(self):
        '''QString KDesktopFile.readIcon()'''
        return QString()
    def readType(self):
        '''QString KDesktopFile.readType()'''
        return QString()
    def desktopGroup(self):
        '''KConfigGroup KDesktopFile.desktopGroup()'''
        return KConfigGroup()
    def locateLocal(self, path):
        '''static QString KDesktopFile.locateLocal(QString path)'''
        return QString()
    def isAuthorizedDesktopFile(self, path):
        '''static bool KDesktopFile.isAuthorizedDesktopFile(QString path)'''
        return bool()
    def isDesktopFile(self, path):
        '''static bool KDesktopFile.isDesktopFile(QString path)'''
        return bool()


class KEncodingDetector():
    """"""
    # Enum KEncodingDetector.AutoDetectScript
    __kdevpythondocumentation_builtin_None = 0
    SemiautomaticDetection = 0
    Arabic = 0
    Baltic = 0
    CentralEuropean = 0
    ChineseSimplified = 0
    ChineseTraditional = 0
    Cyrillic = 0
    Greek = 0
    Hebrew = 0
    Japanese = 0
    Korean = 0
    NorthernSaami = 0
    SouthEasternEurope = 0
    Thai = 0
    Turkish = 0
    Unicode = 0
    WesternEuropean = 0

    # Enum KEncodingDetector.EncodingChoiceSource
    DefaultEncoding = 0
    AutoDetectedEncoding = 0
    BOM = 0
    EncodingFromXMLHeader = 0
    EncodingFromMetaTag = 0
    EncodingFromHTTPHeader = 0
    UserChosenEncoding = 0

    def __init__(self):
        '''void KEncodingDetector.__init__()'''
    def __init__(self, codec, source, script = None):
        '''void KEncodingDetector.__init__(QTextCodec codec, KEncodingDetector.EncodingChoiceSource source, KEncodingDetector.AutoDetectScript script = KEncodingDetector.None)'''
    def decoder(self):
        '''QTextDecoder KEncodingDetector.decoder()'''
        return QTextDecoder()
    def analyze(self, data, len):
        '''bool KEncodingDetector.analyze(str data, int len)'''
        return bool()
    def errorsIfUtf8(self, data, length):
        '''bool KEncodingDetector.errorsIfUtf8(str data, int length)'''
        return bool()
    def processNull(self, data, length):
        '''bool KEncodingDetector.processNull(str data, int length)'''
        return bool()
    def hasAutoDetectionForScript(self):
        '''static KEncodingDetector.AutoDetectScript KEncodingDetector.hasAutoDetectionForScript()'''
        return KEncodingDetector.AutoDetectScript()
    def nameForScript(self):
        '''static KEncodingDetector.AutoDetectScript KEncodingDetector.nameForScript()'''
        return KEncodingDetector.AutoDetectScript()
    def scriptForName(self, lang):
        '''static KEncodingDetector.AutoDetectScript KEncodingDetector.scriptForName(QString lang)'''
        return KEncodingDetector.AutoDetectScript()
    def flush(self):
        '''QString KEncodingDetector.flush()'''
        return QString()
    def resetDecoder(self):
        '''void KEncodingDetector.resetDecoder()'''
    def decodedInvalidCharacters(self):
        '''bool KEncodingDetector.decodedInvalidCharacters()'''
        return bool()
    def decodeWithBuffering(self, data, len):
        '''QString KEncodingDetector.decodeWithBuffering(str data, int len)'''
        return QString()
    def decode(self, data, len):
        '''QString KEncodingDetector.decode(str data, int len)'''
        return QString()
    def decode(self, data):
        '''QString KEncodingDetector.decode(QByteArray data)'''
        return QString()
    def encodingChoiceSource(self):
        '''KEncodingDetector.EncodingChoiceSource KEncodingDetector.encodingChoiceSource()'''
        return KEncodingDetector.EncodingChoiceSource()
    def autoDetectLanguage(self):
        '''KEncodingDetector.AutoDetectScript KEncodingDetector.autoDetectLanguage()'''
        return KEncodingDetector.AutoDetectScript()
    def setAutoDetectLanguage(self):
        '''KEncodingDetector.AutoDetectScript KEncodingDetector.setAutoDetectLanguage()'''
        return KEncodingDetector.AutoDetectScript()
    def visuallyOrdered(self):
        '''bool KEncodingDetector.visuallyOrdered()'''
        return bool()
    def encoding(self):
        '''str KEncodingDetector.encoding()'''
        return str()
    def setEncoding(self, encoding, type):
        '''bool KEncodingDetector.setEncoding(str encoding, KEncodingDetector.EncodingChoiceSource type)'''
        return bool()


class KEncodingProber():
    """"""
    # Enum KEncodingProber.ProberType
    __kdevpythondocumentation_builtin_None = 0
    Universal = 0
    Arabic = 0
    Baltic = 0
    CentralEuropean = 0
    ChineseSimplified = 0
    ChineseTraditional = 0
    Cyrillic = 0
    Greek = 0
    Hebrew = 0
    Japanese = 0
    Korean = 0
    NorthernSaami = 0
    Other = 0
    SouthEasternEurope = 0
    Thai = 0
    Turkish = 0
    Unicode = 0
    WesternEuropean = 0

    # Enum KEncodingProber.ProberState
    FoundIt = 0
    NotMe = 0
    Probing = 0

    def __init__(self, proberType = None):
        '''void KEncodingProber.__init__(KEncodingProber.ProberType proberType = KEncodingProber.Universal)'''
    def nameForProberType(self, proberType):
        '''static QString KEncodingProber.nameForProberType(KEncodingProber.ProberType proberType)'''
        return QString()
    def proberTypeForName(self, lang):
        '''static KEncodingProber.ProberType KEncodingProber.proberTypeForName(QString lang)'''
        return KEncodingProber.ProberType()
    def setProberType(self, proberType):
        '''void KEncodingProber.setProberType(KEncodingProber.ProberType proberType)'''
    def proberType(self):
        '''KEncodingProber.ProberType KEncodingProber.proberType()'''
        return KEncodingProber.ProberType()
    def confidence(self):
        '''float KEncodingProber.confidence()'''
        return float()
    def encoding(self):
        '''QByteArray KEncodingProber.encoding()'''
        return QByteArray()
    def encodingName(self):
        '''str KEncodingProber.encodingName()'''
        return str()
    def state(self):
        '''KEncodingProber.ProberState KEncodingProber.state()'''
        return KEncodingProber.ProberState()
    def feed(self, data):
        '''KEncodingProber.ProberState KEncodingProber.feed(QByteArray data)'''
        return KEncodingProber.ProberState()
    def feed(self, data, len):
        '''KEncodingProber.ProberState KEncodingProber.feed(str data, int len)'''
        return KEncodingProber.ProberState()
    def reset(self):
        '''void KEncodingProber.reset()'''


class KDEPluginVerificationData():
    """"""
    PluginVerificationDataVersion = None # int - member
    KDEVersion = None # int - member
    KDEVersionString = None # str - member
    dataVersion = None # str - member
    def __init__(self):
        '''void KDEPluginVerificationData.__init__()'''
    def __init__(self):
        '''KDEPluginVerificationData KDEPluginVerificationData.__init__()'''
        return KDEPluginVerificationData()


class KFilterBase():
    """"""
    # Enum KFilterBase.FilterFlags
    NoHeaders = 0
    WithHeaders = 0

    # Enum KFilterBase.Result
    Ok = 0
    End = 0
    Error = 0

    def __init__(self):
        '''void KFilterBase.__init__()'''
    def findFilterByMimeType(self, mimeType):
        '''static KFilterBase KFilterBase.findFilterByMimeType(QString mimeType)'''
        return KFilterBase()
    def findFilterByFileName(self, fileName):
        '''static KFilterBase KFilterBase.findFilterByFileName(QString fileName)'''
        return KFilterBase()
    def filterFlags(self):
        '''KFilterBase.FilterFlags KFilterBase.filterFlags()'''
        return KFilterBase.FilterFlags()
    def setFilterFlags(self, flags):
        '''void KFilterBase.setFilterFlags(KFilterBase.FilterFlags flags)'''
    def compress(self, finish):
        '''abstract KFilterBase.Result KFilterBase.compress(bool finish)'''
        return KFilterBase.Result()
    def uncompress(self):
        '''abstract KFilterBase.Result KFilterBase.uncompress()'''
        return KFilterBase.Result()
    def outBufferAvailable(self):
        '''abstract int KFilterBase.outBufferAvailable()'''
        return int()
    def outBufferFull(self):
        '''bool KFilterBase.outBufferFull()'''
        return bool()
    def inBufferAvailable(self):
        '''abstract int KFilterBase.inBufferAvailable()'''
        return int()
    def inBufferEmpty(self):
        '''bool KFilterBase.inBufferEmpty()'''
        return bool()
    def setInBuffer(self, data, size):
        '''abstract void KFilterBase.setInBuffer(str data, int size)'''
    def setOutBuffer(self, data, maxlen):
        '''abstract void KFilterBase.setOutBuffer(str data, int maxlen)'''
    def writeHeader(self, filename):
        '''abstract bool KFilterBase.writeHeader(QByteArray filename)'''
        return bool()
    def readHeader(self):
        '''abstract bool KFilterBase.readHeader()'''
        return bool()
    def reset(self):
        '''void KFilterBase.reset()'''
    def terminate(self):
        '''void KFilterBase.terminate()'''
    def mode(self):
        '''abstract int KFilterBase.mode()'''
        return int()
    def init(self, mode):
        '''abstract void KFilterBase.init(int mode)'''
    def device(self):
        '''QIODevice KFilterBase.device()'''
        return QIODevice()
    def setDevice(self, dev, autodelete = False):
        '''void KFilterBase.setDevice(QIODevice dev, bool autodelete = False)'''


class KFilterDev(QIODevice):
    """"""
    def writeData(self, data, len):
        '''int KFilterDev.writeData(str data, int len)'''
        return int()
    def readData(self, data, maxlen):
        '''int KFilterDev.readData(str data, int maxlen)'''
        return int()
    def device(self, inDevice, mimetype, autoDeleteInDevice = True):
        '''static QIODevice KFilterDev.device(QIODevice inDevice, QString mimetype, bool autoDeleteInDevice = True)'''
        return QIODevice()
    def deviceForFile(self, fileName, mimetype = QString(), forceFilter = False):
        '''static QIODevice KFilterDev.deviceForFile(QString fileName, QString mimetype = QString(), bool forceFilter = False)'''
        return QIODevice()
    def atEnd(self):
        '''bool KFilterDev.atEnd()'''
        return bool()
    def seek(self):
        '''int KFilterDev.seek()'''
        return int()
    def setSkipHeaders(self):
        '''void KFilterDev.setSkipHeaders()'''
    def setOrigFileName(self, fileName):
        '''void KFilterDev.setOrigFileName(QByteArray fileName)'''
    def close(self):
        '''void KFilterDev.close()'''
    def open(self, mode):
        '''bool KFilterDev.open(QIODevice.OpenMode mode)'''
        return bool()


class KCatalogLoader():
    """"""
    def __init__(self, catalogName):
        '''void KCatalogLoader.__init__(QString catalogName)'''
    def __init__(self):
        '''KCatalogLoader KCatalogLoader.__init__()'''
        return KCatalogLoader()


class KJobTrackerInterface(QObject):
    """"""
    def __init__(self, parent = None):
        '''void KJobTrackerInterface.__init__(QObject parent = None)'''
    def speed(self, job, value):
        '''void KJobTrackerInterface.speed(KJob job, int value)'''
    def percent(self, job, percent):
        '''void KJobTrackerInterface.percent(KJob job, int percent)'''
    def processedAmount(self, job, unit, amount):
        '''void KJobTrackerInterface.processedAmount(KJob job, KJob.Unit unit, int amount)'''
    def totalAmount(self, job, unit, amount):
        '''void KJobTrackerInterface.totalAmount(KJob job, KJob.Unit unit, int amount)'''
    def warning(self, job, plain, rich):
        '''void KJobTrackerInterface.warning(KJob job, QString plain, QString rich)'''
    def infoMessage(self, job, plain, rich):
        '''void KJobTrackerInterface.infoMessage(KJob job, QString plain, QString rich)'''
    def description(self, job, title, field1, field2):
        '''void KJobTrackerInterface.description(KJob job, QString title, unknown-type field1, unknown-type field2)'''
    def resumed(self, job):
        '''void KJobTrackerInterface.resumed(KJob job)'''
    def suspended(self, job):
        '''void KJobTrackerInterface.suspended(KJob job)'''
    def finished(self, job):
        '''void KJobTrackerInterface.finished(KJob job)'''
    def unregisterJob(self, job):
        '''void KJobTrackerInterface.unregisterJob(KJob job)'''
    def registerJob(self, job):
        '''void KJobTrackerInterface.registerJob(KJob job)'''


class KJobUiDelegate(QObject):
    """"""
    def __init__(self):
        '''void KJobUiDelegate.__init__()'''
    def slotWarning(self, job, plain, rich):
        '''void KJobUiDelegate.slotWarning(KJob job, QString plain, QString rich)'''
    def isAutoWarningHandlingEnabled(self):
        '''bool KJobUiDelegate.isAutoWarningHandlingEnabled()'''
        return bool()
    def setAutoWarningHandlingEnabled(self, enable):
        '''void KJobUiDelegate.setAutoWarningHandlingEnabled(bool enable)'''
    def isAutoErrorHandlingEnabled(self):
        '''bool KJobUiDelegate.isAutoErrorHandlingEnabled()'''
        return bool()
    def setAutoErrorHandlingEnabled(self, enable):
        '''void KJobUiDelegate.setAutoErrorHandlingEnabled(bool enable)'''
    def showErrorMessage(self):
        '''void KJobUiDelegate.showErrorMessage()'''
    def job(self):
        '''KJob KJobUiDelegate.job()'''
        return KJob()


class KLibLoader(QObject):
    """"""
    # Enum KLibLoader.ComponentLoadingError
    ErrNoLibrary = 0
    ErrNoFactory = 0
    ErrNoComponent = 0
    ErrServiceProvidesNoLibrary = 0
    ErrNoServiceFound = 0

    def errorString(self, componentLoadingError):
        '''static QString KLibLoader.errorString(int componentLoadingError)'''
        return QString()
    def findLibrary(self, libname, cData = None):
        '''static QString KLibLoader.findLibrary(QString libname, KComponentData cData = KGlobal.mainComponent())'''
        return QString()
    def self(self):
        '''static KLibLoader KLibLoader.self()'''
        return KLibLoader()
    def unloadLibrary(self, libname):
        '''void KLibLoader.unloadLibrary(QString libname)'''
    def lastErrorMessage(self):
        '''QString KLibLoader.lastErrorMessage()'''
        return QString()
    def library(self, libname, loadHint = 0):
        '''KLibrary KLibLoader.library(QString libname, QLibrary.LoadHints loadHint = 0)'''
        return KLibrary()
    def factory(self, libname, loadHint = 0):
        '''KPluginFactory KLibLoader.factory(QString libname, QLibrary.LoadHints loadHint = 0)'''
        return KPluginFactory()


class KLibrary(QLibrary):
    """"""
    def __init__(self, parent = None):
        '''void KLibrary.__init__(QObject parent = None)'''
    def __init__(self, name, cData = None, parent = None):
        '''void KLibrary.__init__(QString name, KComponentData cData = KGlobal.mainComponent(), QObject parent = None)'''
    def __init__(self, name, verNum, cData = None, parent = None):
        '''void KLibrary.__init__(QString name, int verNum, KComponentData cData = KGlobal.mainComponent(), QObject parent = None)'''
    def unload(self):
        '''bool KLibrary.unload()'''
        return bool()
    def setFileName(self, name, data = None):
        '''void KLibrary.setFileName(QString name, KComponentData data = KGlobal.mainComponent())'''
    def factory(self, factoryname = None):
        '''KPluginFactory KLibrary.factory(str factoryname = None)'''
        return KPluginFactory()


class KLocale():
    """"""
    # Enum KLocale.DateTimeComponentFormat
    DefaultComponentFormat = 0
    ShortNumber = 0
    LongNumber = 0
    NarrowName = 0
    ShortName = 0
    LongName = 0

    # Enum KLocale.DateTimeComponent
    Year = 0
    YearName = 0
    Month = 0
    MonthName = 0
    Day = 0
    DayName = 0
    JulianDay = 0
    EraName = 0
    EraYear = 0
    YearInEra = 0
    DayOfYear = 0
    DayOfYearName = 0
    DayOfWeek = 0
    DayOfWeekName = 0
    Week = 0
    WeekYear = 0
    MonthsInYear = 0
    WeeksInYear = 0
    DaysInYear = 0
    DaysInMonth = 0
    DaysInWeek = 0
    Hour = 0
    Minute = 0
    Second = 0
    Millisecond = 0
    DayPeriod = 0
    DayPeriodHour = 0
    Timezone = 0
    TimezoneName = 0
    UnixTime = 0

    # Enum KLocale.DateTimeParseMode
    LiberalParsing = 0

    # Enum KLocale.WeekNumberSystem
    DefaultWeekNumber = 0
    IsoWeekNumber = 0
    FirstFullWeek = 0
    FirstPartialWeek = 0
    SimpleWeek = 0

    # Enum KLocale.CalendarSystem
    QDateCalendar = 0
    CopticCalendar = 0
    EthiopianCalendar = 0
    GregorianCalendar = 0
    HebrewCalendar = 0
    IslamicCivilCalendar = 0
    IndianNationalCalendar = 0
    JalaliCalendar = 0
    JapaneseCalendar = 0
    JulianCalendar = 0
    MinguoCalendar = 0
    ThaiCalendar = 0

    # Enum KLocale.DateTimeFormatStandard
    KdeFormat = 0
    PosixFormat = 0
    UnicodeFormat = 0

    # Enum KLocale.TimeProcessingOption
    ProcessStrict = 0
    ProcessNonStrict = 0

    # Enum KLocale.TimeFormatOption
    TimeDefault = 0
    TimeWithoutSeconds = 0
    TimeWithoutAmPm = 0
    TimeDuration = 0
    TimeFoldHours = 0

    # Enum KLocale.BinaryUnitDialect
    DefaultBinaryDialect = 0
    IECBinaryDialect = 0
    JEDECBinaryDialect = 0
    MetricBinaryDialect = 0
    LastBinaryDialect = 0

    # Enum KLocale.BinarySizeUnits
    DefaultBinaryUnits = 0
    UnitByte = 0
    UnitKiloByte = 0
    UnitMegaByte = 0
    UnitGigaByte = 0
    UnitTeraByte = 0
    UnitPetaByte = 0
    UnitExaByte = 0
    UnitZettaByte = 0
    UnitYottaByte = 0
    UnitLastUnit = 0

    # Enum KLocale.MeasureSystem
    Metric = 0
    Imperial = 0

    # Enum KLocale.ReadTimeFlags
    WithSeconds = 0
    WithoutSeconds = 0

    # Enum KLocale.ReadDateFlags
    NormalFormat = 0
    ShortFormat = 0
    IsoFormat = 0
    IsoWeekFormat = 0
    IsoOrdinalFormat = 0

    # Enum KLocale.DateTimeFormatOption
    TimeZone = 0
    Seconds = 0

    # Enum KLocale.DateFormat
    ShortDate = 0
    LongDate = 0
    FancyShortDate = 0
    FancyLongDate = 0
    IsoDate = 0
    IsoWeekDate = 0
    IsoOrdinalDate = 0

    # Enum KLocale.DigitSet
    ArabicDigits = 0
    ArabicIndicDigits = 0
    EasternArabicIndicDigits = 0
    DevenagariDigits = 0
    BengaliDigits = 0
    GujaratiDigits = 0
    GurmukhiDigits = 0
    KannadaDigits = 0
    KhmerDigits = 0
    MalayalamDigits = 0
    OriyaDigits = 0
    TamilDigits = 0
    TeluguDigits = 0
    ThaiDigits = 0

    # Enum KLocale.SignPosition
    ParensAround = 0
    BeforeQuantityMoney = 0
    AfterQuantityMoney = 0
    BeforeMoney = 0
    AfterMoney = 0

    def __init__(self, catalog, config = None):
        '''void KLocale.__init__(QString catalog, unknown-type config = KSharedConfig.Ptr())'''
    def __init__(self, catalog, language, country = QString(), config = None):
        '''void KLocale.__init__(QString catalog, QString language, QString country = QString(), KConfig config = None)'''
    def __init__(self):
        '''KLocale KLocale.__init__()'''
        return KLocale()
    def reparseConfiguration(self):
        '''void KLocale.reparseConfiguration()'''
    def setCountryDivisionCode(self, countryDivision):
        '''bool KLocale.setCountryDivisionCode(QString countryDivision)'''
        return bool()
    def installedLanguages(self):
        '''QStringList KLocale.installedLanguages()'''
        return QStringList()
    def countryDivisionCode(self):
        '''QString KLocale.countryDivisionCode()'''
        return QString()
    def weekNumberSystem(self):
        '''KLocale.WeekNumberSystem KLocale.weekNumberSystem()'''
        return KLocale.WeekNumberSystem()
    def setWeekNumberSystem(self, weekNumberSystem):
        '''void KLocale.setWeekNumberSystem(KLocale.WeekNumberSystem weekNumberSystem)'''
    def setCalendarSystem(self, calendarSystem):
        '''void KLocale.setCalendarSystem(KLocale.CalendarSystem calendarSystem)'''
    def calendarSystem(self):
        '''KLocale.CalendarSystem KLocale.calendarSystem()'''
        return KLocale.CalendarSystem()
    def dayPeriodText(self, time, format = None):
        '''QString KLocale.dayPeriodText(QTime time, KLocale.DateTimeComponentFormat format = KLocale.DefaultComponentFormat)'''
        return QString()
    def translateRawFrom(self, catname, msg, lang, trans):
        '''void KLocale.translateRawFrom(str catname, str msg, QString lang, QString trans)'''
    def translateRawFrom(self, catname, ctxt, msg, lang, trans):
        '''void KLocale.translateRawFrom(str catname, str ctxt, str msg, QString lang, QString trans)'''
    def translateRawFrom(self, catname, singular, plural, n, lang, trans):
        '''void KLocale.translateRawFrom(str catname, str singular, str plural, int n, QString lang, QString trans)'''
    def translateRawFrom(self, catname, ctxt, singular, plural, n, lang, trans):
        '''void KLocale.translateRawFrom(str catname, str ctxt, str singular, str plural, int n, QString lang, QString trans)'''
    def defaultCurrencyCode(self):
        '''static QString KLocale.defaultCurrencyCode()'''
        return QString()
    def setCurrencyCode(self, newCurrencyCode):
        '''void KLocale.setCurrencyCode(QString newCurrencyCode)'''
    def setMonetaryDecimalPlaces(self, digits):
        '''void KLocale.setMonetaryDecimalPlaces(int digits)'''
    def setDecimalPlaces(self, digits):
        '''void KLocale.setDecimalPlaces(int digits)'''
    def currencyCodeList(self):
        '''QStringList KLocale.currencyCodeList()'''
        return QStringList()
    def monetaryDecimalPlaces(self):
        '''int KLocale.monetaryDecimalPlaces()'''
        return int()
    def decimalPlaces(self):
        '''int KLocale.decimalPlaces()'''
        return int()
    def currency(self):
        '''KCurrencyCode KLocale.currency()'''
        return KCurrencyCode()
    def currencyCode(self):
        '''QString KLocale.currencyCode()'''
        return QString()
    def readLocaleTime(self, str, ok, options = None, processing = None):
        '''QTime KLocale.readLocaleTime(QString str, bool ok, KLocale.TimeFormatOptions options = KLocale.TimeDefault, KLocale.TimeProcessingOptions processing = KLocale.ProcessNonStrict)'''
        return QTime()
    def formatLocaleTime(self, pTime, options = None):
        '''QString KLocale.formatLocaleTime(QTime pTime, KLocale.TimeFormatOptions options = KLocale.TimeDefault)'''
        return QString()
    def setBinaryUnitDialect(self, newDialect):
        '''void KLocale.setBinaryUnitDialect(KLocale.BinaryUnitDialect newDialect)'''
    def binaryUnitDialect(self):
        '''KLocale.BinaryUnitDialect KLocale.binaryUnitDialect()'''
        return KLocale.BinaryUnitDialect()
    def convertDigits(self, str, digitSet, ignoreContext = False):
        '''QString KLocale.convertDigits(QString str, KLocale.DigitSet digitSet, bool ignoreContext = False)'''
        return QString()
    def removeAcceleratorMarker(self, label):
        '''QString KLocale.removeAcceleratorMarker(QString label)'''
        return QString()
    def localizedFilePath(self, filePath):
        '''QString KLocale.localizedFilePath(QString filePath)'''
        return QString()
    def setLanguage(self, language, config):
        '''bool KLocale.setLanguage(QString language, KConfig config)'''
        return bool()
    def setLanguage(self, languages):
        '''bool KLocale.setLanguage(QStringList languages)'''
        return bool()
    def setCountry(self, country, config):
        '''bool KLocale.setCountry(QString country, KConfig config)'''
        return bool()
    def copyCatalogsTo(self, locale):
        '''void KLocale.copyCatalogsTo(KLocale locale)'''
    def isApplicationTranslatedInto(self, language):
        '''bool KLocale.isApplicationTranslatedInto(QString language)'''
        return bool()
    def useTranscript(self):
        '''bool KLocale.useTranscript()'''
        return bool()
    def defaultCountry(self):
        '''static QString KLocale.defaultCountry()'''
        return QString()
    def defaultLanguage(self):
        '''static QString KLocale.defaultLanguage()'''
        return QString()
    def langLookup(self, fname, rtype = html):
        '''static QString KLocale.langLookup(QString fname, str rtype = html)'''
        return QString()
    def setMainCatalog(self, catalog):
        '''static void KLocale.setMainCatalog(str catalog)'''
    def splitLocale(self, locale, language, country, modifier, charset):
        '''static void KLocale.splitLocale(QString locale, QString language, QString country, QString modifier, QString charset)'''
    def countryCodeToName(self, country):
        '''QString KLocale.countryCodeToName(QString country)'''
        return QString()
    def allCountriesList(self):
        '''QStringList KLocale.allCountriesList()'''
        return QStringList()
    def languageCodeToName(self, language):
        '''QString KLocale.languageCodeToName(QString language)'''
        return QString()
    def allLanguagesList(self):
        '''QStringList KLocale.allLanguagesList()'''
        return QStringList()
    def translateQt(self, context, sourceText, comment):
        '''QString KLocale.translateQt(str context, str sourceText, str comment)'''
        return QString()
    def setActiveCatalog(self, catalog):
        '''void KLocale.setActiveCatalog(QString catalog)'''
    def removeCatalog(self, catalog):
        '''void KLocale.removeCatalog(QString catalog)'''
    def insertCatalog(self, catalog):
        '''void KLocale.insertCatalog(QString catalog)'''
    def setMeasureSystem(self, value):
        '''void KLocale.setMeasureSystem(KLocale.MeasureSystem value)'''
    def measureSystem(self):
        '''KLocale.MeasureSystem KLocale.measureSystem()'''
        return KLocale.MeasureSystem()
    def setPageSize(self, paperFormat):
        '''void KLocale.setPageSize(int paperFormat)'''
    def pageSize(self):
        '''int KLocale.pageSize()'''
        return int()
    def setMonetaryDigitSet(self, digitSet):
        '''void KLocale.setMonetaryDigitSet(KLocale.DigitSet digitSet)'''
    def setCurrencySymbol(self, symbol):
        '''void KLocale.setCurrencySymbol(QString symbol)'''
    def setMonetaryDecimalSymbol(self, symbol):
        '''void KLocale.setMonetaryDecimalSymbol(QString symbol)'''
    def setMonetaryThousandsSeparator(self, separator):
        '''void KLocale.setMonetaryThousandsSeparator(QString separator)'''
    def setFracDigits(self, digits):
        '''void KLocale.setFracDigits(int digits)'''
    def setNegativePrefixCurrencySymbol(self, prefix):
        '''void KLocale.setNegativePrefixCurrencySymbol(bool prefix)'''
    def setPositivePrefixCurrencySymbol(self, prefix):
        '''void KLocale.setPositivePrefixCurrencySymbol(bool prefix)'''
    def setNegativeMonetarySignPosition(self, signpos):
        '''void KLocale.setNegativeMonetarySignPosition(KLocale.SignPosition signpos)'''
    def setPositiveMonetarySignPosition(self, signpos):
        '''void KLocale.setPositiveMonetarySignPosition(KLocale.SignPosition signpos)'''
    def setDigitSet(self, digitSet):
        '''void KLocale.setDigitSet(KLocale.DigitSet digitSet)'''
    def setNegativeSign(self, sign):
        '''void KLocale.setNegativeSign(QString sign)'''
    def setPositiveSign(self, sign):
        '''void KLocale.setPositiveSign(QString sign)'''
    def setThousandsSeparator(self, separator):
        '''void KLocale.setThousandsSeparator(QString separator)'''
    def setDecimalSymbol(self, symbol):
        '''void KLocale.setDecimalSymbol(QString symbol)'''
    def timeFormat(self):
        '''QString KLocale.timeFormat()'''
        return QString()
    def dateFormatShort(self):
        '''QString KLocale.dateFormatShort()'''
        return QString()
    def dateFormat(self):
        '''QString KLocale.dateFormat()'''
        return QString()
    def setWeekDayOfPray(self, day):
        '''void KLocale.setWeekDayOfPray(int day)'''
    def setWorkingWeekEndDay(self, day):
        '''void KLocale.setWorkingWeekEndDay(int day)'''
    def setWorkingWeekStartDay(self, day):
        '''void KLocale.setWorkingWeekStartDay(int day)'''
    def setWeekStartDay(self, day):
        '''void KLocale.setWeekStartDay(int day)'''
    def setDateTimeDigitSet(self, digitSet):
        '''void KLocale.setDateTimeDigitSet(KLocale.DigitSet digitSet)'''
    def setTimeFormat(self, format):
        '''void KLocale.setTimeFormat(QString format)'''
    def setDateMonthNamePossessive(self, possessive):
        '''void KLocale.setDateMonthNamePossessive(bool possessive)'''
    def setDateFormatShort(self, format):
        '''void KLocale.setDateFormatShort(QString format)'''
    def setDateFormat(self, format):
        '''void KLocale.setDateFormat(QString format)'''
    def fileEncodingMib(self):
        '''int KLocale.fileEncodingMib()'''
        return int()
    def codecForEncoding(self):
        '''QTextCodec KLocale.codecForEncoding()'''
        return QTextCodec()
    def encodingMib(self):
        '''int KLocale.encodingMib()'''
        return int()
    def encoding(self):
        '''QByteArray KLocale.encoding()'''
        return QByteArray()
    def languageList(self):
        '''QStringList KLocale.languageList()'''
        return QStringList()
    def country(self):
        '''QString KLocale.country()'''
        return QString()
    def language(self):
        '''QString KLocale.language()'''
        return QString()
    def readTime(self, str, ok):
        '''QTime KLocale.readTime(QString str, bool ok)'''
        return QTime()
    def readTime(self, str, flags, ok):
        '''QTime KLocale.readTime(QString str, KLocale.ReadTimeFlags flags, bool ok)'''
        return QTime()
    def readDate(self, str, ok):
        '''QDate KLocale.readDate(QString str, bool ok)'''
        return QDate()
    def readDate(self, intstr, fmt, ok):
        '''QDate KLocale.readDate(QString intstr, QString fmt, bool ok)'''
        return QDate()
    def readDate(self, str, flags, ok):
        '''QDate KLocale.readDate(QString str, KLocale.ReadDateFlags flags, bool ok)'''
        return QDate()
    def readNumber(self, numStr, ok):
        '''float KLocale.readNumber(QString numStr, bool ok)'''
        return float()
    def readMoney(self, numStr, ok):
        '''float KLocale.readMoney(QString numStr, bool ok)'''
        return float()
    def setCalendar(self, calendarType):
        '''void KLocale.setCalendar(QString calendarType)'''
    def calendarType(self):
        '''QString KLocale.calendarType()'''
        return QString()
    def calendar(self):
        '''KCalendarSystem KLocale.calendar()'''
        return KCalendarSystem()
    def weekDayOfPray(self):
        '''int KLocale.weekDayOfPray()'''
        return int()
    def workingWeekEndDay(self):
        '''int KLocale.workingWeekEndDay()'''
        return int()
    def workingWeekStartDay(self):
        '''int KLocale.workingWeekStartDay()'''
        return int()
    def weekStartDay(self):
        '''int KLocale.weekStartDay()'''
        return int()
    def use12Clock(self):
        '''bool KLocale.use12Clock()'''
        return bool()
    def dateTimeDigitSet(self):
        '''KLocale.DigitSet KLocale.dateTimeDigitSet()'''
        return KLocale.DigitSet()
    def formatTime(self, pTime, includeSecs = False, isDuration = False):
        '''QString KLocale.formatTime(QTime pTime, bool includeSecs = False, bool isDuration = False)'''
        return QString()
    def dateMonthNamePossessive(self):
        '''bool KLocale.dateMonthNamePossessive()'''
        return bool()
    def formatDateTime(self, dateTime, format = None, includeSecs = False):
        '''QString KLocale.formatDateTime(QDateTime dateTime, KLocale.DateFormat format = KLocale.ShortDate, bool includeSecs = False)'''
        return QString()
    def formatDateTime(self, dateTime, format = None, options = 0):
        '''QString KLocale.formatDateTime(KDateTime dateTime, KLocale.DateFormat format = KLocale.ShortDate, KLocale.DateTimeFormatOptions options = 0)'''
        return QString()
    def formatDate(self, date, format = None):
        '''QString KLocale.formatDate(QDate date, KLocale.DateFormat format = KLocale.LongDate)'''
        return QString()
    def nounDeclension(self):
        '''bool KLocale.nounDeclension()'''
        return bool()
    def prettyFormatDuration(self, mSec):
        '''QString KLocale.prettyFormatDuration(int mSec)'''
        return QString()
    def formatDuration(self, mSec):
        '''QString KLocale.formatDuration(int mSec)'''
        return QString()
    def formatByteSize(self, size):
        '''QString KLocale.formatByteSize(float size)'''
        return QString()
    def formatByteSize(self, size, precision, dialect = None, specificUnit = None):
        '''QString KLocale.formatByteSize(float size, int precision, KLocale.BinaryUnitDialect dialect = KLocale.DefaultBinaryDialect, KLocale.BinarySizeUnits specificUnit = KLocale.DefaultBinaryUnits)'''
        return QString()
    def formatLong(self, num):
        '''QString KLocale.formatLong(int num)'''
        return QString()
    def formatNumber(self, num, precision = None):
        '''QString KLocale.formatNumber(float num, int precision = -1)'''
        return QString()
    def formatNumber(self, numStr, round = True, precision = 2):
        '''QString KLocale.formatNumber(QString numStr, bool round = True, int precision = 2)'''
        return QString()
    def formatMoney(self, num, currency = QString(), precision = None):
        '''QString KLocale.formatMoney(float num, QString currency = QString(), int precision = -1)'''
        return QString()
    def monetaryDigitSet(self):
        '''KLocale.DigitSet KLocale.monetaryDigitSet()'''
        return KLocale.DigitSet()
    def negativeMonetarySignPosition(self):
        '''KLocale.SignPosition KLocale.negativeMonetarySignPosition()'''
        return KLocale.SignPosition()
    def positiveMonetarySignPosition(self):
        '''KLocale.SignPosition KLocale.positiveMonetarySignPosition()'''
        return KLocale.SignPosition()
    def negativePrefixCurrencySymbol(self):
        '''bool KLocale.negativePrefixCurrencySymbol()'''
        return bool()
    def positivePrefixCurrencySymbol(self):
        '''bool KLocale.positivePrefixCurrencySymbol()'''
        return bool()
    def fracDigits(self):
        '''int KLocale.fracDigits()'''
        return int()
    def negativeSign(self):
        '''QString KLocale.negativeSign()'''
        return QString()
    def positiveSign(self):
        '''QString KLocale.positiveSign()'''
        return QString()
    def monetaryThousandsSeparator(self):
        '''QString KLocale.monetaryThousandsSeparator()'''
        return QString()
    def monetaryDecimalSymbol(self):
        '''QString KLocale.monetaryDecimalSymbol()'''
        return QString()
    def currencySymbol(self):
        '''QString KLocale.currencySymbol()'''
        return QString()
    def digitSet(self):
        '''KLocale.DigitSet KLocale.digitSet()'''
        return KLocale.DigitSet()
    def thousandsSeparator(self):
        '''QString KLocale.thousandsSeparator()'''
        return QString()
    def decimalSymbol(self):
        '''QString KLocale.decimalSymbol()'''
        return QString()
    def allDigitSetsList(self):
        '''list-of-KLocale.DigitSet KLocale.allDigitSetsList()'''
        return [KLocale.DigitSet()]
    def digitSetToName(self, digitSet, withDigits = False):
        '''QString KLocale.digitSetToName(KLocale.DigitSet digitSet, bool withDigits = False)'''
        return QString()
    def setEncoding(self, mibEnum):
        '''bool KLocale.setEncoding(int mibEnum)'''
        return bool()
    def translateRaw(self, msg, lang, trans):
        '''void KLocale.translateRaw(str msg, QString lang, QString trans)'''
    def translateRaw(self, ctxt, msg, lang, trans):
        '''void KLocale.translateRaw(str ctxt, str msg, QString lang, QString trans)'''
    def translateRaw(self, singular, plural, n, lang, trans):
        '''void KLocale.translateRaw(str singular, str plural, int n, QString lang, QString trans)'''
    def translateRaw(self, ctxt, singular, plural, n, lang, trans):
        '''void KLocale.translateRaw(str ctxt, str singular, str plural, int n, QString lang, QString trans)'''
    class DateTimeFormatOptions():
        """"""
        def __init__(self):
            '''KLocale.DateTimeFormatOptions KLocale.DateTimeFormatOptions.__init__()'''
            return KLocale.DateTimeFormatOptions()
        def __init__(self):
            '''int KLocale.DateTimeFormatOptions.__init__()'''
            return int()
        def __init__(self):
            '''void KLocale.DateTimeFormatOptions.__init__()'''
        def __bool__(self):
            '''int KLocale.DateTimeFormatOptions.__bool__()'''
            return int()
        def __ne__(self, f):
            '''bool KLocale.DateTimeFormatOptions.__ne__(KLocale.DateTimeFormatOptions f)'''
            return bool()
        def __eq__(self, f):
            '''bool KLocale.DateTimeFormatOptions.__eq__(KLocale.DateTimeFormatOptions f)'''
            return bool()
        def __invert__(self):
            '''KLocale.DateTimeFormatOptions KLocale.DateTimeFormatOptions.__invert__()'''
            return KLocale.DateTimeFormatOptions()
        def __and__(self, mask):
            '''KLocale.DateTimeFormatOptions KLocale.DateTimeFormatOptions.__and__(int mask)'''
            return KLocale.DateTimeFormatOptions()
        def __xor__(self, f):
            '''KLocale.DateTimeFormatOptions KLocale.DateTimeFormatOptions.__xor__(KLocale.DateTimeFormatOptions f)'''
            return KLocale.DateTimeFormatOptions()
        def __xor__(self, f):
            '''KLocale.DateTimeFormatOptions KLocale.DateTimeFormatOptions.__xor__(int f)'''
            return KLocale.DateTimeFormatOptions()
        def __or__(self, f):
            '''KLocale.DateTimeFormatOptions KLocale.DateTimeFormatOptions.__or__(KLocale.DateTimeFormatOptions f)'''
            return KLocale.DateTimeFormatOptions()
        def __or__(self, f):
            '''KLocale.DateTimeFormatOptions KLocale.DateTimeFormatOptions.__or__(int f)'''
            return KLocale.DateTimeFormatOptions()
        def __int__(self):
            '''int KLocale.DateTimeFormatOptions.__int__()'''
            return int()
        def __ixor__(self, f):
            '''KLocale.DateTimeFormatOptions KLocale.DateTimeFormatOptions.__ixor__(KLocale.DateTimeFormatOptions f)'''
            return KLocale.DateTimeFormatOptions()
        def __ior__(self, f):
            '''KLocale.DateTimeFormatOptions KLocale.DateTimeFormatOptions.__ior__(KLocale.DateTimeFormatOptions f)'''
            return KLocale.DateTimeFormatOptions()
        def __iand__(self, mask):
            '''KLocale.DateTimeFormatOptions KLocale.DateTimeFormatOptions.__iand__(int mask)'''
            return KLocale.DateTimeFormatOptions()
    class TimeProcessingOptions():
        """"""
        def __init__(self):
            '''KLocale.TimeProcessingOptions KLocale.TimeProcessingOptions.__init__()'''
            return KLocale.TimeProcessingOptions()
        def __init__(self):
            '''int KLocale.TimeProcessingOptions.__init__()'''
            return int()
        def __init__(self):
            '''void KLocale.TimeProcessingOptions.__init__()'''
        def __bool__(self):
            '''int KLocale.TimeProcessingOptions.__bool__()'''
            return int()
        def __ne__(self, f):
            '''bool KLocale.TimeProcessingOptions.__ne__(KLocale.TimeProcessingOptions f)'''
            return bool()
        def __eq__(self, f):
            '''bool KLocale.TimeProcessingOptions.__eq__(KLocale.TimeProcessingOptions f)'''
            return bool()
        def __invert__(self):
            '''KLocale.TimeProcessingOptions KLocale.TimeProcessingOptions.__invert__()'''
            return KLocale.TimeProcessingOptions()
        def __and__(self, mask):
            '''KLocale.TimeProcessingOptions KLocale.TimeProcessingOptions.__and__(int mask)'''
            return KLocale.TimeProcessingOptions()
        def __xor__(self, f):
            '''KLocale.TimeProcessingOptions KLocale.TimeProcessingOptions.__xor__(KLocale.TimeProcessingOptions f)'''
            return KLocale.TimeProcessingOptions()
        def __xor__(self, f):
            '''KLocale.TimeProcessingOptions KLocale.TimeProcessingOptions.__xor__(int f)'''
            return KLocale.TimeProcessingOptions()
        def __or__(self, f):
            '''KLocale.TimeProcessingOptions KLocale.TimeProcessingOptions.__or__(KLocale.TimeProcessingOptions f)'''
            return KLocale.TimeProcessingOptions()
        def __or__(self, f):
            '''KLocale.TimeProcessingOptions KLocale.TimeProcessingOptions.__or__(int f)'''
            return KLocale.TimeProcessingOptions()
        def __int__(self):
            '''int KLocale.TimeProcessingOptions.__int__()'''
            return int()
        def __ixor__(self, f):
            '''KLocale.TimeProcessingOptions KLocale.TimeProcessingOptions.__ixor__(KLocale.TimeProcessingOptions f)'''
            return KLocale.TimeProcessingOptions()
        def __ior__(self, f):
            '''KLocale.TimeProcessingOptions KLocale.TimeProcessingOptions.__ior__(KLocale.TimeProcessingOptions f)'''
            return KLocale.TimeProcessingOptions()
        def __iand__(self, mask):
            '''KLocale.TimeProcessingOptions KLocale.TimeProcessingOptions.__iand__(int mask)'''
            return KLocale.TimeProcessingOptions()
    class DateTimeComponents():
        """"""
        def __init__(self):
            '''KLocale.DateTimeComponents KLocale.DateTimeComponents.__init__()'''
            return KLocale.DateTimeComponents()
        def __init__(self):
            '''int KLocale.DateTimeComponents.__init__()'''
            return int()
        def __init__(self):
            '''void KLocale.DateTimeComponents.__init__()'''
        def __bool__(self):
            '''int KLocale.DateTimeComponents.__bool__()'''
            return int()
        def __ne__(self, f):
            '''bool KLocale.DateTimeComponents.__ne__(KLocale.DateTimeComponents f)'''
            return bool()
        def __eq__(self, f):
            '''bool KLocale.DateTimeComponents.__eq__(KLocale.DateTimeComponents f)'''
            return bool()
        def __invert__(self):
            '''KLocale.DateTimeComponents KLocale.DateTimeComponents.__invert__()'''
            return KLocale.DateTimeComponents()
        def __and__(self, mask):
            '''KLocale.DateTimeComponents KLocale.DateTimeComponents.__and__(int mask)'''
            return KLocale.DateTimeComponents()
        def __xor__(self, f):
            '''KLocale.DateTimeComponents KLocale.DateTimeComponents.__xor__(KLocale.DateTimeComponents f)'''
            return KLocale.DateTimeComponents()
        def __xor__(self, f):
            '''KLocale.DateTimeComponents KLocale.DateTimeComponents.__xor__(int f)'''
            return KLocale.DateTimeComponents()
        def __or__(self, f):
            '''KLocale.DateTimeComponents KLocale.DateTimeComponents.__or__(KLocale.DateTimeComponents f)'''
            return KLocale.DateTimeComponents()
        def __or__(self, f):
            '''KLocale.DateTimeComponents KLocale.DateTimeComponents.__or__(int f)'''
            return KLocale.DateTimeComponents()
        def __int__(self):
            '''int KLocale.DateTimeComponents.__int__()'''
            return int()
        def __ixor__(self, f):
            '''KLocale.DateTimeComponents KLocale.DateTimeComponents.__ixor__(KLocale.DateTimeComponents f)'''
            return KLocale.DateTimeComponents()
        def __ior__(self, f):
            '''KLocale.DateTimeComponents KLocale.DateTimeComponents.__ior__(KLocale.DateTimeComponents f)'''
            return KLocale.DateTimeComponents()
        def __iand__(self, mask):
            '''KLocale.DateTimeComponents KLocale.DateTimeComponents.__iand__(int mask)'''
            return KLocale.DateTimeComponents()
    class TimeFormatOptions():
        """"""
        def __init__(self):
            '''KLocale.TimeFormatOptions KLocale.TimeFormatOptions.__init__()'''
            return KLocale.TimeFormatOptions()
        def __init__(self):
            '''int KLocale.TimeFormatOptions.__init__()'''
            return int()
        def __init__(self):
            '''void KLocale.TimeFormatOptions.__init__()'''
        def __bool__(self):
            '''int KLocale.TimeFormatOptions.__bool__()'''
            return int()
        def __ne__(self, f):
            '''bool KLocale.TimeFormatOptions.__ne__(KLocale.TimeFormatOptions f)'''
            return bool()
        def __eq__(self, f):
            '''bool KLocale.TimeFormatOptions.__eq__(KLocale.TimeFormatOptions f)'''
            return bool()
        def __invert__(self):
            '''KLocale.TimeFormatOptions KLocale.TimeFormatOptions.__invert__()'''
            return KLocale.TimeFormatOptions()
        def __and__(self, mask):
            '''KLocale.TimeFormatOptions KLocale.TimeFormatOptions.__and__(int mask)'''
            return KLocale.TimeFormatOptions()
        def __xor__(self, f):
            '''KLocale.TimeFormatOptions KLocale.TimeFormatOptions.__xor__(KLocale.TimeFormatOptions f)'''
            return KLocale.TimeFormatOptions()
        def __xor__(self, f):
            '''KLocale.TimeFormatOptions KLocale.TimeFormatOptions.__xor__(int f)'''
            return KLocale.TimeFormatOptions()
        def __or__(self, f):
            '''KLocale.TimeFormatOptions KLocale.TimeFormatOptions.__or__(KLocale.TimeFormatOptions f)'''
            return KLocale.TimeFormatOptions()
        def __or__(self, f):
            '''KLocale.TimeFormatOptions KLocale.TimeFormatOptions.__or__(int f)'''
            return KLocale.TimeFormatOptions()
        def __int__(self):
            '''int KLocale.TimeFormatOptions.__int__()'''
            return int()
        def __ixor__(self, f):
            '''KLocale.TimeFormatOptions KLocale.TimeFormatOptions.__ixor__(KLocale.TimeFormatOptions f)'''
            return KLocale.TimeFormatOptions()
        def __ior__(self, f):
            '''KLocale.TimeFormatOptions KLocale.TimeFormatOptions.__ior__(KLocale.TimeFormatOptions f)'''
            return KLocale.TimeFormatOptions()
        def __iand__(self, mask):
            '''KLocale.TimeFormatOptions KLocale.TimeFormatOptions.__iand__(int mask)'''
            return KLocale.TimeFormatOptions()


class KLocalizedDate():
    """"""
    def __init__(self, date = QDate(), calendar = None):
        '''void KLocalizedDate.__init__(QDate date = QDate(), KCalendarSystem calendar = None)'''
    def __init__(self, year, month, day, calendar = None):
        '''void KLocalizedDate.__init__(int year, int month, int day, KCalendarSystem calendar = None)'''
    def __init__(self, rhs):
        '''void KLocalizedDate.__init__(KLocalizedDate rhs)'''
    def __ge__(self, other):
        '''bool KLocalizedDate.__ge__(KLocalizedDate other)'''
        return bool()
    def __ge__(self, other):
        '''bool KLocalizedDate.__ge__(QDate other)'''
        return bool()
    def __gt__(self, other):
        '''bool KLocalizedDate.__gt__(KLocalizedDate other)'''
        return bool()
    def __gt__(self, other):
        '''bool KLocalizedDate.__gt__(QDate other)'''
        return bool()
    def __le__(self, other):
        '''bool KLocalizedDate.__le__(KLocalizedDate other)'''
        return bool()
    def __le__(self, other):
        '''bool KLocalizedDate.__le__(QDate other)'''
        return bool()
    def __lt__(self, other):
        '''bool KLocalizedDate.__lt__(KLocalizedDate other)'''
        return bool()
    def __lt__(self, other):
        '''bool KLocalizedDate.__lt__(QDate other)'''
        return bool()
    def __ne__(self, other):
        '''bool KLocalizedDate.__ne__(KLocalizedDate other)'''
        return bool()
    def __ne__(self, other):
        '''bool KLocalizedDate.__ne__(QDate other)'''
        return bool()
    def __eq__(self, other):
        '''bool KLocalizedDate.__eq__(KLocalizedDate other)'''
        return bool()
    def __eq__(self, other):
        '''bool KLocalizedDate.__eq__(QDate other)'''
        return bool()
    def lastDayOfMonth(self):
        '''KLocalizedDate KLocalizedDate.lastDayOfMonth()'''
        return KLocalizedDate()
    def firstDayOfMonth(self):
        '''KLocalizedDate KLocalizedDate.firstDayOfMonth()'''
        return KLocalizedDate()
    def lastDayOfYear(self):
        '''KLocalizedDate KLocalizedDate.lastDayOfYear()'''
        return KLocalizedDate()
    def firstDayOfYear(self):
        '''KLocalizedDate KLocalizedDate.firstDayOfYear()'''
        return KLocalizedDate()
    def daysDifference(self, toDate):
        '''int KLocalizedDate.daysDifference(KLocalizedDate toDate)'''
        return int()
    def daysDifference(self, toDate):
        '''int KLocalizedDate.daysDifference(QDate toDate)'''
        return int()
    def monthsDifference(self, toDate):
        '''int KLocalizedDate.monthsDifference(KLocalizedDate toDate)'''
        return int()
    def monthsDifference(self, toDate):
        '''int KLocalizedDate.monthsDifference(QDate toDate)'''
        return int()
    def yearsDifference(self, toDate):
        '''int KLocalizedDate.yearsDifference(KLocalizedDate toDate)'''
        return int()
    def yearsDifference(self, toDate):
        '''int KLocalizedDate.yearsDifference(QDate toDate)'''
        return int()
    def dateDifference(self, toDate, yearsDiff, monthsDiff, daysDiff, direction):
        '''void KLocalizedDate.dateDifference(KLocalizedDate toDate, int yearsDiff, int monthsDiff, int daysDiff, int direction)'''
    def dateDifference(self, toDate, yearsDiff, monthsDiff, daysDiff, direction):
        '''void KLocalizedDate.dateDifference(QDate toDate, int yearsDiff, int monthsDiff, int daysDiff, int direction)'''
    def addDaysTo(self, days):
        '''bool KLocalizedDate.addDaysTo(int days)'''
        return bool()
    def addDays(self, days):
        '''KLocalizedDate KLocalizedDate.addDays(int days)'''
        return KLocalizedDate()
    def addMonthsTo(self, months):
        '''bool KLocalizedDate.addMonthsTo(int months)'''
        return bool()
    def addMonths(self, months):
        '''KLocalizedDate KLocalizedDate.addMonths(int months)'''
        return KLocalizedDate()
    def addYearsTo(self, years):
        '''bool KLocalizedDate.addYearsTo(int years)'''
        return bool()
    def addYears(self, years):
        '''KLocalizedDate KLocalizedDate.addYears(int years)'''
        return KLocalizedDate()
    def readDate(self, dateString, parseMode = None, calendar = None):
        '''static KLocalizedDate KLocalizedDate.readDate(QString dateString, KLocale.DateTimeParseMode parseMode = KLocale.LiberalParsing, KCalendarSystem calendar = None)'''
        return KLocalizedDate()
    def readDate(self, dateString, formatFlags, parseMode = None, calendar = None):
        '''static KLocalizedDate KLocalizedDate.readDate(QString dateString, KLocale.ReadDateFlags formatFlags, KLocale.DateTimeParseMode parseMode = KLocale.LiberalParsing, KCalendarSystem calendar = None)'''
        return KLocalizedDate()
    def readDate(self, dateString, dateFormat, parseMode = None, formatStandard = None, calendar = None):
        '''static KLocalizedDate KLocalizedDate.readDate(QString dateString, QString dateFormat, KLocale.DateTimeParseMode parseMode = KLocale.LiberalParsing, KLocale.DateTimeFormatStandard formatStandard = KLocale.KdeFormat, KCalendarSystem calendar = None)'''
        return KLocalizedDate()
    def formatDate(self, dateFormat = None):
        '''QString KLocalizedDate.formatDate(KLocale.DateFormat dateFormat = KLocale.LongDate)'''
        return QString()
    def formatDate(self, formatString, formatStandard = None):
        '''QString KLocalizedDate.formatDate(QString formatString, KLocale.DateTimeFormatStandard formatStandard = KLocale.KdeFormat)'''
        return QString()
    def formatDate(self, component, format = None, weekNumberSystem = None):
        '''QString KLocalizedDate.formatDate(KLocale.DateTimeComponent component, KLocale.DateTimeComponentFormat format = KLocale.DefaultComponentFormat, KLocale.WeekNumberSystem weekNumberSystem = KLocale.DefaultWeekNumber)'''
        return QString()
    def isLeapYear(self):
        '''bool KLocalizedDate.isLeapYear()'''
        return bool()
    def daysInWeek(self):
        '''int KLocalizedDate.daysInWeek()'''
        return int()
    def daysInMonth(self):
        '''int KLocalizedDate.daysInMonth()'''
        return int()
    def daysInYear(self):
        '''int KLocalizedDate.daysInYear()'''
        return int()
    def weeksInYear(self):
        '''int KLocalizedDate.weeksInYear()'''
        return int()
    def weeksInYear(self, weekNumberSystem):
        '''int KLocalizedDate.weeksInYear(KLocale.WeekNumberSystem weekNumberSystem)'''
        return int()
    def monthsInYear(self):
        '''int KLocalizedDate.monthsInYear()'''
        return int()
    def week(self, yearNum):
        '''int KLocalizedDate.week(int yearNum)'''
        return int()
    def week(self, weekNumberSystem, yearNum):
        '''int KLocalizedDate.week(KLocale.WeekNumberSystem weekNumberSystem, int yearNum)'''
        return int()
    def dayOfWeek(self):
        '''int KLocalizedDate.dayOfWeek()'''
        return int()
    def dayOfYear(self):
        '''int KLocalizedDate.dayOfYear()'''
        return int()
    def yearInEra(self):
        '''int KLocalizedDate.yearInEra()'''
        return int()
    def eraYear(self):
        '''QString KLocalizedDate.eraYear()'''
        return QString()
    def eraName(self):
        '''QString KLocalizedDate.eraName()'''
        return QString()
    def day(self):
        '''int KLocalizedDate.day()'''
        return int()
    def month(self):
        '''int KLocalizedDate.month()'''
        return int()
    def year(self):
        '''int KLocalizedDate.year()'''
        return int()
    def getDate(self, year, month, day):
        '''void KLocalizedDate.getDate(int year, int month, int day)'''
    def date(self):
        '''QDate KLocalizedDate.date()'''
        return QDate()
    def toJulianDay(self):
        '''int KLocalizedDate.toJulianDay()'''
        return int()
    def fromJulianDay(self, jd):
        '''static KLocalizedDate KLocalizedDate.fromJulianDay(int jd)'''
        return KLocalizedDate()
    def fromDate(self, date):
        '''static KLocalizedDate KLocalizedDate.fromDate(QDate date)'''
        return KLocalizedDate()
    def currentDate(self):
        '''static KLocalizedDate KLocalizedDate.currentDate()'''
        return KLocalizedDate()
    def setCurrentDate(self):
        '''bool KLocalizedDate.setCurrentDate()'''
        return bool()
    def setDate(self, date):
        '''bool KLocalizedDate.setDate(QDate date)'''
        return bool()
    def setDate(self, year, month, day):
        '''bool KLocalizedDate.setDate(int year, int month, int day)'''
        return bool()
    def setDate(self, year, dayOfYear):
        '''bool KLocalizedDate.setDate(int year, int dayOfYear)'''
        return bool()
    def setDate(self, eraName, yearInEra, month, day):
        '''bool KLocalizedDate.setDate(QString eraName, int yearInEra, int month, int day)'''
        return bool()
    def setDate(self, weekNumberSystem, year, weekOfYear, dayOfWeek):
        '''bool KLocalizedDate.setDate(KLocale.WeekNumberSystem weekNumberSystem, int year, int weekOfYear, int dayOfWeek)'''
        return bool()
    def isValid(self):
        '''bool KLocalizedDate.isValid()'''
        return bool()
    def isNull(self):
        '''bool KLocalizedDate.isNull()'''
        return bool()
    def calendar(self):
        '''KCalendarSystem KLocalizedDate.calendar()'''
        return KCalendarSystem()
    def calendarSystem(self):
        '''KLocale.CalendarSystem KLocalizedDate.calendarSystem()'''
        return KLocale.CalendarSystem()
    def setCalendarSystem(self, calendarSystem):
        '''void KLocalizedDate.setCalendarSystem(KLocale.CalendarSystem calendarSystem)'''


class KLocalizedString():
    """"""
    def __init__(self):
        '''void KLocalizedString.__init__()'''
    def __init__(self, rhs):
        '''void KLocalizedString.__init__(KLocalizedString rhs)'''
    def inContext(self, key, text):
        '''KLocalizedString KLocalizedString.inContext(QString key, QString text)'''
        return KLocalizedString()
    def subs(self, a, fieldWidth = 0, base = 10, fillChar = None):
        '''KLocalizedString KLocalizedString.subs(int a, int fieldWidth = 0, int base = 10, QChar fillChar = QLatin1Char(' '))'''
        return KLocalizedString()
    def subs(self, a, fieldWidth = 0, fillChar = None):
        '''KLocalizedString KLocalizedString.subs(QChar a, int fieldWidth = 0, QChar fillChar = QLatin1Char(' '))'''
        return KLocalizedString()
    def subs(self, a, fieldWidth = 0, fillChar = None):
        '''KLocalizedString KLocalizedString.subs(QString a, int fieldWidth = 0, QChar fillChar = QLatin1Char(' '))'''
        return KLocalizedString()
    def isEmpty(self):
        '''bool KLocalizedString.isEmpty()'''
        return bool()
    def toString(self):
        '''QString KLocalizedString.toString()'''
        return QString()
    def toString(self, locale):
        '''QString KLocalizedString.toString(KLocale locale)'''
        return QString()
    def toString(self, catalogName):
        '''QString KLocalizedString.toString(QString catalogName)'''
        return QString()
    def toString(self, locale, catalogName):
        '''QString KLocalizedString.toString(KLocale locale, QString catalogName)'''
        return QString()


class KLocalSocket(QTcpSocket):
    """"""
    # Enum KLocalSocket.LocalSocketType
    UnixSocket = 0
    AbstractUnixSocket = 0
    UnknownLocalSocketType = 0

    def __init__(self, parent = None):
        '''void KLocalSocket.__init__(QObject parent = None)'''
    def disconnectFromHostImplementation(self):
        '''void KLocalSocket.disconnectFromHostImplementation()'''
    def connectToHostImplementation(self, hostName, port, mode):
        '''void KLocalSocket.connectToHostImplementation(QString hostName, int port, QIODevice.OpenMode mode)'''
    def peerPath(self):
        '''QString KLocalSocket.peerPath()'''
        return QString()
    def localPath(self):
        '''QString KLocalSocket.localPath()'''
        return QString()
    def localSocketType(self):
        '''KLocalSocket.LocalSocketType KLocalSocket.localSocketType()'''
        return KLocalSocket.LocalSocketType()
    def disconnectFromPath(self):
        '''void KLocalSocket.disconnectFromPath()'''
    def connectToPath(self, path, mode = None):
        '''void KLocalSocket.connectToPath(QString path, QIODevice.OpenMode mode = QIODevice.ReadWrite)'''
    def connectToPath(self, path, type, mode = None):
        '''void KLocalSocket.connectToPath(QString path, KLocalSocket.LocalSocketType type, QIODevice.OpenMode mode = QIODevice.ReadWrite)'''


class KLocalSocketServer(QObject):
    """"""
    def __init__(self, parent = None):
        '''void KLocalSocketServer.__init__(QObject parent = None)'''
    newConnection = pyqtSignal() # void newConnection() - signal
    def incomingConnection(self, handle):
        '''void KLocalSocketServer.incomingConnection(int handle)'''
    def errorString(self):
        '''QString KLocalSocketServer.errorString()'''
        return QString()
    def serverError(self):
        '''QAbstractSocket.SocketError KLocalSocketServer.serverError()'''
        return QAbstractSocket.SocketError()
    def nextPendingConnection(self):
        '''KLocalSocket KLocalSocketServer.nextPendingConnection()'''
        return KLocalSocket()
    def hasPendingConnections(self):
        '''bool KLocalSocketServer.hasPendingConnections()'''
        return bool()
    def waitForNewConnection(self, msec = 0, timedOut = None):
        '''bool KLocalSocketServer.waitForNewConnection(int msec = 0, bool timedOut)'''
        return bool()
    def localPath(self):
        '''QString KLocalSocketServer.localPath()'''
        return QString()
    def localSocketType(self):
        '''KLocalSocket.LocalSocketType KLocalSocketServer.localSocketType()'''
        return KLocalSocket.LocalSocketType()
    def maxPendingConnections(self):
        '''int KLocalSocketServer.maxPendingConnections()'''
        return int()
    def setMaxPendingConnections(self, numConnections):
        '''void KLocalSocketServer.setMaxPendingConnections(int numConnections)'''
    def isListening(self):
        '''bool KLocalSocketServer.isListening()'''
        return bool()
    def close(self):
        '''void KLocalSocketServer.close()'''
    def listen(self, path, type = None):
        '''bool KLocalSocketServer.listen(QString path, KLocalSocket.LocalSocketType type = KLocalSocket.UnixSocket)'''
        return bool()


class KLockFile():
    """"""
    # Enum KLockFile.LockFlag
    NoBlockFlag = 0
    ForceFlag = 0

    # Enum KLockFile.LockResult
    LockOK = 0
    LockFail = 0
    LockError = 0
    LockStale = 0

    def __init__(self, file, componentName = None):
        '''void KLockFile.__init__(QString file, KComponentData componentName = KGlobal.mainComponent())'''
    def getLockInfo(self, pid, hostname, appname):
        '''bool KLockFile.getLockInfo(int pid, QString hostname, QString appname)'''
        return bool()
    def setStaleTime(self, _staleTime):
        '''void KLockFile.setStaleTime(int _staleTime)'''
    def staleTime(self):
        '''int KLockFile.staleTime()'''
        return int()
    def unlock(self):
        '''void KLockFile.unlock()'''
    def isLocked(self):
        '''bool KLockFile.isLocked()'''
        return bool()
    def lock(self, flags = None):
        '''KLockFile.LockResult KLockFile.lock(KLockFile.LockFlags flags = KLockFile.LockFlags())'''
        return KLockFile.LockResult()
    class LockFlags():
        """"""
        def __init__(self):
            '''KLockFile.LockFlags KLockFile.LockFlags.__init__()'''
            return KLockFile.LockFlags()
        def __init__(self):
            '''int KLockFile.LockFlags.__init__()'''
            return int()
        def __init__(self):
            '''void KLockFile.LockFlags.__init__()'''
        def __bool__(self):
            '''int KLockFile.LockFlags.__bool__()'''
            return int()
        def __ne__(self, f):
            '''bool KLockFile.LockFlags.__ne__(KLockFile.LockFlags f)'''
            return bool()
        def __eq__(self, f):
            '''bool KLockFile.LockFlags.__eq__(KLockFile.LockFlags f)'''
            return bool()
        def __invert__(self):
            '''KLockFile.LockFlags KLockFile.LockFlags.__invert__()'''
            return KLockFile.LockFlags()
        def __and__(self, mask):
            '''KLockFile.LockFlags KLockFile.LockFlags.__and__(int mask)'''
            return KLockFile.LockFlags()
        def __xor__(self, f):
            '''KLockFile.LockFlags KLockFile.LockFlags.__xor__(KLockFile.LockFlags f)'''
            return KLockFile.LockFlags()
        def __xor__(self, f):
            '''KLockFile.LockFlags KLockFile.LockFlags.__xor__(int f)'''
            return KLockFile.LockFlags()
        def __or__(self, f):
            '''KLockFile.LockFlags KLockFile.LockFlags.__or__(KLockFile.LockFlags f)'''
            return KLockFile.LockFlags()
        def __or__(self, f):
            '''KLockFile.LockFlags KLockFile.LockFlags.__or__(int f)'''
            return KLockFile.LockFlags()
        def __int__(self):
            '''int KLockFile.LockFlags.__int__()'''
            return int()
        def __ixor__(self, f):
            '''KLockFile.LockFlags KLockFile.LockFlags.__ixor__(KLockFile.LockFlags f)'''
            return KLockFile.LockFlags()
        def __ior__(self, f):
            '''KLockFile.LockFlags KLockFile.LockFlags.__ior__(KLockFile.LockFlags f)'''
            return KLockFile.LockFlags()
        def __iand__(self, mask):
            '''KLockFile.LockFlags KLockFile.LockFlags.__iand__(int mask)'''
            return KLockFile.LockFlags()


class KMacroExpanderBase():
    """"""
    def __init__(self, c = None):
        '''void KMacroExpanderBase.__init__(QChar c = QLatin1Char('%'))'''
    def expandEscapedMacro(self, str, pos, ret):
        '''int KMacroExpanderBase.expandEscapedMacro(QString str, int pos, QStringList ret)'''
        return int()
    def expandPlainMacro(self, str, pos, ret):
        '''int KMacroExpanderBase.expandPlainMacro(QString str, int pos, QStringList ret)'''
        return int()
    def escapeChar(self):
        '''QChar KMacroExpanderBase.escapeChar()'''
        return QChar()
    def setEscapeChar(self, c):
        '''void KMacroExpanderBase.setEscapeChar(QChar c)'''
    def expandMacrosShellQuote(self, str, pos):
        '''bool KMacroExpanderBase.expandMacrosShellQuote(QString str, int pos)'''
        return bool()
    def expandMacros(self, str):
        '''void KMacroExpanderBase.expandMacros(QString str)'''


class KWordMacroExpander(KMacroExpanderBase):
    """"""
    def __init__(self, c = None):
        '''void KWordMacroExpander.__init__(QChar c = QLatin1Char('%'))'''
    def expandMacro(self, str, ret):
        '''abstract bool KWordMacroExpander.expandMacro(QString str, QStringList ret)'''
        return bool()
    def expandEscapedMacro(self, str, pos, ret):
        '''int KWordMacroExpander.expandEscapedMacro(QString str, int pos, QStringList ret)'''
        return int()
    def expandPlainMacro(self, str, pos, ret):
        '''int KWordMacroExpander.expandPlainMacro(QString str, int pos, QStringList ret)'''
        return int()


class KCharMacroExpander(KMacroExpanderBase):
    """"""
    def __init__(self, c = None):
        '''void KCharMacroExpander.__init__(QChar c = QLatin1Char('%'))'''
    def expandMacro(self, chr, ret):
        '''abstract bool KCharMacroExpander.expandMacro(QChar chr, QStringList ret)'''
        return bool()
    def expandEscapedMacro(self, str, pos, ret):
        '''int KCharMacroExpander.expandEscapedMacro(QString str, int pos, QStringList ret)'''
        return int()
    def expandPlainMacro(self, str, pos, ret):
        '''int KCharMacroExpander.expandPlainMacro(QString str, int pos, QStringList ret)'''
        return int()


class KMacroExpander():
    """"""
    def expandMacrosShellQuote(self, str, map, c = None):
        '''static QString KMacroExpander.expandMacrosShellQuote(QString str, dict-of-QChar-QString map, QChar c = QLatin1Char('%'))'''
        return QString()
    def expandMacrosShellQuote(self, str, map, c = None):
        '''static QString KMacroExpander.expandMacrosShellQuote(QString str, dict-of-QString-QString map, QChar c = QLatin1Char('%'))'''
        return QString()
    def expandMacrosShellQuote(self, str, map, c = None):
        '''static QString KMacroExpander.expandMacrosShellQuote(QString str, dict-of-QChar-QStringList map, QChar c = QLatin1Char('%'))'''
        return QString()
    def expandMacrosShellQuote(self, str, map, c = None):
        '''static QString KMacroExpander.expandMacrosShellQuote(QString str, dict-of-QString-QStringList map, QChar c = QLatin1Char('%'))'''
        return QString()
    def expandMacros(self, str, map, c = None):
        '''static QString KMacroExpander.expandMacros(QString str, dict-of-QChar-QString map, QChar c = '%')'''
        return QString()
    def expandMacros(self, str, map, c = None):
        '''static QString KMacroExpander.expandMacros(QString str, dict-of-QString-QString map, QChar c = QLatin1Char('%'))'''
        return QString()
    def expandMacros(self, str, map, c = None):
        '''static QString KMacroExpander.expandMacros(QString str, dict-of-QChar-QStringList map, QChar c = QLatin1Char('%'))'''
        return QString()
    def expandMacros(self, str, map, c = None):
        '''static QString KMacroExpander.expandMacros(QString str, dict-of-QString-QStringList map, QChar c = QLatin1Char('%'))'''
        return QString()


class KMessage():
    """"""
    # Enum KMessage.MessageType
    Error = 0
    Information = 0
    Warning = 0
    Sorry = 0
    Fatal = 0

    def setMessageHandler(self, handler):
        '''static void KMessage.setMessageHandler(KMessageHandler handler)'''
    def message(self, messageType, text, caption = QString()):
        '''static void KMessage.message(KMessage.MessageType messageType, QString text, QString caption = QString())'''


class KMessageHandler():
    """"""
    def __init__(self):
        '''void KMessageHandler.__init__()'''
    def __init__(self):
        '''KMessageHandler KMessageHandler.__init__()'''
        return KMessageHandler()
    def message(self, type, text, caption):
        '''abstract void KMessageHandler.message(KMessage.MessageType type, QString text, QString caption)'''


class KSycocaEntry():
    """"""
    def __init__(self):
        '''void KSycocaEntry.__init__()'''
    def save(self, s):
        '''void KSycocaEntry.save(QDataStream s)'''
    def offset(self):
        '''int KSycocaEntry.offset()'''
        return int()
    def isSeparator(self):
        '''bool KSycocaEntry.isSeparator()'''
        return bool()
    def setDeleted(self, deleted):
        '''void KSycocaEntry.setDeleted(bool deleted)'''
    def propertyNames(self):
        '''QStringList KSycocaEntry.propertyNames()'''
        return QStringList()
    def property(self, name):
        '''QVariant KSycocaEntry.property(QString name)'''
        return QVariant()
    def isDeleted(self):
        '''bool KSycocaEntry.isDeleted()'''
        return bool()
    def isValid(self):
        '''bool KSycocaEntry.isValid()'''
        return bool()
    def storageId(self):
        '''QString KSycocaEntry.storageId()'''
        return QString()
    def entryPath(self):
        '''QString KSycocaEntry.entryPath()'''
        return QString()
    def name(self):
        '''QString KSycocaEntry.name()'''
        return QString()
    def read(self, s, str):
        '''static void KSycocaEntry.read(QDataStream s, QString str)'''
    def read(self, s, list):
        '''static void KSycocaEntry.read(QDataStream s, QStringList list)'''
    def sycocaType(self):
        '''KSycocaType KSycocaEntry.sycocaType()'''
        return KSycocaType()
    def isType(self, t):
        '''bool KSycocaEntry.isType(KSycocaType t)'''
        return bool()


class KServiceType(KSycocaEntry):
    """"""
    def __init__(self, config):
        '''void KServiceType.__init__(KDesktopFile config)'''
    def __init__(self, _str, offset):
        '''void KServiceType.__init__(QDataStream _str, int offset)'''
    def allServiceTypes(self):
        '''static unknown-type KServiceType.allServiceTypes()'''
        return unknown-type()
    def serviceType(self, _name):
        '''static unknown-type KServiceType.serviceType(QString _name)'''
        return unknown-type()
    def serviceOffersOffset(self):
        '''int KServiceType.serviceOffersOffset()'''
        return int()
    def setServiceOffersOffset(self, offset):
        '''void KServiceType.setServiceOffersOffset(int offset)'''
    def parentType(self):
        '''unknown-type KServiceType.parentType()'''
        return unknown-type()
    def propertyDefs(self):
        '''unknown-type KServiceType.propertyDefs()'''
        return unknown-type()
    def propertyDefNames(self):
        '''QStringList KServiceType.propertyDefNames()'''
        return QStringList()
    def propertyDef(self, _name):
        '''Type KServiceType.propertyDef(QString _name)'''
        return Type()
    def inherits(self, servTypeName):
        '''bool KServiceType.inherits(QString servTypeName)'''
        return bool()
    def parentServiceType(self):
        '''QString KServiceType.parentServiceType()'''
        return QString()
    def isDerived(self):
        '''bool KServiceType.isDerived()'''
        return bool()
    def desktopEntryPath(self):
        '''QString KServiceType.desktopEntryPath()'''
        return QString()
    def comment(self):
        '''QString KServiceType.comment()'''
        return QString()


class KMimeType(KServiceType):
    """"""
    # Enum KMimeType.FindByNameOption
    DontResolveAlias = 0
    ResolveAliases = 0

    def __init__(self, str, offset):
        '''void KMimeType.__init__(QDataStream str, int offset)'''
    def __init__(self, fullpath, name, comment):
        '''void KMimeType.__init__(QString fullpath, QString name, QString comment)'''
    def matchFileName(self, filename, pattern):
        '''static bool KMimeType.matchFileName(QString filename, QString pattern)'''
        return bool()
    def sharedMimeInfoVersion(self):
        '''static int KMimeType.sharedMimeInfoVersion()'''
        return int()
    def extractKnownExtension(self, fileName):
        '''static QString KMimeType.extractKnownExtension(QString fileName)'''
        return QString()
    def mainExtension(self):
        '''QString KMimeType.mainExtension()'''
        return QString()
    def userSpecifiedIconName(self):
        '''QString KMimeType.userSpecifiedIconName()'''
        return QString()
    def is_(self, mimeTypeName):
        '''bool KMimeType.is_(QString mimeTypeName)'''
        return bool()
    def allParentMimeTypes(self):
        '''QStringList KMimeType.allParentMimeTypes()'''
        return QStringList()
    def parentMimeTypes(self):
        '''QStringList KMimeType.parentMimeTypes()'''
        return QStringList()
    def parentMimeType(self):
        '''QString KMimeType.parentMimeType()'''
        return QString()
    def isDefault(self):
        '''bool KMimeType.isDefault()'''
        return bool()
    def defaultMimeTypePtr(self):
        '''static unknown-type KMimeType.defaultMimeTypePtr()'''
        return unknown-type()
    def defaultMimeType(self):
        '''static QString KMimeType.defaultMimeType()'''
        return QString()
    def allMimeTypes(self):
        '''static unknown-type KMimeType.allMimeTypes()'''
        return unknown-type()
    def isBufferBinaryData(self, data):
        '''static bool KMimeType.isBufferBinaryData(QByteArray data)'''
        return bool()
    def isBinaryData(self, fileName):
        '''static bool KMimeType.isBinaryData(QString fileName)'''
        return bool()
    def findByFileContent(self, fileName, accuracy):
        '''static unknown-type KMimeType.findByFileContent(QString fileName, int accuracy)'''
        return unknown-type()
    def findByNameAndContent(self, name, data, mode = 0, accuracy = None):
        '''static unknown-type KMimeType.findByNameAndContent(QString name, QByteArray data, int mode = 0, int accuracy)'''
        return unknown-type()
    def findByNameAndContent(self, name, device, mode = 0, accuracy = None):
        '''static unknown-type KMimeType.findByNameAndContent(QString name, QIODevice device, int mode = 0, int accuracy)'''
        return unknown-type()
    def findByContent(self, data, accuracy):
        '''static unknown-type KMimeType.findByContent(QByteArray data, int accuracy)'''
        return unknown-type()
    def findByContent(self, device, accuracy):
        '''static unknown-type KMimeType.findByContent(QIODevice device, int accuracy)'''
        return unknown-type()
    def findByPath(self, path, mode = 0, fast_mode = False, accuracy = None):
        '''static unknown-type KMimeType.findByPath(QString path, int mode = 0, bool fast_mode = False, int accuracy)'''
        return unknown-type()
    def findByUrl(self, url, mode = 0, is_local_file = False, fast_mode = False, accuracy = None):
        '''static unknown-type KMimeType.findByUrl(KUrl url, int mode = 0, bool is_local_file = False, bool fast_mode = False, int accuracy)'''
        return unknown-type()
    def mimeType(self, name, options = None):
        '''static unknown-type KMimeType.mimeType(QString name, KMimeType.FindByNameOption options = KMimeType.DontResolveAlias)'''
        return unknown-type()
    def patterns(self):
        '''QStringList KMimeType.patterns()'''
        return QStringList()
    def comment(self, url = KUrl()):
        '''QString KMimeType.comment(KUrl url = KUrl())'''
        return QString()
    def favIconForUrl(self, url):
        '''static QString KMimeType.favIconForUrl(KUrl url)'''
        return QString()
    def iconNameForUrl(self, url, mode = 0):
        '''static QString KMimeType.iconNameForUrl(KUrl url, int mode = 0)'''
        return QString()
    def iconName(self, url = KUrl()):
        '''QString KMimeType.iconName(KUrl url = KUrl())'''
        return QString()


class KMimeTypeTrader():
    """"""
    def self(self):
        '''static KMimeTypeTrader KMimeTypeTrader.self()'''
        return KMimeTypeTrader()
    def preferredService(self, mimeType, genericServiceType = None):
        '''unknown-type KMimeTypeTrader.preferredService(QString mimeType, QString genericServiceType = QString.fromLatin1Application)'''
        return unknown-type()
    def query(self, mimeType, genericServiceType = None, constraint = QString()):
        '''unknown-type KMimeTypeTrader.query(QString mimeType, QString genericServiceType = QString.fromLatin1Application, QString constraint = QString())'''
        return unknown-type()


class KPluginFactory(QObject):
    """"""
    def __init__(self, componentName = None, catalogName = None, parent = None):
        '''void KPluginFactory.__init__(str componentName = None, str catalogName = None, QObject parent = None)'''
    def __init__(self, aboutData, parent = None):
        '''void KPluginFactory.__init__(KAboutData aboutData, QObject parent = None)'''
    def __init__(self, aboutData, parent = None):
        '''void KPluginFactory.__init__(KAboutData aboutData, QObject parent = None)'''
    def __init__(self, parent):
        '''void KPluginFactory.__init__(QObject parent)'''
    def setComponentData(self, componentData):
        '''void KPluginFactory.setComponentData(KComponentData componentData)'''
    def createObject(self, parent, className, args):
        '''QObject KPluginFactory.createObject(QObject parent, str className, QStringList args)'''
        return QObject()
    def setupTranslations(self):
        '''void KPluginFactory.setupTranslations()'''
    def variantListToStringList(self, list):
        '''QStringList KPluginFactory.variantListToStringList(list-of-QVariant list)'''
        return QStringList()
    def stringListToVariantList(self, list):
        '''list-of-QVariant KPluginFactory.stringListToVariantList(QStringList list)'''
        return [QVariant()]
    objectCreated = pyqtSignal() # void objectCreated(QObject *) - signal
    def create(self, parent = None, classname = QObject, args = QStringList()):
        '''QObject KPluginFactory.create(QObject parent = None, str classname = QObject, QStringList args = QStringList())'''
        return QObject()
    def create(self, iface, parentWidget, parent, args, keyword):
        '''QObject KPluginFactory.create(str iface, QWidget parentWidget, QObject parent, list-of-QVariant args, QString keyword)'''
        return QObject()
    def componentData(self):
        '''KComponentData KPluginFactory.componentData()'''
        return KComponentData()


class KPluginInfo():
    """"""
    def __init__(self, filename, resource = None):
        '''void KPluginInfo.__init__(QString filename, str resource = None)'''
    def __init__(self, service):
        '''void KPluginInfo.__init__(unknown-type service)'''
    def __init__(self):
        '''void KPluginInfo.__init__()'''
    def __init__(self, copy):
        '''void KPluginInfo.__init__(KPluginInfo copy)'''
    def __ge__(self, rhs):
        '''bool KPluginInfo.__ge__(KPluginInfo rhs)'''
        return bool()
    def __le__(self, rhs):
        '''bool KPluginInfo.__le__(KPluginInfo rhs)'''
        return bool()
    def __gt__(self, rhs):
        '''bool KPluginInfo.__gt__(KPluginInfo rhs)'''
        return bool()
    def __lt__(self, rhs):
        '''bool KPluginInfo.__lt__(KPluginInfo rhs)'''
        return bool()
    def __ne__(self, rhs):
        '''bool KPluginInfo.__ne__(KPluginInfo rhs)'''
        return bool()
    def __eq__(self, rhs):
        '''bool KPluginInfo.__eq__(KPluginInfo rhs)'''
        return bool()
    def isValid(self):
        '''bool KPluginInfo.isValid()'''
        return bool()
    def defaults(self):
        '''void KPluginInfo.defaults()'''
    def load(self, config = KConfigGroup()):
        '''void KPluginInfo.load(KConfigGroup config = KConfigGroup())'''
    def save(self, config = KConfigGroup()):
        '''void KPluginInfo.save(KConfigGroup config = KConfigGroup())'''
    def config(self):
        '''KConfigGroup KPluginInfo.config()'''
        return KConfigGroup()
    def setConfig(self, config):
        '''void KPluginInfo.setConfig(KConfigGroup config)'''
    def kcmServices(self):
        '''unknown-type KPluginInfo.kcmServices()'''
        return unknown-type()
    def service(self):
        '''unknown-type KPluginInfo.service()'''
        return unknown-type()
    def dependencies(self):
        '''QStringList KPluginInfo.dependencies()'''
        return QStringList()
    def fullLicense(self):
        '''KAboutLicense KPluginInfo.fullLicense()'''
        return KAboutLicense()
    def license(self):
        '''QString KPluginInfo.license()'''
        return QString()
    def website(self):
        '''QString KPluginInfo.website()'''
        return QString()
    def version(self):
        '''QString KPluginInfo.version()'''
        return QString()
    def pluginName(self):
        '''QString KPluginInfo.pluginName()'''
        return QString()
    def category(self):
        '''QString KPluginInfo.category()'''
        return QString()
    def email(self):
        '''QString KPluginInfo.email()'''
        return QString()
    def author(self):
        '''QString KPluginInfo.author()'''
        return QString()
    def entryPath(self):
        '''QString KPluginInfo.entryPath()'''
        return QString()
    def icon(self):
        '''QString KPluginInfo.icon()'''
        return QString()
    def comment(self):
        '''QString KPluginInfo.comment()'''
        return QString()
    def name(self):
        '''QString KPluginInfo.name()'''
        return QString()
    def property(self, key):
        '''QVariant KPluginInfo.property(QString key)'''
        return QVariant()
    def isPluginEnabledByDefault(self):
        '''bool KPluginInfo.isPluginEnabledByDefault()'''
        return bool()
    def isPluginEnabled(self):
        '''bool KPluginInfo.isPluginEnabled()'''
        return bool()
    def setPluginEnabled(self, enabled):
        '''void KPluginInfo.setPluginEnabled(bool enabled)'''
    def isHidden(self):
        '''bool KPluginInfo.isHidden()'''
        return bool()
    def fromKPartsInstanceName(self, componentName, config = KConfigGroup()):
        '''static list-of-KPluginInfo KPluginInfo.fromKPartsInstanceName(QString componentName, KConfigGroup config = KConfigGroup())'''
        return [KPluginInfo()]
    def fromFiles(self, files, config = KConfigGroup()):
        '''static list-of-KPluginInfo KPluginInfo.fromFiles(QStringList files, KConfigGroup config = KConfigGroup())'''
        return [KPluginInfo()]
    def fromServices(self, services, config = KConfigGroup()):
        '''static list-of-KPluginInfo KPluginInfo.fromServices(unknown-type services, KConfigGroup config = KConfigGroup())'''
        return [KPluginInfo()]


class KPluginLoader(QPluginLoader):
    """"""
    def __init__(self, plugin, componentdata = None, parent = None):
        '''void KPluginLoader.__init__(QString plugin, KComponentData componentdata = KGlobal.mainComponent(), QObject parent = None)'''
    def __init__(self, service, componentdata = None, parent = None):
        '''void KPluginLoader.__init__(KService service, KComponentData componentdata = KGlobal.mainComponent(), QObject parent = None)'''
    def load(self):
        '''bool KPluginLoader.load()'''
        return bool()
    def isLoaded(self):
        '''bool KPluginLoader.isLoaded()'''
        return bool()
    def errorString(self):
        '''QString KPluginLoader.errorString()'''
        return QString()
    def pluginVersion(self):
        '''int KPluginLoader.pluginVersion()'''
        return int()
    def pluginName(self):
        '''QString KPluginLoader.pluginName()'''
        return QString()
    def factory(self):
        '''KPluginFactory KPluginLoader.factory()'''
        return KPluginFactory()


class KProcess(QProcess):
    """"""
    # Enum KProcess.OutputChannelMode
    SeparateChannels = 0
    MergedChannels = 0
    ForwardedChannels = 0
    OnlyStdoutChannel = 0
    OnlyStderrChannel = 0

    def __init__(self, parent = None):
        '''void KProcess.__init__(QObject parent = None)'''
    def pid(self):
        '''int KProcess.pid()'''
        return int()
    def startDetached(self):
        '''int KProcess.startDetached()'''
        return int()
    def startDetached(self, exe, args = QStringList()):
        '''static int KProcess.startDetached(QString exe, QStringList args = QStringList())'''
        return int()
    def startDetached(self, argv):
        '''static int KProcess.startDetached(QStringList argv)'''
        return int()
    def execute(self, msecs = None):
        '''int KProcess.execute(int msecs = -1)'''
        return int()
    def execute(self, exe, args = QStringList(), msecs = None):
        '''static int KProcess.execute(QString exe, QStringList args = QStringList(), int msecs = -1)'''
        return int()
    def execute(self, argv, msecs = None):
        '''static int KProcess.execute(QStringList argv, int msecs = -1)'''
        return int()
    def start(self):
        '''void KProcess.start()'''
    def program(self):
        '''QStringList KProcess.program()'''
        return QStringList()
    def setShellCommand(self, cmd):
        '''void KProcess.setShellCommand(QString cmd)'''
    def clearProgram(self):
        '''void KProcess.clearProgram()'''
    def __lshift__(self, arg):
        '''KProcess KProcess.__lshift__(QString arg)'''
        return KProcess()
    def __lshift__(self, args):
        '''KProcess KProcess.__lshift__(QStringList args)'''
        return KProcess()
    def setProgram(self, exe, args = QStringList()):
        '''void KProcess.setProgram(QString exe, QStringList args = QStringList())'''
    def setProgram(self, argv):
        '''void KProcess.setProgram(QStringList argv)'''
    def clearEnvironment(self):
        '''void KProcess.clearEnvironment()'''
    def unsetEnv(self, name):
        '''void KProcess.unsetEnv(QString name)'''
    def setEnv(self, name, value, overwrite = True):
        '''void KProcess.setEnv(QString name, QString value, bool overwrite = True)'''
    def setNextOpenMode(self, mode):
        '''void KProcess.setNextOpenMode(QIODevice.OpenMode mode)'''
    def outputChannelMode(self):
        '''KProcess.OutputChannelMode KProcess.outputChannelMode()'''
        return KProcess.OutputChannelMode()
    def setOutputChannelMode(self, mode):
        '''void KProcess.setOutputChannelMode(KProcess.OutputChannelMode mode)'''


class KProtocolInfo(KSycocaEntry):
    """"""
    # Enum KProtocolInfo.FileNameUsedForCopying
    Name = 0
    FromUrl = 0
    DisplayName = 0

    # Enum KProtocolInfo.Type
    T_STREAM = 0
    T_FILESYSTEM = 0
    T_NONE = 0
    T_ERROR = 0

    def __init__(self, _str, offset):
        '''void KProtocolInfo.__init__(QDataStream _str, int offset)'''
    def maxSlavesPerHost(self, protocol):
        '''static int KProtocolInfo.maxSlavesPerHost(QString protocol)'''
        return int()
    def fileNameUsedForCopying(self):
        '''KProtocolInfo.FileNameUsedForCopying KProtocolInfo.fileNameUsedForCopying()'''
        return KProtocolInfo.FileNameUsedForCopying()
    def canDeleteRecursive(self):
        '''bool KProtocolInfo.canDeleteRecursive()'''
        return bool()
    def canRenameToFile(self):
        '''bool KProtocolInfo.canRenameToFile()'''
        return bool()
    def canRenameFromFile(self):
        '''bool KProtocolInfo.canRenameFromFile()'''
        return bool()
    def archiveMimeTypes(self):
        '''QStringList KProtocolInfo.archiveMimeTypes()'''
        return QStringList()
    def defaultMimeType(self):
        '''QString KProtocolInfo.defaultMimeType()'''
        return QString()
    def supportsListing(self):
        '''bool KProtocolInfo.supportsListing()'''
        return bool()
    def proxiedBy(self, protocol):
        '''static QString KProtocolInfo.proxiedBy(QString protocol)'''
        return QString()
    def capabilities(self, protocol):
        '''static QStringList KProtocolInfo.capabilities(QString protocol)'''
        return QStringList()
    def showFilePreview(self, protocol):
        '''static bool KProtocolInfo.showFilePreview(QString protocol)'''
        return bool()
    def protocolClass(self, protocol):
        '''static QString KProtocolInfo.protocolClass(QString protocol)'''
        return QString()
    def docPath(self, protocol):
        '''static QString KProtocolInfo.docPath(QString protocol)'''
        return QString()
    def determineMimetypeFromExtension(self, protocol):
        '''static bool KProtocolInfo.determineMimetypeFromExtension(QString protocol)'''
        return bool()
    def maxSlaves(self, protocol):
        '''static int KProtocolInfo.maxSlaves(QString protocol)'''
        return int()
    def config(self, protocol):
        '''static QString KProtocolInfo.config(QString protocol)'''
        return QString()
    def icon(self, protocol):
        '''static QString KProtocolInfo.icon(QString protocol)'''
        return QString()
    def isFilterProtocol(self, url):
        '''static bool KProtocolInfo.isFilterProtocol(KUrl url)'''
        return bool()
    def isFilterProtocol(self, protocol):
        '''static bool KProtocolInfo.isFilterProtocol(QString protocol)'''
        return bool()
    def isHelperProtocol(self, url):
        '''static bool KProtocolInfo.isHelperProtocol(KUrl url)'''
        return bool()
    def isHelperProtocol(self, protocol):
        '''static bool KProtocolInfo.isHelperProtocol(QString protocol)'''
        return bool()
    def extraFields(self, url):
        '''static list-of-KProtocolInfo.ExtraField KProtocolInfo.extraFields(KUrl url)'''
        return [KProtocolInfo.ExtraField()]
    def exec_(self, protocol):
        '''static QString KProtocolInfo.exec_(QString protocol)'''
        return QString()
    def isKnownProtocol(self, url):
        '''static bool KProtocolInfo.isKnownProtocol(KUrl url)'''
        return bool()
    def isKnownProtocol(self, protocol):
        '''static bool KProtocolInfo.isKnownProtocol(QString protocol)'''
        return bool()
    def protocols(self):
        '''static QStringList KProtocolInfo.protocols()'''
        return QStringList()
    class ExtraField():
        """"""
        # Enum KProtocolInfo.ExtraField.Type
        String = 0
        DateTime = 0
        Invalid = 0
    
        name = None # QString - member
        type = None # KProtocolInfo.ExtraField.Type - member
        def __init__(self):
            '''void KProtocolInfo.ExtraField.__init__()'''
        def __init__(self, _name, _type):
            '''void KProtocolInfo.ExtraField.__init__(QString _name, KProtocolInfo.ExtraField.Type _type)'''
        def __init__(self):
            '''KProtocolInfo.ExtraField KProtocolInfo.ExtraField.__init__()'''
            return KProtocolInfo.ExtraField()


class KPty():
    """"""
    def __init__(self):
        '''void KPty.__init__()'''
    def slaveFd(self):
        '''int KPty.slaveFd()'''
        return int()
    def masterFd(self):
        '''int KPty.masterFd()'''
        return int()
    def ttyName(self):
        '''str KPty.ttyName()'''
        return str()
    def setEcho(self):
        '''bool KPty.setEcho()'''
        return bool()
    def setWinSize(self):
        '''int KPty.setWinSize()'''
        return int()
    def logout(self):
        '''void KPty.logout()'''
    def login(self):
        '''str KPty.login()'''
        return str()
    def setCTty(self):
        '''void KPty.setCTty()'''
    def closeSlave(self):
        '''void KPty.closeSlave()'''
    def close(self):
        '''void KPty.close()'''
    def open(self):
        '''bool KPty.open()'''
        return bool()


class KPtyDevice(QIODevice, KPty):
    """"""
    def __init__(self):
        '''QObject KPtyDevice.__init__()'''
        return QObject()
    readEof = pyqtSignal() # void readEof() - signal
    readyRead = pyqtSignal() # void readyRead() - signal
    def waitForReadyRead(self):
        '''int KPtyDevice.waitForReadyRead()'''
        return int()
    def waitForBytesWritten(self):
        '''int KPtyDevice.waitForBytesWritten()'''
        return int()
    def bytesToWrite(self):
        '''int KPtyDevice.bytesToWrite()'''
        return int()
    def bytesAvailable(self):
        '''int KPtyDevice.bytesAvailable()'''
        return int()
    def atEnd(self):
        '''bool KPtyDevice.atEnd()'''
        return bool()
    def canReadLine(self):
        '''bool KPtyDevice.canReadLine()'''
        return bool()
    def isSequential(self):
        '''bool KPtyDevice.isSequential()'''
        return bool()
    def close(self):
        '''void KPtyDevice.close()'''
    def open(self):
        '''QIODevice.OpenMode KPtyDevice.open()'''
        return QIODevice.OpenMode()


class KPtyProcess(KProcess):
    """"""
    # Enum KPtyProcess.PtyChannelFlag
    NoChannels = 0
    StdinChannel = 0
    StdoutChannel = 0
    StderrChannel = 0
    AllOutputChannels = 0
    AllChannels = 0

    def __init__(self):
        '''QObject KPtyProcess.__init__()'''
        return QObject()
    def setupChildProcess(self):
        '''void KPtyProcess.setupChildProcess()'''
    def pty(self):
        '''KPtyDevice KPtyProcess.pty()'''
        return KPtyDevice()
    def isUseUtmp(self):
        '''bool KPtyProcess.isUseUtmp()'''
        return bool()
    def setUseUtmp(self):
        '''bool KPtyProcess.setUseUtmp()'''
        return bool()
    def ptyChannels(self):
        '''KPtyProcess.PtyChannels KPtyProcess.ptyChannels()'''
        return KPtyProcess.PtyChannels()
    def setPtyChannels(self):
        '''KPtyProcess.PtyChannels KPtyProcess.setPtyChannels()'''
        return KPtyProcess.PtyChannels()
    class PtyChannels():
        """"""
        def __init__(self):
            '''KPtyProcess.PtyChannels KPtyProcess.PtyChannels.__init__()'''
            return KPtyProcess.PtyChannels()
        def __init__(self):
            '''int KPtyProcess.PtyChannels.__init__()'''
            return int()
        def __init__(self):
            '''void KPtyProcess.PtyChannels.__init__()'''
        def __bool__(self):
            '''int KPtyProcess.PtyChannels.__bool__()'''
            return int()
        def __ne__(self, f):
            '''bool KPtyProcess.PtyChannels.__ne__(KPtyProcess.PtyChannels f)'''
            return bool()
        def __eq__(self, f):
            '''bool KPtyProcess.PtyChannels.__eq__(KPtyProcess.PtyChannels f)'''
            return bool()
        def __invert__(self):
            '''KPtyProcess.PtyChannels KPtyProcess.PtyChannels.__invert__()'''
            return KPtyProcess.PtyChannels()
        def __and__(self, mask):
            '''KPtyProcess.PtyChannels KPtyProcess.PtyChannels.__and__(int mask)'''
            return KPtyProcess.PtyChannels()
        def __xor__(self, f):
            '''KPtyProcess.PtyChannels KPtyProcess.PtyChannels.__xor__(KPtyProcess.PtyChannels f)'''
            return KPtyProcess.PtyChannels()
        def __xor__(self, f):
            '''KPtyProcess.PtyChannels KPtyProcess.PtyChannels.__xor__(int f)'''
            return KPtyProcess.PtyChannels()
        def __or__(self, f):
            '''KPtyProcess.PtyChannels KPtyProcess.PtyChannels.__or__(KPtyProcess.PtyChannels f)'''
            return KPtyProcess.PtyChannels()
        def __or__(self, f):
            '''KPtyProcess.PtyChannels KPtyProcess.PtyChannels.__or__(int f)'''
            return KPtyProcess.PtyChannels()
        def __int__(self):
            '''int KPtyProcess.PtyChannels.__int__()'''
            return int()
        def __ixor__(self, f):
            '''KPtyProcess.PtyChannels KPtyProcess.PtyChannels.__ixor__(KPtyProcess.PtyChannels f)'''
            return KPtyProcess.PtyChannels()
        def __ior__(self, f):
            '''KPtyProcess.PtyChannels KPtyProcess.PtyChannels.__ior__(KPtyProcess.PtyChannels f)'''
            return KPtyProcess.PtyChannels()
        def __iand__(self, mask):
            '''KPtyProcess.PtyChannels KPtyProcess.PtyChannels.__iand__(int mask)'''
            return KPtyProcess.PtyChannels()


class KRandom():
    """"""
    def randomString(self, length):
        '''static QString KRandom.randomString(int length)'''
        return QString()
    def random(self):
        '''static int KRandom.random()'''
        return int()


class KRandomSequence():
    """"""
    def __init__(self, lngSeed = 0):
        '''void KRandomSequence.__init__(int lngSeed = 0)'''
    def __init__(self, a):
        '''void KRandomSequence.__init__(KRandomSequence a)'''
    def modulate(self, i):
        '''void KRandomSequence.modulate(int i)'''
    def getBool(self):
        '''bool KRandomSequence.getBool()'''
        return bool()
    def getLong(self, max):
        '''int KRandomSequence.getLong(int max)'''
        return int()
    def getDouble(self):
        '''float KRandomSequence.getDouble()'''
        return float()
    def setSeed(self, lngSeed = 0):
        '''void KRandomSequence.setSeed(int lngSeed = 0)'''


class KSaveFile(QFile):
    """"""
    def __init__(self):
        '''void KSaveFile.__init__()'''
    def __init__(self, filename, componentData = None):
        '''void KSaveFile.__init__(QString filename, KComponentData componentData = KGlobal.mainComponent())'''
    def rcsBackupFile(self, filename, backupDir = QString(), backupMessage = QString()):
        '''static bool KSaveFile.rcsBackupFile(QString filename, QString backupDir = QString(), QString backupMessage = QString())'''
        return bool()
    def numberedBackupFile(self, filename, backupDir = QString(), backupExtension = None, maxBackups = 10):
        '''static bool KSaveFile.numberedBackupFile(QString filename, QString backupDir = QString(), QString backupExtension = QString.fromLatin1~, int maxBackups = 10)'''
        return bool()
    def simpleBackupFile(self, filename, backupDir = QString(), backupExtension = None):
        '''static bool KSaveFile.simpleBackupFile(QString filename, QString backupDir = QString(), QString backupExtension = QLatin1String~)'''
        return bool()
    def backupFile(self, filename, backupDir = QString()):
        '''static bool KSaveFile.backupFile(QString filename, QString backupDir = QString())'''
        return bool()
    def finalize(self):
        '''bool KSaveFile.finalize()'''
        return bool()
    def abort(self):
        '''void KSaveFile.abort()'''
    def open(self, flags = None):
        '''bool KSaveFile.open(QIODevice.OpenMode flags = QIODevice.ReadWrite)'''
        return bool()
    def errorString(self):
        '''QString KSaveFile.errorString()'''
        return QString()
    def error(self):
        '''QFile.FileError KSaveFile.error()'''
        return QFile.FileError()
    def fileName(self):
        '''QString KSaveFile.fileName()'''
        return QString()
    def setFileName(self, filename):
        '''void KSaveFile.setFileName(QString filename)'''


class KService(KSycocaEntry):
    """"""
    # Enum KService.DBusStartupType
    DBusNone = 0
    DBusUnique = 0
    DBusMulti = 0
    DBusWait = 0

    def __init__(self, name, exec_, icon):
        '''void KService.__init__(QString name, QString exec, QString icon)'''
    def __init__(self, fullpath):
        '''void KService.__init__(QString fullpath)'''
    def __init__(self, config):
        '''void KService.__init__(KDesktopFile config)'''
    def __init__(self, str, offset):
        '''void KService.__init__(QDataStream str, int offset)'''
    def mimeTypes(self):
        '''QStringList KService.mimeTypes()'''
        return QStringList()
    def showInKDE(self):
        '''bool KService.showInKDE()'''
        return bool()
    def newServicePath(self, showInMenu, suggestedName, menuId = None, reservedMenuIds = None):
        '''static QString KService.newServicePath(bool showInMenu, QString suggestedName, QString menuId = None, QStringList reservedMenuIds = None)'''
        return QString()
    def allServices(self):
        '''static unknown-type KService.allServices()'''
        return unknown-type()
    def serviceByStorageId(self, _storageId):
        '''static unknown-type KService.serviceByStorageId(QString _storageId)'''
        return unknown-type()
    def serviceByMenuId(self, _menuId):
        '''static unknown-type KService.serviceByMenuId(QString _menuId)'''
        return unknown-type()
    def serviceByDesktopName(self, _name):
        '''static unknown-type KService.serviceByDesktopName(QString _name)'''
        return unknown-type()
    def serviceByDesktopPath(self, _path):
        '''static unknown-type KService.serviceByDesktopPath(QString _path)'''
        return unknown-type()
    def serviceByName(self, _name):
        '''static unknown-type KService.serviceByName(QString _name)'''
        return unknown-type()
    def setTerminalOptions(self, options):
        '''void KService.setTerminalOptions(QString options)'''
    def setTerminal(self, b):
        '''void KService.setTerminal(bool b)'''
    def setMenuId(self, menuId):
        '''void KService.setMenuId(QString menuId)'''
    def locateLocal(self):
        '''QString KService.locateLocal()'''
        return QString()
    def property(self, _name, t):
        '''QVariant KService.property(QString _name, Type t)'''
        return QVariant()
    def docPath(self):
        '''QString KService.docPath()'''
        return QString()
    def pluginKeyword(self):
        '''QString KService.pluginKeyword()'''
        return QString()
    def parentApp(self):
        '''QString KService.parentApp()'''
        return QString()
    def noDisplay(self):
        '''bool KService.noDisplay()'''
        return bool()
    def initialPreference(self):
        '''int KService.initialPreference()'''
        return int()
    def allowMultipleFiles(self):
        '''bool KService.allowMultipleFiles()'''
        return bool()
    def actions(self):
        '''list-of-KServiceAction KService.actions()'''
        return [KServiceAction()]
    def allowAsDefault(self):
        '''bool KService.allowAsDefault()'''
        return bool()
    def hasMimeType(self, mimeTypePtr):
        '''bool KService.hasMimeType(KServiceType mimeTypePtr)'''
        return bool()
    def hasMimeType(self, mimeType):
        '''bool KService.hasMimeType(QString mimeType)'''
        return bool()
    def hasServiceType(self, serviceTypePtr):
        '''bool KService.hasServiceType(QString serviceTypePtr)'''
        return bool()
    def serviceTypes(self):
        '''QStringList KService.serviceTypes()'''
        return QStringList()
    def categories(self):
        '''QStringList KService.categories()'''
        return QStringList()
    def keywords(self):
        '''QStringList KService.keywords()'''
        return QStringList()
    def untranslatedGenericName(self):
        '''QString KService.untranslatedGenericName()'''
        return QString()
    def genericName(self):
        '''QString KService.genericName()'''
        return QString()
    def comment(self):
        '''QString KService.comment()'''
        return QString()
    def path(self):
        '''QString KService.path()'''
        return QString()
    def dbusStartupType(self):
        '''KService.DBusStartupType KService.dbusStartupType()'''
        return KService.DBusStartupType()
    def storageId(self):
        '''QString KService.storageId()'''
        return QString()
    def menuId(self):
        '''QString KService.menuId()'''
        return QString()
    def desktopEntryName(self):
        '''QString KService.desktopEntryName()'''
        return QString()
    def desktopEntryPath(self):
        '''QString KService.desktopEntryPath()'''
        return QString()
    def username(self):
        '''QString KService.username()'''
        return QString()
    def substituteUid(self):
        '''bool KService.substituteUid()'''
        return bool()
    def terminalOptions(self):
        '''QString KService.terminalOptions()'''
        return QString()
    def terminal(self):
        '''bool KService.terminal()'''
        return bool()
    def icon(self):
        '''QString KService.icon()'''
        return QString()
    def library(self):
        '''QString KService.library()'''
        return QString()
    def exec_(self):
        '''QString KService.exec_()'''
        return QString()
    def type(self):
        '''QString KService.type()'''
        return QString()
    def isApplication(self):
        '''bool KService.isApplication()'''
        return bool()


class KServiceAction():
    """"""
    def __init__(self, name, text, icon, exec_, noDisplay = False):
        '''void KServiceAction.__init__(QString name, QString text, QString icon, QString exec, bool noDisplay = False)'''
    def __init__(self):
        '''void KServiceAction.__init__()'''
    def __init__(self, other):
        '''void KServiceAction.__init__(KServiceAction other)'''
    def isSeparator(self):
        '''bool KServiceAction.isSeparator()'''
        return bool()
    def noDisplay(self):
        '''bool KServiceAction.noDisplay()'''
        return bool()
    def exec_(self):
        '''QString KServiceAction.exec_()'''
        return QString()
    def icon(self):
        '''QString KServiceAction.icon()'''
        return QString()
    def text(self):
        '''QString KServiceAction.text()'''
        return QString()
    def name(self):
        '''QString KServiceAction.name()'''
        return QString()
    def data(self):
        '''QVariant KServiceAction.data()'''
        return QVariant()
    def setData(self, userData):
        '''void KServiceAction.setData(QVariant userData)'''


class KServiceGroup(KSycocaEntry):
    """"""
    # Enum KServiceGroup.EntriesOption
    NoOptions = 0
    SortEntries = 0
    ExcludeNoDisplay = 0
    AllowSeparators = 0
    SortByGenericName = 0

    def __init__(self, name):
        '''void KServiceGroup.__init__(QString name)'''
    def __init__(self, _fullpath, _relpath):
        '''void KServiceGroup.__init__(QString _fullpath, QString _relpath)'''
    def __init__(self, _str, offset, deep):
        '''void KServiceGroup.__init__(QDataStream _str, int offset, bool deep)'''
    def addEntry(self, entry):
        '''void KServiceGroup.addEntry(unknown-type entry)'''
    def childGroup(self, parent):
        '''static unknown-type KServiceGroup.childGroup(QString parent)'''
        return unknown-type()
    def group(self, relPath):
        '''static unknown-type KServiceGroup.group(QString relPath)'''
        return unknown-type()
    def root(self):
        '''static unknown-type KServiceGroup.root()'''
        return unknown-type()
    def baseGroup(self, baseGroupName):
        '''static unknown-type KServiceGroup.baseGroup(QString baseGroupName)'''
        return unknown-type()
    def directoryEntryPath(self):
        '''QString KServiceGroup.directoryEntryPath()'''
        return QString()
    def baseGroupName(self):
        '''QString KServiceGroup.baseGroupName()'''
        return QString()
    def serviceEntries(self, options = None):
        '''unknown-type KServiceGroup.serviceEntries(KServiceGroup.EntriesOptions options = KServiceGroup.ExcludeNoDisplay)'''
        return unknown-type()
    def entries(self, sorted, excludeNoDisplay, allowSeparators, sortByGenericName = False):
        '''unknown-type KServiceGroup.entries(bool sorted, bool excludeNoDisplay, bool allowSeparators, bool sortByGenericName = False)'''
        return unknown-type()
    def entries(self, sorted, excludeNoDisplay):
        '''unknown-type KServiceGroup.entries(bool sorted, bool excludeNoDisplay)'''
        return unknown-type()
    def entries(self, sorted = False):
        '''unknown-type KServiceGroup.entries(bool sorted = False)'''
        return unknown-type()
    def layoutInfo(self):
        '''QStringList KServiceGroup.layoutInfo()'''
        return QStringList()
    def setLayoutInfo(self, layout):
        '''void KServiceGroup.setLayoutInfo(QStringList layout)'''
    def suppressGenericNames(self):
        '''QStringList KServiceGroup.suppressGenericNames()'''
        return QStringList()
    def setInlineValue(self, _val):
        '''void KServiceGroup.setInlineValue(int _val)'''
    def inlineValue(self):
        '''int KServiceGroup.inlineValue()'''
        return int()
    def setAllowInline(self, _b):
        '''void KServiceGroup.setAllowInline(bool _b)'''
    def allowInline(self):
        '''bool KServiceGroup.allowInline()'''
        return bool()
    def setInlineAlias(self, _b):
        '''void KServiceGroup.setInlineAlias(bool _b)'''
    def inlineAlias(self):
        '''bool KServiceGroup.inlineAlias()'''
        return bool()
    def setShowInlineHeader(self, _b):
        '''void KServiceGroup.setShowInlineHeader(bool _b)'''
    def showInlineHeader(self):
        '''bool KServiceGroup.showInlineHeader()'''
        return bool()
    def setShowEmptyMenu(self, b):
        '''void KServiceGroup.setShowEmptyMenu(bool b)'''
    def showEmptyMenu(self):
        '''bool KServiceGroup.showEmptyMenu()'''
        return bool()
    def noDisplay(self):
        '''bool KServiceGroup.noDisplay()'''
        return bool()
    def childCount(self):
        '''int KServiceGroup.childCount()'''
        return int()
    def comment(self):
        '''QString KServiceGroup.comment()'''
        return QString()
    def icon(self):
        '''QString KServiceGroup.icon()'''
        return QString()
    def caption(self):
        '''QString KServiceGroup.caption()'''
        return QString()
    def relPath(self):
        '''QString KServiceGroup.relPath()'''
        return QString()
    class EntriesOptions():
        """"""
        def __init__(self):
            '''KServiceGroup.EntriesOptions KServiceGroup.EntriesOptions.__init__()'''
            return KServiceGroup.EntriesOptions()
        def __init__(self):
            '''int KServiceGroup.EntriesOptions.__init__()'''
            return int()
        def __init__(self):
            '''void KServiceGroup.EntriesOptions.__init__()'''
        def __bool__(self):
            '''int KServiceGroup.EntriesOptions.__bool__()'''
            return int()
        def __ne__(self, f):
            '''bool KServiceGroup.EntriesOptions.__ne__(KServiceGroup.EntriesOptions f)'''
            return bool()
        def __eq__(self, f):
            '''bool KServiceGroup.EntriesOptions.__eq__(KServiceGroup.EntriesOptions f)'''
            return bool()
        def __invert__(self):
            '''KServiceGroup.EntriesOptions KServiceGroup.EntriesOptions.__invert__()'''
            return KServiceGroup.EntriesOptions()
        def __and__(self, mask):
            '''KServiceGroup.EntriesOptions KServiceGroup.EntriesOptions.__and__(int mask)'''
            return KServiceGroup.EntriesOptions()
        def __xor__(self, f):
            '''KServiceGroup.EntriesOptions KServiceGroup.EntriesOptions.__xor__(KServiceGroup.EntriesOptions f)'''
            return KServiceGroup.EntriesOptions()
        def __xor__(self, f):
            '''KServiceGroup.EntriesOptions KServiceGroup.EntriesOptions.__xor__(int f)'''
            return KServiceGroup.EntriesOptions()
        def __or__(self, f):
            '''KServiceGroup.EntriesOptions KServiceGroup.EntriesOptions.__or__(KServiceGroup.EntriesOptions f)'''
            return KServiceGroup.EntriesOptions()
        def __or__(self, f):
            '''KServiceGroup.EntriesOptions KServiceGroup.EntriesOptions.__or__(int f)'''
            return KServiceGroup.EntriesOptions()
        def __int__(self):
            '''int KServiceGroup.EntriesOptions.__int__()'''
            return int()
        def __ixor__(self, f):
            '''KServiceGroup.EntriesOptions KServiceGroup.EntriesOptions.__ixor__(KServiceGroup.EntriesOptions f)'''
            return KServiceGroup.EntriesOptions()
        def __ior__(self, f):
            '''KServiceGroup.EntriesOptions KServiceGroup.EntriesOptions.__ior__(KServiceGroup.EntriesOptions f)'''
            return KServiceGroup.EntriesOptions()
        def __iand__(self, mask):
            '''KServiceGroup.EntriesOptions KServiceGroup.EntriesOptions.__iand__(int mask)'''
            return KServiceGroup.EntriesOptions()


class KServiceTypeProfile():
    """"""
    def hasProfile(self, serviceType):
        '''static bool KServiceTypeProfile.hasProfile(QString serviceType)'''
        return bool()
    def configurationMode(self):
        '''static bool KServiceTypeProfile.configurationMode()'''
        return bool()
    def setConfigurationMode(self):
        '''static void KServiceTypeProfile.setConfigurationMode()'''
    def deleteServiceTypeProfile(self, serviceType):
        '''static void KServiceTypeProfile.deleteServiceTypeProfile(QString serviceType)'''
    def writeServiceTypeProfile(self, serviceType, services, disabledServices = None):
        '''static void KServiceTypeProfile.writeServiceTypeProfile(QString serviceType, unknown-type services, unknown-type disabledServices = KService.List())'''


class KServiceTypeTrader():
    """"""
    def applyConstraints(self, lst, constraint):
        '''static void KServiceTypeTrader.applyConstraints(unknown-type lst, QString constraint)'''
    def self(self):
        '''static KServiceTypeTrader KServiceTypeTrader.self()'''
        return KServiceTypeTrader()
    def preferredService(self, serviceType):
        '''unknown-type KServiceTypeTrader.preferredService(QString serviceType)'''
        return unknown-type()
    def defaultOffers(self, serviceType, constraint = QString()):
        '''unknown-type KServiceTypeTrader.defaultOffers(QString serviceType, QString constraint = QString())'''
        return unknown-type()
    def query(self, servicetype, constraint = QString()):
        '''unknown-type KServiceTypeTrader.query(QString servicetype, QString constraint = QString())'''
        return unknown-type()


class KSharedConfig(KConfig):
    """"""
    def openConfig(self, fileName = QString(), mode = None, resourceType = config):
        '''static unknown-type KSharedConfig.openConfig(QString fileName = QString(), KConfig.OpenFlags mode = KConfig.FullConfig, str resourceType = config)'''
        return unknown-type()
    def openConfig(self, componentData, fileName = QString(), mode = None, resourceType = config):
        '''static unknown-type KSharedConfig.openConfig(KComponentData componentData, QString fileName = QString(), KConfig.OpenFlags mode = KConfig.FullConfig, str resourceType = config)'''
        return unknown-type()


class KShell():
    """"""
    # Enum KShell.Errors
    NoError = 0
    BadQuoting = 0
    FoundMeta = 0

    # Enum KShell.Option
    NoOptions = 0
    TildeExpand = 0
    AbortOnMeta = 0

    def tildeExpand(self, path):
        '''static QString KShell.tildeExpand(QString path)'''
        return QString()
    def quoteArg(self, arg):
        '''static QString KShell.quoteArg(QString arg)'''
        return QString()
    def joinArgs(self, args):
        '''static QString KShell.joinArgs(QStringList args)'''
        return QString()
    def splitArgs(self, cmd, flags = None, err = None):
        '''static QStringList KShell.splitArgs(QString cmd, KShell.Options flags = KShell.NoOptions, KShell.Errors err)'''
        return QStringList()
    class Options():
        """"""
        def __init__(self):
            '''KShell.Options KShell.Options.__init__()'''
            return KShell.Options()
        def __init__(self):
            '''int KShell.Options.__init__()'''
            return int()
        def __init__(self):
            '''void KShell.Options.__init__()'''
        def __bool__(self):
            '''int KShell.Options.__bool__()'''
            return int()
        def __ne__(self, f):
            '''bool KShell.Options.__ne__(KShell.Options f)'''
            return bool()
        def __eq__(self, f):
            '''bool KShell.Options.__eq__(KShell.Options f)'''
            return bool()
        def __invert__(self):
            '''KShell.Options KShell.Options.__invert__()'''
            return KShell.Options()
        def __and__(self, mask):
            '''KShell.Options KShell.Options.__and__(int mask)'''
            return KShell.Options()
        def __xor__(self, f):
            '''KShell.Options KShell.Options.__xor__(KShell.Options f)'''
            return KShell.Options()
        def __xor__(self, f):
            '''KShell.Options KShell.Options.__xor__(int f)'''
            return KShell.Options()
        def __or__(self, f):
            '''KShell.Options KShell.Options.__or__(KShell.Options f)'''
            return KShell.Options()
        def __or__(self, f):
            '''KShell.Options KShell.Options.__or__(int f)'''
            return KShell.Options()
        def __int__(self):
            '''int KShell.Options.__int__()'''
            return int()
        def __ixor__(self, f):
            '''KShell.Options KShell.Options.__ixor__(KShell.Options f)'''
            return KShell.Options()
        def __ior__(self, f):
            '''KShell.Options KShell.Options.__ior__(KShell.Options f)'''
            return KShell.Options()
        def __iand__(self, mask):
            '''KShell.Options KShell.Options.__iand__(int mask)'''
            return KShell.Options()


class KSocketFactory():
    """"""
    def proxyForDatagram(self, protocol, host):
        '''static QNetworkProxy KSocketFactory.proxyForDatagram(QString protocol, QString host)'''
        return QNetworkProxy()
    def proxyForListening(self, protocol):
        '''static QNetworkProxy KSocketFactory.proxyForListening(QString protocol)'''
        return QNetworkProxy()
    def proxyForConnection(self, protocol, host):
        '''static QNetworkProxy KSocketFactory.proxyForConnection(QString protocol, QString host)'''
        return QNetworkProxy()
    def datagramSocket(self, protocol, host, parent = None):
        '''static QUdpSocket KSocketFactory.datagramSocket(QString protocol, QString host, QObject parent = None)'''
        return QUdpSocket()
    def listen(self, protocol, address = None, port = 0, parent = None):
        '''static QTcpServer KSocketFactory.listen(QString protocol, QHostAddress address = QHostAddress.Any, int port = 0, QObject parent = None)'''
        return QTcpServer()
    def synchronousConnectToHost(self, protocol, host, port, msecs = 30000, parent = None):
        '''static QTcpSocket KSocketFactory.synchronousConnectToHost(QString protocol, QString host, int port, int msecs = 30000, QObject parent = None)'''
        return QTcpSocket()
    def synchronousConnectToHost(self, url, msecs = 30000, parent = None):
        '''static QTcpSocket KSocketFactory.synchronousConnectToHost(QUrl url, int msecs = 30000, QObject parent = None)'''
        return QTcpSocket()
    def synchronousConnectToHost(self, socket, protocol, host, port, msecs = 30000):
        '''static void KSocketFactory.synchronousConnectToHost(QTcpSocket socket, QString protocol, QString host, int port, int msecs = 30000)'''
    def synchronousConnectToHost(self, socket, url, msecs = 30000):
        '''static void KSocketFactory.synchronousConnectToHost(QTcpSocket socket, QUrl url, int msecs = 30000)'''
    def connectToHost(self, protocol, host, port, parent = None):
        '''static QTcpSocket KSocketFactory.connectToHost(QString protocol, QString host, int port, QObject parent = None)'''
        return QTcpSocket()
    def connectToHost(self, url, parent = None):
        '''static QTcpSocket KSocketFactory.connectToHost(QUrl url, QObject parent = None)'''
        return QTcpSocket()
    def connectToHost(self, socket, protocol, host, port):
        '''static void KSocketFactory.connectToHost(QTcpSocket socket, QString protocol, QString host, int port)'''
    def connectToHost(self, socket, url):
        '''static void KSocketFactory.connectToHost(QTcpSocket socket, QUrl url)'''


class KStandardDirs():
    """"""
    # Enum KStandardDirs.SearchOption
    NoSearchOptions = 0
    Recursive = 0
    NoDuplicates = 0
    IgnoreExecBit = 0

    def __init__(self):
        '''void KStandardDirs.__init__()'''
    def checkAccess(self, pathname, mode):
        '''static bool KStandardDirs.checkAccess(QString pathname, int mode)'''
        return bool()
    def locateLocal(self, type, filename, cData = None):
        '''static QString KStandardDirs.locateLocal(str type, QString filename, KComponentData cData = KGlobal.mainComponent())'''
        return QString()
    def locateLocal(self, type, filename, createDir, cData = None):
        '''static QString KStandardDirs.locateLocal(str type, QString filename, bool createDir, KComponentData cData = KGlobal.mainComponent())'''
        return QString()
    def locate(self, type, filename, cData = None):
        '''static QString KStandardDirs.locate(str type, QString filename, KComponentData cData = KGlobal.mainComponent())'''
        return QString()
    def realFilePath(self, filename):
        '''static QString KStandardDirs.realFilePath(QString filename)'''
        return QString()
    def realPath(self, dirname):
        '''static QString KStandardDirs.realPath(QString dirname)'''
        return QString()
    def exists(self, fullPath):
        '''static bool KStandardDirs.exists(QString fullPath)'''
        return bool()
    def installPath(self, type):
        '''static QString KStandardDirs.installPath(str type)'''
        return QString()
    def localxdgconfdir(self):
        '''QString KStandardDirs.localxdgconfdir()'''
        return QString()
    def localxdgdatadir(self):
        '''QString KStandardDirs.localxdgdatadir()'''
        return QString()
    def localkdedir(self):
        '''QString KStandardDirs.localkdedir()'''
        return QString()
    def kfsstnd_xdg_data_prefixes(self):
        '''QString KStandardDirs.kfsstnd_xdg_data_prefixes()'''
        return QString()
    def kfsstnd_xdg_conf_prefixes(self):
        '''QString KStandardDirs.kfsstnd_xdg_conf_prefixes()'''
        return QString()
    def kfsstnd_prefixes(self):
        '''QString KStandardDirs.kfsstnd_prefixes()'''
        return QString()
    def kde_default(self, type):
        '''static QString KStandardDirs.kde_default(str type)'''
        return QString()
    def makeDir(self, dir, mode = 493):
        '''static bool KStandardDirs.makeDir(QString dir, int mode = 493)'''
        return bool()
    def relativeLocation(self, type, absPath):
        '''QString KStandardDirs.relativeLocation(str type, QString absPath)'''
        return QString()
    def saveLocation(self, type, suffix = QString(), create = True):
        '''QString KStandardDirs.saveLocation(str type, QString suffix = QString(), bool create = True)'''
        return QString()
    def allTypes(self):
        '''QStringList KStandardDirs.allTypes()'''
        return QStringList()
    def resourceDirs(self, type):
        '''QStringList KStandardDirs.resourceDirs(str type)'''
        return QStringList()
    def addCustomized(self, config):
        '''bool KStandardDirs.addCustomized(KConfig config)'''
        return bool()
    def findAllExe(self, list, appname, pathstr = QString(), options = None):
        '''static int KStandardDirs.findAllExe(QStringList list, QString appname, QString pathstr = QString(), KStandardDirs.SearchOptions options = KStandardDirs.NoSearchOptions)'''
        return int()
    def findExe(self, appname, pathstr = QString(), options = None):
        '''static QString KStandardDirs.findExe(QString appname, QString pathstr = QString(), KStandardDirs.SearchOptions options = KStandardDirs.NoSearchOptions)'''
        return QString()
    def systemPaths(self, pstr = QString()):
        '''static QStringList KStandardDirs.systemPaths(QString pstr = QString())'''
        return QStringList()
    def findAllResources(self, type, filter = QString(), options = None):
        '''QStringList KStandardDirs.findAllResources(str type, QString filter = QString(), KStandardDirs.SearchOptions options = KStandardDirs.NoSearchOptions)'''
        return QStringList()
    def findAllResources(self, type, filter, options, relPaths):
        '''QStringList KStandardDirs.findAllResources(str type, QString filter, KStandardDirs.SearchOptions options, QStringList relPaths)'''
        return QStringList()
    def findResourceDir(self, type, filename):
        '''QString KStandardDirs.findResourceDir(str type, QString filename)'''
        return QString()
    def findDirs(self, type, reldir):
        '''QStringList KStandardDirs.findDirs(str type, QString reldir)'''
        return QStringList()
    def calcResourceHash(self, type, filename, options = None):
        '''int KStandardDirs.calcResourceHash(str type, QString filename, KStandardDirs.SearchOptions options = KStandardDirs.NoSearchOptions)'''
        return int()
    def isRestrictedResource(self, type, relPath = QString()):
        '''bool KStandardDirs.isRestrictedResource(str type, QString relPath = QString())'''
        return bool()
    def findResource(self, type, filename):
        '''QString KStandardDirs.findResource(str type, QString filename)'''
        return QString()
    def addResourceDir(self, type, absdir, priority = True):
        '''bool KStandardDirs.addResourceDir(str type, QString absdir, bool priority = True)'''
        return bool()
    def addResourceType(self, type, relativename, priority = True):
        '''bool KStandardDirs.addResourceType(str type, QString relativename, bool priority = True)'''
        return bool()
    def addResourceType(self, type, basetype, relativename, priority = True):
        '''bool KStandardDirs.addResourceType(str type, str basetype, QString relativename, bool priority = True)'''
        return bool()
    def addResourceType(self, type, basetype, relativename, priority = True):
        '''bool KStandardDirs.addResourceType(str type, str basetype, str relativename, bool priority = True)'''
        return bool()
    def addXdgDataPrefix(self, dir):
        '''void KStandardDirs.addXdgDataPrefix(QString dir)'''
    def addXdgConfigPrefix(self, dir):
        '''void KStandardDirs.addXdgConfigPrefix(QString dir)'''
    def addPrefix(self, dir):
        '''void KStandardDirs.addPrefix(QString dir)'''
    class SearchOptions():
        """"""
        def __init__(self):
            '''KStandardDirs.SearchOptions KStandardDirs.SearchOptions.__init__()'''
            return KStandardDirs.SearchOptions()
        def __init__(self):
            '''int KStandardDirs.SearchOptions.__init__()'''
            return int()
        def __init__(self):
            '''void KStandardDirs.SearchOptions.__init__()'''
        def __bool__(self):
            '''int KStandardDirs.SearchOptions.__bool__()'''
            return int()
        def __ne__(self, f):
            '''bool KStandardDirs.SearchOptions.__ne__(KStandardDirs.SearchOptions f)'''
            return bool()
        def __eq__(self, f):
            '''bool KStandardDirs.SearchOptions.__eq__(KStandardDirs.SearchOptions f)'''
            return bool()
        def __invert__(self):
            '''KStandardDirs.SearchOptions KStandardDirs.SearchOptions.__invert__()'''
            return KStandardDirs.SearchOptions()
        def __and__(self, mask):
            '''KStandardDirs.SearchOptions KStandardDirs.SearchOptions.__and__(int mask)'''
            return KStandardDirs.SearchOptions()
        def __xor__(self, f):
            '''KStandardDirs.SearchOptions KStandardDirs.SearchOptions.__xor__(KStandardDirs.SearchOptions f)'''
            return KStandardDirs.SearchOptions()
        def __xor__(self, f):
            '''KStandardDirs.SearchOptions KStandardDirs.SearchOptions.__xor__(int f)'''
            return KStandardDirs.SearchOptions()
        def __or__(self, f):
            '''KStandardDirs.SearchOptions KStandardDirs.SearchOptions.__or__(KStandardDirs.SearchOptions f)'''
            return KStandardDirs.SearchOptions()
        def __or__(self, f):
            '''KStandardDirs.SearchOptions KStandardDirs.SearchOptions.__or__(int f)'''
            return KStandardDirs.SearchOptions()
        def __int__(self):
            '''int KStandardDirs.SearchOptions.__int__()'''
            return int()
        def __ixor__(self, f):
            '''KStandardDirs.SearchOptions KStandardDirs.SearchOptions.__ixor__(KStandardDirs.SearchOptions f)'''
            return KStandardDirs.SearchOptions()
        def __ior__(self, f):
            '''KStandardDirs.SearchOptions KStandardDirs.SearchOptions.__ior__(KStandardDirs.SearchOptions f)'''
            return KStandardDirs.SearchOptions()
        def __iand__(self, mask):
            '''KStandardDirs.SearchOptions KStandardDirs.SearchOptions.__iand__(int mask)'''
            return KStandardDirs.SearchOptions()


class KStringHandler():
    """"""
    def preProcessWrap(self, text):
        '''static QString KStringHandler.preProcessWrap(QString text)'''
        return QString()
    def naturalCompare(self, a, b, caseSensitivity = None):
        '''static int KStringHandler.naturalCompare(QString a, QString b, Qt.CaseSensitivity caseSensitivity = Qt.CaseSensitive)'''
        return int()
    def from8Bit(self, str):
        '''static QString KStringHandler.from8Bit(str str)'''
        return QString()
    def isUtf8(self, str):
        '''static bool KStringHandler.isUtf8(str str)'''
        return bool()
    def obscure(self, str):
        '''static QString KStringHandler.obscure(QString str)'''
        return QString()
    def tagUrls(self, text):
        '''static QString KStringHandler.tagUrls(QString text)'''
        return QString()
    def perlSplit(self, sep, s, max = 0):
        '''static QStringList KStringHandler.perlSplit(QString sep, QString s, int max = 0)'''
        return QStringList()
    def perlSplit(self, sep, s, max = 0):
        '''static QStringList KStringHandler.perlSplit(QChar sep, QString s, int max = 0)'''
        return QStringList()
    def perlSplit(self, sep, s, max = 0):
        '''static QStringList KStringHandler.perlSplit(QRegExp sep, QString s, int max = 0)'''
        return QStringList()
    def rsqueeze(self, str, maxlen = 40):
        '''static QString KStringHandler.rsqueeze(QString str, int maxlen = 40)'''
        return QString()
    def csqueeze(self, str, maxlen = 40):
        '''static QString KStringHandler.csqueeze(QString str, int maxlen = 40)'''
        return QString()
    def lsqueeze(self, str, maxlen = 40):
        '''static QString KStringHandler.lsqueeze(QString str, int maxlen = 40)'''
        return QString()
    def capwords(self, text):
        '''static QString KStringHandler.capwords(QString text)'''
        return QString()
    def capwords(self, list):
        '''static QStringList KStringHandler.capwords(QStringList list)'''
        return QStringList()


class KSycoca(QObject):
    """"""
    # Enum KSycoca.DatabaseType
    LocalDatabase = 0
    GlobalDatabase = 0

    def __init__(self):
        '''bool KSycoca.__init__()'''
        return bool()
    def __init__(self):
        '''void KSycoca.__init__()'''
    databaseChanged = pyqtSignal() # void databaseChanged() - signal
    databaseChanged = pyqtSignal() # void databaseChanged(const QStringListamp;) - signal
    def readError(self):
        '''static bool KSycoca.readError()'''
        return bool()
    def flagError(self):
        '''static void KSycoca.flagError()'''
    def isChanged(self, type):
        '''static bool KSycoca.isChanged(str type)'''
        return bool()
    def disableAutoRebuild(self):
        '''static void KSycoca.disableAutoRebuild()'''
    def isBuilding(self):
        '''bool KSycoca.isBuilding()'''
        return bool()
    def allResourceDirs(self):
        '''QStringList KSycoca.allResourceDirs()'''
        return QStringList()
    def updateSignature(self):
        '''int KSycoca.updateSignature()'''
        return int()
    def timeStamp(self):
        '''int KSycoca.timeStamp()'''
        return int()
    def language(self):
        '''QString KSycoca.language()'''
        return QString()
    def absoluteFilePath(self, type = None):
        '''static QString KSycoca.absoluteFilePath(KSycoca.DatabaseType type = KSycoca.LocalDatabase)'''
        return QString()
    def kfsstnd_prefixes(self):
        '''QString KSycoca.kfsstnd_prefixes()'''
        return QString()
    def findFactory(self, id):
        '''QDataStream KSycoca.findFactory(KSycocaFactoryId id)'''
        return QDataStream()
    def findEntry(self, offset, type):
        '''QDataStream KSycoca.findEntry(int offset, KSycocaType type)'''
        return QDataStream()
    def isAvailable(self):
        '''static bool KSycoca.isAvailable()'''
        return bool()
    def version(self):
        '''static int KSycoca.version()'''
        return int()
    def self(self):
        '''static KSycoca KSycoca.self()'''
        return KSycoca()


class KSystemTimeZones(QObject):
    """"""
    def isTimeZoneDaemonAvailable(self):
        '''static bool KSystemTimeZones.isTimeZoneDaemonAvailable()'''
        return bool()
    def isSimulated(self):
        '''static bool KSystemTimeZones.isSimulated()'''
        return bool()
    def setLocalZone(self, tz):
        '''static void KSystemTimeZones.setLocalZone(KTimeZone tz)'''
    def realLocalZone(self):
        '''static KTimeZone KSystemTimeZones.realLocalZone()'''
        return KTimeZone()
    def zoneinfoDir(self):
        '''static QString KSystemTimeZones.zoneinfoDir()'''
        return QString()
    def local(self):
        '''static KTimeZone KSystemTimeZones.local()'''
        return KTimeZone()
    def readZone(self, name):
        '''static KTimeZone KSystemTimeZones.readZone(QString name)'''
        return KTimeZone()
    def zone(self, name):
        '''static KTimeZone KSystemTimeZones.zone(QString name)'''
        return KTimeZone()
    def zones(self):
        '''static dict-of-QString-KTimeZone KSystemTimeZones.zones()'''
        return dict-of-QString-KTimeZone()
    def timeZones(self):
        '''static KTimeZones KSystemTimeZones.timeZones()'''
        return KTimeZones()


class KTimeZone():
    """"""
    InvalidOffset = None # int - member
    InvalidTime_t = None # int - member
    UNKNOWN = None # float - member
    def __init__(self, name):
        '''void KTimeZone.__init__(QString name)'''
    def __init__(self, tz):
        '''void KTimeZone.__init__(KTimeZone tz)'''
    def __init__(self, impl):
        '''void KTimeZone.__init__(KTimeZoneBackend impl)'''
    def setData(self, data, source = None):
        '''void KTimeZone.setData(KTimeZoneData data, KTimeZoneSource source = None)'''
    def utc(self):
        '''static KTimeZone KTimeZone.utc()'''
        return KTimeZone()
    def toTime_t(self, utcDateTime):
        '''static int KTimeZone.toTime_t(QDateTime utcDateTime)'''
        return int()
    def fromTime_t(self, t):
        '''static QDateTime KTimeZone.fromTime_t(int t)'''
        return QDateTime()
    def updateBase(self, other):
        '''bool KTimeZone.updateBase(KTimeZone other)'''
        return bool()
    def data(self, create = False):
        '''KTimeZoneData KTimeZone.data(bool create = False)'''
        return KTimeZoneData()
    def parse(self):
        '''bool KTimeZone.parse()'''
        return bool()
    def source(self):
        '''KTimeZoneSource KTimeZone.source()'''
        return KTimeZoneSource()
    def leapSecondChanges(self):
        '''list-of-KTimeZone.LeapSeconds KTimeZone.leapSecondChanges()'''
        return [KTimeZone.LeapSeconds()]
    def transitionTimes(self, phase, start = QDateTime(), end = QDateTime()):
        '''list-of-QDateTime KTimeZone.transitionTimes(KTimeZone.Phase phase, QDateTime start = QDateTime(), QDateTime end = QDateTime())'''
        return [QDateTime()]
    def transitionIndex(self, dt, secondIndex, validTime):
        '''int KTimeZone.transitionIndex(QDateTime dt, int secondIndex, bool validTime)'''
        return int()
    def transitions(self, start = QDateTime(), end = QDateTime()):
        '''list-of-KTimeZone.Transition KTimeZone.transitions(QDateTime start = QDateTime(), QDateTime end = QDateTime())'''
        return [KTimeZone.Transition()]
    def hasTransitions(self):
        '''bool KTimeZone.hasTransitions()'''
        return bool()
    def phases(self):
        '''list-of-KTimeZone.Phase KTimeZone.phases()'''
        return [KTimeZone.Phase()]
    def isDst(self, t):
        '''bool KTimeZone.isDst(int t)'''
        return bool()
    def isDstAtUtc(self, utcDateTime):
        '''bool KTimeZone.isDstAtUtc(QDateTime utcDateTime)'''
        return bool()
    def offset(self, t):
        '''int KTimeZone.offset(int t)'''
        return int()
    def offsetAtUtc(self, utcDateTime):
        '''int KTimeZone.offsetAtUtc(QDateTime utcDateTime)'''
        return int()
    def offsetAtZoneTime(self, zoneDateTime, secondOffset):
        '''int KTimeZone.offsetAtZoneTime(QDateTime zoneDateTime, int secondOffset)'''
        return int()
    def currentOffset(self, basis = None):
        '''int KTimeZone.currentOffset(Qt.TimeSpec basis = Qt.UTC)'''
        return int()
    def toZoneTime(self, utcDateTime, secondOccurrence):
        '''QDateTime KTimeZone.toZoneTime(QDateTime utcDateTime, bool secondOccurrence)'''
        return QDateTime()
    def toUtc(self, zoneDateTime):
        '''QDateTime KTimeZone.toUtc(QDateTime zoneDateTime)'''
        return QDateTime()
    def convert(self, newZone, zoneDateTime):
        '''QDateTime KTimeZone.convert(KTimeZone newZone, QDateTime zoneDateTime)'''
        return QDateTime()
    def utcOffsets(self):
        '''list-of-int KTimeZone.utcOffsets()'''
        return [int()]
    def abbreviation(self, utcDateTime):
        '''QByteArray KTimeZone.abbreviation(QDateTime utcDateTime)'''
        return QByteArray()
    def abbreviations(self):
        '''list-of-QByteArray KTimeZone.abbreviations()'''
        return [QByteArray()]
    def comment(self):
        '''QString KTimeZone.comment()'''
        return QString()
    def longitude(self):
        '''float KTimeZone.longitude()'''
        return float()
    def latitude(self):
        '''float KTimeZone.latitude()'''
        return float()
    def countryCode(self):
        '''QString KTimeZone.countryCode()'''
        return QString()
    def name(self):
        '''QString KTimeZone.name()'''
        return QString()
    def isValid(self):
        '''bool KTimeZone.isValid()'''
        return bool()
    def type(self):
        '''QByteArray KTimeZone.type()'''
        return QByteArray()
    def __ne__(self, rhs):
        '''bool KTimeZone.__ne__(KTimeZone rhs)'''
        return bool()
    def __eq__(self, rhs):
        '''bool KTimeZone.__eq__(KTimeZone rhs)'''
        return bool()
    class Phase():
        """"""
        def __init__(self):
            '''void KTimeZone.Phase.__init__()'''
        def __init__(self, utcOffset, abbreviations, dst, comment = QString()):
            '''void KTimeZone.Phase.__init__(int utcOffset, QByteArray abbreviations, bool dst, QString comment = QString())'''
        def __init__(self, utcOffset, abbreviations, dst, comment = QString()):
            '''void KTimeZone.Phase.__init__(int utcOffset, list-of-QByteArray abbreviations, bool dst, QString comment = QString())'''
        def __init__(self, rhs):
            '''void KTimeZone.Phase.__init__(KTimeZone.Phase rhs)'''
        def comment(self):
            '''QString KTimeZone.Phase.comment()'''
            return QString()
        def isDst(self):
            '''bool KTimeZone.Phase.isDst()'''
            return bool()
        def abbreviations(self):
            '''list-of-QByteArray KTimeZone.Phase.abbreviations()'''
            return [QByteArray()]
        def utcOffset(self):
            '''int KTimeZone.Phase.utcOffset()'''
            return int()
        def __ne__(self, rhs):
            '''bool KTimeZone.Phase.__ne__(KTimeZone.Phase rhs)'''
            return bool()
        def __eq__(self, rhs):
            '''bool KTimeZone.Phase.__eq__(KTimeZone.Phase rhs)'''
            return bool()
    class LeapSeconds():
        """"""
        def __init__(self):
            '''void KTimeZone.LeapSeconds.__init__()'''
        def __init__(self, utcTime, leapSeconds, comment = QString()):
            '''void KTimeZone.LeapSeconds.__init__(QDateTime utcTime, int leapSeconds, QString comment = QString())'''
        def __init__(self, c):
            '''void KTimeZone.LeapSeconds.__init__(KTimeZone.LeapSeconds c)'''
        def __ge__(self, c):
            '''bool KTimeZone.LeapSeconds.__ge__(KTimeZone.LeapSeconds c)'''
            return bool()
        def comment(self):
            '''QString KTimeZone.LeapSeconds.comment()'''
            return QString()
        def leapSeconds(self):
            '''int KTimeZone.LeapSeconds.leapSeconds()'''
            return int()
        def dateTime(self):
            '''QDateTime KTimeZone.LeapSeconds.dateTime()'''
            return QDateTime()
        def isValid(self):
            '''bool KTimeZone.LeapSeconds.isValid()'''
            return bool()
        def __lt__(self, c):
            '''bool KTimeZone.LeapSeconds.__lt__(KTimeZone.LeapSeconds c)'''
            return bool()
    class Transition():
        """"""
        def __init__(self):
            '''void KTimeZone.Transition.__init__()'''
        def __init__(self, dt, phase):
            '''void KTimeZone.Transition.__init__(QDateTime dt, KTimeZone.Phase phase)'''
        def __init__(self, t):
            '''void KTimeZone.Transition.__init__(KTimeZone.Transition t)'''
        def __ge__(self, rhs):
            '''bool KTimeZone.Transition.__ge__(KTimeZone.Transition rhs)'''
            return bool()
        def __lt__(self, rhs):
            '''bool KTimeZone.Transition.__lt__(KTimeZone.Transition rhs)'''
            return bool()
        def phase(self):
            '''KTimeZone.Phase KTimeZone.Transition.phase()'''
            return KTimeZone.Phase()
        def time(self):
            '''QDateTime KTimeZone.Transition.time()'''
            return QDateTime()


class KSystemTimeZone(KTimeZone):
    """"""
    def __init__(self, source, name, countryCode = QString(), latitude = None, longitude = None, comment = QString()):
        '''void KSystemTimeZone.__init__(KSystemTimeZoneSource source, QString name, QString countryCode = QString(), float latitude = KTimeZone.UNKNOWN, float longitude = KTimeZone.UNKNOWN, QString comment = QString())'''
    def __init__(self):
        '''KSystemTimeZone KSystemTimeZone.__init__()'''
        return KSystemTimeZone()


class KTimeZoneBackend():
    """"""
    def __init__(self):
        '''void KTimeZoneBackend.__init__()'''
    def __init__(self, name):
        '''void KTimeZoneBackend.__init__(QString name)'''
    def __init__(self, other):
        '''void KTimeZoneBackend.__init__(KTimeZoneBackend other)'''
    def __init__(self, source, name, countryCode = QString(), latitude = None, longitude = None, comment = QString()):
        '''void KTimeZoneBackend.__init__(KTimeZoneSource source, QString name, QString countryCode = QString(), float latitude = KTimeZone.UNKNOWN, float longitude = KTimeZone.UNKNOWN, QString comment = QString())'''
    def hasTransitions(self, caller):
        '''bool KTimeZoneBackend.hasTransitions(KTimeZone caller)'''
        return bool()
    def isDst(self, caller, t):
        '''bool KTimeZoneBackend.isDst(KTimeZone caller, int t)'''
        return bool()
    def isDstAtUtc(self, caller, utcDateTime):
        '''bool KTimeZoneBackend.isDstAtUtc(KTimeZone caller, QDateTime utcDateTime)'''
        return bool()
    def offset(self, caller, t):
        '''int KTimeZoneBackend.offset(KTimeZone caller, int t)'''
        return int()
    def offsetAtUtc(self, caller, utcDateTime):
        '''int KTimeZoneBackend.offsetAtUtc(KTimeZone caller, QDateTime utcDateTime)'''
        return int()
    def offsetAtZoneTime(self, caller, zoneDateTime, secondOffset):
        '''int KTimeZoneBackend.offsetAtZoneTime(KTimeZone caller, QDateTime zoneDateTime, int secondOffset)'''
        return int()
    def type(self):
        '''QByteArray KTimeZoneBackend.type()'''
        return QByteArray()
    def clone(self):
        '''KTimeZoneBackend KTimeZoneBackend.clone()'''
        return KTimeZoneBackend()


class KSystemTimeZoneBackend(KTimeZoneBackend):
    """"""
    def __init__(self, source, name, countryCode, latitude, longitude, comment):
        '''void KSystemTimeZoneBackend.__init__(KSystemTimeZoneSource source, QString name, QString countryCode, float latitude, float longitude, QString comment)'''
    def __init__(self):
        '''KSystemTimeZoneBackend KSystemTimeZoneBackend.__init__()'''
        return KSystemTimeZoneBackend()
    def type(self):
        '''QByteArray KSystemTimeZoneBackend.type()'''
        return QByteArray()
    def isDst(self, caller, t):
        '''bool KSystemTimeZoneBackend.isDst(KTimeZone caller, int t)'''
        return bool()
    def isDstAtUtc(self, caller, utcDateTime):
        '''bool KSystemTimeZoneBackend.isDstAtUtc(KTimeZone caller, QDateTime utcDateTime)'''
        return bool()
    def offset(self, caller, t):
        '''int KSystemTimeZoneBackend.offset(KTimeZone caller, int t)'''
        return int()
    def offsetAtUtc(self, caller, utcDateTime):
        '''int KSystemTimeZoneBackend.offsetAtUtc(KTimeZone caller, QDateTime utcDateTime)'''
        return int()
    def offsetAtZoneTime(self, caller, zoneDateTime, secondOffset):
        '''int KSystemTimeZoneBackend.offsetAtZoneTime(KTimeZone caller, QDateTime zoneDateTime, int secondOffset)'''
        return int()
    def clone(self):
        '''KTimeZoneBackend KSystemTimeZoneBackend.clone()'''
        return KTimeZoneBackend()


class KTimeZoneSource():
    """"""
    def __init__(self):
        '''void KTimeZoneSource.__init__()'''
    def __init__(self, useZoneParse):
        '''void KTimeZoneSource.__init__(bool useZoneParse)'''
    def useZoneParse(self):
        '''bool KTimeZoneSource.useZoneParse()'''
        return bool()
    def parse(self, zone):
        '''KTimeZoneData KTimeZoneSource.parse(KTimeZone zone)'''
        return KTimeZoneData()


class KSystemTimeZoneSource(KTimeZoneSource):
    """"""
    def __init__(self):
        '''void KSystemTimeZoneSource.__init__()'''
    def endParseBlock(self):
        '''static void KSystemTimeZoneSource.endParseBlock()'''
    def startParseBlock(self):
        '''static void KSystemTimeZoneSource.startParseBlock()'''
    def parse(self, zone):
        '''KTimeZoneData KSystemTimeZoneSource.parse(KTimeZone zone)'''
        return KTimeZoneData()


class KSslKey():
    """"""
    # Enum KSslKey.KeySecrecy
    PublicKey = 0
    PrivateKey = 0

    # Enum KSslKey.Algorithm
    Rsa = 0
    Dsa = 0
    Dh = 0

    def __init__(self):
        '''void KSslKey.__init__()'''
    def __init__(self, other):
        '''void KSslKey.__init__(KSslKey other)'''
    def __init__(self, sslKey):
        '''void KSslKey.__init__(QSslKey sslKey)'''
    def toDer(self):
        '''QByteArray KSslKey.toDer()'''
        return QByteArray()
    def secrecy(self):
        '''KSslKey.KeySecrecy KSslKey.secrecy()'''
        return KSslKey.KeySecrecy()
    def isExportable(self):
        '''bool KSslKey.isExportable()'''
        return bool()
    def algorithm(self):
        '''KSslKey.Algorithm KSslKey.algorithm()'''
        return KSslKey.Algorithm()


class KSslCipher():
    """"""
    def __init__(self):
        '''void KSslCipher.__init__()'''
    def __init__(self, other):
        '''void KSslCipher.__init__(KSslCipher other)'''
    def __init__(self):
        '''QSslCipher KSslCipher.__init__()'''
        return QSslCipher()
    def supportedCiphers(self):
        '''static list-of-KSslCipher KSslCipher.supportedCiphers()'''
        return [KSslCipher()]
    def usedBits(self):
        '''int KSslCipher.usedBits()'''
        return int()
    def supportedBits(self):
        '''int KSslCipher.supportedBits()'''
        return int()
    def name(self):
        '''QString KSslCipher.name()'''
        return QString()
    def digestMethod(self):
        '''QString KSslCipher.digestMethod()'''
        return QString()
    def keyExchangeMethod(self):
        '''QString KSslCipher.keyExchangeMethod()'''
        return QString()
    def encryptionMethod(self):
        '''QString KSslCipher.encryptionMethod()'''
        return QString()
    def authenticationMethod(self):
        '''QString KSslCipher.authenticationMethod()'''
        return QString()
    def isNull(self):
        '''bool KSslCipher.isNull()'''
        return bool()


class KSslError():
    """"""
    # Enum KSslError.Error
    NoError = 0
    UnknownError = 0
    InvalidCertificateAuthorityCertificate = 0
    InvalidCertificate = 0
    CertificateSignatureFailed = 0
    SelfSignedCertificate = 0
    ExpiredCertificate = 0
    RevokedCertificate = 0
    InvalidCertificatePurpose = 0
    RejectedCertificate = 0
    UntrustedCertificate = 0
    NoPeerCertificate = 0
    HostNameMismatch = 0
    PathLengthExceeded = 0

    def __init__(self, error = None, cert = QSslCertificate()):
        '''void KSslError.__init__(KSslError.Error error = KSslError.NoError, QSslCertificate cert = QSslCertificate())'''
    def __init__(self, error):
        '''void KSslError.__init__(QSslError error)'''
    def __init__(self, other):
        '''void KSslError.__init__(KSslError other)'''
    def certificate(self):
        '''QSslCertificate KSslError.certificate()'''
        return QSslCertificate()
    def errorString(self):
        '''QString KSslError.errorString()'''
        return QString()
    def error(self):
        '''KSslError.Error KSslError.error()'''
        return KSslError.Error()


class KTcpSocket(QIODevice):
    """"""
    # Enum KTcpSocket.ProxyPolicy
    AutoProxy = 0
    ManualProxy = 0

    # Enum KTcpSocket.EncryptionMode
    UnencryptedMode = 0
    SslClientMode = 0
    SslServerMode = 0

    # Enum KTcpSocket.Error
    UnknownError = 0
    ConnectionRefusedError = 0
    RemoteHostClosedError = 0
    HostNotFoundError = 0
    SocketAccessError = 0
    SocketResourceError = 0
    SocketTimeoutError = 0
    NetworkError = 0
    UnsupportedSocketOperationError = 0

    # Enum KTcpSocket.SslVersion
    UnknownSslVersion = 0
    SslV2 = 0
    SslV3 = 0
    TlsV1 = 0
    SslV3_1 = 0
    TlsV1SslV3 = 0
    SecureProtocols = 0
    AnySslVersion = 0

    # Enum KTcpSocket.State
    UnconnectedState = 0
    HostLookupState = 0
    ConnectingState = 0
    ConnectedState = 0
    BoundState = 0
    ListeningState = 0
    ClosingState = 0

    def __init__(self, parent = None):
        '''void KTcpSocket.__init__(QObject parent = None)'''
    encryptedBytesWritten = pyqtSignal() # void encryptedBytesWritten(qint64) - signal
    def setVerificationPeerName(self, hostName):
        '''void KTcpSocket.setVerificationPeerName(QString hostName)'''
    def setSocketOption(self, options, value):
        '''void KTcpSocket.setSocketOption(QAbstractSocket.SocketOption options, QVariant value)'''
    def socketOption(self, options):
        '''QVariant KTcpSocket.socketOption(QAbstractSocket.SocketOption options)'''
        return QVariant()
    def startClientEncryption(self):
        '''void KTcpSocket.startClientEncryption()'''
    def ignoreSslErrors(self):
        '''void KTcpSocket.ignoreSslErrors()'''
    encryptionModeChanged = pyqtSignal() # void encryptionModeChanged(KTcpSocket::EncryptionMode) - signal
    encrypted = pyqtSignal() # void encrypted() - signal
    stateChanged = pyqtSignal() # void stateChanged(KTcpSocket::State) - signal
    proxyAuthenticationRequired = pyqtSignal() # void proxyAuthenticationRequired(const QNetworkProxyamp;,QAuthenticator *) - signal
    hostFound = pyqtSignal() # void hostFound() - signal
    disconnected = pyqtSignal() # void disconnected() - signal
    connected = pyqtSignal() # void connected() - signal
    def encryptionMode(self):
        '''KTcpSocket.EncryptionMode KTcpSocket.encryptionMode()'''
        return KTcpSocket.EncryptionMode()
    def waitForEncrypted(self, msecs = 30000):
        '''bool KTcpSocket.waitForEncrypted(int msecs = 30000)'''
        return bool()
    def negotiatedSslVersionName(self):
        '''QString KTcpSocket.negotiatedSslVersionName()'''
        return QString()
    def negotiatedSslVersion(self):
        '''KTcpSocket.SslVersion KTcpSocket.negotiatedSslVersion()'''
        return KTcpSocket.SslVersion()
    def advertisedSslVersion(self):
        '''KTcpSocket.SslVersion KTcpSocket.advertisedSslVersion()'''
        return KTcpSocket.SslVersion()
    def setAdvertisedSslVersion(self, version):
        '''void KTcpSocket.setAdvertisedSslVersion(KTcpSocket.SslVersion version)'''
    def setPrivateKey(self, key):
        '''void KTcpSocket.setPrivateKey(KSslKey key)'''
    def setPrivateKey(self, fileName, algorithm = None, format = None, passPhrase = QByteArray()):
        '''void KTcpSocket.setPrivateKey(QString fileName, KSslKey.Algorithm algorithm = KSslKey.Rsa, QSsl.EncodingFormat format = QSsl.Pem, QByteArray passPhrase = QByteArray())'''
    def setLocalCertificate(self, certificate):
        '''void KTcpSocket.setLocalCertificate(QSslCertificate certificate)'''
    def setLocalCertificate(self, fileName, format = None):
        '''void KTcpSocket.setLocalCertificate(QString fileName, QSsl.EncodingFormat format = QSsl.Pem)'''
    def setCiphers(self, ciphers):
        '''void KTcpSocket.setCiphers(list-of-KSslCipher ciphers)'''
    def setCaCertificates(self, certificates):
        '''void KTcpSocket.setCaCertificates(list-of-QSslCertificate certificates)'''
    def sessionCipher(self):
        '''KSslCipher KTcpSocket.sessionCipher()'''
        return KSslCipher()
    def privateKey(self):
        '''KSslKey KTcpSocket.privateKey()'''
        return KSslKey()
    def peerCertificateChain(self):
        '''list-of-QSslCertificate KTcpSocket.peerCertificateChain()'''
        return [QSslCertificate()]
    def localCertificate(self):
        '''QSslCertificate KTcpSocket.localCertificate()'''
        return QSslCertificate()
    def connectToHostEncrypted(self, hostName, port, openMode = None):
        '''void KTcpSocket.connectToHostEncrypted(QString hostName, int port, QIODevice.OpenMode openMode = QIODevice.ReadWrite)'''
    def ciphers(self):
        '''list-of-KSslCipher KTcpSocket.ciphers()'''
        return [KSslCipher()]
    def caCertificates(self):
        '''list-of-QSslCertificate KTcpSocket.caCertificates()'''
        return [QSslCertificate()]
    def addCaCertificates(self, certificates):
        '''void KTcpSocket.addCaCertificates(list-of-QSslCertificate certificates)'''
    def addCaCertificate(self, certificate):
        '''void KTcpSocket.addCaCertificate(QSslCertificate certificate)'''
    def waitForDisconnected(self, msecs = 30000):
        '''bool KTcpSocket.waitForDisconnected(int msecs = 30000)'''
        return bool()
    def waitForConnected(self, msecs = 30000):
        '''bool KTcpSocket.waitForConnected(int msecs = 30000)'''
        return bool()
    def state(self):
        '''KTcpSocket.State KTcpSocket.state()'''
        return KTcpSocket.State()
    def setReadBufferSize(self, size):
        '''void KTcpSocket.setReadBufferSize(int size)'''
    def setProxy(self, proxy):
        '''void KTcpSocket.setProxy(QNetworkProxy proxy)'''
    def readBufferSize(self):
        '''int KTcpSocket.readBufferSize()'''
        return int()
    def proxy(self):
        '''QNetworkProxy KTcpSocket.proxy()'''
        return QNetworkProxy()
    def peerPort(self):
        '''int KTcpSocket.peerPort()'''
        return int()
    def peerName(self):
        '''QString KTcpSocket.peerName()'''
        return QString()
    def peerAddress(self):
        '''QHostAddress KTcpSocket.peerAddress()'''
        return QHostAddress()
    def localAddress(self):
        '''QHostAddress KTcpSocket.localAddress()'''
        return QHostAddress()
    def isValid(self):
        '''bool KTcpSocket.isValid()'''
        return bool()
    def flush(self):
        '''bool KTcpSocket.flush()'''
        return bool()
    def sslErrors(self):
        '''list-of-KSslError KTcpSocket.sslErrors()'''
        return [KSslError()]
    sslErrors = pyqtSignal() # void sslErrors(const QListlt;KSslErrorgt;amp;) - signal
    def error(self):
        '''KTcpSocket.Error KTcpSocket.error()'''
        return KTcpSocket.Error()
    error = pyqtSignal() # void error(KTcpSocket::Error) - signal
    def disconnectFromHost(self):
        '''void KTcpSocket.disconnectFromHost()'''
    def connectToHost(self, hostName, port, policy = None):
        '''void KTcpSocket.connectToHost(QString hostName, int port, KTcpSocket.ProxyPolicy policy = KTcpSocket.AutoProxy)'''
    def connectToHost(self, hostAddress, port, policy = None):
        '''void KTcpSocket.connectToHost(QHostAddress hostAddress, int port, KTcpSocket.ProxyPolicy policy = KTcpSocket.AutoProxy)'''
    def connectToHost(self, url, policy = None):
        '''void KTcpSocket.connectToHost(KUrl url, KTcpSocket.ProxyPolicy policy = KTcpSocket.AutoProxy)'''
    def abort(self):
        '''void KTcpSocket.abort()'''
    def waitForReadyRead(self, msecs = 30000):
        '''bool KTcpSocket.waitForReadyRead(int msecs = 30000)'''
        return bool()
    def waitForBytesWritten(self, msecs):
        '''bool KTcpSocket.waitForBytesWritten(int msecs)'''
        return bool()
    def open(self, open):
        '''bool KTcpSocket.open(QIODevice.OpenMode open)'''
        return bool()
    def isSequential(self):
        '''bool KTcpSocket.isSequential()'''
        return bool()
    def close(self):
        '''void KTcpSocket.close()'''
    def canReadLine(self):
        '''bool KTcpSocket.canReadLine()'''
        return bool()
    def bytesToWrite(self):
        '''int KTcpSocket.bytesToWrite()'''
        return int()
    def bytesAvailable(self):
        '''int KTcpSocket.bytesAvailable()'''
        return int()
    def atEnd(self):
        '''bool KTcpSocket.atEnd()'''
        return bool()
    class SslVersions():
        """"""
        def __init__(self):
            '''KTcpSocket.SslVersions KTcpSocket.SslVersions.__init__()'''
            return KTcpSocket.SslVersions()
        def __init__(self):
            '''int KTcpSocket.SslVersions.__init__()'''
            return int()
        def __init__(self):
            '''void KTcpSocket.SslVersions.__init__()'''
        def __bool__(self):
            '''int KTcpSocket.SslVersions.__bool__()'''
            return int()
        def __ne__(self, f):
            '''bool KTcpSocket.SslVersions.__ne__(KTcpSocket.SslVersions f)'''
            return bool()
        def __eq__(self, f):
            '''bool KTcpSocket.SslVersions.__eq__(KTcpSocket.SslVersions f)'''
            return bool()
        def __invert__(self):
            '''KTcpSocket.SslVersions KTcpSocket.SslVersions.__invert__()'''
            return KTcpSocket.SslVersions()
        def __and__(self, mask):
            '''KTcpSocket.SslVersions KTcpSocket.SslVersions.__and__(int mask)'''
            return KTcpSocket.SslVersions()
        def __xor__(self, f):
            '''KTcpSocket.SslVersions KTcpSocket.SslVersions.__xor__(KTcpSocket.SslVersions f)'''
            return KTcpSocket.SslVersions()
        def __xor__(self, f):
            '''KTcpSocket.SslVersions KTcpSocket.SslVersions.__xor__(int f)'''
            return KTcpSocket.SslVersions()
        def __or__(self, f):
            '''KTcpSocket.SslVersions KTcpSocket.SslVersions.__or__(KTcpSocket.SslVersions f)'''
            return KTcpSocket.SslVersions()
        def __or__(self, f):
            '''KTcpSocket.SslVersions KTcpSocket.SslVersions.__or__(int f)'''
            return KTcpSocket.SslVersions()
        def __int__(self):
            '''int KTcpSocket.SslVersions.__int__()'''
            return int()
        def __ixor__(self, f):
            '''KTcpSocket.SslVersions KTcpSocket.SslVersions.__ixor__(KTcpSocket.SslVersions f)'''
            return KTcpSocket.SslVersions()
        def __ior__(self, f):
            '''KTcpSocket.SslVersions KTcpSocket.SslVersions.__ior__(KTcpSocket.SslVersions f)'''
            return KTcpSocket.SslVersions()
        def __iand__(self, mask):
            '''KTcpSocket.SslVersions KTcpSocket.SslVersions.__iand__(int mask)'''
            return KTcpSocket.SslVersions()


class KSslErrorUiData():
    """"""
    def __init__(self):
        '''void KSslErrorUiData.__init__()'''
    def __init__(self, socket):
        '''void KSslErrorUiData.__init__(KTcpSocket socket)'''
    def __init__(self, other):
        '''void KSslErrorUiData.__init__(KSslErrorUiData other)'''
    def __init__(self, socket):
        '''void KSslErrorUiData.__init__(QSslSocket socket)'''


class KTempDir():
    """"""
    def __init__(self, directoryPrefix = QString(), mode = 448):
        '''void KTempDir.__init__(QString directoryPrefix = QString(), int mode = 448)'''
    def create(self, directoryPrefix, mode):
        '''bool KTempDir.create(QString directoryPrefix, int mode)'''
        return bool()
    def removeDir(self, path):
        '''static bool KTempDir.removeDir(QString path)'''
        return bool()
    def exists(self):
        '''bool KTempDir.exists()'''
        return bool()
    def unlink(self):
        '''void KTempDir.unlink()'''
    def name(self):
        '''QString KTempDir.name()'''
        return QString()
    def status(self):
        '''int KTempDir.status()'''
        return int()
    def autoRemove(self):
        '''bool KTempDir.autoRemove()'''
        return bool()
    def setAutoRemove(self, autoRemove):
        '''void KTempDir.setAutoRemove(bool autoRemove)'''


class KTemporaryFile(QTemporaryFile):
    """"""
    def __init__(self, componentData = None):
        '''void KTemporaryFile.__init__(KComponentData componentData = KGlobal.mainComponent())'''
    def setSuffix(self, suffix):
        '''void KTemporaryFile.setSuffix(QString suffix)'''
    def setPrefix(self, prefix):
        '''void KTemporaryFile.setPrefix(QString prefix)'''


class KTimeZones():
    """"""
    def __init__(self):
        '''void KTimeZones.__init__()'''
    def clear(self):
        '''void KTimeZones.clear()'''
    def remove(self, zone):
        '''KTimeZone KTimeZones.remove(KTimeZone zone)'''
        return KTimeZone()
    def remove(self, name):
        '''KTimeZone KTimeZones.remove(QString name)'''
        return KTimeZone()
    def add(self, zone):
        '''bool KTimeZones.add(KTimeZone zone)'''
        return bool()
    def zones(self):
        '''dict-of-QString-KTimeZone KTimeZones.zones()'''
        return dict-of-QString-KTimeZone()
    def zone(self, name):
        '''KTimeZone KTimeZones.zone(QString name)'''
        return KTimeZone()


class KTimeZoneData():
    """"""
    def __init__(self):
        '''void KTimeZoneData.__init__()'''
    def __init__(self, c):
        '''void KTimeZoneData.__init__(KTimeZoneData c)'''
    def setLeapSecondChanges(self, adjusts):
        '''void KTimeZoneData.setLeapSecondChanges(list-of-KTimeZone.LeapSeconds adjusts)'''
    def setTransitions(self, transitions):
        '''void KTimeZoneData.setTransitions(list-of-KTimeZone.Transition transitions)'''
    def setPhases(self, phases, previousUtcOffset):
        '''void KTimeZoneData.setPhases(list-of-KTimeZone.Phase phases, int previousUtcOffset)'''
    def setPhases(self, phases, previousPhase):
        '''void KTimeZoneData.setPhases(list-of-KTimeZone.Phase phases, KTimeZone.Phase previousPhase)'''
    def leapSecondChange(self, utc):
        '''KTimeZone.LeapSeconds KTimeZoneData.leapSecondChange(QDateTime utc)'''
        return KTimeZone.LeapSeconds()
    def leapSecondChanges(self):
        '''list-of-KTimeZone.LeapSeconds KTimeZoneData.leapSecondChanges()'''
        return [KTimeZone.LeapSeconds()]
    def transitionTimes(self, phase, start = QDateTime(), end = QDateTime()):
        '''list-of-QDateTime KTimeZoneData.transitionTimes(KTimeZone.Phase phase, QDateTime start = QDateTime(), QDateTime end = QDateTime())'''
        return [QDateTime()]
    def transitionIndex(self, dt, secondIndex, validTime):
        '''int KTimeZoneData.transitionIndex(QDateTime dt, int secondIndex, bool validTime)'''
        return int()
    def transitions(self, start = QDateTime(), end = QDateTime()):
        '''list-of-KTimeZone.Transition KTimeZoneData.transitions(QDateTime start = QDateTime(), QDateTime end = QDateTime())'''
        return [KTimeZone.Transition()]
    def hasTransitions(self):
        '''bool KTimeZoneData.hasTransitions()'''
        return bool()
    def phases(self):
        '''list-of-KTimeZone.Phase KTimeZoneData.phases()'''
        return [KTimeZone.Phase()]
    def previousUtcOffset(self):
        '''int KTimeZoneData.previousUtcOffset()'''
        return int()
    def utcOffsets(self):
        '''list-of-int KTimeZoneData.utcOffsets()'''
        return [int()]
    def abbreviation(self, utcDateTime):
        '''QByteArray KTimeZoneData.abbreviation(QDateTime utcDateTime)'''
        return QByteArray()
    def abbreviations(self):
        '''list-of-QByteArray KTimeZoneData.abbreviations()'''
        return [QByteArray()]
    def clone(self):
        '''KTimeZoneData KTimeZoneData.clone()'''
        return KTimeZoneData()


class KToolInvocation(QObject):
    """"""
    kapplication_hook = pyqtSignal() # void kapplication_hook(QStringListamp;,QByteArrayamp;) - signal
    def kdeinitExecWait(self, name, args = QStringList(), error = None, pid = None, startup_id = QByteArray()):
        '''static int KToolInvocation.kdeinitExecWait(QString name, QStringList args = QStringList(), QString error = None, int pid, QByteArray startup_id = QByteArray())'''
        return int()
    def kdeinitExec(self, name, args = QStringList(), error = None, pid = None, startup_id = QByteArray()):
        '''static int KToolInvocation.kdeinitExec(QString name, QStringList args = QStringList(), QString error = None, int pid, QByteArray startup_id = QByteArray())'''
        return int()
    def startServiceByDesktopName(self, _name, URL, error = None, serviceName = None, pid = None, startup_id = QByteArray(), noWait = False):
        '''static int KToolInvocation.startServiceByDesktopName(QString _name, QString URL, QString error = None, QString serviceName = None, int pid, QByteArray startup_id = QByteArray(), bool noWait = False)'''
        return int()
    def startServiceByDesktopName(self, _name, URLs = QStringList(), error = None, serviceName = None, pid = None, startup_id = QByteArray(), noWait = False):
        '''static int KToolInvocation.startServiceByDesktopName(QString _name, QStringList URLs = QStringList(), QString error = None, QString serviceName = None, int pid, QByteArray startup_id = QByteArray(), bool noWait = False)'''
        return int()
    def startServiceByDesktopPath(self, _name, URL, error = None, serviceName = None, pid = None, startup_id = QByteArray(), noWait = False):
        '''static int KToolInvocation.startServiceByDesktopPath(QString _name, QString URL, QString error = None, QString serviceName = None, int pid, QByteArray startup_id = QByteArray(), bool noWait = False)'''
        return int()
    def startServiceByDesktopPath(self, _name, URLs = QStringList(), error = None, serviceName = None, pid = None, startup_id = QByteArray(), noWait = False):
        '''static int KToolInvocation.startServiceByDesktopPath(QString _name, QStringList URLs = QStringList(), QString error = None, QString serviceName = None, int pid, QByteArray startup_id = QByteArray(), bool noWait = False)'''
        return int()
    def startServiceByName(self, _name, URL, error = None, serviceName = None, pid = None, startup_id = QByteArray(), noWait = False):
        '''static int KToolInvocation.startServiceByName(QString _name, QString URL, QString error = None, QString serviceName = None, int pid, QByteArray startup_id = QByteArray(), bool noWait = False)'''
        return int()
    def startServiceByName(self, _name, URLs = QStringList(), error = None, serviceName = None, pid = None, startup_id = QByteArray(), noWait = False):
        '''static int KToolInvocation.startServiceByName(QString _name, QStringList URLs = QStringList(), QString error = None, QString serviceName = None, int pid, QByteArray startup_id = QByteArray(), bool noWait = False)'''
        return int()
    def invokeTerminal(self, command, workdir = QString(), startup_id = None):
        '''static void KToolInvocation.invokeTerminal(QString command, QString workdir = QString(), QByteArray startup_id = )'''
    def invokeBrowser(self, url, startup_id = QByteArray()):
        '''static void KToolInvocation.invokeBrowser(QString url, QByteArray startup_id = QByteArray())'''
    def invokeMailer(self, address, subject, startup_id = QByteArray()):
        '''static void KToolInvocation.invokeMailer(QString address, QString subject, QByteArray startup_id = QByteArray())'''
    def invokeMailer(self, mailtoURL, startup_id = QByteArray(), allowAttachments = False):
        '''static void KToolInvocation.invokeMailer(KUrl mailtoURL, QByteArray startup_id = QByteArray(), bool allowAttachments = False)'''
    def invokeMailer(self, to, cc, bcc, subject, body, messageFile = QString(), attachURLs = QStringList(), startup_id = QByteArray()):
        '''static void KToolInvocation.invokeMailer(QString to, QString cc, QString bcc, QString subject, QString body, QString messageFile = QString(), QStringList attachURLs = QStringList(), QByteArray startup_id = QByteArray())'''
    def invokeHelp(self, anchor = QString(), appname = QString(), startup_id = QByteArray()):
        '''static void KToolInvocation.invokeHelp(QString anchor = QString(), QString appname = QString(), QByteArray startup_id = QByteArray())'''
    def self(self):
        '''static KToolInvocation KToolInvocation.self()'''
        return KToolInvocation()


class KTzfileTimeZone(KTimeZone):
    """"""
    def __init__(self, source, name, countryCode = QString(), latitude = None, longitude = None, comment = QString()):
        '''void KTzfileTimeZone.__init__(KTzfileTimeZoneSource source, QString name, QString countryCode = QString(), float latitude = KTimeZone.UNKNOWN, float longitude = KTimeZone.UNKNOWN, QString comment = QString())'''
    def __init__(self):
        '''KTzfileTimeZone KTzfileTimeZone.__init__()'''
        return KTzfileTimeZone()


class KTzfileTimeZoneBackend(KTimeZoneBackend):
    """"""
    def __init__(self, source, name, countryCode, latitude, longitude, comment):
        '''void KTzfileTimeZoneBackend.__init__(KTzfileTimeZoneSource source, QString name, QString countryCode, float latitude, float longitude, QString comment)'''
    def __init__(self):
        '''KTzfileTimeZoneBackend KTzfileTimeZoneBackend.__init__()'''
        return KTzfileTimeZoneBackend()
    def type(self):
        '''QByteArray KTzfileTimeZoneBackend.type()'''
        return QByteArray()
    def hasTransitions(self, caller):
        '''bool KTzfileTimeZoneBackend.hasTransitions(KTimeZone caller)'''
        return bool()
    def clone(self):
        '''KTimeZoneBackend KTzfileTimeZoneBackend.clone()'''
        return KTimeZoneBackend()


class KTzfileTimeZoneSource(KTimeZoneSource):
    """"""
    def __init__(self, location):
        '''void KTzfileTimeZoneSource.__init__(QString location)'''
    def location(self):
        '''QString KTzfileTimeZoneSource.location()'''
        return QString()
    def parse(self, zone):
        '''KTimeZoneData KTzfileTimeZoneSource.parse(KTimeZone zone)'''
        return KTimeZoneData()


class KUrl(QUrl):
    """"""
    # Enum KUrl.EqualsOption
    CompareWithoutTrailingSlash = 0
    CompareWithoutFragment = 0
    AllowEmptyPath = 0

    # Enum KUrl.DirectoryOption
    ObeyTrailingSlash = 0
    AppendTrailingSlash = 0
    IgnoreTrailingSlash = 0

    # Enum KUrl.QueryItemsOption
    CaseInsensitiveKeys = 0

    # Enum KUrl.EncodedPathAndQueryOption
    PermitEmptyPath = 0
    AvoidEmptyPath = 0

    # Enum KUrl.CleanPathOption
    SimplifyDirSeparators = 0
    KeepDirSeparators = 0

    # Enum KUrl.AdjustPathOption
    RemoveTrailingSlash = 0
    LeaveTrailingSlash = 0
    AddTrailingSlash = 0

    # Enum KUrl.MimeDataFlags
    DefaultMimeDataFlags = 0
    NoTextExport = 0

    def __init__(self):
        '''void KUrl.__init__()'''
    def __init__(self, urlOrPath):
        '''void KUrl.__init__(QString urlOrPath)'''
    def __init__(self, urlOrPath):
        '''void KUrl.__init__(str urlOrPath)'''
    def __init__(self, urlOrPath):
        '''void KUrl.__init__(QByteArray urlOrPath)'''
    def __init__(self, u):
        '''void KUrl.__init__(KUrl u)'''
    def __init__(self, u):
        '''void KUrl.__init__(QUrl u)'''
    def __init__(self, _baseurl, _rel_url):
        '''void KUrl.__init__(KUrl _baseurl, QString _rel_url)'''
    def relativePath(self, base_dir, path, isParent):
        '''static QString KUrl.relativePath(QString base_dir, QString path, bool isParent)'''
        return QString()
    def relativeUrl(self, base_url, url):
        '''static QString KUrl.relativeUrl(KUrl base_url, KUrl url)'''
        return QString()
    def isRelativeUrl(self, _url):
        '''static bool KUrl.isRelativeUrl(QString _url)'''
        return bool()
    def decode_string(self, str):
        '''static QString KUrl.decode_string(QString str)'''
        return QString()
    def encode_string_no_slash(self, str):
        '''static QString KUrl.encode_string_no_slash(QString str)'''
        return QString()
    def encode_string(self, str):
        '''static QString KUrl.encode_string(QString str)'''
        return QString()
    def populateMimeData(self, mimeData, metaData = None, flags = None):
        '''void KUrl.populateMimeData(QMimeData mimeData, dict-of-QString-QString metaData = KUrl.MetaDataMap(), KUrl.MimeDataFlags flags = KUrl.DefaultMimeDataFlags)'''
    def fromMimeDataByteArray(self, str):
        '''static KUrl KUrl.fromMimeDataByteArray(QByteArray str)'''
        return KUrl()
    def fromPathOrUrl(self, text):
        '''static KUrl KUrl.fromPathOrUrl(QString text)'''
        return KUrl()
    def fromPath(self, text):
        '''static KUrl KUrl.fromPath(QString text)'''
        return KUrl()
    def join(self, _list):
        '''static KUrl KUrl.join(KUrl.List _list)'''
        return KUrl()
    def split(self, _url):
        '''static KUrl.List KUrl.split(QString _url)'''
        return KUrl.List()
    def split(self, _url):
        '''static KUrl.List KUrl.split(KUrl _url)'''
        return KUrl.List()
    def isParentOf(self, u):
        '''bool KUrl.isParentOf(KUrl u)'''
        return bool()
    def equals(self, u, options = 0):
        '''bool KUrl.equals(KUrl u, KUrl.EqualsOptions options = 0)'''
        return bool()
    def cmp(self, u, ignore_trailing = False):
        '''bool KUrl.cmp(KUrl u, bool ignore_trailing = False)'''
        return bool()
    def __ne__(self, _u):
        '''bool KUrl.__ne__(KUrl _u)'''
        return bool()
    def __ne__(self, _u):
        '''bool KUrl.__ne__(QString _u)'''
        return bool()
    def __eq__(self, _u):
        '''bool KUrl.__eq__(KUrl _u)'''
        return bool()
    def __eq__(self, _u):
        '''bool KUrl.__eq__(QString _u)'''
        return bool()
    def upUrl(self):
        '''KUrl KUrl.upUrl()'''
        return KUrl()
    def toMimeDataString(self):
        '''QString KUrl.toMimeDataString()'''
        return QString()
    def pathOrUrl(self):
        '''QString KUrl.pathOrUrl()'''
        return QString()
    def pathOrUrl(self, trailing):
        '''QString KUrl.pathOrUrl(KUrl.AdjustPathOption trailing)'''
        return QString()
    def prettyUrl(self, trailing = None):
        '''QString KUrl.prettyUrl(KUrl.AdjustPathOption trailing = KUrl.LeaveTrailingSlash)'''
        return QString()
    def url(self, trailing = None):
        '''QString KUrl.url(KUrl.AdjustPathOption trailing = KUrl.LeaveTrailingSlash)'''
        return QString()
    def cd(self, _dir):
        '''bool KUrl.cd(QString _dir)'''
        return bool()
    def setDirectory(self, dir):
        '''void KUrl.setDirectory(QString dir)'''
    def directory(self, options = None):
        '''QString KUrl.directory(KUrl.DirectoryOptions options = KUrl.IgnoreTrailingSlash)'''
        return QString()
    def fileName(self, options = None):
        '''QString KUrl.fileName(KUrl.DirectoryOptions options = KUrl.IgnoreTrailingSlash)'''
        return QString()
    def setFileName(self, _txt):
        '''void KUrl.setFileName(QString _txt)'''
    def addQueryItem(self, _item, _value):
        '''void KUrl.addQueryItem(QString _item, QString _value)'''
    def queryItem(self, item):
        '''QString KUrl.queryItem(QString item)'''
        return QString()
    def queryItems(self, options = 0):
        '''dict-of-QString-QString KUrl.queryItems(KUrl.QueryItemsOptions options = 0)'''
        return dict-of-QString-QString()
    def addPath(self, txt):
        '''void KUrl.addPath(QString txt)'''
    def hasSubUrl(self):
        '''bool KUrl.hasSubUrl()'''
        return bool()
    def fileEncoding(self):
        '''QString KUrl.fileEncoding()'''
        return QString()
    def setFileEncoding(self, encoding):
        '''void KUrl.setFileEncoding(QString encoding)'''
    def isLocalFile(self):
        '''bool KUrl.isLocalFile()'''
        return bool()
    def hasHTMLRef(self):
        '''bool KUrl.hasHTMLRef()'''
        return bool()
    def setHTMLRef(self, _ref):
        '''void KUrl.setHTMLRef(QString _ref)'''
    def encodedHtmlRef(self):
        '''QString KUrl.encodedHtmlRef()'''
        return QString()
    def htmlRef(self):
        '''QString KUrl.htmlRef()'''
        return QString()
    def hasRef(self):
        '''bool KUrl.hasRef()'''
        return bool()
    def setRef(self, fragment):
        '''void KUrl.setRef(QString fragment)'''
    def ref(self):
        '''QString KUrl.ref()'''
        return QString()
    def query(self):
        '''QString KUrl.query()'''
        return QString()
    def setQuery(self, query):
        '''void KUrl.setQuery(QString query)'''
    def encodedPathAndQuery(self, trailing = None, options = None):
        '''QString KUrl.encodedPathAndQuery(KUrl.AdjustPathOption trailing = KUrl.LeaveTrailingSlash, KUrl.EncodedPathAndQueryOptions options = KUrl.PermitEmptyPath)'''
        return QString()
    def setEncodedPathAndQuery(self, _txt):
        '''void KUrl.setEncodedPathAndQuery(QString _txt)'''
    def adjustPath(self, trailing):
        '''void KUrl.adjustPath(KUrl.AdjustPathOption trailing)'''
    def cleanPath(self, options = None):
        '''void KUrl.cleanPath(KUrl.CleanPathOption options = KUrl.SimplifyDirSeparators)'''
    def hasPath(self):
        '''bool KUrl.hasPath()'''
        return bool()
    def setPath(self, path):
        '''void KUrl.setPath(QString path)'''
    def toLocalFile(self, trailing = None):
        '''QString KUrl.toLocalFile(KUrl.AdjustPathOption trailing = KUrl.LeaveTrailingSlash)'''
        return QString()
    def path(self, trailing = None):
        '''QString KUrl.path(KUrl.AdjustPathOption trailing = KUrl.LeaveTrailingSlash)'''
        return QString()
    def hasHost(self):
        '''bool KUrl.hasHost()'''
        return bool()
    def hasPass(self):
        '''bool KUrl.hasPass()'''
        return bool()
    def setPass(self, pass_):
        '''void KUrl.setPass(QString pass)'''
    def pass_(self):
        '''QString KUrl.pass_()'''
        return QString()
    def hasUser(self):
        '''bool KUrl.hasUser()'''
        return bool()
    def setUser(self, user):
        '''void KUrl.setUser(QString user)'''
    def user(self):
        '''QString KUrl.user()'''
        return QString()
    def setProtocol(self, proto):
        '''void KUrl.setProtocol(QString proto)'''
    def protocol(self):
        '''QString KUrl.protocol()'''
        return QString()
    class CleanPathOptions():
        """"""
        def __init__(self):
            '''KUrl.CleanPathOptions KUrl.CleanPathOptions.__init__()'''
            return KUrl.CleanPathOptions()
        def __init__(self):
            '''int KUrl.CleanPathOptions.__init__()'''
            return int()
        def __init__(self):
            '''void KUrl.CleanPathOptions.__init__()'''
        def __bool__(self):
            '''int KUrl.CleanPathOptions.__bool__()'''
            return int()
        def __ne__(self, f):
            '''bool KUrl.CleanPathOptions.__ne__(KUrl.CleanPathOptions f)'''
            return bool()
        def __eq__(self, f):
            '''bool KUrl.CleanPathOptions.__eq__(KUrl.CleanPathOptions f)'''
            return bool()
        def __invert__(self):
            '''KUrl.CleanPathOptions KUrl.CleanPathOptions.__invert__()'''
            return KUrl.CleanPathOptions()
        def __and__(self, mask):
            '''KUrl.CleanPathOptions KUrl.CleanPathOptions.__and__(int mask)'''
            return KUrl.CleanPathOptions()
        def __xor__(self, f):
            '''KUrl.CleanPathOptions KUrl.CleanPathOptions.__xor__(KUrl.CleanPathOptions f)'''
            return KUrl.CleanPathOptions()
        def __xor__(self, f):
            '''KUrl.CleanPathOptions KUrl.CleanPathOptions.__xor__(int f)'''
            return KUrl.CleanPathOptions()
        def __or__(self, f):
            '''KUrl.CleanPathOptions KUrl.CleanPathOptions.__or__(KUrl.CleanPathOptions f)'''
            return KUrl.CleanPathOptions()
        def __or__(self, f):
            '''KUrl.CleanPathOptions KUrl.CleanPathOptions.__or__(int f)'''
            return KUrl.CleanPathOptions()
        def __int__(self):
            '''int KUrl.CleanPathOptions.__int__()'''
            return int()
        def __ixor__(self, f):
            '''KUrl.CleanPathOptions KUrl.CleanPathOptions.__ixor__(KUrl.CleanPathOptions f)'''
            return KUrl.CleanPathOptions()
        def __ior__(self, f):
            '''KUrl.CleanPathOptions KUrl.CleanPathOptions.__ior__(KUrl.CleanPathOptions f)'''
            return KUrl.CleanPathOptions()
        def __iand__(self, mask):
            '''KUrl.CleanPathOptions KUrl.CleanPathOptions.__iand__(int mask)'''
            return KUrl.CleanPathOptions()
    class EncodedPathAndQueryOptions():
        """"""
        def __init__(self):
            '''KUrl.EncodedPathAndQueryOptions KUrl.EncodedPathAndQueryOptions.__init__()'''
            return KUrl.EncodedPathAndQueryOptions()
        def __init__(self):
            '''int KUrl.EncodedPathAndQueryOptions.__init__()'''
            return int()
        def __init__(self):
            '''void KUrl.EncodedPathAndQueryOptions.__init__()'''
        def __bool__(self):
            '''int KUrl.EncodedPathAndQueryOptions.__bool__()'''
            return int()
        def __ne__(self, f):
            '''bool KUrl.EncodedPathAndQueryOptions.__ne__(KUrl.EncodedPathAndQueryOptions f)'''
            return bool()
        def __eq__(self, f):
            '''bool KUrl.EncodedPathAndQueryOptions.__eq__(KUrl.EncodedPathAndQueryOptions f)'''
            return bool()
        def __invert__(self):
            '''KUrl.EncodedPathAndQueryOptions KUrl.EncodedPathAndQueryOptions.__invert__()'''
            return KUrl.EncodedPathAndQueryOptions()
        def __and__(self, mask):
            '''KUrl.EncodedPathAndQueryOptions KUrl.EncodedPathAndQueryOptions.__and__(int mask)'''
            return KUrl.EncodedPathAndQueryOptions()
        def __xor__(self, f):
            '''KUrl.EncodedPathAndQueryOptions KUrl.EncodedPathAndQueryOptions.__xor__(KUrl.EncodedPathAndQueryOptions f)'''
            return KUrl.EncodedPathAndQueryOptions()
        def __xor__(self, f):
            '''KUrl.EncodedPathAndQueryOptions KUrl.EncodedPathAndQueryOptions.__xor__(int f)'''
            return KUrl.EncodedPathAndQueryOptions()
        def __or__(self, f):
            '''KUrl.EncodedPathAndQueryOptions KUrl.EncodedPathAndQueryOptions.__or__(KUrl.EncodedPathAndQueryOptions f)'''
            return KUrl.EncodedPathAndQueryOptions()
        def __or__(self, f):
            '''KUrl.EncodedPathAndQueryOptions KUrl.EncodedPathAndQueryOptions.__or__(int f)'''
            return KUrl.EncodedPathAndQueryOptions()
        def __int__(self):
            '''int KUrl.EncodedPathAndQueryOptions.__int__()'''
            return int()
        def __ixor__(self, f):
            '''KUrl.EncodedPathAndQueryOptions KUrl.EncodedPathAndQueryOptions.__ixor__(KUrl.EncodedPathAndQueryOptions f)'''
            return KUrl.EncodedPathAndQueryOptions()
        def __ior__(self, f):
            '''KUrl.EncodedPathAndQueryOptions KUrl.EncodedPathAndQueryOptions.__ior__(KUrl.EncodedPathAndQueryOptions f)'''
            return KUrl.EncodedPathAndQueryOptions()
        def __iand__(self, mask):
            '''KUrl.EncodedPathAndQueryOptions KUrl.EncodedPathAndQueryOptions.__iand__(int mask)'''
            return KUrl.EncodedPathAndQueryOptions()
    class List():
        """"""
        # Enum KUrl.List.DecodeOptions
        PreferLocalUrls = 0
        PreferKdeUrls = 0
    
        def __init__(self):
            '''void KUrl.List.__init__()'''
        def __init__(self, url):
            '''void KUrl.List.__init__(KUrl url)'''
        def __init__(self, list):
            '''void KUrl.List.__init__(QStringList list)'''
        def __init__(self, list):
            '''void KUrl.List.__init__(list-of-KUrl list)'''
        def __init__(self):
            '''KUrl.List KUrl.List.__init__()'''
            return KUrl.List()
        def __contains__(self):
            '''KUrl KUrl.List.__contains__()'''
            return KUrl()
        def __ne__(self):
            '''KUrl.List KUrl.List.__ne__()'''
            return KUrl.List()
        def __eq__(self):
            '''KUrl.List KUrl.List.__eq__()'''
            return KUrl.List()
        def __imul__(self):
            '''int KUrl.List.__imul__()'''
            return int()
        def __mul__(self):
            '''int KUrl.List.__mul__()'''
            return int()
        def __iadd__(self):
            '''KUrl.List KUrl.List.__iadd__()'''
            return KUrl.List()
        def __add__(self):
            '''KUrl.List KUrl.List.__add__()'''
            return KUrl.List()
        def __getitem__(self):
            '''int KUrl.List.__getitem__()'''
            return int()
        def __getitem__(self):
            '''slice KUrl.List.__getitem__()'''
            return slice()
        def __delitem__(self):
            '''int KUrl.List.__delitem__()'''
            return int()
        def __delitem__(self):
            '''slice KUrl.List.__delitem__()'''
            return slice()
        def __setitem__(self):
            '''KUrl KUrl.List.__setitem__()'''
            return KUrl()
        def __setitem__(self):
            '''KUrl.List KUrl.List.__setitem__()'''
            return KUrl.List()
        def __len__(self):
            '''int KUrl.List.__len__()'''
            return int()
        def fromMimeData(self, mimeData, metaData = None):
            '''static KUrl.List KUrl.List.fromMimeData(QMimeData mimeData, dict-of-QString-QString metaData = None)'''
            return KUrl.List()
        def fromMimeData(self, mimeData, decodeOptions, metaData = None):
            '''static KUrl.List KUrl.List.fromMimeData(QMimeData mimeData, KUrl.List.DecodeOptions decodeOptions, dict-of-QString-QString metaData = None)'''
            return KUrl.List()
        def mimeDataTypes(self):
            '''static QStringList KUrl.List.mimeDataTypes()'''
            return QStringList()
        def canDecode(self, mimeData):
            '''static bool KUrl.List.canDecode(QMimeData mimeData)'''
            return bool()
        def populateMimeData(self, mimeData, metaData = None, flags = None):
            '''void KUrl.List.populateMimeData(QMimeData mimeData, dict-of-QString-QString metaData = KUrl.MetaDataMap(), KUrl.MimeDataFlags flags = KUrl.DefaultMimeDataFlags)'''
        def populateMimeData(self, mostLocalUrls, mimeData, metaData = None, flags = None):
            '''void KUrl.List.populateMimeData(KUrl.List mostLocalUrls, QMimeData mimeData, dict-of-QString-QString metaData = KUrl.MetaDataMap(), KUrl.MimeDataFlags flags = KUrl.DefaultMimeDataFlags)'''
        def toStringList(self):
            '''QStringList KUrl.List.toStringList()'''
            return QStringList()
        def toStringList(self, trailing):
            '''QStringList KUrl.List.toStringList(KUrl.AdjustPathOption trailing)'''
            return QStringList()
    class EqualsOptions():
        """"""
        def __init__(self):
            '''KUrl.EqualsOptions KUrl.EqualsOptions.__init__()'''
            return KUrl.EqualsOptions()
        def __init__(self):
            '''int KUrl.EqualsOptions.__init__()'''
            return int()
        def __init__(self):
            '''void KUrl.EqualsOptions.__init__()'''
        def __bool__(self):
            '''int KUrl.EqualsOptions.__bool__()'''
            return int()
        def __ne__(self, f):
            '''bool KUrl.EqualsOptions.__ne__(KUrl.EqualsOptions f)'''
            return bool()
        def __eq__(self, f):
            '''bool KUrl.EqualsOptions.__eq__(KUrl.EqualsOptions f)'''
            return bool()
        def __invert__(self):
            '''KUrl.EqualsOptions KUrl.EqualsOptions.__invert__()'''
            return KUrl.EqualsOptions()
        def __and__(self, mask):
            '''KUrl.EqualsOptions KUrl.EqualsOptions.__and__(int mask)'''
            return KUrl.EqualsOptions()
        def __xor__(self, f):
            '''KUrl.EqualsOptions KUrl.EqualsOptions.__xor__(KUrl.EqualsOptions f)'''
            return KUrl.EqualsOptions()
        def __xor__(self, f):
            '''KUrl.EqualsOptions KUrl.EqualsOptions.__xor__(int f)'''
            return KUrl.EqualsOptions()
        def __or__(self, f):
            '''KUrl.EqualsOptions KUrl.EqualsOptions.__or__(KUrl.EqualsOptions f)'''
            return KUrl.EqualsOptions()
        def __or__(self, f):
            '''KUrl.EqualsOptions KUrl.EqualsOptions.__or__(int f)'''
            return KUrl.EqualsOptions()
        def __int__(self):
            '''int KUrl.EqualsOptions.__int__()'''
            return int()
        def __ixor__(self, f):
            '''KUrl.EqualsOptions KUrl.EqualsOptions.__ixor__(KUrl.EqualsOptions f)'''
            return KUrl.EqualsOptions()
        def __ior__(self, f):
            '''KUrl.EqualsOptions KUrl.EqualsOptions.__ior__(KUrl.EqualsOptions f)'''
            return KUrl.EqualsOptions()
        def __iand__(self, mask):
            '''KUrl.EqualsOptions KUrl.EqualsOptions.__iand__(int mask)'''
            return KUrl.EqualsOptions()
    class DirectoryOptions():
        """"""
        def __init__(self):
            '''KUrl.DirectoryOptions KUrl.DirectoryOptions.__init__()'''
            return KUrl.DirectoryOptions()
        def __init__(self):
            '''int KUrl.DirectoryOptions.__init__()'''
            return int()
        def __init__(self):
            '''void KUrl.DirectoryOptions.__init__()'''
        def __bool__(self):
            '''int KUrl.DirectoryOptions.__bool__()'''
            return int()
        def __ne__(self, f):
            '''bool KUrl.DirectoryOptions.__ne__(KUrl.DirectoryOptions f)'''
            return bool()
        def __eq__(self, f):
            '''bool KUrl.DirectoryOptions.__eq__(KUrl.DirectoryOptions f)'''
            return bool()
        def __invert__(self):
            '''KUrl.DirectoryOptions KUrl.DirectoryOptions.__invert__()'''
            return KUrl.DirectoryOptions()
        def __and__(self, mask):
            '''KUrl.DirectoryOptions KUrl.DirectoryOptions.__and__(int mask)'''
            return KUrl.DirectoryOptions()
        def __xor__(self, f):
            '''KUrl.DirectoryOptions KUrl.DirectoryOptions.__xor__(KUrl.DirectoryOptions f)'''
            return KUrl.DirectoryOptions()
        def __xor__(self, f):
            '''KUrl.DirectoryOptions KUrl.DirectoryOptions.__xor__(int f)'''
            return KUrl.DirectoryOptions()
        def __or__(self, f):
            '''KUrl.DirectoryOptions KUrl.DirectoryOptions.__or__(KUrl.DirectoryOptions f)'''
            return KUrl.DirectoryOptions()
        def __or__(self, f):
            '''KUrl.DirectoryOptions KUrl.DirectoryOptions.__or__(int f)'''
            return KUrl.DirectoryOptions()
        def __int__(self):
            '''int KUrl.DirectoryOptions.__int__()'''
            return int()
        def __ixor__(self, f):
            '''KUrl.DirectoryOptions KUrl.DirectoryOptions.__ixor__(KUrl.DirectoryOptions f)'''
            return KUrl.DirectoryOptions()
        def __ior__(self, f):
            '''KUrl.DirectoryOptions KUrl.DirectoryOptions.__ior__(KUrl.DirectoryOptions f)'''
            return KUrl.DirectoryOptions()
        def __iand__(self, mask):
            '''KUrl.DirectoryOptions KUrl.DirectoryOptions.__iand__(int mask)'''
            return KUrl.DirectoryOptions()
    class QueryItemsOptions():
        """"""
        def __init__(self):
            '''KUrl.QueryItemsOptions KUrl.QueryItemsOptions.__init__()'''
            return KUrl.QueryItemsOptions()
        def __init__(self):
            '''int KUrl.QueryItemsOptions.__init__()'''
            return int()
        def __init__(self):
            '''void KUrl.QueryItemsOptions.__init__()'''
        def __bool__(self):
            '''int KUrl.QueryItemsOptions.__bool__()'''
            return int()
        def __ne__(self, f):
            '''bool KUrl.QueryItemsOptions.__ne__(KUrl.QueryItemsOptions f)'''
            return bool()
        def __eq__(self, f):
            '''bool KUrl.QueryItemsOptions.__eq__(KUrl.QueryItemsOptions f)'''
            return bool()
        def __invert__(self):
            '''KUrl.QueryItemsOptions KUrl.QueryItemsOptions.__invert__()'''
            return KUrl.QueryItemsOptions()
        def __and__(self, mask):
            '''KUrl.QueryItemsOptions KUrl.QueryItemsOptions.__and__(int mask)'''
            return KUrl.QueryItemsOptions()
        def __xor__(self, f):
            '''KUrl.QueryItemsOptions KUrl.QueryItemsOptions.__xor__(KUrl.QueryItemsOptions f)'''
            return KUrl.QueryItemsOptions()
        def __xor__(self, f):
            '''KUrl.QueryItemsOptions KUrl.QueryItemsOptions.__xor__(int f)'''
            return KUrl.QueryItemsOptions()
        def __or__(self, f):
            '''KUrl.QueryItemsOptions KUrl.QueryItemsOptions.__or__(KUrl.QueryItemsOptions f)'''
            return KUrl.QueryItemsOptions()
        def __or__(self, f):
            '''KUrl.QueryItemsOptions KUrl.QueryItemsOptions.__or__(int f)'''
            return KUrl.QueryItemsOptions()
        def __int__(self):
            '''int KUrl.QueryItemsOptions.__int__()'''
            return int()
        def __ixor__(self, f):
            '''KUrl.QueryItemsOptions KUrl.QueryItemsOptions.__ixor__(KUrl.QueryItemsOptions f)'''
            return KUrl.QueryItemsOptions()
        def __ior__(self, f):
            '''KUrl.QueryItemsOptions KUrl.QueryItemsOptions.__ior__(KUrl.QueryItemsOptions f)'''
            return KUrl.QueryItemsOptions()
        def __iand__(self, mask):
            '''KUrl.QueryItemsOptions KUrl.QueryItemsOptions.__iand__(int mask)'''
            return KUrl.QueryItemsOptions()


class KUser():
    """"""
    # Enum KUser.UserProperty
    FullName = 0
    RoomNumber = 0
    WorkPhone = 0
    HomePhone = 0

    # Enum KUser.UIDMode
    UseEffectiveUID = 0
    UseRealUserID = 0

    def __init__(self, mode = None):
        '''void KUser.__init__(KUser.UIDMode mode = KUser.UseEffectiveUID)'''
    def __init__(self, uid):
        '''void KUser.__init__(int uid)'''
    def __init__(self, name):
        '''void KUser.__init__(QString name)'''
    def __init__(self, name):
        '''void KUser.__init__(str name)'''
    def __init__(self, user):
        '''void KUser.__init__(KUser user)'''
    def allUserNames(self):
        '''static QStringList KUser.allUserNames()'''
        return QStringList()
    def allUsers(self):
        '''static list-of-KUser KUser.allUsers()'''
        return [KUser()]
    def property(self, which):
        '''QVariant KUser.property(KUser.UserProperty which)'''
        return QVariant()
    def groupNames(self):
        '''QStringList KUser.groupNames()'''
        return QStringList()
    def groups(self):
        '''list-of-KUserGroup KUser.groups()'''
        return [KUserGroup()]
    def shell(self):
        '''QString KUser.shell()'''
        return QString()
    def faceIconPath(self):
        '''QString KUser.faceIconPath()'''
        return QString()
    def homeDir(self):
        '''QString KUser.homeDir()'''
        return QString()
    def fullName(self):
        '''QString KUser.fullName()'''
        return QString()
    def loginName(self):
        '''QString KUser.loginName()'''
        return QString()
    def isSuperUser(self):
        '''bool KUser.isSuperUser()'''
        return bool()
    def gid(self):
        '''int KUser.gid()'''
        return int()
    def uid(self):
        '''int KUser.uid()'''
        return int()
    def isValid(self):
        '''bool KUser.isValid()'''
        return bool()
    def __ne__(self, user):
        '''bool KUser.__ne__(KUser user)'''
        return bool()
    def __eq__(self, user):
        '''bool KUser.__eq__(KUser user)'''
        return bool()


class KUserGroup():
    """"""
    def __init__(self, name):
        '''void KUserGroup.__init__(QString name)'''
    def __init__(self, name):
        '''void KUserGroup.__init__(str name)'''
    def __init__(self, mode = None):
        '''void KUserGroup.__init__(KUser.UIDMode mode = KUser.UseEffectiveUID)'''
    def __init__(self, gid):
        '''void KUserGroup.__init__(int gid)'''
    def __init__(self, group):
        '''void KUserGroup.__init__(KUserGroup group)'''
    def allGroupNames(self):
        '''static QStringList KUserGroup.allGroupNames()'''
        return QStringList()
    def allGroups(self):
        '''static list-of-KUserGroup KUserGroup.allGroups()'''
        return [KUserGroup()]
    def userNames(self):
        '''QStringList KUserGroup.userNames()'''
        return QStringList()
    def users(self):
        '''list-of-KUser KUserGroup.users()'''
        return [KUser()]
    def name(self):
        '''QString KUserGroup.name()'''
        return QString()
    def gid(self):
        '''int KUserGroup.gid()'''
        return int()
    def isValid(self):
        '''bool KUserGroup.isValid()'''
        return bool()
    def __ne__(self, group):
        '''bool KUserGroup.__ne__(KUserGroup group)'''
        return bool()
    def __eq__(self, group):
        '''bool KUserGroup.__eq__(KUserGroup group)'''
        return bool()


class Sonnet():
    """"""
    def defaultLanguageName(self):
        '''static QString Sonnet.defaultLanguageName()'''
        return QString()
    def detectLanguage(self, sentence):
        '''static QString Sonnet.detectLanguage(QString sentence)'''
        return QString()
    class Speller():
        """"""
        # Enum Sonnet.Speller.Attribute
        CheckUppercase = 0
        SkipRunTogether = 0
    
        def __init__(self, lang = QString()):
            '''void Sonnet.Speller.__init__(QString lang = QString())'''
        def __init__(self, speller):
            '''void Sonnet.Speller.__init__(Sonnet.Speller speller)'''
        def testAttribute(self, attr):
            '''bool Sonnet.Speller.testAttribute(Sonnet.Speller.Attribute attr)'''
            return bool()
        def setAttribute(self, attr, b = True):
            '''void Sonnet.Speller.setAttribute(Sonnet.Speller.Attribute attr, bool b = True)'''
        def defaultClient(self):
            '''QString Sonnet.Speller.defaultClient()'''
            return QString()
        def setDefaultClient(self, client):
            '''void Sonnet.Speller.setDefaultClient(QString client)'''
        def defaultLanguage(self):
            '''QString Sonnet.Speller.defaultLanguage()'''
            return QString()
        def setDefaultLanguage(self, lang):
            '''void Sonnet.Speller.setDefaultLanguage(QString lang)'''
        def availableDictionaries(self):
            '''dict-of-QString-QString Sonnet.Speller.availableDictionaries()'''
            return dict-of-QString-QString()
        def availableLanguageNames(self):
            '''QStringList Sonnet.Speller.availableLanguageNames()'''
            return QStringList()
        def availableLanguages(self):
            '''QStringList Sonnet.Speller.availableLanguages()'''
            return QStringList()
        def availableBackends(self):
            '''QStringList Sonnet.Speller.availableBackends()'''
            return QStringList()
        def restore(self, config):
            '''void Sonnet.Speller.restore(KConfig config)'''
        def save(self, config):
            '''void Sonnet.Speller.save(KConfig config)'''
        def addToSession(self, word):
            '''bool Sonnet.Speller.addToSession(QString word)'''
            return bool()
        def addToPersonal(self, word):
            '''bool Sonnet.Speller.addToPersonal(QString word)'''
            return bool()
        def storeReplacement(self, bad, good):
            '''bool Sonnet.Speller.storeReplacement(QString bad, QString good)'''
            return bool()
        def checkAndSuggest(self, word, suggestions):
            '''bool Sonnet.Speller.checkAndSuggest(QString word, QStringList suggestions)'''
            return bool()
        def suggest(self, word):
            '''QStringList Sonnet.Speller.suggest(QString word)'''
            return QStringList()
        def isMisspelled(self, word):
            '''bool Sonnet.Speller.isMisspelled(QString word)'''
            return bool()
        def isCorrect(self, word):
            '''bool Sonnet.Speller.isCorrect(QString word)'''
            return bool()
        def language(self):
            '''QString Sonnet.Speller.language()'''
            return QString()
        def setLanguage(self, lang):
            '''void Sonnet.Speller.setLanguage(QString lang)'''
        def isValid(self):
            '''bool Sonnet.Speller.isValid()'''
            return bool()
    class BackgroundChecker(QObject):
        """"""
        def __init__(self, parent = None):
            '''void Sonnet.BackgroundChecker.__init__(QObject parent = None)'''
        def __init__(self, speller, parent = None):
            '''void Sonnet.BackgroundChecker.__init__(Sonnet.Speller speller, QObject parent = None)'''
        def restore(self, config):
            '''void Sonnet.BackgroundChecker.restore(KConfig config)'''
        def slotEngineDone(self):
            '''void Sonnet.BackgroundChecker.slotEngineDone()'''
        def finishedCurrentFeed(self):
            '''void Sonnet.BackgroundChecker.finishedCurrentFeed()'''
        def fetchMoreText(self):
            '''QString Sonnet.BackgroundChecker.fetchMoreText()'''
            return QString()
        done = pyqtSignal() # void done() - signal
        misspelling = pyqtSignal() # void misspelling(const QStringamp;,int) - signal
        def continueChecking(self):
            '''void Sonnet.BackgroundChecker.continueChecking()'''
        def changeLanguage(self, lang):
            '''void Sonnet.BackgroundChecker.changeLanguage(QString lang)'''
        def replace(self, start, oldText, newText):
            '''void Sonnet.BackgroundChecker.replace(int start, QString oldText, QString newText)'''
        def stop(self):
            '''void Sonnet.BackgroundChecker.stop()'''
        def start(self):
            '''void Sonnet.BackgroundChecker.start()'''
        def addWordToPersonal(self, word):
            '''bool Sonnet.BackgroundChecker.addWordToPersonal(QString word)'''
            return bool()
        def suggest(self, word):
            '''QStringList Sonnet.BackgroundChecker.suggest(QString word)'''
            return QStringList()
        def checkWord(self, word):
            '''bool Sonnet.BackgroundChecker.checkWord(QString word)'''
            return bool()
        def setSpeller(self, speller):
            '''void Sonnet.BackgroundChecker.setSpeller(Sonnet.Speller speller)'''
        def speller(self):
            '''Sonnet.Speller Sonnet.BackgroundChecker.speller()'''
            return Sonnet.Speller()
        def currentContext(self):
            '''QString Sonnet.BackgroundChecker.currentContext()'''
            return QString()
        def text(self):
            '''QString Sonnet.BackgroundChecker.text()'''
            return QString()
        def setText(self, text):
            '''void Sonnet.BackgroundChecker.setText(QString text)'''


# Enum KSycocaFactoryId
KST_KServiceFactory = 0
KST_KServiceTypeFactory = 0
KST_KServiceGroupFactory = 0
KST_KImageIO = 0
KST_KProtocolInfoFactory = 0
KST_KMimeTypeFactory = 0
KST_CTimeInfo = 0


# Enum KSycocaType
KST_KSycocaEntry = 0
KST_KService = 0
KST_KServiceType = 0
KST_KMimeType = 0
KST_KFolderMimeType = 0
KST_KDEDesktopMimeType = 0
KST_KMimeTypeEntry = 0
KST_KServiceGroup = 0
KST_KImageIOFormat = 0
KST_KProtocolInfo = 0
KST_KServiceSeparator = 0
KST_KCustom = 0


def urlcmp(_url1, _url2):
    '''static bool urlcmp(QString _url1, QString _url2)'''
    return bool()

def urlcmp(_url1, _url2, options):
    '''static bool urlcmp(QString _url1, QString _url2, KUrl.EqualsOptions options)'''
    return bool()

def qHash():
    '''static KPluginInfo qHash()'''
    return KPluginInfo()

def qHash(kurl):
    '''static int qHash(KUrl kurl)'''
    return int()

def i18ncp(ctxt, sing, plur, *args):
    '''static QString i18ncp(str ctxt, str sing, str plur, ... *args)'''
    return QString()

def i18np(sing, plur, *args):
    '''static QString i18np(str sing, str plur, ... *args)'''
    return QString()

def i18nc(ctxt, text, *args):
    '''static QString i18nc(str ctxt, str text, ... *args)'''
    return QString()

def i18n(text, *args):
    '''static QString i18n(str text, ... *args)'''
    return QString()

def tr2i18n(message, comment = None):
    '''static QString tr2i18n(str message, str comment = None)'''
    return QString()

def ki18ncp(ctxt, singular, plural):
    '''static KLocalizedString ki18ncp(str ctxt, str singular, str plural)'''
    return KLocalizedString()

def ki18np(singular, plural):
    '''static KLocalizedString ki18np(str singular, str plural)'''
    return KLocalizedString()

def ki18nc(ctxt, msg):
    '''static KLocalizedString ki18nc(str ctxt, str msg)'''
    return KLocalizedString()

def ki18n(msg):
    '''static KLocalizedString ki18n(str msg)'''
    return KLocalizedString()

def kAsciiToUpper(str):
    '''static str kAsciiToUpper(str str)'''
    return str()

def kAsciiToLower(str):
    '''static str kAsciiToLower(str str)'''
    return str()

def kasciistricmp(str1, str2):
    '''static int kasciistricmp(str str1, str str2)'''
    return int()

def pykde_versionString():
    '''static str pykde_versionString()'''
    return str()

def pykde_versionRelease():
    '''static int pykde_versionRelease()'''
    return int()

def pykde_versionMinor():
    '''static int pykde_versionMinor()'''
    return int()

def pykde_versionMajor():
    '''static int pykde_versionMajor()'''
    return int()

def pykde_version():
    '''static int pykde_version()'''
    return int()

def versionString():
    '''static str versionString()'''
    return str()

def versionRelease():
    '''static int versionRelease()'''
    return int()

def versionMinor():
    '''static int versionMinor()'''
    return int()

def versionMajor():
    '''static int versionMajor()'''
    return int()

def version():
    '''static int version()'''
    return int()

