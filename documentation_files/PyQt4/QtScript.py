class pyqtSignal():
 def connect(self, targetSignal): pass
 def emit(self, *args): pass
from QtCore import *

class QScriptClass():
    """"""
    # Enum QScriptClass.Extension
    Callable = 0
    HasInstance = 0

    # Enum QScriptClass.QueryFlag
    HandlesReadAccess = 0
    HandlesWriteAccess = 0

    def __init__(self, engine):
        '''void QScriptClass.__init__(QScriptEngine engine)'''
    def extension(self, extension, argument = QVariant()):
        '''QVariant QScriptClass.extension(QScriptClass.Extension extension, QVariant argument = QVariant())'''
        return QVariant()
    def supportsExtension(self, extension):
        '''bool QScriptClass.supportsExtension(QScriptClass.Extension extension)'''
        return bool()
    def name(self):
        '''QString QScriptClass.name()'''
        return QString()
    def prototype(self):
        '''QScriptValue QScriptClass.prototype()'''
        return QScriptValue()
    def newIterator(self, object):
        '''QScriptClassPropertyIterator QScriptClass.newIterator(QScriptValue object)'''
        return QScriptClassPropertyIterator()
    def propertyFlags(self, object, name, id):
        '''QScriptValue.PropertyFlags QScriptClass.propertyFlags(QScriptValue object, QScriptString name, int id)'''
        return QScriptValue.PropertyFlags()
    def setProperty(self, object, name, id, value):
        '''void QScriptClass.setProperty(QScriptValue object, QScriptString name, int id, QScriptValue value)'''
    def property(self, object, name, id):
        '''QScriptValue QScriptClass.property(QScriptValue object, QScriptString name, int id)'''
        return QScriptValue()
    def queryProperty(self, object, name, flags, id):
        '''QScriptClass.QueryFlags QScriptClass.queryProperty(QScriptValue object, QScriptString name, QScriptClass.QueryFlags flags, int id)'''
        return QScriptClass.QueryFlags()
    def engine(self):
        '''QScriptEngine QScriptClass.engine()'''
        return QScriptEngine()
    class QueryFlags():
        """"""
        def __init__(self):
            '''QScriptClass.QueryFlags QScriptClass.QueryFlags.__init__()'''
            return QScriptClass.QueryFlags()
        def __init__(self):
            '''int QScriptClass.QueryFlags.__init__()'''
            return int()
        def __init__(self):
            '''void QScriptClass.QueryFlags.__init__()'''
        def __bool__(self):
            '''int QScriptClass.QueryFlags.__bool__()'''
            return int()
        def __ne__(self, f):
            '''bool QScriptClass.QueryFlags.__ne__(QScriptClass.QueryFlags f)'''
            return bool()
        def __eq__(self, f):
            '''bool QScriptClass.QueryFlags.__eq__(QScriptClass.QueryFlags f)'''
            return bool()
        def __invert__(self):
            '''QScriptClass.QueryFlags QScriptClass.QueryFlags.__invert__()'''
            return QScriptClass.QueryFlags()
        def __and__(self, mask):
            '''QScriptClass.QueryFlags QScriptClass.QueryFlags.__and__(int mask)'''
            return QScriptClass.QueryFlags()
        def __xor__(self, f):
            '''QScriptClass.QueryFlags QScriptClass.QueryFlags.__xor__(QScriptClass.QueryFlags f)'''
            return QScriptClass.QueryFlags()
        def __xor__(self, f):
            '''QScriptClass.QueryFlags QScriptClass.QueryFlags.__xor__(int f)'''
            return QScriptClass.QueryFlags()
        def __or__(self, f):
            '''QScriptClass.QueryFlags QScriptClass.QueryFlags.__or__(QScriptClass.QueryFlags f)'''
            return QScriptClass.QueryFlags()
        def __or__(self, f):
            '''QScriptClass.QueryFlags QScriptClass.QueryFlags.__or__(int f)'''
            return QScriptClass.QueryFlags()
        def __int__(self):
            '''int QScriptClass.QueryFlags.__int__()'''
            return int()
        def __ixor__(self, f):
            '''QScriptClass.QueryFlags QScriptClass.QueryFlags.__ixor__(QScriptClass.QueryFlags f)'''
            return QScriptClass.QueryFlags()
        def __ior__(self, f):
            '''QScriptClass.QueryFlags QScriptClass.QueryFlags.__ior__(QScriptClass.QueryFlags f)'''
            return QScriptClass.QueryFlags()
        def __iand__(self, mask):
            '''QScriptClass.QueryFlags QScriptClass.QueryFlags.__iand__(int mask)'''
            return QScriptClass.QueryFlags()


