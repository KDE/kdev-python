class pyqtSignal():
 def connect(self, targetSignal): pass
 def emit(self, *args): pass
from QtCore import *

from QtWidgets import *

import datetime

class QtWin():
    """"""
    # Enum QtWin.WindowFlip3DPolicy
    FlipDefault = 0
    FlipExcludeBelow = 0
    FlipExcludeAbove = 0

    # Enum QtWin.HBitmapFormat
    HBitmapNoAlpha = 0
    HBitmapPremultipliedAlpha = 0
    HBitmapAlpha = 0

    def taskbarDeleteTab(self):
        '''static QWindow QtWin.taskbarDeleteTab()'''
        return QWindow()
    def taskbarDeleteTab(self, window):
        '''static void QtWin.taskbarDeleteTab(QWidget window)'''
    def taskbarAddTab(self):
        '''static QWindow QtWin.taskbarAddTab()'''
        return QWindow()
    def taskbarAddTab(self, window):
        '''static void QtWin.taskbarAddTab(QWidget window)'''
    def taskbarActivateTabAlt(self):
        '''static QWindow QtWin.taskbarActivateTabAlt()'''
        return QWindow()
    def taskbarActivateTabAlt(self, window):
        '''static void QtWin.taskbarActivateTabAlt(QWidget window)'''
    def taskbarActivateTab(self):
        '''static QWindow QtWin.taskbarActivateTab()'''
        return QWindow()
    def taskbarActivateTab(self, window):
        '''static void QtWin.taskbarActivateTab(QWidget window)'''
    def markFullscreenWindow(self, fullscreen = True):
        '''static QWindow QtWin.markFullscreenWindow(bool fullscreen = True)'''
        return QWindow()
    def markFullscreenWindow(self, window, fullscreen = True):
        '''static void QtWin.markFullscreenWindow(QWidget window, bool fullscreen = True)'''
    def setCurrentProcessExplicitAppUserModelID(self, id):
        '''static void QtWin.setCurrentProcessExplicitAppUserModelID(str id)'''
    def isCompositionOpaque(self):
        '''static bool QtWin.isCompositionOpaque()'''
        return bool()
    def setCompositionEnabled(self, enabled):
        '''static void QtWin.setCompositionEnabled(bool enabled)'''
    def isCompositionEnabled(self):
        '''static bool QtWin.isCompositionEnabled()'''
        return bool()
    def disableBlurBehindWindow(self, window):
        '''static void QtWin.disableBlurBehindWindow(QWindow window)'''
    def disableBlurBehindWindow(self, window):
        '''static void QtWin.disableBlurBehindWindow(QWidget window)'''
    def enableBlurBehindWindow(self, window, region):
        '''static void QtWin.enableBlurBehindWindow(QWindow window, QRegion region)'''
    def enableBlurBehindWindow(self, window):
        '''static void QtWin.enableBlurBehindWindow(QWindow window)'''
    def enableBlurBehindWindow(self, window, region):
        '''static void QtWin.enableBlurBehindWindow(QWidget window, QRegion region)'''
    def enableBlurBehindWindow(self, window):
        '''static void QtWin.enableBlurBehindWindow(QWidget window)'''
    def resetExtendedFrame(self, window):
        '''static void QtWin.resetExtendedFrame(QWindow window)'''
    def resetExtendedFrame(self, window):
        '''static void QtWin.resetExtendedFrame(QWidget window)'''
    def extendFrameIntoClientArea(self, window, left, top, right, bottom):
        '''static void QtWin.extendFrameIntoClientArea(QWindow window, int left, int top, int right, int bottom)'''
    def extendFrameIntoClientArea(self, window, margins):
        '''static void QtWin.extendFrameIntoClientArea(QWindow window, QMargins margins)'''
    def extendFrameIntoClientArea(self, window, margins):
        '''static void QtWin.extendFrameIntoClientArea(QWidget window, QMargins margins)'''
    def extendFrameIntoClientArea(self, window, left, top, right, bottom):
        '''static void QtWin.extendFrameIntoClientArea(QWidget window, int left, int top, int right, int bottom)'''
    def windowFlip3DPolicy(self):
        '''static QWindow QtWin.windowFlip3DPolicy()'''
        return QWindow()
    def windowFlip3DPolicy(self, window):
        '''static QtWin.WindowFlip3DPolicy QtWin.windowFlip3DPolicy(QWidget window)'''
        return QtWin.WindowFlip3DPolicy()
    def setWindowFlip3DPolicy(self, window, policy):
        '''static void QtWin.setWindowFlip3DPolicy(QWindow window, QtWin.WindowFlip3DPolicy policy)'''
    def setWindowFlip3DPolicy(self, window, policy):
        '''static void QtWin.setWindowFlip3DPolicy(QWidget window, QtWin.WindowFlip3DPolicy policy)'''
    def isWindowPeekDisallowed(self, window):
        '''static bool QtWin.isWindowPeekDisallowed(QWindow window)'''
        return bool()
    def isWindowPeekDisallowed(self, window):
        '''static bool QtWin.isWindowPeekDisallowed(QWidget window)'''
        return bool()
    def setWindowDisallowPeek(self, window, disallow):
        '''static void QtWin.setWindowDisallowPeek(QWindow window, bool disallow)'''
    def setWindowDisallowPeek(self, window, disallow):
        '''static void QtWin.setWindowDisallowPeek(QWidget window, bool disallow)'''
    def isWindowExcludedFromPeek(self, window):
        '''static bool QtWin.isWindowExcludedFromPeek(QWindow window)'''
        return bool()
    def isWindowExcludedFromPeek(self, window):
        '''static bool QtWin.isWindowExcludedFromPeek(QWidget window)'''
        return bool()
    def setWindowExcludedFromPeek(self, window, exclude):
        '''static void QtWin.setWindowExcludedFromPeek(QWindow window, bool exclude)'''
    def setWindowExcludedFromPeek(self, window, exclude):
        '''static void QtWin.setWindowExcludedFromPeek(QWidget window, bool exclude)'''
    def realColorizationColor(self):
        '''static QColor QtWin.realColorizationColor()'''
        return QColor()
    def colorizationColor(self, opaqueBlend):
        '''static QColor QtWin.colorizationColor(bool opaqueBlend)'''
        return QColor()
    def errorStringFromHresult(self, hresult):
        '''static str QtWin.errorStringFromHresult(int hresult)'''
        return str()
    def stringFromHresult(self, hresult):
        '''static str QtWin.stringFromHresult(int hresult)'''
        return str()
    def fromHRGN(self, hrgn):
        '''static QRegion QtWin.fromHRGN(sip.voidptr hrgn)'''
        return QRegion()
    def toHRGN(self, region):
        '''static sip.voidptr QtWin.toHRGN(QRegion region)'''
        return sip.voidptr()
    def fromHICON(self, icon):
        '''static QPixmap QtWin.fromHICON(sip.voidptr icon)'''
        return QPixmap()
    def imageFromHBITMAP(self, hdc, bitmap, width, height):
        '''static QImage QtWin.imageFromHBITMAP(sip.voidptr hdc, sip.voidptr bitmap, int width, int height)'''
        return QImage()
    def toHICON(self, p):
        '''static sip.voidptr QtWin.toHICON(QPixmap p)'''
        return sip.voidptr()
    def fromHBITMAP(self, bitmap, format = None):
        '''static QPixmap QtWin.fromHBITMAP(sip.voidptr bitmap, QtWin.HBitmapFormat format = QtWin.HBitmapNoAlpha)'''
        return QPixmap()
    def toHBITMAP(self, p, format = None):
        '''static sip.voidptr QtWin.toHBITMAP(QPixmap p, QtWin.HBitmapFormat format = QtWin.HBitmapNoAlpha)'''
        return sip.voidptr()
    def createMask(self, bitmap):
        '''static sip.voidptr QtWin.createMask(QBitmap bitmap)'''
        return sip.voidptr()


