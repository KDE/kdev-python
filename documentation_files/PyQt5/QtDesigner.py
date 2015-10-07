class pyqtSignal():
 def connect(self, targetSignal): pass
 def emit(self, *args): pass
from QtCore import *

from QtWidgets import *

import datetime

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
    def errorString(self):
        '''str QAbstractFormBuilder.errorString()'''
        return str()
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
    def activateResourceFilePaths(self, paths, errorCount, errorMessages):
        '''void QDesignerFormWindowInterface.activateResourceFilePaths(list-of-str paths, int errorCount, str errorMessages)'''
    def formContainer(self):
        '''abstract QWidget QDesignerFormWindowInterface.formContainer()'''
        return QWidget()
    def activeResourceFilePaths(self):
        '''list-of-str QDesignerFormWindowInterface.activeResourceFilePaths()'''
        return [str()]
    def checkContents(self):
        '''abstract list-of-str QDesignerFormWindowInterface.checkContents()'''
        return [str()]
    objectRemoved = pyqtSignal() # void objectRemoved(QObject*) - signal
    widgetRemoved = pyqtSignal() # void widgetRemoved(QWidget*) - signal
    changed = pyqtSignal() # void changed() - signal
    activated = pyqtSignal() # void activated(QWidget*) - signal
    aboutToUnmanageWidget = pyqtSignal() # void aboutToUnmanageWidget(QWidget*) - signal
    widgetUnmanaged = pyqtSignal() # void widgetUnmanaged(QWidget*) - signal
    widgetManaged = pyqtSignal() # void widgetManaged(QWidget*) - signal
    resourceFilesChanged = pyqtSignal() # void resourceFilesChanged() - signal
    geometryChanged = pyqtSignal() # void geometryChanged() - signal
    selectionChanged = pyqtSignal() # void selectionChanged() - signal
    featureChanged = pyqtSignal() # void featureChanged(QDesignerFormWindowInterface::Feature) - signal
    fileNameChanged = pyqtSignal() # void fileNameChanged(const QStringamp;) - signal
    mainContainerChanged = pyqtSignal() # void mainContainerChanged(QWidget*) - signal
    def setFileName(self, fileName):
        '''abstract void QDesignerFormWindowInterface.setFileName(str fileName)'''
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
        '''abstract void QDesignerFormWindowInterface.removeResourceFile(str path)'''
    def addResourceFile(self, path):
        '''abstract void QDesignerFormWindowInterface.addResourceFile(str path)'''
    def resourceFiles(self):
        '''abstract list-of-str QDesignerFormWindowInterface.resourceFiles()'''
        return [str()]
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
        '''abstract void QDesignerFormWindowInterface.setIncludeHints(list-of-str includeHints)'''
    def includeHints(self):
        '''abstract list-of-str QDesignerFormWindowInterface.includeHints()'''
        return [str()]
    def setExportMacro(self, exportMacro):
        '''abstract void QDesignerFormWindowInterface.setExportMacro(str exportMacro)'''
    def exportMacro(self):
        '''abstract str QDesignerFormWindowInterface.exportMacro()'''
        return str()
    def setPixmapFunction(self, pixmapFunction):
        '''abstract void QDesignerFormWindowInterface.setPixmapFunction(str pixmapFunction)'''
    def pixmapFunction(self):
        '''abstract str QDesignerFormWindowInterface.pixmapFunction()'''
        return str()
    def setLayoutFunction(self, margin, spacing):
        '''abstract void QDesignerFormWindowInterface.setLayoutFunction(str margin, str spacing)'''
    def layoutFunction(self, margin, spacing):
        '''abstract void QDesignerFormWindowInterface.layoutFunction(str margin, str spacing)'''
    def setLayoutDefault(self, margin, spacing):
        '''abstract void QDesignerFormWindowInterface.setLayoutDefault(int margin, int spacing)'''
    def layoutDefault(self, margin, spacing):
        '''abstract void QDesignerFormWindowInterface.layoutDefault(int margin, int spacing)'''
    def setComment(self, comment):
        '''abstract void QDesignerFormWindowInterface.setComment(str comment)'''
    def comment(self):
        '''abstract str QDesignerFormWindowInterface.comment()'''
        return str()
    def setAuthor(self, author):
        '''abstract void QDesignerFormWindowInterface.setAuthor(str author)'''
    def author(self):
        '''abstract str QDesignerFormWindowInterface.author()'''
        return str()
    def hasFeature(self, f):
        '''abstract bool QDesignerFormWindowInterface.hasFeature(QDesignerFormWindowInterface.Feature f)'''
        return bool()
    def features(self):
        '''abstract QDesignerFormWindowInterface.Feature QDesignerFormWindowInterface.features()'''
        return QDesignerFormWindowInterface.Feature()
    def setContents(self, dev, errorMessage = None):
        '''abstract bool QDesignerFormWindowInterface.setContents(QIODevice dev, str errorMessage = None)'''
        return bool()
    def setContents(self, contents):
        '''abstract bool QDesignerFormWindowInterface.setContents(str contents)'''
        return bool()
    def contents(self):
        '''abstract str QDesignerFormWindowInterface.contents()'''
        return str()
    def absoluteDir(self):
        '''abstract QDir QDesignerFormWindowInterface.absoluteDir()'''
        return QDir()
    def fileName(self):
        '''abstract str QDesignerFormWindowInterface.fileName()'''
        return str()
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
        '''abstract void QDesignerFormWindowCursorInterface.resetWidgetProperty(QWidget widget, str name)'''
    def setWidgetProperty(self, widget, name, value):
        '''abstract void QDesignerFormWindowCursorInterface.setWidgetProperty(QWidget widget, str name, QVariant value)'''
    def setProperty(self, name, value):
        '''abstract void QDesignerFormWindowCursorInterface.setProperty(str name, QVariant value)'''
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
    # Enum QDesignerFormWindowManagerInterface.ActionGroup
    StyledPreviewActionGroup = 0

    # Enum QDesignerFormWindowManagerInterface.Action
    CutAction = 0
    CopyAction = 0
    PasteAction = 0
    DeleteAction = 0
    SelectAllAction = 0
    LowerAction = 0
    RaiseAction = 0
    UndoAction = 0
    RedoAction = 0
    HorizontalLayoutAction = 0
    VerticalLayoutAction = 0
    SplitHorizontalAction = 0
    SplitVerticalAction = 0
    GridLayoutAction = 0
    FormLayoutAction = 0
    BreakLayoutAction = 0
    AdjustSizeAction = 0
    SimplifyLayoutAction = 0
    DefaultPreviewAction = 0
    FormWindowSettingsDialogAction = 0

    def __init__(self, parent = None):
        '''void QDesignerFormWindowManagerInterface.__init__(QObject parent = None)'''
    def showPluginDialog(self):
        '''abstract void QDesignerFormWindowManagerInterface.showPluginDialog()'''
    def closeAllPreviews(self):
        '''abstract void QDesignerFormWindowManagerInterface.closeAllPreviews()'''
    def showPreview(self):
        '''abstract void QDesignerFormWindowManagerInterface.showPreview()'''
    def actionGroup(self, actionGroup):
        '''abstract QActionGroup QDesignerFormWindowManagerInterface.actionGroup(QDesignerFormWindowManagerInterface.ActionGroup actionGroup)'''
        return QActionGroup()
    def action(self, action):
        '''abstract QAction QDesignerFormWindowManagerInterface.action(QDesignerFormWindowManagerInterface.Action action)'''
        return QAction()
    def setActiveFormWindow(self, formWindow):
        '''abstract void QDesignerFormWindowManagerInterface.setActiveFormWindow(QDesignerFormWindowInterface formWindow)'''
    def removeFormWindow(self, formWindow):
        '''abstract void QDesignerFormWindowManagerInterface.removeFormWindow(QDesignerFormWindowInterface formWindow)'''
    def addFormWindow(self, formWindow):
        '''abstract void QDesignerFormWindowManagerInterface.addFormWindow(QDesignerFormWindowInterface formWindow)'''
    formWindowSettingsChanged = pyqtSignal() # void formWindowSettingsChanged(QDesignerFormWindowInterface*) - signal
    activeFormWindowChanged = pyqtSignal() # void activeFormWindowChanged(QDesignerFormWindowInterface*) - signal
    formWindowRemoved = pyqtSignal() # void formWindowRemoved(QDesignerFormWindowInterface*) - signal
    formWindowAdded = pyqtSignal() # void formWindowAdded(QDesignerFormWindowInterface*) - signal
    def core(self):
        '''abstract QDesignerFormEditorInterface QDesignerFormWindowManagerInterface.core()'''
        return QDesignerFormEditorInterface()
    def createFormWindow(self, parent = None, flags = 0):
        '''abstract QDesignerFormWindowInterface QDesignerFormWindowManagerInterface.createFormWindow(QWidget parent = None, Qt.WindowFlags flags = 0)'''
        return QDesignerFormWindowInterface()
    def formWindow(self, index):
        '''abstract QDesignerFormWindowInterface QDesignerFormWindowManagerInterface.formWindow(int index)'''
        return QDesignerFormWindowInterface()
    def formWindowCount(self):
        '''abstract int QDesignerFormWindowManagerInterface.formWindowCount()'''
        return int()
    def activeFormWindow(self):
        '''abstract QDesignerFormWindowInterface QDesignerFormWindowManagerInterface.activeFormWindow()'''
        return QDesignerFormWindowInterface()
    def actionSimplifyLayout(self):
        '''QAction QDesignerFormWindowManagerInterface.actionSimplifyLayout()'''
        return QAction()
    def actionFormLayout(self):
        '''QAction QDesignerFormWindowManagerInterface.actionFormLayout()'''
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
        '''abstract void QDesignerPropertyEditorInterface.setPropertyValue(str name, QVariant value, bool changed = True)'''
    def setObject(self, object):
        '''abstract void QDesignerPropertyEditorInterface.setObject(QObject object)'''
    propertyChanged = pyqtSignal() # void propertyChanged(const QStringamp;,const QVariantamp;) - signal
    def currentPropertyName(self):
        '''abstract str QDesignerPropertyEditorInterface.currentPropertyName()'''
        return str()
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
        '''abstract str QDesignerWidgetBoxInterface.fileName()'''
        return str()
    def setFileName(self, file_name):
        '''abstract void QDesignerWidgetBoxInterface.setFileName(str file_name)'''