class QScriptClassPropertyIterator():
    """"""
    def __init__(self, object):
        '''void QScriptClassPropertyIterator.__init__(QScriptValue object)'''
    def flags(self):
        '''QScriptValue.PropertyFlags QScriptClassPropertyIterator.flags()'''
        return QScriptValue.PropertyFlags()
    def id(self):
        '''int QScriptClassPropertyIterator.id()'''
        return int()
    def name(self):
        '''abstract QScriptString QScriptClassPropertyIterator.name()'''
        return QScriptString()
    def toBack(self):
        '''abstract void QScriptClassPropertyIterator.toBack()'''
    def toFront(self):
        '''abstract void QScriptClassPropertyIterator.toFront()'''
    def previous(self):
        '''abstract void QScriptClassPropertyIterator.previous()'''
    def hasPrevious(self):
        '''abstract bool QScriptClassPropertyIterator.hasPrevious()'''
        return bool()
    def next(self):
        '''abstract void QScriptClassPropertyIterator.next()'''
    def hasNext(self):
        '''abstract bool QScriptClassPropertyIterator.hasNext()'''
        return bool()
    def object(self):
        '''QScriptValue QScriptClassPropertyIterator.object()'''
        return QScriptValue()


class QScriptContext():
    """"""
    # Enum QScriptContext.Error
    UnknownError = 0
    ReferenceError = 0
    SyntaxError = 0
    TypeError = 0
    RangeError = 0
    URIError = 0

    # Enum QScriptContext.ExecutionState
    NormalState = 0
    ExceptionState = 0

    def toString(self):
        '''QString QScriptContext.toString()'''
        return QString()
    def throwError(self, error, text):
        '''QScriptValue QScriptContext.throwError(QScriptContext.Error error, QString text)'''
        return QScriptValue()
    def throwError(self, text):
        '''QScriptValue QScriptContext.throwError(QString text)'''
        return QScriptValue()
    def throwValue(self, value):
        '''QScriptValue QScriptContext.throwValue(QScriptValue value)'''
        return QScriptValue()
    def backtrace(self):
        '''QStringList QScriptContext.backtrace()'''
        return QStringList()
    def isCalledAsConstructor(self):
        '''bool QScriptContext.isCalledAsConstructor()'''
        return bool()
    def setThisObject(self, thisObject):
        '''void QScriptContext.setThisObject(QScriptValue thisObject)'''
    def thisObject(self):
        '''QScriptValue QScriptContext.thisObject()'''
        return QScriptValue()
    def setActivationObject(self, activation):
        '''void QScriptContext.setActivationObject(QScriptValue activation)'''
    def activationObject(self):
        '''QScriptValue QScriptContext.activationObject()'''
        return QScriptValue()
    def argumentsObject(self):
        '''QScriptValue QScriptContext.argumentsObject()'''
        return QScriptValue()
    def argument(self, index):
        '''QScriptValue QScriptContext.argument(int index)'''
        return QScriptValue()
    def argumentCount(self):
        '''int QScriptContext.argumentCount()'''
        return int()
    def callee(self):
        '''QScriptValue QScriptContext.callee()'''
        return QScriptValue()
    def state(self):
        '''QScriptContext.ExecutionState QScriptContext.state()'''
        return QScriptContext.ExecutionState()
    def engine(self):
        '''QScriptEngine QScriptContext.engine()'''
        return QScriptEngine()
    def parentContext(self):
        '''QScriptContext QScriptContext.parentContext()'''
        return QScriptContext()


class QScriptContextInfo():
    """"""
    # Enum QScriptContextInfo.FunctionType
    ScriptFunction = 0
    QtFunction = 0
    QtPropertyFunction = 0
    NativeFunction = 0

    def __init__(self, context):
        '''void QScriptContextInfo.__init__(QScriptContext context)'''
    def __init__(self, other):
        '''void QScriptContextInfo.__init__(QScriptContextInfo other)'''
    def __init__(self):
        '''void QScriptContextInfo.__init__()'''
    def __ne__(self, other):
        '''bool QScriptContextInfo.__ne__(QScriptContextInfo other)'''
        return bool()
    def __eq__(self, other):
        '''bool QScriptContextInfo.__eq__(QScriptContextInfo other)'''
        return bool()
    def functionMetaIndex(self):
        '''int QScriptContextInfo.functionMetaIndex()'''
        return int()
    def functionEndLineNumber(self):
        '''int QScriptContextInfo.functionEndLineNumber()'''
        return int()
    def functionStartLineNumber(self):
        '''int QScriptContextInfo.functionStartLineNumber()'''
        return int()
    def functionParameterNames(self):
        '''QStringList QScriptContextInfo.functionParameterNames()'''
        return QStringList()
    def functionType(self):
        '''QScriptContextInfo.FunctionType QScriptContextInfo.functionType()'''
        return QScriptContextInfo.FunctionType()
    def functionName(self):
        '''QString QScriptContextInfo.functionName()'''
        return QString()
    def columnNumber(self):
        '''int QScriptContextInfo.columnNumber()'''
        return int()
    def lineNumber(self):
        '''int QScriptContextInfo.lineNumber()'''
        return int()
    def fileName(self):
        '''QString QScriptContextInfo.fileName()'''
        return QString()
    def scriptId(self):
        '''int QScriptContextInfo.scriptId()'''
        return int()
    def isNull(self):
        '''bool QScriptContextInfo.isNull()'''
        return bool()


