class pyqtSignal():
 def connect(self, targetSignal): pass
 def emit(self, *args): pass
from QtCore import *

from QtWidgets import *

import datetime

class QMacPasteboardMime():
    """"""
    # Enum QMacPasteboardMime.QMacPasteboardMimeType
    MIME_DND = 0
    MIME_CLIP = 0
    MIME_QT_CONVERTOR = 0
    MIME_QT3_CONVERTOR = 0
    MIME_ALL = 0

    def __init__(self, t):
        '''void QMacPasteboardMime.__init__(int t)'''
    def __init__(self):
        '''QMacPasteboardMime QMacPasteboardMime.__init__()'''
        return QMacPasteboardMime()
    def count(self, mimeData):
        '''int QMacPasteboardMime.count(QMimeData mimeData)'''
        return int()
    def convertFromMime(self, mime, data, flav):
        '''abstract list-of-QByteArray QMacPasteboardMime.convertFromMime(str mime, QVariant data, str flav)'''
        return [QByteArray()]
    def convertToMime(self, mime, data, flav):
        '''abstract QVariant QMacPasteboardMime.convertToMime(str mime, list-of-QByteArray data, str flav)'''
        return QVariant()
    def flavorFor(self, mime):
        '''abstract str QMacPasteboardMime.flavorFor(str mime)'''
        return str()
    def mimeFor(self, flav):
        '''abstract str QMacPasteboardMime.mimeFor(str flav)'''
        return str()
    def canConvert(self, mime, flav):
        '''abstract bool QMacPasteboardMime.canConvert(str mime, str flav)'''
        return bool()
    def convertorName(self):
        '''abstract str QMacPasteboardMime.convertorName()'''
        return str()


class QMacToolBar(QObject):
    """"""
    def __init__(self, parent = None):
        '''void QMacToolBar.__init__(QObject parent = None)'''
    def __init__(self, identifier, parent = None):
        '''void QMacToolBar.__init__(str identifier, QObject parent = None)'''
    def nativeToolbar(self):
        '''NSToolbar QMacToolBar.nativeToolbar()'''
        return NSToolbar()
    def detachFromWindow(self):
        '''void QMacToolBar.detachFromWindow()'''
    def attachToWindow(self, window):
        '''void QMacToolBar.attachToWindow(QWindow window)'''
    def allowedItems(self):
        '''list-of-QMacToolBarItem QMacToolBar.allowedItems()'''
        return [QMacToolBarItem()]
    def setAllowedItems(self, allowedItems):
        '''void QMacToolBar.setAllowedItems(list-of-QMacToolBarItem allowedItems)'''
    def items(self):
        '''list-of-QMacToolBarItem QMacToolBar.items()'''
        return [QMacToolBarItem()]
    def setItems(self, items):
        '''void QMacToolBar.setItems(list-of-QMacToolBarItem items)'''
    def addSeparator(self):
        '''void QMacToolBar.addSeparator()'''
    def addAllowedItem(self, icon, text):
        '''QMacToolBarItem QMacToolBar.addAllowedItem(QIcon icon, str text)'''
        return QMacToolBarItem()
    def addItem(self, icon, text):
        '''QMacToolBarItem QMacToolBar.addItem(QIcon icon, str text)'''
        return QMacToolBarItem()


class QMacToolBarItem(QObject):
    """"""
    # Enum QMacToolBarItem.StandardItem
    NoStandardItem = 0
    Space = 0
    FlexibleSpace = 0

    def __init__(self, parent = None):
        '''void QMacToolBarItem.__init__(QObject parent = None)'''
    activated = pyqtSignal() # void activated() - signal
    def nativeToolBarItem(self):
        '''NSToolbarItem QMacToolBarItem.nativeToolBarItem()'''
        return NSToolbarItem()
    def setIcon(self, icon):
        '''void QMacToolBarItem.setIcon(QIcon icon)'''
    def icon(self):
        '''QIcon QMacToolBarItem.icon()'''
        return QIcon()
    def setText(self, text):
        '''void QMacToolBarItem.setText(str text)'''
    def text(self):
        '''str QMacToolBarItem.text()'''
        return str()
    def setStandardItem(self, standardItem):
        '''void QMacToolBarItem.setStandardItem(QMacToolBarItem.StandardItem standardItem)'''
    def standardItem(self):
        '''QMacToolBarItem.StandardItem QMacToolBarItem.standardItem()'''
        return QMacToolBarItem.StandardItem()
    def setSelectable(self, selectable):
        '''void QMacToolBarItem.setSelectable(bool selectable)'''
    def selectable(self):
        '''bool QMacToolBarItem.selectable()'''
        return bool()


def qRegisterDraggedTypes(types):
    '''static void qRegisterDraggedTypes(list-of-str types)'''