class QDesignerContainerExtension():
    """"""
    def __init__(self):
        '''void QDesignerContainerExtension.__init__()'''
    def __init__(self):
        '''QDesignerContainerExtension QDesignerContainerExtension.__init__()'''
        return QDesignerContainerExtension()
    def canRemove(self, index):
        '''bool QDesignerContainerExtension.canRemove(int index)'''
        return bool()
    def canAddWidget(self):
        '''bool QDesignerContainerExtension.canAddWidget()'''
        return bool()
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
        ''' QDesignerContainerExtension.__len__()'''
        return ()
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
        '''str QDesignerCustomWidgetInterface.codeTemplate()'''
        return str()
    def domXml(self):
        '''str QDesignerCustomWidgetInterface.domXml()'''
        return str()
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
        '''abstract str QDesignerCustomWidgetInterface.includeFile()'''
        return str()
    def whatsThis(self):
        '''abstract str QDesignerCustomWidgetInterface.whatsThis()'''
        return str()
    def toolTip(self):
        '''abstract str QDesignerCustomWidgetInterface.toolTip()'''
        return str()
    def group(self):
        '''abstract str QDesignerCustomWidgetInterface.group()'''
        return str()
    def name(self):
        '''abstract str QDesignerCustomWidgetInterface.name()'''
        return str()


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
        '''abstract QObject QAbstractExtensionFactory.extension(QObject object, str iid)'''
        return QObject()