class QScriptEngine(QObject):
    """"""
    # Enum QScriptEngine.QObjectWrapOption
    ExcludeChildObjects = 0
    ExcludeSuperClassMethods = 0
    ExcludeSuperClassProperties = 0
    AutoCreateDynamicProperties = 0
    SkipMethodsInEnumeration = 0
    PreferExistingWrapperObject = 0
    ExcludeSuperClassContents = 0
    ExcludeDeleteLater = 0
    ExcludeSlots = 0

    # Enum QScriptEngine.ValueOwnership
    QtOwnership = 0
    ScriptOwnership = 0
    AutoOwnership = 0

    def __init__(self):
        '''void QScriptEngine.__init__()'''
    def __init__(self, parent):
        '''void QScriptEngine.__init__(QObject parent)'''
    def reportAdditionalMemoryCost(self, size):
        '''void QScriptEngine.reportAdditionalMemoryCost(int size)'''
    signalHandlerException = pyqtSignal() # void signalHandlerException(const QScriptValueamp;) - signal
    def toObject(self, value):
        '''QScriptValue QScriptEngine.toObject(QScriptValue value)'''
        return QScriptValue()
    def installTranslatorFunctions(self, object = QScriptValue()):
        '''void QScriptEngine.installTranslatorFunctions(QScriptValue object = QScriptValue())'''
    def checkSyntax(self, program):
        '''static QScriptSyntaxCheckResult QScriptEngine.checkSyntax(QString program)'''
        return QScriptSyntaxCheckResult()
    def setGlobalObject(self, object):
        '''void QScriptEngine.setGlobalObject(QScriptValue object)'''
    def toStringHandle(self, str):
        '''QScriptString QScriptEngine.toStringHandle(QString str)'''
        return QScriptString()
    def agent(self):
        '''QScriptEngineAgent QScriptEngine.agent()'''
        return QScriptEngineAgent()
    def setAgent(self, agent):
        '''void QScriptEngine.setAgent(QScriptEngineAgent agent)'''
    def importedExtensions(self):
        '''QStringList QScriptEngine.importedExtensions()'''
        return QStringList()
    def availableExtensions(self):
        '''QStringList QScriptEngine.availableExtensions()'''
        return QStringList()
    def clearExceptions(self):
        '''void QScriptEngine.clearExceptions()'''
    def abortEvaluation(self, result = QScriptValue()):
        '''void QScriptEngine.abortEvaluation(QScriptValue result = QScriptValue())'''
    def isEvaluating(self):
        '''bool QScriptEngine.isEvaluating()'''
        return bool()
    def processEventsInterval(self):
        '''int QScriptEngine.processEventsInterval()'''
        return int()
    def setProcessEventsInterval(self, interval):
        '''void QScriptEngine.setProcessEventsInterval(int interval)'''
    def collectGarbage(self):
        '''void QScriptEngine.collectGarbage()'''
    def importExtension(self, extension):
        '''QScriptValue QScriptEngine.importExtension(QString extension)'''
        return QScriptValue()
    def setDefaultPrototype(self, metaTypeId, prototype):
        '''void QScriptEngine.setDefaultPrototype(int metaTypeId, QScriptValue prototype)'''
    def defaultPrototype(self, metaTypeId):
        '''QScriptValue QScriptEngine.defaultPrototype(int metaTypeId)'''
        return QScriptValue()
    def newQMetaObject(self, metaObject, ctor = QScriptValue()):
        '''QScriptValue QScriptEngine.newQMetaObject(QMetaObject metaObject, QScriptValue ctor = QScriptValue())'''
        return QScriptValue()
    def newQObject(self, object, ownership = None, options = 0):
        '''QScriptValue QScriptEngine.newQObject(QObject object, QScriptEngine.ValueOwnership ownership = QScriptEngine.QtOwnership, QScriptEngine.QObjectWrapOptions options = 0)'''
        return QScriptValue()
    def newQObject(self, scriptObject, qtObject, ownership = None, options = 0):
        '''QScriptValue QScriptEngine.newQObject(QScriptValue scriptObject, QObject qtObject, QScriptEngine.ValueOwnership ownership = QScriptEngine.QtOwnership, QScriptEngine.QObjectWrapOptions options = 0)'''
        return QScriptValue()
    def newDate(self, value):
        '''QScriptValue QScriptEngine.newDate(float value)'''
        return QScriptValue()
    def newDate(self, value):
        '''QScriptValue QScriptEngine.newDate(QDateTime value)'''
        return QScriptValue()
    def newArray(self, length = 0):
        '''QScriptValue QScriptEngine.newArray(int length = 0)'''
        return QScriptValue()
    def newObject(self):
        '''QScriptValue QScriptEngine.newObject()'''
        return QScriptValue()
    def newObject(self, scriptClass, data = QScriptValue()):
        '''QScriptValue QScriptEngine.newObject(QScriptClass scriptClass, QScriptValue data = QScriptValue())'''
        return QScriptValue()
    def newRegExp(self, regexp):
        '''QScriptValue QScriptEngine.newRegExp(QRegExp regexp)'''
        return QScriptValue()
    def newRegExp(self, pattern, flags):
        '''QScriptValue QScriptEngine.newRegExp(QString pattern, QString flags)'''
        return QScriptValue()
    def newVariant(self, value):
        '''QScriptValue QScriptEngine.newVariant(QVariant value)'''
        return QScriptValue()
    def newVariant(self, object, value):
        '''QScriptValue QScriptEngine.newVariant(QScriptValue object, QVariant value)'''
        return QScriptValue()
    def newFunction(self, signature, length = 0):
        '''QScriptValue QScriptEngine.newFunction(callable signature, int length = 0)'''
        return QScriptValue()
    def newFunction(self, signature, prototype, length = 0):
        '''QScriptValue QScriptEngine.newFunction(callable signature, QScriptValue prototype, int length = 0)'''
        return QScriptValue()
    def undefinedValue(self):
        '''QScriptValue QScriptEngine.undefinedValue()'''
        return QScriptValue()
    def nullValue(self):
        '''QScriptValue QScriptEngine.nullValue()'''
        return QScriptValue()
    def uncaughtExceptionLineNumber(self):
        '''int QScriptEngine.uncaughtExceptionLineNumber()'''
        return int()
    def uncaughtException(self):
        '''QScriptValue QScriptEngine.uncaughtException()'''
        return QScriptValue()
    def uncaughtExceptionBacktrace(self):
        '''QStringList QScriptEngine.uncaughtExceptionBacktrace()'''
        return QStringList()
    def hasUncaughtException(self):
        '''bool QScriptEngine.hasUncaughtException()'''
        return bool()
    def evaluate(self, program, fileName = QString(), lineNumber = 1):
        '''QScriptValue QScriptEngine.evaluate(QString program, QString fileName = QString(), int lineNumber = 1)'''
        return QScriptValue()
    def canEvaluate(self, program):
        '''bool QScriptEngine.canEvaluate(QString program)'''
        return bool()
    def popContext(self):
        '''void QScriptEngine.popContext()'''
    def pushContext(self):
        '''QScriptContext QScriptEngine.pushContext()'''
        return QScriptContext()
    def currentContext(self):
        '''QScriptContext QScriptEngine.currentContext()'''
        return QScriptContext()
    def globalObject(self):
        '''QScriptValue QScriptEngine.globalObject()'''
        return QScriptValue()
    class QObjectWrapOptions():
        """"""
        def __init__(self):
            '''QScriptEngine.QObjectWrapOptions QScriptEngine.QObjectWrapOptions.__init__()'''
            return QScriptEngine.QObjectWrapOptions()
        def __init__(self):
            '''int QScriptEngine.QObjectWrapOptions.__init__()'''
            return int()
        def __init__(self):
            '''void QScriptEngine.QObjectWrapOptions.__init__()'''
        def __bool__(self):
            '''int QScriptEngine.QObjectWrapOptions.__bool__()'''
            return int()
        def __ne__(self, f):
            '''bool QScriptEngine.QObjectWrapOptions.__ne__(QScriptEngine.QObjectWrapOptions f)'''
            return bool()
        def __eq__(self, f):
            '''bool QScriptEngine.QObjectWrapOptions.__eq__(QScriptEngine.QObjectWrapOptions f)'''
            return bool()
        def __invert__(self):
            '''QScriptEngine.QObjectWrapOptions QScriptEngine.QObjectWrapOptions.__invert__()'''
            return QScriptEngine.QObjectWrapOptions()
        def __and__(self, mask):
            '''QScriptEngine.QObjectWrapOptions QScriptEngine.QObjectWrapOptions.__and__(int mask)'''
            return QScriptEngine.QObjectWrapOptions()
        def __xor__(self, f):
            '''QScriptEngine.QObjectWrapOptions QScriptEngine.QObjectWrapOptions.__xor__(QScriptEngine.QObjectWrapOptions f)'''
            return QScriptEngine.QObjectWrapOptions()
        def __xor__(self, f):
            '''QScriptEngine.QObjectWrapOptions QScriptEngine.QObjectWrapOptions.__xor__(int f)'''
            return QScriptEngine.QObjectWrapOptions()
        def __or__(self, f):
            '''QScriptEngine.QObjectWrapOptions QScriptEngine.QObjectWrapOptions.__or__(QScriptEngine.QObjectWrapOptions f)'''
            return QScriptEngine.QObjectWrapOptions()
        def __or__(self, f):
            '''QScriptEngine.QObjectWrapOptions QScriptEngine.QObjectWrapOptions.__or__(int f)'''
            return QScriptEngine.QObjectWrapOptions()
        def __int__(self):
            '''int QScriptEngine.QObjectWrapOptions.__int__()'''
            return int()
        def __ixor__(self, f):
            '''QScriptEngine.QObjectWrapOptions QScriptEngine.QObjectWrapOptions.__ixor__(QScriptEngine.QObjectWrapOptions f)'''
            return QScriptEngine.QObjectWrapOptions()
        def __ior__(self, f):
            '''QScriptEngine.QObjectWrapOptions QScriptEngine.QObjectWrapOptions.__ior__(QScriptEngine.QObjectWrapOptions f)'''
            return QScriptEngine.QObjectWrapOptions()
        def __iand__(self, mask):
            '''QScriptEngine.QObjectWrapOptions QScriptEngine.QObjectWrapOptions.__iand__(int mask)'''
            return QScriptEngine.QObjectWrapOptions()


