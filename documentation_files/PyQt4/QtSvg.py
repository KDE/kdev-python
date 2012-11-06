class pyqtSignal():
 def connect(self, targetSignal): pass
 def emit(self, *args): pass
from QtCore import *

class QGraphicsSvgItem(QGraphicsObject):
    """"""
    def __init__(self, parent = None):
        '''void QGraphicsSvgItem.__init__(QGraphicsItem parent = None)'''
    def __init__(self, fileName, parent = None):
        '''void QGraphicsSvgItem.__init__(QString fileName, QGraphicsItem parent = None)'''
    def type(self):
        '''int QGraphicsSvgItem.type()'''
        return int()
    def paint(self, painter, option, widget = None):
        '''void QGraphicsSvgItem.paint(QPainter painter, QStyleOptionGraphicsItem option, QWidget widget = None)'''
    def boundingRect(self):
        '''QRectF QGraphicsSvgItem.boundingRect()'''
        return QRectF()
    def maximumCacheSize(self):
        '''QSize QGraphicsSvgItem.maximumCacheSize()'''
        return QSize()
    def setMaximumCacheSize(self, size):
        '''void QGraphicsSvgItem.setMaximumCacheSize(QSize size)'''
    def isCachingEnabled(self):
        '''bool QGraphicsSvgItem.isCachingEnabled()'''
        return bool()
    def setCachingEnabled(self):
        '''bool QGraphicsSvgItem.setCachingEnabled()'''
        return bool()
    def elementId(self):
        '''QString QGraphicsSvgItem.elementId()'''
        return QString()
    def setElementId(self, id):
        '''void QGraphicsSvgItem.setElementId(QString id)'''
    def renderer(self):
        '''QSvgRenderer QGraphicsSvgItem.renderer()'''
        return QSvgRenderer()
    def setSharedRenderer(self, renderer):
        '''void QGraphicsSvgItem.setSharedRenderer(QSvgRenderer renderer)'''


class QSvgGenerator(QPaintDevice):
    """"""
    def __init__(self):
        '''void QSvgGenerator.__init__()'''
    def metric(self, metric):
        '''int QSvgGenerator.metric(QPaintDevice.PaintDeviceMetric metric)'''
        return int()
    def paintEngine(self):
        '''QPaintEngine QSvgGenerator.paintEngine()'''
        return QPaintEngine()
    def setViewBox(self, viewBox):
        '''void QSvgGenerator.setViewBox(QRect viewBox)'''
    def setViewBox(self, viewBox):
        '''void QSvgGenerator.setViewBox(QRectF viewBox)'''
    def viewBoxF(self):
        '''QRectF QSvgGenerator.viewBoxF()'''
        return QRectF()
    def viewBox(self):
        '''QRect QSvgGenerator.viewBox()'''
        return QRect()
    def setDescription(self, description):
        '''void QSvgGenerator.setDescription(QString description)'''
    def description(self):
        '''QString QSvgGenerator.description()'''
        return QString()
    def setTitle(self, title):
        '''void QSvgGenerator.setTitle(QString title)'''
    def title(self):
        '''QString QSvgGenerator.title()'''
        return QString()
    def setResolution(self, resolution):
        '''void QSvgGenerator.setResolution(int resolution)'''
    def resolution(self):
        '''int QSvgGenerator.resolution()'''
        return int()
    def setOutputDevice(self, outputDevice):
        '''void QSvgGenerator.setOutputDevice(QIODevice outputDevice)'''
    def outputDevice(self):
        '''QIODevice QSvgGenerator.outputDevice()'''
        return QIODevice()
    def setFileName(self, fileName):
        '''void QSvgGenerator.setFileName(QString fileName)'''
    def fileName(self):
        '''QString QSvgGenerator.fileName()'''
        return QString()
    def setSize(self, size):
        '''void QSvgGenerator.setSize(QSize size)'''
    def size(self):
        '''QSize QSvgGenerator.size()'''
        return QSize()


class QSvgRenderer(QObject):
    """"""
    def __init__(self, parent = None):
        '''void QSvgRenderer.__init__(QObject parent = None)'''
    def __init__(self, filename, parent = None):
        '''void QSvgRenderer.__init__(QString filename, QObject parent = None)'''
    def __init__(self, contents, parent = None):
        '''void QSvgRenderer.__init__(QByteArray contents, QObject parent = None)'''
    def __init__(self, contents, parent = None):
        '''void QSvgRenderer.__init__(QXmlStreamReader contents, QObject parent = None)'''
    repaintNeeded = pyqtSignal() # void repaintNeeded() - signal
    def render(self, p):
        '''void QSvgRenderer.render(QPainter p)'''
    def render(self, p, bounds):
        '''void QSvgRenderer.render(QPainter p, QRectF bounds)'''
    def render(self, painter, elementId, bounds = QRectF()):
        '''void QSvgRenderer.render(QPainter painter, QString elementId, QRectF bounds = QRectF())'''
    def load(self, filename):
        '''bool QSvgRenderer.load(QString filename)'''
        return bool()
    def load(self, contents):
        '''bool QSvgRenderer.load(QByteArray contents)'''
        return bool()
    def load(self, contents):
        '''bool QSvgRenderer.load(QXmlStreamReader contents)'''
        return bool()
    def animationDuration(self):
        '''int QSvgRenderer.animationDuration()'''
        return int()
    def setCurrentFrame(self):
        '''int QSvgRenderer.setCurrentFrame()'''
        return int()
    def currentFrame(self):
        '''int QSvgRenderer.currentFrame()'''
        return int()
    def setFramesPerSecond(self, num):
        '''void QSvgRenderer.setFramesPerSecond(int num)'''
    def framesPerSecond(self):
        '''int QSvgRenderer.framesPerSecond()'''
        return int()
    def boundsOnElement(self, id):
        '''QRectF QSvgRenderer.boundsOnElement(QString id)'''
        return QRectF()
    def animated(self):
        '''bool QSvgRenderer.animated()'''
        return bool()
    def setViewBox(self, viewbox):
        '''void QSvgRenderer.setViewBox(QRect viewbox)'''
    def setViewBox(self, viewbox):
        '''void QSvgRenderer.setViewBox(QRectF viewbox)'''
    def viewBoxF(self):
        '''QRectF QSvgRenderer.viewBoxF()'''
        return QRectF()
    def viewBox(self):
        '''QRect QSvgRenderer.viewBox()'''
        return QRect()
    def elementExists(self, id):
        '''bool QSvgRenderer.elementExists(QString id)'''
        return bool()
    def defaultSize(self):
        '''QSize QSvgRenderer.defaultSize()'''
        return QSize()
    def matrixForElement(self, id):
        '''QMatrix QSvgRenderer.matrixForElement(QString id)'''
        return QMatrix()
    def isValid(self):
        '''bool QSvgRenderer.isValid()'''
        return bool()


class QSvgWidget(QWidget):
    """"""
    def __init__(self, parent = None):
        '''void QSvgWidget.__init__(QWidget parent = None)'''
    def __init__(self, file, parent = None):
        '''void QSvgWidget.__init__(QString file, QWidget parent = None)'''
    def paintEvent(self, event):
        '''void QSvgWidget.paintEvent(QPaintEvent event)'''
    def load(self, file):
        '''void QSvgWidget.load(QString file)'''
    def load(self, contents):
        '''void QSvgWidget.load(QByteArray contents)'''
    def sizeHint(self):
        '''QSize QSvgWidget.sizeHint()'''
        return QSize()
    def renderer(self):
        '''QSvgRenderer QSvgWidget.renderer()'''
        return QSvgRenderer()