class QExtensionFactory(QObject, QAbstractExtensionFactory):
    """"""
    def __init__(self, parent = None):
        '''void QExtensionFactory.__init__(QExtensionManager parent = None)'''
    def createExtension(self, object, iid, parent):
        '''QObject QExtensionFactory.createExtension(QObject object, str iid, QObject parent)'''
        return QObject()
    def extensionManager(self):
        '''QExtensionManager QExtensionFactory.extensionManager()'''
        return QExtensionManager()
    def extension(self, object, iid):
        '''QObject QExtensionFactory.extension(QObject object, str iid)'''
        return QObject()


class QAbstractExtensionManager():
    """"""
    def __init__(self):
        '''void QAbstractExtensionManager.__init__()'''
    def __init__(self):
        '''QAbstractExtensionManager QAbstractExtensionManager.__init__()'''
        return QAbstractExtensionManager()
    def extension(self, object, iid):
        '''abstract QObject QAbstractExtensionManager.extension(QObject object, str iid)'''
        return QObject()
    def unregisterExtensions(self, factory, iid):
        '''abstract void QAbstractExtensionManager.unregisterExtensions(QAbstractExtensionFactory factory, str iid)'''
    def registerExtensions(self, factory, iid):
        '''abstract void QAbstractExtensionManager.registerExtensions(QAbstractExtensionFactory factory, str iid)'''


