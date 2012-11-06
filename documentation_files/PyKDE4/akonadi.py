class pyqtSignal():
 def connect(self, targetSignal): pass
 def emit(self, *args): pass
from QtCore import *

class Akonadi():
    """"""
    class EntityTreeViewStateSaver(QObject):
        """"""
        def __init__(self, view):
            '''void Akonadi.EntityTreeViewStateSaver.__init__(QTreeView view)'''
        def restoreState(self, configGroup):
            '''void Akonadi.EntityTreeViewStateSaver.restoreState(KConfigGroup configGroup)'''
        def saveState(self, configGroup):
            '''void Akonadi.EntityTreeViewStateSaver.saveState(KConfigGroup configGroup)'''
    class Attribute():
        """"""
        def __init__(self):
            '''void Akonadi.Attribute.__init__()'''
        def __init__(self):
            '''Akonadi.Attribute Akonadi.Attribute.__init__()'''
            return Akonadi.Attribute()
        def deserialize(self, data):
            '''abstract void Akonadi.Attribute.deserialize(QByteArray data)'''
        def serialized(self):
            '''abstract QByteArray Akonadi.Attribute.serialized()'''
            return QByteArray()
        def type(self):
            '''abstract QByteArray Akonadi.Attribute.type()'''
            return QByteArray()
    class EntityTreeModel(QAbstractItemModel):
        """"""
        # Enum Akonadi.EntityTreeModel.FetchState
        IdleState = 0
        FetchingState = 0
    
        # Enum Akonadi.EntityTreeModel.CollectionFetchStrategy
        FetchNoCollections = 0
        FetchFirstLevelChildCollections = 0
        FetchCollectionsRecursive = 0
        InvisibleCollectionFetch = 0
    
        # Enum Akonadi.EntityTreeModel.ItemPopulationStrategy
        NoItemPopulation = 0
        ImmediatePopulation = 0
        LazyPopulation = 0
    
        # Enum Akonadi.EntityTreeModel.HeaderGroup
        EntityTreeHeaders = 0
        CollectionTreeHeaders = 0
        ItemListHeaders = 0
        UserHeaders = 0
        EndHeaderGroup = 0
    
        # Enum Akonadi.EntityTreeModel.Roles
        ItemIdRole = 0
        ItemRole = 0
        MimeTypeRole = 0
        CollectionIdRole = 0
        CollectionRole = 0
        RemoteIdRole = 0
        CollectionChildOrderRole = 0
        AmazingCompletionRole = 0
        ParentCollectionRole = 0
        ColumnCountRole = 0
        LoadedPartsRole = 0
        AvailablePartsRole = 0
        SessionRole = 0
        CollectionRefRole = 0
        CollectionDerefRole = 0
        PendingCutRole = 0
        EntityUrlRole = 0
        UnreadCountRole = 0
        FetchStateRole = 0
        CollectionSyncProgressRole = 0
        UserRole = 0
        TerminalUserRole = 0
        EndRole = 0
    
        def __init__(self, monitor, parent = None):
            '''void Akonadi.EntityTreeModel.__init__(Akonadi.ChangeRecorder monitor, QObject parent = None)'''
        def setIncludeUnsubscribed(self, show):
            '''void Akonadi.EntityTreeModel.setIncludeUnsubscribed(bool show)'''
        def includeUnsubscribed(self):
            '''bool Akonadi.EntityTreeModel.includeUnsubscribed()'''
            return bool()
        def modelIndexesForItem(self, model, item):
            '''static list-of-QModelIndex Akonadi.EntityTreeModel.modelIndexesForItem(QAbstractItemModel model, Akonadi.Item item)'''
            return [QModelIndex()]
        def modelIndexForCollection(self, model, collection):
            '''static QModelIndex Akonadi.EntityTreeModel.modelIndexForCollection(QAbstractItemModel model, Akonadi.Collection collection)'''
            return QModelIndex()
        def entityMatch(self, item, value, flags):
            '''bool Akonadi.EntityTreeModel.entityMatch(Akonadi.Item item, QVariant value, Qt.MatchFlags flags)'''
            return bool()
        def entityMatch(self, collection, value, flags):
            '''bool Akonadi.EntityTreeModel.entityMatch(Akonadi.Collection collection, QVariant value, Qt.MatchFlags flags)'''
            return bool()
        def entityColumnCount(self, headerGroup):
            '''int Akonadi.EntityTreeModel.entityColumnCount(Akonadi.EntityTreeModel.HeaderGroup headerGroup)'''
            return int()
        def entityHeaderData(self, section, orientation, role, headerGroup):
            '''QVariant Akonadi.EntityTreeModel.entityHeaderData(int section, Qt.Orientation orientation, int role, Akonadi.EntityTreeModel.HeaderGroup headerGroup)'''
            return QVariant()
        def entityData(self, item, column, role = None):
            '''QVariant Akonadi.EntityTreeModel.entityData(Akonadi.Item item, int column, int role = Qt.DisplayRole)'''
            return QVariant()
        def entityData(self, collection, column, role = None):
            '''QVariant Akonadi.EntityTreeModel.entityData(Akonadi.Collection collection, int column, int role = Qt.DisplayRole)'''
            return QVariant()
        def clearAndReset(self):
            '''void Akonadi.EntityTreeModel.clearAndReset()'''
        def match(self, start, role, value, hits = 1, flags = None):
            '''list-of-QModelIndex Akonadi.EntityTreeModel.match(QModelIndex start, int role, QVariant value, int hits = 1, Qt.MatchFlags flags = Qt.MatchFlags(Qt.MatchStartsWith|Qt.MatchWrap))'''
            return [QModelIndex()]
        def hasChildren(self, parent = QModelIndex()):
            '''bool Akonadi.EntityTreeModel.hasChildren(QModelIndex parent = QModelIndex())'''
            return bool()
        def fetchMore(self, parent):
            '''void Akonadi.EntityTreeModel.fetchMore(QModelIndex parent)'''
        def canFetchMore(self, parent):
            '''bool Akonadi.EntityTreeModel.canFetchMore(QModelIndex parent)'''
            return bool()
        def parent(self, index):
            '''QModelIndex Akonadi.EntityTreeModel.parent(QModelIndex index)'''
            return QModelIndex()
        def index(self, row, column, parent = QModelIndex()):
            '''QModelIndex Akonadi.EntityTreeModel.index(int row, int column, QModelIndex parent = QModelIndex())'''
            return QModelIndex()
        def setData(self, index, value, role = None):
            '''bool Akonadi.EntityTreeModel.setData(QModelIndex index, QVariant value, int role = Qt.EditRole)'''
            return bool()
        def dropMimeData(self, data, action, row, column, parent):
            '''bool Akonadi.EntityTreeModel.dropMimeData(QMimeData data, Qt.DropAction action, int row, int column, QModelIndex parent)'''
            return bool()
        def mimeData(self, indexes):
            '''QMimeData Akonadi.EntityTreeModel.mimeData(list-of-QModelIndex indexes)'''
            return QMimeData()
        def supportedDropActions(self):
            '''Qt.DropActions Akonadi.EntityTreeModel.supportedDropActions()'''
            return Qt.DropActions()
        def mimeTypes(self):
            '''QStringList Akonadi.EntityTreeModel.mimeTypes()'''
            return QStringList()
        def flags(self, index):
            '''Qt.ItemFlags Akonadi.EntityTreeModel.flags(QModelIndex index)'''
            return Qt.ItemFlags()
        def headerData(self, section, orientation, role = None):
            '''QVariant Akonadi.EntityTreeModel.headerData(int section, Qt.Orientation orientation, int role = Qt.DisplayRole)'''
            return QVariant()
        def data(self, index, role = None):
            '''QVariant Akonadi.EntityTreeModel.data(QModelIndex index, int role = Qt.DisplayRole)'''
            return QVariant()
        def rowCount(self, parent = QModelIndex()):
            '''int Akonadi.EntityTreeModel.rowCount(QModelIndex parent = QModelIndex())'''
            return int()
        def columnCount(self, parent = QModelIndex()):
            '''int Akonadi.EntityTreeModel.columnCount(QModelIndex parent = QModelIndex())'''
            return int()
        def collectionFetchStrategy(self):
            '''Akonadi.EntityTreeModel.CollectionFetchStrategy Akonadi.EntityTreeModel.collectionFetchStrategy()'''
            return Akonadi.EntityTreeModel.CollectionFetchStrategy()
        def setCollectionFetchStrategy(self, strategy):
            '''void Akonadi.EntityTreeModel.setCollectionFetchStrategy(Akonadi.EntityTreeModel.CollectionFetchStrategy strategy)'''
        def rootCollectionDisplayName(self):
            '''QString Akonadi.EntityTreeModel.rootCollectionDisplayName()'''
            return QString()
        def setRootCollectionDisplayName(self, name):
            '''void Akonadi.EntityTreeModel.setRootCollectionDisplayName(QString name)'''
        def includeRootCollection(self):
            '''bool Akonadi.EntityTreeModel.includeRootCollection()'''
            return bool()
        def setIncludeRootCollection(self, include):
            '''void Akonadi.EntityTreeModel.setIncludeRootCollection(bool include)'''
        def itemPopulationStrategy(self):
            '''Akonadi.EntityTreeModel.ItemPopulationStrategy Akonadi.EntityTreeModel.itemPopulationStrategy()'''
            return Akonadi.EntityTreeModel.ItemPopulationStrategy()
        def setItemPopulationStrategy(self, strategy):
            '''void Akonadi.EntityTreeModel.setItemPopulationStrategy(Akonadi.EntityTreeModel.ItemPopulationStrategy strategy)'''
        def systemEntitiesShown(self):
            '''bool Akonadi.EntityTreeModel.systemEntitiesShown()'''
            return bool()
        def setShowSystemEntities(self, show):
            '''void Akonadi.EntityTreeModel.setShowSystemEntities(bool show)'''
    class SearchCreateJob(Akonadi.Job):
        """"""
        def __init__(self, name, query, parent = None):
            '''void Akonadi.SearchCreateJob.__init__(QString name, QString query, QObject parent = None)'''
        def setQueryLanguage(self, queryLanguage):
            '''void Akonadi.SearchCreateJob.setQueryLanguage(QString queryLanguage)'''
        def doHandleResponse(self, tag, data):
            '''void Akonadi.SearchCreateJob.doHandleResponse(QByteArray tag, QByteArray data)'''
        def createdCollection(self):
            '''Akonadi.Collection Akonadi.SearchCreateJob.createdCollection()'''
            return Akonadi.Collection()
        def doStart(self):
            '''void Akonadi.SearchCreateJob.doStart()'''
    class ItemMonitor():
        """"""
        def __init__(self):
            '''void Akonadi.ItemMonitor.__init__()'''
        def fetchScope(self):
            '''Akonadi.ItemFetchScope Akonadi.ItemMonitor.fetchScope()'''
            return Akonadi.ItemFetchScope()
        def setFetchScope(self, fetchScope):
            '''void Akonadi.ItemMonitor.setFetchScope(Akonadi.ItemFetchScope fetchScope)'''
        def itemRemoved(self):
            '''void Akonadi.ItemMonitor.itemRemoved()'''
        def itemChanged(self, item):
            '''void Akonadi.ItemMonitor.itemChanged(Akonadi.Item item)'''
        def item(self):
            '''Akonadi.Item Akonadi.ItemMonitor.item()'''
            return Akonadi.Item()
        def setItem(self, item):
            '''void Akonadi.ItemMonitor.setItem(Akonadi.Item item)'''
    class AgentTypeDialog(KDialog):
        """"""
        def __init__(self, parent = None):
            '''void Akonadi.AgentTypeDialog.__init__(QWidget parent = None)'''
        def done(self, result):
            '''void Akonadi.AgentTypeDialog.done(int result)'''
        def agentFilterProxyModel(self):
            '''Akonadi.AgentFilterProxyModel Akonadi.AgentTypeDialog.agentFilterProxyModel()'''
            return Akonadi.AgentFilterProxyModel()
        def agentType(self):
            '''Akonadi.AgentType Akonadi.AgentTypeDialog.agentType()'''
            return Akonadi.AgentType()
    class AgentActionManager(QObject):
        """"""
        # Enum Akonadi.AgentActionManager.TextContext
        DialogTitle = 0
        DialogText = 0
        MessageBoxTitle = 0
        MessageBoxText = 0
        MessageBoxAlternativeText = 0
        ErrorMessageTitle = 0
        ErrorMessageText = 0
    
        # Enum Akonadi.AgentActionManager.Type
        CreateAgentInstance = 0
        DeleteAgentInstance = 0
        ConfigureAgentInstance = 0
        LastType = 0
    
        def __init__(self, actionCollection, parent = None):
            '''void Akonadi.AgentActionManager.__init__(KActionCollection actionCollection, QWidget parent = None)'''
        actionStateUpdated = pyqtSignal() # void actionStateUpdated() - signal
        def setContextText(self, type, context, text):
            '''void Akonadi.AgentActionManager.setContextText(Akonadi.AgentActionManager.Type type, Akonadi.AgentActionManager.TextContext context, QString text)'''
        def setContextText(self, type, context, text):
            '''void Akonadi.AgentActionManager.setContextText(Akonadi.AgentActionManager.Type type, Akonadi.AgentActionManager.TextContext context, KLocalizedString text)'''
        def selectedAgentInstances(self):
            '''list-of-Akonadi.AgentInstance Akonadi.AgentActionManager.selectedAgentInstances()'''
            return [Akonadi.AgentInstance()]
        def interceptAction(self, type, intercept = True):
            '''void Akonadi.AgentActionManager.interceptAction(Akonadi.AgentActionManager.Type type, bool intercept = True)'''
        def action(self, type):
            '''KAction Akonadi.AgentActionManager.action(Akonadi.AgentActionManager.Type type)'''
            return KAction()
        def createAllActions(self):
            '''void Akonadi.AgentActionManager.createAllActions()'''
        def createAction(self, type):
            '''KAction Akonadi.AgentActionManager.createAction(Akonadi.AgentActionManager.Type type)'''
            return KAction()
        def setCapabilityFilter(self, capabilities):
            '''void Akonadi.AgentActionManager.setCapabilityFilter(QStringList capabilities)'''
        def setMimeTypeFilter(self, mimeTypes):
            '''void Akonadi.AgentActionManager.setMimeTypeFilter(QStringList mimeTypes)'''
        def setSelectionModel(self, model):
            '''void Akonadi.AgentActionManager.setSelectionModel(QItemSelectionModel model)'''
    class AttributeFactory():
        """"""
        def __init__(self):
            '''void Akonadi.AttributeFactory.__init__()'''
        def createAttribute(self, type):
            '''static Akonadi.Attribute Akonadi.AttributeFactory.createAttribute(QByteArray type)'''
            return Akonadi.Attribute()
    class LinkJob(Akonadi.Job):
        """"""
        def __init__(self, collection, items, parent = None):
            '''void Akonadi.LinkJob.__init__(Akonadi.Collection collection, list-of-Akonadi.Item items, QObject parent = None)'''
        def doStart(self):
            '''void Akonadi.LinkJob.doStart()'''
    class SpecialMailCollectionsRequestJob(Akonadi.SpecialCollectionsRequestJob):
        """"""
        def __init__(self, parent = None):
            '''void Akonadi.SpecialMailCollectionsRequestJob.__init__(QObject parent = None)'''
        def requestCollection(self, type, instance):
            '''void Akonadi.SpecialMailCollectionsRequestJob.requestCollection(Akonadi.SpecialMailCollections.Type type, Akonadi.AgentInstance instance)'''
        def requestDefaultCollection(self, type):
            '''void Akonadi.SpecialMailCollectionsRequestJob.requestDefaultCollection(Akonadi.SpecialMailCollections.Type type)'''
    class EntityDisplayAttribute(Akonadi.Attribute):
        """"""
        def __init__(self):
            '''void Akonadi.EntityDisplayAttribute.__init__()'''
        def setBackgroundColor(self, color):
            '''void Akonadi.EntityDisplayAttribute.setBackgroundColor(QColor color)'''
        def backgroundColor(self):
            '''QColor Akonadi.EntityDisplayAttribute.backgroundColor()'''
            return QColor()
        def activeIconName(self):
            '''QString Akonadi.EntityDisplayAttribute.activeIconName()'''
            return QString()
        def activeIcon(self):
            '''KIcon Akonadi.EntityDisplayAttribute.activeIcon()'''
            return KIcon()
        def setActiveIconName(self, name):
            '''void Akonadi.EntityDisplayAttribute.setActiveIconName(QString name)'''
        def deserialize(self, data):
            '''void Akonadi.EntityDisplayAttribute.deserialize(QByteArray data)'''
        def serialized(self):
            '''QByteArray Akonadi.EntityDisplayAttribute.serialized()'''
            return QByteArray()
        def clone(self):
            '''Akonadi.EntityDisplayAttribute Akonadi.EntityDisplayAttribute.clone()'''
            return Akonadi.EntityDisplayAttribute()
        def type(self):
            '''QByteArray Akonadi.EntityDisplayAttribute.type()'''
            return QByteArray()
        def iconName(self):
            '''QString Akonadi.EntityDisplayAttribute.iconName()'''
            return QString()
        def icon(self):
            '''KIcon Akonadi.EntityDisplayAttribute.icon()'''
            return KIcon()
        def setIconName(self, name):
            '''void Akonadi.EntityDisplayAttribute.setIconName(QString name)'''
        def displayName(self):
            '''QString Akonadi.EntityDisplayAttribute.displayName()'''
            return QString()
        def setDisplayName(self, name):
            '''void Akonadi.EntityDisplayAttribute.setDisplayName(QString name)'''
    class StandardMailActionManager(QObject):
        """"""
        # Enum Akonadi.StandardMailActionManager.Type
        MarkMailAsRead = 0
        MarkMailAsUnread = 0
        MarkMailAsImportant = 0
        MarkMailAsActionItem = 0
        MarkAllMailAsRead = 0
        MarkAllMailAsUnread = 0
        MarkAllMailAsImportant = 0
        MarkAllMailAsActionItem = 0
        MoveToTrash = 0
        MoveAllToTrash = 0
        RemoveDuplicates = 0
        EmptyAllTrash = 0
        EmptyTrash = 0
        LastType = 0
    
        def __init__(self, actionCollection, parent = None):
            '''void Akonadi.StandardMailActionManager.__init__(KActionCollection actionCollection, QWidget parent = None)'''
        def standardActionManager(self):
            '''Akonadi.StandardActionManager Akonadi.StandardMailActionManager.standardActionManager()'''
            return Akonadi.StandardActionManager()
        actionStateUpdated = pyqtSignal() # void actionStateUpdated() - signal
        def setCollectionPropertiesPageNames(self, names):
            '''void Akonadi.StandardMailActionManager.setCollectionPropertiesPageNames(QStringList names)'''
        def setFavoriteSelectionModel(self, selectionModel):
            '''void Akonadi.StandardMailActionManager.setFavoriteSelectionModel(QItemSelectionModel selectionModel)'''
        def setFavoriteCollectionsModel(self, favoritesModel):
            '''void Akonadi.StandardMailActionManager.setFavoriteCollectionsModel(Akonadi.FavoriteCollectionsModel favoritesModel)'''
        def selectedItems(self):
            '''list-of-Akonadi.Item Akonadi.StandardMailActionManager.selectedItems()'''
            return [Akonadi.Item()]
        def selectedCollections(self):
            '''list-of-Akonadi.Collection Akonadi.StandardMailActionManager.selectedCollections()'''
            return [Akonadi.Collection()]
        def interceptAction(self, type, intercept = True):
            '''void Akonadi.StandardMailActionManager.interceptAction(Akonadi.StandardMailActionManager.Type type, bool intercept = True)'''
        def interceptAction(self, type, intercept = True):
            '''void Akonadi.StandardMailActionManager.interceptAction(Akonadi.StandardActionManager.Type type, bool intercept = True)'''
        def setActionText(self, type, text):
            '''void Akonadi.StandardMailActionManager.setActionText(Akonadi.StandardActionManager.Type type, KLocalizedString text)'''
        def action(self, type):
            '''KAction Akonadi.StandardMailActionManager.action(Akonadi.StandardMailActionManager.Type type)'''
            return KAction()
        def action(self, type):
            '''KAction Akonadi.StandardMailActionManager.action(Akonadi.StandardActionManager.Type type)'''
            return KAction()
        def createAllActions(self):
            '''void Akonadi.StandardMailActionManager.createAllActions()'''
        def createAction(self, type):
            '''KAction Akonadi.StandardMailActionManager.createAction(Akonadi.StandardMailActionManager.Type type)'''
            return KAction()
        def createAction(self, type):
            '''KAction Akonadi.StandardMailActionManager.createAction(Akonadi.StandardActionManager.Type type)'''
            return KAction()
        def setItemSelectionModel(self, selectionModel):
            '''void Akonadi.StandardMailActionManager.setItemSelectionModel(QItemSelectionModel selectionModel)'''
        def setCollectionSelectionModel(self, selectionModel):
            '''void Akonadi.StandardMailActionManager.setCollectionSelectionModel(QItemSelectionModel selectionModel)'''
    class ItemModel(QAbstractTableModel):
        """"""
        # Enum Akonadi.ItemModel.Roles
        IdRole = 0
        ItemRole = 0
        MimeTypeRole = 0
        UserRole = 0
    
        # Enum Akonadi.ItemModel.Column
        Id = 0
        RemoteId = 0
        MimeType = 0
    
        def __init__(self, parent = None):
            '''void Akonadi.ItemModel.__init__(QObject parent = None)'''
        def supportedDropActions(self):
            '''Qt.DropActions Akonadi.ItemModel.supportedDropActions()'''
            return Qt.DropActions()
        def session(self):
            '''Akonadi.Session Akonadi.ItemModel.session()'''
            return Akonadi.Session()
        collectionChanged = pyqtSignal() # void collectionChanged(const Akonadi::Collectionamp;) - signal
        def setCollection(self, collection):
            '''void Akonadi.ItemModel.setCollection(Akonadi.Collection collection)'''
        def collection(self):
            '''Akonadi.Collection Akonadi.ItemModel.collection()'''
            return Akonadi.Collection()
        def dropMimeData(self, data, action, row, column, parent):
            '''bool Akonadi.ItemModel.dropMimeData(QMimeData data, Qt.DropAction action, int row, int column, QModelIndex parent)'''
            return bool()
        def indexForItem(self, item, column):
            '''QModelIndex Akonadi.ItemModel.indexForItem(Akonadi.Item item, int column)'''
            return QModelIndex()
        def itemForIndex(self, index):
            '''Akonadi.Item Akonadi.ItemModel.itemForIndex(QModelIndex index)'''
            return Akonadi.Item()
        def fetchScope(self):
            '''Akonadi.ItemFetchScope Akonadi.ItemModel.fetchScope()'''
            return Akonadi.ItemFetchScope()
        def setFetchScope(self, fetchScope):
            '''void Akonadi.ItemModel.setFetchScope(Akonadi.ItemFetchScope fetchScope)'''
        def mimeTypes(self):
            '''QStringList Akonadi.ItemModel.mimeTypes()'''
            return QStringList()
        def mimeData(self, indexes):
            '''QMimeData Akonadi.ItemModel.mimeData(list-of-QModelIndex indexes)'''
            return QMimeData()
        def flags(self, index):
            '''Qt.ItemFlags Akonadi.ItemModel.flags(QModelIndex index)'''
            return Qt.ItemFlags()
        def headerData(self, section, orientation, role = None):
            '''QVariant Akonadi.ItemModel.headerData(int section, Qt.Orientation orientation, int role = Qt.DisplayRole)'''
            return QVariant()
        def rowCount(self, parent = QModelIndex()):
            '''int Akonadi.ItemModel.rowCount(QModelIndex parent = QModelIndex())'''
            return int()
        def data(self, index, role = None):
            '''QVariant Akonadi.ItemModel.data(QModelIndex index, int role = Qt.DisplayRole)'''
            return QVariant()
        def columnCount(self, parent = QModelIndex()):
            '''int Akonadi.ItemModel.columnCount(QModelIndex parent = QModelIndex())'''
            return int()
    class AgentBase():
        """"""
        class Observer():
            """"""
            def __init__(self):
                '''void Akonadi.AgentBase.Observer.__init__()'''
            def __init__(self):
                '''Akonadi.AgentBase.Observer Akonadi.AgentBase.Observer.__init__()'''
                return Akonadi.AgentBase.Observer()
            def collectionRemoved(self, collection):
                '''void Akonadi.AgentBase.Observer.collectionRemoved(Akonadi.Collection collection)'''
            def collectionChanged(self, collection):
                '''void Akonadi.AgentBase.Observer.collectionChanged(Akonadi.Collection collection)'''
            def collectionAdded(self, collection, parent):
                '''void Akonadi.AgentBase.Observer.collectionAdded(Akonadi.Collection collection, Akonadi.Collection parent)'''
            def itemRemoved(self, item):
                '''void Akonadi.AgentBase.Observer.itemRemoved(Akonadi.Item item)'''
            def itemChanged(self, item, partIdentifiers):
                '''void Akonadi.AgentBase.Observer.itemChanged(Akonadi.Item item, list-of-QByteArray partIdentifiers)'''
            def itemAdded(self, item, collection):
                '''void Akonadi.AgentBase.Observer.itemAdded(Akonadi.Item item, Akonadi.Collection collection)'''
    class SpecialCollectionsRequestJob(Akonadi.TransactionSequence):
        """"""
        def __init__(self, collections, parent = None):
            '''void Akonadi.SpecialCollectionsRequestJob.__init__(Akonadi.SpecialCollections collections, QObject parent = None)'''
        def slotResult(self, job):
            '''void Akonadi.SpecialCollectionsRequestJob.slotResult(KJob job)'''
        def doStart(self):
            '''void Akonadi.SpecialCollectionsRequestJob.doStart()'''
        def setIconForTypeMap(self, map):
            '''void Akonadi.SpecialCollectionsRequestJob.setIconForTypeMap(dict-of-QByteArray-QString map)'''
        def setNameForTypeMap(self, map):
            '''void Akonadi.SpecialCollectionsRequestJob.setNameForTypeMap(dict-of-QByteArray-QString map)'''
        def setTypes(self, types):
            '''void Akonadi.SpecialCollectionsRequestJob.setTypes(list-of-QByteArray types)'''
        def setDefaultResourceOptions(self, options):
            '''void Akonadi.SpecialCollectionsRequestJob.setDefaultResourceOptions(dict-of-QString-QVariant options)'''
        def setDefaultResourceType(self, type):
            '''void Akonadi.SpecialCollectionsRequestJob.setDefaultResourceType(QString type)'''
        def collection(self):
            '''Akonadi.Collection Akonadi.SpecialCollectionsRequestJob.collection()'''
            return Akonadi.Collection()
        def requestCollection(self, type, instance):
            '''void Akonadi.SpecialCollectionsRequestJob.requestCollection(QByteArray type, Akonadi.AgentInstance instance)'''
        def requestDefaultCollection(self, type):
            '''void Akonadi.SpecialCollectionsRequestJob.requestDefaultCollection(QByteArray type)'''
    class ETMViewStateSaver(KViewStateSaver):
        """"""
        def __init__(self, parent = None):
            '''void Akonadi.ETMViewStateSaver.__init__(QObject parent = None)'''
        def indexToConfigString(self, index):
            '''QString Akonadi.ETMViewStateSaver.indexToConfigString(QModelIndex index)'''
            return QString()
        def indexFromConfigString(self, model, key):
            '''QModelIndex Akonadi.ETMViewStateSaver.indexFromConfigString(QAbstractItemModel model, QString key)'''
            return QModelIndex()
        def selectItems(self, list):
            '''void Akonadi.ETMViewStateSaver.selectItems(list-of-Akonadi.Item list)'''
        def selectCollections(self, list):
            '''void Akonadi.ETMViewStateSaver.selectCollections(list-of-Akonadi.Collection list)'''
    class EntityOrderProxyModel(QSortFilterProxyModel):
        """"""
        def __init__(self, parent = None):
            '''void Akonadi.EntityOrderProxyModel.__init__(QObject parent = None)'''
        def configString(self, index):
            '''QString Akonadi.EntityOrderProxyModel.configString(QModelIndex index)'''
            return QString()
        def parentConfigString(self, index):
            '''QString Akonadi.EntityOrderProxyModel.parentConfigString(QModelIndex index)'''
            return QString()
        def match(self, start, role, value, hits = 1, flags = None):
            '''list-of-QModelIndex Akonadi.EntityOrderProxyModel.match(QModelIndex start, int role, QVariant value, int hits = 1, Qt.MatchFlags flags = Qt.MatchFlags(Qt.MatchStartsWith|Qt.MatchWrap))'''
            return [QModelIndex()]
        def dropMimeData(self, data, action, row, column, parent):
            '''bool Akonadi.EntityOrderProxyModel.dropMimeData(QMimeData data, Qt.DropAction action, int row, int column, QModelIndex parent)'''
            return bool()
        def lessThan(self, left, right):
            '''bool Akonadi.EntityOrderProxyModel.lessThan(QModelIndex left, QModelIndex right)'''
            return bool()
        def clearTreeOrder(self):
            '''void Akonadi.EntityOrderProxyModel.clearTreeOrder()'''
        def clearOrder(self, index):
            '''void Akonadi.EntityOrderProxyModel.clearOrder(QModelIndex index)'''
        def saveOrder(self):
            '''void Akonadi.EntityOrderProxyModel.saveOrder()'''
        def setOrderConfig(self, group):
            '''void Akonadi.EntityOrderProxyModel.setOrderConfig(KConfigGroup group)'''
    class CollectionStatistics():
        """"""
        def __init__(self):
            '''void Akonadi.CollectionStatistics.__init__()'''
        def __init__(self, other):
            '''void Akonadi.CollectionStatistics.__init__(Akonadi.CollectionStatistics other)'''
        def setSize(self, size):
            '''void Akonadi.CollectionStatistics.setSize(int size)'''
        def size(self):
            '''int Akonadi.CollectionStatistics.size()'''
            return int()
        def setUnreadCount(self, count):
            '''void Akonadi.CollectionStatistics.setUnreadCount(int count)'''
        def unreadCount(self):
            '''int Akonadi.CollectionStatistics.unreadCount()'''
            return int()
        def setCount(self, count):
            '''void Akonadi.CollectionStatistics.setCount(int count)'''
        def count(self):
            '''int Akonadi.CollectionStatistics.count()'''
            return int()
    class RecursiveItemFetchJob(KJob):
        """"""
        def __init__(self, collection, mimeTypes, parent = None):
            '''void Akonadi.RecursiveItemFetchJob.__init__(Akonadi.Collection collection, QStringList mimeTypes, QObject parent = None)'''
        def start(self):
            '''void Akonadi.RecursiveItemFetchJob.start()'''
        def items(self):
            '''list-of-Akonadi.Item Akonadi.RecursiveItemFetchJob.items()'''
            return [Akonadi.Item()]
        def fetchScope(self):
            '''Akonadi.ItemFetchScope Akonadi.RecursiveItemFetchJob.fetchScope()'''
            return Akonadi.ItemFetchScope()
        def setFetchScope(self, fetchScope):
            '''void Akonadi.RecursiveItemFetchJob.setFetchScope(Akonadi.ItemFetchScope fetchScope)'''
    class IndexPolicyAttribute(Akonadi.Attribute):
        """"""
        def __init__(self):
            '''void Akonadi.IndexPolicyAttribute.__init__()'''
        def deserialize(self, data):
            '''void Akonadi.IndexPolicyAttribute.deserialize(QByteArray data)'''
        def serialized(self):
            '''QByteArray Akonadi.IndexPolicyAttribute.serialized()'''
            return QByteArray()
        def clone(self):
            '''Akonadi.Attribute Akonadi.IndexPolicyAttribute.clone()'''
            return Akonadi.Attribute()
        def type(self):
            '''QByteArray Akonadi.IndexPolicyAttribute.type()'''
            return QByteArray()
        def setIndexingEnabled(self, enable):
            '''void Akonadi.IndexPolicyAttribute.setIndexingEnabled(bool enable)'''
        def indexingEnabled(self):
            '''bool Akonadi.IndexPolicyAttribute.indexingEnabled()'''
            return bool()
    class TransactionRollbackJob(Akonadi.Job):
        """"""
        def __init__(self, parent):
            '''void Akonadi.TransactionRollbackJob.__init__(QObject parent)'''
        def doStart(self):
            '''void Akonadi.TransactionRollbackJob.doStart()'''
    class ResourceSynchronizationJob(KJob):
        """"""
        def __init__(self, instance, parent = None):
            '''void Akonadi.ResourceSynchronizationJob.__init__(Akonadi.AgentInstance instance, QObject parent = None)'''
        def setCollectionTreeOnly(self, collectionTreeOnly):
            '''void Akonadi.ResourceSynchronizationJob.setCollectionTreeOnly(bool collectionTreeOnly)'''
        def collectionTreeOnly(self):
            '''bool Akonadi.ResourceSynchronizationJob.collectionTreeOnly()'''
            return bool()
        def start(self):
            '''void Akonadi.ResourceSynchronizationJob.start()'''
        def resource(self):
            '''Akonadi.AgentInstance Akonadi.ResourceSynchronizationJob.resource()'''
            return Akonadi.AgentInstance()
    class AgentBase(QObject):
        """"""
        # Enum Akonadi.AgentBase.Status
        Idle = 0
        Running = 0
        Broken = 0
    
        def __init__(self, id):
            '''void Akonadi.AgentBase.__init__(QString id)'''
        def config(self):
            '''KSharedConfigPtr Akonadi.AgentBase.config()'''
            return KSharedConfigPtr()
        advancedStatus = pyqtSignal() # void advancedStatus(const QVariantMapamp;) - signal
        def componentData(self):
            '''static KComponentData Akonadi.AgentBase.componentData()'''
            return KComponentData()
        def doSetOnline(self, online):
            '''void Akonadi.AgentBase.doSetOnline(bool online)'''
        def setOnline(self, state):
            '''void Akonadi.AgentBase.setOnline(bool state)'''
        def setNeedsNetwork(self, needsNetwork):
            '''void Akonadi.AgentBase.setNeedsNetwork(bool needsNetwork)'''
        def isOnline(self):
            '''bool Akonadi.AgentBase.isOnline()'''
            return bool()
        def changeProcessed(self):
            '''void Akonadi.AgentBase.changeProcessed()'''
        def changeRecorder(self):
            '''Akonadi.ChangeRecorder Akonadi.AgentBase.changeRecorder()'''
            return Akonadi.ChangeRecorder()
        def aboutToQuit(self):
            '''void Akonadi.AgentBase.aboutToQuit()'''
        configurationDialogRejected = pyqtSignal() # void configurationDialogRejected() - signal
        configurationDialogAccepted = pyqtSignal() # void configurationDialogAccepted() - signal
        onlineChanged = pyqtSignal() # void onlineChanged(bool) - signal
        reloadConfiguration = pyqtSignal() # void reloadConfiguration() - signal
        abortRequested = pyqtSignal() # void abortRequested() - signal
        error = pyqtSignal() # void error(const QStringamp;) - signal
        warning = pyqtSignal() # void warning(const QStringamp;) - signal
        percent = pyqtSignal() # void percent(int) - signal
        agentNameChanged = pyqtSignal() # void agentNameChanged(const QStringamp;) - signal
        def agentName(self):
            '''QString Akonadi.AgentBase.agentName()'''
            return QString()
        def setAgentName(self, name):
            '''void Akonadi.AgentBase.setAgentName(QString name)'''
        def registerObserver(self, observer):
            '''void Akonadi.AgentBase.registerObserver(Akonadi.AgentBase.Observer observer)'''
        def cleanup(self):
            '''void Akonadi.AgentBase.cleanup()'''
        def identifier(self):
            '''QString Akonadi.AgentBase.identifier()'''
            return QString()
        def winIdForDialogs(self):
            '''int Akonadi.AgentBase.winIdForDialogs()'''
            return int()
        def configure(self, windowId):
            '''void Akonadi.AgentBase.configure(int windowId)'''
        def progressMessage(self):
            '''QString Akonadi.AgentBase.progressMessage()'''
            return QString()
        def progress(self):
            '''int Akonadi.AgentBase.progress()'''
            return int()
        def statusMessage(self):
            '''QString Akonadi.AgentBase.statusMessage()'''
            return QString()
        def status(self):
            '''int Akonadi.AgentBase.status()'''
            return int()
        status = pyqtSignal() # void status(int,const QStringamp; = QString()) - signal
    class AgentInstanceCreateJob(KJob):
        """"""
        def __init__(self, type, parent = None):
            '''void Akonadi.AgentInstanceCreateJob.__init__(Akonadi.AgentType type, QObject parent = None)'''
        def __init__(self, typeId, parent = None):
            '''void Akonadi.AgentInstanceCreateJob.__init__(QString typeId, QObject parent = None)'''
        def start(self):
            '''void Akonadi.AgentInstanceCreateJob.start()'''
        def instance(self):
            '''Akonadi.AgentInstance Akonadi.AgentInstanceCreateJob.instance()'''
            return Akonadi.AgentInstance()
        def configure(self, parent = None):
            '''void Akonadi.AgentInstanceCreateJob.configure(QWidget parent = None)'''
    class CollectionCopyJob(Akonadi.Job):
        """"""
        def __init__(self, source, target, parent = None):
            '''void Akonadi.CollectionCopyJob.__init__(Akonadi.Collection source, Akonadi.Collection target, QObject parent = None)'''
        def doStart(self):
            '''void Akonadi.CollectionCopyJob.doStart()'''
    class Collection():
        """"""
        class Rights():
            """"""
            def __init__(self):
                '''Akonadi.Collection.Rights Akonadi.Collection.Rights.__init__()'''
                return Akonadi.Collection.Rights()
            def __init__(self):
                '''int Akonadi.Collection.Rights.__init__()'''
                return int()
            def __init__(self):
                '''void Akonadi.Collection.Rights.__init__()'''
            def __bool__(self):
                '''int Akonadi.Collection.Rights.__bool__()'''
                return int()
            def __ne__(self, f):
                '''bool Akonadi.Collection.Rights.__ne__(Akonadi.Collection.Rights f)'''
                return bool()
            def __eq__(self, f):
                '''bool Akonadi.Collection.Rights.__eq__(Akonadi.Collection.Rights f)'''
                return bool()
            def __invert__(self):
                '''Akonadi.Collection.Rights Akonadi.Collection.Rights.__invert__()'''
                return Akonadi.Collection.Rights()
            def __and__(self, mask):
                '''Akonadi.Collection.Rights Akonadi.Collection.Rights.__and__(int mask)'''
                return Akonadi.Collection.Rights()
            def __xor__(self, f):
                '''Akonadi.Collection.Rights Akonadi.Collection.Rights.__xor__(Akonadi.Collection.Rights f)'''
                return Akonadi.Collection.Rights()
            def __xor__(self, f):
                '''Akonadi.Collection.Rights Akonadi.Collection.Rights.__xor__(int f)'''
                return Akonadi.Collection.Rights()
            def __or__(self, f):
                '''Akonadi.Collection.Rights Akonadi.Collection.Rights.__or__(Akonadi.Collection.Rights f)'''
                return Akonadi.Collection.Rights()
            def __or__(self, f):
                '''Akonadi.Collection.Rights Akonadi.Collection.Rights.__or__(int f)'''
                return Akonadi.Collection.Rights()
            def __int__(self):
                '''int Akonadi.Collection.Rights.__int__()'''
                return int()
            def __ixor__(self, f):
                '''Akonadi.Collection.Rights Akonadi.Collection.Rights.__ixor__(Akonadi.Collection.Rights f)'''
                return Akonadi.Collection.Rights()
            def __ior__(self, f):
                '''Akonadi.Collection.Rights Akonadi.Collection.Rights.__ior__(Akonadi.Collection.Rights f)'''
                return Akonadi.Collection.Rights()
            def __iand__(self, mask):
                '''Akonadi.Collection.Rights Akonadi.Collection.Rights.__iand__(int mask)'''
                return Akonadi.Collection.Rights()
    class MessageFlags():
        """"""
        Answered = None # str - member
        Deleted = None # str - member
        Encrypted = None # str - member
        Flagged = None # str - member
        Forwarded = None # str - member
        Ham = None # str - member
        HasAttachment = None # str - member
        HasError = None # str - member
        HasInvitation = None # str - member
        Ignored = None # str - member
        Queued = None # str - member
        Replied = None # str - member
        Seen = None # str - member
        Sent = None # str - member
        Signed = None # str - member
        Spam = None # str - member
        ToAct = None # str - member
        Watched = None # str - member
    class AgentTypeWidget(QWidget):
        """"""
        def __init__(self, parent = None):
            '''void Akonadi.AgentTypeWidget.__init__(QWidget parent = None)'''
        activated = pyqtSignal() # void activated() - signal
        currentChanged = pyqtSignal() # void currentChanged(const Akonadi::AgentTypeamp;,const Akonadi::AgentTypeamp;) - signal
        def agentFilterProxyModel(self):
            '''Akonadi.AgentFilterProxyModel Akonadi.AgentTypeWidget.agentFilterProxyModel()'''
            return Akonadi.AgentFilterProxyModel()
        def currentAgentType(self):
            '''Akonadi.AgentType Akonadi.AgentTypeWidget.currentAgentType()'''
            return Akonadi.AgentType()
    class TrashSettings():
        """"""
        def getTrashCollection(self, resource):
            '''static Akonadi.Collection Akonadi.TrashSettings.getTrashCollection(QString resource)'''
            return Akonadi.Collection()
        def setTrashCollection(self, resource, collection):
            '''static void Akonadi.TrashSettings.setTrashCollection(QString resource, Akonadi.Collection collection)'''
    class AgentSearchInterface():
        """"""
        def __init__(self):
            '''void Akonadi.AgentSearchInterface.__init__()'''
        def __init__(self):
            '''Akonadi.AgentSearchInterface Akonadi.AgentSearchInterface.__init__()'''
            return Akonadi.AgentSearchInterface()
        def removeSearch(self, resultCollection):
            '''abstract void Akonadi.AgentSearchInterface.removeSearch(Akonadi.Collection resultCollection)'''
        def addSearch(self, query, queryLanguage, resultCollection):
            '''abstract void Akonadi.AgentSearchInterface.addSearch(QString query, QString queryLanguage, Akonadi.Collection resultCollection)'''
    class TransactionBeginJob(Akonadi.Job):
        """"""
        def __init__(self, parent):
            '''void Akonadi.TransactionBeginJob.__init__(QObject parent)'''
        def doStart(self):
            '''void Akonadi.TransactionBeginJob.doStart()'''
    class CollectionAttributesSynchronizationJob(KJob):
        """"""
        def __init__(self, collection, parent = None):
            '''void Akonadi.CollectionAttributesSynchronizationJob.__init__(Akonadi.Collection collection, QObject parent = None)'''
        def start(self):
            '''void Akonadi.CollectionAttributesSynchronizationJob.start()'''
    class AgentManager(QObject):
        """"""
        instanceOnline = pyqtSignal() # void instanceOnline(const Akonadi::AgentInstanceamp;,bool) - signal
        instanceWarning = pyqtSignal() # void instanceWarning(const Akonadi::AgentInstanceamp;,const QStringamp;) - signal
        instanceError = pyqtSignal() # void instanceError(const Akonadi::AgentInstanceamp;,const QStringamp;) - signal
        instanceNameChanged = pyqtSignal() # void instanceNameChanged(const Akonadi::AgentInstanceamp;) - signal
        instanceProgressChanged = pyqtSignal() # void instanceProgressChanged(const Akonadi::AgentInstanceamp;) - signal
        instanceStatusChanged = pyqtSignal() # void instanceStatusChanged(const Akonadi::AgentInstanceamp;) - signal
        instanceRemoved = pyqtSignal() # void instanceRemoved(const Akonadi::AgentInstanceamp;) - signal
        instanceAdded = pyqtSignal() # void instanceAdded(const Akonadi::AgentInstanceamp;) - signal
        typeRemoved = pyqtSignal() # void typeRemoved(const Akonadi::AgentTypeamp;) - signal
        typeAdded = pyqtSignal() # void typeAdded(const Akonadi::AgentTypeamp;) - signal
        def synchronizeCollection(self, collection):
            '''void Akonadi.AgentManager.synchronizeCollection(Akonadi.Collection collection)'''
        def synchronizeCollection(self, collection, recursive):
            '''void Akonadi.AgentManager.synchronizeCollection(Akonadi.Collection collection, bool recursive)'''
        def removeInstance(self, instance):
            '''void Akonadi.AgentManager.removeInstance(Akonadi.AgentInstance instance)'''
        def instance(self, identifier):
            '''Akonadi.AgentInstance Akonadi.AgentManager.instance(QString identifier)'''
            return Akonadi.AgentInstance()
        def instances(self):
            '''list-of-Akonadi.AgentInstance Akonadi.AgentManager.instances()'''
            return [Akonadi.AgentInstance()]
        def type(self, identifier):
            '''Akonadi.AgentType Akonadi.AgentManager.type(QString identifier)'''
            return Akonadi.AgentType()
        def types(self):
            '''list-of-Akonadi.AgentType Akonadi.AgentManager.types()'''
            return [Akonadi.AgentType()]
        def self(self):
            '''static Akonadi.AgentManager Akonadi.AgentManager.self()'''
            return Akonadi.AgentManager()
    class EntityMimeTypeFilterModel(QSortFilterProxyModel):
        """"""
        def __init__(self, parent = None):
            '''void Akonadi.EntityMimeTypeFilterModel.__init__(QObject parent = None)'''
        def filterAcceptsColumn(self, sourceColumn, sourceParent):
            '''bool Akonadi.EntityMimeTypeFilterModel.filterAcceptsColumn(int sourceColumn, QModelIndex sourceParent)'''
            return bool()
        def filterAcceptsRow(self, sourceRow, sourceParent):
            '''bool Akonadi.EntityMimeTypeFilterModel.filterAcceptsRow(int sourceRow, QModelIndex sourceParent)'''
            return bool()
        def columnCount(self, parent = QModelIndex()):
            '''int Akonadi.EntityMimeTypeFilterModel.columnCount(QModelIndex parent = QModelIndex())'''
            return int()
        def match(self, start, role, value, hits = 1, flags = None):
            '''list-of-QModelIndex Akonadi.EntityMimeTypeFilterModel.match(QModelIndex start, int role, QVariant value, int hits = 1, Qt.MatchFlags flags = Qt.MatchFlags(Qt.MatchStartsWith|Qt.MatchWrap))'''
            return [QModelIndex()]
        def canFetchMore(self, parent):
            '''bool Akonadi.EntityMimeTypeFilterModel.canFetchMore(QModelIndex parent)'''
            return bool()
        def hasChildren(self, parent = QModelIndex()):
            '''bool Akonadi.EntityMimeTypeFilterModel.hasChildren(QModelIndex parent = QModelIndex())'''
            return bool()
        def headerData(self, section, orientation, role = None):
            '''QVariant Akonadi.EntityMimeTypeFilterModel.headerData(int section, Qt.Orientation orientation, int role = Qt.DisplayRole)'''
            return QVariant()
        def setHeaderGroup(self, headerGroup):
            '''void Akonadi.EntityMimeTypeFilterModel.setHeaderGroup(Akonadi.EntityTreeModel.HeaderGroup headerGroup)'''
        def clearFilters(self):
            '''void Akonadi.EntityMimeTypeFilterModel.clearFilters()'''
        def addMimeTypeExclusionFilter(self, mimeType):
            '''void Akonadi.EntityMimeTypeFilterModel.addMimeTypeExclusionFilter(QString mimeType)'''
        def addMimeTypeInclusionFilter(self, mimeType):
            '''void Akonadi.EntityMimeTypeFilterModel.addMimeTypeInclusionFilter(QString mimeType)'''
        def mimeTypeExclusionFilters(self):
            '''QStringList Akonadi.EntityMimeTypeFilterModel.mimeTypeExclusionFilters()'''
            return QStringList()
        def mimeTypeInclusionFilters(self):
            '''QStringList Akonadi.EntityMimeTypeFilterModel.mimeTypeInclusionFilters()'''
            return QStringList()
        def addMimeTypeExclusionFilters(self, mimeTypes):
            '''void Akonadi.EntityMimeTypeFilterModel.addMimeTypeExclusionFilters(QStringList mimeTypes)'''
        def addMimeTypeInclusionFilters(self, mimeTypes):
            '''void Akonadi.EntityMimeTypeFilterModel.addMimeTypeInclusionFilters(QStringList mimeTypes)'''
    class CollectionDialog():
        """"""
        class CollectionDialogOptions():
            """"""
            def __init__(self):
                '''Akonadi.CollectionDialog.CollectionDialogOptions Akonadi.CollectionDialog.CollectionDialogOptions.__init__()'''
                return Akonadi.CollectionDialog.CollectionDialogOptions()
            def __init__(self):
                '''int Akonadi.CollectionDialog.CollectionDialogOptions.__init__()'''
                return int()
            def __init__(self):
                '''void Akonadi.CollectionDialog.CollectionDialogOptions.__init__()'''
            def __bool__(self):
                '''int Akonadi.CollectionDialog.CollectionDialogOptions.__bool__()'''
                return int()
            def __ne__(self, f):
                '''bool Akonadi.CollectionDialog.CollectionDialogOptions.__ne__(Akonadi.CollectionDialog.CollectionDialogOptions f)'''
                return bool()
            def __eq__(self, f):
                '''bool Akonadi.CollectionDialog.CollectionDialogOptions.__eq__(Akonadi.CollectionDialog.CollectionDialogOptions f)'''
                return bool()
            def __invert__(self):
                '''Akonadi.CollectionDialog.CollectionDialogOptions Akonadi.CollectionDialog.CollectionDialogOptions.__invert__()'''
                return Akonadi.CollectionDialog.CollectionDialogOptions()
            def __and__(self, mask):
                '''Akonadi.CollectionDialog.CollectionDialogOptions Akonadi.CollectionDialog.CollectionDialogOptions.__and__(int mask)'''
                return Akonadi.CollectionDialog.CollectionDialogOptions()
            def __xor__(self, f):
                '''Akonadi.CollectionDialog.CollectionDialogOptions Akonadi.CollectionDialog.CollectionDialogOptions.__xor__(Akonadi.CollectionDialog.CollectionDialogOptions f)'''
                return Akonadi.CollectionDialog.CollectionDialogOptions()
            def __xor__(self, f):
                '''Akonadi.CollectionDialog.CollectionDialogOptions Akonadi.CollectionDialog.CollectionDialogOptions.__xor__(int f)'''
                return Akonadi.CollectionDialog.CollectionDialogOptions()
            def __or__(self, f):
                '''Akonadi.CollectionDialog.CollectionDialogOptions Akonadi.CollectionDialog.CollectionDialogOptions.__or__(Akonadi.CollectionDialog.CollectionDialogOptions f)'''
                return Akonadi.CollectionDialog.CollectionDialogOptions()
            def __or__(self, f):
                '''Akonadi.CollectionDialog.CollectionDialogOptions Akonadi.CollectionDialog.CollectionDialogOptions.__or__(int f)'''
                return Akonadi.CollectionDialog.CollectionDialogOptions()
            def __int__(self):
                '''int Akonadi.CollectionDialog.CollectionDialogOptions.__int__()'''
                return int()
            def __ixor__(self, f):
                '''Akonadi.CollectionDialog.CollectionDialogOptions Akonadi.CollectionDialog.CollectionDialogOptions.__ixor__(Akonadi.CollectionDialog.CollectionDialogOptions f)'''
                return Akonadi.CollectionDialog.CollectionDialogOptions()
            def __ior__(self, f):
                '''Akonadi.CollectionDialog.CollectionDialogOptions Akonadi.CollectionDialog.CollectionDialogOptions.__ior__(Akonadi.CollectionDialog.CollectionDialogOptions f)'''
                return Akonadi.CollectionDialog.CollectionDialogOptions()
            def __iand__(self, mask):
                '''Akonadi.CollectionDialog.CollectionDialogOptions Akonadi.CollectionDialog.CollectionDialogOptions.__iand__(int mask)'''
                return Akonadi.CollectionDialog.CollectionDialogOptions()
    class CollectionRequester(KHBox):
        """"""
        def __init__(self, parent = None):
            '''void Akonadi.CollectionRequester.__init__(QWidget parent = None)'''
        def __init__(self, collection, parent = None):
            '''void Akonadi.CollectionRequester.__init__(Akonadi.Collection collection, QWidget parent = None)'''
        def changeCollectionDialogOptions(self, options):
            '''void Akonadi.CollectionRequester.changeCollectionDialogOptions(Akonadi.CollectionDialog.CollectionDialogOptions options)'''
        collectionChanged = pyqtSignal() # void collectionChanged(const Akonadi::Collectionamp;) - signal
        def accessRightsFilter(self):
            '''Akonadi.Collection.Rights Akonadi.CollectionRequester.accessRightsFilter()'''
            return Akonadi.Collection.Rights()
        def setAccessRightsFilter(self, rights):
            '''void Akonadi.CollectionRequester.setAccessRightsFilter(Akonadi.Collection.Rights rights)'''
        def setCollection(self, collection):
            '''void Akonadi.CollectionRequester.setCollection(Akonadi.Collection collection)'''
        def mimeTypeFilter(self):
            '''QStringList Akonadi.CollectionRequester.mimeTypeFilter()'''
            return QStringList()
        def setMimeTypeFilter(self, mimeTypes):
            '''void Akonadi.CollectionRequester.setMimeTypeFilter(QStringList mimeTypes)'''
        def collection(self):
            '''Akonadi.Collection Akonadi.CollectionRequester.collection()'''
            return Akonadi.Collection()
    class AddressAttribute(Akonadi.Attribute):
        """"""
        def __init__(self, from_ = QString(), to = QStringList(), cc = QStringList(), bcc = QStringList()):
            '''void Akonadi.AddressAttribute.__init__(QString from = QString(), QStringList to = QStringList(), QStringList cc = QStringList(), QStringList bcc = QStringList())'''
        def __init__(self):
            '''Akonadi.AddressAttribute Akonadi.AddressAttribute.__init__()'''
            return Akonadi.AddressAttribute()
        def setBcc(self, bcc):
            '''void Akonadi.AddressAttribute.setBcc(QStringList bcc)'''
        def bcc(self):
            '''QStringList Akonadi.AddressAttribute.bcc()'''
            return QStringList()
        def setCc(self, cc):
            '''void Akonadi.AddressAttribute.setCc(QStringList cc)'''
        def cc(self):
            '''QStringList Akonadi.AddressAttribute.cc()'''
            return QStringList()
        def setTo(self, to):
            '''void Akonadi.AddressAttribute.setTo(QStringList to)'''
        def to(self):
            '''QStringList Akonadi.AddressAttribute.to()'''
            return QStringList()
        def setFrom(self, from_):
            '''void Akonadi.AddressAttribute.setFrom(QString from)'''
        def from_(self):
            '''QString Akonadi.AddressAttribute.from()'''
            return QString()
        def deserialize(self, data):
            '''void Akonadi.AddressAttribute.deserialize(QByteArray data)'''
        def serialized(self):
            '''QByteArray Akonadi.AddressAttribute.serialized()'''
            return QByteArray()
        def type(self):
            '''QByteArray Akonadi.AddressAttribute.type()'''
            return QByteArray()
        def clone(self):
            '''Akonadi.AddressAttribute Akonadi.AddressAttribute.clone()'''
            return Akonadi.AddressAttribute()
    class ItemCopyJob(Akonadi.Job):
        """"""
        def __init__(self, item, target, parent = None):
            '''void Akonadi.ItemCopyJob.__init__(Akonadi.Item item, Akonadi.Collection target, QObject parent = None)'''
        def __init__(self, items, target, parent = None):
            '''void Akonadi.ItemCopyJob.__init__(list-of-Akonadi.Item items, Akonadi.Collection target, QObject parent = None)'''
        def doStart(self):
            '''void Akonadi.ItemCopyJob.doStart()'''
    class MessageStatus():
        """"""
        def __init__(self):
            '''void Akonadi.MessageStatus.__init__()'''
        def __init__(self):
            '''Akonadi.MessageStatus Akonadi.MessageStatus.__init__()'''
            return Akonadi.MessageStatus()
        def statusHasError(self):
            '''static Akonadi.MessageStatus Akonadi.MessageStatus.statusHasError()'''
            return Akonadi.MessageStatus()
        def statusEncrypted(self):
            '''static Akonadi.MessageStatus Akonadi.MessageStatus.statusEncrypted()'''
            return Akonadi.MessageStatus()
        def statusSigned(self):
            '''static Akonadi.MessageStatus Akonadi.MessageStatus.statusSigned()'''
            return Akonadi.MessageStatus()
        def statusHasInvitation(self):
            '''static Akonadi.MessageStatus Akonadi.MessageStatus.statusHasInvitation()'''
            return Akonadi.MessageStatus()
        def statusHasAttachment(self):
            '''static Akonadi.MessageStatus Akonadi.MessageStatus.statusHasAttachment()'''
            return Akonadi.MessageStatus()
        def statusHam(self):
            '''static Akonadi.MessageStatus Akonadi.MessageStatus.statusHam()'''
            return Akonadi.MessageStatus()
        def statusSpam(self):
            '''static Akonadi.MessageStatus Akonadi.MessageStatus.statusSpam()'''
            return Akonadi.MessageStatus()
        def statusToAct(self):
            '''static Akonadi.MessageStatus Akonadi.MessageStatus.statusToAct()'''
            return Akonadi.MessageStatus()
        def statusIgnored(self):
            '''static Akonadi.MessageStatus Akonadi.MessageStatus.statusIgnored()'''
            return Akonadi.MessageStatus()
        def statusWatched(self):
            '''static Akonadi.MessageStatus Akonadi.MessageStatus.statusWatched()'''
            return Akonadi.MessageStatus()
        def statusImportant(self):
            '''static Akonadi.MessageStatus Akonadi.MessageStatus.statusImportant()'''
            return Akonadi.MessageStatus()
        def statusSent(self):
            '''static Akonadi.MessageStatus Akonadi.MessageStatus.statusSent()'''
            return Akonadi.MessageStatus()
        def statusQueued(self):
            '''static Akonadi.MessageStatus Akonadi.MessageStatus.statusQueued()'''
            return Akonadi.MessageStatus()
        def statusForwarded(self):
            '''static Akonadi.MessageStatus Akonadi.MessageStatus.statusForwarded()'''
            return Akonadi.MessageStatus()
        def statusReplied(self):
            '''static Akonadi.MessageStatus Akonadi.MessageStatus.statusReplied()'''
            return Akonadi.MessageStatus()
        def statusDeleted(self):
            '''static Akonadi.MessageStatus Akonadi.MessageStatus.statusDeleted()'''
            return Akonadi.MessageStatus()
        def statusRead(self):
            '''static Akonadi.MessageStatus Akonadi.MessageStatus.statusRead()'''
            return Akonadi.MessageStatus()
        def statusUnread(self):
            '''static Akonadi.MessageStatus Akonadi.MessageStatus.statusUnread()'''
            return Akonadi.MessageStatus()
        def setStatusFromFlags(self, flags):
            '''void Akonadi.MessageStatus.setStatusFromFlags(list-of-QByteArray flags)'''
        def statusFlags(self):
            '''list-of-QByteArray Akonadi.MessageStatus.statusFlags()'''
            return [QByteArray()]
        def setStatusFromStr(self, aStr):
            '''void Akonadi.MessageStatus.setStatusFromStr(QString aStr)'''
        def statusStr(self):
            '''QString Akonadi.MessageStatus.statusStr()'''
            return QString()
        def fromQInt32(self, status):
            '''void Akonadi.MessageStatus.fromQInt32(int status)'''
        def toQInt32(self):
            '''int Akonadi.MessageStatus.toQInt32()'''
            return int()
        def setHasError(self, value = True):
            '''void Akonadi.MessageStatus.setHasError(bool value = True)'''
        def setEncrypted(self, value = True):
            '''void Akonadi.MessageStatus.setEncrypted(bool value = True)'''
        def setSigned(self, value = True):
            '''void Akonadi.MessageStatus.setSigned(bool value = True)'''
        def setHasInvitation(self, hasInvitation = True):
            '''void Akonadi.MessageStatus.setHasInvitation(bool hasInvitation = True)'''
        def setHasAttachment(self, hasAttachment = True):
            '''void Akonadi.MessageStatus.setHasAttachment(bool hasAttachment = True)'''
        def setHam(self, ham = True):
            '''void Akonadi.MessageStatus.setHam(bool ham = True)'''
        def setSpam(self, spam = True):
            '''void Akonadi.MessageStatus.setSpam(bool spam = True)'''
        def setToAct(self, toAct = True):
            '''void Akonadi.MessageStatus.setToAct(bool toAct = True)'''
        def setIgnored(self, ignored = True):
            '''void Akonadi.MessageStatus.setIgnored(bool ignored = True)'''
        def setWatched(self, watched = True):
            '''void Akonadi.MessageStatus.setWatched(bool watched = True)'''
        def setImportant(self, important = True):
            '''void Akonadi.MessageStatus.setImportant(bool important = True)'''
        def setSent(self, sent = True):
            '''void Akonadi.MessageStatus.setSent(bool sent = True)'''
        def setQueued(self, queued = True):
            '''void Akonadi.MessageStatus.setQueued(bool queued = True)'''
        def setForwarded(self, forwarded = True):
            '''void Akonadi.MessageStatus.setForwarded(bool forwarded = True)'''
        def setReplied(self, replied = True):
            '''void Akonadi.MessageStatus.setReplied(bool replied = True)'''
        def setDeleted(self, deleted = True):
            '''void Akonadi.MessageStatus.setDeleted(bool deleted = True)'''
        def setRead(self, read = True):
            '''void Akonadi.MessageStatus.setRead(bool read = True)'''
        def hasError(self):
            '''bool Akonadi.MessageStatus.hasError()'''
            return bool()
        def isEncrypted(self):
            '''bool Akonadi.MessageStatus.isEncrypted()'''
            return bool()
        def isSigned(self):
            '''bool Akonadi.MessageStatus.isSigned()'''
            return bool()
        def hasInvitation(self):
            '''bool Akonadi.MessageStatus.hasInvitation()'''
            return bool()
        def hasAttachment(self):
            '''bool Akonadi.MessageStatus.hasAttachment()'''
            return bool()
        def isHam(self):
            '''bool Akonadi.MessageStatus.isHam()'''
            return bool()
        def isSpam(self):
            '''bool Akonadi.MessageStatus.isSpam()'''
            return bool()
        def isToAct(self):
            '''bool Akonadi.MessageStatus.isToAct()'''
            return bool()
        def isIgnored(self):
            '''bool Akonadi.MessageStatus.isIgnored()'''
            return bool()
        def isWatched(self):
            '''bool Akonadi.MessageStatus.isWatched()'''
            return bool()
        def isImportant(self):
            '''bool Akonadi.MessageStatus.isImportant()'''
            return bool()
        def isSent(self):
            '''bool Akonadi.MessageStatus.isSent()'''
            return bool()
        def isQueued(self):
            '''bool Akonadi.MessageStatus.isQueued()'''
            return bool()
        def isForwarded(self):
            '''bool Akonadi.MessageStatus.isForwarded()'''
            return bool()
        def isReplied(self):
            '''bool Akonadi.MessageStatus.isReplied()'''
            return bool()
        def isDeleted(self):
            '''bool Akonadi.MessageStatus.isDeleted()'''
            return bool()
        def isRead(self):
            '''bool Akonadi.MessageStatus.isRead()'''
            return bool()
        def isOfUnknownStatus(self):
            '''bool Akonadi.MessageStatus.isOfUnknownStatus()'''
            return bool()
        def toggle(self, other):
            '''void Akonadi.MessageStatus.toggle(Akonadi.MessageStatus other)'''
        def set(self, other):
            '''void Akonadi.MessageStatus.set(Akonadi.MessageStatus other)'''
        def clear(self):
            '''void Akonadi.MessageStatus.clear()'''
        def __and__(self, other):
            '''bool Akonadi.MessageStatus.__and__(Akonadi.MessageStatus other)'''
            return bool()
        def __ne__(self, other):
            '''bool Akonadi.MessageStatus.__ne__(Akonadi.MessageStatus other)'''
            return bool()
        def __eq__(self, other):
            '''bool Akonadi.MessageStatus.__eq__(Akonadi.MessageStatus other)'''
            return bool()
    class AgentTypeModel(QAbstractItemModel):
        """"""
        # Enum Akonadi.AgentTypeModel.Roles
        TypeRole = 0
        IdentifierRole = 0
        DescriptionRole = 0
        MimeTypesRole = 0
        CapabilitiesRole = 0
        UserRole = 0
    
        def __init__(self, parent = None):
            '''void Akonadi.AgentTypeModel.__init__(QObject parent = None)'''
        def flags(self, index):
            '''Qt.ItemFlags Akonadi.AgentTypeModel.flags(QModelIndex index)'''
            return Qt.ItemFlags()
        def parent(self, index):
            '''QModelIndex Akonadi.AgentTypeModel.parent(QModelIndex index)'''
            return QModelIndex()
        def index(self, row, column, parent = QModelIndex()):
            '''QModelIndex Akonadi.AgentTypeModel.index(int row, int column, QModelIndex parent = QModelIndex())'''
            return QModelIndex()
        def data(self, index, role = None):
            '''QVariant Akonadi.AgentTypeModel.data(QModelIndex index, int role = Qt.DisplayRole)'''
            return QVariant()
        def rowCount(self, parent = QModelIndex()):
            '''int Akonadi.AgentTypeModel.rowCount(QModelIndex parent = QModelIndex())'''
            return int()
        def columnCount(self, parent = QModelIndex()):
            '''int Akonadi.AgentTypeModel.columnCount(QModelIndex parent = QModelIndex())'''
            return int()
    class ResourceBase(Akonadi.AgentBase):
        """"""
        # Enum Akonadi.ResourceBase.SchedulePriority
        Prepend = 0
        AfterChangeReplay = 0
        Append = 0
    
        def __init__(self, id):
            '''void Akonadi.ResourceBase.__init__(QString id)'''
        def dumpSchedulerToString(self):
            '''QString Akonadi.ResourceBase.dumpSchedulerToString()'''
            return QString()
        def dumpNotificationListToString(self):
            '''QString Akonadi.ResourceBase.dumpNotificationListToString()'''
            return QString()
        def invalidateCache(self, collection):
            '''void Akonadi.ResourceBase.invalidateCache(Akonadi.Collection collection)'''
        collectionTreeSynchronized = pyqtSignal() # void collectionTreeSynchronized() - signal
        def setAutomaticProgressReporting(self, enabled):
            '''void Akonadi.ResourceBase.setAutomaticProgressReporting(bool enabled)'''
        def synchronizeCollectionAttributes(self, id):
            '''void Akonadi.ResourceBase.synchronizeCollectionAttributes(int id)'''
        def setItemSynchronizationFetchScope(self, fetchScope):
            '''void Akonadi.ResourceBase.setItemSynchronizationFetchScope(Akonadi.ItemFetchScope fetchScope)'''
        def setItemTransactionMode(self, mode):
            '''void Akonadi.ResourceBase.setItemTransactionMode(Akonadi.ItemSync.TransactionMode mode)'''
        def collectionAttributesRetrieved(self, collection):
            '''void Akonadi.ResourceBase.collectionAttributesRetrieved(Akonadi.Collection collection)'''
        def abortActivity(self):
            '''void Akonadi.ResourceBase.abortActivity()'''
        def retrieveCollectionAttributes(self, collection):
            '''void Akonadi.ResourceBase.retrieveCollectionAttributes(Akonadi.Collection collection)'''
        attributesSynchronized = pyqtSignal() # void attributesSynchronized(qlonglong) - signal
        def taskDone(self):
            '''void Akonadi.ResourceBase.taskDone()'''
        def scheduleCustomTask(self, receiver, method, argument, priority):
            '''void Akonadi.ResourceBase.scheduleCustomTask(QObject receiver, str method, QVariant argument, Akonadi.ResourceBase.SchedulePriority priority)'''
        def setHierarchicalRemoteIdentifiersEnabled(self, enable):
            '''void Akonadi.ResourceBase.setHierarchicalRemoteIdentifiersEnabled(bool enable)'''
        def doSetOnline(self, online):
            '''void Akonadi.ResourceBase.doSetOnline(bool online)'''
        def deferTask(self):
            '''void Akonadi.ResourceBase.deferTask()'''
        def cancelTask(self):
            '''void Akonadi.ResourceBase.cancelTask()'''
        def cancelTask(self, error):
            '''void Akonadi.ResourceBase.cancelTask(QString error)'''
        def synchronizeCollectionTree(self):
            '''void Akonadi.ResourceBase.synchronizeCollectionTree()'''
        def synchronizeCollection(self, id):
            '''void Akonadi.ResourceBase.synchronizeCollection(int id)'''
        def synchronizeCollection(self, id, recursive):
            '''void Akonadi.ResourceBase.synchronizeCollection(int id, bool recursive)'''
        def synchronize(self):
            '''void Akonadi.ResourceBase.synchronize()'''
        def currentItem(self):
            '''Akonadi.Item Akonadi.ResourceBase.currentItem()'''
            return Akonadi.Item()
        def currentCollection(self):
            '''Akonadi.Collection Akonadi.ResourceBase.currentCollection()'''
            return Akonadi.Collection()
        def clearCache(self):
            '''void Akonadi.ResourceBase.clearCache()'''
        def itemsRetrievalDone(self):
            '''void Akonadi.ResourceBase.itemsRetrievalDone()'''
        def itemsRetrievedIncremental(self, changedItems, removedItems):
            '''void Akonadi.ResourceBase.itemsRetrievedIncremental(list-of-Akonadi.Item changedItems, list-of-Akonadi.Item removedItems)'''
        def setItemStreamingEnabled(self, enable):
            '''void Akonadi.ResourceBase.setItemStreamingEnabled(bool enable)'''
        def setTotalItems(self, amount):
            '''void Akonadi.ResourceBase.setTotalItems(int amount)'''
        def itemsRetrieved(self, items):
            '''void Akonadi.ResourceBase.itemsRetrieved(list-of-Akonadi.Item items)'''
        def collectionsRetrievalDone(self):
            '''void Akonadi.ResourceBase.collectionsRetrievalDone()'''
        def setCollectionStreamingEnabled(self, enable):
            '''void Akonadi.ResourceBase.setCollectionStreamingEnabled(bool enable)'''
        def collectionsRetrievedIncremental(self, changedCollections, removedCollections):
            '''void Akonadi.ResourceBase.collectionsRetrievedIncremental(list-of-Akonadi.Collection changedCollections, list-of-Akonadi.Collection removedCollections)'''
        def collectionsRetrieved(self, collections):
            '''void Akonadi.ResourceBase.collectionsRetrieved(list-of-Akonadi.Collection collections)'''
        def changeCommitted(self, item):
            '''void Akonadi.ResourceBase.changeCommitted(Akonadi.Item item)'''
        def changeCommitted(self, collection):
            '''void Akonadi.ResourceBase.changeCommitted(Akonadi.Collection collection)'''
        def itemRetrieved(self, item):
            '''void Akonadi.ResourceBase.itemRetrieved(Akonadi.Item item)'''
        def retrieveItem(self, item, parts):
            '''abstract bool Akonadi.ResourceBase.retrieveItem(Akonadi.Item item, list-of-QByteArray parts)'''
            return bool()
        def retrieveItems(self, collection):
            '''abstract void Akonadi.ResourceBase.retrieveItems(Akonadi.Collection collection)'''
        def retrieveCollections(self):
            '''abstract void Akonadi.ResourceBase.retrieveCollections()'''
        synchronized = pyqtSignal() # void synchronized() - signal
        nameChanged = pyqtSignal() # void nameChanged(const QStringamp;) - signal
        def name(self):
            '''QString Akonadi.ResourceBase.name()'''
            return QString()
        def setName(self, name):
            '''void Akonadi.ResourceBase.setName(QString name)'''
    class CollectionModifyJob(Akonadi.Job):
        """"""
        def __init__(self, collection, parent = None):
            '''void Akonadi.CollectionModifyJob.__init__(Akonadi.Collection collection, QObject parent = None)'''
        def collection(self):
            '''Akonadi.Collection Akonadi.CollectionModifyJob.collection()'''
            return Akonadi.Collection()
        def doStart(self):
            '''void Akonadi.CollectionModifyJob.doStart()'''
    class AgentType():
        """"""
        def __init__(self):
            '''void Akonadi.AgentType.__init__()'''
        def __init__(self, other):
            '''void Akonadi.AgentType.__init__(Akonadi.AgentType other)'''
        def __ne__(self, other):
            '''bool Akonadi.AgentType.__ne__(Akonadi.AgentType other)'''
            return bool()
        def __eq__(self, other):
            '''bool Akonadi.AgentType.__eq__(Akonadi.AgentType other)'''
            return bool()
        def capabilities(self):
            '''QStringList Akonadi.AgentType.capabilities()'''
            return QStringList()
        def mimeTypes(self):
            '''QStringList Akonadi.AgentType.mimeTypes()'''
            return QStringList()
        def icon(self):
            '''QIcon Akonadi.AgentType.icon()'''
            return QIcon()
        def iconName(self):
            '''QString Akonadi.AgentType.iconName()'''
            return QString()
        def description(self):
            '''QString Akonadi.AgentType.description()'''
            return QString()
        def name(self):
            '''QString Akonadi.AgentType.name()'''
            return QString()
        def identifier(self):
            '''QString Akonadi.AgentType.identifier()'''
            return QString()
        def isValid(self):
            '''bool Akonadi.AgentType.isValid()'''
            return bool()
    class MessagePart():
        """"""
        Body = None # str - member
        Envelope = None # str - member
        Header = None # str - member
    class CollectionModel(QAbstractItemModel):
        """"""
        # Enum Akonadi.CollectionModel.Roles
        OldCollectionIdRole = 0
        OldCollectionRole = 0
        CollectionIdRole = 0
        CollectionRole = 0
        UserRole = 0
    
        def __init__(self, parent = None):
            '''void Akonadi.CollectionModel.__init__(QObject parent = None)'''
        def collectionForId(self, id):
            '''Akonadi.Collection Akonadi.CollectionModel.collectionForId(int id)'''
            return Akonadi.Collection()
        def mimeTypes(self):
            '''QStringList Akonadi.CollectionModel.mimeTypes()'''
            return QStringList()
        def dropMimeData(self, data, action, row, column, parent):
            '''bool Akonadi.CollectionModel.dropMimeData(QMimeData data, Qt.DropAction action, int row, int column, QModelIndex parent)'''
            return bool()
        def mimeData(self, indexes):
            '''QMimeData Akonadi.CollectionModel.mimeData(list-of-QModelIndex indexes)'''
            return QMimeData()
        def supportedDropActions(self):
            '''Qt.DropActions Akonadi.CollectionModel.supportedDropActions()'''
            return Qt.DropActions()
        def flags(self, index):
            '''Qt.ItemFlags Akonadi.CollectionModel.flags(QModelIndex index)'''
            return Qt.ItemFlags()
        def setData(self, index, value, role = None):
            '''bool Akonadi.CollectionModel.setData(QModelIndex index, QVariant value, int role = Qt.EditRole)'''
            return bool()
        def setHeaderData(self, section, orientation, value, role = None):
            '''bool Akonadi.CollectionModel.setHeaderData(int section, Qt.Orientation orientation, QVariant value, int role = Qt.EditRole)'''
            return bool()
        def headerData(self, section, orientation, role = None):
            '''QVariant Akonadi.CollectionModel.headerData(int section, Qt.Orientation orientation, int role = Qt.DisplayRole)'''
            return QVariant()
        def rowCount(self, parent = QModelIndex()):
            '''int Akonadi.CollectionModel.rowCount(QModelIndex parent = QModelIndex())'''
            return int()
        def parent(self, index):
            '''QModelIndex Akonadi.CollectionModel.parent(QModelIndex index)'''
            return QModelIndex()
        def index(self, row, column, parent = QModelIndex()):
            '''QModelIndex Akonadi.CollectionModel.index(int row, int column, QModelIndex parent = QModelIndex())'''
            return QModelIndex()
        def data(self, index, role = None):
            '''QVariant Akonadi.CollectionModel.data(QModelIndex index, int role = Qt.DisplayRole)'''
            return QVariant()
        def columnCount(self, parent = QModelIndex()):
            '''int Akonadi.CollectionModel.columnCount(QModelIndex parent = QModelIndex())'''
            return int()
        def includeUnsubscribed(self, include = True):
            '''void Akonadi.CollectionModel.includeUnsubscribed(bool include = True)'''
        def fetchCollectionStatistics(self, enable):
            '''void Akonadi.CollectionModel.fetchCollectionStatistics(bool enable)'''
    class MessageFolderAttribute(Akonadi.Attribute):
        """"""
        def __init__(self):
            '''void Akonadi.MessageFolderAttribute.__init__()'''
        def __init__(self, other):
            '''void Akonadi.MessageFolderAttribute.__init__(Akonadi.MessageFolderAttribute other)'''
        def deserialize(self, data):
            '''void Akonadi.MessageFolderAttribute.deserialize(QByteArray data)'''
        def serialized(self):
            '''QByteArray Akonadi.MessageFolderAttribute.serialized()'''
            return QByteArray()
        def clone(self):
            '''Akonadi.MessageFolderAttribute Akonadi.MessageFolderAttribute.clone()'''
            return Akonadi.MessageFolderAttribute()
        def type(self):
            '''QByteArray Akonadi.MessageFolderAttribute.type()'''
            return QByteArray()
        def setOutboundFolder(self, outbound):
            '''void Akonadi.MessageFolderAttribute.setOutboundFolder(bool outbound)'''
        def isOutboundFolder(self):
            '''bool Akonadi.MessageFolderAttribute.isOutboundFolder()'''
            return bool()
    class ChangeRecorder(Akonadi.Monitor):
        """"""
        def __init__(self, parent = None):
            '''void Akonadi.ChangeRecorder.__init__(QObject parent = None)'''
        def dumpNotificationListToString(self):
            '''QString Akonadi.ChangeRecorder.dumpNotificationListToString()'''
            return QString()
        nothingToReplay = pyqtSignal() # void nothingToReplay() - signal
        changesAdded = pyqtSignal() # void changesAdded() - signal
        def replayNext(self):
            '''void Akonadi.ChangeRecorder.replayNext()'''
        def setChangeRecordingEnabled(self, enable):
            '''void Akonadi.ChangeRecorder.setChangeRecordingEnabled(bool enable)'''
        def changeProcessed(self):
            '''void Akonadi.ChangeRecorder.changeProcessed()'''
        def isEmpty(self):
            '''bool Akonadi.ChangeRecorder.isEmpty()'''
            return bool()
        def setConfig(self, settings):
            '''void Akonadi.ChangeRecorder.setConfig(QSettings settings)'''
    class CollectionView(QTreeView):
        """"""
        def __init__(self, parent = None):
            '''void Akonadi.CollectionView.__init__(QWidget parent = None)'''
        def __init__(self, xmlGuiWindow, parent = None):
            '''void Akonadi.CollectionView.__init__(KXmlGuiWindow xmlGuiWindow, QWidget parent = None)'''
        def __init__(self, xmlGuiClient, parent = None):
            '''void Akonadi.CollectionView.__init__(KXMLGUIClient xmlGuiClient, QWidget parent = None)'''
        def contextMenuEvent(self, event):
            '''void Akonadi.CollectionView.contextMenuEvent(QContextMenuEvent event)'''
        def dropEvent(self, event):
            '''void Akonadi.CollectionView.dropEvent(QDropEvent event)'''
        def dragLeaveEvent(self, event):
            '''void Akonadi.CollectionView.dragLeaveEvent(QDragLeaveEvent event)'''
        def dragMoveEvent(self, event):
            '''void Akonadi.CollectionView.dragMoveEvent(QDragMoveEvent event)'''
        currentChanged = pyqtSignal() # void currentChanged(const Akonadi::Collectionamp;) - signal
        clicked = pyqtSignal() # void clicked(const Akonadi::Collectionamp;) - signal
        def setModel(self, model):
            '''void Akonadi.CollectionView.setModel(QAbstractItemModel model)'''
        def setXmlGuiClient(self, xmlGuiClient):
            '''void Akonadi.CollectionView.setXmlGuiClient(KXMLGUIClient xmlGuiClient)'''
        def setXmlGuiWindow(self, xmlGuiWindow):
            '''void Akonadi.CollectionView.setXmlGuiWindow(KXmlGuiWindow xmlGuiWindow)'''
    class SpecialMailCollections(Akonadi.SpecialCollections):
        """"""
        # Enum Akonadi.SpecialMailCollections.Type
        Invalid = 0
        Root = 0
        Inbox = 0
        Outbox = 0
        SentMail = 0
        Trash = 0
        Drafts = 0
        Templates = 0
        LastType = 0
    
        def __init__(self):
            '''void Akonadi.SpecialMailCollections.__init__()'''
        def defaultCollection(self, type):
            '''Akonadi.Collection Akonadi.SpecialMailCollections.defaultCollection(Akonadi.SpecialMailCollections.Type type)'''
            return Akonadi.Collection()
        def hasDefaultCollection(self, type):
            '''bool Akonadi.SpecialMailCollections.hasDefaultCollection(Akonadi.SpecialMailCollections.Type type)'''
            return bool()
        def registerCollection(self, type, collection):
            '''bool Akonadi.SpecialMailCollections.registerCollection(Akonadi.SpecialMailCollections.Type type, Akonadi.Collection collection)'''
            return bool()
        def collection(self, type, instance):
            '''Akonadi.Collection Akonadi.SpecialMailCollections.collection(Akonadi.SpecialMailCollections.Type type, Akonadi.AgentInstance instance)'''
            return Akonadi.Collection()
        def hasCollection(self, type, instance):
            '''bool Akonadi.SpecialMailCollections.hasCollection(Akonadi.SpecialMailCollections.Type type, Akonadi.AgentInstance instance)'''
            return bool()
        def self(self):
            '''static Akonadi.SpecialMailCollections Akonadi.SpecialMailCollections.self()'''
            return Akonadi.SpecialMailCollections()
    class AgentBase():
        """"""
        class ObserverV2(Akonadi.AgentBase.Observer):
            """"""
            def __init__(self):
                '''void Akonadi.AgentBase.ObserverV2.__init__()'''
            def __init__(self):
                '''Akonadi.AgentBase.ObserverV2 Akonadi.AgentBase.ObserverV2.__init__()'''
                return Akonadi.AgentBase.ObserverV2()
            def collectionChanged(self, collection, changedAttributes):
                '''void Akonadi.AgentBase.ObserverV2.collectionChanged(Akonadi.Collection collection, list-of-QByteArray changedAttributes)'''
            def collectionMoved(self, collection, collectionSource, collectionDestination):
                '''void Akonadi.AgentBase.ObserverV2.collectionMoved(Akonadi.Collection collection, Akonadi.Collection collectionSource, Akonadi.Collection collectionDestination)'''
            def itemUnlinked(self, item, collection):
                '''void Akonadi.AgentBase.ObserverV2.itemUnlinked(Akonadi.Item item, Akonadi.Collection collection)'''
            def itemLinked(self, item, collection):
                '''void Akonadi.AgentBase.ObserverV2.itemLinked(Akonadi.Item item, Akonadi.Collection collection)'''
            def itemMoved(self, item, collectionSource, collectionDestination):
                '''void Akonadi.AgentBase.ObserverV2.itemMoved(Akonadi.Item item, Akonadi.Collection collectionSource, Akonadi.Collection collectionDestination)'''
    class ItemSync(Akonadi.Job):
        """"""
        # Enum Akonadi.ItemSync.TransactionMode
        SingleTransaction = 0
        MultipleTransactions = 0
        NoTransaction = 0
    
        def __init__(self, collection, parent = None):
            '''void Akonadi.ItemSync.__init__(Akonadi.Collection collection, QObject parent = None)'''
        def setTransactionMode(self, mode):
            '''void Akonadi.ItemSync.setTransactionMode(Akonadi.ItemSync.TransactionMode mode)'''
        def rollback(self):
            '''void Akonadi.ItemSync.rollback()'''
        def slotResult(self, job):
            '''void Akonadi.ItemSync.slotResult(KJob job)'''
        def updateItem(self, storedItem, newItem):
            '''bool Akonadi.ItemSync.updateItem(Akonadi.Item storedItem, Akonadi.Item newItem)'''
            return bool()
        def doStart(self):
            '''void Akonadi.ItemSync.doStart()'''
        def fetchScope(self):
            '''Akonadi.ItemFetchScope Akonadi.ItemSync.fetchScope()'''
            return Akonadi.ItemFetchScope()
        def setFetchScope(self, fetchScope):
            '''void Akonadi.ItemSync.setFetchScope(Akonadi.ItemFetchScope fetchScope)'''
        def setIncrementalSyncItems(self, changedItems, removedItems):
            '''void Akonadi.ItemSync.setIncrementalSyncItems(list-of-Akonadi.Item changedItems, list-of-Akonadi.Item removedItems)'''
        def deliveryDone(self):
            '''void Akonadi.ItemSync.deliveryDone()'''
        def setStreamingEnabled(self, enable):
            '''void Akonadi.ItemSync.setStreamingEnabled(bool enable)'''
        def setTotalItems(self, amount):
            '''void Akonadi.ItemSync.setTotalItems(int amount)'''
        def setFullSyncItems(self, items):
            '''void Akonadi.ItemSync.setFullSyncItems(list-of-Akonadi.Item items)'''
    class SpecialCollections(QObject):
        """"""
        def __init__(self, config, parent = None):
            '''void Akonadi.SpecialCollections.__init__(KCoreConfigSkeleton config, QObject parent = None)'''
        defaultCollectionsChanged = pyqtSignal() # void defaultCollectionsChanged() - signal
        collectionsChanged = pyqtSignal() # void collectionsChanged(const Akonadi::AgentInstanceamp;) - signal
        def defaultCollection(self, type):
            '''Akonadi.Collection Akonadi.SpecialCollections.defaultCollection(QByteArray type)'''
            return Akonadi.Collection()
        def hasDefaultCollection(self, type):
            '''bool Akonadi.SpecialCollections.hasDefaultCollection(QByteArray type)'''
            return bool()
        def registerCollection(self, type, collection):
            '''bool Akonadi.SpecialCollections.registerCollection(QByteArray type, Akonadi.Collection collection)'''
            return bool()
        def collection(self, type, instance):
            '''Akonadi.Collection Akonadi.SpecialCollections.collection(QByteArray type, Akonadi.AgentInstance instance)'''
            return Akonadi.Collection()
        def hasCollection(self, type, instance):
            '''bool Akonadi.SpecialCollections.hasCollection(QByteArray type, Akonadi.AgentInstance instance)'''
            return bool()
    class AgentFilterProxyModel(QSortFilterProxyModel):
        """"""
        def __init__(self, parent = None):
            '''void Akonadi.AgentFilterProxyModel.__init__(QObject parent = None)'''
        def excludeCapabilities(self, capability):
            '''void Akonadi.AgentFilterProxyModel.excludeCapabilities(QString capability)'''
        def filterAcceptsRow(self, row, parent):
            '''bool Akonadi.AgentFilterProxyModel.filterAcceptsRow(int row, QModelIndex parent)'''
            return bool()
        def clearFilters(self):
            '''void Akonadi.AgentFilterProxyModel.clearFilters()'''
        def addCapabilityFilter(self, capability):
            '''void Akonadi.AgentFilterProxyModel.addCapabilityFilter(QString capability)'''
        def addMimeTypeFilter(self, mimeType):
            '''void Akonadi.AgentFilterProxyModel.addMimeTypeFilter(QString mimeType)'''
    class EntityListView(QListView):
        """"""
        def __init__(self, parent = None):
            '''void Akonadi.EntityListView.__init__(QWidget parent = None)'''
        def __init__(self, xmlGuiClient, parent = None):
            '''void Akonadi.EntityListView.__init__(KXMLGUIClient xmlGuiClient, QWidget parent = None)'''
        def isDropActionMenuEnabled(self):
            '''bool Akonadi.EntityListView.isDropActionMenuEnabled()'''
            return bool()
        def setDropActionMenuEnabled(self, enabled):
            '''void Akonadi.EntityListView.setDropActionMenuEnabled(bool enabled)'''
        def startDrag(self, supportedActions):
            '''void Akonadi.EntityListView.startDrag(Qt.DropActions supportedActions)'''
        def contextMenuEvent(self, event):
            '''void Akonadi.EntityListView.contextMenuEvent(QContextMenuEvent event)'''
        def dropEvent(self, event):
            '''void Akonadi.EntityListView.dropEvent(QDropEvent event)'''
        def dragMoveEvent(self, event):
            '''void Akonadi.EntityListView.dragMoveEvent(QDragMoveEvent event)'''
        currentChanged = pyqtSignal() # void currentChanged(const Akonadi::Collectionamp;) - signal
        currentChanged = pyqtSignal() # void currentChanged(const Akonadi::Itemamp;) - signal
        doubleClicked = pyqtSignal() # void doubleClicked(const Akonadi::Collectionamp;) - signal
        doubleClicked = pyqtSignal() # void doubleClicked(const Akonadi::Itemamp;) - signal
        clicked = pyqtSignal() # void clicked(const Akonadi::Collectionamp;) - signal
        clicked = pyqtSignal() # void clicked(const Akonadi::Itemamp;) - signal
        def setModel(self, model):
            '''void Akonadi.EntityListView.setModel(QAbstractItemModel model)'''
        def setXmlGuiClient(self, xmlGuiClient):
            '''void Akonadi.EntityListView.setXmlGuiClient(KXMLGUIClient xmlGuiClient)'''
    class MessageThreadingAttribute(Akonadi.Attribute):
        """"""
        def __init__(self):
            '''void Akonadi.MessageThreadingAttribute.__init__()'''
        def setSubjectParents(self, parents):
            '''void Akonadi.MessageThreadingAttribute.setSubjectParents(unknown-type parents)'''
        def setUnperfectParents(self, parents):
            '''void Akonadi.MessageThreadingAttribute.setUnperfectParents(unknown-type parents)'''
        def setPerfectParents(self, parents):
            '''void Akonadi.MessageThreadingAttribute.setPerfectParents(unknown-type parents)'''
        def subjectParents(self):
            '''unknown-type Akonadi.MessageThreadingAttribute.subjectParents()'''
            return unknown-type()
        def unperfectParents(self):
            '''unknown-type Akonadi.MessageThreadingAttribute.unperfectParents()'''
            return unknown-type()
        def perfectParents(self):
            '''unknown-type Akonadi.MessageThreadingAttribute.perfectParents()'''
            return unknown-type()
        def deserialize(self, data):
            '''void Akonadi.MessageThreadingAttribute.deserialize(QByteArray data)'''
        def serialized(self):
            '''QByteArray Akonadi.MessageThreadingAttribute.serialized()'''
            return QByteArray()
        def clone(self):
            '''Akonadi.MessageThreadingAttribute Akonadi.MessageThreadingAttribute.clone()'''
            return Akonadi.MessageThreadingAttribute()
        def type(self):
            '''QByteArray Akonadi.MessageThreadingAttribute.type()'''
            return QByteArray()
    class ItemSearchJob(Akonadi.Job):
        """"""
        def __init__(self, query, parent = None):
            '''void Akonadi.ItemSearchJob.__init__(QString query, QObject parent = None)'''
        def akonadiItemIdUri(self):
            '''static QUrl Akonadi.ItemSearchJob.akonadiItemIdUri()'''
            return QUrl()
        def doHandleResponse(self, tag, data):
            '''void Akonadi.ItemSearchJob.doHandleResponse(QByteArray tag, QByteArray data)'''
        def doStart(self):
            '''void Akonadi.ItemSearchJob.doStart()'''
        itemsReceived = pyqtSignal() # void itemsReceived(const Akonadi::Item::Listamp;) - signal
        def items(self):
            '''list-of-Akonadi.Item Akonadi.ItemSearchJob.items()'''
            return [Akonadi.Item()]
        def fetchScope(self):
            '''Akonadi.ItemFetchScope Akonadi.ItemSearchJob.fetchScope()'''
            return Akonadi.ItemFetchScope()
        def setFetchScope(self, fetchScope):
            '''void Akonadi.ItemSearchJob.setFetchScope(Akonadi.ItemFetchScope fetchScope)'''
        def setQuery(self, query):
            '''void Akonadi.ItemSearchJob.setQuery(QString query)'''
    class ItemView(QTreeView):
        """"""
        def __init__(self, parent = None):
            '''void Akonadi.ItemView.__init__(QWidget parent = None)'''
        def __init__(self, xmlGuiWindow, parent = None):
            '''void Akonadi.ItemView.__init__(KXmlGuiWindow xmlGuiWindow, QWidget parent = None)'''
        def __init__(self, xmlGuiClient, parent = None):
            '''void Akonadi.ItemView.__init__(KXMLGUIClient xmlGuiClient, QWidget parent = None)'''
        def contextMenuEvent(self, event):
            '''void Akonadi.ItemView.contextMenuEvent(QContextMenuEvent event)'''
        doubleClicked = pyqtSignal() # void doubleClicked(const Akonadi::Itemamp;) - signal
        clicked = pyqtSignal() # void clicked(const Akonadi::Itemamp;) - signal
        currentChanged = pyqtSignal() # void currentChanged(const Akonadi::Itemamp;) - signal
        activated = pyqtSignal() # void activated(const Akonadi::Itemamp;) - signal
        def setModel(self, model):
            '''void Akonadi.ItemView.setModel(QAbstractItemModel model)'''
        def setXmlGuiClient(self, xmlGuiClient):
            '''void Akonadi.ItemView.setXmlGuiClient(KXMLGUIClient xmlGuiClient)'''
        def setXmlGuiWindow(self, xmlGuiWindow):
            '''void Akonadi.ItemView.setXmlGuiWindow(KXmlGuiWindow xmlGuiWindow)'''
    class SelectionProxyModel(KSelectionProxyModel):
        """"""
        def __init__(self, selectionModel, parent = None):
            '''void Akonadi.SelectionProxyModel.__init__(QItemSelectionModel selectionModel, QObject parent = None)'''
    class CollectionCreateJob(Akonadi.Job):
        """"""
        def __init__(self, collection, parent = None):
            '''void Akonadi.CollectionCreateJob.__init__(Akonadi.Collection collection, QObject parent = None)'''
        def doHandleResponse(self, tag, data):
            '''void Akonadi.CollectionCreateJob.doHandleResponse(QByteArray tag, QByteArray data)'''
        def doStart(self):
            '''void Akonadi.CollectionCreateJob.doStart()'''
        def collection(self):
            '''Akonadi.Collection Akonadi.CollectionCreateJob.collection()'''
            return Akonadi.Collection()
    class Monitor(QObject):
        """"""
        def __init__(self, parent = None):
            '''void Akonadi.Monitor.__init__(QObject parent = None)'''
        def fetchChangedOnly(self, enable):
            '''void Akonadi.Monitor.fetchChangedOnly(bool enable)'''
        collectionUnsubscribed = pyqtSignal() # void collectionUnsubscribed(const Akonadi::Collectionamp;) - signal
        collectionSubscribed = pyqtSignal() # void collectionSubscribed(const Akonadi::Collectionamp;,const Akonadi::Collectionamp;) - signal
        def itemsMonitoredEx(self):
            '''unknown-type Akonadi.Monitor.itemsMonitoredEx()'''
            return unknown-type()
        def session(self):
            '''Akonadi.Session Akonadi.Monitor.session()'''
            return Akonadi.Session()
        def setSession(self, session):
            '''void Akonadi.Monitor.setSession(Akonadi.Session session)'''
        collectionStatisticsChanged = pyqtSignal() # void collectionStatisticsChanged(Akonadi::Entity::Id,const Akonadi::CollectionStatisticsamp;) - signal
        collectionMoved = pyqtSignal() # void collectionMoved(const Akonadi::Collectionamp;,const Akonadi::Collectionamp;,const Akonadi::Collectionamp;) - signal
        def collectionFetchScope(self):
            '''Akonadi.CollectionFetchScope Akonadi.Monitor.collectionFetchScope()'''
            return Akonadi.CollectionFetchScope()
        def setCollectionFetchScope(self, fetchScope):
            '''void Akonadi.Monitor.setCollectionFetchScope(Akonadi.CollectionFetchScope fetchScope)'''
        allMonitored = pyqtSignal() # void allMonitored(bool) - signal
        mimeTypeMonitored = pyqtSignal() # void mimeTypeMonitored(const QStringamp;,bool) - signal
        resourceMonitored = pyqtSignal() # void resourceMonitored(const QByteArrayamp;,bool) - signal
        itemMonitored = pyqtSignal() # void itemMonitored(const Akonadi::Itemamp;,bool) - signal
        collectionMonitored = pyqtSignal() # void collectionMonitored(const Akonadi::Collectionamp;,bool) - signal
        collectionRemoved = pyqtSignal() # void collectionRemoved(const Akonadi::Collectionamp;) - signal
        collectionChanged = pyqtSignal() # void collectionChanged(const Akonadi::Collectionamp;) - signal
        collectionChanged = pyqtSignal() # void collectionChanged(const Akonadi::Collectionamp;,const QSetlt;QByteArraygt;amp;) - signal
        collectionAdded = pyqtSignal() # void collectionAdded(const Akonadi::Collectionamp;,const Akonadi::Collectionamp;) - signal
        itemUnlinked = pyqtSignal() # void itemUnlinked(const Akonadi::Itemamp;,const Akonadi::Collectionamp;) - signal
        itemLinked = pyqtSignal() # void itemLinked(const Akonadi::Itemamp;,const Akonadi::Collectionamp;) - signal
        itemRemoved = pyqtSignal() # void itemRemoved(const Akonadi::Itemamp;) - signal
        itemAdded = pyqtSignal() # void itemAdded(const Akonadi::Itemamp;,const Akonadi::Collectionamp;) - signal
        itemMoved = pyqtSignal() # void itemMoved(const Akonadi::Itemamp;,const Akonadi::Collectionamp;,const Akonadi::Collectionamp;) - signal
        itemChanged = pyqtSignal() # void itemChanged(const Akonadi::Itemamp;,const QSetlt;QByteArraygt;amp;) - signal
        def isAllMonitored(self):
            '''bool Akonadi.Monitor.isAllMonitored()'''
            return bool()
        def resourcesMonitored(self):
            '''list-of-QByteArray Akonadi.Monitor.resourcesMonitored()'''
            return [QByteArray()]
        def mimeTypesMonitored(self):
            '''QStringList Akonadi.Monitor.mimeTypesMonitored()'''
            return QStringList()
        def itemsMonitored(self):
            '''unknown-type Akonadi.Monitor.itemsMonitored()'''
            return unknown-type()
        def collectionsMonitored(self):
            '''list-of-Akonadi.Collection Akonadi.Monitor.collectionsMonitored()'''
            return [Akonadi.Collection()]
        def itemFetchScope(self):
            '''Akonadi.ItemFetchScope Akonadi.Monitor.itemFetchScope()'''
            return Akonadi.ItemFetchScope()
        def setItemFetchScope(self, fetchScope):
            '''void Akonadi.Monitor.setItemFetchScope(Akonadi.ItemFetchScope fetchScope)'''
        def fetchCollectionStatistics(self, enable):
            '''void Akonadi.Monitor.fetchCollectionStatistics(bool enable)'''
        def fetchCollection(self, enable):
            '''void Akonadi.Monitor.fetchCollection(bool enable)'''
        def ignoreSession(self, session):
            '''void Akonadi.Monitor.ignoreSession(Akonadi.Session session)'''
        def setAllMonitored(self, monitored = True):
            '''void Akonadi.Monitor.setAllMonitored(bool monitored = True)'''
        def setMimeTypeMonitored(self, mimetype, monitored = True):
            '''void Akonadi.Monitor.setMimeTypeMonitored(QString mimetype, bool monitored = True)'''
        def setResourceMonitored(self, resource, monitored = True):
            '''void Akonadi.Monitor.setResourceMonitored(QByteArray resource, bool monitored = True)'''
        def setItemMonitored(self, item, monitored = True):
            '''void Akonadi.Monitor.setItemMonitored(Akonadi.Item item, bool monitored = True)'''
        def setCollectionMonitored(self, collection, monitored = True):
            '''void Akonadi.Monitor.setCollectionMonitored(Akonadi.Collection collection, bool monitored = True)'''
    class ResourceBaseSettings(KConfigSkeleton):
        """"""
        def __init__(self):
            '''void Akonadi.ResourceBaseSettings.__init__()'''
        def minimumCheckIntervalItem(self):
            '''KCoreConfigSkeleton.ItemInt Akonadi.ResourceBaseSettings.minimumCheckIntervalItem()'''
            return KCoreConfigSkeleton.ItemInt()
        def minimumCheckInterval(self):
            '''static int Akonadi.ResourceBaseSettings.minimumCheckInterval()'''
            return int()
        def setMinimumCheckInterval(self, v):
            '''static void Akonadi.ResourceBaseSettings.setMinimumCheckInterval(int v)'''
        def self(self):
            '''static Akonadi.ResourceBaseSettings Akonadi.ResourceBaseSettings.self()'''
            return Akonadi.ResourceBaseSettings()
    class AgentInstanceWidget(QWidget):
        """"""
        def __init__(self, parent = None):
            '''void Akonadi.AgentInstanceWidget.__init__(QWidget parent = None)'''
        def view(self):
            '''QAbstractItemView Akonadi.AgentInstanceWidget.view()'''
            return QAbstractItemView()
        def selectedAgentInstances(self):
            '''list-of-Akonadi.AgentInstance Akonadi.AgentInstanceWidget.selectedAgentInstances()'''
            return [Akonadi.AgentInstance()]
        doubleClicked = pyqtSignal() # void doubleClicked(const Akonadi::AgentInstanceamp;) - signal
        currentChanged = pyqtSignal() # void currentChanged(const Akonadi::AgentInstanceamp;,const Akonadi::AgentInstanceamp;) - signal
        def agentFilterProxyModel(self):
            '''Akonadi.AgentFilterProxyModel Akonadi.AgentInstanceWidget.agentFilterProxyModel()'''
            return Akonadi.AgentFilterProxyModel()
        def currentAgentInstance(self):
            '''Akonadi.AgentInstance Akonadi.AgentInstanceWidget.currentAgentInstance()'''
            return Akonadi.AgentInstance()
    class PartFetcher(KJob):
        """"""
        def __init__(self, index, partName, parent = None):
            '''void Akonadi.PartFetcher.__init__(QModelIndex index, QByteArray partName, QObject parent = None)'''
        def item(self):
            '''Akonadi.Item Akonadi.PartFetcher.item()'''
            return Akonadi.Item()
        def partName(self):
            '''QByteArray Akonadi.PartFetcher.partName()'''
            return QByteArray()
        def index(self):
            '''QModelIndex Akonadi.PartFetcher.index()'''
            return QModelIndex()
        def start(self):
            '''void Akonadi.PartFetcher.start()'''
    class CollectionDialog(KDialog):
        """"""
        # Enum Akonadi.CollectionDialog.CollectionDialogOption
        __kdevpythondocumentation_builtin_None = 0
        AllowToCreateNewChildCollection = 0
    
        def __init__(self, parent = None):
            '''void Akonadi.CollectionDialog.__init__(QWidget parent = None)'''
        def __init__(self, model, parent = None):
            '''void Akonadi.CollectionDialog.__init__(QAbstractItemModel model, QWidget parent = None)'''
        def __init__(self, options, model = None, parent = None):
            '''void Akonadi.CollectionDialog.__init__(Akonadi.CollectionDialog.CollectionDialogOptions options, QAbstractItemModel model = None, QWidget parent = None)'''
        def changeCollectionDialogOptions(self, options):
            '''void Akonadi.CollectionDialog.changeCollectionDialogOptions(Akonadi.CollectionDialog.CollectionDialogOptions options)'''
        def setDefaultCollection(self, collection):
            '''void Akonadi.CollectionDialog.setDefaultCollection(Akonadi.Collection collection)'''
        def setDescription(self, text):
            '''void Akonadi.CollectionDialog.setDescription(QString text)'''
        def accessRightsFilter(self):
            '''Akonadi.Collection.Rights Akonadi.CollectionDialog.accessRightsFilter()'''
            return Akonadi.Collection.Rights()
        def setAccessRightsFilter(self, rights):
            '''void Akonadi.CollectionDialog.setAccessRightsFilter(Akonadi.Collection.Rights rights)'''
        def selectionMode(self):
            '''QAbstractItemView.SelectionMode Akonadi.CollectionDialog.selectionMode()'''
            return QAbstractItemView.SelectionMode()
        def setSelectionMode(self, mode):
            '''void Akonadi.CollectionDialog.setSelectionMode(QAbstractItemView.SelectionMode mode)'''
        def mimeTypeFilter(self):
            '''QStringList Akonadi.CollectionDialog.mimeTypeFilter()'''
            return QStringList()
        def setMimeTypeFilter(self, mimeTypes):
            '''void Akonadi.CollectionDialog.setMimeTypeFilter(QStringList mimeTypes)'''
        def selectedCollections(self):
            '''list-of-Akonadi.Collection Akonadi.CollectionDialog.selectedCollections()'''
            return [Akonadi.Collection()]
        def selectedCollection(self):
            '''Akonadi.Collection Akonadi.CollectionDialog.selectedCollection()'''
            return Akonadi.Collection()
    class EntityHiddenAttribute(Akonadi.Attribute):
        """"""
        def __init__(self):
            '''void Akonadi.EntityHiddenAttribute.__init__()'''
        def deserialize(self, data):
            '''void Akonadi.EntityHiddenAttribute.deserialize(QByteArray data)'''
        def serialized(self):
            '''QByteArray Akonadi.EntityHiddenAttribute.serialized()'''
            return QByteArray()
        def clone(self):
            '''Akonadi.EntityHiddenAttribute Akonadi.EntityHiddenAttribute.clone()'''
            return Akonadi.EntityHiddenAttribute()
        def type(self):
            '''QByteArray Akonadi.EntityHiddenAttribute.type()'''
            return QByteArray()
    class FavoriteCollectionsModel(Akonadi.SelectionProxyModel):
        """"""
        def __init__(self, model, group, parent = None):
            '''void Akonadi.FavoriteCollectionsModel.__init__(QAbstractItemModel model, KConfigGroup group, QObject parent = None)'''
        def flags(self, index):
            '''Qt.ItemFlags Akonadi.FavoriteCollectionsModel.flags(QModelIndex index)'''
            return Qt.ItemFlags()
        def mimeTypes(self):
            '''QStringList Akonadi.FavoriteCollectionsModel.mimeTypes()'''
            return QStringList()
        def dropMimeData(self, data, action, row, column, parent):
            '''bool Akonadi.FavoriteCollectionsModel.dropMimeData(QMimeData data, Qt.DropAction action, int row, int column, QModelIndex parent)'''
            return bool()
        def setData(self, index, value, role = None):
            '''bool Akonadi.FavoriteCollectionsModel.setData(QModelIndex index, QVariant value, int role = Qt.EditRole)'''
            return bool()
        def collectionIds(self):
            '''unknown-type Akonadi.FavoriteCollectionsModel.collectionIds()'''
            return unknown-type()
        def favoriteLabel(self, col):
            '''QString Akonadi.FavoriteCollectionsModel.favoriteLabel(Akonadi.Collection col)'''
            return QString()
        def setFavoriteLabel(self, collection, label):
            '''void Akonadi.FavoriteCollectionsModel.setFavoriteLabel(Akonadi.Collection collection, QString label)'''
        def removeCollection(self, collection):
            '''void Akonadi.FavoriteCollectionsModel.removeCollection(Akonadi.Collection collection)'''
        def addCollection(self, collection):
            '''void Akonadi.FavoriteCollectionsModel.addCollection(Akonadi.Collection collection)'''
        def setCollections(self, collections):
            '''void Akonadi.FavoriteCollectionsModel.setCollections(list-of-Akonadi.Collection collections)'''
        def headerData(self, section, orientation, role = None):
            '''QVariant Akonadi.FavoriteCollectionsModel.headerData(int section, Qt.Orientation orientation, int role = Qt.DisplayRole)'''
            return QVariant()
        def data(self, index, role = None):
            '''QVariant Akonadi.FavoriteCollectionsModel.data(QModelIndex index, int role = Qt.DisplayRole)'''
            return QVariant()
        def collections(self):
            '''list-of-Akonadi.Collection Akonadi.FavoriteCollectionsModel.collections()'''
            return [Akonadi.Collection()]
    class CachePolicy():
        """"""
        def __init__(self):
            '''void Akonadi.CachePolicy.__init__()'''
        def __init__(self, other):
            '''void Akonadi.CachePolicy.__init__(Akonadi.CachePolicy other)'''
        def __ne__(self, other):
            '''bool Akonadi.CachePolicy.__ne__(Akonadi.CachePolicy other)'''
            return bool()
        def __eq__(self, other):
            '''bool Akonadi.CachePolicy.__eq__(Akonadi.CachePolicy other)'''
            return bool()
        def setSyncOnDemand(self, enable):
            '''void Akonadi.CachePolicy.setSyncOnDemand(bool enable)'''
        def syncOnDemand(self):
            '''bool Akonadi.CachePolicy.syncOnDemand()'''
            return bool()
        def setIntervalCheckTime(self, time):
            '''void Akonadi.CachePolicy.setIntervalCheckTime(int time)'''
        def intervalCheckTime(self):
            '''int Akonadi.CachePolicy.intervalCheckTime()'''
            return int()
        def setCacheTimeout(self, timeout):
            '''void Akonadi.CachePolicy.setCacheTimeout(int timeout)'''
        def cacheTimeout(self):
            '''int Akonadi.CachePolicy.cacheTimeout()'''
            return int()
        def setLocalParts(self, parts):
            '''void Akonadi.CachePolicy.setLocalParts(QStringList parts)'''
        def localParts(self):
            '''QStringList Akonadi.CachePolicy.localParts()'''
            return QStringList()
        def setInheritFromParent(self, inherit):
            '''void Akonadi.CachePolicy.setInheritFromParent(bool inherit)'''
        def inheritFromParent(self):
            '''bool Akonadi.CachePolicy.inheritFromParent()'''
            return bool()
    class TrashJob(Akonadi.Job):
        """"""
        def __init__(self, item, parent = None):
            '''void Akonadi.TrashJob.__init__(Akonadi.Item item, QObject parent = None)'''
        def __init__(self, items, parent = None):
            '''void Akonadi.TrashJob.__init__(list-of-Akonadi.Item items, QObject parent = None)'''
        def __init__(self, collection, parent = None):
            '''void Akonadi.TrashJob.__init__(Akonadi.Collection collection, QObject parent = None)'''
        def doStart(self):
            '''void Akonadi.TrashJob.doStart()'''
        def items(self):
            '''list-of-Akonadi.Item Akonadi.TrashJob.items()'''
            return [Akonadi.Item()]
        def deleteIfInTrash(self, enable):
            '''void Akonadi.TrashJob.deleteIfInTrash(bool enable)'''
        def setTrashCollection(self, trashcollection):
            '''void Akonadi.TrashJob.setTrashCollection(Akonadi.Collection trashcollection)'''
        def keepTrashInCollection(self, enable):
            '''void Akonadi.TrashJob.keepTrashInCollection(bool enable)'''
    class CollectionPropertiesPageFactory():
        """"""
        def __init__(self):
            '''void Akonadi.CollectionPropertiesPageFactory.__init__()'''
        def __init__(self):
            '''Akonadi.CollectionPropertiesPageFactory Akonadi.CollectionPropertiesPageFactory.__init__()'''
            return Akonadi.CollectionPropertiesPageFactory()
        def createWidget(self, parent = None):
            '''abstract Akonadi.CollectionPropertiesPage Akonadi.CollectionPropertiesPageFactory.createWidget(QWidget parent = None)'''
            return Akonadi.CollectionPropertiesPage()
    class CollectionStatisticsModel(Akonadi.CollectionModel):
        """"""
        # Enum Akonadi.CollectionStatisticsModel.Roles
        UnreadRole = 0
        TotalRole = 0
        StatisticsRole = 0
        RecursiveUnreadRole = 0
        RecursiveTotalRole = 0
        RecursiveStatisticsRole = 0
        SizeRole = 0
        RecursiveSizeRole = 0
        UserRole = 0
    
        def __init__(self, parent = None):
            '''void Akonadi.CollectionStatisticsModel.__init__(QObject parent = None)'''
        def headerData(self, section, orientation, role = None):
            '''QVariant Akonadi.CollectionStatisticsModel.headerData(int section, Qt.Orientation orientation, int role = Qt.DisplayRole)'''
            return QVariant()
        def data(self, index, role = None):
            '''QVariant Akonadi.CollectionStatisticsModel.data(QModelIndex index, int role = Qt.DisplayRole)'''
            return QVariant()
        def columnCount(self, parent = QModelIndex()):
            '''int Akonadi.CollectionStatisticsModel.columnCount(QModelIndex parent = QModelIndex())'''
            return int()
    class CollectionPropertiesDialog(KDialog):
        """"""
        # Enum Akonadi.CollectionPropertiesDialog.DefaultPage
        GeneralPage = 0
        CachePage = 0
    
        def __init__(self, collection, parent = None):
            '''void Akonadi.CollectionPropertiesDialog.__init__(Akonadi.Collection collection, QWidget parent = None)'''
        def __init__(self, collection, pages, parent = None):
            '''void Akonadi.CollectionPropertiesDialog.__init__(Akonadi.Collection collection, QStringList pages, QWidget parent = None)'''
        def defaultPageObjectName(self, page):
            '''static QString Akonadi.CollectionPropertiesDialog.defaultPageObjectName(Akonadi.CollectionPropertiesDialog.DefaultPage page)'''
            return QString()
        def useDefaultPage(self, use):
            '''static void Akonadi.CollectionPropertiesDialog.useDefaultPage(bool use)'''
        def registerPage(self, factory):
            '''static void Akonadi.CollectionPropertiesDialog.registerPage(Akonadi.CollectionPropertiesPageFactory factory)'''
    class Job(KCompositeJob):
        """"""
        # Enum Akonadi.Job.Error
        ConnectionFailed = 0
        ProtocolVersionMismatch = 0
        UserCanceled = 0
        Unknown = 0
        UserError = 0
    
        def __init__(self, parent = None):
            '''void Akonadi.Job.__init__(QObject parent = None)'''
        def slotResult(self, job):
            '''void Akonadi.Job.slotResult(KJob job)'''
        def emitWriteFinished(self):
            '''void Akonadi.Job.emitWriteFinished()'''
        def doKill(self):
            '''bool Akonadi.Job.doKill()'''
            return bool()
        def removeSubjob(self, job):
            '''bool Akonadi.Job.removeSubjob(KJob job)'''
            return bool()
        def addSubjob(self, job):
            '''bool Akonadi.Job.addSubjob(KJob job)'''
            return bool()
        def doHandleResponse(self, tag, data):
            '''void Akonadi.Job.doHandleResponse(QByteArray tag, QByteArray data)'''
        def doStart(self):
            '''abstract void Akonadi.Job.doStart()'''
        writeFinished = pyqtSignal() # void writeFinished(Akonadi::Job *) - signal
        aboutToStart = pyqtSignal() # void aboutToStart(Akonadi::Job *) - signal
        def errorString(self):
            '''QString Akonadi.Job.errorString()'''
            return QString()
        def start(self):
            '''void Akonadi.Job.start()'''
    class CollectionFetchJob(Akonadi.Job):
        """"""
        # Enum Akonadi.CollectionFetchJob.Type
        Base = 0
        FirstLevel = 0
        Recursive = 0
        NonOverlappingRoots = 0
    
        def __init__(self, collection, type = None, parent = None):
            '''void Akonadi.CollectionFetchJob.__init__(Akonadi.Collection collection, Akonadi.CollectionFetchJob.Type type = Akonadi.CollectionFetchJob.FirstLevel, QObject parent = None)'''
        def __init__(self, collections, parent = None):
            '''void Akonadi.CollectionFetchJob.__init__(list-of-Akonadi.Collection collections, QObject parent = None)'''
        def __init__(self, collections, type, parent = None):
            '''void Akonadi.CollectionFetchJob.__init__(list-of-Akonadi.Collection collections, Akonadi.CollectionFetchJob.Type type, QObject parent = None)'''
        def fetchScope(self):
            '''Akonadi.CollectionFetchScope Akonadi.CollectionFetchJob.fetchScope()'''
            return Akonadi.CollectionFetchScope()
        def setFetchScope(self, fetchScope):
            '''void Akonadi.CollectionFetchJob.setFetchScope(Akonadi.CollectionFetchScope fetchScope)'''
        def slotResult(self, job):
            '''void Akonadi.CollectionFetchJob.slotResult(KJob job)'''
        def doHandleResponse(self, tag, data):
            '''void Akonadi.CollectionFetchJob.doHandleResponse(QByteArray tag, QByteArray data)'''
        def doStart(self):
            '''void Akonadi.CollectionFetchJob.doStart()'''
        collectionsReceived = pyqtSignal() # void collectionsReceived(const Akonadi::Collection::Listamp;) - signal
        def includeStatistics(self, include = True):
            '''void Akonadi.CollectionFetchJob.includeStatistics(bool include = True)'''
        def includeUnsubscribed(self, include = True):
            '''void Akonadi.CollectionFetchJob.includeUnsubscribed(bool include = True)'''
        def setResource(self, resource):
            '''void Akonadi.CollectionFetchJob.setResource(QString resource)'''
        def collections(self):
            '''list-of-Akonadi.Collection Akonadi.CollectionFetchJob.collections()'''
            return [Akonadi.Collection()]
    class EntityTreeView(QTreeView):
        """"""
        def __init__(self, parent = None):
            '''void Akonadi.EntityTreeView.__init__(QWidget parent = None)'''
        def __init__(self, xmlGuiClient, parent = None):
            '''void Akonadi.EntityTreeView.__init__(KXMLGUIClient xmlGuiClient, QWidget parent = None)'''
        def setManualSortingActive(self, active):
            '''void Akonadi.EntityTreeView.setManualSortingActive(bool active)'''
        def isManualSortingActive(self):
            '''bool Akonadi.EntityTreeView.isManualSortingActive()'''
            return bool()
        def isDropActionMenuEnabled(self):
            '''bool Akonadi.EntityTreeView.isDropActionMenuEnabled()'''
            return bool()
        def setDropActionMenuEnabled(self, enabled):
            '''void Akonadi.EntityTreeView.setDropActionMenuEnabled(bool enabled)'''
        def startDrag(self, supportedActions):
            '''void Akonadi.EntityTreeView.startDrag(Qt.DropActions supportedActions)'''
        def contextMenuEvent(self, event):
            '''void Akonadi.EntityTreeView.contextMenuEvent(QContextMenuEvent event)'''
        def dropEvent(self, event):
            '''void Akonadi.EntityTreeView.dropEvent(QDropEvent event)'''
        def timerEvent(self, event):
            '''void Akonadi.EntityTreeView.timerEvent(QTimerEvent event)'''
        def dragMoveEvent(self, event):
            '''void Akonadi.EntityTreeView.dragMoveEvent(QDragMoveEvent event)'''
        currentChanged = pyqtSignal() # void currentChanged(const Akonadi::Collectionamp;) - signal
        currentChanged = pyqtSignal() # void currentChanged(const Akonadi::Itemamp;) - signal
        doubleClicked = pyqtSignal() # void doubleClicked(const Akonadi::Collectionamp;) - signal
        doubleClicked = pyqtSignal() # void doubleClicked(const Akonadi::Itemamp;) - signal
        clicked = pyqtSignal() # void clicked(const Akonadi::Collectionamp;) - signal
        clicked = pyqtSignal() # void clicked(const Akonadi::Itemamp;) - signal
        def setModel(self, model):
            '''void Akonadi.EntityTreeView.setModel(QAbstractItemModel model)'''
        def setXmlGuiClient(self, xmlGuiClient):
            '''void Akonadi.EntityTreeView.setXmlGuiClient(KXMLGUIClient xmlGuiClient)'''
    class ItemModifyJob(Akonadi.Job):
        """"""
        def __init__(self, item, parent = None):
            '''void Akonadi.ItemModifyJob.__init__(Akonadi.Item item, QObject parent = None)'''
        def __init__(self, items, parent = None):
            '''void Akonadi.ItemModifyJob.__init__(list-of-Akonadi.Item items, QObject parent = None)'''
        def disableAutomaticConflictHandling(self):
            '''void Akonadi.ItemModifyJob.disableAutomaticConflictHandling()'''
        def items(self):
            '''list-of-Akonadi.Item Akonadi.ItemModifyJob.items()'''
            return [Akonadi.Item()]
        def doHandleResponse(self, tag, data):
            '''void Akonadi.ItemModifyJob.doHandleResponse(QByteArray tag, QByteArray data)'''
        def doStart(self):
            '''void Akonadi.ItemModifyJob.doStart()'''
        def item(self):
            '''Akonadi.Item Akonadi.ItemModifyJob.item()'''
            return Akonadi.Item()
        def disableRevisionCheck(self):
            '''void Akonadi.ItemModifyJob.disableRevisionCheck()'''
        def ignorePayload(self):
            '''bool Akonadi.ItemModifyJob.ignorePayload()'''
            return bool()
        def setIgnorePayload(self, ignore):
            '''void Akonadi.ItemModifyJob.setIgnorePayload(bool ignore)'''
    class ItemSerializerPlugin():
        """"""
        def __init__(self):
            '''void Akonadi.ItemSerializerPlugin.__init__()'''
        def __init__(self):
            '''Akonadi.ItemSerializerPlugin Akonadi.ItemSerializerPlugin.__init__()'''
            return Akonadi.ItemSerializerPlugin()
        def parts(self, item):
            '''list-of-QByteArray Akonadi.ItemSerializerPlugin.parts(Akonadi.Item item)'''
            return [QByteArray()]
        def serialize(self, item, label, data, version):
            '''abstract void Akonadi.ItemSerializerPlugin.serialize(Akonadi.Item item, QByteArray label, QIODevice data, int version)'''
        def deserialize(self, item, label, data, version):
            '''abstract bool Akonadi.ItemSerializerPlugin.deserialize(Akonadi.Item item, QByteArray label, QIODevice data, int version)'''
            return bool()
    class TransportResourceBase():
        """"""
        # Enum Akonadi.TransportResourceBase.TransportResult
        TransportSucceeded = 0
        TransportFailed = 0
    
        def __init__(self):
            '''void Akonadi.TransportResourceBase.__init__()'''
        def __init__(self):
            '''Akonadi.TransportResourceBase Akonadi.TransportResourceBase.__init__()'''
            return Akonadi.TransportResourceBase()
        def itemSent(self, item, result, message = QString()):
            '''void Akonadi.TransportResourceBase.itemSent(Akonadi.Item item, Akonadi.TransportResourceBase.TransportResult result, QString message = QString())'''
        def sendItem(self, item):
            '''abstract void Akonadi.TransportResourceBase.sendItem(Akonadi.Item item)'''
    class MessageThreaderProxyModel(QAbstractProxyModel):
        """"""
        def __init__(self, parent = None):
            '''void Akonadi.MessageThreaderProxyModel.__init__(QObject parent = None)'''
        def setSourceModel(self, sourceMessageModel):
            '''void Akonadi.MessageThreaderProxyModel.setSourceModel(QAbstractItemModel sourceMessageModel)'''
        def mapToSource(self, index):
            '''QModelIndex Akonadi.MessageThreaderProxyModel.mapToSource(QModelIndex index)'''
            return QModelIndex()
        def mapFromSource(self, index):
            '''QModelIndex Akonadi.MessageThreaderProxyModel.mapFromSource(QModelIndex index)'''
            return QModelIndex()
        def mimeData(self, indexes):
            '''QMimeData Akonadi.MessageThreaderProxyModel.mimeData(list-of-QModelIndex indexes)'''
            return QMimeData()
        def mimeTypes(self):
            '''QStringList Akonadi.MessageThreaderProxyModel.mimeTypes()'''
            return QStringList()
        def columnCount(self, index):
            '''int Akonadi.MessageThreaderProxyModel.columnCount(QModelIndex index)'''
            return int()
        def createIndex(self, row, column, internalId):
            '''QModelIndex Akonadi.MessageThreaderProxyModel.createIndex(int row, int column, int internalId)'''
            return QModelIndex()
        def hasChildren(self, index):
            '''bool Akonadi.MessageThreaderProxyModel.hasChildren(QModelIndex index)'''
            return bool()
        def index(self, row, column, parent):
            '''QModelIndex Akonadi.MessageThreaderProxyModel.index(int row, int column, QModelIndex parent)'''
            return QModelIndex()
        def rowCount(self, index):
            '''int Akonadi.MessageThreaderProxyModel.rowCount(QModelIndex index)'''
            return int()
        def parent(self, index):
            '''QModelIndex Akonadi.MessageThreaderProxyModel.parent(QModelIndex index)'''
            return QModelIndex()
    class CollectionQuotaAttribute(Akonadi.Attribute):
        """"""
        def __init__(self):
            '''void Akonadi.CollectionQuotaAttribute.__init__()'''
        def __init__(self, currentValue, maxValue):
            '''void Akonadi.CollectionQuotaAttribute.__init__(int currentValue, int maxValue)'''
        def deserialize(self, data):
            '''void Akonadi.CollectionQuotaAttribute.deserialize(QByteArray data)'''
        def serialized(self):
            '''QByteArray Akonadi.CollectionQuotaAttribute.serialized()'''
            return QByteArray()
        def clone(self):
            '''Akonadi.Attribute Akonadi.CollectionQuotaAttribute.clone()'''
            return Akonadi.Attribute()
        def type(self):
            '''QByteArray Akonadi.CollectionQuotaAttribute.type()'''
            return QByteArray()
        def maximumValue(self):
            '''int Akonadi.CollectionQuotaAttribute.maximumValue()'''
            return int()
        def currentValue(self):
            '''int Akonadi.CollectionQuotaAttribute.currentValue()'''
            return int()
        def setMaximumValue(self, value):
            '''void Akonadi.CollectionQuotaAttribute.setMaximumValue(int value)'''
        def setCurrentValue(self, value):
            '''void Akonadi.CollectionQuotaAttribute.setCurrentValue(int value)'''
    class Entity():
        """"""
        # Enum Akonadi.Entity.CreateOption
        AddIfMissing = 0
    
        def __init__(self, other):
            '''void Akonadi.Entity.__init__(Akonadi.Entity other)'''
        def __ge__(self, other):
            '''bool Akonadi.Entity.__ge__(Akonadi.Entity other)'''
            return bool()
        def __lt__(self, other):
            '''bool Akonadi.Entity.__lt__(Akonadi.Entity other)'''
            return bool()
        def remoteRevision(self):
            '''QString Akonadi.Entity.remoteRevision()'''
            return QString()
        def setRemoteRevision(self, revision):
            '''void Akonadi.Entity.setRemoteRevision(QString revision)'''
        def setParentCollection(self, parent):
            '''void Akonadi.Entity.setParentCollection(Akonadi.Collection parent)'''
        def parentCollection(self):
            '''Akonadi.Collection Akonadi.Entity.parentCollection()'''
            return Akonadi.Collection()
        def setId(self, identifier):
            '''void Akonadi.Entity.setId(int identifier)'''
        def attribute(self, name):
            '''Akonadi.Attribute Akonadi.Entity.attribute(QByteArray name)'''
            return Akonadi.Attribute()
        def clearAttributes(self):
            '''void Akonadi.Entity.clearAttributes()'''
        def attributes(self):
            '''list-of-Akonadi.Attribute Akonadi.Entity.attributes()'''
            return [Akonadi.Attribute()]
        def hasAttribute(self, name):
            '''bool Akonadi.Entity.hasAttribute(QByteArray name)'''
            return bool()
        def removeAttribute(self, name):
            '''void Akonadi.Entity.removeAttribute(QByteArray name)'''
        def addAttribute(self, attribute):
            '''void Akonadi.Entity.addAttribute(Akonadi.Attribute attribute)'''
        def __ne__(self, other):
            '''bool Akonadi.Entity.__ne__(Akonadi.Entity other)'''
            return bool()
        def __eq__(self, other):
            '''bool Akonadi.Entity.__eq__(Akonadi.Entity other)'''
            return bool()
        def isValid(self):
            '''bool Akonadi.Entity.isValid()'''
            return bool()
        def remoteId(self):
            '''QString Akonadi.Entity.remoteId()'''
            return QString()
        def setRemoteId(self, id):
            '''void Akonadi.Entity.setRemoteId(QString id)'''
        def id(self):
            '''int Akonadi.Entity.id()'''
            return int()
    class AgentInstanceModel(QAbstractItemModel):
        """"""
        # Enum Akonadi.AgentInstanceModel.Roles
        TypeRole = 0
        TypeIdentifierRole = 0
        DescriptionRole = 0
        MimeTypesRole = 0
        CapabilitiesRole = 0
        InstanceRole = 0
        InstanceIdentifierRole = 0
        StatusRole = 0
        StatusMessageRole = 0
        ProgressRole = 0
        OnlineRole = 0
        UserRole = 0
    
        def __init__(self, parent = None):
            '''void Akonadi.AgentInstanceModel.__init__(QObject parent = None)'''
        def setData(self, index, value, role):
            '''bool Akonadi.AgentInstanceModel.setData(QModelIndex index, QVariant value, int role)'''
            return bool()
        def flags(self, index):
            '''Qt.ItemFlags Akonadi.AgentInstanceModel.flags(QModelIndex index)'''
            return Qt.ItemFlags()
        def parent(self, index):
            '''QModelIndex Akonadi.AgentInstanceModel.parent(QModelIndex index)'''
            return QModelIndex()
        def index(self, row, column, parent = QModelIndex()):
            '''QModelIndex Akonadi.AgentInstanceModel.index(int row, int column, QModelIndex parent = QModelIndex())'''
            return QModelIndex()
        def headerData(self, section, orientation, role = None):
            '''QVariant Akonadi.AgentInstanceModel.headerData(int section, Qt.Orientation orientation, int role = Qt.DisplayRole)'''
            return QVariant()
        def data(self, index, role = None):
            '''QVariant Akonadi.AgentInstanceModel.data(QModelIndex index, int role = Qt.DisplayRole)'''
            return QVariant()
        def rowCount(self, parent = QModelIndex()):
            '''int Akonadi.AgentInstanceModel.rowCount(QModelIndex parent = QModelIndex())'''
            return int()
        def columnCount(self, parent = QModelIndex()):
            '''int Akonadi.AgentInstanceModel.columnCount(QModelIndex parent = QModelIndex())'''
            return int()
    class ItemCreateJob(Akonadi.Job):
        """"""
        def __init__(self, item, collection, parent = None):
            '''void Akonadi.ItemCreateJob.__init__(Akonadi.Item item, Akonadi.Collection collection, QObject parent = None)'''
        def doHandleResponse(self, tag, data):
            '''void Akonadi.ItemCreateJob.doHandleResponse(QByteArray tag, QByteArray data)'''
        def doStart(self):
            '''void Akonadi.ItemCreateJob.doStart()'''
        def item(self):
            '''Akonadi.Item Akonadi.ItemCreateJob.item()'''
            return Akonadi.Item()
    class Collection(Akonadi.Entity):
        """"""
        # Enum Akonadi.Collection.UrlType
        UrlShort = 0
        UrlWithName = 0
    
        # Enum Akonadi.Collection.Right
        ReadOnly = 0
        CanChangeItem = 0
        CanCreateItem = 0
        CanDeleteItem = 0
        CanChangeCollection = 0
        CanCreateCollection = 0
        CanDeleteCollection = 0
        CanLinkItem = 0
        CanUnlinkItem = 0
        AllRights = 0
    
        def __init__(self):
            '''void Akonadi.Collection.__init__()'''
        def __init__(self, other):
            '''void Akonadi.Collection.__init__(Akonadi.Collection other)'''
        def __init__(self, id):
            '''void Akonadi.Collection.__init__(int id)'''
        def isVirtual(self):
            '''bool Akonadi.Collection.isVirtual()'''
            return bool()
        def url(self):
            '''KUrl Akonadi.Collection.url()'''
            return KUrl()
        def url(self, type):
            '''KUrl Akonadi.Collection.url(Akonadi.Collection.UrlType type)'''
            return KUrl()
        def setStatistics(self, statistics):
            '''void Akonadi.Collection.setStatistics(Akonadi.CollectionStatistics statistics)'''
        def statistics(self):
            '''Akonadi.CollectionStatistics Akonadi.Collection.statistics()'''
            return Akonadi.CollectionStatistics()
        def setCachePolicy(self, policy):
            '''void Akonadi.Collection.setCachePolicy(Akonadi.CachePolicy policy)'''
        def cachePolicy(self):
            '''Akonadi.CachePolicy Akonadi.Collection.cachePolicy()'''
            return Akonadi.CachePolicy()
        def setResource(self, identifier):
            '''void Akonadi.Collection.setResource(QString identifier)'''
        def resource(self):
            '''QString Akonadi.Collection.resource()'''
            return QString()
        def mimeType(self):
            '''static QString Akonadi.Collection.mimeType()'''
            return QString()
        def root(self):
            '''static Akonadi.Collection Akonadi.Collection.root()'''
            return Akonadi.Collection()
        def setParentRemoteId(self, identifier):
            '''void Akonadi.Collection.setParentRemoteId(QString identifier)'''
        def parentRemoteId(self):
            '''QString Akonadi.Collection.parentRemoteId()'''
            return QString()
        def setParent(self, collection):
            '''void Akonadi.Collection.setParent(Akonadi.Collection collection)'''
        def setParent(self, parent):
            '''void Akonadi.Collection.setParent(int parent)'''
        def parent(self):
            '''int Akonadi.Collection.parent()'''
            return int()
        def setContentMimeTypes(self, types):
            '''void Akonadi.Collection.setContentMimeTypes(QStringList types)'''
        def contentMimeTypes(self):
            '''QStringList Akonadi.Collection.contentMimeTypes()'''
            return QStringList()
        def setRights(self, rights):
            '''void Akonadi.Collection.setRights(Akonadi.Collection.Rights rights)'''
        def rights(self):
            '''Akonadi.Collection.Rights Akonadi.Collection.rights()'''
            return Akonadi.Collection.Rights()
        def setName(self, name):
            '''void Akonadi.Collection.setName(QString name)'''
        def name(self):
            '''QString Akonadi.Collection.name()'''
            return QString()
        def fromUrl(self, url):
            '''static Akonadi.Collection Akonadi.Collection.fromUrl(KUrl url)'''
            return Akonadi.Collection()
    class ResourceSettings(Akonadi.ResourceBaseSettings):
        """"""
        def self(self):
            '''static Akonadi.ResourceSettings Akonadi.ResourceSettings.self()'''
            return Akonadi.ResourceSettings()
    class TrashFilterProxyModel(KRecursiveFilterProxyModel):
        """"""
        def __init__(self, parent = None):
            '''void Akonadi.TrashFilterProxyModel.__init__(QObject parent = None)'''
        def acceptRow(self, sourceRow, sourceParent):
            '''bool Akonadi.TrashFilterProxyModel.acceptRow(int sourceRow, QModelIndex sourceParent)'''
            return bool()
        def trashIsShown(self):
            '''bool Akonadi.TrashFilterProxyModel.trashIsShown()'''
            return bool()
        def showTrash(self, enable):
            '''void Akonadi.TrashFilterProxyModel.showTrash(bool enable)'''
    class ItemMoveJob(Akonadi.Job):
        """"""
        def __init__(self, item, destination, parent = None):
            '''void Akonadi.ItemMoveJob.__init__(Akonadi.Item item, Akonadi.Collection destination, QObject parent = None)'''
        def __init__(self, items, destination, parent = None):
            '''void Akonadi.ItemMoveJob.__init__(list-of-Akonadi.Item items, Akonadi.Collection destination, QObject parent = None)'''
        def items(self):
            '''list-of-Akonadi.Item Akonadi.ItemMoveJob.items()'''
            return [Akonadi.Item()]
        def destinationCollection(self):
            '''Akonadi.Collection Akonadi.ItemMoveJob.destinationCollection()'''
            return Akonadi.Collection()
        def doStart(self):
            '''void Akonadi.ItemMoveJob.doStart()'''
    class Session(QObject):
        """"""
        def __init__(self, sessionId = QByteArray(), parent = None):
            '''void Akonadi.Session.__init__(QByteArray sessionId = QByteArray(), QObject parent = None)'''
        reconnected = pyqtSignal() # void reconnected() - signal
        def clear(self):
            '''void Akonadi.Session.clear()'''
        def defaultSession(self):
            '''static Akonadi.Session Akonadi.Session.defaultSession()'''
            return Akonadi.Session()
        def sessionId(self):
            '''QByteArray Akonadi.Session.sessionId()'''
            return QByteArray()
    class CollectionStatisticsJob(Akonadi.Job):
        """"""
        def __init__(self, collection, parent = None):
            '''void Akonadi.CollectionStatisticsJob.__init__(Akonadi.Collection collection, QObject parent = None)'''
        def doHandleResponse(self, tag, data):
            '''void Akonadi.CollectionStatisticsJob.doHandleResponse(QByteArray tag, QByteArray data)'''
        def doStart(self):
            '''void Akonadi.CollectionStatisticsJob.doStart()'''
        def collection(self):
            '''Akonadi.Collection Akonadi.CollectionStatisticsJob.collection()'''
            return Akonadi.Collection()
        def statistics(self):
            '''Akonadi.CollectionStatistics Akonadi.CollectionStatisticsJob.statistics()'''
            return Akonadi.CollectionStatistics()
    class CollectionFetchScope():
        """"""
        # Enum Akonadi.CollectionFetchScope.AncestorRetrieval
        __kdevpythondocumentation_builtin_None = 0
        Parent = 0
        All = 0
    
        def __init__(self):
            '''void Akonadi.CollectionFetchScope.__init__()'''
        def __init__(self, other):
            '''void Akonadi.CollectionFetchScope.__init__(Akonadi.CollectionFetchScope other)'''
        def includeUnsubscribed(self):
            '''bool Akonadi.CollectionFetchScope.includeUnsubscribed()'''
            return bool()
        def isEmpty(self):
            '''bool Akonadi.CollectionFetchScope.isEmpty()'''
            return bool()
        def ancestorRetrieval(self):
            '''Akonadi.CollectionFetchScope.AncestorRetrieval Akonadi.CollectionFetchScope.ancestorRetrieval()'''
            return Akonadi.CollectionFetchScope.AncestorRetrieval()
        def setAncestorRetrieval(self, ancestorDepth):
            '''void Akonadi.CollectionFetchScope.setAncestorRetrieval(Akonadi.CollectionFetchScope.AncestorRetrieval ancestorDepth)'''
        def contentMimeTypes(self):
            '''QStringList Akonadi.CollectionFetchScope.contentMimeTypes()'''
            return QStringList()
        def setContentMimeTypes(self, mimeTypes):
            '''void Akonadi.CollectionFetchScope.setContentMimeTypes(QStringList mimeTypes)'''
        def setResource(self, resource):
            '''void Akonadi.CollectionFetchScope.setResource(QString resource)'''
        def resource(self):
            '''QString Akonadi.CollectionFetchScope.resource()'''
            return QString()
        def setIncludeStatistics(self, include):
            '''void Akonadi.CollectionFetchScope.setIncludeStatistics(bool include)'''
        def includeStatistics(self):
            '''bool Akonadi.CollectionFetchScope.includeStatistics()'''
            return bool()
        def setIncludeUnsubscribed(self, include):
            '''void Akonadi.CollectionFetchScope.setIncludeUnsubscribed(bool include)'''
        def includeUnubscribed(self):
            '''bool Akonadi.CollectionFetchScope.includeUnubscribed()'''
            return bool()
    class CollectionDeleteJob(Akonadi.Job):
        """"""
        def __init__(self, collection, parent = None):
            '''void Akonadi.CollectionDeleteJob.__init__(Akonadi.Collection collection, QObject parent = None)'''
        def doStart(self):
            '''void Akonadi.CollectionDeleteJob.doStart()'''
    class TrashRestoreJob(Akonadi.Job):
        """"""
        def __init__(self, item, parent = None):
            '''void Akonadi.TrashRestoreJob.__init__(Akonadi.Item item, QObject parent = None)'''
        def __init__(self, items, parent = None):
            '''void Akonadi.TrashRestoreJob.__init__(list-of-Akonadi.Item items, QObject parent = None)'''
        def __init__(self, collection, parent = None):
            '''void Akonadi.TrashRestoreJob.__init__(Akonadi.Collection collection, QObject parent = None)'''
        def doStart(self):
            '''void Akonadi.TrashRestoreJob.doStart()'''
        def items(self):
            '''list-of-Akonadi.Item Akonadi.TrashRestoreJob.items()'''
            return [Akonadi.Item()]
        def setTargetCollection(self, collection):
            '''void Akonadi.TrashRestoreJob.setTargetCollection(Akonadi.Collection collection)'''
    class TransactionSequence(Akonadi.Job):
        """"""
        def __init__(self, parent = None):
            '''void Akonadi.TransactionSequence.__init__(QObject parent = None)'''
        def rollback(self):
            '''void Akonadi.TransactionSequence.rollback()'''
        def setAutomaticCommittingEnabled(self, enable):
            '''void Akonadi.TransactionSequence.setAutomaticCommittingEnabled(bool enable)'''
        def setIgnoreJobFailure(self, job):
            '''void Akonadi.TransactionSequence.setIgnoreJobFailure(KJob job)'''
        def slotResult(self, job):
            '''void Akonadi.TransactionSequence.slotResult(KJob job)'''
        def doStart(self):
            '''void Akonadi.TransactionSequence.doStart()'''
        def addSubjob(self, job):
            '''bool Akonadi.TransactionSequence.addSubjob(KJob job)'''
            return bool()
        def commit(self):
            '''void Akonadi.TransactionSequence.commit()'''
    class StatisticsProxyModel(QSortFilterProxyModel):
        """"""
        def __init__(self, parent = None):
            '''void Akonadi.StatisticsProxyModel.__init__(QObject parent = None)'''
        def setSourceModel(self, sourceModel):
            '''void Akonadi.StatisticsProxyModel.setSourceModel(QAbstractItemModel sourceModel)'''
        def match(self, start, role, value, hits = 1, flags = None):
            '''list-of-QModelIndex Akonadi.StatisticsProxyModel.match(QModelIndex start, int role, QVariant value, int hits = 1, Qt.MatchFlags flags = Qt.MatchFlags(Qt.MatchStartsWith|Qt.MatchWrap))'''
            return [QModelIndex()]
        def columnCount(self, parent = QModelIndex()):
            '''int Akonadi.StatisticsProxyModel.columnCount(QModelIndex parent = QModelIndex())'''
            return int()
        def flags(self, index):
            '''Qt.ItemFlags Akonadi.StatisticsProxyModel.flags(QModelIndex index)'''
            return Qt.ItemFlags()
        def headerData(self, section, orientation, role = None):
            '''QVariant Akonadi.StatisticsProxyModel.headerData(int section, Qt.Orientation orientation, int role = Qt.DisplayRole)'''
            return QVariant()
        def data(self, index, role = None):
            '''QVariant Akonadi.StatisticsProxyModel.data(QModelIndex index, int role = Qt.DisplayRole)'''
            return QVariant()
        def index(self, row, column, parent = QModelIndex()):
            '''QModelIndex Akonadi.StatisticsProxyModel.index(int row, int column, QModelIndex parent = QModelIndex())'''
            return QModelIndex()
        def isExtraColumnsEnabled(self):
            '''bool Akonadi.StatisticsProxyModel.isExtraColumnsEnabled()'''
            return bool()
        def setExtraColumnsEnabled(self, enable):
            '''void Akonadi.StatisticsProxyModel.setExtraColumnsEnabled(bool enable)'''
        def isToolTipEnabled(self):
            '''bool Akonadi.StatisticsProxyModel.isToolTipEnabled()'''
            return bool()
        def setToolTipEnabled(self, enable):
            '''void Akonadi.StatisticsProxyModel.setToolTipEnabled(bool enable)'''
    class ItemFetchScope():
        """"""
        # Enum Akonadi.ItemFetchScope.AncestorRetrieval
        __kdevpythondocumentation_builtin_None = 0
        Parent = 0
        All = 0
    
        def __init__(self):
            '''void Akonadi.ItemFetchScope.__init__()'''
        def __init__(self, other):
            '''void Akonadi.ItemFetchScope.__init__(Akonadi.ItemFetchScope other)'''
        def fetchModificationTime(self):
            '''bool Akonadi.ItemFetchScope.fetchModificationTime()'''
            return bool()
        def setFetchModificationTime(self, retrieveMtime):
            '''void Akonadi.ItemFetchScope.setFetchModificationTime(bool retrieveMtime)'''
        def ancestorRetrieval(self):
            '''Akonadi.ItemFetchScope.AncestorRetrieval Akonadi.ItemFetchScope.ancestorRetrieval()'''
            return Akonadi.ItemFetchScope.AncestorRetrieval()
        def setAncestorRetrieval(self, ancestorDepth):
            '''void Akonadi.ItemFetchScope.setAncestorRetrieval(Akonadi.ItemFetchScope.AncestorRetrieval ancestorDepth)'''
        def isEmpty(self):
            '''bool Akonadi.ItemFetchScope.isEmpty()'''
            return bool()
        def setCacheOnly(self, cacheOnly):
            '''void Akonadi.ItemFetchScope.setCacheOnly(bool cacheOnly)'''
        def cacheOnly(self):
            '''bool Akonadi.ItemFetchScope.cacheOnly()'''
            return bool()
        def fetchAllAttributes(self, fetch = True):
            '''void Akonadi.ItemFetchScope.fetchAllAttributes(bool fetch = True)'''
        def allAttributes(self):
            '''bool Akonadi.ItemFetchScope.allAttributes()'''
            return bool()
        def fetchAttribute(self, type, fetch = True):
            '''void Akonadi.ItemFetchScope.fetchAttribute(QByteArray type, bool fetch = True)'''
        def attributes(self):
            '''list-of-QByteArray Akonadi.ItemFetchScope.attributes()'''
            return [QByteArray()]
        def fetchFullPayload(self, fetch = True):
            '''void Akonadi.ItemFetchScope.fetchFullPayload(bool fetch = True)'''
        def fullPayload(self):
            '''bool Akonadi.ItemFetchScope.fullPayload()'''
            return bool()
        def fetchPayloadPart(self, part, fetch = True):
            '''void Akonadi.ItemFetchScope.fetchPayloadPart(QByteArray part, bool fetch = True)'''
        def payloadParts(self):
            '''list-of-QByteArray Akonadi.ItemFetchScope.payloadParts()'''
            return [QByteArray()]
    class PersistentSearchAttribute(Akonadi.Attribute):
        """"""
        def __init__(self):
            '''void Akonadi.PersistentSearchAttribute.__init__()'''
        def __init__(self):
            '''Akonadi.PersistentSearchAttribute Akonadi.PersistentSearchAttribute.__init__()'''
            return Akonadi.PersistentSearchAttribute()
        def deserialize(self, data):
            '''void Akonadi.PersistentSearchAttribute.deserialize(QByteArray data)'''
        def serialized(self):
            '''QByteArray Akonadi.PersistentSearchAttribute.serialized()'''
            return QByteArray()
        def clone(self):
            '''Akonadi.Attribute Akonadi.PersistentSearchAttribute.clone()'''
            return Akonadi.Attribute()
        def type(self):
            '''QByteArray Akonadi.PersistentSearchAttribute.type()'''
            return QByteArray()
        def setQueryString(self, query):
            '''void Akonadi.PersistentSearchAttribute.setQueryString(QString query)'''
        def queryString(self):
            '''QString Akonadi.PersistentSearchAttribute.queryString()'''
            return QString()
        def setQueryLanguage(self, language):
            '''void Akonadi.PersistentSearchAttribute.setQueryLanguage(QString language)'''
        def queryLanguage(self):
            '''QString Akonadi.PersistentSearchAttribute.queryLanguage()'''
            return QString()
    class ServerManager(QObject):
        """"""
        # Enum Akonadi.ServerManager.State
        NotRunning = 0
        Starting = 0
        Running = 0
        Stopping = 0
        Broken = 0
    
        def __init__(self):
            '''void Akonadi.ServerManager.__init__()'''
        stateChanged = pyqtSignal() # void stateChanged(Akonadi::ServerManager::State) - signal
        def state(self):
            '''static Akonadi.ServerManager.State Akonadi.ServerManager.state()'''
            return Akonadi.ServerManager.State()
        stopped = pyqtSignal() # void stopped() - signal
        started = pyqtSignal() # void started() - signal
        def self(self):
            '''static Akonadi.ServerManager Akonadi.ServerManager.self()'''
            return Akonadi.ServerManager()
        def isRunning(self):
            '''static bool Akonadi.ServerManager.isRunning()'''
            return bool()
        def showSelfTestDialog(self, parent):
            '''static void Akonadi.ServerManager.showSelfTestDialog(QWidget parent)'''
        def stop(self):
            '''static bool Akonadi.ServerManager.stop()'''
            return bool()
        def start(self):
            '''static bool Akonadi.ServerManager.start()'''
            return bool()
    class CollectionPropertiesPage(QWidget):
        """"""
        def __init__(self, parent = None):
            '''void Akonadi.CollectionPropertiesPage.__init__(QWidget parent = None)'''
        def pageTitle(self):
            '''QString Akonadi.CollectionPropertiesPage.pageTitle()'''
            return QString()
        def setPageTitle(self, title):
            '''void Akonadi.CollectionPropertiesPage.setPageTitle(QString title)'''
        def canHandle(self, collection):
            '''bool Akonadi.CollectionPropertiesPage.canHandle(Akonadi.Collection collection)'''
            return bool()
        def save(self, collection):
            '''abstract void Akonadi.CollectionPropertiesPage.save(Akonadi.Collection collection)'''
        def load(self, collection):
            '''abstract void Akonadi.CollectionPropertiesPage.load(Akonadi.Collection collection)'''
    class CollectionComboBox(KComboBox):
        """"""
        def __init__(self, parent = None):
            '''void Akonadi.CollectionComboBox.__init__(QWidget parent = None)'''
        def __init__(self, model, parent = None):
            '''void Akonadi.CollectionComboBox.__init__(QAbstractItemModel model, QWidget parent = None)'''
        currentChanged = pyqtSignal() # void currentChanged(const Akonadi::Collectionamp;) - signal
        def currentCollection(self):
            '''Akonadi.Collection Akonadi.CollectionComboBox.currentCollection()'''
            return Akonadi.Collection()
        def setDefaultCollection(self, collection):
            '''void Akonadi.CollectionComboBox.setDefaultCollection(Akonadi.Collection collection)'''
        def accessRightsFilter(self):
            '''Akonadi.Collection.Rights Akonadi.CollectionComboBox.accessRightsFilter()'''
            return Akonadi.Collection.Rights()
        def setAccessRightsFilter(self, rights):
            '''void Akonadi.CollectionComboBox.setAccessRightsFilter(Akonadi.Collection.Rights rights)'''
        def mimeTypeFilter(self):
            '''QStringList Akonadi.CollectionComboBox.mimeTypeFilter()'''
            return QStringList()
        def setMimeTypeFilter(self, mimetypes):
            '''void Akonadi.CollectionComboBox.setMimeTypeFilter(QStringList mimetypes)'''
    class ItemDeleteJob(Akonadi.Job):
        """"""
        def __init__(self, item, parent = None):
            '''void Akonadi.ItemDeleteJob.__init__(Akonadi.Item item, QObject parent = None)'''
        def __init__(self, items, parent = None):
            '''void Akonadi.ItemDeleteJob.__init__(list-of-Akonadi.Item items, QObject parent = None)'''
        def __init__(self, collection, parent = None):
            '''void Akonadi.ItemDeleteJob.__init__(Akonadi.Collection collection, QObject parent = None)'''
        def deletedItems(self):
            '''list-of-Akonadi.Item Akonadi.ItemDeleteJob.deletedItems()'''
            return [Akonadi.Item()]
        def doStart(self):
            '''void Akonadi.ItemDeleteJob.doStart()'''
    class ItemSerializerPluginV2(Akonadi.ItemSerializerPlugin):
        """"""
        def __init__(self):
            '''void Akonadi.ItemSerializerPluginV2.__init__()'''
        def __init__(self):
            '''Akonadi.ItemSerializerPluginV2 Akonadi.ItemSerializerPluginV2.__init__()'''
            return Akonadi.ItemSerializerPluginV2()
        def availableParts(self, item):
            '''list-of-QByteArray Akonadi.ItemSerializerPluginV2.availableParts(Akonadi.Item item)'''
            return [QByteArray()]
        def apply(self, item, other):
            '''void Akonadi.ItemSerializerPluginV2.apply(Akonadi.Item item, Akonadi.Item other)'''
    class ItemFetchJob(Akonadi.Job):
        """"""
        def __init__(self, collection, parent = None):
            '''void Akonadi.ItemFetchJob.__init__(Akonadi.Collection collection, QObject parent = None)'''
        def __init__(self, item, parent = None):
            '''void Akonadi.ItemFetchJob.__init__(Akonadi.Item item, QObject parent = None)'''
        def __init__(self, items, parent = None):
            '''void Akonadi.ItemFetchJob.__init__(list-of-Akonadi.Item items, QObject parent = None)'''
        def setFetchScope(self, fetchScope):
            '''void Akonadi.ItemFetchJob.setFetchScope(Akonadi.ItemFetchScope fetchScope)'''
        def doHandleResponse(self, tag, data):
            '''void Akonadi.ItemFetchJob.doHandleResponse(QByteArray tag, QByteArray data)'''
        def doStart(self):
            '''void Akonadi.ItemFetchJob.doStart()'''
        itemsReceived = pyqtSignal() # void itemsReceived(const Akonadi::Item::Listamp;) - signal
        def setCollection(self, collection):
            '''void Akonadi.ItemFetchJob.setCollection(Akonadi.Collection collection)'''
        def fetchScope(self):
            '''Akonadi.ItemFetchScope Akonadi.ItemFetchJob.fetchScope()'''
            return Akonadi.ItemFetchScope()
        def items(self):
            '''list-of-Akonadi.Item Akonadi.ItemFetchJob.items()'''
            return [Akonadi.Item()]
    class EntityRightsFilterModel(KRecursiveFilterProxyModel):
        """"""
        def __init__(self, parent = None):
            '''void Akonadi.EntityRightsFilterModel.__init__(QObject parent = None)'''
        def acceptRow(self, sourceRow, sourceParent):
            '''bool Akonadi.EntityRightsFilterModel.acceptRow(int sourceRow, QModelIndex sourceParent)'''
            return bool()
        def match(self, start, role, value, hits = 1, flags = None):
            '''list-of-QModelIndex Akonadi.EntityRightsFilterModel.match(QModelIndex start, int role, QVariant value, int hits = 1, Qt.MatchFlags flags = Qt.MatchFlags(Qt.MatchStartsWith|Qt.MatchWrap))'''
            return [QModelIndex()]
        def flags(self, index):
            '''Qt.ItemFlags Akonadi.EntityRightsFilterModel.flags(QModelIndex index)'''
            return Qt.ItemFlags()
        def accessRights(self):
            '''Akonadi.Collection.Rights Akonadi.EntityRightsFilterModel.accessRights()'''
            return Akonadi.Collection.Rights()
        def setAccessRights(self, rights):
            '''void Akonadi.EntityRightsFilterModel.setAccessRights(Akonadi.Collection.Rights rights)'''
    class PreprocessorBase(Akonadi.AgentBase):
        """"""
        # Enum Akonadi.PreprocessorBase.ProcessingResult
        ProcessingCompleted = 0
        ProcessingDelayed = 0
        ProcessingFailed = 0
        ProcessingRefused = 0
    
        def __init__(self, id):
            '''void Akonadi.PreprocessorBase.__init__(QString id)'''
        def fetchScope(self):
            '''Akonadi.ItemFetchScope Akonadi.PreprocessorBase.fetchScope()'''
            return Akonadi.ItemFetchScope()
        def setFetchScope(self, fetchScope):
            '''void Akonadi.PreprocessorBase.setFetchScope(Akonadi.ItemFetchScope fetchScope)'''
        def finishProcessing(self, result):
            '''void Akonadi.PreprocessorBase.finishProcessing(Akonadi.PreprocessorBase.ProcessingResult result)'''
        def processItem(self, item):
            '''abstract Akonadi.PreprocessorBase.ProcessingResult Akonadi.PreprocessorBase.processItem(Akonadi.Item item)'''
            return Akonadi.PreprocessorBase.ProcessingResult()
    class UnlinkJob(Akonadi.Job):
        """"""
        def __init__(self, collection, items, parent = None):
            '''void Akonadi.UnlinkJob.__init__(Akonadi.Collection collection, list-of-Akonadi.Item items, QObject parent = None)'''
        def doStart(self):
            '''void Akonadi.UnlinkJob.doStart()'''
    class AgentInstance():
        """"""
        # Enum Akonadi.AgentInstance.Status
        Idle = 0
        Running = 0
        Broken = 0
    
        def __init__(self):
            '''void Akonadi.AgentInstance.__init__()'''
        def __init__(self, other):
            '''void Akonadi.AgentInstance.__init__(Akonadi.AgentInstance other)'''
        def __ne__(self, other):
            '''bool Akonadi.AgentInstance.__ne__(Akonadi.AgentInstance other)'''
            return bool()
        def abortCurrentTask(self):
            '''void Akonadi.AgentInstance.abortCurrentTask()'''
        def restart(self):
            '''void Akonadi.AgentInstance.restart()'''
        def reconfigure(self):
            '''void Akonadi.AgentInstance.reconfigure()'''
        def __eq__(self, other):
            '''bool Akonadi.AgentInstance.__eq__(Akonadi.AgentInstance other)'''
            return bool()
        def synchronizeCollectionTree(self):
            '''void Akonadi.AgentInstance.synchronizeCollectionTree()'''
        def synchronize(self):
            '''void Akonadi.AgentInstance.synchronize()'''
        def configure(self, parent = None):
            '''void Akonadi.AgentInstance.configure(QWidget parent = None)'''
        def setIsOnline(self, online):
            '''void Akonadi.AgentInstance.setIsOnline(bool online)'''
        def isOnline(self):
            '''bool Akonadi.AgentInstance.isOnline()'''
            return bool()
        def progress(self):
            '''int Akonadi.AgentInstance.progress()'''
            return int()
        def statusMessage(self):
            '''QString Akonadi.AgentInstance.statusMessage()'''
            return QString()
        def status(self):
            '''Akonadi.AgentInstance.Status Akonadi.AgentInstance.status()'''
            return Akonadi.AgentInstance.Status()
        def setName(self, name):
            '''void Akonadi.AgentInstance.setName(QString name)'''
        def name(self):
            '''QString Akonadi.AgentInstance.name()'''
            return QString()
        def identifier(self):
            '''QString Akonadi.AgentInstance.identifier()'''
            return QString()
        def type(self):
            '''Akonadi.AgentType Akonadi.AgentInstance.type()'''
            return Akonadi.AgentType()
        def isValid(self):
            '''bool Akonadi.AgentInstance.isValid()'''
            return bool()
    class CollectionMoveJob(Akonadi.Job):
        """"""
        def __init__(self, collection, destination, parent = None):
            '''void Akonadi.CollectionMoveJob.__init__(Akonadi.Collection collection, Akonadi.Collection destination, QObject parent = None)'''
        def doStart(self):
            '''void Akonadi.CollectionMoveJob.doStart()'''
    class Control(QObject):
        """"""
        def __init__(self):
            '''void Akonadi.Control.__init__()'''
        def widgetNeedsAkonadi(self, widget):
            '''static void Akonadi.Control.widgetNeedsAkonadi(QWidget widget)'''
        def restart(self):
            '''static bool Akonadi.Control.restart()'''
            return bool()
        def restart(self, parent):
            '''static bool Akonadi.Control.restart(QWidget parent)'''
            return bool()
        def stop(self):
            '''static bool Akonadi.Control.stop()'''
            return bool()
        def stop(self, parent):
            '''static bool Akonadi.Control.stop(QWidget parent)'''
            return bool()
        def start(self):
            '''static bool Akonadi.Control.start()'''
            return bool()
        def start(self, parent):
            '''static bool Akonadi.Control.start(QWidget parent)'''
            return bool()
    class AgentFactoryBase(QObject):
        """"""
        def __init__(self, catalogName, parent = None):
            '''void Akonadi.AgentFactoryBase.__init__(str catalogName, QObject parent = None)'''
        def createComponentData(self, identifier):
            '''void Akonadi.AgentFactoryBase.createComponentData(QString identifier)'''
        def createInstance(self, identifier):
            '''abstract QObject Akonadi.AgentFactoryBase.createInstance(QString identifier)'''
            return QObject()
    class StandardActionManager(QObject):
        """"""
        # Enum Akonadi.StandardActionManager.TextContext
        DialogTitle = 0
        DialogText = 0
        MessageBoxTitle = 0
        MessageBoxText = 0
        MessageBoxAlternativeText = 0
        ErrorMessageTitle = 0
        ErrorMessageText = 0
    
        # Enum Akonadi.StandardActionManager.Type
        CreateCollection = 0
        CopyCollections = 0
        DeleteCollections = 0
        SynchronizeCollections = 0
        CollectionProperties = 0
        CopyItems = 0
        Paste = 0
        DeleteItems = 0
        ManageLocalSubscriptions = 0
        AddToFavoriteCollections = 0
        RemoveFromFavoriteCollections = 0
        RenameFavoriteCollection = 0
        CopyCollectionToMenu = 0
        CopyItemToMenu = 0
        MoveItemToMenu = 0
        MoveCollectionToMenu = 0
        CutItems = 0
        CutCollections = 0
        CreateResource = 0
        DeleteResources = 0
        ResourceProperties = 0
        SynchronizeResources = 0
        ToggleWorkOffline = 0
        CopyCollectionToDialog = 0
        MoveCollectionToDialog = 0
        CopyItemToDialog = 0
        MoveItemToDialog = 0
        SynchronizeCollectionsRecursive = 0
        MoveCollectionsToTrash = 0
        MoveItemsToTrash = 0
        RestoreCollectionsFromTrash = 0
        RestoreItemsFromTrash = 0
        MoveToTrashRestoreCollection = 0
        MoveToTrashRestoreCollectionAlternative = 0
        MoveToTrashRestoreItem = 0
        MoveToTrashRestoreItemAlternative = 0
        SynchronizeFavoriteCollections = 0
        LastType = 0
    
        def __init__(self, actionCollection, parent = None):
            '''void Akonadi.StandardActionManager.__init__(KActionCollection actionCollection, QWidget parent = None)'''
        def createActionFolderMenu(self, menu, type):
            '''void Akonadi.StandardActionManager.createActionFolderMenu(QMenu menu, Akonadi.StandardActionManager.Type type)'''
        def setCollectionPropertiesPageNames(self, names):
            '''void Akonadi.StandardActionManager.setCollectionPropertiesPageNames(QStringList names)'''
        def setCapabilityFilter(self, capabilities):
            '''void Akonadi.StandardActionManager.setCapabilityFilter(QStringList capabilities)'''
        def setMimeTypeFilter(self, mimeTypes):
            '''void Akonadi.StandardActionManager.setMimeTypeFilter(QStringList mimeTypes)'''
        def setContextText(self, type, context, text):
            '''void Akonadi.StandardActionManager.setContextText(Akonadi.StandardActionManager.Type type, Akonadi.StandardActionManager.TextContext context, QString text)'''
        def setContextText(self, type, context, text):
            '''void Akonadi.StandardActionManager.setContextText(Akonadi.StandardActionManager.Type type, Akonadi.StandardActionManager.TextContext context, KLocalizedString text)'''
        def selectedItems(self):
            '''list-of-Akonadi.Item Akonadi.StandardActionManager.selectedItems()'''
            return [Akonadi.Item()]
        def selectedCollections(self):
            '''list-of-Akonadi.Collection Akonadi.StandardActionManager.selectedCollections()'''
            return [Akonadi.Collection()]
        def interceptAction(self, type, intercept = True):
            '''void Akonadi.StandardActionManager.interceptAction(Akonadi.StandardActionManager.Type type, bool intercept = True)'''
        def setFavoriteSelectionModel(self, selectionModel):
            '''void Akonadi.StandardActionManager.setFavoriteSelectionModel(QItemSelectionModel selectionModel)'''
        def setFavoriteCollectionsModel(self, favoritesModel):
            '''void Akonadi.StandardActionManager.setFavoriteCollectionsModel(Akonadi.FavoriteCollectionsModel favoritesModel)'''
        actionStateUpdated = pyqtSignal() # void actionStateUpdated() - signal
        def setActionText(self, type, text):
            '''void Akonadi.StandardActionManager.setActionText(Akonadi.StandardActionManager.Type type, KLocalizedString text)'''
        def action(self, type):
            '''KAction Akonadi.StandardActionManager.action(Akonadi.StandardActionManager.Type type)'''
            return KAction()
        def createAllActions(self):
            '''void Akonadi.StandardActionManager.createAllActions()'''
        def createAction(self, type):
            '''KAction Akonadi.StandardActionManager.createAction(Akonadi.StandardActionManager.Type type)'''
            return KAction()
        def setItemSelectionModel(self, selectionModel):
            '''void Akonadi.StandardActionManager.setItemSelectionModel(QItemSelectionModel selectionModel)'''
        def setCollectionSelectionModel(self, selectionModel):
            '''void Akonadi.StandardActionManager.setCollectionSelectionModel(QItemSelectionModel selectionModel)'''
    class TransactionCommitJob(Akonadi.Job):
        """"""
        def __init__(self, parent):
            '''void Akonadi.TransactionCommitJob.__init__(QObject parent)'''
        def doStart(self):
            '''void Akonadi.TransactionCommitJob.doStart()'''
    class CollectionFilterProxyModel(QSortFilterProxyModel):
        """"""
        def __init__(self, parent = None):
            '''void Akonadi.CollectionFilterProxyModel.__init__(QObject parent = None)'''
        def setExcludeVirtualCollections(self, exclude):
            '''void Akonadi.CollectionFilterProxyModel.setExcludeVirtualCollections(bool exclude)'''
        def flags(self, index):
            '''Qt.ItemFlags Akonadi.CollectionFilterProxyModel.flags(QModelIndex index)'''
            return Qt.ItemFlags()
        def filterAcceptsRow(self, sourceRow, sourceParent):
            '''bool Akonadi.CollectionFilterProxyModel.filterAcceptsRow(int sourceRow, QModelIndex sourceParent)'''
            return bool()
        def clearFilters(self):
            '''void Akonadi.CollectionFilterProxyModel.clearFilters()'''
        def mimeTypeFilters(self):
            '''QStringList Akonadi.CollectionFilterProxyModel.mimeTypeFilters()'''
            return QStringList()
        def addMimeTypeFilter(self, mimeType):
            '''void Akonadi.CollectionFilterProxyModel.addMimeTypeFilter(QString mimeType)'''
        def addMimeTypeFilters(self, mimeTypes):
            '''void Akonadi.CollectionFilterProxyModel.addMimeTypeFilters(QStringList mimeTypes)'''
    class EntityDeletedAttribute(Akonadi.Attribute):
        """"""
        def __init__(self):
            '''void Akonadi.EntityDeletedAttribute.__init__()'''
        def deserialize(self, data):
            '''void Akonadi.EntityDeletedAttribute.deserialize(QByteArray data)'''
        def serialized(self):
            '''QByteArray Akonadi.EntityDeletedAttribute.serialized()'''
            return QByteArray()
        def clone(self):
            '''Akonadi.EntityDeletedAttribute Akonadi.EntityDeletedAttribute.clone()'''
            return Akonadi.EntityDeletedAttribute()
        def type(self):
            '''QByteArray Akonadi.EntityDeletedAttribute.type()'''
            return QByteArray()
        def restoreResource(self):
            '''QString Akonadi.EntityDeletedAttribute.restoreResource()'''
            return QString()
        def restoreCollection(self):
            '''Akonadi.Collection Akonadi.EntityDeletedAttribute.restoreCollection()'''
            return Akonadi.Collection()
        def setRestoreCollection(self, col):
            '''void Akonadi.EntityDeletedAttribute.setRestoreCollection(Akonadi.Collection col)'''
    class MimeTypeChecker():
        """"""
        def __init__(self):
            '''void Akonadi.MimeTypeChecker.__init__()'''
        def __init__(self, other):
            '''void Akonadi.MimeTypeChecker.__init__(Akonadi.MimeTypeChecker other)'''
        def containsWantedMimeType(self, mimeTypes):
            '''bool Akonadi.MimeTypeChecker.containsWantedMimeType(QStringList mimeTypes)'''
            return bool()
        def isWantedMimeType(self, mimeType):
            '''bool Akonadi.MimeTypeChecker.isWantedMimeType(QString mimeType)'''
            return bool()
        def isWantedCollection(self, collection):
            '''bool Akonadi.MimeTypeChecker.isWantedCollection(Akonadi.Collection collection)'''
            return bool()
        def isWantedCollection(self, collection, wantedMimeType):
            '''static bool Akonadi.MimeTypeChecker.isWantedCollection(Akonadi.Collection collection, QString wantedMimeType)'''
            return bool()
        def isWantedItem(self, item):
            '''bool Akonadi.MimeTypeChecker.isWantedItem(Akonadi.Item item)'''
            return bool()
        def isWantedItem(self, item, wantedMimeType):
            '''static bool Akonadi.MimeTypeChecker.isWantedItem(Akonadi.Item item, QString wantedMimeType)'''
            return bool()
        def removeWantedMimeType(self, mimeType):
            '''void Akonadi.MimeTypeChecker.removeWantedMimeType(QString mimeType)'''
        def addWantedMimeType(self, mimeType):
            '''void Akonadi.MimeTypeChecker.addWantedMimeType(QString mimeType)'''
        def setWantedMimeTypes(self, mimeTypes):
            '''void Akonadi.MimeTypeChecker.setWantedMimeTypes(QStringList mimeTypes)'''
        def wantedMimeTypes(self):
            '''QStringList Akonadi.MimeTypeChecker.wantedMimeTypes()'''
            return QStringList()
    class RecursiveCollectionFilterProxyModel(KRecursiveFilterProxyModel):
        """"""
        def __init__(self, parent = None):
            '''void Akonadi.RecursiveCollectionFilterProxyModel.__init__(QObject parent = None)'''
        def columnCount(self, index):
            '''int Akonadi.RecursiveCollectionFilterProxyModel.columnCount(QModelIndex index)'''
            return int()
        def setSearchPattern(self, pattern):
            '''void Akonadi.RecursiveCollectionFilterProxyModel.setSearchPattern(QString pattern)'''
        def acceptRow(self, sourceRow, sourceParent):
            '''bool Akonadi.RecursiveCollectionFilterProxyModel.acceptRow(int sourceRow, QModelIndex sourceParent)'''
            return bool()
        def contentMimeTypeInclusionFilters(self):
            '''QStringList Akonadi.RecursiveCollectionFilterProxyModel.contentMimeTypeInclusionFilters()'''
            return QStringList()
        def setContentMimeTypeInclusionFilters(self, mimeTypes):
            '''void Akonadi.RecursiveCollectionFilterProxyModel.setContentMimeTypeInclusionFilters(QStringList mimeTypes)'''
        def clearFilters(self):
            '''void Akonadi.RecursiveCollectionFilterProxyModel.clearFilters()'''
        def addContentMimeTypeInclusionFilters(self, mimeTypes):
            '''void Akonadi.RecursiveCollectionFilterProxyModel.addContentMimeTypeInclusionFilters(QStringList mimeTypes)'''
        def addContentMimeTypeInclusionFilter(self, mimeType):
            '''void Akonadi.RecursiveCollectionFilterProxyModel.addContentMimeTypeInclusionFilter(QString mimeType)'''
    class Item(Akonadi.Entity):
        """"""
        # Enum Akonadi.Item.UrlType
        UrlShort = 0
        UrlWithMimeType = 0
    
        FullPayload = None # str - member
        def __init__(self):
            '''void Akonadi.Item.__init__()'''
        def __init__(self, mimeType):
            '''void Akonadi.Item.__init__(QString mimeType)'''
        def __init__(self, other):
            '''void Akonadi.Item.__init__(Akonadi.Item other)'''
        def __init__(self, id):
            '''void Akonadi.Item.__init__(int id)'''
        def availablePayloadMetaTypeIds(self):
            '''unknown-type Akonadi.Item.availablePayloadMetaTypeIds()'''
            return unknown-type()
        def clearPayload(self):
            '''void Akonadi.Item.clearPayload()'''
        def apply(self, other):
            '''void Akonadi.Item.apply(Akonadi.Item other)'''
        def availablePayloadParts(self):
            '''list-of-QByteArray Akonadi.Item.availablePayloadParts()'''
            return [QByteArray()]
        def url(self, type = None):
            '''KUrl Akonadi.Item.url(Akonadi.Item.UrlType type = Akonadi.Item.UrlShort)'''
            return KUrl()
        def hasPayload(self):
            '''bool Akonadi.Item.hasPayload()'''
            return bool()
        def mimeType(self):
            '''QString Akonadi.Item.mimeType()'''
            return QString()
        def setMimeType(self, mimeType):
            '''void Akonadi.Item.setMimeType(QString mimeType)'''
        def size(self):
            '''int Akonadi.Item.size()'''
            return int()
        def setSize(self, size):
            '''void Akonadi.Item.setSize(int size)'''
        def storageCollectionId(self):
            '''int Akonadi.Item.storageCollectionId()'''
            return int()
        def revision(self):
            '''int Akonadi.Item.revision()'''
            return int()
        def setRevision(self, revision):
            '''void Akonadi.Item.setRevision(int revision)'''
        def loadedPayloadParts(self):
            '''list-of-QByteArray Akonadi.Item.loadedPayloadParts()'''
            return [QByteArray()]
        def payloadData(self):
            '''QByteArray Akonadi.Item.payloadData()'''
            return QByteArray()
        def setPayloadFromData(self, data):
            '''void Akonadi.Item.setPayloadFromData(QByteArray data)'''
        def clearFlags(self):
            '''void Akonadi.Item.clearFlags()'''
        def setFlags(self, flags):
            '''void Akonadi.Item.setFlags(list-of-QByteArray flags)'''
        def clearFlag(self, name):
            '''void Akonadi.Item.clearFlag(QByteArray name)'''
        def setFlag(self, name):
            '''void Akonadi.Item.setFlag(QByteArray name)'''
        def hasFlag(self, name):
            '''bool Akonadi.Item.hasFlag(QByteArray name)'''
            return bool()
        def setModificationTime(self, datetime):
            '''void Akonadi.Item.setModificationTime(QDateTime datetime)'''
        def modificationTime(self):
            '''QDateTime Akonadi.Item.modificationTime()'''
            return QDateTime()
        def flags(self):
            '''list-of-QByteArray Akonadi.Item.flags()'''
            return [QByteArray()]
        def fromUrl(self, url):
            '''static Akonadi.Item Akonadi.Item.fromUrl(KUrl url)'''
            return Akonadi.Item()
    class CollectionStatisticsDelegate(QStyledItemDelegate):
        """"""
        def __init__(self, parent):
            '''void Akonadi.CollectionStatisticsDelegate.__init__(QTreeView parent)'''
        def __init__(self, parent):
            '''void Akonadi.CollectionStatisticsDelegate.__init__(QAbstractItemView parent)'''
        def progressAnimationEnabled(self):
            '''bool Akonadi.CollectionStatisticsDelegate.progressAnimationEnabled()'''
            return bool()
        def setProgressAnimationEnabled(self, enable):
            '''void Akonadi.CollectionStatisticsDelegate.setProgressAnimationEnabled(bool enable)'''
        def initStyleOption(self, option, index):
            '''void Akonadi.CollectionStatisticsDelegate.initStyleOption(QStyleOptionViewItem option, QModelIndex index)'''
        def paint(self, painter, option, index):
            '''void Akonadi.CollectionStatisticsDelegate.paint(QPainter painter, QStyleOptionViewItem option, QModelIndex index)'''
        def unreadCountShown(self):
            '''bool Akonadi.CollectionStatisticsDelegate.unreadCountShown()'''
            return bool()
        def setUnreadCountShown(self, enable):
            '''void Akonadi.CollectionStatisticsDelegate.setUnreadCountShown(bool enable)'''
    class MessageModel(Akonadi.ItemModel):
        """"""
        # Enum Akonadi.MessageModel.Column
        Subject = 0
        Sender = 0
        Receiver = 0
        Date = 0
        Size = 0
    
        def __init__(self, parent = None):
            '''void Akonadi.MessageModel.__init__(QObject parent = None)'''
        def mimeTypes(self):
            '''QStringList Akonadi.MessageModel.mimeTypes()'''
            return QStringList()
        def rowCount(self, parent = QModelIndex()):
            '''int Akonadi.MessageModel.rowCount(QModelIndex parent = QModelIndex())'''
            return int()
        def headerData(self, section, orientation, role = None):
            '''QVariant Akonadi.MessageModel.headerData(int section, Qt.Orientation orientation, int role = Qt.DisplayRole)'''
            return QVariant()
        def data(self, index, role = None):
            '''QVariant Akonadi.MessageModel.data(QModelIndex index, int role = Qt.DisplayRole)'''
            return QVariant()
        def columnCount(self, parent = QModelIndex()):
            '''int Akonadi.MessageModel.columnCount(QModelIndex parent = QModelIndex())'''
            return int()


def qHash(collection):
    '''static int qHash(Akonadi.Collection collection)'''
    return int()

def qHash():
    '''static Akonadi.Entity qHash()'''
    return Akonadi.Entity()

