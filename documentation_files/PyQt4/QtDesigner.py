class pyqtSignal():
 def connect(self, targetSignal): pass
 def emit(self, *args): pass
from QtCore import *

class QDesignerActionEditorInterface(QWidget):
    """"""
    def __init__(self, parent, flags = 0):
        '''void QDesignerActionEditorInterface.__init__(QWidget parent, Qt.WindowFlags flags = 0)'''
    def setFormWindow(self, formWindow):
        '''abstract void QDesignerActionEditorInterface.setFormWindow(QDesignerFormWindowInterface formWindow)'''
    def unmanageAction(self, action):
        '''abstract void QDesignerActionEditorInterface.unmanageAction(QAction action)'''
    def manageAction(self, action):
        '''abstract void QDesignerActionEditorInterface.manageAction(QAction action)'''
    def core(self):
        '''QDesignerFormEditorInterface QDesignerActionEditorInterface.core()'''
        return QDesignerFormEditorInterface()


class QAbstractFormBuilder():
    """"""
    def __init__(self):
        '''void QAbstractFormBuilder.__init__()'''
    def workingDirectory(self):
        '''QDir QAbstractFormBuilder.workingDirectory()'''
        return QDir()
    def setWorkingDirectory(self, directory):
        '''void QAbstractFormBuilder.setWorkingDirectory(QDir directory)'''
    def save(self, dev, widget):
        '''void QAbstractFormBuilder.save(QIODevice dev, QWidget widget)'''
    def load(self, device, parent = None):
        '''QWidget QAbstractFormBuilder.load(QIODevice device, QWidget parent = None)'''
        return QWidget()


class QDesignerFormEditorInterface(QObject):
    """"""
    def __init__(self, parent = None):
        '''void QDesignerFormEditorInterface.__init__(QObject parent = None)'''
    def setActionEditor(self, actionEditor):
        '''void QDesignerFormEditorInterface.setActionEditor(QDesignerActionEditorInterface actionEditor)'''
    def setObjectInspector(self, objectInspector):
        '''void QDesignerFormEditorInterface.setObjectInspector(QDesignerObjectInspectorInterface objectInspector)'''
    def setPropertyEditor(self, propertyEditor):
        '''void QDesignerFormEditorInterface.setPropertyEditor(QDesignerPropertyEditorInterface propertyEditor)'''
    def setWidgetBox(self, widgetBox):
        '''void QDesignerFormEditorInterface.setWidgetBox(QDesignerWidgetBoxInterface widgetBox)'''
    def actionEditor(self):
        '''QDesignerActionEditorInterface QDesignerFormEditorInterface.actionEditor()'''
        return QDesignerActionEditorInterface()
    def formWindowManager(self):
        '''QDesignerFormWindowManagerInterface QDesignerFormEditorInterface.formWindowManager()'''
        return QDesignerFormWindowManagerInterface()
    def objectInspector(self):
        '''QDesignerObjectInspectorInterface QDesignerFormEditorInterface.objectInspector()'''
        return QDesignerObjectInspectorInterface()
    def propertyEditor(self):
        '''QDesignerPropertyEditorInterface QDesignerFormEditorInterface.propertyEditor()'''
        return QDesignerPropertyEditorInterface()
    def widgetBox(self):
        '''QDesignerWidgetBoxInterface QDesignerFormEditorInterface.widgetBox()'''
        return QDesignerWidgetBoxInterface()
    def topLevel(self):
        '''QWidget QDesignerFormEditorInterface.topLevel()'''
        return QWidget()
    def extensionManager(self):
        '''QExtensionManager QDesignerFormEditorInterface.extensionManager()'''
        return QExtensionManager()