class QScriptSyntaxCheckResult():
    """"""
    # Enum QScriptSyntaxCheckResult.State
    Error = 0
    Intermediate = 0
    Valid = 0

    def __init__(self, other):
        '''void QScriptSyntaxCheckResult.__init__(QScriptSyntaxCheckResult other)'''
    def errorMessage(self):
        '''QString QScriptSyntaxCheckResult.errorMessage()'''
        return QString()
    def errorColumnNumber(self):
        '''int QScriptSyntaxCheckResult.errorColumnNumber()'''
        return int()
    def errorLineNumber(self):
        '''int QScriptSyntaxCheckResult.errorLineNumber()'''
        return int()
    def state(self):
        '''QScriptSyntaxCheckResult.State QScriptSyntaxCheckResult.state()'''
        return QScriptSyntaxCheckResult.State()


class QScriptEngineAgent():
    """"""
    # Enum QScriptEngineAgent.Extension
    DebuggerInvocationRequest = 0

    def __init__(self, engine):
        '''void QScriptEngineAgent.__init__(QScriptEngine engine)'''
    def engine(self):
        '''QScriptEngine QScriptEngineAgent.engine()'''
        return QScriptEngine()
    def extension(self, extension, argument = QVariant()):
        '''QVariant QScriptEngineAgent.extension(QScriptEngineAgent.Extension extension, QVariant argument = QVariant())'''
        return QVariant()
    def supportsExtension(self, extension):
        '''bool QScriptEngineAgent.supportsExtension(QScriptEngineAgent.Extension extension)'''
        return bool()
    def exceptionCatch(self, scriptId, exception):
        '''void QScriptEngineAgent.exceptionCatch(int scriptId, QScriptValue exception)'''
    def exceptionThrow(self, scriptId, exception, hasHandler):
        '''void QScriptEngineAgent.exceptionThrow(int scriptId, QScriptValue exception, bool hasHandler)'''
    def positionChange(self, scriptId, lineNumber, columnNumber):
        '''void QScriptEngineAgent.positionChange(int scriptId, int lineNumber, int columnNumber)'''
    def functionExit(self, scriptId, returnValue):
        '''void QScriptEngineAgent.functionExit(int scriptId, QScriptValue returnValue)'''
    def functionEntry(self, scriptId):
        '''void QScriptEngineAgent.functionEntry(int scriptId)'''
    def contextPop(self):
        '''void QScriptEngineAgent.contextPop()'''
    def contextPush(self):
        '''void QScriptEngineAgent.contextPush()'''
    def scriptUnload(self, id):
        '''void QScriptEngineAgent.scriptUnload(int id)'''
    def scriptLoad(self, id, program, fileName, baseLineNumber):
        '''void QScriptEngineAgent.scriptLoad(int id, QString program, QString fileName, int baseLineNumber)'''


