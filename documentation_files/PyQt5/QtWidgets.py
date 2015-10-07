class pyqtSignal():
 def connect(self, targetSignal): pass
 def emit(self, *args): pass
from QtCore import *

from QtWidgets import *

import datetime

class QWidget(QObject, QPaintDevice):
    """"""
    # Enum QWidget.RenderFlag
    DrawWindowBackground = 0
    DrawChildren = 0
    IgnoreMask = 0

    def __init__(self, parent = None, flags = 0):
        '''void QWidget.__init__(QWidget parent = None, Qt.WindowFlags flags = 0)'''
    windowIconTextChanged = pyqtSignal() # void windowIconTextChanged(const QStringamp;) - signal
    windowIconChanged = pyqtSignal() # void windowIconChanged(const QIconamp;) - signal
    windowTitleChanged = pyqtSignal() # void windowTitleChanged(const QStringamp;) - signal
    def toolTipDuration(self):
        '''int QWidget.toolTipDuration()'''
        return int()
    def setToolTipDuration(self, msec):
        '''void QWidget.setToolTipDuration(int msec)'''
    def initPainter(self, painter):
        '''void QWidget.initPainter(QPainter painter)'''
    def sharedPainter(self):
        '''QPainter QWidget.sharedPainter()'''
        return QPainter()
    def nativeEvent(self, eventType, message, result):
        '''bool QWidget.nativeEvent(QByteArray eventType, sip.voidptr message, int result)'''
        return bool()
    def windowHandle(self):
        '''QWindow QWidget.windowHandle()'''
        return QWindow()
    def createWindowContainer(self, window, parent = None, flags = 0):
        '''static QWidget QWidget.createWindowContainer(QWindow window, QWidget parent = None, Qt.WindowFlags flags = 0)'''
        return QWidget()
    def grab(self, rectangle = None):
        '''QPixmap QWidget.grab(QRect rectangle = QRect(QPoint(0,0),QSize(-1,-1)))'''
        return QPixmap()
    def hasHeightForWidth(self):
        '''bool QWidget.hasHeightForWidth()'''
        return bool()
    def setInputMethodHints(self, hints):
        '''void QWidget.setInputMethodHints(Qt.InputMethodHints hints)'''
    def inputMethodHints(self):
        '''Qt.InputMethodHints QWidget.inputMethodHints()'''
        return Qt.InputMethodHints()
    def previousInFocusChain(self):
        '''QWidget QWidget.previousInFocusChain()'''
        return QWidget()
    def contentsMargins(self):
        '''QMargins QWidget.contentsMargins()'''
        return QMargins()
    def ungrabGesture(self, type):
        '''void QWidget.ungrabGesture(Qt.GestureType type)'''
    def grabGesture(self, type, flags = None):
        '''void QWidget.grabGesture(Qt.GestureType type, Qt.GestureFlags flags = Qt.GestureFlags(0))'''
    def setGraphicsEffect(self, effect):
        '''void QWidget.setGraphicsEffect(QGraphicsEffect effect)'''
    def graphicsEffect(self):
        '''QGraphicsEffect QWidget.graphicsEffect()'''
        return QGraphicsEffect()
    def graphicsProxyWidget(self):
        '''QGraphicsProxyWidget QWidget.graphicsProxyWidget()'''
        return QGraphicsProxyWidget()
    def windowFilePath(self):
        '''str QWidget.windowFilePath()'''
        return str()
    def setWindowFilePath(self, filePath):
        '''void QWidget.setWindowFilePath(str filePath)'''
    def nativeParentWidget(self):
        '''QWidget QWidget.nativeParentWidget()'''
        return QWidget()
    def effectiveWinId(self):
        '''sip.voidptr QWidget.effectiveWinId()'''
        return sip.voidptr()
    def unsetLocale(self):
        '''void QWidget.unsetLocale()'''
    def locale(self):
        '''QLocale QWidget.locale()'''
        return QLocale()
    def setLocale(self, locale):
        '''void QWidget.setLocale(QLocale locale)'''
    def render(self, target, targetOffset = QPoint(), sourceRegion = QRegion(), flags = None):
        '''void QWidget.render(QPaintDevice target, QPoint targetOffset = QPoint(), QRegion sourceRegion = QRegion(), QWidget.RenderFlags flags = QWidget.DrawWindowBackground|QWidget.DrawChildren)'''
    def render(self, painter, targetOffset = QPoint(), sourceRegion = QRegion(), flags = None):
        '''void QWidget.render(QPainter painter, QPoint targetOffset = QPoint(), QRegion sourceRegion = QRegion(), QWidget.RenderFlags flags = QWidget.DrawWindowBackground|QWidget.DrawChildren)'''
    def restoreGeometry(self, geometry):
        '''bool QWidget.restoreGeometry(QByteArray geometry)'''
        return bool()
    def saveGeometry(self):
        '''QByteArray QWidget.saveGeometry()'''
        return QByteArray()
    def setShortcutAutoRepeat(self, id, enabled = True):
        '''void QWidget.setShortcutAutoRepeat(int id, bool enabled = True)'''
    def styleSheet(self):
        '''str QWidget.styleSheet()'''
        return str()
    def setStyleSheet(self, styleSheet):
        '''void QWidget.setStyleSheet(str styleSheet)'''
    def setAutoFillBackground(self, enabled):
        '''void QWidget.setAutoFillBackground(bool enabled)'''
    def autoFillBackground(self):
        '''bool QWidget.autoFillBackground()'''
        return bool()
    def setWindowModality(self, windowModality):
        '''void QWidget.setWindowModality(Qt.WindowModality windowModality)'''
    def windowModality(self):
        '''Qt.WindowModality QWidget.windowModality()'''
        return Qt.WindowModality()
    def testAttribute(self, attribute):
        '''bool QWidget.testAttribute(Qt.WidgetAttribute attribute)'''
        return bool()
    def parentWidget(self):
        '''QWidget QWidget.parentWidget()'''
        return QWidget()
    def height(self):
        '''int QWidget.height()'''
        return int()
    def width(self):
        '''int QWidget.width()'''
        return int()
    def size(self):
        '''QSize QWidget.size()'''
        return QSize()
    def geometry(self):
        '''QRect QWidget.geometry()'''
        return QRect()
    def rect(self):
        '''QRect QWidget.rect()'''
        return QRect()
    def isHidden(self):
        '''bool QWidget.isHidden()'''
        return bool()
    def isVisible(self):
        '''bool QWidget.isVisible()'''
        return bool()
    def updatesEnabled(self):
        '''bool QWidget.updatesEnabled()'''
        return bool()
    def underMouse(self):
        '''bool QWidget.underMouse()'''
        return bool()
    def hasMouseTracking(self):
        '''bool QWidget.hasMouseTracking()'''
        return bool()
    def setMouseTracking(self, enable):
        '''void QWidget.setMouseTracking(bool enable)'''
    def fontInfo(self):
        '''QFontInfo QWidget.fontInfo()'''
        return QFontInfo()
    def fontMetrics(self):
        '''QFontMetrics QWidget.fontMetrics()'''
        return QFontMetrics()
    def font(self):
        '''QFont QWidget.font()'''
        return QFont()
    def maximumHeight(self):
        '''int QWidget.maximumHeight()'''
        return int()
    def maximumWidth(self):
        '''int QWidget.maximumWidth()'''
        return int()
    def minimumHeight(self):
        '''int QWidget.minimumHeight()'''
        return int()
    def minimumWidth(self):
        '''int QWidget.minimumWidth()'''
        return int()
    def isModal(self):
        '''bool QWidget.isModal()'''
        return bool()
    def isEnabled(self):
        '''bool QWidget.isEnabled()'''
        return bool()
    def isWindow(self):
        '''bool QWidget.isWindow()'''
        return bool()
    def winId(self):
        '''sip.voidptr QWidget.winId()'''
        return sip.voidptr()
    def windowFlags(self):
        '''Qt.WindowFlags QWidget.windowFlags()'''
        return Qt.WindowFlags()
    def windowType(self):
        '''Qt.WindowType QWidget.windowType()'''
        return Qt.WindowType()
    def focusPreviousChild(self):
        '''bool QWidget.focusPreviousChild()'''
        return bool()
    def focusNextChild(self):
        '''bool QWidget.focusNextChild()'''
        return bool()
    def focusNextPrevChild(self, next):
        '''bool QWidget.focusNextPrevChild(bool next)'''
        return bool()
    def destroy(self, destroyWindow = True, destroySubWindows = True):
        '''void QWidget.destroy(bool destroyWindow = True, bool destroySubWindows = True)'''
    def create(self, window = 0, initializeWindow = True, destroyOldWindow = True):
        '''void QWidget.create(sip.voidptr window = 0, bool initializeWindow = True, bool destroyOldWindow = True)'''
    def updateMicroFocus(self):
        '''void QWidget.updateMicroFocus()'''
    def inputMethodQuery(self):
        '''Qt.InputMethodQuery QWidget.inputMethodQuery()'''
        return Qt.InputMethodQuery()
    def inputMethodEvent(self):
        '''QInputMethodEvent QWidget.inputMethodEvent()'''
        return QInputMethodEvent()
    def metric(self):
        '''QPaintDevice.PaintDeviceMetric QWidget.metric()'''
        return QPaintDevice.PaintDeviceMetric()
    def changeEvent(self):
        '''QEvent QWidget.changeEvent()'''
        return QEvent()
    def hideEvent(self):
        '''QHideEvent QWidget.hideEvent()'''
        return QHideEvent()
    def showEvent(self):
        '''QShowEvent QWidget.showEvent()'''
        return QShowEvent()
    def dropEvent(self):
        '''QDropEvent QWidget.dropEvent()'''
        return QDropEvent()
    def dragLeaveEvent(self):
        '''QDragLeaveEvent QWidget.dragLeaveEvent()'''
        return QDragLeaveEvent()
    def dragMoveEvent(self):
        '''QDragMoveEvent QWidget.dragMoveEvent()'''
        return QDragMoveEvent()
    def dragEnterEvent(self):
        '''QDragEnterEvent QWidget.dragEnterEvent()'''
        return QDragEnterEvent()
    def actionEvent(self):
        '''QActionEvent QWidget.actionEvent()'''
        return QActionEvent()
    def tabletEvent(self):
        '''QTabletEvent QWidget.tabletEvent()'''
        return QTabletEvent()
    def contextMenuEvent(self):
        '''QContextMenuEvent QWidget.contextMenuEvent()'''
        return QContextMenuEvent()
    def closeEvent(self):
        '''QCloseEvent QWidget.closeEvent()'''
        return QCloseEvent()
    def resizeEvent(self):
        '''QResizeEvent QWidget.resizeEvent()'''
        return QResizeEvent()
    def moveEvent(self):
        '''QMoveEvent QWidget.moveEvent()'''
        return QMoveEvent()
    def paintEvent(self):
        '''QPaintEvent QWidget.paintEvent()'''
        return QPaintEvent()
    def leaveEvent(self):
        '''QEvent QWidget.leaveEvent()'''
        return QEvent()
    def enterEvent(self):
        '''QEvent QWidget.enterEvent()'''
        return QEvent()
    def focusOutEvent(self):
        '''QFocusEvent QWidget.focusOutEvent()'''
        return QFocusEvent()
    def focusInEvent(self):
        '''QFocusEvent QWidget.focusInEvent()'''
        return QFocusEvent()
    def keyReleaseEvent(self):
        '''QKeyEvent QWidget.keyReleaseEvent()'''
        return QKeyEvent()
    def keyPressEvent(self):
        '''QKeyEvent QWidget.keyPressEvent()'''
        return QKeyEvent()
    def wheelEvent(self):
        '''QWheelEvent QWidget.wheelEvent()'''
        return QWheelEvent()
    def mouseMoveEvent(self):
        '''QMouseEvent QWidget.mouseMoveEvent()'''
        return QMouseEvent()
    def mouseDoubleClickEvent(self):
        '''QMouseEvent QWidget.mouseDoubleClickEvent()'''
        return QMouseEvent()
    def mouseReleaseEvent(self):
        '''QMouseEvent QWidget.mouseReleaseEvent()'''
        return QMouseEvent()
    def mousePressEvent(self):
        '''QMouseEvent QWidget.mousePressEvent()'''
        return QMouseEvent()
    def event(self):
        '''QEvent QWidget.event()'''
        return QEvent()
    customContextMenuRequested = pyqtSignal() # void customContextMenuRequested(const QPointamp;) - signal
    def isAncestorOf(self, child):
        '''bool QWidget.isAncestorOf(QWidget child)'''
        return bool()
    def ensurePolished(self):
        '''void QWidget.ensurePolished()'''
    def paintEngine(self):
        '''QPaintEngine QWidget.paintEngine()'''
        return QPaintEngine()
    def setAttribute(self, attribute, on = True):
        '''void QWidget.setAttribute(Qt.WidgetAttribute attribute, bool on = True)'''
    def childAt(self, p):
        '''QWidget QWidget.childAt(QPoint p)'''
        return QWidget()
    def childAt(self, ax, ay):
        '''QWidget QWidget.childAt(int ax, int ay)'''
        return QWidget()
    def find(self):
        '''static sip.voidptr QWidget.find()'''
        return sip.voidptr()
    def overrideWindowFlags(self, type):
        '''void QWidget.overrideWindowFlags(Qt.WindowFlags type)'''
    def setWindowFlags(self, type):
        '''void QWidget.setWindowFlags(Qt.WindowFlags type)'''
    def actions(self):
        '''list-of-QAction QWidget.actions()'''
        return [QAction()]
    def removeAction(self, action):
        '''void QWidget.removeAction(QAction action)'''
    def insertActions(self, before, actions):
        '''void QWidget.insertActions(QAction before, list-of-QAction actions)'''
    def insertAction(self, before, action):
        '''void QWidget.insertAction(QAction before, QAction action)'''
    def addActions(self, actions):
        '''void QWidget.addActions(list-of-QAction actions)'''
    def addAction(self, action):
        '''void QWidget.addAction(QAction action)'''
    def setAcceptDrops(self, on):
        '''void QWidget.setAcceptDrops(bool on)'''
    def acceptDrops(self):
        '''bool QWidget.acceptDrops()'''
        return bool()
    def nextInFocusChain(self):
        '''QWidget QWidget.nextInFocusChain()'''
        return QWidget()
    def focusWidget(self):
        '''QWidget QWidget.focusWidget()'''
        return QWidget()
    def scroll(self, dx, dy):
        '''void QWidget.scroll(int dx, int dy)'''
    def scroll(self, dx, dy):
        '''QRect QWidget.scroll(int dx, int dy)'''
        return QRect()
    def setParent(self, parent):
        '''void QWidget.setParent(QWidget parent)'''
    def setParent(self, parent, f):
        '''void QWidget.setParent(QWidget parent, Qt.WindowFlags f)'''
    def updateGeometry(self):
        '''void QWidget.updateGeometry()'''
    def setLayout(self):
        '''QLayout QWidget.setLayout()'''
        return QLayout()
    def layout(self):
        '''QLayout QWidget.layout()'''
        return QLayout()
    def contentsRect(self):
        '''QRect QWidget.contentsRect()'''
        return QRect()
    def getContentsMargins(self, left, top, right, bottom):
        '''void QWidget.getContentsMargins(int left, int top, int right, int bottom)'''
    def setContentsMargins(self, left, top, right, bottom):
        '''void QWidget.setContentsMargins(int left, int top, int right, int bottom)'''
    def setContentsMargins(self, margins):
        '''void QWidget.setContentsMargins(QMargins margins)'''
    def visibleRegion(self):
        '''QRegion QWidget.visibleRegion()'''
        return QRegion()
    def heightForWidth(self):
        '''int QWidget.heightForWidth()'''
        return int()
    def setSizePolicy(self):
        '''QSizePolicy QWidget.setSizePolicy()'''
        return QSizePolicy()
    def setSizePolicy(self, hor, ver):
        '''void QWidget.setSizePolicy(QSizePolicy.Policy hor, QSizePolicy.Policy ver)'''
    def sizePolicy(self):
        '''QSizePolicy QWidget.sizePolicy()'''
        return QSizePolicy()
    def minimumSizeHint(self):
        '''QSize QWidget.minimumSizeHint()'''
        return QSize()
    def sizeHint(self):
        '''QSize QWidget.sizeHint()'''
        return QSize()
    def overrideWindowState(self, state):
        '''void QWidget.overrideWindowState(Qt.WindowStates state)'''
    def setWindowState(self, state):
        '''void QWidget.setWindowState(Qt.WindowStates state)'''
    def windowState(self):
        '''Qt.WindowStates QWidget.windowState()'''
        return Qt.WindowStates()
    def isFullScreen(self):
        '''bool QWidget.isFullScreen()'''
        return bool()
    def isMaximized(self):
        '''bool QWidget.isMaximized()'''
        return bool()
    def isMinimized(self):
        '''bool QWidget.isMinimized()'''
        return bool()
    def isVisibleTo(self):
        '''QWidget QWidget.isVisibleTo()'''
        return QWidget()
    def adjustSize(self):
        '''void QWidget.adjustSize()'''
    def setGeometry(self):
        '''QRect QWidget.setGeometry()'''
        return QRect()
    def setGeometry(self, ax, ay, aw, ah):
        '''void QWidget.setGeometry(int ax, int ay, int aw, int ah)'''
    def resize(self):
        '''QSize QWidget.resize()'''
        return QSize()
    def resize(self, w, h):
        '''void QWidget.resize(int w, int h)'''
    def move(self):
        '''QPoint QWidget.move()'''
        return QPoint()
    def move(self, ax, ay):
        '''void QWidget.move(int ax, int ay)'''
    def stackUnder(self):
        '''QWidget QWidget.stackUnder()'''
        return QWidget()
    def lower(self):
        '''void QWidget.lower()'''
    def raise_(self):
        '''void QWidget.raise_()'''
    def close(self):
        '''bool QWidget.close()'''
        return bool()
    def showNormal(self):
        '''void QWidget.showNormal()'''
    def showFullScreen(self):
        '''void QWidget.showFullScreen()'''
    def showMaximized(self):
        '''void QWidget.showMaximized()'''
    def showMinimized(self):
        '''void QWidget.showMinimized()'''
    def hide(self):
        '''void QWidget.hide()'''
    def show(self):
        '''void QWidget.show()'''
    def setHidden(self, hidden):
        '''void QWidget.setHidden(bool hidden)'''
    def setVisible(self, visible):
        '''void QWidget.setVisible(bool visible)'''
    def repaint(self):
        '''void QWidget.repaint()'''
    def repaint(self, x, y, w, h):
        '''void QWidget.repaint(int x, int y, int w, int h)'''
    def repaint(self):
        '''QRect QWidget.repaint()'''
        return QRect()
    def repaint(self):
        '''QRegion QWidget.repaint()'''
        return QRegion()
    def update(self):
        '''void QWidget.update()'''
    def update(self):
        '''QRect QWidget.update()'''
        return QRect()
    def update(self):
        '''QRegion QWidget.update()'''
        return QRegion()
    def update(self, ax, ay, aw, ah):
        '''void QWidget.update(int ax, int ay, int aw, int ah)'''
    def setUpdatesEnabled(self, enable):
        '''void QWidget.setUpdatesEnabled(bool enable)'''
    def keyboardGrabber(self):
        '''static QWidget QWidget.keyboardGrabber()'''
        return QWidget()
    def mouseGrabber(self):
        '''static QWidget QWidget.mouseGrabber()'''
        return QWidget()
    def setShortcutEnabled(self, id, enabled = True):
        '''void QWidget.setShortcutEnabled(int id, bool enabled = True)'''
    def releaseShortcut(self, id):
        '''void QWidget.releaseShortcut(int id)'''
    def grabShortcut(self, key, context = None):
        '''int QWidget.grabShortcut(QKeySequence key, Qt.ShortcutContext context = Qt.WindowShortcut)'''
        return int()
    def releaseKeyboard(self):
        '''void QWidget.releaseKeyboard()'''
    def grabKeyboard(self):
        '''void QWidget.grabKeyboard()'''
    def releaseMouse(self):
        '''void QWidget.releaseMouse()'''
    def grabMouse(self):
        '''void QWidget.grabMouse()'''
    def grabMouse(self):
        '''QCursor QWidget.grabMouse()'''
        return QCursor()
    def setContextMenuPolicy(self, policy):
        '''void QWidget.setContextMenuPolicy(Qt.ContextMenuPolicy policy)'''
    def contextMenuPolicy(self):
        '''Qt.ContextMenuPolicy QWidget.contextMenuPolicy()'''
        return Qt.ContextMenuPolicy()
    def focusProxy(self):
        '''QWidget QWidget.focusProxy()'''
        return QWidget()
    def setFocusProxy(self):
        '''QWidget QWidget.setFocusProxy()'''
        return QWidget()
    def setTabOrder(self):
        '''static QWidget QWidget.setTabOrder()'''
        return QWidget()
    def hasFocus(self):
        '''bool QWidget.hasFocus()'''
        return bool()
    def setFocusPolicy(self, policy):
        '''void QWidget.setFocusPolicy(Qt.FocusPolicy policy)'''
    def focusPolicy(self):
        '''Qt.FocusPolicy QWidget.focusPolicy()'''
        return Qt.FocusPolicy()
    def clearFocus(self):
        '''void QWidget.clearFocus()'''
    def activateWindow(self):
        '''void QWidget.activateWindow()'''
    def isActiveWindow(self):
        '''bool QWidget.isActiveWindow()'''
        return bool()
    def setFocus(self):
        '''void QWidget.setFocus()'''
    def setFocus(self, reason):
        '''void QWidget.setFocus(Qt.FocusReason reason)'''
    def isLeftToRight(self):
        '''bool QWidget.isLeftToRight()'''
        return bool()
    def isRightToLeft(self):
        '''bool QWidget.isRightToLeft()'''
        return bool()
    def unsetLayoutDirection(self):
        '''void QWidget.unsetLayoutDirection()'''
    def layoutDirection(self):
        '''Qt.LayoutDirection QWidget.layoutDirection()'''
        return Qt.LayoutDirection()
    def setLayoutDirection(self, direction):
        '''void QWidget.setLayoutDirection(Qt.LayoutDirection direction)'''
    def setAccessibleDescription(self, description):
        '''void QWidget.setAccessibleDescription(str description)'''
    def accessibleDescription(self):
        '''str QWidget.accessibleDescription()'''
        return str()
    def setAccessibleName(self, name):
        '''void QWidget.setAccessibleName(str name)'''
    def accessibleName(self):
        '''str QWidget.accessibleName()'''
        return str()
    def whatsThis(self):
        '''str QWidget.whatsThis()'''
        return str()
    def setWhatsThis(self):
        '''str QWidget.setWhatsThis()'''
        return str()
    def statusTip(self):
        '''str QWidget.statusTip()'''
        return str()
    def setStatusTip(self):
        '''str QWidget.setStatusTip()'''
        return str()
    def toolTip(self):
        '''str QWidget.toolTip()'''
        return str()
    def setToolTip(self):
        '''str QWidget.setToolTip()'''
        return str()
    def isWindowModified(self):
        '''bool QWidget.isWindowModified()'''
        return bool()
    def windowOpacity(self):
        '''float QWidget.windowOpacity()'''
        return float()
    def setWindowOpacity(self, level):
        '''void QWidget.setWindowOpacity(float level)'''
    def windowRole(self):
        '''str QWidget.windowRole()'''
        return str()
    def setWindowRole(self):
        '''str QWidget.setWindowRole()'''
        return str()
    def windowIconText(self):
        '''str QWidget.windowIconText()'''
        return str()
    def setWindowIconText(self):
        '''str QWidget.setWindowIconText()'''
        return str()
    def windowIcon(self):
        '''QIcon QWidget.windowIcon()'''
        return QIcon()
    def setWindowIcon(self, icon):
        '''void QWidget.setWindowIcon(QIcon icon)'''
    def windowTitle(self):
        '''str QWidget.windowTitle()'''
        return str()
    def setWindowTitle(self):
        '''str QWidget.setWindowTitle()'''
        return str()
    def clearMask(self):
        '''void QWidget.clearMask()'''
    def mask(self):
        '''QRegion QWidget.mask()'''
        return QRegion()
    def setMask(self):
        '''QBitmap QWidget.setMask()'''
        return QBitmap()
    def setMask(self):
        '''QRegion QWidget.setMask()'''
        return QRegion()
    def unsetCursor(self):
        '''void QWidget.unsetCursor()'''
    def setCursor(self):
        '''QCursor QWidget.setCursor()'''
        return QCursor()
    def cursor(self):
        '''QCursor QWidget.cursor()'''
        return QCursor()
    def setFont(self):
        '''QFont QWidget.setFont()'''
        return QFont()
    def foregroundRole(self):
        '''QPalette.ColorRole QWidget.foregroundRole()'''
        return QPalette.ColorRole()
    def setForegroundRole(self):
        '''QPalette.ColorRole QWidget.setForegroundRole()'''
        return QPalette.ColorRole()
    def backgroundRole(self):
        '''QPalette.ColorRole QWidget.backgroundRole()'''
        return QPalette.ColorRole()
    def setBackgroundRole(self):
        '''QPalette.ColorRole QWidget.setBackgroundRole()'''
        return QPalette.ColorRole()
    def setPalette(self):
        '''QPalette QWidget.setPalette()'''
        return QPalette()
    def palette(self):
        '''QPalette QWidget.palette()'''
        return QPalette()
    def window(self):
        '''QWidget QWidget.window()'''
        return QWidget()
    def mapFrom(self):
        '''QPoint QWidget.mapFrom()'''
        return QPoint()
    def mapTo(self):
        '''QPoint QWidget.mapTo()'''
        return QPoint()
    def mapFromParent(self):
        '''QPoint QWidget.mapFromParent()'''
        return QPoint()
    def mapToParent(self):
        '''QPoint QWidget.mapToParent()'''
        return QPoint()
    def mapFromGlobal(self):
        '''QPoint QWidget.mapFromGlobal()'''
        return QPoint()
    def mapToGlobal(self):
        '''QPoint QWidget.mapToGlobal()'''
        return QPoint()
    def setFixedHeight(self, h):
        '''void QWidget.setFixedHeight(int h)'''
    def setFixedWidth(self, w):
        '''void QWidget.setFixedWidth(int w)'''
    def setFixedSize(self):
        '''QSize QWidget.setFixedSize()'''
        return QSize()
    def setFixedSize(self, w, h):
        '''void QWidget.setFixedSize(int w, int h)'''
    def setBaseSize(self, basew, baseh):
        '''void QWidget.setBaseSize(int basew, int baseh)'''
    def setBaseSize(self, s):
        '''void QWidget.setBaseSize(QSize s)'''
    def baseSize(self):
        '''QSize QWidget.baseSize()'''
        return QSize()
    def setSizeIncrement(self, w, h):
        '''void QWidget.setSizeIncrement(int w, int h)'''
    def setSizeIncrement(self, s):
        '''void QWidget.setSizeIncrement(QSize s)'''
    def sizeIncrement(self):
        '''QSize QWidget.sizeIncrement()'''
        return QSize()
    def setMaximumHeight(self, maxh):
        '''void QWidget.setMaximumHeight(int maxh)'''
    def setMaximumWidth(self, maxw):
        '''void QWidget.setMaximumWidth(int maxw)'''
    def setMinimumHeight(self, minh):
        '''void QWidget.setMinimumHeight(int minh)'''
    def setMinimumWidth(self, minw):
        '''void QWidget.setMinimumWidth(int minw)'''
    def setMaximumSize(self, maxw, maxh):
        '''void QWidget.setMaximumSize(int maxw, int maxh)'''
    def setMaximumSize(self, s):
        '''void QWidget.setMaximumSize(QSize s)'''
    def setMinimumSize(self, minw, minh):
        '''void QWidget.setMinimumSize(int minw, int minh)'''
    def setMinimumSize(self, s):
        '''void QWidget.setMinimumSize(QSize s)'''
    def maximumSize(self):
        '''QSize QWidget.maximumSize()'''
        return QSize()
    def minimumSize(self):
        '''QSize QWidget.minimumSize()'''
        return QSize()
    def childrenRegion(self):
        '''QRegion QWidget.childrenRegion()'''
        return QRegion()
    def childrenRect(self):
        '''QRect QWidget.childrenRect()'''
        return QRect()
    def frameSize(self):
        '''QSize QWidget.frameSize()'''
        return QSize()
    def pos(self):
        '''QPoint QWidget.pos()'''
        return QPoint()
    def y(self):
        '''int QWidget.y()'''
        return int()
    def x(self):
        '''int QWidget.x()'''
        return int()
    def normalGeometry(self):
        '''QRect QWidget.normalGeometry()'''
        return QRect()
    def frameGeometry(self):
        '''QRect QWidget.frameGeometry()'''
        return QRect()
    def setWindowModified(self):
        '''bool QWidget.setWindowModified()'''
        return bool()
    def setDisabled(self):
        '''bool QWidget.setDisabled()'''
        return bool()
    def setEnabled(self):
        '''bool QWidget.setEnabled()'''
        return bool()
    def isEnabledTo(self):
        '''QWidget QWidget.isEnabledTo()'''
        return QWidget()
    def setStyle(self):
        '''QStyle QWidget.setStyle()'''
        return QStyle()
    def style(self):
        '''QStyle QWidget.style()'''
        return QStyle()
    def devType(self):
        '''int QWidget.devType()'''
        return int()
    class RenderFlags():
        """"""
        def __init__(self):
            '''QWidget.RenderFlags QWidget.RenderFlags.__init__()'''
            return QWidget.RenderFlags()
        def __init__(self):
            '''int QWidget.RenderFlags.__init__()'''
            return int()
        def __init__(self):
            '''void QWidget.RenderFlags.__init__()'''
        def __bool__(self):
            '''int QWidget.RenderFlags.__bool__()'''
            return int()
        def __ne__(self, f):
            '''bool QWidget.RenderFlags.__ne__(QWidget.RenderFlags f)'''
            return bool()
        def __eq__(self, f):
            '''bool QWidget.RenderFlags.__eq__(QWidget.RenderFlags f)'''
            return bool()
        def __invert__(self):
            '''QWidget.RenderFlags QWidget.RenderFlags.__invert__()'''
            return QWidget.RenderFlags()
        def __and__(self, mask):
            '''QWidget.RenderFlags QWidget.RenderFlags.__and__(int mask)'''
            return QWidget.RenderFlags()
        def __xor__(self, f):
            '''QWidget.RenderFlags QWidget.RenderFlags.__xor__(QWidget.RenderFlags f)'''
            return QWidget.RenderFlags()
        def __xor__(self, f):
            '''QWidget.RenderFlags QWidget.RenderFlags.__xor__(int f)'''
            return QWidget.RenderFlags()
        def __or__(self, f):
            '''QWidget.RenderFlags QWidget.RenderFlags.__or__(QWidget.RenderFlags f)'''
            return QWidget.RenderFlags()
        def __or__(self, f):
            '''QWidget.RenderFlags QWidget.RenderFlags.__or__(int f)'''
            return QWidget.RenderFlags()
        def __int__(self):
            '''int QWidget.RenderFlags.__int__()'''
            return int()
        def __ixor__(self, f):
            '''QWidget.RenderFlags QWidget.RenderFlags.__ixor__(QWidget.RenderFlags f)'''
            return QWidget.RenderFlags()
        def __ior__(self, f):
            '''QWidget.RenderFlags QWidget.RenderFlags.__ior__(QWidget.RenderFlags f)'''
            return QWidget.RenderFlags()
        def __iand__(self, mask):
            '''QWidget.RenderFlags QWidget.RenderFlags.__iand__(int mask)'''
            return QWidget.RenderFlags()


class QAbstractButton(QWidget):
    """"""
    def __init__(self, parent = None):
        '''void QAbstractButton.__init__(QWidget parent = None)'''
    def timerEvent(self, e):
        '''void QAbstractButton.timerEvent(QTimerEvent e)'''
    def changeEvent(self, e):
        '''void QAbstractButton.changeEvent(QEvent e)'''
    def focusOutEvent(self, e):
        '''void QAbstractButton.focusOutEvent(QFocusEvent e)'''
    def focusInEvent(self, e):
        '''void QAbstractButton.focusInEvent(QFocusEvent e)'''
    def mouseMoveEvent(self, e):
        '''void QAbstractButton.mouseMoveEvent(QMouseEvent e)'''
    def mouseReleaseEvent(self, e):
        '''void QAbstractButton.mouseReleaseEvent(QMouseEvent e)'''
    def mousePressEvent(self, e):
        '''void QAbstractButton.mousePressEvent(QMouseEvent e)'''
    def keyReleaseEvent(self, e):
        '''void QAbstractButton.keyReleaseEvent(QKeyEvent e)'''
    def keyPressEvent(self, e):
        '''void QAbstractButton.keyPressEvent(QKeyEvent e)'''
    def event(self, e):
        '''bool QAbstractButton.event(QEvent e)'''
        return bool()
    def nextCheckState(self):
        '''void QAbstractButton.nextCheckState()'''
    def checkStateSet(self):
        '''void QAbstractButton.checkStateSet()'''
    def hitButton(self, pos):
        '''bool QAbstractButton.hitButton(QPoint pos)'''
        return bool()
    def paintEvent(self, e):
        '''abstract void QAbstractButton.paintEvent(QPaintEvent e)'''
    toggled = pyqtSignal() # void toggled(bool) - signal
    clicked = pyqtSignal() # void clicked(bool = 0) - signal
    released = pyqtSignal() # void released() - signal
    pressed = pyqtSignal() # void pressed() - signal
    def setChecked(self):
        '''bool QAbstractButton.setChecked()'''
        return bool()
    def toggle(self):
        '''void QAbstractButton.toggle()'''
    def click(self):
        '''void QAbstractButton.click()'''
    def animateClick(self, msecs = 100):
        '''void QAbstractButton.animateClick(int msecs = 100)'''
    def setIconSize(self, size):
        '''void QAbstractButton.setIconSize(QSize size)'''
    def group(self):
        '''QButtonGroup QAbstractButton.group()'''
        return QButtonGroup()
    def autoExclusive(self):
        '''bool QAbstractButton.autoExclusive()'''
        return bool()
    def setAutoExclusive(self):
        '''bool QAbstractButton.setAutoExclusive()'''
        return bool()
    def autoRepeat(self):
        '''bool QAbstractButton.autoRepeat()'''
        return bool()
    def setAutoRepeat(self):
        '''bool QAbstractButton.setAutoRepeat()'''
        return bool()
    def isDown(self):
        '''bool QAbstractButton.isDown()'''
        return bool()
    def setDown(self):
        '''bool QAbstractButton.setDown()'''
        return bool()
    def isChecked(self):
        '''bool QAbstractButton.isChecked()'''
        return bool()
    def isCheckable(self):
        '''bool QAbstractButton.isCheckable()'''
        return bool()
    def setCheckable(self):
        '''bool QAbstractButton.setCheckable()'''
        return bool()
    def shortcut(self):
        '''QKeySequence QAbstractButton.shortcut()'''
        return QKeySequence()
    def setShortcut(self, key):
        '''void QAbstractButton.setShortcut(QKeySequence key)'''
    def iconSize(self):
        '''QSize QAbstractButton.iconSize()'''
        return QSize()
    def icon(self):
        '''QIcon QAbstractButton.icon()'''
        return QIcon()
    def setIcon(self, icon):
        '''void QAbstractButton.setIcon(QIcon icon)'''
    def text(self):
        '''str QAbstractButton.text()'''
        return str()
    def setText(self, text):
        '''void QAbstractButton.setText(str text)'''
    def autoRepeatInterval(self):
        '''int QAbstractButton.autoRepeatInterval()'''
        return int()
    def setAutoRepeatInterval(self):
        '''int QAbstractButton.setAutoRepeatInterval()'''
        return int()
    def autoRepeatDelay(self):
        '''int QAbstractButton.autoRepeatDelay()'''
        return int()
    def setAutoRepeatDelay(self):
        '''int QAbstractButton.setAutoRepeatDelay()'''
        return int()


class QAbstractItemDelegate(QObject):
    """"""
    # Enum QAbstractItemDelegate.EndEditHint
    NoHint = 0
    EditNextItem = 0
    EditPreviousItem = 0
    SubmitModelCache = 0
    RevertModelCache = 0

    def __init__(self, parent = None):
        '''void QAbstractItemDelegate.__init__(QObject parent = None)'''
    sizeHintChanged = pyqtSignal() # void sizeHintChanged(const QModelIndexamp;) - signal
    closeEditor = pyqtSignal() # void closeEditor(QWidget*,QAbstractItemDelegate::EndEditHint = QAbstractItemDelegate.NoHint) - signal
    commitData = pyqtSignal() # void commitData(QWidget*) - signal
    def helpEvent(self, event, view, option, index):
        '''bool QAbstractItemDelegate.helpEvent(QHelpEvent event, QAbstractItemView view, QStyleOptionViewItem option, QModelIndex index)'''
        return bool()
    def editorEvent(self, event, model, option, index):
        '''bool QAbstractItemDelegate.editorEvent(QEvent event, QAbstractItemModel model, QStyleOptionViewItem option, QModelIndex index)'''
        return bool()
    def destroyEditor(self, editor, index):
        '''void QAbstractItemDelegate.destroyEditor(QWidget editor, QModelIndex index)'''
    def updateEditorGeometry(self, editor, option, index):
        '''void QAbstractItemDelegate.updateEditorGeometry(QWidget editor, QStyleOptionViewItem option, QModelIndex index)'''
    def setModelData(self, editor, model, index):
        '''void QAbstractItemDelegate.setModelData(QWidget editor, QAbstractItemModel model, QModelIndex index)'''
    def setEditorData(self, editor, index):
        '''void QAbstractItemDelegate.setEditorData(QWidget editor, QModelIndex index)'''
    def createEditor(self, parent, option, index):
        '''QWidget QAbstractItemDelegate.createEditor(QWidget parent, QStyleOptionViewItem option, QModelIndex index)'''
        return QWidget()
    def sizeHint(self, option, index):
        '''abstract QSize QAbstractItemDelegate.sizeHint(QStyleOptionViewItem option, QModelIndex index)'''
        return QSize()
    def paint(self, painter, option, index):
        '''abstract void QAbstractItemDelegate.paint(QPainter painter, QStyleOptionViewItem option, QModelIndex index)'''


class QFrame(QWidget):
    """"""
    # Enum QFrame.StyleMask
    Shadow_Mask = 0
    Shape_Mask = 0

    # Enum QFrame.Shape
    NoFrame = 0
    Box = 0
    Panel = 0
    WinPanel = 0
    HLine = 0
    VLine = 0
    StyledPanel = 0

    # Enum QFrame.Shadow
    Plain = 0
    Raised = 0
    Sunken = 0

    def __init__(self, parent = None, flags = 0):
        '''void QFrame.__init__(QWidget parent = None, Qt.WindowFlags flags = 0)'''
    def initStyleOption(self, option):
        '''void QFrame.initStyleOption(QStyleOptionFrame option)'''
    def drawFrame(self):
        '''QPainter QFrame.drawFrame()'''
        return QPainter()
    def changeEvent(self):
        '''QEvent QFrame.changeEvent()'''
        return QEvent()
    def paintEvent(self):
        '''QPaintEvent QFrame.paintEvent()'''
        return QPaintEvent()
    def event(self, e):
        '''bool QFrame.event(QEvent e)'''
        return bool()
    def setFrameRect(self):
        '''QRect QFrame.setFrameRect()'''
        return QRect()
    def frameRect(self):
        '''QRect QFrame.frameRect()'''
        return QRect()
    def setMidLineWidth(self):
        '''int QFrame.setMidLineWidth()'''
        return int()
    def midLineWidth(self):
        '''int QFrame.midLineWidth()'''
        return int()
    def setLineWidth(self):
        '''int QFrame.setLineWidth()'''
        return int()
    def lineWidth(self):
        '''int QFrame.lineWidth()'''
        return int()
    def setFrameShadow(self):
        '''QFrame.Shadow QFrame.setFrameShadow()'''
        return QFrame.Shadow()
    def frameShadow(self):
        '''QFrame.Shadow QFrame.frameShadow()'''
        return QFrame.Shadow()
    def setFrameShape(self):
        '''QFrame.Shape QFrame.setFrameShape()'''
        return QFrame.Shape()
    def frameShape(self):
        '''QFrame.Shape QFrame.frameShape()'''
        return QFrame.Shape()
    def sizeHint(self):
        '''QSize QFrame.sizeHint()'''
        return QSize()
    def frameWidth(self):
        '''int QFrame.frameWidth()'''
        return int()
    def setFrameStyle(self):
        '''int QFrame.setFrameStyle()'''
        return int()
    def frameStyle(self):
        '''int QFrame.frameStyle()'''
        return int()


class QAbstractScrollArea(QFrame):
    """"""
    # Enum QAbstractScrollArea.SizeAdjustPolicy
    AdjustIgnored = 0
    AdjustToContentsOnFirstShow = 0
    AdjustToContents = 0

    def __init__(self, parent = None):
        '''void QAbstractScrollArea.__init__(QWidget parent = None)'''
    def setSizeAdjustPolicy(self, policy):
        '''void QAbstractScrollArea.setSizeAdjustPolicy(QAbstractScrollArea.SizeAdjustPolicy policy)'''
    def sizeAdjustPolicy(self):
        '''QAbstractScrollArea.SizeAdjustPolicy QAbstractScrollArea.sizeAdjustPolicy()'''
        return QAbstractScrollArea.SizeAdjustPolicy()
    def setupViewport(self, viewport):
        '''void QAbstractScrollArea.setupViewport(QWidget viewport)'''
    def setViewport(self, widget):
        '''void QAbstractScrollArea.setViewport(QWidget widget)'''
    def scrollBarWidgets(self, alignment):
        '''list-of-QWidget QAbstractScrollArea.scrollBarWidgets(Qt.Alignment alignment)'''
        return [QWidget()]
    def addScrollBarWidget(self, widget, alignment):
        '''void QAbstractScrollArea.addScrollBarWidget(QWidget widget, Qt.Alignment alignment)'''
    def setCornerWidget(self, widget):
        '''void QAbstractScrollArea.setCornerWidget(QWidget widget)'''
    def cornerWidget(self):
        '''QWidget QAbstractScrollArea.cornerWidget()'''
        return QWidget()
    def setHorizontalScrollBar(self, scrollbar):
        '''void QAbstractScrollArea.setHorizontalScrollBar(QScrollBar scrollbar)'''
    def setVerticalScrollBar(self, scrollbar):
        '''void QAbstractScrollArea.setVerticalScrollBar(QScrollBar scrollbar)'''
    def scrollContentsBy(self, dx, dy):
        '''void QAbstractScrollArea.scrollContentsBy(int dx, int dy)'''
    def eventFilter(self):
        '''QEvent QAbstractScrollArea.eventFilter()'''
        return QEvent()
    def keyPressEvent(self):
        '''QKeyEvent QAbstractScrollArea.keyPressEvent()'''
        return QKeyEvent()
    def dropEvent(self):
        '''QDropEvent QAbstractScrollArea.dropEvent()'''
        return QDropEvent()
    def dragLeaveEvent(self):
        '''QDragLeaveEvent QAbstractScrollArea.dragLeaveEvent()'''
        return QDragLeaveEvent()
    def dragMoveEvent(self):
        '''QDragMoveEvent QAbstractScrollArea.dragMoveEvent()'''
        return QDragMoveEvent()
    def dragEnterEvent(self):
        '''QDragEnterEvent QAbstractScrollArea.dragEnterEvent()'''
        return QDragEnterEvent()
    def contextMenuEvent(self):
        '''QContextMenuEvent QAbstractScrollArea.contextMenuEvent()'''
        return QContextMenuEvent()
    def wheelEvent(self):
        '''QWheelEvent QAbstractScrollArea.wheelEvent()'''
        return QWheelEvent()
    def mouseMoveEvent(self):
        '''QMouseEvent QAbstractScrollArea.mouseMoveEvent()'''
        return QMouseEvent()
    def mouseDoubleClickEvent(self):
        '''QMouseEvent QAbstractScrollArea.mouseDoubleClickEvent()'''
        return QMouseEvent()
    def mouseReleaseEvent(self):
        '''QMouseEvent QAbstractScrollArea.mouseReleaseEvent()'''
        return QMouseEvent()
    def mousePressEvent(self):
        '''QMouseEvent QAbstractScrollArea.mousePressEvent()'''
        return QMouseEvent()
    def paintEvent(self):
        '''QPaintEvent QAbstractScrollArea.paintEvent()'''
        return QPaintEvent()
    def resizeEvent(self):
        '''QResizeEvent QAbstractScrollArea.resizeEvent()'''
        return QResizeEvent()
    def viewportEvent(self):
        '''QEvent QAbstractScrollArea.viewportEvent()'''
        return QEvent()
    def event(self):
        '''QEvent QAbstractScrollArea.event()'''
        return QEvent()
    def viewportSizeHint(self):
        '''QSize QAbstractScrollArea.viewportSizeHint()'''
        return QSize()
    def viewportMargins(self):
        '''QMargins QAbstractScrollArea.viewportMargins()'''
        return QMargins()
    def setViewportMargins(self, left, top, right, bottom):
        '''void QAbstractScrollArea.setViewportMargins(int left, int top, int right, int bottom)'''
    def setViewportMargins(self, margins):
        '''void QAbstractScrollArea.setViewportMargins(QMargins margins)'''
    def sizeHint(self):
        '''QSize QAbstractScrollArea.sizeHint()'''
        return QSize()
    def minimumSizeHint(self):
        '''QSize QAbstractScrollArea.minimumSizeHint()'''
        return QSize()
    def maximumViewportSize(self):
        '''QSize QAbstractScrollArea.maximumViewportSize()'''
        return QSize()
    def viewport(self):
        '''QWidget QAbstractScrollArea.viewport()'''
        return QWidget()
    def horizontalScrollBar(self):
        '''QScrollBar QAbstractScrollArea.horizontalScrollBar()'''
        return QScrollBar()
    def setHorizontalScrollBarPolicy(self):
        '''Qt.ScrollBarPolicy QAbstractScrollArea.setHorizontalScrollBarPolicy()'''
        return Qt.ScrollBarPolicy()
    def horizontalScrollBarPolicy(self):
        '''Qt.ScrollBarPolicy QAbstractScrollArea.horizontalScrollBarPolicy()'''
        return Qt.ScrollBarPolicy()
    def verticalScrollBar(self):
        '''QScrollBar QAbstractScrollArea.verticalScrollBar()'''
        return QScrollBar()
    def setVerticalScrollBarPolicy(self):
        '''Qt.ScrollBarPolicy QAbstractScrollArea.setVerticalScrollBarPolicy()'''
        return Qt.ScrollBarPolicy()
    def verticalScrollBarPolicy(self):
        '''Qt.ScrollBarPolicy QAbstractScrollArea.verticalScrollBarPolicy()'''
        return Qt.ScrollBarPolicy()


class QAbstractItemView(QAbstractScrollArea):
    """"""
    # Enum QAbstractItemView.DropIndicatorPosition
    OnItem = 0
    AboveItem = 0
    BelowItem = 0
    OnViewport = 0

    # Enum QAbstractItemView.State
    NoState = 0
    DraggingState = 0
    DragSelectingState = 0
    EditingState = 0
    ExpandingState = 0
    CollapsingState = 0
    AnimatingState = 0

    # Enum QAbstractItemView.CursorAction
    MoveUp = 0
    MoveDown = 0
    MoveLeft = 0
    MoveRight = 0
    MoveHome = 0
    MoveEnd = 0
    MovePageUp = 0
    MovePageDown = 0
    MoveNext = 0
    MovePrevious = 0

    # Enum QAbstractItemView.SelectionMode
    NoSelection = 0
    SingleSelection = 0
    MultiSelection = 0
    ExtendedSelection = 0
    ContiguousSelection = 0

    # Enum QAbstractItemView.SelectionBehavior
    SelectItems = 0
    SelectRows = 0
    SelectColumns = 0

    # Enum QAbstractItemView.ScrollMode
    ScrollPerItem = 0
    ScrollPerPixel = 0

    # Enum QAbstractItemView.ScrollHint
    EnsureVisible = 0
    PositionAtTop = 0
    PositionAtBottom = 0
    PositionAtCenter = 0

    # Enum QAbstractItemView.EditTrigger
    NoEditTriggers = 0
    CurrentChanged = 0
    DoubleClicked = 0
    SelectedClicked = 0
    EditKeyPressed = 0
    AnyKeyPressed = 0
    AllEditTriggers = 0

    # Enum QAbstractItemView.DragDropMode
    NoDragDrop = 0
    DragOnly = 0
    DropOnly = 0
    DragDrop = 0
    InternalMove = 0

    def __init__(self, parent = None):
        '''void QAbstractItemView.__init__(QWidget parent = None)'''
    def defaultDropAction(self):
        '''Qt.DropAction QAbstractItemView.defaultDropAction()'''
        return Qt.DropAction()
    def setDefaultDropAction(self, dropAction):
        '''void QAbstractItemView.setDefaultDropAction(Qt.DropAction dropAction)'''
    def viewportSizeHint(self):
        '''QSize QAbstractItemView.viewportSizeHint()'''
        return QSize()
    def inputMethodEvent(self, event):
        '''void QAbstractItemView.inputMethodEvent(QInputMethodEvent event)'''
    def focusNextPrevChild(self, next):
        '''bool QAbstractItemView.focusNextPrevChild(bool next)'''
        return bool()
    def autoScrollMargin(self):
        '''int QAbstractItemView.autoScrollMargin()'''
        return int()
    def setAutoScrollMargin(self, margin):
        '''void QAbstractItemView.setAutoScrollMargin(int margin)'''
    def inputMethodQuery(self, query):
        '''QVariant QAbstractItemView.inputMethodQuery(Qt.InputMethodQuery query)'''
        return QVariant()
    def itemDelegateForColumn(self, column):
        '''QAbstractItemDelegate QAbstractItemView.itemDelegateForColumn(int column)'''
        return QAbstractItemDelegate()
    def setItemDelegateForColumn(self, column, delegate):
        '''void QAbstractItemView.setItemDelegateForColumn(int column, QAbstractItemDelegate delegate)'''
    def itemDelegateForRow(self, row):
        '''QAbstractItemDelegate QAbstractItemView.itemDelegateForRow(int row)'''
        return QAbstractItemDelegate()
    def setItemDelegateForRow(self, row, delegate):
        '''void QAbstractItemView.setItemDelegateForRow(int row, QAbstractItemDelegate delegate)'''
    def dragDropMode(self):
        '''QAbstractItemView.DragDropMode QAbstractItemView.dragDropMode()'''
        return QAbstractItemView.DragDropMode()
    def setDragDropMode(self, behavior):
        '''void QAbstractItemView.setDragDropMode(QAbstractItemView.DragDropMode behavior)'''
    def dragDropOverwriteMode(self):
        '''bool QAbstractItemView.dragDropOverwriteMode()'''
        return bool()
    def setDragDropOverwriteMode(self, overwrite):
        '''void QAbstractItemView.setDragDropOverwriteMode(bool overwrite)'''
    def horizontalScrollMode(self):
        '''QAbstractItemView.ScrollMode QAbstractItemView.horizontalScrollMode()'''
        return QAbstractItemView.ScrollMode()
    def setHorizontalScrollMode(self, mode):
        '''void QAbstractItemView.setHorizontalScrollMode(QAbstractItemView.ScrollMode mode)'''
    def verticalScrollMode(self):
        '''QAbstractItemView.ScrollMode QAbstractItemView.verticalScrollMode()'''
        return QAbstractItemView.ScrollMode()
    def setVerticalScrollMode(self, mode):
        '''void QAbstractItemView.setVerticalScrollMode(QAbstractItemView.ScrollMode mode)'''
    def dropIndicatorPosition(self):
        '''QAbstractItemView.DropIndicatorPosition QAbstractItemView.dropIndicatorPosition()'''
        return QAbstractItemView.DropIndicatorPosition()
    def timerEvent(self, e):
        '''void QAbstractItemView.timerEvent(QTimerEvent e)'''
    def resizeEvent(self, e):
        '''void QAbstractItemView.resizeEvent(QResizeEvent e)'''
    def keyPressEvent(self, e):
        '''void QAbstractItemView.keyPressEvent(QKeyEvent e)'''
    def focusOutEvent(self, e):
        '''void QAbstractItemView.focusOutEvent(QFocusEvent e)'''
    def focusInEvent(self, e):
        '''void QAbstractItemView.focusInEvent(QFocusEvent e)'''
    def dropEvent(self, e):
        '''void QAbstractItemView.dropEvent(QDropEvent e)'''
    def dragLeaveEvent(self, e):
        '''void QAbstractItemView.dragLeaveEvent(QDragLeaveEvent e)'''
    def dragMoveEvent(self, e):
        '''void QAbstractItemView.dragMoveEvent(QDragMoveEvent e)'''
    def dragEnterEvent(self, e):
        '''void QAbstractItemView.dragEnterEvent(QDragEnterEvent e)'''
    def mouseDoubleClickEvent(self, e):
        '''void QAbstractItemView.mouseDoubleClickEvent(QMouseEvent e)'''
    def mouseReleaseEvent(self, e):
        '''void QAbstractItemView.mouseReleaseEvent(QMouseEvent e)'''
    def mouseMoveEvent(self, e):
        '''void QAbstractItemView.mouseMoveEvent(QMouseEvent e)'''
    def mousePressEvent(self, e):
        '''void QAbstractItemView.mousePressEvent(QMouseEvent e)'''
    def viewportEvent(self, e):
        '''bool QAbstractItemView.viewportEvent(QEvent e)'''
        return bool()
    def event(self, event):
        '''bool QAbstractItemView.event(QEvent event)'''
        return bool()
    def dirtyRegionOffset(self):
        '''QPoint QAbstractItemView.dirtyRegionOffset()'''
        return QPoint()
    def setDirtyRegion(self, region):
        '''void QAbstractItemView.setDirtyRegion(QRegion region)'''
    def scrollDirtyRegion(self, dx, dy):
        '''void QAbstractItemView.scrollDirtyRegion(int dx, int dy)'''
    def executeDelayedItemsLayout(self):
        '''void QAbstractItemView.executeDelayedItemsLayout()'''
    def scheduleDelayedItemsLayout(self):
        '''void QAbstractItemView.scheduleDelayedItemsLayout()'''
    def setState(self, state):
        '''void QAbstractItemView.setState(QAbstractItemView.State state)'''
    def state(self):
        '''QAbstractItemView.State QAbstractItemView.state()'''
        return QAbstractItemView.State()
    def viewOptions(self):
        '''QStyleOptionViewItem QAbstractItemView.viewOptions()'''
        return QStyleOptionViewItem()
    def startDrag(self, supportedActions):
        '''void QAbstractItemView.startDrag(Qt.DropActions supportedActions)'''
    def selectionCommand(self, index, event = None):
        '''QItemSelectionModel.SelectionFlags QAbstractItemView.selectionCommand(QModelIndex index, QEvent event = None)'''
        return QItemSelectionModel.SelectionFlags()
    def selectedIndexes(self):
        '''list-of-QModelIndex QAbstractItemView.selectedIndexes()'''
        return [QModelIndex()]
    def visualRegionForSelection(self, selection):
        '''abstract QRegion QAbstractItemView.visualRegionForSelection(QItemSelection selection)'''
        return QRegion()
    def setSelection(self, rect, command):
        '''abstract void QAbstractItemView.setSelection(QRect rect, QItemSelectionModel.SelectionFlags command)'''
    def isIndexHidden(self, index):
        '''abstract bool QAbstractItemView.isIndexHidden(QModelIndex index)'''
        return bool()
    def verticalOffset(self):
        '''abstract int QAbstractItemView.verticalOffset()'''
        return int()
    def horizontalOffset(self):
        '''abstract int QAbstractItemView.horizontalOffset()'''
        return int()
    def moveCursor(self, cursorAction, modifiers):
        '''abstract QModelIndex QAbstractItemView.moveCursor(QAbstractItemView.CursorAction cursorAction, Qt.KeyboardModifiers modifiers)'''
        return QModelIndex()
    iconSizeChanged = pyqtSignal() # void iconSizeChanged(const QSizeamp;) - signal
    viewportEntered = pyqtSignal() # void viewportEntered() - signal
    entered = pyqtSignal() # void entered(const QModelIndexamp;) - signal
    activated = pyqtSignal() # void activated(const QModelIndexamp;) - signal
    doubleClicked = pyqtSignal() # void doubleClicked(const QModelIndexamp;) - signal
    clicked = pyqtSignal() # void clicked(const QModelIndexamp;) - signal
    pressed = pyqtSignal() # void pressed(const QModelIndexamp;) - signal
    def editorDestroyed(self, editor):
        '''void QAbstractItemView.editorDestroyed(QObject editor)'''
    def commitData(self, editor):
        '''void QAbstractItemView.commitData(QWidget editor)'''
    def closeEditor(self, editor, hint):
        '''void QAbstractItemView.closeEditor(QWidget editor, QAbstractItemDelegate.EndEditHint hint)'''
    def horizontalScrollbarValueChanged(self, value):
        '''void QAbstractItemView.horizontalScrollbarValueChanged(int value)'''
    def verticalScrollbarValueChanged(self, value):
        '''void QAbstractItemView.verticalScrollbarValueChanged(int value)'''
    def horizontalScrollbarAction(self, action):
        '''void QAbstractItemView.horizontalScrollbarAction(int action)'''
    def verticalScrollbarAction(self, action):
        '''void QAbstractItemView.verticalScrollbarAction(int action)'''
    def updateGeometries(self):
        '''void QAbstractItemView.updateGeometries()'''
    def updateEditorGeometries(self):
        '''void QAbstractItemView.updateEditorGeometries()'''
    def updateEditorData(self):
        '''void QAbstractItemView.updateEditorData()'''
    def currentChanged(self, current, previous):
        '''void QAbstractItemView.currentChanged(QModelIndex current, QModelIndex previous)'''
    def selectionChanged(self, selected, deselected):
        '''void QAbstractItemView.selectionChanged(QItemSelection selected, QItemSelection deselected)'''
    def rowsAboutToBeRemoved(self, parent, start, end):
        '''void QAbstractItemView.rowsAboutToBeRemoved(QModelIndex parent, int start, int end)'''
    def rowsInserted(self, parent, start, end):
        '''void QAbstractItemView.rowsInserted(QModelIndex parent, int start, int end)'''
    def dataChanged(self, topLeft, bottomRight, roles = None):
        '''void QAbstractItemView.dataChanged(QModelIndex topLeft, QModelIndex bottomRight, list-of-int roles = [])'''
    def update(self):
        '''void QAbstractItemView.update()'''
    def update(self, index):
        '''void QAbstractItemView.update(QModelIndex index)'''
    def scrollToBottom(self):
        '''void QAbstractItemView.scrollToBottom()'''
    def scrollToTop(self):
        '''void QAbstractItemView.scrollToTop()'''
    def setCurrentIndex(self, index):
        '''void QAbstractItemView.setCurrentIndex(QModelIndex index)'''
    def clearSelection(self):
        '''void QAbstractItemView.clearSelection()'''
    def edit(self, index):
        '''void QAbstractItemView.edit(QModelIndex index)'''
    def edit(self, index, trigger, event):
        '''bool QAbstractItemView.edit(QModelIndex index, QAbstractItemView.EditTrigger trigger, QEvent event)'''
        return bool()
    def selectAll(self):
        '''void QAbstractItemView.selectAll()'''
    def setRootIndex(self, index):
        '''void QAbstractItemView.setRootIndex(QModelIndex index)'''
    def reset(self):
        '''void QAbstractItemView.reset()'''
    def indexWidget(self, index):
        '''QWidget QAbstractItemView.indexWidget(QModelIndex index)'''
        return QWidget()
    def setIndexWidget(self, index, widget):
        '''void QAbstractItemView.setIndexWidget(QModelIndex index, QWidget widget)'''
    def closePersistentEditor(self, index):
        '''void QAbstractItemView.closePersistentEditor(QModelIndex index)'''
    def openPersistentEditor(self, index):
        '''void QAbstractItemView.openPersistentEditor(QModelIndex index)'''
    def sizeHintForColumn(self, column):
        '''int QAbstractItemView.sizeHintForColumn(int column)'''
        return int()
    def sizeHintForRow(self, row):
        '''int QAbstractItemView.sizeHintForRow(int row)'''
        return int()
    def sizeHintForIndex(self, index):
        '''QSize QAbstractItemView.sizeHintForIndex(QModelIndex index)'''
        return QSize()
    def indexAt(self, p):
        '''abstract QModelIndex QAbstractItemView.indexAt(QPoint p)'''
        return QModelIndex()
    def scrollTo(self, index, hint = None):
        '''abstract void QAbstractItemView.scrollTo(QModelIndex index, QAbstractItemView.ScrollHint hint = QAbstractItemView.EnsureVisible)'''
    def visualRect(self, index):
        '''abstract QRect QAbstractItemView.visualRect(QModelIndex index)'''
        return QRect()
    def keyboardSearch(self, search):
        '''void QAbstractItemView.keyboardSearch(str search)'''
    def textElideMode(self):
        '''Qt.TextElideMode QAbstractItemView.textElideMode()'''
        return Qt.TextElideMode()
    def setTextElideMode(self, mode):
        '''void QAbstractItemView.setTextElideMode(Qt.TextElideMode mode)'''
    def iconSize(self):
        '''QSize QAbstractItemView.iconSize()'''
        return QSize()
    def setIconSize(self, size):
        '''void QAbstractItemView.setIconSize(QSize size)'''
    def alternatingRowColors(self):
        '''bool QAbstractItemView.alternatingRowColors()'''
        return bool()
    def setAlternatingRowColors(self, enable):
        '''void QAbstractItemView.setAlternatingRowColors(bool enable)'''
    def dragEnabled(self):
        '''bool QAbstractItemView.dragEnabled()'''
        return bool()
    def setDragEnabled(self, enable):
        '''void QAbstractItemView.setDragEnabled(bool enable)'''
    def showDropIndicator(self):
        '''bool QAbstractItemView.showDropIndicator()'''
        return bool()
    def setDropIndicatorShown(self, enable):
        '''void QAbstractItemView.setDropIndicatorShown(bool enable)'''
    def tabKeyNavigation(self):
        '''bool QAbstractItemView.tabKeyNavigation()'''
        return bool()
    def setTabKeyNavigation(self, enable):
        '''void QAbstractItemView.setTabKeyNavigation(bool enable)'''
    def hasAutoScroll(self):
        '''bool QAbstractItemView.hasAutoScroll()'''
        return bool()
    def setAutoScroll(self, enable):
        '''void QAbstractItemView.setAutoScroll(bool enable)'''
    def editTriggers(self):
        '''QAbstractItemView.EditTriggers QAbstractItemView.editTriggers()'''
        return QAbstractItemView.EditTriggers()
    def setEditTriggers(self, triggers):
        '''void QAbstractItemView.setEditTriggers(QAbstractItemView.EditTriggers triggers)'''
    def rootIndex(self):
        '''QModelIndex QAbstractItemView.rootIndex()'''
        return QModelIndex()
    def currentIndex(self):
        '''QModelIndex QAbstractItemView.currentIndex()'''
        return QModelIndex()
    def selectionBehavior(self):
        '''QAbstractItemView.SelectionBehavior QAbstractItemView.selectionBehavior()'''
        return QAbstractItemView.SelectionBehavior()
    def setSelectionBehavior(self, behavior):
        '''void QAbstractItemView.setSelectionBehavior(QAbstractItemView.SelectionBehavior behavior)'''
    def selectionMode(self):
        '''QAbstractItemView.SelectionMode QAbstractItemView.selectionMode()'''
        return QAbstractItemView.SelectionMode()
    def setSelectionMode(self, mode):
        '''void QAbstractItemView.setSelectionMode(QAbstractItemView.SelectionMode mode)'''
    def itemDelegate(self):
        '''QAbstractItemDelegate QAbstractItemView.itemDelegate()'''
        return QAbstractItemDelegate()
    def itemDelegate(self, index):
        '''QAbstractItemDelegate QAbstractItemView.itemDelegate(QModelIndex index)'''
        return QAbstractItemDelegate()
    def setItemDelegate(self, delegate):
        '''void QAbstractItemView.setItemDelegate(QAbstractItemDelegate delegate)'''
    def selectionModel(self):
        '''QItemSelectionModel QAbstractItemView.selectionModel()'''
        return QItemSelectionModel()
    def setSelectionModel(self, selectionModel):
        '''void QAbstractItemView.setSelectionModel(QItemSelectionModel selectionModel)'''
    def model(self):
        '''QAbstractItemModel QAbstractItemView.model()'''
        return QAbstractItemModel()
    def setModel(self, model):
        '''void QAbstractItemView.setModel(QAbstractItemModel model)'''
    class EditTriggers():
        """"""
        def __init__(self):
            '''QAbstractItemView.EditTriggers QAbstractItemView.EditTriggers.__init__()'''
            return QAbstractItemView.EditTriggers()
        def __init__(self):
            '''int QAbstractItemView.EditTriggers.__init__()'''
            return int()
        def __init__(self):
            '''void QAbstractItemView.EditTriggers.__init__()'''
        def __bool__(self):
            '''int QAbstractItemView.EditTriggers.__bool__()'''
            return int()
        def __ne__(self, f):
            '''bool QAbstractItemView.EditTriggers.__ne__(QAbstractItemView.EditTriggers f)'''
            return bool()
        def __eq__(self, f):
            '''bool QAbstractItemView.EditTriggers.__eq__(QAbstractItemView.EditTriggers f)'''
            return bool()
        def __invert__(self):
            '''QAbstractItemView.EditTriggers QAbstractItemView.EditTriggers.__invert__()'''
            return QAbstractItemView.EditTriggers()
        def __and__(self, mask):
            '''QAbstractItemView.EditTriggers QAbstractItemView.EditTriggers.__and__(int mask)'''
            return QAbstractItemView.EditTriggers()
        def __xor__(self, f):
            '''QAbstractItemView.EditTriggers QAbstractItemView.EditTriggers.__xor__(QAbstractItemView.EditTriggers f)'''
            return QAbstractItemView.EditTriggers()
        def __xor__(self, f):
            '''QAbstractItemView.EditTriggers QAbstractItemView.EditTriggers.__xor__(int f)'''
            return QAbstractItemView.EditTriggers()
        def __or__(self, f):
            '''QAbstractItemView.EditTriggers QAbstractItemView.EditTriggers.__or__(QAbstractItemView.EditTriggers f)'''
            return QAbstractItemView.EditTriggers()
        def __or__(self, f):
            '''QAbstractItemView.EditTriggers QAbstractItemView.EditTriggers.__or__(int f)'''
            return QAbstractItemView.EditTriggers()
        def __int__(self):
            '''int QAbstractItemView.EditTriggers.__int__()'''
            return int()
        def __ixor__(self, f):
            '''QAbstractItemView.EditTriggers QAbstractItemView.EditTriggers.__ixor__(QAbstractItemView.EditTriggers f)'''
            return QAbstractItemView.EditTriggers()
        def __ior__(self, f):
            '''QAbstractItemView.EditTriggers QAbstractItemView.EditTriggers.__ior__(QAbstractItemView.EditTriggers f)'''
            return QAbstractItemView.EditTriggers()
        def __iand__(self, mask):
            '''QAbstractItemView.EditTriggers QAbstractItemView.EditTriggers.__iand__(int mask)'''
            return QAbstractItemView.EditTriggers()


class QAbstractSlider(QWidget):
    """"""
    # Enum QAbstractSlider.SliderChange
    SliderRangeChange = 0
    SliderOrientationChange = 0
    SliderStepsChange = 0
    SliderValueChange = 0

    # Enum QAbstractSlider.SliderAction
    SliderNoAction = 0
    SliderSingleStepAdd = 0
    SliderSingleStepSub = 0
    SliderPageStepAdd = 0
    SliderPageStepSub = 0
    SliderToMinimum = 0
    SliderToMaximum = 0
    SliderMove = 0

    def __init__(self, parent = None):
        '''void QAbstractSlider.__init__(QWidget parent = None)'''
    def changeEvent(self, e):
        '''void QAbstractSlider.changeEvent(QEvent e)'''
    def wheelEvent(self, e):
        '''void QAbstractSlider.wheelEvent(QWheelEvent e)'''
    def timerEvent(self):
        '''QTimerEvent QAbstractSlider.timerEvent()'''
        return QTimerEvent()
    def keyPressEvent(self, ev):
        '''void QAbstractSlider.keyPressEvent(QKeyEvent ev)'''
    def event(self, e):
        '''bool QAbstractSlider.event(QEvent e)'''
        return bool()
    def sliderChange(self, change):
        '''void QAbstractSlider.sliderChange(QAbstractSlider.SliderChange change)'''
    def repeatAction(self):
        '''QAbstractSlider.SliderAction QAbstractSlider.repeatAction()'''
        return QAbstractSlider.SliderAction()
    def setRepeatAction(self, action, thresholdTime = 500, repeatTime = 50):
        '''void QAbstractSlider.setRepeatAction(QAbstractSlider.SliderAction action, int thresholdTime = 500, int repeatTime = 50)'''
    actionTriggered = pyqtSignal() # void actionTriggered(int) - signal
    rangeChanged = pyqtSignal() # void rangeChanged(int,int) - signal
    sliderReleased = pyqtSignal() # void sliderReleased() - signal
    sliderMoved = pyqtSignal() # void sliderMoved(int) - signal
    sliderPressed = pyqtSignal() # void sliderPressed() - signal
    valueChanged = pyqtSignal() # void valueChanged(int) - signal
    def setOrientation(self):
        '''Qt.Orientation QAbstractSlider.setOrientation()'''
        return Qt.Orientation()
    def setValue(self):
        '''int QAbstractSlider.setValue()'''
        return int()
    def triggerAction(self, action):
        '''void QAbstractSlider.triggerAction(QAbstractSlider.SliderAction action)'''
    def value(self):
        '''int QAbstractSlider.value()'''
        return int()
    def invertedControls(self):
        '''bool QAbstractSlider.invertedControls()'''
        return bool()
    def setInvertedControls(self):
        '''bool QAbstractSlider.setInvertedControls()'''
        return bool()
    def invertedAppearance(self):
        '''bool QAbstractSlider.invertedAppearance()'''
        return bool()
    def setInvertedAppearance(self):
        '''bool QAbstractSlider.setInvertedAppearance()'''
        return bool()
    def sliderPosition(self):
        '''int QAbstractSlider.sliderPosition()'''
        return int()
    def setSliderPosition(self):
        '''int QAbstractSlider.setSliderPosition()'''
        return int()
    def isSliderDown(self):
        '''bool QAbstractSlider.isSliderDown()'''
        return bool()
    def setSliderDown(self):
        '''bool QAbstractSlider.setSliderDown()'''
        return bool()
    def hasTracking(self):
        '''bool QAbstractSlider.hasTracking()'''
        return bool()
    def setTracking(self, enable):
        '''void QAbstractSlider.setTracking(bool enable)'''
    def pageStep(self):
        '''int QAbstractSlider.pageStep()'''
        return int()
    def setPageStep(self):
        '''int QAbstractSlider.setPageStep()'''
        return int()
    def singleStep(self):
        '''int QAbstractSlider.singleStep()'''
        return int()
    def setSingleStep(self):
        '''int QAbstractSlider.setSingleStep()'''
        return int()
    def setRange(self, min, max):
        '''void QAbstractSlider.setRange(int min, int max)'''
    def maximum(self):
        '''int QAbstractSlider.maximum()'''
        return int()
    def setMaximum(self):
        '''int QAbstractSlider.setMaximum()'''
        return int()
    def minimum(self):
        '''int QAbstractSlider.minimum()'''
        return int()
    def setMinimum(self):
        '''int QAbstractSlider.setMinimum()'''
        return int()
    def orientation(self):
        '''Qt.Orientation QAbstractSlider.orientation()'''
        return Qt.Orientation()


class QAbstractSpinBox(QWidget):
    """"""
    # Enum QAbstractSpinBox.CorrectionMode
    CorrectToPreviousValue = 0
    CorrectToNearestValue = 0

    # Enum QAbstractSpinBox.ButtonSymbols
    UpDownArrows = 0
    PlusMinus = 0
    NoButtons = 0

    # Enum QAbstractSpinBox.StepEnabledFlag
    StepNone = 0
    StepUpEnabled = 0
    StepDownEnabled = 0

    def __init__(self, parent = None):
        '''void QAbstractSpinBox.__init__(QWidget parent = None)'''
    def isGroupSeparatorShown(self):
        '''bool QAbstractSpinBox.isGroupSeparatorShown()'''
        return bool()
    def setGroupSeparatorShown(self, shown):
        '''void QAbstractSpinBox.setGroupSeparatorShown(bool shown)'''
    def inputMethodQuery(self):
        '''Qt.InputMethodQuery QAbstractSpinBox.inputMethodQuery()'''
        return Qt.InputMethodQuery()
    def keyboardTracking(self):
        '''bool QAbstractSpinBox.keyboardTracking()'''
        return bool()
    def setKeyboardTracking(self, kt):
        '''void QAbstractSpinBox.setKeyboardTracking(bool kt)'''
    def isAccelerated(self):
        '''bool QAbstractSpinBox.isAccelerated()'''
        return bool()
    def setAccelerated(self, on):
        '''void QAbstractSpinBox.setAccelerated(bool on)'''
    def hasAcceptableInput(self):
        '''bool QAbstractSpinBox.hasAcceptableInput()'''
        return bool()
    def correctionMode(self):
        '''QAbstractSpinBox.CorrectionMode QAbstractSpinBox.correctionMode()'''
        return QAbstractSpinBox.CorrectionMode()
    def setCorrectionMode(self, cm):
        '''void QAbstractSpinBox.setCorrectionMode(QAbstractSpinBox.CorrectionMode cm)'''
    def initStyleOption(self, option):
        '''void QAbstractSpinBox.initStyleOption(QStyleOptionSpinBox option)'''
    def stepEnabled(self):
        '''QAbstractSpinBox.StepEnabled QAbstractSpinBox.stepEnabled()'''
        return QAbstractSpinBox.StepEnabled()
    def setLineEdit(self, e):
        '''void QAbstractSpinBox.setLineEdit(QLineEdit e)'''
    def lineEdit(self):
        '''QLineEdit QAbstractSpinBox.lineEdit()'''
        return QLineEdit()
    def showEvent(self, e):
        '''void QAbstractSpinBox.showEvent(QShowEvent e)'''
    def paintEvent(self, e):
        '''void QAbstractSpinBox.paintEvent(QPaintEvent e)'''
    def timerEvent(self, e):
        '''void QAbstractSpinBox.timerEvent(QTimerEvent e)'''
    def mouseMoveEvent(self, e):
        '''void QAbstractSpinBox.mouseMoveEvent(QMouseEvent e)'''
    def mouseReleaseEvent(self, e):
        '''void QAbstractSpinBox.mouseReleaseEvent(QMouseEvent e)'''
    def mousePressEvent(self, e):
        '''void QAbstractSpinBox.mousePressEvent(QMouseEvent e)'''
    def hideEvent(self, e):
        '''void QAbstractSpinBox.hideEvent(QHideEvent e)'''
    def closeEvent(self, e):
        '''void QAbstractSpinBox.closeEvent(QCloseEvent e)'''
    def changeEvent(self, e):
        '''void QAbstractSpinBox.changeEvent(QEvent e)'''
    def contextMenuEvent(self, e):
        '''void QAbstractSpinBox.contextMenuEvent(QContextMenuEvent e)'''
    def focusOutEvent(self, e):
        '''void QAbstractSpinBox.focusOutEvent(QFocusEvent e)'''
    def focusInEvent(self, e):
        '''void QAbstractSpinBox.focusInEvent(QFocusEvent e)'''
    def wheelEvent(self, e):
        '''void QAbstractSpinBox.wheelEvent(QWheelEvent e)'''
    def keyReleaseEvent(self, e):
        '''void QAbstractSpinBox.keyReleaseEvent(QKeyEvent e)'''
    def keyPressEvent(self, e):
        '''void QAbstractSpinBox.keyPressEvent(QKeyEvent e)'''
    def resizeEvent(self, e):
        '''void QAbstractSpinBox.resizeEvent(QResizeEvent e)'''
    editingFinished = pyqtSignal() # void editingFinished() - signal
    def clear(self):
        '''void QAbstractSpinBox.clear()'''
    def selectAll(self):
        '''void QAbstractSpinBox.selectAll()'''
    def stepDown(self):
        '''void QAbstractSpinBox.stepDown()'''
    def stepUp(self):
        '''void QAbstractSpinBox.stepUp()'''
    def stepBy(self, steps):
        '''void QAbstractSpinBox.stepBy(int steps)'''
    def fixup(self, input):
        '''void QAbstractSpinBox.fixup(str input)'''
    def validate(self, input, pos):
        '''QValidator.State QAbstractSpinBox.validate(str input, int pos)'''
        return QValidator.State()
    def event(self, event):
        '''bool QAbstractSpinBox.event(QEvent event)'''
        return bool()
    def interpretText(self):
        '''void QAbstractSpinBox.interpretText()'''
    def minimumSizeHint(self):
        '''QSize QAbstractSpinBox.minimumSizeHint()'''
        return QSize()
    def sizeHint(self):
        '''QSize QAbstractSpinBox.sizeHint()'''
        return QSize()
    def hasFrame(self):
        '''bool QAbstractSpinBox.hasFrame()'''
        return bool()
    def setFrame(self):
        '''bool QAbstractSpinBox.setFrame()'''
        return bool()
    def alignment(self):
        '''Qt.Alignment QAbstractSpinBox.alignment()'''
        return Qt.Alignment()
    def setAlignment(self, flag):
        '''void QAbstractSpinBox.setAlignment(Qt.Alignment flag)'''
    def isReadOnly(self):
        '''bool QAbstractSpinBox.isReadOnly()'''
        return bool()
    def setReadOnly(self, r):
        '''void QAbstractSpinBox.setReadOnly(bool r)'''
    def setWrapping(self, w):
        '''void QAbstractSpinBox.setWrapping(bool w)'''
    def wrapping(self):
        '''bool QAbstractSpinBox.wrapping()'''
        return bool()
    def setSpecialValueText(self, s):
        '''void QAbstractSpinBox.setSpecialValueText(str s)'''
    def specialValueText(self):
        '''str QAbstractSpinBox.specialValueText()'''
        return str()
    def text(self):
        '''str QAbstractSpinBox.text()'''
        return str()
    def setButtonSymbols(self, bs):
        '''void QAbstractSpinBox.setButtonSymbols(QAbstractSpinBox.ButtonSymbols bs)'''
    def buttonSymbols(self):
        '''QAbstractSpinBox.ButtonSymbols QAbstractSpinBox.buttonSymbols()'''
        return QAbstractSpinBox.ButtonSymbols()
    class StepEnabled():
        """"""
        def __init__(self):
            '''QAbstractSpinBox.StepEnabled QAbstractSpinBox.StepEnabled.__init__()'''
            return QAbstractSpinBox.StepEnabled()
        def __init__(self):
            '''int QAbstractSpinBox.StepEnabled.__init__()'''
            return int()
        def __init__(self):
            '''void QAbstractSpinBox.StepEnabled.__init__()'''
        def __bool__(self):
            '''int QAbstractSpinBox.StepEnabled.__bool__()'''
            return int()
        def __ne__(self, f):
            '''bool QAbstractSpinBox.StepEnabled.__ne__(QAbstractSpinBox.StepEnabled f)'''
            return bool()
        def __eq__(self, f):
            '''bool QAbstractSpinBox.StepEnabled.__eq__(QAbstractSpinBox.StepEnabled f)'''
            return bool()
        def __invert__(self):
            '''QAbstractSpinBox.StepEnabled QAbstractSpinBox.StepEnabled.__invert__()'''
            return QAbstractSpinBox.StepEnabled()
        def __and__(self, mask):
            '''QAbstractSpinBox.StepEnabled QAbstractSpinBox.StepEnabled.__and__(int mask)'''
            return QAbstractSpinBox.StepEnabled()
        def __xor__(self, f):
            '''QAbstractSpinBox.StepEnabled QAbstractSpinBox.StepEnabled.__xor__(QAbstractSpinBox.StepEnabled f)'''
            return QAbstractSpinBox.StepEnabled()
        def __xor__(self, f):
            '''QAbstractSpinBox.StepEnabled QAbstractSpinBox.StepEnabled.__xor__(int f)'''
            return QAbstractSpinBox.StepEnabled()
        def __or__(self, f):
            '''QAbstractSpinBox.StepEnabled QAbstractSpinBox.StepEnabled.__or__(QAbstractSpinBox.StepEnabled f)'''
            return QAbstractSpinBox.StepEnabled()
        def __or__(self, f):
            '''QAbstractSpinBox.StepEnabled QAbstractSpinBox.StepEnabled.__or__(int f)'''
            return QAbstractSpinBox.StepEnabled()
        def __int__(self):
            '''int QAbstractSpinBox.StepEnabled.__int__()'''
            return int()
        def __ixor__(self, f):
            '''QAbstractSpinBox.StepEnabled QAbstractSpinBox.StepEnabled.__ixor__(QAbstractSpinBox.StepEnabled f)'''
            return QAbstractSpinBox.StepEnabled()
        def __ior__(self, f):
            '''QAbstractSpinBox.StepEnabled QAbstractSpinBox.StepEnabled.__ior__(QAbstractSpinBox.StepEnabled f)'''
            return QAbstractSpinBox.StepEnabled()
        def __iand__(self, mask):
            '''QAbstractSpinBox.StepEnabled QAbstractSpinBox.StepEnabled.__iand__(int mask)'''
            return QAbstractSpinBox.StepEnabled()


class QAction(QObject):
    """"""
    # Enum QAction.Priority
    LowPriority = 0
    NormalPriority = 0
    HighPriority = 0

    # Enum QAction.MenuRole
    NoRole = 0
    TextHeuristicRole = 0
    ApplicationSpecificRole = 0
    AboutQtRole = 0
    AboutRole = 0
    PreferencesRole = 0
    QuitRole = 0

    # Enum QAction.ActionEvent
    Trigger = 0
    Hover = 0

    def __init__(self, parent):
        '''void QAction.__init__(QObject parent)'''
    def __init__(self, text, parent):
        '''void QAction.__init__(str text, QObject parent)'''
    def __init__(self, icon, text, parent):
        '''void QAction.__init__(QIcon icon, str text, QObject parent)'''
    def priority(self):
        '''QAction.Priority QAction.priority()'''
        return QAction.Priority()
    def setPriority(self, priority):
        '''void QAction.setPriority(QAction.Priority priority)'''
    def isIconVisibleInMenu(self):
        '''bool QAction.isIconVisibleInMenu()'''
        return bool()
    def setIconVisibleInMenu(self, visible):
        '''void QAction.setIconVisibleInMenu(bool visible)'''
    def associatedGraphicsWidgets(self):
        '''list-of-QGraphicsWidget QAction.associatedGraphicsWidgets()'''
        return [QGraphicsWidget()]
    def associatedWidgets(self):
        '''list-of-QWidget QAction.associatedWidgets()'''
        return [QWidget()]
    def menuRole(self):
        '''QAction.MenuRole QAction.menuRole()'''
        return QAction.MenuRole()
    def setMenuRole(self, menuRole):
        '''void QAction.setMenuRole(QAction.MenuRole menuRole)'''
    def autoRepeat(self):
        '''bool QAction.autoRepeat()'''
        return bool()
    def setAutoRepeat(self):
        '''bool QAction.setAutoRepeat()'''
        return bool()
    def shortcuts(self):
        '''list-of-QKeySequence QAction.shortcuts()'''
        return [QKeySequence()]
    def setShortcuts(self, shortcuts):
        '''void QAction.setShortcuts(list-of-QKeySequence shortcuts)'''
    def setShortcuts(self):
        '''QKeySequence.StandardKey QAction.setShortcuts()'''
        return QKeySequence.StandardKey()
    toggled = pyqtSignal() # void toggled(bool) - signal
    hovered = pyqtSignal() # void hovered() - signal
    triggered = pyqtSignal() # void triggered(bool = 0) - signal
    changed = pyqtSignal() # void changed() - signal
    def setVisible(self):
        '''bool QAction.setVisible()'''
        return bool()
    def setDisabled(self, b):
        '''void QAction.setDisabled(bool b)'''
    def setEnabled(self):
        '''bool QAction.setEnabled()'''
        return bool()
    def toggle(self):
        '''void QAction.toggle()'''
    def setChecked(self):
        '''bool QAction.setChecked()'''
        return bool()
    def hover(self):
        '''void QAction.hover()'''
    def trigger(self):
        '''void QAction.trigger()'''
    def event(self):
        '''QEvent QAction.event()'''
        return QEvent()
    def parentWidget(self):
        '''QWidget QAction.parentWidget()'''
        return QWidget()
    def showStatusText(self, widget = None):
        '''bool QAction.showStatusText(QWidget widget = None)'''
        return bool()
    def activate(self, event):
        '''void QAction.activate(QAction.ActionEvent event)'''
    def isVisible(self):
        '''bool QAction.isVisible()'''
        return bool()
    def isEnabled(self):
        '''bool QAction.isEnabled()'''
        return bool()
    def isChecked(self):
        '''bool QAction.isChecked()'''
        return bool()
    def setData(self, var):
        '''void QAction.setData(QVariant var)'''
    def data(self):
        '''QVariant QAction.data()'''
        return QVariant()
    def isCheckable(self):
        '''bool QAction.isCheckable()'''
        return bool()
    def setCheckable(self):
        '''bool QAction.setCheckable()'''
        return bool()
    def font(self):
        '''QFont QAction.font()'''
        return QFont()
    def setFont(self, font):
        '''void QAction.setFont(QFont font)'''
    def shortcutContext(self):
        '''Qt.ShortcutContext QAction.shortcutContext()'''
        return Qt.ShortcutContext()
    def setShortcutContext(self, context):
        '''void QAction.setShortcutContext(Qt.ShortcutContext context)'''
    def shortcut(self):
        '''QKeySequence QAction.shortcut()'''
        return QKeySequence()
    def setShortcut(self, shortcut):
        '''void QAction.setShortcut(QKeySequence shortcut)'''
    def isSeparator(self):
        '''bool QAction.isSeparator()'''
        return bool()
    def setSeparator(self, b):
        '''void QAction.setSeparator(bool b)'''
    def setMenu(self, menu):
        '''void QAction.setMenu(QMenu menu)'''
    def menu(self):
        '''QMenu QAction.menu()'''
        return QMenu()
    def whatsThis(self):
        '''str QAction.whatsThis()'''
        return str()
    def setWhatsThis(self, what):
        '''void QAction.setWhatsThis(str what)'''
    def statusTip(self):
        '''str QAction.statusTip()'''
        return str()
    def setStatusTip(self, statusTip):
        '''void QAction.setStatusTip(str statusTip)'''
    def toolTip(self):
        '''str QAction.toolTip()'''
        return str()
    def setToolTip(self, tip):
        '''void QAction.setToolTip(str tip)'''
    def iconText(self):
        '''str QAction.iconText()'''
        return str()
    def setIconText(self, text):
        '''void QAction.setIconText(str text)'''
    def text(self):
        '''str QAction.text()'''
        return str()
    def setText(self, text):
        '''void QAction.setText(str text)'''
    def icon(self):
        '''QIcon QAction.icon()'''
        return QIcon()
    def setIcon(self, icon):
        '''void QAction.setIcon(QIcon icon)'''
    def actionGroup(self):
        '''QActionGroup QAction.actionGroup()'''
        return QActionGroup()
    def setActionGroup(self, group):
        '''void QAction.setActionGroup(QActionGroup group)'''


class QActionGroup(QObject):
    """"""
    def __init__(self, parent):
        '''void QActionGroup.__init__(QObject parent)'''
    hovered = pyqtSignal() # void hovered(QAction*) - signal
    triggered = pyqtSignal() # void triggered(QAction*) - signal
    def setExclusive(self):
        '''bool QActionGroup.setExclusive()'''
        return bool()
    def setVisible(self):
        '''bool QActionGroup.setVisible()'''
        return bool()
    def setDisabled(self, b):
        '''void QActionGroup.setDisabled(bool b)'''
    def setEnabled(self):
        '''bool QActionGroup.setEnabled()'''
        return bool()
    def isVisible(self):
        '''bool QActionGroup.isVisible()'''
        return bool()
    def isEnabled(self):
        '''bool QActionGroup.isEnabled()'''
        return bool()
    def isExclusive(self):
        '''bool QActionGroup.isExclusive()'''
        return bool()
    def checkedAction(self):
        '''QAction QActionGroup.checkedAction()'''
        return QAction()
    def actions(self):
        '''list-of-QAction QActionGroup.actions()'''
        return [QAction()]
    def removeAction(self, a):
        '''void QActionGroup.removeAction(QAction a)'''
    def addAction(self, a):
        '''QAction QActionGroup.addAction(QAction a)'''
        return QAction()
    def addAction(self, text):
        '''QAction QActionGroup.addAction(str text)'''
        return QAction()
    def addAction(self, icon, text):
        '''QAction QActionGroup.addAction(QIcon icon, str text)'''
        return QAction()


class QApplication(QGuiApplication):
    """"""
    # Enum QApplication.ColorSpec
    NormalColor = 0
    CustomColor = 0
    ManyColor = 0

    def __init__(self, argv):
        '''void QApplication.__init__(list-of-str argv)'''
    def event(self):
        '''QEvent QApplication.event()'''
        return QEvent()
    def setStyleSheet(self, sheet):
        '''void QApplication.setStyleSheet(str sheet)'''
    def setAutoSipEnabled(self, enabled):
        '''void QApplication.setAutoSipEnabled(bool enabled)'''
    def closeAllWindows(self):
        '''static void QApplication.closeAllWindows()'''
    def aboutQt(self):
        '''static void QApplication.aboutQt()'''
    focusChanged = pyqtSignal() # void focusChanged(QWidget*,QWidget*) - signal
    def styleSheet(self):
        '''str QApplication.styleSheet()'''
        return str()
    def autoSipEnabled(self):
        '''bool QApplication.autoSipEnabled()'''
        return bool()
    def notify(self):
        '''QEvent QApplication.notify()'''
        return QEvent()
    def exec_(self):
        '''static int QApplication.exec_()'''
        return int()
    def setEffectEnabled(self, enabled = True):
        '''static Qt.UIEffect QApplication.setEffectEnabled(bool enabled = True)'''
        return Qt.UIEffect()
    def isEffectEnabled(self):
        '''static Qt.UIEffect QApplication.isEffectEnabled()'''
        return Qt.UIEffect()
    def startDragDistance(self):
        '''static int QApplication.startDragDistance()'''
        return int()
    def setStartDragDistance(self, l):
        '''static void QApplication.setStartDragDistance(int l)'''
    def startDragTime(self):
        '''static int QApplication.startDragTime()'''
        return int()
    def setStartDragTime(self, ms):
        '''static void QApplication.setStartDragTime(int ms)'''
    def globalStrut(self):
        '''static QSize QApplication.globalStrut()'''
        return QSize()
    def setGlobalStrut(self):
        '''static QSize QApplication.setGlobalStrut()'''
        return QSize()
    def wheelScrollLines(self):
        '''static int QApplication.wheelScrollLines()'''
        return int()
    def setWheelScrollLines(self):
        '''static int QApplication.setWheelScrollLines()'''
        return int()
    def keyboardInputInterval(self):
        '''static int QApplication.keyboardInputInterval()'''
        return int()
    def setKeyboardInputInterval(self):
        '''static int QApplication.setKeyboardInputInterval()'''
        return int()
    def doubleClickInterval(self):
        '''static int QApplication.doubleClickInterval()'''
        return int()
    def setDoubleClickInterval(self):
        '''static int QApplication.setDoubleClickInterval()'''
        return int()
    def cursorFlashTime(self):
        '''static int QApplication.cursorFlashTime()'''
        return int()
    def setCursorFlashTime(self):
        '''static int QApplication.setCursorFlashTime()'''
        return int()
    def alert(self, widget, msecs = 0):
        '''static void QApplication.alert(QWidget widget, int msecs = 0)'''
    def beep(self):
        '''static void QApplication.beep()'''
    def topLevelAt(self, p):
        '''static QWidget QApplication.topLevelAt(QPoint p)'''
        return QWidget()
    def topLevelAt(self, x, y):
        '''static QWidget QApplication.topLevelAt(int x, int y)'''
        return QWidget()
    def widgetAt(self, p):
        '''static QWidget QApplication.widgetAt(QPoint p)'''
        return QWidget()
    def widgetAt(self, x, y):
        '''static QWidget QApplication.widgetAt(int x, int y)'''
        return QWidget()
    def setActiveWindow(self, act):
        '''static void QApplication.setActiveWindow(QWidget act)'''
    def activeWindow(self):
        '''static QWidget QApplication.activeWindow()'''
        return QWidget()
    def focusWidget(self):
        '''static QWidget QApplication.focusWidget()'''
        return QWidget()
    def activeModalWidget(self):
        '''static QWidget QApplication.activeModalWidget()'''
        return QWidget()
    def activePopupWidget(self):
        '''static QWidget QApplication.activePopupWidget()'''
        return QWidget()
    def desktop(self):
        '''static QDesktopWidget QApplication.desktop()'''
        return QDesktopWidget()
    def topLevelWidgets(self):
        '''static list-of-QWidget QApplication.topLevelWidgets()'''
        return [QWidget()]
    def allWidgets(self):
        '''static list-of-QWidget QApplication.allWidgets()'''
        return [QWidget()]
    def windowIcon(self):
        '''static QIcon QApplication.windowIcon()'''
        return QIcon()
    def setWindowIcon(self, icon):
        '''static void QApplication.setWindowIcon(QIcon icon)'''
    def fontMetrics(self):
        '''static QFontMetrics QApplication.fontMetrics()'''
        return QFontMetrics()
    def setFont(self, className = None):
        '''static QFont QApplication.setFont(str className = None)'''
        return QFont()
    def font(self):
        '''static QFont QApplication.font()'''
        return QFont()
    def font(self):
        '''static QWidget QApplication.font()'''
        return QWidget()
    def font(self, className):
        '''static QFont QApplication.font(str className)'''
        return QFont()
    def setPalette(self, className = None):
        '''static QPalette QApplication.setPalette(str className = None)'''
        return QPalette()
    def palette(self):
        '''static QPalette QApplication.palette()'''
        return QPalette()
    def palette(self):
        '''static QWidget QApplication.palette()'''
        return QWidget()
    def palette(self, className):
        '''static QPalette QApplication.palette(str className)'''
        return QPalette()
    def setColorSpec(self):
        '''static int QApplication.setColorSpec()'''
        return int()
    def colorSpec(self):
        '''static int QApplication.colorSpec()'''
        return int()
    def setStyle(self):
        '''static QStyle QApplication.setStyle()'''
        return QStyle()
    def setStyle(self):
        '''static str QApplication.setStyle()'''
        return str()
    def style(self):
        '''static QStyle QApplication.style()'''
        return QStyle()


class QLayoutItem():
    """"""
    def __init__(self, alignment = 0):
        '''void QLayoutItem.__init__(Qt.Alignment alignment = 0)'''
    def __init__(self):
        '''QLayoutItem QLayoutItem.__init__()'''
        return QLayoutItem()
    def controlTypes(self):
        '''QSizePolicy.ControlTypes QLayoutItem.controlTypes()'''
        return QSizePolicy.ControlTypes()
    def setAlignment(self, a):
        '''void QLayoutItem.setAlignment(Qt.Alignment a)'''
    def alignment(self):
        '''Qt.Alignment QLayoutItem.alignment()'''
        return Qt.Alignment()
    def spacerItem(self):
        '''QSpacerItem QLayoutItem.spacerItem()'''
        return QSpacerItem()
    def layout(self):
        '''QLayout QLayoutItem.layout()'''
        return QLayout()
    def widget(self):
        '''QWidget QLayoutItem.widget()'''
        return QWidget()
    def invalidate(self):
        '''void QLayoutItem.invalidate()'''
    def minimumHeightForWidth(self):
        '''int QLayoutItem.minimumHeightForWidth()'''
        return int()
    def heightForWidth(self):
        '''int QLayoutItem.heightForWidth()'''
        return int()
    def hasHeightForWidth(self):
        '''bool QLayoutItem.hasHeightForWidth()'''
        return bool()
    def isEmpty(self):
        '''abstract bool QLayoutItem.isEmpty()'''
        return bool()
    def geometry(self):
        '''abstract QRect QLayoutItem.geometry()'''
        return QRect()
    def setGeometry(self):
        '''abstract QRect QLayoutItem.setGeometry()'''
        return QRect()
    def expandingDirections(self):
        '''abstract Qt.Orientations QLayoutItem.expandingDirections()'''
        return Qt.Orientations()
    def maximumSize(self):
        '''abstract QSize QLayoutItem.maximumSize()'''
        return QSize()
    def minimumSize(self):
        '''abstract QSize QLayoutItem.minimumSize()'''
        return QSize()
    def sizeHint(self):
        '''abstract QSize QLayoutItem.sizeHint()'''
        return QSize()


class QLayout(QObject, QLayoutItem):
    """"""
    # Enum QLayout.SizeConstraint
    SetDefaultConstraint = 0
    SetNoConstraint = 0
    SetMinimumSize = 0
    SetFixedSize = 0
    SetMaximumSize = 0
    SetMinAndMaxSize = 0

    def __init__(self, parent):
        '''void QLayout.__init__(QWidget parent)'''
    def __init__(self):
        '''void QLayout.__init__()'''
    def replaceWidget(self, from_, to, options = None):
        '''QLayoutItem QLayout.replaceWidget(QWidget from, QWidget to, Qt.FindChildOptions options = Qt.FindChildrenRecursively)'''
        return QLayoutItem()
    def controlTypes(self):
        '''QSizePolicy.ControlTypes QLayout.controlTypes()'''
        return QSizePolicy.ControlTypes()
    def contentsMargins(self):
        '''QMargins QLayout.contentsMargins()'''
        return QMargins()
    def contentsRect(self):
        '''QRect QLayout.contentsRect()'''
        return QRect()
    def getContentsMargins(self, left, top, right, bottom):
        '''void QLayout.getContentsMargins(int left, int top, int right, int bottom)'''
    def setContentsMargins(self, left, top, right, bottom):
        '''void QLayout.setContentsMargins(int left, int top, int right, int bottom)'''
    def setContentsMargins(self, margins):
        '''void QLayout.setContentsMargins(QMargins margins)'''
    def alignmentRect(self):
        '''QRect QLayout.alignmentRect()'''
        return QRect()
    def addChildWidget(self, w):
        '''void QLayout.addChildWidget(QWidget w)'''
    def addChildLayout(self, l):
        '''void QLayout.addChildLayout(QLayout l)'''
    def childEvent(self, e):
        '''void QLayout.childEvent(QChildEvent e)'''
    def widgetEvent(self):
        '''QEvent QLayout.widgetEvent()'''
        return QEvent()
    def closestAcceptableSize(self, w, s):
        '''static QSize QLayout.closestAcceptableSize(QWidget w, QSize s)'''
        return QSize()
    def isEnabled(self):
        '''bool QLayout.isEnabled()'''
        return bool()
    def setEnabled(self):
        '''bool QLayout.setEnabled()'''
        return bool()
    def layout(self):
        '''QLayout QLayout.layout()'''
        return QLayout()
    def totalSizeHint(self):
        '''QSize QLayout.totalSizeHint()'''
        return QSize()
    def totalMaximumSize(self):
        '''QSize QLayout.totalMaximumSize()'''
        return QSize()
    def totalMinimumSize(self):
        '''QSize QLayout.totalMinimumSize()'''
        return QSize()
    def totalHeightForWidth(self, w):
        '''int QLayout.totalHeightForWidth(int w)'''
        return int()
    def isEmpty(self):
        '''bool QLayout.isEmpty()'''
        return bool()
    def __len__(self):
        ''' QLayout.__len__()'''
        return ()
    def count(self):
        '''abstract int QLayout.count()'''
        return int()
    def indexOf(self):
        '''QWidget QLayout.indexOf()'''
        return QWidget()
    def takeAt(self, index):
        '''abstract QLayoutItem QLayout.takeAt(int index)'''
        return QLayoutItem()
    def itemAt(self, index):
        '''abstract QLayoutItem QLayout.itemAt(int index)'''
        return QLayoutItem()
    def setGeometry(self):
        '''QRect QLayout.setGeometry()'''
        return QRect()
    def maximumSize(self):
        '''QSize QLayout.maximumSize()'''
        return QSize()
    def minimumSize(self):
        '''QSize QLayout.minimumSize()'''
        return QSize()
    def expandingDirections(self):
        '''Qt.Orientations QLayout.expandingDirections()'''
        return Qt.Orientations()
    def removeItem(self):
        '''QLayoutItem QLayout.removeItem()'''
        return QLayoutItem()
    def removeWidget(self, w):
        '''void QLayout.removeWidget(QWidget w)'''
    def addItem(self):
        '''abstract QLayoutItem QLayout.addItem()'''
        return QLayoutItem()
    def addWidget(self, w):
        '''void QLayout.addWidget(QWidget w)'''
    def update(self):
        '''void QLayout.update()'''
    def activate(self):
        '''bool QLayout.activate()'''
        return bool()
    def geometry(self):
        '''QRect QLayout.geometry()'''
        return QRect()
    def invalidate(self):
        '''void QLayout.invalidate()'''
    def parentWidget(self):
        '''QWidget QLayout.parentWidget()'''
        return QWidget()
    def menuBar(self):
        '''QWidget QLayout.menuBar()'''
        return QWidget()
    def setMenuBar(self, w):
        '''void QLayout.setMenuBar(QWidget w)'''
    def sizeConstraint(self):
        '''QLayout.SizeConstraint QLayout.sizeConstraint()'''
        return QLayout.SizeConstraint()
    def setSizeConstraint(self):
        '''QLayout.SizeConstraint QLayout.setSizeConstraint()'''
        return QLayout.SizeConstraint()
    def setAlignment(self, w, alignment):
        '''bool QLayout.setAlignment(QWidget w, Qt.Alignment alignment)'''
        return bool()
    def setAlignment(self, l, alignment):
        '''bool QLayout.setAlignment(QLayout l, Qt.Alignment alignment)'''
        return bool()
    def setAlignment(self, alignment):
        '''void QLayout.setAlignment(Qt.Alignment alignment)'''
    def setSpacing(self):
        '''int QLayout.setSpacing()'''
        return int()
    def spacing(self):
        '''int QLayout.spacing()'''
        return int()


class QBoxLayout(QLayout):
    """"""
    # Enum QBoxLayout.Direction
    LeftToRight = 0
    RightToLeft = 0
    TopToBottom = 0
    BottomToTop = 0
    Down = 0
    Up = 0

    def __init__(self, direction, parent = None):
        '''void QBoxLayout.__init__(QBoxLayout.Direction direction, QWidget parent = None)'''
    def insertItem(self, index):
        '''QLayoutItem QBoxLayout.insertItem(int index)'''
        return QLayoutItem()
    def stretch(self, index):
        '''int QBoxLayout.stretch(int index)'''
        return int()
    def setStretch(self, index, stretch):
        '''void QBoxLayout.setStretch(int index, int stretch)'''
    def insertSpacerItem(self, index, spacerItem):
        '''void QBoxLayout.insertSpacerItem(int index, QSpacerItem spacerItem)'''
    def addSpacerItem(self, spacerItem):
        '''void QBoxLayout.addSpacerItem(QSpacerItem spacerItem)'''
    def setSpacing(self, spacing):
        '''void QBoxLayout.setSpacing(int spacing)'''
    def spacing(self):
        '''int QBoxLayout.spacing()'''
        return int()
    def setGeometry(self):
        '''QRect QBoxLayout.setGeometry()'''
        return QRect()
    def count(self):
        '''int QBoxLayout.count()'''
        return int()
    def takeAt(self):
        '''int QBoxLayout.takeAt()'''
        return int()
    def itemAt(self):
        '''int QBoxLayout.itemAt()'''
        return int()
    def invalidate(self):
        '''void QBoxLayout.invalidate()'''
    def expandingDirections(self):
        '''Qt.Orientations QBoxLayout.expandingDirections()'''
        return Qt.Orientations()
    def minimumHeightForWidth(self):
        '''int QBoxLayout.minimumHeightForWidth()'''
        return int()
    def heightForWidth(self):
        '''int QBoxLayout.heightForWidth()'''
        return int()
    def hasHeightForWidth(self):
        '''bool QBoxLayout.hasHeightForWidth()'''
        return bool()
    def maximumSize(self):
        '''QSize QBoxLayout.maximumSize()'''
        return QSize()
    def minimumSize(self):
        '''QSize QBoxLayout.minimumSize()'''
        return QSize()
    def sizeHint(self):
        '''QSize QBoxLayout.sizeHint()'''
        return QSize()
    def setStretchFactor(self, w, stretch):
        '''bool QBoxLayout.setStretchFactor(QWidget w, int stretch)'''
        return bool()
    def setStretchFactor(self, l, stretch):
        '''bool QBoxLayout.setStretchFactor(QLayout l, int stretch)'''
        return bool()
    def insertLayout(self, index, layout, stretch = 0):
        '''void QBoxLayout.insertLayout(int index, QLayout layout, int stretch = 0)'''
    def insertWidget(self, index, widget, stretch = 0, alignment = 0):
        '''void QBoxLayout.insertWidget(int index, QWidget widget, int stretch = 0, Qt.Alignment alignment = 0)'''
    def insertStretch(self, index, stretch = 0):
        '''void QBoxLayout.insertStretch(int index, int stretch = 0)'''
    def insertSpacing(self, index, size):
        '''void QBoxLayout.insertSpacing(int index, int size)'''
    def addItem(self):
        '''QLayoutItem QBoxLayout.addItem()'''
        return QLayoutItem()
    def addStrut(self):
        '''int QBoxLayout.addStrut()'''
        return int()
    def addLayout(self, layout, stretch = 0):
        '''void QBoxLayout.addLayout(QLayout layout, int stretch = 0)'''
    def addWidget(self, stretch = 0, alignment = 0):
        '''QWidget QBoxLayout.addWidget(int stretch = 0, Qt.Alignment alignment = 0)'''
        return QWidget()
    def addStretch(self, stretch = 0):
        '''void QBoxLayout.addStretch(int stretch = 0)'''
    def addSpacing(self, size):
        '''void QBoxLayout.addSpacing(int size)'''
    def setDirection(self):
        '''QBoxLayout.Direction QBoxLayout.setDirection()'''
        return QBoxLayout.Direction()
    def direction(self):
        '''QBoxLayout.Direction QBoxLayout.direction()'''
        return QBoxLayout.Direction()


class QHBoxLayout(QBoxLayout):
    """"""
    def __init__(self):
        '''void QHBoxLayout.__init__()'''
    def __init__(self, parent):
        '''void QHBoxLayout.__init__(QWidget parent)'''


class QVBoxLayout(QBoxLayout):
    """"""
    def __init__(self):
        '''void QVBoxLayout.__init__()'''
    def __init__(self, parent):
        '''void QVBoxLayout.__init__(QWidget parent)'''


class QButtonGroup(QObject):
    """"""
    def __init__(self, parent = None):
        '''void QButtonGroup.__init__(QObject parent = None)'''
    buttonToggled = pyqtSignal() # void buttonToggled(QAbstractButton*,bool) - signal
    buttonToggled = pyqtSignal() # void buttonToggled(int,bool) - signal
    buttonReleased = pyqtSignal() # void buttonReleased(QAbstractButton*) - signal
    buttonReleased = pyqtSignal() # void buttonReleased(int) - signal
    buttonPressed = pyqtSignal() # void buttonPressed(QAbstractButton*) - signal
    buttonPressed = pyqtSignal() # void buttonPressed(int) - signal
    buttonClicked = pyqtSignal() # void buttonClicked(QAbstractButton*) - signal
    buttonClicked = pyqtSignal() # void buttonClicked(int) - signal
    def checkedId(self):
        '''int QButtonGroup.checkedId()'''
        return int()
    def id(self, button):
        '''int QButtonGroup.id(QAbstractButton button)'''
        return int()
    def setId(self, button, id):
        '''void QButtonGroup.setId(QAbstractButton button, int id)'''
    def checkedButton(self):
        '''QAbstractButton QButtonGroup.checkedButton()'''
        return QAbstractButton()
    def button(self, id):
        '''QAbstractButton QButtonGroup.button(int id)'''
        return QAbstractButton()
    def buttons(self):
        '''list-of-QAbstractButton QButtonGroup.buttons()'''
        return [QAbstractButton()]
    def removeButton(self):
        '''QAbstractButton QButtonGroup.removeButton()'''
        return QAbstractButton()
    def addButton(self, id = None):
        '''QAbstractButton QButtonGroup.addButton(int id = -1)'''
        return QAbstractButton()
    def exclusive(self):
        '''bool QButtonGroup.exclusive()'''
        return bool()
    def setExclusive(self):
        '''bool QButtonGroup.setExclusive()'''
        return bool()


class QCalendarWidget(QWidget):
    """"""
    # Enum QCalendarWidget.SelectionMode
    NoSelection = 0
    SingleSelection = 0

    # Enum QCalendarWidget.VerticalHeaderFormat
    NoVerticalHeader = 0
    ISOWeekNumbers = 0

    # Enum QCalendarWidget.HorizontalHeaderFormat
    NoHorizontalHeader = 0
    SingleLetterDayNames = 0
    ShortDayNames = 0
    LongDayNames = 0

    def __init__(self, parent = None):
        '''void QCalendarWidget.__init__(QWidget parent = None)'''
    def setNavigationBarVisible(self, visible):
        '''void QCalendarWidget.setNavigationBarVisible(bool visible)'''
    def setDateEditAcceptDelay(self, delay):
        '''void QCalendarWidget.setDateEditAcceptDelay(int delay)'''
    def dateEditAcceptDelay(self):
        '''int QCalendarWidget.dateEditAcceptDelay()'''
        return int()
    def setDateEditEnabled(self, enable):
        '''void QCalendarWidget.setDateEditEnabled(bool enable)'''
    def isDateEditEnabled(self):
        '''bool QCalendarWidget.isDateEditEnabled()'''
        return bool()
    def isNavigationBarVisible(self):
        '''bool QCalendarWidget.isNavigationBarVisible()'''
        return bool()
    selectionChanged = pyqtSignal() # void selectionChanged() - signal
    currentPageChanged = pyqtSignal() # void currentPageChanged(int,int) - signal
    clicked = pyqtSignal() # void clicked(const QDateamp;) - signal
    activated = pyqtSignal() # void activated(const QDateamp;) - signal
    def showToday(self):
        '''void QCalendarWidget.showToday()'''
    def showSelectedDate(self):
        '''void QCalendarWidget.showSelectedDate()'''
    def showPreviousYear(self):
        '''void QCalendarWidget.showPreviousYear()'''
    def showPreviousMonth(self):
        '''void QCalendarWidget.showPreviousMonth()'''
    def showNextYear(self):
        '''void QCalendarWidget.showNextYear()'''
    def showNextMonth(self):
        '''void QCalendarWidget.showNextMonth()'''
    def setSelectedDate(self, date):
        '''void QCalendarWidget.setSelectedDate(QDate date)'''
    def setDateRange(self, min, max):
        '''void QCalendarWidget.setDateRange(QDate min, QDate max)'''
    def setCurrentPage(self, year, month):
        '''void QCalendarWidget.setCurrentPage(int year, int month)'''
    def paintCell(self, painter, rect, date):
        '''void QCalendarWidget.paintCell(QPainter painter, QRect rect, QDate date)'''
    def keyPressEvent(self, event):
        '''void QCalendarWidget.keyPressEvent(QKeyEvent event)'''
    def resizeEvent(self, event):
        '''void QCalendarWidget.resizeEvent(QResizeEvent event)'''
    def mousePressEvent(self, event):
        '''void QCalendarWidget.mousePressEvent(QMouseEvent event)'''
    def eventFilter(self, watched, event):
        '''bool QCalendarWidget.eventFilter(QObject watched, QEvent event)'''
        return bool()
    def event(self, event):
        '''bool QCalendarWidget.event(QEvent event)'''
        return bool()
    def updateCells(self):
        '''void QCalendarWidget.updateCells()'''
    def updateCell(self, date):
        '''void QCalendarWidget.updateCell(QDate date)'''
    def setDateTextFormat(self, date, color):
        '''void QCalendarWidget.setDateTextFormat(QDate date, QTextCharFormat color)'''
    def dateTextFormat(self):
        '''dict-of-QDate-QTextCharFormat QCalendarWidget.dateTextFormat()'''
        return {QDate():QTextCharFormat()}
    def dateTextFormat(self, date):
        '''QTextCharFormat QCalendarWidget.dateTextFormat(QDate date)'''
        return QTextCharFormat()
    def setWeekdayTextFormat(self, dayOfWeek, format):
        '''void QCalendarWidget.setWeekdayTextFormat(Qt.DayOfWeek dayOfWeek, QTextCharFormat format)'''
    def weekdayTextFormat(self, dayOfWeek):
        '''QTextCharFormat QCalendarWidget.weekdayTextFormat(Qt.DayOfWeek dayOfWeek)'''
        return QTextCharFormat()
    def setHeaderTextFormat(self, format):
        '''void QCalendarWidget.setHeaderTextFormat(QTextCharFormat format)'''
    def headerTextFormat(self):
        '''QTextCharFormat QCalendarWidget.headerTextFormat()'''
        return QTextCharFormat()
    def setVerticalHeaderFormat(self, format):
        '''void QCalendarWidget.setVerticalHeaderFormat(QCalendarWidget.VerticalHeaderFormat format)'''
    def verticalHeaderFormat(self):
        '''QCalendarWidget.VerticalHeaderFormat QCalendarWidget.verticalHeaderFormat()'''
        return QCalendarWidget.VerticalHeaderFormat()
    def setHorizontalHeaderFormat(self, format):
        '''void QCalendarWidget.setHorizontalHeaderFormat(QCalendarWidget.HorizontalHeaderFormat format)'''
    def horizontalHeaderFormat(self):
        '''QCalendarWidget.HorizontalHeaderFormat QCalendarWidget.horizontalHeaderFormat()'''
        return QCalendarWidget.HorizontalHeaderFormat()
    def setSelectionMode(self, mode):
        '''void QCalendarWidget.setSelectionMode(QCalendarWidget.SelectionMode mode)'''
    def selectionMode(self):
        '''QCalendarWidget.SelectionMode QCalendarWidget.selectionMode()'''
        return QCalendarWidget.SelectionMode()
    def setGridVisible(self, show):
        '''void QCalendarWidget.setGridVisible(bool show)'''
    def isGridVisible(self):
        '''bool QCalendarWidget.isGridVisible()'''
        return bool()
    def setFirstDayOfWeek(self, dayOfWeek):
        '''void QCalendarWidget.setFirstDayOfWeek(Qt.DayOfWeek dayOfWeek)'''
    def firstDayOfWeek(self):
        '''Qt.DayOfWeek QCalendarWidget.firstDayOfWeek()'''
        return Qt.DayOfWeek()
    def setMaximumDate(self, date):
        '''void QCalendarWidget.setMaximumDate(QDate date)'''
    def maximumDate(self):
        '''QDate QCalendarWidget.maximumDate()'''
        return QDate()
    def setMinimumDate(self, date):
        '''void QCalendarWidget.setMinimumDate(QDate date)'''
    def minimumDate(self):
        '''QDate QCalendarWidget.minimumDate()'''
        return QDate()
    def monthShown(self):
        '''int QCalendarWidget.monthShown()'''
        return int()
    def yearShown(self):
        '''int QCalendarWidget.yearShown()'''
        return int()
    def selectedDate(self):
        '''QDate QCalendarWidget.selectedDate()'''
        return QDate()
    def minimumSizeHint(self):
        '''QSize QCalendarWidget.minimumSizeHint()'''
        return QSize()
    def sizeHint(self):
        '''QSize QCalendarWidget.sizeHint()'''
        return QSize()


class QCheckBox(QAbstractButton):
    """"""
    def __init__(self, parent = None):
        '''void QCheckBox.__init__(QWidget parent = None)'''
    def __init__(self, text, parent = None):
        '''void QCheckBox.__init__(str text, QWidget parent = None)'''
    def initStyleOption(self, option):
        '''void QCheckBox.initStyleOption(QStyleOptionButton option)'''
    def mouseMoveEvent(self):
        '''QMouseEvent QCheckBox.mouseMoveEvent()'''
        return QMouseEvent()
    def paintEvent(self):
        '''QPaintEvent QCheckBox.paintEvent()'''
        return QPaintEvent()
    def event(self, e):
        '''bool QCheckBox.event(QEvent e)'''
        return bool()
    def nextCheckState(self):
        '''void QCheckBox.nextCheckState()'''
    def checkStateSet(self):
        '''void QCheckBox.checkStateSet()'''
    def hitButton(self, pos):
        '''bool QCheckBox.hitButton(QPoint pos)'''
        return bool()
    stateChanged = pyqtSignal() # void stateChanged(int) - signal
    def minimumSizeHint(self):
        '''QSize QCheckBox.minimumSizeHint()'''
        return QSize()
    def setCheckState(self, state):
        '''void QCheckBox.setCheckState(Qt.CheckState state)'''
    def checkState(self):
        '''Qt.CheckState QCheckBox.checkState()'''
        return Qt.CheckState()
    def isTristate(self):
        '''bool QCheckBox.isTristate()'''
        return bool()
    def setTristate(self, on = True):
        '''void QCheckBox.setTristate(bool on = True)'''
    def sizeHint(self):
        '''QSize QCheckBox.sizeHint()'''
        return QSize()


class QDialog(QWidget):
    """"""
    # Enum QDialog.DialogCode
    Rejected = 0
    Accepted = 0

    def __init__(self, parent = None, flags = 0):
        '''void QDialog.__init__(QWidget parent = None, Qt.WindowFlags flags = 0)'''
    def eventFilter(self):
        '''QEvent QDialog.eventFilter()'''
        return QEvent()
    def contextMenuEvent(self):
        '''QContextMenuEvent QDialog.contextMenuEvent()'''
        return QContextMenuEvent()
    def resizeEvent(self):
        '''QResizeEvent QDialog.resizeEvent()'''
        return QResizeEvent()
    def showEvent(self):
        '''QShowEvent QDialog.showEvent()'''
        return QShowEvent()
    def closeEvent(self):
        '''QCloseEvent QDialog.closeEvent()'''
        return QCloseEvent()
    def keyPressEvent(self):
        '''QKeyEvent QDialog.keyPressEvent()'''
        return QKeyEvent()
    rejected = pyqtSignal() # void rejected() - signal
    finished = pyqtSignal() # void finished(int) - signal
    accepted = pyqtSignal() # void accepted() - signal
    def open(self):
        '''void QDialog.open()'''
    def reject(self):
        '''void QDialog.reject()'''
    def accept(self):
        '''void QDialog.accept()'''
    def done(self):
        '''int QDialog.done()'''
        return int()
    def exec_(self):
        '''int QDialog.exec_()'''
        return int()
    def setResult(self, r):
        '''void QDialog.setResult(int r)'''
    def setModal(self, modal):
        '''void QDialog.setModal(bool modal)'''
    def isSizeGripEnabled(self):
        '''bool QDialog.isSizeGripEnabled()'''
        return bool()
    def setSizeGripEnabled(self):
        '''bool QDialog.setSizeGripEnabled()'''
        return bool()
    def minimumSizeHint(self):
        '''QSize QDialog.minimumSizeHint()'''
        return QSize()
    def sizeHint(self):
        '''QSize QDialog.sizeHint()'''
        return QSize()
    def setVisible(self, visible):
        '''void QDialog.setVisible(bool visible)'''
    def result(self):
        '''int QDialog.result()'''
        return int()


class QColorDialog(QDialog):
    """"""
    # Enum QColorDialog.ColorDialogOption
    ShowAlphaChannel = 0
    NoButtons = 0
    DontUseNativeDialog = 0

    def __init__(self, parent = None):
        '''void QColorDialog.__init__(QWidget parent = None)'''
    def __init__(self, initial, parent = None):
        '''void QColorDialog.__init__(QColor initial, QWidget parent = None)'''
    def setVisible(self, visible):
        '''void QColorDialog.setVisible(bool visible)'''
    def open(self):
        '''void QColorDialog.open()'''
    def open(self, slot):
        '''void QColorDialog.open(slot slot)'''
    def options(self):
        '''QColorDialog.ColorDialogOptions QColorDialog.options()'''
        return QColorDialog.ColorDialogOptions()
    def setOptions(self, options):
        '''void QColorDialog.setOptions(QColorDialog.ColorDialogOptions options)'''
    def testOption(self, option):
        '''bool QColorDialog.testOption(QColorDialog.ColorDialogOption option)'''
        return bool()
    def setOption(self, option, on = True):
        '''void QColorDialog.setOption(QColorDialog.ColorDialogOption option, bool on = True)'''
    def selectedColor(self):
        '''QColor QColorDialog.selectedColor()'''
        return QColor()
    def currentColor(self):
        '''QColor QColorDialog.currentColor()'''
        return QColor()
    def setCurrentColor(self, color):
        '''void QColorDialog.setCurrentColor(QColor color)'''
    def done(self, result):
        '''void QColorDialog.done(int result)'''
    def changeEvent(self, e):
        '''void QColorDialog.changeEvent(QEvent e)'''
    currentColorChanged = pyqtSignal() # void currentColorChanged(const QColoramp;) - signal
    colorSelected = pyqtSignal() # void colorSelected(const QColoramp;) - signal
    def setStandardColor(self, index, color):
        '''static void QColorDialog.setStandardColor(int index, QColor color)'''
    def standardColor(self, index):
        '''static QColor QColorDialog.standardColor(int index)'''
        return QColor()
    def setCustomColor(self, index, color):
        '''static void QColorDialog.setCustomColor(int index, QColor color)'''
    def customColor(self, index):
        '''static QColor QColorDialog.customColor(int index)'''
        return QColor()
    def customCount(self):
        '''static int QColorDialog.customCount()'''
        return int()
    def getColor(self, initial = None, parent = None, title = str(), options = 0):
        '''static QColor QColorDialog.getColor(QColor initial = Qt.white, QWidget parent = None, str title = str(), QColorDialog.ColorDialogOptions options = 0)'''
        return QColor()
    class ColorDialogOptions():
        """"""
        def __init__(self):
            '''QColorDialog.ColorDialogOptions QColorDialog.ColorDialogOptions.__init__()'''
            return QColorDialog.ColorDialogOptions()
        def __init__(self):
            '''int QColorDialog.ColorDialogOptions.__init__()'''
            return int()
        def __init__(self):
            '''void QColorDialog.ColorDialogOptions.__init__()'''
        def __bool__(self):
            '''int QColorDialog.ColorDialogOptions.__bool__()'''
            return int()
        def __ne__(self, f):
            '''bool QColorDialog.ColorDialogOptions.__ne__(QColorDialog.ColorDialogOptions f)'''
            return bool()
        def __eq__(self, f):
            '''bool QColorDialog.ColorDialogOptions.__eq__(QColorDialog.ColorDialogOptions f)'''
            return bool()
        def __invert__(self):
            '''QColorDialog.ColorDialogOptions QColorDialog.ColorDialogOptions.__invert__()'''
            return QColorDialog.ColorDialogOptions()
        def __and__(self, mask):
            '''QColorDialog.ColorDialogOptions QColorDialog.ColorDialogOptions.__and__(int mask)'''
            return QColorDialog.ColorDialogOptions()
        def __xor__(self, f):
            '''QColorDialog.ColorDialogOptions QColorDialog.ColorDialogOptions.__xor__(QColorDialog.ColorDialogOptions f)'''
            return QColorDialog.ColorDialogOptions()
        def __xor__(self, f):
            '''QColorDialog.ColorDialogOptions QColorDialog.ColorDialogOptions.__xor__(int f)'''
            return QColorDialog.ColorDialogOptions()
        def __or__(self, f):
            '''QColorDialog.ColorDialogOptions QColorDialog.ColorDialogOptions.__or__(QColorDialog.ColorDialogOptions f)'''
            return QColorDialog.ColorDialogOptions()
        def __or__(self, f):
            '''QColorDialog.ColorDialogOptions QColorDialog.ColorDialogOptions.__or__(int f)'''
            return QColorDialog.ColorDialogOptions()
        def __int__(self):
            '''int QColorDialog.ColorDialogOptions.__int__()'''
            return int()
        def __ixor__(self, f):
            '''QColorDialog.ColorDialogOptions QColorDialog.ColorDialogOptions.__ixor__(QColorDialog.ColorDialogOptions f)'''
            return QColorDialog.ColorDialogOptions()
        def __ior__(self, f):
            '''QColorDialog.ColorDialogOptions QColorDialog.ColorDialogOptions.__ior__(QColorDialog.ColorDialogOptions f)'''
            return QColorDialog.ColorDialogOptions()
        def __iand__(self, mask):
            '''QColorDialog.ColorDialogOptions QColorDialog.ColorDialogOptions.__iand__(int mask)'''
            return QColorDialog.ColorDialogOptions()


class QColumnView(QAbstractItemView):
    """"""
    def __init__(self, parent = None):
        '''void QColumnView.__init__(QWidget parent = None)'''
    def currentChanged(self, current, previous):
        '''void QColumnView.currentChanged(QModelIndex current, QModelIndex previous)'''
    def rowsInserted(self, parent, start, end):
        '''void QColumnView.rowsInserted(QModelIndex parent, int start, int end)'''
    def scrollContentsBy(self, dx, dy):
        '''void QColumnView.scrollContentsBy(int dx, int dy)'''
    def verticalOffset(self):
        '''int QColumnView.verticalOffset()'''
        return int()
    def horizontalOffset(self):
        '''int QColumnView.horizontalOffset()'''
        return int()
    def visualRegionForSelection(self, selection):
        '''QRegion QColumnView.visualRegionForSelection(QItemSelection selection)'''
        return QRegion()
    def setSelection(self, rect, command):
        '''void QColumnView.setSelection(QRect rect, QItemSelectionModel.SelectionFlags command)'''
    def resizeEvent(self, event):
        '''void QColumnView.resizeEvent(QResizeEvent event)'''
    def moveCursor(self, cursorAction, modifiers):
        '''QModelIndex QColumnView.moveCursor(QAbstractItemView.CursorAction cursorAction, Qt.KeyboardModifiers modifiers)'''
        return QModelIndex()
    def isIndexHidden(self, index):
        '''bool QColumnView.isIndexHidden(QModelIndex index)'''
        return bool()
    def initializeColumn(self, column):
        '''void QColumnView.initializeColumn(QAbstractItemView column)'''
    def createColumn(self, rootIndex):
        '''QAbstractItemView QColumnView.createColumn(QModelIndex rootIndex)'''
        return QAbstractItemView()
    updatePreviewWidget = pyqtSignal() # void updatePreviewWidget(const QModelIndexamp;) - signal
    def selectAll(self):
        '''void QColumnView.selectAll()'''
    def setRootIndex(self, index):
        '''void QColumnView.setRootIndex(QModelIndex index)'''
    def setSelectionModel(self, selectionModel):
        '''void QColumnView.setSelectionModel(QItemSelectionModel selectionModel)'''
    def setModel(self, model):
        '''void QColumnView.setModel(QAbstractItemModel model)'''
    def visualRect(self, index):
        '''QRect QColumnView.visualRect(QModelIndex index)'''
        return QRect()
    def sizeHint(self):
        '''QSize QColumnView.sizeHint()'''
        return QSize()
    def scrollTo(self, index, hint = None):
        '''void QColumnView.scrollTo(QModelIndex index, QAbstractItemView.ScrollHint hint = QAbstractItemView.EnsureVisible)'''
    def indexAt(self, point):
        '''QModelIndex QColumnView.indexAt(QPoint point)'''
        return QModelIndex()
    def setResizeGripsVisible(self, visible):
        '''void QColumnView.setResizeGripsVisible(bool visible)'''
    def setPreviewWidget(self, widget):
        '''void QColumnView.setPreviewWidget(QWidget widget)'''
    def setColumnWidths(self, list):
        '''void QColumnView.setColumnWidths(list-of-int list)'''
    def resizeGripsVisible(self):
        '''bool QColumnView.resizeGripsVisible()'''
        return bool()
    def previewWidget(self):
        '''QWidget QColumnView.previewWidget()'''
        return QWidget()
    def columnWidths(self):
        '''list-of-int QColumnView.columnWidths()'''
        return [int()]


class QComboBox(QWidget):
    """"""
    # Enum QComboBox.SizeAdjustPolicy
    AdjustToContents = 0
    AdjustToContentsOnFirstShow = 0
    AdjustToMinimumContentsLength = 0
    AdjustToMinimumContentsLengthWithIcon = 0

    # Enum QComboBox.InsertPolicy
    NoInsert = 0
    InsertAtTop = 0
    InsertAtCurrent = 0
    InsertAtBottom = 0
    InsertAfterCurrent = 0
    InsertBeforeCurrent = 0
    InsertAlphabetically = 0

    def __init__(self, parent = None):
        '''void QComboBox.__init__(QWidget parent = None)'''
    def currentData(self, role = None):
        '''QVariant QComboBox.currentData(int role = Qt.UserRole)'''
        return QVariant()
    def inputMethodQuery(self):
        '''Qt.InputMethodQuery QComboBox.inputMethodQuery()'''
        return Qt.InputMethodQuery()
    def inputMethodEvent(self):
        '''QInputMethodEvent QComboBox.inputMethodEvent()'''
        return QInputMethodEvent()
    def contextMenuEvent(self, e):
        '''void QComboBox.contextMenuEvent(QContextMenuEvent e)'''
    def wheelEvent(self, e):
        '''void QComboBox.wheelEvent(QWheelEvent e)'''
    def keyReleaseEvent(self, e):
        '''void QComboBox.keyReleaseEvent(QKeyEvent e)'''
    def keyPressEvent(self, e):
        '''void QComboBox.keyPressEvent(QKeyEvent e)'''
    def mouseReleaseEvent(self, e):
        '''void QComboBox.mouseReleaseEvent(QMouseEvent e)'''
    def mousePressEvent(self, e):
        '''void QComboBox.mousePressEvent(QMouseEvent e)'''
    def hideEvent(self, e):
        '''void QComboBox.hideEvent(QHideEvent e)'''
    def showEvent(self, e):
        '''void QComboBox.showEvent(QShowEvent e)'''
    def paintEvent(self, e):
        '''void QComboBox.paintEvent(QPaintEvent e)'''
    def resizeEvent(self, e):
        '''void QComboBox.resizeEvent(QResizeEvent e)'''
    def changeEvent(self, e):
        '''void QComboBox.changeEvent(QEvent e)'''
    def focusOutEvent(self, e):
        '''void QComboBox.focusOutEvent(QFocusEvent e)'''
    def focusInEvent(self, e):
        '''void QComboBox.focusInEvent(QFocusEvent e)'''
    def initStyleOption(self, option):
        '''void QComboBox.initStyleOption(QStyleOptionComboBox option)'''
    highlighted = pyqtSignal() # void highlighted(int) - signal
    highlighted = pyqtSignal() # void highlighted(const QStringamp;) - signal
    currentTextChanged = pyqtSignal() # void currentTextChanged(const QStringamp;) - signal
    currentIndexChanged = pyqtSignal() # void currentIndexChanged(int) - signal
    currentIndexChanged = pyqtSignal() # void currentIndexChanged(const QStringamp;) - signal
    activated = pyqtSignal() # void activated(int) - signal
    activated = pyqtSignal() # void activated(const QStringamp;) - signal
    editTextChanged = pyqtSignal() # void editTextChanged(const QStringamp;) - signal
    def setCurrentText(self, text):
        '''void QComboBox.setCurrentText(str text)'''
    def setEditText(self, text):
        '''void QComboBox.setEditText(str text)'''
    def clearEditText(self):
        '''void QComboBox.clearEditText()'''
    def clear(self):
        '''void QComboBox.clear()'''
    def insertSeparator(self, index):
        '''void QComboBox.insertSeparator(int index)'''
    def completer(self):
        '''QCompleter QComboBox.completer()'''
        return QCompleter()
    def setCompleter(self, c):
        '''void QComboBox.setCompleter(QCompleter c)'''
    def event(self, event):
        '''bool QComboBox.event(QEvent event)'''
        return bool()
    def hidePopup(self):
        '''void QComboBox.hidePopup()'''
    def showPopup(self):
        '''void QComboBox.showPopup()'''
    def minimumSizeHint(self):
        '''QSize QComboBox.minimumSizeHint()'''
        return QSize()
    def sizeHint(self):
        '''QSize QComboBox.sizeHint()'''
        return QSize()
    def setView(self, itemView):
        '''void QComboBox.setView(QAbstractItemView itemView)'''
    def view(self):
        '''QAbstractItemView QComboBox.view()'''
        return QAbstractItemView()
    def setItemData(self, index, value, role = None):
        '''void QComboBox.setItemData(int index, QVariant value, int role = Qt.UserRole)'''
    def setItemIcon(self, index, icon):
        '''void QComboBox.setItemIcon(int index, QIcon icon)'''
    def setItemText(self, index, text):
        '''void QComboBox.setItemText(int index, str text)'''
    def removeItem(self, index):
        '''void QComboBox.removeItem(int index)'''
    def insertItems(self, index, texts):
        '''void QComboBox.insertItems(int index, list-of-str texts)'''
    def insertItem(self, index, text, userData = None):
        '''void QComboBox.insertItem(int index, str text, QVariant userData = None)'''
    def insertItem(self, index, icon, text, userData = None):
        '''void QComboBox.insertItem(int index, QIcon icon, str text, QVariant userData = None)'''
    def addItem(self, text, userData = None):
        '''void QComboBox.addItem(str text, QVariant userData = None)'''
    def addItem(self, icon, text, userData = None):
        '''void QComboBox.addItem(QIcon icon, str text, QVariant userData = None)'''
    def addItems(self, texts):
        '''void QComboBox.addItems(list-of-str texts)'''
    def itemData(self, index, role = None):
        '''QVariant QComboBox.itemData(int index, int role = Qt.UserRole)'''
        return QVariant()
    def itemIcon(self, index):
        '''QIcon QComboBox.itemIcon(int index)'''
        return QIcon()
    def itemText(self, index):
        '''str QComboBox.itemText(int index)'''
        return str()
    def currentText(self):
        '''str QComboBox.currentText()'''
        return str()
    def setCurrentIndex(self, index):
        '''void QComboBox.setCurrentIndex(int index)'''
    def currentIndex(self):
        '''int QComboBox.currentIndex()'''
        return int()
    def setModelColumn(self, visibleColumn):
        '''void QComboBox.setModelColumn(int visibleColumn)'''
    def modelColumn(self):
        '''int QComboBox.modelColumn()'''
        return int()
    def setRootModelIndex(self, index):
        '''void QComboBox.setRootModelIndex(QModelIndex index)'''
    def rootModelIndex(self):
        '''QModelIndex QComboBox.rootModelIndex()'''
        return QModelIndex()
    def setModel(self, model):
        '''void QComboBox.setModel(QAbstractItemModel model)'''
    def model(self):
        '''QAbstractItemModel QComboBox.model()'''
        return QAbstractItemModel()
    def setItemDelegate(self, delegate):
        '''void QComboBox.setItemDelegate(QAbstractItemDelegate delegate)'''
    def itemDelegate(self):
        '''QAbstractItemDelegate QComboBox.itemDelegate()'''
        return QAbstractItemDelegate()
    def validator(self):
        '''QValidator QComboBox.validator()'''
        return QValidator()
    def setValidator(self, v):
        '''void QComboBox.setValidator(QValidator v)'''
    def lineEdit(self):
        '''QLineEdit QComboBox.lineEdit()'''
        return QLineEdit()
    def setLineEdit(self, edit):
        '''void QComboBox.setLineEdit(QLineEdit edit)'''
    def setEditable(self, editable):
        '''void QComboBox.setEditable(bool editable)'''
    def isEditable(self):
        '''bool QComboBox.isEditable()'''
        return bool()
    def setIconSize(self, size):
        '''void QComboBox.setIconSize(QSize size)'''
    def iconSize(self):
        '''QSize QComboBox.iconSize()'''
        return QSize()
    def setMinimumContentsLength(self, characters):
        '''void QComboBox.setMinimumContentsLength(int characters)'''
    def minimumContentsLength(self):
        '''int QComboBox.minimumContentsLength()'''
        return int()
    def setSizeAdjustPolicy(self, policy):
        '''void QComboBox.setSizeAdjustPolicy(QComboBox.SizeAdjustPolicy policy)'''
    def sizeAdjustPolicy(self):
        '''QComboBox.SizeAdjustPolicy QComboBox.sizeAdjustPolicy()'''
        return QComboBox.SizeAdjustPolicy()
    def setInsertPolicy(self, policy):
        '''void QComboBox.setInsertPolicy(QComboBox.InsertPolicy policy)'''
    def insertPolicy(self):
        '''QComboBox.InsertPolicy QComboBox.insertPolicy()'''
        return QComboBox.InsertPolicy()
    def findData(self, data, role = None, flags = None):
        '''int QComboBox.findData(QVariant data, int role = Qt.UserRole, Qt.MatchFlags flags = Qt.MatchExactly|Qt.MatchCaseSensitive)'''
        return int()
    def findText(self, text, flags = None):
        '''int QComboBox.findText(str text, Qt.MatchFlags flags = Qt.MatchExactly|Qt.MatchCaseSensitive)'''
        return int()
    def hasFrame(self):
        '''bool QComboBox.hasFrame()'''
        return bool()
    def setFrame(self):
        '''bool QComboBox.setFrame()'''
        return bool()
    def setDuplicatesEnabled(self, enable):
        '''void QComboBox.setDuplicatesEnabled(bool enable)'''
    def duplicatesEnabled(self):
        '''bool QComboBox.duplicatesEnabled()'''
        return bool()
    def maxCount(self):
        '''int QComboBox.maxCount()'''
        return int()
    def setMaxCount(self, max):
        '''void QComboBox.setMaxCount(int max)'''
    def __len__(self):
        ''' QComboBox.__len__()'''
        return ()
    def count(self):
        '''int QComboBox.count()'''
        return int()
    def setMaxVisibleItems(self, maxItems):
        '''void QComboBox.setMaxVisibleItems(int maxItems)'''
    def maxVisibleItems(self):
        '''int QComboBox.maxVisibleItems()'''
        return int()


class QPushButton(QAbstractButton):
    """"""
    def __init__(self, parent = None):
        '''void QPushButton.__init__(QWidget parent = None)'''
    def __init__(self, text, parent = None):
        '''void QPushButton.__init__(str text, QWidget parent = None)'''
    def __init__(self, icon, text, parent = None):
        '''void QPushButton.__init__(QIcon icon, str text, QWidget parent = None)'''
    def focusOutEvent(self):
        '''QFocusEvent QPushButton.focusOutEvent()'''
        return QFocusEvent()
    def focusInEvent(self):
        '''QFocusEvent QPushButton.focusInEvent()'''
        return QFocusEvent()
    def keyPressEvent(self):
        '''QKeyEvent QPushButton.keyPressEvent()'''
        return QKeyEvent()
    def paintEvent(self):
        '''QPaintEvent QPushButton.paintEvent()'''
        return QPaintEvent()
    def event(self, e):
        '''bool QPushButton.event(QEvent e)'''
        return bool()
    def initStyleOption(self, option):
        '''void QPushButton.initStyleOption(QStyleOptionButton option)'''
    def showMenu(self):
        '''void QPushButton.showMenu()'''
    def isFlat(self):
        '''bool QPushButton.isFlat()'''
        return bool()
    def setFlat(self):
        '''bool QPushButton.setFlat()'''
        return bool()
    def menu(self):
        '''QMenu QPushButton.menu()'''
        return QMenu()
    def setMenu(self, menu):
        '''void QPushButton.setMenu(QMenu menu)'''
    def setDefault(self):
        '''bool QPushButton.setDefault()'''
        return bool()
    def isDefault(self):
        '''bool QPushButton.isDefault()'''
        return bool()
    def setAutoDefault(self):
        '''bool QPushButton.setAutoDefault()'''
        return bool()
    def autoDefault(self):
        '''bool QPushButton.autoDefault()'''
        return bool()
    def minimumSizeHint(self):
        '''QSize QPushButton.minimumSizeHint()'''
        return QSize()
    def sizeHint(self):
        '''QSize QPushButton.sizeHint()'''
        return QSize()


class QCommandLinkButton(QPushButton):
    """"""
    def __init__(self, parent = None):
        '''void QCommandLinkButton.__init__(QWidget parent = None)'''
    def __init__(self, text, parent = None):
        '''void QCommandLinkButton.__init__(str text, QWidget parent = None)'''
    def __init__(self, text, description, parent = None):
        '''void QCommandLinkButton.__init__(str text, str description, QWidget parent = None)'''
    def paintEvent(self):
        '''QPaintEvent QCommandLinkButton.paintEvent()'''
        return QPaintEvent()
    def event(self, e):
        '''bool QCommandLinkButton.event(QEvent e)'''
        return bool()
    def minimumSizeHint(self):
        '''QSize QCommandLinkButton.minimumSizeHint()'''
        return QSize()
    def heightForWidth(self):
        '''int QCommandLinkButton.heightForWidth()'''
        return int()
    def sizeHint(self):
        '''QSize QCommandLinkButton.sizeHint()'''
        return QSize()
    def setDescription(self, description):
        '''void QCommandLinkButton.setDescription(str description)'''
    def description(self):
        '''str QCommandLinkButton.description()'''
        return str()


class QStyle(QObject):
    """"""
    # Enum QStyle.RequestSoftwareInputPanel
    RSIP_OnMouseClickAndAlreadyFocused = 0
    RSIP_OnMouseClick = 0

    # Enum QStyle.StandardPixmap
    SP_TitleBarMenuButton = 0
    SP_TitleBarMinButton = 0
    SP_TitleBarMaxButton = 0
    SP_TitleBarCloseButton = 0
    SP_TitleBarNormalButton = 0
    SP_TitleBarShadeButton = 0
    SP_TitleBarUnshadeButton = 0
    SP_TitleBarContextHelpButton = 0
    SP_DockWidgetCloseButton = 0
    SP_MessageBoxInformation = 0
    SP_MessageBoxWarning = 0
    SP_MessageBoxCritical = 0
    SP_MessageBoxQuestion = 0
    SP_DesktopIcon = 0
    SP_TrashIcon = 0
    SP_ComputerIcon = 0
    SP_DriveFDIcon = 0
    SP_DriveHDIcon = 0
    SP_DriveCDIcon = 0
    SP_DriveDVDIcon = 0
    SP_DriveNetIcon = 0
    SP_DirOpenIcon = 0
    SP_DirClosedIcon = 0
    SP_DirLinkIcon = 0
    SP_FileIcon = 0
    SP_FileLinkIcon = 0
    SP_ToolBarHorizontalExtensionButton = 0
    SP_ToolBarVerticalExtensionButton = 0
    SP_FileDialogStart = 0
    SP_FileDialogEnd = 0
    SP_FileDialogToParent = 0
    SP_FileDialogNewFolder = 0
    SP_FileDialogDetailedView = 0
    SP_FileDialogInfoView = 0
    SP_FileDialogContentsView = 0
    SP_FileDialogListView = 0
    SP_FileDialogBack = 0
    SP_DirIcon = 0
    SP_DialogOkButton = 0
    SP_DialogCancelButton = 0
    SP_DialogHelpButton = 0
    SP_DialogOpenButton = 0
    SP_DialogSaveButton = 0
    SP_DialogCloseButton = 0
    SP_DialogApplyButton = 0
    SP_DialogResetButton = 0
    SP_DialogDiscardButton = 0
    SP_DialogYesButton = 0
    SP_DialogNoButton = 0
    SP_ArrowUp = 0
    SP_ArrowDown = 0
    SP_ArrowLeft = 0
    SP_ArrowRight = 0
    SP_ArrowBack = 0
    SP_ArrowForward = 0
    SP_DirHomeIcon = 0
    SP_CommandLink = 0
    SP_VistaShield = 0
    SP_BrowserReload = 0
    SP_BrowserStop = 0
    SP_MediaPlay = 0
    SP_MediaStop = 0
    SP_MediaPause = 0
    SP_MediaSkipForward = 0
    SP_MediaSkipBackward = 0
    SP_MediaSeekForward = 0
    SP_MediaSeekBackward = 0
    SP_MediaVolume = 0
    SP_MediaVolumeMuted = 0
    SP_DirLinkOpenIcon = 0
    SP_LineEditClearButton = 0
    SP_CustomBase = 0

    # Enum QStyle.StyleHint
    SH_EtchDisabledText = 0
    SH_DitherDisabledText = 0
    SH_ScrollBar_MiddleClickAbsolutePosition = 0
    SH_ScrollBar_ScrollWhenPointerLeavesControl = 0
    SH_TabBar_SelectMouseType = 0
    SH_TabBar_Alignment = 0
    SH_Header_ArrowAlignment = 0
    SH_Slider_SnapToValue = 0
    SH_Slider_SloppyKeyEvents = 0
    SH_ProgressDialog_CenterCancelButton = 0
    SH_ProgressDialog_TextLabelAlignment = 0
    SH_PrintDialog_RightAlignButtons = 0
    SH_MainWindow_SpaceBelowMenuBar = 0
    SH_FontDialog_SelectAssociatedText = 0
    SH_Menu_AllowActiveAndDisabled = 0
    SH_Menu_SpaceActivatesItem = 0
    SH_Menu_SubMenuPopupDelay = 0
    SH_ScrollView_FrameOnlyAroundContents = 0
    SH_MenuBar_AltKeyNavigation = 0
    SH_ComboBox_ListMouseTracking = 0
    SH_Menu_MouseTracking = 0
    SH_MenuBar_MouseTracking = 0
    SH_ItemView_ChangeHighlightOnFocus = 0
    SH_Widget_ShareActivation = 0
    SH_Workspace_FillSpaceOnMaximize = 0
    SH_ComboBox_Popup = 0
    SH_TitleBar_NoBorder = 0
    SH_ScrollBar_StopMouseOverSlider = 0
    SH_BlinkCursorWhenTextSelected = 0
    SH_RichText_FullWidthSelection = 0
    SH_Menu_Scrollable = 0
    SH_GroupBox_TextLabelVerticalAlignment = 0
    SH_GroupBox_TextLabelColor = 0
    SH_Menu_SloppySubMenus = 0
    SH_Table_GridLineColor = 0
    SH_LineEdit_PasswordCharacter = 0
    SH_DialogButtons_DefaultButton = 0
    SH_ToolBox_SelectedPageTitleBold = 0
    SH_TabBar_PreferNoArrows = 0
    SH_ScrollBar_LeftClickAbsolutePosition = 0
    SH_UnderlineShortcut = 0
    SH_SpinBox_AnimateButton = 0
    SH_SpinBox_KeyPressAutoRepeatRate = 0
    SH_SpinBox_ClickAutoRepeatRate = 0
    SH_Menu_FillScreenWithScroll = 0
    SH_ToolTipLabel_Opacity = 0
    SH_DrawMenuBarSeparator = 0
    SH_TitleBar_ModifyNotification = 0
    SH_Button_FocusPolicy = 0
    SH_MessageBox_UseBorderForButtonSpacing = 0
    SH_TitleBar_AutoRaise = 0
    SH_ToolButton_PopupDelay = 0
    SH_FocusFrame_Mask = 0
    SH_RubberBand_Mask = 0
    SH_WindowFrame_Mask = 0
    SH_SpinControls_DisableOnBounds = 0
    SH_Dial_BackgroundRole = 0
    SH_ComboBox_LayoutDirection = 0
    SH_ItemView_EllipsisLocation = 0
    SH_ItemView_ShowDecorationSelected = 0
    SH_ItemView_ActivateItemOnSingleClick = 0
    SH_ScrollBar_ContextMenu = 0
    SH_ScrollBar_RollBetweenButtons = 0
    SH_Slider_StopMouseOverSlider = 0
    SH_Slider_AbsoluteSetButtons = 0
    SH_Slider_PageSetButtons = 0
    SH_Menu_KeyboardSearch = 0
    SH_TabBar_ElideMode = 0
    SH_DialogButtonLayout = 0
    SH_ComboBox_PopupFrameStyle = 0
    SH_MessageBox_TextInteractionFlags = 0
    SH_DialogButtonBox_ButtonsHaveIcons = 0
    SH_SpellCheckUnderlineStyle = 0
    SH_MessageBox_CenterButtons = 0
    SH_Menu_SelectionWrap = 0
    SH_ItemView_MovementWithoutUpdatingSelection = 0
    SH_ToolTip_Mask = 0
    SH_FocusFrame_AboveWidget = 0
    SH_TextControl_FocusIndicatorTextCharFormat = 0
    SH_WizardStyle = 0
    SH_ItemView_ArrowKeysNavigateIntoChildren = 0
    SH_Menu_Mask = 0
    SH_Menu_FlashTriggeredItem = 0
    SH_Menu_FadeOutOnHide = 0
    SH_SpinBox_ClickAutoRepeatThreshold = 0
    SH_ItemView_PaintAlternatingRowColorsForEmptyArea = 0
    SH_FormLayoutWrapPolicy = 0
    SH_TabWidget_DefaultTabPosition = 0
    SH_ToolBar_Movable = 0
    SH_FormLayoutFieldGrowthPolicy = 0
    SH_FormLayoutFormAlignment = 0
    SH_FormLayoutLabelAlignment = 0
    SH_ItemView_DrawDelegateFrame = 0
    SH_TabBar_CloseButtonPosition = 0
    SH_DockWidget_ButtonsHaveFrame = 0
    SH_ToolButtonStyle = 0
    SH_RequestSoftwareInputPanel = 0
    SH_ListViewExpand_SelectMouseType = 0
    SH_ScrollBar_Transient = 0
    SH_Menu_SupportsSections = 0
    SH_ToolTip_WakeUpDelay = 0
    SH_ToolTip_FallAsleepDelay = 0
    SH_Widget_Animate = 0
    SH_Splitter_OpaqueResize = 0
    SH_LineEdit_PasswordMaskDelay = 0
    SH_TabBar_ChangeCurrentDelay = 0
    SH_Menu_SubMenuUniDirection = 0
    SH_Menu_SubMenuUniDirectionFailCount = 0
    SH_Menu_SubMenuSloppySelectOtherActions = 0
    SH_Menu_SubMenuSloppyCloseTimeout = 0
    SH_Menu_SubMenuResetWhenReenteringParent = 0
    SH_Menu_SubMenuDontStartSloppyOnLeave = 0
    SH_CustomBase = 0

    # Enum QStyle.ContentsType
    CT_PushButton = 0
    CT_CheckBox = 0
    CT_RadioButton = 0
    CT_ToolButton = 0
    CT_ComboBox = 0
    CT_Splitter = 0
    CT_ProgressBar = 0
    CT_MenuItem = 0
    CT_MenuBarItem = 0
    CT_MenuBar = 0
    CT_Menu = 0
    CT_TabBarTab = 0
    CT_Slider = 0
    CT_ScrollBar = 0
    CT_LineEdit = 0
    CT_SpinBox = 0
    CT_SizeGrip = 0
    CT_TabWidget = 0
    CT_DialogButtons = 0
    CT_HeaderSection = 0
    CT_GroupBox = 0
    CT_MdiControls = 0
    CT_ItemViewItem = 0
    CT_CustomBase = 0

    # Enum QStyle.PixelMetric
    PM_ButtonMargin = 0
    PM_ButtonDefaultIndicator = 0
    PM_MenuButtonIndicator = 0
    PM_ButtonShiftHorizontal = 0
    PM_ButtonShiftVertical = 0
    PM_DefaultFrameWidth = 0
    PM_SpinBoxFrameWidth = 0
    PM_ComboBoxFrameWidth = 0
    PM_MaximumDragDistance = 0
    PM_ScrollBarExtent = 0
    PM_ScrollBarSliderMin = 0
    PM_SliderThickness = 0
    PM_SliderControlThickness = 0
    PM_SliderLength = 0
    PM_SliderTickmarkOffset = 0
    PM_SliderSpaceAvailable = 0
    PM_DockWidgetSeparatorExtent = 0
    PM_DockWidgetHandleExtent = 0
    PM_DockWidgetFrameWidth = 0
    PM_TabBarTabOverlap = 0
    PM_TabBarTabHSpace = 0
    PM_TabBarTabVSpace = 0
    PM_TabBarBaseHeight = 0
    PM_TabBarBaseOverlap = 0
    PM_ProgressBarChunkWidth = 0
    PM_SplitterWidth = 0
    PM_TitleBarHeight = 0
    PM_MenuScrollerHeight = 0
    PM_MenuHMargin = 0
    PM_MenuVMargin = 0
    PM_MenuPanelWidth = 0
    PM_MenuTearoffHeight = 0
    PM_MenuDesktopFrameWidth = 0
    PM_MenuBarPanelWidth = 0
    PM_MenuBarItemSpacing = 0
    PM_MenuBarVMargin = 0
    PM_MenuBarHMargin = 0
    PM_IndicatorWidth = 0
    PM_IndicatorHeight = 0
    PM_ExclusiveIndicatorWidth = 0
    PM_ExclusiveIndicatorHeight = 0
    PM_DialogButtonsSeparator = 0
    PM_DialogButtonsButtonWidth = 0
    PM_DialogButtonsButtonHeight = 0
    PM_MdiSubWindowFrameWidth = 0
    PM_MDIFrameWidth = 0
    PM_MdiSubWindowMinimizedWidth = 0
    PM_MDIMinimizedWidth = 0
    PM_HeaderMargin = 0
    PM_HeaderMarkSize = 0
    PM_HeaderGripMargin = 0
    PM_TabBarTabShiftHorizontal = 0
    PM_TabBarTabShiftVertical = 0
    PM_TabBarScrollButtonWidth = 0
    PM_ToolBarFrameWidth = 0
    PM_ToolBarHandleExtent = 0
    PM_ToolBarItemSpacing = 0
    PM_ToolBarItemMargin = 0
    PM_ToolBarSeparatorExtent = 0
    PM_ToolBarExtensionExtent = 0
    PM_SpinBoxSliderHeight = 0
    PM_DefaultTopLevelMargin = 0
    PM_DefaultChildMargin = 0
    PM_DefaultLayoutSpacing = 0
    PM_ToolBarIconSize = 0
    PM_ListViewIconSize = 0
    PM_IconViewIconSize = 0
    PM_SmallIconSize = 0
    PM_LargeIconSize = 0
    PM_FocusFrameVMargin = 0
    PM_FocusFrameHMargin = 0
    PM_ToolTipLabelFrameWidth = 0
    PM_CheckBoxLabelSpacing = 0
    PM_TabBarIconSize = 0
    PM_SizeGripSize = 0
    PM_DockWidgetTitleMargin = 0
    PM_MessageBoxIconSize = 0
    PM_ButtonIconSize = 0
    PM_DockWidgetTitleBarButtonMargin = 0
    PM_RadioButtonLabelSpacing = 0
    PM_LayoutLeftMargin = 0
    PM_LayoutTopMargin = 0
    PM_LayoutRightMargin = 0
    PM_LayoutBottomMargin = 0
    PM_LayoutHorizontalSpacing = 0
    PM_LayoutVerticalSpacing = 0
    PM_TabBar_ScrollButtonOverlap = 0
    PM_TextCursorWidth = 0
    PM_TabCloseIndicatorWidth = 0
    PM_TabCloseIndicatorHeight = 0
    PM_ScrollView_ScrollBarSpacing = 0
    PM_SubMenuOverlap = 0
    PM_ScrollView_ScrollBarOverlap = 0
    PM_TreeViewIndentation = 0
    PM_HeaderDefaultSectionSizeHorizontal = 0
    PM_HeaderDefaultSectionSizeVertical = 0
    PM_CustomBase = 0

    # Enum QStyle.SubControl
    SC_None = 0
    SC_ScrollBarAddLine = 0
    SC_ScrollBarSubLine = 0
    SC_ScrollBarAddPage = 0
    SC_ScrollBarSubPage = 0
    SC_ScrollBarFirst = 0
    SC_ScrollBarLast = 0
    SC_ScrollBarSlider = 0
    SC_ScrollBarGroove = 0
    SC_SpinBoxUp = 0
    SC_SpinBoxDown = 0
    SC_SpinBoxFrame = 0
    SC_SpinBoxEditField = 0
    SC_ComboBoxFrame = 0
    SC_ComboBoxEditField = 0
    SC_ComboBoxArrow = 0
    SC_ComboBoxListBoxPopup = 0
    SC_SliderGroove = 0
    SC_SliderHandle = 0
    SC_SliderTickmarks = 0
    SC_ToolButton = 0
    SC_ToolButtonMenu = 0
    SC_TitleBarSysMenu = 0
    SC_TitleBarMinButton = 0
    SC_TitleBarMaxButton = 0
    SC_TitleBarCloseButton = 0
    SC_TitleBarNormalButton = 0
    SC_TitleBarShadeButton = 0
    SC_TitleBarUnshadeButton = 0
    SC_TitleBarContextHelpButton = 0
    SC_TitleBarLabel = 0
    SC_DialGroove = 0
    SC_DialHandle = 0
    SC_DialTickmarks = 0
    SC_GroupBoxCheckBox = 0
    SC_GroupBoxLabel = 0
    SC_GroupBoxContents = 0
    SC_GroupBoxFrame = 0
    SC_MdiMinButton = 0
    SC_MdiNormalButton = 0
    SC_MdiCloseButton = 0
    SC_CustomBase = 0
    SC_All = 0

    # Enum QStyle.ComplexControl
    CC_SpinBox = 0
    CC_ComboBox = 0
    CC_ScrollBar = 0
    CC_Slider = 0
    CC_ToolButton = 0
    CC_TitleBar = 0
    CC_Dial = 0
    CC_GroupBox = 0
    CC_MdiControls = 0
    CC_CustomBase = 0

    # Enum QStyle.SubElement
    SE_PushButtonContents = 0
    SE_PushButtonFocusRect = 0
    SE_CheckBoxIndicator = 0
    SE_CheckBoxContents = 0
    SE_CheckBoxFocusRect = 0
    SE_CheckBoxClickRect = 0
    SE_RadioButtonIndicator = 0
    SE_RadioButtonContents = 0
    SE_RadioButtonFocusRect = 0
    SE_RadioButtonClickRect = 0
    SE_ComboBoxFocusRect = 0
    SE_SliderFocusRect = 0
    SE_ProgressBarGroove = 0
    SE_ProgressBarContents = 0
    SE_ProgressBarLabel = 0
    SE_ToolBoxTabContents = 0
    SE_HeaderLabel = 0
    SE_HeaderArrow = 0
    SE_TabWidgetTabBar = 0
    SE_TabWidgetTabPane = 0
    SE_TabWidgetTabContents = 0
    SE_TabWidgetLeftCorner = 0
    SE_TabWidgetRightCorner = 0
    SE_ViewItemCheckIndicator = 0
    SE_TabBarTearIndicator = 0
    SE_TreeViewDisclosureItem = 0
    SE_LineEditContents = 0
    SE_FrameContents = 0
    SE_DockWidgetCloseButton = 0
    SE_DockWidgetFloatButton = 0
    SE_DockWidgetTitleBarText = 0
    SE_DockWidgetIcon = 0
    SE_CheckBoxLayoutItem = 0
    SE_ComboBoxLayoutItem = 0
    SE_DateTimeEditLayoutItem = 0
    SE_DialogButtonBoxLayoutItem = 0
    SE_LabelLayoutItem = 0
    SE_ProgressBarLayoutItem = 0
    SE_PushButtonLayoutItem = 0
    SE_RadioButtonLayoutItem = 0
    SE_SliderLayoutItem = 0
    SE_SpinBoxLayoutItem = 0
    SE_ToolButtonLayoutItem = 0
    SE_FrameLayoutItem = 0
    SE_GroupBoxLayoutItem = 0
    SE_TabWidgetLayoutItem = 0
    SE_ItemViewItemCheckIndicator = 0
    SE_ItemViewItemDecoration = 0
    SE_ItemViewItemText = 0
    SE_ItemViewItemFocusRect = 0
    SE_TabBarTabLeftButton = 0
    SE_TabBarTabRightButton = 0
    SE_TabBarTabText = 0
    SE_ShapedFrameContents = 0
    SE_ToolBarHandle = 0
    SE_CustomBase = 0

    # Enum QStyle.ControlElement
    CE_PushButton = 0
    CE_PushButtonBevel = 0
    CE_PushButtonLabel = 0
    CE_CheckBox = 0
    CE_CheckBoxLabel = 0
    CE_RadioButton = 0
    CE_RadioButtonLabel = 0
    CE_TabBarTab = 0
    CE_TabBarTabShape = 0
    CE_TabBarTabLabel = 0
    CE_ProgressBar = 0
    CE_ProgressBarGroove = 0
    CE_ProgressBarContents = 0
    CE_ProgressBarLabel = 0
    CE_MenuItem = 0
    CE_MenuScroller = 0
    CE_MenuVMargin = 0
    CE_MenuHMargin = 0
    CE_MenuTearoff = 0
    CE_MenuEmptyArea = 0
    CE_MenuBarItem = 0
    CE_MenuBarEmptyArea = 0
    CE_ToolButtonLabel = 0
    CE_Header = 0
    CE_HeaderSection = 0
    CE_HeaderLabel = 0
    CE_ToolBoxTab = 0
    CE_SizeGrip = 0
    CE_Splitter = 0
    CE_RubberBand = 0
    CE_DockWidgetTitle = 0
    CE_ScrollBarAddLine = 0
    CE_ScrollBarSubLine = 0
    CE_ScrollBarAddPage = 0
    CE_ScrollBarSubPage = 0
    CE_ScrollBarSlider = 0
    CE_ScrollBarFirst = 0
    CE_ScrollBarLast = 0
    CE_FocusFrame = 0
    CE_ComboBoxLabel = 0
    CE_ToolBar = 0
    CE_ToolBoxTabShape = 0
    CE_ToolBoxTabLabel = 0
    CE_HeaderEmptyArea = 0
    CE_ColumnViewGrip = 0
    CE_ItemViewItem = 0
    CE_ShapedFrame = 0
    CE_CustomBase = 0

    # Enum QStyle.PrimitiveElement
    PE_Frame = 0
    PE_FrameDefaultButton = 0
    PE_FrameDockWidget = 0
    PE_FrameFocusRect = 0
    PE_FrameGroupBox = 0
    PE_FrameLineEdit = 0
    PE_FrameMenu = 0
    PE_FrameStatusBar = 0
    PE_FrameTabWidget = 0
    PE_FrameWindow = 0
    PE_FrameButtonBevel = 0
    PE_FrameButtonTool = 0
    PE_FrameTabBarBase = 0
    PE_PanelButtonCommand = 0
    PE_PanelButtonBevel = 0
    PE_PanelButtonTool = 0
    PE_PanelMenuBar = 0
    PE_PanelToolBar = 0
    PE_PanelLineEdit = 0
    PE_IndicatorArrowDown = 0
    PE_IndicatorArrowLeft = 0
    PE_IndicatorArrowRight = 0
    PE_IndicatorArrowUp = 0
    PE_IndicatorBranch = 0
    PE_IndicatorButtonDropDown = 0
    PE_IndicatorViewItemCheck = 0
    PE_IndicatorCheckBox = 0
    PE_IndicatorDockWidgetResizeHandle = 0
    PE_IndicatorHeaderArrow = 0
    PE_IndicatorMenuCheckMark = 0
    PE_IndicatorProgressChunk = 0
    PE_IndicatorRadioButton = 0
    PE_IndicatorSpinDown = 0
    PE_IndicatorSpinMinus = 0
    PE_IndicatorSpinPlus = 0
    PE_IndicatorSpinUp = 0
    PE_IndicatorToolBarHandle = 0
    PE_IndicatorToolBarSeparator = 0
    PE_PanelTipLabel = 0
    PE_IndicatorTabTear = 0
    PE_PanelScrollAreaCorner = 0
    PE_Widget = 0
    PE_IndicatorColumnViewArrow = 0
    PE_FrameStatusBarItem = 0
    PE_IndicatorItemViewItemCheck = 0
    PE_IndicatorItemViewItemDrop = 0
    PE_PanelItemViewItem = 0
    PE_PanelItemViewRow = 0
    PE_PanelStatusBar = 0
    PE_IndicatorTabClose = 0
    PE_PanelMenu = 0
    PE_CustomBase = 0

    # Enum QStyle.StateFlag
    State_None = 0
    State_Enabled = 0
    State_Raised = 0
    State_Sunken = 0
    State_Off = 0
    State_NoChange = 0
    State_On = 0
    State_DownArrow = 0
    State_Horizontal = 0
    State_HasFocus = 0
    State_Top = 0
    State_Bottom = 0
    State_FocusAtBorder = 0
    State_AutoRaise = 0
    State_MouseOver = 0
    State_UpArrow = 0
    State_Selected = 0
    State_Active = 0
    State_Open = 0
    State_Children = 0
    State_Item = 0
    State_Sibling = 0
    State_Editing = 0
    State_KeyboardFocusChange = 0
    State_ReadOnly = 0
    State_Window = 0
    State_Small = 0
    State_Mini = 0

    def __init__(self):
        '''void QStyle.__init__()'''
    def proxy(self):
        '''QStyle QStyle.proxy()'''
        return QStyle()
    def combinedLayoutSpacing(self, controls1, controls2, orientation, option = None, widget = None):
        '''int QStyle.combinedLayoutSpacing(QSizePolicy.ControlTypes controls1, QSizePolicy.ControlTypes controls2, Qt.Orientation orientation, QStyleOption option = None, QWidget widget = None)'''
        return int()
    def layoutSpacing(self, control1, control2, orientation, option = None, widget = None):
        '''abstract int QStyle.layoutSpacing(QSizePolicy.ControlType control1, QSizePolicy.ControlType control2, Qt.Orientation orientation, QStyleOption option = None, QWidget widget = None)'''
        return int()
    def alignedRect(self, direction, alignment, size, rectangle):
        '''static QRect QStyle.alignedRect(Qt.LayoutDirection direction, Qt.Alignment alignment, QSize size, QRect rectangle)'''
        return QRect()
    def visualAlignment(self, direction, alignment):
        '''static Qt.Alignment QStyle.visualAlignment(Qt.LayoutDirection direction, Qt.Alignment alignment)'''
        return Qt.Alignment()
    def sliderValueFromPosition(self, min, max, position, span, upsideDown = False):
        '''static int QStyle.sliderValueFromPosition(int min, int max, int position, int span, bool upsideDown = False)'''
        return int()
    def sliderPositionFromValue(self, min, max, logicalValue, span, upsideDown = False):
        '''static int QStyle.sliderPositionFromValue(int min, int max, int logicalValue, int span, bool upsideDown = False)'''
        return int()
    def visualPos(self, direction, boundingRect, logicalPos):
        '''static QPoint QStyle.visualPos(Qt.LayoutDirection direction, QRect boundingRect, QPoint logicalPos)'''
        return QPoint()
    def visualRect(self, direction, boundingRect, logicalRect):
        '''static QRect QStyle.visualRect(Qt.LayoutDirection direction, QRect boundingRect, QRect logicalRect)'''
        return QRect()
    def generatedIconPixmap(self, iconMode, pixmap, opt):
        '''abstract QPixmap QStyle.generatedIconPixmap(QIcon.Mode iconMode, QPixmap pixmap, QStyleOption opt)'''
        return QPixmap()
    def standardIcon(self, standardIcon, option = None, widget = None):
        '''abstract QIcon QStyle.standardIcon(QStyle.StandardPixmap standardIcon, QStyleOption option = None, QWidget widget = None)'''
        return QIcon()
    def standardPixmap(self, standardPixmap, option = None, widget = None):
        '''abstract QPixmap QStyle.standardPixmap(QStyle.StandardPixmap standardPixmap, QStyleOption option = None, QWidget widget = None)'''
        return QPixmap()
    def styleHint(self, stylehint, option = None, widget = None, returnData = None):
        '''abstract int QStyle.styleHint(QStyle.StyleHint stylehint, QStyleOption option = None, QWidget widget = None, QStyleHintReturn returnData = None)'''
        return int()
    def sizeFromContents(self, ct, opt, contentsSize, widget = None):
        '''abstract QSize QStyle.sizeFromContents(QStyle.ContentsType ct, QStyleOption opt, QSize contentsSize, QWidget widget = None)'''
        return QSize()
    def pixelMetric(self, metric, option = None, widget = None):
        '''abstract int QStyle.pixelMetric(QStyle.PixelMetric metric, QStyleOption option = None, QWidget widget = None)'''
        return int()
    def subControlRect(self, cc, opt, sc, widget = None):
        '''abstract QRect QStyle.subControlRect(QStyle.ComplexControl cc, QStyleOptionComplex opt, QStyle.SubControl sc, QWidget widget = None)'''
        return QRect()
    def hitTestComplexControl(self, cc, opt, pt, widget = None):
        '''abstract QStyle.SubControl QStyle.hitTestComplexControl(QStyle.ComplexControl cc, QStyleOptionComplex opt, QPoint pt, QWidget widget = None)'''
        return QStyle.SubControl()
    def drawComplexControl(self, cc, opt, p, widget = None):
        '''abstract void QStyle.drawComplexControl(QStyle.ComplexControl cc, QStyleOptionComplex opt, QPainter p, QWidget widget = None)'''
    def subElementRect(self, subElement, option, widget = None):
        '''abstract QRect QStyle.subElementRect(QStyle.SubElement subElement, QStyleOption option, QWidget widget = None)'''
        return QRect()
    def drawControl(self, element, opt, p, widget = None):
        '''abstract void QStyle.drawControl(QStyle.ControlElement element, QStyleOption opt, QPainter p, QWidget widget = None)'''
    def drawPrimitive(self, pe, opt, p, widget = None):
        '''abstract void QStyle.drawPrimitive(QStyle.PrimitiveElement pe, QStyleOption opt, QPainter p, QWidget widget = None)'''
    def standardPalette(self):
        '''QPalette QStyle.standardPalette()'''
        return QPalette()
    def drawItemPixmap(self, painter, rect, alignment, pixmap):
        '''void QStyle.drawItemPixmap(QPainter painter, QRect rect, int alignment, QPixmap pixmap)'''
    def drawItemText(self, painter, rectangle, alignment, palette, enabled, text, textRole = None):
        '''void QStyle.drawItemText(QPainter painter, QRect rectangle, int alignment, QPalette palette, bool enabled, str text, QPalette.ColorRole textRole = QPalette.NoRole)'''
    def itemPixmapRect(self, r, flags, pixmap):
        '''QRect QStyle.itemPixmapRect(QRect r, int flags, QPixmap pixmap)'''
        return QRect()
    def itemTextRect(self, fm, r, flags, enabled, text):
        '''QRect QStyle.itemTextRect(QFontMetrics fm, QRect r, int flags, bool enabled, str text)'''
        return QRect()
    def unpolish(self):
        '''QWidget QStyle.unpolish()'''
        return QWidget()
    def unpolish(self):
        '''QApplication QStyle.unpolish()'''
        return QApplication()
    def polish(self):
        '''QWidget QStyle.polish()'''
        return QWidget()
    def polish(self):
        '''QApplication QStyle.polish()'''
        return QApplication()
    def polish(self):
        '''QPalette QStyle.polish()'''
        return QPalette()
    class SubControls():
        """"""
        def __init__(self):
            '''QStyle.SubControls QStyle.SubControls.__init__()'''
            return QStyle.SubControls()
        def __init__(self):
            '''int QStyle.SubControls.__init__()'''
            return int()
        def __init__(self):
            '''void QStyle.SubControls.__init__()'''
        def __bool__(self):
            '''int QStyle.SubControls.__bool__()'''
            return int()
        def __ne__(self, f):
            '''bool QStyle.SubControls.__ne__(QStyle.SubControls f)'''
            return bool()
        def __eq__(self, f):
            '''bool QStyle.SubControls.__eq__(QStyle.SubControls f)'''
            return bool()
        def __invert__(self):
            '''QStyle.SubControls QStyle.SubControls.__invert__()'''
            return QStyle.SubControls()
        def __and__(self, mask):
            '''QStyle.SubControls QStyle.SubControls.__and__(int mask)'''
            return QStyle.SubControls()
        def __xor__(self, f):
            '''QStyle.SubControls QStyle.SubControls.__xor__(QStyle.SubControls f)'''
            return QStyle.SubControls()
        def __xor__(self, f):
            '''QStyle.SubControls QStyle.SubControls.__xor__(int f)'''
            return QStyle.SubControls()
        def __or__(self, f):
            '''QStyle.SubControls QStyle.SubControls.__or__(QStyle.SubControls f)'''
            return QStyle.SubControls()
        def __or__(self, f):
            '''QStyle.SubControls QStyle.SubControls.__or__(int f)'''
            return QStyle.SubControls()
        def __int__(self):
            '''int QStyle.SubControls.__int__()'''
            return int()
        def __ixor__(self, f):
            '''QStyle.SubControls QStyle.SubControls.__ixor__(QStyle.SubControls f)'''
            return QStyle.SubControls()
        def __ior__(self, f):
            '''QStyle.SubControls QStyle.SubControls.__ior__(QStyle.SubControls f)'''
            return QStyle.SubControls()
        def __iand__(self, mask):
            '''QStyle.SubControls QStyle.SubControls.__iand__(int mask)'''
            return QStyle.SubControls()
    class State():
        """"""
        def __init__(self):
            '''QStyle.State QStyle.State.__init__()'''
            return QStyle.State()
        def __init__(self):
            '''int QStyle.State.__init__()'''
            return int()
        def __init__(self):
            '''void QStyle.State.__init__()'''
        def __bool__(self):
            '''int QStyle.State.__bool__()'''
            return int()
        def __ne__(self, f):
            '''bool QStyle.State.__ne__(QStyle.State f)'''
            return bool()
        def __eq__(self, f):
            '''bool QStyle.State.__eq__(QStyle.State f)'''
            return bool()
        def __invert__(self):
            '''QStyle.State QStyle.State.__invert__()'''
            return QStyle.State()
        def __and__(self, mask):
            '''QStyle.State QStyle.State.__and__(int mask)'''
            return QStyle.State()
        def __xor__(self, f):
            '''QStyle.State QStyle.State.__xor__(QStyle.State f)'''
            return QStyle.State()
        def __xor__(self, f):
            '''QStyle.State QStyle.State.__xor__(int f)'''
            return QStyle.State()
        def __or__(self, f):
            '''QStyle.State QStyle.State.__or__(QStyle.State f)'''
            return QStyle.State()
        def __or__(self, f):
            '''QStyle.State QStyle.State.__or__(int f)'''
            return QStyle.State()
        def __int__(self):
            '''int QStyle.State.__int__()'''
            return int()
        def __ixor__(self, f):
            '''QStyle.State QStyle.State.__ixor__(QStyle.State f)'''
            return QStyle.State()
        def __ior__(self, f):
            '''QStyle.State QStyle.State.__ior__(QStyle.State f)'''
            return QStyle.State()
        def __iand__(self, mask):
            '''QStyle.State QStyle.State.__iand__(int mask)'''
            return QStyle.State()


class QCommonStyle(QStyle):
    """"""
    def __init__(self):
        '''void QCommonStyle.__init__()'''
    def layoutSpacing(self, control1, control2, orientation, option = None, widget = None):
        '''int QCommonStyle.layoutSpacing(QSizePolicy.ControlType control1, QSizePolicy.ControlType control2, Qt.Orientation orientation, QStyleOption option = None, QWidget widget = None)'''
        return int()
    def standardIcon(self, standardIcon, option = None, widget = None):
        '''QIcon QCommonStyle.standardIcon(QStyle.StandardPixmap standardIcon, QStyleOption option = None, QWidget widget = None)'''
        return QIcon()
    def generatedIconPixmap(self, iconMode, pixmap, opt):
        '''QPixmap QCommonStyle.generatedIconPixmap(QIcon.Mode iconMode, QPixmap pixmap, QStyleOption opt)'''
        return QPixmap()
    def standardPixmap(self, sp, option = None, widget = None):
        '''QPixmap QCommonStyle.standardPixmap(QStyle.StandardPixmap sp, QStyleOption option = None, QWidget widget = None)'''
        return QPixmap()
    def styleHint(self, sh, option = None, widget = None, returnData = None):
        '''int QCommonStyle.styleHint(QStyle.StyleHint sh, QStyleOption option = None, QWidget widget = None, QStyleHintReturn returnData = None)'''
        return int()
    def pixelMetric(self, m, option = None, widget = None):
        '''int QCommonStyle.pixelMetric(QStyle.PixelMetric m, QStyleOption option = None, QWidget widget = None)'''
        return int()
    def sizeFromContents(self, ct, opt, contentsSize, widget = None):
        '''QSize QCommonStyle.sizeFromContents(QStyle.ContentsType ct, QStyleOption opt, QSize contentsSize, QWidget widget = None)'''
        return QSize()
    def subControlRect(self, cc, opt, sc, widget = None):
        '''QRect QCommonStyle.subControlRect(QStyle.ComplexControl cc, QStyleOptionComplex opt, QStyle.SubControl sc, QWidget widget = None)'''
        return QRect()
    def hitTestComplexControl(self, cc, opt, pt, widget = None):
        '''QStyle.SubControl QCommonStyle.hitTestComplexControl(QStyle.ComplexControl cc, QStyleOptionComplex opt, QPoint pt, QWidget widget = None)'''
        return QStyle.SubControl()
    def drawComplexControl(self, cc, opt, p, widget = None):
        '''void QCommonStyle.drawComplexControl(QStyle.ComplexControl cc, QStyleOptionComplex opt, QPainter p, QWidget widget = None)'''
    def subElementRect(self, r, opt, widget = None):
        '''QRect QCommonStyle.subElementRect(QStyle.SubElement r, QStyleOption opt, QWidget widget = None)'''
        return QRect()
    def drawControl(self, element, opt, p, widget = None):
        '''void QCommonStyle.drawControl(QStyle.ControlElement element, QStyleOption opt, QPainter p, QWidget widget = None)'''
    def drawPrimitive(self, pe, opt, p, widget = None):
        '''void QCommonStyle.drawPrimitive(QStyle.PrimitiveElement pe, QStyleOption opt, QPainter p, QWidget widget = None)'''
    def unpolish(self, widget):
        '''void QCommonStyle.unpolish(QWidget widget)'''
    def unpolish(self, application):
        '''void QCommonStyle.unpolish(QApplication application)'''
    def polish(self, widget):
        '''void QCommonStyle.polish(QWidget widget)'''
    def polish(self, app):
        '''void QCommonStyle.polish(QApplication app)'''
    def polish(self):
        '''QPalette QCommonStyle.polish()'''
        return QPalette()


class QCompleter(QObject):
    """"""
    # Enum QCompleter.ModelSorting
    UnsortedModel = 0
    CaseSensitivelySortedModel = 0
    CaseInsensitivelySortedModel = 0

    # Enum QCompleter.CompletionMode
    PopupCompletion = 0
    UnfilteredPopupCompletion = 0
    InlineCompletion = 0

    def __init__(self, parent = None):
        '''void QCompleter.__init__(QObject parent = None)'''
    def __init__(self, model, parent = None):
        '''void QCompleter.__init__(QAbstractItemModel model, QObject parent = None)'''
    def __init__(self, list, parent = None):
        '''void QCompleter.__init__(list-of-str list, QObject parent = None)'''
    def filterMode(self):
        '''Qt.MatchFlags QCompleter.filterMode()'''
        return Qt.MatchFlags()
    def setFilterMode(self, filterMode):
        '''void QCompleter.setFilterMode(Qt.MatchFlags filterMode)'''
    def setMaxVisibleItems(self, maxItems):
        '''void QCompleter.setMaxVisibleItems(int maxItems)'''
    def maxVisibleItems(self):
        '''int QCompleter.maxVisibleItems()'''
        return int()
    highlighted = pyqtSignal() # void highlighted(const QStringamp;) - signal
    highlighted = pyqtSignal() # void highlighted(const QModelIndexamp;) - signal
    activated = pyqtSignal() # void activated(const QStringamp;) - signal
    activated = pyqtSignal() # void activated(const QModelIndexamp;) - signal
    def event(self):
        '''QEvent QCompleter.event()'''
        return QEvent()
    def eventFilter(self, o, e):
        '''bool QCompleter.eventFilter(QObject o, QEvent e)'''
        return bool()
    def setWrapAround(self, wrap):
        '''void QCompleter.setWrapAround(bool wrap)'''
    def setCompletionPrefix(self, prefix):
        '''void QCompleter.setCompletionPrefix(str prefix)'''
    def complete(self, rect = QRect()):
        '''void QCompleter.complete(QRect rect = QRect())'''
    def wrapAround(self):
        '''bool QCompleter.wrapAround()'''
        return bool()
    def splitPath(self, path):
        '''list-of-str QCompleter.splitPath(str path)'''
        return [str()]
    def pathFromIndex(self, index):
        '''str QCompleter.pathFromIndex(QModelIndex index)'''
        return str()
    def completionPrefix(self):
        '''str QCompleter.completionPrefix()'''
        return str()
    def completionModel(self):
        '''QAbstractItemModel QCompleter.completionModel()'''
        return QAbstractItemModel()
    def currentCompletion(self):
        '''str QCompleter.currentCompletion()'''
        return str()
    def currentIndex(self):
        '''QModelIndex QCompleter.currentIndex()'''
        return QModelIndex()
    def currentRow(self):
        '''int QCompleter.currentRow()'''
        return int()
    def setCurrentRow(self, row):
        '''bool QCompleter.setCurrentRow(int row)'''
        return bool()
    def completionCount(self):
        '''int QCompleter.completionCount()'''
        return int()
    def completionRole(self):
        '''int QCompleter.completionRole()'''
        return int()
    def setCompletionRole(self, role):
        '''void QCompleter.setCompletionRole(int role)'''
    def completionColumn(self):
        '''int QCompleter.completionColumn()'''
        return int()
    def setCompletionColumn(self, column):
        '''void QCompleter.setCompletionColumn(int column)'''
    def modelSorting(self):
        '''QCompleter.ModelSorting QCompleter.modelSorting()'''
        return QCompleter.ModelSorting()
    def setModelSorting(self, sorting):
        '''void QCompleter.setModelSorting(QCompleter.ModelSorting sorting)'''
    def caseSensitivity(self):
        '''Qt.CaseSensitivity QCompleter.caseSensitivity()'''
        return Qt.CaseSensitivity()
    def setCaseSensitivity(self, caseSensitivity):
        '''void QCompleter.setCaseSensitivity(Qt.CaseSensitivity caseSensitivity)'''
    def setPopup(self, popup):
        '''void QCompleter.setPopup(QAbstractItemView popup)'''
    def popup(self):
        '''QAbstractItemView QCompleter.popup()'''
        return QAbstractItemView()
    def completionMode(self):
        '''QCompleter.CompletionMode QCompleter.completionMode()'''
        return QCompleter.CompletionMode()
    def setCompletionMode(self, mode):
        '''void QCompleter.setCompletionMode(QCompleter.CompletionMode mode)'''
    def model(self):
        '''QAbstractItemModel QCompleter.model()'''
        return QAbstractItemModel()
    def setModel(self, c):
        '''void QCompleter.setModel(QAbstractItemModel c)'''
    def widget(self):
        '''QWidget QCompleter.widget()'''
        return QWidget()
    def setWidget(self, widget):
        '''void QCompleter.setWidget(QWidget widget)'''


class QDataWidgetMapper(QObject):
    """"""
    # Enum QDataWidgetMapper.SubmitPolicy
    AutoSubmit = 0
    ManualSubmit = 0

    def __init__(self, parent = None):
        '''void QDataWidgetMapper.__init__(QObject parent = None)'''
    currentIndexChanged = pyqtSignal() # void currentIndexChanged(int) - signal
    def toPrevious(self):
        '''void QDataWidgetMapper.toPrevious()'''
    def toNext(self):
        '''void QDataWidgetMapper.toNext()'''
    def toLast(self):
        '''void QDataWidgetMapper.toLast()'''
    def toFirst(self):
        '''void QDataWidgetMapper.toFirst()'''
    def submit(self):
        '''bool QDataWidgetMapper.submit()'''
        return bool()
    def setCurrentModelIndex(self, index):
        '''void QDataWidgetMapper.setCurrentModelIndex(QModelIndex index)'''
    def setCurrentIndex(self, index):
        '''void QDataWidgetMapper.setCurrentIndex(int index)'''
    def revert(self):
        '''void QDataWidgetMapper.revert()'''
    def currentIndex(self):
        '''int QDataWidgetMapper.currentIndex()'''
        return int()
    def clearMapping(self):
        '''void QDataWidgetMapper.clearMapping()'''
    def mappedWidgetAt(self, section):
        '''QWidget QDataWidgetMapper.mappedWidgetAt(int section)'''
        return QWidget()
    def mappedSection(self, widget):
        '''int QDataWidgetMapper.mappedSection(QWidget widget)'''
        return int()
    def mappedPropertyName(self, widget):
        '''QByteArray QDataWidgetMapper.mappedPropertyName(QWidget widget)'''
        return QByteArray()
    def removeMapping(self, widget):
        '''void QDataWidgetMapper.removeMapping(QWidget widget)'''
    def addMapping(self, widget, section):
        '''void QDataWidgetMapper.addMapping(QWidget widget, int section)'''
    def addMapping(self, widget, section, propertyName):
        '''void QDataWidgetMapper.addMapping(QWidget widget, int section, QByteArray propertyName)'''
    def submitPolicy(self):
        '''QDataWidgetMapper.SubmitPolicy QDataWidgetMapper.submitPolicy()'''
        return QDataWidgetMapper.SubmitPolicy()
    def setSubmitPolicy(self, policy):
        '''void QDataWidgetMapper.setSubmitPolicy(QDataWidgetMapper.SubmitPolicy policy)'''
    def orientation(self):
        '''Qt.Orientation QDataWidgetMapper.orientation()'''
        return Qt.Orientation()
    def setOrientation(self, aOrientation):
        '''void QDataWidgetMapper.setOrientation(Qt.Orientation aOrientation)'''
    def rootIndex(self):
        '''QModelIndex QDataWidgetMapper.rootIndex()'''
        return QModelIndex()
    def setRootIndex(self, index):
        '''void QDataWidgetMapper.setRootIndex(QModelIndex index)'''
    def itemDelegate(self):
        '''QAbstractItemDelegate QDataWidgetMapper.itemDelegate()'''
        return QAbstractItemDelegate()
    def setItemDelegate(self, delegate):
        '''void QDataWidgetMapper.setItemDelegate(QAbstractItemDelegate delegate)'''
    def model(self):
        '''QAbstractItemModel QDataWidgetMapper.model()'''
        return QAbstractItemModel()
    def setModel(self, model):
        '''void QDataWidgetMapper.setModel(QAbstractItemModel model)'''


class QDateTimeEdit(QAbstractSpinBox):
    """"""
    # Enum QDateTimeEdit.Section
    NoSection = 0
    AmPmSection = 0
    MSecSection = 0
    SecondSection = 0
    MinuteSection = 0
    HourSection = 0
    DaySection = 0
    MonthSection = 0
    YearSection = 0
    TimeSections_Mask = 0
    DateSections_Mask = 0

    def __init__(self, parent = None):
        '''void QDateTimeEdit.__init__(QWidget parent = None)'''
    def __init__(self, datetime, parent = None):
        '''void QDateTimeEdit.__init__(QDateTime datetime, QWidget parent = None)'''
    def __init__(self, date, parent = None):
        '''void QDateTimeEdit.__init__(QDate date, QWidget parent = None)'''
    def __init__(self, time, parent = None):
        '''void QDateTimeEdit.__init__(QTime time, QWidget parent = None)'''
    def setTimeSpec(self, spec):
        '''void QDateTimeEdit.setTimeSpec(Qt.TimeSpec spec)'''
    def timeSpec(self):
        '''Qt.TimeSpec QDateTimeEdit.timeSpec()'''
        return Qt.TimeSpec()
    def setCalendarWidget(self, calendarWidget):
        '''void QDateTimeEdit.setCalendarWidget(QCalendarWidget calendarWidget)'''
    def calendarWidget(self):
        '''QCalendarWidget QDateTimeEdit.calendarWidget()'''
        return QCalendarWidget()
    def setDateTimeRange(self, min, max):
        '''void QDateTimeEdit.setDateTimeRange(QDateTime min, QDateTime max)'''
    def setMaximumDateTime(self, dt):
        '''void QDateTimeEdit.setMaximumDateTime(QDateTime dt)'''
    def clearMaximumDateTime(self):
        '''void QDateTimeEdit.clearMaximumDateTime()'''
    def maximumDateTime(self):
        '''QDateTime QDateTimeEdit.maximumDateTime()'''
        return QDateTime()
    def setMinimumDateTime(self, dt):
        '''void QDateTimeEdit.setMinimumDateTime(QDateTime dt)'''
    def clearMinimumDateTime(self):
        '''void QDateTimeEdit.clearMinimumDateTime()'''
    def minimumDateTime(self):
        '''QDateTime QDateTimeEdit.minimumDateTime()'''
        return QDateTime()
    def stepEnabled(self):
        '''QAbstractSpinBox.StepEnabled QDateTimeEdit.stepEnabled()'''
        return QAbstractSpinBox.StepEnabled()
    def textFromDateTime(self, dt):
        '''str QDateTimeEdit.textFromDateTime(QDateTime dt)'''
        return str()
    def dateTimeFromText(self, text):
        '''QDateTime QDateTimeEdit.dateTimeFromText(str text)'''
        return QDateTime()
    def fixup(self, input):
        '''void QDateTimeEdit.fixup(str input)'''
    def validate(self, input, pos):
        '''QValidator.State QDateTimeEdit.validate(str input, int pos)'''
        return QValidator.State()
    def paintEvent(self, event):
        '''void QDateTimeEdit.paintEvent(QPaintEvent event)'''
    def mousePressEvent(self, event):
        '''void QDateTimeEdit.mousePressEvent(QMouseEvent event)'''
    def focusNextPrevChild(self, next):
        '''bool QDateTimeEdit.focusNextPrevChild(bool next)'''
        return bool()
    def focusInEvent(self, e):
        '''void QDateTimeEdit.focusInEvent(QFocusEvent e)'''
    def wheelEvent(self, e):
        '''void QDateTimeEdit.wheelEvent(QWheelEvent e)'''
    def keyPressEvent(self, e):
        '''void QDateTimeEdit.keyPressEvent(QKeyEvent e)'''
    def initStyleOption(self, option):
        '''void QDateTimeEdit.initStyleOption(QStyleOptionSpinBox option)'''
    def setTime(self, time):
        '''void QDateTimeEdit.setTime(QTime time)'''
    def setDate(self, date):
        '''void QDateTimeEdit.setDate(QDate date)'''
    def setDateTime(self, dateTime):
        '''void QDateTimeEdit.setDateTime(QDateTime dateTime)'''
    dateChanged = pyqtSignal() # void dateChanged(const QDateamp;) - signal
    timeChanged = pyqtSignal() # void timeChanged(const QTimeamp;) - signal
    dateTimeChanged = pyqtSignal() # void dateTimeChanged(const QDateTimeamp;) - signal
    def sectionCount(self):
        '''int QDateTimeEdit.sectionCount()'''
        return int()
    def setCurrentSectionIndex(self, index):
        '''void QDateTimeEdit.setCurrentSectionIndex(int index)'''
    def currentSectionIndex(self):
        '''int QDateTimeEdit.currentSectionIndex()'''
        return int()
    def sectionAt(self, index):
        '''QDateTimeEdit.Section QDateTimeEdit.sectionAt(int index)'''
        return QDateTimeEdit.Section()
    def event(self, e):
        '''bool QDateTimeEdit.event(QEvent e)'''
        return bool()
    def stepBy(self, steps):
        '''void QDateTimeEdit.stepBy(int steps)'''
    def clear(self):
        '''void QDateTimeEdit.clear()'''
    def sizeHint(self):
        '''QSize QDateTimeEdit.sizeHint()'''
        return QSize()
    def setSelectedSection(self, section):
        '''void QDateTimeEdit.setSelectedSection(QDateTimeEdit.Section section)'''
    def setCalendarPopup(self, enable):
        '''void QDateTimeEdit.setCalendarPopup(bool enable)'''
    def calendarPopup(self):
        '''bool QDateTimeEdit.calendarPopup()'''
        return bool()
    def setDisplayFormat(self, format):
        '''void QDateTimeEdit.setDisplayFormat(str format)'''
    def displayFormat(self):
        '''str QDateTimeEdit.displayFormat()'''
        return str()
    def sectionText(self, s):
        '''str QDateTimeEdit.sectionText(QDateTimeEdit.Section s)'''
        return str()
    def setCurrentSection(self, section):
        '''void QDateTimeEdit.setCurrentSection(QDateTimeEdit.Section section)'''
    def currentSection(self):
        '''QDateTimeEdit.Section QDateTimeEdit.currentSection()'''
        return QDateTimeEdit.Section()
    def displayedSections(self):
        '''QDateTimeEdit.Sections QDateTimeEdit.displayedSections()'''
        return QDateTimeEdit.Sections()
    def setTimeRange(self, min, max):
        '''void QDateTimeEdit.setTimeRange(QTime min, QTime max)'''
    def clearMaximumTime(self):
        '''void QDateTimeEdit.clearMaximumTime()'''
    def setMaximumTime(self, max):
        '''void QDateTimeEdit.setMaximumTime(QTime max)'''
    def maximumTime(self):
        '''QTime QDateTimeEdit.maximumTime()'''
        return QTime()
    def clearMinimumTime(self):
        '''void QDateTimeEdit.clearMinimumTime()'''
    def setMinimumTime(self, min):
        '''void QDateTimeEdit.setMinimumTime(QTime min)'''
    def minimumTime(self):
        '''QTime QDateTimeEdit.minimumTime()'''
        return QTime()
    def setDateRange(self, min, max):
        '''void QDateTimeEdit.setDateRange(QDate min, QDate max)'''
    def clearMaximumDate(self):
        '''void QDateTimeEdit.clearMaximumDate()'''
    def setMaximumDate(self, max):
        '''void QDateTimeEdit.setMaximumDate(QDate max)'''
    def maximumDate(self):
        '''QDate QDateTimeEdit.maximumDate()'''
        return QDate()
    def clearMinimumDate(self):
        '''void QDateTimeEdit.clearMinimumDate()'''
    def setMinimumDate(self, min):
        '''void QDateTimeEdit.setMinimumDate(QDate min)'''
    def minimumDate(self):
        '''QDate QDateTimeEdit.minimumDate()'''
        return QDate()
    def time(self):
        '''QTime QDateTimeEdit.time()'''
        return QTime()
    def date(self):
        '''QDate QDateTimeEdit.date()'''
        return QDate()
    def dateTime(self):
        '''QDateTime QDateTimeEdit.dateTime()'''
        return QDateTime()
    class Sections():
        """"""
        def __init__(self):
            '''QDateTimeEdit.Sections QDateTimeEdit.Sections.__init__()'''
            return QDateTimeEdit.Sections()
        def __init__(self):
            '''int QDateTimeEdit.Sections.__init__()'''
            return int()
        def __init__(self):
            '''void QDateTimeEdit.Sections.__init__()'''
        def __bool__(self):
            '''int QDateTimeEdit.Sections.__bool__()'''
            return int()
        def __ne__(self, f):
            '''bool QDateTimeEdit.Sections.__ne__(QDateTimeEdit.Sections f)'''
            return bool()
        def __eq__(self, f):
            '''bool QDateTimeEdit.Sections.__eq__(QDateTimeEdit.Sections f)'''
            return bool()
        def __invert__(self):
            '''QDateTimeEdit.Sections QDateTimeEdit.Sections.__invert__()'''
            return QDateTimeEdit.Sections()
        def __and__(self, mask):
            '''QDateTimeEdit.Sections QDateTimeEdit.Sections.__and__(int mask)'''
            return QDateTimeEdit.Sections()
        def __xor__(self, f):
            '''QDateTimeEdit.Sections QDateTimeEdit.Sections.__xor__(QDateTimeEdit.Sections f)'''
            return QDateTimeEdit.Sections()
        def __xor__(self, f):
            '''QDateTimeEdit.Sections QDateTimeEdit.Sections.__xor__(int f)'''
            return QDateTimeEdit.Sections()
        def __or__(self, f):
            '''QDateTimeEdit.Sections QDateTimeEdit.Sections.__or__(QDateTimeEdit.Sections f)'''
            return QDateTimeEdit.Sections()
        def __or__(self, f):
            '''QDateTimeEdit.Sections QDateTimeEdit.Sections.__or__(int f)'''
            return QDateTimeEdit.Sections()
        def __int__(self):
            '''int QDateTimeEdit.Sections.__int__()'''
            return int()
        def __ixor__(self, f):
            '''QDateTimeEdit.Sections QDateTimeEdit.Sections.__ixor__(QDateTimeEdit.Sections f)'''
            return QDateTimeEdit.Sections()
        def __ior__(self, f):
            '''QDateTimeEdit.Sections QDateTimeEdit.Sections.__ior__(QDateTimeEdit.Sections f)'''
            return QDateTimeEdit.Sections()
        def __iand__(self, mask):
            '''QDateTimeEdit.Sections QDateTimeEdit.Sections.__iand__(int mask)'''
            return QDateTimeEdit.Sections()


class QTimeEdit(QDateTimeEdit):
    """"""
    def __init__(self, parent = None):
        '''void QTimeEdit.__init__(QWidget parent = None)'''
    def __init__(self, time, parent = None):
        '''void QTimeEdit.__init__(QTime time, QWidget parent = None)'''


class QDateEdit(QDateTimeEdit):
    """"""
    def __init__(self, parent = None):
        '''void QDateEdit.__init__(QWidget parent = None)'''
    def __init__(self, date, parent = None):
        '''void QDateEdit.__init__(QDate date, QWidget parent = None)'''


class QDesktopWidget(QWidget):
    """"""
    def __init__(self):
        '''void QDesktopWidget.__init__()'''
    def resizeEvent(self, e):
        '''void QDesktopWidget.resizeEvent(QResizeEvent e)'''
    screenCountChanged = pyqtSignal() # void screenCountChanged(int) - signal
    workAreaResized = pyqtSignal() # void workAreaResized(int) - signal
    resized = pyqtSignal() # void resized(int) - signal
    def availableGeometry(self, screen = None):
        '''QRect QDesktopWidget.availableGeometry(int screen = -1)'''
        return QRect()
    def availableGeometry(self, widget):
        '''QRect QDesktopWidget.availableGeometry(QWidget widget)'''
        return QRect()
    def availableGeometry(self, point):
        '''QRect QDesktopWidget.availableGeometry(QPoint point)'''
        return QRect()
    def screenGeometry(self, screen = None):
        '''QRect QDesktopWidget.screenGeometry(int screen = -1)'''
        return QRect()
    def screenGeometry(self, widget):
        '''QRect QDesktopWidget.screenGeometry(QWidget widget)'''
        return QRect()
    def screenGeometry(self, point):
        '''QRect QDesktopWidget.screenGeometry(QPoint point)'''
        return QRect()
    def screenCount(self):
        '''int QDesktopWidget.screenCount()'''
        return int()
    def screen(self, screen = None):
        '''QWidget QDesktopWidget.screen(int screen = -1)'''
        return QWidget()
    def screenNumber(self, widget = None):
        '''int QDesktopWidget.screenNumber(QWidget widget = None)'''
        return int()
    def screenNumber(self):
        '''QPoint QDesktopWidget.screenNumber()'''
        return QPoint()
    def primaryScreen(self):
        '''int QDesktopWidget.primaryScreen()'''
        return int()
    def isVirtualDesktop(self):
        '''bool QDesktopWidget.isVirtualDesktop()'''
        return bool()


class QDial(QAbstractSlider):
    """"""
    def __init__(self, parent = None):
        '''void QDial.__init__(QWidget parent = None)'''
    def sliderChange(self, change):
        '''void QDial.sliderChange(QAbstractSlider.SliderChange change)'''
    def mouseMoveEvent(self, me):
        '''void QDial.mouseMoveEvent(QMouseEvent me)'''
    def mouseReleaseEvent(self, me):
        '''void QDial.mouseReleaseEvent(QMouseEvent me)'''
    def mousePressEvent(self, me):
        '''void QDial.mousePressEvent(QMouseEvent me)'''
    def paintEvent(self, pe):
        '''void QDial.paintEvent(QPaintEvent pe)'''
    def resizeEvent(self, re):
        '''void QDial.resizeEvent(QResizeEvent re)'''
    def event(self, e):
        '''bool QDial.event(QEvent e)'''
        return bool()
    def initStyleOption(self, option):
        '''void QDial.initStyleOption(QStyleOptionSlider option)'''
    def setWrapping(self, on):
        '''void QDial.setWrapping(bool on)'''
    def setNotchesVisible(self, visible):
        '''void QDial.setNotchesVisible(bool visible)'''
    def minimumSizeHint(self):
        '''QSize QDial.minimumSizeHint()'''
        return QSize()
    def sizeHint(self):
        '''QSize QDial.sizeHint()'''
        return QSize()
    def notchesVisible(self):
        '''bool QDial.notchesVisible()'''
        return bool()
    def notchTarget(self):
        '''float QDial.notchTarget()'''
        return float()
    def setNotchTarget(self, target):
        '''void QDial.setNotchTarget(float target)'''
    def notchSize(self):
        '''int QDial.notchSize()'''
        return int()
    def wrapping(self):
        '''bool QDial.wrapping()'''
        return bool()


class QDialogButtonBox(QWidget):
    """"""
    # Enum QDialogButtonBox.StandardButton
    NoButton = 0
    Ok = 0
    Save = 0
    SaveAll = 0
    Open = 0
    Yes = 0
    YesToAll = 0
    No = 0
    NoToAll = 0
    Abort = 0
    Retry = 0
    Ignore = 0
    Close = 0
    Cancel = 0
    Discard = 0
    Help = 0
    Apply = 0
    Reset = 0
    RestoreDefaults = 0

    # Enum QDialogButtonBox.ButtonRole
    InvalidRole = 0
    AcceptRole = 0
    RejectRole = 0
    DestructiveRole = 0
    ActionRole = 0
    HelpRole = 0
    YesRole = 0
    NoRole = 0
    ResetRole = 0
    ApplyRole = 0

    # Enum QDialogButtonBox.ButtonLayout
    WinLayout = 0
    MacLayout = 0
    KdeLayout = 0
    GnomeLayout = 0

    def __init__(self, parent = None):
        '''void QDialogButtonBox.__init__(QWidget parent = None)'''
    def __init__(self, orientation, parent = None):
        '''void QDialogButtonBox.__init__(Qt.Orientation orientation, QWidget parent = None)'''
    def __init__(self, buttons, parent = None):
        '''void QDialogButtonBox.__init__(QDialogButtonBox.StandardButtons buttons, QWidget parent = None)'''
    def __init__(self, buttons, orientation, parent = None):
        '''void QDialogButtonBox.__init__(QDialogButtonBox.StandardButtons buttons, Qt.Orientation orientation, QWidget parent = None)'''
    def event(self, event):
        '''bool QDialogButtonBox.event(QEvent event)'''
        return bool()
    def changeEvent(self, event):
        '''void QDialogButtonBox.changeEvent(QEvent event)'''
    rejected = pyqtSignal() # void rejected() - signal
    helpRequested = pyqtSignal() # void helpRequested() - signal
    clicked = pyqtSignal() # void clicked(QAbstractButton*) - signal
    accepted = pyqtSignal() # void accepted() - signal
    def centerButtons(self):
        '''bool QDialogButtonBox.centerButtons()'''
        return bool()
    def setCenterButtons(self, center):
        '''void QDialogButtonBox.setCenterButtons(bool center)'''
    def button(self, which):
        '''QPushButton QDialogButtonBox.button(QDialogButtonBox.StandardButton which)'''
        return QPushButton()
    def standardButton(self, button):
        '''QDialogButtonBox.StandardButton QDialogButtonBox.standardButton(QAbstractButton button)'''
        return QDialogButtonBox.StandardButton()
    def standardButtons(self):
        '''QDialogButtonBox.StandardButtons QDialogButtonBox.standardButtons()'''
        return QDialogButtonBox.StandardButtons()
    def setStandardButtons(self, buttons):
        '''void QDialogButtonBox.setStandardButtons(QDialogButtonBox.StandardButtons buttons)'''
    def buttonRole(self, button):
        '''QDialogButtonBox.ButtonRole QDialogButtonBox.buttonRole(QAbstractButton button)'''
        return QDialogButtonBox.ButtonRole()
    def buttons(self):
        '''list-of-QAbstractButton QDialogButtonBox.buttons()'''
        return [QAbstractButton()]
    def clear(self):
        '''void QDialogButtonBox.clear()'''
    def removeButton(self, button):
        '''void QDialogButtonBox.removeButton(QAbstractButton button)'''
    def addButton(self, button, role):
        '''void QDialogButtonBox.addButton(QAbstractButton button, QDialogButtonBox.ButtonRole role)'''
    def addButton(self, text, role):
        '''QPushButton QDialogButtonBox.addButton(str text, QDialogButtonBox.ButtonRole role)'''
        return QPushButton()
    def addButton(self, button):
        '''QPushButton QDialogButtonBox.addButton(QDialogButtonBox.StandardButton button)'''
        return QPushButton()
    def orientation(self):
        '''Qt.Orientation QDialogButtonBox.orientation()'''
        return Qt.Orientation()
    def setOrientation(self, orientation):
        '''void QDialogButtonBox.setOrientation(Qt.Orientation orientation)'''
    class StandardButtons():
        """"""
        def __init__(self):
            '''QDialogButtonBox.StandardButtons QDialogButtonBox.StandardButtons.__init__()'''
            return QDialogButtonBox.StandardButtons()
        def __init__(self):
            '''int QDialogButtonBox.StandardButtons.__init__()'''
            return int()
        def __init__(self):
            '''void QDialogButtonBox.StandardButtons.__init__()'''
        def __bool__(self):
            '''int QDialogButtonBox.StandardButtons.__bool__()'''
            return int()
        def __ne__(self, f):
            '''bool QDialogButtonBox.StandardButtons.__ne__(QDialogButtonBox.StandardButtons f)'''
            return bool()
        def __eq__(self, f):
            '''bool QDialogButtonBox.StandardButtons.__eq__(QDialogButtonBox.StandardButtons f)'''
            return bool()
        def __invert__(self):
            '''QDialogButtonBox.StandardButtons QDialogButtonBox.StandardButtons.__invert__()'''
            return QDialogButtonBox.StandardButtons()
        def __and__(self, mask):
            '''QDialogButtonBox.StandardButtons QDialogButtonBox.StandardButtons.__and__(int mask)'''
            return QDialogButtonBox.StandardButtons()
        def __xor__(self, f):
            '''QDialogButtonBox.StandardButtons QDialogButtonBox.StandardButtons.__xor__(QDialogButtonBox.StandardButtons f)'''
            return QDialogButtonBox.StandardButtons()
        def __xor__(self, f):
            '''QDialogButtonBox.StandardButtons QDialogButtonBox.StandardButtons.__xor__(int f)'''
            return QDialogButtonBox.StandardButtons()
        def __or__(self, f):
            '''QDialogButtonBox.StandardButtons QDialogButtonBox.StandardButtons.__or__(QDialogButtonBox.StandardButtons f)'''
            return QDialogButtonBox.StandardButtons()
        def __or__(self, f):
            '''QDialogButtonBox.StandardButtons QDialogButtonBox.StandardButtons.__or__(int f)'''
            return QDialogButtonBox.StandardButtons()
        def __int__(self):
            '''int QDialogButtonBox.StandardButtons.__int__()'''
            return int()
        def __ixor__(self, f):
            '''QDialogButtonBox.StandardButtons QDialogButtonBox.StandardButtons.__ixor__(QDialogButtonBox.StandardButtons f)'''
            return QDialogButtonBox.StandardButtons()
        def __ior__(self, f):
            '''QDialogButtonBox.StandardButtons QDialogButtonBox.StandardButtons.__ior__(QDialogButtonBox.StandardButtons f)'''
            return QDialogButtonBox.StandardButtons()
        def __iand__(self, mask):
            '''QDialogButtonBox.StandardButtons QDialogButtonBox.StandardButtons.__iand__(int mask)'''
            return QDialogButtonBox.StandardButtons()


class QDirModel(QAbstractItemModel):
    """"""
    # Enum QDirModel.Roles
    FileIconRole = 0
    FilePathRole = 0
    FileNameRole = 0

    def __init__(self, nameFilters, filters, sort, parent = None):
        '''void QDirModel.__init__(list-of-str nameFilters, QDir.Filters filters, QDir.SortFlags sort, QObject parent = None)'''
    def __init__(self, parent = None):
        '''void QDirModel.__init__(QObject parent = None)'''
    def fileInfo(self, index):
        '''QFileInfo QDirModel.fileInfo(QModelIndex index)'''
        return QFileInfo()
    def fileIcon(self, index):
        '''QIcon QDirModel.fileIcon(QModelIndex index)'''
        return QIcon()
    def fileName(self, index):
        '''str QDirModel.fileName(QModelIndex index)'''
        return str()
    def filePath(self, index):
        '''str QDirModel.filePath(QModelIndex index)'''
        return str()
    def remove(self, index):
        '''bool QDirModel.remove(QModelIndex index)'''
        return bool()
    def rmdir(self, index):
        '''bool QDirModel.rmdir(QModelIndex index)'''
        return bool()
    def mkdir(self, parent, name):
        '''QModelIndex QDirModel.mkdir(QModelIndex parent, str name)'''
        return QModelIndex()
    def isDir(self, index):
        '''bool QDirModel.isDir(QModelIndex index)'''
        return bool()
    def refresh(self, parent = QModelIndex()):
        '''void QDirModel.refresh(QModelIndex parent = QModelIndex())'''
    def lazyChildCount(self):
        '''bool QDirModel.lazyChildCount()'''
        return bool()
    def setLazyChildCount(self, enable):
        '''void QDirModel.setLazyChildCount(bool enable)'''
    def isReadOnly(self):
        '''bool QDirModel.isReadOnly()'''
        return bool()
    def setReadOnly(self, enable):
        '''void QDirModel.setReadOnly(bool enable)'''
    def resolveSymlinks(self):
        '''bool QDirModel.resolveSymlinks()'''
        return bool()
    def setResolveSymlinks(self, enable):
        '''void QDirModel.setResolveSymlinks(bool enable)'''
    def sorting(self):
        '''QDir.SortFlags QDirModel.sorting()'''
        return QDir.SortFlags()
    def setSorting(self, sort):
        '''void QDirModel.setSorting(QDir.SortFlags sort)'''
    def filter(self):
        '''QDir.Filters QDirModel.filter()'''
        return QDir.Filters()
    def setFilter(self, filters):
        '''void QDirModel.setFilter(QDir.Filters filters)'''
    def nameFilters(self):
        '''list-of-str QDirModel.nameFilters()'''
        return [str()]
    def setNameFilters(self, filters):
        '''void QDirModel.setNameFilters(list-of-str filters)'''
    def iconProvider(self):
        '''QFileIconProvider QDirModel.iconProvider()'''
        return QFileIconProvider()
    def setIconProvider(self, provider):
        '''void QDirModel.setIconProvider(QFileIconProvider provider)'''
    def supportedDropActions(self):
        '''Qt.DropActions QDirModel.supportedDropActions()'''
        return Qt.DropActions()
    def dropMimeData(self, data, action, row, column, parent):
        '''bool QDirModel.dropMimeData(QMimeData data, Qt.DropAction action, int row, int column, QModelIndex parent)'''
        return bool()
    def mimeData(self, indexes):
        '''QMimeData QDirModel.mimeData(list-of-QModelIndex indexes)'''
        return QMimeData()
    def mimeTypes(self):
        '''list-of-str QDirModel.mimeTypes()'''
        return [str()]
    def sort(self, column, order = None):
        '''void QDirModel.sort(int column, Qt.SortOrder order = Qt.AscendingOrder)'''
    def flags(self, index):
        '''Qt.ItemFlags QDirModel.flags(QModelIndex index)'''
        return Qt.ItemFlags()
    def hasChildren(self, parent = QModelIndex()):
        '''bool QDirModel.hasChildren(QModelIndex parent = QModelIndex())'''
        return bool()
    def headerData(self, section, orientation, role = None):
        '''QVariant QDirModel.headerData(int section, Qt.Orientation orientation, int role = Qt.DisplayRole)'''
        return QVariant()
    def setData(self, index, value, role = None):
        '''bool QDirModel.setData(QModelIndex index, QVariant value, int role = Qt.EditRole)'''
        return bool()
    def data(self, index, role = None):
        '''QVariant QDirModel.data(QModelIndex index, int role = Qt.DisplayRole)'''
        return QVariant()
    def columnCount(self, parent = QModelIndex()):
        '''int QDirModel.columnCount(QModelIndex parent = QModelIndex())'''
        return int()
    def rowCount(self, parent = QModelIndex()):
        '''int QDirModel.rowCount(QModelIndex parent = QModelIndex())'''
        return int()
    def parent(self, child):
        '''QModelIndex QDirModel.parent(QModelIndex child)'''
        return QModelIndex()
    def parent(self):
        '''QObject QDirModel.parent()'''
        return QObject()
    def index(self, row, column, parent = QModelIndex()):
        '''QModelIndex QDirModel.index(int row, int column, QModelIndex parent = QModelIndex())'''
        return QModelIndex()
    def index(self, path, column = 0):
        '''QModelIndex QDirModel.index(str path, int column = 0)'''
        return QModelIndex()


class QDockWidget(QWidget):
    """"""
    # Enum QDockWidget.DockWidgetFeature
    DockWidgetClosable = 0
    DockWidgetMovable = 0
    DockWidgetFloatable = 0
    DockWidgetVerticalTitleBar = 0
    AllDockWidgetFeatures = 0
    NoDockWidgetFeatures = 0

    def __init__(self, title, parent = None, flags = 0):
        '''void QDockWidget.__init__(str title, QWidget parent = None, Qt.WindowFlags flags = 0)'''
    def __init__(self, parent = None, flags = 0):
        '''void QDockWidget.__init__(QWidget parent = None, Qt.WindowFlags flags = 0)'''
    def event(self, event):
        '''bool QDockWidget.event(QEvent event)'''
        return bool()
    def paintEvent(self, event):
        '''void QDockWidget.paintEvent(QPaintEvent event)'''
    def closeEvent(self, event):
        '''void QDockWidget.closeEvent(QCloseEvent event)'''
    def changeEvent(self, event):
        '''void QDockWidget.changeEvent(QEvent event)'''
    def initStyleOption(self, option):
        '''void QDockWidget.initStyleOption(QStyleOptionDockWidget option)'''
    visibilityChanged = pyqtSignal() # void visibilityChanged(bool) - signal
    dockLocationChanged = pyqtSignal() # void dockLocationChanged(Qt::DockWidgetArea) - signal
    allowedAreasChanged = pyqtSignal() # void allowedAreasChanged(Qt::DockWidgetAreas) - signal
    topLevelChanged = pyqtSignal() # void topLevelChanged(bool) - signal
    featuresChanged = pyqtSignal() # void featuresChanged(QDockWidget::DockWidgetFeatures) - signal
    def titleBarWidget(self):
        '''QWidget QDockWidget.titleBarWidget()'''
        return QWidget()
    def setTitleBarWidget(self, widget):
        '''void QDockWidget.setTitleBarWidget(QWidget widget)'''
    def toggleViewAction(self):
        '''QAction QDockWidget.toggleViewAction()'''
        return QAction()
    def isAreaAllowed(self, area):
        '''bool QDockWidget.isAreaAllowed(Qt.DockWidgetArea area)'''
        return bool()
    def allowedAreas(self):
        '''Qt.DockWidgetAreas QDockWidget.allowedAreas()'''
        return Qt.DockWidgetAreas()
    def setAllowedAreas(self, areas):
        '''void QDockWidget.setAllowedAreas(Qt.DockWidgetAreas areas)'''
    def isFloating(self):
        '''bool QDockWidget.isFloating()'''
        return bool()
    def setFloating(self, floating):
        '''void QDockWidget.setFloating(bool floating)'''
    def features(self):
        '''QDockWidget.DockWidgetFeatures QDockWidget.features()'''
        return QDockWidget.DockWidgetFeatures()
    def setFeatures(self, features):
        '''void QDockWidget.setFeatures(QDockWidget.DockWidgetFeatures features)'''
    def setWidget(self, widget):
        '''void QDockWidget.setWidget(QWidget widget)'''
    def widget(self):
        '''QWidget QDockWidget.widget()'''
        return QWidget()
    class DockWidgetFeatures():
        """"""
        def __init__(self):
            '''QDockWidget.DockWidgetFeatures QDockWidget.DockWidgetFeatures.__init__()'''
            return QDockWidget.DockWidgetFeatures()
        def __init__(self):
            '''int QDockWidget.DockWidgetFeatures.__init__()'''
            return int()
        def __init__(self):
            '''void QDockWidget.DockWidgetFeatures.__init__()'''
        def __bool__(self):
            '''int QDockWidget.DockWidgetFeatures.__bool__()'''
            return int()
        def __ne__(self, f):
            '''bool QDockWidget.DockWidgetFeatures.__ne__(QDockWidget.DockWidgetFeatures f)'''
            return bool()
        def __eq__(self, f):
            '''bool QDockWidget.DockWidgetFeatures.__eq__(QDockWidget.DockWidgetFeatures f)'''
            return bool()
        def __invert__(self):
            '''QDockWidget.DockWidgetFeatures QDockWidget.DockWidgetFeatures.__invert__()'''
            return QDockWidget.DockWidgetFeatures()
        def __and__(self, mask):
            '''QDockWidget.DockWidgetFeatures QDockWidget.DockWidgetFeatures.__and__(int mask)'''
            return QDockWidget.DockWidgetFeatures()
        def __xor__(self, f):
            '''QDockWidget.DockWidgetFeatures QDockWidget.DockWidgetFeatures.__xor__(QDockWidget.DockWidgetFeatures f)'''
            return QDockWidget.DockWidgetFeatures()
        def __xor__(self, f):
            '''QDockWidget.DockWidgetFeatures QDockWidget.DockWidgetFeatures.__xor__(int f)'''
            return QDockWidget.DockWidgetFeatures()
        def __or__(self, f):
            '''QDockWidget.DockWidgetFeatures QDockWidget.DockWidgetFeatures.__or__(QDockWidget.DockWidgetFeatures f)'''
            return QDockWidget.DockWidgetFeatures()
        def __or__(self, f):
            '''QDockWidget.DockWidgetFeatures QDockWidget.DockWidgetFeatures.__or__(int f)'''
            return QDockWidget.DockWidgetFeatures()
        def __int__(self):
            '''int QDockWidget.DockWidgetFeatures.__int__()'''
            return int()
        def __ixor__(self, f):
            '''QDockWidget.DockWidgetFeatures QDockWidget.DockWidgetFeatures.__ixor__(QDockWidget.DockWidgetFeatures f)'''
            return QDockWidget.DockWidgetFeatures()
        def __ior__(self, f):
            '''QDockWidget.DockWidgetFeatures QDockWidget.DockWidgetFeatures.__ior__(QDockWidget.DockWidgetFeatures f)'''
            return QDockWidget.DockWidgetFeatures()
        def __iand__(self, mask):
            '''QDockWidget.DockWidgetFeatures QDockWidget.DockWidgetFeatures.__iand__(int mask)'''
            return QDockWidget.DockWidgetFeatures()


class QErrorMessage(QDialog):
    """"""
    def __init__(self, parent = None):
        '''void QErrorMessage.__init__(QWidget parent = None)'''
    def done(self):
        '''int QErrorMessage.done()'''
        return int()
    def changeEvent(self, e):
        '''void QErrorMessage.changeEvent(QEvent e)'''
    def showMessage(self, message):
        '''void QErrorMessage.showMessage(str message)'''
    def showMessage(self, message, type):
        '''void QErrorMessage.showMessage(str message, str type)'''
    def qtHandler(self):
        '''static QErrorMessage QErrorMessage.qtHandler()'''
        return QErrorMessage()


class QFileDialog(QDialog):
    """"""
    # Enum QFileDialog.Option
    ShowDirsOnly = 0
    DontResolveSymlinks = 0
    DontConfirmOverwrite = 0
    DontUseSheet = 0
    DontUseNativeDialog = 0
    ReadOnly = 0
    HideNameFilterDetails = 0
    DontUseCustomDirectoryIcons = 0

    # Enum QFileDialog.DialogLabel
    LookIn = 0
    FileName = 0
    FileType = 0
    Accept = 0
    Reject = 0

    # Enum QFileDialog.AcceptMode
    AcceptOpen = 0
    AcceptSave = 0

    # Enum QFileDialog.FileMode
    AnyFile = 0
    ExistingFile = 0
    Directory = 0
    ExistingFiles = 0
    DirectoryOnly = 0

    # Enum QFileDialog.ViewMode
    Detail = 0
    List = 0

    def __init__(self, parent, f):
        '''void QFileDialog.__init__(QWidget parent, Qt.WindowFlags f)'''
    def __init__(self, parent = None, caption = None, directory = None, filter = None):
        '''void QFileDialog.__init__(QWidget parent = None, str caption = '', str directory = '', str filter = '')'''
    def getSaveFileUrl(self, parent = None, caption = None, directory = None, filter = None, initialFilter = None, options = 0, supportedSchemes = None):
        '''static (QUrl, str) QFileDialog.getSaveFileUrl(QWidget parent = None, str caption = '', str directory = '', str filter = '', str initialFilter = '', QFileDialog.Options options = 0, list-of-str supportedSchemes = [])'''
        return (QUrl, str)()
    def getOpenFileUrls(self, parent = None, caption = None, directory = None, filter = None, initialFilter = None, options = 0, supportedSchemes = None):
        '''static (list-of-QUrl, str) QFileDialog.getOpenFileUrls(QWidget parent = None, str caption = '', str directory = '', str filter = '', str initialFilter = '', QFileDialog.Options options = 0, list-of-str supportedSchemes = [])'''
        return (list-of-QUrl, str)()
    def getOpenFileUrl(self, parent = None, caption = None, directory = None, filter = None, initialFilter = None, options = 0, supportedSchemes = None):
        '''static (QUrl, str) QFileDialog.getOpenFileUrl(QWidget parent = None, str caption = '', str directory = '', str filter = '', str initialFilter = '', QFileDialog.Options options = 0, list-of-str supportedSchemes = [])'''
        return (QUrl, str)()
    def getExistingDirectoryUrl(self, parent = None, caption = None, directory = QUrl(), options = None, supportedSchemes = None):
        '''static QUrl QFileDialog.getExistingDirectoryUrl(QWidget parent = None, str caption = '', QUrl directory = QUrl(), QFileDialog.Options options = QFileDialog.ShowDirsOnly, list-of-str supportedSchemes = [])'''
        return QUrl()
    directoryUrlEntered = pyqtSignal() # void directoryUrlEntered(const QUrlamp;) - signal
    currentUrlChanged = pyqtSignal() # void currentUrlChanged(const QUrlamp;) - signal
    urlsSelected = pyqtSignal() # void urlsSelected(const QListlt;QUrlgt;amp;) - signal
    urlSelected = pyqtSignal() # void urlSelected(const QUrlamp;) - signal
    def selectMimeTypeFilter(self, filter):
        '''void QFileDialog.selectMimeTypeFilter(str filter)'''
    def mimeTypeFilters(self):
        '''list-of-str QFileDialog.mimeTypeFilters()'''
        return [str()]
    def setMimeTypeFilters(self, filters):
        '''void QFileDialog.setMimeTypeFilters(list-of-str filters)'''
    def selectedUrls(self):
        '''list-of-QUrl QFileDialog.selectedUrls()'''
        return [QUrl()]
    def selectUrl(self, url):
        '''void QFileDialog.selectUrl(QUrl url)'''
    def directoryUrl(self):
        '''QUrl QFileDialog.directoryUrl()'''
        return QUrl()
    def setDirectoryUrl(self, directory):
        '''void QFileDialog.setDirectoryUrl(QUrl directory)'''
    def setVisible(self, visible):
        '''void QFileDialog.setVisible(bool visible)'''
    def open(self):
        '''void QFileDialog.open()'''
    def open(self, slot):
        '''void QFileDialog.open(slot slot)'''
    def options(self):
        '''QFileDialog.Options QFileDialog.options()'''
        return QFileDialog.Options()
    def setOptions(self, options):
        '''void QFileDialog.setOptions(QFileDialog.Options options)'''
    def testOption(self, option):
        '''bool QFileDialog.testOption(QFileDialog.Option option)'''
        return bool()
    def setOption(self, option, on = True):
        '''void QFileDialog.setOption(QFileDialog.Option option, bool on = True)'''
    def setFilter(self, filters):
        '''void QFileDialog.setFilter(QDir.Filters filters)'''
    def filter(self):
        '''QDir.Filters QFileDialog.filter()'''
        return QDir.Filters()
    def selectedNameFilter(self):
        '''str QFileDialog.selectedNameFilter()'''
        return str()
    def selectNameFilter(self, filter):
        '''void QFileDialog.selectNameFilter(str filter)'''
    def nameFilters(self):
        '''list-of-str QFileDialog.nameFilters()'''
        return [str()]
    def setNameFilters(self, filters):
        '''void QFileDialog.setNameFilters(list-of-str filters)'''
    def setNameFilter(self, filter):
        '''void QFileDialog.setNameFilter(str filter)'''
    def proxyModel(self):
        '''QAbstractProxyModel QFileDialog.proxyModel()'''
        return QAbstractProxyModel()
    def setProxyModel(self, model):
        '''void QFileDialog.setProxyModel(QAbstractProxyModel model)'''
    def restoreState(self, state):
        '''bool QFileDialog.restoreState(QByteArray state)'''
        return bool()
    def saveState(self):
        '''QByteArray QFileDialog.saveState()'''
        return QByteArray()
    def sidebarUrls(self):
        '''list-of-QUrl QFileDialog.sidebarUrls()'''
        return [QUrl()]
    def setSidebarUrls(self, urls):
        '''void QFileDialog.setSidebarUrls(list-of-QUrl urls)'''
    def changeEvent(self, e):
        '''void QFileDialog.changeEvent(QEvent e)'''
    def accept(self):
        '''void QFileDialog.accept()'''
    def done(self, result):
        '''void QFileDialog.done(int result)'''
    def getSaveFileName(self, parent = None, caption = None, directory = None, filter = None, initialFilter = None, options = 0):
        '''static (str, str) QFileDialog.getSaveFileName(QWidget parent = None, str caption = '', str directory = '', str filter = '', str initialFilter = '', QFileDialog.Options options = 0)'''
        return (str, str)()
    def getOpenFileNames(self, parent = None, caption = None, directory = None, filter = None, initialFilter = None, options = 0):
        '''static (list-of-str, str) QFileDialog.getOpenFileNames(QWidget parent = None, str caption = '', str directory = '', str filter = '', str initialFilter = '', QFileDialog.Options options = 0)'''
        return (list-of-str, str)()
    def getOpenFileName(self, parent = None, caption = None, directory = None, filter = None, initialFilter = None, options = 0):
        '''static (str, str) QFileDialog.getOpenFileName(QWidget parent = None, str caption = '', str directory = '', str filter = '', str initialFilter = '', QFileDialog.Options options = 0)'''
        return (str, str)()
    def getExistingDirectory(self, parent = None, caption = None, directory = None, options = None):
        '''static str QFileDialog.getExistingDirectory(QWidget parent = None, str caption = '', str directory = '', QFileDialog.Options options = QFileDialog.ShowDirsOnly)'''
        return str()
    fileSelected = pyqtSignal() # void fileSelected(const QStringamp;) - signal
    filterSelected = pyqtSignal() # void filterSelected(const QStringamp;) - signal
    filesSelected = pyqtSignal() # void filesSelected(const QStringListamp;) - signal
    directoryEntered = pyqtSignal() # void directoryEntered(const QStringamp;) - signal
    currentChanged = pyqtSignal() # void currentChanged(const QStringamp;) - signal
    def labelText(self, label):
        '''str QFileDialog.labelText(QFileDialog.DialogLabel label)'''
        return str()
    def setLabelText(self, label, text):
        '''void QFileDialog.setLabelText(QFileDialog.DialogLabel label, str text)'''
    def iconProvider(self):
        '''QFileIconProvider QFileDialog.iconProvider()'''
        return QFileIconProvider()
    def setIconProvider(self, provider):
        '''void QFileDialog.setIconProvider(QFileIconProvider provider)'''
    def itemDelegate(self):
        '''QAbstractItemDelegate QFileDialog.itemDelegate()'''
        return QAbstractItemDelegate()
    def setItemDelegate(self, delegate):
        '''void QFileDialog.setItemDelegate(QAbstractItemDelegate delegate)'''
    def history(self):
        '''list-of-str QFileDialog.history()'''
        return [str()]
    def setHistory(self, paths):
        '''void QFileDialog.setHistory(list-of-str paths)'''
    def defaultSuffix(self):
        '''str QFileDialog.defaultSuffix()'''
        return str()
    def setDefaultSuffix(self, suffix):
        '''void QFileDialog.setDefaultSuffix(str suffix)'''
    def acceptMode(self):
        '''QFileDialog.AcceptMode QFileDialog.acceptMode()'''
        return QFileDialog.AcceptMode()
    def setAcceptMode(self, mode):
        '''void QFileDialog.setAcceptMode(QFileDialog.AcceptMode mode)'''
    def fileMode(self):
        '''QFileDialog.FileMode QFileDialog.fileMode()'''
        return QFileDialog.FileMode()
    def setFileMode(self, mode):
        '''void QFileDialog.setFileMode(QFileDialog.FileMode mode)'''
    def viewMode(self):
        '''QFileDialog.ViewMode QFileDialog.viewMode()'''
        return QFileDialog.ViewMode()
    def setViewMode(self, mode):
        '''void QFileDialog.setViewMode(QFileDialog.ViewMode mode)'''
    def selectedFiles(self):
        '''list-of-str QFileDialog.selectedFiles()'''
        return [str()]
    def selectFile(self, filename):
        '''void QFileDialog.selectFile(str filename)'''
    def directory(self):
        '''QDir QFileDialog.directory()'''
        return QDir()
    def setDirectory(self, directory):
        '''void QFileDialog.setDirectory(str directory)'''
    def setDirectory(self, adirectory):
        '''void QFileDialog.setDirectory(QDir adirectory)'''
    class Options():
        """"""
        def __init__(self):
            '''QFileDialog.Options QFileDialog.Options.__init__()'''
            return QFileDialog.Options()
        def __init__(self):
            '''int QFileDialog.Options.__init__()'''
            return int()
        def __init__(self):
            '''void QFileDialog.Options.__init__()'''
        def __bool__(self):
            '''int QFileDialog.Options.__bool__()'''
            return int()
        def __ne__(self, f):
            '''bool QFileDialog.Options.__ne__(QFileDialog.Options f)'''
            return bool()
        def __eq__(self, f):
            '''bool QFileDialog.Options.__eq__(QFileDialog.Options f)'''
            return bool()
        def __invert__(self):
            '''QFileDialog.Options QFileDialog.Options.__invert__()'''
            return QFileDialog.Options()
        def __and__(self, mask):
            '''QFileDialog.Options QFileDialog.Options.__and__(int mask)'''
            return QFileDialog.Options()
        def __xor__(self, f):
            '''QFileDialog.Options QFileDialog.Options.__xor__(QFileDialog.Options f)'''
            return QFileDialog.Options()
        def __xor__(self, f):
            '''QFileDialog.Options QFileDialog.Options.__xor__(int f)'''
            return QFileDialog.Options()
        def __or__(self, f):
            '''QFileDialog.Options QFileDialog.Options.__or__(QFileDialog.Options f)'''
            return QFileDialog.Options()
        def __or__(self, f):
            '''QFileDialog.Options QFileDialog.Options.__or__(int f)'''
            return QFileDialog.Options()
        def __int__(self):
            '''int QFileDialog.Options.__int__()'''
            return int()
        def __ixor__(self, f):
            '''QFileDialog.Options QFileDialog.Options.__ixor__(QFileDialog.Options f)'''
            return QFileDialog.Options()
        def __ior__(self, f):
            '''QFileDialog.Options QFileDialog.Options.__ior__(QFileDialog.Options f)'''
            return QFileDialog.Options()
        def __iand__(self, mask):
            '''QFileDialog.Options QFileDialog.Options.__iand__(int mask)'''
            return QFileDialog.Options()


class QFileIconProvider():
    """"""
    # Enum QFileIconProvider.Option
    DontUseCustomDirectoryIcons = 0

    # Enum QFileIconProvider.IconType
    Computer = 0
    Desktop = 0
    Trashcan = 0
    Network = 0
    Drive = 0
    Folder = 0
    File = 0

    def __init__(self):
        '''void QFileIconProvider.__init__()'''
    def options(self):
        '''QFileIconProvider.Options QFileIconProvider.options()'''
        return QFileIconProvider.Options()
    def setOptions(self, options):
        '''void QFileIconProvider.setOptions(QFileIconProvider.Options options)'''
    def type(self, info):
        '''str QFileIconProvider.type(QFileInfo info)'''
        return str()
    def icon(self, type):
        '''QIcon QFileIconProvider.icon(QFileIconProvider.IconType type)'''
        return QIcon()
    def icon(self, info):
        '''QIcon QFileIconProvider.icon(QFileInfo info)'''
        return QIcon()
    class Options():
        """"""
        def __init__(self):
            '''QFileIconProvider.Options QFileIconProvider.Options.__init__()'''
            return QFileIconProvider.Options()
        def __init__(self):
            '''int QFileIconProvider.Options.__init__()'''
            return int()
        def __init__(self):
            '''void QFileIconProvider.Options.__init__()'''
        def __bool__(self):
            '''int QFileIconProvider.Options.__bool__()'''
            return int()
        def __ne__(self, f):
            '''bool QFileIconProvider.Options.__ne__(QFileIconProvider.Options f)'''
            return bool()
        def __eq__(self, f):
            '''bool QFileIconProvider.Options.__eq__(QFileIconProvider.Options f)'''
            return bool()
        def __invert__(self):
            '''QFileIconProvider.Options QFileIconProvider.Options.__invert__()'''
            return QFileIconProvider.Options()
        def __and__(self, mask):
            '''QFileIconProvider.Options QFileIconProvider.Options.__and__(int mask)'''
            return QFileIconProvider.Options()
        def __xor__(self, f):
            '''QFileIconProvider.Options QFileIconProvider.Options.__xor__(QFileIconProvider.Options f)'''
            return QFileIconProvider.Options()
        def __xor__(self, f):
            '''QFileIconProvider.Options QFileIconProvider.Options.__xor__(int f)'''
            return QFileIconProvider.Options()
        def __or__(self, f):
            '''QFileIconProvider.Options QFileIconProvider.Options.__or__(QFileIconProvider.Options f)'''
            return QFileIconProvider.Options()
        def __or__(self, f):
            '''QFileIconProvider.Options QFileIconProvider.Options.__or__(int f)'''
            return QFileIconProvider.Options()
        def __int__(self):
            '''int QFileIconProvider.Options.__int__()'''
            return int()
        def __ixor__(self, f):
            '''QFileIconProvider.Options QFileIconProvider.Options.__ixor__(QFileIconProvider.Options f)'''
            return QFileIconProvider.Options()
        def __ior__(self, f):
            '''QFileIconProvider.Options QFileIconProvider.Options.__ior__(QFileIconProvider.Options f)'''
            return QFileIconProvider.Options()
        def __iand__(self, mask):
            '''QFileIconProvider.Options QFileIconProvider.Options.__iand__(int mask)'''
            return QFileIconProvider.Options()


class QFileSystemModel(QAbstractItemModel):
    """"""
    # Enum QFileSystemModel.Roles
    FileIconRole = 0
    FilePathRole = 0
    FileNameRole = 0
    FilePermissions = 0

    def __init__(self, parent = None):
        '''void QFileSystemModel.__init__(QObject parent = None)'''
    def timerEvent(self, event):
        '''void QFileSystemModel.timerEvent(QTimerEvent event)'''
    def event(self, event):
        '''bool QFileSystemModel.event(QEvent event)'''
        return bool()
    directoryLoaded = pyqtSignal() # void directoryLoaded(const QStringamp;) - signal
    rootPathChanged = pyqtSignal() # void rootPathChanged(const QStringamp;) - signal
    fileRenamed = pyqtSignal() # void fileRenamed(const QStringamp;,const QStringamp;,const QStringamp;) - signal
    def remove(self, index):
        '''bool QFileSystemModel.remove(QModelIndex index)'''
        return bool()
    def fileInfo(self, aindex):
        '''QFileInfo QFileSystemModel.fileInfo(QModelIndex aindex)'''
        return QFileInfo()
    def fileIcon(self, aindex):
        '''QIcon QFileSystemModel.fileIcon(QModelIndex aindex)'''
        return QIcon()
    def fileName(self, aindex):
        '''str QFileSystemModel.fileName(QModelIndex aindex)'''
        return str()
    def rmdir(self, index):
        '''bool QFileSystemModel.rmdir(QModelIndex index)'''
        return bool()
    def permissions(self, index):
        '''QFileDevice.Permissions QFileSystemModel.permissions(QModelIndex index)'''
        return QFileDevice.Permissions()
    def mkdir(self, parent, name):
        '''QModelIndex QFileSystemModel.mkdir(QModelIndex parent, str name)'''
        return QModelIndex()
    def lastModified(self, index):
        '''QDateTime QFileSystemModel.lastModified(QModelIndex index)'''
        return QDateTime()
    def type(self, index):
        '''str QFileSystemModel.type(QModelIndex index)'''
        return str()
    def size(self, index):
        '''int QFileSystemModel.size(QModelIndex index)'''
        return int()
    def isDir(self, index):
        '''bool QFileSystemModel.isDir(QModelIndex index)'''
        return bool()
    def filePath(self, index):
        '''str QFileSystemModel.filePath(QModelIndex index)'''
        return str()
    def nameFilters(self):
        '''list-of-str QFileSystemModel.nameFilters()'''
        return [str()]
    def setNameFilters(self, filters):
        '''void QFileSystemModel.setNameFilters(list-of-str filters)'''
    def nameFilterDisables(self):
        '''bool QFileSystemModel.nameFilterDisables()'''
        return bool()
    def setNameFilterDisables(self, enable):
        '''void QFileSystemModel.setNameFilterDisables(bool enable)'''
    def isReadOnly(self):
        '''bool QFileSystemModel.isReadOnly()'''
        return bool()
    def setReadOnly(self, enable):
        '''void QFileSystemModel.setReadOnly(bool enable)'''
    def resolveSymlinks(self):
        '''bool QFileSystemModel.resolveSymlinks()'''
        return bool()
    def setResolveSymlinks(self, enable):
        '''void QFileSystemModel.setResolveSymlinks(bool enable)'''
    def filter(self):
        '''QDir.Filters QFileSystemModel.filter()'''
        return QDir.Filters()
    def setFilter(self, filters):
        '''void QFileSystemModel.setFilter(QDir.Filters filters)'''
    def iconProvider(self):
        '''QFileIconProvider QFileSystemModel.iconProvider()'''
        return QFileIconProvider()
    def setIconProvider(self, provider):
        '''void QFileSystemModel.setIconProvider(QFileIconProvider provider)'''
    def rootDirectory(self):
        '''QDir QFileSystemModel.rootDirectory()'''
        return QDir()
    def rootPath(self):
        '''str QFileSystemModel.rootPath()'''
        return str()
    def setRootPath(self, path):
        '''QModelIndex QFileSystemModel.setRootPath(str path)'''
        return QModelIndex()
    def supportedDropActions(self):
        '''Qt.DropActions QFileSystemModel.supportedDropActions()'''
        return Qt.DropActions()
    def dropMimeData(self, data, action, row, column, parent):
        '''bool QFileSystemModel.dropMimeData(QMimeData data, Qt.DropAction action, int row, int column, QModelIndex parent)'''
        return bool()
    def mimeData(self, indexes):
        '''QMimeData QFileSystemModel.mimeData(list-of-QModelIndex indexes)'''
        return QMimeData()
    def mimeTypes(self):
        '''list-of-str QFileSystemModel.mimeTypes()'''
        return [str()]
    def sort(self, column, order = None):
        '''void QFileSystemModel.sort(int column, Qt.SortOrder order = Qt.AscendingOrder)'''
    def flags(self, index):
        '''Qt.ItemFlags QFileSystemModel.flags(QModelIndex index)'''
        return Qt.ItemFlags()
    def headerData(self, section, orientation, role = None):
        '''QVariant QFileSystemModel.headerData(int section, Qt.Orientation orientation, int role = Qt.DisplayRole)'''
        return QVariant()
    def setData(self, idx, value, role = None):
        '''bool QFileSystemModel.setData(QModelIndex idx, QVariant value, int role = Qt.EditRole)'''
        return bool()
    def data(self, index, role = None):
        '''QVariant QFileSystemModel.data(QModelIndex index, int role = Qt.DisplayRole)'''
        return QVariant()
    def myComputer(self, role = None):
        '''QVariant QFileSystemModel.myComputer(int role = Qt.DisplayRole)'''
        return QVariant()
    def columnCount(self, parent = QModelIndex()):
        '''int QFileSystemModel.columnCount(QModelIndex parent = QModelIndex())'''
        return int()
    def rowCount(self, parent = QModelIndex()):
        '''int QFileSystemModel.rowCount(QModelIndex parent = QModelIndex())'''
        return int()
    def fetchMore(self, parent):
        '''void QFileSystemModel.fetchMore(QModelIndex parent)'''
    def canFetchMore(self, parent):
        '''bool QFileSystemModel.canFetchMore(QModelIndex parent)'''
        return bool()
    def hasChildren(self, parent = QModelIndex()):
        '''bool QFileSystemModel.hasChildren(QModelIndex parent = QModelIndex())'''
        return bool()
    def parent(self, child):
        '''QModelIndex QFileSystemModel.parent(QModelIndex child)'''
        return QModelIndex()
    def index(self, row, column, parent = QModelIndex()):
        '''QModelIndex QFileSystemModel.index(int row, int column, QModelIndex parent = QModelIndex())'''
        return QModelIndex()
    def index(self, path, column = 0):
        '''QModelIndex QFileSystemModel.index(str path, int column = 0)'''
        return QModelIndex()


class QFocusFrame(QWidget):
    """"""
    def __init__(self, parent = None):
        '''void QFocusFrame.__init__(QWidget parent = None)'''
    def paintEvent(self):
        '''QPaintEvent QFocusFrame.paintEvent()'''
        return QPaintEvent()
    def event(self, e):
        '''bool QFocusFrame.event(QEvent e)'''
        return bool()
    def eventFilter(self):
        '''QEvent QFocusFrame.eventFilter()'''
        return QEvent()
    def initStyleOption(self, option):
        '''void QFocusFrame.initStyleOption(QStyleOption option)'''
    def widget(self):
        '''QWidget QFocusFrame.widget()'''
        return QWidget()
    def setWidget(self, widget):
        '''void QFocusFrame.setWidget(QWidget widget)'''


class QFontComboBox(QComboBox):
    """"""
    # Enum QFontComboBox.FontFilter
    AllFonts = 0
    ScalableFonts = 0
    NonScalableFonts = 0
    MonospacedFonts = 0
    ProportionalFonts = 0

    def __init__(self, parent = None):
        '''void QFontComboBox.__init__(QWidget parent = None)'''
    def event(self, e):
        '''bool QFontComboBox.event(QEvent e)'''
        return bool()
    currentFontChanged = pyqtSignal() # void currentFontChanged(const QFontamp;) - signal
    def setCurrentFont(self, f):
        '''void QFontComboBox.setCurrentFont(QFont f)'''
    def sizeHint(self):
        '''QSize QFontComboBox.sizeHint()'''
        return QSize()
    def currentFont(self):
        '''QFont QFontComboBox.currentFont()'''
        return QFont()
    def setFontFilters(self, filters):
        '''void QFontComboBox.setFontFilters(QFontComboBox.FontFilters filters)'''
    def writingSystem(self):
        '''QFontDatabase.WritingSystem QFontComboBox.writingSystem()'''
        return QFontDatabase.WritingSystem()
    def setWritingSystem(self):
        '''QFontDatabase.WritingSystem QFontComboBox.setWritingSystem()'''
        return QFontDatabase.WritingSystem()
    def fontFilters(self):
        '''QFontComboBox.FontFilters QFontComboBox.fontFilters()'''
        return QFontComboBox.FontFilters()
    class FontFilters():
        """"""
        def __init__(self):
            '''QFontComboBox.FontFilters QFontComboBox.FontFilters.__init__()'''
            return QFontComboBox.FontFilters()
        def __init__(self):
            '''int QFontComboBox.FontFilters.__init__()'''
            return int()
        def __init__(self):
            '''void QFontComboBox.FontFilters.__init__()'''
        def __bool__(self):
            '''int QFontComboBox.FontFilters.__bool__()'''
            return int()
        def __ne__(self, f):
            '''bool QFontComboBox.FontFilters.__ne__(QFontComboBox.FontFilters f)'''
            return bool()
        def __eq__(self, f):
            '''bool QFontComboBox.FontFilters.__eq__(QFontComboBox.FontFilters f)'''
            return bool()
        def __invert__(self):
            '''QFontComboBox.FontFilters QFontComboBox.FontFilters.__invert__()'''
            return QFontComboBox.FontFilters()
        def __and__(self, mask):
            '''QFontComboBox.FontFilters QFontComboBox.FontFilters.__and__(int mask)'''
            return QFontComboBox.FontFilters()
        def __xor__(self, f):
            '''QFontComboBox.FontFilters QFontComboBox.FontFilters.__xor__(QFontComboBox.FontFilters f)'''
            return QFontComboBox.FontFilters()
        def __xor__(self, f):
            '''QFontComboBox.FontFilters QFontComboBox.FontFilters.__xor__(int f)'''
            return QFontComboBox.FontFilters()
        def __or__(self, f):
            '''QFontComboBox.FontFilters QFontComboBox.FontFilters.__or__(QFontComboBox.FontFilters f)'''
            return QFontComboBox.FontFilters()
        def __or__(self, f):
            '''QFontComboBox.FontFilters QFontComboBox.FontFilters.__or__(int f)'''
            return QFontComboBox.FontFilters()
        def __int__(self):
            '''int QFontComboBox.FontFilters.__int__()'''
            return int()
        def __ixor__(self, f):
            '''QFontComboBox.FontFilters QFontComboBox.FontFilters.__ixor__(QFontComboBox.FontFilters f)'''
            return QFontComboBox.FontFilters()
        def __ior__(self, f):
            '''QFontComboBox.FontFilters QFontComboBox.FontFilters.__ior__(QFontComboBox.FontFilters f)'''
            return QFontComboBox.FontFilters()
        def __iand__(self, mask):
            '''QFontComboBox.FontFilters QFontComboBox.FontFilters.__iand__(int mask)'''
            return QFontComboBox.FontFilters()


class QFontDialog(QDialog):
    """"""
    # Enum QFontDialog.FontDialogOption
    NoButtons = 0
    DontUseNativeDialog = 0
    ScalableFonts = 0
    NonScalableFonts = 0
    MonospacedFonts = 0
    ProportionalFonts = 0

    def __init__(self, parent = None):
        '''void QFontDialog.__init__(QWidget parent = None)'''
    def __init__(self, initial, parent = None):
        '''void QFontDialog.__init__(QFont initial, QWidget parent = None)'''
    fontSelected = pyqtSignal() # void fontSelected(const QFontamp;) - signal
    currentFontChanged = pyqtSignal() # void currentFontChanged(const QFontamp;) - signal
    def setVisible(self, visible):
        '''void QFontDialog.setVisible(bool visible)'''
    def open(self):
        '''void QFontDialog.open()'''
    def open(self, slot):
        '''void QFontDialog.open(slot slot)'''
    def options(self):
        '''QFontDialog.FontDialogOptions QFontDialog.options()'''
        return QFontDialog.FontDialogOptions()
    def setOptions(self, options):
        '''void QFontDialog.setOptions(QFontDialog.FontDialogOptions options)'''
    def testOption(self, option):
        '''bool QFontDialog.testOption(QFontDialog.FontDialogOption option)'''
        return bool()
    def setOption(self, option, on = True):
        '''void QFontDialog.setOption(QFontDialog.FontDialogOption option, bool on = True)'''
    def selectedFont(self):
        '''QFont QFontDialog.selectedFont()'''
        return QFont()
    def currentFont(self):
        '''QFont QFontDialog.currentFont()'''
        return QFont()
    def setCurrentFont(self, font):
        '''void QFontDialog.setCurrentFont(QFont font)'''
    def eventFilter(self, object, event):
        '''bool QFontDialog.eventFilter(QObject object, QEvent event)'''
        return bool()
    def done(self, result):
        '''void QFontDialog.done(int result)'''
    def changeEvent(self, e):
        '''void QFontDialog.changeEvent(QEvent e)'''
    def getFont(self, ok, initial, parent = None, caption = str(), options = 0):
        '''static QFont QFontDialog.getFont(bool ok, QFont initial, QWidget parent = None, str caption = str(), QFontDialog.FontDialogOptions options = 0)'''
        return QFont()
    def getFont(self, ok, parent = None):
        '''static QFont QFontDialog.getFont(bool ok, QWidget parent = None)'''
        return QFont()
    class FontDialogOptions():
        """"""
        def __init__(self):
            '''QFontDialog.FontDialogOptions QFontDialog.FontDialogOptions.__init__()'''
            return QFontDialog.FontDialogOptions()
        def __init__(self):
            '''int QFontDialog.FontDialogOptions.__init__()'''
            return int()
        def __init__(self):
            '''void QFontDialog.FontDialogOptions.__init__()'''
        def __bool__(self):
            '''int QFontDialog.FontDialogOptions.__bool__()'''
            return int()
        def __ne__(self, f):
            '''bool QFontDialog.FontDialogOptions.__ne__(QFontDialog.FontDialogOptions f)'''
            return bool()
        def __eq__(self, f):
            '''bool QFontDialog.FontDialogOptions.__eq__(QFontDialog.FontDialogOptions f)'''
            return bool()
        def __invert__(self):
            '''QFontDialog.FontDialogOptions QFontDialog.FontDialogOptions.__invert__()'''
            return QFontDialog.FontDialogOptions()
        def __and__(self, mask):
            '''QFontDialog.FontDialogOptions QFontDialog.FontDialogOptions.__and__(int mask)'''
            return QFontDialog.FontDialogOptions()
        def __xor__(self, f):
            '''QFontDialog.FontDialogOptions QFontDialog.FontDialogOptions.__xor__(QFontDialog.FontDialogOptions f)'''
            return QFontDialog.FontDialogOptions()
        def __xor__(self, f):
            '''QFontDialog.FontDialogOptions QFontDialog.FontDialogOptions.__xor__(int f)'''
            return QFontDialog.FontDialogOptions()
        def __or__(self, f):
            '''QFontDialog.FontDialogOptions QFontDialog.FontDialogOptions.__or__(QFontDialog.FontDialogOptions f)'''
            return QFontDialog.FontDialogOptions()
        def __or__(self, f):
            '''QFontDialog.FontDialogOptions QFontDialog.FontDialogOptions.__or__(int f)'''
            return QFontDialog.FontDialogOptions()
        def __int__(self):
            '''int QFontDialog.FontDialogOptions.__int__()'''
            return int()
        def __ixor__(self, f):
            '''QFontDialog.FontDialogOptions QFontDialog.FontDialogOptions.__ixor__(QFontDialog.FontDialogOptions f)'''
            return QFontDialog.FontDialogOptions()
        def __ior__(self, f):
            '''QFontDialog.FontDialogOptions QFontDialog.FontDialogOptions.__ior__(QFontDialog.FontDialogOptions f)'''
            return QFontDialog.FontDialogOptions()
        def __iand__(self, mask):
            '''QFontDialog.FontDialogOptions QFontDialog.FontDialogOptions.__iand__(int mask)'''
            return QFontDialog.FontDialogOptions()


class QFormLayout(QLayout):
    """"""
    # Enum QFormLayout.ItemRole
    LabelRole = 0
    FieldRole = 0
    SpanningRole = 0

    # Enum QFormLayout.RowWrapPolicy
    DontWrapRows = 0
    WrapLongRows = 0
    WrapAllRows = 0

    # Enum QFormLayout.FieldGrowthPolicy
    FieldsStayAtSizeHint = 0
    ExpandingFieldsGrow = 0
    AllNonFixedFieldsGrow = 0

    def __init__(self, parent = None):
        '''void QFormLayout.__init__(QWidget parent = None)'''
    def rowCount(self):
        '''int QFormLayout.rowCount()'''
        return int()
    def count(self):
        '''int QFormLayout.count()'''
        return int()
    def expandingDirections(self):
        '''Qt.Orientations QFormLayout.expandingDirections()'''
        return Qt.Orientations()
    def heightForWidth(self, width):
        '''int QFormLayout.heightForWidth(int width)'''
        return int()
    def hasHeightForWidth(self):
        '''bool QFormLayout.hasHeightForWidth()'''
        return bool()
    def invalidate(self):
        '''void QFormLayout.invalidate()'''
    def sizeHint(self):
        '''QSize QFormLayout.sizeHint()'''
        return QSize()
    def minimumSize(self):
        '''QSize QFormLayout.minimumSize()'''
        return QSize()
    def setGeometry(self, rect):
        '''void QFormLayout.setGeometry(QRect rect)'''
    def takeAt(self, index):
        '''QLayoutItem QFormLayout.takeAt(int index)'''
        return QLayoutItem()
    def addItem(self, item):
        '''void QFormLayout.addItem(QLayoutItem item)'''
    def labelForField(self, field):
        '''QWidget QFormLayout.labelForField(QWidget field)'''
        return QWidget()
    def labelForField(self, field):
        '''QWidget QFormLayout.labelForField(QLayout field)'''
        return QWidget()
    def getLayoutPosition(self, layout, rowPtr, rolePtr):
        '''void QFormLayout.getLayoutPosition(QLayout layout, int rowPtr, QFormLayout.ItemRole rolePtr)'''
    def getWidgetPosition(self, widget, rowPtr, rolePtr):
        '''void QFormLayout.getWidgetPosition(QWidget widget, int rowPtr, QFormLayout.ItemRole rolePtr)'''
    def getItemPosition(self, index, rowPtr, rolePtr):
        '''void QFormLayout.getItemPosition(int index, int rowPtr, QFormLayout.ItemRole rolePtr)'''
    def itemAt(self, row, role):
        '''QLayoutItem QFormLayout.itemAt(int row, QFormLayout.ItemRole role)'''
        return QLayoutItem()
    def itemAt(self, index):
        '''QLayoutItem QFormLayout.itemAt(int index)'''
        return QLayoutItem()
    def setLayout(self, row, role, layout):
        '''void QFormLayout.setLayout(int row, QFormLayout.ItemRole role, QLayout layout)'''
    def setWidget(self, row, role, widget):
        '''void QFormLayout.setWidget(int row, QFormLayout.ItemRole role, QWidget widget)'''
    def setItem(self, row, role, item):
        '''void QFormLayout.setItem(int row, QFormLayout.ItemRole role, QLayoutItem item)'''
    def insertRow(self, row, label, field):
        '''void QFormLayout.insertRow(int row, QWidget label, QWidget field)'''
    def insertRow(self, row, label, field):
        '''void QFormLayout.insertRow(int row, QWidget label, QLayout field)'''
    def insertRow(self, row, labelText, field):
        '''void QFormLayout.insertRow(int row, str labelText, QWidget field)'''
    def insertRow(self, row, labelText, field):
        '''void QFormLayout.insertRow(int row, str labelText, QLayout field)'''
    def insertRow(self, row, widget):
        '''void QFormLayout.insertRow(int row, QWidget widget)'''
    def insertRow(self, row, layout):
        '''void QFormLayout.insertRow(int row, QLayout layout)'''
    def addRow(self, label, field):
        '''void QFormLayout.addRow(QWidget label, QWidget field)'''
    def addRow(self, label, field):
        '''void QFormLayout.addRow(QWidget label, QLayout field)'''
    def addRow(self, labelText, field):
        '''void QFormLayout.addRow(str labelText, QWidget field)'''
    def addRow(self, labelText, field):
        '''void QFormLayout.addRow(str labelText, QLayout field)'''
    def addRow(self, widget):
        '''void QFormLayout.addRow(QWidget widget)'''
    def addRow(self, layout):
        '''void QFormLayout.addRow(QLayout layout)'''
    def setSpacing(self):
        '''int QFormLayout.setSpacing()'''
        return int()
    def spacing(self):
        '''int QFormLayout.spacing()'''
        return int()
    def verticalSpacing(self):
        '''int QFormLayout.verticalSpacing()'''
        return int()
    def setVerticalSpacing(self, spacing):
        '''void QFormLayout.setVerticalSpacing(int spacing)'''
    def horizontalSpacing(self):
        '''int QFormLayout.horizontalSpacing()'''
        return int()
    def setHorizontalSpacing(self, spacing):
        '''void QFormLayout.setHorizontalSpacing(int spacing)'''
    def formAlignment(self):
        '''Qt.Alignment QFormLayout.formAlignment()'''
        return Qt.Alignment()
    def setFormAlignment(self, alignment):
        '''void QFormLayout.setFormAlignment(Qt.Alignment alignment)'''
    def labelAlignment(self):
        '''Qt.Alignment QFormLayout.labelAlignment()'''
        return Qt.Alignment()
    def setLabelAlignment(self, alignment):
        '''void QFormLayout.setLabelAlignment(Qt.Alignment alignment)'''
    def rowWrapPolicy(self):
        '''QFormLayout.RowWrapPolicy QFormLayout.rowWrapPolicy()'''
        return QFormLayout.RowWrapPolicy()
    def setRowWrapPolicy(self, policy):
        '''void QFormLayout.setRowWrapPolicy(QFormLayout.RowWrapPolicy policy)'''
    def fieldGrowthPolicy(self):
        '''QFormLayout.FieldGrowthPolicy QFormLayout.fieldGrowthPolicy()'''
        return QFormLayout.FieldGrowthPolicy()
    def setFieldGrowthPolicy(self, policy):
        '''void QFormLayout.setFieldGrowthPolicy(QFormLayout.FieldGrowthPolicy policy)'''


class QGesture(QObject):
    """"""
    # Enum QGesture.GestureCancelPolicy
    CancelNone = 0
    CancelAllInContext = 0

    def __init__(self, parent = None):
        '''void QGesture.__init__(QObject parent = None)'''
    def gestureCancelPolicy(self):
        '''QGesture.GestureCancelPolicy QGesture.gestureCancelPolicy()'''
        return QGesture.GestureCancelPolicy()
    def setGestureCancelPolicy(self, policy):
        '''void QGesture.setGestureCancelPolicy(QGesture.GestureCancelPolicy policy)'''
    def unsetHotSpot(self):
        '''void QGesture.unsetHotSpot()'''
    def hasHotSpot(self):
        '''bool QGesture.hasHotSpot()'''
        return bool()
    def setHotSpot(self, value):
        '''void QGesture.setHotSpot(QPointF value)'''
    def hotSpot(self):
        '''QPointF QGesture.hotSpot()'''
        return QPointF()
    def state(self):
        '''Qt.GestureState QGesture.state()'''
        return Qt.GestureState()
    def gestureType(self):
        '''Qt.GestureType QGesture.gestureType()'''
        return Qt.GestureType()


class QPanGesture(QGesture):
    """"""
    def __init__(self, parent = None):
        '''void QPanGesture.__init__(QObject parent = None)'''
    def setAcceleration(self, value):
        '''void QPanGesture.setAcceleration(float value)'''
    def setOffset(self, value):
        '''void QPanGesture.setOffset(QPointF value)'''
    def setLastOffset(self, value):
        '''void QPanGesture.setLastOffset(QPointF value)'''
    def acceleration(self):
        '''float QPanGesture.acceleration()'''
        return float()
    def delta(self):
        '''QPointF QPanGesture.delta()'''
        return QPointF()
    def offset(self):
        '''QPointF QPanGesture.offset()'''
        return QPointF()
    def lastOffset(self):
        '''QPointF QPanGesture.lastOffset()'''
        return QPointF()


class QPinchGesture(QGesture):
    """"""
    # Enum QPinchGesture.ChangeFlag
    ScaleFactorChanged = 0
    RotationAngleChanged = 0
    CenterPointChanged = 0

    def __init__(self, parent = None):
        '''void QPinchGesture.__init__(QObject parent = None)'''
    def setRotationAngle(self, value):
        '''void QPinchGesture.setRotationAngle(float value)'''
    def setLastRotationAngle(self, value):
        '''void QPinchGesture.setLastRotationAngle(float value)'''
    def setTotalRotationAngle(self, value):
        '''void QPinchGesture.setTotalRotationAngle(float value)'''
    def rotationAngle(self):
        '''float QPinchGesture.rotationAngle()'''
        return float()
    def lastRotationAngle(self):
        '''float QPinchGesture.lastRotationAngle()'''
        return float()
    def totalRotationAngle(self):
        '''float QPinchGesture.totalRotationAngle()'''
        return float()
    def setScaleFactor(self, value):
        '''void QPinchGesture.setScaleFactor(float value)'''
    def setLastScaleFactor(self, value):
        '''void QPinchGesture.setLastScaleFactor(float value)'''
    def setTotalScaleFactor(self, value):
        '''void QPinchGesture.setTotalScaleFactor(float value)'''
    def scaleFactor(self):
        '''float QPinchGesture.scaleFactor()'''
        return float()
    def lastScaleFactor(self):
        '''float QPinchGesture.lastScaleFactor()'''
        return float()
    def totalScaleFactor(self):
        '''float QPinchGesture.totalScaleFactor()'''
        return float()
    def setCenterPoint(self, value):
        '''void QPinchGesture.setCenterPoint(QPointF value)'''
    def setLastCenterPoint(self, value):
        '''void QPinchGesture.setLastCenterPoint(QPointF value)'''
    def setStartCenterPoint(self, value):
        '''void QPinchGesture.setStartCenterPoint(QPointF value)'''
    def centerPoint(self):
        '''QPointF QPinchGesture.centerPoint()'''
        return QPointF()
    def lastCenterPoint(self):
        '''QPointF QPinchGesture.lastCenterPoint()'''
        return QPointF()
    def startCenterPoint(self):
        '''QPointF QPinchGesture.startCenterPoint()'''
        return QPointF()
    def setChangeFlags(self, value):
        '''void QPinchGesture.setChangeFlags(QPinchGesture.ChangeFlags value)'''
    def changeFlags(self):
        '''QPinchGesture.ChangeFlags QPinchGesture.changeFlags()'''
        return QPinchGesture.ChangeFlags()
    def setTotalChangeFlags(self, value):
        '''void QPinchGesture.setTotalChangeFlags(QPinchGesture.ChangeFlags value)'''
    def totalChangeFlags(self):
        '''QPinchGesture.ChangeFlags QPinchGesture.totalChangeFlags()'''
        return QPinchGesture.ChangeFlags()
    class ChangeFlags():
        """"""
        def __init__(self):
            '''QPinchGesture.ChangeFlags QPinchGesture.ChangeFlags.__init__()'''
            return QPinchGesture.ChangeFlags()
        def __init__(self):
            '''int QPinchGesture.ChangeFlags.__init__()'''
            return int()
        def __init__(self):
            '''void QPinchGesture.ChangeFlags.__init__()'''
        def __bool__(self):
            '''int QPinchGesture.ChangeFlags.__bool__()'''
            return int()
        def __ne__(self, f):
            '''bool QPinchGesture.ChangeFlags.__ne__(QPinchGesture.ChangeFlags f)'''
            return bool()
        def __eq__(self, f):
            '''bool QPinchGesture.ChangeFlags.__eq__(QPinchGesture.ChangeFlags f)'''
            return bool()
        def __invert__(self):
            '''QPinchGesture.ChangeFlags QPinchGesture.ChangeFlags.__invert__()'''
            return QPinchGesture.ChangeFlags()
        def __and__(self, mask):
            '''QPinchGesture.ChangeFlags QPinchGesture.ChangeFlags.__and__(int mask)'''
            return QPinchGesture.ChangeFlags()
        def __xor__(self, f):
            '''QPinchGesture.ChangeFlags QPinchGesture.ChangeFlags.__xor__(QPinchGesture.ChangeFlags f)'''
            return QPinchGesture.ChangeFlags()
        def __xor__(self, f):
            '''QPinchGesture.ChangeFlags QPinchGesture.ChangeFlags.__xor__(int f)'''
            return QPinchGesture.ChangeFlags()
        def __or__(self, f):
            '''QPinchGesture.ChangeFlags QPinchGesture.ChangeFlags.__or__(QPinchGesture.ChangeFlags f)'''
            return QPinchGesture.ChangeFlags()
        def __or__(self, f):
            '''QPinchGesture.ChangeFlags QPinchGesture.ChangeFlags.__or__(int f)'''
            return QPinchGesture.ChangeFlags()
        def __int__(self):
            '''int QPinchGesture.ChangeFlags.__int__()'''
            return int()
        def __ixor__(self, f):
            '''QPinchGesture.ChangeFlags QPinchGesture.ChangeFlags.__ixor__(QPinchGesture.ChangeFlags f)'''
            return QPinchGesture.ChangeFlags()
        def __ior__(self, f):
            '''QPinchGesture.ChangeFlags QPinchGesture.ChangeFlags.__ior__(QPinchGesture.ChangeFlags f)'''
            return QPinchGesture.ChangeFlags()
        def __iand__(self, mask):
            '''QPinchGesture.ChangeFlags QPinchGesture.ChangeFlags.__iand__(int mask)'''
            return QPinchGesture.ChangeFlags()


class QSwipeGesture(QGesture):
    """"""
    # Enum QSwipeGesture.SwipeDirection
    NoDirection = 0
    Left = 0
    Right = 0
    Up = 0
    Down = 0

    def __init__(self, parent = None):
        '''void QSwipeGesture.__init__(QObject parent = None)'''
    def setSwipeAngle(self, value):
        '''void QSwipeGesture.setSwipeAngle(float value)'''
    def swipeAngle(self):
        '''float QSwipeGesture.swipeAngle()'''
        return float()
    def verticalDirection(self):
        '''QSwipeGesture.SwipeDirection QSwipeGesture.verticalDirection()'''
        return QSwipeGesture.SwipeDirection()
    def horizontalDirection(self):
        '''QSwipeGesture.SwipeDirection QSwipeGesture.horizontalDirection()'''
        return QSwipeGesture.SwipeDirection()


class QTapGesture(QGesture):
    """"""
    def __init__(self, parent = None):
        '''void QTapGesture.__init__(QObject parent = None)'''
    def setPosition(self, pos):
        '''void QTapGesture.setPosition(QPointF pos)'''
    def position(self):
        '''QPointF QTapGesture.position()'''
        return QPointF()


class QTapAndHoldGesture(QGesture):
    """"""
    def __init__(self, parent = None):
        '''void QTapAndHoldGesture.__init__(QObject parent = None)'''
    def timeout(self):
        '''static int QTapAndHoldGesture.timeout()'''
        return int()
    def setTimeout(self, msecs):
        '''static void QTapAndHoldGesture.setTimeout(int msecs)'''
    def setPosition(self, pos):
        '''void QTapAndHoldGesture.setPosition(QPointF pos)'''
    def position(self):
        '''QPointF QTapAndHoldGesture.position()'''
        return QPointF()


class QGestureEvent(QEvent):
    """"""
    def __init__(self, gestures):
        '''void QGestureEvent.__init__(list-of-QGesture gestures)'''
    def __init__(self):
        '''QGestureEvent QGestureEvent.__init__()'''
        return QGestureEvent()
    def mapToGraphicsScene(self, gesturePoint):
        '''QPointF QGestureEvent.mapToGraphicsScene(QPointF gesturePoint)'''
        return QPointF()
    def widget(self):
        '''QWidget QGestureEvent.widget()'''
        return QWidget()
    def ignore(self):
        '''void QGestureEvent.ignore()'''
    def ignore(self):
        '''QGesture QGestureEvent.ignore()'''
        return QGesture()
    def ignore(self):
        '''Qt.GestureType QGestureEvent.ignore()'''
        return Qt.GestureType()
    def accept(self):
        '''void QGestureEvent.accept()'''
    def accept(self):
        '''QGesture QGestureEvent.accept()'''
        return QGesture()
    def accept(self):
        '''Qt.GestureType QGestureEvent.accept()'''
        return Qt.GestureType()
    def isAccepted(self):
        '''bool QGestureEvent.isAccepted()'''
        return bool()
    def isAccepted(self):
        '''QGesture QGestureEvent.isAccepted()'''
        return QGesture()
    def isAccepted(self):
        '''Qt.GestureType QGestureEvent.isAccepted()'''
        return Qt.GestureType()
    def setAccepted(self, accepted):
        '''void QGestureEvent.setAccepted(bool accepted)'''
    def setAccepted(self):
        '''bool QGestureEvent.setAccepted()'''
        return bool()
    def setAccepted(self):
        '''bool QGestureEvent.setAccepted()'''
        return bool()
    def canceledGestures(self):
        '''list-of-QGesture QGestureEvent.canceledGestures()'''
        return [QGesture()]
    def activeGestures(self):
        '''list-of-QGesture QGestureEvent.activeGestures()'''
        return [QGesture()]
    def gesture(self, type):
        '''QGesture QGestureEvent.gesture(Qt.GestureType type)'''
        return QGesture()
    def gestures(self):
        '''list-of-QGesture QGestureEvent.gestures()'''
        return [QGesture()]


class QGestureRecognizer():
    """"""
    # Enum QGestureRecognizer.ResultFlag
    Ignore = 0
    MayBeGesture = 0
    TriggerGesture = 0
    FinishGesture = 0
    CancelGesture = 0
    ConsumeEventHint = 0

    def __init__(self):
        '''void QGestureRecognizer.__init__()'''
    def __init__(self):
        '''QGestureRecognizer QGestureRecognizer.__init__()'''
        return QGestureRecognizer()
    def unregisterRecognizer(self, type):
        '''static void QGestureRecognizer.unregisterRecognizer(Qt.GestureType type)'''
    def registerRecognizer(self, recognizer):
        '''static Qt.GestureType QGestureRecognizer.registerRecognizer(QGestureRecognizer recognizer)'''
        return Qt.GestureType()
    def reset(self, state):
        '''void QGestureRecognizer.reset(QGesture state)'''
    def recognize(self, state, watched, event):
        '''abstract QGestureRecognizer.Result QGestureRecognizer.recognize(QGesture state, QObject watched, QEvent event)'''
        return QGestureRecognizer.Result()
    def create(self, target):
        '''QGesture QGestureRecognizer.create(QObject target)'''
        return QGesture()
    class Result():
        """"""
        def __init__(self):
            '''QGestureRecognizer.Result QGestureRecognizer.Result.__init__()'''
            return QGestureRecognizer.Result()
        def __init__(self):
            '''int QGestureRecognizer.Result.__init__()'''
            return int()
        def __init__(self):
            '''void QGestureRecognizer.Result.__init__()'''
        def __bool__(self):
            '''int QGestureRecognizer.Result.__bool__()'''
            return int()
        def __ne__(self, f):
            '''bool QGestureRecognizer.Result.__ne__(QGestureRecognizer.Result f)'''
            return bool()
        def __eq__(self, f):
            '''bool QGestureRecognizer.Result.__eq__(QGestureRecognizer.Result f)'''
            return bool()
        def __invert__(self):
            '''QGestureRecognizer.Result QGestureRecognizer.Result.__invert__()'''
            return QGestureRecognizer.Result()
        def __and__(self, mask):
            '''QGestureRecognizer.Result QGestureRecognizer.Result.__and__(int mask)'''
            return QGestureRecognizer.Result()
        def __xor__(self, f):
            '''QGestureRecognizer.Result QGestureRecognizer.Result.__xor__(QGestureRecognizer.Result f)'''
            return QGestureRecognizer.Result()
        def __xor__(self, f):
            '''QGestureRecognizer.Result QGestureRecognizer.Result.__xor__(int f)'''
            return QGestureRecognizer.Result()
        def __or__(self, f):
            '''QGestureRecognizer.Result QGestureRecognizer.Result.__or__(QGestureRecognizer.Result f)'''
            return QGestureRecognizer.Result()
        def __or__(self, f):
            '''QGestureRecognizer.Result QGestureRecognizer.Result.__or__(int f)'''
            return QGestureRecognizer.Result()
        def __int__(self):
            '''int QGestureRecognizer.Result.__int__()'''
            return int()
        def __ixor__(self, f):
            '''QGestureRecognizer.Result QGestureRecognizer.Result.__ixor__(QGestureRecognizer.Result f)'''
            return QGestureRecognizer.Result()
        def __ior__(self, f):
            '''QGestureRecognizer.Result QGestureRecognizer.Result.__ior__(QGestureRecognizer.Result f)'''
            return QGestureRecognizer.Result()
        def __iand__(self, mask):
            '''QGestureRecognizer.Result QGestureRecognizer.Result.__iand__(int mask)'''
            return QGestureRecognizer.Result()


class QGraphicsAnchor(QObject):
    """"""
    def sizePolicy(self):
        '''QSizePolicy.Policy QGraphicsAnchor.sizePolicy()'''
        return QSizePolicy.Policy()
    def setSizePolicy(self, policy):
        '''void QGraphicsAnchor.setSizePolicy(QSizePolicy.Policy policy)'''
    def spacing(self):
        '''float QGraphicsAnchor.spacing()'''
        return float()
    def unsetSpacing(self):
        '''void QGraphicsAnchor.unsetSpacing()'''
    def setSpacing(self, spacing):
        '''void QGraphicsAnchor.setSpacing(float spacing)'''


class QGraphicsLayoutItem():
    """"""
    def __init__(self, parent = None, isLayout = False):
        '''void QGraphicsLayoutItem.__init__(QGraphicsLayoutItem parent = None, bool isLayout = False)'''
    def setOwnedByLayout(self, ownedByLayout):
        '''void QGraphicsLayoutItem.setOwnedByLayout(bool ownedByLayout)'''
    def setGraphicsItem(self, item):
        '''void QGraphicsLayoutItem.setGraphicsItem(QGraphicsItem item)'''
    def sizeHint(self, which, constraint = QSizeF()):
        '''abstract QSizeF QGraphicsLayoutItem.sizeHint(Qt.SizeHint which, QSizeF constraint = QSizeF())'''
        return QSizeF()
    def ownedByLayout(self):
        '''bool QGraphicsLayoutItem.ownedByLayout()'''
        return bool()
    def graphicsItem(self):
        '''QGraphicsItem QGraphicsLayoutItem.graphicsItem()'''
        return QGraphicsItem()
    def maximumHeight(self):
        '''float QGraphicsLayoutItem.maximumHeight()'''
        return float()
    def maximumWidth(self):
        '''float QGraphicsLayoutItem.maximumWidth()'''
        return float()
    def preferredHeight(self):
        '''float QGraphicsLayoutItem.preferredHeight()'''
        return float()
    def preferredWidth(self):
        '''float QGraphicsLayoutItem.preferredWidth()'''
        return float()
    def minimumHeight(self):
        '''float QGraphicsLayoutItem.minimumHeight()'''
        return float()
    def minimumWidth(self):
        '''float QGraphicsLayoutItem.minimumWidth()'''
        return float()
    def isLayout(self):
        '''bool QGraphicsLayoutItem.isLayout()'''
        return bool()
    def setParentLayoutItem(self, parent):
        '''void QGraphicsLayoutItem.setParentLayoutItem(QGraphicsLayoutItem parent)'''
    def parentLayoutItem(self):
        '''QGraphicsLayoutItem QGraphicsLayoutItem.parentLayoutItem()'''
        return QGraphicsLayoutItem()
    def updateGeometry(self):
        '''void QGraphicsLayoutItem.updateGeometry()'''
    def effectiveSizeHint(self, which, constraint = QSizeF()):
        '''QSizeF QGraphicsLayoutItem.effectiveSizeHint(Qt.SizeHint which, QSizeF constraint = QSizeF())'''
        return QSizeF()
    def contentsRect(self):
        '''QRectF QGraphicsLayoutItem.contentsRect()'''
        return QRectF()
    def getContentsMargins(self, left, top, right, bottom):
        '''void QGraphicsLayoutItem.getContentsMargins(float left, float top, float right, float bottom)'''
    def geometry(self):
        '''QRectF QGraphicsLayoutItem.geometry()'''
        return QRectF()
    def setGeometry(self, rect):
        '''void QGraphicsLayoutItem.setGeometry(QRectF rect)'''
    def setMaximumHeight(self, height):
        '''void QGraphicsLayoutItem.setMaximumHeight(float height)'''
    def setMaximumWidth(self, width):
        '''void QGraphicsLayoutItem.setMaximumWidth(float width)'''
    def maximumSize(self):
        '''QSizeF QGraphicsLayoutItem.maximumSize()'''
        return QSizeF()
    def setMaximumSize(self, size):
        '''void QGraphicsLayoutItem.setMaximumSize(QSizeF size)'''
    def setMaximumSize(self, aw, ah):
        '''void QGraphicsLayoutItem.setMaximumSize(float aw, float ah)'''
    def setPreferredHeight(self, height):
        '''void QGraphicsLayoutItem.setPreferredHeight(float height)'''
    def setPreferredWidth(self, width):
        '''void QGraphicsLayoutItem.setPreferredWidth(float width)'''
    def preferredSize(self):
        '''QSizeF QGraphicsLayoutItem.preferredSize()'''
        return QSizeF()
    def setPreferredSize(self, size):
        '''void QGraphicsLayoutItem.setPreferredSize(QSizeF size)'''
    def setPreferredSize(self, aw, ah):
        '''void QGraphicsLayoutItem.setPreferredSize(float aw, float ah)'''
    def setMinimumHeight(self, height):
        '''void QGraphicsLayoutItem.setMinimumHeight(float height)'''
    def setMinimumWidth(self, width):
        '''void QGraphicsLayoutItem.setMinimumWidth(float width)'''
    def minimumSize(self):
        '''QSizeF QGraphicsLayoutItem.minimumSize()'''
        return QSizeF()
    def setMinimumSize(self, size):
        '''void QGraphicsLayoutItem.setMinimumSize(QSizeF size)'''
    def setMinimumSize(self, aw, ah):
        '''void QGraphicsLayoutItem.setMinimumSize(float aw, float ah)'''
    def sizePolicy(self):
        '''QSizePolicy QGraphicsLayoutItem.sizePolicy()'''
        return QSizePolicy()
    def setSizePolicy(self, policy):
        '''void QGraphicsLayoutItem.setSizePolicy(QSizePolicy policy)'''
    def setSizePolicy(self, hPolicy, vPolicy, controlType = None):
        '''void QGraphicsLayoutItem.setSizePolicy(QSizePolicy.Policy hPolicy, QSizePolicy.Policy vPolicy, QSizePolicy.ControlType controlType = QSizePolicy.DefaultType)'''


class QGraphicsLayout(QGraphicsLayoutItem):
    """"""
    def __init__(self, parent = None):
        '''void QGraphicsLayout.__init__(QGraphicsLayoutItem parent = None)'''
    def addChildLayoutItem(self, layoutItem):
        '''void QGraphicsLayout.addChildLayoutItem(QGraphicsLayoutItem layoutItem)'''
    def updateGeometry(self):
        '''void QGraphicsLayout.updateGeometry()'''
    def removeAt(self, index):
        '''abstract void QGraphicsLayout.removeAt(int index)'''
    def itemAt(self, i):
        '''abstract QGraphicsLayoutItem QGraphicsLayout.itemAt(int i)'''
        return QGraphicsLayoutItem()
    def __len__(self):
        ''' QGraphicsLayout.__len__()'''
        return ()
    def count(self):
        '''abstract int QGraphicsLayout.count()'''
        return int()
    def widgetEvent(self, e):
        '''void QGraphicsLayout.widgetEvent(QEvent e)'''
    def invalidate(self):
        '''void QGraphicsLayout.invalidate()'''
    def isActivated(self):
        '''bool QGraphicsLayout.isActivated()'''
        return bool()
    def activate(self):
        '''void QGraphicsLayout.activate()'''
    def getContentsMargins(self, left, top, right, bottom):
        '''void QGraphicsLayout.getContentsMargins(float left, float top, float right, float bottom)'''
    def setContentsMargins(self, left, top, right, bottom):
        '''void QGraphicsLayout.setContentsMargins(float left, float top, float right, float bottom)'''


class QGraphicsAnchorLayout(QGraphicsLayout):
    """"""
    def __init__(self, parent = None):
        '''void QGraphicsAnchorLayout.__init__(QGraphicsLayoutItem parent = None)'''
    def sizeHint(self, which, constraint = QSizeF()):
        '''QSizeF QGraphicsAnchorLayout.sizeHint(Qt.SizeHint which, QSizeF constraint = QSizeF())'''
        return QSizeF()
    def invalidate(self):
        '''void QGraphicsAnchorLayout.invalidate()'''
    def itemAt(self, index):
        '''QGraphicsLayoutItem QGraphicsAnchorLayout.itemAt(int index)'''
        return QGraphicsLayoutItem()
    def count(self):
        '''int QGraphicsAnchorLayout.count()'''
        return int()
    def setGeometry(self, rect):
        '''void QGraphicsAnchorLayout.setGeometry(QRectF rect)'''
    def removeAt(self, index):
        '''void QGraphicsAnchorLayout.removeAt(int index)'''
    def verticalSpacing(self):
        '''float QGraphicsAnchorLayout.verticalSpacing()'''
        return float()
    def horizontalSpacing(self):
        '''float QGraphicsAnchorLayout.horizontalSpacing()'''
        return float()
    def setSpacing(self, spacing):
        '''void QGraphicsAnchorLayout.setSpacing(float spacing)'''
    def setVerticalSpacing(self, spacing):
        '''void QGraphicsAnchorLayout.setVerticalSpacing(float spacing)'''
    def setHorizontalSpacing(self, spacing):
        '''void QGraphicsAnchorLayout.setHorizontalSpacing(float spacing)'''
    def addAnchors(self, firstItem, secondItem, orientations = None):
        '''void QGraphicsAnchorLayout.addAnchors(QGraphicsLayoutItem firstItem, QGraphicsLayoutItem secondItem, Qt.Orientations orientations = Qt.Horizontal|Qt.Vertical)'''
    def addCornerAnchors(self, firstItem, firstCorner, secondItem, secondCorner):
        '''void QGraphicsAnchorLayout.addCornerAnchors(QGraphicsLayoutItem firstItem, Qt.Corner firstCorner, QGraphicsLayoutItem secondItem, Qt.Corner secondCorner)'''
    def anchor(self, firstItem, firstEdge, secondItem, secondEdge):
        '''QGraphicsAnchor QGraphicsAnchorLayout.anchor(QGraphicsLayoutItem firstItem, Qt.AnchorPoint firstEdge, QGraphicsLayoutItem secondItem, Qt.AnchorPoint secondEdge)'''
        return QGraphicsAnchor()
    def addAnchor(self, firstItem, firstEdge, secondItem, secondEdge):
        '''QGraphicsAnchor QGraphicsAnchorLayout.addAnchor(QGraphicsLayoutItem firstItem, Qt.AnchorPoint firstEdge, QGraphicsLayoutItem secondItem, Qt.AnchorPoint secondEdge)'''
        return QGraphicsAnchor()


class QGraphicsEffect(QObject):
    """"""
    # Enum QGraphicsEffect.PixmapPadMode
    NoPad = 0
    PadToTransparentBorder = 0
    PadToEffectiveBoundingRect = 0

    # Enum QGraphicsEffect.ChangeFlag
    SourceAttached = 0
    SourceDetached = 0
    SourceBoundingRectChanged = 0
    SourceInvalidated = 0

    def __init__(self, parent = None):
        '''void QGraphicsEffect.__init__(QObject parent = None)'''
    def sourcePixmap(self, system = None, offset = None, mode = None):
        '''QPixmap QGraphicsEffect.sourcePixmap(Qt.CoordinateSystem system = Qt.LogicalCoordinates, QPoint offset, QGraphicsEffect.PixmapPadMode mode = QGraphicsEffect.PadToEffectiveBoundingRect)'''
        return QPixmap()
    def drawSource(self, painter):
        '''void QGraphicsEffect.drawSource(QPainter painter)'''
    def sourceBoundingRect(self, system = None):
        '''QRectF QGraphicsEffect.sourceBoundingRect(Qt.CoordinateSystem system = Qt.LogicalCoordinates)'''
        return QRectF()
    def sourceIsPixmap(self):
        '''bool QGraphicsEffect.sourceIsPixmap()'''
        return bool()
    def updateBoundingRect(self):
        '''void QGraphicsEffect.updateBoundingRect()'''
    def sourceChanged(self, flags):
        '''void QGraphicsEffect.sourceChanged(QGraphicsEffect.ChangeFlags flags)'''
    def draw(self, painter):
        '''abstract void QGraphicsEffect.draw(QPainter painter)'''
    enabledChanged = pyqtSignal() # void enabledChanged(bool) - signal
    def update(self):
        '''void QGraphicsEffect.update()'''
    def setEnabled(self, enable):
        '''void QGraphicsEffect.setEnabled(bool enable)'''
    def isEnabled(self):
        '''bool QGraphicsEffect.isEnabled()'''
        return bool()
    def boundingRect(self):
        '''QRectF QGraphicsEffect.boundingRect()'''
        return QRectF()
    def boundingRectFor(self, sourceRect):
        '''QRectF QGraphicsEffect.boundingRectFor(QRectF sourceRect)'''
        return QRectF()
    class ChangeFlags():
        """"""
        def __init__(self):
            '''QGraphicsEffect.ChangeFlags QGraphicsEffect.ChangeFlags.__init__()'''
            return QGraphicsEffect.ChangeFlags()
        def __init__(self):
            '''int QGraphicsEffect.ChangeFlags.__init__()'''
            return int()
        def __init__(self):
            '''void QGraphicsEffect.ChangeFlags.__init__()'''
        def __bool__(self):
            '''int QGraphicsEffect.ChangeFlags.__bool__()'''
            return int()
        def __ne__(self, f):
            '''bool QGraphicsEffect.ChangeFlags.__ne__(QGraphicsEffect.ChangeFlags f)'''
            return bool()
        def __eq__(self, f):
            '''bool QGraphicsEffect.ChangeFlags.__eq__(QGraphicsEffect.ChangeFlags f)'''
            return bool()
        def __invert__(self):
            '''QGraphicsEffect.ChangeFlags QGraphicsEffect.ChangeFlags.__invert__()'''
            return QGraphicsEffect.ChangeFlags()
        def __and__(self, mask):
            '''QGraphicsEffect.ChangeFlags QGraphicsEffect.ChangeFlags.__and__(int mask)'''
            return QGraphicsEffect.ChangeFlags()
        def __xor__(self, f):
            '''QGraphicsEffect.ChangeFlags QGraphicsEffect.ChangeFlags.__xor__(QGraphicsEffect.ChangeFlags f)'''
            return QGraphicsEffect.ChangeFlags()
        def __xor__(self, f):
            '''QGraphicsEffect.ChangeFlags QGraphicsEffect.ChangeFlags.__xor__(int f)'''
            return QGraphicsEffect.ChangeFlags()
        def __or__(self, f):
            '''QGraphicsEffect.ChangeFlags QGraphicsEffect.ChangeFlags.__or__(QGraphicsEffect.ChangeFlags f)'''
            return QGraphicsEffect.ChangeFlags()
        def __or__(self, f):
            '''QGraphicsEffect.ChangeFlags QGraphicsEffect.ChangeFlags.__or__(int f)'''
            return QGraphicsEffect.ChangeFlags()
        def __int__(self):
            '''int QGraphicsEffect.ChangeFlags.__int__()'''
            return int()
        def __ixor__(self, f):
            '''QGraphicsEffect.ChangeFlags QGraphicsEffect.ChangeFlags.__ixor__(QGraphicsEffect.ChangeFlags f)'''
            return QGraphicsEffect.ChangeFlags()
        def __ior__(self, f):
            '''QGraphicsEffect.ChangeFlags QGraphicsEffect.ChangeFlags.__ior__(QGraphicsEffect.ChangeFlags f)'''
            return QGraphicsEffect.ChangeFlags()
        def __iand__(self, mask):
            '''QGraphicsEffect.ChangeFlags QGraphicsEffect.ChangeFlags.__iand__(int mask)'''
            return QGraphicsEffect.ChangeFlags()


class QGraphicsColorizeEffect(QGraphicsEffect):
    """"""
    def __init__(self, parent = None):
        '''void QGraphicsColorizeEffect.__init__(QObject parent = None)'''
    def draw(self, painter):
        '''void QGraphicsColorizeEffect.draw(QPainter painter)'''
    strengthChanged = pyqtSignal() # void strengthChanged(qreal) - signal
    colorChanged = pyqtSignal() # void colorChanged(const QColoramp;) - signal
    def setStrength(self, strength):
        '''void QGraphicsColorizeEffect.setStrength(float strength)'''
    def setColor(self, c):
        '''void QGraphicsColorizeEffect.setColor(QColor c)'''
    def strength(self):
        '''float QGraphicsColorizeEffect.strength()'''
        return float()
    def color(self):
        '''QColor QGraphicsColorizeEffect.color()'''
        return QColor()


class QGraphicsBlurEffect(QGraphicsEffect):
    """"""
    # Enum QGraphicsBlurEffect.BlurHint
    PerformanceHint = 0
    QualityHint = 0
    AnimationHint = 0

    def __init__(self, parent = None):
        '''void QGraphicsBlurEffect.__init__(QObject parent = None)'''
    def draw(self, painter):
        '''void QGraphicsBlurEffect.draw(QPainter painter)'''
    blurHintsChanged = pyqtSignal() # void blurHintsChanged(QGraphicsBlurEffect::BlurHints) - signal
    blurRadiusChanged = pyqtSignal() # void blurRadiusChanged(qreal) - signal
    def setBlurHints(self, hints):
        '''void QGraphicsBlurEffect.setBlurHints(QGraphicsBlurEffect.BlurHints hints)'''
    def setBlurRadius(self, blurRadius):
        '''void QGraphicsBlurEffect.setBlurRadius(float blurRadius)'''
    def blurHints(self):
        '''QGraphicsBlurEffect.BlurHints QGraphicsBlurEffect.blurHints()'''
        return QGraphicsBlurEffect.BlurHints()
    def blurRadius(self):
        '''float QGraphicsBlurEffect.blurRadius()'''
        return float()
    def boundingRectFor(self, rect):
        '''QRectF QGraphicsBlurEffect.boundingRectFor(QRectF rect)'''
        return QRectF()
    class BlurHints():
        """"""
        def __init__(self):
            '''QGraphicsBlurEffect.BlurHints QGraphicsBlurEffect.BlurHints.__init__()'''
            return QGraphicsBlurEffect.BlurHints()
        def __init__(self):
            '''int QGraphicsBlurEffect.BlurHints.__init__()'''
            return int()
        def __init__(self):
            '''void QGraphicsBlurEffect.BlurHints.__init__()'''
        def __bool__(self):
            '''int QGraphicsBlurEffect.BlurHints.__bool__()'''
            return int()
        def __ne__(self, f):
            '''bool QGraphicsBlurEffect.BlurHints.__ne__(QGraphicsBlurEffect.BlurHints f)'''
            return bool()
        def __eq__(self, f):
            '''bool QGraphicsBlurEffect.BlurHints.__eq__(QGraphicsBlurEffect.BlurHints f)'''
            return bool()
        def __invert__(self):
            '''QGraphicsBlurEffect.BlurHints QGraphicsBlurEffect.BlurHints.__invert__()'''
            return QGraphicsBlurEffect.BlurHints()
        def __and__(self, mask):
            '''QGraphicsBlurEffect.BlurHints QGraphicsBlurEffect.BlurHints.__and__(int mask)'''
            return QGraphicsBlurEffect.BlurHints()
        def __xor__(self, f):
            '''QGraphicsBlurEffect.BlurHints QGraphicsBlurEffect.BlurHints.__xor__(QGraphicsBlurEffect.BlurHints f)'''
            return QGraphicsBlurEffect.BlurHints()
        def __xor__(self, f):
            '''QGraphicsBlurEffect.BlurHints QGraphicsBlurEffect.BlurHints.__xor__(int f)'''
            return QGraphicsBlurEffect.BlurHints()
        def __or__(self, f):
            '''QGraphicsBlurEffect.BlurHints QGraphicsBlurEffect.BlurHints.__or__(QGraphicsBlurEffect.BlurHints f)'''
            return QGraphicsBlurEffect.BlurHints()
        def __or__(self, f):
            '''QGraphicsBlurEffect.BlurHints QGraphicsBlurEffect.BlurHints.__or__(int f)'''
            return QGraphicsBlurEffect.BlurHints()
        def __int__(self):
            '''int QGraphicsBlurEffect.BlurHints.__int__()'''
            return int()
        def __ixor__(self, f):
            '''QGraphicsBlurEffect.BlurHints QGraphicsBlurEffect.BlurHints.__ixor__(QGraphicsBlurEffect.BlurHints f)'''
            return QGraphicsBlurEffect.BlurHints()
        def __ior__(self, f):
            '''QGraphicsBlurEffect.BlurHints QGraphicsBlurEffect.BlurHints.__ior__(QGraphicsBlurEffect.BlurHints f)'''
            return QGraphicsBlurEffect.BlurHints()
        def __iand__(self, mask):
            '''QGraphicsBlurEffect.BlurHints QGraphicsBlurEffect.BlurHints.__iand__(int mask)'''
            return QGraphicsBlurEffect.BlurHints()


class QGraphicsDropShadowEffect(QGraphicsEffect):
    """"""
    def __init__(self, parent = None):
        '''void QGraphicsDropShadowEffect.__init__(QObject parent = None)'''
    def draw(self, painter):
        '''void QGraphicsDropShadowEffect.draw(QPainter painter)'''
    colorChanged = pyqtSignal() # void colorChanged(const QColoramp;) - signal
    blurRadiusChanged = pyqtSignal() # void blurRadiusChanged(qreal) - signal
    offsetChanged = pyqtSignal() # void offsetChanged(const QPointFamp;) - signal
    def setColor(self, color):
        '''void QGraphicsDropShadowEffect.setColor(QColor color)'''
    def setBlurRadius(self, blurRadius):
        '''void QGraphicsDropShadowEffect.setBlurRadius(float blurRadius)'''
    def setYOffset(self, dy):
        '''void QGraphicsDropShadowEffect.setYOffset(float dy)'''
    def setXOffset(self, dx):
        '''void QGraphicsDropShadowEffect.setXOffset(float dx)'''
    def setOffset(self, ofs):
        '''void QGraphicsDropShadowEffect.setOffset(QPointF ofs)'''
    def setOffset(self, dx, dy):
        '''void QGraphicsDropShadowEffect.setOffset(float dx, float dy)'''
    def setOffset(self, d):
        '''void QGraphicsDropShadowEffect.setOffset(float d)'''
    def color(self):
        '''QColor QGraphicsDropShadowEffect.color()'''
        return QColor()
    def blurRadius(self):
        '''float QGraphicsDropShadowEffect.blurRadius()'''
        return float()
    def yOffset(self):
        '''float QGraphicsDropShadowEffect.yOffset()'''
        return float()
    def xOffset(self):
        '''float QGraphicsDropShadowEffect.xOffset()'''
        return float()
    def offset(self):
        '''QPointF QGraphicsDropShadowEffect.offset()'''
        return QPointF()
    def boundingRectFor(self, rect):
        '''QRectF QGraphicsDropShadowEffect.boundingRectFor(QRectF rect)'''
        return QRectF()


class QGraphicsOpacityEffect(QGraphicsEffect):
    """"""
    def __init__(self, parent = None):
        '''void QGraphicsOpacityEffect.__init__(QObject parent = None)'''
    def draw(self, painter):
        '''void QGraphicsOpacityEffect.draw(QPainter painter)'''
    opacityMaskChanged = pyqtSignal() # void opacityMaskChanged(const QBrushamp;) - signal
    opacityChanged = pyqtSignal() # void opacityChanged(qreal) - signal
    def setOpacityMask(self, mask):
        '''void QGraphicsOpacityEffect.setOpacityMask(QBrush mask)'''
    def setOpacity(self, opacity):
        '''void QGraphicsOpacityEffect.setOpacity(float opacity)'''
    def opacityMask(self):
        '''QBrush QGraphicsOpacityEffect.opacityMask()'''
        return QBrush()
    def opacity(self):
        '''float QGraphicsOpacityEffect.opacity()'''
        return float()


class QGraphicsGridLayout(QGraphicsLayout):
    """"""
    def __init__(self, parent = None):
        '''void QGraphicsGridLayout.__init__(QGraphicsLayoutItem parent = None)'''
    def removeItem(self, item):
        '''void QGraphicsGridLayout.removeItem(QGraphicsLayoutItem item)'''
    def sizeHint(self, which, constraint = QSizeF()):
        '''QSizeF QGraphicsGridLayout.sizeHint(Qt.SizeHint which, QSizeF constraint = QSizeF())'''
        return QSizeF()
    def setGeometry(self, rect):
        '''void QGraphicsGridLayout.setGeometry(QRectF rect)'''
    def invalidate(self):
        '''void QGraphicsGridLayout.invalidate()'''
    def removeAt(self, index):
        '''void QGraphicsGridLayout.removeAt(int index)'''
    def count(self):
        '''int QGraphicsGridLayout.count()'''
        return int()
    def itemAt(self, row, column):
        '''QGraphicsLayoutItem QGraphicsGridLayout.itemAt(int row, int column)'''
        return QGraphicsLayoutItem()
    def itemAt(self, index):
        '''QGraphicsLayoutItem QGraphicsGridLayout.itemAt(int index)'''
        return QGraphicsLayoutItem()
    def columnCount(self):
        '''int QGraphicsGridLayout.columnCount()'''
        return int()
    def rowCount(self):
        '''int QGraphicsGridLayout.rowCount()'''
        return int()
    def alignment(self, item):
        '''Qt.Alignment QGraphicsGridLayout.alignment(QGraphicsLayoutItem item)'''
        return Qt.Alignment()
    def setAlignment(self, item, alignment):
        '''void QGraphicsGridLayout.setAlignment(QGraphicsLayoutItem item, Qt.Alignment alignment)'''
    def columnAlignment(self, column):
        '''Qt.Alignment QGraphicsGridLayout.columnAlignment(int column)'''
        return Qt.Alignment()
    def setColumnAlignment(self, column, alignment):
        '''void QGraphicsGridLayout.setColumnAlignment(int column, Qt.Alignment alignment)'''
    def rowAlignment(self, row):
        '''Qt.Alignment QGraphicsGridLayout.rowAlignment(int row)'''
        return Qt.Alignment()
    def setRowAlignment(self, row, alignment):
        '''void QGraphicsGridLayout.setRowAlignment(int row, Qt.Alignment alignment)'''
    def setColumnFixedWidth(self, column, width):
        '''void QGraphicsGridLayout.setColumnFixedWidth(int column, float width)'''
    def columnMaximumWidth(self, column):
        '''float QGraphicsGridLayout.columnMaximumWidth(int column)'''
        return float()
    def setColumnMaximumWidth(self, column, width):
        '''void QGraphicsGridLayout.setColumnMaximumWidth(int column, float width)'''
    def columnPreferredWidth(self, column):
        '''float QGraphicsGridLayout.columnPreferredWidth(int column)'''
        return float()
    def setColumnPreferredWidth(self, column, width):
        '''void QGraphicsGridLayout.setColumnPreferredWidth(int column, float width)'''
    def columnMinimumWidth(self, column):
        '''float QGraphicsGridLayout.columnMinimumWidth(int column)'''
        return float()
    def setColumnMinimumWidth(self, column, width):
        '''void QGraphicsGridLayout.setColumnMinimumWidth(int column, float width)'''
    def setRowFixedHeight(self, row, height):
        '''void QGraphicsGridLayout.setRowFixedHeight(int row, float height)'''
    def rowMaximumHeight(self, row):
        '''float QGraphicsGridLayout.rowMaximumHeight(int row)'''
        return float()
    def setRowMaximumHeight(self, row, height):
        '''void QGraphicsGridLayout.setRowMaximumHeight(int row, float height)'''
    def rowPreferredHeight(self, row):
        '''float QGraphicsGridLayout.rowPreferredHeight(int row)'''
        return float()
    def setRowPreferredHeight(self, row, height):
        '''void QGraphicsGridLayout.setRowPreferredHeight(int row, float height)'''
    def rowMinimumHeight(self, row):
        '''float QGraphicsGridLayout.rowMinimumHeight(int row)'''
        return float()
    def setRowMinimumHeight(self, row, height):
        '''void QGraphicsGridLayout.setRowMinimumHeight(int row, float height)'''
    def columnStretchFactor(self, column):
        '''int QGraphicsGridLayout.columnStretchFactor(int column)'''
        return int()
    def setColumnStretchFactor(self, column, stretch):
        '''void QGraphicsGridLayout.setColumnStretchFactor(int column, int stretch)'''
    def rowStretchFactor(self, row):
        '''int QGraphicsGridLayout.rowStretchFactor(int row)'''
        return int()
    def setRowStretchFactor(self, row, stretch):
        '''void QGraphicsGridLayout.setRowStretchFactor(int row, int stretch)'''
    def columnSpacing(self, column):
        '''float QGraphicsGridLayout.columnSpacing(int column)'''
        return float()
    def setColumnSpacing(self, column, spacing):
        '''void QGraphicsGridLayout.setColumnSpacing(int column, float spacing)'''
    def rowSpacing(self, row):
        '''float QGraphicsGridLayout.rowSpacing(int row)'''
        return float()
    def setRowSpacing(self, row, spacing):
        '''void QGraphicsGridLayout.setRowSpacing(int row, float spacing)'''
    def setSpacing(self, spacing):
        '''void QGraphicsGridLayout.setSpacing(float spacing)'''
    def verticalSpacing(self):
        '''float QGraphicsGridLayout.verticalSpacing()'''
        return float()
    def setVerticalSpacing(self, spacing):
        '''void QGraphicsGridLayout.setVerticalSpacing(float spacing)'''
    def horizontalSpacing(self):
        '''float QGraphicsGridLayout.horizontalSpacing()'''
        return float()
    def setHorizontalSpacing(self, spacing):
        '''void QGraphicsGridLayout.setHorizontalSpacing(float spacing)'''
    def addItem(self, item, row, column, rowSpan, columnSpan, alignment = 0):
        '''void QGraphicsGridLayout.addItem(QGraphicsLayoutItem item, int row, int column, int rowSpan, int columnSpan, Qt.Alignment alignment = 0)'''
    def addItem(self, aitem, arow, acolumn, alignment = 0):
        '''void QGraphicsGridLayout.addItem(QGraphicsLayoutItem aitem, int arow, int acolumn, Qt.Alignment alignment = 0)'''


class QGraphicsItem():
    """"""
    # Enum QGraphicsItem.PanelModality
    NonModal = 0
    PanelModal = 0
    SceneModal = 0

    # Enum QGraphicsItem.GraphicsItemFlag
    ItemIsMovable = 0
    ItemIsSelectable = 0
    ItemIsFocusable = 0
    ItemClipsToShape = 0
    ItemClipsChildrenToShape = 0
    ItemIgnoresTransformations = 0
    ItemIgnoresParentOpacity = 0
    ItemDoesntPropagateOpacityToChildren = 0
    ItemStacksBehindParent = 0
    ItemUsesExtendedStyleOption = 0
    ItemHasNoContents = 0
    ItemSendsGeometryChanges = 0
    ItemAcceptsInputMethod = 0
    ItemNegativeZStacksBehindParent = 0
    ItemIsPanel = 0
    ItemSendsScenePositionChanges = 0
    ItemContainsChildrenInShape = 0

    # Enum QGraphicsItem.GraphicsItemChange
    ItemPositionChange = 0
    ItemMatrixChange = 0
    ItemVisibleChange = 0
    ItemEnabledChange = 0
    ItemSelectedChange = 0
    ItemParentChange = 0
    ItemChildAddedChange = 0
    ItemChildRemovedChange = 0
    ItemTransformChange = 0
    ItemPositionHasChanged = 0
    ItemTransformHasChanged = 0
    ItemSceneChange = 0
    ItemVisibleHasChanged = 0
    ItemEnabledHasChanged = 0
    ItemSelectedHasChanged = 0
    ItemParentHasChanged = 0
    ItemSceneHasChanged = 0
    ItemCursorChange = 0
    ItemCursorHasChanged = 0
    ItemToolTipChange = 0
    ItemToolTipHasChanged = 0
    ItemFlagsChange = 0
    ItemFlagsHaveChanged = 0
    ItemZValueChange = 0
    ItemZValueHasChanged = 0
    ItemOpacityChange = 0
    ItemOpacityHasChanged = 0
    ItemScenePositionHasChanged = 0
    ItemRotationChange = 0
    ItemRotationHasChanged = 0
    ItemScaleChange = 0
    ItemScaleHasChanged = 0
    ItemTransformOriginPointChange = 0
    ItemTransformOriginPointHasChanged = 0

    # Enum QGraphicsItem.CacheMode
    NoCache = 0
    ItemCoordinateCache = 0
    DeviceCoordinateCache = 0

    Type = None # int - member
    UserType = None # int - member
    def __init__(self, parent = None):
        '''void QGraphicsItem.__init__(QGraphicsItem parent = None)'''
    def updateMicroFocus(self):
        '''void QGraphicsItem.updateMicroFocus()'''
    def setInputMethodHints(self, hints):
        '''void QGraphicsItem.setInputMethodHints(Qt.InputMethodHints hints)'''
    def inputMethodHints(self):
        '''Qt.InputMethodHints QGraphicsItem.inputMethodHints()'''
        return Qt.InputMethodHints()
    def stackBefore(self, sibling):
        '''void QGraphicsItem.stackBefore(QGraphicsItem sibling)'''
    def setTransformOriginPoint(self, origin):
        '''void QGraphicsItem.setTransformOriginPoint(QPointF origin)'''
    def setTransformOriginPoint(self, ax, ay):
        '''void QGraphicsItem.setTransformOriginPoint(float ax, float ay)'''
    def transformOriginPoint(self):
        '''QPointF QGraphicsItem.transformOriginPoint()'''
        return QPointF()
    def setTransformations(self, transformations):
        '''void QGraphicsItem.setTransformations(list-of-QGraphicsTransform transformations)'''
    def transformations(self):
        '''list-of-QGraphicsTransform QGraphicsItem.transformations()'''
        return [QGraphicsTransform()]
    def scale(self):
        '''float QGraphicsItem.scale()'''
        return float()
    def setScale(self, scale):
        '''void QGraphicsItem.setScale(float scale)'''
    def rotation(self):
        '''float QGraphicsItem.rotation()'''
        return float()
    def setRotation(self, angle):
        '''void QGraphicsItem.setRotation(float angle)'''
    def setY(self, y):
        '''void QGraphicsItem.setY(float y)'''
    def setX(self, x):
        '''void QGraphicsItem.setX(float x)'''
    def focusItem(self):
        '''QGraphicsItem QGraphicsItem.focusItem()'''
        return QGraphicsItem()
    def setFocusProxy(self, item):
        '''void QGraphicsItem.setFocusProxy(QGraphicsItem item)'''
    def focusProxy(self):
        '''QGraphicsItem QGraphicsItem.focusProxy()'''
        return QGraphicsItem()
    def setActive(self, active):
        '''void QGraphicsItem.setActive(bool active)'''
    def isActive(self):
        '''bool QGraphicsItem.isActive()'''
        return bool()
    def setFiltersChildEvents(self, enabled):
        '''void QGraphicsItem.setFiltersChildEvents(bool enabled)'''
    def filtersChildEvents(self):
        '''bool QGraphicsItem.filtersChildEvents()'''
        return bool()
    def setAcceptTouchEvents(self, enabled):
        '''void QGraphicsItem.setAcceptTouchEvents(bool enabled)'''
    def acceptTouchEvents(self):
        '''bool QGraphicsItem.acceptTouchEvents()'''
        return bool()
    def setGraphicsEffect(self, effect):
        '''void QGraphicsItem.setGraphicsEffect(QGraphicsEffect effect)'''
    def graphicsEffect(self):
        '''QGraphicsEffect QGraphicsItem.graphicsEffect()'''
        return QGraphicsEffect()
    def isBlockedByModalPanel(self, blockingPanel):
        '''bool QGraphicsItem.isBlockedByModalPanel(QGraphicsItem blockingPanel)'''
        return bool()
    def setPanelModality(self, panelModality):
        '''void QGraphicsItem.setPanelModality(QGraphicsItem.PanelModality panelModality)'''
    def panelModality(self):
        '''QGraphicsItem.PanelModality QGraphicsItem.panelModality()'''
        return QGraphicsItem.PanelModality()
    def toGraphicsObject(self):
        '''QGraphicsObject QGraphicsItem.toGraphicsObject()'''
        return QGraphicsObject()
    def isPanel(self):
        '''bool QGraphicsItem.isPanel()'''
        return bool()
    def panel(self):
        '''QGraphicsItem QGraphicsItem.panel()'''
        return QGraphicsItem()
    def parentObject(self):
        '''QGraphicsObject QGraphicsItem.parentObject()'''
        return QGraphicsObject()
    def mapRectFromScene(self, rect):
        '''QRectF QGraphicsItem.mapRectFromScene(QRectF rect)'''
        return QRectF()
    def mapRectFromScene(self, ax, ay, w, h):
        '''QRectF QGraphicsItem.mapRectFromScene(float ax, float ay, float w, float h)'''
        return QRectF()
    def mapRectFromParent(self, rect):
        '''QRectF QGraphicsItem.mapRectFromParent(QRectF rect)'''
        return QRectF()
    def mapRectFromParent(self, ax, ay, w, h):
        '''QRectF QGraphicsItem.mapRectFromParent(float ax, float ay, float w, float h)'''
        return QRectF()
    def mapRectFromItem(self, item, rect):
        '''QRectF QGraphicsItem.mapRectFromItem(QGraphicsItem item, QRectF rect)'''
        return QRectF()
    def mapRectFromItem(self, item, ax, ay, w, h):
        '''QRectF QGraphicsItem.mapRectFromItem(QGraphicsItem item, float ax, float ay, float w, float h)'''
        return QRectF()
    def mapRectToScene(self, rect):
        '''QRectF QGraphicsItem.mapRectToScene(QRectF rect)'''
        return QRectF()
    def mapRectToScene(self, ax, ay, w, h):
        '''QRectF QGraphicsItem.mapRectToScene(float ax, float ay, float w, float h)'''
        return QRectF()
    def mapRectToParent(self, rect):
        '''QRectF QGraphicsItem.mapRectToParent(QRectF rect)'''
        return QRectF()
    def mapRectToParent(self, ax, ay, w, h):
        '''QRectF QGraphicsItem.mapRectToParent(float ax, float ay, float w, float h)'''
        return QRectF()
    def mapRectToItem(self, item, rect):
        '''QRectF QGraphicsItem.mapRectToItem(QGraphicsItem item, QRectF rect)'''
        return QRectF()
    def mapRectToItem(self, item, ax, ay, w, h):
        '''QRectF QGraphicsItem.mapRectToItem(QGraphicsItem item, float ax, float ay, float w, float h)'''
        return QRectF()
    def clipPath(self):
        '''QPainterPath QGraphicsItem.clipPath()'''
        return QPainterPath()
    def isClipped(self):
        '''bool QGraphicsItem.isClipped()'''
        return bool()
    def itemTransform(self, other, ok):
        '''QTransform QGraphicsItem.itemTransform(QGraphicsItem other, bool ok)'''
        return QTransform()
    def setOpacity(self, opacity):
        '''void QGraphicsItem.setOpacity(float opacity)'''
    def effectiveOpacity(self):
        '''float QGraphicsItem.effectiveOpacity()'''
        return float()
    def opacity(self):
        '''float QGraphicsItem.opacity()'''
        return float()
    def isUnderMouse(self):
        '''bool QGraphicsItem.isUnderMouse()'''
        return bool()
    def commonAncestorItem(self, other):
        '''QGraphicsItem QGraphicsItem.commonAncestorItem(QGraphicsItem other)'''
        return QGraphicsItem()
    def scroll(self, dx, dy, rect = QRectF()):
        '''void QGraphicsItem.scroll(float dx, float dy, QRectF rect = QRectF())'''
    def setBoundingRegionGranularity(self, granularity):
        '''void QGraphicsItem.setBoundingRegionGranularity(float granularity)'''
    def boundingRegionGranularity(self):
        '''float QGraphicsItem.boundingRegionGranularity()'''
        return float()
    def boundingRegion(self, itemToDeviceTransform):
        '''QRegion QGraphicsItem.boundingRegion(QTransform itemToDeviceTransform)'''
        return QRegion()
    def ungrabKeyboard(self):
        '''void QGraphicsItem.ungrabKeyboard()'''
    def grabKeyboard(self):
        '''void QGraphicsItem.grabKeyboard()'''
    def ungrabMouse(self):
        '''void QGraphicsItem.ungrabMouse()'''
    def grabMouse(self):
        '''void QGraphicsItem.grabMouse()'''
    def setAcceptHoverEvents(self, enabled):
        '''void QGraphicsItem.setAcceptHoverEvents(bool enabled)'''
    def acceptHoverEvents(self):
        '''bool QGraphicsItem.acceptHoverEvents()'''
        return bool()
    def isVisibleTo(self, parent):
        '''bool QGraphicsItem.isVisibleTo(QGraphicsItem parent)'''
        return bool()
    def setCacheMode(self, mode, logicalCacheSize = QSize()):
        '''void QGraphicsItem.setCacheMode(QGraphicsItem.CacheMode mode, QSize logicalCacheSize = QSize())'''
    def cacheMode(self):
        '''QGraphicsItem.CacheMode QGraphicsItem.cacheMode()'''
        return QGraphicsItem.CacheMode()
    def isWindow(self):
        '''bool QGraphicsItem.isWindow()'''
        return bool()
    def isWidget(self):
        '''bool QGraphicsItem.isWidget()'''
        return bool()
    def childItems(self):
        '''list-of-QGraphicsItem QGraphicsItem.childItems()'''
        return [QGraphicsItem()]
    def window(self):
        '''QGraphicsWidget QGraphicsItem.window()'''
        return QGraphicsWidget()
    def topLevelWidget(self):
        '''QGraphicsWidget QGraphicsItem.topLevelWidget()'''
        return QGraphicsWidget()
    def parentWidget(self):
        '''QGraphicsWidget QGraphicsItem.parentWidget()'''
        return QGraphicsWidget()
    def isObscured(self, rect = QRectF()):
        '''bool QGraphicsItem.isObscured(QRectF rect = QRectF())'''
        return bool()
    def isObscured(self, ax, ay, w, h):
        '''bool QGraphicsItem.isObscured(float ax, float ay, float w, float h)'''
        return bool()
    def resetTransform(self):
        '''void QGraphicsItem.resetTransform()'''
    def setTransform(self, matrix, combine = False):
        '''void QGraphicsItem.setTransform(QTransform matrix, bool combine = False)'''
    def deviceTransform(self, viewportTransform):
        '''QTransform QGraphicsItem.deviceTransform(QTransform viewportTransform)'''
        return QTransform()
    def sceneTransform(self):
        '''QTransform QGraphicsItem.sceneTransform()'''
        return QTransform()
    def transform(self):
        '''QTransform QGraphicsItem.transform()'''
        return QTransform()
    def wheelEvent(self, event):
        '''void QGraphicsItem.wheelEvent(QGraphicsSceneWheelEvent event)'''
    def sceneEventFilter(self, watched, event):
        '''bool QGraphicsItem.sceneEventFilter(QGraphicsItem watched, QEvent event)'''
        return bool()
    def sceneEvent(self, event):
        '''bool QGraphicsItem.sceneEvent(QEvent event)'''
        return bool()
    def prepareGeometryChange(self):
        '''void QGraphicsItem.prepareGeometryChange()'''
    def mouseReleaseEvent(self, event):
        '''void QGraphicsItem.mouseReleaseEvent(QGraphicsSceneMouseEvent event)'''
    def mousePressEvent(self, event):
        '''void QGraphicsItem.mousePressEvent(QGraphicsSceneMouseEvent event)'''
    def mouseMoveEvent(self, event):
        '''void QGraphicsItem.mouseMoveEvent(QGraphicsSceneMouseEvent event)'''
    def mouseDoubleClickEvent(self, event):
        '''void QGraphicsItem.mouseDoubleClickEvent(QGraphicsSceneMouseEvent event)'''
    def keyReleaseEvent(self, event):
        '''void QGraphicsItem.keyReleaseEvent(QKeyEvent event)'''
    def keyPressEvent(self, event):
        '''void QGraphicsItem.keyPressEvent(QKeyEvent event)'''
    def itemChange(self, change, value):
        '''QVariant QGraphicsItem.itemChange(QGraphicsItem.GraphicsItemChange change, QVariant value)'''
        return QVariant()
    def inputMethodQuery(self, query):
        '''QVariant QGraphicsItem.inputMethodQuery(Qt.InputMethodQuery query)'''
        return QVariant()
    def inputMethodEvent(self, event):
        '''void QGraphicsItem.inputMethodEvent(QInputMethodEvent event)'''
    def hoverMoveEvent(self, event):
        '''void QGraphicsItem.hoverMoveEvent(QGraphicsSceneHoverEvent event)'''
    def hoverLeaveEvent(self, event):
        '''void QGraphicsItem.hoverLeaveEvent(QGraphicsSceneHoverEvent event)'''
    def hoverEnterEvent(self, event):
        '''void QGraphicsItem.hoverEnterEvent(QGraphicsSceneHoverEvent event)'''
    def focusOutEvent(self, event):
        '''void QGraphicsItem.focusOutEvent(QFocusEvent event)'''
    def focusInEvent(self, event):
        '''void QGraphicsItem.focusInEvent(QFocusEvent event)'''
    def dropEvent(self, event):
        '''void QGraphicsItem.dropEvent(QGraphicsSceneDragDropEvent event)'''
    def dragMoveEvent(self, event):
        '''void QGraphicsItem.dragMoveEvent(QGraphicsSceneDragDropEvent event)'''
    def dragLeaveEvent(self, event):
        '''void QGraphicsItem.dragLeaveEvent(QGraphicsSceneDragDropEvent event)'''
    def dragEnterEvent(self, event):
        '''void QGraphicsItem.dragEnterEvent(QGraphicsSceneDragDropEvent event)'''
    def contextMenuEvent(self, event):
        '''void QGraphicsItem.contextMenuEvent(QGraphicsSceneContextMenuEvent event)'''
    def removeSceneEventFilter(self, filterItem):
        '''void QGraphicsItem.removeSceneEventFilter(QGraphicsItem filterItem)'''
    def installSceneEventFilter(self, filterItem):
        '''void QGraphicsItem.installSceneEventFilter(QGraphicsItem filterItem)'''
    def type(self):
        '''int QGraphicsItem.type()'''
        return int()
    def setData(self, key, value):
        '''void QGraphicsItem.setData(int key, QVariant value)'''
    def data(self, key):
        '''QVariant QGraphicsItem.data(int key)'''
        return QVariant()
    def isAncestorOf(self, child):
        '''bool QGraphicsItem.isAncestorOf(QGraphicsItem child)'''
        return bool()
    def mapFromScene(self, point):
        '''QPointF QGraphicsItem.mapFromScene(QPointF point)'''
        return QPointF()
    def mapFromScene(self, rect):
        '''QPolygonF QGraphicsItem.mapFromScene(QRectF rect)'''
        return QPolygonF()
    def mapFromScene(self, polygon):
        '''QPolygonF QGraphicsItem.mapFromScene(QPolygonF polygon)'''
        return QPolygonF()
    def mapFromScene(self, path):
        '''QPainterPath QGraphicsItem.mapFromScene(QPainterPath path)'''
        return QPainterPath()
    def mapFromScene(self, ax, ay):
        '''QPointF QGraphicsItem.mapFromScene(float ax, float ay)'''
        return QPointF()
    def mapFromScene(self, ax, ay, w, h):
        '''QPolygonF QGraphicsItem.mapFromScene(float ax, float ay, float w, float h)'''
        return QPolygonF()
    def mapFromParent(self, point):
        '''QPointF QGraphicsItem.mapFromParent(QPointF point)'''
        return QPointF()
    def mapFromParent(self, rect):
        '''QPolygonF QGraphicsItem.mapFromParent(QRectF rect)'''
        return QPolygonF()
    def mapFromParent(self, polygon):
        '''QPolygonF QGraphicsItem.mapFromParent(QPolygonF polygon)'''
        return QPolygonF()
    def mapFromParent(self, path):
        '''QPainterPath QGraphicsItem.mapFromParent(QPainterPath path)'''
        return QPainterPath()
    def mapFromParent(self, ax, ay):
        '''QPointF QGraphicsItem.mapFromParent(float ax, float ay)'''
        return QPointF()
    def mapFromParent(self, ax, ay, w, h):
        '''QPolygonF QGraphicsItem.mapFromParent(float ax, float ay, float w, float h)'''
        return QPolygonF()
    def mapFromItem(self, item, point):
        '''QPointF QGraphicsItem.mapFromItem(QGraphicsItem item, QPointF point)'''
        return QPointF()
    def mapFromItem(self, item, rect):
        '''QPolygonF QGraphicsItem.mapFromItem(QGraphicsItem item, QRectF rect)'''
        return QPolygonF()
    def mapFromItem(self, item, polygon):
        '''QPolygonF QGraphicsItem.mapFromItem(QGraphicsItem item, QPolygonF polygon)'''
        return QPolygonF()
    def mapFromItem(self, item, path):
        '''QPainterPath QGraphicsItem.mapFromItem(QGraphicsItem item, QPainterPath path)'''
        return QPainterPath()
    def mapFromItem(self, item, ax, ay):
        '''QPointF QGraphicsItem.mapFromItem(QGraphicsItem item, float ax, float ay)'''
        return QPointF()
    def mapFromItem(self, item, ax, ay, w, h):
        '''QPolygonF QGraphicsItem.mapFromItem(QGraphicsItem item, float ax, float ay, float w, float h)'''
        return QPolygonF()
    def mapToScene(self, point):
        '''QPointF QGraphicsItem.mapToScene(QPointF point)'''
        return QPointF()
    def mapToScene(self, rect):
        '''QPolygonF QGraphicsItem.mapToScene(QRectF rect)'''
        return QPolygonF()
    def mapToScene(self, polygon):
        '''QPolygonF QGraphicsItem.mapToScene(QPolygonF polygon)'''
        return QPolygonF()
    def mapToScene(self, path):
        '''QPainterPath QGraphicsItem.mapToScene(QPainterPath path)'''
        return QPainterPath()
    def mapToScene(self, ax, ay):
        '''QPointF QGraphicsItem.mapToScene(float ax, float ay)'''
        return QPointF()
    def mapToScene(self, ax, ay, w, h):
        '''QPolygonF QGraphicsItem.mapToScene(float ax, float ay, float w, float h)'''
        return QPolygonF()
    def mapToParent(self, point):
        '''QPointF QGraphicsItem.mapToParent(QPointF point)'''
        return QPointF()
    def mapToParent(self, rect):
        '''QPolygonF QGraphicsItem.mapToParent(QRectF rect)'''
        return QPolygonF()
    def mapToParent(self, polygon):
        '''QPolygonF QGraphicsItem.mapToParent(QPolygonF polygon)'''
        return QPolygonF()
    def mapToParent(self, path):
        '''QPainterPath QGraphicsItem.mapToParent(QPainterPath path)'''
        return QPainterPath()
    def mapToParent(self, ax, ay):
        '''QPointF QGraphicsItem.mapToParent(float ax, float ay)'''
        return QPointF()
    def mapToParent(self, ax, ay, w, h):
        '''QPolygonF QGraphicsItem.mapToParent(float ax, float ay, float w, float h)'''
        return QPolygonF()
    def mapToItem(self, item, point):
        '''QPointF QGraphicsItem.mapToItem(QGraphicsItem item, QPointF point)'''
        return QPointF()
    def mapToItem(self, item, rect):
        '''QPolygonF QGraphicsItem.mapToItem(QGraphicsItem item, QRectF rect)'''
        return QPolygonF()
    def mapToItem(self, item, polygon):
        '''QPolygonF QGraphicsItem.mapToItem(QGraphicsItem item, QPolygonF polygon)'''
        return QPolygonF()
    def mapToItem(self, item, path):
        '''QPainterPath QGraphicsItem.mapToItem(QGraphicsItem item, QPainterPath path)'''
        return QPainterPath()
    def mapToItem(self, item, ax, ay):
        '''QPointF QGraphicsItem.mapToItem(QGraphicsItem item, float ax, float ay)'''
        return QPointF()
    def mapToItem(self, item, ax, ay, w, h):
        '''QPolygonF QGraphicsItem.mapToItem(QGraphicsItem item, float ax, float ay, float w, float h)'''
        return QPolygonF()
    def update(self, rect = QRectF()):
        '''void QGraphicsItem.update(QRectF rect = QRectF())'''
    def update(self, ax, ay, width, height):
        '''void QGraphicsItem.update(float ax, float ay, float width, float height)'''
    def paint(self, painter, option, widget = None):
        '''abstract void QGraphicsItem.paint(QPainter painter, QStyleOptionGraphicsItem option, QWidget widget = None)'''
    def opaqueArea(self):
        '''QPainterPath QGraphicsItem.opaqueArea()'''
        return QPainterPath()
    def isObscuredBy(self, item):
        '''bool QGraphicsItem.isObscuredBy(QGraphicsItem item)'''
        return bool()
    def collidingItems(self, mode = None):
        '''list-of-QGraphicsItem QGraphicsItem.collidingItems(Qt.ItemSelectionMode mode = Qt.IntersectsItemShape)'''
        return [QGraphicsItem()]
    def collidesWithPath(self, path, mode = None):
        '''bool QGraphicsItem.collidesWithPath(QPainterPath path, Qt.ItemSelectionMode mode = Qt.IntersectsItemShape)'''
        return bool()
    def collidesWithItem(self, other, mode = None):
        '''bool QGraphicsItem.collidesWithItem(QGraphicsItem other, Qt.ItemSelectionMode mode = Qt.IntersectsItemShape)'''
        return bool()
    def contains(self, point):
        '''bool QGraphicsItem.contains(QPointF point)'''
        return bool()
    def shape(self):
        '''QPainterPath QGraphicsItem.shape()'''
        return QPainterPath()
    def sceneBoundingRect(self):
        '''QRectF QGraphicsItem.sceneBoundingRect()'''
        return QRectF()
    def childrenBoundingRect(self):
        '''QRectF QGraphicsItem.childrenBoundingRect()'''
        return QRectF()
    def boundingRect(self):
        '''abstract QRectF QGraphicsItem.boundingRect()'''
        return QRectF()
    def setZValue(self, z):
        '''void QGraphicsItem.setZValue(float z)'''
    def zValue(self):
        '''float QGraphicsItem.zValue()'''
        return float()
    def advance(self, phase):
        '''void QGraphicsItem.advance(int phase)'''
    def ensureVisible(self, rect = QRectF(), xMargin = 50, yMargin = 50):
        '''void QGraphicsItem.ensureVisible(QRectF rect = QRectF(), int xMargin = 50, int yMargin = 50)'''
    def ensureVisible(self, x, y, w, h, xMargin = 50, yMargin = 50):
        '''void QGraphicsItem.ensureVisible(float x, float y, float w, float h, int xMargin = 50, int yMargin = 50)'''
    def moveBy(self, dx, dy):
        '''void QGraphicsItem.moveBy(float dx, float dy)'''
    def setPos(self, pos):
        '''void QGraphicsItem.setPos(QPointF pos)'''
    def setPos(self, ax, ay):
        '''void QGraphicsItem.setPos(float ax, float ay)'''
    def scenePos(self):
        '''QPointF QGraphicsItem.scenePos()'''
        return QPointF()
    def y(self):
        '''float QGraphicsItem.y()'''
        return float()
    def x(self):
        '''float QGraphicsItem.x()'''
        return float()
    def pos(self):
        '''QPointF QGraphicsItem.pos()'''
        return QPointF()
    def clearFocus(self):
        '''void QGraphicsItem.clearFocus()'''
    def setFocus(self, focusReason = None):
        '''void QGraphicsItem.setFocus(Qt.FocusReason focusReason = Qt.OtherFocusReason)'''
    def hasFocus(self):
        '''bool QGraphicsItem.hasFocus()'''
        return bool()
    def setAcceptedMouseButtons(self, buttons):
        '''void QGraphicsItem.setAcceptedMouseButtons(Qt.MouseButtons buttons)'''
    def acceptedMouseButtons(self):
        '''Qt.MouseButtons QGraphicsItem.acceptedMouseButtons()'''
        return Qt.MouseButtons()
    def setAcceptDrops(self, on):
        '''void QGraphicsItem.setAcceptDrops(bool on)'''
    def acceptDrops(self):
        '''bool QGraphicsItem.acceptDrops()'''
        return bool()
    def setSelected(self, selected):
        '''void QGraphicsItem.setSelected(bool selected)'''
    def isSelected(self):
        '''bool QGraphicsItem.isSelected()'''
        return bool()
    def setEnabled(self, enabled):
        '''void QGraphicsItem.setEnabled(bool enabled)'''
    def isEnabled(self):
        '''bool QGraphicsItem.isEnabled()'''
        return bool()
    def show(self):
        '''void QGraphicsItem.show()'''
    def hide(self):
        '''void QGraphicsItem.hide()'''
    def setVisible(self, visible):
        '''void QGraphicsItem.setVisible(bool visible)'''
    def isVisible(self):
        '''bool QGraphicsItem.isVisible()'''
        return bool()
    def unsetCursor(self):
        '''void QGraphicsItem.unsetCursor()'''
    def hasCursor(self):
        '''bool QGraphicsItem.hasCursor()'''
        return bool()
    def setCursor(self, cursor):
        '''void QGraphicsItem.setCursor(QCursor cursor)'''
    def cursor(self):
        '''QCursor QGraphicsItem.cursor()'''
        return QCursor()
    def setToolTip(self, toolTip):
        '''void QGraphicsItem.setToolTip(str toolTip)'''
    def toolTip(self):
        '''str QGraphicsItem.toolTip()'''
        return str()
    def setFlags(self, flags):
        '''void QGraphicsItem.setFlags(QGraphicsItem.GraphicsItemFlags flags)'''
    def setFlag(self, flag, enabled = True):
        '''void QGraphicsItem.setFlag(QGraphicsItem.GraphicsItemFlag flag, bool enabled = True)'''
    def flags(self):
        '''QGraphicsItem.GraphicsItemFlags QGraphicsItem.flags()'''
        return QGraphicsItem.GraphicsItemFlags()
    def setGroup(self, group):
        '''void QGraphicsItem.setGroup(QGraphicsItemGroup group)'''
    def group(self):
        '''QGraphicsItemGroup QGraphicsItem.group()'''
        return QGraphicsItemGroup()
    def setParentItem(self, parent):
        '''void QGraphicsItem.setParentItem(QGraphicsItem parent)'''
    def topLevelItem(self):
        '''QGraphicsItem QGraphicsItem.topLevelItem()'''
        return QGraphicsItem()
    def parentItem(self):
        '''QGraphicsItem QGraphicsItem.parentItem()'''
        return QGraphicsItem()
    def scene(self):
        '''QGraphicsScene QGraphicsItem.scene()'''
        return QGraphicsScene()
    class GraphicsItemFlags():
        """"""
        def __init__(self):
            '''QGraphicsItem.GraphicsItemFlags QGraphicsItem.GraphicsItemFlags.__init__()'''
            return QGraphicsItem.GraphicsItemFlags()
        def __init__(self):
            '''int QGraphicsItem.GraphicsItemFlags.__init__()'''
            return int()
        def __init__(self):
            '''void QGraphicsItem.GraphicsItemFlags.__init__()'''
        def __bool__(self):
            '''int QGraphicsItem.GraphicsItemFlags.__bool__()'''
            return int()
        def __ne__(self, f):
            '''bool QGraphicsItem.GraphicsItemFlags.__ne__(QGraphicsItem.GraphicsItemFlags f)'''
            return bool()
        def __eq__(self, f):
            '''bool QGraphicsItem.GraphicsItemFlags.__eq__(QGraphicsItem.GraphicsItemFlags f)'''
            return bool()
        def __invert__(self):
            '''QGraphicsItem.GraphicsItemFlags QGraphicsItem.GraphicsItemFlags.__invert__()'''
            return QGraphicsItem.GraphicsItemFlags()
        def __and__(self, mask):
            '''QGraphicsItem.GraphicsItemFlags QGraphicsItem.GraphicsItemFlags.__and__(int mask)'''
            return QGraphicsItem.GraphicsItemFlags()
        def __xor__(self, f):
            '''QGraphicsItem.GraphicsItemFlags QGraphicsItem.GraphicsItemFlags.__xor__(QGraphicsItem.GraphicsItemFlags f)'''
            return QGraphicsItem.GraphicsItemFlags()
        def __xor__(self, f):
            '''QGraphicsItem.GraphicsItemFlags QGraphicsItem.GraphicsItemFlags.__xor__(int f)'''
            return QGraphicsItem.GraphicsItemFlags()
        def __or__(self, f):
            '''QGraphicsItem.GraphicsItemFlags QGraphicsItem.GraphicsItemFlags.__or__(QGraphicsItem.GraphicsItemFlags f)'''
            return QGraphicsItem.GraphicsItemFlags()
        def __or__(self, f):
            '''QGraphicsItem.GraphicsItemFlags QGraphicsItem.GraphicsItemFlags.__or__(int f)'''
            return QGraphicsItem.GraphicsItemFlags()
        def __int__(self):
            '''int QGraphicsItem.GraphicsItemFlags.__int__()'''
            return int()
        def __ixor__(self, f):
            '''QGraphicsItem.GraphicsItemFlags QGraphicsItem.GraphicsItemFlags.__ixor__(QGraphicsItem.GraphicsItemFlags f)'''
            return QGraphicsItem.GraphicsItemFlags()
        def __ior__(self, f):
            '''QGraphicsItem.GraphicsItemFlags QGraphicsItem.GraphicsItemFlags.__ior__(QGraphicsItem.GraphicsItemFlags f)'''
            return QGraphicsItem.GraphicsItemFlags()
        def __iand__(self, mask):
            '''QGraphicsItem.GraphicsItemFlags QGraphicsItem.GraphicsItemFlags.__iand__(int mask)'''
            return QGraphicsItem.GraphicsItemFlags()


class QAbstractGraphicsShapeItem(QGraphicsItem):
    """"""
    def __init__(self, parent = None):
        '''void QAbstractGraphicsShapeItem.__init__(QGraphicsItem parent = None)'''
    def opaqueArea(self):
        '''QPainterPath QAbstractGraphicsShapeItem.opaqueArea()'''
        return QPainterPath()
    def isObscuredBy(self, item):
        '''bool QAbstractGraphicsShapeItem.isObscuredBy(QGraphicsItem item)'''
        return bool()
    def setBrush(self, brush):
        '''void QAbstractGraphicsShapeItem.setBrush(QBrush brush)'''
    def brush(self):
        '''QBrush QAbstractGraphicsShapeItem.brush()'''
        return QBrush()
    def setPen(self, pen):
        '''void QAbstractGraphicsShapeItem.setPen(QPen pen)'''
    def pen(self):
        '''QPen QAbstractGraphicsShapeItem.pen()'''
        return QPen()


class QGraphicsPathItem(QAbstractGraphicsShapeItem):
    """"""
    def __init__(self, parent = None):
        '''void QGraphicsPathItem.__init__(QGraphicsItem parent = None)'''
    def __init__(self, path, parent = None):
        '''void QGraphicsPathItem.__init__(QPainterPath path, QGraphicsItem parent = None)'''
    def type(self):
        '''int QGraphicsPathItem.type()'''
        return int()
    def opaqueArea(self):
        '''QPainterPath QGraphicsPathItem.opaqueArea()'''
        return QPainterPath()
    def isObscuredBy(self, item):
        '''bool QGraphicsPathItem.isObscuredBy(QGraphicsItem item)'''
        return bool()
    def paint(self, painter, option, widget = None):
        '''void QGraphicsPathItem.paint(QPainter painter, QStyleOptionGraphicsItem option, QWidget widget = None)'''
    def contains(self, point):
        '''bool QGraphicsPathItem.contains(QPointF point)'''
        return bool()
    def shape(self):
        '''QPainterPath QGraphicsPathItem.shape()'''
        return QPainterPath()
    def boundingRect(self):
        '''QRectF QGraphicsPathItem.boundingRect()'''
        return QRectF()
    def setPath(self, path):
        '''void QGraphicsPathItem.setPath(QPainterPath path)'''
    def path(self):
        '''QPainterPath QGraphicsPathItem.path()'''
        return QPainterPath()


class QGraphicsRectItem(QAbstractGraphicsShapeItem):
    """"""
    def __init__(self, parent = None):
        '''void QGraphicsRectItem.__init__(QGraphicsItem parent = None)'''
    def __init__(self, rect, parent = None):
        '''void QGraphicsRectItem.__init__(QRectF rect, QGraphicsItem parent = None)'''
    def __init__(self, x, y, w, h, parent = None):
        '''void QGraphicsRectItem.__init__(float x, float y, float w, float h, QGraphicsItem parent = None)'''
    def type(self):
        '''int QGraphicsRectItem.type()'''
        return int()
    def opaqueArea(self):
        '''QPainterPath QGraphicsRectItem.opaqueArea()'''
        return QPainterPath()
    def isObscuredBy(self, item):
        '''bool QGraphicsRectItem.isObscuredBy(QGraphicsItem item)'''
        return bool()
    def paint(self, painter, option, widget = None):
        '''void QGraphicsRectItem.paint(QPainter painter, QStyleOptionGraphicsItem option, QWidget widget = None)'''
    def contains(self, point):
        '''bool QGraphicsRectItem.contains(QPointF point)'''
        return bool()
    def shape(self):
        '''QPainterPath QGraphicsRectItem.shape()'''
        return QPainterPath()
    def boundingRect(self):
        '''QRectF QGraphicsRectItem.boundingRect()'''
        return QRectF()
    def setRect(self, rect):
        '''void QGraphicsRectItem.setRect(QRectF rect)'''
    def setRect(self, ax, ay, w, h):
        '''void QGraphicsRectItem.setRect(float ax, float ay, float w, float h)'''
    def rect(self):
        '''QRectF QGraphicsRectItem.rect()'''
        return QRectF()


class QGraphicsEllipseItem(QAbstractGraphicsShapeItem):
    """"""
    def __init__(self, parent = None):
        '''void QGraphicsEllipseItem.__init__(QGraphicsItem parent = None)'''
    def __init__(self, rect, parent = None):
        '''void QGraphicsEllipseItem.__init__(QRectF rect, QGraphicsItem parent = None)'''
    def __init__(self, x, y, w, h, parent = None):
        '''void QGraphicsEllipseItem.__init__(float x, float y, float w, float h, QGraphicsItem parent = None)'''
    def type(self):
        '''int QGraphicsEllipseItem.type()'''
        return int()
    def opaqueArea(self):
        '''QPainterPath QGraphicsEllipseItem.opaqueArea()'''
        return QPainterPath()
    def isObscuredBy(self, item):
        '''bool QGraphicsEllipseItem.isObscuredBy(QGraphicsItem item)'''
        return bool()
    def paint(self, painter, option, widget = None):
        '''void QGraphicsEllipseItem.paint(QPainter painter, QStyleOptionGraphicsItem option, QWidget widget = None)'''
    def contains(self, point):
        '''bool QGraphicsEllipseItem.contains(QPointF point)'''
        return bool()
    def shape(self):
        '''QPainterPath QGraphicsEllipseItem.shape()'''
        return QPainterPath()
    def boundingRect(self):
        '''QRectF QGraphicsEllipseItem.boundingRect()'''
        return QRectF()
    def setSpanAngle(self, angle):
        '''void QGraphicsEllipseItem.setSpanAngle(int angle)'''
    def spanAngle(self):
        '''int QGraphicsEllipseItem.spanAngle()'''
        return int()
    def setStartAngle(self, angle):
        '''void QGraphicsEllipseItem.setStartAngle(int angle)'''
    def startAngle(self):
        '''int QGraphicsEllipseItem.startAngle()'''
        return int()
    def setRect(self, rect):
        '''void QGraphicsEllipseItem.setRect(QRectF rect)'''
    def setRect(self, ax, ay, w, h):
        '''void QGraphicsEllipseItem.setRect(float ax, float ay, float w, float h)'''
    def rect(self):
        '''QRectF QGraphicsEllipseItem.rect()'''
        return QRectF()


class QGraphicsPolygonItem(QAbstractGraphicsShapeItem):
    """"""
    def __init__(self, parent = None):
        '''void QGraphicsPolygonItem.__init__(QGraphicsItem parent = None)'''
    def __init__(self, polygon, parent = None):
        '''void QGraphicsPolygonItem.__init__(QPolygonF polygon, QGraphicsItem parent = None)'''
    def type(self):
        '''int QGraphicsPolygonItem.type()'''
        return int()
    def opaqueArea(self):
        '''QPainterPath QGraphicsPolygonItem.opaqueArea()'''
        return QPainterPath()
    def isObscuredBy(self, item):
        '''bool QGraphicsPolygonItem.isObscuredBy(QGraphicsItem item)'''
        return bool()
    def paint(self, painter, option, widget = None):
        '''void QGraphicsPolygonItem.paint(QPainter painter, QStyleOptionGraphicsItem option, QWidget widget = None)'''
    def contains(self, point):
        '''bool QGraphicsPolygonItem.contains(QPointF point)'''
        return bool()
    def shape(self):
        '''QPainterPath QGraphicsPolygonItem.shape()'''
        return QPainterPath()
    def boundingRect(self):
        '''QRectF QGraphicsPolygonItem.boundingRect()'''
        return QRectF()
    def setFillRule(self, rule):
        '''void QGraphicsPolygonItem.setFillRule(Qt.FillRule rule)'''
    def fillRule(self):
        '''Qt.FillRule QGraphicsPolygonItem.fillRule()'''
        return Qt.FillRule()
    def setPolygon(self, polygon):
        '''void QGraphicsPolygonItem.setPolygon(QPolygonF polygon)'''
    def polygon(self):
        '''QPolygonF QGraphicsPolygonItem.polygon()'''
        return QPolygonF()


class QGraphicsLineItem(QGraphicsItem):
    """"""
    def __init__(self, parent = None):
        '''void QGraphicsLineItem.__init__(QGraphicsItem parent = None)'''
    def __init__(self, line, parent = None):
        '''void QGraphicsLineItem.__init__(QLineF line, QGraphicsItem parent = None)'''
    def __init__(self, x1, y1, x2, y2, parent = None):
        '''void QGraphicsLineItem.__init__(float x1, float y1, float x2, float y2, QGraphicsItem parent = None)'''
    def type(self):
        '''int QGraphicsLineItem.type()'''
        return int()
    def opaqueArea(self):
        '''QPainterPath QGraphicsLineItem.opaqueArea()'''
        return QPainterPath()
    def isObscuredBy(self, item):
        '''bool QGraphicsLineItem.isObscuredBy(QGraphicsItem item)'''
        return bool()
    def paint(self, painter, option, widget = None):
        '''void QGraphicsLineItem.paint(QPainter painter, QStyleOptionGraphicsItem option, QWidget widget = None)'''
    def contains(self, point):
        '''bool QGraphicsLineItem.contains(QPointF point)'''
        return bool()
    def shape(self):
        '''QPainterPath QGraphicsLineItem.shape()'''
        return QPainterPath()
    def boundingRect(self):
        '''QRectF QGraphicsLineItem.boundingRect()'''
        return QRectF()
    def setLine(self, line):
        '''void QGraphicsLineItem.setLine(QLineF line)'''
    def setLine(self, x1, y1, x2, y2):
        '''void QGraphicsLineItem.setLine(float x1, float y1, float x2, float y2)'''
    def line(self):
        '''QLineF QGraphicsLineItem.line()'''
        return QLineF()
    def setPen(self, pen):
        '''void QGraphicsLineItem.setPen(QPen pen)'''
    def pen(self):
        '''QPen QGraphicsLineItem.pen()'''
        return QPen()


class QGraphicsPixmapItem(QGraphicsItem):
    """"""
    # Enum QGraphicsPixmapItem.ShapeMode
    MaskShape = 0
    BoundingRectShape = 0
    HeuristicMaskShape = 0

    def __init__(self, parent = None):
        '''void QGraphicsPixmapItem.__init__(QGraphicsItem parent = None)'''
    def __init__(self, pixmap, parent = None):
        '''void QGraphicsPixmapItem.__init__(QPixmap pixmap, QGraphicsItem parent = None)'''
    def setShapeMode(self, mode):
        '''void QGraphicsPixmapItem.setShapeMode(QGraphicsPixmapItem.ShapeMode mode)'''
    def shapeMode(self):
        '''QGraphicsPixmapItem.ShapeMode QGraphicsPixmapItem.shapeMode()'''
        return QGraphicsPixmapItem.ShapeMode()
    def type(self):
        '''int QGraphicsPixmapItem.type()'''
        return int()
    def opaqueArea(self):
        '''QPainterPath QGraphicsPixmapItem.opaqueArea()'''
        return QPainterPath()
    def isObscuredBy(self, item):
        '''bool QGraphicsPixmapItem.isObscuredBy(QGraphicsItem item)'''
        return bool()
    def paint(self, painter, option, widget):
        '''void QGraphicsPixmapItem.paint(QPainter painter, QStyleOptionGraphicsItem option, QWidget widget)'''
    def contains(self, point):
        '''bool QGraphicsPixmapItem.contains(QPointF point)'''
        return bool()
    def shape(self):
        '''QPainterPath QGraphicsPixmapItem.shape()'''
        return QPainterPath()
    def boundingRect(self):
        '''QRectF QGraphicsPixmapItem.boundingRect()'''
        return QRectF()
    def setOffset(self, offset):
        '''void QGraphicsPixmapItem.setOffset(QPointF offset)'''
    def setOffset(self, ax, ay):
        '''void QGraphicsPixmapItem.setOffset(float ax, float ay)'''
    def offset(self):
        '''QPointF QGraphicsPixmapItem.offset()'''
        return QPointF()
    def setTransformationMode(self, mode):
        '''void QGraphicsPixmapItem.setTransformationMode(Qt.TransformationMode mode)'''
    def transformationMode(self):
        '''Qt.TransformationMode QGraphicsPixmapItem.transformationMode()'''
        return Qt.TransformationMode()
    def setPixmap(self, pixmap):
        '''void QGraphicsPixmapItem.setPixmap(QPixmap pixmap)'''
    def pixmap(self):
        '''QPixmap QGraphicsPixmapItem.pixmap()'''
        return QPixmap()


class QGraphicsSimpleTextItem(QAbstractGraphicsShapeItem):
    """"""
    def __init__(self, parent = None):
        '''void QGraphicsSimpleTextItem.__init__(QGraphicsItem parent = None)'''
    def __init__(self, text, parent = None):
        '''void QGraphicsSimpleTextItem.__init__(str text, QGraphicsItem parent = None)'''
    def type(self):
        '''int QGraphicsSimpleTextItem.type()'''
        return int()
    def opaqueArea(self):
        '''QPainterPath QGraphicsSimpleTextItem.opaqueArea()'''
        return QPainterPath()
    def isObscuredBy(self, item):
        '''bool QGraphicsSimpleTextItem.isObscuredBy(QGraphicsItem item)'''
        return bool()
    def paint(self, painter, option, widget):
        '''void QGraphicsSimpleTextItem.paint(QPainter painter, QStyleOptionGraphicsItem option, QWidget widget)'''
    def contains(self, point):
        '''bool QGraphicsSimpleTextItem.contains(QPointF point)'''
        return bool()
    def shape(self):
        '''QPainterPath QGraphicsSimpleTextItem.shape()'''
        return QPainterPath()
    def boundingRect(self):
        '''QRectF QGraphicsSimpleTextItem.boundingRect()'''
        return QRectF()
    def font(self):
        '''QFont QGraphicsSimpleTextItem.font()'''
        return QFont()
    def setFont(self, font):
        '''void QGraphicsSimpleTextItem.setFont(QFont font)'''
    def text(self):
        '''str QGraphicsSimpleTextItem.text()'''
        return str()
    def setText(self, text):
        '''void QGraphicsSimpleTextItem.setText(str text)'''


class QGraphicsItemGroup(QGraphicsItem):
    """"""
    def __init__(self, parent = None):
        '''void QGraphicsItemGroup.__init__(QGraphicsItem parent = None)'''
    def type(self):
        '''int QGraphicsItemGroup.type()'''
        return int()
    def opaqueArea(self):
        '''QPainterPath QGraphicsItemGroup.opaqueArea()'''
        return QPainterPath()
    def isObscuredBy(self, item):
        '''bool QGraphicsItemGroup.isObscuredBy(QGraphicsItem item)'''
        return bool()
    def paint(self, painter, option, widget = None):
        '''void QGraphicsItemGroup.paint(QPainter painter, QStyleOptionGraphicsItem option, QWidget widget = None)'''
    def boundingRect(self):
        '''QRectF QGraphicsItemGroup.boundingRect()'''
        return QRectF()
    def removeFromGroup(self, item):
        '''void QGraphicsItemGroup.removeFromGroup(QGraphicsItem item)'''
    def addToGroup(self, item):
        '''void QGraphicsItemGroup.addToGroup(QGraphicsItem item)'''


class QGraphicsObject(QObject, QGraphicsItem):
    """"""
    def __init__(self, parent = None):
        '''void QGraphicsObject.__init__(QGraphicsItem parent = None)'''
    def event(self, ev):
        '''bool QGraphicsObject.event(QEvent ev)'''
        return bool()
    def updateMicroFocus(self):
        '''void QGraphicsObject.updateMicroFocus()'''
    scaleChanged = pyqtSignal() # void scaleChanged() - signal
    rotationChanged = pyqtSignal() # void rotationChanged() - signal
    zChanged = pyqtSignal() # void zChanged() - signal
    yChanged = pyqtSignal() # void yChanged() - signal
    xChanged = pyqtSignal() # void xChanged() - signal
    enabledChanged = pyqtSignal() # void enabledChanged() - signal
    visibleChanged = pyqtSignal() # void visibleChanged() - signal
    opacityChanged = pyqtSignal() # void opacityChanged() - signal
    parentChanged = pyqtSignal() # void parentChanged() - signal
    def ungrabGesture(self, type):
        '''void QGraphicsObject.ungrabGesture(Qt.GestureType type)'''
    def grabGesture(self, type, flags = None):
        '''void QGraphicsObject.grabGesture(Qt.GestureType type, Qt.GestureFlags flags = Qt.GestureFlags(0))'''


class QGraphicsTextItem(QGraphicsObject):
    """"""
    def __init__(self, parent = None):
        '''void QGraphicsTextItem.__init__(QGraphicsItem parent = None)'''
    def __init__(self, text, parent = None):
        '''void QGraphicsTextItem.__init__(str text, QGraphicsItem parent = None)'''
    def inputMethodQuery(self, query):
        '''QVariant QGraphicsTextItem.inputMethodQuery(Qt.InputMethodQuery query)'''
        return QVariant()
    def hoverLeaveEvent(self, event):
        '''void QGraphicsTextItem.hoverLeaveEvent(QGraphicsSceneHoverEvent event)'''
    def hoverMoveEvent(self, event):
        '''void QGraphicsTextItem.hoverMoveEvent(QGraphicsSceneHoverEvent event)'''
    def hoverEnterEvent(self, event):
        '''void QGraphicsTextItem.hoverEnterEvent(QGraphicsSceneHoverEvent event)'''
    def inputMethodEvent(self, event):
        '''void QGraphicsTextItem.inputMethodEvent(QInputMethodEvent event)'''
    def dropEvent(self, event):
        '''void QGraphicsTextItem.dropEvent(QGraphicsSceneDragDropEvent event)'''
    def dragMoveEvent(self, event):
        '''void QGraphicsTextItem.dragMoveEvent(QGraphicsSceneDragDropEvent event)'''
    def dragLeaveEvent(self, event):
        '''void QGraphicsTextItem.dragLeaveEvent(QGraphicsSceneDragDropEvent event)'''
    def dragEnterEvent(self, event):
        '''void QGraphicsTextItem.dragEnterEvent(QGraphicsSceneDragDropEvent event)'''
    def focusOutEvent(self, event):
        '''void QGraphicsTextItem.focusOutEvent(QFocusEvent event)'''
    def focusInEvent(self, event):
        '''void QGraphicsTextItem.focusInEvent(QFocusEvent event)'''
    def keyReleaseEvent(self, event):
        '''void QGraphicsTextItem.keyReleaseEvent(QKeyEvent event)'''
    def keyPressEvent(self, event):
        '''void QGraphicsTextItem.keyPressEvent(QKeyEvent event)'''
    def contextMenuEvent(self, event):
        '''void QGraphicsTextItem.contextMenuEvent(QGraphicsSceneContextMenuEvent event)'''
    def mouseDoubleClickEvent(self, event):
        '''void QGraphicsTextItem.mouseDoubleClickEvent(QGraphicsSceneMouseEvent event)'''
    def mouseReleaseEvent(self, event):
        '''void QGraphicsTextItem.mouseReleaseEvent(QGraphicsSceneMouseEvent event)'''
    def mouseMoveEvent(self, event):
        '''void QGraphicsTextItem.mouseMoveEvent(QGraphicsSceneMouseEvent event)'''
    def mousePressEvent(self, event):
        '''void QGraphicsTextItem.mousePressEvent(QGraphicsSceneMouseEvent event)'''
    def sceneEvent(self, event):
        '''bool QGraphicsTextItem.sceneEvent(QEvent event)'''
        return bool()
    linkHovered = pyqtSignal() # void linkHovered(const QStringamp;) - signal
    linkActivated = pyqtSignal() # void linkActivated(const QStringamp;) - signal
    def textCursor(self):
        '''QTextCursor QGraphicsTextItem.textCursor()'''
        return QTextCursor()
    def setTextCursor(self, cursor):
        '''void QGraphicsTextItem.setTextCursor(QTextCursor cursor)'''
    def openExternalLinks(self):
        '''bool QGraphicsTextItem.openExternalLinks()'''
        return bool()
    def setOpenExternalLinks(self, open):
        '''void QGraphicsTextItem.setOpenExternalLinks(bool open)'''
    def tabChangesFocus(self):
        '''bool QGraphicsTextItem.tabChangesFocus()'''
        return bool()
    def setTabChangesFocus(self, b):
        '''void QGraphicsTextItem.setTabChangesFocus(bool b)'''
    def textInteractionFlags(self):
        '''Qt.TextInteractionFlags QGraphicsTextItem.textInteractionFlags()'''
        return Qt.TextInteractionFlags()
    def setTextInteractionFlags(self, flags):
        '''void QGraphicsTextItem.setTextInteractionFlags(Qt.TextInteractionFlags flags)'''
    def document(self):
        '''QTextDocument QGraphicsTextItem.document()'''
        return QTextDocument()
    def setDocument(self, document):
        '''void QGraphicsTextItem.setDocument(QTextDocument document)'''
    def adjustSize(self):
        '''void QGraphicsTextItem.adjustSize()'''
    def textWidth(self):
        '''float QGraphicsTextItem.textWidth()'''
        return float()
    def setTextWidth(self, width):
        '''void QGraphicsTextItem.setTextWidth(float width)'''
    def type(self):
        '''int QGraphicsTextItem.type()'''
        return int()
    def opaqueArea(self):
        '''QPainterPath QGraphicsTextItem.opaqueArea()'''
        return QPainterPath()
    def isObscuredBy(self, item):
        '''bool QGraphicsTextItem.isObscuredBy(QGraphicsItem item)'''
        return bool()
    def paint(self, painter, option, widget):
        '''void QGraphicsTextItem.paint(QPainter painter, QStyleOptionGraphicsItem option, QWidget widget)'''
    def contains(self, point):
        '''bool QGraphicsTextItem.contains(QPointF point)'''
        return bool()
    def shape(self):
        '''QPainterPath QGraphicsTextItem.shape()'''
        return QPainterPath()
    def boundingRect(self):
        '''QRectF QGraphicsTextItem.boundingRect()'''
        return QRectF()
    def defaultTextColor(self):
        '''QColor QGraphicsTextItem.defaultTextColor()'''
        return QColor()
    def setDefaultTextColor(self, c):
        '''void QGraphicsTextItem.setDefaultTextColor(QColor c)'''
    def setFont(self, font):
        '''void QGraphicsTextItem.setFont(QFont font)'''
    def font(self):
        '''QFont QGraphicsTextItem.font()'''
        return QFont()
    def setPlainText(self, text):
        '''void QGraphicsTextItem.setPlainText(str text)'''
    def toPlainText(self):
        '''str QGraphicsTextItem.toPlainText()'''
        return str()
    def setHtml(self, html):
        '''void QGraphicsTextItem.setHtml(str html)'''
    def toHtml(self):
        '''str QGraphicsTextItem.toHtml()'''
        return str()


class QGraphicsLinearLayout(QGraphicsLayout):
    """"""
    def __init__(self, parent = None):
        '''void QGraphicsLinearLayout.__init__(QGraphicsLayoutItem parent = None)'''
    def __init__(self, orientation, parent = None):
        '''void QGraphicsLinearLayout.__init__(Qt.Orientation orientation, QGraphicsLayoutItem parent = None)'''
    def sizeHint(self, which, constraint = QSizeF()):
        '''QSizeF QGraphicsLinearLayout.sizeHint(Qt.SizeHint which, QSizeF constraint = QSizeF())'''
        return QSizeF()
    def invalidate(self):
        '''void QGraphicsLinearLayout.invalidate()'''
    def itemAt(self, index):
        '''QGraphicsLayoutItem QGraphicsLinearLayout.itemAt(int index)'''
        return QGraphicsLayoutItem()
    def count(self):
        '''int QGraphicsLinearLayout.count()'''
        return int()
    def setGeometry(self, rect):
        '''void QGraphicsLinearLayout.setGeometry(QRectF rect)'''
    def alignment(self, item):
        '''Qt.Alignment QGraphicsLinearLayout.alignment(QGraphicsLayoutItem item)'''
        return Qt.Alignment()
    def setAlignment(self, item, alignment):
        '''void QGraphicsLinearLayout.setAlignment(QGraphicsLayoutItem item, Qt.Alignment alignment)'''
    def stretchFactor(self, item):
        '''int QGraphicsLinearLayout.stretchFactor(QGraphicsLayoutItem item)'''
        return int()
    def setStretchFactor(self, item, stretch):
        '''void QGraphicsLinearLayout.setStretchFactor(QGraphicsLayoutItem item, int stretch)'''
    def itemSpacing(self, index):
        '''float QGraphicsLinearLayout.itemSpacing(int index)'''
        return float()
    def setItemSpacing(self, index, spacing):
        '''void QGraphicsLinearLayout.setItemSpacing(int index, float spacing)'''
    def spacing(self):
        '''float QGraphicsLinearLayout.spacing()'''
        return float()
    def setSpacing(self, spacing):
        '''void QGraphicsLinearLayout.setSpacing(float spacing)'''
    def removeAt(self, index):
        '''void QGraphicsLinearLayout.removeAt(int index)'''
    def removeItem(self, item):
        '''void QGraphicsLinearLayout.removeItem(QGraphicsLayoutItem item)'''
    def insertStretch(self, index, stretch = 1):
        '''void QGraphicsLinearLayout.insertStretch(int index, int stretch = 1)'''
    def insertItem(self, index, item):
        '''void QGraphicsLinearLayout.insertItem(int index, QGraphicsLayoutItem item)'''
    def addStretch(self, stretch = 1):
        '''void QGraphicsLinearLayout.addStretch(int stretch = 1)'''
    def addItem(self, item):
        '''void QGraphicsLinearLayout.addItem(QGraphicsLayoutItem item)'''
    def orientation(self):
        '''Qt.Orientation QGraphicsLinearLayout.orientation()'''
        return Qt.Orientation()
    def setOrientation(self, orientation):
        '''void QGraphicsLinearLayout.setOrientation(Qt.Orientation orientation)'''


class QGraphicsWidget(QGraphicsObject, QGraphicsLayoutItem):
    """"""
    def __init__(self, parent = None, flags = 0):
        '''void QGraphicsWidget.__init__(QGraphicsItem parent = None, Qt.WindowFlags flags = 0)'''
    geometryChanged = pyqtSignal() # void geometryChanged() - signal
    def setAutoFillBackground(self, enabled):
        '''void QGraphicsWidget.setAutoFillBackground(bool enabled)'''
    def autoFillBackground(self):
        '''bool QGraphicsWidget.autoFillBackground()'''
        return bool()
    def ungrabKeyboardEvent(self, event):
        '''void QGraphicsWidget.ungrabKeyboardEvent(QEvent event)'''
    def grabKeyboardEvent(self, event):
        '''void QGraphicsWidget.grabKeyboardEvent(QEvent event)'''
    def ungrabMouseEvent(self, event):
        '''void QGraphicsWidget.ungrabMouseEvent(QEvent event)'''
    def grabMouseEvent(self, event):
        '''void QGraphicsWidget.grabMouseEvent(QEvent event)'''
    def hoverLeaveEvent(self, event):
        '''void QGraphicsWidget.hoverLeaveEvent(QGraphicsSceneHoverEvent event)'''
    def hoverMoveEvent(self, event):
        '''void QGraphicsWidget.hoverMoveEvent(QGraphicsSceneHoverEvent event)'''
    def showEvent(self, event):
        '''void QGraphicsWidget.showEvent(QShowEvent event)'''
    def resizeEvent(self, event):
        '''void QGraphicsWidget.resizeEvent(QGraphicsSceneResizeEvent event)'''
    def polishEvent(self):
        '''void QGraphicsWidget.polishEvent()'''
    def moveEvent(self, event):
        '''void QGraphicsWidget.moveEvent(QGraphicsSceneMoveEvent event)'''
    def hideEvent(self, event):
        '''void QGraphicsWidget.hideEvent(QHideEvent event)'''
    def focusOutEvent(self, event):
        '''void QGraphicsWidget.focusOutEvent(QFocusEvent event)'''
    def focusNextPrevChild(self, next):
        '''bool QGraphicsWidget.focusNextPrevChild(bool next)'''
        return bool()
    def focusInEvent(self, event):
        '''void QGraphicsWidget.focusInEvent(QFocusEvent event)'''
    def closeEvent(self, event):
        '''void QGraphicsWidget.closeEvent(QCloseEvent event)'''
    def changeEvent(self, event):
        '''void QGraphicsWidget.changeEvent(QEvent event)'''
    def event(self, event):
        '''bool QGraphicsWidget.event(QEvent event)'''
        return bool()
    def windowFrameSectionAt(self, pos):
        '''Qt.WindowFrameSection QGraphicsWidget.windowFrameSectionAt(QPointF pos)'''
        return Qt.WindowFrameSection()
    def windowFrameEvent(self, e):
        '''bool QGraphicsWidget.windowFrameEvent(QEvent e)'''
        return bool()
    def sceneEvent(self, event):
        '''bool QGraphicsWidget.sceneEvent(QEvent event)'''
        return bool()
    def itemChange(self, change, value):
        '''QVariant QGraphicsWidget.itemChange(QGraphicsItem.GraphicsItemChange change, QVariant value)'''
        return QVariant()
    def updateGeometry(self):
        '''void QGraphicsWidget.updateGeometry()'''
    def sizeHint(self, which, constraint = QSizeF()):
        '''QSizeF QGraphicsWidget.sizeHint(Qt.SizeHint which, QSizeF constraint = QSizeF())'''
        return QSizeF()
    def initStyleOption(self, option):
        '''void QGraphicsWidget.initStyleOption(QStyleOption option)'''
    def close(self):
        '''bool QGraphicsWidget.close()'''
        return bool()
    def shape(self):
        '''QPainterPath QGraphicsWidget.shape()'''
        return QPainterPath()
    def boundingRect(self):
        '''QRectF QGraphicsWidget.boundingRect()'''
        return QRectF()
    def paintWindowFrame(self, painter, option, widget = None):
        '''void QGraphicsWidget.paintWindowFrame(QPainter painter, QStyleOptionGraphicsItem option, QWidget widget = None)'''
    def paint(self, painter, option, widget = None):
        '''void QGraphicsWidget.paint(QPainter painter, QStyleOptionGraphicsItem option, QWidget widget = None)'''
    def type(self):
        '''int QGraphicsWidget.type()'''
        return int()
    def testAttribute(self, attribute):
        '''bool QGraphicsWidget.testAttribute(Qt.WidgetAttribute attribute)'''
        return bool()
    def setAttribute(self, attribute, on = True):
        '''void QGraphicsWidget.setAttribute(Qt.WidgetAttribute attribute, bool on = True)'''
    def actions(self):
        '''list-of-QAction QGraphicsWidget.actions()'''
        return [QAction()]
    def removeAction(self, action):
        '''void QGraphicsWidget.removeAction(QAction action)'''
    def insertActions(self, before, actions):
        '''void QGraphicsWidget.insertActions(QAction before, list-of-QAction actions)'''
    def insertAction(self, before, action):
        '''void QGraphicsWidget.insertAction(QAction before, QAction action)'''
    def addActions(self, actions):
        '''void QGraphicsWidget.addActions(list-of-QAction actions)'''
    def addAction(self, action):
        '''void QGraphicsWidget.addAction(QAction action)'''
    def setShortcutAutoRepeat(self, id, enabled = True):
        '''void QGraphicsWidget.setShortcutAutoRepeat(int id, bool enabled = True)'''
    def setShortcutEnabled(self, id, enabled = True):
        '''void QGraphicsWidget.setShortcutEnabled(int id, bool enabled = True)'''
    def releaseShortcut(self, id):
        '''void QGraphicsWidget.releaseShortcut(int id)'''
    def grabShortcut(self, sequence, context = None):
        '''int QGraphicsWidget.grabShortcut(QKeySequence sequence, Qt.ShortcutContext context = Qt.WindowShortcut)'''
        return int()
    def focusWidget(self):
        '''QGraphicsWidget QGraphicsWidget.focusWidget()'''
        return QGraphicsWidget()
    def setTabOrder(self, first, second):
        '''static void QGraphicsWidget.setTabOrder(QGraphicsWidget first, QGraphicsWidget second)'''
    def setFocusPolicy(self, policy):
        '''void QGraphicsWidget.setFocusPolicy(Qt.FocusPolicy policy)'''
    def focusPolicy(self):
        '''Qt.FocusPolicy QGraphicsWidget.focusPolicy()'''
        return Qt.FocusPolicy()
    def windowTitle(self):
        '''str QGraphicsWidget.windowTitle()'''
        return str()
    def setWindowTitle(self, title):
        '''void QGraphicsWidget.setWindowTitle(str title)'''
    def isActiveWindow(self):
        '''bool QGraphicsWidget.isActiveWindow()'''
        return bool()
    def setWindowFlags(self, wFlags):
        '''void QGraphicsWidget.setWindowFlags(Qt.WindowFlags wFlags)'''
    def windowType(self):
        '''Qt.WindowType QGraphicsWidget.windowType()'''
        return Qt.WindowType()
    def windowFlags(self):
        '''Qt.WindowFlags QGraphicsWidget.windowFlags()'''
        return Qt.WindowFlags()
    def windowFrameRect(self):
        '''QRectF QGraphicsWidget.windowFrameRect()'''
        return QRectF()
    def windowFrameGeometry(self):
        '''QRectF QGraphicsWidget.windowFrameGeometry()'''
        return QRectF()
    def unsetWindowFrameMargins(self):
        '''void QGraphicsWidget.unsetWindowFrameMargins()'''
    def getWindowFrameMargins(self, left, top, right, bottom):
        '''void QGraphicsWidget.getWindowFrameMargins(float left, float top, float right, float bottom)'''
    def setWindowFrameMargins(self, left, top, right, bottom):
        '''void QGraphicsWidget.setWindowFrameMargins(float left, float top, float right, float bottom)'''
    def getContentsMargins(self, left, top, right, bottom):
        '''void QGraphicsWidget.getContentsMargins(float left, float top, float right, float bottom)'''
    def setContentsMargins(self, left, top, right, bottom):
        '''void QGraphicsWidget.setContentsMargins(float left, float top, float right, float bottom)'''
    def rect(self):
        '''QRectF QGraphicsWidget.rect()'''
        return QRectF()
    def setGeometry(self, rect):
        '''void QGraphicsWidget.setGeometry(QRectF rect)'''
    def setGeometry(self, ax, ay, aw, ah):
        '''void QGraphicsWidget.setGeometry(float ax, float ay, float aw, float ah)'''
    def size(self):
        '''QSizeF QGraphicsWidget.size()'''
        return QSizeF()
    def resize(self, size):
        '''void QGraphicsWidget.resize(QSizeF size)'''
    def resize(self, w, h):
        '''void QGraphicsWidget.resize(float w, float h)'''
    def setPalette(self, palette):
        '''void QGraphicsWidget.setPalette(QPalette palette)'''
    def palette(self):
        '''QPalette QGraphicsWidget.palette()'''
        return QPalette()
    def setFont(self, font):
        '''void QGraphicsWidget.setFont(QFont font)'''
    def font(self):
        '''QFont QGraphicsWidget.font()'''
        return QFont()
    def setStyle(self, style):
        '''void QGraphicsWidget.setStyle(QStyle style)'''
    def style(self):
        '''QStyle QGraphicsWidget.style()'''
        return QStyle()
    def unsetLayoutDirection(self):
        '''void QGraphicsWidget.unsetLayoutDirection()'''
    def setLayoutDirection(self, direction):
        '''void QGraphicsWidget.setLayoutDirection(Qt.LayoutDirection direction)'''
    def layoutDirection(self):
        '''Qt.LayoutDirection QGraphicsWidget.layoutDirection()'''
        return Qt.LayoutDirection()
    def adjustSize(self):
        '''void QGraphicsWidget.adjustSize()'''
    def setLayout(self, layout):
        '''void QGraphicsWidget.setLayout(QGraphicsLayout layout)'''
    def layout(self):
        '''QGraphicsLayout QGraphicsWidget.layout()'''
        return QGraphicsLayout()


class QGraphicsProxyWidget(QGraphicsWidget):
    """"""
    def __init__(self, parent = None, flags = 0):
        '''void QGraphicsProxyWidget.__init__(QGraphicsItem parent = None, Qt.WindowFlags flags = 0)'''
    def inputMethodEvent(self, event):
        '''void QGraphicsProxyWidget.inputMethodEvent(QInputMethodEvent event)'''
    def inputMethodQuery(self, query):
        '''QVariant QGraphicsProxyWidget.inputMethodQuery(Qt.InputMethodQuery query)'''
        return QVariant()
    def newProxyWidget(self):
        '''QWidget QGraphicsProxyWidget.newProxyWidget()'''
        return QWidget()
    def dropEvent(self, event):
        '''void QGraphicsProxyWidget.dropEvent(QGraphicsSceneDragDropEvent event)'''
    def dragMoveEvent(self, event):
        '''void QGraphicsProxyWidget.dragMoveEvent(QGraphicsSceneDragDropEvent event)'''
    def dragLeaveEvent(self, event):
        '''void QGraphicsProxyWidget.dragLeaveEvent(QGraphicsSceneDragDropEvent event)'''
    def dragEnterEvent(self, event):
        '''void QGraphicsProxyWidget.dragEnterEvent(QGraphicsSceneDragDropEvent event)'''
    def resizeEvent(self, event):
        '''void QGraphicsProxyWidget.resizeEvent(QGraphicsSceneResizeEvent event)'''
    def sizeHint(self, which, constraint = QSizeF()):
        '''QSizeF QGraphicsProxyWidget.sizeHint(Qt.SizeHint which, QSizeF constraint = QSizeF())'''
        return QSizeF()
    def focusNextPrevChild(self, next):
        '''bool QGraphicsProxyWidget.focusNextPrevChild(bool next)'''
        return bool()
    def focusOutEvent(self, event):
        '''void QGraphicsProxyWidget.focusOutEvent(QFocusEvent event)'''
    def focusInEvent(self, event):
        '''void QGraphicsProxyWidget.focusInEvent(QFocusEvent event)'''
    def keyReleaseEvent(self, event):
        '''void QGraphicsProxyWidget.keyReleaseEvent(QKeyEvent event)'''
    def keyPressEvent(self, event):
        '''void QGraphicsProxyWidget.keyPressEvent(QKeyEvent event)'''
    def wheelEvent(self, event):
        '''void QGraphicsProxyWidget.wheelEvent(QGraphicsSceneWheelEvent event)'''
    def mouseDoubleClickEvent(self, event):
        '''void QGraphicsProxyWidget.mouseDoubleClickEvent(QGraphicsSceneMouseEvent event)'''
    def mouseReleaseEvent(self, event):
        '''void QGraphicsProxyWidget.mouseReleaseEvent(QGraphicsSceneMouseEvent event)'''
    def mousePressEvent(self, event):
        '''void QGraphicsProxyWidget.mousePressEvent(QGraphicsSceneMouseEvent event)'''
    def mouseMoveEvent(self, event):
        '''void QGraphicsProxyWidget.mouseMoveEvent(QGraphicsSceneMouseEvent event)'''
    def ungrabMouseEvent(self, event):
        '''void QGraphicsProxyWidget.ungrabMouseEvent(QEvent event)'''
    def grabMouseEvent(self, event):
        '''void QGraphicsProxyWidget.grabMouseEvent(QEvent event)'''
    def hoverMoveEvent(self, event):
        '''void QGraphicsProxyWidget.hoverMoveEvent(QGraphicsSceneHoverEvent event)'''
    def hoverLeaveEvent(self, event):
        '''void QGraphicsProxyWidget.hoverLeaveEvent(QGraphicsSceneHoverEvent event)'''
    def hoverEnterEvent(self, event):
        '''void QGraphicsProxyWidget.hoverEnterEvent(QGraphicsSceneHoverEvent event)'''
    def contextMenuEvent(self, event):
        '''void QGraphicsProxyWidget.contextMenuEvent(QGraphicsSceneContextMenuEvent event)'''
    def hideEvent(self, event):
        '''void QGraphicsProxyWidget.hideEvent(QHideEvent event)'''
    def showEvent(self, event):
        '''void QGraphicsProxyWidget.showEvent(QShowEvent event)'''
    def eventFilter(self, object, event):
        '''bool QGraphicsProxyWidget.eventFilter(QObject object, QEvent event)'''
        return bool()
    def event(self, event):
        '''bool QGraphicsProxyWidget.event(QEvent event)'''
        return bool()
    def itemChange(self, change, value):
        '''QVariant QGraphicsProxyWidget.itemChange(QGraphicsItem.GraphicsItemChange change, QVariant value)'''
        return QVariant()
    def createProxyForChildWidget(self, child):
        '''QGraphicsProxyWidget QGraphicsProxyWidget.createProxyForChildWidget(QWidget child)'''
        return QGraphicsProxyWidget()
    def type(self):
        '''int QGraphicsProxyWidget.type()'''
        return int()
    def paint(self, painter, option, widget):
        '''void QGraphicsProxyWidget.paint(QPainter painter, QStyleOptionGraphicsItem option, QWidget widget)'''
    def setGeometry(self, rect):
        '''void QGraphicsProxyWidget.setGeometry(QRectF rect)'''
    def subWidgetRect(self, widget):
        '''QRectF QGraphicsProxyWidget.subWidgetRect(QWidget widget)'''
        return QRectF()
    def widget(self):
        '''QWidget QGraphicsProxyWidget.widget()'''
        return QWidget()
    def setWidget(self, widget):
        '''void QGraphicsProxyWidget.setWidget(QWidget widget)'''


class QGraphicsScene(QObject):
    """"""
    # Enum QGraphicsScene.SceneLayer
    ItemLayer = 0
    BackgroundLayer = 0
    ForegroundLayer = 0
    AllLayers = 0

    # Enum QGraphicsScene.ItemIndexMethod
    BspTreeIndex = 0
    NoIndex = 0

    def __init__(self, parent = None):
        '''void QGraphicsScene.__init__(QObject parent = None)'''
    def __init__(self, sceneRect, parent = None):
        '''void QGraphicsScene.__init__(QRectF sceneRect, QObject parent = None)'''
    def __init__(self, x, y, width, height, parent = None):
        '''void QGraphicsScene.__init__(float x, float y, float width, float height, QObject parent = None)'''
    focusItemChanged = pyqtSignal() # void focusItemChanged(QGraphicsItem*,QGraphicsItem*,Qt::FocusReason) - signal
    def setMinimumRenderSize(self, minSize):
        '''void QGraphicsScene.setMinimumRenderSize(float minSize)'''
    def minimumRenderSize(self):
        '''float QGraphicsScene.minimumRenderSize()'''
        return float()
    def sendEvent(self, item, event):
        '''bool QGraphicsScene.sendEvent(QGraphicsItem item, QEvent event)'''
        return bool()
    def setActivePanel(self, item):
        '''void QGraphicsScene.setActivePanel(QGraphicsItem item)'''
    def activePanel(self):
        '''QGraphicsItem QGraphicsScene.activePanel()'''
        return QGraphicsItem()
    def isActive(self):
        '''bool QGraphicsScene.isActive()'''
        return bool()
    def itemAt(self, pos, deviceTransform):
        '''QGraphicsItem QGraphicsScene.itemAt(QPointF pos, QTransform deviceTransform)'''
        return QGraphicsItem()
    def itemAt(self, x, y, deviceTransform):
        '''QGraphicsItem QGraphicsScene.itemAt(float x, float y, QTransform deviceTransform)'''
        return QGraphicsItem()
    def stickyFocus(self):
        '''bool QGraphicsScene.stickyFocus()'''
        return bool()
    def setStickyFocus(self, enabled):
        '''void QGraphicsScene.setStickyFocus(bool enabled)'''
    def focusNextPrevChild(self, next):
        '''bool QGraphicsScene.focusNextPrevChild(bool next)'''
        return bool()
    def eventFilter(self, watched, event):
        '''bool QGraphicsScene.eventFilter(QObject watched, QEvent event)'''
        return bool()
    def setActiveWindow(self, widget):
        '''void QGraphicsScene.setActiveWindow(QGraphicsWidget widget)'''
    def activeWindow(self):
        '''QGraphicsWidget QGraphicsScene.activeWindow()'''
        return QGraphicsWidget()
    def setPalette(self, palette):
        '''void QGraphicsScene.setPalette(QPalette palette)'''
    def palette(self):
        '''QPalette QGraphicsScene.palette()'''
        return QPalette()
    def setFont(self, font):
        '''void QGraphicsScene.setFont(QFont font)'''
    def font(self):
        '''QFont QGraphicsScene.font()'''
        return QFont()
    def setStyle(self, style):
        '''void QGraphicsScene.setStyle(QStyle style)'''
    def style(self):
        '''QStyle QGraphicsScene.style()'''
        return QStyle()
    def addWidget(self, widget, flags = 0):
        '''QGraphicsProxyWidget QGraphicsScene.addWidget(QWidget widget, Qt.WindowFlags flags = 0)'''
        return QGraphicsProxyWidget()
    def selectionArea(self):
        '''QPainterPath QGraphicsScene.selectionArea()'''
        return QPainterPath()
    def setBspTreeDepth(self, depth):
        '''void QGraphicsScene.setBspTreeDepth(int depth)'''
    def bspTreeDepth(self):
        '''int QGraphicsScene.bspTreeDepth()'''
        return int()
    def drawForeground(self, painter, rect):
        '''void QGraphicsScene.drawForeground(QPainter painter, QRectF rect)'''
    def drawBackground(self, painter, rect):
        '''void QGraphicsScene.drawBackground(QPainter painter, QRectF rect)'''
    def inputMethodEvent(self, event):
        '''void QGraphicsScene.inputMethodEvent(QInputMethodEvent event)'''
    def wheelEvent(self, event):
        '''void QGraphicsScene.wheelEvent(QGraphicsSceneWheelEvent event)'''
    def mouseDoubleClickEvent(self, event):
        '''void QGraphicsScene.mouseDoubleClickEvent(QGraphicsSceneMouseEvent event)'''
    def mouseReleaseEvent(self, event):
        '''void QGraphicsScene.mouseReleaseEvent(QGraphicsSceneMouseEvent event)'''
    def mouseMoveEvent(self, event):
        '''void QGraphicsScene.mouseMoveEvent(QGraphicsSceneMouseEvent event)'''
    def mousePressEvent(self, event):
        '''void QGraphicsScene.mousePressEvent(QGraphicsSceneMouseEvent event)'''
    def keyReleaseEvent(self, event):
        '''void QGraphicsScene.keyReleaseEvent(QKeyEvent event)'''
    def keyPressEvent(self, event):
        '''void QGraphicsScene.keyPressEvent(QKeyEvent event)'''
    def helpEvent(self, event):
        '''void QGraphicsScene.helpEvent(QGraphicsSceneHelpEvent event)'''
    def focusOutEvent(self, event):
        '''void QGraphicsScene.focusOutEvent(QFocusEvent event)'''
    def focusInEvent(self, event):
        '''void QGraphicsScene.focusInEvent(QFocusEvent event)'''
    def dropEvent(self, event):
        '''void QGraphicsScene.dropEvent(QGraphicsSceneDragDropEvent event)'''
    def dragLeaveEvent(self, event):
        '''void QGraphicsScene.dragLeaveEvent(QGraphicsSceneDragDropEvent event)'''
    def dragMoveEvent(self, event):
        '''void QGraphicsScene.dragMoveEvent(QGraphicsSceneDragDropEvent event)'''
    def dragEnterEvent(self, event):
        '''void QGraphicsScene.dragEnterEvent(QGraphicsSceneDragDropEvent event)'''
    def contextMenuEvent(self, event):
        '''void QGraphicsScene.contextMenuEvent(QGraphicsSceneContextMenuEvent event)'''
    def event(self, event):
        '''bool QGraphicsScene.event(QEvent event)'''
        return bool()
    selectionChanged = pyqtSignal() # void selectionChanged() - signal
    sceneRectChanged = pyqtSignal() # void sceneRectChanged(const QRectFamp;) - signal
    changed = pyqtSignal() # void changed(const QListlt;QRectFgt;amp;) - signal
    def clear(self):
        '''void QGraphicsScene.clear()'''
    def invalidate(self, rect = QRectF(), layers = None):
        '''void QGraphicsScene.invalidate(QRectF rect = QRectF(), QGraphicsScene.SceneLayers layers = QGraphicsScene.AllLayers)'''
    def invalidate(self, x, y, w, h, layers = None):
        '''void QGraphicsScene.invalidate(float x, float y, float w, float h, QGraphicsScene.SceneLayers layers = QGraphicsScene.AllLayers)'''
    def update(self, rect = QRectF()):
        '''void QGraphicsScene.update(QRectF rect = QRectF())'''
    def update(self, x, y, w, h):
        '''void QGraphicsScene.update(float x, float y, float w, float h)'''
    def advance(self):
        '''void QGraphicsScene.advance()'''
    def views(self):
        '''list-of-QGraphicsView QGraphicsScene.views()'''
        return [QGraphicsView()]
    def inputMethodQuery(self, query):
        '''QVariant QGraphicsScene.inputMethodQuery(Qt.InputMethodQuery query)'''
        return QVariant()
    def setForegroundBrush(self, brush):
        '''void QGraphicsScene.setForegroundBrush(QBrush brush)'''
    def foregroundBrush(self):
        '''QBrush QGraphicsScene.foregroundBrush()'''
        return QBrush()
    def setBackgroundBrush(self, brush):
        '''void QGraphicsScene.setBackgroundBrush(QBrush brush)'''
    def backgroundBrush(self):
        '''QBrush QGraphicsScene.backgroundBrush()'''
        return QBrush()
    def mouseGrabberItem(self):
        '''QGraphicsItem QGraphicsScene.mouseGrabberItem()'''
        return QGraphicsItem()
    def clearFocus(self):
        '''void QGraphicsScene.clearFocus()'''
    def setFocus(self, focusReason = None):
        '''void QGraphicsScene.setFocus(Qt.FocusReason focusReason = Qt.OtherFocusReason)'''
    def hasFocus(self):
        '''bool QGraphicsScene.hasFocus()'''
        return bool()
    def setFocusItem(self, item, focusReason = None):
        '''void QGraphicsScene.setFocusItem(QGraphicsItem item, Qt.FocusReason focusReason = Qt.OtherFocusReason)'''
    def focusItem(self):
        '''QGraphicsItem QGraphicsScene.focusItem()'''
        return QGraphicsItem()
    def removeItem(self, item):
        '''void QGraphicsScene.removeItem(QGraphicsItem item)'''
    def addText(self, text, font = QFont()):
        '''QGraphicsTextItem QGraphicsScene.addText(str text, QFont font = QFont())'''
        return QGraphicsTextItem()
    def addSimpleText(self, text, font = QFont()):
        '''QGraphicsSimpleTextItem QGraphicsScene.addSimpleText(str text, QFont font = QFont())'''
        return QGraphicsSimpleTextItem()
    def addRect(self, rect, pen = QPen(), brush = QBrush()):
        '''QGraphicsRectItem QGraphicsScene.addRect(QRectF rect, QPen pen = QPen(), QBrush brush = QBrush())'''
        return QGraphicsRectItem()
    def addRect(self, x, y, w, h, pen = QPen(), brush = QBrush()):
        '''QGraphicsRectItem QGraphicsScene.addRect(float x, float y, float w, float h, QPen pen = QPen(), QBrush brush = QBrush())'''
        return QGraphicsRectItem()
    def addPolygon(self, polygon, pen = QPen(), brush = QBrush()):
        '''QGraphicsPolygonItem QGraphicsScene.addPolygon(QPolygonF polygon, QPen pen = QPen(), QBrush brush = QBrush())'''
        return QGraphicsPolygonItem()
    def addPixmap(self, pixmap):
        '''QGraphicsPixmapItem QGraphicsScene.addPixmap(QPixmap pixmap)'''
        return QGraphicsPixmapItem()
    def addPath(self, path, pen = QPen(), brush = QBrush()):
        '''QGraphicsPathItem QGraphicsScene.addPath(QPainterPath path, QPen pen = QPen(), QBrush brush = QBrush())'''
        return QGraphicsPathItem()
    def addLine(self, line, pen = QPen()):
        '''QGraphicsLineItem QGraphicsScene.addLine(QLineF line, QPen pen = QPen())'''
        return QGraphicsLineItem()
    def addLine(self, x1, y1, x2, y2, pen = QPen()):
        '''QGraphicsLineItem QGraphicsScene.addLine(float x1, float y1, float x2, float y2, QPen pen = QPen())'''
        return QGraphicsLineItem()
    def addEllipse(self, rect, pen = QPen(), brush = QBrush()):
        '''QGraphicsEllipseItem QGraphicsScene.addEllipse(QRectF rect, QPen pen = QPen(), QBrush brush = QBrush())'''
        return QGraphicsEllipseItem()
    def addEllipse(self, x, y, w, h, pen = QPen(), brush = QBrush()):
        '''QGraphicsEllipseItem QGraphicsScene.addEllipse(float x, float y, float w, float h, QPen pen = QPen(), QBrush brush = QBrush())'''
        return QGraphicsEllipseItem()
    def addItem(self, item):
        '''void QGraphicsScene.addItem(QGraphicsItem item)'''
    def destroyItemGroup(self, group):
        '''void QGraphicsScene.destroyItemGroup(QGraphicsItemGroup group)'''
    def createItemGroup(self, items):
        '''QGraphicsItemGroup QGraphicsScene.createItemGroup(list-of-QGraphicsItem items)'''
        return QGraphicsItemGroup()
    def clearSelection(self):
        '''void QGraphicsScene.clearSelection()'''
    def setSelectionArea(self, path, deviceTransform):
        '''void QGraphicsScene.setSelectionArea(QPainterPath path, QTransform deviceTransform)'''
    def setSelectionArea(self, path, mode = None, deviceTransform = QTransform()):
        '''void QGraphicsScene.setSelectionArea(QPainterPath path, Qt.ItemSelectionMode mode = Qt.IntersectsItemShape, QTransform deviceTransform = QTransform())'''
    def setSelectionArea(self, path, selectionOperation, mode = None, deviceTransform = QTransform()):
        '''void QGraphicsScene.setSelectionArea(QPainterPath path, Qt.ItemSelectionOperation selectionOperation, Qt.ItemSelectionMode mode = Qt.IntersectsItemShape, QTransform deviceTransform = QTransform())'''
    def selectedItems(self):
        '''list-of-QGraphicsItem QGraphicsScene.selectedItems()'''
        return [QGraphicsItem()]
    def collidingItems(self, item, mode = None):
        '''list-of-QGraphicsItem QGraphicsScene.collidingItems(QGraphicsItem item, Qt.ItemSelectionMode mode = Qt.IntersectsItemShape)'''
        return [QGraphicsItem()]
    def items(self, order = None):
        '''list-of-QGraphicsItem QGraphicsScene.items(Qt.SortOrder order = Qt.DescendingOrder)'''
        return [QGraphicsItem()]
    def items(self, pos, mode = None, order = None, deviceTransform = QTransform()):
        '''list-of-QGraphicsItem QGraphicsScene.items(QPointF pos, Qt.ItemSelectionMode mode = Qt.IntersectsItemShape, Qt.SortOrder order = Qt.DescendingOrder, QTransform deviceTransform = QTransform())'''
        return [QGraphicsItem()]
    def items(self, rect, mode = None, order = None, deviceTransform = QTransform()):
        '''list-of-QGraphicsItem QGraphicsScene.items(QRectF rect, Qt.ItemSelectionMode mode = Qt.IntersectsItemShape, Qt.SortOrder order = Qt.DescendingOrder, QTransform deviceTransform = QTransform())'''
        return [QGraphicsItem()]
    def items(self, polygon, mode = None, order = None, deviceTransform = QTransform()):
        '''list-of-QGraphicsItem QGraphicsScene.items(QPolygonF polygon, Qt.ItemSelectionMode mode = Qt.IntersectsItemShape, Qt.SortOrder order = Qt.DescendingOrder, QTransform deviceTransform = QTransform())'''
        return [QGraphicsItem()]
    def items(self, path, mode = None, order = None, deviceTransform = QTransform()):
        '''list-of-QGraphicsItem QGraphicsScene.items(QPainterPath path, Qt.ItemSelectionMode mode = Qt.IntersectsItemShape, Qt.SortOrder order = Qt.DescendingOrder, QTransform deviceTransform = QTransform())'''
        return [QGraphicsItem()]
    def items(self, x, y, w, h, mode, order, deviceTransform = QTransform()):
        '''list-of-QGraphicsItem QGraphicsScene.items(float x, float y, float w, float h, Qt.ItemSelectionMode mode, Qt.SortOrder order, QTransform deviceTransform = QTransform())'''
        return [QGraphicsItem()]
    def itemsBoundingRect(self):
        '''QRectF QGraphicsScene.itemsBoundingRect()'''
        return QRectF()
    def setItemIndexMethod(self, method):
        '''void QGraphicsScene.setItemIndexMethod(QGraphicsScene.ItemIndexMethod method)'''
    def itemIndexMethod(self):
        '''QGraphicsScene.ItemIndexMethod QGraphicsScene.itemIndexMethod()'''
        return QGraphicsScene.ItemIndexMethod()
    def render(self, painter, target = QRectF(), source = QRectF(), mode = None):
        '''void QGraphicsScene.render(QPainter painter, QRectF target = QRectF(), QRectF source = QRectF(), Qt.AspectRatioMode mode = Qt.KeepAspectRatio)'''
    def setSceneRect(self, rect):
        '''void QGraphicsScene.setSceneRect(QRectF rect)'''
    def setSceneRect(self, x, y, w, h):
        '''void QGraphicsScene.setSceneRect(float x, float y, float w, float h)'''
    def height(self):
        '''float QGraphicsScene.height()'''
        return float()
    def width(self):
        '''float QGraphicsScene.width()'''
        return float()
    def sceneRect(self):
        '''QRectF QGraphicsScene.sceneRect()'''
        return QRectF()
    class SceneLayers():
        """"""
        def __init__(self):
            '''QGraphicsScene.SceneLayers QGraphicsScene.SceneLayers.__init__()'''
            return QGraphicsScene.SceneLayers()
        def __init__(self):
            '''int QGraphicsScene.SceneLayers.__init__()'''
            return int()
        def __init__(self):
            '''void QGraphicsScene.SceneLayers.__init__()'''
        def __bool__(self):
            '''int QGraphicsScene.SceneLayers.__bool__()'''
            return int()
        def __ne__(self, f):
            '''bool QGraphicsScene.SceneLayers.__ne__(QGraphicsScene.SceneLayers f)'''
            return bool()
        def __eq__(self, f):
            '''bool QGraphicsScene.SceneLayers.__eq__(QGraphicsScene.SceneLayers f)'''
            return bool()
        def __invert__(self):
            '''QGraphicsScene.SceneLayers QGraphicsScene.SceneLayers.__invert__()'''
            return QGraphicsScene.SceneLayers()
        def __and__(self, mask):
            '''QGraphicsScene.SceneLayers QGraphicsScene.SceneLayers.__and__(int mask)'''
            return QGraphicsScene.SceneLayers()
        def __xor__(self, f):
            '''QGraphicsScene.SceneLayers QGraphicsScene.SceneLayers.__xor__(QGraphicsScene.SceneLayers f)'''
            return QGraphicsScene.SceneLayers()
        def __xor__(self, f):
            '''QGraphicsScene.SceneLayers QGraphicsScene.SceneLayers.__xor__(int f)'''
            return QGraphicsScene.SceneLayers()
        def __or__(self, f):
            '''QGraphicsScene.SceneLayers QGraphicsScene.SceneLayers.__or__(QGraphicsScene.SceneLayers f)'''
            return QGraphicsScene.SceneLayers()
        def __or__(self, f):
            '''QGraphicsScene.SceneLayers QGraphicsScene.SceneLayers.__or__(int f)'''
            return QGraphicsScene.SceneLayers()
        def __int__(self):
            '''int QGraphicsScene.SceneLayers.__int__()'''
            return int()
        def __ixor__(self, f):
            '''QGraphicsScene.SceneLayers QGraphicsScene.SceneLayers.__ixor__(QGraphicsScene.SceneLayers f)'''
            return QGraphicsScene.SceneLayers()
        def __ior__(self, f):
            '''QGraphicsScene.SceneLayers QGraphicsScene.SceneLayers.__ior__(QGraphicsScene.SceneLayers f)'''
            return QGraphicsScene.SceneLayers()
        def __iand__(self, mask):
            '''QGraphicsScene.SceneLayers QGraphicsScene.SceneLayers.__iand__(int mask)'''
            return QGraphicsScene.SceneLayers()


class QGraphicsSceneEvent(QEvent):
    """"""
    def widget(self):
        '''QWidget QGraphicsSceneEvent.widget()'''
        return QWidget()


class QGraphicsSceneMouseEvent(QGraphicsSceneEvent):
    """"""
    def flags(self):
        '''Qt.MouseEventFlags QGraphicsSceneMouseEvent.flags()'''
        return Qt.MouseEventFlags()
    def source(self):
        '''Qt.MouseEventSource QGraphicsSceneMouseEvent.source()'''
        return Qt.MouseEventSource()
    def modifiers(self):
        '''Qt.KeyboardModifiers QGraphicsSceneMouseEvent.modifiers()'''
        return Qt.KeyboardModifiers()
    def button(self):
        '''Qt.MouseButton QGraphicsSceneMouseEvent.button()'''
        return Qt.MouseButton()
    def buttons(self):
        '''Qt.MouseButtons QGraphicsSceneMouseEvent.buttons()'''
        return Qt.MouseButtons()
    def lastScreenPos(self):
        '''QPoint QGraphicsSceneMouseEvent.lastScreenPos()'''
        return QPoint()
    def lastScenePos(self):
        '''QPointF QGraphicsSceneMouseEvent.lastScenePos()'''
        return QPointF()
    def lastPos(self):
        '''QPointF QGraphicsSceneMouseEvent.lastPos()'''
        return QPointF()
    def buttonDownScreenPos(self, button):
        '''QPoint QGraphicsSceneMouseEvent.buttonDownScreenPos(Qt.MouseButton button)'''
        return QPoint()
    def buttonDownScenePos(self, button):
        '''QPointF QGraphicsSceneMouseEvent.buttonDownScenePos(Qt.MouseButton button)'''
        return QPointF()
    def buttonDownPos(self, button):
        '''QPointF QGraphicsSceneMouseEvent.buttonDownPos(Qt.MouseButton button)'''
        return QPointF()
    def screenPos(self):
        '''QPoint QGraphicsSceneMouseEvent.screenPos()'''
        return QPoint()
    def scenePos(self):
        '''QPointF QGraphicsSceneMouseEvent.scenePos()'''
        return QPointF()
    def pos(self):
        '''QPointF QGraphicsSceneMouseEvent.pos()'''
        return QPointF()


class QGraphicsSceneWheelEvent(QGraphicsSceneEvent):
    """"""
    def orientation(self):
        '''Qt.Orientation QGraphicsSceneWheelEvent.orientation()'''
        return Qt.Orientation()
    def delta(self):
        '''int QGraphicsSceneWheelEvent.delta()'''
        return int()
    def modifiers(self):
        '''Qt.KeyboardModifiers QGraphicsSceneWheelEvent.modifiers()'''
        return Qt.KeyboardModifiers()
    def buttons(self):
        '''Qt.MouseButtons QGraphicsSceneWheelEvent.buttons()'''
        return Qt.MouseButtons()
    def screenPos(self):
        '''QPoint QGraphicsSceneWheelEvent.screenPos()'''
        return QPoint()
    def scenePos(self):
        '''QPointF QGraphicsSceneWheelEvent.scenePos()'''
        return QPointF()
    def pos(self):
        '''QPointF QGraphicsSceneWheelEvent.pos()'''
        return QPointF()


class QGraphicsSceneContextMenuEvent(QGraphicsSceneEvent):
    """"""
    # Enum QGraphicsSceneContextMenuEvent.Reason
    Mouse = 0
    Keyboard = 0
    Other = 0

    def reason(self):
        '''QGraphicsSceneContextMenuEvent.Reason QGraphicsSceneContextMenuEvent.reason()'''
        return QGraphicsSceneContextMenuEvent.Reason()
    def modifiers(self):
        '''Qt.KeyboardModifiers QGraphicsSceneContextMenuEvent.modifiers()'''
        return Qt.KeyboardModifiers()
    def screenPos(self):
        '''QPoint QGraphicsSceneContextMenuEvent.screenPos()'''
        return QPoint()
    def scenePos(self):
        '''QPointF QGraphicsSceneContextMenuEvent.scenePos()'''
        return QPointF()
    def pos(self):
        '''QPointF QGraphicsSceneContextMenuEvent.pos()'''
        return QPointF()


class QGraphicsSceneHoverEvent(QGraphicsSceneEvent):
    """"""
    def modifiers(self):
        '''Qt.KeyboardModifiers QGraphicsSceneHoverEvent.modifiers()'''
        return Qt.KeyboardModifiers()
    def lastScreenPos(self):
        '''QPoint QGraphicsSceneHoverEvent.lastScreenPos()'''
        return QPoint()
    def lastScenePos(self):
        '''QPointF QGraphicsSceneHoverEvent.lastScenePos()'''
        return QPointF()
    def lastPos(self):
        '''QPointF QGraphicsSceneHoverEvent.lastPos()'''
        return QPointF()
    def screenPos(self):
        '''QPoint QGraphicsSceneHoverEvent.screenPos()'''
        return QPoint()
    def scenePos(self):
        '''QPointF QGraphicsSceneHoverEvent.scenePos()'''
        return QPointF()
    def pos(self):
        '''QPointF QGraphicsSceneHoverEvent.pos()'''
        return QPointF()


class QGraphicsSceneHelpEvent(QGraphicsSceneEvent):
    """"""
    def screenPos(self):
        '''QPoint QGraphicsSceneHelpEvent.screenPos()'''
        return QPoint()
    def scenePos(self):
        '''QPointF QGraphicsSceneHelpEvent.scenePos()'''
        return QPointF()


class QGraphicsSceneDragDropEvent(QGraphicsSceneEvent):
    """"""
    def mimeData(self):
        '''QMimeData QGraphicsSceneDragDropEvent.mimeData()'''
        return QMimeData()
    def source(self):
        '''QWidget QGraphicsSceneDragDropEvent.source()'''
        return QWidget()
    def setDropAction(self, action):
        '''void QGraphicsSceneDragDropEvent.setDropAction(Qt.DropAction action)'''
    def dropAction(self):
        '''Qt.DropAction QGraphicsSceneDragDropEvent.dropAction()'''
        return Qt.DropAction()
    def acceptProposedAction(self):
        '''void QGraphicsSceneDragDropEvent.acceptProposedAction()'''
    def proposedAction(self):
        '''Qt.DropAction QGraphicsSceneDragDropEvent.proposedAction()'''
        return Qt.DropAction()
    def possibleActions(self):
        '''Qt.DropActions QGraphicsSceneDragDropEvent.possibleActions()'''
        return Qt.DropActions()
    def modifiers(self):
        '''Qt.KeyboardModifiers QGraphicsSceneDragDropEvent.modifiers()'''
        return Qt.KeyboardModifiers()
    def buttons(self):
        '''Qt.MouseButtons QGraphicsSceneDragDropEvent.buttons()'''
        return Qt.MouseButtons()
    def screenPos(self):
        '''QPoint QGraphicsSceneDragDropEvent.screenPos()'''
        return QPoint()
    def scenePos(self):
        '''QPointF QGraphicsSceneDragDropEvent.scenePos()'''
        return QPointF()
    def pos(self):
        '''QPointF QGraphicsSceneDragDropEvent.pos()'''
        return QPointF()


class QGraphicsSceneResizeEvent(QGraphicsSceneEvent):
    """"""
    def __init__(self):
        '''void QGraphicsSceneResizeEvent.__init__()'''
    def newSize(self):
        '''QSizeF QGraphicsSceneResizeEvent.newSize()'''
        return QSizeF()
    def oldSize(self):
        '''QSizeF QGraphicsSceneResizeEvent.oldSize()'''
        return QSizeF()


class QGraphicsSceneMoveEvent(QGraphicsSceneEvent):
    """"""
    def __init__(self):
        '''void QGraphicsSceneMoveEvent.__init__()'''
    def newPos(self):
        '''QPointF QGraphicsSceneMoveEvent.newPos()'''
        return QPointF()
    def oldPos(self):
        '''QPointF QGraphicsSceneMoveEvent.oldPos()'''
        return QPointF()


class QGraphicsTransform(QObject):
    """"""
    def __init__(self, parent = None):
        '''void QGraphicsTransform.__init__(QObject parent = None)'''
    def update(self):
        '''void QGraphicsTransform.update()'''
    def applyTo(self, matrix):
        '''abstract void QGraphicsTransform.applyTo(QMatrix4x4 matrix)'''


class QGraphicsScale(QGraphicsTransform):
    """"""
    def __init__(self, parent = None):
        '''void QGraphicsScale.__init__(QObject parent = None)'''
    zScaleChanged = pyqtSignal() # void zScaleChanged() - signal
    yScaleChanged = pyqtSignal() # void yScaleChanged() - signal
    xScaleChanged = pyqtSignal() # void xScaleChanged() - signal
    scaleChanged = pyqtSignal() # void scaleChanged() - signal
    originChanged = pyqtSignal() # void originChanged() - signal
    def applyTo(self, matrix):
        '''void QGraphicsScale.applyTo(QMatrix4x4 matrix)'''
    def setZScale(self):
        '''float QGraphicsScale.setZScale()'''
        return float()
    def zScale(self):
        '''float QGraphicsScale.zScale()'''
        return float()
    def setYScale(self):
        '''float QGraphicsScale.setYScale()'''
        return float()
    def yScale(self):
        '''float QGraphicsScale.yScale()'''
        return float()
    def setXScale(self):
        '''float QGraphicsScale.setXScale()'''
        return float()
    def xScale(self):
        '''float QGraphicsScale.xScale()'''
        return float()
    def setOrigin(self, point):
        '''void QGraphicsScale.setOrigin(QVector3D point)'''
    def origin(self):
        '''QVector3D QGraphicsScale.origin()'''
        return QVector3D()


class QGraphicsRotation(QGraphicsTransform):
    """"""
    def __init__(self, parent = None):
        '''void QGraphicsRotation.__init__(QObject parent = None)'''
    axisChanged = pyqtSignal() # void axisChanged() - signal
    angleChanged = pyqtSignal() # void angleChanged() - signal
    originChanged = pyqtSignal() # void originChanged() - signal
    def applyTo(self, matrix):
        '''void QGraphicsRotation.applyTo(QMatrix4x4 matrix)'''
    def setAxis(self, axis):
        '''void QGraphicsRotation.setAxis(QVector3D axis)'''
    def setAxis(self, axis):
        '''void QGraphicsRotation.setAxis(Qt.Axis axis)'''
    def axis(self):
        '''QVector3D QGraphicsRotation.axis()'''
        return QVector3D()
    def setAngle(self):
        '''float QGraphicsRotation.setAngle()'''
        return float()
    def angle(self):
        '''float QGraphicsRotation.angle()'''
        return float()
    def setOrigin(self, point):
        '''void QGraphicsRotation.setOrigin(QVector3D point)'''
    def origin(self):
        '''QVector3D QGraphicsRotation.origin()'''
        return QVector3D()


class QGraphicsView(QAbstractScrollArea):
    """"""
    # Enum QGraphicsView.OptimizationFlag
    DontClipPainter = 0
    DontSavePainterState = 0
    DontAdjustForAntialiasing = 0

    # Enum QGraphicsView.ViewportUpdateMode
    FullViewportUpdate = 0
    MinimalViewportUpdate = 0
    SmartViewportUpdate = 0
    BoundingRectViewportUpdate = 0
    NoViewportUpdate = 0

    # Enum QGraphicsView.ViewportAnchor
    NoAnchor = 0
    AnchorViewCenter = 0
    AnchorUnderMouse = 0

    # Enum QGraphicsView.DragMode
    NoDrag = 0
    ScrollHandDrag = 0
    RubberBandDrag = 0

    # Enum QGraphicsView.CacheModeFlag
    CacheNone = 0
    CacheBackground = 0

    def __init__(self, parent = None):
        '''void QGraphicsView.__init__(QWidget parent = None)'''
    def __init__(self, scene, parent = None):
        '''void QGraphicsView.__init__(QGraphicsScene scene, QWidget parent = None)'''
    rubberBandChanged = pyqtSignal() # void rubberBandChanged(QRect,QPointF,QPointF) - signal
    def rubberBandRect(self):
        '''QRect QGraphicsView.rubberBandRect()'''
        return QRect()
    def isTransformed(self):
        '''bool QGraphicsView.isTransformed()'''
        return bool()
    def resetTransform(self):
        '''void QGraphicsView.resetTransform()'''
    def setTransform(self, matrix, combine = False):
        '''void QGraphicsView.setTransform(QTransform matrix, bool combine = False)'''
    def viewportTransform(self):
        '''QTransform QGraphicsView.viewportTransform()'''
        return QTransform()
    def transform(self):
        '''QTransform QGraphicsView.transform()'''
        return QTransform()
    def setRubberBandSelectionMode(self, mode):
        '''void QGraphicsView.setRubberBandSelectionMode(Qt.ItemSelectionMode mode)'''
    def rubberBandSelectionMode(self):
        '''Qt.ItemSelectionMode QGraphicsView.rubberBandSelectionMode()'''
        return Qt.ItemSelectionMode()
    def setOptimizationFlags(self, flags):
        '''void QGraphicsView.setOptimizationFlags(QGraphicsView.OptimizationFlags flags)'''
    def setOptimizationFlag(self, flag, enabled = True):
        '''void QGraphicsView.setOptimizationFlag(QGraphicsView.OptimizationFlag flag, bool enabled = True)'''
    def optimizationFlags(self):
        '''QGraphicsView.OptimizationFlags QGraphicsView.optimizationFlags()'''
        return QGraphicsView.OptimizationFlags()
    def setViewportUpdateMode(self, mode):
        '''void QGraphicsView.setViewportUpdateMode(QGraphicsView.ViewportUpdateMode mode)'''
    def viewportUpdateMode(self):
        '''QGraphicsView.ViewportUpdateMode QGraphicsView.viewportUpdateMode()'''
        return QGraphicsView.ViewportUpdateMode()
    def drawForeground(self, painter, rect):
        '''void QGraphicsView.drawForeground(QPainter painter, QRectF rect)'''
    def drawBackground(self, painter, rect):
        '''void QGraphicsView.drawBackground(QPainter painter, QRectF rect)'''
    def inputMethodEvent(self, event):
        '''void QGraphicsView.inputMethodEvent(QInputMethodEvent event)'''
    def showEvent(self, event):
        '''void QGraphicsView.showEvent(QShowEvent event)'''
    def scrollContentsBy(self, dx, dy):
        '''void QGraphicsView.scrollContentsBy(int dx, int dy)'''
    def resizeEvent(self, event):
        '''void QGraphicsView.resizeEvent(QResizeEvent event)'''
    def paintEvent(self, event):
        '''void QGraphicsView.paintEvent(QPaintEvent event)'''
    def wheelEvent(self, event):
        '''void QGraphicsView.wheelEvent(QWheelEvent event)'''
    def mouseReleaseEvent(self, event):
        '''void QGraphicsView.mouseReleaseEvent(QMouseEvent event)'''
    def mouseMoveEvent(self, event):
        '''void QGraphicsView.mouseMoveEvent(QMouseEvent event)'''
    def mousePressEvent(self, event):
        '''void QGraphicsView.mousePressEvent(QMouseEvent event)'''
    def mouseDoubleClickEvent(self, event):
        '''void QGraphicsView.mouseDoubleClickEvent(QMouseEvent event)'''
    def keyReleaseEvent(self, event):
        '''void QGraphicsView.keyReleaseEvent(QKeyEvent event)'''
    def keyPressEvent(self, event):
        '''void QGraphicsView.keyPressEvent(QKeyEvent event)'''
    def focusNextPrevChild(self, next):
        '''bool QGraphicsView.focusNextPrevChild(bool next)'''
        return bool()
    def focusOutEvent(self, event):
        '''void QGraphicsView.focusOutEvent(QFocusEvent event)'''
    def focusInEvent(self, event):
        '''void QGraphicsView.focusInEvent(QFocusEvent event)'''
    def dropEvent(self, event):
        '''void QGraphicsView.dropEvent(QDropEvent event)'''
    def dragMoveEvent(self, event):
        '''void QGraphicsView.dragMoveEvent(QDragMoveEvent event)'''
    def dragLeaveEvent(self, event):
        '''void QGraphicsView.dragLeaveEvent(QDragLeaveEvent event)'''
    def dragEnterEvent(self, event):
        '''void QGraphicsView.dragEnterEvent(QDragEnterEvent event)'''
    def contextMenuEvent(self, event):
        '''void QGraphicsView.contextMenuEvent(QContextMenuEvent event)'''
    def viewportEvent(self, event):
        '''bool QGraphicsView.viewportEvent(QEvent event)'''
        return bool()
    def event(self, event):
        '''bool QGraphicsView.event(QEvent event)'''
        return bool()
    def setupViewport(self, widget):
        '''void QGraphicsView.setupViewport(QWidget widget)'''
    def updateSceneRect(self, rect):
        '''void QGraphicsView.updateSceneRect(QRectF rect)'''
    def updateScene(self, rects):
        '''void QGraphicsView.updateScene(list-of-QRectF rects)'''
    def invalidateScene(self, rect = QRectF(), layers = None):
        '''void QGraphicsView.invalidateScene(QRectF rect = QRectF(), QGraphicsScene.SceneLayers layers = QGraphicsScene.AllLayers)'''
    def setForegroundBrush(self, brush):
        '''void QGraphicsView.setForegroundBrush(QBrush brush)'''
    def foregroundBrush(self):
        '''QBrush QGraphicsView.foregroundBrush()'''
        return QBrush()
    def setBackgroundBrush(self, brush):
        '''void QGraphicsView.setBackgroundBrush(QBrush brush)'''
    def backgroundBrush(self):
        '''QBrush QGraphicsView.backgroundBrush()'''
        return QBrush()
    def inputMethodQuery(self, query):
        '''QVariant QGraphicsView.inputMethodQuery(Qt.InputMethodQuery query)'''
        return QVariant()
    def mapFromScene(self, point):
        '''QPoint QGraphicsView.mapFromScene(QPointF point)'''
        return QPoint()
    def mapFromScene(self, rect):
        '''QPolygon QGraphicsView.mapFromScene(QRectF rect)'''
        return QPolygon()
    def mapFromScene(self, polygon):
        '''QPolygon QGraphicsView.mapFromScene(QPolygonF polygon)'''
        return QPolygon()
    def mapFromScene(self, path):
        '''QPainterPath QGraphicsView.mapFromScene(QPainterPath path)'''
        return QPainterPath()
    def mapFromScene(self, ax, ay):
        '''QPoint QGraphicsView.mapFromScene(float ax, float ay)'''
        return QPoint()
    def mapFromScene(self, ax, ay, w, h):
        '''QPolygon QGraphicsView.mapFromScene(float ax, float ay, float w, float h)'''
        return QPolygon()
    def mapToScene(self, point):
        '''QPointF QGraphicsView.mapToScene(QPoint point)'''
        return QPointF()
    def mapToScene(self, rect):
        '''QPolygonF QGraphicsView.mapToScene(QRect rect)'''
        return QPolygonF()
    def mapToScene(self, polygon):
        '''QPolygonF QGraphicsView.mapToScene(QPolygon polygon)'''
        return QPolygonF()
    def mapToScene(self, path):
        '''QPainterPath QGraphicsView.mapToScene(QPainterPath path)'''
        return QPainterPath()
    def mapToScene(self, ax, ay):
        '''QPointF QGraphicsView.mapToScene(int ax, int ay)'''
        return QPointF()
    def mapToScene(self, ax, ay, w, h):
        '''QPolygonF QGraphicsView.mapToScene(int ax, int ay, int w, int h)'''
        return QPolygonF()
    def itemAt(self, pos):
        '''QGraphicsItem QGraphicsView.itemAt(QPoint pos)'''
        return QGraphicsItem()
    def itemAt(self, ax, ay):
        '''QGraphicsItem QGraphicsView.itemAt(int ax, int ay)'''
        return QGraphicsItem()
    def items(self):
        '''list-of-QGraphicsItem QGraphicsView.items()'''
        return [QGraphicsItem()]
    def items(self, pos):
        '''list-of-QGraphicsItem QGraphicsView.items(QPoint pos)'''
        return [QGraphicsItem()]
    def items(self, ax, ay):
        '''list-of-QGraphicsItem QGraphicsView.items(int ax, int ay)'''
        return [QGraphicsItem()]
    def items(self, x, y, w, h, mode = None):
        '''list-of-QGraphicsItem QGraphicsView.items(int x, int y, int w, int h, Qt.ItemSelectionMode mode = Qt.IntersectsItemShape)'''
        return [QGraphicsItem()]
    def items(self, rect, mode = None):
        '''list-of-QGraphicsItem QGraphicsView.items(QRect rect, Qt.ItemSelectionMode mode = Qt.IntersectsItemShape)'''
        return [QGraphicsItem()]
    def items(self, polygon, mode = None):
        '''list-of-QGraphicsItem QGraphicsView.items(QPolygon polygon, Qt.ItemSelectionMode mode = Qt.IntersectsItemShape)'''
        return [QGraphicsItem()]
    def items(self, path, mode = None):
        '''list-of-QGraphicsItem QGraphicsView.items(QPainterPath path, Qt.ItemSelectionMode mode = Qt.IntersectsItemShape)'''
        return [QGraphicsItem()]
    def render(self, painter, target = QRectF(), source = QRect(), mode = None):
        '''void QGraphicsView.render(QPainter painter, QRectF target = QRectF(), QRect source = QRect(), Qt.AspectRatioMode mode = Qt.KeepAspectRatio)'''
    def fitInView(self, rect, mode = None):
        '''void QGraphicsView.fitInView(QRectF rect, Qt.AspectRatioMode mode = Qt.IgnoreAspectRatio)'''
    def fitInView(self, item, mode = None):
        '''void QGraphicsView.fitInView(QGraphicsItem item, Qt.AspectRatioMode mode = Qt.IgnoreAspectRatio)'''
    def fitInView(self, x, y, w, h, mode = None):
        '''void QGraphicsView.fitInView(float x, float y, float w, float h, Qt.AspectRatioMode mode = Qt.IgnoreAspectRatio)'''
    def ensureVisible(self, rect, xMargin = 50, yMargin = 50):
        '''void QGraphicsView.ensureVisible(QRectF rect, int xMargin = 50, int yMargin = 50)'''
    def ensureVisible(self, item, xMargin = 50, yMargin = 50):
        '''void QGraphicsView.ensureVisible(QGraphicsItem item, int xMargin = 50, int yMargin = 50)'''
    def ensureVisible(self, x, y, w, h, xMargin = 50, yMargin = 50):
        '''void QGraphicsView.ensureVisible(float x, float y, float w, float h, int xMargin = 50, int yMargin = 50)'''
    def centerOn(self, pos):
        '''void QGraphicsView.centerOn(QPointF pos)'''
    def centerOn(self, item):
        '''void QGraphicsView.centerOn(QGraphicsItem item)'''
    def centerOn(self, ax, ay):
        '''void QGraphicsView.centerOn(float ax, float ay)'''
    def translate(self, dx, dy):
        '''void QGraphicsView.translate(float dx, float dy)'''
    def shear(self, sh, sv):
        '''void QGraphicsView.shear(float sh, float sv)'''
    def scale(self, sx, sy):
        '''void QGraphicsView.scale(float sx, float sy)'''
    def rotate(self, angle):
        '''void QGraphicsView.rotate(float angle)'''
    def setSceneRect(self, rect):
        '''void QGraphicsView.setSceneRect(QRectF rect)'''
    def setSceneRect(self, ax, ay, aw, ah):
        '''void QGraphicsView.setSceneRect(float ax, float ay, float aw, float ah)'''
    def sceneRect(self):
        '''QRectF QGraphicsView.sceneRect()'''
        return QRectF()
    def setScene(self, scene):
        '''void QGraphicsView.setScene(QGraphicsScene scene)'''
    def scene(self):
        '''QGraphicsScene QGraphicsView.scene()'''
        return QGraphicsScene()
    def setInteractive(self, allowed):
        '''void QGraphicsView.setInteractive(bool allowed)'''
    def isInteractive(self):
        '''bool QGraphicsView.isInteractive()'''
        return bool()
    def resetCachedContent(self):
        '''void QGraphicsView.resetCachedContent()'''
    def setCacheMode(self, mode):
        '''void QGraphicsView.setCacheMode(QGraphicsView.CacheMode mode)'''
    def cacheMode(self):
        '''QGraphicsView.CacheMode QGraphicsView.cacheMode()'''
        return QGraphicsView.CacheMode()
    def setDragMode(self, mode):
        '''void QGraphicsView.setDragMode(QGraphicsView.DragMode mode)'''
    def dragMode(self):
        '''QGraphicsView.DragMode QGraphicsView.dragMode()'''
        return QGraphicsView.DragMode()
    def setResizeAnchor(self, anchor):
        '''void QGraphicsView.setResizeAnchor(QGraphicsView.ViewportAnchor anchor)'''
    def resizeAnchor(self):
        '''QGraphicsView.ViewportAnchor QGraphicsView.resizeAnchor()'''
        return QGraphicsView.ViewportAnchor()
    def setTransformationAnchor(self, anchor):
        '''void QGraphicsView.setTransformationAnchor(QGraphicsView.ViewportAnchor anchor)'''
    def transformationAnchor(self):
        '''QGraphicsView.ViewportAnchor QGraphicsView.transformationAnchor()'''
        return QGraphicsView.ViewportAnchor()
    def setAlignment(self, alignment):
        '''void QGraphicsView.setAlignment(Qt.Alignment alignment)'''
    def alignment(self):
        '''Qt.Alignment QGraphicsView.alignment()'''
        return Qt.Alignment()
    def setRenderHints(self, hints):
        '''void QGraphicsView.setRenderHints(QPainter.RenderHints hints)'''
    def setRenderHint(self, hint, on = True):
        '''void QGraphicsView.setRenderHint(QPainter.RenderHint hint, bool on = True)'''
    def renderHints(self):
        '''QPainter.RenderHints QGraphicsView.renderHints()'''
        return QPainter.RenderHints()
    def sizeHint(self):
        '''QSize QGraphicsView.sizeHint()'''
        return QSize()
    class CacheMode():
        """"""
        def __init__(self):
            '''QGraphicsView.CacheMode QGraphicsView.CacheMode.__init__()'''
            return QGraphicsView.CacheMode()
        def __init__(self):
            '''int QGraphicsView.CacheMode.__init__()'''
            return int()
        def __init__(self):
            '''void QGraphicsView.CacheMode.__init__()'''
        def __bool__(self):
            '''int QGraphicsView.CacheMode.__bool__()'''
            return int()
        def __ne__(self, f):
            '''bool QGraphicsView.CacheMode.__ne__(QGraphicsView.CacheMode f)'''
            return bool()
        def __eq__(self, f):
            '''bool QGraphicsView.CacheMode.__eq__(QGraphicsView.CacheMode f)'''
            return bool()
        def __invert__(self):
            '''QGraphicsView.CacheMode QGraphicsView.CacheMode.__invert__()'''
            return QGraphicsView.CacheMode()
        def __and__(self, mask):
            '''QGraphicsView.CacheMode QGraphicsView.CacheMode.__and__(int mask)'''
            return QGraphicsView.CacheMode()
        def __xor__(self, f):
            '''QGraphicsView.CacheMode QGraphicsView.CacheMode.__xor__(QGraphicsView.CacheMode f)'''
            return QGraphicsView.CacheMode()
        def __xor__(self, f):
            '''QGraphicsView.CacheMode QGraphicsView.CacheMode.__xor__(int f)'''
            return QGraphicsView.CacheMode()
        def __or__(self, f):
            '''QGraphicsView.CacheMode QGraphicsView.CacheMode.__or__(QGraphicsView.CacheMode f)'''
            return QGraphicsView.CacheMode()
        def __or__(self, f):
            '''QGraphicsView.CacheMode QGraphicsView.CacheMode.__or__(int f)'''
            return QGraphicsView.CacheMode()
        def __int__(self):
            '''int QGraphicsView.CacheMode.__int__()'''
            return int()
        def __ixor__(self, f):
            '''QGraphicsView.CacheMode QGraphicsView.CacheMode.__ixor__(QGraphicsView.CacheMode f)'''
            return QGraphicsView.CacheMode()
        def __ior__(self, f):
            '''QGraphicsView.CacheMode QGraphicsView.CacheMode.__ior__(QGraphicsView.CacheMode f)'''
            return QGraphicsView.CacheMode()
        def __iand__(self, mask):
            '''QGraphicsView.CacheMode QGraphicsView.CacheMode.__iand__(int mask)'''
            return QGraphicsView.CacheMode()
    class OptimizationFlags():
        """"""
        def __init__(self):
            '''QGraphicsView.OptimizationFlags QGraphicsView.OptimizationFlags.__init__()'''
            return QGraphicsView.OptimizationFlags()
        def __init__(self):
            '''int QGraphicsView.OptimizationFlags.__init__()'''
            return int()
        def __init__(self):
            '''void QGraphicsView.OptimizationFlags.__init__()'''
        def __bool__(self):
            '''int QGraphicsView.OptimizationFlags.__bool__()'''
            return int()
        def __ne__(self, f):
            '''bool QGraphicsView.OptimizationFlags.__ne__(QGraphicsView.OptimizationFlags f)'''
            return bool()
        def __eq__(self, f):
            '''bool QGraphicsView.OptimizationFlags.__eq__(QGraphicsView.OptimizationFlags f)'''
            return bool()
        def __invert__(self):
            '''QGraphicsView.OptimizationFlags QGraphicsView.OptimizationFlags.__invert__()'''
            return QGraphicsView.OptimizationFlags()
        def __and__(self, mask):
            '''QGraphicsView.OptimizationFlags QGraphicsView.OptimizationFlags.__and__(int mask)'''
            return QGraphicsView.OptimizationFlags()
        def __xor__(self, f):
            '''QGraphicsView.OptimizationFlags QGraphicsView.OptimizationFlags.__xor__(QGraphicsView.OptimizationFlags f)'''
            return QGraphicsView.OptimizationFlags()
        def __xor__(self, f):
            '''QGraphicsView.OptimizationFlags QGraphicsView.OptimizationFlags.__xor__(int f)'''
            return QGraphicsView.OptimizationFlags()
        def __or__(self, f):
            '''QGraphicsView.OptimizationFlags QGraphicsView.OptimizationFlags.__or__(QGraphicsView.OptimizationFlags f)'''
            return QGraphicsView.OptimizationFlags()
        def __or__(self, f):
            '''QGraphicsView.OptimizationFlags QGraphicsView.OptimizationFlags.__or__(int f)'''
            return QGraphicsView.OptimizationFlags()
        def __int__(self):
            '''int QGraphicsView.OptimizationFlags.__int__()'''
            return int()
        def __ixor__(self, f):
            '''QGraphicsView.OptimizationFlags QGraphicsView.OptimizationFlags.__ixor__(QGraphicsView.OptimizationFlags f)'''
            return QGraphicsView.OptimizationFlags()
        def __ior__(self, f):
            '''QGraphicsView.OptimizationFlags QGraphicsView.OptimizationFlags.__ior__(QGraphicsView.OptimizationFlags f)'''
            return QGraphicsView.OptimizationFlags()
        def __iand__(self, mask):
            '''QGraphicsView.OptimizationFlags QGraphicsView.OptimizationFlags.__iand__(int mask)'''
            return QGraphicsView.OptimizationFlags()


class QGridLayout(QLayout):
    """"""
    def __init__(self, parent):
        '''void QGridLayout.__init__(QWidget parent)'''
    def __init__(self):
        '''void QGridLayout.__init__()'''
    def itemAtPosition(self, row, column):
        '''QLayoutItem QGridLayout.itemAtPosition(int row, int column)'''
        return QLayoutItem()
    def spacing(self):
        '''int QGridLayout.spacing()'''
        return int()
    def setSpacing(self, spacing):
        '''void QGridLayout.setSpacing(int spacing)'''
    def verticalSpacing(self):
        '''int QGridLayout.verticalSpacing()'''
        return int()
    def setVerticalSpacing(self, spacing):
        '''void QGridLayout.setVerticalSpacing(int spacing)'''
    def horizontalSpacing(self):
        '''int QGridLayout.horizontalSpacing()'''
        return int()
    def setHorizontalSpacing(self, spacing):
        '''void QGridLayout.setHorizontalSpacing(int spacing)'''
    def getItemPosition(self, idx, row, column, rowSpan, columnSpan):
        '''void QGridLayout.getItemPosition(int idx, int row, int column, int rowSpan, int columnSpan)'''
    def setDefaultPositioning(self, n, orient):
        '''void QGridLayout.setDefaultPositioning(int n, Qt.Orientation orient)'''
    def addItem(self, item, row, column, rowSpan = 1, columnSpan = 1, alignment = 0):
        '''void QGridLayout.addItem(QLayoutItem item, int row, int column, int rowSpan = 1, int columnSpan = 1, Qt.Alignment alignment = 0)'''
    def addItem(self):
        '''QLayoutItem QGridLayout.addItem()'''
        return QLayoutItem()
    def setGeometry(self):
        '''QRect QGridLayout.setGeometry()'''
        return QRect()
    def count(self):
        '''int QGridLayout.count()'''
        return int()
    def takeAt(self):
        '''int QGridLayout.takeAt()'''
        return int()
    def itemAt(self):
        '''int QGridLayout.itemAt()'''
        return int()
    def originCorner(self):
        '''Qt.Corner QGridLayout.originCorner()'''
        return Qt.Corner()
    def setOriginCorner(self):
        '''Qt.Corner QGridLayout.setOriginCorner()'''
        return Qt.Corner()
    def addLayout(self, row, column, alignment = 0):
        '''QLayout QGridLayout.addLayout(int row, int column, Qt.Alignment alignment = 0)'''
        return QLayout()
    def addLayout(self, row, column, rowSpan, columnSpan, alignment = 0):
        '''QLayout QGridLayout.addLayout(int row, int column, int rowSpan, int columnSpan, Qt.Alignment alignment = 0)'''
        return QLayout()
    def addWidget(self, w):
        '''void QGridLayout.addWidget(QWidget w)'''
    def addWidget(self, row, column, alignment = 0):
        '''QWidget QGridLayout.addWidget(int row, int column, Qt.Alignment alignment = 0)'''
        return QWidget()
    def addWidget(self, row, column, rowSpan, columnSpan, alignment = 0):
        '''QWidget QGridLayout.addWidget(int row, int column, int rowSpan, int columnSpan, Qt.Alignment alignment = 0)'''
        return QWidget()
    def invalidate(self):
        '''void QGridLayout.invalidate()'''
    def expandingDirections(self):
        '''Qt.Orientations QGridLayout.expandingDirections()'''
        return Qt.Orientations()
    def minimumHeightForWidth(self):
        '''int QGridLayout.minimumHeightForWidth()'''
        return int()
    def heightForWidth(self):
        '''int QGridLayout.heightForWidth()'''
        return int()
    def hasHeightForWidth(self):
        '''bool QGridLayout.hasHeightForWidth()'''
        return bool()
    def cellRect(self, row, column):
        '''QRect QGridLayout.cellRect(int row, int column)'''
        return QRect()
    def rowCount(self):
        '''int QGridLayout.rowCount()'''
        return int()
    def columnCount(self):
        '''int QGridLayout.columnCount()'''
        return int()
    def columnMinimumWidth(self, column):
        '''int QGridLayout.columnMinimumWidth(int column)'''
        return int()
    def rowMinimumHeight(self, row):
        '''int QGridLayout.rowMinimumHeight(int row)'''
        return int()
    def setColumnMinimumWidth(self, column, minSize):
        '''void QGridLayout.setColumnMinimumWidth(int column, int minSize)'''
    def setRowMinimumHeight(self, row, minSize):
        '''void QGridLayout.setRowMinimumHeight(int row, int minSize)'''
    def columnStretch(self, column):
        '''int QGridLayout.columnStretch(int column)'''
        return int()
    def rowStretch(self, row):
        '''int QGridLayout.rowStretch(int row)'''
        return int()
    def setColumnStretch(self, column, stretch):
        '''void QGridLayout.setColumnStretch(int column, int stretch)'''
    def setRowStretch(self, row, stretch):
        '''void QGridLayout.setRowStretch(int row, int stretch)'''
    def maximumSize(self):
        '''QSize QGridLayout.maximumSize()'''
        return QSize()
    def minimumSize(self):
        '''QSize QGridLayout.minimumSize()'''
        return QSize()
    def sizeHint(self):
        '''QSize QGridLayout.sizeHint()'''
        return QSize()


class QGroupBox(QWidget):
    """"""
    def __init__(self, parent = None):
        '''void QGroupBox.__init__(QWidget parent = None)'''
    def __init__(self, title, parent = None):
        '''void QGroupBox.__init__(str title, QWidget parent = None)'''
    def mouseReleaseEvent(self, event):
        '''void QGroupBox.mouseReleaseEvent(QMouseEvent event)'''
    def mouseMoveEvent(self, event):
        '''void QGroupBox.mouseMoveEvent(QMouseEvent event)'''
    def mousePressEvent(self, event):
        '''void QGroupBox.mousePressEvent(QMouseEvent event)'''
    def changeEvent(self):
        '''QEvent QGroupBox.changeEvent()'''
        return QEvent()
    def focusInEvent(self):
        '''QFocusEvent QGroupBox.focusInEvent()'''
        return QFocusEvent()
    def paintEvent(self):
        '''QPaintEvent QGroupBox.paintEvent()'''
        return QPaintEvent()
    def resizeEvent(self):
        '''QResizeEvent QGroupBox.resizeEvent()'''
        return QResizeEvent()
    def childEvent(self):
        '''QChildEvent QGroupBox.childEvent()'''
        return QChildEvent()
    def event(self):
        '''QEvent QGroupBox.event()'''
        return QEvent()
    def initStyleOption(self, option):
        '''void QGroupBox.initStyleOption(QStyleOptionGroupBox option)'''
    toggled = pyqtSignal() # void toggled(bool) - signal
    clicked = pyqtSignal() # void clicked(bool = 0) - signal
    def setChecked(self, b):
        '''void QGroupBox.setChecked(bool b)'''
    def isChecked(self):
        '''bool QGroupBox.isChecked()'''
        return bool()
    def setCheckable(self, b):
        '''void QGroupBox.setCheckable(bool b)'''
    def isCheckable(self):
        '''bool QGroupBox.isCheckable()'''
        return bool()
    def setFlat(self, b):
        '''void QGroupBox.setFlat(bool b)'''
    def isFlat(self):
        '''bool QGroupBox.isFlat()'''
        return bool()
    def minimumSizeHint(self):
        '''QSize QGroupBox.minimumSizeHint()'''
        return QSize()
    def setAlignment(self):
        '''int QGroupBox.setAlignment()'''
        return int()
    def alignment(self):
        '''Qt.Alignment QGroupBox.alignment()'''
        return Qt.Alignment()
    def setTitle(self):
        '''str QGroupBox.setTitle()'''
        return str()
    def title(self):
        '''str QGroupBox.title()'''
        return str()


class QHeaderView(QAbstractItemView):
    """"""
    # Enum QHeaderView.ResizeMode
    Interactive = 0
    Fixed = 0
    Stretch = 0
    ResizeToContents = 0
    Custom = 0

    def __init__(self, orientation, parent = None):
        '''void QHeaderView.__init__(Qt.Orientation orientation, QWidget parent = None)'''
    def resetDefaultSectionSize(self):
        '''void QHeaderView.resetDefaultSectionSize()'''
    def setMaximumSectionSize(self, size):
        '''void QHeaderView.setMaximumSectionSize(int size)'''
    def maximumSectionSize(self):
        '''int QHeaderView.maximumSectionSize()'''
        return int()
    def resizeContentsPrecision(self):
        '''int QHeaderView.resizeContentsPrecision()'''
        return int()
    def setResizeContentsPrecision(self, precision):
        '''void QHeaderView.setResizeContentsPrecision(int precision)'''
    def setVisible(self, v):
        '''void QHeaderView.setVisible(bool v)'''
    def setSectionResizeMode(self, logicalIndex, mode):
        '''void QHeaderView.setSectionResizeMode(int logicalIndex, QHeaderView.ResizeMode mode)'''
    def setSectionResizeMode(self, mode):
        '''void QHeaderView.setSectionResizeMode(QHeaderView.ResizeMode mode)'''
    def sectionResizeMode(self, logicalIndex):
        '''QHeaderView.ResizeMode QHeaderView.sectionResizeMode(int logicalIndex)'''
        return QHeaderView.ResizeMode()
    def sectionsClickable(self):
        '''bool QHeaderView.sectionsClickable()'''
        return bool()
    def setSectionsClickable(self, clickable):
        '''void QHeaderView.setSectionsClickable(bool clickable)'''
    def sectionsMovable(self):
        '''bool QHeaderView.sectionsMovable()'''
        return bool()
    def setSectionsMovable(self, movable):
        '''void QHeaderView.setSectionsMovable(bool movable)'''
    def initStyleOption(self, option):
        '''void QHeaderView.initStyleOption(QStyleOptionHeader option)'''
    sortIndicatorChanged = pyqtSignal() # void sortIndicatorChanged(int,Qt::SortOrder) - signal
    sectionEntered = pyqtSignal() # void sectionEntered(int) - signal
    def setOffsetToLastSection(self):
        '''void QHeaderView.setOffsetToLastSection()'''
    def reset(self):
        '''void QHeaderView.reset()'''
    def restoreState(self, state):
        '''bool QHeaderView.restoreState(QByteArray state)'''
        return bool()
    def saveState(self):
        '''QByteArray QHeaderView.saveState()'''
        return QByteArray()
    def setMinimumSectionSize(self, size):
        '''void QHeaderView.setMinimumSectionSize(int size)'''
    def minimumSectionSize(self):
        '''int QHeaderView.minimumSectionSize()'''
        return int()
    def setCascadingSectionResizes(self, enable):
        '''void QHeaderView.setCascadingSectionResizes(bool enable)'''
    def cascadingSectionResizes(self):
        '''bool QHeaderView.cascadingSectionResizes()'''
        return bool()
    def swapSections(self, first, second):
        '''void QHeaderView.swapSections(int first, int second)'''
    def sectionsHidden(self):
        '''bool QHeaderView.sectionsHidden()'''
        return bool()
    def setDefaultAlignment(self, alignment):
        '''void QHeaderView.setDefaultAlignment(Qt.Alignment alignment)'''
    def defaultAlignment(self):
        '''Qt.Alignment QHeaderView.defaultAlignment()'''
        return Qt.Alignment()
    def setDefaultSectionSize(self, size):
        '''void QHeaderView.setDefaultSectionSize(int size)'''
    def defaultSectionSize(self):
        '''int QHeaderView.defaultSectionSize()'''
        return int()
    def hiddenSectionCount(self):
        '''int QHeaderView.hiddenSectionCount()'''
        return int()
    def showSection(self, alogicalIndex):
        '''void QHeaderView.showSection(int alogicalIndex)'''
    def hideSection(self, alogicalIndex):
        '''void QHeaderView.hideSection(int alogicalIndex)'''
    def visualRegionForSelection(self, selection):
        '''QRegion QHeaderView.visualRegionForSelection(QItemSelection selection)'''
        return QRegion()
    def setSelection(self):
        '''QItemSelectionModel.SelectionFlags QHeaderView.setSelection()'''
        return QItemSelectionModel.SelectionFlags()
    def moveCursor(self):
        '''Qt.KeyboardModifiers QHeaderView.moveCursor()'''
        return Qt.KeyboardModifiers()
    def isIndexHidden(self, index):
        '''bool QHeaderView.isIndexHidden(QModelIndex index)'''
        return bool()
    def indexAt(self, p):
        '''QModelIndex QHeaderView.indexAt(QPoint p)'''
        return QModelIndex()
    def scrollTo(self, index, hint):
        '''void QHeaderView.scrollTo(QModelIndex index, QAbstractItemView.ScrollHint hint)'''
    def visualRect(self, index):
        '''QRect QHeaderView.visualRect(QModelIndex index)'''
        return QRect()
    def rowsInserted(self, parent, start, end):
        '''void QHeaderView.rowsInserted(QModelIndex parent, int start, int end)'''
    def dataChanged(self, topLeft, bottomRight, roles = None):
        '''void QHeaderView.dataChanged(QModelIndex topLeft, QModelIndex bottomRight, list-of-int roles = [])'''
    def scrollContentsBy(self, dx, dy):
        '''void QHeaderView.scrollContentsBy(int dx, int dy)'''
    def updateGeometries(self):
        '''void QHeaderView.updateGeometries()'''
    def verticalOffset(self):
        '''int QHeaderView.verticalOffset()'''
        return int()
    def horizontalOffset(self):
        '''int QHeaderView.horizontalOffset()'''
        return int()
    def sectionSizeFromContents(self, logicalIndex):
        '''QSize QHeaderView.sectionSizeFromContents(int logicalIndex)'''
        return QSize()
    def paintSection(self, painter, rect, logicalIndex):
        '''void QHeaderView.paintSection(QPainter painter, QRect rect, int logicalIndex)'''
    def mouseDoubleClickEvent(self, e):
        '''void QHeaderView.mouseDoubleClickEvent(QMouseEvent e)'''
    def mouseReleaseEvent(self, e):
        '''void QHeaderView.mouseReleaseEvent(QMouseEvent e)'''
    def mouseMoveEvent(self, e):
        '''void QHeaderView.mouseMoveEvent(QMouseEvent e)'''
    def mousePressEvent(self, e):
        '''void QHeaderView.mousePressEvent(QMouseEvent e)'''
    def paintEvent(self, e):
        '''void QHeaderView.paintEvent(QPaintEvent e)'''
    def viewportEvent(self, e):
        '''bool QHeaderView.viewportEvent(QEvent e)'''
        return bool()
    def event(self, e):
        '''bool QHeaderView.event(QEvent e)'''
        return bool()
    def currentChanged(self, current, old):
        '''void QHeaderView.currentChanged(QModelIndex current, QModelIndex old)'''
    def initializeSections(self):
        '''void QHeaderView.initializeSections()'''
    def initializeSections(self, start, end):
        '''void QHeaderView.initializeSections(int start, int end)'''
    def initialize(self):
        '''void QHeaderView.initialize()'''
    def sectionsAboutToBeRemoved(self, parent, logicalFirst, logicalLast):
        '''void QHeaderView.sectionsAboutToBeRemoved(QModelIndex parent, int logicalFirst, int logicalLast)'''
    def sectionsInserted(self, parent, logicalFirst, logicalLast):
        '''void QHeaderView.sectionsInserted(QModelIndex parent, int logicalFirst, int logicalLast)'''
    def resizeSections(self):
        '''void QHeaderView.resizeSections()'''
    def resizeSections(self, mode):
        '''void QHeaderView.resizeSections(QHeaderView.ResizeMode mode)'''
    def updateSection(self, logicalIndex):
        '''void QHeaderView.updateSection(int logicalIndex)'''
    sectionHandleDoubleClicked = pyqtSignal() # void sectionHandleDoubleClicked(int) - signal
    sectionCountChanged = pyqtSignal() # void sectionCountChanged(int,int) - signal
    sectionDoubleClicked = pyqtSignal() # void sectionDoubleClicked(int) - signal
    sectionClicked = pyqtSignal() # void sectionClicked(int) - signal
    sectionPressed = pyqtSignal() # void sectionPressed(int) - signal
    sectionResized = pyqtSignal() # void sectionResized(int,int,int) - signal
    sectionMoved = pyqtSignal() # void sectionMoved(int,int,int) - signal
    geometriesChanged = pyqtSignal() # void geometriesChanged() - signal
    def setOffsetToSectionPosition(self, visualIndex):
        '''void QHeaderView.setOffsetToSectionPosition(int visualIndex)'''
    def headerDataChanged(self, orientation, logicalFirst, logicalLast):
        '''void QHeaderView.headerDataChanged(Qt.Orientation orientation, int logicalFirst, int logicalLast)'''
    def setOffset(self, offset):
        '''void QHeaderView.setOffset(int offset)'''
    def sectionsMoved(self):
        '''bool QHeaderView.sectionsMoved()'''
        return bool()
    def setStretchLastSection(self, stretch):
        '''void QHeaderView.setStretchLastSection(bool stretch)'''
    def stretchLastSection(self):
        '''bool QHeaderView.stretchLastSection()'''
        return bool()
    def sortIndicatorOrder(self):
        '''Qt.SortOrder QHeaderView.sortIndicatorOrder()'''
        return Qt.SortOrder()
    def sortIndicatorSection(self):
        '''int QHeaderView.sortIndicatorSection()'''
        return int()
    def setSortIndicator(self, logicalIndex, order):
        '''void QHeaderView.setSortIndicator(int logicalIndex, Qt.SortOrder order)'''
    def isSortIndicatorShown(self):
        '''bool QHeaderView.isSortIndicatorShown()'''
        return bool()
    def setSortIndicatorShown(self, show):
        '''void QHeaderView.setSortIndicatorShown(bool show)'''
    def stretchSectionCount(self):
        '''int QHeaderView.stretchSectionCount()'''
        return int()
    def highlightSections(self):
        '''bool QHeaderView.highlightSections()'''
        return bool()
    def setHighlightSections(self, highlight):
        '''void QHeaderView.setHighlightSections(bool highlight)'''
    def logicalIndex(self, visualIndex):
        '''int QHeaderView.logicalIndex(int visualIndex)'''
        return int()
    def visualIndex(self, logicalIndex):
        '''int QHeaderView.visualIndex(int logicalIndex)'''
        return int()
    def __len__(self):
        ''' QHeaderView.__len__()'''
        return ()
    def count(self):
        '''int QHeaderView.count()'''
        return int()
    def setSectionHidden(self, logicalIndex, hide):
        '''void QHeaderView.setSectionHidden(int logicalIndex, bool hide)'''
    def isSectionHidden(self, logicalIndex):
        '''bool QHeaderView.isSectionHidden(int logicalIndex)'''
        return bool()
    def resizeSection(self, logicalIndex, size):
        '''void QHeaderView.resizeSection(int logicalIndex, int size)'''
    def moveSection(self, from_, to):
        '''void QHeaderView.moveSection(int from, int to)'''
    def sectionViewportPosition(self, logicalIndex):
        '''int QHeaderView.sectionViewportPosition(int logicalIndex)'''
        return int()
    def sectionPosition(self, logicalIndex):
        '''int QHeaderView.sectionPosition(int logicalIndex)'''
        return int()
    def sectionSize(self, logicalIndex):
        '''int QHeaderView.sectionSize(int logicalIndex)'''
        return int()
    def logicalIndexAt(self, position):
        '''int QHeaderView.logicalIndexAt(int position)'''
        return int()
    def logicalIndexAt(self, ax, ay):
        '''int QHeaderView.logicalIndexAt(int ax, int ay)'''
        return int()
    def logicalIndexAt(self, apos):
        '''int QHeaderView.logicalIndexAt(QPoint apos)'''
        return int()
    def visualIndexAt(self, position):
        '''int QHeaderView.visualIndexAt(int position)'''
        return int()
    def sectionSizeHint(self, logicalIndex):
        '''int QHeaderView.sectionSizeHint(int logicalIndex)'''
        return int()
    def sizeHint(self):
        '''QSize QHeaderView.sizeHint()'''
        return QSize()
    def length(self):
        '''int QHeaderView.length()'''
        return int()
    def offset(self):
        '''int QHeaderView.offset()'''
        return int()
    def orientation(self):
        '''Qt.Orientation QHeaderView.orientation()'''
        return Qt.Orientation()
    def setModel(self, model):
        '''void QHeaderView.setModel(QAbstractItemModel model)'''


class QInputDialog(QDialog):
    """"""
    # Enum QInputDialog.InputMode
    TextInput = 0
    IntInput = 0
    DoubleInput = 0

    # Enum QInputDialog.InputDialogOption
    NoButtons = 0
    UseListViewForComboBoxItems = 0
    UsePlainTextEditForTextInput = 0

    def __init__(self, parent = None, flags = 0):
        '''void QInputDialog.__init__(QWidget parent = None, Qt.WindowFlags flags = 0)'''
    doubleValueSelected = pyqtSignal() # void doubleValueSelected(double) - signal
    doubleValueChanged = pyqtSignal() # void doubleValueChanged(double) - signal
    intValueSelected = pyqtSignal() # void intValueSelected(int) - signal
    intValueChanged = pyqtSignal() # void intValueChanged(int) - signal
    textValueSelected = pyqtSignal() # void textValueSelected(const QStringamp;) - signal
    textValueChanged = pyqtSignal() # void textValueChanged(const QStringamp;) - signal
    def done(self, result):
        '''void QInputDialog.done(int result)'''
    def setVisible(self, visible):
        '''void QInputDialog.setVisible(bool visible)'''
    def sizeHint(self):
        '''QSize QInputDialog.sizeHint()'''
        return QSize()
    def minimumSizeHint(self):
        '''QSize QInputDialog.minimumSizeHint()'''
        return QSize()
    def open(self):
        '''void QInputDialog.open()'''
    def open(self, slot):
        '''void QInputDialog.open(slot slot)'''
    def cancelButtonText(self):
        '''str QInputDialog.cancelButtonText()'''
        return str()
    def setCancelButtonText(self, text):
        '''void QInputDialog.setCancelButtonText(str text)'''
    def okButtonText(self):
        '''str QInputDialog.okButtonText()'''
        return str()
    def setOkButtonText(self, text):
        '''void QInputDialog.setOkButtonText(str text)'''
    def doubleDecimals(self):
        '''int QInputDialog.doubleDecimals()'''
        return int()
    def setDoubleDecimals(self, decimals):
        '''void QInputDialog.setDoubleDecimals(int decimals)'''
    def setDoubleRange(self, min, max):
        '''void QInputDialog.setDoubleRange(float min, float max)'''
    def doubleMaximum(self):
        '''float QInputDialog.doubleMaximum()'''
        return float()
    def setDoubleMaximum(self, max):
        '''void QInputDialog.setDoubleMaximum(float max)'''
    def doubleMinimum(self):
        '''float QInputDialog.doubleMinimum()'''
        return float()
    def setDoubleMinimum(self, min):
        '''void QInputDialog.setDoubleMinimum(float min)'''
    def doubleValue(self):
        '''float QInputDialog.doubleValue()'''
        return float()
    def setDoubleValue(self, value):
        '''void QInputDialog.setDoubleValue(float value)'''
    def intStep(self):
        '''int QInputDialog.intStep()'''
        return int()
    def setIntStep(self, step):
        '''void QInputDialog.setIntStep(int step)'''
    def setIntRange(self, min, max):
        '''void QInputDialog.setIntRange(int min, int max)'''
    def intMaximum(self):
        '''int QInputDialog.intMaximum()'''
        return int()
    def setIntMaximum(self, max):
        '''void QInputDialog.setIntMaximum(int max)'''
    def intMinimum(self):
        '''int QInputDialog.intMinimum()'''
        return int()
    def setIntMinimum(self, min):
        '''void QInputDialog.setIntMinimum(int min)'''
    def intValue(self):
        '''int QInputDialog.intValue()'''
        return int()
    def setIntValue(self, value):
        '''void QInputDialog.setIntValue(int value)'''
    def comboBoxItems(self):
        '''list-of-str QInputDialog.comboBoxItems()'''
        return [str()]
    def setComboBoxItems(self, items):
        '''void QInputDialog.setComboBoxItems(list-of-str items)'''
    def isComboBoxEditable(self):
        '''bool QInputDialog.isComboBoxEditable()'''
        return bool()
    def setComboBoxEditable(self, editable):
        '''void QInputDialog.setComboBoxEditable(bool editable)'''
    def textEchoMode(self):
        '''QLineEdit.EchoMode QInputDialog.textEchoMode()'''
        return QLineEdit.EchoMode()
    def setTextEchoMode(self, mode):
        '''void QInputDialog.setTextEchoMode(QLineEdit.EchoMode mode)'''
    def textValue(self):
        '''str QInputDialog.textValue()'''
        return str()
    def setTextValue(self, text):
        '''void QInputDialog.setTextValue(str text)'''
    def options(self):
        '''QInputDialog.InputDialogOptions QInputDialog.options()'''
        return QInputDialog.InputDialogOptions()
    def setOptions(self, options):
        '''void QInputDialog.setOptions(QInputDialog.InputDialogOptions options)'''
    def testOption(self, option):
        '''bool QInputDialog.testOption(QInputDialog.InputDialogOption option)'''
        return bool()
    def setOption(self, option, on = True):
        '''void QInputDialog.setOption(QInputDialog.InputDialogOption option, bool on = True)'''
    def labelText(self):
        '''str QInputDialog.labelText()'''
        return str()
    def setLabelText(self, text):
        '''void QInputDialog.setLabelText(str text)'''
    def inputMode(self):
        '''QInputDialog.InputMode QInputDialog.inputMode()'''
        return QInputDialog.InputMode()
    def setInputMode(self, mode):
        '''void QInputDialog.setInputMode(QInputDialog.InputMode mode)'''
    def getMultiLineText(self, parent, title, label, text = None, ok = None, flags = 0, inputMethodHints = None):
        '''static str QInputDialog.getMultiLineText(QWidget parent, str title, str label, str text = '', bool ok, Qt.WindowFlags flags = 0, Qt.InputMethodHints inputMethodHints = Qt.ImhNone)'''
        return str()
    def getItem(self, parent, title, label, items, current = 0, editable = True, ok = None, flags = 0, inputMethodHints = None):
        '''static str QInputDialog.getItem(QWidget parent, str title, str label, list-of-str items, int current = 0, bool editable = True, bool ok, Qt.WindowFlags flags = 0, Qt.InputMethodHints inputMethodHints = Qt.ImhNone)'''
        return str()
    def getDouble(self, parent, title, label, value = 0, min = None, max = 2147483647, decimals = 1, ok = None, flags = 0):
        '''static float QInputDialog.getDouble(QWidget parent, str title, str label, float value = 0, float min = -2147483647, float max = 2147483647, int decimals = 1, bool ok, Qt.WindowFlags flags = 0)'''
        return float()
    def getInt(self, parent, title, label, value = 0, min = None, max = 2147483647, step = 1, ok = None, flags = 0):
        '''static int QInputDialog.getInt(QWidget parent, str title, str label, int value = 0, int min = -2147483647, int max = 2147483647, int step = 1, bool ok, Qt.WindowFlags flags = 0)'''
        return int()
    def getText(self, parent, title, label, echo = None, text = str(), ok = None, flags = 0, inputMethodHints = None):
        '''static str QInputDialog.getText(QWidget parent, str title, str label, QLineEdit.EchoMode echo = QLineEdit.Normal, str text = str(), bool ok, Qt.WindowFlags flags = 0, Qt.InputMethodHints inputMethodHints = Qt.ImhNone)'''
        return str()
    class InputDialogOptions():
        """"""
        def __init__(self):
            '''QInputDialog.InputDialogOptions QInputDialog.InputDialogOptions.__init__()'''
            return QInputDialog.InputDialogOptions()
        def __init__(self):
            '''int QInputDialog.InputDialogOptions.__init__()'''
            return int()
        def __init__(self):
            '''void QInputDialog.InputDialogOptions.__init__()'''
        def __bool__(self):
            '''int QInputDialog.InputDialogOptions.__bool__()'''
            return int()
        def __ne__(self, f):
            '''bool QInputDialog.InputDialogOptions.__ne__(QInputDialog.InputDialogOptions f)'''
            return bool()
        def __eq__(self, f):
            '''bool QInputDialog.InputDialogOptions.__eq__(QInputDialog.InputDialogOptions f)'''
            return bool()
        def __invert__(self):
            '''QInputDialog.InputDialogOptions QInputDialog.InputDialogOptions.__invert__()'''
            return QInputDialog.InputDialogOptions()
        def __and__(self, mask):
            '''QInputDialog.InputDialogOptions QInputDialog.InputDialogOptions.__and__(int mask)'''
            return QInputDialog.InputDialogOptions()
        def __xor__(self, f):
            '''QInputDialog.InputDialogOptions QInputDialog.InputDialogOptions.__xor__(QInputDialog.InputDialogOptions f)'''
            return QInputDialog.InputDialogOptions()
        def __xor__(self, f):
            '''QInputDialog.InputDialogOptions QInputDialog.InputDialogOptions.__xor__(int f)'''
            return QInputDialog.InputDialogOptions()
        def __or__(self, f):
            '''QInputDialog.InputDialogOptions QInputDialog.InputDialogOptions.__or__(QInputDialog.InputDialogOptions f)'''
            return QInputDialog.InputDialogOptions()
        def __or__(self, f):
            '''QInputDialog.InputDialogOptions QInputDialog.InputDialogOptions.__or__(int f)'''
            return QInputDialog.InputDialogOptions()
        def __int__(self):
            '''int QInputDialog.InputDialogOptions.__int__()'''
            return int()
        def __ixor__(self, f):
            '''QInputDialog.InputDialogOptions QInputDialog.InputDialogOptions.__ixor__(QInputDialog.InputDialogOptions f)'''
            return QInputDialog.InputDialogOptions()
        def __ior__(self, f):
            '''QInputDialog.InputDialogOptions QInputDialog.InputDialogOptions.__ior__(QInputDialog.InputDialogOptions f)'''
            return QInputDialog.InputDialogOptions()
        def __iand__(self, mask):
            '''QInputDialog.InputDialogOptions QInputDialog.InputDialogOptions.__iand__(int mask)'''
            return QInputDialog.InputDialogOptions()


class QItemDelegate(QAbstractItemDelegate):
    """"""
    def __init__(self, parent = None):
        '''void QItemDelegate.__init__(QObject parent = None)'''
    def editorEvent(self, event, model, option, index):
        '''bool QItemDelegate.editorEvent(QEvent event, QAbstractItemModel model, QStyleOptionViewItem option, QModelIndex index)'''
        return bool()
    def eventFilter(self, object, event):
        '''bool QItemDelegate.eventFilter(QObject object, QEvent event)'''
        return bool()
    def drawFocus(self, painter, option, rect):
        '''void QItemDelegate.drawFocus(QPainter painter, QStyleOptionViewItem option, QRect rect)'''
    def drawDisplay(self, painter, option, rect, text):
        '''void QItemDelegate.drawDisplay(QPainter painter, QStyleOptionViewItem option, QRect rect, str text)'''
    def drawDecoration(self, painter, option, rect, pixmap):
        '''void QItemDelegate.drawDecoration(QPainter painter, QStyleOptionViewItem option, QRect rect, QPixmap pixmap)'''
    def drawCheck(self, painter, option, rect, state):
        '''void QItemDelegate.drawCheck(QPainter painter, QStyleOptionViewItem option, QRect rect, Qt.CheckState state)'''
    def drawBackground(self, painter, option, index):
        '''void QItemDelegate.drawBackground(QPainter painter, QStyleOptionViewItem option, QModelIndex index)'''
    def setClipping(self, clip):
        '''void QItemDelegate.setClipping(bool clip)'''
    def hasClipping(self):
        '''bool QItemDelegate.hasClipping()'''
        return bool()
    def setItemEditorFactory(self, factory):
        '''void QItemDelegate.setItemEditorFactory(QItemEditorFactory factory)'''
    def itemEditorFactory(self):
        '''QItemEditorFactory QItemDelegate.itemEditorFactory()'''
        return QItemEditorFactory()
    def updateEditorGeometry(self, editor, option, index):
        '''void QItemDelegate.updateEditorGeometry(QWidget editor, QStyleOptionViewItem option, QModelIndex index)'''
    def setModelData(self, editor, model, index):
        '''void QItemDelegate.setModelData(QWidget editor, QAbstractItemModel model, QModelIndex index)'''
    def setEditorData(self, editor, index):
        '''void QItemDelegate.setEditorData(QWidget editor, QModelIndex index)'''
    def createEditor(self, parent, option, index):
        '''QWidget QItemDelegate.createEditor(QWidget parent, QStyleOptionViewItem option, QModelIndex index)'''
        return QWidget()
    def sizeHint(self, option, index):
        '''QSize QItemDelegate.sizeHint(QStyleOptionViewItem option, QModelIndex index)'''
        return QSize()
    def paint(self, painter, option, index):
        '''void QItemDelegate.paint(QPainter painter, QStyleOptionViewItem option, QModelIndex index)'''


class QItemEditorCreatorBase():
    """"""
    def __init__(self):
        '''void QItemEditorCreatorBase.__init__()'''
    def __init__(self):
        '''QItemEditorCreatorBase QItemEditorCreatorBase.__init__()'''
        return QItemEditorCreatorBase()
    def valuePropertyName(self):
        '''abstract QByteArray QItemEditorCreatorBase.valuePropertyName()'''
        return QByteArray()
    def createWidget(self, parent):
        '''abstract QWidget QItemEditorCreatorBase.createWidget(QWidget parent)'''
        return QWidget()


class QItemEditorFactory():
    """"""
    def __init__(self):
        '''void QItemEditorFactory.__init__()'''
    def __init__(self):
        '''QItemEditorFactory QItemEditorFactory.__init__()'''
        return QItemEditorFactory()
    def setDefaultFactory(self, factory):
        '''static void QItemEditorFactory.setDefaultFactory(QItemEditorFactory factory)'''
    def defaultFactory(self):
        '''static QItemEditorFactory QItemEditorFactory.defaultFactory()'''
        return QItemEditorFactory()
    def registerEditor(self, userType, creator):
        '''void QItemEditorFactory.registerEditor(int userType, QItemEditorCreatorBase creator)'''
    def valuePropertyName(self, userType):
        '''QByteArray QItemEditorFactory.valuePropertyName(int userType)'''
        return QByteArray()
    def createEditor(self, userType, parent):
        '''QWidget QItemEditorFactory.createEditor(int userType, QWidget parent)'''
        return QWidget()


class QKeyEventTransition(QEventTransition):
    """"""
    def __init__(self, sourceState = None):
        '''void QKeyEventTransition.__init__(QState sourceState = None)'''
    def __init__(self, object, type, key, sourceState = None):
        '''void QKeyEventTransition.__init__(QObject object, QEvent.Type type, int key, QState sourceState = None)'''
    def eventTest(self, event):
        '''bool QKeyEventTransition.eventTest(QEvent event)'''
        return bool()
    def onTransition(self, event):
        '''void QKeyEventTransition.onTransition(QEvent event)'''
    def setModifierMask(self, modifiers):
        '''void QKeyEventTransition.setModifierMask(Qt.KeyboardModifiers modifiers)'''
    def modifierMask(self):
        '''Qt.KeyboardModifiers QKeyEventTransition.modifierMask()'''
        return Qt.KeyboardModifiers()
    def setKey(self, key):
        '''void QKeyEventTransition.setKey(int key)'''
    def key(self):
        '''int QKeyEventTransition.key()'''
        return int()


class QKeySequenceEdit(QWidget):
    """"""
    def __init__(self, parent = None):
        '''void QKeySequenceEdit.__init__(QWidget parent = None)'''
    def __init__(self, keySequence, parent = None):
        '''void QKeySequenceEdit.__init__(QKeySequence keySequence, QWidget parent = None)'''
    def timerEvent(self):
        '''QTimerEvent QKeySequenceEdit.timerEvent()'''
        return QTimerEvent()
    def keyReleaseEvent(self):
        '''QKeyEvent QKeySequenceEdit.keyReleaseEvent()'''
        return QKeyEvent()
    def keyPressEvent(self):
        '''QKeyEvent QKeySequenceEdit.keyPressEvent()'''
        return QKeyEvent()
    def event(self):
        '''QEvent QKeySequenceEdit.event()'''
        return QEvent()
    keySequenceChanged = pyqtSignal() # void keySequenceChanged(const QKeySequenceamp;) - signal
    editingFinished = pyqtSignal() # void editingFinished() - signal
    def clear(self):
        '''void QKeySequenceEdit.clear()'''
    def setKeySequence(self, keySequence):
        '''void QKeySequenceEdit.setKeySequence(QKeySequence keySequence)'''
    def keySequence(self):
        '''QKeySequence QKeySequenceEdit.keySequence()'''
        return QKeySequence()


class QLabel(QFrame):
    """"""
    def __init__(self, parent = None, flags = 0):
        '''void QLabel.__init__(QWidget parent = None, Qt.WindowFlags flags = 0)'''
    def __init__(self, text, parent = None, flags = 0):
        '''void QLabel.__init__(str text, QWidget parent = None, Qt.WindowFlags flags = 0)'''
    def selectionStart(self):
        '''int QLabel.selectionStart()'''
        return int()
    def selectedText(self):
        '''str QLabel.selectedText()'''
        return str()
    def hasSelectedText(self):
        '''bool QLabel.hasSelectedText()'''
        return bool()
    def setSelection(self):
        '''int QLabel.setSelection()'''
        return int()
    def focusNextPrevChild(self, next):
        '''bool QLabel.focusNextPrevChild(bool next)'''
        return bool()
    def focusOutEvent(self, ev):
        '''void QLabel.focusOutEvent(QFocusEvent ev)'''
    def focusInEvent(self, ev):
        '''void QLabel.focusInEvent(QFocusEvent ev)'''
    def contextMenuEvent(self, ev):
        '''void QLabel.contextMenuEvent(QContextMenuEvent ev)'''
    def mouseReleaseEvent(self, ev):
        '''void QLabel.mouseReleaseEvent(QMouseEvent ev)'''
    def mouseMoveEvent(self, ev):
        '''void QLabel.mouseMoveEvent(QMouseEvent ev)'''
    def mousePressEvent(self, ev):
        '''void QLabel.mousePressEvent(QMouseEvent ev)'''
    def keyPressEvent(self, ev):
        '''void QLabel.keyPressEvent(QKeyEvent ev)'''
    def changeEvent(self):
        '''QEvent QLabel.changeEvent()'''
        return QEvent()
    def paintEvent(self):
        '''QPaintEvent QLabel.paintEvent()'''
        return QPaintEvent()
    def event(self, e):
        '''bool QLabel.event(QEvent e)'''
        return bool()
    linkHovered = pyqtSignal() # void linkHovered(const QStringamp;) - signal
    linkActivated = pyqtSignal() # void linkActivated(const QStringamp;) - signal
    def setText(self):
        '''str QLabel.setText()'''
        return str()
    def setPixmap(self):
        '''QPixmap QLabel.setPixmap()'''
        return QPixmap()
    def setPicture(self):
        '''QPicture QLabel.setPicture()'''
        return QPicture()
    def setNum(self):
        '''float QLabel.setNum()'''
        return float()
    def setNum(self):
        '''int QLabel.setNum()'''
        return int()
    def setMovie(self, movie):
        '''void QLabel.setMovie(QMovie movie)'''
    def clear(self):
        '''void QLabel.clear()'''
    def setOpenExternalLinks(self, open):
        '''void QLabel.setOpenExternalLinks(bool open)'''
    def textInteractionFlags(self):
        '''Qt.TextInteractionFlags QLabel.textInteractionFlags()'''
        return Qt.TextInteractionFlags()
    def setTextInteractionFlags(self, flags):
        '''void QLabel.setTextInteractionFlags(Qt.TextInteractionFlags flags)'''
    def openExternalLinks(self):
        '''bool QLabel.openExternalLinks()'''
        return bool()
    def heightForWidth(self):
        '''int QLabel.heightForWidth()'''
        return int()
    def buddy(self):
        '''QWidget QLabel.buddy()'''
        return QWidget()
    def setBuddy(self):
        '''QWidget QLabel.setBuddy()'''
        return QWidget()
    def minimumSizeHint(self):
        '''QSize QLabel.minimumSizeHint()'''
        return QSize()
    def sizeHint(self):
        '''QSize QLabel.sizeHint()'''
        return QSize()
    def setScaledContents(self):
        '''bool QLabel.setScaledContents()'''
        return bool()
    def hasScaledContents(self):
        '''bool QLabel.hasScaledContents()'''
        return bool()
    def setMargin(self):
        '''int QLabel.setMargin()'''
        return int()
    def margin(self):
        '''int QLabel.margin()'''
        return int()
    def setIndent(self):
        '''int QLabel.setIndent()'''
        return int()
    def indent(self):
        '''int QLabel.indent()'''
        return int()
    def wordWrap(self):
        '''bool QLabel.wordWrap()'''
        return bool()
    def setWordWrap(self, on):
        '''void QLabel.setWordWrap(bool on)'''
    def setAlignment(self):
        '''Qt.Alignment QLabel.setAlignment()'''
        return Qt.Alignment()
    def alignment(self):
        '''Qt.Alignment QLabel.alignment()'''
        return Qt.Alignment()
    def setTextFormat(self):
        '''Qt.TextFormat QLabel.setTextFormat()'''
        return Qt.TextFormat()
    def textFormat(self):
        '''Qt.TextFormat QLabel.textFormat()'''
        return Qt.TextFormat()
    def movie(self):
        '''QMovie QLabel.movie()'''
        return QMovie()
    def picture(self):
        '''QPicture QLabel.picture()'''
        return QPicture()
    def pixmap(self):
        '''QPixmap QLabel.pixmap()'''
        return QPixmap()
    def text(self):
        '''str QLabel.text()'''
        return str()


class QSpacerItem(QLayoutItem):
    """"""
    def __init__(self, w, h, hPolicy = None, vPolicy = None):
        '''void QSpacerItem.__init__(int w, int h, QSizePolicy.Policy hPolicy = QSizePolicy.Minimum, QSizePolicy.Policy vPolicy = QSizePolicy.Minimum)'''
    def __init__(self):
        '''QSpacerItem QSpacerItem.__init__()'''
        return QSpacerItem()
    def sizePolicy(self):
        '''QSizePolicy QSpacerItem.sizePolicy()'''
        return QSizePolicy()
    def spacerItem(self):
        '''QSpacerItem QSpacerItem.spacerItem()'''
        return QSpacerItem()
    def geometry(self):
        '''QRect QSpacerItem.geometry()'''
        return QRect()
    def setGeometry(self):
        '''QRect QSpacerItem.setGeometry()'''
        return QRect()
    def isEmpty(self):
        '''bool QSpacerItem.isEmpty()'''
        return bool()
    def expandingDirections(self):
        '''Qt.Orientations QSpacerItem.expandingDirections()'''
        return Qt.Orientations()
    def maximumSize(self):
        '''QSize QSpacerItem.maximumSize()'''
        return QSize()
    def minimumSize(self):
        '''QSize QSpacerItem.minimumSize()'''
        return QSize()
    def sizeHint(self):
        '''QSize QSpacerItem.sizeHint()'''
        return QSize()
    def changeSize(self, w, h, hPolicy = None, vPolicy = None):
        '''void QSpacerItem.changeSize(int w, int h, QSizePolicy.Policy hPolicy = QSizePolicy.Minimum, QSizePolicy.Policy vPolicy = QSizePolicy.Minimum)'''


class QWidgetItem(QLayoutItem):
    """"""
    def __init__(self, w):
        '''void QWidgetItem.__init__(QWidget w)'''
    def controlTypes(self):
        '''QSizePolicy.ControlTypes QWidgetItem.controlTypes()'''
        return QSizePolicy.ControlTypes()
    def heightForWidth(self):
        '''int QWidgetItem.heightForWidth()'''
        return int()
    def hasHeightForWidth(self):
        '''bool QWidgetItem.hasHeightForWidth()'''
        return bool()
    def widget(self):
        '''QWidget QWidgetItem.widget()'''
        return QWidget()
    def geometry(self):
        '''QRect QWidgetItem.geometry()'''
        return QRect()
    def setGeometry(self):
        '''QRect QWidgetItem.setGeometry()'''
        return QRect()
    def isEmpty(self):
        '''bool QWidgetItem.isEmpty()'''
        return bool()
    def expandingDirections(self):
        '''Qt.Orientations QWidgetItem.expandingDirections()'''
        return Qt.Orientations()
    def maximumSize(self):
        '''QSize QWidgetItem.maximumSize()'''
        return QSize()
    def minimumSize(self):
        '''QSize QWidgetItem.minimumSize()'''
        return QSize()
    def sizeHint(self):
        '''QSize QWidgetItem.sizeHint()'''
        return QSize()


class QLCDNumber(QFrame):
    """"""
    # Enum QLCDNumber.SegmentStyle
    Outline = 0
    Filled = 0
    Flat = 0

    # Enum QLCDNumber.Mode
    Hex = 0
    Dec = 0
    Oct = 0
    Bin = 0

    def __init__(self, parent = None):
        '''void QLCDNumber.__init__(QWidget parent = None)'''
    def __init__(self, numDigits, parent = None):
        '''void QLCDNumber.__init__(int numDigits, QWidget parent = None)'''
    def paintEvent(self):
        '''QPaintEvent QLCDNumber.paintEvent()'''
        return QPaintEvent()
    def event(self, e):
        '''bool QLCDNumber.event(QEvent e)'''
        return bool()
    overflow = pyqtSignal() # void overflow() - signal
    def setSmallDecimalPoint(self):
        '''bool QLCDNumber.setSmallDecimalPoint()'''
        return bool()
    def setBinMode(self):
        '''void QLCDNumber.setBinMode()'''
    def setOctMode(self):
        '''void QLCDNumber.setOctMode()'''
    def setDecMode(self):
        '''void QLCDNumber.setDecMode()'''
    def setHexMode(self):
        '''void QLCDNumber.setHexMode()'''
    def display(self, str):
        '''void QLCDNumber.display(str str)'''
    def display(self, num):
        '''void QLCDNumber.display(float num)'''
    def display(self, num):
        '''void QLCDNumber.display(int num)'''
    def sizeHint(self):
        '''QSize QLCDNumber.sizeHint()'''
        return QSize()
    def intValue(self):
        '''int QLCDNumber.intValue()'''
        return int()
    def value(self):
        '''float QLCDNumber.value()'''
        return float()
    def setSegmentStyle(self):
        '''QLCDNumber.SegmentStyle QLCDNumber.setSegmentStyle()'''
        return QLCDNumber.SegmentStyle()
    def segmentStyle(self):
        '''QLCDNumber.SegmentStyle QLCDNumber.segmentStyle()'''
        return QLCDNumber.SegmentStyle()
    def setMode(self):
        '''QLCDNumber.Mode QLCDNumber.setMode()'''
        return QLCDNumber.Mode()
    def mode(self):
        '''QLCDNumber.Mode QLCDNumber.mode()'''
        return QLCDNumber.Mode()
    def checkOverflow(self, num):
        '''bool QLCDNumber.checkOverflow(float num)'''
        return bool()
    def checkOverflow(self, num):
        '''bool QLCDNumber.checkOverflow(int num)'''
        return bool()
    def setNumDigits(self, nDigits):
        '''void QLCDNumber.setNumDigits(int nDigits)'''
    def setDigitCount(self, nDigits):
        '''void QLCDNumber.setDigitCount(int nDigits)'''
    def digitCount(self):
        '''int QLCDNumber.digitCount()'''
        return int()
    def smallDecimalPoint(self):
        '''bool QLCDNumber.smallDecimalPoint()'''
        return bool()


class QLineEdit(QWidget):
    """"""
    # Enum QLineEdit.ActionPosition
    LeadingPosition = 0
    TrailingPosition = 0

    # Enum QLineEdit.EchoMode
    Normal = 0
    NoEcho = 0
    Password = 0
    PasswordEchoOnEdit = 0

    def __init__(self, parent = None):
        '''void QLineEdit.__init__(QWidget parent = None)'''
    def __init__(self, contents, parent = None):
        '''void QLineEdit.__init__(str contents, QWidget parent = None)'''
    def addAction(self, action):
        '''void QLineEdit.addAction(QAction action)'''
    def addAction(self, action, position):
        '''void QLineEdit.addAction(QAction action, QLineEdit.ActionPosition position)'''
    def addAction(self, icon, position):
        '''QAction QLineEdit.addAction(QIcon icon, QLineEdit.ActionPosition position)'''
        return QAction()
    def isClearButtonEnabled(self):
        '''bool QLineEdit.isClearButtonEnabled()'''
        return bool()
    def setClearButtonEnabled(self, enable):
        '''void QLineEdit.setClearButtonEnabled(bool enable)'''
    def cursorMoveStyle(self):
        '''Qt.CursorMoveStyle QLineEdit.cursorMoveStyle()'''
        return Qt.CursorMoveStyle()
    def setCursorMoveStyle(self, style):
        '''void QLineEdit.setCursorMoveStyle(Qt.CursorMoveStyle style)'''
    def setPlaceholderText(self):
        '''str QLineEdit.setPlaceholderText()'''
        return str()
    def placeholderText(self):
        '''str QLineEdit.placeholderText()'''
        return str()
    def textMargins(self):
        '''QMargins QLineEdit.textMargins()'''
        return QMargins()
    def getTextMargins(self, left, top, right, bottom):
        '''void QLineEdit.getTextMargins(int left, int top, int right, int bottom)'''
    def setTextMargins(self, left, top, right, bottom):
        '''void QLineEdit.setTextMargins(int left, int top, int right, int bottom)'''
    def setTextMargins(self, margins):
        '''void QLineEdit.setTextMargins(QMargins margins)'''
    def completer(self):
        '''QCompleter QLineEdit.completer()'''
        return QCompleter()
    def setCompleter(self, completer):
        '''void QLineEdit.setCompleter(QCompleter completer)'''
    def event(self):
        '''QEvent QLineEdit.event()'''
        return QEvent()
    def inputMethodQuery(self):
        '''Qt.InputMethodQuery QLineEdit.inputMethodQuery()'''
        return Qt.InputMethodQuery()
    def cursorRect(self):
        '''QRect QLineEdit.cursorRect()'''
        return QRect()
    def inputMethodEvent(self):
        '''QInputMethodEvent QLineEdit.inputMethodEvent()'''
        return QInputMethodEvent()
    def contextMenuEvent(self):
        '''QContextMenuEvent QLineEdit.contextMenuEvent()'''
        return QContextMenuEvent()
    def changeEvent(self):
        '''QEvent QLineEdit.changeEvent()'''
        return QEvent()
    def dropEvent(self):
        '''QDropEvent QLineEdit.dropEvent()'''
        return QDropEvent()
    def dragLeaveEvent(self, e):
        '''void QLineEdit.dragLeaveEvent(QDragLeaveEvent e)'''
    def dragMoveEvent(self, e):
        '''void QLineEdit.dragMoveEvent(QDragMoveEvent e)'''
    def dragEnterEvent(self):
        '''QDragEnterEvent QLineEdit.dragEnterEvent()'''
        return QDragEnterEvent()
    def paintEvent(self):
        '''QPaintEvent QLineEdit.paintEvent()'''
        return QPaintEvent()
    def focusOutEvent(self):
        '''QFocusEvent QLineEdit.focusOutEvent()'''
        return QFocusEvent()
    def focusInEvent(self):
        '''QFocusEvent QLineEdit.focusInEvent()'''
        return QFocusEvent()
    def keyPressEvent(self):
        '''QKeyEvent QLineEdit.keyPressEvent()'''
        return QKeyEvent()
    def mouseDoubleClickEvent(self):
        '''QMouseEvent QLineEdit.mouseDoubleClickEvent()'''
        return QMouseEvent()
    def mouseReleaseEvent(self):
        '''QMouseEvent QLineEdit.mouseReleaseEvent()'''
        return QMouseEvent()
    def mouseMoveEvent(self):
        '''QMouseEvent QLineEdit.mouseMoveEvent()'''
        return QMouseEvent()
    def mousePressEvent(self):
        '''QMouseEvent QLineEdit.mousePressEvent()'''
        return QMouseEvent()
    def initStyleOption(self, option):
        '''void QLineEdit.initStyleOption(QStyleOptionFrame option)'''
    selectionChanged = pyqtSignal() # void selectionChanged() - signal
    editingFinished = pyqtSignal() # void editingFinished() - signal
    returnPressed = pyqtSignal() # void returnPressed() - signal
    cursorPositionChanged = pyqtSignal() # void cursorPositionChanged(int,int) - signal
    textEdited = pyqtSignal() # void textEdited(const QStringamp;) - signal
    textChanged = pyqtSignal() # void textChanged(const QStringamp;) - signal
    def createStandardContextMenu(self):
        '''QMenu QLineEdit.createStandardContextMenu()'''
        return QMenu()
    def insert(self):
        '''str QLineEdit.insert()'''
        return str()
    def deselect(self):
        '''void QLineEdit.deselect()'''
    def paste(self):
        '''void QLineEdit.paste()'''
    def copy(self):
        '''void QLineEdit.copy()'''
    def cut(self):
        '''void QLineEdit.cut()'''
    def redo(self):
        '''void QLineEdit.redo()'''
    def undo(self):
        '''void QLineEdit.undo()'''
    def selectAll(self):
        '''void QLineEdit.selectAll()'''
    def clear(self):
        '''void QLineEdit.clear()'''
    def setText(self):
        '''str QLineEdit.setText()'''
        return str()
    def hasAcceptableInput(self):
        '''bool QLineEdit.hasAcceptableInput()'''
        return bool()
    def setInputMask(self, inputMask):
        '''void QLineEdit.setInputMask(str inputMask)'''
    def inputMask(self):
        '''str QLineEdit.inputMask()'''
        return str()
    def dragEnabled(self):
        '''bool QLineEdit.dragEnabled()'''
        return bool()
    def setDragEnabled(self, b):
        '''void QLineEdit.setDragEnabled(bool b)'''
    def isRedoAvailable(self):
        '''bool QLineEdit.isRedoAvailable()'''
        return bool()
    def isUndoAvailable(self):
        '''bool QLineEdit.isUndoAvailable()'''
        return bool()
    def selectionStart(self):
        '''int QLineEdit.selectionStart()'''
        return int()
    def selectedText(self):
        '''str QLineEdit.selectedText()'''
        return str()
    def hasSelectedText(self):
        '''bool QLineEdit.hasSelectedText()'''
        return bool()
    def setSelection(self):
        '''int QLineEdit.setSelection()'''
        return int()
    def setModified(self):
        '''bool QLineEdit.setModified()'''
        return bool()
    def isModified(self):
        '''bool QLineEdit.isModified()'''
        return bool()
    def end(self, mark):
        '''void QLineEdit.end(bool mark)'''
    def home(self, mark):
        '''void QLineEdit.home(bool mark)'''
    def del_(self):
        '''void QLineEdit.del_()'''
    def backspace(self):
        '''void QLineEdit.backspace()'''
    def cursorWordBackward(self, mark):
        '''void QLineEdit.cursorWordBackward(bool mark)'''
    def cursorWordForward(self, mark):
        '''void QLineEdit.cursorWordForward(bool mark)'''
    def cursorBackward(self, mark, steps = 1):
        '''void QLineEdit.cursorBackward(bool mark, int steps = 1)'''
    def cursorForward(self, mark, steps = 1):
        '''void QLineEdit.cursorForward(bool mark, int steps = 1)'''
    def alignment(self):
        '''Qt.Alignment QLineEdit.alignment()'''
        return Qt.Alignment()
    def setAlignment(self, flag):
        '''void QLineEdit.setAlignment(Qt.Alignment flag)'''
    def cursorPositionAt(self, pos):
        '''int QLineEdit.cursorPositionAt(QPoint pos)'''
        return int()
    def setCursorPosition(self):
        '''int QLineEdit.setCursorPosition()'''
        return int()
    def cursorPosition(self):
        '''int QLineEdit.cursorPosition()'''
        return int()
    def minimumSizeHint(self):
        '''QSize QLineEdit.minimumSizeHint()'''
        return QSize()
    def sizeHint(self):
        '''QSize QLineEdit.sizeHint()'''
        return QSize()
    def validator(self):
        '''QValidator QLineEdit.validator()'''
        return QValidator()
    def setValidator(self):
        '''QValidator QLineEdit.setValidator()'''
        return QValidator()
    def setReadOnly(self):
        '''bool QLineEdit.setReadOnly()'''
        return bool()
    def isReadOnly(self):
        '''bool QLineEdit.isReadOnly()'''
        return bool()
    def setEchoMode(self):
        '''QLineEdit.EchoMode QLineEdit.setEchoMode()'''
        return QLineEdit.EchoMode()
    def echoMode(self):
        '''QLineEdit.EchoMode QLineEdit.echoMode()'''
        return QLineEdit.EchoMode()
    def hasFrame(self):
        '''bool QLineEdit.hasFrame()'''
        return bool()
    def setFrame(self):
        '''bool QLineEdit.setFrame()'''
        return bool()
    def setMaxLength(self):
        '''int QLineEdit.setMaxLength()'''
        return int()
    def maxLength(self):
        '''int QLineEdit.maxLength()'''
        return int()
    def displayText(self):
        '''str QLineEdit.displayText()'''
        return str()
    def text(self):
        '''str QLineEdit.text()'''
        return str()


class QListView(QAbstractItemView):
    """"""
    # Enum QListView.ViewMode
    ListMode = 0
    IconMode = 0

    # Enum QListView.LayoutMode
    SinglePass = 0
    Batched = 0

    # Enum QListView.ResizeMode
    Fixed = 0
    Adjust = 0

    # Enum QListView.Flow
    LeftToRight = 0
    TopToBottom = 0

    # Enum QListView.Movement
    Static = 0
    Free = 0
    Snap = 0

    def __init__(self, parent = None):
        '''void QListView.__init__(QWidget parent = None)'''
    def currentChanged(self, current, previous):
        '''void QListView.currentChanged(QModelIndex current, QModelIndex previous)'''
    def selectionChanged(self, selected, deselected):
        '''void QListView.selectionChanged(QItemSelection selected, QItemSelection deselected)'''
    def isSelectionRectVisible(self):
        '''bool QListView.isSelectionRectVisible()'''
        return bool()
    def setSelectionRectVisible(self, show):
        '''void QListView.setSelectionRectVisible(bool show)'''
    def wordWrap(self):
        '''bool QListView.wordWrap()'''
        return bool()
    def setWordWrap(self, on):
        '''void QListView.setWordWrap(bool on)'''
    def batchSize(self):
        '''int QListView.batchSize()'''
        return int()
    def setBatchSize(self, batchSize):
        '''void QListView.setBatchSize(int batchSize)'''
    def viewportSizeHint(self):
        '''QSize QListView.viewportSizeHint()'''
        return QSize()
    def isIndexHidden(self, index):
        '''bool QListView.isIndexHidden(QModelIndex index)'''
        return bool()
    def updateGeometries(self):
        '''void QListView.updateGeometries()'''
    def selectedIndexes(self):
        '''list-of-QModelIndex QListView.selectedIndexes()'''
        return [QModelIndex()]
    def visualRegionForSelection(self, selection):
        '''QRegion QListView.visualRegionForSelection(QItemSelection selection)'''
        return QRegion()
    def setSelection(self, rect, command):
        '''void QListView.setSelection(QRect rect, QItemSelectionModel.SelectionFlags command)'''
    def setPositionForIndex(self, position, index):
        '''void QListView.setPositionForIndex(QPoint position, QModelIndex index)'''
    def rectForIndex(self, index):
        '''QRect QListView.rectForIndex(QModelIndex index)'''
        return QRect()
    def moveCursor(self, cursorAction, modifiers):
        '''QModelIndex QListView.moveCursor(QAbstractItemView.CursorAction cursorAction, Qt.KeyboardModifiers modifiers)'''
        return QModelIndex()
    def verticalOffset(self):
        '''int QListView.verticalOffset()'''
        return int()
    def horizontalOffset(self):
        '''int QListView.horizontalOffset()'''
        return int()
    def paintEvent(self, e):
        '''void QListView.paintEvent(QPaintEvent e)'''
    def viewOptions(self):
        '''QStyleOptionViewItem QListView.viewOptions()'''
        return QStyleOptionViewItem()
    def startDrag(self, supportedActions):
        '''void QListView.startDrag(Qt.DropActions supportedActions)'''
    def dropEvent(self, e):
        '''void QListView.dropEvent(QDropEvent e)'''
    def dragLeaveEvent(self, e):
        '''void QListView.dragLeaveEvent(QDragLeaveEvent e)'''
    def dragMoveEvent(self, e):
        '''void QListView.dragMoveEvent(QDragMoveEvent e)'''
    def resizeEvent(self, e):
        '''void QListView.resizeEvent(QResizeEvent e)'''
    def timerEvent(self, e):
        '''void QListView.timerEvent(QTimerEvent e)'''
    def mouseReleaseEvent(self, e):
        '''void QListView.mouseReleaseEvent(QMouseEvent e)'''
    def mouseMoveEvent(self, e):
        '''void QListView.mouseMoveEvent(QMouseEvent e)'''
    def event(self, e):
        '''bool QListView.event(QEvent e)'''
        return bool()
    def rowsAboutToBeRemoved(self, parent, start, end):
        '''void QListView.rowsAboutToBeRemoved(QModelIndex parent, int start, int end)'''
    def rowsInserted(self, parent, start, end):
        '''void QListView.rowsInserted(QModelIndex parent, int start, int end)'''
    def dataChanged(self, topLeft, bottomRight, roles = None):
        '''void QListView.dataChanged(QModelIndex topLeft, QModelIndex bottomRight, list-of-int roles = [])'''
    def scrollContentsBy(self, dx, dy):
        '''void QListView.scrollContentsBy(int dx, int dy)'''
    indexesMoved = pyqtSignal() # void indexesMoved(const QModelIndexListamp;) - signal
    def setRootIndex(self, index):
        '''void QListView.setRootIndex(QModelIndex index)'''
    def reset(self):
        '''void QListView.reset()'''
    def indexAt(self, p):
        '''QModelIndex QListView.indexAt(QPoint p)'''
        return QModelIndex()
    def scrollTo(self, index, hint = None):
        '''void QListView.scrollTo(QModelIndex index, QAbstractItemView.ScrollHint hint = QAbstractItemView.EnsureVisible)'''
    def visualRect(self, index):
        '''QRect QListView.visualRect(QModelIndex index)'''
        return QRect()
    def uniformItemSizes(self):
        '''bool QListView.uniformItemSizes()'''
        return bool()
    def setUniformItemSizes(self, enable):
        '''void QListView.setUniformItemSizes(bool enable)'''
    def modelColumn(self):
        '''int QListView.modelColumn()'''
        return int()
    def setModelColumn(self, column):
        '''void QListView.setModelColumn(int column)'''
    def setRowHidden(self, row, hide):
        '''void QListView.setRowHidden(int row, bool hide)'''
    def isRowHidden(self, row):
        '''bool QListView.isRowHidden(int row)'''
        return bool()
    def clearPropertyFlags(self):
        '''void QListView.clearPropertyFlags()'''
    def viewMode(self):
        '''QListView.ViewMode QListView.viewMode()'''
        return QListView.ViewMode()
    def setViewMode(self, mode):
        '''void QListView.setViewMode(QListView.ViewMode mode)'''
    def gridSize(self):
        '''QSize QListView.gridSize()'''
        return QSize()
    def setGridSize(self, size):
        '''void QListView.setGridSize(QSize size)'''
    def spacing(self):
        '''int QListView.spacing()'''
        return int()
    def setSpacing(self, space):
        '''void QListView.setSpacing(int space)'''
    def layoutMode(self):
        '''QListView.LayoutMode QListView.layoutMode()'''
        return QListView.LayoutMode()
    def setLayoutMode(self, mode):
        '''void QListView.setLayoutMode(QListView.LayoutMode mode)'''
    def resizeMode(self):
        '''QListView.ResizeMode QListView.resizeMode()'''
        return QListView.ResizeMode()
    def setResizeMode(self, mode):
        '''void QListView.setResizeMode(QListView.ResizeMode mode)'''
    def isWrapping(self):
        '''bool QListView.isWrapping()'''
        return bool()
    def setWrapping(self, enable):
        '''void QListView.setWrapping(bool enable)'''
    def flow(self):
        '''QListView.Flow QListView.flow()'''
        return QListView.Flow()
    def setFlow(self, flow):
        '''void QListView.setFlow(QListView.Flow flow)'''
    def movement(self):
        '''QListView.Movement QListView.movement()'''
        return QListView.Movement()
    def setMovement(self, movement):
        '''void QListView.setMovement(QListView.Movement movement)'''


class QListWidgetItem():
    """"""
    # Enum QListWidgetItem.ItemType
    Type = 0
    UserType = 0

    def __init__(self, parent = None, type = None):
        '''void QListWidgetItem.__init__(QListWidget parent = None, int type = QListWidgetItem.Type)'''
    def __init__(self, text, parent = None, type = None):
        '''void QListWidgetItem.__init__(str text, QListWidget parent = None, int type = QListWidgetItem.Type)'''
    def __init__(self, icon, text, parent = None, type = None):
        '''void QListWidgetItem.__init__(QIcon icon, str text, QListWidget parent = None, int type = QListWidgetItem.Type)'''
    def __init__(self, other):
        '''void QListWidgetItem.__init__(QListWidgetItem other)'''
    def __ge__(self, other):
        '''bool QListWidgetItem.__ge__(QListWidgetItem other)'''
        return bool()
    def isHidden(self):
        '''bool QListWidgetItem.isHidden()'''
        return bool()
    def setHidden(self, ahide):
        '''void QListWidgetItem.setHidden(bool ahide)'''
    def isSelected(self):
        '''bool QListWidgetItem.isSelected()'''
        return bool()
    def setSelected(self, aselect):
        '''void QListWidgetItem.setSelected(bool aselect)'''
    def setForeground(self, brush):
        '''void QListWidgetItem.setForeground(QBrush brush)'''
    def foreground(self):
        '''QBrush QListWidgetItem.foreground()'''
        return QBrush()
    def setBackground(self, brush):
        '''void QListWidgetItem.setBackground(QBrush brush)'''
    def background(self):
        '''QBrush QListWidgetItem.background()'''
        return QBrush()
    def setFont(self, afont):
        '''void QListWidgetItem.setFont(QFont afont)'''
    def setWhatsThis(self, awhatsThis):
        '''void QListWidgetItem.setWhatsThis(str awhatsThis)'''
    def setToolTip(self, atoolTip):
        '''void QListWidgetItem.setToolTip(str atoolTip)'''
    def setStatusTip(self, astatusTip):
        '''void QListWidgetItem.setStatusTip(str astatusTip)'''
    def setIcon(self, aicon):
        '''void QListWidgetItem.setIcon(QIcon aicon)'''
    def setText(self, atext):
        '''void QListWidgetItem.setText(str atext)'''
    def setFlags(self, aflags):
        '''void QListWidgetItem.setFlags(Qt.ItemFlags aflags)'''
    def type(self):
        '''int QListWidgetItem.type()'''
        return int()
    def write(self, out):
        '''void QListWidgetItem.write(QDataStream out)'''
    def read(self, in_):
        '''void QListWidgetItem.read(QDataStream in)'''
    def __lt__(self, other):
        '''bool QListWidgetItem.__lt__(QListWidgetItem other)'''
        return bool()
    def setData(self, role, value):
        '''void QListWidgetItem.setData(int role, QVariant value)'''
    def data(self, role):
        '''QVariant QListWidgetItem.data(int role)'''
        return QVariant()
    def setSizeHint(self, size):
        '''void QListWidgetItem.setSizeHint(QSize size)'''
    def sizeHint(self):
        '''QSize QListWidgetItem.sizeHint()'''
        return QSize()
    def setCheckState(self, state):
        '''void QListWidgetItem.setCheckState(Qt.CheckState state)'''
    def checkState(self):
        '''Qt.CheckState QListWidgetItem.checkState()'''
        return Qt.CheckState()
    def setTextAlignment(self, alignment):
        '''void QListWidgetItem.setTextAlignment(int alignment)'''
    def textAlignment(self):
        '''int QListWidgetItem.textAlignment()'''
        return int()
    def font(self):
        '''QFont QListWidgetItem.font()'''
        return QFont()
    def whatsThis(self):
        '''str QListWidgetItem.whatsThis()'''
        return str()
    def toolTip(self):
        '''str QListWidgetItem.toolTip()'''
        return str()
    def statusTip(self):
        '''str QListWidgetItem.statusTip()'''
        return str()
    def icon(self):
        '''QIcon QListWidgetItem.icon()'''
        return QIcon()
    def text(self):
        '''str QListWidgetItem.text()'''
        return str()
    def flags(self):
        '''Qt.ItemFlags QListWidgetItem.flags()'''
        return Qt.ItemFlags()
    def listWidget(self):
        '''QListWidget QListWidgetItem.listWidget()'''
        return QListWidget()
    def clone(self):
        '''QListWidgetItem QListWidgetItem.clone()'''
        return QListWidgetItem()


class QListWidget(QListView):
    """"""
    def __init__(self, parent = None):
        '''void QListWidget.__init__(QWidget parent = None)'''
    def removeItemWidget(self, aItem):
        '''void QListWidget.removeItemWidget(QListWidgetItem aItem)'''
    def dropEvent(self, event):
        '''void QListWidget.dropEvent(QDropEvent event)'''
    def isSortingEnabled(self):
        '''bool QListWidget.isSortingEnabled()'''
        return bool()
    def setSortingEnabled(self, enable):
        '''void QListWidget.setSortingEnabled(bool enable)'''
    def event(self, e):
        '''bool QListWidget.event(QEvent e)'''
        return bool()
    def itemFromIndex(self, index):
        '''QListWidgetItem QListWidget.itemFromIndex(QModelIndex index)'''
        return QListWidgetItem()
    def indexFromItem(self, item):
        '''QModelIndex QListWidget.indexFromItem(QListWidgetItem item)'''
        return QModelIndex()
    def items(self, data):
        '''list-of-QListWidgetItem QListWidget.items(QMimeData data)'''
        return [QListWidgetItem()]
    def supportedDropActions(self):
        '''Qt.DropActions QListWidget.supportedDropActions()'''
        return Qt.DropActions()
    def dropMimeData(self, index, data, action):
        '''bool QListWidget.dropMimeData(int index, QMimeData data, Qt.DropAction action)'''
        return bool()
    def mimeData(self, items):
        '''QMimeData QListWidget.mimeData(list-of-QListWidgetItem items)'''
        return QMimeData()
    def mimeTypes(self):
        '''list-of-str QListWidget.mimeTypes()'''
        return [str()]
    itemSelectionChanged = pyqtSignal() # void itemSelectionChanged() - signal
    currentRowChanged = pyqtSignal() # void currentRowChanged(int) - signal
    currentTextChanged = pyqtSignal() # void currentTextChanged(const QStringamp;) - signal
    currentItemChanged = pyqtSignal() # void currentItemChanged(QListWidgetItem*,QListWidgetItem*) - signal
    itemChanged = pyqtSignal() # void itemChanged(QListWidgetItem*) - signal
    itemEntered = pyqtSignal() # void itemEntered(QListWidgetItem*) - signal
    itemActivated = pyqtSignal() # void itemActivated(QListWidgetItem*) - signal
    itemDoubleClicked = pyqtSignal() # void itemDoubleClicked(QListWidgetItem*) - signal
    itemClicked = pyqtSignal() # void itemClicked(QListWidgetItem*) - signal
    itemPressed = pyqtSignal() # void itemPressed(QListWidgetItem*) - signal
    def scrollToItem(self, item, hint = None):
        '''void QListWidget.scrollToItem(QListWidgetItem item, QAbstractItemView.ScrollHint hint = QAbstractItemView.EnsureVisible)'''
    def clear(self):
        '''void QListWidget.clear()'''
    def findItems(self, text, flags):
        '''list-of-QListWidgetItem QListWidget.findItems(str text, Qt.MatchFlags flags)'''
        return [QListWidgetItem()]
    def selectedItems(self):
        '''list-of-QListWidgetItem QListWidget.selectedItems()'''
        return [QListWidgetItem()]
    def closePersistentEditor(self, item):
        '''void QListWidget.closePersistentEditor(QListWidgetItem item)'''
    def openPersistentEditor(self, item):
        '''void QListWidget.openPersistentEditor(QListWidgetItem item)'''
    def editItem(self, item):
        '''void QListWidget.editItem(QListWidgetItem item)'''
    def sortItems(self, order = None):
        '''void QListWidget.sortItems(Qt.SortOrder order = Qt.AscendingOrder)'''
    def visualItemRect(self, item):
        '''QRect QListWidget.visualItemRect(QListWidgetItem item)'''
        return QRect()
    def setItemWidget(self, item, widget):
        '''void QListWidget.setItemWidget(QListWidgetItem item, QWidget widget)'''
    def itemWidget(self, item):
        '''QWidget QListWidget.itemWidget(QListWidgetItem item)'''
        return QWidget()
    def itemAt(self, p):
        '''QListWidgetItem QListWidget.itemAt(QPoint p)'''
        return QListWidgetItem()
    def itemAt(self, ax, ay):
        '''QListWidgetItem QListWidget.itemAt(int ax, int ay)'''
        return QListWidgetItem()
    def setCurrentRow(self, row):
        '''void QListWidget.setCurrentRow(int row)'''
    def setCurrentRow(self, row, command):
        '''void QListWidget.setCurrentRow(int row, QItemSelectionModel.SelectionFlags command)'''
    def currentRow(self):
        '''int QListWidget.currentRow()'''
        return int()
    def setCurrentItem(self, item):
        '''void QListWidget.setCurrentItem(QListWidgetItem item)'''
    def setCurrentItem(self, item, command):
        '''void QListWidget.setCurrentItem(QListWidgetItem item, QItemSelectionModel.SelectionFlags command)'''
    def currentItem(self):
        '''QListWidgetItem QListWidget.currentItem()'''
        return QListWidgetItem()
    def __len__(self):
        ''' QListWidget.__len__()'''
        return ()
    def count(self):
        '''int QListWidget.count()'''
        return int()
    def takeItem(self, row):
        '''QListWidgetItem QListWidget.takeItem(int row)'''
        return QListWidgetItem()
    def addItems(self, labels):
        '''void QListWidget.addItems(list-of-str labels)'''
    def addItem(self, aitem):
        '''void QListWidget.addItem(QListWidgetItem aitem)'''
    def addItem(self, label):
        '''void QListWidget.addItem(str label)'''
    def insertItems(self, row, labels):
        '''void QListWidget.insertItems(int row, list-of-str labels)'''
    def insertItem(self, row, item):
        '''void QListWidget.insertItem(int row, QListWidgetItem item)'''
    def insertItem(self, row, label):
        '''void QListWidget.insertItem(int row, str label)'''
    def row(self, item):
        '''int QListWidget.row(QListWidgetItem item)'''
        return int()
    def item(self, row):
        '''QListWidgetItem QListWidget.item(int row)'''
        return QListWidgetItem()


class QMainWindow(QWidget):
    """"""
    # Enum QMainWindow.DockOption
    AnimatedDocks = 0
    AllowNestedDocks = 0
    AllowTabbedDocks = 0
    ForceTabbedDocks = 0
    VerticalTabs = 0

    def __init__(self, parent = None, flags = 0):
        '''void QMainWindow.__init__(QWidget parent = None, Qt.WindowFlags flags = 0)'''
    def takeCentralWidget(self):
        '''QWidget QMainWindow.takeCentralWidget()'''
        return QWidget()
    def tabifiedDockWidgets(self, dockwidget):
        '''list-of-QDockWidget QMainWindow.tabifiedDockWidgets(QDockWidget dockwidget)'''
        return [QDockWidget()]
    def setTabPosition(self, areas, tabPosition):
        '''void QMainWindow.setTabPosition(Qt.DockWidgetAreas areas, QTabWidget.TabPosition tabPosition)'''
    def tabPosition(self, area):
        '''QTabWidget.TabPosition QMainWindow.tabPosition(Qt.DockWidgetArea area)'''
        return QTabWidget.TabPosition()
    def setTabShape(self, tabShape):
        '''void QMainWindow.setTabShape(QTabWidget.TabShape tabShape)'''
    def tabShape(self):
        '''QTabWidget.TabShape QMainWindow.tabShape()'''
        return QTabWidget.TabShape()
    def setDocumentMode(self, enabled):
        '''void QMainWindow.setDocumentMode(bool enabled)'''
    def documentMode(self):
        '''bool QMainWindow.documentMode()'''
        return bool()
    def restoreDockWidget(self, dockwidget):
        '''bool QMainWindow.restoreDockWidget(QDockWidget dockwidget)'''
        return bool()
    def unifiedTitleAndToolBarOnMac(self):
        '''bool QMainWindow.unifiedTitleAndToolBarOnMac()'''
        return bool()
    def setUnifiedTitleAndToolBarOnMac(self, set):
        '''void QMainWindow.setUnifiedTitleAndToolBarOnMac(bool set)'''
    def toolBarBreak(self, toolbar):
        '''bool QMainWindow.toolBarBreak(QToolBar toolbar)'''
        return bool()
    def removeToolBarBreak(self, before):
        '''void QMainWindow.removeToolBarBreak(QToolBar before)'''
    def dockOptions(self):
        '''QMainWindow.DockOptions QMainWindow.dockOptions()'''
        return QMainWindow.DockOptions()
    def setDockOptions(self, options):
        '''void QMainWindow.setDockOptions(QMainWindow.DockOptions options)'''
    def tabifyDockWidget(self, first, second):
        '''void QMainWindow.tabifyDockWidget(QDockWidget first, QDockWidget second)'''
    def setMenuWidget(self, menubar):
        '''void QMainWindow.setMenuWidget(QWidget menubar)'''
    def menuWidget(self):
        '''QWidget QMainWindow.menuWidget()'''
        return QWidget()
    def isSeparator(self, pos):
        '''bool QMainWindow.isSeparator(QPoint pos)'''
        return bool()
    def isDockNestingEnabled(self):
        '''bool QMainWindow.isDockNestingEnabled()'''
        return bool()
    def isAnimated(self):
        '''bool QMainWindow.isAnimated()'''
        return bool()
    def event(self, event):
        '''bool QMainWindow.event(QEvent event)'''
        return bool()
    def contextMenuEvent(self, event):
        '''void QMainWindow.contextMenuEvent(QContextMenuEvent event)'''
    toolButtonStyleChanged = pyqtSignal() # void toolButtonStyleChanged(Qt::ToolButtonStyle) - signal
    iconSizeChanged = pyqtSignal() # void iconSizeChanged(const QSizeamp;) - signal
    def setDockNestingEnabled(self, enabled):
        '''void QMainWindow.setDockNestingEnabled(bool enabled)'''
    def setAnimated(self, enabled):
        '''void QMainWindow.setAnimated(bool enabled)'''
    def createPopupMenu(self):
        '''QMenu QMainWindow.createPopupMenu()'''
        return QMenu()
    def restoreState(self, state, version = 0):
        '''bool QMainWindow.restoreState(QByteArray state, int version = 0)'''
        return bool()
    def saveState(self, version = 0):
        '''QByteArray QMainWindow.saveState(int version = 0)'''
        return QByteArray()
    def dockWidgetArea(self, dockwidget):
        '''Qt.DockWidgetArea QMainWindow.dockWidgetArea(QDockWidget dockwidget)'''
        return Qt.DockWidgetArea()
    def removeDockWidget(self, dockwidget):
        '''void QMainWindow.removeDockWidget(QDockWidget dockwidget)'''
    def splitDockWidget(self, after, dockwidget, orientation):
        '''void QMainWindow.splitDockWidget(QDockWidget after, QDockWidget dockwidget, Qt.Orientation orientation)'''
    def addDockWidget(self, area, dockwidget):
        '''void QMainWindow.addDockWidget(Qt.DockWidgetArea area, QDockWidget dockwidget)'''
    def addDockWidget(self, area, dockwidget, orientation):
        '''void QMainWindow.addDockWidget(Qt.DockWidgetArea area, QDockWidget dockwidget, Qt.Orientation orientation)'''
    def toolBarArea(self, toolbar):
        '''Qt.ToolBarArea QMainWindow.toolBarArea(QToolBar toolbar)'''
        return Qt.ToolBarArea()
    def removeToolBar(self, toolbar):
        '''void QMainWindow.removeToolBar(QToolBar toolbar)'''
    def insertToolBar(self, before, toolbar):
        '''void QMainWindow.insertToolBar(QToolBar before, QToolBar toolbar)'''
    def addToolBar(self, area, toolbar):
        '''void QMainWindow.addToolBar(Qt.ToolBarArea area, QToolBar toolbar)'''
    def addToolBar(self, toolbar):
        '''void QMainWindow.addToolBar(QToolBar toolbar)'''
    def addToolBar(self, title):
        '''QToolBar QMainWindow.addToolBar(str title)'''
        return QToolBar()
    def insertToolBarBreak(self, before):
        '''void QMainWindow.insertToolBarBreak(QToolBar before)'''
    def addToolBarBreak(self, area = None):
        '''void QMainWindow.addToolBarBreak(Qt.ToolBarArea area = Qt.TopToolBarArea)'''
    def corner(self, corner):
        '''Qt.DockWidgetArea QMainWindow.corner(Qt.Corner corner)'''
        return Qt.DockWidgetArea()
    def setCorner(self, corner, area):
        '''void QMainWindow.setCorner(Qt.Corner corner, Qt.DockWidgetArea area)'''
    def setCentralWidget(self, widget):
        '''void QMainWindow.setCentralWidget(QWidget widget)'''
    def centralWidget(self):
        '''QWidget QMainWindow.centralWidget()'''
        return QWidget()
    def setStatusBar(self, statusbar):
        '''void QMainWindow.setStatusBar(QStatusBar statusbar)'''
    def statusBar(self):
        '''QStatusBar QMainWindow.statusBar()'''
        return QStatusBar()
    def setMenuBar(self, menubar):
        '''void QMainWindow.setMenuBar(QMenuBar menubar)'''
    def menuBar(self):
        '''QMenuBar QMainWindow.menuBar()'''
        return QMenuBar()
    def setToolButtonStyle(self, toolButtonStyle):
        '''void QMainWindow.setToolButtonStyle(Qt.ToolButtonStyle toolButtonStyle)'''
    def toolButtonStyle(self):
        '''Qt.ToolButtonStyle QMainWindow.toolButtonStyle()'''
        return Qt.ToolButtonStyle()
    def setIconSize(self, iconSize):
        '''void QMainWindow.setIconSize(QSize iconSize)'''
    def iconSize(self):
        '''QSize QMainWindow.iconSize()'''
        return QSize()
    class DockOptions():
        """"""
        def __init__(self):
            '''QMainWindow.DockOptions QMainWindow.DockOptions.__init__()'''
            return QMainWindow.DockOptions()
        def __init__(self):
            '''int QMainWindow.DockOptions.__init__()'''
            return int()
        def __init__(self):
            '''void QMainWindow.DockOptions.__init__()'''
        def __bool__(self):
            '''int QMainWindow.DockOptions.__bool__()'''
            return int()
        def __ne__(self, f):
            '''bool QMainWindow.DockOptions.__ne__(QMainWindow.DockOptions f)'''
            return bool()
        def __eq__(self, f):
            '''bool QMainWindow.DockOptions.__eq__(QMainWindow.DockOptions f)'''
            return bool()
        def __invert__(self):
            '''QMainWindow.DockOptions QMainWindow.DockOptions.__invert__()'''
            return QMainWindow.DockOptions()
        def __and__(self, mask):
            '''QMainWindow.DockOptions QMainWindow.DockOptions.__and__(int mask)'''
            return QMainWindow.DockOptions()
        def __xor__(self, f):
            '''QMainWindow.DockOptions QMainWindow.DockOptions.__xor__(QMainWindow.DockOptions f)'''
            return QMainWindow.DockOptions()
        def __xor__(self, f):
            '''QMainWindow.DockOptions QMainWindow.DockOptions.__xor__(int f)'''
            return QMainWindow.DockOptions()
        def __or__(self, f):
            '''QMainWindow.DockOptions QMainWindow.DockOptions.__or__(QMainWindow.DockOptions f)'''
            return QMainWindow.DockOptions()
        def __or__(self, f):
            '''QMainWindow.DockOptions QMainWindow.DockOptions.__or__(int f)'''
            return QMainWindow.DockOptions()
        def __int__(self):
            '''int QMainWindow.DockOptions.__int__()'''
            return int()
        def __ixor__(self, f):
            '''QMainWindow.DockOptions QMainWindow.DockOptions.__ixor__(QMainWindow.DockOptions f)'''
            return QMainWindow.DockOptions()
        def __ior__(self, f):
            '''QMainWindow.DockOptions QMainWindow.DockOptions.__ior__(QMainWindow.DockOptions f)'''
            return QMainWindow.DockOptions()
        def __iand__(self, mask):
            '''QMainWindow.DockOptions QMainWindow.DockOptions.__iand__(int mask)'''
            return QMainWindow.DockOptions()


class QMdiArea(QAbstractScrollArea):
    """"""
    # Enum QMdiArea.WindowOrder
    CreationOrder = 0
    StackingOrder = 0
    ActivationHistoryOrder = 0

    # Enum QMdiArea.ViewMode
    SubWindowView = 0
    TabbedView = 0

    # Enum QMdiArea.AreaOption
    DontMaximizeSubWindowOnActivation = 0

    def __init__(self, parent = None):
        '''void QMdiArea.__init__(QWidget parent = None)'''
    def tabsMovable(self):
        '''bool QMdiArea.tabsMovable()'''
        return bool()
    def setTabsMovable(self, movable):
        '''void QMdiArea.setTabsMovable(bool movable)'''
    def tabsClosable(self):
        '''bool QMdiArea.tabsClosable()'''
        return bool()
    def setTabsClosable(self, closable):
        '''void QMdiArea.setTabsClosable(bool closable)'''
    def setDocumentMode(self, enabled):
        '''void QMdiArea.setDocumentMode(bool enabled)'''
    def documentMode(self):
        '''bool QMdiArea.documentMode()'''
        return bool()
    def tabPosition(self):
        '''QTabWidget.TabPosition QMdiArea.tabPosition()'''
        return QTabWidget.TabPosition()
    def setTabPosition(self, position):
        '''void QMdiArea.setTabPosition(QTabWidget.TabPosition position)'''
    def tabShape(self):
        '''QTabWidget.TabShape QMdiArea.tabShape()'''
        return QTabWidget.TabShape()
    def setTabShape(self, shape):
        '''void QMdiArea.setTabShape(QTabWidget.TabShape shape)'''
    def viewMode(self):
        '''QMdiArea.ViewMode QMdiArea.viewMode()'''
        return QMdiArea.ViewMode()
    def setViewMode(self, mode):
        '''void QMdiArea.setViewMode(QMdiArea.ViewMode mode)'''
    def setActivationOrder(self, order):
        '''void QMdiArea.setActivationOrder(QMdiArea.WindowOrder order)'''
    def activationOrder(self):
        '''QMdiArea.WindowOrder QMdiArea.activationOrder()'''
        return QMdiArea.WindowOrder()
    def scrollContentsBy(self, dx, dy):
        '''void QMdiArea.scrollContentsBy(int dx, int dy)'''
    def viewportEvent(self, event):
        '''bool QMdiArea.viewportEvent(QEvent event)'''
        return bool()
    def showEvent(self, showEvent):
        '''void QMdiArea.showEvent(QShowEvent showEvent)'''
    def timerEvent(self, timerEvent):
        '''void QMdiArea.timerEvent(QTimerEvent timerEvent)'''
    def resizeEvent(self, resizeEvent):
        '''void QMdiArea.resizeEvent(QResizeEvent resizeEvent)'''
    def childEvent(self, childEvent):
        '''void QMdiArea.childEvent(QChildEvent childEvent)'''
    def paintEvent(self, paintEvent):
        '''void QMdiArea.paintEvent(QPaintEvent paintEvent)'''
    def eventFilter(self, object, event):
        '''bool QMdiArea.eventFilter(QObject object, QEvent event)'''
        return bool()
    def event(self, event):
        '''bool QMdiArea.event(QEvent event)'''
        return bool()
    def setupViewport(self, viewport):
        '''void QMdiArea.setupViewport(QWidget viewport)'''
    def activatePreviousSubWindow(self):
        '''void QMdiArea.activatePreviousSubWindow()'''
    def activateNextSubWindow(self):
        '''void QMdiArea.activateNextSubWindow()'''
    def closeAllSubWindows(self):
        '''void QMdiArea.closeAllSubWindows()'''
    def closeActiveSubWindow(self):
        '''void QMdiArea.closeActiveSubWindow()'''
    def cascadeSubWindows(self):
        '''void QMdiArea.cascadeSubWindows()'''
    def tileSubWindows(self):
        '''void QMdiArea.tileSubWindows()'''
    def setActiveSubWindow(self, window):
        '''void QMdiArea.setActiveSubWindow(QMdiSubWindow window)'''
    subWindowActivated = pyqtSignal() # void subWindowActivated(QMdiSubWindow*) - signal
    def testOption(self, opton):
        '''bool QMdiArea.testOption(QMdiArea.AreaOption opton)'''
        return bool()
    def setOption(self, option, on = True):
        '''void QMdiArea.setOption(QMdiArea.AreaOption option, bool on = True)'''
    def setBackground(self, background):
        '''void QMdiArea.setBackground(QBrush background)'''
    def background(self):
        '''QBrush QMdiArea.background()'''
        return QBrush()
    def removeSubWindow(self, widget):
        '''void QMdiArea.removeSubWindow(QWidget widget)'''
    def currentSubWindow(self):
        '''QMdiSubWindow QMdiArea.currentSubWindow()'''
        return QMdiSubWindow()
    def subWindowList(self, order = None):
        '''list-of-QMdiSubWindow QMdiArea.subWindowList(QMdiArea.WindowOrder order = QMdiArea.CreationOrder)'''
        return [QMdiSubWindow()]
    def addSubWindow(self, widget, flags = 0):
        '''QMdiSubWindow QMdiArea.addSubWindow(QWidget widget, Qt.WindowFlags flags = 0)'''
        return QMdiSubWindow()
    def activeSubWindow(self):
        '''QMdiSubWindow QMdiArea.activeSubWindow()'''
        return QMdiSubWindow()
    def minimumSizeHint(self):
        '''QSize QMdiArea.minimumSizeHint()'''
        return QSize()
    def sizeHint(self):
        '''QSize QMdiArea.sizeHint()'''
        return QSize()
    class AreaOptions():
        """"""
        def __init__(self):
            '''QMdiArea.AreaOptions QMdiArea.AreaOptions.__init__()'''
            return QMdiArea.AreaOptions()
        def __init__(self):
            '''int QMdiArea.AreaOptions.__init__()'''
            return int()
        def __init__(self):
            '''void QMdiArea.AreaOptions.__init__()'''
        def __bool__(self):
            '''int QMdiArea.AreaOptions.__bool__()'''
            return int()
        def __ne__(self, f):
            '''bool QMdiArea.AreaOptions.__ne__(QMdiArea.AreaOptions f)'''
            return bool()
        def __eq__(self, f):
            '''bool QMdiArea.AreaOptions.__eq__(QMdiArea.AreaOptions f)'''
            return bool()
        def __invert__(self):
            '''QMdiArea.AreaOptions QMdiArea.AreaOptions.__invert__()'''
            return QMdiArea.AreaOptions()
        def __and__(self, mask):
            '''QMdiArea.AreaOptions QMdiArea.AreaOptions.__and__(int mask)'''
            return QMdiArea.AreaOptions()
        def __xor__(self, f):
            '''QMdiArea.AreaOptions QMdiArea.AreaOptions.__xor__(QMdiArea.AreaOptions f)'''
            return QMdiArea.AreaOptions()
        def __xor__(self, f):
            '''QMdiArea.AreaOptions QMdiArea.AreaOptions.__xor__(int f)'''
            return QMdiArea.AreaOptions()
        def __or__(self, f):
            '''QMdiArea.AreaOptions QMdiArea.AreaOptions.__or__(QMdiArea.AreaOptions f)'''
            return QMdiArea.AreaOptions()
        def __or__(self, f):
            '''QMdiArea.AreaOptions QMdiArea.AreaOptions.__or__(int f)'''
            return QMdiArea.AreaOptions()
        def __int__(self):
            '''int QMdiArea.AreaOptions.__int__()'''
            return int()
        def __ixor__(self, f):
            '''QMdiArea.AreaOptions QMdiArea.AreaOptions.__ixor__(QMdiArea.AreaOptions f)'''
            return QMdiArea.AreaOptions()
        def __ior__(self, f):
            '''QMdiArea.AreaOptions QMdiArea.AreaOptions.__ior__(QMdiArea.AreaOptions f)'''
            return QMdiArea.AreaOptions()
        def __iand__(self, mask):
            '''QMdiArea.AreaOptions QMdiArea.AreaOptions.__iand__(int mask)'''
            return QMdiArea.AreaOptions()


class QMdiSubWindow(QWidget):
    """"""
    # Enum QMdiSubWindow.SubWindowOption
    RubberBandResize = 0
    RubberBandMove = 0

    def __init__(self, parent = None, flags = 0):
        '''void QMdiSubWindow.__init__(QWidget parent = None, Qt.WindowFlags flags = 0)'''
    def childEvent(self, childEvent):
        '''void QMdiSubWindow.childEvent(QChildEvent childEvent)'''
    def focusOutEvent(self, focusOutEvent):
        '''void QMdiSubWindow.focusOutEvent(QFocusEvent focusOutEvent)'''
    def focusInEvent(self, focusInEvent):
        '''void QMdiSubWindow.focusInEvent(QFocusEvent focusInEvent)'''
    def contextMenuEvent(self, contextMenuEvent):
        '''void QMdiSubWindow.contextMenuEvent(QContextMenuEvent contextMenuEvent)'''
    def keyPressEvent(self, keyEvent):
        '''void QMdiSubWindow.keyPressEvent(QKeyEvent keyEvent)'''
    def mouseMoveEvent(self, mouseEvent):
        '''void QMdiSubWindow.mouseMoveEvent(QMouseEvent mouseEvent)'''
    def mouseReleaseEvent(self, mouseEvent):
        '''void QMdiSubWindow.mouseReleaseEvent(QMouseEvent mouseEvent)'''
    def mouseDoubleClickEvent(self, mouseEvent):
        '''void QMdiSubWindow.mouseDoubleClickEvent(QMouseEvent mouseEvent)'''
    def mousePressEvent(self, mouseEvent):
        '''void QMdiSubWindow.mousePressEvent(QMouseEvent mouseEvent)'''
    def paintEvent(self, paintEvent):
        '''void QMdiSubWindow.paintEvent(QPaintEvent paintEvent)'''
    def moveEvent(self, moveEvent):
        '''void QMdiSubWindow.moveEvent(QMoveEvent moveEvent)'''
    def timerEvent(self, timerEvent):
        '''void QMdiSubWindow.timerEvent(QTimerEvent timerEvent)'''
    def resizeEvent(self, resizeEvent):
        '''void QMdiSubWindow.resizeEvent(QResizeEvent resizeEvent)'''
    def leaveEvent(self, leaveEvent):
        '''void QMdiSubWindow.leaveEvent(QEvent leaveEvent)'''
    def closeEvent(self, closeEvent):
        '''void QMdiSubWindow.closeEvent(QCloseEvent closeEvent)'''
    def changeEvent(self, changeEvent):
        '''void QMdiSubWindow.changeEvent(QEvent changeEvent)'''
    def hideEvent(self, hideEvent):
        '''void QMdiSubWindow.hideEvent(QHideEvent hideEvent)'''
    def showEvent(self, showEvent):
        '''void QMdiSubWindow.showEvent(QShowEvent showEvent)'''
    def event(self, event):
        '''bool QMdiSubWindow.event(QEvent event)'''
        return bool()
    def eventFilter(self, object, event):
        '''bool QMdiSubWindow.eventFilter(QObject object, QEvent event)'''
        return bool()
    def showShaded(self):
        '''void QMdiSubWindow.showShaded()'''
    def showSystemMenu(self):
        '''void QMdiSubWindow.showSystemMenu()'''
    aboutToActivate = pyqtSignal() # void aboutToActivate() - signal
    windowStateChanged = pyqtSignal() # void windowStateChanged(Qt::WindowStates,Qt::WindowStates) - signal
    def mdiArea(self):
        '''QMdiArea QMdiSubWindow.mdiArea()'''
        return QMdiArea()
    def systemMenu(self):
        '''QMenu QMdiSubWindow.systemMenu()'''
        return QMenu()
    def setSystemMenu(self, systemMenu):
        '''void QMdiSubWindow.setSystemMenu(QMenu systemMenu)'''
    def keyboardPageStep(self):
        '''int QMdiSubWindow.keyboardPageStep()'''
        return int()
    def setKeyboardPageStep(self, step):
        '''void QMdiSubWindow.setKeyboardPageStep(int step)'''
    def keyboardSingleStep(self):
        '''int QMdiSubWindow.keyboardSingleStep()'''
        return int()
    def setKeyboardSingleStep(self, step):
        '''void QMdiSubWindow.setKeyboardSingleStep(int step)'''
    def testOption(self):
        '''QMdiSubWindow.SubWindowOption QMdiSubWindow.testOption()'''
        return QMdiSubWindow.SubWindowOption()
    def setOption(self, option, on = True):
        '''void QMdiSubWindow.setOption(QMdiSubWindow.SubWindowOption option, bool on = True)'''
    def isShaded(self):
        '''bool QMdiSubWindow.isShaded()'''
        return bool()
    def widget(self):
        '''QWidget QMdiSubWindow.widget()'''
        return QWidget()
    def setWidget(self, widget):
        '''void QMdiSubWindow.setWidget(QWidget widget)'''
    def minimumSizeHint(self):
        '''QSize QMdiSubWindow.minimumSizeHint()'''
        return QSize()
    def sizeHint(self):
        '''QSize QMdiSubWindow.sizeHint()'''
        return QSize()
    class SubWindowOptions():
        """"""
        def __init__(self):
            '''QMdiSubWindow.SubWindowOptions QMdiSubWindow.SubWindowOptions.__init__()'''
            return QMdiSubWindow.SubWindowOptions()
        def __init__(self):
            '''int QMdiSubWindow.SubWindowOptions.__init__()'''
            return int()
        def __init__(self):
            '''void QMdiSubWindow.SubWindowOptions.__init__()'''
        def __bool__(self):
            '''int QMdiSubWindow.SubWindowOptions.__bool__()'''
            return int()
        def __ne__(self, f):
            '''bool QMdiSubWindow.SubWindowOptions.__ne__(QMdiSubWindow.SubWindowOptions f)'''
            return bool()
        def __eq__(self, f):
            '''bool QMdiSubWindow.SubWindowOptions.__eq__(QMdiSubWindow.SubWindowOptions f)'''
            return bool()
        def __invert__(self):
            '''QMdiSubWindow.SubWindowOptions QMdiSubWindow.SubWindowOptions.__invert__()'''
            return QMdiSubWindow.SubWindowOptions()
        def __and__(self, mask):
            '''QMdiSubWindow.SubWindowOptions QMdiSubWindow.SubWindowOptions.__and__(int mask)'''
            return QMdiSubWindow.SubWindowOptions()
        def __xor__(self, f):
            '''QMdiSubWindow.SubWindowOptions QMdiSubWindow.SubWindowOptions.__xor__(QMdiSubWindow.SubWindowOptions f)'''
            return QMdiSubWindow.SubWindowOptions()
        def __xor__(self, f):
            '''QMdiSubWindow.SubWindowOptions QMdiSubWindow.SubWindowOptions.__xor__(int f)'''
            return QMdiSubWindow.SubWindowOptions()
        def __or__(self, f):
            '''QMdiSubWindow.SubWindowOptions QMdiSubWindow.SubWindowOptions.__or__(QMdiSubWindow.SubWindowOptions f)'''
            return QMdiSubWindow.SubWindowOptions()
        def __or__(self, f):
            '''QMdiSubWindow.SubWindowOptions QMdiSubWindow.SubWindowOptions.__or__(int f)'''
            return QMdiSubWindow.SubWindowOptions()
        def __int__(self):
            '''int QMdiSubWindow.SubWindowOptions.__int__()'''
            return int()
        def __ixor__(self, f):
            '''QMdiSubWindow.SubWindowOptions QMdiSubWindow.SubWindowOptions.__ixor__(QMdiSubWindow.SubWindowOptions f)'''
            return QMdiSubWindow.SubWindowOptions()
        def __ior__(self, f):
            '''QMdiSubWindow.SubWindowOptions QMdiSubWindow.SubWindowOptions.__ior__(QMdiSubWindow.SubWindowOptions f)'''
            return QMdiSubWindow.SubWindowOptions()
        def __iand__(self, mask):
            '''QMdiSubWindow.SubWindowOptions QMdiSubWindow.SubWindowOptions.__iand__(int mask)'''
            return QMdiSubWindow.SubWindowOptions()


class QMenu(QWidget):
    """"""
    def __init__(self, parent = None):
        '''void QMenu.__init__(QWidget parent = None)'''
    def __init__(self, title, parent = None):
        '''void QMenu.__init__(str title, QWidget parent = None)'''
    def setToolTipsVisible(self, visible):
        '''void QMenu.setToolTipsVisible(bool visible)'''
    def toolTipsVisible(self):
        '''bool QMenu.toolTipsVisible()'''
        return bool()
    def insertSection(self, before, text):
        '''QAction QMenu.insertSection(QAction before, str text)'''
        return QAction()
    def insertSection(self, before, icon, text):
        '''QAction QMenu.insertSection(QAction before, QIcon icon, str text)'''
        return QAction()
    def addSection(self, text):
        '''QAction QMenu.addSection(str text)'''
        return QAction()
    def addSection(self, icon, text):
        '''QAction QMenu.addSection(QIcon icon, str text)'''
        return QAction()
    def setSeparatorsCollapsible(self, collapse):
        '''void QMenu.setSeparatorsCollapsible(bool collapse)'''
    def separatorsCollapsible(self):
        '''bool QMenu.separatorsCollapsible()'''
        return bool()
    def isEmpty(self):
        '''bool QMenu.isEmpty()'''
        return bool()
    def focusNextPrevChild(self, next):
        '''bool QMenu.focusNextPrevChild(bool next)'''
        return bool()
    def event(self):
        '''QEvent QMenu.event()'''
        return QEvent()
    def timerEvent(self):
        '''QTimerEvent QMenu.timerEvent()'''
        return QTimerEvent()
    def actionEvent(self):
        '''QActionEvent QMenu.actionEvent()'''
        return QActionEvent()
    def paintEvent(self):
        '''QPaintEvent QMenu.paintEvent()'''
        return QPaintEvent()
    def hideEvent(self):
        '''QHideEvent QMenu.hideEvent()'''
        return QHideEvent()
    def leaveEvent(self):
        '''QEvent QMenu.leaveEvent()'''
        return QEvent()
    def enterEvent(self):
        '''QEvent QMenu.enterEvent()'''
        return QEvent()
    def wheelEvent(self):
        '''QWheelEvent QMenu.wheelEvent()'''
        return QWheelEvent()
    def mouseMoveEvent(self):
        '''QMouseEvent QMenu.mouseMoveEvent()'''
        return QMouseEvent()
    def mousePressEvent(self):
        '''QMouseEvent QMenu.mousePressEvent()'''
        return QMouseEvent()
    def mouseReleaseEvent(self):
        '''QMouseEvent QMenu.mouseReleaseEvent()'''
        return QMouseEvent()
    def keyPressEvent(self):
        '''QKeyEvent QMenu.keyPressEvent()'''
        return QKeyEvent()
    def changeEvent(self):
        '''QEvent QMenu.changeEvent()'''
        return QEvent()
    def initStyleOption(self, option, action):
        '''void QMenu.initStyleOption(QStyleOptionMenuItem option, QAction action)'''
    def columnCount(self):
        '''int QMenu.columnCount()'''
        return int()
    triggered = pyqtSignal() # void triggered(QAction*) - signal
    hovered = pyqtSignal() # void hovered(QAction*) - signal
    aboutToShow = pyqtSignal() # void aboutToShow() - signal
    aboutToHide = pyqtSignal() # void aboutToHide() - signal
    def setNoReplayFor(self, widget):
        '''void QMenu.setNoReplayFor(QWidget widget)'''
    def setIcon(self, icon):
        '''void QMenu.setIcon(QIcon icon)'''
    def icon(self):
        '''QIcon QMenu.icon()'''
        return QIcon()
    def setTitle(self, title):
        '''void QMenu.setTitle(str title)'''
    def title(self):
        '''str QMenu.title()'''
        return str()
    def menuAction(self):
        '''QAction QMenu.menuAction()'''
        return QAction()
    def actionAt(self):
        '''QPoint QMenu.actionAt()'''
        return QPoint()
    def actionGeometry(self):
        '''QAction QMenu.actionGeometry()'''
        return QAction()
    def sizeHint(self):
        '''QSize QMenu.sizeHint()'''
        return QSize()
    def exec_(self):
        '''QAction QMenu.exec_()'''
        return QAction()
    def exec_(self, p, action = None):
        '''QAction QMenu.exec_(QPoint p, QAction action = None)'''
        return QAction()
    def exec_(self, actions, pos, at = None, parent = None):
        '''static QAction QMenu.exec_(list-of-QAction actions, QPoint pos, QAction at = None, QWidget parent = None)'''
        return QAction()
    def popup(self, p, action = None):
        '''void QMenu.popup(QPoint p, QAction action = None)'''
    def activeAction(self):
        '''QAction QMenu.activeAction()'''
        return QAction()
    def setActiveAction(self, act):
        '''void QMenu.setActiveAction(QAction act)'''
    def defaultAction(self):
        '''QAction QMenu.defaultAction()'''
        return QAction()
    def setDefaultAction(self):
        '''QAction QMenu.setDefaultAction()'''
        return QAction()
    def hideTearOffMenu(self):
        '''void QMenu.hideTearOffMenu()'''
    def isTearOffMenuVisible(self):
        '''bool QMenu.isTearOffMenuVisible()'''
        return bool()
    def isTearOffEnabled(self):
        '''bool QMenu.isTearOffEnabled()'''
        return bool()
    def setTearOffEnabled(self):
        '''bool QMenu.setTearOffEnabled()'''
        return bool()
    def clear(self):
        '''void QMenu.clear()'''
    def insertSeparator(self, before):
        '''QAction QMenu.insertSeparator(QAction before)'''
        return QAction()
    def insertMenu(self, before, menu):
        '''QAction QMenu.insertMenu(QAction before, QMenu menu)'''
        return QAction()
    def addSeparator(self):
        '''QAction QMenu.addSeparator()'''
        return QAction()
    def addMenu(self, menu):
        '''QAction QMenu.addMenu(QMenu menu)'''
        return QAction()
    def addMenu(self, title):
        '''QMenu QMenu.addMenu(str title)'''
        return QMenu()
    def addMenu(self, icon, title):
        '''QMenu QMenu.addMenu(QIcon icon, str title)'''
        return QMenu()
    def addAction(self, action):
        '''void QMenu.addAction(QAction action)'''
    def addAction(self, text):
        '''QAction QMenu.addAction(str text)'''
        return QAction()
    def addAction(self, icon, text):
        '''QAction QMenu.addAction(QIcon icon, str text)'''
        return QAction()
    def addAction(self, text, slot, shortcut = 0):
        '''QAction QMenu.addAction(str text, slot slot, QKeySequence shortcut = 0)'''
        return QAction()
    def addAction(self, icon, text, slot, shortcut = 0):
        '''QAction QMenu.addAction(QIcon icon, str text, slot slot, QKeySequence shortcut = 0)'''
        return QAction()


class QMenuBar(QWidget):
    """"""
    def __init__(self, parent = None):
        '''void QMenuBar.__init__(QWidget parent = None)'''
    def setNativeMenuBar(self, nativeMenuBar):
        '''void QMenuBar.setNativeMenuBar(bool nativeMenuBar)'''
    def isNativeMenuBar(self):
        '''bool QMenuBar.isNativeMenuBar()'''
        return bool()
    def timerEvent(self):
        '''QTimerEvent QMenuBar.timerEvent()'''
        return QTimerEvent()
    def event(self):
        '''QEvent QMenuBar.event()'''
        return QEvent()
    def eventFilter(self):
        '''QEvent QMenuBar.eventFilter()'''
        return QEvent()
    def focusInEvent(self):
        '''QFocusEvent QMenuBar.focusInEvent()'''
        return QFocusEvent()
    def focusOutEvent(self):
        '''QFocusEvent QMenuBar.focusOutEvent()'''
        return QFocusEvent()
    def actionEvent(self):
        '''QActionEvent QMenuBar.actionEvent()'''
        return QActionEvent()
    def resizeEvent(self):
        '''QResizeEvent QMenuBar.resizeEvent()'''
        return QResizeEvent()
    def paintEvent(self):
        '''QPaintEvent QMenuBar.paintEvent()'''
        return QPaintEvent()
    def leaveEvent(self):
        '''QEvent QMenuBar.leaveEvent()'''
        return QEvent()
    def mouseMoveEvent(self):
        '''QMouseEvent QMenuBar.mouseMoveEvent()'''
        return QMouseEvent()
    def mousePressEvent(self):
        '''QMouseEvent QMenuBar.mousePressEvent()'''
        return QMouseEvent()
    def mouseReleaseEvent(self):
        '''QMouseEvent QMenuBar.mouseReleaseEvent()'''
        return QMouseEvent()
    def keyPressEvent(self):
        '''QKeyEvent QMenuBar.keyPressEvent()'''
        return QKeyEvent()
    def changeEvent(self):
        '''QEvent QMenuBar.changeEvent()'''
        return QEvent()
    def initStyleOption(self, option, action):
        '''void QMenuBar.initStyleOption(QStyleOptionMenuItem option, QAction action)'''
    hovered = pyqtSignal() # void hovered(QAction*) - signal
    triggered = pyqtSignal() # void triggered(QAction*) - signal
    def setVisible(self, visible):
        '''void QMenuBar.setVisible(bool visible)'''
    def cornerWidget(self, corner = None):
        '''QWidget QMenuBar.cornerWidget(Qt.Corner corner = Qt.TopRightCorner)'''
        return QWidget()
    def setCornerWidget(self, widget, corner = None):
        '''void QMenuBar.setCornerWidget(QWidget widget, Qt.Corner corner = Qt.TopRightCorner)'''
    def actionAt(self):
        '''QPoint QMenuBar.actionAt()'''
        return QPoint()
    def actionGeometry(self):
        '''QAction QMenuBar.actionGeometry()'''
        return QAction()
    def heightForWidth(self):
        '''int QMenuBar.heightForWidth()'''
        return int()
    def minimumSizeHint(self):
        '''QSize QMenuBar.minimumSizeHint()'''
        return QSize()
    def sizeHint(self):
        '''QSize QMenuBar.sizeHint()'''
        return QSize()
    def isDefaultUp(self):
        '''bool QMenuBar.isDefaultUp()'''
        return bool()
    def setDefaultUp(self):
        '''bool QMenuBar.setDefaultUp()'''
        return bool()
    def setActiveAction(self, action):
        '''void QMenuBar.setActiveAction(QAction action)'''
    def activeAction(self):
        '''QAction QMenuBar.activeAction()'''
        return QAction()
    def clear(self):
        '''void QMenuBar.clear()'''
    def insertSeparator(self, before):
        '''QAction QMenuBar.insertSeparator(QAction before)'''
        return QAction()
    def insertMenu(self, before, menu):
        '''QAction QMenuBar.insertMenu(QAction before, QMenu menu)'''
        return QAction()
    def addSeparator(self):
        '''QAction QMenuBar.addSeparator()'''
        return QAction()
    def addMenu(self, menu):
        '''QAction QMenuBar.addMenu(QMenu menu)'''
        return QAction()
    def addMenu(self, title):
        '''QMenu QMenuBar.addMenu(str title)'''
        return QMenu()
    def addMenu(self, icon, title):
        '''QMenu QMenuBar.addMenu(QIcon icon, str title)'''
        return QMenu()
    def addAction(self, action):
        '''void QMenuBar.addAction(QAction action)'''
    def addAction(self, text):
        '''QAction QMenuBar.addAction(str text)'''
        return QAction()
    def addAction(self, text, slot):
        '''QAction QMenuBar.addAction(str text, slot slot)'''
        return QAction()


class QMessageBox(QDialog):
    """"""
    # Enum QMessageBox.StandardButton
    NoButton = 0
    Ok = 0
    Save = 0
    SaveAll = 0
    Open = 0
    Yes = 0
    YesToAll = 0
    No = 0
    NoToAll = 0
    Abort = 0
    Retry = 0
    Ignore = 0
    Close = 0
    Cancel = 0
    Discard = 0
    Help = 0
    Apply = 0
    Reset = 0
    RestoreDefaults = 0
    FirstButton = 0
    LastButton = 0
    YesAll = 0
    NoAll = 0
    Default = 0
    Escape = 0
    FlagMask = 0
    ButtonMask = 0

    # Enum QMessageBox.Icon
    NoIcon = 0
    Information = 0
    Warning = 0
    Critical = 0
    Question = 0

    # Enum QMessageBox.ButtonRole
    InvalidRole = 0
    AcceptRole = 0
    RejectRole = 0
    DestructiveRole = 0
    ActionRole = 0
    HelpRole = 0
    YesRole = 0
    NoRole = 0
    ResetRole = 0
    ApplyRole = 0

    def __init__(self, parent = None):
        '''void QMessageBox.__init__(QWidget parent = None)'''
    def __init__(self, icon, title, text, buttons = None, parent = None, flags = None):
        '''void QMessageBox.__init__(QMessageBox.Icon icon, str title, str text, QMessageBox.StandardButtons buttons = QMessageBox.NoButton, QWidget parent = None, Qt.WindowFlags flags = Qt.Dialog|Qt.MSWindowsFixedSizeDialogHint)'''
    def checkBox(self):
        '''QCheckBox QMessageBox.checkBox()'''
        return QCheckBox()
    def setCheckBox(self, cb):
        '''void QMessageBox.setCheckBox(QCheckBox cb)'''
    def textInteractionFlags(self):
        '''Qt.TextInteractionFlags QMessageBox.textInteractionFlags()'''
        return Qt.TextInteractionFlags()
    def setTextInteractionFlags(self, flags):
        '''void QMessageBox.setTextInteractionFlags(Qt.TextInteractionFlags flags)'''
    buttonClicked = pyqtSignal() # void buttonClicked(QAbstractButton*) - signal
    def buttonRole(self, button):
        '''QMessageBox.ButtonRole QMessageBox.buttonRole(QAbstractButton button)'''
        return QMessageBox.ButtonRole()
    def buttons(self):
        '''list-of-QAbstractButton QMessageBox.buttons()'''
        return [QAbstractButton()]
    def open(self):
        '''void QMessageBox.open()'''
    def open(self, slot):
        '''void QMessageBox.open(slot slot)'''
    def setWindowModality(self, windowModality):
        '''void QMessageBox.setWindowModality(Qt.WindowModality windowModality)'''
    def setWindowTitle(self, title):
        '''void QMessageBox.setWindowTitle(str title)'''
    def setDetailedText(self, text):
        '''void QMessageBox.setDetailedText(str text)'''
    def detailedText(self):
        '''str QMessageBox.detailedText()'''
        return str()
    def setInformativeText(self, text):
        '''void QMessageBox.setInformativeText(str text)'''
    def informativeText(self):
        '''str QMessageBox.informativeText()'''
        return str()
    def clickedButton(self):
        '''QAbstractButton QMessageBox.clickedButton()'''
        return QAbstractButton()
    def setEscapeButton(self, button):
        '''void QMessageBox.setEscapeButton(QAbstractButton button)'''
    def setEscapeButton(self, button):
        '''void QMessageBox.setEscapeButton(QMessageBox.StandardButton button)'''
    def escapeButton(self):
        '''QAbstractButton QMessageBox.escapeButton()'''
        return QAbstractButton()
    def setDefaultButton(self, button):
        '''void QMessageBox.setDefaultButton(QPushButton button)'''
    def setDefaultButton(self, button):
        '''void QMessageBox.setDefaultButton(QMessageBox.StandardButton button)'''
    def defaultButton(self):
        '''QPushButton QMessageBox.defaultButton()'''
        return QPushButton()
    def button(self, which):
        '''QAbstractButton QMessageBox.button(QMessageBox.StandardButton which)'''
        return QAbstractButton()
    def standardButton(self, button):
        '''QMessageBox.StandardButton QMessageBox.standardButton(QAbstractButton button)'''
        return QMessageBox.StandardButton()
    def standardButtons(self):
        '''QMessageBox.StandardButtons QMessageBox.standardButtons()'''
        return QMessageBox.StandardButtons()
    def setStandardButtons(self, buttons):
        '''void QMessageBox.setStandardButtons(QMessageBox.StandardButtons buttons)'''
    def removeButton(self, button):
        '''void QMessageBox.removeButton(QAbstractButton button)'''
    def addButton(self, button, role):
        '''void QMessageBox.addButton(QAbstractButton button, QMessageBox.ButtonRole role)'''
    def addButton(self, text, role):
        '''QPushButton QMessageBox.addButton(str text, QMessageBox.ButtonRole role)'''
        return QPushButton()
    def addButton(self, button):
        '''QPushButton QMessageBox.addButton(QMessageBox.StandardButton button)'''
        return QPushButton()
    def changeEvent(self):
        '''QEvent QMessageBox.changeEvent()'''
        return QEvent()
    def keyPressEvent(self):
        '''QKeyEvent QMessageBox.keyPressEvent()'''
        return QKeyEvent()
    def closeEvent(self):
        '''QCloseEvent QMessageBox.closeEvent()'''
        return QCloseEvent()
    def showEvent(self):
        '''QShowEvent QMessageBox.showEvent()'''
        return QShowEvent()
    def resizeEvent(self):
        '''QResizeEvent QMessageBox.resizeEvent()'''
        return QResizeEvent()
    def event(self, e):
        '''bool QMessageBox.event(QEvent e)'''
        return bool()
    def standardIcon(self, icon):
        '''static QPixmap QMessageBox.standardIcon(QMessageBox.Icon icon)'''
        return QPixmap()
    def aboutQt(self, parent, title = None):
        '''static void QMessageBox.aboutQt(QWidget parent, str title = '')'''
    def about(self, parent, caption, text):
        '''static void QMessageBox.about(QWidget parent, str caption, str text)'''
    def critical(self, parent, title, text, buttons = None, defaultButton = None):
        '''static QMessageBox.StandardButton QMessageBox.critical(QWidget parent, str title, str text, QMessageBox.StandardButtons buttons = QMessageBox.Ok, QMessageBox.StandardButton defaultButton = QMessageBox.NoButton)'''
        return QMessageBox.StandardButton()
    def warning(self, parent, title, text, buttons = None, defaultButton = None):
        '''static QMessageBox.StandardButton QMessageBox.warning(QWidget parent, str title, str text, QMessageBox.StandardButtons buttons = QMessageBox.Ok, QMessageBox.StandardButton defaultButton = QMessageBox.NoButton)'''
        return QMessageBox.StandardButton()
    def question(self, parent, title, text, buttons = None, defaultButton = None):
        '''static QMessageBox.StandardButton QMessageBox.question(QWidget parent, str title, str text, QMessageBox.StandardButtons buttons = QFlagslt;QMessageBox.StandardButtongt;(QFlag(81920)), QMessageBox.StandardButton defaultButton = QMessageBox.NoButton)'''
        return QMessageBox.StandardButton()
    def information(self, parent, title, text, buttons = None, defaultButton = None):
        '''static QMessageBox.StandardButton QMessageBox.information(QWidget parent, str title, str text, QMessageBox.StandardButtons buttons = QMessageBox.Ok, QMessageBox.StandardButton defaultButton = QMessageBox.NoButton)'''
        return QMessageBox.StandardButton()
    def setTextFormat(self):
        '''Qt.TextFormat QMessageBox.setTextFormat()'''
        return Qt.TextFormat()
    def textFormat(self):
        '''Qt.TextFormat QMessageBox.textFormat()'''
        return Qt.TextFormat()
    def setIconPixmap(self):
        '''QPixmap QMessageBox.setIconPixmap()'''
        return QPixmap()
    def iconPixmap(self):
        '''QPixmap QMessageBox.iconPixmap()'''
        return QPixmap()
    def setIcon(self):
        '''QMessageBox.Icon QMessageBox.setIcon()'''
        return QMessageBox.Icon()
    def icon(self):
        '''QMessageBox.Icon QMessageBox.icon()'''
        return QMessageBox.Icon()
    def setText(self):
        '''str QMessageBox.setText()'''
        return str()
    def text(self):
        '''str QMessageBox.text()'''
        return str()
    class StandardButtons():
        """"""
        def __init__(self):
            '''QMessageBox.StandardButtons QMessageBox.StandardButtons.__init__()'''
            return QMessageBox.StandardButtons()
        def __init__(self):
            '''int QMessageBox.StandardButtons.__init__()'''
            return int()
        def __init__(self):
            '''void QMessageBox.StandardButtons.__init__()'''
        def __bool__(self):
            '''int QMessageBox.StandardButtons.__bool__()'''
            return int()
        def __ne__(self, f):
            '''bool QMessageBox.StandardButtons.__ne__(QMessageBox.StandardButtons f)'''
            return bool()
        def __eq__(self, f):
            '''bool QMessageBox.StandardButtons.__eq__(QMessageBox.StandardButtons f)'''
            return bool()
        def __invert__(self):
            '''QMessageBox.StandardButtons QMessageBox.StandardButtons.__invert__()'''
            return QMessageBox.StandardButtons()
        def __and__(self, mask):
            '''QMessageBox.StandardButtons QMessageBox.StandardButtons.__and__(int mask)'''
            return QMessageBox.StandardButtons()
        def __xor__(self, f):
            '''QMessageBox.StandardButtons QMessageBox.StandardButtons.__xor__(QMessageBox.StandardButtons f)'''
            return QMessageBox.StandardButtons()
        def __xor__(self, f):
            '''QMessageBox.StandardButtons QMessageBox.StandardButtons.__xor__(int f)'''
            return QMessageBox.StandardButtons()
        def __or__(self, f):
            '''QMessageBox.StandardButtons QMessageBox.StandardButtons.__or__(QMessageBox.StandardButtons f)'''
            return QMessageBox.StandardButtons()
        def __or__(self, f):
            '''QMessageBox.StandardButtons QMessageBox.StandardButtons.__or__(int f)'''
            return QMessageBox.StandardButtons()
        def __int__(self):
            '''int QMessageBox.StandardButtons.__int__()'''
            return int()
        def __ixor__(self, f):
            '''QMessageBox.StandardButtons QMessageBox.StandardButtons.__ixor__(QMessageBox.StandardButtons f)'''
            return QMessageBox.StandardButtons()
        def __ior__(self, f):
            '''QMessageBox.StandardButtons QMessageBox.StandardButtons.__ior__(QMessageBox.StandardButtons f)'''
            return QMessageBox.StandardButtons()
        def __iand__(self, mask):
            '''QMessageBox.StandardButtons QMessageBox.StandardButtons.__iand__(int mask)'''
            return QMessageBox.StandardButtons()


class QMouseEventTransition(QEventTransition):
    """"""
    def __init__(self, sourceState = None):
        '''void QMouseEventTransition.__init__(QState sourceState = None)'''
    def __init__(self, object, type, button, sourceState = None):
        '''void QMouseEventTransition.__init__(QObject object, QEvent.Type type, Qt.MouseButton button, QState sourceState = None)'''
    def eventTest(self, event):
        '''bool QMouseEventTransition.eventTest(QEvent event)'''
        return bool()
    def onTransition(self, event):
        '''void QMouseEventTransition.onTransition(QEvent event)'''
    def setHitTestPath(self, path):
        '''void QMouseEventTransition.setHitTestPath(QPainterPath path)'''
    def hitTestPath(self):
        '''QPainterPath QMouseEventTransition.hitTestPath()'''
        return QPainterPath()
    def setModifierMask(self, modifiers):
        '''void QMouseEventTransition.setModifierMask(Qt.KeyboardModifiers modifiers)'''
    def modifierMask(self):
        '''Qt.KeyboardModifiers QMouseEventTransition.modifierMask()'''
        return Qt.KeyboardModifiers()
    def setButton(self, button):
        '''void QMouseEventTransition.setButton(Qt.MouseButton button)'''
    def button(self):
        '''Qt.MouseButton QMouseEventTransition.button()'''
        return Qt.MouseButton()


class QOpenGLWidget(QWidget):
    """"""
    # Enum QOpenGLWidget.UpdateBehavior
    NoPartialUpdate = 0
    PartialUpdate = 0

    def __init__(self, parent = None, flags = 0):
        '''void QOpenGLWidget.__init__(QWidget parent = None, Qt.WindowFlags flags = 0)'''
    def updateBehavior(self):
        '''QOpenGLWidget.UpdateBehavior QOpenGLWidget.updateBehavior()'''
        return QOpenGLWidget.UpdateBehavior()
    def setUpdateBehavior(self, updateBehavior):
        '''void QOpenGLWidget.setUpdateBehavior(QOpenGLWidget.UpdateBehavior updateBehavior)'''
    def paintEngine(self):
        '''QPaintEngine QOpenGLWidget.paintEngine()'''
        return QPaintEngine()
    def metric(self, metric):
        '''int QOpenGLWidget.metric(QPaintDevice.PaintDeviceMetric metric)'''
        return int()
    def event(self, e):
        '''bool QOpenGLWidget.event(QEvent e)'''
        return bool()
    def resizeEvent(self, e):
        '''void QOpenGLWidget.resizeEvent(QResizeEvent e)'''
    def paintEvent(self, e):
        '''void QOpenGLWidget.paintEvent(QPaintEvent e)'''
    def paintGL(self):
        '''void QOpenGLWidget.paintGL()'''
    def resizeGL(self, w, h):
        '''void QOpenGLWidget.resizeGL(int w, int h)'''
    def initializeGL(self):
        '''void QOpenGLWidget.initializeGL()'''
    resized = pyqtSignal() # void resized() - signal
    aboutToResize = pyqtSignal() # void aboutToResize() - signal
    frameSwapped = pyqtSignal() # void frameSwapped() - signal
    aboutToCompose = pyqtSignal() # void aboutToCompose() - signal
    def grabFramebuffer(self):
        '''QImage QOpenGLWidget.grabFramebuffer()'''
        return QImage()
    def defaultFramebufferObject(self):
        '''int QOpenGLWidget.defaultFramebufferObject()'''
        return int()
    def context(self):
        '''QOpenGLContext QOpenGLWidget.context()'''
        return QOpenGLContext()
    def doneCurrent(self):
        '''void QOpenGLWidget.doneCurrent()'''
    def makeCurrent(self):
        '''void QOpenGLWidget.makeCurrent()'''
    def isValid(self):
        '''bool QOpenGLWidget.isValid()'''
        return bool()
    def format(self):
        '''QSurfaceFormat QOpenGLWidget.format()'''
        return QSurfaceFormat()
    def setFormat(self, format):
        '''void QOpenGLWidget.setFormat(QSurfaceFormat format)'''


class QPlainTextEdit(QAbstractScrollArea):
    """"""
    # Enum QPlainTextEdit.LineWrapMode
    NoWrap = 0
    WidgetWidth = 0

    def __init__(self, parent = None):
        '''void QPlainTextEdit.__init__(QWidget parent = None)'''
    def __init__(self, text, parent = None):
        '''void QPlainTextEdit.__init__(str text, QWidget parent = None)'''
    def placeholderText(self):
        '''str QPlainTextEdit.placeholderText()'''
        return str()
    def setPlaceholderText(self, placeholderText):
        '''void QPlainTextEdit.setPlaceholderText(str placeholderText)'''
    def zoomOut(self, range = 1):
        '''void QPlainTextEdit.zoomOut(int range = 1)'''
    def zoomIn(self, range = 1):
        '''void QPlainTextEdit.zoomIn(int range = 1)'''
    def anchorAt(self, pos):
        '''str QPlainTextEdit.anchorAt(QPoint pos)'''
        return str()
    def getPaintContext(self):
        '''QAbstractTextDocumentLayout.PaintContext QPlainTextEdit.getPaintContext()'''
        return QAbstractTextDocumentLayout.PaintContext()
    def blockBoundingGeometry(self, block):
        '''QRectF QPlainTextEdit.blockBoundingGeometry(QTextBlock block)'''
        return QRectF()
    def blockBoundingRect(self, block):
        '''QRectF QPlainTextEdit.blockBoundingRect(QTextBlock block)'''
        return QRectF()
    def contentOffset(self):
        '''QPointF QPlainTextEdit.contentOffset()'''
        return QPointF()
    def firstVisibleBlock(self):
        '''QTextBlock QPlainTextEdit.firstVisibleBlock()'''
        return QTextBlock()
    def scrollContentsBy(self, dx, dy):
        '''void QPlainTextEdit.scrollContentsBy(int dx, int dy)'''
    def insertFromMimeData(self, source):
        '''void QPlainTextEdit.insertFromMimeData(QMimeData source)'''
    def canInsertFromMimeData(self, source):
        '''bool QPlainTextEdit.canInsertFromMimeData(QMimeData source)'''
        return bool()
    def createMimeDataFromSelection(self):
        '''QMimeData QPlainTextEdit.createMimeDataFromSelection()'''
        return QMimeData()
    def inputMethodQuery(self, property):
        '''QVariant QPlainTextEdit.inputMethodQuery(Qt.InputMethodQuery property)'''
        return QVariant()
    def inputMethodQuery(self, query, argument):
        '''QVariant QPlainTextEdit.inputMethodQuery(Qt.InputMethodQuery query, QVariant argument)'''
        return QVariant()
    def inputMethodEvent(self):
        '''QInputMethodEvent QPlainTextEdit.inputMethodEvent()'''
        return QInputMethodEvent()
    def wheelEvent(self, e):
        '''void QPlainTextEdit.wheelEvent(QWheelEvent e)'''
    def changeEvent(self, e):
        '''void QPlainTextEdit.changeEvent(QEvent e)'''
    def showEvent(self):
        '''QShowEvent QPlainTextEdit.showEvent()'''
        return QShowEvent()
    def focusOutEvent(self, e):
        '''void QPlainTextEdit.focusOutEvent(QFocusEvent e)'''
    def focusInEvent(self, e):
        '''void QPlainTextEdit.focusInEvent(QFocusEvent e)'''
    def dropEvent(self, e):
        '''void QPlainTextEdit.dropEvent(QDropEvent e)'''
    def dragMoveEvent(self, e):
        '''void QPlainTextEdit.dragMoveEvent(QDragMoveEvent e)'''
    def dragLeaveEvent(self, e):
        '''void QPlainTextEdit.dragLeaveEvent(QDragLeaveEvent e)'''
    def dragEnterEvent(self, e):
        '''void QPlainTextEdit.dragEnterEvent(QDragEnterEvent e)'''
    def contextMenuEvent(self, e):
        '''void QPlainTextEdit.contextMenuEvent(QContextMenuEvent e)'''
    def focusNextPrevChild(self, next):
        '''bool QPlainTextEdit.focusNextPrevChild(bool next)'''
        return bool()
    def mouseDoubleClickEvent(self, e):
        '''void QPlainTextEdit.mouseDoubleClickEvent(QMouseEvent e)'''
    def mouseReleaseEvent(self, e):
        '''void QPlainTextEdit.mouseReleaseEvent(QMouseEvent e)'''
    def mouseMoveEvent(self, e):
        '''void QPlainTextEdit.mouseMoveEvent(QMouseEvent e)'''
    def mousePressEvent(self, e):
        '''void QPlainTextEdit.mousePressEvent(QMouseEvent e)'''
    def paintEvent(self, e):
        '''void QPlainTextEdit.paintEvent(QPaintEvent e)'''
    def resizeEvent(self, e):
        '''void QPlainTextEdit.resizeEvent(QResizeEvent e)'''
    def keyReleaseEvent(self, e):
        '''void QPlainTextEdit.keyReleaseEvent(QKeyEvent e)'''
    def keyPressEvent(self, e):
        '''void QPlainTextEdit.keyPressEvent(QKeyEvent e)'''
    def timerEvent(self, e):
        '''void QPlainTextEdit.timerEvent(QTimerEvent e)'''
    def event(self, e):
        '''bool QPlainTextEdit.event(QEvent e)'''
        return bool()
    modificationChanged = pyqtSignal() # void modificationChanged(bool) - signal
    blockCountChanged = pyqtSignal() # void blockCountChanged(int) - signal
    updateRequest = pyqtSignal() # void updateRequest(const QRectamp;,int) - signal
    cursorPositionChanged = pyqtSignal() # void cursorPositionChanged() - signal
    selectionChanged = pyqtSignal() # void selectionChanged() - signal
    copyAvailable = pyqtSignal() # void copyAvailable(bool) - signal
    redoAvailable = pyqtSignal() # void redoAvailable(bool) - signal
    undoAvailable = pyqtSignal() # void undoAvailable(bool) - signal
    textChanged = pyqtSignal() # void textChanged() - signal
    def centerCursor(self):
        '''void QPlainTextEdit.centerCursor()'''
    def appendHtml(self, html):
        '''void QPlainTextEdit.appendHtml(str html)'''
    def appendPlainText(self, text):
        '''void QPlainTextEdit.appendPlainText(str text)'''
    def insertPlainText(self, text):
        '''void QPlainTextEdit.insertPlainText(str text)'''
    def selectAll(self):
        '''void QPlainTextEdit.selectAll()'''
    def clear(self):
        '''void QPlainTextEdit.clear()'''
    def redo(self):
        '''void QPlainTextEdit.redo()'''
    def undo(self):
        '''void QPlainTextEdit.undo()'''
    def paste(self):
        '''void QPlainTextEdit.paste()'''
    def copy(self):
        '''void QPlainTextEdit.copy()'''
    def cut(self):
        '''void QPlainTextEdit.cut()'''
    def setPlainText(self, text):
        '''void QPlainTextEdit.setPlainText(str text)'''
    def blockCount(self):
        '''int QPlainTextEdit.blockCount()'''
        return int()
    def print_(self, printer):
        '''void QPlainTextEdit.print_(QPagedPaintDevice printer)'''
    def canPaste(self):
        '''bool QPlainTextEdit.canPaste()'''
        return bool()
    def moveCursor(self, operation, mode = None):
        '''void QPlainTextEdit.moveCursor(QTextCursor.MoveOperation operation, QTextCursor.MoveMode mode = QTextCursor.MoveAnchor)'''
    def extraSelections(self):
        '''list-of-QTextEdit.ExtraSelection QPlainTextEdit.extraSelections()'''
        return [QTextEdit.ExtraSelection()]
    def setExtraSelections(self, selections):
        '''void QPlainTextEdit.setExtraSelections(list-of-QTextEdit.ExtraSelection selections)'''
    def setCursorWidth(self, width):
        '''void QPlainTextEdit.setCursorWidth(int width)'''
    def cursorWidth(self):
        '''int QPlainTextEdit.cursorWidth()'''
        return int()
    def setTabStopWidth(self, width):
        '''void QPlainTextEdit.setTabStopWidth(int width)'''
    def tabStopWidth(self):
        '''int QPlainTextEdit.tabStopWidth()'''
        return int()
    def setOverwriteMode(self, overwrite):
        '''void QPlainTextEdit.setOverwriteMode(bool overwrite)'''
    def overwriteMode(self):
        '''bool QPlainTextEdit.overwriteMode()'''
        return bool()
    def cursorRect(self, cursor):
        '''QRect QPlainTextEdit.cursorRect(QTextCursor cursor)'''
        return QRect()
    def cursorRect(self):
        '''QRect QPlainTextEdit.cursorRect()'''
        return QRect()
    def cursorForPosition(self, pos):
        '''QTextCursor QPlainTextEdit.cursorForPosition(QPoint pos)'''
        return QTextCursor()
    def createStandardContextMenu(self):
        '''QMenu QPlainTextEdit.createStandardContextMenu()'''
        return QMenu()
    def createStandardContextMenu(self, position):
        '''QMenu QPlainTextEdit.createStandardContextMenu(QPoint position)'''
        return QMenu()
    def loadResource(self, type, name):
        '''QVariant QPlainTextEdit.loadResource(int type, QUrl name)'''
        return QVariant()
    def ensureCursorVisible(self):
        '''void QPlainTextEdit.ensureCursorVisible()'''
    def toPlainText(self):
        '''str QPlainTextEdit.toPlainText()'''
        return str()
    def find(self, exp, options = 0):
        '''bool QPlainTextEdit.find(str exp, QTextDocument.FindFlags options = 0)'''
        return bool()
    def find(self, exp, options = 0):
        '''bool QPlainTextEdit.find(QRegExp exp, QTextDocument.FindFlags options = 0)'''
        return bool()
    def centerOnScroll(self):
        '''bool QPlainTextEdit.centerOnScroll()'''
        return bool()
    def setCenterOnScroll(self, enabled):
        '''void QPlainTextEdit.setCenterOnScroll(bool enabled)'''
    def backgroundVisible(self):
        '''bool QPlainTextEdit.backgroundVisible()'''
        return bool()
    def setBackgroundVisible(self, visible):
        '''void QPlainTextEdit.setBackgroundVisible(bool visible)'''
    def setWordWrapMode(self, policy):
        '''void QPlainTextEdit.setWordWrapMode(QTextOption.WrapMode policy)'''
    def wordWrapMode(self):
        '''QTextOption.WrapMode QPlainTextEdit.wordWrapMode()'''
        return QTextOption.WrapMode()
    def setLineWrapMode(self, mode):
        '''void QPlainTextEdit.setLineWrapMode(QPlainTextEdit.LineWrapMode mode)'''
    def lineWrapMode(self):
        '''QPlainTextEdit.LineWrapMode QPlainTextEdit.lineWrapMode()'''
        return QPlainTextEdit.LineWrapMode()
    def maximumBlockCount(self):
        '''int QPlainTextEdit.maximumBlockCount()'''
        return int()
    def setMaximumBlockCount(self, maximum):
        '''void QPlainTextEdit.setMaximumBlockCount(int maximum)'''
    def setUndoRedoEnabled(self, enable):
        '''void QPlainTextEdit.setUndoRedoEnabled(bool enable)'''
    def isUndoRedoEnabled(self):
        '''bool QPlainTextEdit.isUndoRedoEnabled()'''
        return bool()
    def documentTitle(self):
        '''str QPlainTextEdit.documentTitle()'''
        return str()
    def setDocumentTitle(self, title):
        '''void QPlainTextEdit.setDocumentTitle(str title)'''
    def setTabChangesFocus(self, b):
        '''void QPlainTextEdit.setTabChangesFocus(bool b)'''
    def tabChangesFocus(self):
        '''bool QPlainTextEdit.tabChangesFocus()'''
        return bool()
    def currentCharFormat(self):
        '''QTextCharFormat QPlainTextEdit.currentCharFormat()'''
        return QTextCharFormat()
    def setCurrentCharFormat(self, format):
        '''void QPlainTextEdit.setCurrentCharFormat(QTextCharFormat format)'''
    def mergeCurrentCharFormat(self, modifier):
        '''void QPlainTextEdit.mergeCurrentCharFormat(QTextCharFormat modifier)'''
    def textInteractionFlags(self):
        '''Qt.TextInteractionFlags QPlainTextEdit.textInteractionFlags()'''
        return Qt.TextInteractionFlags()
    def setTextInteractionFlags(self, flags):
        '''void QPlainTextEdit.setTextInteractionFlags(Qt.TextInteractionFlags flags)'''
    def setReadOnly(self, ro):
        '''void QPlainTextEdit.setReadOnly(bool ro)'''
    def isReadOnly(self):
        '''bool QPlainTextEdit.isReadOnly()'''
        return bool()
    def textCursor(self):
        '''QTextCursor QPlainTextEdit.textCursor()'''
        return QTextCursor()
    def setTextCursor(self, cursor):
        '''void QPlainTextEdit.setTextCursor(QTextCursor cursor)'''
    def document(self):
        '''QTextDocument QPlainTextEdit.document()'''
        return QTextDocument()
    def setDocument(self, document):
        '''void QPlainTextEdit.setDocument(QTextDocument document)'''


class QPlainTextDocumentLayout(QAbstractTextDocumentLayout):
    """"""
    def __init__(self, document):
        '''void QPlainTextDocumentLayout.__init__(QTextDocument document)'''
    def documentChanged(self, from_, charsAdded):
        '''int QPlainTextDocumentLayout.documentChanged(int from, int charsAdded)'''
        return int()
    def requestUpdate(self):
        '''void QPlainTextDocumentLayout.requestUpdate()'''
    def cursorWidth(self):
        '''int QPlainTextDocumentLayout.cursorWidth()'''
        return int()
    def setCursorWidth(self, width):
        '''void QPlainTextDocumentLayout.setCursorWidth(int width)'''
    def ensureBlockLayout(self, block):
        '''void QPlainTextDocumentLayout.ensureBlockLayout(QTextBlock block)'''
    def blockBoundingRect(self, block):
        '''QRectF QPlainTextDocumentLayout.blockBoundingRect(QTextBlock block)'''
        return QRectF()
    def frameBoundingRect(self):
        '''QTextFrame QPlainTextDocumentLayout.frameBoundingRect()'''
        return QTextFrame()
    def documentSize(self):
        '''QSizeF QPlainTextDocumentLayout.documentSize()'''
        return QSizeF()
    def pageCount(self):
        '''int QPlainTextDocumentLayout.pageCount()'''
        return int()
    def hitTest(self):
        '''Qt.HitTestAccuracy QPlainTextDocumentLayout.hitTest()'''
        return Qt.HitTestAccuracy()
    def draw(self):
        '''QAbstractTextDocumentLayout.PaintContext QPlainTextDocumentLayout.draw()'''
        return QAbstractTextDocumentLayout.PaintContext()


class QProgressBar(QWidget):
    """"""
    # Enum QProgressBar.Direction
    TopToBottom = 0
    BottomToTop = 0

    def __init__(self, parent = None):
        '''void QProgressBar.__init__(QWidget parent = None)'''
    def paintEvent(self):
        '''QPaintEvent QProgressBar.paintEvent()'''
        return QPaintEvent()
    def event(self, e):
        '''bool QProgressBar.event(QEvent e)'''
        return bool()
    def initStyleOption(self, option):
        '''void QProgressBar.initStyleOption(QStyleOptionProgressBar option)'''
    valueChanged = pyqtSignal() # void valueChanged(int) - signal
    def setOrientation(self):
        '''Qt.Orientation QProgressBar.setOrientation()'''
        return Qt.Orientation()
    def setValue(self, value):
        '''void QProgressBar.setValue(int value)'''
    def setMaximum(self, maximum):
        '''void QProgressBar.setMaximum(int maximum)'''
    def setMinimum(self, minimum):
        '''void QProgressBar.setMinimum(int minimum)'''
    def reset(self):
        '''void QProgressBar.reset()'''
    def resetFormat(self):
        '''void QProgressBar.resetFormat()'''
    def format(self):
        '''str QProgressBar.format()'''
        return str()
    def setFormat(self, format):
        '''void QProgressBar.setFormat(str format)'''
    def setTextDirection(self, textDirection):
        '''void QProgressBar.setTextDirection(QProgressBar.Direction textDirection)'''
    def setInvertedAppearance(self, invert):
        '''void QProgressBar.setInvertedAppearance(bool invert)'''
    def orientation(self):
        '''Qt.Orientation QProgressBar.orientation()'''
        return Qt.Orientation()
    def minimumSizeHint(self):
        '''QSize QProgressBar.minimumSizeHint()'''
        return QSize()
    def sizeHint(self):
        '''QSize QProgressBar.sizeHint()'''
        return QSize()
    def setAlignment(self, alignment):
        '''void QProgressBar.setAlignment(Qt.Alignment alignment)'''
    def alignment(self):
        '''Qt.Alignment QProgressBar.alignment()'''
        return Qt.Alignment()
    def isTextVisible(self):
        '''bool QProgressBar.isTextVisible()'''
        return bool()
    def setTextVisible(self, visible):
        '''void QProgressBar.setTextVisible(bool visible)'''
    def text(self):
        '''str QProgressBar.text()'''
        return str()
    def value(self):
        '''int QProgressBar.value()'''
        return int()
    def setRange(self, minimum, maximum):
        '''void QProgressBar.setRange(int minimum, int maximum)'''
    def maximum(self):
        '''int QProgressBar.maximum()'''
        return int()
    def minimum(self):
        '''int QProgressBar.minimum()'''
        return int()


class QProgressDialog(QDialog):
    """"""
    def __init__(self, parent = None, flags = 0):
        '''void QProgressDialog.__init__(QWidget parent = None, Qt.WindowFlags flags = 0)'''
    def __init__(self, labelText, cancelButtonText, minimum, maximum, parent = None, flags = 0):
        '''void QProgressDialog.__init__(str labelText, str cancelButtonText, int minimum, int maximum, QWidget parent = None, Qt.WindowFlags flags = 0)'''
    def open(self):
        '''void QProgressDialog.open()'''
    def open(self, slot):
        '''void QProgressDialog.open(slot slot)'''
    def forceShow(self):
        '''void QProgressDialog.forceShow()'''
    def showEvent(self, e):
        '''void QProgressDialog.showEvent(QShowEvent e)'''
    def changeEvent(self):
        '''QEvent QProgressDialog.changeEvent()'''
        return QEvent()
    def closeEvent(self):
        '''QCloseEvent QProgressDialog.closeEvent()'''
        return QCloseEvent()
    def resizeEvent(self):
        '''QResizeEvent QProgressDialog.resizeEvent()'''
        return QResizeEvent()
    canceled = pyqtSignal() # void canceled() - signal
    def setMinimumDuration(self, ms):
        '''void QProgressDialog.setMinimumDuration(int ms)'''
    def setCancelButtonText(self):
        '''str QProgressDialog.setCancelButtonText()'''
        return str()
    def setLabelText(self):
        '''str QProgressDialog.setLabelText()'''
        return str()
    def setValue(self, progress):
        '''void QProgressDialog.setValue(int progress)'''
    def setMinimum(self, minimum):
        '''void QProgressDialog.setMinimum(int minimum)'''
    def setMaximum(self, maximum):
        '''void QProgressDialog.setMaximum(int maximum)'''
    def reset(self):
        '''void QProgressDialog.reset()'''
    def cancel(self):
        '''void QProgressDialog.cancel()'''
    def autoClose(self):
        '''bool QProgressDialog.autoClose()'''
        return bool()
    def setAutoClose(self, b):
        '''void QProgressDialog.setAutoClose(bool b)'''
    def autoReset(self):
        '''bool QProgressDialog.autoReset()'''
        return bool()
    def setAutoReset(self, b):
        '''void QProgressDialog.setAutoReset(bool b)'''
    def minimumDuration(self):
        '''int QProgressDialog.minimumDuration()'''
        return int()
    def labelText(self):
        '''str QProgressDialog.labelText()'''
        return str()
    def sizeHint(self):
        '''QSize QProgressDialog.sizeHint()'''
        return QSize()
    def value(self):
        '''int QProgressDialog.value()'''
        return int()
    def setRange(self, minimum, maximum):
        '''void QProgressDialog.setRange(int minimum, int maximum)'''
    def maximum(self):
        '''int QProgressDialog.maximum()'''
        return int()
    def minimum(self):
        '''int QProgressDialog.minimum()'''
        return int()
    def wasCanceled(self):
        '''bool QProgressDialog.wasCanceled()'''
        return bool()
    def setBar(self, bar):
        '''void QProgressDialog.setBar(QProgressBar bar)'''
    def setCancelButton(self, button):
        '''void QProgressDialog.setCancelButton(QPushButton button)'''
    def setLabel(self, label):
        '''void QProgressDialog.setLabel(QLabel label)'''


class QProxyStyle(QCommonStyle):
    """"""
    def __init__(self, style = None):
        '''void QProxyStyle.__init__(QStyle style = None)'''
    def __init__(self, key):
        '''void QProxyStyle.__init__(str key)'''
    def event(self, e):
        '''bool QProxyStyle.event(QEvent e)'''
        return bool()
    def unpolish(self, widget):
        '''void QProxyStyle.unpolish(QWidget widget)'''
    def unpolish(self, app):
        '''void QProxyStyle.unpolish(QApplication app)'''
    def polish(self, widget):
        '''void QProxyStyle.polish(QWidget widget)'''
    def polish(self, pal):
        '''void QProxyStyle.polish(QPalette pal)'''
    def polish(self, app):
        '''void QProxyStyle.polish(QApplication app)'''
    def standardPalette(self):
        '''QPalette QProxyStyle.standardPalette()'''
        return QPalette()
    def generatedIconPixmap(self, iconMode, pixmap, opt):
        '''QPixmap QProxyStyle.generatedIconPixmap(QIcon.Mode iconMode, QPixmap pixmap, QStyleOption opt)'''
        return QPixmap()
    def standardPixmap(self, standardPixmap, opt, widget = None):
        '''QPixmap QProxyStyle.standardPixmap(QStyle.StandardPixmap standardPixmap, QStyleOption opt, QWidget widget = None)'''
        return QPixmap()
    def standardIcon(self, standardIcon, option = None, widget = None):
        '''QIcon QProxyStyle.standardIcon(QStyle.StandardPixmap standardIcon, QStyleOption option = None, QWidget widget = None)'''
        return QIcon()
    def layoutSpacing(self, control1, control2, orientation, option = None, widget = None):
        '''int QProxyStyle.layoutSpacing(QSizePolicy.ControlType control1, QSizePolicy.ControlType control2, Qt.Orientation orientation, QStyleOption option = None, QWidget widget = None)'''
        return int()
    def pixelMetric(self, metric, option = None, widget = None):
        '''int QProxyStyle.pixelMetric(QStyle.PixelMetric metric, QStyleOption option = None, QWidget widget = None)'''
        return int()
    def styleHint(self, hint, option = None, widget = None, returnData = None):
        '''int QProxyStyle.styleHint(QStyle.StyleHint hint, QStyleOption option = None, QWidget widget = None, QStyleHintReturn returnData = None)'''
        return int()
    def hitTestComplexControl(self, control, option, pos, widget = None):
        '''QStyle.SubControl QProxyStyle.hitTestComplexControl(QStyle.ComplexControl control, QStyleOptionComplex option, QPoint pos, QWidget widget = None)'''
        return QStyle.SubControl()
    def itemPixmapRect(self, r, flags, pixmap):
        '''QRect QProxyStyle.itemPixmapRect(QRect r, int flags, QPixmap pixmap)'''
        return QRect()
    def itemTextRect(self, fm, r, flags, enabled, text):
        '''QRect QProxyStyle.itemTextRect(QFontMetrics fm, QRect r, int flags, bool enabled, str text)'''
        return QRect()
    def subControlRect(self, cc, opt, sc, widget):
        '''QRect QProxyStyle.subControlRect(QStyle.ComplexControl cc, QStyleOptionComplex opt, QStyle.SubControl sc, QWidget widget)'''
        return QRect()
    def subElementRect(self, element, option, widget):
        '''QRect QProxyStyle.subElementRect(QStyle.SubElement element, QStyleOption option, QWidget widget)'''
        return QRect()
    def sizeFromContents(self, type, option, size, widget):
        '''QSize QProxyStyle.sizeFromContents(QStyle.ContentsType type, QStyleOption option, QSize size, QWidget widget)'''
        return QSize()
    def drawItemPixmap(self, painter, rect, alignment, pixmap):
        '''void QProxyStyle.drawItemPixmap(QPainter painter, QRect rect, int alignment, QPixmap pixmap)'''
    def drawItemText(self, painter, rect, flags, pal, enabled, text, textRole = None):
        '''void QProxyStyle.drawItemText(QPainter painter, QRect rect, int flags, QPalette pal, bool enabled, str text, QPalette.ColorRole textRole = QPalette.NoRole)'''
    def drawComplexControl(self, control, option, painter, widget = None):
        '''void QProxyStyle.drawComplexControl(QStyle.ComplexControl control, QStyleOptionComplex option, QPainter painter, QWidget widget = None)'''
    def drawControl(self, element, option, painter, widget = None):
        '''void QProxyStyle.drawControl(QStyle.ControlElement element, QStyleOption option, QPainter painter, QWidget widget = None)'''
    def drawPrimitive(self, element, option, painter, widget = None):
        '''void QProxyStyle.drawPrimitive(QStyle.PrimitiveElement element, QStyleOption option, QPainter painter, QWidget widget = None)'''
    def setBaseStyle(self, style):
        '''void QProxyStyle.setBaseStyle(QStyle style)'''
    def baseStyle(self):
        '''QStyle QProxyStyle.baseStyle()'''
        return QStyle()


class QRadioButton(QAbstractButton):
    """"""
    def __init__(self, parent = None):
        '''void QRadioButton.__init__(QWidget parent = None)'''
    def __init__(self, text, parent = None):
        '''void QRadioButton.__init__(str text, QWidget parent = None)'''
    def mouseMoveEvent(self):
        '''QMouseEvent QRadioButton.mouseMoveEvent()'''
        return QMouseEvent()
    def paintEvent(self):
        '''QPaintEvent QRadioButton.paintEvent()'''
        return QPaintEvent()
    def event(self, e):
        '''bool QRadioButton.event(QEvent e)'''
        return bool()
    def hitButton(self):
        '''QPoint QRadioButton.hitButton()'''
        return QPoint()
    def initStyleOption(self, button):
        '''void QRadioButton.initStyleOption(QStyleOptionButton button)'''
    def minimumSizeHint(self):
        '''QSize QRadioButton.minimumSizeHint()'''
        return QSize()
    def sizeHint(self):
        '''QSize QRadioButton.sizeHint()'''
        return QSize()


class QRubberBand(QWidget):
    """"""
    # Enum QRubberBand.Shape
    Line = 0
    Rectangle = 0

    def __init__(self, parent = None):
        '''QRubberBand.Shape QRubberBand.__init__(QWidget parent = None)'''
        return QRubberBand.Shape()
    def moveEvent(self):
        '''QMoveEvent QRubberBand.moveEvent()'''
        return QMoveEvent()
    def resizeEvent(self):
        '''QResizeEvent QRubberBand.resizeEvent()'''
        return QResizeEvent()
    def showEvent(self):
        '''QShowEvent QRubberBand.showEvent()'''
        return QShowEvent()
    def changeEvent(self):
        '''QEvent QRubberBand.changeEvent()'''
        return QEvent()
    def paintEvent(self):
        '''QPaintEvent QRubberBand.paintEvent()'''
        return QPaintEvent()
    def event(self, e):
        '''bool QRubberBand.event(QEvent e)'''
        return bool()
    def initStyleOption(self, option):
        '''void QRubberBand.initStyleOption(QStyleOptionRubberBand option)'''
    def resize(self, w, h):
        '''void QRubberBand.resize(int w, int h)'''
    def resize(self, s):
        '''void QRubberBand.resize(QSize s)'''
    def move(self, p):
        '''void QRubberBand.move(QPoint p)'''
    def move(self, ax, ay):
        '''void QRubberBand.move(int ax, int ay)'''
    def setGeometry(self, r):
        '''void QRubberBand.setGeometry(QRect r)'''
    def setGeometry(self, ax, ay, aw, ah):
        '''void QRubberBand.setGeometry(int ax, int ay, int aw, int ah)'''
    def shape(self):
        '''QRubberBand.Shape QRubberBand.shape()'''
        return QRubberBand.Shape()


class QScrollArea(QAbstractScrollArea):
    """"""
    def __init__(self, parent = None):
        '''void QScrollArea.__init__(QWidget parent = None)'''
    def viewportSizeHint(self):
        '''QSize QScrollArea.viewportSizeHint()'''
        return QSize()
    def scrollContentsBy(self, dx, dy):
        '''void QScrollArea.scrollContentsBy(int dx, int dy)'''
    def resizeEvent(self):
        '''QResizeEvent QScrollArea.resizeEvent()'''
        return QResizeEvent()
    def eventFilter(self):
        '''QEvent QScrollArea.eventFilter()'''
        return QEvent()
    def event(self):
        '''QEvent QScrollArea.event()'''
        return QEvent()
    def ensureWidgetVisible(self, childWidget, xMargin = 50, yMargin = 50):
        '''void QScrollArea.ensureWidgetVisible(QWidget childWidget, int xMargin = 50, int yMargin = 50)'''
    def ensureVisible(self, x, y, xMargin = 50, yMargin = 50):
        '''void QScrollArea.ensureVisible(int x, int y, int xMargin = 50, int yMargin = 50)'''
    def focusNextPrevChild(self, next):
        '''bool QScrollArea.focusNextPrevChild(bool next)'''
        return bool()
    def sizeHint(self):
        '''QSize QScrollArea.sizeHint()'''
        return QSize()
    def setAlignment(self):
        '''Qt.Alignment QScrollArea.setAlignment()'''
        return Qt.Alignment()
    def alignment(self):
        '''Qt.Alignment QScrollArea.alignment()'''
        return Qt.Alignment()
    def setWidgetResizable(self, resizable):
        '''void QScrollArea.setWidgetResizable(bool resizable)'''
    def widgetResizable(self):
        '''bool QScrollArea.widgetResizable()'''
        return bool()
    def takeWidget(self):
        '''QWidget QScrollArea.takeWidget()'''
        return QWidget()
    def setWidget(self, w):
        '''void QScrollArea.setWidget(QWidget w)'''
    def widget(self):
        '''QWidget QScrollArea.widget()'''
        return QWidget()


class QScrollBar(QAbstractSlider):
    """"""
    def __init__(self, parent = None):
        '''void QScrollBar.__init__(QWidget parent = None)'''
    def __init__(self, orientation, parent = None):
        '''void QScrollBar.__init__(Qt.Orientation orientation, QWidget parent = None)'''
    def sliderChange(self, change):
        '''void QScrollBar.sliderChange(QAbstractSlider.SliderChange change)'''
    def wheelEvent(self):
        '''QWheelEvent QScrollBar.wheelEvent()'''
        return QWheelEvent()
    def contextMenuEvent(self):
        '''QContextMenuEvent QScrollBar.contextMenuEvent()'''
        return QContextMenuEvent()
    def hideEvent(self):
        '''QHideEvent QScrollBar.hideEvent()'''
        return QHideEvent()
    def mouseMoveEvent(self):
        '''QMouseEvent QScrollBar.mouseMoveEvent()'''
        return QMouseEvent()
    def mouseReleaseEvent(self):
        '''QMouseEvent QScrollBar.mouseReleaseEvent()'''
        return QMouseEvent()
    def mousePressEvent(self):
        '''QMouseEvent QScrollBar.mousePressEvent()'''
        return QMouseEvent()
    def paintEvent(self):
        '''QPaintEvent QScrollBar.paintEvent()'''
        return QPaintEvent()
    def initStyleOption(self, option):
        '''void QScrollBar.initStyleOption(QStyleOptionSlider option)'''
    def event(self, event):
        '''bool QScrollBar.event(QEvent event)'''
        return bool()
    def sizeHint(self):
        '''QSize QScrollBar.sizeHint()'''
        return QSize()


class QScroller(QObject):
    """"""
    # Enum QScroller.Input
    InputPress = 0
    InputMove = 0
    InputRelease = 0

    # Enum QScroller.ScrollerGestureType
    TouchGesture = 0
    LeftMouseButtonGesture = 0
    RightMouseButtonGesture = 0
    MiddleMouseButtonGesture = 0

    # Enum QScroller.State
    Inactive = 0
    Pressed = 0
    Dragging = 0
    Scrolling = 0

    scrollerPropertiesChanged = pyqtSignal() # void scrollerPropertiesChanged(const QScrollerPropertiesamp;) - signal
    stateChanged = pyqtSignal() # void stateChanged(QScroller::State) - signal
    def resendPrepareEvent(self):
        '''void QScroller.resendPrepareEvent()'''
    def ensureVisible(self, rect, xmargin, ymargin):
        '''void QScroller.ensureVisible(QRectF rect, float xmargin, float ymargin)'''
    def ensureVisible(self, rect, xmargin, ymargin, scrollTime):
        '''void QScroller.ensureVisible(QRectF rect, float xmargin, float ymargin, int scrollTime)'''
    def scrollTo(self, pos):
        '''void QScroller.scrollTo(QPointF pos)'''
    def scrollTo(self, pos, scrollTime):
        '''void QScroller.scrollTo(QPointF pos, int scrollTime)'''
    def setScrollerProperties(self, prop):
        '''void QScroller.setScrollerProperties(QScrollerProperties prop)'''
    def setSnapPositionsY(self, positions):
        '''void QScroller.setSnapPositionsY(list-of-float positions)'''
    def setSnapPositionsY(self, first, interval):
        '''void QScroller.setSnapPositionsY(float first, float interval)'''
    def setSnapPositionsX(self, positions):
        '''void QScroller.setSnapPositionsX(list-of-float positions)'''
    def setSnapPositionsX(self, first, interval):
        '''void QScroller.setSnapPositionsX(float first, float interval)'''
    def scrollerProperties(self):
        '''QScrollerProperties QScroller.scrollerProperties()'''
        return QScrollerProperties()
    def pixelPerMeter(self):
        '''QPointF QScroller.pixelPerMeter()'''
        return QPointF()
    def finalPosition(self):
        '''QPointF QScroller.finalPosition()'''
        return QPointF()
    def velocity(self):
        '''QPointF QScroller.velocity()'''
        return QPointF()
    def stop(self):
        '''void QScroller.stop()'''
    def handleInput(self, input, position, timestamp = 0):
        '''bool QScroller.handleInput(QScroller.Input input, QPointF position, int timestamp = 0)'''
        return bool()
    def state(self):
        '''QScroller.State QScroller.state()'''
        return QScroller.State()
    def target(self):
        '''QObject QScroller.target()'''
        return QObject()
    def activeScrollers(self):
        '''static list-of-QScroller QScroller.activeScrollers()'''
        return [QScroller()]
    def ungrabGesture(self, target):
        '''static void QScroller.ungrabGesture(QObject target)'''
    def grabbedGesture(self, target):
        '''static Qt.GestureType QScroller.grabbedGesture(QObject target)'''
        return Qt.GestureType()
    def grabGesture(self, target, scrollGestureType = None):
        '''static Qt.GestureType QScroller.grabGesture(QObject target, QScroller.ScrollerGestureType scrollGestureType = QScroller.TouchGesture)'''
        return Qt.GestureType()
    def scroller(self, target):
        '''static QScroller QScroller.scroller(QObject target)'''
        return QScroller()
    def hasScroller(self, target):
        '''static bool QScroller.hasScroller(QObject target)'''
        return bool()


class QScrollerProperties():
    """"""
    # Enum QScrollerProperties.ScrollMetric
    MousePressEventDelay = 0
    DragStartDistance = 0
    DragVelocitySmoothingFactor = 0
    AxisLockThreshold = 0
    ScrollingCurve = 0
    DecelerationFactor = 0
    MinimumVelocity = 0
    MaximumVelocity = 0
    MaximumClickThroughVelocity = 0
    AcceleratingFlickMaximumTime = 0
    AcceleratingFlickSpeedupFactor = 0
    SnapPositionRatio = 0
    SnapTime = 0
    OvershootDragResistanceFactor = 0
    OvershootDragDistanceFactor = 0
    OvershootScrollDistanceFactor = 0
    OvershootScrollTime = 0
    HorizontalOvershootPolicy = 0
    VerticalOvershootPolicy = 0
    FrameRate = 0
    ScrollMetricCount = 0

    # Enum QScrollerProperties.FrameRates
    Standard = 0
    Fps60 = 0
    Fps30 = 0
    Fps20 = 0

    # Enum QScrollerProperties.OvershootPolicy
    OvershootWhenScrollable = 0
    OvershootAlwaysOff = 0
    OvershootAlwaysOn = 0

    def __init__(self):
        '''void QScrollerProperties.__init__()'''
    def __init__(self, sp):
        '''void QScrollerProperties.__init__(QScrollerProperties sp)'''
    def setScrollMetric(self, metric, value):
        '''void QScrollerProperties.setScrollMetric(QScrollerProperties.ScrollMetric metric, QVariant value)'''
    def scrollMetric(self, metric):
        '''QVariant QScrollerProperties.scrollMetric(QScrollerProperties.ScrollMetric metric)'''
        return QVariant()
    def unsetDefaultScrollerProperties(self):
        '''static void QScrollerProperties.unsetDefaultScrollerProperties()'''
    def setDefaultScrollerProperties(self, sp):
        '''static void QScrollerProperties.setDefaultScrollerProperties(QScrollerProperties sp)'''
    def __ne__(self, sp):
        '''bool QScrollerProperties.__ne__(QScrollerProperties sp)'''
        return bool()
    def __eq__(self, sp):
        '''bool QScrollerProperties.__eq__(QScrollerProperties sp)'''
        return bool()


class QShortcut(QObject):
    """"""
    def __init__(self, parent):
        '''void QShortcut.__init__(QWidget parent)'''
    def __init__(self, key, parent, member = 0, ambiguousMember = 0, context = None):
        '''void QShortcut.__init__(QKeySequence key, QWidget parent, slot member = 0, slot ambiguousMember = 0, Qt.ShortcutContext context = Qt.WindowShortcut)'''
    def event(self, e):
        '''bool QShortcut.event(QEvent e)'''
        return bool()
    activatedAmbiguously = pyqtSignal() # void activatedAmbiguously() - signal
    activated = pyqtSignal() # void activated() - signal
    def autoRepeat(self):
        '''bool QShortcut.autoRepeat()'''
        return bool()
    def setAutoRepeat(self, on):
        '''void QShortcut.setAutoRepeat(bool on)'''
    def parentWidget(self):
        '''QWidget QShortcut.parentWidget()'''
        return QWidget()
    def id(self):
        '''int QShortcut.id()'''
        return int()
    def whatsThis(self):
        '''str QShortcut.whatsThis()'''
        return str()
    def setWhatsThis(self, text):
        '''void QShortcut.setWhatsThis(str text)'''
    def context(self):
        '''Qt.ShortcutContext QShortcut.context()'''
        return Qt.ShortcutContext()
    def setContext(self, context):
        '''void QShortcut.setContext(Qt.ShortcutContext context)'''
    def isEnabled(self):
        '''bool QShortcut.isEnabled()'''
        return bool()
    def setEnabled(self, enable):
        '''void QShortcut.setEnabled(bool enable)'''
    def key(self):
        '''QKeySequence QShortcut.key()'''
        return QKeySequence()
    def setKey(self, key):
        '''void QShortcut.setKey(QKeySequence key)'''


class QSizeGrip(QWidget):
    """"""
    def __init__(self, parent):
        '''void QSizeGrip.__init__(QWidget parent)'''
    def hideEvent(self, hideEvent):
        '''void QSizeGrip.hideEvent(QHideEvent hideEvent)'''
    def showEvent(self, showEvent):
        '''void QSizeGrip.showEvent(QShowEvent showEvent)'''
    def moveEvent(self, moveEvent):
        '''void QSizeGrip.moveEvent(QMoveEvent moveEvent)'''
    def event(self):
        '''QEvent QSizeGrip.event()'''
        return QEvent()
    def eventFilter(self):
        '''QEvent QSizeGrip.eventFilter()'''
        return QEvent()
    def mouseMoveEvent(self):
        '''QMouseEvent QSizeGrip.mouseMoveEvent()'''
        return QMouseEvent()
    def mouseReleaseEvent(self, mouseEvent):
        '''void QSizeGrip.mouseReleaseEvent(QMouseEvent mouseEvent)'''
    def mousePressEvent(self):
        '''QMouseEvent QSizeGrip.mousePressEvent()'''
        return QMouseEvent()
    def paintEvent(self):
        '''QPaintEvent QSizeGrip.paintEvent()'''
        return QPaintEvent()
    def setVisible(self):
        '''bool QSizeGrip.setVisible()'''
        return bool()
    def sizeHint(self):
        '''QSize QSizeGrip.sizeHint()'''
        return QSize()


class QSizePolicy():
    """"""
    # Enum QSizePolicy.ControlType
    DefaultType = 0
    ButtonBox = 0
    CheckBox = 0
    ComboBox = 0
    Frame = 0
    GroupBox = 0
    Label = 0
    Line = 0
    LineEdit = 0
    PushButton = 0
    RadioButton = 0
    Slider = 0
    SpinBox = 0
    TabWidget = 0
    ToolButton = 0

    # Enum QSizePolicy.Policy
    Fixed = 0
    Minimum = 0
    Maximum = 0
    Preferred = 0
    MinimumExpanding = 0
    Expanding = 0
    Ignored = 0

    # Enum QSizePolicy.PolicyFlag
    GrowFlag = 0
    ExpandFlag = 0
    ShrinkFlag = 0
    IgnoreFlag = 0

    def __init__(self):
        '''void QSizePolicy.__init__()'''
    def __init__(self, horizontal, vertical, type = None):
        '''void QSizePolicy.__init__(QSizePolicy.Policy horizontal, QSizePolicy.Policy vertical, QSizePolicy.ControlType type = QSizePolicy.DefaultType)'''
    def __init__(self, variant):
        '''void QSizePolicy.__init__(QVariant variant)'''
    def __init__(self):
        '''QSizePolicy QSizePolicy.__init__()'''
        return QSizePolicy()
    def setRetainSizeWhenHidden(self, retainSize):
        '''void QSizePolicy.setRetainSizeWhenHidden(bool retainSize)'''
    def retainSizeWhenHidden(self):
        '''bool QSizePolicy.retainSizeWhenHidden()'''
        return bool()
    def hasWidthForHeight(self):
        '''bool QSizePolicy.hasWidthForHeight()'''
        return bool()
    def setWidthForHeight(self, b):
        '''void QSizePolicy.setWidthForHeight(bool b)'''
    def setControlType(self, type):
        '''void QSizePolicy.setControlType(QSizePolicy.ControlType type)'''
    def controlType(self):
        '''QSizePolicy.ControlType QSizePolicy.controlType()'''
        return QSizePolicy.ControlType()
    def transpose(self):
        '''void QSizePolicy.transpose()'''
    def setVerticalStretch(self, stretchFactor):
        '''void QSizePolicy.setVerticalStretch(int stretchFactor)'''
    def setHorizontalStretch(self, stretchFactor):
        '''void QSizePolicy.setHorizontalStretch(int stretchFactor)'''
    def verticalStretch(self):
        '''int QSizePolicy.verticalStretch()'''
        return int()
    def horizontalStretch(self):
        '''int QSizePolicy.horizontalStretch()'''
        return int()
    def __ne__(self, s):
        '''bool QSizePolicy.__ne__(QSizePolicy s)'''
        return bool()
    def __eq__(self, s):
        '''bool QSizePolicy.__eq__(QSizePolicy s)'''
        return bool()
    def hasHeightForWidth(self):
        '''bool QSizePolicy.hasHeightForWidth()'''
        return bool()
    def setHeightForWidth(self, b):
        '''void QSizePolicy.setHeightForWidth(bool b)'''
    def expandingDirections(self):
        '''Qt.Orientations QSizePolicy.expandingDirections()'''
        return Qt.Orientations()
    def setVerticalPolicy(self, d):
        '''void QSizePolicy.setVerticalPolicy(QSizePolicy.Policy d)'''
    def setHorizontalPolicy(self, d):
        '''void QSizePolicy.setHorizontalPolicy(QSizePolicy.Policy d)'''
    def verticalPolicy(self):
        '''QSizePolicy.Policy QSizePolicy.verticalPolicy()'''
        return QSizePolicy.Policy()
    def horizontalPolicy(self):
        '''QSizePolicy.Policy QSizePolicy.horizontalPolicy()'''
        return QSizePolicy.Policy()
    class ControlTypes():
        """"""
        def __init__(self):
            '''QSizePolicy.ControlTypes QSizePolicy.ControlTypes.__init__()'''
            return QSizePolicy.ControlTypes()
        def __init__(self):
            '''int QSizePolicy.ControlTypes.__init__()'''
            return int()
        def __init__(self):
            '''void QSizePolicy.ControlTypes.__init__()'''
        def __bool__(self):
            '''int QSizePolicy.ControlTypes.__bool__()'''
            return int()
        def __ne__(self, f):
            '''bool QSizePolicy.ControlTypes.__ne__(QSizePolicy.ControlTypes f)'''
            return bool()
        def __eq__(self, f):
            '''bool QSizePolicy.ControlTypes.__eq__(QSizePolicy.ControlTypes f)'''
            return bool()
        def __invert__(self):
            '''QSizePolicy.ControlTypes QSizePolicy.ControlTypes.__invert__()'''
            return QSizePolicy.ControlTypes()
        def __and__(self, mask):
            '''QSizePolicy.ControlTypes QSizePolicy.ControlTypes.__and__(int mask)'''
            return QSizePolicy.ControlTypes()
        def __xor__(self, f):
            '''QSizePolicy.ControlTypes QSizePolicy.ControlTypes.__xor__(QSizePolicy.ControlTypes f)'''
            return QSizePolicy.ControlTypes()
        def __xor__(self, f):
            '''QSizePolicy.ControlTypes QSizePolicy.ControlTypes.__xor__(int f)'''
            return QSizePolicy.ControlTypes()
        def __or__(self, f):
            '''QSizePolicy.ControlTypes QSizePolicy.ControlTypes.__or__(QSizePolicy.ControlTypes f)'''
            return QSizePolicy.ControlTypes()
        def __or__(self, f):
            '''QSizePolicy.ControlTypes QSizePolicy.ControlTypes.__or__(int f)'''
            return QSizePolicy.ControlTypes()
        def __int__(self):
            '''int QSizePolicy.ControlTypes.__int__()'''
            return int()
        def __ixor__(self, f):
            '''QSizePolicy.ControlTypes QSizePolicy.ControlTypes.__ixor__(QSizePolicy.ControlTypes f)'''
            return QSizePolicy.ControlTypes()
        def __ior__(self, f):
            '''QSizePolicy.ControlTypes QSizePolicy.ControlTypes.__ior__(QSizePolicy.ControlTypes f)'''
            return QSizePolicy.ControlTypes()
        def __iand__(self, mask):
            '''QSizePolicy.ControlTypes QSizePolicy.ControlTypes.__iand__(int mask)'''
            return QSizePolicy.ControlTypes()


class QSlider(QAbstractSlider):
    """"""
    # Enum QSlider.TickPosition
    NoTicks = 0
    TicksAbove = 0
    TicksLeft = 0
    TicksBelow = 0
    TicksRight = 0
    TicksBothSides = 0

    def __init__(self, parent = None):
        '''void QSlider.__init__(QWidget parent = None)'''
    def __init__(self, orientation, parent = None):
        '''void QSlider.__init__(Qt.Orientation orientation, QWidget parent = None)'''
    def mouseMoveEvent(self, ev):
        '''void QSlider.mouseMoveEvent(QMouseEvent ev)'''
    def mouseReleaseEvent(self, ev):
        '''void QSlider.mouseReleaseEvent(QMouseEvent ev)'''
    def mousePressEvent(self, ev):
        '''void QSlider.mousePressEvent(QMouseEvent ev)'''
    def paintEvent(self, ev):
        '''void QSlider.paintEvent(QPaintEvent ev)'''
    def initStyleOption(self, option):
        '''void QSlider.initStyleOption(QStyleOptionSlider option)'''
    def event(self, event):
        '''bool QSlider.event(QEvent event)'''
        return bool()
    def tickInterval(self):
        '''int QSlider.tickInterval()'''
        return int()
    def setTickInterval(self, ti):
        '''void QSlider.setTickInterval(int ti)'''
    def tickPosition(self):
        '''QSlider.TickPosition QSlider.tickPosition()'''
        return QSlider.TickPosition()
    def setTickPosition(self, position):
        '''void QSlider.setTickPosition(QSlider.TickPosition position)'''
    def minimumSizeHint(self):
        '''QSize QSlider.minimumSizeHint()'''
        return QSize()
    def sizeHint(self):
        '''QSize QSlider.sizeHint()'''
        return QSize()


class QSpinBox(QAbstractSpinBox):
    """"""
    def __init__(self, parent = None):
        '''void QSpinBox.__init__(QWidget parent = None)'''
    def setDisplayIntegerBase(self, base):
        '''void QSpinBox.setDisplayIntegerBase(int base)'''
    def displayIntegerBase(self):
        '''int QSpinBox.displayIntegerBase()'''
        return int()
    valueChanged = pyqtSignal() # void valueChanged(int) - signal
    valueChanged = pyqtSignal() # void valueChanged(const QStringamp;) - signal
    def setValue(self, val):
        '''void QSpinBox.setValue(int val)'''
    def event(self, e):
        '''bool QSpinBox.event(QEvent e)'''
        return bool()
    def fixup(self, str):
        '''void QSpinBox.fixup(str str)'''
    def textFromValue(self, v):
        '''str QSpinBox.textFromValue(int v)'''
        return str()
    def valueFromText(self, text):
        '''int QSpinBox.valueFromText(str text)'''
        return int()
    def validate(self, input, pos):
        '''QValidator.State QSpinBox.validate(str input, int pos)'''
        return QValidator.State()
    def setRange(self, min, max):
        '''void QSpinBox.setRange(int min, int max)'''
    def setMaximum(self, max):
        '''void QSpinBox.setMaximum(int max)'''
    def maximum(self):
        '''int QSpinBox.maximum()'''
        return int()
    def setMinimum(self, min):
        '''void QSpinBox.setMinimum(int min)'''
    def minimum(self):
        '''int QSpinBox.minimum()'''
        return int()
    def setSingleStep(self, val):
        '''void QSpinBox.setSingleStep(int val)'''
    def singleStep(self):
        '''int QSpinBox.singleStep()'''
        return int()
    def cleanText(self):
        '''str QSpinBox.cleanText()'''
        return str()
    def setSuffix(self, s):
        '''void QSpinBox.setSuffix(str s)'''
    def suffix(self):
        '''str QSpinBox.suffix()'''
        return str()
    def setPrefix(self, p):
        '''void QSpinBox.setPrefix(str p)'''
    def prefix(self):
        '''str QSpinBox.prefix()'''
        return str()
    def value(self):
        '''int QSpinBox.value()'''
        return int()


class QDoubleSpinBox(QAbstractSpinBox):
    """"""
    def __init__(self, parent = None):
        '''void QDoubleSpinBox.__init__(QWidget parent = None)'''
    valueChanged = pyqtSignal() # void valueChanged(double) - signal
    valueChanged = pyqtSignal() # void valueChanged(const QStringamp;) - signal
    def setValue(self, val):
        '''void QDoubleSpinBox.setValue(float val)'''
    def fixup(self, str):
        '''void QDoubleSpinBox.fixup(str str)'''
    def textFromValue(self, v):
        '''str QDoubleSpinBox.textFromValue(float v)'''
        return str()
    def valueFromText(self, text):
        '''float QDoubleSpinBox.valueFromText(str text)'''
        return float()
    def validate(self, input, pos):
        '''QValidator.State QDoubleSpinBox.validate(str input, int pos)'''
        return QValidator.State()
    def setDecimals(self, prec):
        '''void QDoubleSpinBox.setDecimals(int prec)'''
    def decimals(self):
        '''int QDoubleSpinBox.decimals()'''
        return int()
    def setRange(self, min, max):
        '''void QDoubleSpinBox.setRange(float min, float max)'''
    def setMaximum(self, max):
        '''void QDoubleSpinBox.setMaximum(float max)'''
    def maximum(self):
        '''float QDoubleSpinBox.maximum()'''
        return float()
    def setMinimum(self, min):
        '''void QDoubleSpinBox.setMinimum(float min)'''
    def minimum(self):
        '''float QDoubleSpinBox.minimum()'''
        return float()
    def setSingleStep(self, val):
        '''void QDoubleSpinBox.setSingleStep(float val)'''
    def singleStep(self):
        '''float QDoubleSpinBox.singleStep()'''
        return float()
    def cleanText(self):
        '''str QDoubleSpinBox.cleanText()'''
        return str()
    def setSuffix(self, s):
        '''void QDoubleSpinBox.setSuffix(str s)'''
    def suffix(self):
        '''str QDoubleSpinBox.suffix()'''
        return str()
    def setPrefix(self, p):
        '''void QDoubleSpinBox.setPrefix(str p)'''
    def prefix(self):
        '''str QDoubleSpinBox.prefix()'''
        return str()
    def value(self):
        '''float QDoubleSpinBox.value()'''
        return float()


class QSplashScreen(QWidget):
    """"""
    def __init__(self, pixmap = QPixmap(), flags = 0):
        '''void QSplashScreen.__init__(QPixmap pixmap = QPixmap(), Qt.WindowFlags flags = 0)'''
    def __init__(self, parent, pixmap = QPixmap(), flags = 0):
        '''void QSplashScreen.__init__(QWidget parent, QPixmap pixmap = QPixmap(), Qt.WindowFlags flags = 0)'''
    def mousePressEvent(self):
        '''QMouseEvent QSplashScreen.mousePressEvent()'''
        return QMouseEvent()
    def event(self, e):
        '''bool QSplashScreen.event(QEvent e)'''
        return bool()
    def drawContents(self, painter):
        '''void QSplashScreen.drawContents(QPainter painter)'''
    messageChanged = pyqtSignal() # void messageChanged(const QStringamp;) - signal
    def clearMessage(self):
        '''void QSplashScreen.clearMessage()'''
    def showMessage(self, message, alignment = None, color = None):
        '''void QSplashScreen.showMessage(str message, int alignment = Qt.AlignLeft, QColor color = Qt.black)'''
    def message(self):
        '''str QSplashScreen.message()'''
        return str()
    def repaint(self):
        '''void QSplashScreen.repaint()'''
    def finish(self, w):
        '''void QSplashScreen.finish(QWidget w)'''
    def pixmap(self):
        '''QPixmap QSplashScreen.pixmap()'''
        return QPixmap()
    def setPixmap(self, pixmap):
        '''void QSplashScreen.setPixmap(QPixmap pixmap)'''


class QSplitter(QFrame):
    """"""
    def __init__(self, parent = None):
        '''void QSplitter.__init__(QWidget parent = None)'''
    def __init__(self, orientation, parent = None):
        '''void QSplitter.__init__(Qt.Orientation orientation, QWidget parent = None)'''
    def closestLegalPosition(self):
        '''int QSplitter.closestLegalPosition()'''
        return int()
    def setRubberBand(self, position):
        '''void QSplitter.setRubberBand(int position)'''
    def moveSplitter(self, pos, index):
        '''void QSplitter.moveSplitter(int pos, int index)'''
    def changeEvent(self):
        '''QEvent QSplitter.changeEvent()'''
        return QEvent()
    def resizeEvent(self):
        '''QResizeEvent QSplitter.resizeEvent()'''
        return QResizeEvent()
    def event(self):
        '''QEvent QSplitter.event()'''
        return QEvent()
    def childEvent(self):
        '''QChildEvent QSplitter.childEvent()'''
        return QChildEvent()
    def createHandle(self):
        '''QSplitterHandle QSplitter.createHandle()'''
        return QSplitterHandle()
    splitterMoved = pyqtSignal() # void splitterMoved(int,int) - signal
    def setStretchFactor(self, index, stretch):
        '''void QSplitter.setStretchFactor(int index, int stretch)'''
    def handle(self, index):
        '''QSplitterHandle QSplitter.handle(int index)'''
        return QSplitterHandle()
    def getRange(self, index):
        '''int QSplitter.getRange(int index)'''
        return int()
    def __len__(self):
        ''' QSplitter.__len__()'''
        return ()
    def count(self):
        '''int QSplitter.count()'''
        return int()
    def widget(self, index):
        '''QWidget QSplitter.widget(int index)'''
        return QWidget()
    def indexOf(self, w):
        '''int QSplitter.indexOf(QWidget w)'''
        return int()
    def setHandleWidth(self):
        '''int QSplitter.setHandleWidth()'''
        return int()
    def handleWidth(self):
        '''int QSplitter.handleWidth()'''
        return int()
    def restoreState(self, state):
        '''bool QSplitter.restoreState(QByteArray state)'''
        return bool()
    def saveState(self):
        '''QByteArray QSplitter.saveState()'''
        return QByteArray()
    def setSizes(self, list):
        '''void QSplitter.setSizes(list-of-int list)'''
    def sizes(self):
        '''list-of-int QSplitter.sizes()'''
        return [int()]
    def minimumSizeHint(self):
        '''QSize QSplitter.minimumSizeHint()'''
        return QSize()
    def sizeHint(self):
        '''QSize QSplitter.sizeHint()'''
        return QSize()
    def refresh(self):
        '''void QSplitter.refresh()'''
    def opaqueResize(self):
        '''bool QSplitter.opaqueResize()'''
        return bool()
    def setOpaqueResize(self, opaque = True):
        '''void QSplitter.setOpaqueResize(bool opaque = True)'''
    def isCollapsible(self, index):
        '''bool QSplitter.isCollapsible(int index)'''
        return bool()
    def setCollapsible(self, index):
        '''bool QSplitter.setCollapsible(int index)'''
        return bool()
    def childrenCollapsible(self):
        '''bool QSplitter.childrenCollapsible()'''
        return bool()
    def setChildrenCollapsible(self):
        '''bool QSplitter.setChildrenCollapsible()'''
        return bool()
    def orientation(self):
        '''Qt.Orientation QSplitter.orientation()'''
        return Qt.Orientation()
    def setOrientation(self):
        '''Qt.Orientation QSplitter.setOrientation()'''
        return Qt.Orientation()
    def insertWidget(self, index, widget):
        '''void QSplitter.insertWidget(int index, QWidget widget)'''
    def addWidget(self, widget):
        '''void QSplitter.addWidget(QWidget widget)'''


class QSplitterHandle(QWidget):
    """"""
    def __init__(self, o, parent):
        '''void QSplitterHandle.__init__(Qt.Orientation o, QSplitter parent)'''
    def resizeEvent(self):
        '''QResizeEvent QSplitterHandle.resizeEvent()'''
        return QResizeEvent()
    def closestLegalPosition(self, p):
        '''int QSplitterHandle.closestLegalPosition(int p)'''
        return int()
    def moveSplitter(self, p):
        '''void QSplitterHandle.moveSplitter(int p)'''
    def event(self):
        '''QEvent QSplitterHandle.event()'''
        return QEvent()
    def mouseReleaseEvent(self):
        '''QMouseEvent QSplitterHandle.mouseReleaseEvent()'''
        return QMouseEvent()
    def mousePressEvent(self):
        '''QMouseEvent QSplitterHandle.mousePressEvent()'''
        return QMouseEvent()
    def mouseMoveEvent(self):
        '''QMouseEvent QSplitterHandle.mouseMoveEvent()'''
        return QMouseEvent()
    def paintEvent(self):
        '''QPaintEvent QSplitterHandle.paintEvent()'''
        return QPaintEvent()
    def sizeHint(self):
        '''QSize QSplitterHandle.sizeHint()'''
        return QSize()
    def splitter(self):
        '''QSplitter QSplitterHandle.splitter()'''
        return QSplitter()
    def opaqueResize(self):
        '''bool QSplitterHandle.opaqueResize()'''
        return bool()
    def orientation(self):
        '''Qt.Orientation QSplitterHandle.orientation()'''
        return Qt.Orientation()
    def setOrientation(self, o):
        '''void QSplitterHandle.setOrientation(Qt.Orientation o)'''


class QStackedLayout(QLayout):
    """"""
    # Enum QStackedLayout.StackingMode
    StackOne = 0
    StackAll = 0

    def __init__(self):
        '''void QStackedLayout.__init__()'''
    def __init__(self, parent):
        '''void QStackedLayout.__init__(QWidget parent)'''
    def __init__(self, parentLayout):
        '''void QStackedLayout.__init__(QLayout parentLayout)'''
    def heightForWidth(self, width):
        '''int QStackedLayout.heightForWidth(int width)'''
        return int()
    def hasHeightForWidth(self):
        '''bool QStackedLayout.hasHeightForWidth()'''
        return bool()
    def setStackingMode(self, stackingMode):
        '''void QStackedLayout.setStackingMode(QStackedLayout.StackingMode stackingMode)'''
    def stackingMode(self):
        '''QStackedLayout.StackingMode QStackedLayout.stackingMode()'''
        return QStackedLayout.StackingMode()
    def setCurrentWidget(self, w):
        '''void QStackedLayout.setCurrentWidget(QWidget w)'''
    def setCurrentIndex(self, index):
        '''void QStackedLayout.setCurrentIndex(int index)'''
    currentChanged = pyqtSignal() # void currentChanged(int) - signal
    widgetRemoved = pyqtSignal() # void widgetRemoved(int) - signal
    def setGeometry(self, rect):
        '''void QStackedLayout.setGeometry(QRect rect)'''
    def takeAt(self):
        '''int QStackedLayout.takeAt()'''
        return int()
    def itemAt(self):
        '''int QStackedLayout.itemAt()'''
        return int()
    def minimumSize(self):
        '''QSize QStackedLayout.minimumSize()'''
        return QSize()
    def sizeHint(self):
        '''QSize QStackedLayout.sizeHint()'''
        return QSize()
    def addItem(self, item):
        '''void QStackedLayout.addItem(QLayoutItem item)'''
    def count(self):
        '''int QStackedLayout.count()'''
        return int()
    def widget(self):
        '''int QStackedLayout.widget()'''
        return int()
    def widget(self):
        '''QWidget QStackedLayout.widget()'''
        return QWidget()
    def currentIndex(self):
        '''int QStackedLayout.currentIndex()'''
        return int()
    def currentWidget(self):
        '''QWidget QStackedLayout.currentWidget()'''
        return QWidget()
    def insertWidget(self, index, w):
        '''int QStackedLayout.insertWidget(int index, QWidget w)'''
        return int()
    def addWidget(self, w):
        '''int QStackedLayout.addWidget(QWidget w)'''
        return int()


class QStackedWidget(QFrame):
    """"""
    def __init__(self, parent = None):
        '''void QStackedWidget.__init__(QWidget parent = None)'''
    def event(self, e):
        '''bool QStackedWidget.event(QEvent e)'''
        return bool()
    widgetRemoved = pyqtSignal() # void widgetRemoved(int) - signal
    currentChanged = pyqtSignal() # void currentChanged(int) - signal
    def setCurrentWidget(self, w):
        '''void QStackedWidget.setCurrentWidget(QWidget w)'''
    def setCurrentIndex(self, index):
        '''void QStackedWidget.setCurrentIndex(int index)'''
    def __len__(self):
        ''' QStackedWidget.__len__()'''
        return ()
    def count(self):
        '''int QStackedWidget.count()'''
        return int()
    def widget(self):
        '''int QStackedWidget.widget()'''
        return int()
    def indexOf(self):
        '''QWidget QStackedWidget.indexOf()'''
        return QWidget()
    def currentIndex(self):
        '''int QStackedWidget.currentIndex()'''
        return int()
    def currentWidget(self):
        '''QWidget QStackedWidget.currentWidget()'''
        return QWidget()
    def removeWidget(self, w):
        '''void QStackedWidget.removeWidget(QWidget w)'''
    def insertWidget(self, index, w):
        '''int QStackedWidget.insertWidget(int index, QWidget w)'''
        return int()
    def addWidget(self, w):
        '''int QStackedWidget.addWidget(QWidget w)'''
        return int()


class QStatusBar(QWidget):
    """"""
    def __init__(self, parent = None):
        '''void QStatusBar.__init__(QWidget parent = None)'''
    def showEvent(self):
        '''QShowEvent QStatusBar.showEvent()'''
        return QShowEvent()
    def event(self):
        '''QEvent QStatusBar.event()'''
        return QEvent()
    def hideOrShow(self):
        '''void QStatusBar.hideOrShow()'''
    def reformat(self):
        '''void QStatusBar.reformat()'''
    def resizeEvent(self):
        '''QResizeEvent QStatusBar.resizeEvent()'''
        return QResizeEvent()
    def paintEvent(self):
        '''QPaintEvent QStatusBar.paintEvent()'''
        return QPaintEvent()
    messageChanged = pyqtSignal() # void messageChanged(const QStringamp;) - signal
    def clearMessage(self):
        '''void QStatusBar.clearMessage()'''
    def showMessage(self, message, msecs = 0):
        '''void QStatusBar.showMessage(str message, int msecs = 0)'''
    def insertPermanentWidget(self, index, widget, stretch = 0):
        '''int QStatusBar.insertPermanentWidget(int index, QWidget widget, int stretch = 0)'''
        return int()
    def insertWidget(self, index, widget, stretch = 0):
        '''int QStatusBar.insertWidget(int index, QWidget widget, int stretch = 0)'''
        return int()
    def currentMessage(self):
        '''str QStatusBar.currentMessage()'''
        return str()
    def isSizeGripEnabled(self):
        '''bool QStatusBar.isSizeGripEnabled()'''
        return bool()
    def setSizeGripEnabled(self):
        '''bool QStatusBar.setSizeGripEnabled()'''
        return bool()
    def removeWidget(self, widget):
        '''void QStatusBar.removeWidget(QWidget widget)'''
    def addPermanentWidget(self, widget, stretch = 0):
        '''void QStatusBar.addPermanentWidget(QWidget widget, int stretch = 0)'''
    def addWidget(self, widget, stretch = 0):
        '''void QStatusBar.addWidget(QWidget widget, int stretch = 0)'''


class QStyledItemDelegate(QAbstractItemDelegate):
    """"""
    def __init__(self, parent = None):
        '''void QStyledItemDelegate.__init__(QObject parent = None)'''
    def editorEvent(self, event, model, option, index):
        '''bool QStyledItemDelegate.editorEvent(QEvent event, QAbstractItemModel model, QStyleOptionViewItem option, QModelIndex index)'''
        return bool()
    def eventFilter(self, object, event):
        '''bool QStyledItemDelegate.eventFilter(QObject object, QEvent event)'''
        return bool()
    def initStyleOption(self, option, index):
        '''void QStyledItemDelegate.initStyleOption(QStyleOptionViewItem option, QModelIndex index)'''
    def displayText(self, value, locale):
        '''str QStyledItemDelegate.displayText(QVariant value, QLocale locale)'''
        return str()
    def setItemEditorFactory(self, factory):
        '''void QStyledItemDelegate.setItemEditorFactory(QItemEditorFactory factory)'''
    def itemEditorFactory(self):
        '''QItemEditorFactory QStyledItemDelegate.itemEditorFactory()'''
        return QItemEditorFactory()
    def updateEditorGeometry(self, editor, option, index):
        '''void QStyledItemDelegate.updateEditorGeometry(QWidget editor, QStyleOptionViewItem option, QModelIndex index)'''
    def setModelData(self, editor, model, index):
        '''void QStyledItemDelegate.setModelData(QWidget editor, QAbstractItemModel model, QModelIndex index)'''
    def setEditorData(self, editor, index):
        '''void QStyledItemDelegate.setEditorData(QWidget editor, QModelIndex index)'''
    def createEditor(self, parent, option, index):
        '''QWidget QStyledItemDelegate.createEditor(QWidget parent, QStyleOptionViewItem option, QModelIndex index)'''
        return QWidget()
    def sizeHint(self, option, index):
        '''QSize QStyledItemDelegate.sizeHint(QStyleOptionViewItem option, QModelIndex index)'''
        return QSize()
    def paint(self, painter, option, index):
        '''void QStyledItemDelegate.paint(QPainter painter, QStyleOptionViewItem option, QModelIndex index)'''


class QStyleFactory():
    """"""
    def __init__(self):
        '''void QStyleFactory.__init__()'''
    def __init__(self):
        '''QStyleFactory QStyleFactory.__init__()'''
        return QStyleFactory()
    def create(self):
        '''static str QStyleFactory.create()'''
        return str()
    def keys(self):
        '''static list-of-str QStyleFactory.keys()'''
        return [str()]


class QStyleOption():
    """"""
    # Enum QStyleOption.StyleOptionVersion
    Version = 0

    # Enum QStyleOption.StyleOptionType
    Type = 0

    # Enum QStyleOption.OptionType
    SO_Default = 0
    SO_FocusRect = 0
    SO_Button = 0
    SO_Tab = 0
    SO_MenuItem = 0
    SO_Frame = 0
    SO_ProgressBar = 0
    SO_ToolBox = 0
    SO_Header = 0
    SO_DockWidget = 0
    SO_ViewItem = 0
    SO_TabWidgetFrame = 0
    SO_TabBarBase = 0
    SO_RubberBand = 0
    SO_ToolBar = 0
    SO_Complex = 0
    SO_Slider = 0
    SO_SpinBox = 0
    SO_ToolButton = 0
    SO_ComboBox = 0
    SO_TitleBar = 0
    SO_GroupBox = 0
    SO_ComplexCustomBase = 0
    SO_GraphicsItem = 0
    SO_SizeGrip = 0
    SO_CustomBase = 0

    direction = None # Qt.LayoutDirection - member
    fontMetrics = None # QFontMetrics - member
    palette = None # QPalette - member
    rect = None # QRect - member
    state = None # QStyle.State - member
    styleObject = None # QObject - member
    type = None # int - member
    version = None # int - member
    def __init__(self, version = None, type = None):
        '''void QStyleOption.__init__(int version = QStyleOption.Version, int type = QStyleOption.SO_Default)'''
    def __init__(self, other):
        '''void QStyleOption.__init__(QStyleOption other)'''
    def initFrom(self, w):
        '''void QStyleOption.initFrom(QWidget w)'''


class QStyleOptionFocusRect(QStyleOption):
    """"""
    # Enum QStyleOptionFocusRect.StyleOptionVersion
    Version = 0

    # Enum QStyleOptionFocusRect.StyleOptionType
    Type = 0

    backgroundColor = None # QColor - member
    def __init__(self):
        '''void QStyleOptionFocusRect.__init__()'''
    def __init__(self, other):
        '''void QStyleOptionFocusRect.__init__(QStyleOptionFocusRect other)'''


class QStyleOptionFrame(QStyleOption):
    """"""
    # Enum QStyleOptionFrame.FrameFeature
    __kdevpythondocumentation_builtin_None = 0
    Flat = 0
    Rounded = 0

    # Enum QStyleOptionFrame.StyleOptionVersion
    Version = 0

    # Enum QStyleOptionFrame.StyleOptionType
    Type = 0

    features = None # QStyleOptionFrame.FrameFeatures - member
    frameShape = None # QFrame.Shape - member
    lineWidth = None # int - member
    midLineWidth = None # int - member
    def __init__(self):
        '''void QStyleOptionFrame.__init__()'''
    def __init__(self, other):
        '''void QStyleOptionFrame.__init__(QStyleOptionFrame other)'''
    class FrameFeatures():
        """"""
        def __init__(self):
            '''QStyleOptionFrame.FrameFeatures QStyleOptionFrame.FrameFeatures.__init__()'''
            return QStyleOptionFrame.FrameFeatures()
        def __init__(self):
            '''int QStyleOptionFrame.FrameFeatures.__init__()'''
            return int()
        def __init__(self):
            '''void QStyleOptionFrame.FrameFeatures.__init__()'''
        def __bool__(self):
            '''int QStyleOptionFrame.FrameFeatures.__bool__()'''
            return int()
        def __ne__(self, f):
            '''bool QStyleOptionFrame.FrameFeatures.__ne__(QStyleOptionFrame.FrameFeatures f)'''
            return bool()
        def __eq__(self, f):
            '''bool QStyleOptionFrame.FrameFeatures.__eq__(QStyleOptionFrame.FrameFeatures f)'''
            return bool()
        def __invert__(self):
            '''QStyleOptionFrame.FrameFeatures QStyleOptionFrame.FrameFeatures.__invert__()'''
            return QStyleOptionFrame.FrameFeatures()
        def __and__(self, mask):
            '''QStyleOptionFrame.FrameFeatures QStyleOptionFrame.FrameFeatures.__and__(int mask)'''
            return QStyleOptionFrame.FrameFeatures()
        def __xor__(self, f):
            '''QStyleOptionFrame.FrameFeatures QStyleOptionFrame.FrameFeatures.__xor__(QStyleOptionFrame.FrameFeatures f)'''
            return QStyleOptionFrame.FrameFeatures()
        def __xor__(self, f):
            '''QStyleOptionFrame.FrameFeatures QStyleOptionFrame.FrameFeatures.__xor__(int f)'''
            return QStyleOptionFrame.FrameFeatures()
        def __or__(self, f):
            '''QStyleOptionFrame.FrameFeatures QStyleOptionFrame.FrameFeatures.__or__(QStyleOptionFrame.FrameFeatures f)'''
            return QStyleOptionFrame.FrameFeatures()
        def __or__(self, f):
            '''QStyleOptionFrame.FrameFeatures QStyleOptionFrame.FrameFeatures.__or__(int f)'''
            return QStyleOptionFrame.FrameFeatures()
        def __int__(self):
            '''int QStyleOptionFrame.FrameFeatures.__int__()'''
            return int()
        def __ixor__(self, f):
            '''QStyleOptionFrame.FrameFeatures QStyleOptionFrame.FrameFeatures.__ixor__(QStyleOptionFrame.FrameFeatures f)'''
            return QStyleOptionFrame.FrameFeatures()
        def __ior__(self, f):
            '''QStyleOptionFrame.FrameFeatures QStyleOptionFrame.FrameFeatures.__ior__(QStyleOptionFrame.FrameFeatures f)'''
            return QStyleOptionFrame.FrameFeatures()
        def __iand__(self, mask):
            '''QStyleOptionFrame.FrameFeatures QStyleOptionFrame.FrameFeatures.__iand__(int mask)'''
            return QStyleOptionFrame.FrameFeatures()


class QStyleOptionTabWidgetFrame(QStyleOption):
    """"""
    # Enum QStyleOptionTabWidgetFrame.StyleOptionVersion
    Version = 0

    # Enum QStyleOptionTabWidgetFrame.StyleOptionType
    Type = 0

    leftCornerWidgetSize = None # QSize - member
    lineWidth = None # int - member
    midLineWidth = None # int - member
    rightCornerWidgetSize = None # QSize - member
    selectedTabRect = None # QRect - member
    shape = None # QTabBar.Shape - member
    tabBarRect = None # QRect - member
    tabBarSize = None # QSize - member
    def __init__(self):
        '''void QStyleOptionTabWidgetFrame.__init__()'''
    def __init__(self, other):
        '''void QStyleOptionTabWidgetFrame.__init__(QStyleOptionTabWidgetFrame other)'''


class QStyleOptionTabBarBase(QStyleOption):
    """"""
    # Enum QStyleOptionTabBarBase.StyleOptionVersion
    Version = 0

    # Enum QStyleOptionTabBarBase.StyleOptionType
    Type = 0

    documentMode = None # bool - member
    selectedTabRect = None # QRect - member
    shape = None # QTabBar.Shape - member
    tabBarRect = None # QRect - member
    def __init__(self):
        '''void QStyleOptionTabBarBase.__init__()'''
    def __init__(self, other):
        '''void QStyleOptionTabBarBase.__init__(QStyleOptionTabBarBase other)'''


class QStyleOptionHeader(QStyleOption):
    """"""
    # Enum QStyleOptionHeader.SortIndicator
    __kdevpythondocumentation_builtin_None = 0
    SortUp = 0
    SortDown = 0

    # Enum QStyleOptionHeader.SelectedPosition
    NotAdjacent = 0
    NextIsSelected = 0
    PreviousIsSelected = 0
    NextAndPreviousAreSelected = 0

    # Enum QStyleOptionHeader.SectionPosition
    Beginning = 0
    Middle = 0
    End = 0
    OnlyOneSection = 0

    # Enum QStyleOptionHeader.StyleOptionVersion
    Version = 0

    # Enum QStyleOptionHeader.StyleOptionType
    Type = 0

    icon = None # QIcon - member
    iconAlignment = None # Qt.Alignment - member
    orientation = None # Qt.Orientation - member
    position = None # QStyleOptionHeader.SectionPosition - member
    section = None # int - member
    selectedPosition = None # QStyleOptionHeader.SelectedPosition - member
    sortIndicator = None # QStyleOptionHeader.SortIndicator - member
    text = None # str - member
    textAlignment = None # Qt.Alignment - member
    def __init__(self):
        '''void QStyleOptionHeader.__init__()'''
    def __init__(self, other):
        '''void QStyleOptionHeader.__init__(QStyleOptionHeader other)'''


class QStyleOptionButton(QStyleOption):
    """"""
    # Enum QStyleOptionButton.ButtonFeature
    __kdevpythondocumentation_builtin_None = 0
    Flat = 0
    HasMenu = 0
    DefaultButton = 0
    AutoDefaultButton = 0
    CommandLinkButton = 0

    # Enum QStyleOptionButton.StyleOptionVersion
    Version = 0

    # Enum QStyleOptionButton.StyleOptionType
    Type = 0

    features = None # QStyleOptionButton.ButtonFeatures - member
    icon = None # QIcon - member
    iconSize = None # QSize - member
    text = None # str - member
    def __init__(self):
        '''void QStyleOptionButton.__init__()'''
    def __init__(self, other):
        '''void QStyleOptionButton.__init__(QStyleOptionButton other)'''
    class ButtonFeatures():
        """"""
        def __init__(self):
            '''QStyleOptionButton.ButtonFeatures QStyleOptionButton.ButtonFeatures.__init__()'''
            return QStyleOptionButton.ButtonFeatures()
        def __init__(self):
            '''int QStyleOptionButton.ButtonFeatures.__init__()'''
            return int()
        def __init__(self):
            '''void QStyleOptionButton.ButtonFeatures.__init__()'''
        def __bool__(self):
            '''int QStyleOptionButton.ButtonFeatures.__bool__()'''
            return int()
        def __ne__(self, f):
            '''bool QStyleOptionButton.ButtonFeatures.__ne__(QStyleOptionButton.ButtonFeatures f)'''
            return bool()
        def __eq__(self, f):
            '''bool QStyleOptionButton.ButtonFeatures.__eq__(QStyleOptionButton.ButtonFeatures f)'''
            return bool()
        def __invert__(self):
            '''QStyleOptionButton.ButtonFeatures QStyleOptionButton.ButtonFeatures.__invert__()'''
            return QStyleOptionButton.ButtonFeatures()
        def __and__(self, mask):
            '''QStyleOptionButton.ButtonFeatures QStyleOptionButton.ButtonFeatures.__and__(int mask)'''
            return QStyleOptionButton.ButtonFeatures()
        def __xor__(self, f):
            '''QStyleOptionButton.ButtonFeatures QStyleOptionButton.ButtonFeatures.__xor__(QStyleOptionButton.ButtonFeatures f)'''
            return QStyleOptionButton.ButtonFeatures()
        def __xor__(self, f):
            '''QStyleOptionButton.ButtonFeatures QStyleOptionButton.ButtonFeatures.__xor__(int f)'''
            return QStyleOptionButton.ButtonFeatures()
        def __or__(self, f):
            '''QStyleOptionButton.ButtonFeatures QStyleOptionButton.ButtonFeatures.__or__(QStyleOptionButton.ButtonFeatures f)'''
            return QStyleOptionButton.ButtonFeatures()
        def __or__(self, f):
            '''QStyleOptionButton.ButtonFeatures QStyleOptionButton.ButtonFeatures.__or__(int f)'''
            return QStyleOptionButton.ButtonFeatures()
        def __int__(self):
            '''int QStyleOptionButton.ButtonFeatures.__int__()'''
            return int()
        def __ixor__(self, f):
            '''QStyleOptionButton.ButtonFeatures QStyleOptionButton.ButtonFeatures.__ixor__(QStyleOptionButton.ButtonFeatures f)'''
            return QStyleOptionButton.ButtonFeatures()
        def __ior__(self, f):
            '''QStyleOptionButton.ButtonFeatures QStyleOptionButton.ButtonFeatures.__ior__(QStyleOptionButton.ButtonFeatures f)'''
            return QStyleOptionButton.ButtonFeatures()
        def __iand__(self, mask):
            '''QStyleOptionButton.ButtonFeatures QStyleOptionButton.ButtonFeatures.__iand__(int mask)'''
            return QStyleOptionButton.ButtonFeatures()


class QStyleOptionTab(QStyleOption):
    """"""
    # Enum QStyleOptionTab.TabFeature
    __kdevpythondocumentation_builtin_None = 0
    HasFrame = 0

    # Enum QStyleOptionTab.CornerWidget
    NoCornerWidgets = 0
    LeftCornerWidget = 0
    RightCornerWidget = 0

    # Enum QStyleOptionTab.SelectedPosition
    NotAdjacent = 0
    NextIsSelected = 0
    PreviousIsSelected = 0

    # Enum QStyleOptionTab.TabPosition
    Beginning = 0
    Middle = 0
    End = 0
    OnlyOneTab = 0

    # Enum QStyleOptionTab.StyleOptionVersion
    Version = 0

    # Enum QStyleOptionTab.StyleOptionType
    Type = 0

    cornerWidgets = None # QStyleOptionTab.CornerWidgets - member
    documentMode = None # bool - member
    features = None # QStyleOptionTab.TabFeatures - member
    icon = None # QIcon - member
    iconSize = None # QSize - member
    leftButtonSize = None # QSize - member
    position = None # QStyleOptionTab.TabPosition - member
    rightButtonSize = None # QSize - member
    row = None # int - member
    selectedPosition = None # QStyleOptionTab.SelectedPosition - member
    shape = None # QTabBar.Shape - member
    text = None # str - member
    def __init__(self):
        '''void QStyleOptionTab.__init__()'''
    def __init__(self, other):
        '''void QStyleOptionTab.__init__(QStyleOptionTab other)'''
    class CornerWidgets():
        """"""
        def __init__(self):
            '''QStyleOptionTab.CornerWidgets QStyleOptionTab.CornerWidgets.__init__()'''
            return QStyleOptionTab.CornerWidgets()
        def __init__(self):
            '''int QStyleOptionTab.CornerWidgets.__init__()'''
            return int()
        def __init__(self):
            '''void QStyleOptionTab.CornerWidgets.__init__()'''
        def __bool__(self):
            '''int QStyleOptionTab.CornerWidgets.__bool__()'''
            return int()
        def __ne__(self, f):
            '''bool QStyleOptionTab.CornerWidgets.__ne__(QStyleOptionTab.CornerWidgets f)'''
            return bool()
        def __eq__(self, f):
            '''bool QStyleOptionTab.CornerWidgets.__eq__(QStyleOptionTab.CornerWidgets f)'''
            return bool()
        def __invert__(self):
            '''QStyleOptionTab.CornerWidgets QStyleOptionTab.CornerWidgets.__invert__()'''
            return QStyleOptionTab.CornerWidgets()
        def __and__(self, mask):
            '''QStyleOptionTab.CornerWidgets QStyleOptionTab.CornerWidgets.__and__(int mask)'''
            return QStyleOptionTab.CornerWidgets()
        def __xor__(self, f):
            '''QStyleOptionTab.CornerWidgets QStyleOptionTab.CornerWidgets.__xor__(QStyleOptionTab.CornerWidgets f)'''
            return QStyleOptionTab.CornerWidgets()
        def __xor__(self, f):
            '''QStyleOptionTab.CornerWidgets QStyleOptionTab.CornerWidgets.__xor__(int f)'''
            return QStyleOptionTab.CornerWidgets()
        def __or__(self, f):
            '''QStyleOptionTab.CornerWidgets QStyleOptionTab.CornerWidgets.__or__(QStyleOptionTab.CornerWidgets f)'''
            return QStyleOptionTab.CornerWidgets()
        def __or__(self, f):
            '''QStyleOptionTab.CornerWidgets QStyleOptionTab.CornerWidgets.__or__(int f)'''
            return QStyleOptionTab.CornerWidgets()
        def __int__(self):
            '''int QStyleOptionTab.CornerWidgets.__int__()'''
            return int()
        def __ixor__(self, f):
            '''QStyleOptionTab.CornerWidgets QStyleOptionTab.CornerWidgets.__ixor__(QStyleOptionTab.CornerWidgets f)'''
            return QStyleOptionTab.CornerWidgets()
        def __ior__(self, f):
            '''QStyleOptionTab.CornerWidgets QStyleOptionTab.CornerWidgets.__ior__(QStyleOptionTab.CornerWidgets f)'''
            return QStyleOptionTab.CornerWidgets()
        def __iand__(self, mask):
            '''QStyleOptionTab.CornerWidgets QStyleOptionTab.CornerWidgets.__iand__(int mask)'''
            return QStyleOptionTab.CornerWidgets()
    class TabFeatures():
        """"""
        def __init__(self):
            '''QStyleOptionTab.TabFeatures QStyleOptionTab.TabFeatures.__init__()'''
            return QStyleOptionTab.TabFeatures()
        def __init__(self):
            '''int QStyleOptionTab.TabFeatures.__init__()'''
            return int()
        def __init__(self):
            '''void QStyleOptionTab.TabFeatures.__init__()'''
        def __bool__(self):
            '''int QStyleOptionTab.TabFeatures.__bool__()'''
            return int()
        def __ne__(self, f):
            '''bool QStyleOptionTab.TabFeatures.__ne__(QStyleOptionTab.TabFeatures f)'''
            return bool()
        def __eq__(self, f):
            '''bool QStyleOptionTab.TabFeatures.__eq__(QStyleOptionTab.TabFeatures f)'''
            return bool()
        def __invert__(self):
            '''QStyleOptionTab.TabFeatures QStyleOptionTab.TabFeatures.__invert__()'''
            return QStyleOptionTab.TabFeatures()
        def __and__(self, mask):
            '''QStyleOptionTab.TabFeatures QStyleOptionTab.TabFeatures.__and__(int mask)'''
            return QStyleOptionTab.TabFeatures()
        def __xor__(self, f):
            '''QStyleOptionTab.TabFeatures QStyleOptionTab.TabFeatures.__xor__(QStyleOptionTab.TabFeatures f)'''
            return QStyleOptionTab.TabFeatures()
        def __xor__(self, f):
            '''QStyleOptionTab.TabFeatures QStyleOptionTab.TabFeatures.__xor__(int f)'''
            return QStyleOptionTab.TabFeatures()
        def __or__(self, f):
            '''QStyleOptionTab.TabFeatures QStyleOptionTab.TabFeatures.__or__(QStyleOptionTab.TabFeatures f)'''
            return QStyleOptionTab.TabFeatures()
        def __or__(self, f):
            '''QStyleOptionTab.TabFeatures QStyleOptionTab.TabFeatures.__or__(int f)'''
            return QStyleOptionTab.TabFeatures()
        def __int__(self):
            '''int QStyleOptionTab.TabFeatures.__int__()'''
            return int()
        def __ixor__(self, f):
            '''QStyleOptionTab.TabFeatures QStyleOptionTab.TabFeatures.__ixor__(QStyleOptionTab.TabFeatures f)'''
            return QStyleOptionTab.TabFeatures()
        def __ior__(self, f):
            '''QStyleOptionTab.TabFeatures QStyleOptionTab.TabFeatures.__ior__(QStyleOptionTab.TabFeatures f)'''
            return QStyleOptionTab.TabFeatures()
        def __iand__(self, mask):
            '''QStyleOptionTab.TabFeatures QStyleOptionTab.TabFeatures.__iand__(int mask)'''
            return QStyleOptionTab.TabFeatures()


class QStyleOptionProgressBar(QStyleOption):
    """"""
    # Enum QStyleOptionProgressBar.StyleOptionVersion
    Version = 0

    # Enum QStyleOptionProgressBar.StyleOptionType
    Type = 0

    bottomToTop = None # bool - member
    invertedAppearance = None # bool - member
    maximum = None # int - member
    minimum = None # int - member
    orientation = None # Qt.Orientation - member
    progress = None # int - member
    text = None # str - member
    textAlignment = None # Qt.Alignment - member
    textVisible = None # bool - member
    def __init__(self):
        '''void QStyleOptionProgressBar.__init__()'''
    def __init__(self, other):
        '''void QStyleOptionProgressBar.__init__(QStyleOptionProgressBar other)'''


class QStyleOptionMenuItem(QStyleOption):
    """"""
    # Enum QStyleOptionMenuItem.CheckType
    NotCheckable = 0
    Exclusive = 0
    NonExclusive = 0

    # Enum QStyleOptionMenuItem.MenuItemType
    Normal = 0
    DefaultItem = 0
    Separator = 0
    SubMenu = 0
    Scroller = 0
    TearOff = 0
    Margin = 0
    EmptyArea = 0

    # Enum QStyleOptionMenuItem.StyleOptionVersion
    Version = 0

    # Enum QStyleOptionMenuItem.StyleOptionType
    Type = 0

    checkType = None # QStyleOptionMenuItem.CheckType - member
    checked = None # bool - member
    font = None # QFont - member
    icon = None # QIcon - member
    maxIconWidth = None # int - member
    menuHasCheckableItems = None # bool - member
    menuItemType = None # QStyleOptionMenuItem.MenuItemType - member
    menuRect = None # QRect - member
    tabWidth = None # int - member
    text = None # str - member
    def __init__(self):
        '''void QStyleOptionMenuItem.__init__()'''
    def __init__(self, other):
        '''void QStyleOptionMenuItem.__init__(QStyleOptionMenuItem other)'''


class QStyleOptionDockWidget(QStyleOption):
    """"""
    # Enum QStyleOptionDockWidget.StyleOptionVersion
    Version = 0

    # Enum QStyleOptionDockWidget.StyleOptionType
    Type = 0

    closable = None # bool - member
    floatable = None # bool - member
    movable = None # bool - member
    title = None # str - member
    verticalTitleBar = None # bool - member
    def __init__(self):
        '''void QStyleOptionDockWidget.__init__()'''
    def __init__(self, other):
        '''void QStyleOptionDockWidget.__init__(QStyleOptionDockWidget other)'''


class QStyleOptionViewItem(QStyleOption):
    """"""
    # Enum QStyleOptionViewItem.ViewItemPosition
    Invalid = 0
    Beginning = 0
    Middle = 0
    End = 0
    OnlyOne = 0

    # Enum QStyleOptionViewItem.ViewItemFeature
    __kdevpythondocumentation_builtin_None = 0
    WrapText = 0
    Alternate = 0
    HasCheckIndicator = 0
    HasDisplay = 0
    HasDecoration = 0

    # Enum QStyleOptionViewItem.Position
    Left = 0
    Right = 0
    Top = 0
    Bottom = 0

    # Enum QStyleOptionViewItem.StyleOptionVersion
    Version = 0

    # Enum QStyleOptionViewItem.StyleOptionType
    Type = 0

    backgroundBrush = None # QBrush - member
    checkState = None # Qt.CheckState - member
    decorationAlignment = None # Qt.Alignment - member
    decorationPosition = None # QStyleOptionViewItem.Position - member
    decorationSize = None # QSize - member
    displayAlignment = None # Qt.Alignment - member
    features = None # QStyleOptionViewItem.ViewItemFeatures - member
    font = None # QFont - member
    icon = None # QIcon - member
    index = None # QModelIndex - member
    locale = None # QLocale - member
    showDecorationSelected = None # bool - member
    text = None # str - member
    textElideMode = None # Qt.TextElideMode - member
    viewItemPosition = None # QStyleOptionViewItem.ViewItemPosition - member
    widget = None # QWidget - member
    def __init__(self):
        '''void QStyleOptionViewItem.__init__()'''
    def __init__(self, other):
        '''void QStyleOptionViewItem.__init__(QStyleOptionViewItem other)'''
    class ViewItemFeatures():
        """"""
        def __init__(self):
            '''QStyleOptionViewItem.ViewItemFeatures QStyleOptionViewItem.ViewItemFeatures.__init__()'''
            return QStyleOptionViewItem.ViewItemFeatures()
        def __init__(self):
            '''int QStyleOptionViewItem.ViewItemFeatures.__init__()'''
            return int()
        def __init__(self):
            '''void QStyleOptionViewItem.ViewItemFeatures.__init__()'''
        def __bool__(self):
            '''int QStyleOptionViewItem.ViewItemFeatures.__bool__()'''
            return int()
        def __ne__(self, f):
            '''bool QStyleOptionViewItem.ViewItemFeatures.__ne__(QStyleOptionViewItem.ViewItemFeatures f)'''
            return bool()
        def __eq__(self, f):
            '''bool QStyleOptionViewItem.ViewItemFeatures.__eq__(QStyleOptionViewItem.ViewItemFeatures f)'''
            return bool()
        def __invert__(self):
            '''QStyleOptionViewItem.ViewItemFeatures QStyleOptionViewItem.ViewItemFeatures.__invert__()'''
            return QStyleOptionViewItem.ViewItemFeatures()
        def __and__(self, mask):
            '''QStyleOptionViewItem.ViewItemFeatures QStyleOptionViewItem.ViewItemFeatures.__and__(int mask)'''
            return QStyleOptionViewItem.ViewItemFeatures()
        def __xor__(self, f):
            '''QStyleOptionViewItem.ViewItemFeatures QStyleOptionViewItem.ViewItemFeatures.__xor__(QStyleOptionViewItem.ViewItemFeatures f)'''
            return QStyleOptionViewItem.ViewItemFeatures()
        def __xor__(self, f):
            '''QStyleOptionViewItem.ViewItemFeatures QStyleOptionViewItem.ViewItemFeatures.__xor__(int f)'''
            return QStyleOptionViewItem.ViewItemFeatures()
        def __or__(self, f):
            '''QStyleOptionViewItem.ViewItemFeatures QStyleOptionViewItem.ViewItemFeatures.__or__(QStyleOptionViewItem.ViewItemFeatures f)'''
            return QStyleOptionViewItem.ViewItemFeatures()
        def __or__(self, f):
            '''QStyleOptionViewItem.ViewItemFeatures QStyleOptionViewItem.ViewItemFeatures.__or__(int f)'''
            return QStyleOptionViewItem.ViewItemFeatures()
        def __int__(self):
            '''int QStyleOptionViewItem.ViewItemFeatures.__int__()'''
            return int()
        def __ixor__(self, f):
            '''QStyleOptionViewItem.ViewItemFeatures QStyleOptionViewItem.ViewItemFeatures.__ixor__(QStyleOptionViewItem.ViewItemFeatures f)'''
            return QStyleOptionViewItem.ViewItemFeatures()
        def __ior__(self, f):
            '''QStyleOptionViewItem.ViewItemFeatures QStyleOptionViewItem.ViewItemFeatures.__ior__(QStyleOptionViewItem.ViewItemFeatures f)'''
            return QStyleOptionViewItem.ViewItemFeatures()
        def __iand__(self, mask):
            '''QStyleOptionViewItem.ViewItemFeatures QStyleOptionViewItem.ViewItemFeatures.__iand__(int mask)'''
            return QStyleOptionViewItem.ViewItemFeatures()


class QStyleOptionToolBox(QStyleOption):
    """"""
    # Enum QStyleOptionToolBox.SelectedPosition
    NotAdjacent = 0
    NextIsSelected = 0
    PreviousIsSelected = 0

    # Enum QStyleOptionToolBox.TabPosition
    Beginning = 0
    Middle = 0
    End = 0
    OnlyOneTab = 0

    # Enum QStyleOptionToolBox.StyleOptionVersion
    Version = 0

    # Enum QStyleOptionToolBox.StyleOptionType
    Type = 0

    icon = None # QIcon - member
    position = None # QStyleOptionToolBox.TabPosition - member
    selectedPosition = None # QStyleOptionToolBox.SelectedPosition - member
    text = None # str - member
    def __init__(self):
        '''void QStyleOptionToolBox.__init__()'''
    def __init__(self, other):
        '''void QStyleOptionToolBox.__init__(QStyleOptionToolBox other)'''


class QStyleOptionRubberBand(QStyleOption):
    """"""
    # Enum QStyleOptionRubberBand.StyleOptionVersion
    Version = 0

    # Enum QStyleOptionRubberBand.StyleOptionType
    Type = 0

    opaque = None # bool - member
    shape = None # QRubberBand.Shape - member
    def __init__(self):
        '''void QStyleOptionRubberBand.__init__()'''
    def __init__(self, other):
        '''void QStyleOptionRubberBand.__init__(QStyleOptionRubberBand other)'''


class QStyleOptionComplex(QStyleOption):
    """"""
    # Enum QStyleOptionComplex.StyleOptionVersion
    Version = 0

    # Enum QStyleOptionComplex.StyleOptionType
    Type = 0

    activeSubControls = None # QStyle.SubControls - member
    subControls = None # QStyle.SubControls - member
    def __init__(self, version = None, type = None):
        '''void QStyleOptionComplex.__init__(int version = QStyleOptionComplex.Version, int type = QStyleOption.SO_Complex)'''
    def __init__(self, other):
        '''void QStyleOptionComplex.__init__(QStyleOptionComplex other)'''


class QStyleOptionSlider(QStyleOptionComplex):
    """"""
    # Enum QStyleOptionSlider.StyleOptionVersion
    Version = 0

    # Enum QStyleOptionSlider.StyleOptionType
    Type = 0

    dialWrapping = None # bool - member
    maximum = None # int - member
    minimum = None # int - member
    notchTarget = None # float - member
    orientation = None # Qt.Orientation - member
    pageStep = None # int - member
    singleStep = None # int - member
    sliderPosition = None # int - member
    sliderValue = None # int - member
    tickInterval = None # int - member
    tickPosition = None # QSlider.TickPosition - member
    upsideDown = None # bool - member
    def __init__(self):
        '''void QStyleOptionSlider.__init__()'''
    def __init__(self, other):
        '''void QStyleOptionSlider.__init__(QStyleOptionSlider other)'''


class QStyleOptionSpinBox(QStyleOptionComplex):
    """"""
    # Enum QStyleOptionSpinBox.StyleOptionVersion
    Version = 0

    # Enum QStyleOptionSpinBox.StyleOptionType
    Type = 0

    buttonSymbols = None # QAbstractSpinBox.ButtonSymbols - member
    frame = None # bool - member
    stepEnabled = None # QAbstractSpinBox.StepEnabled - member
    def __init__(self):
        '''void QStyleOptionSpinBox.__init__()'''
    def __init__(self, other):
        '''void QStyleOptionSpinBox.__init__(QStyleOptionSpinBox other)'''


class QStyleOptionToolButton(QStyleOptionComplex):
    """"""
    # Enum QStyleOptionToolButton.ToolButtonFeature
    __kdevpythondocumentation_builtin_None = 0
    Arrow = 0
    Menu = 0
    PopupDelay = 0
    MenuButtonPopup = 0
    HasMenu = 0

    # Enum QStyleOptionToolButton.StyleOptionVersion
    Version = 0

    # Enum QStyleOptionToolButton.StyleOptionType
    Type = 0

    arrowType = None # Qt.ArrowType - member
    features = None # QStyleOptionToolButton.ToolButtonFeatures - member
    font = None # QFont - member
    icon = None # QIcon - member
    iconSize = None # QSize - member
    pos = None # QPoint - member
    text = None # str - member
    toolButtonStyle = None # Qt.ToolButtonStyle - member
    def __init__(self):
        '''void QStyleOptionToolButton.__init__()'''
    def __init__(self, other):
        '''void QStyleOptionToolButton.__init__(QStyleOptionToolButton other)'''
    class ToolButtonFeatures():
        """"""
        def __init__(self):
            '''QStyleOptionToolButton.ToolButtonFeatures QStyleOptionToolButton.ToolButtonFeatures.__init__()'''
            return QStyleOptionToolButton.ToolButtonFeatures()
        def __init__(self):
            '''int QStyleOptionToolButton.ToolButtonFeatures.__init__()'''
            return int()
        def __init__(self):
            '''void QStyleOptionToolButton.ToolButtonFeatures.__init__()'''
        def __bool__(self):
            '''int QStyleOptionToolButton.ToolButtonFeatures.__bool__()'''
            return int()
        def __ne__(self, f):
            '''bool QStyleOptionToolButton.ToolButtonFeatures.__ne__(QStyleOptionToolButton.ToolButtonFeatures f)'''
            return bool()
        def __eq__(self, f):
            '''bool QStyleOptionToolButton.ToolButtonFeatures.__eq__(QStyleOptionToolButton.ToolButtonFeatures f)'''
            return bool()
        def __invert__(self):
            '''QStyleOptionToolButton.ToolButtonFeatures QStyleOptionToolButton.ToolButtonFeatures.__invert__()'''
            return QStyleOptionToolButton.ToolButtonFeatures()
        def __and__(self, mask):
            '''QStyleOptionToolButton.ToolButtonFeatures QStyleOptionToolButton.ToolButtonFeatures.__and__(int mask)'''
            return QStyleOptionToolButton.ToolButtonFeatures()
        def __xor__(self, f):
            '''QStyleOptionToolButton.ToolButtonFeatures QStyleOptionToolButton.ToolButtonFeatures.__xor__(QStyleOptionToolButton.ToolButtonFeatures f)'''
            return QStyleOptionToolButton.ToolButtonFeatures()
        def __xor__(self, f):
            '''QStyleOptionToolButton.ToolButtonFeatures QStyleOptionToolButton.ToolButtonFeatures.__xor__(int f)'''
            return QStyleOptionToolButton.ToolButtonFeatures()
        def __or__(self, f):
            '''QStyleOptionToolButton.ToolButtonFeatures QStyleOptionToolButton.ToolButtonFeatures.__or__(QStyleOptionToolButton.ToolButtonFeatures f)'''
            return QStyleOptionToolButton.ToolButtonFeatures()
        def __or__(self, f):
            '''QStyleOptionToolButton.ToolButtonFeatures QStyleOptionToolButton.ToolButtonFeatures.__or__(int f)'''
            return QStyleOptionToolButton.ToolButtonFeatures()
        def __int__(self):
            '''int QStyleOptionToolButton.ToolButtonFeatures.__int__()'''
            return int()
        def __ixor__(self, f):
            '''QStyleOptionToolButton.ToolButtonFeatures QStyleOptionToolButton.ToolButtonFeatures.__ixor__(QStyleOptionToolButton.ToolButtonFeatures f)'''
            return QStyleOptionToolButton.ToolButtonFeatures()
        def __ior__(self, f):
            '''QStyleOptionToolButton.ToolButtonFeatures QStyleOptionToolButton.ToolButtonFeatures.__ior__(QStyleOptionToolButton.ToolButtonFeatures f)'''
            return QStyleOptionToolButton.ToolButtonFeatures()
        def __iand__(self, mask):
            '''QStyleOptionToolButton.ToolButtonFeatures QStyleOptionToolButton.ToolButtonFeatures.__iand__(int mask)'''
            return QStyleOptionToolButton.ToolButtonFeatures()


class QStyleOptionComboBox(QStyleOptionComplex):
    """"""
    # Enum QStyleOptionComboBox.StyleOptionVersion
    Version = 0

    # Enum QStyleOptionComboBox.StyleOptionType
    Type = 0

    currentIcon = None # QIcon - member
    currentText = None # str - member
    editable = None # bool - member
    frame = None # bool - member
    iconSize = None # QSize - member
    popupRect = None # QRect - member
    def __init__(self):
        '''void QStyleOptionComboBox.__init__()'''
    def __init__(self, other):
        '''void QStyleOptionComboBox.__init__(QStyleOptionComboBox other)'''


class QStyleOptionTitleBar(QStyleOptionComplex):
    """"""
    # Enum QStyleOptionTitleBar.StyleOptionVersion
    Version = 0

    # Enum QStyleOptionTitleBar.StyleOptionType
    Type = 0

    icon = None # QIcon - member
    text = None # str - member
    titleBarFlags = None # Qt.WindowFlags - member
    titleBarState = None # int - member
    def __init__(self):
        '''void QStyleOptionTitleBar.__init__()'''
    def __init__(self, other):
        '''void QStyleOptionTitleBar.__init__(QStyleOptionTitleBar other)'''


class QStyleHintReturn():
    """"""
    # Enum QStyleHintReturn.StyleOptionVersion
    Version = 0

    # Enum QStyleHintReturn.StyleOptionType
    Type = 0

    # Enum QStyleHintReturn.HintReturnType
    SH_Default = 0
    SH_Mask = 0
    SH_Variant = 0

    type = None # int - member
    version = None # int - member
    def __init__(self, version = None, type = None):
        '''void QStyleHintReturn.__init__(int version = QStyleOption.Version, int type = QStyleHintReturn.SH_Default)'''
    def __init__(self):
        '''QStyleHintReturn QStyleHintReturn.__init__()'''
        return QStyleHintReturn()


class QStyleHintReturnMask(QStyleHintReturn):
    """"""
    # Enum QStyleHintReturnMask.StyleOptionVersion
    Version = 0

    # Enum QStyleHintReturnMask.StyleOptionType
    Type = 0

    region = None # QRegion - member
    def __init__(self):
        '''void QStyleHintReturnMask.__init__()'''
    def __init__(self):
        '''QStyleHintReturnMask QStyleHintReturnMask.__init__()'''
        return QStyleHintReturnMask()


class QStyleOptionToolBar(QStyleOption):
    """"""
    # Enum QStyleOptionToolBar.ToolBarFeature
    __kdevpythondocumentation_builtin_None = 0
    Movable = 0

    # Enum QStyleOptionToolBar.ToolBarPosition
    Beginning = 0
    Middle = 0
    End = 0
    OnlyOne = 0

    # Enum QStyleOptionToolBar.StyleOptionVersion
    Version = 0

    # Enum QStyleOptionToolBar.StyleOptionType
    Type = 0

    features = None # QStyleOptionToolBar.ToolBarFeatures - member
    lineWidth = None # int - member
    midLineWidth = None # int - member
    positionOfLine = None # QStyleOptionToolBar.ToolBarPosition - member
    positionWithinLine = None # QStyleOptionToolBar.ToolBarPosition - member
    toolBarArea = None # Qt.ToolBarArea - member
    def __init__(self):
        '''void QStyleOptionToolBar.__init__()'''
    def __init__(self, other):
        '''void QStyleOptionToolBar.__init__(QStyleOptionToolBar other)'''
    class ToolBarFeatures():
        """"""
        def __init__(self):
            '''QStyleOptionToolBar.ToolBarFeatures QStyleOptionToolBar.ToolBarFeatures.__init__()'''
            return QStyleOptionToolBar.ToolBarFeatures()
        def __init__(self):
            '''int QStyleOptionToolBar.ToolBarFeatures.__init__()'''
            return int()
        def __init__(self):
            '''void QStyleOptionToolBar.ToolBarFeatures.__init__()'''
        def __bool__(self):
            '''int QStyleOptionToolBar.ToolBarFeatures.__bool__()'''
            return int()
        def __ne__(self, f):
            '''bool QStyleOptionToolBar.ToolBarFeatures.__ne__(QStyleOptionToolBar.ToolBarFeatures f)'''
            return bool()
        def __eq__(self, f):
            '''bool QStyleOptionToolBar.ToolBarFeatures.__eq__(QStyleOptionToolBar.ToolBarFeatures f)'''
            return bool()
        def __invert__(self):
            '''QStyleOptionToolBar.ToolBarFeatures QStyleOptionToolBar.ToolBarFeatures.__invert__()'''
            return QStyleOptionToolBar.ToolBarFeatures()
        def __and__(self, mask):
            '''QStyleOptionToolBar.ToolBarFeatures QStyleOptionToolBar.ToolBarFeatures.__and__(int mask)'''
            return QStyleOptionToolBar.ToolBarFeatures()
        def __xor__(self, f):
            '''QStyleOptionToolBar.ToolBarFeatures QStyleOptionToolBar.ToolBarFeatures.__xor__(QStyleOptionToolBar.ToolBarFeatures f)'''
            return QStyleOptionToolBar.ToolBarFeatures()
        def __xor__(self, f):
            '''QStyleOptionToolBar.ToolBarFeatures QStyleOptionToolBar.ToolBarFeatures.__xor__(int f)'''
            return QStyleOptionToolBar.ToolBarFeatures()
        def __or__(self, f):
            '''QStyleOptionToolBar.ToolBarFeatures QStyleOptionToolBar.ToolBarFeatures.__or__(QStyleOptionToolBar.ToolBarFeatures f)'''
            return QStyleOptionToolBar.ToolBarFeatures()
        def __or__(self, f):
            '''QStyleOptionToolBar.ToolBarFeatures QStyleOptionToolBar.ToolBarFeatures.__or__(int f)'''
            return QStyleOptionToolBar.ToolBarFeatures()
        def __int__(self):
            '''int QStyleOptionToolBar.ToolBarFeatures.__int__()'''
            return int()
        def __ixor__(self, f):
            '''QStyleOptionToolBar.ToolBarFeatures QStyleOptionToolBar.ToolBarFeatures.__ixor__(QStyleOptionToolBar.ToolBarFeatures f)'''
            return QStyleOptionToolBar.ToolBarFeatures()
        def __ior__(self, f):
            '''QStyleOptionToolBar.ToolBarFeatures QStyleOptionToolBar.ToolBarFeatures.__ior__(QStyleOptionToolBar.ToolBarFeatures f)'''
            return QStyleOptionToolBar.ToolBarFeatures()
        def __iand__(self, mask):
            '''QStyleOptionToolBar.ToolBarFeatures QStyleOptionToolBar.ToolBarFeatures.__iand__(int mask)'''
            return QStyleOptionToolBar.ToolBarFeatures()


class QStyleOptionGroupBox(QStyleOptionComplex):
    """"""
    # Enum QStyleOptionGroupBox.StyleOptionVersion
    Version = 0

    # Enum QStyleOptionGroupBox.StyleOptionType
    Type = 0

    features = None # QStyleOptionFrame.FrameFeatures - member
    lineWidth = None # int - member
    midLineWidth = None # int - member
    text = None # str - member
    textAlignment = None # Qt.Alignment - member
    textColor = None # QColor - member
    def __init__(self):
        '''void QStyleOptionGroupBox.__init__()'''
    def __init__(self, other):
        '''void QStyleOptionGroupBox.__init__(QStyleOptionGroupBox other)'''


class QStyleOptionSizeGrip(QStyleOptionComplex):
    """"""
    # Enum QStyleOptionSizeGrip.StyleOptionVersion
    Version = 0

    # Enum QStyleOptionSizeGrip.StyleOptionType
    Type = 0

    corner = None # Qt.Corner - member
    def __init__(self):
        '''void QStyleOptionSizeGrip.__init__()'''
    def __init__(self, other):
        '''void QStyleOptionSizeGrip.__init__(QStyleOptionSizeGrip other)'''


class QStyleOptionGraphicsItem(QStyleOption):
    """"""
    # Enum QStyleOptionGraphicsItem.StyleOptionVersion
    Version = 0

    # Enum QStyleOptionGraphicsItem.StyleOptionType
    Type = 0

    exposedRect = None # QRectF - member
    def __init__(self):
        '''void QStyleOptionGraphicsItem.__init__()'''
    def __init__(self, other):
        '''void QStyleOptionGraphicsItem.__init__(QStyleOptionGraphicsItem other)'''
    def levelOfDetailFromTransform(self, worldTransform):
        '''static float QStyleOptionGraphicsItem.levelOfDetailFromTransform(QTransform worldTransform)'''
        return float()


class QStyleHintReturnVariant(QStyleHintReturn):
    """"""
    # Enum QStyleHintReturnVariant.StyleOptionVersion
    Version = 0

    # Enum QStyleHintReturnVariant.StyleOptionType
    Type = 0

    variant = None # QVariant - member
    def __init__(self):
        '''void QStyleHintReturnVariant.__init__()'''
    def __init__(self):
        '''QStyleHintReturnVariant QStyleHintReturnVariant.__init__()'''
        return QStyleHintReturnVariant()


class QStylePainter(QPainter):
    """"""
    def __init__(self):
        '''void QStylePainter.__init__()'''
    def __init__(self, w):
        '''void QStylePainter.__init__(QWidget w)'''
    def __init__(self, pd, w):
        '''void QStylePainter.__init__(QPaintDevice pd, QWidget w)'''
    def drawItemPixmap(self, r, flags, pixmap):
        '''void QStylePainter.drawItemPixmap(QRect r, int flags, QPixmap pixmap)'''
    def drawItemText(self, rect, flags, pal, enabled, text, textRole = None):
        '''void QStylePainter.drawItemText(QRect rect, int flags, QPalette pal, bool enabled, str text, QPalette.ColorRole textRole = QPalette.NoRole)'''
    def drawComplexControl(self, cc, opt):
        '''void QStylePainter.drawComplexControl(QStyle.ComplexControl cc, QStyleOptionComplex opt)'''
    def drawControl(self, ce, opt):
        '''void QStylePainter.drawControl(QStyle.ControlElement ce, QStyleOption opt)'''
    def drawPrimitive(self, pe, opt):
        '''void QStylePainter.drawPrimitive(QStyle.PrimitiveElement pe, QStyleOption opt)'''
    def style(self):
        '''QStyle QStylePainter.style()'''
        return QStyle()
    def begin(self, w):
        '''bool QStylePainter.begin(QWidget w)'''
        return bool()
    def begin(self, pd, w):
        '''bool QStylePainter.begin(QPaintDevice pd, QWidget w)'''
        return bool()


class QSystemTrayIcon(QObject):
    """"""
    # Enum QSystemTrayIcon.MessageIcon
    NoIcon = 0
    Information = 0
    Warning = 0
    Critical = 0

    # Enum QSystemTrayIcon.ActivationReason
    Unknown = 0
    Context = 0
    DoubleClick = 0
    Trigger = 0
    MiddleClick = 0

    def __init__(self, parent = None):
        '''void QSystemTrayIcon.__init__(QObject parent = None)'''
    def __init__(self, icon, parent = None):
        '''void QSystemTrayIcon.__init__(QIcon icon, QObject parent = None)'''
    def event(self, event):
        '''bool QSystemTrayIcon.event(QEvent event)'''
        return bool()
    messageClicked = pyqtSignal() # void messageClicked() - signal
    activated = pyqtSignal() # void activated(QSystemTrayIcon::ActivationReason) - signal
    def show(self):
        '''void QSystemTrayIcon.show()'''
    def setVisible(self, visible):
        '''void QSystemTrayIcon.setVisible(bool visible)'''
    def hide(self):
        '''void QSystemTrayIcon.hide()'''
    def isVisible(self):
        '''bool QSystemTrayIcon.isVisible()'''
        return bool()
    def showMessage(self, title, msg, icon = None, msecs = 10000):
        '''void QSystemTrayIcon.showMessage(str title, str msg, QSystemTrayIcon.MessageIcon icon = QSystemTrayIcon.Information, int msecs = 10000)'''
    def supportsMessages(self):
        '''static bool QSystemTrayIcon.supportsMessages()'''
        return bool()
    def isSystemTrayAvailable(self):
        '''static bool QSystemTrayIcon.isSystemTrayAvailable()'''
        return bool()
    def setToolTip(self, tip):
        '''void QSystemTrayIcon.setToolTip(str tip)'''
    def toolTip(self):
        '''str QSystemTrayIcon.toolTip()'''
        return str()
    def setIcon(self, icon):
        '''void QSystemTrayIcon.setIcon(QIcon icon)'''
    def icon(self):
        '''QIcon QSystemTrayIcon.icon()'''
        return QIcon()
    def geometry(self):
        '''QRect QSystemTrayIcon.geometry()'''
        return QRect()
    def contextMenu(self):
        '''QMenu QSystemTrayIcon.contextMenu()'''
        return QMenu()
    def setContextMenu(self, menu):
        '''void QSystemTrayIcon.setContextMenu(QMenu menu)'''


class QTabBar(QWidget):
    """"""
    # Enum QTabBar.SelectionBehavior
    SelectLeftTab = 0
    SelectRightTab = 0
    SelectPreviousTab = 0

    # Enum QTabBar.ButtonPosition
    LeftSide = 0
    RightSide = 0

    # Enum QTabBar.Shape
    RoundedNorth = 0
    RoundedSouth = 0
    RoundedWest = 0
    RoundedEast = 0
    TriangularNorth = 0
    TriangularSouth = 0
    TriangularWest = 0
    TriangularEast = 0

    def __init__(self, parent = None):
        '''void QTabBar.__init__(QWidget parent = None)'''
    def timerEvent(self, event):
        '''void QTabBar.timerEvent(QTimerEvent event)'''
    def setChangeCurrentOnDrag(self, change):
        '''void QTabBar.setChangeCurrentOnDrag(bool change)'''
    def changeCurrentOnDrag(self):
        '''bool QTabBar.changeCurrentOnDrag()'''
        return bool()
    def setAutoHide(self, hide):
        '''void QTabBar.setAutoHide(bool hide)'''
    def autoHide(self):
        '''bool QTabBar.autoHide()'''
        return bool()
    tabBarDoubleClicked = pyqtSignal() # void tabBarDoubleClicked(int) - signal
    tabBarClicked = pyqtSignal() # void tabBarClicked(int) - signal
    def minimumTabSizeHint(self, index):
        '''QSize QTabBar.minimumTabSizeHint(int index)'''
        return QSize()
    def wheelEvent(self, event):
        '''void QTabBar.wheelEvent(QWheelEvent event)'''
    def hideEvent(self):
        '''QHideEvent QTabBar.hideEvent()'''
        return QHideEvent()
    tabMoved = pyqtSignal() # void tabMoved(int,int) - signal
    tabCloseRequested = pyqtSignal() # void tabCloseRequested(int) - signal
    def setDocumentMode(self, set):
        '''void QTabBar.setDocumentMode(bool set)'''
    def documentMode(self):
        '''bool QTabBar.documentMode()'''
        return bool()
    def setMovable(self, movable):
        '''void QTabBar.setMovable(bool movable)'''
    def isMovable(self):
        '''bool QTabBar.isMovable()'''
        return bool()
    def setExpanding(self, enabled):
        '''void QTabBar.setExpanding(bool enabled)'''
    def expanding(self):
        '''bool QTabBar.expanding()'''
        return bool()
    def setSelectionBehaviorOnRemove(self, behavior):
        '''void QTabBar.setSelectionBehaviorOnRemove(QTabBar.SelectionBehavior behavior)'''
    def selectionBehaviorOnRemove(self):
        '''QTabBar.SelectionBehavior QTabBar.selectionBehaviorOnRemove()'''
        return QTabBar.SelectionBehavior()
    def tabButton(self, index, position):
        '''QWidget QTabBar.tabButton(int index, QTabBar.ButtonPosition position)'''
        return QWidget()
    def setTabButton(self, index, position, widget):
        '''void QTabBar.setTabButton(int index, QTabBar.ButtonPosition position, QWidget widget)'''
    def setTabsClosable(self, closable):
        '''void QTabBar.setTabsClosable(bool closable)'''
    def tabsClosable(self):
        '''bool QTabBar.tabsClosable()'''
        return bool()
    def moveTab(self, from_, to):
        '''void QTabBar.moveTab(int from, int to)'''
    def changeEvent(self):
        '''QEvent QTabBar.changeEvent()'''
        return QEvent()
    def keyPressEvent(self):
        '''QKeyEvent QTabBar.keyPressEvent()'''
        return QKeyEvent()
    def mouseReleaseEvent(self):
        '''QMouseEvent QTabBar.mouseReleaseEvent()'''
        return QMouseEvent()
    def mouseMoveEvent(self):
        '''QMouseEvent QTabBar.mouseMoveEvent()'''
        return QMouseEvent()
    def mousePressEvent(self):
        '''QMouseEvent QTabBar.mousePressEvent()'''
        return QMouseEvent()
    def paintEvent(self):
        '''QPaintEvent QTabBar.paintEvent()'''
        return QPaintEvent()
    def showEvent(self):
        '''QShowEvent QTabBar.showEvent()'''
        return QShowEvent()
    def resizeEvent(self):
        '''QResizeEvent QTabBar.resizeEvent()'''
        return QResizeEvent()
    def event(self):
        '''QEvent QTabBar.event()'''
        return QEvent()
    def tabLayoutChange(self):
        '''void QTabBar.tabLayoutChange()'''
    def tabRemoved(self, index):
        '''void QTabBar.tabRemoved(int index)'''
    def tabInserted(self, index):
        '''void QTabBar.tabInserted(int index)'''
    def tabSizeHint(self, index):
        '''QSize QTabBar.tabSizeHint(int index)'''
        return QSize()
    def initStyleOption(self, option, tabIndex):
        '''void QTabBar.initStyleOption(QStyleOptionTab option, int tabIndex)'''
    currentChanged = pyqtSignal() # void currentChanged(int) - signal
    def setCurrentIndex(self, index):
        '''void QTabBar.setCurrentIndex(int index)'''
    def usesScrollButtons(self):
        '''bool QTabBar.usesScrollButtons()'''
        return bool()
    def setUsesScrollButtons(self, useButtons):
        '''void QTabBar.setUsesScrollButtons(bool useButtons)'''
    def setElideMode(self):
        '''Qt.TextElideMode QTabBar.setElideMode()'''
        return Qt.TextElideMode()
    def elideMode(self):
        '''Qt.TextElideMode QTabBar.elideMode()'''
        return Qt.TextElideMode()
    def setIconSize(self, size):
        '''void QTabBar.setIconSize(QSize size)'''
    def iconSize(self):
        '''QSize QTabBar.iconSize()'''
        return QSize()
    def drawBase(self):
        '''bool QTabBar.drawBase()'''
        return bool()
    def setDrawBase(self, drawTheBase):
        '''void QTabBar.setDrawBase(bool drawTheBase)'''
    def minimumSizeHint(self):
        '''QSize QTabBar.minimumSizeHint()'''
        return QSize()
    def sizeHint(self):
        '''QSize QTabBar.sizeHint()'''
        return QSize()
    def __len__(self):
        ''' QTabBar.__len__()'''
        return ()
    def count(self):
        '''int QTabBar.count()'''
        return int()
    def currentIndex(self):
        '''int QTabBar.currentIndex()'''
        return int()
    def tabRect(self, index):
        '''QRect QTabBar.tabRect(int index)'''
        return QRect()
    def tabAt(self, pos):
        '''int QTabBar.tabAt(QPoint pos)'''
        return int()
    def tabData(self, index):
        '''QVariant QTabBar.tabData(int index)'''
        return QVariant()
    def setTabData(self, index, data):
        '''void QTabBar.setTabData(int index, QVariant data)'''
    def tabWhatsThis(self, index):
        '''str QTabBar.tabWhatsThis(int index)'''
        return str()
    def setTabWhatsThis(self, index, text):
        '''void QTabBar.setTabWhatsThis(int index, str text)'''
    def tabToolTip(self, index):
        '''str QTabBar.tabToolTip(int index)'''
        return str()
    def setTabToolTip(self, index, tip):
        '''void QTabBar.setTabToolTip(int index, str tip)'''
    def setTabIcon(self, index, icon):
        '''void QTabBar.setTabIcon(int index, QIcon icon)'''
    def tabIcon(self, index):
        '''QIcon QTabBar.tabIcon(int index)'''
        return QIcon()
    def setTabTextColor(self, index, color):
        '''void QTabBar.setTabTextColor(int index, QColor color)'''
    def tabTextColor(self, index):
        '''QColor QTabBar.tabTextColor(int index)'''
        return QColor()
    def setTabText(self, index, text):
        '''void QTabBar.setTabText(int index, str text)'''
    def tabText(self, index):
        '''str QTabBar.tabText(int index)'''
        return str()
    def setTabEnabled(self, index):
        '''bool QTabBar.setTabEnabled(int index)'''
        return bool()
    def isTabEnabled(self, index):
        '''bool QTabBar.isTabEnabled(int index)'''
        return bool()
    def removeTab(self, index):
        '''void QTabBar.removeTab(int index)'''
    def insertTab(self, index, text):
        '''int QTabBar.insertTab(int index, str text)'''
        return int()
    def insertTab(self, index, icon, text):
        '''int QTabBar.insertTab(int index, QIcon icon, str text)'''
        return int()
    def addTab(self, text):
        '''int QTabBar.addTab(str text)'''
        return int()
    def addTab(self, icon, text):
        '''int QTabBar.addTab(QIcon icon, str text)'''
        return int()
    def setShape(self, shape):
        '''void QTabBar.setShape(QTabBar.Shape shape)'''
    def shape(self):
        '''QTabBar.Shape QTabBar.shape()'''
        return QTabBar.Shape()


class QTableView(QAbstractItemView):
    """"""
    def __init__(self, parent = None):
        '''void QTableView.__init__(QWidget parent = None)'''
    def currentChanged(self, current, previous):
        '''void QTableView.currentChanged(QModelIndex current, QModelIndex previous)'''
    def selectionChanged(self, selected, deselected):
        '''void QTableView.selectionChanged(QItemSelection selected, QItemSelection deselected)'''
    def clearSpans(self):
        '''void QTableView.clearSpans()'''
    def isCornerButtonEnabled(self):
        '''bool QTableView.isCornerButtonEnabled()'''
        return bool()
    def setCornerButtonEnabled(self, enable):
        '''void QTableView.setCornerButtonEnabled(bool enable)'''
    def wordWrap(self):
        '''bool QTableView.wordWrap()'''
        return bool()
    def setWordWrap(self, on):
        '''void QTableView.setWordWrap(bool on)'''
    def sortByColumn(self, column, order):
        '''void QTableView.sortByColumn(int column, Qt.SortOrder order)'''
    def columnSpan(self, row, column):
        '''int QTableView.columnSpan(int row, int column)'''
        return int()
    def rowSpan(self, row, column):
        '''int QTableView.rowSpan(int row, int column)'''
        return int()
    def setSpan(self, row, column, rowSpan, columnSpan):
        '''void QTableView.setSpan(int row, int column, int rowSpan, int columnSpan)'''
    def isSortingEnabled(self):
        '''bool QTableView.isSortingEnabled()'''
        return bool()
    def setSortingEnabled(self, enable):
        '''void QTableView.setSortingEnabled(bool enable)'''
    def viewportSizeHint(self):
        '''QSize QTableView.viewportSizeHint()'''
        return QSize()
    def isIndexHidden(self, index):
        '''bool QTableView.isIndexHidden(QModelIndex index)'''
        return bool()
    def horizontalScrollbarAction(self, action):
        '''void QTableView.horizontalScrollbarAction(int action)'''
    def verticalScrollbarAction(self, action):
        '''void QTableView.verticalScrollbarAction(int action)'''
    def sizeHintForColumn(self, column):
        '''int QTableView.sizeHintForColumn(int column)'''
        return int()
    def sizeHintForRow(self, row):
        '''int QTableView.sizeHintForRow(int row)'''
        return int()
    def updateGeometries(self):
        '''void QTableView.updateGeometries()'''
    def selectedIndexes(self):
        '''list-of-QModelIndex QTableView.selectedIndexes()'''
        return [QModelIndex()]
    def visualRegionForSelection(self, selection):
        '''QRegion QTableView.visualRegionForSelection(QItemSelection selection)'''
        return QRegion()
    def setSelection(self, rect, command):
        '''void QTableView.setSelection(QRect rect, QItemSelectionModel.SelectionFlags command)'''
    def moveCursor(self, cursorAction, modifiers):
        '''QModelIndex QTableView.moveCursor(QAbstractItemView.CursorAction cursorAction, Qt.KeyboardModifiers modifiers)'''
        return QModelIndex()
    def verticalOffset(self):
        '''int QTableView.verticalOffset()'''
        return int()
    def horizontalOffset(self):
        '''int QTableView.horizontalOffset()'''
        return int()
    def timerEvent(self, event):
        '''void QTableView.timerEvent(QTimerEvent event)'''
    def paintEvent(self, e):
        '''void QTableView.paintEvent(QPaintEvent e)'''
    def viewOptions(self):
        '''QStyleOptionViewItem QTableView.viewOptions()'''
        return QStyleOptionViewItem()
    def scrollContentsBy(self, dx, dy):
        '''void QTableView.scrollContentsBy(int dx, int dy)'''
    def columnCountChanged(self, oldCount, newCount):
        '''void QTableView.columnCountChanged(int oldCount, int newCount)'''
    def rowCountChanged(self, oldCount, newCount):
        '''void QTableView.rowCountChanged(int oldCount, int newCount)'''
    def columnResized(self, column, oldWidth, newWidth):
        '''void QTableView.columnResized(int column, int oldWidth, int newWidth)'''
    def rowResized(self, row, oldHeight, newHeight):
        '''void QTableView.rowResized(int row, int oldHeight, int newHeight)'''
    def columnMoved(self, column, oldIndex, newIndex):
        '''void QTableView.columnMoved(int column, int oldIndex, int newIndex)'''
    def rowMoved(self, row, oldIndex, newIndex):
        '''void QTableView.rowMoved(int row, int oldIndex, int newIndex)'''
    def resizeColumnsToContents(self):
        '''void QTableView.resizeColumnsToContents()'''
    def resizeColumnToContents(self, column):
        '''void QTableView.resizeColumnToContents(int column)'''
    def resizeRowsToContents(self):
        '''void QTableView.resizeRowsToContents()'''
    def resizeRowToContents(self, row):
        '''void QTableView.resizeRowToContents(int row)'''
    def showColumn(self, column):
        '''void QTableView.showColumn(int column)'''
    def showRow(self, row):
        '''void QTableView.showRow(int row)'''
    def hideColumn(self, column):
        '''void QTableView.hideColumn(int column)'''
    def hideRow(self, row):
        '''void QTableView.hideRow(int row)'''
    def selectColumn(self, column):
        '''void QTableView.selectColumn(int column)'''
    def selectRow(self, row):
        '''void QTableView.selectRow(int row)'''
    def indexAt(self, p):
        '''QModelIndex QTableView.indexAt(QPoint p)'''
        return QModelIndex()
    def scrollTo(self, index, hint = None):
        '''void QTableView.scrollTo(QModelIndex index, QAbstractItemView.ScrollHint hint = QAbstractItemView.EnsureVisible)'''
    def visualRect(self, index):
        '''QRect QTableView.visualRect(QModelIndex index)'''
        return QRect()
    def setGridStyle(self, style):
        '''void QTableView.setGridStyle(Qt.PenStyle style)'''
    def gridStyle(self):
        '''Qt.PenStyle QTableView.gridStyle()'''
        return Qt.PenStyle()
    def setShowGrid(self, show):
        '''void QTableView.setShowGrid(bool show)'''
    def showGrid(self):
        '''bool QTableView.showGrid()'''
        return bool()
    def setColumnHidden(self, column, hide):
        '''void QTableView.setColumnHidden(int column, bool hide)'''
    def isColumnHidden(self, column):
        '''bool QTableView.isColumnHidden(int column)'''
        return bool()
    def setRowHidden(self, row, hide):
        '''void QTableView.setRowHidden(int row, bool hide)'''
    def isRowHidden(self, row):
        '''bool QTableView.isRowHidden(int row)'''
        return bool()
    def columnAt(self, x):
        '''int QTableView.columnAt(int x)'''
        return int()
    def columnWidth(self, column):
        '''int QTableView.columnWidth(int column)'''
        return int()
    def setColumnWidth(self, column, width):
        '''void QTableView.setColumnWidth(int column, int width)'''
    def columnViewportPosition(self, column):
        '''int QTableView.columnViewportPosition(int column)'''
        return int()
    def rowAt(self, y):
        '''int QTableView.rowAt(int y)'''
        return int()
    def rowHeight(self, row):
        '''int QTableView.rowHeight(int row)'''
        return int()
    def setRowHeight(self, row, height):
        '''void QTableView.setRowHeight(int row, int height)'''
    def rowViewportPosition(self, row):
        '''int QTableView.rowViewportPosition(int row)'''
        return int()
    def setVerticalHeader(self, header):
        '''void QTableView.setVerticalHeader(QHeaderView header)'''
    def setHorizontalHeader(self, header):
        '''void QTableView.setHorizontalHeader(QHeaderView header)'''
    def verticalHeader(self):
        '''QHeaderView QTableView.verticalHeader()'''
        return QHeaderView()
    def horizontalHeader(self):
        '''QHeaderView QTableView.horizontalHeader()'''
        return QHeaderView()
    def setSelectionModel(self, selectionModel):
        '''void QTableView.setSelectionModel(QItemSelectionModel selectionModel)'''
    def setRootIndex(self, index):
        '''void QTableView.setRootIndex(QModelIndex index)'''
    def setModel(self, model):
        '''void QTableView.setModel(QAbstractItemModel model)'''


class QTableWidgetSelectionRange():
    """"""
    def __init__(self):
        '''void QTableWidgetSelectionRange.__init__()'''
    def __init__(self, top, left, bottom, right):
        '''void QTableWidgetSelectionRange.__init__(int top, int left, int bottom, int right)'''
    def __init__(self, other):
        '''void QTableWidgetSelectionRange.__init__(QTableWidgetSelectionRange other)'''
    def columnCount(self):
        '''int QTableWidgetSelectionRange.columnCount()'''
        return int()
    def rowCount(self):
        '''int QTableWidgetSelectionRange.rowCount()'''
        return int()
    def rightColumn(self):
        '''int QTableWidgetSelectionRange.rightColumn()'''
        return int()
    def leftColumn(self):
        '''int QTableWidgetSelectionRange.leftColumn()'''
        return int()
    def bottomRow(self):
        '''int QTableWidgetSelectionRange.bottomRow()'''
        return int()
    def topRow(self):
        '''int QTableWidgetSelectionRange.topRow()'''
        return int()


class QTableWidgetItem():
    """"""
    # Enum QTableWidgetItem.ItemType
    Type = 0
    UserType = 0

    def __init__(self, type = None):
        '''void QTableWidgetItem.__init__(int type = QTableWidgetItem.Type)'''
    def __init__(self, text, type = None):
        '''void QTableWidgetItem.__init__(str text, int type = QTableWidgetItem.Type)'''
    def __init__(self, icon, text, type = None):
        '''void QTableWidgetItem.__init__(QIcon icon, str text, int type = QTableWidgetItem.Type)'''
    def __init__(self, other):
        '''void QTableWidgetItem.__init__(QTableWidgetItem other)'''
    def __ge__(self, other):
        '''bool QTableWidgetItem.__ge__(QTableWidgetItem other)'''
        return bool()
    def isSelected(self):
        '''bool QTableWidgetItem.isSelected()'''
        return bool()
    def setSelected(self, aselect):
        '''void QTableWidgetItem.setSelected(bool aselect)'''
    def column(self):
        '''int QTableWidgetItem.column()'''
        return int()
    def row(self):
        '''int QTableWidgetItem.row()'''
        return int()
    def setForeground(self, brush):
        '''void QTableWidgetItem.setForeground(QBrush brush)'''
    def foreground(self):
        '''QBrush QTableWidgetItem.foreground()'''
        return QBrush()
    def setBackground(self, brush):
        '''void QTableWidgetItem.setBackground(QBrush brush)'''
    def background(self):
        '''QBrush QTableWidgetItem.background()'''
        return QBrush()
    def setSizeHint(self, size):
        '''void QTableWidgetItem.setSizeHint(QSize size)'''
    def sizeHint(self):
        '''QSize QTableWidgetItem.sizeHint()'''
        return QSize()
    def setFont(self, afont):
        '''void QTableWidgetItem.setFont(QFont afont)'''
    def setWhatsThis(self, awhatsThis):
        '''void QTableWidgetItem.setWhatsThis(str awhatsThis)'''
    def setToolTip(self, atoolTip):
        '''void QTableWidgetItem.setToolTip(str atoolTip)'''
    def setStatusTip(self, astatusTip):
        '''void QTableWidgetItem.setStatusTip(str astatusTip)'''
    def setIcon(self, aicon):
        '''void QTableWidgetItem.setIcon(QIcon aicon)'''
    def setText(self, atext):
        '''void QTableWidgetItem.setText(str atext)'''
    def setFlags(self, aflags):
        '''void QTableWidgetItem.setFlags(Qt.ItemFlags aflags)'''
    def type(self):
        '''int QTableWidgetItem.type()'''
        return int()
    def write(self, out):
        '''void QTableWidgetItem.write(QDataStream out)'''
    def read(self, in_):
        '''void QTableWidgetItem.read(QDataStream in)'''
    def __lt__(self, other):
        '''bool QTableWidgetItem.__lt__(QTableWidgetItem other)'''
        return bool()
    def setData(self, role, value):
        '''void QTableWidgetItem.setData(int role, QVariant value)'''
    def data(self, role):
        '''QVariant QTableWidgetItem.data(int role)'''
        return QVariant()
    def setCheckState(self, state):
        '''void QTableWidgetItem.setCheckState(Qt.CheckState state)'''
    def checkState(self):
        '''Qt.CheckState QTableWidgetItem.checkState()'''
        return Qt.CheckState()
    def setTextAlignment(self, alignment):
        '''void QTableWidgetItem.setTextAlignment(int alignment)'''
    def textAlignment(self):
        '''int QTableWidgetItem.textAlignment()'''
        return int()
    def font(self):
        '''QFont QTableWidgetItem.font()'''
        return QFont()
    def whatsThis(self):
        '''str QTableWidgetItem.whatsThis()'''
        return str()
    def toolTip(self):
        '''str QTableWidgetItem.toolTip()'''
        return str()
    def statusTip(self):
        '''str QTableWidgetItem.statusTip()'''
        return str()
    def icon(self):
        '''QIcon QTableWidgetItem.icon()'''
        return QIcon()
    def text(self):
        '''str QTableWidgetItem.text()'''
        return str()
    def flags(self):
        '''Qt.ItemFlags QTableWidgetItem.flags()'''
        return Qt.ItemFlags()
    def tableWidget(self):
        '''QTableWidget QTableWidgetItem.tableWidget()'''
        return QTableWidget()
    def clone(self):
        '''QTableWidgetItem QTableWidgetItem.clone()'''
        return QTableWidgetItem()


class QTableWidget(QTableView):
    """"""
    def __init__(self, parent = None):
        '''void QTableWidget.__init__(QWidget parent = None)'''
    def __init__(self, rows, columns, parent = None):
        '''void QTableWidget.__init__(int rows, int columns, QWidget parent = None)'''
    def dropEvent(self, event):
        '''void QTableWidget.dropEvent(QDropEvent event)'''
    def event(self, e):
        '''bool QTableWidget.event(QEvent e)'''
        return bool()
    def itemFromIndex(self, index):
        '''QTableWidgetItem QTableWidget.itemFromIndex(QModelIndex index)'''
        return QTableWidgetItem()
    def indexFromItem(self, item):
        '''QModelIndex QTableWidget.indexFromItem(QTableWidgetItem item)'''
        return QModelIndex()
    def items(self, data):
        '''list-of-QTableWidgetItem QTableWidget.items(QMimeData data)'''
        return [QTableWidgetItem()]
    def supportedDropActions(self):
        '''Qt.DropActions QTableWidget.supportedDropActions()'''
        return Qt.DropActions()
    def dropMimeData(self, row, column, data, action):
        '''bool QTableWidget.dropMimeData(int row, int column, QMimeData data, Qt.DropAction action)'''
        return bool()
    def mimeData(self, items):
        '''QMimeData QTableWidget.mimeData(list-of-QTableWidgetItem items)'''
        return QMimeData()
    def mimeTypes(self):
        '''list-of-str QTableWidget.mimeTypes()'''
        return [str()]
    currentCellChanged = pyqtSignal() # void currentCellChanged(int,int,int,int) - signal
    cellChanged = pyqtSignal() # void cellChanged(int,int) - signal
    cellEntered = pyqtSignal() # void cellEntered(int,int) - signal
    cellActivated = pyqtSignal() # void cellActivated(int,int) - signal
    cellDoubleClicked = pyqtSignal() # void cellDoubleClicked(int,int) - signal
    cellClicked = pyqtSignal() # void cellClicked(int,int) - signal
    cellPressed = pyqtSignal() # void cellPressed(int,int) - signal
    itemSelectionChanged = pyqtSignal() # void itemSelectionChanged() - signal
    currentItemChanged = pyqtSignal() # void currentItemChanged(QTableWidgetItem*,QTableWidgetItem*) - signal
    itemChanged = pyqtSignal() # void itemChanged(QTableWidgetItem*) - signal
    itemEntered = pyqtSignal() # void itemEntered(QTableWidgetItem*) - signal
    itemActivated = pyqtSignal() # void itemActivated(QTableWidgetItem*) - signal
    itemDoubleClicked = pyqtSignal() # void itemDoubleClicked(QTableWidgetItem*) - signal
    itemClicked = pyqtSignal() # void itemClicked(QTableWidgetItem*) - signal
    itemPressed = pyqtSignal() # void itemPressed(QTableWidgetItem*) - signal
    def clearContents(self):
        '''void QTableWidget.clearContents()'''
    def clear(self):
        '''void QTableWidget.clear()'''
    def removeColumn(self, column):
        '''void QTableWidget.removeColumn(int column)'''
    def removeRow(self, row):
        '''void QTableWidget.removeRow(int row)'''
    def insertColumn(self, column):
        '''void QTableWidget.insertColumn(int column)'''
    def insertRow(self, row):
        '''void QTableWidget.insertRow(int row)'''
    def scrollToItem(self, item, hint = None):
        '''void QTableWidget.scrollToItem(QTableWidgetItem item, QAbstractItemView.ScrollHint hint = QAbstractItemView.EnsureVisible)'''
    def setItemPrototype(self, item):
        '''void QTableWidget.setItemPrototype(QTableWidgetItem item)'''
    def itemPrototype(self):
        '''QTableWidgetItem QTableWidget.itemPrototype()'''
        return QTableWidgetItem()
    def visualItemRect(self, item):
        '''QRect QTableWidget.visualItemRect(QTableWidgetItem item)'''
        return QRect()
    def itemAt(self, p):
        '''QTableWidgetItem QTableWidget.itemAt(QPoint p)'''
        return QTableWidgetItem()
    def itemAt(self, ax, ay):
        '''QTableWidgetItem QTableWidget.itemAt(int ax, int ay)'''
        return QTableWidgetItem()
    def visualColumn(self, logicalColumn):
        '''int QTableWidget.visualColumn(int logicalColumn)'''
        return int()
    def visualRow(self, logicalRow):
        '''int QTableWidget.visualRow(int logicalRow)'''
        return int()
    def findItems(self, text, flags):
        '''list-of-QTableWidgetItem QTableWidget.findItems(str text, Qt.MatchFlags flags)'''
        return [QTableWidgetItem()]
    def selectedItems(self):
        '''list-of-QTableWidgetItem QTableWidget.selectedItems()'''
        return [QTableWidgetItem()]
    def selectedRanges(self):
        '''list-of-QTableWidgetSelectionRange QTableWidget.selectedRanges()'''
        return [QTableWidgetSelectionRange()]
    def setRangeSelected(self, range, select):
        '''void QTableWidget.setRangeSelected(QTableWidgetSelectionRange range, bool select)'''
    def removeCellWidget(self, arow, acolumn):
        '''void QTableWidget.removeCellWidget(int arow, int acolumn)'''
    def setCellWidget(self, row, column, widget):
        '''void QTableWidget.setCellWidget(int row, int column, QWidget widget)'''
    def cellWidget(self, row, column):
        '''QWidget QTableWidget.cellWidget(int row, int column)'''
        return QWidget()
    def closePersistentEditor(self, item):
        '''void QTableWidget.closePersistentEditor(QTableWidgetItem item)'''
    def openPersistentEditor(self, item):
        '''void QTableWidget.openPersistentEditor(QTableWidgetItem item)'''
    def editItem(self, item):
        '''void QTableWidget.editItem(QTableWidgetItem item)'''
    def isSortingEnabled(self):
        '''bool QTableWidget.isSortingEnabled()'''
        return bool()
    def setSortingEnabled(self, enable):
        '''void QTableWidget.setSortingEnabled(bool enable)'''
    def sortItems(self, column, order = None):
        '''void QTableWidget.sortItems(int column, Qt.SortOrder order = Qt.AscendingOrder)'''
    def setCurrentCell(self, row, column):
        '''void QTableWidget.setCurrentCell(int row, int column)'''
    def setCurrentCell(self, row, column, command):
        '''void QTableWidget.setCurrentCell(int row, int column, QItemSelectionModel.SelectionFlags command)'''
    def setCurrentItem(self, item):
        '''void QTableWidget.setCurrentItem(QTableWidgetItem item)'''
    def setCurrentItem(self, item, command):
        '''void QTableWidget.setCurrentItem(QTableWidgetItem item, QItemSelectionModel.SelectionFlags command)'''
    def currentItem(self):
        '''QTableWidgetItem QTableWidget.currentItem()'''
        return QTableWidgetItem()
    def currentColumn(self):
        '''int QTableWidget.currentColumn()'''
        return int()
    def currentRow(self):
        '''int QTableWidget.currentRow()'''
        return int()
    def setHorizontalHeaderLabels(self, labels):
        '''void QTableWidget.setHorizontalHeaderLabels(list-of-str labels)'''
    def setVerticalHeaderLabels(self, labels):
        '''void QTableWidget.setVerticalHeaderLabels(list-of-str labels)'''
    def takeHorizontalHeaderItem(self, column):
        '''QTableWidgetItem QTableWidget.takeHorizontalHeaderItem(int column)'''
        return QTableWidgetItem()
    def setHorizontalHeaderItem(self, column, item):
        '''void QTableWidget.setHorizontalHeaderItem(int column, QTableWidgetItem item)'''
    def horizontalHeaderItem(self, column):
        '''QTableWidgetItem QTableWidget.horizontalHeaderItem(int column)'''
        return QTableWidgetItem()
    def takeVerticalHeaderItem(self, row):
        '''QTableWidgetItem QTableWidget.takeVerticalHeaderItem(int row)'''
        return QTableWidgetItem()
    def setVerticalHeaderItem(self, row, item):
        '''void QTableWidget.setVerticalHeaderItem(int row, QTableWidgetItem item)'''
    def verticalHeaderItem(self, row):
        '''QTableWidgetItem QTableWidget.verticalHeaderItem(int row)'''
        return QTableWidgetItem()
    def takeItem(self, row, column):
        '''QTableWidgetItem QTableWidget.takeItem(int row, int column)'''
        return QTableWidgetItem()
    def setItem(self, row, column, item):
        '''void QTableWidget.setItem(int row, int column, QTableWidgetItem item)'''
    def item(self, row, column):
        '''QTableWidgetItem QTableWidget.item(int row, int column)'''
        return QTableWidgetItem()
    def column(self, item):
        '''int QTableWidget.column(QTableWidgetItem item)'''
        return int()
    def row(self, item):
        '''int QTableWidget.row(QTableWidgetItem item)'''
        return int()
    def columnCount(self):
        '''int QTableWidget.columnCount()'''
        return int()
    def setColumnCount(self, columns):
        '''void QTableWidget.setColumnCount(int columns)'''
    def rowCount(self):
        '''int QTableWidget.rowCount()'''
        return int()
    def setRowCount(self, rows):
        '''void QTableWidget.setRowCount(int rows)'''


class QTabWidget(QWidget):
    """"""
    # Enum QTabWidget.TabShape
    Rounded = 0
    Triangular = 0

    # Enum QTabWidget.TabPosition
    North = 0
    South = 0
    West = 0
    East = 0

    def __init__(self, parent = None):
        '''void QTabWidget.__init__(QWidget parent = None)'''
    def setTabBarAutoHide(self, enabled):
        '''void QTabWidget.setTabBarAutoHide(bool enabled)'''
    def tabBarAutoHide(self):
        '''bool QTabWidget.tabBarAutoHide()'''
        return bool()
    tabBarDoubleClicked = pyqtSignal() # void tabBarDoubleClicked(int) - signal
    tabBarClicked = pyqtSignal() # void tabBarClicked(int) - signal
    def hasHeightForWidth(self):
        '''bool QTabWidget.hasHeightForWidth()'''
        return bool()
    def heightForWidth(self, width):
        '''int QTabWidget.heightForWidth(int width)'''
        return int()
    tabCloseRequested = pyqtSignal() # void tabCloseRequested(int) - signal
    def setDocumentMode(self, set):
        '''void QTabWidget.setDocumentMode(bool set)'''
    def documentMode(self):
        '''bool QTabWidget.documentMode()'''
        return bool()
    def setMovable(self, movable):
        '''void QTabWidget.setMovable(bool movable)'''
    def isMovable(self):
        '''bool QTabWidget.isMovable()'''
        return bool()
    def setTabsClosable(self, closeable):
        '''void QTabWidget.setTabsClosable(bool closeable)'''
    def tabsClosable(self):
        '''bool QTabWidget.tabsClosable()'''
        return bool()
    def setUsesScrollButtons(self, useButtons):
        '''void QTabWidget.setUsesScrollButtons(bool useButtons)'''
    def usesScrollButtons(self):
        '''bool QTabWidget.usesScrollButtons()'''
        return bool()
    def setIconSize(self, size):
        '''void QTabWidget.setIconSize(QSize size)'''
    def iconSize(self):
        '''QSize QTabWidget.iconSize()'''
        return QSize()
    def setElideMode(self):
        '''Qt.TextElideMode QTabWidget.setElideMode()'''
        return Qt.TextElideMode()
    def elideMode(self):
        '''Qt.TextElideMode QTabWidget.elideMode()'''
        return Qt.TextElideMode()
    def changeEvent(self):
        '''QEvent QTabWidget.changeEvent()'''
        return QEvent()
    def tabBar(self):
        '''QTabBar QTabWidget.tabBar()'''
        return QTabBar()
    def setTabBar(self):
        '''QTabBar QTabWidget.setTabBar()'''
        return QTabBar()
    def paintEvent(self):
        '''QPaintEvent QTabWidget.paintEvent()'''
        return QPaintEvent()
    def keyPressEvent(self):
        '''QKeyEvent QTabWidget.keyPressEvent()'''
        return QKeyEvent()
    def resizeEvent(self):
        '''QResizeEvent QTabWidget.resizeEvent()'''
        return QResizeEvent()
    def showEvent(self):
        '''QShowEvent QTabWidget.showEvent()'''
        return QShowEvent()
    def event(self):
        '''QEvent QTabWidget.event()'''
        return QEvent()
    def tabRemoved(self, index):
        '''void QTabWidget.tabRemoved(int index)'''
    def tabInserted(self, index):
        '''void QTabWidget.tabInserted(int index)'''
    def initStyleOption(self, option):
        '''void QTabWidget.initStyleOption(QStyleOptionTabWidgetFrame option)'''
    currentChanged = pyqtSignal() # void currentChanged(int) - signal
    def setCurrentWidget(self, widget):
        '''void QTabWidget.setCurrentWidget(QWidget widget)'''
    def setCurrentIndex(self, index):
        '''void QTabWidget.setCurrentIndex(int index)'''
    def cornerWidget(self, corner = None):
        '''QWidget QTabWidget.cornerWidget(Qt.Corner corner = Qt.TopRightCorner)'''
        return QWidget()
    def setCornerWidget(self, widget, corner = None):
        '''void QTabWidget.setCornerWidget(QWidget widget, Qt.Corner corner = Qt.TopRightCorner)'''
    def minimumSizeHint(self):
        '''QSize QTabWidget.minimumSizeHint()'''
        return QSize()
    def sizeHint(self):
        '''QSize QTabWidget.sizeHint()'''
        return QSize()
    def setTabShape(self, s):
        '''void QTabWidget.setTabShape(QTabWidget.TabShape s)'''
    def tabShape(self):
        '''QTabWidget.TabShape QTabWidget.tabShape()'''
        return QTabWidget.TabShape()
    def setTabPosition(self):
        '''QTabWidget.TabPosition QTabWidget.setTabPosition()'''
        return QTabWidget.TabPosition()
    def tabPosition(self):
        '''QTabWidget.TabPosition QTabWidget.tabPosition()'''
        return QTabWidget.TabPosition()
    def __len__(self):
        ''' QTabWidget.__len__()'''
        return ()
    def count(self):
        '''int QTabWidget.count()'''
        return int()
    def indexOf(self, widget):
        '''int QTabWidget.indexOf(QWidget widget)'''
        return int()
    def widget(self, index):
        '''QWidget QTabWidget.widget(int index)'''
        return QWidget()
    def currentWidget(self):
        '''QWidget QTabWidget.currentWidget()'''
        return QWidget()
    def currentIndex(self):
        '''int QTabWidget.currentIndex()'''
        return int()
    def tabWhatsThis(self, index):
        '''str QTabWidget.tabWhatsThis(int index)'''
        return str()
    def setTabWhatsThis(self, index, text):
        '''void QTabWidget.setTabWhatsThis(int index, str text)'''
    def tabToolTip(self, index):
        '''str QTabWidget.tabToolTip(int index)'''
        return str()
    def setTabToolTip(self, index, tip):
        '''void QTabWidget.setTabToolTip(int index, str tip)'''
    def setTabIcon(self, index, icon):
        '''void QTabWidget.setTabIcon(int index, QIcon icon)'''
    def tabIcon(self, index):
        '''QIcon QTabWidget.tabIcon(int index)'''
        return QIcon()
    def setTabText(self, index):
        '''str QTabWidget.setTabText(int index)'''
        return str()
    def tabText(self, index):
        '''str QTabWidget.tabText(int index)'''
        return str()
    def setTabEnabled(self, index):
        '''bool QTabWidget.setTabEnabled(int index)'''
        return bool()
    def isTabEnabled(self, index):
        '''bool QTabWidget.isTabEnabled(int index)'''
        return bool()
    def removeTab(self, index):
        '''void QTabWidget.removeTab(int index)'''
    def insertTab(self, index, widget):
        '''str QTabWidget.insertTab(int index, QWidget widget)'''
        return str()
    def insertTab(self, index, widget, icon, label):
        '''int QTabWidget.insertTab(int index, QWidget widget, QIcon icon, str label)'''
        return int()
    def addTab(self, widget):
        '''str QTabWidget.addTab(QWidget widget)'''
        return str()
    def addTab(self, widget, icon, label):
        '''int QTabWidget.addTab(QWidget widget, QIcon icon, str label)'''
        return int()
    def clear(self):
        '''void QTabWidget.clear()'''


class QTextEdit(QAbstractScrollArea):
    """"""
    # Enum QTextEdit.AutoFormattingFlag
    AutoNone = 0
    AutoBulletList = 0
    AutoAll = 0

    # Enum QTextEdit.LineWrapMode
    NoWrap = 0
    WidgetWidth = 0
    FixedPixelWidth = 0
    FixedColumnWidth = 0

    def __init__(self, parent = None):
        '''void QTextEdit.__init__(QWidget parent = None)'''
    def __init__(self, text, parent = None):
        '''void QTextEdit.__init__(str text, QWidget parent = None)'''
    def placeholderText(self):
        '''str QTextEdit.placeholderText()'''
        return str()
    def setPlaceholderText(self, placeholderText):
        '''void QTextEdit.setPlaceholderText(str placeholderText)'''
    def setTextBackgroundColor(self, c):
        '''void QTextEdit.setTextBackgroundColor(QColor c)'''
    def textBackgroundColor(self):
        '''QColor QTextEdit.textBackgroundColor()'''
        return QColor()
    def scrollContentsBy(self, dx, dy):
        '''void QTextEdit.scrollContentsBy(int dx, int dy)'''
    def inputMethodQuery(self, property):
        '''QVariant QTextEdit.inputMethodQuery(Qt.InputMethodQuery property)'''
        return QVariant()
    def inputMethodQuery(self, query, argument):
        '''QVariant QTextEdit.inputMethodQuery(Qt.InputMethodQuery query, QVariant argument)'''
        return QVariant()
    def inputMethodEvent(self):
        '''QInputMethodEvent QTextEdit.inputMethodEvent()'''
        return QInputMethodEvent()
    def insertFromMimeData(self, source):
        '''void QTextEdit.insertFromMimeData(QMimeData source)'''
    def canInsertFromMimeData(self, source):
        '''bool QTextEdit.canInsertFromMimeData(QMimeData source)'''
        return bool()
    def createMimeDataFromSelection(self):
        '''QMimeData QTextEdit.createMimeDataFromSelection()'''
        return QMimeData()
    def wheelEvent(self, e):
        '''void QTextEdit.wheelEvent(QWheelEvent e)'''
    def changeEvent(self, e):
        '''void QTextEdit.changeEvent(QEvent e)'''
    def showEvent(self):
        '''QShowEvent QTextEdit.showEvent()'''
        return QShowEvent()
    def focusOutEvent(self, e):
        '''void QTextEdit.focusOutEvent(QFocusEvent e)'''
    def focusInEvent(self, e):
        '''void QTextEdit.focusInEvent(QFocusEvent e)'''
    def dropEvent(self, e):
        '''void QTextEdit.dropEvent(QDropEvent e)'''
    def dragMoveEvent(self, e):
        '''void QTextEdit.dragMoveEvent(QDragMoveEvent e)'''
    def dragLeaveEvent(self, e):
        '''void QTextEdit.dragLeaveEvent(QDragLeaveEvent e)'''
    def dragEnterEvent(self, e):
        '''void QTextEdit.dragEnterEvent(QDragEnterEvent e)'''
    def contextMenuEvent(self, e):
        '''void QTextEdit.contextMenuEvent(QContextMenuEvent e)'''
    def focusNextPrevChild(self, next):
        '''bool QTextEdit.focusNextPrevChild(bool next)'''
        return bool()
    def mouseDoubleClickEvent(self, e):
        '''void QTextEdit.mouseDoubleClickEvent(QMouseEvent e)'''
    def mouseReleaseEvent(self, e):
        '''void QTextEdit.mouseReleaseEvent(QMouseEvent e)'''
    def mouseMoveEvent(self, e):
        '''void QTextEdit.mouseMoveEvent(QMouseEvent e)'''
    def mousePressEvent(self, e):
        '''void QTextEdit.mousePressEvent(QMouseEvent e)'''
    def paintEvent(self, e):
        '''void QTextEdit.paintEvent(QPaintEvent e)'''
    def resizeEvent(self):
        '''QResizeEvent QTextEdit.resizeEvent()'''
        return QResizeEvent()
    def keyReleaseEvent(self, e):
        '''void QTextEdit.keyReleaseEvent(QKeyEvent e)'''
    def keyPressEvent(self, e):
        '''void QTextEdit.keyPressEvent(QKeyEvent e)'''
    def timerEvent(self, e):
        '''void QTextEdit.timerEvent(QTimerEvent e)'''
    def event(self, e):
        '''bool QTextEdit.event(QEvent e)'''
        return bool()
    cursorPositionChanged = pyqtSignal() # void cursorPositionChanged() - signal
    selectionChanged = pyqtSignal() # void selectionChanged() - signal
    copyAvailable = pyqtSignal() # void copyAvailable(bool) - signal
    currentCharFormatChanged = pyqtSignal() # void currentCharFormatChanged(const QTextCharFormatamp;) - signal
    redoAvailable = pyqtSignal() # void redoAvailable(bool) - signal
    undoAvailable = pyqtSignal() # void undoAvailable(bool) - signal
    textChanged = pyqtSignal() # void textChanged() - signal
    def zoomOut(self, range = 1):
        '''void QTextEdit.zoomOut(int range = 1)'''
    def zoomIn(self, range = 1):
        '''void QTextEdit.zoomIn(int range = 1)'''
    def undo(self):
        '''void QTextEdit.undo()'''
    def redo(self):
        '''void QTextEdit.redo()'''
    def scrollToAnchor(self, name):
        '''void QTextEdit.scrollToAnchor(str name)'''
    def insertHtml(self, text):
        '''void QTextEdit.insertHtml(str text)'''
    def insertPlainText(self, text):
        '''void QTextEdit.insertPlainText(str text)'''
    def selectAll(self):
        '''void QTextEdit.selectAll()'''
    def clear(self):
        '''void QTextEdit.clear()'''
    def paste(self):
        '''void QTextEdit.paste()'''
    def copy(self):
        '''void QTextEdit.copy()'''
    def cut(self):
        '''void QTextEdit.cut()'''
    def setHtml(self, text):
        '''void QTextEdit.setHtml(str text)'''
    def setPlainText(self, text):
        '''void QTextEdit.setPlainText(str text)'''
    def setAlignment(self, a):
        '''void QTextEdit.setAlignment(Qt.Alignment a)'''
    def setCurrentFont(self, f):
        '''void QTextEdit.setCurrentFont(QFont f)'''
    def setTextColor(self, c):
        '''void QTextEdit.setTextColor(QColor c)'''
    def setText(self, text):
        '''void QTextEdit.setText(str text)'''
    def setFontItalic(self, b):
        '''void QTextEdit.setFontItalic(bool b)'''
    def setFontUnderline(self, b):
        '''void QTextEdit.setFontUnderline(bool b)'''
    def setFontWeight(self, w):
        '''void QTextEdit.setFontWeight(int w)'''
    def setFontFamily(self, fontFamily):
        '''void QTextEdit.setFontFamily(str fontFamily)'''
    def setFontPointSize(self, s):
        '''void QTextEdit.setFontPointSize(float s)'''
    def print_(self, printer):
        '''void QTextEdit.print_(QPagedPaintDevice printer)'''
    def moveCursor(self, operation, mode = None):
        '''void QTextEdit.moveCursor(QTextCursor.MoveOperation operation, QTextCursor.MoveMode mode = QTextCursor.MoveAnchor)'''
    def canPaste(self):
        '''bool QTextEdit.canPaste()'''
        return bool()
    def extraSelections(self):
        '''list-of-QTextEdit.ExtraSelection QTextEdit.extraSelections()'''
        return [QTextEdit.ExtraSelection()]
    def setExtraSelections(self, selections):
        '''void QTextEdit.setExtraSelections(list-of-QTextEdit.ExtraSelection selections)'''
    def cursorWidth(self):
        '''int QTextEdit.cursorWidth()'''
        return int()
    def setCursorWidth(self, width):
        '''void QTextEdit.setCursorWidth(int width)'''
    def textInteractionFlags(self):
        '''Qt.TextInteractionFlags QTextEdit.textInteractionFlags()'''
        return Qt.TextInteractionFlags()
    def setTextInteractionFlags(self, flags):
        '''void QTextEdit.setTextInteractionFlags(Qt.TextInteractionFlags flags)'''
    def setAcceptRichText(self, accept):
        '''void QTextEdit.setAcceptRichText(bool accept)'''
    def acceptRichText(self):
        '''bool QTextEdit.acceptRichText()'''
        return bool()
    def setTabStopWidth(self, width):
        '''void QTextEdit.setTabStopWidth(int width)'''
    def tabStopWidth(self):
        '''int QTextEdit.tabStopWidth()'''
        return int()
    def setOverwriteMode(self, overwrite):
        '''void QTextEdit.setOverwriteMode(bool overwrite)'''
    def overwriteMode(self):
        '''bool QTextEdit.overwriteMode()'''
        return bool()
    def anchorAt(self, pos):
        '''str QTextEdit.anchorAt(QPoint pos)'''
        return str()
    def cursorRect(self, cursor):
        '''QRect QTextEdit.cursorRect(QTextCursor cursor)'''
        return QRect()
    def cursorRect(self):
        '''QRect QTextEdit.cursorRect()'''
        return QRect()
    def cursorForPosition(self, pos):
        '''QTextCursor QTextEdit.cursorForPosition(QPoint pos)'''
        return QTextCursor()
    def createStandardContextMenu(self):
        '''QMenu QTextEdit.createStandardContextMenu()'''
        return QMenu()
    def createStandardContextMenu(self, position):
        '''QMenu QTextEdit.createStandardContextMenu(QPoint position)'''
        return QMenu()
    def loadResource(self, type, name):
        '''QVariant QTextEdit.loadResource(int type, QUrl name)'''
        return QVariant()
    def ensureCursorVisible(self):
        '''void QTextEdit.ensureCursorVisible()'''
    def append(self, text):
        '''void QTextEdit.append(str text)'''
    def toHtml(self):
        '''str QTextEdit.toHtml()'''
        return str()
    def toPlainText(self):
        '''str QTextEdit.toPlainText()'''
        return str()
    def find(self, exp, options = 0):
        '''bool QTextEdit.find(str exp, QTextDocument.FindFlags options = 0)'''
        return bool()
    def find(self, exp, options = 0):
        '''bool QTextEdit.find(QRegExp exp, QTextDocument.FindFlags options = 0)'''
        return bool()
    def setWordWrapMode(self, policy):
        '''void QTextEdit.setWordWrapMode(QTextOption.WrapMode policy)'''
    def wordWrapMode(self):
        '''QTextOption.WrapMode QTextEdit.wordWrapMode()'''
        return QTextOption.WrapMode()
    def setLineWrapColumnOrWidth(self, w):
        '''void QTextEdit.setLineWrapColumnOrWidth(int w)'''
    def lineWrapColumnOrWidth(self):
        '''int QTextEdit.lineWrapColumnOrWidth()'''
        return int()
    def setLineWrapMode(self, mode):
        '''void QTextEdit.setLineWrapMode(QTextEdit.LineWrapMode mode)'''
    def lineWrapMode(self):
        '''QTextEdit.LineWrapMode QTextEdit.lineWrapMode()'''
        return QTextEdit.LineWrapMode()
    def setUndoRedoEnabled(self, enable):
        '''void QTextEdit.setUndoRedoEnabled(bool enable)'''
    def isUndoRedoEnabled(self):
        '''bool QTextEdit.isUndoRedoEnabled()'''
        return bool()
    def documentTitle(self):
        '''str QTextEdit.documentTitle()'''
        return str()
    def setDocumentTitle(self, title):
        '''void QTextEdit.setDocumentTitle(str title)'''
    def setTabChangesFocus(self, b):
        '''void QTextEdit.setTabChangesFocus(bool b)'''
    def tabChangesFocus(self):
        '''bool QTextEdit.tabChangesFocus()'''
        return bool()
    def setAutoFormatting(self, features):
        '''void QTextEdit.setAutoFormatting(QTextEdit.AutoFormatting features)'''
    def autoFormatting(self):
        '''QTextEdit.AutoFormatting QTextEdit.autoFormatting()'''
        return QTextEdit.AutoFormatting()
    def currentCharFormat(self):
        '''QTextCharFormat QTextEdit.currentCharFormat()'''
        return QTextCharFormat()
    def setCurrentCharFormat(self, format):
        '''void QTextEdit.setCurrentCharFormat(QTextCharFormat format)'''
    def mergeCurrentCharFormat(self, modifier):
        '''void QTextEdit.mergeCurrentCharFormat(QTextCharFormat modifier)'''
    def alignment(self):
        '''Qt.Alignment QTextEdit.alignment()'''
        return Qt.Alignment()
    def currentFont(self):
        '''QFont QTextEdit.currentFont()'''
        return QFont()
    def textColor(self):
        '''QColor QTextEdit.textColor()'''
        return QColor()
    def fontItalic(self):
        '''bool QTextEdit.fontItalic()'''
        return bool()
    def fontUnderline(self):
        '''bool QTextEdit.fontUnderline()'''
        return bool()
    def fontWeight(self):
        '''int QTextEdit.fontWeight()'''
        return int()
    def fontFamily(self):
        '''str QTextEdit.fontFamily()'''
        return str()
    def fontPointSize(self):
        '''float QTextEdit.fontPointSize()'''
        return float()
    def setReadOnly(self, ro):
        '''void QTextEdit.setReadOnly(bool ro)'''
    def isReadOnly(self):
        '''bool QTextEdit.isReadOnly()'''
        return bool()
    def textCursor(self):
        '''QTextCursor QTextEdit.textCursor()'''
        return QTextCursor()
    def setTextCursor(self, cursor):
        '''void QTextEdit.setTextCursor(QTextCursor cursor)'''
    def document(self):
        '''QTextDocument QTextEdit.document()'''
        return QTextDocument()
    def setDocument(self, document):
        '''void QTextEdit.setDocument(QTextDocument document)'''
    class ExtraSelection():
        """"""
        cursor = None # QTextCursor - member
        format = None # QTextCharFormat - member
        def __init__(self):
            '''void QTextEdit.ExtraSelection.__init__()'''
        def __init__(self):
            '''QTextEdit.ExtraSelection QTextEdit.ExtraSelection.__init__()'''
            return QTextEdit.ExtraSelection()
    class AutoFormatting():
        """"""
        def __init__(self):
            '''QTextEdit.AutoFormatting QTextEdit.AutoFormatting.__init__()'''
            return QTextEdit.AutoFormatting()
        def __init__(self):
            '''int QTextEdit.AutoFormatting.__init__()'''
            return int()
        def __init__(self):
            '''void QTextEdit.AutoFormatting.__init__()'''
        def __bool__(self):
            '''int QTextEdit.AutoFormatting.__bool__()'''
            return int()
        def __ne__(self, f):
            '''bool QTextEdit.AutoFormatting.__ne__(QTextEdit.AutoFormatting f)'''
            return bool()
        def __eq__(self, f):
            '''bool QTextEdit.AutoFormatting.__eq__(QTextEdit.AutoFormatting f)'''
            return bool()
        def __invert__(self):
            '''QTextEdit.AutoFormatting QTextEdit.AutoFormatting.__invert__()'''
            return QTextEdit.AutoFormatting()
        def __and__(self, mask):
            '''QTextEdit.AutoFormatting QTextEdit.AutoFormatting.__and__(int mask)'''
            return QTextEdit.AutoFormatting()
        def __xor__(self, f):
            '''QTextEdit.AutoFormatting QTextEdit.AutoFormatting.__xor__(QTextEdit.AutoFormatting f)'''
            return QTextEdit.AutoFormatting()
        def __xor__(self, f):
            '''QTextEdit.AutoFormatting QTextEdit.AutoFormatting.__xor__(int f)'''
            return QTextEdit.AutoFormatting()
        def __or__(self, f):
            '''QTextEdit.AutoFormatting QTextEdit.AutoFormatting.__or__(QTextEdit.AutoFormatting f)'''
            return QTextEdit.AutoFormatting()
        def __or__(self, f):
            '''QTextEdit.AutoFormatting QTextEdit.AutoFormatting.__or__(int f)'''
            return QTextEdit.AutoFormatting()
        def __int__(self):
            '''int QTextEdit.AutoFormatting.__int__()'''
            return int()
        def __ixor__(self, f):
            '''QTextEdit.AutoFormatting QTextEdit.AutoFormatting.__ixor__(QTextEdit.AutoFormatting f)'''
            return QTextEdit.AutoFormatting()
        def __ior__(self, f):
            '''QTextEdit.AutoFormatting QTextEdit.AutoFormatting.__ior__(QTextEdit.AutoFormatting f)'''
            return QTextEdit.AutoFormatting()
        def __iand__(self, mask):
            '''QTextEdit.AutoFormatting QTextEdit.AutoFormatting.__iand__(int mask)'''
            return QTextEdit.AutoFormatting()


class QTextBrowser(QTextEdit):
    """"""
    def __init__(self, parent = None):
        '''void QTextBrowser.__init__(QWidget parent = None)'''
    historyChanged = pyqtSignal() # void historyChanged() - signal
    def forwardHistoryCount(self):
        '''int QTextBrowser.forwardHistoryCount()'''
        return int()
    def backwardHistoryCount(self):
        '''int QTextBrowser.backwardHistoryCount()'''
        return int()
    def historyUrl(self):
        '''int QTextBrowser.historyUrl()'''
        return int()
    def historyTitle(self):
        '''int QTextBrowser.historyTitle()'''
        return int()
    def setOpenLinks(self, open):
        '''void QTextBrowser.setOpenLinks(bool open)'''
    def openLinks(self):
        '''bool QTextBrowser.openLinks()'''
        return bool()
    def setOpenExternalLinks(self, open):
        '''void QTextBrowser.setOpenExternalLinks(bool open)'''
    def openExternalLinks(self):
        '''bool QTextBrowser.openExternalLinks()'''
        return bool()
    def clearHistory(self):
        '''void QTextBrowser.clearHistory()'''
    def isForwardAvailable(self):
        '''bool QTextBrowser.isForwardAvailable()'''
        return bool()
    def isBackwardAvailable(self):
        '''bool QTextBrowser.isBackwardAvailable()'''
        return bool()
    def paintEvent(self, e):
        '''void QTextBrowser.paintEvent(QPaintEvent e)'''
    def focusNextPrevChild(self, next):
        '''bool QTextBrowser.focusNextPrevChild(bool next)'''
        return bool()
    def focusOutEvent(self, ev):
        '''void QTextBrowser.focusOutEvent(QFocusEvent ev)'''
    def mouseReleaseEvent(self, ev):
        '''void QTextBrowser.mouseReleaseEvent(QMouseEvent ev)'''
    def mousePressEvent(self, ev):
        '''void QTextBrowser.mousePressEvent(QMouseEvent ev)'''
    def mouseMoveEvent(self, ev):
        '''void QTextBrowser.mouseMoveEvent(QMouseEvent ev)'''
    def keyPressEvent(self, ev):
        '''void QTextBrowser.keyPressEvent(QKeyEvent ev)'''
    def event(self, e):
        '''bool QTextBrowser.event(QEvent e)'''
        return bool()
    anchorClicked = pyqtSignal() # void anchorClicked(const QUrlamp;) - signal
    highlighted = pyqtSignal() # void highlighted(const QUrlamp;) - signal
    highlighted = pyqtSignal() # void highlighted(const QStringamp;) - signal
    sourceChanged = pyqtSignal() # void sourceChanged(const QUrlamp;) - signal
    forwardAvailable = pyqtSignal() # void forwardAvailable(bool) - signal
    backwardAvailable = pyqtSignal() # void backwardAvailable(bool) - signal
    def reload(self):
        '''void QTextBrowser.reload()'''
    def home(self):
        '''void QTextBrowser.home()'''
    def forward(self):
        '''void QTextBrowser.forward()'''
    def backward(self):
        '''void QTextBrowser.backward()'''
    def setSource(self, name):
        '''void QTextBrowser.setSource(QUrl name)'''
    def loadResource(self, type, name):
        '''QVariant QTextBrowser.loadResource(int type, QUrl name)'''
        return QVariant()
    def setSearchPaths(self, paths):
        '''void QTextBrowser.setSearchPaths(list-of-str paths)'''
    def searchPaths(self):
        '''list-of-str QTextBrowser.searchPaths()'''
        return [str()]
    def source(self):
        '''QUrl QTextBrowser.source()'''
        return QUrl()


class QToolBar(QWidget):
    """"""
    def __init__(self, title, parent = None):
        '''void QToolBar.__init__(str title, QWidget parent = None)'''
    def __init__(self, parent = None):
        '''void QToolBar.__init__(QWidget parent = None)'''
    def isFloating(self):
        '''bool QToolBar.isFloating()'''
        return bool()
    def setFloatable(self, floatable):
        '''void QToolBar.setFloatable(bool floatable)'''
    def isFloatable(self):
        '''bool QToolBar.isFloatable()'''
        return bool()
    def event(self, event):
        '''bool QToolBar.event(QEvent event)'''
        return bool()
    def paintEvent(self, event):
        '''void QToolBar.paintEvent(QPaintEvent event)'''
    def changeEvent(self, event):
        '''void QToolBar.changeEvent(QEvent event)'''
    def actionEvent(self, event):
        '''void QToolBar.actionEvent(QActionEvent event)'''
    def initStyleOption(self, option):
        '''void QToolBar.initStyleOption(QStyleOptionToolBar option)'''
    visibilityChanged = pyqtSignal() # void visibilityChanged(bool) - signal
    topLevelChanged = pyqtSignal() # void topLevelChanged(bool) - signal
    toolButtonStyleChanged = pyqtSignal() # void toolButtonStyleChanged(Qt::ToolButtonStyle) - signal
    iconSizeChanged = pyqtSignal() # void iconSizeChanged(const QSizeamp;) - signal
    orientationChanged = pyqtSignal() # void orientationChanged(Qt::Orientation) - signal
    allowedAreasChanged = pyqtSignal() # void allowedAreasChanged(Qt::ToolBarAreas) - signal
    movableChanged = pyqtSignal() # void movableChanged(bool) - signal
    actionTriggered = pyqtSignal() # void actionTriggered(QAction*) - signal
    def setToolButtonStyle(self, toolButtonStyle):
        '''void QToolBar.setToolButtonStyle(Qt.ToolButtonStyle toolButtonStyle)'''
    def setIconSize(self, iconSize):
        '''void QToolBar.setIconSize(QSize iconSize)'''
    def widgetForAction(self, action):
        '''QWidget QToolBar.widgetForAction(QAction action)'''
        return QWidget()
    def toolButtonStyle(self):
        '''Qt.ToolButtonStyle QToolBar.toolButtonStyle()'''
        return Qt.ToolButtonStyle()
    def iconSize(self):
        '''QSize QToolBar.iconSize()'''
        return QSize()
    def toggleViewAction(self):
        '''QAction QToolBar.toggleViewAction()'''
        return QAction()
    def actionAt(self, p):
        '''QAction QToolBar.actionAt(QPoint p)'''
        return QAction()
    def actionAt(self, ax, ay):
        '''QAction QToolBar.actionAt(int ax, int ay)'''
        return QAction()
    def actionGeometry(self, action):
        '''QRect QToolBar.actionGeometry(QAction action)'''
        return QRect()
    def insertWidget(self, before, widget):
        '''QAction QToolBar.insertWidget(QAction before, QWidget widget)'''
        return QAction()
    def addWidget(self, widget):
        '''QAction QToolBar.addWidget(QWidget widget)'''
        return QAction()
    def insertSeparator(self, before):
        '''QAction QToolBar.insertSeparator(QAction before)'''
        return QAction()
    def addSeparator(self):
        '''QAction QToolBar.addSeparator()'''
        return QAction()
    def addAction(self, action):
        '''void QToolBar.addAction(QAction action)'''
    def addAction(self, text):
        '''QAction QToolBar.addAction(str text)'''
        return QAction()
    def addAction(self, icon, text):
        '''QAction QToolBar.addAction(QIcon icon, str text)'''
        return QAction()
    def addAction(self, text, slot):
        '''QAction QToolBar.addAction(str text, slot slot)'''
        return QAction()
    def addAction(self, icon, text, slot):
        '''QAction QToolBar.addAction(QIcon icon, str text, slot slot)'''
        return QAction()
    def clear(self):
        '''void QToolBar.clear()'''
    def orientation(self):
        '''Qt.Orientation QToolBar.orientation()'''
        return Qt.Orientation()
    def setOrientation(self, orientation):
        '''void QToolBar.setOrientation(Qt.Orientation orientation)'''
    def isAreaAllowed(self, area):
        '''bool QToolBar.isAreaAllowed(Qt.ToolBarArea area)'''
        return bool()
    def allowedAreas(self):
        '''Qt.ToolBarAreas QToolBar.allowedAreas()'''
        return Qt.ToolBarAreas()
    def setAllowedAreas(self, areas):
        '''void QToolBar.setAllowedAreas(Qt.ToolBarAreas areas)'''
    def isMovable(self):
        '''bool QToolBar.isMovable()'''
        return bool()
    def setMovable(self, movable):
        '''void QToolBar.setMovable(bool movable)'''


class QToolBox(QFrame):
    """"""
    def __init__(self, parent = None, flags = 0):
        '''void QToolBox.__init__(QWidget parent = None, Qt.WindowFlags flags = 0)'''
    def changeEvent(self):
        '''QEvent QToolBox.changeEvent()'''
        return QEvent()
    def showEvent(self, e):
        '''void QToolBox.showEvent(QShowEvent e)'''
    def event(self, e):
        '''bool QToolBox.event(QEvent e)'''
        return bool()
    def itemRemoved(self, index):
        '''void QToolBox.itemRemoved(int index)'''
    def itemInserted(self, index):
        '''void QToolBox.itemInserted(int index)'''
    currentChanged = pyqtSignal() # void currentChanged(int) - signal
    def setCurrentWidget(self, widget):
        '''void QToolBox.setCurrentWidget(QWidget widget)'''
    def setCurrentIndex(self, index):
        '''void QToolBox.setCurrentIndex(int index)'''
    def __len__(self):
        ''' QToolBox.__len__()'''
        return ()
    def count(self):
        '''int QToolBox.count()'''
        return int()
    def indexOf(self, widget):
        '''int QToolBox.indexOf(QWidget widget)'''
        return int()
    def widget(self, index):
        '''QWidget QToolBox.widget(int index)'''
        return QWidget()
    def currentWidget(self):
        '''QWidget QToolBox.currentWidget()'''
        return QWidget()
    def currentIndex(self):
        '''int QToolBox.currentIndex()'''
        return int()
    def itemToolTip(self, index):
        '''str QToolBox.itemToolTip(int index)'''
        return str()
    def setItemToolTip(self, index, toolTip):
        '''void QToolBox.setItemToolTip(int index, str toolTip)'''
    def itemIcon(self, index):
        '''QIcon QToolBox.itemIcon(int index)'''
        return QIcon()
    def setItemIcon(self, index, icon):
        '''void QToolBox.setItemIcon(int index, QIcon icon)'''
    def itemText(self, index):
        '''str QToolBox.itemText(int index)'''
        return str()
    def setItemText(self, index, text):
        '''void QToolBox.setItemText(int index, str text)'''
    def isItemEnabled(self, index):
        '''bool QToolBox.isItemEnabled(int index)'''
        return bool()
    def setItemEnabled(self, index, enabled):
        '''void QToolBox.setItemEnabled(int index, bool enabled)'''
    def removeItem(self, index):
        '''void QToolBox.removeItem(int index)'''
    def insertItem(self, index, item, text):
        '''int QToolBox.insertItem(int index, QWidget item, str text)'''
        return int()
    def insertItem(self, index, widget, icon, text):
        '''int QToolBox.insertItem(int index, QWidget widget, QIcon icon, str text)'''
        return int()
    def addItem(self, item, text):
        '''int QToolBox.addItem(QWidget item, str text)'''
        return int()
    def addItem(self, item, iconSet, text):
        '''int QToolBox.addItem(QWidget item, QIcon iconSet, str text)'''
        return int()


class QToolButton(QAbstractButton):
    """"""
    # Enum QToolButton.ToolButtonPopupMode
    DelayedPopup = 0
    MenuButtonPopup = 0
    InstantPopup = 0

    def __init__(self, parent = None):
        '''void QToolButton.__init__(QWidget parent = None)'''
    def hitButton(self, pos):
        '''bool QToolButton.hitButton(QPoint pos)'''
        return bool()
    def nextCheckState(self):
        '''void QToolButton.nextCheckState()'''
    def mouseReleaseEvent(self):
        '''QMouseEvent QToolButton.mouseReleaseEvent()'''
        return QMouseEvent()
    def changeEvent(self):
        '''QEvent QToolButton.changeEvent()'''
        return QEvent()
    def timerEvent(self):
        '''QTimerEvent QToolButton.timerEvent()'''
        return QTimerEvent()
    def leaveEvent(self):
        '''QEvent QToolButton.leaveEvent()'''
        return QEvent()
    def enterEvent(self):
        '''QEvent QToolButton.enterEvent()'''
        return QEvent()
    def actionEvent(self):
        '''QActionEvent QToolButton.actionEvent()'''
        return QActionEvent()
    def paintEvent(self):
        '''QPaintEvent QToolButton.paintEvent()'''
        return QPaintEvent()
    def mousePressEvent(self):
        '''QMouseEvent QToolButton.mousePressEvent()'''
        return QMouseEvent()
    def event(self, e):
        '''bool QToolButton.event(QEvent e)'''
        return bool()
    def initStyleOption(self, option):
        '''void QToolButton.initStyleOption(QStyleOptionToolButton option)'''
    triggered = pyqtSignal() # void triggered(QAction*) - signal
    def setDefaultAction(self):
        '''QAction QToolButton.setDefaultAction()'''
        return QAction()
    def setToolButtonStyle(self, style):
        '''void QToolButton.setToolButtonStyle(Qt.ToolButtonStyle style)'''
    def showMenu(self):
        '''void QToolButton.showMenu()'''
    def autoRaise(self):
        '''bool QToolButton.autoRaise()'''
        return bool()
    def setAutoRaise(self, enable):
        '''void QToolButton.setAutoRaise(bool enable)'''
    def defaultAction(self):
        '''QAction QToolButton.defaultAction()'''
        return QAction()
    def popupMode(self):
        '''QToolButton.ToolButtonPopupMode QToolButton.popupMode()'''
        return QToolButton.ToolButtonPopupMode()
    def setPopupMode(self, mode):
        '''void QToolButton.setPopupMode(QToolButton.ToolButtonPopupMode mode)'''
    def menu(self):
        '''QMenu QToolButton.menu()'''
        return QMenu()
    def setMenu(self, menu):
        '''void QToolButton.setMenu(QMenu menu)'''
    def setArrowType(self, type):
        '''void QToolButton.setArrowType(Qt.ArrowType type)'''
    def arrowType(self):
        '''Qt.ArrowType QToolButton.arrowType()'''
        return Qt.ArrowType()
    def toolButtonStyle(self):
        '''Qt.ToolButtonStyle QToolButton.toolButtonStyle()'''
        return Qt.ToolButtonStyle()
    def minimumSizeHint(self):
        '''QSize QToolButton.minimumSizeHint()'''
        return QSize()
    def sizeHint(self):
        '''QSize QToolButton.sizeHint()'''
        return QSize()


class QToolTip():
    """"""
    def __init__(self):
        '''QToolTip QToolTip.__init__()'''
        return QToolTip()
    def text(self):
        '''static str QToolTip.text()'''
        return str()
    def isVisible(self):
        '''static bool QToolTip.isVisible()'''
        return bool()
    def setFont(self):
        '''static QFont QToolTip.setFont()'''
        return QFont()
    def font(self):
        '''static QFont QToolTip.font()'''
        return QFont()
    def setPalette(self):
        '''static QPalette QToolTip.setPalette()'''
        return QPalette()
    def hideText(self):
        '''static void QToolTip.hideText()'''
    def palette(self):
        '''static QPalette QToolTip.palette()'''
        return QPalette()
    def showText(self, pos, text, widget = None):
        '''static void QToolTip.showText(QPoint pos, str text, QWidget widget = None)'''
    def showText(self, pos, text, w, rect):
        '''static void QToolTip.showText(QPoint pos, str text, QWidget w, QRect rect)'''
    def showText(self, pos, text, w, rect, msecShowTime):
        '''static void QToolTip.showText(QPoint pos, str text, QWidget w, QRect rect, int msecShowTime)'''


class QTreeView(QAbstractItemView):
    """"""
    def __init__(self, parent = None):
        '''void QTreeView.__init__(QWidget parent = None)'''
    def resetIndentation(self):
        '''void QTreeView.resetIndentation()'''
    def viewportSizeHint(self):
        '''QSize QTreeView.viewportSizeHint()'''
        return QSize()
    def treePosition(self):
        '''int QTreeView.treePosition()'''
        return int()
    def setTreePosition(self, logicalIndex):
        '''void QTreeView.setTreePosition(int logicalIndex)'''
    def setHeaderHidden(self, hide):
        '''void QTreeView.setHeaderHidden(bool hide)'''
    def isHeaderHidden(self):
        '''bool QTreeView.isHeaderHidden()'''
        return bool()
    def setExpandsOnDoubleClick(self, enable):
        '''void QTreeView.setExpandsOnDoubleClick(bool enable)'''
    def expandsOnDoubleClick(self):
        '''bool QTreeView.expandsOnDoubleClick()'''
        return bool()
    def currentChanged(self, current, previous):
        '''void QTreeView.currentChanged(QModelIndex current, QModelIndex previous)'''
    def selectionChanged(self, selected, deselected):
        '''void QTreeView.selectionChanged(QItemSelection selected, QItemSelection deselected)'''
    def rowHeight(self, index):
        '''int QTreeView.rowHeight(QModelIndex index)'''
        return int()
    def viewportEvent(self, event):
        '''bool QTreeView.viewportEvent(QEvent event)'''
        return bool()
    def dragMoveEvent(self, event):
        '''void QTreeView.dragMoveEvent(QDragMoveEvent event)'''
    def expandToDepth(self, depth):
        '''void QTreeView.expandToDepth(int depth)'''
    def wordWrap(self):
        '''bool QTreeView.wordWrap()'''
        return bool()
    def setWordWrap(self, on):
        '''void QTreeView.setWordWrap(bool on)'''
    def setFirstColumnSpanned(self, row, parent, span):
        '''void QTreeView.setFirstColumnSpanned(int row, QModelIndex parent, bool span)'''
    def isFirstColumnSpanned(self, row, parent):
        '''bool QTreeView.isFirstColumnSpanned(int row, QModelIndex parent)'''
        return bool()
    def setAutoExpandDelay(self, delay):
        '''void QTreeView.setAutoExpandDelay(int delay)'''
    def autoExpandDelay(self):
        '''int QTreeView.autoExpandDelay()'''
        return int()
    def sortByColumn(self, column, order):
        '''void QTreeView.sortByColumn(int column, Qt.SortOrder order)'''
    def allColumnsShowFocus(self):
        '''bool QTreeView.allColumnsShowFocus()'''
        return bool()
    def setAllColumnsShowFocus(self, enable):
        '''void QTreeView.setAllColumnsShowFocus(bool enable)'''
    def isAnimated(self):
        '''bool QTreeView.isAnimated()'''
        return bool()
    def setAnimated(self, enable):
        '''void QTreeView.setAnimated(bool enable)'''
    def isSortingEnabled(self):
        '''bool QTreeView.isSortingEnabled()'''
        return bool()
    def setSortingEnabled(self, enable):
        '''void QTreeView.setSortingEnabled(bool enable)'''
    def setColumnWidth(self, column, width):
        '''void QTreeView.setColumnWidth(int column, int width)'''
    def isIndexHidden(self, index):
        '''bool QTreeView.isIndexHidden(QModelIndex index)'''
        return bool()
    def horizontalScrollbarAction(self, action):
        '''void QTreeView.horizontalScrollbarAction(int action)'''
    def indexRowSizeHint(self, index):
        '''int QTreeView.indexRowSizeHint(QModelIndex index)'''
        return int()
    def sizeHintForColumn(self, column):
        '''int QTreeView.sizeHintForColumn(int column)'''
        return int()
    def updateGeometries(self):
        '''void QTreeView.updateGeometries()'''
    def keyPressEvent(self, event):
        '''void QTreeView.keyPressEvent(QKeyEvent event)'''
    def mouseDoubleClickEvent(self, e):
        '''void QTreeView.mouseDoubleClickEvent(QMouseEvent e)'''
    def mouseMoveEvent(self, event):
        '''void QTreeView.mouseMoveEvent(QMouseEvent event)'''
    def mousePressEvent(self, e):
        '''void QTreeView.mousePressEvent(QMouseEvent e)'''
    def drawTree(self, painter, region):
        '''void QTreeView.drawTree(QPainter painter, QRegion region)'''
    def drawBranches(self, painter, rect, index):
        '''void QTreeView.drawBranches(QPainter painter, QRect rect, QModelIndex index)'''
    def drawRow(self, painter, options, index):
        '''void QTreeView.drawRow(QPainter painter, QStyleOptionViewItem options, QModelIndex index)'''
    def mouseReleaseEvent(self, event):
        '''void QTreeView.mouseReleaseEvent(QMouseEvent event)'''
    def timerEvent(self, event):
        '''void QTreeView.timerEvent(QTimerEvent event)'''
    def paintEvent(self, e):
        '''void QTreeView.paintEvent(QPaintEvent e)'''
    def selectedIndexes(self):
        '''list-of-QModelIndex QTreeView.selectedIndexes()'''
        return [QModelIndex()]
    def visualRegionForSelection(self, selection):
        '''QRegion QTreeView.visualRegionForSelection(QItemSelection selection)'''
        return QRegion()
    def setSelection(self, rect, command):
        '''void QTreeView.setSelection(QRect rect, QItemSelectionModel.SelectionFlags command)'''
    def verticalOffset(self):
        '''int QTreeView.verticalOffset()'''
        return int()
    def horizontalOffset(self):
        '''int QTreeView.horizontalOffset()'''
        return int()
    def moveCursor(self, cursorAction, modifiers):
        '''QModelIndex QTreeView.moveCursor(QAbstractItemView.CursorAction cursorAction, Qt.KeyboardModifiers modifiers)'''
        return QModelIndex()
    def rowsAboutToBeRemoved(self, parent, start, end):
        '''void QTreeView.rowsAboutToBeRemoved(QModelIndex parent, int start, int end)'''
    def rowsInserted(self, parent, start, end):
        '''void QTreeView.rowsInserted(QModelIndex parent, int start, int end)'''
    def scrollContentsBy(self, dx, dy):
        '''void QTreeView.scrollContentsBy(int dx, int dy)'''
    def rowsRemoved(self, parent, first, last):
        '''void QTreeView.rowsRemoved(QModelIndex parent, int first, int last)'''
    def reexpand(self):
        '''void QTreeView.reexpand()'''
    def columnMoved(self):
        '''void QTreeView.columnMoved()'''
    def columnCountChanged(self, oldCount, newCount):
        '''void QTreeView.columnCountChanged(int oldCount, int newCount)'''
    def columnResized(self, column, oldSize, newSize):
        '''void QTreeView.columnResized(int column, int oldSize, int newSize)'''
    def selectAll(self):
        '''void QTreeView.selectAll()'''
    def resizeColumnToContents(self, column):
        '''void QTreeView.resizeColumnToContents(int column)'''
    def collapseAll(self):
        '''void QTreeView.collapseAll()'''
    def collapse(self, index):
        '''void QTreeView.collapse(QModelIndex index)'''
    def expandAll(self):
        '''void QTreeView.expandAll()'''
    def expand(self, index):
        '''void QTreeView.expand(QModelIndex index)'''
    def showColumn(self, column):
        '''void QTreeView.showColumn(int column)'''
    def hideColumn(self, column):
        '''void QTreeView.hideColumn(int column)'''
    def dataChanged(self, topLeft, bottomRight, roles = None):
        '''void QTreeView.dataChanged(QModelIndex topLeft, QModelIndex bottomRight, list-of-int roles = [])'''
    collapsed = pyqtSignal() # void collapsed(const QModelIndexamp;) - signal
    expanded = pyqtSignal() # void expanded(const QModelIndexamp;) - signal
    def reset(self):
        '''void QTreeView.reset()'''
    def indexBelow(self, index):
        '''QModelIndex QTreeView.indexBelow(QModelIndex index)'''
        return QModelIndex()
    def indexAbove(self, index):
        '''QModelIndex QTreeView.indexAbove(QModelIndex index)'''
        return QModelIndex()
    def indexAt(self, p):
        '''QModelIndex QTreeView.indexAt(QPoint p)'''
        return QModelIndex()
    def scrollTo(self, index, hint = None):
        '''void QTreeView.scrollTo(QModelIndex index, QAbstractItemView.ScrollHint hint = QAbstractItemView.EnsureVisible)'''
    def visualRect(self, index):
        '''QRect QTreeView.visualRect(QModelIndex index)'''
        return QRect()
    def keyboardSearch(self, search):
        '''void QTreeView.keyboardSearch(str search)'''
    def setExpanded(self, index, expand):
        '''void QTreeView.setExpanded(QModelIndex index, bool expand)'''
    def isExpanded(self, index):
        '''bool QTreeView.isExpanded(QModelIndex index)'''
        return bool()
    def setRowHidden(self, row, parent, hide):
        '''void QTreeView.setRowHidden(int row, QModelIndex parent, bool hide)'''
    def isRowHidden(self, row, parent):
        '''bool QTreeView.isRowHidden(int row, QModelIndex parent)'''
        return bool()
    def setColumnHidden(self, column, hide):
        '''void QTreeView.setColumnHidden(int column, bool hide)'''
    def isColumnHidden(self, column):
        '''bool QTreeView.isColumnHidden(int column)'''
        return bool()
    def columnAt(self, x):
        '''int QTreeView.columnAt(int x)'''
        return int()
    def columnWidth(self, column):
        '''int QTreeView.columnWidth(int column)'''
        return int()
    def columnViewportPosition(self, column):
        '''int QTreeView.columnViewportPosition(int column)'''
        return int()
    def setItemsExpandable(self, enable):
        '''void QTreeView.setItemsExpandable(bool enable)'''
    def itemsExpandable(self):
        '''bool QTreeView.itemsExpandable()'''
        return bool()
    def setUniformRowHeights(self, uniform):
        '''void QTreeView.setUniformRowHeights(bool uniform)'''
    def uniformRowHeights(self):
        '''bool QTreeView.uniformRowHeights()'''
        return bool()
    def setRootIsDecorated(self, show):
        '''void QTreeView.setRootIsDecorated(bool show)'''
    def rootIsDecorated(self):
        '''bool QTreeView.rootIsDecorated()'''
        return bool()
    def setIndentation(self, i):
        '''void QTreeView.setIndentation(int i)'''
    def indentation(self):
        '''int QTreeView.indentation()'''
        return int()
    def setHeader(self, header):
        '''void QTreeView.setHeader(QHeaderView header)'''
    def header(self):
        '''QHeaderView QTreeView.header()'''
        return QHeaderView()
    def setSelectionModel(self, selectionModel):
        '''void QTreeView.setSelectionModel(QItemSelectionModel selectionModel)'''
    def setRootIndex(self, index):
        '''void QTreeView.setRootIndex(QModelIndex index)'''
    def setModel(self, model):
        '''void QTreeView.setModel(QAbstractItemModel model)'''


class QTreeWidgetItem():
    """"""
    # Enum QTreeWidgetItem.ChildIndicatorPolicy
    ShowIndicator = 0
    DontShowIndicator = 0
    DontShowIndicatorWhenChildless = 0

    # Enum QTreeWidgetItem.ItemType
    Type = 0
    UserType = 0

    def __init__(self, type = None):
        '''void QTreeWidgetItem.__init__(int type = QTreeWidgetItem.Type)'''
    def __init__(self, strings, type = None):
        '''void QTreeWidgetItem.__init__(list-of-str strings, int type = QTreeWidgetItem.Type)'''
    def __init__(self, parent, type = None):
        '''void QTreeWidgetItem.__init__(QTreeWidget parent, int type = QTreeWidgetItem.Type)'''
    def __init__(self, parent, strings, type = None):
        '''void QTreeWidgetItem.__init__(QTreeWidget parent, list-of-str strings, int type = QTreeWidgetItem.Type)'''
    def __init__(self, parent, preceding, type = None):
        '''void QTreeWidgetItem.__init__(QTreeWidget parent, QTreeWidgetItem preceding, int type = QTreeWidgetItem.Type)'''
    def __init__(self, parent, type = None):
        '''void QTreeWidgetItem.__init__(QTreeWidgetItem parent, int type = QTreeWidgetItem.Type)'''
    def __init__(self, parent, strings, type = None):
        '''void QTreeWidgetItem.__init__(QTreeWidgetItem parent, list-of-str strings, int type = QTreeWidgetItem.Type)'''
    def __init__(self, parent, preceding, type = None):
        '''void QTreeWidgetItem.__init__(QTreeWidgetItem parent, QTreeWidgetItem preceding, int type = QTreeWidgetItem.Type)'''
    def __init__(self, other):
        '''void QTreeWidgetItem.__init__(QTreeWidgetItem other)'''
    def __ge__(self, other):
        '''bool QTreeWidgetItem.__ge__(QTreeWidgetItem other)'''
        return bool()
    def emitDataChanged(self):
        '''void QTreeWidgetItem.emitDataChanged()'''
    def isDisabled(self):
        '''bool QTreeWidgetItem.isDisabled()'''
        return bool()
    def setDisabled(self, disabled):
        '''void QTreeWidgetItem.setDisabled(bool disabled)'''
    def isFirstColumnSpanned(self):
        '''bool QTreeWidgetItem.isFirstColumnSpanned()'''
        return bool()
    def setFirstColumnSpanned(self, aspan):
        '''void QTreeWidgetItem.setFirstColumnSpanned(bool aspan)'''
    def removeChild(self, child):
        '''void QTreeWidgetItem.removeChild(QTreeWidgetItem child)'''
    def childIndicatorPolicy(self):
        '''QTreeWidgetItem.ChildIndicatorPolicy QTreeWidgetItem.childIndicatorPolicy()'''
        return QTreeWidgetItem.ChildIndicatorPolicy()
    def setChildIndicatorPolicy(self, policy):
        '''void QTreeWidgetItem.setChildIndicatorPolicy(QTreeWidgetItem.ChildIndicatorPolicy policy)'''
    def isExpanded(self):
        '''bool QTreeWidgetItem.isExpanded()'''
        return bool()
    def setExpanded(self, aexpand):
        '''void QTreeWidgetItem.setExpanded(bool aexpand)'''
    def isHidden(self):
        '''bool QTreeWidgetItem.isHidden()'''
        return bool()
    def setHidden(self, ahide):
        '''void QTreeWidgetItem.setHidden(bool ahide)'''
    def isSelected(self):
        '''bool QTreeWidgetItem.isSelected()'''
        return bool()
    def setSelected(self, aselect):
        '''void QTreeWidgetItem.setSelected(bool aselect)'''
    def sortChildren(self, column, order):
        '''void QTreeWidgetItem.sortChildren(int column, Qt.SortOrder order)'''
    def setForeground(self, column, brush):
        '''void QTreeWidgetItem.setForeground(int column, QBrush brush)'''
    def foreground(self, column):
        '''QBrush QTreeWidgetItem.foreground(int column)'''
        return QBrush()
    def setBackground(self, column, brush):
        '''void QTreeWidgetItem.setBackground(int column, QBrush brush)'''
    def background(self, column):
        '''QBrush QTreeWidgetItem.background(int column)'''
        return QBrush()
    def takeChildren(self):
        '''list-of-QTreeWidgetItem QTreeWidgetItem.takeChildren()'''
        return [QTreeWidgetItem()]
    def insertChildren(self, index, children):
        '''void QTreeWidgetItem.insertChildren(int index, list-of-QTreeWidgetItem children)'''
    def addChildren(self, children):
        '''void QTreeWidgetItem.addChildren(list-of-QTreeWidgetItem children)'''
    def setSizeHint(self, column, size):
        '''void QTreeWidgetItem.setSizeHint(int column, QSize size)'''
    def sizeHint(self, column):
        '''QSize QTreeWidgetItem.sizeHint(int column)'''
        return QSize()
    def indexOfChild(self, achild):
        '''int QTreeWidgetItem.indexOfChild(QTreeWidgetItem achild)'''
        return int()
    def setFont(self, column, afont):
        '''void QTreeWidgetItem.setFont(int column, QFont afont)'''
    def setWhatsThis(self, column, awhatsThis):
        '''void QTreeWidgetItem.setWhatsThis(int column, str awhatsThis)'''
    def setToolTip(self, column, atoolTip):
        '''void QTreeWidgetItem.setToolTip(int column, str atoolTip)'''
    def setStatusTip(self, column, astatusTip):
        '''void QTreeWidgetItem.setStatusTip(int column, str astatusTip)'''
    def setIcon(self, column, aicon):
        '''void QTreeWidgetItem.setIcon(int column, QIcon aicon)'''
    def setText(self, column, atext):
        '''void QTreeWidgetItem.setText(int column, str atext)'''
    def setFlags(self, aflags):
        '''void QTreeWidgetItem.setFlags(Qt.ItemFlags aflags)'''
    def type(self):
        '''int QTreeWidgetItem.type()'''
        return int()
    def takeChild(self, index):
        '''QTreeWidgetItem QTreeWidgetItem.takeChild(int index)'''
        return QTreeWidgetItem()
    def insertChild(self, index, child):
        '''void QTreeWidgetItem.insertChild(int index, QTreeWidgetItem child)'''
    def addChild(self, child):
        '''void QTreeWidgetItem.addChild(QTreeWidgetItem child)'''
    def columnCount(self):
        '''int QTreeWidgetItem.columnCount()'''
        return int()
    def childCount(self):
        '''int QTreeWidgetItem.childCount()'''
        return int()
    def child(self, index):
        '''QTreeWidgetItem QTreeWidgetItem.child(int index)'''
        return QTreeWidgetItem()
    def parent(self):
        '''QTreeWidgetItem QTreeWidgetItem.parent()'''
        return QTreeWidgetItem()
    def write(self, out):
        '''void QTreeWidgetItem.write(QDataStream out)'''
    def read(self, in_):
        '''void QTreeWidgetItem.read(QDataStream in)'''
    def __lt__(self, other):
        '''bool QTreeWidgetItem.__lt__(QTreeWidgetItem other)'''
        return bool()
    def setData(self, column, role, value):
        '''void QTreeWidgetItem.setData(int column, int role, QVariant value)'''
    def data(self, column, role):
        '''QVariant QTreeWidgetItem.data(int column, int role)'''
        return QVariant()
    def setCheckState(self, column, state):
        '''void QTreeWidgetItem.setCheckState(int column, Qt.CheckState state)'''
    def checkState(self, column):
        '''Qt.CheckState QTreeWidgetItem.checkState(int column)'''
        return Qt.CheckState()
    def setTextAlignment(self, column, alignment):
        '''void QTreeWidgetItem.setTextAlignment(int column, int alignment)'''
    def textAlignment(self, column):
        '''int QTreeWidgetItem.textAlignment(int column)'''
        return int()
    def font(self, column):
        '''QFont QTreeWidgetItem.font(int column)'''
        return QFont()
    def whatsThis(self, column):
        '''str QTreeWidgetItem.whatsThis(int column)'''
        return str()
    def toolTip(self, column):
        '''str QTreeWidgetItem.toolTip(int column)'''
        return str()
    def statusTip(self, column):
        '''str QTreeWidgetItem.statusTip(int column)'''
        return str()
    def icon(self, column):
        '''QIcon QTreeWidgetItem.icon(int column)'''
        return QIcon()
    def text(self, column):
        '''str QTreeWidgetItem.text(int column)'''
        return str()
    def flags(self):
        '''Qt.ItemFlags QTreeWidgetItem.flags()'''
        return Qt.ItemFlags()
    def treeWidget(self):
        '''QTreeWidget QTreeWidgetItem.treeWidget()'''
        return QTreeWidget()
    def clone(self):
        '''QTreeWidgetItem QTreeWidgetItem.clone()'''
        return QTreeWidgetItem()


class QTreeWidget(QTreeView):
    """"""
    def __init__(self, parent = None):
        '''void QTreeWidget.__init__(QWidget parent = None)'''
    def setSelectionModel(self, selectionModel):
        '''void QTreeWidget.setSelectionModel(QItemSelectionModel selectionModel)'''
    def removeItemWidget(self, item, column):
        '''void QTreeWidget.removeItemWidget(QTreeWidgetItem item, int column)'''
    def itemBelow(self, item):
        '''QTreeWidgetItem QTreeWidget.itemBelow(QTreeWidgetItem item)'''
        return QTreeWidgetItem()
    def itemAbove(self, item):
        '''QTreeWidgetItem QTreeWidget.itemAbove(QTreeWidgetItem item)'''
        return QTreeWidgetItem()
    def setFirstItemColumnSpanned(self, item, span):
        '''void QTreeWidget.setFirstItemColumnSpanned(QTreeWidgetItem item, bool span)'''
    def isFirstItemColumnSpanned(self, item):
        '''bool QTreeWidget.isFirstItemColumnSpanned(QTreeWidgetItem item)'''
        return bool()
    def setHeaderLabel(self, alabel):
        '''void QTreeWidget.setHeaderLabel(str alabel)'''
    def invisibleRootItem(self):
        '''QTreeWidgetItem QTreeWidget.invisibleRootItem()'''
        return QTreeWidgetItem()
    def dropEvent(self, event):
        '''void QTreeWidget.dropEvent(QDropEvent event)'''
    def event(self, e):
        '''bool QTreeWidget.event(QEvent e)'''
        return bool()
    def itemFromIndex(self, index):
        '''QTreeWidgetItem QTreeWidget.itemFromIndex(QModelIndex index)'''
        return QTreeWidgetItem()
    def indexFromItem(self, item, column = 0):
        '''QModelIndex QTreeWidget.indexFromItem(QTreeWidgetItem item, int column = 0)'''
        return QModelIndex()
    def supportedDropActions(self):
        '''Qt.DropActions QTreeWidget.supportedDropActions()'''
        return Qt.DropActions()
    def dropMimeData(self, parent, index, data, action):
        '''bool QTreeWidget.dropMimeData(QTreeWidgetItem parent, int index, QMimeData data, Qt.DropAction action)'''
        return bool()
    def mimeData(self, items):
        '''QMimeData QTreeWidget.mimeData(list-of-QTreeWidgetItem items)'''
        return QMimeData()
    def mimeTypes(self):
        '''list-of-str QTreeWidget.mimeTypes()'''
        return [str()]
    itemSelectionChanged = pyqtSignal() # void itemSelectionChanged() - signal
    currentItemChanged = pyqtSignal() # void currentItemChanged(QTreeWidgetItem*,QTreeWidgetItem*) - signal
    itemCollapsed = pyqtSignal() # void itemCollapsed(QTreeWidgetItem*) - signal
    itemExpanded = pyqtSignal() # void itemExpanded(QTreeWidgetItem*) - signal
    itemChanged = pyqtSignal() # void itemChanged(QTreeWidgetItem*,int) - signal
    itemEntered = pyqtSignal() # void itemEntered(QTreeWidgetItem*,int) - signal
    itemActivated = pyqtSignal() # void itemActivated(QTreeWidgetItem*,int) - signal
    itemDoubleClicked = pyqtSignal() # void itemDoubleClicked(QTreeWidgetItem*,int) - signal
    itemClicked = pyqtSignal() # void itemClicked(QTreeWidgetItem*,int) - signal
    itemPressed = pyqtSignal() # void itemPressed(QTreeWidgetItem*,int) - signal
    def clear(self):
        '''void QTreeWidget.clear()'''
    def collapseItem(self, item):
        '''void QTreeWidget.collapseItem(QTreeWidgetItem item)'''
    def expandItem(self, item):
        '''void QTreeWidget.expandItem(QTreeWidgetItem item)'''
    def scrollToItem(self, item, hint = None):
        '''void QTreeWidget.scrollToItem(QTreeWidgetItem item, QAbstractItemView.ScrollHint hint = QAbstractItemView.EnsureVisible)'''
    def findItems(self, text, flags, column = 0):
        '''list-of-QTreeWidgetItem QTreeWidget.findItems(str text, Qt.MatchFlags flags, int column = 0)'''
        return [QTreeWidgetItem()]
    def selectedItems(self):
        '''list-of-QTreeWidgetItem QTreeWidget.selectedItems()'''
        return [QTreeWidgetItem()]
    def setItemWidget(self, item, column, widget):
        '''void QTreeWidget.setItemWidget(QTreeWidgetItem item, int column, QWidget widget)'''
    def itemWidget(self, item, column):
        '''QWidget QTreeWidget.itemWidget(QTreeWidgetItem item, int column)'''
        return QWidget()
    def closePersistentEditor(self, item, column = 0):
        '''void QTreeWidget.closePersistentEditor(QTreeWidgetItem item, int column = 0)'''
    def openPersistentEditor(self, item, column = 0):
        '''void QTreeWidget.openPersistentEditor(QTreeWidgetItem item, int column = 0)'''
    def editItem(self, item, column = 0):
        '''void QTreeWidget.editItem(QTreeWidgetItem item, int column = 0)'''
    def sortItems(self, column, order):
        '''void QTreeWidget.sortItems(int column, Qt.SortOrder order)'''
    def sortColumn(self):
        '''int QTreeWidget.sortColumn()'''
        return int()
    def visualItemRect(self, item):
        '''QRect QTreeWidget.visualItemRect(QTreeWidgetItem item)'''
        return QRect()
    def itemAt(self, p):
        '''QTreeWidgetItem QTreeWidget.itemAt(QPoint p)'''
        return QTreeWidgetItem()
    def itemAt(self, ax, ay):
        '''QTreeWidgetItem QTreeWidget.itemAt(int ax, int ay)'''
        return QTreeWidgetItem()
    def setCurrentItem(self, item):
        '''void QTreeWidget.setCurrentItem(QTreeWidgetItem item)'''
    def setCurrentItem(self, item, column):
        '''void QTreeWidget.setCurrentItem(QTreeWidgetItem item, int column)'''
    def setCurrentItem(self, item, column, command):
        '''void QTreeWidget.setCurrentItem(QTreeWidgetItem item, int column, QItemSelectionModel.SelectionFlags command)'''
    def currentColumn(self):
        '''int QTreeWidget.currentColumn()'''
        return int()
    def currentItem(self):
        '''QTreeWidgetItem QTreeWidget.currentItem()'''
        return QTreeWidgetItem()
    def setHeaderLabels(self, labels):
        '''void QTreeWidget.setHeaderLabels(list-of-str labels)'''
    def setHeaderItem(self, item):
        '''void QTreeWidget.setHeaderItem(QTreeWidgetItem item)'''
    def headerItem(self):
        '''QTreeWidgetItem QTreeWidget.headerItem()'''
        return QTreeWidgetItem()
    def addTopLevelItems(self, items):
        '''void QTreeWidget.addTopLevelItems(list-of-QTreeWidgetItem items)'''
    def insertTopLevelItems(self, index, items):
        '''void QTreeWidget.insertTopLevelItems(int index, list-of-QTreeWidgetItem items)'''
    def indexOfTopLevelItem(self, item):
        '''int QTreeWidget.indexOfTopLevelItem(QTreeWidgetItem item)'''
        return int()
    def takeTopLevelItem(self, index):
        '''QTreeWidgetItem QTreeWidget.takeTopLevelItem(int index)'''
        return QTreeWidgetItem()
    def addTopLevelItem(self, item):
        '''void QTreeWidget.addTopLevelItem(QTreeWidgetItem item)'''
    def insertTopLevelItem(self, index, item):
        '''void QTreeWidget.insertTopLevelItem(int index, QTreeWidgetItem item)'''
    def topLevelItemCount(self):
        '''int QTreeWidget.topLevelItemCount()'''
        return int()
    def topLevelItem(self, index):
        '''QTreeWidgetItem QTreeWidget.topLevelItem(int index)'''
        return QTreeWidgetItem()
    def setColumnCount(self, columns):
        '''void QTreeWidget.setColumnCount(int columns)'''
    def columnCount(self):
        '''int QTreeWidget.columnCount()'''
        return int()


class QTreeWidgetItemIterator():
    """"""
    # Enum QTreeWidgetItemIterator.IteratorFlag
    All = 0
    Hidden = 0
    NotHidden = 0
    Selected = 0
    Unselected = 0
    Selectable = 0
    NotSelectable = 0
    DragEnabled = 0
    DragDisabled = 0
    DropEnabled = 0
    DropDisabled = 0
    HasChildren = 0
    NoChildren = 0
    Checked = 0
    NotChecked = 0
    Enabled = 0
    Disabled = 0
    Editable = 0
    NotEditable = 0
    UserFlag = 0

    def __init__(self, it):
        '''void QTreeWidgetItemIterator.__init__(QTreeWidgetItemIterator it)'''
    def __init__(self, widget, flags = None):
        '''void QTreeWidgetItemIterator.__init__(QTreeWidget widget, QTreeWidgetItemIterator.IteratorFlags flags = QTreeWidgetItemIterator.All)'''
    def __init__(self, item, flags = None):
        '''void QTreeWidgetItemIterator.__init__(QTreeWidgetItem item, QTreeWidgetItemIterator.IteratorFlags flags = QTreeWidgetItemIterator.All)'''
    def __isub__(self, n):
        '''QTreeWidgetItemIterator QTreeWidgetItemIterator.__isub__(int n)'''
        return QTreeWidgetItemIterator()
    def __iadd__(self, n):
        '''QTreeWidgetItemIterator QTreeWidgetItemIterator.__iadd__(int n)'''
        return QTreeWidgetItemIterator()
    def value(self):
        '''QTreeWidgetItem QTreeWidgetItemIterator.value()'''
        return QTreeWidgetItem()
    class IteratorFlags():
        """"""
        def __init__(self):
            '''QTreeWidgetItemIterator.IteratorFlags QTreeWidgetItemIterator.IteratorFlags.__init__()'''
            return QTreeWidgetItemIterator.IteratorFlags()
        def __init__(self):
            '''int QTreeWidgetItemIterator.IteratorFlags.__init__()'''
            return int()
        def __init__(self):
            '''void QTreeWidgetItemIterator.IteratorFlags.__init__()'''
        def __bool__(self):
            '''int QTreeWidgetItemIterator.IteratorFlags.__bool__()'''
            return int()
        def __ne__(self, f):
            '''bool QTreeWidgetItemIterator.IteratorFlags.__ne__(QTreeWidgetItemIterator.IteratorFlags f)'''
            return bool()
        def __eq__(self, f):
            '''bool QTreeWidgetItemIterator.IteratorFlags.__eq__(QTreeWidgetItemIterator.IteratorFlags f)'''
            return bool()
        def __invert__(self):
            '''QTreeWidgetItemIterator.IteratorFlags QTreeWidgetItemIterator.IteratorFlags.__invert__()'''
            return QTreeWidgetItemIterator.IteratorFlags()
        def __and__(self, mask):
            '''QTreeWidgetItemIterator.IteratorFlags QTreeWidgetItemIterator.IteratorFlags.__and__(int mask)'''
            return QTreeWidgetItemIterator.IteratorFlags()
        def __xor__(self, f):
            '''QTreeWidgetItemIterator.IteratorFlags QTreeWidgetItemIterator.IteratorFlags.__xor__(QTreeWidgetItemIterator.IteratorFlags f)'''
            return QTreeWidgetItemIterator.IteratorFlags()
        def __xor__(self, f):
            '''QTreeWidgetItemIterator.IteratorFlags QTreeWidgetItemIterator.IteratorFlags.__xor__(int f)'''
            return QTreeWidgetItemIterator.IteratorFlags()
        def __or__(self, f):
            '''QTreeWidgetItemIterator.IteratorFlags QTreeWidgetItemIterator.IteratorFlags.__or__(QTreeWidgetItemIterator.IteratorFlags f)'''
            return QTreeWidgetItemIterator.IteratorFlags()
        def __or__(self, f):
            '''QTreeWidgetItemIterator.IteratorFlags QTreeWidgetItemIterator.IteratorFlags.__or__(int f)'''
            return QTreeWidgetItemIterator.IteratorFlags()
        def __int__(self):
            '''int QTreeWidgetItemIterator.IteratorFlags.__int__()'''
            return int()
        def __ixor__(self, f):
            '''QTreeWidgetItemIterator.IteratorFlags QTreeWidgetItemIterator.IteratorFlags.__ixor__(QTreeWidgetItemIterator.IteratorFlags f)'''
            return QTreeWidgetItemIterator.IteratorFlags()
        def __ior__(self, f):
            '''QTreeWidgetItemIterator.IteratorFlags QTreeWidgetItemIterator.IteratorFlags.__ior__(QTreeWidgetItemIterator.IteratorFlags f)'''
            return QTreeWidgetItemIterator.IteratorFlags()
        def __iand__(self, mask):
            '''QTreeWidgetItemIterator.IteratorFlags QTreeWidgetItemIterator.IteratorFlags.__iand__(int mask)'''
            return QTreeWidgetItemIterator.IteratorFlags()


class QUndoGroup(QObject):
    """"""
    def __init__(self, parent = None):
        '''void QUndoGroup.__init__(QObject parent = None)'''
    undoTextChanged = pyqtSignal() # void undoTextChanged(const QStringamp;) - signal
    redoTextChanged = pyqtSignal() # void redoTextChanged(const QStringamp;) - signal
    indexChanged = pyqtSignal() # void indexChanged(int) - signal
    cleanChanged = pyqtSignal() # void cleanChanged(bool) - signal
    canUndoChanged = pyqtSignal() # void canUndoChanged(bool) - signal
    canRedoChanged = pyqtSignal() # void canRedoChanged(bool) - signal
    activeStackChanged = pyqtSignal() # void activeStackChanged(QUndoStack*) - signal
    def undo(self):
        '''void QUndoGroup.undo()'''
    def setActiveStack(self, stack):
        '''void QUndoGroup.setActiveStack(QUndoStack stack)'''
    def redo(self):
        '''void QUndoGroup.redo()'''
    def isClean(self):
        '''bool QUndoGroup.isClean()'''
        return bool()
    def redoText(self):
        '''str QUndoGroup.redoText()'''
        return str()
    def undoText(self):
        '''str QUndoGroup.undoText()'''
        return str()
    def canRedo(self):
        '''bool QUndoGroup.canRedo()'''
        return bool()
    def canUndo(self):
        '''bool QUndoGroup.canUndo()'''
        return bool()
    def createUndoAction(self, parent, prefix = None):
        '''QAction QUndoGroup.createUndoAction(QObject parent, str prefix = '')'''
        return QAction()
    def createRedoAction(self, parent, prefix = None):
        '''QAction QUndoGroup.createRedoAction(QObject parent, str prefix = '')'''
        return QAction()
    def activeStack(self):
        '''QUndoStack QUndoGroup.activeStack()'''
        return QUndoStack()
    def stacks(self):
        '''list-of-QUndoStack QUndoGroup.stacks()'''
        return [QUndoStack()]
    def removeStack(self, stack):
        '''void QUndoGroup.removeStack(QUndoStack stack)'''
    def addStack(self, stack):
        '''void QUndoGroup.addStack(QUndoStack stack)'''


class QUndoCommand():
    """"""
    def __init__(self, parent = None):
        '''void QUndoCommand.__init__(QUndoCommand parent = None)'''
    def __init__(self, text, parent = None):
        '''void QUndoCommand.__init__(str text, QUndoCommand parent = None)'''
    def actionText(self):
        '''str QUndoCommand.actionText()'''
        return str()
    def child(self, index):
        '''QUndoCommand QUndoCommand.child(int index)'''
        return QUndoCommand()
    def childCount(self):
        '''int QUndoCommand.childCount()'''
        return int()
    def undo(self):
        '''void QUndoCommand.undo()'''
    def text(self):
        '''str QUndoCommand.text()'''
        return str()
    def setText(self, text):
        '''void QUndoCommand.setText(str text)'''
    def redo(self):
        '''void QUndoCommand.redo()'''
    def mergeWith(self, other):
        '''bool QUndoCommand.mergeWith(QUndoCommand other)'''
        return bool()
    def id(self):
        '''int QUndoCommand.id()'''
        return int()


class QUndoStack(QObject):
    """"""
    def __init__(self, parent = None):
        '''void QUndoStack.__init__(QObject parent = None)'''
    def command(self, index):
        '''QUndoCommand QUndoStack.command(int index)'''
        return QUndoCommand()
    def undoLimit(self):
        '''int QUndoStack.undoLimit()'''
        return int()
    def setUndoLimit(self, limit):
        '''void QUndoStack.setUndoLimit(int limit)'''
    undoTextChanged = pyqtSignal() # void undoTextChanged(const QStringamp;) - signal
    redoTextChanged = pyqtSignal() # void redoTextChanged(const QStringamp;) - signal
    indexChanged = pyqtSignal() # void indexChanged(int) - signal
    cleanChanged = pyqtSignal() # void cleanChanged(bool) - signal
    canUndoChanged = pyqtSignal() # void canUndoChanged(bool) - signal
    canRedoChanged = pyqtSignal() # void canRedoChanged(bool) - signal
    def undo(self):
        '''void QUndoStack.undo()'''
    def setIndex(self, idx):
        '''void QUndoStack.setIndex(int idx)'''
    def setClean(self):
        '''void QUndoStack.setClean()'''
    def setActive(self, active = True):
        '''void QUndoStack.setActive(bool active = True)'''
    def redo(self):
        '''void QUndoStack.redo()'''
    def endMacro(self):
        '''void QUndoStack.endMacro()'''
    def beginMacro(self, text):
        '''void QUndoStack.beginMacro(str text)'''
    def cleanIndex(self):
        '''int QUndoStack.cleanIndex()'''
        return int()
    def isClean(self):
        '''bool QUndoStack.isClean()'''
        return bool()
    def isActive(self):
        '''bool QUndoStack.isActive()'''
        return bool()
    def createRedoAction(self, parent, prefix = None):
        '''QAction QUndoStack.createRedoAction(QObject parent, str prefix = '')'''
        return QAction()
    def createUndoAction(self, parent, prefix = None):
        '''QAction QUndoStack.createUndoAction(QObject parent, str prefix = '')'''
        return QAction()
    def text(self, idx):
        '''str QUndoStack.text(int idx)'''
        return str()
    def index(self):
        '''int QUndoStack.index()'''
        return int()
    def __len__(self):
        ''' QUndoStack.__len__()'''
        return ()
    def count(self):
        '''int QUndoStack.count()'''
        return int()
    def redoText(self):
        '''str QUndoStack.redoText()'''
        return str()
    def undoText(self):
        '''str QUndoStack.undoText()'''
        return str()
    def canRedo(self):
        '''bool QUndoStack.canRedo()'''
        return bool()
    def canUndo(self):
        '''bool QUndoStack.canUndo()'''
        return bool()
    def push(self, cmd):
        '''void QUndoStack.push(QUndoCommand cmd)'''
    def clear(self):
        '''void QUndoStack.clear()'''


class QUndoView(QListView):
    """"""
    def __init__(self, parent = None):
        '''void QUndoView.__init__(QWidget parent = None)'''
    def __init__(self, stack, parent = None):
        '''void QUndoView.__init__(QUndoStack stack, QWidget parent = None)'''
    def __init__(self, group, parent = None):
        '''void QUndoView.__init__(QUndoGroup group, QWidget parent = None)'''
    def setGroup(self, group):
        '''void QUndoView.setGroup(QUndoGroup group)'''
    def setStack(self, stack):
        '''void QUndoView.setStack(QUndoStack stack)'''
    def cleanIcon(self):
        '''QIcon QUndoView.cleanIcon()'''
        return QIcon()
    def setCleanIcon(self, icon):
        '''void QUndoView.setCleanIcon(QIcon icon)'''
    def emptyLabel(self):
        '''str QUndoView.emptyLabel()'''
        return str()
    def setEmptyLabel(self, label):
        '''void QUndoView.setEmptyLabel(str label)'''
    def group(self):
        '''QUndoGroup QUndoView.group()'''
        return QUndoGroup()
    def stack(self):
        '''QUndoStack QUndoView.stack()'''
        return QUndoStack()


class QWhatsThis():
    """"""
    def __init__(self):
        '''QWhatsThis QWhatsThis.__init__()'''
        return QWhatsThis()
    def createAction(self, parent = None):
        '''static QAction QWhatsThis.createAction(QObject parent = None)'''
        return QAction()
    def hideText(self):
        '''static void QWhatsThis.hideText()'''
    def showText(self, pos, text, widget = None):
        '''static void QWhatsThis.showText(QPoint pos, str text, QWidget widget = None)'''
    def leaveWhatsThisMode(self):
        '''static void QWhatsThis.leaveWhatsThisMode()'''
    def inWhatsThisMode(self):
        '''static bool QWhatsThis.inWhatsThisMode()'''
        return bool()
    def enterWhatsThisMode(self):
        '''static void QWhatsThis.enterWhatsThisMode()'''


class QWidgetAction(QAction):
    """"""
    def __init__(self, parent):
        '''void QWidgetAction.__init__(QObject parent)'''
    def createdWidgets(self):
        '''list-of-QWidget QWidgetAction.createdWidgets()'''
        return [QWidget()]
    def deleteWidget(self, widget):
        '''void QWidgetAction.deleteWidget(QWidget widget)'''
    def createWidget(self, parent):
        '''QWidget QWidgetAction.createWidget(QWidget parent)'''
        return QWidget()
    def eventFilter(self):
        '''QEvent QWidgetAction.eventFilter()'''
        return QEvent()
    def event(self):
        '''QEvent QWidgetAction.event()'''
        return QEvent()
    def releaseWidget(self, widget):
        '''void QWidgetAction.releaseWidget(QWidget widget)'''
    def requestWidget(self, parent):
        '''QWidget QWidgetAction.requestWidget(QWidget parent)'''
        return QWidget()
    def defaultWidget(self):
        '''QWidget QWidgetAction.defaultWidget()'''
        return QWidget()
    def setDefaultWidget(self, w):
        '''void QWidgetAction.setDefaultWidget(QWidget w)'''


class QWizard(QDialog):
    """"""
    # Enum QWizard.WizardOption
    IndependentPages = 0
    IgnoreSubTitles = 0
    ExtendedWatermarkPixmap = 0
    NoDefaultButton = 0
    NoBackButtonOnStartPage = 0
    NoBackButtonOnLastPage = 0
    DisabledBackButtonOnLastPage = 0
    HaveNextButtonOnLastPage = 0
    HaveFinishButtonOnEarlyPages = 0
    NoCancelButton = 0
    CancelButtonOnLeft = 0
    HaveHelpButton = 0
    HelpButtonOnRight = 0
    HaveCustomButton1 = 0
    HaveCustomButton2 = 0
    HaveCustomButton3 = 0
    NoCancelButtonOnLastPage = 0

    # Enum QWizard.WizardStyle
    ClassicStyle = 0
    ModernStyle = 0
    MacStyle = 0
    AeroStyle = 0

    # Enum QWizard.WizardPixmap
    WatermarkPixmap = 0
    LogoPixmap = 0
    BannerPixmap = 0
    BackgroundPixmap = 0

    # Enum QWizard.WizardButton
    BackButton = 0
    NextButton = 0
    CommitButton = 0
    FinishButton = 0
    CancelButton = 0
    HelpButton = 0
    CustomButton1 = 0
    CustomButton2 = 0
    CustomButton3 = 0
    Stretch = 0

    def __init__(self, parent = None, flags = 0):
        '''void QWizard.__init__(QWidget parent = None, Qt.WindowFlags flags = 0)'''
    pageRemoved = pyqtSignal() # void pageRemoved(int) - signal
    pageAdded = pyqtSignal() # void pageAdded(int) - signal
    def sideWidget(self):
        '''QWidget QWizard.sideWidget()'''
        return QWidget()
    def setSideWidget(self, widget):
        '''void QWizard.setSideWidget(QWidget widget)'''
    def pageIds(self):
        '''list-of-int QWizard.pageIds()'''
        return [int()]
    def removePage(self, id):
        '''void QWizard.removePage(int id)'''
    def cleanupPage(self, id):
        '''void QWizard.cleanupPage(int id)'''
    def initializePage(self, id):
        '''void QWizard.initializePage(int id)'''
    def done(self, result):
        '''void QWizard.done(int result)'''
    def paintEvent(self, event):
        '''void QWizard.paintEvent(QPaintEvent event)'''
    def resizeEvent(self, event):
        '''void QWizard.resizeEvent(QResizeEvent event)'''
    def event(self, event):
        '''bool QWizard.event(QEvent event)'''
        return bool()
    def restart(self):
        '''void QWizard.restart()'''
    def next(self):
        '''void QWizard.next()'''
    def back(self):
        '''void QWizard.back()'''
    customButtonClicked = pyqtSignal() # void customButtonClicked(int) - signal
    helpRequested = pyqtSignal() # void helpRequested() - signal
    currentIdChanged = pyqtSignal() # void currentIdChanged(int) - signal
    def sizeHint(self):
        '''QSize QWizard.sizeHint()'''
        return QSize()
    def setVisible(self, visible):
        '''void QWizard.setVisible(bool visible)'''
    def setDefaultProperty(self, className, property, changedSignal):
        '''void QWizard.setDefaultProperty(str className, str property, str changedSignal)'''
    def pixmap(self, which):
        '''QPixmap QWizard.pixmap(QWizard.WizardPixmap which)'''
        return QPixmap()
    def setPixmap(self, which, pixmap):
        '''void QWizard.setPixmap(QWizard.WizardPixmap which, QPixmap pixmap)'''
    def subTitleFormat(self):
        '''Qt.TextFormat QWizard.subTitleFormat()'''
        return Qt.TextFormat()
    def setSubTitleFormat(self, format):
        '''void QWizard.setSubTitleFormat(Qt.TextFormat format)'''
    def titleFormat(self):
        '''Qt.TextFormat QWizard.titleFormat()'''
        return Qt.TextFormat()
    def setTitleFormat(self, format):
        '''void QWizard.setTitleFormat(Qt.TextFormat format)'''
    def button(self, which):
        '''QAbstractButton QWizard.button(QWizard.WizardButton which)'''
        return QAbstractButton()
    def setButton(self, which, button):
        '''void QWizard.setButton(QWizard.WizardButton which, QAbstractButton button)'''
    def setButtonLayout(self, layout):
        '''void QWizard.setButtonLayout(list-of-QWizard.WizardButton layout)'''
    def buttonText(self, which):
        '''str QWizard.buttonText(QWizard.WizardButton which)'''
        return str()
    def setButtonText(self, which, text):
        '''void QWizard.setButtonText(QWizard.WizardButton which, str text)'''
    def options(self):
        '''QWizard.WizardOptions QWizard.options()'''
        return QWizard.WizardOptions()
    def setOptions(self, options):
        '''void QWizard.setOptions(QWizard.WizardOptions options)'''
    def testOption(self, option):
        '''bool QWizard.testOption(QWizard.WizardOption option)'''
        return bool()
    def setOption(self, option, on = True):
        '''void QWizard.setOption(QWizard.WizardOption option, bool on = True)'''
    def wizardStyle(self):
        '''QWizard.WizardStyle QWizard.wizardStyle()'''
        return QWizard.WizardStyle()
    def setWizardStyle(self, style):
        '''void QWizard.setWizardStyle(QWizard.WizardStyle style)'''
    def field(self, name):
        '''QVariant QWizard.field(str name)'''
        return QVariant()
    def setField(self, name, value):
        '''void QWizard.setField(str name, QVariant value)'''
    def nextId(self):
        '''int QWizard.nextId()'''
        return int()
    def validateCurrentPage(self):
        '''bool QWizard.validateCurrentPage()'''
        return bool()
    def currentId(self):
        '''int QWizard.currentId()'''
        return int()
    def currentPage(self):
        '''QWizardPage QWizard.currentPage()'''
        return QWizardPage()
    def startId(self):
        '''int QWizard.startId()'''
        return int()
    def setStartId(self, id):
        '''void QWizard.setStartId(int id)'''
    def visitedPages(self):
        '''list-of-int QWizard.visitedPages()'''
        return [int()]
    def hasVisitedPage(self, id):
        '''bool QWizard.hasVisitedPage(int id)'''
        return bool()
    def page(self, id):
        '''QWizardPage QWizard.page(int id)'''
        return QWizardPage()
    def setPage(self, id, page):
        '''void QWizard.setPage(int id, QWizardPage page)'''
    def addPage(self, page):
        '''int QWizard.addPage(QWizardPage page)'''
        return int()
    class WizardOptions():
        """"""
        def __init__(self):
            '''QWizard.WizardOptions QWizard.WizardOptions.__init__()'''
            return QWizard.WizardOptions()
        def __init__(self):
            '''int QWizard.WizardOptions.__init__()'''
            return int()
        def __init__(self):
            '''void QWizard.WizardOptions.__init__()'''
        def __bool__(self):
            '''int QWizard.WizardOptions.__bool__()'''
            return int()
        def __ne__(self, f):
            '''bool QWizard.WizardOptions.__ne__(QWizard.WizardOptions f)'''
            return bool()
        def __eq__(self, f):
            '''bool QWizard.WizardOptions.__eq__(QWizard.WizardOptions f)'''
            return bool()
        def __invert__(self):
            '''QWizard.WizardOptions QWizard.WizardOptions.__invert__()'''
            return QWizard.WizardOptions()
        def __and__(self, mask):
            '''QWizard.WizardOptions QWizard.WizardOptions.__and__(int mask)'''
            return QWizard.WizardOptions()
        def __xor__(self, f):
            '''QWizard.WizardOptions QWizard.WizardOptions.__xor__(QWizard.WizardOptions f)'''
            return QWizard.WizardOptions()
        def __xor__(self, f):
            '''QWizard.WizardOptions QWizard.WizardOptions.__xor__(int f)'''
            return QWizard.WizardOptions()
        def __or__(self, f):
            '''QWizard.WizardOptions QWizard.WizardOptions.__or__(QWizard.WizardOptions f)'''
            return QWizard.WizardOptions()
        def __or__(self, f):
            '''QWizard.WizardOptions QWizard.WizardOptions.__or__(int f)'''
            return QWizard.WizardOptions()
        def __int__(self):
            '''int QWizard.WizardOptions.__int__()'''
            return int()
        def __ixor__(self, f):
            '''QWizard.WizardOptions QWizard.WizardOptions.__ixor__(QWizard.WizardOptions f)'''
            return QWizard.WizardOptions()
        def __ior__(self, f):
            '''QWizard.WizardOptions QWizard.WizardOptions.__ior__(QWizard.WizardOptions f)'''
            return QWizard.WizardOptions()
        def __iand__(self, mask):
            '''QWizard.WizardOptions QWizard.WizardOptions.__iand__(int mask)'''
            return QWizard.WizardOptions()


class QWizardPage(QWidget):
    """"""
    def __init__(self, parent = None):
        '''void QWizardPage.__init__(QWidget parent = None)'''
    def wizard(self):
        '''QWizard QWizardPage.wizard()'''
        return QWizard()
    def registerField(self, name, widget, property = None, changedSignal = 0):
        '''void QWizardPage.registerField(str name, QWidget widget, str property = None, signal changedSignal = 0)'''
    def registerField(self, name, widget, property = None, changedSignal = None):
        '''void QWizardPage.registerField(str name, QWidget widget, str property = None, str changedSignal = None)'''
    def field(self, name):
        '''QVariant QWizardPage.field(str name)'''
        return QVariant()
    def setField(self, name, value):
        '''void QWizardPage.setField(str name, QVariant value)'''
    completeChanged = pyqtSignal() # void completeChanged() - signal
    def nextId(self):
        '''int QWizardPage.nextId()'''
        return int()
    def isComplete(self):
        '''bool QWizardPage.isComplete()'''
        return bool()
    def validatePage(self):
        '''bool QWizardPage.validatePage()'''
        return bool()
    def cleanupPage(self):
        '''void QWizardPage.cleanupPage()'''
    def initializePage(self):
        '''void QWizardPage.initializePage()'''
    def buttonText(self, which):
        '''str QWizardPage.buttonText(QWizard.WizardButton which)'''
        return str()
    def setButtonText(self, which, text):
        '''void QWizardPage.setButtonText(QWizard.WizardButton which, str text)'''
    def isCommitPage(self):
        '''bool QWizardPage.isCommitPage()'''
        return bool()
    def setCommitPage(self, commitPage):
        '''void QWizardPage.setCommitPage(bool commitPage)'''
    def isFinalPage(self):
        '''bool QWizardPage.isFinalPage()'''
        return bool()
    def setFinalPage(self, finalPage):
        '''void QWizardPage.setFinalPage(bool finalPage)'''
    def pixmap(self, which):
        '''QPixmap QWizardPage.pixmap(QWizard.WizardPixmap which)'''
        return QPixmap()
    def setPixmap(self, which, pixmap):
        '''void QWizardPage.setPixmap(QWizard.WizardPixmap which, QPixmap pixmap)'''
    def subTitle(self):
        '''str QWizardPage.subTitle()'''
        return str()
    def setSubTitle(self, subTitle):
        '''void QWizardPage.setSubTitle(str subTitle)'''
    def title(self):
        '''str QWizardPage.title()'''
        return str()
    def setTitle(self, title):
        '''void QWizardPage.setTitle(str title)'''


QWIDGETSIZE_MAX = None # int member

qApp = None # QApplication member

def qDrawBorderPixmap(painter, target, margins, pixmap):
    '''static void qDrawBorderPixmap(QPainter painter, QRect target, QMargins margins, QPixmap pixmap)'''


def qDrawPlainRect(p, x, y, w, h, lineWidth = 1, fill = None):
    '''static QColor qDrawPlainRect(QPainter p, int x, int y, int w, int h, int lineWidth = 1, QBrush fill = None)'''
    return QColor()

def qDrawPlainRect(p, r, lineWidth = 1, fill = None):
    '''static QColor qDrawPlainRect(QPainter p, QRect r, int lineWidth = 1, QBrush fill = None)'''
    return QColor()

def qDrawWinPanel(p, x, y, w, h, pal, sunken = False, fill = None):
    '''static void qDrawWinPanel(QPainter p, int x, int y, int w, int h, QPalette pal, bool sunken = False, QBrush fill = None)'''


def qDrawWinPanel(p, r, pal, sunken = False, fill = None):
    '''static void qDrawWinPanel(QPainter p, QRect r, QPalette pal, bool sunken = False, QBrush fill = None)'''


def qDrawWinButton(p, x, y, w, h, pal, sunken = False, fill = None):
    '''static void qDrawWinButton(QPainter p, int x, int y, int w, int h, QPalette pal, bool sunken = False, QBrush fill = None)'''


def qDrawWinButton(p, r, pal, sunken = False, fill = None):
    '''static void qDrawWinButton(QPainter p, QRect r, QPalette pal, bool sunken = False, QBrush fill = None)'''


def qDrawShadePanel(p, x, y, w, h, pal, sunken = False, lineWidth = 1, fill = None):
    '''static void qDrawShadePanel(QPainter p, int x, int y, int w, int h, QPalette pal, bool sunken = False, int lineWidth = 1, QBrush fill = None)'''


def qDrawShadePanel(p, r, pal, sunken = False, lineWidth = 1, fill = None):
    '''static void qDrawShadePanel(QPainter p, QRect r, QPalette pal, bool sunken = False, int lineWidth = 1, QBrush fill = None)'''


def qDrawShadeRect(p, x, y, w, h, pal, sunken = False, lineWidth = 1, midLineWidth = 0, fill = None):
    '''static void qDrawShadeRect(QPainter p, int x, int y, int w, int h, QPalette pal, bool sunken = False, int lineWidth = 1, int midLineWidth = 0, QBrush fill = None)'''


def qDrawShadeRect(p, r, pal, sunken = False, lineWidth = 1, midLineWidth = 0, fill = None):
    '''static void qDrawShadeRect(QPainter p, QRect r, QPalette pal, bool sunken = False, int lineWidth = 1, int midLineWidth = 0, QBrush fill = None)'''


def qDrawShadeLine(p, x1, y1, x2, y2, pal, sunken = True, lineWidth = 1, midLineWidth = 0):
    '''static void qDrawShadeLine(QPainter p, int x1, int y1, int x2, int y2, QPalette pal, bool sunken = True, int lineWidth = 1, int midLineWidth = 0)'''


def qDrawShadeLine(p, p1, p2, pal, sunken = True, lineWidth = 1, midLineWidth = 0):
    '''static void qDrawShadeLine(QPainter p, QPoint p1, QPoint p2, QPalette pal, bool sunken = True, int lineWidth = 1, int midLineWidth = 0)'''


