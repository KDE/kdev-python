class pyqtSignal():
 def connect(self, targetSignal): pass
 def emit(self, *args): pass
from QtCore import *

class Nepomuk():
    """"""
    # Enum Nepomuk.ErrorCode
    NoError = 0
    CommunicationError = 0
    InvalidType = 0
    UnknownError = 0

    def RDFLiteralToValue(self, node):
        '''static Nepomuk.Variant Nepomuk.RDFLiteralToValue(Soprano.Node node)'''
        return Nepomuk.Variant()
    def valueToRDFNode(self):
        '''static Nepomuk.Variant Nepomuk.valueToRDFNode()'''
        return Nepomuk.Variant()
    def valuesToRDFNodes(self):
        '''static Nepomuk.Variant Nepomuk.valuesToRDFNodes()'''
        return Nepomuk.Variant()
    def qHash(self, res):
        '''static int Nepomuk.qHash(Nepomuk.Resource res)'''
        return int()
    def errorString(self, code):
        '''static QString Nepomuk.errorString(Nepomuk.ErrorCode code)'''
        return QString()
    def extractNamespace(self, url):
        '''static QUrl Nepomuk.extractNamespace(QUrl url)'''
        return QUrl()
    class Query():
        """"""
        class Query():
            """"""
            class SparqlFlags():
                """"""
                def __init__(self):
                    '''Nepomuk.Query.Query.SparqlFlags Nepomuk.Query.Query.SparqlFlags.__init__()'''
                    return Nepomuk.Query.Query.SparqlFlags()
                def __init__(self):
                    '''int Nepomuk.Query.Query.SparqlFlags.__init__()'''
                    return int()
                def __init__(self):
                    '''void Nepomuk.Query.Query.SparqlFlags.__init__()'''
                def __bool__(self):
                    '''int Nepomuk.Query.Query.SparqlFlags.__bool__()'''
                    return int()
                def __ne__(self, f):
                    '''bool Nepomuk.Query.Query.SparqlFlags.__ne__(Nepomuk.Query.Query.SparqlFlags f)'''
                    return bool()
                def __eq__(self, f):
                    '''bool Nepomuk.Query.Query.SparqlFlags.__eq__(Nepomuk.Query.Query.SparqlFlags f)'''
                    return bool()
                def __invert__(self):
                    '''Nepomuk.Query.Query.SparqlFlags Nepomuk.Query.Query.SparqlFlags.__invert__()'''
                    return Nepomuk.Query.Query.SparqlFlags()
                def __and__(self, mask):
                    '''Nepomuk.Query.Query.SparqlFlags Nepomuk.Query.Query.SparqlFlags.__and__(int mask)'''
                    return Nepomuk.Query.Query.SparqlFlags()
                def __xor__(self, f):
                    '''Nepomuk.Query.Query.SparqlFlags Nepomuk.Query.Query.SparqlFlags.__xor__(Nepomuk.Query.Query.SparqlFlags f)'''
                    return Nepomuk.Query.Query.SparqlFlags()
                def __xor__(self, f):
                    '''Nepomuk.Query.Query.SparqlFlags Nepomuk.Query.Query.SparqlFlags.__xor__(int f)'''
                    return Nepomuk.Query.Query.SparqlFlags()
                def __or__(self, f):
                    '''Nepomuk.Query.Query.SparqlFlags Nepomuk.Query.Query.SparqlFlags.__or__(Nepomuk.Query.Query.SparqlFlags f)'''
                    return Nepomuk.Query.Query.SparqlFlags()
                def __or__(self, f):
                    '''Nepomuk.Query.Query.SparqlFlags Nepomuk.Query.Query.SparqlFlags.__or__(int f)'''
                    return Nepomuk.Query.Query.SparqlFlags()
                def __int__(self):
                    '''int Nepomuk.Query.Query.SparqlFlags.__int__()'''
                    return int()
                def __ixor__(self, f):
                    '''Nepomuk.Query.Query.SparqlFlags Nepomuk.Query.Query.SparqlFlags.__ixor__(Nepomuk.Query.Query.SparqlFlags f)'''
                    return Nepomuk.Query.Query.SparqlFlags()
                def __ior__(self, f):
                    '''Nepomuk.Query.Query.SparqlFlags Nepomuk.Query.Query.SparqlFlags.__ior__(Nepomuk.Query.Query.SparqlFlags f)'''
                    return Nepomuk.Query.Query.SparqlFlags()
                def __iand__(self, mask):
                    '''Nepomuk.Query.Query.SparqlFlags Nepomuk.Query.Query.SparqlFlags.__iand__(int mask)'''
                    return Nepomuk.Query.Query.SparqlFlags()
    class Query():
        """"""
        class ResourceTypeTerm(Nepomuk.Query.Term):
            """"""
            def __init__(self, term):
                '''void Nepomuk.Query.ResourceTypeTerm.__init__(Nepomuk.Query.ResourceTypeTerm term)'''
            def __init__(self, type = None):
                '''void Nepomuk.Query.ResourceTypeTerm.__init__(Nepomuk.Types.Class type = Nepomuk.Types.Class())'''
            def setType(self, type):
                '''void Nepomuk.Query.ResourceTypeTerm.setType(Nepomuk.Types.Class type)'''
            def type(self):
                '''Nepomuk.Types.Class Nepomuk.Query.ResourceTypeTerm.type()'''
                return Nepomuk.Types.Class()
    class Vocabulary():
        """"""
    class Resource():
        """"""
        def __init__(self):
            '''void Nepomuk.Resource.__init__()'''
        def __init__(self, manager):
            '''void Nepomuk.Resource.__init__(Nepomuk.ResourceManager manager)'''
        def __init__(self):
            '''Nepomuk.Resource Nepomuk.Resource.__init__()'''
            return Nepomuk.Resource()
        def __init__(self, pathOrIdentifier, type = QUrl()):
            '''void Nepomuk.Resource.__init__(QString pathOrIdentifier, QUrl type = QUrl())'''
        def __init__(self, pathOrIdentifier, type, manager):
            '''void Nepomuk.Resource.__init__(QString pathOrIdentifier, QUrl type, Nepomuk.ResourceManager manager)'''
        def __init__(self, pathOrIdentifier, type):
            '''void Nepomuk.Resource.__init__(QString pathOrIdentifier, QString type)'''
        def __init__(self, uri, type = QUrl()):
            '''void Nepomuk.Resource.__init__(QUrl uri, QUrl type = QUrl())'''
        def __init__(self, uri, type, manager):
            '''void Nepomuk.Resource.__init__(QUrl uri, QUrl type, Nepomuk.ResourceManager manager)'''
        def toFile(self):
            '''Nepomuk.File Nepomuk.Resource.toFile()'''
            return Nepomuk.File()
        def isFile(self):
            '''bool Nepomuk.Resource.isFile()'''
            return bool()
        def fromResourceUri(self, uri, type = None, manager = None):
            '''static Nepomuk.Resource Nepomuk.Resource.fromResourceUri(KUrl uri, Nepomuk.Types.Class type = Nepomuk.Types.Class(), Nepomuk.ResourceManager manager = None)'''
            return Nepomuk.Resource()
        def increaseUsageCount(self):
            '''void Nepomuk.Resource.increaseUsageCount()'''
        def usageCount(self):
            '''int Nepomuk.Resource.usageCount()'''
            return int()
        def __ne__(self):
            '''Nepomuk.Resource Nepomuk.Resource.__ne__()'''
            return Nepomuk.Resource()
        def allResources(self):
            '''static list-of-Nepomuk.Resource Nepomuk.Resource.allResources()'''
            return [Nepomuk.Resource()]
        def isRelatedOf(self):
            '''list-of-Nepomuk.Resource Nepomuk.Resource.isRelatedOf()'''
            return [Nepomuk.Resource()]
        def annotationOf(self):
            '''list-of-Nepomuk.Resource Nepomuk.Resource.annotationOf()'''
            return [Nepomuk.Resource()]
        def symbolUri(self):
            '''static QString Nepomuk.Resource.symbolUri()'''
            return QString()
        def addSymbol(self, value):
            '''void Nepomuk.Resource.addSymbol(QString value)'''
        def setSymbols(self, value):
            '''void Nepomuk.Resource.setSymbols(QStringList value)'''
        def symbols(self):
            '''QStringList Nepomuk.Resource.symbols()'''
            return QStringList()
        def ratingUri(self):
            '''static QString Nepomuk.Resource.ratingUri()'''
            return QString()
        def setRating(self, value):
            '''void Nepomuk.Resource.setRating(int value)'''
        def rating(self):
            '''int Nepomuk.Resource.rating()'''
            return int()
        def labelUri(self):
            '''static QString Nepomuk.Resource.labelUri()'''
            return QString()
        def setLabel(self, value):
            '''void Nepomuk.Resource.setLabel(QString value)'''
        def label(self):
            '''QString Nepomuk.Resource.label()'''
            return QString()
        def isRelatedUri(self):
            '''static QString Nepomuk.Resource.isRelatedUri()'''
            return QString()
        def addIsRelated(self, value):
            '''void Nepomuk.Resource.addIsRelated(Nepomuk.Resource value)'''
        def setIsRelateds(self, value):
            '''void Nepomuk.Resource.setIsRelateds(list-of-Nepomuk.Resource value)'''
        def isRelateds(self):
            '''list-of-Nepomuk.Resource Nepomuk.Resource.isRelateds()'''
            return [Nepomuk.Resource()]
        def isTopicOfUri(self):
            '''static QString Nepomuk.Resource.isTopicOfUri()'''
            return QString()
        def addIsTopicOf(self, value):
            '''void Nepomuk.Resource.addIsTopicOf(Nepomuk.Resource value)'''
        def setIsTopicOfs(self, value):
            '''void Nepomuk.Resource.setIsTopicOfs(list-of-Nepomuk.Resource value)'''
        def isTopicOfs(self):
            '''list-of-Nepomuk.Resource Nepomuk.Resource.isTopicOfs()'''
            return [Nepomuk.Resource()]
        def topicUri(self):
            '''static QString Nepomuk.Resource.topicUri()'''
            return QString()
        def addTopic(self, value):
            '''void Nepomuk.Resource.addTopic(Nepomuk.Resource value)'''
        def setTopics(self, value):
            '''void Nepomuk.Resource.setTopics(list-of-Nepomuk.Resource value)'''
        def topics(self):
            '''list-of-Nepomuk.Resource Nepomuk.Resource.topics()'''
            return [Nepomuk.Resource()]
        def tagUri(self):
            '''static QString Nepomuk.Resource.tagUri()'''
            return QString()
        def addTag(self, value):
            '''void Nepomuk.Resource.addTag(Nepomuk.Tag value)'''
        def setTags(self, value):
            '''void Nepomuk.Resource.setTags(list-of-Nepomuk.Tag value)'''
        def tags(self):
            '''list-of-Nepomuk.Tag Nepomuk.Resource.tags()'''
            return [Nepomuk.Tag()]
        def annotationUri(self):
            '''static QString Nepomuk.Resource.annotationUri()'''
            return QString()
        def addAnnotation(self, value):
            '''void Nepomuk.Resource.addAnnotation(Nepomuk.Resource value)'''
        def setAnnotations(self, value):
            '''void Nepomuk.Resource.setAnnotations(list-of-Nepomuk.Resource value)'''
        def annotations(self):
            '''list-of-Nepomuk.Resource Nepomuk.Resource.annotations()'''
            return [Nepomuk.Resource()]
        def altLabelUri(self):
            '''static QString Nepomuk.Resource.altLabelUri()'''
            return QString()
        def addAltLabel(self, value):
            '''void Nepomuk.Resource.addAltLabel(QString value)'''
        def setAltLabels(self, value):
            '''void Nepomuk.Resource.setAltLabels(QStringList value)'''
        def altLabels(self):
            '''QStringList Nepomuk.Resource.altLabels()'''
            return QStringList()
        def identifierUri(self):
            '''static QString Nepomuk.Resource.identifierUri()'''
            return QString()
        def addIdentifier(self, value):
            '''void Nepomuk.Resource.addIdentifier(QString value)'''
        def setIdentifiers(self, value):
            '''void Nepomuk.Resource.setIdentifiers(QStringList value)'''
        def identifiers(self):
            '''QStringList Nepomuk.Resource.identifiers()'''
            return QStringList()
        def descriptionUri(self):
            '''static QString Nepomuk.Resource.descriptionUri()'''
            return QString()
        def setDescription(self, value):
            '''void Nepomuk.Resource.setDescription(QString value)'''
        def description(self):
            '''QString Nepomuk.Resource.description()'''
            return QString()
        def __eq__(self):
            '''Nepomuk.Resource Nepomuk.Resource.__eq__()'''
            return Nepomuk.Resource()
        def pimoThing(self):
            '''Nepomuk.Thing Nepomuk.Resource.pimoThing()'''
            return Nepomuk.Thing()
        def genericIcon(self):
            '''QString Nepomuk.Resource.genericIcon()'''
            return QString()
        def genericDescription(self):
            '''QString Nepomuk.Resource.genericDescription()'''
            return QString()
        def genericLabel(self):
            '''QString Nepomuk.Resource.genericLabel()'''
            return QString()
        def isValid(self):
            '''bool Nepomuk.Resource.isValid()'''
            return bool()
        def exists(self):
            '''bool Nepomuk.Resource.exists()'''
            return bool()
        def remove(self):
            '''void Nepomuk.Resource.remove()'''
        def removeProperty(self, uri):
            '''void Nepomuk.Resource.removeProperty(QUrl uri)'''
        def removeProperty(self, uri, value):
            '''void Nepomuk.Resource.removeProperty(QUrl uri, Nepomuk.Variant value)'''
        def removeProperty(self, uri):
            '''void Nepomuk.Resource.removeProperty(QString uri)'''
        def addProperty(self, uri, value):
            '''void Nepomuk.Resource.addProperty(QUrl uri, Nepomuk.Variant value)'''
        def setProperty(self, uri, value):
            '''void Nepomuk.Resource.setProperty(QUrl uri, Nepomuk.Variant value)'''
        def setProperty(self, uri, value):
            '''void Nepomuk.Resource.setProperty(QString uri, Nepomuk.Variant value)'''
        def property(self, uri):
            '''Nepomuk.Variant Nepomuk.Resource.property(QUrl uri)'''
            return Nepomuk.Variant()
        def property(self, uri):
            '''Nepomuk.Variant Nepomuk.Resource.property(QString uri)'''
            return Nepomuk.Variant()
        def hasProperty(self, uri):
            '''bool Nepomuk.Resource.hasProperty(QUrl uri)'''
            return bool()
        def hasProperty(self, uri):
            '''bool Nepomuk.Resource.hasProperty(QString uri)'''
            return bool()
        def hasProperty(self, p, v):
            '''bool Nepomuk.Resource.hasProperty(Nepomuk.Types.Property p, Nepomuk.Variant v)'''
            return bool()
        def properties(self):
            '''dict-of-QUrl-Nepomuk.Variant Nepomuk.Resource.properties()'''
            return dict-of-QUrl-Nepomuk.Variant()
        def allProperties(self):
            '''dict-of-QString-Nepomuk.Variant Nepomuk.Resource.allProperties()'''
            return dict-of-QString-Nepomuk.Variant()
        def className(self):
            '''QString Nepomuk.Resource.className()'''
            return QString()
        def hasType(self, typeUri):
            '''bool Nepomuk.Resource.hasType(QUrl typeUri)'''
            return bool()
        def addType(self, type):
            '''void Nepomuk.Resource.addType(QUrl type)'''
        def setTypes(self, types):
            '''void Nepomuk.Resource.setTypes(list-of-QUrl types)'''
        def types(self):
            '''list-of-QUrl Nepomuk.Resource.types()'''
            return [QUrl()]
        def resourceType(self):
            '''QUrl Nepomuk.Resource.resourceType()'''
            return QUrl()
        def type(self):
            '''QString Nepomuk.Resource.type()'''
            return QString()
        def resourceUri(self):
            '''QUrl Nepomuk.Resource.resourceUri()'''
            return QUrl()
        def uri(self):
            '''QString Nepomuk.Resource.uri()'''
            return QString()
        def manager(self):
            '''Nepomuk.ResourceManager Nepomuk.Resource.manager()'''
            return Nepomuk.ResourceManager()
    class TagWidget(QWidget):
        """"""
        # Enum Nepomuk.TagWidget.ModeFlag
        MiniMode = 0
        StandardMode = 0
        ReadOnly = 0
        DisableTagClicking = 0
    
        def __init__(self, resource, parent = None):
            '''void Nepomuk.TagWidget.__init__(Nepomuk.Resource resource, QWidget parent = None)'''
        def __init__(self, parent = None):
            '''void Nepomuk.TagWidget.__init__(QWidget parent = None)'''
        def setModeFlags(self, flags):
            '''void Nepomuk.TagWidget.setModeFlags(Nepomuk.TagWidget.ModeFlags flags)'''
        def setAlignment(self, alignment):
            '''void Nepomuk.TagWidget.setAlignment(Qt.Alignment alignment)'''
        def setMaxTagsShown(self, max):
            '''void Nepomuk.TagWidget.setMaxTagsShown(int max)'''
        def setSelectedTags(self, tags):
            '''void Nepomuk.TagWidget.setSelectedTags(list-of-Nepomuk.Tag tags)'''
        selectionChanged = pyqtSignal() # void selectionChanged(const QListlt;Nepomuk::Taggt;amp;) - signal
        def modeFlags(self):
            '''Nepomuk.TagWidget.ModeFlags Nepomuk.TagWidget.modeFlags()'''
            return Nepomuk.TagWidget.ModeFlags()
        def alignment(self):
            '''Qt.Alignment Nepomuk.TagWidget.alignment()'''
            return Qt.Alignment()
        def maxTagsShown(self):
            '''int Nepomuk.TagWidget.maxTagsShown()'''
            return int()
        def selectedTags(self):
            '''list-of-Nepomuk.Tag Nepomuk.TagWidget.selectedTags()'''
            return [Nepomuk.Tag()]
        def setAssignedTags(self, tags):
            '''void Nepomuk.TagWidget.setAssignedTags(list-of-Nepomuk.Tag tags)'''
        def setTaggedResources(self, resources):
            '''void Nepomuk.TagWidget.setTaggedResources(list-of-Nepomuk.Resource resources)'''
        def setTaggedResource(self, resource):
            '''void Nepomuk.TagWidget.setTaggedResource(Nepomuk.Resource resource)'''
        tagClicked = pyqtSignal() # void tagClicked(Nepomuk::Tag) - signal
        def assignedTags(self):
            '''list-of-Nepomuk.Tag Nepomuk.TagWidget.assignedTags()'''
            return [Nepomuk.Tag()]
        def taggedResources(self):
            '''list-of-Nepomuk.Resource Nepomuk.TagWidget.taggedResources()'''
            return [Nepomuk.Resource()]
    class Query():
        """"""
        class LiteralTerm(Nepomuk.Query.Term):
            """"""
            def __init__(self, term):
                '''void Nepomuk.Query.LiteralTerm.__init__(Nepomuk.Query.LiteralTerm term)'''
            def __init__(self, value = None):
                '''void Nepomuk.Query.LiteralTerm.__init__(Soprano.LiteralValue value = Soprano.LiteralValue())'''
            def setValue(self, value):
                '''void Nepomuk.Query.LiteralTerm.setValue(Soprano.LiteralValue value)'''
            def value(self):
                '''Soprano.LiteralValue Nepomuk.Query.LiteralTerm.value()'''
                return Soprano.LiteralValue()
    class Vocabulary():
        """"""
        class NDO():
            """"""
            def metadata(self):
                '''static QUrl Nepomuk.Vocabulary.NDO.metadata()'''
                return QUrl()
            def referrer(self):
                '''static QUrl Nepomuk.Vocabulary.NDO.referrer()'''
                return QUrl()
            def copiedFrom(self):
                '''static QUrl Nepomuk.Vocabulary.NDO.copiedFrom()'''
                return QUrl()
            def TorrentedFile(self):
                '''static QUrl Nepomuk.Vocabulary.NDO.TorrentedFile()'''
                return QUrl()
            def Torrent(self):
                '''static QUrl Nepomuk.Vocabulary.NDO.Torrent()'''
                return QUrl()
            def P2PFile(self):
                '''static QUrl Nepomuk.Vocabulary.NDO.P2PFile()'''
                return QUrl()
            def DownloadEvent(self):
                '''static QUrl Nepomuk.Vocabulary.NDO.DownloadEvent()'''
                return QUrl()
            def ndoNamespace(self):
                '''static QUrl Nepomuk.Vocabulary.NDO.ndoNamespace()'''
                return QUrl()
    class Query():
        """"""
        class ComparisonTerm(Nepomuk.Query.SimpleTerm):
            """"""
            # Enum Nepomuk.Query.ComparisonTerm.AggregateFunction
            NoAggregateFunction = 0
            Count = 0
            DistinctCount = 0
            Max = 0
            Min = 0
            Sum = 0
            DistinctSum = 0
            Average = 0
            DistinctAverage = 0
        
            # Enum Nepomuk.Query.ComparisonTerm.Comparator
            Contains = 0
            Regexp = 0
            Equal = 0
            Greater = 0
            Smaller = 0
            GreaterOrEqual = 0
            SmallerOrEqual = 0
        
            def __init__(self):
                '''void Nepomuk.Query.ComparisonTerm.__init__()'''
            def __init__(self, term):
                '''void Nepomuk.Query.ComparisonTerm.__init__(Nepomuk.Query.ComparisonTerm term)'''
            def __init__(self, property, term, comparator = None):
                '''void Nepomuk.Query.ComparisonTerm.__init__(Nepomuk.Types.Property property, Nepomuk.Query.Term term, Nepomuk.Query.ComparisonTerm.Comparator comparator = Nepomuk.Query.ComparisonTerm.Contains)'''
            def inverted(self):
                '''Nepomuk.Query.ComparisonTerm Nepomuk.Query.ComparisonTerm.inverted()'''
                return Nepomuk.Query.ComparisonTerm()
            def setInverted(self, invert):
                '''void Nepomuk.Query.ComparisonTerm.setInverted(bool invert)'''
            def isInverted(self):
                '''bool Nepomuk.Query.ComparisonTerm.isInverted()'''
                return bool()
            def sortOrder(self):
                '''Qt.SortOrder Nepomuk.Query.ComparisonTerm.sortOrder()'''
                return Qt.SortOrder()
            def sortWeight(self):
                '''int Nepomuk.Query.ComparisonTerm.sortWeight()'''
                return int()
            def setSortWeight(self, weight, sortOrder = None):
                '''void Nepomuk.Query.ComparisonTerm.setSortWeight(int weight, Qt.SortOrder sortOrder = Qt.AscendingOrder)'''
            def aggregateFunction(self):
                '''Nepomuk.Query.ComparisonTerm.AggregateFunction Nepomuk.Query.ComparisonTerm.aggregateFunction()'''
                return Nepomuk.Query.ComparisonTerm.AggregateFunction()
            def setAggregateFunction(self, function):
                '''void Nepomuk.Query.ComparisonTerm.setAggregateFunction(Nepomuk.Query.ComparisonTerm.AggregateFunction function)'''
            def variableName(self):
                '''QString Nepomuk.Query.ComparisonTerm.variableName()'''
                return QString()
            def setVariableName(self, name):
                '''void Nepomuk.Query.ComparisonTerm.setVariableName(QString name)'''
            def setProperty(self):
                '''Nepomuk.Types.Property Nepomuk.Query.ComparisonTerm.setProperty()'''
                return Nepomuk.Types.Property()
            def setComparator(self):
                '''Nepomuk.Query.ComparisonTerm.Comparator Nepomuk.Query.ComparisonTerm.setComparator()'''
                return Nepomuk.Query.ComparisonTerm.Comparator()
            def property(self):
                '''Nepomuk.Types.Property Nepomuk.Query.ComparisonTerm.property()'''
                return Nepomuk.Types.Property()
            def comparator(self):
                '''Nepomuk.Query.ComparisonTerm.Comparator Nepomuk.Query.ComparisonTerm.comparator()'''
                return Nepomuk.Query.ComparisonTerm.Comparator()
    class Query():
        """"""
        class QueryServiceClient(QObject):
            """"""
            def __init__(self, parent = None):
                '''void Nepomuk.Query.QueryServiceClient.__init__(QObject parent = None)'''
            serviceAvailabilityChanged = pyqtSignal() # void serviceAvailabilityChanged(bool) - signal
            error = pyqtSignal() # void error(const QStringamp;) - signal
            resultCount = pyqtSignal() # void resultCount(int) - signal
            def errorMessage(self):
                '''QString Nepomuk.Query.QueryServiceClient.errorMessage()'''
                return QString()
            def isListingFinished(self):
                '''bool Nepomuk.Query.QueryServiceClient.isListingFinished()'''
                return bool()
            def syncDesktopQuery(self, query, ok):
                '''static list-of-Nepomuk.Query.Result Nepomuk.Query.QueryServiceClient.syncDesktopQuery(QString query, bool ok)'''
                return [Nepomuk.Query.Result()]
            def syncSparqlQuery(self, query, requestPropertyMap = None, ok = None):
                '''static list-of-Nepomuk.Query.Result Nepomuk.Query.QueryServiceClient.syncSparqlQuery(QString query, dict-of-QString-Nepomuk.Types.Property requestPropertyMap = Nepomuk.Query.RequestPropertyMap(), bool ok)'''
                return [Nepomuk.Query.Result()]
            def syncQuery(self, query, ok):
                '''static list-of-Nepomuk.Query.Result Nepomuk.Query.QueryServiceClient.syncQuery(Nepomuk.Query.Query query, bool ok)'''
                return [Nepomuk.Query.Result()]
            finishedListing = pyqtSignal() # void finishedListing() - signal
            entriesRemoved = pyqtSignal() # void entriesRemoved(const QListlt;QUrlgt;amp;) - signal
            newEntries = pyqtSignal() # void newEntries(const QListlt;Nepomuk::Query::Resultgt;amp;) - signal
            def close(self):
                '''void Nepomuk.Query.QueryServiceClient.close()'''
            def blockingDesktopQuery(self, query):
                '''bool Nepomuk.Query.QueryServiceClient.blockingDesktopQuery(QString query)'''
                return bool()
            def blockingSparqlQuery(self, query, requestPropertyMap = None):
                '''bool Nepomuk.Query.QueryServiceClient.blockingSparqlQuery(QString query, dict-of-QString-Nepomuk.Types.Property requestPropertyMap = Nepomuk.Query.RequestPropertyMap())'''
                return bool()
            def blockingQuery(self, query):
                '''bool Nepomuk.Query.QueryServiceClient.blockingQuery(Nepomuk.Query.Query query)'''
                return bool()
            def desktopQuery(self, query):
                '''bool Nepomuk.Query.QueryServiceClient.desktopQuery(QString query)'''
                return bool()
            def sparqlQuery(self, query, requestPropertyMap = None):
                '''bool Nepomuk.Query.QueryServiceClient.sparqlQuery(QString query, dict-of-QString-Nepomuk.Types.Property requestPropertyMap = Nepomuk.Query.RequestPropertyMap())'''
                return bool()
            def query(self, query):
                '''bool Nepomuk.Query.QueryServiceClient.query(Nepomuk.Query.Query query)'''
                return bool()
            def serviceAvailable(self):
                '''static bool Nepomuk.Query.QueryServiceClient.serviceAvailable()'''
                return bool()
    class Vocabulary():
        """"""
        class NUAO():
            """"""
            def totalFocusDuration(self):
                '''static QUrl Nepomuk.Vocabulary.NUAO.totalFocusDuration()'''
                return QUrl()
            def targettedResource(self):
                '''static QUrl Nepomuk.Vocabulary.NUAO.targettedResource()'''
                return QUrl()
            def initiatingAgent(self):
                '''static QUrl Nepomuk.Vocabulary.NUAO.initiatingAgent()'''
                return QUrl()
            def end(self):
                '''static QUrl Nepomuk.Vocabulary.NUAO.end()'''
                return QUrl()
            def FocusEvent(self):
                '''static QUrl Nepomuk.Vocabulary.NUAO.FocusEvent()'''
                return QUrl()
            def metadata(self):
                '''static QUrl Nepomuk.Vocabulary.NUAO.metadata()'''
                return QUrl()
            def usageCount(self):
                '''static QUrl Nepomuk.Vocabulary.NUAO.usageCount()'''
                return QUrl()
            def totalUsageDuration(self):
                '''static QUrl Nepomuk.Vocabulary.NUAO.totalUsageDuration()'''
                return QUrl()
            def totalModificationDuration(self):
                '''static QUrl Nepomuk.Vocabulary.NUAO.totalModificationDuration()'''
                return QUrl()
            def totalEventDuration(self):
                '''static QUrl Nepomuk.Vocabulary.NUAO.totalEventDuration()'''
                return QUrl()
            def start(self):
                '''static QUrl Nepomuk.Vocabulary.NUAO.start()'''
                return QUrl()
            def modificationCount(self):
                '''static QUrl Nepomuk.Vocabulary.NUAO.modificationCount()'''
                return QUrl()
            def lastUsage(self):
                '''static QUrl Nepomuk.Vocabulary.NUAO.lastUsage()'''
                return QUrl()
            def lastModification(self):
                '''static QUrl Nepomuk.Vocabulary.NUAO.lastModification()'''
                return QUrl()
            def lastEvent(self):
                '''static QUrl Nepomuk.Vocabulary.NUAO.lastEvent()'''
                return QUrl()
            def involves(self):
                '''static QUrl Nepomuk.Vocabulary.NUAO.involves()'''
                return QUrl()
            def firstUsage(self):
                '''static QUrl Nepomuk.Vocabulary.NUAO.firstUsage()'''
                return QUrl()
            def firstModification(self):
                '''static QUrl Nepomuk.Vocabulary.NUAO.firstModification()'''
                return QUrl()
            def firstEvent(self):
                '''static QUrl Nepomuk.Vocabulary.NUAO.firstEvent()'''
                return QUrl()
            def eventCount(self):
                '''static QUrl Nepomuk.Vocabulary.NUAO.eventCount()'''
                return QUrl()
            def duration(self):
                '''static QUrl Nepomuk.Vocabulary.NUAO.duration()'''
                return QUrl()
            def UsageEvent(self):
                '''static QUrl Nepomuk.Vocabulary.NUAO.UsageEvent()'''
                return QUrl()
            def ModificationEvent(self):
                '''static QUrl Nepomuk.Vocabulary.NUAO.ModificationEvent()'''
                return QUrl()
            def Event(self):
                '''static QUrl Nepomuk.Vocabulary.NUAO.Event()'''
                return QUrl()
            def DesktopEvent(self):
                '''static QUrl Nepomuk.Vocabulary.NUAO.DesktopEvent()'''
                return QUrl()
            def nuaoNamespace(self):
                '''static QUrl Nepomuk.Vocabulary.NUAO.nuaoNamespace()'''
                return QUrl()
    class Query():
        """"""
        class NegationTerm(Nepomuk.Query.SimpleTerm):
            """"""
            def __init__(self):
                '''void Nepomuk.Query.NegationTerm.__init__()'''
            def __init__(self, term):
                '''void Nepomuk.Query.NegationTerm.__init__(Nepomuk.Query.NegationTerm term)'''
            def negateTerm(self, term):
                '''static Nepomuk.Query.Term Nepomuk.Query.NegationTerm.negateTerm(Nepomuk.Query.Term term)'''
                return Nepomuk.Query.Term()
    class File(Nepomuk.Resource):
        """"""
        def __init__(self, url = KUrl(), manager = None):
            '''void Nepomuk.File.__init__(KUrl url = KUrl(), Nepomuk.ResourceManager manager = None)'''
        def __init__(self, other):
            '''void Nepomuk.File.__init__(Nepomuk.Resource other)'''
        def __init__(self):
            '''Nepomuk.File Nepomuk.File.__init__()'''
            return Nepomuk.File()
        def dirResource(self):
            '''Nepomuk.File Nepomuk.File.dirResource()'''
            return Nepomuk.File()
        def url(self):
            '''KUrl Nepomuk.File.url()'''
            return KUrl()
    class Query():
        """"""
        class FileQuery(Nepomuk.Query.Query):
            """"""
            # Enum Nepomuk.Query.FileQuery.FileModeFlags
            QueryFiles = 0
            QueryFolders = 0
            QueryFilesAndFolders = 0
        
            def __init__(self):
                '''void Nepomuk.Query.FileQuery.__init__()'''
            def __init__(self, query):
                '''void Nepomuk.Query.FileQuery.__init__(Nepomuk.Query.Query query)'''
            def __init__(self, term):
                '''void Nepomuk.Query.FileQuery.__init__(Nepomuk.Query.Term term)'''
            def __init__(self):
                '''Nepomuk.Query.FileQuery Nepomuk.Query.FileQuery.__init__()'''
                return Nepomuk.Query.FileQuery()
            def allIncludeFolders(self):
                '''unknown-type Nepomuk.Query.FileQuery.allIncludeFolders()'''
                return unknown-type()
            def fileMode(self):
                '''Nepomuk.Query.FileQuery.FileMode Nepomuk.Query.FileQuery.fileMode()'''
                return Nepomuk.Query.FileQuery.FileMode()
            def setFileMode(self, mode):
                '''void Nepomuk.Query.FileQuery.setFileMode(Nepomuk.Query.FileQuery.FileMode mode)'''
            def excludeFolders(self):
                '''KUrl.List Nepomuk.Query.FileQuery.excludeFolders()'''
                return KUrl.List()
            def setExcludeFolders(self, folders):
                '''void Nepomuk.Query.FileQuery.setExcludeFolders(KUrl.List folders)'''
            def addExcludeFolder(self, folder):
                '''void Nepomuk.Query.FileQuery.addExcludeFolder(KUrl folder)'''
            def includeFolders(self):
                '''KUrl.List Nepomuk.Query.FileQuery.includeFolders()'''
                return KUrl.List()
            def setIncludeFolders(self, folders):
                '''void Nepomuk.Query.FileQuery.setIncludeFolders(KUrl.List folders)'''
            def setIncludeFolders(self, folders):
                '''void Nepomuk.Query.FileQuery.setIncludeFolders(unknown-type folders)'''
            def addIncludeFolder(self, folder):
                '''void Nepomuk.Query.FileQuery.addIncludeFolder(KUrl folder)'''
            def addIncludeFolder(self, folder, recursive):
                '''void Nepomuk.Query.FileQuery.addIncludeFolder(KUrl folder, bool recursive)'''
    class Query():
        """"""
        class QueryParser():
            """"""
            # Enum Nepomuk.Query.QueryParser.ParserFlag
            NoParserFlags = 0
            QueryTermGlobbing = 0
            DetectFilenamePattern = 0
        
            def __init__(self):
                '''void Nepomuk.Query.QueryParser.__init__()'''
            def parseQuery(self, query):
                '''static Nepomuk.Query.Query Nepomuk.Query.QueryParser.parseQuery(QString query)'''
                return Nepomuk.Query.Query()
            def parseQuery(self, query, flags):
                '''static Nepomuk.Query.Query Nepomuk.Query.QueryParser.parseQuery(QString query, Nepomuk.Query.QueryParser.ParserFlags flags)'''
                return Nepomuk.Query.Query()
            def matchProperty(self, fieldName):
                '''list-of-Nepomuk.Types.Property Nepomuk.Query.QueryParser.matchProperty(QString fieldName)'''
                return [Nepomuk.Types.Property()]
            def parse(self, query):
                '''Nepomuk.Query.Query Nepomuk.Query.QueryParser.parse(QString query)'''
                return Nepomuk.Query.Query()
            def parse(self, query, flags):
                '''Nepomuk.Query.Query Nepomuk.Query.QueryParser.parse(QString query, Nepomuk.Query.QueryParser.ParserFlags flags)'''
                return Nepomuk.Query.Query()
    class Vocabulary():
        """"""
        class NFO():
            """"""
            def paletteSize(self):
                '''static QUrl Nepomuk.Vocabulary.NFO.paletteSize()'''
                return QUrl()
            def colorCount(self):
                '''static QUrl Nepomuk.Vocabulary.NFO.colorCount()'''
                return QUrl()
            def WebDataObject(self):
                '''static QUrl Nepomuk.Vocabulary.NFO.WebDataObject()'''
                return QUrl()
            def wordCount(self):
                '''static QUrl Nepomuk.Vocabulary.NFO.wordCount()'''
                return QUrl()
            def width(self):
                '''static QUrl Nepomuk.Vocabulary.NFO.width()'''
                return QUrl()
            def verticalResolution(self):
                '''static QUrl Nepomuk.Vocabulary.NFO.verticalResolution()'''
                return QUrl()
            def uuid(self):
                '''static QUrl Nepomuk.Vocabulary.NFO.uuid()'''
                return QUrl()
            def uncompressedSize(self):
                '''static QUrl Nepomuk.Vocabulary.NFO.uncompressedSize()'''
                return QUrl()
            def totalSpace(self):
                '''static QUrl Nepomuk.Vocabulary.NFO.totalSpace()'''
                return QUrl()
            def supercedes(self):
                '''static QUrl Nepomuk.Vocabulary.NFO.supercedes()'''
                return QUrl()
            def streamPosition(self):
                '''static QUrl Nepomuk.Vocabulary.NFO.streamPosition()'''
                return QUrl()
            def sideChannels(self):
                '''static QUrl Nepomuk.Vocabulary.NFO.sideChannels()'''
                return QUrl()
            def sampleRate(self):
                '''static QUrl Nepomuk.Vocabulary.NFO.sampleRate()'''
                return QUrl()
            def sampleCount(self):
                '''static QUrl Nepomuk.Vocabulary.NFO.sampleCount()'''
                return QUrl()
            def rearChannels(self):
                '''static QUrl Nepomuk.Vocabulary.NFO.rearChannels()'''
                return QUrl()
            def rate(self):
                '''static QUrl Nepomuk.Vocabulary.NFO.rate()'''
                return QUrl()
            def programmingLanguage(self):
                '''static QUrl Nepomuk.Vocabulary.NFO.programmingLanguage()'''
                return QUrl()
            def permissions(self):
                '''static QUrl Nepomuk.Vocabulary.NFO.permissions()'''
                return QUrl()
            def pageNumber(self):
                '''static QUrl Nepomuk.Vocabulary.NFO.pageNumber()'''
                return QUrl()
            def pageCount(self):
                '''static QUrl Nepomuk.Vocabulary.NFO.pageCount()'''
                return QUrl()
            def originalLocation(self):
                '''static QUrl Nepomuk.Vocabulary.NFO.originalLocation()'''
                return QUrl()
            def occupiedSpace(self):
                '''static QUrl Nepomuk.Vocabulary.NFO.occupiedSpace()'''
                return QUrl()
            def lossyCompressionType(self):
                '''static QUrl Nepomuk.Vocabulary.NFO.lossyCompressionType()'''
                return QUrl()
            def losslessCompressionType(self):
                '''static QUrl Nepomuk.Vocabulary.NFO.losslessCompressionType()'''
                return QUrl()
            def lineCount(self):
                '''static QUrl Nepomuk.Vocabulary.NFO.lineCount()'''
                return QUrl()
            def lfeChannels(self):
                '''static QUrl Nepomuk.Vocabulary.NFO.lfeChannels()'''
                return QUrl()
            def isPasswordProtected(self):
                '''static QUrl Nepomuk.Vocabulary.NFO.isPasswordProtected()'''
                return QUrl()
            def interlaceMode(self):
                '''static QUrl Nepomuk.Vocabulary.NFO.interlaceMode()'''
                return QUrl()
            def horizontalResolution(self):
                '''static QUrl Nepomuk.Vocabulary.NFO.horizontalResolution()'''
                return QUrl()
            def height(self):
                '''static QUrl Nepomuk.Vocabulary.NFO.height()'''
                return QUrl()
            def hashValue(self):
                '''static QUrl Nepomuk.Vocabulary.NFO.hashValue()'''
                return QUrl()
            def hashAlgorithm(self):
                '''static QUrl Nepomuk.Vocabulary.NFO.hashAlgorithm()'''
                return QUrl()
            def hasMediaStream(self):
                '''static QUrl Nepomuk.Vocabulary.NFO.hasMediaStream()'''
                return QUrl()
            def hasMediaFileListEntry(self):
                '''static QUrl Nepomuk.Vocabulary.NFO.hasMediaFileListEntry()'''
                return QUrl()
            def hasHash(self):
                '''static QUrl Nepomuk.Vocabulary.NFO.hasHash()'''
                return QUrl()
            def frontChannels(self):
                '''static QUrl Nepomuk.Vocabulary.NFO.frontChannels()'''
                return QUrl()
            def freeSpace(self):
                '''static QUrl Nepomuk.Vocabulary.NFO.freeSpace()'''
                return QUrl()
            def frameRate(self):
                '''static QUrl Nepomuk.Vocabulary.NFO.frameRate()'''
                return QUrl()
            def frameCount(self):
                '''static QUrl Nepomuk.Vocabulary.NFO.frameCount()'''
                return QUrl()
            def foundry(self):
                '''static QUrl Nepomuk.Vocabulary.NFO.foundry()'''
                return QUrl()
            def fontFamily(self):
                '''static QUrl Nepomuk.Vocabulary.NFO.fontFamily()'''
                return QUrl()
            def filesystemType(self):
                '''static QUrl Nepomuk.Vocabulary.NFO.filesystemType()'''
                return QUrl()
            def fileUrl(self):
                '''static QUrl Nepomuk.Vocabulary.NFO.fileUrl()'''
                return QUrl()
            def fileSize(self):
                '''static QUrl Nepomuk.Vocabulary.NFO.fileSize()'''
                return QUrl()
            def fileOwner(self):
                '''static QUrl Nepomuk.Vocabulary.NFO.fileOwner()'''
                return QUrl()
            def fileName(self):
                '''static QUrl Nepomuk.Vocabulary.NFO.fileName()'''
                return QUrl()
            def fileLastModified(self):
                '''static QUrl Nepomuk.Vocabulary.NFO.fileLastModified()'''
                return QUrl()
            def fileLastAccessed(self):
                '''static QUrl Nepomuk.Vocabulary.NFO.fileLastAccessed()'''
                return QUrl()
            def fileCreated(self):
                '''static QUrl Nepomuk.Vocabulary.NFO.fileCreated()'''
                return QUrl()
            def encryptionStatus(self):
                '''static QUrl Nepomuk.Vocabulary.NFO.encryptionStatus()'''
                return QUrl()
            def encryptedStatus(self):
                '''static QUrl Nepomuk.Vocabulary.NFO.encryptedStatus()'''
                return QUrl()
            def encoding(self):
                '''static QUrl Nepomuk.Vocabulary.NFO.encoding()'''
                return QUrl()
            def duration(self):
                '''static QUrl Nepomuk.Vocabulary.NFO.duration()'''
                return QUrl()
            def deletionDate(self):
                '''static QUrl Nepomuk.Vocabulary.NFO.deletionDate()'''
                return QUrl()
            def definesGlobalVariable(self):
                '''static QUrl Nepomuk.Vocabulary.NFO.definesGlobalVariable()'''
                return QUrl()
            def definesFunction(self):
                '''static QUrl Nepomuk.Vocabulary.NFO.definesFunction()'''
                return QUrl()
            def definesClass(self):
                '''static QUrl Nepomuk.Vocabulary.NFO.definesClass()'''
                return QUrl()
            def decryptedStatus(self):
                '''static QUrl Nepomuk.Vocabulary.NFO.decryptedStatus()'''
                return QUrl()
            def count(self):
                '''static QUrl Nepomuk.Vocabulary.NFO.count()'''
                return QUrl()
            def containsBookmarkFolder(self):
                '''static QUrl Nepomuk.Vocabulary.NFO.containsBookmarkFolder()'''
                return QUrl()
            def containsBookmark(self):
                '''static QUrl Nepomuk.Vocabulary.NFO.containsBookmark()'''
                return QUrl()
            def conflicts(self):
                '''static QUrl Nepomuk.Vocabulary.NFO.conflicts()'''
                return QUrl()
            def compressionType(self):
                '''static QUrl Nepomuk.Vocabulary.NFO.compressionType()'''
                return QUrl()
            def commentCharacterCount(self):
                '''static QUrl Nepomuk.Vocabulary.NFO.commentCharacterCount()'''
                return QUrl()
            def colorDepth(self):
                '''static QUrl Nepomuk.Vocabulary.NFO.colorDepth()'''
                return QUrl()
            def codec(self):
                '''static QUrl Nepomuk.Vocabulary.NFO.codec()'''
                return QUrl()
            def characterPosition(self):
                '''static QUrl Nepomuk.Vocabulary.NFO.characterPosition()'''
                return QUrl()
            def characterCount(self):
                '''static QUrl Nepomuk.Vocabulary.NFO.characterCount()'''
                return QUrl()
            def channels(self):
                '''static QUrl Nepomuk.Vocabulary.NFO.channels()'''
                return QUrl()
            def bookmarks(self):
                '''static QUrl Nepomuk.Vocabulary.NFO.bookmarks()'''
                return QUrl()
            def bitsPerSample(self):
                '''static QUrl Nepomuk.Vocabulary.NFO.bitsPerSample()'''
                return QUrl()
            def bitrateType(self):
                '''static QUrl Nepomuk.Vocabulary.NFO.bitrateType()'''
                return QUrl()
            def bitDepth(self):
                '''static QUrl Nepomuk.Vocabulary.NFO.bitDepth()'''
                return QUrl()
            def belongsToContainer(self):
                '''static QUrl Nepomuk.Vocabulary.NFO.belongsToContainer()'''
                return QUrl()
            def averageBitrate(self):
                '''static QUrl Nepomuk.Vocabulary.NFO.averageBitrate()'''
                return QUrl()
            def aspectRatio(self):
                '''static QUrl Nepomuk.Vocabulary.NFO.aspectRatio()'''
                return QUrl()
            def Website(self):
                '''static QUrl Nepomuk.Vocabulary.NFO.Website()'''
                return QUrl()
            def Visual(self):
                '''static QUrl Nepomuk.Vocabulary.NFO.Visual()'''
                return QUrl()
            def Video(self):
                '''static QUrl Nepomuk.Vocabulary.NFO.Video()'''
                return QUrl()
            def VectorImage(self):
                '''static QUrl Nepomuk.Vocabulary.NFO.VectorImage()'''
                return QUrl()
            def Trash(self):
                '''static QUrl Nepomuk.Vocabulary.NFO.Trash()'''
                return QUrl()
            def TextDocument(self):
                '''static QUrl Nepomuk.Vocabulary.NFO.TextDocument()'''
                return QUrl()
            def Spreadsheet(self):
                '''static QUrl Nepomuk.Vocabulary.NFO.Spreadsheet()'''
                return QUrl()
            def SourceCode(self):
                '''static QUrl Nepomuk.Vocabulary.NFO.SourceCode()'''
                return QUrl()
            def SoftwareService(self):
                '''static QUrl Nepomuk.Vocabulary.NFO.SoftwareService()'''
                return QUrl()
            def SoftwareItem(self):
                '''static QUrl Nepomuk.Vocabulary.NFO.SoftwareItem()'''
                return QUrl()
            def Software(self):
                '''static QUrl Nepomuk.Vocabulary.NFO.Software()'''
                return QUrl()
            def RemotePortAddress(self):
                '''static QUrl Nepomuk.Vocabulary.NFO.RemotePortAddress()'''
                return QUrl()
            def RemoteDataObject(self):
                '''static QUrl Nepomuk.Vocabulary.NFO.RemoteDataObject()'''
                return QUrl()
            def RasterImage(self):
                '''static QUrl Nepomuk.Vocabulary.NFO.RasterImage()'''
                return QUrl()
            def Presentation(self):
                '''static QUrl Nepomuk.Vocabulary.NFO.Presentation()'''
                return QUrl()
            def PlainTextDocument(self):
                '''static QUrl Nepomuk.Vocabulary.NFO.PlainTextDocument()'''
                return QUrl()
            def PaginatedTextDocument(self):
                '''static QUrl Nepomuk.Vocabulary.NFO.PaginatedTextDocument()'''
                return QUrl()
            def OperatingSystem(self):
                '''static QUrl Nepomuk.Vocabulary.NFO.OperatingSystem()'''
                return QUrl()
            def MindMap(self):
                '''static QUrl Nepomuk.Vocabulary.NFO.MindMap()'''
                return QUrl()
            def MediaStream(self):
                '''static QUrl Nepomuk.Vocabulary.NFO.MediaStream()'''
                return QUrl()
            def MediaList(self):
                '''static QUrl Nepomuk.Vocabulary.NFO.MediaList()'''
                return QUrl()
            def MediaFileListEntry(self):
                '''static QUrl Nepomuk.Vocabulary.NFO.MediaFileListEntry()'''
                return QUrl()
            def Media(self):
                '''static QUrl Nepomuk.Vocabulary.NFO.Media()'''
                return QUrl()
            def Image(self):
                '''static QUrl Nepomuk.Vocabulary.NFO.Image()'''
                return QUrl()
            def Icon(self):
                '''static QUrl Nepomuk.Vocabulary.NFO.Icon()'''
                return QUrl()
            def HtmlDocument(self):
                '''static QUrl Nepomuk.Vocabulary.NFO.HtmlDocument()'''
                return QUrl()
            def HardDiskPartition(self):
                '''static QUrl Nepomuk.Vocabulary.NFO.HardDiskPartition()'''
                return QUrl()
            def Font(self):
                '''static QUrl Nepomuk.Vocabulary.NFO.Font()'''
                return QUrl()
            def Folder(self):
                '''static QUrl Nepomuk.Vocabulary.NFO.Folder()'''
                return QUrl()
            def FilesystemImage(self):
                '''static QUrl Nepomuk.Vocabulary.NFO.FilesystemImage()'''
                return QUrl()
            def Filesystem(self):
                '''static QUrl Nepomuk.Vocabulary.NFO.Filesystem()'''
                return QUrl()
            def FileHash(self):
                '''static QUrl Nepomuk.Vocabulary.NFO.FileHash()'''
                return QUrl()
            def FileDataObject(self):
                '''static QUrl Nepomuk.Vocabulary.NFO.FileDataObject()'''
                return QUrl()
            def Executable(self):
                '''static QUrl Nepomuk.Vocabulary.NFO.Executable()'''
                return QUrl()
            def EncryptionStatus(self):
                '''static QUrl Nepomuk.Vocabulary.NFO.EncryptionStatus()'''
                return QUrl()
            def EmbeddedFileDataObject(self):
                '''static QUrl Nepomuk.Vocabulary.NFO.EmbeddedFileDataObject()'''
                return QUrl()
            def Document(self):
                '''static QUrl Nepomuk.Vocabulary.NFO.Document()'''
                return QUrl()
            def DeletedResource(self):
                '''static QUrl Nepomuk.Vocabulary.NFO.DeletedResource()'''
                return QUrl()
            def DataContainer(self):
                '''static QUrl Nepomuk.Vocabulary.NFO.DataContainer()'''
                return QUrl()
            def Cursor(self):
                '''static QUrl Nepomuk.Vocabulary.NFO.Cursor()'''
                return QUrl()
            def CompressionType(self):
                '''static QUrl Nepomuk.Vocabulary.NFO.CompressionType()'''
                return QUrl()
            def BookmarkFolder(self):
                '''static QUrl Nepomuk.Vocabulary.NFO.BookmarkFolder()'''
                return QUrl()
            def Bookmark(self):
                '''static QUrl Nepomuk.Vocabulary.NFO.Bookmark()'''
                return QUrl()
            def Audio(self):
                '''static QUrl Nepomuk.Vocabulary.NFO.Audio()'''
                return QUrl()
            def Attachment(self):
                '''static QUrl Nepomuk.Vocabulary.NFO.Attachment()'''
                return QUrl()
            def ArchiveItem(self):
                '''static QUrl Nepomuk.Vocabulary.NFO.ArchiveItem()'''
                return QUrl()
            def Archive(self):
                '''static QUrl Nepomuk.Vocabulary.NFO.Archive()'''
                return QUrl()
            def Application(self):
                '''static QUrl Nepomuk.Vocabulary.NFO.Application()'''
                return QUrl()
            def nrlOntologyGraph(self):
                '''static QUrl Nepomuk.Vocabulary.NFO.nrlOntologyGraph()'''
                return QUrl()
            def nfoNamespace(self):
                '''static QUrl Nepomuk.Vocabulary.NFO.nfoNamespace()'''
                return QUrl()
    class Query():
        """"""
        class OrTerm(Nepomuk.Query.GroupTerm):
            """"""
            def __init__(self):
                '''void Nepomuk.Query.OrTerm.__init__()'''
            def __init__(self, term):
                '''void Nepomuk.Query.OrTerm.__init__(Nepomuk.Query.OrTerm term)'''
            def __init__(self, term1, term2, term3 = None, term4 = None, term5 = None, term6 = None):
                '''void Nepomuk.Query.OrTerm.__init__(Nepomuk.Query.Term term1, Nepomuk.Query.Term term2, Nepomuk.Query.Term term3 = Nepomuk.Query.Term(), Nepomuk.Query.Term term4 = Nepomuk.Query.Term(), Nepomuk.Query.Term term5 = Nepomuk.Query.Term(), Nepomuk.Query.Term term6 = Nepomuk.Query.Term())'''
            def __init__(self, terms):
                '''void Nepomuk.Query.OrTerm.__init__(list-of-Nepomuk.Query.Term terms)'''
    class Query():
        """"""
        class Query():
            """"""
            class RequestProperty():
                """"""
                def __init__(self, property, optional = True):
                    '''void Nepomuk.Query.Query.RequestProperty.__init__(Nepomuk.Types.Property property, bool optional = True)'''
                def __init__(self):
                    '''Nepomuk.Query.Query.RequestProperty Nepomuk.Query.Query.RequestProperty.__init__()'''
                    return Nepomuk.Query.Query.RequestProperty()
                def __ne__(self, other):
                    '''bool Nepomuk.Query.Query.RequestProperty.__ne__(Nepomuk.Query.Query.RequestProperty other)'''
                    return bool()
                def optional(self):
                    '''bool Nepomuk.Query.Query.RequestProperty.optional()'''
                    return bool()
                def property(self):
                    '''Nepomuk.Types.Property Nepomuk.Query.Query.RequestProperty.property()'''
                    return Nepomuk.Types.Property()
                def __eq__(self, other):
                    '''bool Nepomuk.Query.Query.RequestProperty.__eq__(Nepomuk.Query.Query.RequestProperty other)'''
                    return bool()
    class TagCloud(KTagCloudWidget):
        """"""
        def __init__(self, parent = None):
            '''void Nepomuk.TagCloud.__init__(QWidget parent = None)'''
        tagClicked = pyqtSignal() # void tagClicked(Nepomuk::Tag) - signal
        def setAutoUpdate(self, enable):
            '''void Nepomuk.TagCloud.setAutoUpdate(bool enable)'''
        def updateTags(self):
            '''void Nepomuk.TagCloud.updateTags()'''
        def autoUpdate(self):
            '''bool Nepomuk.TagCloud.autoUpdate()'''
            return bool()
    class Query():
        """"""
        class Term():
            """"""
            # Enum Nepomuk.Query.Term.Type
            Invalid = 0
            Literal = 0
            Resource = 0
            And = 0
            Or = 0
            Comparison = 0
            ResourceType = 0
            Negation = 0
            Optional = 0
        
            def __init__(self):
                '''void Nepomuk.Query.Term.__init__()'''
            def __init__(self, other):
                '''void Nepomuk.Query.Term.__init__(Nepomuk.Query.Term other)'''
            def __ne__(self, term):
                '''bool Nepomuk.Query.Term.__ne__(Nepomuk.Query.Term term)'''
                return bool()
            def fromProperty(self, property, variant):
                '''static Nepomuk.Query.Term Nepomuk.Query.Term.fromProperty(Nepomuk.Types.Property property, Nepomuk.Variant variant)'''
                return Nepomuk.Query.Term()
            def fromVariant(self, variant):
                '''static Nepomuk.Query.Term Nepomuk.Query.Term.fromVariant(Nepomuk.Variant variant)'''
                return Nepomuk.Query.Term()
            def optimized(self):
                '''Nepomuk.Query.Term Nepomuk.Query.Term.optimized()'''
                return Nepomuk.Query.Term()
            def fromString(self, s):
                '''static Nepomuk.Query.Term Nepomuk.Query.Term.fromString(QString s)'''
                return Nepomuk.Query.Term()
            def toString(self):
                '''QString Nepomuk.Query.Term.toString()'''
                return QString()
            def toOptionalTerm(self):
                '''Nepomuk.Query.OptionalTerm Nepomuk.Query.Term.toOptionalTerm()'''
                return Nepomuk.Query.OptionalTerm()
            def isOptionalTerm(self):
                '''bool Nepomuk.Query.Term.isOptionalTerm()'''
                return bool()
            def __eq__(self, term):
                '''bool Nepomuk.Query.Term.__eq__(Nepomuk.Query.Term term)'''
                return bool()
            def toResourceTypeTerm(self):
                '''Nepomuk.Query.ResourceTypeTerm Nepomuk.Query.Term.toResourceTypeTerm()'''
                return Nepomuk.Query.ResourceTypeTerm()
            def toComparisonTerm(self):
                '''Nepomuk.Query.ComparisonTerm Nepomuk.Query.Term.toComparisonTerm()'''
                return Nepomuk.Query.ComparisonTerm()
            def toOrTerm(self):
                '''Nepomuk.Query.OrTerm Nepomuk.Query.Term.toOrTerm()'''
                return Nepomuk.Query.OrTerm()
            def toAndTerm(self):
                '''Nepomuk.Query.AndTerm Nepomuk.Query.Term.toAndTerm()'''
                return Nepomuk.Query.AndTerm()
            def toNegationTerm(self):
                '''Nepomuk.Query.NegationTerm Nepomuk.Query.Term.toNegationTerm()'''
                return Nepomuk.Query.NegationTerm()
            def toResourceTerm(self):
                '''Nepomuk.Query.ResourceTerm Nepomuk.Query.Term.toResourceTerm()'''
                return Nepomuk.Query.ResourceTerm()
            def toLiteralTerm(self):
                '''Nepomuk.Query.LiteralTerm Nepomuk.Query.Term.toLiteralTerm()'''
                return Nepomuk.Query.LiteralTerm()
            def isResourceTypeTerm(self):
                '''bool Nepomuk.Query.Term.isResourceTypeTerm()'''
                return bool()
            def isComparisonTerm(self):
                '''bool Nepomuk.Query.Term.isComparisonTerm()'''
                return bool()
            def isOrTerm(self):
                '''bool Nepomuk.Query.Term.isOrTerm()'''
                return bool()
            def isAndTerm(self):
                '''bool Nepomuk.Query.Term.isAndTerm()'''
                return bool()
            def isNegationTerm(self):
                '''bool Nepomuk.Query.Term.isNegationTerm()'''
                return bool()
            def isResourceTerm(self):
                '''bool Nepomuk.Query.Term.isResourceTerm()'''
                return bool()
            def isLiteralTerm(self):
                '''bool Nepomuk.Query.Term.isLiteralTerm()'''
                return bool()
            def type(self):
                '''Nepomuk.Query.Term.Type Nepomuk.Query.Term.type()'''
                return Nepomuk.Query.Term.Type()
            def isValid(self):
                '''bool Nepomuk.Query.Term.isValid()'''
                return bool()
    class Vocabulary():
        """"""
        class NMM():
            """"""
            def setSize(self):
                '''static QUrl Nepomuk.Vocabulary.NMM.setSize()'''
                return QUrl()
            def setNumber(self):
                '''static QUrl Nepomuk.Vocabulary.NMM.setNumber()'''
                return QUrl()
            def albumTrackCount(self):
                '''static QUrl Nepomuk.Vocabulary.NMM.albumTrackCount()'''
                return QUrl()
            def metadata(self):
                '''static QUrl Nepomuk.Vocabulary.NMM.metadata()'''
                return QUrl()
            def writer(self):
                '''static QUrl Nepomuk.Vocabulary.NMM.writer()'''
                return QUrl()
            def trackPeakGain(self):
                '''static QUrl Nepomuk.Vocabulary.NMM.trackPeakGain()'''
                return QUrl()
            def trackNumber(self):
                '''static QUrl Nepomuk.Vocabulary.NMM.trackNumber()'''
                return QUrl()
            def trackGain(self):
                '''static QUrl Nepomuk.Vocabulary.NMM.trackGain()'''
                return QUrl()
            def synopsis(self):
                '''static QUrl Nepomuk.Vocabulary.NMM.synopsis()'''
                return QUrl()
            def series(self):
                '''static QUrl Nepomuk.Vocabulary.NMM.series()'''
                return QUrl()
            def season(self):
                '''static QUrl Nepomuk.Vocabulary.NMM.season()'''
                return QUrl()
            def releaseDate(self):
                '''static QUrl Nepomuk.Vocabulary.NMM.releaseDate()'''
                return QUrl()
            def producer(self):
                '''static QUrl Nepomuk.Vocabulary.NMM.producer()'''
                return QUrl()
            def performer(self):
                '''static QUrl Nepomuk.Vocabulary.NMM.performer()'''
                return QUrl()
            def musicCDIdentifier(self):
                '''static QUrl Nepomuk.Vocabulary.NMM.musicCDIdentifier()'''
                return QUrl()
            def musicBrainzTrackID(self):
                '''static QUrl Nepomuk.Vocabulary.NMM.musicBrainzTrackID()'''
                return QUrl()
            def musicBrainzAlbumID(self):
                '''static QUrl Nepomuk.Vocabulary.NMM.musicBrainzAlbumID()'''
                return QUrl()
            def musicAlbum(self):
                '''static QUrl Nepomuk.Vocabulary.NMM.musicAlbum()'''
                return QUrl()
            def lyricist(self):
                '''static QUrl Nepomuk.Vocabulary.NMM.lyricist()'''
                return QUrl()
            def internationalStandardRecordingCode(self):
                '''static QUrl Nepomuk.Vocabulary.NMM.internationalStandardRecordingCode()'''
                return QUrl()
            def hasEpisode(self):
                '''static QUrl Nepomuk.Vocabulary.NMM.hasEpisode()'''
                return QUrl()
            def genre(self):
                '''static QUrl Nepomuk.Vocabulary.NMM.genre()'''
                return QUrl()
            def episodeNumber(self):
                '''static QUrl Nepomuk.Vocabulary.NMM.episodeNumber()'''
                return QUrl()
            def director(self):
                '''static QUrl Nepomuk.Vocabulary.NMM.director()'''
                return QUrl()
            def composer(self):
                '''static QUrl Nepomuk.Vocabulary.NMM.composer()'''
                return QUrl()
            def cinematographer(self):
                '''static QUrl Nepomuk.Vocabulary.NMM.cinematographer()'''
                return QUrl()
            def beatsPerMinute(self):
                '''static QUrl Nepomuk.Vocabulary.NMM.beatsPerMinute()'''
                return QUrl()
            def audienceRating(self):
                '''static QUrl Nepomuk.Vocabulary.NMM.audienceRating()'''
                return QUrl()
            def assistantDirector(self):
                '''static QUrl Nepomuk.Vocabulary.NMM.assistantDirector()'''
                return QUrl()
            def artwork(self):
                '''static QUrl Nepomuk.Vocabulary.NMM.artwork()'''
                return QUrl()
            def albumPeakGain(self):
                '''static QUrl Nepomuk.Vocabulary.NMM.albumPeakGain()'''
                return QUrl()
            def albumGain(self):
                '''static QUrl Nepomuk.Vocabulary.NMM.albumGain()'''
                return QUrl()
            def actor(self):
                '''static QUrl Nepomuk.Vocabulary.NMM.actor()'''
                return QUrl()
            def TVShow(self):
                '''static QUrl Nepomuk.Vocabulary.NMM.TVShow()'''
                return QUrl()
            def TVSeries(self):
                '''static QUrl Nepomuk.Vocabulary.NMM.TVSeries()'''
                return QUrl()
            def MusicPiece(self):
                '''static QUrl Nepomuk.Vocabulary.NMM.MusicPiece()'''
                return QUrl()
            def MusicAlbum(self):
                '''static QUrl Nepomuk.Vocabulary.NMM.MusicAlbum()'''
                return QUrl()
            def Movie(self):
                '''static QUrl Nepomuk.Vocabulary.NMM.Movie()'''
                return QUrl()
            def nrlOntologyGraph(self):
                '''static QUrl Nepomuk.Vocabulary.NMM.nrlOntologyGraph()'''
                return QUrl()
            def nmmNamespace(self):
                '''static QUrl Nepomuk.Vocabulary.NMM.nmmNamespace()'''
                return QUrl()
    class Types():
        """"""
        class Ontology(Nepomuk.Types.Entity):
            """"""
            def __init__(self):
                '''void Nepomuk.Types.Ontology.__init__()'''
            def __init__(self, uri):
                '''void Nepomuk.Types.Ontology.__init__(QUrl uri)'''
            def __init__(self):
                '''Nepomuk.Types.Ontology Nepomuk.Types.Ontology.__init__()'''
                return Nepomuk.Types.Ontology()
            def findPropertyByLabel(self, label, language = QString()):
                '''Nepomuk.Types.Property Nepomuk.Types.Ontology.findPropertyByLabel(QString label, QString language = QString())'''
                return Nepomuk.Types.Property()
            def findPropertyByName(self, name):
                '''Nepomuk.Types.Property Nepomuk.Types.Ontology.findPropertyByName(QString name)'''
                return Nepomuk.Types.Property()
            def allProperties(self):
                '''list-of-Nepomuk.Types.Property Nepomuk.Types.Ontology.allProperties()'''
                return [Nepomuk.Types.Property()]
            def findClassByLabel(self, label, language = QString()):
                '''Nepomuk.Types.Class Nepomuk.Types.Ontology.findClassByLabel(QString label, QString language = QString())'''
                return Nepomuk.Types.Class()
            def findClassByName(self, name):
                '''Nepomuk.Types.Class Nepomuk.Types.Ontology.findClassByName(QString name)'''
                return Nepomuk.Types.Class()
            def allClasses(self):
                '''list-of-Nepomuk.Types.Class Nepomuk.Types.Ontology.allClasses()'''
                return [Nepomuk.Types.Class()]
    class ResourceManager(QObject):
        """"""
        def clearCache(self):
            '''void Nepomuk.ResourceManager.clearCache()'''
        nepomukSystemStopped = pyqtSignal() # void nepomukSystemStopped() - signal
        nepomukSystemStarted = pyqtSignal() # void nepomukSystemStarted() - signal
        def createManagerForModel(self, model):
            '''static Nepomuk.ResourceManager Nepomuk.ResourceManager.createManagerForModel(Soprano.Model model)'''
            return Nepomuk.ResourceManager()
        def setOverrideMainModel(self, model):
            '''void Nepomuk.ResourceManager.setOverrideMainModel(Soprano.Model model)'''
        def mainModel(self):
            '''Soprano.Model Nepomuk.ResourceManager.mainModel()'''
            return Soprano.Model()
        error = pyqtSignal() # void error(const QStringamp;,int) - signal
        resourceModified = pyqtSignal() # void resourceModified(const QStringamp;) - signal
        def notifyError(self, uri, errorCode):
            '''void Nepomuk.ResourceManager.notifyError(QString uri, int errorCode)'''
        def generateUniqueUri(self):
            '''QString Nepomuk.ResourceManager.generateUniqueUri()'''
            return QString()
        def generateUniqueUri(self, label):
            '''QUrl Nepomuk.ResourceManager.generateUniqueUri(QString label)'''
            return QUrl()
        def allResourcesWithProperty(self, uri, v):
            '''list-of-Nepomuk.Resource Nepomuk.ResourceManager.allResourcesWithProperty(QUrl uri, Nepomuk.Variant v)'''
            return [Nepomuk.Resource()]
        def allResourcesWithProperty(self, uri, v):
            '''list-of-Nepomuk.Resource Nepomuk.ResourceManager.allResourcesWithProperty(QString uri, Nepomuk.Variant v)'''
            return [Nepomuk.Resource()]
        def allResourcesOfType(self, type):
            '''list-of-Nepomuk.Resource Nepomuk.ResourceManager.allResourcesOfType(QUrl type)'''
            return [Nepomuk.Resource()]
        def allResourcesOfType(self, type):
            '''list-of-Nepomuk.Resource Nepomuk.ResourceManager.allResourcesOfType(QString type)'''
            return [Nepomuk.Resource()]
        def removeResource(self, uri):
            '''void Nepomuk.ResourceManager.removeResource(QString uri)'''
        def createResourceFromUri(self, uri):
            '''Nepomuk.Resource Nepomuk.ResourceManager.createResourceFromUri(QString uri)'''
            return Nepomuk.Resource()
        def initialized(self):
            '''bool Nepomuk.ResourceManager.initialized()'''
            return bool()
        def init(self):
            '''int Nepomuk.ResourceManager.init()'''
            return int()
        def deleteInstance(self):
            '''void Nepomuk.ResourceManager.deleteInstance()'''
        def instance(self):
            '''static Nepomuk.ResourceManager Nepomuk.ResourceManager.instance()'''
            return Nepomuk.ResourceManager()
    class Query():
        """"""
        # Enum Nepomuk.Query.DateRangeFlag
        ModificationDate = 0
        ContentDate = 0
        UsageDate = 0
        AllDates = 0
    
        # Enum Nepomuk.Query.StandardQuery
        LastModifiedFilesQuery = 0
        MostImportantResourcesQuery = 0
        NeverOpenedFilesQuery = 0
        ResourcesForActivityQuery = 0
    
        def dateRangeQuery(self, start, end, dateFlags = None):
            '''static Nepomuk.Query.Query Nepomuk.Query.dateRangeQuery(QDate start, QDate end, Nepomuk.Query.DateRangeFlags dateFlags = Nepomuk.Query.AllDates)'''
            return Nepomuk.Query.Query()
        def standardQuery(self, query, subterm = None):
            '''static Nepomuk.Query.Query Nepomuk.Query.standardQuery(Nepomuk.Query.StandardQuery query, Nepomuk.Query.Term subterm = Nepomuk.Query.Term())'''
            return Nepomuk.Query.Query()
        def qHash(self):
            '''static Nepomuk.Query.Query Nepomuk.Query.qHash()'''
            return Nepomuk.Query.Query()
        def qHash(self):
            '''static Nepomuk.Query.Term Nepomuk.Query.qHash()'''
            return Nepomuk.Query.Term()
    class Query():
        """"""
        class Query():
            """"""
            # Enum Nepomuk.Query.Query.QueryFlag
            NoQueryFlags = 0
            NoResultRestrictions = 0
            WithoutFullTextExcerpt = 0
        
            # Enum Nepomuk.Query.Query.SparqlFlag
            NoFlags = 0
            CreateCountQuery = 0
            HandleInverseProperties = 0
            CreateAskQuery = 0
        
            def __init__(self):
                '''void Nepomuk.Query.Query.__init__()'''
            def __init__(self, term):
                '''void Nepomuk.Query.Query.__init__(Nepomuk.Query.Term term)'''
            def __init__(self):
                '''Nepomuk.Query.Query Nepomuk.Query.Query.__init__()'''
                return Nepomuk.Query.Query()
            def optimized(self):
                '''Nepomuk.Query.Query Nepomuk.Query.Query.optimized()'''
                return Nepomuk.Query.Query()
            def __ne__(self, query):
                '''bool Nepomuk.Query.Query.__ne__(Nepomuk.Query.Query query)'''
                return bool()
            def queryFlags(self):
                '''Nepomuk.Query.Query.QueryFlags Nepomuk.Query.Query.queryFlags()'''
                return Nepomuk.Query.Query.QueryFlags()
            def setQueryFlags(self, flags):
                '''void Nepomuk.Query.Query.setQueryFlags(Nepomuk.Query.Query.QueryFlags flags)'''
            def fullTextScoringSortOrder(self):
                '''Qt.SortOrder Nepomuk.Query.Query.fullTextScoringSortOrder()'''
                return Qt.SortOrder()
            def fullTextScoringEnabled(self):
                '''bool Nepomuk.Query.Query.fullTextScoringEnabled()'''
                return bool()
            def setFullTextScoringSortOrder(self, order):
                '''void Nepomuk.Query.Query.setFullTextScoringSortOrder(Qt.SortOrder order)'''
            def setFullTextScoringEnabled(self, enabled):
                '''void Nepomuk.Query.Query.setFullTextScoringEnabled(bool enabled)'''
            def toFileQuery(self):
                '''Nepomuk.Query.FileQuery Nepomuk.Query.Query.toFileQuery()'''
                return Nepomuk.Query.FileQuery()
            def titleFromQueryUrl(self, url):
                '''static QString Nepomuk.Query.Query.titleFromQueryUrl(KUrl url)'''
                return QString()
            def sparqlFromQueryUrl(self, url):
                '''static QString Nepomuk.Query.Query.sparqlFromQueryUrl(KUrl url)'''
                return QString()
            def fromQueryUrl(self, url):
                '''static Nepomuk.Query.Query Nepomuk.Query.Query.fromQueryUrl(KUrl url)'''
                return Nepomuk.Query.Query()
            def fromString(self, queryString):
                '''static Nepomuk.Query.Query Nepomuk.Query.Query.fromString(QString queryString)'''
                return Nepomuk.Query.Query()
            def toString(self):
                '''QString Nepomuk.Query.Query.toString()'''
                return QString()
            def isFileQuery(self):
                '''bool Nepomuk.Query.Query.isFileQuery()'''
                return bool()
            def setOffset(self, offset):
                '''void Nepomuk.Query.Query.setOffset(int offset)'''
            def offset(self):
                '''int Nepomuk.Query.Query.offset()'''
                return int()
            def __eq__(self, query):
                '''bool Nepomuk.Query.Query.__eq__(Nepomuk.Query.Query query)'''
                return bool()
            def requestPropertyMap(self):
                '''dict-of-QString-Nepomuk.Types.Property Nepomuk.Query.Query.requestPropertyMap()'''
                return dict-of-QString-Nepomuk.Types.Property()
            def toSearchUrl(self, flags = None):
                '''KUrl Nepomuk.Query.Query.toSearchUrl(Nepomuk.Query.Query.SparqlFlags flags = Nepomuk.Query.Query.NoFlags)'''
                return KUrl()
            def toSearchUrl(self, customTitle, flags = None):
                '''KUrl Nepomuk.Query.Query.toSearchUrl(QString customTitle, Nepomuk.Query.Query.SparqlFlags flags = Nepomuk.Query.Query.NoFlags)'''
                return KUrl()
            def toSparqlQuery(self, flags = None):
                '''QString Nepomuk.Query.Query.toSparqlQuery(Nepomuk.Query.Query.SparqlFlags flags = Nepomuk.Query.Query.NoFlags)'''
                return QString()
            def requestProperties(self):
                '''list-of-Nepomuk.Query.Query.RequestProperty Nepomuk.Query.Query.requestProperties()'''
                return [Nepomuk.Query.Query.RequestProperty()]
            def setRequestProperties(self, properties):
                '''void Nepomuk.Query.Query.setRequestProperties(list-of-Nepomuk.Query.Query.RequestProperty properties)'''
            def addRequestProperty(self, property):
                '''void Nepomuk.Query.Query.addRequestProperty(Nepomuk.Query.Query.RequestProperty property)'''
            def setLimit(self):
                '''int Nepomuk.Query.Query.setLimit()'''
                return int()
            def setTerm(self):
                '''Nepomuk.Query.Term Nepomuk.Query.Query.setTerm()'''
                return Nepomuk.Query.Term()
            def limit(self):
                '''int Nepomuk.Query.Query.limit()'''
                return int()
            def term(self):
                '''Nepomuk.Query.Term Nepomuk.Query.Query.term()'''
                return Nepomuk.Query.Term()
            def isValid(self):
                '''bool Nepomuk.Query.Query.isValid()'''
                return bool()
    class Types():
        """"""
        class Property(Nepomuk.Types.Entity):
            """"""
            def __init__(self):
                '''void Nepomuk.Types.Property.__init__()'''
            def __init__(self, uri):
                '''void Nepomuk.Types.Property.__init__(QUrl uri)'''
            def __init__(self):
                '''Nepomuk.Types.Property Nepomuk.Types.Property.__init__()'''
                return Nepomuk.Types.Property()
            def __lt__(self, term):
                '''Nepomuk.Query.ComparisonTerm Nepomuk.Types.Property.__lt__(Nepomuk.Query.Term term)'''
                return Nepomuk.Query.ComparisonTerm()
            def __gt__(self, term):
                '''Nepomuk.Query.ComparisonTerm Nepomuk.Types.Property.__gt__(Nepomuk.Query.Term term)'''
                return Nepomuk.Query.ComparisonTerm()
            def __le__(self, term):
                '''Nepomuk.Query.ComparisonTerm Nepomuk.Types.Property.__le__(Nepomuk.Query.Term term)'''
                return Nepomuk.Query.ComparisonTerm()
            def __ge__(self, term):
                '''Nepomuk.Query.ComparisonTerm Nepomuk.Types.Property.__ge__(Nepomuk.Query.Term term)'''
                return Nepomuk.Query.ComparisonTerm()
            def __eq__(self, term):
                '''Nepomuk.Query.ComparisonTerm Nepomuk.Types.Property.__eq__(Nepomuk.Query.Term term)'''
                return Nepomuk.Query.ComparisonTerm()
            def __ne__(self, term):
                '''Nepomuk.Query.Term Nepomuk.Types.Property.__ne__(Nepomuk.Query.Term term)'''
                return Nepomuk.Query.Term()
            def isSubPropertyOf(self, other):
                '''bool Nepomuk.Types.Property.isSubPropertyOf(Nepomuk.Types.Property other)'''
                return bool()
            def isParentOf(self, other):
                '''bool Nepomuk.Types.Property.isParentOf(Nepomuk.Types.Property other)'''
                return bool()
            def maxCardinality(self):
                '''int Nepomuk.Types.Property.maxCardinality()'''
                return int()
            def minCardinality(self):
                '''int Nepomuk.Types.Property.minCardinality()'''
                return int()
            def cardinality(self):
                '''int Nepomuk.Types.Property.cardinality()'''
                return int()
            def domain(self):
                '''Nepomuk.Types.Class Nepomuk.Types.Property.domain()'''
                return Nepomuk.Types.Class()
            def literalRangeType(self):
                '''Nepomuk.Types.Literal Nepomuk.Types.Property.literalRangeType()'''
                return Nepomuk.Types.Literal()
            def range(self):
                '''Nepomuk.Types.Class Nepomuk.Types.Property.range()'''
                return Nepomuk.Types.Class()
            def inverseProperty(self):
                '''Nepomuk.Types.Property Nepomuk.Types.Property.inverseProperty()'''
                return Nepomuk.Types.Property()
            def subProperties(self):
                '''list-of-Nepomuk.Types.Property Nepomuk.Types.Property.subProperties()'''
                return [Nepomuk.Types.Property()]
            def parentProperties(self):
                '''list-of-Nepomuk.Types.Property Nepomuk.Types.Property.parentProperties()'''
                return [Nepomuk.Types.Property()]
    class Query():
        """"""
        class ResourceTerm(Nepomuk.Query.Term):
            """"""
            def __init__(self, term):
                '''void Nepomuk.Query.ResourceTerm.__init__(Nepomuk.Query.ResourceTerm term)'''
            def __init__(self, resource = None):
                '''void Nepomuk.Query.ResourceTerm.__init__(Nepomuk.Resource resource = Nepomuk.Resource())'''
            def setResource(self, resource):
                '''void Nepomuk.Query.ResourceTerm.setResource(Nepomuk.Resource resource)'''
            def resource(self):
                '''Nepomuk.Resource Nepomuk.Query.ResourceTerm.resource()'''
                return Nepomuk.Resource()
    class Tag(Nepomuk.Resource):
        """"""
        def __init__(self):
            '''void Nepomuk.Tag.__init__()'''
        def __init__(self, manager):
            '''void Nepomuk.Tag.__init__(Nepomuk.ResourceManager manager)'''
        def __init__(self):
            '''Nepomuk.Tag Nepomuk.Tag.__init__()'''
            return Nepomuk.Tag()
        def __init__(self):
            '''Nepomuk.Resource Nepomuk.Tag.__init__()'''
            return Nepomuk.Resource()
        def __init__(self, uriOrIdentifier):
            '''void Nepomuk.Tag.__init__(QString uriOrIdentifier)'''
        def __init__(self, uriOrIdentifier, manager):
            '''void Nepomuk.Tag.__init__(QString uriOrIdentifier, Nepomuk.ResourceManager manager)'''
        def __init__(self, uri):
            '''void Nepomuk.Tag.__init__(QUrl uri)'''
        def __init__(self, uri, manager):
            '''void Nepomuk.Tag.__init__(QUrl uri, Nepomuk.ResourceManager manager)'''
        def __init__(self, uri, type):
            '''void Nepomuk.Tag.__init__(QString uri, QUrl type)'''
        def __init__(self, uri, type):
            '''void Nepomuk.Tag.__init__(QUrl uri, QUrl type)'''
        def __init__(self, uri, type, manager):
            '''void Nepomuk.Tag.__init__(QString uri, QUrl type, Nepomuk.ResourceManager manager)'''
        def __init__(self, uri, type, manager):
            '''void Nepomuk.Tag.__init__(QUrl uri, QUrl type, Nepomuk.ResourceManager manager)'''
        def resourceTypeUri(self):
            '''static QString Nepomuk.Tag.resourceTypeUri()'''
            return QString()
        def allTags(self):
            '''static list-of-Nepomuk.Tag Nepomuk.Tag.allTags()'''
            return [Nepomuk.Tag()]
        def tagOf(self):
            '''list-of-Nepomuk.Resource Nepomuk.Tag.tagOf()'''
            return [Nepomuk.Resource()]
    class Vocabulary():
        """"""
        class PIMO():
            """"""
            def pimoLong(self):
                '''static QUrl Nepomuk.Vocabulary.PIMO.pimoLong()'''
                return QUrl()
            def lat(self):
                '''static QUrl Nepomuk.Vocabulary.PIMO.lat()'''
                return QUrl()
            def alt(self):
                '''static QUrl Nepomuk.Vocabulary.PIMO.alt()'''
                return QUrl()
            def wikiText(self):
                '''static QUrl Nepomuk.Vocabulary.PIMO.wikiText()'''
                return QUrl()
            def taskDueTime(self):
                '''static QUrl Nepomuk.Vocabulary.PIMO.taskDueTime()'''
                return QUrl()
            def tagLabel(self):
                '''static QUrl Nepomuk.Vocabulary.PIMO.tagLabel()'''
                return QUrl()
            def superTopic(self):
                '''static QUrl Nepomuk.Vocabulary.PIMO.superTopic()'''
                return QUrl()
            def subTopic(self):
                '''static QUrl Nepomuk.Vocabulary.PIMO.subTopic()'''
                return QUrl()
            def roleHolder(self):
                '''static QUrl Nepomuk.Vocabulary.PIMO.roleHolder()'''
                return QUrl()
            def roleContext(self):
                '''static QUrl Nepomuk.Vocabulary.PIMO.roleContext()'''
                return QUrl()
            def referencingOccurrence(self):
                '''static QUrl Nepomuk.Vocabulary.PIMO.referencingOccurrence()'''
                return QUrl()
            def partOf(self):
                '''static QUrl Nepomuk.Vocabulary.PIMO.partOf()'''
                return QUrl()
            def organization(self):
                '''static QUrl Nepomuk.Vocabulary.PIMO.organization()'''
                return QUrl()
            def occurrence(self):
                '''static QUrl Nepomuk.Vocabulary.PIMO.occurrence()'''
                return QUrl()
            def objectProperty(self):
                '''static QUrl Nepomuk.Vocabulary.PIMO.objectProperty()'''
                return QUrl()
            def locatedWithin(self):
                '''static QUrl Nepomuk.Vocabulary.PIMO.locatedWithin()'''
                return QUrl()
            def jabberId(self):
                '''static QUrl Nepomuk.Vocabulary.PIMO.jabberId()'''
                return QUrl()
            def isWriteable(self):
                '''static QUrl Nepomuk.Vocabulary.PIMO.isWriteable()'''
                return QUrl()
            def isTagFor(self):
                '''static QUrl Nepomuk.Vocabulary.PIMO.isTagFor()'''
                return QUrl()
            def isRelated(self):
                '''static QUrl Nepomuk.Vocabulary.PIMO.isRelated()'''
                return QUrl()
            def isOrganizationMemberOf(self):
                '''static QUrl Nepomuk.Vocabulary.PIMO.isOrganizationMemberOf()'''
                return QUrl()
            def isLocationOf(self):
                '''static QUrl Nepomuk.Vocabulary.PIMO.isLocationOf()'''
                return QUrl()
            def isDefinedBy(self):
                '''static QUrl Nepomuk.Vocabulary.PIMO.isDefinedBy()'''
                return QUrl()
            def hasTag(self):
                '''static QUrl Nepomuk.Vocabulary.PIMO.hasTag()'''
                return QUrl()
            def hasRootTopic(self):
                '''static QUrl Nepomuk.Vocabulary.PIMO.hasRootTopic()'''
                return QUrl()
            def hasPart(self):
                '''static QUrl Nepomuk.Vocabulary.PIMO.hasPart()'''
                return QUrl()
            def hasOtherSlot(self):
                '''static QUrl Nepomuk.Vocabulary.PIMO.hasOtherSlot()'''
                return QUrl()
            def hasOtherRepresentation(self):
                '''static QUrl Nepomuk.Vocabulary.PIMO.hasOtherRepresentation()'''
                return QUrl()
            def hasOtherConceptualization(self):
                '''static QUrl Nepomuk.Vocabulary.PIMO.hasOtherConceptualization()'''
                return QUrl()
            def hasOrganizationMember(self):
                '''static QUrl Nepomuk.Vocabulary.PIMO.hasOrganizationMember()'''
                return QUrl()
            def hasLocation(self):
                '''static QUrl Nepomuk.Vocabulary.PIMO.hasLocation()'''
                return QUrl()
            def hasLocalNamespace(self):
                '''static QUrl Nepomuk.Vocabulary.PIMO.hasLocalNamespace()'''
                return QUrl()
            def hasGlobalNamespace(self):
                '''static QUrl Nepomuk.Vocabulary.PIMO.hasGlobalNamespace()'''
                return QUrl()
            def hasFolder(self):
                '''static QUrl Nepomuk.Vocabulary.PIMO.hasFolder()'''
                return QUrl()
            def hasDeprecatedRepresentation(self):
                '''static QUrl Nepomuk.Vocabulary.PIMO.hasDeprecatedRepresentation()'''
                return QUrl()
            def groundingOccurrence(self):
                '''static QUrl Nepomuk.Vocabulary.PIMO.groundingOccurrence()'''
                return QUrl()
            def groundingForDeletedThing(self):
                '''static QUrl Nepomuk.Vocabulary.PIMO.groundingForDeletedThing()'''
                return QUrl()
            def duration(self):
                '''static QUrl Nepomuk.Vocabulary.PIMO.duration()'''
                return QUrl()
            def dtstart(self):
                '''static QUrl Nepomuk.Vocabulary.PIMO.dtstart()'''
                return QUrl()
            def dtend(self):
                '''static QUrl Nepomuk.Vocabulary.PIMO.dtend()'''
                return QUrl()
            def datatypeProperty(self):
                '''static QUrl Nepomuk.Vocabulary.PIMO.datatypeProperty()'''
                return QUrl()
            def creator(self):
                '''static QUrl Nepomuk.Vocabulary.PIMO.creator()'''
                return QUrl()
            def createdPimo(self):
                '''static QUrl Nepomuk.Vocabulary.PIMO.createdPimo()'''
                return QUrl()
            def containsLocation(self):
                '''static QUrl Nepomuk.Vocabulary.PIMO.containsLocation()'''
                return QUrl()
            def classRole(self):
                '''static QUrl Nepomuk.Vocabulary.PIMO.classRole()'''
                return QUrl()
            def attends(self):
                '''static QUrl Nepomuk.Vocabulary.PIMO.attends()'''
                return QUrl()
            def attendingMeeting(self):
                '''static QUrl Nepomuk.Vocabulary.PIMO.attendingMeeting()'''
                return QUrl()
            def attendee(self):
                '''static QUrl Nepomuk.Vocabulary.PIMO.attendee()'''
                return QUrl()
            def associationMember(self):
                '''static QUrl Nepomuk.Vocabulary.PIMO.associationMember()'''
                return QUrl()
            def associationEffectual(self):
                '''static QUrl Nepomuk.Vocabulary.PIMO.associationEffectual()'''
                return QUrl()
            def Topic(self):
                '''static QUrl Nepomuk.Vocabulary.PIMO.Topic()'''
                return QUrl()
            def Thing(self):
                '''static QUrl Nepomuk.Vocabulary.PIMO.Thing()'''
                return QUrl()
            def Task(self):
                '''static QUrl Nepomuk.Vocabulary.PIMO.Task()'''
                return QUrl()
            def Tag(self):
                '''static QUrl Nepomuk.Vocabulary.PIMO.Tag()'''
                return QUrl()
            def State(self):
                '''static QUrl Nepomuk.Vocabulary.PIMO.State()'''
                return QUrl()
            def SocialEvent(self):
                '''static QUrl Nepomuk.Vocabulary.PIMO.SocialEvent()'''
                return QUrl()
            def RuleViewSpecificationOccurrenceClosure(self):
                '''static QUrl Nepomuk.Vocabulary.PIMO.RuleViewSpecificationOccurrenceClosure()'''
                return QUrl()
            def RuleViewSpecificationInferOccurrences(self):
                '''static QUrl Nepomuk.Vocabulary.PIMO.RuleViewSpecificationInferOccurrences()'''
                return QUrl()
            def RuleViewSpecificationGroundingClosure(self):
                '''static QUrl Nepomuk.Vocabulary.PIMO.RuleViewSpecificationGroundingClosure()'''
                return QUrl()
            def Room(self):
                '''static QUrl Nepomuk.Vocabulary.PIMO.Room()'''
                return QUrl()
            def Project(self):
                '''static QUrl Nepomuk.Vocabulary.PIMO.Project()'''
                return QUrl()
            def ProcessConcept(self):
                '''static QUrl Nepomuk.Vocabulary.PIMO.ProcessConcept()'''
                return QUrl()
            def PersonalInformationModel(self):
                '''static QUrl Nepomuk.Vocabulary.PIMO.PersonalInformationModel()'''
                return QUrl()
            def PersonRole(self):
                '''static QUrl Nepomuk.Vocabulary.PIMO.PersonRole()'''
                return QUrl()
            def PersonGroup(self):
                '''static QUrl Nepomuk.Vocabulary.PIMO.PersonGroup()'''
                return QUrl()
            def Person(self):
                '''static QUrl Nepomuk.Vocabulary.PIMO.Person()'''
                return QUrl()
            def OrganizationMember(self):
                '''static QUrl Nepomuk.Vocabulary.PIMO.OrganizationMember()'''
                return QUrl()
            def Organization(self):
                '''static QUrl Nepomuk.Vocabulary.PIMO.Organization()'''
                return QUrl()
            def OccurrenceClosure(self):
                '''static QUrl Nepomuk.Vocabulary.PIMO.OccurrenceClosure()'''
                return QUrl()
            def Note(self):
                '''static QUrl Nepomuk.Vocabulary.PIMO.Note()'''
                return QUrl()
            def Meeting(self):
                '''static QUrl Nepomuk.Vocabulary.PIMO.Meeting()'''
                return QUrl()
            def LogicalMediaType(self):
                '''static QUrl Nepomuk.Vocabulary.PIMO.LogicalMediaType()'''
                return QUrl()
            def Location(self):
                '''static QUrl Nepomuk.Vocabulary.PIMO.Location()'''
                return QUrl()
            def Locatable(self):
                '''static QUrl Nepomuk.Vocabulary.PIMO.Locatable()'''
                return QUrl()
            def InferOccurrences(self):
                '''static QUrl Nepomuk.Vocabulary.PIMO.InferOccurrences()'''
                return QUrl()
            def GroundingClosure(self):
                '''static QUrl Nepomuk.Vocabulary.PIMO.GroundingClosure()'''
                return QUrl()
            def FullPimoView(self):
                '''static QUrl Nepomuk.Vocabulary.PIMO.FullPimoView()'''
                return QUrl()
            def Event(self):
                '''static QUrl Nepomuk.Vocabulary.PIMO.Event()'''
                return QUrl()
            def Document(self):
                '''static QUrl Nepomuk.Vocabulary.PIMO.Document()'''
                return QUrl()
            def Country(self):
                '''static QUrl Nepomuk.Vocabulary.PIMO.Country()'''
                return QUrl()
            def Contract(self):
                '''static QUrl Nepomuk.Vocabulary.PIMO.Contract()'''
                return QUrl()
            def ConcreteClass(self):
                '''static QUrl Nepomuk.Vocabulary.PIMO.ConcreteClass()'''
                return QUrl()
            def Collection(self):
                '''static QUrl Nepomuk.Vocabulary.PIMO.Collection()'''
                return QUrl()
            def ClassRole(self):
                '''static QUrl Nepomuk.Vocabulary.PIMO.ClassRole()'''
                return QUrl()
            def ClassOrThingOrPropertyOrAssociation(self):
                '''static QUrl Nepomuk.Vocabulary.PIMO.ClassOrThingOrPropertyOrAssociation()'''
                return QUrl()
            def ClassOrThing(self):
                '''static QUrl Nepomuk.Vocabulary.PIMO.ClassOrThing()'''
                return QUrl()
            def City(self):
                '''static QUrl Nepomuk.Vocabulary.PIMO.City()'''
                return QUrl()
            def Building(self):
                '''static QUrl Nepomuk.Vocabulary.PIMO.Building()'''
                return QUrl()
            def BlogPost(self):
                '''static QUrl Nepomuk.Vocabulary.PIMO.BlogPost()'''
                return QUrl()
            def Attendee(self):
                '''static QUrl Nepomuk.Vocabulary.PIMO.Attendee()'''
                return QUrl()
            def Association(self):
                '''static QUrl Nepomuk.Vocabulary.PIMO.Association()'''
                return QUrl()
            def Agent(self):
                '''static QUrl Nepomuk.Vocabulary.PIMO.Agent()'''
                return QUrl()
            def AbstractClass(self):
                '''static QUrl Nepomuk.Vocabulary.PIMO.AbstractClass()'''
                return QUrl()
            def nrlOntologyGraph(self):
                '''static QUrl Nepomuk.Vocabulary.PIMO.nrlOntologyGraph()'''
                return QUrl()
            def pimoNamespace(self):
                '''static QUrl Nepomuk.Vocabulary.PIMO.pimoNamespace()'''
                return QUrl()
    class Types():
        """"""
        class Class(Nepomuk.Types.Entity):
            """"""
            def __init__(self):
                '''void Nepomuk.Types.Class.__init__()'''
            def __init__(self, uri):
                '''void Nepomuk.Types.Class.__init__(QUrl uri)'''
            def __init__(self):
                '''Nepomuk.Types.Class Nepomuk.Types.Class.__init__()'''
                return Nepomuk.Types.Class()
            def isSubClassOf(self, other):
                '''bool Nepomuk.Types.Class.isSubClassOf(Nepomuk.Types.Class other)'''
                return bool()
            def isParentOf(self, other):
                '''bool Nepomuk.Types.Class.isParentOf(Nepomuk.Types.Class other)'''
                return bool()
            def allSubClasses(self):
                '''list-of-Nepomuk.Types.Class Nepomuk.Types.Class.allSubClasses()'''
                return [Nepomuk.Types.Class()]
            def allParentClasses(self):
                '''list-of-Nepomuk.Types.Class Nepomuk.Types.Class.allParentClasses()'''
                return [Nepomuk.Types.Class()]
            def subClasses(self):
                '''list-of-Nepomuk.Types.Class Nepomuk.Types.Class.subClasses()'''
                return [Nepomuk.Types.Class()]
            def parentClasses(self):
                '''list-of-Nepomuk.Types.Class Nepomuk.Types.Class.parentClasses()'''
                return [Nepomuk.Types.Class()]
            def findPropertyByLabel(self, label, language = QString()):
                '''Nepomuk.Types.Property Nepomuk.Types.Class.findPropertyByLabel(QString label, QString language = QString())'''
                return Nepomuk.Types.Property()
            def findPropertyByName(self, name):
                '''Nepomuk.Types.Property Nepomuk.Types.Class.findPropertyByName(QString name)'''
                return Nepomuk.Types.Property()
            def domainOf(self):
                '''list-of-Nepomuk.Types.Property Nepomuk.Types.Class.domainOf()'''
                return [Nepomuk.Types.Property()]
            def rangeOf(self):
                '''list-of-Nepomuk.Types.Property Nepomuk.Types.Class.rangeOf()'''
                return [Nepomuk.Types.Property()]
    class Query():
        """"""
        class Query():
            """"""
            class QueryFlags():
                """"""
                def __init__(self):
                    '''Nepomuk.Query.Query.QueryFlags Nepomuk.Query.Query.QueryFlags.__init__()'''
                    return Nepomuk.Query.Query.QueryFlags()
                def __init__(self):
                    '''int Nepomuk.Query.Query.QueryFlags.__init__()'''
                    return int()
                def __init__(self):
                    '''void Nepomuk.Query.Query.QueryFlags.__init__()'''
                def __bool__(self):
                    '''int Nepomuk.Query.Query.QueryFlags.__bool__()'''
                    return int()
                def __ne__(self, f):
                    '''bool Nepomuk.Query.Query.QueryFlags.__ne__(Nepomuk.Query.Query.QueryFlags f)'''
                    return bool()
                def __eq__(self, f):
                    '''bool Nepomuk.Query.Query.QueryFlags.__eq__(Nepomuk.Query.Query.QueryFlags f)'''
                    return bool()
                def __invert__(self):
                    '''Nepomuk.Query.Query.QueryFlags Nepomuk.Query.Query.QueryFlags.__invert__()'''
                    return Nepomuk.Query.Query.QueryFlags()
                def __and__(self, mask):
                    '''Nepomuk.Query.Query.QueryFlags Nepomuk.Query.Query.QueryFlags.__and__(int mask)'''
                    return Nepomuk.Query.Query.QueryFlags()
                def __xor__(self, f):
                    '''Nepomuk.Query.Query.QueryFlags Nepomuk.Query.Query.QueryFlags.__xor__(Nepomuk.Query.Query.QueryFlags f)'''
                    return Nepomuk.Query.Query.QueryFlags()
                def __xor__(self, f):
                    '''Nepomuk.Query.Query.QueryFlags Nepomuk.Query.Query.QueryFlags.__xor__(int f)'''
                    return Nepomuk.Query.Query.QueryFlags()
                def __or__(self, f):
                    '''Nepomuk.Query.Query.QueryFlags Nepomuk.Query.Query.QueryFlags.__or__(Nepomuk.Query.Query.QueryFlags f)'''
                    return Nepomuk.Query.Query.QueryFlags()
                def __or__(self, f):
                    '''Nepomuk.Query.Query.QueryFlags Nepomuk.Query.Query.QueryFlags.__or__(int f)'''
                    return Nepomuk.Query.Query.QueryFlags()
                def __int__(self):
                    '''int Nepomuk.Query.Query.QueryFlags.__int__()'''
                    return int()
                def __ixor__(self, f):
                    '''Nepomuk.Query.Query.QueryFlags Nepomuk.Query.Query.QueryFlags.__ixor__(Nepomuk.Query.Query.QueryFlags f)'''
                    return Nepomuk.Query.Query.QueryFlags()
                def __ior__(self, f):
                    '''Nepomuk.Query.Query.QueryFlags Nepomuk.Query.Query.QueryFlags.__ior__(Nepomuk.Query.Query.QueryFlags f)'''
                    return Nepomuk.Query.Query.QueryFlags()
                def __iand__(self, mask):
                    '''Nepomuk.Query.Query.QueryFlags Nepomuk.Query.Query.QueryFlags.__iand__(int mask)'''
                    return Nepomuk.Query.Query.QueryFlags()
    class Service(QObject):
        """"""
        def __init__(self, parent = None, delayedInitialization = False):
            '''void Nepomuk.Service.__init__(QObject parent = None, bool delayedInitialization = False)'''
        def mainModel(self):
            '''Soprano.Model Nepomuk.Service.mainModel()'''
            return Soprano.Model()
        def setServiceInitialized(self, success):
            '''void Nepomuk.Service.setServiceInitialized(bool success)'''
    class Vocabulary():
        """"""
        class NIE():
            """"""
            def modified(self):
                '''static QUrl Nepomuk.Vocabulary.NIE.modified()'''
                return QUrl()
            def htmlContent(self):
                '''static QUrl Nepomuk.Vocabulary.NIE.htmlContent()'''
                return QUrl()
            def contentModified(self):
                '''static QUrl Nepomuk.Vocabulary.NIE.contentModified()'''
                return QUrl()
            def version(self):
                '''static QUrl Nepomuk.Vocabulary.NIE.version()'''
                return QUrl()
            def url(self):
                '''static QUrl Nepomuk.Vocabulary.NIE.url()'''
                return QUrl()
            def title(self):
                '''static QUrl Nepomuk.Vocabulary.NIE.title()'''
                return QUrl()
            def subject(self):
                '''static QUrl Nepomuk.Vocabulary.NIE.subject()'''
                return QUrl()
            def rootElementOf(self):
                '''static QUrl Nepomuk.Vocabulary.NIE.rootElementOf()'''
                return QUrl()
            def relatedTo(self):
                '''static QUrl Nepomuk.Vocabulary.NIE.relatedTo()'''
                return QUrl()
            def plainTextContent(self):
                '''static QUrl Nepomuk.Vocabulary.NIE.plainTextContent()'''
                return QUrl()
            def mimeType(self):
                '''static QUrl Nepomuk.Vocabulary.NIE.mimeType()'''
                return QUrl()
            def links(self):
                '''static QUrl Nepomuk.Vocabulary.NIE.links()'''
                return QUrl()
            def licenseType(self):
                '''static QUrl Nepomuk.Vocabulary.NIE.licenseType()'''
                return QUrl()
            def license(self):
                '''static QUrl Nepomuk.Vocabulary.NIE.license()'''
                return QUrl()
            def legal(self):
                '''static QUrl Nepomuk.Vocabulary.NIE.legal()'''
                return QUrl()
            def lastRefreshed(self):
                '''static QUrl Nepomuk.Vocabulary.NIE.lastRefreshed()'''
                return QUrl()
            def lastModified(self):
                '''static QUrl Nepomuk.Vocabulary.NIE.lastModified()'''
                return QUrl()
            def language(self):
                '''static QUrl Nepomuk.Vocabulary.NIE.language()'''
                return QUrl()
            def keyword(self):
                '''static QUrl Nepomuk.Vocabulary.NIE.keyword()'''
                return QUrl()
            def isStoredAs(self):
                '''static QUrl Nepomuk.Vocabulary.NIE.isStoredAs()'''
                return QUrl()
            def isPartOf(self):
                '''static QUrl Nepomuk.Vocabulary.NIE.isPartOf()'''
                return QUrl()
            def isLogicalPartOf(self):
                '''static QUrl Nepomuk.Vocabulary.NIE.isLogicalPartOf()'''
                return QUrl()
            def interpretedAs(self):
                '''static QUrl Nepomuk.Vocabulary.NIE.interpretedAs()'''
                return QUrl()
            def informationElementDate(self):
                '''static QUrl Nepomuk.Vocabulary.NIE.informationElementDate()'''
                return QUrl()
            def identifier(self):
                '''static QUrl Nepomuk.Vocabulary.NIE.identifier()'''
                return QUrl()
            def hasPart(self):
                '''static QUrl Nepomuk.Vocabulary.NIE.hasPart()'''
                return QUrl()
            def hasLogicalPart(self):
                '''static QUrl Nepomuk.Vocabulary.NIE.hasLogicalPart()'''
                return QUrl()
            def generatorOption(self):
                '''static QUrl Nepomuk.Vocabulary.NIE.generatorOption()'''
                return QUrl()
            def generator(self):
                '''static QUrl Nepomuk.Vocabulary.NIE.generator()'''
                return QUrl()
            def disclaimer(self):
                '''static QUrl Nepomuk.Vocabulary.NIE.disclaimer()'''
                return QUrl()
            def description(self):
                '''static QUrl Nepomuk.Vocabulary.NIE.description()'''
                return QUrl()
            def depends(self):
                '''static QUrl Nepomuk.Vocabulary.NIE.depends()'''
                return QUrl()
            def dataSource(self):
                '''static QUrl Nepomuk.Vocabulary.NIE.dataSource()'''
                return QUrl()
            def created(self):
                '''static QUrl Nepomuk.Vocabulary.NIE.created()'''
                return QUrl()
            def coreGraph(self):
                '''static QUrl Nepomuk.Vocabulary.NIE.coreGraph()'''
                return QUrl()
            def copyright(self):
                '''static QUrl Nepomuk.Vocabulary.NIE.copyright()'''
                return QUrl()
            def contentSize(self):
                '''static QUrl Nepomuk.Vocabulary.NIE.contentSize()'''
                return QUrl()
            def contentLastModified(self):
                '''static QUrl Nepomuk.Vocabulary.NIE.contentLastModified()'''
                return QUrl()
            def contentCreated(self):
                '''static QUrl Nepomuk.Vocabulary.NIE.contentCreated()'''
                return QUrl()
            def comment(self):
                '''static QUrl Nepomuk.Vocabulary.NIE.comment()'''
                return QUrl()
            def characterSet(self):
                '''static QUrl Nepomuk.Vocabulary.NIE.characterSet()'''
                return QUrl()
            def byteSize(self):
                '''static QUrl Nepomuk.Vocabulary.NIE.byteSize()'''
                return QUrl()
            def InformationElement(self):
                '''static QUrl Nepomuk.Vocabulary.NIE.InformationElement()'''
                return QUrl()
            def DataSource(self):
                '''static QUrl Nepomuk.Vocabulary.NIE.DataSource()'''
                return QUrl()
            def DataObject(self):
                '''static QUrl Nepomuk.Vocabulary.NIE.DataObject()'''
                return QUrl()
            def nrlOntologyGraph(self):
                '''static QUrl Nepomuk.Vocabulary.NIE.nrlOntologyGraph()'''
                return QUrl()
            def nieNamespace(self):
                '''static QUrl Nepomuk.Vocabulary.NIE.nieNamespace()'''
                return QUrl()
    class Variant():
        """"""
        def __init__(self):
            '''void Nepomuk.Variant.__init__()'''
        def __init__(self, other):
            '''void Nepomuk.Variant.__init__(Nepomuk.Variant other)'''
        def __init__(self, other):
            '''void Nepomuk.Variant.__init__(QVariant other)'''
        def __init__(self, i):
            '''void Nepomuk.Variant.__init__(int i)'''
        def __init__(self, d):
            '''void Nepomuk.Variant.__init__(float d)'''
        def __init__(self, string):
            '''void Nepomuk.Variant.__init__(QString string)'''
        def __init__(self, date):
            '''void Nepomuk.Variant.__init__(QDate date)'''
        def __init__(self, time):
            '''void Nepomuk.Variant.__init__(QTime time)'''
        def __init__(self, datetime):
            '''void Nepomuk.Variant.__init__(QDateTime datetime)'''
        def __init__(self, url):
            '''void Nepomuk.Variant.__init__(QUrl url)'''
        def __init__(self, r):
            '''void Nepomuk.Variant.__init__(Nepomuk.Resource r)'''
        def __init__(self, i):
            '''void Nepomuk.Variant.__init__(list-of-int i)'''
        def __init__(self, i):
            '''void Nepomuk.Variant.__init__(list-of-int i)'''
        def __init__(self, d):
            '''void Nepomuk.Variant.__init__(list-of-float d)'''
        def __init__(self, stringlist):
            '''void Nepomuk.Variant.__init__(QStringList stringlist)'''
        def __init__(self, date):
            '''void Nepomuk.Variant.__init__(list-of-QDate date)'''
        def __init__(self, time):
            '''void Nepomuk.Variant.__init__(list-of-QTime time)'''
        def __init__(self, datetime):
            '''void Nepomuk.Variant.__init__(list-of-QDateTime datetime)'''
        def __init__(self, url):
            '''void Nepomuk.Variant.__init__(list-of-QUrl url)'''
        def __init__(self, r):
            '''void Nepomuk.Variant.__init__(list-of-Nepomuk.Resource r)'''
        def __init__(self, vl):
            '''void Nepomuk.Variant.__init__(list-of-Nepomuk.Variant vl)'''
        def fromNodeList(self, node):
            '''static Nepomuk.Variant Nepomuk.Variant.fromNodeList(list-of-Soprano.Node node)'''
            return Nepomuk.Variant()
        def toNodeList(self):
            '''list-of-Soprano.Node Nepomuk.Variant.toNodeList()'''
            return [Soprano.Node()]
        def toNode(self):
            '''Soprano.Node Nepomuk.Variant.toNode()'''
            return Soprano.Node()
        def fromNode(self, node):
            '''static Nepomuk.Variant Nepomuk.Variant.fromNode(Soprano.Node node)'''
            return Nepomuk.Variant()
        def fromString(self, value, type):
            '''static Nepomuk.Variant Nepomuk.Variant.fromString(QString value, int type)'''
            return Nepomuk.Variant()
        def toVariantList(self):
            '''list-of-Nepomuk.Variant Nepomuk.Variant.toVariantList()'''
            return [Nepomuk.Variant()]
        def toResourceList(self):
            '''list-of-Nepomuk.Resource Nepomuk.Variant.toResourceList()'''
            return [Nepomuk.Resource()]
        def toUrlList(self):
            '''list-of-QUrl Nepomuk.Variant.toUrlList()'''
            return [QUrl()]
        def toDateTimeList(self):
            '''list-of-QDateTime Nepomuk.Variant.toDateTimeList()'''
            return [QDateTime()]
        def toTimeList(self):
            '''list-of-QTime Nepomuk.Variant.toTimeList()'''
            return [QTime()]
        def toDateList(self):
            '''list-of-QDate Nepomuk.Variant.toDateList()'''
            return [QDate()]
        def toStringList(self):
            '''QStringList Nepomuk.Variant.toStringList()'''
            return QStringList()
        def toDoubleList(self):
            '''list-of-float Nepomuk.Variant.toDoubleList()'''
            return [float()]
        def toUnsignedIntList(self):
            '''list-of-int Nepomuk.Variant.toUnsignedIntList()'''
            return [int()]
        def toIntList(self):
            '''list-of-int Nepomuk.Variant.toIntList()'''
            return [int()]
        def toResource(self):
            '''Nepomuk.Resource Nepomuk.Variant.toResource()'''
            return Nepomuk.Resource()
        def toUrl(self):
            '''QUrl Nepomuk.Variant.toUrl()'''
            return QUrl()
        def toDateTime(self):
            '''QDateTime Nepomuk.Variant.toDateTime()'''
            return QDateTime()
        def toTime(self):
            '''QTime Nepomuk.Variant.toTime()'''
            return QTime()
        def toDate(self):
            '''QDate Nepomuk.Variant.toDate()'''
            return QDate()
        def toString(self):
            '''QString Nepomuk.Variant.toString()'''
            return QString()
        def toDouble(self):
            '''float Nepomuk.Variant.toDouble()'''
            return float()
        def toBool(self):
            '''bool Nepomuk.Variant.toBool()'''
            return bool()
        def toUnsignedInt64(self):
            '''int Nepomuk.Variant.toUnsignedInt64()'''
            return int()
        def toUnsignedInt(self):
            '''int Nepomuk.Variant.toUnsignedInt()'''
            return int()
        def toInt64(self):
            '''int Nepomuk.Variant.toInt64()'''
            return int()
        def toInt(self):
            '''int Nepomuk.Variant.toInt()'''
            return int()
        def variant(self):
            '''QVariant Nepomuk.Variant.variant()'''
            return QVariant()
        def isResourceList(self):
            '''bool Nepomuk.Variant.isResourceList()'''
            return bool()
        def isUrlList(self):
            '''bool Nepomuk.Variant.isUrlList()'''
            return bool()
        def isDateTimeList(self):
            '''bool Nepomuk.Variant.isDateTimeList()'''
            return bool()
        def isTimeList(self):
            '''bool Nepomuk.Variant.isTimeList()'''
            return bool()
        def isDateList(self):
            '''bool Nepomuk.Variant.isDateList()'''
            return bool()
        def isStringList(self):
            '''bool Nepomuk.Variant.isStringList()'''
            return bool()
        def isDoubleList(self):
            '''bool Nepomuk.Variant.isDoubleList()'''
            return bool()
        def isBoolList(self):
            '''bool Nepomuk.Variant.isBoolList()'''
            return bool()
        def isUnsignedInt64List(self):
            '''bool Nepomuk.Variant.isUnsignedInt64List()'''
            return bool()
        def isUnsignedIntList(self):
            '''bool Nepomuk.Variant.isUnsignedIntList()'''
            return bool()
        def isInt64List(self):
            '''bool Nepomuk.Variant.isInt64List()'''
            return bool()
        def isIntList(self):
            '''bool Nepomuk.Variant.isIntList()'''
            return bool()
        def isResource(self):
            '''bool Nepomuk.Variant.isResource()'''
            return bool()
        def isUrl(self):
            '''bool Nepomuk.Variant.isUrl()'''
            return bool()
        def isDateTime(self):
            '''bool Nepomuk.Variant.isDateTime()'''
            return bool()
        def isTime(self):
            '''bool Nepomuk.Variant.isTime()'''
            return bool()
        def isDate(self):
            '''bool Nepomuk.Variant.isDate()'''
            return bool()
        def isString(self):
            '''bool Nepomuk.Variant.isString()'''
            return bool()
        def isDouble(self):
            '''bool Nepomuk.Variant.isDouble()'''
            return bool()
        def isBool(self):
            '''bool Nepomuk.Variant.isBool()'''
            return bool()
        def isUnsignedInt64(self):
            '''bool Nepomuk.Variant.isUnsignedInt64()'''
            return bool()
        def isUnsignedInt(self):
            '''bool Nepomuk.Variant.isUnsignedInt()'''
            return bool()
        def isInt64(self):
            '''bool Nepomuk.Variant.isInt64()'''
            return bool()
        def isInt(self):
            '''bool Nepomuk.Variant.isInt()'''
            return bool()
        def isList(self):
            '''bool Nepomuk.Variant.isList()'''
            return bool()
        def simpleType(self):
            '''int Nepomuk.Variant.simpleType()'''
            return int()
        def type(self):
            '''int Nepomuk.Variant.type()'''
            return int()
        def isValid(self):
            '''bool Nepomuk.Variant.isValid()'''
            return bool()
        def __ne__(self, other):
            '''bool Nepomuk.Variant.__ne__(Nepomuk.Variant other)'''
            return bool()
        def __eq__(self, other):
            '''bool Nepomuk.Variant.__eq__(Nepomuk.Variant other)'''
            return bool()
        def append(self, i):
            '''void Nepomuk.Variant.append(int i)'''
        def append(self, d):
            '''void Nepomuk.Variant.append(float d)'''
        def append(self, string):
            '''void Nepomuk.Variant.append(QString string)'''
        def append(self, date):
            '''void Nepomuk.Variant.append(QDate date)'''
        def append(self, time):
            '''void Nepomuk.Variant.append(QTime time)'''
        def append(self, datetime):
            '''void Nepomuk.Variant.append(QDateTime datetime)'''
        def append(self, url):
            '''void Nepomuk.Variant.append(QUrl url)'''
        def append(self, r):
            '''void Nepomuk.Variant.append(Nepomuk.Resource r)'''
        def append(self, v):
            '''void Nepomuk.Variant.append(Nepomuk.Variant v)'''
    class MassUpdateJob(KJob):
        """"""
        def __init__(self, parent = None):
            '''void Nepomuk.MassUpdateJob.__init__(QObject parent = None)'''
        def doResume(self):
            '''bool Nepomuk.MassUpdateJob.doResume()'''
            return bool()
        def doSuspend(self):
            '''bool Nepomuk.MassUpdateJob.doSuspend()'''
            return bool()
        def doKill(self):
            '''bool Nepomuk.MassUpdateJob.doKill()'''
            return bool()
        def commentResources(self, comment):
            '''static list-of-Nepomuk.Resource Nepomuk.MassUpdateJob.commentResources(QString comment)'''
            return [Nepomuk.Resource()]
        def rateResources(self, rating):
            '''static list-of-Nepomuk.Resource Nepomuk.MassUpdateJob.rateResources(int rating)'''
            return [Nepomuk.Resource()]
        def tagResources(self, tags):
            '''static list-of-Nepomuk.Resource Nepomuk.MassUpdateJob.tagResources(list-of-Nepomuk.Tag tags)'''
            return [Nepomuk.Resource()]
        def start(self):
            '''void Nepomuk.MassUpdateJob.start()'''
        def setProperties(self, props):
            '''void Nepomuk.MassUpdateJob.setProperties(list-of-tuple-of-QUrl-Nepomuk.Variant props)'''
        def setResources(self):
            '''list-of-Nepomuk.Resource Nepomuk.MassUpdateJob.setResources()'''
            return [Nepomuk.Resource()]
        def setFiles(self, urls):
            '''void Nepomuk.MassUpdateJob.setFiles(KUrl.List urls)'''
    class Vocabulary():
        """"""
        class NCAL():
            """"""
            def yearly(self):
                '''static QUrl Nepomuk.Vocabulary.NCAL.yearly()'''
                return QUrl()
            def wkst(self):
                '''static QUrl Nepomuk.Vocabulary.NCAL.wkst()'''
                return QUrl()
            def weekly(self):
                '''static QUrl Nepomuk.Vocabulary.NCAL.weekly()'''
                return QUrl()
            def wednesday(self):
                '''static QUrl Nepomuk.Vocabulary.NCAL.wednesday()'''
                return QUrl()
            def version(self):
                '''static QUrl Nepomuk.Vocabulary.NCAL.version()'''
                return QUrl()
            def url(self):
                '''static QUrl Nepomuk.Vocabulary.NCAL.url()'''
                return QUrl()
            def until(self):
                '''static QUrl Nepomuk.Vocabulary.NCAL.until()'''
                return QUrl()
            def unknownUserType(self):
                '''static QUrl Nepomuk.Vocabulary.NCAL.unknownUserType()'''
                return QUrl()
            def uid(self):
                '''static QUrl Nepomuk.Vocabulary.NCAL.uid()'''
                return QUrl()
            def tzurl(self):
                '''static QUrl Nepomuk.Vocabulary.NCAL.tzurl()'''
                return QUrl()
            def tzoffsetto(self):
                '''static QUrl Nepomuk.Vocabulary.NCAL.tzoffsetto()'''
                return QUrl()
            def tzoffsetfrom(self):
                '''static QUrl Nepomuk.Vocabulary.NCAL.tzoffsetfrom()'''
                return QUrl()
            def tzname(self):
                '''static QUrl Nepomuk.Vocabulary.NCAL.tzname()'''
                return QUrl()
            def tzid(self):
                '''static QUrl Nepomuk.Vocabulary.NCAL.tzid()'''
                return QUrl()
            def tuesday(self):
                '''static QUrl Nepomuk.Vocabulary.NCAL.tuesday()'''
                return QUrl()
            def triggerDuration(self):
                '''static QUrl Nepomuk.Vocabulary.NCAL.triggerDuration()'''
                return QUrl()
            def triggerDateTime(self):
                '''static QUrl Nepomuk.Vocabulary.NCAL.triggerDateTime()'''
                return QUrl()
            def trigger(self):
                '''static QUrl Nepomuk.Vocabulary.NCAL.trigger()'''
                return QUrl()
            def transparentTransparency(self):
                '''static QUrl Nepomuk.Vocabulary.NCAL.transparentTransparency()'''
                return QUrl()
            def transp(self):
                '''static QUrl Nepomuk.Vocabulary.NCAL.transp()'''
                return QUrl()
            def todoStatus(self):
                '''static QUrl Nepomuk.Vocabulary.NCAL.todoStatus()'''
                return QUrl()
            def thursday(self):
                '''static QUrl Nepomuk.Vocabulary.NCAL.thursday()'''
                return QUrl()
            def thisAndPriorRange(self):
                '''static QUrl Nepomuk.Vocabulary.NCAL.thisAndPriorRange()'''
                return QUrl()
            def thisAndFutureRange(self):
                '''static QUrl Nepomuk.Vocabulary.NCAL.thisAndFutureRange()'''
                return QUrl()
            def tentativeStatus(self):
                '''static QUrl Nepomuk.Vocabulary.NCAL.tentativeStatus()'''
                return QUrl()
            def tentativeParticipationStatus(self):
                '''static QUrl Nepomuk.Vocabulary.NCAL.tentativeParticipationStatus()'''
                return QUrl()
            def sunday(self):
                '''static QUrl Nepomuk.Vocabulary.NCAL.sunday()'''
                return QUrl()
            def summaryAltRep(self):
                '''static QUrl Nepomuk.Vocabulary.NCAL.summaryAltRep()'''
                return QUrl()
            def summary(self):
                '''static QUrl Nepomuk.Vocabulary.NCAL.summary()'''
                return QUrl()
            def statusDescription(self):
                '''static QUrl Nepomuk.Vocabulary.NCAL.statusDescription()'''
                return QUrl()
            def startTriggerRelation(self):
                '''static QUrl Nepomuk.Vocabulary.NCAL.startTriggerRelation()'''
                return QUrl()
            def standard(self):
                '''static QUrl Nepomuk.Vocabulary.NCAL.standard()'''
                return QUrl()
            def sequence(self):
                '''static QUrl Nepomuk.Vocabulary.NCAL.sequence()'''
                return QUrl()
            def sentBy(self):
                '''static QUrl Nepomuk.Vocabulary.NCAL.sentBy()'''
                return QUrl()
            def secondly(self):
                '''static QUrl Nepomuk.Vocabulary.NCAL.secondly()'''
                return QUrl()
            def saturday(self):
                '''static QUrl Nepomuk.Vocabulary.NCAL.saturday()'''
                return QUrl()
            def rsvp(self):
                '''static QUrl Nepomuk.Vocabulary.NCAL.rsvp()'''
                return QUrl()
            def rrule(self):
                '''static QUrl Nepomuk.Vocabulary.NCAL.rrule()'''
                return QUrl()
            def roomUserType(self):
                '''static QUrl Nepomuk.Vocabulary.NCAL.roomUserType()'''
                return QUrl()
            def role(self):
                '''static QUrl Nepomuk.Vocabulary.NCAL.role()'''
                return QUrl()
            def returnStatus(self):
                '''static QUrl Nepomuk.Vocabulary.NCAL.returnStatus()'''
                return QUrl()
            def resourcesAltRep(self):
                '''static QUrl Nepomuk.Vocabulary.NCAL.resourcesAltRep()'''
                return QUrl()
            def resources(self):
                '''static QUrl Nepomuk.Vocabulary.NCAL.resources()'''
                return QUrl()
            def resourceUserType(self):
                '''static QUrl Nepomuk.Vocabulary.NCAL.resourceUserType()'''
                return QUrl()
            def requestStatusData(self):
                '''static QUrl Nepomuk.Vocabulary.NCAL.requestStatusData()'''
                return QUrl()
            def requestStatus(self):
                '''static QUrl Nepomuk.Vocabulary.NCAL.requestStatus()'''
                return QUrl()
            def reqParticipantRole(self):
                '''static QUrl Nepomuk.Vocabulary.NCAL.reqParticipantRole()'''
                return QUrl()
            def repeat(self):
                '''static QUrl Nepomuk.Vocabulary.NCAL.repeat()'''
                return QUrl()
            def relatedToSibling(self):
                '''static QUrl Nepomuk.Vocabulary.NCAL.relatedToSibling()'''
                return QUrl()
            def relatedToParent(self):
                '''static QUrl Nepomuk.Vocabulary.NCAL.relatedToParent()'''
                return QUrl()
            def relatedToChild(self):
                '''static QUrl Nepomuk.Vocabulary.NCAL.relatedToChild()'''
                return QUrl()
            def related(self):
                '''static QUrl Nepomuk.Vocabulary.NCAL.related()'''
                return QUrl()
            def recurrenceIdDateTime(self):
                '''static QUrl Nepomuk.Vocabulary.NCAL.recurrenceIdDateTime()'''
                return QUrl()
            def recurrenceId(self):
                '''static QUrl Nepomuk.Vocabulary.NCAL.recurrenceId()'''
                return QUrl()
            def rdate(self):
                '''static QUrl Nepomuk.Vocabulary.NCAL.rdate()'''
                return QUrl()
            def range(self):
                '''static QUrl Nepomuk.Vocabulary.NCAL.range()'''
                return QUrl()
            def publicClassification(self):
                '''static QUrl Nepomuk.Vocabulary.NCAL.publicClassification()'''
                return QUrl()
            def prodid(self):
                '''static QUrl Nepomuk.Vocabulary.NCAL.prodid()'''
                return QUrl()
            def procedureAction(self):
                '''static QUrl Nepomuk.Vocabulary.NCAL.procedureAction()'''
                return QUrl()
            def privateClassification(self):
                '''static QUrl Nepomuk.Vocabulary.NCAL.privateClassification()'''
                return QUrl()
            def priority(self):
                '''static QUrl Nepomuk.Vocabulary.NCAL.priority()'''
                return QUrl()
            def periodEnd(self):
                '''static QUrl Nepomuk.Vocabulary.NCAL.periodEnd()'''
                return QUrl()
            def periodDuration(self):
                '''static QUrl Nepomuk.Vocabulary.NCAL.periodDuration()'''
                return QUrl()
            def periodBegin(self):
                '''static QUrl Nepomuk.Vocabulary.NCAL.periodBegin()'''
                return QUrl()
            def percentComplete(self):
                '''static QUrl Nepomuk.Vocabulary.NCAL.percentComplete()'''
                return QUrl()
            def partstat(self):
                '''static QUrl Nepomuk.Vocabulary.NCAL.partstat()'''
                return QUrl()
            def organizer(self):
                '''static QUrl Nepomuk.Vocabulary.NCAL.organizer()'''
                return QUrl()
            def optParticipantRole(self):
                '''static QUrl Nepomuk.Vocabulary.NCAL.optParticipantRole()'''
                return QUrl()
            def opaqueTransparency(self):
                '''static QUrl Nepomuk.Vocabulary.NCAL.opaqueTransparency()'''
                return QUrl()
            def nonParticipantRole(self):
                '''static QUrl Nepomuk.Vocabulary.NCAL.nonParticipantRole()'''
                return QUrl()
            def needsActionStatus(self):
                '''static QUrl Nepomuk.Vocabulary.NCAL.needsActionStatus()'''
                return QUrl()
            def needsActionParticipationStatus(self):
                '''static QUrl Nepomuk.Vocabulary.NCAL.needsActionParticipationStatus()'''
                return QUrl()
            def ncalTimezone(self):
                '''static QUrl Nepomuk.Vocabulary.NCAL.ncalTimezone()'''
                return QUrl()
            def ncalRelation(self):
                '''static QUrl Nepomuk.Vocabulary.NCAL.ncalRelation()'''
                return QUrl()
            def monthly(self):
                '''static QUrl Nepomuk.Vocabulary.NCAL.monthly()'''
                return QUrl()
            def monday(self):
                '''static QUrl Nepomuk.Vocabulary.NCAL.monday()'''
                return QUrl()
            def minutely(self):
                '''static QUrl Nepomuk.Vocabulary.NCAL.minutely()'''
                return QUrl()
            def method(self):
                '''static QUrl Nepomuk.Vocabulary.NCAL.method()'''
                return QUrl()
            def member(self):
                '''static QUrl Nepomuk.Vocabulary.NCAL.member()'''
                return QUrl()
            def locationAltRep(self):
                '''static QUrl Nepomuk.Vocabulary.NCAL.locationAltRep()'''
                return QUrl()
            def location(self):
                '''static QUrl Nepomuk.Vocabulary.NCAL.location()'''
                return QUrl()
            def lastModified(self):
                '''static QUrl Nepomuk.Vocabulary.NCAL.lastModified()'''
                return QUrl()
            def journalStatus(self):
                '''static QUrl Nepomuk.Vocabulary.NCAL.journalStatus()'''
                return QUrl()
            def involvedContact(self):
                '''static QUrl Nepomuk.Vocabulary.NCAL.involvedContact()'''
                return QUrl()
            def interval(self):
                '''static QUrl Nepomuk.Vocabulary.NCAL.interval()'''
                return QUrl()
            def individualUserType(self):
                '''static QUrl Nepomuk.Vocabulary.NCAL.individualUserType()'''
                return QUrl()
            def inProcessStatus(self):
                '''static QUrl Nepomuk.Vocabulary.NCAL.inProcessStatus()'''
                return QUrl()
            def inProcessParticipationStatus(self):
                '''static QUrl Nepomuk.Vocabulary.NCAL.inProcessParticipationStatus()'''
                return QUrl()
            def hourly(self):
                '''static QUrl Nepomuk.Vocabulary.NCAL.hourly()'''
                return QUrl()
            def hasAlarm(self):
                '''static QUrl Nepomuk.Vocabulary.NCAL.hasAlarm()'''
                return QUrl()
            def groupUserType(self):
                '''static QUrl Nepomuk.Vocabulary.NCAL.groupUserType()'''
                return QUrl()
            def gregorianCalendarScale(self):
                '''static QUrl Nepomuk.Vocabulary.NCAL.gregorianCalendarScale()'''
                return QUrl()
            def geo(self):
                '''static QUrl Nepomuk.Vocabulary.NCAL.geo()'''
                return QUrl()
            def friday(self):
                '''static QUrl Nepomuk.Vocabulary.NCAL.friday()'''
                return QUrl()
            def freq(self):
                '''static QUrl Nepomuk.Vocabulary.NCAL.freq()'''
                return QUrl()
            def freebusy(self):
                '''static QUrl Nepomuk.Vocabulary.NCAL.freebusy()'''
                return QUrl()
            def freeFreebusyType(self):
                '''static QUrl Nepomuk.Vocabulary.NCAL.freeFreebusyType()'''
                return QUrl()
            def fmttype(self):
                '''static QUrl Nepomuk.Vocabulary.NCAL.fmttype()'''
                return QUrl()
            def finalStatus(self):
                '''static QUrl Nepomuk.Vocabulary.NCAL.finalStatus()'''
                return QUrl()
            def fbtype(self):
                '''static QUrl Nepomuk.Vocabulary.NCAL.fbtype()'''
                return QUrl()
            def exrule(self):
                '''static QUrl Nepomuk.Vocabulary.NCAL.exrule()'''
                return QUrl()
            def exdate(self):
                '''static QUrl Nepomuk.Vocabulary.NCAL.exdate()'''
                return QUrl()
            def eventStatus(self):
                '''static QUrl Nepomuk.Vocabulary.NCAL.eventStatus()'''
                return QUrl()
            def endTriggerRelation(self):
                '''static QUrl Nepomuk.Vocabulary.NCAL.endTriggerRelation()'''
                return QUrl()
            def encoding(self):
                '''static QUrl Nepomuk.Vocabulary.NCAL.encoding()'''
                return QUrl()
            def emailAction(self):
                '''static QUrl Nepomuk.Vocabulary.NCAL.emailAction()'''
                return QUrl()
            def duration(self):
                '''static QUrl Nepomuk.Vocabulary.NCAL.duration()'''
                return QUrl()
            def due(self):
                '''static QUrl Nepomuk.Vocabulary.NCAL.due()'''
                return QUrl()
            def dtstart(self):
                '''static QUrl Nepomuk.Vocabulary.NCAL.dtstart()'''
                return QUrl()
            def dtstamp(self):
                '''static QUrl Nepomuk.Vocabulary.NCAL.dtstamp()'''
                return QUrl()
            def dtend(self):
                '''static QUrl Nepomuk.Vocabulary.NCAL.dtend()'''
                return QUrl()
            def draftStatus(self):
                '''static QUrl Nepomuk.Vocabulary.NCAL.draftStatus()'''
                return QUrl()
            def displayAction(self):
                '''static QUrl Nepomuk.Vocabulary.NCAL.displayAction()'''
                return QUrl()
            def dir(self):
                '''static QUrl Nepomuk.Vocabulary.NCAL.dir()'''
                return QUrl()
            def descriptionAltRep(self):
                '''static QUrl Nepomuk.Vocabulary.NCAL.descriptionAltRep()'''
                return QUrl()
            def description(self):
                '''static QUrl Nepomuk.Vocabulary.NCAL.description()'''
                return QUrl()
            def delegatedTo(self):
                '''static QUrl Nepomuk.Vocabulary.NCAL.delegatedTo()'''
                return QUrl()
            def delegatedParticipationStatus(self):
                '''static QUrl Nepomuk.Vocabulary.NCAL.delegatedParticipationStatus()'''
                return QUrl()
            def delegatedFrom(self):
                '''static QUrl Nepomuk.Vocabulary.NCAL.delegatedFrom()'''
                return QUrl()
            def declinedParticipationStatus(self):
                '''static QUrl Nepomuk.Vocabulary.NCAL.declinedParticipationStatus()'''
                return QUrl()
            def daylight(self):
                '''static QUrl Nepomuk.Vocabulary.NCAL.daylight()'''
                return QUrl()
            def dateTime(self):
                '''static QUrl Nepomuk.Vocabulary.NCAL.dateTime()'''
                return QUrl()
            def date(self):
                '''static QUrl Nepomuk.Vocabulary.NCAL.date()'''
                return QUrl()
            def daily(self):
                '''static QUrl Nepomuk.Vocabulary.NCAL.daily()'''
                return QUrl()
            def cutype(self):
                '''static QUrl Nepomuk.Vocabulary.NCAL.cutype()'''
                return QUrl()
            def created(self):
                '''static QUrl Nepomuk.Vocabulary.NCAL.created()'''
                return QUrl()
            def count(self):
                '''static QUrl Nepomuk.Vocabulary.NCAL.count()'''
                return QUrl()
            def contactAltRep(self):
                '''static QUrl Nepomuk.Vocabulary.NCAL.contactAltRep()'''
                return QUrl()
            def contact(self):
                '''static QUrl Nepomuk.Vocabulary.NCAL.contact()'''
                return QUrl()
            def confirmedStatus(self):
                '''static QUrl Nepomuk.Vocabulary.NCAL.confirmedStatus()'''
                return QUrl()
            def confidentialClassification(self):
                '''static QUrl Nepomuk.Vocabulary.NCAL.confidentialClassification()'''
                return QUrl()
            def component(self):
                '''static QUrl Nepomuk.Vocabulary.NCAL.component()'''
                return QUrl()
            def completedStatus(self):
                '''static QUrl Nepomuk.Vocabulary.NCAL.completedStatus()'''
                return QUrl()
            def completedParticipationStatus(self):
                '''static QUrl Nepomuk.Vocabulary.NCAL.completedParticipationStatus()'''
                return QUrl()
            def completed(self):
                '''static QUrl Nepomuk.Vocabulary.NCAL.completed()'''
                return QUrl()
            def commentAltRep(self):
                '''static QUrl Nepomuk.Vocabulary.NCAL.commentAltRep()'''
                return QUrl()
            def comment(self):
                '''static QUrl Nepomuk.Vocabulary.NCAL.comment()'''
                return QUrl()
            def ncalClass(self):
                '''static QUrl Nepomuk.Vocabulary.NCAL.ncalClass()'''
                return QUrl()
            def chairRole(self):
                '''static QUrl Nepomuk.Vocabulary.NCAL.chairRole()'''
                return QUrl()
            def categories(self):
                '''static QUrl Nepomuk.Vocabulary.NCAL.categories()'''
                return QUrl()
            def cancelledTodoStatus(self):
                '''static QUrl Nepomuk.Vocabulary.NCAL.cancelledTodoStatus()'''
                return QUrl()
            def cancelledJournalStatus(self):
                '''static QUrl Nepomuk.Vocabulary.NCAL.cancelledJournalStatus()'''
                return QUrl()
            def cancelledEventStatus(self):
                '''static QUrl Nepomuk.Vocabulary.NCAL.cancelledEventStatus()'''
                return QUrl()
            def calscale(self):
                '''static QUrl Nepomuk.Vocabulary.NCAL.calscale()'''
                return QUrl()
            def byyearday(self):
                '''static QUrl Nepomuk.Vocabulary.NCAL.byyearday()'''
                return QUrl()
            def byweekno(self):
                '''static QUrl Nepomuk.Vocabulary.NCAL.byweekno()'''
                return QUrl()
            def bysetpos(self):
                '''static QUrl Nepomuk.Vocabulary.NCAL.bysetpos()'''
                return QUrl()
            def bysecond(self):
                '''static QUrl Nepomuk.Vocabulary.NCAL.bysecond()'''
                return QUrl()
            def bymonthday(self):
                '''static QUrl Nepomuk.Vocabulary.NCAL.bymonthday()'''
                return QUrl()
            def bymonth(self):
                '''static QUrl Nepomuk.Vocabulary.NCAL.bymonth()'''
                return QUrl()
            def byminute(self):
                '''static QUrl Nepomuk.Vocabulary.NCAL.byminute()'''
                return QUrl()
            def byhour(self):
                '''static QUrl Nepomuk.Vocabulary.NCAL.byhour()'''
                return QUrl()
            def bydayWeekday(self):
                '''static QUrl Nepomuk.Vocabulary.NCAL.bydayWeekday()'''
                return QUrl()
            def bydayModifier(self):
                '''static QUrl Nepomuk.Vocabulary.NCAL.bydayModifier()'''
                return QUrl()
            def byday(self):
                '''static QUrl Nepomuk.Vocabulary.NCAL.byday()'''
                return QUrl()
            def busyUnavailableFreebusyType(self):
                '''static QUrl Nepomuk.Vocabulary.NCAL.busyUnavailableFreebusyType()'''
                return QUrl()
            def busyTentativeFreebusyType(self):
                '''static QUrl Nepomuk.Vocabulary.NCAL.busyTentativeFreebusyType()'''
                return QUrl()
            def busyFreebusyType(self):
                '''static QUrl Nepomuk.Vocabulary.NCAL.busyFreebusyType()'''
                return QUrl()
            def base64Encoding(self):
                '''static QUrl Nepomuk.Vocabulary.NCAL.base64Encoding()'''
                return QUrl()
            def audioAction(self):
                '''static QUrl Nepomuk.Vocabulary.NCAL.audioAction()'''
                return QUrl()
            def attendee(self):
                '''static QUrl Nepomuk.Vocabulary.NCAL.attendee()'''
                return QUrl()
            def attachmentUri(self):
                '''static QUrl Nepomuk.Vocabulary.NCAL.attachmentUri()'''
                return QUrl()
            def attachmentContent(self):
                '''static QUrl Nepomuk.Vocabulary.NCAL.attachmentContent()'''
                return QUrl()
            def attach(self):
                '''static QUrl Nepomuk.Vocabulary.NCAL.attach()'''
                return QUrl()
            def action(self):
                '''static QUrl Nepomuk.Vocabulary.NCAL.action()'''
                return QUrl()
            def acceptedParticipationStatus(self):
                '''static QUrl Nepomuk.Vocabulary.NCAL.acceptedParticipationStatus()'''
                return QUrl()
            def _8bitEncoding(self):
                '''static QUrl Nepomuk.Vocabulary.NCAL._8bitEncoding()'''
                return QUrl()
            def Weekday(self):
                '''static QUrl Nepomuk.Vocabulary.NCAL.Weekday()'''
                return QUrl()
            def UnionParentClass(self):
                '''static QUrl Nepomuk.Vocabulary.NCAL.UnionParentClass()'''
                return QUrl()
            def UnionOfTimezoneObservanceEventJournalTimezoneTodo(self):
                '''static QUrl Nepomuk.Vocabulary.NCAL.UnionOfTimezoneObservanceEventJournalTimezoneTodo()'''
                return QUrl()
            def UnionOfTimezoneObservanceEventFreebusyTimezoneTodo(self):
                '''static QUrl Nepomuk.Vocabulary.NCAL.UnionOfTimezoneObservanceEventFreebusyTimezoneTodo()'''
                return QUrl()
            def UnionOfTimezoneObservanceEventFreebusyJournalTimezoneTodo(self):
                '''static QUrl Nepomuk.Vocabulary.NCAL.UnionOfTimezoneObservanceEventFreebusyJournalTimezoneTodo()'''
                return QUrl()
            def UnionOfEventTodo(self):
                '''static QUrl Nepomuk.Vocabulary.NCAL.UnionOfEventTodo()'''
                return QUrl()
            def UnionOfEventJournalTodo(self):
                '''static QUrl Nepomuk.Vocabulary.NCAL.UnionOfEventJournalTodo()'''
                return QUrl()
            def UnionOfEventJournalTimezoneTodo(self):
                '''static QUrl Nepomuk.Vocabulary.NCAL.UnionOfEventJournalTimezoneTodo()'''
                return QUrl()
            def UnionOfEventFreebusyJournalTodo(self):
                '''static QUrl Nepomuk.Vocabulary.NCAL.UnionOfEventFreebusyJournalTodo()'''
                return QUrl()
            def UnionOfEventFreebusy(self):
                '''static QUrl Nepomuk.Vocabulary.NCAL.UnionOfEventFreebusy()'''
                return QUrl()
            def UnionOfAlarmEventTodo(self):
                '''static QUrl Nepomuk.Vocabulary.NCAL.UnionOfAlarmEventTodo()'''
                return QUrl()
            def UnionOfAlarmEventJournalTodo(self):
                '''static QUrl Nepomuk.Vocabulary.NCAL.UnionOfAlarmEventJournalTodo()'''
                return QUrl()
            def UnionOfAlarmEventFreebusyTodo(self):
                '''static QUrl Nepomuk.Vocabulary.NCAL.UnionOfAlarmEventFreebusyTodo()'''
                return QUrl()
            def UnionOfAlarmEventFreebusyJournalTodo(self):
                '''static QUrl Nepomuk.Vocabulary.NCAL.UnionOfAlarmEventFreebusyJournalTodo()'''
                return QUrl()
            def TriggerRelation(self):
                '''static QUrl Nepomuk.Vocabulary.NCAL.TriggerRelation()'''
                return QUrl()
            def Trigger(self):
                '''static QUrl Nepomuk.Vocabulary.NCAL.Trigger()'''
                return QUrl()
            def TodoStatus(self):
                '''static QUrl Nepomuk.Vocabulary.NCAL.TodoStatus()'''
                return QUrl()
            def Todo(self):
                '''static QUrl Nepomuk.Vocabulary.NCAL.Todo()'''
                return QUrl()
            def TimezoneObservance(self):
                '''static QUrl Nepomuk.Vocabulary.NCAL.TimezoneObservance()'''
                return QUrl()
            def Timezone(self):
                '''static QUrl Nepomuk.Vocabulary.NCAL.Timezone()'''
                return QUrl()
            def TimeTransparency(self):
                '''static QUrl Nepomuk.Vocabulary.NCAL.TimeTransparency()'''
                return QUrl()
            def RequestStatus(self):
                '''static QUrl Nepomuk.Vocabulary.NCAL.RequestStatus()'''
                return QUrl()
            def RecurrenceRule(self):
                '''static QUrl Nepomuk.Vocabulary.NCAL.RecurrenceRule()'''
                return QUrl()
            def RecurrenceIdentifierRange(self):
                '''static QUrl Nepomuk.Vocabulary.NCAL.RecurrenceIdentifierRange()'''
                return QUrl()
            def RecurrenceIdentifier(self):
                '''static QUrl Nepomuk.Vocabulary.NCAL.RecurrenceIdentifier()'''
                return QUrl()
            def RecurrenceFrequency(self):
                '''static QUrl Nepomuk.Vocabulary.NCAL.RecurrenceFrequency()'''
                return QUrl()
            def ParticipationStatus(self):
                '''static QUrl Nepomuk.Vocabulary.NCAL.ParticipationStatus()'''
                return QUrl()
            def Organizer(self):
                '''static QUrl Nepomuk.Vocabulary.NCAL.Organizer()'''
                return QUrl()
            def NcalTimeEntity(self):
                '''static QUrl Nepomuk.Vocabulary.NCAL.NcalTimeEntity()'''
                return QUrl()
            def NcalPeriod(self):
                '''static QUrl Nepomuk.Vocabulary.NCAL.NcalPeriod()'''
                return QUrl()
            def NcalDateTime(self):
                '''static QUrl Nepomuk.Vocabulary.NCAL.NcalDateTime()'''
                return QUrl()
            def JournalStatus(self):
                '''static QUrl Nepomuk.Vocabulary.NCAL.JournalStatus()'''
                return QUrl()
            def Journal(self):
                '''static QUrl Nepomuk.Vocabulary.NCAL.Journal()'''
                return QUrl()
            def FreebusyType(self):
                '''static QUrl Nepomuk.Vocabulary.NCAL.FreebusyType()'''
                return QUrl()
            def FreebusyPeriod(self):
                '''static QUrl Nepomuk.Vocabulary.NCAL.FreebusyPeriod()'''
                return QUrl()
            def Freebusy(self):
                '''static QUrl Nepomuk.Vocabulary.NCAL.Freebusy()'''
                return QUrl()
            def EventStatus(self):
                '''static QUrl Nepomuk.Vocabulary.NCAL.EventStatus()'''
                return QUrl()
            def Event(self):
                '''static QUrl Nepomuk.Vocabulary.NCAL.Event()'''
                return QUrl()
            def CalendarUserType(self):
                '''static QUrl Nepomuk.Vocabulary.NCAL.CalendarUserType()'''
                return QUrl()
            def CalendarScale(self):
                '''static QUrl Nepomuk.Vocabulary.NCAL.CalendarScale()'''
                return QUrl()
            def CalendarDataObject(self):
                '''static QUrl Nepomuk.Vocabulary.NCAL.CalendarDataObject()'''
                return QUrl()
            def Calendar(self):
                '''static QUrl Nepomuk.Vocabulary.NCAL.Calendar()'''
                return QUrl()
            def BydayRulePart(self):
                '''static QUrl Nepomuk.Vocabulary.NCAL.BydayRulePart()'''
                return QUrl()
            def AttendeeRole(self):
                '''static QUrl Nepomuk.Vocabulary.NCAL.AttendeeRole()'''
                return QUrl()
            def AttendeeOrOrganizer(self):
                '''static QUrl Nepomuk.Vocabulary.NCAL.AttendeeOrOrganizer()'''
                return QUrl()
            def Attendee(self):
                '''static QUrl Nepomuk.Vocabulary.NCAL.Attendee()'''
                return QUrl()
            def AttachmentEncoding(self):
                '''static QUrl Nepomuk.Vocabulary.NCAL.AttachmentEncoding()'''
                return QUrl()
            def Attachment(self):
                '''static QUrl Nepomuk.Vocabulary.NCAL.Attachment()'''
                return QUrl()
            def AlarmAction(self):
                '''static QUrl Nepomuk.Vocabulary.NCAL.AlarmAction()'''
                return QUrl()
            def Alarm(self):
                '''static QUrl Nepomuk.Vocabulary.NCAL.Alarm()'''
                return QUrl()
            def AccessClassification(self):
                '''static QUrl Nepomuk.Vocabulary.NCAL.AccessClassification()'''
                return QUrl()
            def nrlOntologyGraph(self):
                '''static QUrl Nepomuk.Vocabulary.NCAL.nrlOntologyGraph()'''
                return QUrl()
            def ncalNamespace(self):
                '''static QUrl Nepomuk.Vocabulary.NCAL.ncalNamespace()'''
                return QUrl()
    class Vocabulary():
        """"""
        class NCO():
            """"""
            def requestedPresenceSubscriptionTo(self):
                '''static QUrl Nepomuk.Vocabulary.NCO.requestedPresenceSubscriptionTo()'''
                return QUrl()
            def publishesPresenceTo(self):
                '''static QUrl Nepomuk.Vocabulary.NCO.publishesPresenceTo()'''
                return QUrl()
            def isBlocked(self):
                '''static QUrl Nepomuk.Vocabulary.NCO.isBlocked()'''
                return QUrl()
            def isAccessedBy(self):
                '''static QUrl Nepomuk.Vocabulary.NCO.isAccessedBy()'''
                return QUrl()
            def imStatusType(self):
                '''static QUrl Nepomuk.Vocabulary.NCO.imStatusType()'''
                return QUrl()
            def imCapabilityVideo(self):
                '''static QUrl Nepomuk.Vocabulary.NCO.imCapabilityVideo()'''
                return QUrl()
            def imCapabilityText(self):
                '''static QUrl Nepomuk.Vocabulary.NCO.imCapabilityText()'''
                return QUrl()
            def imCapabilityAudio(self):
                '''static QUrl Nepomuk.Vocabulary.NCO.imCapabilityAudio()'''
                return QUrl()
            def hasIMCapability(self):
                '''static QUrl Nepomuk.Vocabulary.NCO.hasIMCapability()'''
                return QUrl()
            def IMStatusTypeUnknown(self):
                '''static QUrl Nepomuk.Vocabulary.NCO.IMStatusTypeUnknown()'''
                return QUrl()
            def IMStatusTypeOffline(self):
                '''static QUrl Nepomuk.Vocabulary.NCO.IMStatusTypeOffline()'''
                return QUrl()
            def IMStatusTypeHidden(self):
                '''static QUrl Nepomuk.Vocabulary.NCO.IMStatusTypeHidden()'''
                return QUrl()
            def IMStatusTypeExtendedAway(self):
                '''static QUrl Nepomuk.Vocabulary.NCO.IMStatusTypeExtendedAway()'''
                return QUrl()
            def IMStatusTypeBusy(self):
                '''static QUrl Nepomuk.Vocabulary.NCO.IMStatusTypeBusy()'''
                return QUrl()
            def IMStatusTypeAway(self):
                '''static QUrl Nepomuk.Vocabulary.NCO.IMStatusTypeAway()'''
                return QUrl()
            def IMStatusTypeAvailable(self):
                '''static QUrl Nepomuk.Vocabulary.NCO.IMStatusTypeAvailable()'''
                return QUrl()
            def IMStatusType(self):
                '''static QUrl Nepomuk.Vocabulary.NCO.IMStatusType()'''
                return QUrl()
            def IMCapability(self):
                '''static QUrl Nepomuk.Vocabulary.NCO.IMCapability()'''
                return QUrl()
            def websiteUrl(self):
                '''static QUrl Nepomuk.Vocabulary.NCO.websiteUrl()'''
                return QUrl()
            def voiceMail(self):
                '''static QUrl Nepomuk.Vocabulary.NCO.voiceMail()'''
                return QUrl()
            def url(self):
                '''static QUrl Nepomuk.Vocabulary.NCO.url()'''
                return QUrl()
            def title(self):
                '''static QUrl Nepomuk.Vocabulary.NCO.title()'''
                return QUrl()
            def streetAddress(self):
                '''static QUrl Nepomuk.Vocabulary.NCO.streetAddress()'''
                return QUrl()
            def start(self):
                '''static QUrl Nepomuk.Vocabulary.NCO.start()'''
                return QUrl()
            def sound(self):
                '''static QUrl Nepomuk.Vocabulary.NCO.sound()'''
                return QUrl()
            def role(self):
                '''static QUrl Nepomuk.Vocabulary.NCO.role()'''
                return QUrl()
            def representative(self):
                '''static QUrl Nepomuk.Vocabulary.NCO.representative()'''
                return QUrl()
            def region(self):
                '''static QUrl Nepomuk.Vocabulary.NCO.region()'''
                return QUrl()
            def publisher(self):
                '''static QUrl Nepomuk.Vocabulary.NCO.publisher()'''
                return QUrl()
            def postalcode(self):
                '''static QUrl Nepomuk.Vocabulary.NCO.postalcode()'''
                return QUrl()
            def pobox(self):
                '''static QUrl Nepomuk.Vocabulary.NCO.pobox()'''
                return QUrl()
            def photo(self):
                '''static QUrl Nepomuk.Vocabulary.NCO.photo()'''
                return QUrl()
            def phoneNumber(self):
                '''static QUrl Nepomuk.Vocabulary.NCO.phoneNumber()'''
                return QUrl()
            def org(self):
                '''static QUrl Nepomuk.Vocabulary.NCO.org()'''
                return QUrl()
            def note(self):
                '''static QUrl Nepomuk.Vocabulary.NCO.note()'''
                return QUrl()
            def nickname(self):
                '''static QUrl Nepomuk.Vocabulary.NCO.nickname()'''
                return QUrl()
            def nameHonorificSuffix(self):
                '''static QUrl Nepomuk.Vocabulary.NCO.nameHonorificSuffix()'''
                return QUrl()
            def nameHonorificPrefix(self):
                '''static QUrl Nepomuk.Vocabulary.NCO.nameHonorificPrefix()'''
                return QUrl()
            def nameGiven(self):
                '''static QUrl Nepomuk.Vocabulary.NCO.nameGiven()'''
                return QUrl()
            def nameFamily(self):
                '''static QUrl Nepomuk.Vocabulary.NCO.nameFamily()'''
                return QUrl()
            def nameAdditional(self):
                '''static QUrl Nepomuk.Vocabulary.NCO.nameAdditional()'''
                return QUrl()
            def male(self):
                '''static QUrl Nepomuk.Vocabulary.NCO.male()'''
                return QUrl()
            def logo(self):
                '''static QUrl Nepomuk.Vocabulary.NCO.logo()'''
                return QUrl()
            def locality(self):
                '''static QUrl Nepomuk.Vocabulary.NCO.locality()'''
                return QUrl()
            def key(self):
                '''static QUrl Nepomuk.Vocabulary.NCO.key()'''
                return QUrl()
            def imStatusMessage(self):
                '''static QUrl Nepomuk.Vocabulary.NCO.imStatusMessage()'''
                return QUrl()
            def imStatus(self):
                '''static QUrl Nepomuk.Vocabulary.NCO.imStatus()'''
                return QUrl()
            def imNickname(self):
                '''static QUrl Nepomuk.Vocabulary.NCO.imNickname()'''
                return QUrl()
            def imID(self):
                '''static QUrl Nepomuk.Vocabulary.NCO.imID()'''
                return QUrl()
            def imAccountType(self):
                '''static QUrl Nepomuk.Vocabulary.NCO.imAccountType()'''
                return QUrl()
            def hobby(self):
                '''static QUrl Nepomuk.Vocabulary.NCO.hobby()'''
                return QUrl()
            def hasPostalAddress(self):
                '''static QUrl Nepomuk.Vocabulary.NCO.hasPostalAddress()'''
                return QUrl()
            def hasPhoneNumber(self):
                '''static QUrl Nepomuk.Vocabulary.NCO.hasPhoneNumber()'''
                return QUrl()
            def hasLocation(self):
                '''static QUrl Nepomuk.Vocabulary.NCO.hasLocation()'''
                return QUrl()
            def hasIMAccount(self):
                '''static QUrl Nepomuk.Vocabulary.NCO.hasIMAccount()'''
                return QUrl()
            def hasEmailAddress(self):
                '''static QUrl Nepomuk.Vocabulary.NCO.hasEmailAddress()'''
                return QUrl()
            def hasContactMedium(self):
                '''static QUrl Nepomuk.Vocabulary.NCO.hasContactMedium()'''
                return QUrl()
            def hasAffiliation(self):
                '''static QUrl Nepomuk.Vocabulary.NCO.hasAffiliation()'''
                return QUrl()
            def gender(self):
                '''static QUrl Nepomuk.Vocabulary.NCO.gender()'''
                return QUrl()
            def fullname(self):
                '''static QUrl Nepomuk.Vocabulary.NCO.fullname()'''
                return QUrl()
            def foafUrl(self):
                '''static QUrl Nepomuk.Vocabulary.NCO.foafUrl()'''
                return QUrl()
            def female(self):
                '''static QUrl Nepomuk.Vocabulary.NCO.female()'''
                return QUrl()
            def extendedAddress(self):
                '''static QUrl Nepomuk.Vocabulary.NCO.extendedAddress()'''
                return QUrl()
            def end(self):
                '''static QUrl Nepomuk.Vocabulary.NCO.end()'''
                return QUrl()
            def emailAddress(self):
                '''static QUrl Nepomuk.Vocabulary.NCO.emailAddress()'''
                return QUrl()
            def department(self):
                '''static QUrl Nepomuk.Vocabulary.NCO.department()'''
                return QUrl()
            def creator(self):
                '''static QUrl Nepomuk.Vocabulary.NCO.creator()'''
                return QUrl()
            def country(self):
                '''static QUrl Nepomuk.Vocabulary.NCO.country()'''
                return QUrl()
            def contributor(self):
                '''static QUrl Nepomuk.Vocabulary.NCO.contributor()'''
                return QUrl()
            def containsContact(self):
                '''static QUrl Nepomuk.Vocabulary.NCO.containsContact()'''
                return QUrl()
            def contactUID(self):
                '''static QUrl Nepomuk.Vocabulary.NCO.contactUID()'''
                return QUrl()
            def contactMediumComment(self):
                '''static QUrl Nepomuk.Vocabulary.NCO.contactMediumComment()'''
                return QUrl()
            def contactGroupName(self):
                '''static QUrl Nepomuk.Vocabulary.NCO.contactGroupName()'''
                return QUrl()
            def blogUrl(self):
                '''static QUrl Nepomuk.Vocabulary.NCO.blogUrl()'''
                return QUrl()
            def birthDate(self):
                '''static QUrl Nepomuk.Vocabulary.NCO.birthDate()'''
                return QUrl()
            def belongsToGroup(self):
                '''static QUrl Nepomuk.Vocabulary.NCO.belongsToGroup()'''
                return QUrl()
            def addressLocation(self):
                '''static QUrl Nepomuk.Vocabulary.NCO.addressLocation()'''
                return QUrl()
            def VoicePhoneNumber(self):
                '''static QUrl Nepomuk.Vocabulary.NCO.VoicePhoneNumber()'''
                return QUrl()
            def VideoTelephoneNumber(self):
                '''static QUrl Nepomuk.Vocabulary.NCO.VideoTelephoneNumber()'''
                return QUrl()
            def VideoIMAccount(self):
                '''static QUrl Nepomuk.Vocabulary.NCO.VideoIMAccount()'''
                return QUrl()
            def Role(self):
                '''static QUrl Nepomuk.Vocabulary.NCO.Role()'''
                return QUrl()
            def PostalAddress(self):
                '''static QUrl Nepomuk.Vocabulary.NCO.PostalAddress()'''
                return QUrl()
            def PhoneNumber(self):
                '''static QUrl Nepomuk.Vocabulary.NCO.PhoneNumber()'''
                return QUrl()
            def PersonContact(self):
                '''static QUrl Nepomuk.Vocabulary.NCO.PersonContact()'''
                return QUrl()
            def PcsNumber(self):
                '''static QUrl Nepomuk.Vocabulary.NCO.PcsNumber()'''
                return QUrl()
            def ParcelDeliveryAddress(self):
                '''static QUrl Nepomuk.Vocabulary.NCO.ParcelDeliveryAddress()'''
                return QUrl()
            def PagerNumber(self):
                '''static QUrl Nepomuk.Vocabulary.NCO.PagerNumber()'''
                return QUrl()
            def OrganizationContact(self):
                '''static QUrl Nepomuk.Vocabulary.NCO.OrganizationContact()'''
                return QUrl()
            def ModemNumber(self):
                '''static QUrl Nepomuk.Vocabulary.NCO.ModemNumber()'''
                return QUrl()
            def MessagingNumber(self):
                '''static QUrl Nepomuk.Vocabulary.NCO.MessagingNumber()'''
                return QUrl()
            def IsdnNumber(self):
                '''static QUrl Nepomuk.Vocabulary.NCO.IsdnNumber()'''
                return QUrl()
            def InternationalDeliveryAddress(self):
                '''static QUrl Nepomuk.Vocabulary.NCO.InternationalDeliveryAddress()'''
                return QUrl()
            def IMAccount(self):
                '''static QUrl Nepomuk.Vocabulary.NCO.IMAccount()'''
                return QUrl()
            def Gender(self):
                '''static QUrl Nepomuk.Vocabulary.NCO.Gender()'''
                return QUrl()
            def FaxNumber(self):
                '''static QUrl Nepomuk.Vocabulary.NCO.FaxNumber()'''
                return QUrl()
            def EmailAddress(self):
                '''static QUrl Nepomuk.Vocabulary.NCO.EmailAddress()'''
                return QUrl()
            def DomesticDeliveryAddress(self):
                '''static QUrl Nepomuk.Vocabulary.NCO.DomesticDeliveryAddress()'''
                return QUrl()
            def ContactMedium(self):
                '''static QUrl Nepomuk.Vocabulary.NCO.ContactMedium()'''
                return QUrl()
            def ContactListDataObject(self):
                '''static QUrl Nepomuk.Vocabulary.NCO.ContactListDataObject()'''
                return QUrl()
            def ContactList(self):
                '''static QUrl Nepomuk.Vocabulary.NCO.ContactList()'''
                return QUrl()
            def ContactGroup(self):
                '''static QUrl Nepomuk.Vocabulary.NCO.ContactGroup()'''
                return QUrl()
            def Contact(self):
                '''static QUrl Nepomuk.Vocabulary.NCO.Contact()'''
                return QUrl()
            def CellPhoneNumber(self):
                '''static QUrl Nepomuk.Vocabulary.NCO.CellPhoneNumber()'''
                return QUrl()
            def CarPhoneNumber(self):
                '''static QUrl Nepomuk.Vocabulary.NCO.CarPhoneNumber()'''
                return QUrl()
            def BbsNumber(self):
                '''static QUrl Nepomuk.Vocabulary.NCO.BbsNumber()'''
                return QUrl()
            def AudioIMAccount(self):
                '''static QUrl Nepomuk.Vocabulary.NCO.AudioIMAccount()'''
                return QUrl()
            def Affiliation(self):
                '''static QUrl Nepomuk.Vocabulary.NCO.Affiliation()'''
                return QUrl()
            def nrlOntologyGraph(self):
                '''static QUrl Nepomuk.Vocabulary.NCO.nrlOntologyGraph()'''
                return QUrl()
            def ncoNamespace(self):
                '''static QUrl Nepomuk.Vocabulary.NCO.ncoNamespace()'''
                return QUrl()
    class Query():
        """"""
        class DateRangeFlags():
            """"""
            def __init__(self):
                '''Nepomuk.Query.DateRangeFlags Nepomuk.Query.DateRangeFlags.__init__()'''
                return Nepomuk.Query.DateRangeFlags()
            def __init__(self):
                '''int Nepomuk.Query.DateRangeFlags.__init__()'''
                return int()
            def __init__(self):
                '''void Nepomuk.Query.DateRangeFlags.__init__()'''
            def __bool__(self):
                '''int Nepomuk.Query.DateRangeFlags.__bool__()'''
                return int()
            def __ne__(self, f):
                '''bool Nepomuk.Query.DateRangeFlags.__ne__(Nepomuk.Query.DateRangeFlags f)'''
                return bool()
            def __eq__(self, f):
                '''bool Nepomuk.Query.DateRangeFlags.__eq__(Nepomuk.Query.DateRangeFlags f)'''
                return bool()
            def __invert__(self):
                '''Nepomuk.Query.DateRangeFlags Nepomuk.Query.DateRangeFlags.__invert__()'''
                return Nepomuk.Query.DateRangeFlags()
            def __and__(self, mask):
                '''Nepomuk.Query.DateRangeFlags Nepomuk.Query.DateRangeFlags.__and__(int mask)'''
                return Nepomuk.Query.DateRangeFlags()
            def __xor__(self, f):
                '''Nepomuk.Query.DateRangeFlags Nepomuk.Query.DateRangeFlags.__xor__(Nepomuk.Query.DateRangeFlags f)'''
                return Nepomuk.Query.DateRangeFlags()
            def __xor__(self, f):
                '''Nepomuk.Query.DateRangeFlags Nepomuk.Query.DateRangeFlags.__xor__(int f)'''
                return Nepomuk.Query.DateRangeFlags()
            def __or__(self, f):
                '''Nepomuk.Query.DateRangeFlags Nepomuk.Query.DateRangeFlags.__or__(Nepomuk.Query.DateRangeFlags f)'''
                return Nepomuk.Query.DateRangeFlags()
            def __or__(self, f):
                '''Nepomuk.Query.DateRangeFlags Nepomuk.Query.DateRangeFlags.__or__(int f)'''
                return Nepomuk.Query.DateRangeFlags()
            def __int__(self):
                '''int Nepomuk.Query.DateRangeFlags.__int__()'''
                return int()
            def __ixor__(self, f):
                '''Nepomuk.Query.DateRangeFlags Nepomuk.Query.DateRangeFlags.__ixor__(Nepomuk.Query.DateRangeFlags f)'''
                return Nepomuk.Query.DateRangeFlags()
            def __ior__(self, f):
                '''Nepomuk.Query.DateRangeFlags Nepomuk.Query.DateRangeFlags.__ior__(Nepomuk.Query.DateRangeFlags f)'''
                return Nepomuk.Query.DateRangeFlags()
            def __iand__(self, mask):
                '''Nepomuk.Query.DateRangeFlags Nepomuk.Query.DateRangeFlags.__iand__(int mask)'''
                return Nepomuk.Query.DateRangeFlags()
    class TagWidget():
        """"""
        class ModeFlags():
            """"""
            def __init__(self):
                '''Nepomuk.TagWidget.ModeFlags Nepomuk.TagWidget.ModeFlags.__init__()'''
                return Nepomuk.TagWidget.ModeFlags()
            def __init__(self):
                '''int Nepomuk.TagWidget.ModeFlags.__init__()'''
                return int()
            def __init__(self):
                '''void Nepomuk.TagWidget.ModeFlags.__init__()'''
            def __bool__(self):
                '''int Nepomuk.TagWidget.ModeFlags.__bool__()'''
                return int()
            def __ne__(self, f):
                '''bool Nepomuk.TagWidget.ModeFlags.__ne__(Nepomuk.TagWidget.ModeFlags f)'''
                return bool()
            def __eq__(self, f):
                '''bool Nepomuk.TagWidget.ModeFlags.__eq__(Nepomuk.TagWidget.ModeFlags f)'''
                return bool()
            def __invert__(self):
                '''Nepomuk.TagWidget.ModeFlags Nepomuk.TagWidget.ModeFlags.__invert__()'''
                return Nepomuk.TagWidget.ModeFlags()
            def __and__(self, mask):
                '''Nepomuk.TagWidget.ModeFlags Nepomuk.TagWidget.ModeFlags.__and__(int mask)'''
                return Nepomuk.TagWidget.ModeFlags()
            def __xor__(self, f):
                '''Nepomuk.TagWidget.ModeFlags Nepomuk.TagWidget.ModeFlags.__xor__(Nepomuk.TagWidget.ModeFlags f)'''
                return Nepomuk.TagWidget.ModeFlags()
            def __xor__(self, f):
                '''Nepomuk.TagWidget.ModeFlags Nepomuk.TagWidget.ModeFlags.__xor__(int f)'''
                return Nepomuk.TagWidget.ModeFlags()
            def __or__(self, f):
                '''Nepomuk.TagWidget.ModeFlags Nepomuk.TagWidget.ModeFlags.__or__(Nepomuk.TagWidget.ModeFlags f)'''
                return Nepomuk.TagWidget.ModeFlags()
            def __or__(self, f):
                '''Nepomuk.TagWidget.ModeFlags Nepomuk.TagWidget.ModeFlags.__or__(int f)'''
                return Nepomuk.TagWidget.ModeFlags()
            def __int__(self):
                '''int Nepomuk.TagWidget.ModeFlags.__int__()'''
                return int()
            def __ixor__(self, f):
                '''Nepomuk.TagWidget.ModeFlags Nepomuk.TagWidget.ModeFlags.__ixor__(Nepomuk.TagWidget.ModeFlags f)'''
                return Nepomuk.TagWidget.ModeFlags()
            def __ior__(self, f):
                '''Nepomuk.TagWidget.ModeFlags Nepomuk.TagWidget.ModeFlags.__ior__(Nepomuk.TagWidget.ModeFlags f)'''
                return Nepomuk.TagWidget.ModeFlags()
            def __iand__(self, mask):
                '''Nepomuk.TagWidget.ModeFlags Nepomuk.TagWidget.ModeFlags.__iand__(int mask)'''
                return Nepomuk.TagWidget.ModeFlags()
    class Types():
        """"""
        def qHash(self, c):
            '''static int Nepomuk.Types.qHash(Nepomuk.Types.Entity c)'''
            return int()
    class Thing(Nepomuk.Resource):
        """"""
        def __init__(self, uri = QUrl(), pimoType = QUrl()):
            '''void Nepomuk.Thing.__init__(QUrl uri = QUrl(), QUrl pimoType = QUrl())'''
        def __init__(self, uri, pimoType, manager):
            '''void Nepomuk.Thing.__init__(QUrl uri, QUrl pimoType, Nepomuk.ResourceManager manager)'''
        def __init__(self, uriOrName, pimoType = QUrl()):
            '''void Nepomuk.Thing.__init__(QString uriOrName, QUrl pimoType = QUrl())'''
        def __init__(self, uriOrName, pimoType, manager):
            '''void Nepomuk.Thing.__init__(QString uriOrName, QUrl pimoType, Nepomuk.ResourceManager manager)'''
        def __init__(self, other):
            '''void Nepomuk.Thing.__init__(Nepomuk.Thing other)'''
        def __init__(self, other):
            '''void Nepomuk.Thing.__init__(Nepomuk.Resource other)'''
        def addGroundingOccurrence(self, res):
            '''void Nepomuk.Thing.addGroundingOccurrence(Nepomuk.Resource res)'''
        def occurrences(self):
            '''list-of-Nepomuk.Resource Nepomuk.Thing.occurrences()'''
            return [Nepomuk.Resource()]
        def referencingOccurrences(self):
            '''list-of-Nepomuk.Resource Nepomuk.Thing.referencingOccurrences()'''
            return [Nepomuk.Resource()]
        def groundingOccurrences(self):
            '''list-of-Nepomuk.Resource Nepomuk.Thing.groundingOccurrences()'''
            return [Nepomuk.Resource()]
    class Query():
        """"""
        class SimpleTerm(Nepomuk.Query.Term):
            """"""
            def __init__(self, term):
                '''void Nepomuk.Query.SimpleTerm.__init__(Nepomuk.Query.Term term)'''
            def __init__(self):
                '''Nepomuk.Query.SimpleTerm Nepomuk.Query.SimpleTerm.__init__()'''
                return Nepomuk.Query.SimpleTerm()
            def setSubTerm(self, term):
                '''void Nepomuk.Query.SimpleTerm.setSubTerm(Nepomuk.Query.Term term)'''
            def subTerm(self):
                '''Nepomuk.Query.Term Nepomuk.Query.SimpleTerm.subTerm()'''
                return Nepomuk.Query.Term()
    class Query():
        """"""
        class GroupTerm(Nepomuk.Query.Term):
            """"""
            def __init__(self, term):
                '''void Nepomuk.Query.GroupTerm.__init__(Nepomuk.Query.Term term)'''
            def __init__(self):
                '''Nepomuk.Query.GroupTerm Nepomuk.Query.GroupTerm.__init__()'''
                return Nepomuk.Query.GroupTerm()
            def addSubTerm(self, term):
                '''void Nepomuk.Query.GroupTerm.addSubTerm(Nepomuk.Query.Term term)'''
            def setSubTerms(self, terms):
                '''void Nepomuk.Query.GroupTerm.setSubTerms(list-of-Nepomuk.Query.Term terms)'''
            def subTerms(self):
                '''list-of-Nepomuk.Query.Term Nepomuk.Query.GroupTerm.subTerms()'''
                return [Nepomuk.Query.Term()]
    class Vocabulary():
        """"""
        class TMO():
            """"""
            def urgency(self):
                '''static QUrl Nepomuk.Vocabulary.TMO.urgency()'''
                return QUrl()
            def transmissionType(self):
                '''static QUrl Nepomuk.Vocabulary.TMO.transmissionType()'''
                return QUrl()
            def transmissionTo(self):
                '''static QUrl Nepomuk.Vocabulary.TMO.transmissionTo()'''
                return QUrl()
            def transmissionTask(self):
                '''static QUrl Nepomuk.Vocabulary.TMO.transmissionTask()'''
                return QUrl()
            def transmissionStateChangesTo(self):
                '''static QUrl Nepomuk.Vocabulary.TMO.transmissionStateChangesTo()'''
                return QUrl()
            def transmissionStateChangesFrom(self):
                '''static QUrl Nepomuk.Vocabulary.TMO.transmissionStateChangesFrom()'''
                return QUrl()
            def transmissionState(self):
                '''static QUrl Nepomuk.Vocabulary.TMO.transmissionState()'''
                return QUrl()
            def transmissionFrom(self):
                '''static QUrl Nepomuk.Vocabulary.TMO.transmissionFrom()'''
                return QUrl()
            def timemanagement(self):
                '''static QUrl Nepomuk.Vocabulary.TMO.timemanagement()'''
                return QUrl()
            def taskTransmission(self):
                '''static QUrl Nepomuk.Vocabulary.TMO.taskTransmission()'''
                return QUrl()
            def taskStateChangesTo(self):
                '''static QUrl Nepomuk.Vocabulary.TMO.taskStateChangesTo()'''
                return QUrl()
            def taskStateChangesFrom(self):
                '''static QUrl Nepomuk.Vocabulary.TMO.taskStateChangesFrom()'''
                return QUrl()
            def taskState(self):
                '''static QUrl Nepomuk.Vocabulary.TMO.taskState()'''
                return QUrl()
            def taskSource(self):
                '''static QUrl Nepomuk.Vocabulary.TMO.taskSource()'''
                return QUrl()
            def taskReference(self):
                '''static QUrl Nepomuk.Vocabulary.TMO.taskReference()'''
                return QUrl()
            def taskPrivacyState(self):
                '''static QUrl Nepomuk.Vocabulary.TMO.taskPrivacyState()'''
                return QUrl()
            def taskName(self):
                '''static QUrl Nepomuk.Vocabulary.TMO.taskName()'''
                return QUrl()
            def taskId(self):
                '''static QUrl Nepomuk.Vocabulary.TMO.taskId()'''
                return QUrl()
            def taskGoal(self):
                '''static QUrl Nepomuk.Vocabulary.TMO.taskGoal()'''
                return QUrl()
            def taskDescription(self):
                '''static QUrl Nepomuk.Vocabulary.TMO.taskDescription()'''
                return QUrl()
            def targetTime(self):
                '''static QUrl Nepomuk.Vocabulary.TMO.targetTime()'''
                return QUrl()
            def targetStartTime(self):
                '''static QUrl Nepomuk.Vocabulary.TMO.targetStartTime()'''
                return QUrl()
            def targetEndTime(self):
                '''static QUrl Nepomuk.Vocabulary.TMO.targetEndTime()'''
                return QUrl()
            def targetCompletion(self):
                '''static QUrl Nepomuk.Vocabulary.TMO.targetCompletion()'''
                return QUrl()
            def superTask(self):
                '''static QUrl Nepomuk.Vocabulary.TMO.superTask()'''
                return QUrl()
            def subTaskOrdering(self):
                '''static QUrl Nepomuk.Vocabulary.TMO.subTaskOrdering()'''
                return QUrl()
            def subTask(self):
                '''static QUrl Nepomuk.Vocabulary.TMO.subTask()'''
                return QUrl()
            def stateTypeRole(self):
                '''static QUrl Nepomuk.Vocabulary.TMO.stateTypeRole()'''
                return QUrl()
            def startTime(self):
                '''static QUrl Nepomuk.Vocabulary.TMO.startTime()'''
                return QUrl()
            def sendDateTime(self):
                '''static QUrl Nepomuk.Vocabulary.TMO.sendDateTime()'''
                return QUrl()
            def receiveDateTime(self):
                '''static QUrl Nepomuk.Vocabulary.TMO.receiveDateTime()'''
                return QUrl()
            def progress(self):
                '''static QUrl Nepomuk.Vocabulary.TMO.progress()'''
                return QUrl()
            def priority(self):
                '''static QUrl Nepomuk.Vocabulary.TMO.priority()'''
                return QUrl()
            def nextReviewIntervall(self):
                '''static QUrl Nepomuk.Vocabulary.TMO.nextReviewIntervall()'''
                return QUrl()
            def logEntry(self):
                '''static QUrl Nepomuk.Vocabulary.TMO.logEntry()'''
                return QUrl()
            def lastReviewDate(self):
                '''static QUrl Nepomuk.Vocabulary.TMO.lastReviewDate()'''
                return QUrl()
            def involvedPersons(self):
                '''static QUrl Nepomuk.Vocabulary.TMO.involvedPersons()'''
                return QUrl()
            def involvedPersonTask(self):
                '''static QUrl Nepomuk.Vocabulary.TMO.involvedPersonTask()'''
                return QUrl()
            def involvedPersonRole(self):
                '''static QUrl Nepomuk.Vocabulary.TMO.involvedPersonRole()'''
                return QUrl()
            def involvedPerson(self):
                '''static QUrl Nepomuk.Vocabulary.TMO.involvedPerson()'''
                return QUrl()
            def indexPosition(self):
                '''static QUrl Nepomuk.Vocabulary.TMO.indexPosition()'''
                return QUrl()
            def importance(self):
                '''static QUrl Nepomuk.Vocabulary.TMO.importance()'''
                return QUrl()
            def endTime(self):
                '''static QUrl Nepomuk.Vocabulary.TMO.endTime()'''
                return QUrl()
            def dueDate(self):
                '''static QUrl Nepomuk.Vocabulary.TMO.dueDate()'''
                return QUrl()
            def dependencyType(self):
                '''static QUrl Nepomuk.Vocabulary.TMO.dependencyType()'''
                return QUrl()
            def dependencyOrderNumber(self):
                '''static QUrl Nepomuk.Vocabulary.TMO.dependencyOrderNumber()'''
                return QUrl()
            def dependencyMemberB(self):
                '''static QUrl Nepomuk.Vocabulary.TMO.dependencyMemberB()'''
                return QUrl()
            def dependencyMemberA(self):
                '''static QUrl Nepomuk.Vocabulary.TMO.dependencyMemberA()'''
                return QUrl()
            def dependencyDescription(self):
                '''static QUrl Nepomuk.Vocabulary.TMO.dependencyDescription()'''
                return QUrl()
            def dependency(self):
                '''static QUrl Nepomuk.Vocabulary.TMO.dependency()'''
                return QUrl()
            def delegability(self):
                '''static QUrl Nepomuk.Vocabulary.TMO.delegability()'''
                return QUrl()
            def dateTime(self):
                '''static QUrl Nepomuk.Vocabulary.TMO.dateTime()'''
                return QUrl()
            def createdBy(self):
                '''static QUrl Nepomuk.Vocabulary.TMO.createdBy()'''
                return QUrl()
            def contextThread(self):
                '''static QUrl Nepomuk.Vocabulary.TMO.contextThread()'''
                return QUrl()
            def contextTask(self):
                '''static QUrl Nepomuk.Vocabulary.TMO.contextTask()'''
                return QUrl()
            def containsTask(self):
                '''static QUrl Nepomuk.Vocabulary.TMO.containsTask()'''
                return QUrl()
            def attachmentTask(self):
                '''static QUrl Nepomuk.Vocabulary.TMO.attachmentTask()'''
                return QUrl()
            def attachmentRole(self):
                '''static QUrl Nepomuk.Vocabulary.TMO.attachmentRole()'''
                return QUrl()
            def attachmentReference(self):
                '''static QUrl Nepomuk.Vocabulary.TMO.attachmentReference()'''
                return QUrl()
            def attachment(self):
                '''static QUrl Nepomuk.Vocabulary.TMO.attachment()'''
                return QUrl()
            def actualTime(self):
                '''static QUrl Nepomuk.Vocabulary.TMO.actualTime()'''
                return QUrl()
            def actualStartTime(self):
                '''static QUrl Nepomuk.Vocabulary.TMO.actualStartTime()'''
                return QUrl()
            def actualEndTime(self):
                '''static QUrl Nepomuk.Vocabulary.TMO.actualEndTime()'''
                return QUrl()
            def actualCompletion(self):
                '''static QUrl Nepomuk.Vocabulary.TMO.actualCompletion()'''
                return QUrl()
            def abilityCarrierTask(self):
                '''static QUrl Nepomuk.Vocabulary.TMO.abilityCarrierTask()'''
                return QUrl()
            def abilityCarrierRole(self):
                '''static QUrl Nepomuk.Vocabulary.TMO.abilityCarrierRole()'''
                return QUrl()
            def abilityCarrierInvolvement(self):
                '''static QUrl Nepomuk.Vocabulary.TMO.abilityCarrierInvolvement()'''
                return QUrl()
            def abilityCarrier(self):
                '''static QUrl Nepomuk.Vocabulary.TMO.abilityCarrier()'''
                return QUrl()
            def Urgency(self):
                '''static QUrl Nepomuk.Vocabulary.TMO.Urgency()'''
                return QUrl()
            def UndirectedDependency(self):
                '''static QUrl Nepomuk.Vocabulary.TMO.UndirectedDependency()'''
                return QUrl()
            def TransmissionType(self):
                '''static QUrl Nepomuk.Vocabulary.TMO.TransmissionType()'''
                return QUrl()
            def TransmissionState(self):
                '''static QUrl Nepomuk.Vocabulary.TMO.TransmissionState()'''
                return QUrl()
            def TaskTransmission(self):
                '''static QUrl Nepomuk.Vocabulary.TMO.TaskTransmission()'''
                return QUrl()
            def TaskState(self):
                '''static QUrl Nepomuk.Vocabulary.TMO.TaskState()'''
                return QUrl()
            def TaskPrivacyState(self):
                '''static QUrl Nepomuk.Vocabulary.TMO.TaskPrivacyState()'''
                return QUrl()
            def TaskDependency(self):
                '''static QUrl Nepomuk.Vocabulary.TMO.TaskDependency()'''
                return QUrl()
            def TaskContainer(self):
                '''static QUrl Nepomuk.Vocabulary.TMO.TaskContainer()'''
                return QUrl()
            def Task(self):
                '''static QUrl Nepomuk.Vocabulary.TMO.Task()'''
                return QUrl()
            def TMO_Instance_Urgency_10(self):
                '''static QUrl Nepomuk.Vocabulary.TMO.TMO_Instance_Urgency_10()'''
                return QUrl()
            def TMO_Instance_Urgency_09(self):
                '''static QUrl Nepomuk.Vocabulary.TMO.TMO_Instance_Urgency_09()'''
                return QUrl()
            def TMO_Instance_Urgency_08(self):
                '''static QUrl Nepomuk.Vocabulary.TMO.TMO_Instance_Urgency_08()'''
                return QUrl()
            def TMO_Instance_Urgency_07(self):
                '''static QUrl Nepomuk.Vocabulary.TMO.TMO_Instance_Urgency_07()'''
                return QUrl()
            def TMO_Instance_Urgency_06(self):
                '''static QUrl Nepomuk.Vocabulary.TMO.TMO_Instance_Urgency_06()'''
                return QUrl()
            def TMO_Instance_Urgency_05(self):
                '''static QUrl Nepomuk.Vocabulary.TMO.TMO_Instance_Urgency_05()'''
                return QUrl()
            def TMO_Instance_Urgency_04(self):
                '''static QUrl Nepomuk.Vocabulary.TMO.TMO_Instance_Urgency_04()'''
                return QUrl()
            def TMO_Instance_Urgency_03(self):
                '''static QUrl Nepomuk.Vocabulary.TMO.TMO_Instance_Urgency_03()'''
                return QUrl()
            def TMO_Instance_Urgency_02(self):
                '''static QUrl Nepomuk.Vocabulary.TMO.TMO_Instance_Urgency_02()'''
                return QUrl()
            def TMO_Instance_Urgency_01(self):
                '''static QUrl Nepomuk.Vocabulary.TMO.TMO_Instance_Urgency_01()'''
                return QUrl()
            def TMO_Instance_TransmissionType_Transfer(self):
                '''static QUrl Nepomuk.Vocabulary.TMO.TMO_Instance_TransmissionType_Transfer()'''
                return QUrl()
            def TMO_Instance_TransmissionType_Join(self):
                '''static QUrl Nepomuk.Vocabulary.TMO.TMO_Instance_TransmissionType_Join()'''
                return QUrl()
            def TMO_Instance_TransmissionType_Delegation(self):
                '''static QUrl Nepomuk.Vocabulary.TMO.TMO_Instance_TransmissionType_Delegation()'''
                return QUrl()
            def TMO_Instance_TransmissionState_Transmitted(self):
                '''static QUrl Nepomuk.Vocabulary.TMO.TMO_Instance_TransmissionState_Transmitted()'''
                return QUrl()
            def TMO_Instance_TransmissionState_Rejected_Transmitted(self):
                '''static QUrl Nepomuk.Vocabulary.TMO.TMO_Instance_TransmissionState_Rejected_Transmitted()'''
                return QUrl()
            def TMO_Instance_TransmissionState_Rejected_NotTransmitted(self):
                '''static QUrl Nepomuk.Vocabulary.TMO.TMO_Instance_TransmissionState_Rejected_NotTransmitted()'''
                return QUrl()
            def TMO_Instance_TransmissionState_NotTransmitted(self):
                '''static QUrl Nepomuk.Vocabulary.TMO.TMO_Instance_TransmissionState_NotTransmitted()'''
                return QUrl()
            def TMO_Instance_TransmissionState_Accepted_Transmitted(self):
                '''static QUrl Nepomuk.Vocabulary.TMO.TMO_Instance_TransmissionState_Accepted_Transmitted()'''
                return QUrl()
            def TMO_Instance_TransmissionState_Accepted_NotTransmitted(self):
                '''static QUrl Nepomuk.Vocabulary.TMO.TMO_Instance_TransmissionState_Accepted_NotTransmitted()'''
                return QUrl()
            def TMO_Instance_TaskState_Terminated(self):
                '''static QUrl Nepomuk.Vocabulary.TMO.TMO_Instance_TaskState_Terminated()'''
                return QUrl()
            def TMO_Instance_TaskState_Suspended(self):
                '''static QUrl Nepomuk.Vocabulary.TMO.TMO_Instance_TaskState_Suspended()'''
                return QUrl()
            def TMO_Instance_TaskState_Running(self):
                '''static QUrl Nepomuk.Vocabulary.TMO.TMO_Instance_TaskState_Running()'''
                return QUrl()
            def TMO_Instance_TaskState_New(self):
                '''static QUrl Nepomuk.Vocabulary.TMO.TMO_Instance_TaskState_New()'''
                return QUrl()
            def TMO_Instance_TaskState_Finalized(self):
                '''static QUrl Nepomuk.Vocabulary.TMO.TMO_Instance_TaskState_Finalized()'''
                return QUrl()
            def TMO_Instance_TaskState_Deleted(self):
                '''static QUrl Nepomuk.Vocabulary.TMO.TMO_Instance_TaskState_Deleted()'''
                return QUrl()
            def TMO_Instance_TaskState_Completed(self):
                '''static QUrl Nepomuk.Vocabulary.TMO.TMO_Instance_TaskState_Completed()'''
                return QUrl()
            def TMO_Instance_TaskState_Archived(self):
                '''static QUrl Nepomuk.Vocabulary.TMO.TMO_Instance_TaskState_Archived()'''
                return QUrl()
            def TMO_Instance_TaskPrivacy_Professional(self):
                '''static QUrl Nepomuk.Vocabulary.TMO.TMO_Instance_TaskPrivacy_Professional()'''
                return QUrl()
            def TMO_Instance_TaskPrivacy_Private(self):
                '''static QUrl Nepomuk.Vocabulary.TMO.TMO_Instance_TaskPrivacy_Private()'''
                return QUrl()
            def TMO_Instance_TaskContainer_trashtasks(self):
                '''static QUrl Nepomuk.Vocabulary.TMO.TMO_Instance_TaskContainer_trashtasks()'''
                return QUrl()
            def TMO_Instance_TaskContainer_outbox(self):
                '''static QUrl Nepomuk.Vocabulary.TMO.TMO_Instance_TaskContainer_outbox()'''
                return QUrl()
            def TMO_Instance_TaskContainer_inbox(self):
                '''static QUrl Nepomuk.Vocabulary.TMO.TMO_Instance_TaskContainer_inbox()'''
                return QUrl()
            def TMO_Instance_TaskContainer_archive(self):
                '''static QUrl Nepomuk.Vocabulary.TMO.TMO_Instance_TaskContainer_archive()'''
                return QUrl()
            def TMO_Instance_TaskContainer_activetasks(self):
                '''static QUrl Nepomuk.Vocabulary.TMO.TMO_Instance_TaskContainer_activetasks()'''
                return QUrl()
            def TMO_Instance_Priority_Medium(self):
                '''static QUrl Nepomuk.Vocabulary.TMO.TMO_Instance_Priority_Medium()'''
                return QUrl()
            def TMO_Instance_Priority_Low(self):
                '''static QUrl Nepomuk.Vocabulary.TMO.TMO_Instance_Priority_Low()'''
                return QUrl()
            def TMO_Instance_Priority_High(self):
                '''static QUrl Nepomuk.Vocabulary.TMO.TMO_Instance_Priority_High()'''
                return QUrl()
            def TMO_Instance_PersonInvolvementRole_Suggested(self):
                '''static QUrl Nepomuk.Vocabulary.TMO.TMO_Instance_PersonInvolvementRole_Suggested()'''
                return QUrl()
            def TMO_Instance_PersonInvolvementRole_Reviewer(self):
                '''static QUrl Nepomuk.Vocabulary.TMO.TMO_Instance_PersonInvolvementRole_Reviewer()'''
                return QUrl()
            def TMO_Instance_PersonInvolvementRole_Related(self):
                '''static QUrl Nepomuk.Vocabulary.TMO.TMO_Instance_PersonInvolvementRole_Related()'''
                return QUrl()
            def TMO_Instance_PersonInvolvementRole_Receiver(self):
                '''static QUrl Nepomuk.Vocabulary.TMO.TMO_Instance_PersonInvolvementRole_Receiver()'''
                return QUrl()
            def TMO_Instance_PersonInvolvementRole_Owner(self):
                '''static QUrl Nepomuk.Vocabulary.TMO.TMO_Instance_PersonInvolvementRole_Owner()'''
                return QUrl()
            def TMO_Instance_PersonInvolvementRole_Observer(self):
                '''static QUrl Nepomuk.Vocabulary.TMO.TMO_Instance_PersonInvolvementRole_Observer()'''
                return QUrl()
            def TMO_Instance_PersonInvolvementRole_Involved(self):
                '''static QUrl Nepomuk.Vocabulary.TMO.TMO_Instance_PersonInvolvementRole_Involved()'''
                return QUrl()
            def TMO_Instance_PersonInvolvementRole_InternalObserver(self):
                '''static QUrl Nepomuk.Vocabulary.TMO.TMO_Instance_PersonInvolvementRole_InternalObserver()'''
                return QUrl()
            def TMO_Instance_PersonInvolvementRole_Initiator(self):
                '''static QUrl Nepomuk.Vocabulary.TMO.TMO_Instance_PersonInvolvementRole_Initiator()'''
                return QUrl()
            def TMO_Instance_PersonInvolvementRole_ExternalObserver(self):
                '''static QUrl Nepomuk.Vocabulary.TMO.TMO_Instance_PersonInvolvementRole_ExternalObserver()'''
                return QUrl()
            def TMO_Instance_PersonInvolvementRole_Executor(self):
                '''static QUrl Nepomuk.Vocabulary.TMO.TMO_Instance_PersonInvolvementRole_Executor()'''
                return QUrl()
            def TMO_Instance_PersonInvolvementRole_Delegate(self):
                '''static QUrl Nepomuk.Vocabulary.TMO.TMO_Instance_PersonInvolvementRole_Delegate()'''
                return QUrl()
            def TMO_Instance_PersonInvolvementRole_Creator(self):
                '''static QUrl Nepomuk.Vocabulary.TMO.TMO_Instance_PersonInvolvementRole_Creator()'''
                return QUrl()
            def TMO_Instance_PersonInvolvementRole_Controller(self):
                '''static QUrl Nepomuk.Vocabulary.TMO.TMO_Instance_PersonInvolvementRole_Controller()'''
                return QUrl()
            def TMO_Instance_PersonInvolvementRole_Collaborator(self):
                '''static QUrl Nepomuk.Vocabulary.TMO.TMO_Instance_PersonInvolvementRole_Collaborator()'''
                return QUrl()
            def TMO_Instance_PersonInvolvementRole_Coworker(self):
                '''static QUrl Nepomuk.Vocabulary.TMO.TMO_Instance_PersonInvolvementRole_Coworker()'''
                return QUrl()
            def TMO_Instance_PersonInvolvementRole_Analyst(self):
                '''static QUrl Nepomuk.Vocabulary.TMO.TMO_Instance_PersonInvolvementRole_Analyst()'''
                return QUrl()
            def TMO_Instance_Importance_10(self):
                '''static QUrl Nepomuk.Vocabulary.TMO.TMO_Instance_Importance_10()'''
                return QUrl()
            def TMO_Instance_Importance_09(self):
                '''static QUrl Nepomuk.Vocabulary.TMO.TMO_Instance_Importance_09()'''
                return QUrl()
            def TMO_Instance_Importance_08(self):
                '''static QUrl Nepomuk.Vocabulary.TMO.TMO_Instance_Importance_08()'''
                return QUrl()
            def TMO_Instance_Importance_07(self):
                '''static QUrl Nepomuk.Vocabulary.TMO.TMO_Instance_Importance_07()'''
                return QUrl()
            def TMO_Instance_Importance_06(self):
                '''static QUrl Nepomuk.Vocabulary.TMO.TMO_Instance_Importance_06()'''
                return QUrl()
            def TMO_Instance_Importance_05(self):
                '''static QUrl Nepomuk.Vocabulary.TMO.TMO_Instance_Importance_05()'''
                return QUrl()
            def TMO_Instance_Importance_04(self):
                '''static QUrl Nepomuk.Vocabulary.TMO.TMO_Instance_Importance_04()'''
                return QUrl()
            def TMO_Instance_Importance_03(self):
                '''static QUrl Nepomuk.Vocabulary.TMO.TMO_Instance_Importance_03()'''
                return QUrl()
            def TMO_Instance_Importance_02(self):
                '''static QUrl Nepomuk.Vocabulary.TMO.TMO_Instance_Importance_02()'''
                return QUrl()
            def TMO_Instance_Importance_01(self):
                '''static QUrl Nepomuk.Vocabulary.TMO.TMO_Instance_Importance_01()'''
                return QUrl()
            def TMO_Instance_Delegability_Unrestricted(self):
                '''static QUrl Nepomuk.Vocabulary.TMO.TMO_Instance_Delegability_Unrestricted()'''
                return QUrl()
            def TMO_Instance_Delegability_Never(self):
                '''static QUrl Nepomuk.Vocabulary.TMO.TMO_Instance_Delegability_Never()'''
                return QUrl()
            def TMO_Instance_Delegability_Medium(self):
                '''static QUrl Nepomuk.Vocabulary.TMO.TMO_Instance_Delegability_Medium()'''
                return QUrl()
            def TMO_Instance_Delegability_Low(self):
                '''static QUrl Nepomuk.Vocabulary.TMO.TMO_Instance_Delegability_Low()'''
                return QUrl()
            def TMO_Instance_Delegability_High(self):
                '''static QUrl Nepomuk.Vocabulary.TMO.TMO_Instance_Delegability_High()'''
                return QUrl()
            def TMO_Instance_AttachmentRole_Used(self):
                '''static QUrl Nepomuk.Vocabulary.TMO.TMO_Instance_AttachmentRole_Used()'''
                return QUrl()
            def TMO_Instance_AttachmentRole_Required(self):
                '''static QUrl Nepomuk.Vocabulary.TMO.TMO_Instance_AttachmentRole_Required()'''
                return QUrl()
            def TMO_Instance_AttachmentRole_Related(self):
                '''static QUrl Nepomuk.Vocabulary.TMO.TMO_Instance_AttachmentRole_Related()'''
                return QUrl()
            def TMO_Instance_AttachmentRole_Desired_Requested(self):
                '''static QUrl Nepomuk.Vocabulary.TMO.TMO_Instance_AttachmentRole_Desired_Requested()'''
                return QUrl()
            def TMO_Instance_AbilityCarrierRole_Used(self):
                '''static QUrl Nepomuk.Vocabulary.TMO.TMO_Instance_AbilityCarrierRole_Used()'''
                return QUrl()
            def TMO_Instance_AbilityCarrierRole_Required(self):
                '''static QUrl Nepomuk.Vocabulary.TMO.TMO_Instance_AbilityCarrierRole_Required()'''
                return QUrl()
            def TMO_Instance_AbilityCarrierRole_Requested(self):
                '''static QUrl Nepomuk.Vocabulary.TMO.TMO_Instance_AbilityCarrierRole_Requested()'''
                return QUrl()
            def SuperSubTaskDependency(self):
                '''static QUrl Nepomuk.Vocabulary.TMO.SuperSubTaskDependency()'''
                return QUrl()
            def SuccessorDependency(self):
                '''static QUrl Nepomuk.Vocabulary.TMO.SuccessorDependency()'''
                return QUrl()
            def StateTypeRole(self):
                '''static QUrl Nepomuk.Vocabulary.TMO.StateTypeRole()'''
                return QUrl()
            def Skill(self):
                '''static QUrl Nepomuk.Vocabulary.TMO.Skill()'''
                return QUrl()
            def SimilarityDependence(self):
                '''static QUrl Nepomuk.Vocabulary.TMO.SimilarityDependence()'''
                return QUrl()
            def Role(self):
                '''static QUrl Nepomuk.Vocabulary.TMO.Role()'''
                return QUrl()
            def Priority(self):
                '''static QUrl Nepomuk.Vocabulary.TMO.Priority()'''
                return QUrl()
            def PredecessorSuccessorDependency(self):
                '''static QUrl Nepomuk.Vocabulary.TMO.PredecessorSuccessorDependency()'''
                return QUrl()
            def PredecessorDependency(self):
                '''static QUrl Nepomuk.Vocabulary.TMO.PredecessorDependency()'''
                return QUrl()
            def PersonInvolvementRole(self):
                '''static QUrl Nepomuk.Vocabulary.TMO.PersonInvolvementRole()'''
                return QUrl()
            def PersonInvolvement(self):
                '''static QUrl Nepomuk.Vocabulary.TMO.PersonInvolvement()'''
                return QUrl()
            def Interdependence(self):
                '''static QUrl Nepomuk.Vocabulary.TMO.Interdependence()'''
                return QUrl()
            def Importance(self):
                '''static QUrl Nepomuk.Vocabulary.TMO.Importance()'''
                return QUrl()
            def Delegability(self):
                '''static QUrl Nepomuk.Vocabulary.TMO.Delegability()'''
                return QUrl()
            def AttachmentRole(self):
                '''static QUrl Nepomuk.Vocabulary.TMO.AttachmentRole()'''
                return QUrl()
            def Attachment(self):
                '''static QUrl Nepomuk.Vocabulary.TMO.Attachment()'''
                return QUrl()
            def AssociationDependency(self):
                '''static QUrl Nepomuk.Vocabulary.TMO.AssociationDependency()'''
                return QUrl()
            def AgentAbilityCarrier(self):
                '''static QUrl Nepomuk.Vocabulary.TMO.AgentAbilityCarrier()'''
                return QUrl()
            def AbilityCarrierRole(self):
                '''static QUrl Nepomuk.Vocabulary.TMO.AbilityCarrierRole()'''
                return QUrl()
            def AbilityCarrierInvolvement(self):
                '''static QUrl Nepomuk.Vocabulary.TMO.AbilityCarrierInvolvement()'''
                return QUrl()
            def AbilityCarrier(self):
                '''static QUrl Nepomuk.Vocabulary.TMO.AbilityCarrier()'''
                return QUrl()
            def nrlOntologyGraph(self):
                '''static QUrl Nepomuk.Vocabulary.TMO.nrlOntologyGraph()'''
                return QUrl()
            def tmoNamespace(self):
                '''static QUrl Nepomuk.Vocabulary.TMO.tmoNamespace()'''
                return QUrl()
    class Query():
        """"""
        class Result():
            """"""
            def __init__(self):
                '''void Nepomuk.Query.Result.__init__()'''
            def __init__(self, resource, score = 0):
                '''void Nepomuk.Query.Result.__init__(Nepomuk.Resource resource, float score = 0)'''
            def __init__(self):
                '''Nepomuk.Query.Result Nepomuk.Query.Result.__init__()'''
                return Nepomuk.Query.Result()
            def __ne__(self):
                '''Nepomuk.Query.Result Nepomuk.Query.Result.__ne__()'''
                return Nepomuk.Query.Result()
            def excerpt(self):
                '''QString Nepomuk.Query.Result.excerpt()'''
                return QString()
            def setExcerpt(self, text):
                '''void Nepomuk.Query.Result.setExcerpt(QString text)'''
            def additionalBinding(self, name):
                '''Nepomuk.Variant Nepomuk.Query.Result.additionalBinding(QString name)'''
                return Nepomuk.Variant()
            def additionalBindings(self):
                '''Soprano.BindingSet Nepomuk.Query.Result.additionalBindings()'''
                return Soprano.BindingSet()
            def setAdditionalBindings(self, bindings):
                '''void Nepomuk.Query.Result.setAdditionalBindings(Soprano.BindingSet bindings)'''
            def __eq__(self):
                '''Nepomuk.Query.Result Nepomuk.Query.Result.__eq__()'''
                return Nepomuk.Query.Result()
            def requestProperty(self, property):
                '''Soprano.Node Nepomuk.Query.Result.requestProperty(Nepomuk.Types.Property property)'''
                return Soprano.Node()
            def __getitem__(self, property):
                '''Soprano.Node Nepomuk.Query.Result.__getitem__(Nepomuk.Types.Property property)'''
                return Soprano.Node()
            def requestProperties(self):
                '''dict-of-Nepomuk.Types.Property-Soprano.Node Nepomuk.Query.Result.requestProperties()'''
                return dict-of-Nepomuk.Types.Property-Soprano.Node()
            def addRequestProperty(self, property, value):
                '''void Nepomuk.Query.Result.addRequestProperty(Nepomuk.Types.Property property, Soprano.Node value)'''
            def setScore(self, score):
                '''void Nepomuk.Query.Result.setScore(float score)'''
            def resource(self):
                '''Nepomuk.Resource Nepomuk.Query.Result.resource()'''
                return Nepomuk.Resource()
            def score(self):
                '''float Nepomuk.Query.Result.score()'''
                return float()
    class Query():
        """"""
        class AndTerm(Nepomuk.Query.GroupTerm):
            """"""
            def __init__(self):
                '''void Nepomuk.Query.AndTerm.__init__()'''
            def __init__(self, term):
                '''void Nepomuk.Query.AndTerm.__init__(Nepomuk.Query.AndTerm term)'''
            def __init__(self, term1, term2, term3 = None, term4 = None, term5 = None, term6 = None):
                '''void Nepomuk.Query.AndTerm.__init__(Nepomuk.Query.Term term1, Nepomuk.Query.Term term2, Nepomuk.Query.Term term3 = Nepomuk.Query.Term(), Nepomuk.Query.Term term4 = Nepomuk.Query.Term(), Nepomuk.Query.Term term5 = Nepomuk.Query.Term(), Nepomuk.Query.Term term6 = Nepomuk.Query.Term())'''
            def __init__(self, terms):
                '''void Nepomuk.Query.AndTerm.__init__(list-of-Nepomuk.Query.Term terms)'''
    class Query():
        """"""
        class QueryParser():
            """"""
            class ParserFlags():
                """"""
                def __init__(self):
                    '''Nepomuk.Query.QueryParser.ParserFlags Nepomuk.Query.QueryParser.ParserFlags.__init__()'''
                    return Nepomuk.Query.QueryParser.ParserFlags()
                def __init__(self):
                    '''int Nepomuk.Query.QueryParser.ParserFlags.__init__()'''
                    return int()
                def __init__(self):
                    '''void Nepomuk.Query.QueryParser.ParserFlags.__init__()'''
                def __bool__(self):
                    '''int Nepomuk.Query.QueryParser.ParserFlags.__bool__()'''
                    return int()
                def __ne__(self, f):
                    '''bool Nepomuk.Query.QueryParser.ParserFlags.__ne__(Nepomuk.Query.QueryParser.ParserFlags f)'''
                    return bool()
                def __eq__(self, f):
                    '''bool Nepomuk.Query.QueryParser.ParserFlags.__eq__(Nepomuk.Query.QueryParser.ParserFlags f)'''
                    return bool()
                def __invert__(self):
                    '''Nepomuk.Query.QueryParser.ParserFlags Nepomuk.Query.QueryParser.ParserFlags.__invert__()'''
                    return Nepomuk.Query.QueryParser.ParserFlags()
                def __and__(self, mask):
                    '''Nepomuk.Query.QueryParser.ParserFlags Nepomuk.Query.QueryParser.ParserFlags.__and__(int mask)'''
                    return Nepomuk.Query.QueryParser.ParserFlags()
                def __xor__(self, f):
                    '''Nepomuk.Query.QueryParser.ParserFlags Nepomuk.Query.QueryParser.ParserFlags.__xor__(Nepomuk.Query.QueryParser.ParserFlags f)'''
                    return Nepomuk.Query.QueryParser.ParserFlags()
                def __xor__(self, f):
                    '''Nepomuk.Query.QueryParser.ParserFlags Nepomuk.Query.QueryParser.ParserFlags.__xor__(int f)'''
                    return Nepomuk.Query.QueryParser.ParserFlags()
                def __or__(self, f):
                    '''Nepomuk.Query.QueryParser.ParserFlags Nepomuk.Query.QueryParser.ParserFlags.__or__(Nepomuk.Query.QueryParser.ParserFlags f)'''
                    return Nepomuk.Query.QueryParser.ParserFlags()
                def __or__(self, f):
                    '''Nepomuk.Query.QueryParser.ParserFlags Nepomuk.Query.QueryParser.ParserFlags.__or__(int f)'''
                    return Nepomuk.Query.QueryParser.ParserFlags()
                def __int__(self):
                    '''int Nepomuk.Query.QueryParser.ParserFlags.__int__()'''
                    return int()
                def __ixor__(self, f):
                    '''Nepomuk.Query.QueryParser.ParserFlags Nepomuk.Query.QueryParser.ParserFlags.__ixor__(Nepomuk.Query.QueryParser.ParserFlags f)'''
                    return Nepomuk.Query.QueryParser.ParserFlags()
                def __ior__(self, f):
                    '''Nepomuk.Query.QueryParser.ParserFlags Nepomuk.Query.QueryParser.ParserFlags.__ior__(Nepomuk.Query.QueryParser.ParserFlags f)'''
                    return Nepomuk.Query.QueryParser.ParserFlags()
                def __iand__(self, mask):
                    '''Nepomuk.Query.QueryParser.ParserFlags Nepomuk.Query.QueryParser.ParserFlags.__iand__(int mask)'''
                    return Nepomuk.Query.QueryParser.ParserFlags()
    class Query():
        """"""
        class OptionalTerm(Nepomuk.Query.SimpleTerm):
            """"""
            def __init__(self):
                '''void Nepomuk.Query.OptionalTerm.__init__()'''
            def __init__(self, term):
                '''void Nepomuk.Query.OptionalTerm.__init__(Nepomuk.Query.OptionalTerm term)'''
            def optionalizeTerm(self, term):
                '''static Nepomuk.Query.Term Nepomuk.Query.OptionalTerm.optionalizeTerm(Nepomuk.Query.Term term)'''
                return Nepomuk.Query.Term()
    class Query():
        """"""
        class FileQuery():
            """"""
            class FileMode():
                """"""
                def __init__(self):
                    '''Nepomuk.Query.FileQuery.FileMode Nepomuk.Query.FileQuery.FileMode.__init__()'''
                    return Nepomuk.Query.FileQuery.FileMode()
                def __init__(self):
                    '''int Nepomuk.Query.FileQuery.FileMode.__init__()'''
                    return int()
                def __init__(self):
                    '''void Nepomuk.Query.FileQuery.FileMode.__init__()'''
                def __bool__(self):
                    '''int Nepomuk.Query.FileQuery.FileMode.__bool__()'''
                    return int()
                def __ne__(self, f):
                    '''bool Nepomuk.Query.FileQuery.FileMode.__ne__(Nepomuk.Query.FileQuery.FileMode f)'''
                    return bool()
                def __eq__(self, f):
                    '''bool Nepomuk.Query.FileQuery.FileMode.__eq__(Nepomuk.Query.FileQuery.FileMode f)'''
                    return bool()
                def __invert__(self):
                    '''Nepomuk.Query.FileQuery.FileMode Nepomuk.Query.FileQuery.FileMode.__invert__()'''
                    return Nepomuk.Query.FileQuery.FileMode()
                def __and__(self, mask):
                    '''Nepomuk.Query.FileQuery.FileMode Nepomuk.Query.FileQuery.FileMode.__and__(int mask)'''
                    return Nepomuk.Query.FileQuery.FileMode()
                def __xor__(self, f):
                    '''Nepomuk.Query.FileQuery.FileMode Nepomuk.Query.FileQuery.FileMode.__xor__(Nepomuk.Query.FileQuery.FileMode f)'''
                    return Nepomuk.Query.FileQuery.FileMode()
                def __xor__(self, f):
                    '''Nepomuk.Query.FileQuery.FileMode Nepomuk.Query.FileQuery.FileMode.__xor__(int f)'''
                    return Nepomuk.Query.FileQuery.FileMode()
                def __or__(self, f):
                    '''Nepomuk.Query.FileQuery.FileMode Nepomuk.Query.FileQuery.FileMode.__or__(Nepomuk.Query.FileQuery.FileMode f)'''
                    return Nepomuk.Query.FileQuery.FileMode()
                def __or__(self, f):
                    '''Nepomuk.Query.FileQuery.FileMode Nepomuk.Query.FileQuery.FileMode.__or__(int f)'''
                    return Nepomuk.Query.FileQuery.FileMode()
                def __int__(self):
                    '''int Nepomuk.Query.FileQuery.FileMode.__int__()'''
                    return int()
                def __ixor__(self, f):
                    '''Nepomuk.Query.FileQuery.FileMode Nepomuk.Query.FileQuery.FileMode.__ixor__(Nepomuk.Query.FileQuery.FileMode f)'''
                    return Nepomuk.Query.FileQuery.FileMode()
                def __ior__(self, f):
                    '''Nepomuk.Query.FileQuery.FileMode Nepomuk.Query.FileQuery.FileMode.__ior__(Nepomuk.Query.FileQuery.FileMode f)'''
                    return Nepomuk.Query.FileQuery.FileMode()
                def __iand__(self, mask):
                    '''Nepomuk.Query.FileQuery.FileMode Nepomuk.Query.FileQuery.FileMode.__iand__(int mask)'''
                    return Nepomuk.Query.FileQuery.FileMode()
    class Types():
        """"""
        class Literal():
            """"""
            def __init__(self):
                '''void Nepomuk.Types.Literal.__init__()'''
            def __init__(self):
                '''Nepomuk.Types.Literal Nepomuk.Types.Literal.__init__()'''
                return Nepomuk.Types.Literal()
            def __init__(self, dataTypeUri):
                '''void Nepomuk.Types.Literal.__init__(QUrl dataTypeUri)'''
            def isValid(self):
                '''bool Nepomuk.Types.Literal.isValid()'''
                return bool()
            def dataType(self):
                '''Type Nepomuk.Types.Literal.dataType()'''
                return Type()
            def dataTypeUri(self):
                '''QUrl Nepomuk.Types.Literal.dataTypeUri()'''
                return QUrl()
    class Types():
        """"""
        class Entity():
            """"""
            def __init__(self):
                '''Nepomuk.Types.Entity Nepomuk.Types.Entity.__init__()'''
                return Nepomuk.Types.Entity()
            def __init__(self):
                '''void Nepomuk.Types.Entity.__init__()'''
            def userVisible(self):
                '''bool Nepomuk.Types.Entity.userVisible()'''
                return bool()
            def comment(self, language):
                '''QString Nepomuk.Types.Entity.comment(QString language)'''
                return QString()
            def label(self, language):
                '''QString Nepomuk.Types.Entity.label(QString language)'''
                return QString()
            def __ne__(self, other):
                '''bool Nepomuk.Types.Entity.__ne__(Nepomuk.Types.Entity other)'''
                return bool()
            def __ne__(self, other):
                '''bool Nepomuk.Types.Entity.__ne__(QUrl other)'''
                return bool()
            def __eq__(self, other):
                '''bool Nepomuk.Types.Entity.__eq__(Nepomuk.Types.Entity other)'''
                return bool()
            def __eq__(self, other):
                '''bool Nepomuk.Types.Entity.__eq__(QUrl other)'''
                return bool()
            def reset(self, recursive = False):
                '''void Nepomuk.Types.Entity.reset(bool recursive = False)'''
            def isAvailable(self):
                '''bool Nepomuk.Types.Entity.isAvailable()'''
                return bool()
            def isValid(self):
                '''bool Nepomuk.Types.Entity.isValid()'''
                return bool()
            def icon(self):
                '''QIcon Nepomuk.Types.Entity.icon()'''
                return QIcon()
            def uri(self):
                '''QUrl Nepomuk.Types.Entity.uri()'''
                return QUrl()
            def name(self):
                '''QString Nepomuk.Types.Entity.name()'''
                return QString()