class QScriptString():
    """"""
    def __init__(self):
        '''void QScriptString.__init__()'''
    def __init__(self, other):
        '''void QScriptString.__init__(QScriptString other)'''
    def toArrayIndex(self, ok):
        '''int QScriptString.toArrayIndex(bool ok)'''
        return int()
    def toString(self):
        '''QString QScriptString.toString()'''
        return QString()
    def __ne__(self, other):
        '''bool QScriptString.__ne__(QScriptString other)'''
        return bool()
    def __eq__(self, other):
        '''bool QScriptString.__eq__(QScriptString other)'''
        return bool()
    def isValid(self):
        '''bool QScriptString.isValid()'''
        return bool()
    def __hash__(self):
        '''int QScriptString.__hash__()'''
        return int()


class QScriptValue():
    """"""
    # Enum QScriptValue.SpecialValue
    NullValue = 0
    UndefinedValue = 0

    # Enum QScriptValue.PropertyFlag
    ReadOnly = 0
    Undeletable = 0
    SkipInEnumeration = 0
    PropertyGetter = 0
    PropertySetter = 0
    QObjectMember = 0
    KeepExistingFlags = 0
    UserRange = 0

    # Enum QScriptValue.ResolveFlag
    ResolveLocal = 0
    ResolvePrototype = 0
    ResolveScope = 0
    ResolveFull = 0

    def __init__(self):
        '''void QScriptValue.__init__()'''
    def __init__(self, other):
        '''void QScriptValue.__init__(QScriptValue other)'''
    def __init__(self, value):
        '''void QScriptValue.__init__(QScriptValue.SpecialValue value)'''
    def __init__(self, engine, val):
        '''void QScriptValue.__init__(QScriptEngine engine, QScriptValue.SpecialValue val)'''
    def __init__(self, value):
        '''void QScriptValue.__init__(bool value)'''
    def __init__(self, engine, val):
        '''void QScriptValue.__init__(QScriptEngine engine, bool val)'''
    def __init__(self, value):
        '''void QScriptValue.__init__(int value)'''
    def __init__(self, engine, val):
        '''void QScriptValue.__init__(QScriptEngine engine, int val)'''
    def __init__(self, value):
        '''void QScriptValue.__init__(float value)'''
    def __init__(self, engine, val):
        '''void QScriptValue.__init__(QScriptEngine engine, float val)'''
    def __init__(self, value):
        '''void QScriptValue.__init__(QString value)'''
    def __init__(self, engine, val):
        '''void QScriptValue.__init__(QScriptEngine engine, QString val)'''
    def setScriptClass(self, scriptClass):
        '''void QScriptValue.setScriptClass(QScriptClass scriptClass)'''
    def scriptClass(self):
        '''QScriptClass QScriptValue.scriptClass()'''
        return QScriptClass()
    def setData(self, data):
        '''void QScriptValue.setData(QScriptValue data)'''
    def data(self):
        '''QScriptValue QScriptValue.data()'''
        return QScriptValue()
    def construct(self, args = QScriptValueList()):
        '''QScriptValue QScriptValue.construct(list-of-QScriptValue args = QScriptValueList())'''
        return QScriptValue()
    def construct(self, arguments):
        '''QScriptValue QScriptValue.construct(QScriptValue arguments)'''
        return QScriptValue()
    def call(self, thisObject = QScriptValue(), args = QScriptValueList()):
        '''QScriptValue QScriptValue.call(QScriptValue thisObject = QScriptValue(), list-of-QScriptValue args = QScriptValueList())'''
        return QScriptValue()
    def call(self, thisObject, arguments):
        '''QScriptValue QScriptValue.call(QScriptValue thisObject, QScriptValue arguments)'''
        return QScriptValue()
    def propertyFlags(self, name, mode = None):
        '''QScriptValue.PropertyFlags QScriptValue.propertyFlags(QString name, QScriptValue.ResolveFlags mode = QScriptValue.ResolvePrototype)'''
        return QScriptValue.PropertyFlags()
    def propertyFlags(self, name, mode = None):
        '''QScriptValue.PropertyFlags QScriptValue.propertyFlags(QScriptString name, QScriptValue.ResolveFlags mode = QScriptValue.ResolvePrototype)'''
        return QScriptValue.PropertyFlags()
    def setProperty(self, name, value, flags = None):
        '''void QScriptValue.setProperty(QString name, QScriptValue value, QScriptValue.PropertyFlags flags = QScriptValue.KeepExistingFlags)'''
    def setProperty(self, name, value, flags = None):
        '''void QScriptValue.setProperty(QScriptString name, QScriptValue value, QScriptValue.PropertyFlags flags = QScriptValue.KeepExistingFlags)'''
    def setProperty(self, arrayIndex, value, flags = None):
        '''void QScriptValue.setProperty(int arrayIndex, QScriptValue value, QScriptValue.PropertyFlags flags = QScriptValue.KeepExistingFlags)'''
    def property(self, name, mode = None):
        '''QScriptValue QScriptValue.property(QString name, QScriptValue.ResolveFlags mode = QScriptValue.ResolvePrototype)'''
        return QScriptValue()
    def property(self, name, mode = None):
        '''QScriptValue QScriptValue.property(QScriptString name, QScriptValue.ResolveFlags mode = QScriptValue.ResolvePrototype)'''
        return QScriptValue()
    def property(self, arrayIndex, mode = None):
        '''QScriptValue QScriptValue.property(int arrayIndex, QScriptValue.ResolveFlags mode = QScriptValue.ResolvePrototype)'''
        return QScriptValue()
    def setPrototype(self, prototype):
        '''void QScriptValue.setPrototype(QScriptValue prototype)'''
    def prototype(self):
        '''QScriptValue QScriptValue.prototype()'''
        return QScriptValue()
    def strictlyEquals(self, other):
        '''bool QScriptValue.strictlyEquals(QScriptValue other)'''
        return bool()
    def equals(self, other):
        '''bool QScriptValue.equals(QScriptValue other)'''
        return bool()
    def lessThan(self, other):
        '''bool QScriptValue.lessThan(QScriptValue other)'''
        return bool()
    def instanceOf(self, ctor):
        '''bool QScriptValue.instanceOf(QScriptValue ctor)'''
        return bool()
    def toRegExp(self):
        '''QRegExp QScriptValue.toRegExp()'''
        return QRegExp()
    def toDateTime(self):
        '''QDateTime QScriptValue.toDateTime()'''
        return QDateTime()
    def toObject(self):
        '''QScriptValue QScriptValue.toObject()'''
        return QScriptValue()
    def toQMetaObject(self):
        '''QMetaObject QScriptValue.toQMetaObject()'''
        return QMetaObject()
    def toQObject(self):
        '''QObject QScriptValue.toQObject()'''
        return QObject()
    def toVariant(self):
        '''QVariant QScriptValue.toVariant()'''
        return QVariant()
    def toUInt16(self):
        '''int QScriptValue.toUInt16()'''
        return int()
    def toUInt32(self):
        '''int QScriptValue.toUInt32()'''
        return int()
    def toInt32(self):
        '''int QScriptValue.toInt32()'''
        return int()
    def toInteger(self):
        '''float QScriptValue.toInteger()'''
        return float()
    def toBoolean(self):
        '''bool QScriptValue.toBoolean()'''
        return bool()
    def toBool(self):
        '''bool QScriptValue.toBool()'''
        return bool()
    def toNumber(self):
        '''float QScriptValue.toNumber()'''
        return float()
    def toString(self):
        '''QString QScriptValue.toString()'''
        return QString()
    def isError(self):
        '''bool QScriptValue.isError()'''
        return bool()
    def isArray(self):
        '''bool QScriptValue.isArray()'''
        return bool()
    def isRegExp(self):
        '''bool QScriptValue.isRegExp()'''
        return bool()
    def isDate(self):
        '''bool QScriptValue.isDate()'''
        return bool()
    def isObject(self):
        '''bool QScriptValue.isObject()'''
        return bool()
    def isQMetaObject(self):
        '''bool QScriptValue.isQMetaObject()'''
        return bool()
    def isQObject(self):
        '''bool QScriptValue.isQObject()'''
        return bool()
    def isVariant(self):
        '''bool QScriptValue.isVariant()'''
        return bool()
    def isUndefined(self):
        '''bool QScriptValue.isUndefined()'''
        return bool()
    def isString(self):
        '''bool QScriptValue.isString()'''
        return bool()
    def isNull(self):
        '''bool QScriptValue.isNull()'''
        return bool()
    def isFunction(self):
        '''bool QScriptValue.isFunction()'''
        return bool()
    def isNumber(self):
        '''bool QScriptValue.isNumber()'''
        return bool()
    def isBoolean(self):
        '''bool QScriptValue.isBoolean()'''
        return bool()
    def isBool(self):
        '''bool QScriptValue.isBool()'''
        return bool()
    def isValid(self):
        '''bool QScriptValue.isValid()'''
        return bool()
    def engine(self):
        '''QScriptEngine QScriptValue.engine()'''
        return QScriptEngine()
    class ResolveFlags():
        """"""
        def __init__(self):
            '''QScriptValue.ResolveFlags QScriptValue.ResolveFlags.__init__()'''
            return QScriptValue.ResolveFlags()
        def __init__(self):
            '''int QScriptValue.ResolveFlags.__init__()'''
            return int()
        def __init__(self):
            '''void QScriptValue.ResolveFlags.__init__()'''
        def __bool__(self):
            '''int QScriptValue.ResolveFlags.__bool__()'''
            return int()
        def __ne__(self, f):
            '''bool QScriptValue.ResolveFlags.__ne__(QScriptValue.ResolveFlags f)'''
            return bool()
        def __eq__(self, f):
            '''bool QScriptValue.ResolveFlags.__eq__(QScriptValue.ResolveFlags f)'''
            return bool()
        def __invert__(self):
            '''QScriptValue.ResolveFlags QScriptValue.ResolveFlags.__invert__()'''
            return QScriptValue.ResolveFlags()
        def __and__(self, mask):
            '''QScriptValue.ResolveFlags QScriptValue.ResolveFlags.__and__(int mask)'''
            return QScriptValue.ResolveFlags()
        def __xor__(self, f):
            '''QScriptValue.ResolveFlags QScriptValue.ResolveFlags.__xor__(QScriptValue.ResolveFlags f)'''
            return QScriptValue.ResolveFlags()
        def __xor__(self, f):
            '''QScriptValue.ResolveFlags QScriptValue.ResolveFlags.__xor__(int f)'''
            return QScriptValue.ResolveFlags()
        def __or__(self, f):
            '''QScriptValue.ResolveFlags QScriptValue.ResolveFlags.__or__(QScriptValue.ResolveFlags f)'''
            return QScriptValue.ResolveFlags()
        def __or__(self, f):
            '''QScriptValue.ResolveFlags QScriptValue.ResolveFlags.__or__(int f)'''
            return QScriptValue.ResolveFlags()
        def __int__(self):
            '''int QScriptValue.ResolveFlags.__int__()'''
            return int()
        def __ixor__(self, f):
            '''QScriptValue.ResolveFlags QScriptValue.ResolveFlags.__ixor__(QScriptValue.ResolveFlags f)'''
            return QScriptValue.ResolveFlags()
        def __ior__(self, f):
            '''QScriptValue.ResolveFlags QScriptValue.ResolveFlags.__ior__(QScriptValue.ResolveFlags f)'''
            return QScriptValue.ResolveFlags()
        def __iand__(self, mask):
            '''QScriptValue.ResolveFlags QScriptValue.ResolveFlags.__iand__(int mask)'''
            return QScriptValue.ResolveFlags()
    class PropertyFlags():
        """"""
        def __init__(self):
            '''QScriptValue.PropertyFlags QScriptValue.PropertyFlags.__init__()'''
            return QScriptValue.PropertyFlags()
        def __init__(self):
            '''int QScriptValue.PropertyFlags.__init__()'''
            return int()
        def __init__(self):
            '''void QScriptValue.PropertyFlags.__init__()'''
        def __bool__(self):
            '''int QScriptValue.PropertyFlags.__bool__()'''
            return int()
        def __ne__(self, f):
            '''bool QScriptValue.PropertyFlags.__ne__(QScriptValue.PropertyFlags f)'''
            return bool()
        def __eq__(self, f):
            '''bool QScriptValue.PropertyFlags.__eq__(QScriptValue.PropertyFlags f)'''
            return bool()
        def __invert__(self):
            '''QScriptValue.PropertyFlags QScriptValue.PropertyFlags.__invert__()'''
            return QScriptValue.PropertyFlags()
        def __and__(self, mask):
            '''QScriptValue.PropertyFlags QScriptValue.PropertyFlags.__and__(int mask)'''
            return QScriptValue.PropertyFlags()
        def __xor__(self, f):
            '''QScriptValue.PropertyFlags QScriptValue.PropertyFlags.__xor__(QScriptValue.PropertyFlags f)'''
            return QScriptValue.PropertyFlags()
        def __xor__(self, f):
            '''QScriptValue.PropertyFlags QScriptValue.PropertyFlags.__xor__(int f)'''
            return QScriptValue.PropertyFlags()
        def __or__(self, f):
            '''QScriptValue.PropertyFlags QScriptValue.PropertyFlags.__or__(QScriptValue.PropertyFlags f)'''
            return QScriptValue.PropertyFlags()
        def __or__(self, f):
            '''QScriptValue.PropertyFlags QScriptValue.PropertyFlags.__or__(int f)'''
            return QScriptValue.PropertyFlags()
        def __int__(self):
            '''int QScriptValue.PropertyFlags.__int__()'''
            return int()
        def __ixor__(self, f):
            '''QScriptValue.PropertyFlags QScriptValue.PropertyFlags.__ixor__(QScriptValue.PropertyFlags f)'''
            return QScriptValue.PropertyFlags()
        def __ior__(self, f):
            '''QScriptValue.PropertyFlags QScriptValue.PropertyFlags.__ior__(QScriptValue.PropertyFlags f)'''
            return QScriptValue.PropertyFlags()
        def __iand__(self, mask):
            '''QScriptValue.PropertyFlags QScriptValue.PropertyFlags.__iand__(int mask)'''
            return QScriptValue.PropertyFlags()


