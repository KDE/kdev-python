class pyqtSignal():
 def connect(self, targetSignal): pass
 def emit(self, *args): pass
from QtCore import *

class QHelpContentItem():
    """"""
    def childPosition(self, child):
        '''int QHelpContentItem.childPosition(QHelpContentItem child)'''
        return int()
    def parent(self):
        '''QHelpContentItem QHelpContentItem.parent()'''
        return QHelpContentItem()
    def row(self):
        '''int QHelpContentItem.row()'''
        return int()
    def url(self):
        '''QUrl QHelpContentItem.url()'''
        return QUrl()
    def title(self):
        '''QString QHelpContentItem.title()'''
        return QString()
    def childCount(self):
        '''int QHelpContentItem.childCount()'''
        return int()
    def child(self, row):
        '''QHelpContentItem QHelpContentItem.child(int row)'''
        return QHelpContentItem()


class QHelpContentModel(QAbstractItemModel):
    """"""
    contentsCreated = pyqtSignal() # void contentsCreated() - signal
    contentsCreationStarted = pyqtSignal() # void contentsCreationStarted() - signal
    def isCreatingContents(self):
        '''bool QHelpContentModel.isCreatingContents()'''
        return bool()
    def columnCount(self, parent = QModelIndex()):
        '''int QHelpContentModel.columnCount(QModelIndex parent = QModelIndex())'''
        return int()
    def rowCount(self, parent = QModelIndex()):
        '''int QHelpContentModel.rowCount(QModelIndex parent = QModelIndex())'''
        return int()
    def parent(self, index):
        '''QModelIndex QHelpContentModel.parent(QModelIndex index)'''
        return QModelIndex()
    def index(self, row, column, parent = QModelIndex()):
        '''QModelIndex QHelpContentModel.index(int row, int column, QModelIndex parent = QModelIndex())'''
        return QModelIndex()
    def data(self, index, role):
        '''QVariant QHelpContentModel.data(QModelIndex index, int role)'''
        return QVariant()
    def contentItemAt(self, index):
        '''QHelpContentItem QHelpContentModel.contentItemAt(QModelIndex index)'''
        return QHelpContentItem()
    def createContents(self, customFilterName):
        '''void QHelpContentModel.createContents(QString customFilterName)'''


class QHelpContentWidget(QTreeView):
    """"""
    linkActivated = pyqtSignal() # void linkActivated(const QUrlamp;) - signal
    def indexOf(self, link):
        '''QModelIndex QHelpContentWidget.indexOf(QUrl link)'''
        return QModelIndex()