class QDesignerFormWindowInterface(QWidget):
    """"""
    # Enum QDesignerFormWindowInterface.FeatureFlag
    EditFeature = 0
    GridFeature = 0
    TabOrderFeature = 0
    DefaultFeature = 0

    def __init__(self, parent = None, flags = 0):
        '''void QDesignerFormWindowInterface.__init__(QWidget parent = None, Qt.WindowFlags flags = 0)'''
    objectRemoved = pyqtSignal() # void objectRemoved(QObject *) - signal
    widgetRemoved = pyqtSignal() # void widgetRemoved(QWidget *) - signal
    changed = pyqtSignal() # void changed() - signal
    activated = pyqtSignal() # void activated(QWidget *) - signal
    aboutToUnmanageWidget = pyqtSignal() # void aboutToUnmanageWidget(QWidget *) - signal
    widgetUnmanaged = pyqtSignal() # void widgetUnmanaged(QWidget *) - signal
    widgetManaged = pyqtSignal() # void widgetManaged(QWidget *) - signal
    resourceFilesChanged = pyqtSignal() # void resourceFilesChanged() - signal
    geometryChanged = pyqtSignal() # void geometryChanged() - signal
    selectionChanged = pyqtSignal() # void selectionChanged() - signal
    featureChanged = pyqtSignal() # void featureChanged(QDesignerFormWindowInterface::Feature) - signal
    fileNameChanged = pyqtSignal() # void fileNameChanged(const QStringamp;) - signal
    mainContainerChanged = pyqtSignal() # void mainContainerChanged(QWidget *) - signal
    def setFileName(self, fileName):
        '''abstract void QDesignerFormWindowInterface.setFileName(QString fileName)'''
    def setGrid(self, grid):
        '''abstract void QDesignerFormWindowInterface.setGrid(QPoint grid)'''
    def selectWidget(self, widget, select = True):
        '''abstract void QDesignerFormWindowInterface.selectWidget(QWidget widget, bool select = True)'''
    def clearSelection(self, update = True):
        '''abstract void QDesignerFormWindowInterface.clearSelection(bool update = True)'''
    def setDirty(self, dirty):
        '''abstract void QDesignerFormWindowInterface.setDirty(bool dirty)'''
    def setFeatures(self, f):
        '''abstract void QDesignerFormWindowInterface.setFeatures(QDesignerFormWindowInterface.Feature f)'''
    def unmanageWidget(self, widget):
        '''abstract void QDesignerFormWindowInterface.unmanageWidget(QWidget widget)'''
    def manageWidget(self, widget):
        '''abstract void QDesignerFormWindowInterface.manageWidget(QWidget widget)'''
    def removeResourceFile(self, path):
        '''abstract void QDesignerFormWindowInterface.removeResourceFile(QString path)'''
    def addResourceFile(self, path):
        '''abstract void QDesignerFormWindowInterface.addResourceFile(QString path)'''
    def resourceFiles(self):
        '''abstract QStringList QDesignerFormWindowInterface.resourceFiles()'''
        return QStringList()
    def emitSelectionChanged(self):
        '''abstract void QDesignerFormWindowInterface.emitSelectionChanged()'''
    def findFormWindow(self, w):
        '''static QDesignerFormWindowInterface QDesignerFormWindowInterface.findFormWindow(QWidget w)'''
        return QDesignerFormWindowInterface()
    def findFormWindow(self, obj):
        '''static QDesignerFormWindowInterface QDesignerFormWindowInterface.findFormWindow(QObject obj)'''
        return QDesignerFormWindowInterface()
    def isDirty(self):
        '''abstract bool QDesignerFormWindowInterface.isDirty()'''
        return bool()
    def isManaged(self, widget):
        '''abstract bool QDesignerFormWindowInterface.isManaged(QWidget widget)'''
        return bool()
    def setMainContainer(self, mainContainer):
        '''abstract void QDesignerFormWindowInterface.setMainContainer(QWidget mainContainer)'''
    def mainContainer(self):
        '''abstract QWidget QDesignerFormWindowInterface.mainContainer()'''
        return QWidget()
    def grid(self):
        '''abstract QPoint QDesignerFormWindowInterface.grid()'''
        return QPoint()
    def cursor(self):
        '''abstract QDesignerFormWindowCursorInterface QDesignerFormWindowInterface.cursor()'''
        return QDesignerFormWindowCursorInterface()
    def core(self):
        '''QDesignerFormEditorInterface QDesignerFormWindowInterface.core()'''
        return QDesignerFormEditorInterface()
    def setIncludeHints(self, includeHints):
        '''abstract void QDesignerFormWindowInterface.setIncludeHints(QStringList includeHints)'''
    def includeHints(self):
        '''abstract QStringList QDesignerFormWindowInterface.includeHints()'''
        return QStringList()
    def setExportMacro(self, exportMacro):
        '''abstract void QDesignerFormWindowInterface.setExportMacro(QString exportMacro)'''
    def exportMacro(self):
        '''abstract QString QDesignerFormWindowInterface.exportMacro()'''
        return QString()
    def setPixmapFunction(self, pixmapFunction):
        '''abstract void QDesignerFormWindowInterface.setPixmapFunction(QString pixmapFunction)'''
    def pixmapFunction(self):
        '''abstract QString QDesignerFormWindowInterface.pixmapFunction()'''
        return QString()
    def setLayoutFunction(self, margin, spacing):
        '''abstract void QDesignerFormWindowInterface.setLayoutFunction(QString margin, QString spacing)'''
    def layoutFunction(self, margin, spacing):
        '''abstract void QDesignerFormWindowInterface.layoutFunction(QString margin, QString spacing)'''
    def setLayoutDefault(self, margin, spacing):
        '''abstract void QDesignerFormWindowInterface.setLayoutDefault(int margin, int spacing)'''
    def layoutDefault(self, margin, spacing):
        '''abstract void QDesignerFormWindowInterface.layoutDefault(int margin, int spacing)'''
    def setComment(self, comment):
        '''abstract void QDesignerFormWindowInterface.setComment(QString comment)'''
    def comment(self):
        '''abstract QString QDesignerFormWindowInterface.comment()'''
        return QString()
    def setAuthor(self, author):
        '''abstract void QDesignerFormWindowInterface.setAuthor(QString author)'''
    def author(self):
        '''abstract QString QDesignerFormWindowInterface.author()'''
        return QString()
    def hasFeature(self, f):
        '''abstract bool QDesignerFormWindowInterface.hasFeature(QDesignerFormWindowInterface.Feature f)'''
        return bool()
    def features(self):
        '''abstract QDesignerFormWindowInterface.Feature QDesignerFormWindowInterface.features()'''
        return QDesignerFormWindowInterface.Feature()
    def setContents(self, dev):
        '''abstract void QDesignerFormWindowInterface.setContents(QIODevice dev)'''
    def setContents(self, contents):
        '''abstract void QDesignerFormWindowInterface.setContents(QString contents)'''
    def contents(self):
        '''abstract QString QDesignerFormWindowInterface.contents()'''
        return QString()
    def absoluteDir(self):
        '''abstract QDir QDesignerFormWindowInterface.absoluteDir()'''
        return QDir()
    def fileName(self):
        '''abstract QString QDesignerFormWindowInterface.fileName()'''
        return QString()
    class Feature():
        """"""
        def __init__(self):
            '''QDesignerFormWindowInterface.Feature QDesignerFormWindowInterface.Feature.__init__()'''
            return QDesignerFormWindowInterface.Feature()
        def __init__(self):
            '''int QDesignerFormWindowInterface.Feature.__init__()'''
            return int()
        def __init__(self):
            '''void QDesignerFormWindowInterface.Feature.__init__()'''
        def __bool__(self):
            '''int QDesignerFormWindowInterface.Feature.__bool__()'''
            return int()
        def __ne__(self, f):
            '''bool QDesignerFormWindowInterface.Feature.__ne__(QDesignerFormWindowInterface.Feature f)'''
            return bool()
        def __eq__(self, f):
            '''bool QDesignerFormWindowInterface.Feature.__eq__(QDesignerFormWindowInterface.Feature f)'''
            return bool()
        def __invert__(self):
            '''QDesignerFormWindowInterface.Feature QDesignerFormWindowInterface.Feature.__invert__()'''
            return QDesignerFormWindowInterface.Feature()
        def __and__(self, mask):
            '''QDesignerFormWindowInterface.Feature QDesignerFormWindowInterface.Feature.__and__(int mask)'''
            return QDesignerFormWindowInterface.Feature()
        def __xor__(self, f):
            '''QDesignerFormWindowInterface.Feature QDesignerFormWindowInterface.Feature.__xor__(QDesignerFormWindowInterface.Feature f)'''
            return QDesignerFormWindowInterface.Feature()
        def __xor__(self, f):
            '''QDesignerFormWindowInterface.Feature QDesignerFormWindowInterface.Feature.__xor__(int f)'''
            return QDesignerFormWindowInterface.Feature()
        def __or__(self, f):
            '''QDesignerFormWindowInterface.Feature QDesignerFormWindowInterface.Feature.__or__(QDesignerFormWindowInterface.Feature f)'''
            return QDesignerFormWindowInterface.Feature()
        def __or__(self, f):
            '''QDesignerFormWindowInterface.Feature QDesignerFormWindowInterface.Feature.__or__(int f)'''
            return QDesignerFormWindowInterface.Feature()
        def __int__(self):
            '''int QDesignerFormWindowInterface.Feature.__int__()'''
            return int()
        def __ixor__(self, f):
            '''QDesignerFormWindowInterface.Feature QDesignerFormWindowInterface.Feature.__ixor__(QDesignerFormWindowInterface.Feature f)'''
            return QDesignerFormWindowInterface.Feature()
        def __ior__(self, f):
            '''QDesignerFormWindowInterface.Feature QDesignerFormWindowInterface.Feature.__ior__(QDesignerFormWindowInterface.Feature f)'''
            return QDesignerFormWindowInterface.Feature()
        def __iand__(self, mask):
            '''QDesignerFormWindowInterface.Feature QDesignerFormWindowInterface.Feature.__iand__(int mask)'''
            return QDesignerFormWindowInterface.Feature()


