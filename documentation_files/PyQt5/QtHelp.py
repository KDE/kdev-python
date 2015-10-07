class pyqtSignal():
 def connect(self, targetSignal): pass
 def emit(self, *args): pass
from QtCore import *

from QtWidgets import *

import datetime

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
        '''str QHelpContentItem.title()'''
        return str()
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
        '''void QHelpContentModel.createContents(str customFilterName)'''


class QHelpContentWidget(QTreeView):
    """"""
    linkActivated = pyqtSignal() # void linkActivated(const QUrlamp;) - signal
    def indexOf(self, link):
        '''QModelIndex QHelpContentWidget.indexOf(QUrl link)'''
        return QModelIndex()


class QHelpEngineCore(QObject):
    """"""
    def __init__(self, collectionFile, parent = None):
        '''void QHelpEngineCore.__init__(str collectionFile, QObject parent = None)'''
    readersAboutToBeInvalidated = pyqtSignal() # void readersAboutToBeInvalidated() - signal
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
        '''str QHelpEngineCore.error()'''
        return str()
    def metaData(self, documentationFileName, name):
        '''static QVariant QHelpEngineCore.metaData(str documentationFileName, str name)'''
        return QVariant()
    def setCustomValue(self, key, value):
        '''bool QHelpEngineCore.setCustomValue(str key, QVariant value)'''
        return bool()
    def customValue(self, key, defaultValue = None):
        '''QVariant QHelpEngineCore.customValue(str key, QVariant defaultValue = None)'''
        return QVariant()
    def removeCustomValue(self, key):
        '''bool QHelpEngineCore.removeCustomValue(str key)'''
        return bool()
    def linksForIdentifier(self, id):
        '''dict-of-QString-QUrl QHelpEngineCore.linksForIdentifier(str id)'''
        return {str():QUrl()}
    def fileData(self, url):
        '''QByteArray QHelpEngineCore.fileData(QUrl url)'''
        return QByteArray()
    def findFile(self, url):
        '''QUrl QHelpEngineCore.findFile(QUrl url)'''
        return QUrl()
    def files(self, namespaceName, filterAttributes, extensionFilter = None):
        '''list-of-QUrl QHelpEngineCore.files(str namespaceName, list-of-str filterAttributes, str extensionFilter = '')'''
        return [QUrl()]
    def filterAttributeSets(self, namespaceName):
        '''list-of-QStringList QHelpEngineCore.filterAttributeSets(str namespaceName)'''
        return [strList()]
    def registeredDocumentations(self):
        '''list-of-str QHelpEngineCore.registeredDocumentations()'''
        return [str()]
    def setCurrentFilter(self, filterName):
        '''void QHelpEngineCore.setCurrentFilter(str filterName)'''
    def currentFilter(self):
        '''str QHelpEngineCore.currentFilter()'''
        return str()
    def filterAttributes(self):
        '''list-of-str QHelpEngineCore.filterAttributes()'''
        return [str()]
    def filterAttributes(self, filterName):
        '''list-of-str QHelpEngineCore.filterAttributes(str filterName)'''
        return [str()]
    def addCustomFilter(self, filterName, attributes):
        '''bool QHelpEngineCore.addCustomFilter(str filterName, list-of-str attributes)'''
        return bool()
    def removeCustomFilter(self, filterName):
        '''bool QHelpEngineCore.removeCustomFilter(str filterName)'''
        return bool()
    def customFilters(self):
        '''list-of-str QHelpEngineCore.customFilters()'''
        return [str()]
    def documentationFileName(self, namespaceName):
        '''str QHelpEngineCore.documentationFileName(str namespaceName)'''
        return str()
    def unregisterDocumentation(self, namespaceName):
        '''bool QHelpEngineCore.unregisterDocumentation(str namespaceName)'''
        return bool()
    def registerDocumentation(self, documentationFileName):
        '''bool QHelpEngineCore.registerDocumentation(str documentationFileName)'''
        return bool()
    def namespaceName(self, documentationFileName):
        '''static str QHelpEngineCore.namespaceName(str documentationFileName)'''
        return str()
    def copyCollectionFile(self, fileName):
        '''bool QHelpEngineCore.copyCollectionFile(str fileName)'''
        return bool()
    def setCollectionFile(self, fileName):
        '''void QHelpEngineCore.setCollectionFile(str fileName)'''
    def collectionFile(self):
        '''str QHelpEngineCore.collectionFile()'''
        return str()
    def setupData(self):
        '''bool QHelpEngineCore.setupData()'''
        return bool()


class QHelpEngine(QHelpEngineCore):
    """"""
    def __init__(self, collectionFile, parent = None):
        '''void QHelpEngine.__init__(str collectionFile, QObject parent = None)'''
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
        '''dict-of-QString-QUrl QHelpIndexModel.linksForKeyword(str keyword)'''
        return {str():QUrl()}
    def filter(self, filter, wildcard = None):
        '''QModelIndex QHelpIndexModel.filter(str filter, str wildcard = '')'''
        return QModelIndex()
    def createIndex(self, customFilterName):
        '''void QHelpIndexModel.createIndex(str customFilterName)'''


class QHelpIndexWidget(QListView):
    """"""
    def activateCurrentItem(self):
        '''void QHelpIndexWidget.activateCurrentItem()'''
    def filterIndices(self, filter, wildcard = None):
        '''void QHelpIndexWidget.filterIndices(str filter, str wildcard = '')'''
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
        '''void QHelpSearchQuery.__init__(QHelpSearchQuery.FieldName field, list-of-str wordList)'''
    def __init__(self):
        '''QHelpSearchQuery QHelpSearchQuery.__init__()'''
        return QHelpSearchQuery()


class QHelpSearchEngine(QObject):
    """"""
    def __init__(self, helpEngine, parent = None):
        '''void QHelpSearchEngine.__init__(QHelpEngineCore helpEngine, QObject parent = None)'''
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
        return [tuple-of-str-str()]
    def hitCount(self):
        '''int QHelpSearchEngine.hitCount()'''
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
    def setCompactMode(self, on):
        '''void QHelpSearchQueryWidget.setCompactMode(bool on)'''
    def isCompactMode(self):
        '''bool QHelpSearchQueryWidget.isCompactMode()'''
        return bool()
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


