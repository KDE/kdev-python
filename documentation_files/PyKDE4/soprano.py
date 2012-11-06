class pyqtSignal():
 def connect(self, targetSignal): pass
 def emit(self, *args): pass
from QtCore import *

class Soprano():
    """"""
    # Enum Soprano.BackendFeature
    BackendFeatureNone = 0
    BackendFeatureAddStatement = 0
    BackendFeatureRemoveStatements = 0
    BackendFeatureListStatements = 0
    BackendFeatureQuery = 0
    BackendFeatureInference = 0
    BackendFeatureInferenceOptional = 0
    BackendFeatureContext = 0
    BackendFeatureStorageMemory = 0
    BackendFeatureAll = 0
    BackendFeatureUser = 0

    # Enum Soprano.BackendOption
    BackendOptionNone = 0
    BackendOptionStorageMemory = 0
    BackendOptionEnableInference = 0
    BackendOptionStorageDir = 0
    BackendOptionHost = 0
    BackendOptionPort = 0
    BackendOptionUsername = 0
    BackendOptionPassword = 0
    BackendOptionUser = 0

    # Enum Soprano.RdfSerialization
    SerializationUnknown = 0
    SerializationRdfXml = 0
    SerializationN3 = 0
    SerializationNTriples = 0
    SerializationTurtle = 0
    SerializationTrig = 0
    SerializationNQuads = 0
    SerializationUser = 0

    def qHash(self, node):
        '''static int Soprano.qHash(Soprano.LanguageTag node)'''
        return int()
    def qHash(self, lit):
        '''static int Soprano.qHash(Soprano.LiteralValue lit)'''
        return int()
    def qHash(self, node):
        '''static int Soprano.qHash(Soprano.Node node)'''
        return int()
    def qHash(self, s):
        '''static int Soprano.qHash(Soprano.Statement s)'''
        return int()
    def createModel(self, settings = None):
        '''static Soprano.Model Soprano.createModel(list-of-Soprano.BackendSetting settings = Soprano.BackendSettings())'''
        return Soprano.Model()
    def usedBackend(self):
        '''static Soprano.Backend Soprano.usedBackend()'''
        return Soprano.Backend()
    def setUsedBackend(self):
        '''static Soprano.Backend Soprano.setUsedBackend()'''
        return Soprano.Backend()
    def discoverBackendByFeatures(self, features, userFeatures = QStringList()):
        '''static Soprano.Backend Soprano.discoverBackendByFeatures(Soprano.BackendFeatures features, QStringList userFeatures = QStringList())'''
        return Soprano.Backend()
    def discoverBackendByName(self, name):
        '''static Soprano.Backend Soprano.discoverBackendByName(QString name)'''
        return Soprano.Backend()
    def valueInSettingsWithDefault(self, settings, option, defaultValue):
        '''static QVariant Soprano.valueInSettingsWithDefault(list-of-Soprano.BackendSetting settings, Soprano.BackendOption option, QVariant defaultValue)'''
        return QVariant()
    def valueInSettings(self, settings, option, userOptionName = QString()):
        '''static QVariant Soprano.valueInSettings(list-of-Soprano.BackendSetting settings, Soprano.BackendOption option, QString userOptionName = QString())'''
        return QVariant()
    def valueInSettings(self, settings, userOptionName, defaultValue = QVariant()):
        '''static QVariant Soprano.valueInSettings(list-of-Soprano.BackendSetting settings, QString userOptionName, QVariant defaultValue = QVariant())'''
        return QVariant()
    def settingInSettings(self, settings, option, userOptionName = QString()):
        '''static Soprano.BackendSetting Soprano.settingInSettings(list-of-Soprano.BackendSetting settings, Soprano.BackendOption option, QString userOptionName = QString())'''
        return Soprano.BackendSetting()
    def settingInSettings(self, settings, userOptionName):
        '''static Soprano.BackendSetting Soprano.settingInSettings(list-of-Soprano.BackendSetting settings, QString userOptionName)'''
        return Soprano.BackendSetting()
    def isOptionInSettings(self, settings, option, userOptionName = QString()):
        '''static bool Soprano.isOptionInSettings(list-of-Soprano.BackendSetting settings, Soprano.BackendOption option, QString userOptionName = QString())'''
        return bool()
    def mimeTypeToSerialization(self, mimetype):
        '''static Soprano.RdfSerialization Soprano.mimeTypeToSerialization(QString mimetype)'''
        return Soprano.RdfSerialization()
    def serializationMimeType(self, serialization, userSerialization = QString()):
        '''static QString Soprano.serializationMimeType(Soprano.RdfSerialization serialization, QString userSerialization = QString())'''
        return QString()
    class Util():
        """"""
        class AsyncModel(Soprano.FilterModel):
            """"""
            # Enum Soprano.Util.AsyncModel.AsyncModelMode
            SingleThreaded = 0
            MultiThreaded = 0
        
            def __init__(self, parent = None):
                '''void Soprano.Util.AsyncModel.__init__(Soprano.Model parent = None)'''
            def executeQuery(self, query, language, userQueryLanguage = QString()):
                '''Soprano.QueryResultIterator Soprano.Util.AsyncModel.executeQuery(QString query, Soprano.Query.QueryLanguage language, QString userQueryLanguage = QString())'''
                return Soprano.QueryResultIterator()
            def listContexts(self):
                '''Soprano.NodeIterator Soprano.Util.AsyncModel.listContexts()'''
                return Soprano.NodeIterator()
            def listStatements(self, partial):
                '''Soprano.StatementIterator Soprano.Util.AsyncModel.listStatements(Soprano.Statement partial)'''
                return Soprano.StatementIterator()
            def createBlankNodeAsync(self):
                '''Soprano.Util.AsyncResult Soprano.Util.AsyncModel.createBlankNodeAsync()'''
                return Soprano.Util.AsyncResult()
            def containsAnyStatementAsync(self, statement):
                '''Soprano.Util.AsyncResult Soprano.Util.AsyncModel.containsAnyStatementAsync(Soprano.Statement statement)'''
                return Soprano.Util.AsyncResult()
            def containsAnyStatementAsync(self, subject, predicate, object, context = None):
                '''Soprano.Util.AsyncResult Soprano.Util.AsyncModel.containsAnyStatementAsync(Soprano.Node subject, Soprano.Node predicate, Soprano.Node object, Soprano.Node context = Soprano.Node())'''
                return Soprano.Util.AsyncResult()
            def containsStatementAsync(self, statement):
                '''Soprano.Util.AsyncResult Soprano.Util.AsyncModel.containsStatementAsync(Soprano.Statement statement)'''
                return Soprano.Util.AsyncResult()
            def containsStatementAsync(self, subject, predicate, object, context = None):
                '''Soprano.Util.AsyncResult Soprano.Util.AsyncModel.containsStatementAsync(Soprano.Node subject, Soprano.Node predicate, Soprano.Node object, Soprano.Node context = Soprano.Node())'''
                return Soprano.Util.AsyncResult()
            def executeQueryAsync(self, query, language, userQueryLanguage = QString()):
                '''Soprano.Util.AsyncResult Soprano.Util.AsyncModel.executeQueryAsync(QString query, Soprano.Query.QueryLanguage language, QString userQueryLanguage = QString())'''
                return Soprano.Util.AsyncResult()
            def listContextsAsync(self):
                '''Soprano.Util.AsyncResult Soprano.Util.AsyncModel.listContextsAsync()'''
                return Soprano.Util.AsyncResult()
            def listStatementsAsync(self, statement):
                '''Soprano.Util.AsyncResult Soprano.Util.AsyncModel.listStatementsAsync(Soprano.Statement statement)'''
                return Soprano.Util.AsyncResult()
            def listStatementsAsync(self, subject, predicate, object, context = None):
                '''Soprano.Util.AsyncResult Soprano.Util.AsyncModel.listStatementsAsync(Soprano.Node subject, Soprano.Node predicate, Soprano.Node object, Soprano.Node context = Soprano.Node())'''
                return Soprano.Util.AsyncResult()
            def listStatementsAsync(self):
                '''Soprano.Util.AsyncResult Soprano.Util.AsyncModel.listStatementsAsync()'''
                return Soprano.Util.AsyncResult()
            def statementCountAsync(self):
                '''Soprano.Util.AsyncResult Soprano.Util.AsyncModel.statementCountAsync()'''
                return Soprano.Util.AsyncResult()
            def isEmptyAsync(self):
                '''Soprano.Util.AsyncResult Soprano.Util.AsyncModel.isEmptyAsync()'''
                return Soprano.Util.AsyncResult()
            def removeAllStatementsAsync(self, statement):
                '''Soprano.Util.AsyncResult Soprano.Util.AsyncModel.removeAllStatementsAsync(Soprano.Statement statement)'''
                return Soprano.Util.AsyncResult()
            def removeAllStatementsAsync(self, subject, predicate, object, context = None):
                '''Soprano.Util.AsyncResult Soprano.Util.AsyncModel.removeAllStatementsAsync(Soprano.Node subject, Soprano.Node predicate, Soprano.Node object, Soprano.Node context = Soprano.Node())'''
                return Soprano.Util.AsyncResult()
            def removeStatementsAsync(self, statements):
                '''Soprano.Util.AsyncResult Soprano.Util.AsyncModel.removeStatementsAsync(list-of-Soprano.Statement statements)'''
                return Soprano.Util.AsyncResult()
            def removeStatementAsync(self, statement):
                '''Soprano.Util.AsyncResult Soprano.Util.AsyncModel.removeStatementAsync(Soprano.Statement statement)'''
                return Soprano.Util.AsyncResult()
            def removeStatementAsync(self, subject, predicate, object, context = None):
                '''Soprano.Util.AsyncResult Soprano.Util.AsyncModel.removeStatementAsync(Soprano.Node subject, Soprano.Node predicate, Soprano.Node object, Soprano.Node context = Soprano.Node())'''
                return Soprano.Util.AsyncResult()
            def addStatementsAsync(self, statements):
                '''Soprano.Util.AsyncResult Soprano.Util.AsyncModel.addStatementsAsync(list-of-Soprano.Statement statements)'''
                return Soprano.Util.AsyncResult()
            def addStatementAsync(self, statement):
                '''Soprano.Util.AsyncResult Soprano.Util.AsyncModel.addStatementAsync(Soprano.Statement statement)'''
                return Soprano.Util.AsyncResult()
            def addStatementAsync(self, subject, predicate, object, context = None):
                '''Soprano.Util.AsyncResult Soprano.Util.AsyncModel.addStatementAsync(Soprano.Node subject, Soprano.Node predicate, Soprano.Node object, Soprano.Node context = Soprano.Node())'''
                return Soprano.Util.AsyncResult()
            def mode(self):
                '''Soprano.Util.AsyncModel.AsyncModelMode Soprano.Util.AsyncModel.mode()'''
                return Soprano.Util.AsyncModel.AsyncModelMode()
            def setMode(self, mode):
                '''void Soprano.Util.AsyncModel.setMode(Soprano.Util.AsyncModel.AsyncModelMode mode)'''
    class Inference():
        """"""
        class NodePattern():
            """"""
            def __init__(self):
                '''void Soprano.Inference.NodePattern.__init__()'''
            def __init__(self):
                '''Soprano.Node Soprano.Inference.NodePattern.__init__()'''
                return Soprano.Node()
            def __init__(self, varname):
                '''void Soprano.Inference.NodePattern.__init__(QString varname)'''
            def __init__(self):
                '''Soprano.Inference.NodePattern Soprano.Inference.NodePattern.__init__()'''
                return Soprano.Inference.NodePattern()
            def isValid(self):
                '''bool Soprano.Inference.NodePattern.isValid()'''
                return bool()
            def createSparqlNodePattern(self, bindings):
                '''QString Soprano.Inference.NodePattern.createSparqlNodePattern(Soprano.BindingSet bindings)'''
                return QString()
            def match(self, node):
                '''bool Soprano.Inference.NodePattern.match(Soprano.Node node)'''
                return bool()
            def variableName(self):
                '''QString Soprano.Inference.NodePattern.variableName()'''
                return QString()
            def resource(self):
                '''Soprano.Node Soprano.Inference.NodePattern.resource()'''
                return Soprano.Node()
            def isVariable(self):
                '''bool Soprano.Inference.NodePattern.isVariable()'''
                return bool()
    class BackendSetting():
        """"""
        def __init__(self):
            '''void Soprano.BackendSetting.__init__()'''
        def __init__(self, option):
            '''void Soprano.BackendSetting.__init__(Soprano.BackendOption option)'''
        def __init__(self, s, value_):
            '''void Soprano.BackendSetting.__init__(Soprano.BackendOption s, QVariant value_)'''
        def __init__(self, userOption, value_):
            '''void Soprano.BackendSetting.__init__(QString userOption, QVariant value_)'''
        def __init__(self, other):
            '''void Soprano.BackendSetting.__init__(Soprano.BackendSetting other)'''
        def setValue(self, value):
            '''void Soprano.BackendSetting.setValue(QVariant value)'''
        def value(self):
            '''QVariant Soprano.BackendSetting.value()'''
            return QVariant()
        def userOptionName(self):
            '''QString Soprano.BackendSetting.userOptionName()'''
            return QString()
        def option(self):
            '''Soprano.BackendOption Soprano.BackendSetting.option()'''
            return Soprano.BackendOption()
    class Plugin():
        """"""
        def __init__(self, name):
            '''void Soprano.Plugin.__init__(QString name)'''
        def __init__(self):
            '''Soprano.Plugin Soprano.Plugin.__init__()'''
            return Soprano.Plugin()
        def isAvailable(self):
            '''bool Soprano.Plugin.isAvailable()'''
            return bool()
        def pluginName(self):
            '''QString Soprano.Plugin.pluginName()'''
            return QString()
    class Client():
        """"""
    class Vocabulary():
        """"""
        class NRL():
            """"""
            def NonDefiningProperty(self):
                '''static QUrl Soprano.Vocabulary.NRL.NonDefiningProperty()'''
                return QUrl()
            def DefiningProperty(self):
                '''static QUrl Soprano.Vocabulary.NRL.DefiningProperty()'''
                return QUrl()
            def DiscardableInstanceBase(self):
                '''static QUrl Soprano.Vocabulary.NRL.DiscardableInstanceBase()'''
                return QUrl()
            def viewOn(self):
                '''static QUrl Soprano.Vocabulary.NRL.viewOn()'''
                return QUrl()
            def updatable(self):
                '''static QUrl Soprano.Vocabulary.NRL.updatable()'''
                return QUrl()
            def superGraphOf(self):
                '''static QUrl Soprano.Vocabulary.NRL.superGraphOf()'''
                return QUrl()
            def subGraphOf(self):
                '''static QUrl Soprano.Vocabulary.NRL.subGraphOf()'''
                return QUrl()
            def semanticsDefinedBy(self):
                '''static QUrl Soprano.Vocabulary.NRL.semanticsDefinedBy()'''
                return QUrl()
            def ruleLanguage(self):
                '''static QUrl Soprano.Vocabulary.NRL.ruleLanguage()'''
                return QUrl()
            def rule(self):
                '''static QUrl Soprano.Vocabulary.NRL.rule()'''
                return QUrl()
            def realizes(self):
                '''static QUrl Soprano.Vocabulary.NRL.realizes()'''
                return QUrl()
            def minCardinality(self):
                '''static QUrl Soprano.Vocabulary.NRL.minCardinality()'''
                return QUrl()
            def maxCardinality(self):
                '''static QUrl Soprano.Vocabulary.NRL.maxCardinality()'''
                return QUrl()
            def inverseProperty(self):
                '''static QUrl Soprano.Vocabulary.NRL.inverseProperty()'''
                return QUrl()
            def imports(self):
                '''static QUrl Soprano.Vocabulary.NRL.imports()'''
                return QUrl()
            def hasSpecification(self):
                '''static QUrl Soprano.Vocabulary.NRL.hasSpecification()'''
                return QUrl()
            def hasSemantics(self):
                '''static QUrl Soprano.Vocabulary.NRL.hasSemantics()'''
                return QUrl()
            def graphMetadataFor(self):
                '''static QUrl Soprano.Vocabulary.NRL.graphMetadataFor()'''
                return QUrl()
            def externalRealizer(self):
                '''static QUrl Soprano.Vocabulary.NRL.externalRealizer()'''
                return QUrl()
            def equivalentGraph(self):
                '''static QUrl Soprano.Vocabulary.NRL.equivalentGraph()'''
                return QUrl()
            def coreGraphMetadataFor(self):
                '''static QUrl Soprano.Vocabulary.NRL.coreGraphMetadataFor()'''
                return QUrl()
            def cardinality(self):
                '''static QUrl Soprano.Vocabulary.NRL.cardinality()'''
                return QUrl()
            def ViewSpecification(self):
                '''static QUrl Soprano.Vocabulary.NRL.ViewSpecification()'''
                return QUrl()
            def TransitiveProperty(self):
                '''static QUrl Soprano.Vocabulary.NRL.TransitiveProperty()'''
                return QUrl()
            def SymmetricProperty(self):
                '''static QUrl Soprano.Vocabulary.NRL.SymmetricProperty()'''
                return QUrl()
            def Semantics(self):
                '''static QUrl Soprano.Vocabulary.NRL.Semantics()'''
                return QUrl()
            def Schema(self):
                '''static QUrl Soprano.Vocabulary.NRL.Schema()'''
                return QUrl()
            def RuleViewSpecification(self):
                '''static QUrl Soprano.Vocabulary.NRL.RuleViewSpecification()'''
                return QUrl()
            def ReflexiveProperty(self):
                '''static QUrl Soprano.Vocabulary.NRL.ReflexiveProperty()'''
                return QUrl()
            def Ontology(self):
                '''static QUrl Soprano.Vocabulary.NRL.Ontology()'''
                return QUrl()
            def KnowledgeBase(self):
                '''static QUrl Soprano.Vocabulary.NRL.KnowledgeBase()'''
                return QUrl()
            def InverseFunctionalProperty(self):
                '''static QUrl Soprano.Vocabulary.NRL.InverseFunctionalProperty()'''
                return QUrl()
            def InstanceBase(self):
                '''static QUrl Soprano.Vocabulary.NRL.InstanceBase()'''
                return QUrl()
            def GraphView(self):
                '''static QUrl Soprano.Vocabulary.NRL.GraphView()'''
                return QUrl()
            def GraphMetadata(self):
                '''static QUrl Soprano.Vocabulary.NRL.GraphMetadata()'''
                return QUrl()
            def Graph(self):
                '''static QUrl Soprano.Vocabulary.NRL.Graph()'''
                return QUrl()
            def FunctionalProperty(self):
                '''static QUrl Soprano.Vocabulary.NRL.FunctionalProperty()'''
                return QUrl()
            def ExternalViewSpecification(self):
                '''static QUrl Soprano.Vocabulary.NRL.ExternalViewSpecification()'''
                return QUrl()
            def DocumentGraph(self):
                '''static QUrl Soprano.Vocabulary.NRL.DocumentGraph()'''
                return QUrl()
            def DefaultGraph(self):
                '''static QUrl Soprano.Vocabulary.NRL.DefaultGraph()'''
                return QUrl()
            def Data(self):
                '''static QUrl Soprano.Vocabulary.NRL.Data()'''
                return QUrl()
            def Configuration(self):
                '''static QUrl Soprano.Vocabulary.NRL.Configuration()'''
                return QUrl()
            def AsymmetricProperty(self):
                '''static QUrl Soprano.Vocabulary.NRL.AsymmetricProperty()'''
                return QUrl()
            def nrlNamespace(self):
                '''static QUrl Soprano.Vocabulary.NRL.nrlNamespace()'''
                return QUrl()
    class Util():
        """"""
        class SimpleNodeIterator(Soprano.NodeIterator):
            """"""
            def __init__(self):
                '''void Soprano.Util.SimpleNodeIterator.__init__()'''
            def __init__(self):
                '''list-of-Soprano.Node Soprano.Util.SimpleNodeIterator.__init__()'''
                return [Soprano.Node()]
            def __init__(self):
                '''Soprano.Util.SimpleNodeIterator Soprano.Util.SimpleNodeIterator.__init__()'''
                return Soprano.Util.SimpleNodeIterator()
    class NodeIterator():
        """"""
        def __init__(self):
            '''void Soprano.NodeIterator.__init__()'''
        def __init__(self, sti):
            '''void Soprano.NodeIterator.__init__(Soprano.NodeIterator sti)'''
        def allElements(self):
            '''list-of-Soprano.Node Soprano.NodeIterator.allElements()'''
            return [Soprano.Node()]
        def isValid(self):
            '''bool Soprano.NodeIterator.isValid()'''
            return bool()
        def current(self):
            '''Soprano.Node Soprano.NodeIterator.current()'''
            return Soprano.Node()
        def next(self):
            '''bool Soprano.NodeIterator.next()'''
            return bool()
        def close(self):
            '''void Soprano.NodeIterator.close()'''
        def allNodes(self):
            '''list-of-Soprano.Node Soprano.NodeIterator.allNodes()'''
            return [Soprano.Node()]
    class Inference():
        """"""
        class StatementPattern():
            """"""
            def __init__(self):
                '''void Soprano.Inference.StatementPattern.__init__()'''
            def __init__(self):
                '''Soprano.Inference.NodePattern Soprano.Inference.StatementPattern.__init__()'''
                return Soprano.Inference.NodePattern()
            def __init__(self):
                '''Soprano.Inference.StatementPattern Soprano.Inference.StatementPattern.__init__()'''
                return Soprano.Inference.StatementPattern()
            def isValid(self):
                '''bool Soprano.Inference.StatementPattern.isValid()'''
                return bool()
            def createSparqlGraphPattern(self, bindings):
                '''QString Soprano.Inference.StatementPattern.createSparqlGraphPattern(Soprano.BindingSet bindings)'''
                return QString()
            def match(self):
                '''Soprano.Statement Soprano.Inference.StatementPattern.match()'''
                return Soprano.Statement()
            def objectPattern(self):
                '''Soprano.Inference.NodePattern Soprano.Inference.StatementPattern.objectPattern()'''
                return Soprano.Inference.NodePattern()
            def predicatePattern(self):
                '''Soprano.Inference.NodePattern Soprano.Inference.StatementPattern.predicatePattern()'''
                return Soprano.Inference.NodePattern()
            def subjectPattern(self):
                '''Soprano.Inference.NodePattern Soprano.Inference.StatementPattern.subjectPattern()'''
                return Soprano.Inference.NodePattern()
    class Util():
        """"""
        class DummyModel(Soprano.Model):
            """"""
            def __init__(self):
                '''void Soprano.Util.DummyModel.__init__()'''
            def createBlankNode(self):
                '''Soprano.Node Soprano.Util.DummyModel.createBlankNode()'''
                return Soprano.Node()
            def write(self, os):
                '''Soprano.Error.ErrorCode Soprano.Util.DummyModel.write(QTextStream os)'''
                return Soprano.Error.ErrorCode()
            def statementCount(self):
                '''int Soprano.Util.DummyModel.statementCount()'''
                return int()
            def isEmpty(self):
                '''bool Soprano.Util.DummyModel.isEmpty()'''
                return bool()
            def containsStatement(self, statement):
                '''bool Soprano.Util.DummyModel.containsStatement(Soprano.Statement statement)'''
                return bool()
            def containsStatement(self, subject, predicate, object, context = None):
                '''bool Soprano.Util.DummyModel.containsStatement(Soprano.Node subject, Soprano.Node predicate, Soprano.Node object, Soprano.Node context = Soprano.Node())'''
                return bool()
            def containsAnyStatement(self, statement):
                '''bool Soprano.Util.DummyModel.containsAnyStatement(Soprano.Statement statement)'''
                return bool()
            def containsAnyStatement(self, subject, predicate, object, context = None):
                '''bool Soprano.Util.DummyModel.containsAnyStatement(Soprano.Node subject, Soprano.Node predicate, Soprano.Node object, Soprano.Node context = Soprano.Node())'''
                return bool()
            def executeQuery(self, query, language, userQueryLanguage = QString()):
                '''Soprano.QueryResultIterator Soprano.Util.DummyModel.executeQuery(QString query, Soprano.Query.QueryLanguage language, QString userQueryLanguage = QString())'''
                return Soprano.QueryResultIterator()
            def listContexts(self):
                '''Soprano.NodeIterator Soprano.Util.DummyModel.listContexts()'''
                return Soprano.NodeIterator()
            def listStatements(self, partial):
                '''Soprano.StatementIterator Soprano.Util.DummyModel.listStatements(Soprano.Statement partial)'''
                return Soprano.StatementIterator()
            def listStatements(self, subject, predicate, object, context = None):
                '''Soprano.StatementIterator Soprano.Util.DummyModel.listStatements(Soprano.Node subject, Soprano.Node predicate, Soprano.Node object, Soprano.Node context = Soprano.Node())'''
                return Soprano.StatementIterator()
            def removeAllStatements(self, statement):
                '''Soprano.Error.ErrorCode Soprano.Util.DummyModel.removeAllStatements(Soprano.Statement statement)'''
                return Soprano.Error.ErrorCode()
            def removeStatement(self, statement):
                '''Soprano.Error.ErrorCode Soprano.Util.DummyModel.removeStatement(Soprano.Statement statement)'''
                return Soprano.Error.ErrorCode()
            def removeStatement(self, subject, predicate, object, context = None):
                '''Soprano.Error.ErrorCode Soprano.Util.DummyModel.removeStatement(Soprano.Node subject, Soprano.Node predicate, Soprano.Node object, Soprano.Node context = Soprano.Node())'''
                return Soprano.Error.ErrorCode()
            def addStatement(self, statement):
                '''Soprano.Error.ErrorCode Soprano.Util.DummyModel.addStatement(Soprano.Statement statement)'''
                return Soprano.Error.ErrorCode()
            def addStatement(self, subject, predicate, object, context = None):
                '''Soprano.Error.ErrorCode Soprano.Util.DummyModel.addStatement(Soprano.Node subject, Soprano.Node predicate, Soprano.Node object, Soprano.Node context = Soprano.Node())'''
                return Soprano.Error.ErrorCode()
    class QueryResultIterator():
        """"""
        def __init__(self):
            '''void Soprano.QueryResultIterator.__init__()'''
        def __init__(self):
            '''Soprano.QueryResultIterator Soprano.QueryResultIterator.__init__()'''
            return Soprano.QueryResultIterator()
        def __init__(self, qr):
            '''void Soprano.QueryResultIterator.__init__(Soprano.QueryResultIteratorBackend qr)'''
        def allElements(self):
            '''list-of-Soprano.BindingSet Soprano.QueryResultIterator.allElements()'''
            return [Soprano.BindingSet()]
        def isValid(self):
            '''bool Soprano.QueryResultIterator.isValid()'''
            return bool()
        def current(self):
            '''Soprano.BindingSet Soprano.QueryResultIterator.current()'''
            return Soprano.BindingSet()
        def next(self):
            '''bool Soprano.QueryResultIterator.next()'''
            return bool()
        def close(self):
            '''void Soprano.QueryResultIterator.close()'''
        def iterateStatementsFromBindings(self, subjectBindingName, predicateBindingName, objectBindingName, contextBindingName = QString(), templateStatement = None):
            '''Soprano.StatementIterator Soprano.QueryResultIterator.iterateStatementsFromBindings(QString subjectBindingName, QString predicateBindingName, QString objectBindingName, QString contextBindingName = QString(), Soprano.Statement templateStatement = Soprano.Statement())'''
            return Soprano.StatementIterator()
        def iterateBindings(self, variableName):
            '''Soprano.NodeIterator Soprano.QueryResultIterator.iterateBindings(QString variableName)'''
            return Soprano.NodeIterator()
        def iterateBindings(self, offset):
            '''Soprano.NodeIterator Soprano.QueryResultIterator.iterateBindings(int offset)'''
            return Soprano.NodeIterator()
        def iterateStatements(self):
            '''Soprano.StatementIterator Soprano.QueryResultIterator.iterateStatements()'''
            return Soprano.StatementIterator()
        def allBindings(self):
            '''list-of-Soprano.BindingSet Soprano.QueryResultIterator.allBindings()'''
            return [Soprano.BindingSet()]
        def isBool(self):
            '''bool Soprano.QueryResultIterator.isBool()'''
            return bool()
        def isBinding(self):
            '''bool Soprano.QueryResultIterator.isBinding()'''
            return bool()
        def isGraph(self):
            '''bool Soprano.QueryResultIterator.isGraph()'''
            return bool()
        def bindingNames(self):
            '''QStringList Soprano.QueryResultIterator.bindingNames()'''
            return QStringList()
        def bindingCount(self):
            '''int Soprano.QueryResultIterator.bindingCount()'''
            return int()
        def binding(self, name):
            '''Soprano.Node Soprano.QueryResultIterator.binding(QString name)'''
            return Soprano.Node()
        def binding(self, offset):
            '''Soprano.Node Soprano.QueryResultIterator.binding(int offset)'''
            return Soprano.Node()
        def __getitem__(self, offset):
            '''Soprano.Node Soprano.QueryResultIterator.__getitem__(int offset)'''
            return Soprano.Node()
        def __getitem__(self, name):
            '''Soprano.Node Soprano.QueryResultIterator.__getitem__(QString name)'''
            return Soprano.Node()
        def boolValue(self):
            '''bool Soprano.QueryResultIterator.boolValue()'''
            return bool()
        def currentBindings(self):
            '''Soprano.BindingSet Soprano.QueryResultIterator.currentBindings()'''
            return Soprano.BindingSet()
        def currentStatement(self):
            '''Soprano.Statement Soprano.QueryResultIterator.currentStatement()'''
            return Soprano.Statement()
    class LiteralValue():
        """"""
        def __init__(self):
            '''void Soprano.LiteralValue.__init__()'''
        def __init__(self, other):
            '''void Soprano.LiteralValue.__init__(Soprano.LiteralValue other)'''
        def __init__(self, v):
            '''void Soprano.LiteralValue.__init__(QVariant v)'''
        def __init__(self, i):
            '''void Soprano.LiteralValue.__init__(int i)'''
        def __init__(self, d):
            '''void Soprano.LiteralValue.__init__(float d)'''
        def __init__(self, string):
            '''void Soprano.LiteralValue.__init__(str string)'''
        def __init__(self, string):
            '''void Soprano.LiteralValue.__init__(QLatin1String string)'''
        def __init__(self, string):
            '''void Soprano.LiteralValue.__init__(QString string)'''
        def __init__(self, date):
            '''void Soprano.LiteralValue.__init__(QDate date)'''
        def __init__(self, time):
            '''void Soprano.LiteralValue.__init__(QTime time)'''
        def __init__(self, datetime):
            '''void Soprano.LiteralValue.__init__(QDateTime datetime)'''
        def __init__(self, data):
            '''void Soprano.LiteralValue.__init__(QByteArray data)'''
        def fromVariant(self, value, dataType):
            '''static Soprano.LiteralValue Soprano.LiteralValue.fromVariant(QVariant value, QUrl dataType)'''
            return Soprano.LiteralValue()
        def dataTypeUriFromType(self, type):
            '''static QUrl Soprano.LiteralValue.dataTypeUriFromType(Type type)'''
            return QUrl()
        def typeFromDataTypeUri(self, dataTypeUri):
            '''static Type Soprano.LiteralValue.typeFromDataTypeUri(QUrl dataTypeUri)'''
            return Type()
        def createPlainLiteral(self, value, lang = None):
            '''static Soprano.LiteralValue Soprano.LiteralValue.createPlainLiteral(QString value, Soprano.LanguageTag lang = Soprano.LanguageTag())'''
            return Soprano.LiteralValue()
        def fromString(self, value, type):
            '''static Soprano.LiteralValue Soprano.LiteralValue.fromString(QString value, Type type)'''
            return Soprano.LiteralValue()
        def fromString(self, value, dataTypeUri):
            '''static Soprano.LiteralValue Soprano.LiteralValue.fromString(QString value, QUrl dataTypeUri)'''
            return Soprano.LiteralValue()
        def variant(self):
            '''QVariant Soprano.LiteralValue.variant()'''
            return QVariant()
        def type(self):
            '''Type Soprano.LiteralValue.type()'''
            return Type()
        def language(self):
            '''Soprano.LanguageTag Soprano.LiteralValue.language()'''
            return Soprano.LanguageTag()
        def dataTypeUri(self):
            '''QUrl Soprano.LiteralValue.dataTypeUri()'''
            return QUrl()
        def toByteArray(self):
            '''QByteArray Soprano.LiteralValue.toByteArray()'''
            return QByteArray()
        def toDateTime(self):
            '''QDateTime Soprano.LiteralValue.toDateTime()'''
            return QDateTime()
        def toTime(self):
            '''QTime Soprano.LiteralValue.toTime()'''
            return QTime()
        def toDate(self):
            '''QDate Soprano.LiteralValue.toDate()'''
            return QDate()
        def toString(self):
            '''QString Soprano.LiteralValue.toString()'''
            return QString()
        def toDouble(self):
            '''float Soprano.LiteralValue.toDouble()'''
            return float()
        def toBool(self):
            '''bool Soprano.LiteralValue.toBool()'''
            return bool()
        def toUnsignedInt64(self):
            '''int Soprano.LiteralValue.toUnsignedInt64()'''
            return int()
        def toUnsignedInt(self):
            '''int Soprano.LiteralValue.toUnsignedInt()'''
            return int()
        def toInt64(self):
            '''int Soprano.LiteralValue.toInt64()'''
            return int()
        def toInt(self):
            '''int Soprano.LiteralValue.toInt()'''
            return int()
        def isByteArray(self):
            '''bool Soprano.LiteralValue.isByteArray()'''
            return bool()
        def isDateTime(self):
            '''bool Soprano.LiteralValue.isDateTime()'''
            return bool()
        def isTime(self):
            '''bool Soprano.LiteralValue.isTime()'''
            return bool()
        def isDate(self):
            '''bool Soprano.LiteralValue.isDate()'''
            return bool()
        def isString(self):
            '''bool Soprano.LiteralValue.isString()'''
            return bool()
        def isDouble(self):
            '''bool Soprano.LiteralValue.isDouble()'''
            return bool()
        def isBool(self):
            '''bool Soprano.LiteralValue.isBool()'''
            return bool()
        def isUnsignedInt64(self):
            '''bool Soprano.LiteralValue.isUnsignedInt64()'''
            return bool()
        def isUnsignedInt(self):
            '''bool Soprano.LiteralValue.isUnsignedInt()'''
            return bool()
        def isInt64(self):
            '''bool Soprano.LiteralValue.isInt64()'''
            return bool()
        def isInt(self):
            '''bool Soprano.LiteralValue.isInt()'''
            return bool()
        def isPlain(self):
            '''bool Soprano.LiteralValue.isPlain()'''
            return bool()
        def isValid(self):
            '''bool Soprano.LiteralValue.isValid()'''
            return bool()
        def __ne__(self, other):
            '''bool Soprano.LiteralValue.__ne__(Soprano.LiteralValue other)'''
            return bool()
        def __eq__(self, other):
            '''bool Soprano.LiteralValue.__eq__(Soprano.LiteralValue other)'''
            return bool()
    class Util():
        """"""
        class MutexModel(Soprano.FilterModel):
            """"""
            # Enum Soprano.Util.MutexModel.ProtectionMode
            PlainMultiThreading = 0
            ReadWriteMultiThreading = 0
            ReadWriteSingleThreading = 0
        
            def __init__(self, mode, parent = None):
                '''void Soprano.Util.MutexModel.__init__(Soprano.Util.MutexModel.ProtectionMode mode, Soprano.Model parent = None)'''
            def statementCount(self):
                '''int Soprano.Util.MutexModel.statementCount()'''
                return int()
            def isEmpty(self):
                '''bool Soprano.Util.MutexModel.isEmpty()'''
                return bool()
            def containsAnyStatement(self, statement):
                '''bool Soprano.Util.MutexModel.containsAnyStatement(Soprano.Statement statement)'''
                return bool()
            def containsStatement(self, statement):
                '''bool Soprano.Util.MutexModel.containsStatement(Soprano.Statement statement)'''
                return bool()
            def executeQuery(self, query, language, userQueryLanguage = QString()):
                '''Soprano.QueryResultIterator Soprano.Util.MutexModel.executeQuery(QString query, Soprano.Query.QueryLanguage language, QString userQueryLanguage = QString())'''
                return Soprano.QueryResultIterator()
            def listContexts(self):
                '''Soprano.NodeIterator Soprano.Util.MutexModel.listContexts()'''
                return Soprano.NodeIterator()
            def listStatements(self, partial):
                '''Soprano.StatementIterator Soprano.Util.MutexModel.listStatements(Soprano.Statement partial)'''
                return Soprano.StatementIterator()
            def removeAllStatements(self, statement):
                '''Soprano.Error.ErrorCode Soprano.Util.MutexModel.removeAllStatements(Soprano.Statement statement)'''
                return Soprano.Error.ErrorCode()
            def removeStatement(self, statement):
                '''Soprano.Error.ErrorCode Soprano.Util.MutexModel.removeStatement(Soprano.Statement statement)'''
                return Soprano.Error.ErrorCode()
            def addStatement(self, statement):
                '''Soprano.Error.ErrorCode Soprano.Util.MutexModel.addStatement(Soprano.Statement statement)'''
                return Soprano.Error.ErrorCode()
    class Vocabulary():
        """"""
        class OWL():
            """"""
            def versionInfo(self):
                '''static QUrl Soprano.Vocabulary.OWL.versionInfo()'''
                return QUrl()
            def unionOf(self):
                '''static QUrl Soprano.Vocabulary.OWL.unionOf()'''
                return QUrl()
            def someValuesFrom(self):
                '''static QUrl Soprano.Vocabulary.OWL.someValuesFrom()'''
                return QUrl()
            def sameAs(self):
                '''static QUrl Soprano.Vocabulary.OWL.sameAs()'''
                return QUrl()
            def priorVersion(self):
                '''static QUrl Soprano.Vocabulary.OWL.priorVersion()'''
                return QUrl()
            def oneOf(self):
                '''static QUrl Soprano.Vocabulary.OWL.oneOf()'''
                return QUrl()
            def onProperty(self):
                '''static QUrl Soprano.Vocabulary.OWL.onProperty()'''
                return QUrl()
            def minCardinality(self):
                '''static QUrl Soprano.Vocabulary.OWL.minCardinality()'''
                return QUrl()
            def maxCardinality(self):
                '''static QUrl Soprano.Vocabulary.OWL.maxCardinality()'''
                return QUrl()
            def inverseOf(self):
                '''static QUrl Soprano.Vocabulary.OWL.inverseOf()'''
                return QUrl()
            def intersectionOf(self):
                '''static QUrl Soprano.Vocabulary.OWL.intersectionOf()'''
                return QUrl()
            def incompatibleWith(self):
                '''static QUrl Soprano.Vocabulary.OWL.incompatibleWith()'''
                return QUrl()
            def imports(self):
                '''static QUrl Soprano.Vocabulary.OWL.imports()'''
                return QUrl()
            def hasValue(self):
                '''static QUrl Soprano.Vocabulary.OWL.hasValue()'''
                return QUrl()
            def equivalentProperty(self):
                '''static QUrl Soprano.Vocabulary.OWL.equivalentProperty()'''
                return QUrl()
            def equivalentClass(self):
                '''static QUrl Soprano.Vocabulary.OWL.equivalentClass()'''
                return QUrl()
            def distinctMembers(self):
                '''static QUrl Soprano.Vocabulary.OWL.distinctMembers()'''
                return QUrl()
            def disjointWith(self):
                '''static QUrl Soprano.Vocabulary.OWL.disjointWith()'''
                return QUrl()
            def differentFrom(self):
                '''static QUrl Soprano.Vocabulary.OWL.differentFrom()'''
                return QUrl()
            def complementOf(self):
                '''static QUrl Soprano.Vocabulary.OWL.complementOf()'''
                return QUrl()
            def cardinality(self):
                '''static QUrl Soprano.Vocabulary.OWL.cardinality()'''
                return QUrl()
            def backwardCompatibleWith(self):
                '''static QUrl Soprano.Vocabulary.OWL.backwardCompatibleWith()'''
                return QUrl()
            def allValuesFrom(self):
                '''static QUrl Soprano.Vocabulary.OWL.allValuesFrom()'''
                return QUrl()
            def TransitiveProperty(self):
                '''static QUrl Soprano.Vocabulary.OWL.TransitiveProperty()'''
                return QUrl()
            def Thing(self):
                '''static QUrl Soprano.Vocabulary.OWL.Thing()'''
                return QUrl()
            def SymmetricProperty(self):
                '''static QUrl Soprano.Vocabulary.OWL.SymmetricProperty()'''
                return QUrl()
            def Restriction(self):
                '''static QUrl Soprano.Vocabulary.OWL.Restriction()'''
                return QUrl()
            def OntologyProperty(self):
                '''static QUrl Soprano.Vocabulary.OWL.OntologyProperty()'''
                return QUrl()
            def Ontology(self):
                '''static QUrl Soprano.Vocabulary.OWL.Ontology()'''
                return QUrl()
            def ObjectProperty(self):
                '''static QUrl Soprano.Vocabulary.OWL.ObjectProperty()'''
                return QUrl()
            def Nothing(self):
                '''static QUrl Soprano.Vocabulary.OWL.Nothing()'''
                return QUrl()
            def InverseFunctionalProperty(self):
                '''static QUrl Soprano.Vocabulary.OWL.InverseFunctionalProperty()'''
                return QUrl()
            def FunctionalProperty(self):
                '''static QUrl Soprano.Vocabulary.OWL.FunctionalProperty()'''
                return QUrl()
            def DeprecatedProperty(self):
                '''static QUrl Soprano.Vocabulary.OWL.DeprecatedProperty()'''
                return QUrl()
            def DeprecatedClass(self):
                '''static QUrl Soprano.Vocabulary.OWL.DeprecatedClass()'''
                return QUrl()
            def DatatypeProperty(self):
                '''static QUrl Soprano.Vocabulary.OWL.DatatypeProperty()'''
                return QUrl()
            def DataRange(self):
                '''static QUrl Soprano.Vocabulary.OWL.DataRange()'''
                return QUrl()
            def Class(self):
                '''static QUrl Soprano.Vocabulary.OWL.Class()'''
                return QUrl()
            def AnnotationProperty(self):
                '''static QUrl Soprano.Vocabulary.OWL.AnnotationProperty()'''
                return QUrl()
            def AllDifferent(self):
                '''static QUrl Soprano.Vocabulary.OWL.AllDifferent()'''
                return QUrl()
            def owlNamespace(self):
                '''static QUrl Soprano.Vocabulary.OWL.owlNamespace()'''
                return QUrl()
    class BackendFeatures():
        """"""
        def __init__(self):
            '''Soprano.BackendFeatures Soprano.BackendFeatures.__init__()'''
            return Soprano.BackendFeatures()
        def __init__(self):
            '''int Soprano.BackendFeatures.__init__()'''
            return int()
        def __init__(self):
            '''void Soprano.BackendFeatures.__init__()'''
        def __bool__(self):
            '''int Soprano.BackendFeatures.__bool__()'''
            return int()
        def __ne__(self, f):
            '''bool Soprano.BackendFeatures.__ne__(Soprano.BackendFeatures f)'''
            return bool()
        def __eq__(self, f):
            '''bool Soprano.BackendFeatures.__eq__(Soprano.BackendFeatures f)'''
            return bool()
        def __invert__(self):
            '''Soprano.BackendFeatures Soprano.BackendFeatures.__invert__()'''
            return Soprano.BackendFeatures()
        def __and__(self, mask):
            '''Soprano.BackendFeatures Soprano.BackendFeatures.__and__(int mask)'''
            return Soprano.BackendFeatures()
        def __xor__(self, f):
            '''Soprano.BackendFeatures Soprano.BackendFeatures.__xor__(Soprano.BackendFeatures f)'''
            return Soprano.BackendFeatures()
        def __xor__(self, f):
            '''Soprano.BackendFeatures Soprano.BackendFeatures.__xor__(int f)'''
            return Soprano.BackendFeatures()
        def __or__(self, f):
            '''Soprano.BackendFeatures Soprano.BackendFeatures.__or__(Soprano.BackendFeatures f)'''
            return Soprano.BackendFeatures()
        def __or__(self, f):
            '''Soprano.BackendFeatures Soprano.BackendFeatures.__or__(int f)'''
            return Soprano.BackendFeatures()
        def __int__(self):
            '''int Soprano.BackendFeatures.__int__()'''
            return int()
        def __ixor__(self, f):
            '''Soprano.BackendFeatures Soprano.BackendFeatures.__ixor__(Soprano.BackendFeatures f)'''
            return Soprano.BackendFeatures()
        def __ior__(self, f):
            '''Soprano.BackendFeatures Soprano.BackendFeatures.__ior__(Soprano.BackendFeatures f)'''
            return Soprano.BackendFeatures()
        def __iand__(self, mask):
            '''Soprano.BackendFeatures Soprano.BackendFeatures.__iand__(int mask)'''
            return Soprano.BackendFeatures()
    class Client():
        """"""
        class DBusClient(QObject, Soprano.Error.ErrorCache):
            """"""
            def __init__(self, service = QString(), parent = None):
                '''void Soprano.Client.DBusClient.__init__(QString service = QString(), QObject parent = None)'''
            def removeModel(self, name):
                '''void Soprano.Client.DBusClient.removeModel(QString name)'''
            def createModel(self, name, settings = None):
                '''Soprano.Client.DBusModel Soprano.Client.DBusClient.createModel(QString name, list-of-Soprano.BackendSetting settings = Soprano.BackendSettings())'''
                return Soprano.Client.DBusModel()
            def allModels(self):
                '''QStringList Soprano.Client.DBusClient.allModels()'''
                return QStringList()
            def isValid(self):
                '''bool Soprano.Client.DBusClient.isValid()'''
                return bool()
    class Node():
        """"""
        # Enum Soprano.Node.N3ParserFlag
        NoFlags = 0
        StrictLiteralTypes = 0
        StrictUris = 0
        IgnorePrefixes = 0
    
        # Enum Soprano.Node.Type
        EmptyNode = 0
        ResourceNode = 0
        LiteralNode = 0
        BlankNode = 0
    
        def __init__(self):
            '''void Soprano.Node.__init__()'''
        def __init__(self, uri):
            '''void Soprano.Node.__init__(QUrl uri)'''
        def __init__(self, id):
            '''void Soprano.Node.__init__(QString id)'''
        def __init__(self, value):
            '''void Soprano.Node.__init__(Soprano.LiteralValue value)'''
        def __init__(self, value, language):
            '''void Soprano.Node.__init__(Soprano.LiteralValue value, QString language)'''
        def __init__(self, other):
            '''void Soprano.Node.__init__(Soprano.Node other)'''
        def fromN3Stream(self, stream, flags = None):
            '''static Soprano.Node Soprano.Node.fromN3Stream(QTextStream stream, Soprano.Node.N3ParserFlags flags = Soprano.Node.NoFlags)'''
            return Soprano.Node()
        def fromN3(self, n3, flags = None):
            '''static Soprano.Node Soprano.Node.fromN3(QString n3, Soprano.Node.N3ParserFlags flags = Soprano.Node.NoFlags)'''
            return Soprano.Node()
        def literalToN3(self, literal):
            '''static QString Soprano.Node.literalToN3(Soprano.LiteralValue literal)'''
            return QString()
        def blankToN3(self, blank):
            '''static QString Soprano.Node.blankToN3(QString blank)'''
            return QString()
        def resourceToN3(self, resource):
            '''static QString Soprano.Node.resourceToN3(QUrl resource)'''
            return QString()
        def createLiteralNode(self, value):
            '''static Soprano.Node Soprano.Node.createLiteralNode(Soprano.LiteralValue value)'''
            return Soprano.Node()
        def createLiteralNode(self, value, language):
            '''static Soprano.Node Soprano.Node.createLiteralNode(Soprano.LiteralValue value, QString language)'''
            return Soprano.Node()
        def createBlankNode(self, id):
            '''static Soprano.Node Soprano.Node.createBlankNode(QString id)'''
            return Soprano.Node()
        def createResourceNode(self, uri):
            '''static Soprano.Node Soprano.Node.createResourceNode(QUrl uri)'''
            return Soprano.Node()
        def createEmptyNode(self):
            '''static Soprano.Node Soprano.Node.createEmptyNode()'''
            return Soprano.Node()
        def toN3(self):
            '''QString Soprano.Node.toN3()'''
            return QString()
        def toString(self):
            '''QString Soprano.Node.toString()'''
            return QString()
        def language(self):
            '''QString Soprano.Node.language()'''
            return QString()
        def dataType(self):
            '''QUrl Soprano.Node.dataType()'''
            return QUrl()
        def literal(self):
            '''Soprano.LiteralValue Soprano.Node.literal()'''
            return Soprano.LiteralValue()
        def identifier(self):
            '''QString Soprano.Node.identifier()'''
            return QString()
        def uri(self):
            '''QUrl Soprano.Node.uri()'''
            return QUrl()
        def isBlank(self):
            '''bool Soprano.Node.isBlank()'''
            return bool()
        def isResource(self):
            '''bool Soprano.Node.isResource()'''
            return bool()
        def isLiteral(self):
            '''bool Soprano.Node.isLiteral()'''
            return bool()
        def isValid(self):
            '''bool Soprano.Node.isValid()'''
            return bool()
        def isEmpty(self):
            '''bool Soprano.Node.isEmpty()'''
            return bool()
        def type(self):
            '''Soprano.Node.Type Soprano.Node.type()'''
            return Soprano.Node.Type()
        def matches(self, other):
            '''bool Soprano.Node.matches(Soprano.Node other)'''
            return bool()
        def __ne__(self, other):
            '''bool Soprano.Node.__ne__(Soprano.LiteralValue other)'''
            return bool()
        def __ne__(self, uri):
            '''bool Soprano.Node.__ne__(QUrl uri)'''
            return bool()
        def __ne__(self, other):
            '''bool Soprano.Node.__ne__(Soprano.Node other)'''
            return bool()
        def __eq__(self, other):
            '''bool Soprano.Node.__eq__(Soprano.Node other)'''
            return bool()
        def __eq__(self, uri):
            '''bool Soprano.Node.__eq__(QUrl uri)'''
            return bool()
        def __eq__(self, other):
            '''bool Soprano.Node.__eq__(Soprano.LiteralValue other)'''
            return bool()
    class Inference():
        """"""
        class RuleParser():
            """"""
            def __init__(self):
                '''void Soprano.Inference.RuleParser.__init__()'''
            def clear(self):
                '''void Soprano.Inference.RuleParser.clear()'''
            def prefixes(self):
                '''dict-of-QString-QUrl Soprano.Inference.RuleParser.prefixes()'''
                return dict-of-QString-QUrl()
            def addPrefix(self, qname, uri):
                '''void Soprano.Inference.RuleParser.addPrefix(QString qname, QUrl uri)'''
            def parseRule(self, line):
                '''Soprano.Inference.Rule Soprano.Inference.RuleParser.parseRule(QString line)'''
                return Soprano.Inference.Rule()
            def rules(self):
                '''Soprano.Inference.RuleSet Soprano.Inference.RuleParser.rules()'''
                return Soprano.Inference.RuleSet()
            def parseFile(self, path):
                '''bool Soprano.Inference.RuleParser.parseFile(QString path)'''
                return bool()
    class StatementIterator():
        """"""
        def __init__(self):
            '''void Soprano.StatementIterator.__init__()'''
        def __init__(self, sti):
            '''void Soprano.StatementIterator.__init__(Soprano.StatementIterator sti)'''
        def allElements(self):
            '''list-of-Soprano.Statement Soprano.StatementIterator.allElements()'''
            return [Soprano.Statement()]
        def isValid(self):
            '''bool Soprano.StatementIterator.isValid()'''
            return bool()
        def current(self):
            '''Soprano.Statement Soprano.StatementIterator.current()'''
            return Soprano.Statement()
        def next(self):
            '''bool Soprano.StatementIterator.next()'''
            return bool()
        def close(self):
            '''void Soprano.StatementIterator.close()'''
        def iterateContexts(self):
            '''Soprano.NodeIterator Soprano.StatementIterator.iterateContexts()'''
            return Soprano.NodeIterator()
        def iterateObjects(self):
            '''Soprano.NodeIterator Soprano.StatementIterator.iterateObjects()'''
            return Soprano.NodeIterator()
        def iteratePredicates(self):
            '''Soprano.NodeIterator Soprano.StatementIterator.iteratePredicates()'''
            return Soprano.NodeIterator()
        def iterateSubjects(self):
            '''Soprano.NodeIterator Soprano.StatementIterator.iterateSubjects()'''
            return Soprano.NodeIterator()
        def allStatements(self):
            '''list-of-Soprano.Statement Soprano.StatementIterator.allStatements()'''
            return [Soprano.Statement()]
    class Error():
        """"""
        class Locator():
            """"""
            def __init__(self):
                '''void Soprano.Error.Locator.__init__()'''
            def __init__(self, line, column, byte = None, filename = QString()):
                '''void Soprano.Error.Locator.__init__(int line, int column, int byte = -1, QString filename = QString())'''
            def __init__(self, other):
                '''void Soprano.Error.Locator.__init__(Soprano.Error.Locator other)'''
            def setFileName(self, fileName):
                '''void Soprano.Error.Locator.setFileName(QString fileName)'''
            def setByte(self, byte):
                '''void Soprano.Error.Locator.setByte(int byte)'''
            def setColumn(self, column):
                '''void Soprano.Error.Locator.setColumn(int column)'''
            def setLine(self, line):
                '''void Soprano.Error.Locator.setLine(int line)'''
            def fileName(self):
                '''QString Soprano.Error.Locator.fileName()'''
                return QString()
            def byte(self):
                '''int Soprano.Error.Locator.byte()'''
                return int()
            def column(self):
                '''int Soprano.Error.Locator.column()'''
                return int()
            def line(self):
                '''int Soprano.Error.Locator.line()'''
                return int()
    class Client():
        """"""
        class LocalSocketClient(QObject, Soprano.Error.ErrorCache):
            """"""
            def __init__(self, parent = None):
                '''void Soprano.Client.LocalSocketClient.__init__(QObject parent = None)'''
            def disconnect(self):
                '''void Soprano.Client.LocalSocketClient.disconnect()'''
            def connect(self, name = QString()):
                '''bool Soprano.Client.LocalSocketClient.connect(QString name = QString())'''
                return bool()
            def removeModel(self, name):
                '''void Soprano.Client.LocalSocketClient.removeModel(QString name)'''
            def createModel(self, name, settings = None):
                '''Soprano.Model Soprano.Client.LocalSocketClient.createModel(QString name, list-of-Soprano.BackendSetting settings = QListlt;Soprano.BackendSettinggt;())'''
                return Soprano.Model()
            def isConnected(self):
                '''bool Soprano.Client.LocalSocketClient.isConnected()'''
                return bool()
    class Backend(Soprano.Plugin, Soprano.Error.ErrorCache):
        """"""
        def __init__(self, name):
            '''void Soprano.Backend.__init__(QString name)'''
        def __init__(self):
            '''Soprano.Backend Soprano.Backend.__init__()'''
            return Soprano.Backend()
        def supportsFeatures(self, feature, userFeatures = QStringList()):
            '''bool Soprano.Backend.supportsFeatures(Soprano.BackendFeatures feature, QStringList userFeatures = QStringList())'''
            return bool()
        def supportedUserFeatures(self):
            '''QStringList Soprano.Backend.supportedUserFeatures()'''
            return QStringList()
        def supportedFeatures(self):
            '''abstract Soprano.BackendFeatures Soprano.Backend.supportedFeatures()'''
            return Soprano.BackendFeatures()
        def deleteModelData(self, settings):
            '''abstract bool Soprano.Backend.deleteModelData(list-of-Soprano.BackendSetting settings)'''
            return bool()
        def createModel(self, settings = None):
            '''abstract Soprano.StorageModel Soprano.Backend.createModel(list-of-Soprano.BackendSetting settings = Soprano.BackendSettings())'''
            return Soprano.StorageModel()
    class Node():
        """"""
        class N3ParserFlags():
            """"""
            def __init__(self):
                '''Soprano.Node.N3ParserFlags Soprano.Node.N3ParserFlags.__init__()'''
                return Soprano.Node.N3ParserFlags()
            def __init__(self):
                '''int Soprano.Node.N3ParserFlags.__init__()'''
                return int()
            def __init__(self):
                '''void Soprano.Node.N3ParserFlags.__init__()'''
            def __bool__(self):
                '''int Soprano.Node.N3ParserFlags.__bool__()'''
                return int()
            def __ne__(self, f):
                '''bool Soprano.Node.N3ParserFlags.__ne__(Soprano.Node.N3ParserFlags f)'''
                return bool()
            def __eq__(self, f):
                '''bool Soprano.Node.N3ParserFlags.__eq__(Soprano.Node.N3ParserFlags f)'''
                return bool()
            def __invert__(self):
                '''Soprano.Node.N3ParserFlags Soprano.Node.N3ParserFlags.__invert__()'''
                return Soprano.Node.N3ParserFlags()
            def __and__(self, mask):
                '''Soprano.Node.N3ParserFlags Soprano.Node.N3ParserFlags.__and__(int mask)'''
                return Soprano.Node.N3ParserFlags()
            def __xor__(self, f):
                '''Soprano.Node.N3ParserFlags Soprano.Node.N3ParserFlags.__xor__(Soprano.Node.N3ParserFlags f)'''
                return Soprano.Node.N3ParserFlags()
            def __xor__(self, f):
                '''Soprano.Node.N3ParserFlags Soprano.Node.N3ParserFlags.__xor__(int f)'''
                return Soprano.Node.N3ParserFlags()
            def __or__(self, f):
                '''Soprano.Node.N3ParserFlags Soprano.Node.N3ParserFlags.__or__(Soprano.Node.N3ParserFlags f)'''
                return Soprano.Node.N3ParserFlags()
            def __or__(self, f):
                '''Soprano.Node.N3ParserFlags Soprano.Node.N3ParserFlags.__or__(int f)'''
                return Soprano.Node.N3ParserFlags()
            def __int__(self):
                '''int Soprano.Node.N3ParserFlags.__int__()'''
                return int()
            def __ixor__(self, f):
                '''Soprano.Node.N3ParserFlags Soprano.Node.N3ParserFlags.__ixor__(Soprano.Node.N3ParserFlags f)'''
                return Soprano.Node.N3ParserFlags()
            def __ior__(self, f):
                '''Soprano.Node.N3ParserFlags Soprano.Node.N3ParserFlags.__ior__(Soprano.Node.N3ParserFlags f)'''
                return Soprano.Node.N3ParserFlags()
            def __iand__(self, mask):
                '''Soprano.Node.N3ParserFlags Soprano.Node.N3ParserFlags.__iand__(int mask)'''
                return Soprano.Node.N3ParserFlags()
    class Util():
        """"""
        class AsyncResult(QObject, Soprano.Error.ErrorCache):
            """"""
            def setResult(self, result, error):
                '''void Soprano.Util.AsyncResult.setResult(QVariant result, Soprano.Error.Error error)'''
            def node(self):
                '''Soprano.Node Soprano.Util.AsyncResult.node()'''
                return Soprano.Node()
            def queryResultIterator(self):
                '''Soprano.QueryResultIterator Soprano.Util.AsyncResult.queryResultIterator()'''
                return Soprano.QueryResultIterator()
            def nodeIterator(self):
                '''Soprano.NodeIterator Soprano.Util.AsyncResult.nodeIterator()'''
                return Soprano.NodeIterator()
            def statementIterator(self):
                '''Soprano.StatementIterator Soprano.Util.AsyncResult.statementIterator()'''
                return Soprano.StatementIterator()
            def errorCode(self):
                '''Soprano.Error.ErrorCode Soprano.Util.AsyncResult.errorCode()'''
                return Soprano.Error.ErrorCode()
            def value(self):
                '''QVariant Soprano.Util.AsyncResult.value()'''
                return QVariant()
            def createResult(self):
                '''static Soprano.Util.AsyncResult Soprano.Util.AsyncResult.createResult()'''
                return Soprano.Util.AsyncResult()
            resultReady = pyqtSignal() # void resultReady(Soprano::Util::AsyncResult *) - signal
    class QueryResultIteratorBackend():
        """"""
        def __init__(self):
            '''void Soprano.QueryResultIteratorBackend.__init__()'''
        def __init__(self):
            '''Soprano.QueryResultIteratorBackend Soprano.QueryResultIteratorBackend.__init__()'''
            return Soprano.QueryResultIteratorBackend()
        def close(self):
            '''abstract void Soprano.QueryResultIteratorBackend.close()'''
        def boolValue(self):
            '''abstract bool Soprano.QueryResultIteratorBackend.boolValue()'''
            return bool()
        def isBool(self):
            '''abstract bool Soprano.QueryResultIteratorBackend.isBool()'''
            return bool()
        def isBinding(self):
            '''abstract bool Soprano.QueryResultIteratorBackend.isBinding()'''
            return bool()
        def isGraph(self):
            '''abstract bool Soprano.QueryResultIteratorBackend.isGraph()'''
            return bool()
        def bindingNames(self):
            '''abstract QStringList Soprano.QueryResultIteratorBackend.bindingNames()'''
            return QStringList()
        def bindingCount(self):
            '''abstract int Soprano.QueryResultIteratorBackend.bindingCount()'''
            return int()
        def binding(self, name):
            '''abstract Soprano.Node Soprano.QueryResultIteratorBackend.binding(QString name)'''
            return Soprano.Node()
        def binding(self, offset):
            '''abstract Soprano.Node Soprano.QueryResultIteratorBackend.binding(int offset)'''
            return Soprano.Node()
        def currentStatement(self):
            '''abstract Soprano.Statement Soprano.QueryResultIteratorBackend.currentStatement()'''
            return Soprano.Statement()
        def current(self):
            '''Soprano.BindingSet Soprano.QueryResultIteratorBackend.current()'''
            return Soprano.BindingSet()
        def next(self):
            '''abstract bool Soprano.QueryResultIteratorBackend.next()'''
            return bool()
    class Client():
        """"""
        class DBusNodeIterator(Soprano.NodeIterator):
            """"""
            def __init__(self, serviceName, dbusObject):
                '''void Soprano.Client.DBusNodeIterator.__init__(QString serviceName, QString dbusObject)'''
            def __init__(self):
                '''Soprano.Client.DBusNodeIterator Soprano.Client.DBusNodeIterator.__init__()'''
                return Soprano.Client.DBusNodeIterator()
    class BackendOptions():
        """"""
        def __init__(self):
            '''Soprano.BackendOptions Soprano.BackendOptions.__init__()'''
            return Soprano.BackendOptions()
        def __init__(self):
            '''int Soprano.BackendOptions.__init__()'''
            return int()
        def __init__(self):
            '''void Soprano.BackendOptions.__init__()'''
        def __bool__(self):
            '''int Soprano.BackendOptions.__bool__()'''
            return int()
        def __ne__(self, f):
            '''bool Soprano.BackendOptions.__ne__(Soprano.BackendOptions f)'''
            return bool()
        def __eq__(self, f):
            '''bool Soprano.BackendOptions.__eq__(Soprano.BackendOptions f)'''
            return bool()
        def __invert__(self):
            '''Soprano.BackendOptions Soprano.BackendOptions.__invert__()'''
            return Soprano.BackendOptions()
        def __and__(self, mask):
            '''Soprano.BackendOptions Soprano.BackendOptions.__and__(int mask)'''
            return Soprano.BackendOptions()
        def __xor__(self, f):
            '''Soprano.BackendOptions Soprano.BackendOptions.__xor__(Soprano.BackendOptions f)'''
            return Soprano.BackendOptions()
        def __xor__(self, f):
            '''Soprano.BackendOptions Soprano.BackendOptions.__xor__(int f)'''
            return Soprano.BackendOptions()
        def __or__(self, f):
            '''Soprano.BackendOptions Soprano.BackendOptions.__or__(Soprano.BackendOptions f)'''
            return Soprano.BackendOptions()
        def __or__(self, f):
            '''Soprano.BackendOptions Soprano.BackendOptions.__or__(int f)'''
            return Soprano.BackendOptions()
        def __int__(self):
            '''int Soprano.BackendOptions.__int__()'''
            return int()
        def __ixor__(self, f):
            '''Soprano.BackendOptions Soprano.BackendOptions.__ixor__(Soprano.BackendOptions f)'''
            return Soprano.BackendOptions()
        def __ior__(self, f):
            '''Soprano.BackendOptions Soprano.BackendOptions.__ior__(Soprano.BackendOptions f)'''
            return Soprano.BackendOptions()
        def __iand__(self, mask):
            '''Soprano.BackendOptions Soprano.BackendOptions.__iand__(int mask)'''
            return Soprano.BackendOptions()
    class Server():
        """"""
        class DBusExportModel(Soprano.FilterModel):
            """"""
            def __init__(self, model = None):
                '''void Soprano.Server.DBusExportModel.__init__(Soprano.Model model = None)'''
            def dbusObjectPath(self):
                '''QString Soprano.Server.DBusExportModel.dbusObjectPath()'''
                return QString()
            def unregisterModel(self):
                '''void Soprano.Server.DBusExportModel.unregisterModel()'''
            def registerModel(self, dbusObjectPath):
                '''bool Soprano.Server.DBusExportModel.registerModel(QString dbusObjectPath)'''
                return bool()
    class Query():
        """"""
        class QueryLanguages():
            """"""
            def __init__(self):
                '''Soprano.Query.QueryLanguages Soprano.Query.QueryLanguages.__init__()'''
                return Soprano.Query.QueryLanguages()
            def __init__(self):
                '''int Soprano.Query.QueryLanguages.__init__()'''
                return int()
            def __init__(self):
                '''void Soprano.Query.QueryLanguages.__init__()'''
            def __bool__(self):
                '''int Soprano.Query.QueryLanguages.__bool__()'''
                return int()
            def __ne__(self, f):
                '''bool Soprano.Query.QueryLanguages.__ne__(Soprano.Query.QueryLanguages f)'''
                return bool()
            def __eq__(self, f):
                '''bool Soprano.Query.QueryLanguages.__eq__(Soprano.Query.QueryLanguages f)'''
                return bool()
            def __invert__(self):
                '''Soprano.Query.QueryLanguages Soprano.Query.QueryLanguages.__invert__()'''
                return Soprano.Query.QueryLanguages()
            def __and__(self, mask):
                '''Soprano.Query.QueryLanguages Soprano.Query.QueryLanguages.__and__(int mask)'''
                return Soprano.Query.QueryLanguages()
            def __xor__(self, f):
                '''Soprano.Query.QueryLanguages Soprano.Query.QueryLanguages.__xor__(Soprano.Query.QueryLanguages f)'''
                return Soprano.Query.QueryLanguages()
            def __xor__(self, f):
                '''Soprano.Query.QueryLanguages Soprano.Query.QueryLanguages.__xor__(int f)'''
                return Soprano.Query.QueryLanguages()
            def __or__(self, f):
                '''Soprano.Query.QueryLanguages Soprano.Query.QueryLanguages.__or__(Soprano.Query.QueryLanguages f)'''
                return Soprano.Query.QueryLanguages()
            def __or__(self, f):
                '''Soprano.Query.QueryLanguages Soprano.Query.QueryLanguages.__or__(int f)'''
                return Soprano.Query.QueryLanguages()
            def __int__(self):
                '''int Soprano.Query.QueryLanguages.__int__()'''
                return int()
            def __ixor__(self, f):
                '''Soprano.Query.QueryLanguages Soprano.Query.QueryLanguages.__ixor__(Soprano.Query.QueryLanguages f)'''
                return Soprano.Query.QueryLanguages()
            def __ior__(self, f):
                '''Soprano.Query.QueryLanguages Soprano.Query.QueryLanguages.__ior__(Soprano.Query.QueryLanguages f)'''
                return Soprano.Query.QueryLanguages()
            def __iand__(self, mask):
                '''Soprano.Query.QueryLanguages Soprano.Query.QueryLanguages.__iand__(int mask)'''
                return Soprano.Query.QueryLanguages()
    class Inference():
        """"""
        class InferenceModel(Soprano.FilterModel):
            """"""
            def __init__(self, parent):
                '''void Soprano.Inference.InferenceModel.__init__(Soprano.Model parent)'''
            def setOptimizedQueriesEnabled(self, b):
                '''void Soprano.Inference.InferenceModel.setOptimizedQueriesEnabled(bool b)'''
            def setCompressedSourceStatements(self, b):
                '''void Soprano.Inference.InferenceModel.setCompressedSourceStatements(bool b)'''
            def clearInference(self):
                '''void Soprano.Inference.InferenceModel.clearInference()'''
            def performInference(self):
                '''void Soprano.Inference.InferenceModel.performInference()'''
            def setRules(self, rules):
                '''void Soprano.Inference.InferenceModel.setRules(list-of-Soprano.Inference.Rule rules)'''
            def addRule(self):
                '''Soprano.Inference.Rule Soprano.Inference.InferenceModel.addRule()'''
                return Soprano.Inference.Rule()
            def removeAllStatements(self):
                '''Soprano.Statement Soprano.Inference.InferenceModel.removeAllStatements()'''
                return Soprano.Statement()
            def removeStatement(self):
                '''Soprano.Statement Soprano.Inference.InferenceModel.removeStatement()'''
                return Soprano.Statement()
            def addStatement(self):
                '''Soprano.Statement Soprano.Inference.InferenceModel.addStatement()'''
                return Soprano.Statement()
    class Vocabulary():
        """"""
        class NAO():
            """"""
            def maintainedBy(self):
                '''static QUrl Soprano.Vocabulary.NAO.maintainedBy()'''
                return QUrl()
            def Agent(self):
                '''static QUrl Soprano.Vocabulary.NAO.Agent()'''
                return QUrl()
            def userVisible(self):
                '''static QUrl Soprano.Vocabulary.NAO.userVisible()'''
                return QUrl()
            def isDataGraphFor(self):
                '''static QUrl Soprano.Vocabulary.NAO.isDataGraphFor()'''
                return QUrl()
            def deprecated(self):
                '''static QUrl Soprano.Vocabulary.NAO.deprecated()'''
                return QUrl()
            def version(self):
                '''static QUrl Soprano.Vocabulary.NAO.version()'''
                return QUrl()
            def status(self):
                '''static QUrl Soprano.Vocabulary.NAO.status()'''
                return QUrl()
            def serializationLanguage(self):
                '''static QUrl Soprano.Vocabulary.NAO.serializationLanguage()'''
                return QUrl()
            def scoreParameter(self):
                '''static QUrl Soprano.Vocabulary.NAO.scoreParameter()'''
                return QUrl()
            def score(self):
                '''static QUrl Soprano.Vocabulary.NAO.score()'''
                return QUrl()
            def rating(self):
                '''static QUrl Soprano.Vocabulary.NAO.rating()'''
                return QUrl()
            def prefSymbol(self):
                '''static QUrl Soprano.Vocabulary.NAO.prefSymbol()'''
                return QUrl()
            def prefLabel(self):
                '''static QUrl Soprano.Vocabulary.NAO.prefLabel()'''
                return QUrl()
            def pluralPrefLabel(self):
                '''static QUrl Soprano.Vocabulary.NAO.pluralPrefLabel()'''
                return QUrl()
            def personalIdentifier(self):
                '''static QUrl Soprano.Vocabulary.NAO.personalIdentifier()'''
                return QUrl()
            def numericRating(self):
                '''static QUrl Soprano.Vocabulary.NAO.numericRating()'''
                return QUrl()
            def modified(self):
                '''static QUrl Soprano.Vocabulary.NAO.modified()'''
                return QUrl()
            def lastModified(self):
                '''static QUrl Soprano.Vocabulary.NAO.lastModified()'''
                return QUrl()
            def isTopicOf(self):
                '''static QUrl Soprano.Vocabulary.NAO.isTopicOf()'''
                return QUrl()
            def isTagFor(self):
                '''static QUrl Soprano.Vocabulary.NAO.isTagFor()'''
                return QUrl()
            def isRelated(self):
                '''static QUrl Soprano.Vocabulary.NAO.isRelated()'''
                return QUrl()
            def identifier(self):
                '''static QUrl Soprano.Vocabulary.NAO.identifier()'''
                return QUrl()
            def iconName(self):
                '''static QUrl Soprano.Vocabulary.NAO.iconName()'''
                return QUrl()
            def hasTopic(self):
                '''static QUrl Soprano.Vocabulary.NAO.hasTopic()'''
                return QUrl()
            def hasTag(self):
                '''static QUrl Soprano.Vocabulary.NAO.hasTag()'''
                return QUrl()
            def hasSymbol(self):
                '''static QUrl Soprano.Vocabulary.NAO.hasSymbol()'''
                return QUrl()
            def hasSuperResource(self):
                '''static QUrl Soprano.Vocabulary.NAO.hasSuperResource()'''
                return QUrl()
            def hasSubResource(self):
                '''static QUrl Soprano.Vocabulary.NAO.hasSubResource()'''
                return QUrl()
            def hasDefaultNamespaceAbbreviation(self):
                '''static QUrl Soprano.Vocabulary.NAO.hasDefaultNamespaceAbbreviation()'''
                return QUrl()
            def hasDefaultNamespace(self):
                '''static QUrl Soprano.Vocabulary.NAO.hasDefaultNamespace()'''
                return QUrl()
            def engineeringTool(self):
                '''static QUrl Soprano.Vocabulary.NAO.engineeringTool()'''
                return QUrl()
            def description(self):
                '''static QUrl Soprano.Vocabulary.NAO.description()'''
                return QUrl()
            def creator(self):
                '''static QUrl Soprano.Vocabulary.NAO.creator()'''
                return QUrl()
            def created(self):
                '''static QUrl Soprano.Vocabulary.NAO.created()'''
                return QUrl()
            def contributor(self):
                '''static QUrl Soprano.Vocabulary.NAO.contributor()'''
                return QUrl()
            def annotation(self):
                '''static QUrl Soprano.Vocabulary.NAO.annotation()'''
                return QUrl()
            def altSymbol(self):
                '''static QUrl Soprano.Vocabulary.NAO.altSymbol()'''
                return QUrl()
            def altLabel(self):
                '''static QUrl Soprano.Vocabulary.NAO.altLabel()'''
                return QUrl()
            def Tag(self):
                '''static QUrl Soprano.Vocabulary.NAO.Tag()'''
                return QUrl()
            def Symbol(self):
                '''static QUrl Soprano.Vocabulary.NAO.Symbol()'''
                return QUrl()
            def Party(self):
                '''static QUrl Soprano.Vocabulary.NAO.Party()'''
                return QUrl()
            def FreeDesktopIcon(self):
                '''static QUrl Soprano.Vocabulary.NAO.FreeDesktopIcon()'''
                return QUrl()
            def naoNamespace(self):
                '''static QUrl Soprano.Vocabulary.NAO.naoNamespace()'''
                return QUrl()
    class Client():
        """"""
        class SparqlModel(Soprano.Model):
            """"""
            def __init__(self, host = QString(), port = 80, user = QString(), password = QString()):
                '''void Soprano.Client.SparqlModel.__init__(QString host = QString(), int port = 80, QString user = QString(), QString password = QString())'''
            def listContextsAsync(self):
                '''Soprano.Util.AsyncResult Soprano.Client.SparqlModel.listContextsAsync()'''
                return Soprano.Util.AsyncResult()
            def executeQueryAsync(self, query, language = None, userQueryLanguage = QString()):
                '''Soprano.Util.AsyncResult Soprano.Client.SparqlModel.executeQueryAsync(QString query, Soprano.Query.QueryLanguage language = Soprano.Query.QueryLanguageSparql, QString userQueryLanguage = QString())'''
                return Soprano.Util.AsyncResult()
            def executeQuery(self, query, language = None, userQueryLanguage = QString()):
                '''Soprano.QueryResultIterator Soprano.Client.SparqlModel.executeQuery(QString query, Soprano.Query.QueryLanguage language = Soprano.Query.QueryLanguageSparql, QString userQueryLanguage = QString())'''
                return Soprano.QueryResultIterator()
            def listStatementsAsync(self, statement):
                '''Soprano.Util.AsyncResult Soprano.Client.SparqlModel.listStatementsAsync(Soprano.Statement statement)'''
                return Soprano.Util.AsyncResult()
            def setPath(self, path):
                '''void Soprano.Client.SparqlModel.setPath(QString path)'''
            def createBlankNode(self):
                '''Soprano.Node Soprano.Client.SparqlModel.createBlankNode()'''
                return Soprano.Node()
            def isEmpty(self):
                '''bool Soprano.Client.SparqlModel.isEmpty()'''
                return bool()
            def statementCount(self):
                '''int Soprano.Client.SparqlModel.statementCount()'''
                return int()
            def listStatements(self, partial):
                '''Soprano.StatementIterator Soprano.Client.SparqlModel.listStatements(Soprano.Statement partial)'''
                return Soprano.StatementIterator()
            def containsAnyStatement(self, statement):
                '''bool Soprano.Client.SparqlModel.containsAnyStatement(Soprano.Statement statement)'''
                return bool()
            def containsStatement(self, statement):
                '''bool Soprano.Client.SparqlModel.containsStatement(Soprano.Statement statement)'''
                return bool()
            def listContexts(self):
                '''Soprano.NodeIterator Soprano.Client.SparqlModel.listContexts()'''
                return Soprano.NodeIterator()
            def removeAllStatements(self, statement):
                '''Soprano.Error.ErrorCode Soprano.Client.SparqlModel.removeAllStatements(Soprano.Statement statement)'''
                return Soprano.Error.ErrorCode()
            def removeStatement(self, statement):
                '''Soprano.Error.ErrorCode Soprano.Client.SparqlModel.removeStatement(Soprano.Statement statement)'''
                return Soprano.Error.ErrorCode()
            def addStatement(self, statement):
                '''Soprano.Error.ErrorCode Soprano.Client.SparqlModel.addStatement(Soprano.Statement statement)'''
                return Soprano.Error.ErrorCode()
            def setUser(self, user, password = QString()):
                '''void Soprano.Client.SparqlModel.setUser(QString user, QString password = QString())'''
            def setHost(self, host, port = 80):
                '''void Soprano.Client.SparqlModel.setHost(QString host, int port = 80)'''
    class Util():
        """"""
        class SimpleStatementIterator(Soprano.StatementIterator):
            """"""
            def __init__(self):
                '''void Soprano.Util.SimpleStatementIterator.__init__()'''
            def __init__(self):
                '''list-of-Soprano.Statement Soprano.Util.SimpleStatementIterator.__init__()'''
                return [Soprano.Statement()]
            def __init__(self):
                '''Soprano.Util.SimpleStatementIterator Soprano.Util.SimpleStatementIterator.__init__()'''
                return Soprano.Util.SimpleStatementIterator()
    class Statement():
        """"""
        def __init__(self):
            '''void Soprano.Statement.__init__()'''
        def __init__(self, subject, predicate, object, context = None):
            '''void Soprano.Statement.__init__(Soprano.Node subject, Soprano.Node predicate, Soprano.Node object, Soprano.Node context = Soprano.Node())'''
        def __init__(self, other):
            '''void Soprano.Statement.__init__(Soprano.Statement other)'''
        def setContext(self, context):
            '''void Soprano.Statement.setContext(Soprano.Node context)'''
        def setObject(self, object):
            '''void Soprano.Statement.setObject(Soprano.Node object)'''
        def setPredicate(self, predicate):
            '''void Soprano.Statement.setPredicate(Soprano.Node predicate)'''
        def setSubject(self, subject):
            '''void Soprano.Statement.setSubject(Soprano.Node subject)'''
        def context(self):
            '''Soprano.Node Soprano.Statement.context()'''
            return Soprano.Node()
        def object(self):
            '''Soprano.Node Soprano.Statement.object()'''
            return Soprano.Node()
        def predicate(self):
            '''Soprano.Node Soprano.Statement.predicate()'''
            return Soprano.Node()
        def subject(self):
            '''Soprano.Node Soprano.Statement.subject()'''
            return Soprano.Node()
        def isValid(self):
            '''bool Soprano.Statement.isValid()'''
            return bool()
        def matches(self, other):
            '''bool Soprano.Statement.matches(Soprano.Statement other)'''
            return bool()
        def __ne__(self, other):
            '''bool Soprano.Statement.__ne__(Soprano.Statement other)'''
            return bool()
        def __eq__(self, other):
            '''bool Soprano.Statement.__eq__(Soprano.Statement other)'''
            return bool()
    class Inference():
        """"""
        # Enum Soprano.Inference.StandardRuleSet
        RDFS = 0
        NRL = 0
    
    class Vocabulary():
        """"""
    class Error():
        """"""
        class Error():
            """"""
            def __init__(self):
                '''void Soprano.Error.Error.__init__()'''
            def __init__(self, message, code = None):
                '''void Soprano.Error.Error.__init__(QString message, int code = Soprano.Error.ErrorUnknown)'''
            def __init__(self):
                '''Soprano.Error.Error Soprano.Error.Error.__init__()'''
                return Soprano.Error.Error()
            def toParserError(self):
                '''Soprano.Error.ParserError Soprano.Error.Error.toParserError()'''
                return Soprano.Error.ParserError()
            def isParserError(self):
                '''bool Soprano.Error.Error.isParserError()'''
                return bool()
            def code(self):
                '''int Soprano.Error.Error.code()'''
                return int()
            def message(self):
                '''QString Soprano.Error.Error.message()'''
                return QString()
    class Client():
        """"""
        class DBusQueryResultIterator(Soprano.QueryResultIterator):
            """"""
            def __init__(self, serviceName, dbusObject):
                '''void Soprano.Client.DBusQueryResultIterator.__init__(QString serviceName, QString dbusObject)'''
            def __init__(self):
                '''Soprano.Client.DBusQueryResultIterator Soprano.Client.DBusQueryResultIterator.__init__()'''
                return Soprano.Client.DBusQueryResultIterator()
    class NRLModel(Soprano.FilterModel):
        """"""
        def __init__(self):
            '''void Soprano.NRLModel.__init__()'''
        def __init__(self, parent):
            '''void Soprano.NRLModel.__init__(Soprano.Model parent)'''
        def removeAllStatements(self, statement):
            '''Soprano.Error.ErrorCode Soprano.NRLModel.removeAllStatements(Soprano.Statement statement)'''
            return Soprano.Error.ErrorCode()
        def executeQuery(self, query, language, userQueryLanguage = QString()):
            '''Soprano.QueryResultIterator Soprano.NRLModel.executeQuery(QString query, Soprano.Query.QueryLanguage language, QString userQueryLanguage = QString())'''
            return Soprano.QueryResultIterator()
        def queryPrefixes(self):
            '''dict-of-QString-QUrl Soprano.NRLModel.queryPrefixes()'''
            return dict-of-QString-QUrl()
        def queryPrefixExpansionEnabled(self):
            '''bool Soprano.NRLModel.queryPrefixExpansionEnabled()'''
            return bool()
        def setEnableQueryPrefixExpansion(self, enable):
            '''void Soprano.NRLModel.setEnableQueryPrefixExpansion(bool enable)'''
        def removeGraph(self, graph):
            '''Soprano.Error.ErrorCode Soprano.NRLModel.removeGraph(QUrl graph)'''
            return Soprano.Error.ErrorCode()
        def createGraph(self, type, metadataGraph = None):
            '''QUrl Soprano.NRLModel.createGraph(QUrl type, QUrl metadataGraph = None)'''
            return QUrl()
        def addNrlStatement(self, s):
            '''Soprano.Error.ErrorCode Soprano.NRLModel.addNrlStatement(Soprano.Statement s)'''
            return Soprano.Error.ErrorCode()
        def ignoreContext(self):
            '''bool Soprano.NRLModel.ignoreContext()'''
            return bool()
        def setIgnoreContext(self, b):
            '''void Soprano.NRLModel.setIgnoreContext(bool b)'''
    class Vocabulary():
        """"""
        class Xesam():
            """"""
            def definesGlobalVariable(self):
                '''static QUrl Soprano.Vocabulary.Xesam.definesGlobalVariable()'''
                return QUrl()
            def definesFunction(self):
                '''static QUrl Soprano.Vocabulary.Xesam.definesFunction()'''
                return QUrl()
            def definesClass(self):
                '''static QUrl Soprano.Vocabulary.Xesam.definesClass()'''
                return QUrl()
            def workPostalAddress(self):
                '''static QUrl Soprano.Vocabulary.Xesam.workPostalAddress()'''
                return QUrl()
            def workPhoneNumber(self):
                '''static QUrl Soprano.Vocabulary.Xesam.workPhoneNumber()'''
                return QUrl()
            def workEmailAddress(self):
                '''static QUrl Soprano.Vocabulary.Xesam.workEmailAddress()'''
                return QUrl()
            def wordCount(self):
                '''static QUrl Soprano.Vocabulary.Xesam.wordCount()'''
                return QUrl()
            def width(self):
                '''static QUrl Soprano.Vocabulary.Xesam.width()'''
                return QUrl()
            def whiteBalance(self):
                '''static QUrl Soprano.Vocabulary.Xesam.whiteBalance()'''
                return QUrl()
            def videoCodecType(self):
                '''static QUrl Soprano.Vocabulary.Xesam.videoCodecType()'''
                return QUrl()
            def videoCodec(self):
                '''static QUrl Soprano.Vocabulary.Xesam.videoCodec()'''
                return QUrl()
            def videoBitrate(self):
                '''static QUrl Soprano.Vocabulary.Xesam.videoBitrate()'''
                return QUrl()
            def verticalResolution(self):
                '''static QUrl Soprano.Vocabulary.Xesam.verticalResolution()'''
                return QUrl()
            def version(self):
                '''static QUrl Soprano.Vocabulary.Xesam.version()'''
                return QUrl()
            def usesNamespace(self):
                '''static QUrl Soprano.Vocabulary.Xesam.usesNamespace()'''
                return QUrl()
            def userRating(self):
                '''static QUrl Soprano.Vocabulary.Xesam.userRating()'''
                return QUrl()
            def userKeyword(self):
                '''static QUrl Soprano.Vocabulary.Xesam.userKeyword()'''
                return QUrl()
            def userComment(self):
                '''static QUrl Soprano.Vocabulary.Xesam.userComment()'''
                return QUrl()
            def useCount(self):
                '''static QUrl Soprano.Vocabulary.Xesam.useCount()'''
                return QUrl()
            def url(self):
                '''static QUrl Soprano.Vocabulary.Xesam.url()'''
                return QUrl()
            def trackPeakGain(self):
                '''static QUrl Soprano.Vocabulary.Xesam.trackPeakGain()'''
                return QUrl()
            def trackNumber(self):
                '''static QUrl Soprano.Vocabulary.Xesam.trackNumber()'''
                return QUrl()
            def trackGain(self):
                '''static QUrl Soprano.Vocabulary.Xesam.trackGain()'''
                return QUrl()
            def totalUncompressedSize(self):
                '''static QUrl Soprano.Vocabulary.Xesam.totalUncompressedSize()'''
                return QUrl()
            def totalSpace(self):
                '''static QUrl Soprano.Vocabulary.Xesam.totalSpace()'''
                return QUrl()
            def to(self):
                '''static QUrl Soprano.Vocabulary.Xesam.to()'''
                return QUrl()
            def title(self):
                '''static QUrl Soprano.Vocabulary.Xesam.title()'''
                return QUrl()
            def targetQuality(self):
                '''static QUrl Soprano.Vocabulary.Xesam.targetQuality()'''
                return QUrl()
            def supercedes(self):
                '''static QUrl Soprano.Vocabulary.Xesam.supercedes()'''
                return QUrl()
            def summary(self):
                '''static QUrl Soprano.Vocabulary.Xesam.summary()'''
                return QUrl()
            def subject(self):
                '''static QUrl Soprano.Vocabulary.Xesam.subject()'''
                return QUrl()
            def storageSize(self):
                '''static QUrl Soprano.Vocabulary.Xesam.storageSize()'''
                return QUrl()
            def sourceModified(self):
                '''static QUrl Soprano.Vocabulary.Xesam.sourceModified()'''
                return QUrl()
            def sourceCreated(self):
                '''static QUrl Soprano.Vocabulary.Xesam.sourceCreated()'''
                return QUrl()
            def size(self):
                '''static QUrl Soprano.Vocabulary.Xesam.size()'''
                return QUrl()
            def sha1Hash(self):
                '''static QUrl Soprano.Vocabulary.Xesam.sha1Hash()'''
                return QUrl()
            def setRate(self):
                '''static QUrl Soprano.Vocabulary.Xesam.setRate()'''
                return QUrl()
            def setCount(self):
                '''static QUrl Soprano.Vocabulary.Xesam.setCount()'''
                return QUrl()
            def seenAttachedAs(self):
                '''static QUrl Soprano.Vocabulary.Xesam.seenAttachedAs()'''
                return QUrl()
            def secondaryRecipient(self):
                '''static QUrl Soprano.Vocabulary.Xesam.secondaryRecipient()'''
                return QUrl()
            def sampleDataType(self):
                '''static QUrl Soprano.Vocabulary.Xesam.sampleDataType()'''
                return QUrl()
            def sampleDataBitDepth(self):
                '''static QUrl Soprano.Vocabulary.Xesam.sampleDataBitDepth()'''
                return QUrl()
            def sampleConfiguration(self):
                '''static QUrl Soprano.Vocabulary.Xesam.sampleConfiguration()'''
                return QUrl()
            def rssFeed(self):
                '''static QUrl Soprano.Vocabulary.Xesam.rssFeed()'''
                return QUrl()
            def rowCount(self):
                '''static QUrl Soprano.Vocabulary.Xesam.rowCount()'''
                return QUrl()
            def replyTo(self):
                '''static QUrl Soprano.Vocabulary.Xesam.replyTo()'''
                return QUrl()
            def remoteUser(self):
                '''static QUrl Soprano.Vocabulary.Xesam.remoteUser()'''
                return QUrl()
            def remoteServer(self):
                '''static QUrl Soprano.Vocabulary.Xesam.remoteServer()'''
                return QUrl()
            def remotePort(self):
                '''static QUrl Soprano.Vocabulary.Xesam.remotePort()'''
                return QUrl()
            def remotePassword(self):
                '''static QUrl Soprano.Vocabulary.Xesam.remotePassword()'''
                return QUrl()
            def related(self):
                '''static QUrl Soprano.Vocabulary.Xesam.related()'''
                return QUrl()
            def recipient(self):
                '''static QUrl Soprano.Vocabulary.Xesam.recipient()'''
                return QUrl()
            def receptionTime(self):
                '''static QUrl Soprano.Vocabulary.Xesam.receptionTime()'''
                return QUrl()
            def programmingLanguage(self):
                '''static QUrl Soprano.Vocabulary.Xesam.programmingLanguage()'''
                return QUrl()
            def primaryRecipient(self):
                '''static QUrl Soprano.Vocabulary.Xesam.primaryRecipient()'''
                return QUrl()
            def postalAddress(self):
                '''static QUrl Soprano.Vocabulary.Xesam.postalAddress()'''
                return QUrl()
            def pixelDataType(self):
                '''static QUrl Soprano.Vocabulary.Xesam.pixelDataType()'''
                return QUrl()
            def pixelDataBitDepth(self):
                '''static QUrl Soprano.Vocabulary.Xesam.pixelDataBitDepth()'''
                return QUrl()
            def phoneNumber(self):
                '''static QUrl Soprano.Vocabulary.Xesam.phoneNumber()'''
                return QUrl()
            def personPhoto(self):
                '''static QUrl Soprano.Vocabulary.Xesam.personPhoto()'''
                return QUrl()
            def permissions(self):
                '''static QUrl Soprano.Vocabulary.Xesam.permissions()'''
                return QUrl()
            def performer(self):
                '''static QUrl Soprano.Vocabulary.Xesam.performer()'''
                return QUrl()
            def paragraphCount(self):
                '''static QUrl Soprano.Vocabulary.Xesam.paragraphCount()'''
                return QUrl()
            def pageCount(self):
                '''static QUrl Soprano.Vocabulary.Xesam.pageCount()'''
                return QUrl()
            def owner(self):
                '''static QUrl Soprano.Vocabulary.Xesam.owner()'''
                return QUrl()
            def otherName(self):
                '''static QUrl Soprano.Vocabulary.Xesam.otherName()'''
                return QUrl()
            def originalLocation(self):
                '''static QUrl Soprano.Vocabulary.Xesam.originalLocation()'''
                return QUrl()
            def originURL(self):
                '''static QUrl Soprano.Vocabulary.Xesam.originURL()'''
                return QUrl()
            def orientation(self):
                '''static QUrl Soprano.Vocabulary.Xesam.orientation()'''
                return QUrl()
            def occupiedSpace(self):
                '''static QUrl Soprano.Vocabulary.Xesam.occupiedSpace()'''
                return QUrl()
            def newsGroup(self):
                '''static QUrl Soprano.Vocabulary.Xesam.newsGroup()'''
                return QUrl()
            def name(self):
                '''static QUrl Soprano.Vocabulary.Xesam.name()'''
                return QUrl()
            def mountPoint(self):
                '''static QUrl Soprano.Vocabulary.Xesam.mountPoint()'''
                return QUrl()
            def mimeType(self):
                '''static QUrl Soprano.Vocabulary.Xesam.mimeType()'''
                return QUrl()
            def meteringMode(self):
                '''static QUrl Soprano.Vocabulary.Xesam.meteringMode()'''
                return QUrl()
            def mergeConflict(self):
                '''static QUrl Soprano.Vocabulary.Xesam.mergeConflict()'''
                return QUrl()
            def mediaDuration(self):
                '''static QUrl Soprano.Vocabulary.Xesam.mediaDuration()'''
                return QUrl()
            def mediaCodecType(self):
                '''static QUrl Soprano.Vocabulary.Xesam.mediaCodecType()'''
                return QUrl()
            def mediaCodec(self):
                '''static QUrl Soprano.Vocabulary.Xesam.mediaCodec()'''
                return QUrl()
            def mediaBitrate(self):
                '''static QUrl Soprano.Vocabulary.Xesam.mediaBitrate()'''
                return QUrl()
            def md5Hash(self):
                '''static QUrl Soprano.Vocabulary.Xesam.md5Hash()'''
                return QUrl()
            def markupCharacterCount(self):
                '''static QUrl Soprano.Vocabulary.Xesam.markupCharacterCount()'''
                return QUrl()
            def maintainer(self):
                '''static QUrl Soprano.Vocabulary.Xesam.maintainer()'''
                return QUrl()
            def mailingPostalAddress(self):
                '''static QUrl Soprano.Vocabulary.Xesam.mailingPostalAddress()'''
                return QUrl()
            def mailingList(self):
                '''static QUrl Soprano.Vocabulary.Xesam.mailingList()'''
                return QUrl()
            def lyricist(self):
                '''static QUrl Soprano.Vocabulary.Xesam.lyricist()'''
                return QUrl()
            def localRevision(self):
                '''static QUrl Soprano.Vocabulary.Xesam.localRevision()'''
                return QUrl()
            def links(self):
                '''static QUrl Soprano.Vocabulary.Xesam.links()'''
                return QUrl()
            def lineCount(self):
                '''static QUrl Soprano.Vocabulary.Xesam.lineCount()'''
                return QUrl()
            def licenseType(self):
                '''static QUrl Soprano.Vocabulary.Xesam.licenseType()'''
                return QUrl()
            def license(self):
                '''static QUrl Soprano.Vocabulary.Xesam.license()'''
                return QUrl()
            def legal(self):
                '''static QUrl Soprano.Vocabulary.Xesam.legal()'''
                return QUrl()
            def lastUsed(self):
                '''static QUrl Soprano.Vocabulary.Xesam.lastUsed()'''
                return QUrl()
            def lastRefreshed(self):
                '''static QUrl Soprano.Vocabulary.Xesam.lastRefreshed()'''
                return QUrl()
            def language(self):
                '''static QUrl Soprano.Vocabulary.Xesam.language()'''
                return QUrl()
            def knows(self):
                '''static QUrl Soprano.Vocabulary.Xesam.knows()'''
                return QUrl()
            def keyword(self):
                '''static QUrl Soprano.Vocabulary.Xesam.keyword()'''
                return QUrl()
            def jabberContactMedium(self):
                '''static QUrl Soprano.Vocabulary.Xesam.jabberContactMedium()'''
                return QUrl()
            def isoEquivalent(self):
                '''static QUrl Soprano.Vocabulary.Xesam.isoEquivalent()'''
                return QUrl()
            def isSourceEncrypted(self):
                '''static QUrl Soprano.Vocabulary.Xesam.isSourceEncrypted()'''
                return QUrl()
            def isRead(self):
                '''static QUrl Soprano.Vocabulary.Xesam.isRead()'''
                return QUrl()
            def isPublicChannel(self):
                '''static QUrl Soprano.Vocabulary.Xesam.isPublicChannel()'''
                return QUrl()
            def isInProgress(self):
                '''static QUrl Soprano.Vocabulary.Xesam.isInProgress()'''
                return QUrl()
            def isImportant(self):
                '''static QUrl Soprano.Vocabulary.Xesam.isImportant()'''
                return QUrl()
            def isEncrypted(self):
                '''static QUrl Soprano.Vocabulary.Xesam.isEncrypted()'''
                return QUrl()
            def isContentEncrypted(self):
                '''static QUrl Soprano.Vocabulary.Xesam.isContentEncrypted()'''
                return QUrl()
            def ircContactMedium(self):
                '''static QUrl Soprano.Vocabulary.Xesam.ircContactMedium()'''
                return QUrl()
            def interlaceMode(self):
                '''static QUrl Soprano.Vocabulary.Xesam.interlaceMode()'''
                return QUrl()
            def interest(self):
                '''static QUrl Soprano.Vocabulary.Xesam.interest()'''
                return QUrl()
            def inReplyTo(self):
                '''static QUrl Soprano.Vocabulary.Xesam.inReplyTo()'''
                return QUrl()
            def imContactMedium(self):
                '''static QUrl Soprano.Vocabulary.Xesam.imContactMedium()'''
                return QUrl()
            def id(self):
                '''static QUrl Soprano.Vocabulary.Xesam.id()'''
                return QUrl()
            def horizontalResolution(self):
                '''static QUrl Soprano.Vocabulary.Xesam.horizontalResolution()'''
                return QUrl()
            def honorificSuffix(self):
                '''static QUrl Soprano.Vocabulary.Xesam.honorificSuffix()'''
                return QUrl()
            def honorificPrefix(self):
                '''static QUrl Soprano.Vocabulary.Xesam.honorificPrefix()'''
                return QUrl()
            def homepageContactURL(self):
                '''static QUrl Soprano.Vocabulary.Xesam.homepageContactURL()'''
                return QUrl()
            def homePostalAddress(self):
                '''static QUrl Soprano.Vocabulary.Xesam.homePostalAddress()'''
                return QUrl()
            def homePhoneNumber(self):
                '''static QUrl Soprano.Vocabulary.Xesam.homePhoneNumber()'''
                return QUrl()
            def homeEmailAddress(self):
                '''static QUrl Soprano.Vocabulary.Xesam.homeEmailAddress()'''
                return QUrl()
            def height(self):
                '''static QUrl Soprano.Vocabulary.Xesam.height()'''
                return QUrl()
            def group(self):
                '''static QUrl Soprano.Vocabulary.Xesam.group()'''
                return QUrl()
            def givenName(self):
                '''static QUrl Soprano.Vocabulary.Xesam.givenName()'''
                return QUrl()
            def genre(self):
                '''static QUrl Soprano.Vocabulary.Xesam.genre()'''
                return QUrl()
            def generatorOptions(self):
                '''static QUrl Soprano.Vocabulary.Xesam.generatorOptions()'''
                return QUrl()
            def generator(self):
                '''static QUrl Soprano.Vocabulary.Xesam.generator()'''
                return QUrl()
            def gender(self):
                '''static QUrl Soprano.Vocabulary.Xesam.gender()'''
                return QUrl()
            def freeSpace(self):
                '''static QUrl Soprano.Vocabulary.Xesam.freeSpace()'''
                return QUrl()
            def frameRate(self):
                '''static QUrl Soprano.Vocabulary.Xesam.frameRate()'''
                return QUrl()
            def frameCount(self):
                '''static QUrl Soprano.Vocabulary.Xesam.frameCount()'''
                return QUrl()
            def formatSubtype(self):
                '''static QUrl Soprano.Vocabulary.Xesam.formatSubtype()'''
                return QUrl()
            def focusDistance(self):
                '''static QUrl Soprano.Vocabulary.Xesam.focusDistance()'''
                return QUrl()
            def focalLength(self):
                '''static QUrl Soprano.Vocabulary.Xesam.focalLength()'''
                return QUrl()
            def flashUsed(self):
                '''static QUrl Soprano.Vocabulary.Xesam.flashUsed()'''
                return QUrl()
            def firstUsed(self):
                '''static QUrl Soprano.Vocabulary.Xesam.firstUsed()'''
                return QUrl()
            def fingerprint(self):
                '''static QUrl Soprano.Vocabulary.Xesam.fingerprint()'''
                return QUrl()
            def fileSystemType(self):
                '''static QUrl Soprano.Vocabulary.Xesam.fileSystemType()'''
                return QUrl()
            def fileExtension(self):
                '''static QUrl Soprano.Vocabulary.Xesam.fileExtension()'''
                return QUrl()
            def faxPhoneNumber(self):
                '''static QUrl Soprano.Vocabulary.Xesam.faxPhoneNumber()'''
                return QUrl()
            def familyName(self):
                '''static QUrl Soprano.Vocabulary.Xesam.familyName()'''
                return QUrl()
            def exposureTime(self):
                '''static QUrl Soprano.Vocabulary.Xesam.exposureTime()'''
                return QUrl()
            def exposureProgram(self):
                '''static QUrl Soprano.Vocabulary.Xesam.exposureProgram()'''
                return QUrl()
            def exposureBias(self):
                '''static QUrl Soprano.Vocabulary.Xesam.exposureBias()'''
                return QUrl()
            def emailAddress(self):
                '''static QUrl Soprano.Vocabulary.Xesam.emailAddress()'''
                return QUrl()
            def documentCategory(self):
                '''static QUrl Soprano.Vocabulary.Xesam.documentCategory()'''
                return QUrl()
            def disclaimer(self):
                '''static QUrl Soprano.Vocabulary.Xesam.disclaimer()'''
                return QUrl()
            def discNumber(self):
                '''static QUrl Soprano.Vocabulary.Xesam.discNumber()'''
                return QUrl()
            def description(self):
                '''static QUrl Soprano.Vocabulary.Xesam.description()'''
                return QUrl()
            def derivedFrom(self):
                '''static QUrl Soprano.Vocabulary.Xesam.derivedFrom()'''
                return QUrl()
            def depends(self):
                '''static QUrl Soprano.Vocabulary.Xesam.depends()'''
                return QUrl()
            def deletionTime(self):
                '''static QUrl Soprano.Vocabulary.Xesam.deletionTime()'''
                return QUrl()
            def creator(self):
                '''static QUrl Soprano.Vocabulary.Xesam.creator()'''
                return QUrl()
            def copyright(self):
                '''static QUrl Soprano.Vocabulary.Xesam.copyright()'''
                return QUrl()
            def contributor(self):
                '''static QUrl Soprano.Vocabulary.Xesam.contributor()'''
                return QUrl()
            def contentType(self):
                '''static QUrl Soprano.Vocabulary.Xesam.contentType()'''
                return QUrl()
            def contentModified(self):
                '''static QUrl Soprano.Vocabulary.Xesam.contentModified()'''
                return QUrl()
            def contentKeyword(self):
                '''static QUrl Soprano.Vocabulary.Xesam.contentKeyword()'''
                return QUrl()
            def contentCreated(self):
                '''static QUrl Soprano.Vocabulary.Xesam.contentCreated()'''
                return QUrl()
            def contentComment(self):
                '''static QUrl Soprano.Vocabulary.Xesam.contentComment()'''
                return QUrl()
            def contains(self):
                '''static QUrl Soprano.Vocabulary.Xesam.contains()'''
                return QUrl()
            def contactURL(self):
                '''static QUrl Soprano.Vocabulary.Xesam.contactURL()'''
                return QUrl()
            def contactNick(self):
                '''static QUrl Soprano.Vocabulary.Xesam.contactNick()'''
                return QUrl()
            def contactMedium(self):
                '''static QUrl Soprano.Vocabulary.Xesam.contactMedium()'''
                return QUrl()
            def conflicts(self):
                '''static QUrl Soprano.Vocabulary.Xesam.conflicts()'''
                return QUrl()
            def compressionLevel(self):
                '''static QUrl Soprano.Vocabulary.Xesam.compressionLevel()'''
                return QUrl()
            def compressionAlgorithm(self):
                '''static QUrl Soprano.Vocabulary.Xesam.compressionAlgorithm()'''
                return QUrl()
            def composer(self):
                '''static QUrl Soprano.Vocabulary.Xesam.composer()'''
                return QUrl()
            def communicationChannel(self):
                '''static QUrl Soprano.Vocabulary.Xesam.communicationChannel()'''
                return QUrl()
            def commitDiff(self):
                '''static QUrl Soprano.Vocabulary.Xesam.commitDiff()'''
                return QUrl()
            def commentCharacterCount(self):
                '''static QUrl Soprano.Vocabulary.Xesam.commentCharacterCount()'''
                return QUrl()
            def comment(self):
                '''static QUrl Soprano.Vocabulary.Xesam.comment()'''
                return QUrl()
            def columnCount(self):
                '''static QUrl Soprano.Vocabulary.Xesam.columnCount()'''
                return QUrl()
            def colorSpace(self):
                '''static QUrl Soprano.Vocabulary.Xesam.colorSpace()'''
                return QUrl()
            def colorCount(self):
                '''static QUrl Soprano.Vocabulary.Xesam.colorCount()'''
                return QUrl()
            def chatRoom(self):
                '''static QUrl Soprano.Vocabulary.Xesam.chatRoom()'''
                return QUrl()
            def charset(self):
                '''static QUrl Soprano.Vocabulary.Xesam.charset()'''
                return QUrl()
            def characterCount(self):
                '''static QUrl Soprano.Vocabulary.Xesam.characterCount()'''
                return QUrl()
            def changeCommitter(self):
                '''static QUrl Soprano.Vocabulary.Xesam.changeCommitter()'''
                return QUrl()
            def changeCommitTime(self):
                '''static QUrl Soprano.Vocabulary.Xesam.changeCommitTime()'''
                return QUrl()
            def cellPhoneNumber(self):
                '''static QUrl Soprano.Vocabulary.Xesam.cellPhoneNumber()'''
                return QUrl()
            def ccdWidth(self):
                '''static QUrl Soprano.Vocabulary.Xesam.ccdWidth()'''
                return QUrl()
            def cc(self):
                '''static QUrl Soprano.Vocabulary.Xesam.cc()'''
                return QUrl()
            def cameraModel(self):
                '''static QUrl Soprano.Vocabulary.Xesam.cameraModel()'''
                return QUrl()
            def cameraManufacturer(self):
                '''static QUrl Soprano.Vocabulary.Xesam.cameraManufacturer()'''
                return QUrl()
            def blogContactURL(self):
                '''static QUrl Soprano.Vocabulary.Xesam.blogContactURL()'''
                return QUrl()
            def birthDate(self):
                '''static QUrl Soprano.Vocabulary.Xesam.birthDate()'''
                return QUrl()
            def bcc(self):
                '''static QUrl Soprano.Vocabulary.Xesam.bcc()'''
                return QUrl()
            def baseRevisionID(self):
                '''static QUrl Soprano.Vocabulary.Xesam.baseRevisionID()'''
                return QUrl()
            def autoRating(self):
                '''static QUrl Soprano.Vocabulary.Xesam.autoRating()'''
                return QUrl()
            def author(self):
                '''static QUrl Soprano.Vocabulary.Xesam.author()'''
                return QUrl()
            def audioSampleRate(self):
                '''static QUrl Soprano.Vocabulary.Xesam.audioSampleRate()'''
                return QUrl()
            def audioSampleDataType(self):
                '''static QUrl Soprano.Vocabulary.Xesam.audioSampleDataType()'''
                return QUrl()
            def audioSampleCount(self):
                '''static QUrl Soprano.Vocabulary.Xesam.audioSampleCount()'''
                return QUrl()
            def audioSampleBitDepth(self):
                '''static QUrl Soprano.Vocabulary.Xesam.audioSampleBitDepth()'''
                return QUrl()
            def audioCodecType(self):
                '''static QUrl Soprano.Vocabulary.Xesam.audioCodecType()'''
                return QUrl()
            def audioCodec(self):
                '''static QUrl Soprano.Vocabulary.Xesam.audioCodec()'''
                return QUrl()
            def audioChannels(self):
                '''static QUrl Soprano.Vocabulary.Xesam.audioChannels()'''
                return QUrl()
            def audioBitrate(self):
                '''static QUrl Soprano.Vocabulary.Xesam.audioBitrate()'''
                return QUrl()
            def audioBPM(self):
                '''static QUrl Soprano.Vocabulary.Xesam.audioBPM()'''
                return QUrl()
            def attachmentEncoding(self):
                '''static QUrl Soprano.Vocabulary.Xesam.attachmentEncoding()'''
                return QUrl()
            def aspectRatio(self):
                '''static QUrl Soprano.Vocabulary.Xesam.aspectRatio()'''
                return QUrl()
            def asText(self):
                '''static QUrl Soprano.Vocabulary.Xesam.asText()'''
                return QUrl()
            def artist(self):
                '''static QUrl Soprano.Vocabulary.Xesam.artist()'''
                return QUrl()
            def aperture(self):
                '''static QUrl Soprano.Vocabulary.Xesam.aperture()'''
                return QUrl()
            def albumTrackCount(self):
                '''static QUrl Soprano.Vocabulary.Xesam.albumTrackCount()'''
                return QUrl()
            def albumPeakGain(self):
                '''static QUrl Soprano.Vocabulary.Xesam.albumPeakGain()'''
                return QUrl()
            def albumGain(self):
                '''static QUrl Soprano.Vocabulary.Xesam.albumGain()'''
                return QUrl()
            def albumArtist(self):
                '''static QUrl Soprano.Vocabulary.Xesam.albumArtist()'''
                return QUrl()
            def album(self):
                '''static QUrl Soprano.Vocabulary.Xesam.album()'''
                return QUrl()
            def acl(self):
                '''static QUrl Soprano.Vocabulary.Xesam.acl()'''
                return QUrl()
            def XML(self):
                '''static QUrl Soprano.Vocabulary.Xesam.XML()'''
                return QUrl()
            def Visual(self):
                '''static QUrl Soprano.Vocabulary.Xesam.Visual()'''
                return QUrl()
            def Video(self):
                '''static QUrl Soprano.Vocabulary.Xesam.Video()'''
                return QUrl()
            def UncategorizedText(self):
                '''static QUrl Soprano.Vocabulary.Xesam.UncategorizedText()'''
                return QUrl()
            def TextDocument(self):
                '''static QUrl Soprano.Vocabulary.Xesam.TextDocument()'''
                return QUrl()
            def Text(self):
                '''static QUrl Soprano.Vocabulary.Xesam.Text()'''
                return QUrl()
            def Tag(self):
                '''static QUrl Soprano.Vocabulary.Xesam.Tag()'''
                return QUrl()
            def SystemResource(self):
                '''static QUrl Soprano.Vocabulary.Xesam.SystemResource()'''
                return QUrl()
            def Spreadsheet(self):
                '''static QUrl Soprano.Vocabulary.Xesam.Spreadsheet()'''
                return QUrl()
            def SourceCode(self):
                '''static QUrl Soprano.Vocabulary.Xesam.SourceCode()'''
                return QUrl()
            def Source(self):
                '''static QUrl Soprano.Vocabulary.Xesam.Source()'''
                return QUrl()
            def SoftwarePackage(self):
                '''static QUrl Soprano.Vocabulary.Xesam.SoftwarePackage()'''
                return QUrl()
            def RevisionControlledRepository(self):
                '''static QUrl Soprano.Vocabulary.Xesam.RevisionControlledRepository()'''
                return QUrl()
            def RevisionControlledFile(self):
                '''static QUrl Soprano.Vocabulary.Xesam.RevisionControlledFile()'''
                return QUrl()
            def RemoteResource(self):
                '''static QUrl Soprano.Vocabulary.Xesam.RemoteResource()'''
                return QUrl()
            def RemoteMessageboxMessage(self):
                '''static QUrl Soprano.Vocabulary.Xesam.RemoteMessageboxMessage()'''
                return QUrl()
            def RemoteFile(self):
                '''static QUrl Soprano.Vocabulary.Xesam.RemoteFile()'''
                return QUrl()
            def RSSMessage(self):
                '''static QUrl Soprano.Vocabulary.Xesam.RSSMessage()'''
                return QUrl()
            def RSSFeed(self):
                '''static QUrl Soprano.Vocabulary.Xesam.RSSFeed()'''
                return QUrl()
            def Project(self):
                '''static QUrl Soprano.Vocabulary.Xesam.Project()'''
                return QUrl()
            def Presentation(self):
                '''static QUrl Soprano.Vocabulary.Xesam.Presentation()'''
                return QUrl()
            def Photo(self):
                '''static QUrl Soprano.Vocabulary.Xesam.Photo()'''
                return QUrl()
            def PersonalEmail(self):
                '''static QUrl Soprano.Vocabulary.Xesam.PersonalEmail()'''
                return QUrl()
            def Person(self):
                '''static QUrl Soprano.Vocabulary.Xesam.Person()'''
                return QUrl()
            def POP3Message(self):
                '''static QUrl Soprano.Vocabulary.Xesam.POP3Message()'''
                return QUrl()
            def Organization(self):
                '''static QUrl Soprano.Vocabulary.Xesam.Organization()'''
                return QUrl()
            def OfflineMedia(self):
                '''static QUrl Soprano.Vocabulary.Xesam.OfflineMedia()'''
                return QUrl()
            def NewsGroupEmail(self):
                '''static QUrl Soprano.Vocabulary.Xesam.NewsGroupEmail()'''
                return QUrl()
            def NewsGroup(self):
                '''static QUrl Soprano.Vocabulary.Xesam.NewsGroup()'''
                return QUrl()
            def Music(self):
                '''static QUrl Soprano.Vocabulary.Xesam.Music()'''
                return QUrl()
            def MessageboxMessage(self):
                '''static QUrl Soprano.Vocabulary.Xesam.MessageboxMessage()'''
                return QUrl()
            def Message(self):
                '''static QUrl Soprano.Vocabulary.Xesam.Message()'''
                return QUrl()
            def MediaList(self):
                '''static QUrl Soprano.Vocabulary.Xesam.MediaList()'''
                return QUrl()
            def Media(self):
                '''static QUrl Soprano.Vocabulary.Xesam.Media()'''
                return QUrl()
            def MailingListEmail(self):
                '''static QUrl Soprano.Vocabulary.Xesam.MailingListEmail()'''
                return QUrl()
            def MailingList(self):
                '''static QUrl Soprano.Vocabulary.Xesam.MailingList()'''
                return QUrl()
            def Image(self):
                '''static QUrl Soprano.Vocabulary.Xesam.Image()'''
                return QUrl()
            def IMMessage(self):
                '''static QUrl Soprano.Vocabulary.Xesam.IMMessage()'''
                return QUrl()
            def IMAP4Message(self):
                '''static QUrl Soprano.Vocabulary.Xesam.IMAP4Message()'''
                return QUrl()
            def Folder(self):
                '''static QUrl Soprano.Vocabulary.Xesam.Folder()'''
                return QUrl()
            def Filelike(self):
                '''static QUrl Soprano.Vocabulary.Xesam.Filelike()'''
                return QUrl()
            def FileSystem(self):
                '''static QUrl Soprano.Vocabulary.Xesam.FileSystem()'''
                return QUrl()
            def File(self):
                '''static QUrl Soprano.Vocabulary.Xesam.File()'''
                return QUrl()
            def EmbeddedObject(self):
                '''static QUrl Soprano.Vocabulary.Xesam.EmbeddedObject()'''
                return QUrl()
            def EmailAttachment(self):
                '''static QUrl Soprano.Vocabulary.Xesam.EmailAttachment()'''
                return QUrl()
            def Email(self):
                '''static QUrl Soprano.Vocabulary.Xesam.Email()'''
                return QUrl()
            def Documentation(self):
                '''static QUrl Soprano.Vocabulary.Xesam.Documentation()'''
                return QUrl()
            def Document(self):
                '''static QUrl Soprano.Vocabulary.Xesam.Document()'''
                return QUrl()
            def DeletedFile(self):
                '''static QUrl Soprano.Vocabulary.Xesam.DeletedFile()'''
                return QUrl()
            def DataObject(self):
                '''static QUrl Soprano.Vocabulary.Xesam.DataObject()'''
                return QUrl()
            def Content(self):
                '''static QUrl Soprano.Vocabulary.Xesam.Content()'''
                return QUrl()
            def ContactGroup(self):
                '''static QUrl Soprano.Vocabulary.Xesam.ContactGroup()'''
                return QUrl()
            def Contact(self):
                '''static QUrl Soprano.Vocabulary.Xesam.Contact()'''
                return QUrl()
            def CommunicationChannel(self):
                '''static QUrl Soprano.Vocabulary.Xesam.CommunicationChannel()'''
                return QUrl()
            def Bookmark(self):
                '''static QUrl Soprano.Vocabulary.Xesam.Bookmark()'''
                return QUrl()
            def BlockDevice(self):
                '''static QUrl Soprano.Vocabulary.Xesam.BlockDevice()'''
                return QUrl()
            def AudioList(self):
                '''static QUrl Soprano.Vocabulary.Xesam.AudioList()'''
                return QUrl()
            def Audio(self):
                '''static QUrl Soprano.Vocabulary.Xesam.Audio()'''
                return QUrl()
            def ArchivedFile(self):
                '''static QUrl Soprano.Vocabulary.Xesam.ArchivedFile()'''
                return QUrl()
            def Archive(self):
                '''static QUrl Soprano.Vocabulary.Xesam.Archive()'''
                return QUrl()
            def Annotation(self):
                '''static QUrl Soprano.Vocabulary.Xesam.Annotation()'''
                return QUrl()
            def xesam35mmEquivalent(self):
                '''static QUrl Soprano.Vocabulary.Xesam.xesam35mmEquivalent()'''
                return QUrl()
            def xesamNamespace(self):
                '''static QUrl Soprano.Vocabulary.Xesam.xesamNamespace()'''
                return QUrl()
    class Util():
        """"""
        class SignalCacheModel(Soprano.FilterModel):
            """"""
            def __init__(self, parent = None):
                '''void Soprano.Util.SignalCacheModel.__init__(Soprano.Model parent = None)'''
            def timerEvent(self, event):
                '''void Soprano.Util.SignalCacheModel.timerEvent(QTimerEvent event)'''
            def parentStatementsRemoved(self):
                '''void Soprano.Util.SignalCacheModel.parentStatementsRemoved()'''
            def parentStatementsAdded(self):
                '''void Soprano.Util.SignalCacheModel.parentStatementsAdded()'''
            def setCacheTime(self, msec):
                '''void Soprano.Util.SignalCacheModel.setCacheTime(int msec)'''
            def cacheTime(self):
                '''int Soprano.Util.SignalCacheModel.cacheTime()'''
                return int()
    class Vocabulary():
        """"""
        class SIL():
            """"""
            def context(self):
                '''static QUrl Soprano.Vocabulary.SIL.context()'''
                return QUrl()
            def sourceStatement(self):
                '''static QUrl Soprano.Vocabulary.SIL.sourceStatement()'''
                return QUrl()
            def InferenceGraph(self):
                '''static QUrl Soprano.Vocabulary.SIL.InferenceGraph()'''
                return QUrl()
            def InferenceMetaData(self):
                '''static QUrl Soprano.Vocabulary.SIL.InferenceMetaData()'''
                return QUrl()
            def silNamespace(self):
                '''static QUrl Soprano.Vocabulary.SIL.silNamespace()'''
                return QUrl()
    class Query():
        """"""
        # Enum Soprano.Query.QueryLanguage
        QueryLanguageNone = 0
        QueryLanguageSparql = 0
        QueryLanguageRdql = 0
        QueryLanguageSerql = 0
        QueryLanguageSparqlNoInference = 0
        QueryLanguageUser = 0
        QUERY_LANGUAGE_NONE = 0
        QUERY_LANGUAGE_SPARQL = 0
        QUERY_LANGUAGE_RDQL = 0
        QUERY_LANGUAGE_SERQL = 0
        QUERY_LANGUAGE_USER = 0
    
        def queryLanguageFromString(self, queryLanguage):
            '''static Soprano.Query.QueryLanguage Soprano.Query.queryLanguageFromString(QString queryLanguage)'''
            return Soprano.Query.QueryLanguage()
        def queryLanguageToString(self, lang, userQueryLanguage = QString()):
            '''static QString Soprano.Query.queryLanguageToString(Soprano.Query.QueryLanguage lang, QString userQueryLanguage = QString())'''
            return QString()
    class Server():
        """"""
    class LanguageTag():
        """"""
        class LookupFlags():
            """"""
            def __init__(self):
                '''Soprano.LanguageTag.LookupFlags Soprano.LanguageTag.LookupFlags.__init__()'''
                return Soprano.LanguageTag.LookupFlags()
            def __init__(self):
                '''int Soprano.LanguageTag.LookupFlags.__init__()'''
                return int()
            def __init__(self):
                '''void Soprano.LanguageTag.LookupFlags.__init__()'''
            def __bool__(self):
                '''int Soprano.LanguageTag.LookupFlags.__bool__()'''
                return int()
            def __ne__(self, f):
                '''bool Soprano.LanguageTag.LookupFlags.__ne__(Soprano.LanguageTag.LookupFlags f)'''
                return bool()
            def __eq__(self, f):
                '''bool Soprano.LanguageTag.LookupFlags.__eq__(Soprano.LanguageTag.LookupFlags f)'''
                return bool()
            def __invert__(self):
                '''Soprano.LanguageTag.LookupFlags Soprano.LanguageTag.LookupFlags.__invert__()'''
                return Soprano.LanguageTag.LookupFlags()
            def __and__(self, mask):
                '''Soprano.LanguageTag.LookupFlags Soprano.LanguageTag.LookupFlags.__and__(int mask)'''
                return Soprano.LanguageTag.LookupFlags()
            def __xor__(self, f):
                '''Soprano.LanguageTag.LookupFlags Soprano.LanguageTag.LookupFlags.__xor__(Soprano.LanguageTag.LookupFlags f)'''
                return Soprano.LanguageTag.LookupFlags()
            def __xor__(self, f):
                '''Soprano.LanguageTag.LookupFlags Soprano.LanguageTag.LookupFlags.__xor__(int f)'''
                return Soprano.LanguageTag.LookupFlags()
            def __or__(self, f):
                '''Soprano.LanguageTag.LookupFlags Soprano.LanguageTag.LookupFlags.__or__(Soprano.LanguageTag.LookupFlags f)'''
                return Soprano.LanguageTag.LookupFlags()
            def __or__(self, f):
                '''Soprano.LanguageTag.LookupFlags Soprano.LanguageTag.LookupFlags.__or__(int f)'''
                return Soprano.LanguageTag.LookupFlags()
            def __int__(self):
                '''int Soprano.LanguageTag.LookupFlags.__int__()'''
                return int()
            def __ixor__(self, f):
                '''Soprano.LanguageTag.LookupFlags Soprano.LanguageTag.LookupFlags.__ixor__(Soprano.LanguageTag.LookupFlags f)'''
                return Soprano.LanguageTag.LookupFlags()
            def __ior__(self, f):
                '''Soprano.LanguageTag.LookupFlags Soprano.LanguageTag.LookupFlags.__ior__(Soprano.LanguageTag.LookupFlags f)'''
                return Soprano.LanguageTag.LookupFlags()
            def __iand__(self, mask):
                '''Soprano.LanguageTag.LookupFlags Soprano.LanguageTag.LookupFlags.__iand__(int mask)'''
                return Soprano.LanguageTag.LookupFlags()
    class Client():
        """"""
        class TcpClient(QObject, Soprano.Error.ErrorCache):
            """"""
            DEFAULT_PORT = None # int - member
            def __init__(self, parent = None):
                '''void Soprano.Client.TcpClient.__init__(QObject parent = None)'''
            def removeModel(self, name):
                '''void Soprano.Client.TcpClient.removeModel(QString name)'''
            def createModel(self, name, settings = None):
                '''Soprano.Model Soprano.Client.TcpClient.createModel(QString name, list-of-Soprano.BackendSetting settings = QListlt;Soprano.BackendSettinggt;())'''
                return Soprano.Model()
            def disconnect(self):
                '''void Soprano.Client.TcpClient.disconnect()'''
            def isConnected(self):
                '''bool Soprano.Client.TcpClient.isConnected()'''
                return bool()
            def connect(self, address = None, port = None):
                '''bool Soprano.Client.TcpClient.connect(QHostAddress address = QHostAddress.LocalHost, int port = Soprano.Server.ServerCore.DEFAULT_PORT)'''
                return bool()
    class Server():
        """"""
        class DBusExportIterator(QObject, Soprano.Error.ErrorCache):
            """"""
            def __init__(self, it, parent = None):
                '''void Soprano.Server.DBusExportIterator.__init__(Soprano.StatementIterator it, QObject parent = None)'''
            def __init__(self, it, parent = None):
                '''void Soprano.Server.DBusExportIterator.__init__(Soprano.NodeIterator it, QObject parent = None)'''
            def __init__(self, it, parent = None):
                '''void Soprano.Server.DBusExportIterator.__init__(Soprano.QueryResultIterator it, QObject parent = None)'''
            def unregisterIterator(self):
                '''void Soprano.Server.DBusExportIterator.unregisterIterator()'''
            def registerIterator(self, dbusObjectPath, dbusClient = QString()):
                '''bool Soprano.Server.DBusExportIterator.registerIterator(QString dbusObjectPath, QString dbusClient = QString())'''
                return bool()
            def setDeleteOnClose(self, deleteOnClose):
                '''void Soprano.Server.DBusExportIterator.setDeleteOnClose(bool deleteOnClose)'''
            def deleteOnClose(self):
                '''bool Soprano.Server.DBusExportIterator.deleteOnClose()'''
                return bool()
            def dbusObjectPath(self):
                '''QString Soprano.Server.DBusExportIterator.dbusObjectPath()'''
                return QString()
            def queryResultIterator(self):
                '''Soprano.QueryResultIterator Soprano.Server.DBusExportIterator.queryResultIterator()'''
                return Soprano.QueryResultIterator()
            def nodeIterator(self):
                '''Soprano.NodeIterator Soprano.Server.DBusExportIterator.nodeIterator()'''
                return Soprano.NodeIterator()
            def statementIterator(self):
                '''Soprano.StatementIterator Soprano.Server.DBusExportIterator.statementIterator()'''
                return Soprano.StatementIterator()
    class FilterModel(Soprano.Model):
        """"""
        def __init__(self):
            '''void Soprano.FilterModel.__init__()'''
        def __init__(self, parent):
            '''void Soprano.FilterModel.__init__(Soprano.Model parent)'''
        def parentStatementRemoved(self):
            '''Soprano.Statement Soprano.FilterModel.parentStatementRemoved()'''
            return Soprano.Statement()
        def parentStatementAdded(self):
            '''Soprano.Statement Soprano.FilterModel.parentStatementAdded()'''
            return Soprano.Statement()
        def parentStatementsRemoved(self):
            '''void Soprano.FilterModel.parentStatementsRemoved()'''
        def parentStatementsAdded(self):
            '''void Soprano.FilterModel.parentStatementsAdded()'''
        def createBlankNode(self):
            '''Soprano.Node Soprano.FilterModel.createBlankNode()'''
            return Soprano.Node()
        def write(self, os):
            '''Soprano.Error.ErrorCode Soprano.FilterModel.write(QTextStream os)'''
            return Soprano.Error.ErrorCode()
        def statementCount(self):
            '''int Soprano.FilterModel.statementCount()'''
            return int()
        def isEmpty(self):
            '''bool Soprano.FilterModel.isEmpty()'''
            return bool()
        def containsAnyStatement(self, statement):
            '''bool Soprano.FilterModel.containsAnyStatement(Soprano.Statement statement)'''
            return bool()
        def containsAnyStatement(self, subject, predicate, object, context = None):
            '''bool Soprano.FilterModel.containsAnyStatement(Soprano.Node subject, Soprano.Node predicate, Soprano.Node object, Soprano.Node context = Soprano.Node())'''
            return bool()
        def containsStatement(self, statement):
            '''bool Soprano.FilterModel.containsStatement(Soprano.Statement statement)'''
            return bool()
        def containsStatement(self, subject, predicate, object, context = None):
            '''bool Soprano.FilterModel.containsStatement(Soprano.Node subject, Soprano.Node predicate, Soprano.Node object, Soprano.Node context = Soprano.Node())'''
            return bool()
        def executeQuery(self, query, language, userQueryLanguage = QString()):
            '''Soprano.QueryResultIterator Soprano.FilterModel.executeQuery(QString query, Soprano.Query.QueryLanguage language, QString userQueryLanguage = QString())'''
            return Soprano.QueryResultIterator()
        def listContexts(self):
            '''Soprano.NodeIterator Soprano.FilterModel.listContexts()'''
            return Soprano.NodeIterator()
        def listStatements(self, partial):
            '''Soprano.StatementIterator Soprano.FilterModel.listStatements(Soprano.Statement partial)'''
            return Soprano.StatementIterator()
        def listStatements(self, subject, predicate, object, context = None):
            '''Soprano.StatementIterator Soprano.FilterModel.listStatements(Soprano.Node subject, Soprano.Node predicate, Soprano.Node object, Soprano.Node context = Soprano.Node())'''
            return Soprano.StatementIterator()
        def removeAllStatements(self, statement):
            '''Soprano.Error.ErrorCode Soprano.FilterModel.removeAllStatements(Soprano.Statement statement)'''
            return Soprano.Error.ErrorCode()
        def removeAllStatements(self, subject, predicate, object, context = None):
            '''Soprano.Error.ErrorCode Soprano.FilterModel.removeAllStatements(Soprano.Node subject, Soprano.Node predicate, Soprano.Node object, Soprano.Node context = Soprano.Node())'''
            return Soprano.Error.ErrorCode()
        def removeStatement(self, statement):
            '''Soprano.Error.ErrorCode Soprano.FilterModel.removeStatement(Soprano.Statement statement)'''
            return Soprano.Error.ErrorCode()
        def removeStatement(self, subject, predicate, object, context = None):
            '''Soprano.Error.ErrorCode Soprano.FilterModel.removeStatement(Soprano.Node subject, Soprano.Node predicate, Soprano.Node object, Soprano.Node context = Soprano.Node())'''
            return Soprano.Error.ErrorCode()
        def addStatement(self, statement):
            '''Soprano.Error.ErrorCode Soprano.FilterModel.addStatement(Soprano.Statement statement)'''
            return Soprano.Error.ErrorCode()
        def addStatement(self, subject, predicate, object, context = None):
            '''Soprano.Error.ErrorCode Soprano.FilterModel.addStatement(Soprano.Node subject, Soprano.Node predicate, Soprano.Node object, Soprano.Node context = Soprano.Node())'''
            return Soprano.Error.ErrorCode()
        def parentModel(self):
            '''Soprano.Model Soprano.FilterModel.parentModel()'''
            return Soprano.Model()
        def setParentModel(self, model):
            '''void Soprano.FilterModel.setParentModel(Soprano.Model model)'''
    class Error():
        """"""
        class ParserError(Soprano.Error.Error):
            """"""
            def __init__(self):
                '''void Soprano.Error.ParserError.__init__()'''
            def __init__(self, message = QString(), code = None):
                '''Soprano.Error.Locator Soprano.Error.ParserError.__init__(QString message = QString(), int code = Soprano.Error.ErrorParsingFailed)'''
                return Soprano.Error.Locator()
            def __init__(self):
                '''Soprano.Error.Error Soprano.Error.ParserError.__init__()'''
                return Soprano.Error.Error()
            def __init__(self):
                '''Soprano.Error.ParserError Soprano.Error.ParserError.__init__()'''
                return Soprano.Error.ParserError()
            def locator(self):
                '''Soprano.Error.Locator Soprano.Error.ParserError.locator()'''
                return Soprano.Error.Locator()
    class Client():
        """"""
        class DBusModel(Soprano.StorageModel):
            """"""
            def __init__(self, serviceName, dbusObject, backend = None):
                '''void Soprano.Client.DBusModel.__init__(QString serviceName, QString dbusObject, Soprano.Backend backend = None)'''
            def createBlankNode(self):
                '''Soprano.Node Soprano.Client.DBusModel.createBlankNode()'''
                return Soprano.Node()
            def containsAnyStatement(self, statement):
                '''bool Soprano.Client.DBusModel.containsAnyStatement(Soprano.Statement statement)'''
                return bool()
            def containsStatement(self, statement):
                '''bool Soprano.Client.DBusModel.containsStatement(Soprano.Statement statement)'''
                return bool()
            def isEmpty(self):
                '''bool Soprano.Client.DBusModel.isEmpty()'''
                return bool()
            def statementCount(self):
                '''int Soprano.Client.DBusModel.statementCount()'''
                return int()
            def removeAllStatements(self, statement):
                '''Soprano.Error.ErrorCode Soprano.Client.DBusModel.removeAllStatements(Soprano.Statement statement)'''
                return Soprano.Error.ErrorCode()
            def removeStatement(self, statement):
                '''Soprano.Error.ErrorCode Soprano.Client.DBusModel.removeStatement(Soprano.Statement statement)'''
                return Soprano.Error.ErrorCode()
            def listStatements(self, partial):
                '''Soprano.StatementIterator Soprano.Client.DBusModel.listStatements(Soprano.Statement partial)'''
                return Soprano.StatementIterator()
            def executeQuery(self, query, language, userQueryLanguage = QString()):
                '''Soprano.QueryResultIterator Soprano.Client.DBusModel.executeQuery(QString query, Soprano.Query.QueryLanguage language, QString userQueryLanguage = QString())'''
                return Soprano.QueryResultIterator()
            def listContexts(self):
                '''Soprano.NodeIterator Soprano.Client.DBusModel.listContexts()'''
                return Soprano.NodeIterator()
            def addStatement(self, statement):
                '''Soprano.Error.ErrorCode Soprano.Client.DBusModel.addStatement(Soprano.Statement statement)'''
                return Soprano.Error.ErrorCode()
            def asyncCalls(self):
                '''bool Soprano.Client.DBusModel.asyncCalls()'''
                return bool()
            def setAsyncCalls(self, b):
                '''void Soprano.Client.DBusModel.setAsyncCalls(bool b)'''
    class RdfSerializations():
        """"""
        def __init__(self):
            '''Soprano.RdfSerializations Soprano.RdfSerializations.__init__()'''
            return Soprano.RdfSerializations()
        def __init__(self):
            '''int Soprano.RdfSerializations.__init__()'''
            return int()
        def __init__(self):
            '''void Soprano.RdfSerializations.__init__()'''
        def __bool__(self):
            '''int Soprano.RdfSerializations.__bool__()'''
            return int()
        def __ne__(self, f):
            '''bool Soprano.RdfSerializations.__ne__(Soprano.RdfSerializations f)'''
            return bool()
        def __eq__(self, f):
            '''bool Soprano.RdfSerializations.__eq__(Soprano.RdfSerializations f)'''
            return bool()
        def __invert__(self):
            '''Soprano.RdfSerializations Soprano.RdfSerializations.__invert__()'''
            return Soprano.RdfSerializations()
        def __and__(self, mask):
            '''Soprano.RdfSerializations Soprano.RdfSerializations.__and__(int mask)'''
            return Soprano.RdfSerializations()
        def __xor__(self, f):
            '''Soprano.RdfSerializations Soprano.RdfSerializations.__xor__(Soprano.RdfSerializations f)'''
            return Soprano.RdfSerializations()
        def __xor__(self, f):
            '''Soprano.RdfSerializations Soprano.RdfSerializations.__xor__(int f)'''
            return Soprano.RdfSerializations()
        def __or__(self, f):
            '''Soprano.RdfSerializations Soprano.RdfSerializations.__or__(Soprano.RdfSerializations f)'''
            return Soprano.RdfSerializations()
        def __or__(self, f):
            '''Soprano.RdfSerializations Soprano.RdfSerializations.__or__(int f)'''
            return Soprano.RdfSerializations()
        def __int__(self):
            '''int Soprano.RdfSerializations.__int__()'''
            return int()
        def __ixor__(self, f):
            '''Soprano.RdfSerializations Soprano.RdfSerializations.__ixor__(Soprano.RdfSerializations f)'''
            return Soprano.RdfSerializations()
        def __ior__(self, f):
            '''Soprano.RdfSerializations Soprano.RdfSerializations.__ior__(Soprano.RdfSerializations f)'''
            return Soprano.RdfSerializations()
        def __iand__(self, mask):
            '''Soprano.RdfSerializations Soprano.RdfSerializations.__iand__(int mask)'''
            return Soprano.RdfSerializations()
    class Server():
        """"""
        class ServerCore(QObject, Soprano.Error.ErrorCache):
            """"""
            DEFAULT_PORT = None # int - member
            def __init__(self, parent = None):
                '''void Soprano.Server.ServerCore.__init__(QObject parent = None)'''
            def maximumConnectionCount(self):
                '''int Soprano.Server.ServerCore.maximumConnectionCount()'''
                return int()
            def setMaximumConnectionCount(self, max):
                '''void Soprano.Server.ServerCore.setMaximumConnectionCount(int max)'''
            def createModel(self, settings):
                '''Soprano.Model Soprano.Server.ServerCore.createModel(list-of-Soprano.BackendSetting settings)'''
                return Soprano.Model()
            def registerAsDBusObject(self, objectPath = QString()):
                '''void Soprano.Server.ServerCore.registerAsDBusObject(QString objectPath = QString())'''
            def serverPort(self):
                '''int Soprano.Server.ServerCore.serverPort()'''
                return int()
            def listen(self, port = None):
                '''bool Soprano.Server.ServerCore.listen(int port = Soprano.Server.ServerCore.DEFAULT_PORT)'''
                return bool()
            def start(self, socketPath = QString()):
                '''bool Soprano.Server.ServerCore.start(QString socketPath = QString())'''
                return bool()
            def allModels(self):
                '''QStringList Soprano.Server.ServerCore.allModels()'''
                return QStringList()
            def removeModel(self, name):
                '''void Soprano.Server.ServerCore.removeModel(QString name)'''
            def model(self, name):
                '''Soprano.Model Soprano.Server.ServerCore.model(QString name)'''
                return Soprano.Model()
            def backendSettings(self):
                '''list-of-Soprano.BackendSetting Soprano.Server.ServerCore.backendSettings()'''
                return [Soprano.BackendSetting()]
            def setBackendSettings(self, settings):
                '''void Soprano.Server.ServerCore.setBackendSettings(list-of-Soprano.BackendSetting settings)'''
            def backend(self):
                '''Soprano.Backend Soprano.Server.ServerCore.backend()'''
                return Soprano.Backend()
            def setBackend(self, backend):
                '''void Soprano.Server.ServerCore.setBackend(Soprano.Backend backend)'''
    class LanguageTag():
        """"""
        # Enum Soprano.LanguageTag.LookupFlag
        LookupFlagNone = 0
        LookupFlagNoFallback = 0
    
        # Enum Soprano.LanguageTag.MatchFilter
        MatchFilterBasic = 0
        MatchFilterExtended = 0
    
        def __init__(self):
            '''void Soprano.LanguageTag.__init__()'''
        def __init__(self, other):
            '''void Soprano.LanguageTag.__init__(Soprano.LanguageTag other)'''
        def __init__(self, tag):
            '''void Soprano.LanguageTag.__init__(str tag)'''
        def __init__(self, tag):
            '''void Soprano.LanguageTag.__init__(QLatin1String tag)'''
        def __init__(self, tag):
            '''void Soprano.LanguageTag.__init__(QString tag)'''
        def __init__(self, locale):
            '''void Soprano.LanguageTag.__init__(QLocale locale)'''
        def __init__(self, lang, country = None):
            '''void Soprano.LanguageTag.__init__(QLocale.Language lang, QLocale.Country country = QLocale.AnyCountry)'''
        def lookup(self, choices, priority, flags = None, scheme = None):
            '''static int Soprano.LanguageTag.lookup(list-of-Soprano.LanguageTag choices, list-of-Soprano.LanguageTag priority, Soprano.LanguageTag.LookupFlags flags = Soprano.LanguageTag.LookupFlagNone, Soprano.LanguageTag.MatchFilter scheme = Soprano.LanguageTag.MatchFilterBasic)'''
            return int()
        def lookup(self, choices, priority, flags = None, scheme = None):
            '''static int Soprano.LanguageTag.lookup(list-of-Soprano.LanguageTag choices, Soprano.LanguageTag priority, Soprano.LanguageTag.LookupFlags flags = Soprano.LanguageTag.LookupFlagNone, Soprano.LanguageTag.MatchFilter scheme = Soprano.LanguageTag.MatchFilterBasic)'''
            return int()
        def toLocale(self):
            '''QLocale Soprano.LanguageTag.toLocale()'''
            return QLocale()
        def toPrettyString(self):
            '''QString Soprano.LanguageTag.toPrettyString()'''
            return QString()
        def toString(self):
            '''QString Soprano.LanguageTag.toString()'''
            return QString()
        def subTags(self):
            '''QStringList Soprano.LanguageTag.subTags()'''
            return QStringList()
        def isValid(self):
            '''bool Soprano.LanguageTag.isValid()'''
            return bool()
        def isEmpty(self):
            '''bool Soprano.LanguageTag.isEmpty()'''
            return bool()
        def matches(self, range, scheme = None):
            '''bool Soprano.LanguageTag.matches(Soprano.LanguageTag range, Soprano.LanguageTag.MatchFilter scheme = Soprano.LanguageTag.MatchFilterBasic)'''
            return bool()
        def __ge__(self, other):
            '''bool Soprano.LanguageTag.__ge__(Soprano.LanguageTag other)'''
            return bool()
        def __gt__(self, other):
            '''bool Soprano.LanguageTag.__gt__(Soprano.LanguageTag other)'''
            return bool()
        def __le__(self, other):
            '''bool Soprano.LanguageTag.__le__(Soprano.LanguageTag other)'''
            return bool()
        def __lt__(self, other):
            '''bool Soprano.LanguageTag.__lt__(Soprano.LanguageTag other)'''
            return bool()
        def __ne__(self, other):
            '''bool Soprano.LanguageTag.__ne__(Soprano.LanguageTag other)'''
            return bool()
        def __eq__(self, other):
            '''bool Soprano.LanguageTag.__eq__(Soprano.LanguageTag other)'''
            return bool()
    class Model(QObject, Soprano.Error.ErrorCache):
        """"""
        def __init__(self):
            '''void Soprano.Model.__init__()'''
        statementRemoved = pyqtSignal() # void statementRemoved(const Soprano::Statementamp;) - signal
        statementAdded = pyqtSignal() # void statementAdded(const Soprano::Statementamp;) - signal
        statementsRemoved = pyqtSignal() # void statementsRemoved() - signal
        statementsAdded = pyqtSignal() # void statementsAdded() - signal
        def createBlankNode(self):
            '''abstract Soprano.Node Soprano.Model.createBlankNode()'''
            return Soprano.Node()
        def write(self, os):
            '''Soprano.Error.ErrorCode Soprano.Model.write(QTextStream os)'''
            return Soprano.Error.ErrorCode()
        def statementCount(self):
            '''abstract int Soprano.Model.statementCount()'''
            return int()
        def isEmpty(self):
            '''abstract bool Soprano.Model.isEmpty()'''
            return bool()
        def containsContext(self, context):
            '''bool Soprano.Model.containsContext(Soprano.Node context)'''
            return bool()
        def containsStatement(self, statement):
            '''abstract bool Soprano.Model.containsStatement(Soprano.Statement statement)'''
            return bool()
        def containsStatement(self, subject, predicate, object, context = None):
            '''bool Soprano.Model.containsStatement(Soprano.Node subject, Soprano.Node predicate, Soprano.Node object, Soprano.Node context = Soprano.Node())'''
            return bool()
        def containsAnyStatement(self, statement):
            '''abstract bool Soprano.Model.containsAnyStatement(Soprano.Statement statement)'''
            return bool()
        def containsAnyStatement(self, subject, predicate, object, context = None):
            '''bool Soprano.Model.containsAnyStatement(Soprano.Node subject, Soprano.Node predicate, Soprano.Node object, Soprano.Node context = Soprano.Node())'''
            return bool()
        def executeQuery(self, query, language, userQueryLanguage = QString()):
            '''abstract Soprano.QueryResultIterator Soprano.Model.executeQuery(QString query, Soprano.Query.QueryLanguage language, QString userQueryLanguage = QString())'''
            return Soprano.QueryResultIterator()
        def listContexts(self):
            '''abstract Soprano.NodeIterator Soprano.Model.listContexts()'''
            return Soprano.NodeIterator()
        def listStatementsInContext(self, context):
            '''Soprano.StatementIterator Soprano.Model.listStatementsInContext(Soprano.Node context)'''
            return Soprano.StatementIterator()
        def listStatements(self, partial):
            '''abstract Soprano.StatementIterator Soprano.Model.listStatements(Soprano.Statement partial)'''
            return Soprano.StatementIterator()
        def listStatements(self, subject, predicate, object, context = None):
            '''Soprano.StatementIterator Soprano.Model.listStatements(Soprano.Node subject, Soprano.Node predicate, Soprano.Node object, Soprano.Node context = Soprano.Node())'''
            return Soprano.StatementIterator()
        def listStatements(self):
            '''Soprano.StatementIterator Soprano.Model.listStatements()'''
            return Soprano.StatementIterator()
        def removeContext(self):
            '''Soprano.Node Soprano.Model.removeContext()'''
            return Soprano.Node()
        def removeStatements(self, statements):
            '''Soprano.Error.ErrorCode Soprano.Model.removeStatements(list-of-Soprano.Statement statements)'''
            return Soprano.Error.ErrorCode()
        def removeAllStatements(self, statement):
            '''abstract Soprano.Error.ErrorCode Soprano.Model.removeAllStatements(Soprano.Statement statement)'''
            return Soprano.Error.ErrorCode()
        def removeAllStatements(self, subject, predicate, object, context = None):
            '''Soprano.Error.ErrorCode Soprano.Model.removeAllStatements(Soprano.Node subject, Soprano.Node predicate, Soprano.Node object, Soprano.Node context = Soprano.Node())'''
            return Soprano.Error.ErrorCode()
        def removeAllStatements(self):
            '''Soprano.Error.ErrorCode Soprano.Model.removeAllStatements()'''
            return Soprano.Error.ErrorCode()
        def removeStatement(self, statement):
            '''abstract Soprano.Error.ErrorCode Soprano.Model.removeStatement(Soprano.Statement statement)'''
            return Soprano.Error.ErrorCode()
        def removeStatement(self, subject, predicate, object, context = None):
            '''Soprano.Error.ErrorCode Soprano.Model.removeStatement(Soprano.Node subject, Soprano.Node predicate, Soprano.Node object, Soprano.Node context = Soprano.Node())'''
            return Soprano.Error.ErrorCode()
        def addStatements(self, statements):
            '''Soprano.Error.ErrorCode Soprano.Model.addStatements(list-of-Soprano.Statement statements)'''
            return Soprano.Error.ErrorCode()
        def addStatement(self, statement):
            '''abstract Soprano.Error.ErrorCode Soprano.Model.addStatement(Soprano.Statement statement)'''
            return Soprano.Error.ErrorCode()
        def addStatement(self, subject, predicate, object, context = None):
            '''Soprano.Error.ErrorCode Soprano.Model.addStatement(Soprano.Node subject, Soprano.Node predicate, Soprano.Node object, Soprano.Node context = Soprano.Node())'''
            return Soprano.Error.ErrorCode()
    class Vocabulary():
        """"""
        class XMLSchema():
            """"""
            def base64Binary(self):
                '''static QUrl Soprano.Vocabulary.XMLSchema.base64Binary()'''
                return QUrl()
            def time(self):
                '''static QUrl Soprano.Vocabulary.XMLSchema.time()'''
                return QUrl()
            def dateTime(self):
                '''static QUrl Soprano.Vocabulary.XMLSchema.dateTime()'''
                return QUrl()
            def date(self):
                '''static QUrl Soprano.Vocabulary.XMLSchema.date()'''
                return QUrl()
            def boolean(self):
                '''static QUrl Soprano.Vocabulary.XMLSchema.boolean()'''
                return QUrl()
            def xsdDouble(self):
                '''static QUrl Soprano.Vocabulary.XMLSchema.xsdDouble()'''
                return QUrl()
            def xsdFloat(self):
                '''static QUrl Soprano.Vocabulary.XMLSchema.xsdFloat()'''
                return QUrl()
            def string(self):
                '''static QUrl Soprano.Vocabulary.XMLSchema.string()'''
                return QUrl()
            def unsignedLong(self):
                '''static QUrl Soprano.Vocabulary.XMLSchema.unsignedLong()'''
                return QUrl()
            def unsignedShort(self):
                '''static QUrl Soprano.Vocabulary.XMLSchema.unsignedShort()'''
                return QUrl()
            def unsignedInt(self):
                '''static QUrl Soprano.Vocabulary.XMLSchema.unsignedInt()'''
                return QUrl()
            def xsdLong(self):
                '''static QUrl Soprano.Vocabulary.XMLSchema.xsdLong()'''
                return QUrl()
            def xsdShort(self):
                '''static QUrl Soprano.Vocabulary.XMLSchema.xsdShort()'''
                return QUrl()
            def decimal(self):
                '''static QUrl Soprano.Vocabulary.XMLSchema.decimal()'''
                return QUrl()
            def nonNegativeInteger(self):
                '''static QUrl Soprano.Vocabulary.XMLSchema.nonNegativeInteger()'''
                return QUrl()
            def negativeInteger(self):
                '''static QUrl Soprano.Vocabulary.XMLSchema.negativeInteger()'''
                return QUrl()
            def integer(self):
                '''static QUrl Soprano.Vocabulary.XMLSchema.integer()'''
                return QUrl()
            def xsdInt(self):
                '''static QUrl Soprano.Vocabulary.XMLSchema.xsdInt()'''
                return QUrl()
            def xsdNamespace(self):
                '''static QUrl Soprano.Vocabulary.XMLSchema.xsdNamespace()'''
                return QUrl()
    class Inference():
        """"""
        class RuleSet():
            """"""
            def __init__(self):
                '''void Soprano.Inference.RuleSet.__init__()'''
            def __init__(self):
                '''Soprano.Inference.RuleSet Soprano.Inference.RuleSet.__init__()'''
                return Soprano.Inference.RuleSet()
            def standardRuleSet(self):
                '''static Soprano.Inference.StandardRuleSet Soprano.Inference.RuleSet.standardRuleSet()'''
                return Soprano.Inference.StandardRuleSet()
            def allRules(self):
                '''list-of-Soprano.Inference.Rule Soprano.Inference.RuleSet.allRules()'''
                return [Soprano.Inference.Rule()]
            def ruleNames(self):
                '''QStringList Soprano.Inference.RuleSet.ruleNames()'''
                return QStringList()
            def rule(self, name):
                '''Soprano.Inference.Rule Soprano.Inference.RuleSet.rule(QString name)'''
                return Soprano.Inference.Rule()
            def __getitem__(self, index):
                '''Soprano.Inference.Rule Soprano.Inference.RuleSet.__getitem__(int index)'''
                return Soprano.Inference.Rule()
            def __getitem__(self, name):
                '''Soprano.Inference.Rule Soprano.Inference.RuleSet.__getitem__(QString name)'''
                return Soprano.Inference.Rule()
            def at(self, index):
                '''Soprano.Inference.Rule Soprano.Inference.RuleSet.at(int index)'''
                return Soprano.Inference.Rule()
            def count(self):
                '''int Soprano.Inference.RuleSet.count()'''
                return int()
            def insert(self, name, rule):
                '''void Soprano.Inference.RuleSet.insert(QString name, Soprano.Inference.Rule rule)'''
            def clear(self):
                '''void Soprano.Inference.RuleSet.clear()'''
    class BindingSet():
        """"""
        def __init__(self):
            '''void Soprano.BindingSet.__init__()'''
        def __init__(self, other):
            '''void Soprano.BindingSet.__init__(Soprano.BindingSet other)'''
        def __ne__(self, other):
            '''bool Soprano.BindingSet.__ne__(Soprano.BindingSet other)'''
            return bool()
        def __eq__(self, other):
            '''bool Soprano.BindingSet.__eq__(Soprano.BindingSet other)'''
            return bool()
        def replace(self, offset, value):
            '''void Soprano.BindingSet.replace(int offset, Soprano.Node value)'''
        def replace(self, name, value):
            '''void Soprano.BindingSet.replace(QString name, Soprano.Node value)'''
        def insert(self, name, value):
            '''void Soprano.BindingSet.insert(QString name, Soprano.Node value)'''
        def count(self):
            '''int Soprano.BindingSet.count()'''
            return int()
        def contains(self, name):
            '''bool Soprano.BindingSet.contains(QString name)'''
            return bool()
        def value(self, offset):
            '''Soprano.Node Soprano.BindingSet.value(int offset)'''
            return Soprano.Node()
        def value(self, name):
            '''Soprano.Node Soprano.BindingSet.value(QString name)'''
            return Soprano.Node()
        def __getitem__(self, offset):
            '''Soprano.Node Soprano.BindingSet.__getitem__(int offset)'''
            return Soprano.Node()
        def __getitem__(self, name):
            '''Soprano.Node Soprano.BindingSet.__getitem__(QString name)'''
            return Soprano.Node()
        def bindingNames(self):
            '''QStringList Soprano.BindingSet.bindingNames()'''
            return QStringList()
    class Util():
        """"""
        class AsyncQuery(QObject, Soprano.Error.ErrorCache):
            """"""
            def executeQuery(self, model, query, language, userQueryLanguage = QString()):
                '''static Soprano.Util.AsyncQuery Soprano.Util.AsyncQuery.executeQuery(Soprano.Model model, QString query, Soprano.Query.QueryLanguage language, QString userQueryLanguage = QString())'''
                return Soprano.Util.AsyncQuery()
            finished = pyqtSignal() # void finished(Soprano::Util::AsyncQuery *) - signal
            nextReady = pyqtSignal() # void nextReady(Soprano::Util::AsyncQuery *) - signal
            def close(self):
                '''void Soprano.Util.AsyncQuery.close()'''
            def next(self):
                '''bool Soprano.Util.AsyncQuery.next()'''
                return bool()
            def isBool(self):
                '''bool Soprano.Util.AsyncQuery.isBool()'''
                return bool()
            def isBinding(self):
                '''bool Soprano.Util.AsyncQuery.isBinding()'''
                return bool()
            def isGraph(self):
                '''bool Soprano.Util.AsyncQuery.isGraph()'''
                return bool()
            def bindingNames(self):
                '''QStringList Soprano.Util.AsyncQuery.bindingNames()'''
                return QStringList()
            def bindingCount(self):
                '''int Soprano.Util.AsyncQuery.bindingCount()'''
                return int()
            def binding(self, name):
                '''Soprano.Node Soprano.Util.AsyncQuery.binding(QString name)'''
                return Soprano.Node()
            def binding(self, offset):
                '''Soprano.Node Soprano.Util.AsyncQuery.binding(int offset)'''
                return Soprano.Node()
            def boolValue(self):
                '''bool Soprano.Util.AsyncQuery.boolValue()'''
                return bool()
            def currentBindings(self):
                '''Soprano.BindingSet Soprano.Util.AsyncQuery.currentBindings()'''
                return Soprano.BindingSet()
            def currentStatement(self):
                '''Soprano.Statement Soprano.Util.AsyncQuery.currentStatement()'''
                return Soprano.Statement()
    class Serializer(Soprano.Plugin, Soprano.Error.ErrorCache):
        """"""
        def __init__(self, name):
            '''void Soprano.Serializer.__init__(QString name)'''
        def prefixes(self):
            '''dict-of-QString-QUrl Soprano.Serializer.prefixes()'''
            return dict-of-QString-QUrl()
        def clearPrefixes(self):
            '''void Soprano.Serializer.clearPrefixes()'''
        def addPrefix(self, qname, uri):
            '''void Soprano.Serializer.addPrefix(QString qname, QUrl uri)'''
        def serialize(self, it, stream, serialization, userSerialization = QString()):
            '''abstract bool Soprano.Serializer.serialize(Soprano.StatementIterator it, QTextStream stream, Soprano.RdfSerialization serialization, QString userSerialization = QString())'''
            return bool()
        def supportsSerialization(self, s, userSerialization = QString()):
            '''bool Soprano.Serializer.supportsSerialization(Soprano.RdfSerialization s, QString userSerialization = QString())'''
            return bool()
        def supportedUserSerializations(self):
            '''QStringList Soprano.Serializer.supportedUserSerializations()'''
            return QStringList()
        def supportedSerializations(self):
            '''abstract Soprano.RdfSerializations Soprano.Serializer.supportedSerializations()'''
            return Soprano.RdfSerializations()
    class Parser(Soprano.Plugin, Soprano.Error.ErrorCache):
        """"""
        def __init__(self, name):
            '''void Soprano.Parser.__init__(QString name)'''
        def __init__(self):
            '''Soprano.Parser Soprano.Parser.__init__()'''
            return Soprano.Parser()
        def parseStream(self, stream, baseUri, serialization, userSerialization = QString()):
            '''abstract Soprano.StatementIterator Soprano.Parser.parseStream(QTextStream stream, QUrl baseUri, Soprano.RdfSerialization serialization, QString userSerialization = QString())'''
            return Soprano.StatementIterator()
        def parseString(self, data, baseUri, serialization, userSerialization = QString()):
            '''Soprano.StatementIterator Soprano.Parser.parseString(QString data, QUrl baseUri, Soprano.RdfSerialization serialization, QString userSerialization = QString())'''
            return Soprano.StatementIterator()
        def parseFile(self, filename, baseUri, serialization, userSerialization = QString()):
            '''Soprano.StatementIterator Soprano.Parser.parseFile(QString filename, QUrl baseUri, Soprano.RdfSerialization serialization, QString userSerialization = QString())'''
            return Soprano.StatementIterator()
        def supportsSerialization(self, s, userSerialization = QString()):
            '''bool Soprano.Parser.supportsSerialization(Soprano.RdfSerialization s, QString userSerialization = QString())'''
            return bool()
        def supportedUserSerializations(self):
            '''QStringList Soprano.Parser.supportedUserSerializations()'''
            return QStringList()
        def supportedSerializations(self):
            '''abstract Soprano.RdfSerializations Soprano.Parser.supportedSerializations()'''
            return Soprano.RdfSerializations()
    class Graph():
        """"""
        def __init__(self):
            '''void Soprano.Graph.__init__()'''
        def __init__(self):
            '''Soprano.Graph Soprano.Graph.__init__()'''
            return Soprano.Graph()
        def __init__(self):
            '''list-of-Soprano.Statement Soprano.Graph.__init__()'''
            return [Soprano.Statement()]
        def toSet(self):
            '''list-of-Soprano.Statement Soprano.Graph.toSet()'''
            return [Soprano.Statement()]
        def __ne__(self, g):
            '''bool Soprano.Graph.__ne__(Soprano.Graph g)'''
            return bool()
        def __eq__(self, g):
            '''bool Soprano.Graph.__eq__(Soprano.Graph g)'''
            return bool()
        def __lshift__(self):
            '''Soprano.Graph Soprano.Graph.__lshift__()'''
            return Soprano.Graph()
        def __lshift__(self):
            '''Soprano.Statement Soprano.Graph.__lshift__()'''
            return Soprano.Statement()
        def __isub__(self, g):
            '''Soprano.Graph Soprano.Graph.__isub__(Soprano.Graph g)'''
            return Soprano.Graph()
        def __isub__(self, s):
            '''Soprano.Graph Soprano.Graph.__isub__(Soprano.Statement s)'''
            return Soprano.Graph()
        def __sub__(self):
            '''Soprano.Graph Soprano.Graph.__sub__()'''
            return Soprano.Graph()
        def __sub__(self, s):
            '''Soprano.Graph Soprano.Graph.__sub__(Soprano.Statement s)'''
            return Soprano.Graph()
        def __iadd__(self, g):
            '''Soprano.Graph Soprano.Graph.__iadd__(Soprano.Graph g)'''
            return Soprano.Graph()
        def __iadd__(self, s):
            '''Soprano.Graph Soprano.Graph.__iadd__(Soprano.Statement s)'''
            return Soprano.Graph()
        def __add__(self, g):
            '''Soprano.Graph Soprano.Graph.__add__(Soprano.Graph g)'''
            return Soprano.Graph()
        def __add__(self, s):
            '''Soprano.Graph Soprano.Graph.__add__(Soprano.Statement s)'''
            return Soprano.Graph()
        def toList(self):
            '''list-of-Soprano.Statement Soprano.Graph.toList()'''
            return [Soprano.Statement()]
        def statementCount(self):
            '''int Soprano.Graph.statementCount()'''
            return int()
        def isEmpty(self):
            '''bool Soprano.Graph.isEmpty()'''
            return bool()
        def containsContext(self, context):
            '''bool Soprano.Graph.containsContext(Soprano.Node context)'''
            return bool()
        def containsStatement(self, statement):
            '''bool Soprano.Graph.containsStatement(Soprano.Statement statement)'''
            return bool()
        def containsStatement(self, subject, predicate, object, context = None):
            '''bool Soprano.Graph.containsStatement(Soprano.Node subject, Soprano.Node predicate, Soprano.Node object, Soprano.Node context = Soprano.Node())'''
            return bool()
        def containsAnyStatement(self, statement):
            '''bool Soprano.Graph.containsAnyStatement(Soprano.Statement statement)'''
            return bool()
        def containsAnyStatement(self, subject, predicate, object, context = None):
            '''bool Soprano.Graph.containsAnyStatement(Soprano.Node subject, Soprano.Node predicate, Soprano.Node object, Soprano.Node context = Soprano.Node())'''
            return bool()
        def listContexts(self):
            '''Soprano.NodeIterator Soprano.Graph.listContexts()'''
            return Soprano.NodeIterator()
        def listStatementsInContext(self, context):
            '''Soprano.StatementIterator Soprano.Graph.listStatementsInContext(Soprano.Node context)'''
            return Soprano.StatementIterator()
        def listStatements(self, partial = None):
            '''Soprano.StatementIterator Soprano.Graph.listStatements(Soprano.Statement partial = Soprano.Statement())'''
            return Soprano.StatementIterator()
        def listStatements(self, subject, predicate, object, context = None):
            '''Soprano.StatementIterator Soprano.Graph.listStatements(Soprano.Node subject, Soprano.Node predicate, Soprano.Node object, Soprano.Node context = Soprano.Node())'''
            return Soprano.StatementIterator()
        def removeContext(self):
            '''Soprano.Node Soprano.Graph.removeContext()'''
            return Soprano.Node()
        def removeStatements(self, statements):
            '''void Soprano.Graph.removeStatements(list-of-Soprano.Statement statements)'''
        def removeAllStatements(self, statement = None):
            '''void Soprano.Graph.removeAllStatements(Soprano.Statement statement = Soprano.Statement())'''
        def removeAllStatements(self, subject, predicate, object, context = None):
            '''void Soprano.Graph.removeAllStatements(Soprano.Node subject, Soprano.Node predicate, Soprano.Node object, Soprano.Node context = Soprano.Node())'''
        def removeStatement(self, statement):
            '''void Soprano.Graph.removeStatement(Soprano.Statement statement)'''
        def removeStatement(self, subject, predicate, object, context = None):
            '''void Soprano.Graph.removeStatement(Soprano.Node subject, Soprano.Node predicate, Soprano.Node object, Soprano.Node context = Soprano.Node())'''
        def addStatements(self, statements):
            '''void Soprano.Graph.addStatements(list-of-Soprano.Statement statements)'''
        def addStatement(self, statement):
            '''void Soprano.Graph.addStatement(Soprano.Statement statement)'''
        def addStatement(self, subject, predicate, object, context = None):
            '''void Soprano.Graph.addStatement(Soprano.Node subject, Soprano.Node predicate, Soprano.Node object, Soprano.Node context = Soprano.Node())'''
    class Error():
        """"""
        class ErrorCache():
            """"""
            def __init__(self):
                '''void Soprano.Error.ErrorCache.__init__()'''
            def setError(self):
                '''Soprano.Error.Error Soprano.Error.ErrorCache.setError()'''
                return Soprano.Error.Error()
            def setError(self, errorMessage, code = None):
                '''void Soprano.Error.ErrorCache.setError(QString errorMessage, int code = Soprano.Error.ErrorUnknown)'''
            def clearError(self):
                '''void Soprano.Error.ErrorCache.clearError()'''
            def lastError(self):
                '''Soprano.Error.Error Soprano.Error.ErrorCache.lastError()'''
                return Soprano.Error.Error()
    class Inference():
        """"""
        class Rule():
            """"""
            def __init__(self):
                '''void Soprano.Inference.Rule.__init__()'''
            def __init__(self, other):
                '''void Soprano.Inference.Rule.__init__(Soprano.Inference.Rule other)'''
            def isValid(self):
                '''bool Soprano.Inference.Rule.isValid()'''
                return bool()
            def bindPreconditions(self, bindings):
                '''list-of-Soprano.Statement Soprano.Inference.Rule.bindPreconditions(Soprano.BindingSet bindings)'''
                return [Soprano.Statement()]
            def bindEffect(self, bindings):
                '''Soprano.Statement Soprano.Inference.Rule.bindEffect(Soprano.BindingSet bindings)'''
                return Soprano.Statement()
            def createSparqlQuery(self, bindVariables = False):
                '''QString Soprano.Inference.Rule.createSparqlQuery(bool bindVariables = False)'''
                return QString()
            def boundToStatement(self):
                '''Soprano.Statement Soprano.Inference.Rule.boundToStatement()'''
                return Soprano.Statement()
            def bindToStatement(self, statement):
                '''void Soprano.Inference.Rule.bindToStatement(Soprano.Statement statement)'''
            def match(self, statement):
                '''bool Soprano.Inference.Rule.match(Soprano.Statement statement)'''
                return bool()
            def setEffect(self):
                '''Soprano.Inference.StatementPattern Soprano.Inference.Rule.setEffect()'''
                return Soprano.Inference.StatementPattern()
            def effect(self):
                '''Soprano.Inference.StatementPattern Soprano.Inference.Rule.effect()'''
                return Soprano.Inference.StatementPattern()
            def addPrecondition(self):
                '''Soprano.Inference.StatementPattern Soprano.Inference.Rule.addPrecondition()'''
                return Soprano.Inference.StatementPattern()
            def preconditions(self):
                '''list-of-Soprano.Inference.StatementPattern Soprano.Inference.Rule.preconditions()'''
                return [Soprano.Inference.StatementPattern()]
    class StorageModel(Soprano.Model):
        """"""
        def __init__(self, backend):
            '''void Soprano.StorageModel.__init__(Soprano.Backend backend)'''
        def backend(self):
            '''Soprano.Backend Soprano.StorageModel.backend()'''
            return Soprano.Backend()
        def removeAllStatements(self, statement):
            '''Soprano.Error.ErrorCode Soprano.StorageModel.removeAllStatements(Soprano.Statement statement)'''
            return Soprano.Error.ErrorCode()
        def containsAnyStatement(self, statement):
            '''bool Soprano.StorageModel.containsAnyStatement(Soprano.Statement statement)'''
            return bool()
        def containsStatement(self, statement):
            '''bool Soprano.StorageModel.containsStatement(Soprano.Statement statement)'''
            return bool()
        def isEmpty(self):
            '''bool Soprano.StorageModel.isEmpty()'''
            return bool()
    class Vocabulary():
        """"""
        class RDF():
            """"""
            def value(self):
                '''static QUrl Soprano.Vocabulary.RDF.value()'''
                return QUrl()
            def type(self):
                '''static QUrl Soprano.Vocabulary.RDF.type()'''
                return QUrl()
            def subject(self):
                '''static QUrl Soprano.Vocabulary.RDF.subject()'''
                return QUrl()
            def rest(self):
                '''static QUrl Soprano.Vocabulary.RDF.rest()'''
                return QUrl()
            def predicate(self):
                '''static QUrl Soprano.Vocabulary.RDF.predicate()'''
                return QUrl()
            def object(self):
                '''static QUrl Soprano.Vocabulary.RDF.object()'''
                return QUrl()
            def nil(self):
                '''static QUrl Soprano.Vocabulary.RDF.nil()'''
                return QUrl()
            def first(self):
                '''static QUrl Soprano.Vocabulary.RDF.first()'''
                return QUrl()
            def XMLLiteral(self):
                '''static QUrl Soprano.Vocabulary.RDF.XMLLiteral()'''
                return QUrl()
            def Statement(self):
                '''static QUrl Soprano.Vocabulary.RDF.Statement()'''
                return QUrl()
            def Seq(self):
                '''static QUrl Soprano.Vocabulary.RDF.Seq()'''
                return QUrl()
            def Property(self):
                '''static QUrl Soprano.Vocabulary.RDF.Property()'''
                return QUrl()
            def List(self):
                '''static QUrl Soprano.Vocabulary.RDF.List()'''
                return QUrl()
            def Bag(self):
                '''static QUrl Soprano.Vocabulary.RDF.Bag()'''
                return QUrl()
            def Alt(self):
                '''static QUrl Soprano.Vocabulary.RDF.Alt()'''
                return QUrl()
            def rdfNamespace(self):
                '''static QUrl Soprano.Vocabulary.RDF.rdfNamespace()'''
                return QUrl()
    class Util():
        """"""
    class Vocabulary():
        """"""
        class RDFS():
            """"""
            def subPropertyOf(self):
                '''static QUrl Soprano.Vocabulary.RDFS.subPropertyOf()'''
                return QUrl()
            def subClassOf(self):
                '''static QUrl Soprano.Vocabulary.RDFS.subClassOf()'''
                return QUrl()
            def seeAlso(self):
                '''static QUrl Soprano.Vocabulary.RDFS.seeAlso()'''
                return QUrl()
            def range(self):
                '''static QUrl Soprano.Vocabulary.RDFS.range()'''
                return QUrl()
            def member(self):
                '''static QUrl Soprano.Vocabulary.RDFS.member()'''
                return QUrl()
            def label(self):
                '''static QUrl Soprano.Vocabulary.RDFS.label()'''
                return QUrl()
            def isDefinedBy(self):
                '''static QUrl Soprano.Vocabulary.RDFS.isDefinedBy()'''
                return QUrl()
            def domain(self):
                '''static QUrl Soprano.Vocabulary.RDFS.domain()'''
                return QUrl()
            def comment(self):
                '''static QUrl Soprano.Vocabulary.RDFS.comment()'''
                return QUrl()
            def Resource(self):
                '''static QUrl Soprano.Vocabulary.RDFS.Resource()'''
                return QUrl()
            def Literal(self):
                '''static QUrl Soprano.Vocabulary.RDFS.Literal()'''
                return QUrl()
            def Datatype(self):
                '''static QUrl Soprano.Vocabulary.RDFS.Datatype()'''
                return QUrl()
            def ContainerMembershipProperty(self):
                '''static QUrl Soprano.Vocabulary.RDFS.ContainerMembershipProperty()'''
                return QUrl()
            def Container(self):
                '''static QUrl Soprano.Vocabulary.RDFS.Container()'''
                return QUrl()
            def Class(self):
                '''static QUrl Soprano.Vocabulary.RDFS.Class()'''
                return QUrl()
            def rdfsNamespace(self):
                '''static QUrl Soprano.Vocabulary.RDFS.rdfsNamespace()'''
                return QUrl()
    class Error():
        """"""
        # Enum Soprano.Error.ErrorCode
        ErrorNone = 0
        ErrorInvalidArgument = 0
        ErrorInvalidStatement = 0
        ErrorNotSupported = 0
        ErrorParsingFailed = 0
        ErrorPermissionDenied = 0
        ErrorTimeout = 0
        ErrorUnknown = 0
    
        def convertErrorCode(self, code):
            '''static Soprano.Error.ErrorCode Soprano.Error.convertErrorCode(int code)'''
            return Soprano.Error.ErrorCode()
        def errorMessage(self):
            '''static Soprano.Error.ErrorCode Soprano.Error.errorMessage()'''
            return Soprano.Error.ErrorCode()
    class Client():
        """"""
        class DBusStatementIterator(Soprano.StatementIterator):
            """"""
            def __init__(self, serviceName, dbusObject):
                '''void Soprano.Client.DBusStatementIterator.__init__(QString serviceName, QString dbusObject)'''
            def __init__(self):
                '''Soprano.Client.DBusStatementIterator Soprano.Client.DBusStatementIterator.__init__()'''
                return Soprano.Client.DBusStatementIterator()
    class PluginManager(QObject):
        """"""
        def loadCustomSerializer(self, path):
            '''Soprano.Serializer Soprano.PluginManager.loadCustomSerializer(QString path)'''
            return Soprano.Serializer()
        def loadCustomParser(self, path):
            '''Soprano.Parser Soprano.PluginManager.loadCustomParser(QString path)'''
            return Soprano.Parser()
        def loadCustomBackend(self, path):
            '''Soprano.Backend Soprano.PluginManager.loadCustomBackend(QString path)'''
            return Soprano.Backend()
        def loadCustomPlugin(self, path):
            '''bool Soprano.PluginManager.loadCustomPlugin(QString path)'''
            return bool()
        def instance(self):
            '''static Soprano.PluginManager Soprano.PluginManager.instance()'''
            return Soprano.PluginManager()
        def allSerializers(self):
            '''unknown-type Soprano.PluginManager.allSerializers()'''
            return unknown-type()
        def discoverSerializerForSerialization(self, serialization, userSerialization = QString()):
            '''Soprano.Serializer Soprano.PluginManager.discoverSerializerForSerialization(Soprano.RdfSerialization serialization, QString userSerialization = QString())'''
            return Soprano.Serializer()
        def discoverSerializerByName(self, name):
            '''Soprano.Serializer Soprano.PluginManager.discoverSerializerByName(QString name)'''
            return Soprano.Serializer()
        def allParsers(self):
            '''unknown-type Soprano.PluginManager.allParsers()'''
            return unknown-type()
        def discoverParserForSerialization(self, serialization, userSerialization = QString()):
            '''Soprano.Parser Soprano.PluginManager.discoverParserForSerialization(Soprano.RdfSerialization serialization, QString userSerialization = QString())'''
            return Soprano.Parser()
        def discoverParserByName(self, name):
            '''Soprano.Parser Soprano.PluginManager.discoverParserByName(QString name)'''
            return Soprano.Parser()
        def allBackends(self):
            '''unknown-type Soprano.PluginManager.allBackends()'''
            return unknown-type()
        def discoverBackendByFeatures(self, features, userFeatures = QStringList()):
            '''Soprano.Backend Soprano.PluginManager.discoverBackendByFeatures(Soprano.BackendFeatures features, QStringList userFeatures = QStringList())'''
            return Soprano.Backend()
        def discoverBackendByName(self, name):
            '''Soprano.Backend Soprano.PluginManager.discoverBackendByName(QString name)'''
            return Soprano.Backend()
        def setPluginSearchPath(self, path, useDefaults = True):
            '''void Soprano.PluginManager.setPluginSearchPath(QStringList path, bool useDefaults = True)'''