class QHelpEngineCore(QObject):
    """"""
    def __init__(self, collectionFile, parent = None):
        '''void QHelpEngineCore.__init__(QString collectionFile, QObject parent = None)'''
    warning = pyqtSignal() # void warning(const QStringamp;) - signal
    currentFilterChanged = pyqtSignal() # void currentFilterChanged(const QStringamp;) - signal
    setupFinished = pyqtSignal() # void setupFinished() - signal
    setupStarted = pyqtSignal() # void setupStarted() - signal
    def setAutoSaveFilter(self, save):
        '''void QHelpEngineCore.setAutoSaveFilter(bool save)'''
    def autoSaveFilter(self):
        '''bool QHelpEngineCore.autoSaveFilter()'''
        return bool()
    def error(self):
        '''QString QHelpEngineCore.error()'''
        return QString()
    def metaData(self, documentationFileName, name):
        '''static QVariant QHelpEngineCore.metaData(QString documentationFileName, QString name)'''
        return QVariant()
    def setCustomValue(self, key, value):
        '''bool QHelpEngineCore.setCustomValue(QString key, QVariant value)'''
        return bool()
    def customValue(self, key, defaultValue = QVariant()):
        '''QVariant QHelpEngineCore.customValue(QString key, QVariant defaultValue = QVariant())'''
        return QVariant()
    def removeCustomValue(self, key):
        '''bool QHelpEngineCore.removeCustomValue(QString key)'''
        return bool()
    def linksForIdentifier(self, id):
        '''dict-of-QString-QUrl QHelpEngineCore.linksForIdentifier(QString id)'''
        return dict-of-QString-QUrl()
    def fileData(self, url):
        '''QByteArray QHelpEngineCore.fileData(QUrl url)'''
        return QByteArray()
    def findFile(self, url):
        '''QUrl QHelpEngineCore.findFile(QUrl url)'''
        return QUrl()
    def files(self, namespaceName, filterAttributes, extensionFilter = QString()):
        '''list-of-QUrl QHelpEngineCore.files(QString namespaceName, QStringList filterAttributes, QString extensionFilter = QString())'''
        return [QUrl()]
    def filterAttributeSets(self, namespaceName):
        '''list-of-QStringList QHelpEngineCore.filterAttributeSets(QString namespaceName)'''
        return [QStringList()]
    def registeredDocumentations(self):
        '''QStringList QHelpEngineCore.registeredDocumentations()'''
        return QStringList()
    def setCurrentFilter(self, filterName):
        '''void QHelpEngineCore.setCurrentFilter(QString filterName)'''
    def currentFilter(self):
        '''QString QHelpEngineCore.currentFilter()'''
        return QString()
    def filterAttributes(self):
        '''QStringList QHelpEngineCore.filterAttributes()'''
        return QStringList()
    def filterAttributes(self, filterName):
        '''QStringList QHelpEngineCore.filterAttributes(QString filterName)'''
        return QStringList()
    def addCustomFilter(self, filterName, attributes):
        '''bool QHelpEngineCore.addCustomFilter(QString filterName, QStringList attributes)'''
        return bool()
    def removeCustomFilter(self, filterName):
        '''bool QHelpEngineCore.removeCustomFilter(QString filterName)'''
        return bool()
    def customFilters(self):
        '''QStringList QHelpEngineCore.customFilters()'''
        return QStringList()
    def documentationFileName(self, namespaceName):
        '''QString QHelpEngineCore.documentationFileName(QString namespaceName)'''
        return QString()
    def unregisterDocumentation(self, namespaceName):
        '''bool QHelpEngineCore.unregisterDocumentation(QString namespaceName)'''
        return bool()
    def registerDocumentation(self, documentationFileName):
        '''bool QHelpEngineCore.registerDocumentation(QString documentationFileName)'''
        return bool()
    def namespaceName(self, documentationFileName):
        '''static QString QHelpEngineCore.namespaceName(QString documentationFileName)'''
        return QString()
    def copyCollectionFile(self, fileName):
        '''bool QHelpEngineCore.copyCollectionFile(QString fileName)'''
        return bool()
    def setCollectionFile(self, fileName):
        '''void QHelpEngineCore.setCollectionFile(QString fileName)'''
    def collectionFile(self):
        '''QString QHelpEngineCore.collectionFile()'''
        return QString()
    def setupData(self):
        '''bool QHelpEngineCore.setupData()'''
        return bool()


class QHelpEngine(QHelpEngineCore):
    """"""
    def __init__(self, collectionFile, parent = None):
        '''void QHelpEngine.__init__(QString collectionFile, QObject parent = None)'''
    def searchEngine(self):
        '''QHelpSearchEngine QHelpEngine.searchEngine()'''
        return QHelpSearchEngine()
    def indexWidget(self):
        '''QHelpIndexWidget QHelpEngine.indexWidget()'''
        return QHelpIndexWidget()
    def contentWidget(self):
        '''QHelpContentWidget QHelpEngine.contentWidget()'''
        return QHelpContentWidget()
    def indexModel(self):
        '''QHelpIndexModel QHelpEngine.indexModel()'''
        return QHelpIndexModel()
    def contentModel(self):
        '''QHelpContentModel QHelpEngine.contentModel()'''
        return QHelpContentModel()


class QHelpIndexModel(QStringListModel):
    """"""
    indexCreated = pyqtSignal() # void indexCreated() - signal
    indexCreationStarted = pyqtSignal() # void indexCreationStarted() - signal
    def isCreatingIndex(self):
        '''bool QHelpIndexModel.isCreatingIndex()'''
        return bool()
    def linksForKeyword(self, keyword):
        '''dict-of-QString-QUrl QHelpIndexModel.linksForKeyword(QString keyword)'''
        return dict-of-QString-QUrl()
    def filter(self, filter, wildcard = QString()):
        '''QModelIndex QHelpIndexModel.filter(QString filter, QString wildcard = QString())'''
        return QModelIndex()
    def createIndex(self, customFilterName):
        '''void QHelpIndexModel.createIndex(QString customFilterName)'''