class QDesignerFormWindowCursorInterface():
    """"""
    # Enum QDesignerFormWindowCursorInterface.MoveMode
    MoveAnchor = 0
    KeepAnchor = 0

    # Enum QDesignerFormWindowCursorInterface.MoveOperation
    NoMove = 0
    Start = 0
    End = 0
    Next = 0
    Prev = 0
    Left = 0
    Right = 0
    Up = 0
    Down = 0

    def __init__(self):
        '''void QDesignerFormWindowCursorInterface.__init__()'''
    def __init__(self):
        '''QDesignerFormWindowCursorInterface QDesignerFormWindowCursorInterface.__init__()'''
        return QDesignerFormWindowCursorInterface()
    def isWidgetSelected(self, widget):
        '''bool QDesignerFormWindowCursorInterface.isWidgetSelected(QWidget widget)'''
        return bool()
    def resetWidgetProperty(self, widget, name):
        '''abstract void QDesignerFormWindowCursorInterface.resetWidgetProperty(QWidget widget, QString name)'''
    def setWidgetProperty(self, widget, name, value):
        '''abstract void QDesignerFormWindowCursorInterface.setWidgetProperty(QWidget widget, QString name, QVariant value)'''
    def setProperty(self, name, value):
        '''abstract void QDesignerFormWindowCursorInterface.setProperty(QString name, QVariant value)'''
    def selectedWidget(self, index):
        '''abstract QWidget QDesignerFormWindowCursorInterface.selectedWidget(int index)'''
        return QWidget()
    def selectedWidgetCount(self):
        '''abstract int QDesignerFormWindowCursorInterface.selectedWidgetCount()'''
        return int()
    def hasSelection(self):
        '''abstract bool QDesignerFormWindowCursorInterface.hasSelection()'''
        return bool()
    def widget(self, index):
        '''abstract QWidget QDesignerFormWindowCursorInterface.widget(int index)'''
        return QWidget()
    def widgetCount(self):
        '''abstract int QDesignerFormWindowCursorInterface.widgetCount()'''
        return int()
    def current(self):
        '''abstract QWidget QDesignerFormWindowCursorInterface.current()'''
        return QWidget()
    def setPosition(self, pos, mode = None):
        '''abstract void QDesignerFormWindowCursorInterface.setPosition(int pos, QDesignerFormWindowCursorInterface.MoveMode mode = QDesignerFormWindowCursorInterface.MoveAnchor)'''
    def position(self):
        '''abstract int QDesignerFormWindowCursorInterface.position()'''
        return int()
    def movePosition(self, op, mode = None):
        '''abstract bool QDesignerFormWindowCursorInterface.movePosition(QDesignerFormWindowCursorInterface.MoveOperation op, QDesignerFormWindowCursorInterface.MoveMode mode = QDesignerFormWindowCursorInterface.MoveAnchor)'''
        return bool()
    def formWindow(self):
        '''abstract QDesignerFormWindowInterface QDesignerFormWindowCursorInterface.formWindow()'''
        return QDesignerFormWindowInterface()