class QWinJumpList(QObject):
    """"""
    def __init__(self, parent = None):
        '''void QWinJumpList.__init__(QObject parent = None)'''
    def clear(self):
        '''void QWinJumpList.clear()'''
    def addCategory(self, category):
        '''void QWinJumpList.addCategory(QWinJumpListCategory category)'''
    def addCategory(self, title, items = None):
        '''QWinJumpListCategory QWinJumpList.addCategory(str title, list-of-QWinJumpListItem items = QListlt;QWinJumpListItem*gt;())'''
        return QWinJumpListCategory()
    def categories(self):
        '''list-of-QWinJumpListCategory QWinJumpList.categories()'''
        return [QWinJumpListCategory()]
    def tasks(self):
        '''QWinJumpListCategory QWinJumpList.tasks()'''
        return QWinJumpListCategory()
    def frequent(self):
        '''QWinJumpListCategory QWinJumpList.frequent()'''
        return QWinJumpListCategory()
    def recent(self):
        '''QWinJumpListCategory QWinJumpList.recent()'''
        return QWinJumpListCategory()
    def setIdentifier(self, identifier):
        '''void QWinJumpList.setIdentifier(str identifier)'''
    def identifier(self):
        '''str QWinJumpList.identifier()'''
        return str()


class QWinJumpListCategory():
    """"""
    # Enum QWinJumpListCategory.Type
    Custom = 0
    Recent = 0
    Frequent = 0
    Tasks = 0

    def __init__(self, title = str()):
        '''void QWinJumpListCategory.__init__(str title = str())'''
    def clear(self):
        '''void QWinJumpListCategory.clear()'''
    def addSeparator(self):
        '''QWinJumpListItem QWinJumpListCategory.addSeparator()'''
        return QWinJumpListItem()
    def addLink(self, title, executablePath, arguments = strList()):
        '''QWinJumpListItem QWinJumpListCategory.addLink(str title, str executablePath, list-of-str arguments = strList())'''
        return QWinJumpListItem()
    def addLink(self, icon, title, executablePath, arguments = strList()):
        '''QWinJumpListItem QWinJumpListCategory.addLink(QIcon icon, str title, str executablePath, list-of-str arguments = strList())'''
        return QWinJumpListItem()
    def addDestination(self, filePath):
        '''QWinJumpListItem QWinJumpListCategory.addDestination(str filePath)'''
        return QWinJumpListItem()
    def addItem(self, item):
        '''void QWinJumpListCategory.addItem(QWinJumpListItem item)'''
    def items(self):
        '''list-of-QWinJumpListItem QWinJumpListCategory.items()'''
        return [QWinJumpListItem()]
    def isEmpty(self):
        '''bool QWinJumpListCategory.isEmpty()'''
        return bool()
    def count(self):
        '''int QWinJumpListCategory.count()'''
        return int()
    def setTitle(self, title):
        '''void QWinJumpListCategory.setTitle(str title)'''
    def title(self):
        '''str QWinJumpListCategory.title()'''
        return str()
    def setVisible(self, visible):
        '''void QWinJumpListCategory.setVisible(bool visible)'''
    def isVisible(self):
        '''bool QWinJumpListCategory.isVisible()'''
        return bool()
    def type(self):
        '''QWinJumpListCategory.Type QWinJumpListCategory.type()'''
        return QWinJumpListCategory.Type()


