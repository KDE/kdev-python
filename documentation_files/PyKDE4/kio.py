class pyqtSignal():
 def connect(self, targetSignal): pass
 def emit(self, *args): pass
from QtCore import *

class KIO():
    """"""
    # Enum KIO.Message
    MSG_DATA = 0
    MSG_DATA_REQ = 0
    MSG_ERROR = 0
    MSG_CONNECTED = 0
    MSG_FINISHED = 0
    MSG_STAT_ENTRY = 0
    MSG_LIST_ENTRIES = 0
    MSG_RENAMED = 0
    MSG_RESUME = 0
    MSG_SLAVE_STATUS = 0
    MSG_SLAVE_ACK = 0
    MSG_NET_REQUEST = 0
    MSG_NET_DROP = 0
    MSG_NEED_SUBURL_DATA = 0
    MSG_CANRESUME = 0
    MSG_AUTH_KEY = 0
    MSG_DEL_AUTH_KEY = 0
    MSG_OPENED = 0
    MSG_WRITTEN = 0
    MSG_HOST_INFO_REQ = 0

    # Enum KIO.Info
    INF_TOTAL_SIZE = 0
    INF_PROCESSED_SIZE = 0
    INF_SPEED = 0
    INF_REDIRECTION = 0
    INF_MIME_TYPE = 0
    INF_ERROR_PAGE = 0
    INF_WARNING = 0
    INF_GETTING_FILE = 0
    INF_UNUSED = 0
    INF_INFOMESSAGE = 0
    INF_META_DATA = 0
    INF_NETWORK_STATUS = 0
    INF_MESSAGEBOX = 0
    INF_POSITION = 0

    # Enum KIO.SkipDialog_Result
    S_SKIP = 0
    S_AUTO_SKIP = 0
    S_CANCEL = 0

    # Enum KIO.RenameDialog_Result
    R_RESUME = 0
    R_RESUME_ALL = 0
    R_OVERWRITE = 0
    R_OVERWRITE_ALL = 0
    R_SKIP = 0
    R_AUTO_SKIP = 0
    R_RENAME = 0
    R_AUTO_RENAME = 0
    R_CANCEL = 0

    # Enum KIO.RenameDialog_Mode
    M_OVERWRITE = 0
    M_OVERWRITE_ITSELF = 0
    M_SKIP = 0
    M_SINGLE = 0
    M_MULTI = 0
    M_RESUME = 0
    M_NORENAME = 0
    M_ISDIR = 0

    # Enum KIO.JobFlag
    DefaultFlags = 0
    HideProgressInfo = 0
    Resume = 0
    Overwrite = 0

    # Enum KIO.LoadType
    Reload = 0
    NoReload = 0

    # Enum KIO.CacheControl
    CC_CacheOnly = 0
    CC_Cache = 0
    CC_Verify = 0
    CC_Refresh = 0
    CC_Reload = 0

    # Enum KIO.Error
    ERR_CANNOT_OPEN_FOR_READING = 0
    ERR_CANNOT_OPEN_FOR_WRITING = 0
    ERR_CANNOT_LAUNCH_PROCESS = 0
    ERR_INTERNAL = 0
    ERR_MALFORMED_URL = 0
    ERR_UNSUPPORTED_PROTOCOL = 0
    ERR_NO_SOURCE_PROTOCOL = 0
    ERR_UNSUPPORTED_ACTION = 0
    ERR_IS_DIRECTORY = 0
    ERR_IS_FILE = 0
    ERR_DOES_NOT_EXIST = 0
    ERR_FILE_ALREADY_EXIST = 0
    ERR_DIR_ALREADY_EXIST = 0
    ERR_UNKNOWN_HOST = 0
    ERR_ACCESS_DENIED = 0
    ERR_WRITE_ACCESS_DENIED = 0
    ERR_CANNOT_ENTER_DIRECTORY = 0
    ERR_PROTOCOL_IS_NOT_A_FILESYSTEM = 0
    ERR_CYCLIC_LINK = 0
    ERR_USER_CANCELED = 0
    ERR_CYCLIC_COPY = 0
    ERR_COULD_NOT_CREATE_SOCKET = 0
    ERR_COULD_NOT_CONNECT = 0
    ERR_CONNECTION_BROKEN = 0
    ERR_NOT_FILTER_PROTOCOL = 0
    ERR_COULD_NOT_MOUNT = 0
    ERR_COULD_NOT_UNMOUNT = 0
    ERR_COULD_NOT_READ = 0
    ERR_COULD_NOT_WRITE = 0
    ERR_COULD_NOT_BIND = 0
    ERR_COULD_NOT_LISTEN = 0
    ERR_COULD_NOT_ACCEPT = 0
    ERR_COULD_NOT_LOGIN = 0
    ERR_COULD_NOT_STAT = 0
    ERR_COULD_NOT_CLOSEDIR = 0
    ERR_COULD_NOT_MKDIR = 0
    ERR_COULD_NOT_RMDIR = 0
    ERR_CANNOT_RESUME = 0
    ERR_CANNOT_RENAME = 0
    ERR_CANNOT_CHMOD = 0
    ERR_CANNOT_DELETE = 0
    ERR_SLAVE_DIED = 0
    ERR_OUT_OF_MEMORY = 0
    ERR_UNKNOWN_PROXY_HOST = 0
    ERR_COULD_NOT_AUTHENTICATE = 0
    ERR_ABORTED = 0
    ERR_INTERNAL_SERVER = 0
    ERR_SERVER_TIMEOUT = 0
    ERR_SERVICE_NOT_AVAILABLE = 0
    ERR_UNKNOWN = 0
    ERR_UNKNOWN_INTERRUPT = 0
    ERR_CANNOT_DELETE_ORIGINAL = 0
    ERR_CANNOT_DELETE_PARTIAL = 0
    ERR_CANNOT_RENAME_ORIGINAL = 0
    ERR_CANNOT_RENAME_PARTIAL = 0
    ERR_NEED_PASSWD = 0
    ERR_CANNOT_SYMLINK = 0
    ERR_NO_CONTENT = 0
    ERR_DISK_FULL = 0
    ERR_IDENTICAL_FILES = 0
    ERR_SLAVE_DEFINED = 0
    ERR_UPGRADE_REQUIRED = 0
    ERR_POST_DENIED = 0
    ERR_COULD_NOT_SEEK = 0
    ERR_CANNOT_SETTIME = 0
    ERR_CANNOT_CHOWN = 0
    ERR_POST_NO_SIZE = 0

    # Enum KIO.Command
    CMD_HOST = 0
    CMD_CONNECT = 0
    CMD_DISCONNECT = 0
    CMD_SLAVE_STATUS = 0
    CMD_SLAVE_CONNECT = 0
    CMD_SLAVE_HOLD = 0
    CMD_NONE = 0
    CMD_TESTDIR = 0
    CMD_GET = 0
    CMD_PUT = 0
    CMD_STAT = 0
    CMD_MIMETYPE = 0
    CMD_LISTDIR = 0
    CMD_MKDIR = 0
    CMD_RENAME = 0
    CMD_COPY = 0
    CMD_DEL = 0
    CMD_CHMOD = 0
    CMD_SPECIAL = 0
    CMD_SETMODIFICATIONTIME = 0
    CMD_REPARSECONFIGURATION = 0
    CMD_META_DATA = 0
    CMD_SYMLINK = 0
    CMD_SUBURL = 0
    CMD_MESSAGEBOXANSWER = 0
    CMD_RESUMEANSWER = 0
    CMD_CONFIG = 0
    CMD_MULTI_GET = 0
    CMD_SETLINKDEST = 0
    CMD_OPEN = 0
    CMD_CHOWN = 0
    CMD_READ = 0
    CMD_WRITE = 0
    CMD_SEEK = 0
    CMD_CLOSE = 0
    CMD_HOST_INFO = 0

    def filePreview(self, items, width, height = 0, iconSize = 0, iconAlpha = 70, scale = True, save = True, enabledPlugins = None):
        '''static KIO.PreviewJob KIO.filePreview(KFileItemList items, int width, int height = 0, int iconSize = 0, int iconAlpha = 70, bool scale = True, bool save = True, QStringList enabledPlugins = None)'''
        return KIO.PreviewJob()
    def filePreview(self, items, width, height = 0, iconSize = 0, iconAlpha = 70, scale = True, save = True, enabledPlugins = None):
        '''static KIO.PreviewJob KIO.filePreview(KUrl.List items, int width, int height = 0, int iconSize = 0, int iconAlpha = 70, bool scale = True, bool save = True, QStringList enabledPlugins = None)'''
        return KIO.PreviewJob()
    def filePreview(self, items, size, enabledPlugins = None):
        '''static KIO.PreviewJob KIO.filePreview(KFileItemList items, QSize size, QStringList enabledPlugins = None)'''
        return KIO.PreviewJob()
    def pasteMimeData(self, data, destUrl, dialogText, widget):
        '''static KIO.Job KIO.pasteMimeData(QMimeData data, KUrl destUrl, QString dialogText, QWidget widget)'''
        return KIO.Job()
    def pasteActionText(self):
        '''static QString KIO.pasteActionText()'''
        return QString()
    def canPasteMimeSource(self, data):
        '''static bool KIO.canPasteMimeSource(QMimeData data)'''
        return bool()
    def pasteMimeSource(self, data, destURL, dialogText, widget, clipboard = False):
        '''static KIO.CopyJob KIO.pasteMimeSource(QMimeData data, KUrl destURL, QString dialogText, QWidget widget, bool clipboard = False)'''
        return KIO.CopyJob()
    def pasteDataAsync(self, destURL, data, widget, dialogText = QString()):
        '''static KIO.CopyJob KIO.pasteDataAsync(KUrl destURL, QByteArray data, QWidget widget, QString dialogText = QString())'''
        return KIO.CopyJob()
    def pasteData(self, destURL, data, widget):
        '''static void KIO.pasteData(KUrl destURL, QByteArray data, QWidget widget)'''
    def pasteClipboard(self, destURL, widget, move = False):
        '''static KIO.Job KIO.pasteClipboard(KUrl destURL, QWidget widget, bool move = False)'''
        return KIO.Job()
    def fileMetaInfo(self, items):
        '''static KIO.MetaInfoJob KIO.fileMetaInfo(KFileItemList items)'''
        return KIO.MetaInfoJob()
    def fileMetaInfo(self, items):
        '''static KIO.MetaInfoJob KIO.fileMetaInfo(KUrl.List items)'''
        return KIO.MetaInfoJob()
    def http_delete(self, url, flags = None):
        '''static KIO.TransferJob KIO.http_delete(KUrl url, KIO.JobFlags flags = KIO.DefaultFlags)'''
        return KIO.TransferJob()
    def mostLocalUrl(self, url, flags = None):
        '''static KIO.StatJob KIO.mostLocalUrl(KUrl url, KIO.JobFlags flags = KIO.DefaultFlags)'''
        return KIO.StatJob()
    def listRecursive(self, url, flags = None, includeHidden = True):
        '''static KIO.ListJob KIO.listRecursive(KUrl url, KIO.JobFlags flags = KIO.DefaultFlags, bool includeHidden = True)'''
        return KIO.ListJob()
    def listDir(self, url, flags = None, includeHidden = True):
        '''static KIO.ListJob KIO.listDir(KUrl url, KIO.JobFlags flags = KIO.DefaultFlags, bool includeHidden = True)'''
        return KIO.ListJob()
    def file_delete(self, src, flags = None):
        '''static KIO.SimpleJob KIO.file_delete(KUrl src, KIO.JobFlags flags = KIO.DefaultFlags)'''
        return KIO.SimpleJob()
    def file_move(self, src, dest, permissions = None, flags = None):
        '''static KIO.FileCopyJob KIO.file_move(KUrl src, KUrl dest, int permissions = -1, KIO.JobFlags flags = KIO.DefaultFlags)'''
        return KIO.FileCopyJob()
    def file_copy(self, src, dest, permissions = None, flags = None):
        '''static KIO.FileCopyJob KIO.file_copy(KUrl src, KUrl dest, int permissions = -1, KIO.JobFlags flags = KIO.DefaultFlags)'''
        return KIO.FileCopyJob()
    def mimetype(self, url, flags = None):
        '''static KIO.MimetypeJob KIO.mimetype(KUrl url, KIO.JobFlags flags = KIO.DefaultFlags)'''
        return KIO.MimetypeJob()
    def multi_get(self, id, url, metaData):
        '''static KIO.MultiGetJob KIO.multi_get(int id, KUrl url, MetaData metaData)'''
        return KIO.MultiGetJob()
    def storedHttpPost(self, arr, url, flags = None):
        '''static KIO.StoredTransferJob KIO.storedHttpPost(QByteArray arr, KUrl url, KIO.JobFlags flags = KIO.DefaultFlags)'''
        return KIO.StoredTransferJob()
    def storedHttpPost(self, device, url, size = None, flags = None):
        '''static KIO.StoredTransferJob KIO.storedHttpPost(QIODevice device, KUrl url, int size = -1, KIO.JobFlags flags = KIO.DefaultFlags)'''
        return KIO.StoredTransferJob()
    def storedPut(self, arr, url, permissions, flags = None):
        '''static KIO.StoredTransferJob KIO.storedPut(QByteArray arr, KUrl url, int permissions, KIO.JobFlags flags = KIO.DefaultFlags)'''
        return KIO.StoredTransferJob()
    def storedGet(self, url, reload = None, flags = None):
        '''static KIO.StoredTransferJob KIO.storedGet(KUrl url, KIO.LoadType reload = KIO.NoReload, KIO.JobFlags flags = KIO.DefaultFlags)'''
        return KIO.StoredTransferJob()
    def http_post(self, url, postData, flags = None):
        '''static KIO.TransferJob KIO.http_post(KUrl url, QByteArray postData, KIO.JobFlags flags = KIO.DefaultFlags)'''
        return KIO.TransferJob()
    def http_post(self, url, device, size = None, flags = None):
        '''static KIO.TransferJob KIO.http_post(KUrl url, QIODevice device, int size = -1, KIO.JobFlags flags = KIO.DefaultFlags)'''
        return KIO.TransferJob()
    def put(self, url, permissions, flags = None):
        '''static KIO.TransferJob KIO.put(KUrl url, int permissions, KIO.JobFlags flags = KIO.DefaultFlags)'''
        return KIO.TransferJob()
    def open(self, url, mode):
        '''static KIO.FileJob KIO.open(KUrl url, QIODevice.OpenMode mode)'''
        return KIO.FileJob()
    def get(self, url, reload = None, flags = None):
        '''static KIO.TransferJob KIO.get(KUrl url, KIO.LoadType reload = KIO.NoReload, KIO.JobFlags flags = KIO.DefaultFlags)'''
        return KIO.TransferJob()
    def stat(self, url, flags = None):
        '''static KIO.StatJob KIO.stat(KUrl url, KIO.JobFlags flags = KIO.DefaultFlags)'''
        return KIO.StatJob()
    def stat(self, url, side, details, flags = None):
        '''static KIO.StatJob KIO.stat(KUrl url, KIO.StatJob.StatSide side, int details, KIO.JobFlags flags = KIO.DefaultFlags)'''
        return KIO.StatJob()
    def stat(self, url, sideIsSource, details, flags = None):
        '''static KIO.StatJob KIO.stat(KUrl url, bool sideIsSource, int details, KIO.JobFlags flags = KIO.DefaultFlags)'''
        return KIO.StatJob()
    def http_update_cache(self, url, no_cache, expireDate):
        '''static KIO.SimpleJob KIO.http_update_cache(KUrl url, bool no_cache, int expireDate)'''
        return KIO.SimpleJob()
    def unmount(self, point, flags = None):
        '''static KIO.SimpleJob KIO.unmount(QString point, KIO.JobFlags flags = KIO.DefaultFlags)'''
        return KIO.SimpleJob()
    def mount(self, ro, fstype, dev, point, flags = None):
        '''static KIO.SimpleJob KIO.mount(bool ro, QByteArray fstype, QString dev, QString point, KIO.JobFlags flags = KIO.DefaultFlags)'''
        return KIO.SimpleJob()
    def special(self, url, data, flags = None):
        '''static KIO.SimpleJob KIO.special(KUrl url, QByteArray data, KIO.JobFlags flags = KIO.DefaultFlags)'''
        return KIO.SimpleJob()
    def symlink(self, target, dest, flags = None):
        '''static KIO.SimpleJob KIO.symlink(QString target, KUrl dest, KIO.JobFlags flags = KIO.DefaultFlags)'''
        return KIO.SimpleJob()
    def rename(self, src, dest, flags = None):
        '''static KIO.SimpleJob KIO.rename(KUrl src, KUrl dest, KIO.JobFlags flags = KIO.DefaultFlags)'''
        return KIO.SimpleJob()
    def setModificationTime(self, url, mtime):
        '''static KIO.SimpleJob KIO.setModificationTime(KUrl url, QDateTime mtime)'''
        return KIO.SimpleJob()
    def chown(self, url, owner, group):
        '''static KIO.SimpleJob KIO.chown(KUrl url, QString owner, QString group)'''
        return KIO.SimpleJob()
    def rmdir(self, url):
        '''static KIO.SimpleJob KIO.rmdir(KUrl url)'''
        return KIO.SimpleJob()
    def mkdir(self, url, permissions = None):
        '''static KIO.SimpleJob KIO.mkdir(KUrl url, int permissions = -1)'''
        return KIO.SimpleJob()
    def getJobTracker(self):
        '''static KJobTrackerInterface KIO.getJobTracker()'''
        return KJobTrackerInterface()
    def getCacheControlString(self, cacheControl):
        '''static QString KIO.getCacheControlString(KIO.CacheControl cacheControl)'''
        return QString()
    def parseCacheControl(self, cacheControl):
        '''static KIO.CacheControl KIO.parseCacheControl(QString cacheControl)'''
        return KIO.CacheControl()
    def unsupportedActionErrorString(self, protocol, cmd):
        '''static QString KIO.unsupportedActionErrorString(QString protocol, int cmd)'''
        return QString()
    def rawErrorDetail(self, errorCode, errorText, reqUrl = None, method = None):
        '''static QByteArray KIO.rawErrorDetail(int errorCode, QString errorText, KUrl reqUrl = None, int method = -1)'''
        return QByteArray()
    def buildErrorString(self, errorCode, errorText):
        '''static QString KIO.buildErrorString(int errorCode, QString errorText)'''
        return QString()
    def decodeFileName(self, str):
        '''static QString KIO.decodeFileName(QString str)'''
        return QString()
    def encodeFileName(self, str):
        '''static QString KIO.encodeFileName(QString str)'''
        return QString()
    def itemsSummaryString(self, items, files, dirs, size, showSize):
        '''static QString KIO.itemsSummaryString(int items, int files, int dirs, int size, bool showSize)'''
        return QString()
    def calculateRemaining(self, totalSize, processedSize, speed):
        '''static QTime KIO.calculateRemaining(int totalSize, int processedSize, int speed)'''
        return QTime()
    def convertSeconds(self, seconds):
        '''static QString KIO.convertSeconds(int seconds)'''
        return QString()
    def calculateRemainingSeconds(self, totalSize, processedSize, speed):
        '''static int KIO.calculateRemainingSeconds(int totalSize, int processedSize, int speed)'''
        return int()
    def convertSizeFromKiB(self, kibSize):
        '''static QString KIO.convertSizeFromKiB(int kibSize)'''
        return QString()
    def number(self, size):
        '''static QString KIO.number(int size)'''
        return QString()
    def convertSize(self, size):
        '''static QString KIO.convertSize(int size)'''
        return QString()
    def directorySize(self, directory):
        '''static KIO.DirectorySizeJob KIO.directorySize(KUrl directory)'''
        return KIO.DirectorySizeJob()
    def directorySize(self, lstItems):
        '''static KIO.DirectorySizeJob KIO.directorySize(KFileItemList lstItems)'''
        return KIO.DirectorySizeJob()
    def del_(self, src, flags = None):
        '''static KIO.DeleteJob KIO.del_(KUrl src, KIO.JobFlags flags = KIO.DefaultFlags)'''
        return KIO.DeleteJob()
    def del_(self, src, flags = None):
        '''static KIO.DeleteJob KIO.del_(KUrl.List src, KIO.JobFlags flags = KIO.DefaultFlags)'''
        return KIO.DeleteJob()
    def davReport(self, url, report, depth, flags = None):
        '''static KIO.DavJob KIO.davReport(KUrl url, QString report, QString depth, KIO.JobFlags flags = KIO.DefaultFlags)'''
        return KIO.DavJob()
    def davSearch(self, url, nsURI, qName, query, flags = None):
        '''static KIO.DavJob KIO.davSearch(KUrl url, QString nsURI, QString qName, QString query, KIO.JobFlags flags = KIO.DefaultFlags)'''
        return KIO.DavJob()
    def davPropPatch(self, url, properties, flags = None):
        '''static KIO.DavJob KIO.davPropPatch(KUrl url, QDomDocument properties, KIO.JobFlags flags = KIO.DefaultFlags)'''
        return KIO.DavJob()
    def davPropFind(self, url, properties, depth, flags = None):
        '''static KIO.DavJob KIO.davPropFind(KUrl url, QDomDocument properties, QString depth, KIO.JobFlags flags = KIO.DefaultFlags)'''
        return KIO.DavJob()
    def trash(self, src, flags = None):
        '''static KIO.CopyJob KIO.trash(KUrl src, KIO.JobFlags flags = KIO.DefaultFlags)'''
        return KIO.CopyJob()
    def trash(self, src, flags = None):
        '''static KIO.CopyJob KIO.trash(KUrl.List src, KIO.JobFlags flags = KIO.DefaultFlags)'''
        return KIO.CopyJob()
    def linkAs(self, src, dest, flags = None):
        '''static KIO.CopyJob KIO.linkAs(KUrl src, KUrl dest, KIO.JobFlags flags = KIO.DefaultFlags)'''
        return KIO.CopyJob()
    def link(self, src, destDir, flags = None):
        '''static KIO.CopyJob KIO.link(KUrl src, KUrl destDir, KIO.JobFlags flags = KIO.DefaultFlags)'''
        return KIO.CopyJob()
    def link(self, src, destDir, flags = None):
        '''static KIO.CopyJob KIO.link(KUrl.List src, KUrl destDir, KIO.JobFlags flags = KIO.DefaultFlags)'''
        return KIO.CopyJob()
    def moveAs(self, src, dest, flags = None):
        '''static KIO.CopyJob KIO.moveAs(KUrl src, KUrl dest, KIO.JobFlags flags = KIO.DefaultFlags)'''
        return KIO.CopyJob()
    def move(self, src, dest, flags = None):
        '''static KIO.CopyJob KIO.move(KUrl src, KUrl dest, KIO.JobFlags flags = KIO.DefaultFlags)'''
        return KIO.CopyJob()
    def move(self, src, dest, flags = None):
        '''static KIO.CopyJob KIO.move(KUrl.List src, KUrl dest, KIO.JobFlags flags = KIO.DefaultFlags)'''
        return KIO.CopyJob()
    def copyAs(self, src, dest, flags = None):
        '''static KIO.CopyJob KIO.copyAs(KUrl src, KUrl dest, KIO.JobFlags flags = KIO.DefaultFlags)'''
        return KIO.CopyJob()
    def copy(self, src, dest, flags = None):
        '''static KIO.CopyJob KIO.copy(KUrl src, KUrl dest, KIO.JobFlags flags = KIO.DefaultFlags)'''
        return KIO.CopyJob()
    def copy(self, src, dest, flags = None):
        '''static KIO.CopyJob KIO.copy(KUrl.List src, KUrl dest, KIO.JobFlags flags = KIO.DefaultFlags)'''
        return KIO.CopyJob()
    def chmod(self, lstItems, permissions, mask, newOwner, newGroup, recursive, flags = None):
        '''static KIO.ChmodJob KIO.chmod(KFileItemList lstItems, int permissions, int mask, QString newOwner, QString newGroup, bool recursive, KIO.JobFlags flags = KIO.DefaultFlags)'''
        return KIO.ChmodJob()
    def chmod(self, url, permissions):
        '''static KIO.SimpleJob KIO.chmod(KUrl url, int permissions)'''
        return KIO.SimpleJob()
    class Connection(QObject):
        """"""
        def __init__(self, parent = None):
            '''void KIO.Connection.__init__(QObject parent = None)'''
        readyRead = pyqtSignal() # void readyRead() - signal
        def suspended(self):
            '''bool KIO.Connection.suspended()'''
            return bool()
        def resume(self):
            '''void KIO.Connection.resume()'''
        def suspend(self):
            '''void KIO.Connection.suspend()'''
        def waitForIncomingTask(self, ms = 30000):
            '''bool KIO.Connection.waitForIncomingTask(int ms = 30000)'''
            return bool()
        def hasTaskAvailable(self):
            '''bool KIO.Connection.hasTaskAvailable()'''
            return bool()
        def sendnow(self, _cmd, data):
            '''bool KIO.Connection.sendnow(int _cmd, QByteArray data)'''
            return bool()
        def send(self, cmd, arr = QByteArray()):
            '''bool KIO.Connection.send(int cmd, QByteArray arr = QByteArray())'''
            return bool()
        def inited(self):
            '''bool KIO.Connection.inited()'''
            return bool()
        def isConnected(self):
            '''bool KIO.Connection.isConnected()'''
            return bool()
        def errorString(self):
            '''QString KIO.Connection.errorString()'''
            return QString()
        def close(self):
            '''void KIO.Connection.close()'''
        def connectToRemote(self, address):
            '''void KIO.Connection.connectToRemote(QString address)'''
    class UDSEntry():
        """"""
        # Enum KIO.UDSEntry.StandardFieldTypes
        UDS_STRING = 0
        UDS_NUMBER = 0
        UDS_TIME = 0
        UDS_SIZE = 0
        UDS_SIZE_LARGE = 0
        UDS_USER = 0
        UDS_ICON_NAME = 0
        UDS_GROUP = 0
        UDS_NAME = 0
        UDS_LOCAL_PATH = 0
        UDS_HIDDEN = 0
        UDS_ACCESS = 0
        UDS_MODIFICATION_TIME = 0
        UDS_ACCESS_TIME = 0
        UDS_CREATION_TIME = 0
        UDS_FILE_TYPE = 0
        UDS_LINK_DEST = 0
        UDS_URL = 0
        UDS_MIME_TYPE = 0
        UDS_GUESSED_MIME_TYPE = 0
        UDS_XML_PROPERTIES = 0
        UDS_EXTENDED_ACL = 0
        UDS_ACL_STRING = 0
        UDS_DEFAULT_ACL_STRING = 0
        UDS_DISPLAY_NAME = 0
        UDS_TARGET_URL = 0
        UDS_DISPLAY_TYPE = 0
        UDS_NEPOMUK_URI = 0
        UDS_ICON_OVERLAY_NAMES = 0
        UDS_NEPOMUK_QUERY = 0
        UDS_COMMENT = 0
        UDS_DEVICE_ID = 0
        UDS_INODE = 0
        UDS_EXTRA = 0
        UDS_EXTRA_END = 0
    
        def __init__(self):
            '''void KIO.UDSEntry.__init__()'''
        def __init__(self, other):
            '''void KIO.UDSEntry.__init__(KIO.UDSEntry other)'''
        def clear(self):
            '''void KIO.UDSEntry.clear()'''
        def listFields(self):
            '''list-of-int KIO.UDSEntry.listFields()'''
            return [int()]
        def remove(self, field):
            '''bool KIO.UDSEntry.remove(int field)'''
            return bool()
        def contains(self, field):
            '''bool KIO.UDSEntry.contains(int field)'''
            return bool()
        def count(self):
            '''int KIO.UDSEntry.count()'''
            return int()
        def insert(self, field, value):
            '''void KIO.UDSEntry.insert(int field, QString value)'''
        def insert(self, field, l):
            '''void KIO.UDSEntry.insert(int field, int l)'''
        def isLink(self):
            '''bool KIO.UDSEntry.isLink()'''
            return bool()
        def isDir(self):
            '''bool KIO.UDSEntry.isDir()'''
            return bool()
        def numberValue(self, field, defaultValue = 0):
            '''int KIO.UDSEntry.numberValue(int field, int defaultValue = 0)'''
            return int()
        def stringValue(self, field):
            '''QString KIO.UDSEntry.stringValue(int field)'''
            return QString()
    class ForwardingSlaveBase(QObject, KIO.SlaveBase):
        """"""
        def __init__(self, protocol, poolSocket, appSocket):
            '''void KIO.ForwardingSlaveBase.__init__(QByteArray protocol, QByteArray poolSocket, QByteArray appSocket)'''
        def requestedUrl(self):
            '''KUrl KIO.ForwardingSlaveBase.requestedUrl()'''
            return KUrl()
        def processedUrl(self):
            '''KUrl KIO.ForwardingSlaveBase.processedUrl()'''
            return KUrl()
        def prepareUDSEntry(self, entry, listing = False):
            '''void KIO.ForwardingSlaveBase.prepareUDSEntry(KIO.UDSEntry entry, bool listing = False)'''
        def rewriteUrl(self, url, newURL):
            '''abstract bool KIO.ForwardingSlaveBase.rewriteUrl(KUrl url, KUrl newURL)'''
            return bool()
        def del_(self, url, isfile):
            '''void KIO.ForwardingSlaveBase.del_(KUrl url, bool isfile)'''
        def copy(self, src, dest, permissions, flags):
            '''void KIO.ForwardingSlaveBase.copy(KUrl src, KUrl dest, int permissions, KIO.JobFlags flags)'''
        def setModificationTime(self, url, mtime):
            '''void KIO.ForwardingSlaveBase.setModificationTime(KUrl url, QDateTime mtime)'''
        def chmod(self, url, permissions):
            '''void KIO.ForwardingSlaveBase.chmod(KUrl url, int permissions)'''
        def symlink(self, target, dest, flags):
            '''void KIO.ForwardingSlaveBase.symlink(QString target, KUrl dest, KIO.JobFlags flags)'''
        def rename(self, src, dest, flags):
            '''void KIO.ForwardingSlaveBase.rename(KUrl src, KUrl dest, KIO.JobFlags flags)'''
        def mkdir(self, url, permissions):
            '''void KIO.ForwardingSlaveBase.mkdir(KUrl url, int permissions)'''
        def listDir(self, url):
            '''void KIO.ForwardingSlaveBase.listDir(KUrl url)'''
        def mimetype(self, url):
            '''void KIO.ForwardingSlaveBase.mimetype(KUrl url)'''
        def stat(self, url):
            '''void KIO.ForwardingSlaveBase.stat(KUrl url)'''
        def put(self, url, permissions, flags):
            '''void KIO.ForwardingSlaveBase.put(KUrl url, int permissions, KIO.JobFlags flags)'''
        def get(self, url):
            '''void KIO.ForwardingSlaveBase.get(KUrl url)'''
    class FileJob(KIO.SimpleJob):
        """"""
        position = pyqtSignal() # void position(KIO::Job *,KIO::filesize_t) - signal
        written = pyqtSignal() # void written(KIO::Job *,KIO::filesize_t) - signal
        open = pyqtSignal() # void open(KIO::Job *) - signal
        mimetype = pyqtSignal() # void mimetype(KIO::Job *,const QStringamp;) - signal
        redirection = pyqtSignal() # void redirection(KIO::Job *,const KUrlamp;) - signal
        data = pyqtSignal() # void data(KIO::Job *,const QByteArrayamp;) - signal
        def size(self):
            '''int KIO.FileJob.size()'''
            return int()
        def seek(self, offset):
            '''void KIO.FileJob.seek(int offset)'''
        def close(self):
            '''void KIO.FileJob.close()'''
        close = pyqtSignal() # void close(KIO::Job *) - signal
        def write(self, data):
            '''void KIO.FileJob.write(QByteArray data)'''
        def read(self, size):
            '''void KIO.FileJob.read(int size)'''
    class SpecialJob(KIO.TransferJob):
        """"""
        def __init__(self, url, data = QByteArray()):
            '''void KIO.SpecialJob.__init__(KUrl url, QByteArray data = QByteArray())'''
        def arguments(self):
            '''QByteArray KIO.SpecialJob.arguments()'''
            return QByteArray()
        def setArguments(self, data):
            '''void KIO.SpecialJob.setArguments(QByteArray data)'''
    class SkipDialog(KDialog):
        """"""
        def __init__(self, parent, _multi, _error_text):
            '''void KIO.SkipDialog.__init__(QWidget parent, bool _multi, QString _error_text)'''
        result = pyqtSignal() # void result(KIO::SkipDialog *,int) - signal
    class StatJob(KIO.SimpleJob):
        """"""
        # Enum KIO.StatJob.StatSide
        SourceSide = 0
        DestinationSide = 0
    
        def mostLocalUrl(self):
            '''KUrl KIO.StatJob.mostLocalUrl()'''
            return KUrl()
        def slotMetaData(self, _metaData):
            '''void KIO.StatJob.slotMetaData(MetaData _metaData)'''
        def slotFinished(self):
            '''void KIO.StatJob.slotFinished()'''
        permanentRedirection = pyqtSignal() # void permanentRedirection(KIO::Job *,const KUrlamp;,const KUrlamp;) - signal
        redirection = pyqtSignal() # void redirection(KIO::Job *,const KUrlamp;) - signal
        def statResult(self):
            '''KIO.UDSEntry KIO.StatJob.statResult()'''
            return KIO.UDSEntry()
        def setDetails(self, details):
            '''void KIO.StatJob.setDetails(int details)'''
        def setSide(self, side):
            '''void KIO.StatJob.setSide(KIO.StatJob.StatSide side)'''
        def setSide(self, source):
            '''void KIO.StatJob.setSide(bool source)'''
    class ChmodJob(KIO.Job):
        """"""
        def slotResult(self, job):
            '''void KIO.ChmodJob.slotResult(KJob job)'''
    class TCPSlaveBase():
        """"""
        class SslResult():
            """"""
            def __init__(self):
                '''KIO.TCPSlaveBase.SslResult KIO.TCPSlaveBase.SslResult.__init__()'''
                return KIO.TCPSlaveBase.SslResult()
            def __init__(self):
                '''int KIO.TCPSlaveBase.SslResult.__init__()'''
                return int()
            def __init__(self):
                '''void KIO.TCPSlaveBase.SslResult.__init__()'''
            def __bool__(self):
                '''int KIO.TCPSlaveBase.SslResult.__bool__()'''
                return int()
            def __ne__(self, f):
                '''bool KIO.TCPSlaveBase.SslResult.__ne__(KIO.TCPSlaveBase.SslResult f)'''
                return bool()
            def __eq__(self, f):
                '''bool KIO.TCPSlaveBase.SslResult.__eq__(KIO.TCPSlaveBase.SslResult f)'''
                return bool()
            def __invert__(self):
                '''KIO.TCPSlaveBase.SslResult KIO.TCPSlaveBase.SslResult.__invert__()'''
                return KIO.TCPSlaveBase.SslResult()
            def __and__(self, mask):
                '''KIO.TCPSlaveBase.SslResult KIO.TCPSlaveBase.SslResult.__and__(int mask)'''
                return KIO.TCPSlaveBase.SslResult()
            def __xor__(self, f):
                '''KIO.TCPSlaveBase.SslResult KIO.TCPSlaveBase.SslResult.__xor__(KIO.TCPSlaveBase.SslResult f)'''
                return KIO.TCPSlaveBase.SslResult()
            def __xor__(self, f):
                '''KIO.TCPSlaveBase.SslResult KIO.TCPSlaveBase.SslResult.__xor__(int f)'''
                return KIO.TCPSlaveBase.SslResult()
            def __or__(self, f):
                '''KIO.TCPSlaveBase.SslResult KIO.TCPSlaveBase.SslResult.__or__(KIO.TCPSlaveBase.SslResult f)'''
                return KIO.TCPSlaveBase.SslResult()
            def __or__(self, f):
                '''KIO.TCPSlaveBase.SslResult KIO.TCPSlaveBase.SslResult.__or__(int f)'''
                return KIO.TCPSlaveBase.SslResult()
            def __int__(self):
                '''int KIO.TCPSlaveBase.SslResult.__int__()'''
                return int()
            def __ixor__(self, f):
                '''KIO.TCPSlaveBase.SslResult KIO.TCPSlaveBase.SslResult.__ixor__(KIO.TCPSlaveBase.SslResult f)'''
                return KIO.TCPSlaveBase.SslResult()
            def __ior__(self, f):
                '''KIO.TCPSlaveBase.SslResult KIO.TCPSlaveBase.SslResult.__ior__(KIO.TCPSlaveBase.SslResult f)'''
                return KIO.TCPSlaveBase.SslResult()
            def __iand__(self, mask):
                '''KIO.TCPSlaveBase.SslResult KIO.TCPSlaveBase.SslResult.__iand__(int mask)'''
                return KIO.TCPSlaveBase.SslResult()
    class CopyInfo():
        """"""
        ctime = None # int - member
        linkDest = None # QString - member
        mtime = None # int - member
        permissions = None # int - member
        size = None # int - member
        uDest = None # KUrl - member
        uSource = None # KUrl - member
        def __init__(self):
            '''void KIO.CopyInfo.__init__()'''
        def __init__(self):
            '''KIO.CopyInfo KIO.CopyInfo.__init__()'''
            return KIO.CopyInfo()
    class Integration():
        """"""
        class CookieJar(QNetworkCookieJar):
            """"""
            def __init__(self, parent = None):
                '''void KIO.Integration.CookieJar.__init__(QObject parent = None)'''
            def setDisableCookieStorage(self, disable):
                '''void KIO.Integration.CookieJar.setDisableCookieStorage(bool disable)'''
            def isCookieStorageDisabled(self):
                '''bool KIO.Integration.CookieJar.isCookieStorageDisabled()'''
                return bool()
            def setCookiesFromUrl(self, cookieList, url):
                '''bool KIO.Integration.CookieJar.setCookiesFromUrl(list-of-QNetworkCookie cookieList, QUrl url)'''
                return bool()
            def cookiesForUrl(self, url):
                '''list-of-QNetworkCookie KIO.Integration.CookieJar.cookiesForUrl(QUrl url)'''
                return [QNetworkCookie()]
            def reparseConfiguration(self):
                '''void KIO.Integration.CookieJar.reparseConfiguration()'''
            def setWindowId(self, id):
                '''void KIO.Integration.CookieJar.setWindowId(int id)'''
            def windowId(self):
                '''int KIO.Integration.CookieJar.windowId()'''
                return int()
    class NetRC():
        """"""
        # Enum KIO.NetRC.LookUpModeFlag
        exactOnly = 0
        defaultOnly = 0
        presetOnly = 0
    
        def lookup(self, url, login, userealnetrc, type, mode):
            '''bool KIO.NetRC.lookup(KUrl url, KIO.NetRC.AutoLogin login, bool userealnetrc, QString type, KIO.NetRC.LookUpMode mode)'''
            return bool()
        def parse(self):
            '''int KIO.NetRC.parse()'''
            return int()
        def openf(self):
            '''QString KIO.NetRC.openf()'''
            return QString()
        def reload(self):
            '''void KIO.NetRC.reload()'''
        def self(self):
            '''static KIO.NetRC KIO.NetRC.self()'''
            return KIO.NetRC()
    class AuthInfo():
        """"""
        # Enum KIO.AuthInfo.FieldFlags
        ExtraFieldNoFlags = 0
        ExtraFieldReadOnly = 0
        ExtraFieldMandatory = 0
    
        caption = None # QString - member
        comment = None # QString - member
        commentLabel = None # QString - member
        digestInfo = None # QString - member
        keepPassword = None # bool - member
        password = None # QString - member
        prompt = None # QString - member
        readOnly = None # bool - member
        realmValue = None # QString - member
        url = None # KUrl - member
        username = None # QString - member
        verifyPath = None # bool - member
        def __init__(self):
            '''void KIO.AuthInfo.__init__()'''
        def __init__(self, info):
            '''void KIO.AuthInfo.__init__(KIO.AuthInfo info)'''
        def registerMetaTypes(self):
            '''static void KIO.AuthInfo.registerMetaTypes()'''
        def getExtraFieldFlags(self, fieldName):
            '''KIO.AuthInfo.FieldFlags KIO.AuthInfo.getExtraFieldFlags(QString fieldName)'''
            return KIO.AuthInfo.FieldFlags()
        def getExtraField(self, fieldName):
            '''QVariant KIO.AuthInfo.getExtraField(QString fieldName)'''
            return QVariant()
        def setExtraFieldFlags(self, fieldName, flags):
            '''void KIO.AuthInfo.setExtraFieldFlags(QString fieldName, KIO.AuthInfo.FieldFlags flags)'''
        def setExtraField(self, fieldName, value):
            '''void KIO.AuthInfo.setExtraField(QString fieldName, QVariant value)'''
        def setModified(self, flag):
            '''void KIO.AuthInfo.setModified(bool flag)'''
        def isModified(self):
            '''bool KIO.AuthInfo.isModified()'''
            return bool()
    class StoredTransferJob(KIO.TransferJob):
        """"""
        def data(self):
            '''QByteArray KIO.StoredTransferJob.data()'''
            return QByteArray()
        def setData(self, arr):
            '''void KIO.StoredTransferJob.setData(QByteArray arr)'''
    class NetRC():
        """"""
        class LookUpMode():
            """"""
            def __init__(self):
                '''KIO.NetRC.LookUpMode KIO.NetRC.LookUpMode.__init__()'''
                return KIO.NetRC.LookUpMode()
            def __init__(self):
                '''int KIO.NetRC.LookUpMode.__init__()'''
                return int()
            def __init__(self):
                '''void KIO.NetRC.LookUpMode.__init__()'''
            def __bool__(self):
                '''int KIO.NetRC.LookUpMode.__bool__()'''
                return int()
            def __ne__(self, f):
                '''bool KIO.NetRC.LookUpMode.__ne__(KIO.NetRC.LookUpMode f)'''
                return bool()
            def __eq__(self, f):
                '''bool KIO.NetRC.LookUpMode.__eq__(KIO.NetRC.LookUpMode f)'''
                return bool()
            def __invert__(self):
                '''KIO.NetRC.LookUpMode KIO.NetRC.LookUpMode.__invert__()'''
                return KIO.NetRC.LookUpMode()
            def __and__(self, mask):
                '''KIO.NetRC.LookUpMode KIO.NetRC.LookUpMode.__and__(int mask)'''
                return KIO.NetRC.LookUpMode()
            def __xor__(self, f):
                '''KIO.NetRC.LookUpMode KIO.NetRC.LookUpMode.__xor__(KIO.NetRC.LookUpMode f)'''
                return KIO.NetRC.LookUpMode()
            def __xor__(self, f):
                '''KIO.NetRC.LookUpMode KIO.NetRC.LookUpMode.__xor__(int f)'''
                return KIO.NetRC.LookUpMode()
            def __or__(self, f):
                '''KIO.NetRC.LookUpMode KIO.NetRC.LookUpMode.__or__(KIO.NetRC.LookUpMode f)'''
                return KIO.NetRC.LookUpMode()
            def __or__(self, f):
                '''KIO.NetRC.LookUpMode KIO.NetRC.LookUpMode.__or__(int f)'''
                return KIO.NetRC.LookUpMode()
            def __int__(self):
                '''int KIO.NetRC.LookUpMode.__int__()'''
                return int()
            def __ixor__(self, f):
                '''KIO.NetRC.LookUpMode KIO.NetRC.LookUpMode.__ixor__(KIO.NetRC.LookUpMode f)'''
                return KIO.NetRC.LookUpMode()
            def __ior__(self, f):
                '''KIO.NetRC.LookUpMode KIO.NetRC.LookUpMode.__ior__(KIO.NetRC.LookUpMode f)'''
                return KIO.NetRC.LookUpMode()
            def __iand__(self, mask):
                '''KIO.NetRC.LookUpMode KIO.NetRC.LookUpMode.__iand__(int mask)'''
                return KIO.NetRC.LookUpMode()
    class MimetypeJob(KIO.TransferJob):
        """"""
        def slotFinished(self):
            '''void KIO.MimetypeJob.slotFinished()'''
    class SslUi():
        """"""
        # Enum KIO.SslUi.RulesStorage
        RecallRules = 0
        StoreRules = 0
        RecallAndStoreRules = 0
    
        def askIgnoreSslErrors(self, socket, storedRules = None):
            '''static bool KIO.SslUi.askIgnoreSslErrors(KTcpSocket socket, KIO.SslUi.RulesStorage storedRules = KIO.SslUi.RecallAndStoreRules)'''
            return bool()
        def askIgnoreSslErrors(self, uiData, storedRules = None):
            '''static bool KIO.SslUi.askIgnoreSslErrors(KSslErrorUiData uiData, KIO.SslUi.RulesStorage storedRules = KIO.SslUi.RecallAndStoreRules)'''
            return bool()
    class AccessManager(QNetworkAccessManager):
        """"""
        # Enum KIO.AccessManager.Attribute
        MetaData = 0
        KioError = 0
    
        def __init__(self, parent):
            '''void KIO.AccessManager.__init__(QObject parent)'''
        def setEmitReadyReadOnMetaDataChange(self):
            '''bool KIO.AccessManager.setEmitReadyReadOnMetaDataChange()'''
            return bool()
        def putReplyOnHold(self, reply):
            '''static void KIO.AccessManager.putReplyOnHold(QNetworkReply reply)'''
        def window(self):
            '''QWidget KIO.AccessManager.window()'''
            return QWidget()
        def setWindow(self, widget):
            '''void KIO.AccessManager.setWindow(QWidget widget)'''
        def sessionMetaData(self):
            '''MetaData KIO.AccessManager.sessionMetaData()'''
            return MetaData()
        def requestMetaData(self):
            '''MetaData KIO.AccessManager.requestMetaData()'''
            return MetaData()
        def cookieJarWindowid(self):
            '''int KIO.AccessManager.cookieJarWindowid()'''
            return int()
        def setCookieJarWindowId(self, id):
            '''void KIO.AccessManager.setCookieJarWindowId(int id)'''
        def createRequest(self, op, req, outgoingData = None):
            '''QNetworkReply KIO.AccessManager.createRequest(QNetworkAccessManager.Operation op, QNetworkRequest req, QIODevice outgoingData = None)'''
            return QNetworkReply()
        def isExternalContentAllowed(self):
            '''bool KIO.AccessManager.isExternalContentAllowed()'''
            return bool()
        def setExternalContentAllowed(self, allowed):
            '''void KIO.AccessManager.setExternalContentAllowed(bool allowed)'''
    class DavJob(KIO.TransferJob):
        """"""
        def slotData(self, data):
            '''void KIO.DavJob.slotData(QByteArray data)'''
        def slotFinished(self):
            '''void KIO.DavJob.slotFinished()'''
        def response(self):
            '''QDomDocument KIO.DavJob.response()'''
            return QDomDocument()
    class TransferJob(KIO.SimpleJob):
        """"""
        def slotMetaData(self, _metaData):
            '''void KIO.TransferJob.slotMetaData(MetaData _metaData)'''
        def slotMimetype(self, mimetype):
            '''void KIO.TransferJob.slotMimetype(QString mimetype)'''
        def slotDataReq(self):
            '''void KIO.TransferJob.slotDataReq()'''
        def slotData(self, data):
            '''void KIO.TransferJob.slotData(QByteArray data)'''
        def slotFinished(self):
            '''void KIO.TransferJob.slotFinished()'''
        def slotRedirection(self, url):
            '''void KIO.TransferJob.slotRedirection(KUrl url)'''
        canResume = pyqtSignal() # void canResume(KIO::Job *,KIO::filesize_t) - signal
        permanentRedirection = pyqtSignal() # void permanentRedirection(KIO::Job *,const KUrlamp;,const KUrlamp;) - signal
        redirection = pyqtSignal() # void redirection(KIO::Job *,const KUrlamp;) - signal
        dataReq = pyqtSignal() # void dataReq(KIO::Job *,QByteArrayamp;) - signal
        data = pyqtSignal() # void data(KIO::Job *,const QByteArrayamp;) - signal
        def doResume(self):
            '''bool KIO.TransferJob.doResume()'''
            return bool()
        def slotResult(self, job):
            '''void KIO.TransferJob.slotResult(KJob job)'''
        def setTotalSize(self, bytes):
            '''void KIO.TransferJob.setTotalSize(int bytes)'''
        def mimetype(self):
            '''QString KIO.TransferJob.mimetype()'''
            return QString()
        mimetype = pyqtSignal() # void mimetype(KIO::Job *,const QStringamp;) - signal
        def reportDataSent(self):
            '''bool KIO.TransferJob.reportDataSent()'''
            return bool()
        def setReportDataSent(self, enabled):
            '''void KIO.TransferJob.setReportDataSent(bool enabled)'''
        def sendAsyncData(self, data):
            '''void KIO.TransferJob.sendAsyncData(QByteArray data)'''
        def setAsyncDataEnabled(self, enabled):
            '''void KIO.TransferJob.setAsyncDataEnabled(bool enabled)'''
        def isErrorPage(self):
            '''bool KIO.TransferJob.isErrorPage()'''
            return bool()
        def setModificationTime(self, mtime):
            '''void KIO.TransferJob.setModificationTime(QDateTime mtime)'''
    class FileUndoManager():
        """"""
        class UiInterface():
            """"""
            def __init__(self):
                '''void KIO.FileUndoManager.UiInterface.__init__()'''
            def __init__(self):
                '''KIO.FileUndoManager.UiInterface KIO.FileUndoManager.UiInterface.__init__()'''
                return KIO.FileUndoManager.UiInterface()
            def virtual_hook(self, id, data):
                '''void KIO.FileUndoManager.UiInterface.virtual_hook(int id, sip.voidptr data)'''
            def copiedFileWasModified(self, src, dest, srcTime, destTime):
                '''bool KIO.FileUndoManager.UiInterface.copiedFileWasModified(KUrl src, KUrl dest, KDateTime srcTime, KDateTime destTime)'''
                return bool()
            def confirmDeletion(self, files):
                '''bool KIO.FileUndoManager.UiInterface.confirmDeletion(KUrl.List files)'''
                return bool()
            def jobError(self, job):
                '''void KIO.FileUndoManager.UiInterface.jobError(KIO.Job job)'''
            def parentWidget(self):
                '''QWidget KIO.FileUndoManager.UiInterface.parentWidget()'''
                return QWidget()
            def setParentWidget(self, parentWidget):
                '''void KIO.FileUndoManager.UiInterface.setParentWidget(QWidget parentWidget)'''
            def showProgressInfo(self):
                '''bool KIO.FileUndoManager.UiInterface.showProgressInfo()'''
                return bool()
            def setShowProgressInfo(self, b):
                '''void KIO.FileUndoManager.UiInterface.setShowProgressInfo(bool b)'''
    class Integration():
        """"""
        def sslConfigFromMetaData(self, metadata, sslconfig):
            '''static bool KIO.Integration.sslConfigFromMetaData(MetaData metadata, QSslConfiguration sslconfig)'''
            return bool()
    class JobUiDelegate(KDialogJobUiDelegate):
        """"""
        # Enum KIO.JobUiDelegate.ConfirmationType
        DefaultConfirmation = 0
        ForceConfirmation = 0
    
        # Enum KIO.JobUiDelegate.DeletionType
        Delete = 0
        Trash = 0
        EmptyTrash = 0
    
        def __init__(self):
            '''void KIO.JobUiDelegate.__init__()'''
        def askDeleteConfirmation(self, urls, deletionType, confirmationType):
            '''bool KIO.JobUiDelegate.askDeleteConfirmation(KUrl.List urls, KIO.JobUiDelegate.DeletionType deletionType, KIO.JobUiDelegate.ConfirmationType confirmationType)'''
            return bool()
        def askSkip(self, job, multi, error_text):
            '''KIO.SkipDialog_Result KIO.JobUiDelegate.askSkip(KJob job, bool multi, QString error_text)'''
            return KIO.SkipDialog_Result()
        def askFileRename(self, job, caption, src, dest, mode, newDest, sizeSrc = None, sizeDest = None, ctimeSrc = None, ctimeDest = None, mtimeSrc = None, mtimeDest = None):
            '''KIO.RenameDialog_Result KIO.JobUiDelegate.askFileRename(KJob job, QString caption, QString src, QString dest, KIO.RenameDialog_Mode mode, QString newDest, int sizeSrc = -1, int sizeDest = -1, int ctimeSrc = -1, int ctimeDest = -1, int mtimeSrc = -1, int mtimeDest = -1)'''
            return KIO.RenameDialog_Result()
        def setWindow(self, window):
            '''void KIO.JobUiDelegate.setWindow(QWidget window)'''
    class DirectorySizeJob(KIO.Job):
        """"""
        def slotResult(self, job):
            '''void KIO.DirectorySizeJob.slotResult(KJob job)'''
        def totalSubdirs(self):
            '''int KIO.DirectorySizeJob.totalSubdirs()'''
            return int()
        def totalFiles(self):
            '''int KIO.DirectorySizeJob.totalFiles()'''
            return int()
        def totalSize(self):
            '''int KIO.DirectorySizeJob.totalSize()'''
            return int()
    class PasswordDialog(KPasswordDialog):
        """"""
        def __init__(self, prompt, user, enableKeep = False, modal = True, parent = None):
            '''void KIO.PasswordDialog.__init__(QString prompt, QString user, bool enableKeep = False, bool modal = True, QWidget parent = None)'''
        def getNameAndPassword(self, user, pass_, keep, prompt = QString(), readOnly = False, caption = QString(), comment = QString(), label = QString()):
            '''static int KIO.PasswordDialog.getNameAndPassword(QString user, QString pass, bool keep, QString prompt = QString(), bool readOnly = False, QString caption = QString(), QString comment = QString(), QString label = QString())'''
            return int()
    class SlaveConfig(QObject):
        """"""
        def __init__(self):
            '''void KIO.SlaveConfig.__init__()'''
        configNeeded = pyqtSignal() # void configNeeded(const QStringamp;,const QStringamp;) - signal
        def reset(self):
            '''void KIO.SlaveConfig.reset()'''
        def configData(self, protocol, host):
            '''MetaData KIO.SlaveConfig.configData(QString protocol, QString host)'''
            return MetaData()
        def configData(self, protocol, host, key):
            '''QString KIO.SlaveConfig.configData(QString protocol, QString host, QString key)'''
            return QString()
        def setConfigData(self, protocol, host, key, value):
            '''void KIO.SlaveConfig.setConfigData(QString protocol, QString host, QString key, QString value)'''
        def setConfigData(self, protocol, host, config):
            '''void KIO.SlaveConfig.setConfigData(QString protocol, QString host, MetaData config)'''
        def self(self):
            '''static KIO.SlaveConfig KIO.SlaveConfig.self()'''
            return KIO.SlaveConfig()
    class SlaveInterface(QObject):
        """"""
        def setWindow(self, window):
            '''void KIO.SlaveInterface.setWindow(QWidget window)'''
        def window(self):
            '''QWidget KIO.SlaveInterface.window()'''
            return QWidget()
        def setConnection(self, connection):
            '''void KIO.SlaveInterface.setConnection(KIO.Connection connection)'''
        def calcSpeed(self):
            '''void KIO.SlaveInterface.calcSpeed()'''
        def dropNetwork(self):
            '''QString KIO.SlaveInterface.dropNetwork()'''
            return QString()
        def requestNetwork(self):
            '''QString KIO.SlaveInterface.requestNetwork()'''
            return QString()
        def messageBox(self, type, text, caption, buttonYes, buttonNo):
            '''void KIO.SlaveInterface.messageBox(int type, QString text, QString caption, QString buttonYes, QString buttonNo)'''
        def messageBox(self, type, text, caption, buttonYes, buttonNo, dontAskAgainName):
            '''void KIO.SlaveInterface.messageBox(int type, QString text, QString caption, QString buttonYes, QString buttonNo, QString dontAskAgainName)'''
        def dispatch(self):
            '''bool KIO.SlaveInterface.dispatch()'''
            return bool()
        def dispatch(self, _cmd, data):
            '''bool KIO.SlaveInterface.dispatch(int _cmd, QByteArray data)'''
            return bool()
        infoMessage = pyqtSignal() # void infoMessage(const QStringamp;) - signal
        warning = pyqtSignal() # void warning(const QStringamp;) - signal
        mimeType = pyqtSignal() # void mimeType(const QStringamp;) - signal
        errorPage = pyqtSignal() # void errorPage() - signal
        speed = pyqtSignal() # void speed(unsigned long) - signal
        position = pyqtSignal() # void position(KIO::filesize_t) - signal
        redirection = pyqtSignal() # void redirection(const KUrlamp;) - signal
        processedSize = pyqtSignal() # void processedSize(KIO::filesize_t) - signal
        totalSize = pyqtSignal() # void totalSize(KIO::filesize_t) - signal
        metaData = pyqtSignal() # void metaData(const KIO.MetaDataamp;) - signal
        written = pyqtSignal() # void written(KIO::filesize_t) - signal
        open = pyqtSignal() # void open() - signal
        canResume = pyqtSignal() # void canResume(KIO::filesize_t) - signal
        needSubUrlData = pyqtSignal() # void needSubUrlData() - signal
        statEntry = pyqtSignal() # void statEntry(const KIO::UDSEntryamp;) - signal
        listEntries = pyqtSignal() # void listEntries(const KIO::UDSEntryListamp;) - signal
        slaveStatus = pyqtSignal() # void slaveStatus(pid_t,const QByteArrayamp;,const QStringamp;,bool) - signal
        finished = pyqtSignal() # void finished() - signal
        connected = pyqtSignal() # void connected() - signal
        error = pyqtSignal() # void error(int,const QStringamp;) - signal
        dataReq = pyqtSignal() # void dataReq() - signal
        data = pyqtSignal() # void data(const QByteArrayamp;) - signal
        def offset(self):
            '''int KIO.SlaveInterface.offset()'''
            return int()
        def setOffset(self, offset):
            '''void KIO.SlaveInterface.setOffset(int offset)'''
        def sendResumeAnswer(self, resume):
            '''void KIO.SlaveInterface.sendResumeAnswer(bool resume)'''
        def connection(self):
            '''KIO.Connection KIO.SlaveInterface.connection()'''
            return KIO.Connection()
    class Scheduler(QObject):
        """"""
        def updateInternalMetaData(self, job):
            '''static void KIO.Scheduler.updateInternalMetaData(KIO.SimpleJob job)'''
        slaveOnHoldListChanged = pyqtSignal() # void slaveOnHoldListChanged() - signal
        def isSlaveOnHoldFor(self, url):
            '''static bool KIO.Scheduler.isSlaveOnHoldFor(KUrl url)'''
            return bool()
        def setJobPriority(self, job, priority):
            '''static void KIO.Scheduler.setJobPriority(KIO.SimpleJob job, int priority)'''
        reparseSlaveConfiguration = pyqtSignal() # void reparseSlaveConfiguration(const QStringamp;) - signal
        slaveError = pyqtSignal() # void slaveError(KIO::Slave *,int,const QStringamp;) - signal
        slaveConnected = pyqtSignal() # void slaveConnected(KIO::Slave *) - signal
        def emitReparseSlaveConfiguration(self):
            '''static void KIO.Scheduler.emitReparseSlaveConfiguration()'''
        def checkSlaveOnHold(self, b):
            '''static void KIO.Scheduler.checkSlaveOnHold(bool b)'''
        def disconnect(self, sender, signal, receiver, member):
            '''static bool KIO.Scheduler.disconnect(QObject sender, str signal, QObject receiver, str member)'''
            return bool()
        def connect(self, signal, receiver, member):
            '''static bool KIO.Scheduler.connect(str signal, QObject receiver, str member)'''
            return bool()
        def connect(self, sender, signal, receiver, member):
            '''static bool KIO.Scheduler.connect(QObject sender, str signal, QObject receiver, str member)'''
            return bool()
        def connect(self, sender, signal, member):
            '''bool KIO.Scheduler.connect(QObject sender, str signal, str member)'''
            return bool()
        def unregisterWindow(self, wid):
            '''static void KIO.Scheduler.unregisterWindow(QObject wid)'''
        def registerWindow(self, wid):
            '''static void KIO.Scheduler.registerWindow(QWidget wid)'''
        def disconnectSlave(self, slave):
            '''static bool KIO.Scheduler.disconnectSlave(KIO.Slave slave)'''
            return bool()
        def assignJobToSlave(self, slave, job):
            '''static bool KIO.Scheduler.assignJobToSlave(KIO.Slave slave, KIO.SimpleJob job)'''
            return bool()
        def getConnectedSlave(self, url, config = None):
            '''static KIO.Slave KIO.Scheduler.getConnectedSlave(KUrl url, MetaData config = KIO.MetaData())'''
            return KIO.Slave()
        def publishSlaveOnHold(self):
            '''static void KIO.Scheduler.publishSlaveOnHold()'''
        def removeSlaveOnHold(self):
            '''static void KIO.Scheduler.removeSlaveOnHold()'''
        def putSlaveOnHold(self, job, url):
            '''static void KIO.Scheduler.putSlaveOnHold(KIO.SimpleJob job, KUrl url)'''
        def jobFinished(self, job, slave):
            '''static void KIO.Scheduler.jobFinished(KIO.SimpleJob job, KIO.Slave slave)'''
        def cancelJob(self, job):
            '''static void KIO.Scheduler.cancelJob(KIO.SimpleJob job)'''
        def scheduleJob(self, job):
            '''static void KIO.Scheduler.scheduleJob(KIO.SimpleJob job)'''
        def doJob(self, job):
            '''static void KIO.Scheduler.doJob(KIO.SimpleJob job)'''
    class NetRC():
        """"""
        class AutoLogin():
            """"""
            login = None # QString - member
            macdef = None # dict-of-QString-QStringList - member
            machine = None # QString - member
            password = None # QString - member
            type = None # QString - member
            def __init__(self):
                '''void KIO.NetRC.AutoLogin.__init__()'''
            def __init__(self):
                '''KIO.NetRC.AutoLogin KIO.NetRC.AutoLogin.__init__()'''
                return KIO.NetRC.AutoLogin()
    class PreviewJob(KIO.Job):
        """"""
        # Enum KIO.PreviewJob.ScaleType
        Unscaled = 0
        Scaled = 0
        ScaledAndCached = 0
    
        def __init__(self, items, width, height, iconSize, iconAlpha, scale, save, enabledPlugins):
            '''void KIO.PreviewJob.__init__(KFileItemList items, int width, int height, int iconSize, int iconAlpha, bool scale, bool save, QStringList enabledPlugins)'''
        def __init__(self, items, size, enabledPlugins = None):
            '''void KIO.PreviewJob.__init__(KFileItemList items, QSize size, QStringList enabledPlugins = None)'''
        def scaleType(self):
            '''KIO.PreviewJob.ScaleType KIO.PreviewJob.scaleType()'''
            return KIO.PreviewJob.ScaleType()
        def setScaleType(self, type):
            '''void KIO.PreviewJob.setScaleType(KIO.PreviewJob.ScaleType type)'''
        def overlayIconAlpha(self):
            '''int KIO.PreviewJob.overlayIconAlpha()'''
            return int()
        def setOverlayIconAlpha(self, alpha):
            '''void KIO.PreviewJob.setOverlayIconAlpha(int alpha)'''
        def overlayIconSize(self):
            '''int KIO.PreviewJob.overlayIconSize()'''
            return int()
        def setOverlayIconSize(self, size):
            '''void KIO.PreviewJob.setOverlayIconSize(int size)'''
        def slotResult(self, job):
            '''void KIO.PreviewJob.slotResult(KJob job)'''
        failed = pyqtSignal() # void failed(const KFileItemamp;) - signal
        gotPreview = pyqtSignal() # void gotPreview(const KFileItemamp;,const QPixmapamp;) - signal
        def maximumFileSize(self):
            '''static int KIO.PreviewJob.maximumFileSize()'''
            return int()
        def supportedMimeTypes(self):
            '''static QStringList KIO.PreviewJob.supportedMimeTypes()'''
            return QStringList()
        def availablePlugins(self):
            '''static QStringList KIO.PreviewJob.availablePlugins()'''
            return QStringList()
        def sequenceIndex(self):
            '''int KIO.PreviewJob.sequenceIndex()'''
            return int()
        def setSequenceIndex(self, index):
            '''void KIO.PreviewJob.setSequenceIndex(int index)'''
        def setIgnoreMaximumSize(self, ignoreSize = True):
            '''void KIO.PreviewJob.setIgnoreMaximumSize(bool ignoreSize = True)'''
        def removeItem(self, url):
            '''void KIO.PreviewJob.removeItem(KUrl url)'''
    class SimpleJob(KIO.Job):
        """"""
        def setRedirectionHandlingEnabled(self, handle):
            '''void KIO.SimpleJob.setRedirectionHandlingEnabled(bool handle)'''
        def isRedirectionHandlingEnabled(self):
            '''bool KIO.SimpleJob.isRedirectionHandlingEnabled()'''
            return bool()
        def storeSSLSessionFromJob(self, m_redirectionURL):
            '''void KIO.SimpleJob.storeSSLSessionFromJob(KUrl m_redirectionURL)'''
        def slotMetaData(self, _metaData):
            '''void KIO.SimpleJob.slotMetaData(MetaData _metaData)'''
        def slotWarning(self):
            '''QString KIO.SimpleJob.slotWarning()'''
            return QString()
        def slotFinished(self):
            '''void KIO.SimpleJob.slotFinished()'''
        def slotError(self):
            '''QString KIO.SimpleJob.slotError()'''
            return QString()
        def removeOnHold(self):
            '''static void KIO.SimpleJob.removeOnHold()'''
        def putOnHold(self):
            '''void KIO.SimpleJob.putOnHold()'''
        def url(self):
            '''KUrl KIO.SimpleJob.url()'''
            return KUrl()
        def doKill(self):
            '''bool KIO.SimpleJob.doKill()'''
            return bool()
        def doResume(self):
            '''bool KIO.SimpleJob.doResume()'''
            return bool()
        def doSuspend(self):
            '''bool KIO.SimpleJob.doSuspend()'''
            return bool()
    class RenameDialogPlugin():
        """"""
        class FileItem():
            """"""
            def __init__(self, url, mimeSrc, ctime, mtime):
                '''int KIO.RenameDialogPlugin.FileItem.__init__(KUrl url, QString mimeSrc, int ctime, int mtime)'''
                return int()
            def mTime(self):
                '''int KIO.RenameDialogPlugin.FileItem.mTime()'''
                return int()
            def cTime(self):
                '''int KIO.RenameDialogPlugin.FileItem.cTime()'''
                return int()
            def fileSize(self):
                '''int KIO.RenameDialogPlugin.FileItem.fileSize()'''
                return int()
            def mimeType(self):
                '''QString KIO.RenameDialogPlugin.FileItem.mimeType()'''
                return QString()
            def url(self):
                '''KUrl KIO.RenameDialogPlugin.FileItem.url()'''
                return KUrl()
    class TCPSlaveBase(KIO.SlaveBase):
        """"""
        # Enum KIO.TCPSlaveBase.SslResultDetail
        ResultOk = 0
        ResultOverridden = 0
        ResultFailed = 0
        ResultFailedEarly = 0
    
        def __init__(self, protocol, poolSocket, appSocket, autoSsl = False):
            '''void KIO.TCPSlaveBase.__init__(QByteArray protocol, QByteArray poolSocket, QByteArray appSocket, bool autoSsl = False)'''
        def socket(self):
            '''QIODevice KIO.TCPSlaveBase.socket()'''
            return QIODevice()
        def setBlocking(self, b):
            '''void KIO.TCPSlaveBase.setBlocking(bool b)'''
        def waitForResponse(self, t):
            '''bool KIO.TCPSlaveBase.waitForResponse(int t)'''
            return bool()
        def isConnected(self):
            '''bool KIO.TCPSlaveBase.isConnected()'''
            return bool()
        def atEnd(self):
            '''bool KIO.TCPSlaveBase.atEnd()'''
            return bool()
        def disconnectFromHost(self):
            '''void KIO.TCPSlaveBase.disconnectFromHost()'''
        def startSsl(self):
            '''bool KIO.TCPSlaveBase.startSsl()'''
            return bool()
        def isUsingSsl(self):
            '''bool KIO.TCPSlaveBase.isUsingSsl()'''
            return bool()
        def isAutoSsl(self):
            '''bool KIO.TCPSlaveBase.isAutoSsl()'''
            return bool()
        def port(self):
            '''int KIO.TCPSlaveBase.port()'''
            return int()
        def connectToHost(self, protocol, host, port):
            '''bool KIO.TCPSlaveBase.connectToHost(QString protocol, QString host, int port)'''
            return bool()
        def connectToHost(self, host, port, errorString = None):
            '''int KIO.TCPSlaveBase.connectToHost(QString host, int port, QString errorString = None)'''
            return int()
        def readLine(self, data, len):
            '''int KIO.TCPSlaveBase.readLine(str data, int len)'''
            return int()
        def read(self, data, len):
            '''int KIO.TCPSlaveBase.read(str data, int len)'''
            return int()
        def write(self, data, len):
            '''int KIO.TCPSlaveBase.write(str data, int len)'''
            return int()
    class ListJob(KIO.SimpleJob):
        """"""
        def slotResult(self, job):
            '''void KIO.ListJob.slotResult(KJob job)'''
        def slotMetaData(self, _metaData):
            '''void KIO.ListJob.slotMetaData(MetaData _metaData)'''
        def slotFinished(self):
            '''void KIO.ListJob.slotFinished()'''
        permanentRedirection = pyqtSignal() # void permanentRedirection(KIO::Job *,const KUrlamp;,const KUrlamp;) - signal
        redirection = pyqtSignal() # void redirection(KIO::Job *,const KUrlamp;) - signal
        entries = pyqtSignal() # void entries(KIO::Job *,const KIO::UDSEntryListamp;) - signal
        def setUnrestricted(self, unrestricted):
            '''void KIO.ListJob.setUnrestricted(bool unrestricted)'''
        def redirectionUrl(self):
            '''KUrl KIO.ListJob.redirectionUrl()'''
            return KUrl()
    class RenameDialog(QDialog):
        """"""
        def __init__(self, parent, caption, src, dest, mode, sizeSrc = None, sizeDest = None, ctimeSrc = None, ctimeDest = None, mtimeSrc = None, mtimeDest = None):
            '''void KIO.RenameDialog.__init__(QWidget parent, QString caption, KUrl src, KUrl dest, KIO.RenameDialog_Mode mode, int sizeSrc = -1, int sizeDest = -1, int ctimeSrc = -1, int ctimeDest = -1, int mtimeSrc = -1, int mtimeDest = -1)'''
        def autoDestUrl(self):
            '''KUrl KIO.RenameDialog.autoDestUrl()'''
            return KUrl()
        def enableRenameButton(self):
            '''QString KIO.RenameDialog.enableRenameButton()'''
            return QString()
        def suggestNewNamePressed(self):
            '''void KIO.RenameDialog.suggestNewNamePressed()'''
        def resumeAllPressed(self):
            '''void KIO.RenameDialog.resumeAllPressed()'''
        def resumePressed(self):
            '''void KIO.RenameDialog.resumePressed()'''
        def overwriteAllPressed(self):
            '''void KIO.RenameDialog.overwriteAllPressed()'''
        def overwritePressed(self):
            '''void KIO.RenameDialog.overwritePressed()'''
        def autoSkipPressed(self):
            '''void KIO.RenameDialog.autoSkipPressed()'''
        def skipPressed(self):
            '''void KIO.RenameDialog.skipPressed()'''
        def renamePressed(self):
            '''void KIO.RenameDialog.renamePressed()'''
        def cancelPressed(self):
            '''void KIO.RenameDialog.cancelPressed()'''
        def suggestName(self, baseURL, oldName):
            '''static QString KIO.RenameDialog.suggestName(KUrl baseURL, QString oldName)'''
            return QString()
        def newDestUrl(self):
            '''KUrl KIO.RenameDialog.newDestUrl()'''
            return KUrl()
    class ConnectionServer(QObject):
        """"""
        def __init__(self, parent = None):
            '''void KIO.ConnectionServer.__init__(QObject parent = None)'''
        def setNextPendingConnection(self, conn):
            '''void KIO.ConnectionServer.setNextPendingConnection(KIO.Connection conn)'''
        newConnection = pyqtSignal() # void newConnection() - signal
        def nextPendingConnection(self):
            '''KIO.Connection KIO.ConnectionServer.nextPendingConnection()'''
            return KIO.Connection()
        def address(self):
            '''QString KIO.ConnectionServer.address()'''
            return QString()
        def close(self):
            '''void KIO.ConnectionServer.close()'''
        def isListening(self):
            '''bool KIO.ConnectionServer.isListening()'''
            return bool()
        def listenForRemote(self):
            '''void KIO.ConnectionServer.listenForRemote()'''
    class DeleteJob(KIO.Job):
        """"""
        def slotResult(self, job):
            '''void KIO.DeleteJob.slotResult(KJob job)'''
        deleting = pyqtSignal() # void deleting(KIO::Job *,const KUrlamp;) - signal
        processedDirs = pyqtSignal() # void processedDirs(KIO::Job *,unsigned long) - signal
        processedFiles = pyqtSignal() # void processedFiles(KIO::Job *,unsigned long) - signal
        totalDirs = pyqtSignal() # void totalDirs(KJob *,unsigned long) - signal
        totalFiles = pyqtSignal() # void totalFiles(KJob *,unsigned long) - signal
        def urls(self):
            '''KUrl.List KIO.DeleteJob.urls()'''
            return KUrl.List()
    class RenameDialogPlugin(QWidget):
        """"""
        def __init__(self, dialog):
            '''void KIO.RenameDialogPlugin.__init__(QDialog dialog)'''
        def handle(self, mode, srcFile, dstFile):
            '''abstract void KIO.RenameDialogPlugin.handle(KIO.RenameDialog_Mode mode, KIO.RenameDialogPlugin.FileItem srcFile, KIO.RenameDialogPlugin.FileItem dstFile)'''
        def wantToHandle(self, mode, srcFile, dstFile):
            '''abstract bool KIO.RenameDialogPlugin.wantToHandle(KIO.RenameDialog_Mode mode, KIO.RenameDialogPlugin.FileItem srcFile, KIO.RenameDialogPlugin.FileItem dstFile)'''
            return bool()
    class NetAccess(QObject):
        """"""
        # Enum KIO.NetAccess.StatSide
        SourceSide = 0
        DestinationSide = 0
    
        leaveModality = pyqtSignal() # void leaveModality() - signal
        def lastError(self):
            '''static int KIO.NetAccess.lastError()'''
            return int()
        def lastErrorString(self):
            '''static QString KIO.NetAccess.lastErrorString()'''
            return QString()
        def mimetype(self, url, window):
            '''static QString KIO.NetAccess.mimetype(KUrl url, QWidget window)'''
            return QString()
        def synchronousRun(self, job, window, data = None, finalURL = None, metaData = None):
            '''static bool KIO.NetAccess.synchronousRun(KIO.Job job, QWidget window, QByteArray data = None, KUrl finalURL = None, dict-of-QString-QString metaData = None)'''
            return bool()
        def fish_execute(self, url, command, window):
            '''static QString KIO.NetAccess.fish_execute(KUrl url, QString command, QWidget window)'''
            return QString()
        def mkdir(self, url, window, permissions = None):
            '''static bool KIO.NetAccess.mkdir(KUrl url, QWidget window, int permissions = -1)'''
            return bool()
        def del_(self, url, window):
            '''static bool KIO.NetAccess.del_(KUrl url, QWidget window)'''
            return bool()
        def mostLocalUrl(self, url, window):
            '''static KUrl KIO.NetAccess.mostLocalUrl(KUrl url, QWidget window)'''
            return KUrl()
        def stat(self, url, entry, window):
            '''static bool KIO.NetAccess.stat(KUrl url, KIO.UDSEntry entry, QWidget window)'''
            return bool()
        def exists(self, url, source, window):
            '''static bool KIO.NetAccess.exists(KUrl url, bool source, QWidget window)'''
            return bool()
        def exists(self, url, statSide, window):
            '''static bool KIO.NetAccess.exists(KUrl url, KIO.NetAccess.StatSide statSide, QWidget window)'''
            return bool()
        def move(self, src, target, window = None):
            '''static bool KIO.NetAccess.move(KUrl src, KUrl target, QWidget window = None)'''
            return bool()
        def move(self, src, target, window = None):
            '''static bool KIO.NetAccess.move(KUrl.List src, KUrl target, QWidget window = None)'''
            return bool()
        def dircopy(self, src, target, window):
            '''static bool KIO.NetAccess.dircopy(KUrl src, KUrl target, QWidget window)'''
            return bool()
        def dircopy(self, src, target, window = None):
            '''static bool KIO.NetAccess.dircopy(KUrl.List src, KUrl target, QWidget window = None)'''
            return bool()
        def copy(self, src, target, window = None):
            '''static bool KIO.NetAccess.copy(KUrl src, KUrl target, QWidget window = None)'''
            return bool()
        def file_copy(self, src, target, window = None):
            '''static bool KIO.NetAccess.file_copy(KUrl src, KUrl target, QWidget window = None)'''
            return bool()
        def upload(self, src, target, window):
            '''static bool KIO.NetAccess.upload(QString src, KUrl target, QWidget window)'''
            return bool()
        def removeTempFile(self, name):
            '''static void KIO.NetAccess.removeTempFile(QString name)'''
        def download(self, src, target, window):
            '''static bool KIO.NetAccess.download(KUrl src, QString target, QWidget window)'''
            return bool()
    class SlaveBase():
        """"""
        # Enum KIO.SlaveBase.VirtualFunctionId
        AppConnectionMade = 0
    
        # Enum KIO.SlaveBase.MessageBoxType
        QuestionYesNo = 0
        WarningYesNo = 0
        WarningContinueCancel = 0
        WarningYesNoCancel = 0
        Information = 0
        SSLMessageBox = 0
    
        def __init__(self, protocol, pool_socket, app_socket):
            '''void KIO.SlaveBase.__init__(QByteArray protocol, QByteArray pool_socket, QByteArray app_socket)'''
        def waitForHostInfo(self, info):
            '''int KIO.SlaveBase.waitForHostInfo(QHostInfo info)'''
            return int()
        def lookupHost(self, host):
            '''void KIO.SlaveBase.lookupHost(QString host)'''
        def setKillFlag(self):
            '''void KIO.SlaveBase.setKillFlag()'''
        def wasKilled(self):
            '''bool KIO.SlaveBase.wasKilled()'''
            return bool()
        def sendAndKeepMetaData(self):
            '''void KIO.SlaveBase.sendAndKeepMetaData()'''
        def sendMetaData(self):
            '''void KIO.SlaveBase.sendMetaData()'''
        def waitForAnswer(self, expected1, expected2, data, pCmd):
            '''int KIO.SlaveBase.waitForAnswer(int expected1, int expected2, QByteArray data, int pCmd)'''
            return int()
        def dropNetwork(self, host = QString()):
            '''void KIO.SlaveBase.dropNetwork(QString host = QString())'''
        def requestNetwork(self, host = QString()):
            '''bool KIO.SlaveBase.requestNetwork(QString host = QString())'''
            return bool()
        def cacheAuthentication(self, info):
            '''bool KIO.SlaveBase.cacheAuthentication(KIO.AuthInfo info)'''
            return bool()
        def checkCachedAuthentication(self, info):
            '''bool KIO.SlaveBase.checkCachedAuthentication(KIO.AuthInfo info)'''
            return bool()
        def openPasswordDialog(self, info, errorMsg = QString()):
            '''bool KIO.SlaveBase.openPasswordDialog(KIO.AuthInfo info, QString errorMsg = QString())'''
            return bool()
        def disconnectSlave(self):
            '''void KIO.SlaveBase.disconnectSlave()'''
        def connectSlave(self, path):
            '''void KIO.SlaveBase.connectSlave(QString path)'''
        def listEntry(self, _entry, ready):
            '''void KIO.SlaveBase.listEntry(KIO.UDSEntry _entry, bool ready)'''
        def readData(self, buffer):
            '''int KIO.SlaveBase.readData(QByteArray buffer)'''
            return int()
        def dispatchOpenCommand(self, command, data):
            '''void KIO.SlaveBase.dispatchOpenCommand(int command, QByteArray data)'''
        def dispatch(self, command, data):
            '''void KIO.SlaveBase.dispatch(int command, QByteArray data)'''
        def setTimeoutSpecialCommand(self, timeout, data = QByteArray()):
            '''void KIO.SlaveBase.setTimeoutSpecialCommand(int timeout, QByteArray data = QByteArray())'''
        def readTimeout(self):
            '''int KIO.SlaveBase.readTimeout()'''
            return int()
        def responseTimeout(self):
            '''int KIO.SlaveBase.responseTimeout()'''
            return int()
        def proxyConnectTimeout(self):
            '''int KIO.SlaveBase.proxyConnectTimeout()'''
            return int()
        def connectTimeout(self):
            '''int KIO.SlaveBase.connectTimeout()'''
            return int()
        def reparseConfiguration(self):
            '''void KIO.SlaveBase.reparseConfiguration()'''
        def slave_status(self):
            '''void KIO.SlaveBase.slave_status()'''
        def multiGet(self, data):
            '''void KIO.SlaveBase.multiGet(QByteArray data)'''
        def special(self, data):
            '''void KIO.SlaveBase.special(QByteArray data)'''
        def setLinkDest(self, url, target):
            '''void KIO.SlaveBase.setLinkDest(KUrl url, QString target)'''
        def del_(self, url, isfile):
            '''void KIO.SlaveBase.del_(KUrl url, bool isfile)'''
        def copy(self, src, dest, permissions, flags):
            '''void KIO.SlaveBase.copy(KUrl src, KUrl dest, int permissions, KIO.JobFlags flags)'''
        def setModificationTime(self, url, mtime):
            '''void KIO.SlaveBase.setModificationTime(KUrl url, QDateTime mtime)'''
        def chown(self, url, owner, group):
            '''void KIO.SlaveBase.chown(KUrl url, QString owner, QString group)'''
        def chmod(self, url, permissions):
            '''void KIO.SlaveBase.chmod(KUrl url, int permissions)'''
        def symlink(self, target, dest, flags):
            '''void KIO.SlaveBase.symlink(QString target, KUrl dest, KIO.JobFlags flags)'''
        def rename(self, src, dest, flags):
            '''void KIO.SlaveBase.rename(KUrl src, KUrl dest, KIO.JobFlags flags)'''
        def mkdir(self, url, permissions):
            '''void KIO.SlaveBase.mkdir(KUrl url, int permissions)'''
        def listDir(self, url):
            '''void KIO.SlaveBase.listDir(KUrl url)'''
        def mimetype(self, url):
            '''void KIO.SlaveBase.mimetype(KUrl url)'''
        def stat(self, url):
            '''void KIO.SlaveBase.stat(KUrl url)'''
        def put(self, url, permissions, flags):
            '''void KIO.SlaveBase.put(KUrl url, int permissions, KIO.JobFlags flags)'''
        def close(self):
            '''void KIO.SlaveBase.close()'''
        def seek(self, offset):
            '''void KIO.SlaveBase.seek(int offset)'''
        def write(self, data):
            '''void KIO.SlaveBase.write(QByteArray data)'''
        def read(self, size):
            '''void KIO.SlaveBase.read(int size)'''
        def open(self, url, mode):
            '''void KIO.SlaveBase.open(KUrl url, QIODevice.OpenMode mode)'''
        def get(self, url):
            '''void KIO.SlaveBase.get(KUrl url)'''
        def closeConnection(self):
            '''void KIO.SlaveBase.closeConnection()'''
        def openConnection(self):
            '''void KIO.SlaveBase.openConnection()'''
        def setSubUrl(self, url):
            '''void KIO.SlaveBase.setSubUrl(KUrl url)'''
        def setHost(self, host, port, user, pass_):
            '''void KIO.SlaveBase.setHost(QString host, int port, QString user, QString pass)'''
        def remoteEncoding(self):
            '''KRemoteEncoding KIO.SlaveBase.remoteEncoding()'''
            return KRemoteEncoding()
        def config(self):
            '''KConfigGroup KIO.SlaveBase.config()'''
            return KConfigGroup()
        def allMetaData(self):
            '''MetaData KIO.SlaveBase.allMetaData()'''
            return MetaData()
        def metaData(self, key):
            '''QString KIO.SlaveBase.metaData(QString key)'''
            return QString()
        def hasMetaData(self, key):
            '''bool KIO.SlaveBase.hasMetaData(QString key)'''
            return bool()
        def setMetaData(self, key, value):
            '''void KIO.SlaveBase.setMetaData(QString key, QString value)'''
        def messageBox(self, type, text, caption = QString(), buttonYes = i18nYes, buttonNo = i18nNo):
            '''int KIO.SlaveBase.messageBox(KIO.SlaveBase.MessageBoxType type, QString text, QString caption = QString(), QString buttonYes = i18nYes, QString buttonNo = i18nNo)'''
            return int()
        def messageBox(self, text, type, caption = QString(), buttonYes = i18nYes, buttonNo = i18nNo, dontAskAgainName = QString()):
            '''int KIO.SlaveBase.messageBox(QString text, KIO.SlaveBase.MessageBoxType type, QString caption = QString(), QString buttonYes = i18nYes, QString buttonNo = i18nNo, QString dontAskAgainName = QString())'''
            return int()
        def infoMessage(self, msg):
            '''void KIO.SlaveBase.infoMessage(QString msg)'''
        def warning(self, msg):
            '''void KIO.SlaveBase.warning(QString msg)'''
        def mimeType(self, _type):
            '''void KIO.SlaveBase.mimeType(QString _type)'''
        def errorPage(self):
            '''void KIO.SlaveBase.errorPage()'''
        def redirection(self, _url):
            '''void KIO.SlaveBase.redirection(KUrl _url)'''
        def speed(self, _bytes_per_second):
            '''void KIO.SlaveBase.speed(int _bytes_per_second)'''
        def processedPercent(self, percent):
            '''void KIO.SlaveBase.processedPercent(float percent)'''
        def written(self, _bytes):
            '''void KIO.SlaveBase.written(int _bytes)'''
        def position(self, _pos):
            '''void KIO.SlaveBase.position(int _pos)'''
        def processedSize(self, _bytes):
            '''void KIO.SlaveBase.processedSize(int _bytes)'''
        def totalSize(self, _bytes):
            '''void KIO.SlaveBase.totalSize(int _bytes)'''
        def canResume(self, offset):
            '''bool KIO.SlaveBase.canResume(int offset)'''
            return bool()
        def canResume(self):
            '''void KIO.SlaveBase.canResume()'''
        def listEntries(self, _entry):
            '''void KIO.SlaveBase.listEntries(list-of-KIO.UDSEntry _entry)'''
        def statEntry(self, _entry):
            '''void KIO.SlaveBase.statEntry(KIO.UDSEntry _entry)'''
        def slaveStatus(self, host, connected):
            '''void KIO.SlaveBase.slaveStatus(QString host, bool connected)'''
        def needSubUrlData(self):
            '''void KIO.SlaveBase.needSubUrlData()'''
        def finished(self):
            '''void KIO.SlaveBase.finished()'''
        def connected(self):
            '''void KIO.SlaveBase.connected()'''
        def error(self, _errid, _text):
            '''void KIO.SlaveBase.error(int _errid, QString _text)'''
        def opened(self):
            '''void KIO.SlaveBase.opened()'''
        def dataReq(self):
            '''void KIO.SlaveBase.dataReq()'''
        def data(self, data):
            '''void KIO.SlaveBase.data(QByteArray data)'''
        def dispatchLoop(self):
            '''void KIO.SlaveBase.dispatchLoop()'''
        def exit(self):
            '''void KIO.SlaveBase.exit()'''
    class Job(KCompositeJob):
        """"""
        def __init__(self):
            '''void KIO.Job.__init__()'''
        def removeSubjob(self, job):
            '''bool KIO.Job.removeSubjob(KJob job)'''
            return bool()
        def addSubjob(self, job):
            '''bool KIO.Job.addSubjob(KJob job)'''
            return bool()
        connected = pyqtSignal() # void connected(KIO::Job *) - signal
        canceled = pyqtSignal() # void canceled(KJob *) - signal
        def queryMetaData(self, key):
            '''QString KIO.Job.queryMetaData(QString key)'''
            return QString()
        def metaData(self):
            '''MetaData KIO.Job.metaData()'''
            return MetaData()
        def outgoingMetaData(self):
            '''MetaData KIO.Job.outgoingMetaData()'''
            return MetaData()
        def mergeMetaData(self, values):
            '''void KIO.Job.mergeMetaData(dict-of-QString-QString values)'''
        def addMetaData(self, key, value):
            '''void KIO.Job.addMetaData(QString key, QString value)'''
        def addMetaData(self, values):
            '''void KIO.Job.addMetaData(dict-of-QString-QString values)'''
        def setMetaData(self, metaData):
            '''void KIO.Job.setMetaData(MetaData metaData)'''
        def parentJob(self):
            '''KIO.Job KIO.Job.parentJob()'''
            return KIO.Job()
        def setParentJob(self, parentJob):
            '''void KIO.Job.setParentJob(KIO.Job parentJob)'''
        def isInteractive(self):
            '''bool KIO.Job.isInteractive()'''
            return bool()
        def showErrorDialog(self, parent = None):
            '''void KIO.Job.showErrorDialog(QWidget parent = None)'''
        def detailedErrorStrings(self, reqUrl = None, method = None):
            '''QStringList KIO.Job.detailedErrorStrings(KUrl reqUrl = None, int method = -1)'''
            return QStringList()
        def errorString(self):
            '''QString KIO.Job.errorString()'''
            return QString()
        def doResume(self):
            '''bool KIO.Job.doResume()'''
            return bool()
        def doSuspend(self):
            '''bool KIO.Job.doSuspend()'''
            return bool()
        def doKill(self):
            '''bool KIO.Job.doKill()'''
            return bool()
        def ui(self):
            '''KIO.JobUiDelegate KIO.Job.ui()'''
            return KIO.JobUiDelegate()
        def start(self):
            '''void KIO.Job.start()'''
    class MultiGetJob(KIO.TransferJob):
        """"""
        def slotMimetype(self, mimetype):
            '''void KIO.MultiGetJob.slotMimetype(QString mimetype)'''
        def slotData(self, data):
            '''void KIO.MultiGetJob.slotData(QByteArray data)'''
        def slotFinished(self):
            '''void KIO.MultiGetJob.slotFinished()'''
        def slotRedirection(self, url):
            '''void KIO.MultiGetJob.slotRedirection(KUrl url)'''
        result = pyqtSignal() # void result(long) - signal
        mimetype = pyqtSignal() # void mimetype(long,const QStringamp;) - signal
        data = pyqtSignal() # void data(long,const QByteArrayamp;) - signal
        def get(self, id, url, metaData):
            '''void KIO.MultiGetJob.get(int id, KUrl url, MetaData metaData)'''
    class CopyJob(KIO.Job):
        """"""
        # Enum KIO.CopyJob.CopyMode
        Copy = 0
        Move = 0
        Link = 0
    
        def setAutoRename(self, autoRename):
            '''void KIO.CopyJob.setAutoRename(bool autoRename)'''
        def emitResult(self):
            '''void KIO.CopyJob.emitResult()'''
        def slotResult(self, job):
            '''void KIO.CopyJob.slotResult(KJob job)'''
        copyingLinkDone = pyqtSignal() # void copyingLinkDone(KIO::Job *,const KUrlamp;,const QStringamp;,const KUrlamp;) - signal
        copyingDone = pyqtSignal() # void copyingDone(KIO::Job *,const KUrlamp;,const KUrlamp;,time_t,bool,bool) - signal
        renamed = pyqtSignal() # void renamed(KIO::Job *,const KUrlamp;,const KUrlamp;) - signal
        creatingDir = pyqtSignal() # void creatingDir(KIO::Job *,const KUrlamp;) - signal
        moving = pyqtSignal() # void moving(KIO::Job *,const KUrlamp;,const KUrlamp;) - signal
        linking = pyqtSignal() # void linking(KIO::Job *,const QStringamp;,const KUrlamp;) - signal
        copying = pyqtSignal() # void copying(KIO::Job *,const KUrlamp;,const KUrlamp;) - signal
        processedDirs = pyqtSignal() # void processedDirs(KIO::Job *,unsigned long) - signal
        processedFiles = pyqtSignal() # void processedFiles(KIO::Job *,unsigned long) - signal
        aboutToCreate = pyqtSignal() # void aboutToCreate(KIO::Job *,const QListlt;KIO::CopyInfogt;amp;) - signal
        totalDirs = pyqtSignal() # void totalDirs(KJob *,unsigned long) - signal
        totalFiles = pyqtSignal() # void totalFiles(KJob *,unsigned long) - signal
        def doSuspend(self):
            '''bool KIO.CopyJob.doSuspend()'''
            return bool()
        def setWriteIntoExistingDirectories(self, overwriteAllDirs):
            '''void KIO.CopyJob.setWriteIntoExistingDirectories(bool overwriteAllDirs)'''
        def setAutoSkip(self, autoSkip):
            '''void KIO.CopyJob.setAutoSkip(bool autoSkip)'''
        def setDefaultPermissions(self, b):
            '''void KIO.CopyJob.setDefaultPermissions(bool b)'''
        def destUrl(self):
            '''KUrl KIO.CopyJob.destUrl()'''
            return KUrl()
        def srcUrls(self):
            '''KUrl.List KIO.CopyJob.srcUrls()'''
            return KUrl.List()
        def operationMode(self):
            '''KIO.CopyJob.CopyMode KIO.CopyJob.operationMode()'''
            return KIO.CopyJob.CopyMode()
    class FileUndoManager(QObject):
        """"""
        # Enum KIO.FileUndoManager.CommandType
        Copy = 0
        Move = 0
        Rename = 0
        Link = 0
        Mkdir = 0
        Trash = 0
        Put = 0
    
        jobRecordingFinished = pyqtSignal() # void jobRecordingFinished(KIO::FileUndoManager::CommandType) - signal
        jobRecordingStarted = pyqtSignal() # void jobRecordingStarted(KIO::FileUndoManager::CommandType) - signal
        undoJobFinished = pyqtSignal() # void undoJobFinished() - signal
        undoTextChanged = pyqtSignal() # void undoTextChanged(const QStringamp;) - signal
        def undo(self):
            '''void KIO.FileUndoManager.undo()'''
        def currentCommandSerialNumber(self):
            '''int KIO.FileUndoManager.currentCommandSerialNumber()'''
            return int()
        def newCommandSerialNumber(self):
            '''int KIO.FileUndoManager.newCommandSerialNumber()'''
            return int()
        def undoText(self):
            '''QString KIO.FileUndoManager.undoText()'''
            return QString()
        def undoAvailable(self):
            '''bool KIO.FileUndoManager.undoAvailable()'''
            return bool()
        undoAvailable = pyqtSignal() # void undoAvailable(bool) - signal
        def recordCopyJob(self, copyJob):
            '''void KIO.FileUndoManager.recordCopyJob(KIO.CopyJob copyJob)'''
        def recordJob(self, op, src, dst, job):
            '''void KIO.FileUndoManager.recordJob(KIO.FileUndoManager.CommandType op, KUrl.List src, KUrl dst, KIO.Job job)'''
        def uiInterface(self):
            '''KIO.FileUndoManager.UiInterface KIO.FileUndoManager.uiInterface()'''
            return KIO.FileUndoManager.UiInterface()
        def setUiInterface(self, ui):
            '''void KIO.FileUndoManager.setUiInterface(KIO.FileUndoManager.UiInterface ui)'''
        def self(self):
            '''static KIO.FileUndoManager KIO.FileUndoManager.self()'''
            return KIO.FileUndoManager()
    class MetaInfoJob(KIO.Job):
        """"""
        def __init__(self, items, w = None, iocost = 3, cpucost = 6, requiredfields = QStringList(), requestedfields = QStringList()):
            '''void KIO.MetaInfoJob.__init__(KFileItemList items, KFileMetaInfo.WhatFlags w = KFileMetaInfo.Everything, int iocost = 3, int cpucost = 6, QStringList requiredfields = QStringList(), QStringList requestedfields = QStringList())'''
        def slotResult(self, job):
            '''void KIO.MetaInfoJob.slotResult(KJob job)'''
        def getMetaInfo(self):
            '''void KIO.MetaInfoJob.getMetaInfo()'''
        failed = pyqtSignal() # void failed(const KFileItemamp;) - signal
        gotMetaInfo = pyqtSignal() # void gotMetaInfo(const KFileItemamp;) - signal
        def removeItem(self, item):
            '''void KIO.MetaInfoJob.removeItem(KFileItem item)'''
    class SessionData(QObject):
        """"""
        def __init__(self):
            '''void KIO.SessionData.__init__()'''
        def reset(self):
            '''void KIO.SessionData.reset()'''
        def configDataFor(self, configData, proto, host):
            '''void KIO.SessionData.configDataFor(MetaData configData, QString proto, QString host)'''
    class FileCopyJob(KIO.Job):
        """"""
        def slotResult(self, job):
            '''void KIO.FileCopyJob.slotResult(KJob job)'''
        mimetype = pyqtSignal() # void mimetype(KIO::Job *,const QStringamp;) - signal
        def doResume(self):
            '''bool KIO.FileCopyJob.doResume()'''
            return bool()
        def doSuspend(self):
            '''bool KIO.FileCopyJob.doSuspend()'''
            return bool()
        def destUrl(self):
            '''KUrl KIO.FileCopyJob.destUrl()'''
            return KUrl()
        def srcUrl(self):
            '''KUrl KIO.FileCopyJob.srcUrl()'''
            return KUrl()
        def setModificationTime(self, mtime):
            '''void KIO.FileCopyJob.setModificationTime(QDateTime mtime)'''
        def setSourceSize(self, size):
            '''void KIO.FileCopyJob.setSourceSize(int size)'''
    class Slave(KIO.SlaveInterface):
        """"""
        def __init__(self, protocol, parent = None):
            '''void KIO.Slave.__init__(QString protocol, QObject parent = None)'''
        def checkForHeldSlave(self, url):
            '''static bool KIO.Slave.checkForHeldSlave(KUrl url)'''
            return bool()
        def job(self):
            '''KIO.SimpleJob KIO.Slave.job()'''
            return KIO.SimpleJob()
        def setJob(self, job):
            '''void KIO.Slave.setJob(KIO.SimpleJob job)'''
        slaveDied = pyqtSignal() # void slaveDied(KIO::Slave *) - signal
        def timeout(self):
            '''void KIO.Slave.timeout()'''
        def gotInput(self):
            '''void KIO.Slave.gotInput()'''
        def accept(self):
            '''void KIO.Slave.accept()'''
        def deref(self):
            '''void KIO.Slave.deref()'''
        def ref(self):
            '''void KIO.Slave.ref()'''
        def setConnected(self, c):
            '''void KIO.Slave.setConnected(bool c)'''
        def isConnected(self):
            '''bool KIO.Slave.isConnected()'''
            return bool()
        def setIdle(self):
            '''void KIO.Slave.setIdle()'''
        def idleTime(self):
            '''int KIO.Slave.idleTime()'''
            return int()
        def hold(self, url):
            '''void KIO.Slave.hold(KUrl url)'''
        def send(self, cmd, arr = QByteArray()):
            '''void KIO.Slave.send(int cmd, QByteArray arr = QByteArray())'''
        def suspended(self):
            '''bool KIO.Slave.suspended()'''
            return bool()
        def resume(self):
            '''void KIO.Slave.resume()'''
        def suspend(self):
            '''void KIO.Slave.suspend()'''
        def holdSlave(self, protocol, url):
            '''static KIO.Slave KIO.Slave.holdSlave(QString protocol, KUrl url)'''
            return KIO.Slave()
        def createSlave(self, protocol, url, error, error_text):
            '''static KIO.Slave KIO.Slave.createSlave(QString protocol, KUrl url, int error, QString error_text)'''
            return KIO.Slave()
        def passwd(self):
            '''QString KIO.Slave.passwd()'''
            return QString()
        def user(self):
            '''QString KIO.Slave.user()'''
            return QString()
        def port(self):
            '''int KIO.Slave.port()'''
            return int()
        def host(self):
            '''QString KIO.Slave.host()'''
            return QString()
        def slaveProtocol(self):
            '''QString KIO.Slave.slaveProtocol()'''
            return QString()
        def setProtocol(self, protocol):
            '''void KIO.Slave.setProtocol(QString protocol)'''
        def protocol(self):
            '''QString KIO.Slave.protocol()'''
            return QString()
        def setConfig(self, config):
            '''void KIO.Slave.setConfig(MetaData config)'''
        def resetHost(self):
            '''void KIO.Slave.resetHost()'''
        def setHost(self, host, port, user, passwd):
            '''void KIO.Slave.setHost(QString host, int port, QString user, QString passwd)'''
        def isAlive(self):
            '''bool KIO.Slave.isAlive()'''
            return bool()
        def kill(self):
            '''void KIO.Slave.kill()'''
        def slave_pid(self):
            '''int KIO.Slave.slave_pid()'''
            return int()
        def setPID(self):
            '''int KIO.Slave.setPID()'''
            return int()
    class JobFlags():
        """"""
        def __init__(self):
            '''KIO.JobFlags KIO.JobFlags.__init__()'''
            return KIO.JobFlags()
        def __init__(self):
            '''int KIO.JobFlags.__init__()'''
            return int()
        def __init__(self):
            '''void KIO.JobFlags.__init__()'''
        def __bool__(self):
            '''int KIO.JobFlags.__bool__()'''
            return int()
        def __ne__(self, f):
            '''bool KIO.JobFlags.__ne__(KIO.JobFlags f)'''
            return bool()
        def __eq__(self, f):
            '''bool KIO.JobFlags.__eq__(KIO.JobFlags f)'''
            return bool()
        def __invert__(self):
            '''KIO.JobFlags KIO.JobFlags.__invert__()'''
            return KIO.JobFlags()
        def __and__(self, mask):
            '''KIO.JobFlags KIO.JobFlags.__and__(int mask)'''
            return KIO.JobFlags()
        def __xor__(self, f):
            '''KIO.JobFlags KIO.JobFlags.__xor__(KIO.JobFlags f)'''
            return KIO.JobFlags()
        def __xor__(self, f):
            '''KIO.JobFlags KIO.JobFlags.__xor__(int f)'''
            return KIO.JobFlags()
        def __or__(self, f):
            '''KIO.JobFlags KIO.JobFlags.__or__(KIO.JobFlags f)'''
            return KIO.JobFlags()
        def __or__(self, f):
            '''KIO.JobFlags KIO.JobFlags.__or__(int f)'''
            return KIO.JobFlags()
        def __int__(self):
            '''int KIO.JobFlags.__int__()'''
            return int()
        def __ixor__(self, f):
            '''KIO.JobFlags KIO.JobFlags.__ixor__(KIO.JobFlags f)'''
            return KIO.JobFlags()
        def __ior__(self, f):
            '''KIO.JobFlags KIO.JobFlags.__ior__(KIO.JobFlags f)'''
            return KIO.JobFlags()
        def __iand__(self, mask):
            '''KIO.JobFlags KIO.JobFlags.__iand__(int mask)'''
            return KIO.JobFlags()


class KAbstractFileItemActionPlugin(QObject):
    """"""
    def __init__(self, parent):
        '''void KAbstractFileItemActionPlugin.__init__(QObject parent)'''
    def actions(self, fileItemInfos, parentWidget):
        '''abstract list-of-QAction KAbstractFileItemActionPlugin.actions(KFileItemListProperties fileItemInfos, QWidget parentWidget)'''
        return [QAction()]


class KAbstractFileModule(QObject):
    """"""
    def __init__(self, parent):
        '''void KAbstractFileModule.__init__(QObject parent)'''
    def selectDirectory(self, startDir, localOnly, parent, caption):
        '''abstract KUrl KAbstractFileModule.selectDirectory(KUrl startDir, bool localOnly, QWidget parent, QString caption)'''
        return KUrl()
    def setStartDir(self, directory):
        '''abstract void KAbstractFileModule.setStartDir(KUrl directory)'''
    def getStartUrl(self, startDir, recentDirClass):
        '''abstract KUrl KAbstractFileModule.getStartUrl(KUrl startDir, QString recentDirClass)'''
        return KUrl()
    def createFileWidget(self, startDir, parent):
        '''abstract QWidget KAbstractFileModule.createFileWidget(KUrl startDir, QWidget parent)'''
        return QWidget()


class KAbstractFileWidget():
    """"""
    # Enum KAbstractFileWidget.OperationMode
    Other = 0
    Opening = 0
    Saving = 0

    def __init__(self):
        '''void KAbstractFileWidget.__init__()'''
    def __init__(self):
        '''KAbstractFileWidget KAbstractFileWidget.__init__()'''
        return KAbstractFileWidget()
    def setInlinePreviewShown(self, show):
        '''void KAbstractFileWidget.setInlinePreviewShown(bool show)'''
    def setConfirmOverwrite(self, enable):
        '''void KAbstractFileWidget.setConfirmOverwrite(bool enable)'''
    def virtual_hook(self, id, data):
        '''abstract void KAbstractFileWidget.virtual_hook(int id, sip.voidptr data)'''
    def slotCancel(self):
        '''abstract void KAbstractFileWidget.slotCancel()'''
    def accept(self):
        '''abstract void KAbstractFileWidget.accept()'''
    def slotOk(self):
        '''abstract void KAbstractFileWidget.slotOk()'''
    def setCustomWidget(self, widget):
        '''abstract void KAbstractFileWidget.setCustomWidget(QWidget widget)'''
    def setCustomWidget(self, text, widget):
        '''abstract void KAbstractFileWidget.setCustomWidget(QString text, QWidget widget)'''
    def actionCollection(self):
        '''abstract KActionCollection KAbstractFileWidget.actionCollection()'''
        return KActionCollection()
    def filterWidget(self):
        '''abstract KFileFilterCombo KAbstractFileWidget.filterWidget()'''
        return KFileFilterCombo()
    def locationEdit(self):
        '''abstract KUrlComboBox KAbstractFileWidget.locationEdit()'''
        return KUrlComboBox()
    def cancelButton(self):
        '''abstract KPushButton KAbstractFileWidget.cancelButton()'''
        return KPushButton()
    def okButton(self):
        '''abstract KPushButton KAbstractFileWidget.okButton()'''
        return KPushButton()
    def toolBar(self):
        '''abstract KToolBar KAbstractFileWidget.toolBar()'''
        return KToolBar()
    def setLocationLabel(self, text):
        '''abstract void KAbstractFileWidget.setLocationLabel(QString text)'''
    def mode(self):
        '''abstract KFile.Modes KAbstractFileWidget.mode()'''
        return KFile.Modes()
    def setMode(self, m):
        '''abstract void KAbstractFileWidget.setMode(KFile.Modes m)'''
    def setPreviewWidget(self, w):
        '''abstract void KAbstractFileWidget.setPreviewWidget(KPreviewWidgetBase w)'''
    def clearFilter(self):
        '''abstract void KAbstractFileWidget.clearFilter()'''
    def currentMimeFilter(self):
        '''abstract QString KAbstractFileWidget.currentMimeFilter()'''
        return QString()
    def setMimeFilter(self, types, defaultType = QString()):
        '''abstract void KAbstractFileWidget.setMimeFilter(QStringList types, QString defaultType = QString())'''
    def currentFilterMimeType(self):
        '''abstract unknown-type KAbstractFileWidget.currentFilterMimeType()'''
        return unknown-type()
    def currentFilter(self):
        '''abstract QString KAbstractFileWidget.currentFilter()'''
        return QString()
    def setFilter(self, filter):
        '''abstract void KAbstractFileWidget.setFilter(QString filter)'''
    def keepsLocation(self):
        '''abstract bool KAbstractFileWidget.keepsLocation()'''
        return bool()
    def setKeepLocation(self, keep):
        '''abstract void KAbstractFileWidget.setKeepLocation(bool keep)'''
    def operationMode(self):
        '''abstract KAbstractFileWidget.OperationMode KAbstractFileWidget.operationMode()'''
        return KAbstractFileWidget.OperationMode()
    def setOperationMode(self):
        '''abstract KAbstractFileWidget.OperationMode KAbstractFileWidget.setOperationMode()'''
        return KAbstractFileWidget.OperationMode()
    def setSelection(self, name):
        '''abstract void KAbstractFileWidget.setSelection(QString name)'''
    def setUrl(self, url, clearforward = True):
        '''abstract void KAbstractFileWidget.setUrl(KUrl url, bool clearforward = True)'''
    def selectedFiles(self):
        '''abstract QStringList KAbstractFileWidget.selectedFiles()'''
        return QStringList()
    def selectedFile(self):
        '''abstract QString KAbstractFileWidget.selectedFile()'''
        return QString()
    def baseUrl(self):
        '''abstract KUrl KAbstractFileWidget.baseUrl()'''
        return KUrl()
    def selectedUrls(self):
        '''abstract KUrl.List KAbstractFileWidget.selectedUrls()'''
        return KUrl.List()
    def selectedUrl(self):
        '''abstract KUrl KAbstractFileWidget.selectedUrl()'''
        return KUrl()


class KACL():
    """"""
    def __init__(self, aclString):
        '''void KACL.__init__(QString aclString)'''
    def __init__(self, rhs):
        '''void KACL.__init__(KACL rhs)'''
    def __init__(self, basicPermissions):
        '''void KACL.__init__(int basicPermissions)'''
    def __init__(self):
        '''void KACL.__init__()'''
    def asString(self):
        '''QString KACL.asString()'''
        return QString()
    def setACL(self, aclStr):
        '''bool KACL.setACL(QString aclStr)'''
        return bool()
    def setAllGroupPermissions(self):
        '''ACLUserPermissionsList KACL.setAllGroupPermissions()'''
        return ACLUserPermissionsList()
    def allGroupPermissions(self):
        '''ACLUserPermissionsList KACL.allGroupPermissions()'''
        return ACLUserPermissionsList()
    def setNamedGroupPermissions(self, name):
        '''int KACL.setNamedGroupPermissions(QString name)'''
        return int()
    def namedGroupPermissions(self, name, exists):
        '''int KACL.namedGroupPermissions(QString name, bool exists)'''
        return int()
    def setAllUserPermissions(self, list):
        '''bool KACL.setAllUserPermissions(ACLUserPermissionsList list)'''
        return bool()
    def allUserPermissions(self):
        '''ACLUserPermissionsList KACL.allUserPermissions()'''
        return ACLUserPermissionsList()
    def setNamedUserPermissions(self, name):
        '''int KACL.setNamedUserPermissions(QString name)'''
        return int()
    def namedUserPermissions(self, name, exists):
        '''int KACL.namedUserPermissions(QString name, bool exists)'''
        return int()
    def setMaskPermissions(self):
        '''int KACL.setMaskPermissions()'''
        return int()
    def maskPermissions(self, exists):
        '''int KACL.maskPermissions(bool exists)'''
        return int()
    def isExtended(self):
        '''bool KACL.isExtended()'''
        return bool()
    def basePermissions(self):
        '''int KACL.basePermissions()'''
        return int()
    def setOthersPermissions(self):
        '''int KACL.setOthersPermissions()'''
        return int()
    def othersPermissions(self):
        '''int KACL.othersPermissions()'''
        return int()
    def setOwningGroupPermissions(self):
        '''int KACL.setOwningGroupPermissions()'''
        return int()
    def owningGroupPermissions(self):
        '''int KACL.owningGroupPermissions()'''
        return int()
    def setOwnerPermissions(self):
        '''int KACL.setOwnerPermissions()'''
        return int()
    def ownerPermissions(self):
        '''int KACL.ownerPermissions()'''
        return int()
    def isValid(self):
        '''bool KACL.isValid()'''
        return bool()
    def __ne__(self, rhs):
        '''bool KACL.__ne__(KACL rhs)'''
        return bool()
    def __eq__(self, rhs):
        '''bool KACL.__eq__(KACL rhs)'''
        return bool()


class KArchive():
    """"""
    UnknownTime = None # int - member
    def __init__(self, fileName):
        '''void KArchive.__init__(QString fileName)'''
    def __init__(self, dev):
        '''void KArchive.__init__(QIODevice dev)'''
    def setRootDir(self, rootDir):
        '''void KArchive.setRootDir(KArchiveDirectory rootDir)'''
    def setDevice(self, dev):
        '''void KArchive.setDevice(QIODevice dev)'''
    def createDevice(self, mode):
        '''bool KArchive.createDevice(QIODevice.OpenMode mode)'''
        return bool()
    def findOrCreate(self, path):
        '''KArchiveDirectory KArchive.findOrCreate(QString path)'''
        return KArchiveDirectory()
    def doFinishWriting(self, size):
        '''abstract bool KArchive.doFinishWriting(int size)'''
        return bool()
    def doPrepareWriting(self, name, user, group, size, perm, atime, mtime, ctime):
        '''abstract bool KArchive.doPrepareWriting(QString name, QString user, QString group, int size, int perm, int atime, int mtime, int ctime)'''
        return bool()
    def doWriteSymLink(self, name, target, user, group, perm, atime, mtime, ctime):
        '''abstract bool KArchive.doWriteSymLink(QString name, QString target, QString user, QString group, int perm, int atime, int mtime, int ctime)'''
        return bool()
    def doWriteDir(self, name, user, group, perm, atime, mtime, ctime):
        '''abstract bool KArchive.doWriteDir(QString name, QString user, QString group, int perm, int atime, int mtime, int ctime)'''
        return bool()
    def rootDir(self):
        '''KArchiveDirectory KArchive.rootDir()'''
        return KArchiveDirectory()
    def closeArchive(self):
        '''abstract bool KArchive.closeArchive()'''
        return bool()
    def openArchive(self, mode):
        '''abstract bool KArchive.openArchive(QIODevice.OpenMode mode)'''
        return bool()
    def finishWriting(self, size):
        '''bool KArchive.finishWriting(int size)'''
        return bool()
    def writeData(self, data, size):
        '''bool KArchive.writeData(str data, int size)'''
        return bool()
    def prepareWriting(self, name, user, group, size, perm = 33188, atime = None, mtime = None, ctime = None):
        '''bool KArchive.prepareWriting(QString name, QString user, QString group, int size, int perm = 33188, int atime = KArchive.UnknownTime, int mtime = KArchive.UnknownTime, int ctime = KArchive.UnknownTime)'''
        return bool()
    def writeFile(self, name, user, group, data, size, perm = 33188, atime = None, mtime = None, ctime = None):
        '''bool KArchive.writeFile(QString name, QString user, QString group, str data, int size, int perm = 33188, int atime = KArchive.UnknownTime, int mtime = KArchive.UnknownTime, int ctime = KArchive.UnknownTime)'''
        return bool()
    def writeSymLink(self, name, target, user, group, perm = 41453, atime = None, mtime = None, ctime = None):
        '''bool KArchive.writeSymLink(QString name, QString target, QString user, QString group, int perm = 41453, int atime = KArchive.UnknownTime, int mtime = KArchive.UnknownTime, int ctime = KArchive.UnknownTime)'''
        return bool()
    def writeDir(self, name, user, group, perm = 16877, atime = None, mtime = None, ctime = None):
        '''bool KArchive.writeDir(QString name, QString user, QString group, int perm = 16877, int atime = KArchive.UnknownTime, int mtime = KArchive.UnknownTime, int ctime = KArchive.UnknownTime)'''
        return bool()
    def addLocalDirectory(self, path, destName):
        '''bool KArchive.addLocalDirectory(QString path, QString destName)'''
        return bool()
    def addLocalFile(self, fileName, destName):
        '''bool KArchive.addLocalFile(QString fileName, QString destName)'''
        return bool()
    def directory(self):
        '''KArchiveDirectory KArchive.directory()'''
        return KArchiveDirectory()
    def fileName(self):
        '''QString KArchive.fileName()'''
        return QString()
    def device(self):
        '''QIODevice KArchive.device()'''
        return QIODevice()
    def mode(self):
        '''QIODevice.OpenMode KArchive.mode()'''
        return QIODevice.OpenMode()
    def isOpen(self):
        '''bool KArchive.isOpen()'''
        return bool()
    def close(self):
        '''bool KArchive.close()'''
        return bool()
    def open(self, mode):
        '''bool KArchive.open(QIODevice.OpenMode mode)'''
        return bool()


class KAr(KArchive):
    """"""
    def __init__(self, filename):
        '''void KAr.__init__(QString filename)'''
    def __init__(self, dev):
        '''void KAr.__init__(QIODevice dev)'''
    def closeArchive(self):
        '''bool KAr.closeArchive()'''
        return bool()
    def openArchive(self, mode):
        '''bool KAr.openArchive(QIODevice.OpenMode mode)'''
        return bool()
    def doWriteSymLink(self, name, target, user, group, perm, atime, mtime, ctime):
        '''bool KAr.doWriteSymLink(QString name, QString target, QString user, QString group, int perm, int atime, int mtime, int ctime)'''
        return bool()
    def doWriteDir(self, name, user, group, perm, atime, mtime, ctime):
        '''bool KAr.doWriteDir(QString name, QString user, QString group, int perm, int atime, int mtime, int ctime)'''
        return bool()
    def doFinishWriting(self, size):
        '''bool KAr.doFinishWriting(int size)'''
        return bool()
    def doPrepareWriting(self, name, user, group, size, perm, atime, mtime, ctime):
        '''bool KAr.doPrepareWriting(QString name, QString user, QString group, int size, int perm, int atime, int mtime, int ctime)'''
        return bool()


class KArchiveEntry():
    """"""
    def __init__(self, archive, name, access, date, user, group, symlink):
        '''void KArchiveEntry.__init__(KArchive archive, QString name, int access, int date, QString user, QString group, QString symlink)'''
    def archive(self):
        '''KArchive KArchiveEntry.archive()'''
        return KArchive()
    def isDirectory(self):
        '''bool KArchiveEntry.isDirectory()'''
        return bool()
    def isFile(self):
        '''bool KArchiveEntry.isFile()'''
        return bool()
    def symLinkTarget(self):
        '''QString KArchiveEntry.symLinkTarget()'''
        return QString()
    def group(self):
        '''QString KArchiveEntry.group()'''
        return QString()
    def user(self):
        '''QString KArchiveEntry.user()'''
        return QString()
    def permissions(self):
        '''int KArchiveEntry.permissions()'''
        return int()
    def name(self):
        '''QString KArchiveEntry.name()'''
        return QString()
    def date(self):
        '''int KArchiveEntry.date()'''
        return int()
    def datetime(self):
        '''QDateTime KArchiveEntry.datetime()'''
        return QDateTime()


class KArchiveFile(KArchiveEntry):
    """"""
    def __init__(self, archive, name, access, date, user, group, symlink, pos, size):
        '''void KArchiveFile.__init__(KArchive archive, QString name, int access, int date, QString user, QString group, QString symlink, int pos, int size)'''
    def copyTo(self, dest):
        '''void KArchiveFile.copyTo(QString dest)'''
    def isFile(self):
        '''bool KArchiveFile.isFile()'''
        return bool()
    def createDevice(self):
        '''QIODevice KArchiveFile.createDevice()'''
        return QIODevice()
    def data(self):
        '''QByteArray KArchiveFile.data()'''
        return QByteArray()
    def setSize(self, s):
        '''void KArchiveFile.setSize(int s)'''
    def size(self):
        '''int KArchiveFile.size()'''
        return int()
    def position(self):
        '''int KArchiveFile.position()'''
        return int()


class KArchiveDirectory(KArchiveEntry):
    """"""
    def __init__(self, archive, name, access, date, user, group, symlink):
        '''void KArchiveDirectory.__init__(KArchive archive, QString name, int access, int date, QString user, QString group, QString symlink)'''
    def copyTo(self, dest, recursive = True):
        '''void KArchiveDirectory.copyTo(QString dest, bool recursive = True)'''
    def isDirectory(self):
        '''bool KArchiveDirectory.isDirectory()'''
        return bool()
    def addEntry(self):
        '''KArchiveEntry KArchiveDirectory.addEntry()'''
        return KArchiveEntry()
    def entry(self, name):
        '''KArchiveEntry KArchiveDirectory.entry(QString name)'''
        return KArchiveEntry()
    def entries(self):
        '''QStringList KArchiveDirectory.entries()'''
        return QStringList()


class KAutoMount(QObject):
    """"""
    def __init__(self, readonly, format, device, mountpoint, desktopFile, show_filemanager_window = True):
        '''void KAutoMount.__init__(bool readonly, QByteArray format, QString device, QString mountpoint, QString desktopFile, bool show_filemanager_window = True)'''
    error = pyqtSignal() # void error() - signal
    finished = pyqtSignal() # void finished() - signal


class KAutoUnmount(QObject):
    """"""
    def __init__(self, mountpoint, desktopFile):
        '''void KAutoUnmount.__init__(QString mountpoint, QString desktopFile)'''
    error = pyqtSignal() # void error() - signal
    finished = pyqtSignal() # void finished() - signal


class KBookmark():
    """"""
    # Enum KBookmark.MetaDataOverwriteMode
    OverwriteMetaData = 0
    DontOverwriteMetaData = 0

    def __init__(self):
        '''void KBookmark.__init__()'''
    def __init__(self, elem):
        '''void KBookmark.__init__(QDomElement elem)'''
    def __init__(self):
        '''KBookmark KBookmark.__init__()'''
        return KBookmark()
    def __ne__(self, rhs):
        '''bool KBookmark.__ne__(KBookmark rhs)'''
        return bool()
    def setDescription(self, description):
        '''void KBookmark.setDescription(QString description)'''
    def description(self):
        '''QString KBookmark.description()'''
        return QString()
    def __eq__(self, rhs):
        '''bool KBookmark.__eq__(KBookmark rhs)'''
        return bool()
    def populateMimeData(self, mimeData):
        '''void KBookmark.populateMimeData(QMimeData mimeData)'''
    def setMetaDataItem(self, key, value, mode = None):
        '''void KBookmark.setMetaDataItem(QString key, QString value, KBookmark.MetaDataOverwriteMode mode = KBookmark.OverwriteMetaData)'''
    def metaDataItem(self, key):
        '''QString KBookmark.metaDataItem(QString key)'''
        return QString()
    def metaData(self, owner, create):
        '''QDomNode KBookmark.metaData(QString owner, bool create)'''
        return QDomNode()
    def commonParent(self, A, B):
        '''static QString KBookmark.commonParent(QString A, QString B)'''
        return QString()
    def nextAddress(self, address):
        '''static QString KBookmark.nextAddress(QString address)'''
        return QString()
    def previousAddress(self, address):
        '''static QString KBookmark.previousAddress(QString address)'''
        return QString()
    def parentAddress(self, address):
        '''static QString KBookmark.parentAddress(QString address)'''
        return QString()
    def updateAccessMetadata(self):
        '''void KBookmark.updateAccessMetadata()'''
    def internalElement(self):
        '''QDomElement KBookmark.internalElement()'''
        return QDomElement()
    def positionInParent(self):
        '''int KBookmark.positionInParent()'''
        return int()
    def positionInParent(self, address):
        '''static int KBookmark.positionInParent(QString address)'''
        return int()
    def address(self):
        '''QString KBookmark.address()'''
        return QString()
    def toGroup(self):
        '''KBookmarkGroup KBookmark.toGroup()'''
        return KBookmarkGroup()
    def parentGroup(self):
        '''KBookmarkGroup KBookmark.parentGroup()'''
        return KBookmarkGroup()
    def setShowInToolbar(self, show):
        '''void KBookmark.setShowInToolbar(bool show)'''
    def showInToolbar(self):
        '''bool KBookmark.showInToolbar()'''
        return bool()
    def setMimeType(self, mimeType):
        '''void KBookmark.setMimeType(QString mimeType)'''
    def mimeType(self):
        '''QString KBookmark.mimeType()'''
        return QString()
    def setIcon(self, icon):
        '''void KBookmark.setIcon(QString icon)'''
    def icon(self):
        '''QString KBookmark.icon()'''
        return QString()
    def setUrl(self, url):
        '''void KBookmark.setUrl(KUrl url)'''
    def url(self):
        '''KUrl KBookmark.url()'''
        return KUrl()
    def setFullText(self, fullText):
        '''void KBookmark.setFullText(QString fullText)'''
    def fullText(self):
        '''QString KBookmark.fullText()'''
        return QString()
    def text(self):
        '''QString KBookmark.text()'''
        return QString()
    def hasParent(self):
        '''bool KBookmark.hasParent()'''
        return bool()
    def isNull(self):
        '''bool KBookmark.isNull()'''
        return bool()
    def isSeparator(self):
        '''bool KBookmark.isSeparator()'''
        return bool()
    def isGroup(self):
        '''bool KBookmark.isGroup()'''
        return bool()
    def standaloneBookmark(self, text, url, icon = QString()):
        '''static KBookmark KBookmark.standaloneBookmark(QString text, KUrl url, QString icon = QString())'''
        return KBookmark()
    class List():
        """"""
        def __init__(self):
            '''void KBookmark.List.__init__()'''
        def __init__(self):
            '''KBookmark.List KBookmark.List.__init__()'''
            return KBookmark.List()
        def fromMimeData(self, mimeData):
            '''static KBookmark.List KBookmark.List.fromMimeData(QMimeData mimeData)'''
            return KBookmark.List()
        def fromMimeData(self, mimeData, parentDocument):
            '''static KBookmark.List KBookmark.List.fromMimeData(QMimeData mimeData, QDomDocument parentDocument)'''
            return KBookmark.List()
        def mimeDataTypes(self):
            '''static QStringList KBookmark.List.mimeDataTypes()'''
            return QStringList()
        def canDecode(self, mimeData):
            '''static bool KBookmark.List.canDecode(QMimeData mimeData)'''
            return bool()
        def populateMimeData(self, mimeData):
            '''void KBookmark.List.populateMimeData(QMimeData mimeData)'''


class KBookmarkGroup(KBookmark):
    """"""
    def __init__(self):
        '''void KBookmarkGroup.__init__()'''
    def __init__(self, elem):
        '''void KBookmarkGroup.__init__(QDomElement elem)'''
    def __init__(self):
        '''KBookmarkGroup KBookmarkGroup.__init__()'''
        return KBookmarkGroup()
    def nextKnownTag(self, start, goNext):
        '''QDomElement KBookmarkGroup.nextKnownTag(QDomElement start, bool goNext)'''
        return QDomElement()
    def groupUrlList(self):
        '''list-of-KUrl KBookmarkGroup.groupUrlList()'''
        return [KUrl()]
    def findToolbar(self):
        '''QDomElement KBookmarkGroup.findToolbar()'''
        return QDomElement()
    def isToolbarGroup(self):
        '''bool KBookmarkGroup.isToolbarGroup()'''
        return bool()
    def deleteBookmark(self, bk):
        '''void KBookmarkGroup.deleteBookmark(KBookmark bk)'''
    def moveItem(self, item, after):
        '''bool KBookmarkGroup.moveItem(KBookmark item, KBookmark after)'''
        return bool()
    def moveBookmark(self, bookmark, after):
        '''bool KBookmarkGroup.moveBookmark(KBookmark bookmark, KBookmark after)'''
        return bool()
    def addBookmark(self, bm):
        '''KBookmark KBookmarkGroup.addBookmark(KBookmark bm)'''
        return KBookmark()
    def addBookmark(self, text, url, icon = QString()):
        '''KBookmark KBookmarkGroup.addBookmark(QString text, KUrl url, QString icon = QString())'''
        return KBookmark()
    def createNewSeparator(self):
        '''KBookmark KBookmarkGroup.createNewSeparator()'''
        return KBookmark()
    def createNewFolder(self, text):
        '''KBookmarkGroup KBookmarkGroup.createNewFolder(QString text)'''
        return KBookmarkGroup()
    def indexOf(self, child):
        '''int KBookmarkGroup.indexOf(KBookmark child)'''
        return int()
    def next(self, current):
        '''KBookmark KBookmarkGroup.next(KBookmark current)'''
        return KBookmark()
    def previous(self, current):
        '''KBookmark KBookmarkGroup.previous(KBookmark current)'''
        return KBookmark()
    def first(self):
        '''KBookmark KBookmarkGroup.first()'''
        return KBookmark()
    def isOpen(self):
        '''bool KBookmarkGroup.isOpen()'''
        return bool()


class KBookmarkGroupTraverser():
    """"""
    def __init__(self):
        '''void KBookmarkGroupTraverser.__init__()'''
    def __init__(self):
        '''KBookmarkGroupTraverser KBookmarkGroupTraverser.__init__()'''
        return KBookmarkGroupTraverser()
    def visitLeave(self):
        '''KBookmarkGroup KBookmarkGroupTraverser.visitLeave()'''
        return KBookmarkGroup()
    def visitEnter(self):
        '''KBookmarkGroup KBookmarkGroupTraverser.visitEnter()'''
        return KBookmarkGroup()
    def visit(self):
        '''KBookmark KBookmarkGroupTraverser.visit()'''
        return KBookmark()
    def traverse(self):
        '''KBookmarkGroup KBookmarkGroupTraverser.traverse()'''
        return KBookmarkGroup()


class KBookmarkDialog(KDialog):
    """"""
    # Enum KBookmarkDialog.BookmarkDialogMode
    NewFolder = 0
    NewBookmark = 0
    EditBookmark = 0
    NewMultipleBookmarks = 0
    SelectFolder = 0

    def __init__(self):
        '''QWidget KBookmarkDialog.__init__()'''
        return QWidget()
    def addBookmarks(self, list, name = QString(), parent = KBookmarkGroup()):
        '''KBookmarkGroup KBookmarkDialog.addBookmarks(list-of-tuple-of-QString-QString list, QString name = QString(), KBookmarkGroup parent = KBookmarkGroup())'''
        return KBookmarkGroup()
    def newFolderButton(self):
        '''void KBookmarkDialog.newFolderButton()'''
    def initLayoutPrivate(self):
        '''void KBookmarkDialog.initLayoutPrivate()'''
    def fillGroup(self, parentItem, group):
        '''void KBookmarkDialog.fillGroup(QTreeWidgetItem parentItem, KBookmarkGroup group)'''
    def slotButtonClicked(self):
        '''int KBookmarkDialog.slotButtonClicked()'''
        return int()
    def parentBookmark(self):
        '''KBookmarkGroup KBookmarkDialog.parentBookmark()'''
        return KBookmarkGroup()
    def setParentBookmark(self, bm):
        '''void KBookmarkDialog.setParentBookmark(KBookmark bm)'''
    def save(self, mode):
        '''KBookmark KBookmarkDialog.save(KBookmarkDialog.BookmarkDialogMode mode)'''
        return KBookmark()
    def aboutToShow(self, mode):
        '''void KBookmarkDialog.aboutToShow(KBookmarkDialog.BookmarkDialogMode mode)'''
    def initLayout(self):
        '''void KBookmarkDialog.initLayout()'''
    def selectFolder(self, start = KBookmark()):
        '''KBookmarkGroup KBookmarkDialog.selectFolder(KBookmark start = KBookmark())'''
        return KBookmarkGroup()
    def createNewFolder(self, name, parent = KBookmark()):
        '''KBookmarkGroup KBookmarkDialog.createNewFolder(QString name, KBookmark parent = KBookmark())'''
        return KBookmarkGroup()
    def addBookmark(self, title, url, parent = KBookmark()):
        '''KBookmark KBookmarkDialog.addBookmark(QString title, KUrl url, KBookmark parent = KBookmark())'''
        return KBookmark()
    def editBookmark(self, bm):
        '''KBookmark KBookmarkDialog.editBookmark(KBookmark bm)'''
        return KBookmark()


class KBookmarkDomBuilder(QObject):
    """"""
    def __init__(self, group):
        '''KBookmarkManager KBookmarkDomBuilder.__init__(KBookmarkGroup group)'''
        return KBookmarkManager()
    def endFolder(self):
        '''void KBookmarkDomBuilder.endFolder()'''
    def newSeparator(self):
        '''void KBookmarkDomBuilder.newSeparator()'''
    def newFolder(self, text, open, additionalInfo):
        '''void KBookmarkDomBuilder.newFolder(QString text, bool open, QString additionalInfo)'''
    def newBookmark(self, text, url, additionalInfo):
        '''void KBookmarkDomBuilder.newBookmark(QString text, QString url, QString additionalInfo)'''
    def connectImporter(self):
        '''QObject KBookmarkDomBuilder.connectImporter()'''
        return QObject()


class KBookmarkExporterBase():
    """"""
    def __init__(self, mgr, fileName):
        '''void KBookmarkExporterBase.__init__(KBookmarkManager mgr, QString fileName)'''
    def __init__(self):
        '''KBookmarkExporterBase KBookmarkExporterBase.__init__()'''
        return KBookmarkExporterBase()
    def write(self):
        '''abstract KBookmarkGroup KBookmarkExporterBase.write()'''
        return KBookmarkGroup()


class KBookmarkImporterBase(QObject):
    """"""
    def __init__(self):
        '''void KBookmarkImporterBase.__init__()'''
    endFolder = pyqtSignal() # void endFolder() - signal
    newSeparator = pyqtSignal() # void newSeparator() - signal
    newFolder = pyqtSignal() # void newFolder(const QStringamp;,bool,const QStringamp;) - signal
    newBookmark = pyqtSignal() # void newBookmark(const QStringamp;,const QStringamp;,const QStringamp;) - signal
    def factory(self, type):
        '''static KBookmarkImporterBase KBookmarkImporterBase.factory(QString type)'''
        return KBookmarkImporterBase()
    def setupSignalForwards(self, src, dst):
        '''void KBookmarkImporterBase.setupSignalForwards(QObject src, QObject dst)'''
    def findDefaultLocation(self, forSaving = False):
        '''abstract QString KBookmarkImporterBase.findDefaultLocation(bool forSaving = False)'''
        return QString()
    def parse(self):
        '''abstract void KBookmarkImporterBase.parse()'''
    def setFilename(self, filename):
        '''void KBookmarkImporterBase.setFilename(QString filename)'''


class KXBELBookmarkImporterImpl(KBookmarkImporterBase, KBookmarkGroupTraverser):
    """"""
    def __init__(self):
        '''void KXBELBookmarkImporterImpl.__init__()'''
    def visitLeave(self):
        '''KBookmarkGroup KXBELBookmarkImporterImpl.visitLeave()'''
        return KBookmarkGroup()
    def visitEnter(self):
        '''KBookmarkGroup KXBELBookmarkImporterImpl.visitEnter()'''
        return KBookmarkGroup()
    def visit(self):
        '''KBookmark KXBELBookmarkImporterImpl.visit()'''
        return KBookmark()
    def findDefaultLocation(self):
        '''bool KXBELBookmarkImporterImpl.findDefaultLocation()'''
        return bool()
    def parse(self):
        '''void KXBELBookmarkImporterImpl.parse()'''


class KCrashBookmarkImporter(QObject):
    """"""
    def __init__(self, fileName):
        '''void KCrashBookmarkImporter.__init__(QString fileName)'''
    endFolder = pyqtSignal() # void endFolder() - signal
    newSeparator = pyqtSignal() # void newSeparator() - signal
    newFolder = pyqtSignal() # void newFolder(const QStringamp;,bool,const QStringamp;) - signal
    newBookmark = pyqtSignal() # void newBookmark(const QStringamp;,const QStringamp;,const QStringamp;) - signal
    def crashBookmarksDir(self):
        '''static QString KCrashBookmarkImporter.crashBookmarksDir()'''
        return QString()
    def parseCrashBookmarks(self, del_ = True):
        '''void KCrashBookmarkImporter.parseCrashBookmarks(bool del = True)'''


class KCrashBookmarkImporterImpl(KBookmarkImporterBase):
    """"""
    def __init__(self):
        '''void KCrashBookmarkImporterImpl.__init__()'''
    def getCrashLogs(self):
        '''static QStringList KCrashBookmarkImporterImpl.getCrashLogs()'''
        return QStringList()
    def findDefaultLocation(self, forSaving = False):
        '''QString KCrashBookmarkImporterImpl.findDefaultLocation(bool forSaving = False)'''
        return QString()
    def parse(self):
        '''void KCrashBookmarkImporterImpl.parse()'''
    def setShouldDelete(self):
        '''bool KCrashBookmarkImporterImpl.setShouldDelete()'''
        return bool()


class KIEBookmarkImporterImpl(KBookmarkImporterBase):
    """"""
    def __init__(self):
        '''void KIEBookmarkImporterImpl.__init__()'''
    def findDefaultLocation(self, forSaving = False):
        '''QString KIEBookmarkImporterImpl.findDefaultLocation(bool forSaving = False)'''
        return QString()
    def parse(self):
        '''void KIEBookmarkImporterImpl.parse()'''


class KIEBookmarkExporterImpl(KBookmarkExporterBase):
    """"""
    def __init__(self, mgr, path):
        '''void KIEBookmarkExporterImpl.__init__(KBookmarkManager mgr, QString path)'''
    def __init__(self):
        '''KIEBookmarkExporterImpl KIEBookmarkExporterImpl.__init__()'''
        return KIEBookmarkExporterImpl()
    def write(self):
        '''KBookmarkGroup KIEBookmarkExporterImpl.write()'''
        return KBookmarkGroup()


class KNSBookmarkImporterImpl(KBookmarkImporterBase):
    """"""
    def __init__(self):
        '''void KNSBookmarkImporterImpl.__init__()'''
    def findDefaultLocation(self, forSaving = False):
        '''QString KNSBookmarkImporterImpl.findDefaultLocation(bool forSaving = False)'''
        return QString()
    def parse(self):
        '''void KNSBookmarkImporterImpl.parse()'''
    def setUtf8(self, utf8):
        '''void KNSBookmarkImporterImpl.setUtf8(bool utf8)'''


class KMozillaBookmarkImporterImpl(KNSBookmarkImporterImpl):
    """"""
    def __init__(self):
        '''void KMozillaBookmarkImporterImpl.__init__()'''


class KNSBookmarkExporterImpl(KBookmarkExporterBase):
    """"""
    def __init__(self, mgr, fileName):
        '''void KNSBookmarkExporterImpl.__init__(KBookmarkManager mgr, QString fileName)'''
    def __init__(self):
        '''KNSBookmarkExporterImpl KNSBookmarkExporterImpl.__init__()'''
        return KNSBookmarkExporterImpl()
    def folderAsString(self, parent):
        '''QString KNSBookmarkExporterImpl.folderAsString(KBookmarkGroup parent)'''
        return QString()
    def setUtf8(self):
        '''bool KNSBookmarkExporterImpl.setUtf8()'''
        return bool()
    def write(self, parent):
        '''void KNSBookmarkExporterImpl.write(KBookmarkGroup parent)'''


class KOperaBookmarkImporterImpl(KBookmarkImporterBase):
    """"""
    def __init__(self):
        '''void KOperaBookmarkImporterImpl.__init__()'''
    def findDefaultLocation(self, forSaving = False):
        '''QString KOperaBookmarkImporterImpl.findDefaultLocation(bool forSaving = False)'''
        return QString()
    def parse(self):
        '''void KOperaBookmarkImporterImpl.parse()'''


class KOperaBookmarkExporterImpl(KBookmarkExporterBase):
    """"""
    def __init__(self, mgr, filename):
        '''void KOperaBookmarkExporterImpl.__init__(KBookmarkManager mgr, QString filename)'''
    def __init__(self):
        '''KOperaBookmarkExporterImpl KOperaBookmarkExporterImpl.__init__()'''
        return KOperaBookmarkExporterImpl()
    def write(self, parent):
        '''void KOperaBookmarkExporterImpl.write(KBookmarkGroup parent)'''


class KBookmarkManager(QObject):
    """"""
    error = pyqtSignal() # void error(const QStringamp;) - signal
    def setAutoErrorHandlingEnabled(self, enable, parent):
        '''void KBookmarkManager.setAutoErrorHandlingEnabled(bool enable, QWidget parent)'''
    def autoErrorHandlingEnabled(self):
        '''bool KBookmarkManager.autoErrorHandlingEnabled()'''
        return bool()
    configChanged = pyqtSignal() # void configChanged() - signal
    changed = pyqtSignal() # void changed(const QStringamp;,const QStringamp;) - signal
    bookmarkConfigChanged = pyqtSignal() # void bookmarkConfigChanged() - signal
    bookmarksChanged = pyqtSignal() # void bookmarksChanged(QString) - signal
    bookmarkCompleteChange = pyqtSignal() # void bookmarkCompleteChange(QString) - signal
    def notifyConfigChanged(self):
        '''void KBookmarkManager.notifyConfigChanged()'''
    def notifyCompleteChange(self, caller):
        '''void KBookmarkManager.notifyCompleteChange(QString caller)'''
    def slotEditBookmarksAtAddress(self, address):
        '''void KBookmarkManager.slotEditBookmarksAtAddress(QString address)'''
    def slotEditBookmarks(self):
        '''void KBookmarkManager.slotEditBookmarks()'''
    def internalDocument(self):
        '''QDomDocument KBookmarkManager.internalDocument()'''
        return QDomDocument()
    def userBookmarksManager(self):
        '''static KBookmarkManager KBookmarkManager.userBookmarksManager()'''
        return KBookmarkManager()
    def createTempManager(self):
        '''static KBookmarkManager KBookmarkManager.createTempManager()'''
        return KBookmarkManager()
    def managerForExternalFile(self, bookmarksFile):
        '''static KBookmarkManager KBookmarkManager.managerForExternalFile(QString bookmarksFile)'''
        return KBookmarkManager()
    def managerForFile(self, bookmarksFile, dbusObjectName):
        '''static KBookmarkManager KBookmarkManager.managerForFile(QString bookmarksFile, QString dbusObjectName)'''
        return KBookmarkManager()
    def setEditorOptions(self, caption, browser):
        '''void KBookmarkManager.setEditorOptions(QString caption, bool browser)'''
    def emitConfigChanged(self):
        '''void KBookmarkManager.emitConfigChanged()'''
    def save(self, toolbarCache = True):
        '''bool KBookmarkManager.save(bool toolbarCache = True)'''
        return bool()
    def emitChanged(self):
        '''void KBookmarkManager.emitChanged()'''
    def emitChanged(self, group):
        '''void KBookmarkManager.emitChanged(KBookmarkGroup group)'''
    def findByAddress(self, address):
        '''KBookmark KBookmarkManager.findByAddress(QString address)'''
        return KBookmark()
    def toolbar(self):
        '''KBookmarkGroup KBookmarkManager.toolbar()'''
        return KBookmarkGroup()
    def root(self):
        '''KBookmarkGroup KBookmarkManager.root()'''
        return KBookmarkGroup()
    def path(self):
        '''QString KBookmarkManager.path()'''
        return QString()
    def updateFavicon(self, url, faviconurl):
        '''void KBookmarkManager.updateFavicon(QString url, QString faviconurl)'''
    def updateAccessMetadata(self, url):
        '''bool KBookmarkManager.updateAccessMetadata(QString url)'''
        return bool()
    def saveAs(self, filename, toolbarCache = True):
        '''bool KBookmarkManager.saveAs(QString filename, bool toolbarCache = True)'''
        return bool()
    def setUpdate(self, update):
        '''void KBookmarkManager.setUpdate(bool update)'''


class KBookmarkOwner():
    """"""
    # Enum KBookmarkOwner.BookmarkOption
    ShowAddBookmark = 0
    ShowEditBookmark = 0

    def __init__(self):
        '''void KBookmarkOwner.__init__()'''
    def __init__(self):
        '''KBookmarkOwner KBookmarkOwner.__init__()'''
        return KBookmarkOwner()
    def bookmarkDialog(self, mgr, parent):
        '''KBookmarkDialog KBookmarkOwner.bookmarkDialog(KBookmarkManager mgr, QWidget parent)'''
        return KBookmarkDialog()
    def openFolderinTabs(self, bm):
        '''void KBookmarkOwner.openFolderinTabs(KBookmarkGroup bm)'''
    def openBookmark(self, bm, mb, km):
        '''abstract void KBookmarkOwner.openBookmark(KBookmark bm, Qt.MouseButtons mb, Qt.KeyboardModifiers km)'''
    def enableOption(self, option):
        '''bool KBookmarkOwner.enableOption(KBookmarkOwner.BookmarkOption option)'''
        return bool()
    def currentBookmarkList(self):
        '''list-of-tuple-of-QString-QString KBookmarkOwner.currentBookmarkList()'''
        return [tuple-of-QString-QString()]
    def supportsTabs(self):
        '''bool KBookmarkOwner.supportsTabs()'''
        return bool()
    def currentUrl(self):
        '''QString KBookmarkOwner.currentUrl()'''
        return QString()
    def currentTitle(self):
        '''QString KBookmarkOwner.currentTitle()'''
        return QString()


class KBookmarkMenu(QObject):
    """"""
    def __init__(self, mgr, owner, parentMenu, collec):
        '''void KBookmarkMenu.__init__(KBookmarkManager mgr, KBookmarkOwner owner, KMenu parentMenu, KActionCollection collec)'''
    def __init__(self, mgr, owner, parentMenu, parentAddress):
        '''void KBookmarkMenu.__init__(KBookmarkManager mgr, KBookmarkOwner owner, KMenu parentMenu, QString parentAddress)'''
    def parentMenu(self):
        '''KMenu KBookmarkMenu.parentMenu()'''
        return KMenu()
    def owner(self):
        '''KBookmarkOwner KBookmarkMenu.owner()'''
        return KBookmarkOwner()
    def manager(self):
        '''KBookmarkManager KBookmarkMenu.manager()'''
        return KBookmarkManager()
    def parentAddress(self):
        '''QString KBookmarkMenu.parentAddress()'''
        return QString()
    def isDirty(self):
        '''bool KBookmarkMenu.isDirty()'''
        return bool()
    def isRoot(self):
        '''bool KBookmarkMenu.isRoot()'''
        return bool()
    def addOpenInTabs(self):
        '''void KBookmarkMenu.addOpenInTabs()'''
    def addNewFolder(self):
        '''void KBookmarkMenu.addNewFolder()'''
    def addEditBookmarks(self):
        '''void KBookmarkMenu.addEditBookmarks()'''
    def addAddBookmarksList(self):
        '''void KBookmarkMenu.addAddBookmarksList()'''
    def addAddBookmark(self):
        '''void KBookmarkMenu.addAddBookmark()'''
    def fillBookmarks(self):
        '''void KBookmarkMenu.fillBookmarks()'''
    def addActions(self):
        '''void KBookmarkMenu.addActions()'''
    def contextMenu(self, action):
        '''KMenu KBookmarkMenu.contextMenu(QAction action)'''
        return KMenu()
    def actionForBookmark(self, bm):
        '''QAction KBookmarkMenu.actionForBookmark(KBookmark bm)'''
        return QAction()
    def refill(self):
        '''void KBookmarkMenu.refill()'''
    def clear(self):
        '''void KBookmarkMenu.clear()'''
    def slotOpenFolderInTabs(self):
        '''void KBookmarkMenu.slotOpenFolderInTabs()'''
    def slotNewFolder(self):
        '''void KBookmarkMenu.slotNewFolder()'''
    def slotAddBookmark(self):
        '''void KBookmarkMenu.slotAddBookmark()'''
    def slotAddBookmarksList(self):
        '''void KBookmarkMenu.slotAddBookmarksList()'''
    def slotAboutToShow(self):
        '''void KBookmarkMenu.slotAboutToShow()'''
    def slotBookmarksChanged(self):
        '''QString KBookmarkMenu.slotBookmarksChanged()'''
        return QString()
    def ensureUpToDate(self):
        '''void KBookmarkMenu.ensureUpToDate()'''


class KBookmarkContextMenu(KMenu):
    """"""
    def __init__(self, bm, manager, owner, parent = None):
        '''void KBookmarkContextMenu.__init__(KBookmark bm, KBookmarkManager manager, KBookmarkOwner owner, QWidget parent = None)'''
    def bookmark(self):
        '''KBookmark KBookmarkContextMenu.bookmark()'''
        return KBookmark()
    def owner(self):
        '''KBookmarkOwner KBookmarkContextMenu.owner()'''
        return KBookmarkOwner()
    def manager(self):
        '''KBookmarkManager KBookmarkContextMenu.manager()'''
        return KBookmarkManager()
    def addOpenFolderInTabs(self):
        '''void KBookmarkContextMenu.addOpenFolderInTabs()'''
    def addBookmarkActions(self):
        '''void KBookmarkContextMenu.addBookmarkActions()'''
    def addProperties(self):
        '''void KBookmarkContextMenu.addProperties()'''
    def addFolderActions(self):
        '''void KBookmarkContextMenu.addFolderActions()'''
    def addBookmark(self):
        '''void KBookmarkContextMenu.addBookmark()'''
    def slotOpenFolderInTabs(self):
        '''void KBookmarkContextMenu.slotOpenFolderInTabs()'''
    def slotCopyLocation(self):
        '''void KBookmarkContextMenu.slotCopyLocation()'''
    def slotRemove(self):
        '''void KBookmarkContextMenu.slotRemove()'''
    def slotInsert(self):
        '''void KBookmarkContextMenu.slotInsert()'''
    def slotProperties(self):
        '''void KBookmarkContextMenu.slotProperties()'''
    def slotEditAt(self):
        '''void KBookmarkContextMenu.slotEditAt()'''
    def addActions(self):
        '''void KBookmarkContextMenu.addActions()'''


class KBookmarkActionInterface():
    """"""
    def __init__(self, bk):
        '''void KBookmarkActionInterface.__init__(KBookmark bk)'''
    def __init__(self):
        '''KBookmarkActionInterface KBookmarkActionInterface.__init__()'''
        return KBookmarkActionInterface()
    def bookmark(self):
        '''KBookmark KBookmarkActionInterface.bookmark()'''
        return KBookmark()


class KBookmarkActionMenu(KActionMenu, KBookmarkActionInterface):
    """"""
    def __init__(self, bm, parent):
        '''void KBookmarkActionMenu.__init__(KBookmark bm, QObject parent)'''
    def __init__(self, bm, text, parent):
        '''void KBookmarkActionMenu.__init__(KBookmark bm, QString text, QObject parent)'''


class KBookmarkAction(KAction, KBookmarkActionInterface):
    """"""
    def __init__(self, bk, owner, parent):
        '''void KBookmarkAction.__init__(KBookmark bk, KBookmarkOwner owner, QObject parent)'''
    def slotSelected(self, mb, km):
        '''void KBookmarkAction.slotSelected(Qt.MouseButtons mb, Qt.KeyboardModifiers km)'''


class KBuildSycocaProgressDialog(QProgressDialog):
    """"""
    def rebuildKSycoca(self, parent):
        '''static void KBuildSycocaProgressDialog.rebuildKSycoca(QWidget parent)'''


class KDataToolInfo():
    """"""
    def __init__(self):
        '''void KDataToolInfo.__init__()'''
    def __init__(self, service, instance):
        '''void KDataToolInfo.__init__(unknown-type service, KComponentData instance)'''
    def __init__(self, info):
        '''void KDataToolInfo.__init__(KDataToolInfo info)'''
    def query(self, datatype, mimetype, instance):
        '''static list-of-KDataToolInfo KDataToolInfo.query(QString datatype, QString mimetype, KComponentData instance)'''
        return [KDataToolInfo()]
    def isValid(self):
        '''bool KDataToolInfo.isValid()'''
        return bool()
    def componentData(self):
        '''KComponentData KDataToolInfo.componentData()'''
        return KComponentData()
    def service(self):
        '''unknown-type KDataToolInfo.service()'''
        return unknown-type()
    def createTool(self, parent = None):
        '''KDataTool KDataToolInfo.createTool(QObject parent = None)'''
        return KDataTool()
    def commands(self):
        '''QStringList KDataToolInfo.commands()'''
        return QStringList()
    def userCommands(self):
        '''QStringList KDataToolInfo.userCommands()'''
        return QStringList()
    def iconName(self):
        '''QString KDataToolInfo.iconName()'''
        return QString()
    def miniIcon(self):
        '''QPixmap KDataToolInfo.miniIcon()'''
        return QPixmap()
    def icon(self):
        '''QPixmap KDataToolInfo.icon()'''
        return QPixmap()
    def isReadOnly(self):
        '''bool KDataToolInfo.isReadOnly()'''
        return bool()
    def mimeTypes(self):
        '''QStringList KDataToolInfo.mimeTypes()'''
        return QStringList()
    def dataType(self):
        '''QString KDataToolInfo.dataType()'''
        return QString()


class KDataToolAction(KAction):
    """"""
    def __init__(self, text, info, command, parent):
        '''void KDataToolAction.__init__(QString text, KDataToolInfo info, QString command, QObject parent)'''
    def slotActivated(self):
        '''void KDataToolAction.slotActivated()'''
    toolActivated = pyqtSignal() # void toolActivated(const KDataToolInfoamp;,const QStringamp;) - signal
    def dataToolActionList(self, tools, receiver, slot, parent):
        '''static list-of-QAction KDataToolAction.dataToolActionList(list-of-KDataToolInfo tools, QObject receiver, str slot, KActionCollection parent)'''
        return [QAction()]


class KDataTool(QObject):
    """"""
    def __init__(self, parent = None):
        '''void KDataTool.__init__(QObject parent = None)'''
    def run(self, command, data, datatype, mimetype):
        '''abstract bool KDataTool.run(QString command, sip.voidptr data, QString datatype, QString mimetype)'''
        return bool()
    def componentData(self):
        '''KComponentData KDataTool.componentData()'''
        return KComponentData()
    def setComponentData(self, componentData):
        '''void KDataTool.setComponentData(KComponentData componentData)'''


class KDBusServiceStarter():
    """"""
    def __init__(self):
        '''void KDBusServiceStarter.__init__()'''
    def __init__(self):
        '''KDBusServiceStarter KDBusServiceStarter.__init__()'''
        return KDBusServiceStarter()
    def startServiceFor(self, serviceType, constraint = QString(), error = None, dbusService = None, flags = 0):
        '''int KDBusServiceStarter.startServiceFor(QString serviceType, QString constraint = QString(), QString error = None, QString dbusService = None, int flags = 0)'''
        return int()
    def findServiceFor(self, serviceType, constraint = QString(), error = None, dbusService = None, flags = 0):
        '''int KDBusServiceStarter.findServiceFor(QString serviceType, QString constraint = QString(), QString error = None, QString dbusService = None, int flags = 0)'''
        return int()
    def self(self):
        '''static KDBusServiceStarter KDBusServiceStarter.self()'''
        return KDBusServiceStarter()


class KDesktopFileActions():
    """"""
    def run(self, _url, _is_local):
        '''static bool KDesktopFileActions.run(KUrl _url, bool _is_local)'''
        return bool()
    def executeService(self, urls, service):
        '''static void KDesktopFileActions.executeService(KUrl.List urls, KServiceAction service)'''
    def userDefinedServices(self, path, bLocalFiles):
        '''static list-of-KServiceAction KDesktopFileActions.userDefinedServices(QString path, bool bLocalFiles)'''
        return [KServiceAction()]
    def userDefinedServices(self, path, desktopFile, bLocalFiles, file_list = None):
        '''static list-of-KServiceAction KDesktopFileActions.userDefinedServices(QString path, KDesktopFile desktopFile, bool bLocalFiles, KUrl.List file_list = KUrl.List())'''
        return [KServiceAction()]
    def userDefinedServices(self, service, bLocalFiles, file_list = None):
        '''static list-of-KServiceAction KDesktopFileActions.userDefinedServices(KService service, bool bLocalFiles, KUrl.List file_list = KUrl.List())'''
        return [KServiceAction()]
    def builtinServices(self, url):
        '''static list-of-KServiceAction KDesktopFileActions.builtinServices(KUrl url)'''
        return [KServiceAction()]


class KDeviceListModel(QAbstractItemModel):
    """"""
    def __init__(self, parent = None):
        '''void KDeviceListModel.__init__(QObject parent = None)'''
    def __init__(self, predicate, parent = None):
        '''void KDeviceListModel.__init__(QString predicate, QObject parent = None)'''
    def __init__(self, predicate, parent = None):
        '''void KDeviceListModel.__init__(Solid.Predicate predicate, QObject parent = None)'''
    modelInitialized = pyqtSignal() # void modelInitialized() - signal
    def deviceForIndex(self, index):
        '''Solid.Device KDeviceListModel.deviceForIndex(QModelIndex index)'''
        return Solid.Device()
    def columnCount(self, parent = QModelIndex()):
        '''int KDeviceListModel.columnCount(QModelIndex parent = QModelIndex())'''
        return int()
    def rowCount(self, parent = QModelIndex()):
        '''int KDeviceListModel.rowCount(QModelIndex parent = QModelIndex())'''
        return int()
    def parent(self, child):
        '''QModelIndex KDeviceListModel.parent(QModelIndex child)'''
        return QModelIndex()
    def rootIndex(self):
        '''QModelIndex KDeviceListModel.rootIndex()'''
        return QModelIndex()
    def index(self, row, column, parent = QModelIndex()):
        '''QModelIndex KDeviceListModel.index(int row, int column, QModelIndex parent = QModelIndex())'''
        return QModelIndex()
    def headerData(self, section, orientation, role = None):
        '''QVariant KDeviceListModel.headerData(int section, Qt.Orientation orientation, int role = Qt.DisplayRole)'''
        return QVariant()
    def data(self, index, role):
        '''QVariant KDeviceListModel.data(QModelIndex index, int role)'''
        return QVariant()


class KDirLister(QObject):
    """"""
    # Enum KDirLister.Changes
    NONE = 0
    NAME_FILTER = 0
    MIME_FILTER = 0
    DOT_FILES = 0
    DIR_ONLY_MODE = 0

    # Enum KDirLister.WhichItems
    AllItems = 0
    FilteredItems = 0

    # Enum KDirLister.OpenUrlFlag
    NoFlags = 0
    Keep = 0
    Reload = 0

    def __init__(self, parent = None):
        '''void KDirLister.__init__(QObject parent = None)'''
    refreshItems = pyqtSignal() # void refreshItems(const QListlt;QPairlt;KFileItem,KFileItemgt;gt;amp;) - signal
    def handleError(self):
        '''KIO.Job KDirLister.handleError()'''
        return KIO.Job()
    def doMimeFilter(self, mime, filters):
        '''bool KDirLister.doMimeFilter(QString mime, QStringList filters)'''
        return bool()
    def doNameFilter(self, name, filters):
        '''bool KDirLister.doNameFilter(QString name, list-of-QRegExp filters)'''
        return bool()
    speed = pyqtSignal() # void speed(int) - signal
    processedSize = pyqtSignal() # void processedSize(KIO::filesize_t) - signal
    totalSize = pyqtSignal() # void totalSize(KIO::filesize_t) - signal
    percent = pyqtSignal() # void percent(int) - signal
    infoMessage = pyqtSignal() # void infoMessage(const QStringamp;) - signal
    itemsDeleted = pyqtSignal() # void itemsDeleted(const KFileItemListamp;) - signal
    deleteItem = pyqtSignal() # void deleteItem(const KFileItemamp;) - signal
    itemsFilteredByMime = pyqtSignal() # void itemsFilteredByMime(const KFileItemListamp;) - signal
    itemsAdded = pyqtSignal() # void itemsAdded(const KUrlamp;,const KFileItemListamp;) - signal
    newItems = pyqtSignal() # void newItems(const KFileItemListamp;) - signal
    clear = pyqtSignal() # void clear() - signal
    clear = pyqtSignal() # void clear(const KUrlamp;) - signal
    redirection = pyqtSignal() # void redirection(const KUrlamp;) - signal
    redirection = pyqtSignal() # void redirection(const KUrlamp;,const KUrlamp;) - signal
    canceled = pyqtSignal() # void canceled() - signal
    canceled = pyqtSignal() # void canceled(const KUrlamp;) - signal
    completed = pyqtSignal() # void completed() - signal
    completed = pyqtSignal() # void completed(const KUrlamp;) - signal
    started = pyqtSignal() # void started(const KUrlamp;) - signal
    def cachedItemForUrl(self, url):
        '''static KFileItem KDirLister.cachedItemForUrl(KUrl url)'''
        return KFileItem()
    def itemsForDir(self, dir, which = None):
        '''KFileItemList KDirLister.itemsForDir(KUrl dir, KDirLister.WhichItems which = KDirLister.FilteredItems)'''
        return KFileItemList()
    def items(self, which = None):
        '''KFileItemList KDirLister.items(KDirLister.WhichItems which = KDirLister.FilteredItems)'''
        return KFileItemList()
    def mainWindow(self):
        '''QWidget KDirLister.mainWindow()'''
        return QWidget()
    def setMainWindow(self, window):
        '''void KDirLister.setMainWindow(QWidget window)'''
    def matchesMimeFilter(self, mime):
        '''bool KDirLister.matchesMimeFilter(QString mime)'''
        return bool()
    def matchesMimeFilter(self):
        '''KFileItem KDirLister.matchesMimeFilter()'''
        return KFileItem()
    def matchesFilter(self, name):
        '''bool KDirLister.matchesFilter(QString name)'''
        return bool()
    def matchesFilter(self):
        '''KFileItem KDirLister.matchesFilter()'''
        return KFileItem()
    def mimeFilters(self):
        '''QStringList KDirLister.mimeFilters()'''
        return QStringList()
    def clearMimeFilter(self):
        '''void KDirLister.clearMimeFilter()'''
    def setMimeExcludeFilter(self, mimeList):
        '''void KDirLister.setMimeExcludeFilter(QStringList mimeList)'''
    def setMimeFilter(self, mimeList):
        '''void KDirLister.setMimeFilter(QStringList mimeList)'''
    def nameFilter(self):
        '''QString KDirLister.nameFilter()'''
        return QString()
    def setNameFilter(self, filter):
        '''void KDirLister.setNameFilter(QString filter)'''
    def findByName(self, name):
        '''KFileItem KDirLister.findByName(QString name)'''
        return KFileItem()
    def findByUrl(self, _url):
        '''KFileItem KDirLister.findByUrl(KUrl _url)'''
        return KFileItem()
    def rootItem(self):
        '''KFileItem KDirLister.rootItem()'''
        return KFileItem()
    def isFinished(self):
        '''bool KDirLister.isFinished()'''
        return bool()
    def updateDirectory(self, _dir):
        '''void KDirLister.updateDirectory(KUrl _dir)'''
    def emitChanges(self):
        '''void KDirLister.emitChanges()'''
    def directories(self):
        '''KUrl.List KDirLister.directories()'''
        return KUrl.List()
    def url(self):
        '''KUrl KDirLister.url()'''
        return KUrl()
    def setDirOnlyMode(self, dirsOnly):
        '''void KDirLister.setDirOnlyMode(bool dirsOnly)'''
    def dirOnlyMode(self):
        '''bool KDirLister.dirOnlyMode()'''
        return bool()
    def setShowingDotFiles(self, _showDotFiles):
        '''void KDirLister.setShowingDotFiles(bool _showDotFiles)'''
    def showingDotFiles(self):
        '''bool KDirLister.showingDotFiles()'''
        return bool()
    def setAutoErrorHandlingEnabled(self, enable, parent):
        '''void KDirLister.setAutoErrorHandlingEnabled(bool enable, QWidget parent)'''
    def autoErrorHandlingEnabled(self):
        '''bool KDirLister.autoErrorHandlingEnabled()'''
        return bool()
    def setAutoUpdate(self, enable):
        '''void KDirLister.setAutoUpdate(bool enable)'''
    def autoUpdate(self):
        '''bool KDirLister.autoUpdate()'''
        return bool()
    def setDelayedMimeTypes(self, delayedMimeTypes):
        '''void KDirLister.setDelayedMimeTypes(bool delayedMimeTypes)'''
    def delayedMimeTypes(self):
        '''bool KDirLister.delayedMimeTypes()'''
        return bool()
    def stop(self):
        '''void KDirLister.stop()'''
    def stop(self, _url):
        '''void KDirLister.stop(KUrl _url)'''
    def openUrl(self, _url, _flags = None):
        '''bool KDirLister.openUrl(KUrl _url, KDirLister.OpenUrlFlags _flags = KDirLister.NoFlags)'''
        return bool()
    class OpenUrlFlags():
        """"""
        def __init__(self):
            '''KDirLister.OpenUrlFlags KDirLister.OpenUrlFlags.__init__()'''
            return KDirLister.OpenUrlFlags()
        def __init__(self):
            '''int KDirLister.OpenUrlFlags.__init__()'''
            return int()
        def __init__(self):
            '''void KDirLister.OpenUrlFlags.__init__()'''
        def __bool__(self):
            '''int KDirLister.OpenUrlFlags.__bool__()'''
            return int()
        def __ne__(self, f):
            '''bool KDirLister.OpenUrlFlags.__ne__(KDirLister.OpenUrlFlags f)'''
            return bool()
        def __eq__(self, f):
            '''bool KDirLister.OpenUrlFlags.__eq__(KDirLister.OpenUrlFlags f)'''
            return bool()
        def __invert__(self):
            '''KDirLister.OpenUrlFlags KDirLister.OpenUrlFlags.__invert__()'''
            return KDirLister.OpenUrlFlags()
        def __and__(self, mask):
            '''KDirLister.OpenUrlFlags KDirLister.OpenUrlFlags.__and__(int mask)'''
            return KDirLister.OpenUrlFlags()
        def __xor__(self, f):
            '''KDirLister.OpenUrlFlags KDirLister.OpenUrlFlags.__xor__(KDirLister.OpenUrlFlags f)'''
            return KDirLister.OpenUrlFlags()
        def __xor__(self, f):
            '''KDirLister.OpenUrlFlags KDirLister.OpenUrlFlags.__xor__(int f)'''
            return KDirLister.OpenUrlFlags()
        def __or__(self, f):
            '''KDirLister.OpenUrlFlags KDirLister.OpenUrlFlags.__or__(KDirLister.OpenUrlFlags f)'''
            return KDirLister.OpenUrlFlags()
        def __or__(self, f):
            '''KDirLister.OpenUrlFlags KDirLister.OpenUrlFlags.__or__(int f)'''
            return KDirLister.OpenUrlFlags()
        def __int__(self):
            '''int KDirLister.OpenUrlFlags.__int__()'''
            return int()
        def __ixor__(self, f):
            '''KDirLister.OpenUrlFlags KDirLister.OpenUrlFlags.__ixor__(KDirLister.OpenUrlFlags f)'''
            return KDirLister.OpenUrlFlags()
        def __ior__(self, f):
            '''KDirLister.OpenUrlFlags KDirLister.OpenUrlFlags.__ior__(KDirLister.OpenUrlFlags f)'''
            return KDirLister.OpenUrlFlags()
        def __iand__(self, mask):
            '''KDirLister.OpenUrlFlags KDirLister.OpenUrlFlags.__iand__(int mask)'''
            return KDirLister.OpenUrlFlags()


class KDirModel(QAbstractItemModel):
    """"""
    # Enum KDirModel.DropsAllowedFlag
    NoDrops = 0
    DropOnDirectory = 0
    DropOnAnyFile = 0
    DropOnLocalExecutable = 0

    # Enum KDirModel.AdditionalRoles
    FileItemRole = 0
    ChildCountRole = 0
    HasJobRole = 0

    ChildCountUnknown = None # int - member
    # Enum KDirModel.ModelColumns
    Name = 0
    Size = 0
    ModifiedTime = 0
    Permissions = 0
    Owner = 0
    Group = 0
    Type = 0
    ColumnCount = 0

    def __init__(self, parent = None):
        '''void KDirModel.__init__(QObject parent = None)'''
    def jobTransfersVisible(self):
        '''bool KDirModel.jobTransfersVisible()'''
        return bool()
    def setJobTransfersVisible(self, value):
        '''void KDirModel.setJobTransfersVisible(bool value)'''
    needSequenceIcon = pyqtSignal() # void needSequenceIcon(const QModelIndexamp;,int) - signal
    expand = pyqtSignal() # void expand(const QModelIndexamp;) - signal
    def requestSequenceIcon(self, index, sequenceIndex):
        '''void KDirModel.requestSequenceIcon(QModelIndex index, int sequenceIndex)'''
    def simplifiedUrlList(self, urls):
        '''static KUrl.List KDirModel.simplifiedUrlList(KUrl.List urls)'''
        return KUrl.List()
    def sort(self, column, order = None):
        '''void KDirModel.sort(int column, Qt.SortOrder order = Qt.AscendingOrder)'''
    def setData(self, index, value, role = None):
        '''bool KDirModel.setData(QModelIndex index, QVariant value, int role = Qt.EditRole)'''
        return bool()
    def rowCount(self, parent = QModelIndex()):
        '''int KDirModel.rowCount(QModelIndex parent = QModelIndex())'''
        return int()
    def parent(self, index):
        '''QModelIndex KDirModel.parent(QModelIndex index)'''
        return QModelIndex()
    def mimeTypes(self):
        '''QStringList KDirModel.mimeTypes()'''
        return QStringList()
    def mimeData(self, indexes):
        '''QMimeData KDirModel.mimeData(list-of-QModelIndex indexes)'''
        return QMimeData()
    def index(self, row, column, parent = QModelIndex()):
        '''QModelIndex KDirModel.index(int row, int column, QModelIndex parent = QModelIndex())'''
        return QModelIndex()
    def headerData(self, section, orientation, role = None):
        '''QVariant KDirModel.headerData(int section, Qt.Orientation orientation, int role = Qt.DisplayRole)'''
        return QVariant()
    def hasChildren(self, parent = QModelIndex()):
        '''bool KDirModel.hasChildren(QModelIndex parent = QModelIndex())'''
        return bool()
    def flags(self, index):
        '''Qt.ItemFlags KDirModel.flags(QModelIndex index)'''
        return Qt.ItemFlags()
    def fetchMore(self, parent):
        '''void KDirModel.fetchMore(QModelIndex parent)'''
    def dropMimeData(self, data, action, row, column, parent):
        '''bool KDirModel.dropMimeData(QMimeData data, Qt.DropAction action, int row, int column, QModelIndex parent)'''
        return bool()
    def data(self, index, role = None):
        '''QVariant KDirModel.data(QModelIndex index, int role = Qt.DisplayRole)'''
        return QVariant()
    def columnCount(self, parent = QModelIndex()):
        '''int KDirModel.columnCount(QModelIndex parent = QModelIndex())'''
        return int()
    def canFetchMore(self, parent):
        '''bool KDirModel.canFetchMore(QModelIndex parent)'''
        return bool()
    def setDropsAllowed(self, dropsAllowed):
        '''void KDirModel.setDropsAllowed(KDirModel.DropsAllowed dropsAllowed)'''
    def itemChanged(self, index):
        '''void KDirModel.itemChanged(QModelIndex index)'''
    def expandToUrl(self, url):
        '''void KDirModel.expandToUrl(KUrl url)'''
    def indexForUrl(self, url):
        '''QModelIndex KDirModel.indexForUrl(KUrl url)'''
        return QModelIndex()
    def indexForItem(self):
        '''KFileItem KDirModel.indexForItem()'''
        return KFileItem()
    def indexForItem(self):
        '''KFileItem KDirModel.indexForItem()'''
        return KFileItem()
    def itemForIndex(self, index):
        '''KFileItem KDirModel.itemForIndex(QModelIndex index)'''
        return KFileItem()
    def dirLister(self):
        '''KDirLister KDirModel.dirLister()'''
        return KDirLister()
    def setDirLister(self, dirLister):
        '''void KDirModel.setDirLister(KDirLister dirLister)'''
    class DropsAllowed():
        """"""
        def __init__(self):
            '''KDirModel.DropsAllowed KDirModel.DropsAllowed.__init__()'''
            return KDirModel.DropsAllowed()
        def __init__(self):
            '''int KDirModel.DropsAllowed.__init__()'''
            return int()
        def __init__(self):
            '''void KDirModel.DropsAllowed.__init__()'''
        def __bool__(self):
            '''int KDirModel.DropsAllowed.__bool__()'''
            return int()
        def __ne__(self, f):
            '''bool KDirModel.DropsAllowed.__ne__(KDirModel.DropsAllowed f)'''
            return bool()
        def __eq__(self, f):
            '''bool KDirModel.DropsAllowed.__eq__(KDirModel.DropsAllowed f)'''
            return bool()
        def __invert__(self):
            '''KDirModel.DropsAllowed KDirModel.DropsAllowed.__invert__()'''
            return KDirModel.DropsAllowed()
        def __and__(self, mask):
            '''KDirModel.DropsAllowed KDirModel.DropsAllowed.__and__(int mask)'''
            return KDirModel.DropsAllowed()
        def __xor__(self, f):
            '''KDirModel.DropsAllowed KDirModel.DropsAllowed.__xor__(KDirModel.DropsAllowed f)'''
            return KDirModel.DropsAllowed()
        def __xor__(self, f):
            '''KDirModel.DropsAllowed KDirModel.DropsAllowed.__xor__(int f)'''
            return KDirModel.DropsAllowed()
        def __or__(self, f):
            '''KDirModel.DropsAllowed KDirModel.DropsAllowed.__or__(KDirModel.DropsAllowed f)'''
            return KDirModel.DropsAllowed()
        def __or__(self, f):
            '''KDirModel.DropsAllowed KDirModel.DropsAllowed.__or__(int f)'''
            return KDirModel.DropsAllowed()
        def __int__(self):
            '''int KDirModel.DropsAllowed.__int__()'''
            return int()
        def __ixor__(self, f):
            '''KDirModel.DropsAllowed KDirModel.DropsAllowed.__ixor__(KDirModel.DropsAllowed f)'''
            return KDirModel.DropsAllowed()
        def __ior__(self, f):
            '''KDirModel.DropsAllowed KDirModel.DropsAllowed.__ior__(KDirModel.DropsAllowed f)'''
            return KDirModel.DropsAllowed()
        def __iand__(self, mask):
            '''KDirModel.DropsAllowed KDirModel.DropsAllowed.__iand__(int mask)'''
            return KDirModel.DropsAllowed()


class KDirOperator(QWidget):
    """"""
    # Enum KDirOperator.ActionType
    SortActions = 0
    ViewActions = 0
    NavActions = 0
    FileActions = 0
    AllActions = 0

    def __init__(self, urlName = KUrl(), parent = None):
        '''void KDirOperator.__init__(KUrl urlName = KUrl(), QWidget parent = None)'''
    def keyPressEvent(self, event):
        '''void KDirOperator.keyPressEvent(QKeyEvent event)'''
    def newFileMenuSupportedMimeTypes(self):
        '''QStringList KDirOperator.newFileMenuSupportedMimeTypes()'''
        return QStringList()
    def setNewFileMenuSupportedMimeTypes(self, mime):
        '''void KDirOperator.setNewFileMenuSupportedMimeTypes(QStringList mime)'''
    currentIconSizeChanged = pyqtSignal() # void currentIconSizeChanged(int) - signal
    contextMenuAboutToShow = pyqtSignal() # void contextMenuAboutToShow(const KFileItemamp;,QMenu *) - signal
    dropped = pyqtSignal() # void dropped(const KFileItemamp;,QDropEvent *,const KUrl::Listamp;) - signal
    fileSelected = pyqtSignal() # void fileSelected(const KFileItemamp;) - signal
    dirActivated = pyqtSignal() # void dirActivated(const KFileItemamp;) - signal
    fileHighlighted = pyqtSignal() # void fileHighlighted(const KFileItemamp;) - signal
    viewChanged = pyqtSignal() # void viewChanged(QAbstractItemView *) - signal
    finishedLoading = pyqtSignal() # void finishedLoading() - signal
    completion = pyqtSignal() # void completion(const QStringamp;) - signal
    updateInformation = pyqtSignal() # void updateInformation(int,int) - signal
    urlEntered = pyqtSignal() # void urlEntered(const KUrlamp;) - signal
    def slotCompletionMatch(self, match):
        '''void KDirOperator.slotCompletionMatch(QString match)'''
    def toggleIgnoreCase(self):
        '''void KDirOperator.toggleIgnoreCase()'''
    def toggleDirsFirst(self):
        '''void KDirOperator.toggleDirsFirst()'''
    def sortReversed(self):
        '''void KDirOperator.sortReversed()'''
    def sortByType(self):
        '''void KDirOperator.sortByType()'''
    def sortByDate(self):
        '''void KDirOperator.sortByDate()'''
    def sortBySize(self):
        '''void KDirOperator.sortBySize()'''
    def sortByName(self):
        '''void KDirOperator.sortByName()'''
    def highlightFile(self, item):
        '''void KDirOperator.highlightFile(KFileItem item)'''
    def selectFile(self, item):
        '''void KDirOperator.selectFile(KFileItem item)'''
    def selectDir(self, item):
        '''void KDirOperator.selectDir(KFileItem item)'''
    def pathChanged(self):
        '''void KDirOperator.pathChanged()'''
    def resetCursor(self):
        '''void KDirOperator.resetCursor()'''
    def setIconsZoom(self, value):
        '''void KDirOperator.setIconsZoom(int value)'''
    def trashSelected(self):
        '''void KDirOperator.trashSelected()'''
    def makeDirCompletion(self):
        '''QString KDirOperator.makeDirCompletion()'''
        return QString()
    def makeCompletion(self):
        '''QString KDirOperator.makeCompletion()'''
        return QString()
    def updateSelectionDependentActions(self):
        '''void KDirOperator.updateSelectionDependentActions()'''
    def deleteSelected(self):
        '''void KDirOperator.deleteSelected()'''
    def rereadDir(self):
        '''void KDirOperator.rereadDir()'''
    def updateDir(self):
        '''void KDirOperator.updateDir()'''
    def cdUp(self):
        '''void KDirOperator.cdUp()'''
    def home(self):
        '''void KDirOperator.home()'''
    def forward(self):
        '''void KDirOperator.forward()'''
    def back(self):
        '''void KDirOperator.back()'''
    def eventFilter(self, watched, event):
        '''bool KDirOperator.eventFilter(QObject watched, QEvent event)'''
        return bool()
    def changeEvent(self, event):
        '''void KDirOperator.changeEvent(QEvent event)'''
    def activatedMenu(self, item, pos):
        '''void KDirOperator.activatedMenu(KFileItem item, QPoint pos)'''
    def checkPreviewSupport(self):
        '''bool KDirOperator.checkPreviewSupport()'''
        return bool()
    def prepareCompletionObjects(self):
        '''void KDirOperator.prepareCompletionObjects()'''
    def updateViewActions(self):
        '''void KDirOperator.updateViewActions()'''
    def updateSortActions(self):
        '''void KDirOperator.updateSortActions()'''
    def setupActions(self):
        '''void KDirOperator.setupActions()'''
    def resizeEvent(self, event):
        '''void KDirOperator.resizeEvent(QResizeEvent event)'''
    def setDirLister(self, lister):
        '''void KDirOperator.setDirLister(KDirLister lister)'''
    def createView(self, parent, viewKind):
        '''QAbstractItemView KDirOperator.createView(QWidget parent, KFile.FileView viewKind)'''
        return QAbstractItemView()
    def isSaving(self):
        '''bool KDirOperator.isSaving()'''
        return bool()
    def setIsSaving(self, isSaving):
        '''void KDirOperator.setIsSaving(bool isSaving)'''
    def iconsZoom(self):
        '''int KDirOperator.iconsZoom()'''
        return int()
    def isInlinePreviewShown(self):
        '''bool KDirOperator.isInlinePreviewShown()'''
        return bool()
    def setDecorationPosition(self, position):
        '''void KDirOperator.setDecorationPosition(QStyleOptionViewItem.Position position)'''
    def decorationPosition(self):
        '''QStyleOptionViewItem.Position KDirOperator.decorationPosition()'''
        return QStyleOptionViewItem.Position()
    def setInlinePreviewShown(self, show):
        '''void KDirOperator.setInlinePreviewShown(bool show)'''
    def previewGenerator(self):
        '''KFilePreviewGenerator KDirOperator.previewGenerator()'''
        return KFilePreviewGenerator()
    def trash(self, items, parent, ask = True, showProgress = True):
        '''KIO.CopyJob KDirOperator.trash(KFileItemList items, QWidget parent, bool ask = True, bool showProgress = True)'''
        return KIO.CopyJob()
    def setDropOptions(self, options):
        '''void KDirOperator.setDropOptions(int options)'''
    def setAcceptDrops(self, b):
        '''void KDirOperator.setAcceptDrops(bool b)'''
    def setupMenu(self, whichActions):
        '''void KDirOperator.setupMenu(int whichActions)'''
    def setupMenu(self):
        '''void KDirOperator.setupMenu()'''
    def dirOnlyMode(self):
        '''bool KDirOperator.dirOnlyMode()'''
        return bool()
    def dirOnlyMode(self, mode):
        '''static bool KDirOperator.dirOnlyMode(int mode)'''
        return bool()
    def dirHighlighting(self):
        '''bool KDirOperator.dirHighlighting()'''
        return bool()
    def setEnableDirHighlighting(self, enable):
        '''void KDirOperator.setEnableDirHighlighting(bool enable)'''
    def clearHistory(self):
        '''void KDirOperator.clearHistory()'''
    def del_(self, items, parent = None, ask = True, showProgress = True):
        '''KIO.DeleteJob KDirOperator.del_(KFileItemList items, QWidget parent = None, bool ask = True, bool showProgress = True)'''
        return KIO.DeleteJob()
    def mkdir(self, directory, enterDirectory = True):
        '''bool KDirOperator.mkdir(QString directory, bool enterDirectory = True)'''
        return bool()
    def mkdir(self):
        '''void KDirOperator.mkdir()'''
    def onlyDoubleClickSelectsFiles(self):
        '''bool KDirOperator.onlyDoubleClickSelectsFiles()'''
        return bool()
    def setOnlyDoubleClickSelectsFiles(self, enable):
        '''void KDirOperator.setOnlyDoubleClickSelectsFiles(bool enable)'''
    def writeConfig(self, configGroup):
        '''void KDirOperator.writeConfig(KConfigGroup configGroup)'''
    def readConfig(self, configGroup):
        '''void KDirOperator.readConfig(KConfigGroup configGroup)'''
    def viewConfigGroup(self):
        '''KConfigGroup KDirOperator.viewConfigGroup()'''
        return KConfigGroup()
    def setViewConfig(self, configGroup):
        '''void KDirOperator.setViewConfig(KConfigGroup configGroup)'''
    def actionCollection(self):
        '''KActionCollection KDirOperator.actionCollection()'''
        return KActionCollection()
    def dirCompletionObject(self):
        '''KCompletion KDirOperator.dirCompletionObject()'''
        return KCompletion()
    def completionObject(self):
        '''KCompletion KDirOperator.completionObject()'''
        return KCompletion()
    def numFiles(self):
        '''int KDirOperator.numFiles()'''
        return int()
    def numDirs(self):
        '''int KDirOperator.numDirs()'''
        return int()
    def isSelected(self, item):
        '''bool KDirOperator.isSelected(KFileItem item)'''
        return bool()
    def selectedItems(self):
        '''KFileItemList KDirOperator.selectedItems()'''
        return KFileItemList()
    def setPreviewWidget(self, w):
        '''void KDirOperator.setPreviewWidget(KPreviewWidgetBase w)'''
    def mode(self):
        '''KFile.Modes KDirOperator.mode()'''
        return KFile.Modes()
    def setMode(self, m):
        '''void KDirOperator.setMode(KFile.Modes m)'''
    def progressBar(self):
        '''QProgressBar KDirOperator.progressBar()'''
        return QProgressBar()
    def dirLister(self):
        '''KDirLister KDirOperator.dirLister()'''
        return KDirLister()
    def isRoot(self):
        '''bool KDirOperator.isRoot()'''
        return bool()
    def sorting(self):
        '''QDir.SortFlags KDirOperator.sorting()'''
        return QDir.SortFlags()
    def setSorting(self):
        '''QDir.SortFlags KDirOperator.setSorting()'''
        return QDir.SortFlags()
    def view(self):
        '''QAbstractItemView KDirOperator.view()'''
        return QAbstractItemView()
    def setView(self, view):
        '''void KDirOperator.setView(QAbstractItemView view)'''
    def setView(self, viewKind):
        '''void KDirOperator.setView(KFile.FileView viewKind)'''
    def setCurrentItems(self, urls):
        '''void KDirOperator.setCurrentItems(QStringList urls)'''
    def setCurrentItems(self, items):
        '''void KDirOperator.setCurrentItems(KFileItemList items)'''
    def setCurrentItem(self, url):
        '''void KDirOperator.setCurrentItem(QString url)'''
    def setCurrentItem(self, item):
        '''void KDirOperator.setCurrentItem(KFileItem item)'''
    def setUrl(self, url, clearforward):
        '''void KDirOperator.setUrl(KUrl url, bool clearforward)'''
    def url(self):
        '''KUrl KDirOperator.url()'''
        return KUrl()
    def clearFilter(self):
        '''void KDirOperator.clearFilter()'''
    def mimeFilter(self):
        '''QStringList KDirOperator.mimeFilter()'''
        return QStringList()
    def setMimeFilter(self, mimetypes):
        '''void KDirOperator.setMimeFilter(QStringList mimetypes)'''
    def nameFilter(self):
        '''QString KDirOperator.nameFilter()'''
        return QString()
    def setNameFilter(self, filter):
        '''void KDirOperator.setNameFilter(QString filter)'''
    def close(self):
        '''void KDirOperator.close()'''
    def showHiddenFiles(self):
        '''bool KDirOperator.showHiddenFiles()'''
        return bool()
    def setShowHiddenFiles(self, s):
        '''void KDirOperator.setShowHiddenFiles(bool s)'''


class KDirSelectDialog(KDialog):
    """"""
    def __init__(self, startDir = KUrl(), localOnly = False, parent = None):
        '''void KDirSelectDialog.__init__(KUrl startDir = KUrl(), bool localOnly = False, QWidget parent = None)'''
    def hideEvent(self, event):
        '''void KDirSelectDialog.hideEvent(QHideEvent event)'''
    def accept(self):
        '''void KDirSelectDialog.accept()'''
    def setCurrentUrl(self, url):
        '''void KDirSelectDialog.setCurrentUrl(KUrl url)'''
    def startDir(self):
        '''KUrl KDirSelectDialog.startDir()'''
        return KUrl()
    def selectDirectory(self, startDir = KUrl(), localOnly = False, parent = None, caption = QString()):
        '''static KUrl KDirSelectDialog.selectDirectory(KUrl startDir = KUrl(), bool localOnly = False, QWidget parent = None, QString caption = QString())'''
        return KUrl()
    def localOnly(self):
        '''bool KDirSelectDialog.localOnly()'''
        return bool()
    def view(self):
        '''QAbstractItemView KDirSelectDialog.view()'''
        return QAbstractItemView()
    def url(self):
        '''KUrl KDirSelectDialog.url()'''
        return KUrl()


class KDirSortFilterProxyModel(KCategorizedSortFilterProxyModel):
    """"""
    def __init__(self, parent = None):
        '''void KDirSortFilterProxyModel.__init__(QObject parent = None)'''
    def subSortLessThan(self, left, right):
        '''bool KDirSortFilterProxyModel.subSortLessThan(QModelIndex left, QModelIndex right)'''
        return bool()
    def sortFoldersFirst(self):
        '''bool KDirSortFilterProxyModel.sortFoldersFirst()'''
        return bool()
    def setSortFoldersFirst(self, foldersFirst):
        '''void KDirSortFilterProxyModel.setSortFoldersFirst(bool foldersFirst)'''
    def pointsForPermissions(self, info):
        '''static int KDirSortFilterProxyModel.pointsForPermissions(QFileInfo info)'''
        return int()
    def canFetchMore(self, parent):
        '''bool KDirSortFilterProxyModel.canFetchMore(QModelIndex parent)'''
        return bool()
    def hasChildren(self, parent = QModelIndex()):
        '''bool KDirSortFilterProxyModel.hasChildren(QModelIndex parent = QModelIndex())'''
        return bool()


class KDirWatch(QObject):
    """"""
    # Enum KDirWatch.Method
    FAM = 0
    INotify = 0
    DNotify = 0
    Stat = 0

    # Enum KDirWatch.WatchMode
    WatchDirOnly = 0
    WatchFiles = 0
    WatchSubDirs = 0

    def __init__(self, parent = None):
        '''void KDirWatch.__init__(QObject parent = None)'''
    deleted = pyqtSignal() # void deleted(const QStringamp;) - signal
    created = pyqtSignal() # void created(const QStringamp;) - signal
    dirty = pyqtSignal() # void dirty(const QStringamp;) - signal
    def exists(self):
        '''static bool KDirWatch.exists()'''
        return bool()
    def self(self):
        '''static KDirWatch KDirWatch.self()'''
        return KDirWatch()
    def internalMethod(self):
        '''KDirWatch.Method KDirWatch.internalMethod()'''
        return KDirWatch.Method()
    def setDeleted(self, path):
        '''void KDirWatch.setDeleted(QString path)'''
    def setDirty(self, path):
        '''void KDirWatch.setDirty(QString path)'''
    def setCreated(self, path):
        '''void KDirWatch.setCreated(QString path)'''
    def statistics(self):
        '''static void KDirWatch.statistics()'''
    def contains(self, path):
        '''bool KDirWatch.contains(QString path)'''
        return bool()
    def isStopped(self):
        '''bool KDirWatch.isStopped()'''
        return bool()
    def stopScan(self):
        '''void KDirWatch.stopScan()'''
    def startScan(self, notify = False, skippedToo = False):
        '''void KDirWatch.startScan(bool notify = False, bool skippedToo = False)'''
    def restartDirScan(self, path):
        '''bool KDirWatch.restartDirScan(QString path)'''
        return bool()
    def stopDirScan(self, path):
        '''bool KDirWatch.stopDirScan(QString path)'''
        return bool()
    def removeFile(self, file):
        '''void KDirWatch.removeFile(QString file)'''
    def removeDir(self, path):
        '''void KDirWatch.removeDir(QString path)'''
    def ctime(self, path):
        '''QDateTime KDirWatch.ctime(QString path)'''
        return QDateTime()
    def addFile(self, file):
        '''void KDirWatch.addFile(QString file)'''
    def addDir(self, path, watchModes = None):
        '''void KDirWatch.addDir(QString path, KDirWatch.WatchModes watchModes = KDirWatch.WatchDirOnly)'''
    class WatchModes():
        """"""
        def __init__(self):
            '''KDirWatch.WatchModes KDirWatch.WatchModes.__init__()'''
            return KDirWatch.WatchModes()
        def __init__(self):
            '''int KDirWatch.WatchModes.__init__()'''
            return int()
        def __init__(self):
            '''void KDirWatch.WatchModes.__init__()'''
        def __bool__(self):
            '''int KDirWatch.WatchModes.__bool__()'''
            return int()
        def __ne__(self, f):
            '''bool KDirWatch.WatchModes.__ne__(KDirWatch.WatchModes f)'''
            return bool()
        def __eq__(self, f):
            '''bool KDirWatch.WatchModes.__eq__(KDirWatch.WatchModes f)'''
            return bool()
        def __invert__(self):
            '''KDirWatch.WatchModes KDirWatch.WatchModes.__invert__()'''
            return KDirWatch.WatchModes()
        def __and__(self, mask):
            '''KDirWatch.WatchModes KDirWatch.WatchModes.__and__(int mask)'''
            return KDirWatch.WatchModes()
        def __xor__(self, f):
            '''KDirWatch.WatchModes KDirWatch.WatchModes.__xor__(KDirWatch.WatchModes f)'''
            return KDirWatch.WatchModes()
        def __xor__(self, f):
            '''KDirWatch.WatchModes KDirWatch.WatchModes.__xor__(int f)'''
            return KDirWatch.WatchModes()
        def __or__(self, f):
            '''KDirWatch.WatchModes KDirWatch.WatchModes.__or__(KDirWatch.WatchModes f)'''
            return KDirWatch.WatchModes()
        def __or__(self, f):
            '''KDirWatch.WatchModes KDirWatch.WatchModes.__or__(int f)'''
            return KDirWatch.WatchModes()
        def __int__(self):
            '''int KDirWatch.WatchModes.__int__()'''
            return int()
        def __ixor__(self, f):
            '''KDirWatch.WatchModes KDirWatch.WatchModes.__ixor__(KDirWatch.WatchModes f)'''
            return KDirWatch.WatchModes()
        def __ior__(self, f):
            '''KDirWatch.WatchModes KDirWatch.WatchModes.__ior__(KDirWatch.WatchModes f)'''
            return KDirWatch.WatchModes()
        def __iand__(self, mask):
            '''KDirWatch.WatchModes KDirWatch.WatchModes.__iand__(int mask)'''
            return KDirWatch.WatchModes()


class KDiskFreeSpace(QObject):
    """"""
    def __init__(self, parent = None):
        '''void KDiskFreeSpace.__init__(QObject parent = None)'''
    done = pyqtSignal() # void done() - signal
    foundMountPoint = pyqtSignal() # void foundMountPoint(const QStringamp;,quint64,quint64,quint64) - signal
    def findUsageInfo(self, path):
        '''static KDiskFreeSpace KDiskFreeSpace.findUsageInfo(QString path)'''
        return KDiskFreeSpace()
    def readDF(self, mountPoint):
        '''bool KDiskFreeSpace.readDF(QString mountPoint)'''
        return bool()


class KDiskFreeSpaceInfo():
    """"""
    def __init__(self):
        '''KDiskFreeSpaceInfo KDiskFreeSpaceInfo.__init__()'''
        return KDiskFreeSpaceInfo()
    def freeSpaceInfo(self, path):
        '''static KDiskFreeSpaceInfo KDiskFreeSpaceInfo.freeSpaceInfo(QString path)'''
        return KDiskFreeSpaceInfo()
    def used(self):
        '''int KDiskFreeSpaceInfo.used()'''
        return int()
    def available(self):
        '''int KDiskFreeSpaceInfo.available()'''
        return int()
    def size(self):
        '''int KDiskFreeSpaceInfo.size()'''
        return int()
    def mountPoint(self):
        '''QString KDiskFreeSpaceInfo.mountPoint()'''
        return QString()
    def isValid(self):
        '''bool KDiskFreeSpaceInfo.isValid()'''
        return bool()


class KEMailSettings():
    """"""
    # Enum KEMailSettings.Extension
    POP3 = 0
    SMTP = 0
    OTHER = 0

    # Enum KEMailSettings.Setting
    ClientProgram = 0
    ClientTerminal = 0
    RealName = 0
    EmailAddress = 0
    ReplyToAddress = 0
    Organization = 0
    OutServer = 0
    OutServerLogin = 0
    OutServerPass = 0
    OutServerType = 0
    OutServerCommand = 0
    OutServerTLS = 0
    InServer = 0
    InServerLogin = 0
    InServerPass = 0
    InServerType = 0
    InServerMBXType = 0
    InServerTLS = 0

    def __init__(self):
        '''void KEMailSettings.__init__()'''
    def setSetting(self, s, v):
        '''void KEMailSettings.setSetting(KEMailSettings.Setting s, QString v)'''
    def getSetting(self, s):
        '''QString KEMailSettings.getSetting(KEMailSettings.Setting s)'''
        return QString()
    def setDefault(self, def_):
        '''void KEMailSettings.setDefault(QString def)'''
    def defaultProfileName(self):
        '''QString KEMailSettings.defaultProfileName()'''
        return QString()
    def setProfile(self, s):
        '''void KEMailSettings.setProfile(QString s)'''
    def currentProfileName(self):
        '''QString KEMailSettings.currentProfileName()'''
        return QString()
    def profiles(self):
        '''QStringList KEMailSettings.profiles()'''
        return QStringList()


class KFileDialog(KDialog):
    """"""
    # Enum KFileDialog.Option
    ConfirmOverwrite = 0
    ShowInlinePreview = 0

    # Enum KFileDialog.OperationMode
    Other = 0
    Opening = 0
    Saving = 0

    def __init__(self, startDir, filter, parent, widget = None):
        '''void KFileDialog.__init__(KUrl startDir, QString filter, QWidget parent, QWidget widget = None)'''
    def slotCancel(self):
        '''void KFileDialog.slotCancel()'''
    def accept(self):
        '''void KFileDialog.accept()'''
    def slotOk(self):
        '''void KFileDialog.slotOk()'''
    def hideEvent(self, event):
        '''void KFileDialog.hideEvent(QHideEvent event)'''
    def keyPressEvent(self, e):
        '''void KFileDialog.keyPressEvent(QKeyEvent e)'''
    filterChanged = pyqtSignal() # void filterChanged(const QStringamp;) - signal
    selectionChanged = pyqtSignal() # void selectionChanged() - signal
    fileHighlighted = pyqtSignal() # void fileHighlighted(const QStringamp;) - signal
    fileHighlighted = pyqtSignal() # void fileHighlighted(const KUrlamp;) - signal
    fileSelected = pyqtSignal() # void fileSelected(const QStringamp;) - signal
    fileSelected = pyqtSignal() # void fileSelected(const KUrlamp;) - signal
    def setStartDir(self, directory):
        '''static void KFileDialog.setStartDir(KUrl directory)'''
    def getStartUrl(self, startDir, recentDirClass):
        '''static KUrl KFileDialog.getStartUrl(KUrl startDir, QString recentDirClass)'''
        return KUrl()
    def actionCollection(self):
        '''KActionCollection KFileDialog.actionCollection()'''
        return KActionCollection()
    def filterWidget(self):
        '''KFileFilterCombo KFileDialog.filterWidget()'''
        return KFileFilterCombo()
    def locationEdit(self):
        '''KUrlComboBox KFileDialog.locationEdit()'''
        return KUrlComboBox()
    def cancelButton(self):
        '''KPushButton KFileDialog.cancelButton()'''
        return KPushButton()
    def okButton(self):
        '''KPushButton KFileDialog.okButton()'''
        return KPushButton()
    def toolBar(self):
        '''KToolBar KFileDialog.toolBar()'''
        return KToolBar()
    def fileWidget(self):
        '''KAbstractFileWidget KFileDialog.fileWidget()'''
        return KAbstractFileWidget()
    def setLocationLabel(self, text):
        '''void KFileDialog.setLocationLabel(QString text)'''
    def mode(self):
        '''KFile.Modes KFileDialog.mode()'''
        return KFile.Modes()
    def setMode(self, m):
        '''void KFileDialog.setMode(KFile.Modes m)'''
    def getImageOpenUrl(self, startDir = KUrl(), parent = None, caption = QString()):
        '''static KUrl KFileDialog.getImageOpenUrl(KUrl startDir = KUrl(), QWidget parent = None, QString caption = QString())'''
        return KUrl()
    def getExistingDirectoryUrl(self, startDir = KUrl(), parent = None, caption = QString()):
        '''static KUrl KFileDialog.getExistingDirectoryUrl(KUrl startDir = KUrl(), QWidget parent = None, QString caption = QString())'''
        return KUrl()
    def getExistingDirectory(self, startDir = KUrl(), parent = None, caption = QString()):
        '''static QString KFileDialog.getExistingDirectory(KUrl startDir = KUrl(), QWidget parent = None, QString caption = QString())'''
        return QString()
    def getSaveUrl(self, startDir = KUrl(), filter = QString(), parent = None, caption = QString()):
        '''static KUrl KFileDialog.getSaveUrl(KUrl startDir = KUrl(), QString filter = QString(), QWidget parent = None, QString caption = QString())'''
        return KUrl()
    def getSaveUrl(self, startDir, filter, parent, caption, options):
        '''static KUrl KFileDialog.getSaveUrl(KUrl startDir, QString filter, QWidget parent, QString caption, KFileDialog.Options options)'''
        return KUrl()
    def getSaveFileNameWId(self, startDir, filter, parent_id, caption):
        '''static QString KFileDialog.getSaveFileNameWId(KUrl startDir, QString filter, int parent_id, QString caption)'''
        return QString()
    def getSaveFileNameWId(self, startDir, filter, parent_id, caption, options):
        '''static QString KFileDialog.getSaveFileNameWId(KUrl startDir, QString filter, int parent_id, QString caption, KFileDialog.Options options)'''
        return QString()
    def getSaveFileName(self, startDir = KUrl(), filter = QString(), parent = None, caption = QString()):
        '''static QString KFileDialog.getSaveFileName(KUrl startDir = KUrl(), QString filter = QString(), QWidget parent = None, QString caption = QString())'''
        return QString()
    def getSaveFileName(self, startDir, filter, parent, caption, options):
        '''static QString KFileDialog.getSaveFileName(KUrl startDir, QString filter, QWidget parent, QString caption, KFileDialog.Options options)'''
        return QString()
    def getOpenUrls(self, startDir = KUrl(), filter = QString(), parent = None, caption = QString()):
        '''static KUrl.List KFileDialog.getOpenUrls(KUrl startDir = KUrl(), QString filter = QString(), QWidget parent = None, QString caption = QString())'''
        return KUrl.List()
    def getOpenUrl(self, startDir = KUrl(), filter = QString(), parent = None, caption = QString()):
        '''static KUrl KFileDialog.getOpenUrl(KUrl startDir = KUrl(), QString filter = QString(), QWidget parent = None, QString caption = QString())'''
        return KUrl()
    def getOpenFileNames(self, startDir = KUrl(), filter = QString(), parent = None, caption = QString()):
        '''static QStringList KFileDialog.getOpenFileNames(KUrl startDir = KUrl(), QString filter = QString(), QWidget parent = None, QString caption = QString())'''
        return QStringList()
    def getOpenFileNameWId(self, startDir, filter, parent_id, caption):
        '''static QString KFileDialog.getOpenFileNameWId(KUrl startDir, QString filter, int parent_id, QString caption)'''
        return QString()
    def getOpenFileName(self, startDir = KUrl(), filter = QString(), parent = None, caption = QString()):
        '''static QString KFileDialog.getOpenFileName(KUrl startDir = KUrl(), QString filter = QString(), QWidget parent = None, QString caption = QString())'''
        return QString()
    def sizeHint(self):
        '''QSize KFileDialog.sizeHint()'''
        return QSize()
    def setConfirmOverwrite(self, enable):
        '''void KFileDialog.setConfirmOverwrite(bool enable)'''
    def setInlinePreviewShown(self, show):
        '''void KFileDialog.setInlinePreviewShown(bool show)'''
    def setPreviewWidget(self, w):
        '''void KFileDialog.setPreviewWidget(KPreviewWidgetBase w)'''
    def clearFilter(self):
        '''void KFileDialog.clearFilter()'''
    def currentMimeFilter(self):
        '''QString KFileDialog.currentMimeFilter()'''
        return QString()
    def setMimeFilter(self, types, defaultType = QString()):
        '''void KFileDialog.setMimeFilter(QStringList types, QString defaultType = QString())'''
    def currentFilterMimeType(self):
        '''unknown-type KFileDialog.currentFilterMimeType()'''
        return unknown-type()
    def currentFilter(self):
        '''QString KFileDialog.currentFilter()'''
        return QString()
    def setFilter(self, filter):
        '''void KFileDialog.setFilter(QString filter)'''
    def keepsLocation(self):
        '''bool KFileDialog.keepsLocation()'''
        return bool()
    def setKeepLocation(self, keep):
        '''void KFileDialog.setKeepLocation(bool keep)'''
    def operationMode(self):
        '''KFileDialog.OperationMode KFileDialog.operationMode()'''
        return KFileDialog.OperationMode()
    def setOperationMode(self):
        '''KFileDialog.OperationMode KFileDialog.setOperationMode()'''
        return KFileDialog.OperationMode()
    def setSelection(self, name):
        '''void KFileDialog.setSelection(QString name)'''
    def setUrl(self, url, clearforward = True):
        '''void KFileDialog.setUrl(KUrl url, bool clearforward = True)'''
    def selectedFiles(self):
        '''QStringList KFileDialog.selectedFiles()'''
        return QStringList()
    def selectedFile(self):
        '''QString KFileDialog.selectedFile()'''
        return QString()
    def baseUrl(self):
        '''KUrl KFileDialog.baseUrl()'''
        return KUrl()
    def selectedUrls(self):
        '''KUrl.List KFileDialog.selectedUrls()'''
        return KUrl.List()
    def selectedUrl(self):
        '''KUrl KFileDialog.selectedUrl()'''
        return KUrl()
    class Options():
        """"""
        def __init__(self):
            '''KFileDialog.Options KFileDialog.Options.__init__()'''
            return KFileDialog.Options()
        def __init__(self):
            '''int KFileDialog.Options.__init__()'''
            return int()
        def __init__(self):
            '''void KFileDialog.Options.__init__()'''
        def __bool__(self):
            '''int KFileDialog.Options.__bool__()'''
            return int()
        def __ne__(self, f):
            '''bool KFileDialog.Options.__ne__(KFileDialog.Options f)'''
            return bool()
        def __eq__(self, f):
            '''bool KFileDialog.Options.__eq__(KFileDialog.Options f)'''
            return bool()
        def __invert__(self):
            '''KFileDialog.Options KFileDialog.Options.__invert__()'''
            return KFileDialog.Options()
        def __and__(self, mask):
            '''KFileDialog.Options KFileDialog.Options.__and__(int mask)'''
            return KFileDialog.Options()
        def __xor__(self, f):
            '''KFileDialog.Options KFileDialog.Options.__xor__(KFileDialog.Options f)'''
            return KFileDialog.Options()
        def __xor__(self, f):
            '''KFileDialog.Options KFileDialog.Options.__xor__(int f)'''
            return KFileDialog.Options()
        def __or__(self, f):
            '''KFileDialog.Options KFileDialog.Options.__or__(KFileDialog.Options f)'''
            return KFileDialog.Options()
        def __or__(self, f):
            '''KFileDialog.Options KFileDialog.Options.__or__(int f)'''
            return KFileDialog.Options()
        def __int__(self):
            '''int KFileDialog.Options.__int__()'''
            return int()
        def __ixor__(self, f):
            '''KFileDialog.Options KFileDialog.Options.__ixor__(KFileDialog.Options f)'''
            return KFileDialog.Options()
        def __ior__(self, f):
            '''KFileDialog.Options KFileDialog.Options.__ior__(KFileDialog.Options f)'''
            return KFileDialog.Options()
        def __iand__(self, mask):
            '''KFileDialog.Options KFileDialog.Options.__iand__(int mask)'''
            return KFileDialog.Options()


class KEncodingFileDialog(KFileDialog):
    """"""
    def __init__(self, startDir = QString(), encoding = QString(), filter = QString(), caption = QString(), type = None, parent = None):
        '''void KEncodingFileDialog.__init__(QString startDir = QString(), QString encoding = QString(), QString filter = QString(), QString caption = QString(), KFileDialog.OperationMode type = KFileDialog.Opening, QWidget parent = None)'''
    def getSaveUrlAndEncoding(self, encoding = QString(), startDir = QString(), filter = QString(), parent = None, caption = QString()):
        '''static KEncodingFileDialog.Result KEncodingFileDialog.getSaveUrlAndEncoding(QString encoding = QString(), QString startDir = QString(), QString filter = QString(), QWidget parent = None, QString caption = QString())'''
        return KEncodingFileDialog.Result()
    def getSaveFileNameAndEncoding(self, encoding = QString(), startDir = QString(), filter = QString(), parent = None, caption = QString()):
        '''static KEncodingFileDialog.Result KEncodingFileDialog.getSaveFileNameAndEncoding(QString encoding = QString(), QString startDir = QString(), QString filter = QString(), QWidget parent = None, QString caption = QString())'''
        return KEncodingFileDialog.Result()
    def getOpenUrlsAndEncoding(self, encoding = QString(), startDir = QString(), filter = QString(), parent = None, caption = QString()):
        '''static KEncodingFileDialog.Result KEncodingFileDialog.getOpenUrlsAndEncoding(QString encoding = QString(), QString startDir = QString(), QString filter = QString(), QWidget parent = None, QString caption = QString())'''
        return KEncodingFileDialog.Result()
    def getOpenUrlAndEncoding(self, encoding = QString(), startDir = QString(), filter = QString(), parent = None, caption = QString()):
        '''static KEncodingFileDialog.Result KEncodingFileDialog.getOpenUrlAndEncoding(QString encoding = QString(), QString startDir = QString(), QString filter = QString(), QWidget parent = None, QString caption = QString())'''
        return KEncodingFileDialog.Result()
    def getOpenFileNamesAndEncoding(self, encoding = QString(), startDir = QString(), filter = QString(), parent = None, caption = QString()):
        '''static KEncodingFileDialog.Result KEncodingFileDialog.getOpenFileNamesAndEncoding(QString encoding = QString(), QString startDir = QString(), QString filter = QString(), QWidget parent = None, QString caption = QString())'''
        return KEncodingFileDialog.Result()
    def getOpenFileNameAndEncoding(self, encoding = QString(), startDir = QString(), filter = QString(), parent = None, caption = QString()):
        '''static KEncodingFileDialog.Result KEncodingFileDialog.getOpenFileNameAndEncoding(QString encoding = QString(), QString startDir = QString(), QString filter = QString(), QWidget parent = None, QString caption = QString())'''
        return KEncodingFileDialog.Result()
    def selectedEncoding(self):
        '''QString KEncodingFileDialog.selectedEncoding()'''
        return QString()
    class Result():
        """"""
        URLs = None # KUrl.List - member
        encoding = None # QString - member
        fileNames = None # QStringList - member
        def __init__(self):
            '''void KEncodingFileDialog.Result.__init__()'''
        def __init__(self):
            '''KEncodingFileDialog.Result KEncodingFileDialog.Result.__init__()'''
            return KEncodingFileDialog.Result()


class KFile():
    """"""
    # Enum KFile.SelectionMode
    Single = 0
    Multi = 0
    Extended = 0
    NoSelection = 0

    # Enum KFile.FileView
    Default = 0
    Simple = 0
    Detail = 0
    SeparateDirs = 0
    PreviewContents = 0
    PreviewInfo = 0
    Tree = 0
    DetailTree = 0
    FileViewMax = 0

    # Enum KFile.Mode
    File = 0
    Directory = 0
    Files = 0
    ExistingOnly = 0
    LocalOnly = 0
    ModeMax = 0

    def __init__(self):
        '''KFile KFile.__init__()'''
        return KFile()
    def isDetailTreeView(self, view):
        '''static bool KFile.isDetailTreeView(KFile.FileView view)'''
        return bool()
    def isTreeView(self, view):
        '''static bool KFile.isTreeView(KFile.FileView view)'''
        return bool()
    def isPreviewInfo(self, view):
        '''static bool KFile.isPreviewInfo(KFile.FileView view)'''
        return bool()
    def isPreviewContents(self, view):
        '''static bool KFile.isPreviewContents(KFile.FileView view)'''
        return bool()
    def isSeparateDirs(self, view):
        '''static bool KFile.isSeparateDirs(KFile.FileView view)'''
        return bool()
    def isDetailView(self, view):
        '''static bool KFile.isDetailView(KFile.FileView view)'''
        return bool()
    def isSimpleView(self, view):
        '''static bool KFile.isSimpleView(KFile.FileView view)'''
        return bool()
    def isDefaultView(self, view):
        '''static bool KFile.isDefaultView(KFile.FileView view)'''
        return bool()
    def isSortCaseInsensitive(self, sort):
        '''static bool KFile.isSortCaseInsensitive(QDir.SortFlags sort)'''
        return bool()
    def isSortDirsFirst(self, sort):
        '''static bool KFile.isSortDirsFirst(QDir.SortFlags sort)'''
        return bool()
    def isSortByType(self, sort):
        '''static bool KFile.isSortByType(QDir.SortFlags sort)'''
        return bool()
    def isSortByDate(self, sort):
        '''static bool KFile.isSortByDate(QDir.SortFlags sort)'''
        return bool()
    def isSortBySize(self, sort):
        '''static bool KFile.isSortBySize(QDir.SortFlags sort)'''
        return bool()
    def isSortByName(self, sort):
        '''static bool KFile.isSortByName(QDir.SortFlags sort)'''
        return bool()
    class Modes():
        """"""
        def __init__(self):
            '''KFile.Modes KFile.Modes.__init__()'''
            return KFile.Modes()
        def __init__(self):
            '''int KFile.Modes.__init__()'''
            return int()
        def __init__(self):
            '''void KFile.Modes.__init__()'''
        def __bool__(self):
            '''int KFile.Modes.__bool__()'''
            return int()
        def __ne__(self, f):
            '''bool KFile.Modes.__ne__(KFile.Modes f)'''
            return bool()
        def __eq__(self, f):
            '''bool KFile.Modes.__eq__(KFile.Modes f)'''
            return bool()
        def __invert__(self):
            '''KFile.Modes KFile.Modes.__invert__()'''
            return KFile.Modes()
        def __and__(self, mask):
            '''KFile.Modes KFile.Modes.__and__(int mask)'''
            return KFile.Modes()
        def __xor__(self, f):
            '''KFile.Modes KFile.Modes.__xor__(KFile.Modes f)'''
            return KFile.Modes()
        def __xor__(self, f):
            '''KFile.Modes KFile.Modes.__xor__(int f)'''
            return KFile.Modes()
        def __or__(self, f):
            '''KFile.Modes KFile.Modes.__or__(KFile.Modes f)'''
            return KFile.Modes()
        def __or__(self, f):
            '''KFile.Modes KFile.Modes.__or__(int f)'''
            return KFile.Modes()
        def __int__(self):
            '''int KFile.Modes.__int__()'''
            return int()
        def __ixor__(self, f):
            '''KFile.Modes KFile.Modes.__ixor__(KFile.Modes f)'''
            return KFile.Modes()
        def __ior__(self, f):
            '''KFile.Modes KFile.Modes.__ior__(KFile.Modes f)'''
            return KFile.Modes()
        def __iand__(self, mask):
            '''KFile.Modes KFile.Modes.__iand__(int mask)'''
            return KFile.Modes()


class KFileFilterCombo(KComboBox):
    """"""
    def __init__(self, parent = None):
        '''void KFileFilterCombo.__init__(QWidget parent = None)'''
    def isMimeFilter(self):
        '''bool KFileFilterCombo.isMimeFilter()'''
        return bool()
    filterChanged = pyqtSignal() # void filterChanged() - signal
    def eventFilter(self):
        '''QEvent KFileFilterCombo.eventFilter()'''
        return QEvent()
    def filters(self):
        '''QStringList KFileFilterCombo.filters()'''
        return QStringList()
    def defaultFilter(self):
        '''QString KFileFilterCombo.defaultFilter()'''
        return QString()
    def setDefaultFilter(self, filter):
        '''void KFileFilterCombo.setDefaultFilter(QString filter)'''
    def showsAllTypes(self):
        '''bool KFileFilterCombo.showsAllTypes()'''
        return bool()
    def setMimeFilter(self, types, defaultType):
        '''void KFileFilterCombo.setMimeFilter(QStringList types, QString defaultType)'''
    def setCurrentFilter(self, filter):
        '''void KFileFilterCombo.setCurrentFilter(QString filter)'''
    def currentFilter(self):
        '''QString KFileFilterCombo.currentFilter()'''
        return QString()
    def setFilter(self, filter):
        '''void KFileFilterCombo.setFilter(QString filter)'''


class KFileItem():
    """"""
    # Enum KFileItem.FileTimes
    ModificationTime = 0
    AccessTime = 0
    CreationTime = 0

    Unknown = None # int - member
    def __init__(self):
        '''void KFileItem.__init__()'''
    def __init__(self, entry, itemOrDirUrl, delayedMimeTypes = False, urlIsDirectory = False):
        '''void KFileItem.__init__(KIO.UDSEntry entry, KUrl itemOrDirUrl, bool delayedMimeTypes = False, bool urlIsDirectory = False)'''
    def __init__(self, mode, permissions, url, delayedMimeTypes = False):
        '''void KFileItem.__init__(int mode, int permissions, KUrl url, bool delayedMimeTypes = False)'''
    def __init__(self, url, mimeType, mode):
        '''void KFileItem.__init__(KUrl url, QString mimeType, int mode)'''
    def __init__(self, other):
        '''void KFileItem.__init__(KFileItem other)'''
    def isSlow(self):
        '''bool KFileItem.isSlow()'''
        return bool()
    def comment(self):
        '''QString KFileItem.comment()'''
        return QString()
    def nepomukUri(self):
        '''KUrl KFileItem.nepomukUri()'''
        return KUrl()
    def isNull(self):
        '''bool KFileItem.isNull()'''
        return bool()
    def mostLocalUrl(self, local):
        '''KUrl KFileItem.mostLocalUrl(bool local)'''
        return KUrl()
    def setUDSEntry(self, entry, url, delayedMimeTypes = False, urlIsDirectory = False):
        '''void KFileItem.setUDSEntry(KIO.UDSEntry entry, KUrl url, bool delayedMimeTypes = False, bool urlIsDirectory = False)'''
    def assign(self, item):
        '''void KFileItem.assign(KFileItem item)'''
    def metaInfo(self, autoget = True, what = None):
        '''KFileMetaInfo KFileItem.metaInfo(bool autoget = True, int what = KFileMetaInfo.Fastest)'''
        return KFileMetaInfo()
    def setMetaInfo(self, info):
        '''void KFileItem.setMetaInfo(KFileMetaInfo info)'''
    def __ne__(self, other):
        '''bool KFileItem.__ne__(KFileItem other)'''
        return bool()
    def __eq__(self, other):
        '''bool KFileItem.__eq__(KFileItem other)'''
        return bool()
    def cmp(self, item):
        '''bool KFileItem.cmp(KFileItem item)'''
        return bool()
    def isRegularFile(self):
        '''bool KFileItem.isRegularFile()'''
        return bool()
    def unmark(self):
        '''void KFileItem.unmark()'''
    def mark(self):
        '''void KFileItem.mark()'''
    def isMarked(self):
        '''bool KFileItem.isMarked()'''
        return bool()
    def entry(self):
        '''KIO.UDSEntry KFileItem.entry()'''
        return KIO.UDSEntry()
    def run(self, parentWidget = None):
        '''void KFileItem.run(QWidget parentWidget = None)'''
    def acceptsDrops(self):
        '''bool KFileItem.acceptsDrops()'''
        return bool()
    def getToolTipText(self, maxcount = 6):
        '''QString KFileItem.getToolTipText(int maxcount = 6)'''
        return QString()
    def getStatusBarInfo(self):
        '''QString KFileItem.getStatusBarInfo()'''
        return QString()
    def overlays(self):
        '''QStringList KFileItem.overlays()'''
        return QStringList()
    def pixmap(self, _size, _state = 0):
        '''QPixmap KFileItem.pixmap(int _size, int _state = 0)'''
        return QPixmap()
    def iconName(self):
        '''QString KFileItem.iconName()'''
        return QString()
    def mimeComment(self):
        '''QString KFileItem.mimeComment()'''
        return QString()
    def isMimeTypeKnown(self):
        '''bool KFileItem.isMimeTypeKnown()'''
        return bool()
    def mimeTypePtr(self):
        '''unknown-type KFileItem.mimeTypePtr()'''
        return unknown-type()
    def determineMimeType(self):
        '''unknown-type KFileItem.determineMimeType()'''
        return unknown-type()
    def mimetype(self):
        '''QString KFileItem.mimetype()'''
        return QString()
    def name(self, lowerCase = False):
        '''QString KFileItem.name(bool lowerCase = False)'''
        return QString()
    def text(self):
        '''QString KFileItem.text()'''
        return QString()
    def isLocalFile(self):
        '''bool KFileItem.isLocalFile()'''
        return bool()
    def timeString(self, which = None):
        '''QString KFileItem.timeString(KFileItem.FileTimes which = KFileItem.ModificationTime)'''
        return QString()
    def timeString(self, which):
        '''QString KFileItem.timeString(int which)'''
        return QString()
    def time(self, which):
        '''KDateTime KFileItem.time(KFileItem.FileTimes which)'''
        return KDateTime()
    def time(self, which):
        '''int KFileItem.time(int which)'''
        return int()
    def size(self):
        '''int KFileItem.size()'''
        return int()
    def localPath(self):
        '''QString KFileItem.localPath()'''
        return QString()
    def targetUrl(self):
        '''KUrl KFileItem.targetUrl()'''
        return KUrl()
    def linkDest(self):
        '''QString KFileItem.linkDest()'''
        return QString()
    def isDesktopFile(self):
        '''bool KFileItem.isDesktopFile()'''
        return bool()
    def isHidden(self):
        '''bool KFileItem.isHidden()'''
        return bool()
    def isWritable(self):
        '''bool KFileItem.isWritable()'''
        return bool()
    def isReadable(self):
        '''bool KFileItem.isReadable()'''
        return bool()
    def isFile(self):
        '''bool KFileItem.isFile()'''
        return bool()
    def isDir(self):
        '''bool KFileItem.isDir()'''
        return bool()
    def isLink(self):
        '''bool KFileItem.isLink()'''
        return bool()
    def group(self):
        '''QString KFileItem.group()'''
        return QString()
    def user(self):
        '''QString KFileItem.user()'''
        return QString()
    def mode(self):
        '''int KFileItem.mode()'''
        return int()
    def defaultACL(self):
        '''KACL KFileItem.defaultACL()'''
        return KACL()
    def ACL(self):
        '''KACL KFileItem.ACL()'''
        return KACL()
    def hasExtendedACL(self):
        '''bool KFileItem.hasExtendedACL()'''
        return bool()
    def permissionsString(self):
        '''QString KFileItem.permissionsString()'''
        return QString()
    def permissions(self):
        '''int KFileItem.permissions()'''
        return int()
    def setName(self, name):
        '''void KFileItem.setName(QString name)'''
    def setUrl(self, url):
        '''void KFileItem.setUrl(KUrl url)'''
    def url(self):
        '''KUrl KFileItem.url()'''
        return KUrl()
    def refreshMimeType(self):
        '''void KFileItem.refreshMimeType()'''
    def refresh(self):
        '''void KFileItem.refresh()'''


class KFileItemList():
    """"""
    def __init__(self):
        '''void KFileItemList.__init__()'''
    def __init__(self, items):
        '''void KFileItemList.__init__(list-of-KFileItem items)'''
    def __init__(self):
        '''KFileItemList KFileItemList.__init__()'''
        return KFileItemList()
    def __getitem__(self):
        '''int KFileItemList.__getitem__()'''
        return int()
    def __getitem__(self):
        '''slice KFileItemList.__getitem__()'''
        return slice()
    def __delitem__(self):
        '''int KFileItemList.__delitem__()'''
        return int()
    def __delitem__(self):
        '''slice KFileItemList.__delitem__()'''
        return slice()
    def __setitem__(self):
        '''KFileItem KFileItemList.__setitem__()'''
        return KFileItem()
    def __setitem__(self):
        '''KFileItemList KFileItemList.__setitem__()'''
        return KFileItemList()
    def __len__(self):
        '''int KFileItemList.__len__()'''
        return int()
    def targetUrlList(self):
        '''KUrl.List KFileItemList.targetUrlList()'''
        return KUrl.List()
    def urlList(self):
        '''KUrl.List KFileItemList.urlList()'''
        return KUrl.List()
    def findByUrl(self, url):
        '''KFileItem KFileItemList.findByUrl(KUrl url)'''
        return KFileItem()
    def findByName(self, fileName):
        '''KFileItem KFileItemList.findByName(QString fileName)'''
        return KFileItem()


class KFileItemActionPlugin(QObject):
    """"""
    def __init__(self, parent):
        '''void KFileItemActionPlugin.__init__(QObject parent)'''
    def actions(self, fileItemInfos, parentWidget):
        '''abstract list-of-QAction KFileItemActionPlugin.actions(KFileItemListProperties fileItemInfos, QWidget parentWidget)'''
        return [QAction()]


class KFileItemActions(QObject):
    """"""
    def __init__(self, parent = None):
        '''void KFileItemActions.__init__(QObject parent = None)'''
    openWithDialogAboutToBeShown = pyqtSignal() # void openWithDialogAboutToBeShown() - signal
    def runPreferredApplications(self, fileOpenList, traderConstraint):
        '''void KFileItemActions.runPreferredApplications(KFileItemList fileOpenList, QString traderConstraint)'''
    def addOpenWithActionsTo(self, menu, traderConstraint = QString()):
        '''void KFileItemActions.addOpenWithActionsTo(QMenu menu, QString traderConstraint = QString())'''
    def associatedApplications(self, mimeTypeList, traderConstraint):
        '''static unknown-type KFileItemActions.associatedApplications(QStringList mimeTypeList, QString traderConstraint)'''
        return unknown-type()
    def addServiceActionsTo(self, menu):
        '''int KFileItemActions.addServiceActionsTo(QMenu menu)'''
        return int()
    def preferredOpenWithAction(self, traderConstraint):
        '''KAction KFileItemActions.preferredOpenWithAction(QString traderConstraint)'''
        return KAction()
    def setParentWidget(self, widget):
        '''void KFileItemActions.setParentWidget(QWidget widget)'''
    def setItemListProperties(self, itemList):
        '''void KFileItemActions.setItemListProperties(KFileItemListProperties itemList)'''


class KFileItemDelegate(QAbstractItemDelegate):
    """"""
    # Enum KFileItemDelegate.Information
    NoInformation = 0
    Size = 0
    Permissions = 0
    OctalPermissions = 0
    Owner = 0
    OwnerAndGroup = 0
    CreationTime = 0
    ModificationTime = 0
    AccessTime = 0
    MimeType = 0
    FriendlyMimeType = 0
    LinkDest = 0
    LocalPathOrUrl = 0
    Comment = 0

    def __init__(self, parent = None):
        '''void KFileItemDelegate.__init__(QObject parent = None)'''
    def jobTransfersVisible(self):
        '''bool KFileItemDelegate.jobTransfersVisible()'''
        return bool()
    def setJobTransfersVisible(self, jobTransfersVisible):
        '''void KFileItemDelegate.setJobTransfersVisible(bool jobTransfersVisible)'''
    def wrapMode(self):
        '''QTextOption.WrapMode KFileItemDelegate.wrapMode()'''
        return QTextOption.WrapMode()
    def setWrapMode(self, wrapMode):
        '''void KFileItemDelegate.setWrapMode(QTextOption.WrapMode wrapMode)'''
    def iconRect(self, option, index):
        '''QRect KFileItemDelegate.iconRect(QStyleOptionViewItem option, QModelIndex index)'''
        return QRect()
    def shape(self, option, index):
        '''QRegion KFileItemDelegate.shape(QStyleOptionViewItem option, QModelIndex index)'''
        return QRegion()
    def helpEvent(self, event, view, option, index):
        '''bool KFileItemDelegate.helpEvent(QHelpEvent event, QAbstractItemView view, QStyleOptionViewItem option, QModelIndex index)'''
        return bool()
    def eventFilter(self, object, event):
        '''bool KFileItemDelegate.eventFilter(QObject object, QEvent event)'''
        return bool()
    def showToolTipWhenElided(self):
        '''bool KFileItemDelegate.showToolTipWhenElided()'''
        return bool()
    def setShowToolTipWhenElided(self, showToolTip):
        '''void KFileItemDelegate.setShowToolTipWhenElided(bool showToolTip)'''
    def maximumSize(self):
        '''QSize KFileItemDelegate.maximumSize()'''
        return QSize()
    def setMaximumSize(self, size):
        '''void KFileItemDelegate.setMaximumSize(QSize size)'''
    def shadowBlur(self):
        '''float KFileItemDelegate.shadowBlur()'''
        return float()
    def setShadowBlur(self, radius):
        '''void KFileItemDelegate.setShadowBlur(float radius)'''
    def shadowOffset(self):
        '''QPointF KFileItemDelegate.shadowOffset()'''
        return QPointF()
    def setShadowOffset(self, offset):
        '''void KFileItemDelegate.setShadowOffset(QPointF offset)'''
    def shadowColor(self):
        '''QColor KFileItemDelegate.shadowColor()'''
        return QColor()
    def setShadowColor(self, color):
        '''void KFileItemDelegate.setShadowColor(QColor color)'''
    def setShowInformation(self, information):
        '''void KFileItemDelegate.setShowInformation(KFileItemDelegate.Information information)'''
    def updateEditorGeometry(self, editor, option, index):
        '''void KFileItemDelegate.updateEditorGeometry(QWidget editor, QStyleOptionViewItem option, QModelIndex index)'''
    def setModelData(self, editor, model, index):
        '''void KFileItemDelegate.setModelData(QWidget editor, QAbstractItemModel model, QModelIndex index)'''
    def setEditorData(self, editor, index):
        '''void KFileItemDelegate.setEditorData(QWidget editor, QModelIndex index)'''
    def editorEvent(self, event, model, option, index):
        '''bool KFileItemDelegate.editorEvent(QEvent event, QAbstractItemModel model, QStyleOptionViewItem option, QModelIndex index)'''
        return bool()
    def createEditor(self, parent, option, index):
        '''QWidget KFileItemDelegate.createEditor(QWidget parent, QStyleOptionViewItem option, QModelIndex index)'''
        return QWidget()
    def paint(self, painter, option, index):
        '''void KFileItemDelegate.paint(QPainter painter, QStyleOptionViewItem option, QModelIndex index)'''
    def sizeHint(self, option, index):
        '''QSize KFileItemDelegate.sizeHint(QStyleOptionViewItem option, QModelIndex index)'''
        return QSize()


class KFileItemListProperties():
    """"""
    def __init__(self):
        '''void KFileItemListProperties.__init__()'''
    def __init__(self, items):
        '''void KFileItemListProperties.__init__(KFileItemList items)'''
    def __init__(self):
        '''KFileItemListProperties KFileItemListProperties.__init__()'''
        return KFileItemListProperties()
    def mimeGroup(self):
        '''QString KFileItemListProperties.mimeGroup()'''
        return QString()
    def mimeType(self):
        '''QString KFileItemListProperties.mimeType()'''
        return QString()
    def isDirectory(self):
        '''bool KFileItemListProperties.isDirectory()'''
        return bool()
    def urlList(self):
        '''KUrl.List KFileItemListProperties.urlList()'''
        return KUrl.List()
    def items(self):
        '''KFileItemList KFileItemListProperties.items()'''
        return KFileItemList()
    def isLocal(self):
        '''bool KFileItemListProperties.isLocal()'''
        return bool()
    def supportsMoving(self):
        '''bool KFileItemListProperties.supportsMoving()'''
        return bool()
    def supportsWriting(self):
        '''bool KFileItemListProperties.supportsWriting()'''
        return bool()
    def supportsDeleting(self):
        '''bool KFileItemListProperties.supportsDeleting()'''
        return bool()
    def supportsReading(self):
        '''bool KFileItemListProperties.supportsReading()'''
        return bool()
    def setItems(self, items):
        '''void KFileItemListProperties.setItems(KFileItemList items)'''


class KFileMetaDataConfigurationWidget(QWidget):
    """"""
    def __init__(self, parent = None):
        '''void KFileMetaDataConfigurationWidget.__init__(QWidget parent = None)'''
    def event(self, event):
        '''bool KFileMetaDataConfigurationWidget.event(QEvent event)'''
        return bool()
    def sizeHint(self):
        '''QSize KFileMetaDataConfigurationWidget.sizeHint()'''
        return QSize()
    def save(self):
        '''void KFileMetaDataConfigurationWidget.save()'''
    def items(self):
        '''KFileItemList KFileMetaDataConfigurationWidget.items()'''
        return KFileItemList()
    def setItems(self, items):
        '''void KFileMetaDataConfigurationWidget.setItems(KFileItemList items)'''


class KFileMetaDataWidget(QWidget):
    """"""
    def __init__(self, parent = None):
        '''void KFileMetaDataWidget.__init__(QWidget parent = None)'''
    metaDataRequestFinished = pyqtSignal() # void metaDataRequestFinished(const KFileItemListamp;) - signal
    def event(self, event):
        '''bool KFileMetaDataWidget.event(QEvent event)'''
        return bool()
    urlActivated = pyqtSignal() # void urlActivated(const KUrlamp;) - signal
    def sizeHint(self):
        '''QSize KFileMetaDataWidget.sizeHint()'''
        return QSize()
    def isReadOnly(self):
        '''bool KFileMetaDataWidget.isReadOnly()'''
        return bool()
    def setReadOnly(self, readOnly):
        '''void KFileMetaDataWidget.setReadOnly(bool readOnly)'''
    def items(self):
        '''KFileItemList KFileMetaDataWidget.items()'''
        return KFileItemList()
    def setItems(self, items):
        '''void KFileMetaDataWidget.setItems(KFileItemList items)'''


class KFileMetaInfo():
    """"""
    # Enum KFileMetaInfo.What
    Fastest = 0
    TechnicalInfo = 0
    ContentInfo = 0
    ExternalSources = 0
    Thumbnail = 0
    LinkedData = 0
    Everything = 0

    def __init__(self, path, mimetype = QString(), w = None):
        '''void KFileMetaInfo.__init__(QString path, QString mimetype = QString(), KFileMetaInfo.WhatFlags w = KFileMetaInfo.Everything)'''
    def __init__(self, url):
        '''void KFileMetaInfo.__init__(KUrl url)'''
    def __init__(self):
        '''void KFileMetaInfo.__init__()'''
    def __init__(self):
        '''KFileMetaInfo KFileMetaInfo.__init__()'''
        return KFileMetaInfo()
    def url(self):
        '''KUrl KFileMetaInfo.url()'''
        return KUrl()
    def keys(self):
        '''QStringList KFileMetaInfo.keys()'''
        return QStringList()
    def supportedKeys(self):
        '''QStringList KFileMetaInfo.supportedKeys()'''
        return QStringList()
    def preferredKeys(self):
        '''QStringList KFileMetaInfo.preferredKeys()'''
        return QStringList()
    def isValid(self):
        '''bool KFileMetaInfo.isValid()'''
        return bool()
    def item(self, key):
        '''KFileMetaInfoItem KFileMetaInfo.item(QString key)'''
        return KFileMetaInfoItem()
    def items(self):
        '''dict-of-QString-KFileMetaInfoItem KFileMetaInfo.items()'''
        return dict-of-QString-KFileMetaInfoItem()
    def applyChanges(self):
        '''bool KFileMetaInfo.applyChanges()'''
        return bool()
    class WhatFlags():
        """"""
        def __init__(self):
            '''KFileMetaInfo.WhatFlags KFileMetaInfo.WhatFlags.__init__()'''
            return KFileMetaInfo.WhatFlags()
        def __init__(self):
            '''int KFileMetaInfo.WhatFlags.__init__()'''
            return int()
        def __init__(self):
            '''void KFileMetaInfo.WhatFlags.__init__()'''
        def __bool__(self):
            '''int KFileMetaInfo.WhatFlags.__bool__()'''
            return int()
        def __ne__(self, f):
            '''bool KFileMetaInfo.WhatFlags.__ne__(KFileMetaInfo.WhatFlags f)'''
            return bool()
        def __eq__(self, f):
            '''bool KFileMetaInfo.WhatFlags.__eq__(KFileMetaInfo.WhatFlags f)'''
            return bool()
        def __invert__(self):
            '''KFileMetaInfo.WhatFlags KFileMetaInfo.WhatFlags.__invert__()'''
            return KFileMetaInfo.WhatFlags()
        def __and__(self, mask):
            '''KFileMetaInfo.WhatFlags KFileMetaInfo.WhatFlags.__and__(int mask)'''
            return KFileMetaInfo.WhatFlags()
        def __xor__(self, f):
            '''KFileMetaInfo.WhatFlags KFileMetaInfo.WhatFlags.__xor__(KFileMetaInfo.WhatFlags f)'''
            return KFileMetaInfo.WhatFlags()
        def __xor__(self, f):
            '''KFileMetaInfo.WhatFlags KFileMetaInfo.WhatFlags.__xor__(int f)'''
            return KFileMetaInfo.WhatFlags()
        def __or__(self, f):
            '''KFileMetaInfo.WhatFlags KFileMetaInfo.WhatFlags.__or__(KFileMetaInfo.WhatFlags f)'''
            return KFileMetaInfo.WhatFlags()
        def __or__(self, f):
            '''KFileMetaInfo.WhatFlags KFileMetaInfo.WhatFlags.__or__(int f)'''
            return KFileMetaInfo.WhatFlags()
        def __int__(self):
            '''int KFileMetaInfo.WhatFlags.__int__()'''
            return int()
        def __ixor__(self, f):
            '''KFileMetaInfo.WhatFlags KFileMetaInfo.WhatFlags.__ixor__(KFileMetaInfo.WhatFlags f)'''
            return KFileMetaInfo.WhatFlags()
        def __ior__(self, f):
            '''KFileMetaInfo.WhatFlags KFileMetaInfo.WhatFlags.__ior__(KFileMetaInfo.WhatFlags f)'''
            return KFileMetaInfo.WhatFlags()
        def __iand__(self, mask):
            '''KFileMetaInfo.WhatFlags KFileMetaInfo.WhatFlags.__iand__(int mask)'''
            return KFileMetaInfo.WhatFlags()


class KFileMetaInfoItem():
    """"""
    def __init__(self):
        '''void KFileMetaInfoItem.__init__()'''
    def __init__(self, item):
        '''void KFileMetaInfoItem.__init__(KFileMetaInfoItem item)'''
    def prefix(self):
        '''QString KFileMetaInfoItem.prefix()'''
        return QString()
    def suffix(self):
        '''QString KFileMetaInfoItem.suffix()'''
        return QString()
    def name(self):
        '''QString KFileMetaInfoItem.name()'''
        return QString()
    def properties(self):
        '''PredicateProperties KFileMetaInfoItem.properties()'''
        return PredicateProperties()
    def isValid(self):
        '''bool KFileMetaInfoItem.isValid()'''
        return bool()
    def addValue(self):
        '''QVariant KFileMetaInfoItem.addValue()'''
        return QVariant()
    def setValue(self, value):
        '''bool KFileMetaInfoItem.setValue(QVariant value)'''
        return bool()
    def value(self):
        '''QVariant KFileMetaInfoItem.value()'''
        return QVariant()
    def isSkipped(self):
        '''bool KFileMetaInfoItem.isSkipped()'''
        return bool()
    def isModified(self):
        '''bool KFileMetaInfoItem.isModified()'''
        return bool()
    def isRemoved(self):
        '''bool KFileMetaInfoItem.isRemoved()'''
        return bool()
    def isEditable(self):
        '''bool KFileMetaInfoItem.isEditable()'''
        return bool()


class KFilePlacesModel(QAbstractItemModel):
    """"""
    # Enum KFilePlacesModel.AdditionalRoles
    UrlRole = 0
    HiddenRole = 0
    SetupNeededRole = 0
    FixedDeviceRole = 0
    CapacityBarRecommendedRole = 0

    def __init__(self, parent = None):
        '''void KFilePlacesModel.__init__(QObject parent = None)'''
    setupDone = pyqtSignal() # void setupDone(const QModelIndexamp;,bool) - signal
    errorMessage = pyqtSignal() # void errorMessage(const QStringamp;) - signal
    def dropMimeData(self, data, action, row, column, parent):
        '''bool KFilePlacesModel.dropMimeData(QMimeData data, Qt.DropAction action, int row, int column, QModelIndex parent)'''
        return bool()
    def mimeData(self, indexes):
        '''QMimeData KFilePlacesModel.mimeData(list-of-QModelIndex indexes)'''
        return QMimeData()
    def mimeTypes(self):
        '''QStringList KFilePlacesModel.mimeTypes()'''
        return QStringList()
    def flags(self, index):
        '''Qt.ItemFlags KFilePlacesModel.flags(QModelIndex index)'''
        return Qt.ItemFlags()
    def supportedDropActions(self):
        '''Qt.DropActions KFilePlacesModel.supportedDropActions()'''
        return Qt.DropActions()
    def closestItem(self, url):
        '''QModelIndex KFilePlacesModel.closestItem(KUrl url)'''
        return QModelIndex()
    def columnCount(self, parent = QModelIndex()):
        '''int KFilePlacesModel.columnCount(QModelIndex parent = QModelIndex())'''
        return int()
    def rowCount(self, parent = QModelIndex()):
        '''int KFilePlacesModel.rowCount(QModelIndex parent = QModelIndex())'''
        return int()
    def parent(self, child):
        '''QModelIndex KFilePlacesModel.parent(QModelIndex child)'''
        return QModelIndex()
    def index(self, row, column, parent = QModelIndex()):
        '''QModelIndex KFilePlacesModel.index(int row, int column, QModelIndex parent = QModelIndex())'''
        return QModelIndex()
    def data(self, index, role):
        '''QVariant KFilePlacesModel.data(QModelIndex index, int role)'''
        return QVariant()
    def hiddenCount(self):
        '''int KFilePlacesModel.hiddenCount()'''
        return int()
    def setPlaceHidden(self, index, hidden):
        '''void KFilePlacesModel.setPlaceHidden(QModelIndex index, bool hidden)'''
    def removePlace(self, index):
        '''void KFilePlacesModel.removePlace(QModelIndex index)'''
    def editPlace(self, index, text, url, iconName = QString(), appName = QString()):
        '''void KFilePlacesModel.editPlace(QModelIndex index, QString text, KUrl url, QString iconName = QString(), QString appName = QString())'''
    def addPlace(self, text, url, iconName = QString(), appName = QString()):
        '''void KFilePlacesModel.addPlace(QString text, KUrl url, QString iconName = QString(), QString appName = QString())'''
    def addPlace(self, text, url, iconName, appName, after):
        '''void KFilePlacesModel.addPlace(QString text, KUrl url, QString iconName, QString appName, QModelIndex after)'''
    def requestSetup(self, index):
        '''void KFilePlacesModel.requestSetup(QModelIndex index)'''
    def requestEject(self, index):
        '''void KFilePlacesModel.requestEject(QModelIndex index)'''
    def requestTeardown(self, index):
        '''void KFilePlacesModel.requestTeardown(QModelIndex index)'''
    def ejectActionForIndex(self, index):
        '''QAction KFilePlacesModel.ejectActionForIndex(QModelIndex index)'''
        return QAction()
    def teardownActionForIndex(self, index):
        '''QAction KFilePlacesModel.teardownActionForIndex(QModelIndex index)'''
        return QAction()
    def bookmarkForIndex(self, index):
        '''KBookmark KFilePlacesModel.bookmarkForIndex(QModelIndex index)'''
        return KBookmark()
    def deviceForIndex(self, index):
        '''Solid.Device KFilePlacesModel.deviceForIndex(QModelIndex index)'''
        return Solid.Device()
    def isDevice(self, index):
        '''bool KFilePlacesModel.isDevice(QModelIndex index)'''
        return bool()
    def isHidden(self, index):
        '''bool KFilePlacesModel.isHidden(QModelIndex index)'''
        return bool()
    def text(self, index):
        '''QString KFilePlacesModel.text(QModelIndex index)'''
        return QString()
    def icon(self, index):
        '''KIcon KFilePlacesModel.icon(QModelIndex index)'''
        return KIcon()
    def setupNeeded(self, index):
        '''bool KFilePlacesModel.setupNeeded(QModelIndex index)'''
        return bool()
    def url(self, index):
        '''KUrl KFilePlacesModel.url(QModelIndex index)'''
        return KUrl()


class KFilePlacesView(QListView):
    """"""
    def __init__(self, parent = None):
        '''void KFilePlacesView.__init__(QWidget parent = None)'''
    urlsDropped = pyqtSignal() # void urlsDropped(const KUrlamp;,QDropEvent *,QWidget *) - signal
    urlChanged = pyqtSignal() # void urlChanged(const KUrlamp;) - signal
    def dataChanged(self, topLeft, bottomRight):
        '''void KFilePlacesView.dataChanged(QModelIndex topLeft, QModelIndex bottomRight)'''
    def rowsInserted(self, parent, start, end):
        '''void KFilePlacesView.rowsInserted(QModelIndex parent, int start, int end)'''
    def paintEvent(self, event):
        '''void KFilePlacesView.paintEvent(QPaintEvent event)'''
    def dropEvent(self, event):
        '''void KFilePlacesView.dropEvent(QDropEvent event)'''
    def dragMoveEvent(self, event):
        '''void KFilePlacesView.dragMoveEvent(QDragMoveEvent event)'''
    def dragLeaveEvent(self, event):
        '''void KFilePlacesView.dragLeaveEvent(QDragLeaveEvent event)'''
    def dragEnterEvent(self, event):
        '''void KFilePlacesView.dragEnterEvent(QDragEnterEvent event)'''
    def hideEvent(self, event):
        '''void KFilePlacesView.hideEvent(QHideEvent event)'''
    def showEvent(self, event):
        '''void KFilePlacesView.showEvent(QShowEvent event)'''
    def resizeEvent(self, event):
        '''void KFilePlacesView.resizeEvent(QResizeEvent event)'''
    def contextMenuEvent(self, event):
        '''void KFilePlacesView.contextMenuEvent(QContextMenuEvent event)'''
    def keyPressEvent(self, event):
        '''void KFilePlacesView.keyPressEvent(QKeyEvent event)'''
    def setModel(self, model):
        '''void KFilePlacesView.setModel(QAbstractItemModel model)'''
    def sizeHint(self):
        '''QSize KFilePlacesView.sizeHint()'''
        return QSize()
    def setShowAll(self, showAll):
        '''void KFilePlacesView.setShowAll(bool showAll)'''
    def setUrl(self, url):
        '''void KFilePlacesView.setUrl(KUrl url)'''
    def isAutoResizeItemsEnabled(self):
        '''bool KFilePlacesView.isAutoResizeItemsEnabled()'''
        return bool()
    def setAutoResizeItemsEnabled(self, enabled):
        '''void KFilePlacesView.setAutoResizeItemsEnabled(bool enabled)'''
    def isDropOnPlaceEnabled(self):
        '''bool KFilePlacesView.isDropOnPlaceEnabled()'''
        return bool()
    def setDropOnPlaceEnabled(self, enabled):
        '''void KFilePlacesView.setDropOnPlaceEnabled(bool enabled)'''


class KFilePreviewGenerator(QObject):
    """"""
    def __init__(self, parent):
        '''void KFilePreviewGenerator.__init__(QAbstractItemView parent)'''
    def enabledPlugins(self):
        '''QStringList KFilePreviewGenerator.enabledPlugins()'''
        return QStringList()
    def setEnabledPlugins(self, list):
        '''void KFilePreviewGenerator.setEnabledPlugins(QStringList list)'''
    def cancelPreviews(self):
        '''void KFilePreviewGenerator.cancelPreviews()'''
    def updateIcons(self):
        '''void KFilePreviewGenerator.updateIcons()'''
    def updatePreviews(self):
        '''void KFilePreviewGenerator.updatePreviews()'''
    def isPreviewShown(self):
        '''bool KFilePreviewGenerator.isPreviewShown()'''
        return bool()
    def setPreviewShown(self, show):
        '''void KFilePreviewGenerator.setPreviewShown(bool show)'''


class KFileShare():
    """"""
    # Enum KFileShare.ShareMode
    Simple = 0
    Advanced = 0

    # Enum KFileShare.Authorization
    NotInitialized = 0
    ErrorNotFound = 0
    Authorized = 0
    UserNotAllowed = 0

    def nfsEnabled(self):
        '''static bool KFileShare.nfsEnabled()'''
        return bool()
    def sambaEnabled(self):
        '''static bool KFileShare.sambaEnabled()'''
        return bool()
    def shareMode(self):
        '''static KFileShare.ShareMode KFileShare.shareMode()'''
        return KFileShare.ShareMode()
    def fileShareGroup(self):
        '''static QString KFileShare.fileShareGroup()'''
        return QString()
    def isRestricted(self):
        '''static bool KFileShare.isRestricted()'''
        return bool()
    def sharingEnabled(self):
        '''static bool KFileShare.sharingEnabled()'''
        return bool()
    def setShared(self, path, shared):
        '''static bool KFileShare.setShared(QString path, bool shared)'''
        return bool()
    def authorization(self):
        '''static KFileShare.Authorization KFileShare.authorization()'''
        return KFileShare.Authorization()
    def isDirectoryShared(self, path):
        '''static bool KFileShare.isDirectoryShared(QString path)'''
        return bool()
    def readShareList(self):
        '''static void KFileShare.readShareList()'''
    def readConfig(self):
        '''static void KFileShare.readConfig()'''


class KPropertiesDialogPlugin(QObject):
    """"""
    def __init__(self, _props):
        '''void KPropertiesDialogPlugin.__init__(KPropertiesDialog _props)'''
    def fontHeight(self):
        '''int KPropertiesDialogPlugin.fontHeight()'''
        return int()
    changed = pyqtSignal() # void changed() - signal
    def isDirty(self):
        '''bool KPropertiesDialogPlugin.isDirty()'''
        return bool()
    def setDirty(self, b):
        '''void KPropertiesDialogPlugin.setDirty(bool b)'''
    def setDirty(self):
        '''void KPropertiesDialogPlugin.setDirty()'''
    def isDesktopFile(self, _item):
        '''static bool KPropertiesDialogPlugin.isDesktopFile(KFileItem _item)'''
        return bool()
    def applyChanges(self):
        '''void KPropertiesDialogPlugin.applyChanges()'''


class KFileSharePropsPlugin(KPropertiesDialogPlugin):
    """"""
    def __init__(self, _props):
        '''void KFileSharePropsPlugin.__init__(KPropertiesDialog _props)'''
    def slotConfigureFileSharingDone(self):
        '''void KFileSharePropsPlugin.slotConfigureFileSharingDone()'''
    def slotConfigureFileSharing(self):
        '''void KFileSharePropsPlugin.slotConfigureFileSharing()'''
    def page(self):
        '''QWidget KFileSharePropsPlugin.page()'''
        return QWidget()
    def supports(self, items):
        '''static bool KFileSharePropsPlugin.supports(KFileItemList items)'''
        return bool()
    def applyChanges(self):
        '''void KFileSharePropsPlugin.applyChanges()'''


class KFileWidget(QWidget, KAbstractFileWidget):
    """"""
    def __init__(self, startDir, parent):
        '''void KFileWidget.__init__(KUrl startDir, QWidget parent)'''
    def readConfig(self, group):
        '''void KFileWidget.readConfig(KConfigGroup group)'''
    def dirOperator(self):
        '''KDirOperator KFileWidget.dirOperator()'''
        return KDirOperator()
    accepted = pyqtSignal() # void accepted() - signal
    filterChanged = pyqtSignal() # void filterChanged(const QStringamp;) - signal
    selectionChanged = pyqtSignal() # void selectionChanged() - signal
    fileHighlighted = pyqtSignal() # void fileHighlighted(const QStringamp;) - signal
    fileHighlighted = pyqtSignal() # void fileHighlighted(const KUrlamp;) - signal
    fileSelected = pyqtSignal() # void fileSelected(const QStringamp;) - signal
    fileSelected = pyqtSignal() # void fileSelected(const KUrlamp;) - signal
    def eventFilter(self, watched, event):
        '''bool KFileWidget.eventFilter(QObject watched, QEvent event)'''
        return bool()
    def showEvent(self, event):
        '''void KFileWidget.showEvent(QShowEvent event)'''
    def resizeEvent(self, event):
        '''void KFileWidget.resizeEvent(QResizeEvent event)'''
    def slotCancel(self):
        '''void KFileWidget.slotCancel()'''
    def accept(self):
        '''void KFileWidget.accept()'''
    def slotOk(self):
        '''void KFileWidget.slotOk()'''
    def setCustomWidget(self, widget):
        '''void KFileWidget.setCustomWidget(QWidget widget)'''
    def setCustomWidget(self, text, widget):
        '''void KFileWidget.setCustomWidget(QString text, QWidget widget)'''
    def setStartDir(self, directory):
        '''static void KFileWidget.setStartDir(KUrl directory)'''
    def getStartUrl(self, startDir, recentDirClass):
        '''static KUrl KFileWidget.getStartUrl(KUrl startDir, QString recentDirClass)'''
        return KUrl()
    def getStartUrl(self, startDir, recentDirClass, fileName):
        '''static KUrl KFileWidget.getStartUrl(KUrl startDir, QString recentDirClass, QString fileName)'''
        return KUrl()
    def actionCollection(self):
        '''KActionCollection KFileWidget.actionCollection()'''
        return KActionCollection()
    def filterWidget(self):
        '''KFileFilterCombo KFileWidget.filterWidget()'''
        return KFileFilterCombo()
    def locationEdit(self):
        '''KUrlComboBox KFileWidget.locationEdit()'''
        return KUrlComboBox()
    def cancelButton(self):
        '''KPushButton KFileWidget.cancelButton()'''
        return KPushButton()
    def okButton(self):
        '''KPushButton KFileWidget.okButton()'''
        return KPushButton()
    def toolBar(self):
        '''KToolBar KFileWidget.toolBar()'''
        return KToolBar()
    def setLocationLabel(self, text):
        '''void KFileWidget.setLocationLabel(QString text)'''
    def mode(self):
        '''KFile.Modes KFileWidget.mode()'''
        return KFile.Modes()
    def setMode(self, m):
        '''void KFileWidget.setMode(KFile.Modes m)'''
    def setPreviewWidget(self, w):
        '''void KFileWidget.setPreviewWidget(KPreviewWidgetBase w)'''
    def clearFilter(self):
        '''void KFileWidget.clearFilter()'''
    def currentMimeFilter(self):
        '''QString KFileWidget.currentMimeFilter()'''
        return QString()
    def setMimeFilter(self, types, defaultType = QString()):
        '''void KFileWidget.setMimeFilter(QStringList types, QString defaultType = QString())'''
    def currentFilterMimeType(self):
        '''unknown-type KFileWidget.currentFilterMimeType()'''
        return unknown-type()
    def currentFilter(self):
        '''QString KFileWidget.currentFilter()'''
        return QString()
    def setFilter(self, filter):
        '''void KFileWidget.setFilter(QString filter)'''
    def keepsLocation(self):
        '''bool KFileWidget.keepsLocation()'''
        return bool()
    def setKeepLocation(self, keep):
        '''void KFileWidget.setKeepLocation(bool keep)'''
    def operationMode(self):
        '''KAbstractFileWidget.OperationMode KFileWidget.operationMode()'''
        return KAbstractFileWidget.OperationMode()
    def setOperationMode(self):
        '''KAbstractFileWidget.OperationMode KFileWidget.setOperationMode()'''
        return KAbstractFileWidget.OperationMode()
    def setSelection(self, name):
        '''void KFileWidget.setSelection(QString name)'''
    def setUrl(self, url, clearforward = True):
        '''void KFileWidget.setUrl(KUrl url, bool clearforward = True)'''
    def selectedFiles(self):
        '''QStringList KFileWidget.selectedFiles()'''
        return QStringList()
    def selectedFile(self):
        '''QString KFileWidget.selectedFile()'''
        return QString()
    def baseUrl(self):
        '''KUrl KFileWidget.baseUrl()'''
        return KUrl()
    def selectedUrls(self):
        '''KUrl.List KFileWidget.selectedUrls()'''
        return KUrl.List()
    def selectedUrl(self):
        '''KUrl KFileWidget.selectedUrl()'''
        return KUrl()


class KFileWritePlugin(QObject):
    """"""
    def __init__(self, parent, args):
        '''void KFileWritePlugin.__init__(QObject parent, QStringList args)'''
    def write(self, file, data):
        '''abstract bool KFileWritePlugin.write(KUrl file, dict-of-QString-QVariant data)'''
        return bool()
    def canWrite(self, file, key):
        '''abstract bool KFileWritePlugin.canWrite(KUrl file, QString key)'''
        return bool()


class KIconCanvas(KListWidget):
    """"""
    def __init__(self, parent = None):
        '''void KIconCanvas.__init__(QWidget parent = None)'''
    finished = pyqtSignal() # void finished() - signal
    progress = pyqtSignal() # void progress(int) - signal
    startLoading = pyqtSignal() # void startLoading(int) - signal
    nameChanged = pyqtSignal() # void nameChanged(const QStringamp;) - signal
    def stopLoading(self):
        '''void KIconCanvas.stopLoading()'''
    def getCurrent(self):
        '''QString KIconCanvas.getCurrent()'''
        return QString()
    def loadFiles(self, files):
        '''void KIconCanvas.loadFiles(QStringList files)'''


class KIconDialog(KDialog):
    """"""
    def __init__(self, parent = None):
        '''void KIconDialog.__init__(QWidget parent = None)'''
    def __init__(self, loader, parent = None):
        '''void KIconDialog.__init__(KIconLoader loader, QWidget parent = None)'''
    def slotOk(self):
        '''void KIconDialog.slotOk()'''
    newIconName = pyqtSignal() # void newIconName(const QStringamp;) - signal
    def getIcon(self, group = None, context = None, strictIconSize = False, iconSize = 0, user = False, parent = None, caption = QString()):
        '''static QString KIconDialog.getIcon(KIconLoader.Group group = KIconLoader.Desktop, KIconLoader.Context context = KIconLoader.Application, bool strictIconSize = False, int iconSize = 0, bool user = False, QWidget parent = None, QString caption = QString())'''
        return QString()
    def showDialog(self):
        '''void KIconDialog.showDialog()'''
    def openDialog(self):
        '''QString KIconDialog.openDialog()'''
        return QString()
    def setup(self, group, context = None, strictIconSize = False, iconSize = 0, user = False, lockUser = False, lockCustomDir = False):
        '''void KIconDialog.setup(KIconLoader.Group group, KIconLoader.Context context = KIconLoader.Application, bool strictIconSize = False, int iconSize = 0, bool user = False, bool lockUser = False, bool lockCustomDir = False)'''
    def iconSize(self):
        '''int KIconDialog.iconSize()'''
        return int()
    def setIconSize(self, size):
        '''void KIconDialog.setIconSize(int size)'''
    def setCustomLocation(self, location):
        '''void KIconDialog.setCustomLocation(QString location)'''
    def strictIconSize(self):
        '''bool KIconDialog.strictIconSize()'''
        return bool()
    def setStrictIconSize(self, b):
        '''void KIconDialog.setStrictIconSize(bool b)'''


class KIconButton(QPushButton):
    """"""
    def __init__(self, parent = None):
        '''void KIconButton.__init__(QWidget parent = None)'''
    def __init__(self, loader, parent):
        '''void KIconButton.__init__(KIconLoader loader, QWidget parent)'''
    iconChanged = pyqtSignal() # void iconChanged(const QStringamp;) - signal
    def buttonIconSize(self):
        '''int KIconButton.buttonIconSize()'''
        return int()
    def setButtonIconSize(self, size):
        '''void KIconButton.setButtonIconSize(int size)'''
    def iconSize(self):
        '''int KIconButton.iconSize()'''
        return int()
    def setIconSize(self, size):
        '''void KIconButton.setIconSize(int size)'''
    def icon(self):
        '''QString KIconButton.icon()'''
        return QString()
    def resetIcon(self):
        '''void KIconButton.resetIcon()'''
    def setIcon(self, icon):
        '''void KIconButton.setIcon(QString icon)'''
    def setIcon(self, icon):
        '''void KIconButton.setIcon(QIcon icon)'''
    def setIconType(self, group, context, user = False):
        '''void KIconButton.setIconType(KIconLoader.Group group, KIconLoader.Context context, bool user = False)'''
    def strictIconSize(self):
        '''bool KIconButton.strictIconSize()'''
        return bool()
    def setStrictIconSize(self, b):
        '''void KIconButton.setStrictIconSize(bool b)'''


class KPreviewWidgetBase(QWidget):
    """"""
    def __init__(self, parent):
        '''void KPreviewWidgetBase.__init__(QWidget parent)'''
    def setSupportedMimeTypes(self, mimeTypes):
        '''void KPreviewWidgetBase.setSupportedMimeTypes(QStringList mimeTypes)'''
    def supportedMimeTypes(self):
        '''QStringList KPreviewWidgetBase.supportedMimeTypes()'''
        return QStringList()
    def clearPreview(self):
        '''abstract void KPreviewWidgetBase.clearPreview()'''
    def showPreview(self, url):
        '''abstract void KPreviewWidgetBase.showPreview(KUrl url)'''


class KImageFilePreview(KPreviewWidgetBase):
    """"""
    def __init__(self, parent = None):
        '''void KImageFilePreview.__init__(QWidget parent = None)'''
    def createJob(self, url, width, height):
        '''KIO.PreviewJob KImageFilePreview.createJob(KUrl url, int width, int height)'''
        return KIO.PreviewJob()
    def resizeEvent(self, event):
        '''void KImageFilePreview.resizeEvent(QResizeEvent event)'''
    def gotPreview(self):
        '''QPixmap KImageFilePreview.gotPreview()'''
        return QPixmap()
    def clearPreview(self):
        '''void KImageFilePreview.clearPreview()'''
    def showPreview(self, url):
        '''void KImageFilePreview.showPreview(KUrl url)'''
    def showPreview(self):
        '''void KImageFilePreview.showPreview()'''
    def showPreview(self, url, force):
        '''void KImageFilePreview.showPreview(KUrl url, bool force)'''
    def sizeHint(self):
        '''QSize KImageFilePreview.sizeHint()'''
        return QSize()


class KImageIO():
    """"""
    # Enum KImageIO.Mode
    Reading = 0
    Writing = 0

    def isSupported(self, mimeType, mode = None):
        '''static bool KImageIO.isSupported(QString mimeType, KImageIO.Mode mode = KImageIO.Writing)'''
        return bool()
    def mimeTypes(self, mode = None):
        '''static QStringList KImageIO.mimeTypes(KImageIO.Mode mode = KImageIO.Writing)'''
        return QStringList()
    def types(self, mode = None):
        '''static QStringList KImageIO.types(KImageIO.Mode mode = KImageIO.Writing)'''
        return QStringList()
    def typeForMime(self, mimeType):
        '''static QStringList KImageIO.typeForMime(QString mimeType)'''
        return QStringList()
    def pattern(self, mode = None):
        '''static QString KImageIO.pattern(KImageIO.Mode mode = KImageIO.Reading)'''
        return QString()


class ThumbCreator():
    """"""
    # Enum ThumbCreator.Flags
    __kdevpythondocumentation_builtin_None = 0
    DrawFrame = 0
    BlendIcon = 0

    def __init__(self):
        '''void ThumbCreator.__init__()'''
    def __init__(self):
        '''ThumbCreator ThumbCreator.__init__()'''
        return ThumbCreator()
    def flags(self):
        '''ThumbCreator.Flags ThumbCreator.flags()'''
        return ThumbCreator.Flags()
    def create(self, path, width, height, img):
        '''abstract bool ThumbCreator.create(QString path, int width, int height, QImage img)'''
        return bool()


class ThumbSequenceCreator(ThumbCreator):
    """"""
    def __init__(self):
        '''void ThumbSequenceCreator.__init__()'''
    def setSequenceIndex(self, index):
        '''void ThumbSequenceCreator.setSequenceIndex(float index)'''
    def sequenceIndex(self):
        '''float ThumbSequenceCreator.sequenceIndex()'''
        return float()


class KMimeTypeChooser(KVBox):
    """"""
    # Enum KMimeTypeChooser.Visuals
    Comments = 0
    Patterns = 0
    EditButton = 0

    def __init__(self, text = QString(), selectedMimeTypes = QStringList(), defaultGroup = QString(), groupsToShow = QStringList(), visuals = None, parent = None):
        '''void KMimeTypeChooser.__init__(QString text = QString(), QStringList selectedMimeTypes = QStringList(), QString defaultGroup = QString(), QStringList groupsToShow = QStringList(), int visuals = KMimeTypeChooser.Comments|KMimeTypeChooser.Patterns|KMimeTypeChooser.EditButton, QWidget parent = None)'''
    def patterns(self):
        '''QStringList KMimeTypeChooser.patterns()'''
        return QStringList()
    def mimeTypes(self):
        '''QStringList KMimeTypeChooser.mimeTypes()'''
        return QStringList()


class KMimeTypeChooserDialog(KDialog):
    """"""
    def __init__(self, caption = QString(), text = QString(), selectedMimeTypes = QStringList(), defaultGroup = QString(), groupsToShow = QStringList(), visuals = None, parent = None):
        '''void KMimeTypeChooserDialog.__init__(QString caption = QString(), QString text = QString(), QStringList selectedMimeTypes = QStringList(), QString defaultGroup = QString(), QStringList groupsToShow = QStringList(), int visuals = KMimeTypeChooser.Comments|KMimeTypeChooser.Patterns|KMimeTypeChooser.EditButton, QWidget parent = None)'''
    def __init__(self, caption, text, selectedMimeTypes, defaultGroup, parent = None):
        '''void KMimeTypeChooserDialog.__init__(QString caption, QString text, QStringList selectedMimeTypes, QString defaultGroup, QWidget parent = None)'''
    def chooser(self):
        '''KMimeTypeChooser KMimeTypeChooserDialog.chooser()'''
        return KMimeTypeChooser()


class KMountPoint():
    """"""
    # Enum KMountPoint.FileSystemFlag
    SupportsChmod = 0
    SupportsChown = 0
    SupportsUTime = 0
    SupportsSymlinks = 0
    CaseInsensitive = 0

    # Enum KMountPoint.DetailsNeededFlag
    BasicInfoNeeded = 0
    NeedMountOptions = 0
    NeedRealDeviceName = 0

    def testFileSystemFlag(self, flag):
        '''bool KMountPoint.testFileSystemFlag(KMountPoint.FileSystemFlag flag)'''
        return bool()
    def probablySlow(self):
        '''bool KMountPoint.probablySlow()'''
        return bool()
    def mountOptions(self):
        '''QStringList KMountPoint.mountOptions()'''
        return QStringList()
    def mountType(self):
        '''QString KMountPoint.mountType()'''
        return QString()
    def mountPoint(self):
        '''QString KMountPoint.mountPoint()'''
        return QString()
    def realDeviceName(self):
        '''QString KMountPoint.realDeviceName()'''
        return QString()
    def mountedFrom(self):
        '''QString KMountPoint.mountedFrom()'''
        return QString()
    def currentMountPoints(self, infoNeeded = None):
        '''static KMountPoint.List KMountPoint.currentMountPoints(KMountPoint.DetailsNeededFlags infoNeeded = KMountPoint.BasicInfoNeeded)'''
        return KMountPoint.List()
    def possibleMountPoints(self, infoNeeded = None):
        '''static KMountPoint.List KMountPoint.possibleMountPoints(KMountPoint.DetailsNeededFlags infoNeeded = KMountPoint.BasicInfoNeeded)'''
        return KMountPoint.List()
    class DetailsNeededFlags():
        """"""
        def __init__(self):
            '''KMountPoint.DetailsNeededFlags KMountPoint.DetailsNeededFlags.__init__()'''
            return KMountPoint.DetailsNeededFlags()
        def __init__(self):
            '''int KMountPoint.DetailsNeededFlags.__init__()'''
            return int()
        def __init__(self):
            '''void KMountPoint.DetailsNeededFlags.__init__()'''
        def __bool__(self):
            '''int KMountPoint.DetailsNeededFlags.__bool__()'''
            return int()
        def __ne__(self, f):
            '''bool KMountPoint.DetailsNeededFlags.__ne__(KMountPoint.DetailsNeededFlags f)'''
            return bool()
        def __eq__(self, f):
            '''bool KMountPoint.DetailsNeededFlags.__eq__(KMountPoint.DetailsNeededFlags f)'''
            return bool()
        def __invert__(self):
            '''KMountPoint.DetailsNeededFlags KMountPoint.DetailsNeededFlags.__invert__()'''
            return KMountPoint.DetailsNeededFlags()
        def __and__(self, mask):
            '''KMountPoint.DetailsNeededFlags KMountPoint.DetailsNeededFlags.__and__(int mask)'''
            return KMountPoint.DetailsNeededFlags()
        def __xor__(self, f):
            '''KMountPoint.DetailsNeededFlags KMountPoint.DetailsNeededFlags.__xor__(KMountPoint.DetailsNeededFlags f)'''
            return KMountPoint.DetailsNeededFlags()
        def __xor__(self, f):
            '''KMountPoint.DetailsNeededFlags KMountPoint.DetailsNeededFlags.__xor__(int f)'''
            return KMountPoint.DetailsNeededFlags()
        def __or__(self, f):
            '''KMountPoint.DetailsNeededFlags KMountPoint.DetailsNeededFlags.__or__(KMountPoint.DetailsNeededFlags f)'''
            return KMountPoint.DetailsNeededFlags()
        def __or__(self, f):
            '''KMountPoint.DetailsNeededFlags KMountPoint.DetailsNeededFlags.__or__(int f)'''
            return KMountPoint.DetailsNeededFlags()
        def __int__(self):
            '''int KMountPoint.DetailsNeededFlags.__int__()'''
            return int()
        def __ixor__(self, f):
            '''KMountPoint.DetailsNeededFlags KMountPoint.DetailsNeededFlags.__ixor__(KMountPoint.DetailsNeededFlags f)'''
            return KMountPoint.DetailsNeededFlags()
        def __ior__(self, f):
            '''KMountPoint.DetailsNeededFlags KMountPoint.DetailsNeededFlags.__ior__(KMountPoint.DetailsNeededFlags f)'''
            return KMountPoint.DetailsNeededFlags()
        def __iand__(self, mask):
            '''KMountPoint.DetailsNeededFlags KMountPoint.DetailsNeededFlags.__iand__(int mask)'''
            return KMountPoint.DetailsNeededFlags()
    class List():
        """"""
        def __init__(self):
            '''void KMountPoint.List.__init__()'''
        def __init__(self):
            '''KMountPoint.List KMountPoint.List.__init__()'''
            return KMountPoint.List()
        def findByDevice(self, device):
            '''unknown-type KMountPoint.List.findByDevice(QString device)'''
            return unknown-type()
        def findByPath(self, path):
            '''unknown-type KMountPoint.List.findByPath(QString path)'''
            return unknown-type()


class KNameAndUrlInputDialog(KDialog):
    """"""
    def __init__(self, nameLabel, urlLabel, startDir, parent):
        '''void KNameAndUrlInputDialog.__init__(QString nameLabel, QString urlLabel, KUrl startDir, QWidget parent)'''
    def url(self):
        '''KUrl KNameAndUrlInputDialog.url()'''
        return KUrl()
    def name(self):
        '''QString KNameAndUrlInputDialog.name()'''
        return QString()
    def setSuggestedUrl(self, url):
        '''void KNameAndUrlInputDialog.setSuggestedUrl(KUrl url)'''
    def setSuggestedName(self, name):
        '''void KNameAndUrlInputDialog.setSuggestedName(QString name)'''


class KNewFileMenu(KActionMenu):
    """"""
    def __init__(self, collection, name, parent):
        '''void KNewFileMenu.__init__(KActionCollection collection, QString name, QObject parent)'''
    def setModal(self, modality):
        '''void KNewFileMenu.setModal(bool modality)'''
    def isModal(self):
        '''bool KNewFileMenu.isModal()'''
        return bool()
    def slotResult(self, job):
        '''void KNewFileMenu.slotResult(KJob job)'''
    directoryCreated = pyqtSignal() # void directoryCreated(const KUrlamp;) - signal
    fileCreated = pyqtSignal() # void fileCreated(const KUrlamp;) - signal
    def createDirectory(self):
        '''void KNewFileMenu.createDirectory()'''
    def checkUpToDate(self):
        '''void KNewFileMenu.checkUpToDate()'''
    def popupFiles(self):
        '''KUrl.List KNewFileMenu.popupFiles()'''
        return KUrl.List()
    def setPopupFiles(self, files):
        '''void KNewFileMenu.setPopupFiles(KUrl.List files)'''
    def setViewShowsHiddenFiles(self, b):
        '''void KNewFileMenu.setViewShowsHiddenFiles(bool b)'''
    def supportedMimeTypes(self):
        '''QStringList KNewFileMenu.supportedMimeTypes()'''
        return QStringList()
    def setSupportedMimeTypes(self, mime):
        '''void KNewFileMenu.setSupportedMimeTypes(QStringList mime)'''
    def setParentWidget(self, parentWidget):
        '''void KNewFileMenu.setParentWidget(QWidget parentWidget)'''


class KNFSShare(QObject):
    """"""
    changed = pyqtSignal() # void changed() - signal
    def exportsPath(self):
        '''QString KNFSShare.exportsPath()'''
        return QString()
    def sharedDirectories(self):
        '''QStringList KNFSShare.sharedDirectories()'''
        return QStringList()
    def isDirectoryShared(self, path):
        '''bool KNFSShare.isDirectoryShared(QString path)'''
        return bool()
    def instance(self):
        '''static KNFSShare KNFSShare.instance()'''
        return KNFSShare()


class KonqBookmarkOwner(KBookmarkOwner):
    """"""
    def __init__(self):
        '''void KonqBookmarkOwner.__init__()'''
    def __init__(self):
        '''KonqBookmarkOwner KonqBookmarkOwner.__init__()'''
        return KonqBookmarkOwner()
    def openInNewWindow(self, bm):
        '''abstract void KonqBookmarkOwner.openInNewWindow(KBookmark bm)'''
    def openInNewTab(self, bm):
        '''abstract void KonqBookmarkOwner.openInNewTab(KBookmark bm)'''


class KonqBookmarkMenu(KBookmarkMenu):
    """"""
    def __init__(self, mgr, owner, parentMenu, collec):
        '''void KonqBookmarkMenu.__init__(KBookmarkManager mgr, KonqBookmarkOwner owner, KBookmarkActionMenu parentMenu, KActionCollection collec)'''
    def __init__(self, mgr, owner, parentMenu, parentAddress):
        '''void KonqBookmarkMenu.__init__(KBookmarkManager mgr, KonqBookmarkOwner owner, KBookmarkActionMenu parentMenu, QString parentAddress)'''
    def fillDynamicBookmarks(self):
        '''void KonqBookmarkMenu.fillDynamicBookmarks()'''
    def contextMenu(self, act):
        '''KMenu KonqBookmarkMenu.contextMenu(QAction act)'''
        return KMenu()
    def actionForBookmark(self, bm):
        '''QAction KonqBookmarkMenu.actionForBookmark(KBookmark bm)'''
        return QAction()
    def refill(self):
        '''void KonqBookmarkMenu.refill()'''
    def dynamicBookmarksList(self):
        '''static QStringList KonqBookmarkMenu.dynamicBookmarksList()'''
        return QStringList()


class KonqBookmarkContextMenu(KBookmarkContextMenu):
    """"""
    def __init__(self, bm, mgr, owner):
        '''void KonqBookmarkContextMenu.__init__(KBookmark bm, KBookmarkManager mgr, KonqBookmarkOwner owner)'''
    def toggleShowInToolbar(self):
        '''void KonqBookmarkContextMenu.toggleShowInToolbar()'''
    def openInNewWindow(self):
        '''void KonqBookmarkContextMenu.openInNewWindow()'''
    def openInNewTab(self):
        '''void KonqBookmarkContextMenu.openInNewTab()'''
    def addActions(self):
        '''void KonqBookmarkContextMenu.addActions()'''


class KOpenWithDialog(KDialog):
    """"""
    def __init__(self, urls, parent = None):
        '''void KOpenWithDialog.__init__(KUrl.List urls, QWidget parent = None)'''
    def __init__(self, urls, text, value, parent = None):
        '''void KOpenWithDialog.__init__(KUrl.List urls, QString text, QString value, QWidget parent = None)'''
    def __init__(self, mimeType, value, parent = None):
        '''void KOpenWithDialog.__init__(QString mimeType, QString value, QWidget parent = None)'''
    def __init__(self, parent = None):
        '''void KOpenWithDialog.__init__(QWidget parent = None)'''
    def accept(self):
        '''void KOpenWithDialog.accept()'''
    def slotTerminalToggled(self):
        '''bool KOpenWithDialog.slotTerminalToggled()'''
        return bool()
    def slotTextChanged(self):
        '''void KOpenWithDialog.slotTextChanged()'''
    def slotHighlighted(self, _name, _exec):
        '''void KOpenWithDialog.slotHighlighted(QString _name, QString _exec)'''
    def slotSelected(self, _name, _exec):
        '''void KOpenWithDialog.slotSelected(QString _name, QString _exec)'''
    def setSaveNewApplications(self, b):
        '''void KOpenWithDialog.setSaveNewApplications(bool b)'''
    def service(self):
        '''unknown-type KOpenWithDialog.service()'''
        return unknown-type()
    def hideRunInTerminal(self):
        '''void KOpenWithDialog.hideRunInTerminal()'''
    def hideNoCloseOnExit(self):
        '''void KOpenWithDialog.hideNoCloseOnExit()'''
    def text(self):
        '''QString KOpenWithDialog.text()'''
        return QString()


class KPropertiesDialog(KPageDialog):
    """"""
    def __init__(self, item, parent = None):
        '''void KPropertiesDialog.__init__(KFileItem item, QWidget parent = None)'''
    def __init__(self, _items, parent = None):
        '''void KPropertiesDialog.__init__(KFileItemList _items, QWidget parent = None)'''
    def __init__(self, _url, parent = None):
        '''void KPropertiesDialog.__init__(KUrl _url, QWidget parent = None)'''
    def __init__(self, _tempUrl, _currentDir, _defaultName, parent = None):
        '''void KPropertiesDialog.__init__(KUrl _tempUrl, KUrl _currentDir, QString _defaultName, QWidget parent = None)'''
    def __init__(self, title, parent = None):
        '''void KPropertiesDialog.__init__(QString title, QWidget parent = None)'''
    leaveModality = pyqtSignal() # void leaveModality() - signal
    saveAs = pyqtSignal() # void saveAs(const KUrlamp;,KUrlamp;) - signal
    canceled = pyqtSignal() # void canceled() - signal
    applied = pyqtSignal() # void applied() - signal
    propertiesClosed = pyqtSignal() # void propertiesClosed() - signal
    def slotCancel(self):
        '''void KPropertiesDialog.slotCancel()'''
    def slotOk(self):
        '''void KPropertiesDialog.slotOk()'''
    def setFileNameReadOnly(self, ro):
        '''void KPropertiesDialog.setFileNameReadOnly(bool ro)'''
    def setFileSharingPage(self, page):
        '''void KPropertiesDialog.setFileSharingPage(QWidget page)'''
    def showFileSharingPage(self):
        '''void KPropertiesDialog.showFileSharingPage()'''
    def abortApplying(self):
        '''void KPropertiesDialog.abortApplying()'''
    def rename(self, _name):
        '''void KPropertiesDialog.rename(QString _name)'''
    def updateUrl(self, _newUrl):
        '''void KPropertiesDialog.updateUrl(KUrl _newUrl)'''
    def defaultName(self):
        '''QString KPropertiesDialog.defaultName()'''
        return QString()
    def currentDir(self):
        '''KUrl KPropertiesDialog.currentDir()'''
        return KUrl()
    def items(self):
        '''KFileItemList KPropertiesDialog.items()'''
        return KFileItemList()
    def item(self):
        '''KFileItem KPropertiesDialog.item()'''
        return KFileItem()
    def kurl(self):
        '''KUrl KPropertiesDialog.kurl()'''
        return KUrl()
    def insertPlugin(self, plugin):
        '''void KPropertiesDialog.insertPlugin(KPropertiesDialogPlugin plugin)'''
    def showDialog(self, item, parent = None, modal = True):
        '''static bool KPropertiesDialog.showDialog(KFileItem item, QWidget parent = None, bool modal = True)'''
        return bool()
    def showDialog(self, _url, parent = None, modal = True):
        '''static bool KPropertiesDialog.showDialog(KUrl _url, QWidget parent = None, bool modal = True)'''
        return bool()
    def showDialog(self, _items, parent = None, modal = True):
        '''static bool KPropertiesDialog.showDialog(KFileItemList _items, QWidget parent = None, bool modal = True)'''
        return bool()
    def canDisplay(self, _items):
        '''static bool KPropertiesDialog.canDisplay(KFileItemList _items)'''
        return bool()


class KProtocolManager():
    """"""
    # Enum KProtocolManager.ProxyAuthMode
    Prompt = 0
    Automatic = 0

    # Enum KProtocolManager.ProxyType
    NoProxy = 0
    ManualProxy = 0
    PACProxy = 0
    WPADProxy = 0
    EnvVarProxy = 0

    def __init__(self):
        '''void KProtocolManager.__init__()'''
    def __init__(self):
        '''KProtocolManager KProtocolManager.__init__()'''
        return KProtocolManager()
    def proxiesForUrl(self, url):
        '''static QStringList KProtocolManager.proxiesForUrl(KUrl url)'''
        return QStringList()
    def acceptLanguagesHeader(self):
        '''static QString KProtocolManager.acceptLanguagesHeader()'''
        return QString()
    def slaveProtocol(self, url, proxy):
        '''static QString KProtocolManager.slaveProtocol(KUrl url, QString proxy)'''
        return QString()
    def slaveProtocol(self, url, proxy):
        '''static QString KProtocolManager.slaveProtocol(KUrl url, QStringList proxy)'''
        return QString()
    def reparseConfiguration(self):
        '''static void KProtocolManager.reparseConfiguration()'''
    def protocolForArchiveMimetype(self, mimeType):
        '''static QString KProtocolManager.protocolForArchiveMimetype(QString mimeType)'''
        return QString()
    def isSourceProtocol(self, url):
        '''static bool KProtocolManager.isSourceProtocol(KUrl url)'''
        return bool()
    def listing(self, url):
        '''static QStringList KProtocolManager.listing(KUrl url)'''
        return QStringList()
    def outputType(self, url):
        '''static KProtocolInfo.Type KProtocolManager.outputType(KUrl url)'''
        return KProtocolInfo.Type()
    def inputType(self, url):
        '''static KProtocolInfo.Type KProtocolManager.inputType(KUrl url)'''
        return KProtocolInfo.Type()
    def defaultMimetype(self, url):
        '''static QString KProtocolManager.defaultMimetype(KUrl url)'''
        return QString()
    def fileNameUsedForCopying(self, url):
        '''static KProtocolInfo.FileNameUsedForCopying KProtocolManager.fileNameUsedForCopying(KUrl url)'''
        return KProtocolInfo.FileNameUsedForCopying()
    def canDeleteRecursive(self, url):
        '''static bool KProtocolManager.canDeleteRecursive(KUrl url)'''
        return bool()
    def canRenameToFile(self, url):
        '''static bool KProtocolManager.canRenameToFile(KUrl url)'''
        return bool()
    def canRenameFromFile(self, url):
        '''static bool KProtocolManager.canRenameFromFile(KUrl url)'''
        return bool()
    def canCopyToFile(self, url):
        '''static bool KProtocolManager.canCopyToFile(KUrl url)'''
        return bool()
    def canCopyFromFile(self, url):
        '''static bool KProtocolManager.canCopyFromFile(KUrl url)'''
        return bool()
    def supportsOpening(self, url):
        '''static bool KProtocolManager.supportsOpening(KUrl url)'''
        return bool()
    def supportsMoving(self, url):
        '''static bool KProtocolManager.supportsMoving(KUrl url)'''
        return bool()
    def supportsLinking(self, url):
        '''static bool KProtocolManager.supportsLinking(KUrl url)'''
        return bool()
    def supportsDeleting(self, url):
        '''static bool KProtocolManager.supportsDeleting(KUrl url)'''
        return bool()
    def supportsMakeDir(self, url):
        '''static bool KProtocolManager.supportsMakeDir(KUrl url)'''
        return bool()
    def supportsWriting(self, url):
        '''static bool KProtocolManager.supportsWriting(KUrl url)'''
        return bool()
    def supportsReading(self, url):
        '''static bool KProtocolManager.supportsReading(KUrl url)'''
        return bool()
    def supportsListing(self, url):
        '''static bool KProtocolManager.supportsListing(KUrl url)'''
        return bool()
    def persistentConnections(self):
        '''static bool KProtocolManager.persistentConnections()'''
        return bool()
    def persistentProxyConnection(self):
        '''static bool KProtocolManager.persistentProxyConnection()'''
        return bool()
    def minimumKeepSize(self):
        '''static int KProtocolManager.minimumKeepSize()'''
        return int()
    def markPartial(self):
        '''static bool KProtocolManager.markPartial()'''
        return bool()
    def autoResume(self):
        '''static bool KProtocolManager.autoResume()'''
        return bool()
    def cacheControl(self):
        '''static KIO.CacheControl KProtocolManager.cacheControl()'''
        return KIO.CacheControl()
    def cacheDir(self):
        '''static QString KProtocolManager.cacheDir()'''
        return QString()
    def maxCacheSize(self):
        '''static int KProtocolManager.maxCacheSize()'''
        return int()
    def maxCacheAge(self):
        '''static int KProtocolManager.maxCacheAge()'''
        return int()
    def useCache(self):
        '''static bool KProtocolManager.useCache()'''
        return bool()
    def proxyConfigScript(self):
        '''static QString KProtocolManager.proxyConfigScript()'''
        return QString()
    def badProxy(self, proxy):
        '''static void KProtocolManager.badProxy(QString proxy)'''
    def proxyForUrl(self, url):
        '''static QString KProtocolManager.proxyForUrl(KUrl url)'''
        return QString()
    def proxyFor(self, protocol):
        '''static QString KProtocolManager.proxyFor(QString protocol)'''
        return QString()
    def noProxyFor(self):
        '''static QString KProtocolManager.noProxyFor()'''
        return QString()
    def proxyAuthMode(self):
        '''static KProtocolManager.ProxyAuthMode KProtocolManager.proxyAuthMode()'''
        return KProtocolManager.ProxyAuthMode()
    def proxyType(self):
        '''static KProtocolManager.ProxyType KProtocolManager.proxyType()'''
        return KProtocolManager.ProxyType()
    def useReverseProxy(self):
        '''static bool KProtocolManager.useReverseProxy()'''
        return bool()
    def useProxy(self):
        '''static bool KProtocolManager.useProxy()'''
        return bool()
    def responseTimeout(self):
        '''static int KProtocolManager.responseTimeout()'''
        return int()
    def proxyConnectTimeout(self):
        '''static int KProtocolManager.proxyConnectTimeout()'''
        return int()
    def connectTimeout(self):
        '''static int KProtocolManager.connectTimeout()'''
        return int()
    def readTimeout(self):
        '''static int KProtocolManager.readTimeout()'''
        return int()
    def getSystemNameVersionAndMachine(self, systemName, systemVersion, machine):
        '''static bool KProtocolManager.getSystemNameVersionAndMachine(QString systemName, QString systemVersion, QString machine)'''
        return bool()
    def userAgentForHost(self, hostname):
        '''static QString KProtocolManager.userAgentForHost(QString hostname)'''
        return QString()
    def userAgentForApplication(self, appName, appVersion, extraInfo = QStringList()):
        '''static QString KProtocolManager.userAgentForApplication(QString appName, QString appVersion, QStringList extraInfo = QStringList())'''
        return QString()
    def defaultUserAgent(self):
        '''static QString KProtocolManager.defaultUserAgent()'''
        return QString()
    def defaultUserAgent(self, keys):
        '''static QString KProtocolManager.defaultUserAgent(QString keys)'''
        return QString()


class KRecentDirs():
    """"""
    def add(self, fileClass, directory):
        '''static void KRecentDirs.add(QString fileClass, QString directory)'''
    def dir(self, fileClass):
        '''static QString KRecentDirs.dir(QString fileClass)'''
        return QString()
    def list(self, fileClass):
        '''static QStringList KRecentDirs.list(QString fileClass)'''
        return QStringList()


class KRecentDocument():
    """"""
    def __init__(self):
        '''void KRecentDocument.__init__()'''
    def __init__(self):
        '''KRecentDocument KRecentDocument.__init__()'''
        return KRecentDocument()
    def recentDocumentDirectory(self):
        '''static QString KRecentDocument.recentDocumentDirectory()'''
        return QString()
    def maximumItems(self):
        '''static int KRecentDocument.maximumItems()'''
        return int()
    def clear(self):
        '''static void KRecentDocument.clear()'''
    def add(self, url):
        '''static void KRecentDocument.add(KUrl url)'''
    def add(self, url, desktopEntryName):
        '''static void KRecentDocument.add(KUrl url, QString desktopEntryName)'''
    def add(self, documentStr, isURL = False):
        '''static void KRecentDocument.add(QString documentStr, bool isURL = False)'''
    def recentDocuments(self):
        '''static QStringList KRecentDocument.recentDocuments()'''
        return QStringList()


class KRemoteEncoding():
    """"""
    def __init__(self, name = None):
        '''void KRemoteEncoding.__init__(str name = None)'''
    def setEncoding(self, name):
        '''void KRemoteEncoding.setEncoding(str name)'''
    def encodingMib(self):
        '''int KRemoteEncoding.encodingMib()'''
        return int()
    def encoding(self):
        '''str KRemoteEncoding.encoding()'''
        return str()
    def fileName(self, url):
        '''QByteArray KRemoteEncoding.fileName(KUrl url)'''
        return QByteArray()
    def directory(self, url, ignore_trailing_slash = True):
        '''QByteArray KRemoteEncoding.directory(KUrl url, bool ignore_trailing_slash = True)'''
        return QByteArray()
    def encode(self, name):
        '''QByteArray KRemoteEncoding.encode(QString name)'''
        return QByteArray()
    def encode(self, url):
        '''QByteArray KRemoteEncoding.encode(KUrl url)'''
        return QByteArray()
    def decode(self, name):
        '''QString KRemoteEncoding.decode(QByteArray name)'''
        return QString()


class KRun(QObject):
    """"""
    def __init__(self, url, window, mode = 0, isLocalFile = False, showProgressInfo = True, asn = QByteArray()):
        '''void KRun.__init__(KUrl url, QWidget window, int mode = 0, bool isLocalFile = False, bool showProgressInfo = True, QByteArray asn = QByteArray())'''
    def mode(self):
        '''int KRun.mode()'''
        return int()
    def setMode(self, mode):
        '''void KRun.setMode(int mode)'''
    def isLocalFile(self):
        '''bool KRun.isLocalFile()'''
        return bool()
    def setIsLocalFile(self, isLocalFile):
        '''void KRun.setIsLocalFile(bool isLocalFile)'''
    def initializeNextAction(self):
        '''bool KRun.initializeNextAction()'''
        return bool()
    def setInitializeNextAction(self, initialize):
        '''void KRun.setInitializeNextAction(bool initialize)'''
    def isDirectory(self):
        '''bool KRun.isDirectory()'''
        return bool()
    def setIsDirecory(self, isDirectory):
        '''void KRun.setIsDirecory(bool isDirectory)'''
    def doScanFile(self):
        '''bool KRun.doScanFile()'''
        return bool()
    def setDoScanFile(self, scanFile):
        '''void KRun.setDoScanFile(bool scanFile)'''
    def timer(self):
        '''QTimer KRun.timer()'''
        return QTimer()
    def job(self):
        '''KIO.Job KRun.job()'''
        return KIO.Job()
    def setJob(self, job):
        '''void KRun.setJob(KIO.Job job)'''
    def setFinished(self, finished):
        '''void KRun.setFinished(bool finished)'''
    def progressInfo(self):
        '''bool KRun.progressInfo()'''
        return bool()
    def setProgressInfo(self, progressInfo):
        '''void KRun.setProgressInfo(bool progressInfo)'''
    def setError(self, error):
        '''void KRun.setError(bool error)'''
    def url(self):
        '''KUrl KRun.url()'''
        return KUrl()
    def setUrl(self, url):
        '''void KRun.setUrl(KUrl url)'''
    def killJob(self):
        '''void KRun.killJob()'''
    def foundMimeType(self, type):
        '''void KRun.foundMimeType(QString type)'''
    def scanFile(self):
        '''void KRun.scanFile()'''
    def init(self):
        '''void KRun.init()'''
    def slotStatResult(self):
        '''KJob KRun.slotStatResult()'''
        return KJob()
    def mimeTypeDetermined(self, mimeType):
        '''void KRun.mimeTypeDetermined(QString mimeType)'''
    def slotScanMimeType(self, type):
        '''KIO.Job KRun.slotScanMimeType(QString type)'''
        return KIO.Job()
    def slotScanFinished(self):
        '''KJob KRun.slotScanFinished()'''
        return KJob()
    def slotTimeout(self):
        '''void KRun.slotTimeout()'''
    error = pyqtSignal() # void error() - signal
    finished = pyqtSignal() # void finished() - signal
    def isExecutableFile(self, url, mimetype):
        '''static bool KRun.isExecutableFile(KUrl url, QString mimetype)'''
        return bool()
    def isExecutable(self, serviceType):
        '''static bool KRun.isExecutable(QString serviceType)'''
        return bool()
    def binaryName(self, execLine, removePath):
        '''static QString KRun.binaryName(QString execLine, bool removePath)'''
        return QString()
    def processDesktopExec(self, _service, _urls, tempFiles = False, suggestedFileName = QString()):
        '''static QStringList KRun.processDesktopExec(KService _service, KUrl.List _urls, bool tempFiles = False, QString suggestedFileName = QString())'''
        return QStringList()
    def shellQuote(self, str):
        '''static void KRun.shellQuote(QString str)'''
    def displayOpenWithDialog(self, lst, window, tempFiles = False, suggestedFileName = QString(), asn = QByteArray()):
        '''static bool KRun.displayOpenWithDialog(KUrl.List lst, QWidget window, bool tempFiles = False, QString suggestedFileName = QString(), QByteArray asn = QByteArray())'''
        return bool()
    def runCommand(self, cmd, window):
        '''static bool KRun.runCommand(QString cmd, QWidget window)'''
        return bool()
    def runCommand(self, cmd, execName, icon, window, asn = QByteArray()):
        '''static bool KRun.runCommand(QString cmd, QString execName, QString icon, QWidget window, QByteArray asn = QByteArray())'''
        return bool()
    def runCommand(self, cmd, window, workingDirectory):
        '''static bool KRun.runCommand(QString cmd, QWidget window, QString workingDirectory)'''
        return bool()
    def runCommand(self, cmd, execName, icon, window, asn, workingDirectory):
        '''static bool KRun.runCommand(QString cmd, QString execName, QString icon, QWidget window, QByteArray asn, QString workingDirectory)'''
        return bool()
    def runUrl(self, url, mimetype, window, tempFile = False, runExecutables = True, suggestedFileName = QString(), asn = QByteArray()):
        '''static bool KRun.runUrl(KUrl url, QString mimetype, QWidget window, bool tempFile = False, bool runExecutables = True, QString suggestedFileName = QString(), QByteArray asn = QByteArray())'''
        return bool()
    def run(self, service, urls, window, tempFiles = False, suggestedFileName = QString(), asn = QByteArray()):
        '''static bool KRun.run(KService service, KUrl.List urls, QWidget window, bool tempFiles = False, QString suggestedFileName = QString(), QByteArray asn = QByteArray())'''
        return bool()
    def run(self, exec_, urls, window, name = QString(), icon = QString(), asn = QByteArray()):
        '''static bool KRun.run(QString exec, KUrl.List urls, QWidget window, QString name = QString(), QString icon = QString(), QByteArray asn = QByteArray())'''
        return bool()
    def suggestedFileName(self):
        '''QString KRun.suggestedFileName()'''
        return QString()
    def setSuggestedFileName(self, fileName):
        '''void KRun.setSuggestedFileName(QString fileName)'''
    def setEnableExternalBrowser(self, b):
        '''void KRun.setEnableExternalBrowser(bool b)'''
    def setRunExecutables(self, b):
        '''void KRun.setRunExecutables(bool b)'''
    def setPreferredService(self, desktopEntryName):
        '''void KRun.setPreferredService(QString desktopEntryName)'''
    def setAutoDelete(self, b):
        '''void KRun.setAutoDelete(bool b)'''
    def autoDelete(self):
        '''bool KRun.autoDelete()'''
        return bool()
    def hasFinished(self):
        '''bool KRun.hasFinished()'''
        return bool()
    def hasError(self):
        '''bool KRun.hasError()'''
        return bool()
    def abort(self):
        '''void KRun.abort()'''


class KSambaShare(QObject):
    """"""
    def getSharesByPath(self, path):
        '''list-of-KSambaShareData KSambaShare.getSharesByPath(QString path)'''
        return [KSambaShareData()]
    def getShareByName(self, name):
        '''KSambaShareData KSambaShare.getShareByName(QString name)'''
        return KSambaShareData()
    def shareNames(self):
        '''QStringList KSambaShare.shareNames()'''
        return QStringList()
    def isShareNameAvailable(self, name):
        '''bool KSambaShare.isShareNameAvailable(QString name)'''
        return bool()
    changed = pyqtSignal() # void changed() - signal
    def smbConfPath(self):
        '''QString KSambaShare.smbConfPath()'''
        return QString()
    def sharedDirectories(self):
        '''QStringList KSambaShare.sharedDirectories()'''
        return QStringList()
    def isDirectoryShared(self, path):
        '''bool KSambaShare.isDirectoryShared(QString path)'''
        return bool()
    def instance(self):
        '''static KSambaShare KSambaShare.instance()'''
        return KSambaShare()


class KSambaShareData():
    """"""
    # Enum KSambaShareData.UserShareError
    UserShareOk = 0
    UserShareExceedMaxShares = 0
    UserShareNameOk = 0
    UserShareNameInvalid = 0
    UserShareNameInUse = 0
    UserSharePathOk = 0
    UserSharePathInvalid = 0
    UserSharePathNotExists = 0
    UserSharePathNotDirectory = 0
    UserSharePathNotAbsolute = 0
    UserSharePathNotAllowed = 0
    UserShareAclOk = 0
    UserShareAclInvalid = 0
    UserShareAclUserNotValid = 0
    UserShareCommentOk = 0
    UserShareGuestsOk = 0
    UserShareGuestsInvalid = 0
    UserShareGuestsNotAllowed = 0
    UserShareSystemError = 0

    # Enum KSambaShareData.GuestPermission
    GuestsNotAllowed = 0
    GuestsAllowed = 0

    def __init__(self):
        '''void KSambaShareData.__init__()'''
    def __init__(self, other):
        '''void KSambaShareData.__init__(KSambaShareData other)'''
    def __ne__(self, other):
        '''bool KSambaShareData.__ne__(KSambaShareData other)'''
        return bool()
    def __eq__(self, other):
        '''bool KSambaShareData.__eq__(KSambaShareData other)'''
        return bool()
    def remove(self):
        '''KSambaShareData.UserShareError KSambaShareData.remove()'''
        return KSambaShareData.UserShareError()
    def save(self):
        '''KSambaShareData.UserShareError KSambaShareData.save()'''
        return KSambaShareData.UserShareError()
    def setGuestPermission(self, permission = None):
        '''KSambaShareData.UserShareError KSambaShareData.setGuestPermission(KSambaShareData.GuestPermission permission = KSambaShareData.GuestsNotAllowed)'''
        return KSambaShareData.UserShareError()
    def setAcl(self, acl):
        '''KSambaShareData.UserShareError KSambaShareData.setAcl(QString acl)'''
        return KSambaShareData.UserShareError()
    def setComment(self, comment):
        '''KSambaShareData.UserShareError KSambaShareData.setComment(QString comment)'''
        return KSambaShareData.UserShareError()
    def setPath(self, path):
        '''KSambaShareData.UserShareError KSambaShareData.setPath(QString path)'''
        return KSambaShareData.UserShareError()
    def setName(self, name):
        '''KSambaShareData.UserShareError KSambaShareData.setName(QString name)'''
        return KSambaShareData.UserShareError()
    def guestPermission(self):
        '''KSambaShareData.GuestPermission KSambaShareData.guestPermission()'''
        return KSambaShareData.GuestPermission()
    def acl(self):
        '''QString KSambaShareData.acl()'''
        return QString()
    def comment(self):
        '''QString KSambaShareData.comment()'''
        return QString()
    def path(self):
        '''QString KSambaShareData.path()'''
        return QString()
    def name(self):
        '''QString KSambaShareData.name()'''
        return QString()


class KScanDialog(KPageDialog):
    """"""
    def __init__(self, dialogFace = None, buttonMask = None, parent = None):
        '''void KScanDialog.__init__(int dialogFace = KPageDialog.Tabbed, int buttonMask = KDialog.Close|KDialog.Help, QWidget parent = None)'''
    textRecognized = pyqtSignal() # void textRecognized(const QStringamp;,int) - signal
    finalImage = pyqtSignal() # void finalImage(const QImageamp;,int) - signal
    preview = pyqtSignal() # void preview(const QImageamp;,int) - signal
    def nextId(self):
        '''int KScanDialog.nextId()'''
        return int()
    def id(self):
        '''int KScanDialog.id()'''
        return int()
    def setup(self):
        '''bool KScanDialog.setup()'''
        return bool()
    def getScanDialog(self, parent = None):
        '''static KScanDialog KScanDialog.getScanDialog(QWidget parent = None)'''
        return KScanDialog()


class KOCRDialog(KPageDialog):
    """"""
    def __init__(self, dialogFace = None, buttonMask = None, parent = None, modal = False):
        '''void KOCRDialog.__init__(int dialogFace = KPageDialog.Tabbed, int buttonMask = KDialog.Close|KDialog.Help, QWidget parent = None, bool modal = False)'''
    textRecognized = pyqtSignal() # void textRecognized(const QStringamp;,int) - signal
    def nextId(self):
        '''int KOCRDialog.nextId()'''
        return int()
    def id(self):
        '''int KOCRDialog.id()'''
        return int()
    def getOCRDialog(self, parent = None):
        '''static KOCRDialog KOCRDialog.getOCRDialog(QWidget parent = None)'''
        return KOCRDialog()


class KUrlCompletion(KCompletion):
    """"""
    # Enum KUrlCompletion.Mode
    ExeCompletion = 0
    FileCompletion = 0
    DirCompletion = 0

    def __init__(self):
        '''void KUrlCompletion.__init__()'''
    def __init__(self):
        '''KUrlCompletion.Mode KUrlCompletion.__init__()'''
        return KUrlCompletion.Mode()
    def customEvent(self, e):
        '''void KUrlCompletion.customEvent(QEvent e)'''
    def postProcessMatches(self, matches):
        '''void KUrlCompletion.postProcessMatches(QStringList matches)'''
    def postProcessMatch(self, match):
        '''void KUrlCompletion.postProcessMatch(QString match)'''
    def replacedPath(self, text):
        '''QString KUrlCompletion.replacedPath(QString text)'''
        return QString()
    def replacedPath(self, text, replaceHome, replaceEnv = True):
        '''static QString KUrlCompletion.replacedPath(QString text, bool replaceHome, bool replaceEnv = True)'''
        return QString()
    def setReplaceHome(self, replace):
        '''void KUrlCompletion.setReplaceHome(bool replace)'''
    def replaceHome(self):
        '''bool KUrlCompletion.replaceHome()'''
        return bool()
    def setReplaceEnv(self, replace):
        '''void KUrlCompletion.setReplaceEnv(bool replace)'''
    def replaceEnv(self):
        '''bool KUrlCompletion.replaceEnv()'''
        return bool()
    def setMode(self, mode):
        '''void KUrlCompletion.setMode(KUrlCompletion.Mode mode)'''
    def mode(self):
        '''KUrlCompletion.Mode KUrlCompletion.mode()'''
        return KUrlCompletion.Mode()
    def stop(self):
        '''void KUrlCompletion.stop()'''
    def isRunning(self):
        '''bool KUrlCompletion.isRunning()'''
        return bool()
    def dir(self):
        '''QString KUrlCompletion.dir()'''
        return QString()
    def setDir(self, dir):
        '''void KUrlCompletion.setDir(QString dir)'''
    def makeCompletion(self, text):
        '''QString KUrlCompletion.makeCompletion(QString text)'''
        return QString()


class KShellCompletion(KUrlCompletion):
    """"""
    def __init__(self):
        '''void KShellCompletion.__init__()'''
    def postProcessMatches(self, matches):
        '''void KShellCompletion.postProcessMatches(QStringList matches)'''
    def postProcessMatch(self, match):
        '''void KShellCompletion.postProcessMatch(QString match)'''
    def makeCompletion(self, text):
        '''QString KShellCompletion.makeCompletion(QString text)'''
        return QString()


class KStatusBarOfflineIndicator(QWidget):
    """"""
    def __init__(self, parent):
        '''void KStatusBarOfflineIndicator.__init__(QWidget parent)'''


class KTar(KArchive):
    """"""
    def __init__(self, filename, mimetype = QString()):
        '''void KTar.__init__(QString filename, QString mimetype = QString())'''
    def __init__(self, dev):
        '''void KTar.__init__(QIODevice dev)'''
    def createDevice(self, mode):
        '''bool KTar.createDevice(QIODevice.OpenMode mode)'''
        return bool()
    def closeArchive(self):
        '''bool KTar.closeArchive()'''
        return bool()
    def openArchive(self, mode):
        '''bool KTar.openArchive(QIODevice.OpenMode mode)'''
        return bool()
    def doFinishWriting(self, size):
        '''bool KTar.doFinishWriting(int size)'''
        return bool()
    def doPrepareWriting(self, name, user, group, size, perm, atime, mtime, ctime):
        '''bool KTar.doPrepareWriting(QString name, QString user, QString group, int size, int perm, int atime, int mtime, int ctime)'''
        return bool()
    def doWriteDir(self, name, user, group, perm, atime, mtime, ctime):
        '''bool KTar.doWriteDir(QString name, QString user, QString group, int perm, int atime, int mtime, int ctime)'''
        return bool()
    def doWriteSymLink(self, name, target, user, group, perm, atime, mtime, ctime):
        '''bool KTar.doWriteSymLink(QString name, QString target, QString user, QString group, int perm, int atime, int mtime, int ctime)'''
        return bool()
    def setOrigFileName(self, fileName):
        '''void KTar.setOrigFileName(QByteArray fileName)'''


class KUriFilterData():
    """"""
    # Enum KUriFilterData.SearchFilterOption
    SearchFilterOptionNone = 0
    RetrieveSearchProvidersOnly = 0
    RetrievePreferredSearchProvidersOnly = 0
    RetrieveAvailableSearchProvidersOnly = 0

    # Enum KUriFilterData.UriTypes
    NetProtocol = 0
    LocalFile = 0
    LocalDir = 0
    Executable = 0
    Help = 0
    Shell = 0
    Blocked = 0
    Error = 0
    Unknown = 0

    def __init__(self):
        '''void KUriFilterData.__init__()'''
    def __init__(self, url):
        '''void KUriFilterData.__init__(KUrl url)'''
    def __init__(self, url):
        '''void KUriFilterData.__init__(QString url)'''
    def setSearchFilteringOptions(self, options):
        '''void KUriFilterData.setSearchFilteringOptions(KUriFilterData.SearchFilterOptions options)'''
    def setDefaultUrlScheme(self):
        '''QString KUriFilterData.setDefaultUrlScheme()'''
        return QString()
    def searchFilteringOptions(self):
        '''KUriFilterData.SearchFilterOptions KUriFilterData.searchFilteringOptions()'''
        return KUriFilterData.SearchFilterOptions()
    def defaultUrlScheme(self):
        '''QString KUriFilterData.defaultUrlScheme()'''
        return QString()
    def allQueriesForSearchProvider(self, provider):
        '''QStringList KUriFilterData.allQueriesForSearchProvider(QString provider)'''
        return QStringList()
    def queryForSearchProvider(self, provider):
        '''KUriFilterSearchProvider KUriFilterData.queryForSearchProvider(QString provider)'''
        return KUriFilterSearchProvider()
    def setAlternateDefaultSearchProvider(self, provider):
        '''void KUriFilterData.setAlternateDefaultSearchProvider(QString provider)'''
    def setAlternateSearchProviders(self, providers):
        '''void KUriFilterData.setAlternateSearchProviders(QStringList providers)'''
    def alternateDefaultSearchProvider(self):
        '''QString KUriFilterData.alternateDefaultSearchProvider()'''
        return QString()
    def alternateSearchProviders(self):
        '''QStringList KUriFilterData.alternateSearchProviders()'''
        return QStringList()
    def iconNameForPreferredSearchProvider(self, provider):
        '''QString KUriFilterData.iconNameForPreferredSearchProvider(QString provider)'''
        return QString()
    def queryForPreferredSearchProvider(self, provider):
        '''QString KUriFilterData.queryForPreferredSearchProvider(QString provider)'''
        return QString()
    def preferredSearchProviders(self):
        '''QStringList KUriFilterData.preferredSearchProviders()'''
        return QStringList()
    def searchProvider(self):
        '''QString KUriFilterData.searchProvider()'''
        return QString()
    def searchTermSeparator(self):
        '''QChar KUriFilterData.searchTermSeparator()'''
        return QChar()
    def searchTerm(self):
        '''QString KUriFilterData.searchTerm()'''
        return QString()
    def typedString(self):
        '''QString KUriFilterData.typedString()'''
        return QString()
    def checkForExecutables(self):
        '''bool KUriFilterData.checkForExecutables()'''
        return bool()
    def setCheckForExecutables(self, check):
        '''void KUriFilterData.setCheckForExecutables(bool check)'''
    def iconName(self):
        '''QString KUriFilterData.iconName()'''
        return QString()
    def hasArgsAndOptions(self):
        '''bool KUriFilterData.hasArgsAndOptions()'''
        return bool()
    def argsAndOptions(self):
        '''QString KUriFilterData.argsAndOptions()'''
        return QString()
    def hasAbsolutePath(self):
        '''bool KUriFilterData.hasAbsolutePath()'''
        return bool()
    def absolutePath(self):
        '''QString KUriFilterData.absolutePath()'''
        return QString()
    def setAbsolutePath(self, abs_path):
        '''bool KUriFilterData.setAbsolutePath(QString abs_path)'''
        return bool()
    def setData(self, url):
        '''void KUriFilterData.setData(KUrl url)'''
    def setData(self, url):
        '''void KUriFilterData.setData(QString url)'''
    def uriType(self):
        '''KUriFilterData.UriTypes KUriFilterData.uriType()'''
        return KUriFilterData.UriTypes()
    def errorMsg(self):
        '''QString KUriFilterData.errorMsg()'''
        return QString()
    def uri(self):
        '''KUrl KUriFilterData.uri()'''
        return KUrl()
    class SearchFilterOptions():
        """"""
        def __init__(self):
            '''KUriFilterData.SearchFilterOptions KUriFilterData.SearchFilterOptions.__init__()'''
            return KUriFilterData.SearchFilterOptions()
        def __init__(self):
            '''int KUriFilterData.SearchFilterOptions.__init__()'''
            return int()
        def __init__(self):
            '''void KUriFilterData.SearchFilterOptions.__init__()'''
        def __bool__(self):
            '''int KUriFilterData.SearchFilterOptions.__bool__()'''
            return int()
        def __ne__(self, f):
            '''bool KUriFilterData.SearchFilterOptions.__ne__(KUriFilterData.SearchFilterOptions f)'''
            return bool()
        def __eq__(self, f):
            '''bool KUriFilterData.SearchFilterOptions.__eq__(KUriFilterData.SearchFilterOptions f)'''
            return bool()
        def __invert__(self):
            '''KUriFilterData.SearchFilterOptions KUriFilterData.SearchFilterOptions.__invert__()'''
            return KUriFilterData.SearchFilterOptions()
        def __and__(self, mask):
            '''KUriFilterData.SearchFilterOptions KUriFilterData.SearchFilterOptions.__and__(int mask)'''
            return KUriFilterData.SearchFilterOptions()
        def __xor__(self, f):
            '''KUriFilterData.SearchFilterOptions KUriFilterData.SearchFilterOptions.__xor__(KUriFilterData.SearchFilterOptions f)'''
            return KUriFilterData.SearchFilterOptions()
        def __xor__(self, f):
            '''KUriFilterData.SearchFilterOptions KUriFilterData.SearchFilterOptions.__xor__(int f)'''
            return KUriFilterData.SearchFilterOptions()
        def __or__(self, f):
            '''KUriFilterData.SearchFilterOptions KUriFilterData.SearchFilterOptions.__or__(KUriFilterData.SearchFilterOptions f)'''
            return KUriFilterData.SearchFilterOptions()
        def __or__(self, f):
            '''KUriFilterData.SearchFilterOptions KUriFilterData.SearchFilterOptions.__or__(int f)'''
            return KUriFilterData.SearchFilterOptions()
        def __int__(self):
            '''int KUriFilterData.SearchFilterOptions.__int__()'''
            return int()
        def __ixor__(self, f):
            '''KUriFilterData.SearchFilterOptions KUriFilterData.SearchFilterOptions.__ixor__(KUriFilterData.SearchFilterOptions f)'''
            return KUriFilterData.SearchFilterOptions()
        def __ior__(self, f):
            '''KUriFilterData.SearchFilterOptions KUriFilterData.SearchFilterOptions.__ior__(KUriFilterData.SearchFilterOptions f)'''
            return KUriFilterData.SearchFilterOptions()
        def __iand__(self, mask):
            '''KUriFilterData.SearchFilterOptions KUriFilterData.SearchFilterOptions.__iand__(int mask)'''
            return KUriFilterData.SearchFilterOptions()


class KUriFilterPlugin(QObject):
    """"""
    def __init__(self, name, parent = None):
        '''void KUriFilterPlugin.__init__(QString name, QObject parent = None)'''
    def resolveName(self, hostname, timeout):
        '''QHostInfo KUriFilterPlugin.resolveName(QString hostname, int timeout)'''
        return QHostInfo()
    def setSearchProviders(self, data, providers):
        '''void KUriFilterPlugin.setSearchProviders(KUriFilterData data, list-of-KUriFilterSearchProvider providers)'''
    def iconNameFor(self, url, type):
        '''QString KUriFilterPlugin.iconNameFor(KUrl url, KUriFilterData.UriTypes type)'''
        return QString()
    def setSearchProvider(self, data, provider, term, separator):
        '''void KUriFilterPlugin.setSearchProvider(KUriFilterData data, QString provider, QString term, QChar separator)'''
    def setArguments(self, data, args):
        '''void KUriFilterPlugin.setArguments(KUriFilterData data, QString args)'''
    def setUriType(self, data, type):
        '''void KUriFilterPlugin.setUriType(KUriFilterData data, KUriFilterData.UriTypes type)'''
    def setErrorMsg(self, data, errmsg):
        '''void KUriFilterPlugin.setErrorMsg(KUriFilterData data, QString errmsg)'''
    def setFilteredUri(self, data, uri):
        '''void KUriFilterPlugin.setFilteredUri(KUriFilterData data, KUrl uri)'''
    def configName(self):
        '''QString KUriFilterPlugin.configName()'''
        return QString()
    def configModule(self):
        '''str KUriFilterPlugin.configModule()'''
        return str()
    def filterUri(self, data):
        '''abstract bool KUriFilterPlugin.filterUri(KUriFilterData data)'''
        return bool()


class KUriFilter():
    """"""
    # Enum KUriFilter.SearchFilterType
    NormalTextFilter = 0
    WebShortcutFilter = 0

    def __init__(self):
        '''void KUriFilter.__init__()'''
    def filterSearchUri(self, data):
        '''bool KUriFilter.filterSearchUri(KUriFilterData data)'''
        return bool()
    def filterSearchUri(self, data, types):
        '''bool KUriFilter.filterSearchUri(KUriFilterData data, KUriFilter.SearchFilterTypes types)'''
        return bool()
    def loadPlugins(self):
        '''void KUriFilter.loadPlugins()'''
    def pluginNames(self):
        '''QStringList KUriFilter.pluginNames()'''
        return QStringList()
    def filteredUri(self, uri, filters = QStringList()):
        '''KUrl KUriFilter.filteredUri(KUrl uri, QStringList filters = QStringList())'''
        return KUrl()
    def filteredUri(self, uri, filters = QStringList()):
        '''QString KUriFilter.filteredUri(QString uri, QStringList filters = QStringList())'''
        return QString()
    def filterUri(self, data, filters = QStringList()):
        '''bool KUriFilter.filterUri(KUriFilterData data, QStringList filters = QStringList())'''
        return bool()
    def filterUri(self, uri, filters = QStringList()):
        '''bool KUriFilter.filterUri(KUrl uri, QStringList filters = QStringList())'''
        return bool()
    def filterUri(self, uri, filters = QStringList()):
        '''bool KUriFilter.filterUri(QString uri, QStringList filters = QStringList())'''
        return bool()
    def self(self):
        '''static KUriFilter KUriFilter.self()'''
        return KUriFilter()
    class SearchFilterTypes():
        """"""
        def __init__(self):
            '''KUriFilter.SearchFilterTypes KUriFilter.SearchFilterTypes.__init__()'''
            return KUriFilter.SearchFilterTypes()
        def __init__(self):
            '''int KUriFilter.SearchFilterTypes.__init__()'''
            return int()
        def __init__(self):
            '''void KUriFilter.SearchFilterTypes.__init__()'''
        def __bool__(self):
            '''int KUriFilter.SearchFilterTypes.__bool__()'''
            return int()
        def __ne__(self, f):
            '''bool KUriFilter.SearchFilterTypes.__ne__(KUriFilter.SearchFilterTypes f)'''
            return bool()
        def __eq__(self, f):
            '''bool KUriFilter.SearchFilterTypes.__eq__(KUriFilter.SearchFilterTypes f)'''
            return bool()
        def __invert__(self):
            '''KUriFilter.SearchFilterTypes KUriFilter.SearchFilterTypes.__invert__()'''
            return KUriFilter.SearchFilterTypes()
        def __and__(self, mask):
            '''KUriFilter.SearchFilterTypes KUriFilter.SearchFilterTypes.__and__(int mask)'''
            return KUriFilter.SearchFilterTypes()
        def __xor__(self, f):
            '''KUriFilter.SearchFilterTypes KUriFilter.SearchFilterTypes.__xor__(KUriFilter.SearchFilterTypes f)'''
            return KUriFilter.SearchFilterTypes()
        def __xor__(self, f):
            '''KUriFilter.SearchFilterTypes KUriFilter.SearchFilterTypes.__xor__(int f)'''
            return KUriFilter.SearchFilterTypes()
        def __or__(self, f):
            '''KUriFilter.SearchFilterTypes KUriFilter.SearchFilterTypes.__or__(KUriFilter.SearchFilterTypes f)'''
            return KUriFilter.SearchFilterTypes()
        def __or__(self, f):
            '''KUriFilter.SearchFilterTypes KUriFilter.SearchFilterTypes.__or__(int f)'''
            return KUriFilter.SearchFilterTypes()
        def __int__(self):
            '''int KUriFilter.SearchFilterTypes.__int__()'''
            return int()
        def __ixor__(self, f):
            '''KUriFilter.SearchFilterTypes KUriFilter.SearchFilterTypes.__ixor__(KUriFilter.SearchFilterTypes f)'''
            return KUriFilter.SearchFilterTypes()
        def __ior__(self, f):
            '''KUriFilter.SearchFilterTypes KUriFilter.SearchFilterTypes.__ior__(KUriFilter.SearchFilterTypes f)'''
            return KUriFilter.SearchFilterTypes()
        def __iand__(self, mask):
            '''KUriFilter.SearchFilterTypes KUriFilter.SearchFilterTypes.__iand__(int mask)'''
            return KUriFilter.SearchFilterTypes()


class KUriFilterSearchProvider():
    """"""
    def __init__(self):
        '''void KUriFilterSearchProvider.__init__()'''
    def __init__(self):
        '''KUriFilterSearchProvider KUriFilterSearchProvider.__init__()'''
        return KUriFilterSearchProvider()
    def setName(self):
        '''QString KUriFilterSearchProvider.setName()'''
        return QString()
    def setKeys(self):
        '''QStringList KUriFilterSearchProvider.setKeys()'''
        return QStringList()
    def setIconName(self):
        '''QString KUriFilterSearchProvider.setIconName()'''
        return QString()
    def setDesktopEntryName(self):
        '''QString KUriFilterSearchProvider.setDesktopEntryName()'''
        return QString()
    def defaultKey(self):
        '''QString KUriFilterSearchProvider.defaultKey()'''
        return QString()
    def keys(self):
        '''QStringList KUriFilterSearchProvider.keys()'''
        return QStringList()
    def iconName(self):
        '''QString KUriFilterSearchProvider.iconName()'''
        return QString()
    def name(self):
        '''QString KUriFilterSearchProvider.name()'''
        return QString()
    def desktopEntryName(self):
        '''QString KUriFilterSearchProvider.desktopEntryName()'''
        return QString()


class KUrlComboBox(KComboBox):
    """"""
    # Enum KUrlComboBox.OverLoadResolving
    RemoveTop = 0
    RemoveBottom = 0

    # Enum KUrlComboBox.Mode
    Files = 0
    Directories = 0
    Both = 0

    def __init__(self, mode, parent = None):
        '''void KUrlComboBox.__init__(KUrlComboBox.Mode mode, QWidget parent = None)'''
    def __init__(self, mode, rw, parent = None):
        '''void KUrlComboBox.__init__(KUrlComboBox.Mode mode, bool rw, QWidget parent = None)'''
    def mouseMoveEvent(self, event):
        '''void KUrlComboBox.mouseMoveEvent(QMouseEvent event)'''
    def mousePressEvent(self, event):
        '''void KUrlComboBox.mousePressEvent(QMouseEvent event)'''
    urlActivated = pyqtSignal() # void urlActivated(const KUrlamp;) - signal
    def setCompletionObject(self, compObj, hsig = True):
        '''void KUrlComboBox.setCompletionObject(KCompletion compObj, bool hsig = True)'''
    def removeUrl(self, url, checkDefaultURLs = True):
        '''void KUrlComboBox.removeUrl(KUrl url, bool checkDefaultURLs = True)'''
    def setDefaults(self):
        '''void KUrlComboBox.setDefaults()'''
    def addDefaultUrl(self, url, text = QString()):
        '''void KUrlComboBox.addDefaultUrl(KUrl url, QString text = QString())'''
    def addDefaultUrl(self, url, icon, text = QString()):
        '''void KUrlComboBox.addDefaultUrl(KUrl url, QIcon icon, QString text = QString())'''
    def maxItems(self):
        '''int KUrlComboBox.maxItems()'''
        return int()
    def setMaxItems(self):
        '''int KUrlComboBox.setMaxItems()'''
        return int()
    def urls(self):
        '''QStringList KUrlComboBox.urls()'''
        return QStringList()
    def setUrls(self, urls):
        '''void KUrlComboBox.setUrls(QStringList urls)'''
    def setUrls(self, urls, remove):
        '''void KUrlComboBox.setUrls(QStringList urls, KUrlComboBox.OverLoadResolving remove)'''
    def setUrl(self, url):
        '''void KUrlComboBox.setUrl(KUrl url)'''


class KUrlNavigator(QWidget):
    """"""
    def __init__(self, placesModel, url, parent):
        '''void KUrlNavigator.__init__(KFilePlacesModel placesModel, KUrl url, QWidget parent)'''
    def __init__(self, parent = None):
        '''void KUrlNavigator.__init__(QWidget parent = None)'''
    def wheelEvent(self, event):
        '''void KUrlNavigator.wheelEvent(QWheelEvent event)'''
    def keyReleaseEvent(self, event):
        '''void KUrlNavigator.keyReleaseEvent(QKeyEvent event)'''
    def keyPressEvent(self, event):
        '''void KUrlNavigator.keyPressEvent(QKeyEvent event)'''
    tabRequested = pyqtSignal() # void tabRequested(const KUrlamp;) - signal
    urlAboutToBeChanged = pyqtSignal() # void urlAboutToBeChanged(const KUrlamp;) - signal
    def setLocationUrl(self, url):
        '''void KUrlNavigator.setLocationUrl(KUrl url)'''
    def homeUrl(self):
        '''KUrl KUrlNavigator.homeUrl()'''
        return KUrl()
    def locationState(self, historyIndex = None):
        '''QByteArray KUrlNavigator.locationState(int historyIndex = -1)'''
        return QByteArray()
    def saveLocationState(self, state):
        '''void KUrlNavigator.saveLocationState(QByteArray state)'''
    def locationUrl(self, historyIndex = None):
        '''KUrl KUrlNavigator.locationUrl(int historyIndex = -1)'''
        return KUrl()
    def eventFilter(self, watched, event):
        '''bool KUrlNavigator.eventFilter(QObject watched, QEvent event)'''
        return bool()
    def resizeEvent(self, event):
        '''void KUrlNavigator.resizeEvent(QResizeEvent event)'''
    def mouseReleaseEvent(self, event):
        '''void KUrlNavigator.mouseReleaseEvent(QMouseEvent event)'''
    returnPressed = pyqtSignal() # void returnPressed() - signal
    urlsDropped = pyqtSignal() # void urlsDropped(const KUrl::Listamp;,const KUrlamp;) - signal
    urlsDropped = pyqtSignal() # void urlsDropped(const KUrlamp;,QDropEvent *) - signal
    historyChanged = pyqtSignal() # void historyChanged() - signal
    editableStateChanged = pyqtSignal() # void editableStateChanged(bool) - signal
    urlChanged = pyqtSignal() # void urlChanged(const KUrlamp;) - signal
    activated = pyqtSignal() # void activated() - signal
    def setFocus(self):
        '''void KUrlNavigator.setFocus()'''
    def savePosition(self, x, y):
        '''void KUrlNavigator.savePosition(int x, int y)'''
    def saveRootUrl(self, url):
        '''void KUrlNavigator.saveRootUrl(KUrl url)'''
    def requestActivation(self):
        '''void KUrlNavigator.requestActivation()'''
    def setUrl(self, url):
        '''void KUrlNavigator.setUrl(KUrl url)'''
    def customProtocols(self):
        '''QStringList KUrlNavigator.customProtocols()'''
        return QStringList()
    def setCustomProtocols(self, protocols):
        '''void KUrlNavigator.setCustomProtocols(QStringList protocols)'''
    def editor(self):
        '''KUrlComboBox KUrlNavigator.editor()'''
        return KUrlComboBox()
    def savedPosition(self):
        '''QPoint KUrlNavigator.savedPosition()'''
        return QPoint()
    def savedRootUrl(self):
        '''KUrl KUrlNavigator.savedRootUrl()'''
        return KUrl()
    def historyUrl(self, historyIndex):
        '''KUrl KUrlNavigator.historyUrl(int historyIndex)'''
        return KUrl()
    def historyIndex(self):
        '''int KUrlNavigator.historyIndex()'''
        return int()
    def historySize(self):
        '''int KUrlNavigator.historySize()'''
        return int()
    def isPlacesSelectorVisible(self):
        '''bool KUrlNavigator.isPlacesSelectorVisible()'''
        return bool()
    def setPlacesSelectorVisible(self, visible):
        '''void KUrlNavigator.setPlacesSelectorVisible(bool visible)'''
    def isActive(self):
        '''bool KUrlNavigator.isActive()'''
        return bool()
    def setActive(self, active):
        '''void KUrlNavigator.setActive(bool active)'''
    def showFullPath(self):
        '''bool KUrlNavigator.showFullPath()'''
        return bool()
    def setShowFullPath(self, show):
        '''void KUrlNavigator.setShowFullPath(bool show)'''
    def isUrlEditable(self):
        '''bool KUrlNavigator.isUrlEditable()'''
        return bool()
    def setUrlEditable(self, editable):
        '''void KUrlNavigator.setUrlEditable(bool editable)'''
    def setHomeUrl(self, homeUrl):
        '''void KUrlNavigator.setHomeUrl(QString homeUrl)'''
    def setHomeUrl(self, url):
        '''void KUrlNavigator.setHomeUrl(KUrl url)'''
    def goHome(self):
        '''void KUrlNavigator.goHome()'''
    def goUp(self):
        '''bool KUrlNavigator.goUp()'''
        return bool()
    def goForward(self):
        '''bool KUrlNavigator.goForward()'''
        return bool()
    def goBack(self):
        '''bool KUrlNavigator.goBack()'''
        return bool()
    def uncommittedUrl(self):
        '''KUrl KUrlNavigator.uncommittedUrl()'''
        return KUrl()
    def url(self):
        '''KUrl KUrlNavigator.url()'''
        return KUrl()
    def url(self, index):
        '''KUrl KUrlNavigator.url(int index)'''
        return KUrl()


class KUrlPixmapProvider(KPixmapProvider):
    """"""
    def __init__(self):
        '''void KUrlPixmapProvider.__init__()'''
    def pixmapFor(self, url, size = 0):
        '''QPixmap KUrlPixmapProvider.pixmapFor(QString url, int size = 0)'''
        return QPixmap()


class KUrlRequester(KHBox):
    """"""
    def __init__(self, parent = None):
        '''void KUrlRequester.__init__(QWidget parent = None)'''
    def __init__(self, url, parent = None):
        '''void KUrlRequester.__init__(KUrl url, QWidget parent = None)'''
    def __init__(self, editWidget, parent):
        '''void KUrlRequester.__init__(QWidget editWidget, QWidget parent)'''
    def setFileDialogModality(self, modality):
        '''void KUrlRequester.setFileDialogModality(Qt.WindowModality modality)'''
    def fileDialogModality(self):
        '''Qt.WindowModality KUrlRequester.fileDialogModality()'''
        return Qt.WindowModality()
    def eventFilter(self, obj, ev):
        '''bool KUrlRequester.eventFilter(QObject obj, QEvent ev)'''
        return bool()
    def changeEvent(self, e):
        '''void KUrlRequester.changeEvent(QEvent e)'''
    urlSelected = pyqtSignal() # void urlSelected(const KUrlamp;) - signal
    openFileDialog = pyqtSignal() # void openFileDialog(KUrlRequester *) - signal
    returnPressed = pyqtSignal() # void returnPressed() - signal
    returnPressed = pyqtSignal() # void returnPressed(const QStringamp;) - signal
    textChanged = pyqtSignal() # void textChanged(const QStringamp;) - signal
    def clear(self):
        '''void KUrlRequester.clear()'''
    def setText(self, text):
        '''void KUrlRequester.setText(QString text)'''
    def setPath(self, path):
        '''void KUrlRequester.setPath(QString path)'''
    def setStartDir(self, startDir):
        '''void KUrlRequester.setStartDir(KUrl startDir)'''
    def setUrl(self, url):
        '''void KUrlRequester.setUrl(KUrl url)'''
    def setClickMessage(self, msg):
        '''void KUrlRequester.setClickMessage(QString msg)'''
    def clickMessage(self):
        '''QString KUrlRequester.clickMessage()'''
        return QString()
    def customEditor(self):
        '''KEditListBox.CustomEditor KUrlRequester.customEditor()'''
        return KEditListBox.CustomEditor()
    def completionObject(self):
        '''KUrlCompletion KUrlRequester.completionObject()'''
        return KUrlCompletion()
    def button(self):
        '''KPushButton KUrlRequester.button()'''
        return KPushButton()
    def comboBox(self):
        '''KComboBox KUrlRequester.comboBox()'''
        return KComboBox()
    def lineEdit(self):
        '''KLineEdit KUrlRequester.lineEdit()'''
        return KLineEdit()
    def fileDialog(self):
        '''KFileDialog KUrlRequester.fileDialog()'''
        return KFileDialog()
    def filter(self):
        '''QString KUrlRequester.filter()'''
        return QString()
    def setFilter(self, filter):
        '''void KUrlRequester.setFilter(QString filter)'''
    def mode(self):
        '''KFile.Modes KUrlRequester.mode()'''
        return KFile.Modes()
    def setMode(self, m):
        '''void KUrlRequester.setMode(KFile.Modes m)'''
    def text(self):
        '''QString KUrlRequester.text()'''
        return QString()
    def startDir(self):
        '''KUrl KUrlRequester.startDir()'''
        return KUrl()
    def url(self):
        '''KUrl KUrlRequester.url()'''
        return KUrl()


class KUrlComboRequester(KUrlRequester):
    """"""
    def __init__(self, parent = None):
        '''void KUrlComboRequester.__init__(QWidget parent = None)'''


class KUrlRequesterDialog(KDialog):
    """"""
    def __init__(self, url, parent = None):
        '''void KUrlRequesterDialog.__init__(QString url, QWidget parent = None)'''
    def __init__(self, url, text, parent):
        '''void KUrlRequesterDialog.__init__(QString url, QString text, QWidget parent)'''
    def urlRequester(self):
        '''KUrlRequester KUrlRequesterDialog.urlRequester()'''
        return KUrlRequester()
    def fileDialog(self):
        '''KFileDialog KUrlRequesterDialog.fileDialog()'''
        return KFileDialog()
    def getUrl(self, url = QString(), parent = None, caption = QString()):
        '''static KUrl KUrlRequesterDialog.getUrl(QString url = QString(), QWidget parent = None, QString caption = QString())'''
        return KUrl()
    def selectedUrl(self):
        '''KUrl KUrlRequesterDialog.selectedUrl()'''
        return KUrl()


class KZip(KArchive):
    """"""
    # Enum KZip.Compression
    NoCompression = 0
    DeflateCompression = 0

    # Enum KZip.ExtraField
    NoExtraField = 0
    ModificationTime = 0
    DefaultExtraField = 0

    def __init__(self, filename):
        '''void KZip.__init__(QString filename)'''
    def __init__(self, dev):
        '''void KZip.__init__(QIODevice dev)'''
    def doWriteDir(self, name, user, group, perm, atime, mtime, ctime):
        '''bool KZip.doWriteDir(QString name, QString user, QString group, int perm, int atime, int mtime, int ctime)'''
        return bool()
    def closeArchive(self):
        '''bool KZip.closeArchive()'''
        return bool()
    def openArchive(self, mode):
        '''bool KZip.openArchive(QIODevice.OpenMode mode)'''
        return bool()
    def doFinishWriting(self, size):
        '''bool KZip.doFinishWriting(int size)'''
        return bool()
    def doPrepareWriting(self, name, user, group, size, perm, atime, mtime, ctime):
        '''bool KZip.doPrepareWriting(QString name, QString user, QString group, int size, int perm, int atime, int mtime, int ctime)'''
        return bool()
    def doWriteSymLink(self, name, target, user, group, perm, atime, mtime, ctime):
        '''bool KZip.doWriteSymLink(QString name, QString target, QString user, QString group, int perm, int atime, int mtime, int ctime)'''
        return bool()
    def writeData(self, data, size):
        '''bool KZip.writeData(str data, int size)'''
        return bool()
    def compression(self):
        '''KZip.Compression KZip.compression()'''
        return KZip.Compression()
    def setCompression(self, c):
        '''void KZip.setCompression(KZip.Compression c)'''
    def extraField(self):
        '''KZip.ExtraField KZip.extraField()'''
        return KZip.ExtraField()
    def setExtraField(self, ef):
        '''void KZip.setExtraField(KZip.ExtraField ef)'''


class KZipFileEntry(KArchiveFile):
    """"""
    def __init__(self, zip, name, access, date, user, group, symlink, path, start, uncompressedSize, encoding, compressedSize):
        '''void KZipFileEntry.__init__(KZip zip, QString name, int access, int date, QString user, QString group, QString symlink, QString path, int start, int uncompressedSize, int encoding, int compressedSize)'''
    def createDevice(self):
        '''QIODevice KZipFileEntry.createDevice()'''
        return QIODevice()
    def data(self):
        '''QByteArray KZipFileEntry.data()'''
        return QByteArray()
    def path(self):
        '''QString KZipFileEntry.path()'''
        return QString()
    def setCRC32(self, crc32):
        '''void KZipFileEntry.setCRC32(int crc32)'''
    def crc32(self):
        '''int KZipFileEntry.crc32()'''
        return int()
    def headerStart(self):
        '''int KZipFileEntry.headerStart()'''
        return int()
    def setHeaderStart(self, headerstart):
        '''void KZipFileEntry.setHeaderStart(int headerstart)'''
    def setCompressedSize(self, compressedSize):
        '''void KZipFileEntry.setCompressedSize(int compressedSize)'''
    def compressedSize(self):
        '''int KZipFileEntry.compressedSize()'''
        return int()
    def encoding(self):
        '''int KZipFileEntry.encoding()'''
        return int()


class PredicateProperties():
    """"""
    # Enum PredicateProperties.Attributes
    Addable = 0
    Removable = 0
    Modifiable = 0
    Cumulative = 0
    Averaged = 0
    MultiLine = 0
    SqueezeText = 0

    def __init__(self, predicate = QString()):
        '''void PredicateProperties.__init__(QString predicate = QString())'''
    def __init__(self, p):
        '''void PredicateProperties.__init__(PredicateProperties p)'''
    def isValid(self):
        '''bool PredicateProperties.isValid()'''
        return bool()
    def parent(self):
        '''PredicateProperties PredicateProperties.parent()'''
        return PredicateProperties()
    def maxCardinality(self):
        '''int PredicateProperties.maxCardinality()'''
        return int()
    def minCardinality(self):
        '''int PredicateProperties.minCardinality()'''
        return int()
    def suggestedValues(self):
        '''QStringList PredicateProperties.suggestedValues()'''
        return QStringList()
    def createValidator(self):
        '''QValidator PredicateProperties.createValidator()'''
        return QValidator()
    def name(self):
        '''QString PredicateProperties.name()'''
        return QString()
    def type(self):
        '''Type PredicateProperties.type()'''
        return Type()
    def attributes(self):
        '''int PredicateProperties.attributes()'''
        return int()


class ThumbCreatorV2(ThumbCreator):
    """"""
    def __init__(self):
        '''void ThumbCreatorV2.__init__()'''
    def __init__(self):
        '''ThumbCreatorV2 ThumbCreatorV2.__init__()'''
        return ThumbCreatorV2()
    def writeConfiguration(self, configurationWidget):
        '''void ThumbCreatorV2.writeConfiguration(QWidget configurationWidget)'''
    def createConfigurationWidget(self):
        '''QWidget ThumbCreatorV2.createConfigurationWidget()'''
        return QWidget()


def qHash(key):
    '''static int qHash(QString key)'''
    return int()

def qHash(item):
    '''static int qHash(KFileItem item)'''
    return int()