class QDesignerFormWindowManagerInterface(QObject):
    """"""
    def __init__(self, parent = None):
        '''void QDesignerFormWindowManagerInterface.__init__(QObject parent = None)'''
    def setActiveFormWindow(self, formWindow):
        '''void QDesignerFormWindowManagerInterface.setActiveFormWindow(QDesignerFormWindowInterface formWindow)'''
    def removeFormWindow(self, formWindow):
        '''void QDesignerFormWindowManagerInterface.removeFormWindow(QDesignerFormWindowInterface formWindow)'''
    def addFormWindow(self, formWindow):
        '''void QDesignerFormWindowManagerInterface.addFormWindow(QDesignerFormWindowInterface formWindow)'''
    activeFormWindowChanged = pyqtSignal() # void activeFormWindowChanged(QDesignerFormWindowInterface *) - signal
    formWindowRemoved = pyqtSignal() # void formWindowRemoved(QDesignerFormWindowInterface *) - signal
    formWindowAdded = pyqtSignal() # void formWindowAdded(QDesignerFormWindowInterface *) - signal
    def core(self):
        '''QDesignerFormEditorInterface QDesignerFormWindowManagerInterface.core()'''
        return QDesignerFormEditorInterface()
    def createFormWindow(self, parent = None, flags = 0):
        '''QDesignerFormWindowInterface QDesignerFormWindowManagerInterface.createFormWindow(QWidget parent = None, Qt.WindowFlags flags = 0)'''
        return QDesignerFormWindowInterface()
    def formWindow(self, index):
        '''QDesignerFormWindowInterface QDesignerFormWindowManagerInterface.formWindow(int index)'''
        return QDesignerFormWindowInterface()
    def formWindowCount(self):
        '''int QDesignerFormWindowManagerInterface.formWindowCount()'''
        return int()
    def activeFormWindow(self):
        '''QDesignerFormWindowInterface QDesignerFormWindowManagerInterface.activeFormWindow()'''
        return QDesignerFormWindowInterface()
    def actionSimplifyLayout(self):
        '''QAction QDesignerFormWindowManagerInterface.actionSimplifyLayout()'''
        return QAction()
    def actionFormLayout(self):
        '''QAction QDesignerFormWindowManagerInterface.actionFormLayout()'''
        return QAction()
    def actionAdjustSize(self):
        '''QAction QDesignerFormWindowManagerInterface.actionAdjustSize()'''
        return QAction()
    def actionBreakLayout(self):
        '''QAction QDesignerFormWindowManagerInterface.actionBreakLayout()'''
        return QAction()
    def actionGridLayout(self):
        '''QAction QDesignerFormWindowManagerInterface.actionGridLayout()'''
        return QAction()
    def actionSplitVertical(self):
        '''QAction QDesignerFormWindowManagerInterface.actionSplitVertical()'''
        return QAction()
    def actionSplitHorizontal(self):
        '''QAction QDesignerFormWindowManagerInterface.actionSplitHorizontal()'''
        return QAction()
    def actionVerticalLayout(self):
        '''QAction QDesignerFormWindowManagerInterface.actionVerticalLayout()'''
        return QAction()
    def actionHorizontalLayout(self):
        '''QAction QDesignerFormWindowManagerInterface.actionHorizontalLayout()'''
        return QAction()
    def actionRedo(self):
        '''QAction QDesignerFormWindowManagerInterface.actionRedo()'''
        return QAction()
    def actionUndo(self):
        '''QAction QDesignerFormWindowManagerInterface.actionUndo()'''
        return QAction()
    def actionRaise(self):
        '''QAction QDesignerFormWindowManagerInterface.actionRaise()'''
        return QAction()
    def actionLower(self):
        '''QAction QDesignerFormWindowManagerInterface.actionLower()'''
        return QAction()
    def actionSelectAll(self):
        '''QAction QDesignerFormWindowManagerInterface.actionSelectAll()'''
        return QAction()
    def actionDelete(self):
        '''QAction QDesignerFormWindowManagerInterface.actionDelete()'''
        return QAction()
    def actionPaste(self):
        '''QAction QDesignerFormWindowManagerInterface.actionPaste()'''
        return QAction()
    def actionCopy(self):
        '''QAction QDesignerFormWindowManagerInterface.actionCopy()'''
        return QAction()
    def actionCut(self):
        '''QAction QDesignerFormWindowManagerInterface.actionCut()'''
        return QAction()