class QWinJumpListItem():
    """"""
    # Enum QWinJumpListItem.Type
    Destination = 0
    Link = 0
    Separator = 0

    def __init__(self, type):
        '''void QWinJumpListItem.__init__(QWinJumpListItem.Type type)'''
    def arguments(self):
        '''list-of-str QWinJumpListItem.arguments()'''
        return [str()]
    def setArguments(self, arguments):
        '''void QWinJumpListItem.setArguments(list-of-str arguments)'''
    def description(self):
        '''str QWinJumpListItem.description()'''
        return str()
    def setDescription(self, description):
        '''void QWinJumpListItem.setDescription(str description)'''
    def title(self):
        '''str QWinJumpListItem.title()'''
        return str()
    def setTitle(self, title):
        '''void QWinJumpListItem.setTitle(str title)'''
    def icon(self):
        '''QIcon QWinJumpListItem.icon()'''
        return QIcon()
    def setIcon(self, icon):
        '''void QWinJumpListItem.setIcon(QIcon icon)'''
    def workingDirectory(self):
        '''str QWinJumpListItem.workingDirectory()'''
        return str()
    def setWorkingDirectory(self, workingDirectory):
        '''void QWinJumpListItem.setWorkingDirectory(str workingDirectory)'''
    def filePath(self):
        '''str QWinJumpListItem.filePath()'''
        return str()
    def setFilePath(self, filePath):
        '''void QWinJumpListItem.setFilePath(str filePath)'''
    def type(self):
        '''QWinJumpListItem.Type QWinJumpListItem.type()'''
        return QWinJumpListItem.Type()
    def setType(self, type):
        '''void QWinJumpListItem.setType(QWinJumpListItem.Type type)'''


