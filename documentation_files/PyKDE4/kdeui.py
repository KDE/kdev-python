class pyqtSignal():
 def connect(self, targetSignal): pass
 def emit(self, *args): pass
from QtCore import *

class K3Icon():
    """"""
    context = None # KIconLoader.Context - member
    path = None # QString - member
    size = None # int - member
    threshold = None # int - member
    type = None # KIconLoader.Type - member
    def __init__(self):
        '''void K3Icon.__init__()'''
    def __init__(self):
        '''K3Icon K3Icon.__init__()'''
        return K3Icon()
    def isValid(self):
        '''bool K3Icon.isValid()'''
        return bool()


class KDialog(QDialog):
    """"""
    # Enum KDialog.CaptionFlag
    NoCaptionFlags = 0
    AppNameCaption = 0
    ModifiedCaption = 0
    HIGCompliantCaption = 0

    # Enum KDialog.ButtonPopupMode
    InstantPopup = 0
    DelayedPopup = 0

    # Enum KDialog.ButtonCode
    __kdevpythondocumentation_builtin_None = 0
    Help = 0
    Default = 0
    Ok = 0
    Apply = 0
    Try = 0
    Cancel = 0
    Close = 0
    No = 0
    Yes = 0
    Reset = 0
    Details = 0
    User1 = 0
    User2 = 0
    User3 = 0
    NoDefault = 0

    def __init__(self, parent = None, flags = 0):
        '''void KDialog.__init__(QWidget parent = None, Qt.WindowFlags flags = 0)'''
    def setAllowEmbeddingInGraphicsView(self, allowEmbedding):
        '''static void KDialog.setAllowEmbeddingInGraphicsView(bool allowEmbedding)'''
    def updateGeometry(self):
        '''void KDialog.updateGeometry()'''
    def slotButtonClicked(self, button):
        '''void KDialog.slotButtonClicked(int button)'''
    def keyPressEvent(self):
        '''QKeyEvent KDialog.keyPressEvent()'''
        return QKeyEvent()
    def closeEvent(self, e):
        '''void KDialog.closeEvent(QCloseEvent e)'''
    def hideEvent(self):
        '''QHideEvent KDialog.hideEvent()'''
        return QHideEvent()
    aboutToShowDetails = pyqtSignal() # void aboutToShowDetails() - signal
    finished = pyqtSignal() # void finished() - signal
    hidden = pyqtSignal() # void hidden() - signal
    buttonClicked = pyqtSignal() # void buttonClicked(KDialog::ButtonCode) - signal
    closeClicked = pyqtSignal() # void closeClicked() - signal
    cancelClicked = pyqtSignal() # void cancelClicked() - signal
    noClicked = pyqtSignal() # void noClicked() - signal
    yesClicked = pyqtSignal() # void yesClicked() - signal
    okClicked = pyqtSignal() # void okClicked() - signal
    tryClicked = pyqtSignal() # void tryClicked() - signal
    applyClicked = pyqtSignal() # void applyClicked() - signal
    user1Clicked = pyqtSignal() # void user1Clicked() - signal
    user2Clicked = pyqtSignal() # void user2Clicked() - signal
    user3Clicked = pyqtSignal() # void user3Clicked() - signal
    resetClicked = pyqtSignal() # void resetClicked() - signal
    defaultClicked = pyqtSignal() # void defaultClicked() - signal
    helpClicked = pyqtSignal() # void helpClicked() - signal
    layoutHintChanged = pyqtSignal() # void layoutHintChanged() - signal
    def delayedDestruct(self):
        '''void KDialog.delayedDestruct()'''
    def setDetailsWidget(self, detailsWidget):
        '''void KDialog.setDetailsWidget(QWidget detailsWidget)'''
    def setDetailsWidgetVisible(self, visible):
        '''void KDialog.setDetailsWidgetVisible(bool visible)'''
    def isDetailsWidgetVisible(self):
        '''bool KDialog.isDetailsWidgetVisible()'''
        return bool()
    def setHelp(self, anchor, appname = QString()):
        '''void KDialog.setHelp(QString anchor, QString appname = QString())'''
    def setHelpLinkText(self, text):
        '''void KDialog.setHelpLinkText(QString text)'''
    def enableLinkedHelp(self, state):
        '''void KDialog.enableLinkedHelp(bool state)'''
    def enableButtonCancel(self, state):
        '''void KDialog.enableButtonCancel(bool state)'''
    def enableButtonApply(self, state):
        '''void KDialog.enableButtonApply(bool state)'''
    def enableButtonOk(self, state):
        '''void KDialog.enableButtonOk(bool state)'''
    def enableButton(self, id, state):
        '''void KDialog.enableButton(KDialog.ButtonCode id, bool state)'''
    def setPlainCaption(self, caption):
        '''void KDialog.setPlainCaption(QString caption)'''
    def setCaption(self, caption):
        '''void KDialog.setCaption(QString caption)'''
    def setCaption(self, caption, modified):
        '''void KDialog.setCaption(QString caption, bool modified)'''
    def minimumSizeHint(self):
        '''QSize KDialog.minimumSizeHint()'''
        return QSize()
    def sizeHint(self):
        '''QSize KDialog.sizeHint()'''
        return QSize()
    def mainWidget(self):
        '''QWidget KDialog.mainWidget()'''
        return QWidget()
    def setMainWidget(self, widget):
        '''void KDialog.setMainWidget(QWidget widget)'''
    def avoidArea(self, widget, area, screen = None):
        '''static bool KDialog.avoidArea(QWidget widget, QRect area, int screen = -1)'''
        return bool()
    def centerOnScreen(self, widget, screen = None):
        '''static void KDialog.centerOnScreen(QWidget widget, int screen = -1)'''
    def resizeLayout(self, widget, margin, spacing):
        '''static void KDialog.resizeLayout(QWidget widget, int margin, int spacing)'''
    def resizeLayout(self, lay, margin, spacing):
        '''static void KDialog.resizeLayout(QLayout lay, int margin, int spacing)'''
    def makeStandardCaption(self, userCaption, window = None, flags = None):
        '''static QString KDialog.makeStandardCaption(QString userCaption, QWidget window = None, KDialog.CaptionFlags flags = KDialog.HIGCompliantCaption)'''
        return QString()
    def groupSpacingHint(self):
        '''static int KDialog.groupSpacingHint()'''
        return int()
    def spacingHint(self):
        '''static int KDialog.spacingHint()'''
        return int()
    def marginHint(self):
        '''static int KDialog.marginHint()'''
        return int()
    def button(self, id):
        '''KPushButton KDialog.button(KDialog.ButtonCode id)'''
        return KPushButton()
    def isButtonEnabled(self, id):
        '''bool KDialog.isButtonEnabled(KDialog.ButtonCode id)'''
        return bool()
    def helpLinkText(self):
        '''QString KDialog.helpLinkText()'''
        return QString()
    def saveDialogSize(self, config, options = None):
        '''void KDialog.saveDialogSize(KConfigGroup config, KConfigBase.WriteConfigFlags options = KConfigGroup.Normal)'''
    def restoreDialogSize(self, config):
        '''void KDialog.restoreDialogSize(KConfigGroup config)'''
    def incrementInitialSize(self, size):
        '''void KDialog.incrementInitialSize(QSize size)'''
    def setInitialSize(self, size):
        '''void KDialog.setInitialSize(QSize size)'''
    def setButtonFocus(self, id):
        '''void KDialog.setButtonFocus(KDialog.ButtonCode id)'''
    def setButtonMenu(self, id, menu, popupmode = None):
        '''void KDialog.setButtonMenu(KDialog.ButtonCode id, QMenu menu, KDialog.ButtonPopupMode popupmode = KDialog.InstantPopup)'''
    def setButtonGuiItem(self, id, item):
        '''void KDialog.setButtonGuiItem(KDialog.ButtonCode id, KGuiItem item)'''
    def buttonWhatsThis(self, id):
        '''QString KDialog.buttonWhatsThis(KDialog.ButtonCode id)'''
        return QString()
    def setButtonWhatsThis(self, id, text):
        '''void KDialog.setButtonWhatsThis(KDialog.ButtonCode id, QString text)'''
    def buttonToolTip(self, id):
        '''QString KDialog.buttonToolTip(KDialog.ButtonCode id)'''
        return QString()
    def setButtonToolTip(self, id, text):
        '''void KDialog.setButtonToolTip(KDialog.ButtonCode id, QString text)'''
    def buttonIcon(self, id):
        '''KIcon KDialog.buttonIcon(KDialog.ButtonCode id)'''
        return KIcon()
    def setButtonIcon(self, id, icon):
        '''void KDialog.setButtonIcon(KDialog.ButtonCode id, KIcon icon)'''
    def buttonText(self, id):
        '''QString KDialog.buttonText(KDialog.ButtonCode id)'''
        return QString()
    def setButtonText(self, id, text):
        '''void KDialog.setButtonText(KDialog.ButtonCode id, QString text)'''
    def showButton(self, id, state):
        '''void KDialog.showButton(KDialog.ButtonCode id, bool state)'''
    def showButtonSeparator(self, state):
        '''void KDialog.showButtonSeparator(bool state)'''
    def defaultButton(self):
        '''KDialog.ButtonCode KDialog.defaultButton()'''
        return KDialog.ButtonCode()
    def setDefaultButton(self, id):
        '''void KDialog.setDefaultButton(KDialog.ButtonCode id)'''
    def setEscapeButton(self, id):
        '''void KDialog.setEscapeButton(KDialog.ButtonCode id)'''
    def setButtonsOrientation(self, orientation):
        '''void KDialog.setButtonsOrientation(Qt.Orientation orientation)'''
    def setButtons(self, buttonMask):
        '''void KDialog.setButtons(KDialog.ButtonCodes buttonMask)'''
    class ButtonPopupModes():
        """"""
        def __init__(self):
            '''KDialog.ButtonPopupModes KDialog.ButtonPopupModes.__init__()'''
            return KDialog.ButtonPopupModes()
        def __init__(self):
            '''int KDialog.ButtonPopupModes.__init__()'''
            return int()
        def __init__(self):
            '''void KDialog.ButtonPopupModes.__init__()'''
        def __bool__(self):
            '''int KDialog.ButtonPopupModes.__bool__()'''
            return int()
        def __ne__(self, f):
            '''bool KDialog.ButtonPopupModes.__ne__(KDialog.ButtonPopupModes f)'''
            return bool()
        def __eq__(self, f):
            '''bool KDialog.ButtonPopupModes.__eq__(KDialog.ButtonPopupModes f)'''
            return bool()
        def __invert__(self):
            '''KDialog.ButtonPopupModes KDialog.ButtonPopupModes.__invert__()'''
            return KDialog.ButtonPopupModes()
        def __and__(self, mask):
            '''KDialog.ButtonPopupModes KDialog.ButtonPopupModes.__and__(int mask)'''
            return KDialog.ButtonPopupModes()
        def __xor__(self, f):
            '''KDialog.ButtonPopupModes KDialog.ButtonPopupModes.__xor__(KDialog.ButtonPopupModes f)'''
            return KDialog.ButtonPopupModes()
        def __xor__(self, f):
            '''KDialog.ButtonPopupModes KDialog.ButtonPopupModes.__xor__(int f)'''
            return KDialog.ButtonPopupModes()
        def __or__(self, f):
            '''KDialog.ButtonPopupModes KDialog.ButtonPopupModes.__or__(KDialog.ButtonPopupModes f)'''
            return KDialog.ButtonPopupModes()
        def __or__(self, f):
            '''KDialog.ButtonPopupModes KDialog.ButtonPopupModes.__or__(int f)'''
            return KDialog.ButtonPopupModes()
        def __int__(self):
            '''int KDialog.ButtonPopupModes.__int__()'''
            return int()
        def __ixor__(self, f):
            '''KDialog.ButtonPopupModes KDialog.ButtonPopupModes.__ixor__(KDialog.ButtonPopupModes f)'''
            return KDialog.ButtonPopupModes()
        def __ior__(self, f):
            '''KDialog.ButtonPopupModes KDialog.ButtonPopupModes.__ior__(KDialog.ButtonPopupModes f)'''
            return KDialog.ButtonPopupModes()
        def __iand__(self, mask):
            '''KDialog.ButtonPopupModes KDialog.ButtonPopupModes.__iand__(int mask)'''
            return KDialog.ButtonPopupModes()
    class ButtonCodes():
        """"""
        def __init__(self):
            '''KDialog.ButtonCodes KDialog.ButtonCodes.__init__()'''
            return KDialog.ButtonCodes()
        def __init__(self):
            '''int KDialog.ButtonCodes.__init__()'''
            return int()
        def __init__(self):
            '''void KDialog.ButtonCodes.__init__()'''
        def __bool__(self):
            '''int KDialog.ButtonCodes.__bool__()'''
            return int()
        def __ne__(self, f):
            '''bool KDialog.ButtonCodes.__ne__(KDialog.ButtonCodes f)'''
            return bool()
        def __eq__(self, f):
            '''bool KDialog.ButtonCodes.__eq__(KDialog.ButtonCodes f)'''
            return bool()
        def __invert__(self):
            '''KDialog.ButtonCodes KDialog.ButtonCodes.__invert__()'''
            return KDialog.ButtonCodes()
        def __and__(self, mask):
            '''KDialog.ButtonCodes KDialog.ButtonCodes.__and__(int mask)'''
            return KDialog.ButtonCodes()
        def __xor__(self, f):
            '''KDialog.ButtonCodes KDialog.ButtonCodes.__xor__(KDialog.ButtonCodes f)'''
            return KDialog.ButtonCodes()
        def __xor__(self, f):
            '''KDialog.ButtonCodes KDialog.ButtonCodes.__xor__(int f)'''
            return KDialog.ButtonCodes()
        def __or__(self, f):
            '''KDialog.ButtonCodes KDialog.ButtonCodes.__or__(KDialog.ButtonCodes f)'''
            return KDialog.ButtonCodes()
        def __or__(self, f):
            '''KDialog.ButtonCodes KDialog.ButtonCodes.__or__(int f)'''
            return KDialog.ButtonCodes()
        def __int__(self):
            '''int KDialog.ButtonCodes.__int__()'''
            return int()
        def __ixor__(self, f):
            '''KDialog.ButtonCodes KDialog.ButtonCodes.__ixor__(KDialog.ButtonCodes f)'''
            return KDialog.ButtonCodes()
        def __ior__(self, f):
            '''KDialog.ButtonCodes KDialog.ButtonCodes.__ior__(KDialog.ButtonCodes f)'''
            return KDialog.ButtonCodes()
        def __iand__(self, mask):
            '''KDialog.ButtonCodes KDialog.ButtonCodes.__iand__(int mask)'''
            return KDialog.ButtonCodes()
    class CaptionFlags():
        """"""
        def __init__(self):
            '''KDialog.CaptionFlags KDialog.CaptionFlags.__init__()'''
            return KDialog.CaptionFlags()
        def __init__(self):
            '''int KDialog.CaptionFlags.__init__()'''
            return int()
        def __init__(self):
            '''void KDialog.CaptionFlags.__init__()'''
        def __bool__(self):
            '''int KDialog.CaptionFlags.__bool__()'''
            return int()
        def __ne__(self, f):
            '''bool KDialog.CaptionFlags.__ne__(KDialog.CaptionFlags f)'''
            return bool()
        def __eq__(self, f):
            '''bool KDialog.CaptionFlags.__eq__(KDialog.CaptionFlags f)'''
            return bool()
        def __invert__(self):
            '''KDialog.CaptionFlags KDialog.CaptionFlags.__invert__()'''
            return KDialog.CaptionFlags()
        def __and__(self, mask):
            '''KDialog.CaptionFlags KDialog.CaptionFlags.__and__(int mask)'''
            return KDialog.CaptionFlags()
        def __xor__(self, f):
            '''KDialog.CaptionFlags KDialog.CaptionFlags.__xor__(KDialog.CaptionFlags f)'''
            return KDialog.CaptionFlags()
        def __xor__(self, f):
            '''KDialog.CaptionFlags KDialog.CaptionFlags.__xor__(int f)'''
            return KDialog.CaptionFlags()
        def __or__(self, f):
            '''KDialog.CaptionFlags KDialog.CaptionFlags.__or__(KDialog.CaptionFlags f)'''
            return KDialog.CaptionFlags()
        def __or__(self, f):
            '''KDialog.CaptionFlags KDialog.CaptionFlags.__or__(int f)'''
            return KDialog.CaptionFlags()
        def __int__(self):
            '''int KDialog.CaptionFlags.__int__()'''
            return int()
        def __ixor__(self, f):
            '''KDialog.CaptionFlags KDialog.CaptionFlags.__ixor__(KDialog.CaptionFlags f)'''
            return KDialog.CaptionFlags()
        def __ior__(self, f):
            '''KDialog.CaptionFlags KDialog.CaptionFlags.__ior__(KDialog.CaptionFlags f)'''
            return KDialog.CaptionFlags()
        def __iand__(self, mask):
            '''KDialog.CaptionFlags KDialog.CaptionFlags.__iand__(int mask)'''
            return KDialog.CaptionFlags()


class KAboutApplicationDialog(KDialog):
    """"""
    # Enum KAboutApplicationDialog.Option
    NoOptions = 0
    HideTranslators = 0
    HideKdeVersion = 0

    def __init__(self, aboutData, parent = None):
        '''void KAboutApplicationDialog.__init__(KAboutData aboutData, QWidget parent = None)'''
    def __init__(self, aboutData, opts, parent = None):
        '''void KAboutApplicationDialog.__init__(KAboutData aboutData, KAboutApplicationDialog.Options opts, QWidget parent = None)'''
    class Options():
        """"""
        def __init__(self):
            '''KAboutApplicationDialog.Options KAboutApplicationDialog.Options.__init__()'''
            return KAboutApplicationDialog.Options()
        def __init__(self):
            '''int KAboutApplicationDialog.Options.__init__()'''
            return int()
        def __init__(self):
            '''void KAboutApplicationDialog.Options.__init__()'''
        def __bool__(self):
            '''int KAboutApplicationDialog.Options.__bool__()'''
            return int()
        def __ne__(self, f):
            '''bool KAboutApplicationDialog.Options.__ne__(KAboutApplicationDialog.Options f)'''
            return bool()
        def __eq__(self, f):
            '''bool KAboutApplicationDialog.Options.__eq__(KAboutApplicationDialog.Options f)'''
            return bool()
        def __invert__(self):
            '''KAboutApplicationDialog.Options KAboutApplicationDialog.Options.__invert__()'''
            return KAboutApplicationDialog.Options()
        def __and__(self, mask):
            '''KAboutApplicationDialog.Options KAboutApplicationDialog.Options.__and__(int mask)'''
            return KAboutApplicationDialog.Options()
        def __xor__(self, f):
            '''KAboutApplicationDialog.Options KAboutApplicationDialog.Options.__xor__(KAboutApplicationDialog.Options f)'''
            return KAboutApplicationDialog.Options()
        def __xor__(self, f):
            '''KAboutApplicationDialog.Options KAboutApplicationDialog.Options.__xor__(int f)'''
            return KAboutApplicationDialog.Options()
        def __or__(self, f):
            '''KAboutApplicationDialog.Options KAboutApplicationDialog.Options.__or__(KAboutApplicationDialog.Options f)'''
            return KAboutApplicationDialog.Options()
        def __or__(self, f):
            '''KAboutApplicationDialog.Options KAboutApplicationDialog.Options.__or__(int f)'''
            return KAboutApplicationDialog.Options()
        def __int__(self):
            '''int KAboutApplicationDialog.Options.__int__()'''
            return int()
        def __ixor__(self, f):
            '''KAboutApplicationDialog.Options KAboutApplicationDialog.Options.__ixor__(KAboutApplicationDialog.Options f)'''
            return KAboutApplicationDialog.Options()
        def __ior__(self, f):
            '''KAboutApplicationDialog.Options KAboutApplicationDialog.Options.__ior__(KAboutApplicationDialog.Options f)'''
            return KAboutApplicationDialog.Options()
        def __iand__(self, mask):
            '''KAboutApplicationDialog.Options KAboutApplicationDialog.Options.__iand__(int mask)'''
            return KAboutApplicationDialog.Options()


class KAbstractWidgetJobTracker(KJobTrackerInterface):
    """"""
    def __init__(self, parent = None):
        '''void KAbstractWidgetJobTracker.__init__(QWidget parent = None)'''
    resume = pyqtSignal() # void resume(KJob *) - signal
    suspend = pyqtSignal() # void suspend(KJob *) - signal
    stopped = pyqtSignal() # void stopped(KJob *) - signal
    def slotClean(self, job):
        '''void KAbstractWidgetJobTracker.slotClean(KJob job)'''
    def slotResume(self, job):
        '''void KAbstractWidgetJobTracker.slotResume(KJob job)'''
    def slotSuspend(self, job):
        '''void KAbstractWidgetJobTracker.slotSuspend(KJob job)'''
    def slotStop(self, job):
        '''void KAbstractWidgetJobTracker.slotStop(KJob job)'''
    def finished(self, job):
        '''void KAbstractWidgetJobTracker.finished(KJob job)'''
    def autoDelete(self, job):
        '''bool KAbstractWidgetJobTracker.autoDelete(KJob job)'''
        return bool()
    def setAutoDelete(self, job, autoDelete):
        '''void KAbstractWidgetJobTracker.setAutoDelete(KJob job, bool autoDelete)'''
    def stopOnClose(self, job):
        '''bool KAbstractWidgetJobTracker.stopOnClose(KJob job)'''
        return bool()
    def setStopOnClose(self, job, stopOnClose):
        '''void KAbstractWidgetJobTracker.setStopOnClose(KJob job, bool stopOnClose)'''
    def widget(self, job):
        '''abstract QWidget KAbstractWidgetJobTracker.widget(KJob job)'''
        return QWidget()
    def unregisterJob(self, job):
        '''void KAbstractWidgetJobTracker.unregisterJob(KJob job)'''
    def registerJob(self, job):
        '''void KAbstractWidgetJobTracker.registerJob(KJob job)'''


class KAcceleratorManager():
    """"""
    def __init__(self):
        '''void KAcceleratorManager.__init__()'''
    def __init__(self):
        '''KAcceleratorManager KAcceleratorManager.__init__()'''
        return KAcceleratorManager()
    def setNoAccel(self, widget):
        '''static void KAcceleratorManager.setNoAccel(QWidget widget)'''
    def last_manage(self, added, changed, removed):
        '''static void KAcceleratorManager.last_manage(QString added, QString changed, QString removed)'''
    def manage(self, widget, programmers_mode = False):
        '''static void KAcceleratorManager.manage(QWidget widget, bool programmers_mode = False)'''


class KAccelGen():
    """"""
    def generate(self, source, target):
        '''static void KAccelGen.generate(QStringList source, QStringList target)'''
    def isLegalAccelerator(self, str, index):
        '''static bool KAccelGen.isLegalAccelerator(QString str, int index)'''
        return bool()


class KAction(QWidgetAction):
    """"""
    # Enum KAction.GlobalShortcutLoading
    Autoloading = 0
    NoAutoloading = 0

    # Enum KAction.ShortcutType
    ActiveShortcut = 0
    DefaultShortcut = 0

    def __init__(self, parent):
        '''void KAction.__init__(QObject parent)'''
    def __init__(self, text, parent):
        '''void KAction.__init__(QString text, QObject parent)'''
    def __init__(self, icon, text, parent):
        '''void KAction.__init__(KIcon icon, QString text, QObject parent)'''
    authorized = pyqtSignal() # void authorized(KAuth::Action *) - signal
    def setAuthAction(self, action):
        '''void KAction.setAuthAction(KAuth.Action action)'''
    def setAuthAction(self, actionName):
        '''void KAction.setAuthAction(QString actionName)'''
    def authAction(self):
        '''KAuth.Action KAction.authAction()'''
        return KAuth.Action()
    globalShortcutChanged = pyqtSignal() # void globalShortcutChanged(const QKeySequenceamp;) - signal
    triggered = pyqtSignal() # void triggered(Qt::MouseButtons,Qt::KeyboardModifiers) - signal
    def event(self):
        '''QEvent KAction.event()'''
        return QEvent()
    def setRockerGesture(self, gest, type = None):
        '''void KAction.setRockerGesture(KRockerGesture gest, KAction.ShortcutTypes type = KAction.ShortcutTypes(KAction.ActiveShortcut|KAction.DefaultShortcut))'''
    def setShapeGesture(self, gest, type = None):
        '''void KAction.setShapeGesture(KShapeGesture gest, KAction.ShortcutTypes type = KAction.ShortcutTypes(KAction.ActiveShortcut|KAction.DefaultShortcut))'''
    def rockerGesture(self, type = None):
        '''KRockerGesture KAction.rockerGesture(KAction.ShortcutTypes type = KAction.ActiveShortcut)'''
        return KRockerGesture()
    def shapeGesture(self, type = None):
        '''KShapeGesture KAction.shapeGesture(KAction.ShortcutTypes type = KAction.ActiveShortcut)'''
        return KShapeGesture()
    def forgetGlobalShortcut(self):
        '''void KAction.forgetGlobalShortcut()'''
    def isGlobalShortcutEnabled(self):
        '''bool KAction.isGlobalShortcutEnabled()'''
        return bool()
    def setGlobalShortcutAllowed(self, allowed, loading = None):
        '''void KAction.setGlobalShortcutAllowed(bool allowed, KAction.GlobalShortcutLoading loading = KAction.Autoloading)'''
    def globalShortcutAllowed(self):
        '''bool KAction.globalShortcutAllowed()'''
        return bool()
    def setGlobalShortcut(self, shortcut, type = None, loading = None):
        '''void KAction.setGlobalShortcut(KShortcut shortcut, KAction.ShortcutTypes type = KAction.ShortcutTypes(KAction.ActiveShortcut|KAction.DefaultShortcut), KAction.GlobalShortcutLoading loading = KAction.Autoloading)'''
    def globalShortcut(self, type = None):
        '''KShortcut KAction.globalShortcut(KAction.ShortcutTypes type = KAction.ActiveShortcut)'''
        return KShortcut()
    def setShortcutConfigurable(self, configurable):
        '''void KAction.setShortcutConfigurable(bool configurable)'''
    def isShortcutConfigurable(self):
        '''bool KAction.isShortcutConfigurable()'''
        return bool()
    def setShortcuts(self, shortcuts, type = None):
        '''void KAction.setShortcuts(list-of-QKeySequence shortcuts, KAction.ShortcutTypes type = KAction.ShortcutTypes(KAction.ActiveShortcut|KAction.DefaultShortcut))'''
    def setShortcut(self, shortcut, type = None):
        '''void KAction.setShortcut(KShortcut shortcut, KAction.ShortcutTypes type = KAction.ShortcutTypes(KAction.ActiveShortcut|KAction.DefaultShortcut))'''
    def setShortcut(self, shortcut, type = None):
        '''void KAction.setShortcut(QKeySequence shortcut, KAction.ShortcutTypes type = KAction.ShortcutTypes(KAction.ActiveShortcut|KAction.DefaultShortcut))'''
    def shortcut(self, types = None):
        '''KShortcut KAction.shortcut(KAction.ShortcutTypes types = KAction.ActiveShortcut)'''
        return KShortcut()
    def setHelpText(self, text):
        '''void KAction.setHelpText(QString text)'''
    class ShortcutTypes():
        """"""
        def __init__(self):
            '''KAction.ShortcutTypes KAction.ShortcutTypes.__init__()'''
            return KAction.ShortcutTypes()
        def __init__(self):
            '''int KAction.ShortcutTypes.__init__()'''
            return int()
        def __init__(self):
            '''void KAction.ShortcutTypes.__init__()'''
        def __bool__(self):
            '''int KAction.ShortcutTypes.__bool__()'''
            return int()
        def __ne__(self, f):
            '''bool KAction.ShortcutTypes.__ne__(KAction.ShortcutTypes f)'''
            return bool()
        def __eq__(self, f):
            '''bool KAction.ShortcutTypes.__eq__(KAction.ShortcutTypes f)'''
            return bool()
        def __invert__(self):
            '''KAction.ShortcutTypes KAction.ShortcutTypes.__invert__()'''
            return KAction.ShortcutTypes()
        def __and__(self, mask):
            '''KAction.ShortcutTypes KAction.ShortcutTypes.__and__(int mask)'''
            return KAction.ShortcutTypes()
        def __xor__(self, f):
            '''KAction.ShortcutTypes KAction.ShortcutTypes.__xor__(KAction.ShortcutTypes f)'''
            return KAction.ShortcutTypes()
        def __xor__(self, f):
            '''KAction.ShortcutTypes KAction.ShortcutTypes.__xor__(int f)'''
            return KAction.ShortcutTypes()
        def __or__(self, f):
            '''KAction.ShortcutTypes KAction.ShortcutTypes.__or__(KAction.ShortcutTypes f)'''
            return KAction.ShortcutTypes()
        def __or__(self, f):
            '''KAction.ShortcutTypes KAction.ShortcutTypes.__or__(int f)'''
            return KAction.ShortcutTypes()
        def __int__(self):
            '''int KAction.ShortcutTypes.__int__()'''
            return int()
        def __ixor__(self, f):
            '''KAction.ShortcutTypes KAction.ShortcutTypes.__ixor__(KAction.ShortcutTypes f)'''
            return KAction.ShortcutTypes()
        def __ior__(self, f):
            '''KAction.ShortcutTypes KAction.ShortcutTypes.__ior__(KAction.ShortcutTypes f)'''
            return KAction.ShortcutTypes()
        def __iand__(self, mask):
            '''KAction.ShortcutTypes KAction.ShortcutTypes.__iand__(int mask)'''
            return KAction.ShortcutTypes()


class KActionCategory(QObject):
    """"""
    def __init__(self, text, parent = None):
        '''void KActionCategory.__init__(QString text, KActionCollection parent = None)'''
    def setText(self, text):
        '''void KActionCategory.setText(QString text)'''
    def text(self):
        '''QString KActionCategory.text()'''
        return QString()
    def collection(self):
        '''KActionCollection KActionCategory.collection()'''
        return KActionCollection()
    def actions(self):
        '''list-of-QAction KActionCategory.actions()'''
        return [QAction()]
    def addAction(self, name, action):
        '''QAction KActionCategory.addAction(QString name, QAction action)'''
        return QAction()
    def addAction(self, name, action):
        '''KAction KActionCategory.addAction(QString name, KAction action)'''
        return KAction()
    def addAction(self, actionType, receiver = None, member = None):
        '''KAction KActionCategory.addAction(KStandardAction.StandardAction actionType, QObject receiver = None, str member = None)'''
        return KAction()
    def addAction(self, actionType, name, receiver = None, member = None):
        '''KAction KActionCategory.addAction(KStandardAction.StandardAction actionType, QString name, QObject receiver = None, str member = None)'''
        return KAction()
    def addAction(self, name, receiver = None, member = None):
        '''KAction KActionCategory.addAction(QString name, QObject receiver = None, str member = None)'''
        return KAction()


class KActionCollection(QObject):
    """"""
    def __init__(self, parent, cData = KComponentData()):
        '''void KActionCollection.__init__(QObject parent, KComponentData cData = KComponentData())'''
    def takeAction(self, action):
        '''QAction KActionCollection.takeAction(QAction action)'''
        return QAction()
    def removeAction(self, action):
        '''void KActionCollection.removeAction(QAction action)'''
    def addAction(self, name, action):
        '''QAction KActionCollection.addAction(QString name, QAction action)'''
        return QAction()
    def addAction(self, name, action):
        '''KAction KActionCollection.addAction(QString name, KAction action)'''
        return KAction()
    def addAction(self, actionType, receiver = None, member = None):
        '''KAction KActionCollection.addAction(KStandardAction.StandardAction actionType, QObject receiver = None, str member = None)'''
        return KAction()
    def addAction(self, actionType, name, receiver = None, member = None):
        '''KAction KActionCollection.addAction(KStandardAction.StandardAction actionType, QString name, QObject receiver = None, str member = None)'''
        return KAction()
    def addAction(self, name, receiver = None, member = None):
        '''KAction KActionCollection.addAction(QString name, QObject receiver = None, str member = None)'''
        return KAction()
    def slotActionHighlighted(self):
        '''void KActionCollection.slotActionHighlighted()'''
    def slotActionTriggered(self):
        '''void KActionCollection.slotActionTriggered()'''
    def connectNotify(self):
        '''SIGNAL() KActionCollection.connectNotify()'''
        return SIGNAL()()
    actionTriggered = pyqtSignal() # void actionTriggered(QAction *) - signal
    actionHovered = pyqtSignal() # void actionHovered(QAction *) - signal
    actionHighlighted = pyqtSignal() # void actionHighlighted(QAction *) - signal
    removed = pyqtSignal() # void removed(QAction *) - signal
    inserted = pyqtSignal() # void inserted(QAction *) - signal
    def parentGUIClient(self):
        '''KXMLGUIClient KActionCollection.parentGUIClient()'''
        return KXMLGUIClient()
    def componentData(self):
        '''KComponentData KActionCollection.componentData()'''
        return KComponentData()
    def setComponentData(self, componentData):
        '''void KActionCollection.setComponentData(KComponentData componentData)'''
    def actionGroups(self):
        '''list-of-QActionGroup KActionCollection.actionGroups()'''
        return [QActionGroup()]
    def actionsWithoutGroup(self):
        '''list-of-QAction KActionCollection.actionsWithoutGroup()'''
        return [QAction()]
    def actions(self):
        '''list-of-QAction KActionCollection.actions()'''
        return [QAction()]
    def action(self, index):
        '''QAction KActionCollection.action(int index)'''
        return QAction()
    def action(self, name):
        '''QAction KActionCollection.action(QString name)'''
        return QAction()
    def isEmpty(self):
        '''bool KActionCollection.isEmpty()'''
        return bool()
    def count(self):
        '''int KActionCollection.count()'''
        return int()
    def writeSettings(self, config = None, writeDefaults = False, oneAction = None):
        '''void KActionCollection.writeSettings(KConfigGroup config = None, bool writeDefaults = False, QAction oneAction = None)'''
    def exportGlobalShortcuts(self, config, writeDefaults = False):
        '''void KActionCollection.exportGlobalShortcuts(KConfigGroup config, bool writeDefaults = False)'''
    def importGlobalShortcuts(self, config):
        '''void KActionCollection.importGlobalShortcuts(KConfigGroup config)'''
    def readSettings(self, config = None):
        '''void KActionCollection.readSettings(KConfigGroup config = None)'''
    def setConfigGlobal(self, global_):
        '''void KActionCollection.setConfigGlobal(bool global)'''
    def setConfigGroup(self, group):
        '''void KActionCollection.setConfigGroup(QString group)'''
    def configIsGlobal(self):
        '''bool KActionCollection.configIsGlobal()'''
        return bool()
    def configGroup(self):
        '''QString KActionCollection.configGroup()'''
        return QString()
    def clearAssociatedWidgets(self):
        '''void KActionCollection.clearAssociatedWidgets()'''
    def associatedWidgets(self):
        '''list-of-QWidget KActionCollection.associatedWidgets()'''
        return [QWidget()]
    def removeAssociatedWidget(self, widget):
        '''void KActionCollection.removeAssociatedWidget(QWidget widget)'''
    def addAssociatedWidget(self, widget):
        '''void KActionCollection.addAssociatedWidget(QWidget widget)'''
    def associateWidget(self, widget):
        '''void KActionCollection.associateWidget(QWidget widget)'''
    def clear(self):
        '''void KActionCollection.clear()'''
    def allCollections(self):
        '''static list-of-KActionCollection KActionCollection.allCollections()'''
        return [KActionCollection()]


class KActionMenu(KAction):
    """"""
    def __init__(self, parent):
        '''void KActionMenu.__init__(QObject parent)'''
    def __init__(self, text, parent):
        '''void KActionMenu.__init__(QString text, QObject parent)'''
    def __init__(self, icon, text, parent):
        '''void KActionMenu.__init__(KIcon icon, QString text, QObject parent)'''
    def createWidget(self, parent):
        '''QWidget KActionMenu.createWidget(QWidget parent)'''
        return QWidget()
    def setStickyMenu(self, sticky):
        '''void KActionMenu.setStickyMenu(bool sticky)'''
    def stickyMenu(self):
        '''bool KActionMenu.stickyMenu()'''
        return bool()
    def setDelayed(self, delayed):
        '''void KActionMenu.setDelayed(bool delayed)'''
    def delayed(self):
        '''bool KActionMenu.delayed()'''
        return bool()
    def setMenu(self, menu):
        '''void KActionMenu.setMenu(KMenu menu)'''
    def menu(self):
        '''KMenu KActionMenu.menu()'''
        return KMenu()
    def popupMenu(self):
        '''KMenu KActionMenu.popupMenu()'''
        return KMenu()
    def removeAction(self, action):
        '''void KActionMenu.removeAction(QAction action)'''
    def insertSeparator(self, before):
        '''QAction KActionMenu.insertSeparator(QAction before)'''
        return QAction()
    def insertAction(self, before, action):
        '''void KActionMenu.insertAction(QAction before, QAction action)'''
    def addSeparator(self):
        '''QAction KActionMenu.addSeparator()'''
        return QAction()
    def addAction(self, action):
        '''void KActionMenu.addAction(QAction action)'''
    def remove(self):
        '''KAction KActionMenu.remove()'''
        return KAction()


class KActionSelector(QWidget):
    """"""
    # Enum KActionSelector.InsertionPolicy
    BelowCurrent = 0
    Sorted = 0
    AtTop = 0
    AtBottom = 0

    # Enum KActionSelector.MoveButton
    ButtonAdd = 0
    ButtonRemove = 0
    ButtonUp = 0
    ButtonDown = 0

    def __init__(self, parent = None):
        '''void KActionSelector.__init__(QWidget parent = None)'''
    def eventFilter(self):
        '''QEvent KActionSelector.eventFilter()'''
        return QEvent()
    def keyPressEvent(self):
        '''QKeyEvent KActionSelector.keyPressEvent()'''
        return QKeyEvent()
    def polish(self):
        '''void KActionSelector.polish()'''
    movedDown = pyqtSignal() # void movedDown(QListWidgetItem *) - signal
    movedUp = pyqtSignal() # void movedUp(QListWidgetItem *) - signal
    removed = pyqtSignal() # void removed(QListWidgetItem *) - signal
    added = pyqtSignal() # void added(QListWidgetItem *) - signal
    def setButtonsEnabled(self):
        '''void KActionSelector.setButtonsEnabled()'''
    def setButtonWhatsThis(self, text, button):
        '''void KActionSelector.setButtonWhatsThis(QString text, KActionSelector.MoveButton button)'''
    def setButtonTooltip(self, tip, button):
        '''void KActionSelector.setButtonTooltip(QString tip, KActionSelector.MoveButton button)'''
    def setButtonIconSet(self, iconset, button):
        '''void KActionSelector.setButtonIconSet(QIcon iconset, KActionSelector.MoveButton button)'''
    def setButtonIcon(self, icon, button):
        '''void KActionSelector.setButtonIcon(QString icon, KActionSelector.MoveButton button)'''
    def setShowUpDownButtons(self, show):
        '''void KActionSelector.setShowUpDownButtons(bool show)'''
    def showUpDownButtons(self):
        '''bool KActionSelector.showUpDownButtons()'''
        return bool()
    def setSelectedInsertionPolicy(self, policy):
        '''void KActionSelector.setSelectedInsertionPolicy(KActionSelector.InsertionPolicy policy)'''
    def selectedInsertionPolicy(self):
        '''KActionSelector.InsertionPolicy KActionSelector.selectedInsertionPolicy()'''
        return KActionSelector.InsertionPolicy()
    def setAvailableInsertionPolicy(self, policy):
        '''void KActionSelector.setAvailableInsertionPolicy(KActionSelector.InsertionPolicy policy)'''
    def availableInsertionPolicy(self):
        '''KActionSelector.InsertionPolicy KActionSelector.availableInsertionPolicy()'''
        return KActionSelector.InsertionPolicy()
    def setSelectedLabel(self, text):
        '''void KActionSelector.setSelectedLabel(QString text)'''
    def selectedLabel(self):
        '''QString KActionSelector.selectedLabel()'''
        return QString()
    def setAvailableLabel(self, text):
        '''void KActionSelector.setAvailableLabel(QString text)'''
    def availableLabel(self):
        '''QString KActionSelector.availableLabel()'''
        return QString()
    def setKeyboardEnabled(self, enable):
        '''void KActionSelector.setKeyboardEnabled(bool enable)'''
    def keyboardEnabled(self):
        '''bool KActionSelector.keyboardEnabled()'''
        return bool()
    def setMoveOnDoubleClick(self, enable):
        '''void KActionSelector.setMoveOnDoubleClick(bool enable)'''
    def moveOnDoubleClick(self):
        '''bool KActionSelector.moveOnDoubleClick()'''
        return bool()
    def selectedListWidget(self):
        '''QListWidget KActionSelector.selectedListWidget()'''
        return QListWidget()
    def availableListWidget(self):
        '''QListWidget KActionSelector.availableListWidget()'''
        return QListWidget()


class KAnimatedButton(QToolButton):
    """"""
    def __init__(self, parent = None):
        '''void KAnimatedButton.__init__(QWidget parent = None)'''
    def slotTimerUpdate(self):
        '''void KAnimatedButton.slotTimerUpdate()'''
    clicked = pyqtSignal() # void clicked() - signal
    def updateIcons(self):
        '''void KAnimatedButton.updateIcons()'''
    def stop(self):
        '''void KAnimatedButton.stop()'''
    def start(self):
        '''void KAnimatedButton.start()'''
    def setIcons(self, icons):
        '''void KAnimatedButton.setIcons(QString icons)'''
    def icons(self):
        '''QString KAnimatedButton.icons()'''
        return QString()
    def iconDimensions(self):
        '''int KAnimatedButton.iconDimensions()'''
        return int()


class KApplication(QApplication):
    """"""
    loadedByKdeinit = None # bool - member
    def __init__(self, GUIenabled = True):
        '''void KApplication.__init__(bool GUIenabled = True)'''
    def __init__(self, display, visual = 0, colormap = 0):
        '''void KApplication.__init__(Display display, int visual = 0, int colormap = 0)'''
    def __init__(self, display, list, rAppName, GUIenabled = True):
        '''void KApplication.__init__(Display display, list list, QByteArray rAppName, bool GUIenabled = True)'''
    def __init__(self, GUIenabled, cData):
        '''void KApplication.__init__(bool GUIenabled, KComponentData cData)'''
    def __init__(self, display, visual, colormap, cData):
        '''void KApplication.__init__(Display display, int visual, int colormap, KComponentData cData)'''
    saveYourself = pyqtSignal() # void saveYourself() - signal
    def quit(self):
        '''void KApplication.quit()'''
    def reparseConfiguration(self):
        '''void KApplication.reparseConfiguration()'''
    def updateUserTimestamp(self, time = 0):
        '''void KApplication.updateUserTimestamp(int time = 0)'''
    def xioErrhandler(self):
        '''Display KApplication.xioErrhandler()'''
        return Display()
    def notify(self, receiver, event):
        '''bool KApplication.notify(QObject receiver, QEvent event)'''
        return bool()
    def updateRemoteUserTimestamp(self, service, time = 0):
        '''void KApplication.updateRemoteUserTimestamp(QString service, int time = 0)'''
    def userTimestamp(self):
        '''int KApplication.userTimestamp()'''
        return int()
    def setSynchronizeClipboard(self, synchronize):
        '''void KApplication.setSynchronizeClipboard(bool synchronize)'''
    def clearStartupId(self):
        '''void KApplication.clearStartupId()'''
    def setStartupId(self, startup_id):
        '''void KApplication.setStartupId(QByteArray startup_id)'''
    def startupId(self):
        '''QByteArray KApplication.startupId()'''
        return QByteArray()
    def removeX11EventFilter(self, filter):
        '''void KApplication.removeX11EventFilter(QWidget filter)'''
    def installX11EventFilter(self, filter):
        '''void KApplication.installX11EventFilter(QWidget filter)'''
    def checkRecoverFile(self, pFilename, bRecover):
        '''static QString KApplication.checkRecoverFile(QString pFilename, bool bRecover)'''
        return QString()
    def tempSaveName(self, pFilename):
        '''static QString KApplication.tempSaveName(QString pFilename)'''
        return QString()
    def setTopWidget(self, topWidget):
        '''void KApplication.setTopWidget(QWidget topWidget)'''
    def sessionSaving(self):
        '''bool KApplication.sessionSaving()'''
        return bool()
    def saveState(self, sm):
        '''void KApplication.saveState(QSessionManager sm)'''
    def commitData(self, sm):
        '''void KApplication.commitData(QSessionManager sm)'''
    def enableSessionManagement(self):
        '''void KApplication.enableSessionManagement()'''
    def disableSessionManagement(self):
        '''void KApplication.disableSessionManagement()'''
    def sessionConfig(self):
        '''KConfig KApplication.sessionConfig()'''
        return KConfig()
    def kApplication(self):
        '''static KApplication KApplication.kApplication()'''
        return KApplication()


class KArrowButton(QPushButton):
    """"""
    def __init__(self, parent = None, arrow = None):
        '''void KArrowButton.__init__(QWidget parent = None, Qt.ArrowType arrow = Qt.UpArrow)'''
    def paintEvent(self):
        '''QPaintEvent KArrowButton.paintEvent()'''
        return QPaintEvent()
    def setArrowType(self, a):
        '''void KArrowButton.setArrowType(Qt.ArrowType a)'''
    def setArrowTp(self, tp):
        '''void KArrowButton.setArrowTp(int tp)'''
    def arrowTp(self):
        '''int KArrowButton.arrowTp()'''
        return int()
    def arrowType(self):
        '''Qt.ArrowType KArrowButton.arrowType()'''
        return Qt.ArrowType()
    def sizeHint(self):
        '''QSize KArrowButton.sizeHint()'''
        return QSize()


class KPageDialog(KDialog):
    """"""
    # Enum KPageDialog.FaceType
    Auto = 0
    Plain = 0
    List = 0
    Tree = 0
    Tabbed = 0

    def __init__(self, parent = None, flags = 0):
        '''void KPageDialog.__init__(QWidget parent = None, Qt.WindowFlags flags = 0)'''
    def __init__(self, widget, parent, flags = 0):
        '''void KPageDialog.__init__(KPageWidget widget, QWidget parent, Qt.WindowFlags flags = 0)'''
    def setPageWidget(self, widget):
        '''void KPageDialog.setPageWidget(KPageWidget widget)'''
    def pageWidget(self):
        '''KPageWidget KPageDialog.pageWidget()'''
        return KPageWidget()
    pageRemoved = pyqtSignal() # void pageRemoved(KPageWidgetItem *) - signal
    currentPageChanged = pyqtSignal() # void currentPageChanged(KPageWidgetItem *,KPageWidgetItem *) - signal
    def currentPage(self):
        '''KPageWidgetItem KPageDialog.currentPage()'''
        return KPageWidgetItem()
    def setCurrentPage(self, item):
        '''void KPageDialog.setCurrentPage(KPageWidgetItem item)'''
    def removePage(self, item):
        '''void KPageDialog.removePage(KPageWidgetItem item)'''
    def addSubPage(self, parent, widget, name):
        '''KPageWidgetItem KPageDialog.addSubPage(KPageWidgetItem parent, QWidget widget, QString name)'''
        return KPageWidgetItem()
    def addSubPage(self, parent, item):
        '''void KPageDialog.addSubPage(KPageWidgetItem parent, KPageWidgetItem item)'''
    def insertPage(self, before, widget, name):
        '''KPageWidgetItem KPageDialog.insertPage(KPageWidgetItem before, QWidget widget, QString name)'''
        return KPageWidgetItem()
    def insertPage(self, before, item):
        '''void KPageDialog.insertPage(KPageWidgetItem before, KPageWidgetItem item)'''
    def addPage(self, widget, name):
        '''KPageWidgetItem KPageDialog.addPage(QWidget widget, QString name)'''
        return KPageWidgetItem()
    def addPage(self, item):
        '''void KPageDialog.addPage(KPageWidgetItem item)'''
    def setFaceType(self, faceType):
        '''void KPageDialog.setFaceType(KPageDialog.FaceType faceType)'''


class KAssistantDialog(KPageDialog):
    """"""
    def __init__(self, parent = None, flags = 0):
        '''void KAssistantDialog.__init__(QWidget parent = None, Qt.WindowFlags flags = 0)'''
    def __init__(self, widget, parent = None, flags = 0):
        '''void KAssistantDialog.__init__(KPageWidget widget, QWidget parent = None, Qt.WindowFlags flags = 0)'''
    def showEvent(self, event):
        '''void KAssistantDialog.showEvent(QShowEvent event)'''
    def next(self):
        '''void KAssistantDialog.next()'''
    def back(self):
        '''void KAssistantDialog.back()'''
    def isAppropriate(self, page):
        '''bool KAssistantDialog.isAppropriate(KPageWidgetItem page)'''
        return bool()
    def setAppropriate(self, page, appropriate):
        '''void KAssistantDialog.setAppropriate(KPageWidgetItem page, bool appropriate)'''
    def isValid(self, page):
        '''bool KAssistantDialog.isValid(KPageWidgetItem page)'''
        return bool()
    def setValid(self, page, enable):
        '''void KAssistantDialog.setValid(KPageWidgetItem page, bool enable)'''


class KBreadcrumbSelectionModel(QItemSelectionModel):
    """"""
    # Enum KBreadcrumbSelectionModel.BreadcrumbTarget
    MakeBreadcrumbSelectionInOther = 0
    MakeBreadcrumbSelectionInSelf = 0

    def __init__(self, selectionModel, parent = None):
        '''void KBreadcrumbSelectionModel.__init__(QItemSelectionModel selectionModel, QObject parent = None)'''
    def __init__(self, selectionModel, target, parent = None):
        '''void KBreadcrumbSelectionModel.__init__(QItemSelectionModel selectionModel, KBreadcrumbSelectionModel.BreadcrumbTarget target, QObject parent = None)'''
    def select(self, index, command):
        '''void KBreadcrumbSelectionModel.select(QModelIndex index, QItemSelectionModel.SelectionFlags command)'''
    def select(self, selection, command):
        '''void KBreadcrumbSelectionModel.select(QItemSelection selection, QItemSelectionModel.SelectionFlags command)'''
    def setBreadcrumbLength(self, breadcrumbLength):
        '''void KBreadcrumbSelectionModel.setBreadcrumbLength(int breadcrumbLength)'''
    def breadcrumbLength(self):
        '''int KBreadcrumbSelectionModel.breadcrumbLength()'''
        return int()
    def setActualSelectionIncluded(self, isActualSelectionIncluded):
        '''void KBreadcrumbSelectionModel.setActualSelectionIncluded(bool isActualSelectionIncluded)'''
    def isActualSelectionIncluded(self):
        '''bool KBreadcrumbSelectionModel.isActualSelectionIncluded()'''
        return bool()


class KBugReport(KDialog):
    """"""
    def __init__(self, parent = None, modal = True, aboutData = None):
        '''void KBugReport.__init__(QWidget parent = None, bool modal = True, KAboutData aboutData = None)'''
    def closeEvent(self, e):
        '''void KBugReport.closeEvent(QCloseEvent e)'''
    def sendBugReport(self):
        '''bool KBugReport.sendBugReport()'''
        return bool()
    def text(self):
        '''QString KBugReport.text()'''
        return QString()
    def accept(self):
        '''void KBugReport.accept()'''
    def setMessageBody(self, messageBody):
        '''void KBugReport.setMessageBody(QString messageBody)'''
    def messageBody(self):
        '''QString KBugReport.messageBody()'''
        return QString()


class KButtonGroup(QGroupBox):
    """"""
    def __init__(self, parent = None):
        '''void KButtonGroup.__init__(QWidget parent = None)'''
    def childEvent(self, event):
        '''void KButtonGroup.childEvent(QChildEvent event)'''
    changed = pyqtSignal() # void changed(int) - signal
    released = pyqtSignal() # void released(int) - signal
    pressed = pyqtSignal() # void pressed(int) - signal
    clicked = pyqtSignal() # void clicked(int) - signal
    def setSelected(self, id):
        '''void KButtonGroup.setSelected(int id)'''
    def id(self, button):
        '''int KButtonGroup.id(QAbstractButton button)'''
        return int()
    def selected(self):
        '''int KButtonGroup.selected()'''
        return int()


class KCapacityBar(QWidget):
    """"""
    # Enum KCapacityBar.DrawTextMode
    DrawTextInline = 0
    DrawTextOutline = 0

    def __init__(self, drawTextMode = None, parent = None):
        '''void KCapacityBar.__init__(KCapacityBar.DrawTextMode drawTextMode = KCapacityBar.DrawTextOutline, QWidget parent = None)'''
    def drawTextMode(self):
        '''KCapacityBar.DrawTextMode KCapacityBar.drawTextMode()'''
        return KCapacityBar.DrawTextMode()
    def setDrawTextMode(self, mode):
        '''void KCapacityBar.setDrawTextMode(KCapacityBar.DrawTextMode mode)'''
    def changeEvent(self, event):
        '''void KCapacityBar.changeEvent(QEvent event)'''
    def paintEvent(self, event):
        '''void KCapacityBar.paintEvent(QPaintEvent event)'''
    def minimumSizeHint(self):
        '''QSize KCapacityBar.minimumSizeHint()'''
        return QSize()
    def drawCapacityBar(self, p, rect):
        '''void KCapacityBar.drawCapacityBar(QPainter p, QRect rect)'''
    def horizontalTextAlignment(self):
        '''Qt.Alignment KCapacityBar.horizontalTextAlignment()'''
        return Qt.Alignment()
    def setHorizontalTextAlignment(self, textAlignment):
        '''void KCapacityBar.setHorizontalTextAlignment(Qt.Alignment textAlignment)'''
    def barHeight(self):
        '''int KCapacityBar.barHeight()'''
        return int()
    def setBarHeight(self, barHeight):
        '''void KCapacityBar.setBarHeight(int barHeight)'''
    def continuous(self):
        '''bool KCapacityBar.continuous()'''
        return bool()
    def setContinuous(self, continuous):
        '''void KCapacityBar.setContinuous(bool continuous)'''
    def fillFullBlocks(self):
        '''bool KCapacityBar.fillFullBlocks()'''
        return bool()
    def setFillFullBlocks(self, fillFullBlocks):
        '''void KCapacityBar.setFillFullBlocks(bool fillFullBlocks)'''
    def text(self):
        '''QString KCapacityBar.text()'''
        return QString()
    def setText(self, text):
        '''void KCapacityBar.setText(QString text)'''
    def value(self):
        '''int KCapacityBar.value()'''
        return int()
    def setValue(self, value):
        '''void KCapacityBar.setValue(int value)'''


class KCategorizedSortFilterProxyModel(QSortFilterProxyModel):
    """"""
    # Enum KCategorizedSortFilterProxyModel.AdditionalRoles
    CategoryDisplayRole = 0
    CategorySortRole = 0

    def __init__(self, parent = None):
        '''void KCategorizedSortFilterProxyModel.__init__(QObject parent = None)'''
    def compareCategories(self, left, right):
        '''int KCategorizedSortFilterProxyModel.compareCategories(QModelIndex left, QModelIndex right)'''
        return int()
    def subSortLessThan(self, left, right):
        '''bool KCategorizedSortFilterProxyModel.subSortLessThan(QModelIndex left, QModelIndex right)'''
        return bool()
    def lessThan(self, left, right):
        '''bool KCategorizedSortFilterProxyModel.lessThan(QModelIndex left, QModelIndex right)'''
        return bool()
    def naturalCompare(self, a, b):
        '''static int KCategorizedSortFilterProxyModel.naturalCompare(QString a, QString b)'''
        return int()
    def sortCategoriesByNaturalComparison(self):
        '''bool KCategorizedSortFilterProxyModel.sortCategoriesByNaturalComparison()'''
        return bool()
    def setSortCategoriesByNaturalComparison(self, sortCategoriesByNaturalComparison):
        '''void KCategorizedSortFilterProxyModel.setSortCategoriesByNaturalComparison(bool sortCategoriesByNaturalComparison)'''
    def sortOrder(self):
        '''Qt.SortOrder KCategorizedSortFilterProxyModel.sortOrder()'''
        return Qt.SortOrder()
    def sortColumn(self):
        '''int KCategorizedSortFilterProxyModel.sortColumn()'''
        return int()
    def setCategorizedModel(self, categorizedModel):
        '''void KCategorizedSortFilterProxyModel.setCategorizedModel(bool categorizedModel)'''
    def isCategorizedModel(self):
        '''bool KCategorizedSortFilterProxyModel.isCategorizedModel()'''
        return bool()
    def sort(self, column, order = None):
        '''void KCategorizedSortFilterProxyModel.sort(int column, Qt.SortOrder order = Qt.AscendingOrder)'''


class KCategorizedView(QListView):
    """"""
    def __init__(self, parent = None):
        '''void KCategorizedView.__init__(QWidget parent = None)'''
    def block(self, category):
        '''list-of-QModelIndex KCategorizedView.block(QString category)'''
        return [QModelIndex()]
    def block(self, representative):
        '''list-of-QModelIndex KCategorizedView.block(QModelIndex representative)'''
        return [QModelIndex()]
    def rowsAboutToBeRemoved(self, parent, start, end):
        '''void KCategorizedView.rowsAboutToBeRemoved(QModelIndex parent, int start, int end)'''
    def dragEnterEvent(self, event):
        '''void KCategorizedView.dragEnterEvent(QDragEnterEvent event)'''
    def setCollapsibleBlocks(self, enable):
        '''void KCategorizedView.setCollapsibleBlocks(bool enable)'''
    def collapsibleBlocks(self):
        '''bool KCategorizedView.collapsibleBlocks()'''
        return bool()
    def setAlternatingBlockColors(self, enable):
        '''void KCategorizedView.setAlternatingBlockColors(bool enable)'''
    def alternatingBlockColors(self):
        '''bool KCategorizedView.alternatingBlockColors()'''
        return bool()
    def setCategorySpacing(self, categorySpacing):
        '''void KCategorizedView.setCategorySpacing(int categorySpacing)'''
    def categorySpacing(self):
        '''int KCategorizedView.categorySpacing()'''
        return int()
    def setGridSizeOwn(self, size):
        '''void KCategorizedView.setGridSizeOwn(QSize size)'''
    def dataChanged(self, topLeft, bottomRight):
        '''void KCategorizedView.dataChanged(QModelIndex topLeft, QModelIndex bottomRight)'''
    def currentChanged(self, current, previous):
        '''void KCategorizedView.currentChanged(QModelIndex current, QModelIndex previous)'''
    def slotLayoutChanged(self):
        '''void KCategorizedView.slotLayoutChanged()'''
    def updateGeometries(self):
        '''void KCategorizedView.updateGeometries()'''
    def rowsRemoved(self, parent, start, end):
        '''void KCategorizedView.rowsRemoved(QModelIndex parent, int start, int end)'''
    def rowsInsertedArtifficial(self, parent, start, end):
        '''void KCategorizedView.rowsInsertedArtifficial(QModelIndex parent, int start, int end)'''
    def rowsInserted(self, parent, start, end):
        '''void KCategorizedView.rowsInserted(QModelIndex parent, int start, int end)'''
    def moveCursor(self, cursorAction, modifiers):
        '''QModelIndex KCategorizedView.moveCursor(QAbstractItemView.CursorAction cursorAction, Qt.KeyboardModifiers modifiers)'''
        return QModelIndex()
    def dropEvent(self, event):
        '''void KCategorizedView.dropEvent(QDropEvent event)'''
    def dragLeaveEvent(self, event):
        '''void KCategorizedView.dragLeaveEvent(QDragLeaveEvent event)'''
    def dragMoveEvent(self, event):
        '''void KCategorizedView.dragMoveEvent(QDragMoveEvent event)'''
    def startDrag(self, supportedActions):
        '''void KCategorizedView.startDrag(Qt.DropActions supportedActions)'''
    def leaveEvent(self, event):
        '''void KCategorizedView.leaveEvent(QEvent event)'''
    def mouseReleaseEvent(self, event):
        '''void KCategorizedView.mouseReleaseEvent(QMouseEvent event)'''
    def mousePressEvent(self, event):
        '''void KCategorizedView.mousePressEvent(QMouseEvent event)'''
    def mouseMoveEvent(self, event):
        '''void KCategorizedView.mouseMoveEvent(QMouseEvent event)'''
    def setSelection(self, rect, flags):
        '''void KCategorizedView.setSelection(QRect rect, QItemSelectionModel.SelectionFlags flags)'''
    def resizeEvent(self, event):
        '''void KCategorizedView.resizeEvent(QResizeEvent event)'''
    def paintEvent(self, event):
        '''void KCategorizedView.paintEvent(QPaintEvent event)'''
    def reset(self):
        '''void KCategorizedView.reset()'''
    def indexAt(self, point):
        '''QModelIndex KCategorizedView.indexAt(QPoint point)'''
        return QModelIndex()
    def setCategoryDrawer(self, categoryDrawer):
        '''void KCategorizedView.setCategoryDrawer(KCategoryDrawer categoryDrawer)'''
    def categoryDrawer(self):
        '''KCategoryDrawer KCategorizedView.categoryDrawer()'''
        return KCategoryDrawer()
    def visualRect(self, index):
        '''QRect KCategorizedView.visualRect(QModelIndex index)'''
        return QRect()
    def setGridSize(self, size):
        '''void KCategorizedView.setGridSize(QSize size)'''
    def setModel(self, model):
        '''void KCategorizedView.setModel(QAbstractItemModel model)'''


class KCategoryDrawer():
    """"""
    def __init__(self):
        '''void KCategoryDrawer.__init__()'''
    def __init__(self):
        '''KCategoryDrawer KCategoryDrawer.__init__()'''
        return KCategoryDrawer()
    def setRightMargin(self, rightMargin):
        '''void KCategoryDrawer.setRightMargin(int rightMargin)'''
    def rightMargin(self):
        '''int KCategoryDrawer.rightMargin()'''
        return int()
    def setLeftMargin(self, leftMargin):
        '''void KCategoryDrawer.setLeftMargin(int leftMargin)'''
    def leftMargin(self):
        '''int KCategoryDrawer.leftMargin()'''
        return int()
    def categoryHeight(self, index, option):
        '''int KCategoryDrawer.categoryHeight(QModelIndex index, QStyleOption option)'''
        return int()
    def drawCategory(self, index, sortRole, option, painter):
        '''void KCategoryDrawer.drawCategory(QModelIndex index, int sortRole, QStyleOption option, QPainter painter)'''


class KCategoryDrawerV2(QObject, KCategoryDrawer):
    """"""
    def __init__(self, parent = None):
        '''void KCategoryDrawerV2.__init__(QObject parent = None)'''
    actionRequested = pyqtSignal() # void actionRequested(int,const QModelIndexamp;) - signal
    collapseOrExpandClicked = pyqtSignal() # void collapseOrExpandClicked(const QModelIndexamp;) - signal
    def mouseButtonDoubleClicked(self, index, event):
        '''void KCategoryDrawerV2.mouseButtonDoubleClicked(QModelIndex index, QMouseEvent event)'''
    def mouseButtonMoved(self, index, event):
        '''void KCategoryDrawerV2.mouseButtonMoved(QModelIndex index, QMouseEvent event)'''
    def mouseButtonReleased(self, index, event):
        '''void KCategoryDrawerV2.mouseButtonReleased(QModelIndex index, QMouseEvent event)'''
    def mouseButtonPressed(self, index, event):
        '''void KCategoryDrawerV2.mouseButtonPressed(QModelIndex index, QMouseEvent event)'''


class KCategoryDrawerV3(KCategoryDrawerV2):
    """"""
    def __init__(self, view):
        '''void KCategoryDrawerV3.__init__(KCategorizedView view)'''
    def mouseLeft(self, index, blockRect):
        '''void KCategoryDrawerV3.mouseLeft(QModelIndex index, QRect blockRect)'''
    def mouseButtonDoubleClicked(self, index, blockRect, event):
        '''void KCategoryDrawerV3.mouseButtonDoubleClicked(QModelIndex index, QRect blockRect, QMouseEvent event)'''
    def mouseMoved(self, index, blockRect, event):
        '''void KCategoryDrawerV3.mouseMoved(QModelIndex index, QRect blockRect, QMouseEvent event)'''
    def mouseButtonReleased(self, index, blockRect, event):
        '''void KCategoryDrawerV3.mouseButtonReleased(QModelIndex index, QRect blockRect, QMouseEvent event)'''
    def mouseButtonPressed(self, index, blockRect, event):
        '''void KCategoryDrawerV3.mouseButtonPressed(QModelIndex index, QRect blockRect, QMouseEvent event)'''
    def view(self):
        '''KCategorizedView KCategoryDrawerV3.view()'''
        return KCategorizedView()


class KCharSelect(QWidget):
    """"""
    # Enum KCharSelect.Control
    SearchLine = 0
    FontCombo = 0
    FontSize = 0
    BlockCombos = 0
    CharacterTable = 0
    DetailBrowser = 0
    HistoryButtons = 0
    AllGuiElements = 0

    def __init__(self, parent, controls = None):
        '''void KCharSelect.__init__(QWidget parent, KCharSelect.Controls controls = KCharSelect.AllGuiElements)'''
    def __init__(self, parent, collection, controls = None):
        '''void KCharSelect.__init__(QWidget parent, KActionCollection collection, KCharSelect.Controls controls = KCharSelect.AllGuiElements)'''
    charSelected = pyqtSignal() # void charSelected(const QCharamp;) - signal
    displayedCharsChanged = pyqtSignal() # void displayedCharsChanged() - signal
    currentCharChanged = pyqtSignal() # void currentCharChanged(const QCharamp;) - signal
    currentFontChanged = pyqtSignal() # void currentFontChanged(const QFontamp;) - signal
    def setCurrentFont(self, font):
        '''void KCharSelect.setCurrentFont(QFont font)'''
    def setCurrentChar(self, c):
        '''void KCharSelect.setCurrentChar(QChar c)'''
    def displayedChars(self):
        '''list-of-QChar KCharSelect.displayedChars()'''
        return [QChar()]
    def currentFont(self):
        '''QFont KCharSelect.currentFont()'''
        return QFont()
    def currentChar(self):
        '''QChar KCharSelect.currentChar()'''
        return QChar()
    def sizeHint(self):
        '''QSize KCharSelect.sizeHint()'''
        return QSize()
    class Controls():
        """"""
        def __init__(self):
            '''KCharSelect.Controls KCharSelect.Controls.__init__()'''
            return KCharSelect.Controls()
        def __init__(self):
            '''int KCharSelect.Controls.__init__()'''
            return int()
        def __init__(self):
            '''void KCharSelect.Controls.__init__()'''
        def __bool__(self):
            '''int KCharSelect.Controls.__bool__()'''
            return int()
        def __ne__(self, f):
            '''bool KCharSelect.Controls.__ne__(KCharSelect.Controls f)'''
            return bool()
        def __eq__(self, f):
            '''bool KCharSelect.Controls.__eq__(KCharSelect.Controls f)'''
            return bool()
        def __invert__(self):
            '''KCharSelect.Controls KCharSelect.Controls.__invert__()'''
            return KCharSelect.Controls()
        def __and__(self, mask):
            '''KCharSelect.Controls KCharSelect.Controls.__and__(int mask)'''
            return KCharSelect.Controls()
        def __xor__(self, f):
            '''KCharSelect.Controls KCharSelect.Controls.__xor__(KCharSelect.Controls f)'''
            return KCharSelect.Controls()
        def __xor__(self, f):
            '''KCharSelect.Controls KCharSelect.Controls.__xor__(int f)'''
            return KCharSelect.Controls()
        def __or__(self, f):
            '''KCharSelect.Controls KCharSelect.Controls.__or__(KCharSelect.Controls f)'''
            return KCharSelect.Controls()
        def __or__(self, f):
            '''KCharSelect.Controls KCharSelect.Controls.__or__(int f)'''
            return KCharSelect.Controls()
        def __int__(self):
            '''int KCharSelect.Controls.__int__()'''
            return int()
        def __ixor__(self, f):
            '''KCharSelect.Controls KCharSelect.Controls.__ixor__(KCharSelect.Controls f)'''
            return KCharSelect.Controls()
        def __ior__(self, f):
            '''KCharSelect.Controls KCharSelect.Controls.__ior__(KCharSelect.Controls f)'''
            return KCharSelect.Controls()
        def __iand__(self, mask):
            '''KCharSelect.Controls KCharSelect.Controls.__iand__(int mask)'''
            return KCharSelect.Controls()


class KIdentityProxyModel(QAbstractProxyModel):
    """"""
    def __init__(self, parent = None):
        '''void KIdentityProxyModel.__init__(QObject parent = None)'''
    def supportedDropActions(self):
        '''Qt.DropActions KIdentityProxyModel.supportedDropActions()'''
        return Qt.DropActions()
    def mimeData(self, indexes):
        '''QMimeData KIdentityProxyModel.mimeData(list-of-QModelIndex indexes)'''
        return QMimeData()
    def mimeTypes(self):
        '''QStringList KIdentityProxyModel.mimeTypes()'''
        return QStringList()
    def fetchMore(self, parent):
        '''void KIdentityProxyModel.fetchMore(QModelIndex parent)'''
    def canFetchMore(self, parent):
        '''bool KIdentityProxyModel.canFetchMore(QModelIndex parent)'''
        return bool()
    def resetInternalData(self):
        '''void KIdentityProxyModel.resetInternalData()'''
    def removeRows(self, row, count, parent = QModelIndex()):
        '''bool KIdentityProxyModel.removeRows(int row, int count, QModelIndex parent = QModelIndex())'''
        return bool()
    def removeColumns(self, column, count, parent = QModelIndex()):
        '''bool KIdentityProxyModel.removeColumns(int column, int count, QModelIndex parent = QModelIndex())'''
        return bool()
    def insertRows(self, row, count, parent = QModelIndex()):
        '''bool KIdentityProxyModel.insertRows(int row, int count, QModelIndex parent = QModelIndex())'''
        return bool()
    def insertColumns(self, column, count, parent = QModelIndex()):
        '''bool KIdentityProxyModel.insertColumns(int column, int count, QModelIndex parent = QModelIndex())'''
        return bool()
    def setSourceModel(self, sourceModel):
        '''void KIdentityProxyModel.setSourceModel(QAbstractItemModel sourceModel)'''
    def match(self, start, role, value, hits = 1, flags = None):
        '''list-of-QModelIndex KIdentityProxyModel.match(QModelIndex start, int role, QVariant value, int hits = 1, Qt.MatchFlags flags = Qt.MatchFlags(Qt.MatchStartsWith|Qt.MatchWrap))'''
        return [QModelIndex()]
    def mapSelectionToSource(self, selection):
        '''QItemSelection KIdentityProxyModel.mapSelectionToSource(QItemSelection selection)'''
        return QItemSelection()
    def mapSelectionFromSource(self, selection):
        '''QItemSelection KIdentityProxyModel.mapSelectionFromSource(QItemSelection selection)'''
        return QItemSelection()
    def dropMimeData(self, data, action, row, column, parent):
        '''bool KIdentityProxyModel.dropMimeData(QMimeData data, Qt.DropAction action, int row, int column, QModelIndex parent)'''
        return bool()
    def rowCount(self, parent = QModelIndex()):
        '''int KIdentityProxyModel.rowCount(QModelIndex parent = QModelIndex())'''
        return int()
    def parent(self, child):
        '''QModelIndex KIdentityProxyModel.parent(QModelIndex child)'''
        return QModelIndex()
    def mapToSource(self, proxyIndex):
        '''QModelIndex KIdentityProxyModel.mapToSource(QModelIndex proxyIndex)'''
        return QModelIndex()
    def mapFromSource(self, sourceIndex):
        '''QModelIndex KIdentityProxyModel.mapFromSource(QModelIndex sourceIndex)'''
        return QModelIndex()
    def index(self, row, column, parent = QModelIndex()):
        '''QModelIndex KIdentityProxyModel.index(int row, int column, QModelIndex parent = QModelIndex())'''
        return QModelIndex()
    def columnCount(self, parent = QModelIndex()):
        '''int KIdentityProxyModel.columnCount(QModelIndex parent = QModelIndex())'''
        return int()


class KCheckableProxyModel(KIdentityProxyModel):
    """"""
    def __init__(self, parent = None):
        '''void KCheckableProxyModel.__init__(QObject parent = None)'''
    def select(self, selection, command):
        '''bool KCheckableProxyModel.select(QItemSelection selection, QItemSelectionModel.SelectionFlags command)'''
        return bool()
    def setSourceModel(self, sourceModel):
        '''void KCheckableProxyModel.setSourceModel(QAbstractItemModel sourceModel)'''
    def setData(self, index, value, role = None):
        '''bool KCheckableProxyModel.setData(QModelIndex index, QVariant value, int role = Qt.EditRole)'''
        return bool()
    def data(self, index, role = None):
        '''QVariant KCheckableProxyModel.data(QModelIndex index, int role = Qt.DisplayRole)'''
        return QVariant()
    def flags(self, index):
        '''Qt.ItemFlags KCheckableProxyModel.flags(QModelIndex index)'''
        return Qt.ItemFlags()
    def selectionModel(self):
        '''QItemSelectionModel KCheckableProxyModel.selectionModel()'''
        return QItemSelectionModel()
    def setSelectionModel(self, itemSelectionModel):
        '''void KCheckableProxyModel.setSelectionModel(QItemSelectionModel itemSelectionModel)'''


class KCModule(QWidget):
    """"""
    # Enum KCModule.Button
    NoAdditionalButton = 0
    Help = 0
    Default = 0
    Apply = 0
    Export = 0

    def __init__(self, componentData, parent = None, args = QVariantList()):
        '''void KCModule.__init__(KComponentData componentData, QWidget parent = None, list-of-QVariant args = QVariantList())'''
    def setExportText(self):
        '''QString KCModule.setExportText()'''
        return QString()
    def exportText(self):
        '''QString KCModule.exportText()'''
        return QString()
    def authStatusChanged(self):
        '''int KCModule.authStatusChanged()'''
        return int()
    rootOnlyMessageChanged = pyqtSignal() # void rootOnlyMessageChanged(bool,QString) - signal
    def authAction(self):
        '''KAuth.Action KCModule.authAction()'''
        return KAuth.Action()
    def needsAuthorization(self):
        '''bool KCModule.needsAuthorization()'''
        return bool()
    def setNeedsAuthorization(self, needsAuth):
        '''void KCModule.setNeedsAuthorization(bool needsAuth)'''
    def unmanagedWidgetChangeState(self):
        '''bool KCModule.unmanagedWidgetChangeState()'''
        return bool()
    def managedWidgetChangeState(self):
        '''bool KCModule.managedWidgetChangeState()'''
        return bool()
    def setUseRootOnlyMessage(self, on):
        '''void KCModule.setUseRootOnlyMessage(bool on)'''
    def setRootOnlyMessage(self, message):
        '''void KCModule.setRootOnlyMessage(QString message)'''
    def setButtons(self, btn):
        '''void KCModule.setButtons(KCModule.Buttons btn)'''
    def widgetChanged(self):
        '''void KCModule.widgetChanged()'''
    quickHelpChanged = pyqtSignal() # void quickHelpChanged() - signal
    changed = pyqtSignal() # void changed(bool) - signal
    def changed(self):
        '''void KCModule.changed()'''
    def showEvent(self, ev):
        '''void KCModule.showEvent(QShowEvent ev)'''
    def setQuickHelp(self, help):
        '''void KCModule.setQuickHelp(QString help)'''
    def addConfig(self, config, widget):
        '''KConfigDialogManager KCModule.addConfig(KConfigSkeleton config, QWidget widget)'''
        return KConfigDialogManager()
    def addConfig(self, config, widget):
        '''KConfigDialogManager KCModule.addConfig(KCoreConfigSkeleton config, QWidget widget)'''
        return KConfigDialogManager()
    def defaults(self):
        '''void KCModule.defaults()'''
    def save(self):
        '''void KCModule.save()'''
    def load(self):
        '''void KCModule.load()'''
    def configs(self):
        '''list-of-KConfigDialogManager KCModule.configs()'''
        return [KConfigDialogManager()]
    def componentData(self):
        '''KComponentData KCModule.componentData()'''
        return KComponentData()
    def useRootOnlyMessage(self):
        '''bool KCModule.useRootOnlyMessage()'''
        return bool()
    def rootOnlyMessage(self):
        '''QString KCModule.rootOnlyMessage()'''
        return QString()
    def buttons(self):
        '''KCModule.Buttons KCModule.buttons()'''
        return KCModule.Buttons()
    def setAboutData(self, about):
        '''void KCModule.setAboutData(KAboutData about)'''
    def aboutData(self):
        '''KAboutData KCModule.aboutData()'''
        return KAboutData()
    def quickHelp(self):
        '''QString KCModule.quickHelp()'''
        return QString()
    class Buttons():
        """"""
        def __init__(self):
            '''KCModule.Buttons KCModule.Buttons.__init__()'''
            return KCModule.Buttons()
        def __init__(self):
            '''int KCModule.Buttons.__init__()'''
            return int()
        def __init__(self):
            '''void KCModule.Buttons.__init__()'''
        def __bool__(self):
            '''int KCModule.Buttons.__bool__()'''
            return int()
        def __ne__(self, f):
            '''bool KCModule.Buttons.__ne__(KCModule.Buttons f)'''
            return bool()
        def __eq__(self, f):
            '''bool KCModule.Buttons.__eq__(KCModule.Buttons f)'''
            return bool()
        def __invert__(self):
            '''KCModule.Buttons KCModule.Buttons.__invert__()'''
            return KCModule.Buttons()
        def __and__(self, mask):
            '''KCModule.Buttons KCModule.Buttons.__and__(int mask)'''
            return KCModule.Buttons()
        def __xor__(self, f):
            '''KCModule.Buttons KCModule.Buttons.__xor__(KCModule.Buttons f)'''
            return KCModule.Buttons()
        def __xor__(self, f):
            '''KCModule.Buttons KCModule.Buttons.__xor__(int f)'''
            return KCModule.Buttons()
        def __or__(self, f):
            '''KCModule.Buttons KCModule.Buttons.__or__(KCModule.Buttons f)'''
            return KCModule.Buttons()
        def __or__(self, f):
            '''KCModule.Buttons KCModule.Buttons.__or__(int f)'''
            return KCModule.Buttons()
        def __int__(self):
            '''int KCModule.Buttons.__int__()'''
            return int()
        def __ixor__(self, f):
            '''KCModule.Buttons KCModule.Buttons.__ixor__(KCModule.Buttons f)'''
            return KCModule.Buttons()
        def __ior__(self, f):
            '''KCModule.Buttons KCModule.Buttons.__ior__(KCModule.Buttons f)'''
            return KCModule.Buttons()
        def __iand__(self, mask):
            '''KCModule.Buttons KCModule.Buttons.__iand__(int mask)'''
            return KCModule.Buttons()


class KSelectAction(KAction):
    """"""
    # Enum KSelectAction.ToolBarMode
    MenuMode = 0
    ComboBoxMode = 0

    def __init__(self, parent):
        '''void KSelectAction.__init__(QObject parent)'''
    def __init__(self, text, parent):
        '''void KSelectAction.__init__(QString text, QObject parent)'''
    def __init__(self, icon, text, parent):
        '''void KSelectAction.__init__(KIcon icon, QString text, QObject parent)'''
    def event(self, event):
        '''bool KSelectAction.event(QEvent event)'''
        return bool()
    def eventFilter(self, watched, event):
        '''bool KSelectAction.eventFilter(QObject watched, QEvent event)'''
        return bool()
    def deleteWidget(self, widget):
        '''void KSelectAction.deleteWidget(QWidget widget)'''
    def createWidget(self, parent):
        '''QWidget KSelectAction.createWidget(QWidget parent)'''
        return QWidget()
    def slotToggled(self):
        '''bool KSelectAction.slotToggled()'''
        return bool()
    def actionTriggered(self, action):
        '''void KSelectAction.actionTriggered(QAction action)'''
    triggered = pyqtSignal() # void triggered(QAction *) - signal
    triggered = pyqtSignal() # void triggered(int) - signal
    triggered = pyqtSignal() # void triggered(const QStringamp;) - signal
    def changeItem(self, index, text):
        '''void KSelectAction.changeItem(int index, QString text)'''
    def menuAccelsEnabled(self):
        '''bool KSelectAction.menuAccelsEnabled()'''
        return bool()
    def setMenuAccelsEnabled(self, b):
        '''void KSelectAction.setMenuAccelsEnabled(bool b)'''
    def removeAllActions(self):
        '''void KSelectAction.removeAllActions()'''
    def clear(self):
        '''void KSelectAction.clear()'''
    def setMaxComboViewCount(self, n):
        '''void KSelectAction.setMaxComboViewCount(int n)'''
    def setComboWidth(self, width):
        '''void KSelectAction.setComboWidth(int width)'''
    def comboWidth(self):
        '''int KSelectAction.comboWidth()'''
        return int()
    def setEditable(self):
        '''bool KSelectAction.setEditable()'''
        return bool()
    def isEditable(self):
        '''bool KSelectAction.isEditable()'''
        return bool()
    def items(self):
        '''QStringList KSelectAction.items()'''
        return QStringList()
    def setItems(self, lst):
        '''void KSelectAction.setItems(QStringList lst)'''
    def removeAction(self, action):
        '''QAction KSelectAction.removeAction(QAction action)'''
        return QAction()
    def addAction(self, action):
        '''void KSelectAction.addAction(QAction action)'''
    def addAction(self, text):
        '''KAction KSelectAction.addAction(QString text)'''
        return KAction()
    def addAction(self, icon, text):
        '''KAction KSelectAction.addAction(KIcon icon, QString text)'''
        return KAction()
    def setCurrentItem(self, index):
        '''bool KSelectAction.setCurrentItem(int index)'''
        return bool()
    def setCurrentAction(self, action):
        '''bool KSelectAction.setCurrentAction(QAction action)'''
        return bool()
    def setCurrentAction(self, text, cs = None):
        '''bool KSelectAction.setCurrentAction(QString text, Qt.CaseSensitivity cs = Qt.CaseSensitive)'''
        return bool()
    def action(self, index):
        '''QAction KSelectAction.action(int index)'''
        return QAction()
    def action(self, text, cs = None):
        '''QAction KSelectAction.action(QString text, Qt.CaseSensitivity cs = Qt.CaseSensitive)'''
        return QAction()
    def actions(self):
        '''list-of-QAction KSelectAction.actions()'''
        return [QAction()]
    def currentText(self):
        '''QString KSelectAction.currentText()'''
        return QString()
    def currentItem(self):
        '''int KSelectAction.currentItem()'''
        return int()
    def currentAction(self):
        '''QAction KSelectAction.currentAction()'''
        return QAction()
    def selectableActionGroup(self):
        '''QActionGroup KSelectAction.selectableActionGroup()'''
        return QActionGroup()
    def setToolButtonPopupMode(self, mode):
        '''void KSelectAction.setToolButtonPopupMode(QToolButton.ToolButtonPopupMode mode)'''
    def toolButtonPopupMode(self):
        '''QToolButton.ToolButtonPopupMode KSelectAction.toolButtonPopupMode()'''
        return QToolButton.ToolButtonPopupMode()
    def setToolBarMode(self, mode):
        '''void KSelectAction.setToolBarMode(KSelectAction.ToolBarMode mode)'''
    def toolBarMode(self):
        '''KSelectAction.ToolBarMode KSelectAction.toolBarMode()'''
        return KSelectAction.ToolBarMode()


class KCodecAction(KSelectAction):
    """"""
    def __init__(self, parent, showAutoOptions = False):
        '''void KCodecAction.__init__(QObject parent, bool showAutoOptions = False)'''
    def __init__(self, text, parent, showAutoOptions = False):
        '''void KCodecAction.__init__(QString text, QObject parent, bool showAutoOptions = False)'''
    def __init__(self, icon, text, parent, showAutoOptions = False):
        '''void KCodecAction.__init__(KIcon icon, QString text, QObject parent, bool showAutoOptions = False)'''
    def actionTriggered(self):
        '''QAction KCodecAction.actionTriggered()'''
        return QAction()
    defaultItemTriggered = pyqtSignal() # void defaultItemTriggered() - signal
    triggered = pyqtSignal() # void triggered(QTextCodec *) - signal
    triggered = pyqtSignal() # void triggered(KEncodingDetector::AutoDetectScript) - signal
    def setCurrentAutoDetectScript(self):
        '''KEncodingDetector.AutoDetectScript KCodecAction.setCurrentAutoDetectScript()'''
        return KEncodingDetector.AutoDetectScript()
    def currentAutoDetectScript(self):
        '''KEncodingDetector.AutoDetectScript KCodecAction.currentAutoDetectScript()'''
        return KEncodingDetector.AutoDetectScript()
    def currentCodecMib(self):
        '''int KCodecAction.currentCodecMib()'''
        return int()
    def currentCodecName(self):
        '''QString KCodecAction.currentCodecName()'''
        return QString()
    def setCurrentCodec(self, codec):
        '''bool KCodecAction.setCurrentCodec(QTextCodec codec)'''
        return bool()
    def setCurrentCodec(self, codecName):
        '''bool KCodecAction.setCurrentCodec(QString codecName)'''
        return bool()
    def setCurrentCodec(self, mib):
        '''bool KCodecAction.setCurrentCodec(int mib)'''
        return bool()
    def currentCodec(self):
        '''QTextCodec KCodecAction.currentCodec()'''
        return QTextCodec()
    def codecForMib(self, mib):
        '''QTextCodec KCodecAction.codecForMib(int mib)'''
        return QTextCodec()
    def mibForName(self, codecName, ok):
        '''int KCodecAction.mibForName(QString codecName, bool ok)'''
        return int()


class KColorButton(QPushButton):
    """"""
    def __init__(self, parent = None):
        '''void KColorButton.__init__(QWidget parent = None)'''
    def __init__(self, c, parent = None):
        '''void KColorButton.__init__(QColor c, QWidget parent = None)'''
    def __init__(self, c, defaultColor, parent = None):
        '''void KColorButton.__init__(QColor c, QColor defaultColor, QWidget parent = None)'''
    def isAlphaChannelEnabled(self):
        '''bool KColorButton.isAlphaChannelEnabled()'''
        return bool()
    def setAlphaChannelEnabled(self, alpha):
        '''void KColorButton.setAlphaChannelEnabled(bool alpha)'''
    def keyPressEvent(self, e):
        '''void KColorButton.keyPressEvent(QKeyEvent e)'''
    def mouseMoveEvent(self, e):
        '''void KColorButton.mouseMoveEvent(QMouseEvent e)'''
    def mousePressEvent(self, e):
        '''void KColorButton.mousePressEvent(QMouseEvent e)'''
    def dropEvent(self):
        '''QDropEvent KColorButton.dropEvent()'''
        return QDropEvent()
    def dragEnterEvent(self):
        '''QDragEnterEvent KColorButton.dragEnterEvent()'''
        return QDragEnterEvent()
    def paintEvent(self, pe):
        '''void KColorButton.paintEvent(QPaintEvent pe)'''
    changed = pyqtSignal() # void changed(const QColoramp;) - signal
    def minimumSizeHint(self):
        '''QSize KColorButton.minimumSizeHint()'''
        return QSize()
    def sizeHint(self):
        '''QSize KColorButton.sizeHint()'''
        return QSize()
    def setDefaultColor(self, c):
        '''void KColorButton.setDefaultColor(QColor c)'''
    def defaultColor(self):
        '''QColor KColorButton.defaultColor()'''
        return QColor()
    def setColor(self, c):
        '''void KColorButton.setColor(QColor c)'''
    def color(self):
        '''QColor KColorButton.color()'''
        return QColor()


class KColorCollection():
    """"""
    # Enum KColorCollection.Editable
    Yes = 0
    No = 0
    Ask = 0

    def __init__(self, name = QString()):
        '''void KColorCollection.__init__(QString name = QString())'''
    def __init__(self):
        '''KColorCollection KColorCollection.__init__()'''
        return KColorCollection()
    def changeColor(self, index, newColor, newColorName = QString()):
        '''int KColorCollection.changeColor(int index, QColor newColor, QString newColorName = QString())'''
        return int()
    def changeColor(self, oldColor, newColor, newColorName = QString()):
        '''int KColorCollection.changeColor(QColor oldColor, QColor newColor, QString newColorName = QString())'''
        return int()
    def addColor(self, newColor, newColorName = QString()):
        '''int KColorCollection.addColor(QColor newColor, QString newColorName = QString())'''
        return int()
    def findColor(self, color):
        '''int KColorCollection.findColor(QColor color)'''
        return int()
    def color(self, index):
        '''QColor KColorCollection.color(int index)'''
        return QColor()
    def count(self):
        '''int KColorCollection.count()'''
        return int()
    def setEditable(self, editable):
        '''void KColorCollection.setEditable(KColorCollection.Editable editable)'''
    def editable(self):
        '''KColorCollection.Editable KColorCollection.editable()'''
        return KColorCollection.Editable()
    def setName(self, name):
        '''void KColorCollection.setName(QString name)'''
    def name(self):
        '''QString KColorCollection.name()'''
        return QString()
    def name(self, index):
        '''QString KColorCollection.name(int index)'''
        return QString()
    def name(self, color):
        '''QString KColorCollection.name(QColor color)'''
        return QString()
    def setDescription(self, desc):
        '''void KColorCollection.setDescription(QString desc)'''
    def description(self):
        '''QString KColorCollection.description()'''
        return QString()
    def save(self):
        '''bool KColorCollection.save()'''
        return bool()
    def installedCollections(self):
        '''static QStringList KColorCollection.installedCollections()'''
        return QStringList()


class KColorCombo(QComboBox):
    """"""
    def __init__(self, parent = None):
        '''void KColorCombo.__init__(QWidget parent = None)'''
    def paintEvent(self, event):
        '''void KColorCombo.paintEvent(QPaintEvent event)'''
    highlighted = pyqtSignal() # void highlighted(const QColoramp;) - signal
    activated = pyqtSignal() # void activated(const QColoramp;) - signal
    def showEmptyList(self):
        '''void KColorCombo.showEmptyList()'''
    def colors(self):
        '''list-of-QColor KColorCombo.colors()'''
        return [QColor()]
    def setColors(self, colors):
        '''void KColorCombo.setColors(list-of-QColor colors)'''
    def isCustomColor(self):
        '''bool KColorCombo.isCustomColor()'''
        return bool()
    def color(self):
        '''QColor KColorCombo.color()'''
        return QColor()
    def setColor(self, col):
        '''void KColorCombo.setColor(QColor col)'''


class KColorCells(QTableWidget):
    """"""
    def __init__(self, parent, rows, columns):
        '''void KColorCells.__init__(QWidget parent, int rows, int columns)'''
    def positionToCell(self, pos, ignoreBorders = False):
        '''int KColorCells.positionToCell(QPoint pos, bool ignoreBorders = False)'''
        return int()
    def mouseDoubleClickEvent(self):
        '''QMouseEvent KColorCells.mouseDoubleClickEvent()'''
        return QMouseEvent()
    def dropEvent(self):
        '''QDropEvent KColorCells.dropEvent()'''
        return QDropEvent()
    def dragMoveEvent(self):
        '''QDragMoveEvent KColorCells.dragMoveEvent()'''
        return QDragMoveEvent()
    def dragEnterEvent(self):
        '''QDragEnterEvent KColorCells.dragEnterEvent()'''
        return QDragEnterEvent()
    def mouseMoveEvent(self):
        '''QMouseEvent KColorCells.mouseMoveEvent()'''
        return QMouseEvent()
    def mousePressEvent(self):
        '''QMouseEvent KColorCells.mousePressEvent()'''
        return QMouseEvent()
    def mouseReleaseEvent(self):
        '''QMouseEvent KColorCells.mouseReleaseEvent()'''
        return QMouseEvent()
    def resizeEvent(self, event):
        '''void KColorCells.resizeEvent(QResizeEvent event)'''
    def sizeHintForRow(self, column):
        '''int KColorCells.sizeHintForRow(int column)'''
        return int()
    def sizeHintForColumn(self, column):
        '''int KColorCells.sizeHintForColumn(int column)'''
        return int()
    colorDoubleClicked = pyqtSignal() # void colorDoubleClicked(int,const QColoramp;) - signal
    colorSelected = pyqtSignal() # void colorSelected(int,const QColoramp;) - signal
    def selectedIndex(self):
        '''int KColorCells.selectedIndex()'''
        return int()
    def setSelected(self, index):
        '''void KColorCells.setSelected(int index)'''
    def setAcceptDrags(self, acceptDrags):
        '''void KColorCells.setAcceptDrags(bool acceptDrags)'''
    def setShading(self, shade):
        '''void KColorCells.setShading(bool shade)'''
    def count(self):
        '''int KColorCells.count()'''
        return int()
    def color(self, index):
        '''QColor KColorCells.color(int index)'''
        return QColor()
    def setColor(self, index, col):
        '''void KColorCells.setColor(int index, QColor col)'''


class KColorPatch(QFrame):
    """"""
    def __init__(self, parent):
        '''void KColorPatch.__init__(QWidget parent)'''
    def color(self):
        '''QColor KColorPatch.color()'''
        return QColor()
    def dropEvent(self):
        '''QDropEvent KColorPatch.dropEvent()'''
        return QDropEvent()
    def dragEnterEvent(self):
        '''QDragEnterEvent KColorPatch.dragEnterEvent()'''
        return QDragEnterEvent()
    def mouseMoveEvent(self):
        '''QMouseEvent KColorPatch.mouseMoveEvent()'''
        return QMouseEvent()
    def paintEvent(self, pe):
        '''void KColorPatch.paintEvent(QPaintEvent pe)'''
    colorChanged = pyqtSignal() # void colorChanged(const QColoramp;) - signal
    def setColor(self, col):
        '''void KColorPatch.setColor(QColor col)'''


class KColorDialog(KDialog):
    """"""
    def __init__(self, parent = None, modal = False):
        '''void KColorDialog.__init__(QWidget parent = None, bool modal = False)'''
    def isAlphaChannelEnabled(self):
        '''bool KColorDialog.isAlphaChannelEnabled()'''
        return bool()
    def setAlphaChannelEnabled(self, alpha):
        '''void KColorDialog.setAlphaChannelEnabled(bool alpha)'''
    def eventFilter(self, obj, ev):
        '''bool KColorDialog.eventFilter(QObject obj, QEvent ev)'''
        return bool()
    def keyPressEvent(self):
        '''QKeyEvent KColorDialog.keyPressEvent()'''
        return QKeyEvent()
    def mouseReleaseEvent(self):
        '''QMouseEvent KColorDialog.mouseReleaseEvent()'''
        return QMouseEvent()
    def mouseMoveEvent(self):
        '''QMouseEvent KColorDialog.mouseMoveEvent()'''
        return QMouseEvent()
    colorSelected = pyqtSignal() # void colorSelected(const QColoramp;) - signal
    def setColor(self, col):
        '''void KColorDialog.setColor(QColor col)'''
    def defaultColor(self):
        '''QColor KColorDialog.defaultColor()'''
        return QColor()
    def setDefaultColor(self, defaultCol):
        '''void KColorDialog.setDefaultColor(QColor defaultCol)'''
    def grabColor(self, p):
        '''static QColor KColorDialog.grabColor(QPoint p)'''
        return QColor()
    def getColor(self, theColor, parent = None):
        '''static int KColorDialog.getColor(QColor theColor, QWidget parent = None)'''
        return int()
    def getColor(self, theColor, defaultColor, parent = None):
        '''static int KColorDialog.getColor(QColor theColor, QColor defaultColor, QWidget parent = None)'''
        return int()
    def color(self):
        '''QColor KColorDialog.color()'''
        return QColor()


class KColorMimeData():
    """"""
    def createDrag(self, color, dragsource):
        '''static QDrag KColorMimeData.createDrag(QColor color, QWidget dragsource)'''
        return QDrag()
    def fromMimeData(self, mimeData):
        '''static QColor KColorMimeData.fromMimeData(QMimeData mimeData)'''
        return QColor()
    def canDecode(self, mimeData):
        '''static bool KColorMimeData.canDecode(QMimeData mimeData)'''
        return bool()
    def populateMimeData(self, mimeData, color):
        '''static void KColorMimeData.populateMimeData(QMimeData mimeData, QColor color)'''


class KColorScheme():
    """"""
    # Enum KColorScheme.ShadeRole
    LightShade = 0
    MidlightShade = 0
    MidShade = 0
    DarkShade = 0
    ShadowShade = 0

    # Enum KColorScheme.DecorationRole
    FocusColor = 0
    HoverColor = 0

    # Enum KColorScheme.ForegroundRole
    NormalText = 0
    InactiveText = 0
    ActiveText = 0
    LinkText = 0
    VisitedText = 0
    NegativeText = 0
    NeutralText = 0
    PositiveText = 0

    # Enum KColorScheme.BackgroundRole
    NormalBackground = 0
    AlternateBackground = 0
    ActiveBackground = 0
    LinkBackground = 0
    VisitedBackground = 0
    NegativeBackground = 0
    NeutralBackground = 0
    PositiveBackground = 0

    # Enum KColorScheme.ColorSet
    View = 0
    Window = 0
    Button = 0
    Selection = 0
    Tooltip = 0

    def __init__(self):
        '''KColorScheme KColorScheme.__init__()'''
        return KColorScheme()
    def __init__(self):
        '''KSharedConfigPtr KColorScheme.__init__()'''
        return KSharedConfigPtr()
    def adjustForeground(self, newRole = None, color = None, set = None):
        '''static KSharedConfigPtr KColorScheme.adjustForeground(KColorScheme.ForegroundRole newRole = KColorScheme.NormalText, QPalette.ColorRole color = QPalette.Text, KColorScheme.ColorSet set = KColorScheme.View)'''
        return KSharedConfigPtr()
    def adjustBackground(self, newRole = None, color = None, set = None):
        '''static KSharedConfigPtr KColorScheme.adjustBackground(KColorScheme.BackgroundRole newRole = KColorScheme.NormalBackground, QPalette.ColorRole color = QPalette.Base, KColorScheme.ColorSet set = KColorScheme.View)'''
        return KSharedConfigPtr()
    def shade(self):
        '''KColorScheme.ShadeRole KColorScheme.shade()'''
        return KColorScheme.ShadeRole()
    def shade(self):
        '''static KColorScheme.ShadeRole KColorScheme.shade()'''
        return KColorScheme.ShadeRole()
    def shade(self, contrast, chromaAdjust = 0):
        '''static KColorScheme.ShadeRole KColorScheme.shade(float contrast, float chromaAdjust = 0)'''
        return KColorScheme.ShadeRole()
    def decoration(self):
        '''KColorScheme.DecorationRole KColorScheme.decoration()'''
        return KColorScheme.DecorationRole()
    def foreground(self):
        '''KColorScheme.ForegroundRole KColorScheme.foreground()'''
        return KColorScheme.ForegroundRole()
    def background(self):
        '''KColorScheme.BackgroundRole KColorScheme.background()'''
        return KColorScheme.BackgroundRole()


class KStatefulBrush():
    """"""
    def __init__(self):
        '''void KStatefulBrush.__init__()'''
    def __init__(self):
        '''KSharedConfigPtr KStatefulBrush.__init__()'''
        return KSharedConfigPtr()
    def __init__(self):
        '''KSharedConfigPtr KStatefulBrush.__init__()'''
        return KSharedConfigPtr()
    def __init__(self):
        '''KSharedConfigPtr KStatefulBrush.__init__()'''
        return KSharedConfigPtr()
    def __init__(self):
        '''KSharedConfigPtr KStatefulBrush.__init__()'''
        return KSharedConfigPtr()
    def __init__(self, background):
        '''KSharedConfigPtr KStatefulBrush.__init__(QBrush background)'''
        return KSharedConfigPtr()
    def __init__(self):
        '''KStatefulBrush KStatefulBrush.__init__()'''
        return KStatefulBrush()
    def brush(self):
        '''QPalette.ColorGroup KStatefulBrush.brush()'''
        return QPalette.ColorGroup()
    def brush(self):
        '''QPalette KStatefulBrush.brush()'''
        return QPalette()
    def brush(self):
        '''QWidget KStatefulBrush.brush()'''
        return QWidget()


class KColorUtils():
    """"""
    def overlayColors(self, base, paint, comp = None):
        '''static QColor KColorUtils.overlayColors(QColor base, QColor paint, QPainter.CompositionMode comp = QPainter.CompositionMode_SourceOver)'''
        return QColor()
    def mix(self, c1, c2, bias = None):
        '''static QColor KColorUtils.mix(QColor c1, QColor c2, float bias = 0.5)'''
        return QColor()
    def tint(self, base, color, amount = None):
        '''static QColor KColorUtils.tint(QColor base, QColor color, float amount = 0.3)'''
        return QColor()
    def shade(self, lumaAmount, chromaAmount = 0):
        '''static QColor KColorUtils.shade(float lumaAmount, float chromaAmount = 0)'''
        return QColor()
    def darken(self, amount = None, chromaGain = 1):
        '''static QColor KColorUtils.darken(float amount = 0.5, float chromaGain = 1)'''
        return QColor()
    def lighten(self, amount = None, chromaInverseGain = 1):
        '''static QColor KColorUtils.lighten(float amount = 0.5, float chromaInverseGain = 1)'''
        return QColor()
    def contrastRatio(self):
        '''static QColor KColorUtils.contrastRatio()'''
        return QColor()
    def luma(self):
        '''static QColor KColorUtils.luma()'''
        return QColor()


class KSelector(QAbstractSlider):
    """"""
    def __init__(self, parent = None):
        '''void KSelector.__init__(QWidget parent = None)'''
    def __init__(self, o, parent = None):
        '''void KSelector.__init__(Qt.Orientation o, QWidget parent = None)'''
    def wheelEvent(self):
        '''QWheelEvent KSelector.wheelEvent()'''
        return QWheelEvent()
    def mouseReleaseEvent(self, e):
        '''void KSelector.mouseReleaseEvent(QMouseEvent e)'''
    def mouseMoveEvent(self, e):
        '''void KSelector.mouseMoveEvent(QMouseEvent e)'''
    def mousePressEvent(self, e):
        '''void KSelector.mousePressEvent(QMouseEvent e)'''
    def paintEvent(self):
        '''QPaintEvent KSelector.paintEvent()'''
        return QPaintEvent()
    def drawArrow(self, painter, pos):
        '''void KSelector.drawArrow(QPainter painter, QPoint pos)'''
    def drawContents(self):
        '''QPainter KSelector.drawContents()'''
        return QPainter()
    def arrowDirection(self):
        '''Qt.ArrowType KSelector.arrowDirection()'''
        return Qt.ArrowType()
    def setArrowDirection(self, direction):
        '''void KSelector.setArrowDirection(Qt.ArrowType direction)'''
    def indent(self):
        '''bool KSelector.indent()'''
        return bool()
    def setIndent(self, i):
        '''void KSelector.setIndent(bool i)'''
    def contentsRect(self):
        '''QRect KSelector.contentsRect()'''
        return QRect()


class KColorValueSelector(KSelector):
    """"""
    def __init__(self, parent = None):
        '''void KColorValueSelector.__init__(QWidget parent = None)'''
    def __init__(self, o, parent = None):
        '''void KColorValueSelector.__init__(Qt.Orientation o, QWidget parent = None)'''
    def drawContents(self, painter):
        '''void KColorValueSelector.drawContents(QPainter painter)'''
    def resizeEvent(self):
        '''QResizeEvent KColorValueSelector.resizeEvent()'''
        return QResizeEvent()
    def drawPalette(self, pixmap):
        '''void KColorValueSelector.drawPalette(QPixmap pixmap)'''
    def chooserMode(self):
        '''KColorChooserMode KColorValueSelector.chooserMode()'''
        return KColorChooserMode()
    def setChooserMode(self, chooserMode):
        '''void KColorValueSelector.setChooserMode(KColorChooserMode chooserMode)'''
    def setColorValue(self, colorValue):
        '''void KColorValueSelector.setColorValue(int colorValue)'''
    def colorValue(self):
        '''int KColorValueSelector.colorValue()'''
        return int()
    def setSaturation(self, saturation):
        '''void KColorValueSelector.setSaturation(int saturation)'''
    def saturation(self):
        '''int KColorValueSelector.saturation()'''
        return int()
    def setHue(self, hue):
        '''void KColorValueSelector.setHue(int hue)'''
    def hue(self):
        '''int KColorValueSelector.hue()'''
        return int()
    def updateContents(self):
        '''void KColorValueSelector.updateContents()'''


class KCompletionBase():
    """"""
    # Enum KCompletionBase.KeyBindingType
    TextCompletion = 0
    PrevCompletionMatch = 0
    NextCompletionMatch = 0
    SubstringCompletion = 0

    def __init__(self):
        '''void KCompletionBase.__init__()'''
    def delegate(self):
        '''KCompletionBase KCompletionBase.delegate()'''
        return KCompletionBase()
    def setDelegate(self, delegate):
        '''void KCompletionBase.setDelegate(KCompletionBase delegate)'''
    def getKeyBindings(self):
        '''unknown-type KCompletionBase.getKeyBindings()'''
        return unknown-type()
    def compObj(self):
        '''KCompletion KCompletionBase.compObj()'''
        return KCompletion()
    def setCompletedItems(self, items, autoSuggest = True):
        '''abstract void KCompletionBase.setCompletedItems(QStringList items, bool autoSuggest = True)'''
    def setCompletedText(self, text):
        '''abstract void KCompletionBase.setCompletedText(QString text)'''
    def useGlobalKeyBindings(self):
        '''void KCompletionBase.useGlobalKeyBindings()'''
    def getKeyBinding(self, item):
        '''KShortcut KCompletionBase.getKeyBinding(KCompletionBase.KeyBindingType item)'''
        return KShortcut()
    def setKeyBinding(self, item, key):
        '''bool KCompletionBase.setKeyBinding(KCompletionBase.KeyBindingType item, KShortcut key)'''
        return bool()
    def completionMode(self):
        '''KGlobalSettings.Completion KCompletionBase.completionMode()'''
        return KGlobalSettings.Completion()
    def setCompletionMode(self, mode):
        '''void KCompletionBase.setCompletionMode(KGlobalSettings.Completion mode)'''
    def emitSignals(self):
        '''bool KCompletionBase.emitSignals()'''
        return bool()
    def handleSignals(self):
        '''bool KCompletionBase.handleSignals()'''
        return bool()
    def setEnableSignals(self, enable):
        '''void KCompletionBase.setEnableSignals(bool enable)'''
    def setAutoDeleteCompletionObject(self, autoDelete):
        '''void KCompletionBase.setAutoDeleteCompletionObject(bool autoDelete)'''
    def isCompletionObjectAutoDeleted(self):
        '''bool KCompletionBase.isCompletionObjectAutoDeleted()'''
        return bool()
    def setHandleSignals(self, handle):
        '''void KCompletionBase.setHandleSignals(bool handle)'''
    def setCompletionObject(self, compObj, hsig = True):
        '''void KCompletionBase.setCompletionObject(KCompletion compObj, bool hsig = True)'''
    def completionObject(self, hsig = True):
        '''KCompletion KCompletionBase.completionObject(bool hsig = True)'''
        return KCompletion()


class KComboBox(QComboBox, KCompletionBase):
    """"""
    def __init__(self, parent = None):
        '''void KComboBox.__init__(QWidget parent = None)'''
    def __init__(self, rw, parent = None):
        '''void KComboBox.__init__(bool rw, QWidget parent = None)'''
    def minimumSizeHint(self):
        '''QSize KComboBox.minimumSizeHint()'''
        return QSize()
    def wheelEvent(self, ev):
        '''void KComboBox.wheelEvent(QWheelEvent ev)'''
    def create(self, initializeWindow = True, destroyOldWindow = True):
        '''int KComboBox.create(bool initializeWindow = True, bool destroyOldWindow = True)'''
        return int()
    def makeCompletion(self):
        '''QString KComboBox.makeCompletion()'''
        return QString()
    def setCurrentItem(self, item, insert = False, index = None):
        '''void KComboBox.setCurrentItem(QString item, bool insert = False, int index = -1)'''
    def setCompletedItems(self, items, autosubject = True):
        '''void KComboBox.setCompletedItems(QStringList items, bool autosubject = True)'''
    def setCompletedText(self):
        '''QString KComboBox.setCompletedText()'''
        return QString()
    def setCompletedText(self):
        '''bool KComboBox.setCompletedText()'''
        return bool()
    def rotateText(self, type):
        '''void KComboBox.rotateText(KCompletionBase.KeyBindingType type)'''
    aboutToShowContextMenu = pyqtSignal() # void aboutToShowContextMenu(QMenu *) - signal
    completionModeChanged = pyqtSignal() # void completionModeChanged(KGlobalSettings::Completion) - signal
    textRotation = pyqtSignal() # void textRotation(KCompletionBase::KeyBindingType) - signal
    substringCompletion = pyqtSignal() # void substringCompletion(const QStringamp;) - signal
    completion = pyqtSignal() # void completion(const QStringamp;) - signal
    returnPressed = pyqtSignal() # void returnPressed() - signal
    returnPressed = pyqtSignal() # void returnPressed(const QStringamp;) - signal
    def setEditable(self, editable):
        '''void KComboBox.setEditable(bool editable)'''
    def setLineEdit(self):
        '''QLineEdit KComboBox.setLineEdit()'''
        return QLineEdit()
    def completionBox(self, create = True):
        '''KCompletionBox KComboBox.completionBox(bool create = True)'''
        return KCompletionBox()
    def eventFilter(self):
        '''QEvent KComboBox.eventFilter()'''
        return QEvent()
    def trapReturnKey(self):
        '''bool KComboBox.trapReturnKey()'''
        return bool()
    def setTrapReturnKey(self, trap):
        '''void KComboBox.setTrapReturnKey(bool trap)'''
    def contains(self, text):
        '''bool KComboBox.contains(QString text)'''
        return bool()
    def urlDropsEnabled(self):
        '''bool KComboBox.urlDropsEnabled()'''
        return bool()
    def setUrlDropsEnabled(self, enable):
        '''void KComboBox.setUrlDropsEnabled(bool enable)'''
    def setContextMenuEnabled(self, showMenu):
        '''void KComboBox.setContextMenuEnabled(bool showMenu)'''
    def autoCompletion(self):
        '''bool KComboBox.autoCompletion()'''
        return bool()
    def setAutoCompletion(self, autocomplete):
        '''void KComboBox.setAutoCompletion(bool autocomplete)'''
    def cursorPosition(self):
        '''int KComboBox.cursorPosition()'''
        return int()
    def changeUrl(self, index, url):
        '''void KComboBox.changeUrl(int index, KUrl url)'''
    def changeUrl(self, index, icon, url):
        '''void KComboBox.changeUrl(int index, QIcon icon, KUrl url)'''
    def insertUrl(self, index, url):
        '''void KComboBox.insertUrl(int index, KUrl url)'''
    def insertUrl(self, index, icon, url):
        '''void KComboBox.insertUrl(int index, QIcon icon, KUrl url)'''
    def addUrl(self, url):
        '''void KComboBox.addUrl(KUrl url)'''
    def addUrl(self, icon, url):
        '''void KComboBox.addUrl(QIcon icon, KUrl url)'''
    def setEditUrl(self, url):
        '''void KComboBox.setEditUrl(KUrl url)'''
    def changeURL(self, url, index):
        '''void KComboBox.changeURL(KUrl url, int index)'''
    def changeURL(self, pixmap, url, index):
        '''void KComboBox.changeURL(QPixmap pixmap, KUrl url, int index)'''
    def insertURL(self, url, index = None):
        '''void KComboBox.insertURL(KUrl url, int index = -1)'''
    def insertURL(self, pixmap, url, index = None):
        '''void KComboBox.insertURL(QPixmap pixmap, KUrl url, int index = -1)'''


class KCompletion(QObject):
    """"""
    # Enum KCompletion.CompOrder
    Sorted = 0
    Insertion = 0
    Weighted = 0

    def __init__(self):
        '''void KCompletion.__init__()'''
    def postProcessMatches(self, pMatches):
        '''void KCompletion.postProcessMatches(QStringList pMatches)'''
    def postProcessMatch(self, pMatch):
        '''void KCompletion.postProcessMatch(QString pMatch)'''
    multipleMatches = pyqtSignal() # void multipleMatches() - signal
    matches = pyqtSignal() # void matches(const QStringListamp;) - signal
    match = pyqtSignal() # void match(const QStringamp;) - signal
    def clear(self):
        '''void KCompletion.clear()'''
    def removeItem(self, item):
        '''void KCompletion.removeItem(QString item)'''
    def addItem(self, item):
        '''void KCompletion.addItem(QString item)'''
    def addItem(self, item, weight):
        '''void KCompletion.addItem(QString item, int weight)'''
    def setItems(self, list):
        '''void KCompletion.setItems(QStringList list)'''
    def insertItems(self, items):
        '''void KCompletion.insertItems(QStringList items)'''
    def slotNextMatch(self):
        '''void KCompletion.slotNextMatch()'''
    def slotPreviousMatch(self):
        '''void KCompletion.slotPreviousMatch()'''
    def slotMakeCompletion(self, string):
        '''void KCompletion.slotMakeCompletion(QString string)'''
    def hasMultipleMatches(self):
        '''bool KCompletion.hasMultipleMatches()'''
        return bool()
    def soundsEnabled(self):
        '''bool KCompletion.soundsEnabled()'''
        return bool()
    def setSoundsEnabled(self, enable):
        '''void KCompletion.setSoundsEnabled(bool enable)'''
    def allMatches(self):
        '''QStringList KCompletion.allMatches()'''
        return QStringList()
    def allMatches(self, string):
        '''QStringList KCompletion.allMatches(QString string)'''
        return QStringList()
    def ignoreCase(self):
        '''bool KCompletion.ignoreCase()'''
        return bool()
    def setIgnoreCase(self, ignoreCase):
        '''void KCompletion.setIgnoreCase(bool ignoreCase)'''
    def order(self):
        '''KCompletion.CompOrder KCompletion.order()'''
        return KCompletion.CompOrder()
    def setOrder(self, order):
        '''void KCompletion.setOrder(KCompletion.CompOrder order)'''
    def completionMode(self):
        '''KGlobalSettings.Completion KCompletion.completionMode()'''
        return KGlobalSettings.Completion()
    def setCompletionMode(self, mode):
        '''void KCompletion.setCompletionMode(KGlobalSettings.Completion mode)'''
    def isEmpty(self):
        '''bool KCompletion.isEmpty()'''
        return bool()
    def items(self):
        '''QStringList KCompletion.items()'''
        return QStringList()
    def lastMatch(self):
        '''QString KCompletion.lastMatch()'''
        return QString()
    def nextMatch(self):
        '''QString KCompletion.nextMatch()'''
        return QString()
    def previousMatch(self):
        '''QString KCompletion.previousMatch()'''
        return QString()
    def substringCompletion(self, string):
        '''QStringList KCompletion.substringCompletion(QString string)'''
        return QStringList()
    def makeCompletion(self, string):
        '''QString KCompletion.makeCompletion(QString string)'''
        return QString()


class KListWidget(QListWidget):
    """"""
    def __init__(self, parent = None):
        '''void KListWidget.__init__(QWidget parent = None)'''
    def mouseDoubleClickEvent(self, e):
        '''void KListWidget.mouseDoubleClickEvent(QMouseEvent e)'''
    def mousePressEvent(self, e):
        '''void KListWidget.mousePressEvent(QMouseEvent e)'''
    def leaveEvent(self, e):
        '''void KListWidget.leaveEvent(QEvent e)'''
    def focusOutEvent(self, e):
        '''void KListWidget.focusOutEvent(QFocusEvent e)'''
    def keyPressEvent(self, e):
        '''void KListWidget.keyPressEvent(QKeyEvent e)'''
    doubleClicked = pyqtSignal() # void doubleClicked(QListWidgetItem *,const QPointamp;) - signal
    executed = pyqtSignal() # void executed(QListWidgetItem *) - signal
    executed = pyqtSignal() # void executed(QListWidgetItem *,const QPointamp;) - signal


class KCompletionBox(KListWidget):
    """"""
    def __init__(self, parent = None):
        '''void KCompletionBox.__init__(QWidget parent = None)'''
    def slotActivated(self):
        '''QListWidgetItem KCompletionBox.slotActivated()'''
        return QListWidgetItem()
    def globalPositionHint(self):
        '''QPoint KCompletionBox.globalPositionHint()'''
        return QPoint()
    def eventFilter(self):
        '''QEvent KCompletionBox.eventFilter()'''
        return QEvent()
    def sizeAndPosition(self):
        '''void KCompletionBox.sizeAndPosition()'''
    def calculateGeometry(self):
        '''QRect KCompletionBox.calculateGeometry()'''
        return QRect()
    userCancelled = pyqtSignal() # void userCancelled(const QStringamp;) - signal
    activated = pyqtSignal() # void activated(const QStringamp;) - signal
    def setVisible(self, visible):
        '''void KCompletionBox.setVisible(bool visible)'''
    def end(self):
        '''void KCompletionBox.end()'''
    def home(self):
        '''void KCompletionBox.home()'''
    def pageUp(self):
        '''void KCompletionBox.pageUp()'''
    def pageDown(self):
        '''void KCompletionBox.pageDown()'''
    def up(self):
        '''void KCompletionBox.up()'''
    def down(self):
        '''void KCompletionBox.down()'''
    def setActivateOnSelect(self, state):
        '''void KCompletionBox.setActivateOnSelect(bool state)'''
    def cancelledText(self):
        '''QString KCompletionBox.cancelledText()'''
        return QString()
    def setCancelledText(self, txt):
        '''void KCompletionBox.setCancelledText(QString txt)'''
    def isTabHandling(self):
        '''bool KCompletionBox.isTabHandling()'''
        return bool()
    def setTabHandling(self, enable):
        '''void KCompletionBox.setTabHandling(bool enable)'''
    def popup(self):
        '''void KCompletionBox.popup()'''
    def setItems(self, items):
        '''void KCompletionBox.setItems(QStringList items)'''
    def insertItems(self, items, index = None):
        '''void KCompletionBox.insertItems(QStringList items, int index = -1)'''
    def items(self):
        '''QStringList KCompletionBox.items()'''
        return QStringList()
    def activateOnSelect(self):
        '''bool KCompletionBox.activateOnSelect()'''
        return bool()
    def sizeHint(self):
        '''QSize KCompletionBox.sizeHint()'''
        return QSize()


class KConfigDialog(KPageDialog):
    """"""
    def __init__(self, parent, name, config):
        '''void KConfigDialog.__init__(QWidget parent, QString name, KConfigSkeleton config)'''
    def __init__(self, parent, name, config):
        '''void KConfigDialog.__init__(QWidget parent, QString name, KCoreConfigSkeleton config)'''
    def showEvent(self, e):
        '''void KConfigDialog.showEvent(QShowEvent e)'''
    def isDefault(self):
        '''bool KConfigDialog.isDefault()'''
        return bool()
    def hasChanged(self):
        '''bool KConfigDialog.hasChanged()'''
        return bool()
    def settingsChangedSlot(self):
        '''void KConfigDialog.settingsChangedSlot()'''
    def updateButtons(self):
        '''void KConfigDialog.updateButtons()'''
    def updateWidgetsDefault(self):
        '''void KConfigDialog.updateWidgetsDefault()'''
    def updateWidgets(self):
        '''void KConfigDialog.updateWidgets()'''
    def updateSettings(self):
        '''void KConfigDialog.updateSettings()'''
    def showDialog(self, name):
        '''static bool KConfigDialog.showDialog(QString name)'''
        return bool()
    def exists(self, name):
        '''static KConfigDialog KConfigDialog.exists(QString name)'''
        return KConfigDialog()
    def addPage(self, page, itemName, pixmapName = QString(), header = QString(), manage = True):
        '''KPageWidgetItem KConfigDialog.addPage(QWidget page, QString itemName, QString pixmapName = QString(), QString header = QString(), bool manage = True)'''
        return KPageWidgetItem()
    def addPage(self, page, config, itemName, pixmapName = QString(), header = QString()):
        '''KPageWidgetItem KConfigDialog.addPage(QWidget page, KConfigSkeleton config, QString itemName, QString pixmapName = QString(), QString header = QString())'''
        return KPageWidgetItem()
    settingsChanged = pyqtSignal() # void settingsChanged(const QStringamp;) - signal
    widgetModified = pyqtSignal() # void widgetModified() - signal


class KConfigDialogManager(QObject):
    """"""
    def __init__(self, parent, conf):
        '''void KConfigDialogManager.__init__(QWidget parent, KConfigSkeleton conf)'''
    def __init__(self, parent, conf):
        '''void KConfigDialogManager.__init__(QWidget parent, KCoreConfigSkeleton conf)'''
    def initMaps(self):
        '''static void KConfigDialogManager.initMaps()'''
    def setupWidget(self, widget, item):
        '''void KConfigDialogManager.setupWidget(QWidget widget, KConfigSkeletonItem item)'''
    def property(self, w):
        '''QVariant KConfigDialogManager.property(QWidget w)'''
        return QVariant()
    def setProperty(self, w, v):
        '''void KConfigDialogManager.setProperty(QWidget w, QVariant v)'''
    def getCustomProperty(self, widget):
        '''QByteArray KConfigDialogManager.getCustomProperty(QWidget widget)'''
        return QByteArray()
    def getUserProperty(self, widget):
        '''QByteArray KConfigDialogManager.getUserProperty(QWidget widget)'''
        return QByteArray()
    def parseChildren(self, widget, trackChanges):
        '''bool KConfigDialogManager.parseChildren(QWidget widget, bool trackChanges)'''
        return bool()
    def init(self, trackChanges):
        '''void KConfigDialogManager.init(bool trackChanges)'''
    def updateWidgetsDefault(self):
        '''void KConfigDialogManager.updateWidgetsDefault()'''
    def updateWidgets(self):
        '''void KConfigDialogManager.updateWidgets()'''
    def updateSettings(self):
        '''void KConfigDialogManager.updateSettings()'''
    def changedMap(self):
        '''static dict-of-QString-QByteArray KConfigDialogManager.changedMap()'''
        return dict-of-QString-QByteArray()
    def propertyMap(self):
        '''static dict-of-QString-QByteArray KConfigDialogManager.propertyMap()'''
        return dict-of-QString-QByteArray()
    def isDefault(self):
        '''bool KConfigDialogManager.isDefault()'''
        return bool()
    def hasChanged(self):
        '''bool KConfigDialogManager.hasChanged()'''
        return bool()
    def addWidget(self, widget):
        '''void KConfigDialogManager.addWidget(QWidget widget)'''
    widgetModified = pyqtSignal() # void widgetModified() - signal
    settingsChanged = pyqtSignal() # void settingsChanged() - signal
    settingsChanged = pyqtSignal() # void settingsChanged(QWidget *) - signal


class KConfigSkeleton(KCoreConfigSkeleton):
    """"""
    def __init__(self, configname = QString(), parent = None):
        '''void KConfigSkeleton.__init__(QString configname = QString(), QObject parent = None)'''
    def __init__(self, config, parent = None):
        '''void KConfigSkeleton.__init__(unknown-type config, QObject parent = None)'''
    def addItemFont(self, name, reference, defaultValue = QFont(), key = QString()):
        '''KConfigSkeleton.ItemFont KConfigSkeleton.addItemFont(QString name, QFont reference, QFont defaultValue = QFont(), QString key = QString())'''
        return KConfigSkeleton.ItemFont()
    def addItemColor(self, name, reference, defaultValue = None, key = QString()):
        '''KConfigSkeleton.ItemColor KConfigSkeleton.addItemColor(QString name, QColor reference, QColor defaultValue = QColor(128,128,128), QString key = QString())'''
        return KConfigSkeleton.ItemColor()
    class ItemColor(KConfigSkeletonItem):
        """"""
        def __init__(self, _group, _key, reference, defaultValue = None):
            '''void KConfigSkeleton.ItemColor.__init__(QString _group, QString _key, QColor reference, QColor defaultValue = QColor(128,128,128))'''
        def property(self):
            '''QVariant KConfigSkeleton.ItemColor.property()'''
            return QVariant()
        def isEqual(self, p):
            '''bool KConfigSkeleton.ItemColor.isEqual(QVariant p)'''
            return bool()
        def setProperty(self, p):
            '''void KConfigSkeleton.ItemColor.setProperty(QVariant p)'''
        def readConfig(self, config):
            '''void KConfigSkeleton.ItemColor.readConfig(KConfig config)'''
    class ItemFont(KConfigSkeletonItem):
        """"""
        def __init__(self, _group, _key, reference, defaultValue = QFont()):
            '''void KConfigSkeleton.ItemFont.__init__(QString _group, QString _key, QFont reference, QFont defaultValue = QFont())'''
        def property(self):
            '''QVariant KConfigSkeleton.ItemFont.property()'''
            return QVariant()
        def isEqual(self, p):
            '''bool KConfigSkeleton.ItemFont.isEqual(QVariant p)'''
            return bool()
        def setProperty(self, p):
            '''void KConfigSkeleton.ItemFont.setProperty(QVariant p)'''
        def readConfig(self, config):
            '''void KConfigSkeleton.ItemFont.readConfig(KConfig config)'''


class KCrash():
    """"""
    # Enum KCrash.CrashFlag
    KeepFDs = 0
    SaferDialog = 0
    AlwaysDirectly = 0
    AutoRestart = 0

    def isDrKonqiEnabled(self):
        '''static bool KCrash.isDrKonqiEnabled()'''
        return bool()
    def setDrKonqiEnabled(self, enabled):
        '''static void KCrash.setDrKonqiEnabled(bool enabled)'''
    def setApplicationName(self, name):
        '''static void KCrash.setApplicationName(QString name)'''
    def setApplicationPath(self, path):
        '''static void KCrash.setApplicationPath(QString path)'''
    def setFlags(self, flags):
        '''static void KCrash.setFlags(KCrash.CrashFlags flags)'''
    def defaultCrashHandler(self, signal):
        '''static void KCrash.defaultCrashHandler(int signal)'''
    class CrashFlags():
        """"""
        def __init__(self):
            '''KCrash.CrashFlags KCrash.CrashFlags.__init__()'''
            return KCrash.CrashFlags()
        def __init__(self):
            '''int KCrash.CrashFlags.__init__()'''
            return int()
        def __init__(self):
            '''void KCrash.CrashFlags.__init__()'''
        def __bool__(self):
            '''int KCrash.CrashFlags.__bool__()'''
            return int()
        def __ne__(self, f):
            '''bool KCrash.CrashFlags.__ne__(KCrash.CrashFlags f)'''
            return bool()
        def __eq__(self, f):
            '''bool KCrash.CrashFlags.__eq__(KCrash.CrashFlags f)'''
            return bool()
        def __invert__(self):
            '''KCrash.CrashFlags KCrash.CrashFlags.__invert__()'''
            return KCrash.CrashFlags()
        def __and__(self, mask):
            '''KCrash.CrashFlags KCrash.CrashFlags.__and__(int mask)'''
            return KCrash.CrashFlags()
        def __xor__(self, f):
            '''KCrash.CrashFlags KCrash.CrashFlags.__xor__(KCrash.CrashFlags f)'''
            return KCrash.CrashFlags()
        def __xor__(self, f):
            '''KCrash.CrashFlags KCrash.CrashFlags.__xor__(int f)'''
            return KCrash.CrashFlags()
        def __or__(self, f):
            '''KCrash.CrashFlags KCrash.CrashFlags.__or__(KCrash.CrashFlags f)'''
            return KCrash.CrashFlags()
        def __or__(self, f):
            '''KCrash.CrashFlags KCrash.CrashFlags.__or__(int f)'''
            return KCrash.CrashFlags()
        def __int__(self):
            '''int KCrash.CrashFlags.__int__()'''
            return int()
        def __ixor__(self, f):
            '''KCrash.CrashFlags KCrash.CrashFlags.__ixor__(KCrash.CrashFlags f)'''
            return KCrash.CrashFlags()
        def __ior__(self, f):
            '''KCrash.CrashFlags KCrash.CrashFlags.__ior__(KCrash.CrashFlags f)'''
            return KCrash.CrashFlags()
        def __iand__(self, mask):
            '''KCrash.CrashFlags KCrash.CrashFlags.__iand__(int mask)'''
            return KCrash.CrashFlags()


class KCursor(QCursor):
    """"""
    def __init__(self, name, fallback = None):
        '''void KCursor.__init__(QString name, Qt.CursorShape fallback = Qt.ArrowCursor)'''
    def __init__(self, cursor):
        '''void KCursor.__init__(QCursor cursor)'''
    def __init__(self):
        '''KCursor KCursor.__init__()'''
        return KCursor()
    def autoHideEventFilter(self):
        '''static QEvent KCursor.autoHideEventFilter()'''
        return QEvent()
    def hideCursorDelay(self):
        '''static int KCursor.hideCursorDelay()'''
        return int()
    def setHideCursorDelay(self, ms):
        '''static void KCursor.setHideCursorDelay(int ms)'''
    def setAutoHideCursor(self, w, enable, customEventFilter = False):
        '''static void KCursor.setAutoHideCursor(QWidget w, bool enable, bool customEventFilter = False)'''


class KDateComboBox(KComboBox):
    """"""
    # Enum KDateComboBox.Option
    EditDate = 0
    SelectDate = 0
    DatePicker = 0
    DateKeywords = 0
    WarnOnInvalid = 0

    def __init__(self, parent = None):
        '''void KDateComboBox.__init__(QWidget parent = None)'''
    def displayFormat(self):
        '''KLocale.DateFormat KDateComboBox.displayFormat()'''
        return KLocale.DateFormat()
    def isNull(self):
        '''bool KDateComboBox.isNull()'''
        return bool()
    def calendarSystem(self):
        '''KLocale.CalendarSystem KDateComboBox.calendarSystem()'''
        return KLocale.CalendarSystem()
    def dateMap(self):
        '''dict-of-QDate-QString KDateComboBox.dateMap()'''
        return dict-of-QDate-QString()
    def assignCalendarSystem(self, calendarSystem):
        '''void KDateComboBox.assignCalendarSystem(KLocale.CalendarSystem calendarSystem)'''
    def assignDate(self, date):
        '''void KDateComboBox.assignDate(QDate date)'''
    def resizeEvent(self, event):
        '''void KDateComboBox.resizeEvent(QResizeEvent event)'''
    def focusOutEvent(self, event):
        '''void KDateComboBox.focusOutEvent(QFocusEvent event)'''
    def focusInEvent(self, event):
        '''void KDateComboBox.focusInEvent(QFocusEvent event)'''
    def keyPressEvent(self, event):
        '''void KDateComboBox.keyPressEvent(QKeyEvent event)'''
    def wheelEvent(self, event):
        '''void KDateComboBox.wheelEvent(QWheelEvent event)'''
    def mousePressEvent(self, event):
        '''void KDateComboBox.mousePressEvent(QMouseEvent event)'''
    def hidePopup(self):
        '''void KDateComboBox.hidePopup()'''
    def showPopup(self):
        '''void KDateComboBox.showPopup()'''
    def eventFilter(self, object, event):
        '''bool KDateComboBox.eventFilter(QObject object, QEvent event)'''
        return bool()
    def setDateMap(self, dateMap):
        '''void KDateComboBox.setDateMap(dict-of-QDate-QString dateMap)'''
    def setMaximumDate(self, maxDate, maxWarnMsg = QString()):
        '''void KDateComboBox.setMaximumDate(QDate maxDate, QString maxWarnMsg = QString())'''
    def resetMinimumDate(self):
        '''void KDateComboBox.resetMinimumDate()'''
    def setMinimumDate(self, minTime, minWarnMsg = QString()):
        '''void KDateComboBox.setMinimumDate(QDate minTime, QString minWarnMsg = QString())'''
    def setDisplayFormat(self, format):
        '''void KDateComboBox.setDisplayFormat(KLocale.DateFormat format)'''
    def setOptions(self, options):
        '''void KDateComboBox.setOptions(KDateComboBox.Options options)'''
    def setCalendarSystem(self, calendarSystem):
        '''void KDateComboBox.setCalendarSystem(KLocale.CalendarSystem calendarSystem)'''
    def setDate(self, date):
        '''void KDateComboBox.setDate(QDate date)'''
    dateEdited = pyqtSignal() # void dateEdited(const QDateamp;) - signal
    dateChanged = pyqtSignal() # void dateChanged(const QDateamp;) - signal
    dateEntered = pyqtSignal() # void dateEntered(const QDateamp;) - signal
    def setCalendar(self, calendar = None):
        '''void KDateComboBox.setCalendar(KCalendarSystem calendar = None)'''
    def resetDateRange(self):
        '''void KDateComboBox.resetDateRange()'''
    def setDateRange(self, minDate, maxDate, minWarnMsg = QString(), maxWarnMsg = QString()):
        '''void KDateComboBox.setDateRange(QDate minDate, QDate maxDate, QString minWarnMsg = QString(), QString maxWarnMsg = QString())'''
    def resetMaximumDate(self):
        '''void KDateComboBox.resetMaximumDate()'''
    def maximumDate(self):
        '''QDate KDateComboBox.maximumDate()'''
        return QDate()
    def minimumDate(self):
        '''QDate KDateComboBox.minimumDate()'''
        return QDate()
    def options(self):
        '''KDateComboBox.Options KDateComboBox.options()'''
        return KDateComboBox.Options()
    def isValid(self):
        '''bool KDateComboBox.isValid()'''
        return bool()
    def calendar(self):
        '''KCalendarSystem KDateComboBox.calendar()'''
        return KCalendarSystem()
    def date(self):
        '''QDate KDateComboBox.date()'''
        return QDate()
    class Options():
        """"""
        def __init__(self):
            '''KDateComboBox.Options KDateComboBox.Options.__init__()'''
            return KDateComboBox.Options()
        def __init__(self):
            '''int KDateComboBox.Options.__init__()'''
            return int()
        def __init__(self):
            '''void KDateComboBox.Options.__init__()'''
        def __bool__(self):
            '''int KDateComboBox.Options.__bool__()'''
            return int()
        def __ne__(self, f):
            '''bool KDateComboBox.Options.__ne__(KDateComboBox.Options f)'''
            return bool()
        def __eq__(self, f):
            '''bool KDateComboBox.Options.__eq__(KDateComboBox.Options f)'''
            return bool()
        def __invert__(self):
            '''KDateComboBox.Options KDateComboBox.Options.__invert__()'''
            return KDateComboBox.Options()
        def __and__(self, mask):
            '''KDateComboBox.Options KDateComboBox.Options.__and__(int mask)'''
            return KDateComboBox.Options()
        def __xor__(self, f):
            '''KDateComboBox.Options KDateComboBox.Options.__xor__(KDateComboBox.Options f)'''
            return KDateComboBox.Options()
        def __xor__(self, f):
            '''KDateComboBox.Options KDateComboBox.Options.__xor__(int f)'''
            return KDateComboBox.Options()
        def __or__(self, f):
            '''KDateComboBox.Options KDateComboBox.Options.__or__(KDateComboBox.Options f)'''
            return KDateComboBox.Options()
        def __or__(self, f):
            '''KDateComboBox.Options KDateComboBox.Options.__or__(int f)'''
            return KDateComboBox.Options()
        def __int__(self):
            '''int KDateComboBox.Options.__int__()'''
            return int()
        def __ixor__(self, f):
            '''KDateComboBox.Options KDateComboBox.Options.__ixor__(KDateComboBox.Options f)'''
            return KDateComboBox.Options()
        def __ior__(self, f):
            '''KDateComboBox.Options KDateComboBox.Options.__ior__(KDateComboBox.Options f)'''
            return KDateComboBox.Options()
        def __iand__(self, mask):
            '''KDateComboBox.Options KDateComboBox.Options.__iand__(int mask)'''
            return KDateComboBox.Options()


class KDatePicker(QFrame):
    """"""
    def __init__(self, parent = None):
        '''void KDatePicker.__init__(QWidget parent = None)'''
    def __init__(self, dt, parent = None):
        '''void KDatePicker.__init__(QDate dt, QWidget parent = None)'''
    def setCalendarSystem(self, calendarSystem):
        '''bool KDatePicker.setCalendarSystem(KLocale.CalendarSystem calendarSystem)'''
        return bool()
    tableClicked = pyqtSignal() # void tableClicked() - signal
    dateEntered = pyqtSignal() # void dateEntered(const QDateamp;) - signal
    dateSelected = pyqtSignal() # void dateSelected(const QDateamp;) - signal
    dateChanged = pyqtSignal() # void dateChanged(const QDateamp;) - signal
    def weekSelected(self):
        '''int KDatePicker.weekSelected()'''
        return int()
    def todayButtonClicked(self):
        '''void KDatePicker.todayButtonClicked()'''
    def lineEnterPressed(self):
        '''void KDatePicker.lineEnterPressed()'''
    def uncheckYearSelector(self):
        '''void KDatePicker.uncheckYearSelector()'''
    def selectYearClicked(self):
        '''void KDatePicker.selectYearClicked()'''
    def selectMonthClicked(self):
        '''void KDatePicker.selectMonthClicked()'''
    def yearBackwardClicked(self):
        '''void KDatePicker.yearBackwardClicked()'''
    def yearForwardClicked(self):
        '''void KDatePicker.yearForwardClicked()'''
    def monthBackwardClicked(self):
        '''void KDatePicker.monthBackwardClicked()'''
    def monthForwardClicked(self):
        '''void KDatePicker.monthForwardClicked()'''
    def tableClickedSlot(self):
        '''void KDatePicker.tableClickedSlot()'''
    def dateChangedSlot(self, date):
        '''void KDatePicker.dateChangedSlot(QDate date)'''
    def resizeEvent(self):
        '''QResizeEvent KDatePicker.resizeEvent()'''
        return QResizeEvent()
    def eventFilter(self, o, e):
        '''bool KDatePicker.eventFilter(QObject o, QEvent e)'''
        return bool()
    def hasCloseButton(self):
        '''bool KDatePicker.hasCloseButton()'''
        return bool()
    def setCloseButton(self, enable):
        '''void KDatePicker.setCloseButton(bool enable)'''
    def fontSize(self):
        '''int KDatePicker.fontSize()'''
        return int()
    def setFontSize(self):
        '''int KDatePicker.setFontSize()'''
        return int()
    def dateTable(self):
        '''KDateTable KDatePicker.dateTable()'''
        return KDateTable()
    def setEnabled(self, enable):
        '''void KDatePicker.setEnabled(bool enable)'''
    def setCalendar(self, calendar = None):
        '''bool KDatePicker.setCalendar(KCalendarSystem calendar = None)'''
        return bool()
    def setCalendar(self, calendarType):
        '''bool KDatePicker.setCalendar(QString calendarType)'''
        return bool()
    def calendar(self):
        '''KCalendarSystem KDatePicker.calendar()'''
        return KCalendarSystem()
    def date(self):
        '''QDate KDatePicker.date()'''
        return QDate()
    def setDate(self, date):
        '''bool KDatePicker.setDate(QDate date)'''
        return bool()
    def sizeHint(self):
        '''QSize KDatePicker.sizeHint()'''
        return QSize()


class KPopupFrame(QFrame):
    """"""
    def __init__(self, parent = None):
        '''void KPopupFrame.__init__(QWidget parent = None)'''
    leaveModality = pyqtSignal() # void leaveModality() - signal
    def exec_(self, p):
        '''int KPopupFrame.exec_(QPoint p)'''
        return int()
    def exec_(self, x, y):
        '''int KPopupFrame.exec_(int x, int y)'''
        return int()
    def popup(self, pos):
        '''void KPopupFrame.popup(QPoint pos)'''
    def resizeEvent(self, resize):
        '''void KPopupFrame.resizeEvent(QResizeEvent resize)'''
    def setMainWidget(self, m):
        '''void KPopupFrame.setMainWidget(QWidget m)'''
    def close(self, r):
        '''void KPopupFrame.close(int r)'''
    def keyPressEvent(self, e):
        '''void KPopupFrame.keyPressEvent(QKeyEvent e)'''


class KDateValidator(QValidator):
    """"""
    def __init__(self, parent = None):
        '''void KDateValidator.__init__(QWidget parent = None)'''
    def date(self, text, date):
        '''QValidator.State KDateValidator.date(QString text, QDate date)'''
        return QValidator.State()
    def fixup(self, input):
        '''void KDateValidator.fixup(QString input)'''
    def validate(self, text, e):
        '''QValidator.State KDateValidator.validate(QString text, int e)'''
        return QValidator.State()


class KDateTable(QWidget):
    """"""
    # Enum KDateTable.BackgroundMode
    NoBgMode = 0
    RectangleMode = 0
    CircleMode = 0

    def __init__(self, parent = None):
        '''void KDateTable.__init__(QWidget parent = None)'''
    def __init__(self, parent = None):
        '''QDate KDateTable.__init__(QWidget parent = None)'''
        return QDate()
    def setCalendarSystem(self, calendarSystem):
        '''bool KDateTable.setCalendarSystem(KLocale.CalendarSystem calendarSystem)'''
        return bool()
    def event(self, e):
        '''bool KDateTable.event(QEvent e)'''
        return bool()
    aboutToShowContextMenu = pyqtSignal() # void aboutToShowContextMenu(KMenu *,const QDateamp;) - signal
    tableClicked = pyqtSignal() # void tableClicked() - signal
    dateChanged = pyqtSignal() # void dateChanged(const QDateamp;) - signal
    dateChanged = pyqtSignal() # void dateChanged(const QDateamp;,const QDateamp;) - signal
    def focusOutEvent(self, e):
        '''void KDateTable.focusOutEvent(QFocusEvent e)'''
    def focusInEvent(self, e):
        '''void KDateTable.focusInEvent(QFocusEvent e)'''
    def keyPressEvent(self, e):
        '''void KDateTable.keyPressEvent(QKeyEvent e)'''
    def wheelEvent(self, e):
        '''void KDateTable.wheelEvent(QWheelEvent e)'''
    def mousePressEvent(self, e):
        '''void KDateTable.mousePressEvent(QMouseEvent e)'''
    def paintEvent(self, e):
        '''void KDateTable.paintEvent(QPaintEvent e)'''
    def dateFromPos(self, pos):
        '''QDate KDateTable.dateFromPos(int pos)'''
        return QDate()
    def posFromDate(self, date):
        '''int KDateTable.posFromDate(QDate date)'''
        return int()
    def unsetCustomDatePainting(self, date):
        '''void KDateTable.unsetCustomDatePainting(QDate date)'''
    def setCustomDatePainting(self, date, fgColor, bgMode = None, bgColor = QColor()):
        '''void KDateTable.setCustomDatePainting(QDate date, QColor fgColor, KDateTable.BackgroundMode bgMode = KDateTable.NoBgMode, QColor bgColor = QColor())'''
    def popupMenuEnabled(self):
        '''bool KDateTable.popupMenuEnabled()'''
        return bool()
    def setPopupMenuEnabled(self, enable):
        '''void KDateTable.setPopupMenuEnabled(bool enable)'''
    def setCalendar(self, calendar = None):
        '''bool KDateTable.setCalendar(KCalendarSystem calendar = None)'''
        return bool()
    def setCalendar(self, calendarType):
        '''bool KDateTable.setCalendar(QString calendarType)'''
        return bool()
    def calendar(self):
        '''KCalendarSystem KDateTable.calendar()'''
        return KCalendarSystem()
    def date(self):
        '''QDate KDateTable.date()'''
        return QDate()
    def setDate(self, date):
        '''bool KDateTable.setDate(QDate date)'''
        return bool()
    def setFontSize(self, size):
        '''void KDateTable.setFontSize(int size)'''
    def sizeHint(self):
        '''QSize KDateTable.sizeHint()'''
        return QSize()


class KDateTimeEdit(QWidget):
    """"""
    # Enum KDateTimeEdit.Option
    ShowCalendar = 0
    ShowDate = 0
    ShowTime = 0
    ShowTimeSpec = 0
    EditDate = 0
    EditTime = 0
    SelectCalendar = 0
    SelectDate = 0
    SelectTime = 0
    SelectTimeSpec = 0
    DatePicker = 0
    DateKeywords = 0
    ForceTime = 0
    WarnOnInvalid = 0

    def __init__(self, parent = None):
        '''void KDateTimeEdit.__init__(QWidget parent = None)'''
    def isNullTime(self):
        '''bool KDateTimeEdit.isNullTime()'''
        return bool()
    def isNullDate(self):
        '''bool KDateTimeEdit.isNullDate()'''
        return bool()
    def isNull(self):
        '''bool KDateTimeEdit.isNull()'''
        return bool()
    def timeZones(self):
        '''dict-of-QString-KTimeZone KDateTimeEdit.timeZones()'''
        return dict-of-QString-KTimeZone()
    def timeDisplayFormat(self):
        '''KLocale.TimeFormatOptions KDateTimeEdit.timeDisplayFormat()'''
        return KLocale.TimeFormatOptions()
    def dateDisplayFormat(self):
        '''KLocale.DateFormat KDateTimeEdit.dateDisplayFormat()'''
        return KLocale.DateFormat()
    def calendarSystemsList(self):
        '''list-of-KLocale.CalendarSystem KDateTimeEdit.calendarSystemsList()'''
        return [KLocale.CalendarSystem()]
    def calendarSystem(self):
        '''KLocale.CalendarSystem KDateTimeEdit.calendarSystem()'''
        return KLocale.CalendarSystem()
    def setOptions(self, options):
        '''void KDateTimeEdit.setOptions(KDateTimeEdit.Options options)'''
    calendarChanged = pyqtSignal() # void calendarChanged(KLocale::CalendarSystem) - signal
    calendarEntered = pyqtSignal() # void calendarEntered(KLocale::CalendarSystem) - signal
    def setTimeListInterval(self, minutes):
        '''void KDateTimeEdit.setTimeListInterval(int minutes)'''
    def setCalendarSystemsList(self, calendars):
        '''void KDateTimeEdit.setCalendarSystemsList(list-of-KLocale.CalendarSystem calendars)'''
    def isValidTime(self):
        '''bool KDateTimeEdit.isValidTime()'''
        return bool()
    def isValidDate(self):
        '''bool KDateTimeEdit.isValidDate()'''
        return bool()
    def timeListInterval(self):
        '''int KDateTimeEdit.timeListInterval()'''
        return int()
    def assignTime(self, time):
        '''void KDateTimeEdit.assignTime(QTime time)'''
    def assignCalendarSystem(self, calendarSystem):
        '''void KDateTimeEdit.assignCalendarSystem(KLocale.CalendarSystem calendarSystem)'''
    def assignDate(self, date):
        '''void KDateTimeEdit.assignDate(QDate date)'''
    def assignDateTime(self, dateTime):
        '''void KDateTimeEdit.assignDateTime(KDateTime dateTime)'''
    def resizeEvent(self, event):
        '''void KDateTimeEdit.resizeEvent(QResizeEvent event)'''
    def focusOutEvent(self, event):
        '''void KDateTimeEdit.focusOutEvent(QFocusEvent event)'''
    def focusInEvent(self, event):
        '''void KDateTimeEdit.focusInEvent(QFocusEvent event)'''
    def eventFilter(self, object, event):
        '''bool KDateTimeEdit.eventFilter(QObject object, QEvent event)'''
        return bool()
    def setTimeList(self, timeList, minWarnMsg = QString(), maxWarnMsg = QString()):
        '''void KDateTimeEdit.setTimeList(list-of-QTime timeList, QString minWarnMsg = QString(), QString maxWarnMsg = QString())'''
    def setTimeDisplayFormat(self, formatOptions):
        '''void KDateTimeEdit.setTimeDisplayFormat(KLocale.TimeFormatOptions formatOptions)'''
    def setDateMap(self, dateMap):
        '''void KDateTimeEdit.setDateMap(dict-of-QDate-QString dateMap)'''
    def setDateDisplayFormat(self, format):
        '''void KDateTimeEdit.setDateDisplayFormat(KLocale.DateFormat format)'''
    def setMaximumDateTime(self, maxDateTime, maxWarnMsg = QString()):
        '''void KDateTimeEdit.setMaximumDateTime(KDateTime maxDateTime, QString maxWarnMsg = QString())'''
    def setMinimumDateTime(self, minDateTime, minWarnMsg = QString()):
        '''void KDateTimeEdit.setMinimumDateTime(KDateTime minDateTime, QString minWarnMsg = QString())'''
    def setDateTimeRange(self, minDateTime, maxDateTime, minWarnMsg = QString(), maxWarnMsg = QString()):
        '''void KDateTimeEdit.setDateTimeRange(KDateTime minDateTime, KDateTime maxDateTime, QString minWarnMsg = QString(), QString maxWarnMsg = QString())'''
    def setTimeSpec(self, spec):
        '''void KDateTimeEdit.setTimeSpec(KDateTime.Spec spec)'''
    def setTime(self, time):
        '''void KDateTimeEdit.setTime(QTime time)'''
    def setCalendarSystem(self, calendarSystem):
        '''void KDateTimeEdit.setCalendarSystem(KLocale.CalendarSystem calendarSystem)'''
    def setDate(self, date):
        '''void KDateTimeEdit.setDate(QDate date)'''
    def setDateTime(self, dateTime):
        '''void KDateTimeEdit.setDateTime(KDateTime dateTime)'''
    timeSpecChanged = pyqtSignal() # void timeSpecChanged(const KDateTime::Specamp;) - signal
    timeSpecEntered = pyqtSignal() # void timeSpecEntered(const KDateTime::Specamp;) - signal
    timeEdited = pyqtSignal() # void timeEdited(const QTimeamp;) - signal
    timeChanged = pyqtSignal() # void timeChanged(const QTimeamp;) - signal
    timeEntered = pyqtSignal() # void timeEntered(const QTimeamp;) - signal
    dateEdited = pyqtSignal() # void dateEdited(const QDateamp;) - signal
    dateChanged = pyqtSignal() # void dateChanged(const QDateamp;) - signal
    dateEntered = pyqtSignal() # void dateEntered(const QDateamp;) - signal
    dateTimeEdited = pyqtSignal() # void dateTimeEdited(const KDateTimeamp;) - signal
    dateTimeChanged = pyqtSignal() # void dateTimeChanged(const KDateTimeamp;) - signal
    dateTimeEntered = pyqtSignal() # void dateTimeEntered(const KDateTimeamp;) - signal
    def setTimeZones(self, zones):
        '''void KDateTimeEdit.setTimeZones(dict-of-QString-KTimeZone zones)'''
    def setCalendar(self, calendar = None):
        '''void KDateTimeEdit.setCalendar(KCalendarSystem calendar = None)'''
    def resetDateTimeRange(self):
        '''void KDateTimeEdit.resetDateTimeRange()'''
    def resetMaximumDateTime(self):
        '''void KDateTimeEdit.resetMaximumDateTime()'''
    def resetMinimumDateTime(self):
        '''void KDateTimeEdit.resetMinimumDateTime()'''
    def options(self):
        '''KDateTimeEdit.Options KDateTimeEdit.options()'''
        return KDateTimeEdit.Options()
    def isValid(self):
        '''bool KDateTimeEdit.isValid()'''
        return bool()
    def timeList(self):
        '''list-of-QTime KDateTimeEdit.timeList()'''
        return [QTime()]
    def dateMap(self):
        '''dict-of-QDate-QString KDateTimeEdit.dateMap()'''
        return dict-of-QDate-QString()
    def maximumDateTime(self):
        '''KDateTime KDateTimeEdit.maximumDateTime()'''
        return KDateTime()
    def minimumDateTime(self):
        '''KDateTime KDateTimeEdit.minimumDateTime()'''
        return KDateTime()
    def timeSpec(self):
        '''KDateTime.Spec KDateTimeEdit.timeSpec()'''
        return KDateTime.Spec()
    def time(self):
        '''QTime KDateTimeEdit.time()'''
        return QTime()
    def date(self):
        '''QDate KDateTimeEdit.date()'''
        return QDate()
    def dateTime(self):
        '''KDateTime KDateTimeEdit.dateTime()'''
        return KDateTime()
    class Options():
        """"""
        def __init__(self):
            '''KDateTimeEdit.Options KDateTimeEdit.Options.__init__()'''
            return KDateTimeEdit.Options()
        def __init__(self):
            '''int KDateTimeEdit.Options.__init__()'''
            return int()
        def __init__(self):
            '''void KDateTimeEdit.Options.__init__()'''
        def __bool__(self):
            '''int KDateTimeEdit.Options.__bool__()'''
            return int()
        def __ne__(self, f):
            '''bool KDateTimeEdit.Options.__ne__(KDateTimeEdit.Options f)'''
            return bool()
        def __eq__(self, f):
            '''bool KDateTimeEdit.Options.__eq__(KDateTimeEdit.Options f)'''
            return bool()
        def __invert__(self):
            '''KDateTimeEdit.Options KDateTimeEdit.Options.__invert__()'''
            return KDateTimeEdit.Options()
        def __and__(self, mask):
            '''KDateTimeEdit.Options KDateTimeEdit.Options.__and__(int mask)'''
            return KDateTimeEdit.Options()
        def __xor__(self, f):
            '''KDateTimeEdit.Options KDateTimeEdit.Options.__xor__(KDateTimeEdit.Options f)'''
            return KDateTimeEdit.Options()
        def __xor__(self, f):
            '''KDateTimeEdit.Options KDateTimeEdit.Options.__xor__(int f)'''
            return KDateTimeEdit.Options()
        def __or__(self, f):
            '''KDateTimeEdit.Options KDateTimeEdit.Options.__or__(KDateTimeEdit.Options f)'''
            return KDateTimeEdit.Options()
        def __or__(self, f):
            '''KDateTimeEdit.Options KDateTimeEdit.Options.__or__(int f)'''
            return KDateTimeEdit.Options()
        def __int__(self):
            '''int KDateTimeEdit.Options.__int__()'''
            return int()
        def __ixor__(self, f):
            '''KDateTimeEdit.Options KDateTimeEdit.Options.__ixor__(KDateTimeEdit.Options f)'''
            return KDateTimeEdit.Options()
        def __ior__(self, f):
            '''KDateTimeEdit.Options KDateTimeEdit.Options.__ior__(KDateTimeEdit.Options f)'''
            return KDateTimeEdit.Options()
        def __iand__(self, mask):
            '''KDateTimeEdit.Options KDateTimeEdit.Options.__iand__(int mask)'''
            return KDateTimeEdit.Options()


class KDateTimeWidget(QWidget):
    """"""
    def __init__(self, parent = None):
        '''void KDateTimeWidget.__init__(QWidget parent = None)'''
    def __init__(self, datetime, parent = None):
        '''void KDateTimeWidget.__init__(QDateTime datetime, QWidget parent = None)'''
    valueChanged = pyqtSignal() # void valueChanged(const QDateTimeamp;) - signal
    def setDateTime(self, datetime):
        '''void KDateTimeWidget.setDateTime(QDateTime datetime)'''
    def dateTime(self):
        '''QDateTime KDateTimeWidget.dateTime()'''
        return QDateTime()


class KDateWidget(QWidget):
    """"""
    def __init__(self, parent = None):
        '''void KDateWidget.__init__(QWidget parent = None)'''
    def __init__(self, date, parent = None):
        '''void KDateWidget.__init__(QDate date, QWidget parent = None)'''
    def setCalendarSystem(self, calendarSystem):
        '''bool KDateWidget.setCalendarSystem(KLocale.CalendarSystem calendarSystem)'''
        return bool()
    def slotDateChanged(self):
        '''void KDateWidget.slotDateChanged()'''
    def init(self, date):
        '''void KDateWidget.init(QDate date)'''
    changed = pyqtSignal() # void changed(const QDateamp;) - signal
    def setCalendar(self, calendar = None):
        '''bool KDateWidget.setCalendar(KCalendarSystem calendar = None)'''
        return bool()
    def setCalendar(self, calendarType):
        '''bool KDateWidget.setCalendar(QString calendarType)'''
        return bool()
    def calendar(self):
        '''KCalendarSystem KDateWidget.calendar()'''
        return KCalendarSystem()
    def setDate(self, date):
        '''bool KDateWidget.setDate(QDate date)'''
        return bool()
    def date(self):
        '''QDate KDateWidget.date()'''
        return QDate()


class KdePrint():
    """"""
    # Enum KdePrint.PageSelectPolicy
    ApplicationSelectsPages = 0
    SystemSelectsPages = 0

    def createPrintDialog(self, printer, customTabs, parent = None):
        '''static QPrintDialog KdePrint.createPrintDialog(QPrinter printer, list-of-QWidget customTabs, QWidget parent = None)'''
        return QPrintDialog()
    def createPrintDialog(self, printer, parent = None):
        '''static QPrintDialog KdePrint.createPrintDialog(QPrinter printer, QWidget parent = None)'''
        return QPrintDialog()
    def createPrintDialog(self, printer, pageSelectPolicy, customTabs, parent = None):
        '''static QPrintDialog KdePrint.createPrintDialog(QPrinter printer, KdePrint.PageSelectPolicy pageSelectPolicy, list-of-QWidget customTabs, QWidget parent = None)'''
        return QPrintDialog()
    def createPrintDialog(self, printer, pageSelectPolicy, parent = None):
        '''static QPrintDialog KdePrint.createPrintDialog(QPrinter printer, KdePrint.PageSelectPolicy pageSelectPolicy, QWidget parent = None)'''
        return QPrintDialog()


class KDescendantsProxyModel(QAbstractProxyModel):
    """"""
    def __init__(self, parent = None):
        '''void KDescendantsProxyModel.__init__(QObject parent = None)'''
    def match(self, start, role, value, hits = 1, flags = None):
        '''list-of-QModelIndex KDescendantsProxyModel.match(QModelIndex start, int role, QVariant value, int hits = 1, Qt.MatchFlags flags = Qt.MatchFlags(Qt.MatchStartsWith|Qt.MatchWrap))'''
        return [QModelIndex()]
    def supportedDropActions(self):
        '''Qt.DropActions KDescendantsProxyModel.supportedDropActions()'''
        return Qt.DropActions()
    def columnCount(self, index = QModelIndex()):
        '''int KDescendantsProxyModel.columnCount(QModelIndex index = QModelIndex())'''
        return int()
    def parent(self):
        '''QModelIndex KDescendantsProxyModel.parent()'''
        return QModelIndex()
    def index(self, parent = QModelIndex()):
        '''int KDescendantsProxyModel.index(QModelIndex parent = QModelIndex())'''
        return int()
    def hasChildren(self, parent = QModelIndex()):
        '''bool KDescendantsProxyModel.hasChildren(QModelIndex parent = QModelIndex())'''
        return bool()
    def mimeTypes(self):
        '''QStringList KDescendantsProxyModel.mimeTypes()'''
        return QStringList()
    def mimeData(self, indexes):
        '''QMimeData KDescendantsProxyModel.mimeData(list-of-QModelIndex indexes)'''
        return QMimeData()
    def headerData(self, section, orientation, role):
        '''QVariant KDescendantsProxyModel.headerData(int section, Qt.Orientation orientation, int role)'''
        return QVariant()
    def rowCount(self, parent = QModelIndex()):
        '''int KDescendantsProxyModel.rowCount(QModelIndex parent = QModelIndex())'''
        return int()
    def data(self, index, role = None):
        '''QVariant KDescendantsProxyModel.data(QModelIndex index, int role = Qt.DisplayRole)'''
        return QVariant()
    def flags(self, index):
        '''Qt.ItemFlags KDescendantsProxyModel.flags(QModelIndex index)'''
        return Qt.ItemFlags()
    def mapToSource(self, proxyIndex):
        '''QModelIndex KDescendantsProxyModel.mapToSource(QModelIndex proxyIndex)'''
        return QModelIndex()
    def mapFromSource(self, sourceIndex):
        '''QModelIndex KDescendantsProxyModel.mapFromSource(QModelIndex sourceIndex)'''
        return QModelIndex()
    def ancestorSeparator(self):
        '''QString KDescendantsProxyModel.ancestorSeparator()'''
        return QString()
    def setAncestorSeparator(self, separator):
        '''void KDescendantsProxyModel.setAncestorSeparator(QString separator)'''
    def displayAncestorData(self):
        '''bool KDescendantsProxyModel.displayAncestorData()'''
        return bool()
    def setDisplayAncestorData(self, display):
        '''void KDescendantsProxyModel.setDisplayAncestorData(bool display)'''
    def setRootIndex(self, index):
        '''void KDescendantsProxyModel.setRootIndex(QModelIndex index)'''
    def setSourceModel(self, model):
        '''void KDescendantsProxyModel.setSourceModel(QAbstractItemModel model)'''


class KDialogButtonBox(QDialogButtonBox):
    """"""
    def __init__(self, parent, _orientation = None):
        '''void KDialogButtonBox.__init__(QWidget parent, Qt.Orientation _orientation = Qt.Horizontal)'''
    def addButton(self, text, role):
        '''SLOT() KDialogButtonBox.addButton(QString text, QDialogButtonBox.ButtonRole role)'''
        return SLOT()()
    def addButton(self, text, role):
        '''callable KDialogButtonBox.addButton(QString text, QDialogButtonBox.ButtonRole role)'''
        return callable()
    def addButton(self, guiitem, role):
        '''SLOT() KDialogButtonBox.addButton(KGuiItem guiitem, QDialogButtonBox.ButtonRole role)'''
        return SLOT()()
    def addButton(self, guiitem, role):
        '''callable KDialogButtonBox.addButton(KGuiItem guiitem, QDialogButtonBox.ButtonRole role)'''
        return callable()


class KDialogJobUiDelegate(KJobUiDelegate):
    """"""
    def __init__(self):
        '''void KDialogJobUiDelegate.__init__()'''
    def slotWarning(self, job, plain, rich):
        '''void KDialogJobUiDelegate.slotWarning(KJob job, QString plain, QString rich)'''
    def showErrorMessage(self):
        '''void KDialogJobUiDelegate.showErrorMessage()'''
    def userTimestamp(self):
        '''int KDialogJobUiDelegate.userTimestamp()'''
        return int()
    def updateUserTimestamp(self, time):
        '''void KDialogJobUiDelegate.updateUserTimestamp(int time)'''
    def window(self):
        '''QWidget KDialogJobUiDelegate.window()'''
        return QWidget()
    def setWindow(self, window):
        '''void KDialogJobUiDelegate.setWindow(QWidget window)'''


class KDualAction(KAction):
    """"""
    def __init__(self, parent):
        '''void KDualAction.__init__(QObject parent)'''
    def __init__(self, inactiveText, activeText, parent):
        '''void KDualAction.__init__(QString inactiveText, QString activeText, QObject parent)'''
    activeChangedByUser = pyqtSignal() # void activeChangedByUser(bool) - signal
    activeChanged = pyqtSignal() # void activeChanged(bool) - signal
    def setActive(self, state):
        '''void KDualAction.setActive(bool state)'''
    def autoToggle(self):
        '''bool KDualAction.autoToggle()'''
        return bool()
    def setAutoToggle(self):
        '''bool KDualAction.setAutoToggle()'''
        return bool()
    def isActive(self):
        '''bool KDualAction.isActive()'''
        return bool()
    def setIconForStates(self, icon):
        '''void KDualAction.setIconForStates(QIcon icon)'''
    def inactiveToolTip(self):
        '''QString KDualAction.inactiveToolTip()'''
        return QString()
    def setInactiveToolTip(self):
        '''QString KDualAction.setInactiveToolTip()'''
        return QString()
    def activeToolTip(self):
        '''QString KDualAction.activeToolTip()'''
        return QString()
    def setActiveToolTip(self):
        '''QString KDualAction.setActiveToolTip()'''
        return QString()
    def inactiveText(self):
        '''QString KDualAction.inactiveText()'''
        return QString()
    def setInactiveText(self):
        '''QString KDualAction.setInactiveText()'''
        return QString()
    def activeText(self):
        '''QString KDualAction.activeText()'''
        return QString()
    def setActiveText(self):
        '''QString KDualAction.setActiveText()'''
        return QString()
    def inactiveIcon(self):
        '''QIcon KDualAction.inactiveIcon()'''
        return QIcon()
    def setInactiveIcon(self):
        '''QIcon KDualAction.setInactiveIcon()'''
        return QIcon()
    def activeIcon(self):
        '''QIcon KDualAction.activeIcon()'''
        return QIcon()
    def setActiveIcon(self):
        '''QIcon KDualAction.setActiveIcon()'''
        return QIcon()
    def inactiveGuiItem(self):
        '''KGuiItem KDualAction.inactiveGuiItem()'''
        return KGuiItem()
    def setInactiveGuiItem(self):
        '''KGuiItem KDualAction.setInactiveGuiItem()'''
        return KGuiItem()
    def activeGuiItem(self):
        '''KGuiItem KDualAction.activeGuiItem()'''
        return KGuiItem()
    def setActiveGuiItem(self):
        '''KGuiItem KDualAction.setActiveGuiItem()'''
        return KGuiItem()


class KEditListBox(QGroupBox):
    """"""
    # Enum KEditListBox.Button
    Add = 0
    Remove = 0
    UpDown = 0
    All = 0

    def __init__(self, parent = None):
        '''void KEditListBox.__init__(QWidget parent = None)'''
    def __init__(self, title, parent = None):
        '''void KEditListBox.__init__(QString title, QWidget parent = None)'''
    def __init__(self, parent, name, checkAtEntering = False, buttons = None):
        '''void KEditListBox.__init__(QWidget parent, str name, bool checkAtEntering = False, KEditListBox.Buttons buttons = KEditListBox.All)'''
    def __init__(self, title, parent, name, checkAtEntering = False, buttons = None):
        '''void KEditListBox.__init__(QString title, QWidget parent, str name, bool checkAtEntering = False, KEditListBox.Buttons buttons = KEditListBox.All)'''
    def __init__(self, title, customEditor, parent = None, name = None, checkAtEntering = False, buttons = None):
        '''void KEditListBox.__init__(QString title, KEditListBox.CustomEditor customEditor, QWidget parent = None, str name = None, bool checkAtEntering = False, KEditListBox.Buttons buttons = KEditListBox.All)'''
    def typedSomething(self, text):
        '''void KEditListBox.typedSomething(QString text)'''
    def enableMoveButtons(self):
        '''QModelIndex KEditListBox.enableMoveButtons()'''
        return QModelIndex()
    def removeItem(self):
        '''void KEditListBox.removeItem()'''
    def addItem(self):
        '''void KEditListBox.addItem()'''
    def moveItemDown(self):
        '''void KEditListBox.moveItemDown()'''
    def moveItemUp(self):
        '''void KEditListBox.moveItemUp()'''
    removed = pyqtSignal() # void removed(const QStringamp;) - signal
    added = pyqtSignal() # void added(const QStringamp;) - signal
    changed = pyqtSignal() # void changed() - signal
    def eventFilter(self, o, e):
        '''bool KEditListBox.eventFilter(QObject o, QEvent e)'''
        return bool()
    def setCustomEditor(self, editor):
        '''void KEditListBox.setCustomEditor(KEditListBox.CustomEditor editor)'''
    def checkAtEntering(self):
        '''bool KEditListBox.checkAtEntering()'''
        return bool()
    def setCheckAtEntering(self, check):
        '''void KEditListBox.setCheckAtEntering(bool check)'''
    def setButtons(self, buttons):
        '''void KEditListBox.setButtons(KEditListBox.Buttons buttons)'''
    def buttons(self):
        '''KEditListBox.Buttons KEditListBox.buttons()'''
        return KEditListBox.Buttons()
    def setItems(self, items):
        '''void KEditListBox.setItems(QStringList items)'''
    def items(self):
        '''QStringList KEditListBox.items()'''
        return QStringList()
    def currentText(self):
        '''QString KEditListBox.currentText()'''
        return QString()
    def currentItem(self):
        '''int KEditListBox.currentItem()'''
        return int()
    def text(self, index):
        '''QString KEditListBox.text(int index)'''
        return QString()
    def clear(self):
        '''void KEditListBox.clear()'''
    def insertItem(self, text, index = None):
        '''void KEditListBox.insertItem(QString text, int index = -1)'''
    def insertStringList(self, list, index = None):
        '''void KEditListBox.insertStringList(QStringList list, int index = -1)'''
    def count(self):
        '''int KEditListBox.count()'''
        return int()
    def downButton(self):
        '''QPushButton KEditListBox.downButton()'''
        return QPushButton()
    def upButton(self):
        '''QPushButton KEditListBox.upButton()'''
        return QPushButton()
    def removeButton(self):
        '''QPushButton KEditListBox.removeButton()'''
        return QPushButton()
    def addButton(self):
        '''QPushButton KEditListBox.addButton()'''
        return QPushButton()
    def lineEdit(self):
        '''KLineEdit KEditListBox.lineEdit()'''
        return KLineEdit()
    def listView(self):
        '''QListView KEditListBox.listView()'''
        return QListView()
    class Buttons():
        """"""
        def __init__(self):
            '''KEditListBox.Buttons KEditListBox.Buttons.__init__()'''
            return KEditListBox.Buttons()
        def __init__(self):
            '''int KEditListBox.Buttons.__init__()'''
            return int()
        def __init__(self):
            '''void KEditListBox.Buttons.__init__()'''
        def __bool__(self):
            '''int KEditListBox.Buttons.__bool__()'''
            return int()
        def __ne__(self, f):
            '''bool KEditListBox.Buttons.__ne__(KEditListBox.Buttons f)'''
            return bool()
        def __eq__(self, f):
            '''bool KEditListBox.Buttons.__eq__(KEditListBox.Buttons f)'''
            return bool()
        def __invert__(self):
            '''KEditListBox.Buttons KEditListBox.Buttons.__invert__()'''
            return KEditListBox.Buttons()
        def __and__(self, mask):
            '''KEditListBox.Buttons KEditListBox.Buttons.__and__(int mask)'''
            return KEditListBox.Buttons()
        def __xor__(self, f):
            '''KEditListBox.Buttons KEditListBox.Buttons.__xor__(KEditListBox.Buttons f)'''
            return KEditListBox.Buttons()
        def __xor__(self, f):
            '''KEditListBox.Buttons KEditListBox.Buttons.__xor__(int f)'''
            return KEditListBox.Buttons()
        def __or__(self, f):
            '''KEditListBox.Buttons KEditListBox.Buttons.__or__(KEditListBox.Buttons f)'''
            return KEditListBox.Buttons()
        def __or__(self, f):
            '''KEditListBox.Buttons KEditListBox.Buttons.__or__(int f)'''
            return KEditListBox.Buttons()
        def __int__(self):
            '''int KEditListBox.Buttons.__int__()'''
            return int()
        def __ixor__(self, f):
            '''KEditListBox.Buttons KEditListBox.Buttons.__ixor__(KEditListBox.Buttons f)'''
            return KEditListBox.Buttons()
        def __ior__(self, f):
            '''KEditListBox.Buttons KEditListBox.Buttons.__ior__(KEditListBox.Buttons f)'''
            return KEditListBox.Buttons()
        def __iand__(self, mask):
            '''KEditListBox.Buttons KEditListBox.Buttons.__iand__(int mask)'''
            return KEditListBox.Buttons()
    class CustomEditor():
        """"""
        def __init__(self):
            '''void KEditListBox.CustomEditor.__init__()'''
        def __init__(self, repWidget, edit):
            '''void KEditListBox.CustomEditor.__init__(QWidget repWidget, KLineEdit edit)'''
        def __init__(self, combo):
            '''void KEditListBox.CustomEditor.__init__(KComboBox combo)'''
        def lineEdit(self):
            '''KLineEdit KEditListBox.CustomEditor.lineEdit()'''
            return KLineEdit()
        def representationWidget(self):
            '''QWidget KEditListBox.CustomEditor.representationWidget()'''
            return QWidget()
        def setLineEdit(self, edit):
            '''void KEditListBox.CustomEditor.setLineEdit(KLineEdit edit)'''
        def setRepresentationWidget(self, repWidget):
            '''void KEditListBox.CustomEditor.setRepresentationWidget(QWidget repWidget)'''


class KEditListWidget(QWidget):
    """"""
    # Enum KEditListWidget.Button
    Add = 0
    Remove = 0
    UpDown = 0
    All = 0

    def __init__(self, parent = None):
        '''void KEditListWidget.__init__(QWidget parent = None)'''
    def __init__(self, customEditor, parent = None, checkAtEntering = False, buttons = None):
        '''void KEditListWidget.__init__(KEditListWidget.CustomEditor customEditor, QWidget parent = None, bool checkAtEntering = False, KEditListWidget.Buttons buttons = KEditListWidget.All)'''
    removed = pyqtSignal() # void removed(const QStringamp;) - signal
    added = pyqtSignal() # void added(const QStringamp;) - signal
    changed = pyqtSignal() # void changed() - signal
    def eventFilter(self, o, e):
        '''bool KEditListWidget.eventFilter(QObject o, QEvent e)'''
        return bool()
    def setCustomEditor(self, editor):
        '''void KEditListWidget.setCustomEditor(KEditListWidget.CustomEditor editor)'''
    def checkAtEntering(self):
        '''bool KEditListWidget.checkAtEntering()'''
        return bool()
    def setCheckAtEntering(self, check):
        '''void KEditListWidget.setCheckAtEntering(bool check)'''
    def setButtons(self, buttons):
        '''void KEditListWidget.setButtons(KEditListWidget.Buttons buttons)'''
    def buttons(self):
        '''KEditListWidget.Buttons KEditListWidget.buttons()'''
        return KEditListWidget.Buttons()
    def setItems(self, items):
        '''void KEditListWidget.setItems(QStringList items)'''
    def items(self):
        '''QStringList KEditListWidget.items()'''
        return QStringList()
    def currentText(self):
        '''QString KEditListWidget.currentText()'''
        return QString()
    def currentItem(self):
        '''int KEditListWidget.currentItem()'''
        return int()
    def text(self, index):
        '''QString KEditListWidget.text(int index)'''
        return QString()
    def clear(self):
        '''void KEditListWidget.clear()'''
    def insertItem(self, text, index = None):
        '''void KEditListWidget.insertItem(QString text, int index = -1)'''
    def insertStringList(self, list, index = None):
        '''void KEditListWidget.insertStringList(QStringList list, int index = -1)'''
    def count(self):
        '''int KEditListWidget.count()'''
        return int()
    def downButton(self):
        '''QPushButton KEditListWidget.downButton()'''
        return QPushButton()
    def upButton(self):
        '''QPushButton KEditListWidget.upButton()'''
        return QPushButton()
    def removeButton(self):
        '''QPushButton KEditListWidget.removeButton()'''
        return QPushButton()
    def addButton(self):
        '''QPushButton KEditListWidget.addButton()'''
        return QPushButton()
    def lineEdit(self):
        '''KLineEdit KEditListWidget.lineEdit()'''
        return KLineEdit()
    def listView(self):
        '''QListView KEditListWidget.listView()'''
        return QListView()
    class CustomEditor():
        """"""
        def __init__(self):
            '''void KEditListWidget.CustomEditor.__init__()'''
        def __init__(self, repWidget, edit):
            '''void KEditListWidget.CustomEditor.__init__(QWidget repWidget, KLineEdit edit)'''
        def __init__(self, combo):
            '''void KEditListWidget.CustomEditor.__init__(KComboBox combo)'''
        def lineEdit(self):
            '''KLineEdit KEditListWidget.CustomEditor.lineEdit()'''
            return KLineEdit()
        def representationWidget(self):
            '''QWidget KEditListWidget.CustomEditor.representationWidget()'''
            return QWidget()
        def setLineEdit(self, edit):
            '''void KEditListWidget.CustomEditor.setLineEdit(KLineEdit edit)'''
        def setRepresentationWidget(self, repWidget):
            '''void KEditListWidget.CustomEditor.setRepresentationWidget(QWidget repWidget)'''
    class Buttons():
        """"""
        def __init__(self):
            '''KEditListWidget.Buttons KEditListWidget.Buttons.__init__()'''
            return KEditListWidget.Buttons()
        def __init__(self):
            '''int KEditListWidget.Buttons.__init__()'''
            return int()
        def __init__(self):
            '''void KEditListWidget.Buttons.__init__()'''
        def __bool__(self):
            '''int KEditListWidget.Buttons.__bool__()'''
            return int()
        def __ne__(self, f):
            '''bool KEditListWidget.Buttons.__ne__(KEditListWidget.Buttons f)'''
            return bool()
        def __eq__(self, f):
            '''bool KEditListWidget.Buttons.__eq__(KEditListWidget.Buttons f)'''
            return bool()
        def __invert__(self):
            '''KEditListWidget.Buttons KEditListWidget.Buttons.__invert__()'''
            return KEditListWidget.Buttons()
        def __and__(self, mask):
            '''KEditListWidget.Buttons KEditListWidget.Buttons.__and__(int mask)'''
            return KEditListWidget.Buttons()
        def __xor__(self, f):
            '''KEditListWidget.Buttons KEditListWidget.Buttons.__xor__(KEditListWidget.Buttons f)'''
            return KEditListWidget.Buttons()
        def __xor__(self, f):
            '''KEditListWidget.Buttons KEditListWidget.Buttons.__xor__(int f)'''
            return KEditListWidget.Buttons()
        def __or__(self, f):
            '''KEditListWidget.Buttons KEditListWidget.Buttons.__or__(KEditListWidget.Buttons f)'''
            return KEditListWidget.Buttons()
        def __or__(self, f):
            '''KEditListWidget.Buttons KEditListWidget.Buttons.__or__(int f)'''
            return KEditListWidget.Buttons()
        def __int__(self):
            '''int KEditListWidget.Buttons.__int__()'''
            return int()
        def __ixor__(self, f):
            '''KEditListWidget.Buttons KEditListWidget.Buttons.__ixor__(KEditListWidget.Buttons f)'''
            return KEditListWidget.Buttons()
        def __ior__(self, f):
            '''KEditListWidget.Buttons KEditListWidget.Buttons.__ior__(KEditListWidget.Buttons f)'''
            return KEditListWidget.Buttons()
        def __iand__(self, mask):
            '''KEditListWidget.Buttons KEditListWidget.Buttons.__iand__(int mask)'''
            return KEditListWidget.Buttons()


class KEditToolBar(KDialog):
    """"""
    def __init__(self, collection, parent = None):
        '''void KEditToolBar.__init__(KActionCollection collection, QWidget parent = None)'''
    def __init__(self, factory, parent = None):
        '''void KEditToolBar.__init__(KXMLGUIFactory factory, QWidget parent = None)'''
    def hideEvent(self, event):
        '''void KEditToolBar.hideEvent(QHideEvent event)'''
    def showEvent(self, event):
        '''void KEditToolBar.showEvent(QShowEvent event)'''
    newToolbarConfig = pyqtSignal() # void newToolbarConfig() - signal
    newToolBarConfig = pyqtSignal() # void newToolBarConfig() - signal
    def setGlobalDefaultToolBar(self, toolBarName):
        '''static void KEditToolBar.setGlobalDefaultToolBar(str toolBarName)'''
    def setResourceFile(self, file, global_ = True):
        '''void KEditToolBar.setResourceFile(QString file, bool global = True)'''
    def setDefaultToolBar(self, toolBarName):
        '''void KEditToolBar.setDefaultToolBar(QString toolBarName)'''


class KExtendableItemDelegate(QStyledItemDelegate):
    """"""
    # Enum KExtendableItemDelegate.auxDataRoles
    ShowExtensionIndicatorRole = 0

    def __init__(self, parent):
        '''void KExtendableItemDelegate.__init__(QAbstractItemView parent)'''
    def contractPixmap(self):
        '''QPixmap KExtendableItemDelegate.contractPixmap()'''
        return QPixmap()
    def extendPixmap(self):
        '''QPixmap KExtendableItemDelegate.extendPixmap()'''
        return QPixmap()
    def setContractPixmap(self, pixmap):
        '''void KExtendableItemDelegate.setContractPixmap(QPixmap pixmap)'''
    def setExtendPixmap(self, pixmap):
        '''void KExtendableItemDelegate.setExtendPixmap(QPixmap pixmap)'''
    def extenderRect(self, extender, option, index):
        '''QRect KExtendableItemDelegate.extenderRect(QWidget extender, QStyleOptionViewItem option, QModelIndex index)'''
        return QRect()
    extenderDestroyed = pyqtSignal() # void extenderDestroyed(QWidget *,const QModelIndexamp;) - signal
    extenderCreated = pyqtSignal() # void extenderCreated(QWidget *,const QModelIndexamp;) - signal
    def updateExtenderGeometry(self, extender, option, index):
        '''void KExtendableItemDelegate.updateExtenderGeometry(QWidget extender, QStyleOptionViewItem option, QModelIndex index)'''
    def isExtended(self, index):
        '''bool KExtendableItemDelegate.isExtended(QModelIndex index)'''
        return bool()
    def contractAll(self):
        '''void KExtendableItemDelegate.contractAll()'''
    def contractItem(self, index):
        '''void KExtendableItemDelegate.contractItem(QModelIndex index)'''
    def extendItem(self, extender, index):
        '''void KExtendableItemDelegate.extendItem(QWidget extender, QModelIndex index)'''
    def paint(self, painter, option, index):
        '''void KExtendableItemDelegate.paint(QPainter painter, QStyleOptionViewItem option, QModelIndex index)'''
    def sizeHint(self, option, index):
        '''QSize KExtendableItemDelegate.sizeHint(QStyleOptionViewItem option, QModelIndex index)'''
        return QSize()


class KFadeWidgetEffect(QWidget):
    """"""
    def __init__(self, destWidget):
        '''void KFadeWidgetEffect.__init__(QWidget destWidget)'''
    def paintEvent(self):
        '''QPaintEvent KFadeWidgetEffect.paintEvent()'''
        return QPaintEvent()
    def start(self, duration = 250):
        '''void KFadeWidgetEffect.start(int duration = 250)'''


class KFilterProxySearchLine(QWidget):
    """"""
    def __init__(self, parent = None):
        '''void KFilterProxySearchLine.__init__(QWidget parent = None)'''
    def lineEdit(self):
        '''KLineEdit KFilterProxySearchLine.lineEdit()'''
        return KLineEdit()
    def setText(self, text):
        '''void KFilterProxySearchLine.setText(QString text)'''
    def setProxy(self, proxy):
        '''void KFilterProxySearchLine.setProxy(QSortFilterProxyModel proxy)'''


class KFind(QObject):
    """"""
    # Enum KFind.Result
    NoMatch = 0
    Match = 0

    # Enum KFind.Options
    WholeWordsOnly = 0
    FromCursor = 0
    SelectedText = 0
    CaseSensitive = 0
    FindBackwards = 0
    RegularExpression = 0
    FindIncremental = 0
    MinimumUserOption = 0

    def __init__(self, pattern, options, parent):
        '''void KFind.__init__(QString pattern, int options, QWidget parent)'''
    def __init__(self, pattern, options, parent, findDialog):
        '''void KFind.__init__(QString pattern, int options, QWidget parent, QWidget findDialog)'''
    def dialogsParent(self):
        '''QWidget KFind.dialogsParent()'''
        return QWidget()
    def parentWidget(self):
        '''QWidget KFind.parentWidget()'''
        return QWidget()
    dialogClosed = pyqtSignal() # void dialogClosed() - signal
    optionsChanged = pyqtSignal() # void optionsChanged() - signal
    findNext = pyqtSignal() # void findNext() - signal
    highlight = pyqtSignal() # void highlight(const QStringamp;,int,int) - signal
    highlight = pyqtSignal() # void highlight(int,int,int) - signal
    def index(self):
        '''int KFind.index()'''
        return int()
    def closeFindNextDialog(self):
        '''void KFind.closeFindNextDialog()'''
    def findNextDialog(self, create = False):
        '''KDialog KFind.findNextDialog(bool create = False)'''
        return KDialog()
    def displayFinalDialog(self):
        '''void KFind.displayFinalDialog()'''
    def shouldRestart(self, forceAsking = False, showNumMatches = True):
        '''bool KFind.shouldRestart(bool forceAsking = False, bool showNumMatches = True)'''
        return bool()
    def validateMatch(self, text, index, matchedlength):
        '''bool KFind.validateMatch(QString text, int index, int matchedlength)'''
        return bool()
    def resetCounts(self):
        '''void KFind.resetCounts()'''
    def numMatches(self):
        '''int KFind.numMatches()'''
        return int()
    def setPattern(self, pattern):
        '''void KFind.setPattern(QString pattern)'''
    def pattern(self):
        '''QString KFind.pattern()'''
        return QString()
    def setOptions(self, options):
        '''void KFind.setOptions(int options)'''
    def options(self):
        '''int KFind.options()'''
        return int()
    def find(self):
        '''KFind.Result KFind.find()'''
        return KFind.Result()
    def find(self, text, pattern, index, options, matchedlength):
        '''static int KFind.find(QString text, QString pattern, int index, int options, int matchedlength)'''
        return int()
    def find(self, text, pattern, index, options, matchedlength):
        '''static int KFind.find(QString text, QRegExp pattern, int index, int options, int matchedlength)'''
        return int()
    def setData(self, data, startPos = None):
        '''void KFind.setData(QString data, int startPos = -1)'''
    def setData(self, id, data, startPos = None):
        '''void KFind.setData(int id, QString data, int startPos = -1)'''
    def needData(self):
        '''bool KFind.needData()'''
        return bool()
    class SearchOptions():
        """"""
        def __init__(self):
            '''KFind.SearchOptions KFind.SearchOptions.__init__()'''
            return KFind.SearchOptions()
        def __init__(self):
            '''int KFind.SearchOptions.__init__()'''
            return int()
        def __init__(self):
            '''void KFind.SearchOptions.__init__()'''
        def __bool__(self):
            '''int KFind.SearchOptions.__bool__()'''
            return int()
        def __ne__(self, f):
            '''bool KFind.SearchOptions.__ne__(KFind.SearchOptions f)'''
            return bool()
        def __eq__(self, f):
            '''bool KFind.SearchOptions.__eq__(KFind.SearchOptions f)'''
            return bool()
        def __invert__(self):
            '''KFind.SearchOptions KFind.SearchOptions.__invert__()'''
            return KFind.SearchOptions()
        def __and__(self, mask):
            '''KFind.SearchOptions KFind.SearchOptions.__and__(int mask)'''
            return KFind.SearchOptions()
        def __xor__(self, f):
            '''KFind.SearchOptions KFind.SearchOptions.__xor__(KFind.SearchOptions f)'''
            return KFind.SearchOptions()
        def __xor__(self, f):
            '''KFind.SearchOptions KFind.SearchOptions.__xor__(int f)'''
            return KFind.SearchOptions()
        def __or__(self, f):
            '''KFind.SearchOptions KFind.SearchOptions.__or__(KFind.SearchOptions f)'''
            return KFind.SearchOptions()
        def __or__(self, f):
            '''KFind.SearchOptions KFind.SearchOptions.__or__(int f)'''
            return KFind.SearchOptions()
        def __int__(self):
            '''int KFind.SearchOptions.__int__()'''
            return int()
        def __ixor__(self, f):
            '''KFind.SearchOptions KFind.SearchOptions.__ixor__(KFind.SearchOptions f)'''
            return KFind.SearchOptions()
        def __ior__(self, f):
            '''KFind.SearchOptions KFind.SearchOptions.__ior__(KFind.SearchOptions f)'''
            return KFind.SearchOptions()
        def __iand__(self, mask):
            '''KFind.SearchOptions KFind.SearchOptions.__iand__(int mask)'''
            return KFind.SearchOptions()


class KFindDialog(KDialog):
    """"""
    def __init__(self, parent = None, options = 0, findStrings = QStringList(), hasSelection = False, replaceDialog = False):
        '''void KFindDialog.__init__(QWidget parent = None, int options = 0, QStringList findStrings = QStringList(), bool hasSelection = False, bool replaceDialog = False)'''
    def showEvent(self):
        '''QShowEvent KFindDialog.showEvent()'''
        return QShowEvent()
    optionsChanged = pyqtSignal() # void optionsChanged() - signal
    def findExtension(self):
        '''QWidget KFindDialog.findExtension()'''
        return QWidget()
    def setPattern(self, pattern):
        '''void KFindDialog.setPattern(QString pattern)'''
    def pattern(self):
        '''QString KFindDialog.pattern()'''
        return QString()
    def options(self):
        '''int KFindDialog.options()'''
        return int()
    def setOptions(self, options):
        '''void KFindDialog.setOptions(int options)'''
    def setSupportsRegularExpressionFind(self, supports):
        '''void KFindDialog.setSupportsRegularExpressionFind(bool supports)'''
    def setSupportsWholeWordsFind(self, supports):
        '''void KFindDialog.setSupportsWholeWordsFind(bool supports)'''
    def setSupportsCaseSensitiveFind(self, supports):
        '''void KFindDialog.setSupportsCaseSensitiveFind(bool supports)'''
    def setSupportsBackwardsFind(self, supports):
        '''void KFindDialog.setSupportsBackwardsFind(bool supports)'''
    def setHasCursor(self, hasCursor):
        '''void KFindDialog.setHasCursor(bool hasCursor)'''
    def setHasSelection(self, hasSelection):
        '''void KFindDialog.setHasSelection(bool hasSelection)'''
    def findHistory(self):
        '''QStringList KFindDialog.findHistory()'''
        return QStringList()
    def setFindHistory(self, history):
        '''void KFindDialog.setFindHistory(QStringList history)'''


class KFontAction(KSelectAction):
    """"""
    def __init__(self, fontListCriteria, parent):
        '''void KFontAction.__init__(int fontListCriteria, QObject parent)'''
    def __init__(self, parent):
        '''void KFontAction.__init__(QObject parent)'''
    def __init__(self, text, parent):
        '''void KFontAction.__init__(QString text, QObject parent)'''
    def __init__(self, icon, text, parent):
        '''void KFontAction.__init__(KIcon icon, QString text, QObject parent)'''
    def createWidget(self, parent):
        '''QWidget KFontAction.createWidget(QWidget parent)'''
        return QWidget()
    def setFont(self, family):
        '''void KFontAction.setFont(QString family)'''
    def font(self):
        '''QString KFontAction.font()'''
        return QString()


class KFontChooser(QWidget):
    """"""
    # Enum KFontChooser.FontListCriteria
    FixedWidthFonts = 0
    ScalableFonts = 0
    SmoothScalableFonts = 0

    # Enum KFontChooser.DisplayFlag
    NoDisplayFlags = 0
    FixedFontsOnly = 0
    DisplayFrame = 0
    ShowDifferences = 0

    # Enum KFontChooser.FontDiff
    NoFontDiffFlags = 0
    FontDiffFamily = 0
    FontDiffStyle = 0
    FontDiffSize = 0
    AllFontDiffs = 0

    # Enum KFontChooser.FontColumn
    FamilyList = 0
    StyleList = 0
    SizeList = 0

    def __init__(self, parent = None, flags = None, fontList = QStringList(), visibleListSize = 8, sizeIsRelativeState = None):
        '''void KFontChooser.__init__(QWidget parent = None, KFontChooser.DisplayFlags flags = KFontChooser.DisplayFrame, QStringList fontList = QStringList(), int visibleListSize = 8, Qt.CheckState sizeIsRelativeState)'''
    fontSelected = pyqtSignal() # void fontSelected(const QFontamp;) - signal
    def sizeHint(self):
        '''QSize KFontChooser.sizeHint()'''
        return QSize()
    def getFontList(self, list, fontListCriteria):
        '''static void KFontChooser.getFontList(QStringList list, int fontListCriteria)'''
    def setSampleBoxVisible(self, visible):
        '''void KFontChooser.setSampleBoxVisible(bool visible)'''
    def setSampleText(self, text):
        '''void KFontChooser.setSampleText(QString text)'''
    def sampleText(self):
        '''QString KFontChooser.sampleText()'''
        return QString()
    def sizeIsRelative(self):
        '''Qt.CheckState KFontChooser.sizeIsRelative()'''
        return Qt.CheckState()
    def setSizeIsRelative(self, relative):
        '''void KFontChooser.setSizeIsRelative(Qt.CheckState relative)'''
    def backgroundColor(self):
        '''QColor KFontChooser.backgroundColor()'''
        return QColor()
    def setBackgroundColor(self, col):
        '''void KFontChooser.setBackgroundColor(QColor col)'''
    def color(self):
        '''QColor KFontChooser.color()'''
        return QColor()
    def setColor(self, col):
        '''void KFontChooser.setColor(QColor col)'''
    def font(self):
        '''QFont KFontChooser.font()'''
        return QFont()
    def fontDiffFlags(self):
        '''KFontChooser.FontDiffFlags KFontChooser.fontDiffFlags()'''
        return KFontChooser.FontDiffFlags()
    def setFont(self, font, onlyFixed = False):
        '''void KFontChooser.setFont(QFont font, bool onlyFixed = False)'''
    def enableColumn(self, column, state):
        '''void KFontChooser.enableColumn(int column, bool state)'''
    class DisplayFlags():
        """"""
        def __init__(self):
            '''KFontChooser.DisplayFlags KFontChooser.DisplayFlags.__init__()'''
            return KFontChooser.DisplayFlags()
        def __init__(self):
            '''int KFontChooser.DisplayFlags.__init__()'''
            return int()
        def __init__(self):
            '''void KFontChooser.DisplayFlags.__init__()'''
        def __bool__(self):
            '''int KFontChooser.DisplayFlags.__bool__()'''
            return int()
        def __ne__(self, f):
            '''bool KFontChooser.DisplayFlags.__ne__(KFontChooser.DisplayFlags f)'''
            return bool()
        def __eq__(self, f):
            '''bool KFontChooser.DisplayFlags.__eq__(KFontChooser.DisplayFlags f)'''
            return bool()
        def __invert__(self):
            '''KFontChooser.DisplayFlags KFontChooser.DisplayFlags.__invert__()'''
            return KFontChooser.DisplayFlags()
        def __and__(self, mask):
            '''KFontChooser.DisplayFlags KFontChooser.DisplayFlags.__and__(int mask)'''
            return KFontChooser.DisplayFlags()
        def __xor__(self, f):
            '''KFontChooser.DisplayFlags KFontChooser.DisplayFlags.__xor__(KFontChooser.DisplayFlags f)'''
            return KFontChooser.DisplayFlags()
        def __xor__(self, f):
            '''KFontChooser.DisplayFlags KFontChooser.DisplayFlags.__xor__(int f)'''
            return KFontChooser.DisplayFlags()
        def __or__(self, f):
            '''KFontChooser.DisplayFlags KFontChooser.DisplayFlags.__or__(KFontChooser.DisplayFlags f)'''
            return KFontChooser.DisplayFlags()
        def __or__(self, f):
            '''KFontChooser.DisplayFlags KFontChooser.DisplayFlags.__or__(int f)'''
            return KFontChooser.DisplayFlags()
        def __int__(self):
            '''int KFontChooser.DisplayFlags.__int__()'''
            return int()
        def __ixor__(self, f):
            '''KFontChooser.DisplayFlags KFontChooser.DisplayFlags.__ixor__(KFontChooser.DisplayFlags f)'''
            return KFontChooser.DisplayFlags()
        def __ior__(self, f):
            '''KFontChooser.DisplayFlags KFontChooser.DisplayFlags.__ior__(KFontChooser.DisplayFlags f)'''
            return KFontChooser.DisplayFlags()
        def __iand__(self, mask):
            '''KFontChooser.DisplayFlags KFontChooser.DisplayFlags.__iand__(int mask)'''
            return KFontChooser.DisplayFlags()
    class FontDiffFlags():
        """"""
        def __init__(self):
            '''KFontChooser.FontDiffFlags KFontChooser.FontDiffFlags.__init__()'''
            return KFontChooser.FontDiffFlags()
        def __init__(self):
            '''int KFontChooser.FontDiffFlags.__init__()'''
            return int()
        def __init__(self):
            '''void KFontChooser.FontDiffFlags.__init__()'''
        def __bool__(self):
            '''int KFontChooser.FontDiffFlags.__bool__()'''
            return int()
        def __ne__(self, f):
            '''bool KFontChooser.FontDiffFlags.__ne__(KFontChooser.FontDiffFlags f)'''
            return bool()
        def __eq__(self, f):
            '''bool KFontChooser.FontDiffFlags.__eq__(KFontChooser.FontDiffFlags f)'''
            return bool()
        def __invert__(self):
            '''KFontChooser.FontDiffFlags KFontChooser.FontDiffFlags.__invert__()'''
            return KFontChooser.FontDiffFlags()
        def __and__(self, mask):
            '''KFontChooser.FontDiffFlags KFontChooser.FontDiffFlags.__and__(int mask)'''
            return KFontChooser.FontDiffFlags()
        def __xor__(self, f):
            '''KFontChooser.FontDiffFlags KFontChooser.FontDiffFlags.__xor__(KFontChooser.FontDiffFlags f)'''
            return KFontChooser.FontDiffFlags()
        def __xor__(self, f):
            '''KFontChooser.FontDiffFlags KFontChooser.FontDiffFlags.__xor__(int f)'''
            return KFontChooser.FontDiffFlags()
        def __or__(self, f):
            '''KFontChooser.FontDiffFlags KFontChooser.FontDiffFlags.__or__(KFontChooser.FontDiffFlags f)'''
            return KFontChooser.FontDiffFlags()
        def __or__(self, f):
            '''KFontChooser.FontDiffFlags KFontChooser.FontDiffFlags.__or__(int f)'''
            return KFontChooser.FontDiffFlags()
        def __int__(self):
            '''int KFontChooser.FontDiffFlags.__int__()'''
            return int()
        def __ixor__(self, f):
            '''KFontChooser.FontDiffFlags KFontChooser.FontDiffFlags.__ixor__(KFontChooser.FontDiffFlags f)'''
            return KFontChooser.FontDiffFlags()
        def __ior__(self, f):
            '''KFontChooser.FontDiffFlags KFontChooser.FontDiffFlags.__ior__(KFontChooser.FontDiffFlags f)'''
            return KFontChooser.FontDiffFlags()
        def __iand__(self, mask):
            '''KFontChooser.FontDiffFlags KFontChooser.FontDiffFlags.__iand__(int mask)'''
            return KFontChooser.FontDiffFlags()


class KFontComboBox(KComboBox):
    """"""
    def __init__(self, parent = None):
        '''void KFontComboBox.__init__(QWidget parent = None)'''
    def event(self, e):
        '''bool KFontComboBox.event(QEvent e)'''
        return bool()
    currentFontChanged = pyqtSignal() # void currentFontChanged(const QFontamp;) - signal
    def setCurrentFont(self, font):
        '''void KFontComboBox.setCurrentFont(QFont font)'''
    def sizeHint(self):
        '''QSize KFontComboBox.sizeHint()'''
        return QSize()
    def currentFont(self):
        '''QFont KFontComboBox.currentFont()'''
        return QFont()
    def setOnlyFixed(self, onlyFixed):
        '''void KFontComboBox.setOnlyFixed(bool onlyFixed)'''


class KFontDialog(KDialog):
    """"""
    def __init__(self, parent = None, flags = None, fontlist = QStringList(), sizeIsRelativeState = None):
        '''void KFontDialog.__init__(QWidget parent = None, KFontChooser.DisplayFlags flags = KFontChooser.NoDisplayFlags, QStringList fontlist = QStringList(), Qt.CheckState sizeIsRelativeState)'''
    fontSelected = pyqtSignal() # void fontSelected(const QFontamp;) - signal
    def getFontAndText(self, theFont, theString, flags = None, parent = None, sizeIsRelativeState = None):
        '''static tuple KFontDialog.getFontAndText(QFont theFont, QString theString, KFontChooser.DisplayFlags flags = KFontChooser.NoDisplayFlags, QWidget parent = None, Qt.CheckState sizeIsRelativeState = Qt.Unchecked)'''
        return tuple()
    def getFontDiff(self, theFont, diffFlags, flags = None, parent = None, sizeIsRelativeState = None):
        '''static tuple KFontDialog.getFontDiff(QFont theFont, KFontChooser.FontDiffFlags diffFlags, KFontChooser.DisplayFlags flags = KFontChooser.NoDisplayFlags, QWidget parent = None, Qt.CheckState sizeIsRelativeState = Qt.Unchecked)'''
        return tuple()
    def getFont(self, theFont, flags = None, parent = None, sizeIsRelativeState = None):
        '''static tuple KFontDialog.getFont(QFont theFont, KFontChooser.DisplayFlags flags = KFontChooser.NoDisplayFlags, QWidget parent = None, Qt.CheckState sizeIsRelativeState)'''
        return tuple()
    def sizeIsRelative(self):
        '''Qt.CheckState KFontDialog.sizeIsRelative()'''
        return Qt.CheckState()
    def setSizeIsRelative(self, relative):
        '''void KFontDialog.setSizeIsRelative(Qt.CheckState relative)'''
    def font(self):
        '''QFont KFontDialog.font()'''
        return QFont()
    def setFont(self, font, onlyFixed = False):
        '''void KFontDialog.setFont(QFont font, bool onlyFixed = False)'''


class KFontRequester(QWidget):
    """"""
    def __init__(self, parent = None, onlyFixed = False):
        '''void KFontRequester.__init__(QWidget parent = None, bool onlyFixed = False)'''
    fontSelected = pyqtSignal() # void fontSelected(const QFontamp;) - signal
    def setTitle(self, title):
        '''void KFontRequester.setTitle(QString title)'''
    def setSampleText(self, text):
        '''void KFontRequester.setSampleText(QString text)'''
    def setFont(self, font, onlyFixed = False):
        '''void KFontRequester.setFont(QFont font, bool onlyFixed = False)'''
    def button(self):
        '''QPushButton KFontRequester.button()'''
        return QPushButton()
    def label(self):
        '''QLabel KFontRequester.label()'''
        return QLabel()
    def title(self):
        '''QString KFontRequester.title()'''
        return QString()
    def sampleText(self):
        '''QString KFontRequester.sampleText()'''
        return QString()
    def isFixedOnly(self):
        '''bool KFontRequester.isFixedOnly()'''
        return bool()
    def font(self):
        '''QFont KFontRequester.font()'''
        return QFont()


class KFontSizeAction(KSelectAction):
    """"""
    def __init__(self, parent):
        '''void KFontSizeAction.__init__(QObject parent)'''
    def __init__(self, text, parent):
        '''void KFontSizeAction.__init__(QString text, QObject parent)'''
    def __init__(self, icon, text, parent):
        '''void KFontSizeAction.__init__(KIcon icon, QString text, QObject parent)'''
    def actionTriggered(self, action):
        '''void KFontSizeAction.actionTriggered(QAction action)'''
    fontSizeChanged = pyqtSignal() # void fontSizeChanged(int) - signal
    def setFontSize(self, size):
        '''void KFontSizeAction.setFontSize(int size)'''
    def fontSize(self):
        '''int KFontSizeAction.fontSize()'''
        return int()


class KFontUtils():
    """"""
    # Enum KFontUtils.AdaptFontSizeOption
    NoFlags = 0
    DoNotAllowWordWrap = 0

    def adaptFontSize(self, painter, text, width, height, maxFontSize = 28, minFontSize = 1, flags = None):
        '''static float KFontUtils.adaptFontSize(QPainter painter, QString text, float width, float height, float maxFontSize = 28, float minFontSize = 1, KFontUtils.AdaptFontSizeOptions flags = KFontUtils.NoFlags)'''
        return float()
    def adaptFontSize(self, painter, text, availableSize, maxFontSize = 28, minFontSize = 1, flags = None):
        '''static float KFontUtils.adaptFontSize(QPainter painter, QString text, QSizeF availableSize, float maxFontSize = 28, float minFontSize = 1, KFontUtils.AdaptFontSizeOptions flags = KFontUtils.NoFlags)'''
        return float()
    class AdaptFontSizeOptions():
        """"""
        def __init__(self):
            '''KFontUtils.AdaptFontSizeOptions KFontUtils.AdaptFontSizeOptions.__init__()'''
            return KFontUtils.AdaptFontSizeOptions()
        def __init__(self):
            '''int KFontUtils.AdaptFontSizeOptions.__init__()'''
            return int()
        def __init__(self):
            '''void KFontUtils.AdaptFontSizeOptions.__init__()'''
        def __bool__(self):
            '''int KFontUtils.AdaptFontSizeOptions.__bool__()'''
            return int()
        def __ne__(self, f):
            '''bool KFontUtils.AdaptFontSizeOptions.__ne__(KFontUtils.AdaptFontSizeOptions f)'''
            return bool()
        def __eq__(self, f):
            '''bool KFontUtils.AdaptFontSizeOptions.__eq__(KFontUtils.AdaptFontSizeOptions f)'''
            return bool()
        def __invert__(self):
            '''KFontUtils.AdaptFontSizeOptions KFontUtils.AdaptFontSizeOptions.__invert__()'''
            return KFontUtils.AdaptFontSizeOptions()
        def __and__(self, mask):
            '''KFontUtils.AdaptFontSizeOptions KFontUtils.AdaptFontSizeOptions.__and__(int mask)'''
            return KFontUtils.AdaptFontSizeOptions()
        def __xor__(self, f):
            '''KFontUtils.AdaptFontSizeOptions KFontUtils.AdaptFontSizeOptions.__xor__(KFontUtils.AdaptFontSizeOptions f)'''
            return KFontUtils.AdaptFontSizeOptions()
        def __xor__(self, f):
            '''KFontUtils.AdaptFontSizeOptions KFontUtils.AdaptFontSizeOptions.__xor__(int f)'''
            return KFontUtils.AdaptFontSizeOptions()
        def __or__(self, f):
            '''KFontUtils.AdaptFontSizeOptions KFontUtils.AdaptFontSizeOptions.__or__(KFontUtils.AdaptFontSizeOptions f)'''
            return KFontUtils.AdaptFontSizeOptions()
        def __or__(self, f):
            '''KFontUtils.AdaptFontSizeOptions KFontUtils.AdaptFontSizeOptions.__or__(int f)'''
            return KFontUtils.AdaptFontSizeOptions()
        def __int__(self):
            '''int KFontUtils.AdaptFontSizeOptions.__int__()'''
            return int()
        def __ixor__(self, f):
            '''KFontUtils.AdaptFontSizeOptions KFontUtils.AdaptFontSizeOptions.__ixor__(KFontUtils.AdaptFontSizeOptions f)'''
            return KFontUtils.AdaptFontSizeOptions()
        def __ior__(self, f):
            '''KFontUtils.AdaptFontSizeOptions KFontUtils.AdaptFontSizeOptions.__ior__(KFontUtils.AdaptFontSizeOptions f)'''
            return KFontUtils.AdaptFontSizeOptions()
        def __iand__(self, mask):
            '''KFontUtils.AdaptFontSizeOptions KFontUtils.AdaptFontSizeOptions.__iand__(int mask)'''
            return KFontUtils.AdaptFontSizeOptions()


class KShapeGesture():
    """"""
    def __init__(self):
        '''void KShapeGesture.__init__()'''
    def __init__(self, shape):
        '''void KShapeGesture.__init__(QPolygon shape)'''
    def __init__(self, description):
        '''void KShapeGesture.__init__(QString description)'''
    def __init__(self, other):
        '''void KShapeGesture.__init__(KShapeGesture other)'''
    def hashable(self):
        '''int KShapeGesture.hashable()'''
        return int()
    def __ne__(self, other):
        '''bool KShapeGesture.__ne__(KShapeGesture other)'''
        return bool()
    def __eq__(self, other):
        '''bool KShapeGesture.__eq__(KShapeGesture other)'''
        return bool()
    def distance(self, other, abortThreshold):
        '''float KShapeGesture.distance(KShapeGesture other, float abortThreshold)'''
        return float()
    def toSvg(self, attributes = QString()):
        '''QByteArray KShapeGesture.toSvg(QString attributes = QString())'''
        return QByteArray()
    def toString(self):
        '''QString KShapeGesture.toString()'''
        return QString()
    def isValid(self):
        '''bool KShapeGesture.isValid()'''
        return bool()
    def shapeName(self):
        '''QString KShapeGesture.shapeName()'''
        return QString()
    def setShapeName(self, friendlyName):
        '''void KShapeGesture.setShapeName(QString friendlyName)'''
    def setShape(self, shape):
        '''void KShapeGesture.setShape(QPolygon shape)'''


class KRockerGesture():
    """"""
    def __init__(self):
        '''void KRockerGesture.__init__()'''
    def __init__(self, hold, thenPush):
        '''void KRockerGesture.__init__(Qt.MouseButton hold, Qt.MouseButton thenPush)'''
    def __init__(self, description):
        '''void KRockerGesture.__init__(QString description)'''
    def __init__(self, other):
        '''void KRockerGesture.__init__(KRockerGesture other)'''
    def hashable(self):
        '''int KRockerGesture.hashable()'''
        return int()
    def __ne__(self, other):
        '''bool KRockerGesture.__ne__(KRockerGesture other)'''
        return bool()
    def __eq__(self, other):
        '''bool KRockerGesture.__eq__(KRockerGesture other)'''
        return bool()
    def toString(self):
        '''QString KRockerGesture.toString()'''
        return QString()
    def isValid(self):
        '''bool KRockerGesture.isValid()'''
        return bool()
    def mouseButtonName(self, button):
        '''static QString KRockerGesture.mouseButtonName(Qt.MouseButton button)'''
        return QString()
    def rockerName(self):
        '''QString KRockerGesture.rockerName()'''
        return QString()
    def getButtons(self, hold, thenPush):
        '''void KRockerGesture.getButtons(Qt.MouseButton hold, Qt.MouseButton thenPush)'''
    def setButtons(self, hold, thenPush):
        '''void KRockerGesture.setButtons(Qt.MouseButton hold, Qt.MouseButton thenPush)'''


class KGlobalAccel(QObject):
    """"""
    # Enum KGlobalAccel.actionIdFields
    ComponentUnique = 0
    ActionUnique = 0
    ComponentFriendly = 0
    ActionFriendly = 0

    def findActionNameSystemwide(self, seq):
        '''static QStringList KGlobalAccel.findActionNameSystemwide(QKeySequence seq)'''
        return QStringList()
    def allActionsForComponent(self, actionId):
        '''list-of-QStringList KGlobalAccel.allActionsForComponent(QStringList actionId)'''
        return [QStringList()]
    def allMainComponents(self):
        '''list-of-QStringList KGlobalAccel.allMainComponents()'''
        return [QStringList()]
    def overrideMainComponentData(self, componentData):
        '''void KGlobalAccel.overrideMainComponentData(KComponentData componentData)'''
    def setEnabled(self, enabled):
        '''void KGlobalAccel.setEnabled(bool enabled)'''
    def isEnabled(self):
        '''bool KGlobalAccel.isEnabled()'''
        return bool()
    def promptStealShortcutSystemwide(self, parent, shortcuts, seq):
        '''static bool KGlobalAccel.promptStealShortcutSystemwide(QWidget parent, list-of-KGlobalShortcutInfo shortcuts, QKeySequence seq)'''
        return bool()
    def promptStealShortcutSystemwide(self, parent, actionIdentifier, seq):
        '''static bool KGlobalAccel.promptStealShortcutSystemwide(QWidget parent, QStringList actionIdentifier, QKeySequence seq)'''
        return bool()
    def isGlobalShortcutAvailable(self, seq, component = QString()):
        '''static bool KGlobalAccel.isGlobalShortcutAvailable(QKeySequence seq, QString component = QString())'''
        return bool()
    def getGlobalShortcutsByKey(self, seq):
        '''static list-of-KGlobalShortcutInfo KGlobalAccel.getGlobalShortcutsByKey(QKeySequence seq)'''
        return [KGlobalShortcutInfo()]
    def isComponentActive(self, componentName):
        '''static bool KGlobalAccel.isComponentActive(QString componentName)'''
        return bool()
    def cleanComponent(self, componentUnique):
        '''static bool KGlobalAccel.cleanComponent(QString componentUnique)'''
        return bool()
    def activateGlobalShortcutContext(self, contextUnique, contextFriendly, component = None):
        '''static void KGlobalAccel.activateGlobalShortcutContext(QString contextUnique, QString contextFriendly, KComponentData component = KGlobal.mainComponent())'''
    def stealShortcutSystemwide(self, seq):
        '''static void KGlobalAccel.stealShortcutSystemwide(QKeySequence seq)'''
    def self(self):
        '''static KGlobalAccel KGlobalAccel.self()'''
        return KGlobalAccel()


class KGlobalSettings(QObject):
    """"""
    # Enum KGlobalSettings.ActivateOption
    ApplySettings = 0
    ListenForChanges = 0

    # Enum KGlobalSettings.SettingsCategory
    SETTINGS_MOUSE = 0
    SETTINGS_COMPLETION = 0
    SETTINGS_PATHS = 0
    SETTINGS_POPUPMENU = 0
    SETTINGS_QT = 0
    SETTINGS_SHORTCUTS = 0
    SETTINGS_LOCALE = 0
    SETTINGS_STYLE = 0

    # Enum KGlobalSettings.ChangeType
    PaletteChanged = 0
    FontChanged = 0
    StyleChanged = 0
    SettingsChanged = 0
    IconChanged = 0
    CursorChanged = 0
    ToolbarStyleChanged = 0
    ClipboardConfigChanged = 0
    BlockShortcuts = 0
    NaturalSortingChanged = 0

    # Enum KGlobalSettings.GraphicEffect
    NoEffects = 0
    GradientEffects = 0
    SimpleAnimationEffects = 0
    ComplexAnimationEffects = 0

    # Enum KGlobalSettings.Completion
    CompletionNone = 0
    CompletionAuto = 0
    CompletionMan = 0
    CompletionShell = 0
    CompletionPopup = 0
    CompletionPopupAuto = 0

    # Enum KGlobalSettings.TearOffHandle
    Disable = 0
    ApplicationLevel = 0
    Enable = 0

    def createNewApplicationPalette(self, config = KSharedConfigPtr()):
        '''static QPalette KGlobalSettings.createNewApplicationPalette(KSharedConfigPtr config = KSharedConfigPtr())'''
        return QPalette()
    naturalSortingChanged = pyqtSignal() # void naturalSortingChanged() - signal
    def naturalSorting(self):
        '''static bool KGlobalSettings.naturalSorting()'''
        return bool()
    def activate(self):
        '''void KGlobalSettings.activate()'''
    def activate(self, options):
        '''void KGlobalSettings.activate(KGlobalSettings.ActivateOptions options)'''
    blockShortcuts = pyqtSignal() # void blockShortcuts(int) - signal
    cursorChanged = pyqtSignal() # void cursorChanged() - signal
    iconChanged = pyqtSignal() # void iconChanged(int) - signal
    settingsChanged = pyqtSignal() # void settingsChanged(int) - signal
    toolbarAppearanceChanged = pyqtSignal() # void toolbarAppearanceChanged(int) - signal
    appearanceChanged = pyqtSignal() # void appearanceChanged() - signal
    kdisplayFontChanged = pyqtSignal() # void kdisplayFontChanged() - signal
    kdisplayStyleChanged = pyqtSignal() # void kdisplayStyleChanged() - signal
    kdisplayPaletteChanged = pyqtSignal() # void kdisplayPaletteChanged() - signal
    def self(self):
        '''static KGlobalSettings KGlobalSettings.self()'''
        return KGlobalSettings()
    def emitChange(self, changeType, arg = 0):
        '''static void KGlobalSettings.emitChange(KGlobalSettings.ChangeType changeType, int arg = 0)'''
    def createApplicationPalette(self, config = KSharedConfigPtr()):
        '''static QPalette KGlobalSettings.createApplicationPalette(KSharedConfigPtr config = KSharedConfigPtr())'''
        return QPalette()
    def buttonLayout(self):
        '''static int KGlobalSettings.buttonLayout()'''
        return int()
    def opaqueResize(self):
        '''static bool KGlobalSettings.opaqueResize()'''
        return bool()
    def showFilePreview(self):
        '''static KUrl KGlobalSettings.showFilePreview()'''
        return KUrl()
    def graphicEffectsLevelDefault(self):
        '''static KGlobalSettings.GraphicEffects KGlobalSettings.graphicEffectsLevelDefault()'''
        return KGlobalSettings.GraphicEffects()
    def graphicEffectsLevel(self):
        '''static KGlobalSettings.GraphicEffects KGlobalSettings.graphicEffectsLevel()'''
        return KGlobalSettings.GraphicEffects()
    def showIconsOnPushButtons(self):
        '''static bool KGlobalSettings.showIconsOnPushButtons()'''
        return bool()
    def desktopGeometry(self, point):
        '''static QRect KGlobalSettings.desktopGeometry(QPoint point)'''
        return QRect()
    def desktopGeometry(self, w):
        '''static QRect KGlobalSettings.desktopGeometry(QWidget w)'''
        return QRect()
    def splashScreenDesktopGeometry(self):
        '''static QRect KGlobalSettings.splashScreenDesktopGeometry()'''
        return QRect()
    def wheelMouseZooms(self):
        '''static bool KGlobalSettings.wheelMouseZooms()'''
        return bool()
    def isMultiHead(self):
        '''static bool KGlobalSettings.isMultiHead()'''
        return bool()
    def smallestReadableFont(self):
        '''static QFont KGlobalSettings.smallestReadableFont()'''
        return QFont()
    def largeFont(self, text = QString()):
        '''static QFont KGlobalSettings.largeFont(QString text = QString())'''
        return QFont()
    def taskbarFont(self):
        '''static QFont KGlobalSettings.taskbarFont()'''
        return QFont()
    def windowTitleFont(self):
        '''static QFont KGlobalSettings.windowTitleFont()'''
        return QFont()
    def menuFont(self):
        '''static QFont KGlobalSettings.menuFont()'''
        return QFont()
    def toolBarFont(self):
        '''static QFont KGlobalSettings.toolBarFont()'''
        return QFont()
    def fixedFont(self):
        '''static QFont KGlobalSettings.fixedFont()'''
        return QFont()
    def generalFont(self):
        '''static QFont KGlobalSettings.generalFont()'''
        return QFont()
    def allowDefaultBackgroundImages(self):
        '''static bool KGlobalSettings.allowDefaultBackgroundImages()'''
        return bool()
    def shadeSortColumn(self):
        '''static bool KGlobalSettings.shadeSortColumn()'''
        return bool()
    def contrastF(self, config = KSharedConfigPtr()):
        '''static float KGlobalSettings.contrastF(KSharedConfigPtr config = KSharedConfigPtr())'''
        return float()
    def contrast(self):
        '''static int KGlobalSettings.contrast()'''
        return int()
    def activeTextColor(self):
        '''static QColor KGlobalSettings.activeTextColor()'''
        return QColor()
    def activeTitleColor(self):
        '''static QColor KGlobalSettings.activeTitleColor()'''
        return QColor()
    def inactiveTextColor(self):
        '''static QColor KGlobalSettings.inactiveTextColor()'''
        return QColor()
    def inactiveTitleColor(self):
        '''static QColor KGlobalSettings.inactiveTitleColor()'''
        return QColor()
    def picturesPath(self):
        '''static QString KGlobalSettings.picturesPath()'''
        return QString()
    def downloadPath(self):
        '''static QString KGlobalSettings.downloadPath()'''
        return QString()
    def videosPath(self):
        '''static QString KGlobalSettings.videosPath()'''
        return QString()
    def musicPath(self):
        '''static QString KGlobalSettings.musicPath()'''
        return QString()
    def documentPath(self):
        '''static QString KGlobalSettings.documentPath()'''
        return QString()
    def autostartPath(self):
        '''static QString KGlobalSettings.autostartPath()'''
        return QString()
    def desktopPath(self):
        '''static QString KGlobalSettings.desktopPath()'''
        return QString()
    def mouseSettings(self):
        '''static KGlobalSettings.KMouseSettings KGlobalSettings.mouseSettings()'''
        return KGlobalSettings.KMouseSettings()
    def completionMode(self):
        '''static KGlobalSettings.Completion KGlobalSettings.completionMode()'''
        return KGlobalSettings.Completion()
    def showContextMenusOnPress(self):
        '''static bool KGlobalSettings.showContextMenusOnPress()'''
        return bool()
    def contextMenuKey(self):
        '''static int KGlobalSettings.contextMenuKey()'''
        return int()
    def autoSelectDelay(self):
        '''static int KGlobalSettings.autoSelectDelay()'''
        return int()
    def changeCursorOverIcon(self):
        '''static bool KGlobalSettings.changeCursorOverIcon()'''
        return bool()
    def insertTearOffHandle(self):
        '''static KGlobalSettings.TearOffHandle KGlobalSettings.insertTearOffHandle()'''
        return KGlobalSettings.TearOffHandle()
    def smoothScroll(self):
        '''static bool KGlobalSettings.smoothScroll()'''
        return bool()
    def singleClick(self):
        '''static bool KGlobalSettings.singleClick()'''
        return bool()
    def dndEventDelay(self):
        '''static int KGlobalSettings.dndEventDelay()'''
        return int()
    class GraphicEffects():
        """"""
        def __init__(self):
            '''KGlobalSettings.GraphicEffects KGlobalSettings.GraphicEffects.__init__()'''
            return KGlobalSettings.GraphicEffects()
        def __init__(self):
            '''int KGlobalSettings.GraphicEffects.__init__()'''
            return int()
        def __init__(self):
            '''void KGlobalSettings.GraphicEffects.__init__()'''
        def __bool__(self):
            '''int KGlobalSettings.GraphicEffects.__bool__()'''
            return int()
        def __ne__(self, f):
            '''bool KGlobalSettings.GraphicEffects.__ne__(KGlobalSettings.GraphicEffects f)'''
            return bool()
        def __eq__(self, f):
            '''bool KGlobalSettings.GraphicEffects.__eq__(KGlobalSettings.GraphicEffects f)'''
            return bool()
        def __invert__(self):
            '''KGlobalSettings.GraphicEffects KGlobalSettings.GraphicEffects.__invert__()'''
            return KGlobalSettings.GraphicEffects()
        def __and__(self, mask):
            '''KGlobalSettings.GraphicEffects KGlobalSettings.GraphicEffects.__and__(int mask)'''
            return KGlobalSettings.GraphicEffects()
        def __xor__(self, f):
            '''KGlobalSettings.GraphicEffects KGlobalSettings.GraphicEffects.__xor__(KGlobalSettings.GraphicEffects f)'''
            return KGlobalSettings.GraphicEffects()
        def __xor__(self, f):
            '''KGlobalSettings.GraphicEffects KGlobalSettings.GraphicEffects.__xor__(int f)'''
            return KGlobalSettings.GraphicEffects()
        def __or__(self, f):
            '''KGlobalSettings.GraphicEffects KGlobalSettings.GraphicEffects.__or__(KGlobalSettings.GraphicEffects f)'''
            return KGlobalSettings.GraphicEffects()
        def __or__(self, f):
            '''KGlobalSettings.GraphicEffects KGlobalSettings.GraphicEffects.__or__(int f)'''
            return KGlobalSettings.GraphicEffects()
        def __int__(self):
            '''int KGlobalSettings.GraphicEffects.__int__()'''
            return int()
        def __ixor__(self, f):
            '''KGlobalSettings.GraphicEffects KGlobalSettings.GraphicEffects.__ixor__(KGlobalSettings.GraphicEffects f)'''
            return KGlobalSettings.GraphicEffects()
        def __ior__(self, f):
            '''KGlobalSettings.GraphicEffects KGlobalSettings.GraphicEffects.__ior__(KGlobalSettings.GraphicEffects f)'''
            return KGlobalSettings.GraphicEffects()
        def __iand__(self, mask):
            '''KGlobalSettings.GraphicEffects KGlobalSettings.GraphicEffects.__iand__(int mask)'''
            return KGlobalSettings.GraphicEffects()
    class ActivateOptions():
        """"""
        def __init__(self):
            '''KGlobalSettings.ActivateOptions KGlobalSettings.ActivateOptions.__init__()'''
            return KGlobalSettings.ActivateOptions()
        def __init__(self):
            '''int KGlobalSettings.ActivateOptions.__init__()'''
            return int()
        def __init__(self):
            '''void KGlobalSettings.ActivateOptions.__init__()'''
        def __bool__(self):
            '''int KGlobalSettings.ActivateOptions.__bool__()'''
            return int()
        def __ne__(self, f):
            '''bool KGlobalSettings.ActivateOptions.__ne__(KGlobalSettings.ActivateOptions f)'''
            return bool()
        def __eq__(self, f):
            '''bool KGlobalSettings.ActivateOptions.__eq__(KGlobalSettings.ActivateOptions f)'''
            return bool()
        def __invert__(self):
            '''KGlobalSettings.ActivateOptions KGlobalSettings.ActivateOptions.__invert__()'''
            return KGlobalSettings.ActivateOptions()
        def __and__(self, mask):
            '''KGlobalSettings.ActivateOptions KGlobalSettings.ActivateOptions.__and__(int mask)'''
            return KGlobalSettings.ActivateOptions()
        def __xor__(self, f):
            '''KGlobalSettings.ActivateOptions KGlobalSettings.ActivateOptions.__xor__(KGlobalSettings.ActivateOptions f)'''
            return KGlobalSettings.ActivateOptions()
        def __xor__(self, f):
            '''KGlobalSettings.ActivateOptions KGlobalSettings.ActivateOptions.__xor__(int f)'''
            return KGlobalSettings.ActivateOptions()
        def __or__(self, f):
            '''KGlobalSettings.ActivateOptions KGlobalSettings.ActivateOptions.__or__(KGlobalSettings.ActivateOptions f)'''
            return KGlobalSettings.ActivateOptions()
        def __or__(self, f):
            '''KGlobalSettings.ActivateOptions KGlobalSettings.ActivateOptions.__or__(int f)'''
            return KGlobalSettings.ActivateOptions()
        def __int__(self):
            '''int KGlobalSettings.ActivateOptions.__int__()'''
            return int()
        def __ixor__(self, f):
            '''KGlobalSettings.ActivateOptions KGlobalSettings.ActivateOptions.__ixor__(KGlobalSettings.ActivateOptions f)'''
            return KGlobalSettings.ActivateOptions()
        def __ior__(self, f):
            '''KGlobalSettings.ActivateOptions KGlobalSettings.ActivateOptions.__ior__(KGlobalSettings.ActivateOptions f)'''
            return KGlobalSettings.ActivateOptions()
        def __iand__(self, mask):
            '''KGlobalSettings.ActivateOptions KGlobalSettings.ActivateOptions.__iand__(int mask)'''
            return KGlobalSettings.ActivateOptions()
    class KMouseSettings():
        """"""
        RightHanded = None # int - member
        LeftHanded = None # int - member
        handed = None # int - member
        def __init__(self):
            '''void KGlobalSettings.KMouseSettings.__init__()'''
        def __init__(self):
            '''KGlobalSettings.KMouseSettings KGlobalSettings.KMouseSettings.__init__()'''
            return KGlobalSettings.KMouseSettings()


class KGlobalShortcutInfo(QObject):
    """"""
    def __init__(self):
        '''void KGlobalShortcutInfo.__init__()'''
    def __init__(self, rhs):
        '''void KGlobalShortcutInfo.__init__(KGlobalShortcutInfo rhs)'''
    def uniqueName(self):
        '''QString KGlobalShortcutInfo.uniqueName()'''
        return QString()
    def keys(self):
        '''list-of-QKeySequence KGlobalShortcutInfo.keys()'''
        return [QKeySequence()]
    def friendlyName(self):
        '''QString KGlobalShortcutInfo.friendlyName()'''
        return QString()
    def defaultKeys(self):
        '''list-of-QKeySequence KGlobalShortcutInfo.defaultKeys()'''
        return [QKeySequence()]
    def componentUniqueName(self):
        '''QString KGlobalShortcutInfo.componentUniqueName()'''
        return QString()
    def componentFriendlyName(self):
        '''QString KGlobalShortcutInfo.componentFriendlyName()'''
        return QString()
    def contextUniqueName(self):
        '''QString KGlobalShortcutInfo.contextUniqueName()'''
        return QString()
    def contextFriendlyName(self):
        '''QString KGlobalShortcutInfo.contextFriendlyName()'''
        return QString()


class KGuiItem():
    """"""
    def __init__(self):
        '''void KGuiItem.__init__()'''
    def __init__(self, text, iconName = QString(), toolTip = QString(), whatsThis = QString()):
        '''void KGuiItem.__init__(QString text, QString iconName = QString(), QString toolTip = QString(), QString whatsThis = QString())'''
    def __init__(self, text, icon, toolTip = QString(), whatsThis = QString()):
        '''void KGuiItem.__init__(QString text, KIcon icon, QString toolTip = QString(), QString whatsThis = QString())'''
    def __init__(self, rhs):
        '''void KGuiItem.__init__(KGuiItem rhs)'''
    def setEnabled(self, enable):
        '''void KGuiItem.setEnabled(bool enable)'''
    def setWhatsThis(self, whatsThis):
        '''void KGuiItem.setWhatsThis(QString whatsThis)'''
    def setToolTip(self, tooltip):
        '''void KGuiItem.setToolTip(QString tooltip)'''
    def setIconName(self, iconName):
        '''void KGuiItem.setIconName(QString iconName)'''
    def setIcon(self, iconset):
        '''void KGuiItem.setIcon(KIcon iconset)'''
    def setText(self, text):
        '''void KGuiItem.setText(QString text)'''
    def hasIconSet(self):
        '''bool KGuiItem.hasIconSet()'''
        return bool()
    def hasIcon(self):
        '''bool KGuiItem.hasIcon()'''
        return bool()
    def isEnabled(self):
        '''bool KGuiItem.isEnabled()'''
        return bool()
    def whatsThis(self):
        '''QString KGuiItem.whatsThis()'''
        return QString()
    def toolTip(self):
        '''QString KGuiItem.toolTip()'''
        return QString()
    def iconName(self):
        '''QString KGuiItem.iconName()'''
        return QString()
    def icon(self):
        '''KIcon KGuiItem.icon()'''
        return KIcon()
    def plainText(self):
        '''QString KGuiItem.plainText()'''
        return QString()
    def text(self):
        '''QString KGuiItem.text()'''
        return QString()


class KHBox(QFrame):
    """"""
    def __init__(self, parent = None):
        '''void KHBox.__init__(QWidget parent = None)'''
    def __init__(self, vertical, parent):
        '''void KHBox.__init__(bool vertical, QWidget parent)'''
    def childEvent(self, ev):
        '''void KHBox.childEvent(QChildEvent ev)'''
    def minimumSizeHint(self):
        '''QSize KHBox.minimumSizeHint()'''
        return QSize()
    def sizeHint(self):
        '''QSize KHBox.sizeHint()'''
        return QSize()
    def setStretchFactor(self, widget, stretch):
        '''void KHBox.setStretchFactor(QWidget widget, int stretch)'''
    def setSpacing(self, space):
        '''void KHBox.setSpacing(int space)'''
    def setMargin(self, margin):
        '''void KHBox.setMargin(int margin)'''


class KHelpMenu(QObject):
    """"""
    # Enum KHelpMenu.MenuId
    menuHelpContents = 0
    menuWhatsThis = 0
    menuAboutApp = 0
    menuAboutKDE = 0
    menuReportBug = 0
    menuSwitchLanguage = 0

    def __init__(self, parent = None, aboutAppText = QString(), showWhatsThis = True):
        '''void KHelpMenu.__init__(QWidget parent = None, QString aboutAppText = QString(), bool showWhatsThis = True)'''
    def __init__(self, parent, aboutData, showWhatsThis = True, actions = None):
        '''void KHelpMenu.__init__(QWidget parent, KAboutData aboutData, bool showWhatsThis = True, KActionCollection actions = None)'''
    showAboutApplication = pyqtSignal() # void showAboutApplication() - signal
    def switchApplicationLanguage(self):
        '''void KHelpMenu.switchApplicationLanguage()'''
    def reportBug(self):
        '''void KHelpMenu.reportBug()'''
    def aboutKDE(self):
        '''void KHelpMenu.aboutKDE()'''
    def aboutApplication(self):
        '''void KHelpMenu.aboutApplication()'''
    def contextHelpActivated(self):
        '''void KHelpMenu.contextHelpActivated()'''
    def appHelpActivated(self):
        '''void KHelpMenu.appHelpActivated()'''
    def action(self, id):
        '''QAction KHelpMenu.action(KHelpMenu.MenuId id)'''
        return QAction()
    def menu(self):
        '''KMenu KHelpMenu.menu()'''
        return KMenu()


class KHistoryComboBox(KComboBox):
    """"""
    def __init__(self, parent = None):
        '''void KHistoryComboBox.__init__(QWidget parent = None)'''
    def __init__(self, useCompletion, parent = None):
        '''void KHistoryComboBox.__init__(bool useCompletion, QWidget parent = None)'''
    def useCompletion(self):
        '''bool KHistoryComboBox.useCompletion()'''
        return bool()
    def insertItems(self, items):
        '''void KHistoryComboBox.insertItems(QStringList items)'''
    def wheelEvent(self, ev):
        '''void KHistoryComboBox.wheelEvent(QWheelEvent ev)'''
    def keyPressEvent(self):
        '''QKeyEvent KHistoryComboBox.keyPressEvent()'''
        return QKeyEvent()
    cleared = pyqtSignal() # void cleared() - signal
    def clearHistory(self):
        '''void KHistoryComboBox.clearHistory()'''
    def addToHistory(self, item):
        '''void KHistoryComboBox.addToHistory(QString item)'''
    def reset(self):
        '''void KHistoryComboBox.reset()'''
    def pixmapProvider(self):
        '''KPixmapProvider KHistoryComboBox.pixmapProvider()'''
        return KPixmapProvider()
    def setPixmapProvider(self, prov):
        '''void KHistoryComboBox.setPixmapProvider(KPixmapProvider prov)'''
    def removeFromHistory(self, item):
        '''bool KHistoryComboBox.removeFromHistory(QString item)'''
        return bool()
    def historyItems(self):
        '''QStringList KHistoryComboBox.historyItems()'''
        return QStringList()
    def setHistoryItems(self, items):
        '''void KHistoryComboBox.setHistoryItems(QStringList items)'''
    def setHistoryItems(self, items, setCompletionList):
        '''void KHistoryComboBox.setHistoryItems(QStringList items, bool setCompletionList)'''


class KXYSelector(QWidget):
    """"""
    def __init__(self, parent = None):
        '''void KXYSelector.__init__(QWidget parent = None)'''
    def valuesFromPosition(self, x, y, xVal, yVal):
        '''void KXYSelector.valuesFromPosition(int x, int y, int xVal, int yVal)'''
    def wheelEvent(self):
        '''QWheelEvent KXYSelector.wheelEvent()'''
        return QWheelEvent()
    def mouseMoveEvent(self, e):
        '''void KXYSelector.mouseMoveEvent(QMouseEvent e)'''
    def mousePressEvent(self, e):
        '''void KXYSelector.mousePressEvent(QMouseEvent e)'''
    def paintEvent(self, e):
        '''void KXYSelector.paintEvent(QPaintEvent e)'''
    def drawMarker(self, p, xp, yp):
        '''void KXYSelector.drawMarker(QPainter p, int xp, int yp)'''
    def drawContents(self):
        '''QPainter KXYSelector.drawContents()'''
        return QPainter()
    valueChanged = pyqtSignal() # void valueChanged(int,int) - signal
    def minimumSizeHint(self):
        '''QSize KXYSelector.minimumSizeHint()'''
        return QSize()
    def contentsRect(self):
        '''QRect KXYSelector.contentsRect()'''
        return QRect()
    def yValue(self):
        '''int KXYSelector.yValue()'''
        return int()
    def xValue(self):
        '''int KXYSelector.xValue()'''
        return int()
    def setMarkerColor(self, col):
        '''void KXYSelector.setMarkerColor(QColor col)'''
    def setRange(self, minX, minY, maxX, maxY):
        '''void KXYSelector.setRange(int minX, int minY, int maxX, int maxY)'''
    def setYValue(self, yPos):
        '''void KXYSelector.setYValue(int yPos)'''
    def setXValue(self, xPos):
        '''void KXYSelector.setXValue(int xPos)'''
    def setValues(self, xPos, yPos):
        '''void KXYSelector.setValues(int xPos, int yPos)'''


class KHueSaturationSelector(KXYSelector):
    """"""
    def __init__(self, parent = None):
        '''void KHueSaturationSelector.__init__(QWidget parent = None)'''
    def drawContents(self, painter):
        '''void KHueSaturationSelector.drawContents(QPainter painter)'''
    def resizeEvent(self):
        '''QResizeEvent KHueSaturationSelector.resizeEvent()'''
        return QResizeEvent()
    def drawPalette(self, pixmap):
        '''void KHueSaturationSelector.drawPalette(QPixmap pixmap)'''
    def updateContents(self):
        '''void KHueSaturationSelector.updateContents()'''
    def setColorValue(self, colorValue):
        '''void KHueSaturationSelector.setColorValue(int colorValue)'''
    def colorValue(self):
        '''int KHueSaturationSelector.colorValue()'''
        return int()
    def setSaturation(self, saturation):
        '''void KHueSaturationSelector.setSaturation(int saturation)'''
    def saturation(self):
        '''int KHueSaturationSelector.saturation()'''
        return int()
    def setHue(self, hue):
        '''void KHueSaturationSelector.setHue(int hue)'''
    def hue(self):
        '''int KHueSaturationSelector.hue()'''
        return int()
    def chooserMode(self):
        '''KColorChooserMode KHueSaturationSelector.chooserMode()'''
        return KColorChooserMode()
    def setChooserMode(self, chooserMode):
        '''void KHueSaturationSelector.setChooserMode(KColorChooserMode chooserMode)'''


class KIcon(QIcon):
    """"""
    def __init__(self, iconName, iconLoader, overlays):
        '''void KIcon.__init__(QString iconName, KIconLoader iconLoader, QStringList overlays)'''
    def __init__(self, iconName, iconLoader):
        '''void KIcon.__init__(QString iconName, KIconLoader iconLoader)'''
    def __init__(self, iconName):
        '''void KIcon.__init__(QString iconName)'''
    def __init__(self, copy):
        '''void KIcon.__init__(QIcon copy)'''
    def __init__(self):
        '''void KIcon.__init__()'''
    def __init__(self):
        '''KIcon KIcon.__init__()'''
        return KIcon()


class KPixmapCache():
    """"""
    # Enum KPixmapCache.RemoveStrategy
    RemoveOldest = 0
    RemoveSeldomUsed = 0
    RemoveLeastRecentlyUsed = 0

    def __init__(self, name):
        '''void KPixmapCache.__init__(QString name)'''
    def recreateCacheFiles(self):
        '''bool KPixmapCache.recreateCacheFiles()'''
        return bool()
    def setValid(self, valid):
        '''void KPixmapCache.setValid(bool valid)'''
    def writeCustomIndexHeader(self, stream):
        '''void KPixmapCache.writeCustomIndexHeader(QDataStream stream)'''
    def loadCustomIndexHeader(self, stream):
        '''bool KPixmapCache.loadCustomIndexHeader(QDataStream stream)'''
        return bool()
    def writeCustomData(self, stream):
        '''bool KPixmapCache.writeCustomData(QDataStream stream)'''
        return bool()
    def loadCustomData(self, stream):
        '''bool KPixmapCache.loadCustomData(QDataStream stream)'''
        return bool()
    def ensureInited(self):
        '''void KPixmapCache.ensureInited()'''
    def removeEntries(self, newsize = 0):
        '''void KPixmapCache.removeEntries(int newsize = 0)'''
    def discard(self):
        '''void KPixmapCache.discard()'''
    def deleteCache(self, name):
        '''static void KPixmapCache.deleteCache(QString name)'''
    def isValid(self):
        '''bool KPixmapCache.isValid()'''
        return bool()
    def isEnabled(self):
        '''bool KPixmapCache.isEnabled()'''
        return bool()
    def setRemoveEntryStrategy(self, strategy):
        '''void KPixmapCache.setRemoveEntryStrategy(KPixmapCache.RemoveStrategy strategy)'''
    def removeEntryStrategy(self):
        '''KPixmapCache.RemoveStrategy KPixmapCache.removeEntryStrategy()'''
        return KPixmapCache.RemoveStrategy()
    def setCacheLimit(self, kbytes):
        '''void KPixmapCache.setCacheLimit(int kbytes)'''
    def cacheLimit(self):
        '''int KPixmapCache.cacheLimit()'''
        return int()
    def size(self):
        '''int KPixmapCache.size()'''
        return int()
    def useQPixmapCache(self):
        '''bool KPixmapCache.useQPixmapCache()'''
        return bool()
    def setUseQPixmapCache(self, use):
        '''void KPixmapCache.setUseQPixmapCache(bool use)'''
    def setTimestamp(self, time):
        '''void KPixmapCache.setTimestamp(int time)'''
    def timestamp(self):
        '''int KPixmapCache.timestamp()'''
        return int()
    def loadFromSvg(self, filename, size = QSize()):
        '''QPixmap KPixmapCache.loadFromSvg(QString filename, QSize size = QSize())'''
        return QPixmap()
    def loadFromFile(self, filename):
        '''QPixmap KPixmapCache.loadFromFile(QString filename)'''
        return QPixmap()
    def insert(self, key, pix):
        '''void KPixmapCache.insert(QString key, QPixmap pix)'''
    def find(self, key, pix):
        '''bool KPixmapCache.find(QString key, QPixmap pix)'''
        return bool()


class KIconCache(KPixmapCache):
    """"""
    def __init__(self):
        '''void KIconCache.__init__()'''
    def mostRecentMTime(self, dirNames):
        '''int KIconCache.mostRecentMTime(list-of-QString dirNames)'''
        return int()
    def existingIconThemeDirs(self, themeNames):
        '''list-of-QString KIconCache.existingIconThemeDirs(QStringList themeNames)'''
        return [QString()]
    def writeCustomData(self, stream):
        '''bool KIconCache.writeCustomData(QDataStream stream)'''
        return bool()
    def loadCustomData(self, stream):
        '''bool KIconCache.loadCustomData(QDataStream stream)'''
        return bool()
    def writeCustomIndexHeader(self, stream):
        '''void KIconCache.writeCustomIndexHeader(QDataStream stream)'''
    def loadCustomIndexHeader(self, stream):
        '''bool KIconCache.loadCustomIndexHeader(QDataStream stream)'''
        return bool()
    def setThemeInfo(self, themes):
        '''void KIconCache.setThemeInfo(list-of-KIconTheme themes)'''
    def defaultIconSize(self, group):
        '''int KIconCache.defaultIconSize(KIconLoader.Group group)'''
        return int()
    def deleteCache(self):
        '''static void KIconCache.deleteCache()'''
    def insert(self, key, pix, path):
        '''void KIconCache.insert(QString key, QPixmap pix, QString path)'''
    def insert(self, key, pix):
        '''void KIconCache.insert(QString key, QPixmap pix)'''
    def find(self, key, pix, path):
        '''bool KIconCache.find(QString key, QPixmap pix, QString path)'''
        return bool()
    def find(self, key, pix):
        '''bool KIconCache.find(QString key, QPixmap pix)'''
        return bool()


class KIconEffect():
    """"""
    # Enum KIconEffect.Effects
    NoEffect = 0
    ToGray = 0
    Colorize = 0
    ToGamma = 0
    DeSaturate = 0
    ToMonochrome = 0
    LastEffect = 0

    def __init__(self):
        '''void KIconEffect.__init__()'''
    def overlay(self, src, overlay):
        '''static void KIconEffect.overlay(QImage src, QImage overlay)'''
    def semiTransparent(self, image):
        '''static void KIconEffect.semiTransparent(QImage image)'''
    def semiTransparent(self, pixmap):
        '''static void KIconEffect.semiTransparent(QPixmap pixmap)'''
    def toGamma(self, image, value):
        '''static void KIconEffect.toGamma(QImage image, float value)'''
    def deSaturate(self, image, value):
        '''static void KIconEffect.deSaturate(QImage image, float value)'''
    def toMonochrome(self, image, black, white, value):
        '''static void KIconEffect.toMonochrome(QImage image, QColor black, QColor white, float value)'''
    def colorize(self, image, col, value):
        '''static void KIconEffect.colorize(QImage image, QColor col, float value)'''
    def toGray(self, image, value):
        '''static void KIconEffect.toGray(QImage image, float value)'''
    def doublePixels(self, src):
        '''QImage KIconEffect.doublePixels(QImage src)'''
        return QImage()
    def apply(self, src, group, state):
        '''QImage KIconEffect.apply(QImage src, int group, int state)'''
        return QImage()
    def apply(self, src, effect, value, rgb, trans):
        '''QImage KIconEffect.apply(QImage src, int effect, float value, QColor rgb, bool trans)'''
        return QImage()
    def apply(self, src, effect, value, rgb, rgb2, trans):
        '''QImage KIconEffect.apply(QImage src, int effect, float value, QColor rgb, QColor rgb2, bool trans)'''
        return QImage()
    def apply(self, src, group, state):
        '''QPixmap KIconEffect.apply(QPixmap src, int group, int state)'''
        return QPixmap()
    def apply(self, src, effect, value, rgb, trans):
        '''QPixmap KIconEffect.apply(QPixmap src, int effect, float value, QColor rgb, bool trans)'''
        return QPixmap()
    def apply(self, src, effect, value, rgb, rgb2, trans):
        '''QPixmap KIconEffect.apply(QPixmap src, int effect, float value, QColor rgb, QColor rgb2, bool trans)'''
        return QPixmap()
    def fingerprint(self, group, state):
        '''QString KIconEffect.fingerprint(int group, int state)'''
        return QString()
    def hasEffect(self, group, state):
        '''bool KIconEffect.hasEffect(int group, int state)'''
        return bool()
    def init(self):
        '''void KIconEffect.init()'''


class KIconLoader(QObject):
    """"""
    # Enum KIconLoader.States
    DefaultState = 0
    ActiveState = 0
    DisabledState = 0
    LastState = 0

    # Enum KIconLoader.StdSizes
    SizeSmall = 0
    SizeSmallMedium = 0
    SizeMedium = 0
    SizeLarge = 0
    SizeHuge = 0
    SizeEnormous = 0

    # Enum KIconLoader.Group
    NoGroup = 0
    Desktop = 0
    FirstGroup = 0
    Toolbar = 0
    MainToolbar = 0
    Small = 0
    Panel = 0
    Dialog = 0
    LastGroup = 0
    User = 0

    # Enum KIconLoader.MatchType
    MatchExact = 0
    MatchBest = 0

    # Enum KIconLoader.Type
    Fixed = 0
    Scalable = 0
    Threshold = 0

    # Enum KIconLoader.Context
    Any = 0
    Action = 0
    Application = 0
    Device = 0
    FileSystem = 0
    MimeType = 0
    Animation = 0
    Category = 0
    Emblem = 0
    Emote = 0
    International = 0
    Place = 0
    StatusIcon = 0

    def __init__(self, appname = QString(), dirs = None, parent = None):
        '''void KIconLoader.__init__(QString appname = QString(), KStandardDirs dirs = None, QObject parent = None)'''
    def __init__(self, componentData, parent = None):
        '''void KIconLoader.__init__(KComponentData componentData, QObject parent = None)'''
    def drawOverlays(self, overlays, pixmap, group, state = None):
        '''void KIconLoader.drawOverlays(QStringList overlays, QPixmap pixmap, KIconLoader.Group group, int state = KIconLoader.DefaultState)'''
    iconLoaderSettingsChanged = pyqtSignal() # void iconLoaderSettingsChanged() - signal
    def newIconLoader(self):
        '''void KIconLoader.newIconLoader()'''
    def extraDesktopThemesAdded(self):
        '''bool KIconLoader.extraDesktopThemesAdded()'''
        return bool()
    def addExtraDesktopThemes(self):
        '''void KIconLoader.addExtraDesktopThemes()'''
    def unknown(self):
        '''static QPixmap KIconLoader.unknown()'''
        return QPixmap()
    def reconfigure(self, _appname, _dirs):
        '''void KIconLoader.reconfigure(QString _appname, KStandardDirs _dirs)'''
    def iconEffect(self):
        '''KIconEffect KIconLoader.iconEffect()'''
        return KIconEffect()
    def theme(self):
        '''KIconTheme KIconLoader.theme()'''
        return KIconTheme()
    def queryIconsByDir(self, iconsDir):
        '''QStringList KIconLoader.queryIconsByDir(QString iconsDir)'''
        return QStringList()
    def iconPath(self, name, group_or_size, canReturnNull = False):
        '''QString KIconLoader.iconPath(QString name, int group_or_size, bool canReturnNull = False)'''
        return QString()
    def loadMimeTypeIcon(self, iconName, group, size = 0, state = None, overlays = QStringList(), path_store = None):
        '''QPixmap KIconLoader.loadMimeTypeIcon(QString iconName, KIconLoader.Group group, int size = 0, int state = KIconLoader.DefaultState, QStringList overlays = QStringList(), QString path_store = None)'''
        return QPixmap()
    def loadIcon(self, name, group, size = 0, state = None, overlays = QStringList(), path_store = None, canReturnNull = False):
        '''QPixmap KIconLoader.loadIcon(QString name, KIconLoader.Group group, int size = 0, int state = KIconLoader.DefaultState, QStringList overlays = QStringList(), QString path_store = None, bool canReturnNull = False)'''
        return QPixmap()
    def addAppDir(self, appname):
        '''void KIconLoader.addAppDir(QString appname)'''
    def global_(self):
        '''static KIconLoader KIconLoader.global_()'''
        return KIconLoader()


class KIconTheme():
    """"""
    # Enum KIconTheme.ContextMenus
    TextEditor = 0
    ReadOnlyText = 0

    def __init__(self, name, appName = QString()):
        '''void KIconTheme.__init__(QString name, QString appName = QString())'''
    def assignIconsToContextMenu(self, type, actions):
        '''static void KIconTheme.assignIconsToContextMenu(KIconTheme.ContextMenus type, list-of-QAction actions)'''
    def defaultThemeName(self):
        '''static QString KIconTheme.defaultThemeName()'''
        return QString()
    def reconfigure(self):
        '''static void KIconTheme.reconfigure()'''
    def current(self):
        '''static QString KIconTheme.current()'''
        return QString()
    def list(self):
        '''static QStringList KIconTheme.list()'''
        return QStringList()
    def depth(self):
        '''int KIconTheme.depth()'''
        return int()
    def isHidden(self):
        '''bool KIconTheme.isHidden()'''
        return bool()
    def isValid(self):
        '''bool KIconTheme.isValid()'''
        return bool()
    def inherits(self):
        '''QStringList KIconTheme.inherits()'''
        return QStringList()
    def dir(self):
        '''QString KIconTheme.dir()'''
        return QString()
    def screenshot(self):
        '''QString KIconTheme.screenshot()'''
        return QString()
    def example(self):
        '''QString KIconTheme.example()'''
        return QString()
    def description(self):
        '''QString KIconTheme.description()'''
        return QString()
    def internalName(self):
        '''QString KIconTheme.internalName()'''
        return QString()
    def name(self):
        '''QString KIconTheme.name()'''
        return QString()


class KInputDialog():
    """"""
    def getDouble(self, caption, label, value = 0, minValue = None, maxValue = None, step = None, decimals = 1, ok = None, parent = None):
        '''static float KInputDialog.getDouble(QString caption, QString label, float value = 0, float minValue = -DBL_MAX, float maxValue = DBL_MAX, float step = 0.1, int decimals = 1, bool ok, QWidget parent = None)'''
        return float()
    def getItemList(self, caption, label, list = QStringList(), select = QStringList(), multiple = False, ok = None, parent = None):
        '''static QStringList KInputDialog.getItemList(QString caption, QString label, QStringList list = QStringList(), QStringList select = QStringList(), bool multiple = False, bool ok, QWidget parent = None)'''
        return QStringList()
    def getItem(self, caption, label, list, current = 0, editable = False, ok = None, parent = None):
        '''static QString KInputDialog.getItem(QString caption, QString label, QStringList list, int current = 0, bool editable = False, bool ok, QWidget parent = None)'''
        return QString()
    def getInteger(self, caption, label, value = 0, minValue = None, maxValue = None, step = 1, base = 10, ok = None, parent = None):
        '''static int KInputDialog.getInteger(QString caption, QString label, int value = 0, int minValue = INT_MIN, int maxValue = INT_MAX, int step = 1, int base = 10, bool ok, QWidget parent = None)'''
        return int()
    def getMultiLineText(self, caption, label, value = QString(), ok = None, parent = None):
        '''static QString KInputDialog.getMultiLineText(QString caption, QString label, QString value = QString(), bool ok, QWidget parent = None)'''
        return QString()
    def getText(self, caption, label, value = QString(), ok = None, parent = None, validator = None, mask = QString(), whatsThis = QString(), completionList = QStringList()):
        '''static QString KInputDialog.getText(QString caption, QString label, QString value = QString(), bool ok, QWidget parent = None, QValidator validator = None, QString mask = QString(), QString whatsThis = QString(), QStringList completionList = QStringList())'''
        return QString()


class KKeySequenceWidget(QWidget):
    """"""
    # Enum KKeySequenceWidget.ShortcutType
    __kdevpythondocumentation_builtin_None = 0
    LocalShortcuts = 0
    StandardShortcuts = 0
    GlobalShortcuts = 0

    # Enum KKeySequenceWidget.Validation
    Validate = 0
    NoValidate = 0

    def __init__(self, parent = None):
        '''void KKeySequenceWidget.__init__(QWidget parent = None)'''
    def applyStealShortcut(self):
        '''void KKeySequenceWidget.applyStealShortcut()'''
    def clearKeySequence(self):
        '''void KKeySequenceWidget.clearKeySequence()'''
    def setKeySequence(self, seq, val = None):
        '''void KKeySequenceWidget.setKeySequence(QKeySequence seq, KKeySequenceWidget.Validation val = KKeySequenceWidget.NoValidate)'''
    def captureKeySequence(self):
        '''void KKeySequenceWidget.captureKeySequence()'''
    stealShortcut = pyqtSignal() # void stealShortcut(const QKeySequenceamp;,KAction *) - signal
    keySequenceChanged = pyqtSignal() # void keySequenceChanged(const QKeySequenceamp;) - signal
    def setComponentName(self, componentName):
        '''void KKeySequenceWidget.setComponentName(QString componentName)'''
    def setCheckActionList(self, checkList):
        '''void KKeySequenceWidget.setCheckActionList(list-of-QAction checkList)'''
    def setCheckActionCollections(self, actionCollections):
        '''void KKeySequenceWidget.setCheckActionCollections(list-of-KActionCollection actionCollections)'''
    def keySequence(self):
        '''QKeySequence KKeySequenceWidget.keySequence()'''
        return QKeySequence()
    def isKeySequenceAvailable(self, seq):
        '''bool KKeySequenceWidget.isKeySequenceAvailable(QKeySequence seq)'''
        return bool()
    def setClearButtonShown(self, show):
        '''void KKeySequenceWidget.setClearButtonShown(bool show)'''
    def isModifierlessAllowed(self):
        '''bool KKeySequenceWidget.isModifierlessAllowed()'''
        return bool()
    def setModifierlessAllowed(self, allow):
        '''void KKeySequenceWidget.setModifierlessAllowed(bool allow)'''
    def multiKeyShortcutsAllowed(self):
        '''bool KKeySequenceWidget.multiKeyShortcutsAllowed()'''
        return bool()
    def setMultiKeyShortcutsAllowed(self):
        '''bool KKeySequenceWidget.setMultiKeyShortcutsAllowed()'''
        return bool()
    def checkForConflictsAgainst(self):
        '''KKeySequenceWidget.ShortcutTypes KKeySequenceWidget.checkForConflictsAgainst()'''
        return KKeySequenceWidget.ShortcutTypes()
    def setCheckForConflictsAgainst(self, types):
        '''void KKeySequenceWidget.setCheckForConflictsAgainst(KKeySequenceWidget.ShortcutTypes types)'''
    class ShortcutTypes():
        """"""
        def __init__(self):
            '''KKeySequenceWidget.ShortcutTypes KKeySequenceWidget.ShortcutTypes.__init__()'''
            return KKeySequenceWidget.ShortcutTypes()
        def __init__(self):
            '''int KKeySequenceWidget.ShortcutTypes.__init__()'''
            return int()
        def __init__(self):
            '''void KKeySequenceWidget.ShortcutTypes.__init__()'''
        def __bool__(self):
            '''int KKeySequenceWidget.ShortcutTypes.__bool__()'''
            return int()
        def __ne__(self, f):
            '''bool KKeySequenceWidget.ShortcutTypes.__ne__(KKeySequenceWidget.ShortcutTypes f)'''
            return bool()
        def __eq__(self, f):
            '''bool KKeySequenceWidget.ShortcutTypes.__eq__(KKeySequenceWidget.ShortcutTypes f)'''
            return bool()
        def __invert__(self):
            '''KKeySequenceWidget.ShortcutTypes KKeySequenceWidget.ShortcutTypes.__invert__()'''
            return KKeySequenceWidget.ShortcutTypes()
        def __and__(self, mask):
            '''KKeySequenceWidget.ShortcutTypes KKeySequenceWidget.ShortcutTypes.__and__(int mask)'''
            return KKeySequenceWidget.ShortcutTypes()
        def __xor__(self, f):
            '''KKeySequenceWidget.ShortcutTypes KKeySequenceWidget.ShortcutTypes.__xor__(KKeySequenceWidget.ShortcutTypes f)'''
            return KKeySequenceWidget.ShortcutTypes()
        def __xor__(self, f):
            '''KKeySequenceWidget.ShortcutTypes KKeySequenceWidget.ShortcutTypes.__xor__(int f)'''
            return KKeySequenceWidget.ShortcutTypes()
        def __or__(self, f):
            '''KKeySequenceWidget.ShortcutTypes KKeySequenceWidget.ShortcutTypes.__or__(KKeySequenceWidget.ShortcutTypes f)'''
            return KKeySequenceWidget.ShortcutTypes()
        def __or__(self, f):
            '''KKeySequenceWidget.ShortcutTypes KKeySequenceWidget.ShortcutTypes.__or__(int f)'''
            return KKeySequenceWidget.ShortcutTypes()
        def __int__(self):
            '''int KKeySequenceWidget.ShortcutTypes.__int__()'''
            return int()
        def __ixor__(self, f):
            '''KKeySequenceWidget.ShortcutTypes KKeySequenceWidget.ShortcutTypes.__ixor__(KKeySequenceWidget.ShortcutTypes f)'''
            return KKeySequenceWidget.ShortcutTypes()
        def __ior__(self, f):
            '''KKeySequenceWidget.ShortcutTypes KKeySequenceWidget.ShortcutTypes.__ior__(KKeySequenceWidget.ShortcutTypes f)'''
            return KKeySequenceWidget.ShortcutTypes()
        def __iand__(self, mask):
            '''KKeySequenceWidget.ShortcutTypes KKeySequenceWidget.ShortcutTypes.__iand__(int mask)'''
            return KKeySequenceWidget.ShortcutTypes()


class KKeyServer():
    """"""
    def modXToQt(self, modX, modQt):
        '''static bool KKeyServer.modXToQt(int modX, int modQt)'''
        return bool()
    def symXToKeyQt(self, sym, keyQt):
        '''static bool KKeyServer.symXToKeyQt(int sym, int keyQt)'''
        return bool()
    def keyQtToModX(self, keyQt, mod):
        '''static bool KKeyServer.keyQtToModX(int keyQt, int mod)'''
        return bool()
    def keyQtToCodeX(self, keyQt, keyCode):
        '''static bool KKeyServer.keyQtToCodeX(int keyQt, int keyCode)'''
        return bool()
    def keyQtToSymX(self, keyQt, sym):
        '''static bool KKeyServer.keyQtToSymX(int keyQt, int sym)'''
        return bool()
    def accelModMaskX(self):
        '''static int KKeyServer.accelModMaskX()'''
        return int()
    def modXModeSwitch(self):
        '''static int KKeyServer.modXModeSwitch()'''
        return int()
    def modXScrollLock(self):
        '''static int KKeyServer.modXScrollLock()'''
        return int()
    def modXNumLock(self):
        '''static int KKeyServer.modXNumLock()'''
        return int()
    def modXMeta(self):
        '''static int KKeyServer.modXMeta()'''
        return int()
    def modXAlt(self):
        '''static int KKeyServer.modXAlt()'''
        return int()
    def modXCtrl(self):
        '''static int KKeyServer.modXCtrl()'''
        return int()
    def modXLock(self):
        '''static int KKeyServer.modXLock()'''
        return int()
    def modXShift(self):
        '''static int KKeyServer.modXShift()'''
        return int()
    def keyboardHasMetaKey(self):
        '''static bool KKeyServer.keyboardHasMetaKey()'''
        return bool()
    def initializeMods(self):
        '''static bool KKeyServer.initializeMods()'''
        return bool()
    def isShiftAsModifierAllowed(self, keyQt):
        '''static bool KKeyServer.isShiftAsModifierAllowed(int keyQt)'''
        return bool()
    def stringUserToMod(self, mod):
        '''static int KKeyServer.stringUserToMod(QString mod)'''
        return int()
    def modToStringUser(self, mod):
        '''static QString KKeyServer.modToStringUser(int mod)'''
        return QString()


class KLanguageButton(QWidget):
    """"""
    def __init__(self, parent = None):
        '''void KLanguageButton.__init__(QWidget parent = None)'''
    def __init__(self, text, parent = None):
        '''void KLanguageButton.__init__(QString text, QWidget parent = None)'''
    highlighted = pyqtSignal() # void highlighted(const QStringamp;) - signal
    activated = pyqtSignal() # void activated(const QStringamp;) - signal
    def setCurrentItem(self, languageCode):
        '''void KLanguageButton.setCurrentItem(QString languageCode)'''
    def contains(self, languageCode):
        '''bool KLanguageButton.contains(QString languageCode)'''
        return bool()
    def current(self):
        '''QString KLanguageButton.current()'''
        return QString()
    def clear(self):
        '''void KLanguageButton.clear()'''
    def count(self):
        '''int KLanguageButton.count()'''
        return int()
    def insertSeparator(self, index = None):
        '''void KLanguageButton.insertSeparator(int index = -1)'''
    def insertLanguage(self, languageCode, name = QString(), index = None):
        '''void KLanguageButton.insertLanguage(QString languageCode, QString name = QString(), int index = -1)'''
    def loadAllLanguages(self):
        '''void KLanguageButton.loadAllLanguages()'''
    def showLanguageCodes(self, show):
        '''void KLanguageButton.showLanguageCodes(bool show)'''
    def setText(self, text):
        '''void KLanguageButton.setText(QString text)'''
    def setLocale(self, locale):
        '''void KLanguageButton.setLocale(KLocale locale)'''


class KLed(QWidget):
    """"""
    # Enum KLed.Look
    Flat = 0
    Raised = 0
    Sunken = 0

    # Enum KLed.Shape
    Rectangular = 0
    Circular = 0

    # Enum KLed.State
    Off = 0
    On = 0

    def __init__(self, parent = None):
        '''void KLed.__init__(QWidget parent = None)'''
    def __init__(self, color, parent = None):
        '''void KLed.__init__(QColor color, QWidget parent = None)'''
    def __init__(self, color, state, look, shape, parent = None):
        '''void KLed.__init__(QColor color, KLed.State state, KLed.Look look, KLed.Shape shape, QWidget parent = None)'''
    def paintLed(self, shape, look):
        '''void KLed.paintLed(KLed.Shape shape, KLed.Look look)'''
    def updateCachedPixmap(self):
        '''void KLed.updateCachedPixmap()'''
    def resizeEvent(self):
        '''QResizeEvent KLed.resizeEvent()'''
        return QResizeEvent()
    def paintCachedPixmap(self):
        '''bool KLed.paintCachedPixmap()'''
        return bool()
    def paintEvent(self):
        '''QPaintEvent KLed.paintEvent()'''
        return QPaintEvent()
    def paintRectFrame(self, raised):
        '''void KLed.paintRectFrame(bool raised)'''
    def paintRect(self):
        '''void KLed.paintRect()'''
    def paintSunken(self):
        '''void KLed.paintSunken()'''
    def paintRaised(self):
        '''void KLed.paintRaised()'''
    def paintFlat(self):
        '''void KLed.paintFlat()'''
    def ledWidth(self):
        '''int KLed.ledWidth()'''
        return int()
    def off(self):
        '''void KLed.off()'''
    def on(self):
        '''void KLed.on()'''
    def toggle(self):
        '''void KLed.toggle()'''
    def minimumSizeHint(self):
        '''QSize KLed.minimumSizeHint()'''
        return QSize()
    def sizeHint(self):
        '''QSize KLed.sizeHint()'''
        return QSize()
    def setDarkFactor(self, darkFactor):
        '''void KLed.setDarkFactor(int darkFactor)'''
    def setShape(self, shape):
        '''void KLed.setShape(KLed.Shape shape)'''
    def setLook(self, look):
        '''void KLed.setLook(KLed.Look look)'''
    def setState(self, state):
        '''void KLed.setState(KLed.State state)'''
    def setColor(self, color):
        '''void KLed.setColor(QColor color)'''
    def darkFactor(self):
        '''int KLed.darkFactor()'''
        return int()
    def shape(self):
        '''KLed.Shape KLed.shape()'''
        return KLed.Shape()
    def look(self):
        '''KLed.Look KLed.look()'''
        return KLed.Look()
    def state(self):
        '''KLed.State KLed.state()'''
        return KLed.State()
    def color(self):
        '''QColor KLed.color()'''
        return QColor()


class KLineEdit(QLineEdit, KCompletionBase):
    """"""
    def __init__(self, string, parent = None):
        '''void KLineEdit.__init__(QString string, QWidget parent = None)'''
    def __init__(self, parent = None):
        '''void KLineEdit.__init__(QWidget parent = None)'''
    def focusOutEvent(self, ev):
        '''void KLineEdit.focusOutEvent(QFocusEvent ev)'''
    def focusInEvent(self, ev):
        '''void KLineEdit.focusInEvent(QFocusEvent ev)'''
    def paintEvent(self, ev):
        '''void KLineEdit.paintEvent(QPaintEvent ev)'''
    def autoSuggest(self):
        '''bool KLineEdit.autoSuggest()'''
        return bool()
    def create(self, initializeWindow = True, destroyOldWindow = True):
        '''int KLineEdit.create(bool initializeWindow = True, bool destroyOldWindow = True)'''
        return int()
    def setUserSelection(self, userSelection):
        '''void KLineEdit.setUserSelection(bool userSelection)'''
    def dropEvent(self):
        '''QDropEvent KLineEdit.dropEvent()'''
        return QDropEvent()
    def createStandardContextMenu(self):
        '''QMenu KLineEdit.createStandardContextMenu()'''
        return QMenu()
    def contextMenuEvent(self):
        '''QContextMenuEvent KLineEdit.contextMenuEvent()'''
        return QContextMenuEvent()
    def mouseDoubleClickEvent(self):
        '''QMouseEvent KLineEdit.mouseDoubleClickEvent()'''
        return QMouseEvent()
    def mouseReleaseEvent(self):
        '''QMouseEvent KLineEdit.mouseReleaseEvent()'''
        return QMouseEvent()
    def mousePressEvent(self):
        '''QMouseEvent KLineEdit.mousePressEvent()'''
        return QMouseEvent()
    def keyPressEvent(self):
        '''QKeyEvent KLineEdit.keyPressEvent()'''
        return QKeyEvent()
    def resizeEvent(self):
        '''QResizeEvent KLineEdit.resizeEvent()'''
        return QResizeEvent()
    def event(self):
        '''QEvent KLineEdit.event()'''
        return QEvent()
    def userCancelled(self, cancelText):
        '''void KLineEdit.userCancelled(QString cancelText)'''
    def makeCompletion(self):
        '''QString KLineEdit.makeCompletion()'''
        return QString()
    def passwordMode(self):
        '''bool KLineEdit.passwordMode()'''
        return bool()
    def setPasswordMode(self, b = True):
        '''void KLineEdit.setPasswordMode(bool b = True)'''
    def setText(self):
        '''QString KLineEdit.setText()'''
        return QString()
    def setSqueezedText(self, text):
        '''void KLineEdit.setSqueezedText(QString text)'''
    def clear(self):
        '''void KLineEdit.clear()'''
    def setCompletedItems(self, items, autoSuggest = True):
        '''void KLineEdit.setCompletedItems(QStringList items, bool autoSuggest = True)'''
    def setCompletedText(self):
        '''QString KLineEdit.setCompletedText()'''
        return QString()
    def setCompletedText(self):
        '''bool KLineEdit.setCompletedText()'''
        return bool()
    def rotateText(self, type):
        '''void KLineEdit.rotateText(KCompletionBase.KeyBindingType type)'''
    def setReadOnly(self):
        '''bool KLineEdit.setReadOnly()'''
        return bool()
    clearButtonClicked = pyqtSignal() # void clearButtonClicked() - signal
    aboutToShowContextMenu = pyqtSignal() # void aboutToShowContextMenu(QMenu *) - signal
    completionModeChanged = pyqtSignal() # void completionModeChanged(KGlobalSettings::Completion) - signal
    textRotation = pyqtSignal() # void textRotation(KCompletionBase::KeyBindingType) - signal
    userTextChanged = pyqtSignal() # void userTextChanged(const QStringamp;) - signal
    substringCompletion = pyqtSignal() # void substringCompletion(const QStringamp;) - signal
    completion = pyqtSignal() # void completion(const QStringamp;) - signal
    returnPressed = pyqtSignal() # void returnPressed(const QStringamp;) - signal
    completionBoxActivated = pyqtSignal() # void completionBoxActivated(const QStringamp;) - signal
    def doCompletion(self, txt):
        '''void KLineEdit.doCompletion(QString txt)'''
    def clearButtonUsedSize(self):
        '''QSize KLineEdit.clearButtonUsedSize()'''
        return QSize()
    def isClearButtonShown(self):
        '''bool KLineEdit.isClearButtonShown()'''
        return bool()
    def setClearButtonShown(self, show):
        '''void KLineEdit.setClearButtonShown(bool show)'''
    def clickMessage(self):
        '''QString KLineEdit.clickMessage()'''
        return QString()
    def setClickMessage(self, msg):
        '''void KLineEdit.setClickMessage(QString msg)'''
    def setCompletionBox(self, box):
        '''void KLineEdit.setCompletionBox(KCompletionBox box)'''
    def userText(self):
        '''QString KLineEdit.userText()'''
        return QString()
    def originalText(self):
        '''QString KLineEdit.originalText()'''
        return QString()
    def isSqueezedTextEnabled(self):
        '''bool KLineEdit.isSqueezedTextEnabled()'''
        return bool()
    def setSqueezedTextEnabled(self, enable):
        '''void KLineEdit.setSqueezedTextEnabled(bool enable)'''
    def copy(self):
        '''void KLineEdit.copy()'''
    def setCompletionObject(self, hsig = True):
        '''KCompletion KLineEdit.setCompletionObject(bool hsig = True)'''
        return KCompletion()
    def completionBox(self, create = True):
        '''KCompletionBox KLineEdit.completionBox(bool create = True)'''
        return KCompletionBox()
    def trapReturnKey(self):
        '''bool KLineEdit.trapReturnKey()'''
        return bool()
    def setTrapReturnKey(self, trap):
        '''void KLineEdit.setTrapReturnKey(bool trap)'''
    def urlDropsEnabled(self):
        '''bool KLineEdit.urlDropsEnabled()'''
        return bool()
    def setUrlDropsEnabled(self, enable):
        '''void KLineEdit.setUrlDropsEnabled(bool enable)'''
    def isContextMenuEnabled(self):
        '''bool KLineEdit.isContextMenuEnabled()'''
        return bool()
    def setContextMenuEnabled(self, showMenu):
        '''void KLineEdit.setContextMenuEnabled(bool showMenu)'''
    def setCompletionModeDisabled(self, mode, disable = True):
        '''void KLineEdit.setCompletionModeDisabled(KGlobalSettings.Completion mode, bool disable = True)'''
    def setCompletionMode(self, mode):
        '''void KLineEdit.setCompletionMode(KGlobalSettings.Completion mode)'''
    def setUrl(self, url):
        '''void KLineEdit.setUrl(KUrl url)'''


class KLinkItemSelectionModel(QItemSelectionModel):
    """"""
    def __init__(self, targetModel, linkedItemSelectionModel, parent = None):
        '''void KLinkItemSelectionModel.__init__(QAbstractItemModel targetModel, QItemSelectionModel linkedItemSelectionModel, QObject parent = None)'''
    def select(self, index, command):
        '''void KLinkItemSelectionModel.select(QModelIndex index, QItemSelectionModel.SelectionFlags command)'''
    def select(self, selection, command):
        '''void KLinkItemSelectionModel.select(QItemSelection selection, QItemSelectionModel.SelectionFlags command)'''


class KListWidgetSearchLine(KLineEdit):
    """"""
    def __init__(self, parent = None, listWidget = None):
        '''void KListWidgetSearchLine.__init__(QWidget parent = None, QListWidget listWidget = None)'''
    def event(self, event):
        '''bool KListWidgetSearchLine.event(QEvent event)'''
        return bool()
    def itemMatches(self, item, s):
        '''bool KListWidgetSearchLine.itemMatches(QListWidgetItem item, QString s)'''
        return bool()
    def clear(self):
        '''void KListWidgetSearchLine.clear()'''
    def setListWidget(self, lv):
        '''void KListWidgetSearchLine.setListWidget(QListWidget lv)'''
    def setCaseSensitivity(self, cs):
        '''void KListWidgetSearchLine.setCaseSensitivity(Qt.CaseSensitivity cs)'''
    def updateSearch(self, s = QString()):
        '''void KListWidgetSearchLine.updateSearch(QString s = QString())'''
    def listWidget(self):
        '''QListWidget KListWidgetSearchLine.listWidget()'''
        return QListWidget()
    def caseSensitive(self):
        '''Qt.CaseSensitivity KListWidgetSearchLine.caseSensitive()'''
        return Qt.CaseSensitivity()


class KMainWindow(QMainWindow):
    """"""
    def __init__(self, parent = None, f = 0):
        '''void KMainWindow.__init__(QWidget parent = None, Qt.WindowFlags f = 0)'''
    def saveAutoSaveSettings(self):
        '''void KMainWindow.saveAutoSaveSettings()'''
    def showAboutApplication(self):
        '''void KMainWindow.showAboutApplication()'''
    def parseGeometry(self, parsewidth):
        '''void KMainWindow.parseGeometry(bool parsewidth)'''
    def restoreWindowSize(self, config):
        '''void KMainWindow.restoreWindowSize(KConfigGroup config)'''
    def saveWindowSize(self, config):
        '''void KMainWindow.saveWindowSize(KConfigGroup config)'''
    def settingsDirty(self):
        '''bool KMainWindow.settingsDirty()'''
        return bool()
    def readPropertiesInternal(self):
        '''int KMainWindow.readPropertiesInternal()'''
        return int()
    def savePropertiesInternal(self):
        '''int KMainWindow.savePropertiesInternal()'''
        return int()
    def readGlobalProperties(self, sessionConfig):
        '''void KMainWindow.readGlobalProperties(KConfig sessionConfig)'''
    def saveGlobalProperties(self, sessionConfig):
        '''void KMainWindow.saveGlobalProperties(KConfig sessionConfig)'''
    def readProperties(self):
        '''KConfigGroup KMainWindow.readProperties()'''
        return KConfigGroup()
    def saveProperties(self):
        '''KConfigGroup KMainWindow.saveProperties()'''
        return KConfigGroup()
    def queryClose(self):
        '''bool KMainWindow.queryClose()'''
        return bool()
    def queryExit(self):
        '''bool KMainWindow.queryExit()'''
        return bool()
    def closeEvent(self):
        '''QCloseEvent KMainWindow.closeEvent()'''
        return QCloseEvent()
    def event(self, event):
        '''bool KMainWindow.event(QEvent event)'''
        return bool()
    def setSettingsDirty(self):
        '''void KMainWindow.setSettingsDirty()'''
    def appHelpActivated(self):
        '''void KMainWindow.appHelpActivated()'''
    def setPlainCaption(self, caption):
        '''void KMainWindow.setPlainCaption(QString caption)'''
    def setCaption(self, caption):
        '''void KMainWindow.setCaption(QString caption)'''
    def setCaption(self, caption, modified):
        '''void KMainWindow.setCaption(QString caption, bool modified)'''
    def dbusName(self):
        '''QString KMainWindow.dbusName()'''
        return QString()
    def ignoreInitialGeometry(self):
        '''void KMainWindow.ignoreInitialGeometry()'''
    def initialGeometrySet(self):
        '''bool KMainWindow.initialGeometrySet()'''
        return bool()
    def saveMainWindowSettings(self, config):
        '''void KMainWindow.saveMainWindowSettings(KConfigGroup config)'''
    def applyMainWindowSettings(self, config, forceGlobal = False):
        '''void KMainWindow.applyMainWindowSettings(KConfigGroup config, bool forceGlobal = False)'''
    def autoSaveConfigGroup(self):
        '''KConfigGroup KMainWindow.autoSaveConfigGroup()'''
        return KConfigGroup()
    def autoSaveGroup(self):
        '''QString KMainWindow.autoSaveGroup()'''
        return QString()
    def autoSaveSettings(self):
        '''bool KMainWindow.autoSaveSettings()'''
        return bool()
    def resetAutoSaveSettings(self):
        '''void KMainWindow.resetAutoSaveSettings()'''
    def setAutoSaveSettings(self, groupName = QLatin1StringMainWindow, saveWindowSize = True):
        '''void KMainWindow.setAutoSaveSettings(QString groupName = QLatin1StringMainWindow, bool saveWindowSize = True)'''
    def setAutoSaveSettings(self, group, saveWindowSize = True):
        '''void KMainWindow.setAutoSaveSettings(KConfigGroup group, bool saveWindowSize = True)'''
    def toolBars(self):
        '''list-of-KToolBar KMainWindow.toolBars()'''
        return [KToolBar()]
    def toolBar(self, name = QString()):
        '''KToolBar KMainWindow.toolBar(QString name = QString())'''
        return KToolBar()
    def memberList(self):
        '''static list-of-KMainWindow KMainWindow.memberList()'''
        return [KMainWindow()]
    def statusBar(self):
        '''KStatusBar KMainWindow.statusBar()'''
        return KStatusBar()
    def menuBar(self):
        '''KMenuBar KMainWindow.menuBar()'''
        return KMenuBar()
    def hasMenuBar(self):
        '''bool KMainWindow.hasMenuBar()'''
        return bool()
    def restore(self, number, show = True):
        '''bool KMainWindow.restore(int number, bool show = True)'''
        return bool()
    def classNameOfToplevel(self, number):
        '''static QString KMainWindow.classNameOfToplevel(int number)'''
        return QString()
    def canBeRestored(self, number):
        '''static bool KMainWindow.canBeRestored(int number)'''
        return bool()
    def customHelpMenu(self, showWhatsThis = True):
        '''KMenu KMainWindow.customHelpMenu(bool showWhatsThis = True)'''
        return KMenu()
    def helpMenu(self, aboutAppText = QString(), showWhatsThis = True):
        '''KMenu KMainWindow.helpMenu(QString aboutAppText = QString(), bool showWhatsThis = True)'''
        return KMenu()


class KSelectionOwner(QObject):
    """"""
    def __init__(self, selection, screen = None, parent = None):
        '''void KSelectionOwner.__init__(int selection, int screen = -1, QObject parent = None)'''
    def __init__(self, selection, screen = None, parent = None):
        '''void KSelectionOwner.__init__(str selection, int screen = -1, QObject parent = None)'''
    def setData(self, extra1, extra2):
        '''void KSelectionOwner.setData(int extra1, int extra2)'''
    def getAtoms(self):
        '''void KSelectionOwner.getAtoms()'''
    def replyTargets(self, property, requestor):
        '''void KSelectionOwner.replyTargets(int property, int requestor)'''
    def genericReply(self, target, property, requestor):
        '''bool KSelectionOwner.genericReply(int target, int property, int requestor)'''
        return bool()
    lostOwnership = pyqtSignal() # void lostOwnership() - signal
    def ownerWindow(self):
        '''int KSelectionOwner.ownerWindow()'''
        return int()
    def release(self):
        '''void KSelectionOwner.release()'''
    def claim(self, force, force_kill = True):
        '''bool KSelectionOwner.claim(bool force, bool force_kill = True)'''
        return bool()


class KSelectionWatcher(QObject):
    """"""
    def __init__(self, selection, screen = None, parent = None):
        '''void KSelectionWatcher.__init__(int selection, int screen = -1, QObject parent = None)'''
    def __init__(self, selection, screen = None, parent = None):
        '''void KSelectionWatcher.__init__(str selection, int screen = -1, QObject parent = None)'''
    lostOwner = pyqtSignal() # void lostOwner() - signal
    newOwner = pyqtSignal() # void newOwner(Window) - signal
    def owner(self):
        '''int KSelectionWatcher.owner()'''
        return int()


class KMenu(QMenu):
    """"""
    def __init__(self, parent = None):
        '''void KMenu.__init__(QWidget parent = None)'''
    def __init__(self, title, parent = None):
        '''void KMenu.__init__(QString title, QWidget parent = None)'''
    def hideEvent(self):
        '''QHideEvent KMenu.hideEvent()'''
        return QHideEvent()
    def contextMenuEvent(self, e):
        '''void KMenu.contextMenuEvent(QContextMenuEvent e)'''
    def focusNextPrevChild(self, next):
        '''bool KMenu.focusNextPrevChild(bool next)'''
        return bool()
    def mousePressEvent(self, e):
        '''void KMenu.mousePressEvent(QMouseEvent e)'''
    def mouseReleaseEvent(self, e):
        '''void KMenu.mouseReleaseEvent(QMouseEvent e)'''
    def keyPressEvent(self, e):
        '''void KMenu.keyPressEvent(QKeyEvent e)'''
    def closeEvent(self):
        '''QCloseEvent KMenu.closeEvent()'''
        return QCloseEvent()
    aboutToShowContextMenu = pyqtSignal() # void aboutToShowContextMenu(KMenu *,QAction *,QMenu *) - signal
    def keyboardModifiers(self):
        '''Qt.KeyboardModifiers KMenu.keyboardModifiers()'''
        return Qt.KeyboardModifiers()
    def mouseButtons(self):
        '''Qt.MouseButtons KMenu.mouseButtons()'''
        return Qt.MouseButtons()
    def contextMenuFocusAction(self):
        '''static QAction KMenu.contextMenuFocusAction()'''
        return QAction()
    def contextMenuFocus(self):
        '''static KMenu KMenu.contextMenuFocus()'''
        return KMenu()
    def hideContextMenu(self):
        '''void KMenu.hideContextMenu()'''
    def contextMenu(self):
        '''QMenu KMenu.contextMenu()'''
        return QMenu()
    def setKeyboardShortcutsExecute(self, enable):
        '''void KMenu.setKeyboardShortcutsExecute(bool enable)'''
    def setKeyboardShortcutsEnabled(self, enable):
        '''void KMenu.setKeyboardShortcutsEnabled(bool enable)'''
    def addTitle(self, text, before = None):
        '''QAction KMenu.addTitle(QString text, QAction before = None)'''
        return QAction()
    def addTitle(self, icon, text, before = None):
        '''QAction KMenu.addTitle(QIcon icon, QString text, QAction before = None)'''
        return QAction()


class KMenuBar(QMenuBar):
    """"""
    def __init__(self, parent = None):
        '''void KMenuBar.__init__(QWidget parent = None)'''
    def paintEvent(self):
        '''QPaintEvent KMenuBar.paintEvent()'''
        return QPaintEvent()
    def closeEvent(self):
        '''QCloseEvent KMenuBar.closeEvent()'''
        return QCloseEvent()
    def eventFilter(self):
        '''QEvent KMenuBar.eventFilter()'''
        return QEvent()
    def resizeEvent(self):
        '''QResizeEvent KMenuBar.resizeEvent()'''
        return QResizeEvent()
    def slotReadConfig(self):
        '''void KMenuBar.slotReadConfig()'''
    def sizeHint(self):
        '''QSize KMenuBar.sizeHint()'''
        return QSize()
    def setMargin(self):
        '''int KMenuBar.setMargin()'''
        return int()
    def setLineWidth(self):
        '''int KMenuBar.setLineWidth()'''
        return int()
    def setFrameStyle(self):
        '''int KMenuBar.setFrameStyle()'''
        return int()
    def resize(self, w, h):
        '''void KMenuBar.resize(int w, int h)'''
    def resize(self, s):
        '''void KMenuBar.resize(QSize s)'''
    def setGeometry(self, r):
        '''void KMenuBar.setGeometry(QRect r)'''
    def setGeometry(self, x, y, w, h):
        '''void KMenuBar.setGeometry(int x, int y, int w, int h)'''
    def isTopLevelMenu(self):
        '''bool KMenuBar.isTopLevelMenu()'''
        return bool()
    def setTopLevelMenu(self, top_level = True):
        '''void KMenuBar.setTopLevelMenu(bool top_level = True)'''


class KMessageBox():
    """"""
    # Enum KMessageBox.Option
    Notify = 0
    AllowLink = 0
    Dangerous = 0
    PlainCaption = 0
    NoExec = 0
    WindowModal = 0

    # Enum KMessageBox.DialogType
    QuestionYesNo = 0
    WarningYesNo = 0
    WarningContinueCancel = 0
    WarningYesNoCancel = 0
    Information = 0
    Sorry = 0
    Error = 0
    QuestionYesNoCancel = 0

    # Enum KMessageBox.ButtonCode
    Ok = 0
    Cancel = 0
    Yes = 0
    No = 0
    Continue = 0

    def __init__(self):
        '''void KMessageBox.__init__()'''
    def __init__(self):
        '''KMessageBox KMessageBox.__init__()'''
        return KMessageBox()
    def createKMessageBox(self, dialog, icon, text, strlist, ask, checkboxReturn, options, details = QString()):
        '''static int KMessageBox.createKMessageBox(KDialog dialog, QMessageBox.Icon icon, QString text, QStringList strlist, QString ask, bool checkboxReturn, KMessageBox.Options options, QString details = QString())'''
        return int()
    def createKMessageBox(self, dialog, icon, text, strlist, ask, checkboxReturn, options, details = QString(), notifyType = None):
        '''static int KMessageBox.createKMessageBox(KDialog dialog, QIcon icon, QString text, QStringList strlist, QString ask, bool checkboxReturn, KMessageBox.Options options, QString details = QString(), QMessageBox.Icon notifyType = QMessageBox.Information)'''
        return int()
    def setDontShowAskAgainConfig(self, cfg):
        '''static void KMessageBox.setDontShowAskAgainConfig(KConfig cfg)'''
    def saveDontShowAgainContinue(self, dontShowAgainName):
        '''static void KMessageBox.saveDontShowAgainContinue(QString dontShowAgainName)'''
    def saveDontShowAgainYesNo(self, dontShowAgainName, result):
        '''static void KMessageBox.saveDontShowAgainYesNo(QString dontShowAgainName, KMessageBox.ButtonCode result)'''
    def shouldBeShownContinue(self, dontShowAgainName):
        '''static bool KMessageBox.shouldBeShownContinue(QString dontShowAgainName)'''
        return bool()
    def shouldBeShownYesNo(self, dontShowAgainName, result):
        '''static bool KMessageBox.shouldBeShownYesNo(QString dontShowAgainName, KMessageBox.ButtonCode result)'''
        return bool()
    def queuedMessageBoxWId(self, parent_id, type, text, caption, options):
        '''static void KMessageBox.queuedMessageBoxWId(int parent_id, KMessageBox.DialogType type, QString text, QString caption, KMessageBox.Options options)'''
    def queuedMessageBoxWId(self, parent_id, type, text, caption = QString()):
        '''static void KMessageBox.queuedMessageBoxWId(int parent_id, KMessageBox.DialogType type, QString text, QString caption = QString())'''
    def queuedMessageBox(self, parent, type, text, caption, options):
        '''static void KMessageBox.queuedMessageBox(QWidget parent, KMessageBox.DialogType type, QString text, QString caption, KMessageBox.Options options)'''
    def queuedMessageBox(self, parent, type, text, caption = QString()):
        '''static void KMessageBox.queuedMessageBox(QWidget parent, KMessageBox.DialogType type, QString text, QString caption = QString())'''
    def messageBoxWId(self, parent_id, type, text, caption = QString(), buttonYes = None, buttonNo = None, buttonCancel = None, dontShowAskAgainName = QString(), options = None):
        '''static int KMessageBox.messageBoxWId(int parent_id, KMessageBox.DialogType type, QString text, QString caption = QString(), KGuiItem buttonYes = KStandardGuiItem.yes(), KGuiItem buttonNo = KStandardGuiItem.no(), KGuiItem buttonCancel = KStandardGuiItem.cancel(), QString dontShowAskAgainName = QString(), KMessageBox.Options options = KMessageBox.Notify)'''
        return int()
    def messageBox(self, parent, type, text, caption = QString(), buttonYes = None, buttonNo = None, buttonCancel = None, dontShowAskAgainName = QString(), options = None):
        '''static int KMessageBox.messageBox(QWidget parent, KMessageBox.DialogType type, QString text, QString caption = QString(), KGuiItem buttonYes = KStandardGuiItem.yes(), KGuiItem buttonNo = KStandardGuiItem.no(), KGuiItem buttonCancel = KStandardGuiItem.cancel(), QString dontShowAskAgainName = QString(), KMessageBox.Options options = KMessageBox.Notify)'''
        return int()
    def about(self, parent, text, caption = QString(), options = None):
        '''static void KMessageBox.about(QWidget parent, QString text, QString caption = QString(), KMessageBox.Options options = KMessageBox.Notify)'''
    def enableMessage(self, dontShowAgainName):
        '''static void KMessageBox.enableMessage(QString dontShowAgainName)'''
    def enableAllMessages(self):
        '''static void KMessageBox.enableAllMessages()'''
    def informationListWId(self, parent_id, text, strlist, caption = QString(), dontShowAgainName = QString(), options = None):
        '''static void KMessageBox.informationListWId(int parent_id, QString text, QStringList strlist, QString caption = QString(), QString dontShowAgainName = QString(), KMessageBox.Options options = KMessageBox.Notify)'''
    def informationList(self, parent, text, strlist, caption = QString(), dontShowAgainName = QString(), options = None):
        '''static void KMessageBox.informationList(QWidget parent, QString text, QStringList strlist, QString caption = QString(), QString dontShowAgainName = QString(), KMessageBox.Options options = KMessageBox.Notify)'''
    def informationWId(self, parent_id, text, caption = QString(), dontShowAgainName = QString(), options = None):
        '''static void KMessageBox.informationWId(int parent_id, QString text, QString caption = QString(), QString dontShowAgainName = QString(), KMessageBox.Options options = KMessageBox.Notify)'''
    def information(self, parent, text, caption = QString(), dontShowAgainName = QString(), options = None):
        '''static void KMessageBox.information(QWidget parent, QString text, QString caption = QString(), QString dontShowAgainName = QString(), KMessageBox.Options options = KMessageBox.Notify)'''
    def detailedSorryWId(self, parent_id, text, details, caption = QString(), options = None):
        '''static void KMessageBox.detailedSorryWId(int parent_id, QString text, QString details, QString caption = QString(), KMessageBox.Options options = KMessageBox.Notify)'''
    def detailedSorry(self, parent, text, details, caption = QString(), options = None):
        '''static void KMessageBox.detailedSorry(QWidget parent, QString text, QString details, QString caption = QString(), KMessageBox.Options options = KMessageBox.Notify)'''
    def sorryWId(self, parent_id, text, caption = QString(), options = None):
        '''static void KMessageBox.sorryWId(int parent_id, QString text, QString caption = QString(), KMessageBox.Options options = KMessageBox.Notify)'''
    def sorry(self, parent, text, caption = QString(), options = None):
        '''static void KMessageBox.sorry(QWidget parent, QString text, QString caption = QString(), KMessageBox.Options options = KMessageBox.Notify)'''
    def queuedDetailedErrorWId(self, parent_id, text, details, caption = QString()):
        '''static void KMessageBox.queuedDetailedErrorWId(int parent_id, QString text, QString details, QString caption = QString())'''
    def queuedDetailedError(self, parent, text, details, caption = QString()):
        '''static void KMessageBox.queuedDetailedError(QWidget parent, QString text, QString details, QString caption = QString())'''
    def detailedErrorWId(self, parent_id, text, details, caption = QString(), options = None):
        '''static void KMessageBox.detailedErrorWId(int parent_id, QString text, QString details, QString caption = QString(), KMessageBox.Options options = KMessageBox.Notify)'''
    def detailedError(self, parent, text, details, caption = QString(), options = None):
        '''static void KMessageBox.detailedError(QWidget parent, QString text, QString details, QString caption = QString(), KMessageBox.Options options = KMessageBox.Notify)'''
    def errorListWId(self, parent_id, text, strlist, caption = QString(), options = None):
        '''static void KMessageBox.errorListWId(int parent_id, QString text, QStringList strlist, QString caption = QString(), KMessageBox.Options options = KMessageBox.Notify)'''
    def errorList(self, parent, text, strlist, caption = QString(), options = None):
        '''static void KMessageBox.errorList(QWidget parent, QString text, QStringList strlist, QString caption = QString(), KMessageBox.Options options = KMessageBox.Notify)'''
    def errorWId(self, parent_id, text, caption = QString(), options = None):
        '''static void KMessageBox.errorWId(int parent_id, QString text, QString caption = QString(), KMessageBox.Options options = KMessageBox.Notify)'''
    def error(self, parent, text, caption = QString(), options = None):
        '''static void KMessageBox.error(QWidget parent, QString text, QString caption = QString(), KMessageBox.Options options = KMessageBox.Notify)'''
    def warningYesNoCancelListWId(self, parent_id, text, strlist, caption = QString(), buttonYes = None, buttonNo = None, buttonCancel = None, dontAskAgainName = QString(), options = None):
        '''static int KMessageBox.warningYesNoCancelListWId(int parent_id, QString text, QStringList strlist, QString caption = QString(), KGuiItem buttonYes = KStandardGuiItem.yes(), KGuiItem buttonNo = KStandardGuiItem.no(), KGuiItem buttonCancel = KStandardGuiItem.cancel(), QString dontAskAgainName = QString(), KMessageBox.Options options = KMessageBox.Notify)'''
        return int()
    def warningYesNoCancelList(self, parent, text, strlist, caption = QString(), buttonYes = None, buttonNo = None, buttonCancel = None, dontAskAgainName = QString(), options = None):
        '''static int KMessageBox.warningYesNoCancelList(QWidget parent, QString text, QStringList strlist, QString caption = QString(), KGuiItem buttonYes = KStandardGuiItem.yes(), KGuiItem buttonNo = KStandardGuiItem.no(), KGuiItem buttonCancel = KStandardGuiItem.cancel(), QString dontAskAgainName = QString(), KMessageBox.Options options = KMessageBox.Notify)'''
        return int()
    def warningYesNoCancelWId(self, parent_id, text, caption = QString(), buttonYes = None, buttonNo = None, buttonCancel = None, dontAskAgainName = QString(), options = None):
        '''static int KMessageBox.warningYesNoCancelWId(int parent_id, QString text, QString caption = QString(), KGuiItem buttonYes = KStandardGuiItem.yes(), KGuiItem buttonNo = KStandardGuiItem.no(), KGuiItem buttonCancel = KStandardGuiItem.cancel(), QString dontAskAgainName = QString(), KMessageBox.Options options = KMessageBox.Notify)'''
        return int()
    def warningYesNoCancel(self, parent, text, caption = QString(), buttonYes = None, buttonNo = None, buttonCancel = None, dontAskAgainName = QString(), options = None):
        '''static int KMessageBox.warningYesNoCancel(QWidget parent, QString text, QString caption = QString(), KGuiItem buttonYes = KStandardGuiItem.yes(), KGuiItem buttonNo = KStandardGuiItem.no(), KGuiItem buttonCancel = KStandardGuiItem.cancel(), QString dontAskAgainName = QString(), KMessageBox.Options options = KMessageBox.Notify)'''
        return int()
    def warningContinueCancelListWId(self, parent_id, text, strlist, caption = QString(), buttonContinue = None, buttonCancel = None, dontAskAgainName = QString(), options = None):
        '''static int KMessageBox.warningContinueCancelListWId(int parent_id, QString text, QStringList strlist, QString caption = QString(), KGuiItem buttonContinue = KStandardGuiItem.cont(), KGuiItem buttonCancel = KStandardGuiItem.cancel(), QString dontAskAgainName = QString(), KMessageBox.Options options = KMessageBox.Notify)'''
        return int()
    def warningContinueCancelList(self, parent, text, strlist, caption = QString(), buttonContinue = None, buttonCancel = None, dontAskAgainName = QString(), options = None):
        '''static int KMessageBox.warningContinueCancelList(QWidget parent, QString text, QStringList strlist, QString caption = QString(), KGuiItem buttonContinue = KStandardGuiItem.cont(), KGuiItem buttonCancel = KStandardGuiItem.cancel(), QString dontAskAgainName = QString(), KMessageBox.Options options = KMessageBox.Notify)'''
        return int()
    def warningContinueCancelWId(self, parent_id, text, caption = QString(), buttonContinue = None, buttonCancel = None, dontAskAgainName = QString(), options = None):
        '''static int KMessageBox.warningContinueCancelWId(int parent_id, QString text, QString caption = QString(), KGuiItem buttonContinue = KStandardGuiItem.cont(), KGuiItem buttonCancel = KStandardGuiItem.cancel(), QString dontAskAgainName = QString(), KMessageBox.Options options = KMessageBox.Notify)'''
        return int()
    def warningContinueCancel(self, parent, text, caption = QString(), buttonContinue = None, buttonCancel = None, dontAskAgainName = QString(), options = None):
        '''static int KMessageBox.warningContinueCancel(QWidget parent, QString text, QString caption = QString(), KGuiItem buttonContinue = KStandardGuiItem.cont(), KGuiItem buttonCancel = KStandardGuiItem.cancel(), QString dontAskAgainName = QString(), KMessageBox.Options options = KMessageBox.Notify)'''
        return int()
    def warningYesNoListWId(self, parent_id, text, strlist, caption = QString(), buttonYes = None, buttonNo = None, dontAskAgainName = QString(), options = None):
        '''static int KMessageBox.warningYesNoListWId(int parent_id, QString text, QStringList strlist, QString caption = QString(), KGuiItem buttonYes = KStandardGuiItem.yes(), KGuiItem buttonNo = KStandardGuiItem.no(), QString dontAskAgainName = QString(), KMessageBox.Options options = KMessageBox.Options(KMessageBox.Notify|KMessageBox.Dangerous))'''
        return int()
    def warningYesNoList(self, parent, text, strlist, caption = QString(), buttonYes = None, buttonNo = None, dontAskAgainName = QString(), options = None):
        '''static int KMessageBox.warningYesNoList(QWidget parent, QString text, QStringList strlist, QString caption = QString(), KGuiItem buttonYes = KStandardGuiItem.yes(), KGuiItem buttonNo = KStandardGuiItem.no(), QString dontAskAgainName = QString(), KMessageBox.Options options = KMessageBox.Options(KMessageBox.Notify|KMessageBox.Dangerous))'''
        return int()
    def warningYesNoWId(self, parent_id, text, caption = QString(), buttonYes = None, buttonNo = None, dontAskAgainName = QString(), options = None):
        '''static int KMessageBox.warningYesNoWId(int parent_id, QString text, QString caption = QString(), KGuiItem buttonYes = KStandardGuiItem.yes(), KGuiItem buttonNo = KStandardGuiItem.no(), QString dontAskAgainName = QString(), KMessageBox.Options options = KMessageBox.Options(KMessageBox.Notify|KMessageBox.Dangerous))'''
        return int()
    def warningYesNo(self, parent, text, caption = QString(), buttonYes = None, buttonNo = None, dontAskAgainName = QString(), options = None):
        '''static int KMessageBox.warningYesNo(QWidget parent, QString text, QString caption = QString(), KGuiItem buttonYes = KStandardGuiItem.yes(), KGuiItem buttonNo = KStandardGuiItem.no(), QString dontAskAgainName = QString(), KMessageBox.Options options = KMessageBox.Options(KMessageBox.Notify|KMessageBox.Dangerous))'''
        return int()
    def questionYesNoListWId(self, parent_id, text, strlist, caption = QString(), buttonYes = None, buttonNo = None, dontAskAgainName = QString(), options = None):
        '''static int KMessageBox.questionYesNoListWId(int parent_id, QString text, QStringList strlist, QString caption = QString(), KGuiItem buttonYes = KStandardGuiItem.yes(), KGuiItem buttonNo = KStandardGuiItem.no(), QString dontAskAgainName = QString(), KMessageBox.Options options = KMessageBox.Notify)'''
        return int()
    def questionYesNoList(self, parent, text, strlist, caption = QString(), buttonYes = None, buttonNo = None, dontAskAgainName = QString(), options = None):
        '''static int KMessageBox.questionYesNoList(QWidget parent, QString text, QStringList strlist, QString caption = QString(), KGuiItem buttonYes = KStandardGuiItem.yes(), KGuiItem buttonNo = KStandardGuiItem.no(), QString dontAskAgainName = QString(), KMessageBox.Options options = KMessageBox.Notify)'''
        return int()
    def questionYesNoCancelWId(self, parent_id, text, caption = QString(), buttonYes = None, buttonNo = None, buttonCancel = None, dontAskAgainName = QString(), options = None):
        '''static int KMessageBox.questionYesNoCancelWId(int parent_id, QString text, QString caption = QString(), KGuiItem buttonYes = KStandardGuiItem.yes(), KGuiItem buttonNo = KStandardGuiItem.no(), KGuiItem buttonCancel = KStandardGuiItem.cancel(), QString dontAskAgainName = QString(), KMessageBox.Options options = KMessageBox.Notify)'''
        return int()
    def questionYesNoCancel(self, parent, text, caption = QString(), buttonYes = None, buttonNo = None, buttonCancel = None, dontAskAgainName = QString(), options = None):
        '''static int KMessageBox.questionYesNoCancel(QWidget parent, QString text, QString caption = QString(), KGuiItem buttonYes = KStandardGuiItem.yes(), KGuiItem buttonNo = KStandardGuiItem.no(), KGuiItem buttonCancel = KStandardGuiItem.cancel(), QString dontAskAgainName = QString(), KMessageBox.Options options = KMessageBox.Notify)'''
        return int()
    def questionYesNoWId(self, parent_id, text, caption = QString(), buttonYes = None, buttonNo = None, dontAskAgainName = QString(), options = None):
        '''static int KMessageBox.questionYesNoWId(int parent_id, QString text, QString caption = QString(), KGuiItem buttonYes = KStandardGuiItem.yes(), KGuiItem buttonNo = KStandardGuiItem.no(), QString dontAskAgainName = QString(), KMessageBox.Options options = KMessageBox.Notify)'''
        return int()
    def questionYesNo(self, parent, text, caption = QString(), buttonYes = None, buttonNo = None, dontAskAgainName = QString(), options = None):
        '''static int KMessageBox.questionYesNo(QWidget parent, QString text, QString caption = QString(), KGuiItem buttonYes = KStandardGuiItem.yes(), KGuiItem buttonNo = KStandardGuiItem.no(), QString dontAskAgainName = QString(), KMessageBox.Options options = KMessageBox.Notify)'''
        return int()
    class Options():
        """"""
        def __init__(self):
            '''KMessageBox.Options KMessageBox.Options.__init__()'''
            return KMessageBox.Options()
        def __init__(self):
            '''int KMessageBox.Options.__init__()'''
            return int()
        def __init__(self):
            '''void KMessageBox.Options.__init__()'''
        def __bool__(self):
            '''int KMessageBox.Options.__bool__()'''
            return int()
        def __ne__(self, f):
            '''bool KMessageBox.Options.__ne__(KMessageBox.Options f)'''
            return bool()
        def __eq__(self, f):
            '''bool KMessageBox.Options.__eq__(KMessageBox.Options f)'''
            return bool()
        def __invert__(self):
            '''KMessageBox.Options KMessageBox.Options.__invert__()'''
            return KMessageBox.Options()
        def __and__(self, mask):
            '''KMessageBox.Options KMessageBox.Options.__and__(int mask)'''
            return KMessageBox.Options()
        def __xor__(self, f):
            '''KMessageBox.Options KMessageBox.Options.__xor__(KMessageBox.Options f)'''
            return KMessageBox.Options()
        def __xor__(self, f):
            '''KMessageBox.Options KMessageBox.Options.__xor__(int f)'''
            return KMessageBox.Options()
        def __or__(self, f):
            '''KMessageBox.Options KMessageBox.Options.__or__(KMessageBox.Options f)'''
            return KMessageBox.Options()
        def __or__(self, f):
            '''KMessageBox.Options KMessageBox.Options.__or__(int f)'''
            return KMessageBox.Options()
        def __int__(self):
            '''int KMessageBox.Options.__int__()'''
            return int()
        def __ixor__(self, f):
            '''KMessageBox.Options KMessageBox.Options.__ixor__(KMessageBox.Options f)'''
            return KMessageBox.Options()
        def __ior__(self, f):
            '''KMessageBox.Options KMessageBox.Options.__ior__(KMessageBox.Options f)'''
            return KMessageBox.Options()
        def __iand__(self, mask):
            '''KMessageBox.Options KMessageBox.Options.__iand__(int mask)'''
            return KMessageBox.Options()


class KMessageBoxMessageHandler(QObject, KMessageHandler):
    """"""
    def __init__(self, parent = None):
        '''void KMessageBoxMessageHandler.__init__(QWidget parent = None)'''
    def message(self, messageType, text, caption):
        '''void KMessageBoxMessageHandler.message(KMessage.MessageType messageType, QString text, QString caption)'''


class KMessageWidget(QFrame):
    """"""
    # Enum KMessageWidget.MessageType
    Positive = 0
    Information = 0
    Warning = 0
    Error = 0

    def __init__(self, parent = None):
        '''void KMessageWidget.__init__(QWidget parent = None)'''
    def __init__(self, text, parent = None):
        '''void KMessageWidget.__init__(QString text, QWidget parent = None)'''
    def heightForWidth(self, width):
        '''int KMessageWidget.heightForWidth(int width)'''
        return int()
    def showEvent(self, event):
        '''void KMessageWidget.showEvent(QShowEvent event)'''
    def resizeEvent(self, event):
        '''void KMessageWidget.resizeEvent(QResizeEvent event)'''
    def event(self, event):
        '''bool KMessageWidget.event(QEvent event)'''
        return bool()
    def paintEvent(self, event):
        '''void KMessageWidget.paintEvent(QPaintEvent event)'''
    def animatedHide(self):
        '''void KMessageWidget.animatedHide()'''
    def animatedShow(self):
        '''void KMessageWidget.animatedShow()'''
    def setMessageType(self, type):
        '''void KMessageWidget.setMessageType(KMessageWidget.MessageType type)'''
    def setCloseButtonVisible(self, visible):
        '''void KMessageWidget.setCloseButtonVisible(bool visible)'''
    def setWordWrap(self, wordWrap):
        '''void KMessageWidget.setWordWrap(bool wordWrap)'''
    def setText(self, text):
        '''void KMessageWidget.setText(QString text)'''
    def minimumSizeHint(self):
        '''QSize KMessageWidget.minimumSizeHint()'''
        return QSize()
    def sizeHint(self):
        '''QSize KMessageWidget.sizeHint()'''
        return QSize()
    def removeAction(self, action):
        '''void KMessageWidget.removeAction(QAction action)'''
    def addAction(self, action):
        '''void KMessageWidget.addAction(QAction action)'''
    def messageType(self):
        '''KMessageWidget.MessageType KMessageWidget.messageType()'''
        return KMessageWidget.MessageType()
    def isCloseButtonVisible(self):
        '''bool KMessageWidget.isCloseButtonVisible()'''
        return bool()
    def wordWrap(self):
        '''bool KMessageWidget.wordWrap()'''
        return bool()
    def text(self):
        '''QString KMessageWidget.text()'''
        return QString()


class KModelIndexProxyMapper(QObject):
    """"""
    def __init__(self, leftModel, rightModel, parent = None):
        '''void KModelIndexProxyMapper.__init__(QAbstractItemModel leftModel, QAbstractItemModel rightModel, QObject parent = None)'''
    def mapSelectionRightToLeft(self, selection):
        '''QItemSelection KModelIndexProxyMapper.mapSelectionRightToLeft(QItemSelection selection)'''
        return QItemSelection()
    def mapSelectionLeftToRight(self, selection):
        '''QItemSelection KModelIndexProxyMapper.mapSelectionLeftToRight(QItemSelection selection)'''
        return QItemSelection()
    def mapRightToLeft(self, index):
        '''QModelIndex KModelIndexProxyMapper.mapRightToLeft(QModelIndex index)'''
        return QModelIndex()
    def mapLeftToRight(self, index):
        '''QModelIndex KModelIndexProxyMapper.mapLeftToRight(QModelIndex index)'''
        return QModelIndex()


class KModifierKeyInfo(QObject):
    """"""
    def __init__(self, parent = None):
        '''void KModifierKeyInfo.__init__(QObject parent = None)'''
    keyRemoved = pyqtSignal() # void keyRemoved(Qt::Key) - signal
    keyAdded = pyqtSignal() # void keyAdded(Qt::Key) - signal
    buttonPressed = pyqtSignal() # void buttonPressed(Qt::MouseButton,bool) - signal
    keyLocked = pyqtSignal() # void keyLocked(Qt::Key,bool) - signal
    keyLatched = pyqtSignal() # void keyLatched(Qt::Key,bool) - signal
    keyPressed = pyqtSignal() # void keyPressed(Qt::Key,bool) - signal
    def isButtonPressed(self, button):
        '''bool KModifierKeyInfo.isButtonPressed(Qt.MouseButton button)'''
        return bool()
    def setKeyLocked(self, key, locked):
        '''bool KModifierKeyInfo.setKeyLocked(Qt.Key key, bool locked)'''
        return bool()
    def isKeyLocked(self, key):
        '''bool KModifierKeyInfo.isKeyLocked(Qt.Key key)'''
        return bool()
    def setKeyLatched(self, key, latched):
        '''bool KModifierKeyInfo.setKeyLatched(Qt.Key key, bool latched)'''
        return bool()
    def isKeyLatched(self, key):
        '''bool KModifierKeyInfo.isKeyLatched(Qt.Key key)'''
        return bool()
    def isKeyPressed(self, key):
        '''bool KModifierKeyInfo.isKeyPressed(Qt.Key key)'''
        return bool()
    def knownKeys(self):
        '''list-of-Qt.Key KModifierKeyInfo.knownKeys()'''
        return [Qt.Key()]
    def knowsKey(self, key):
        '''bool KModifierKeyInfo.knowsKey(Qt.Key key)'''
        return bool()


class KMultiTabBar(QWidget):
    """"""
    # Enum KMultiTabBar.KMultiTabBarStyle
    VSNET = 0
    KDEV3ICON = 0
    STYLELAST = 0

    # Enum KMultiTabBar.KMultiTabBarPosition
    Left = 0
    Right = 0
    Top = 0
    Bottom = 0

    def __init__(self, pos, parent = None):
        '''void KMultiTabBar.__init__(KMultiTabBar.KMultiTabBarPosition pos, QWidget parent = None)'''
    def updateSeparator(self):
        '''void KMultiTabBar.updateSeparator()'''
    def fontChange(self):
        '''QFont KMultiTabBar.fontChange()'''
        return QFont()
    def tabStyle(self):
        '''KMultiTabBar.KMultiTabBarStyle KMultiTabBar.tabStyle()'''
        return KMultiTabBar.KMultiTabBarStyle()
    def setStyle(self, style):
        '''void KMultiTabBar.setStyle(KMultiTabBar.KMultiTabBarStyle style)'''
    def position(self):
        '''KMultiTabBar.KMultiTabBarPosition KMultiTabBar.position()'''
        return KMultiTabBar.KMultiTabBarPosition()
    def setPosition(self, pos):
        '''void KMultiTabBar.setPosition(KMultiTabBar.KMultiTabBarPosition pos)'''
    def tab(self, id):
        '''KMultiTabBarTab KMultiTabBar.tab(int id)'''
        return KMultiTabBarTab()
    def button(self, id):
        '''KMultiTabBarButton KMultiTabBar.button(int id)'''
        return KMultiTabBarButton()
    def isTabRaised(self, id):
        '''bool KMultiTabBar.isTabRaised(int id)'''
        return bool()
    def setTab(self, id, state):
        '''void KMultiTabBar.setTab(int id, bool state)'''
    def removeTab(self, id):
        '''void KMultiTabBar.removeTab(int id)'''
    def appendTab(self, pic, id = None, text = QString()):
        '''int KMultiTabBar.appendTab(QPixmap pic, int id = -1, QString text = QString())'''
        return int()
    def removeButton(self, id):
        '''void KMultiTabBar.removeButton(int id)'''
    def appendButton(self, pic, id = None, popup = None, not_used_yet = QString()):
        '''int KMultiTabBar.appendButton(QPixmap pic, int id = -1, QMenu popup = None, QString not_used_yet = QString())'''
        return int()


class KMultiTabBarButton(QPushButton):
    """"""
    def __init__(self, pic, id, parent):
        '''QString KMultiTabBarButton.__init__(QPixmap pic, int id, QWidget parent)'''
        return QString()
    def paintEvent(self):
        '''QPaintEvent KMultiTabBarButton.paintEvent()'''
        return QPaintEvent()
    def showEvent(self):
        '''QShowEvent KMultiTabBarButton.showEvent()'''
        return QShowEvent()
    def hideEvent(self):
        '''QHideEvent KMultiTabBarButton.hideEvent()'''
        return QHideEvent()
    def slotClicked(self):
        '''void KMultiTabBarButton.slotClicked()'''
    clicked = pyqtSignal() # void clicked(int) - signal
    def setText(self, text):
        '''void KMultiTabBarButton.setText(QString text)'''
    def id(self):
        '''int KMultiTabBarButton.id()'''
        return int()


class KMultiTabBarTab(KMultiTabBarButton):
    """"""
    def paintEvent(self):
        '''QPaintEvent KMultiTabBarTab.paintEvent()'''
        return QPaintEvent()
    def setIcon(self):
        '''QString KMultiTabBarTab.setIcon()'''
        return QString()
    def setIcon(self):
        '''QPixmap KMultiTabBarTab.setIcon()'''
        return QPixmap()
    def setState(self, state):
        '''void KMultiTabBarTab.setState(bool state)'''
    def setStyle(self):
        '''KMultiTabBar.KMultiTabBarStyle KMultiTabBarTab.setStyle()'''
        return KMultiTabBar.KMultiTabBarStyle()
    def setPosition(self):
        '''KMultiTabBar.KMultiTabBarPosition KMultiTabBarTab.setPosition()'''
        return KMultiTabBar.KMultiTabBarPosition()
    def minimumSizeHint(self):
        '''QSize KMultiTabBarTab.minimumSizeHint()'''
        return QSize()
    def sizeHint(self):
        '''QSize KMultiTabBarTab.sizeHint()'''
        return QSize()


class KNewPasswordDialog(KDialog):
    """"""
    def __init__(self, parent = None):
        '''void KNewPasswordDialog.__init__(QWidget parent = None)'''
    newPassword = pyqtSignal() # void newPassword(const QStringamp;) - signal
    def checkAndGetPassword(self, pwd):
        '''bool KNewPasswordDialog.checkAndGetPassword(QString pwd)'''
        return bool()
    def checkPassword(self):
        '''QString KNewPasswordDialog.checkPassword()'''
        return QString()
    def accept(self):
        '''void KNewPasswordDialog.accept()'''
    def password(self):
        '''QString KNewPasswordDialog.password()'''
        return QString()
    def passwordStrengthWarningLevel(self):
        '''int KNewPasswordDialog.passwordStrengthWarningLevel()'''
        return int()
    def setPasswordStrengthWarningLevel(self, warningLevel):
        '''void KNewPasswordDialog.setPasswordStrengthWarningLevel(int warningLevel)'''
    def reasonablePasswordLength(self):
        '''int KNewPasswordDialog.reasonablePasswordLength()'''
        return int()
    def setReasonablePasswordLength(self, reasonableLength):
        '''void KNewPasswordDialog.setReasonablePasswordLength(int reasonableLength)'''
    def maximumPasswordLength(self):
        '''int KNewPasswordDialog.maximumPasswordLength()'''
        return int()
    def setMaximumPasswordLength(self, maxLength):
        '''void KNewPasswordDialog.setMaximumPasswordLength(int maxLength)'''
    def minimumPasswordLength(self):
        '''int KNewPasswordDialog.minimumPasswordLength()'''
        return int()
    def setMinimumPasswordLength(self, minLength):
        '''void KNewPasswordDialog.setMinimumPasswordLength(int minLength)'''
    def allowEmptyPasswords(self):
        '''bool KNewPasswordDialog.allowEmptyPasswords()'''
        return bool()
    def setAllowEmptyPasswords(self, allowed):
        '''void KNewPasswordDialog.setAllowEmptyPasswords(bool allowed)'''
    def pixmap(self):
        '''QPixmap KNewPasswordDialog.pixmap()'''
        return QPixmap()
    def setPixmap(self):
        '''QPixmap KNewPasswordDialog.setPixmap()'''
        return QPixmap()
    def prompt(self):
        '''QString KNewPasswordDialog.prompt()'''
        return QString()
    def setPrompt(self, prompt):
        '''void KNewPasswordDialog.setPrompt(QString prompt)'''


class KNotification(QObject):
    """"""
    # Enum KNotification.StandardEvent
    Notification = 0
    Warning = 0
    Error = 0
    Catastrophe = 0

    # Enum KNotification.NotificationFlag
    RaiseWidgetOnActivation = 0
    CloseOnTimeout = 0
    Persistent = 0
    CloseWhenWidgetActivated = 0
    Persistant = 0
    DefaultEvent = 0

    def __init__(self, eventId, widget = None, flags = None):
        '''void KNotification.__init__(QString eventId, QWidget widget = None, KNotification.NotificationFlags flags = KNotification.CloseOnTimeout)'''
    def __init__(self, eventId, flags, parent = None):
        '''void KNotification.__init__(QString eventId, KNotification.NotificationFlags flags, QObject parent = None)'''
    def beep(self, reason = QString(), widget = None):
        '''static void KNotification.beep(QString reason = QString(), QWidget widget = None)'''
    def event(self, eventId, text = QString(), pixmap = QPixmap(), widget = None, flags = None, componentData = KComponentData()):
        '''static KNotification KNotification.event(QString eventId, QString text = QString(), QPixmap pixmap = QPixmap(), QWidget widget = None, KNotification.NotificationFlags flags = KNotification.CloseOnTimeout, KComponentData componentData = KComponentData())'''
        return KNotification()
    def event(self, eventId, text = QString(), pixmap = QPixmap(), widget = None, flags = None):
        '''static KNotification KNotification.event(KNotification.StandardEvent eventId, QString text = QString(), QPixmap pixmap = QPixmap(), QWidget widget = None, KNotification.NotificationFlags flags = KNotification.CloseOnTimeout)'''
        return KNotification()
    def event(self, eventId, title, text, pixmap = QPixmap(), widget = None, flags = None, componentData = KComponentData()):
        '''static KNotification KNotification.event(QString eventId, QString title, QString text, QPixmap pixmap = QPixmap(), QWidget widget = None, KNotification.NotificationFlags flags = KNotification.CloseOnTimeout, KComponentData componentData = KComponentData())'''
        return KNotification()
    def event(self, eventId, title, text, pixmap = QPixmap(), widget = None, flags = None):
        '''static KNotification KNotification.event(KNotification.StandardEvent eventId, QString title, QString text, QPixmap pixmap = QPixmap(), QWidget widget = None, KNotification.NotificationFlags flags = KNotification.CloseOnTimeout)'''
        return KNotification()
    def eventFilter(self, watched, event):
        '''bool KNotification.eventFilter(QObject watched, QEvent event)'''
        return bool()
    def update(self):
        '''void KNotification.update()'''
    def sendEvent(self):
        '''void KNotification.sendEvent()'''
    def deref(self):
        '''void KNotification.deref()'''
    def ref(self):
        '''void KNotification.ref()'''
    def raiseWidget(self):
        '''void KNotification.raiseWidget()'''
    def close(self):
        '''void KNotification.close()'''
    def activate(self, action = 0):
        '''void KNotification.activate(int action = 0)'''
    ignored = pyqtSignal() # void ignored() - signal
    closed = pyqtSignal() # void closed() - signal
    action3Activated = pyqtSignal() # void action3Activated() - signal
    action2Activated = pyqtSignal() # void action2Activated() - signal
    action1Activated = pyqtSignal() # void action1Activated() - signal
    activated = pyqtSignal() # void activated() - signal
    activated = pyqtSignal() # void activated(uint) - signal
    def setComponentData(self, componentData):
        '''void KNotification.setComponentData(KComponentData componentData)'''
    def setFlags(self, flags):
        '''void KNotification.setFlags(KNotification.NotificationFlags flags)'''
    def flags(self):
        '''KNotification.NotificationFlags KNotification.flags()'''
        return KNotification.NotificationFlags()
    def addContext(self, context):
        '''void KNotification.addContext(unknown-type context)'''
    def addContext(self, context_key, context_value):
        '''void KNotification.addContext(QString context_key, QString context_value)'''
    def setContexts(self, contexts):
        '''void KNotification.setContexts(list-of-tuple-of-QString-QString contexts)'''
    def contexts(self):
        '''list-of-tuple-of-QString-QString KNotification.contexts()'''
        return [tuple-of-QString-QString()]
    def setActions(self, actions):
        '''void KNotification.setActions(QStringList actions)'''
    def actions(self):
        '''QStringList KNotification.actions()'''
        return QStringList()
    def setPixmap(self, pix):
        '''void KNotification.setPixmap(QPixmap pix)'''
    def pixmap(self):
        '''QPixmap KNotification.pixmap()'''
        return QPixmap()
    def setText(self, text):
        '''void KNotification.setText(QString text)'''
    def text(self):
        '''QString KNotification.text()'''
        return QString()
    def setTitle(self, title):
        '''void KNotification.setTitle(QString title)'''
    def title(self):
        '''QString KNotification.title()'''
        return QString()
    def eventId(self):
        '''QString KNotification.eventId()'''
        return QString()
    def setWidget(self, widget):
        '''void KNotification.setWidget(QWidget widget)'''
    def widget(self):
        '''QWidget KNotification.widget()'''
        return QWidget()
    class NotificationFlags():
        """"""
        def __init__(self):
            '''KNotification.NotificationFlags KNotification.NotificationFlags.__init__()'''
            return KNotification.NotificationFlags()
        def __init__(self):
            '''int KNotification.NotificationFlags.__init__()'''
            return int()
        def __init__(self):
            '''void KNotification.NotificationFlags.__init__()'''
        def __bool__(self):
            '''int KNotification.NotificationFlags.__bool__()'''
            return int()
        def __ne__(self, f):
            '''bool KNotification.NotificationFlags.__ne__(KNotification.NotificationFlags f)'''
            return bool()
        def __eq__(self, f):
            '''bool KNotification.NotificationFlags.__eq__(KNotification.NotificationFlags f)'''
            return bool()
        def __invert__(self):
            '''KNotification.NotificationFlags KNotification.NotificationFlags.__invert__()'''
            return KNotification.NotificationFlags()
        def __and__(self, mask):
            '''KNotification.NotificationFlags KNotification.NotificationFlags.__and__(int mask)'''
            return KNotification.NotificationFlags()
        def __xor__(self, f):
            '''KNotification.NotificationFlags KNotification.NotificationFlags.__xor__(KNotification.NotificationFlags f)'''
            return KNotification.NotificationFlags()
        def __xor__(self, f):
            '''KNotification.NotificationFlags KNotification.NotificationFlags.__xor__(int f)'''
            return KNotification.NotificationFlags()
        def __or__(self, f):
            '''KNotification.NotificationFlags KNotification.NotificationFlags.__or__(KNotification.NotificationFlags f)'''
            return KNotification.NotificationFlags()
        def __or__(self, f):
            '''KNotification.NotificationFlags KNotification.NotificationFlags.__or__(int f)'''
            return KNotification.NotificationFlags()
        def __int__(self):
            '''int KNotification.NotificationFlags.__int__()'''
            return int()
        def __ixor__(self, f):
            '''KNotification.NotificationFlags KNotification.NotificationFlags.__ixor__(KNotification.NotificationFlags f)'''
            return KNotification.NotificationFlags()
        def __ior__(self, f):
            '''KNotification.NotificationFlags KNotification.NotificationFlags.__ior__(KNotification.NotificationFlags f)'''
            return KNotification.NotificationFlags()
        def __iand__(self, mask):
            '''KNotification.NotificationFlags KNotification.NotificationFlags.__iand__(int mask)'''
            return KNotification.NotificationFlags()


class KNotificationRestrictions(QObject):
    """"""
    # Enum KNotificationRestrictions.Service
    NoServices = 0
    ScreenSaver = 0
    MessagingPopups = 0
    Notifications = 0
    CriticalNotifications = 0
    NonCriticalServices = 0
    AllServices = 0

    def __init__(self, control = None, parent = None):
        '''void KNotificationRestrictions.__init__(KNotificationRestrictions.Services control = KNotificationRestrictions.NonCriticalServices, QObject parent = None)'''
    class Services():
        """"""
        def __init__(self):
            '''KNotificationRestrictions.Services KNotificationRestrictions.Services.__init__()'''
            return KNotificationRestrictions.Services()
        def __init__(self):
            '''int KNotificationRestrictions.Services.__init__()'''
            return int()
        def __init__(self):
            '''void KNotificationRestrictions.Services.__init__()'''
        def __bool__(self):
            '''int KNotificationRestrictions.Services.__bool__()'''
            return int()
        def __ne__(self, f):
            '''bool KNotificationRestrictions.Services.__ne__(KNotificationRestrictions.Services f)'''
            return bool()
        def __eq__(self, f):
            '''bool KNotificationRestrictions.Services.__eq__(KNotificationRestrictions.Services f)'''
            return bool()
        def __invert__(self):
            '''KNotificationRestrictions.Services KNotificationRestrictions.Services.__invert__()'''
            return KNotificationRestrictions.Services()
        def __and__(self, mask):
            '''KNotificationRestrictions.Services KNotificationRestrictions.Services.__and__(int mask)'''
            return KNotificationRestrictions.Services()
        def __xor__(self, f):
            '''KNotificationRestrictions.Services KNotificationRestrictions.Services.__xor__(KNotificationRestrictions.Services f)'''
            return KNotificationRestrictions.Services()
        def __xor__(self, f):
            '''KNotificationRestrictions.Services KNotificationRestrictions.Services.__xor__(int f)'''
            return KNotificationRestrictions.Services()
        def __or__(self, f):
            '''KNotificationRestrictions.Services KNotificationRestrictions.Services.__or__(KNotificationRestrictions.Services f)'''
            return KNotificationRestrictions.Services()
        def __or__(self, f):
            '''KNotificationRestrictions.Services KNotificationRestrictions.Services.__or__(int f)'''
            return KNotificationRestrictions.Services()
        def __int__(self):
            '''int KNotificationRestrictions.Services.__int__()'''
            return int()
        def __ixor__(self, f):
            '''KNotificationRestrictions.Services KNotificationRestrictions.Services.__ixor__(KNotificationRestrictions.Services f)'''
            return KNotificationRestrictions.Services()
        def __ior__(self, f):
            '''KNotificationRestrictions.Services KNotificationRestrictions.Services.__ior__(KNotificationRestrictions.Services f)'''
            return KNotificationRestrictions.Services()
        def __iand__(self, mask):
            '''KNotificationRestrictions.Services KNotificationRestrictions.Services.__iand__(int mask)'''
            return KNotificationRestrictions.Services()


class KNumInput(QWidget):
    """"""
    def __init__(self, parent = None):
        '''void KNumInput.__init__(QWidget parent = None)'''
    def __init__(self, parent, below):
        '''void KNumInput.__init__(QWidget parent, KNumInput below)'''
    def doLayout(self):
        '''abstract void KNumInput.doLayout()'''
    def layout(self, deep):
        '''void KNumInput.layout(bool deep)'''
    def slider(self):
        '''QSlider KNumInput.slider()'''
        return QSlider()
    def sizeHint(self):
        '''QSize KNumInput.sizeHint()'''
        return QSize()
    def setSteps(self, minor, major):
        '''void KNumInput.setSteps(int minor, int major)'''
    def showSlider(self):
        '''bool KNumInput.showSlider()'''
        return bool()
    def label(self):
        '''QString KNumInput.label()'''
        return QString()
    def setLabel(self, label, a = None):
        '''void KNumInput.setLabel(QString label, Qt.Alignment a = Qt.AlignLeft|Qt.AlignTop)'''


class KIntNumInput(KNumInput):
    """"""
    def __init__(self, parent = None):
        '''void KIntNumInput.__init__(QWidget parent = None)'''
    def __init__(self, value, parent = None, base = 10):
        '''void KIntNumInput.__init__(int value, QWidget parent = None, int base = 10)'''
    def __init__(self, below, value, parent, base = 10):
        '''void KIntNumInput.__init__(KNumInput below, int value, QWidget parent, int base = 10)'''
    def resizeEvent(self):
        '''QResizeEvent KIntNumInput.resizeEvent()'''
        return QResizeEvent()
    def doLayout(self):
        '''void KIntNumInput.doLayout()'''
    def spinBox(self):
        '''QSpinBox KIntNumInput.spinBox()'''
        return QSpinBox()
    relativeValueChanged = pyqtSignal() # void relativeValueChanged(double) - signal
    valueChanged = pyqtSignal() # void valueChanged(int) - signal
    def setEditFocus(self, mark = True):
        '''void KIntNumInput.setEditFocus(bool mark = True)'''
    def setPrefix(self, prefix):
        '''void KIntNumInput.setPrefix(QString prefix)'''
    def setSuffix(self, suffix):
        '''void KIntNumInput.setSuffix(QString suffix)'''
    def setSuffix(self, suffix):
        '''void KIntNumInput.setSuffix(KLocalizedString suffix)'''
    def setReferencePoint(self):
        '''int KIntNumInput.setReferencePoint()'''
        return int()
    def setRelativeValue(self):
        '''float KIntNumInput.setRelativeValue()'''
        return float()
    def setValue(self):
        '''int KIntNumInput.setValue()'''
        return int()
    def minimumSizeHint(self):
        '''QSize KIntNumInput.minimumSizeHint()'''
        return QSize()
    def setLabel(self, label, a = None):
        '''void KIntNumInput.setLabel(QString label, Qt.Alignment a = Qt.AlignLeft|Qt.AlignTop)'''
    def setSpecialValueText(self, text):
        '''void KIntNumInput.setSpecialValueText(QString text)'''
    def setSingleStep(self, step):
        '''void KIntNumInput.setSingleStep(int step)'''
    def singleStep(self):
        '''int KIntNumInput.singleStep()'''
        return int()
    def maximum(self):
        '''int KIntNumInput.maximum()'''
        return int()
    def setMaximum(self, max):
        '''void KIntNumInput.setMaximum(int max)'''
    def minimum(self):
        '''int KIntNumInput.minimum()'''
        return int()
    def setMinimum(self, min):
        '''void KIntNumInput.setMinimum(int min)'''
    def setSliderEnabled(self, enabled = True):
        '''void KIntNumInput.setSliderEnabled(bool enabled = True)'''
    def setRange(self, min, max, singleStep = 1):
        '''void KIntNumInput.setRange(int min, int max, int singleStep = 1)'''
    def setRange(self, min, max, singleStep, slider):
        '''void KIntNumInput.setRange(int min, int max, int singleStep, bool slider)'''
    def specialValueText(self):
        '''QString KIntNumInput.specialValueText()'''
        return QString()
    def prefix(self):
        '''QString KIntNumInput.prefix()'''
        return QString()
    def suffix(self):
        '''QString KIntNumInput.suffix()'''
        return QString()
    def referencePoint(self):
        '''int KIntNumInput.referencePoint()'''
        return int()
    def relativeValue(self):
        '''float KIntNumInput.relativeValue()'''
        return float()
    def value(self):
        '''int KIntNumInput.value()'''
        return int()


class KDoubleNumInput(KNumInput):
    """"""
    def __init__(self, parent = None):
        '''void KDoubleNumInput.__init__(QWidget parent = None)'''
    def __init__(self, lower, upper, value, parent = None, singleStep = None, precision = 2):
        '''void KDoubleNumInput.__init__(float lower, float upper, float value, QWidget parent = None, float singleStep = 0.01, int precision = 2)'''
    def __init__(self, below, lower, upper, value, parent = None, singleStep = None, precision = 2):
        '''void KDoubleNumInput.__init__(KNumInput below, float lower, float upper, float value, QWidget parent = None, float singleStep = 0.02, int precision = 2)'''
    def resizeEvent(self):
        '''QResizeEvent KDoubleNumInput.resizeEvent()'''
        return QResizeEvent()
    def doLayout(self):
        '''void KDoubleNumInput.doLayout()'''
    relativeValueChanged = pyqtSignal() # void relativeValueChanged(double) - signal
    valueChanged = pyqtSignal() # void valueChanged(double) - signal
    def setPrefix(self, prefix):
        '''void KDoubleNumInput.setPrefix(QString prefix)'''
    def setSuffix(self, suffix):
        '''void KDoubleNumInput.setSuffix(QString suffix)'''
    def setReferencePoint(self, ref):
        '''void KDoubleNumInput.setReferencePoint(float ref)'''
    def setRelativeValue(self):
        '''float KDoubleNumInput.setRelativeValue()'''
        return float()
    def setValue(self):
        '''float KDoubleNumInput.setValue()'''
        return float()
    def setExponentRatio(self, dbl):
        '''void KDoubleNumInput.setExponentRatio(float dbl)'''
    def exponentRatio(self):
        '''float KDoubleNumInput.exponentRatio()'''
        return float()
    def minimumSizeHint(self):
        '''QSize KDoubleNumInput.minimumSizeHint()'''
        return QSize()
    def setLabel(self, label, a = None):
        '''void KDoubleNumInput.setLabel(QString label, Qt.Alignment a = Qt.AlignLeft|Qt.AlignTop)'''
    def setSpecialValueText(self, text):
        '''void KDoubleNumInput.setSpecialValueText(QString text)'''
    def relativeValue(self):
        '''float KDoubleNumInput.relativeValue()'''
        return float()
    def referencePoint(self):
        '''float KDoubleNumInput.referencePoint()'''
        return float()
    def setPrecision(self, precision):
        '''void KDoubleNumInput.setPrecision(int precision)'''
    def setDecimals(self, decimals):
        '''void KDoubleNumInput.setDecimals(int decimals)'''
    def setSingleStep(self, singleStep):
        '''void KDoubleNumInput.setSingleStep(float singleStep)'''
    def singleStep(self):
        '''float KDoubleNumInput.singleStep()'''
        return float()
    def maximum(self):
        '''float KDoubleNumInput.maximum()'''
        return float()
    def setMaximum(self, max):
        '''void KDoubleNumInput.setMaximum(float max)'''
    def minimum(self):
        '''float KDoubleNumInput.minimum()'''
        return float()
    def setMinimum(self, min):
        '''void KDoubleNumInput.setMinimum(float min)'''
    def setSliderEnabled(self, enabled):
        '''void KDoubleNumInput.setSliderEnabled(bool enabled)'''
    def setRange(self, min, max, singleStep = 1, slider = True):
        '''void KDoubleNumInput.setRange(float min, float max, float singleStep = 1, bool slider = True)'''
    def specialValueText(self):
        '''QString KDoubleNumInput.specialValueText()'''
        return QString()
    def decimals(self):
        '''int KDoubleNumInput.decimals()'''
        return int()
    def prefix(self):
        '''QString KDoubleNumInput.prefix()'''
        return QString()
    def suffix(self):
        '''QString KDoubleNumInput.suffix()'''
        return QString()
    def value(self):
        '''float KDoubleNumInput.value()'''
        return float()


class KIntSpinBox(QSpinBox):
    """"""
    def __init__(self, parent = None):
        '''void KIntSpinBox.__init__(QWidget parent = None)'''
    def __init__(self, lower, upper, singleStep, value, parent, base = 10):
        '''void KIntSpinBox.__init__(int lower, int upper, int singleStep, int value, QWidget parent, int base = 10)'''
    def valueFromText(self, text):
        '''int KIntSpinBox.valueFromText(QString text)'''
        return int()
    def textFromValue(self):
        '''int KIntSpinBox.textFromValue()'''
        return int()
    def setSuffix(self, suffix):
        '''void KIntSpinBox.setSuffix(KLocalizedString suffix)'''
    def setEditFocus(self, mark):
        '''void KIntSpinBox.setEditFocus(bool mark)'''
    def base(self):
        '''int KIntSpinBox.base()'''
        return int()
    def setBase(self, base):
        '''void KIntSpinBox.setBase(int base)'''


class KIntValidator(QValidator):
    """"""
    def __init__(self, parent, base = 10):
        '''void KIntValidator.__init__(QWidget parent, int base = 10)'''
    def __init__(self, bottom, top, parent, base = 10):
        '''void KIntValidator.__init__(int bottom, int top, QWidget parent, int base = 10)'''
    def base(self):
        '''int KIntValidator.base()'''
        return int()
    def top(self):
        '''int KIntValidator.top()'''
        return int()
    def bottom(self):
        '''int KIntValidator.bottom()'''
        return int()
    def setBase(self, base):
        '''void KIntValidator.setBase(int base)'''
    def setRange(self, bottom, top):
        '''void KIntValidator.setRange(int bottom, int top)'''
    def fixup(self):
        '''QString KIntValidator.fixup()'''
        return QString()
    def validate(self):
        '''int KIntValidator.validate()'''
        return int()


class KFloatValidator(QValidator):
    """"""
    def __init__(self, parent):
        '''void KFloatValidator.__init__(QWidget parent)'''
    def __init__(self, bottom, top, parent):
        '''void KFloatValidator.__init__(float bottom, float top, QWidget parent)'''
    def __init__(self, bottom, top, localeAware, parent):
        '''void KFloatValidator.__init__(float bottom, float top, bool localeAware, QWidget parent)'''
    def acceptLocalizedNumbers(self):
        '''bool KFloatValidator.acceptLocalizedNumbers()'''
        return bool()
    def setAcceptLocalizedNumbers(self, b):
        '''void KFloatValidator.setAcceptLocalizedNumbers(bool b)'''
    def top(self):
        '''float KFloatValidator.top()'''
        return float()
    def bottom(self):
        '''float KFloatValidator.bottom()'''
        return float()
    def setRange(self, bottom, top):
        '''void KFloatValidator.setRange(float bottom, float top)'''
    def fixup(self):
        '''QString KFloatValidator.fixup()'''
        return QString()
    def validate(self):
        '''int KFloatValidator.validate()'''
        return int()


class KDoubleValidator(QDoubleValidator):
    """"""
    def __init__(self, parent):
        '''void KDoubleValidator.__init__(QObject parent)'''
    def __init__(self, bottom, top, decimals, parent):
        '''void KDoubleValidator.__init__(float bottom, float top, int decimals, QObject parent)'''
    def setAcceptLocalizedNumbers(self, accept):
        '''void KDoubleValidator.setAcceptLocalizedNumbers(bool accept)'''
    def acceptLocalizedNumbers(self):
        '''bool KDoubleValidator.acceptLocalizedNumbers()'''
        return bool()
    def validate(self, input, pos):
        '''QValidator.State KDoubleValidator.validate(QString input, int pos)'''
        return QValidator.State()


class KPageModel(QAbstractItemModel):
    """"""
    # Enum KPageModel.Role
    HeaderRole = 0
    WidgetRole = 0

    def __init__(self, parent = None):
        '''void KPageModel.__init__(QObject parent = None)'''


class KPageView(QWidget):
    """"""
    # Enum KPageView.FaceType
    Auto = 0
    Plain = 0
    List = 0
    Tree = 0
    Tabbed = 0

    def __init__(self, parent = None):
        '''void KPageView.__init__(QWidget parent = None)'''
    def viewPosition(self):
        '''Qt.Alignment KPageView.viewPosition()'''
        return Qt.Alignment()
    def showPageHeader(self):
        '''bool KPageView.showPageHeader()'''
        return bool()
    def createView(self):
        '''QAbstractItemView KPageView.createView()'''
        return QAbstractItemView()
    currentPageChanged = pyqtSignal() # void currentPageChanged(const QModelIndexamp;,const QModelIndexamp;) - signal
    def setDefaultWidget(self, widget):
        '''void KPageView.setDefaultWidget(QWidget widget)'''
    def itemDelegate(self):
        '''QAbstractItemDelegate KPageView.itemDelegate()'''
        return QAbstractItemDelegate()
    def setItemDelegate(self, delegate):
        '''void KPageView.setItemDelegate(QAbstractItemDelegate delegate)'''
    def currentPage(self):
        '''QModelIndex KPageView.currentPage()'''
        return QModelIndex()
    def setCurrentPage(self, index):
        '''void KPageView.setCurrentPage(QModelIndex index)'''
    def faceType(self):
        '''KPageView.FaceType KPageView.faceType()'''
        return KPageView.FaceType()
    def setFaceType(self, faceType):
        '''void KPageView.setFaceType(KPageView.FaceType faceType)'''
    def model(self):
        '''QAbstractItemModel KPageView.model()'''
        return QAbstractItemModel()
    def setModel(self, model):
        '''void KPageView.setModel(QAbstractItemModel model)'''


class KPageWidget(KPageView):
    """"""
    def __init__(self, parent = None):
        '''void KPageWidget.__init__(QWidget parent = None)'''
    pageRemoved = pyqtSignal() # void pageRemoved(KPageWidgetItem *) - signal
    pageToggled = pyqtSignal() # void pageToggled(KPageWidgetItem *,bool) - signal
    currentPageChanged = pyqtSignal() # void currentPageChanged(KPageWidgetItem *,KPageWidgetItem *) - signal
    def currentPage(self):
        '''KPageWidgetItem KPageWidget.currentPage()'''
        return KPageWidgetItem()
    def setCurrentPage(self, item):
        '''void KPageWidget.setCurrentPage(KPageWidgetItem item)'''
    def removePage(self, item):
        '''void KPageWidget.removePage(KPageWidgetItem item)'''
    def addSubPage(self, parent, widget, name):
        '''KPageWidgetItem KPageWidget.addSubPage(KPageWidgetItem parent, QWidget widget, QString name)'''
        return KPageWidgetItem()
    def addSubPage(self, parent, item):
        '''void KPageWidget.addSubPage(KPageWidgetItem parent, KPageWidgetItem item)'''
    def insertPage(self, before, widget, name):
        '''KPageWidgetItem KPageWidget.insertPage(KPageWidgetItem before, QWidget widget, QString name)'''
        return KPageWidgetItem()
    def insertPage(self, before, item):
        '''void KPageWidget.insertPage(KPageWidgetItem before, KPageWidgetItem item)'''
    def addPage(self, widget, name):
        '''KPageWidgetItem KPageWidget.addPage(QWidget widget, QString name)'''
        return KPageWidgetItem()
    def addPage(self, item):
        '''void KPageWidget.addPage(KPageWidgetItem item)'''


class KPageWidgetItem(QObject):
    """"""
    def __init__(self, widget):
        '''void KPageWidgetItem.__init__(QWidget widget)'''
    def __init__(self, widget, name):
        '''void KPageWidgetItem.__init__(QWidget widget, QString name)'''
    toggled = pyqtSignal() # void toggled(bool) - signal
    changed = pyqtSignal() # void changed() - signal
    def setChecked(self, checked):
        '''void KPageWidgetItem.setChecked(bool checked)'''
    def setEnabled(self):
        '''bool KPageWidgetItem.setEnabled()'''
        return bool()
    def isEnabled(self):
        '''bool KPageWidgetItem.isEnabled()'''
        return bool()
    def isChecked(self):
        '''bool KPageWidgetItem.isChecked()'''
        return bool()
    def isCheckable(self):
        '''bool KPageWidgetItem.isCheckable()'''
        return bool()
    def setCheckable(self, checkable):
        '''void KPageWidgetItem.setCheckable(bool checkable)'''
    def icon(self):
        '''KIcon KPageWidgetItem.icon()'''
        return KIcon()
    def setIcon(self, icon):
        '''void KPageWidgetItem.setIcon(KIcon icon)'''
    def header(self):
        '''QString KPageWidgetItem.header()'''
        return QString()
    def setHeader(self, header):
        '''void KPageWidgetItem.setHeader(QString header)'''
    def name(self):
        '''QString KPageWidgetItem.name()'''
        return QString()
    def setName(self, name):
        '''void KPageWidgetItem.setName(QString name)'''
    def widget(self):
        '''QWidget KPageWidgetItem.widget()'''
        return QWidget()


class KPageWidgetModel(KPageModel):
    """"""
    def __init__(self, parent = None):
        '''void KPageWidgetModel.__init__(QObject parent = None)'''
    toggled = pyqtSignal() # void toggled(KPageWidgetItem *,bool) - signal
    def item(self, index):
        '''KPageWidgetItem KPageWidgetModel.item(QModelIndex index)'''
        return KPageWidgetItem()
    def rowCount(self, parent = QModelIndex()):
        '''int KPageWidgetModel.rowCount(QModelIndex parent = QModelIndex())'''
        return int()
    def parent(self, index):
        '''QModelIndex KPageWidgetModel.parent(QModelIndex index)'''
        return QModelIndex()
    def index(self, row, column, parent = QModelIndex()):
        '''QModelIndex KPageWidgetModel.index(int row, int column, QModelIndex parent = QModelIndex())'''
        return QModelIndex()
    def index(self, item):
        '''QModelIndex KPageWidgetModel.index(KPageWidgetItem item)'''
        return QModelIndex()
    def flags(self, index):
        '''Qt.ItemFlags KPageWidgetModel.flags(QModelIndex index)'''
        return Qt.ItemFlags()
    def setData(self, index, value, role = None):
        '''bool KPageWidgetModel.setData(QModelIndex index, QVariant value, int role = Qt.EditRole)'''
        return bool()
    def data(self, index, role = None):
        '''QVariant KPageWidgetModel.data(QModelIndex index, int role = Qt.DisplayRole)'''
        return QVariant()
    def columnCount(self, parent = QModelIndex()):
        '''int KPageWidgetModel.columnCount(QModelIndex parent = QModelIndex())'''
        return int()
    def removePage(self, item):
        '''void KPageWidgetModel.removePage(KPageWidgetItem item)'''
    def addSubPage(self, parent, widget, name):
        '''KPageWidgetItem KPageWidgetModel.addSubPage(KPageWidgetItem parent, QWidget widget, QString name)'''
        return KPageWidgetItem()
    def addSubPage(self, parent, item):
        '''void KPageWidgetModel.addSubPage(KPageWidgetItem parent, KPageWidgetItem item)'''
    def insertPage(self, before, widget, name):
        '''KPageWidgetItem KPageWidgetModel.insertPage(KPageWidgetItem before, QWidget widget, QString name)'''
        return KPageWidgetItem()
    def insertPage(self, before, item):
        '''void KPageWidgetModel.insertPage(KPageWidgetItem before, KPageWidgetItem item)'''
    def addPage(self, widget, name):
        '''KPageWidgetItem KPageWidgetModel.addPage(QWidget widget, QString name)'''
        return KPageWidgetItem()
    def addPage(self, item):
        '''void KPageWidgetModel.addPage(KPageWidgetItem item)'''


class KPassivePopup(QFrame):
    """"""
    # Enum KPassivePopup.PopupStyle
    Boxed = 0
    Balloon = 0
    CustomStyle = 0

    def __init__(self, parent = None, f = 0):
        '''void KPassivePopup.__init__(QWidget parent = None, Qt.WindowFlags f = 0)'''
    def __init__(self, parent):
        '''void KPassivePopup.__init__(int parent)'''
    def paintEvent(self, pe):
        '''void KPassivePopup.paintEvent(QPaintEvent pe)'''
    def updateMask(self):
        '''void KPassivePopup.updateMask()'''
    def mouseReleaseEvent(self, e):
        '''void KPassivePopup.mouseReleaseEvent(QMouseEvent e)'''
    def calculateNearbyPoint(self, target):
        '''QPoint KPassivePopup.calculateNearbyPoint(QRect target)'''
        return QPoint()
    def moveNear(self, target):
        '''void KPassivePopup.moveNear(QRect target)'''
    def hideEvent(self):
        '''QHideEvent KPassivePopup.hideEvent()'''
        return QHideEvent()
    def positionSelf(self):
        '''void KPassivePopup.positionSelf()'''
    clicked = pyqtSignal() # void clicked() - signal
    clicked = pyqtSignal() # void clicked(const QPointamp;) - signal
    def setVisible(self, visible):
        '''void KPassivePopup.setVisible(bool visible)'''
    def show(self):
        '''void KPassivePopup.show()'''
    def show(self, p):
        '''void KPassivePopup.show(QPoint p)'''
    def setPopupStyle(self, popupstyle):
        '''void KPassivePopup.setPopupStyle(int popupstyle)'''
    def setTimeout(self, delay):
        '''void KPassivePopup.setTimeout(int delay)'''
    def message(self, text, parent):
        '''static KPassivePopup KPassivePopup.message(QString text, QWidget parent)'''
        return KPassivePopup()
    def message(self, text, parent):
        '''static KPassivePopup KPassivePopup.message(QString text, QSystemTrayIcon parent)'''
        return KPassivePopup()
    def message(self, caption, text, parent):
        '''static KPassivePopup KPassivePopup.message(QString caption, QString text, QWidget parent)'''
        return KPassivePopup()
    def message(self, caption, text, parent):
        '''static KPassivePopup KPassivePopup.message(QString caption, QString text, QSystemTrayIcon parent)'''
        return KPassivePopup()
    def message(self, caption, text, icon, parent, timeout = None):
        '''static KPassivePopup KPassivePopup.message(QString caption, QString text, QPixmap icon, QWidget parent, int timeout = -1)'''
        return KPassivePopup()
    def message(self, caption, text, icon, parent, timeout = None):
        '''static KPassivePopup KPassivePopup.message(QString caption, QString text, QPixmap icon, QSystemTrayIcon parent, int timeout = -1)'''
        return KPassivePopup()
    def message(self, caption, text, icon, parent, timeout = None):
        '''static KPassivePopup KPassivePopup.message(QString caption, QString text, QPixmap icon, int parent, int timeout = -1)'''
        return KPassivePopup()
    def message(self, popupStyle, text, parent):
        '''static KPassivePopup KPassivePopup.message(int popupStyle, QString text, QWidget parent)'''
        return KPassivePopup()
    def message(self, popupStyle, text, parent):
        '''static KPassivePopup KPassivePopup.message(int popupStyle, QString text, QSystemTrayIcon parent)'''
        return KPassivePopup()
    def message(self, popupStyle, caption, text, parent):
        '''static KPassivePopup KPassivePopup.message(int popupStyle, QString caption, QString text, QSystemTrayIcon parent)'''
        return KPassivePopup()
    def message(self, popupStyle, caption, text, parent):
        '''static KPassivePopup KPassivePopup.message(int popupStyle, QString caption, QString text, QWidget parent)'''
        return KPassivePopup()
    def message(self, popupStyle, caption, text, icon, parent, timeout = None):
        '''static KPassivePopup KPassivePopup.message(int popupStyle, QString caption, QString text, QPixmap icon, QWidget parent, int timeout = -1)'''
        return KPassivePopup()
    def message(self, popupStyle, caption, text, icon, parent, timeout = None):
        '''static KPassivePopup KPassivePopup.message(int popupStyle, QString caption, QString text, QPixmap icon, QSystemTrayIcon parent, int timeout = -1)'''
        return KPassivePopup()
    def message(self, popupStyle, caption, text, icon, parent, timeout = None):
        '''static KPassivePopup KPassivePopup.message(int popupStyle, QString caption, QString text, QPixmap icon, int parent, int timeout = -1)'''
        return KPassivePopup()
    def setAnchor(self, anchor):
        '''void KPassivePopup.setAnchor(QPoint anchor)'''
    def anchor(self):
        '''QPoint KPassivePopup.anchor()'''
        return QPoint()
    def defaultArea(self):
        '''QRect KPassivePopup.defaultArea()'''
        return QRect()
    def autoDelete(self):
        '''bool KPassivePopup.autoDelete()'''
        return bool()
    def setAutoDelete(self, autoDelete):
        '''void KPassivePopup.setAutoDelete(bool autoDelete)'''
    def timeout(self):
        '''int KPassivePopup.timeout()'''
        return int()
    def view(self):
        '''QWidget KPassivePopup.view()'''
        return QWidget()
    def standardView(self, caption, text, icon, parent = None):
        '''KVBox KPassivePopup.standardView(QString caption, QString text, QPixmap icon, QWidget parent = None)'''
        return KVBox()
    def setView(self, child):
        '''void KPassivePopup.setView(QWidget child)'''
    def setView(self, caption, text = QString()):
        '''void KPassivePopup.setView(QString caption, QString text = QString())'''
    def setView(self, caption, text, icon):
        '''void KPassivePopup.setView(QString caption, QString text, QPixmap icon)'''


class KPassivePopupMessageHandler(QObject, KMessageHandler):
    """"""
    def __init__(self, parent = None):
        '''void KPassivePopupMessageHandler.__init__(QWidget parent = None)'''
    def message(self, messageType, text, caption):
        '''void KPassivePopupMessageHandler.message(KMessage.MessageType messageType, QString text, QString caption)'''


class KPasswordDialog(KDialog):
    """"""
    # Enum KPasswordDialog.ErrorType
    UnknownError = 0
    UsernameError = 0
    PasswordError = 0
    FatalError = 0
    DomainError = 0

    # Enum KPasswordDialog.KPasswordDialogFlag
    NoFlags = 0
    ShowKeepPassword = 0
    ShowUsernameLine = 0
    UsernameReadOnly = 0
    ShowAnonymousLoginCheckBox = 0
    ShowDomainLine = 0
    DomainReadOnly = 0

    def __init__(self, parent = None, flags = 0, otherButtons = 0):
        '''void KPasswordDialog.__init__(QWidget parent = None, KPasswordDialog.KPasswordDialogFlags flags = 0, KDialog.ButtonCodes otherButtons = 0)'''
    def checkPassword(self):
        '''bool KPasswordDialog.checkPassword()'''
        return bool()
    gotUsernameAndPassword = pyqtSignal() # void gotUsernameAndPassword(const QStringamp;,const QStringamp;,bool) - signal
    gotPassword = pyqtSignal() # void gotPassword(const QStringamp;,bool) - signal
    def accept(self):
        '''void KPasswordDialog.accept()'''
    def setKnownLogins(self, knownLogins):
        '''void KPasswordDialog.setKnownLogins(dict-of-QString-QString knownLogins)'''
    def setPassword(self, password):
        '''void KPasswordDialog.setPassword(QString password)'''
    def setUsernameReadOnly(self, readOnly):
        '''void KPasswordDialog.setUsernameReadOnly(bool readOnly)'''
    def setKeepPassword(self, b):
        '''void KPasswordDialog.setKeepPassword(bool b)'''
    def keepPassword(self):
        '''bool KPasswordDialog.keepPassword()'''
        return bool()
    def anonymousMode(self):
        '''bool KPasswordDialog.anonymousMode()'''
        return bool()
    def setAnonymousMode(self, anonymous):
        '''void KPasswordDialog.setAnonymousMode(bool anonymous)'''
    def domain(self):
        '''QString KPasswordDialog.domain()'''
        return QString()
    def setDomain(self):
        '''QString KPasswordDialog.setDomain()'''
        return QString()
    def username(self):
        '''QString KPasswordDialog.username()'''
        return QString()
    def setUsername(self):
        '''QString KPasswordDialog.setUsername()'''
        return QString()
    def password(self):
        '''QString KPasswordDialog.password()'''
        return QString()
    def showErrorMessage(self, message, type = None):
        '''void KPasswordDialog.showErrorMessage(QString message, KPasswordDialog.ErrorType type = KPasswordDialog.PasswordError)'''
    def addCommentLine(self, label, comment):
        '''void KPasswordDialog.addCommentLine(QString label, QString comment)'''
    def pixmap(self):
        '''QPixmap KPasswordDialog.pixmap()'''
        return QPixmap()
    def setPixmap(self):
        '''QPixmap KPasswordDialog.setPixmap()'''
        return QPixmap()
    def prompt(self):
        '''QString KPasswordDialog.prompt()'''
        return QString()
    def setPrompt(self, prompt):
        '''void KPasswordDialog.setPrompt(QString prompt)'''
    class KPasswordDialogFlags():
        """"""
        def __init__(self):
            '''KPasswordDialog.KPasswordDialogFlags KPasswordDialog.KPasswordDialogFlags.__init__()'''
            return KPasswordDialog.KPasswordDialogFlags()
        def __init__(self):
            '''int KPasswordDialog.KPasswordDialogFlags.__init__()'''
            return int()
        def __init__(self):
            '''void KPasswordDialog.KPasswordDialogFlags.__init__()'''
        def __bool__(self):
            '''int KPasswordDialog.KPasswordDialogFlags.__bool__()'''
            return int()
        def __ne__(self, f):
            '''bool KPasswordDialog.KPasswordDialogFlags.__ne__(KPasswordDialog.KPasswordDialogFlags f)'''
            return bool()
        def __eq__(self, f):
            '''bool KPasswordDialog.KPasswordDialogFlags.__eq__(KPasswordDialog.KPasswordDialogFlags f)'''
            return bool()
        def __invert__(self):
            '''KPasswordDialog.KPasswordDialogFlags KPasswordDialog.KPasswordDialogFlags.__invert__()'''
            return KPasswordDialog.KPasswordDialogFlags()
        def __and__(self, mask):
            '''KPasswordDialog.KPasswordDialogFlags KPasswordDialog.KPasswordDialogFlags.__and__(int mask)'''
            return KPasswordDialog.KPasswordDialogFlags()
        def __xor__(self, f):
            '''KPasswordDialog.KPasswordDialogFlags KPasswordDialog.KPasswordDialogFlags.__xor__(KPasswordDialog.KPasswordDialogFlags f)'''
            return KPasswordDialog.KPasswordDialogFlags()
        def __xor__(self, f):
            '''KPasswordDialog.KPasswordDialogFlags KPasswordDialog.KPasswordDialogFlags.__xor__(int f)'''
            return KPasswordDialog.KPasswordDialogFlags()
        def __or__(self, f):
            '''KPasswordDialog.KPasswordDialogFlags KPasswordDialog.KPasswordDialogFlags.__or__(KPasswordDialog.KPasswordDialogFlags f)'''
            return KPasswordDialog.KPasswordDialogFlags()
        def __or__(self, f):
            '''KPasswordDialog.KPasswordDialogFlags KPasswordDialog.KPasswordDialogFlags.__or__(int f)'''
            return KPasswordDialog.KPasswordDialogFlags()
        def __int__(self):
            '''int KPasswordDialog.KPasswordDialogFlags.__int__()'''
            return int()
        def __ixor__(self, f):
            '''KPasswordDialog.KPasswordDialogFlags KPasswordDialog.KPasswordDialogFlags.__ixor__(KPasswordDialog.KPasswordDialogFlags f)'''
            return KPasswordDialog.KPasswordDialogFlags()
        def __ior__(self, f):
            '''KPasswordDialog.KPasswordDialogFlags KPasswordDialog.KPasswordDialogFlags.__ior__(KPasswordDialog.KPasswordDialogFlags f)'''
            return KPasswordDialog.KPasswordDialogFlags()
        def __iand__(self, mask):
            '''KPasswordDialog.KPasswordDialogFlags KPasswordDialog.KPasswordDialogFlags.__iand__(int mask)'''
            return KPasswordDialog.KPasswordDialogFlags()


class KPasteTextAction(KAction):
    """"""
    def __init__(self, parent):
        '''void KPasteTextAction.__init__(QObject parent)'''
    def __init__(self, text, parent):
        '''void KPasteTextAction.__init__(QString text, QObject parent)'''
    def __init__(self, icon, text, parent):
        '''void KPasteTextAction.__init__(KIcon icon, QString text, QObject parent)'''
    def setMixedMode(self, mode):
        '''void KPasteTextAction.setMixedMode(bool mode)'''


class KPixmapProvider():
    """"""
    def __init__(self):
        '''void KPixmapProvider.__init__()'''
    def __init__(self):
        '''KPixmapProvider KPixmapProvider.__init__()'''
        return KPixmapProvider()
    def pixmapFor(self, text, size = 0):
        '''abstract QPixmap KPixmapProvider.pixmapFor(QString text, int size = 0)'''
        return QPixmap()


class KPixmapRegionSelectorDialog(KDialog):
    """"""
    def __init__(self, parent = None):
        '''void KPixmapRegionSelectorDialog.__init__(QWidget parent = None)'''
    def adjustRegionSelectorWidgetSizeToFitScreen(self):
        '''void KPixmapRegionSelectorDialog.adjustRegionSelectorWidgetSizeToFitScreen()'''
    def getSelectedImage(self, pixmap, parent = None):
        '''static QImage KPixmapRegionSelectorDialog.getSelectedImage(QPixmap pixmap, QWidget parent = None)'''
        return QImage()
    def getSelectedImage(self, pixmap, aspectRatioWidth, aspectRatioHeight, parent = None):
        '''static QImage KPixmapRegionSelectorDialog.getSelectedImage(QPixmap pixmap, int aspectRatioWidth, int aspectRatioHeight, QWidget parent = None)'''
        return QImage()
    def getSelectedRegion(self, pixmap, parent = None):
        '''static QRect KPixmapRegionSelectorDialog.getSelectedRegion(QPixmap pixmap, QWidget parent = None)'''
        return QRect()
    def getSelectedRegion(self, pixmap, aspectRatioWidth, aspectRatioHeight, parent = None):
        '''static QRect KPixmapRegionSelectorDialog.getSelectedRegion(QPixmap pixmap, int aspectRatioWidth, int aspectRatioHeight, QWidget parent = None)'''
        return QRect()
    def pixmapRegionSelectorWidget(self):
        '''KPixmapRegionSelectorWidget KPixmapRegionSelectorDialog.pixmapRegionSelectorWidget()'''
        return KPixmapRegionSelectorWidget()


class KPixmapRegionSelectorWidget(QWidget):
    """"""
    # Enum KPixmapRegionSelectorWidget.RotateDirection
    Rotate90 = 0
    Rotate180 = 0
    Rotate270 = 0

    def __init__(self, parent = None):
        '''void KPixmapRegionSelectorWidget.__init__(QWidget parent = None)'''
    pixmapRotated = pyqtSignal() # void pixmapRotated() - signal
    def createPopupMenu(self):
        '''KMenu KPixmapRegionSelectorWidget.createPopupMenu()'''
        return KMenu()
    def rotateCounterclockwise(self):
        '''void KPixmapRegionSelectorWidget.rotateCounterclockwise()'''
    def rotateClockwise(self):
        '''void KPixmapRegionSelectorWidget.rotateClockwise()'''
    def rotate(self, direction):
        '''void KPixmapRegionSelectorWidget.rotate(KPixmapRegionSelectorWidget.RotateDirection direction)'''
    def setMaximumWidgetSize(self, width, height):
        '''void KPixmapRegionSelectorWidget.setMaximumWidgetSize(int width, int height)'''
    def setFreeSelectionAspectRatio(self):
        '''void KPixmapRegionSelectorWidget.setFreeSelectionAspectRatio()'''
    def setSelectionAspectRatio(self, width, height):
        '''void KPixmapRegionSelectorWidget.setSelectionAspectRatio(int width, int height)'''
    def selectedImage(self):
        '''QImage KPixmapRegionSelectorWidget.selectedImage()'''
        return QImage()
    def resetSelection(self):
        '''void KPixmapRegionSelectorWidget.resetSelection()'''
    def unzoomedSelectedRegion(self):
        '''QRect KPixmapRegionSelectorWidget.unzoomedSelectedRegion()'''
        return QRect()
    def selectedRegion(self):
        '''QRect KPixmapRegionSelectorWidget.selectedRegion()'''
        return QRect()
    def setSelectedRegion(self, rect):
        '''void KPixmapRegionSelectorWidget.setSelectedRegion(QRect rect)'''
    def pixmap(self):
        '''QPixmap KPixmapRegionSelectorWidget.pixmap()'''
        return QPixmap()
    def setPixmap(self, pixmap):
        '''void KPixmapRegionSelectorWidget.setPixmap(QPixmap pixmap)'''


class KPixmapSequence():
    """"""
    def __init__(self):
        '''void KPixmapSequence.__init__()'''
    def __init__(self, other):
        '''void KPixmapSequence.__init__(KPixmapSequence other)'''
    def __init__(self, pixmap, frameSize = QSize()):
        '''void KPixmapSequence.__init__(QPixmap pixmap, QSize frameSize = QSize())'''
    def __init__(self, iconName, size = None):
        '''void KPixmapSequence.__init__(QString iconName, int size = KIconLoader.SizeSmall)'''
    def frameAt(self, index):
        '''QPixmap KPixmapSequence.frameAt(int index)'''
        return QPixmap()
    def frameCount(self):
        '''int KPixmapSequence.frameCount()'''
        return int()
    def frameSize(self):
        '''QSize KPixmapSequence.frameSize()'''
        return QSize()
    def isEmpty(self):
        '''bool KPixmapSequence.isEmpty()'''
        return bool()
    def isValid(self):
        '''bool KPixmapSequence.isValid()'''
        return bool()


class KPixmapSequenceOverlayPainter(QObject):
    """"""
    def __init__(self, parent = None):
        '''void KPixmapSequenceOverlayPainter.__init__(QObject parent = None)'''
    def stop(self):
        '''void KPixmapSequenceOverlayPainter.stop()'''
    def start(self):
        '''void KPixmapSequenceOverlayPainter.start()'''
    def setOffset(self, offset):
        '''void KPixmapSequenceOverlayPainter.setOffset(QPoint offset)'''
    def setAlignment(self, align):
        '''void KPixmapSequenceOverlayPainter.setAlignment(Qt.Alignment align)'''
    def setRect(self, rect):
        '''void KPixmapSequenceOverlayPainter.setRect(QRect rect)'''
    def setWidget(self, w):
        '''void KPixmapSequenceOverlayPainter.setWidget(QWidget w)'''
    def setInterval(self, msecs):
        '''void KPixmapSequenceOverlayPainter.setInterval(int msecs)'''
    def setSequence(self, seq):
        '''void KPixmapSequenceOverlayPainter.setSequence(KPixmapSequence seq)'''
    def offset(self):
        '''QPoint KPixmapSequenceOverlayPainter.offset()'''
        return QPoint()
    def alignment(self):
        '''Qt.Alignment KPixmapSequenceOverlayPainter.alignment()'''
        return Qt.Alignment()
    def rect(self):
        '''QRect KPixmapSequenceOverlayPainter.rect()'''
        return QRect()
    def interval(self):
        '''int KPixmapSequenceOverlayPainter.interval()'''
        return int()
    def sequence(self):
        '''KPixmapSequence KPixmapSequenceOverlayPainter.sequence()'''
        return KPixmapSequence()


class KPixmapSequenceWidget(QWidget):
    """"""
    def __init__(self, parent = None):
        '''void KPixmapSequenceWidget.__init__(QWidget parent = None)'''
    def setInterval(self, msecs):
        '''void KPixmapSequenceWidget.setInterval(int msecs)'''
    def setSequence(self, seq):
        '''void KPixmapSequenceWidget.setSequence(KPixmapSequence seq)'''
    def sizeHint(self):
        '''QSize KPixmapSequenceWidget.sizeHint()'''
        return QSize()
    def interval(self):
        '''int KPixmapSequenceWidget.interval()'''
        return int()
    def sequence(self):
        '''KPixmapSequence KPixmapSequenceWidget.sequence()'''
        return KPixmapSequence()


class KPlotAxis():
    """"""
    def __init__(self, label = QString()):
        '''void KPlotAxis.__init__(QString label = QString())'''
    def minorTickMarks(self):
        '''list-of-float KPlotAxis.minorTickMarks()'''
        return [float()]
    def majorTickMarks(self):
        '''list-of-float KPlotAxis.majorTickMarks()'''
        return [float()]
    def setTickMarks(self, x0, length):
        '''void KPlotAxis.setTickMarks(float x0, float length)'''
    def tickLabelPrecision(self):
        '''int KPlotAxis.tickLabelPrecision()'''
        return int()
    def tickLabelFormat(self):
        '''str KPlotAxis.tickLabelFormat()'''
        return str()
    def tickLabelWidth(self):
        '''int KPlotAxis.tickLabelWidth()'''
        return int()
    def setTickLabelFormat(self, format = None, fieldWidth = 0, precision = None):
        '''void KPlotAxis.setTickLabelFormat(str format = 'g', int fieldWidth = 0, int precision = -1)'''
    def tickLabel(self, value):
        '''QString KPlotAxis.tickLabel(float value)'''
        return QString()
    def label(self):
        '''QString KPlotAxis.label()'''
        return QString()
    def setLabel(self, label):
        '''void KPlotAxis.setLabel(QString label)'''
    def setTickLabelsShown(self, b):
        '''void KPlotAxis.setTickLabelsShown(bool b)'''
    def areTickLabelsShown(self):
        '''bool KPlotAxis.areTickLabelsShown()'''
        return bool()
    def setVisible(self, visible):
        '''void KPlotAxis.setVisible(bool visible)'''
    def isVisible(self):
        '''bool KPlotAxis.isVisible()'''
        return bool()


class KPlotObject():
    """"""
    # Enum KPlotObject.PointStyle
    NoPoints = 0
    Circle = 0
    Letter = 0
    Triangle = 0
    Square = 0
    Pentagon = 0
    Hexagon = 0
    Asterisk = 0
    Star = 0
    UnknwonPoint = 0

    # Enum KPlotObject.PlotType
    UnknownType = 0
    Points = 0
    Lines = 0
    Bars = 0

    def __init__(self, color = None, otype = None, size = 2, ps = None):
        '''void KPlotObject.__init__(QColor color = Qt.white, KPlotObject.PlotType otype = KPlotObject.Points, float size = 2, KPlotObject.PointStyle ps = KPlotObject.Circle)'''
    def draw(self, p, pw):
        '''void KPlotObject.draw(QPainter p, KPlotWidget pw)'''
    def clearPoints(self):
        '''void KPlotObject.clearPoints()'''
    def removePoint(self, index):
        '''void KPlotObject.removePoint(int index)'''
    def addPoint(self, p, label = QString(), barWidth = 0):
        '''void KPlotObject.addPoint(QPointF p, QString label = QString(), float barWidth = 0)'''
    def addPoint(self, p):
        '''void KPlotObject.addPoint(KPlotPoint p)'''
    def addPoint(self, x, y, label = QString(), barWidth = 0):
        '''void KPlotObject.addPoint(float x, float y, QString label = QString(), float barWidth = 0)'''
    def points(self):
        '''list-of-KPlotPoint KPlotObject.points()'''
        return [KPlotPoint()]
    def setBarBrush(self, b):
        '''void KPlotObject.setBarBrush(QBrush b)'''
    def barBrush(self):
        '''QBrush KPlotObject.barBrush()'''
        return QBrush()
    def setBrush(self, b):
        '''void KPlotObject.setBrush(QBrush b)'''
    def brush(self):
        '''QBrush KPlotObject.brush()'''
        return QBrush()
    def setLabelPen(self, p):
        '''void KPlotObject.setLabelPen(QPen p)'''
    def labelPen(self):
        '''QPen KPlotObject.labelPen()'''
        return QPen()
    def setBarPen(self, p):
        '''void KPlotObject.setBarPen(QPen p)'''
    def barPen(self):
        '''QPen KPlotObject.barPen()'''
        return QPen()
    def setLinePen(self, p):
        '''void KPlotObject.setLinePen(QPen p)'''
    def linePen(self):
        '''QPen KPlotObject.linePen()'''
        return QPen()
    def setPen(self, p):
        '''void KPlotObject.setPen(QPen p)'''
    def pen(self):
        '''QPen KPlotObject.pen()'''
        return QPen()
    def setPointStyle(self, p):
        '''void KPlotObject.setPointStyle(KPlotObject.PointStyle p)'''
    def pointStyle(self):
        '''KPlotObject.PointStyle KPlotObject.pointStyle()'''
        return KPlotObject.PointStyle()
    def setSize(self, s):
        '''void KPlotObject.setSize(float s)'''
    def size(self):
        '''float KPlotObject.size()'''
        return float()
    def setShowBars(self, b):
        '''void KPlotObject.setShowBars(bool b)'''
    def setShowLines(self, b):
        '''void KPlotObject.setShowLines(bool b)'''
    def setShowPoints(self, b):
        '''void KPlotObject.setShowPoints(bool b)'''
    def plotTypes(self):
        '''KPlotObject.PlotTypes KPlotObject.plotTypes()'''
        return KPlotObject.PlotTypes()
    class PlotTypes():
        """"""
        def __init__(self):
            '''KPlotObject.PlotTypes KPlotObject.PlotTypes.__init__()'''
            return KPlotObject.PlotTypes()
        def __init__(self):
            '''int KPlotObject.PlotTypes.__init__()'''
            return int()
        def __init__(self):
            '''void KPlotObject.PlotTypes.__init__()'''
        def __bool__(self):
            '''int KPlotObject.PlotTypes.__bool__()'''
            return int()
        def __ne__(self, f):
            '''bool KPlotObject.PlotTypes.__ne__(KPlotObject.PlotTypes f)'''
            return bool()
        def __eq__(self, f):
            '''bool KPlotObject.PlotTypes.__eq__(KPlotObject.PlotTypes f)'''
            return bool()
        def __invert__(self):
            '''KPlotObject.PlotTypes KPlotObject.PlotTypes.__invert__()'''
            return KPlotObject.PlotTypes()
        def __and__(self, mask):
            '''KPlotObject.PlotTypes KPlotObject.PlotTypes.__and__(int mask)'''
            return KPlotObject.PlotTypes()
        def __xor__(self, f):
            '''KPlotObject.PlotTypes KPlotObject.PlotTypes.__xor__(KPlotObject.PlotTypes f)'''
            return KPlotObject.PlotTypes()
        def __xor__(self, f):
            '''KPlotObject.PlotTypes KPlotObject.PlotTypes.__xor__(int f)'''
            return KPlotObject.PlotTypes()
        def __or__(self, f):
            '''KPlotObject.PlotTypes KPlotObject.PlotTypes.__or__(KPlotObject.PlotTypes f)'''
            return KPlotObject.PlotTypes()
        def __or__(self, f):
            '''KPlotObject.PlotTypes KPlotObject.PlotTypes.__or__(int f)'''
            return KPlotObject.PlotTypes()
        def __int__(self):
            '''int KPlotObject.PlotTypes.__int__()'''
            return int()
        def __ixor__(self, f):
            '''KPlotObject.PlotTypes KPlotObject.PlotTypes.__ixor__(KPlotObject.PlotTypes f)'''
            return KPlotObject.PlotTypes()
        def __ior__(self, f):
            '''KPlotObject.PlotTypes KPlotObject.PlotTypes.__ior__(KPlotObject.PlotTypes f)'''
            return KPlotObject.PlotTypes()
        def __iand__(self, mask):
            '''KPlotObject.PlotTypes KPlotObject.PlotTypes.__iand__(int mask)'''
            return KPlotObject.PlotTypes()


class KPlotPoint():
    """"""
    def __init__(self):
        '''void KPlotPoint.__init__()'''
    def __init__(self, x, y, label = QString(), width = 0):
        '''void KPlotPoint.__init__(float x, float y, QString label = QString(), float width = 0)'''
    def __init__(self, p, label = QString(), width = 0):
        '''void KPlotPoint.__init__(QPointF p, QString label = QString(), float width = 0)'''
    def setBarWidth(self, w):
        '''void KPlotPoint.setBarWidth(float w)'''
    def barWidth(self):
        '''float KPlotPoint.barWidth()'''
        return float()
    def setLabel(self, label):
        '''void KPlotPoint.setLabel(QString label)'''
    def label(self):
        '''QString KPlotPoint.label()'''
        return QString()
    def setY(self, y):
        '''void KPlotPoint.setY(float y)'''
    def y(self):
        '''float KPlotPoint.y()'''
        return float()
    def setX(self, x):
        '''void KPlotPoint.setX(float x)'''
    def x(self):
        '''float KPlotPoint.x()'''
        return float()
    def setPosition(self, pos):
        '''void KPlotPoint.setPosition(QPointF pos)'''
    def position(self):
        '''QPointF KPlotPoint.position()'''
        return QPointF()


class KPlotWidget(QFrame):
    """"""
    # Enum KPlotWidget.Axis
    LeftAxis = 0
    BottomAxis = 0
    RightAxis = 0
    TopAxis = 0

    def __init__(self, parent = None):
        '''void KPlotWidget.__init__(QWidget parent = None)'''
    def pointsUnderPoint(self, p):
        '''list-of-KPlotPoint KPlotWidget.pointsUnderPoint(QPoint p)'''
        return [KPlotPoint()]
    def setPixRect(self):
        '''void KPlotWidget.setPixRect()'''
    def drawAxes(self, p):
        '''void KPlotWidget.drawAxes(QPainter p)'''
    def resizeEvent(self):
        '''QResizeEvent KPlotWidget.resizeEvent()'''
        return QResizeEvent()
    def paintEvent(self):
        '''QPaintEvent KPlotWidget.paintEvent()'''
        return QPaintEvent()
    def event(self):
        '''QEvent KPlotWidget.event()'''
        return QEvent()
    def setObjectToolTipShown(self, show):
        '''void KPlotWidget.setObjectToolTipShown(bool show)'''
    def setShowGrid(self, show):
        '''void KPlotWidget.setShowGrid(bool show)'''
    def axis(self, type):
        '''KPlotAxis KPlotWidget.axis(KPlotWidget.Axis type)'''
        return KPlotAxis()
    def placeLabel(self, painter, pp):
        '''void KPlotWidget.placeLabel(QPainter painter, KPlotPoint pp)'''
    def maskAlongLine(self, p1, p2, value = 1):
        '''void KPlotWidget.maskAlongLine(QPointF p1, QPointF p2, float value = 1)'''
    def maskRect(self, r, value = 1):
        '''void KPlotWidget.maskRect(QRectF r, float value = 1)'''
    def mapToWidget(self, p):
        '''QPointF KPlotWidget.mapToWidget(QPointF p)'''
        return QPointF()
    def setDefaultPaddings(self):
        '''void KPlotWidget.setDefaultPaddings()'''
    def setBottomPadding(self, padding):
        '''void KPlotWidget.setBottomPadding(int padding)'''
    def setTopPadding(self, padding):
        '''void KPlotWidget.setTopPadding(int padding)'''
    def setRightPadding(self, padding):
        '''void KPlotWidget.setRightPadding(int padding)'''
    def setLeftPadding(self, padding):
        '''void KPlotWidget.setLeftPadding(int padding)'''
    def bottomPadding(self):
        '''int KPlotWidget.bottomPadding()'''
        return int()
    def topPadding(self):
        '''int KPlotWidget.topPadding()'''
        return int()
    def rightPadding(self):
        '''int KPlotWidget.rightPadding()'''
        return int()
    def leftPadding(self):
        '''int KPlotWidget.leftPadding()'''
        return int()
    def setAntialiasing(self, b):
        '''void KPlotWidget.setAntialiasing(bool b)'''
    def antialiasing(self):
        '''bool KPlotWidget.antialiasing()'''
        return bool()
    def isObjectToolTipShown(self):
        '''bool KPlotWidget.isObjectToolTipShown()'''
        return bool()
    def isGridShown(self):
        '''bool KPlotWidget.isGridShown()'''
        return bool()
    def setGridColor(self, gc):
        '''void KPlotWidget.setGridColor(QColor gc)'''
    def setForegroundColor(self, fg):
        '''void KPlotWidget.setForegroundColor(QColor fg)'''
    def setBackgroundColor(self, bg):
        '''void KPlotWidget.setBackgroundColor(QColor bg)'''
    def gridColor(self):
        '''QColor KPlotWidget.gridColor()'''
        return QColor()
    def foregroundColor(self):
        '''QColor KPlotWidget.foregroundColor()'''
        return QColor()
    def backgroundColor(self):
        '''QColor KPlotWidget.backgroundColor()'''
        return QColor()
    def replacePlotObject(self, i, o):
        '''void KPlotWidget.replacePlotObject(int i, KPlotObject o)'''
    def resetPlot(self):
        '''void KPlotWidget.resetPlot()'''
    def resetPlotMask(self):
        '''void KPlotWidget.resetPlotMask()'''
    def removeAllPlotObjects(self):
        '''void KPlotWidget.removeAllPlotObjects()'''
    def plotObjects(self):
        '''list-of-KPlotObject KPlotWidget.plotObjects()'''
        return [KPlotObject()]
    def addPlotObjects(self, objects):
        '''void KPlotWidget.addPlotObjects(list-of-KPlotObject objects)'''
    def addPlotObject(self, object):
        '''void KPlotWidget.addPlotObject(KPlotObject object)'''
    def pixRect(self):
        '''QRect KPlotWidget.pixRect()'''
        return QRect()
    def secondaryDataRect(self):
        '''QRectF KPlotWidget.secondaryDataRect()'''
        return QRectF()
    def dataRect(self):
        '''QRectF KPlotWidget.dataRect()'''
        return QRectF()
    def clearSecondaryLimits(self):
        '''void KPlotWidget.clearSecondaryLimits()'''
    def setSecondaryLimits(self, x1, x2, y1, y2):
        '''void KPlotWidget.setSecondaryLimits(float x1, float x2, float y1, float y2)'''
    def setLimits(self, x1, x2, y1, y2):
        '''void KPlotWidget.setLimits(float x1, float x2, float y1, float y2)'''
    def sizeHint(self):
        '''QSize KPlotWidget.sizeHint()'''
        return QSize()
    def minimumSizeHint(self):
        '''QSize KPlotWidget.minimumSizeHint()'''
        return QSize()


class KProgressDialog(KDialog):
    """"""
    def __init__(self, parent = None, caption = QString(), text = QString(), flags = 0):
        '''void KProgressDialog.__init__(QWidget parent = None, QString caption = QString(), QString text = QString(), Qt.WindowFlags flags = 0)'''
    def showEvent(self, event):
        '''void KProgressDialog.showEvent(QShowEvent event)'''
    def reject(self):
        '''void KProgressDialog.reject()'''
    def minimumDuration(self):
        '''int KProgressDialog.minimumDuration()'''
        return int()
    def setMinimumDuration(self, ms):
        '''void KProgressDialog.setMinimumDuration(int ms)'''
    def buttonText(self):
        '''QString KProgressDialog.buttonText()'''
        return QString()
    def setButtonText(self, text):
        '''void KProgressDialog.setButtonText(QString text)'''
    def ignoreCancel(self):
        '''void KProgressDialog.ignoreCancel()'''
    def wasCancelled(self):
        '''bool KProgressDialog.wasCancelled()'''
        return bool()
    def autoReset(self):
        '''bool KProgressDialog.autoReset()'''
        return bool()
    def setAutoReset(self, autoReset):
        '''void KProgressDialog.setAutoReset(bool autoReset)'''
    def autoClose(self):
        '''bool KProgressDialog.autoClose()'''
        return bool()
    def setAutoClose(self, close):
        '''void KProgressDialog.setAutoClose(bool close)'''
    def showCancelButton(self, show):
        '''void KProgressDialog.showCancelButton(bool show)'''
    def allowCancel(self):
        '''bool KProgressDialog.allowCancel()'''
        return bool()
    def setAllowCancel(self, allowCancel):
        '''void KProgressDialog.setAllowCancel(bool allowCancel)'''
    def labelText(self):
        '''QString KProgressDialog.labelText()'''
        return QString()
    def setLabelText(self, text):
        '''void KProgressDialog.setLabelText(QString text)'''
    def progressBar(self):
        '''QProgressBar KProgressDialog.progressBar()'''
        return QProgressBar()


class KPushButton(QPushButton):
    """"""
    def __init__(self, parent = None):
        '''void KPushButton.__init__(QWidget parent = None)'''
    def __init__(self, text, parent = None):
        '''void KPushButton.__init__(QString text, QWidget parent = None)'''
    def __init__(self, icon, text, parent = None):
        '''void KPushButton.__init__(KIcon icon, QString text, QWidget parent = None)'''
    def __init__(self, item, parent = None):
        '''void KPushButton.__init__(KGuiItem item, QWidget parent = None)'''
    authorized = pyqtSignal() # void authorized(KAuth::Action *) - signal
    def paintEvent(self):
        '''QPaintEvent KPushButton.paintEvent()'''
        return QPaintEvent()
    def setAuthAction(self, action):
        '''void KPushButton.setAuthAction(KAuth.Action action)'''
    def setAuthAction(self, actionName):
        '''void KPushButton.setAuthAction(QString actionName)'''
    def authAction(self):
        '''KAuth.Action KPushButton.authAction()'''
        return KAuth.Action()
    def sizeHint(self):
        '''QSize KPushButton.sizeHint()'''
        return QSize()
    def startDrag(self):
        '''void KPushButton.startDrag()'''
    def mouseMoveEvent(self):
        '''QMouseEvent KPushButton.mouseMoveEvent()'''
        return QMouseEvent()
    def mousePressEvent(self):
        '''QMouseEvent KPushButton.mousePressEvent()'''
        return QMouseEvent()
    def dragObject(self):
        '''QDrag KPushButton.dragObject()'''
        return QDrag()
    def delayedMenu(self):
        '''QMenu KPushButton.delayedMenu()'''
        return QMenu()
    def setDelayedMenu(self, delayed_menu):
        '''void KPushButton.setDelayedMenu(QMenu delayed_menu)'''
    def setText(self, text):
        '''void KPushButton.setText(QString text)'''
    def setIcon(self, icon):
        '''void KPushButton.setIcon(KIcon icon)'''
    def setIcon(self, pix):
        '''void KPushButton.setIcon(QIcon pix)'''
    def guiItem(self):
        '''KStandardGuiItem.StandardItem KPushButton.guiItem()'''
        return KStandardGuiItem.StandardItem()
    def setGuiItem(self, item):
        '''void KPushButton.setGuiItem(KGuiItem item)'''
    def setGuiItem(self, item):
        '''void KPushButton.setGuiItem(KStandardGuiItem.StandardItem item)'''
    def isDragEnabled(self):
        '''bool KPushButton.isDragEnabled()'''
        return bool()
    def setDragEnabled(self, enable):
        '''void KPushButton.setDragEnabled(bool enable)'''


class KRecentFilesAction(KSelectAction):
    """"""
    def __init__(self, parent):
        '''void KRecentFilesAction.__init__(QObject parent)'''
    def __init__(self, text, parent):
        '''void KRecentFilesAction.__init__(QString text, QObject parent)'''
    def __init__(self, icon, text, parent):
        '''void KRecentFilesAction.__init__(KIcon icon, QString text, QObject parent)'''
    recentListCleared = pyqtSignal() # void recentListCleared() - signal
    urlSelected = pyqtSignal() # void urlSelected(const KUrlamp;) - signal
    def urls(self):
        '''KUrl.List KRecentFilesAction.urls()'''
        return KUrl.List()
    def removeUrl(self, url):
        '''void KRecentFilesAction.removeUrl(KUrl url)'''
    def addUrl(self, url, name = QString()):
        '''void KRecentFilesAction.addUrl(KUrl url, QString name = QString())'''
    def saveEntries(self, config):
        '''void KRecentFilesAction.saveEntries(KConfigGroup config)'''
    def loadEntries(self, config):
        '''void KRecentFilesAction.loadEntries(KConfigGroup config)'''
    def setMaxItems(self, maxItems):
        '''void KRecentFilesAction.setMaxItems(int maxItems)'''
    def maxItems(self):
        '''int KRecentFilesAction.maxItems()'''
        return int()
    def clear(self):
        '''void KRecentFilesAction.clear()'''
    def removeAction(self, action):
        '''QAction KRecentFilesAction.removeAction(QAction action)'''
        return QAction()
    def addAction(self, action, url, name):
        '''void KRecentFilesAction.addAction(QAction action, KUrl url, QString name)'''


class KRecursiveFilterProxyModel(QSortFilterProxyModel):
    """"""
    def __init__(self, parent = None):
        '''void KRecursiveFilterProxyModel.__init__(QObject parent = None)'''
    def match(self, start, role, value, hits = 1, flags = None):
        '''list-of-QModelIndex KRecursiveFilterProxyModel.match(QModelIndex start, int role, QVariant value, int hits = 1, Qt.MatchFlags flags = Qt.MatchFlags(Qt.MatchStartsWith|Qt.MatchWrap))'''
        return [QModelIndex()]
    def acceptRow(self, sourceRow, sourceParent):
        '''bool KRecursiveFilterProxyModel.acceptRow(int sourceRow, QModelIndex sourceParent)'''
        return bool()
    def setSourceModel(self, model):
        '''void KRecursiveFilterProxyModel.setSourceModel(QAbstractItemModel model)'''


class KReplace(KFind):
    """"""
    def __init__(self, pattern, replacement, options, parent = None):
        '''void KReplace.__init__(QString pattern, QString replacement, int options, QWidget parent = None)'''
    def __init__(self, pattern, replacement, options, parent, replaceDialog):
        '''void KReplace.__init__(QString pattern, QString replacement, int options, QWidget parent, QWidget replaceDialog)'''
    def displayFinalDialog(self):
        '''void KReplace.displayFinalDialog()'''
    def shouldRestart(self, forceAsking = False, showNumMatches = True):
        '''bool KReplace.shouldRestart(bool forceAsking = False, bool showNumMatches = True)'''
        return bool()
    def closeReplaceNextDialog(self):
        '''void KReplace.closeReplaceNextDialog()'''
    def replaceNextDialog(self, create = False):
        '''KDialog KReplace.replaceNextDialog(bool create = False)'''
        return KDialog()
    def replace(self):
        '''KFind.Result KReplace.replace()'''
        return KFind.Result()
    def replace(self, text, pattern, replacement, index, options, replacedLength):
        '''static int KReplace.replace(QString text, QString pattern, QString replacement, int index, int options, int replacedLength)'''
        return int()
    def replace(self, text, pattern, replacement, index, options, replacedLength):
        '''static int KReplace.replace(QString text, QRegExp pattern, QString replacement, int index, int options, int replacedLength)'''
        return int()
    replace = pyqtSignal() # void replace(const QStringamp;,int,int,int) - signal
    def resetCounts(self):
        '''void KReplace.resetCounts()'''
    def numReplacements(self):
        '''int KReplace.numReplacements()'''
        return int()


class KReplaceDialog(KFindDialog):
    """"""
    # Enum KReplaceDialog.Options
    PromptOnReplace = 0
    BackReference = 0

    def __init__(self, parent = None, options = 0, findStrings = QStringList(), replaceStrings = QStringList(), hasSelection = True):
        '''void KReplaceDialog.__init__(QWidget parent = None, int options = 0, QStringList findStrings = QStringList(), QStringList replaceStrings = QStringList(), bool hasSelection = True)'''
    def showEvent(self):
        '''QShowEvent KReplaceDialog.showEvent()'''
        return QShowEvent()
    def replaceExtension(self):
        '''QWidget KReplaceDialog.replaceExtension()'''
        return QWidget()
    def replacement(self):
        '''QString KReplaceDialog.replacement()'''
        return QString()
    def options(self):
        '''int KReplaceDialog.options()'''
        return int()
    def setOptions(self, options):
        '''void KReplaceDialog.setOptions(int options)'''
    def replacementHistory(self):
        '''QStringList KReplaceDialog.replacementHistory()'''
        return QStringList()
    def setReplacementHistory(self, history):
        '''void KReplaceDialog.setReplacementHistory(QStringList history)'''


class KRestrictedLine(KLineEdit):
    """"""
    def __init__(self, parent = None):
        '''void KRestrictedLine.__init__(QWidget parent = None)'''
    def inputMethodEvent(self, e):
        '''void KRestrictedLine.inputMethodEvent(QInputMethodEvent e)'''
    def keyPressEvent(self, e):
        '''void KRestrictedLine.keyPressEvent(QKeyEvent e)'''
    invalidChar = pyqtSignal() # void invalidChar(int) - signal
    def validChars(self):
        '''QString KRestrictedLine.validChars()'''
        return QString()
    def setValidChars(self, valid):
        '''void KRestrictedLine.setValidChars(QString valid)'''


class KTextEdit(QTextEdit):
    """"""
    def __init__(self, text, parent = None):
        '''void KTextEdit.__init__(QString text, QWidget parent = None)'''
    def __init__(self, parent = None):
        '''void KTextEdit.__init__(QWidget parent = None)'''
    aboutToShowContextMenu = pyqtSignal() # void aboutToShowContextMenu(QMenu *) - signal
    def focusOutEvent(self):
        '''QFocusEvent KTextEdit.focusOutEvent()'''
        return QFocusEvent()
    def paintEvent(self):
        '''QPaintEvent KTextEdit.paintEvent()'''
        return QPaintEvent()
    def clickMessage(self):
        '''QString KTextEdit.clickMessage()'''
        return QString()
    def setClickMessage(self, msg):
        '''void KTextEdit.setClickMessage(QString msg)'''
    def checkSpellingEnabledInternal(self):
        '''bool KTextEdit.checkSpellingEnabledInternal()'''
        return bool()
    def setCheckSpellingEnabledInternal(self, check):
        '''void KTextEdit.setCheckSpellingEnabledInternal(bool check)'''
    def contextMenuEvent(self):
        '''QContextMenuEvent KTextEdit.contextMenuEvent()'''
        return QContextMenuEvent()
    def deleteWordForward(self):
        '''void KTextEdit.deleteWordForward()'''
    def deleteWordBack(self):
        '''void KTextEdit.deleteWordBack()'''
    def wheelEvent(self):
        '''QWheelEvent KTextEdit.wheelEvent()'''
        return QWheelEvent()
    def focusInEvent(self):
        '''QFocusEvent KTextEdit.focusInEvent()'''
        return QFocusEvent()
    def keyPressEvent(self):
        '''QKeyEvent KTextEdit.keyPressEvent()'''
        return QKeyEvent()
    def event(self):
        '''QEvent KTextEdit.event()'''
        return QEvent()
    def slotSpeakText(self):
        '''void KTextEdit.slotSpeakText()'''
    def slotReplace(self):
        '''void KTextEdit.slotReplace()'''
    def slotFindNext(self):
        '''void KTextEdit.slotFindNext()'''
    def slotFind(self):
        '''void KTextEdit.slotFind()'''
    def slotDoFind(self):
        '''void KTextEdit.slotDoFind()'''
    def slotReplaceNext(self):
        '''void KTextEdit.slotReplaceNext()'''
    def slotDoReplace(self):
        '''void KTextEdit.slotDoReplace()'''
    def replace(self):
        '''void KTextEdit.replace()'''
    def showSpellConfigDialog(self, configFileName, windowIcon = QString()):
        '''void KTextEdit.showSpellConfigDialog(QString configFileName, QString windowIcon = QString())'''
    def checkSpelling(self):
        '''void KTextEdit.checkSpelling()'''
    def setSpellCheckingLanguage(self, language):
        '''void KTextEdit.setSpellCheckingLanguage(QString language)'''
    languageChanged = pyqtSignal() # void languageChanged(const QStringamp;) - signal
    spellCheckStatus = pyqtSignal() # void spellCheckStatus(const QStringamp;) - signal
    checkSpellingChanged = pyqtSignal() # void checkSpellingChanged(bool) - signal
    def spellCheckingLanguage(self):
        '''QString KTextEdit.spellCheckingLanguage()'''
        return QString()
    def setSpellInterface(self, spellInterface):
        '''void KTextEdit.setSpellInterface(KTextEditSpellInterface spellInterface)'''
    def enableFindReplace(self, enabled):
        '''void KTextEdit.enableFindReplace(bool enabled)'''
    def mousePopupMenu(self):
        '''QMenu KTextEdit.mousePopupMenu()'''
        return QMenu()
    def setHighlighter(self, _highLighter):
        '''void KTextEdit.setHighlighter(Sonnet.Highlighter _highLighter)'''
    def highlighter(self):
        '''Sonnet.Highlighter KTextEdit.highlighter()'''
        return Sonnet.Highlighter()
    def createHighlighter(self):
        '''void KTextEdit.createHighlighter()'''
    def setSpellCheckingConfigFileName(self, fileName):
        '''void KTextEdit.setSpellCheckingConfigFileName(QString fileName)'''
    def highlightWord(self, length, pos):
        '''void KTextEdit.highlightWord(int length, int pos)'''
    def checkSpellingEnabled(self):
        '''bool KTextEdit.checkSpellingEnabled()'''
        return bool()
    def setCheckSpellingEnabled(self, check):
        '''void KTextEdit.setCheckSpellingEnabled(bool check)'''
    def setReadOnly(self, readOnly):
        '''void KTextEdit.setReadOnly(bool readOnly)'''


class KRichTextEdit(KTextEdit):
    """"""
    # Enum KRichTextEdit.Mode
    Plain = 0
    Rich = 0

    def __init__(self, text, parent = None):
        '''void KRichTextEdit.__init__(QString text, QWidget parent = None)'''
    def __init__(self, parent = None):
        '''void KRichTextEdit.__init__(QWidget parent = None)'''
    def makeLeftToRight(self):
        '''void KRichTextEdit.makeLeftToRight()'''
    def makeRightToLeft(self):
        '''void KRichTextEdit.makeRightToLeft()'''
    def keyPressEvent(self, event):
        '''void KRichTextEdit.keyPressEvent(QKeyEvent event)'''
    selectionFinished = pyqtSignal() # void selectionFinished() - signal
    textModeChanged = pyqtSignal() # void textModeChanged(KRichTextEdit::Mode) - signal
    def setTextSubScript(self, subscript):
        '''void KRichTextEdit.setTextSubScript(bool subscript)'''
    def setTextSuperScript(self, superscript):
        '''void KRichTextEdit.setTextSuperScript(bool superscript)'''
    def toCleanHtml(self):
        '''QString KRichTextEdit.toCleanHtml()'''
        return QString()
    def switchToPlainText(self):
        '''void KRichTextEdit.switchToPlainText()'''
    def insertHorizontalRule(self):
        '''void KRichTextEdit.insertHorizontalRule()'''
    def setTextBackgroundColor(self, color):
        '''void KRichTextEdit.setTextBackgroundColor(QColor color)'''
    def setTextForegroundColor(self, color):
        '''void KRichTextEdit.setTextForegroundColor(QColor color)'''
    def setTextStrikeOut(self, strikeOut):
        '''void KRichTextEdit.setTextStrikeOut(bool strikeOut)'''
    def setTextUnderline(self, underline):
        '''void KRichTextEdit.setTextUnderline(bool underline)'''
    def setTextItalic(self, italic):
        '''void KRichTextEdit.setTextItalic(bool italic)'''
    def setTextBold(self, bold):
        '''void KRichTextEdit.setTextBold(bool bold)'''
    def setFont(self, font):
        '''void KRichTextEdit.setFont(QFont font)'''
    def setFontSize(self, size):
        '''void KRichTextEdit.setFontSize(int size)'''
    def setFontFamily(self, fontFamily):
        '''void KRichTextEdit.setFontFamily(QString fontFamily)'''
    def indentListLess(self):
        '''void KRichTextEdit.indentListLess()'''
    def indentListMore(self):
        '''void KRichTextEdit.indentListMore()'''
    def setListStyle(self, _styleIndex):
        '''void KRichTextEdit.setListStyle(int _styleIndex)'''
    def alignJustify(self):
        '''void KRichTextEdit.alignJustify()'''
    def alignRight(self):
        '''void KRichTextEdit.alignRight()'''
    def alignCenter(self):
        '''void KRichTextEdit.alignCenter()'''
    def alignLeft(self):
        '''void KRichTextEdit.alignLeft()'''
    def canDedentList(self):
        '''bool KRichTextEdit.canDedentList()'''
        return bool()
    def canIndentList(self):
        '''bool KRichTextEdit.canIndentList()'''
        return bool()
    def updateLink(self, linkUrl, linkText):
        '''void KRichTextEdit.updateLink(QString linkUrl, QString linkText)'''
    def selectLinkText(self, cursor):
        '''void KRichTextEdit.selectLinkText(QTextCursor cursor)'''
    def selectLinkText(self):
        '''void KRichTextEdit.selectLinkText()'''
    def currentLinkUrl(self):
        '''QString KRichTextEdit.currentLinkUrl()'''
        return QString()
    def currentLinkText(self):
        '''QString KRichTextEdit.currentLinkText()'''
        return QString()
    def setTextOrHtml(self, text):
        '''void KRichTextEdit.setTextOrHtml(QString text)'''
    def textOrHtml(self):
        '''QString KRichTextEdit.textOrHtml()'''
        return QString()
    def textMode(self):
        '''KRichTextEdit.Mode KRichTextEdit.textMode()'''
        return KRichTextEdit.Mode()
    def enableRichTextMode(self):
        '''void KRichTextEdit.enableRichTextMode()'''


class KRichTextWidget(KRichTextEdit):
    """"""
    # Enum KRichTextWidget.RichTextSupportValues
    DisableRichText = 0
    SupportBold = 0
    SupportItalic = 0
    SupportUnderline = 0
    SupportStrikeOut = 0
    SupportFontFamily = 0
    SupportFontSize = 0
    SupportTextForegroundColor = 0
    SupportTextBackgroundColor = 0
    FullTextFormattingSupport = 0
    SupportChangeListStyle = 0
    SupportIndentLists = 0
    SupportDedentLists = 0
    FullListSupport = 0
    SupportAlignment = 0
    SupportRuleLine = 0
    SupportHyperlinks = 0
    SupportFormatPainting = 0
    SupportToPlainText = 0
    SupportSuperScriptAndSubScript = 0
    SupportDirection = 0
    FullSupport = 0

    def __init__(self, parent):
        '''void KRichTextWidget.__init__(QWidget parent)'''
    def __init__(self, text, parent = None):
        '''void KRichTextWidget.__init__(QString text, QWidget parent = None)'''
    def mouseReleaseEvent(self, event):
        '''void KRichTextWidget.mouseReleaseEvent(QMouseEvent event)'''
    def setActionsEnabled(self, enabled):
        '''void KRichTextWidget.setActionsEnabled(bool enabled)'''
    def updateActionStates(self):
        '''void KRichTextWidget.updateActionStates()'''
    def richTextSupport(self):
        '''KRichTextWidget.RichTextSupport KRichTextWidget.richTextSupport()'''
        return KRichTextWidget.RichTextSupport()
    def setRichTextSupport(self, support):
        '''void KRichTextWidget.setRichTextSupport(KRichTextWidget.RichTextSupport support)'''
    def createActions(self, actionCollection):
        '''void KRichTextWidget.createActions(KActionCollection actionCollection)'''
    class RichTextSupport():
        """"""
        def __init__(self):
            '''KRichTextWidget.RichTextSupport KRichTextWidget.RichTextSupport.__init__()'''
            return KRichTextWidget.RichTextSupport()
        def __init__(self):
            '''int KRichTextWidget.RichTextSupport.__init__()'''
            return int()
        def __init__(self):
            '''void KRichTextWidget.RichTextSupport.__init__()'''
        def __bool__(self):
            '''int KRichTextWidget.RichTextSupport.__bool__()'''
            return int()
        def __ne__(self, f):
            '''bool KRichTextWidget.RichTextSupport.__ne__(KRichTextWidget.RichTextSupport f)'''
            return bool()
        def __eq__(self, f):
            '''bool KRichTextWidget.RichTextSupport.__eq__(KRichTextWidget.RichTextSupport f)'''
            return bool()
        def __invert__(self):
            '''KRichTextWidget.RichTextSupport KRichTextWidget.RichTextSupport.__invert__()'''
            return KRichTextWidget.RichTextSupport()
        def __and__(self, mask):
            '''KRichTextWidget.RichTextSupport KRichTextWidget.RichTextSupport.__and__(int mask)'''
            return KRichTextWidget.RichTextSupport()
        def __xor__(self, f):
            '''KRichTextWidget.RichTextSupport KRichTextWidget.RichTextSupport.__xor__(KRichTextWidget.RichTextSupport f)'''
            return KRichTextWidget.RichTextSupport()
        def __xor__(self, f):
            '''KRichTextWidget.RichTextSupport KRichTextWidget.RichTextSupport.__xor__(int f)'''
            return KRichTextWidget.RichTextSupport()
        def __or__(self, f):
            '''KRichTextWidget.RichTextSupport KRichTextWidget.RichTextSupport.__or__(KRichTextWidget.RichTextSupport f)'''
            return KRichTextWidget.RichTextSupport()
        def __or__(self, f):
            '''KRichTextWidget.RichTextSupport KRichTextWidget.RichTextSupport.__or__(int f)'''
            return KRichTextWidget.RichTextSupport()
        def __int__(self):
            '''int KRichTextWidget.RichTextSupport.__int__()'''
            return int()
        def __ixor__(self, f):
            '''KRichTextWidget.RichTextSupport KRichTextWidget.RichTextSupport.__ixor__(KRichTextWidget.RichTextSupport f)'''
            return KRichTextWidget.RichTextSupport()
        def __ior__(self, f):
            '''KRichTextWidget.RichTextSupport KRichTextWidget.RichTextSupport.__ior__(KRichTextWidget.RichTextSupport f)'''
            return KRichTextWidget.RichTextSupport()
        def __iand__(self, mask):
            '''KRichTextWidget.RichTextSupport KRichTextWidget.RichTextSupport.__iand__(int mask)'''
            return KRichTextWidget.RichTextSupport()


class KRuler(QAbstractSlider):
    """"""
    # Enum KRuler.MetricStyle
    Custom = 0
    Pixel = 0
    Inch = 0
    Millimetres = 0
    Centimetres = 0
    Metres = 0

    def __init__(self, parent = None):
        '''void KRuler.__init__(QWidget parent = None)'''
    def __init__(self, orient, parent = None, f = 0):
        '''void KRuler.__init__(Qt.Orientation orient, QWidget parent = None, Qt.WindowFlags f = 0)'''
    def __init__(self, orient, widgetWidth, parent = None, f = 0):
        '''void KRuler.__init__(Qt.Orientation orient, int widgetWidth, QWidget parent = None, Qt.WindowFlags f = 0)'''
    def paintEvent(self):
        '''QPaintEvent KRuler.paintEvent()'''
        return QPaintEvent()
    def slotEndOffset(self):
        '''int KRuler.slotEndOffset()'''
        return int()
    def slotNewOffset(self):
        '''int KRuler.slotNewOffset()'''
        return int()
    def slotNewValue(self):
        '''int KRuler.slotNewValue()'''
        return int()
    def endOffset(self):
        '''int KRuler.endOffset()'''
        return int()
    def offset(self):
        '''int KRuler.offset()'''
        return int()
    def setOffset(self, offset):
        '''void KRuler.setOffset(int offset)'''
    def slideDown(self, count = 1):
        '''void KRuler.slideDown(int count = 1)'''
    def slideUp(self, count = 1):
        '''void KRuler.slideUp(int count = 1)'''
    def lengthFixed(self):
        '''bool KRuler.lengthFixed()'''
        return bool()
    def setLengthFixed(self, fix):
        '''void KRuler.setLengthFixed(bool fix)'''
    def length(self):
        '''int KRuler.length()'''
        return int()
    def setLength(self):
        '''int KRuler.setLength()'''
        return int()
    def pixelPerMark(self):
        '''float KRuler.pixelPerMark()'''
        return float()
    def setPixelPerMark(self, rate):
        '''void KRuler.setPixelPerMark(float rate)'''
    def setRulerMetricStyle(self):
        '''KRuler.MetricStyle KRuler.setRulerMetricStyle()'''
        return KRuler.MetricStyle()
    def endLabel(self):
        '''QString KRuler.endLabel()'''
        return QString()
    def setEndLabel(self):
        '''QString KRuler.setEndLabel()'''
        return QString()
    def showEndLabel(self):
        '''bool KRuler.showEndLabel()'''
        return bool()
    def setShowEndLabel(self):
        '''bool KRuler.setShowEndLabel()'''
        return bool()
    def setFrameStyle(self):
        '''int KRuler.setFrameStyle()'''
        return int()
    def showPointer(self):
        '''bool KRuler.showPointer()'''
        return bool()
    def setShowPointer(self):
        '''bool KRuler.setShowPointer()'''
        return bool()
    def showEndMarks(self):
        '''bool KRuler.showEndMarks()'''
        return bool()
    def setShowEndMarks(self):
        '''bool KRuler.setShowEndMarks()'''
        return bool()
    def showBigMarks(self):
        '''bool KRuler.showBigMarks()'''
        return bool()
    def setShowBigMarks(self):
        '''bool KRuler.setShowBigMarks()'''
        return bool()
    def showMediumMarks(self):
        '''bool KRuler.showMediumMarks()'''
        return bool()
    def setShowMediumMarks(self):
        '''bool KRuler.setShowMediumMarks()'''
        return bool()
    def showLittleMarks(self):
        '''bool KRuler.showLittleMarks()'''
        return bool()
    def setShowLittleMarks(self):
        '''bool KRuler.setShowLittleMarks()'''
        return bool()
    def showTinyMarks(self):
        '''bool KRuler.showTinyMarks()'''
        return bool()
    def setShowTinyMarks(self):
        '''bool KRuler.setShowTinyMarks()'''
        return bool()
    def bigMarkDistance(self):
        '''int KRuler.bigMarkDistance()'''
        return int()
    def setBigMarkDistance(self):
        '''int KRuler.setBigMarkDistance()'''
        return int()
    def mediumMarkDistance(self):
        '''int KRuler.mediumMarkDistance()'''
        return int()
    def setMediumMarkDistance(self):
        '''int KRuler.setMediumMarkDistance()'''
        return int()
    def littleMarkDistance(self):
        '''int KRuler.littleMarkDistance()'''
        return int()
    def setLittleMarkDistance(self):
        '''int KRuler.setLittleMarkDistance()'''
        return int()
    def tinyMarkDistance(self):
        '''int KRuler.tinyMarkDistance()'''
        return int()
    def setTinyMarkDistance(self):
        '''int KRuler.setTinyMarkDistance()'''
        return int()
    def maxValue(self):
        '''int KRuler.maxValue()'''
        return int()
    def setMaxValue(self):
        '''int KRuler.setMaxValue()'''
        return int()
    def minValue(self):
        '''int KRuler.minValue()'''
        return int()
    def setMinValue(self):
        '''int KRuler.setMinValue()'''
        return int()


class KSelectionProxyModel(QAbstractProxyModel):
    """"""
    # Enum KSelectionProxyModel.FilterBehavior
    SubTrees = 0
    SubTreeRoots = 0
    SubTreesWithoutRoots = 0
    ExactSelection = 0
    ChildrenOfExactSelection = 0

    def __init__(self, selectionModel, parent = None):
        '''void KSelectionProxyModel.__init__(QItemSelectionModel selectionModel, QObject parent = None)'''
    def mapSelectionToSource(self, selection):
        '''QItemSelection KSelectionProxyModel.mapSelectionToSource(QItemSelection selection)'''
        return QItemSelection()
    def mapSelectionFromSource(self, selection):
        '''QItemSelection KSelectionProxyModel.mapSelectionFromSource(QItemSelection selection)'''
        return QItemSelection()
    def match(self, start, role, value, hits = 1, flags = None):
        '''list-of-QModelIndex KSelectionProxyModel.match(QModelIndex start, int role, QVariant value, int hits = 1, Qt.MatchFlags flags = Qt.MatchFlags(Qt.MatchStartsWith|Qt.MatchWrap))'''
        return [QModelIndex()]
    def sourceRootIndexes(self):
        '''list-of-QPersistentModelIndex KSelectionProxyModel.sourceRootIndexes()'''
        return [QPersistentModelIndex()]
    def columnCount(self):
        '''QModelIndex KSelectionProxyModel.columnCount()'''
        return QModelIndex()
    def parent(self):
        '''QModelIndex KSelectionProxyModel.parent()'''
        return QModelIndex()
    def index(self):
        '''QModelIndex KSelectionProxyModel.index()'''
        return QModelIndex()
    def hasChildren(self, parent = QModelIndex()):
        '''bool KSelectionProxyModel.hasChildren(QModelIndex parent = QModelIndex())'''
        return bool()
    def dropMimeData(self, data, action, row, column, parent):
        '''bool KSelectionProxyModel.dropMimeData(QMimeData data, Qt.DropAction action, int row, int column, QModelIndex parent)'''
        return bool()
    def supportedDropActions(self):
        '''Qt.DropActions KSelectionProxyModel.supportedDropActions()'''
        return Qt.DropActions()
    def mimeTypes(self):
        '''QStringList KSelectionProxyModel.mimeTypes()'''
        return QStringList()
    def mimeData(self, indexes):
        '''QMimeData KSelectionProxyModel.mimeData(list-of-QModelIndex indexes)'''
        return QMimeData()
    def headerData(self, section, orientation, role = None):
        '''QVariant KSelectionProxyModel.headerData(int section, Qt.Orientation orientation, int role = Qt.DisplayRole)'''
        return QVariant()
    def rowCount(self, parent = QModelIndex()):
        '''int KSelectionProxyModel.rowCount(QModelIndex parent = QModelIndex())'''
        return int()
    def data(self, index, role = None):
        '''QVariant KSelectionProxyModel.data(QModelIndex index, int role = Qt.DisplayRole)'''
        return QVariant()
    def flags(self, index):
        '''Qt.ItemFlags KSelectionProxyModel.flags(QModelIndex index)'''
        return Qt.ItemFlags()
    def mapToSource(self, proxyIndex):
        '''QModelIndex KSelectionProxyModel.mapToSource(QModelIndex proxyIndex)'''
        return QModelIndex()
    def mapFromSource(self, sourceIndex):
        '''QModelIndex KSelectionProxyModel.mapFromSource(QModelIndex sourceIndex)'''
        return QModelIndex()
    def filterBehavior(self):
        '''KSelectionProxyModel.FilterBehavior KSelectionProxyModel.filterBehavior()'''
        return KSelectionProxyModel.FilterBehavior()
    def setFilterBehavior(self, behavior):
        '''void KSelectionProxyModel.setFilterBehavior(KSelectionProxyModel.FilterBehavior behavior)'''
    def selectionModel(self):
        '''QItemSelectionModel KSelectionProxyModel.selectionModel()'''
        return QItemSelectionModel()
    def setSourceModel(self, sourceModel):
        '''void KSelectionProxyModel.setSourceModel(QAbstractItemModel sourceModel)'''


class KGradientSelector(KSelector):
    """"""
    def __init__(self, parent = None):
        '''void KGradientSelector.__init__(QWidget parent = None)'''
    def __init__(self, o, parent = None):
        '''void KGradientSelector.__init__(Qt.Orientation o, QWidget parent = None)'''
    def stops(self):
        '''list-of-tuple-of-float-QColor KGradientSelector.stops()'''
        return [tuple-of-float-QColor()]
    def setStops(self, stops):
        '''void KGradientSelector.setStops(list-of-tuple-of-float-QColor stops)'''
    def minimumSize(self):
        '''QSize KGradientSelector.minimumSize()'''
        return QSize()
    def drawContents(self):
        '''QPainter KGradientSelector.drawContents()'''
        return QPainter()
    def secondText(self):
        '''QString KGradientSelector.secondText()'''
        return QString()
    def firstText(self):
        '''QString KGradientSelector.firstText()'''
        return QString()
    def secondColor(self):
        '''QColor KGradientSelector.secondColor()'''
        return QColor()
    def firstColor(self):
        '''QColor KGradientSelector.firstColor()'''
        return QColor()
    def setSecondText(self, t):
        '''void KGradientSelector.setSecondText(QString t)'''
    def setFirstText(self, t):
        '''void KGradientSelector.setFirstText(QString t)'''
    def setSecondColor(self, col):
        '''void KGradientSelector.setSecondColor(QColor col)'''
    def setFirstColor(self, col):
        '''void KGradientSelector.setFirstColor(QColor col)'''
    def setText(self, t1, t2):
        '''void KGradientSelector.setText(QString t1, QString t2)'''
    def setColors(self, col1, col2):
        '''void KGradientSelector.setColors(QColor col1, QColor col2)'''


class KSeparator(QFrame):
    """"""
    def __init__(self, parent = None, f = 0):
        '''void KSeparator.__init__(QWidget parent = None, Qt.WindowFlags f = 0)'''
    def __init__(self, orientation, parent = None, f = 0):
        '''void KSeparator.__init__(Qt.Orientation orientation, QWidget parent = None, Qt.WindowFlags f = 0)'''
    def setOrientation(self, orientation):
        '''void KSeparator.setOrientation(Qt.Orientation orientation)'''
    def orientation(self):
        '''Qt.Orientation KSeparator.orientation()'''
        return Qt.Orientation()


class KSessionManager():
    """"""
    def __init__(self):
        '''void KSessionManager.__init__()'''
    def sessionClients(self):
        '''static list-of-KSessionManager KSessionManager.sessionClients()'''
        return [KSessionManager()]
    def commitData(self, sm):
        '''bool KSessionManager.commitData(QSessionManager sm)'''
        return bool()
    def saveState(self, sm):
        '''bool KSessionManager.saveState(QSessionManager sm)'''
        return bool()


class KShortcut():
    """"""
    # Enum KShortcut.EmptyHandling
    KeepEmpty = 0
    RemoveEmpty = 0

    def __init__(self):
        '''void KShortcut.__init__()'''
    def __init__(self, primary):
        '''void KShortcut.__init__(QKeySequence primary)'''
    def __init__(self, primary, alternate):
        '''void KShortcut.__init__(QKeySequence primary, QKeySequence alternate)'''
    def __init__(self, keyQtPri, keyQtAlt = 0):
        '''void KShortcut.__init__(int keyQtPri, int keyQtAlt = 0)'''
    def __init__(self, other):
        '''void KShortcut.__init__(KShortcut other)'''
    def __init__(self, description):
        '''void KShortcut.__init__(QString description)'''
    def __init__(self, seqs):
        '''void KShortcut.__init__(list-of-QKeySequence seqs)'''
    def remove(self, keySeq, handleEmpty = None):
        '''void KShortcut.remove(QKeySequence keySeq, KShortcut.EmptyHandling handleEmpty = KShortcut.RemoveEmpty)'''
    def setAlternate(self, keySeq):
        '''void KShortcut.setAlternate(QKeySequence keySeq)'''
    def setPrimary(self, keySeq):
        '''void KShortcut.setPrimary(QKeySequence keySeq)'''
    def toList(self, handleEmpty = None):
        '''list-of-QKeySequence KShortcut.toList(KShortcut.EmptyHandling handleEmpty = KShortcut.RemoveEmpty)'''
        return [QKeySequence()]
    def __ne__(self, other):
        '''bool KShortcut.__ne__(KShortcut other)'''
        return bool()
    def __eq__(self, other):
        '''bool KShortcut.__eq__(KShortcut other)'''
        return bool()
    def toString(self):
        '''QString KShortcut.toString()'''
        return QString()
    def toString(self, format):
        '''QString KShortcut.toString(QKeySequence.SequenceFormat format)'''
        return QString()
    def conflictsWith(self, needle):
        '''bool KShortcut.conflictsWith(QKeySequence needle)'''
        return bool()
    def contains(self, needle):
        '''bool KShortcut.contains(QKeySequence needle)'''
        return bool()
    def isEmpty(self):
        '''bool KShortcut.isEmpty()'''
        return bool()
    def alternate(self):
        '''QKeySequence KShortcut.alternate()'''
        return QKeySequence()
    def primary(self):
        '''QKeySequence KShortcut.primary()'''
        return QKeySequence()


class KShortcutsDialog(KDialog):
    """"""
    def __init__(self, types = None, allowLetterShortcuts = None, parent = None):
        '''void KShortcutsDialog.__init__(KShortcutsEditor.ActionTypes types = KShortcutsEditor.AllActions, KShortcutsEditor.LetterShortcuts allowLetterShortcuts = KShortcutsEditor.LetterShortcutsAllowed, QWidget parent = None)'''
    saved = pyqtSignal() # void saved() - signal
    def sizeHint(self):
        '''QSize KShortcutsDialog.sizeHint()'''
        return QSize()
    def configure(self, saveSettings = True):
        '''bool KShortcutsDialog.configure(bool saveSettings = True)'''
        return bool()
    def configure(self, collection, allowLetterShortcuts = None, parent = None, bSaveSettings = True):
        '''static int KShortcutsDialog.configure(KActionCollection collection, KShortcutsEditor.LetterShortcuts allowLetterShortcuts = KShortcutsEditor.LetterShortcutsAllowed, QWidget parent = None, bool bSaveSettings = True)'''
        return int()
    def actionCollections(self):
        '''list-of-KActionCollection KShortcutsDialog.actionCollections()'''
        return [KActionCollection()]
    def addCollection(self, title = QString()):
        '''KActionCollection KShortcutsDialog.addCollection(QString title = QString())'''
        return KActionCollection()


class KShortcutsEditor(QWidget):
    """"""
    # Enum KShortcutsEditor.LetterShortcuts
    LetterShortcutsDisallowed = 0
    LetterShortcutsAllowed = 0

    # Enum KShortcutsEditor.ActionType
    WidgetAction = 0
    WindowAction = 0
    ApplicationAction = 0
    GlobalAction = 0
    AllActions = 0

    def __init__(self, collection, parent, actionTypes = None, allowLetterShortcuts = None):
        '''void KShortcutsEditor.__init__(KActionCollection collection, QWidget parent, KShortcutsEditor.ActionTypes actionTypes = KShortcutsEditor.AllActions, KShortcutsEditor.LetterShortcuts allowLetterShortcuts = KShortcutsEditor.LetterShortcutsAllowed)'''
    def __init__(self, parent, actionTypes = None, allowLetterShortcuts = None):
        '''void KShortcutsEditor.__init__(QWidget parent, KShortcutsEditor.ActionTypes actionTypes = KShortcutsEditor.AllActions, KShortcutsEditor.LetterShortcuts allowLetterShortcuts = KShortcutsEditor.LetterShortcutsAllowed)'''
    def printShortcuts(self):
        '''void KShortcutsEditor.printShortcuts()'''
    def allDefault(self):
        '''void KShortcutsEditor.allDefault()'''
    def resizeColumns(self):
        '''void KShortcutsEditor.resizeColumns()'''
    keyChange = pyqtSignal() # void keyChange() - signal
    def importConfiguration(self, config):
        '''void KShortcutsEditor.importConfiguration(KConfig config)'''
    def importConfiguration(self, config):
        '''void KShortcutsEditor.importConfiguration(KConfigBase config)'''
    def exportConfiguration(self, config):
        '''void KShortcutsEditor.exportConfiguration(KConfig config)'''
    def exportConfiguration(self, config):
        '''void KShortcutsEditor.exportConfiguration(KConfigBase config)'''
    def writeConfiguration(self, config = None):
        '''void KShortcutsEditor.writeConfiguration(KConfigGroup config = None)'''
    def clearConfiguration(self):
        '''void KShortcutsEditor.clearConfiguration()'''
    def commit(self):
        '''void KShortcutsEditor.commit()'''
    def save(self):
        '''void KShortcutsEditor.save()'''
    def undoChanges(self):
        '''void KShortcutsEditor.undoChanges()'''
    def addCollection(self, title = QString()):
        '''KActionCollection KShortcutsEditor.addCollection(QString title = QString())'''
        return KActionCollection()
    def clearCollections(self):
        '''void KShortcutsEditor.clearCollections()'''
    def isModified(self):
        '''bool KShortcutsEditor.isModified()'''
        return bool()
    class ActionTypes():
        """"""
        def __init__(self):
            '''KShortcutsEditor.ActionTypes KShortcutsEditor.ActionTypes.__init__()'''
            return KShortcutsEditor.ActionTypes()
        def __init__(self):
            '''int KShortcutsEditor.ActionTypes.__init__()'''
            return int()
        def __init__(self):
            '''void KShortcutsEditor.ActionTypes.__init__()'''
        def __bool__(self):
            '''int KShortcutsEditor.ActionTypes.__bool__()'''
            return int()
        def __ne__(self, f):
            '''bool KShortcutsEditor.ActionTypes.__ne__(KShortcutsEditor.ActionTypes f)'''
            return bool()
        def __eq__(self, f):
            '''bool KShortcutsEditor.ActionTypes.__eq__(KShortcutsEditor.ActionTypes f)'''
            return bool()
        def __invert__(self):
            '''KShortcutsEditor.ActionTypes KShortcutsEditor.ActionTypes.__invert__()'''
            return KShortcutsEditor.ActionTypes()
        def __and__(self, mask):
            '''KShortcutsEditor.ActionTypes KShortcutsEditor.ActionTypes.__and__(int mask)'''
            return KShortcutsEditor.ActionTypes()
        def __xor__(self, f):
            '''KShortcutsEditor.ActionTypes KShortcutsEditor.ActionTypes.__xor__(KShortcutsEditor.ActionTypes f)'''
            return KShortcutsEditor.ActionTypes()
        def __xor__(self, f):
            '''KShortcutsEditor.ActionTypes KShortcutsEditor.ActionTypes.__xor__(int f)'''
            return KShortcutsEditor.ActionTypes()
        def __or__(self, f):
            '''KShortcutsEditor.ActionTypes KShortcutsEditor.ActionTypes.__or__(KShortcutsEditor.ActionTypes f)'''
            return KShortcutsEditor.ActionTypes()
        def __or__(self, f):
            '''KShortcutsEditor.ActionTypes KShortcutsEditor.ActionTypes.__or__(int f)'''
            return KShortcutsEditor.ActionTypes()
        def __int__(self):
            '''int KShortcutsEditor.ActionTypes.__int__()'''
            return int()
        def __ixor__(self, f):
            '''KShortcutsEditor.ActionTypes KShortcutsEditor.ActionTypes.__ixor__(KShortcutsEditor.ActionTypes f)'''
            return KShortcutsEditor.ActionTypes()
        def __ior__(self, f):
            '''KShortcutsEditor.ActionTypes KShortcutsEditor.ActionTypes.__ior__(KShortcutsEditor.ActionTypes f)'''
            return KShortcutsEditor.ActionTypes()
        def __iand__(self, mask):
            '''KShortcutsEditor.ActionTypes KShortcutsEditor.ActionTypes.__iand__(int mask)'''
            return KShortcutsEditor.ActionTypes()


class KShortcutWidget(QWidget):
    """"""
    def __init__(self, parent = None):
        '''void KShortcutWidget.__init__(QWidget parent = None)'''
    def applyStealShortcut(self):
        '''void KShortcutWidget.applyStealShortcut()'''
    def clearShortcut(self):
        '''void KShortcutWidget.clearShortcut()'''
    def setShortcut(self, cut):
        '''void KShortcutWidget.setShortcut(KShortcut cut)'''
    shortcutChanged = pyqtSignal() # void shortcutChanged(const KShortcutamp;) - signal
    def setCheckActionList(self, checkList):
        '''void KShortcutWidget.setCheckActionList(list-of-QAction checkList)'''
    def setCheckActionCollections(self, actionCollections):
        '''void KShortcutWidget.setCheckActionCollections(list-of-KActionCollection actionCollections)'''
    def setClearButtonsShown(self, show):
        '''void KShortcutWidget.setClearButtonsShown(bool show)'''
    def isModifierlessAllowed(self):
        '''bool KShortcutWidget.isModifierlessAllowed()'''
        return bool()
    def setModifierlessAllowed(self, allow):
        '''void KShortcutWidget.setModifierlessAllowed(bool allow)'''


class KSplashScreen(QSplashScreen):
    """"""
    def __init__(self, pixmap, f = 0):
        '''void KSplashScreen.__init__(QPixmap pixmap, Qt.WindowFlags f = 0)'''


class KSqueezedTextLabel(QLabel):
    """"""
    def __init__(self, parent = None):
        '''void KSqueezedTextLabel.__init__(QWidget parent = None)'''
    def __init__(self, text, parent = None):
        '''void KSqueezedTextLabel.__init__(QString text, QWidget parent = None)'''
    def mouseReleaseEvent(self):
        '''QMouseEvent KSqueezedTextLabel.mouseReleaseEvent()'''
        return QMouseEvent()
    def fullText(self):
        '''QString KSqueezedTextLabel.fullText()'''
        return QString()
    def squeezeTextToLabel(self):
        '''void KSqueezedTextLabel.squeezeTextToLabel()'''
    def contextMenuEvent(self):
        '''QContextMenuEvent KSqueezedTextLabel.contextMenuEvent()'''
        return QContextMenuEvent()
    def resizeEvent(self):
        '''QResizeEvent KSqueezedTextLabel.resizeEvent()'''
        return QResizeEvent()
    def clear(self):
        '''void KSqueezedTextLabel.clear()'''
    def setText(self, text):
        '''void KSqueezedTextLabel.setText(QString text)'''
    def setTextElideMode(self, mode):
        '''void KSqueezedTextLabel.setTextElideMode(Qt.TextElideMode mode)'''
    def textElideMode(self):
        '''Qt.TextElideMode KSqueezedTextLabel.textElideMode()'''
        return Qt.TextElideMode()
    def setAlignment(self):
        '''Qt.Alignment KSqueezedTextLabel.setAlignment()'''
        return Qt.Alignment()
    def sizeHint(self):
        '''QSize KSqueezedTextLabel.sizeHint()'''
        return QSize()
    def minimumSizeHint(self):
        '''QSize KSqueezedTextLabel.minimumSizeHint()'''
        return QSize()


class KStandardAction():
    """"""
    # Enum KStandardAction.StandardAction
    ActionNone = 0
    New = 0
    Open = 0
    OpenRecent = 0
    Save = 0
    SaveAs = 0
    Revert = 0
    Close = 0
    Print = 0
    PrintPreview = 0
    Mail = 0
    Quit = 0
    Undo = 0
    Redo = 0
    Cut = 0
    Copy = 0
    Paste = 0
    SelectAll = 0
    Deselect = 0
    Find = 0
    FindNext = 0
    FindPrev = 0
    Replace = 0
    ActualSize = 0
    FitToPage = 0
    FitToWidth = 0
    FitToHeight = 0
    ZoomIn = 0
    ZoomOut = 0
    Zoom = 0
    Redisplay = 0
    Up = 0
    Back = 0
    Forward = 0
    Home = 0
    Prior = 0
    Next = 0
    Goto = 0
    GotoPage = 0
    GotoLine = 0
    FirstPage = 0
    LastPage = 0
    DocumentBack = 0
    DocumentForward = 0
    AddBookmark = 0
    EditBookmarks = 0
    Spelling = 0
    ShowMenubar = 0
    ShowToolbar = 0
    ShowStatusbar = 0
    SaveOptions = 0
    KeyBindings = 0
    Preferences = 0
    ConfigureToolbars = 0
    Help = 0
    HelpContents = 0
    WhatsThis = 0
    ReportBug = 0
    AboutApp = 0
    AboutKDE = 0
    TipofDay = 0
    ConfigureNotifications = 0
    FullScreen = 0
    Clear = 0
    PasteText = 0
    SwitchApplicationLanguage = 0

    def aboutKDE(self, parent):
        '''static SLOT() KStandardAction.aboutKDE(QObject parent)'''
        return SLOT()()
    def aboutKDE(self, parent):
        '''static callable KStandardAction.aboutKDE(QObject parent)'''
        return callable()
    def aboutApp(self, parent):
        '''static SLOT() KStandardAction.aboutApp(QObject parent)'''
        return SLOT()()
    def aboutApp(self, parent):
        '''static callable KStandardAction.aboutApp(QObject parent)'''
        return callable()
    def reportBug(self, parent):
        '''static SLOT() KStandardAction.reportBug(QObject parent)'''
        return SLOT()()
    def reportBug(self, parent):
        '''static callable KStandardAction.reportBug(QObject parent)'''
        return callable()
    def tipOfDay(self, parent):
        '''static SLOT() KStandardAction.tipOfDay(QObject parent)'''
        return SLOT()()
    def tipOfDay(self, parent):
        '''static callable KStandardAction.tipOfDay(QObject parent)'''
        return callable()
    def whatsThis(self, parent):
        '''static SLOT() KStandardAction.whatsThis(QObject parent)'''
        return SLOT()()
    def whatsThis(self, parent):
        '''static callable KStandardAction.whatsThis(QObject parent)'''
        return callable()
    def helpContents(self, parent):
        '''static SLOT() KStandardAction.helpContents(QObject parent)'''
        return SLOT()()
    def helpContents(self, parent):
        '''static callable KStandardAction.helpContents(QObject parent)'''
        return callable()
    def help(self, parent):
        '''static SLOT() KStandardAction.help(QObject parent)'''
        return SLOT()()
    def help(self, parent):
        '''static callable KStandardAction.help(QObject parent)'''
        return callable()
    def configureNotifications(self, parent):
        '''static SLOT() KStandardAction.configureNotifications(QObject parent)'''
        return SLOT()()
    def configureNotifications(self, parent):
        '''static callable KStandardAction.configureNotifications(QObject parent)'''
        return callable()
    def configureToolbars(self, parent):
        '''static SLOT() KStandardAction.configureToolbars(QObject parent)'''
        return SLOT()()
    def configureToolbars(self, parent):
        '''static callable KStandardAction.configureToolbars(QObject parent)'''
        return callable()
    def preferences(self, parent):
        '''static SLOT() KStandardAction.preferences(QObject parent)'''
        return SLOT()()
    def preferences(self, parent):
        '''static callable KStandardAction.preferences(QObject parent)'''
        return callable()
    def keyBindings(self, parent):
        '''static SLOT() KStandardAction.keyBindings(QObject parent)'''
        return SLOT()()
    def keyBindings(self, parent):
        '''static callable KStandardAction.keyBindings(QObject parent)'''
        return callable()
    def saveOptions(self, parent):
        '''static SLOT() KStandardAction.saveOptions(QObject parent)'''
        return SLOT()()
    def saveOptions(self, parent):
        '''static callable KStandardAction.saveOptions(QObject parent)'''
        return callable()
    def fullScreen(self, window, parent):
        '''static SLOT() KStandardAction.fullScreen(QWidget window, QObject parent)'''
        return SLOT()()
    def fullScreen(self, window, parent):
        '''static callable KStandardAction.fullScreen(QWidget window, QObject parent)'''
        return callable()
    def showStatusbar(self, parent):
        '''static SLOT() KStandardAction.showStatusbar(QObject parent)'''
        return SLOT()()
    def showStatusbar(self, parent):
        '''static callable KStandardAction.showStatusbar(QObject parent)'''
        return callable()
    def showMenubar(self, parent):
        '''static SLOT() KStandardAction.showMenubar(QObject parent)'''
        return SLOT()()
    def showMenubar(self, parent):
        '''static callable KStandardAction.showMenubar(QObject parent)'''
        return callable()
    def spelling(self, parent):
        '''static SLOT() KStandardAction.spelling(QObject parent)'''
        return SLOT()()
    def spelling(self, parent):
        '''static callable KStandardAction.spelling(QObject parent)'''
        return callable()
    def editBookmarks(self, parent):
        '''static SLOT() KStandardAction.editBookmarks(QObject parent)'''
        return SLOT()()
    def editBookmarks(self, parent):
        '''static callable KStandardAction.editBookmarks(QObject parent)'''
        return callable()
    def addBookmark(self, parent):
        '''static SLOT() KStandardAction.addBookmark(QObject parent)'''
        return SLOT()()
    def addBookmark(self, parent):
        '''static callable KStandardAction.addBookmark(QObject parent)'''
        return callable()
    def documentForward(self, parent):
        '''static SLOT() KStandardAction.documentForward(QObject parent)'''
        return SLOT()()
    def documentForward(self, parent):
        '''static callable KStandardAction.documentForward(QObject parent)'''
        return callable()
    def documentBack(self, parent):
        '''static SLOT() KStandardAction.documentBack(QObject parent)'''
        return SLOT()()
    def documentBack(self, parent):
        '''static callable KStandardAction.documentBack(QObject parent)'''
        return callable()
    def lastPage(self, parent):
        '''static SLOT() KStandardAction.lastPage(QObject parent)'''
        return SLOT()()
    def lastPage(self, parent):
        '''static callable KStandardAction.lastPage(QObject parent)'''
        return callable()
    def firstPage(self, parent):
        '''static SLOT() KStandardAction.firstPage(QObject parent)'''
        return SLOT()()
    def firstPage(self, parent):
        '''static callable KStandardAction.firstPage(QObject parent)'''
        return callable()
    def gotoLine(self, parent):
        '''static SLOT() KStandardAction.gotoLine(QObject parent)'''
        return SLOT()()
    def gotoLine(self, parent):
        '''static callable KStandardAction.gotoLine(QObject parent)'''
        return callable()
    def gotoPage(self, parent):
        '''static SLOT() KStandardAction.gotoPage(QObject parent)'''
        return SLOT()()
    def gotoPage(self, parent):
        '''static callable KStandardAction.gotoPage(QObject parent)'''
        return callable()
    def goTo(self, parent):
        '''static SLOT() KStandardAction.goTo(QObject parent)'''
        return SLOT()()
    def goTo(self, parent):
        '''static callable KStandardAction.goTo(QObject parent)'''
        return callable()
    def next(self, parent):
        '''static SLOT() KStandardAction.next(QObject parent)'''
        return SLOT()()
    def next(self, parent):
        '''static callable KStandardAction.next(QObject parent)'''
        return callable()
    def prior(self, parent):
        '''static SLOT() KStandardAction.prior(QObject parent)'''
        return SLOT()()
    def prior(self, parent):
        '''static callable KStandardAction.prior(QObject parent)'''
        return callable()
    def home(self, parent):
        '''static SLOT() KStandardAction.home(QObject parent)'''
        return SLOT()()
    def home(self, parent):
        '''static callable KStandardAction.home(QObject parent)'''
        return callable()
    def forward(self, parent):
        '''static SLOT() KStandardAction.forward(QObject parent)'''
        return SLOT()()
    def forward(self, parent):
        '''static callable KStandardAction.forward(QObject parent)'''
        return callable()
    def back(self, parent):
        '''static SLOT() KStandardAction.back(QObject parent)'''
        return SLOT()()
    def back(self, parent):
        '''static callable KStandardAction.back(QObject parent)'''
        return callable()
    def up(self, parent):
        '''static SLOT() KStandardAction.up(QObject parent)'''
        return SLOT()()
    def up(self, parent):
        '''static callable KStandardAction.up(QObject parent)'''
        return callable()
    def redisplay(self, parent):
        '''static SLOT() KStandardAction.redisplay(QObject parent)'''
        return SLOT()()
    def redisplay(self, parent):
        '''static callable KStandardAction.redisplay(QObject parent)'''
        return callable()
    def zoom(self, parent):
        '''static SLOT() KStandardAction.zoom(QObject parent)'''
        return SLOT()()
    def zoom(self, parent):
        '''static callable KStandardAction.zoom(QObject parent)'''
        return callable()
    def zoomOut(self, parent):
        '''static SLOT() KStandardAction.zoomOut(QObject parent)'''
        return SLOT()()
    def zoomOut(self, parent):
        '''static callable KStandardAction.zoomOut(QObject parent)'''
        return callable()
    def zoomIn(self, parent):
        '''static SLOT() KStandardAction.zoomIn(QObject parent)'''
        return SLOT()()
    def zoomIn(self, parent):
        '''static callable KStandardAction.zoomIn(QObject parent)'''
        return callable()
    def fitToHeight(self, parent):
        '''static SLOT() KStandardAction.fitToHeight(QObject parent)'''
        return SLOT()()
    def fitToHeight(self, parent):
        '''static callable KStandardAction.fitToHeight(QObject parent)'''
        return callable()
    def fitToWidth(self, parent):
        '''static SLOT() KStandardAction.fitToWidth(QObject parent)'''
        return SLOT()()
    def fitToWidth(self, parent):
        '''static callable KStandardAction.fitToWidth(QObject parent)'''
        return callable()
    def fitToPage(self, parent):
        '''static SLOT() KStandardAction.fitToPage(QObject parent)'''
        return SLOT()()
    def fitToPage(self, parent):
        '''static callable KStandardAction.fitToPage(QObject parent)'''
        return callable()
    def actualSize(self, parent):
        '''static SLOT() KStandardAction.actualSize(QObject parent)'''
        return SLOT()()
    def actualSize(self, parent):
        '''static callable KStandardAction.actualSize(QObject parent)'''
        return callable()
    def replace(self, parent):
        '''static SLOT() KStandardAction.replace(QObject parent)'''
        return SLOT()()
    def replace(self, parent):
        '''static callable KStandardAction.replace(QObject parent)'''
        return callable()
    def findPrev(self, parent):
        '''static SLOT() KStandardAction.findPrev(QObject parent)'''
        return SLOT()()
    def findPrev(self, parent):
        '''static callable KStandardAction.findPrev(QObject parent)'''
        return callable()
    def findNext(self, parent):
        '''static SLOT() KStandardAction.findNext(QObject parent)'''
        return SLOT()()
    def findNext(self, parent):
        '''static callable KStandardAction.findNext(QObject parent)'''
        return callable()
    def find(self, parent):
        '''static SLOT() KStandardAction.find(QObject parent)'''
        return SLOT()()
    def find(self, parent):
        '''static callable KStandardAction.find(QObject parent)'''
        return callable()
    def deselect(self, parent):
        '''static SLOT() KStandardAction.deselect(QObject parent)'''
        return SLOT()()
    def deselect(self, parent):
        '''static callable KStandardAction.deselect(QObject parent)'''
        return callable()
    def pasteText(self, parent):
        '''static SLOT() KStandardAction.pasteText(QObject parent)'''
        return SLOT()()
    def pasteText(self, parent):
        '''static callable KStandardAction.pasteText(QObject parent)'''
        return callable()
    def selectAll(self, parent):
        '''static KAction KStandardAction.selectAll(QObject parent)'''
        return KAction()
    def selectAll(self, parent):
        '''static SLOT() KStandardAction.selectAll(QObject parent)'''
        return SLOT()()
    def selectAll(self, parent):
        '''static callable KStandardAction.selectAll(QObject parent)'''
        return callable()
    def clear(self, parent):
        '''static KAction KStandardAction.clear(QObject parent)'''
        return KAction()
    def clear(self, parent):
        '''static SLOT() KStandardAction.clear(QObject parent)'''
        return SLOT()()
    def clear(self, parent):
        '''static callable KStandardAction.clear(QObject parent)'''
        return callable()
    def paste(self, parent):
        '''static KAction KStandardAction.paste(QObject parent)'''
        return KAction()
    def paste(self, parent):
        '''static SLOT() KStandardAction.paste(QObject parent)'''
        return SLOT()()
    def paste(self, parent):
        '''static callable KStandardAction.paste(QObject parent)'''
        return callable()
    def copy(self, parent):
        '''static KAction KStandardAction.copy(QObject parent)'''
        return KAction()
    def copy(self, parent):
        '''static SLOT() KStandardAction.copy(QObject parent)'''
        return SLOT()()
    def copy(self, parent):
        '''static callable KStandardAction.copy(QObject parent)'''
        return callable()
    def cut(self, parent):
        '''static KAction KStandardAction.cut(QObject parent)'''
        return KAction()
    def cut(self, parent):
        '''static SLOT() KStandardAction.cut(QObject parent)'''
        return SLOT()()
    def cut(self, parent):
        '''static callable KStandardAction.cut(QObject parent)'''
        return callable()
    def redo(self, parent):
        '''static SLOT() KStandardAction.redo(QObject parent)'''
        return SLOT()()
    def redo(self, parent):
        '''static callable KStandardAction.redo(QObject parent)'''
        return callable()
    def undo(self, parent):
        '''static SLOT() KStandardAction.undo(QObject parent)'''
        return SLOT()()
    def undo(self, parent):
        '''static callable KStandardAction.undo(QObject parent)'''
        return callable()
    def quit(self, parent):
        '''static SLOT() KStandardAction.quit(QObject parent)'''
        return SLOT()()
    def quit(self, parent):
        '''static callable KStandardAction.quit(QObject parent)'''
        return callable()
    def mail(self, parent):
        '''static SLOT() KStandardAction.mail(QObject parent)'''
        return SLOT()()
    def mail(self, parent):
        '''static callable KStandardAction.mail(QObject parent)'''
        return callable()
    def printPreview(self, parent):
        '''static SLOT() KStandardAction.printPreview(QObject parent)'''
        return SLOT()()
    def printPreview(self, parent):
        '''static callable KStandardAction.printPreview(QObject parent)'''
        return callable()
    def print_(self, parent):
        '''static SLOT() KStandardAction.print_(QObject parent)'''
        return SLOT()()
    def print_(self, parent):
        '''static callable KStandardAction.print_(QObject parent)'''
        return callable()
    def close(self, parent):
        '''static SLOT() KStandardAction.close(QObject parent)'''
        return SLOT()()
    def close(self, parent):
        '''static callable KStandardAction.close(QObject parent)'''
        return callable()
    def revert(self, parent):
        '''static SLOT() KStandardAction.revert(QObject parent)'''
        return SLOT()()
    def revert(self, parent):
        '''static callable KStandardAction.revert(QObject parent)'''
        return callable()
    def saveAs(self, parent):
        '''static SLOT() KStandardAction.saveAs(QObject parent)'''
        return SLOT()()
    def saveAs(self, parent):
        '''static callable KStandardAction.saveAs(QObject parent)'''
        return callable()
    def save(self, parent):
        '''static SLOT() KStandardAction.save(QObject parent)'''
        return SLOT()()
    def save(self, parent):
        '''static callable KStandardAction.save(QObject parent)'''
        return callable()
    def openRecent(self, parent):
        '''static SLOT() KStandardAction.openRecent(QObject parent)'''
        return SLOT()()
    def openRecent(self, parent):
        '''static callable KStandardAction.openRecent(QObject parent)'''
        return callable()
    def open(self, parent):
        '''static SLOT() KStandardAction.open(QObject parent)'''
        return SLOT()()
    def open(self, parent):
        '''static callable KStandardAction.open(QObject parent)'''
        return callable()
    def openNew(self, parent):
        '''static SLOT() KStandardAction.openNew(QObject parent)'''
        return SLOT()()
    def openNew(self, parent):
        '''static callable KStandardAction.openNew(QObject parent)'''
        return callable()
    def shortcutForActionId(self, id):
        '''static KStandardShortcut.StandardShortcut KStandardAction.shortcutForActionId(KStandardAction.StandardAction id)'''
        return KStandardShortcut.StandardShortcut()
    def actionIds(self):
        '''static unknown-type KStandardAction.actionIds()'''
        return unknown-type()
    def stdNames(self):
        '''static QStringList KStandardAction.stdNames()'''
        return QStringList()
    def stdName(self, act_enum):
        '''static str KStandardAction.stdName(KStandardAction.StandardAction act_enum)'''
        return str()
    def name(self, id):
        '''static str KStandardAction.name(KStandardAction.StandardAction id)'''
        return str()
    def create(self, id, parent):
        '''static SLOT() KStandardAction.create(KStandardAction.StandardAction id, QObject parent)'''
        return SLOT()()
    def create(self, id, parent):
        '''static callable KStandardAction.create(KStandardAction.StandardAction id, QObject parent)'''
        return callable()


class KStandardGuiItem():
    """"""
    # Enum KStandardGuiItem.StandardItem
    Ok = 0
    Cancel = 0
    Yes = 0
    No = 0
    Discard = 0
    Save = 0
    DontSave = 0
    SaveAs = 0
    Apply = 0
    Clear = 0
    Help = 0
    Defaults = 0
    Close = 0
    Back = 0
    Forward = 0
    Print = 0
    Continue = 0
    Open = 0
    Quit = 0
    AdminMode = 0
    Reset = 0
    Delete = 0
    Insert = 0
    Configure = 0
    Find = 0
    Stop = 0
    Add = 0
    Remove = 0
    Test = 0
    Properties = 0
    Overwrite = 0
    CloseWindow = 0
    CloseDocument = 0

    # Enum KStandardGuiItem.BidiMode
    UseRTL = 0
    IgnoreRTL = 0

    def test(self):
        '''static KGuiItem KStandardGuiItem.test()'''
        return KGuiItem()
    def remove(self):
        '''static KGuiItem KStandardGuiItem.remove()'''
        return KGuiItem()
    def add(self):
        '''static KGuiItem KStandardGuiItem.add()'''
        return KGuiItem()
    def stop(self):
        '''static KGuiItem KStandardGuiItem.stop()'''
        return KGuiItem()
    def find(self):
        '''static KGuiItem KStandardGuiItem.find()'''
        return KGuiItem()
    def quit(self):
        '''static KGuiItem KStandardGuiItem.quit()'''
        return KGuiItem()
    def backAndForward(self):
        '''static unknown-type KStandardGuiItem.backAndForward()'''
        return unknown-type()
    def configure(self):
        '''static KGuiItem KStandardGuiItem.configure()'''
        return KGuiItem()
    def forward(self, useBidi = None):
        '''static KGuiItem KStandardGuiItem.forward(KStandardGuiItem.BidiMode useBidi = KStandardGuiItem.IgnoreRTL)'''
        return KGuiItem()
    def back(self, useBidi = None):
        '''static KGuiItem KStandardGuiItem.back(KStandardGuiItem.BidiMode useBidi = KStandardGuiItem.IgnoreRTL)'''
        return KGuiItem()
    def open(self):
        '''static KGuiItem KStandardGuiItem.open()'''
        return KGuiItem()
    def del_(self):
        '''static KGuiItem KStandardGuiItem.del_()'''
        return KGuiItem()
    def cont(self):
        '''static KGuiItem KStandardGuiItem.cont()'''
        return KGuiItem()
    def adminMode(self):
        '''static KGuiItem KStandardGuiItem.adminMode()'''
        return KGuiItem()
    def overwrite(self):
        '''static KGuiItem KStandardGuiItem.overwrite()'''
        return KGuiItem()
    def reset(self):
        '''static KGuiItem KStandardGuiItem.reset()'''
        return KGuiItem()
    def properties(self):
        '''static KGuiItem KStandardGuiItem.properties()'''
        return KGuiItem()
    def print_(self):
        '''static KGuiItem KStandardGuiItem.print_()'''
        return KGuiItem()
    def closeDocument(self):
        '''static KGuiItem KStandardGuiItem.closeDocument()'''
        return KGuiItem()
    def closeWindow(self):
        '''static KGuiItem KStandardGuiItem.closeWindow()'''
        return KGuiItem()
    def close(self):
        '''static KGuiItem KStandardGuiItem.close()'''
        return KGuiItem()
    def defaults(self):
        '''static KGuiItem KStandardGuiItem.defaults()'''
        return KGuiItem()
    def clear(self):
        '''static KGuiItem KStandardGuiItem.clear()'''
        return KGuiItem()
    def apply(self):
        '''static KGuiItem KStandardGuiItem.apply()'''
        return KGuiItem()
    def saveAs(self):
        '''static KGuiItem KStandardGuiItem.saveAs()'''
        return KGuiItem()
    def dontSave(self):
        '''static KGuiItem KStandardGuiItem.dontSave()'''
        return KGuiItem()
    def help(self):
        '''static KGuiItem KStandardGuiItem.help()'''
        return KGuiItem()
    def save(self):
        '''static KGuiItem KStandardGuiItem.save()'''
        return KGuiItem()
    def discard(self):
        '''static KGuiItem KStandardGuiItem.discard()'''
        return KGuiItem()
    def insert(self):
        '''static KGuiItem KStandardGuiItem.insert()'''
        return KGuiItem()
    def no(self):
        '''static KGuiItem KStandardGuiItem.no()'''
        return KGuiItem()
    def yes(self):
        '''static KGuiItem KStandardGuiItem.yes()'''
        return KGuiItem()
    def cancel(self):
        '''static KGuiItem KStandardGuiItem.cancel()'''
        return KGuiItem()
    def ok(self):
        '''static KGuiItem KStandardGuiItem.ok()'''
        return KGuiItem()
    def standardItem(self, id):
        '''static QString KStandardGuiItem.standardItem(KStandardGuiItem.StandardItem id)'''
        return QString()
    def guiItem(self, id):
        '''static KGuiItem KStandardGuiItem.guiItem(KStandardGuiItem.StandardItem id)'''
        return KGuiItem()


class KStandardShortcut():
    """"""
    # Enum KStandardShortcut.StandardShortcut
    AccelNone = 0
    Open = 0
    New = 0
    Close = 0
    Save = 0
    Print = 0
    Quit = 0
    Undo = 0
    Redo = 0
    Cut = 0
    Copy = 0
    Paste = 0
    PasteSelection = 0
    SelectAll = 0
    Deselect = 0
    DeleteWordBack = 0
    DeleteWordForward = 0
    Find = 0
    FindNext = 0
    FindPrev = 0
    Replace = 0
    Home = 0
    Begin = 0
    End = 0
    Prior = 0
    Next = 0
    Up = 0
    Back = 0
    Forward = 0
    Reload = 0
    BeginningOfLine = 0
    EndOfLine = 0
    GotoLine = 0
    BackwardWord = 0
    ForwardWord = 0
    AddBookmark = 0
    ZoomIn = 0
    ZoomOut = 0
    FullScreen = 0
    ShowMenubar = 0
    TabNext = 0
    TabPrev = 0
    Help = 0
    WhatsThis = 0
    TextCompletion = 0
    PrevCompletion = 0
    NextCompletion = 0
    SubstringCompletion = 0
    RotateUp = 0
    RotateDown = 0
    OpenRecent = 0
    SaveAs = 0
    Revert = 0
    PrintPreview = 0
    Mail = 0
    Clear = 0
    ActualSize = 0
    FitToPage = 0
    FitToWidth = 0
    FitToHeight = 0
    Zoom = 0
    Goto = 0
    GotoPage = 0
    DocumentBack = 0
    DocumentForward = 0
    EditBookmarks = 0
    Spelling = 0
    ShowToolbar = 0
    ShowStatusbar = 0
    SaveOptions = 0
    KeyBindings = 0
    Preferences = 0
    ConfigureToolbars = 0
    ConfigureNotifications = 0
    TipofDay = 0
    ReportBug = 0
    SwitchApplicationLanguage = 0
    AboutApp = 0
    AboutKDE = 0
    StandardShortcutCount = 0

    def showMenubar(self):
        '''static KShortcut KStandardShortcut.showMenubar()'''
        return KShortcut()
    def forwardWord(self):
        '''static KShortcut KStandardShortcut.forwardWord()'''
        return KShortcut()
    def backwardWord(self):
        '''static KShortcut KStandardShortcut.backwardWord()'''
        return KShortcut()
    def forward(self):
        '''static KShortcut KStandardShortcut.forward()'''
        return KShortcut()
    def back(self):
        '''static KShortcut KStandardShortcut.back()'''
        return KShortcut()
    def up(self):
        '''static KShortcut KStandardShortcut.up()'''
        return KShortcut()
    def reload(self):
        '''static KShortcut KStandardShortcut.reload()'''
        return KShortcut()
    def rotateDown(self):
        '''static KShortcut KStandardShortcut.rotateDown()'''
        return KShortcut()
    def rotateUp(self):
        '''static KShortcut KStandardShortcut.rotateUp()'''
        return KShortcut()
    def substringCompletion(self):
        '''static KShortcut KStandardShortcut.substringCompletion()'''
        return KShortcut()
    def nextCompletion(self):
        '''static KShortcut KStandardShortcut.nextCompletion()'''
        return KShortcut()
    def prevCompletion(self):
        '''static KShortcut KStandardShortcut.prevCompletion()'''
        return KShortcut()
    def completion(self):
        '''static KShortcut KStandardShortcut.completion()'''
        return KShortcut()
    def help(self):
        '''static KShortcut KStandardShortcut.help()'''
        return KShortcut()
    def fullScreen(self):
        '''static KShortcut KStandardShortcut.fullScreen()'''
        return KShortcut()
    def tabPrev(self):
        '''static KShortcut KStandardShortcut.tabPrev()'''
        return KShortcut()
    def tabNext(self):
        '''static KShortcut KStandardShortcut.tabNext()'''
        return KShortcut()
    def addBookmark(self):
        '''static KShortcut KStandardShortcut.addBookmark()'''
        return KShortcut()
    def gotoLine(self):
        '''static KShortcut KStandardShortcut.gotoLine()'''
        return KShortcut()
    def next(self):
        '''static KShortcut KStandardShortcut.next()'''
        return KShortcut()
    def prior(self):
        '''static KShortcut KStandardShortcut.prior()'''
        return KShortcut()
    def endOfLine(self):
        '''static KShortcut KStandardShortcut.endOfLine()'''
        return KShortcut()
    def beginningOfLine(self):
        '''static KShortcut KStandardShortcut.beginningOfLine()'''
        return KShortcut()
    def end(self):
        '''static KShortcut KStandardShortcut.end()'''
        return KShortcut()
    def begin(self):
        '''static KShortcut KStandardShortcut.begin()'''
        return KShortcut()
    def home(self):
        '''static KShortcut KStandardShortcut.home()'''
        return KShortcut()
    def zoomOut(self):
        '''static KShortcut KStandardShortcut.zoomOut()'''
        return KShortcut()
    def zoomIn(self):
        '''static KShortcut KStandardShortcut.zoomIn()'''
        return KShortcut()
    def replace(self):
        '''static KShortcut KStandardShortcut.replace()'''
        return KShortcut()
    def findPrev(self):
        '''static KShortcut KStandardShortcut.findPrev()'''
        return KShortcut()
    def findNext(self):
        '''static KShortcut KStandardShortcut.findNext()'''
        return KShortcut()
    def deleteWordForward(self):
        '''static KShortcut KStandardShortcut.deleteWordForward()'''
        return KShortcut()
    def deleteWordBack(self):
        '''static KShortcut KStandardShortcut.deleteWordBack()'''
        return KShortcut()
    def selectAll(self):
        '''static KShortcut KStandardShortcut.selectAll()'''
        return KShortcut()
    def pasteSelection(self):
        '''static KShortcut KStandardShortcut.pasteSelection()'''
        return KShortcut()
    def paste(self):
        '''static KShortcut KStandardShortcut.paste()'''
        return KShortcut()
    def copy(self):
        '''static KShortcut KStandardShortcut.copy()'''
        return KShortcut()
    def cut(self):
        '''static KShortcut KStandardShortcut.cut()'''
        return KShortcut()
    def redo(self):
        '''static KShortcut KStandardShortcut.redo()'''
        return KShortcut()
    def undo(self):
        '''static KShortcut KStandardShortcut.undo()'''
        return KShortcut()
    def quit(self):
        '''static KShortcut KStandardShortcut.quit()'''
        return KShortcut()
    def print_(self):
        '''static KShortcut KStandardShortcut.print_()'''
        return KShortcut()
    def save(self):
        '''static KShortcut KStandardShortcut.save()'''
        return KShortcut()
    def close(self):
        '''static KShortcut KStandardShortcut.close()'''
        return KShortcut()
    def openNew(self):
        '''static KShortcut KStandardShortcut.openNew()'''
        return KShortcut()
    def open(self):
        '''static KShortcut KStandardShortcut.open()'''
        return KShortcut()
    def saveShortcut(self, id, newShortcut):
        '''static void KStandardShortcut.saveShortcut(KStandardShortcut.StandardShortcut id, KShortcut newShortcut)'''
    def hardcodedDefaultShortcut(self, id):
        '''static KShortcut KStandardShortcut.hardcodedDefaultShortcut(KStandardShortcut.StandardShortcut id)'''
        return KShortcut()
    def find(self, keySeq):
        '''static KStandardShortcut.StandardShortcut KStandardShortcut.find(QKeySequence keySeq)'''
        return KStandardShortcut.StandardShortcut()
    def find(self, keyName):
        '''static KStandardShortcut.StandardShortcut KStandardShortcut.find(str keyName)'''
        return KStandardShortcut.StandardShortcut()
    def find(self):
        '''static KShortcut KStandardShortcut.find()'''
        return KShortcut()
    def whatsThis(self, id):
        '''static QString KStandardShortcut.whatsThis(KStandardShortcut.StandardShortcut id)'''
        return QString()
    def whatsThis(self):
        '''static KShortcut KStandardShortcut.whatsThis()'''
        return KShortcut()
    def label(self, id):
        '''static QString KStandardShortcut.label(KStandardShortcut.StandardShortcut id)'''
        return QString()
    def name(self, id):
        '''static QString KStandardShortcut.name(KStandardShortcut.StandardShortcut id)'''
        return QString()
    def shortcut(self, id):
        '''static KShortcut KStandardShortcut.shortcut(KStandardShortcut.StandardShortcut id)'''
        return KShortcut()


class KStartupInfo(QObject):
    """"""
    # Enum KStartupInfo.startup_t
    NoMatch = 0
    Match = 0
    CantDetect = 0

    CleanOnCantDetect = None # int - member
    DisableKWinModule = None # int - member
    AnnounceSilenceChanges = None # int - member
    def __init__(self, flags, parent = None):
        '''void KStartupInfo.__init__(int flags, QObject parent = None)'''
    def customEvent(self, e_P):
        '''void KStartupInfo.customEvent(QEvent e_P)'''
    gotRemoveStartup = pyqtSignal() # void gotRemoveStartup(const KStartupInfoIdamp;,const KStartupInfoDataamp;) - signal
    gotStartupChange = pyqtSignal() # void gotStartupChange(const KStartupInfoIdamp;,const KStartupInfoDataamp;) - signal
    gotNewStartup = pyqtSignal() # void gotNewStartup(const KStartupInfoIdamp;,const KStartupInfoDataamp;) - signal
    def handleAutoAppStartedSending(self):
        '''static void KStartupInfo.handleAutoAppStartedSending()'''
    def windowStartupId(self, w):
        '''static QByteArray KStartupInfo.windowStartupId(int w)'''
        return QByteArray()
    def setWindowStartupId(self, window, id):
        '''static void KStartupInfo.setWindowStartupId(int window, QByteArray id)'''
    def setTimeout(self, secs):
        '''void KStartupInfo.setTimeout(int secs)'''
    def checkStartup(self, w):
        '''KStartupInfo.startup_t KStartupInfo.checkStartup(int w)'''
        return KStartupInfo.startup_t()
    def checkStartup(self, w, id):
        '''KStartupInfo.startup_t KStartupInfo.checkStartup(int w, KStartupInfoId id)'''
        return KStartupInfo.startup_t()
    def checkStartup(self, w, data):
        '''KStartupInfo.startup_t KStartupInfo.checkStartup(int w, KStartupInfoData data)'''
        return KStartupInfo.startup_t()
    def checkStartup(self, w, id, data):
        '''KStartupInfo.startup_t KStartupInfo.checkStartup(int w, KStartupInfoId id, KStartupInfoData data)'''
        return KStartupInfo.startup_t()
    def resetStartupEnv(self):
        '''static void KStartupInfo.resetStartupEnv()'''
    def currentStartupIdEnv(self):
        '''static KStartupInfoId KStartupInfo.currentStartupIdEnv()'''
        return KStartupInfoId()
    def sendFinish(self, id):
        '''static bool KStartupInfo.sendFinish(KStartupInfoId id)'''
        return bool()
    def sendFinish(self, id, data):
        '''static bool KStartupInfo.sendFinish(KStartupInfoId id, KStartupInfoData data)'''
        return bool()
    def sendChange(self, id, data):
        '''static bool KStartupInfo.sendChange(KStartupInfoId id, KStartupInfoData data)'''
        return bool()
    def sendStartup(self, id, data):
        '''static bool KStartupInfo.sendStartup(KStartupInfoId id, KStartupInfoData data)'''
        return bool()
    def createNewStartupId(self):
        '''static QByteArray KStartupInfo.createNewStartupId()'''
        return QByteArray()
    def silenceStartup(self, silence):
        '''static void KStartupInfo.silenceStartup(bool silence)'''
    def setNewStartupId(self, window, startup_id):
        '''static void KStartupInfo.setNewStartupId(QWidget window, QByteArray startup_id)'''
    def appStarted(self):
        '''static void KStartupInfo.appStarted()'''
    def appStarted(self, startup_id):
        '''static void KStartupInfo.appStarted(QByteArray startup_id)'''
    def disableAutoAppStartedSending(self, disable = True):
        '''static void KStartupInfo.disableAutoAppStartedSending(bool disable = True)'''


class KStartupInfoId():
    """"""
    def __init__(self):
        '''void KStartupInfoId.__init__()'''
    def __init__(self, data):
        '''void KStartupInfoId.__init__(KStartupInfoId data)'''
    def __ge__(self, id):
        '''bool KStartupInfoId.__ge__(KStartupInfoId id)'''
        return bool()
    def __lt__(self, id):
        '''bool KStartupInfoId.__lt__(KStartupInfoId id)'''
        return bool()
    def setupStartupEnv(self):
        '''bool KStartupInfoId.setupStartupEnv()'''
        return bool()
    def timestamp(self):
        '''int KStartupInfoId.timestamp()'''
        return int()
    def id(self):
        '''QByteArray KStartupInfoId.id()'''
        return QByteArray()
    def initId(self, id = None):
        '''void KStartupInfoId.initId(QByteArray id = )'''
    def none(self):
        '''bool KStartupInfoId.none()'''
        return bool()
    def __ne__(self, id):
        '''bool KStartupInfoId.__ne__(KStartupInfoId id)'''
        return bool()
    def __eq__(self, id):
        '''bool KStartupInfoId.__eq__(KStartupInfoId id)'''
        return bool()


class KStartupInfoData():
    """"""
    # Enum KStartupInfoData.TriState
    Yes = 0
    No = 0
    Unknown = 0

    def __init__(self):
        '''void KStartupInfoData.__init__()'''
    def __init__(self, data):
        '''void KStartupInfoData.__init__(KStartupInfoData data)'''
    def setApplicationId(self, desktop):
        '''void KStartupInfoData.setApplicationId(QString desktop)'''
    def applicationId(self):
        '''QString KStartupInfoData.applicationId()'''
        return QString()
    def pids(self):
        '''list-of-int KStartupInfoData.pids()'''
        return [int()]
    def update(self, data):
        '''void KStartupInfoData.update(KStartupInfoData data)'''
    def setLaunchedBy(self, window):
        '''void KStartupInfoData.setLaunchedBy(int window)'''
    def launchedBy(self):
        '''int KStartupInfoData.launchedBy()'''
        return int()
    def setXinerama(self, xinerama):
        '''void KStartupInfoData.setXinerama(int xinerama)'''
    def xinerama(self):
        '''int KStartupInfoData.xinerama()'''
        return int()
    def setScreen(self, screen):
        '''void KStartupInfoData.setScreen(int screen)'''
    def screen(self):
        '''int KStartupInfoData.screen()'''
        return int()
    def timestamp(self):
        '''int KStartupInfoData.timestamp()'''
        return int()
    def setTimestamp(self, time):
        '''void KStartupInfoData.setTimestamp(int time)'''
    def silent(self):
        '''KStartupInfoData.TriState KStartupInfoData.silent()'''
        return KStartupInfoData.TriState()
    def setSilent(self, state):
        '''void KStartupInfoData.setSilent(KStartupInfoData.TriState state)'''
    def hostname(self):
        '''QByteArray KStartupInfoData.hostname()'''
        return QByteArray()
    def setHostname(self, hostname = QByteArray()):
        '''void KStartupInfoData.setHostname(QByteArray hostname = QByteArray())'''
    def is_pid(self, pid):
        '''bool KStartupInfoData.is_pid(int pid)'''
        return bool()
    def addPid(self, pid):
        '''void KStartupInfoData.addPid(int pid)'''
    def WMClass(self):
        '''QByteArray KStartupInfoData.WMClass()'''
        return QByteArray()
    def findWMClass(self):
        '''QByteArray KStartupInfoData.findWMClass()'''
        return QByteArray()
    def setWMClass(self, wmclass):
        '''void KStartupInfoData.setWMClass(QByteArray wmclass)'''
    def desktop(self):
        '''int KStartupInfoData.desktop()'''
        return int()
    def setDesktop(self, desktop):
        '''void KStartupInfoData.setDesktop(int desktop)'''
    def icon(self):
        '''QString KStartupInfoData.icon()'''
        return QString()
    def findIcon(self):
        '''QString KStartupInfoData.findIcon()'''
        return QString()
    def setIcon(self, icon):
        '''void KStartupInfoData.setIcon(QString icon)'''
    def description(self):
        '''QString KStartupInfoData.description()'''
        return QString()
    def findDescription(self):
        '''QString KStartupInfoData.findDescription()'''
        return QString()
    def setDescription(self, descr):
        '''void KStartupInfoData.setDescription(QString descr)'''
    def name(self):
        '''QString KStartupInfoData.name()'''
        return QString()
    def findName(self):
        '''QString KStartupInfoData.findName()'''
        return QString()
    def setName(self, name):
        '''void KStartupInfoData.setName(QString name)'''
    def bin(self):
        '''QString KStartupInfoData.bin()'''
        return QString()
    def setBin(self, bin):
        '''void KStartupInfoData.setBin(QString bin)'''


class KStatusBar(QStatusBar):
    """"""
    def __init__(self, parent = None):
        '''void KStatusBar.__init__(QWidget parent = None)'''
    def eventFilter(self, object, event):
        '''bool KStatusBar.eventFilter(QObject object, QEvent event)'''
        return bool()
    released = pyqtSignal() # void released(int) - signal
    pressed = pyqtSignal() # void pressed(int) - signal
    def setItemFixed(self, id, width = None):
        '''void KStatusBar.setItemFixed(int id, int width = -1)'''
    def setItemAlignment(self, id, alignment):
        '''void KStatusBar.setItemAlignment(int id, Qt.Alignment alignment)'''
    def changeItem(self, text, id):
        '''void KStatusBar.changeItem(QString text, int id)'''
    def itemText(self, id):
        '''QString KStatusBar.itemText(int id)'''
        return QString()
    def hasItem(self, id):
        '''bool KStatusBar.hasItem(int id)'''
        return bool()
    def removeItem(self, id):
        '''void KStatusBar.removeItem(int id)'''
    def insertPermanentFixedItem(self, text, id):
        '''void KStatusBar.insertPermanentFixedItem(QString text, int id)'''
    def insertFixedItem(self, text, id):
        '''void KStatusBar.insertFixedItem(QString text, int id)'''
    def insertPermanentItem(self, text, id, stretch = 0):
        '''void KStatusBar.insertPermanentItem(QString text, int id, int stretch = 0)'''
    def insertItem(self, text, id, stretch = 0):
        '''void KStatusBar.insertItem(QString text, int id, int stretch = 0)'''


class KStatusBarJobTracker(KAbstractWidgetJobTracker):
    """"""
    # Enum KStatusBarJobTracker.StatusBarMode
    NoInformation = 0
    LabelOnly = 0
    ProgressOnly = 0

    def __init__(self, parent = None, button = True):
        '''void KStatusBarJobTracker.__init__(QWidget parent = None, bool button = True)'''
    def slotClean(self, job):
        '''void KStatusBarJobTracker.slotClean(KJob job)'''
    def speed(self, job, value):
        '''void KStatusBarJobTracker.speed(KJob job, int value)'''
    def percent(self, job, percent):
        '''void KStatusBarJobTracker.percent(KJob job, int percent)'''
    def totalAmount(self, job, unit, amount):
        '''void KStatusBarJobTracker.totalAmount(KJob job, KJob.Unit unit, int amount)'''
    def description(self, job, title, field1, field2):
        '''void KStatusBarJobTracker.description(KJob job, QString title, unknown-type field1, unknown-type field2)'''
    def setStatusBarMode(self, statusBarMode):
        '''void KStatusBarJobTracker.setStatusBarMode(KStatusBarJobTracker.StatusBarModes statusBarMode)'''
    def widget(self, job):
        '''QWidget KStatusBarJobTracker.widget(KJob job)'''
        return QWidget()
    def unregisterJob(self, job):
        '''void KStatusBarJobTracker.unregisterJob(KJob job)'''
    def registerJob(self, job):
        '''void KStatusBarJobTracker.registerJob(KJob job)'''
    class StatusBarModes():
        """"""
        def __init__(self):
            '''KStatusBarJobTracker.StatusBarModes KStatusBarJobTracker.StatusBarModes.__init__()'''
            return KStatusBarJobTracker.StatusBarModes()
        def __init__(self):
            '''int KStatusBarJobTracker.StatusBarModes.__init__()'''
            return int()
        def __init__(self):
            '''void KStatusBarJobTracker.StatusBarModes.__init__()'''
        def __bool__(self):
            '''int KStatusBarJobTracker.StatusBarModes.__bool__()'''
            return int()
        def __ne__(self, f):
            '''bool KStatusBarJobTracker.StatusBarModes.__ne__(KStatusBarJobTracker.StatusBarModes f)'''
            return bool()
        def __eq__(self, f):
            '''bool KStatusBarJobTracker.StatusBarModes.__eq__(KStatusBarJobTracker.StatusBarModes f)'''
            return bool()
        def __invert__(self):
            '''KStatusBarJobTracker.StatusBarModes KStatusBarJobTracker.StatusBarModes.__invert__()'''
            return KStatusBarJobTracker.StatusBarModes()
        def __and__(self, mask):
            '''KStatusBarJobTracker.StatusBarModes KStatusBarJobTracker.StatusBarModes.__and__(int mask)'''
            return KStatusBarJobTracker.StatusBarModes()
        def __xor__(self, f):
            '''KStatusBarJobTracker.StatusBarModes KStatusBarJobTracker.StatusBarModes.__xor__(KStatusBarJobTracker.StatusBarModes f)'''
            return KStatusBarJobTracker.StatusBarModes()
        def __xor__(self, f):
            '''KStatusBarJobTracker.StatusBarModes KStatusBarJobTracker.StatusBarModes.__xor__(int f)'''
            return KStatusBarJobTracker.StatusBarModes()
        def __or__(self, f):
            '''KStatusBarJobTracker.StatusBarModes KStatusBarJobTracker.StatusBarModes.__or__(KStatusBarJobTracker.StatusBarModes f)'''
            return KStatusBarJobTracker.StatusBarModes()
        def __or__(self, f):
            '''KStatusBarJobTracker.StatusBarModes KStatusBarJobTracker.StatusBarModes.__or__(int f)'''
            return KStatusBarJobTracker.StatusBarModes()
        def __int__(self):
            '''int KStatusBarJobTracker.StatusBarModes.__int__()'''
            return int()
        def __ixor__(self, f):
            '''KStatusBarJobTracker.StatusBarModes KStatusBarJobTracker.StatusBarModes.__ixor__(KStatusBarJobTracker.StatusBarModes f)'''
            return KStatusBarJobTracker.StatusBarModes()
        def __ior__(self, f):
            '''KStatusBarJobTracker.StatusBarModes KStatusBarJobTracker.StatusBarModes.__ior__(KStatusBarJobTracker.StatusBarModes f)'''
            return KStatusBarJobTracker.StatusBarModes()
        def __iand__(self, mask):
            '''KStatusBarJobTracker.StatusBarModes KStatusBarJobTracker.StatusBarModes.__iand__(int mask)'''
            return KStatusBarJobTracker.StatusBarModes()


class KStatusNotifierItem(QObject):
    """"""
    # Enum KStatusNotifierItem.ItemCategory
    ApplicationStatus = 0
    Communications = 0
    SystemServices = 0
    Hardware = 0
    Reserved = 0

    # Enum KStatusNotifierItem.ItemStatus
    Passive = 0
    Active = 0
    NeedsAttention = 0

    def __init__(self, parent = None):
        '''void KStatusNotifierItem.__init__(QObject parent = None)'''
    def __init__(self, id, parent = None):
        '''void KStatusNotifierItem.__init__(QString id, QObject parent = None)'''
    def attentionMovieName(self):
        '''QString KStatusNotifierItem.attentionMovieName()'''
        return QString()
    def setAttentionMovieByName(self, name):
        '''void KStatusNotifierItem.setAttentionMovieByName(QString name)'''
    def eventFilter(self, watched, event):
        '''bool KStatusNotifierItem.eventFilter(QObject watched, QEvent event)'''
        return bool()
    secondaryActivateRequested = pyqtSignal() # void secondaryActivateRequested(const QPointamp;) - signal
    activateRequested = pyqtSignal() # void activateRequested(bool,const QPointamp;) - signal
    scrollRequested = pyqtSignal() # void scrollRequested(int,Qt::Orientation) - signal
    def activate(self, pos = QPoint()):
        '''void KStatusNotifierItem.activate(QPoint pos = QPoint())'''
    def showMessage(self, title, message, icon, timeout = 10000):
        '''void KStatusNotifierItem.showMessage(QString title, QString message, QString icon, int timeout = 10000)'''
    def standardActionsEnabled(self):
        '''bool KStatusNotifierItem.standardActionsEnabled()'''
        return bool()
    def setStandardActionsEnabled(self, enabled):
        '''void KStatusNotifierItem.setStandardActionsEnabled(bool enabled)'''
    def actionCollection(self):
        '''KActionCollection KStatusNotifierItem.actionCollection()'''
        return KActionCollection()
    def associatedWidget(self):
        '''QWidget KStatusNotifierItem.associatedWidget()'''
        return QWidget()
    def setAssociatedWidget(self, parent):
        '''void KStatusNotifierItem.setAssociatedWidget(QWidget parent)'''
    def contextMenu(self):
        '''KMenu KStatusNotifierItem.contextMenu()'''
        return KMenu()
    def setContextMenu(self, menu):
        '''void KStatusNotifierItem.setContextMenu(KMenu menu)'''
    def toolTipSubTitle(self):
        '''QString KStatusNotifierItem.toolTipSubTitle()'''
        return QString()
    def setToolTipSubTitle(self, subTitle):
        '''void KStatusNotifierItem.setToolTipSubTitle(QString subTitle)'''
    def toolTipTitle(self):
        '''QString KStatusNotifierItem.toolTipTitle()'''
        return QString()
    def setToolTipTitle(self, title):
        '''void KStatusNotifierItem.setToolTipTitle(QString title)'''
    def toolTipIconPixmap(self):
        '''QIcon KStatusNotifierItem.toolTipIconPixmap()'''
        return QIcon()
    def setToolTipIconByPixmap(self, icon):
        '''void KStatusNotifierItem.setToolTipIconByPixmap(QIcon icon)'''
    def toolTipIconName(self):
        '''QString KStatusNotifierItem.toolTipIconName()'''
        return QString()
    def setToolTipIconByName(self, name):
        '''void KStatusNotifierItem.setToolTipIconByName(QString name)'''
    def setToolTip(self, iconName, title, subTitle):
        '''void KStatusNotifierItem.setToolTip(QString iconName, QString title, QString subTitle)'''
    def setToolTip(self, icon, title, subTitle):
        '''void KStatusNotifierItem.setToolTip(QIcon icon, QString title, QString subTitle)'''
    def attentionIconPixmap(self):
        '''QIcon KStatusNotifierItem.attentionIconPixmap()'''
        return QIcon()
    def setAttentionIconByPixmap(self, icon):
        '''void KStatusNotifierItem.setAttentionIconByPixmap(QIcon icon)'''
    def attentionIconName(self):
        '''QString KStatusNotifierItem.attentionIconName()'''
        return QString()
    def setAttentionIconByName(self, name):
        '''void KStatusNotifierItem.setAttentionIconByName(QString name)'''
    def overlayIconPixmap(self):
        '''QIcon KStatusNotifierItem.overlayIconPixmap()'''
        return QIcon()
    def setOverlayIconByPixmap(self, icon):
        '''void KStatusNotifierItem.setOverlayIconByPixmap(QIcon icon)'''
    def overlayIconName(self):
        '''QString KStatusNotifierItem.overlayIconName()'''
        return QString()
    def setOverlayIconByName(self, name):
        '''void KStatusNotifierItem.setOverlayIconByName(QString name)'''
    def iconPixmap(self):
        '''QIcon KStatusNotifierItem.iconPixmap()'''
        return QIcon()
    def setIconByPixmap(self, icon):
        '''void KStatusNotifierItem.setIconByPixmap(QIcon icon)'''
    def iconName(self):
        '''QString KStatusNotifierItem.iconName()'''
        return QString()
    def setIconByName(self, name):
        '''void KStatusNotifierItem.setIconByName(QString name)'''
    def status(self):
        '''KStatusNotifierItem.ItemStatus KStatusNotifierItem.status()'''
        return KStatusNotifierItem.ItemStatus()
    def setStatus(self, status):
        '''void KStatusNotifierItem.setStatus(KStatusNotifierItem.ItemStatus status)'''
    def title(self):
        '''QString KStatusNotifierItem.title()'''
        return QString()
    def setTitle(self, title):
        '''void KStatusNotifierItem.setTitle(QString title)'''
    def category(self):
        '''KStatusNotifierItem.ItemCategory KStatusNotifierItem.category()'''
        return KStatusNotifierItem.ItemCategory()
    def setCategory(self, category):
        '''void KStatusNotifierItem.setCategory(KStatusNotifierItem.ItemCategory category)'''
    def id(self):
        '''QString KStatusNotifierItem.id()'''
        return QString()


class KStringListValidator(QValidator):
    """"""
    def __init__(self, list = QStringList(), rejecting = True, fixupEnabled = False, parent = None):
        '''void KStringListValidator.__init__(QStringList list = QStringList(), bool rejecting = True, bool fixupEnabled = False, QObject parent = None)'''
    def fixup(self, input):
        '''void KStringListValidator.fixup(QString input)'''
    def validate(self, input, pos):
        '''QValidator.State KStringListValidator.validate(QString input, int pos)'''
        return QValidator.State()
    def stringList(self):
        '''QStringList KStringListValidator.stringList()'''
        return QStringList()
    def setStringList(self, list):
        '''void KStringListValidator.setStringList(QStringList list)'''
    def isFixupEnabled(self):
        '''bool KStringListValidator.isFixupEnabled()'''
        return bool()
    def setFixupEnabled(self, fixupEnabled):
        '''void KStringListValidator.setFixupEnabled(bool fixupEnabled)'''
    def isRejecting(self):
        '''bool KStringListValidator.isRejecting()'''
        return bool()
    def setRejecting(self, rejecting):
        '''void KStringListValidator.setRejecting(bool rejecting)'''


class KMimeTypeValidator(QValidator):
    """"""
    def __init__(self, parent = None):
        '''void KMimeTypeValidator.__init__(QObject parent = None)'''
    def fixup(self, input):
        '''void KMimeTypeValidator.fixup(QString input)'''
    def validate(self, input, pos):
        '''QValidator.State KMimeTypeValidator.validate(QString input, int pos)'''
        return QValidator.State()


class KStyle(QStyle):
    """"""
    # Enum KStyle.MarginOffsets
    MainMargin = 0
    Top = 0
    Bot = 0
    Left = 0
    Right = 0
    MarginInc = 0

    # Enum KStyle.WidgetType
    WT_Generic = 0
    WT_PushButton = 0
    WT_Splitter = 0
    WT_CheckBox = 0
    WT_RadioButton = 0
    WT_DockWidget = 0
    WT_ProgressBar = 0
    WT_MenuBar = 0
    WT_MenuBarItem = 0
    WT_Menu = 0
    WT_MenuItem = 0
    WT_ScrollBar = 0
    WT_TabBar = 0
    WT_TabWidget = 0
    WT_Slider = 0
    WT_Tree = 0
    WT_SpinBox = 0
    WT_ComboBox = 0
    WT_Header = 0
    WT_LineEdit = 0
    WT_GroupBox = 0
    WT_StatusBar = 0
    WT_ToolBar = 0
    WT_ToolButton = 0
    WT_ToolBoxTab = 0
    WT_Window = 0
    WT_Limit = 0

    def __init__(self):
        '''void KStyle.__init__()'''
    def standardIconImplementation(self, standardIcon, option = None, widget = None):
        '''QIcon KStyle.standardIconImplementation(QStyle.StandardPixmap standardIcon, QStyleOption option = None, QWidget widget = None)'''
        return QIcon()
    def standardPixmap(self, standardPixmap, opt, widget = None):
        '''QPixmap KStyle.standardPixmap(QStyle.StandardPixmap standardPixmap, QStyleOption opt, QWidget widget = None)'''
        return QPixmap()
    def drawComplexControl(self, cc, opt, p, w):
        '''void KStyle.drawComplexControl(QStyle.ComplexControl cc, QStyleOptionComplex opt, QPainter p, QWidget w)'''
    def hitTestComplexControl(self, cc, opt, pt, w):
        '''QStyle.SubControl KStyle.hitTestComplexControl(QStyle.ComplexControl cc, QStyleOptionComplex opt, QPoint pt, QWidget w)'''
        return QStyle.SubControl()
    def subControlRect(self, control, opt, subControl, w):
        '''QRect KStyle.subControlRect(QStyle.ComplexControl control, QStyleOptionComplex opt, QStyle.SubControl subControl, QWidget w)'''
        return QRect()
    def styleHint(self, hint, opt, w, returnData):
        '''int KStyle.styleHint(QStyle.StyleHint hint, QStyleOption opt, QWidget w, QStyleHintReturn returnData)'''
        return int()
    def sizeFromContents(self, type, opt, contentsSize, w):
        '''QSize KStyle.sizeFromContents(QStyle.ContentsType type, QStyleOption opt, QSize contentsSize, QWidget w)'''
        return QSize()
    def subElementRect(self, subRect, opt, w):
        '''QRect KStyle.subElementRect(QStyle.SubElement subRect, QStyleOption opt, QWidget w)'''
        return QRect()
    def pixelMetric(self, metric, opt = None, w = None):
        '''int KStyle.pixelMetric(QStyle.PixelMetric metric, QStyleOption opt = None, QWidget w = None)'''
        return int()
    def drawPrimitive(self, elem, opt, p, w):
        '''void KStyle.drawPrimitive(QStyle.PrimitiveElement elem, QStyleOption opt, QPainter p, QWidget w)'''
    def drawControl(self, elem, opt, p, w):
        '''void KStyle.drawControl(QStyle.ControlElement elem, QStyleOption opt, QPainter p, QWidget w)'''
    def layoutSpacingImplementation(self, control1, control2, orientation, option, widget):
        '''int KStyle.layoutSpacingImplementation(QSizePolicy.ControlType control1, QSizePolicy.ControlType control2, Qt.Orientation orientation, QStyleOption option, QWidget widget)'''
        return int()
    def eventFilter(self):
        '''QEvent KStyle.eventFilter()'''
        return QEvent()
    def generatedIconPixmap(self, iconMode, pixmap, opt):
        '''QPixmap KStyle.generatedIconPixmap(QIcon.Mode iconMode, QPixmap pixmap, QStyleOption opt)'''
        return QPixmap()
    def standardPalette(self):
        '''QPalette KStyle.standardPalette()'''
        return QPalette()
    def drawItemPixmap(self, painter, rect, alignment, pixmap):
        '''void KStyle.drawItemPixmap(QPainter painter, QRect rect, int alignment, QPixmap pixmap)'''
    def drawItemText(self, painter, rect, flags, pal, enabled, text, textRole = None):
        '''void KStyle.drawItemText(QPainter painter, QRect rect, int flags, QPalette pal, bool enabled, QString text, QPalette.ColorRole textRole = QPalette.NoRole)'''
    def itemPixmapRect(self, r, flags, pixmap):
        '''QRect KStyle.itemPixmapRect(QRect r, int flags, QPixmap pixmap)'''
        return QRect()
    def itemTextRect(self, fm, r, flags, enabled, text):
        '''QRect KStyle.itemTextRect(QFontMetrics fm, QRect r, int flags, bool enabled, QString text)'''
        return QRect()
    def unpolish(self):
        '''QWidget KStyle.unpolish()'''
        return QWidget()
    def unpolish(self):
        '''QApplication KStyle.unpolish()'''
        return QApplication()
    def polish(self):
        '''QWidget KStyle.polish()'''
        return QWidget()
    def polish(self):
        '''QApplication KStyle.polish()'''
        return QApplication()
    def polish(self):
        '''QPalette KStyle.polish()'''
        return QPalette()
    def widgetLayoutProp(self, widgetType, metric, opt = None, w = None):
        '''int KStyle.widgetLayoutProp(KStyle.WidgetType widgetType, int metric, QStyleOption opt = None, QWidget w = None)'''
        return int()
    def setWidgetLayoutProp(self, widget, metric, value):
        '''void KStyle.setWidgetLayoutProp(KStyle.WidgetType widget, int metric, int value)'''
    def centerRect(self, in_, w, h):
        '''QRect KStyle.centerRect(QRect in, int w, int h)'''
        return QRect()
    def centerRect(self, in_, size):
        '''QRect KStyle.centerRect(QRect in, QSize size)'''
        return QRect()
    def drawInsideRect(self, p, r):
        '''void KStyle.drawInsideRect(QPainter p, QRect r)'''
    def newSubElement(self, element):
        '''QStyle.SubElement KStyle.newSubElement(QString element)'''
        return QStyle.SubElement()
    def newControlElement(self, element):
        '''QStyle.ControlElement KStyle.newControlElement(QString element)'''
        return QStyle.ControlElement()
    def newStyleHint(self, element):
        '''QStyle.StyleHint KStyle.newStyleHint(QString element)'''
        return QStyle.StyleHint()
    def customSubElement(self, element, widget):
        '''static QStyle.SubElement KStyle.customSubElement(QString element, QWidget widget)'''
        return QStyle.SubElement()
    def customControlElement(self, element, widget):
        '''static QStyle.ControlElement KStyle.customControlElement(QString element, QWidget widget)'''
        return QStyle.ControlElement()
    def customStyleHint(self, element, widget):
        '''static QStyle.StyleHint KStyle.customStyleHint(QString element, QWidget widget)'''
        return QStyle.StyleHint()
    def defaultStyle(self):
        '''static QString KStyle.defaultStyle()'''
        return QString()


class KSvgRenderer(QSvgRenderer):
    """"""
    def __init__(self, parent = None):
        '''void KSvgRenderer.__init__(QObject parent = None)'''
    def __init__(self, filename, parent = None):
        '''void KSvgRenderer.__init__(QString filename, QObject parent = None)'''
    def __init__(self, contents, parent = None):
        '''void KSvgRenderer.__init__(QByteArray contents, QObject parent = None)'''
    def load(self, filename):
        '''bool KSvgRenderer.load(QString filename)'''
        return bool()
    def load(self, contents):
        '''bool KSvgRenderer.load(QByteArray contents)'''
        return bool()


class KSystemEventFilter():
    """"""
    def removeEventFilter(self, filter):
        '''static void KSystemEventFilter.removeEventFilter(QWidget filter)'''
    def installEventFilter(self, filter):
        '''static void KSystemEventFilter.installEventFilter(QWidget filter)'''


class KSystemTrayIcon(QSystemTrayIcon):
    """"""
    def __init__(self, parent = None):
        '''void KSystemTrayIcon.__init__(QWidget parent = None)'''
    def __init__(self, icon, parent = None):
        '''void KSystemTrayIcon.__init__(QString icon, QWidget parent = None)'''
    def __init__(self, icon, parent = None):
        '''void KSystemTrayIcon.__init__(QIcon icon, QWidget parent = None)'''
    def __init__(self, movie, parent):
        '''void KSystemTrayIcon.__init__(QMovie movie, QWidget parent)'''
    def toggleActive(self):
        '''void KSystemTrayIcon.toggleActive()'''
    quitSelected = pyqtSignal() # void quitSelected() - signal
    def contextMenuTitle(self):
        '''QAction KSystemTrayIcon.contextMenuTitle()'''
        return QAction()
    def setContextMenuTitle(self, action):
        '''void KSystemTrayIcon.setContextMenuTitle(QAction action)'''
    def loadIcon(self, icon, componentData = None):
        '''static QIcon KSystemTrayIcon.loadIcon(QString icon, KComponentData componentData = KGlobal.mainComponent())'''
        return QIcon()
    def parentWidgetTrayClose(self):
        '''bool KSystemTrayIcon.parentWidgetTrayClose()'''
        return bool()
    def parentWidget(self):
        '''QWidget KSystemTrayIcon.parentWidget()'''
        return QWidget()
    def actionCollection(self):
        '''KActionCollection KSystemTrayIcon.actionCollection()'''
        return KActionCollection()
    def movie(self):
        '''QMovie KSystemTrayIcon.movie()'''
        return QMovie()
    def setMovie(self, movie):
        '''void KSystemTrayIcon.setMovie(QMovie movie)'''


class KTabBar(QTabBar):
    """"""
    def __init__(self, parent = None):
        '''void KTabBar.__init__(QWidget parent = None)'''
    def tabLayoutChange(self):
        '''void KTabBar.tabLayoutChange()'''
    def activateDragSwitchTab(self):
        '''void KTabBar.activateDragSwitchTab()'''
    def enableCloseButton(self):
        '''void KTabBar.enableCloseButton()'''
    def closeButtonClicked(self):
        '''void KTabBar.closeButtonClicked()'''
    def tabSizeHint(self, index):
        '''QSize KTabBar.tabSizeHint(int index)'''
        return QSize()
    def leaveEvent(self, event):
        '''void KTabBar.leaveEvent(QEvent event)'''
    def paintEvent(self, event):
        '''void KTabBar.paintEvent(QPaintEvent event)'''
    def dropEvent(self, event):
        '''void KTabBar.dropEvent(QDropEvent event)'''
    def dragMoveEvent(self, event):
        '''void KTabBar.dragMoveEvent(QDragMoveEvent event)'''
    def dragEnterEvent(self, event):
        '''void KTabBar.dragEnterEvent(QDragEnterEvent event)'''
    def wheelEvent(self, event):
        '''void KTabBar.wheelEvent(QWheelEvent event)'''
    def mouseReleaseEvent(self, event):
        '''void KTabBar.mouseReleaseEvent(QMouseEvent event)'''
    def mouseMoveEvent(self, event):
        '''void KTabBar.mouseMoveEvent(QMouseEvent event)'''
    def mousePressEvent(self, event):
        '''void KTabBar.mousePressEvent(QMouseEvent event)'''
    def mouseDoubleClickEvent(self, event):
        '''void KTabBar.mouseDoubleClickEvent(QMouseEvent event)'''
    wheelDelta = pyqtSignal() # void wheelDelta(int) - signal
    closeRequest = pyqtSignal() # void closeRequest(int) - signal
    moveTab = pyqtSignal() # void moveTab(int,int) - signal
    receivedDropEvent = pyqtSignal() # void receivedDropEvent(int,QDropEvent *) - signal
    initiateDrag = pyqtSignal() # void initiateDrag(int) - signal
    mouseMiddleClick = pyqtSignal() # void mouseMiddleClick(int) - signal
    newTabRequest = pyqtSignal() # void newTabRequest() - signal
    tabDoubleClicked = pyqtSignal() # void tabDoubleClicked(int) - signal
    mouseDoubleClick = pyqtSignal() # void mouseDoubleClick(int) - signal
    emptyAreaContextMenu = pyqtSignal() # void emptyAreaContextMenu(const QPointamp;) - signal
    contextMenu = pyqtSignal() # void contextMenu(int,const QPointamp;) - signal
    def selectTab(self, position):
        '''int KTabBar.selectTab(QPoint position)'''
        return int()
    def tabCloseActivatePrevious(self):
        '''bool KTabBar.tabCloseActivatePrevious()'''
        return bool()
    def setTabCloseActivatePrevious(self):
        '''bool KTabBar.setTabCloseActivatePrevious()'''
        return bool()
    def isCloseButtonEnabled(self):
        '''bool KTabBar.isCloseButtonEnabled()'''
        return bool()
    def setCloseButtonEnabled(self):
        '''bool KTabBar.setCloseButtonEnabled()'''
        return bool()
    def hoverCloseButtonDelayed(self):
        '''bool KTabBar.hoverCloseButtonDelayed()'''
        return bool()
    def setHoverCloseButtonDelayed(self):
        '''bool KTabBar.setHoverCloseButtonDelayed()'''
        return bool()
    def hoverCloseButton(self):
        '''bool KTabBar.hoverCloseButton()'''
        return bool()
    def setHoverCloseButton(self):
        '''bool KTabBar.setHoverCloseButton()'''
        return bool()
    def isTabReorderingEnabled(self):
        '''bool KTabBar.isTabReorderingEnabled()'''
        return bool()
    def setTabReorderingEnabled(self, enable):
        '''void KTabBar.setTabReorderingEnabled(bool enable)'''


class KTabWidget(QTabWidget):
    """"""
    def __init__(self, parent = None, flags = 0):
        '''void KTabWidget.__init__(QWidget parent = None, Qt.WindowFlags flags = 0)'''
    def mouseReleaseEvent(self):
        '''QMouseEvent KTabWidget.mouseReleaseEvent()'''
        return QMouseEvent()
    def wheelDelta(self):
        '''int KTabWidget.wheelDelta()'''
        return int()
    def currentChanged(self):
        '''int KTabWidget.currentChanged()'''
        return int()
    def tabRemoved(self):
        '''int KTabWidget.tabRemoved()'''
        return int()
    def tabInserted(self):
        '''int KTabWidget.tabInserted()'''
        return int()
    def resizeEvent(self):
        '''QResizeEvent KTabWidget.resizeEvent()'''
        return QResizeEvent()
    def wheelEvent(self):
        '''QWheelEvent KTabWidget.wheelEvent()'''
        return QWheelEvent()
    def tabBarWidthForMaxChars(self):
        '''int KTabWidget.tabBarWidthForMaxChars()'''
        return int()
    def dropEvent(self):
        '''QDropEvent KTabWidget.dropEvent()'''
        return QDropEvent()
    def dragMoveEvent(self):
        '''QDragMoveEvent KTabWidget.dragMoveEvent()'''
        return QDragMoveEvent()
    def dragEnterEvent(self):
        '''QDragEnterEvent KTabWidget.dragEnterEvent()'''
        return QDragEnterEvent()
    def mousePressEvent(self):
        '''QMouseEvent KTabWidget.mousePressEvent()'''
        return QMouseEvent()
    def mouseDoubleClickEvent(self):
        '''QMouseEvent KTabWidget.mouseDoubleClickEvent()'''
        return QMouseEvent()
    closeRequest = pyqtSignal() # void closeRequest(QWidget *) - signal
    mouseMiddleClick = pyqtSignal() # void mouseMiddleClick() - signal
    mouseMiddleClick = pyqtSignal() # void mouseMiddleClick(QWidget *) - signal
    mouseDoubleClick = pyqtSignal() # void mouseDoubleClick() - signal
    mouseDoubleClick = pyqtSignal() # void mouseDoubleClick(QWidget *) - signal
    movedTab = pyqtSignal() # void movedTab(int,int) - signal
    contextMenu = pyqtSignal() # void contextMenu(QWidget *,const QPointamp;) - signal
    initiateDrag = pyqtSignal() # void initiateDrag(QWidget *) - signal
    receivedDropEvent = pyqtSignal() # void receivedDropEvent(QDropEvent *) - signal
    receivedDropEvent = pyqtSignal() # void receivedDropEvent(QWidget *,QDropEvent *) - signal
    def setAutomaticResizeTabs(self, enable):
        '''void KTabWidget.setAutomaticResizeTabs(bool enable)'''
    def setTabCloseActivatePrevious(self, previous):
        '''void KTabWidget.setTabCloseActivatePrevious(bool previous)'''
    def setCloseButtonEnabled(self):
        '''bool KTabWidget.setCloseButtonEnabled()'''
        return bool()
    def setHoverCloseButtonDelayed(self, delayed):
        '''void KTabWidget.setHoverCloseButtonDelayed(bool delayed)'''
    def setHoverCloseButton(self, enable):
        '''void KTabWidget.setHoverCloseButton(bool enable)'''
    def setTabReorderingEnabled(self, enable):
        '''void KTabWidget.setTabReorderingEnabled(bool enable)'''
    def removeTab(self, index):
        '''void KTabWidget.removeTab(int index)'''
    def removePage(self, w):
        '''void KTabWidget.removePage(QWidget w)'''
    def moveTab(self):
        '''int KTabWidget.moveTab()'''
        return int()
    def setTabText(self):
        '''QString KTabWidget.setTabText()'''
        return QString()
    def tabText(self):
        '''int KTabWidget.tabText()'''
        return int()
    def isTabBarHidden(self):
        '''bool KTabWidget.isTabBarHidden()'''
        return bool()
    def setTabBarHidden(self, hide):
        '''void KTabWidget.setTabBarHidden(bool hide)'''
    def automaticResizeTabs(self):
        '''bool KTabWidget.automaticResizeTabs()'''
        return bool()
    def tabCloseActivatePrevious(self):
        '''bool KTabWidget.tabCloseActivatePrevious()'''
        return bool()
    def isCloseButtonEnabled(self):
        '''bool KTabWidget.isCloseButtonEnabled()'''
        return bool()
    def hoverCloseButtonDelayed(self):
        '''bool KTabWidget.hoverCloseButtonDelayed()'''
        return bool()
    def hoverCloseButton(self):
        '''bool KTabWidget.hoverCloseButton()'''
        return bool()
    def isTabReorderingEnabled(self):
        '''bool KTabWidget.isTabReorderingEnabled()'''
        return bool()
    def tabTextColor(self, index):
        '''QColor KTabWidget.tabTextColor(int index)'''
        return QColor()
    def setTabTextColor(self, index, color):
        '''void KTabWidget.setTabTextColor(int index, QColor color)'''


class KTextBrowser(QTextBrowser):
    """"""
    def __init__(self, parent = None, notifyClick = False):
        '''void KTextBrowser.__init__(QWidget parent = None, bool notifyClick = False)'''
    urlClick = pyqtSignal() # void urlClick(const QStringamp;) - signal
    mailClick = pyqtSignal() # void mailClick(const QStringamp;,const QStringamp;) - signal
    def contextMenuEvent(self, event):
        '''void KTextBrowser.contextMenuEvent(QContextMenuEvent event)'''
    def wheelEvent(self, event):
        '''void KTextBrowser.wheelEvent(QWheelEvent event)'''
    def keyPressEvent(self, event):
        '''void KTextBrowser.keyPressEvent(QKeyEvent event)'''
    def setSource(self, name):
        '''void KTextBrowser.setSource(QUrl name)'''
    def isNotifyClick(self):
        '''bool KTextBrowser.isNotifyClick()'''
        return bool()
    def setNotifyClick(self, notifyClick):
        '''void KTextBrowser.setNotifyClick(bool notifyClick)'''


class KTextEditSpellInterface():
    """"""
    def __init__(self):
        '''void KTextEditSpellInterface.__init__()'''
    def __init__(self):
        '''KTextEditSpellInterface KTextEditSpellInterface.__init__()'''
        return KTextEditSpellInterface()
    def shouldBlockBeSpellChecked(self, block):
        '''abstract bool KTextEditSpellInterface.shouldBlockBeSpellChecked(QString block)'''
        return bool()
    def setSpellCheckingEnabled(self, enable):
        '''abstract void KTextEditSpellInterface.setSpellCheckingEnabled(bool enable)'''
    def isSpellCheckingEnabled(self):
        '''abstract bool KTextEditSpellInterface.isSpellCheckingEnabled()'''
        return bool()


class KTimeComboBox(KComboBox):
    """"""
    # Enum KTimeComboBox.Option
    EditTime = 0
    SelectTime = 0
    ForceTime = 0
    WarnOnInvalid = 0

    def __init__(self, parent = None):
        '''void KTimeComboBox.__init__(QWidget parent = None)'''
    def displayFormat(self):
        '''KLocale.TimeFormatOptions KTimeComboBox.displayFormat()'''
        return KLocale.TimeFormatOptions()
    def isNull(self):
        '''bool KTimeComboBox.isNull()'''
        return bool()
    def setTimeList(self, timeList, minWarnMsg = QString(), maxWarnMsg = QString()):
        '''void KTimeComboBox.setTimeList(list-of-QTime timeList, QString minWarnMsg = QString(), QString maxWarnMsg = QString())'''
    def setTimeListInterval(self, minutes):
        '''void KTimeComboBox.setTimeListInterval(int minutes)'''
    def setMaximumTime(self, maxTime, maxWarnMsg = QString()):
        '''void KTimeComboBox.setMaximumTime(QTime maxTime, QString maxWarnMsg = QString())'''
    def setMinimumTime(self, minTime, minWarnMsg = QString()):
        '''void KTimeComboBox.setMinimumTime(QTime minTime, QString minWarnMsg = QString())'''
    def timeList(self):
        '''list-of-QTime KTimeComboBox.timeList()'''
        return [QTime()]
    def timeListInterval(self):
        '''int KTimeComboBox.timeListInterval()'''
        return int()
    def assignTime(self, time):
        '''void KTimeComboBox.assignTime(QTime time)'''
    def resizeEvent(self, event):
        '''void KTimeComboBox.resizeEvent(QResizeEvent event)'''
    def focusOutEvent(self, event):
        '''void KTimeComboBox.focusOutEvent(QFocusEvent event)'''
    def focusInEvent(self, event):
        '''void KTimeComboBox.focusInEvent(QFocusEvent event)'''
    def keyPressEvent(self, event):
        '''void KTimeComboBox.keyPressEvent(QKeyEvent event)'''
    def wheelEvent(self, event):
        '''void KTimeComboBox.wheelEvent(QWheelEvent event)'''
    def mousePressEvent(self, event):
        '''void KTimeComboBox.mousePressEvent(QMouseEvent event)'''
    def hidePopup(self):
        '''void KTimeComboBox.hidePopup()'''
    def showPopup(self):
        '''void KTimeComboBox.showPopup()'''
    def eventFilter(self, object, event):
        '''bool KTimeComboBox.eventFilter(QObject object, QEvent event)'''
        return bool()
    def setDisplayFormat(self, formatOptions):
        '''void KTimeComboBox.setDisplayFormat(KLocale.TimeFormatOptions formatOptions)'''
    def setOptions(self, options):
        '''void KTimeComboBox.setOptions(KTimeComboBox.Options options)'''
    def setTime(self, time):
        '''void KTimeComboBox.setTime(QTime time)'''
    timeEdited = pyqtSignal() # void timeEdited(const QTimeamp;) - signal
    timeChanged = pyqtSignal() # void timeChanged(const QTimeamp;) - signal
    timeEntered = pyqtSignal() # void timeEntered(const QTimeamp;) - signal
    def resetTimeRange(self):
        '''void KTimeComboBox.resetTimeRange()'''
    def setTimeRange(self, minTime, maxTime, minWarnMsg = QString(), maxWarnMsg = QString()):
        '''void KTimeComboBox.setTimeRange(QTime minTime, QTime maxTime, QString minWarnMsg = QString(), QString maxWarnMsg = QString())'''
    def resetMaximumTime(self):
        '''void KTimeComboBox.resetMaximumTime()'''
    def maximumTime(self):
        '''QTime KTimeComboBox.maximumTime()'''
        return QTime()
    def resetMinimumTime(self):
        '''void KTimeComboBox.resetMinimumTime()'''
    def minimumTime(self):
        '''QTime KTimeComboBox.minimumTime()'''
        return QTime()
    def options(self):
        '''KTimeComboBox.Options KTimeComboBox.options()'''
        return KTimeComboBox.Options()
    def isValid(self):
        '''bool KTimeComboBox.isValid()'''
        return bool()
    def time(self):
        '''QTime KTimeComboBox.time()'''
        return QTime()
    class Options():
        """"""
        def __init__(self):
            '''KTimeComboBox.Options KTimeComboBox.Options.__init__()'''
            return KTimeComboBox.Options()
        def __init__(self):
            '''int KTimeComboBox.Options.__init__()'''
            return int()
        def __init__(self):
            '''void KTimeComboBox.Options.__init__()'''
        def __bool__(self):
            '''int KTimeComboBox.Options.__bool__()'''
            return int()
        def __ne__(self, f):
            '''bool KTimeComboBox.Options.__ne__(KTimeComboBox.Options f)'''
            return bool()
        def __eq__(self, f):
            '''bool KTimeComboBox.Options.__eq__(KTimeComboBox.Options f)'''
            return bool()
        def __invert__(self):
            '''KTimeComboBox.Options KTimeComboBox.Options.__invert__()'''
            return KTimeComboBox.Options()
        def __and__(self, mask):
            '''KTimeComboBox.Options KTimeComboBox.Options.__and__(int mask)'''
            return KTimeComboBox.Options()
        def __xor__(self, f):
            '''KTimeComboBox.Options KTimeComboBox.Options.__xor__(KTimeComboBox.Options f)'''
            return KTimeComboBox.Options()
        def __xor__(self, f):
            '''KTimeComboBox.Options KTimeComboBox.Options.__xor__(int f)'''
            return KTimeComboBox.Options()
        def __or__(self, f):
            '''KTimeComboBox.Options KTimeComboBox.Options.__or__(KTimeComboBox.Options f)'''
            return KTimeComboBox.Options()
        def __or__(self, f):
            '''KTimeComboBox.Options KTimeComboBox.Options.__or__(int f)'''
            return KTimeComboBox.Options()
        def __int__(self):
            '''int KTimeComboBox.Options.__int__()'''
            return int()
        def __ixor__(self, f):
            '''KTimeComboBox.Options KTimeComboBox.Options.__ixor__(KTimeComboBox.Options f)'''
            return KTimeComboBox.Options()
        def __ior__(self, f):
            '''KTimeComboBox.Options KTimeComboBox.Options.__ior__(KTimeComboBox.Options f)'''
            return KTimeComboBox.Options()
        def __iand__(self, mask):
            '''KTimeComboBox.Options KTimeComboBox.Options.__iand__(int mask)'''
            return KTimeComboBox.Options()


class KTimeZoneWidget(QTreeWidget):
    """"""
    def __init__(self, parent = None, timeZones = None):
        '''void KTimeZoneWidget.__init__(QWidget parent = None, KTimeZones timeZones = None)'''
    def clearSelection(self):
        '''void KTimeZoneWidget.clearSelection()'''
    def selectionMode(self):
        '''QAbstractItemView.SelectionMode KTimeZoneWidget.selectionMode()'''
        return QAbstractItemView.SelectionMode()
    def setSelectionMode(self, mode):
        '''void KTimeZoneWidget.setSelectionMode(QAbstractItemView.SelectionMode mode)'''
    def itemsCheckable(self):
        '''bool KTimeZoneWidget.itemsCheckable()'''
        return bool()
    def setItemsCheckable(self, enable):
        '''void KTimeZoneWidget.setItemsCheckable(bool enable)'''
    def displayName(self, zone):
        '''static QString KTimeZoneWidget.displayName(KTimeZone zone)'''
        return QString()
    def setSelected(self, zone, selected):
        '''void KTimeZoneWidget.setSelected(QString zone, bool selected)'''
    def selection(self):
        '''QStringList KTimeZoneWidget.selection()'''
        return QStringList()


class KTipDatabase():
    """"""
    def __init__(self, tipFile = QString()):
        '''void KTipDatabase.__init__(QString tipFile = QString())'''
    def __init__(self, tipFiles):
        '''void KTipDatabase.__init__(QStringList tipFiles)'''
    def prevTip(self):
        '''void KTipDatabase.prevTip()'''
    def nextTip(self):
        '''void KTipDatabase.nextTip()'''
    def tip(self):
        '''QString KTipDatabase.tip()'''
        return QString()


class KTipDialog(KDialog):
    """"""
    def __init__(self, database, parent = None):
        '''void KTipDialog.__init__(KTipDatabase database, QWidget parent = None)'''
    def eventFilter(self):
        '''QEvent KTipDialog.eventFilter()'''
        return QEvent()
    def setShowOnStart(self, show):
        '''static void KTipDialog.setShowOnStart(bool show)'''
    def showMultiTip(self, parent, tipFiles, force = False):
        '''static void KTipDialog.showMultiTip(QWidget parent, QStringList tipFiles, bool force = False)'''
    def showTip(self, parent, tipFile = QString(), force = False):
        '''static void KTipDialog.showTip(QWidget parent, QString tipFile = QString(), bool force = False)'''
    def showTip(self, tipFile = QString(), force = False):
        '''static void KTipDialog.showTip(QString tipFile = QString(), bool force = False)'''


class KTitleWidget(QWidget):
    """"""
    # Enum KTitleWidget.MessageType
    PlainMessage = 0
    InfoMessage = 0
    WarningMessage = 0
    ErrorMessage = 0

    # Enum KTitleWidget.ImageAlignment
    ImageLeft = 0
    ImageRight = 0

    def __init__(self, parent = None):
        '''void KTitleWidget.__init__(QWidget parent = None)'''
    def eventFilter(self, object, event):
        '''bool KTitleWidget.eventFilter(QObject object, QEvent event)'''
        return bool()
    def showEvent(self, event):
        '''void KTitleWidget.showEvent(QShowEvent event)'''
    def changeEvent(self, e):
        '''void KTitleWidget.changeEvent(QEvent e)'''
    def setAutoHideTimeout(self, msecs):
        '''void KTitleWidget.setAutoHideTimeout(int msecs)'''
    def setPixmap(self, pixmap, alignment = None):
        '''void KTitleWidget.setPixmap(QPixmap pixmap, KTitleWidget.ImageAlignment alignment = KTitleWidget.ImageRight)'''
    def setPixmap(self, icon, alignment = None):
        '''void KTitleWidget.setPixmap(QString icon, KTitleWidget.ImageAlignment alignment = KTitleWidget.ImageRight)'''
    def setPixmap(self, icon, alignment = None):
        '''void KTitleWidget.setPixmap(QIcon icon, KTitleWidget.ImageAlignment alignment = KTitleWidget.ImageRight)'''
    def setPixmap(self, type, alignment = None):
        '''void KTitleWidget.setPixmap(KTitleWidget.MessageType type, KTitleWidget.ImageAlignment alignment = KTitleWidget.ImageRight)'''
    def setComment(self, comment, type = None):
        '''void KTitleWidget.setComment(QString comment, KTitleWidget.MessageType type = KTitleWidget.PlainMessage)'''
    def setText(self, text, alignment = None):
        '''void KTitleWidget.setText(QString text, Qt.Alignment alignment = Qt.AlignLeft|Qt.AlignVCenter)'''
    def setText(self, text, type):
        '''void KTitleWidget.setText(QString text, KTitleWidget.MessageType type)'''
    def autoHideTimeout(self):
        '''int KTitleWidget.autoHideTimeout()'''
        return int()
    def setBuddy(self, buddy):
        '''void KTitleWidget.setBuddy(QWidget buddy)'''
    def pixmap(self):
        '''QPixmap KTitleWidget.pixmap()'''
        return QPixmap()
    def comment(self):
        '''QString KTitleWidget.comment()'''
        return QString()
    def text(self):
        '''QString KTitleWidget.text()'''
        return QString()
    def setWidget(self, widget):
        '''void KTitleWidget.setWidget(QWidget widget)'''


class KToggleAction(KAction):
    """"""
    def __init__(self, parent):
        '''void KToggleAction.__init__(QObject parent)'''
    def __init__(self, text, parent):
        '''void KToggleAction.__init__(QString text, QObject parent)'''
    def __init__(self, icon, text, parent):
        '''void KToggleAction.__init__(KIcon icon, QString text, QObject parent)'''
    def slotToggled(self, checked):
        '''void KToggleAction.slotToggled(bool checked)'''
    def setCheckedState(self, checkedItem):
        '''void KToggleAction.setCheckedState(KGuiItem checkedItem)'''


class KToggleFullScreenAction(KToggleAction):
    """"""
    def __init__(self, parent):
        '''void KToggleFullScreenAction.__init__(QObject parent)'''
    def __init__(self, window, parent):
        '''void KToggleFullScreenAction.__init__(QWidget window, QObject parent)'''
    def eventFilter(self, object, event):
        '''bool KToggleFullScreenAction.eventFilter(QObject object, QEvent event)'''
        return bool()
    def setFullScreen(self, window, set):
        '''static void KToggleFullScreenAction.setFullScreen(QWidget window, bool set)'''
    def setWindow(self, window):
        '''void KToggleFullScreenAction.setWindow(QWidget window)'''


class KToggleToolBarAction(KToggleAction):
    """"""
    def __init__(self, toolBarName, text, parent):
        '''void KToggleToolBarAction.__init__(str toolBarName, QString text, QObject parent)'''
    def __init__(self, toolBar, text, parent):
        '''void KToggleToolBarAction.__init__(KToolBar toolBar, QString text, QObject parent)'''
    def eventFilter(self, watched, event):
        '''bool KToggleToolBarAction.eventFilter(QObject watched, QEvent event)'''
        return bool()
    def toolBar(self):
        '''KToolBar KToggleToolBarAction.toolBar()'''
        return KToolBar()


class KToolBar(QToolBar):
    """"""
    def __init__(self, parent, isMainToolBar = False, readConfig = True):
        '''void KToolBar.__init__(QWidget parent, bool isMainToolBar = False, bool readConfig = True)'''
    def __init__(self, objectName, parentWindow, area, newLine = False, isMainToolBar = False, readConfig = True):
        '''void KToolBar.__init__(QString objectName, QMainWindow parentWindow, Qt.ToolBarArea area, bool newLine = False, bool isMainToolBar = False, bool readConfig = True)'''
    def __init__(self, objectName, parent, readConfig = True):
        '''void KToolBar.__init__(QString objectName, QWidget parent, bool readConfig = True)'''
    def addXMLGUIClient(self, client):
        '''void KToolBar.addXMLGUIClient(KXMLGUIClient client)'''
    def mouseReleaseEvent(self):
        '''QMouseEvent KToolBar.mouseReleaseEvent()'''
        return QMouseEvent()
    def mouseMoveEvent(self):
        '''QMouseEvent KToolBar.mouseMoveEvent()'''
        return QMouseEvent()
    def mousePressEvent(self):
        '''QMouseEvent KToolBar.mousePressEvent()'''
        return QMouseEvent()
    def dropEvent(self):
        '''QDropEvent KToolBar.dropEvent()'''
        return QDropEvent()
    def dragLeaveEvent(self):
        '''QDragLeaveEvent KToolBar.dragLeaveEvent()'''
        return QDragLeaveEvent()
    def dragMoveEvent(self):
        '''QDragMoveEvent KToolBar.dragMoveEvent()'''
        return QDragMoveEvent()
    def dragEnterEvent(self):
        '''QDragEnterEvent KToolBar.dragEnterEvent()'''
        return QDragEnterEvent()
    def actionEvent(self):
        '''QActionEvent KToolBar.actionEvent()'''
        return QActionEvent()
    def contextMenuEvent(self):
        '''QContextMenuEvent KToolBar.contextMenuEvent()'''
        return QContextMenuEvent()
    def slotMovableChanged(self, movable):
        '''void KToolBar.slotMovableChanged(bool movable)'''
    def setToolBarsLocked(self, locked):
        '''static void KToolBar.setToolBarsLocked(bool locked)'''
    def toolBarsLocked(self):
        '''static bool KToolBar.toolBarsLocked()'''
        return bool()
    def setToolBarsEditable(self, editable):
        '''static void KToolBar.setToolBarsEditable(bool editable)'''
    def toolBarsEditable(self):
        '''static bool KToolBar.toolBarsEditable()'''
        return bool()
    def toolButtonStyleSetting(self):
        '''static Qt.ToolButtonStyle KToolBar.toolButtonStyleSetting()'''
        return Qt.ToolButtonStyle()
    def eventFilter(self, watched, event):
        '''bool KToolBar.eventFilter(QObject watched, QEvent event)'''
        return bool()
    def saveState(self, element):
        '''void KToolBar.saveState(QDomElement element)'''
    def loadState(self, element):
        '''void KToolBar.loadState(QDomElement element)'''
    def setXMLGUIClient(self, client):
        '''void KToolBar.setXMLGUIClient(KXMLGUIClient client)'''
    def applySettings(self, cg, forceGlobal = False):
        '''void KToolBar.applySettings(KConfigGroup cg, bool forceGlobal = False)'''
    def saveSettings(self, cg):
        '''void KToolBar.saveSettings(KConfigGroup cg)'''
    def contextMenuEnabled(self):
        '''bool KToolBar.contextMenuEnabled()'''
        return bool()
    def setContextMenuEnabled(self, enable = True):
        '''void KToolBar.setContextMenuEnabled(bool enable = True)'''
    def iconSizeDefault(self):
        '''int KToolBar.iconSizeDefault()'''
        return int()
    def setIconDimensions(self, size):
        '''void KToolBar.setIconDimensions(int size)'''
    def mainWindow(self):
        '''KMainWindow KToolBar.mainWindow()'''
        return KMainWindow()


class KToolBarLabelAction(KAction):
    """"""
    def __init__(self, text, parent):
        '''void KToolBarLabelAction.__init__(QString text, QObject parent)'''
    def __init__(self, buddy, text, parent):
        '''void KToolBarLabelAction.__init__(QAction buddy, QString text, QObject parent)'''
    def eventFilter(self, watched, event):
        '''bool KToolBarLabelAction.eventFilter(QObject watched, QEvent event)'''
        return bool()
    def event(self):
        '''QEvent KToolBarLabelAction.event()'''
        return QEvent()
    textChanged = pyqtSignal() # void textChanged(const QStringamp;) - signal
    def createWidget(self, parent):
        '''QWidget KToolBarLabelAction.createWidget(QWidget parent)'''
        return QWidget()
    def buddy(self):
        '''QAction KToolBarLabelAction.buddy()'''
        return QAction()
    def setBuddy(self, buddy):
        '''void KToolBarLabelAction.setBuddy(QAction buddy)'''


class KToolBarPopupAction(KAction):
    """"""
    def __init__(self, icon, text, parent):
        '''void KToolBarPopupAction.__init__(KIcon icon, QString text, QObject parent)'''
    def createWidget(self, parent):
        '''QWidget KToolBarPopupAction.createWidget(QWidget parent)'''
        return QWidget()
    def setStickyMenu(self, sticky):
        '''void KToolBarPopupAction.setStickyMenu(bool sticky)'''
    def stickyMenu(self):
        '''bool KToolBarPopupAction.stickyMenu()'''
        return bool()
    def setDelayed(self, delayed):
        '''void KToolBarPopupAction.setDelayed(bool delayed)'''
    def delayed(self):
        '''bool KToolBarPopupAction.delayed()'''
        return bool()
    def popupMenu(self):
        '''KMenu KToolBarPopupAction.popupMenu()'''
        return KMenu()


class KToolBarSpacerAction(KAction):
    """"""
    def __init__(self, parent):
        '''void KToolBarSpacerAction.__init__(QObject parent)'''
    def deleteWidget(self, widget):
        '''void KToolBarSpacerAction.deleteWidget(QWidget widget)'''
    def createWidget(self, parent):
        '''QWidget KToolBarSpacerAction.createWidget(QWidget parent)'''
        return QWidget()
    def setMaximumWidth(self, width):
        '''void KToolBarSpacerAction.setMaximumWidth(int width)'''
    def maximumWidth(self):
        '''int KToolBarSpacerAction.maximumWidth()'''
        return int()
    def setMinimumWidth(self, width):
        '''void KToolBarSpacerAction.setMinimumWidth(int width)'''
    def minimumWidth(self):
        '''int KToolBarSpacerAction.minimumWidth()'''
        return int()
    def setWidth(self, width):
        '''void KToolBarSpacerAction.setWidth(int width)'''
    def width(self):
        '''int KToolBarSpacerAction.width()'''
        return int()


class KTreeWidgetSearchLine(KLineEdit):
    """"""
    def __init__(self, parent = None, treeWidget = None):
        '''void KTreeWidgetSearchLine.__init__(QWidget parent = None, QTreeWidget treeWidget = None)'''
    def __init__(self, parent, treeWidgets):
        '''void KTreeWidgetSearchLine.__init__(QWidget parent, list-of-QTreeWidget treeWidgets)'''
    def event(self, event):
        '''bool KTreeWidgetSearchLine.event(QEvent event)'''
        return bool()
    def canChooseColumnsCheck(self):
        '''bool KTreeWidgetSearchLine.canChooseColumnsCheck()'''
        return bool()
    def disconnectTreeWidget(self):
        '''QTreeWidget KTreeWidgetSearchLine.disconnectTreeWidget()'''
        return QTreeWidget()
    def connectTreeWidget(self):
        '''QTreeWidget KTreeWidgetSearchLine.connectTreeWidget()'''
        return QTreeWidget()
    def contextMenuEvent(self):
        '''QContextMenuEvent KTreeWidgetSearchLine.contextMenuEvent()'''
        return QContextMenuEvent()
    def itemMatches(self, item, pattern):
        '''bool KTreeWidgetSearchLine.itemMatches(QTreeWidgetItem item, QString pattern)'''
        return bool()
    def setTreeWidgets(self, treeWidgets):
        '''void KTreeWidgetSearchLine.setTreeWidgets(list-of-QTreeWidget treeWidgets)'''
    def setTreeWidget(self, treeWidget):
        '''void KTreeWidgetSearchLine.setTreeWidget(QTreeWidget treeWidget)'''
    def setSearchColumns(self, columns):
        '''void KTreeWidgetSearchLine.setSearchColumns(list-of-int columns)'''
    def setKeepParentsVisible(self, value):
        '''void KTreeWidgetSearchLine.setKeepParentsVisible(bool value)'''
    def setCaseSensitivity(self, caseSensitivity):
        '''void KTreeWidgetSearchLine.setCaseSensitivity(Qt.CaseSensitivity caseSensitivity)'''
    def updateSearch(self, pattern = QString()):
        '''void KTreeWidgetSearchLine.updateSearch(QString pattern = QString())'''
    def updateSearch(self, treeWidget):
        '''void KTreeWidgetSearchLine.updateSearch(QTreeWidget treeWidget)'''
    def removeTreeWidget(self, treeWidget):
        '''void KTreeWidgetSearchLine.removeTreeWidget(QTreeWidget treeWidget)'''
    def addTreeWidget(self, treeWidget):
        '''void KTreeWidgetSearchLine.addTreeWidget(QTreeWidget treeWidget)'''
    hiddenChanged = pyqtSignal() # void hiddenChanged(QTreeWidgetItem *,bool) - signal
    def treeWidgets(self):
        '''list-of-QTreeWidget KTreeWidgetSearchLine.treeWidgets()'''
        return [QTreeWidget()]
    def treeWidget(self):
        '''QTreeWidget KTreeWidgetSearchLine.treeWidget()'''
        return QTreeWidget()
    def keepParentsVisible(self):
        '''bool KTreeWidgetSearchLine.keepParentsVisible()'''
        return bool()
    def searchColumns(self):
        '''list-of-int KTreeWidgetSearchLine.searchColumns()'''
        return [int()]
    def caseSensitivity(self):
        '''Qt.CaseSensitivity KTreeWidgetSearchLine.caseSensitivity()'''
        return Qt.CaseSensitivity()


class KTreeWidgetSearchLineWidget(QWidget):
    """"""
    def __init__(self, parent = None, treeWidget = None):
        '''void KTreeWidgetSearchLineWidget.__init__(QWidget parent = None, QTreeWidget treeWidget = None)'''
    def createSearchLine(self, treeWidget):
        '''KTreeWidgetSearchLine KTreeWidgetSearchLineWidget.createSearchLine(QTreeWidget treeWidget)'''
        return KTreeWidgetSearchLine()
    def createWidgets(self):
        '''void KTreeWidgetSearchLineWidget.createWidgets()'''
    def searchLine(self):
        '''KTreeWidgetSearchLine KTreeWidgetSearchLineWidget.searchLine()'''
        return KTreeWidgetSearchLine()


class KUiServerJobTracker(KJobTrackerInterface):
    """"""
    def __init__(self, parent = None):
        '''void KUiServerJobTracker.__init__(QObject parent = None)'''
    def speed(self, job, value):
        '''void KUiServerJobTracker.speed(KJob job, int value)'''
    def percent(self, job, percent):
        '''void KUiServerJobTracker.percent(KJob job, int percent)'''
    def processedAmount(self, job, unit, amount):
        '''void KUiServerJobTracker.processedAmount(KJob job, KJob.Unit unit, int amount)'''
    def totalAmount(self, job, unit, amount):
        '''void KUiServerJobTracker.totalAmount(KJob job, KJob.Unit unit, int amount)'''
    def infoMessage(self, job, plain, rich):
        '''void KUiServerJobTracker.infoMessage(KJob job, QString plain, QString rich)'''
    def description(self, job, title, field1, field2):
        '''void KUiServerJobTracker.description(KJob job, QString title, unknown-type field1, unknown-type field2)'''
    def resumed(self, job):
        '''void KUiServerJobTracker.resumed(KJob job)'''
    def suspended(self, job):
        '''void KUiServerJobTracker.suspended(KJob job)'''
    def finished(self, job):
        '''void KUiServerJobTracker.finished(KJob job)'''
    def unregisterJob(self, job):
        '''void KUiServerJobTracker.unregisterJob(KJob job)'''
    def registerJob(self, job):
        '''void KUiServerJobTracker.registerJob(KJob job)'''


class KUndoStack(QUndoStack):
    """"""
    def __init__(self, parent = None):
        '''void KUndoStack.__init__(QObject parent = None)'''
    def createUndoAction(self, actionCollection, actionName = QString()):
        '''QAction KUndoStack.createUndoAction(KActionCollection actionCollection, QString actionName = QString())'''
        return QAction()
    def createRedoAction(self, actionCollection, actionName = QString()):
        '''QAction KUndoStack.createRedoAction(KActionCollection actionCollection, QString actionName = QString())'''
        return QAction()


class KUniqueApplication(KApplication):
    """"""
    # Enum KUniqueApplication.StartFlag
    NonUniqueInstance = 0

    def __init__(self, GUIenabled = True, configUnique = False):
        '''void KUniqueApplication.__init__(bool GUIenabled = True, bool configUnique = False)'''
    def __init__(self, display, visual = 0, colormap = 0, configUnique = False):
        '''void KUniqueApplication.__init__(Display display, int visual = 0, int colormap = 0, bool configUnique = False)'''
    def setHandleAutoStarted(self):
        '''static void KUniqueApplication.setHandleAutoStarted()'''
    def restoringSession(self):
        '''bool KUniqueApplication.restoringSession()'''
        return bool()
    def newInstance(self):
        '''int KUniqueApplication.newInstance()'''
        return int()
    def start(self, flags):
        '''static bool KUniqueApplication.start(KUniqueApplication.StartFlags flags)'''
        return bool()
    def start(self):
        '''static bool KUniqueApplication.start()'''
        return bool()
    def addCmdLineOptions(self):
        '''static void KUniqueApplication.addCmdLineOptions()'''
    class StartFlags():
        """"""
        def __init__(self):
            '''KUniqueApplication.StartFlags KUniqueApplication.StartFlags.__init__()'''
            return KUniqueApplication.StartFlags()
        def __init__(self):
            '''int KUniqueApplication.StartFlags.__init__()'''
            return int()
        def __init__(self):
            '''void KUniqueApplication.StartFlags.__init__()'''
        def __bool__(self):
            '''int KUniqueApplication.StartFlags.__bool__()'''
            return int()
        def __ne__(self, f):
            '''bool KUniqueApplication.StartFlags.__ne__(KUniqueApplication.StartFlags f)'''
            return bool()
        def __eq__(self, f):
            '''bool KUniqueApplication.StartFlags.__eq__(KUniqueApplication.StartFlags f)'''
            return bool()
        def __invert__(self):
            '''KUniqueApplication.StartFlags KUniqueApplication.StartFlags.__invert__()'''
            return KUniqueApplication.StartFlags()
        def __and__(self, mask):
            '''KUniqueApplication.StartFlags KUniqueApplication.StartFlags.__and__(int mask)'''
            return KUniqueApplication.StartFlags()
        def __xor__(self, f):
            '''KUniqueApplication.StartFlags KUniqueApplication.StartFlags.__xor__(KUniqueApplication.StartFlags f)'''
            return KUniqueApplication.StartFlags()
        def __xor__(self, f):
            '''KUniqueApplication.StartFlags KUniqueApplication.StartFlags.__xor__(int f)'''
            return KUniqueApplication.StartFlags()
        def __or__(self, f):
            '''KUniqueApplication.StartFlags KUniqueApplication.StartFlags.__or__(KUniqueApplication.StartFlags f)'''
            return KUniqueApplication.StartFlags()
        def __or__(self, f):
            '''KUniqueApplication.StartFlags KUniqueApplication.StartFlags.__or__(int f)'''
            return KUniqueApplication.StartFlags()
        def __int__(self):
            '''int KUniqueApplication.StartFlags.__int__()'''
            return int()
        def __ixor__(self, f):
            '''KUniqueApplication.StartFlags KUniqueApplication.StartFlags.__ixor__(KUniqueApplication.StartFlags f)'''
            return KUniqueApplication.StartFlags()
        def __ior__(self, f):
            '''KUniqueApplication.StartFlags KUniqueApplication.StartFlags.__ior__(KUniqueApplication.StartFlags f)'''
            return KUniqueApplication.StartFlags()
        def __iand__(self, mask):
            '''KUniqueApplication.StartFlags KUniqueApplication.StartFlags.__iand__(int mask)'''
            return KUniqueApplication.StartFlags()


class KUrlLabel(QLabel):
    """"""
    def __init__(self, parent = None):
        '''void KUrlLabel.__init__(QWidget parent = None)'''
    def __init__(self, url, text = QString(), parent = None):
        '''void KUrlLabel.__init__(QString url, QString text = QString(), QWidget parent = None)'''
    def event(self):
        '''QEvent KUrlLabel.event()'''
        return QEvent()
    def leaveEvent(self):
        '''QEvent KUrlLabel.leaveEvent()'''
        return QEvent()
    def enterEvent(self):
        '''QEvent KUrlLabel.enterEvent()'''
        return QEvent()
    def mouseReleaseEvent(self):
        '''QMouseEvent KUrlLabel.mouseReleaseEvent()'''
        return QMouseEvent()
    middleClickedUrl = pyqtSignal() # void middleClickedUrl(const QStringamp;) - signal
    middleClickedUrl = pyqtSignal() # void middleClickedUrl() - signal
    rightClickedUrl = pyqtSignal() # void rightClickedUrl(const QStringamp;) - signal
    rightClickedUrl = pyqtSignal() # void rightClickedUrl() - signal
    leftClickedUrl = pyqtSignal() # void leftClickedUrl(const QStringamp;) - signal
    leftClickedUrl = pyqtSignal() # void leftClickedUrl() - signal
    leftUrl = pyqtSignal() # void leftUrl(const QStringamp;) - signal
    leftUrl = pyqtSignal() # void leftUrl() - signal
    enteredUrl = pyqtSignal() # void enteredUrl(const QStringamp;) - signal
    enteredUrl = pyqtSignal() # void enteredUrl() - signal
    def setAlternatePixmap(self, pixmap):
        '''void KUrlLabel.setAlternatePixmap(QPixmap pixmap)'''
    def setFloatEnabled(self, do_float = True):
        '''void KUrlLabel.setFloatEnabled(bool do_float = True)'''
    def setGlowEnabled(self, glow = True):
        '''void KUrlLabel.setGlowEnabled(bool glow = True)'''
    def setUseCursor(self, on, cursor = None):
        '''void KUrlLabel.setUseCursor(bool on, QCursor cursor = None)'''
    def setSelectedColor(self, color):
        '''void KUrlLabel.setSelectedColor(QColor color)'''
    def setSelectedColor(self, color):
        '''void KUrlLabel.setSelectedColor(QString color)'''
    def setHighlightedColor(self, highcolor):
        '''void KUrlLabel.setHighlightedColor(QColor highcolor)'''
    def setHighlightedColor(self, highcolor):
        '''void KUrlLabel.setHighlightedColor(QString highcolor)'''
    def setTipText(self, tip):
        '''void KUrlLabel.setTipText(QString tip)'''
    def setUseTips(self, on = True):
        '''void KUrlLabel.setUseTips(bool on = True)'''
    def setFont(self, font):
        '''void KUrlLabel.setFont(QFont font)'''
    def setUrl(self, url):
        '''void KUrlLabel.setUrl(QString url)'''
    def setUnderline(self, on = True):
        '''void KUrlLabel.setUnderline(bool on = True)'''
    def alternatePixmap(self):
        '''QPixmap KUrlLabel.alternatePixmap()'''
        return QPixmap()
    def isFloatEnabled(self):
        '''bool KUrlLabel.isFloatEnabled()'''
        return bool()
    def isGlowEnabled(self):
        '''bool KUrlLabel.isGlowEnabled()'''
        return bool()
    def useCursor(self):
        '''bool KUrlLabel.useCursor()'''
        return bool()
    def useTips(self):
        '''bool KUrlLabel.useTips()'''
        return bool()
    def tipText(self):
        '''QString KUrlLabel.tipText()'''
        return QString()
    def url(self):
        '''QString KUrlLabel.url()'''
        return QString()


class KVBox(KHBox):
    """"""
    def __init__(self, parent = None):
        '''void KVBox.__init__(QWidget parent = None)'''


class KViewStateMaintainerBase(QObject):
    """"""
    def __init__(self, configGroup, parent = None):
        '''void KViewStateMaintainerBase.__init__(KConfigGroup configGroup, QObject parent = None)'''
    def configGroup(self):
        '''KConfigGroup KViewStateMaintainerBase.configGroup()'''
        return KConfigGroup()
    def restoreState(self):
        '''abstract void KViewStateMaintainerBase.restoreState()'''
    def saveState(self):
        '''abstract void KViewStateMaintainerBase.saveState()'''
    def view(self):
        '''QAbstractItemView KViewStateMaintainerBase.view()'''
        return QAbstractItemView()
    def setView(self, view):
        '''void KViewStateMaintainerBase.setView(QAbstractItemView view)'''
    def selectionModel(self):
        '''QItemSelectionModel KViewStateMaintainerBase.selectionModel()'''
        return QItemSelectionModel()
    def setSelectionModel(self, selectionModel):
        '''void KViewStateMaintainerBase.setSelectionModel(QItemSelectionModel selectionModel)'''


class KViewStateSaver(QObject):
    """"""
    def __init__(self, parent = None):
        '''void KViewStateSaver.__init__(QObject parent = None)'''
    def indexToConfigString(self, index):
        '''abstract QString KViewStateSaver.indexToConfigString(QModelIndex index)'''
        return QString()
    def indexFromConfigString(self, model, key):
        '''abstract QModelIndex KViewStateSaver.indexFromConfigString(QAbstractItemModel model, QString key)'''
        return QModelIndex()
    def restoreScrollState(self, verticalScoll, horizontalScroll):
        '''void KViewStateSaver.restoreScrollState(int verticalScoll, int horizontalScroll)'''
    def restoreExpanded(self, indexStrings):
        '''void KViewStateSaver.restoreExpanded(QStringList indexStrings)'''
    def restoreCurrentItem(self, indexString):
        '''void KViewStateSaver.restoreCurrentItem(QString indexString)'''
    def restoreSelection(self, indexStrings):
        '''void KViewStateSaver.restoreSelection(QStringList indexStrings)'''
    def scrollState(self):
        '''tuple-of-int-int KViewStateSaver.scrollState()'''
        return tuple-of-int-int()
    def currentIndexKey(self):
        '''QString KViewStateSaver.currentIndexKey()'''
        return QString()
    def expansionKeys(self):
        '''QStringList KViewStateSaver.expansionKeys()'''
        return QStringList()
    def selectionKeys(self):
        '''QStringList KViewStateSaver.selectionKeys()'''
        return QStringList()
    def restoreState(self, configGroup):
        '''void KViewStateSaver.restoreState(KConfigGroup configGroup)'''
    def saveState(self, configGroup):
        '''void KViewStateSaver.saveState(KConfigGroup configGroup)'''
    def setSelectionModel(self, selectionModel):
        '''void KViewStateSaver.setSelectionModel(QItemSelectionModel selectionModel)'''
    def selectionModel(self):
        '''QItemSelectionModel KViewStateSaver.selectionModel()'''
        return QItemSelectionModel()
    def setView(self, view):
        '''void KViewStateSaver.setView(QAbstractItemView view)'''
    def view(self):
        '''QAbstractItemView KViewStateSaver.view()'''
        return QAbstractItemView()


class KWallet():
    """"""
    class Wallet(QObject):
        """"""
        # Enum KWallet.Wallet.OpenType
        Synchronous = 0
        Asynchronous = 0
        Path = 0
        OpenTypeUnused = 0
    
        # Enum KWallet.Wallet.EntryType
        Unknown = 0
        Password = 0
        Stream = 0
        Map = 0
        Unused = 0
    
        def __init__(self, handle, name):
            '''void KWallet.Wallet.__init__(int handle, QString name)'''
        def isUsingKSecretsService(self):
            '''static bool KWallet.Wallet.isUsingKSecretsService()'''
            return bool()
        walletOpened = pyqtSignal() # void walletOpened(bool) - signal
        folderRemoved = pyqtSignal() # void folderRemoved(const QStringamp;) - signal
        folderListUpdated = pyqtSignal() # void folderListUpdated() - signal
        folderUpdated = pyqtSignal() # void folderUpdated(const QStringamp;) - signal
        walletClosed = pyqtSignal() # void walletClosed() - signal
        def keyDoesNotExist(self, wallet, folder, key):
            '''static bool KWallet.Wallet.keyDoesNotExist(QString wallet, QString folder, QString key)'''
            return bool()
        def folderDoesNotExist(self, wallet, folder):
            '''static bool KWallet.Wallet.folderDoesNotExist(QString wallet, QString folder)'''
            return bool()
        def entryType(self, key):
            '''KWallet.Wallet.EntryType KWallet.Wallet.entryType(QString key)'''
            return KWallet.Wallet.EntryType()
        def removeEntry(self, key):
            '''int KWallet.Wallet.removeEntry(QString key)'''
            return int()
        def hasEntry(self, key):
            '''bool KWallet.Wallet.hasEntry(QString key)'''
            return bool()
        def writePassword(self, key, value):
            '''int KWallet.Wallet.writePassword(QString key, QString value)'''
            return int()
        def writeMap(self, key, value):
            '''int KWallet.Wallet.writeMap(QString key, dict-of-QString-QString value)'''
            return int()
        def writeEntry(self, key, value, entryType):
            '''int KWallet.Wallet.writeEntry(QString key, QByteArray value, KWallet.Wallet.EntryType entryType)'''
            return int()
        def writeEntry(self, key, value):
            '''int KWallet.Wallet.writeEntry(QString key, QByteArray value)'''
            return int()
        def readPasswordList(self, key, value):
            '''int KWallet.Wallet.readPasswordList(QString key, dict-of-QString-QString value)'''
            return int()
        def readEntryList(self, key, value):
            '''int KWallet.Wallet.readEntryList(QString key, dict-of-QString-QByteArray value)'''
            return int()
        def readPassword(self, key, value):
            '''int KWallet.Wallet.readPassword(QString key, QString value)'''
            return int()
        def readMap(self, key, value):
            '''int KWallet.Wallet.readMap(QString key, dict-of-QString-QString value)'''
            return int()
        def readEntry(self, key, value):
            '''int KWallet.Wallet.readEntry(QString key, QByteArray value)'''
            return int()
        def renameEntry(self, oldName, newName):
            '''int KWallet.Wallet.renameEntry(QString oldName, QString newName)'''
            return int()
        def entryList(self):
            '''QStringList KWallet.Wallet.entryList()'''
            return QStringList()
        def currentFolder(self):
            '''QString KWallet.Wallet.currentFolder()'''
            return QString()
        def createFolder(self, f):
            '''bool KWallet.Wallet.createFolder(QString f)'''
            return bool()
        def removeFolder(self, f):
            '''bool KWallet.Wallet.removeFolder(QString f)'''
            return bool()
        def setFolder(self, f):
            '''bool KWallet.Wallet.setFolder(QString f)'''
            return bool()
        def hasFolder(self, f):
            '''bool KWallet.Wallet.hasFolder(QString f)'''
            return bool()
        def folderList(self):
            '''QStringList KWallet.Wallet.folderList()'''
            return QStringList()
        def requestChangePassword(self, w):
            '''void KWallet.Wallet.requestChangePassword(int w)'''
        def walletName(self):
            '''QString KWallet.Wallet.walletName()'''
            return QString()
        def lockWallet(self):
            '''int KWallet.Wallet.lockWallet()'''
            return int()
        def sync(self):
            '''int KWallet.Wallet.sync()'''
            return int()
        def changePassword(self, name, w):
            '''static void KWallet.Wallet.changePassword(QString name, int w)'''
        def FormDataFolder(self):
            '''static QString KWallet.Wallet.FormDataFolder()'''
            return QString()
        def PasswordFolder(self):
            '''static QString KWallet.Wallet.PasswordFolder()'''
            return QString()
        def NetworkWallet(self):
            '''static QString KWallet.Wallet.NetworkWallet()'''
            return QString()
        def LocalWallet(self):
            '''static QString KWallet.Wallet.LocalWallet()'''
            return QString()
        def users(self, wallet):
            '''static QStringList KWallet.Wallet.users(QString wallet)'''
            return QStringList()
        def openWallet(self, name, w, ot = None):
            '''static KWallet.Wallet KWallet.Wallet.openWallet(QString name, int w, KWallet.Wallet.OpenType ot = KWallet.Wallet.Synchronous)'''
            return KWallet.Wallet()
        def disconnectApplication(self, wallet, app):
            '''static bool KWallet.Wallet.disconnectApplication(QString wallet, QString app)'''
            return bool()
        def deleteWallet(self, name):
            '''static int KWallet.Wallet.deleteWallet(QString name)'''
            return int()
        def closeWallet(self, name, force):
            '''static int KWallet.Wallet.closeWallet(QString name, bool force)'''
            return int()
        def isOpen(self, name):
            '''static bool KWallet.Wallet.isOpen(QString name)'''
            return bool()
        def isOpen(self):
            '''bool KWallet.Wallet.isOpen()'''
            return bool()
        def isEnabled(self):
            '''static bool KWallet.Wallet.isEnabled()'''
            return bool()
        def walletList(self):
            '''static QStringList KWallet.Wallet.walletList()'''
            return QStringList()


class KWidgetItemDelegate(QAbstractItemDelegate):
    """"""
    def __init__(self, itemView, parent = None):
        '''void KWidgetItemDelegate.__init__(QAbstractItemView itemView, QObject parent = None)'''
    def blockedEventTypes(self, widget):
        '''unknown-type KWidgetItemDelegate.blockedEventTypes(QWidget widget)'''
        return unknown-type()
    def setBlockedEventTypes(self, widget, types):
        '''void KWidgetItemDelegate.setBlockedEventTypes(QWidget widget, unknown-type types)'''
    def paintWidgets(self, painter, option, index):
        '''void KWidgetItemDelegate.paintWidgets(QPainter painter, QStyleOptionViewItem option, QPersistentModelIndex index)'''
    def updateItemWidgets(self, widgets, option, index):
        '''abstract void KWidgetItemDelegate.updateItemWidgets(list-of-QWidget widgets, QStyleOptionViewItem option, QPersistentModelIndex index)'''
    def createItemWidgets(self):
        '''abstract list-of-QWidget KWidgetItemDelegate.createItemWidgets()'''
        return [QWidget()]
    def focusedIndex(self):
        '''QPersistentModelIndex KWidgetItemDelegate.focusedIndex()'''
        return QPersistentModelIndex()
    def itemView(self):
        '''QAbstractItemView KWidgetItemDelegate.itemView()'''
        return QAbstractItemView()


class KWidgetJobTracker(KAbstractWidgetJobTracker):
    """"""
    def __init__(self, parent = None):
        '''void KWidgetJobTracker.__init__(QWidget parent = None)'''
    def resumed(self, job):
        '''void KWidgetJobTracker.resumed(KJob job)'''
    def suspended(self, job):
        '''void KWidgetJobTracker.suspended(KJob job)'''
    def slotClean(self, job):
        '''void KWidgetJobTracker.slotClean(KJob job)'''
    def speed(self, job, value):
        '''void KWidgetJobTracker.speed(KJob job, int value)'''
    def percent(self, job, percent):
        '''void KWidgetJobTracker.percent(KJob job, int percent)'''
    def processedAmount(self, job, unit, amount):
        '''void KWidgetJobTracker.processedAmount(KJob job, KJob.Unit unit, int amount)'''
    def totalAmount(self, job, unit, amount):
        '''void KWidgetJobTracker.totalAmount(KJob job, KJob.Unit unit, int amount)'''
    def description(self, job, title, field1, field2):
        '''void KWidgetJobTracker.description(KJob job, QString title, unknown-type field1, unknown-type field2)'''
    def infoMessage(self, job, plain, rich):
        '''void KWidgetJobTracker.infoMessage(KJob job, QString plain, QString rich)'''
    def keepOpen(self, job):
        '''bool KWidgetJobTracker.keepOpen(KJob job)'''
        return bool()
    def unregisterJob(self, job):
        '''void KWidgetJobTracker.unregisterJob(KJob job)'''
    def registerJob(self, job):
        '''void KWidgetJobTracker.registerJob(KJob job)'''
    def widget(self, job):
        '''QWidget KWidgetJobTracker.widget(KJob job)'''
        return QWidget()


class KWindowInfo():
    """"""
    def __init__(self, window, properties, properties2 = 0):
        '''void KWindowInfo.__init__(int window, int properties, int properties2 = 0)'''
    def __init__(self):
        '''void KWindowInfo.__init__()'''
    def __init__(self):
        '''KWindowInfo KWindowInfo.__init__()'''
        return KWindowInfo()
    def actionSupported(self, action):
        '''bool KWindowInfo.actionSupported(NET.Action action)'''
        return bool()
    def clientMachine(self):
        '''QByteArray KWindowInfo.clientMachine()'''
        return QByteArray()
    def windowRole(self):
        '''QByteArray KWindowInfo.windowRole()'''
        return QByteArray()
    def windowClassName(self):
        '''QByteArray KWindowInfo.windowClassName()'''
        return QByteArray()
    def windowClassClass(self):
        '''QByteArray KWindowInfo.windowClassClass()'''
        return QByteArray()
    def groupLeader(self):
        '''int KWindowInfo.groupLeader()'''
        return int()
    def transientFor(self):
        '''int KWindowInfo.transientFor()'''
        return int()
    def frameGeometry(self):
        '''QRect KWindowInfo.frameGeometry()'''
        return QRect()
    def geometry(self):
        '''QRect KWindowInfo.geometry()'''
        return QRect()
    def desktop(self):
        '''int KWindowInfo.desktop()'''
        return int()
    def onAllDesktops(self):
        '''bool KWindowInfo.onAllDesktops()'''
        return bool()
    def isOnDesktop(self, desktop):
        '''bool KWindowInfo.isOnDesktop(int desktop)'''
        return bool()
    def isOnCurrentDesktop(self):
        '''bool KWindowInfo.isOnCurrentDesktop()'''
        return bool()
    def iconName(self):
        '''QString KWindowInfo.iconName()'''
        return QString()
    def visibleIconNameWithState(self):
        '''QString KWindowInfo.visibleIconNameWithState()'''
        return QString()
    def visibleIconName(self):
        '''QString KWindowInfo.visibleIconName()'''
        return QString()
    def name(self):
        '''QString KWindowInfo.name()'''
        return QString()
    def visibleNameWithState(self):
        '''QString KWindowInfo.visibleNameWithState()'''
        return QString()
    def visibleName(self):
        '''QString KWindowInfo.visibleName()'''
        return QString()
    def windowType(self, supported_types):
        '''NET.WindowType KWindowInfo.windowType(int supported_types)'''
        return NET.WindowType()
    def extendedStrut(self):
        '''NETExtendedStrut KWindowInfo.extendedStrut()'''
        return NETExtendedStrut()
    def mappingState(self):
        '''NET.MappingState KWindowInfo.mappingState()'''
        return NET.MappingState()
    def isMinimized(self):
        '''bool KWindowInfo.isMinimized()'''
        return bool()
    def hasState(self, s):
        '''bool KWindowInfo.hasState(int s)'''
        return bool()
    def state(self):
        '''int KWindowInfo.state()'''
        return int()
    def win(self):
        '''int KWindowInfo.win()'''
        return int()
    def valid(self, withdrawn_is_valid = False):
        '''bool KWindowInfo.valid(bool withdrawn_is_valid = False)'''
        return bool()


class NET():
    """"""
    # Enum NET.DesktopLayoutCorner
    DesktopLayoutCornerTopLeft = 0
    DesktopLayoutCornerTopRight = 0
    DesktopLayoutCornerBottomLeft = 0
    DesktopLayoutCornerBottomRight = 0

    # Enum NET.Orientation
    OrientationHorizontal = 0
    OrientationVertical = 0

    # Enum NET.RequestSource
    FromUnknown = 0
    FromApplication = 0
    FromTool = 0

    OnAllDesktops = None # int - member
    # Enum NET.Property2
    WM2UserTime = 0
    WM2StartupId = 0
    WM2TransientFor = 0
    WM2GroupLeader = 0
    WM2AllowedActions = 0
    WM2RestackWindow = 0
    WM2MoveResizeWindow = 0
    WM2ExtendedStrut = 0
    WM2TakeActivity = 0
    WM2KDETemporaryRules = 0
    WM2WindowClass = 0
    WM2WindowRole = 0
    WM2ClientMachine = 0
    WM2ShowingDesktop = 0
    WM2Opacity = 0
    WM2DesktopLayout = 0
    WM2FullPlacement = 0
    WM2FullscreenMonitors = 0
    WM2FrameOverlap = 0
    WM2Activities = 0
    WM2BlockCompositing = 0
    WM2KDEShadow = 0

    # Enum NET.Property
    Supported = 0
    ClientList = 0
    ClientListStacking = 0
    NumberOfDesktops = 0
    DesktopGeometry = 0
    DesktopViewport = 0
    CurrentDesktop = 0
    DesktopNames = 0
    ActiveWindow = 0
    WorkArea = 0
    SupportingWMCheck = 0
    VirtualRoots = 0
    CloseWindow = 0
    WMMoveResize = 0
    WMName = 0
    WMVisibleName = 0
    WMDesktop = 0
    WMWindowType = 0
    WMState = 0
    WMStrut = 0
    WMIconGeometry = 0
    WMIcon = 0
    WMPid = 0
    WMHandledIcons = 0
    WMPing = 0
    XAWMState = 0
    WMFrameExtents = 0
    WMIconName = 0
    WMVisibleIconName = 0
    WMGeometry = 0

    # Enum NET.Action
    ActionMove = 0
    ActionResize = 0
    ActionMinimize = 0
    ActionShade = 0
    ActionStick = 0
    ActionMaxVert = 0
    ActionMaxHoriz = 0
    ActionMax = 0
    ActionFullScreen = 0
    ActionChangeDesktop = 0
    ActionClose = 0

    # Enum NET.MappingState
    Visible = 0
    Withdrawn = 0
    Iconic = 0

    # Enum NET.Direction
    TopLeft = 0
    Top = 0
    TopRight = 0
    Right = 0
    BottomRight = 0
    Bottom = 0
    BottomLeft = 0
    Left = 0
    Move = 0
    KeyboardSize = 0
    KeyboardMove = 0
    MoveResizeCancel = 0

    # Enum NET.State
    Modal = 0
    Sticky = 0
    MaxVert = 0
    MaxHoriz = 0
    Max = 0
    Shaded = 0
    SkipTaskbar = 0
    KeepAbove = 0
    StaysOnTop = 0
    SkipPager = 0
    Hidden = 0
    FullScreen = 0
    KeepBelow = 0
    DemandsAttention = 0

    # Enum NET.WindowTypeMask
    NormalMask = 0
    DesktopMask = 0
    DockMask = 0
    ToolbarMask = 0
    MenuMask = 0
    DialogMask = 0
    OverrideMask = 0
    TopMenuMask = 0
    UtilityMask = 0
    SplashMask = 0
    DropdownMenuMask = 0
    PopupMenuMask = 0
    TooltipMask = 0
    NotificationMask = 0
    ComboBoxMask = 0
    DNDIconMask = 0
    AllTypesMask = 0

    # Enum NET.WindowType
    Unknown = 0
    Normal = 0
    Desktop = 0
    Dock = 0
    Toolbar = 0
    Menu = 0
    Dialog = 0
    Override = 0
    TopMenu = 0
    Utility = 0
    Splash = 0
    DropdownMenu = 0
    PopupMenu = 0
    Tooltip = 0
    Notification = 0
    ComboBox = 0
    DNDIcon = 0

    # Enum NET.Role
    Client = 0
    WindowManager = 0

    def __init__(self):
        '''void NET.__init__()'''
    def __init__(self):
        '''NET NET.__init__()'''
        return NET()
    def timestampDiff(self, time1, time2):
        '''static int NET.timestampDiff(int time1, int time2)'''
        return int()
    def timestampCompare(self, time1, time2):
        '''static int NET.timestampCompare(int time1, int time2)'''
        return int()
    def typeMatchesMask(self, type, mask):
        '''static bool NET.typeMatchesMask(NET.WindowType type, int mask)'''
        return bool()


class KWindowSystem(QObject, NET):
    """"""
    # Enum KWindowSystem.IconSource
    NETWM = 0
    WMHints = 0
    ClassHint = 0
    XApp = 0

    compositingChanged = pyqtSignal() # void compositingChanged(bool) - signal
    def setBlockingCompositing(self, window, active):
        '''static void KWindowSystem.setBlockingCompositing(int window, bool active)'''
    def allowExternalProcessWindowActivation(self, pid = None):
        '''static void KWindowSystem.allowExternalProcessWindowActivation(int pid = -1)'''
    def connectNotify(self):
        '''SIGNAL() KWindowSystem.connectNotify()'''
        return SIGNAL()()
    showingDesktopChanged = pyqtSignal() # void showingDesktopChanged(bool) - signal
    windowChanged = pyqtSignal() # void windowChanged(WId,uint) - signal
    windowChanged = pyqtSignal() # void windowChanged(WId) - signal
    stackingOrderChanged = pyqtSignal() # void stackingOrderChanged() - signal
    strutChanged = pyqtSignal() # void strutChanged() - signal
    workAreaChanged = pyqtSignal() # void workAreaChanged() - signal
    numberOfDesktopsChanged = pyqtSignal() # void numberOfDesktopsChanged(int) - signal
    desktopNamesChanged = pyqtSignal() # void desktopNamesChanged() - signal
    activeWindowChanged = pyqtSignal() # void activeWindowChanged(WId) - signal
    windowRemoved = pyqtSignal() # void windowRemoved(WId) - signal
    windowAdded = pyqtSignal() # void windowAdded(WId) - signal
    currentDesktopChanged = pyqtSignal() # void currentDesktopChanged(int) - signal
    def constrainViewportRelativePosition(self, pos):
        '''static QPoint KWindowSystem.constrainViewportRelativePosition(QPoint pos)'''
        return QPoint()
    def desktopToViewport(self, desktop, absolute):
        '''static QPoint KWindowSystem.desktopToViewport(int desktop, bool absolute)'''
        return QPoint()
    def viewportWindowToDesktop(self, r):
        '''static int KWindowSystem.viewportWindowToDesktop(QRect r)'''
        return int()
    def viewportToDesktop(self, pos):
        '''static int KWindowSystem.viewportToDesktop(QPoint pos)'''
        return int()
    def mapViewport(self):
        '''static bool KWindowSystem.mapViewport()'''
        return bool()
    def doNotManage(self, title):
        '''static void KWindowSystem.doNotManage(QString title)'''
    def readNameProperty(self, window, atom):
        '''static QString KWindowSystem.readNameProperty(int window, int atom)'''
        return QString()
    def allowedActionsSupported(self):
        '''static bool KWindowSystem.allowedActionsSupported()'''
        return bool()
    def setStrut(self, win, left, right, top, bottom):
        '''static void KWindowSystem.setStrut(int win, int left, int right, int top, int bottom)'''
    def setExtendedStrut(self, win, left_width, left_start, left_end, right_width, right_start, right_end, top_width, top_start, top_end, bottom_width, bottom_start, bottom_end):
        '''static void KWindowSystem.setExtendedStrut(int win, int left_width, int left_start, int left_end, int right_width, int right_start, int right_end, int top_width, int top_start, int top_end, int bottom_width, int bottom_start, int bottom_end)'''
    def setUserTime(self, win, time):
        '''static void KWindowSystem.setUserTime(int win, int time)'''
    def showingDesktop(self):
        '''static bool KWindowSystem.showingDesktop()'''
        return bool()
    def setDesktopName(self, desktop, name):
        '''static void KWindowSystem.setDesktopName(int desktop, QString name)'''
    def desktopName(self, desktop):
        '''static QString KWindowSystem.desktopName(int desktop)'''
        return QString()
    def workArea(self, desktop = None):
        '''static QRect KWindowSystem.workArea(int desktop = -1)'''
        return QRect()
    def workArea(self, excludes, desktop = None):
        '''static QRect KWindowSystem.workArea(unknown-type excludes, int desktop = -1)'''
        return QRect()
    def icccmCompliantMappingState(self):
        '''static bool KWindowSystem.icccmCompliantMappingState()'''
        return bool()
    def lowerWindow(self, win):
        '''static void KWindowSystem.lowerWindow(int win)'''
    def raiseWindow(self, win):
        '''static void KWindowSystem.raiseWindow(int win)'''
    def unminimizeWindow(self, win, animation = True):
        '''static void KWindowSystem.unminimizeWindow(int win, bool animation = True)'''
    def minimizeWindow(self, win, animation = True):
        '''static void KWindowSystem.minimizeWindow(int win, bool animation = True)'''
    def clearState(self, win, state):
        '''static void KWindowSystem.clearState(int win, int state)'''
    def setState(self, win, state):
        '''static void KWindowSystem.setState(int win, int state)'''
    def setType(self, win, windowType):
        '''static void KWindowSystem.setType(int win, NET.WindowType windowType)'''
    def setIcons(self, win, icon, miniIcon):
        '''static void KWindowSystem.setIcons(int win, QPixmap icon, QPixmap miniIcon)'''
    def icon(self, win, width = None, height = None, scale = False):
        '''static QPixmap KWindowSystem.icon(int win, int width = -1, int height = -1, bool scale = False)'''
        return QPixmap()
    def icon(self, win, width, height, scale, flags):
        '''static QPixmap KWindowSystem.icon(int win, int width, int height, bool scale, int flags)'''
        return QPixmap()
    def groupLeader(self, window):
        '''static int KWindowSystem.groupLeader(int window)'''
        return int()
    def transientFor(self, window):
        '''static int KWindowSystem.transientFor(int window)'''
        return int()
    def setMainWindow(self, subwindow, mainwindow):
        '''static void KWindowSystem.setMainWindow(QWidget subwindow, int mainwindow)'''
    def setOnDesktop(self, win, desktop):
        '''static void KWindowSystem.setOnDesktop(int win, int desktop)'''
    def setOnAllDesktops(self, win, b):
        '''static void KWindowSystem.setOnAllDesktops(int win, bool b)'''
    def setCurrentDesktop(self, desktop):
        '''static void KWindowSystem.setCurrentDesktop(int desktop)'''
    def numberOfDesktops(self):
        '''static int KWindowSystem.numberOfDesktops()'''
        return int()
    def currentDesktop(self):
        '''static int KWindowSystem.currentDesktop()'''
        return int()
    def compositingActive(self):
        '''static bool KWindowSystem.compositingActive()'''
        return bool()
    def demandAttention(self, win, set = True):
        '''static void KWindowSystem.demandAttention(int win, bool set = True)'''
    def forceActiveWindow(self, win, time = 0):
        '''static void KWindowSystem.forceActiveWindow(int win, int time = 0)'''
    def activateWindow(self, win, time = 0):
        '''static void KWindowSystem.activateWindow(int win, int time = 0)'''
    def activeWindow(self):
        '''static int KWindowSystem.activeWindow()'''
        return int()
    def stackingOrder(self):
        '''static unknown-type KWindowSystem.stackingOrder()'''
        return unknown-type()
    def windowInfo(self, win, properties, properties2 = 0):
        '''static KWindowInfo KWindowSystem.windowInfo(int win, int properties, int properties2 = 0)'''
        return KWindowInfo()
    def hasWId(self, id):
        '''static bool KWindowSystem.hasWId(int id)'''
        return bool()
    def windows(self):
        '''static unknown-type KWindowSystem.windows()'''
        return unknown-type()
    def self(self):
        '''static KWindowSystem KWindowSystem.self()'''
        return KWindowSystem()


class KWordWrap():
    """"""
    FadeOut = None # int - member
    Truncate = None # int - member
    def drawTruncateText(self, p, x, y, maxW, t):
        '''static void KWordWrap.drawTruncateText(QPainter p, int x, int y, int maxW, QString t)'''
    def drawFadeoutText(self, p, x, y, maxW, t):
        '''static void KWordWrap.drawFadeoutText(QPainter p, int x, int y, int maxW, QString t)'''
    def drawText(self, painter, x, y, flags = None):
        '''void KWordWrap.drawText(QPainter painter, int x, int y, int flags = Qt.AlignLeft)'''
    def truncatedString(self, dots = True):
        '''QString KWordWrap.truncatedString(bool dots = True)'''
        return QString()
    def wrappedString(self):
        '''QString KWordWrap.wrappedString()'''
        return QString()
    def boundingRect(self):
        '''QRect KWordWrap.boundingRect()'''
        return QRect()
    def formatText(self, fm, r, flags, str, len = None):
        '''static KWordWrap KWordWrap.formatText(QFontMetrics fm, QRect r, int flags, QString str, int len = -1)'''
        return KWordWrap()


class KXMessages(QWidget):
    """"""
    def __init__(self, accept_broadcast, parent, obsolete):
        '''void KXMessages.__init__(str accept_broadcast, QWidget parent, bool obsolete)'''
    def __init__(self, accept_broadcast = None, parent = None):
        '''void KXMessages.__init__(str accept_broadcast = None, QWidget parent = None)'''
    gotMessage = pyqtSignal() # void gotMessage(const QStringamp;) - signal
    def broadcastMessageX(self, disp, msg_type, message, screen, obsolete):
        '''static bool KXMessages.broadcastMessageX(Display disp, str msg_type, QString message, int screen, bool obsolete)'''
        return bool()
    def broadcastMessageX(self, disp, msg_type, message):
        '''static bool KXMessages.broadcastMessageX(Display disp, str msg_type, QString message)'''
        return bool()
    def sendMessageX(self, disp, w, msg_type, message, obsolete):
        '''static bool KXMessages.sendMessageX(Display disp, int w, str msg_type, QString message, bool obsolete)'''
        return bool()
    def sendMessageX(self, disp, w, msg_type, message):
        '''static bool KXMessages.sendMessageX(Display disp, int w, str msg_type, QString message)'''
        return bool()
    def broadcastMessage(self, msg_type, message, screen, obsolete):
        '''void KXMessages.broadcastMessage(str msg_type, QString message, int screen, bool obsolete)'''
    def broadcastMessage(self, msg_type, message):
        '''void KXMessages.broadcastMessage(str msg_type, QString message)'''
    def sendMessage(self, w, msg_type, message, obsolete):
        '''void KXMessages.sendMessage(int w, str msg_type, QString message, bool obsolete)'''
    def sendMessage(self, w, msg_type, message):
        '''void KXMessages.sendMessage(int w, str msg_type, QString message)'''


class KXMLGUIBuilder():
    """"""
    def __init__(self, widget):
        '''void KXMLGUIBuilder.__init__(QWidget widget)'''
    def finalizeGUI(self, client):
        '''void KXMLGUIBuilder.finalizeGUI(KXMLGUIClient client)'''
    def removeCustomElement(self, parent, action):
        '''void KXMLGUIBuilder.removeCustomElement(QWidget parent, QAction action)'''
    def createCustomElement(self, parent, index, element):
        '''QAction KXMLGUIBuilder.createCustomElement(QWidget parent, int index, QDomElement element)'''
        return QAction()
    def customTags(self):
        '''QStringList KXMLGUIBuilder.customTags()'''
        return QStringList()
    def removeContainer(self, container, parent, element, containerAction):
        '''void KXMLGUIBuilder.removeContainer(QWidget container, QWidget parent, QDomElement element, QAction containerAction)'''
    def createContainer(self, parent, index, element):
        '''tuple KXMLGUIBuilder.createContainer(QWidget parent, int index, QDomElement element)'''
        return tuple()
    def containerTags(self):
        '''QStringList KXMLGUIBuilder.containerTags()'''
        return QStringList()
    def widget(self):
        '''QWidget KXMLGUIBuilder.widget()'''
        return QWidget()
    def setBuilderComponentData(self, componentData):
        '''void KXMLGUIBuilder.setBuilderComponentData(KComponentData componentData)'''
    def builderComponentData(self):
        '''KComponentData KXMLGUIBuilder.builderComponentData()'''
        return KComponentData()
    def setBuilderClient(self, client):
        '''void KXMLGUIBuilder.setBuilderClient(KXMLGUIClient client)'''
    def builderClient(self):
        '''KXMLGUIClient KXMLGUIBuilder.builderClient()'''
        return KXMLGUIClient()


class KXMLGUIClient():
    """"""
    # Enum KXMLGUIClient.ReverseStateChange
    StateNoReverse = 0
    StateReverse = 0

    def __init__(self):
        '''void KXMLGUIClient.__init__()'''
    def __init__(self, parent):
        '''void KXMLGUIClient.__init__(KXMLGUIClient parent)'''
    def loadStandardsXmlFile(self):
        '''void KXMLGUIClient.loadStandardsXmlFile()'''
    def replaceXMLFile(self, xmlfile, localxmlfile, merge = False):
        '''void KXMLGUIClient.replaceXMLFile(QString xmlfile, QString localxmlfile, bool merge = False)'''
    def stateChanged(self, newstate, reverse = None):
        '''void KXMLGUIClient.stateChanged(QString newstate, KXMLGUIClient.ReverseStateChange reverse = KXMLGUIClient.StateNoReverse)'''
    def setDOMDocument(self, document, merge = False):
        '''void KXMLGUIClient.setDOMDocument(QDomDocument document, bool merge = False)'''
    def setXML(self, document, merge = False):
        '''void KXMLGUIClient.setXML(QString document, bool merge = False)'''
    def setLocalXMLFile(self, file):
        '''void KXMLGUIClient.setLocalXMLFile(QString file)'''
    def setXMLFile(self, file, merge = False, setXMLDoc = True):
        '''void KXMLGUIClient.setXMLFile(QString file, bool merge = False, bool setXMLDoc = True)'''
    def setComponentData(self, componentData):
        '''void KXMLGUIClient.setComponentData(KComponentData componentData)'''
    def prepareXMLUnplug(self):
        '''QWidget KXMLGUIClient.prepareXMLUnplug()'''
        return QWidget()
    def endXMLPlug(self):
        '''void KXMLGUIClient.endXMLPlug()'''
    def beginXMLPlug(self):
        '''QWidget KXMLGUIClient.beginXMLPlug()'''
        return QWidget()
    def getActionsToChangeForState(self, state):
        '''KXMLGUIClient.StateChange KXMLGUIClient.getActionsToChangeForState(QString state)'''
        return KXMLGUIClient.StateChange()
    def addStateActionDisabled(self, state, action):
        '''void KXMLGUIClient.addStateActionDisabled(QString state, QString action)'''
    def addStateActionEnabled(self, state, action):
        '''void KXMLGUIClient.addStateActionEnabled(QString state, QString action)'''
    def findMostRecentXMLFile(self, files, doc):
        '''static QString KXMLGUIClient.findMostRecentXMLFile(QStringList files, QString doc)'''
        return QString()
    def unplugActionList(self, name):
        '''void KXMLGUIClient.unplugActionList(QString name)'''
    def plugActionList(self, name, actionList):
        '''void KXMLGUIClient.plugActionList(QString name, list-of-QAction actionList)'''
    def reloadXML(self):
        '''void KXMLGUIClient.reloadXML()'''
    def clientBuilder(self):
        '''KXMLGUIBuilder KXMLGUIClient.clientBuilder()'''
        return KXMLGUIBuilder()
    def setClientBuilder(self, builder):
        '''void KXMLGUIClient.setClientBuilder(KXMLGUIBuilder builder)'''
    def childClients(self):
        '''list-of-KXMLGUIClient KXMLGUIClient.childClients()'''
        return [KXMLGUIClient()]
    def removeChildClient(self, child):
        '''void KXMLGUIClient.removeChildClient(KXMLGUIClient child)'''
    def insertChildClient(self, child):
        '''void KXMLGUIClient.insertChildClient(KXMLGUIClient child)'''
    def parentClient(self):
        '''KXMLGUIClient KXMLGUIClient.parentClient()'''
        return KXMLGUIClient()
    def factory(self):
        '''KXMLGUIFactory KXMLGUIClient.factory()'''
        return KXMLGUIFactory()
    def setFactory(self, factory):
        '''void KXMLGUIClient.setFactory(KXMLGUIFactory factory)'''
    def xmlguiBuildDocument(self):
        '''QDomDocument KXMLGUIClient.xmlguiBuildDocument()'''
        return QDomDocument()
    def setXMLGUIBuildDocument(self, doc):
        '''void KXMLGUIClient.setXMLGUIBuildDocument(QDomDocument doc)'''
    def localXMLFile(self):
        '''QString KXMLGUIClient.localXMLFile()'''
        return QString()
    def xmlFile(self):
        '''QString KXMLGUIClient.xmlFile()'''
        return QString()
    def domDocument(self):
        '''QDomDocument KXMLGUIClient.domDocument()'''
        return QDomDocument()
    def componentData(self):
        '''KComponentData KXMLGUIClient.componentData()'''
        return KComponentData()
    def actionCollection(self):
        '''KActionCollection KXMLGUIClient.actionCollection()'''
        return KActionCollection()
    def action(self, name):
        '''QAction KXMLGUIClient.action(str name)'''
        return QAction()
    def action(self, element):
        '''QAction KXMLGUIClient.action(QDomElement element)'''
        return QAction()
    class StateChange():
        """"""
        actionsToDisable = None # QStringList - member
        actionsToEnable = None # QStringList - member
        def __init__(self):
            '''void KXMLGUIClient.StateChange.__init__()'''
        def __init__(self):
            '''KXMLGUIClient.StateChange KXMLGUIClient.StateChange.__init__()'''
            return KXMLGUIClient.StateChange()


class KXMLGUIFactory(QObject):
    """"""
    def __init__(self, builder, parent = None):
        '''void KXMLGUIFactory.__init__(KXMLGUIBuilder builder, QObject parent = None)'''
    makingChanges = pyqtSignal() # void makingChanges(bool) - signal
    clientRemoved = pyqtSignal() # void clientRemoved(KXMLGUIClient *) - signal
    clientAdded = pyqtSignal() # void clientAdded(KXMLGUIClient *) - signal
    def changeShortcutScheme(self, scheme):
        '''void KXMLGUIFactory.changeShortcutScheme(QString scheme)'''
    def configureShortcuts(self, bAllowLetterShortcuts = True, bSaveSettings = True):
        '''int KXMLGUIFactory.configureShortcuts(bool bAllowLetterShortcuts = True, bool bSaveSettings = True)'''
        return int()
    def refreshActionProperties(self):
        '''void KXMLGUIFactory.refreshActionProperties()'''
    def resetContainer(self, containerName, useTagName = False):
        '''void KXMLGUIFactory.resetContainer(QString containerName, bool useTagName = False)'''
    def reset(self):
        '''void KXMLGUIFactory.reset()'''
    def containers(self, tagName):
        '''list-of-QWidget KXMLGUIFactory.containers(QString tagName)'''
        return [QWidget()]
    def container(self, containerName, client, useTagName = False):
        '''QWidget KXMLGUIFactory.container(QString containerName, KXMLGUIClient client, bool useTagName = False)'''
        return QWidget()
    def clients(self):
        '''list-of-KXMLGUIClient KXMLGUIFactory.clients()'''
        return [KXMLGUIClient()]
    def unplugActionList(self, client, name):
        '''void KXMLGUIFactory.unplugActionList(KXMLGUIClient client, QString name)'''
    def plugActionList(self, client, name, actionList):
        '''void KXMLGUIFactory.plugActionList(KXMLGUIClient client, QString name, list-of-QAction actionList)'''
    def removeClient(self, client):
        '''void KXMLGUIFactory.removeClient(KXMLGUIClient client)'''
    def addClient(self, client):
        '''void KXMLGUIFactory.addClient(KXMLGUIClient client)'''
    def findActionByName(self, elem, sName, create):
        '''static QDomElement KXMLGUIFactory.findActionByName(QDomElement elem, QString sName, bool create)'''
        return QDomElement()
    def actionPropertiesElement(self, doc):
        '''static QDomElement KXMLGUIFactory.actionPropertiesElement(QDomDocument doc)'''
        return QDomElement()
    def saveConfigFile(self, doc, filename, componentData = KComponentData()):
        '''static bool KXMLGUIFactory.saveConfigFile(QDomDocument doc, QString filename, KComponentData componentData = KComponentData())'''
        return bool()
    def readConfigFile(self, filename, componentData = KComponentData()):
        '''static QString KXMLGUIFactory.readConfigFile(QString filename, KComponentData componentData = KComponentData())'''
        return QString()


class KXmlGuiWindow(KMainWindow, KXMLGUIBuilder, KXMLGUIClient):
    """"""
    # Enum KXmlGuiWindow.StandardWindowOption
    ToolBar = 0
    Keys = 0
    StatusBar = 0
    Save = 0
    Create = 0
    Default = 0

    def __init__(self, parent = None, f = 0):
        '''void KXmlGuiWindow.__init__(QWidget parent = None, Qt.WindowFlags f = 0)'''
    def saveNewToolbarConfig(self):
        '''void KXmlGuiWindow.saveNewToolbarConfig()'''
    def event(self, event):
        '''bool KXmlGuiWindow.event(QEvent event)'''
        return bool()
    def slotStateChanged(self, newstate):
        '''void KXmlGuiWindow.slotStateChanged(QString newstate)'''
    def slotStateChanged(self, newstate, reverse):
        '''void KXmlGuiWindow.slotStateChanged(QString newstate, bool reverse)'''
    def configureToolbars(self):
        '''void KXmlGuiWindow.configureToolbars()'''
    def applyMainWindowSettings(self, config, force = False):
        '''void KXmlGuiWindow.applyMainWindowSettings(KConfigGroup config, bool force = False)'''
    def finalizeGUI(self, client):
        '''void KXmlGuiWindow.finalizeGUI(KXMLGUIClient client)'''
    def finalizeGUI(self, force):
        '''void KXmlGuiWindow.finalizeGUI(bool force)'''
    def setupToolbarMenuActions(self):
        '''void KXmlGuiWindow.setupToolbarMenuActions()'''
    def toolBarMenuAction(self):
        '''QAction KXmlGuiWindow.toolBarMenuAction()'''
        return QAction()
    def setupGUI(self, options = None, xmlfile = QString()):
        '''void KXmlGuiWindow.setupGUI(KXmlGuiWindow.StandardWindowOptions options = KXmlGuiWindow.Default, QString xmlfile = QString())'''
    def setupGUI(self, defaultSize, options = None, xmlfile = QString()):
        '''void KXmlGuiWindow.setupGUI(QSize defaultSize, KXmlGuiWindow.StandardWindowOptions options = KXmlGuiWindow.Default, QString xmlfile = QString())'''
    def createStandardStatusBarAction(self):
        '''void KXmlGuiWindow.createStandardStatusBarAction()'''
    def isStandardToolBarMenuEnabled(self):
        '''bool KXmlGuiWindow.isStandardToolBarMenuEnabled()'''
        return bool()
    def setStandardToolBarMenuEnabled(self, enable):
        '''void KXmlGuiWindow.setStandardToolBarMenuEnabled(bool enable)'''
    def createGUI(self, xmlfile = QString()):
        '''void KXmlGuiWindow.createGUI(QString xmlfile = QString())'''
    def guiFactory(self):
        '''KXMLGUIFactory KXmlGuiWindow.guiFactory()'''
        return KXMLGUIFactory()
    def isHelpMenuEnabled(self):
        '''bool KXmlGuiWindow.isHelpMenuEnabled()'''
        return bool()
    def setHelpMenuEnabled(self, showHelpMenu = True):
        '''void KXmlGuiWindow.setHelpMenuEnabled(bool showHelpMenu = True)'''
    class StandardWindowOptions():
        """"""
        def __init__(self):
            '''KXmlGuiWindow.StandardWindowOptions KXmlGuiWindow.StandardWindowOptions.__init__()'''
            return KXmlGuiWindow.StandardWindowOptions()
        def __init__(self):
            '''int KXmlGuiWindow.StandardWindowOptions.__init__()'''
            return int()
        def __init__(self):
            '''void KXmlGuiWindow.StandardWindowOptions.__init__()'''
        def __bool__(self):
            '''int KXmlGuiWindow.StandardWindowOptions.__bool__()'''
            return int()
        def __ne__(self, f):
            '''bool KXmlGuiWindow.StandardWindowOptions.__ne__(KXmlGuiWindow.StandardWindowOptions f)'''
            return bool()
        def __eq__(self, f):
            '''bool KXmlGuiWindow.StandardWindowOptions.__eq__(KXmlGuiWindow.StandardWindowOptions f)'''
            return bool()
        def __invert__(self):
            '''KXmlGuiWindow.StandardWindowOptions KXmlGuiWindow.StandardWindowOptions.__invert__()'''
            return KXmlGuiWindow.StandardWindowOptions()
        def __and__(self, mask):
            '''KXmlGuiWindow.StandardWindowOptions KXmlGuiWindow.StandardWindowOptions.__and__(int mask)'''
            return KXmlGuiWindow.StandardWindowOptions()
        def __xor__(self, f):
            '''KXmlGuiWindow.StandardWindowOptions KXmlGuiWindow.StandardWindowOptions.__xor__(KXmlGuiWindow.StandardWindowOptions f)'''
            return KXmlGuiWindow.StandardWindowOptions()
        def __xor__(self, f):
            '''KXmlGuiWindow.StandardWindowOptions KXmlGuiWindow.StandardWindowOptions.__xor__(int f)'''
            return KXmlGuiWindow.StandardWindowOptions()
        def __or__(self, f):
            '''KXmlGuiWindow.StandardWindowOptions KXmlGuiWindow.StandardWindowOptions.__or__(KXmlGuiWindow.StandardWindowOptions f)'''
            return KXmlGuiWindow.StandardWindowOptions()
        def __or__(self, f):
            '''KXmlGuiWindow.StandardWindowOptions KXmlGuiWindow.StandardWindowOptions.__or__(int f)'''
            return KXmlGuiWindow.StandardWindowOptions()
        def __int__(self):
            '''int KXmlGuiWindow.StandardWindowOptions.__int__()'''
            return int()
        def __ixor__(self, f):
            '''KXmlGuiWindow.StandardWindowOptions KXmlGuiWindow.StandardWindowOptions.__ixor__(KXmlGuiWindow.StandardWindowOptions f)'''
            return KXmlGuiWindow.StandardWindowOptions()
        def __ior__(self, f):
            '''KXmlGuiWindow.StandardWindowOptions KXmlGuiWindow.StandardWindowOptions.__ior__(KXmlGuiWindow.StandardWindowOptions f)'''
            return KXmlGuiWindow.StandardWindowOptions()
        def __iand__(self, mask):
            '''KXmlGuiWindow.StandardWindowOptions KXmlGuiWindow.StandardWindowOptions.__iand__(int mask)'''
            return KXmlGuiWindow.StandardWindowOptions()


class KXUtils():
    """"""
    def timestampDiff(self, time1, time2):
        '''static int KXUtils.timestampDiff(int time1, int time2)'''
        return int()
    def timestampCompare(self, time1, time2):
        '''static int KXUtils.timestampCompare(int time1, int time2)'''
        return int()
    def createPixmapFromHandle(self, pixmap, mask = 0):
        '''static QPixmap KXUtils.createPixmapFromHandle(int pixmap, int mask = 0)'''
        return QPixmap()


class KRatingPainter():
    """"""
    def __init__(self):
        '''void KRatingPainter.__init__()'''
    def getRatingFromPosition(self, rect, align, direction, pos):
        '''static int KRatingPainter.getRatingFromPosition(QRect rect, Qt.Alignment align, Qt.LayoutDirection direction, QPoint pos)'''
        return int()
    def paintRating(self, p, rect, align, rating, hoverRating = None):
        '''static void KRatingPainter.paintRating(QPainter p, QRect rect, Qt.Alignment align, int rating, int hoverRating = -1)'''
    def ratingFromPosition(self, rect, pos):
        '''int KRatingPainter.ratingFromPosition(QRect rect, QPoint pos)'''
        return int()
    def paint(self, painter, rect, rating, hoverRating = None):
        '''void KRatingPainter.paint(QPainter painter, QRect rect, int rating, int hoverRating = -1)'''
    def setSpacing(self, spacing):
        '''void KRatingPainter.setSpacing(int spacing)'''
    def setCustomPixmap(self, pixmap):
        '''void KRatingPainter.setCustomPixmap(QPixmap pixmap)'''
    def setEnabled(self, enabled):
        '''void KRatingPainter.setEnabled(bool enabled)'''
    def setIcon(self, icon):
        '''void KRatingPainter.setIcon(QIcon icon)'''
    def setLayoutDirection(self, direction):
        '''void KRatingPainter.setLayoutDirection(Qt.LayoutDirection direction)'''
    def setAlignment(self, align):
        '''void KRatingPainter.setAlignment(Qt.Alignment align)'''
    def setHalfStepsEnabled(self, enabled):
        '''void KRatingPainter.setHalfStepsEnabled(bool enabled)'''
    def setMaxRating(self, max):
        '''void KRatingPainter.setMaxRating(int max)'''
    def spacing(self):
        '''int KRatingPainter.spacing()'''
        return int()
    def customPixmap(self):
        '''QPixmap KRatingPainter.customPixmap()'''
        return QPixmap()
    def isEnabled(self):
        '''bool KRatingPainter.isEnabled()'''
        return bool()
    def icon(self):
        '''QIcon KRatingPainter.icon()'''
        return QIcon()
    def layoutDirection(self):
        '''Qt.LayoutDirection KRatingPainter.layoutDirection()'''
        return Qt.LayoutDirection()
    def alignment(self):
        '''Qt.Alignment KRatingPainter.alignment()'''
        return Qt.Alignment()
    def halfStepsEnabled(self):
        '''bool KRatingPainter.halfStepsEnabled()'''
        return bool()
    def maxRating(self):
        '''int KRatingPainter.maxRating()'''
        return int()


class KRatingWidget(QFrame):
    """"""
    def __init__(self, parent = None):
        '''void KRatingWidget.__init__(QWidget parent = None)'''
    def resizeEvent(self, e):
        '''void KRatingWidget.resizeEvent(QResizeEvent e)'''
    def paintEvent(self, e):
        '''void KRatingWidget.paintEvent(QPaintEvent e)'''
    def leaveEvent(self, e):
        '''void KRatingWidget.leaveEvent(QEvent e)'''
    def mouseMoveEvent(self, e):
        '''void KRatingWidget.mouseMoveEvent(QMouseEvent e)'''
    def mousePressEvent(self, e):
        '''void KRatingWidget.mousePressEvent(QMouseEvent e)'''
    def setPixmapSize(self, size):
        '''void KRatingWidget.setPixmapSize(int size)'''
    def setPixmap(self):
        '''QPixmap KRatingWidget.setPixmap()'''
        return QPixmap()
    def setCustomPixmap(self, pixmap):
        '''void KRatingWidget.setCustomPixmap(QPixmap pixmap)'''
    def setIcon(self, icon):
        '''void KRatingWidget.setIcon(QIcon icon)'''
    def setLayoutDirection(self, direction):
        '''void KRatingWidget.setLayoutDirection(Qt.LayoutDirection direction)'''
    def setAlignment(self, align):
        '''void KRatingWidget.setAlignment(Qt.Alignment align)'''
    def setSpacing(self):
        '''int KRatingWidget.setSpacing()'''
        return int()
    def setOnlyPaintFullSteps(self):
        '''bool KRatingWidget.setOnlyPaintFullSteps()'''
        return bool()
    def setHalfStepsEnabled(self, enabled):
        '''void KRatingWidget.setHalfStepsEnabled(bool enabled)'''
    def setMaxRating(self, max):
        '''void KRatingWidget.setMaxRating(int max)'''
    def setRating(self, rating):
        '''void KRatingWidget.setRating(int rating)'''
    ratingChanged = pyqtSignal() # void ratingChanged(int) - signal
    def icon(self):
        '''QIcon KRatingWidget.icon()'''
        return QIcon()
    def halfStepsEnabled(self):
        '''bool KRatingWidget.halfStepsEnabled()'''
        return bool()
    def sizeHint(self):
        '''QSize KRatingWidget.sizeHint()'''
        return QSize()
    def spacing(self):
        '''int KRatingWidget.spacing()'''
        return int()
    def layoutDirection(self):
        '''Qt.LayoutDirection KRatingWidget.layoutDirection()'''
        return Qt.LayoutDirection()
    def alignment(self):
        '''Qt.Alignment KRatingWidget.alignment()'''
        return Qt.Alignment()
    def maxRating(self):
        '''int KRatingWidget.maxRating()'''
        return int()
    def rating(self):
        '''int KRatingWidget.rating()'''
        return int()


class NETRootInfo(NET):
    """"""
    PROTOCOLS = None # int - member
    WINDOW_TYPES = None # int - member
    STATES = None # int - member
    PROTOCOLS2 = None # int - member
    ACTIONS = None # int - member
    PROPERTIES_SIZE = None # int - member
    def __init__(self, display, supportWindow, wmName, properties, screen = None, doACtivate = True):
        '''void NETRootInfo.__init__(Display display, int supportWindow, str wmName, list properties, int screen = -1, bool doACtivate = True)'''
    def __init__(self, display, properties, screen = None, doActivate = True):
        '''void NETRootInfo.__init__(Display display, list properties, int screen = -1, bool doActivate = True)'''
    def __init__(self, display, properties, screen = None, doActivate = True):
        '''void NETRootInfo.__init__(Display display, int properties, int screen = -1, bool doActivate = True)'''
    def __init__(self, rootinfo):
        '''void NETRootInfo.__init__(NETRootInfo rootinfo)'''
    def setSupported(self, property, on = True):
        '''void NETRootInfo.setSupported(NET.Property property, bool on = True)'''
    def setSupported(self, property, on = True):
        '''void NETRootInfo.setSupported(NET.Property2 property, bool on = True)'''
    def setSupported(self, property, on = True):
        '''void NETRootInfo.setSupported(NET.WindowType property, bool on = True)'''
    def setSupported(self, property, on = True):
        '''void NETRootInfo.setSupported(NET.State property, bool on = True)'''
    def setSupported(self, property, on = True):
        '''void NETRootInfo.setSupported(NET.Action property, bool on = True)'''
    def changeShowingDesktop(self, showing):
        '''void NETRootInfo.changeShowingDesktop(bool showing)'''
    def gotTakeActivity(self, window, timestamp, flags):
        '''void NETRootInfo.gotTakeActivity(int window, int timestamp, int flags)'''
    def restackWindow(self, window, source, above, detail, timestamp):
        '''void NETRootInfo.restackWindow(int window, NET.RequestSource source, int above, int detail, int timestamp)'''
    def moveResizeWindow(self, window, flags, x, y, width, height):
        '''void NETRootInfo.moveResizeWindow(int window, int flags, int x, int y, int width, int height)'''
    def changeActiveWindow(self, window, src, timestamp, active_window):
        '''void NETRootInfo.changeActiveWindow(int window, NET.RequestSource src, int timestamp, int active_window)'''
    def gotPing(self, window, timestamp):
        '''void NETRootInfo.gotPing(int window, int timestamp)'''
    def moveResize(self, window, x_root, y_root, direction):
        '''void NETRootInfo.moveResize(int window, int x_root, int y_root, int direction)'''
    def closeWindow(self, window):
        '''void NETRootInfo.closeWindow(int window)'''
    def changeCurrentDesktop(self, desktop):
        '''void NETRootInfo.changeCurrentDesktop(int desktop)'''
    def changeDesktopViewport(self, desktop, viewport):
        '''void NETRootInfo.changeDesktopViewport(int desktop, NETPoint viewport)'''
    def changeDesktopGeometry(self, desktop, geom):
        '''void NETRootInfo.changeDesktopGeometry(int desktop, NETSize geom)'''
    def changeNumberOfDesktops(self, numberOfDesktops):
        '''void NETRootInfo.changeNumberOfDesktops(int numberOfDesktops)'''
    def removeClient(self, window):
        '''void NETRootInfo.removeClient(int window)'''
    def addClient(self, window):
        '''void NETRootInfo.addClient(int window)'''
    def takeActivity(self, window, timestamp, flags):
        '''void NETRootInfo.takeActivity(int window, int timestamp, int flags)'''
    def sendPing(self, window, timestamp):
        '''void NETRootInfo.sendPing(int window, int timestamp)'''
    def restackRequest(self, window, source, above, detail, timestamp):
        '''void NETRootInfo.restackRequest(int window, NET.RequestSource source, int above, int detail, int timestamp)'''
    def moveResizeWindowRequest(self, window, flags, x, y, width, height):
        '''void NETRootInfo.moveResizeWindowRequest(int window, int flags, int x, int y, int width, int height)'''
    def moveResizeRequest(self, window, x_root, y_root, direction):
        '''void NETRootInfo.moveResizeRequest(int window, int x_root, int y_root, NET.Direction direction)'''
    def closeWindowRequest(self, window):
        '''void NETRootInfo.closeWindowRequest(int window)'''
    def showingDesktop(self):
        '''bool NETRootInfo.showingDesktop()'''
        return bool()
    def setShowingDesktop(self, showing):
        '''void NETRootInfo.setShowingDesktop(bool showing)'''
    def setDesktopLayout(self, orientation, columns, rows, corner):
        '''void NETRootInfo.setDesktopLayout(NET.Orientation orientation, int columns, int rows, NET.DesktopLayoutCorner corner)'''
    def setVirtualRoots(self, windows, count):
        '''void NETRootInfo.setVirtualRoots(int windows, int count)'''
    def setWorkArea(self, desktop, workArea):
        '''void NETRootInfo.setWorkArea(int desktop, NETRect workArea)'''
    def setActiveWindow(self, window, src, timestamp, active_window):
        '''void NETRootInfo.setActiveWindow(int window, NET.RequestSource src, int timestamp, int active_window)'''
    def setActiveWindow(self, window):
        '''void NETRootInfo.setActiveWindow(int window)'''
    def setDesktopName(self, desktop, desktopName):
        '''void NETRootInfo.setDesktopName(int desktop, str desktopName)'''
    def setNumberOfDesktops(self, numberOfDesktops):
        '''void NETRootInfo.setNumberOfDesktops(int numberOfDesktops)'''
    def setDesktopViewport(self, desktop, viewport):
        '''void NETRootInfo.setDesktopViewport(int desktop, NETPoint viewport)'''
    def setDesktopGeometry(self, desktop, geometry):
        '''void NETRootInfo.setDesktopGeometry(int desktop, NETSize geometry)'''
    def setCurrentDesktop(self, desktop, ignore_viewport = False):
        '''void NETRootInfo.setCurrentDesktop(int desktop, bool ignore_viewport = False)'''
    def setClientListStacking(self, windows, count):
        '''void NETRootInfo.setClientListStacking(int windows, int count)'''
    def setClientList(self, windows, count):
        '''void NETRootInfo.setClientList(int windows, int count)'''
    def activate(self):
        '''void NETRootInfo.activate()'''
    def activeWindow(self):
        '''int NETRootInfo.activeWindow()'''
        return int()
    def currentDesktop(self, ignore_viewport = False):
        '''int NETRootInfo.currentDesktop(bool ignore_viewport = False)'''
        return int()
    def numberOfDesktops(self, ignore_viewport = False):
        '''int NETRootInfo.numberOfDesktops(bool ignore_viewport = False)'''
        return int()
    def desktopLayoutCorner(self):
        '''NET.DesktopLayoutCorner NETRootInfo.desktopLayoutCorner()'''
        return NET.DesktopLayoutCorner()
    def desktopLayoutColumnsRows(self):
        '''QSize NETRootInfo.desktopLayoutColumnsRows()'''
        return QSize()
    def desktopLayoutOrientation(self):
        '''NET.Orientation NETRootInfo.desktopLayoutOrientation()'''
        return NET.Orientation()
    def virtualRootsCount(self):
        '''int NETRootInfo.virtualRootsCount()'''
        return int()
    def desktopName(self, desktop):
        '''str NETRootInfo.desktopName(int desktop)'''
        return str()
    def workArea(self, desktop):
        '''NETRect NETRootInfo.workArea(int desktop)'''
        return NETRect()
    def desktopViewport(self, desktop):
        '''NETPoint NETRootInfo.desktopViewport(int desktop)'''
        return NETPoint()
    def desktopGeometry(self, desktop):
        '''NETSize NETRootInfo.desktopGeometry(int desktop)'''
        return NETSize()
    def clientListStackingCount(self):
        '''int NETRootInfo.clientListStackingCount()'''
        return int()
    def clientListCount(self):
        '''int NETRootInfo.clientListCount()'''
        return int()
    def isSupported(self, property):
        '''bool NETRootInfo.isSupported(NET.Property property)'''
        return bool()
    def isSupported(self, property):
        '''bool NETRootInfo.isSupported(NET.Property2 property)'''
        return bool()
    def isSupported(self, type):
        '''bool NETRootInfo.isSupported(NET.WindowType type)'''
        return bool()
    def isSupported(self, state):
        '''bool NETRootInfo.isSupported(NET.State state)'''
        return bool()
    def isSupported(self, action):
        '''bool NETRootInfo.isSupported(NET.Action action)'''
        return bool()
    def screenNumber(self):
        '''int NETRootInfo.screenNumber()'''
        return int()
    def wmName(self):
        '''str NETRootInfo.wmName()'''
        return str()
    def supportWindow(self):
        '''int NETRootInfo.supportWindow()'''
        return int()
    def rootWindow(self):
        '''int NETRootInfo.rootWindow()'''
        return int()
    def x11Display(self):
        '''Display NETRootInfo.x11Display()'''
        return Display()


class NETWinInfo(NET):
    """"""
    PROTOCOLS = None # int - member
    PROTOCOLS2 = None # int - member
    PROPERTIES_SIZE = None # int - member
    OnAllDesktops = None # int - member
    def __init__(self, display, window, rootWindow, properties, role = None):
        '''void NETWinInfo.__init__(Display display, int window, int rootWindow, list properties, NET.Role role = NET.Client)'''
    def __init__(self, display, window, rootWindow, properties, role = None):
        '''void NETWinInfo.__init__(Display display, int window, int rootWindow, int properties, NET.Role role = NET.Client)'''
    def __init__(self, wininfo):
        '''void NETWinInfo.__init__(NETWinInfo wininfo)'''
    def isBlockingCompositing(self):
        '''bool NETWinInfo.isBlockingCompositing()'''
        return bool()
    def setBlockingCompositing(self, active):
        '''void NETWinInfo.setBlockingCompositing(bool active)'''
    def activities(self):
        '''str NETWinInfo.activities()'''
        return str()
    def frameOverlap(self):
        '''NETStrut NETWinInfo.frameOverlap()'''
        return NETStrut()
    def setFrameOverlap(self, strut):
        '''void NETWinInfo.setFrameOverlap(NETStrut strut)'''
    def changeState(self, state, mask):
        '''void NETWinInfo.changeState(int state, int mask)'''
    def changeDesktop(self, desktop):
        '''void NETWinInfo.changeDesktop(int desktop)'''
    def kdeGeometry(self, frame, window):
        '''void NETWinInfo.kdeGeometry(NETRect frame, NETRect window)'''
    def clientMachine(self):
        '''str NETWinInfo.clientMachine()'''
        return str()
    def windowRole(self):
        '''str NETWinInfo.windowRole()'''
        return str()
    def windowClassName(self):
        '''str NETWinInfo.windowClassName()'''
        return str()
    def windowClassClass(self):
        '''str NETWinInfo.windowClassClass()'''
        return str()
    def groupLeader(self):
        '''int NETWinInfo.groupLeader()'''
        return int()
    def transientFor(self):
        '''int NETWinInfo.transientFor()'''
        return int()
    def allowedActions(self):
        '''int NETWinInfo.allowedActions()'''
        return int()
    def setAllowedActions(self, actions):
        '''void NETWinInfo.setAllowedActions(int actions)'''
    def opacity(self):
        '''int NETWinInfo.opacity()'''
        return int()
    def setOpacity(self, opacity):
        '''void NETWinInfo.setOpacity(int opacity)'''
    def startupId(self):
        '''str NETWinInfo.startupId()'''
        return str()
    def setStartupId(self, startup_id):
        '''void NETWinInfo.setStartupId(str startup_id)'''
    def userTime(self):
        '''int NETWinInfo.userTime()'''
        return int()
    def setUserTime(self, time):
        '''void NETWinInfo.setUserTime(int time)'''
    def setFrameExtents(self, strut):
        '''void NETWinInfo.setFrameExtents(NETStrut strut)'''
    def setHandledIcons(self, handled):
        '''void NETWinInfo.setHandledIcons(bool handled)'''
    def setPid(self, pid):
        '''void NETWinInfo.setPid(int pid)'''
    def setDesktop(self, desktop, ignore_viewport = False):
        '''void NETWinInfo.setDesktop(int desktop, bool ignore_viewport = False)'''
    def setVisibleIconName(self, name):
        '''void NETWinInfo.setVisibleIconName(str name)'''
    def setIconName(self, name):
        '''void NETWinInfo.setIconName(str name)'''
    def setVisibleName(self, visibleName):
        '''void NETWinInfo.setVisibleName(str visibleName)'''
    def setName(self, name):
        '''void NETWinInfo.setName(str name)'''
    def setWindowType(self, type):
        '''void NETWinInfo.setWindowType(NET.WindowType type)'''
    def setState(self, state, mask):
        '''void NETWinInfo.setState(int state, int mask)'''
    def setStrut(self, strut):
        '''void NETWinInfo.setStrut(NETStrut strut)'''
    def setExtendedStrut(self, extended_strut):
        '''void NETWinInfo.setExtendedStrut(NETExtendedStrut extended_strut)'''
    def setIconGeometry(self, geometry):
        '''void NETWinInfo.setIconGeometry(NETRect geometry)'''
    def mappingState(self):
        '''NET.MappingState NETWinInfo.mappingState()'''
        return NET.MappingState()
    def handledIcons(self):
        '''bool NETWinInfo.handledIcons()'''
        return bool()
    def pid(self):
        '''int NETWinInfo.pid()'''
        return int()
    def desktop(self, ignore_viewport = False):
        '''int NETWinInfo.desktop(bool ignore_viewport = False)'''
        return int()
    def visibleIconName(self):
        '''str NETWinInfo.visibleIconName()'''
        return str()
    def iconName(self):
        '''str NETWinInfo.iconName()'''
        return str()
    def visibleName(self):
        '''str NETWinInfo.visibleName()'''
        return str()
    def name(self):
        '''str NETWinInfo.name()'''
        return str()
    def hasWindowType(self):
        '''bool NETWinInfo.hasWindowType()'''
        return bool()
    def windowType(self, supported_types):
        '''NET.WindowType NETWinInfo.windowType(int supported_types)'''
        return NET.WindowType()
    def strut(self):
        '''NETStrut NETWinInfo.strut()'''
        return NETStrut()
    def extendedStrut(self):
        '''NETExtendedStrut NETWinInfo.extendedStrut()'''
        return NETExtendedStrut()
    def state(self):
        '''int NETWinInfo.state()'''
        return int()
    def iconGeometry(self):
        '''NETRect NETWinInfo.iconGeometry()'''
        return NETRect()
    def hasNETSupport(self):
        '''bool NETWinInfo.hasNETSupport()'''
        return bool()


class NETPoint():
    """"""
    x = None # int - member
    y = None # int - member
    def __init__(self):
        '''void NETPoint.__init__()'''
    def __init__(self):
        '''NETPoint NETPoint.__init__()'''
        return NETPoint()


class NETSize():
    """"""
    height = None # int - member
    width = None # int - member
    def __init__(self):
        '''void NETSize.__init__()'''
    def __init__(self):
        '''NETSize NETSize.__init__()'''
        return NETSize()


class NETRect():
    """"""
    pos = None # NETPoint - member
    size = None # NETSize - member
    def __init__(self):
        '''void NETRect.__init__()'''
    def __init__(self):
        '''NETRect NETRect.__init__()'''
        return NETRect()


class NETIcon():
    """"""
    data = None # str - member
    size = None # NETSize - member
    def __init__(self):
        '''void NETIcon.__init__()'''
    def __init__(self):
        '''NETIcon NETIcon.__init__()'''
        return NETIcon()


class NETExtendedStrut():
    """"""
    bottom_end = None # int - member
    bottom_start = None # int - member
    bottom_width = None # int - member
    left_end = None # int - member
    left_start = None # int - member
    left_width = None # int - member
    right_end = None # int - member
    right_start = None # int - member
    right_width = None # int - member
    top_end = None # int - member
    top_start = None # int - member
    top_width = None # int - member
    def __init__(self):
        '''void NETExtendedStrut.__init__()'''
    def __init__(self):
        '''NETExtendedStrut NETExtendedStrut.__init__()'''
        return NETExtendedStrut()


class NETStrut():
    """"""
    bottom = None # int - member
    left = None # int - member
    right = None # int - member
    top = None # int - member
    def __init__(self):
        '''void NETStrut.__init__()'''
    def __init__(self):
        '''NETStrut NETStrut.__init__()'''
        return NETStrut()


class NETFullscreenMonitors():
    """"""
    bottom = None # int - member
    left = None # int - member
    right = None # int - member
    top = None # int - member
    def __init__(self):
        '''void NETFullscreenMonitors.__init__()'''
    def __init__(self):
        '''NETFullscreenMonitors NETFullscreenMonitors.__init__()'''
        return NETFullscreenMonitors()
    def isSet(self):
        '''bool NETFullscreenMonitors.isSet()'''
        return bool()


class Sonnet():
    """"""
    class ConfigWidget(QWidget):
        """"""
        def __init__(self, config, parent):
            '''void Sonnet.ConfigWidget.__init__(KConfig config, QWidget parent)'''
        configChanged = pyqtSignal() # void configChanged() - signal
        def slotChanged(self):
            '''void Sonnet.ConfigWidget.slotChanged()'''
        def slotDefault(self):
            '''void Sonnet.ConfigWidget.slotDefault()'''
        def setBackgroundCheckingButtonShown(self):
            '''bool Sonnet.ConfigWidget.setBackgroundCheckingButtonShown()'''
            return bool()
        def save(self):
            '''void Sonnet.ConfigWidget.save()'''
        def language(self):
            '''QString Sonnet.ConfigWidget.language()'''
            return QString()
        def setLanguage(self, language):
            '''void Sonnet.ConfigWidget.setLanguage(QString language)'''
        def backgroundCheckingButtonShown(self):
            '''bool Sonnet.ConfigWidget.backgroundCheckingButtonShown()'''
            return bool()
    class Dialog(KDialog):
        """"""
        def __init__(self, checker, parent):
            '''void Sonnet.Dialog.__init__(Sonnet.BackgroundChecker checker, QWidget parent)'''
        def setSpellCheckContinuedAfterReplacement(self, b):
            '''void Sonnet.Dialog.setSpellCheckContinuedAfterReplacement(bool b)'''
        def showSpellCheckCompletionMessage(self, b = True):
            '''void Sonnet.Dialog.showSpellCheckCompletionMessage(bool b = True)'''
        def showProgressDialog(self, timeout = 500):
            '''void Sonnet.Dialog.showProgressDialog(int timeout = 500)'''
        languageChanged = pyqtSignal() # void languageChanged(const QStringamp;) - signal
        spellCheckStatus = pyqtSignal() # void spellCheckStatus(const QStringamp;) - signal
        autoCorrect = pyqtSignal() # void autoCorrect(const QStringamp;,const QStringamp;) - signal
        cancel = pyqtSignal() # void cancel() - signal
        stop = pyqtSignal() # void stop() - signal
        replace = pyqtSignal() # void replace(const QStringamp;,int,const QStringamp;) - signal
        misspelling = pyqtSignal() # void misspelling(const QStringamp;,int) - signal
        done = pyqtSignal() # void done(const QStringamp;) - signal
        def setBuffer(self):
            '''QString Sonnet.Dialog.setBuffer()'''
            return QString()
        def activeAutoCorrect(self, _active):
            '''void Sonnet.Dialog.activeAutoCorrect(bool _active)'''
        def show(self):
            '''void Sonnet.Dialog.show()'''
        def buffer(self):
            '''QString Sonnet.Dialog.buffer()'''
            return QString()
        def originalBuffer(self):
            '''QString Sonnet.Dialog.originalBuffer()'''
            return QString()
    class ConfigDialog(KDialog):
        """"""
        def __init__(self, config, parent):
            '''void Sonnet.ConfigDialog.__init__(KConfig config, QWidget parent)'''
        configChanged = pyqtSignal() # void configChanged() - signal
        def language(self):
            '''QString Sonnet.ConfigDialog.language()'''
            return QString()
        languageChanged = pyqtSignal() # void languageChanged(const QStringamp;) - signal
        def slotApply(self):
            '''void Sonnet.ConfigDialog.slotApply()'''
        def slotOk(self):
            '''void Sonnet.ConfigDialog.slotOk()'''
        def setLanguage(self, language):
            '''void Sonnet.ConfigDialog.setLanguage(QString language)'''
    class DictionaryComboBox(KComboBox):
        """"""
        def __init__(self, parent = None):
            '''void Sonnet.DictionaryComboBox.__init__(QWidget parent = None)'''
        dictionaryNameChanged = pyqtSignal() # void dictionaryNameChanged(const QStringamp;) - signal
        dictionaryChanged = pyqtSignal() # void dictionaryChanged(const QStringamp;) - signal
        def setCurrentByDictionary(self, dictionary):
            '''void Sonnet.DictionaryComboBox.setCurrentByDictionary(QString dictionary)'''
        def setCurrentByDictionaryName(self, dictionaryName):
            '''void Sonnet.DictionaryComboBox.setCurrentByDictionaryName(QString dictionaryName)'''
        def currentDictionary(self):
            '''QString Sonnet.DictionaryComboBox.currentDictionary()'''
            return QString()
        def currentDictionaryName(self):
            '''QString Sonnet.DictionaryComboBox.currentDictionaryName()'''
            return QString()
        def reloadCombo(self):
            '''void Sonnet.DictionaryComboBox.reloadCombo()'''
    class Highlighter(QSyntaxHighlighter):
        """"""
        def __init__(self, textEdit, configFile = QString(), col = QColor()):
            '''void Sonnet.Highlighter.__init__(QTextEdit textEdit, QString configFile = QString(), QColor col = QColor())'''
        def checkerEnabledByDefault(self):
            '''bool Sonnet.Highlighter.checkerEnabledByDefault()'''
            return bool()
        def slotRehighlight(self):
            '''void Sonnet.Highlighter.slotRehighlight()'''
        def slotAutoDetection(self):
            '''void Sonnet.Highlighter.slotAutoDetection()'''
        def setIntraWordEditing(self, editing):
            '''void Sonnet.Highlighter.setIntraWordEditing(bool editing)'''
        def intraWordEditing(self):
            '''bool Sonnet.Highlighter.intraWordEditing()'''
            return bool()
        def eventFilter(self, o, e):
            '''bool Sonnet.Highlighter.eventFilter(QObject o, QEvent e)'''
            return bool()
        def unsetMisspelled(self, start, count):
            '''void Sonnet.Highlighter.unsetMisspelled(int start, int count)'''
        def setMisspelled(self, start, count):
            '''void Sonnet.Highlighter.setMisspelled(int start, int count)'''
        def highlightBlock(self, text):
            '''void Sonnet.Highlighter.highlightBlock(QString text)'''
        newSuggestions = pyqtSignal() # void newSuggestions(const QStringamp;,const QStringListamp;) - signal
        activeChanged = pyqtSignal() # void activeChanged(const QStringamp;) - signal
        def setMisspelledColor(self, color):
            '''void Sonnet.Highlighter.setMisspelledColor(QColor color)'''
        def isWordMisspelled(self, word):
            '''bool Sonnet.Highlighter.isWordMisspelled(QString word)'''
            return bool()
        def suggestionsForWord(self, word, max = 10):
            '''QStringList Sonnet.Highlighter.suggestionsForWord(QString word, int max = 10)'''
            return QStringList()
        def ignoreWord(self, word):
            '''void Sonnet.Highlighter.ignoreWord(QString word)'''
        def addWordToDictionary(self, word):
            '''void Sonnet.Highlighter.addWordToDictionary(QString word)'''
        def setAutomatic(self, automatic):
            '''void Sonnet.Highlighter.setAutomatic(bool automatic)'''
        def automatic(self):
            '''bool Sonnet.Highlighter.automatic()'''
            return bool()
        def isActive(self):
            '''bool Sonnet.Highlighter.isActive()'''
            return bool()
        def setActive(self, active):
            '''void Sonnet.Highlighter.setActive(bool active)'''
        def personalWords(self):
            '''static QStringList Sonnet.Highlighter.personalWords()'''
            return QStringList()
        def setCurrentLanguage(self, lang):
            '''void Sonnet.Highlighter.setCurrentLanguage(QString lang)'''
        def currentLanguage(self):
            '''QString Sonnet.Highlighter.currentLanguage()'''
            return QString()
        def spellCheckerFound(self):
            '''bool Sonnet.Highlighter.spellCheckerFound()'''
            return bool()


# Enum KColorChooserMode
ChooserClassic = 0
ChooserHue = 0
ChooserSaturation = 0
ChooserValue = 0
ChooserRed = 0
ChooserGreen = 0
ChooserBlue = 0


def UserIconSet(name):
    '''static QIcon UserIconSet(QString name)'''
    return QIcon()

def UserIcon(name, state = None, overlays = QStringList()):
    '''static QPixmap UserIcon(QString name, int state = KIconLoader.DefaultState, QStringList overlays = QStringList())'''
    return QPixmap()

def MainBarIconSet(name, size = 0):
    '''static QIcon MainBarIconSet(QString name, int size = 0)'''
    return QIcon()

def MainBarIcon(name, size = 0, state = None, overlays = QStringList()):
    '''static QPixmap MainBarIcon(QString name, int size = 0, int state = KIconLoader.DefaultState, QStringList overlays = QStringList())'''
    return QPixmap()

def SmallIconSet(name, size = 0):
    '''static QIcon SmallIconSet(QString name, int size = 0)'''
    return QIcon()

def SmallIcon(name, size = 0, state = None, overlays = QStringList()):
    '''static QPixmap SmallIcon(QString name, int size = 0, int state = KIconLoader.DefaultState, QStringList overlays = QStringList())'''
    return QPixmap()

def BarIconSet(name, size = 0):
    '''static QIcon BarIconSet(QString name, int size = 0)'''
    return QIcon()

def BarIcon(name, size = 0, state = None, overlays = QStringList()):
    '''static QPixmap BarIcon(QString name, int size = 0, int state = KIconLoader.DefaultState, QStringList overlays = QStringList())'''
    return QPixmap()

def DesktopIconSet(name, size = 0):
    '''static QIcon DesktopIconSet(QString name, int size = 0)'''
    return QIcon()

def DesktopIcon(name, size = 0, state = None, overlays = QStringList()):
    '''static QPixmap DesktopIcon(QString name, int size = 0, int state = KIconLoader.DefaultState, QStringList overlays = QStringList())'''
    return QPixmap()

def qHash(key):
    '''static int qHash(KShapeGesture key)'''
    return int()

def qHash(key):
    '''static int qHash(KRockerGesture key)'''
    return int()

def qHash():
    '''static int qHash()'''
    return int()

def qHash(key):
    '''static int qHash(KShortcut key)'''
    return int()

def qHash(key):
    '''static int qHash(QKeySequence key)'''
    return int()