class QDesignerObjectInspectorInterface(QWidget):
    """"""
    def __init__(self, parent, flags = 0):
        '''void QDesignerObjectInspectorInterface.__init__(QWidget parent, Qt.WindowFlags flags = 0)'''
    def setFormWindow(self, formWindow):
        '''abstract void QDesignerObjectInspectorInterface.setFormWindow(QDesignerFormWindowInterface formWindow)'''
    def core(self):
        '''QDesignerFormEditorInterface QDesignerObjectInspectorInterface.core()'''
        return QDesignerFormEditorInterface()


class QDesignerPropertyEditorInterface(QWidget):
    """"""
    def __init__(self, parent, flags = 0):
        '''void QDesignerPropertyEditorInterface.__init__(QWidget parent, Qt.WindowFlags flags = 0)'''
    def setReadOnly(self, readOnly):
        '''abstract void QDesignerPropertyEditorInterface.setReadOnly(bool readOnly)'''
    def setPropertyValue(self, name, value, changed = True):
        '''abstract void QDesignerPropertyEditorInterface.setPropertyValue(QString name, QVariant value, bool changed = True)'''
    def setObject(self, object):
        '''abstract void QDesignerPropertyEditorInterface.setObject(QObject object)'''
    propertyChanged = pyqtSignal() # void propertyChanged(const QStringamp;,const QVariantamp;) - signal
    def currentPropertyName(self):
        '''abstract QString QDesignerPropertyEditorInterface.currentPropertyName()'''
        return QString()
    def object(self):
        '''abstract QObject QDesignerPropertyEditorInterface.object()'''
        return QObject()
    def isReadOnly(self):
        '''abstract bool QDesignerPropertyEditorInterface.isReadOnly()'''
        return bool()
    def core(self):
        '''QDesignerFormEditorInterface QDesignerPropertyEditorInterface.core()'''
        return QDesignerFormEditorInterface()