class QWinTaskbarButton(QObject):
    """"""
    def __init__(self, parent = None):
        '''void QWinTaskbarButton.__init__(QObject parent = None)'''
    def clearOverlayIcon(self):
        '''void QWinTaskbarButton.clearOverlayIcon()'''
    def setOverlayAccessibleDescription(self, description):
        '''void QWinTaskbarButton.setOverlayAccessibleDescription(str description)'''
    def setOverlayIcon(self, icon):
        '''void QWinTaskbarButton.setOverlayIcon(QIcon icon)'''
    def eventFilter(self):
        '''QEvent QWinTaskbarButton.eventFilter()'''
        return QEvent()
    def progress(self):
        '''QWinTaskbarProgress QWinTaskbarButton.progress()'''
        return QWinTaskbarProgress()
    def overlayAccessibleDescription(self):
        '''str QWinTaskbarButton.overlayAccessibleDescription()'''
        return str()
    def overlayIcon(self):
        '''QIcon QWinTaskbarButton.overlayIcon()'''
        return QIcon()
    def window(self):
        '''QWindow QWinTaskbarButton.window()'''
        return QWindow()
    def setWindow(self, window):
        '''void QWinTaskbarButton.setWindow(QWindow window)'''


class QWinTaskbarProgress(QObject):
    """"""
    def __init__(self, parent = None):
        '''void QWinTaskbarProgress.__init__(QObject parent = None)'''
    visibilityChanged = pyqtSignal() # void visibilityChanged(bool) - signal
    maximumChanged = pyqtSignal() # void maximumChanged(int) - signal
    minimumChanged = pyqtSignal() # void minimumChanged(int) - signal
    valueChanged = pyqtSignal() # void valueChanged(int) - signal
    def stop(self):
        '''void QWinTaskbarProgress.stop()'''
    def setPaused(self, paused):
        '''void QWinTaskbarProgress.setPaused(bool paused)'''
    def resume(self):
        '''void QWinTaskbarProgress.resume()'''
    def pause(self):
        '''void QWinTaskbarProgress.pause()'''
    def setVisible(self, visible):
        '''void QWinTaskbarProgress.setVisible(bool visible)'''
    def hide(self):
        '''void QWinTaskbarProgress.hide()'''
    def show(self):
        '''void QWinTaskbarProgress.show()'''
    def reset(self):
        '''void QWinTaskbarProgress.reset()'''
    def setRange(self, minimum, maximum):
        '''void QWinTaskbarProgress.setRange(int minimum, int maximum)'''
    def setMaximum(self, maximum):
        '''void QWinTaskbarProgress.setMaximum(int maximum)'''
    def setMinimum(self, minimum):
        '''void QWinTaskbarProgress.setMinimum(int minimum)'''
    def setValue(self, value):
        '''void QWinTaskbarProgress.setValue(int value)'''
    def isStopped(self):
        '''bool QWinTaskbarProgress.isStopped()'''
        return bool()
    def isPaused(self):
        '''bool QWinTaskbarProgress.isPaused()'''
        return bool()
    def isVisible(self):
        '''bool QWinTaskbarProgress.isVisible()'''
        return bool()
    def maximum(self):
        '''int QWinTaskbarProgress.maximum()'''
        return int()
    def minimum(self):
        '''int QWinTaskbarProgress.minimum()'''
        return int()
    def value(self):
        '''int QWinTaskbarProgress.value()'''
        return int()


