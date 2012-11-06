class pyqtSignal():
 def connect(self, targetSignal): pass
 def emit(self, *args): pass
from QtCore import *

class Plasma():
    """"""
    # Enum Plasma.TrustLevel
    InvalidCredentials = 0
    UnknownCredentials = 0
    ValidCredentials = 0
    TrustedCredentials = 0
    UltimateCredentials = 0

    # Enum Plasma.AnnouncementMethod
    NoAnnouncement = 0
    ZeroconfAnnouncement = 0

    # Enum Plasma.ItemStatus
    UnknownStatus = 0
    PassiveStatus = 0
    ActiveStatus = 0
    NeedsAttentionStatus = 0
    AcceptingInputStatus = 0

    # Enum Plasma.MessageButton
    ButtonNone = 0
    ButtonOk = 0
    ButtonYes = 0
    ButtonNo = 0
    ButtonCancel = 0

    # Enum Plasma.MarginEdge
    TopMargin = 0
    BottomMargin = 0
    LeftMargin = 0
    RightMargin = 0

    # Enum Plasma.ComponentType
    AppletComponent = 0
    DataEngineComponent = 0
    RunnerComponent = 0
    AnimatorComponent = 0
    ContainmentComponent = 0
    WallpaperComponent = 0
    GenericComponent = 0

    # Enum Plasma.AspectRatioMode
    InvalidAspectRatioMode = 0
    IgnoreAspectRatio = 0
    KeepAspectRatio = 0
    Square = 0
    ConstrainedSquare = 0
    FixedSize = 0

    # Enum Plasma.ImmutabilityType
    Mutable = 0
    UserImmutable = 0
    SystemImmutable = 0

    # Enum Plasma.ItemTypes
    AppletType = 0
    LineEditType = 0

    # Enum Plasma.IntervalAlignment
    NoAlignment = 0
    AlignToMinute = 0
    AlignToHour = 0

    # Enum Plasma.ZoomLevel
    DesktopZoom = 0
    GroupZoom = 0
    OverviewZoom = 0

    # Enum Plasma.FlipDirection
    NoFlip = 0
    HorizontalFlip = 0
    VerticalFlip = 0

    # Enum Plasma.PopupPlacement
    FloatingPopup = 0
    TopPosedLeftAlignedPopup = 0
    TopPosedRightAlignedPopup = 0
    LeftPosedTopAlignedPopup = 0
    LeftPosedBottomAlignedPopup = 0
    BottomPosedLeftAlignedPopup = 0
    BottomPosedRightAlignedPopup = 0
    RightPosedTopAlignedPopup = 0
    RightPosedBottomAlignedPopup = 0

    # Enum Plasma.Position
    LeftPositioned = 0
    RightPositioned = 0
    TopPositioned = 0
    BottomPositioned = 0
    CenterPositioned = 0

    # Enum Plasma.Location
    Floating = 0
    Desktop = 0
    FullScreen = 0
    TopEdge = 0
    BottomEdge = 0
    LeftEdge = 0
    RightEdge = 0

    # Enum Plasma.ZoomDirection
    ZoomIn = 0
    ZoomOut = 0

    # Enum Plasma.Direction
    Down = 0
    Up = 0
    Left = 0
    Right = 0

    # Enum Plasma.FormFactor
    Planar = 0
    MediaCenter = 0
    Horizontal = 0
    Vertical = 0

    # Enum Plasma.Constraint
    NoConstraint = 0
    FormFactorConstraint = 0
    LocationConstraint = 0
    ScreenConstraint = 0
    SizeConstraint = 0
    ImmutableConstraint = 0
    StartupCompletedConstraint = 0
    ContextConstraint = 0
    PopupConstraint = 0
    AllConstraints = 0

    def isPluginVersionCompatible(self, version):
        '''static bool Plasma.isPluginVersionCompatible(int version)'''
        return bool()
    def versionString(self):
        '''static str Plasma.versionString()'''
        return str()
    def versionRelease(self):
        '''static int Plasma.versionRelease()'''
        return int()
    def versionMinor(self):
        '''static int Plasma.versionMinor()'''
        return int()
    def versionMajor(self):
        '''static int Plasma.versionMajor()'''
        return int()
    def version(self):
        '''static int Plasma.version()'''
        return int()
    def packageStructure(self, language, type):
        '''static unknown-type Plasma.packageStructure(QString language, Plasma.ComponentType type)'''
        return unknown-type()
    def loadScriptEngine(self, language, applet):
        '''static Plasma.AppletScript Plasma.loadScriptEngine(QString language, Plasma.Applet applet)'''
        return Plasma.AppletScript()
    def loadScriptEngine(self, language, dataEngine):
        '''static Plasma.DataEngineScript Plasma.loadScriptEngine(QString language, Plasma.DataEngine dataEngine)'''
        return Plasma.DataEngineScript()
    def loadScriptEngine(self, language, runner):
        '''static Plasma.RunnerScript Plasma.loadScriptEngine(QString language, Plasma.AbstractRunner runner)'''
        return Plasma.RunnerScript()
    def loadScriptEngine(self, language, wallpaper):
        '''static Plasma.WallpaperScript Plasma.loadScriptEngine(QString language, Plasma.Wallpaper wallpaper)'''
        return Plasma.WallpaperScript()
    def knownLanguages(self, types):
        '''static QStringList Plasma.knownLanguages(Plasma.ComponentTypes types)'''
        return QStringList()
    def actionsFromMenu(self, menu, prefix = QString(), parent = None):
        '''static list-of-QAction Plasma.actionsFromMenu(QMenu menu, QString prefix = QString(), QObject parent = None)'''
        return [QAction()]
    def viewFor(self, item):
        '''static QGraphicsView Plasma.viewFor(QGraphicsItem item)'''
        return QGraphicsView()
    def locationToInverseDirection(self, location):
        '''static Plasma.Direction Plasma.locationToInverseDirection(Plasma.Location location)'''
        return Plasma.Direction()
    def locationToDirection(self, location):
        '''static Plasma.Direction Plasma.locationToDirection(Plasma.Location location)'''
        return Plasma.Direction()
    def scalingFactor(self, level):
        '''static float Plasma.scalingFactor(Plasma.ZoomLevel level)'''
        return float()
    class PopupApplet(Plasma.Applet):
        """"""
        def __init__(self, parent, args):
            '''void Plasma.PopupApplet.__init__(QObject parent, list-of-QVariant args)'''
        def timerEvent(self, event):
            '''void Plasma.PopupApplet.timerEvent(QTimerEvent event)'''
        def isIconified(self):
            '''bool Plasma.PopupApplet.isIconified()'''
            return bool()
        def popupAlignment(self):
            '''Qt.AlignmentFlag Plasma.PopupApplet.popupAlignment()'''
            return Qt.AlignmentFlag()
        def setPopupAlignment(self, alignment):
            '''void Plasma.PopupApplet.setPopupAlignment(Qt.AlignmentFlag alignment)'''
        def sizeHint(self, which, constraint = QSizeF()):
            '''QSizeF Plasma.PopupApplet.sizeHint(Qt.SizeHint which, QSizeF constraint = QSizeF())'''
            return QSizeF()
        def setGraphicsWidget(self, widget):
            '''void Plasma.PopupApplet.setGraphicsWidget(QGraphicsWidget widget)'''
        def setWidget(self, widget):
            '''void Plasma.PopupApplet.setWidget(QWidget widget)'''
        def dropEvent(self, event):
            '''void Plasma.PopupApplet.dropEvent(QGraphicsSceneDragDropEvent event)'''
        def dragLeaveEvent(self, event):
            '''void Plasma.PopupApplet.dragLeaveEvent(QGraphicsSceneDragDropEvent event)'''
        def dragEnterEvent(self, event):
            '''void Plasma.PopupApplet.dragEnterEvent(QGraphicsSceneDragDropEvent event)'''
        def eventFilter(self, watched, event):
            '''bool Plasma.PopupApplet.eventFilter(QObject watched, QEvent event)'''
            return bool()
        def mouseReleaseEvent(self, event):
            '''void Plasma.PopupApplet.mouseReleaseEvent(QGraphicsSceneMouseEvent event)'''
        def mousePressEvent(self, event):
            '''void Plasma.PopupApplet.mousePressEvent(QGraphicsSceneMouseEvent event)'''
        def popupEvent(self, show):
            '''void Plasma.PopupApplet.popupEvent(bool show)'''
        def togglePopup(self):
            '''void Plasma.PopupApplet.togglePopup()'''
        def showPopup(self, displayTime = 0):
            '''void Plasma.PopupApplet.showPopup(int displayTime = 0)'''
        def hidePopup(self):
            '''void Plasma.PopupApplet.hidePopup()'''
        def isPopupShowing(self):
            '''bool Plasma.PopupApplet.isPopupShowing()'''
            return bool()
        def isPassivePopup(self):
            '''bool Plasma.PopupApplet.isPassivePopup()'''
            return bool()
        def setPassivePopup(self, passive):
            '''void Plasma.PopupApplet.setPassivePopup(bool passive)'''
        def popupPlacement(self):
            '''Plasma.PopupPlacement Plasma.PopupApplet.popupPlacement()'''
            return Plasma.PopupPlacement()
        def graphicsWidget(self):
            '''QGraphicsWidget Plasma.PopupApplet.graphicsWidget()'''
            return QGraphicsWidget()
        def widget(self):
            '''QWidget Plasma.PopupApplet.widget()'''
            return QWidget()
        def popupIcon(self):
            '''QIcon Plasma.PopupApplet.popupIcon()'''
            return QIcon()
        def setPopupIcon(self, icon):
            '''void Plasma.PopupApplet.setPopupIcon(QIcon icon)'''
        def setPopupIcon(self, iconName):
            '''void Plasma.PopupApplet.setPopupIcon(QString iconName)'''
    class DataContainer(QObject):
        """"""
        def __init__(self, parent = None):
            '''void Plasma.DataContainer.__init__(QObject parent = None)'''
        def timerEvent(self, event):
            '''void Plasma.DataContainer.timerEvent(QTimerEvent event)'''
        def getDataEngine(self):
            '''Plasma.DataEngine Plasma.DataContainer.getDataEngine()'''
            return Plasma.DataEngine()
        def setNeedsToBeStored(self, store):
            '''void Plasma.DataContainer.setNeedsToBeStored(bool store)'''
        def needsToBeStored(self):
            '''bool Plasma.DataContainer.needsToBeStored()'''
            return bool()
        def isStorageEnabled(self):
            '''bool Plasma.DataContainer.isStorageEnabled()'''
            return bool()
        def setStorageEnabled(self, store):
            '''void Plasma.DataContainer.setStorageEnabled(bool store)'''
        def forceImmediateUpdate(self):
            '''void Plasma.DataContainer.forceImmediateUpdate()'''
        def checkUsage(self):
            '''void Plasma.DataContainer.checkUsage()'''
        def setNeedsUpdate(self, update = True):
            '''void Plasma.DataContainer.setNeedsUpdate(bool update = True)'''
        def timeSinceLastUpdate(self):
            '''int Plasma.DataContainer.timeSinceLastUpdate()'''
            return int()
        def checkForUpdate(self):
            '''void Plasma.DataContainer.checkForUpdate()'''
        updateRequested = pyqtSignal() # void updateRequested(Plasma::DataContainer *) - signal
        becameUnused = pyqtSignal() # void becameUnused(const QStringamp;) - signal
        dataUpdated = pyqtSignal() # void dataUpdated(const QStringamp;,const Plasma::DataEngine::Dataamp;) - signal
        def disconnectVisualization(self, visualization):
            '''void Plasma.DataContainer.disconnectVisualization(QObject visualization)'''
        def connectVisualization(self, visualization, pollingInterval, alignment):
            '''void Plasma.DataContainer.connectVisualization(QObject visualization, int pollingInterval, Plasma.IntervalAlignment alignment)'''
        def visualizationIsConnected(self, visualization):
            '''bool Plasma.DataContainer.visualizationIsConnected(QObject visualization)'''
            return bool()
        def removeAllData(self):
            '''void Plasma.DataContainer.removeAllData()'''
        def setData(self, key, value):
            '''void Plasma.DataContainer.setData(QString key, QVariant value)'''
        def data(self):
            '''dict-of-QString-QVariant Plasma.DataContainer.data()'''
            return dict-of-QString-QVariant()
    class AuthorizationManager(QObject):
        """"""
        # Enum Plasma.AuthorizationManager.AuthorizationPolicy
        DenyAll = 0
        TrustedOnly = 0
        PinPairing = 0
        Custom = 0
    
        readyForRemoteAccess = pyqtSignal() # void readyForRemoteAccess() - signal
        def setAuthorizationInterface(self, interface):
            '''void Plasma.AuthorizationManager.setAuthorizationInterface(Plasma.AuthorizationInterface interface)'''
        def setAuthorizationPolicy(self, policy):
            '''void Plasma.AuthorizationManager.setAuthorizationPolicy(Plasma.AuthorizationManager.AuthorizationPolicy policy)'''
        def self(self):
            '''static Plasma.AuthorizationManager Plasma.AuthorizationManager.self()'''
            return Plasma.AuthorizationManager()
    class ScrollBar(QGraphicsProxyWidget):
        """"""
        def __init__(self, parent = None):
            '''void Plasma.ScrollBar.__init__(QGraphicsWidget parent = None)'''
        sliderMoved = pyqtSignal() # void sliderMoved(int) - signal
        def setMaximum(self, max):
            '''void Plasma.ScrollBar.setMaximum(int max)'''
        def setMinimum(self, min):
            '''void Plasma.ScrollBar.setMinimum(int min)'''
        def orientation(self):
            '''Qt.Orientation Plasma.ScrollBar.orientation()'''
            return Qt.Orientation()
        def contextMenuEvent(self, event):
            '''void Plasma.ScrollBar.contextMenuEvent(QGraphicsSceneContextMenuEvent event)'''
        valueChanged = pyqtSignal() # void valueChanged(int) - signal
        def setOrientation(self, orientation):
            '''void Plasma.ScrollBar.setOrientation(Qt.Orientation orientation)'''
        def setValue(self, val):
            '''void Plasma.ScrollBar.setValue(int val)'''
        def nativeWidget(self):
            '''QScrollBar Plasma.ScrollBar.nativeWidget()'''
            return QScrollBar()
        def styleSheet(self):
            '''QString Plasma.ScrollBar.styleSheet()'''
            return QString()
        def setStyleSheet(self, stylesheet):
            '''void Plasma.ScrollBar.setStyleSheet(QString stylesheet)'''
        def maximum(self):
            '''int Plasma.ScrollBar.maximum()'''
            return int()
        def minimum(self):
            '''int Plasma.ScrollBar.minimum()'''
            return int()
        def value(self):
            '''int Plasma.ScrollBar.value()'''
            return int()
        def pageStep(self):
            '''int Plasma.ScrollBar.pageStep()'''
            return int()
        def setPageStep(self, val):
            '''void Plasma.ScrollBar.setPageStep(int val)'''
        def singleStep(self):
            '''int Plasma.ScrollBar.singleStep()'''
            return int()
        def setSingleStep(self, val):
            '''void Plasma.ScrollBar.setSingleStep(int val)'''
        def setRange(self, min, max):
            '''void Plasma.ScrollBar.setRange(int min, int max)'''
    class AbstractDialogManager(QObject):
        """"""
        def __init__(self, parent = None):
            '''void Plasma.AbstractDialogManager.__init__(Plasma.Corona parent = None)'''
        def showDialog(self, widget, applet):
            '''void Plasma.AbstractDialogManager.showDialog(QWidget widget, Plasma.Applet applet)'''
    class RunnerContext(QObject):
        """"""
        # Enum Plasma.RunnerContext.Type
        __kdevpythondocumentation_builtin_None = 0
        UnknownType = 0
        Directory = 0
        File = 0
        NetworkLocation = 0
        Executable = 0
        ShellCommand = 0
        Help = 0
        FileSystem = 0
    
        def __init__(self, parent = None):
            '''void Plasma.RunnerContext.__init__(QObject parent = None)'''
        def __init__(self, other, parent = None):
            '''void Plasma.RunnerContext.__init__(Plasma.RunnerContext other, QObject parent = None)'''
        def singleRunnerQueryMode(self):
            '''bool Plasma.RunnerContext.singleRunnerQueryMode()'''
            return bool()
        def setSingleRunnerQueryMode(self, enabled):
            '''void Plasma.RunnerContext.setSingleRunnerQueryMode(bool enabled)'''
        def removeMatches(self, matchIdList):
            '''bool Plasma.RunnerContext.removeMatches(QStringList matchIdList)'''
            return bool()
        def removeMatch(self, matchId):
            '''bool Plasma.RunnerContext.removeMatch(QString matchId)'''
            return bool()
        def addMatches(self, term, matches):
            '''bool Plasma.RunnerContext.addMatches(QString term, list-of-Plasma.QueryMatch matches)'''
            return bool()
        matchesChanged = pyqtSignal() # void matchesChanged() - signal
        def run(self, match):
            '''void Plasma.RunnerContext.run(Plasma.QueryMatch match)'''
        def save(self, config):
            '''void Plasma.RunnerContext.save(KConfigGroup config)'''
        def restore(self, config):
            '''void Plasma.RunnerContext.restore(KConfigGroup config)'''
        def match(self, id):
            '''Plasma.QueryMatch Plasma.RunnerContext.match(QString id)'''
            return Plasma.QueryMatch()
        def matches(self):
            '''list-of-Plasma.QueryMatch Plasma.RunnerContext.matches()'''
            return [Plasma.QueryMatch()]
        def addMatch(self, term, match):
            '''bool Plasma.RunnerContext.addMatch(QString term, Plasma.QueryMatch match)'''
            return bool()
        def isValid(self):
            '''bool Plasma.RunnerContext.isValid()'''
            return bool()
        def mimeType(self):
            '''QString Plasma.RunnerContext.mimeType()'''
            return QString()
        def type(self):
            '''Plasma.RunnerContext.Type Plasma.RunnerContext.type()'''
            return Plasma.RunnerContext.Type()
        def query(self):
            '''QString Plasma.RunnerContext.query()'''
            return QString()
        def setQuery(self, term):
            '''void Plasma.RunnerContext.setQuery(QString term)'''
        def reset(self):
            '''void Plasma.RunnerContext.reset()'''
    class BusyWidget(QGraphicsWidget):
        """"""
        def __init__(self, parent = None):
            '''void Plasma.BusyWidget.__init__(QGraphicsWidget parent = None)'''
        def mouseReleaseEvent(self, event):
            '''void Plasma.BusyWidget.mouseReleaseEvent(QGraphicsSceneMouseEvent event)'''
        def timerEvent(self, event):
            '''void Plasma.BusyWidget.timerEvent(QTimerEvent event)'''
        def mousePressEvent(self, event):
            '''void Plasma.BusyWidget.mousePressEvent(QGraphicsSceneMouseEvent event)'''
        def resizeEvent(self, event):
            '''void Plasma.BusyWidget.resizeEvent(QGraphicsSceneResizeEvent event)'''
        def hideEvent(self, event):
            '''void Plasma.BusyWidget.hideEvent(QHideEvent event)'''
        def showEvent(self, event):
            '''void Plasma.BusyWidget.showEvent(QShowEvent event)'''
        def paint(self, painter, option, widget = None):
            '''void Plasma.BusyWidget.paint(QPainter painter, QStyleOptionGraphicsItem option, QWidget widget = None)'''
        clicked = pyqtSignal() # void clicked() - signal
        def label(self):
            '''QString Plasma.BusyWidget.label()'''
            return QString()
        def setLabel(self, label):
            '''void Plasma.BusyWidget.setLabel(QString label)'''
        def isRunning(self):
            '''bool Plasma.BusyWidget.isRunning()'''
            return bool()
        def setRunning(self, running):
            '''void Plasma.BusyWidget.setRunning(bool running)'''
    class ToolTipManager(QObject):
        """"""
        # Enum Plasma.ToolTipManager.State
        Activated = 0
        Inhibited = 0
        Deactivated = 0
    
        linkActivated = pyqtSignal() # void linkActivated(const QStringamp;,Qt::MouseButtons,Qt::KeyboardModifiers,const QPointamp;) - signal
        windowPreviewActivated = pyqtSignal() # void windowPreviewActivated(WId,Qt::MouseButtons,Qt::KeyboardModifiers,const QPointamp;) - signal
        def state(self):
            '''Plasma.ToolTipManager.State Plasma.ToolTipManager.state()'''
            return Plasma.ToolTipManager.State()
        def setState(self, state):
            '''void Plasma.ToolTipManager.setState(Plasma.ToolTipManager.State state)'''
        def clearContent(self, widget):
            '''void Plasma.ToolTipManager.clearContent(QGraphicsWidget widget)'''
        def setContent(self, widget, data):
            '''void Plasma.ToolTipManager.setContent(QGraphicsWidget widget, Plasma.ToolTipContent data)'''
        def unregisterWidget(self, widget):
            '''void Plasma.ToolTipManager.unregisterWidget(QGraphicsWidget widget)'''
        def registerWidget(self, widget):
            '''void Plasma.ToolTipManager.registerWidget(QGraphicsWidget widget)'''
        def hide(self, widget):
            '''void Plasma.ToolTipManager.hide(QGraphicsWidget widget)'''
        def isVisible(self, widget):
            '''bool Plasma.ToolTipManager.isVisible(QGraphicsWidget widget)'''
            return bool()
        def show(self, widget):
            '''void Plasma.ToolTipManager.show(QGraphicsWidget widget)'''
        def self(self):
            '''static Plasma.ToolTipManager Plasma.ToolTipManager.self()'''
            return Plasma.ToolTipManager()
    class TreeView(QGraphicsProxyWidget):
        """"""
        def __init__(self, parent = None):
            '''void Plasma.TreeView.__init__(QGraphicsWidget parent = None)'''
        def nativeWidget(self):
            '''QTreeView Plasma.TreeView.nativeWidget()'''
            return QTreeView()
        def styleSheet(self):
            '''QString Plasma.TreeView.styleSheet()'''
            return QString()
        def setStyleSheet(self, stylesheet):
            '''void Plasma.TreeView.setStyleSheet(QString stylesheet)'''
        def model(self):
            '''QAbstractItemModel Plasma.TreeView.model()'''
            return QAbstractItemModel()
        def setModel(self, model):
            '''void Plasma.TreeView.setModel(QAbstractItemModel model)'''
    class AppletScript(Plasma.ScriptEngine):
        """"""
        def __init__(self, parent = None):
            '''void Plasma.AppletScript.__init__(QObject parent = None)'''
        def setContainmentType(self, type):
            '''void Plasma.AppletScript.setContainmentType(Plasma.Containment.Type type)'''
        def containmentType(self):
            '''Plasma.Containment.Type Plasma.AppletScript.containmentType()'''
            return Plasma.Containment.Type()
        def setDrawWallpaper(self, drawWallpaper):
            '''void Plasma.AppletScript.setDrawWallpaper(bool drawWallpaper)'''
        def drawWallpaper(self):
            '''bool Plasma.AppletScript.drawWallpaper()'''
            return bool()
        def loadAnimationFromPackage(self, name, parent):
            '''Plasma.Animation Plasma.AppletScript.loadAnimationFromPackage(QString name, QObject parent)'''
            return Plasma.Animation()
        popupEvent = pyqtSignal() # void popupEvent(bool) const - signal
        def description(self):
            '''KPluginInfo Plasma.AppletScript.description()'''
            return KPluginInfo()
        def isRegisteredAsDragHandle(self, item):
            '''bool Plasma.AppletScript.isRegisteredAsDragHandle(QGraphicsItem item)'''
            return bool()
        def unregisterAsDragHandle(self, item):
            '''void Plasma.AppletScript.unregisterAsDragHandle(QGraphicsItem item)'''
        def registerAsDragHandle(self, item):
            '''void Plasma.AppletScript.registerAsDragHandle(QGraphicsItem item)'''
        def showMessage(self, icon, message, buttons):
            '''void Plasma.AppletScript.showMessage(QIcon icon, QString message, Plasma.MessageButtons buttons)'''
        saveState = pyqtSignal() # void saveState(KConfigGroupamp;) const - signal
        def addStandardConfigurationPages(self, dialog):
            '''void Plasma.AppletScript.addStandardConfigurationPages(KConfigDialog dialog)'''
        def standardConfigurationDialog(self):
            '''KConfigDialog Plasma.AppletScript.standardConfigurationDialog()'''
            return KConfigDialog()
        def package(self):
            '''Plasma.Package Plasma.AppletScript.package()'''
            return Plasma.Package()
        def mainScript(self):
            '''QString Plasma.AppletScript.mainScript()'''
            return QString()
        def dataEngine(self, engine):
            '''Plasma.DataEngine Plasma.AppletScript.dataEngine(QString engine)'''
            return Plasma.DataEngine()
        def configChanged(self):
            '''void Plasma.AppletScript.configChanged()'''
        def showConfigurationInterface(self):
            '''void Plasma.AppletScript.showConfigurationInterface()'''
        def extender(self):
            '''Plasma.Extender Plasma.AppletScript.extender()'''
            return Plasma.Extender()
        def configNeedsSaving(self):
            '''void Plasma.AppletScript.configNeedsSaving()'''
        def setFailedToLaunch(self, failed, reason = QString()):
            '''void Plasma.AppletScript.setFailedToLaunch(bool failed, QString reason = QString())'''
        def setConfigurationRequired(self, req, reason = QString()):
            '''void Plasma.AppletScript.setConfigurationRequired(bool req, QString reason = QString())'''
        def setHasConfigurationInterface(self, hasInterface):
            '''void Plasma.AppletScript.setHasConfigurationInterface(bool hasInterface)'''
        def shape(self):
            '''QPainterPath Plasma.AppletScript.shape()'''
            return QPainterPath()
        def contextualActions(self):
            '''list-of-QAction Plasma.AppletScript.contextualActions()'''
            return [QAction()]
        def constraintsEvent(self, constraints):
            '''void Plasma.AppletScript.constraintsEvent(Plasma.Constraints constraints)'''
        def size(self):
            '''QSizeF Plasma.AppletScript.size()'''
            return QSizeF()
        def paintInterface(self, painter, option, contentsRect):
            '''void Plasma.AppletScript.paintInterface(QPainter painter, QStyleOptionGraphicsItem option, QRect contentsRect)'''
        def applet(self):
            '''Plasma.Applet Plasma.AppletScript.applet()'''
            return Plasma.Applet()
        def setApplet(self, applet):
            '''void Plasma.AppletScript.setApplet(Plasma.Applet applet)'''
    class PaintUtils():
        """"""
        def texturedText(self, text, font, texture):
            '''static QPixmap Plasma.PaintUtils.texturedText(QString text, QFont font, Plasma.Svg texture)'''
            return QPixmap()
        def centerPixmaps(self, from_, to):
            '''static void Plasma.PaintUtils.centerPixmaps(QPixmap from, QPixmap to)'''
        def drawHalo(self, painter, rect):
            '''static void Plasma.PaintUtils.drawHalo(QPainter painter, QRectF rect)'''
        def shadowText(self, text, font, textColor, shadowColor, offset = None, radius = 2):
            '''static QPixmap Plasma.PaintUtils.shadowText(QString text, QFont font, QColor textColor, QColor shadowColor, QPoint offset = QPoint(1,1), int radius = 2)'''
            return QPixmap()
        def shadowText(self, text, textColor, shadowColor, offset = None, radius = 2):
            '''static QPixmap Plasma.PaintUtils.shadowText(QString text, QColor textColor, QColor shadowColor, QPoint offset = QPoint(1,1), int radius = 2)'''
            return QPixmap()
        def transition(self, from_, to, amount):
            '''static QPixmap Plasma.PaintUtils.transition(QPixmap from, QPixmap to, float amount)'''
            return QPixmap()
        def roundedRectangle(self, rect, radius):
            '''static QPainterPath Plasma.PaintUtils.roundedRectangle(QRectF rect, float radius)'''
            return QPainterPath()
        def shadowBlur(self, image, radius, color):
            '''static void Plasma.PaintUtils.shadowBlur(QImage image, int radius, QColor color)'''
    class SpinBox(QGraphicsProxyWidget):
        """"""
        def __init__(self, parent = None):
            '''void Plasma.SpinBox.__init__(QGraphicsWidget parent = None)'''
        def focusOutEvent(self, event):
            '''void Plasma.SpinBox.focusOutEvent(QFocusEvent event)'''
        def mousePressEvent(self, event):
            '''void Plasma.SpinBox.mousePressEvent(QGraphicsSceneMouseEvent event)'''
        def paint(self, painter, option, widget):
            '''void Plasma.SpinBox.paint(QPainter painter, QStyleOptionGraphicsItem option, QWidget widget)'''
        def resizeEvent(self, event):
            '''void Plasma.SpinBox.resizeEvent(QGraphicsSceneResizeEvent event)'''
        def hoverLeaveEvent(self, event):
            '''void Plasma.SpinBox.hoverLeaveEvent(QGraphicsSceneHoverEvent event)'''
        def hoverEnterEvent(self, event):
            '''void Plasma.SpinBox.hoverEnterEvent(QGraphicsSceneHoverEvent event)'''
        def changeEvent(self, event):
            '''void Plasma.SpinBox.changeEvent(QEvent event)'''
        editingFinished = pyqtSignal() # void editingFinished() - signal
        valueChanged = pyqtSignal() # void valueChanged(int) - signal
        sliderMoved = pyqtSignal() # void sliderMoved(int) - signal
        def setValue(self, value):
            '''void Plasma.SpinBox.setValue(int value)'''
        def setRange(self, minimum, maximum):
            '''void Plasma.SpinBox.setRange(int minimum, int maximum)'''
        def setMinimum(self, minimum):
            '''void Plasma.SpinBox.setMinimum(int minimum)'''
        def setMaximum(self, maximum):
            '''void Plasma.SpinBox.setMaximum(int maximum)'''
        def nativeWidget(self):
            '''KIntSpinBox Plasma.SpinBox.nativeWidget()'''
            return KIntSpinBox()
        def styleSheet(self):
            '''QString Plasma.SpinBox.styleSheet()'''
            return QString()
        def setStyleSheet(self, stylesheet):
            '''void Plasma.SpinBox.setStyleSheet(QString stylesheet)'''
        def value(self):
            '''int Plasma.SpinBox.value()'''
            return int()
        def minimum(self):
            '''int Plasma.SpinBox.minimum()'''
            return int()
        def maximum(self):
            '''int Plasma.SpinBox.maximum()'''
            return int()
    class RadioButton(QGraphicsProxyWidget):
        """"""
        def __init__(self, parent = None):
            '''void Plasma.RadioButton.__init__(QGraphicsWidget parent = None)'''
        def changeEvent(self, event):
            '''void Plasma.RadioButton.changeEvent(QEvent event)'''
        def resizeEvent(self, event):
            '''void Plasma.RadioButton.resizeEvent(QGraphicsSceneResizeEvent event)'''
        toggled = pyqtSignal() # void toggled(bool) - signal
        def isChecked(self):
            '''bool Plasma.RadioButton.isChecked()'''
            return bool()
        def setChecked(self, checked):
            '''void Plasma.RadioButton.setChecked(bool checked)'''
        def nativeWidget(self):
            '''QRadioButton Plasma.RadioButton.nativeWidget()'''
            return QRadioButton()
        def styleSheet(self):
            '''QString Plasma.RadioButton.styleSheet()'''
            return QString()
        def setStyleSheet(self, stylesheet):
            '''void Plasma.RadioButton.setStyleSheet(QString stylesheet)'''
        def image(self):
            '''QString Plasma.RadioButton.image()'''
            return QString()
        def setImage(self, path):
            '''void Plasma.RadioButton.setImage(QString path)'''
        def text(self):
            '''QString Plasma.RadioButton.text()'''
            return QString()
        def setText(self, text):
            '''void Plasma.RadioButton.setText(QString text)'''
    class Animation():
        """"""
        class MovementDirection():
            """"""
            def __init__(self):
                '''Plasma.Animation.MovementDirection Plasma.Animation.MovementDirection.__init__()'''
                return Plasma.Animation.MovementDirection()
            def __init__(self):
                '''int Plasma.Animation.MovementDirection.__init__()'''
                return int()
            def __init__(self):
                '''void Plasma.Animation.MovementDirection.__init__()'''
            def __bool__(self):
                '''int Plasma.Animation.MovementDirection.__bool__()'''
                return int()
            def __ne__(self, f):
                '''bool Plasma.Animation.MovementDirection.__ne__(Plasma.Animation.MovementDirection f)'''
                return bool()
            def __eq__(self, f):
                '''bool Plasma.Animation.MovementDirection.__eq__(Plasma.Animation.MovementDirection f)'''
                return bool()
            def __invert__(self):
                '''Plasma.Animation.MovementDirection Plasma.Animation.MovementDirection.__invert__()'''
                return Plasma.Animation.MovementDirection()
            def __and__(self, mask):
                '''Plasma.Animation.MovementDirection Plasma.Animation.MovementDirection.__and__(int mask)'''
                return Plasma.Animation.MovementDirection()
            def __xor__(self, f):
                '''Plasma.Animation.MovementDirection Plasma.Animation.MovementDirection.__xor__(Plasma.Animation.MovementDirection f)'''
                return Plasma.Animation.MovementDirection()
            def __xor__(self, f):
                '''Plasma.Animation.MovementDirection Plasma.Animation.MovementDirection.__xor__(int f)'''
                return Plasma.Animation.MovementDirection()
            def __or__(self, f):
                '''Plasma.Animation.MovementDirection Plasma.Animation.MovementDirection.__or__(Plasma.Animation.MovementDirection f)'''
                return Plasma.Animation.MovementDirection()
            def __or__(self, f):
                '''Plasma.Animation.MovementDirection Plasma.Animation.MovementDirection.__or__(int f)'''
                return Plasma.Animation.MovementDirection()
            def __int__(self):
                '''int Plasma.Animation.MovementDirection.__int__()'''
                return int()
            def __ixor__(self, f):
                '''Plasma.Animation.MovementDirection Plasma.Animation.MovementDirection.__ixor__(Plasma.Animation.MovementDirection f)'''
                return Plasma.Animation.MovementDirection()
            def __ior__(self, f):
                '''Plasma.Animation.MovementDirection Plasma.Animation.MovementDirection.__ior__(Plasma.Animation.MovementDirection f)'''
                return Plasma.Animation.MovementDirection()
            def __iand__(self, mask):
                '''Plasma.Animation.MovementDirection Plasma.Animation.MovementDirection.__iand__(int mask)'''
                return Plasma.Animation.MovementDirection()
    class AbstractRunner(QObject):
        """"""
        # Enum Plasma.AbstractRunner.Priority
        LowestPriority = 0
        LowPriority = 0
        NormalPriority = 0
        HighPriority = 0
        HighestPriority = 0
    
        # Enum Plasma.AbstractRunner.Speed
        SlowSpeed = 0
        NormalSpeed = 0
    
        def __init__(self, parent = None, path = QString()):
            '''void Plasma.AbstractRunner.__init__(QObject parent = None, QString path = QString())'''
        def __init__(self, parent, args):
            '''void Plasma.AbstractRunner.__init__(QObject parent, list-of-QVariant args)'''
        def __init__(self, service, parent = None):
            '''void Plasma.AbstractRunner.__init__(unknown-type service, QObject parent = None)'''
        def suspendMatching(self, suspend):
            '''void Plasma.AbstractRunner.suspendMatching(bool suspend)'''
        matchingSuspended = pyqtSignal() # void matchingSuspended(bool) - signal
        def isMatchingSuspended(self):
            '''bool Plasma.AbstractRunner.isMatchingSuspended()'''
            return bool()
        def mimeDataForMatch(self, match):
            '''QMimeData Plasma.AbstractRunner.mimeDataForMatch(Plasma.QueryMatch match)'''
            return QMimeData()
        def dataEngine(self, name):
            '''Plasma.DataEngine Plasma.AbstractRunner.dataEngine(QString name)'''
            return Plasma.DataEngine()
        def setDefaultSyntax(self, syntax):
            '''void Plasma.AbstractRunner.setDefaultSyntax(Plasma.RunnerSyntax syntax)'''
        def defaultSyntax(self):
            '''Plasma.RunnerSyntax Plasma.AbstractRunner.defaultSyntax()'''
            return Plasma.RunnerSyntax()
        teardown = pyqtSignal() # void teardown() - signal
        prepare = pyqtSignal() # void prepare() - signal
        def setSyntaxes(self, syns):
            '''void Plasma.AbstractRunner.setSyntaxes(list-of-Plasma.RunnerSyntax syns)'''
        def init(self):
            '''void Plasma.AbstractRunner.init()'''
        def addSyntax(self, syntax):
            '''void Plasma.AbstractRunner.addSyntax(Plasma.RunnerSyntax syntax)'''
        def clearActions(self):
            '''void Plasma.AbstractRunner.clearActions()'''
        def actions(self):
            '''unknown-type Plasma.AbstractRunner.actions()'''
            return unknown-type()
        def action(self, id):
            '''QAction Plasma.AbstractRunner.action(QString id)'''
            return QAction()
        def removeAction(self, id):
            '''void Plasma.AbstractRunner.removeAction(QString id)'''
        def addAction(self, id, icon, text):
            '''QAction Plasma.AbstractRunner.addAction(QString id, QIcon icon, QString text)'''
            return QAction()
        def addAction(self, id, action):
            '''void Plasma.AbstractRunner.addAction(QString id, QAction action)'''
        def actionsForMatch(self, match):
            '''list-of-QAction Plasma.AbstractRunner.actionsForMatch(Plasma.QueryMatch match)'''
            return [QAction()]
        def serviceQuery(self, serviceType, constraint = QString()):
            '''unknown-type Plasma.AbstractRunner.serviceQuery(QString serviceType, QString constraint = QString())'''
            return unknown-type()
        def setPriority(self, newPriority):
            '''void Plasma.AbstractRunner.setPriority(Plasma.AbstractRunner.Priority newPriority)'''
        def setSpeed(self, newSpeed):
            '''void Plasma.AbstractRunner.setSpeed(Plasma.AbstractRunner.Speed newSpeed)'''
        def setHasRunOptions(self, hasRunOptions):
            '''void Plasma.AbstractRunner.setHasRunOptions(bool hasRunOptions)'''
        def config(self):
            '''KConfigGroup Plasma.AbstractRunner.config()'''
            return KConfigGroup()
        def bigLock(self):
            '''static QMutex Plasma.AbstractRunner.bigLock()'''
            return QMutex()
        def syntaxes(self):
            '''list-of-Plasma.RunnerSyntax Plasma.AbstractRunner.syntaxes()'''
            return [Plasma.RunnerSyntax()]
        def reloadConfiguration(self):
            '''void Plasma.AbstractRunner.reloadConfiguration()'''
        def package(self):
            '''Plasma.Package Plasma.AbstractRunner.package()'''
            return Plasma.Package()
        def icon(self):
            '''QIcon Plasma.AbstractRunner.icon()'''
            return QIcon()
        def description(self):
            '''QString Plasma.AbstractRunner.description()'''
            return QString()
        def id(self):
            '''QString Plasma.AbstractRunner.id()'''
            return QString()
        def name(self):
            '''QString Plasma.AbstractRunner.name()'''
            return QString()
        def setIgnoredTypes(self, types):
            '''void Plasma.AbstractRunner.setIgnoredTypes(Plasma.RunnerContext.Types types)'''
        def ignoredTypes(self):
            '''Plasma.RunnerContext.Types Plasma.AbstractRunner.ignoredTypes()'''
            return Plasma.RunnerContext.Types()
        def priority(self):
            '''Plasma.AbstractRunner.Priority Plasma.AbstractRunner.priority()'''
            return Plasma.AbstractRunner.Priority()
        def speed(self):
            '''Plasma.AbstractRunner.Speed Plasma.AbstractRunner.speed()'''
            return Plasma.AbstractRunner.Speed()
        def run(self, context, match):
            '''void Plasma.AbstractRunner.run(Plasma.RunnerContext context, Plasma.QueryMatch match)'''
        def createRunOptions(self, widget):
            '''void Plasma.AbstractRunner.createRunOptions(QWidget widget)'''
        def hasRunOptions(self):
            '''bool Plasma.AbstractRunner.hasRunOptions()'''
            return bool()
        def performMatch(self, context):
            '''void Plasma.AbstractRunner.performMatch(Plasma.RunnerContext context)'''
        def match(self, context):
            '''void Plasma.AbstractRunner.match(Plasma.RunnerContext context)'''
    class FlashingLabel(QGraphicsWidget):
        """"""
        def __init__(self, parent = None):
            '''void Plasma.FlashingLabel.__init__(QGraphicsItem parent = None)'''
        def duration(self):
            '''int Plasma.FlashingLabel.duration()'''
            return int()
        def color(self):
            '''QColor Plasma.FlashingLabel.color()'''
            return QColor()
        def font(self):
            '''QFont Plasma.FlashingLabel.font()'''
            return QFont()
        def sizeHint(self, which, constraint):
            '''QSizeF Plasma.FlashingLabel.sizeHint(Qt.SizeHint which, QSizeF constraint)'''
            return QSizeF()
        def fadeOut(self):
            '''void Plasma.FlashingLabel.fadeOut()'''
        def fadeIn(self):
            '''void Plasma.FlashingLabel.fadeIn()'''
        def kill(self):
            '''void Plasma.FlashingLabel.kill()'''
        def autohide(self):
            '''bool Plasma.FlashingLabel.autohide()'''
            return bool()
        def setAutohide(self, autohide):
            '''void Plasma.FlashingLabel.setAutohide(bool autohide)'''
        def flash(self, text, duration = 0, option = None):
            '''void Plasma.FlashingLabel.flash(QString text, int duration = 0, QTextOption option = QTextOption(Qt.AlignCenter))'''
        def flash(self, pixmap, duration = 0, align = None):
            '''void Plasma.FlashingLabel.flash(QPixmap pixmap, int duration = 0, Qt.Alignment align = Qt.AlignCenter)'''
        def setDuration(self, duration):
            '''void Plasma.FlashingLabel.setDuration(int duration)'''
        def setColor(self):
            '''QColor Plasma.FlashingLabel.setColor()'''
            return QColor()
        def setFont(self):
            '''QFont Plasma.FlashingLabel.setFont()'''
            return QFont()
        def paint(self, painter, option, widget = None):
            '''void Plasma.FlashingLabel.paint(QPainter painter, QStyleOptionGraphicsItem option, QWidget widget = None)'''
    class ComponentTypes():
        """"""
        def __init__(self):
            '''Plasma.ComponentTypes Plasma.ComponentTypes.__init__()'''
            return Plasma.ComponentTypes()
        def __init__(self):
            '''int Plasma.ComponentTypes.__init__()'''
            return int()
        def __init__(self):
            '''void Plasma.ComponentTypes.__init__()'''
        def __bool__(self):
            '''int Plasma.ComponentTypes.__bool__()'''
            return int()
        def __ne__(self, f):
            '''bool Plasma.ComponentTypes.__ne__(Plasma.ComponentTypes f)'''
            return bool()
        def __eq__(self, f):
            '''bool Plasma.ComponentTypes.__eq__(Plasma.ComponentTypes f)'''
            return bool()
        def __invert__(self):
            '''Plasma.ComponentTypes Plasma.ComponentTypes.__invert__()'''
            return Plasma.ComponentTypes()
        def __and__(self, mask):
            '''Plasma.ComponentTypes Plasma.ComponentTypes.__and__(int mask)'''
            return Plasma.ComponentTypes()
        def __xor__(self, f):
            '''Plasma.ComponentTypes Plasma.ComponentTypes.__xor__(Plasma.ComponentTypes f)'''
            return Plasma.ComponentTypes()
        def __xor__(self, f):
            '''Plasma.ComponentTypes Plasma.ComponentTypes.__xor__(int f)'''
            return Plasma.ComponentTypes()
        def __or__(self, f):
            '''Plasma.ComponentTypes Plasma.ComponentTypes.__or__(Plasma.ComponentTypes f)'''
            return Plasma.ComponentTypes()
        def __or__(self, f):
            '''Plasma.ComponentTypes Plasma.ComponentTypes.__or__(int f)'''
            return Plasma.ComponentTypes()
        def __int__(self):
            '''int Plasma.ComponentTypes.__int__()'''
            return int()
        def __ixor__(self, f):
            '''Plasma.ComponentTypes Plasma.ComponentTypes.__ixor__(Plasma.ComponentTypes f)'''
            return Plasma.ComponentTypes()
        def __ior__(self, f):
            '''Plasma.ComponentTypes Plasma.ComponentTypes.__ior__(Plasma.ComponentTypes f)'''
            return Plasma.ComponentTypes()
        def __iand__(self, mask):
            '''Plasma.ComponentTypes Plasma.ComponentTypes.__iand__(int mask)'''
            return Plasma.ComponentTypes()
    class Extender(QGraphicsWidget):
        """"""
        # Enum Plasma.Extender.Appearance
        NoBorders = 0
        BottomUpStacked = 0
        TopDownStacked = 0
    
        def __init__(self, applet):
            '''void Plasma.Extender.__init__(Plasma.Applet applet)'''
        def applet(self):
            '''Plasma.Applet Plasma.Extender.applet()'''
            return Plasma.Applet()
        def itemChange(self, change, value):
            '''QVariant Plasma.Extender.itemChange(QGraphicsItem.GraphicsItemChange change, QVariant value)'''
            return QVariant()
        geometryChanged = pyqtSignal() # void geometryChanged() - signal
        itemDetached = pyqtSignal() # void itemDetached(Plasma::ExtenderItem *) - signal
        itemAttached = pyqtSignal() # void itemAttached(Plasma::ExtenderItem *) - signal
        def dropEvent(self, event):
            '''void Plasma.Extender.dropEvent(QGraphicsSceneDragDropEvent event)'''
        def dragLeaveEvent(self, event):
            '''void Plasma.Extender.dragLeaveEvent(QGraphicsSceneDragDropEvent event)'''
        def dragMoveEvent(self, event):
            '''void Plasma.Extender.dragMoveEvent(QGraphicsSceneDragDropEvent event)'''
        def dragEnterEvent(self, event):
            '''void Plasma.Extender.dragEnterEvent(QGraphicsSceneDragDropEvent event)'''
        def mousePressEvent(self, event):
            '''void Plasma.Extender.mousePressEvent(QGraphicsSceneMouseEvent event)'''
        def resizeEvent(self, event):
            '''void Plasma.Extender.resizeEvent(QGraphicsSceneResizeEvent event)'''
        def enabledBordersForItem(self, item):
            '''Plasma.FrameSvg.EnabledBorders Plasma.Extender.enabledBordersForItem(Plasma.ExtenderItem item)'''
            return Plasma.FrameSvg.EnabledBorders()
        def saveState(self):
            '''void Plasma.Extender.saveState()'''
        def itemHoverLeaveEvent(self, item):
            '''void Plasma.Extender.itemHoverLeaveEvent(Plasma.ExtenderItem item)'''
        def itemHoverMoveEvent(self, item, pos):
            '''void Plasma.Extender.itemHoverMoveEvent(Plasma.ExtenderItem item, QPointF pos)'''
        def itemHoverEnterEvent(self, item):
            '''void Plasma.Extender.itemHoverEnterEvent(Plasma.ExtenderItem item)'''
        def itemRemovedEvent(self, item):
            '''void Plasma.Extender.itemRemovedEvent(Plasma.ExtenderItem item)'''
        def itemAddedEvent(self, item, pos = None):
            '''void Plasma.Extender.itemAddedEvent(Plasma.ExtenderItem item, QPointF pos = QPointF(-1,-1))'''
        def groups(self):
            '''list-of-Plasma.ExtenderGroup Plasma.Extender.groups()'''
            return [Plasma.ExtenderGroup()]
        def appearance(self):
            '''Plasma.Extender.Appearance Plasma.Extender.appearance()'''
            return Plasma.Extender.Appearance()
        def setAppearance(self, appearance):
            '''void Plasma.Extender.setAppearance(Plasma.Extender.Appearance appearance)'''
        def isEmpty(self):
            '''bool Plasma.Extender.isEmpty()'''
            return bool()
        def hasItem(self, name):
            '''bool Plasma.Extender.hasItem(QString name)'''
            return bool()
        def group(self, name):
            '''Plasma.ExtenderGroup Plasma.Extender.group(QString name)'''
            return Plasma.ExtenderGroup()
        def item(self, name):
            '''Plasma.ExtenderItem Plasma.Extender.item(QString name)'''
            return Plasma.ExtenderItem()
        def detachedItems(self):
            '''list-of-Plasma.ExtenderItem Plasma.Extender.detachedItems()'''
            return [Plasma.ExtenderItem()]
        def attachedItems(self):
            '''list-of-Plasma.ExtenderItem Plasma.Extender.attachedItems()'''
            return [Plasma.ExtenderItem()]
        def items(self):
            '''list-of-Plasma.ExtenderItem Plasma.Extender.items()'''
            return [Plasma.ExtenderItem()]
        def emptyExtenderMessage(self):
            '''QString Plasma.Extender.emptyExtenderMessage()'''
            return QString()
        def setEmptyExtenderMessage(self, message):
            '''void Plasma.Extender.setEmptyExtenderMessage(QString message)'''
    class GroupBox(QGraphicsProxyWidget):
        """"""
        def __init__(self, parent = None):
            '''void Plasma.GroupBox.__init__(QGraphicsWidget parent = None)'''
        def changeEvent(self, event):
            '''void Plasma.GroupBox.changeEvent(QEvent event)'''
        def resizeEvent(self, event):
            '''void Plasma.GroupBox.resizeEvent(QGraphicsSceneResizeEvent event)'''
        def nativeWidget(self):
            '''QGroupBox Plasma.GroupBox.nativeWidget()'''
            return QGroupBox()
        def styleSheet(self):
            '''QString Plasma.GroupBox.styleSheet()'''
            return QString()
        def setStyleSheet(self, stylesheet):
            '''void Plasma.GroupBox.setStyleSheet(QString stylesheet)'''
        def text(self):
            '''QString Plasma.GroupBox.text()'''
            return QString()
        def setText(self, text):
            '''void Plasma.GroupBox.setText(QString text)'''
    class Svg(QObject):
        """"""
        def __init__(self, parent = None):
            '''void Plasma.Svg.__init__(QObject parent = None)'''
        sizeChanged = pyqtSignal() # void sizeChanged() - signal
        repaintNeeded = pyqtSignal() # void repaintNeeded() - signal
        def theme(self):
            '''Plasma.Theme Plasma.Svg.theme()'''
            return Plasma.Theme()
        def setTheme(self, theme):
            '''void Plasma.Svg.setTheme(Plasma.Theme theme)'''
        def isUsingRenderingCache(self):
            '''bool Plasma.Svg.isUsingRenderingCache()'''
            return bool()
        def setUsingRenderingCache(self, useCache):
            '''void Plasma.Svg.setUsingRenderingCache(bool useCache)'''
        def imagePath(self):
            '''QString Plasma.Svg.imagePath()'''
            return QString()
        def setImagePath(self, svgFilePath):
            '''void Plasma.Svg.setImagePath(QString svgFilePath)'''
        def containsMultipleImages(self):
            '''bool Plasma.Svg.containsMultipleImages()'''
            return bool()
        def setContainsMultipleImages(self, multiple):
            '''void Plasma.Svg.setContainsMultipleImages(bool multiple)'''
        def isValid(self):
            '''bool Plasma.Svg.isValid()'''
            return bool()
        def elementAtPoint(self, point):
            '''QString Plasma.Svg.elementAtPoint(QPoint point)'''
            return QString()
        def hasElement(self, elementId):
            '''bool Plasma.Svg.hasElement(QString elementId)'''
            return bool()
        def elementRect(self, elementId):
            '''QRectF Plasma.Svg.elementRect(QString elementId)'''
            return QRectF()
        def elementSize(self, elementId):
            '''QSize Plasma.Svg.elementSize(QString elementId)'''
            return QSize()
        def resize(self, width, height):
            '''void Plasma.Svg.resize(float width, float height)'''
        def resize(self, size):
            '''void Plasma.Svg.resize(QSizeF size)'''
        def resize(self):
            '''void Plasma.Svg.resize()'''
        def size(self):
            '''QSize Plasma.Svg.size()'''
            return QSize()
        def paint(self, painter, point, elementID = QString()):
            '''void Plasma.Svg.paint(QPainter painter, QPointF point, QString elementID = QString())'''
        def paint(self, painter, x, y, elementID = QString()):
            '''void Plasma.Svg.paint(QPainter painter, int x, int y, QString elementID = QString())'''
        def paint(self, painter, rect, elementID = QString()):
            '''void Plasma.Svg.paint(QPainter painter, QRectF rect, QString elementID = QString())'''
        def paint(self, painter, x, y, width, height, elementID = QString()):
            '''void Plasma.Svg.paint(QPainter painter, int x, int y, int width, int height, QString elementID = QString())'''
        def pixmap(self, elementID = QString()):
            '''QPixmap Plasma.Svg.pixmap(QString elementID = QString())'''
            return QPixmap()
    class VideoWidget(QGraphicsProxyWidget):
        """"""
        # Enum Plasma.VideoWidget.Control
        NoControls = 0
        Play = 0
        Pause = 0
        Stop = 0
        PlayPause = 0
        Previous = 0
        Next = 0
        Progress = 0
        Volume = 0
        OpenFile = 0
        DefaultControls = 0
    
        def __init__(self, parent = None):
            '''void Plasma.VideoWidget.__init__(QGraphicsWidget parent = None)'''
        def tickInterval(self):
            '''int Plasma.VideoWidget.tickInterval()'''
            return int()
        def setTickInterval(self, interval):
            '''void Plasma.VideoWidget.setTickInterval(int interval)'''
        def hoverMoveEvent(self, event):
            '''void Plasma.VideoWidget.hoverMoveEvent(QGraphicsSceneHoverEvent event)'''
        def hoverLeaveEvent(self, event):
            '''void Plasma.VideoWidget.hoverLeaveEvent(QGraphicsSceneHoverEvent event)'''
        def hoverEnterEvent(self, event):
            '''void Plasma.VideoWidget.hoverEnterEvent(QGraphicsSceneHoverEvent event)'''
        def resizeEvent(self, event):
            '''void Plasma.VideoWidget.resizeEvent(QGraphicsSceneResizeEvent event)'''
        previousRequested = pyqtSignal() # void previousRequested() - signal
        nextRequested = pyqtSignal() # void nextRequested() - signal
        aboutToFinish = pyqtSignal() # void aboutToFinish() - signal
        tick = pyqtSignal() # void tick(qint64) - signal
        def seek(self, time):
            '''void Plasma.VideoWidget.seek(int time)'''
        def stop(self):
            '''void Plasma.VideoWidget.stop()'''
        def pause(self):
            '''void Plasma.VideoWidget.pause()'''
        def play(self):
            '''void Plasma.VideoWidget.play()'''
        def styleSheet(self):
            '''QString Plasma.VideoWidget.styleSheet()'''
            return QString()
        def setStyleSheet(self, stylesheet):
            '''void Plasma.VideoWidget.setStyleSheet(QString stylesheet)'''
        def controlsVisible(self):
            '''bool Plasma.VideoWidget.controlsVisible()'''
            return bool()
        def setControlsVisible(self, visible):
            '''void Plasma.VideoWidget.setControlsVisible(bool visible)'''
        def usedControls(self):
            '''Plasma.VideoWidget.Controls Plasma.VideoWidget.usedControls()'''
            return Plasma.VideoWidget.Controls()
        def setUsedControls(self, controls):
            '''void Plasma.VideoWidget.setUsedControls(Plasma.VideoWidget.Controls controls)'''
        def remainingTime(self):
            '''int Plasma.VideoWidget.remainingTime()'''
            return int()
        def totalTime(self):
            '''int Plasma.VideoWidget.totalTime()'''
            return int()
        def currentTime(self):
            '''int Plasma.VideoWidget.currentTime()'''
            return int()
        def url(self):
            '''QString Plasma.VideoWidget.url()'''
            return QString()
        def setUrl(self, url):
            '''void Plasma.VideoWidget.setUrl(QString url)'''
    class View(QGraphicsView):
        """"""
        def __init__(self, containment, parent = None):
            '''void Plasma.View.__init__(Plasma.Containment containment, QWidget parent = None)'''
        def __init__(self, containment, viewId, parent = None):
            '''void Plasma.View.__init__(Plasma.Containment containment, int viewId, QWidget parent = None)'''
        lostContainment = pyqtSignal() # void lostContainment() - signal
        def configNeedsSaving(self):
            '''void Plasma.View.configNeedsSaving()'''
        def config(self):
            '''KConfigGroup Plasma.View.config()'''
            return KConfigGroup()
        def setContainment(self, containment):
            '''void Plasma.View.setContainment(Plasma.Containment containment)'''
        sceneRectChanged = pyqtSignal() # void sceneRectChanged() - signal
        sceneRectAboutToChange = pyqtSignal() # void sceneRectAboutToChange() - signal
        def id(self):
            '''int Plasma.View.id()'''
            return int()
        def topLevelViewAt(self, pos):
            '''static Plasma.View Plasma.View.topLevelViewAt(QPoint pos)'''
            return Plasma.View()
        def trackContainmentChanges(self):
            '''bool Plasma.View.trackContainmentChanges()'''
            return bool()
        def setTrackContainmentChanges(self, trackChanges):
            '''void Plasma.View.setTrackContainmentChanges(bool trackChanges)'''
        def swapContainment(self, existing, name, args = QVariantList()):
            '''Plasma.Containment Plasma.View.swapContainment(Plasma.Containment existing, QString name, list-of-QVariant args = QVariantList())'''
            return Plasma.Containment()
        def swapContainment(self, name, args = QVariantList()):
            '''Plasma.Containment Plasma.View.swapContainment(QString name, list-of-QVariant args = QVariantList())'''
            return Plasma.Containment()
        def containment(self):
            '''Plasma.Containment Plasma.View.containment()'''
            return Plasma.Containment()
        def effectiveDesktop(self):
            '''int Plasma.View.effectiveDesktop()'''
            return int()
        def desktop(self):
            '''int Plasma.View.desktop()'''
            return int()
        def screen(self):
            '''int Plasma.View.screen()'''
            return int()
        def setScreen(self, screen, desktop = None):
            '''void Plasma.View.setScreen(int screen, int desktop = -1)'''
        def isWallpaperEnabled(self):
            '''bool Plasma.View.isWallpaperEnabled()'''
            return bool()
        def setWallpaperEnabled(self, draw):
            '''void Plasma.View.setWallpaperEnabled(bool draw)'''
    class PushButton(QGraphicsProxyWidget):
        """"""
        def __init__(self, parent = None):
            '''void Plasma.PushButton.__init__(QGraphicsWidget parent = None)'''
        def click(self):
            '''void Plasma.PushButton.click()'''
        def sizeHint(self, which, constraint):
            '''QSizeF Plasma.PushButton.sizeHint(Qt.SizeHint which, QSizeF constraint)'''
            return QSizeF()
        def isCheckable(self):
            '''bool Plasma.PushButton.isCheckable()'''
            return bool()
        def changeEvent(self, event):
            '''void Plasma.PushButton.changeEvent(QEvent event)'''
        released = pyqtSignal() # void released() - signal
        pressed = pyqtSignal() # void pressed() - signal
        def isDown(self):
            '''bool Plasma.PushButton.isDown()'''
            return bool()
        def hoverLeaveEvent(self, event):
            '''void Plasma.PushButton.hoverLeaveEvent(QGraphicsSceneHoverEvent event)'''
        def hoverEnterEvent(self, event):
            '''void Plasma.PushButton.hoverEnterEvent(QGraphicsSceneHoverEvent event)'''
        def resizeEvent(self, event):
            '''void Plasma.PushButton.resizeEvent(QGraphicsSceneResizeEvent event)'''
        def paint(self, painter, option, widget = None):
            '''void Plasma.PushButton.paint(QPainter painter, QStyleOptionGraphicsItem option, QWidget widget = None)'''
        toggled = pyqtSignal() # void toggled(bool) - signal
        clicked = pyqtSignal() # void clicked() - signal
        def nativeWidget(self):
            '''KPushButton Plasma.PushButton.nativeWidget()'''
            return KPushButton()
        def isChecked(self):
            '''bool Plasma.PushButton.isChecked()'''
            return bool()
        def setChecked(self, checked):
            '''void Plasma.PushButton.setChecked(bool checked)'''
        def setCheckable(self, checkable):
            '''void Plasma.PushButton.setCheckable(bool checkable)'''
        def icon(self):
            '''QIcon Plasma.PushButton.icon()'''
            return QIcon()
        def setIcon(self, icon):
            '''void Plasma.PushButton.setIcon(QIcon icon)'''
        def setIcon(self, icon):
            '''void Plasma.PushButton.setIcon(KIcon icon)'''
        def action(self):
            '''QAction Plasma.PushButton.action()'''
            return QAction()
        def setAction(self, action):
            '''void Plasma.PushButton.setAction(QAction action)'''
        def styleSheet(self):
            '''QString Plasma.PushButton.styleSheet()'''
            return QString()
        def setStyleSheet(self, stylesheet):
            '''void Plasma.PushButton.setStyleSheet(QString stylesheet)'''
        def image(self):
            '''QString Plasma.PushButton.image()'''
            return QString()
        def setImage(self, path):
            '''void Plasma.PushButton.setImage(QString path)'''
        def setImage(self, path, elementid):
            '''void Plasma.PushButton.setImage(QString path, QString elementid)'''
        def text(self):
            '''QString Plasma.PushButton.text()'''
            return QString()
        def setText(self, text):
            '''void Plasma.PushButton.setText(QString text)'''
    class DeclarativeWidget(QGraphicsWidget):
        """"""
        def __init__(self, parent = None):
            '''void Plasma.DeclarativeWidget.__init__(QGraphicsWidget parent = None)'''
        def scriptEngine(self):
            '''QScriptEngine Plasma.DeclarativeWidget.scriptEngine()'''
            return QScriptEngine()
        finished = pyqtSignal() # void finished() - signal
        def resizeEvent(self, event):
            '''void Plasma.DeclarativeWidget.resizeEvent(QGraphicsSceneResizeEvent event)'''
        def mainComponent(self):
            '''QDeclarativeComponent Plasma.DeclarativeWidget.mainComponent()'''
            return QDeclarativeComponent()
        def rootObject(self):
            '''QObject Plasma.DeclarativeWidget.rootObject()'''
            return QObject()
        def engine(self):
            '''QDeclarativeEngine Plasma.DeclarativeWidget.engine()'''
            return QDeclarativeEngine()
        def isInitializationDelayed(self):
            '''bool Plasma.DeclarativeWidget.isInitializationDelayed()'''
            return bool()
        def setInitializationDelayed(self, delay):
            '''void Plasma.DeclarativeWidget.setInitializationDelayed(bool delay)'''
        def qmlPath(self):
            '''QString Plasma.DeclarativeWidget.qmlPath()'''
            return QString()
        def setQmlPath(self, path):
            '''void Plasma.DeclarativeWidget.setQmlPath(QString path)'''
    class RunnerScript(Plasma.ScriptEngine):
        """"""
        def __init__(self, parent = None):
            '''void Plasma.RunnerScript.__init__(QObject parent = None)'''
        def dataEngine(self, name):
            '''Plasma.DataEngine Plasma.RunnerScript.dataEngine(QString name)'''
            return Plasma.DataEngine()
        def description(self):
            '''KPluginInfo Plasma.RunnerScript.description()'''
            return KPluginInfo()
        actionsForMatch = pyqtSignal() # void actionsForMatch(const Plasma::QueryMatchamp;,QListlt;QAction *gt; *) - signal
        def setSyntaxes(self, syns):
            '''void Plasma.RunnerScript.setSyntaxes(list-of-Plasma.RunnerSyntax syns)'''
        def addSyntax(self, syntax):
            '''void Plasma.RunnerScript.addSyntax(Plasma.RunnerSyntax syntax)'''
        def clearActions(self):
            '''void Plasma.RunnerScript.clearActions()'''
        def actions(self):
            '''unknown-type Plasma.RunnerScript.actions()'''
            return unknown-type()
        def action(self, id):
            '''QAction Plasma.RunnerScript.action(QString id)'''
            return QAction()
        def removeAction(self, id):
            '''void Plasma.RunnerScript.removeAction(QString id)'''
        def addAction(self, id, icon, text):
            '''QAction Plasma.RunnerScript.addAction(QString id, QIcon icon, QString text)'''
            return QAction()
        def addAction(self, id, action):
            '''void Plasma.RunnerScript.addAction(QString id, QAction action)'''
        def serviceQuery(self, serviceType, constraint = QString()):
            '''unknown-type Plasma.RunnerScript.serviceQuery(QString serviceType, QString constraint = QString())'''
            return unknown-type()
        def setPriority(self, newPriority):
            '''void Plasma.RunnerScript.setPriority(Plasma.AbstractRunner.Priority newPriority)'''
        def setSpeed(self, newSpeed):
            '''void Plasma.RunnerScript.setSpeed(Plasma.AbstractRunner.Speed newSpeed)'''
        def setHasRunOptions(self, hasRunOptions):
            '''void Plasma.RunnerScript.setHasRunOptions(bool hasRunOptions)'''
        def setIgnoredTypes(self, types):
            '''void Plasma.RunnerScript.setIgnoredTypes(Plasma.RunnerContext.Types types)'''
        def config(self):
            '''KConfigGroup Plasma.RunnerScript.config()'''
            return KConfigGroup()
        reloadConfiguration = pyqtSignal() # void reloadConfiguration() - signal
        createRunOptions = pyqtSignal() # void createRunOptions(QWidget *) - signal
        teardown = pyqtSignal() # void teardown() - signal
        prepare = pyqtSignal() # void prepare() - signal
        def package(self):
            '''Plasma.Package Plasma.RunnerScript.package()'''
            return Plasma.Package()
        def mainScript(self):
            '''QString Plasma.RunnerScript.mainScript()'''
            return QString()
        def run(self, search, action):
            '''void Plasma.RunnerScript.run(Plasma.RunnerContext search, Plasma.QueryMatch action)'''
        def match(self, search):
            '''void Plasma.RunnerScript.match(Plasma.RunnerContext search)'''
        def runner(self):
            '''Plasma.AbstractRunner Plasma.RunnerScript.runner()'''
            return Plasma.AbstractRunner()
        def setRunner(self, runner):
            '''void Plasma.RunnerScript.setRunner(Plasma.AbstractRunner runner)'''
    class LineEdit(QGraphicsProxyWidget):
        """"""
        def __init__(self, parent = None):
            '''void Plasma.LineEdit.__init__(QGraphicsWidget parent = None)'''
        focusChanged = pyqtSignal() # void focusChanged(bool) - signal
        def focusInEvent(self, event):
            '''void Plasma.LineEdit.focusInEvent(QFocusEvent event)'''
        def focusOutEvent(self, event):
            '''void Plasma.LineEdit.focusOutEvent(QFocusEvent event)'''
        def mousePressEvent(self, event):
            '''void Plasma.LineEdit.mousePressEvent(QGraphicsSceneMouseEvent event)'''
        def clickMessage(self):
            '''QString Plasma.LineEdit.clickMessage()'''
            return QString()
        def setClickMessage(self, message):
            '''void Plasma.LineEdit.setClickMessage(QString message)'''
        textChanged = pyqtSignal() # void textChanged(const QStringamp;) - signal
        def paint(self, painter, option, widget):
            '''void Plasma.LineEdit.paint(QPainter painter, QStyleOptionGraphicsItem option, QWidget widget)'''
        def changeEvent(self, event):
            '''void Plasma.LineEdit.changeEvent(QEvent event)'''
        def hoverLeaveEvent(self, event):
            '''void Plasma.LineEdit.hoverLeaveEvent(QGraphicsSceneHoverEvent event)'''
        def hoverEnterEvent(self, event):
            '''void Plasma.LineEdit.hoverEnterEvent(QGraphicsSceneHoverEvent event)'''
        def setNativeWidget(self, nativeWidget):
            '''void Plasma.LineEdit.setNativeWidget(KLineEdit nativeWidget)'''
        def isClearButtonShown(self):
            '''bool Plasma.LineEdit.isClearButtonShown()'''
            return bool()
        def setClearButtonShown(self, show):
            '''void Plasma.LineEdit.setClearButtonShown(bool show)'''
        textEdited = pyqtSignal() # void textEdited(const QStringamp;) - signal
        returnPressed = pyqtSignal() # void returnPressed() - signal
        editingFinished = pyqtSignal() # void editingFinished() - signal
        def nativeWidget(self):
            '''KLineEdit Plasma.LineEdit.nativeWidget()'''
            return KLineEdit()
        def styleSheet(self):
            '''QString Plasma.LineEdit.styleSheet()'''
            return QString()
        def setStyleSheet(self, stylesheet):
            '''void Plasma.LineEdit.setStyleSheet(QString stylesheet)'''
        def text(self):
            '''QString Plasma.LineEdit.text()'''
            return QString()
        def setText(self, text):
            '''void Plasma.LineEdit.setText(QString text)'''
    class WallpaperScript(Plasma.ScriptEngine):
        """"""
        def __init__(self, parent = None):
            '''void Plasma.WallpaperScript.__init__(QObject parent = None)'''
        def setUrls(self, urls):
            '''void Plasma.WallpaperScript.setUrls(KUrl.List urls)'''
        def description(self):
            '''KPluginInfo Plasma.WallpaperScript.description()'''
            return KPluginInfo()
        def urlDropped(self, url):
            '''void Plasma.WallpaperScript.urlDropped(KUrl url)'''
        def renderCompleted(self, image):
            '''void Plasma.WallpaperScript.renderCompleted(QImage image)'''
        def configNeedsSaving(self):
            '''void Plasma.WallpaperScript.configNeedsSaving()'''
        def update(self, exposedArea):
            '''void Plasma.WallpaperScript.update(QRectF exposedArea)'''
        def setContextualActions(self, actions):
            '''void Plasma.WallpaperScript.setContextualActions(list-of-QAction actions)'''
        def insertIntoCache(self, key, image):
            '''void Plasma.WallpaperScript.insertIntoCache(QString key, QImage image)'''
        def findInCache(self, key, image, lastModified = 0):
            '''bool Plasma.WallpaperScript.findInCache(QString key, QImage image, int lastModified = 0)'''
            return bool()
        def setUsingRenderingCache(self, useCache):
            '''void Plasma.WallpaperScript.setUsingRenderingCache(bool useCache)'''
        def render(self, sourceImagePath, size, resizeMethod = None, color = None):
            '''void Plasma.WallpaperScript.render(QString sourceImagePath, QSize size, Plasma.Wallpaper.ResizeMethod resizeMethod = Plasma.Wallpaper.ScaledResize, QColor color = QColor(0,0,0))'''
        def setConfigurationRequired(self, needsConfiguring, reason = QString()):
            '''void Plasma.WallpaperScript.setConfigurationRequired(bool needsConfiguring, QString reason = QString())'''
        def setTargetSizeHint(self, targetSize):
            '''void Plasma.WallpaperScript.setTargetSizeHint(QSizeF targetSize)'''
        def setResizeMethodHint(self, resizeMethod):
            '''void Plasma.WallpaperScript.setResizeMethodHint(Plasma.Wallpaper.ResizeMethod resizeMethod)'''
        def dataEngine(self, name):
            '''Plasma.DataEngine Plasma.WallpaperScript.dataEngine(QString name)'''
            return Plasma.DataEngine()
        def boundingRect(self):
            '''QRectF Plasma.WallpaperScript.boundingRect()'''
            return QRectF()
        def isInitialized(self):
            '''bool Plasma.WallpaperScript.isInitialized()'''
            return bool()
        def package(self):
            '''Plasma.Package Plasma.WallpaperScript.package()'''
            return Plasma.Package()
        def mainScript(self):
            '''QString Plasma.WallpaperScript.mainScript()'''
            return QString()
        def wheelEvent(self, event):
            '''void Plasma.WallpaperScript.wheelEvent(QGraphicsSceneWheelEvent event)'''
        def mouseReleaseEvent(self, event):
            '''void Plasma.WallpaperScript.mouseReleaseEvent(QGraphicsSceneMouseEvent event)'''
        def mousePressEvent(self, event):
            '''void Plasma.WallpaperScript.mousePressEvent(QGraphicsSceneMouseEvent event)'''
        def mouseMoveEvent(self, event):
            '''void Plasma.WallpaperScript.mouseMoveEvent(QGraphicsSceneMouseEvent event)'''
        def createConfigurationInterface(self, parent):
            '''QWidget Plasma.WallpaperScript.createConfigurationInterface(QWidget parent)'''
            return QWidget()
        def save(self, config):
            '''void Plasma.WallpaperScript.save(KConfigGroup config)'''
        def paint(self, painter, exposedRect):
            '''void Plasma.WallpaperScript.paint(QPainter painter, QRectF exposedRect)'''
        def initWallpaper(self, config):
            '''void Plasma.WallpaperScript.initWallpaper(KConfigGroup config)'''
        def wallpaper(self):
            '''Plasma.Wallpaper Plasma.WallpaperScript.wallpaper()'''
            return Plasma.Wallpaper()
        def setWallpaper(self, wallpaper):
            '''void Plasma.WallpaperScript.setWallpaper(Plasma.Wallpaper wallpaper)'''
    class Frame(QGraphicsWidget):
        """"""
        # Enum Plasma.Frame.Shadow
        Plain = 0
        Raised = 0
        Sunken = 0
    
        def __init__(self, parent = None):
            '''void Plasma.Frame.__init__(QGraphicsWidget parent = None)'''
        def changeEvent(self, event):
            '''void Plasma.Frame.changeEvent(QEvent event)'''
        def enabledBorders(self):
            '''Plasma.FrameSvg.EnabledBorders Plasma.Frame.enabledBorders()'''
            return Plasma.FrameSvg.EnabledBorders()
        def setEnabledBorders(self, borders):
            '''void Plasma.Frame.setEnabledBorders(Plasma.FrameSvg.EnabledBorders borders)'''
        def sizeHint(self, which, constraint):
            '''QSizeF Plasma.Frame.sizeHint(Qt.SizeHint which, QSizeF constraint)'''
            return QSizeF()
        def resizeEvent(self, event):
            '''void Plasma.Frame.resizeEvent(QGraphicsSceneResizeEvent event)'''
        def paint(self, painter, option, widget = None):
            '''void Plasma.Frame.paint(QPainter painter, QStyleOptionGraphicsItem option, QWidget widget = None)'''
        def nativeWidget(self):
            '''QWidget Plasma.Frame.nativeWidget()'''
            return QWidget()
        def styleSheet(self):
            '''QString Plasma.Frame.styleSheet()'''
            return QString()
        def setStyleSheet(self, stylesheet):
            '''void Plasma.Frame.setStyleSheet(QString stylesheet)'''
        def image(self):
            '''QString Plasma.Frame.image()'''
            return QString()
        def setImage(self, path):
            '''void Plasma.Frame.setImage(QString path)'''
        def text(self):
            '''QString Plasma.Frame.text()'''
            return QString()
        def setText(self, text):
            '''void Plasma.Frame.setText(QString text)'''
        def frameShadow(self):
            '''Plasma.Frame.Shadow Plasma.Frame.frameShadow()'''
            return Plasma.Frame.Shadow()
        def setFrameShadow(self, shadow):
            '''void Plasma.Frame.setFrameShadow(Plasma.Frame.Shadow shadow)'''
    class AccessManager(QObject):
        """"""
        remoteAppletUnannounced = pyqtSignal() # void remoteAppletUnannounced(Plasma::PackageMetadata) - signal
        remoteAppletAnnounced = pyqtSignal() # void remoteAppletAnnounced(Plasma::PackageMetadata) - signal
        finished = pyqtSignal() # void finished(Plasma::AccessAppletJob *) - signal
        def supportedProtocols(self):
            '''static QStringList Plasma.AccessManager.supportedProtocols()'''
            return QStringList()
        def remoteApplets(self):
            '''list-of-Plasma.PackageMetadata Plasma.AccessManager.remoteApplets()'''
            return [Plasma.PackageMetadata()]
        def accessRemoteApplet(self, location):
            '''Plasma.AccessAppletJob Plasma.AccessManager.accessRemoteApplet(KUrl location)'''
            return Plasma.AccessAppletJob()
        def self(self):
            '''static Plasma.AccessManager Plasma.AccessManager.self()'''
            return Plasma.AccessManager()
    class FrameSvg(Plasma.Svg):
        """"""
        # Enum Plasma.FrameSvg.EnabledBorder
        NoBorder = 0
        TopBorder = 0
        BottomBorder = 0
        LeftBorder = 0
        RightBorder = 0
        AllBorders = 0
    
        def __init__(self, parent = None):
            '''void Plasma.FrameSvg.__init__(QObject parent = None)'''
        def paintFrame(self, painter, target, source = QRectF()):
            '''void Plasma.FrameSvg.paintFrame(QPainter painter, QRectF target, QRectF source = QRectF())'''
        def paintFrame(self, painter, pos = None):
            '''void Plasma.FrameSvg.paintFrame(QPainter painter, QPointF pos = QPointF(0,0))'''
        def framePixmap(self):
            '''QPixmap Plasma.FrameSvg.framePixmap()'''
            return QPixmap()
        def clearCache(self):
            '''void Plasma.FrameSvg.clearCache()'''
        def cacheAllRenderedFrames(self):
            '''bool Plasma.FrameSvg.cacheAllRenderedFrames()'''
            return bool()
        def setCacheAllRenderedFrames(self, cache):
            '''void Plasma.FrameSvg.setCacheAllRenderedFrames(bool cache)'''
        def alphaMask(self):
            '''QPixmap Plasma.FrameSvg.alphaMask()'''
            return QPixmap()
        def mask(self):
            '''QRegion Plasma.FrameSvg.mask()'''
            return QRegion()
        def prefix(self):
            '''QString Plasma.FrameSvg.prefix()'''
            return QString()
        def hasElementPrefix(self, prefix):
            '''bool Plasma.FrameSvg.hasElementPrefix(QString prefix)'''
            return bool()
        def hasElementPrefix(self, location):
            '''bool Plasma.FrameSvg.hasElementPrefix(Plasma.Location location)'''
            return bool()
        def setElementPrefix(self, location):
            '''void Plasma.FrameSvg.setElementPrefix(Plasma.Location location)'''
        def setElementPrefix(self, prefix):
            '''void Plasma.FrameSvg.setElementPrefix(QString prefix)'''
        def contentsRect(self):
            '''QRectF Plasma.FrameSvg.contentsRect()'''
            return QRectF()
        def getMargins(self, left, top, right, bottom):
            '''void Plasma.FrameSvg.getMargins(float left, float top, float right, float bottom)'''
        def marginSize(self, edge):
            '''float Plasma.FrameSvg.marginSize(Plasma.MarginEdge edge)'''
            return float()
        def frameSize(self):
            '''QSizeF Plasma.FrameSvg.frameSize()'''
            return QSizeF()
        def resizeFrame(self, size):
            '''void Plasma.FrameSvg.resizeFrame(QSizeF size)'''
        def enabledBorders(self):
            '''Plasma.FrameSvg.EnabledBorders Plasma.FrameSvg.enabledBorders()'''
            return Plasma.FrameSvg.EnabledBorders()
        def setEnabledBorders(self, borders):
            '''void Plasma.FrameSvg.setEnabledBorders(Plasma.FrameSvg.EnabledBorders borders)'''
        def setImagePath(self, path):
            '''void Plasma.FrameSvg.setImagePath(QString path)'''
    class AppletProtectedThunk(Plasma.Applet):
        """"""
        def __init__(self):
            '''void Plasma.AppletProtectedThunk.__init__()'''
        def static_public_setConfigurationRequired(self, applet, needsConfiguring, reason = QString()):
            '''static void Plasma.AppletProtectedThunk.static_public_setConfigurationRequired(Plasma.Applet applet, bool needsConfiguring, QString reason = QString())'''
        def static_public_setHasConfigurationInterface(self, applet, hasInterface):
            '''static void Plasma.AppletProtectedThunk.static_public_setHasConfigurationInterface(Plasma.Applet applet, bool hasInterface)'''
    class ClientPinRequest(QObject):
        """"""
        changed = pyqtSignal() # void changed(Plasma::ClientPinRequest *) - signal
        def pin(self):
            '''QString Plasma.ClientPinRequest.pin()'''
            return QString()
        def setPin(self, pin):
            '''void Plasma.ClientPinRequest.setPin(QString pin)'''
        def description(self):
            '''QString Plasma.ClientPinRequest.description()'''
            return QString()
    class VideoWidget():
        """"""
        class Controls():
            """"""
            def __init__(self):
                '''Plasma.VideoWidget.Controls Plasma.VideoWidget.Controls.__init__()'''
                return Plasma.VideoWidget.Controls()
            def __init__(self):
                '''int Plasma.VideoWidget.Controls.__init__()'''
                return int()
            def __init__(self):
                '''void Plasma.VideoWidget.Controls.__init__()'''
            def __bool__(self):
                '''int Plasma.VideoWidget.Controls.__bool__()'''
                return int()
            def __ne__(self, f):
                '''bool Plasma.VideoWidget.Controls.__ne__(Plasma.VideoWidget.Controls f)'''
                return bool()
            def __eq__(self, f):
                '''bool Plasma.VideoWidget.Controls.__eq__(Plasma.VideoWidget.Controls f)'''
                return bool()
            def __invert__(self):
                '''Plasma.VideoWidget.Controls Plasma.VideoWidget.Controls.__invert__()'''
                return Plasma.VideoWidget.Controls()
            def __and__(self, mask):
                '''Plasma.VideoWidget.Controls Plasma.VideoWidget.Controls.__and__(int mask)'''
                return Plasma.VideoWidget.Controls()
            def __xor__(self, f):
                '''Plasma.VideoWidget.Controls Plasma.VideoWidget.Controls.__xor__(Plasma.VideoWidget.Controls f)'''
                return Plasma.VideoWidget.Controls()
            def __xor__(self, f):
                '''Plasma.VideoWidget.Controls Plasma.VideoWidget.Controls.__xor__(int f)'''
                return Plasma.VideoWidget.Controls()
            def __or__(self, f):
                '''Plasma.VideoWidget.Controls Plasma.VideoWidget.Controls.__or__(Plasma.VideoWidget.Controls f)'''
                return Plasma.VideoWidget.Controls()
            def __or__(self, f):
                '''Plasma.VideoWidget.Controls Plasma.VideoWidget.Controls.__or__(int f)'''
                return Plasma.VideoWidget.Controls()
            def __int__(self):
                '''int Plasma.VideoWidget.Controls.__int__()'''
                return int()
            def __ixor__(self, f):
                '''Plasma.VideoWidget.Controls Plasma.VideoWidget.Controls.__ixor__(Plasma.VideoWidget.Controls f)'''
                return Plasma.VideoWidget.Controls()
            def __ior__(self, f):
                '''Plasma.VideoWidget.Controls Plasma.VideoWidget.Controls.__ior__(Plasma.VideoWidget.Controls f)'''
                return Plasma.VideoWidget.Controls()
            def __iand__(self, mask):
                '''Plasma.VideoWidget.Controls Plasma.VideoWidget.Controls.__iand__(int mask)'''
                return Plasma.VideoWidget.Controls()
    class PackageMetadata():
        """"""
        def __init__(self, path = QString()):
            '''void Plasma.PackageMetadata.__init__(QString path = QString())'''
        def setIcon(self, icon):
            '''void Plasma.PackageMetadata.setIcon(QString icon)'''
        def icon(self):
            '''QString Plasma.PackageMetadata.icon()'''
            return QString()
        def setRemoteLocation(self):
            '''KUrl Plasma.PackageMetadata.setRemoteLocation()'''
            return KUrl()
        def remoteLocation(self):
            '''KUrl Plasma.PackageMetadata.remoteLocation()'''
            return KUrl()
        def setImplementationApi(self, api):
            '''void Plasma.PackageMetadata.setImplementationApi(QString api)'''
        def setPluginName(self, name):
            '''void Plasma.PackageMetadata.setPluginName(QString name)'''
        def setType(self, type):
            '''void Plasma.PackageMetadata.setType(QString type)'''
        def setRequiredVersion(self):
            '''QString Plasma.PackageMetadata.setRequiredVersion()'''
            return QString()
        def setCategory(self):
            '''QString Plasma.PackageMetadata.setCategory()'''
            return QString()
        def setApplication(self):
            '''QString Plasma.PackageMetadata.setApplication()'''
            return QString()
        def setLicense(self):
            '''QString Plasma.PackageMetadata.setLicense()'''
            return QString()
        def setWebsite(self):
            '''QString Plasma.PackageMetadata.setWebsite()'''
            return QString()
        def setVersion(self):
            '''QString Plasma.PackageMetadata.setVersion()'''
            return QString()
        def setEmail(self):
            '''QString Plasma.PackageMetadata.setEmail()'''
            return QString()
        def setAuthor(self):
            '''QString Plasma.PackageMetadata.setAuthor()'''
            return QString()
        def setServiceType(self):
            '''QString Plasma.PackageMetadata.setServiceType()'''
            return QString()
        def setKeywords(self, keywords):
            '''void Plasma.PackageMetadata.setKeywords(QStringList keywords)'''
        def setDescription(self):
            '''QString Plasma.PackageMetadata.setDescription()'''
            return QString()
        def setName(self):
            '''QString Plasma.PackageMetadata.setName()'''
            return QString()
        def type(self):
            '''QString Plasma.PackageMetadata.type()'''
            return QString()
        def implementationApi(self):
            '''QString Plasma.PackageMetadata.implementationApi()'''
            return QString()
        def pluginName(self):
            '''QString Plasma.PackageMetadata.pluginName()'''
            return QString()
        def requiredVersion(self):
            '''QString Plasma.PackageMetadata.requiredVersion()'''
            return QString()
        def category(self):
            '''QString Plasma.PackageMetadata.category()'''
            return QString()
        def application(self):
            '''QString Plasma.PackageMetadata.application()'''
            return QString()
        def license(self):
            '''QString Plasma.PackageMetadata.license()'''
            return QString()
        def website(self):
            '''QString Plasma.PackageMetadata.website()'''
            return QString()
        def version(self):
            '''QString Plasma.PackageMetadata.version()'''
            return QString()
        def email(self):
            '''QString Plasma.PackageMetadata.email()'''
            return QString()
        def author(self):
            '''QString Plasma.PackageMetadata.author()'''
            return QString()
        def serviceType(self):
            '''QString Plasma.PackageMetadata.serviceType()'''
            return QString()
        def keywords(self):
            '''QStringList Plasma.PackageMetadata.keywords()'''
            return QStringList()
        def description(self):
            '''QString Plasma.PackageMetadata.description()'''
            return QString()
        def name(self):
            '''QString Plasma.PackageMetadata.name()'''
            return QString()
        def read(self, filename):
            '''void Plasma.PackageMetadata.read(QString filename)'''
        def write(self, filename):
            '''void Plasma.PackageMetadata.write(QString filename)'''
        def isValid(self):
            '''bool Plasma.PackageMetadata.isValid()'''
            return bool()
    class AnimationDriver(QObject):
        """"""
        def __init__(self, parent = None):
            '''void Plasma.AnimationDriver.__init__(QObject parent = None)'''
        def itemSlideOut(self, progress, item, start, destination):
            '''void Plasma.AnimationDriver.itemSlideOut(float progress, QGraphicsItem item, QPoint start, QPoint destination)'''
        def itemSlideIn(self, progress, item, start, destination):
            '''void Plasma.AnimationDriver.itemSlideIn(float progress, QGraphicsItem item, QPoint start, QPoint destination)'''
        def itemActivated(self, progress, item):
            '''void Plasma.AnimationDriver.itemActivated(float progress, QGraphicsItem item)'''
        def itemDisappear(self, progress, item):
            '''void Plasma.AnimationDriver.itemDisappear(float progress, QGraphicsItem item)'''
        def itemAppear(self, progress, item):
            '''void Plasma.AnimationDriver.itemAppear(float progress, QGraphicsItem item)'''
        def elementDisappear(self, progress, pixmap):
            '''QPixmap Plasma.AnimationDriver.elementDisappear(float progress, QPixmap pixmap)'''
            return QPixmap()
        def elementAppear(self, progress, pixmap):
            '''QPixmap Plasma.AnimationDriver.elementAppear(float progress, QPixmap pixmap)'''
            return QPixmap()
        def elementAnimationCurve(self):
            '''Plasma.Animator.Animation Plasma.AnimationDriver.elementAnimationCurve()'''
            return Plasma.Animator.Animation()
        def movementAnimationCurve(self):
            '''Plasma.Animator.Movement Plasma.AnimationDriver.movementAnimationCurve()'''
            return Plasma.Animator.Movement()
        def animationCurve(self):
            '''Plasma.Animator.Animation Plasma.AnimationDriver.animationCurve()'''
            return Plasma.Animator.Animation()
        def elementAnimationDuration(self):
            '''Plasma.Animator.Animation Plasma.AnimationDriver.elementAnimationDuration()'''
            return Plasma.Animator.Animation()
        def movementAnimationDuration(self):
            '''Plasma.Animator.Movement Plasma.AnimationDriver.movementAnimationDuration()'''
            return Plasma.Animator.Movement()
        def animationDuration(self):
            '''Plasma.Animator.Animation Plasma.AnimationDriver.animationDuration()'''
            return Plasma.Animator.Animation()
        def elementAnimationFps(self):
            '''Plasma.Animator.Animation Plasma.AnimationDriver.elementAnimationFps()'''
            return Plasma.Animator.Animation()
        def movementAnimationFps(self):
            '''Plasma.Animator.Movement Plasma.AnimationDriver.movementAnimationFps()'''
            return Plasma.Animator.Movement()
        def animationFps(self):
            '''Plasma.Animator.Animation Plasma.AnimationDriver.animationFps()'''
            return Plasma.Animator.Animation()
    class Dialog():
        """"""
        class ResizeCorners():
            """"""
            def __init__(self):
                '''Plasma.Dialog.ResizeCorners Plasma.Dialog.ResizeCorners.__init__()'''
                return Plasma.Dialog.ResizeCorners()
            def __init__(self):
                '''int Plasma.Dialog.ResizeCorners.__init__()'''
                return int()
            def __init__(self):
                '''void Plasma.Dialog.ResizeCorners.__init__()'''
            def __bool__(self):
                '''int Plasma.Dialog.ResizeCorners.__bool__()'''
                return int()
            def __ne__(self, f):
                '''bool Plasma.Dialog.ResizeCorners.__ne__(Plasma.Dialog.ResizeCorners f)'''
                return bool()
            def __eq__(self, f):
                '''bool Plasma.Dialog.ResizeCorners.__eq__(Plasma.Dialog.ResizeCorners f)'''
                return bool()
            def __invert__(self):
                '''Plasma.Dialog.ResizeCorners Plasma.Dialog.ResizeCorners.__invert__()'''
                return Plasma.Dialog.ResizeCorners()
            def __and__(self, mask):
                '''Plasma.Dialog.ResizeCorners Plasma.Dialog.ResizeCorners.__and__(int mask)'''
                return Plasma.Dialog.ResizeCorners()
            def __xor__(self, f):
                '''Plasma.Dialog.ResizeCorners Plasma.Dialog.ResizeCorners.__xor__(Plasma.Dialog.ResizeCorners f)'''
                return Plasma.Dialog.ResizeCorners()
            def __xor__(self, f):
                '''Plasma.Dialog.ResizeCorners Plasma.Dialog.ResizeCorners.__xor__(int f)'''
                return Plasma.Dialog.ResizeCorners()
            def __or__(self, f):
                '''Plasma.Dialog.ResizeCorners Plasma.Dialog.ResizeCorners.__or__(Plasma.Dialog.ResizeCorners f)'''
                return Plasma.Dialog.ResizeCorners()
            def __or__(self, f):
                '''Plasma.Dialog.ResizeCorners Plasma.Dialog.ResizeCorners.__or__(int f)'''
                return Plasma.Dialog.ResizeCorners()
            def __int__(self):
                '''int Plasma.Dialog.ResizeCorners.__int__()'''
                return int()
            def __ixor__(self, f):
                '''Plasma.Dialog.ResizeCorners Plasma.Dialog.ResizeCorners.__ixor__(Plasma.Dialog.ResizeCorners f)'''
                return Plasma.Dialog.ResizeCorners()
            def __ior__(self, f):
                '''Plasma.Dialog.ResizeCorners Plasma.Dialog.ResizeCorners.__ior__(Plasma.Dialog.ResizeCorners f)'''
                return Plasma.Dialog.ResizeCorners()
            def __iand__(self, mask):
                '''Plasma.Dialog.ResizeCorners Plasma.Dialog.ResizeCorners.__iand__(int mask)'''
                return Plasma.Dialog.ResizeCorners()
    class ToolTipContent():
        """"""
        # Enum Plasma.ToolTipContent.ResourceType
        ImageResource = 0
        HtmlResource = 0
        CssResource = 0
    
        def __init__(self):
            '''void Plasma.ToolTipContent.__init__()'''
        def __init__(self, other):
            '''void Plasma.ToolTipContent.__init__(Plasma.ToolTipContent other)'''
        def __init__(self, mainText, subText, image = QPixmap()):
            '''void Plasma.ToolTipContent.__init__(QString mainText, QString subText, QPixmap image = QPixmap())'''
        def __init__(self, mainText, subText, icon):
            '''void Plasma.ToolTipContent.__init__(QString mainText, QString subText, QIcon icon)'''
        def isInstantPopup(self):
            '''bool Plasma.ToolTipContent.isInstantPopup()'''
            return bool()
        def setInstantPopup(self, enabled):
            '''void Plasma.ToolTipContent.setInstantPopup(bool enabled)'''
        def graphicsWidget(self):
            '''QGraphicsWidget Plasma.ToolTipContent.graphicsWidget()'''
            return QGraphicsWidget()
        def setGraphicsWidget(self, widget):
            '''void Plasma.ToolTipContent.setGraphicsWidget(QGraphicsWidget widget)'''
        def highlightWindows(self):
            '''bool Plasma.ToolTipContent.highlightWindows()'''
            return bool()
        def setHighlightWindows(self, highlight):
            '''void Plasma.ToolTipContent.setHighlightWindows(bool highlight)'''
        def isClickable(self):
            '''bool Plasma.ToolTipContent.isClickable()'''
            return bool()
        def setClickable(self, clickable):
            '''void Plasma.ToolTipContent.setClickable(bool clickable)'''
        def registerResources(self, document):
            '''void Plasma.ToolTipContent.registerResources(QTextDocument document)'''
        def addResource(self, type, path, resource):
            '''void Plasma.ToolTipContent.addResource(Plasma.ToolTipContent.ResourceType type, QUrl path, QVariant resource)'''
        def autohide(self):
            '''bool Plasma.ToolTipContent.autohide()'''
            return bool()
        def setAutohide(self, autohide):
            '''void Plasma.ToolTipContent.setAutohide(bool autohide)'''
        def windowsToPreview(self):
            '''unknown-type Plasma.ToolTipContent.windowsToPreview()'''
            return unknown-type()
        def setWindowsToPreview(self, ids):
            '''void Plasma.ToolTipContent.setWindowsToPreview(unknown-type ids)'''
        def windowToPreview(self):
            '''int Plasma.ToolTipContent.windowToPreview()'''
            return int()
        def setWindowToPreview(self, id):
            '''void Plasma.ToolTipContent.setWindowToPreview(int id)'''
        def image(self):
            '''QPixmap Plasma.ToolTipContent.image()'''
            return QPixmap()
        def setImage(self, image):
            '''void Plasma.ToolTipContent.setImage(QPixmap image)'''
        def setImage(self, icon):
            '''void Plasma.ToolTipContent.setImage(QIcon icon)'''
        def subText(self):
            '''QString Plasma.ToolTipContent.subText()'''
            return QString()
        def setSubText(self, text):
            '''void Plasma.ToolTipContent.setSubText(QString text)'''
        def mainText(self):
            '''QString Plasma.ToolTipContent.mainText()'''
            return QString()
        def setMainText(self, text):
            '''void Plasma.ToolTipContent.setMainText(QString text)'''
        def isEmpty(self):
            '''bool Plasma.ToolTipContent.isEmpty()'''
            return bool()
    class TabBar(QGraphicsWidget):
        """"""
        def __init__(self, parent = None):
            '''void Plasma.TabBar.__init__(QGraphicsWidget parent = None)'''
        def isTabHighlighted(self, index):
            '''bool Plasma.TabBar.isTabHighlighted(int index)'''
            return bool()
        def setTabHighlighted(self, index, highlight):
            '''void Plasma.TabBar.setTabHighlighted(int index, bool highlight)'''
        def lastPositionWidget(self):
            '''QGraphicsWidget Plasma.TabBar.lastPositionWidget()'''
            return QGraphicsWidget()
        def setLastPositionWidget(self, widget):
            '''void Plasma.TabBar.setLastPositionWidget(QGraphicsWidget widget)'''
        def firstPositionWidget(self):
            '''QGraphicsWidget Plasma.TabBar.firstPositionWidget()'''
            return QGraphicsWidget()
        def setFirstPositionWidget(self, widget):
            '''void Plasma.TabBar.setFirstPositionWidget(QGraphicsWidget widget)'''
        def changeEvent(self, event):
            '''void Plasma.TabBar.changeEvent(QEvent event)'''
        def tabAt(self, index):
            '''QGraphicsLayoutItem Plasma.TabBar.tabAt(int index)'''
            return QGraphicsLayoutItem()
        def takeTab(self, index):
            '''QGraphicsLayoutItem Plasma.TabBar.takeTab(int index)'''
            return QGraphicsLayoutItem()
        def resizeEvent(self, event):
            '''void Plasma.TabBar.resizeEvent(QGraphicsSceneResizeEvent event)'''
        def wheelEvent(self, event):
            '''void Plasma.TabBar.wheelEvent(QGraphicsSceneWheelEvent event)'''
        currentChanged = pyqtSignal() # void currentChanged(int) - signal
        def setCurrentIndex(self, index):
            '''void Plasma.TabBar.setCurrentIndex(int index)'''
        def nativeWidget(self):
            '''KTabBar Plasma.TabBar.nativeWidget()'''
            return KTabBar()
        def styleSheet(self):
            '''QString Plasma.TabBar.styleSheet()'''
            return QString()
        def setStyleSheet(self, stylesheet):
            '''void Plasma.TabBar.setStyleSheet(QString stylesheet)'''
        def isTabBarShown(self):
            '''bool Plasma.TabBar.isTabBarShown()'''
            return bool()
        def setTabBarShown(self, show):
            '''void Plasma.TabBar.setTabBarShown(bool show)'''
        def tabIcon(self, index):
            '''QIcon Plasma.TabBar.tabIcon(int index)'''
            return QIcon()
        def setTabIcon(self, index, icon):
            '''void Plasma.TabBar.setTabIcon(int index, QIcon icon)'''
        def tabText(self, index):
            '''QString Plasma.TabBar.tabText(int index)'''
            return QString()
        def setTabText(self, index, label):
            '''void Plasma.TabBar.setTabText(int index, QString label)'''
        def count(self):
            '''int Plasma.TabBar.count()'''
            return int()
        def currentIndex(self):
            '''int Plasma.TabBar.currentIndex()'''
            return int()
        def removeTab(self, index):
            '''void Plasma.TabBar.removeTab(int index)'''
        def addTab(self, icon, label, content = None):
            '''int Plasma.TabBar.addTab(QIcon icon, QString label, QGraphicsLayoutItem content = None)'''
            return int()
        def addTab(self, label, content = None):
            '''int Plasma.TabBar.addTab(QString label, QGraphicsLayoutItem content = None)'''
            return int()
        def insertTab(self, index, icon, label, content = None):
            '''int Plasma.TabBar.insertTab(int index, QIcon icon, QString label, QGraphicsLayoutItem content = None)'''
            return int()
        def insertTab(self, index, label, content = None):
            '''int Plasma.TabBar.insertTab(int index, QString label, QGraphicsLayoutItem content = None)'''
            return int()
    class PackageStructure(QObject):
        """"""
        def __init__(self, parent = None, type = None):
            '''void Plasma.PackageStructure.__init__(QObject parent = None, QString type = i18ncA non-functional packageInvalid)'''
        def setContentsPrefixPaths(self, prefixPaths):
            '''void Plasma.PackageStructure.setContentsPrefixPaths(QStringList prefixPaths)'''
        def contentsPrefixPaths(self):
            '''QStringList Plasma.PackageStructure.contentsPrefixPaths()'''
            return QStringList()
        def searchPath(self, key):
            '''QStringList Plasma.PackageStructure.searchPath(str key)'''
            return QStringList()
        def removeDefinition(self, key):
            '''void Plasma.PackageStructure.removeDefinition(str key)'''
        def pathChanged(self):
            '''void Plasma.PackageStructure.pathChanged()'''
        def setDefaultPackageRoot(self, packageRoot):
            '''void Plasma.PackageStructure.setDefaultPackageRoot(QString packageRoot)'''
        def setContentsPrefix(self, prefix):
            '''void Plasma.PackageStructure.setContentsPrefix(QString prefix)'''
        def setAllowExternalPaths(self, allow):
            '''void Plasma.PackageStructure.setAllowExternalPaths(bool allow)'''
        newWidgetBrowserFinished = pyqtSignal() # void newWidgetBrowserFinished() - signal
        def allowExternalPaths(self):
            '''bool Plasma.PackageStructure.allowExternalPaths()'''
            return bool()
        def setServicePrefix(self, servicePrefix):
            '''void Plasma.PackageStructure.setServicePrefix(QString servicePrefix)'''
        def servicePrefix(self):
            '''QString Plasma.PackageStructure.servicePrefix()'''
            return QString()
        def defaultPackageRoot(self):
            '''QString Plasma.PackageStructure.defaultPackageRoot()'''
            return QString()
        def contentsPrefix(self):
            '''QString Plasma.PackageStructure.contentsPrefix()'''
            return QString()
        def createNewWidgetBrowser(self, parent = None):
            '''void Plasma.PackageStructure.createNewWidgetBrowser(QWidget parent = None)'''
        def uninstallPackage(self, packageName, packageRoot):
            '''bool Plasma.PackageStructure.uninstallPackage(QString packageName, QString packageRoot)'''
            return bool()
        def installPackage(self, archivePath, packageRoot):
            '''bool Plasma.PackageStructure.installPackage(QString archivePath, QString packageRoot)'''
            return bool()
        def write(self, config):
            '''void Plasma.PackageStructure.write(KConfigBase config)'''
        def read(self, config):
            '''void Plasma.PackageStructure.read(KConfigBase config)'''
        def setPath(self, path):
            '''void Plasma.PackageStructure.setPath(QString path)'''
        def mimetypes(self, key):
            '''QStringList Plasma.PackageStructure.mimetypes(str key)'''
            return QStringList()
        def setMimetypes(self, key, mimetypes):
            '''void Plasma.PackageStructure.setMimetypes(str key, QStringList mimetypes)'''
        def setDefaultMimetypes(self, mimetypes):
            '''void Plasma.PackageStructure.setDefaultMimetypes(QStringList mimetypes)'''
        def isRequired(self, key):
            '''bool Plasma.PackageStructure.isRequired(str key)'''
            return bool()
        def setRequired(self, key, required):
            '''void Plasma.PackageStructure.setRequired(str key, bool required)'''
        def name(self, key):
            '''QString Plasma.PackageStructure.name(str key)'''
            return QString()
        def entryList(self, key):
            '''QStringList Plasma.PackageStructure.entryList(str key)'''
            return QStringList()
        def path(self, key):
            '''QString Plasma.PackageStructure.path(str key)'''
            return QString()
        def path(self):
            '''QString Plasma.PackageStructure.path()'''
            return QString()
        def addFileDefinition(self, key, path, name):
            '''void Plasma.PackageStructure.addFileDefinition(str key, QString path, QString name)'''
        def addDirectoryDefinition(self, key, path, name):
            '''void Plasma.PackageStructure.addDirectoryDefinition(str key, QString path, QString name)'''
        def requiredFiles(self):
            '''unknown-type Plasma.PackageStructure.requiredFiles()'''
            return unknown-type()
        def files(self):
            '''unknown-type Plasma.PackageStructure.files()'''
            return unknown-type()
        def requiredDirectories(self):
            '''unknown-type Plasma.PackageStructure.requiredDirectories()'''
            return unknown-type()
        def directories(self):
            '''unknown-type Plasma.PackageStructure.directories()'''
            return unknown-type()
        def type(self):
            '''QString Plasma.PackageStructure.type()'''
            return QString()
        def load(self, packageFormat):
            '''static unknown-type Plasma.PackageStructure.load(QString packageFormat)'''
            return unknown-type()
    class Animator(QObject):
        """"""
        # Enum Plasma.Animator.Movement
        SlideInMovement = 0
        SlideOutMovement = 0
        FastSlideInMovement = 0
        FastSlideOutMovement = 0
    
        # Enum Plasma.Animator.CurveShape
        EaseInCurve = 0
        EaseOutCurve = 0
        EaseInOutCurve = 0
        LinearCurve = 0
        PendularCurve = 0
    
        # Enum Plasma.Animator.Animation
        AppearAnimation = 0
        DisappearAnimation = 0
        ActivateAnimation = 0
        FadeAnimation = 0
        GrowAnimation = 0
        PulseAnimation = 0
        RotationAnimation = 0
        RotationStackedAnimation = 0
        SlideAnimation = 0
        GeometryAnimation = 0
        ZoomAnimation = 0
        PixmapTransitionAnimation = 0
        WaterAnimation = 0
        LastAnimation = 0
    
        def create(self, animationName, parent = None):
            '''static Plasma.Animation Plasma.Animator.create(QString animationName, QObject parent = None)'''
            return Plasma.Animation()
        def create(self, type):
            '''static QEasingCurve Plasma.Animator.create(Plasma.Animator.CurveShape type)'''
            return QEasingCurve()
        scrollStateChanged = pyqtSignal() # void scrollStateChanged(QGraphicsWidget *,QAbstractAnimation::State,QAbstractAnimation::State) - signal
        def unregisterScrollingManager(self, widget):
            '''void Plasma.Animator.unregisterScrollingManager(QGraphicsWidget widget)'''
        def registerScrollingManager(self, widget):
            '''void Plasma.Animator.registerScrollingManager(QGraphicsWidget widget)'''
        def timerEvent(self, event):
            '''void Plasma.Animator.timerEvent(QTimerEvent event)'''
        customAnimationFinished = pyqtSignal() # void customAnimationFinished(int) - signal
        elementAnimationFinished = pyqtSignal() # void elementAnimationFinished(int) - signal
        movementFinished = pyqtSignal() # void movementFinished(QGraphicsItem *) - signal
        animationFinished = pyqtSignal() # void animationFinished(QGraphicsItem *,Plasma::Animator::Animation) - signal
        def isAnimating(self):
            '''bool Plasma.Animator.isAnimating()'''
            return bool()
        def currentPixmap(self, id):
            '''QPixmap Plasma.Animator.currentPixmap(int id)'''
            return QPixmap()
        def setInitialPixmap(self, id, pixmap):
            '''void Plasma.Animator.setInitialPixmap(int id, QPixmap pixmap)'''
        def stopElementAnimation(self, id):
            '''void Plasma.Animator.stopElementAnimation(int id)'''
        def animateElement(self, obj):
            '''Plasma.Animator.Animation Plasma.Animator.animateElement(QGraphicsItem obj)'''
            return Plasma.Animator.Animation()
        def stopCustomAnimation(self, id):
            '''void Plasma.Animator.stopCustomAnimation(int id)'''
        def customAnimation(self, frames, duration, curve, receiver, method):
            '''int Plasma.Animator.customAnimation(int frames, int duration, Plasma.Animator.CurveShape curve, QObject receiver, str method)'''
            return int()
        def stopItemMovement(self, id):
            '''void Plasma.Animator.stopItemMovement(int id)'''
        def moveItem(self, item, movement, destination):
            '''int Plasma.Animator.moveItem(QGraphicsItem item, Plasma.Animator.Movement movement, QPoint destination)'''
            return int()
        def stopItemAnimation(self, id):
            '''void Plasma.Animator.stopItemAnimation(int id)'''
        def animateItem(self, item, anim):
            '''int Plasma.Animator.animateItem(QGraphicsItem item, Plasma.Animator.Animation anim)'''
            return int()
        def self(self):
            '''static Plasma.Animator Plasma.Animator.self()'''
            return Plasma.Animator()
    class Applet():
        """"""
        class BackgroundHints():
            """"""
            def __init__(self):
                '''Plasma.Applet.BackgroundHints Plasma.Applet.BackgroundHints.__init__()'''
                return Plasma.Applet.BackgroundHints()
            def __init__(self):
                '''int Plasma.Applet.BackgroundHints.__init__()'''
                return int()
            def __init__(self):
                '''void Plasma.Applet.BackgroundHints.__init__()'''
            def __bool__(self):
                '''int Plasma.Applet.BackgroundHints.__bool__()'''
                return int()
            def __ne__(self, f):
                '''bool Plasma.Applet.BackgroundHints.__ne__(Plasma.Applet.BackgroundHints f)'''
                return bool()
            def __eq__(self, f):
                '''bool Plasma.Applet.BackgroundHints.__eq__(Plasma.Applet.BackgroundHints f)'''
                return bool()
            def __invert__(self):
                '''Plasma.Applet.BackgroundHints Plasma.Applet.BackgroundHints.__invert__()'''
                return Plasma.Applet.BackgroundHints()
            def __and__(self, mask):
                '''Plasma.Applet.BackgroundHints Plasma.Applet.BackgroundHints.__and__(int mask)'''
                return Plasma.Applet.BackgroundHints()
            def __xor__(self, f):
                '''Plasma.Applet.BackgroundHints Plasma.Applet.BackgroundHints.__xor__(Plasma.Applet.BackgroundHints f)'''
                return Plasma.Applet.BackgroundHints()
            def __xor__(self, f):
                '''Plasma.Applet.BackgroundHints Plasma.Applet.BackgroundHints.__xor__(int f)'''
                return Plasma.Applet.BackgroundHints()
            def __or__(self, f):
                '''Plasma.Applet.BackgroundHints Plasma.Applet.BackgroundHints.__or__(Plasma.Applet.BackgroundHints f)'''
                return Plasma.Applet.BackgroundHints()
            def __or__(self, f):
                '''Plasma.Applet.BackgroundHints Plasma.Applet.BackgroundHints.__or__(int f)'''
                return Plasma.Applet.BackgroundHints()
            def __int__(self):
                '''int Plasma.Applet.BackgroundHints.__int__()'''
                return int()
            def __ixor__(self, f):
                '''Plasma.Applet.BackgroundHints Plasma.Applet.BackgroundHints.__ixor__(Plasma.Applet.BackgroundHints f)'''
                return Plasma.Applet.BackgroundHints()
            def __ior__(self, f):
                '''Plasma.Applet.BackgroundHints Plasma.Applet.BackgroundHints.__ior__(Plasma.Applet.BackgroundHints f)'''
                return Plasma.Applet.BackgroundHints()
            def __iand__(self, mask):
                '''Plasma.Applet.BackgroundHints Plasma.Applet.BackgroundHints.__iand__(int mask)'''
                return Plasma.Applet.BackgroundHints()
    class Slider(QGraphicsProxyWidget):
        """"""
        def __init__(self, parent = None):
            '''void Plasma.Slider.__init__(QGraphicsWidget parent = None)'''
        valueChanged = pyqtSignal() # void valueChanged(int) - signal
        sliderMoved = pyqtSignal() # void sliderMoved(int) - signal
        def setOrientation(self, orientation):
            '''void Plasma.Slider.setOrientation(Qt.Orientation orientation)'''
        def setValue(self, value):
            '''void Plasma.Slider.setValue(int value)'''
        def setRange(self, minimum, maximum):
            '''void Plasma.Slider.setRange(int minimum, int maximum)'''
        def setMinimum(self, minimum):
            '''void Plasma.Slider.setMinimum(int minimum)'''
        def setMaximum(self, maximum):
            '''void Plasma.Slider.setMaximum(int maximum)'''
        def wheelEvent(self, event):
            '''void Plasma.Slider.wheelEvent(QGraphicsSceneWheelEvent event)'''
        def paint(self, painter, option, widget):
            '''void Plasma.Slider.paint(QPainter painter, QStyleOptionGraphicsItem option, QWidget widget)'''
        def nativeWidget(self):
            '''QSlider Plasma.Slider.nativeWidget()'''
            return QSlider()
        def styleSheet(self):
            '''QString Plasma.Slider.styleSheet()'''
            return QString()
        def setStyleSheet(self, stylesheet):
            '''void Plasma.Slider.setStyleSheet(QString stylesheet)'''
        def orientation(self):
            '''Qt.Orientation Plasma.Slider.orientation()'''
            return Qt.Orientation()
        def value(self):
            '''int Plasma.Slider.value()'''
            return int()
        def minimum(self):
            '''int Plasma.Slider.minimum()'''
            return int()
        def maximum(self):
            '''int Plasma.Slider.maximum()'''
            return int()
    class DataEngine(QObject):
        """"""
        def __init__(self, parent = None, service = None):
            '''void Plasma.DataEngine.__init__(QObject parent = None, unknown-type service = KService.Ptr(0))'''
        def __init__(self, parent, args):
            '''void Plasma.DataEngine.__init__(QObject parent, list-of-QVariant args)'''
        def setStorageEnabled(self, source, store):
            '''void Plasma.DataEngine.setStorageEnabled(QString source, bool store)'''
        def setDefaultService(self, serviceName):
            '''void Plasma.DataEngine.setDefaultService(QString serviceName)'''
        def createDefaultService(self, parent = None):
            '''Plasma.Service Plasma.DataEngine.createDefaultService(QObject parent = None)'''
            return Plasma.Service()
        def forceImmediateUpdateOfAllVisualizations(self):
            '''void Plasma.DataEngine.forceImmediateUpdateOfAllVisualizations()'''
        def updateAllSources(self):
            '''void Plasma.DataEngine.updateAllSources()'''
        def removeSource(self, source):
            '''void Plasma.DataEngine.removeSource(QString source)'''
        def scheduleSourcesUpdated(self):
            '''void Plasma.DataEngine.scheduleSourcesUpdated()'''
        def setIcon(self, icon):
            '''void Plasma.DataEngine.setIcon(QString icon)'''
        def setName(self, name):
            '''void Plasma.DataEngine.setName(QString name)'''
        def timerEvent(self, event):
            '''void Plasma.DataEngine.timerEvent(QTimerEvent event)'''
        def containerDict(self):
            '''unknown-type Plasma.DataEngine.containerDict()'''
            return unknown-type()
        def setValid(self, valid):
            '''void Plasma.DataEngine.setValid(bool valid)'''
        def removeAllSources(self):
            '''void Plasma.DataEngine.removeAllSources()'''
        def setPollingInterval(self, frequency):
            '''void Plasma.DataEngine.setPollingInterval(int frequency)'''
        def minimumPollingInterval(self):
            '''int Plasma.DataEngine.minimumPollingInterval()'''
            return int()
        def setMinimumPollingInterval(self, minimumMs):
            '''void Plasma.DataEngine.setMinimumPollingInterval(int minimumMs)'''
        def setMaxSourceCount(self, limit):
            '''void Plasma.DataEngine.setMaxSourceCount(int limit)'''
        def addSource(self, source):
            '''void Plasma.DataEngine.addSource(Plasma.DataContainer source)'''
        def removeData(self, source, key):
            '''void Plasma.DataEngine.removeData(QString source, QString key)'''
        def removeAllData(self, source):
            '''void Plasma.DataEngine.removeAllData(QString source)'''
        def setData(self, source, value):
            '''void Plasma.DataEngine.setData(QString source, QVariant value)'''
        def setData(self, source, key, value):
            '''void Plasma.DataEngine.setData(QString source, QString key, QVariant value)'''
        def setData(self, source, data):
            '''void Plasma.DataEngine.setData(QString source, dict-of-QString-QVariant data)'''
        def updateSourceEvent(self, source):
            '''bool Plasma.DataEngine.updateSourceEvent(QString source)'''
            return bool()
        def sourceRequestEvent(self, source):
            '''bool Plasma.DataEngine.sourceRequestEvent(QString source)'''
            return bool()
        sourceRemoved = pyqtSignal() # void sourceRemoved(const QStringamp;) - signal
        sourceAdded = pyqtSignal() # void sourceAdded(const QStringamp;) - signal
        def pluginName(self):
            '''QString Plasma.DataEngine.pluginName()'''
            return QString()
        def package(self):
            '''Plasma.Package Plasma.DataEngine.package()'''
            return Plasma.Package()
        def icon(self):
            '''QString Plasma.DataEngine.icon()'''
            return QString()
        def maxSourceCount(self):
            '''int Plasma.DataEngine.maxSourceCount()'''
            return int()
        def isEmpty(self):
            '''bool Plasma.DataEngine.isEmpty()'''
            return bool()
        def isValid(self):
            '''bool Plasma.DataEngine.isValid()'''
            return bool()
        def query(self, source):
            '''dict-of-QString-QVariant Plasma.DataEngine.query(QString source)'''
            return dict-of-QString-QVariant()
        def containerForSource(self, source):
            '''Plasma.DataContainer Plasma.DataEngine.containerForSource(QString source)'''
            return Plasma.DataContainer()
        def disconnectSource(self, source, visualization):
            '''void Plasma.DataEngine.disconnectSource(QString source, QObject visualization)'''
        def connectAllSources(self, visualization, pollingInterval = 0, intervalAlignment = None):
            '''void Plasma.DataEngine.connectAllSources(QObject visualization, int pollingInterval = 0, Plasma.IntervalAlignment intervalAlignment = Plasma.NoAlignment)'''
        def connectSource(self, source, visualization, pollingInterval = 0, intervalAlignment = None):
            '''void Plasma.DataEngine.connectSource(QString source, QObject visualization, int pollingInterval = 0, Plasma.IntervalAlignment intervalAlignment = Plasma.NoAlignment)'''
        def name(self):
            '''QString Plasma.DataEngine.name()'''
            return QString()
        def serviceForSource(self, source):
            '''Plasma.Service Plasma.DataEngine.serviceForSource(QString source)'''
            return Plasma.Service()
        def sources(self):
            '''QStringList Plasma.DataEngine.sources()'''
            return QStringList()
        def init(self):
            '''void Plasma.DataEngine.init()'''
    class Constraints():
        """"""
        def __init__(self):
            '''Plasma.Constraints Plasma.Constraints.__init__()'''
            return Plasma.Constraints()
        def __init__(self):
            '''int Plasma.Constraints.__init__()'''
            return int()
        def __init__(self):
            '''void Plasma.Constraints.__init__()'''
        def __bool__(self):
            '''int Plasma.Constraints.__bool__()'''
            return int()
        def __ne__(self, f):
            '''bool Plasma.Constraints.__ne__(Plasma.Constraints f)'''
            return bool()
        def __eq__(self, f):
            '''bool Plasma.Constraints.__eq__(Plasma.Constraints f)'''
            return bool()
        def __invert__(self):
            '''Plasma.Constraints Plasma.Constraints.__invert__()'''
            return Plasma.Constraints()
        def __and__(self, mask):
            '''Plasma.Constraints Plasma.Constraints.__and__(int mask)'''
            return Plasma.Constraints()
        def __xor__(self, f):
            '''Plasma.Constraints Plasma.Constraints.__xor__(Plasma.Constraints f)'''
            return Plasma.Constraints()
        def __xor__(self, f):
            '''Plasma.Constraints Plasma.Constraints.__xor__(int f)'''
            return Plasma.Constraints()
        def __or__(self, f):
            '''Plasma.Constraints Plasma.Constraints.__or__(Plasma.Constraints f)'''
            return Plasma.Constraints()
        def __or__(self, f):
            '''Plasma.Constraints Plasma.Constraints.__or__(int f)'''
            return Plasma.Constraints()
        def __int__(self):
            '''int Plasma.Constraints.__int__()'''
            return int()
        def __ixor__(self, f):
            '''Plasma.Constraints Plasma.Constraints.__ixor__(Plasma.Constraints f)'''
            return Plasma.Constraints()
        def __ior__(self, f):
            '''Plasma.Constraints Plasma.Constraints.__ior__(Plasma.Constraints f)'''
            return Plasma.Constraints()
        def __iand__(self, mask):
            '''Plasma.Constraints Plasma.Constraints.__iand__(int mask)'''
            return Plasma.Constraints()
    class ToolButton(QGraphicsProxyWidget):
        """"""
        def __init__(self, parent = None):
            '''void Plasma.ToolButton.__init__(QGraphicsWidget parent = None)'''
        def itemChange(self, change, value):
            '''QVariant Plasma.ToolButton.itemChange(QGraphicsItem.GraphicsItemChange change, QVariant value)'''
            return QVariant()
        def setDown(self, down):
            '''void Plasma.ToolButton.setDown(bool down)'''
        def sizeHint(self, which, constraint):
            '''QSizeF Plasma.ToolButton.sizeHint(Qt.SizeHint which, QSizeF constraint)'''
            return QSizeF()
        def changeEvent(self, event):
            '''void Plasma.ToolButton.changeEvent(QEvent event)'''
        released = pyqtSignal() # void released() - signal
        pressed = pyqtSignal() # void pressed() - signal
        def isDown(self):
            '''bool Plasma.ToolButton.isDown()'''
            return bool()
        def hoverLeaveEvent(self, event):
            '''void Plasma.ToolButton.hoverLeaveEvent(QGraphicsSceneHoverEvent event)'''
        def hoverEnterEvent(self, event):
            '''void Plasma.ToolButton.hoverEnterEvent(QGraphicsSceneHoverEvent event)'''
        def resizeEvent(self, event):
            '''void Plasma.ToolButton.resizeEvent(QGraphicsSceneResizeEvent event)'''
        def paint(self, painter, option, widget = None):
            '''void Plasma.ToolButton.paint(QPainter painter, QStyleOptionGraphicsItem option, QWidget widget = None)'''
        clicked = pyqtSignal() # void clicked() - signal
        def nativeWidget(self):
            '''QToolButton Plasma.ToolButton.nativeWidget()'''
            return QToolButton()
        def icon(self):
            '''QIcon Plasma.ToolButton.icon()'''
            return QIcon()
        def setIcon(self, icon):
            '''void Plasma.ToolButton.setIcon(QIcon icon)'''
        def action(self):
            '''QAction Plasma.ToolButton.action()'''
            return QAction()
        def setAction(self, action):
            '''void Plasma.ToolButton.setAction(QAction action)'''
        def styleSheet(self):
            '''QString Plasma.ToolButton.styleSheet()'''
            return QString()
        def setStyleSheet(self, stylesheet):
            '''void Plasma.ToolButton.setStyleSheet(QString stylesheet)'''
        def image(self):
            '''QString Plasma.ToolButton.image()'''
            return QString()
        def setImage(self, path):
            '''void Plasma.ToolButton.setImage(QString path)'''
        def setImage(self, path, elementid):
            '''void Plasma.ToolButton.setImage(QString path, QString elementid)'''
        def text(self):
            '''QString Plasma.ToolButton.text()'''
            return QString()
        def setText(self, text):
            '''void Plasma.ToolButton.setText(QString text)'''
        def autoRaise(self):
            '''bool Plasma.ToolButton.autoRaise()'''
            return bool()
        def setAutoRaise(self, raise_):
            '''void Plasma.ToolButton.setAutoRaise(bool raise)'''
    class ContainmentActionsPluginsConfig():
        """"""
        def __init__(self):
            '''void Plasma.ContainmentActionsPluginsConfig.__init__()'''
        def __init__(self, other):
            '''void Plasma.ContainmentActionsPluginsConfig.__init__(Plasma.ContainmentActionsPluginsConfig other)'''
        def addPlugin(self, trigger, name):
            '''void Plasma.ContainmentActionsPluginsConfig.addPlugin(QEvent trigger, QString name)'''
        def addPlugin(self, modifiers, button, name):
            '''void Plasma.ContainmentActionsPluginsConfig.addPlugin(Qt.KeyboardModifiers modifiers, Qt.MouseButton button, QString name)'''
        def addPlugin(self, modifiers, wheelDirection, name):
            '''void Plasma.ContainmentActionsPluginsConfig.addPlugin(Qt.KeyboardModifiers modifiers, Qt.Orientation wheelDirection, QString name)'''
        def remove(self, trigger):
            '''void Plasma.ContainmentActionsPluginsConfig.remove(QEvent trigger)'''
        def clear(self):
            '''void Plasma.ContainmentActionsPluginsConfig.clear()'''
    class ExtenderItem(QGraphicsWidget):
        """"""
        def __init__(self, hostExtender, extenderItemId = 0):
            '''void Plasma.ExtenderItem.__init__(Plasma.Extender hostExtender, int extenderItemId = 0)'''
        def isTransient(self):
            '''bool Plasma.ExtenderItem.isTransient()'''
            return bool()
        def setTransient(self, transient):
            '''void Plasma.ExtenderItem.setTransient(bool transient)'''
        destroyed = pyqtSignal() # void destroyed(Plasma::ExtenderItem *) - signal
        def sizeHint(self, which, constraint):
            '''QSizeF Plasma.ExtenderItem.sizeHint(Qt.SizeHint which, QSizeF constraint)'''
            return QSizeF()
        def sceneEventFilter(self, watched, event):
            '''bool Plasma.ExtenderItem.sceneEventFilter(QGraphicsItem watched, QEvent event)'''
            return bool()
        def hoverLeaveEvent(self, event):
            '''void Plasma.ExtenderItem.hoverLeaveEvent(QGraphicsSceneHoverEvent event)'''
        def hoverMoveEvent(self, event):
            '''void Plasma.ExtenderItem.hoverMoveEvent(QGraphicsSceneHoverEvent event)'''
        def mouseReleaseEvent(self, event):
            '''void Plasma.ExtenderItem.mouseReleaseEvent(QGraphicsSceneMouseEvent event)'''
        def mouseMoveEvent(self, event):
            '''void Plasma.ExtenderItem.mouseMoveEvent(QGraphicsSceneMouseEvent event)'''
        def mouseDoubleClickEvent(self, event):
            '''void Plasma.ExtenderItem.mouseDoubleClickEvent(QGraphicsSceneMouseEvent event)'''
        def mousePressEvent(self, event):
            '''void Plasma.ExtenderItem.mousePressEvent(QGraphicsSceneMouseEvent event)'''
        def resizeEvent(self, event):
            '''void Plasma.ExtenderItem.resizeEvent(QGraphicsSceneResizeEvent event)'''
        def moveEvent(self, event):
            '''void Plasma.ExtenderItem.moveEvent(QGraphicsSceneMoveEvent event)'''
        def paint(self, painter, option, widget):
            '''void Plasma.ExtenderItem.paint(QPainter painter, QStyleOptionGraphicsItem option, QWidget widget)'''
        def hideCloseButton(self):
            '''void Plasma.ExtenderItem.hideCloseButton()'''
        def showCloseButton(self):
            '''void Plasma.ExtenderItem.showCloseButton()'''
        def returnToSource(self):
            '''void Plasma.ExtenderItem.returnToSource()'''
        def setCollapsed(self, collapsed):
            '''void Plasma.ExtenderItem.setCollapsed(bool collapsed)'''
        def destroy(self):
            '''void Plasma.ExtenderItem.destroy()'''
        def action(self, name):
            '''QAction Plasma.ExtenderItem.action(QString name)'''
            return QAction()
        def addAction(self, name, action):
            '''void Plasma.ExtenderItem.addAction(QString name, QAction action)'''
        def isCollapsed(self):
            '''bool Plasma.ExtenderItem.isCollapsed()'''
            return bool()
        def isDetached(self):
            '''bool Plasma.ExtenderItem.isDetached()'''
            return bool()
        def autoExpireDelay(self):
            '''int Plasma.ExtenderItem.autoExpireDelay()'''
            return int()
        def setAutoExpireDelay(self, time):
            '''void Plasma.ExtenderItem.setAutoExpireDelay(int time)'''
        def isGroup(self):
            '''bool Plasma.ExtenderItem.isGroup()'''
            return bool()
        def group(self):
            '''Plasma.ExtenderGroup Plasma.ExtenderItem.group()'''
            return Plasma.ExtenderGroup()
        def setGroup(self, group):
            '''void Plasma.ExtenderItem.setGroup(Plasma.ExtenderGroup group)'''
        def setGroup(self, group, pos):
            '''void Plasma.ExtenderItem.setGroup(Plasma.ExtenderGroup group, QPointF pos)'''
        def extender(self):
            '''Plasma.Extender Plasma.ExtenderItem.extender()'''
            return Plasma.Extender()
        def setExtender(self, extender, pos = None):
            '''void Plasma.ExtenderItem.setExtender(Plasma.Extender extender, QPointF pos = QPointF(-1,-1))'''
        def icon(self):
            '''QIcon Plasma.ExtenderItem.icon()'''
            return QIcon()
        def setIcon(self, icon):
            '''void Plasma.ExtenderItem.setIcon(QString icon)'''
        def setIcon(self, icon):
            '''void Plasma.ExtenderItem.setIcon(QIcon icon)'''
        def name(self):
            '''QString Plasma.ExtenderItem.name()'''
            return QString()
        def setName(self, name):
            '''void Plasma.ExtenderItem.setName(QString name)'''
        def title(self):
            '''QString Plasma.ExtenderItem.title()'''
            return QString()
        def setTitle(self, title):
            '''void Plasma.ExtenderItem.setTitle(QString title)'''
        def widget(self):
            '''QGraphicsItem Plasma.ExtenderItem.widget()'''
            return QGraphicsItem()
        def setWidget(self, widget):
            '''void Plasma.ExtenderItem.setWidget(QGraphicsItem widget)'''
        def config(self):
            '''KConfigGroup Plasma.ExtenderItem.config()'''
            return KConfigGroup()
    class ItemBackground(QGraphicsWidget):
        """"""
        def __init__(self, parent = None):
            '''void Plasma.ItemBackground.__init__(QGraphicsWidget parent = None)'''
        def resizeEvent(self):
            '''QGraphicsSceneResizeEvent Plasma.ItemBackground.resizeEvent()'''
            return QGraphicsSceneResizeEvent()
        def sceneEventFilter(self, watched, event):
            '''bool Plasma.ItemBackground.sceneEventFilter(QGraphicsItem watched, QEvent event)'''
            return bool()
        def eventFilter(self, watched, event):
            '''bool Plasma.ItemBackground.eventFilter(QObject watched, QEvent event)'''
            return bool()
        def itemChange(self, change, value):
            '''QVariant Plasma.ItemBackground.itemChange(QGraphicsItem.GraphicsItemChange change, QVariant value)'''
            return QVariant()
        targetItemReached = pyqtSignal() # void targetItemReached(QGraphicsItem *) - signal
        targetReached = pyqtSignal() # void targetReached(QRectF) - signal
        animationStep = pyqtSignal() # void animationStep(qreal) - signal
        appearanceChanged = pyqtSignal() # void appearanceChanged() - signal
        def paint(self, painter, option, widget):
            '''void Plasma.ItemBackground.paint(QPainter painter, QStyleOptionGraphicsItem option, QWidget widget)'''
        def targetItem(self):
            '''QGraphicsItem Plasma.ItemBackground.targetItem()'''
            return QGraphicsItem()
        def setTargetItem(self, target):
            '''void Plasma.ItemBackground.setTargetItem(QGraphicsItem target)'''
        def target(self):
            '''QRectF Plasma.ItemBackground.target()'''
            return QRectF()
        def setTarget(self, newGeometry):
            '''void Plasma.ItemBackground.setTarget(QRectF newGeometry)'''
    class ServiceAccessJob(KJob):
        """"""
        def __init__(self, location, parent = None):
            '''void Plasma.ServiceAccessJob.__init__(KUrl location, QObject parent = None)'''
        def start(self):
            '''void Plasma.ServiceAccessJob.start()'''
        def service(self):
            '''Plasma.Service Plasma.ServiceAccessJob.service()'''
            return Plasma.Service()
    class QueryMatch():
        """"""
        # Enum Plasma.QueryMatch.Type
        NoMatch = 0
        CompletionMatch = 0
        PossibleMatch = 0
        InformationalMatch = 0
        HelperMatch = 0
        ExactMatch = 0
    
        def __init__(self, runner):
            '''void Plasma.QueryMatch.__init__(Plasma.AbstractRunner runner)'''
        def __init__(self, other):
            '''void Plasma.QueryMatch.__init__(Plasma.QueryMatch other)'''
        def __ge__(self, other):
            '''bool Plasma.QueryMatch.__ge__(Plasma.QueryMatch other)'''
            return bool()
        def __ne__(self, other):
            '''bool Plasma.QueryMatch.__ne__(Plasma.QueryMatch other)'''
            return bool()
        def __eq__(self, other):
            '''bool Plasma.QueryMatch.__eq__(Plasma.QueryMatch other)'''
            return bool()
        def createConfigurationInterface(self, parent):
            '''void Plasma.QueryMatch.createConfigurationInterface(QWidget parent)'''
        def hasConfigurationInterface(self):
            '''bool Plasma.QueryMatch.hasConfigurationInterface()'''
            return bool()
        def setSelectedAction(self, action):
            '''void Plasma.QueryMatch.setSelectedAction(QAction action)'''
        def selectedAction(self):
            '''QAction Plasma.QueryMatch.selectedAction()'''
            return QAction()
        def isEnabled(self):
            '''bool Plasma.QueryMatch.isEnabled()'''
            return bool()
        def setEnabled(self, enable):
            '''void Plasma.QueryMatch.setEnabled(bool enable)'''
        def icon(self):
            '''QIcon Plasma.QueryMatch.icon()'''
            return QIcon()
        def setIcon(self, icon):
            '''void Plasma.QueryMatch.setIcon(QIcon icon)'''
        def subtext(self):
            '''QString Plasma.QueryMatch.subtext()'''
            return QString()
        def setSubtext(self, text):
            '''void Plasma.QueryMatch.setSubtext(QString text)'''
        def text(self):
            '''QString Plasma.QueryMatch.text()'''
            return QString()
        def setText(self, text):
            '''void Plasma.QueryMatch.setText(QString text)'''
        def id(self):
            '''QString Plasma.QueryMatch.id()'''
            return QString()
        def setId(self, id):
            '''void Plasma.QueryMatch.setId(QString id)'''
        def data(self):
            '''QVariant Plasma.QueryMatch.data()'''
            return QVariant()
        def setData(self, data):
            '''void Plasma.QueryMatch.setData(QVariant data)'''
        def run(self, context):
            '''void Plasma.QueryMatch.run(Plasma.RunnerContext context)'''
        def relevance(self):
            '''float Plasma.QueryMatch.relevance()'''
            return float()
        def setRelevance(self, relevance):
            '''void Plasma.QueryMatch.setRelevance(float relevance)'''
        def type(self):
            '''Plasma.QueryMatch.Type Plasma.QueryMatch.type()'''
            return Plasma.QueryMatch.Type()
        def setType(self, type):
            '''void Plasma.QueryMatch.setType(Plasma.QueryMatch.Type type)'''
        def isValid(self):
            '''bool Plasma.QueryMatch.isValid()'''
            return bool()
        def runner(self):
            '''Plasma.AbstractRunner Plasma.QueryMatch.runner()'''
            return Plasma.AbstractRunner()
        def __lt__(self, other):
            '''bool Plasma.QueryMatch.__lt__(Plasma.QueryMatch other)'''
            return bool()
    class FrameSvg():
        """"""
        class EnabledBorders():
            """"""
            def __init__(self):
                '''Plasma.FrameSvg.EnabledBorders Plasma.FrameSvg.EnabledBorders.__init__()'''
                return Plasma.FrameSvg.EnabledBorders()
            def __init__(self):
                '''int Plasma.FrameSvg.EnabledBorders.__init__()'''
                return int()
            def __init__(self):
                '''void Plasma.FrameSvg.EnabledBorders.__init__()'''
            def __bool__(self):
                '''int Plasma.FrameSvg.EnabledBorders.__bool__()'''
                return int()
            def __ne__(self, f):
                '''bool Plasma.FrameSvg.EnabledBorders.__ne__(Plasma.FrameSvg.EnabledBorders f)'''
                return bool()
            def __eq__(self, f):
                '''bool Plasma.FrameSvg.EnabledBorders.__eq__(Plasma.FrameSvg.EnabledBorders f)'''
                return bool()
            def __invert__(self):
                '''Plasma.FrameSvg.EnabledBorders Plasma.FrameSvg.EnabledBorders.__invert__()'''
                return Plasma.FrameSvg.EnabledBorders()
            def __and__(self, mask):
                '''Plasma.FrameSvg.EnabledBorders Plasma.FrameSvg.EnabledBorders.__and__(int mask)'''
                return Plasma.FrameSvg.EnabledBorders()
            def __xor__(self, f):
                '''Plasma.FrameSvg.EnabledBorders Plasma.FrameSvg.EnabledBorders.__xor__(Plasma.FrameSvg.EnabledBorders f)'''
                return Plasma.FrameSvg.EnabledBorders()
            def __xor__(self, f):
                '''Plasma.FrameSvg.EnabledBorders Plasma.FrameSvg.EnabledBorders.__xor__(int f)'''
                return Plasma.FrameSvg.EnabledBorders()
            def __or__(self, f):
                '''Plasma.FrameSvg.EnabledBorders Plasma.FrameSvg.EnabledBorders.__or__(Plasma.FrameSvg.EnabledBorders f)'''
                return Plasma.FrameSvg.EnabledBorders()
            def __or__(self, f):
                '''Plasma.FrameSvg.EnabledBorders Plasma.FrameSvg.EnabledBorders.__or__(int f)'''
                return Plasma.FrameSvg.EnabledBorders()
            def __int__(self):
                '''int Plasma.FrameSvg.EnabledBorders.__int__()'''
                return int()
            def __ixor__(self, f):
                '''Plasma.FrameSvg.EnabledBorders Plasma.FrameSvg.EnabledBorders.__ixor__(Plasma.FrameSvg.EnabledBorders f)'''
                return Plasma.FrameSvg.EnabledBorders()
            def __ior__(self, f):
                '''Plasma.FrameSvg.EnabledBorders Plasma.FrameSvg.EnabledBorders.__ior__(Plasma.FrameSvg.EnabledBorders f)'''
                return Plasma.FrameSvg.EnabledBorders()
            def __iand__(self, mask):
                '''Plasma.FrameSvg.EnabledBorders Plasma.FrameSvg.EnabledBorders.__iand__(int mask)'''
                return Plasma.FrameSvg.EnabledBorders()
    class WebView(QGraphicsWidget):
        """"""
        def __init__(self, parent = None):
            '''void Plasma.WebView.__init__(QGraphicsItem parent = None)'''
        urlChanged = pyqtSignal() # void urlChanged(const QUrlamp;) - signal
        def stop(self):
            '''void Plasma.WebView.stop()'''
        def reload(self):
            '''void Plasma.WebView.reload()'''
        def forward(self):
            '''void Plasma.WebView.forward()'''
        def back(self):
            '''void Plasma.WebView.back()'''
        def itemChange(self, change, value):
            '''QVariant Plasma.WebView.itemChange(QGraphicsItem.GraphicsItemChange change, QVariant value)'''
            return QVariant()
        def setZoomFactor(self, zoom):
            '''void Plasma.WebView.setZoomFactor(float zoom)'''
        def zoomFactor(self):
            '''float Plasma.WebView.zoomFactor()'''
            return float()
        def sizeHint(self, which, constraint):
            '''QSizeF Plasma.WebView.sizeHint(Qt.SizeHint which, QSizeF constraint)'''
            return QSizeF()
        def viewportGeometry(self):
            '''QRectF Plasma.WebView.viewportGeometry()'''
            return QRectF()
        def scrollPosition(self):
            '''QPointF Plasma.WebView.scrollPosition()'''
            return QPointF()
        def setScrollPosition(self, position):
            '''void Plasma.WebView.setScrollPosition(QPointF position)'''
        def contentsSize(self):
            '''QSizeF Plasma.WebView.contentsSize()'''
            return QSizeF()
        def dropEvent(self, event):
            '''void Plasma.WebView.dropEvent(QGraphicsSceneDragDropEvent event)'''
        def dragMoveEvent(self, event):
            '''void Plasma.WebView.dragMoveEvent(QGraphicsSceneDragDropEvent event)'''
        def dragLeaveEvent(self, event):
            '''void Plasma.WebView.dragLeaveEvent(QGraphicsSceneDragDropEvent event)'''
        def dragEnterEvent(self, event):
            '''void Plasma.WebView.dragEnterEvent(QGraphicsSceneDragDropEvent event)'''
        def focusOutEvent(self, event):
            '''void Plasma.WebView.focusOutEvent(QFocusEvent event)'''
        def focusInEvent(self, event):
            '''void Plasma.WebView.focusInEvent(QFocusEvent event)'''
        def keyReleaseEvent(self, event):
            '''void Plasma.WebView.keyReleaseEvent(QKeyEvent event)'''
        def keyPressEvent(self, event):
            '''void Plasma.WebView.keyPressEvent(QKeyEvent event)'''
        def wheelEvent(self, event):
            '''void Plasma.WebView.wheelEvent(QGraphicsSceneWheelEvent event)'''
        def contextMenuEvent(self, event):
            '''void Plasma.WebView.contextMenuEvent(QGraphicsSceneContextMenuEvent event)'''
        def mouseReleaseEvent(self, event):
            '''void Plasma.WebView.mouseReleaseEvent(QGraphicsSceneMouseEvent event)'''
        def mouseDoubleClickEvent(self, event):
            '''void Plasma.WebView.mouseDoubleClickEvent(QGraphicsSceneMouseEvent event)'''
        def mousePressEvent(self, event):
            '''void Plasma.WebView.mousePressEvent(QGraphicsSceneMouseEvent event)'''
        def hoverMoveEvent(self, event):
            '''void Plasma.WebView.hoverMoveEvent(QGraphicsSceneHoverEvent event)'''
        def mouseMoveEvent(self, event):
            '''void Plasma.WebView.mouseMoveEvent(QGraphicsSceneMouseEvent event)'''
        def paint(self, painter, option, widget = None):
            '''void Plasma.WebView.paint(QPainter painter, QStyleOptionGraphicsItem option, QWidget widget = None)'''
        loadFinished = pyqtSignal() # void loadFinished(bool) - signal
        loadProgress = pyqtSignal() # void loadProgress(int) - signal
        def setGeometry(self, geometry):
            '''void Plasma.WebView.setGeometry(QRectF geometry)'''
        def dragToScroll(self):
            '''bool Plasma.WebView.dragToScroll()'''
            return bool()
        def setDragToScroll(self, drag):
            '''void Plasma.WebView.setDragToScroll(bool drag)'''
        def mainFrame(self):
            '''QWebFrame Plasma.WebView.mainFrame()'''
            return QWebFrame()
        def page(self):
            '''QWebPage Plasma.WebView.page()'''
            return QWebPage()
        def setPage(self, page):
            '''void Plasma.WebView.setPage(QWebPage page)'''
        def geometry(self):
            '''QRectF Plasma.WebView.geometry()'''
            return QRectF()
        def setHtml(self, html, baseUrl = KUrl()):
            '''void Plasma.WebView.setHtml(QString html, KUrl baseUrl = KUrl())'''
        def html(self):
            '''QString Plasma.WebView.html()'''
            return QString()
        def url(self):
            '''KUrl Plasma.WebView.url()'''
            return KUrl()
        def setUrl(self, url):
            '''void Plasma.WebView.setUrl(KUrl url)'''
    class Containment():
        """"""
        class StyleOption(QStyleOptionGraphicsItem):
            """"""
            # Enum Plasma.Containment.StyleOption.StyleOptionVersion
            Version = 0
        
            # Enum Plasma.Containment.StyleOption.StyleOptionType
            Type = 0
        
            view = None # Plasma.View - member
            def __init__(self):
                '''void Plasma.Containment.StyleOption.__init__()'''
            def __init__(self, other):
                '''void Plasma.Containment.StyleOption.__init__(Plasma.Containment.StyleOption other)'''
            def __init__(self, other):
                '''void Plasma.Containment.StyleOption.__init__(QStyleOptionGraphicsItem other)'''
    class AbstractToolBox(QGraphicsWidget):
        """"""
        # Enum Plasma.AbstractToolBox.ToolType
        AddTool = 0
        ConfigureTool = 0
        ControlTool = 0
        MiscTool = 0
        DestructiveTool = 0
        UserToolType = 0
    
        def __init__(self, parent):
            '''void Plasma.AbstractToolBox.__init__(Plasma.Containment parent)'''
        def __init__(self, parent = None, args = QVariantList()):
            '''void Plasma.AbstractToolBox.__init__(QObject parent = None, list-of-QVariant args = QVariantList())'''
        def reposition(self):
            '''void Plasma.AbstractToolBox.reposition()'''
        def save(self, group):
            '''void Plasma.AbstractToolBox.save(KConfigGroup group)'''
        def restore(self, group):
            '''void Plasma.AbstractToolBox.restore(KConfigGroup group)'''
        def listToolBoxInfo(self, parentApp = QString()):
            '''static list-of-KPluginInfo Plasma.AbstractToolBox.listToolBoxInfo(QString parentApp = QString())'''
            return [KPluginInfo()]
        def load(self, name, args = QVariantList(), containment = None):
            '''static Plasma.AbstractToolBox Plasma.AbstractToolBox.load(QString name, list-of-QVariant args = QVariantList(), Plasma.Containment containment = None)'''
            return Plasma.AbstractToolBox()
        def containment(self):
            '''Plasma.Containment Plasma.AbstractToolBox.containment()'''
            return Plasma.Containment()
        visibilityChanged = pyqtSignal() # void visibilityChanged(bool) - signal
        toggled = pyqtSignal() # void toggled() - signal
        def setShowing(self, show):
            '''abstract void Plasma.AbstractToolBox.setShowing(bool show)'''
        def isShowing(self):
            '''abstract bool Plasma.AbstractToolBox.isShowing()'''
            return bool()
        def removeTool(self, action):
            '''abstract void Plasma.AbstractToolBox.removeTool(QAction action)'''
        def addTool(self, action):
            '''abstract void Plasma.AbstractToolBox.addTool(QAction action)'''
    class PlotColor():
        """"""
        color = None # QColor - member
        darkColor = None # QColor - member
        def __init__(self):
            '''void Plasma.PlotColor.__init__()'''
        def __init__(self):
            '''Plasma.PlotColor Plasma.PlotColor.__init__()'''
            return Plasma.PlotColor()
    class DataEngineManager(QObject):
        """"""
        def timerEvent(self, event):
            '''void Plasma.DataEngineManager.timerEvent(QTimerEvent event)'''
        def listEngineInfoByCategory(self, category, parentApp = QString()):
            '''static list-of-KPluginInfo Plasma.DataEngineManager.listEngineInfoByCategory(QString category, QString parentApp = QString())'''
            return [KPluginInfo()]
        def listEngineInfo(self, parentApp = QString()):
            '''static list-of-KPluginInfo Plasma.DataEngineManager.listEngineInfo(QString parentApp = QString())'''
            return [KPluginInfo()]
        def listAllEngines(self, parentApp = QString()):
            '''static QStringList Plasma.DataEngineManager.listAllEngines(QString parentApp = QString())'''
            return QStringList()
        def unloadEngine(self, name):
            '''void Plasma.DataEngineManager.unloadEngine(QString name)'''
        def loadEngine(self, name):
            '''Plasma.DataEngine Plasma.DataEngineManager.loadEngine(QString name)'''
            return Plasma.DataEngine()
        def engine(self, name):
            '''Plasma.DataEngine Plasma.DataEngineManager.engine(QString name)'''
            return Plasma.DataEngine()
        def self(self):
            '''static Plasma.DataEngineManager Plasma.DataEngineManager.self()'''
            return Plasma.DataEngineManager()
    class Animation(QAbstractAnimation):
        """"""
        # Enum Plasma.Animation.MovementDirectionFlag
        MoveAny = 0
        MoveUp = 0
        MoveRight = 0
        MoveDown = 0
        MoveLeft = 0
    
        # Enum Plasma.Animation.ReferenceFlag
        Center = 0
        Up = 0
        Down = 0
        Left = 0
        Right = 0
    
        def __init__(self, parent = None):
            '''void Plasma.Animation.__init__(QObject parent = None)'''
        def easingCurve(self):
            '''QEasingCurve Plasma.Animation.easingCurve()'''
            return QEasingCurve()
        def setEasingCurve(self, curve):
            '''void Plasma.Animation.setEasingCurve(QEasingCurve curve)'''
        def targetWidget(self):
            '''QGraphicsWidget Plasma.Animation.targetWidget()'''
            return QGraphicsWidget()
        def setTargetWidget(self, widget):
            '''void Plasma.Animation.setTargetWidget(QGraphicsWidget widget)'''
        def updateCurrentTime(self, currentTime):
            '''void Plasma.Animation.updateCurrentTime(int currentTime)'''
        def setDuration(self, duration = 250):
            '''void Plasma.Animation.setDuration(int duration = 250)'''
        def duration(self):
            '''int Plasma.Animation.duration()'''
            return int()
    class Theme(QObject):
        """"""
        # Enum Plasma.Theme.FontRole
        DefaultFont = 0
        DesktopFont = 0
        SmallestFont = 0
    
        # Enum Plasma.Theme.ColorRole
        TextColor = 0
        HighlightColor = 0
        BackgroundColor = 0
        ButtonTextColor = 0
        ButtonBackgroundColor = 0
        LinkColor = 0
        VisitedLinkColor = 0
        ButtonHoverColor = 0
        ButtonFocusColor = 0
        ViewTextColor = 0
        ViewBackgroundColor = 0
        ViewHoverColor = 0
        ViewFocusColor = 0
    
        def __init__(self, parent = None):
            '''void Plasma.Theme.__init__(QObject parent = None)'''
        def __init__(self, themeName, parent = None):
            '''void Plasma.Theme.__init__(QString themeName, QObject parent = None)'''
        def toolTipDelay(self):
            '''int Plasma.Theme.toolTipDelay()'''
            return int()
        def homepage(self):
            '''KUrl Plasma.Theme.homepage()'''
            return KUrl()
        def listCachedRectKeys(self, image):
            '''QStringList Plasma.Theme.listCachedRectKeys(QString image)'''
            return QStringList()
        def styleSheet(self, css = QString()):
            '''QString Plasma.Theme.styleSheet(QString css = QString())'''
            return QString()
        def animationPath(self, name):
            '''QString Plasma.Theme.animationPath(QString name)'''
            return QString()
        def settingsChanged(self):
            '''void Plasma.Theme.settingsChanged()'''
        themeChanged = pyqtSignal() # void themeChanged() - signal
        def releaseRectsCache(self, image):
            '''void Plasma.Theme.releaseRectsCache(QString image)'''
        def invalidateRectsCache(self, image):
            '''void Plasma.Theme.invalidateRectsCache(QString image)'''
        def insertIntoRectsCache(self, image, element, rect):
            '''void Plasma.Theme.insertIntoRectsCache(QString image, QString element, QRectF rect)'''
        def findInRectsCache(self, image, element, rect):
            '''bool Plasma.Theme.findInRectsCache(QString image, QString element, QRectF rect)'''
            return bool()
        def setCacheLimit(self, kbytes):
            '''void Plasma.Theme.setCacheLimit(int kbytes)'''
        def insertIntoCache(self, key, pix):
            '''void Plasma.Theme.insertIntoCache(QString key, QPixmap pix)'''
        def insertIntoCache(self, key, pix, id):
            '''void Plasma.Theme.insertIntoCache(QString key, QPixmap pix, QString id)'''
        def findInCache(self, key, pix):
            '''bool Plasma.Theme.findInCache(QString key, QPixmap pix)'''
            return bool()
        def findInCache(self, key, pix, lastModified):
            '''bool Plasma.Theme.findInCache(QString key, QPixmap pix, int lastModified)'''
            return bool()
        def useNativeWidgetStyle(self):
            '''bool Plasma.Theme.useNativeWidgetStyle()'''
            return bool()
        def useGlobalSettings(self):
            '''bool Plasma.Theme.useGlobalSettings()'''
            return bool()
        def setUseGlobalSettings(self, useGlobal):
            '''void Plasma.Theme.setUseGlobalSettings(bool useGlobal)'''
        def windowTranslucencyEnabled(self):
            '''bool Plasma.Theme.windowTranslucencyEnabled()'''
            return bool()
        def fontMetrics(self):
            '''QFontMetrics Plasma.Theme.fontMetrics()'''
            return QFontMetrics()
        def font(self, role):
            '''QFont Plasma.Theme.font(Plasma.Theme.FontRole role)'''
            return QFont()
        def setFont(self, font, role = None):
            '''void Plasma.Theme.setFont(QFont font, Plasma.Theme.FontRole role = Plasma.Theme.DefaultFont)'''
        def color(self, role):
            '''QColor Plasma.Theme.color(Plasma.Theme.ColorRole role)'''
            return QColor()
        def colorScheme(self):
            '''KSharedConfigPtr Plasma.Theme.colorScheme()'''
            return KSharedConfigPtr()
        def currentThemeHasImage(self, name):
            '''bool Plasma.Theme.currentThemeHasImage(QString name)'''
            return bool()
        def wallpaperPath(self, size = QSize()):
            '''QString Plasma.Theme.wallpaperPath(QSize size = QSize())'''
            return QString()
        def imagePath(self, name):
            '''QString Plasma.Theme.imagePath(QString name)'''
            return QString()
        def themeName(self):
            '''QString Plasma.Theme.themeName()'''
            return QString()
        def setThemeName(self, themeName):
            '''void Plasma.Theme.setThemeName(QString themeName)'''
        def listThemeInfo(self):
            '''static list-of-KPluginInfo Plasma.Theme.listThemeInfo()'''
            return [KPluginInfo()]
        def packageStructure(self):
            '''static unknown-type Plasma.Theme.packageStructure()'''
            return unknown-type()
        def defaultTheme(self):
            '''static Plasma.Theme Plasma.Theme.defaultTheme()'''
            return Plasma.Theme()
    class ScrollWidget(QGraphicsWidget):
        """"""
        def __init__(self, parent = None):
            '''void Plasma.ScrollWidget.__init__(QGraphicsWidget parent = None)'''
        def setOverflowBordersVisible(self, visible):
            '''void Plasma.ScrollWidget.setOverflowBordersVisible(bool visible)'''
        def overflowBordersVisible(self):
            '''bool Plasma.ScrollWidget.overflowBordersVisible()'''
            return bool()
        def sceneEventFilter(self, i, e):
            '''bool Plasma.ScrollWidget.sceneEventFilter(QGraphicsItem i, QEvent e)'''
            return bool()
        def keyPressEvent(self, event):
            '''void Plasma.ScrollWidget.keyPressEvent(QKeyEvent event)'''
        viewportGeometryChanged = pyqtSignal() # void viewportGeometryChanged(const QRectFamp;) - signal
        def snapSize(self):
            '''QSizeF Plasma.ScrollWidget.snapSize()'''
            return QSizeF()
        def setSnapSize(self, size):
            '''void Plasma.ScrollWidget.setSnapSize(QSizeF size)'''
        def hasOverShoot(self):
            '''bool Plasma.ScrollWidget.hasOverShoot()'''
            return bool()
        def setOverShoot(self, enable):
            '''void Plasma.ScrollWidget.setOverShoot(bool enable)'''
        def alignment(self):
            '''Qt.Alignment Plasma.ScrollWidget.alignment()'''
            return Qt.Alignment()
        def setAlignment(self, align):
            '''void Plasma.ScrollWidget.setAlignment(Qt.Alignment align)'''
        scrollStateChanged = pyqtSignal() # void scrollStateChanged(QAbstractAnimation::State,QAbstractAnimation::State) - signal
        def sizeHint(self, which, constraint):
            '''QSizeF Plasma.ScrollWidget.sizeHint(Qt.SizeHint which, QSizeF constraint)'''
            return QSizeF()
        def focusInEvent(self, event):
            '''void Plasma.ScrollWidget.focusInEvent(QFocusEvent event)'''
        def mouseReleaseEvent(self, event):
            '''void Plasma.ScrollWidget.mouseReleaseEvent(QGraphicsSceneMouseEvent event)'''
        def scrollPosition(self):
            '''QPointF Plasma.ScrollWidget.scrollPosition()'''
            return QPointF()
        def setScrollPosition(self, position):
            '''void Plasma.ScrollWidget.setScrollPosition(QPointF position)'''
        def contentsSize(self):
            '''QSizeF Plasma.ScrollWidget.contentsSize()'''
            return QSizeF()
        def viewportGeometry(self):
            '''QRectF Plasma.ScrollWidget.viewportGeometry()'''
            return QRectF()
        def unregisterAsDragHandle(self, item):
            '''void Plasma.ScrollWidget.unregisterAsDragHandle(QGraphicsWidget item)'''
        def registerAsDragHandle(self, item):
            '''void Plasma.ScrollWidget.registerAsDragHandle(QGraphicsWidget item)'''
        def ensureItemVisible(self, item):
            '''void Plasma.ScrollWidget.ensureItemVisible(QGraphicsItem item)'''
        def ensureRectVisible(self, rect):
            '''void Plasma.ScrollWidget.ensureRectVisible(QRectF rect)'''
        def eventFilter(self, watched, event):
            '''bool Plasma.ScrollWidget.eventFilter(QObject watched, QEvent event)'''
            return bool()
        def wheelEvent(self, event):
            '''void Plasma.ScrollWidget.wheelEvent(QGraphicsSceneWheelEvent event)'''
        def mousePressEvent(self, event):
            '''void Plasma.ScrollWidget.mousePressEvent(QGraphicsSceneMouseEvent event)'''
        def mouseMoveEvent(self, event):
            '''void Plasma.ScrollWidget.mouseMoveEvent(QGraphicsSceneMouseEvent event)'''
        def resizeEvent(self, event):
            '''void Plasma.ScrollWidget.resizeEvent(QGraphicsSceneResizeEvent event)'''
        def nativeWidget(self):
            '''QWidget Plasma.ScrollWidget.nativeWidget()'''
            return QWidget()
        def styleSheet(self):
            '''QString Plasma.ScrollWidget.styleSheet()'''
            return QString()
        def setStyleSheet(self, stylesheet):
            '''void Plasma.ScrollWidget.setStyleSheet(QString stylesheet)'''
        def verticalScrollBarPolicy(self):
            '''Qt.ScrollBarPolicy Plasma.ScrollWidget.verticalScrollBarPolicy()'''
            return Qt.ScrollBarPolicy()
        def setVerticalScrollBarPolicy(self, policy):
            '''void Plasma.ScrollWidget.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy policy)'''
        def horizontalScrollBarPolicy(self):
            '''Qt.ScrollBarPolicy Plasma.ScrollWidget.horizontalScrollBarPolicy()'''
            return Qt.ScrollBarPolicy()
        def setHorizontalScrollBarPolicy(self, policy):
            '''void Plasma.ScrollWidget.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy policy)'''
        def widget(self):
            '''QGraphicsWidget Plasma.ScrollWidget.widget()'''
            return QGraphicsWidget()
        def setWidget(self, widget):
            '''void Plasma.ScrollWidget.setWidget(QGraphicsWidget widget)'''
    class PluginLoader():
        """"""
        def __init__(self):
            '''void Plasma.PluginLoader.__init__()'''
        def standardInternalServiceInfo(self):
            '''list-of-KPluginInfo Plasma.PluginLoader.standardInternalServiceInfo()'''
            return [KPluginInfo()]
        def standardInternalRunnerInfo(self):
            '''list-of-KPluginInfo Plasma.PluginLoader.standardInternalRunnerInfo()'''
            return [KPluginInfo()]
        def standardInternalDataEngineInfo(self):
            '''list-of-KPluginInfo Plasma.PluginLoader.standardInternalDataEngineInfo()'''
            return [KPluginInfo()]
        def standardInternalAppletInfo(self, category):
            '''list-of-KPluginInfo Plasma.PluginLoader.standardInternalAppletInfo(QString category)'''
            return [KPluginInfo()]
        def internalServiceInfo(self):
            '''list-of-KPluginInfo Plasma.PluginLoader.internalServiceInfo()'''
            return [KPluginInfo()]
        def internalRunnerInfo(self):
            '''list-of-KPluginInfo Plasma.PluginLoader.internalRunnerInfo()'''
            return [KPluginInfo()]
        def internalDataEngineInfo(self):
            '''list-of-KPluginInfo Plasma.PluginLoader.internalDataEngineInfo()'''
            return [KPluginInfo()]
        def internalAppletInfo(self, category):
            '''list-of-KPluginInfo Plasma.PluginLoader.internalAppletInfo(QString category)'''
            return [KPluginInfo()]
        def internalLoadService(self, name, args, parent = None):
            '''Plasma.Service Plasma.PluginLoader.internalLoadService(QString name, list-of-QVariant args, QObject parent = None)'''
            return Plasma.Service()
        def internalLoadDataEngine(self, name):
            '''Plasma.DataEngine Plasma.PluginLoader.internalLoadDataEngine(QString name)'''
            return Plasma.DataEngine()
        def internalLoadRunner(self, name):
            '''Plasma.AbstractRunner Plasma.PluginLoader.internalLoadRunner(QString name)'''
            return Plasma.AbstractRunner()
        def internalLoadApplet(self, name, appletId = 0, args = QVariantList()):
            '''Plasma.Applet Plasma.PluginLoader.internalLoadApplet(QString name, int appletId = 0, list-of-QVariant args = QVariantList())'''
            return Plasma.Applet()
        def pluginLoader(self):
            '''static Plasma.PluginLoader Plasma.PluginLoader.pluginLoader()'''
            return Plasma.PluginLoader()
        def setPluginLoader(self, loader):
            '''static void Plasma.PluginLoader.setPluginLoader(Plasma.PluginLoader loader)'''
        def listRunnerInfo(self, parentApp = QString()):
            '''list-of-KPluginInfo Plasma.PluginLoader.listRunnerInfo(QString parentApp = QString())'''
            return [KPluginInfo()]
        def listDataEngineInfo(self, parentApp = QString()):
            '''list-of-KPluginInfo Plasma.PluginLoader.listDataEngineInfo(QString parentApp = QString())'''
            return [KPluginInfo()]
        def listAppletInfo(self, category, parentApp = QString()):
            '''list-of-KPluginInfo Plasma.PluginLoader.listAppletInfo(QString category, QString parentApp = QString())'''
            return [KPluginInfo()]
        def loadService(self, name, args, parent = None):
            '''Plasma.Service Plasma.PluginLoader.loadService(QString name, list-of-QVariant args, QObject parent = None)'''
            return Plasma.Service()
        def loadRunner(self, name):
            '''Plasma.AbstractRunner Plasma.PluginLoader.loadRunner(QString name)'''
            return Plasma.AbstractRunner()
        def loadDataEngine(self, name):
            '''Plasma.DataEngine Plasma.PluginLoader.loadDataEngine(QString name)'''
            return Plasma.DataEngine()
        def loadApplet(self, name, appletId = 0, args = QVariantList()):
            '''Plasma.Applet Plasma.PluginLoader.loadApplet(QString name, int appletId = 0, list-of-QVariant args = QVariantList())'''
            return Plasma.Applet()
    class ServiceJob(KJob):
        """"""
        def __init__(self, destination, operation, parameters, parent = None):
            '''void Plasma.ServiceJob.__init__(QString destination, QString operation, dict-of-QString-QVariant parameters, QObject parent = None)'''
        def setResult(self, result):
            '''void Plasma.ServiceJob.setResult(QVariant result)'''
        def start(self):
            '''void Plasma.ServiceJob.start()'''
        def result(self):
            '''QVariant Plasma.ServiceJob.result()'''
            return QVariant()
        def parameters(self):
            '''dict-of-QString-QVariant Plasma.ServiceJob.parameters()'''
            return dict-of-QString-QVariant()
        def operationName(self):
            '''QString Plasma.ServiceJob.operationName()'''
            return QString()
        def destination(self):
            '''QString Plasma.ServiceJob.destination()'''
            return QString()
    class MessageButtons():
        """"""
        def __init__(self):
            '''Plasma.MessageButtons Plasma.MessageButtons.__init__()'''
            return Plasma.MessageButtons()
        def __init__(self):
            '''int Plasma.MessageButtons.__init__()'''
            return int()
        def __init__(self):
            '''void Plasma.MessageButtons.__init__()'''
        def __bool__(self):
            '''int Plasma.MessageButtons.__bool__()'''
            return int()
        def __ne__(self, f):
            '''bool Plasma.MessageButtons.__ne__(Plasma.MessageButtons f)'''
            return bool()
        def __eq__(self, f):
            '''bool Plasma.MessageButtons.__eq__(Plasma.MessageButtons f)'''
            return bool()
        def __invert__(self):
            '''Plasma.MessageButtons Plasma.MessageButtons.__invert__()'''
            return Plasma.MessageButtons()
        def __and__(self, mask):
            '''Plasma.MessageButtons Plasma.MessageButtons.__and__(int mask)'''
            return Plasma.MessageButtons()
        def __xor__(self, f):
            '''Plasma.MessageButtons Plasma.MessageButtons.__xor__(Plasma.MessageButtons f)'''
            return Plasma.MessageButtons()
        def __xor__(self, f):
            '''Plasma.MessageButtons Plasma.MessageButtons.__xor__(int f)'''
            return Plasma.MessageButtons()
        def __or__(self, f):
            '''Plasma.MessageButtons Plasma.MessageButtons.__or__(Plasma.MessageButtons f)'''
            return Plasma.MessageButtons()
        def __or__(self, f):
            '''Plasma.MessageButtons Plasma.MessageButtons.__or__(int f)'''
            return Plasma.MessageButtons()
        def __int__(self):
            '''int Plasma.MessageButtons.__int__()'''
            return int()
        def __ixor__(self, f):
            '''Plasma.MessageButtons Plasma.MessageButtons.__ixor__(Plasma.MessageButtons f)'''
            return Plasma.MessageButtons()
        def __ior__(self, f):
            '''Plasma.MessageButtons Plasma.MessageButtons.__ior__(Plasma.MessageButtons f)'''
            return Plasma.MessageButtons()
        def __iand__(self, mask):
            '''Plasma.MessageButtons Plasma.MessageButtons.__iand__(int mask)'''
            return Plasma.MessageButtons()
    class RunnerSyntax():
        """"""
        def __init__(self, exampleQuery, description):
            '''void Plasma.RunnerSyntax.__init__(QString exampleQuery, QString description)'''
        def __init__(self, other):
            '''void Plasma.RunnerSyntax.__init__(Plasma.RunnerSyntax other)'''
        def searchTermDescription(self):
            '''QString Plasma.RunnerSyntax.searchTermDescription()'''
            return QString()
        def setSearchTermDescription(self, description):
            '''void Plasma.RunnerSyntax.setSearchTermDescription(QString description)'''
        def description(self):
            '''QString Plasma.RunnerSyntax.description()'''
            return QString()
        def setDescription(self, description):
            '''void Plasma.RunnerSyntax.setDescription(QString description)'''
        def exampleQueriesWithTermDescription(self):
            '''QStringList Plasma.RunnerSyntax.exampleQueriesWithTermDescription()'''
            return QStringList()
        def exampleQueries(self):
            '''QStringList Plasma.RunnerSyntax.exampleQueries()'''
            return QStringList()
        def addExampleQuery(self, exampleQuery):
            '''void Plasma.RunnerSyntax.addExampleQuery(QString exampleQuery)'''
    class ExtenderGroup(Plasma.ExtenderItem):
        """"""
        def __init__(self, parent, groupId = 0):
            '''void Plasma.ExtenderGroup.__init__(Plasma.Extender parent, int groupId = 0)'''
        def dropEvent(self, event):
            '''void Plasma.ExtenderGroup.dropEvent(QGraphicsSceneDragDropEvent event)'''
        def dragLeaveEvent(self, event):
            '''void Plasma.ExtenderGroup.dragLeaveEvent(QGraphicsSceneDragDropEvent event)'''
        def dragMoveEvent(self, event):
            '''void Plasma.ExtenderGroup.dragMoveEvent(QGraphicsSceneDragDropEvent event)'''
        def dragEnterEvent(self, event):
            '''void Plasma.ExtenderGroup.dragEnterEvent(QGraphicsSceneDragDropEvent event)'''
        def eventFilter(self, watched, event):
            '''bool Plasma.ExtenderGroup.eventFilter(QObject watched, QEvent event)'''
            return bool()
        def resizeEvent(self, event):
            '''void Plasma.ExtenderGroup.resizeEvent(QGraphicsSceneResizeEvent event)'''
        def setGroupCollapsed(self, collapsed):
            '''void Plasma.ExtenderGroup.setGroupCollapsed(bool collapsed)'''
        def setAutoCollapse(self, collapse):
            '''void Plasma.ExtenderGroup.setAutoCollapse(bool collapse)'''
        def isAutoCollapse(self):
            '''bool Plasma.ExtenderGroup.isAutoCollapse()'''
            return bool()
        def isGroupCollapsed(self):
            '''bool Plasma.ExtenderGroup.isGroupCollapsed()'''
            return bool()
        def collapseGroup(self):
            '''void Plasma.ExtenderGroup.collapseGroup()'''
        def expandGroup(self):
            '''void Plasma.ExtenderGroup.expandGroup()'''
        def setAutoHide(self, autoHide):
            '''void Plasma.ExtenderGroup.setAutoHide(bool autoHide)'''
        def autoHide(self):
            '''bool Plasma.ExtenderGroup.autoHide()'''
            return bool()
        def items(self):
            '''list-of-Plasma.ExtenderItem Plasma.ExtenderGroup.items()'''
            return [Plasma.ExtenderItem()]
    class Flip():
        """"""
        def __init__(self):
            '''Plasma.Flip Plasma.Flip.__init__()'''
            return Plasma.Flip()
        def __init__(self):
            '''int Plasma.Flip.__init__()'''
            return int()
        def __init__(self):
            '''void Plasma.Flip.__init__()'''
        def __bool__(self):
            '''int Plasma.Flip.__bool__()'''
            return int()
        def __ne__(self, f):
            '''bool Plasma.Flip.__ne__(Plasma.Flip f)'''
            return bool()
        def __eq__(self, f):
            '''bool Plasma.Flip.__eq__(Plasma.Flip f)'''
            return bool()
        def __invert__(self):
            '''Plasma.Flip Plasma.Flip.__invert__()'''
            return Plasma.Flip()
        def __and__(self, mask):
            '''Plasma.Flip Plasma.Flip.__and__(int mask)'''
            return Plasma.Flip()
        def __xor__(self, f):
            '''Plasma.Flip Plasma.Flip.__xor__(Plasma.Flip f)'''
            return Plasma.Flip()
        def __xor__(self, f):
            '''Plasma.Flip Plasma.Flip.__xor__(int f)'''
            return Plasma.Flip()
        def __or__(self, f):
            '''Plasma.Flip Plasma.Flip.__or__(Plasma.Flip f)'''
            return Plasma.Flip()
        def __or__(self, f):
            '''Plasma.Flip Plasma.Flip.__or__(int f)'''
            return Plasma.Flip()
        def __int__(self):
            '''int Plasma.Flip.__int__()'''
            return int()
        def __ixor__(self, f):
            '''Plasma.Flip Plasma.Flip.__ixor__(Plasma.Flip f)'''
            return Plasma.Flip()
        def __ior__(self, f):
            '''Plasma.Flip Plasma.Flip.__ior__(Plasma.Flip f)'''
            return Plasma.Flip()
        def __iand__(self, mask):
            '''Plasma.Flip Plasma.Flip.__iand__(int mask)'''
            return Plasma.Flip()
    class CheckBox(QGraphicsProxyWidget):
        """"""
        def __init__(self, parent = None):
            '''void Plasma.CheckBox.__init__(QGraphicsWidget parent = None)'''
        def changeEvent(self, event):
            '''void Plasma.CheckBox.changeEvent(QEvent event)'''
        def resizeEvent(self, event):
            '''void Plasma.CheckBox.resizeEvent(QGraphicsSceneResizeEvent event)'''
        toggled = pyqtSignal() # void toggled(bool) - signal
        def isChecked(self):
            '''bool Plasma.CheckBox.isChecked()'''
            return bool()
        def setChecked(self, checked):
            '''void Plasma.CheckBox.setChecked(bool checked)'''
        def nativeWidget(self):
            '''QCheckBox Plasma.CheckBox.nativeWidget()'''
            return QCheckBox()
        def styleSheet(self):
            '''QString Plasma.CheckBox.styleSheet()'''
            return QString()
        def setStyleSheet(self, stylesheet):
            '''void Plasma.CheckBox.setStyleSheet(QString stylesheet)'''
        def image(self):
            '''QString Plasma.CheckBox.image()'''
            return QString()
        def setImage(self, path):
            '''void Plasma.CheckBox.setImage(QString path)'''
        def text(self):
            '''QString Plasma.CheckBox.text()'''
            return QString()
        def setText(self, text):
            '''void Plasma.CheckBox.setText(QString text)'''
    class Corona(QGraphicsScene):
        """"""
        def __init__(self, parent = None):
            '''void Plasma.Corona.__init__(QObject parent = None)'''
        def setDefaultContainmentPlugin(self, name):
            '''void Plasma.Corona.setDefaultContainmentPlugin(QString name)'''
        def defaultContainmentPlugin(self):
            '''QString Plasma.Corona.defaultContainmentPlugin()'''
            return QString()
        def setPreferredToolBoxPlugin(self, type, plugin):
            '''void Plasma.Corona.setPreferredToolBoxPlugin(Plasma.Containment.Type type, QString plugin)'''
        def exportLayout(self, config, containments):
            '''void Plasma.Corona.exportLayout(KConfigGroup config, list-of-Plasma.Containment containments)'''
        def preferredToolBoxPlugin(self, type):
            '''QString Plasma.Corona.preferredToolBoxPlugin(Plasma.Containment.Type type)'''
            return QString()
        def mapAnimation(self, from_, to):
            '''void Plasma.Corona.mapAnimation(Plasma.Animator.Animation from, Plasma.Animator.Animation to)'''
        def mapAnimation(self, from_, to):
            '''void Plasma.Corona.mapAnimation(Plasma.Animator.Animation from, QString to)'''
        def layoutContainments(self):
            '''void Plasma.Corona.layoutContainments()'''
        def importLayout(self, config):
            '''list-of-Plasma.Containment Plasma.Corona.importLayout(KConfigBase config)'''
            return [Plasma.Containment()]
        def importLayout(self, config):
            '''list-of-Plasma.Containment Plasma.Corona.importLayout(KConfigGroup config)'''
            return [Plasma.Containment()]
        def dialogManager(self):
            '''Plasma.AbstractDialogManager Plasma.Corona.dialogManager()'''
            return Plasma.AbstractDialogManager()
        def setDialogManager(self, manager):
            '''void Plasma.Corona.setDialogManager(Plasma.AbstractDialogManager manager)'''
        def containmentActionsDefaults(self, containmentType):
            '''Plasma.ContainmentActionsPluginsConfig Plasma.Corona.containmentActionsDefaults(Plasma.Containment.Type containmentType)'''
            return Plasma.ContainmentActionsPluginsConfig()
        def setContainmentActionsDefaults(self, containmentType, config):
            '''void Plasma.Corona.setContainmentActionsDefaults(Plasma.Containment.Type containmentType, Plasma.ContainmentActionsPluginsConfig config)'''
        def dragMoveEvent(self, event):
            '''void Plasma.Corona.dragMoveEvent(QGraphicsSceneDragDropEvent event)'''
        def dragLeaveEvent(self, event):
            '''void Plasma.Corona.dragLeaveEvent(QGraphicsSceneDragDropEvent event)'''
        def dragEnterEvent(self, event):
            '''void Plasma.Corona.dragEnterEvent(QGraphicsSceneDragDropEvent event)'''
        def addContainmentDelayed(self, name, args = QVariantList()):
            '''Plasma.Containment Plasma.Corona.addContainmentDelayed(QString name, list-of-QVariant args = QVariantList())'''
            return Plasma.Containment()
        def loadDefaultLayout(self):
            '''void Plasma.Corona.loadDefaultLayout()'''
        shortcutsChanged = pyqtSignal() # void shortcutsChanged() - signal
        immutabilityChanged = pyqtSignal() # void immutabilityChanged(Plasma::ImmutabilityType) - signal
        availableScreenRegionChanged = pyqtSignal() # void availableScreenRegionChanged() - signal
        configSynced = pyqtSignal() # void configSynced() - signal
        releaseVisualFocus = pyqtSignal() # void releaseVisualFocus() - signal
        screenOwnerChanged = pyqtSignal() # void screenOwnerChanged(int,int,Plasma::Containment *) - signal
        containmentAdded = pyqtSignal() # void containmentAdded(Plasma::Containment *) - signal
        def requireConfigSync(self):
            '''void Plasma.Corona.requireConfigSync()'''
        def requestConfigSync(self):
            '''void Plasma.Corona.requestConfigSync()'''
        def setImmutability(self, immutable):
            '''void Plasma.Corona.setImmutability(Plasma.ImmutabilityType immutable)'''
        def immutability(self):
            '''Plasma.ImmutabilityType Plasma.Corona.immutability()'''
            return Plasma.ImmutabilityType()
        def saveLayout(self, config = QString()):
            '''void Plasma.Corona.saveLayout(QString config = QString())'''
        def loadLayout(self, config = QString()):
            '''void Plasma.Corona.loadLayout(QString config = QString())'''
        def initializeLayout(self, config = QString()):
            '''void Plasma.Corona.initializeLayout(QString config = QString())'''
        def addShortcuts(self, newShortcuts):
            '''void Plasma.Corona.addShortcuts(KActionCollection newShortcuts)'''
        def updateShortcuts(self):
            '''void Plasma.Corona.updateShortcuts()'''
        def enableAction(self, name, enable):
            '''void Plasma.Corona.enableAction(QString name, bool enable)'''
        def actions(self):
            '''list-of-QAction Plasma.Corona.actions()'''
            return [QAction()]
        def addAction(self, name, action):
            '''void Plasma.Corona.addAction(QString name, QAction action)'''
        def addAction(self, name):
            '''KAction Plasma.Corona.addAction(QString name)'''
            return KAction()
        def action(self, name):
            '''QAction Plasma.Corona.action(QString name)'''
            return QAction()
        def freeEdges(self, screen):
            '''list-of-Plasma.Location Plasma.Corona.freeEdges(int screen)'''
            return [Plasma.Location()]
        def popupPosition(self, item, size):
            '''QPoint Plasma.Corona.popupPosition(QGraphicsItem item, QSize size)'''
            return QPoint()
        def popupPosition(self, item, size, alignment):
            '''QPoint Plasma.Corona.popupPosition(QGraphicsItem item, QSize size, Qt.AlignmentFlag alignment)'''
            return QPoint()
        def availableScreenRegion(self, id):
            '''QRegion Plasma.Corona.availableScreenRegion(int id)'''
            return QRegion()
        def screenGeometry(self, id):
            '''QRect Plasma.Corona.screenGeometry(int id)'''
            return QRect()
        def numScreens(self):
            '''int Plasma.Corona.numScreens()'''
            return int()
        def offscreenWidgets(self):
            '''list-of-QGraphicsWidget Plasma.Corona.offscreenWidgets()'''
            return [QGraphicsWidget()]
        def removeOffscreenWidget(self, widget):
            '''void Plasma.Corona.removeOffscreenWidget(QGraphicsWidget widget)'''
        def addOffscreenWidget(self, widget):
            '''void Plasma.Corona.addOffscreenWidget(QGraphicsWidget widget)'''
        def containmentForScreen(self, screen, desktop = None):
            '''Plasma.Containment Plasma.Corona.containmentForScreen(int screen, int desktop = -1)'''
            return Plasma.Containment()
        def containmentForScreen(self, screen, desktop, defaultPluginIfNonExistent, defaultArgs = QVariantList()):
            '''Plasma.Containment Plasma.Corona.containmentForScreen(int screen, int desktop, QString defaultPluginIfNonExistent, list-of-QVariant defaultArgs = QVariantList())'''
            return Plasma.Containment()
        def addContainment(self, name, args = QVariantList()):
            '''Plasma.Containment Plasma.Corona.addContainment(QString name, list-of-QVariant args = QVariantList())'''
            return Plasma.Containment()
        def config(self):
            '''unknown-type Plasma.Corona.config()'''
            return unknown-type()
        def clearContainments(self):
            '''void Plasma.Corona.clearContainments()'''
        def containments(self):
            '''list-of-Plasma.Containment Plasma.Corona.containments()'''
            return [Plasma.Containment()]
        def appletMimeType(self):
            '''QString Plasma.Corona.appletMimeType()'''
            return QString()
        def setAppletMimeType(self, mimetype):
            '''void Plasma.Corona.setAppletMimeType(QString mimetype)'''
    class Separator(QGraphicsWidget):
        """"""
        def __init__(self, parent = None, wFlags = 0):
            '''void Plasma.Separator.__init__(QGraphicsItem parent = None, Qt.WindowFlags wFlags = 0)'''
        def sizeHint(self, which, constraint):
            '''QSizeF Plasma.Separator.sizeHint(Qt.SizeHint which, QSizeF constraint)'''
            return QSizeF()
        def paint(self, painter, option, widget):
            '''void Plasma.Separator.paint(QPainter painter, QStyleOptionGraphicsItem option, QWidget widget)'''
        def orientation(self):
            '''Qt.Orientation Plasma.Separator.orientation()'''
            return Qt.Orientation()
        def setOrientation(self, orientation):
            '''void Plasma.Separator.setOrientation(Qt.Orientation orientation)'''
    class RunnerContext():
        """"""
        class Types():
            """"""
            def __init__(self):
                '''Plasma.RunnerContext.Types Plasma.RunnerContext.Types.__init__()'''
                return Plasma.RunnerContext.Types()
            def __init__(self):
                '''int Plasma.RunnerContext.Types.__init__()'''
                return int()
            def __init__(self):
                '''void Plasma.RunnerContext.Types.__init__()'''
            def __bool__(self):
                '''int Plasma.RunnerContext.Types.__bool__()'''
                return int()
            def __ne__(self, f):
                '''bool Plasma.RunnerContext.Types.__ne__(Plasma.RunnerContext.Types f)'''
                return bool()
            def __eq__(self, f):
                '''bool Plasma.RunnerContext.Types.__eq__(Plasma.RunnerContext.Types f)'''
                return bool()
            def __invert__(self):
                '''Plasma.RunnerContext.Types Plasma.RunnerContext.Types.__invert__()'''
                return Plasma.RunnerContext.Types()
            def __and__(self, mask):
                '''Plasma.RunnerContext.Types Plasma.RunnerContext.Types.__and__(int mask)'''
                return Plasma.RunnerContext.Types()
            def __xor__(self, f):
                '''Plasma.RunnerContext.Types Plasma.RunnerContext.Types.__xor__(Plasma.RunnerContext.Types f)'''
                return Plasma.RunnerContext.Types()
            def __xor__(self, f):
                '''Plasma.RunnerContext.Types Plasma.RunnerContext.Types.__xor__(int f)'''
                return Plasma.RunnerContext.Types()
            def __or__(self, f):
                '''Plasma.RunnerContext.Types Plasma.RunnerContext.Types.__or__(Plasma.RunnerContext.Types f)'''
                return Plasma.RunnerContext.Types()
            def __or__(self, f):
                '''Plasma.RunnerContext.Types Plasma.RunnerContext.Types.__or__(int f)'''
                return Plasma.RunnerContext.Types()
            def __int__(self):
                '''int Plasma.RunnerContext.Types.__int__()'''
                return int()
            def __ixor__(self, f):
                '''Plasma.RunnerContext.Types Plasma.RunnerContext.Types.__ixor__(Plasma.RunnerContext.Types f)'''
                return Plasma.RunnerContext.Types()
            def __ior__(self, f):
                '''Plasma.RunnerContext.Types Plasma.RunnerContext.Types.__ior__(Plasma.RunnerContext.Types f)'''
                return Plasma.RunnerContext.Types()
            def __iand__(self, mask):
                '''Plasma.RunnerContext.Types Plasma.RunnerContext.Types.__iand__(int mask)'''
                return Plasma.RunnerContext.Types()
    class Delegate(QAbstractItemDelegate):
        """"""
        # Enum Plasma.Delegate.ColumnType
        MainColumn = 0
        SecondaryActionColumn = 0
    
        # Enum Plasma.Delegate.SpecificRoles
        SubTitleRole = 0
        SubTitleMandatoryRole = 0
        ColumnTypeRole = 0
    
        def __init__(self, parent = None):
            '''void Plasma.Delegate.__init__(QObject parent = None)'''
        def sizeHint(self, option, index):
            '''QSize Plasma.Delegate.sizeHint(QStyleOptionViewItem option, QModelIndex index)'''
            return QSize()
        def emptyRect(self, option, index):
            '''QRect Plasma.Delegate.emptyRect(QStyleOptionViewItem option, QModelIndex index)'''
            return QRect()
        def rectAfterSubTitle(self, option, index):
            '''QRect Plasma.Delegate.rectAfterSubTitle(QStyleOptionViewItem option, QModelIndex index)'''
            return QRect()
        def rectAfterTitle(self, option, index):
            '''QRect Plasma.Delegate.rectAfterTitle(QStyleOptionViewItem option, QModelIndex index)'''
            return QRect()
        def showToolTip(self):
            '''bool Plasma.Delegate.showToolTip()'''
            return bool()
        def paint(self, painter, option, index):
            '''void Plasma.Delegate.paint(QPainter painter, QStyleOptionViewItem option, QModelIndex index)'''
        def roleMapping(self, role):
            '''int Plasma.Delegate.roleMapping(Plasma.Delegate.SpecificRoles role)'''
            return int()
        def setRoleMapping(self, role, actual):
            '''void Plasma.Delegate.setRoleMapping(Plasma.Delegate.SpecificRoles role, int actual)'''
    class Animation():
        """"""
        class Reference():
            """"""
            def __init__(self):
                '''Plasma.Animation.Reference Plasma.Animation.Reference.__init__()'''
                return Plasma.Animation.Reference()
            def __init__(self):
                '''int Plasma.Animation.Reference.__init__()'''
                return int()
            def __init__(self):
                '''void Plasma.Animation.Reference.__init__()'''
            def __bool__(self):
                '''int Plasma.Animation.Reference.__bool__()'''
                return int()
            def __ne__(self, f):
                '''bool Plasma.Animation.Reference.__ne__(Plasma.Animation.Reference f)'''
                return bool()
            def __eq__(self, f):
                '''bool Plasma.Animation.Reference.__eq__(Plasma.Animation.Reference f)'''
                return bool()
            def __invert__(self):
                '''Plasma.Animation.Reference Plasma.Animation.Reference.__invert__()'''
                return Plasma.Animation.Reference()
            def __and__(self, mask):
                '''Plasma.Animation.Reference Plasma.Animation.Reference.__and__(int mask)'''
                return Plasma.Animation.Reference()
            def __xor__(self, f):
                '''Plasma.Animation.Reference Plasma.Animation.Reference.__xor__(Plasma.Animation.Reference f)'''
                return Plasma.Animation.Reference()
            def __xor__(self, f):
                '''Plasma.Animation.Reference Plasma.Animation.Reference.__xor__(int f)'''
                return Plasma.Animation.Reference()
            def __or__(self, f):
                '''Plasma.Animation.Reference Plasma.Animation.Reference.__or__(Plasma.Animation.Reference f)'''
                return Plasma.Animation.Reference()
            def __or__(self, f):
                '''Plasma.Animation.Reference Plasma.Animation.Reference.__or__(int f)'''
                return Plasma.Animation.Reference()
            def __int__(self):
                '''int Plasma.Animation.Reference.__int__()'''
                return int()
            def __ixor__(self, f):
                '''Plasma.Animation.Reference Plasma.Animation.Reference.__ixor__(Plasma.Animation.Reference f)'''
                return Plasma.Animation.Reference()
            def __ior__(self, f):
                '''Plasma.Animation.Reference Plasma.Animation.Reference.__ior__(Plasma.Animation.Reference f)'''
                return Plasma.Animation.Reference()
            def __iand__(self, mask):
                '''Plasma.Animation.Reference Plasma.Animation.Reference.__iand__(int mask)'''
                return Plasma.Animation.Reference()
    class TextEdit(QGraphicsProxyWidget):
        """"""
        def __init__(self, parent = None):
            '''void Plasma.TextEdit.__init__(QGraphicsWidget parent = None)'''
        def focusOutEvent(self, event):
            '''void Plasma.TextEdit.focusOutEvent(QFocusEvent event)'''
        def mousePressEvent(self, event):
            '''void Plasma.TextEdit.mousePressEvent(QGraphicsSceneMouseEvent event)'''
        def append(self, text):
            '''void Plasma.TextEdit.append(QString text)'''
        def contextMenuEvent(self, event):
            '''void Plasma.TextEdit.contextMenuEvent(QGraphicsSceneContextMenuEvent event)'''
        def isReadOnly(self):
            '''bool Plasma.TextEdit.isReadOnly()'''
            return bool()
        def setReadOnly(self, readOnly):
            '''void Plasma.TextEdit.setReadOnly(bool readOnly)'''
        def changeEvent(self, event):
            '''void Plasma.TextEdit.changeEvent(QEvent event)'''
        def setNativeWidget(self, nativeWidget):
            '''void Plasma.TextEdit.setNativeWidget(KTextEdit nativeWidget)'''
        def resizeEvent(self, event):
            '''void Plasma.TextEdit.resizeEvent(QGraphicsSceneResizeEvent event)'''
        textChanged = pyqtSignal() # void textChanged() - signal
        def dataUpdated(self, sourceName, data):
            '''void Plasma.TextEdit.dataUpdated(QString sourceName, dict-of-QString-QVariant data)'''
        def nativeWidget(self):
            '''KTextEdit Plasma.TextEdit.nativeWidget()'''
            return KTextEdit()
        def styleSheet(self):
            '''QString Plasma.TextEdit.styleSheet()'''
            return QString()
        def setStyleSheet(self, stylesheet):
            '''void Plasma.TextEdit.setStyleSheet(QString stylesheet)'''
        def text(self):
            '''QString Plasma.TextEdit.text()'''
            return QString()
        def setText(self, text):
            '''void Plasma.TextEdit.setText(QString text)'''
    class Context(QObject):
        """"""
        def __init__(self, parent = None):
            '''void Plasma.Context.__init__(QObject parent = None)'''
        def currentActivityId(self):
            '''QString Plasma.Context.currentActivityId()'''
            return QString()
        def setCurrentActivityId(self, id):
            '''void Plasma.Context.setCurrentActivityId(QString id)'''
        locationChanged = pyqtSignal() # void locationChanged(Plasma::Context *) - signal
        activityChanged = pyqtSignal() # void activityChanged(Plasma::Context *) - signal
        changed = pyqtSignal() # void changed(Plasma::Context *) - signal
        def currentActivity(self):
            '''QString Plasma.Context.currentActivity()'''
            return QString()
        def setCurrentActivity(self, name):
            '''void Plasma.Context.setCurrentActivity(QString name)'''
        def listActivities(self):
            '''QStringList Plasma.Context.listActivities()'''
            return QStringList()
        def createActivity(self, name):
            '''void Plasma.Context.createActivity(QString name)'''
    class Meter(QGraphicsWidget):
        """"""
        # Enum Plasma.Meter.MeterType
        BarMeterHorizontal = 0
        BarMeterVertical = 0
        AnalogMeter = 0
    
        def __init__(self, parent = None):
            '''void Plasma.Meter.__init__(QGraphicsItem parent = None)'''
        valueChanged = pyqtSignal() # void valueChanged(const intamp;) - signal
        def sizeHint(self, which, constraint = QSizeF()):
            '''QSizeF Plasma.Meter.sizeHint(Qt.SizeHint which, QSizeF constraint = QSizeF())'''
            return QSizeF()
        def paint(self, p, option, widget = None):
            '''void Plasma.Meter.paint(QPainter p, QStyleOptionGraphicsItem option, QWidget widget = None)'''
        def dataUpdated(self, sourceName, data):
            '''void Plasma.Meter.dataUpdated(QString sourceName, dict-of-QString-QVariant data)'''
        def labelRect(self, index):
            '''QRectF Plasma.Meter.labelRect(int index)'''
            return QRectF()
        def labelAlignment(self, index):
            '''Qt.Alignment Plasma.Meter.labelAlignment(int index)'''
            return Qt.Alignment()
        def setLabelAlignment(self, index, alignment):
            '''void Plasma.Meter.setLabelAlignment(int index, Qt.Alignment alignment)'''
        def labelFont(self, index):
            '''QFont Plasma.Meter.labelFont(int index)'''
            return QFont()
        def setLabelFont(self, index, font):
            '''void Plasma.Meter.setLabelFont(int index, QFont font)'''
        def labelColor(self, index):
            '''QColor Plasma.Meter.labelColor(int index)'''
            return QColor()
        def setLabelColor(self, index, color):
            '''void Plasma.Meter.setLabelColor(int index, QColor color)'''
        def label(self, index):
            '''QString Plasma.Meter.label(int index)'''
            return QString()
        def setLabel(self, index, text):
            '''void Plasma.Meter.setLabel(int index, QString text)'''
        def meterType(self):
            '''Plasma.Meter.MeterType Plasma.Meter.meterType()'''
            return Plasma.Meter.MeterType()
        def setMeterType(self, type):
            '''void Plasma.Meter.setMeterType(Plasma.Meter.MeterType type)'''
        def svg(self):
            '''QString Plasma.Meter.svg()'''
            return QString()
        def setSvg(self, svg):
            '''void Plasma.Meter.setSvg(QString svg)'''
        def value(self):
            '''int Plasma.Meter.value()'''
            return int()
        def setValue(self, value):
            '''void Plasma.Meter.setValue(int value)'''
        def minimum(self):
            '''int Plasma.Meter.minimum()'''
            return int()
        def setMinimum(self, minimum):
            '''void Plasma.Meter.setMinimum(int minimum)'''
        def maximum(self):
            '''int Plasma.Meter.maximum()'''
            return int()
        def setMaximum(self, maximum):
            '''void Plasma.Meter.setMaximum(int maximum)'''
    class AuthorizationRule(QObject):
        """"""
        # Enum Plasma.AuthorizationRule.Target
        Default = 0
        AllUsers = 0
        AllServices = 0
    
        # Enum Plasma.AuthorizationRule.Persistence
        Transient = 0
        Persistent = 0
    
        # Enum Plasma.AuthorizationRule.Policy
        Deny = 0
        Allow = 0
        PinRequired = 0
    
        changed = pyqtSignal() # void changed(Plasma::AuthorizationRule *) - signal
        def serviceName(self):
            '''QString Plasma.AuthorizationRule.serviceName()'''
            return QString()
        def pin(self):
            '''QString Plasma.AuthorizationRule.pin()'''
            return QString()
        def setPin(self, pin):
            '''void Plasma.AuthorizationRule.setPin(QString pin)'''
        def persistence(self):
            '''Plasma.AuthorizationRule.Persistence Plasma.AuthorizationRule.persistence()'''
            return Plasma.AuthorizationRule.Persistence()
        def setPersistence(self, persistence):
            '''void Plasma.AuthorizationRule.setPersistence(Plasma.AuthorizationRule.Persistence persistence)'''
        def policy(self):
            '''Plasma.AuthorizationRule.Policy Plasma.AuthorizationRule.policy()'''
            return Plasma.AuthorizationRule.Policy()
        def setPolicy(self, policy):
            '''void Plasma.AuthorizationRule.setPolicy(Plasma.AuthorizationRule.Policy policy)'''
        def description(self):
            '''QString Plasma.AuthorizationRule.description()'''
            return QString()
    class ComboBox(QGraphicsProxyWidget):
        """"""
        def __init__(self, parent = None):
            '''void Plasma.ComboBox.__init__(QGraphicsWidget parent = None)'''
        currentIndexChanged = pyqtSignal() # void currentIndexChanged(int) - signal
        def setCurrentIndex(self, index):
            '''void Plasma.ComboBox.setCurrentIndex(int index)'''
        def currentIndex(self):
            '''int Plasma.ComboBox.currentIndex()'''
            return int()
        def count(self):
            '''int Plasma.ComboBox.count()'''
            return int()
        def mousePressEvent(self, event):
            '''void Plasma.ComboBox.mousePressEvent(QGraphicsSceneMouseEvent event)'''
        def changeEvent(self, event):
            '''void Plasma.ComboBox.changeEvent(QEvent event)'''
        def focusOutEvent(self, event):
            '''void Plasma.ComboBox.focusOutEvent(QFocusEvent event)'''
        def focusInEvent(self, event):
            '''void Plasma.ComboBox.focusInEvent(QFocusEvent event)'''
        def setNativeWidget(self, nativeWidget):
            '''void Plasma.ComboBox.setNativeWidget(KComboBox nativeWidget)'''
        textChanged = pyqtSignal() # void textChanged(const QStringamp;) - signal
        def hoverLeaveEvent(self, event):
            '''void Plasma.ComboBox.hoverLeaveEvent(QGraphicsSceneHoverEvent event)'''
        def hoverEnterEvent(self, event):
            '''void Plasma.ComboBox.hoverEnterEvent(QGraphicsSceneHoverEvent event)'''
        def paint(self, painter, option, widget):
            '''void Plasma.ComboBox.paint(QPainter painter, QStyleOptionGraphicsItem option, QWidget widget)'''
        def resizeEvent(self, event):
            '''void Plasma.ComboBox.resizeEvent(QGraphicsSceneResizeEvent event)'''
        activated = pyqtSignal() # void activated(const QStringamp;) - signal
        def clear(self):
            '''void Plasma.ComboBox.clear()'''
        def addItem(self, text):
            '''void Plasma.ComboBox.addItem(QString text)'''
        def nativeWidget(self):
            '''KComboBox Plasma.ComboBox.nativeWidget()'''
            return KComboBox()
        def styleSheet(self):
            '''QString Plasma.ComboBox.styleSheet()'''
            return QString()
        def setStyleSheet(self, stylesheet):
            '''void Plasma.ComboBox.setStyleSheet(QString stylesheet)'''
        def text(self):
            '''QString Plasma.ComboBox.text()'''
            return QString()
    class TextBrowser(QGraphicsProxyWidget):
        """"""
        def __init__(self, parent = None):
            '''void Plasma.TextBrowser.__init__(QGraphicsWidget parent = None)'''
        def append(self, text):
            '''void Plasma.TextBrowser.append(QString text)'''
        def contextMenuEvent(self, event):
            '''void Plasma.TextBrowser.contextMenuEvent(QGraphicsSceneContextMenuEvent event)'''
        def changeEvent(self, event):
            '''void Plasma.TextBrowser.changeEvent(QEvent event)'''
        def wheelEvent(self, event):
            '''void Plasma.TextBrowser.wheelEvent(QGraphicsSceneWheelEvent event)'''
        def resizeEvent(self, event):
            '''void Plasma.TextBrowser.resizeEvent(QGraphicsSceneResizeEvent event)'''
        textChanged = pyqtSignal() # void textChanged() - signal
        def dataUpdated(self, sourceName, data):
            '''void Plasma.TextBrowser.dataUpdated(QString sourceName, dict-of-QString-QVariant data)'''
        def nativeWidget(self):
            '''KTextBrowser Plasma.TextBrowser.nativeWidget()'''
            return KTextBrowser()
        def styleSheet(self):
            '''QString Plasma.TextBrowser.styleSheet()'''
            return QString()
        def setStyleSheet(self, stylesheet):
            '''void Plasma.TextBrowser.setStyleSheet(QString stylesheet)'''
        def setVerticalScrollBarPolicy(self, policy):
            '''void Plasma.TextBrowser.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy policy)'''
        def setHorizontalScrollBarPolicy(self, policy):
            '''void Plasma.TextBrowser.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy policy)'''
        def text(self):
            '''QString Plasma.TextBrowser.text()'''
            return QString()
        def setText(self, text):
            '''void Plasma.TextBrowser.setText(QString text)'''
    class Containment(Plasma.Applet):
        """"""
        # Enum Plasma.Containment.Type
        NoContainmentType = 0
        DesktopContainment = 0
        PanelContainment = 0
        CustomContainment = 0
        CustomPanelContainment = 0
    
        def __init__(self, parent = None, serviceId = QString(), containmentId = 0):
            '''void Plasma.Containment.__init__(QGraphicsItem parent = None, QString serviceId = QString(), int containmentId = 0)'''
        def __init__(self, parent, args):
            '''void Plasma.Containment.__init__(QObject parent, list-of-QVariant args)'''
        def configChanged(self):
            '''void Plasma.Containment.configChanged()'''
        def containmentActionsConfig(self):
            '''KConfigGroup Plasma.Containment.containmentActionsConfig()'''
            return KConfigGroup()
        def isToolBoxOpen(self):
            '''bool Plasma.Containment.isToolBoxOpen()'''
            return bool()
        def lastDesktop(self):
            '''int Plasma.Containment.lastDesktop()'''
            return int()
        def lastScreen(self):
            '''int Plasma.Containment.lastScreen()'''
            return int()
        def context(self):
            '''Plasma.Context Plasma.Containment.context()'''
            return Plasma.Context()
        def toolBox(self):
            '''Plasma.AbstractToolBox Plasma.Containment.toolBox()'''
            return Plasma.AbstractToolBox()
        def setToolBox(self, toolBox):
            '''void Plasma.Containment.setToolBox(Plasma.AbstractToolBox toolBox)'''
        def dragLeaveEvent(self, event):
            '''void Plasma.Containment.dragLeaveEvent(QGraphicsSceneDragDropEvent event)'''
        def containmentActions(self, trigger):
            '''QString Plasma.Containment.containmentActions(QString trigger)'''
            return QString()
        def containmentActionsTriggers(self):
            '''QStringList Plasma.Containment.containmentActionsTriggers()'''
            return QStringList()
        def setContainmentActions(self, trigger, pluginName):
            '''void Plasma.Containment.setContainmentActions(QString trigger, QString pluginName)'''
        def itemChange(self, change, value):
            '''QVariant Plasma.Containment.itemChange(QGraphicsItem.GraphicsItemChange change, QVariant value)'''
            return QVariant()
        def toolBoxItem(self):
            '''QGraphicsItem Plasma.Containment.toolBoxItem()'''
            return QGraphicsItem()
        def resizeEvent(self, event):
            '''void Plasma.Containment.resizeEvent(QGraphicsSceneResizeEvent event)'''
        def dropEvent(self, event):
            '''void Plasma.Containment.dropEvent(QGraphicsSceneDragDropEvent event)'''
        def dragMoveEvent(self, event):
            '''void Plasma.Containment.dragMoveEvent(QGraphicsSceneDragDropEvent event)'''
        def dragEnterEvent(self, event):
            '''void Plasma.Containment.dragEnterEvent(QGraphicsSceneDragDropEvent event)'''
        def sceneEventFilter(self, watched, event):
            '''bool Plasma.Containment.sceneEventFilter(QGraphicsItem watched, QEvent event)'''
            return bool()
        def wheelEvent(self, event):
            '''void Plasma.Containment.wheelEvent(QGraphicsSceneWheelEvent event)'''
        def keyPressEvent(self, event):
            '''void Plasma.Containment.keyPressEvent(QKeyEvent event)'''
        def contextMenuEvent(self, event):
            '''void Plasma.Containment.contextMenuEvent(QGraphicsSceneContextMenuEvent event)'''
        def mouseReleaseEvent(self, event):
            '''void Plasma.Containment.mouseReleaseEvent(QGraphicsSceneMouseEvent event)'''
        def mousePressEvent(self, event):
            '''void Plasma.Containment.mousePressEvent(QGraphicsSceneMouseEvent event)'''
        def mouseMoveEvent(self, event):
            '''void Plasma.Containment.mouseMoveEvent(QGraphicsSceneMouseEvent event)'''
        def restoreContents(self, group):
            '''void Plasma.Containment.restoreContents(KConfigGroup group)'''
        def saveContents(self, group):
            '''void Plasma.Containment.saveContents(KConfigGroup group)'''
        def setDrawWallpaper(self, drawWallpaper):
            '''void Plasma.Containment.setDrawWallpaper(bool drawWallpaper)'''
        def setContainmentType(self, type):
            '''void Plasma.Containment.setContainmentType(Plasma.Containment.Type type)'''
        def showConfigurationInterface(self):
            '''void Plasma.Containment.showConfigurationInterface()'''
        def destroy(self):
            '''void Plasma.Containment.destroy()'''
        def destroy(self, confirm):
            '''void Plasma.Containment.destroy(bool confirm)'''
        def focusPreviousApplet(self):
            '''void Plasma.Containment.focusPreviousApplet()'''
        def focusNextApplet(self):
            '''void Plasma.Containment.focusNextApplet()'''
        def setFormFactor(self, formFactor):
            '''void Plasma.Containment.setFormFactor(Plasma.FormFactor formFactor)'''
        def setLocation(self, location):
            '''void Plasma.Containment.setLocation(Plasma.Location location)'''
        contextChanged = pyqtSignal() # void contextChanged(Plasma::Context *) - signal
        configureRequested = pyqtSignal() # void configureRequested(Plasma::Containment *) - signal
        screenChanged = pyqtSignal() # void screenChanged(int,int,Plasma::Containment *) - signal
        showAddWidgetsInterface = pyqtSignal() # void showAddWidgetsInterface(const QPointFamp;) - signal
        addSiblingContainment = pyqtSignal() # void addSiblingContainment(Plasma::Containment *) - signal
        def addSiblingContainment(self):
            '''void Plasma.Containment.addSiblingContainment()'''
        toolBoxVisibilityChanged = pyqtSignal() # void toolBoxVisibilityChanged(bool) - signal
        toolBoxToggled = pyqtSignal() # void toolBoxToggled() - signal
        zoomRequested = pyqtSignal() # void zoomRequested(Plasma::Containment *,Plasma::ZoomDirection) - signal
        appletRemoved = pyqtSignal() # void appletRemoved(Plasma::Applet *) - signal
        appletAdded = pyqtSignal() # void appletAdded(Plasma::Applet *,const QPointFamp;) - signal
        def showDropZone(self, pos):
            '''void Plasma.Containment.showDropZone(QPoint pos)'''
        def showContextMenu(self, containmentPos, screenPos):
            '''void Plasma.Containment.showContextMenu(QPointF containmentPos, QPoint screenPos)'''
        def activity(self):
            '''QString Plasma.Containment.activity()'''
            return QString()
        def setActivity(self, activity):
            '''void Plasma.Containment.setActivity(QString activity)'''
        def wallpaper(self):
            '''Plasma.Wallpaper Plasma.Containment.wallpaper()'''
            return Plasma.Wallpaper()
        def setWallpaper(self, pluginName, mode = QString()):
            '''void Plasma.Containment.setWallpaper(QString pluginName, QString mode = QString())'''
        def drawWallpaper(self):
            '''bool Plasma.Containment.drawWallpaper()'''
            return bool()
        def removeAssociatedWidget(self, widget):
            '''void Plasma.Containment.removeAssociatedWidget(QWidget widget)'''
        def addAssociatedWidget(self, widget):
            '''void Plasma.Containment.addAssociatedWidget(QWidget widget)'''
        def closeToolBox(self):
            '''void Plasma.Containment.closeToolBox()'''
        def openToolBox(self):
            '''void Plasma.Containment.openToolBox()'''
        def setToolBoxOpen(self, open):
            '''void Plasma.Containment.setToolBoxOpen(bool open)'''
        def removeToolBoxAction(self, action):
            '''void Plasma.Containment.removeToolBoxAction(QAction action)'''
        def addToolBoxAction(self, action):
            '''void Plasma.Containment.addToolBoxAction(QAction action)'''
        def enableAction(self, name, enable):
            '''void Plasma.Containment.enableAction(QString name, bool enable)'''
        def restore(self, group):
            '''void Plasma.Containment.restore(KConfigGroup group)'''
        def save(self, group):
            '''void Plasma.Containment.save(KConfigGroup group)'''
        def desktop(self):
            '''int Plasma.Containment.desktop()'''
            return int()
        def screen(self):
            '''int Plasma.Containment.screen()'''
            return int()
        def setScreen(self, screen, desktop = None):
            '''void Plasma.Containment.setScreen(int screen, int desktop = -1)'''
        def clearApplets(self):
            '''void Plasma.Containment.clearApplets()'''
        def applets(self):
            '''list-of-Plasma.Applet Plasma.Containment.applets()'''
            return [Plasma.Applet()]
        def addApplet(self, name, args = QVariantList(), geometry = None):
            '''Plasma.Applet Plasma.Containment.addApplet(QString name, list-of-QVariant args = QVariantList(), QRectF geometry = QRectF(-1,-1,-1,-1))'''
            return Plasma.Applet()
        def addApplet(self, applet, pos = None, dontInit = True):
            '''void Plasma.Containment.addApplet(Plasma.Applet applet, QPointF pos = QPointF(-1,-1), bool dontInit = True)'''
        def listContainmentsForMimetype(self, mimetype):
            '''static list-of-KPluginInfo Plasma.Containment.listContainmentsForMimetype(QString mimetype)'''
            return [KPluginInfo()]
        def listContainmentTypes(self):
            '''static QStringList Plasma.Containment.listContainmentTypes()'''
            return QStringList()
        def listContainmentsOfType(self, type, category = QString(), parentApp = QString()):
            '''static list-of-KPluginInfo Plasma.Containment.listContainmentsOfType(QString type, QString category = QString(), QString parentApp = QString())'''
            return [KPluginInfo()]
        def listContainments(self, category = QString(), parentApp = QString()):
            '''static list-of-KPluginInfo Plasma.Containment.listContainments(QString category = QString(), QString parentApp = QString())'''
            return [KPluginInfo()]
        def corona(self):
            '''Plasma.Corona Plasma.Containment.corona()'''
            return Plasma.Corona()
        def containmentType(self):
            '''Plasma.Containment.Type Plasma.Containment.containmentType()'''
            return Plasma.Containment.Type()
        def init(self):
            '''void Plasma.Containment.init()'''
    class AuthorizationInterface():
        """"""
        def __init__(self):
            '''void Plasma.AuthorizationInterface.__init__()'''
        def __init__(self):
            '''Plasma.AuthorizationInterface Plasma.AuthorizationInterface.__init__()'''
            return Plasma.AuthorizationInterface()
        def clientPinRequest(self, request):
            '''abstract void Plasma.AuthorizationInterface.clientPinRequest(Plasma.ClientPinRequest request)'''
        def authorizationRequest(self, rule):
            '''abstract void Plasma.AuthorizationInterface.authorizationRequest(Plasma.AuthorizationRule rule)'''
    class Label(QGraphicsProxyWidget):
        """"""
        def __init__(self, parent = None):
            '''void Plasma.Label.__init__(QGraphicsWidget parent = None)'''
        def sizeHint(self, which, constraint):
            '''QSizeF Plasma.Label.sizeHint(Qt.SizeHint which, QSizeF constraint)'''
            return QSizeF()
        def itemChange(self, change, value):
            '''QVariant Plasma.Label.itemChange(QGraphicsItem.GraphicsItemChange change, QVariant value)'''
            return QVariant()
        def mouseMoveEvent(self, event):
            '''void Plasma.Label.mouseMoveEvent(QGraphicsSceneMouseEvent event)'''
        def wordWrap(self):
            '''bool Plasma.Label.wordWrap()'''
            return bool()
        def setWordWrap(self, wrap):
            '''void Plasma.Label.setWordWrap(bool wrap)'''
        def contextMenuEvent(self, event):
            '''void Plasma.Label.contextMenuEvent(QGraphicsSceneContextMenuEvent event)'''
        def event(self, event):
            '''bool Plasma.Label.event(QEvent event)'''
            return bool()
        def changeEvent(self, event):
            '''void Plasma.Label.changeEvent(QEvent event)'''
        def paint(self, painter, option, widget):
            '''void Plasma.Label.paint(QPainter painter, QStyleOptionGraphicsItem option, QWidget widget)'''
        def mousePressEvent(self, event):
            '''void Plasma.Label.mousePressEvent(QGraphicsSceneMouseEvent event)'''
        def textSelectable(self):
            '''bool Plasma.Label.textSelectable()'''
            return bool()
        def setTextSelectable(self, enable):
            '''void Plasma.Label.setTextSelectable(bool enable)'''
        def resizeEvent(self, event):
            '''void Plasma.Label.resizeEvent(QGraphicsSceneResizeEvent event)'''
        def dataUpdated(self, sourceName, data):
            '''void Plasma.Label.dataUpdated(QString sourceName, dict-of-QString-QVariant data)'''
        linkHovered = pyqtSignal() # void linkHovered(const QStringamp;) - signal
        linkActivated = pyqtSignal() # void linkActivated(const QStringamp;) - signal
        def nativeWidget(self):
            '''QLabel Plasma.Label.nativeWidget()'''
            return QLabel()
        def styleSheet(self):
            '''QString Plasma.Label.styleSheet()'''
            return QString()
        def setStyleSheet(self, stylesheet):
            '''void Plasma.Label.setStyleSheet(QString stylesheet)'''
        def hasScaledContents(self):
            '''bool Plasma.Label.hasScaledContents()'''
            return bool()
        def setScaledContents(self, scaled):
            '''void Plasma.Label.setScaledContents(bool scaled)'''
        def alignment(self):
            '''Qt.Alignment Plasma.Label.alignment()'''
            return Qt.Alignment()
        def setAlignment(self, alignment):
            '''void Plasma.Label.setAlignment(Qt.Alignment alignment)'''
        def image(self):
            '''QString Plasma.Label.image()'''
            return QString()
        def setImage(self, path):
            '''void Plasma.Label.setImage(QString path)'''
        def text(self):
            '''QString Plasma.Label.text()'''
            return QString()
        def setText(self, text):
            '''void Plasma.Label.setText(QString text)'''
    class Service(QObject):
        """"""
        def __init__(self, parent = None):
            '''void Plasma.Service.__init__(QObject parent = None)'''
        def __init__(self, parent, args):
            '''void Plasma.Service.__init__(QObject parent, list-of-QVariant args)'''
        serviceReady = pyqtSignal() # void serviceReady(Plasma::Service *) - signal
        def parametersFromDescription(self, description):
            '''dict-of-QString-QVariant Plasma.Service.parametersFromDescription(KConfigGroup description)'''
            return dict-of-QString-QVariant()
        def access(self, url, parent = None):
            '''static Plasma.Service Plasma.Service.access(KUrl url, QObject parent = None)'''
            return Plasma.Service()
        def setOperationEnabled(self, operation, enable):
            '''void Plasma.Service.setOperationEnabled(QString operation, bool enable)'''
        def setName(self, name):
            '''void Plasma.Service.setName(QString name)'''
        def setOperationsScheme(self, xml):
            '''void Plasma.Service.setOperationsScheme(QIODevice xml)'''
        def registerOperationsScheme(self):
            '''void Plasma.Service.registerOperationsScheme()'''
        def createJob(self, operation, parameters):
            '''abstract Plasma.ServiceJob Plasma.Service.createJob(QString operation, dict-of-QString-QVariant parameters)'''
            return Plasma.ServiceJob()
        operationsChanged = pyqtSignal() # void operationsChanged() - signal
        finished = pyqtSignal() # void finished(Plasma::ServiceJob *) - signal
        def disassociateWidget(self, widget):
            '''void Plasma.Service.disassociateWidget(QWidget widget)'''
        def disassociateWidget(self, widget):
            '''void Plasma.Service.disassociateWidget(QGraphicsWidget widget)'''
        def associateWidget(self, widget, operation):
            '''void Plasma.Service.associateWidget(QWidget widget, QString operation)'''
        def associateWidget(self, widget, operation):
            '''void Plasma.Service.associateWidget(QGraphicsWidget widget, QString operation)'''
        def name(self):
            '''QString Plasma.Service.name()'''
            return QString()
        def isOperationEnabled(self, operation):
            '''bool Plasma.Service.isOperationEnabled(QString operation)'''
            return bool()
        def startOperationCall(self, description, parent = None):
            '''Plasma.ServiceJob Plasma.Service.startOperationCall(KConfigGroup description, QObject parent = None)'''
            return Plasma.ServiceJob()
        def operationDescription(self, operationName):
            '''KConfigGroup Plasma.Service.operationDescription(QString operationName)'''
            return KConfigGroup()
        def operationNames(self):
            '''QStringList Plasma.Service.operationNames()'''
            return QStringList()
        def destination(self):
            '''QString Plasma.Service.destination()'''
            return QString()
        def setDestination(self, destination):
            '''void Plasma.Service.setDestination(QString destination)'''
        def load(self, name, parent = None):
            '''static Plasma.Service Plasma.Service.load(QString name, QObject parent = None)'''
            return Plasma.Service()
        def load(self, name, args, parent = None):
            '''static Plasma.Service Plasma.Service.load(QString name, list-of-QVariant args, QObject parent = None)'''
            return Plasma.Service()
    class AccessAppletJob(KJob):
        """"""
        def __init__(self, location, parent = None):
            '''void Plasma.AccessAppletJob.__init__(KUrl location, QObject parent = None)'''
        def start(self):
            '''void Plasma.AccessAppletJob.start()'''
        def applet(self):
            '''Plasma.Applet Plasma.AccessAppletJob.applet()'''
            return Plasma.Applet()
    class DataEngineScript(Plasma.ScriptEngine):
        """"""
        def __init__(self, parent = None):
            '''void Plasma.DataEngineScript.__init__(QObject parent = None)'''
        def description(self):
            '''KPluginInfo Plasma.DataEngineScript.description()'''
            return KPluginInfo()
        def forceImmediateUpdateOfAllVisualizations(self):
            '''void Plasma.DataEngineScript.forceImmediateUpdateOfAllVisualizations()'''
        def updateAllSources(self):
            '''void Plasma.DataEngineScript.updateAllSources()'''
        def removeSource(self, source):
            '''void Plasma.DataEngineScript.removeSource(QString source)'''
        def scheduleSourcesUpdated(self):
            '''void Plasma.DataEngineScript.scheduleSourcesUpdated()'''
        def setIcon(self, icon):
            '''void Plasma.DataEngineScript.setIcon(QString icon)'''
        def setName(self, name):
            '''void Plasma.DataEngineScript.setName(QString name)'''
        def containerDict(self):
            '''unknown-type Plasma.DataEngineScript.containerDict()'''
            return unknown-type()
        def addSource(self, source):
            '''void Plasma.DataEngineScript.addSource(Plasma.DataContainer source)'''
        def removeAllSources(self):
            '''void Plasma.DataEngineScript.removeAllSources()'''
        def setPollingInterval(self, frequency):
            '''void Plasma.DataEngineScript.setPollingInterval(int frequency)'''
        def minimumPollingInterval(self):
            '''int Plasma.DataEngineScript.minimumPollingInterval()'''
            return int()
        def setMinimumPollingInterval(self, minimumMs):
            '''void Plasma.DataEngineScript.setMinimumPollingInterval(int minimumMs)'''
        def setMaxSourceCount(self, limit):
            '''void Plasma.DataEngineScript.setMaxSourceCount(int limit)'''
        def removeData(self, source, key):
            '''void Plasma.DataEngineScript.removeData(QString source, QString key)'''
        def removeAllData(self, source):
            '''void Plasma.DataEngineScript.removeAllData(QString source)'''
        def setData(self, source, key, value):
            '''void Plasma.DataEngineScript.setData(QString source, QString key, QVariant value)'''
        def setData(self, source, value):
            '''void Plasma.DataEngineScript.setData(QString source, QVariant value)'''
        def setData(self, source, values):
            '''void Plasma.DataEngineScript.setData(QString source, dict-of-QString-QVariant values)'''
        def package(self):
            '''Plasma.Package Plasma.DataEngineScript.package()'''
            return Plasma.Package()
        def mainScript(self):
            '''QString Plasma.DataEngineScript.mainScript()'''
            return QString()
        def serviceForSource(self, source):
            '''Plasma.Service Plasma.DataEngineScript.serviceForSource(QString source)'''
            return Plasma.Service()
        def updateSourceEvent(self, source):
            '''bool Plasma.DataEngineScript.updateSourceEvent(QString source)'''
            return bool()
        def sourceRequestEvent(self, name):
            '''bool Plasma.DataEngineScript.sourceRequestEvent(QString name)'''
            return bool()
        def sources(self):
            '''QStringList Plasma.DataEngineScript.sources()'''
            return QStringList()
        def dataEngine(self):
            '''Plasma.DataEngine Plasma.DataEngineScript.dataEngine()'''
            return Plasma.DataEngine()
        def setDataEngine(self, dataEngine):
            '''void Plasma.DataEngineScript.setDataEngine(Plasma.DataEngine dataEngine)'''
    class ScriptEngine(QObject):
        """"""
        def __init__(self, parent = None):
            '''void Plasma.ScriptEngine.__init__(QObject parent = None)'''
        def package(self):
            '''Plasma.Package Plasma.ScriptEngine.package()'''
            return Plasma.Package()
        def mainScript(self):
            '''QString Plasma.ScriptEngine.mainScript()'''
            return QString()
        def init(self):
            '''bool Plasma.ScriptEngine.init()'''
            return bool()
    class ConfigLoader(KConfigSkeleton):
        """"""
        def __init__(self, configFile, xml, parent = None):
            '''void Plasma.ConfigLoader.__init__(QString configFile, QIODevice xml, QObject parent = None)'''
        def __init__(self, config, xml, parent = None):
            '''void Plasma.ConfigLoader.__init__(KSharedConfigPtr config, QIODevice xml, QObject parent = None)'''
        def __init__(self, config, xml, parent = None):
            '''void Plasma.ConfigLoader.__init__(KConfigGroup config, QIODevice xml, QObject parent = None)'''
        def usrWriteConfig(self):
            '''void Plasma.ConfigLoader.usrWriteConfig()'''
        def groupList(self):
            '''QStringList Plasma.ConfigLoader.groupList()'''
            return QStringList()
        def hasGroup(self, group):
            '''bool Plasma.ConfigLoader.hasGroup(QString group)'''
            return bool()
        def property(self, name):
            '''QVariant Plasma.ConfigLoader.property(QString name)'''
            return QVariant()
        def findItemByName(self, name):
            '''KConfigSkeletonItem Plasma.ConfigLoader.findItemByName(QString name)'''
            return KConfigSkeletonItem()
        def findItem(self, group, key):
            '''KConfigSkeletonItem Plasma.ConfigLoader.findItem(QString group, QString key)'''
            return KConfigSkeletonItem()
    class WindowEffects():
        """"""
        # Enum Plasma.WindowEffects.Effect
        Slide = 0
        WindowPreview = 0
        PresentWindows = 0
        PresentWindowsGroup = 0
        HighlightWindows = 0
        OverrideShadow = 0
        BlurBehind = 0
        Dashboard = 0
    
        def markAsDashboard(self, window):
            '''static void Plasma.WindowEffects.markAsDashboard(int window)'''
        def enableBlurBehind(self, window, enable = True, region = QRegion()):
            '''static void Plasma.WindowEffects.enableBlurBehind(int window, bool enable = True, QRegion region = QRegion())'''
        def overrideShadow(self, window, override):
            '''static void Plasma.WindowEffects.overrideShadow(int window, bool override)'''
        def highlightWindows(self, controller, ids):
            '''static void Plasma.WindowEffects.highlightWindows(int controller, unknown-type ids)'''
        def presentWindows(self, controller, ids):
            '''static void Plasma.WindowEffects.presentWindows(int controller, unknown-type ids)'''
        def presentWindows(self, controller, desktop = None):
            '''static void Plasma.WindowEffects.presentWindows(int controller, int desktop = -1)'''
        def showWindowThumbnails(self, parent, windows = None, rects = None):
            '''static void Plasma.WindowEffects.showWindowThumbnails(int parent, unknown-type windows = QListlt;WIdgt;(), list-of-QRect rects = QListlt;QRectgt;())'''
        def windowSizes(self, ids):
            '''static list-of-QSize Plasma.WindowEffects.windowSizes(unknown-type ids)'''
            return [QSize()]
        def slideWindow(self, id, location, offset):
            '''static void Plasma.WindowEffects.slideWindow(int id, Plasma.Location location, int offset)'''
        def slideWindow(self, widget, location):
            '''static void Plasma.WindowEffects.slideWindow(QWidget widget, Plasma.Location location)'''
        def isEffectAvailable(self, effect):
            '''static bool Plasma.WindowEffects.isEffectAvailable(Plasma.WindowEffects.Effect effect)'''
            return bool()
    class ContainmentActions(QObject):
        """"""
        def __init__(self, parent = None):
            '''void Plasma.ContainmentActions.__init__(QObject parent = None)'''
        def __init__(self, parent, args):
            '''void Plasma.ContainmentActions.__init__(QObject parent, list-of-QVariant args)'''
        def setContainment(self, newContainment):
            '''void Plasma.ContainmentActions.setContainment(Plasma.Containment newContainment)'''
        def popupPosition(self, s, event):
            '''QPoint Plasma.ContainmentActions.popupPosition(QSize s, QEvent event)'''
            return QPoint()
        def paste(self, scenePos, screenPos):
            '''void Plasma.ContainmentActions.paste(QPointF scenePos, QPoint screenPos)'''
        def containment(self):
            '''Plasma.Containment Plasma.ContainmentActions.containment()'''
            return Plasma.Containment()
        def setConfigurationRequired(self, needsConfiguring = True):
            '''void Plasma.ContainmentActions.setConfigurationRequired(bool needsConfiguring = True)'''
        def init(self, config):
            '''void Plasma.ContainmentActions.init(KConfigGroup config)'''
        def event(self, e):
            '''bool Plasma.ContainmentActions.event(QEvent e)'''
            return bool()
        def eventToString(self, event):
            '''static QString Plasma.ContainmentActions.eventToString(QEvent event)'''
            return QString()
        def configurationRequired(self):
            '''bool Plasma.ContainmentActions.configurationRequired()'''
            return bool()
        def dataEngine(self, name):
            '''Plasma.DataEngine Plasma.ContainmentActions.dataEngine(QString name)'''
            return Plasma.DataEngine()
        def contextualActions(self):
            '''list-of-QAction Plasma.ContainmentActions.contextualActions()'''
            return [QAction()]
        def contextEvent(self, event):
            '''void Plasma.ContainmentActions.contextEvent(QEvent event)'''
        def configurationAccepted(self):
            '''void Plasma.ContainmentActions.configurationAccepted()'''
        def createConfigurationInterface(self, parent):
            '''QWidget Plasma.ContainmentActions.createConfigurationInterface(QWidget parent)'''
            return QWidget()
        def save(self, config):
            '''void Plasma.ContainmentActions.save(KConfigGroup config)'''
        def restore(self, config):
            '''void Plasma.ContainmentActions.restore(KConfigGroup config)'''
        def isInitialized(self):
            '''bool Plasma.ContainmentActions.isInitialized()'''
            return bool()
        def icon(self):
            '''QString Plasma.ContainmentActions.icon()'''
            return QString()
        def pluginName(self):
            '''QString Plasma.ContainmentActions.pluginName()'''
            return QString()
        def name(self):
            '''QString Plasma.ContainmentActions.name()'''
            return QString()
        def packageStructure(self):
            '''static unknown-type Plasma.ContainmentActions.packageStructure()'''
            return unknown-type()
        def load(self, parent, name, args = QVariantList()):
            '''static Plasma.ContainmentActions Plasma.ContainmentActions.load(Plasma.Containment parent, QString name, list-of-QVariant args = QVariantList())'''
            return Plasma.ContainmentActions()
        def load(self, parent, info, args = QVariantList()):
            '''static Plasma.ContainmentActions Plasma.ContainmentActions.load(Plasma.Containment parent, KPluginInfo info, list-of-QVariant args = QVariantList())'''
            return Plasma.ContainmentActions()
        def listContainmentActionsInfo(self):
            '''static list-of-KPluginInfo Plasma.ContainmentActions.listContainmentActionsInfo()'''
            return [KPluginInfo()]
    class IconWidget(QGraphicsWidget):
        """"""
        def __init__(self, parent = None):
            '''void Plasma.IconWidget.__init__(QGraphicsItem parent = None)'''
        def __init__(self, text, parent = None):
            '''void Plasma.IconWidget.__init__(QString text, QGraphicsItem parent = None)'''
        def __init__(self, icon, text, parent = None):
            '''void Plasma.IconWidget.__init__(QIcon icon, QString text, QGraphicsItem parent = None)'''
        def maximumIconSize(self):
            '''QSizeF Plasma.IconWidget.maximumIconSize()'''
            return QSizeF()
        def setMaximumIconSize(self, size):
            '''void Plasma.IconWidget.setMaximumIconSize(QSizeF size)'''
        def minimumIconSize(self):
            '''QSizeF Plasma.IconWidget.minimumIconSize()'''
            return QSizeF()
        def setMinimumIconSize(self, size):
            '''void Plasma.IconWidget.setMinimumIconSize(QSizeF size)'''
        def preferredIconSize(self):
            '''QSizeF Plasma.IconWidget.preferredIconSize()'''
            return QSizeF()
        def setPreferredIconSize(self, size):
            '''void Plasma.IconWidget.setPreferredIconSize(QSizeF size)'''
        def changeEvent(self, event):
            '''void Plasma.IconWidget.changeEvent(QEvent event)'''
        def sizeHint(self, which, constraint = QSizeF()):
            '''QSizeF Plasma.IconWidget.sizeHint(Qt.SizeHint which, QSizeF constraint = QSizeF())'''
            return QSizeF()
        def drawActionButtonBase(self, painter, size, element):
            '''void Plasma.IconWidget.drawActionButtonBase(QPainter painter, QSize size, int element)'''
        def sceneEventFilter(self, watched, event):
            '''bool Plasma.IconWidget.sceneEventFilter(QGraphicsItem watched, QEvent event)'''
            return bool()
        def hoverLeaveEvent(self, event):
            '''void Plasma.IconWidget.hoverLeaveEvent(QGraphicsSceneHoverEvent event)'''
        def hoverEnterEvent(self, event):
            '''void Plasma.IconWidget.hoverEnterEvent(QGraphicsSceneHoverEvent event)'''
        def mouseDoubleClickEvent(self, event):
            '''void Plasma.IconWidget.mouseDoubleClickEvent(QGraphicsSceneMouseEvent event)'''
        def mouseReleaseEvent(self, event):
            '''void Plasma.IconWidget.mouseReleaseEvent(QGraphicsSceneMouseEvent event)'''
        def mouseMoveEvent(self, event):
            '''void Plasma.IconWidget.mouseMoveEvent(QGraphicsSceneMouseEvent event)'''
        def mousePressEvent(self, event):
            '''void Plasma.IconWidget.mousePressEvent(QGraphicsSceneMouseEvent event)'''
        def isDown(self):
            '''bool Plasma.IconWidget.isDown()'''
            return bool()
        changed = pyqtSignal() # void changed() - signal
        activated = pyqtSignal() # void activated() - signal
        doubleClicked = pyqtSignal() # void doubleClicked() - signal
        clicked = pyqtSignal() # void clicked() - signal
        pressed = pyqtSignal() # void pressed(bool) - signal
        def paint(self, painter, option, widget = None):
            '''void Plasma.IconWidget.paint(QPainter painter, QStyleOptionGraphicsItem option, QWidget widget = None)'''
        def setUnpressed(self):
            '''void Plasma.IconWidget.setUnpressed()'''
        def setPressed(self, pressed = True):
            '''void Plasma.IconWidget.setPressed(bool pressed = True)'''
        def shape(self):
            '''QPainterPath Plasma.IconWidget.shape()'''
            return QPainterPath()
        def drawBackground(self):
            '''bool Plasma.IconWidget.drawBackground()'''
            return bool()
        def setDrawBackground(self, draw):
            '''void Plasma.IconWidget.setDrawBackground(bool draw)'''
        def setNumDisplayLines(self, numLines):
            '''void Plasma.IconWidget.setNumDisplayLines(int numLines)'''
        def numDisplayLines(self):
            '''int Plasma.IconWidget.numDisplayLines()'''
            return int()
        def sizeFromIconSize(self, iconWidth):
            '''QSizeF Plasma.IconWidget.sizeFromIconSize(float iconWidth)'''
            return QSizeF()
        def invertedLayout(self):
            '''bool Plasma.IconWidget.invertedLayout()'''
            return bool()
        def invertLayout(self, invert):
            '''void Plasma.IconWidget.invertLayout(bool invert)'''
        def orientation(self):
            '''Qt.Orientation Plasma.IconWidget.orientation()'''
            return Qt.Orientation()
        def setOrientation(self, orientation):
            '''void Plasma.IconWidget.setOrientation(Qt.Orientation orientation)'''
        def action(self):
            '''QAction Plasma.IconWidget.action()'''
            return QAction()
        def setAction(self, action):
            '''void Plasma.IconWidget.setAction(QAction action)'''
        def removeIconAction(self, action):
            '''void Plasma.IconWidget.removeIconAction(QAction action)'''
        def addIconAction(self, action):
            '''void Plasma.IconWidget.addIconAction(QAction action)'''
        def iconSize(self):
            '''QSizeF Plasma.IconWidget.iconSize()'''
            return QSizeF()
        def setTextBackgroundColor(self, color):
            '''void Plasma.IconWidget.setTextBackgroundColor(QColor color)'''
        def textBackgroundColor(self):
            '''QColor Plasma.IconWidget.textBackgroundColor()'''
            return QColor()
        def setIcon(self, icon):
            '''void Plasma.IconWidget.setIcon(QIcon icon)'''
        def setIcon(self, icon):
            '''void Plasma.IconWidget.setIcon(QString icon)'''
        def icon(self):
            '''QIcon Plasma.IconWidget.icon()'''
            return QIcon()
        def setInfoText(self, text):
            '''void Plasma.IconWidget.setInfoText(QString text)'''
        def infoText(self):
            '''QString Plasma.IconWidget.infoText()'''
            return QString()
        def svg(self):
            '''QString Plasma.IconWidget.svg()'''
            return QString()
        def setSvg(self, svgFilePath, svgIconElement = QString()):
            '''void Plasma.IconWidget.setSvg(QString svgFilePath, QString svgIconElement = QString())'''
        def setText(self, text):
            '''void Plasma.IconWidget.setText(QString text)'''
        def text(self):
            '''QString Plasma.IconWidget.text()'''
            return QString()
    class SvgWidget(QGraphicsWidget):
        """"""
        def __init__(self, parent = None, wFlags = 0):
            '''void Plasma.SvgWidget.__init__(QGraphicsItem parent = None, Qt.WindowFlags wFlags = 0)'''
        def __init__(self, svg, elementID = QString(), parent = None, wFlags = 0):
            '''void Plasma.SvgWidget.__init__(Plasma.Svg svg, QString elementID = QString(), QGraphicsItem parent = None, Qt.WindowFlags wFlags = 0)'''
        def mousePressEvent(self, event):
            '''void Plasma.SvgWidget.mousePressEvent(QGraphicsSceneMouseEvent event)'''
        def sizeHint(self, which, constraint):
            '''QSizeF Plasma.SvgWidget.sizeHint(Qt.SizeHint which, QSizeF constraint)'''
            return QSizeF()
        def paint(self, painter, option, widget):
            '''void Plasma.SvgWidget.paint(QPainter painter, QStyleOptionGraphicsItem option, QWidget widget)'''
        clicked = pyqtSignal() # void clicked(Qt::MouseButton) - signal
        def elementID(self):
            '''QString Plasma.SvgWidget.elementID()'''
            return QString()
        def setElementID(self, elementID):
            '''void Plasma.SvgWidget.setElementID(QString elementID)'''
        def svg(self):
            '''Plasma.Svg Plasma.SvgWidget.svg()'''
            return Plasma.Svg()
        def setSvg(self, svg):
            '''void Plasma.SvgWidget.setSvg(Plasma.Svg svg)'''
        def mouseReleaseEvent(self, event):
            '''void Plasma.SvgWidget.mouseReleaseEvent(QGraphicsSceneMouseEvent event)'''
    class Wallpaper(QObject):
        """"""
        # Enum Plasma.Wallpaper.ResizeMethod
        ScaledResize = 0
        CenteredResize = 0
        ScaledAndCroppedResize = 0
        TiledResize = 0
        CenterTiledResize = 0
        MaxpectResize = 0
        LastResizeMethod = 0
    
        def __init__(self, parent = None):
            '''void Plasma.Wallpaper.__init__(QObject parent = None)'''
        def __init__(self, parent, args):
            '''void Plasma.Wallpaper.__init__(QObject parent, list-of-QVariant args)'''
        def targetSizeHint(self):
            '''QSizeF Plasma.Wallpaper.targetSizeHint()'''
            return QSizeF()
        def resizeMethodHint(self):
            '''Plasma.Wallpaper.ResizeMethod Plasma.Wallpaper.resizeMethodHint()'''
            return Plasma.Wallpaper.ResizeMethod()
        def addUrls(self, urls):
            '''void Plasma.Wallpaper.addUrls(KUrl.List urls)'''
        def supportsMimetype(self, mimetype):
            '''bool Plasma.Wallpaper.supportsMimetype(QString mimetype)'''
            return bool()
        def setUrls(self, urls):
            '''void Plasma.Wallpaper.setUrls(KUrl.List urls)'''
        def setPreviewDuringConfiguration(self, preview):
            '''void Plasma.Wallpaper.setPreviewDuringConfiguration(bool preview)'''
        def needsPreviewDuringConfiguration(self):
            '''bool Plasma.Wallpaper.needsPreviewDuringConfiguration()'''
            return bool()
        def setPreviewing(self, previewing):
            '''void Plasma.Wallpaper.setPreviewing(bool previewing)'''
        def isPreviewing(self):
            '''bool Plasma.Wallpaper.isPreviewing()'''
            return bool()
        def setContextualActions(self, actions):
            '''void Plasma.Wallpaper.setContextualActions(list-of-QAction actions)'''
        urlDropped = pyqtSignal() # void urlDropped(const KUrlamp;) - signal
        def contextualActions(self):
            '''list-of-QAction Plasma.Wallpaper.contextualActions()'''
            return [QAction()]
        def package(self):
            '''Plasma.Package Plasma.Wallpaper.package()'''
            return Plasma.Package()
        def listWallpaperInfoForMimetype(self, mimetype, formFactor = QString()):
            '''static list-of-KPluginInfo Plasma.Wallpaper.listWallpaperInfoForMimetype(QString mimetype, QString formFactor = QString())'''
            return [KPluginInfo()]
        def insertIntoCache(self, key, image):
            '''void Plasma.Wallpaper.insertIntoCache(QString key, QImage image)'''
        def findInCache(self, key, image, lastModified = 0):
            '''bool Plasma.Wallpaper.findInCache(QString key, QImage image, int lastModified = 0)'''
            return bool()
        def setUsingRenderingCache(self, useCache):
            '''void Plasma.Wallpaper.setUsingRenderingCache(bool useCache)'''
        def render(self, sourceImagePath, size, resizeMethod = None, color = None):
            '''void Plasma.Wallpaper.render(QString sourceImagePath, QSize size, Plasma.Wallpaper.ResizeMethod resizeMethod = Plasma.Wallpaper.ScaledResize, QColor color = QColor(0,0,0))'''
        def render(self, image, size, resizeMethod = None, color = None):
            '''void Plasma.Wallpaper.render(QImage image, QSize size, Plasma.Wallpaper.ResizeMethod resizeMethod = Plasma.Wallpaper.ScaledResize, QColor color = QColor(0,0,0))'''
        def setConfigurationRequired(self, needsConfiguring, reason = QString()):
            '''void Plasma.Wallpaper.setConfigurationRequired(bool needsConfiguring, QString reason = QString())'''
        def init(self, config):
            '''void Plasma.Wallpaper.init(KConfigGroup config)'''
        renderHintsChanged = pyqtSignal() # void renderHintsChanged() - signal
        renderCompleted = pyqtSignal() # void renderCompleted(const QImageamp;) - signal
        configNeedsSaving = pyqtSignal() # void configNeedsSaving() - signal
        configureRequested = pyqtSignal() # void configureRequested() - signal
        update = pyqtSignal() # void update(const QRectFamp;) - signal
        def setTargetSizeHint(self, targetSize):
            '''void Plasma.Wallpaper.setTargetSizeHint(QSizeF targetSize)'''
        def setResizeMethodHint(self, resizeMethod):
            '''void Plasma.Wallpaper.setResizeMethodHint(Plasma.Wallpaper.ResizeMethod resizeMethod)'''
        def isUsingRenderingCache(self):
            '''bool Plasma.Wallpaper.isUsingRenderingCache()'''
            return bool()
        def configurationRequired(self):
            '''bool Plasma.Wallpaper.configurationRequired()'''
            return bool()
        configurationRequired = pyqtSignal() # void configurationRequired(bool) - signal
        def dataEngine(self, name):
            '''Plasma.DataEngine Plasma.Wallpaper.dataEngine(QString name)'''
            return Plasma.DataEngine()
        def wheelEvent(self, event):
            '''void Plasma.Wallpaper.wheelEvent(QGraphicsSceneWheelEvent event)'''
        def mouseReleaseEvent(self, event):
            '''void Plasma.Wallpaper.mouseReleaseEvent(QGraphicsSceneMouseEvent event)'''
        def mousePressEvent(self, event):
            '''void Plasma.Wallpaper.mousePressEvent(QGraphicsSceneMouseEvent event)'''
        def mouseMoveEvent(self, event):
            '''void Plasma.Wallpaper.mouseMoveEvent(QGraphicsSceneMouseEvent event)'''
        def createConfigurationInterface(self, parent):
            '''QWidget Plasma.Wallpaper.createConfigurationInterface(QWidget parent)'''
            return QWidget()
        def save(self, config):
            '''void Plasma.Wallpaper.save(KConfigGroup config)'''
        def restore(self, config):
            '''void Plasma.Wallpaper.restore(KConfigGroup config)'''
        def paint(self, painter, exposedRect):
            '''abstract void Plasma.Wallpaper.paint(QPainter painter, QRectF exposedRect)'''
        def setBoundingRect(self, boundingRect):
            '''void Plasma.Wallpaper.setBoundingRect(QRectF boundingRect)'''
        def boundingRect(self):
            '''QRectF Plasma.Wallpaper.boundingRect()'''
            return QRectF()
        def isInitialized(self):
            '''bool Plasma.Wallpaper.isInitialized()'''
            return bool()
        def listRenderingModes(self):
            '''list-of-KServiceAction Plasma.Wallpaper.listRenderingModes()'''
            return [KServiceAction()]
        def setRenderingMode(self, mode):
            '''void Plasma.Wallpaper.setRenderingMode(QString mode)'''
        def renderingMode(self):
            '''KServiceAction Plasma.Wallpaper.renderingMode()'''
            return KServiceAction()
        def icon(self):
            '''QString Plasma.Wallpaper.icon()'''
            return QString()
        def pluginName(self):
            '''QString Plasma.Wallpaper.pluginName()'''
            return QString()
        def name(self):
            '''QString Plasma.Wallpaper.name()'''
            return QString()
        def packageStructure(self, paper = None):
            '''static unknown-type Plasma.Wallpaper.packageStructure(Plasma.Wallpaper paper = None)'''
            return unknown-type()
        def load(self, name, args = QVariantList()):
            '''static Plasma.Wallpaper Plasma.Wallpaper.load(QString name, list-of-QVariant args = QVariantList())'''
            return Plasma.Wallpaper()
        def load(self, info, args = QVariantList()):
            '''static Plasma.Wallpaper Plasma.Wallpaper.load(KPluginInfo info, list-of-QVariant args = QVariantList())'''
            return Plasma.Wallpaper()
        def listWallpaperInfo(self, formFactor = QString()):
            '''static list-of-KPluginInfo Plasma.Wallpaper.listWallpaperInfo(QString formFactor = QString())'''
            return [KPluginInfo()]
    class Package():
        """"""
        def __init__(self, packageRoot, package, structure):
            '''void Plasma.Package.__init__(QString packageRoot, QString package, unknown-type structure)'''
        def __init__(self, packagePath, structure):
            '''void Plasma.Package.__init__(QString packagePath, unknown-type structure)'''
        def __init__(self):
            '''void Plasma.Package.__init__()'''
        def contentsHash(self):
            '''QString Plasma.Package.contentsHash()'''
            return QString()
        def createPackage(self, metadata, source, destination, icon = QString()):
            '''static bool Plasma.Package.createPackage(Plasma.PackageMetadata metadata, QString source, QString destination, QString icon = QString())'''
            return bool()
        def registerPackage(self, data, iconPath):
            '''static bool Plasma.Package.registerPackage(Plasma.PackageMetadata data, QString iconPath)'''
            return bool()
        def uninstallPackage(self, package, packageRoot, servicePrefix):
            '''static bool Plasma.Package.uninstallPackage(QString package, QString packageRoot, QString servicePrefix)'''
            return bool()
        def installPackage(self, package, packageRoot, servicePrefix):
            '''static bool Plasma.Package.installPackage(QString package, QString packageRoot, QString servicePrefix)'''
            return bool()
        def listInstalledPaths(self, packageRoot):
            '''static QStringList Plasma.Package.listInstalledPaths(QString packageRoot)'''
            return QStringList()
        def listInstalled(self, packageRoot):
            '''static QStringList Plasma.Package.listInstalled(QString packageRoot)'''
            return QStringList()
        def structure(self):
            '''unknown-type Plasma.Package.structure()'''
            return unknown-type()
        def path(self):
            '''QString Plasma.Package.path()'''
            return QString()
        def setPath(self, path):
            '''void Plasma.Package.setPath(QString path)'''
        def metadata(self):
            '''Plasma.PackageMetadata Plasma.Package.metadata()'''
            return Plasma.PackageMetadata()
        def entryList(self, fileType):
            '''QStringList Plasma.Package.entryList(str fileType)'''
            return QStringList()
        def filePath(self, fileType, filename):
            '''QString Plasma.Package.filePath(str fileType, QString filename)'''
            return QString()
        def filePath(self, fileType):
            '''QString Plasma.Package.filePath(str fileType)'''
            return QString()
        def isValid(self):
            '''bool Plasma.Package.isValid()'''
            return bool()
    class RunnerManager(QObject):
        """"""
        def __init__(self, parent = None):
            '''void Plasma.RunnerManager.__init__(QObject parent = None)'''
        def __init__(self, config, parent = None):
            '''void Plasma.RunnerManager.__init__(KConfigGroup config, QObject parent = None)'''
        def listRunnerInfo(self, parentApp = QString()):
            '''static list-of-KPluginInfo Plasma.RunnerManager.listRunnerInfo(QString parentApp = QString())'''
            return [KPluginInfo()]
        queryFinished = pyqtSignal() # void queryFinished() - signal
        def mimeDataForMatch(self, match):
            '''QMimeData Plasma.RunnerManager.mimeDataForMatch(Plasma.QueryMatch match)'''
            return QMimeData()
        def mimeDataForMatch(self, id):
            '''QMimeData Plasma.RunnerManager.mimeDataForMatch(QString id)'''
            return QMimeData()
        def loadRunner(self, service):
            '''void Plasma.RunnerManager.loadRunner(unknown-type service)'''
        def loadRunner(self, path):
            '''void Plasma.RunnerManager.loadRunner(QString path)'''
        def singleModeAdvertisedRunnerIds(self):
            '''QStringList Plasma.RunnerManager.singleModeAdvertisedRunnerIds()'''
            return QStringList()
        def runnerName(self, id):
            '''QString Plasma.RunnerManager.runnerName(QString id)'''
            return QString()
        def setSingleMode(self, singleMode):
            '''void Plasma.RunnerManager.setSingleMode(bool singleMode)'''
        def singleMode(self):
            '''bool Plasma.RunnerManager.singleMode()'''
            return bool()
        def singleModeRunnerId(self):
            '''QString Plasma.RunnerManager.singleModeRunnerId()'''
            return QString()
        def setSingleModeRunnerId(self, id):
            '''void Plasma.RunnerManager.setSingleModeRunnerId(QString id)'''
        def singleModeRunner(self):
            '''Plasma.AbstractRunner Plasma.RunnerManager.singleModeRunner()'''
            return Plasma.AbstractRunner()
        def matchSessionComplete(self):
            '''void Plasma.RunnerManager.matchSessionComplete()'''
        def setupMatchSession(self):
            '''void Plasma.RunnerManager.setupMatchSession()'''
        def allowedRunners(self):
            '''QStringList Plasma.RunnerManager.allowedRunners()'''
            return QStringList()
        def setAllowedRunners(self, runners):
            '''void Plasma.RunnerManager.setAllowedRunners(QStringList runners)'''
        matchesChanged = pyqtSignal() # void matchesChanged(const QListlt;Plasma::QueryMatchgt;amp;) - signal
        def reset(self):
            '''void Plasma.RunnerManager.reset()'''
        def execQuery(self, term, runnerName):
            '''bool Plasma.RunnerManager.execQuery(QString term, QString runnerName)'''
            return bool()
        def execQuery(self, term):
            '''bool Plasma.RunnerManager.execQuery(QString term)'''
            return bool()
        def launchQuery(self, term, runnerId):
            '''void Plasma.RunnerManager.launchQuery(QString term, QString runnerId)'''
        def launchQuery(self, term):
            '''void Plasma.RunnerManager.launchQuery(QString term)'''
        def reloadConfiguration(self):
            '''void Plasma.RunnerManager.reloadConfiguration()'''
        def query(self):
            '''QString Plasma.RunnerManager.query()'''
            return QString()
        def actionsForMatch(self, match):
            '''list-of-QAction Plasma.RunnerManager.actionsForMatch(Plasma.QueryMatch match)'''
            return [QAction()]
        def run(self, match):
            '''void Plasma.RunnerManager.run(Plasma.QueryMatch match)'''
        def run(self, id):
            '''void Plasma.RunnerManager.run(QString id)'''
        def matches(self):
            '''list-of-Plasma.QueryMatch Plasma.RunnerManager.matches()'''
            return [Plasma.QueryMatch()]
        def searchContext(self):
            '''Plasma.RunnerContext Plasma.RunnerManager.searchContext()'''
            return Plasma.RunnerContext()
        def runners(self):
            '''list-of-Plasma.AbstractRunner Plasma.RunnerManager.runners()'''
            return [Plasma.AbstractRunner()]
        def runner(self, name):
            '''Plasma.AbstractRunner Plasma.RunnerManager.runner(QString name)'''
            return Plasma.AbstractRunner()
    class GLApplet(Plasma.Applet):
        """"""
        def __init__(self, parent, serviceId, appletId):
            '''void Plasma.GLApplet.__init__(QGraphicsItem parent, QString serviceId, int appletId)'''
        def __init__(self, parent, args):
            '''void Plasma.GLApplet.__init__(QObject parent, list-of-QVariant args)'''
        def deleteTexture(self, texture_id):
            '''void Plasma.GLApplet.deleteTexture(int texture_id)'''
        def bindTexture(self, image, target = None):
            '''int Plasma.GLApplet.bindTexture(QImage image, int target = GL_TEXTURE_2D)'''
            return int()
        def makeCurrent(self):
            '''void Plasma.GLApplet.makeCurrent()'''
        def paintGLInterface(self, painter, option):
            '''void Plasma.GLApplet.paintGLInterface(QPainter painter, QStyleOptionGraphicsItem option)'''
    class Applet(QGraphicsWidget):
        """"""
        Type = None # int - member
        # Enum Plasma.Applet.BackgroundHint
        NoBackground = 0
        StandardBackground = 0
        TranslucentBackground = 0
        DefaultBackground = 0
    
        def __init__(self, parent = None, serviceId = QString(), appletId = 0):
            '''void Plasma.Applet.__init__(QGraphicsItem parent = None, QString serviceId = QString(), int appletId = 0)'''
        def __init__(self, parent, serviceId, appletId, args):
            '''void Plasma.Applet.__init__(QGraphicsItem parent, QString serviceId, int appletId, list-of-QVariant args)'''
        def __init__(self, parent, args):
            '''void Plasma.Applet.__init__(QObject parent, list-of-QVariant args)'''
        def __init__(self, info, parent = None, appletId = 0):
            '''void Plasma.Applet.__init__(KPluginInfo info, QGraphicsItem parent = None, int appletId = 0)'''
        def isUserConfiguring(self):
            '''bool Plasma.Applet.isUserConfiguring()'''
            return bool()
        def runAssociatedApplication(self):
            '''void Plasma.Applet.runAssociatedApplication()'''
        def isPublished(self):
            '''bool Plasma.Applet.isPublished()'''
            return bool()
        def unpublish(self):
            '''void Plasma.Applet.unpublish()'''
        def setStatus(self, stat):
            '''void Plasma.Applet.setStatus(Plasma.ItemStatus stat)'''
        def status(self):
            '''Plasma.ItemStatus Plasma.Applet.status()'''
            return Plasma.ItemStatus()
        immutabilityChanged = pyqtSignal() # void immutabilityChanged(Plasma::ImmutabilityType) - signal
        newStatus = pyqtSignal() # void newStatus(Plasma::ItemStatus) - signal
        def hasValidAssociatedApplication(self):
            '''bool Plasma.Applet.hasValidAssociatedApplication()'''
            return bool()
        def associatedApplicationUrls(self):
            '''KUrl.List Plasma.Applet.associatedApplicationUrls()'''
            return KUrl.List()
        def associatedApplication(self):
            '''QString Plasma.Applet.associatedApplication()'''
            return QString()
        def setAssociatedApplicationUrls(self, urls):
            '''void Plasma.Applet.setAssociatedApplicationUrls(KUrl.List urls)'''
        def setAssociatedApplication(self, string):
            '''void Plasma.Applet.setAssociatedApplication(QString string)'''
        def listAppletInfoForUrl(self, url):
            '''static list-of-KPluginInfo Plasma.Applet.listAppletInfoForUrl(QUrl url)'''
            return [KPluginInfo()]
        def itemChange(self, change, value):
            '''QVariant Plasma.Applet.itemChange(QGraphicsItem.GraphicsItemChange change, QVariant value)'''
            return QVariant()
        extenderItemRestored = pyqtSignal() # void extenderItemRestored(Plasma::ExtenderItem *) - signal
        def hasAuthorization(self, constraint):
            '''bool Plasma.Applet.hasAuthorization(QString constraint)'''
            return bool()
        def timerEvent(self, event):
            '''void Plasma.Applet.timerEvent(QTimerEvent event)'''
        def hoverLeaveEvent(self, event):
            '''void Plasma.Applet.hoverLeaveEvent(QGraphicsSceneHoverEvent event)'''
        def hoverEnterEvent(self, event):
            '''void Plasma.Applet.hoverEnterEvent(QGraphicsSceneHoverEvent event)'''
        def sizeHint(self, which, constraint = QSizeF()):
            '''QSizeF Plasma.Applet.sizeHint(Qt.SizeHint which, QSizeF constraint = QSizeF())'''
            return QSizeF()
        def shape(self):
            '''QPainterPath Plasma.Applet.shape()'''
            return QPainterPath()
        def resizeEvent(self, event):
            '''void Plasma.Applet.resizeEvent(QGraphicsSceneResizeEvent event)'''
        def focusInEvent(self, event):
            '''void Plasma.Applet.focusInEvent(QFocusEvent event)'''
        def mouseMoveEvent(self, event):
            '''void Plasma.Applet.mouseMoveEvent(QGraphicsSceneMouseEvent event)'''
        def sceneEventFilter(self, watched, event):
            '''bool Plasma.Applet.sceneEventFilter(QGraphicsItem watched, QEvent event)'''
            return bool()
        def eventFilter(self, o, e):
            '''bool Plasma.Applet.eventFilter(QObject o, QEvent e)'''
            return bool()
        def extender(self):
            '''Plasma.Extender Plasma.Applet.extender()'''
            return Plasma.Extender()
        def isRegisteredAsDragHandle(self, item):
            '''bool Plasma.Applet.isRegisteredAsDragHandle(QGraphicsItem item)'''
            return bool()
        def unregisterAsDragHandle(self, item):
            '''void Plasma.Applet.unregisterAsDragHandle(QGraphicsItem item)'''
        def registerAsDragHandle(self, item):
            '''void Plasma.Applet.registerAsDragHandle(QGraphicsItem item)'''
        def constraintsEvent(self, constraints):
            '''void Plasma.Applet.constraintsEvent(Plasma.Constraints constraints)'''
        def showMessage(self, icon, message, buttons):
            '''void Plasma.Applet.showMessage(QIcon icon, QString message, Plasma.MessageButtons buttons)'''
        def setConfigurationRequired(self, needsConfiguring, reason = QString()):
            '''void Plasma.Applet.setConfigurationRequired(bool needsConfiguring, QString reason = QString())'''
        def setHasConfigurationInterface(self, hasInterface):
            '''void Plasma.Applet.setHasConfigurationInterface(bool hasInterface)'''
        def saveState(self, config):
            '''void Plasma.Applet.saveState(KConfigGroup config)'''
        def setFailedToLaunch(self, failed, reason = QString()):
            '''void Plasma.Applet.setFailedToLaunch(bool failed, QString reason = QString())'''
        def startupArguments(self):
            '''list-of-QVariant Plasma.Applet.startupArguments()'''
            return [QVariant()]
        def setBusy(self, busy):
            '''void Plasma.Applet.setBusy(bool busy)'''
        def configChanged(self):
            '''void Plasma.Applet.configChanged()'''
        def init(self):
            '''void Plasma.Applet.init()'''
        def flushPendingConstraintsEvents(self):
            '''void Plasma.Applet.flushPendingConstraintsEvents()'''
        def lower(self):
            '''void Plasma.Applet.lower()'''
        def raise_(self):
            '''void Plasma.Applet.raise_()'''
        def showConfigurationInterface(self):
            '''void Plasma.Applet.showConfigurationInterface()'''
        def showConfigurationInterface(self, widget):
            '''void Plasma.Applet.showConfigurationInterface(QWidget widget)'''
        def destroy(self):
            '''void Plasma.Applet.destroy()'''
        def setImmutability(self, immutable):
            '''void Plasma.Applet.setImmutability(Plasma.ImmutabilityType immutable)'''
        appletDestroyed = pyqtSignal() # void appletDestroyed(Plasma::Applet *) - signal
        messageButtonPressed = pyqtSignal() # void messageButtonPressed(const Plasma::MessageButton) - signal
        activate = pyqtSignal() # void activate() - signal
        configNeedsSaving = pyqtSignal() # void configNeedsSaving() - signal
        sizeHintChanged = pyqtSignal() # void sizeHintChanged(Qt::SizeHint) - signal
        appletTransformedItself = pyqtSignal() # void appletTransformedItself() - signal
        appletTransformedByUser = pyqtSignal() # void appletTransformedByUser() - signal
        geometryChanged = pyqtSignal() # void geometryChanged() - signal
        releaseVisualFocus = pyqtSignal() # void releaseVisualFocus() - signal
        def createConfigurationInterface(self, parent):
            '''void Plasma.Applet.createConfigurationInterface(KConfigDialog parent)'''
        def destroyed(self):
            '''bool Plasma.Applet.destroyed()'''
            return bool()
        def initExtenderItem(self, item):
            '''void Plasma.Applet.initExtenderItem(Plasma.ExtenderItem item)'''
        def removeAssociatedWidget(self, widget):
            '''void Plasma.Applet.removeAssociatedWidget(QWidget widget)'''
        def addAssociatedWidget(self, widget):
            '''void Plasma.Applet.addAssociatedWidget(QWidget widget)'''
        def isPopupShowing(self):
            '''bool Plasma.Applet.isPopupShowing()'''
            return bool()
        def globalShortcut(self):
            '''KShortcut Plasma.Applet.globalShortcut()'''
            return KShortcut()
        def setGlobalShortcut(self, shortcut):
            '''void Plasma.Applet.setGlobalShortcut(KShortcut shortcut)'''
        def containment(self):
            '''Plasma.Containment Plasma.Applet.containment()'''
            return Plasma.Containment()
        def type(self):
            '''int Plasma.Applet.type()'''
            return int()
        def screenRect(self):
            '''QRect Plasma.Applet.screenRect()'''
            return QRect()
        def isContainment(self):
            '''bool Plasma.Applet.isContainment()'''
            return bool()
        def backgroundHints(self):
            '''Plasma.Applet.BackgroundHints Plasma.Applet.backgroundHints()'''
            return Plasma.Applet.BackgroundHints()
        def setBackgroundHints(self, hints):
            '''void Plasma.Applet.setBackgroundHints(Plasma.Applet.BackgroundHints hints)'''
        def addAction(self, name, action):
            '''void Plasma.Applet.addAction(QString name, QAction action)'''
        def action(self, name):
            '''QAction Plasma.Applet.action(QString name)'''
            return QAction()
        def contextualActions(self):
            '''list-of-QAction Plasma.Applet.contextualActions()'''
            return [QAction()]
        def hasConfigurationInterface(self):
            '''bool Plasma.Applet.hasConfigurationInterface()'''
            return bool()
        def configurationRequired(self):
            '''bool Plasma.Applet.configurationRequired()'''
            return bool()
        def isBusy(self):
            '''bool Plasma.Applet.isBusy()'''
            return bool()
        def hasFailedToLaunch(self):
            '''bool Plasma.Applet.hasFailedToLaunch()'''
            return bool()
        def paintWindowFrame(self, painter, option, widget):
            '''void Plasma.Applet.paintWindowFrame(QPainter painter, QStyleOptionGraphicsItem option, QWidget widget)'''
        def immutability(self):
            '''Plasma.ImmutabilityType Plasma.Applet.immutability()'''
            return Plasma.ImmutabilityType()
        def icon(self):
            '''QString Plasma.Applet.icon()'''
            return QString()
        def shouldConserveResources(self):
            '''bool Plasma.Applet.shouldConserveResources()'''
            return bool()
        def pluginName(self):
            '''QString Plasma.Applet.pluginName()'''
            return QString()
        def font(self):
            '''QFont Plasma.Applet.font()'''
            return QFont()
        def name(self):
            '''QString Plasma.Applet.name()'''
            return QString()
        def paintInterface(self, painter, option, contentsRect):
            '''void Plasma.Applet.paintInterface(QPainter painter, QStyleOptionGraphicsItem option, QRect contentsRect)'''
        def category(self, applet):
            '''static QString Plasma.Applet.category(KPluginInfo applet)'''
            return QString()
        def category(self, appletName):
            '''static QString Plasma.Applet.category(QString appletName)'''
            return QString()
        def category(self):
            '''QString Plasma.Applet.category()'''
            return QString()
        def load(self, name, appletId = 0, args = QVariantList()):
            '''static Plasma.Applet Plasma.Applet.load(QString name, int appletId = 0, list-of-QVariant args = QVariantList())'''
            return Plasma.Applet()
        def load(self, info, appletId = 0, args = QVariantList()):
            '''static Plasma.Applet Plasma.Applet.load(KPluginInfo info, int appletId = 0, list-of-QVariant args = QVariantList())'''
            return Plasma.Applet()
        def loadPlasmoid(self, path, appletId = 0, args = QVariantList()):
            '''static Plasma.Applet Plasma.Applet.loadPlasmoid(QString path, int appletId = 0, list-of-QVariant args = QVariantList())'''
            return Plasma.Applet()
        def customCategories(self):
            '''QStringList Plasma.Applet.customCategories()'''
            return QStringList()
        def setCustomCategories(self, categories):
            '''void Plasma.Applet.setCustomCategories(QStringList categories)'''
        def listCategories(self, parentApp = QString(), visibleOnly = True):
            '''static QStringList Plasma.Applet.listCategories(QString parentApp = QString(), bool visibleOnly = True)'''
            return QStringList()
        def listAppletInfoForMimetype(self, mimetype):
            '''static list-of-KPluginInfo Plasma.Applet.listAppletInfoForMimetype(QString mimetype)'''
            return [KPluginInfo()]
        def listAppletInfo(self, category = QString(), parentApp = QString()):
            '''static list-of-KPluginInfo Plasma.Applet.listAppletInfo(QString category = QString(), QString parentApp = QString())'''
            return [KPluginInfo()]
        def setAspectRatioMode(self):
            '''Plasma.AspectRatioMode Plasma.Applet.setAspectRatioMode()'''
            return Plasma.AspectRatioMode()
        def aspectRatioMode(self):
            '''Plasma.AspectRatioMode Plasma.Applet.aspectRatioMode()'''
            return Plasma.AspectRatioMode()
        def context(self):
            '''Plasma.Context Plasma.Applet.context()'''
            return Plasma.Context()
        def location(self):
            '''Plasma.Location Plasma.Applet.location()'''
            return Plasma.Location()
        def formFactor(self):
            '''Plasma.FormFactor Plasma.Applet.formFactor()'''
            return Plasma.FormFactor()
        def updateConstraints(self, constraints = None):
            '''void Plasma.Applet.updateConstraints(Plasma.Constraints constraints = Plasma.AllConstraints)'''
        def popupPosition(self, s):
            '''QPoint Plasma.Applet.popupPosition(QSize s)'''
            return QPoint()
        def popupPosition(self, s, alignment):
            '''QPoint Plasma.Applet.popupPosition(QSize s, Qt.AlignmentFlag alignment)'''
            return QPoint()
        def mapToView(self, view, rect):
            '''QRect Plasma.Applet.mapToView(QGraphicsView view, QRectF rect)'''
            return QRect()
        def mapFromView(self, view, rect):
            '''QRectF Plasma.Applet.mapFromView(QGraphicsView view, QRect rect)'''
            return QRectF()
        def view(self):
            '''QGraphicsView Plasma.Applet.view()'''
            return QGraphicsView()
        def package(self):
            '''Plasma.Package Plasma.Applet.package()'''
            return Plasma.Package()
        def dataEngine(self, name):
            '''Plasma.DataEngine Plasma.Applet.dataEngine(QString name)'''
            return Plasma.DataEngine()
        def configScheme(self):
            '''Plasma.ConfigLoader Plasma.Applet.configScheme()'''
            return Plasma.ConfigLoader()
        def globalConfig(self):
            '''KConfigGroup Plasma.Applet.globalConfig()'''
            return KConfigGroup()
        def restore(self, group):
            '''void Plasma.Applet.restore(KConfigGroup group)'''
        def save(self, group):
            '''void Plasma.Applet.save(KConfigGroup group)'''
        def config(self):
            '''KConfigGroup Plasma.Applet.config()'''
            return KConfigGroup()
        def config(self, group):
            '''KConfigGroup Plasma.Applet.config(QString group)'''
            return KConfigGroup()
        def id(self):
            '''int Plasma.Applet.id()'''
            return int()
        def packageStructure(self):
            '''static unknown-type Plasma.Applet.packageStructure()'''
            return unknown-type()
    class Dialog(QWidget):
        """"""
        # Enum Plasma.Dialog.ResizeCorner
        NoCorner = 0
        NorthEast = 0
        SouthEast = 0
        NorthWest = 0
        SouthWest = 0
        All = 0
    
        def __init__(self, parent = None, f = None):
            '''void Plasma.Dialog.__init__(QWidget parent = None, Qt.WindowFlags f = Qt.Window)'''
        def getMinimumResizeLimits(self, left, top, right, bottom):
            '''void Plasma.Dialog.getMinimumResizeLimits(int left, int top, int right, int bottom)'''
        def setMinimumResizeLimits(self, left, top, right, bottom):
            '''void Plasma.Dialog.setMinimumResizeLimits(int left, int top, int right, int bottom)'''
        def isUserResizing(self):
            '''bool Plasma.Dialog.isUserResizing()'''
            return bool()
        def syncToGraphicsWidget(self):
            '''void Plasma.Dialog.syncToGraphicsWidget()'''
        def setAspectRatioMode(self, mode):
            '''void Plasma.Dialog.setAspectRatioMode(Plasma.AspectRatioMode mode)'''
        def aspectRatioMode(self):
            '''Plasma.AspectRatioMode Plasma.Dialog.aspectRatioMode()'''
            return Plasma.AspectRatioMode()
        def focusInEvent(self, event):
            '''void Plasma.Dialog.focusInEvent(QFocusEvent event)'''
        def inControlArea(self, point):
            '''bool Plasma.Dialog.inControlArea(QPoint point)'''
            return bool()
        def moveEvent(self, event):
            '''void Plasma.Dialog.moveEvent(QMoveEvent event)'''
        def keyPressEvent(self, event):
            '''void Plasma.Dialog.keyPressEvent(QKeyEvent event)'''
        def mouseReleaseEvent(self, event):
            '''void Plasma.Dialog.mouseReleaseEvent(QMouseEvent event)'''
        def mousePressEvent(self, event):
            '''void Plasma.Dialog.mousePressEvent(QMouseEvent event)'''
        def mouseMoveEvent(self, event):
            '''void Plasma.Dialog.mouseMoveEvent(QMouseEvent event)'''
        def showEvent(self, event):
            '''void Plasma.Dialog.showEvent(QShowEvent event)'''
        def hideEvent(self, event):
            '''void Plasma.Dialog.hideEvent(QHideEvent event)'''
        def eventFilter(self, watched, event):
            '''bool Plasma.Dialog.eventFilter(QObject watched, QEvent event)'''
            return bool()
        def resizeEvent(self, e):
            '''void Plasma.Dialog.resizeEvent(QResizeEvent e)'''
        def event(self, event):
            '''bool Plasma.Dialog.event(QEvent event)'''
            return bool()
        def paintEvent(self, e):
            '''void Plasma.Dialog.paintEvent(QPaintEvent e)'''
        dialogVisible = pyqtSignal() # void dialogVisible(bool) - signal
        dialogResized = pyqtSignal() # void dialogResized() - signal
        def animatedShow(self, direction):
            '''void Plasma.Dialog.animatedShow(Plasma.Direction direction)'''
        def animatedHide(self, direction):
            '''void Plasma.Dialog.animatedHide(Plasma.Direction direction)'''
        def resizeCorners(self):
            '''Plasma.Dialog.ResizeCorners Plasma.Dialog.resizeCorners()'''
            return Plasma.Dialog.ResizeCorners()
        def setResizeHandleCorners(self, corners):
            '''void Plasma.Dialog.setResizeHandleCorners(Plasma.Dialog.ResizeCorners corners)'''
        def graphicsWidget(self):
            '''QGraphicsWidget Plasma.Dialog.graphicsWidget()'''
            return QGraphicsWidget()
        def setGraphicsWidget(self, widget):
            '''void Plasma.Dialog.setGraphicsWidget(QGraphicsWidget widget)'''
    class SignalPlotter(QGraphicsWidget):
        """"""
        def __init__(self, parent = None):
            '''void Plasma.SignalPlotter.__init__(QGraphicsItem parent = None)'''
        def thinFrame(self):
            '''bool Plasma.SignalPlotter.thinFrame()'''
            return bool()
        def drawHorizontalLines(self, p, top, w, h):
            '''void Plasma.SignalPlotter.drawHorizontalLines(QPainter p, int top, int w, int h)'''
        def drawAxisText(self, p, top, h):
            '''void Plasma.SignalPlotter.drawAxisText(QPainter p, int top, int h)'''
        def drawPlots(self, p, top, w, h, horizontalScale):
            '''void Plasma.SignalPlotter.drawPlots(QPainter p, int top, int w, int h, int horizontalScale)'''
        def drawVerticalLines(self, p, top, w, h):
            '''void Plasma.SignalPlotter.drawVerticalLines(QPainter p, int top, int w, int h)'''
        def drawTopBarContents(self, p, x, width, height):
            '''void Plasma.SignalPlotter.drawTopBarContents(QPainter p, int x, int width, int height)'''
        def drawTopBarFrame(self, p, separatorX, height):
            '''void Plasma.SignalPlotter.drawTopBarFrame(QPainter p, int separatorX, int height)'''
        def drawThinFrame(self, p, w, h):
            '''void Plasma.SignalPlotter.drawThinFrame(QPainter p, int w, int h)'''
        def drawBackground(self, p, w, h):
            '''void Plasma.SignalPlotter.drawBackground(QPainter p, int w, int h)'''
        def drawWidget(self, p, w, height, horizontalScale):
            '''void Plasma.SignalPlotter.drawWidget(QPainter p, int w, int height, int horizontalScale)'''
        def paint(self, painter, option, widget):
            '''void Plasma.SignalPlotter.paint(QPainter painter, QStyleOptionGraphicsItem option, QWidget widget)'''
        def calculateNiceRange(self):
            '''void Plasma.SignalPlotter.calculateNiceRange()'''
        def updateDataBuffers(self):
            '''void Plasma.SignalPlotter.updateDataBuffers()'''
        def setGeometry(self, geometry):
            '''void Plasma.SignalPlotter.setGeometry(QRectF geometry)'''
        def getSnapshotImage(self, width, height):
            '''QPixmap Plasma.SignalPlotter.getSnapshotImage(int width, int height)'''
            return QPixmap()
        def stackPlots(self):
            '''bool Plasma.SignalPlotter.stackPlots()'''
            return bool()
        def setStackPlots(self, stack):
            '''void Plasma.SignalPlotter.setStackPlots(bool stack)'''
        def setThinFrame(self, set):
            '''void Plasma.SignalPlotter.setThinFrame(bool set)'''
        def lastValueAsString(self, i):
            '''QString Plasma.SignalPlotter.lastValueAsString(int i)'''
            return QString()
        def lastValue(self, i):
            '''float Plasma.SignalPlotter.lastValue(int i)'''
            return float()
        def svgBackground(self):
            '''QString Plasma.SignalPlotter.svgBackground()'''
            return QString()
        def setSvgBackground(self, filename):
            '''void Plasma.SignalPlotter.setSvgBackground(QString filename)'''
        def backgroundColor(self):
            '''QColor Plasma.SignalPlotter.backgroundColor()'''
            return QColor()
        def setBackgroundColor(self, color):
            '''void Plasma.SignalPlotter.setBackgroundColor(QColor color)'''
        def showTopBar(self):
            '''bool Plasma.SignalPlotter.showTopBar()'''
            return bool()
        def setShowTopBar(self, value):
            '''void Plasma.SignalPlotter.setShowTopBar(bool value)'''
        def showLabels(self):
            '''bool Plasma.SignalPlotter.showLabels()'''
            return bool()
        def setShowLabels(self, value):
            '''void Plasma.SignalPlotter.setShowLabels(bool value)'''
        def horizontalLinesCount(self):
            '''int Plasma.SignalPlotter.horizontalLinesCount()'''
            return int()
        def setHorizontalLinesCount(self, count):
            '''void Plasma.SignalPlotter.setHorizontalLinesCount(int count)'''
        def font(self):
            '''QFont Plasma.SignalPlotter.font()'''
            return QFont()
        def setFont(self, font):
            '''void Plasma.SignalPlotter.setFont(QFont font)'''
        def fontColor(self):
            '''QColor Plasma.SignalPlotter.fontColor()'''
            return QColor()
        def setFontColor(self, color):
            '''void Plasma.SignalPlotter.setFontColor(QColor color)'''
        def horizontalLinesColor(self):
            '''QColor Plasma.SignalPlotter.horizontalLinesColor()'''
            return QColor()
        def setHorizontalLinesColor(self, color):
            '''void Plasma.SignalPlotter.setHorizontalLinesColor(QColor color)'''
        def showHorizontalLines(self):
            '''bool Plasma.SignalPlotter.showHorizontalLines()'''
            return bool()
        def setShowHorizontalLines(self, value):
            '''void Plasma.SignalPlotter.setShowHorizontalLines(bool value)'''
        def verticalLinesScroll(self):
            '''bool Plasma.SignalPlotter.verticalLinesScroll()'''
            return bool()
        def setVerticalLinesScroll(self, value):
            '''void Plasma.SignalPlotter.setVerticalLinesScroll(bool value)'''
        def verticalLinesDistance(self):
            '''int Plasma.SignalPlotter.verticalLinesDistance()'''
            return int()
        def setVerticalLinesDistance(self, distance):
            '''void Plasma.SignalPlotter.setVerticalLinesDistance(int distance)'''
        def verticalLinesColor(self):
            '''QColor Plasma.SignalPlotter.verticalLinesColor()'''
            return QColor()
        def setVerticalLinesColor(self, color):
            '''void Plasma.SignalPlotter.setVerticalLinesColor(QColor color)'''
        def showVerticalLines(self):
            '''bool Plasma.SignalPlotter.showVerticalLines()'''
            return bool()
        def setShowVerticalLines(self, value):
            '''void Plasma.SignalPlotter.setShowVerticalLines(bool value)'''
        def horizontalScale(self):
            '''int Plasma.SignalPlotter.horizontalScale()'''
            return int()
        def setHorizontalScale(self, scale):
            '''void Plasma.SignalPlotter.setHorizontalScale(int scale)'''
        def verticalMaxValue(self):
            '''float Plasma.SignalPlotter.verticalMaxValue()'''
            return float()
        def verticalMinValue(self):
            '''float Plasma.SignalPlotter.verticalMinValue()'''
            return float()
        def setVerticalRange(self, min, max):
            '''void Plasma.SignalPlotter.setVerticalRange(float min, float max)'''
        def useAutoRange(self):
            '''bool Plasma.SignalPlotter.useAutoRange()'''
            return bool()
        def setUseAutoRange(self, value):
            '''void Plasma.SignalPlotter.setUseAutoRange(bool value)'''
        def scaledBy(self):
            '''float Plasma.SignalPlotter.scaledBy()'''
            return float()
        def scale(self, delta):
            '''void Plasma.SignalPlotter.scale(float delta)'''
        def unit(self):
            '''QString Plasma.SignalPlotter.unit()'''
            return QString()
        def setUnit(self, unit):
            '''void Plasma.SignalPlotter.setUnit(QString unit)'''
        def title(self):
            '''QString Plasma.SignalPlotter.title()'''
            return QString()
        def setTitle(self, title):
            '''void Plasma.SignalPlotter.setTitle(QString title)'''
        def plotColors(self):
            '''list-of-Plasma.PlotColor Plasma.SignalPlotter.plotColors()'''
            return [Plasma.PlotColor()]
        def removePlot(self, pos):
            '''void Plasma.SignalPlotter.removePlot(int pos)'''
        def reorderPlots(self, newOrder):
            '''void Plasma.SignalPlotter.reorderPlots(list-of-int newOrder)'''
        def addSample(self, samples):
            '''void Plasma.SignalPlotter.addSample(list-of-float samples)'''
        def addPlot(self, color):
            '''void Plasma.SignalPlotter.addPlot(QColor color)'''


