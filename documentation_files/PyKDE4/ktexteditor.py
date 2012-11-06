class pyqtSignal():
 def connect(self, targetSignal): pass
 def emit(self, *args): pass
from QtCore import *

class KTextEditor():
    """"""
    def createPlugin(self):
        '''static QObject KTextEditor.createPlugin()'''
        return QObject()
    def editor(self):
        '''static str KTextEditor.editor()'''
        return str()
    class Document(KParts.ReadWritePart):
        """"""
        def __init__(self):
            '''QObject KTextEditor.Document.__init__()'''
            return QObject()
        def variableInterface(self):
            '''KTextEditor.VariableInterface KTextEditor.Document.variableInterface()'''
            return KTextEditor.VariableInterface()
        def textHintInterface(self):
            '''KTextEditor.TextHintInterface KTextEditor.Document.textHintInterface()'''
            return KTextEditor.TextHintInterface()
        def templateInterface(self):
            '''KTextEditor.TemplateInterface KTextEditor.Document.templateInterface()'''
            return KTextEditor.TemplateInterface()
        def smartInterface(self):
            '''KTextEditor.SmartInterface KTextEditor.Document.smartInterface()'''
            return KTextEditor.SmartInterface()
        def searchInterface(self):
            '''KTextEditor.SearchInterface KTextEditor.Document.searchInterface()'''
            return KTextEditor.SearchInterface()
        def modificationInterface(self):
            '''KTextEditor.ModificationInterface KTextEditor.Document.modificationInterface()'''
            return KTextEditor.ModificationInterface()
        def markInterface(self):
            '''KTextEditor.MarkInterface KTextEditor.Document.markInterface()'''
            return KTextEditor.MarkInterface()
        def setOpeningErrorMessage(self):
            '''QString KTextEditor.Document.setOpeningErrorMessage()'''
            return QString()
        def setOpeningError(self):
            '''bool KTextEditor.Document.setOpeningError()'''
            return bool()
        def openingErrorMessage(self):
            '''QString KTextEditor.Document.openingErrorMessage()'''
            return QString()
        def openingError(self):
            '''bool KTextEditor.Document.openingError()'''
            return bool()
        def suppressOpeningErrorDialogs(self):
            '''bool KTextEditor.Document.suppressOpeningErrorDialogs()'''
            return bool()
        def setSuppressOpeningErrorDialogs(self):
            '''bool KTextEditor.Document.setSuppressOpeningErrorDialogs()'''
            return bool()
        highlightingModeChanged = pyqtSignal() # void highlightingModeChanged(KTextEditor::Document *) - signal
        modeChanged = pyqtSignal() # void modeChanged(KTextEditor::Document *) - signal
        def modeSection(self):
            '''abstract int KTextEditor.Document.modeSection()'''
            return int()
        def highlightingModeSection(self):
            '''abstract int KTextEditor.Document.highlightingModeSection()'''
            return int()
        def setHighlightingMode(self):
            '''abstract QString KTextEditor.Document.setHighlightingMode()'''
            return QString()
        def setMode(self):
            '''abstract QString KTextEditor.Document.setMode()'''
            return QString()
        def highlightingModes(self):
            '''abstract QStringList KTextEditor.Document.highlightingModes()'''
            return QStringList()
        def modes(self):
            '''abstract QStringList KTextEditor.Document.modes()'''
            return QStringList()
        def highlightingMode(self):
            '''abstract QString KTextEditor.Document.highlightingMode()'''
            return QString()
        def mode(self):
            '''abstract QString KTextEditor.Document.mode()'''
            return QString()
        aboutToClose = pyqtSignal() # void aboutToClose(KTextEditor::Document *) - signal
        textRemoved = pyqtSignal() # void textRemoved(KTextEditor::Document *,const KTextEditor::Rangeamp;) - signal
        textInserted = pyqtSignal() # void textInserted(KTextEditor::Document *,const KTextEditor::Rangeamp;) - signal
        textChanged = pyqtSignal() # void textChanged(KTextEditor::Document *) - signal
        textChanged = pyqtSignal() # void textChanged(KTextEditor::Document *,const KTextEditor::Rangeamp;,const KTextEditor::Rangeamp;) - signal
        def removeLine(self):
            '''abstract int KTextEditor.Document.removeLine()'''
            return int()
        def insertLines(self):
            '''abstract QStringList KTextEditor.Document.insertLines()'''
            return QStringList()
        def insertLine(self):
            '''abstract QString KTextEditor.Document.insertLine()'''
            return QString()
        def cursorInText(self):
            '''KTextEditor.Cursor KTextEditor.Document.cursorInText()'''
            return KTextEditor.Cursor()
        def removeText(self):
            '''abstract bool KTextEditor.Document.removeText()'''
            return bool()
        def replaceText(self):
            '''bool KTextEditor.Document.replaceText()'''
            return bool()
        def replaceText(self):
            '''bool KTextEditor.Document.replaceText()'''
            return bool()
        def insertText(self):
            '''abstract bool KTextEditor.Document.insertText()'''
            return bool()
        def insertText(self):
            '''abstract bool KTextEditor.Document.insertText()'''
            return bool()
        def clear(self):
            '''abstract bool KTextEditor.Document.clear()'''
            return bool()
        def setText(self):
            '''abstract QString KTextEditor.Document.setText()'''
            return QString()
        def setText(self):
            '''abstract QStringList KTextEditor.Document.setText()'''
            return QStringList()
        def endOfLine(self):
            '''int KTextEditor.Document.endOfLine()'''
            return int()
        def lineLength(self):
            '''abstract int KTextEditor.Document.lineLength()'''
            return int()
        def isEmpty(self):
            '''bool KTextEditor.Document.isEmpty()'''
            return bool()
        def totalCharacters(self):
            '''abstract int KTextEditor.Document.totalCharacters()'''
            return int()
        def documentRange(self):
            '''KTextEditor.Range KTextEditor.Document.documentRange()'''
            return KTextEditor.Range()
        def documentEnd(self):
            '''abstract KTextEditor.Cursor KTextEditor.Document.documentEnd()'''
            return KTextEditor.Cursor()
        def lines(self):
            '''abstract int KTextEditor.Document.lines()'''
            return int()
        def line(self):
            '''abstract int KTextEditor.Document.line()'''
            return int()
        def textLines(self):
            '''abstract bool KTextEditor.Document.textLines()'''
            return bool()
        def character(self):
            '''abstract KTextEditor.Cursor KTextEditor.Document.character()'''
            return KTextEditor.Cursor()
        def text(self):
            '''abstract QString KTextEditor.Document.text()'''
            return QString()
        def text(self):
            '''abstract bool KTextEditor.Document.text()'''
            return bool()
        def endEditing(self):
            '''abstract bool KTextEditor.Document.endEditing()'''
            return bool()
        def startEditing(self):
            '''abstract bool KTextEditor.Document.startEditing()'''
            return bool()
        def documentSaveAs(self):
            '''abstract bool KTextEditor.Document.documentSaveAs()'''
            return bool()
        def documentSave(self):
            '''abstract bool KTextEditor.Document.documentSave()'''
            return bool()
        def documentReload(self):
            '''abstract bool KTextEditor.Document.documentReload()'''
            return bool()
        def encoding(self):
            '''abstract QString KTextEditor.Document.encoding()'''
            return QString()
        def setEncoding(self):
            '''abstract QString KTextEditor.Document.setEncoding()'''
            return QString()
        modifiedChanged = pyqtSignal() # void modifiedChanged(KTextEditor::Document *) - signal
        documentUrlChanged = pyqtSignal() # void documentUrlChanged(KTextEditor::Document *) - signal
        documentNameChanged = pyqtSignal() # void documentNameChanged(KTextEditor::Document *) - signal
        def mimeType(self):
            '''abstract QString KTextEditor.Document.mimeType()'''
            return QString()
        def documentName(self):
            '''abstract QString KTextEditor.Document.documentName()'''
            return QString()
        viewCreated = pyqtSignal() # void viewCreated(KTextEditor::Document *,KTextEditor::View *) - signal
        def views(self):
            '''abstract list-of-KTextEditor.View KTextEditor.Document.views()'''
            return [KTextEditor.View()]
        def activeView(self):
            '''abstract KTextEditor.View KTextEditor.Document.activeView()'''
            return KTextEditor.View()
        def createView(self):
            '''abstract QWidget KTextEditor.Document.createView()'''
            return QWidget()
        def editor(self):
            '''abstract KTextEditor.Editor KTextEditor.Document.editor()'''
            return KTextEditor.Editor()
    class Attribute():
        """"""
        class Effects():
            """"""
            def __init__(self):
                '''KTextEditor.Attribute.Effects KTextEditor.Attribute.Effects.__init__()'''
                return KTextEditor.Attribute.Effects()
            def __init__(self):
                '''int KTextEditor.Attribute.Effects.__init__()'''
                return int()
            def __init__(self):
                '''void KTextEditor.Attribute.Effects.__init__()'''
            def __bool__(self):
                '''int KTextEditor.Attribute.Effects.__bool__()'''
                return int()
            def __ne__(self, f):
                '''bool KTextEditor.Attribute.Effects.__ne__(KTextEditor.Attribute.Effects f)'''
                return bool()
            def __eq__(self, f):
                '''bool KTextEditor.Attribute.Effects.__eq__(KTextEditor.Attribute.Effects f)'''
                return bool()
            def __invert__(self):
                '''KTextEditor.Attribute.Effects KTextEditor.Attribute.Effects.__invert__()'''
                return KTextEditor.Attribute.Effects()
            def __and__(self, mask):
                '''KTextEditor.Attribute.Effects KTextEditor.Attribute.Effects.__and__(int mask)'''
                return KTextEditor.Attribute.Effects()
            def __xor__(self, f):
                '''KTextEditor.Attribute.Effects KTextEditor.Attribute.Effects.__xor__(KTextEditor.Attribute.Effects f)'''
                return KTextEditor.Attribute.Effects()
            def __xor__(self, f):
                '''KTextEditor.Attribute.Effects KTextEditor.Attribute.Effects.__xor__(int f)'''
                return KTextEditor.Attribute.Effects()
            def __or__(self, f):
                '''KTextEditor.Attribute.Effects KTextEditor.Attribute.Effects.__or__(KTextEditor.Attribute.Effects f)'''
                return KTextEditor.Attribute.Effects()
            def __or__(self, f):
                '''KTextEditor.Attribute.Effects KTextEditor.Attribute.Effects.__or__(int f)'''
                return KTextEditor.Attribute.Effects()
            def __int__(self):
                '''int KTextEditor.Attribute.Effects.__int__()'''
                return int()
            def __ixor__(self, f):
                '''KTextEditor.Attribute.Effects KTextEditor.Attribute.Effects.__ixor__(KTextEditor.Attribute.Effects f)'''
                return KTextEditor.Attribute.Effects()
            def __ior__(self, f):
                '''KTextEditor.Attribute.Effects KTextEditor.Attribute.Effects.__ior__(KTextEditor.Attribute.Effects f)'''
                return KTextEditor.Attribute.Effects()
            def __iand__(self, mask):
                '''KTextEditor.Attribute.Effects KTextEditor.Attribute.Effects.__iand__(int mask)'''
                return KTextEditor.Attribute.Effects()
    class View(QWidget, KXMLGUIClient):
        """"""
        # Enum KTextEditor.View.EditMode
        EditInsert = 0
        EditOverwrite = 0
    
        def __init__(self):
            '''QWidget KTextEditor.View.__init__()'''
            return QWidget()
        def textHintInterface(self):
            '''KTextEditor.TextHintInterface KTextEditor.View.textHintInterface()'''
            return KTextEditor.TextHintInterface()
        def sessionConfigInterface(self):
            '''KTextEditor.SessionConfigInterface KTextEditor.View.sessionConfigInterface()'''
            return KTextEditor.SessionConfigInterface()
        def codeCompletionInterface(self):
            '''KTextEditor.CodeCompletionInterface KTextEditor.View.codeCompletionInterface()'''
            return KTextEditor.CodeCompletionInterface()
        def insertText(self):
            '''QString KTextEditor.View.insertText()'''
            return QString()
        selectionChanged = pyqtSignal() # void selectionChanged(KTextEditor::View *) - signal
        def blockSelection(self):
            '''abstract bool KTextEditor.View.blockSelection()'''
            return bool()
        def setBlockSelection(self):
            '''abstract bool KTextEditor.View.setBlockSelection()'''
            return bool()
        def removeSelectionText(self):
            '''abstract bool KTextEditor.View.removeSelectionText()'''
            return bool()
        def removeSelection(self):
            '''abstract bool KTextEditor.View.removeSelection()'''
            return bool()
        def selectionText(self):
            '''abstract QString KTextEditor.View.selectionText()'''
            return QString()
        def selectionRange(self):
            '''abstract KTextEditor.Range KTextEditor.View.selectionRange()'''
            return KTextEditor.Range()
        def selection(self):
            '''abstract bool KTextEditor.View.selection()'''
            return bool()
        def setSelection(self):
            '''abstract KTextEditor.Range KTextEditor.View.setSelection()'''
            return KTextEditor.Range()
        def setSelection(self):
            '''bool KTextEditor.View.setSelection()'''
            return bool()
        mousePositionChanged = pyqtSignal() # void mousePositionChanged(KTextEditor::View *,const KTextEditor::Cursoramp;) - signal
        def setMouseTrackingEnabled(self):
            '''abstract bool KTextEditor.View.setMouseTrackingEnabled()'''
            return bool()
        def mouseTrackingEnabled(self):
            '''abstract bool KTextEditor.View.mouseTrackingEnabled()'''
            return bool()
        horizontalScrollPositionChanged = pyqtSignal() # void horizontalScrollPositionChanged(KTextEditor::View *) - signal
        verticalScrollPositionChanged = pyqtSignal() # void verticalScrollPositionChanged(KTextEditor::View *,const KTextEditor::Cursoramp;) - signal
        cursorPositionChanged = pyqtSignal() # void cursorPositionChanged(KTextEditor::View *,const KTextEditor::Cursoramp;) - signal
        def cursorPositionCoordinates(self):
            '''abstract QPoint KTextEditor.View.cursorPositionCoordinates()'''
            return QPoint()
        def cursorToCoordinate(self):
            '''abstract KTextEditor.Cursor KTextEditor.View.cursorToCoordinate()'''
            return KTextEditor.Cursor()
        def cursorPositionVirtual(self):
            '''abstract KTextEditor.Cursor KTextEditor.View.cursorPositionVirtual()'''
            return KTextEditor.Cursor()
        def cursorPosition(self):
            '''abstract KTextEditor.Cursor KTextEditor.View.cursorPosition()'''
            return KTextEditor.Cursor()
        def setCursorPosition(self):
            '''abstract KTextEditor.Cursor KTextEditor.View.setCursorPosition()'''
            return KTextEditor.Cursor()
        contextMenuAboutToShow = pyqtSignal() # void contextMenuAboutToShow(KTextEditor::View *,QMenu *) - signal
        def defaultContextMenu(self):
            '''abstract QMenu KTextEditor.View.defaultContextMenu()'''
            return QMenu()
        def contextMenu(self):
            '''abstract QMenu KTextEditor.View.contextMenu()'''
            return QMenu()
        def setContextMenu(self):
            '''abstract QMenu KTextEditor.View.setContextMenu()'''
            return QMenu()
        textInserted = pyqtSignal() # void textInserted(KTextEditor::View *,const KTextEditor::Cursoramp;,const QStringamp;) - signal
        informationMessage = pyqtSignal() # void informationMessage(KTextEditor::View *,const QStringamp;) - signal
        viewEditModeChanged = pyqtSignal() # void viewEditModeChanged(KTextEditor::View *,KTextEditor::View::EditMode) - signal
        viewModeChanged = pyqtSignal() # void viewModeChanged(KTextEditor::View *) - signal
        focusOut = pyqtSignal() # void focusOut(KTextEditor::View *) - signal
        focusIn = pyqtSignal() # void focusIn(KTextEditor::View *) - signal
        def viewEditMode(self):
            '''abstract KTextEditor.View.EditMode KTextEditor.View.viewEditMode()'''
            return KTextEditor.View.EditMode()
        def viewMode(self):
            '''abstract QString KTextEditor.View.viewMode()'''
            return QString()
        def isActiveView(self):
            '''bool KTextEditor.View.isActiveView()'''
            return bool()
        def document(self):
            '''abstract KTextEditor.Document KTextEditor.View.document()'''
            return KTextEditor.Document()
    class ConfigInterface():
        """"""
        def __init__(self):
            '''void KTextEditor.ConfigInterface.__init__()'''
        def setConfigValue(self):
            '''abstract QVariant KTextEditor.ConfigInterface.setConfigValue()'''
            return QVariant()
        def configValue(self):
            '''abstract QString KTextEditor.ConfigInterface.configValue()'''
            return QString()
        def configKeys(self):
            '''abstract QStringList KTextEditor.ConfigInterface.configKeys()'''
            return QStringList()
    class Command():
        """"""
        def __init__(self):
            '''void KTextEditor.Command.__init__()'''
        def __init__(self):
            '''KTextEditor.Command KTextEditor.Command.__init__()'''
            return KTextEditor.Command()
        def help(self):
            '''abstract QString KTextEditor.Command.help()'''
            return QString()
        def exec_(self):
            '''abstract QString KTextEditor.Command.exec_()'''
            return QString()
        def cmds(self):
            '''abstract QStringList KTextEditor.Command.cmds()'''
            return QStringList()
    class SmartRange():
        """"""
        class InsertBehaviors():
            """"""
            def __init__(self):
                '''KTextEditor.SmartRange.InsertBehaviors KTextEditor.SmartRange.InsertBehaviors.__init__()'''
                return KTextEditor.SmartRange.InsertBehaviors()
            def __init__(self):
                '''int KTextEditor.SmartRange.InsertBehaviors.__init__()'''
                return int()
            def __init__(self):
                '''void KTextEditor.SmartRange.InsertBehaviors.__init__()'''
            def __bool__(self):
                '''int KTextEditor.SmartRange.InsertBehaviors.__bool__()'''
                return int()
            def __ne__(self, f):
                '''bool KTextEditor.SmartRange.InsertBehaviors.__ne__(KTextEditor.SmartRange.InsertBehaviors f)'''
                return bool()
            def __eq__(self, f):
                '''bool KTextEditor.SmartRange.InsertBehaviors.__eq__(KTextEditor.SmartRange.InsertBehaviors f)'''
                return bool()
            def __invert__(self):
                '''KTextEditor.SmartRange.InsertBehaviors KTextEditor.SmartRange.InsertBehaviors.__invert__()'''
                return KTextEditor.SmartRange.InsertBehaviors()
            def __and__(self, mask):
                '''KTextEditor.SmartRange.InsertBehaviors KTextEditor.SmartRange.InsertBehaviors.__and__(int mask)'''
                return KTextEditor.SmartRange.InsertBehaviors()
            def __xor__(self, f):
                '''KTextEditor.SmartRange.InsertBehaviors KTextEditor.SmartRange.InsertBehaviors.__xor__(KTextEditor.SmartRange.InsertBehaviors f)'''
                return KTextEditor.SmartRange.InsertBehaviors()
            def __xor__(self, f):
                '''KTextEditor.SmartRange.InsertBehaviors KTextEditor.SmartRange.InsertBehaviors.__xor__(int f)'''
                return KTextEditor.SmartRange.InsertBehaviors()
            def __or__(self, f):
                '''KTextEditor.SmartRange.InsertBehaviors KTextEditor.SmartRange.InsertBehaviors.__or__(KTextEditor.SmartRange.InsertBehaviors f)'''
                return KTextEditor.SmartRange.InsertBehaviors()
            def __or__(self, f):
                '''KTextEditor.SmartRange.InsertBehaviors KTextEditor.SmartRange.InsertBehaviors.__or__(int f)'''
                return KTextEditor.SmartRange.InsertBehaviors()
            def __int__(self):
                '''int KTextEditor.SmartRange.InsertBehaviors.__int__()'''
                return int()
            def __ixor__(self, f):
                '''KTextEditor.SmartRange.InsertBehaviors KTextEditor.SmartRange.InsertBehaviors.__ixor__(KTextEditor.SmartRange.InsertBehaviors f)'''
                return KTextEditor.SmartRange.InsertBehaviors()
            def __ior__(self, f):
                '''KTextEditor.SmartRange.InsertBehaviors KTextEditor.SmartRange.InsertBehaviors.__ior__(KTextEditor.SmartRange.InsertBehaviors f)'''
                return KTextEditor.SmartRange.InsertBehaviors()
            def __iand__(self, mask):
                '''KTextEditor.SmartRange.InsertBehaviors KTextEditor.SmartRange.InsertBehaviors.__iand__(int mask)'''
                return KTextEditor.SmartRange.InsertBehaviors()
    class Mark():
        """"""
        line = None # int - member
        type = None # int - member
        def __init__(self):
            '''void KTextEditor.Mark.__init__()'''
        def __init__(self):
            '''KTextEditor.Mark KTextEditor.Mark.__init__()'''
            return KTextEditor.Mark()
    class Attribute(QTextCharFormat):
        """"""
        # Enum KTextEditor.Attribute.Effect
        EffectNone = 0
        EffectFadeIn = 0
        EffectFadeOut = 0
        EffectPulse = 0
        EffectCycleGradient = 0
    
        # Enum KTextEditor.Attribute.ActivationType
        ActivateMouseIn = 0
        ActivateCaretIn = 0
    
        # Enum KTextEditor.Attribute.CustomProperties
        Outline = 0
        SelectedForeground = 0
        SelectedBackground = 0
        BackgroundFillWhitespace = 0
        AttributeDynamicEffect = 0
        AttributeInternalProperty = 0
        AttributeUserProperty = 0
    
        def __init__(self):
            '''void KTextEditor.Attribute.__init__()'''
        def __init__(self):
            '''KTextEditor.Attribute KTextEditor.Attribute.__init__()'''
            return KTextEditor.Attribute()
        def __iadd__(self):
            '''KTextEditor.Attribute KTextEditor.Attribute.__iadd__()'''
            return KTextEditor.Attribute()
        def setEffects(self):
            '''KTextEditor.Attribute.Effects KTextEditor.Attribute.setEffects()'''
            return KTextEditor.Attribute.Effects()
        def effects(self):
            '''KTextEditor.Attribute.Effects KTextEditor.Attribute.effects()'''
            return KTextEditor.Attribute.Effects()
        def setDynamicAttribute(self):
            '''unknown-type KTextEditor.Attribute.setDynamicAttribute()'''
            return unknown-type()
        def dynamicAttribute(self):
            '''KTextEditor.Attribute.ActivationType KTextEditor.Attribute.dynamicAttribute()'''
            return KTextEditor.Attribute.ActivationType()
        def clearAssociatedActions(self):
            '''void KTextEditor.Attribute.clearAssociatedActions()'''
        def associatedActions(self):
            '''list-of-KAction KTextEditor.Attribute.associatedActions()'''
            return [KAction()]
        def hasAnyProperty(self):
            '''bool KTextEditor.Attribute.hasAnyProperty()'''
            return bool()
        def clear(self):
            '''void KTextEditor.Attribute.clear()'''
        def setBackgroundFillWhitespace(self):
            '''bool KTextEditor.Attribute.setBackgroundFillWhitespace()'''
            return bool()
        def backgroundFillWhitespace(self):
            '''bool KTextEditor.Attribute.backgroundFillWhitespace()'''
            return bool()
        def setSelectedBackground(self):
            '''QBrush KTextEditor.Attribute.setSelectedBackground()'''
            return QBrush()
        def selectedBackground(self):
            '''QBrush KTextEditor.Attribute.selectedBackground()'''
            return QBrush()
        def setSelectedForeground(self):
            '''QBrush KTextEditor.Attribute.setSelectedForeground()'''
            return QBrush()
        def selectedForeground(self):
            '''QBrush KTextEditor.Attribute.selectedForeground()'''
            return QBrush()
        def setOutline(self):
            '''QBrush KTextEditor.Attribute.setOutline()'''
            return QBrush()
        def outline(self):
            '''QBrush KTextEditor.Attribute.outline()'''
            return QBrush()
        def setFontBold(self):
            '''bool KTextEditor.Attribute.setFontBold()'''
            return bool()
        def fontBold(self):
            '''bool KTextEditor.Attribute.fontBold()'''
            return bool()
    class CommandInterface():
        """"""
        def __init__(self):
            '''void KTextEditor.CommandInterface.__init__()'''
        def __init__(self):
            '''KTextEditor.CommandInterface KTextEditor.CommandInterface.__init__()'''
            return KTextEditor.CommandInterface()
        def commandList(self):
            '''abstract QStringList KTextEditor.CommandInterface.commandList()'''
            return QStringList()
        def commands(self):
            '''abstract list-of-KTextEditor.Command KTextEditor.CommandInterface.commands()'''
            return [KTextEditor.Command()]
        def queryCommand(self):
            '''abstract QString KTextEditor.CommandInterface.queryCommand()'''
            return QString()
        def unregisterCommand(self):
            '''abstract KTextEditor.Command KTextEditor.CommandInterface.unregisterCommand()'''
            return KTextEditor.Command()
        def registerCommand(self):
            '''abstract KTextEditor.Command KTextEditor.CommandInterface.registerCommand()'''
            return KTextEditor.Command()
    class SmartInterface():
        """"""
        def __init__(self):
            '''void KTextEditor.SmartInterface.__init__()'''
        def attributeNotDynamic(self):
            '''abstract unknown-type KTextEditor.SmartInterface.attributeNotDynamic()'''
            return unknown-type()
        def attributeDynamic(self):
            '''abstract unknown-type KTextEditor.SmartInterface.attributeDynamic()'''
            return unknown-type()
        def clearViewActions(self):
            '''abstract KTextEditor.View KTextEditor.SmartInterface.clearViewActions()'''
            return KTextEditor.View()
        def viewActions(self):
            '''abstract KTextEditor.View KTextEditor.SmartInterface.viewActions()'''
            return KTextEditor.View()
        def removeActionsFromView(self):
            '''abstract KTextEditor.SmartRange KTextEditor.SmartInterface.removeActionsFromView()'''
            return KTextEditor.SmartRange()
        def addActionsToView(self):
            '''abstract KTextEditor.SmartRange KTextEditor.SmartInterface.addActionsToView()'''
            return KTextEditor.SmartRange()
        def clearDocumentActions(self):
            '''abstract void KTextEditor.SmartInterface.clearDocumentActions()'''
        def documentActions(self):
            '''abstract list-of-KTextEditor.SmartRange KTextEditor.SmartInterface.documentActions()'''
            return [KTextEditor.SmartRange()]
        def removeActionsFromDocument(self):
            '''abstract KTextEditor.SmartRange KTextEditor.SmartInterface.removeActionsFromDocument()'''
            return KTextEditor.SmartRange()
        def addActionsToDocument(self):
            '''abstract KTextEditor.SmartRange KTextEditor.SmartInterface.addActionsToDocument()'''
            return KTextEditor.SmartRange()
        def clearViewHighlights(self):
            '''abstract KTextEditor.View KTextEditor.SmartInterface.clearViewHighlights()'''
            return KTextEditor.View()
        def viewHighlights(self):
            '''abstract KTextEditor.View KTextEditor.SmartInterface.viewHighlights()'''
            return KTextEditor.View()
        def removeHighlightFromView(self):
            '''abstract KTextEditor.SmartRange KTextEditor.SmartInterface.removeHighlightFromView()'''
            return KTextEditor.SmartRange()
        def addHighlightToView(self):
            '''abstract bool KTextEditor.SmartInterface.addHighlightToView()'''
            return bool()
        def clearDocumentHighlights(self):
            '''abstract void KTextEditor.SmartInterface.clearDocumentHighlights()'''
        def documentHighlights(self):
            '''abstract list-of-KTextEditor.SmartRange KTextEditor.SmartInterface.documentHighlights()'''
            return [KTextEditor.SmartRange()]
        def removeHighlightFromDocument(self):
            '''abstract KTextEditor.SmartRange KTextEditor.SmartInterface.removeHighlightFromDocument()'''
            return KTextEditor.SmartRange()
        def addHighlightToDocument(self):
            '''abstract bool KTextEditor.SmartInterface.addHighlightToDocument()'''
            return bool()
        def deleteRanges(self):
            '''abstract void KTextEditor.SmartInterface.deleteRanges()'''
        def unbindSmartRange(self):
            '''abstract KTextEditor.SmartRange KTextEditor.SmartInterface.unbindSmartRange()'''
            return KTextEditor.SmartRange()
        def newSmartRange(self):
            '''abstract KTextEditor.SmartRange.InsertBehaviors KTextEditor.SmartInterface.newSmartRange()'''
            return KTextEditor.SmartRange.InsertBehaviors()
        def newSmartRange(self):
            '''KTextEditor.SmartRange.InsertBehaviors KTextEditor.SmartInterface.newSmartRange()'''
            return KTextEditor.SmartRange.InsertBehaviors()
        def newSmartRange(self):
            '''KTextEditor.SmartRange.InsertBehaviors KTextEditor.SmartInterface.newSmartRange()'''
            return KTextEditor.SmartRange.InsertBehaviors()
        def newSmartRange(self):
            '''abstract KTextEditor.SmartRange.InsertBehaviors KTextEditor.SmartInterface.newSmartRange()'''
            return KTextEditor.SmartRange.InsertBehaviors()
        def deleteCursors(self):
            '''abstract void KTextEditor.SmartInterface.deleteCursors()'''
        def newSmartCursor(self):
            '''abstract KTextEditor.SmartCursor.InsertBehavior KTextEditor.SmartInterface.newSmartCursor()'''
            return KTextEditor.SmartCursor.InsertBehavior()
        def newSmartCursor(self):
            '''KTextEditor.SmartCursor.InsertBehavior KTextEditor.SmartInterface.newSmartCursor()'''
            return KTextEditor.SmartCursor.InsertBehavior()
        def translateFromRevision(self):
            '''KTextEditor.SmartCursor.InsertBehavior KTextEditor.SmartInterface.translateFromRevision()'''
            return KTextEditor.SmartCursor.InsertBehavior()
        def translateFromRevision(self):
            '''KTextEditor.SmartRange.InsertBehaviors KTextEditor.SmartInterface.translateFromRevision()'''
            return KTextEditor.SmartRange.InsertBehaviors()
        def clearRevision(self):
            '''void KTextEditor.SmartInterface.clearRevision()'''
        def useRevision(self):
            '''abstract int KTextEditor.SmartInterface.useRevision()'''
            return int()
        def releaseRevision(self):
            '''abstract int KTextEditor.SmartInterface.releaseRevision()'''
            return int()
        def currentRevision(self):
            '''abstract int KTextEditor.SmartInterface.currentRevision()'''
            return int()
        def setClearOnDocumentReload(self):
            '''bool KTextEditor.SmartInterface.setClearOnDocumentReload()'''
            return bool()
        def clearOnDocumentReload(self):
            '''bool KTextEditor.SmartInterface.clearOnDocumentReload()'''
            return bool()
        def clearSmartInterface(self):
            '''abstract void KTextEditor.SmartInterface.clearSmartInterface()'''
        def smartMutex(self):
            '''QMutex KTextEditor.SmartInterface.smartMutex()'''
            return QMutex()
    class CodeCompletionModel(QAbstractItemModel):
        """"""
        # Enum KTextEditor.CodeCompletionModel.InvocationType
        AutomaticInvocation = 0
        UserInvocation = 0
        ManualInvocation = 0
    
        # Enum KTextEditor.CodeCompletionModel.ExtraItemDataRoles
        CompletionRole = 0
        ScopeIndex = 0
        MatchQuality = 0
        SetMatchContext = 0
        HighlightingMethod = 0
        CustomHighlight = 0
        InheritanceDepth = 0
        IsExpandable = 0
        ExpandingWidget = 0
        ItemSelected = 0
        ArgumentHintDepth = 0
        BestMatchesCount = 0
        AccessibilityNext = 0
        AccessibilityPrevious = 0
        AccessibilityAccept = 0
    
        # Enum KTextEditor.CodeCompletionModel.HighlightMethod
        NoHighlighting = 0
        InternalHighlighting = 0
        CustomHighlighting = 0
    
        # Enum KTextEditor.CodeCompletionModel.CompletionProperty
        NoProperty = 0
        FirstProperty = 0
        Public = 0
        Protected = 0
        Private = 0
        Static = 0
        Const = 0
        Namespace = 0
        Class = 0
        Struct = 0
        Union = 0
        Function = 0
        Variable = 0
        Enum = 0
        Template = 0
        TypeAlias = 0
        Virtual = 0
        Override = 0
        Inline = 0
        Friend = 0
        Signal = 0
        Slot = 0
        LocalScope = 0
        NamespaceScope = 0
        GlobalScope = 0
        LastProperty = 0
    
        # Enum KTextEditor.CodeCompletionModel.Columns
        Prefix = 0
        Icon = 0
        Scope = 0
        Name = 0
        Arguments = 0
        Postfix = 0
    
        ColumnCount = None # int - member
        LastItemDataRole = None # int - member
        def __init__(self):
            '''QObject KTextEditor.CodeCompletionModel.__init__()'''
            return QObject()
        def rowCount(self):
            '''QModelIndex KTextEditor.CodeCompletionModel.rowCount()'''
            return QModelIndex()
        def parent(self):
            '''QModelIndex KTextEditor.CodeCompletionModel.parent()'''
            return QModelIndex()
        def itemData(self):
            '''QModelIndex KTextEditor.CodeCompletionModel.itemData()'''
            return QModelIndex()
        def index(self):
            '''QModelIndex KTextEditor.CodeCompletionModel.index()'''
            return QModelIndex()
        def columnCount(self):
            '''QModelIndex KTextEditor.CodeCompletionModel.columnCount()'''
            return QModelIndex()
        def executeCompletionItem(self):
            '''int KTextEditor.CodeCompletionModel.executeCompletionItem()'''
            return int()
        def completionInvoked(self):
            '''KTextEditor.CodeCompletionModel.InvocationType KTextEditor.CodeCompletionModel.completionInvoked()'''
            return KTextEditor.CodeCompletionModel.InvocationType()
        def setRowCount(self):
            '''int KTextEditor.CodeCompletionModel.setRowCount()'''
            return int()
    class ConfigPage(QWidget):
        """"""
        def __init__(self):
            '''QWidget KTextEditor.ConfigPage.__init__()'''
            return QWidget()
        changed = pyqtSignal() # void changed() - signal
        def defaults(self):
            '''abstract void KTextEditor.ConfigPage.defaults()'''
        def reset(self):
            '''abstract void KTextEditor.ConfigPage.reset()'''
        def apply(self):
            '''abstract void KTextEditor.ConfigPage.apply()'''
    class CommandExtension():
        """"""
        def __init__(self):
            '''void KTextEditor.CommandExtension.__init__()'''
        def __init__(self):
            '''KTextEditor.CommandExtension KTextEditor.CommandExtension.__init__()'''
            return KTextEditor.CommandExtension()
        def processText(self):
            '''abstract QString KTextEditor.CommandExtension.processText()'''
            return QString()
        def wantsToProcessText(self):
            '''abstract QString KTextEditor.CommandExtension.wantsToProcessText()'''
            return QString()
        def completionObject(self):
            '''abstract QString KTextEditor.CommandExtension.completionObject()'''
            return QString()
        def flagCompletions(self):
            '''abstract QStringList KTextEditor.CommandExtension.flagCompletions()'''
            return QStringList()
    class SmartCursorWatcher():
        """"""
        def __init__(self):
            '''void KTextEditor.SmartCursorWatcher.__init__()'''
        def __init__(self):
            '''KTextEditor.SmartCursorWatcher KTextEditor.SmartCursorWatcher.__init__()'''
            return KTextEditor.SmartCursorWatcher()
        def deleted(self):
            '''KTextEditor.SmartCursor KTextEditor.SmartCursorWatcher.deleted()'''
            return KTextEditor.SmartCursor()
        def characterInserted(self):
            '''bool KTextEditor.SmartCursorWatcher.characterInserted()'''
            return bool()
        def characterDeleted(self):
            '''bool KTextEditor.SmartCursorWatcher.characterDeleted()'''
            return bool()
        def positionDeleted(self):
            '''KTextEditor.SmartCursor KTextEditor.SmartCursorWatcher.positionDeleted()'''
            return KTextEditor.SmartCursor()
        def positionChanged(self):
            '''KTextEditor.SmartCursor KTextEditor.SmartCursorWatcher.positionChanged()'''
            return KTextEditor.SmartCursor()
        def setWantsDirectChanges(self):
            '''bool KTextEditor.SmartCursorWatcher.setWantsDirectChanges()'''
            return bool()
        def wantsDirectChanges(self):
            '''bool KTextEditor.SmartCursorWatcher.wantsDirectChanges()'''
            return bool()
    class SmartRangeWatcher():
        """"""
        def __init__(self):
            '''void KTextEditor.SmartRangeWatcher.__init__()'''
        def __init__(self):
            '''KTextEditor.SmartRangeWatcher KTextEditor.SmartRangeWatcher.__init__()'''
            return KTextEditor.SmartRangeWatcher()
        def rangeAttributeChanged(self):
            '''unknown-type KTextEditor.SmartRangeWatcher.rangeAttributeChanged()'''
            return unknown-type()
        def childRangeRemoved(self):
            '''KTextEditor.SmartRange KTextEditor.SmartRangeWatcher.childRangeRemoved()'''
            return KTextEditor.SmartRange()
        def childRangeInserted(self):
            '''KTextEditor.SmartRange KTextEditor.SmartRangeWatcher.childRangeInserted()'''
            return KTextEditor.SmartRange()
        def parentRangeChanged(self):
            '''KTextEditor.SmartRange KTextEditor.SmartRangeWatcher.parentRangeChanged()'''
            return KTextEditor.SmartRange()
        def rangeDeleted(self):
            '''KTextEditor.SmartRange KTextEditor.SmartRangeWatcher.rangeDeleted()'''
            return KTextEditor.SmartRange()
        def rangeEliminated(self):
            '''KTextEditor.SmartRange KTextEditor.SmartRangeWatcher.rangeEliminated()'''
            return KTextEditor.SmartRange()
        def caretExitedRange(self):
            '''KTextEditor.View KTextEditor.SmartRangeWatcher.caretExitedRange()'''
            return KTextEditor.View()
        def caretEnteredRange(self):
            '''KTextEditor.View KTextEditor.SmartRangeWatcher.caretEnteredRange()'''
            return KTextEditor.View()
        def mouseExitedRange(self):
            '''KTextEditor.View KTextEditor.SmartRangeWatcher.mouseExitedRange()'''
            return KTextEditor.View()
        def mouseEnteredRange(self):
            '''KTextEditor.View KTextEditor.SmartRangeWatcher.mouseEnteredRange()'''
            return KTextEditor.View()
        def rangeContentsChanged(self):
            '''KTextEditor.SmartRange KTextEditor.SmartRangeWatcher.rangeContentsChanged()'''
            return KTextEditor.SmartRange()
        def rangeContentsChanged(self):
            '''KTextEditor.SmartRange KTextEditor.SmartRangeWatcher.rangeContentsChanged()'''
            return KTextEditor.SmartRange()
        def rangePositionChanged(self):
            '''KTextEditor.SmartRange KTextEditor.SmartRangeWatcher.rangePositionChanged()'''
            return KTextEditor.SmartRange()
        def setWantsDirectChanges(self):
            '''bool KTextEditor.SmartRangeWatcher.setWantsDirectChanges()'''
            return bool()
        def wantsDirectChanges(self):
            '''bool KTextEditor.SmartRangeWatcher.wantsDirectChanges()'''
            return bool()
    class Factory(KParts.Factory):
        """"""
        def __init__(self):
            '''QObject KTextEditor.Factory.__init__()'''
            return QObject()
        def editor(self):
            '''abstract KTextEditor.Editor KTextEditor.Factory.editor()'''
            return KTextEditor.Editor()
    class Plugin(QObject):
        """"""
        def __init__(self):
            '''QObject KTextEditor.Plugin.__init__()'''
            return QObject()
        def removeView(self):
            '''KTextEditor.View KTextEditor.Plugin.removeView()'''
            return KTextEditor.View()
        def addView(self):
            '''KTextEditor.View KTextEditor.Plugin.addView()'''
            return KTextEditor.View()
        def removeDocument(self):
            '''KTextEditor.Document KTextEditor.Plugin.removeDocument()'''
            return KTextEditor.Document()
        def addDocument(self):
            '''KTextEditor.Document KTextEditor.Plugin.addDocument()'''
            return KTextEditor.Document()
    class SearchInterface():
        """"""
        def __init__(self):
            '''void KTextEditor.SearchInterface.__init__()'''
        def supportedSearchOptions(self):
            '''abstract KTextEditor.Search.SearchOptions KTextEditor.SearchInterface.supportedSearchOptions()'''
            return KTextEditor.Search.SearchOptions()
        def searchText(self):
            '''abstract KTextEditor.Search.SearchOptions KTextEditor.SearchInterface.searchText()'''
            return KTextEditor.Search.SearchOptions()
    class Search():
        """"""
        class SearchOptions():
            """"""
            def __init__(self):
                '''KTextEditor.Search.SearchOptions KTextEditor.Search.SearchOptions.__init__()'''
                return KTextEditor.Search.SearchOptions()
            def __init__(self):
                '''int KTextEditor.Search.SearchOptions.__init__()'''
                return int()
            def __init__(self):
                '''void KTextEditor.Search.SearchOptions.__init__()'''
            def __bool__(self):
                '''int KTextEditor.Search.SearchOptions.__bool__()'''
                return int()
            def __ne__(self, f):
                '''bool KTextEditor.Search.SearchOptions.__ne__(KTextEditor.Search.SearchOptions f)'''
                return bool()
            def __eq__(self, f):
                '''bool KTextEditor.Search.SearchOptions.__eq__(KTextEditor.Search.SearchOptions f)'''
                return bool()
            def __invert__(self):
                '''KTextEditor.Search.SearchOptions KTextEditor.Search.SearchOptions.__invert__()'''
                return KTextEditor.Search.SearchOptions()
            def __and__(self, mask):
                '''KTextEditor.Search.SearchOptions KTextEditor.Search.SearchOptions.__and__(int mask)'''
                return KTextEditor.Search.SearchOptions()
            def __xor__(self, f):
                '''KTextEditor.Search.SearchOptions KTextEditor.Search.SearchOptions.__xor__(KTextEditor.Search.SearchOptions f)'''
                return KTextEditor.Search.SearchOptions()
            def __xor__(self, f):
                '''KTextEditor.Search.SearchOptions KTextEditor.Search.SearchOptions.__xor__(int f)'''
                return KTextEditor.Search.SearchOptions()
            def __or__(self, f):
                '''KTextEditor.Search.SearchOptions KTextEditor.Search.SearchOptions.__or__(KTextEditor.Search.SearchOptions f)'''
                return KTextEditor.Search.SearchOptions()
            def __or__(self, f):
                '''KTextEditor.Search.SearchOptions KTextEditor.Search.SearchOptions.__or__(int f)'''
                return KTextEditor.Search.SearchOptions()
            def __int__(self):
                '''int KTextEditor.Search.SearchOptions.__int__()'''
                return int()
            def __ixor__(self, f):
                '''KTextEditor.Search.SearchOptions KTextEditor.Search.SearchOptions.__ixor__(KTextEditor.Search.SearchOptions f)'''
                return KTextEditor.Search.SearchOptions()
            def __ior__(self, f):
                '''KTextEditor.Search.SearchOptions KTextEditor.Search.SearchOptions.__ior__(KTextEditor.Search.SearchOptions f)'''
                return KTextEditor.Search.SearchOptions()
            def __iand__(self, mask):
                '''KTextEditor.Search.SearchOptions KTextEditor.Search.SearchOptions.__iand__(int mask)'''
                return KTextEditor.Search.SearchOptions()
    class CodeCompletionInterface():
        """"""
        def __init__(self):
            '''void KTextEditor.CodeCompletionInterface.__init__()'''
        def __init__(self):
            '''KTextEditor.CodeCompletionInterface KTextEditor.CodeCompletionInterface.__init__()'''
            return KTextEditor.CodeCompletionInterface()
        def setAutomaticInvocationEnabled(self):
            '''abstract bool KTextEditor.CodeCompletionInterface.setAutomaticInvocationEnabled()'''
            return bool()
        def isAutomaticInvocationEnabled(self):
            '''abstract bool KTextEditor.CodeCompletionInterface.isAutomaticInvocationEnabled()'''
            return bool()
        def unregisterCompletionModel(self):
            '''abstract KTextEditor.CodeCompletionModel KTextEditor.CodeCompletionInterface.unregisterCompletionModel()'''
            return KTextEditor.CodeCompletionModel()
        def registerCompletionModel(self):
            '''abstract KTextEditor.CodeCompletionModel KTextEditor.CodeCompletionInterface.registerCompletionModel()'''
            return KTextEditor.CodeCompletionModel()
        def forceCompletion(self):
            '''abstract void KTextEditor.CodeCompletionInterface.forceCompletion()'''
        def abortCompletion(self):
            '''abstract void KTextEditor.CodeCompletionInterface.abortCompletion()'''
        def startCompletion(self):
            '''abstract KTextEditor.CodeCompletionModel KTextEditor.CodeCompletionInterface.startCompletion()'''
            return KTextEditor.CodeCompletionModel()
        def isCompletionActive(self):
            '''abstract bool KTextEditor.CodeCompletionInterface.isCompletionActive()'''
            return bool()
    class TemplateInterface():
        """"""
        def __init__(self):
            '''void KTextEditor.TemplateInterface.__init__()'''
        def insertTemplateTextImplementation(self):
            '''abstract dict-of-QString-QString KTextEditor.TemplateInterface.insertTemplateTextImplementation()'''
            return dict-of-QString-QString()
        def insertTemplateText(self):
            '''dict-of-QString-QString KTextEditor.TemplateInterface.insertTemplateText()'''
            return dict-of-QString-QString()
        def expandMacros(self):
            '''static QWidget KTextEditor.TemplateInterface.expandMacros()'''
            return QWidget()
    class TextHintInterface():
        """"""
        def __init__(self):
            '''void KTextEditor.TextHintInterface.__init__()'''
        def needTextHint(self):
            '''abstract QString KTextEditor.TextHintInterface.needTextHint()'''
            return QString()
        def disableTextHints(self):
            '''abstract void KTextEditor.TextHintInterface.disableTextHints()'''
        def enableTextHints(self):
            '''abstract int KTextEditor.TextHintInterface.enableTextHints()'''
            return int()
    class VariableInterface():
        """"""
        def __init__(self):
            '''void KTextEditor.VariableInterface.__init__()'''
        def variableChanged(self):
            '''abstract QString KTextEditor.VariableInterface.variableChanged()'''
            return QString()
        def variable(self):
            '''abstract QString KTextEditor.VariableInterface.variable()'''
            return QString()
    class CodeCompletionModel():
        """"""
        class HighlightMethods():
            """"""
            def __init__(self):
                '''KTextEditor.CodeCompletionModel.HighlightMethods KTextEditor.CodeCompletionModel.HighlightMethods.__init__()'''
                return KTextEditor.CodeCompletionModel.HighlightMethods()
            def __init__(self):
                '''int KTextEditor.CodeCompletionModel.HighlightMethods.__init__()'''
                return int()
            def __init__(self):
                '''void KTextEditor.CodeCompletionModel.HighlightMethods.__init__()'''
            def __bool__(self):
                '''int KTextEditor.CodeCompletionModel.HighlightMethods.__bool__()'''
                return int()
            def __ne__(self, f):
                '''bool KTextEditor.CodeCompletionModel.HighlightMethods.__ne__(KTextEditor.CodeCompletionModel.HighlightMethods f)'''
                return bool()
            def __eq__(self, f):
                '''bool KTextEditor.CodeCompletionModel.HighlightMethods.__eq__(KTextEditor.CodeCompletionModel.HighlightMethods f)'''
                return bool()
            def __invert__(self):
                '''KTextEditor.CodeCompletionModel.HighlightMethods KTextEditor.CodeCompletionModel.HighlightMethods.__invert__()'''
                return KTextEditor.CodeCompletionModel.HighlightMethods()
            def __and__(self, mask):
                '''KTextEditor.CodeCompletionModel.HighlightMethods KTextEditor.CodeCompletionModel.HighlightMethods.__and__(int mask)'''
                return KTextEditor.CodeCompletionModel.HighlightMethods()
            def __xor__(self, f):
                '''KTextEditor.CodeCompletionModel.HighlightMethods KTextEditor.CodeCompletionModel.HighlightMethods.__xor__(KTextEditor.CodeCompletionModel.HighlightMethods f)'''
                return KTextEditor.CodeCompletionModel.HighlightMethods()
            def __xor__(self, f):
                '''KTextEditor.CodeCompletionModel.HighlightMethods KTextEditor.CodeCompletionModel.HighlightMethods.__xor__(int f)'''
                return KTextEditor.CodeCompletionModel.HighlightMethods()
            def __or__(self, f):
                '''KTextEditor.CodeCompletionModel.HighlightMethods KTextEditor.CodeCompletionModel.HighlightMethods.__or__(KTextEditor.CodeCompletionModel.HighlightMethods f)'''
                return KTextEditor.CodeCompletionModel.HighlightMethods()
            def __or__(self, f):
                '''KTextEditor.CodeCompletionModel.HighlightMethods KTextEditor.CodeCompletionModel.HighlightMethods.__or__(int f)'''
                return KTextEditor.CodeCompletionModel.HighlightMethods()
            def __int__(self):
                '''int KTextEditor.CodeCompletionModel.HighlightMethods.__int__()'''
                return int()
            def __ixor__(self, f):
                '''KTextEditor.CodeCompletionModel.HighlightMethods KTextEditor.CodeCompletionModel.HighlightMethods.__ixor__(KTextEditor.CodeCompletionModel.HighlightMethods f)'''
                return KTextEditor.CodeCompletionModel.HighlightMethods()
            def __ior__(self, f):
                '''KTextEditor.CodeCompletionModel.HighlightMethods KTextEditor.CodeCompletionModel.HighlightMethods.__ior__(KTextEditor.CodeCompletionModel.HighlightMethods f)'''
                return KTextEditor.CodeCompletionModel.HighlightMethods()
            def __iand__(self, mask):
                '''KTextEditor.CodeCompletionModel.HighlightMethods KTextEditor.CodeCompletionModel.HighlightMethods.__iand__(int mask)'''
                return KTextEditor.CodeCompletionModel.HighlightMethods()
    class SmartCursor(KTextEditor.Cursor):
        """"""
        # Enum KTextEditor.SmartCursor.InsertBehavior
        StayOnInsert = 0
        MoveOnInsert = 0
    
        # Enum KTextEditor.SmartCursor.AdvanceMode
        ByCharacter = 0
        ByCursorPosition = 0
    
        def __init__(self):
            '''KTextEditor.SmartCursor.InsertBehavior KTextEditor.SmartCursor.__init__()'''
            return KTextEditor.SmartCursor.InsertBehavior()
        def setWatcher(self):
            '''abstract KTextEditor.SmartCursorWatcher KTextEditor.SmartCursor.setWatcher()'''
            return KTextEditor.SmartCursorWatcher()
        def watcher(self):
            '''abstract KTextEditor.SmartCursorWatcher KTextEditor.SmartCursor.watcher()'''
            return KTextEditor.SmartCursorWatcher()
        def deleteNotifier(self):
            '''abstract void KTextEditor.SmartCursor.deleteNotifier()'''
        def notifier(self):
            '''abstract KTextEditor.SmartCursorNotifier KTextEditor.SmartCursor.notifier()'''
            return KTextEditor.SmartCursorNotifier()
        def hasNotifier(self):
            '''abstract bool KTextEditor.SmartCursor.hasNotifier()'''
            return bool()
        def setInsertBehavior(self):
            '''KTextEditor.SmartCursor.InsertBehavior KTextEditor.SmartCursor.setInsertBehavior()'''
            return KTextEditor.SmartCursor.InsertBehavior()
        def insertBehavior(self):
            '''KTextEditor.SmartCursor.InsertBehavior KTextEditor.SmartCursor.insertBehavior()'''
            return KTextEditor.SmartCursor.InsertBehavior()
        def advance(self):
            '''KTextEditor.SmartCursor.AdvanceMode KTextEditor.SmartCursor.advance()'''
            return KTextEditor.SmartCursor.AdvanceMode()
        def insertText(self):
            '''bool KTextEditor.SmartCursor.insertText()'''
            return bool()
        def character(self):
            '''QChar KTextEditor.SmartCursor.character()'''
            return QChar()
        def isValid(self):
            '''bool KTextEditor.SmartCursor.isValid()'''
            return bool()
        def atEndOfDocument(self):
            '''bool KTextEditor.SmartCursor.atEndOfDocument()'''
            return bool()
        def atEndOfLine(self):
            '''bool KTextEditor.SmartCursor.atEndOfLine()'''
            return bool()
        def document(self):
            '''KTextEditor.Document KTextEditor.SmartCursor.document()'''
            return KTextEditor.Document()
        def smartRange(self):
            '''KTextEditor.SmartRange KTextEditor.SmartCursor.smartRange()'''
            return KTextEditor.SmartRange()
        def toSmartCursor(self):
            '''KTextEditor.SmartCursor KTextEditor.SmartCursor.toSmartCursor()'''
            return KTextEditor.SmartCursor()
        def isSmartCursor(self):
            '''bool KTextEditor.SmartCursor.isSmartCursor()'''
            return bool()
    class MarkInterface():
        """"""
        # Enum KTextEditor.MarkInterface.MarkChangeAction
        MarkAdded = 0
        MarkRemoved = 0
    
        # Enum KTextEditor.MarkInterface.MarkTypes
        markType01 = 0
        markType02 = 0
        markType03 = 0
        markType04 = 0
        markType05 = 0
        markType06 = 0
        markType07 = 0
        markType08 = 0
        markType09 = 0
        markType10 = 0
        markType11 = 0
        markType12 = 0
        markType13 = 0
        markType14 = 0
        markType15 = 0
        markType16 = 0
        markType17 = 0
        markType18 = 0
        markType19 = 0
        markType20 = 0
        markType21 = 0
        markType22 = 0
        markType23 = 0
        markType24 = 0
        markType25 = 0
        markType26 = 0
        markType27 = 0
        markType28 = 0
        markType29 = 0
        markType30 = 0
        markType31 = 0
        markType32 = 0
        Bookmark = 0
        BreakpointActive = 0
        BreakpointReached = 0
        BreakpointDisabled = 0
        Execution = 0
        Warning = 0
        Error = 0
    
        def __init__(self):
            '''void KTextEditor.MarkInterface.__init__()'''
        def markChanged(self):
            '''abstract KTextEditor.MarkInterface.MarkChangeAction KTextEditor.MarkInterface.markChanged()'''
            return KTextEditor.MarkInterface.MarkChangeAction()
        def editableMarks(self):
            '''abstract int KTextEditor.MarkInterface.editableMarks()'''
            return int()
        def setEditableMarks(self):
            '''abstract int KTextEditor.MarkInterface.setEditableMarks()'''
            return int()
        def markDescription(self):
            '''abstract KTextEditor.MarkInterface.MarkTypes KTextEditor.MarkInterface.markDescription()'''
            return KTextEditor.MarkInterface.MarkTypes()
        def setMarkDescription(self):
            '''abstract QString KTextEditor.MarkInterface.setMarkDescription()'''
            return QString()
        def markPixmap(self):
            '''abstract KTextEditor.MarkInterface.MarkTypes KTextEditor.MarkInterface.markPixmap()'''
            return KTextEditor.MarkInterface.MarkTypes()
        def setMarkPixmap(self):
            '''abstract QPixmap KTextEditor.MarkInterface.setMarkPixmap()'''
            return QPixmap()
        def marksChanged(self):
            '''abstract KTextEditor.Document KTextEditor.MarkInterface.marksChanged()'''
            return KTextEditor.Document()
        def reservedMarkersCount(self):
            '''static int KTextEditor.MarkInterface.reservedMarkersCount()'''
            return int()
        def clearMarks(self):
            '''abstract void KTextEditor.MarkInterface.clearMarks()'''
        def marks(self):
            '''abstract unknown-type KTextEditor.MarkInterface.marks()'''
            return unknown-type()
        def removeMark(self):
            '''abstract int KTextEditor.MarkInterface.removeMark()'''
            return int()
        def addMark(self):
            '''abstract int KTextEditor.MarkInterface.addMark()'''
            return int()
        def clearMark(self):
            '''abstract int KTextEditor.MarkInterface.clearMark()'''
            return int()
        def setMark(self):
            '''abstract int KTextEditor.MarkInterface.setMark()'''
            return int()
        def mark(self):
            '''abstract int KTextEditor.MarkInterface.mark()'''
            return int()
    class Search():
        """"""
        # Enum KTextEditor.Search.SearchOptionsEnum
        Default = 0
        Regex = 0
        CaseInsensitive = 0
        Backwards = 0
        BlockInputRange = 0
        EscapeSequences = 0
        WholeWords = 0
        DotMatchesNewline = 0
    
    class EditorChooser(QWidget):
        """"""
        def __init__(self):
            '''QWidget KTextEditor.EditorChooser.__init__()'''
            return QWidget()
        changed = pyqtSignal() # void changed() - signal
        def editor(self):
            '''static bool KTextEditor.EditorChooser.editor()'''
            return bool()
        def writeAppSetting(self):
            '''QString KTextEditor.EditorChooser.writeAppSetting()'''
            return QString()
        def readAppSetting(self):
            '''QString KTextEditor.EditorChooser.readAppSetting()'''
            return QString()
    class SessionConfigInterface():
        """"""
        def __init__(self):
            '''void KTextEditor.SessionConfigInterface.__init__()'''
        def writeSessionConfig(self):
            '''abstract KConfigGroup KTextEditor.SessionConfigInterface.writeSessionConfig()'''
            return KConfigGroup()
        def readSessionConfig(self):
            '''abstract KConfigGroup KTextEditor.SessionConfigInterface.readSessionConfig()'''
            return KConfigGroup()
    class Cursor():
        """"""
        def __init__(self):
            '''void KTextEditor.Cursor.__init__()'''
        def __init__(self):
            '''int KTextEditor.Cursor.__init__()'''
            return int()
        def __init__(self):
            '''KTextEditor.Cursor KTextEditor.Cursor.__init__()'''
            return KTextEditor.Cursor()
        def cursorChangedDirectly(self):
            '''KTextEditor.Cursor KTextEditor.Cursor.cursorChangedDirectly()'''
            return KTextEditor.Cursor()
        def setRange(self):
            '''KTextEditor.Range KTextEditor.Cursor.setRange()'''
            return KTextEditor.Range()
        def range(self):
            '''KTextEditor.Range KTextEditor.Cursor.range()'''
            return KTextEditor.Range()
        def position(self):
            '''int KTextEditor.Cursor.position()'''
            return int()
        def atStartOfDocument(self):
            '''bool KTextEditor.Cursor.atStartOfDocument()'''
            return bool()
        def atStartOfLine(self):
            '''bool KTextEditor.Cursor.atStartOfLine()'''
            return bool()
        def setColumn(self):
            '''int KTextEditor.Cursor.setColumn()'''
            return int()
        def column(self):
            '''int KTextEditor.Cursor.column()'''
            return int()
        def setLine(self):
            '''int KTextEditor.Cursor.setLine()'''
            return int()
        def line(self):
            '''int KTextEditor.Cursor.line()'''
            return int()
        def setPosition(self):
            '''KTextEditor.Cursor KTextEditor.Cursor.setPosition()'''
            return KTextEditor.Cursor()
        def setPosition(self):
            '''int KTextEditor.Cursor.setPosition()'''
            return int()
        def start(self):
            '''static KTextEditor.Cursor KTextEditor.Cursor.start()'''
            return KTextEditor.Cursor()
        def invalid(self):
            '''static KTextEditor.Cursor KTextEditor.Cursor.invalid()'''
            return KTextEditor.Cursor()
        def toSmartCursor(self):
            '''KTextEditor.SmartCursor KTextEditor.Cursor.toSmartCursor()'''
            return KTextEditor.SmartCursor()
        def isSmartCursor(self):
            '''bool KTextEditor.Cursor.isSmartCursor()'''
            return bool()
        def isValid(self):
            '''bool KTextEditor.Cursor.isValid()'''
            return bool()
    class CodeCompletionModel():
        """"""
        class CompletionProperties():
            """"""
            def __init__(self):
                '''KTextEditor.CodeCompletionModel.CompletionProperties KTextEditor.CodeCompletionModel.CompletionProperties.__init__()'''
                return KTextEditor.CodeCompletionModel.CompletionProperties()
            def __init__(self):
                '''int KTextEditor.CodeCompletionModel.CompletionProperties.__init__()'''
                return int()
            def __init__(self):
                '''void KTextEditor.CodeCompletionModel.CompletionProperties.__init__()'''
            def __bool__(self):
                '''int KTextEditor.CodeCompletionModel.CompletionProperties.__bool__()'''
                return int()
            def __ne__(self, f):
                '''bool KTextEditor.CodeCompletionModel.CompletionProperties.__ne__(KTextEditor.CodeCompletionModel.CompletionProperties f)'''
                return bool()
            def __eq__(self, f):
                '''bool KTextEditor.CodeCompletionModel.CompletionProperties.__eq__(KTextEditor.CodeCompletionModel.CompletionProperties f)'''
                return bool()
            def __invert__(self):
                '''KTextEditor.CodeCompletionModel.CompletionProperties KTextEditor.CodeCompletionModel.CompletionProperties.__invert__()'''
                return KTextEditor.CodeCompletionModel.CompletionProperties()
            def __and__(self, mask):
                '''KTextEditor.CodeCompletionModel.CompletionProperties KTextEditor.CodeCompletionModel.CompletionProperties.__and__(int mask)'''
                return KTextEditor.CodeCompletionModel.CompletionProperties()
            def __xor__(self, f):
                '''KTextEditor.CodeCompletionModel.CompletionProperties KTextEditor.CodeCompletionModel.CompletionProperties.__xor__(KTextEditor.CodeCompletionModel.CompletionProperties f)'''
                return KTextEditor.CodeCompletionModel.CompletionProperties()
            def __xor__(self, f):
                '''KTextEditor.CodeCompletionModel.CompletionProperties KTextEditor.CodeCompletionModel.CompletionProperties.__xor__(int f)'''
                return KTextEditor.CodeCompletionModel.CompletionProperties()
            def __or__(self, f):
                '''KTextEditor.CodeCompletionModel.CompletionProperties KTextEditor.CodeCompletionModel.CompletionProperties.__or__(KTextEditor.CodeCompletionModel.CompletionProperties f)'''
                return KTextEditor.CodeCompletionModel.CompletionProperties()
            def __or__(self, f):
                '''KTextEditor.CodeCompletionModel.CompletionProperties KTextEditor.CodeCompletionModel.CompletionProperties.__or__(int f)'''
                return KTextEditor.CodeCompletionModel.CompletionProperties()
            def __int__(self):
                '''int KTextEditor.CodeCompletionModel.CompletionProperties.__int__()'''
                return int()
            def __ixor__(self, f):
                '''KTextEditor.CodeCompletionModel.CompletionProperties KTextEditor.CodeCompletionModel.CompletionProperties.__ixor__(KTextEditor.CodeCompletionModel.CompletionProperties f)'''
                return KTextEditor.CodeCompletionModel.CompletionProperties()
            def __ior__(self, f):
                '''KTextEditor.CodeCompletionModel.CompletionProperties KTextEditor.CodeCompletionModel.CompletionProperties.__ior__(KTextEditor.CodeCompletionModel.CompletionProperties f)'''
                return KTextEditor.CodeCompletionModel.CompletionProperties()
            def __iand__(self, mask):
                '''KTextEditor.CodeCompletionModel.CompletionProperties KTextEditor.CodeCompletionModel.CompletionProperties.__iand__(int mask)'''
                return KTextEditor.CodeCompletionModel.CompletionProperties()
    class SmartRange(KTextEditor.Range):
        """"""
        # Enum KTextEditor.SmartRange.InsertBehavior
        DoNotExpand = 0
        ExpandLeft = 0
        ExpandRight = 0
    
        def __init__(self):
            '''KTextEditor.SmartRange.InsertBehaviors KTextEditor.SmartRange.__init__()'''
            return KTextEditor.SmartRange.InsertBehaviors()
        def createNotifier(self):
            '''abstract KTextEditor.SmartRangeNotifier KTextEditor.SmartRange.createNotifier()'''
            return KTextEditor.SmartRangeNotifier()
        def checkFeedback(self):
            '''void KTextEditor.SmartRange.checkFeedback()'''
        def rangeChanged(self):
            '''KTextEditor.Range KTextEditor.SmartRange.rangeChanged()'''
            return KTextEditor.Range()
        def removeWatcher(self):
            '''KTextEditor.SmartRangeWatcher KTextEditor.SmartRange.removeWatcher()'''
            return KTextEditor.SmartRangeWatcher()
        def addWatcher(self):
            '''KTextEditor.SmartRangeWatcher KTextEditor.SmartRange.addWatcher()'''
            return KTextEditor.SmartRangeWatcher()
        def watchers(self):
            '''list-of-KTextEditor.SmartRangeWatcher KTextEditor.SmartRange.watchers()'''
            return [KTextEditor.SmartRangeWatcher()]
        def deletePrimaryNotifier(self):
            '''void KTextEditor.SmartRange.deletePrimaryNotifier()'''
        def removeNotifier(self):
            '''KTextEditor.SmartRangeNotifier KTextEditor.SmartRange.removeNotifier()'''
            return KTextEditor.SmartRangeNotifier()
        def addNotifier(self):
            '''KTextEditor.SmartRangeNotifier KTextEditor.SmartRange.addNotifier()'''
            return KTextEditor.SmartRangeNotifier()
        def notifiers(self):
            '''list-of-KTextEditor.SmartRangeNotifier KTextEditor.SmartRange.notifiers()'''
            return [KTextEditor.SmartRangeNotifier()]
        def primaryNotifier(self):
            '''KTextEditor.SmartRangeNotifier KTextEditor.SmartRange.primaryNotifier()'''
            return KTextEditor.SmartRangeNotifier()
        def clearAssociatedActions(self):
            '''void KTextEditor.SmartRange.clearAssociatedActions()'''
        def associatedActions(self):
            '''list-of-KAction KTextEditor.SmartRange.associatedActions()'''
            return [KAction()]
        def dissociateAction(self):
            '''KAction KTextEditor.SmartRange.dissociateAction()'''
            return KAction()
        def associateAction(self):
            '''KAction KTextEditor.SmartRange.associateAction()'''
            return KAction()
        def setAttribute(self):
            '''unknown-type KTextEditor.SmartRange.setAttribute()'''
            return unknown-type()
        def attribute(self):
            '''unknown-type KTextEditor.SmartRange.attribute()'''
            return unknown-type()
        def deepestRangeContaining(self):
            '''unknown-type KTextEditor.SmartRange.deepestRangeContaining()'''
            return unknown-type()
        def firstRangeContaining(self):
            '''KTextEditor.Cursor KTextEditor.SmartRange.firstRangeContaining()'''
            return KTextEditor.Cursor()
        def mostSpecificRange(self):
            '''KTextEditor.Range KTextEditor.SmartRange.mostSpecificRange()'''
            return KTextEditor.Range()
        def childAfter(self):
            '''KTextEditor.SmartRange KTextEditor.SmartRange.childAfter()'''
            return KTextEditor.SmartRange()
        def childBefore(self):
            '''KTextEditor.SmartRange KTextEditor.SmartRange.childBefore()'''
            return KTextEditor.SmartRange()
        def clearAndDeleteChildRanges(self):
            '''void KTextEditor.SmartRange.clearAndDeleteChildRanges()'''
        def deleteChildRanges(self):
            '''void KTextEditor.SmartRange.deleteChildRanges()'''
        def clearChildRanges(self):
            '''void KTextEditor.SmartRange.clearChildRanges()'''
        def childRanges(self):
            '''list-of-KTextEditor.SmartRange KTextEditor.SmartRange.childRanges()'''
            return [KTextEditor.SmartRange()]
        def topParentRange(self):
            '''KTextEditor.SmartRange KTextEditor.SmartRange.topParentRange()'''
            return KTextEditor.SmartRange()
        def depth(self):
            '''int KTextEditor.SmartRange.depth()'''
            return int()
        def hasParent(self):
            '''KTextEditor.SmartRange KTextEditor.SmartRange.hasParent()'''
            return KTextEditor.SmartRange()
        def setParentRange(self):
            '''KTextEditor.SmartRange KTextEditor.SmartRange.setParentRange()'''
            return KTextEditor.SmartRange()
        def parentRange(self):
            '''KTextEditor.SmartRange KTextEditor.SmartRange.parentRange()'''
            return KTextEditor.SmartRange()
        def setInsertBehavior(self):
            '''KTextEditor.SmartRange.InsertBehaviors KTextEditor.SmartRange.setInsertBehavior()'''
            return KTextEditor.SmartRange.InsertBehaviors()
        def insertBehavior(self):
            '''KTextEditor.SmartRange.InsertBehaviors KTextEditor.SmartRange.insertBehavior()'''
            return KTextEditor.SmartRange.InsertBehaviors()
        def removeText(self):
            '''bool KTextEditor.SmartRange.removeText()'''
            return bool()
        def replaceText(self):
            '''bool KTextEditor.SmartRange.replaceText()'''
            return bool()
        def text(self):
            '''bool KTextEditor.SmartRange.text()'''
            return bool()
        def document(self):
            '''KTextEditor.Document KTextEditor.SmartRange.document()'''
            return KTextEditor.Document()
        def expandToRange(self):
            '''KTextEditor.Range KTextEditor.SmartRange.expandToRange()'''
            return KTextEditor.Range()
        def confineToRange(self):
            '''KTextEditor.Range KTextEditor.SmartRange.confineToRange()'''
            return KTextEditor.Range()
        def smartEnd(self):
            '''KTextEditor.SmartCursor KTextEditor.SmartRange.smartEnd()'''
            return KTextEditor.SmartCursor()
        def smartStart(self):
            '''KTextEditor.SmartCursor KTextEditor.SmartRange.smartStart()'''
            return KTextEditor.SmartCursor()
        def setRange(self):
            '''KTextEditor.Range KTextEditor.SmartRange.setRange()'''
            return KTextEditor.Range()
        def toSmartRange(self):
            '''KTextEditor.SmartRange KTextEditor.SmartRange.toSmartRange()'''
            return KTextEditor.SmartRange()
        def isSmartRange(self):
            '''bool KTextEditor.SmartRange.isSmartRange()'''
            return bool()
    class ContainerInterface():
        """"""
        def __init__(self):
            '''void KTextEditor.ContainerInterface.__init__()'''
        def __init__(self):
            '''KTextEditor.ContainerInterface KTextEditor.ContainerInterface.__init__()'''
            return KTextEditor.ContainerInterface()
        def container(self):
            '''abstract QObject KTextEditor.ContainerInterface.container()'''
            return QObject()
        def setContainer(self):
            '''abstract QObject KTextEditor.ContainerInterface.setContainer()'''
            return QObject()
    class ModificationInterface():
        """"""
        # Enum KTextEditor.ModificationInterface.ModifiedOnDiskReason
        OnDiskUnmodified = 0
        OnDiskModified = 0
        OnDiskCreated = 0
        OnDiskDeleted = 0
    
        def __init__(self):
            '''void KTextEditor.ModificationInterface.__init__()'''
        def modifiedOnDisk(self):
            '''abstract KTextEditor.ModificationInterface.ModifiedOnDiskReason KTextEditor.ModificationInterface.modifiedOnDisk()'''
            return KTextEditor.ModificationInterface.ModifiedOnDiskReason()
        def slotModifiedOnDisk(self):
            '''abstract KTextEditor.View KTextEditor.ModificationInterface.slotModifiedOnDisk()'''
            return KTextEditor.View()
        def setModifiedOnDiskWarning(self):
            '''abstract bool KTextEditor.ModificationInterface.setModifiedOnDiskWarning()'''
            return bool()
        def setModifiedOnDisk(self):
            '''abstract KTextEditor.ModificationInterface.ModifiedOnDiskReason KTextEditor.ModificationInterface.setModifiedOnDisk()'''
            return KTextEditor.ModificationInterface.ModifiedOnDiskReason()
    class Range():
        """"""
        def __init__(self):
            '''void KTextEditor.Range.__init__()'''
        def __init__(self):
            '''KTextEditor.Cursor KTextEditor.Range.__init__()'''
            return KTextEditor.Cursor()
        def __init__(self):
            '''int KTextEditor.Range.__init__()'''
            return int()
        def __init__(self):
            '''int KTextEditor.Range.__init__()'''
            return int()
        def __init__(self):
            '''int KTextEditor.Range.__init__()'''
            return int()
        def __init__(self):
            '''KTextEditor.Range KTextEditor.Range.__init__()'''
            return KTextEditor.Range()
        def __init__(self):
            '''KTextEditor.Cursor KTextEditor.Range.__init__()'''
            return KTextEditor.Cursor()
        def rangeChanged(self):
            '''KTextEditor.Range KTextEditor.Range.rangeChanged()'''
            return KTextEditor.Range()
        def encompass(self):
            '''KTextEditor.Range KTextEditor.Range.encompass()'''
            return KTextEditor.Range()
        def intersect(self):
            '''KTextEditor.Range KTextEditor.Range.intersect()'''
            return KTextEditor.Range()
        def boundaryOnLine(self):
            '''int KTextEditor.Range.boundaryOnLine()'''
            return int()
        def boundaryAtCursor(self):
            '''KTextEditor.Cursor KTextEditor.Range.boundaryAtCursor()'''
            return KTextEditor.Cursor()
        def positionRelativeToLine(self):
            '''int KTextEditor.Range.positionRelativeToLine()'''
            return int()
        def positionRelativeToCursor(self):
            '''KTextEditor.Cursor KTextEditor.Range.positionRelativeToCursor()'''
            return KTextEditor.Cursor()
        def overlapsColumn(self):
            '''int KTextEditor.Range.overlapsColumn()'''
            return int()
        def overlapsLine(self):
            '''int KTextEditor.Range.overlapsLine()'''
            return int()
        def overlaps(self):
            '''KTextEditor.Range KTextEditor.Range.overlaps()'''
            return KTextEditor.Range()
        def containsLine(self):
            '''int KTextEditor.Range.containsLine()'''
            return int()
        def contains(self):
            '''KTextEditor.Range KTextEditor.Range.contains()'''
            return KTextEditor.Range()
        def contains(self):
            '''KTextEditor.Cursor KTextEditor.Range.contains()'''
            return KTextEditor.Cursor()
        def isEmpty(self):
            '''bool KTextEditor.Range.isEmpty()'''
            return bool()
        def columnWidth(self):
            '''int KTextEditor.Range.columnWidth()'''
            return int()
        def numberOfLines(self):
            '''int KTextEditor.Range.numberOfLines()'''
            return int()
        def onSingleLine(self):
            '''bool KTextEditor.Range.onSingleLine()'''
            return bool()
        def confineToRange(self):
            '''KTextEditor.Range KTextEditor.Range.confineToRange()'''
            return KTextEditor.Range()
        def expandToRange(self):
            '''KTextEditor.Range KTextEditor.Range.expandToRange()'''
            return KTextEditor.Range()
        def setRange(self):
            '''KTextEditor.Range KTextEditor.Range.setRange()'''
            return KTextEditor.Range()
        def setRange(self):
            '''KTextEditor.Cursor KTextEditor.Range.setRange()'''
            return KTextEditor.Cursor()
        def setBothColumns(self):
            '''int KTextEditor.Range.setBothColumns()'''
            return int()
        def setBothLines(self):
            '''int KTextEditor.Range.setBothLines()'''
            return int()
        def end(self):
            '''KTextEditor.Cursor KTextEditor.Range.end()'''
            return KTextEditor.Cursor()
        def start(self):
            '''KTextEditor.Cursor KTextEditor.Range.start()'''
            return KTextEditor.Cursor()
        def toSmartRange(self):
            '''KTextEditor.SmartRange KTextEditor.Range.toSmartRange()'''
            return KTextEditor.SmartRange()
        def isSmartRange(self):
            '''bool KTextEditor.Range.isSmartRange()'''
            return bool()
        def invalid(self):
            '''static KTextEditor.Range KTextEditor.Range.invalid()'''
            return KTextEditor.Range()
        def isValid(self):
            '''bool KTextEditor.Range.isValid()'''
            return bool()
    class SmartCursorNotifier(QObject):
        """"""
        def __init__(self):
            '''void KTextEditor.SmartCursorNotifier.__init__()'''
        deleted = pyqtSignal() # void deleted(KTextEditor::SmartCursor *) - signal
        characterInserted = pyqtSignal() # void characterInserted(KTextEditor::SmartCursor *,bool) - signal
        characterDeleted = pyqtSignal() # void characterDeleted(KTextEditor::SmartCursor *,bool) - signal
        positionDeleted = pyqtSignal() # void positionDeleted(KTextEditor::SmartCursor *) - signal
        positionChanged = pyqtSignal() # void positionChanged(KTextEditor::SmartCursor *) - signal
        def setWantsDirectChanges(self):
            '''bool KTextEditor.SmartCursorNotifier.setWantsDirectChanges()'''
            return bool()
        def wantsDirectChanges(self):
            '''bool KTextEditor.SmartCursorNotifier.wantsDirectChanges()'''
            return bool()
    class Editor(QObject):
        """"""
        def __init__(self):
            '''QObject KTextEditor.Editor.__init__()'''
            return QObject()
        documentCreated = pyqtSignal() # void documentCreated(KTextEditor::Editor *,KTextEditor::Document *) - signal
        def configPageIcon(self):
            '''abstract int KTextEditor.Editor.configPageIcon()'''
            return int()
        def configPageFullName(self):
            '''abstract int KTextEditor.Editor.configPageFullName()'''
            return int()
        def configPageName(self):
            '''abstract int KTextEditor.Editor.configPageName()'''
            return int()
        def configPage(self):
            '''abstract QWidget KTextEditor.Editor.configPage()'''
            return QWidget()
        def configPages(self):
            '''abstract int KTextEditor.Editor.configPages()'''
            return int()
        def configDialog(self):
            '''abstract QWidget KTextEditor.Editor.configDialog()'''
            return QWidget()
        def configDialogSupported(self):
            '''abstract bool KTextEditor.Editor.configDialogSupported()'''
            return bool()
        def writeConfig(self):
            '''abstract KConfig KTextEditor.Editor.writeConfig()'''
            return KConfig()
        def readConfig(self):
            '''abstract KConfig KTextEditor.Editor.readConfig()'''
            return KConfig()
        def aboutData(self):
            '''abstract KAboutData KTextEditor.Editor.aboutData()'''
            return KAboutData()
        def documents(self):
            '''abstract list-of-KTextEditor.Document KTextEditor.Editor.documents()'''
            return [KTextEditor.Document()]
        def createDocument(self):
            '''abstract QObject KTextEditor.Editor.createDocument()'''
            return QObject()
    class SmartRangeNotifier(QObject):
        """"""
        def __init__(self):
            '''void KTextEditor.SmartRangeNotifier.__init__()'''
        rangeAttributeChanged = pyqtSignal() # void rangeAttributeChanged(KTextEditor::SmartRange *,KTextEditor::Attribute::Ptr,KTextEditor::Attribute::Ptr) - signal
        childRangeRemoved = pyqtSignal() # void childRangeRemoved(KTextEditor::SmartRange *,KTextEditor::SmartRange *) - signal
        childRangeInserted = pyqtSignal() # void childRangeInserted(KTextEditor::SmartRange *,KTextEditor::SmartRange *) - signal
        parentRangeChanged = pyqtSignal() # void parentRangeChanged(KTextEditor::SmartRange *,KTextEditor::SmartRange *,KTextEditor::SmartRange *) - signal
        rangeDeleted = pyqtSignal() # void rangeDeleted(KTextEditor::SmartRange *) - signal
        rangeEliminated = pyqtSignal() # void rangeEliminated(KTextEditor::SmartRange *) - signal
        caretExitedRange = pyqtSignal() # void caretExitedRange(KTextEditor::SmartRange *,KTextEditor::View *) - signal
        caretEnteredRange = pyqtSignal() # void caretEnteredRange(KTextEditor::SmartRange *,KTextEditor::View *) - signal
        mouseExitedRange = pyqtSignal() # void mouseExitedRange(KTextEditor::SmartRange *,KTextEditor::View *) - signal
        mouseEnteredRange = pyqtSignal() # void mouseEnteredRange(KTextEditor::SmartRange *,KTextEditor::View *) - signal
        rangeContentsChanged = pyqtSignal() # void rangeContentsChanged(KTextEditor::SmartRange *) - signal
        rangeContentsChanged = pyqtSignal() # void rangeContentsChanged(KTextEditor::SmartRange *,KTextEditor::SmartRange *) - signal
        rangePositionChanged = pyqtSignal() # void rangePositionChanged(KTextEditor::SmartRange *) - signal
        def setWantsDirectChanges(self):
            '''bool KTextEditor.SmartRangeNotifier.setWantsDirectChanges()'''
            return bool()
        def wantsDirectChanges(self):
            '''bool KTextEditor.SmartRangeNotifier.wantsDirectChanges()'''
            return bool()