class QWinThumbnailToolBar(QObject):
    """"""
    def __init__(self, parent = None):
        '''void QWinThumbnailToolBar.__init__(QObject parent = None)'''
    iconicLivePreviewPixmapRequested = pyqtSignal() # void iconicLivePreviewPixmapRequested() - signal
    iconicThumbnailPixmapRequested = pyqtSignal() # void iconicThumbnailPixmapRequested() - signal
    def setIconicLivePreviewPixmap(self):
        '''QPixmap QWinThumbnailToolBar.setIconicLivePreviewPixmap()'''
        return QPixmap()
    def setIconicThumbnailPixmap(self):
        '''QPixmap QWinThumbnailToolBar.setIconicThumbnailPixmap()'''
        return QPixmap()
    def clear(self):
        '''void QWinThumbnailToolBar.clear()'''
    def iconicLivePreviewPixmap(self):
        '''QPixmap QWinThumbnailToolBar.iconicLivePreviewPixmap()'''
        return QPixmap()
    def iconicThumbnailPixmap(self):
        '''QPixmap QWinThumbnailToolBar.iconicThumbnailPixmap()'''
        return QPixmap()
    def setIconicPixmapNotificationsEnabled(self, enabled):
        '''void QWinThumbnailToolBar.setIconicPixmapNotificationsEnabled(bool enabled)'''
    def iconicPixmapNotificationsEnabled(self):
        '''bool QWinThumbnailToolBar.iconicPixmapNotificationsEnabled()'''
        return bool()
    def count(self):
        '''int QWinThumbnailToolBar.count()'''
        return int()
    def buttons(self):
        '''list-of-QWinThumbnailToolButton QWinThumbnailToolBar.buttons()'''
        return [QWinThumbnailToolButton()]
    def setButtons(self, buttons):
        '''void QWinThumbnailToolBar.setButtons(list-of-QWinThumbnailToolButton buttons)'''
    def removeButton(self, button):
        '''void QWinThumbnailToolBar.removeButton(QWinThumbnailToolButton button)'''
    def addButton(self, button):
        '''void QWinThumbnailToolBar.addButton(QWinThumbnailToolButton button)'''
    def window(self):
        '''QWindow QWinThumbnailToolBar.window()'''
        return QWindow()
    def setWindow(self, window):
        '''void QWinThumbnailToolBar.setWindow(QWindow window)'''


class QWinThumbnailToolButton(QObject):
    """"""
    def __init__(self, parent = None):
        '''void QWinThumbnailToolButton.__init__(QObject parent = None)'''
    clicked = pyqtSignal() # void clicked() - signal
    def click(self):
        '''void QWinThumbnailToolButton.click()'''
    def isFlat(self):
        '''bool QWinThumbnailToolButton.isFlat()'''
        return bool()
    def setFlat(self, flat):
        '''void QWinThumbnailToolButton.setFlat(bool flat)'''
    def dismissOnClick(self):
        '''bool QWinThumbnailToolButton.dismissOnClick()'''
        return bool()
    def setDismissOnClick(self, dismiss):
        '''void QWinThumbnailToolButton.setDismissOnClick(bool dismiss)'''
    def isVisible(self):
        '''bool QWinThumbnailToolButton.isVisible()'''
        return bool()
    def setVisible(self, visible):
        '''void QWinThumbnailToolButton.setVisible(bool visible)'''
    def isInteractive(self):
        '''bool QWinThumbnailToolButton.isInteractive()'''
        return bool()
    def setInteractive(self, interactive):
        '''void QWinThumbnailToolButton.setInteractive(bool interactive)'''
    def isEnabled(self):
        '''bool QWinThumbnailToolButton.isEnabled()'''
        return bool()
    def setEnabled(self, enabled):
        '''void QWinThumbnailToolButton.setEnabled(bool enabled)'''
    def icon(self):
        '''QIcon QWinThumbnailToolButton.icon()'''
        return QIcon()
    def setIcon(self, icon):
        '''void QWinThumbnailToolButton.setIcon(QIcon icon)'''
    def toolTip(self):
        '''str QWinThumbnailToolButton.toolTip()'''
        return str()
    def setToolTip(self, toolTip):
        '''void QWinThumbnailToolButton.setToolTip(str toolTip)'''


