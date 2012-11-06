class pyqtSignal():
 def connect(self, targetSignal): pass
 def emit(self, *args): pass
from QtCore import *

class PolkitQt():
    """"""
    class ActionButton(PolkitQt.Action):
        """"""
        def __init__(self, button, actionId = QString(), parent = None):
            '''void PolkitQt.ActionButton.__init__(QAbstractButton button, QString actionId = QString(), QObject parent = None)'''
        clicked = pyqtSignal() # void clicked(QAbstractButton *,bool = 0) - signal
        def activate(self):
            '''bool PolkitQt.ActionButton.activate()'''
            return bool()
        def button(self):
            '''QAbstractButton PolkitQt.ActionButton.button()'''
            return QAbstractButton()
        def setButton(self, button):
            '''void PolkitQt.ActionButton.setButton(QAbstractButton button)'''
    class Context(QObject):
        """"""
        def __init__(self):
            '''void PolkitQt.Context.__init__()'''
        consoleKitDBChanged = pyqtSignal() # void consoleKitDBChanged() - signal
        configChanged = pyqtSignal() # void configChanged() - signal
        def lastError(self):
            '''QString PolkitQt.Context.lastError()'''
            return QString()
        def hasError(self):
            '''bool PolkitQt.Context.hasError()'''
            return bool()
    class Auth():
        """"""
        # Enum PolkitQt.Auth.Result
        Unknown = 0
        Yes = 0
        AdminAuthOneShot = 0
        AdminAuth = 0
        AdminAuthKeepSession = 0
        AdminAuthKeepAlways = 0
        SelfAuthOneShot = 0
        SelfAuth = 0
        SelfAuthKeepSession = 0
        SelfAuthKeepAlways = 0
        No = 0
    
        def isCallerAuthorized(self, actionId, pid, revokeIfOneShot):
            '''static PolkitQt.Auth.Result PolkitQt.Auth.isCallerAuthorized(QString actionId, int pid, bool revokeIfOneShot)'''
            return PolkitQt.Auth.Result()
        def isCallerAuthorized(self, actionId, dbusName, revokeIfOneShot):
            '''static PolkitQt.Auth.Result PolkitQt.Auth.isCallerAuthorized(QString actionId, QString dbusName, bool revokeIfOneShot)'''
            return PolkitQt.Auth.Result()
        def obtainAuth(self, actionId, winId = 0, pid = None):
            '''static bool PolkitQt.Auth.obtainAuth(QString actionId, int winId = 0, int pid = QCoreApplication.applicationPid())'''
            return bool()
        def computeAndObtainAuth(self, actionId, winId = 0, pid = None):
            '''static bool PolkitQt.Auth.computeAndObtainAuth(QString actionId, int winId = 0, int pid = QCoreApplication.applicationPid())'''
            return bool()
    class ActionButtons(PolkitQt.ActionButton):
        """"""
        def __init__(self, buttons, actionId = QString(), parent = None):
            '''void PolkitQt.ActionButtons.__init__(list-of-QAbstractButton buttons, QString actionId = QString(), QObject parent = None)'''
        def removeButton(self, button):
            '''void PolkitQt.ActionButtons.removeButton(QAbstractButton button)'''
        def addButton(self, button):
            '''void PolkitQt.ActionButtons.addButton(QAbstractButton button)'''
        def buttons(self):
            '''list-of-QAbstractButton PolkitQt.ActionButtons.buttons()'''
            return [QAbstractButton()]
        def setButtons(self, buttons):
            '''void PolkitQt.ActionButtons.setButtons(list-of-QAbstractButton buttons)'''
    class Action(QAction):
        """"""
        def __init__(self, actionId = QString(), parent = None):
            '''void PolkitQt.Action.__init__(QString actionId = QString(), QObject parent = None)'''
        def is_(self, actionId):
            '''bool PolkitQt.Action.is_(QString actionId)'''
            return bool()
        def isAllowed(self):
            '''bool PolkitQt.Action.isAllowed()'''
            return bool()
        def targetPID(self):
            '''int PolkitQt.Action.targetPID()'''
            return int()
        def setTargetPID(self, pid):
            '''void PolkitQt.Action.setTargetPID(int pid)'''
        def yesIcon(self):
            '''QIcon PolkitQt.Action.yesIcon()'''
            return QIcon()
        def setYesIcon(self, icon):
            '''void PolkitQt.Action.setYesIcon(QIcon icon)'''
        def yesWhatsThis(self):
            '''QString PolkitQt.Action.yesWhatsThis()'''
            return QString()
        def setYesWhatsThis(self, whatsThis):
            '''void PolkitQt.Action.setYesWhatsThis(QString whatsThis)'''
        def yesToolTip(self):
            '''QString PolkitQt.Action.yesToolTip()'''
            return QString()
        def setYesToolTip(self, toolTip):
            '''void PolkitQt.Action.setYesToolTip(QString toolTip)'''
        def yesText(self):
            '''QString PolkitQt.Action.yesText()'''
            return QString()
        def setYesText(self, text):
            '''void PolkitQt.Action.setYesText(QString text)'''
        def yesEnabled(self):
            '''bool PolkitQt.Action.yesEnabled()'''
            return bool()
        def setYesEnabled(self, value):
            '''void PolkitQt.Action.setYesEnabled(bool value)'''
        def yesVisible(self):
            '''bool PolkitQt.Action.yesVisible()'''
            return bool()
        def setYesVisible(self, value):
            '''void PolkitQt.Action.setYesVisible(bool value)'''
        def authIcon(self):
            '''QIcon PolkitQt.Action.authIcon()'''
            return QIcon()
        def setAuthIcon(self, icon):
            '''void PolkitQt.Action.setAuthIcon(QIcon icon)'''
        def authWhatsThis(self):
            '''QString PolkitQt.Action.authWhatsThis()'''
            return QString()
        def setAuthWhatsThis(self, whatsThis):
            '''void PolkitQt.Action.setAuthWhatsThis(QString whatsThis)'''
        def authToolTip(self):
            '''QString PolkitQt.Action.authToolTip()'''
            return QString()
        def setAuthToolTip(self, toolTip):
            '''void PolkitQt.Action.setAuthToolTip(QString toolTip)'''
        def authText(self):
            '''QString PolkitQt.Action.authText()'''
            return QString()
        def setAuthText(self, text):
            '''void PolkitQt.Action.setAuthText(QString text)'''
        def authEnabled(self):
            '''bool PolkitQt.Action.authEnabled()'''
            return bool()
        def setAuthEnabled(self, value):
            '''void PolkitQt.Action.setAuthEnabled(bool value)'''
        def authVisible(self):
            '''bool PolkitQt.Action.authVisible()'''
            return bool()
        def setAuthVisible(self, value):
            '''void PolkitQt.Action.setAuthVisible(bool value)'''
        def noIcon(self):
            '''QIcon PolkitQt.Action.noIcon()'''
            return QIcon()
        def setNoIcon(self, icon):
            '''void PolkitQt.Action.setNoIcon(QIcon icon)'''
        def noWhatsThis(self):
            '''QString PolkitQt.Action.noWhatsThis()'''
            return QString()
        def setNoWhatsThis(self, whatsThis):
            '''void PolkitQt.Action.setNoWhatsThis(QString whatsThis)'''
        def noToolTip(self):
            '''QString PolkitQt.Action.noToolTip()'''
            return QString()
        def setNoToolTip(self, toolTip):
            '''void PolkitQt.Action.setNoToolTip(QString toolTip)'''
        def noText(self):
            '''QString PolkitQt.Action.noText()'''
            return QString()
        def setNoText(self, text):
            '''void PolkitQt.Action.setNoText(QString text)'''
        def noEnabled(self):
            '''bool PolkitQt.Action.noEnabled()'''
            return bool()
        def setNoEnabled(self, value):
            '''void PolkitQt.Action.setNoEnabled(bool value)'''
        def noVisible(self):
            '''bool PolkitQt.Action.noVisible()'''
            return bool()
        def setNoVisible(self, value):
            '''void PolkitQt.Action.setNoVisible(bool value)'''
        def selfBlockedIcon(self):
            '''QIcon PolkitQt.Action.selfBlockedIcon()'''
            return QIcon()
        def setSelfBlockedIcon(self, icon):
            '''void PolkitQt.Action.setSelfBlockedIcon(QIcon icon)'''
        def selfBlockedWhatsThis(self):
            '''QString PolkitQt.Action.selfBlockedWhatsThis()'''
            return QString()
        def setSelfBlockedWhatsThis(self, whatsThis):
            '''void PolkitQt.Action.setSelfBlockedWhatsThis(QString whatsThis)'''
        def selfBlockedToolTip(self):
            '''QString PolkitQt.Action.selfBlockedToolTip()'''
            return QString()
        def setSelfBlockedToolTip(self, toolTip):
            '''void PolkitQt.Action.setSelfBlockedToolTip(QString toolTip)'''
        def selfBlockedText(self):
            '''QString PolkitQt.Action.selfBlockedText()'''
            return QString()
        def setSelfBlockedText(self, text):
            '''void PolkitQt.Action.setSelfBlockedText(QString text)'''
        def selfBlockedEnabled(self):
            '''bool PolkitQt.Action.selfBlockedEnabled()'''
            return bool()
        def setSelfBlockedEnabled(self, value):
            '''void PolkitQt.Action.setSelfBlockedEnabled(bool value)'''
        def selfBlockedVisible(self):
            '''bool PolkitQt.Action.selfBlockedVisible()'''
            return bool()
        def setSelfBlockedVisible(self, value):
            '''void PolkitQt.Action.setSelfBlockedVisible(bool value)'''
        def setIcon(self, icon):
            '''void PolkitQt.Action.setIcon(QIcon icon)'''
        def setWhatsThis(self, whatsThis):
            '''void PolkitQt.Action.setWhatsThis(QString whatsThis)'''
        def setToolTip(self, toolTip):
            '''void PolkitQt.Action.setToolTip(QString toolTip)'''
        def setText(self, text):
            '''void PolkitQt.Action.setText(QString text)'''
        def masterEnabled(self):
            '''bool PolkitQt.Action.masterEnabled()'''
            return bool()
        def setMasterEnabled(self, value):
            '''void PolkitQt.Action.setMasterEnabled(bool value)'''
        def masterVisible(self):
            '''bool PolkitQt.Action.masterVisible()'''
            return bool()
        def setMasterVisible(self, value):
            '''void PolkitQt.Action.setMasterVisible(bool value)'''
        def actionId(self):
            '''QString PolkitQt.Action.actionId()'''
            return QString()
        def setPolkitAction(self, actionId = QString()):
            '''void PolkitQt.Action.setPolkitAction(QString actionId = QString())'''
        def revoke(self):
            '''void PolkitQt.Action.revoke()'''
        def setChecked(self, checked):
            '''void PolkitQt.Action.setChecked(bool checked)'''
        def activate(self, winId = 0):
            '''bool PolkitQt.Action.activate(int winId = 0)'''
            return bool()
        activated = pyqtSignal() # void activated() - signal
        dataChanged = pyqtSignal() # void dataChanged() - signal