class QDesignerWidgetBoxInterface(QWidget):
    """"""
    def __init__(self, parent = None, flags = 0):
        '''void QDesignerWidgetBoxInterface.__init__(QWidget parent = None, Qt.WindowFlags flags = 0)'''
    def save(self):
        '''abstract bool QDesignerWidgetBoxInterface.save()'''
        return bool()
    def load(self):
        '''abstract bool QDesignerWidgetBoxInterface.load()'''
        return bool()
    def fileName(self):
        '''abstract QString QDesignerWidgetBoxInterface.fileName()'''
        return QString()
    def setFileName(self, file_name):
        '''abstract void QDesignerWidgetBoxInterface.setFileName(QString file_name)'''


class QDesignerContainerExtension():
    """"""
    def __init__(self):
        '''void QDesignerContainerExtension.__init__()'''
    def __init__(self):
        '''QDesignerContainerExtension QDesignerContainerExtension.__init__()'''
        return QDesignerContainerExtension()
    def remove(self, index):
        '''abstract void QDesignerContainerExtension.remove(int index)'''
    def insertWidget(self, index, widget):
        '''abstract void QDesignerContainerExtension.insertWidget(int index, QWidget widget)'''
    def addWidget(self, widget):
        '''abstract void QDesignerContainerExtension.addWidget(QWidget widget)'''
    def setCurrentIndex(self, index):
        '''abstract void QDesignerContainerExtension.setCurrentIndex(int index)'''
    def currentIndex(self):
        '''abstract int QDesignerContainerExtension.currentIndex()'''
        return int()
    def widget(self, index):
        '''abstract QWidget QDesignerContainerExtension.widget(int index)'''
        return QWidget()
    def __len__(self):
        '''None QDesignerContainerExtension.__len__()'''
        return None()
    def count(self):
        '''abstract int QDesignerContainerExtension.count()'''
        return int()


class QDesignerCustomWidgetInterface():
    """"""
    def __init__(self):
        '''void QDesignerCustomWidgetInterface.__init__()'''
    def __init__(self):
        '''QDesignerCustomWidgetInterface QDesignerCustomWidgetInterface.__init__()'''
        return QDesignerCustomWidgetInterface()
    def codeTemplate(self):
        '''QString QDesignerCustomWidgetInterface.codeTemplate()'''
        return QString()
    def domXml(self):
        '''QString QDesignerCustomWidgetInterface.domXml()'''
        return QString()
    def initialize(self, core):
        '''void QDesignerCustomWidgetInterface.initialize(QDesignerFormEditorInterface core)'''
    def isInitialized(self):
        '''bool QDesignerCustomWidgetInterface.isInitialized()'''
        return bool()
    def createWidget(self, parent):
        '''abstract QWidget QDesignerCustomWidgetInterface.createWidget(QWidget parent)'''
        return QWidget()
    def isContainer(self):
        '''abstract bool QDesignerCustomWidgetInterface.isContainer()'''
        return bool()
    def icon(self):
        '''abstract QIcon QDesignerCustomWidgetInterface.icon()'''
        return QIcon()
    def includeFile(self):
        '''abstract QString QDesignerCustomWidgetInterface.includeFile()'''
        return QString()
    def whatsThis(self):
        '''abstract QString QDesignerCustomWidgetInterface.whatsThis()'''
        return QString()
    def toolTip(self):
        '''abstract QString QDesignerCustomWidgetInterface.toolTip()'''
        return QString()
    def group(self):
        '''abstract QString QDesignerCustomWidgetInterface.group()'''
        return QString()
    def name(self):
        '''abstract QString QDesignerCustomWidgetInterface.name()'''
        return QString()


class QDesignerCustomWidgetCollectionInterface():
    """"""
    def __init__(self):
        '''void QDesignerCustomWidgetCollectionInterface.__init__()'''
    def __init__(self):
        '''QDesignerCustomWidgetCollectionInterface QDesignerCustomWidgetCollectionInterface.__init__()'''
        return QDesignerCustomWidgetCollectionInterface()
    def customWidgets(self):
        '''abstract list-of-QDesignerCustomWidgetInterface QDesignerCustomWidgetCollectionInterface.customWidgets()'''
        return [QDesignerCustomWidgetInterface()]


class QAbstractExtensionFactory():
    """"""
    def __init__(self):
        '''void QAbstractExtensionFactory.__init__()'''
    def __init__(self):
        '''QAbstractExtensionFactory QAbstractExtensionFactory.__init__()'''
        return QAbstractExtensionFactory()
    def extension(self, object, iid):
        '''abstract QObject QAbstractExtensionFactory.extension(QObject object, QString iid)'''
        return QObject()