class QHelpIndexWidget(QListView):
    """"""
    def activateCurrentItem(self):
        '''void QHelpIndexWidget.activateCurrentItem()'''
    def filterIndices(self, filter, wildcard = QString()):
        '''void QHelpIndexWidget.filterIndices(QString filter, QString wildcard = QString())'''
    linksActivated = pyqtSignal() # void linksActivated(const QMaplt;QString,QUrlgt;amp;,const QStringamp;) - signal
    linkActivated = pyqtSignal() # void linkActivated(const QUrlamp;,const QStringamp;) - signal


class QHelpSearchQuery():
    """"""
    # Enum QHelpSearchQuery.FieldName
    DEFAULT = 0
    FUZZY = 0
    WITHOUT = 0
    PHRASE = 0
    ALL = 0
    ATLEAST = 0

    def __init__(self):
        '''void QHelpSearchQuery.__init__()'''
    def __init__(self, field, wordList):
        '''void QHelpSearchQuery.__init__(QHelpSearchQuery.FieldName field, QStringList wordList)'''
    def __init__(self):
        '''QHelpSearchQuery QHelpSearchQuery.__init__()'''
        return QHelpSearchQuery()


class QHelpSearchEngine(QObject):
    """"""
    def __init__(self, helpEngine, parent = None):
        '''void QHelpSearchEngine.__init__(QHelpEngineCore helpEngine, QObject parent = None)'''
    def hitCount(self):
        '''int QHelpSearchEngine.hitCount()'''
        return int()
    searchingFinished = pyqtSignal() # void searchingFinished(int) - signal
    searchingStarted = pyqtSignal() # void searchingStarted() - signal
    indexingFinished = pyqtSignal() # void indexingFinished() - signal
    indexingStarted = pyqtSignal() # void indexingStarted() - signal
    def cancelSearching(self):
        '''void QHelpSearchEngine.cancelSearching()'''
    def search(self, queryList):
        '''void QHelpSearchEngine.search(list-of-QHelpSearchQuery queryList)'''
    def cancelIndexing(self):
        '''void QHelpSearchEngine.cancelIndexing()'''
    def reindexDocumentation(self):
        '''void QHelpSearchEngine.reindexDocumentation()'''
    def hits(self, start, end):
        '''list-of-tuple-of-QString-QString QHelpSearchEngine.hits(int start, int end)'''
        return [tuple-of-QString-QString()]
    def hitsCount(self):
        '''int QHelpSearchEngine.hitsCount()'''
        return int()
    def resultWidget(self):
        '''QHelpSearchResultWidget QHelpSearchEngine.resultWidget()'''
        return QHelpSearchResultWidget()
    def queryWidget(self):
        '''QHelpSearchQueryWidget QHelpSearchEngine.queryWidget()'''
        return QHelpSearchQueryWidget()
    def query(self):
        '''list-of-QHelpSearchQuery QHelpSearchEngine.query()'''
        return [QHelpSearchQuery()]


class QHelpSearchQueryWidget(QWidget):
    """"""
    def __init__(self, parent = None):
        '''void QHelpSearchQueryWidget.__init__(QWidget parent = None)'''
    search = pyqtSignal() # void search() - signal
    def collapseExtendedSearch(self):
        '''void QHelpSearchQueryWidget.collapseExtendedSearch()'''
    def expandExtendedSearch(self):
        '''void QHelpSearchQueryWidget.expandExtendedSearch()'''
    def setQuery(self, queryList):
        '''void QHelpSearchQueryWidget.setQuery(list-of-QHelpSearchQuery queryList)'''
    def query(self):
        '''list-of-QHelpSearchQuery QHelpSearchQueryWidget.query()'''
        return [QHelpSearchQuery()]


class QHelpSearchResultWidget(QWidget):
    """"""
    requestShowLink = pyqtSignal() # void requestShowLink(const QUrlamp;) - signal
    def linkAt(self, point):
        '''QUrl QHelpSearchResultWidget.linkAt(QPoint point)'''
        return QUrl()