class QFormBuilder(QAbstractFormBuilder):
    """"""
    def __init__(self):
        '''void QFormBuilder.__init__()'''
    def customWidgets(self):
        '''list-of-QDesignerCustomWidgetInterface QFormBuilder.customWidgets()'''
        return [QDesignerCustomWidgetInterface()]
    def setPluginPath(self, pluginPaths):
        '''void QFormBuilder.setPluginPath(list-of-str pluginPaths)'''
    def addPluginPath(self, pluginPath):
        '''void QFormBuilder.addPluginPath(str pluginPath)'''
    def clearPluginPaths(self):
        '''void QFormBuilder.clearPluginPaths()'''
    def pluginPaths(self):
        '''list-of-str QFormBuilder.pluginPaths()'''
        return [str()]


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
        '''abstract str QDesignerMemberSheetExtension.signature(int index)'''
        return str()
    def declaredInClass(self, index):
        '''abstract str QDesignerMemberSheetExtension.declaredInClass(int index)'''
        return str()
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
        '''abstract void QDesignerMemberSheetExtension.setMemberGroup(int index, str group)'''
    def memberGroup(self, index):
        '''abstract str QDesignerMemberSheetExtension.memberGroup(int index)'''
        return str()
    def memberName(self, index):
        '''abstract str QDesignerMemberSheetExtension.memberName(int index)'''
        return str()
    def indexOf(self, name):
        '''abstract int QDesignerMemberSheetExtension.indexOf(str name)'''
        return int()
    def __len__(self):
        ''' QDesignerMemberSheetExtension.__len__()'''
        return ()
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
    def isEnabled(self, index):
        '''bool QDesignerPropertySheetExtension.isEnabled(int index)'''
        return bool()
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
        '''abstract void QDesignerPropertySheetExtension.setPropertyGroup(int index, str group)'''
    def propertyGroup(self, index):
        '''abstract str QDesignerPropertySheetExtension.propertyGroup(int index)'''
        return str()
    def propertyName(self, index):
        '''abstract str QDesignerPropertySheetExtension.propertyName(int index)'''
        return str()
    def indexOf(self, name):
        '''abstract int QDesignerPropertySheetExtension.indexOf(str name)'''
        return int()
    def __len__(self):
        ''' QDesignerPropertySheetExtension.__len__()'''
        return ()
    def count(self):
        '''abstract int QDesignerPropertySheetExtension.count()'''
        return int()


class QExtensionManager(QObject, QAbstractExtensionManager):
    """"""
    def __init__(self, parent = None):
        '''void QExtensionManager.__init__(QObject parent = None)'''
    def extension(self, object, iid):
        '''QObject QExtensionManager.extension(QObject object, str iid)'''
        return QObject()
    def unregisterExtensions(self, factory, iid = None):
        '''void QExtensionManager.unregisterExtensions(QAbstractExtensionFactory factory, str iid = '')'''
    def registerExtensions(self, factory, iid = None):
        '''void QExtensionManager.registerExtensions(QAbstractExtensionFactory factory, str iid = '')'''


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