class KTagCloudWidget(QWidget):
    """"""
    def __init__(self, parent = None):
        '''void KTagCloudWidget.__init__(QWidget parent = None)'''
    def addTags(self, tags):
        '''void KTagCloudWidget.addTags(unknown-type tags)'''
    def resizeEvent(self, e):
        '''void KTagCloudWidget.resizeEvent(QResizeEvent e)'''
    tagClicked = pyqtSignal() # void tagClicked(const QStringamp;) - signal
    def setMinFontSize(self, pointSize):
        '''void KTagCloudWidget.setMinFontSize(int pointSize)'''
    def setMaxFontSize(self, pointSize):
        '''void KTagCloudWidget.setMaxFontSize(int pointSize)'''
    def clear(self):
        '''void KTagCloudWidget.clear()'''
    def addTag(self, tag, weight):
        '''void KTagCloudWidget.addTag(QString tag, int weight)'''
    def tagWeight(self, tag):
        '''int KTagCloudWidget.tagWeight(QString tag)'''
        return int()


class KTagDisplayWidget(QWidget):
    """"""
    def __init__(self, parent = None):
        '''void KTagDisplayWidget.__init__(QWidget parent = None)'''
    tagClicked = pyqtSignal() # void tagClicked(const QStringamp;) - signal
    def clear(self):
        '''void KTagDisplayWidget.clear()'''
    def addTags(self, tags):
        '''void KTagDisplayWidget.addTags(QStringList tags)'''
    def addTag(self, tag):
        '''void KTagDisplayWidget.addTag(QString tag)'''
    def setTags(self, tags):
        '''void KTagDisplayWidget.setTags(QStringList tags)'''