class QExtensionFactory(QObject, QAbstractExtensionFactory):
    """"""
    def __init__(self, parent = None):
        '''void QExtensionFactory.__init__(QExtensionManager parent = None)'''
    def createExtension(self, object, iid, parent):
        '''QObject QExtensionFactory.createExtension(QObject object, QString iid, QObject parent)'''
        return QObject()
    def extensionManager(self):
        '''QExtensionManager QExtensionFactory.extensionManager()'''
        return QExtensionManager()
    def extension(self, object, iid):
        '''QObject QExtensionFactory.extension(QObject object, QString iid)'''
        return QObject()


class QAbstractExtensionManager():
    """"""
    def __init__(self):
        '''void QAbstractExtensionManager.__init__()'''
    def __init__(self):
        '''QAbstractExtensionManager QAbstractExtensionManager.__init__()'''
        return QAbstractExtensionManager()
    def extension(self, object, iid):
        '''abstract QObject QAbstractExtensionManager.extension(QObject object, QString iid)'''
        return QObject()
    def unregisterExtensions(self, factory, iid):
        '''abstract void QAbstractExtensionManager.unregisterExtensions(QAbstractExtensionFactory factory, QString iid)'''
    def registerExtensions(self, factory, iid):
        '''abstract void QAbstractExtensionManager.registerExtensions(QAbstractExtensionFactory factory, QString iid)'''


class QFormBuilder(QAbstractFormBuilder):
    """"""
    def __init__(self):
        '''void QFormBuilder.__init__()'''
    def customWidgets(self):
        '''list-of-QDesignerCustomWidgetInterface QFormBuilder.customWidgets()'''
        return [QDesignerCustomWidgetInterface()]
    def setPluginPath(self, pluginPaths):
        '''void QFormBuilder.setPluginPath(QStringList pluginPaths)'''
    def addPluginPath(self, pluginPath):
        '''void QFormBuilder.addPluginPath(QString pluginPath)'''
    def clearPluginPaths(self):
        '''void QFormBuilder.clearPluginPaths()'''
    def pluginPaths(self):
        '''QStringList QFormBuilder.pluginPaths()'''
        return QStringList()


class QDesignerMemberSheetExtension():
    """"""
    def __init__(self):
        '''void QDesignerMemberSheetExtension.__init__()'''
    def __init__(self):
        '''QDesignerMemberSheetExtension QDesignerMemberSheetExtension.__init__()'''
        return QDesignerMemberSheetExtension()
    def parameterNames(self, index):
        '''abstract list-of-QByteArray QDesignerMemberSheetExtension.parameterNames(int index)'''
        return [QByteArray()]
    def parameterTypes(self, index):
        '''abstract list-of-QByteArray QDesignerMemberSheetExtension.parameterTypes(int index)'''
        return [QByteArray()]
    def signature(self, index):
        '''abstract QString QDesignerMemberSheetExtension.signature(int index)'''
        return QString()
    def declaredInClass(self, index):
        '''abstract QString QDesignerMemberSheetExtension.declaredInClass(int index)'''
        return QString()
    def inheritedFromWidget(self, index):
        '''abstract bool QDesignerMemberSheetExtension.inheritedFromWidget(int index)'''
        return bool()
    def isSlot(self, index):
        '''abstract bool QDesignerMemberSheetExtension.isSlot(int index)'''
        return bool()
    def isSignal(self, index):
        '''abstract bool QDesignerMemberSheetExtension.isSignal(int index)'''
        return bool()
    def setVisible(self, index, b):
        '''abstract void QDesignerMemberSheetExtension.setVisible(int index, bool b)'''
    def isVisible(self, index):
        '''abstract bool QDesignerMemberSheetExtension.isVisible(int index)'''
        return bool()
    def setMemberGroup(self, index, group):
        '''abstract void QDesignerMemberSheetExtension.setMemberGroup(int index, QString group)'''
    def memberGroup(self, index):
        '''abstract QString QDesignerMemberSheetExtension.memberGroup(int index)'''
        return QString()
    def memberName(self, index):
        '''abstract QString QDesignerMemberSheetExtension.memberName(int index)'''
        return QString()
    def indexOf(self, name):
        '''abstract int QDesignerMemberSheetExtension.indexOf(QString name)'''
        return int()
    def __len__(self):
        '''None QDesignerMemberSheetExtension.__len__()'''
        return None()
    def count(self):
        '''abstract int QDesignerMemberSheetExtension.count()'''
        return int()