class QScriptValueIterator():
    """"""
    def __init__(self, value):
        '''void QScriptValueIterator.__init__(QScriptValue value)'''
    def scriptName(self):
        '''QScriptString QScriptValueIterator.scriptName()'''
        return QScriptString()
    def toBack(self):
        '''void QScriptValueIterator.toBack()'''
    def toFront(self):
        '''void QScriptValueIterator.toFront()'''
    def remove(self):
        '''void QScriptValueIterator.remove()'''
    def flags(self):
        '''QScriptValue.PropertyFlags QScriptValueIterator.flags()'''
        return QScriptValue.PropertyFlags()
    def setValue(self, value):
        '''void QScriptValueIterator.setValue(QScriptValue value)'''
    def value(self):
        '''QScriptValue QScriptValueIterator.value()'''
        return QScriptValue()
    def name(self):
        '''QString QScriptValueIterator.name()'''
        return QString()
    def previous(self):
        '''void QScriptValueIterator.previous()'''
    def hasPrevious(self):
        '''bool QScriptValueIterator.hasPrevious()'''
        return bool()
    def next(self):
        '''void QScriptValueIterator.next()'''
    def hasNext(self):
        '''bool QScriptValueIterator.hasNext()'''
        return bool()


class QString():
    """"""
    def __init__(self):
        '''QScriptString QString.__init__()'''
        return QScriptString()


def qScriptDisconnect(sender, signal, receiver, function):
    '''static bool qScriptDisconnect(QObject sender, SIGNAL() signal, QScriptValue receiver, QScriptValue function)'''
    return bool()

def qScriptConnect(sender, signal, receiver, function):
    '''static bool qScriptConnect(QObject sender, SIGNAL() signal, QScriptValue receiver, QScriptValue function)'''
    return bool()

