class pyqtSignal():
 def connect(self, targetSignal): pass
 def emit(self, *args): pass
from QtCore import *

from QtWidgets import *

import datetime

class QVideoWidget(QWidget, QMediaBindableInterface):
    """"""
    def __init__(self, parent = None):
        '''void QVideoWidget.__init__(QWidget parent = None)'''
    def setMediaObject(self, object):
        '''bool QVideoWidget.setMediaObject(QMediaObject object)'''
        return bool()
    def paintEvent(self, event):
        '''void QVideoWidget.paintEvent(QPaintEvent event)'''
    def moveEvent(self, event):
        '''void QVideoWidget.moveEvent(QMoveEvent event)'''
    def resizeEvent(self, event):
        '''void QVideoWidget.resizeEvent(QResizeEvent event)'''
    def hideEvent(self, event):
        '''void QVideoWidget.hideEvent(QHideEvent event)'''
    def showEvent(self, event):
        '''void QVideoWidget.showEvent(QShowEvent event)'''
    def event(self, event):
        '''bool QVideoWidget.event(QEvent event)'''
        return bool()
    saturationChanged = pyqtSignal() # void saturationChanged(int) - signal
    hueChanged = pyqtSignal() # void hueChanged(int) - signal
    contrastChanged = pyqtSignal() # void contrastChanged(int) - signal
    brightnessChanged = pyqtSignal() # void brightnessChanged(int) - signal
    fullScreenChanged = pyqtSignal() # void fullScreenChanged(bool) - signal
    def setSaturation(self, saturation):
        '''void QVideoWidget.setSaturation(int saturation)'''
    def setHue(self, hue):
        '''void QVideoWidget.setHue(int hue)'''
    def setContrast(self, contrast):
        '''void QVideoWidget.setContrast(int contrast)'''
    def setBrightness(self, brightness):
        '''void QVideoWidget.setBrightness(int brightness)'''
    def setAspectRatioMode(self, mode):
        '''void QVideoWidget.setAspectRatioMode(Qt.AspectRatioMode mode)'''
    def setFullScreen(self, fullScreen):
        '''void QVideoWidget.setFullScreen(bool fullScreen)'''
    def sizeHint(self):
        '''QSize QVideoWidget.sizeHint()'''
        return QSize()
    def saturation(self):
        '''int QVideoWidget.saturation()'''
        return int()
    def hue(self):
        '''int QVideoWidget.hue()'''
        return int()
    def contrast(self):
        '''int QVideoWidget.contrast()'''
        return int()
    def brightness(self):
        '''int QVideoWidget.brightness()'''
        return int()
    def aspectRatioMode(self):
        '''Qt.AspectRatioMode QVideoWidget.aspectRatioMode()'''
        return Qt.AspectRatioMode()
    def mediaObject(self):
        '''QMediaObject QVideoWidget.mediaObject()'''
        return QMediaObject()


class QCameraViewfinder(QVideoWidget):
    """"""
    def __init__(self, parent = None):
        '''void QCameraViewfinder.__init__(QWidget parent = None)'''
    def setMediaObject(self, object):
        '''bool QCameraViewfinder.setMediaObject(QMediaObject object)'''
        return bool()
    def mediaObject(self):
        '''QMediaObject QCameraViewfinder.mediaObject()'''
        return QMediaObject()


class QGraphicsVideoItem(QGraphicsObject, QMediaBindableInterface):
    """"""
    def __init__(self, parent = None):
        '''void QGraphicsVideoItem.__init__(QGraphicsItem parent = None)'''
    def setMediaObject(self, object):
        '''bool QGraphicsVideoItem.setMediaObject(QMediaObject object)'''
        return bool()
    def itemChange(self, change, value):
        '''QVariant QGraphicsVideoItem.itemChange(QGraphicsItem.GraphicsItemChange change, QVariant value)'''
        return QVariant()
    def timerEvent(self, event):
        '''void QGraphicsVideoItem.timerEvent(QTimerEvent event)'''
    nativeSizeChanged = pyqtSignal() # void nativeSizeChanged(const QSizeFamp;) - signal
    def paint(self, painter, option, widget = None):
        '''void QGraphicsVideoItem.paint(QPainter painter, QStyleOptionGraphicsItem option, QWidget widget = None)'''
    def boundingRect(self):
        '''QRectF QGraphicsVideoItem.boundingRect()'''
        return QRectF()
    def nativeSize(self):
        '''QSizeF QGraphicsVideoItem.nativeSize()'''
        return QSizeF()
    def setSize(self, size):
        '''void QGraphicsVideoItem.setSize(QSizeF size)'''
    def size(self):
        '''QSizeF QGraphicsVideoItem.size()'''
        return QSizeF()
    def setOffset(self, offset):
        '''void QGraphicsVideoItem.setOffset(QPointF offset)'''
    def offset(self):
        '''QPointF QGraphicsVideoItem.offset()'''
        return QPointF()
    def setAspectRatioMode(self, mode):
        '''void QGraphicsVideoItem.setAspectRatioMode(Qt.AspectRatioMode mode)'''
    def aspectRatioMode(self):
        '''Qt.AspectRatioMode QGraphicsVideoItem.aspectRatioMode()'''
        return Qt.AspectRatioMode()
    def mediaObject(self):
        '''QMediaObject QGraphicsVideoItem.mediaObject()'''
        return QMediaObject()