class QDesignerPropertySheetExtension():
    """"""
    def __init__(self):
        '''void QDesignerPropertySheetExtension.__init__()'''
    def __init__(self):
        '''QDesignerPropertySheetExtension QDesignerPropertySheetExtension.__init__()'''
        return QDesignerPropertySheetExtension()
    def setChanged(self, index, changed):
        '''abstract void QDesignerPropertySheetExtension.setChanged(int index, bool changed)'''
    def isChanged(self, index):
        '''abstract bool QDesignerPropertySheetExtension.isChanged(int index)'''
        return bool()
    def setProperty(self, index, value):
        '''abstract void QDesignerPropertySheetExtension.setProperty(int index, QVariant value)'''
    def property(self, index):
        '''abstract QVariant QDesignerPropertySheetExtension.property(int index)'''
        return QVariant()
    def setAttribute(self, index, b):
        '''abstract void QDesignerPropertySheetExtension.setAttribute(int index, bool b)'''
    def isAttribute(self, index):
        '''abstract bool QDesignerPropertySheetExtension.isAttribute(int index)'''
        return bool()
    def setVisible(self, index, b):
        '''abstract void QDesignerPropertySheetExtension.setVisible(int index, bool b)'''
    def isVisible(self, index):
        '''abstract bool QDesignerPropertySheetExtension.isVisible(int index)'''
        return bool()
    def reset(self, index):
        '''abstract bool QDesignerPropertySheetExtension.reset(int index)'''
        return bool()
    def hasReset(self, index):
        '''abstract bool QDesignerPropertySheetExtension.hasReset(int index)'''
        return bool()
    def setPropertyGroup(self, index, group):
        '''abstract void QDesignerPropertySheetExtension.setPropertyGroup(int index, QString group)'''
    def propertyGroup(self, index):
        '''abstract QString QDesignerPropertySheetExtension.propertyGroup(int index)'''
        return QString()
    def propertyName(self, index):
        '''abstract QString QDesignerPropertySheetExtension.propertyName(int index)'''
        return QString()
    def indexOf(self, name):
        '''abstract int QDesignerPropertySheetExtension.indexOf(QString name)'''
        return int()
    def __len__(self):
        '''None QDesignerPropertySheetExtension.__len__()'''
        return None()
    def count(self):
        '''abstract int QDesignerPropertySheetExtension.count()'''
        return int()


class QExtensionManager(QObject, QAbstractExtensionManager):
    """"""
    def __init__(self, parent = None):
        '''void QExtensionManager.__init__(QObject parent = None)'''
    def extension(self, object, iid):
        '''QObject QExtensionManager.extension(QObject object, QString iid)'''
        return QObject()
    def unregisterExtensions(self, factory, iid = QString()):
        '''void QExtensionManager.unregisterExtensions(QAbstractExtensionFactory factory, QString iid = QString())'''
    def registerExtensions(self, factory, iid = QString()):
        '''void QExtensionManager.registerExtensions(QAbstractExtensionFactory factory, QString iid = QString())'''


class QDesignerTaskMenuExtension():
    """"""
    def __init__(self):
        '''void QDesignerTaskMenuExtension.__init__()'''
    def __init__(self):
        '''QDesignerTaskMenuExtension QDesignerTaskMenuExtension.__init__()'''
        return QDesignerTaskMenuExtension()
    def preferredEditAction(self):
        '''QAction QDesignerTaskMenuExtension.preferredEditAction()'''
        return QAction()
    def taskActions(self):
        '''abstract list-of-QAction QDesignerTaskMenuExtension.taskActions()'''
        return [QAction()]


class QPyDesignerContainerExtension(QObject, QDesignerContainerExtension):
    """"""
    def __init__(self, parent):
        '''void QPyDesignerContainerExtension.__init__(QObject parent)'''


class QPyDesignerCustomWidgetCollectionPlugin(QObject, QDesignerCustomWidgetCollectionInterface):
    """"""
    def __init__(self, parent = None):
        '''void QPyDesignerCustomWidgetCollectionPlugin.__init__(QObject parent = None)'''


class QPyDesignerCustomWidgetPlugin(QObject, QDesignerCustomWidgetInterface):
    """"""
    def __init__(self, parent = None):
        '''void QPyDesignerCustomWidgetPlugin.__init__(QObject parent = None)'''


class QPyDesignerMemberSheetExtension(QObject, QDesignerMemberSheetExtension):
    """"""
    def __init__(self, parent):
        '''void QPyDesignerMemberSheetExtension.__init__(QObject parent)'''


class QPyDesignerPropertySheetExtension(QObject, QDesignerPropertySheetExtension):
    """"""
    def __init__(self, parent):
        '''void QPyDesignerPropertySheetExtension.__init__(QObject parent)'''


class QPyDesignerTaskMenuExtension(QObject, QDesignerTaskMenuExtension):
    """"""
    def __init__(self, parent):
        '''void QPyDesignerTaskMenuExtension.__init__(QObject parent)'''


