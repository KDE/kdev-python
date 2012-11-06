class pyqtSignal():
 def connect(self, targetSignal): pass
 def emit(self, *args): pass
from QtCore import *

class DNSSD():
    """"""
    class ServiceModel(QAbstractItemModel):
        """"""
        # Enum DNSSD.ServiceModel.ModelColumns
        ServiceName = 0
        Host = 0
        Port = 0
    
        # Enum DNSSD.ServiceModel.AdditionalRoles
        ServicePtrRole = 0
    
        def __init__(self, browser, parent = None):
            '''void DNSSD.ServiceModel.__init__(DNSSD.ServiceBrowser browser, QObject parent = None)'''
        def hasIndex(self, row, column, parent):
            '''bool DNSSD.ServiceModel.hasIndex(int row, int column, QModelIndex parent)'''
            return bool()
        def headerData(self, section, orientation, role = None):
            '''QVariant DNSSD.ServiceModel.headerData(int section, Qt.Orientation orientation, int role = Qt.DisplayRole)'''
            return QVariant()
        def data(self, index, role = None):
            '''QVariant DNSSD.ServiceModel.data(QModelIndex index, int role = Qt.DisplayRole)'''
            return QVariant()
        def index(self, row, column, parent = QModelIndex()):
            '''QModelIndex DNSSD.ServiceModel.index(int row, int column, QModelIndex parent = QModelIndex())'''
            return QModelIndex()
        def parent(self, index):
            '''QModelIndex DNSSD.ServiceModel.parent(QModelIndex index)'''
            return QModelIndex()
        def rowCount(self, parent = QModelIndex()):
            '''int DNSSD.ServiceModel.rowCount(QModelIndex parent = QModelIndex())'''
            return int()
        def columnCount(self, parent = QModelIndex()):
            '''int DNSSD.ServiceModel.columnCount(QModelIndex parent = QModelIndex())'''
            return int()
    class RemoteService(QObject, DNSSD.ServiceBase):
        """"""
        def __init__(self, name, type, domain):
            '''void DNSSD.RemoteService.__init__(QString name, QString type, QString domain)'''
        def virtual_hook(self, id, data):
            '''void DNSSD.RemoteService.virtual_hook(int id, sip.voidptr data)'''
        resolved = pyqtSignal() # void resolved(bool) - signal
        def isResolved(self):
            '''bool DNSSD.RemoteService.isResolved()'''
            return bool()
        def resolve(self):
            '''bool DNSSD.RemoteService.resolve()'''
            return bool()
        def resolveAsync(self):
            '''void DNSSD.RemoteService.resolveAsync()'''
    class DomainBrowser(QObject):
        """"""
        # Enum DNSSD.DomainBrowser.DomainType
        Browsing = 0
        Publishing = 0
    
        def __init__(self, type, parent = None):
            '''void DNSSD.DomainBrowser.__init__(DNSSD.DomainBrowser.DomainType type, QObject parent = None)'''
        domainAdded = pyqtSignal() # void domainAdded(const QStringamp;) - signal
        domainRemoved = pyqtSignal() # void domainRemoved(const QStringamp;) - signal
        def isRunning(self):
            '''bool DNSSD.DomainBrowser.isRunning()'''
            return bool()
        def startBrowse(self):
            '''void DNSSD.DomainBrowser.startBrowse()'''
        def domains(self):
            '''QStringList DNSSD.DomainBrowser.domains()'''
            return QStringList()
    class DomainModel(QAbstractItemModel):
        """"""
        def __init__(self, browser, parent = None):
            '''void DNSSD.DomainModel.__init__(DNSSD.DomainBrowser browser, QObject parent = None)'''
        def hasIndex(self, row, column, parent):
            '''bool DNSSD.DomainModel.hasIndex(int row, int column, QModelIndex parent)'''
            return bool()
        def data(self, index, role = None):
            '''QVariant DNSSD.DomainModel.data(QModelIndex index, int role = Qt.DisplayRole)'''
            return QVariant()
        def index(self, row, column, parent = QModelIndex()):
            '''QModelIndex DNSSD.DomainModel.index(int row, int column, QModelIndex parent = QModelIndex())'''
            return QModelIndex()
        def parent(self, index):
            '''QModelIndex DNSSD.DomainModel.parent(QModelIndex index)'''
            return QModelIndex()
        def rowCount(self, parent = QModelIndex()):
            '''int DNSSD.DomainModel.rowCount(QModelIndex parent = QModelIndex())'''
            return int()
        def columnCount(self, parent = QModelIndex()):
            '''int DNSSD.DomainModel.columnCount(QModelIndex parent = QModelIndex())'''
            return int()
    class ServiceTypeBrowser(QObject):
        """"""
        def __init__(self, domain = QString(), parent = None):
            '''void DNSSD.ServiceTypeBrowser.__init__(QString domain = QString(), QObject parent = None)'''
        finished = pyqtSignal() # void finished() - signal
        serviceTypeAdded = pyqtSignal() # void serviceTypeAdded(const QStringamp;) - signal
        serviceTypeRemoved = pyqtSignal() # void serviceTypeRemoved(const QStringamp;) - signal
        def isRunning(self):
            '''bool DNSSD.ServiceTypeBrowser.isRunning()'''
            return bool()
        def startBrowse(self):
            '''void DNSSD.ServiceTypeBrowser.startBrowse()'''
        def serviceTypes(self):
            '''QStringList DNSSD.ServiceTypeBrowser.serviceTypes()'''
            return QStringList()
    class ServiceBrowser(QObject):
        """"""
        # Enum DNSSD.ServiceBrowser.State
        Working = 0
        Stopped = 0
        Unsupported = 0
    
        def __init__(self, type, autoResolve = False, domain = QString(), subtype = QString()):
            '''void DNSSD.ServiceBrowser.__init__(QString type, bool autoResolve = False, QString domain = QString(), QString subtype = QString())'''
        def virtual_hook(self):
            '''sip.voidptr DNSSD.ServiceBrowser.virtual_hook()'''
            return sip.voidptr()
        finished = pyqtSignal() # void finished() - signal
        serviceRemoved = pyqtSignal() # void serviceRemoved(DNSSD::RemoteService::Ptr) - signal
        serviceAdded = pyqtSignal() # void serviceAdded(DNSSD::RemoteService::Ptr) - signal
        def getLocalHostName(self):
            '''static QString DNSSD.ServiceBrowser.getLocalHostName()'''
            return QString()
        def resolveHostName(self, hostname):
            '''static QHostAddress DNSSD.ServiceBrowser.resolveHostName(QString hostname)'''
            return QHostAddress()
        def isAutoResolving(self):
            '''bool DNSSD.ServiceBrowser.isAutoResolving()'''
            return bool()
        def isAvailable(self):
            '''static DNSSD.ServiceBrowser.State DNSSD.ServiceBrowser.isAvailable()'''
            return DNSSD.ServiceBrowser.State()
        def startBrowse(self):
            '''void DNSSD.ServiceBrowser.startBrowse()'''
        def services(self):
            '''unknown-type DNSSD.ServiceBrowser.services()'''
            return unknown-type()
    class PublicService(QObject, DNSSD.ServiceBase):
        """"""
        def __init__(self, name = QString(), type = QString(), port = 0, domain = QString(), subtypes = QStringList()):
            '''void DNSSD.PublicService.__init__(QString name = QString(), QString type = QString(), int port = 0, QString domain = QString(), QStringList subtypes = QStringList())'''
        def virtual_hook(self):
            '''sip.voidptr DNSSD.PublicService.virtual_hook()'''
            return sip.voidptr()
        published = pyqtSignal() # void published(bool) - signal
        def subtypes(self):
            '''QStringList DNSSD.PublicService.subtypes()'''
            return QStringList()
        def setDomain(self, domain):
            '''void DNSSD.PublicService.setDomain(QString domain)'''
        def setPort(self, port):
            '''void DNSSD.PublicService.setPort(int port)'''
        def setSubTypes(self, subtypes):
            '''void DNSSD.PublicService.setSubTypes(QStringList subtypes)'''
        def setType(self, type):
            '''void DNSSD.PublicService.setType(QString type)'''
        def setServiceName(self, serviceName):
            '''void DNSSD.PublicService.setServiceName(QString serviceName)'''
        def setTextData(self, textData):
            '''void DNSSD.PublicService.setTextData(dict-of-QString-QByteArray textData)'''
        def publishAsync(self):
            '''void DNSSD.PublicService.publishAsync()'''
        def isPublished(self):
            '''bool DNSSD.PublicService.isPublished()'''
            return bool()
        def publish(self):
            '''bool DNSSD.PublicService.publish()'''
            return bool()
        def stop(self):
            '''void DNSSD.PublicService.stop()'''
    class ServiceBase(KShared):
        """"""
        def __init__(self, name = QString(), type = QString(), domain = QString(), host = QString(), port = 0):
            '''void DNSSD.ServiceBase.__init__(QString name = QString(), QString type = QString(), QString domain = QString(), QString host = QString(), int port = 0)'''
        def __ne__(self, o):
            '''bool DNSSD.ServiceBase.__ne__(DNSSD.ServiceBase o)'''
            return bool()
        def __eq__(self, o):
            '''bool DNSSD.ServiceBase.__eq__(DNSSD.ServiceBase o)'''
            return bool()
        def textData(self):
            '''dict-of-QString-QByteArray DNSSD.ServiceBase.textData()'''
            return dict-of-QString-QByteArray()
        def port(self):
            '''int DNSSD.ServiceBase.port()'''
            return int()
        def hostName(self):
            '''QString DNSSD.ServiceBase.hostName()'''
            return QString()
        def domain(self):
            '''QString DNSSD.ServiceBase.domain()'''
            return QString()
        def type(self):
            '''QString DNSSD.ServiceBase.type()'''
            return QString()
        def serviceName(self):
            '''QString DNSSD.ServiceBase.serviceName()'''
            return QString()


