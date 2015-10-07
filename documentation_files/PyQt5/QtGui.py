class pyqtSignal():
 def connect(self, targetSignal): pass
 def emit(self, *args): pass
from QtCore import *

from QtWidgets import *

import datetime

class QAbstractTextDocumentLayout(QObject):
    """"""
    def __init__(self, doc):
        '''void QAbstractTextDocumentLayout.__init__(QTextDocument doc)'''
    def format(self, pos):
        '''QTextCharFormat QAbstractTextDocumentLayout.format(int pos)'''
        return QTextCharFormat()
    def drawInlineObject(self, painter, rect, object, posInDocument, format):
        '''void QAbstractTextDocumentLayout.drawInlineObject(QPainter painter, QRectF rect, QTextInlineObject object, int posInDocument, QTextFormat format)'''
    def positionInlineObject(self, item, posInDocument, format):
        '''void QAbstractTextDocumentLayout.positionInlineObject(QTextInlineObject item, int posInDocument, QTextFormat format)'''
    def resizeInlineObject(self, item, posInDocument, format):
        '''void QAbstractTextDocumentLayout.resizeInlineObject(QTextInlineObject item, int posInDocument, QTextFormat format)'''
    def documentChanged(self, from_, charsRemoved, charsAdded):
        '''abstract void QAbstractTextDocumentLayout.documentChanged(int from, int charsRemoved, int charsAdded)'''
    updateBlock = pyqtSignal() # void updateBlock(const QTextBlockamp;) - signal
    pageCountChanged = pyqtSignal() # void pageCountChanged(int) - signal
    documentSizeChanged = pyqtSignal() # void documentSizeChanged(const QSizeFamp;) - signal
    update = pyqtSignal() # void update(const QRectFamp; = QRectF(0,0,1e+09,1e+09)) - signal
    def handlerForObject(self, objectType):
        '''QTextObjectInterface QAbstractTextDocumentLayout.handlerForObject(int objectType)'''
        return QTextObjectInterface()
    def unregisterHandler(self, objectType, component = None):
        '''void QAbstractTextDocumentLayout.unregisterHandler(int objectType, QObject component = None)'''
    def registerHandler(self, objectType, component):
        '''void QAbstractTextDocumentLayout.registerHandler(int objectType, QObject component)'''
    def document(self):
        '''QTextDocument QAbstractTextDocumentLayout.document()'''
        return QTextDocument()
    def paintDevice(self):
        '''QPaintDevice QAbstractTextDocumentLayout.paintDevice()'''
        return QPaintDevice()
    def setPaintDevice(self, device):
        '''void QAbstractTextDocumentLayout.setPaintDevice(QPaintDevice device)'''
    def blockBoundingRect(self, block):
        '''abstract QRectF QAbstractTextDocumentLayout.blockBoundingRect(QTextBlock block)'''
        return QRectF()
    def frameBoundingRect(self, frame):
        '''abstract QRectF QAbstractTextDocumentLayout.frameBoundingRect(QTextFrame frame)'''
        return QRectF()
    def documentSize(self):
        '''abstract QSizeF QAbstractTextDocumentLayout.documentSize()'''
        return QSizeF()
    def pageCount(self):
        '''abstract int QAbstractTextDocumentLayout.pageCount()'''
        return int()
    def anchorAt(self, pos):
        '''str QAbstractTextDocumentLayout.anchorAt(QPointF pos)'''
        return str()
    def hitTest(self, point, accuracy):
        '''abstract int QAbstractTextDocumentLayout.hitTest(QPointF point, Qt.HitTestAccuracy accuracy)'''
        return int()
    def draw(self, painter, context):
        '''abstract void QAbstractTextDocumentLayout.draw(QPainter painter, QAbstractTextDocumentLayout.PaintContext context)'''
    class PaintContext():
        """"""
        clip = None # QRectF - member
        cursorPosition = None # int - member
        palette = None # QPalette - member
        selections = None # list-of-QAbstractTextDocumentLayout.Selection - member
        def __init__(self):
            '''void QAbstractTextDocumentLayout.PaintContext.__init__()'''
        def __init__(self):
            '''QAbstractTextDocumentLayout.PaintContext QAbstractTextDocumentLayout.PaintContext.__init__()'''
            return QAbstractTextDocumentLayout.PaintContext()
    class Selection():
        """"""
        cursor = None # QTextCursor - member
        format = None # QTextCharFormat - member
        def __init__(self):
            '''void QAbstractTextDocumentLayout.Selection.__init__()'''
        def __init__(self):
            '''QAbstractTextDocumentLayout.Selection QAbstractTextDocumentLayout.Selection.__init__()'''
            return QAbstractTextDocumentLayout.Selection()


class QTextObjectInterface():
    """"""
    def __init__(self):
        '''void QTextObjectInterface.__init__()'''
    def __init__(self):
        '''QTextObjectInterface QTextObjectInterface.__init__()'''
        return QTextObjectInterface()
    def drawObject(self, painter, rect, doc, posInDocument, format):
        '''abstract void QTextObjectInterface.drawObject(QPainter painter, QRectF rect, QTextDocument doc, int posInDocument, QTextFormat format)'''
    def intrinsicSize(self, doc, posInDocument, format):
        '''abstract QSizeF QTextObjectInterface.intrinsicSize(QTextDocument doc, int posInDocument, QTextFormat format)'''
        return QSizeF()


class QBackingStore():
    """"""
    def __init__(self, window):
        '''void QBackingStore.__init__(QWindow window)'''
    def hasStaticContents(self):
        '''bool QBackingStore.hasStaticContents()'''
        return bool()
    def staticContents(self):
        '''QRegion QBackingStore.staticContents()'''
        return QRegion()
    def setStaticContents(self, region):
        '''void QBackingStore.setStaticContents(QRegion region)'''
    def endPaint(self):
        '''void QBackingStore.endPaint()'''
    def beginPaint(self):
        '''QRegion QBackingStore.beginPaint()'''
        return QRegion()
    def scroll(self, area, dx, dy):
        '''bool QBackingStore.scroll(QRegion area, int dx, int dy)'''
        return bool()
    def size(self):
        '''QSize QBackingStore.size()'''
        return QSize()
    def resize(self, size):
        '''void QBackingStore.resize(QSize size)'''
    def flush(self, region, window = None, offset = QPoint()):
        '''void QBackingStore.flush(QRegion region, QWindow window = None, QPoint offset = QPoint())'''
    def paintDevice(self):
        '''QPaintDevice QBackingStore.paintDevice()'''
        return QPaintDevice()
    def window(self):
        '''QWindow QBackingStore.window()'''
        return QWindow()


class QPaintDevice():
    """"""
    # Enum QPaintDevice.PaintDeviceMetric
    PdmWidth = 0
    PdmHeight = 0
    PdmWidthMM = 0
    PdmHeightMM = 0
    PdmNumColors = 0
    PdmDepth = 0
    PdmDpiX = 0
    PdmDpiY = 0
    PdmPhysicalDpiX = 0
    PdmPhysicalDpiY = 0
    PdmDevicePixelRatio = 0

    def __init__(self):
        '''void QPaintDevice.__init__()'''
    def metric(self, metric):
        '''int QPaintDevice.metric(QPaintDevice.PaintDeviceMetric metric)'''
        return int()
    def devicePixelRatio(self):
        '''int QPaintDevice.devicePixelRatio()'''
        return int()
    def colorCount(self):
        '''int QPaintDevice.colorCount()'''
        return int()
    def paintingActive(self):
        '''bool QPaintDevice.paintingActive()'''
        return bool()
    def depth(self):
        '''int QPaintDevice.depth()'''
        return int()
    def physicalDpiY(self):
        '''int QPaintDevice.physicalDpiY()'''
        return int()
    def physicalDpiX(self):
        '''int QPaintDevice.physicalDpiX()'''
        return int()
    def logicalDpiY(self):
        '''int QPaintDevice.logicalDpiY()'''
        return int()
    def logicalDpiX(self):
        '''int QPaintDevice.logicalDpiX()'''
        return int()
    def heightMM(self):
        '''int QPaintDevice.heightMM()'''
        return int()
    def widthMM(self):
        '''int QPaintDevice.widthMM()'''
        return int()
    def height(self):
        '''int QPaintDevice.height()'''
        return int()
    def width(self):
        '''int QPaintDevice.width()'''
        return int()
    def paintEngine(self):
        '''abstract QPaintEngine QPaintDevice.paintEngine()'''
        return QPaintEngine()


class QPixmap(QPaintDevice):
    """"""
    def __init__(self):
        '''void QPixmap.__init__()'''
    def __init__(self, w, h):
        '''void QPixmap.__init__(int w, int h)'''
    def __init__(self):
        '''QSize QPixmap.__init__()'''
        return QSize()
    def __init__(self, fileName, format = None, flags = None):
        '''void QPixmap.__init__(str fileName, str format = None, Qt.ImageConversionFlags flags = Qt.AutoColor)'''
    def __init__(self, xpm):
        '''void QPixmap.__init__(list-of-str xpm)'''
    def __init__(self):
        '''QPixmap QPixmap.__init__()'''
        return QPixmap()
    def __init__(self, variant):
        '''void QPixmap.__init__(QVariant variant)'''
    def setDevicePixelRatio(self, scaleFactor):
        '''void QPixmap.setDevicePixelRatio(float scaleFactor)'''
    def devicePixelRatio(self):
        '''float QPixmap.devicePixelRatio()'''
        return float()
    def swap(self, other):
        '''void QPixmap.swap(QPixmap other)'''
    def scroll(self, dx, dy, rect, exposed):
        '''void QPixmap.scroll(int dx, int dy, QRect rect, QRegion exposed)'''
    def scroll(self, dx, dy, x, y, width, height, exposed):
        '''void QPixmap.scroll(int dx, int dy, int x, int y, int width, int height, QRegion exposed)'''
    def cacheKey(self):
        '''int QPixmap.cacheKey()'''
        return int()
    def trueMatrix(self, m, w, h):
        '''static QTransform QPixmap.trueMatrix(QTransform m, int w, int h)'''
        return QTransform()
    def transformed(self, transform, mode = None):
        '''QPixmap QPixmap.transformed(QTransform transform, Qt.TransformationMode mode = Qt.FastTransformation)'''
        return QPixmap()
    def metric(self):
        '''QPaintDevice.PaintDeviceMetric QPixmap.metric()'''
        return QPaintDevice.PaintDeviceMetric()
    def paintEngine(self):
        '''QPaintEngine QPixmap.paintEngine()'''
        return QPaintEngine()
    def isQBitmap(self):
        '''bool QPixmap.isQBitmap()'''
        return bool()
    def detach(self):
        '''void QPixmap.detach()'''
    def copy(self, rect = QRect()):
        '''QPixmap QPixmap.copy(QRect rect = QRect())'''
        return QPixmap()
    def copy(self, ax, ay, awidth, aheight):
        '''QPixmap QPixmap.copy(int ax, int ay, int awidth, int aheight)'''
        return QPixmap()
    def save(self, fileName, format = None, quality = None):
        '''bool QPixmap.save(str fileName, str format = None, int quality = -1)'''
        return bool()
    def save(self, device, format = None, quality = None):
        '''bool QPixmap.save(QIODevice device, str format = None, int quality = -1)'''
        return bool()
    def loadFromData(self, buf, format = None, flags = None):
        '''bool QPixmap.loadFromData(str buf, str format = None, Qt.ImageConversionFlags flags = Qt.AutoColor)'''
        return bool()
    def loadFromData(self, buf, format = None, flags = None):
        '''bool QPixmap.loadFromData(QByteArray buf, str format = None, Qt.ImageConversionFlags flags = Qt.AutoColor)'''
        return bool()
    def load(self, fileName, format = None, flags = None):
        '''bool QPixmap.load(str fileName, str format = None, Qt.ImageConversionFlags flags = Qt.AutoColor)'''
        return bool()
    def convertFromImage(self, img, flags = None):
        '''bool QPixmap.convertFromImage(QImage img, Qt.ImageConversionFlags flags = Qt.AutoColor)'''
        return bool()
    def fromImageReader(self, imageReader, flags = None):
        '''static QPixmap QPixmap.fromImageReader(QImageReader imageReader, Qt.ImageConversionFlags flags = Qt.AutoColor)'''
        return QPixmap()
    def fromImage(self, image, flags = None):
        '''static QPixmap QPixmap.fromImage(QImage image, Qt.ImageConversionFlags flags = Qt.AutoColor)'''
        return QPixmap()
    def toImage(self):
        '''QImage QPixmap.toImage()'''
        return QImage()
    def scaledToHeight(self, height, mode = None):
        '''QPixmap QPixmap.scaledToHeight(int height, Qt.TransformationMode mode = Qt.FastTransformation)'''
        return QPixmap()
    def scaledToWidth(self, width, mode = None):
        '''QPixmap QPixmap.scaledToWidth(int width, Qt.TransformationMode mode = Qt.FastTransformation)'''
        return QPixmap()
    def scaled(self, width, height, aspectRatioMode = None, transformMode = None):
        '''QPixmap QPixmap.scaled(int width, int height, Qt.AspectRatioMode aspectRatioMode = Qt.IgnoreAspectRatio, Qt.TransformationMode transformMode = Qt.FastTransformation)'''
        return QPixmap()
    def scaled(self, size, aspectRatioMode = None, transformMode = None):
        '''QPixmap QPixmap.scaled(QSize size, Qt.AspectRatioMode aspectRatioMode = Qt.IgnoreAspectRatio, Qt.TransformationMode transformMode = Qt.FastTransformation)'''
        return QPixmap()
    def createMaskFromColor(self, maskColor, mode = None):
        '''QBitmap QPixmap.createMaskFromColor(QColor maskColor, Qt.MaskMode mode = Qt.MaskInColor)'''
        return QBitmap()
    def createHeuristicMask(self, clipTight = True):
        '''QBitmap QPixmap.createHeuristicMask(bool clipTight = True)'''
        return QBitmap()
    def hasAlphaChannel(self):
        '''bool QPixmap.hasAlphaChannel()'''
        return bool()
    def hasAlpha(self):
        '''bool QPixmap.hasAlpha()'''
        return bool()
    def setMask(self):
        '''QBitmap QPixmap.setMask()'''
        return QBitmap()
    def mask(self):
        '''QBitmap QPixmap.mask()'''
        return QBitmap()
    def fill(self, color = None):
        '''void QPixmap.fill(QColor color = Qt.white)'''
    def defaultDepth(self):
        '''static int QPixmap.defaultDepth()'''
        return int()
    def depth(self):
        '''int QPixmap.depth()'''
        return int()
    def rect(self):
        '''QRect QPixmap.rect()'''
        return QRect()
    def size(self):
        '''QSize QPixmap.size()'''
        return QSize()
    def height(self):
        '''int QPixmap.height()'''
        return int()
    def width(self):
        '''int QPixmap.width()'''
        return int()
    def devType(self):
        '''int QPixmap.devType()'''
        return int()
    def isNull(self):
        '''bool QPixmap.isNull()'''
        return bool()


class QBitmap(QPixmap):
    """"""
    def __init__(self):
        '''void QBitmap.__init__()'''
    def __init__(self):
        '''QPixmap QBitmap.__init__()'''
        return QPixmap()
    def __init__(self, w, h):
        '''void QBitmap.__init__(int w, int h)'''
    def __init__(self):
        '''QSize QBitmap.__init__()'''
        return QSize()
    def __init__(self, fileName, format = None):
        '''void QBitmap.__init__(str fileName, str format = None)'''
    def __init__(self, variant):
        '''void QBitmap.__init__(QVariant variant)'''
    def __init__(self):
        '''QBitmap QBitmap.__init__()'''
        return QBitmap()
    def swap(self, other):
        '''void QBitmap.swap(QBitmap other)'''
    def transformed(self, matrix):
        '''QBitmap QBitmap.transformed(QTransform matrix)'''
        return QBitmap()
    def fromData(self, size, bits, format = None):
        '''static QBitmap QBitmap.fromData(QSize size, str bits, QImage.Format format = QImage.Format_MonoLSB)'''
        return QBitmap()
    def fromImage(self, image, flags = None):
        '''static QBitmap QBitmap.fromImage(QImage image, Qt.ImageConversionFlags flags = Qt.AutoColor)'''
        return QBitmap()
    def clear(self):
        '''void QBitmap.clear()'''


class QColor():
    """"""
    # Enum QColor.NameFormat
    HexRgb = 0
    HexArgb = 0

    # Enum QColor.Spec
    Invalid = 0
    Rgb = 0
    Hsv = 0
    Cmyk = 0
    Hsl = 0

    def __init__(self, color):
        '''void QColor.__init__(Qt.GlobalColor color)'''
    def __init__(self, rgb):
        '''void QColor.__init__(int rgb)'''
    def __init__(self, variant):
        '''void QColor.__init__(QVariant variant)'''
    def __init__(self):
        '''void QColor.__init__()'''
    def __init__(self, r, g, b, alpha = 255):
        '''void QColor.__init__(int r, int g, int b, int alpha = 255)'''
    def __init__(self, aname):
        '''void QColor.__init__(str aname)'''
    def __init__(self, acolor):
        '''void QColor.__init__(QColor acolor)'''
    def isValidColor(self, name):
        '''static bool QColor.isValidColor(str name)'''
        return bool()
    def fromHslF(self, h, s, l, alpha = 1):
        '''static QColor QColor.fromHslF(float h, float s, float l, float alpha = 1)'''
        return QColor()
    def fromHsl(self, h, s, l, alpha = 255):
        '''static QColor QColor.fromHsl(int h, int s, int l, int alpha = 255)'''
        return QColor()
    def toHsl(self):
        '''QColor QColor.toHsl()'''
        return QColor()
    def setHslF(self, h, s, l, alpha = 1):
        '''void QColor.setHslF(float h, float s, float l, float alpha = 1)'''
    def getHslF(self, h, s, l, alpha):
        '''void QColor.getHslF(float h, float s, float l, float alpha)'''
    def setHsl(self, h, s, l, alpha = 255):
        '''void QColor.setHsl(int h, int s, int l, int alpha = 255)'''
    def getHsl(self, h, s, l, alpha):
        '''void QColor.getHsl(int h, int s, int l, int alpha)'''
    def lightnessF(self):
        '''float QColor.lightnessF()'''
        return float()
    def hslSaturationF(self):
        '''float QColor.hslSaturationF()'''
        return float()
    def hslHueF(self):
        '''float QColor.hslHueF()'''
        return float()
    def lightness(self):
        '''int QColor.lightness()'''
        return int()
    def hslSaturation(self):
        '''int QColor.hslSaturation()'''
        return int()
    def hslHue(self):
        '''int QColor.hslHue()'''
        return int()
    def hsvSaturationF(self):
        '''float QColor.hsvSaturationF()'''
        return float()
    def hsvHueF(self):
        '''float QColor.hsvHueF()'''
        return float()
    def hsvSaturation(self):
        '''int QColor.hsvSaturation()'''
        return int()
    def hsvHue(self):
        '''int QColor.hsvHue()'''
        return int()
    def darker(self, factor = 200):
        '''QColor QColor.darker(int factor = 200)'''
        return QColor()
    def lighter(self, factor = 150):
        '''QColor QColor.lighter(int factor = 150)'''
        return QColor()
    def isValid(self):
        '''bool QColor.isValid()'''
        return bool()
    def __ne__(self, c):
        '''bool QColor.__ne__(QColor c)'''
        return bool()
    def __eq__(self, c):
        '''bool QColor.__eq__(QColor c)'''
        return bool()
    def fromCmykF(self, c, m, y, k, alpha = 1):
        '''static QColor QColor.fromCmykF(float c, float m, float y, float k, float alpha = 1)'''
        return QColor()
    def fromCmyk(self, c, m, y, k, alpha = 255):
        '''static QColor QColor.fromCmyk(int c, int m, int y, int k, int alpha = 255)'''
        return QColor()
    def fromHsvF(self, h, s, v, alpha = 1):
        '''static QColor QColor.fromHsvF(float h, float s, float v, float alpha = 1)'''
        return QColor()
    def fromHsv(self, h, s, v, alpha = 255):
        '''static QColor QColor.fromHsv(int h, int s, int v, int alpha = 255)'''
        return QColor()
    def fromRgbF(self, r, g, b, alpha = 1):
        '''static QColor QColor.fromRgbF(float r, float g, float b, float alpha = 1)'''
        return QColor()
    def fromRgba(self, rgba):
        '''static QColor QColor.fromRgba(int rgba)'''
        return QColor()
    def fromRgb(self, rgb):
        '''static QColor QColor.fromRgb(int rgb)'''
        return QColor()
    def fromRgb(self, r, g, b, alpha = 255):
        '''static QColor QColor.fromRgb(int r, int g, int b, int alpha = 255)'''
        return QColor()
    def convertTo(self, colorSpec):
        '''QColor QColor.convertTo(QColor.Spec colorSpec)'''
        return QColor()
    def toCmyk(self):
        '''QColor QColor.toCmyk()'''
        return QColor()
    def toHsv(self):
        '''QColor QColor.toHsv()'''
        return QColor()
    def toRgb(self):
        '''QColor QColor.toRgb()'''
        return QColor()
    def setCmykF(self, c, m, y, k, alpha = 1):
        '''void QColor.setCmykF(float c, float m, float y, float k, float alpha = 1)'''
    def getCmykF(self, c, m, y, k, alpha):
        '''void QColor.getCmykF(float c, float m, float y, float k, float alpha)'''
    def setCmyk(self, c, m, y, k, alpha = 255):
        '''void QColor.setCmyk(int c, int m, int y, int k, int alpha = 255)'''
    def getCmyk(self, c, m, y, k, alpha):
        '''void QColor.getCmyk(int c, int m, int y, int k, int alpha)'''
    def blackF(self):
        '''float QColor.blackF()'''
        return float()
    def yellowF(self):
        '''float QColor.yellowF()'''
        return float()
    def magentaF(self):
        '''float QColor.magentaF()'''
        return float()
    def cyanF(self):
        '''float QColor.cyanF()'''
        return float()
    def black(self):
        '''int QColor.black()'''
        return int()
    def yellow(self):
        '''int QColor.yellow()'''
        return int()
    def magenta(self):
        '''int QColor.magenta()'''
        return int()
    def cyan(self):
        '''int QColor.cyan()'''
        return int()
    def setHsvF(self, h, s, v, alpha = 1):
        '''void QColor.setHsvF(float h, float s, float v, float alpha = 1)'''
    def getHsvF(self, h, s, v, alpha):
        '''void QColor.getHsvF(float h, float s, float v, float alpha)'''
    def setHsv(self, h, s, v, alpha = 255):
        '''void QColor.setHsv(int h, int s, int v, int alpha = 255)'''
    def getHsv(self, h, s, v, alpha):
        '''void QColor.getHsv(int h, int s, int v, int alpha)'''
    def valueF(self):
        '''float QColor.valueF()'''
        return float()
    def saturationF(self):
        '''float QColor.saturationF()'''
        return float()
    def hueF(self):
        '''float QColor.hueF()'''
        return float()
    def value(self):
        '''int QColor.value()'''
        return int()
    def saturation(self):
        '''int QColor.saturation()'''
        return int()
    def hue(self):
        '''int QColor.hue()'''
        return int()
    def rgb(self):
        '''int QColor.rgb()'''
        return int()
    def setRgba(self, rgba):
        '''void QColor.setRgba(int rgba)'''
    def rgba(self):
        '''int QColor.rgba()'''
        return int()
    def setRgbF(self, r, g, b, alpha = 1):
        '''void QColor.setRgbF(float r, float g, float b, float alpha = 1)'''
    def getRgbF(self, r, g, b, alpha):
        '''void QColor.getRgbF(float r, float g, float b, float alpha)'''
    def setRgb(self, r, g, b, alpha = 255):
        '''void QColor.setRgb(int r, int g, int b, int alpha = 255)'''
    def setRgb(self, rgb):
        '''void QColor.setRgb(int rgb)'''
    def getRgb(self, r, g, b, alpha):
        '''void QColor.getRgb(int r, int g, int b, int alpha)'''
    def setBlueF(self, blue):
        '''void QColor.setBlueF(float blue)'''
    def setGreenF(self, green):
        '''void QColor.setGreenF(float green)'''
    def setRedF(self, red):
        '''void QColor.setRedF(float red)'''
    def blueF(self):
        '''float QColor.blueF()'''
        return float()
    def greenF(self):
        '''float QColor.greenF()'''
        return float()
    def redF(self):
        '''float QColor.redF()'''
        return float()
    def setBlue(self, blue):
        '''void QColor.setBlue(int blue)'''
    def setGreen(self, green):
        '''void QColor.setGreen(int green)'''
    def setRed(self, red):
        '''void QColor.setRed(int red)'''
    def blue(self):
        '''int QColor.blue()'''
        return int()
    def green(self):
        '''int QColor.green()'''
        return int()
    def red(self):
        '''int QColor.red()'''
        return int()
    def setAlphaF(self, alpha):
        '''void QColor.setAlphaF(float alpha)'''
    def alphaF(self):
        '''float QColor.alphaF()'''
        return float()
    def setAlpha(self, alpha):
        '''void QColor.setAlpha(int alpha)'''
    def alpha(self):
        '''int QColor.alpha()'''
        return int()
    def spec(self):
        '''QColor.Spec QColor.spec()'''
        return QColor.Spec()
    def colorNames(self):
        '''static list-of-str QColor.colorNames()'''
        return [str()]
    def setNamedColor(self, name):
        '''void QColor.setNamedColor(str name)'''
    def name(self):
        '''str QColor.name()'''
        return str()
    def name(self, format):
        '''str QColor.name(QColor.NameFormat format)'''
        return str()


class QBrush():
    """"""
    def __init__(self):
        '''void QBrush.__init__()'''
    def __init__(self, bs):
        '''void QBrush.__init__(Qt.BrushStyle bs)'''
    def __init__(self, color, style = None):
        '''void QBrush.__init__(QColor color, Qt.BrushStyle style = Qt.SolidPattern)'''
    def __init__(self, color, style = None):
        '''void QBrush.__init__(Qt.GlobalColor color, Qt.BrushStyle style = Qt.SolidPattern)'''
    def __init__(self, color, pixmap):
        '''void QBrush.__init__(QColor color, QPixmap pixmap)'''
    def __init__(self, color, pixmap):
        '''void QBrush.__init__(Qt.GlobalColor color, QPixmap pixmap)'''
    def __init__(self, pixmap):
        '''void QBrush.__init__(QPixmap pixmap)'''
    def __init__(self, image):
        '''void QBrush.__init__(QImage image)'''
    def __init__(self, gradient):
        '''void QBrush.__init__(QGradient gradient)'''
    def __init__(self, brush):
        '''void QBrush.__init__(QBrush brush)'''
    def __init__(self, variant):
        '''void QBrush.__init__(QVariant variant)'''
    def swap(self, other):
        '''void QBrush.swap(QBrush other)'''
    def transform(self):
        '''QTransform QBrush.transform()'''
        return QTransform()
    def setTransform(self):
        '''QTransform QBrush.setTransform()'''
        return QTransform()
    def textureImage(self):
        '''QImage QBrush.textureImage()'''
        return QImage()
    def setTextureImage(self, image):
        '''void QBrush.setTextureImage(QImage image)'''
    def color(self):
        '''QColor QBrush.color()'''
        return QColor()
    def style(self):
        '''Qt.BrushStyle QBrush.style()'''
        return Qt.BrushStyle()
    def __ne__(self, b):
        '''bool QBrush.__ne__(QBrush b)'''
        return bool()
    def __eq__(self, b):
        '''bool QBrush.__eq__(QBrush b)'''
        return bool()
    def isOpaque(self):
        '''bool QBrush.isOpaque()'''
        return bool()
    def gradient(self):
        '''QGradient QBrush.gradient()'''
        return QGradient()
    def setColor(self, color):
        '''void QBrush.setColor(QColor color)'''
    def setColor(self, acolor):
        '''void QBrush.setColor(Qt.GlobalColor acolor)'''
    def setTexture(self, pixmap):
        '''void QBrush.setTexture(QPixmap pixmap)'''
    def texture(self):
        '''QPixmap QBrush.texture()'''
        return QPixmap()
    def setStyle(self):
        '''Qt.BrushStyle QBrush.setStyle()'''
        return Qt.BrushStyle()


class QGradient():
    """"""
    # Enum QGradient.Spread
    PadSpread = 0
    ReflectSpread = 0
    RepeatSpread = 0

    # Enum QGradient.Type
    LinearGradient = 0
    RadialGradient = 0
    ConicalGradient = 0
    NoGradient = 0

    # Enum QGradient.CoordinateMode
    LogicalMode = 0
    StretchToDeviceMode = 0
    ObjectBoundingMode = 0

    def __init__(self):
        '''void QGradient.__init__()'''
    def __init__(self):
        '''QGradient QGradient.__init__()'''
        return QGradient()
    def setCoordinateMode(self, mode):
        '''void QGradient.setCoordinateMode(QGradient.CoordinateMode mode)'''
    def coordinateMode(self):
        '''QGradient.CoordinateMode QGradient.coordinateMode()'''
        return QGradient.CoordinateMode()
    def setSpread(self, aspread):
        '''void QGradient.setSpread(QGradient.Spread aspread)'''
    def __ne__(self, other):
        '''bool QGradient.__ne__(QGradient other)'''
        return bool()
    def __eq__(self, gradient):
        '''bool QGradient.__eq__(QGradient gradient)'''
        return bool()
    def stops(self):
        '''list-of-tuple-of-float-QColor QGradient.stops()'''
        return [tuple-of-float-QColor()]
    def setStops(self, stops):
        '''void QGradient.setStops(list-of-tuple-of-float-QColor stops)'''
    def setColorAt(self, pos, color):
        '''void QGradient.setColorAt(float pos, QColor color)'''
    def spread(self):
        '''QGradient.Spread QGradient.spread()'''
        return QGradient.Spread()
    def type(self):
        '''QGradient.Type QGradient.type()'''
        return QGradient.Type()


class QLinearGradient(QGradient):
    """"""
    def __init__(self):
        '''void QLinearGradient.__init__()'''
    def __init__(self, start, finalStop):
        '''void QLinearGradient.__init__(QPointF start, QPointF finalStop)'''
    def __init__(self, xStart, yStart, xFinalStop, yFinalStop):
        '''void QLinearGradient.__init__(float xStart, float yStart, float xFinalStop, float yFinalStop)'''
    def __init__(self):
        '''QLinearGradient QLinearGradient.__init__()'''
        return QLinearGradient()
    def setFinalStop(self, stop):
        '''void QLinearGradient.setFinalStop(QPointF stop)'''
    def setFinalStop(self, x, y):
        '''void QLinearGradient.setFinalStop(float x, float y)'''
    def setStart(self, start):
        '''void QLinearGradient.setStart(QPointF start)'''
    def setStart(self, x, y):
        '''void QLinearGradient.setStart(float x, float y)'''
    def finalStop(self):
        '''QPointF QLinearGradient.finalStop()'''
        return QPointF()
    def start(self):
        '''QPointF QLinearGradient.start()'''
        return QPointF()


class QRadialGradient(QGradient):
    """"""
    def __init__(self):
        '''void QRadialGradient.__init__()'''
    def __init__(self, center, radius, focalPoint):
        '''void QRadialGradient.__init__(QPointF center, float radius, QPointF focalPoint)'''
    def __init__(self, center, centerRadius, focalPoint, focalRadius):
        '''void QRadialGradient.__init__(QPointF center, float centerRadius, QPointF focalPoint, float focalRadius)'''
    def __init__(self, center, radius):
        '''void QRadialGradient.__init__(QPointF center, float radius)'''
    def __init__(self, cx, cy, radius, fx, fy):
        '''void QRadialGradient.__init__(float cx, float cy, float radius, float fx, float fy)'''
    def __init__(self, cx, cy, centerRadius, fx, fy, focalRadius):
        '''void QRadialGradient.__init__(float cx, float cy, float centerRadius, float fx, float fy, float focalRadius)'''
    def __init__(self, cx, cy, radius):
        '''void QRadialGradient.__init__(float cx, float cy, float radius)'''
    def __init__(self):
        '''QRadialGradient QRadialGradient.__init__()'''
        return QRadialGradient()
    def setFocalRadius(self, radius):
        '''void QRadialGradient.setFocalRadius(float radius)'''
    def focalRadius(self):
        '''float QRadialGradient.focalRadius()'''
        return float()
    def setCenterRadius(self, radius):
        '''void QRadialGradient.setCenterRadius(float radius)'''
    def centerRadius(self):
        '''float QRadialGradient.centerRadius()'''
        return float()
    def setRadius(self, radius):
        '''void QRadialGradient.setRadius(float radius)'''
    def setFocalPoint(self, focalPoint):
        '''void QRadialGradient.setFocalPoint(QPointF focalPoint)'''
    def setFocalPoint(self, x, y):
        '''void QRadialGradient.setFocalPoint(float x, float y)'''
    def setCenter(self, center):
        '''void QRadialGradient.setCenter(QPointF center)'''
    def setCenter(self, x, y):
        '''void QRadialGradient.setCenter(float x, float y)'''
    def radius(self):
        '''float QRadialGradient.radius()'''
        return float()
    def focalPoint(self):
        '''QPointF QRadialGradient.focalPoint()'''
        return QPointF()
    def center(self):
        '''QPointF QRadialGradient.center()'''
        return QPointF()


class QConicalGradient(QGradient):
    """"""
    def __init__(self):
        '''void QConicalGradient.__init__()'''
    def __init__(self, center, startAngle):
        '''void QConicalGradient.__init__(QPointF center, float startAngle)'''
    def __init__(self, cx, cy, startAngle):
        '''void QConicalGradient.__init__(float cx, float cy, float startAngle)'''
    def __init__(self):
        '''QConicalGradient QConicalGradient.__init__()'''
        return QConicalGradient()
    def setAngle(self, angle):
        '''void QConicalGradient.setAngle(float angle)'''
    def setCenter(self, center):
        '''void QConicalGradient.setCenter(QPointF center)'''
    def setCenter(self, x, y):
        '''void QConicalGradient.setCenter(float x, float y)'''
    def angle(self):
        '''float QConicalGradient.angle()'''
        return float()
    def center(self):
        '''QPointF QConicalGradient.center()'''
        return QPointF()


class QClipboard(QObject):
    """"""
    # Enum QClipboard.Mode
    Clipboard = 0
    Selection = 0
    FindBuffer = 0

    selectionChanged = pyqtSignal() # void selectionChanged() - signal
    findBufferChanged = pyqtSignal() # void findBufferChanged() - signal
    dataChanged = pyqtSignal() # void dataChanged() - signal
    changed = pyqtSignal() # void changed(QClipboard::Mode) - signal
    def setPixmap(self, mode = None):
        '''QPixmap QClipboard.setPixmap(QClipboard.Mode mode = QClipboard.Clipboard)'''
        return QPixmap()
    def setImage(self, mode = None):
        '''QImage QClipboard.setImage(QClipboard.Mode mode = QClipboard.Clipboard)'''
        return QImage()
    def pixmap(self, mode = None):
        '''QPixmap QClipboard.pixmap(QClipboard.Mode mode = QClipboard.Clipboard)'''
        return QPixmap()
    def image(self, mode = None):
        '''QImage QClipboard.image(QClipboard.Mode mode = QClipboard.Clipboard)'''
        return QImage()
    def setMimeData(self, data, mode = None):
        '''void QClipboard.setMimeData(QMimeData data, QClipboard.Mode mode = QClipboard.Clipboard)'''
    def mimeData(self, mode = None):
        '''QMimeData QClipboard.mimeData(QClipboard.Mode mode = QClipboard.Clipboard)'''
        return QMimeData()
    def setText(self, mode = None):
        '''str QClipboard.setText(QClipboard.Mode mode = QClipboard.Clipboard)'''
        return str()
    def text(self, mode = None):
        '''str QClipboard.text(QClipboard.Mode mode = QClipboard.Clipboard)'''
        return str()
    def text(self, subtype, mode = None):
        '''(str, str) QClipboard.text(str subtype, QClipboard.Mode mode = QClipboard.Clipboard)'''
        return (str, str)()
    def ownsSelection(self):
        '''bool QClipboard.ownsSelection()'''
        return bool()
    def ownsFindBuffer(self):
        '''bool QClipboard.ownsFindBuffer()'''
        return bool()
    def ownsClipboard(self):
        '''bool QClipboard.ownsClipboard()'''
        return bool()
    def supportsSelection(self):
        '''bool QClipboard.supportsSelection()'''
        return bool()
    def supportsFindBuffer(self):
        '''bool QClipboard.supportsFindBuffer()'''
        return bool()
    def clear(self, mode = None):
        '''void QClipboard.clear(QClipboard.Mode mode = QClipboard.Clipboard)'''


class QCursor():
    """"""
    def __init__(self):
        '''void QCursor.__init__()'''
    def __init__(self, shape):
        '''void QCursor.__init__(Qt.CursorShape shape)'''
    def __init__(self, bitmap, mask, hotX = None, hotY = None):
        '''void QCursor.__init__(QBitmap bitmap, QBitmap mask, int hotX = -1, int hotY = -1)'''
    def __init__(self, pixmap, hotX = None, hotY = None):
        '''void QCursor.__init__(QPixmap pixmap, int hotX = -1, int hotY = -1)'''
    def __init__(self, cursor):
        '''void QCursor.__init__(QCursor cursor)'''
    def __init__(self, variant):
        '''void QCursor.__init__(QVariant variant)'''
    def setPos(self, x, y):
        '''static void QCursor.setPos(int x, int y)'''
    def setPos(self, p):
        '''static void QCursor.setPos(QPoint p)'''
    def pos(self):
        '''static QPoint QCursor.pos()'''
        return QPoint()
    def hotSpot(self):
        '''QPoint QCursor.hotSpot()'''
        return QPoint()
    def pixmap(self):
        '''QPixmap QCursor.pixmap()'''
        return QPixmap()
    def mask(self):
        '''QBitmap QCursor.mask()'''
        return QBitmap()
    def bitmap(self):
        '''QBitmap QCursor.bitmap()'''
        return QBitmap()
    def setShape(self, newShape):
        '''void QCursor.setShape(Qt.CursorShape newShape)'''
    def shape(self):
        '''Qt.CursorShape QCursor.shape()'''
        return Qt.CursorShape()


class QDesktopServices():
    """"""
    def __init__(self):
        '''void QDesktopServices.__init__()'''
    def __init__(self):
        '''QDesktopServices QDesktopServices.__init__()'''
        return QDesktopServices()
    def unsetUrlHandler(self, scheme):
        '''static void QDesktopServices.unsetUrlHandler(str scheme)'''
    def setUrlHandler(self, scheme, receiver, method):
        '''static void QDesktopServices.setUrlHandler(str scheme, QObject receiver, str method)'''
    def setUrlHandler(self, scheme, method):
        '''static void QDesktopServices.setUrlHandler(str scheme, callable method)'''
    def openUrl(self, url):
        '''static bool QDesktopServices.openUrl(QUrl url)'''
        return bool()


class QDrag(QObject):
    """"""
    def __init__(self, dragSource):
        '''void QDrag.__init__(QObject dragSource)'''
    def defaultAction(self):
        '''Qt.DropAction QDrag.defaultAction()'''
        return Qt.DropAction()
    def supportedActions(self):
        '''Qt.DropActions QDrag.supportedActions()'''
        return Qt.DropActions()
    def dragCursor(self, action):
        '''QPixmap QDrag.dragCursor(Qt.DropAction action)'''
        return QPixmap()
    targetChanged = pyqtSignal() # void targetChanged(QObject*) - signal
    actionChanged = pyqtSignal() # void actionChanged(Qt::DropAction) - signal
    def setDragCursor(self, cursor, action):
        '''void QDrag.setDragCursor(QPixmap cursor, Qt.DropAction action)'''
    def target(self):
        '''QObject QDrag.target()'''
        return QObject()
    def source(self):
        '''QObject QDrag.source()'''
        return QObject()
    def hotSpot(self):
        '''QPoint QDrag.hotSpot()'''
        return QPoint()
    def setHotSpot(self, hotspot):
        '''void QDrag.setHotSpot(QPoint hotspot)'''
    def pixmap(self):
        '''QPixmap QDrag.pixmap()'''
        return QPixmap()
    def setPixmap(self):
        '''QPixmap QDrag.setPixmap()'''
        return QPixmap()
    def mimeData(self):
        '''QMimeData QDrag.mimeData()'''
        return QMimeData()
    def setMimeData(self, data):
        '''void QDrag.setMimeData(QMimeData data)'''
    def exec_(self, supportedActions = None):
        '''Qt.DropAction QDrag.exec_(Qt.DropActions supportedActions = Qt.MoveAction)'''
        return Qt.DropAction()
    def exec_(self, supportedActions, defaultDropAction):
        '''Qt.DropAction QDrag.exec_(Qt.DropActions supportedActions, Qt.DropAction defaultDropAction)'''
        return Qt.DropAction()


class QInputEvent(QEvent):
    """"""
    def setTimestamp(self, atimestamp):
        '''void QInputEvent.setTimestamp(int atimestamp)'''
    def timestamp(self):
        '''int QInputEvent.timestamp()'''
        return int()
    def modifiers(self):
        '''Qt.KeyboardModifiers QInputEvent.modifiers()'''
        return Qt.KeyboardModifiers()


class QMouseEvent(QInputEvent):
    """"""
    def __init__(self, type, pos, button, buttons, modifiers):
        '''void QMouseEvent.__init__(QEvent.Type type, QPointF pos, Qt.MouseButton button, Qt.MouseButtons buttons, Qt.KeyboardModifiers modifiers)'''
    def __init__(self, type, pos, globalPos, button, buttons, modifiers):
        '''void QMouseEvent.__init__(QEvent.Type type, QPointF pos, QPointF globalPos, Qt.MouseButton button, Qt.MouseButtons buttons, Qt.KeyboardModifiers modifiers)'''
    def __init__(self, type, pos, windowPos, globalPos, button, buttons, modifiers):
        '''void QMouseEvent.__init__(QEvent.Type type, QPointF pos, QPointF windowPos, QPointF globalPos, Qt.MouseButton button, Qt.MouseButtons buttons, Qt.KeyboardModifiers modifiers)'''
    def __init__(self):
        '''QMouseEvent QMouseEvent.__init__()'''
        return QMouseEvent()
    def flags(self):
        '''Qt.MouseEventFlags QMouseEvent.flags()'''
        return Qt.MouseEventFlags()
    def source(self):
        '''Qt.MouseEventSource QMouseEvent.source()'''
        return Qt.MouseEventSource()
    def screenPos(self):
        '''QPointF QMouseEvent.screenPos()'''
        return QPointF()
    def windowPos(self):
        '''QPointF QMouseEvent.windowPos()'''
        return QPointF()
    def localPos(self):
        '''QPointF QMouseEvent.localPos()'''
        return QPointF()
    def buttons(self):
        '''Qt.MouseButtons QMouseEvent.buttons()'''
        return Qt.MouseButtons()
    def button(self):
        '''Qt.MouseButton QMouseEvent.button()'''
        return Qt.MouseButton()
    def globalY(self):
        '''int QMouseEvent.globalY()'''
        return int()
    def globalX(self):
        '''int QMouseEvent.globalX()'''
        return int()
    def y(self):
        '''int QMouseEvent.y()'''
        return int()
    def x(self):
        '''int QMouseEvent.x()'''
        return int()
    def globalPos(self):
        '''QPoint QMouseEvent.globalPos()'''
        return QPoint()
    def pos(self):
        '''QPoint QMouseEvent.pos()'''
        return QPoint()


class QHoverEvent(QInputEvent):
    """"""
    def __init__(self, type, pos, oldPos, modifiers = None):
        '''void QHoverEvent.__init__(QEvent.Type type, QPointF pos, QPointF oldPos, Qt.KeyboardModifiers modifiers = Qt.NoModifier)'''
    def __init__(self):
        '''QHoverEvent QHoverEvent.__init__()'''
        return QHoverEvent()
    def oldPosF(self):
        '''QPointF QHoverEvent.oldPosF()'''
        return QPointF()
    def posF(self):
        '''QPointF QHoverEvent.posF()'''
        return QPointF()
    def oldPos(self):
        '''QPoint QHoverEvent.oldPos()'''
        return QPoint()
    def pos(self):
        '''QPoint QHoverEvent.pos()'''
        return QPoint()


class QWheelEvent(QInputEvent):
    """"""
    def __init__(self, pos, globalPos, pixelDelta, angleDelta, qt4Delta, qt4Orientation, buttons, modifiers):
        '''void QWheelEvent.__init__(QPointF pos, QPointF globalPos, QPoint pixelDelta, QPoint angleDelta, int qt4Delta, Qt.Orientation qt4Orientation, Qt.MouseButtons buttons, Qt.KeyboardModifiers modifiers)'''
    def __init__(self, pos, globalPos, pixelDelta, angleDelta, qt4Delta, qt4Orientation, buttons, modifiers, phase):
        '''void QWheelEvent.__init__(QPointF pos, QPointF globalPos, QPoint pixelDelta, QPoint angleDelta, int qt4Delta, Qt.Orientation qt4Orientation, Qt.MouseButtons buttons, Qt.KeyboardModifiers modifiers, Qt.ScrollPhase phase)'''
    def __init__(self, pos, globalPos, pixelDelta, angleDelta, qt4Delta, qt4Orientation, buttons, modifiers, phase, source):
        '''void QWheelEvent.__init__(QPointF pos, QPointF globalPos, QPoint pixelDelta, QPoint angleDelta, int qt4Delta, Qt.Orientation qt4Orientation, Qt.MouseButtons buttons, Qt.KeyboardModifiers modifiers, Qt.ScrollPhase phase, Qt.MouseEventSource source)'''
    def __init__(self):
        '''QWheelEvent QWheelEvent.__init__()'''
        return QWheelEvent()
    def source(self):
        '''Qt.MouseEventSource QWheelEvent.source()'''
        return Qt.MouseEventSource()
    def phase(self):
        '''Qt.ScrollPhase QWheelEvent.phase()'''
        return Qt.ScrollPhase()
    def globalPosF(self):
        '''QPointF QWheelEvent.globalPosF()'''
        return QPointF()
    def posF(self):
        '''QPointF QWheelEvent.posF()'''
        return QPointF()
    def angleDelta(self):
        '''QPoint QWheelEvent.angleDelta()'''
        return QPoint()
    def pixelDelta(self):
        '''QPoint QWheelEvent.pixelDelta()'''
        return QPoint()
    def buttons(self):
        '''Qt.MouseButtons QWheelEvent.buttons()'''
        return Qt.MouseButtons()
    def globalY(self):
        '''int QWheelEvent.globalY()'''
        return int()
    def globalX(self):
        '''int QWheelEvent.globalX()'''
        return int()
    def y(self):
        '''int QWheelEvent.y()'''
        return int()
    def x(self):
        '''int QWheelEvent.x()'''
        return int()
    def globalPos(self):
        '''QPoint QWheelEvent.globalPos()'''
        return QPoint()
    def pos(self):
        '''QPoint QWheelEvent.pos()'''
        return QPoint()


class QTabletEvent(QInputEvent):
    """"""
    # Enum QTabletEvent.PointerType
    UnknownPointer = 0
    Pen = 0
    Cursor = 0
    Eraser = 0

    # Enum QTabletEvent.TabletDevice
    NoDevice = 0
    Puck = 0
    Stylus = 0
    Airbrush = 0
    FourDMouse = 0
    XFreeEraser = 0
    RotationStylus = 0

    def __init__(self, t, pos, globalPos, device, pointerType, pressure, xTilt, yTilt, tangentialPressure, rotation, z, keyState, uniqueID, button, buttons):
        '''void QTabletEvent.__init__(QEvent.Type t, QPointF pos, QPointF globalPos, int device, int pointerType, float pressure, int xTilt, int yTilt, float tangentialPressure, float rotation, int z, Qt.KeyboardModifiers keyState, int uniqueID, Qt.MouseButton button, Qt.MouseButtons buttons)'''
    def __init__(self, t, pos, globalPos, device, pointerType, pressure, xTilt, yTilt, tangentialPressure, rotation, z, keyState, uniqueID):
        '''void QTabletEvent.__init__(QEvent.Type t, QPointF pos, QPointF globalPos, int device, int pointerType, float pressure, int xTilt, int yTilt, float tangentialPressure, float rotation, int z, Qt.KeyboardModifiers keyState, int uniqueID)'''
    def __init__(self):
        '''QTabletEvent QTabletEvent.__init__()'''
        return QTabletEvent()
    def buttons(self):
        '''Qt.MouseButtons QTabletEvent.buttons()'''
        return Qt.MouseButtons()
    def button(self):
        '''Qt.MouseButton QTabletEvent.button()'''
        return Qt.MouseButton()
    def globalPosF(self):
        '''QPointF QTabletEvent.globalPosF()'''
        return QPointF()
    def posF(self):
        '''QPointF QTabletEvent.posF()'''
        return QPointF()
    def yTilt(self):
        '''int QTabletEvent.yTilt()'''
        return int()
    def xTilt(self):
        '''int QTabletEvent.xTilt()'''
        return int()
    def rotation(self):
        '''float QTabletEvent.rotation()'''
        return float()
    def tangentialPressure(self):
        '''float QTabletEvent.tangentialPressure()'''
        return float()
    def z(self):
        '''int QTabletEvent.z()'''
        return int()
    def pressure(self):
        '''float QTabletEvent.pressure()'''
        return float()
    def uniqueId(self):
        '''int QTabletEvent.uniqueId()'''
        return int()
    def pointerType(self):
        '''QTabletEvent.PointerType QTabletEvent.pointerType()'''
        return QTabletEvent.PointerType()
    def device(self):
        '''QTabletEvent.TabletDevice QTabletEvent.device()'''
        return QTabletEvent.TabletDevice()
    def hiResGlobalY(self):
        '''float QTabletEvent.hiResGlobalY()'''
        return float()
    def hiResGlobalX(self):
        '''float QTabletEvent.hiResGlobalX()'''
        return float()
    def globalY(self):
        '''int QTabletEvent.globalY()'''
        return int()
    def globalX(self):
        '''int QTabletEvent.globalX()'''
        return int()
    def y(self):
        '''int QTabletEvent.y()'''
        return int()
    def x(self):
        '''int QTabletEvent.x()'''
        return int()
    def globalPos(self):
        '''QPoint QTabletEvent.globalPos()'''
        return QPoint()
    def pos(self):
        '''QPoint QTabletEvent.pos()'''
        return QPoint()


class QKeyEvent(QInputEvent):
    """"""
    def __init__(self, type, key, modifiers, nativeScanCode, nativeVirtualKey, nativeModifiers, text = str(), autorep = False, count = 1):
        '''void QKeyEvent.__init__(QEvent.Type type, int key, Qt.KeyboardModifiers modifiers, int nativeScanCode, int nativeVirtualKey, int nativeModifiers, str text = str(), bool autorep = False, int count = 1)'''
    def __init__(self, type, key, modifiers, text = None, autorep = False, count = 1):
        '''void QKeyEvent.__init__(QEvent.Type type, int key, Qt.KeyboardModifiers modifiers, str text = '', bool autorep = False, int count = 1)'''
    def __init__(self):
        '''QKeyEvent QKeyEvent.__init__()'''
        return QKeyEvent()
    def __ne__(self, key):
        '''bool QKeyEvent.__ne__(QKeySequence.StandardKey key)'''
        return bool()
    def __eq__(self, key):
        '''bool QKeyEvent.__eq__(QKeySequence.StandardKey key)'''
        return bool()
    def nativeVirtualKey(self):
        '''int QKeyEvent.nativeVirtualKey()'''
        return int()
    def nativeScanCode(self):
        '''int QKeyEvent.nativeScanCode()'''
        return int()
    def nativeModifiers(self):
        '''int QKeyEvent.nativeModifiers()'''
        return int()
    def matches(self, key):
        '''bool QKeyEvent.matches(QKeySequence.StandardKey key)'''
        return bool()
    def __len__(self):
        ''' QKeyEvent.__len__()'''
        return ()
    def count(self):
        '''int QKeyEvent.count()'''
        return int()
    def isAutoRepeat(self):
        '''bool QKeyEvent.isAutoRepeat()'''
        return bool()
    def text(self):
        '''str QKeyEvent.text()'''
        return str()
    def modifiers(self):
        '''Qt.KeyboardModifiers QKeyEvent.modifiers()'''
        return Qt.KeyboardModifiers()
    def key(self):
        '''int QKeyEvent.key()'''
        return int()


class QFocusEvent(QEvent):
    """"""
    def __init__(self, type, reason = None):
        '''void QFocusEvent.__init__(QEvent.Type type, Qt.FocusReason reason = Qt.OtherFocusReason)'''
    def __init__(self):
        '''QFocusEvent QFocusEvent.__init__()'''
        return QFocusEvent()
    def reason(self):
        '''Qt.FocusReason QFocusEvent.reason()'''
        return Qt.FocusReason()
    def lostFocus(self):
        '''bool QFocusEvent.lostFocus()'''
        return bool()
    def gotFocus(self):
        '''bool QFocusEvent.gotFocus()'''
        return bool()


class QPaintEvent(QEvent):
    """"""
    def __init__(self, paintRegion):
        '''void QPaintEvent.__init__(QRegion paintRegion)'''
    def __init__(self, paintRect):
        '''void QPaintEvent.__init__(QRect paintRect)'''
    def __init__(self):
        '''QPaintEvent QPaintEvent.__init__()'''
        return QPaintEvent()
    def region(self):
        '''QRegion QPaintEvent.region()'''
        return QRegion()
    def rect(self):
        '''QRect QPaintEvent.rect()'''
        return QRect()


class QMoveEvent(QEvent):
    """"""
    def __init__(self, pos, oldPos):
        '''void QMoveEvent.__init__(QPoint pos, QPoint oldPos)'''
    def __init__(self):
        '''QMoveEvent QMoveEvent.__init__()'''
        return QMoveEvent()
    def oldPos(self):
        '''QPoint QMoveEvent.oldPos()'''
        return QPoint()
    def pos(self):
        '''QPoint QMoveEvent.pos()'''
        return QPoint()


class QResizeEvent(QEvent):
    """"""
    def __init__(self, size, oldSize):
        '''void QResizeEvent.__init__(QSize size, QSize oldSize)'''
    def __init__(self):
        '''QResizeEvent QResizeEvent.__init__()'''
        return QResizeEvent()
    def oldSize(self):
        '''QSize QResizeEvent.oldSize()'''
        return QSize()
    def size(self):
        '''QSize QResizeEvent.size()'''
        return QSize()


class QCloseEvent(QEvent):
    """"""
    def __init__(self):
        '''void QCloseEvent.__init__()'''
    def __init__(self):
        '''QCloseEvent QCloseEvent.__init__()'''
        return QCloseEvent()


class QIconDragEvent(QEvent):
    """"""
    def __init__(self):
        '''void QIconDragEvent.__init__()'''
    def __init__(self):
        '''QIconDragEvent QIconDragEvent.__init__()'''
        return QIconDragEvent()


class QShowEvent(QEvent):
    """"""
    def __init__(self):
        '''void QShowEvent.__init__()'''
    def __init__(self):
        '''QShowEvent QShowEvent.__init__()'''
        return QShowEvent()


class QHideEvent(QEvent):
    """"""
    def __init__(self):
        '''void QHideEvent.__init__()'''
    def __init__(self):
        '''QHideEvent QHideEvent.__init__()'''
        return QHideEvent()


class QContextMenuEvent(QInputEvent):
    """"""
    # Enum QContextMenuEvent.Reason
    Mouse = 0
    Keyboard = 0
    Other = 0

    def __init__(self, reason, pos, globalPos, modifiers):
        '''void QContextMenuEvent.__init__(QContextMenuEvent.Reason reason, QPoint pos, QPoint globalPos, Qt.KeyboardModifiers modifiers)'''
    def __init__(self, reason, pos, globalPos):
        '''void QContextMenuEvent.__init__(QContextMenuEvent.Reason reason, QPoint pos, QPoint globalPos)'''
    def __init__(self, reason, pos):
        '''void QContextMenuEvent.__init__(QContextMenuEvent.Reason reason, QPoint pos)'''
    def __init__(self):
        '''QContextMenuEvent QContextMenuEvent.__init__()'''
        return QContextMenuEvent()
    def reason(self):
        '''QContextMenuEvent.Reason QContextMenuEvent.reason()'''
        return QContextMenuEvent.Reason()
    def globalPos(self):
        '''QPoint QContextMenuEvent.globalPos()'''
        return QPoint()
    def pos(self):
        '''QPoint QContextMenuEvent.pos()'''
        return QPoint()
    def globalY(self):
        '''int QContextMenuEvent.globalY()'''
        return int()
    def globalX(self):
        '''int QContextMenuEvent.globalX()'''
        return int()
    def y(self):
        '''int QContextMenuEvent.y()'''
        return int()
    def x(self):
        '''int QContextMenuEvent.x()'''
        return int()


class QInputMethodEvent(QEvent):
    """"""
    # Enum QInputMethodEvent.AttributeType
    TextFormat = 0
    Cursor = 0
    Language = 0
    Ruby = 0
    Selection = 0

    def __init__(self):
        '''void QInputMethodEvent.__init__()'''
    def __init__(self, preeditText, attributes):
        '''void QInputMethodEvent.__init__(str preeditText, list-of-QInputMethodEvent.Attribute attributes)'''
    def __init__(self, other):
        '''void QInputMethodEvent.__init__(QInputMethodEvent other)'''
    def replacementLength(self):
        '''int QInputMethodEvent.replacementLength()'''
        return int()
    def replacementStart(self):
        '''int QInputMethodEvent.replacementStart()'''
        return int()
    def commitString(self):
        '''str QInputMethodEvent.commitString()'''
        return str()
    def preeditString(self):
        '''str QInputMethodEvent.preeditString()'''
        return str()
    def attributes(self):
        '''list-of-QInputMethodEvent.Attribute QInputMethodEvent.attributes()'''
        return [QInputMethodEvent.Attribute()]
    def setCommitString(self, commitString, from_ = 0, length = 0):
        '''void QInputMethodEvent.setCommitString(str commitString, int from = 0, int length = 0)'''
    class Attribute():
        """"""
        length = None # int - member
        start = None # int - member
        type = None # QInputMethodEvent.AttributeType - member
        value = None # QVariant - member
        def __init__(self, t, s, l, val):
            '''void QInputMethodEvent.Attribute.__init__(QInputMethodEvent.AttributeType t, int s, int l, QVariant val)'''
        def __init__(self):
            '''QInputMethodEvent.Attribute QInputMethodEvent.Attribute.__init__()'''
            return QInputMethodEvent.Attribute()


class QInputMethodQueryEvent(QEvent):
    """"""
    def __init__(self, queries):
        '''void QInputMethodQueryEvent.__init__(Qt.InputMethodQueries queries)'''
    def __init__(self):
        '''QInputMethodQueryEvent QInputMethodQueryEvent.__init__()'''
        return QInputMethodQueryEvent()
    def value(self, query):
        '''QVariant QInputMethodQueryEvent.value(Qt.InputMethodQuery query)'''
        return QVariant()
    def setValue(self, query, value):
        '''void QInputMethodQueryEvent.setValue(Qt.InputMethodQuery query, QVariant value)'''
    def queries(self):
        '''Qt.InputMethodQueries QInputMethodQueryEvent.queries()'''
        return Qt.InputMethodQueries()


class QDropEvent(QEvent):
    """"""
    def __init__(self, pos, actions, data, buttons, modifiers, type = None):
        '''void QDropEvent.__init__(QPointF pos, Qt.DropActions actions, QMimeData data, Qt.MouseButtons buttons, Qt.KeyboardModifiers modifiers, QEvent.Type type = QEvent.Drop)'''
    def __init__(self):
        '''QDropEvent QDropEvent.__init__()'''
        return QDropEvent()
    def mimeData(self):
        '''QMimeData QDropEvent.mimeData()'''
        return QMimeData()
    def source(self):
        '''QObject QDropEvent.source()'''
        return QObject()
    def setDropAction(self, action):
        '''void QDropEvent.setDropAction(Qt.DropAction action)'''
    def dropAction(self):
        '''Qt.DropAction QDropEvent.dropAction()'''
        return Qt.DropAction()
    def acceptProposedAction(self):
        '''void QDropEvent.acceptProposedAction()'''
    def proposedAction(self):
        '''Qt.DropAction QDropEvent.proposedAction()'''
        return Qt.DropAction()
    def possibleActions(self):
        '''Qt.DropActions QDropEvent.possibleActions()'''
        return Qt.DropActions()
    def keyboardModifiers(self):
        '''Qt.KeyboardModifiers QDropEvent.keyboardModifiers()'''
        return Qt.KeyboardModifiers()
    def mouseButtons(self):
        '''Qt.MouseButtons QDropEvent.mouseButtons()'''
        return Qt.MouseButtons()
    def posF(self):
        '''QPointF QDropEvent.posF()'''
        return QPointF()
    def pos(self):
        '''QPoint QDropEvent.pos()'''
        return QPoint()


class QDragMoveEvent(QDropEvent):
    """"""
    def __init__(self, pos, actions, data, buttons, modifiers, type = None):
        '''void QDragMoveEvent.__init__(QPoint pos, Qt.DropActions actions, QMimeData data, Qt.MouseButtons buttons, Qt.KeyboardModifiers modifiers, QEvent.Type type = QEvent.DragMove)'''
    def __init__(self):
        '''QDragMoveEvent QDragMoveEvent.__init__()'''
        return QDragMoveEvent()
    def ignore(self):
        '''void QDragMoveEvent.ignore()'''
    def ignore(self, r):
        '''void QDragMoveEvent.ignore(QRect r)'''
    def accept(self):
        '''void QDragMoveEvent.accept()'''
    def accept(self, r):
        '''void QDragMoveEvent.accept(QRect r)'''
    def answerRect(self):
        '''QRect QDragMoveEvent.answerRect()'''
        return QRect()


class QDragEnterEvent(QDragMoveEvent):
    """"""
    def __init__(self, pos, actions, data, buttons, modifiers):
        '''void QDragEnterEvent.__init__(QPoint pos, Qt.DropActions actions, QMimeData data, Qt.MouseButtons buttons, Qt.KeyboardModifiers modifiers)'''
    def __init__(self):
        '''QDragEnterEvent QDragEnterEvent.__init__()'''
        return QDragEnterEvent()


class QDragLeaveEvent(QEvent):
    """"""
    def __init__(self):
        '''void QDragLeaveEvent.__init__()'''
    def __init__(self):
        '''QDragLeaveEvent QDragLeaveEvent.__init__()'''
        return QDragLeaveEvent()


class QHelpEvent(QEvent):
    """"""
    def __init__(self, type, pos, globalPos):
        '''void QHelpEvent.__init__(QEvent.Type type, QPoint pos, QPoint globalPos)'''
    def __init__(self):
        '''QHelpEvent QHelpEvent.__init__()'''
        return QHelpEvent()
    def globalPos(self):
        '''QPoint QHelpEvent.globalPos()'''
        return QPoint()
    def pos(self):
        '''QPoint QHelpEvent.pos()'''
        return QPoint()
    def globalY(self):
        '''int QHelpEvent.globalY()'''
        return int()
    def globalX(self):
        '''int QHelpEvent.globalX()'''
        return int()
    def y(self):
        '''int QHelpEvent.y()'''
        return int()
    def x(self):
        '''int QHelpEvent.x()'''
        return int()


class QStatusTipEvent(QEvent):
    """"""
    def __init__(self, tip):
        '''void QStatusTipEvent.__init__(str tip)'''
    def __init__(self):
        '''QStatusTipEvent QStatusTipEvent.__init__()'''
        return QStatusTipEvent()
    def tip(self):
        '''str QStatusTipEvent.tip()'''
        return str()


class QWhatsThisClickedEvent(QEvent):
    """"""
    def __init__(self, href):
        '''void QWhatsThisClickedEvent.__init__(str href)'''
    def __init__(self):
        '''QWhatsThisClickedEvent QWhatsThisClickedEvent.__init__()'''
        return QWhatsThisClickedEvent()
    def href(self):
        '''str QWhatsThisClickedEvent.href()'''
        return str()


class QActionEvent(QEvent):
    """"""
    def __init__(self, type, action, before = None):
        '''void QActionEvent.__init__(int type, QAction action, QAction before = None)'''
    def __init__(self):
        '''QActionEvent QActionEvent.__init__()'''
        return QActionEvent()
    def before(self):
        '''QAction QActionEvent.before()'''
        return QAction()
    def action(self):
        '''QAction QActionEvent.action()'''
        return QAction()


class QFileOpenEvent(QEvent):
    """"""
    def openFile(self, file, flags):
        '''bool QFileOpenEvent.openFile(QFile file, QIODevice.OpenMode flags)'''
        return bool()
    def url(self):
        '''QUrl QFileOpenEvent.url()'''
        return QUrl()
    def file(self):
        '''str QFileOpenEvent.file()'''
        return str()


class QShortcutEvent(QEvent):
    """"""
    def __init__(self, key, id, ambiguous = False):
        '''void QShortcutEvent.__init__(QKeySequence key, int id, bool ambiguous = False)'''
    def __init__(self):
        '''QShortcutEvent QShortcutEvent.__init__()'''
        return QShortcutEvent()
    def shortcutId(self):
        '''int QShortcutEvent.shortcutId()'''
        return int()
    def key(self):
        '''QKeySequence QShortcutEvent.key()'''
        return QKeySequence()
    def isAmbiguous(self):
        '''bool QShortcutEvent.isAmbiguous()'''
        return bool()


class QWindowStateChangeEvent(QEvent):
    """"""
    def oldState(self):
        '''Qt.WindowStates QWindowStateChangeEvent.oldState()'''
        return Qt.WindowStates()


class QTouchEvent(QInputEvent):
    """"""
    def __init__(self, eventType, device = None, modifiers = None, touchPointStates = 0, touchPoints = None):
        '''void QTouchEvent.__init__(QEvent.Type eventType, QTouchDevice device = None, Qt.KeyboardModifiers modifiers = Qt.NoModifier, Qt.TouchPointStates touchPointStates = 0, list-of-QTouchEvent.TouchPoint touchPoints = QListlt;QTouchEvent.TouchPointgt;())'''
    def __init__(self):
        '''QTouchEvent QTouchEvent.__init__()'''
        return QTouchEvent()
    def setDevice(self, adevice):
        '''void QTouchEvent.setDevice(QTouchDevice adevice)'''
    def device(self):
        '''QTouchDevice QTouchEvent.device()'''
        return QTouchDevice()
    def window(self):
        '''QWindow QTouchEvent.window()'''
        return QWindow()
    def touchPoints(self):
        '''list-of-QTouchEvent.TouchPoint QTouchEvent.touchPoints()'''
        return [QTouchEvent.TouchPoint()]
    def touchPointStates(self):
        '''Qt.TouchPointStates QTouchEvent.touchPointStates()'''
        return Qt.TouchPointStates()
    def target(self):
        '''QObject QTouchEvent.target()'''
        return QObject()
    class TouchPoint():
        """"""
        # Enum QTouchEvent.TouchPoint.InfoFlag
        Pen = 0
    
        def rawScreenPositions(self):
            '''list-of-QPointF QTouchEvent.TouchPoint.rawScreenPositions()'''
            return [QPointF()]
        def flags(self):
            '''QTouchEvent.TouchPoint.InfoFlags QTouchEvent.TouchPoint.flags()'''
            return QTouchEvent.TouchPoint.InfoFlags()
        def velocity(self):
            '''QVector2D QTouchEvent.TouchPoint.velocity()'''
            return QVector2D()
        def pressure(self):
            '''float QTouchEvent.TouchPoint.pressure()'''
            return float()
        def screenRect(self):
            '''QRectF QTouchEvent.TouchPoint.screenRect()'''
            return QRectF()
        def sceneRect(self):
            '''QRectF QTouchEvent.TouchPoint.sceneRect()'''
            return QRectF()
        def rect(self):
            '''QRectF QTouchEvent.TouchPoint.rect()'''
            return QRectF()
        def lastNormalizedPos(self):
            '''QPointF QTouchEvent.TouchPoint.lastNormalizedPos()'''
            return QPointF()
        def startNormalizedPos(self):
            '''QPointF QTouchEvent.TouchPoint.startNormalizedPos()'''
            return QPointF()
        def normalizedPos(self):
            '''QPointF QTouchEvent.TouchPoint.normalizedPos()'''
            return QPointF()
        def lastScreenPos(self):
            '''QPointF QTouchEvent.TouchPoint.lastScreenPos()'''
            return QPointF()
        def startScreenPos(self):
            '''QPointF QTouchEvent.TouchPoint.startScreenPos()'''
            return QPointF()
        def screenPos(self):
            '''QPointF QTouchEvent.TouchPoint.screenPos()'''
            return QPointF()
        def lastScenePos(self):
            '''QPointF QTouchEvent.TouchPoint.lastScenePos()'''
            return QPointF()
        def startScenePos(self):
            '''QPointF QTouchEvent.TouchPoint.startScenePos()'''
            return QPointF()
        def scenePos(self):
            '''QPointF QTouchEvent.TouchPoint.scenePos()'''
            return QPointF()
        def lastPos(self):
            '''QPointF QTouchEvent.TouchPoint.lastPos()'''
            return QPointF()
        def startPos(self):
            '''QPointF QTouchEvent.TouchPoint.startPos()'''
            return QPointF()
        def pos(self):
            '''QPointF QTouchEvent.TouchPoint.pos()'''
            return QPointF()
        def state(self):
            '''Qt.TouchPointState QTouchEvent.TouchPoint.state()'''
            return Qt.TouchPointState()
        def id(self):
            '''int QTouchEvent.TouchPoint.id()'''
            return int()
    class TouchPoint():
        """"""
        class InfoFlags():
            """"""
            def __init__(self):
                '''QTouchEvent.TouchPoint.InfoFlags QTouchEvent.TouchPoint.InfoFlags.__init__()'''
                return QTouchEvent.TouchPoint.InfoFlags()
            def __init__(self):
                '''int QTouchEvent.TouchPoint.InfoFlags.__init__()'''
                return int()
            def __init__(self):
                '''void QTouchEvent.TouchPoint.InfoFlags.__init__()'''
            def __bool__(self):
                '''int QTouchEvent.TouchPoint.InfoFlags.__bool__()'''
                return int()
            def __ne__(self, f):
                '''bool QTouchEvent.TouchPoint.InfoFlags.__ne__(QTouchEvent.TouchPoint.InfoFlags f)'''
                return bool()
            def __eq__(self, f):
                '''bool QTouchEvent.TouchPoint.InfoFlags.__eq__(QTouchEvent.TouchPoint.InfoFlags f)'''
                return bool()
            def __invert__(self):
                '''QTouchEvent.TouchPoint.InfoFlags QTouchEvent.TouchPoint.InfoFlags.__invert__()'''
                return QTouchEvent.TouchPoint.InfoFlags()
            def __and__(self, mask):
                '''QTouchEvent.TouchPoint.InfoFlags QTouchEvent.TouchPoint.InfoFlags.__and__(int mask)'''
                return QTouchEvent.TouchPoint.InfoFlags()
            def __xor__(self, f):
                '''QTouchEvent.TouchPoint.InfoFlags QTouchEvent.TouchPoint.InfoFlags.__xor__(QTouchEvent.TouchPoint.InfoFlags f)'''
                return QTouchEvent.TouchPoint.InfoFlags()
            def __xor__(self, f):
                '''QTouchEvent.TouchPoint.InfoFlags QTouchEvent.TouchPoint.InfoFlags.__xor__(int f)'''
                return QTouchEvent.TouchPoint.InfoFlags()
            def __or__(self, f):
                '''QTouchEvent.TouchPoint.InfoFlags QTouchEvent.TouchPoint.InfoFlags.__or__(QTouchEvent.TouchPoint.InfoFlags f)'''
                return QTouchEvent.TouchPoint.InfoFlags()
            def __or__(self, f):
                '''QTouchEvent.TouchPoint.InfoFlags QTouchEvent.TouchPoint.InfoFlags.__or__(int f)'''
                return QTouchEvent.TouchPoint.InfoFlags()
            def __int__(self):
                '''int QTouchEvent.TouchPoint.InfoFlags.__int__()'''
                return int()
            def __ixor__(self, f):
                '''QTouchEvent.TouchPoint.InfoFlags QTouchEvent.TouchPoint.InfoFlags.__ixor__(QTouchEvent.TouchPoint.InfoFlags f)'''
                return QTouchEvent.TouchPoint.InfoFlags()
            def __ior__(self, f):
                '''QTouchEvent.TouchPoint.InfoFlags QTouchEvent.TouchPoint.InfoFlags.__ior__(QTouchEvent.TouchPoint.InfoFlags f)'''
                return QTouchEvent.TouchPoint.InfoFlags()
            def __iand__(self, mask):
                '''QTouchEvent.TouchPoint.InfoFlags QTouchEvent.TouchPoint.InfoFlags.__iand__(int mask)'''
                return QTouchEvent.TouchPoint.InfoFlags()


class QExposeEvent(QEvent):
    """"""
    def __init__(self, rgn):
        '''void QExposeEvent.__init__(QRegion rgn)'''
    def __init__(self):
        '''QExposeEvent QExposeEvent.__init__()'''
        return QExposeEvent()
    def region(self):
        '''QRegion QExposeEvent.region()'''
        return QRegion()


class QScrollPrepareEvent(QEvent):
    """"""
    def __init__(self, startPos):
        '''void QScrollPrepareEvent.__init__(QPointF startPos)'''
    def __init__(self):
        '''QScrollPrepareEvent QScrollPrepareEvent.__init__()'''
        return QScrollPrepareEvent()
    def setContentPos(self, pos):
        '''void QScrollPrepareEvent.setContentPos(QPointF pos)'''
    def setContentPosRange(self, rect):
        '''void QScrollPrepareEvent.setContentPosRange(QRectF rect)'''
    def setViewportSize(self, size):
        '''void QScrollPrepareEvent.setViewportSize(QSizeF size)'''
    def contentPos(self):
        '''QPointF QScrollPrepareEvent.contentPos()'''
        return QPointF()
    def contentPosRange(self):
        '''QRectF QScrollPrepareEvent.contentPosRange()'''
        return QRectF()
    def viewportSize(self):
        '''QSizeF QScrollPrepareEvent.viewportSize()'''
        return QSizeF()
    def startPos(self):
        '''QPointF QScrollPrepareEvent.startPos()'''
        return QPointF()


class QScrollEvent(QEvent):
    """"""
    # Enum QScrollEvent.ScrollState
    ScrollStarted = 0
    ScrollUpdated = 0
    ScrollFinished = 0

    def __init__(self, contentPos, overshoot, scrollState):
        '''void QScrollEvent.__init__(QPointF contentPos, QPointF overshoot, QScrollEvent.ScrollState scrollState)'''
    def __init__(self):
        '''QScrollEvent QScrollEvent.__init__()'''
        return QScrollEvent()
    def scrollState(self):
        '''QScrollEvent.ScrollState QScrollEvent.scrollState()'''
        return QScrollEvent.ScrollState()
    def overshootDistance(self):
        '''QPointF QScrollEvent.overshootDistance()'''
        return QPointF()
    def contentPos(self):
        '''QPointF QScrollEvent.contentPos()'''
        return QPointF()


class QEnterEvent(QEvent):
    """"""
    def __init__(self, localPos, windowPos, screenPos):
        '''void QEnterEvent.__init__(QPointF localPos, QPointF windowPos, QPointF screenPos)'''
    def __init__(self):
        '''QEnterEvent QEnterEvent.__init__()'''
        return QEnterEvent()
    def screenPos(self):
        '''QPointF QEnterEvent.screenPos()'''
        return QPointF()
    def windowPos(self):
        '''QPointF QEnterEvent.windowPos()'''
        return QPointF()
    def localPos(self):
        '''QPointF QEnterEvent.localPos()'''
        return QPointF()
    def globalY(self):
        '''int QEnterEvent.globalY()'''
        return int()
    def globalX(self):
        '''int QEnterEvent.globalX()'''
        return int()
    def y(self):
        '''int QEnterEvent.y()'''
        return int()
    def x(self):
        '''int QEnterEvent.x()'''
        return int()
    def globalPos(self):
        '''QPoint QEnterEvent.globalPos()'''
        return QPoint()
    def pos(self):
        '''QPoint QEnterEvent.pos()'''
        return QPoint()


class QNativeGestureEvent(QInputEvent):
    """"""
    def __init__(self, type, localPos, windowPos, screenPos, value, sequenceId, intArgument):
        '''void QNativeGestureEvent.__init__(Qt.NativeGestureType type, QPointF localPos, QPointF windowPos, QPointF screenPos, float value, int sequenceId, int intArgument)'''
    def __init__(self):
        '''QNativeGestureEvent QNativeGestureEvent.__init__()'''
        return QNativeGestureEvent()
    def screenPos(self):
        '''QPointF QNativeGestureEvent.screenPos()'''
        return QPointF()
    def windowPos(self):
        '''QPointF QNativeGestureEvent.windowPos()'''
        return QPointF()
    def localPos(self):
        '''QPointF QNativeGestureEvent.localPos()'''
        return QPointF()
    def globalPos(self):
        '''QPoint QNativeGestureEvent.globalPos()'''
        return QPoint()
    def pos(self):
        '''QPoint QNativeGestureEvent.pos()'''
        return QPoint()
    def value(self):
        '''float QNativeGestureEvent.value()'''
        return float()
    def gestureType(self):
        '''Qt.NativeGestureType QNativeGestureEvent.gestureType()'''
        return Qt.NativeGestureType()


class QPlatformSurfaceEvent(QEvent):
    """"""
    # Enum QPlatformSurfaceEvent.SurfaceEventType
    SurfaceCreated = 0
    SurfaceAboutToBeDestroyed = 0

    def __init__(self, surfaceEventType):
        '''void QPlatformSurfaceEvent.__init__(QPlatformSurfaceEvent.SurfaceEventType surfaceEventType)'''
    def __init__(self):
        '''QPlatformSurfaceEvent QPlatformSurfaceEvent.__init__()'''
        return QPlatformSurfaceEvent()
    def surfaceEventType(self):
        '''QPlatformSurfaceEvent.SurfaceEventType QPlatformSurfaceEvent.surfaceEventType()'''
        return QPlatformSurfaceEvent.SurfaceEventType()


class QFont():
    """"""
    # Enum QFont.HintingPreference
    PreferDefaultHinting = 0
    PreferNoHinting = 0
    PreferVerticalHinting = 0
    PreferFullHinting = 0

    # Enum QFont.SpacingType
    PercentageSpacing = 0
    AbsoluteSpacing = 0

    # Enum QFont.Capitalization
    MixedCase = 0
    AllUppercase = 0
    AllLowercase = 0
    SmallCaps = 0
    Capitalize = 0

    # Enum QFont.Stretch
    UltraCondensed = 0
    ExtraCondensed = 0
    Condensed = 0
    SemiCondensed = 0
    Unstretched = 0
    SemiExpanded = 0
    Expanded = 0
    ExtraExpanded = 0
    UltraExpanded = 0

    # Enum QFont.Style
    StyleNormal = 0
    StyleItalic = 0
    StyleOblique = 0

    # Enum QFont.Weight
    Thin = 0
    ExtraLight = 0
    Light = 0
    Normal = 0
    Medium = 0
    DemiBold = 0
    Bold = 0
    ExtraBold = 0
    Black = 0

    # Enum QFont.StyleStrategy
    PreferDefault = 0
    PreferBitmap = 0
    PreferDevice = 0
    PreferOutline = 0
    ForceOutline = 0
    PreferMatch = 0
    PreferQuality = 0
    PreferAntialias = 0
    NoAntialias = 0
    NoSubpixelAntialias = 0
    OpenGLCompatible = 0
    NoFontMerging = 0
    ForceIntegerMetrics = 0

    # Enum QFont.StyleHint
    Helvetica = 0
    SansSerif = 0
    Times = 0
    Serif = 0
    Courier = 0
    TypeWriter = 0
    OldEnglish = 0
    Decorative = 0
    System = 0
    AnyStyle = 0
    Cursive = 0
    Monospace = 0
    Fantasy = 0

    def __init__(self):
        '''void QFont.__init__()'''
    def __init__(self, family, pointSize = None, weight = None, italic = False):
        '''void QFont.__init__(str family, int pointSize = -1, int weight = -1, bool italic = False)'''
    def __init__(self, pd):
        '''QFont QFont.__init__(QPaintDevice pd)'''
        return QFont()
    def __init__(self):
        '''QFont QFont.__init__()'''
        return QFont()
    def __init__(self, variant):
        '''void QFont.__init__(QVariant variant)'''
    def __ge__(self):
        '''QFont QFont.__ge__()'''
        return QFont()
    def __hash__(self):
        '''int QFont.__hash__()'''
        return int()
    def swap(self, other):
        '''void QFont.swap(QFont other)'''
    def hintingPreference(self):
        '''QFont.HintingPreference QFont.hintingPreference()'''
        return QFont.HintingPreference()
    def setHintingPreference(self, hintingPreference):
        '''void QFont.setHintingPreference(QFont.HintingPreference hintingPreference)'''
    def setStyleName(self, styleName):
        '''void QFont.setStyleName(str styleName)'''
    def styleName(self):
        '''str QFont.styleName()'''
        return str()
    def capitalization(self):
        '''QFont.Capitalization QFont.capitalization()'''
        return QFont.Capitalization()
    def setCapitalization(self):
        '''QFont.Capitalization QFont.setCapitalization()'''
        return QFont.Capitalization()
    def setWordSpacing(self, spacing):
        '''void QFont.setWordSpacing(float spacing)'''
    def wordSpacing(self):
        '''float QFont.wordSpacing()'''
        return float()
    def setLetterSpacing(self, type, spacing):
        '''void QFont.setLetterSpacing(QFont.SpacingType type, float spacing)'''
    def letterSpacingType(self):
        '''QFont.SpacingType QFont.letterSpacingType()'''
        return QFont.SpacingType()
    def letterSpacing(self):
        '''float QFont.letterSpacing()'''
        return float()
    def setItalic(self, b):
        '''void QFont.setItalic(bool b)'''
    def italic(self):
        '''bool QFont.italic()'''
        return bool()
    def setBold(self, enable):
        '''void QFont.setBold(bool enable)'''
    def bold(self):
        '''bool QFont.bold()'''
        return bool()
    def resolve(self):
        '''QFont QFont.resolve()'''
        return QFont()
    def lastResortFont(self):
        '''str QFont.lastResortFont()'''
        return str()
    def lastResortFamily(self):
        '''str QFont.lastResortFamily()'''
        return str()
    def defaultFamily(self):
        '''str QFont.defaultFamily()'''
        return str()
    def cacheStatistics(self):
        '''static void QFont.cacheStatistics()'''
    def cleanup(self):
        '''static void QFont.cleanup()'''
    def initialize(self):
        '''static void QFont.initialize()'''
    def removeSubstitutions(self):
        '''static str QFont.removeSubstitutions()'''
        return str()
    def insertSubstitutions(self):
        '''static list-of-str QFont.insertSubstitutions()'''
        return [str()]
    def insertSubstitution(self):
        '''static str QFont.insertSubstitution()'''
        return str()
    def substitutions(self):
        '''static list-of-str QFont.substitutions()'''
        return [str()]
    def substitutes(self):
        '''static str QFont.substitutes()'''
        return str()
    def substitute(self):
        '''static str QFont.substitute()'''
        return str()
    def fromString(self):
        '''str QFont.fromString()'''
        return str()
    def toString(self):
        '''str QFont.toString()'''
        return str()
    def key(self):
        '''str QFont.key()'''
        return str()
    def rawName(self):
        '''str QFont.rawName()'''
        return str()
    def setRawName(self):
        '''str QFont.setRawName()'''
        return str()
    def isCopyOf(self):
        '''QFont QFont.isCopyOf()'''
        return QFont()
    def __lt__(self):
        '''QFont QFont.__lt__()'''
        return QFont()
    def __ne__(self):
        '''QFont QFont.__ne__()'''
        return QFont()
    def __eq__(self):
        '''QFont QFont.__eq__()'''
        return QFont()
    def exactMatch(self):
        '''bool QFont.exactMatch()'''
        return bool()
    def setRawMode(self):
        '''bool QFont.setRawMode()'''
        return bool()
    def rawMode(self):
        '''bool QFont.rawMode()'''
        return bool()
    def setStretch(self):
        '''int QFont.setStretch()'''
        return int()
    def stretch(self):
        '''int QFont.stretch()'''
        return int()
    def setStyleStrategy(self, s):
        '''void QFont.setStyleStrategy(QFont.StyleStrategy s)'''
    def setStyleHint(self, hint, strategy = None):
        '''void QFont.setStyleHint(QFont.StyleHint hint, QFont.StyleStrategy strategy = QFont.PreferDefault)'''
    def styleStrategy(self):
        '''QFont.StyleStrategy QFont.styleStrategy()'''
        return QFont.StyleStrategy()
    def styleHint(self):
        '''QFont.StyleHint QFont.styleHint()'''
        return QFont.StyleHint()
    def setKerning(self):
        '''bool QFont.setKerning()'''
        return bool()
    def kerning(self):
        '''bool QFont.kerning()'''
        return bool()
    def setFixedPitch(self):
        '''bool QFont.setFixedPitch()'''
        return bool()
    def fixedPitch(self):
        '''bool QFont.fixedPitch()'''
        return bool()
    def setStrikeOut(self):
        '''bool QFont.setStrikeOut()'''
        return bool()
    def strikeOut(self):
        '''bool QFont.strikeOut()'''
        return bool()
    def setOverline(self):
        '''bool QFont.setOverline()'''
        return bool()
    def overline(self):
        '''bool QFont.overline()'''
        return bool()
    def setUnderline(self):
        '''bool QFont.setUnderline()'''
        return bool()
    def underline(self):
        '''bool QFont.underline()'''
        return bool()
    def style(self):
        '''QFont.Style QFont.style()'''
        return QFont.Style()
    def setStyle(self, style):
        '''void QFont.setStyle(QFont.Style style)'''
    def setWeight(self):
        '''int QFont.setWeight()'''
        return int()
    def weight(self):
        '''int QFont.weight()'''
        return int()
    def setPixelSize(self):
        '''int QFont.setPixelSize()'''
        return int()
    def pixelSize(self):
        '''int QFont.pixelSize()'''
        return int()
    def setPointSizeF(self):
        '''float QFont.setPointSizeF()'''
        return float()
    def pointSizeF(self):
        '''float QFont.pointSizeF()'''
        return float()
    def setPointSize(self):
        '''int QFont.setPointSize()'''
        return int()
    def pointSize(self):
        '''int QFont.pointSize()'''
        return int()
    def setFamily(self):
        '''str QFont.setFamily()'''
        return str()
    def family(self):
        '''str QFont.family()'''
        return str()


class QFontDatabase():
    """"""
    # Enum QFontDatabase.SystemFont
    GeneralFont = 0
    FixedFont = 0
    TitleFont = 0
    SmallestReadableFont = 0

    # Enum QFontDatabase.WritingSystem
    Any = 0
    Latin = 0
    Greek = 0
    Cyrillic = 0
    Armenian = 0
    Hebrew = 0
    Arabic = 0
    Syriac = 0
    Thaana = 0
    Devanagari = 0
    Bengali = 0
    Gurmukhi = 0
    Gujarati = 0
    Oriya = 0
    Tamil = 0
    Telugu = 0
    Kannada = 0
    Malayalam = 0
    Sinhala = 0
    Thai = 0
    Lao = 0
    Tibetan = 0
    Myanmar = 0
    Georgian = 0
    Khmer = 0
    SimplifiedChinese = 0
    TraditionalChinese = 0
    Japanese = 0
    Korean = 0
    Vietnamese = 0
    Other = 0
    Symbol = 0
    Ogham = 0
    Runic = 0
    Nko = 0

    def __init__(self):
        '''void QFontDatabase.__init__()'''
    def __init__(self):
        '''QFontDatabase QFontDatabase.__init__()'''
        return QFontDatabase()
    def isPrivateFamily(self, family):
        '''bool QFontDatabase.isPrivateFamily(str family)'''
        return bool()
    def systemFont(self, type):
        '''static QFont QFontDatabase.systemFont(QFontDatabase.SystemFont type)'''
        return QFont()
    def supportsThreadedFontRendering(self):
        '''static bool QFontDatabase.supportsThreadedFontRendering()'''
        return bool()
    def removeAllApplicationFonts(self):
        '''static bool QFontDatabase.removeAllApplicationFonts()'''
        return bool()
    def removeApplicationFont(self, id):
        '''static bool QFontDatabase.removeApplicationFont(int id)'''
        return bool()
    def applicationFontFamilies(self, id):
        '''static list-of-str QFontDatabase.applicationFontFamilies(int id)'''
        return [str()]
    def addApplicationFontFromData(self, fontData):
        '''static int QFontDatabase.addApplicationFontFromData(QByteArray fontData)'''
        return int()
    def addApplicationFont(self, fileName):
        '''static int QFontDatabase.addApplicationFont(str fileName)'''
        return int()
    def writingSystemSample(self, writingSystem):
        '''static str QFontDatabase.writingSystemSample(QFontDatabase.WritingSystem writingSystem)'''
        return str()
    def writingSystemName(self, writingSystem):
        '''static str QFontDatabase.writingSystemName(QFontDatabase.WritingSystem writingSystem)'''
        return str()
    def weight(self, family, style):
        '''int QFontDatabase.weight(str family, str style)'''
        return int()
    def bold(self, family, style):
        '''bool QFontDatabase.bold(str family, str style)'''
        return bool()
    def italic(self, family, style):
        '''bool QFontDatabase.italic(str family, str style)'''
        return bool()
    def isFixedPitch(self, family, style = None):
        '''bool QFontDatabase.isFixedPitch(str family, str style = '')'''
        return bool()
    def isScalable(self, family, style = None):
        '''bool QFontDatabase.isScalable(str family, str style = '')'''
        return bool()
    def isSmoothlyScalable(self, family, style = None):
        '''bool QFontDatabase.isSmoothlyScalable(str family, str style = '')'''
        return bool()
    def isBitmapScalable(self, family, style = None):
        '''bool QFontDatabase.isBitmapScalable(str family, str style = '')'''
        return bool()
    def font(self, family, style, pointSize):
        '''QFont QFontDatabase.font(str family, str style, int pointSize)'''
        return QFont()
    def styleString(self, font):
        '''str QFontDatabase.styleString(QFont font)'''
        return str()
    def styleString(self, fontInfo):
        '''str QFontDatabase.styleString(QFontInfo fontInfo)'''
        return str()
    def smoothSizes(self, family, style):
        '''list-of-int QFontDatabase.smoothSizes(str family, str style)'''
        return [int()]
    def pointSizes(self, family, style = None):
        '''list-of-int QFontDatabase.pointSizes(str family, str style = '')'''
        return [int()]
    def styles(self, family):
        '''list-of-str QFontDatabase.styles(str family)'''
        return [str()]
    def families(self, writingSystem = None):
        '''list-of-str QFontDatabase.families(QFontDatabase.WritingSystem writingSystem = QFontDatabase.Any)'''
        return [str()]
    def writingSystems(self):
        '''list-of-QFontDatabase.WritingSystem QFontDatabase.writingSystems()'''
        return [QFontDatabase.WritingSystem()]
    def writingSystems(self, family):
        '''list-of-QFontDatabase.WritingSystem QFontDatabase.writingSystems(str family)'''
        return [QFontDatabase.WritingSystem()]
    def standardSizes(self):
        '''static list-of-int QFontDatabase.standardSizes()'''
        return [int()]


class QFontInfo():
    """"""
    def __init__(self):
        '''QFont QFontInfo.__init__()'''
        return QFont()
    def __init__(self):
        '''QFontInfo QFontInfo.__init__()'''
        return QFontInfo()
    def swap(self, other):
        '''void QFontInfo.swap(QFontInfo other)'''
    def styleName(self):
        '''str QFontInfo.styleName()'''
        return str()
    def exactMatch(self):
        '''bool QFontInfo.exactMatch()'''
        return bool()
    def rawMode(self):
        '''bool QFontInfo.rawMode()'''
        return bool()
    def styleHint(self):
        '''QFont.StyleHint QFontInfo.styleHint()'''
        return QFont.StyleHint()
    def fixedPitch(self):
        '''bool QFontInfo.fixedPitch()'''
        return bool()
    def bold(self):
        '''bool QFontInfo.bold()'''
        return bool()
    def weight(self):
        '''int QFontInfo.weight()'''
        return int()
    def style(self):
        '''QFont.Style QFontInfo.style()'''
        return QFont.Style()
    def italic(self):
        '''bool QFontInfo.italic()'''
        return bool()
    def pointSizeF(self):
        '''float QFontInfo.pointSizeF()'''
        return float()
    def pointSize(self):
        '''int QFontInfo.pointSize()'''
        return int()
    def pixelSize(self):
        '''int QFontInfo.pixelSize()'''
        return int()
    def family(self):
        '''str QFontInfo.family()'''
        return str()


class QFontMetrics():
    """"""
    def __init__(self):
        '''QFont QFontMetrics.__init__()'''
        return QFont()
    def __init__(self, pd):
        '''QFont QFontMetrics.__init__(QPaintDevice pd)'''
        return QFont()
    def __init__(self):
        '''QFontMetrics QFontMetrics.__init__()'''
        return QFontMetrics()
    def swap(self, other):
        '''void QFontMetrics.swap(QFontMetrics other)'''
    def inFontUcs4(self, character):
        '''bool QFontMetrics.inFontUcs4(int character)'''
        return bool()
    def tightBoundingRect(self, text):
        '''QRect QFontMetrics.tightBoundingRect(str text)'''
        return QRect()
    def __ne__(self, other):
        '''bool QFontMetrics.__ne__(QFontMetrics other)'''
        return bool()
    def __eq__(self, other):
        '''bool QFontMetrics.__eq__(QFontMetrics other)'''
        return bool()
    def elidedText(self, text, mode, width, flags = 0):
        '''str QFontMetrics.elidedText(str text, Qt.TextElideMode mode, int width, int flags = 0)'''
        return str()
    def averageCharWidth(self):
        '''int QFontMetrics.averageCharWidth()'''
        return int()
    def lineWidth(self):
        '''int QFontMetrics.lineWidth()'''
        return int()
    def strikeOutPos(self):
        '''int QFontMetrics.strikeOutPos()'''
        return int()
    def overlinePos(self):
        '''int QFontMetrics.overlinePos()'''
        return int()
    def underlinePos(self):
        '''int QFontMetrics.underlinePos()'''
        return int()
    def size(self, flags, text, tabStops = 0, tabArray = 0):
        '''QSize QFontMetrics.size(int flags, str text, int tabStops = 0, list-of-int tabArray = 0)'''
        return QSize()
    def boundingRect(self, text):
        '''QRect QFontMetrics.boundingRect(str text)'''
        return QRect()
    def boundingRect(self, rect, flags, text, tabStops = 0, tabArray = 0):
        '''QRect QFontMetrics.boundingRect(QRect rect, int flags, str text, int tabStops = 0, list-of-int tabArray = 0)'''
        return QRect()
    def boundingRect(self, x, y, width, height, flags, text, tabStops = 0, tabArray = 0):
        '''QRect QFontMetrics.boundingRect(int x, int y, int width, int height, int flags, str text, int tabStops = 0, list-of-int tabArray = 0)'''
        return QRect()
    def boundingRectChar(self):
        '''str QFontMetrics.boundingRectChar()'''
        return str()
    def width(self, text, length = None):
        '''int QFontMetrics.width(str text, int length = -1)'''
        return int()
    def widthChar(self):
        '''str QFontMetrics.widthChar()'''
        return str()
    def rightBearing(self):
        '''str QFontMetrics.rightBearing()'''
        return str()
    def leftBearing(self):
        '''str QFontMetrics.leftBearing()'''
        return str()
    def inFont(self):
        '''str QFontMetrics.inFont()'''
        return str()
    def xHeight(self):
        '''int QFontMetrics.xHeight()'''
        return int()
    def maxWidth(self):
        '''int QFontMetrics.maxWidth()'''
        return int()
    def minRightBearing(self):
        '''int QFontMetrics.minRightBearing()'''
        return int()
    def minLeftBearing(self):
        '''int QFontMetrics.minLeftBearing()'''
        return int()
    def lineSpacing(self):
        '''int QFontMetrics.lineSpacing()'''
        return int()
    def leading(self):
        '''int QFontMetrics.leading()'''
        return int()
    def height(self):
        '''int QFontMetrics.height()'''
        return int()
    def descent(self):
        '''int QFontMetrics.descent()'''
        return int()
    def ascent(self):
        '''int QFontMetrics.ascent()'''
        return int()


class QFontMetricsF():
    """"""
    def __init__(self):
        '''QFont QFontMetricsF.__init__()'''
        return QFont()
    def __init__(self, pd):
        '''QFont QFontMetricsF.__init__(QPaintDevice pd)'''
        return QFont()
    def __init__(self):
        '''QFontMetrics QFontMetricsF.__init__()'''
        return QFontMetrics()
    def __init__(self):
        '''QFontMetricsF QFontMetricsF.__init__()'''
        return QFontMetricsF()
    def swap(self, other):
        '''void QFontMetricsF.swap(QFontMetricsF other)'''
    def inFontUcs4(self, character):
        '''bool QFontMetricsF.inFontUcs4(int character)'''
        return bool()
    def tightBoundingRect(self, text):
        '''QRectF QFontMetricsF.tightBoundingRect(str text)'''
        return QRectF()
    def __ne__(self, other):
        '''bool QFontMetricsF.__ne__(QFontMetricsF other)'''
        return bool()
    def __eq__(self, other):
        '''bool QFontMetricsF.__eq__(QFontMetricsF other)'''
        return bool()
    def elidedText(self, text, mode, width, flags = 0):
        '''str QFontMetricsF.elidedText(str text, Qt.TextElideMode mode, float width, int flags = 0)'''
        return str()
    def averageCharWidth(self):
        '''float QFontMetricsF.averageCharWidth()'''
        return float()
    def lineWidth(self):
        '''float QFontMetricsF.lineWidth()'''
        return float()
    def strikeOutPos(self):
        '''float QFontMetricsF.strikeOutPos()'''
        return float()
    def overlinePos(self):
        '''float QFontMetricsF.overlinePos()'''
        return float()
    def underlinePos(self):
        '''float QFontMetricsF.underlinePos()'''
        return float()
    def size(self, flags, text, tabStops = 0, tabArray = 0):
        '''QSizeF QFontMetricsF.size(int flags, str text, int tabStops = 0, list-of-int tabArray = 0)'''
        return QSizeF()
    def boundingRect(self, string):
        '''QRectF QFontMetricsF.boundingRect(str string)'''
        return QRectF()
    def boundingRect(self, rect, flags, text, tabStops = 0, tabArray = 0):
        '''QRectF QFontMetricsF.boundingRect(QRectF rect, int flags, str text, int tabStops = 0, list-of-int tabArray = 0)'''
        return QRectF()
    def boundingRectChar(self):
        '''str QFontMetricsF.boundingRectChar()'''
        return str()
    def width(self, string):
        '''float QFontMetricsF.width(str string)'''
        return float()
    def widthChar(self):
        '''str QFontMetricsF.widthChar()'''
        return str()
    def rightBearing(self):
        '''str QFontMetricsF.rightBearing()'''
        return str()
    def leftBearing(self):
        '''str QFontMetricsF.leftBearing()'''
        return str()
    def inFont(self):
        '''str QFontMetricsF.inFont()'''
        return str()
    def xHeight(self):
        '''float QFontMetricsF.xHeight()'''
        return float()
    def maxWidth(self):
        '''float QFontMetricsF.maxWidth()'''
        return float()
    def minRightBearing(self):
        '''float QFontMetricsF.minRightBearing()'''
        return float()
    def minLeftBearing(self):
        '''float QFontMetricsF.minLeftBearing()'''
        return float()
    def lineSpacing(self):
        '''float QFontMetricsF.lineSpacing()'''
        return float()
    def leading(self):
        '''float QFontMetricsF.leading()'''
        return float()
    def height(self):
        '''float QFontMetricsF.height()'''
        return float()
    def descent(self):
        '''float QFontMetricsF.descent()'''
        return float()
    def ascent(self):
        '''float QFontMetricsF.ascent()'''
        return float()


class QMatrix4x3():
    """"""
    def __init__(self):
        '''void QMatrix4x3.__init__()'''
    def __init__(self, other):
        '''void QMatrix4x3.__init__(QMatrix4x3 other)'''
    def __init__(self, values):
        '''void QMatrix4x3.__init__(sequence-of-float values)'''
    def __ne__(self):
        '''QMatrix4x3 QMatrix4x3.__ne__()'''
        return QMatrix4x3()
    def __eq__(self):
        '''QMatrix4x3 QMatrix4x3.__eq__()'''
        return QMatrix4x3()
    def __idiv__(self):
        '''float QMatrix4x3.__idiv__()'''
        return float()
    def __imul__(self):
        '''float QMatrix4x3.__imul__()'''
        return float()
    def __isub__(self):
        '''QMatrix4x3 QMatrix4x3.__isub__()'''
        return QMatrix4x3()
    def __iadd__(self):
        '''QMatrix4x3 QMatrix4x3.__iadd__()'''
        return QMatrix4x3()
    def transposed(self):
        '''QMatrix3x4 QMatrix4x3.transposed()'''
        return QMatrix3x4()
    def fill(self, value):
        '''void QMatrix4x3.fill(float value)'''
    def setToIdentity(self):
        '''void QMatrix4x3.setToIdentity()'''
    def isIdentity(self):
        '''bool QMatrix4x3.isIdentity()'''
        return bool()
    def __setitem__(self):
        '''float QMatrix4x3.__setitem__()'''
        return float()
    def __getitem__(self):
        '''object QMatrix4x3.__getitem__()'''
        return object()
    def copyDataTo(self):
        '''list-of-float QMatrix4x3.copyDataTo()'''
        return [float()]
    def data(self):
        '''list-of-float QMatrix4x3.data()'''
        return [float()]
    def __repr__(self):
        '''str QMatrix4x3.__repr__()'''
        return str()


class QMatrix4x2():
    """"""
    def __init__(self):
        '''void QMatrix4x2.__init__()'''
    def __init__(self, other):
        '''void QMatrix4x2.__init__(QMatrix4x2 other)'''
    def __init__(self, values):
        '''void QMatrix4x2.__init__(sequence-of-float values)'''
    def __ne__(self):
        '''QMatrix4x2 QMatrix4x2.__ne__()'''
        return QMatrix4x2()
    def __eq__(self):
        '''QMatrix4x2 QMatrix4x2.__eq__()'''
        return QMatrix4x2()
    def __idiv__(self):
        '''float QMatrix4x2.__idiv__()'''
        return float()
    def __imul__(self):
        '''float QMatrix4x2.__imul__()'''
        return float()
    def __isub__(self):
        '''QMatrix4x2 QMatrix4x2.__isub__()'''
        return QMatrix4x2()
    def __iadd__(self):
        '''QMatrix4x2 QMatrix4x2.__iadd__()'''
        return QMatrix4x2()
    def transposed(self):
        '''QMatrix2x4 QMatrix4x2.transposed()'''
        return QMatrix2x4()
    def fill(self, value):
        '''void QMatrix4x2.fill(float value)'''
    def setToIdentity(self):
        '''void QMatrix4x2.setToIdentity()'''
    def isIdentity(self):
        '''bool QMatrix4x2.isIdentity()'''
        return bool()
    def __setitem__(self):
        '''float QMatrix4x2.__setitem__()'''
        return float()
    def __getitem__(self):
        '''object QMatrix4x2.__getitem__()'''
        return object()
    def copyDataTo(self):
        '''list-of-float QMatrix4x2.copyDataTo()'''
        return [float()]
    def data(self):
        '''list-of-float QMatrix4x2.data()'''
        return [float()]
    def __repr__(self):
        '''str QMatrix4x2.__repr__()'''
        return str()


class QMatrix3x4():
    """"""
    def __init__(self):
        '''void QMatrix3x4.__init__()'''
    def __init__(self, other):
        '''void QMatrix3x4.__init__(QMatrix3x4 other)'''
    def __init__(self, values):
        '''void QMatrix3x4.__init__(sequence-of-float values)'''
    def __ne__(self):
        '''QMatrix3x4 QMatrix3x4.__ne__()'''
        return QMatrix3x4()
    def __eq__(self):
        '''QMatrix3x4 QMatrix3x4.__eq__()'''
        return QMatrix3x4()
    def __idiv__(self):
        '''float QMatrix3x4.__idiv__()'''
        return float()
    def __imul__(self):
        '''float QMatrix3x4.__imul__()'''
        return float()
    def __isub__(self):
        '''QMatrix3x4 QMatrix3x4.__isub__()'''
        return QMatrix3x4()
    def __iadd__(self):
        '''QMatrix3x4 QMatrix3x4.__iadd__()'''
        return QMatrix3x4()
    def transposed(self):
        '''QMatrix4x3 QMatrix3x4.transposed()'''
        return QMatrix4x3()
    def fill(self, value):
        '''void QMatrix3x4.fill(float value)'''
    def setToIdentity(self):
        '''void QMatrix3x4.setToIdentity()'''
    def isIdentity(self):
        '''bool QMatrix3x4.isIdentity()'''
        return bool()
    def __setitem__(self):
        '''float QMatrix3x4.__setitem__()'''
        return float()
    def __getitem__(self):
        '''object QMatrix3x4.__getitem__()'''
        return object()
    def copyDataTo(self):
        '''list-of-float QMatrix3x4.copyDataTo()'''
        return [float()]
    def data(self):
        '''list-of-float QMatrix3x4.data()'''
        return [float()]
    def __repr__(self):
        '''str QMatrix3x4.__repr__()'''
        return str()


class QMatrix3x3():
    """"""
    def __init__(self):
        '''void QMatrix3x3.__init__()'''
    def __init__(self, other):
        '''void QMatrix3x3.__init__(QMatrix3x3 other)'''
    def __init__(self, values):
        '''void QMatrix3x3.__init__(sequence-of-float values)'''
    def __ne__(self):
        '''QMatrix3x3 QMatrix3x3.__ne__()'''
        return QMatrix3x3()
    def __eq__(self):
        '''QMatrix3x3 QMatrix3x3.__eq__()'''
        return QMatrix3x3()
    def __idiv__(self):
        '''float QMatrix3x3.__idiv__()'''
        return float()
    def __imul__(self):
        '''float QMatrix3x3.__imul__()'''
        return float()
    def __isub__(self):
        '''QMatrix3x3 QMatrix3x3.__isub__()'''
        return QMatrix3x3()
    def __iadd__(self):
        '''QMatrix3x3 QMatrix3x3.__iadd__()'''
        return QMatrix3x3()
    def transposed(self):
        '''QMatrix3x3 QMatrix3x3.transposed()'''
        return QMatrix3x3()
    def fill(self, value):
        '''void QMatrix3x3.fill(float value)'''
    def setToIdentity(self):
        '''void QMatrix3x3.setToIdentity()'''
    def isIdentity(self):
        '''bool QMatrix3x3.isIdentity()'''
        return bool()
    def __setitem__(self):
        '''float QMatrix3x3.__setitem__()'''
        return float()
    def __getitem__(self):
        '''object QMatrix3x3.__getitem__()'''
        return object()
    def copyDataTo(self):
        '''list-of-float QMatrix3x3.copyDataTo()'''
        return [float()]
    def data(self):
        '''list-of-float QMatrix3x3.data()'''
        return [float()]
    def __repr__(self):
        '''str QMatrix3x3.__repr__()'''
        return str()


class QMatrix3x2():
    """"""
    def __init__(self):
        '''void QMatrix3x2.__init__()'''
    def __init__(self, other):
        '''void QMatrix3x2.__init__(QMatrix3x2 other)'''
    def __init__(self, values):
        '''void QMatrix3x2.__init__(sequence-of-float values)'''
    def __ne__(self):
        '''QMatrix3x2 QMatrix3x2.__ne__()'''
        return QMatrix3x2()
    def __eq__(self):
        '''QMatrix3x2 QMatrix3x2.__eq__()'''
        return QMatrix3x2()
    def __idiv__(self):
        '''float QMatrix3x2.__idiv__()'''
        return float()
    def __imul__(self):
        '''float QMatrix3x2.__imul__()'''
        return float()
    def __isub__(self):
        '''QMatrix3x2 QMatrix3x2.__isub__()'''
        return QMatrix3x2()
    def __iadd__(self):
        '''QMatrix3x2 QMatrix3x2.__iadd__()'''
        return QMatrix3x2()
    def transposed(self):
        '''QMatrix2x3 QMatrix3x2.transposed()'''
        return QMatrix2x3()
    def fill(self, value):
        '''void QMatrix3x2.fill(float value)'''
    def setToIdentity(self):
        '''void QMatrix3x2.setToIdentity()'''
    def isIdentity(self):
        '''bool QMatrix3x2.isIdentity()'''
        return bool()
    def __setitem__(self):
        '''float QMatrix3x2.__setitem__()'''
        return float()
    def __getitem__(self):
        '''object QMatrix3x2.__getitem__()'''
        return object()
    def copyDataTo(self):
        '''list-of-float QMatrix3x2.copyDataTo()'''
        return [float()]
    def data(self):
        '''list-of-float QMatrix3x2.data()'''
        return [float()]
    def __repr__(self):
        '''str QMatrix3x2.__repr__()'''
        return str()


class QMatrix2x4():
    """"""
    def __init__(self):
        '''void QMatrix2x4.__init__()'''
    def __init__(self, other):
        '''void QMatrix2x4.__init__(QMatrix2x4 other)'''
    def __init__(self, values):
        '''void QMatrix2x4.__init__(sequence-of-float values)'''
    def __ne__(self):
        '''QMatrix2x4 QMatrix2x4.__ne__()'''
        return QMatrix2x4()
    def __eq__(self):
        '''QMatrix2x4 QMatrix2x4.__eq__()'''
        return QMatrix2x4()
    def __idiv__(self):
        '''float QMatrix2x4.__idiv__()'''
        return float()
    def __imul__(self):
        '''float QMatrix2x4.__imul__()'''
        return float()
    def __isub__(self):
        '''QMatrix2x4 QMatrix2x4.__isub__()'''
        return QMatrix2x4()
    def __iadd__(self):
        '''QMatrix2x4 QMatrix2x4.__iadd__()'''
        return QMatrix2x4()
    def transposed(self):
        '''QMatrix4x2 QMatrix2x4.transposed()'''
        return QMatrix4x2()
    def fill(self, value):
        '''void QMatrix2x4.fill(float value)'''
    def setToIdentity(self):
        '''void QMatrix2x4.setToIdentity()'''
    def isIdentity(self):
        '''bool QMatrix2x4.isIdentity()'''
        return bool()
    def __setitem__(self):
        '''float QMatrix2x4.__setitem__()'''
        return float()
    def __getitem__(self):
        '''object QMatrix2x4.__getitem__()'''
        return object()
    def copyDataTo(self):
        '''list-of-float QMatrix2x4.copyDataTo()'''
        return [float()]
    def data(self):
        '''list-of-float QMatrix2x4.data()'''
        return [float()]
    def __repr__(self):
        '''str QMatrix2x4.__repr__()'''
        return str()


class QMatrix2x3():
    """"""
    def __init__(self):
        '''void QMatrix2x3.__init__()'''
    def __init__(self, other):
        '''void QMatrix2x3.__init__(QMatrix2x3 other)'''
    def __init__(self, values):
        '''void QMatrix2x3.__init__(sequence-of-float values)'''
    def __ne__(self):
        '''QMatrix2x3 QMatrix2x3.__ne__()'''
        return QMatrix2x3()
    def __eq__(self):
        '''QMatrix2x3 QMatrix2x3.__eq__()'''
        return QMatrix2x3()
    def __idiv__(self):
        '''float QMatrix2x3.__idiv__()'''
        return float()
    def __imul__(self):
        '''float QMatrix2x3.__imul__()'''
        return float()
    def __isub__(self):
        '''QMatrix2x3 QMatrix2x3.__isub__()'''
        return QMatrix2x3()
    def __iadd__(self):
        '''QMatrix2x3 QMatrix2x3.__iadd__()'''
        return QMatrix2x3()
    def transposed(self):
        '''QMatrix3x2 QMatrix2x3.transposed()'''
        return QMatrix3x2()
    def fill(self, value):
        '''void QMatrix2x3.fill(float value)'''
    def setToIdentity(self):
        '''void QMatrix2x3.setToIdentity()'''
    def isIdentity(self):
        '''bool QMatrix2x3.isIdentity()'''
        return bool()
    def __setitem__(self):
        '''float QMatrix2x3.__setitem__()'''
        return float()
    def __getitem__(self):
        '''object QMatrix2x3.__getitem__()'''
        return object()
    def copyDataTo(self):
        '''list-of-float QMatrix2x3.copyDataTo()'''
        return [float()]
    def data(self):
        '''list-of-float QMatrix2x3.data()'''
        return [float()]
    def __repr__(self):
        '''str QMatrix2x3.__repr__()'''
        return str()


class QMatrix2x2():
    """"""
    def __init__(self):
        '''void QMatrix2x2.__init__()'''
    def __init__(self, other):
        '''void QMatrix2x2.__init__(QMatrix2x2 other)'''
    def __init__(self, values):
        '''void QMatrix2x2.__init__(sequence-of-float values)'''
    def __ne__(self):
        '''QMatrix2x2 QMatrix2x2.__ne__()'''
        return QMatrix2x2()
    def __eq__(self):
        '''QMatrix2x2 QMatrix2x2.__eq__()'''
        return QMatrix2x2()
    def __idiv__(self):
        '''float QMatrix2x2.__idiv__()'''
        return float()
    def __imul__(self):
        '''float QMatrix2x2.__imul__()'''
        return float()
    def __isub__(self):
        '''QMatrix2x2 QMatrix2x2.__isub__()'''
        return QMatrix2x2()
    def __iadd__(self):
        '''QMatrix2x2 QMatrix2x2.__iadd__()'''
        return QMatrix2x2()
    def transposed(self):
        '''QMatrix2x2 QMatrix2x2.transposed()'''
        return QMatrix2x2()
    def fill(self, value):
        '''void QMatrix2x2.fill(float value)'''
    def setToIdentity(self):
        '''void QMatrix2x2.setToIdentity()'''
    def isIdentity(self):
        '''bool QMatrix2x2.isIdentity()'''
        return bool()
    def __setitem__(self):
        '''float QMatrix2x2.__setitem__()'''
        return float()
    def __getitem__(self):
        '''object QMatrix2x2.__getitem__()'''
        return object()
    def copyDataTo(self):
        '''list-of-float QMatrix2x2.copyDataTo()'''
        return [float()]
    def data(self):
        '''list-of-float QMatrix2x2.data()'''
        return [float()]
    def __repr__(self):
        '''str QMatrix2x2.__repr__()'''
        return str()


class QGlyphRun():
    """"""
    # Enum QGlyphRun.GlyphRunFlag
    Overline = 0
    Underline = 0
    StrikeOut = 0
    RightToLeft = 0
    SplitLigature = 0

    def __init__(self):
        '''void QGlyphRun.__init__()'''
    def __init__(self, other):
        '''void QGlyphRun.__init__(QGlyphRun other)'''
    def swap(self, other):
        '''void QGlyphRun.swap(QGlyphRun other)'''
    def isEmpty(self):
        '''bool QGlyphRun.isEmpty()'''
        return bool()
    def boundingRect(self):
        '''QRectF QGlyphRun.boundingRect()'''
        return QRectF()
    def setBoundingRect(self, boundingRect):
        '''void QGlyphRun.setBoundingRect(QRectF boundingRect)'''
    def flags(self):
        '''QGlyphRun.GlyphRunFlags QGlyphRun.flags()'''
        return QGlyphRun.GlyphRunFlags()
    def setFlags(self, flags):
        '''void QGlyphRun.setFlags(QGlyphRun.GlyphRunFlags flags)'''
    def setFlag(self, flag, enabled = True):
        '''void QGlyphRun.setFlag(QGlyphRun.GlyphRunFlag flag, bool enabled = True)'''
    def isRightToLeft(self):
        '''bool QGlyphRun.isRightToLeft()'''
        return bool()
    def setRightToLeft(self, on):
        '''void QGlyphRun.setRightToLeft(bool on)'''
    def strikeOut(self):
        '''bool QGlyphRun.strikeOut()'''
        return bool()
    def setStrikeOut(self, strikeOut):
        '''void QGlyphRun.setStrikeOut(bool strikeOut)'''
    def underline(self):
        '''bool QGlyphRun.underline()'''
        return bool()
    def setUnderline(self, underline):
        '''void QGlyphRun.setUnderline(bool underline)'''
    def overline(self):
        '''bool QGlyphRun.overline()'''
        return bool()
    def setOverline(self, overline):
        '''void QGlyphRun.setOverline(bool overline)'''
    def __ne__(self, other):
        '''bool QGlyphRun.__ne__(QGlyphRun other)'''
        return bool()
    def __eq__(self, other):
        '''bool QGlyphRun.__eq__(QGlyphRun other)'''
        return bool()
    def clear(self):
        '''void QGlyphRun.clear()'''
    def setPositions(self, positions):
        '''void QGlyphRun.setPositions(list-of-QPointF positions)'''
    def positions(self):
        '''list-of-QPointF QGlyphRun.positions()'''
        return [QPointF()]
    def setGlyphIndexes(self, glyphIndexes):
        '''void QGlyphRun.setGlyphIndexes(list-of-int glyphIndexes)'''
    def glyphIndexes(self):
        '''list-of-int QGlyphRun.glyphIndexes()'''
        return [int()]
    def setRawFont(self, rawFont):
        '''void QGlyphRun.setRawFont(QRawFont rawFont)'''
    def rawFont(self):
        '''QRawFont QGlyphRun.rawFont()'''
        return QRawFont()
    class GlyphRunFlags():
        """"""
        def __init__(self):
            '''QGlyphRun.GlyphRunFlags QGlyphRun.GlyphRunFlags.__init__()'''
            return QGlyphRun.GlyphRunFlags()
        def __init__(self):
            '''int QGlyphRun.GlyphRunFlags.__init__()'''
            return int()
        def __init__(self):
            '''void QGlyphRun.GlyphRunFlags.__init__()'''
        def __bool__(self):
            '''int QGlyphRun.GlyphRunFlags.__bool__()'''
            return int()
        def __ne__(self, f):
            '''bool QGlyphRun.GlyphRunFlags.__ne__(QGlyphRun.GlyphRunFlags f)'''
            return bool()
        def __eq__(self, f):
            '''bool QGlyphRun.GlyphRunFlags.__eq__(QGlyphRun.GlyphRunFlags f)'''
            return bool()
        def __invert__(self):
            '''QGlyphRun.GlyphRunFlags QGlyphRun.GlyphRunFlags.__invert__()'''
            return QGlyphRun.GlyphRunFlags()
        def __and__(self, mask):
            '''QGlyphRun.GlyphRunFlags QGlyphRun.GlyphRunFlags.__and__(int mask)'''
            return QGlyphRun.GlyphRunFlags()
        def __xor__(self, f):
            '''QGlyphRun.GlyphRunFlags QGlyphRun.GlyphRunFlags.__xor__(QGlyphRun.GlyphRunFlags f)'''
            return QGlyphRun.GlyphRunFlags()
        def __xor__(self, f):
            '''QGlyphRun.GlyphRunFlags QGlyphRun.GlyphRunFlags.__xor__(int f)'''
            return QGlyphRun.GlyphRunFlags()
        def __or__(self, f):
            '''QGlyphRun.GlyphRunFlags QGlyphRun.GlyphRunFlags.__or__(QGlyphRun.GlyphRunFlags f)'''
            return QGlyphRun.GlyphRunFlags()
        def __or__(self, f):
            '''QGlyphRun.GlyphRunFlags QGlyphRun.GlyphRunFlags.__or__(int f)'''
            return QGlyphRun.GlyphRunFlags()
        def __int__(self):
            '''int QGlyphRun.GlyphRunFlags.__int__()'''
            return int()
        def __ixor__(self, f):
            '''QGlyphRun.GlyphRunFlags QGlyphRun.GlyphRunFlags.__ixor__(QGlyphRun.GlyphRunFlags f)'''
            return QGlyphRun.GlyphRunFlags()
        def __ior__(self, f):
            '''QGlyphRun.GlyphRunFlags QGlyphRun.GlyphRunFlags.__ior__(QGlyphRun.GlyphRunFlags f)'''
            return QGlyphRun.GlyphRunFlags()
        def __iand__(self, mask):
            '''QGlyphRun.GlyphRunFlags QGlyphRun.GlyphRunFlags.__iand__(int mask)'''
            return QGlyphRun.GlyphRunFlags()


class QGuiApplication(QCoreApplication):
    """"""
    def __init__(self, argv):
        '''void QGuiApplication.__init__(list-of-str argv)'''
    paletteChanged = pyqtSignal() # void paletteChanged(const QPaletteamp;) - signal
    layoutDirectionChanged = pyqtSignal() # void layoutDirectionChanged(Qt::LayoutDirection) - signal
    screenRemoved = pyqtSignal() # void screenRemoved(QScreen*) - signal
    def event(self):
        '''QEvent QGuiApplication.event()'''
        return QEvent()
    def windowIcon(self):
        '''static QIcon QGuiApplication.windowIcon()'''
        return QIcon()
    def setWindowIcon(self, icon):
        '''static void QGuiApplication.setWindowIcon(QIcon icon)'''
    def sync(self):
        '''static void QGuiApplication.sync()'''
    def applicationState(self):
        '''static Qt.ApplicationState QGuiApplication.applicationState()'''
        return Qt.ApplicationState()
    def isSavingSession(self):
        '''bool QGuiApplication.isSavingSession()'''
        return bool()
    def sessionKey(self):
        '''str QGuiApplication.sessionKey()'''
        return str()
    def sessionId(self):
        '''str QGuiApplication.sessionId()'''
        return str()
    def isSessionRestored(self):
        '''bool QGuiApplication.isSessionRestored()'''
        return bool()
    def devicePixelRatio(self):
        '''float QGuiApplication.devicePixelRatio()'''
        return float()
    def modalWindow(self):
        '''static QWindow QGuiApplication.modalWindow()'''
        return QWindow()
    def applicationDisplayName(self):
        '''static str QGuiApplication.applicationDisplayName()'''
        return str()
    def setApplicationDisplayName(self, name):
        '''static void QGuiApplication.setApplicationDisplayName(str name)'''
    applicationStateChanged = pyqtSignal() # void applicationStateChanged(Qt::ApplicationState) - signal
    focusWindowChanged = pyqtSignal() # void focusWindowChanged(QWindow*) - signal
    saveStateRequest = pyqtSignal() # void saveStateRequest(QSessionManageramp;) - signal
    commitDataRequest = pyqtSignal() # void commitDataRequest(QSessionManageramp;) - signal
    focusObjectChanged = pyqtSignal() # void focusObjectChanged(QObject*) - signal
    lastWindowClosed = pyqtSignal() # void lastWindowClosed() - signal
    screenAdded = pyqtSignal() # void screenAdded(QScreen*) - signal
    fontDatabaseChanged = pyqtSignal() # void fontDatabaseChanged() - signal
    def notify(self):
        '''QEvent QGuiApplication.notify()'''
        return QEvent()
    def exec_(self):
        '''static int QGuiApplication.exec_()'''
        return int()
    def quitOnLastWindowClosed(self):
        '''static bool QGuiApplication.quitOnLastWindowClosed()'''
        return bool()
    def setQuitOnLastWindowClosed(self, quit):
        '''static void QGuiApplication.setQuitOnLastWindowClosed(bool quit)'''
    def desktopSettingsAware(self):
        '''static bool QGuiApplication.desktopSettingsAware()'''
        return bool()
    def setDesktopSettingsAware(self, on):
        '''static void QGuiApplication.setDesktopSettingsAware(bool on)'''
    def isLeftToRight(self):
        '''static bool QGuiApplication.isLeftToRight()'''
        return bool()
    def isRightToLeft(self):
        '''static bool QGuiApplication.isRightToLeft()'''
        return bool()
    def layoutDirection(self):
        '''static Qt.LayoutDirection QGuiApplication.layoutDirection()'''
        return Qt.LayoutDirection()
    def setLayoutDirection(self, direction):
        '''static void QGuiApplication.setLayoutDirection(Qt.LayoutDirection direction)'''
    def mouseButtons(self):
        '''static Qt.MouseButtons QGuiApplication.mouseButtons()'''
        return Qt.MouseButtons()
    def queryKeyboardModifiers(self):
        '''static Qt.KeyboardModifiers QGuiApplication.queryKeyboardModifiers()'''
        return Qt.KeyboardModifiers()
    def keyboardModifiers(self):
        '''static Qt.KeyboardModifiers QGuiApplication.keyboardModifiers()'''
        return Qt.KeyboardModifiers()
    def setPalette(self, pal):
        '''static void QGuiApplication.setPalette(QPalette pal)'''
    def palette(self):
        '''static QPalette QGuiApplication.palette()'''
        return QPalette()
    def clipboard(self):
        '''static QClipboard QGuiApplication.clipboard()'''
        return QClipboard()
    def setFont(self):
        '''static QFont QGuiApplication.setFont()'''
        return QFont()
    def font(self):
        '''static QFont QGuiApplication.font()'''
        return QFont()
    def restoreOverrideCursor(self):
        '''static void QGuiApplication.restoreOverrideCursor()'''
    def changeOverrideCursor(self):
        '''static QCursor QGuiApplication.changeOverrideCursor()'''
        return QCursor()
    def setOverrideCursor(self):
        '''static QCursor QGuiApplication.setOverrideCursor()'''
        return QCursor()
    def overrideCursor(self):
        '''static QCursor QGuiApplication.overrideCursor()'''
        return QCursor()
    def screens(self):
        '''static list-of-QScreen QGuiApplication.screens()'''
        return [QScreen()]
    def primaryScreen(self):
        '''static QScreen QGuiApplication.primaryScreen()'''
        return QScreen()
    def focusObject(self):
        '''static QObject QGuiApplication.focusObject()'''
        return QObject()
    def focusWindow(self):
        '''static QWindow QGuiApplication.focusWindow()'''
        return QWindow()
    def platformName(self):
        '''static str QGuiApplication.platformName()'''
        return str()
    def topLevelAt(self, pos):
        '''static QWindow QGuiApplication.topLevelAt(QPoint pos)'''
        return QWindow()
    def topLevelWindows(self):
        '''static list-of-QWindow QGuiApplication.topLevelWindows()'''
        return [QWindow()]
    def allWindows(self):
        '''static list-of-QWindow QGuiApplication.allWindows()'''
        return [QWindow()]


class QIcon():
    """"""
    # Enum QIcon.State
    On = 0
    Off = 0

    # Enum QIcon.Mode
    Normal = 0
    Disabled = 0
    Active = 0
    Selected = 0

    def __init__(self):
        '''void QIcon.__init__()'''
    def __init__(self, pixmap):
        '''void QIcon.__init__(QPixmap pixmap)'''
    def __init__(self, other):
        '''void QIcon.__init__(QIcon other)'''
    def __init__(self, fileName):
        '''void QIcon.__init__(str fileName)'''
    def __init__(self, engine):
        '''void QIcon.__init__(QIconEngine engine)'''
    def __init__(self, variant):
        '''void QIcon.__init__(QVariant variant)'''
    def swap(self, other):
        '''void QIcon.swap(QIcon other)'''
    def name(self):
        '''str QIcon.name()'''
        return str()
    def setThemeName(self, path):
        '''static void QIcon.setThemeName(str path)'''
    def themeName(self):
        '''static str QIcon.themeName()'''
        return str()
    def setThemeSearchPaths(self, searchpath):
        '''static void QIcon.setThemeSearchPaths(list-of-str searchpath)'''
    def themeSearchPaths(self):
        '''static list-of-str QIcon.themeSearchPaths()'''
        return [str()]
    def hasThemeIcon(self, name):
        '''static bool QIcon.hasThemeIcon(str name)'''
        return bool()
    def fromTheme(self, name, fallback = QIcon()):
        '''static QIcon QIcon.fromTheme(str name, QIcon fallback = QIcon())'''
        return QIcon()
    def cacheKey(self):
        '''int QIcon.cacheKey()'''
        return int()
    def addFile(self, fileName, size = QSize(), mode = None, state = None):
        '''void QIcon.addFile(str fileName, QSize size = QSize(), QIcon.Mode mode = QIcon.Normal, QIcon.State state = QIcon.Off)'''
    def addPixmap(self, pixmap, mode = None, state = None):
        '''void QIcon.addPixmap(QPixmap pixmap, QIcon.Mode mode = QIcon.Normal, QIcon.State state = QIcon.Off)'''
    def isDetached(self):
        '''bool QIcon.isDetached()'''
        return bool()
    def isNull(self):
        '''bool QIcon.isNull()'''
        return bool()
    def paint(self, painter, rect, alignment = None, mode = None, state = None):
        '''void QIcon.paint(QPainter painter, QRect rect, Qt.Alignment alignment = Qt.AlignCenter, QIcon.Mode mode = QIcon.Normal, QIcon.State state = QIcon.Off)'''
    def paint(self, painter, x, y, w, h, alignment = None, mode = None, state = None):
        '''void QIcon.paint(QPainter painter, int x, int y, int w, int h, Qt.Alignment alignment = Qt.AlignCenter, QIcon.Mode mode = QIcon.Normal, QIcon.State state = QIcon.Off)'''
    def availableSizes(self, mode = None, state = None):
        '''list-of-QSize QIcon.availableSizes(QIcon.Mode mode = QIcon.Normal, QIcon.State state = QIcon.Off)'''
        return [QSize()]
    def actualSize(self, size, mode = None, state = None):
        '''QSize QIcon.actualSize(QSize size, QIcon.Mode mode = QIcon.Normal, QIcon.State state = QIcon.Off)'''
        return QSize()
    def actualSize(self, window, size, mode = None, state = None):
        '''QSize QIcon.actualSize(QWindow window, QSize size, QIcon.Mode mode = QIcon.Normal, QIcon.State state = QIcon.Off)'''
        return QSize()
    def pixmap(self, size, mode = None, state = None):
        '''QPixmap QIcon.pixmap(QSize size, QIcon.Mode mode = QIcon.Normal, QIcon.State state = QIcon.Off)'''
        return QPixmap()
    def pixmap(self, w, h, mode = None, state = None):
        '''QPixmap QIcon.pixmap(int w, int h, QIcon.Mode mode = QIcon.Normal, QIcon.State state = QIcon.Off)'''
        return QPixmap()
    def pixmap(self, extent, mode = None, state = None):
        '''QPixmap QIcon.pixmap(int extent, QIcon.Mode mode = QIcon.Normal, QIcon.State state = QIcon.Off)'''
        return QPixmap()
    def pixmap(self, window, size, mode = None, state = None):
        '''QPixmap QIcon.pixmap(QWindow window, QSize size, QIcon.Mode mode = QIcon.Normal, QIcon.State state = QIcon.Off)'''
        return QPixmap()


class QIconEngine():
    """"""
    # Enum QIconEngine.IconEngineHook
    AvailableSizesHook = 0
    IconNameHook = 0

    def __init__(self):
        '''void QIconEngine.__init__()'''
    def __init__(self):
        '''QIconEngine QIconEngine.__init__()'''
        return QIconEngine()
    def iconName(self):
        '''str QIconEngine.iconName()'''
        return str()
    def availableSizes(self, mode = None, state = None):
        '''list-of-QSize QIconEngine.availableSizes(QIcon.Mode mode = QIcon.Normal, QIcon.State state = QIcon.Off)'''
        return [QSize()]
    def write(self, out):
        '''bool QIconEngine.write(QDataStream out)'''
        return bool()
    def read(self, in_):
        '''bool QIconEngine.read(QDataStream in)'''
        return bool()
    def clone(self):
        '''abstract QIconEngine QIconEngine.clone()'''
        return QIconEngine()
    def key(self):
        '''str QIconEngine.key()'''
        return str()
    def addFile(self, fileName, size, mode, state):
        '''void QIconEngine.addFile(str fileName, QSize size, QIcon.Mode mode, QIcon.State state)'''
    def addPixmap(self, pixmap, mode, state):
        '''void QIconEngine.addPixmap(QPixmap pixmap, QIcon.Mode mode, QIcon.State state)'''
    def pixmap(self, size, mode, state):
        '''QPixmap QIconEngine.pixmap(QSize size, QIcon.Mode mode, QIcon.State state)'''
        return QPixmap()
    def actualSize(self, size, mode, state):
        '''QSize QIconEngine.actualSize(QSize size, QIcon.Mode mode, QIcon.State state)'''
        return QSize()
    def paint(self, painter, rect, mode, state):
        '''abstract void QIconEngine.paint(QPainter painter, QRect rect, QIcon.Mode mode, QIcon.State state)'''
    class AvailableSizesArgument():
        """"""
        mode = None # QIcon.Mode - member
        sizes = None # list-of-QSize - member
        state = None # QIcon.State - member
        def __init__(self):
            '''void QIconEngine.AvailableSizesArgument.__init__()'''
        def __init__(self):
            '''QIconEngine.AvailableSizesArgument QIconEngine.AvailableSizesArgument.__init__()'''
            return QIconEngine.AvailableSizesArgument()


class QImage(QPaintDevice):
    """"""
    # Enum QImage.Format
    Format_Invalid = 0
    Format_Mono = 0
    Format_MonoLSB = 0
    Format_Indexed8 = 0
    Format_RGB32 = 0
    Format_ARGB32 = 0
    Format_ARGB32_Premultiplied = 0
    Format_RGB16 = 0
    Format_ARGB8565_Premultiplied = 0
    Format_RGB666 = 0
    Format_ARGB6666_Premultiplied = 0
    Format_RGB555 = 0
    Format_ARGB8555_Premultiplied = 0
    Format_RGB888 = 0
    Format_RGB444 = 0
    Format_ARGB4444_Premultiplied = 0
    Format_RGBX8888 = 0
    Format_RGBA8888 = 0
    Format_RGBA8888_Premultiplied = 0
    Format_BGR30 = 0
    Format_A2BGR30_Premultiplied = 0
    Format_RGB30 = 0
    Format_A2RGB30_Premultiplied = 0
    Format_Alpha8 = 0
    Format_Grayscale8 = 0

    # Enum QImage.InvertMode
    InvertRgb = 0
    InvertRgba = 0

    def __init__(self):
        '''void QImage.__init__()'''
    def __init__(self, size, format):
        '''void QImage.__init__(QSize size, QImage.Format format)'''
    def __init__(self, width, height, format):
        '''void QImage.__init__(int width, int height, QImage.Format format)'''
    def __init__(self, data, width, height, format):
        '''void QImage.__init__(str data, int width, int height, QImage.Format format)'''
    def __init__(self, data, width, height, format):
        '''void QImage.__init__(sip.voidptr data, int width, int height, QImage.Format format)'''
    def __init__(self, data, width, height, bytesPerLine, format):
        '''void QImage.__init__(str data, int width, int height, int bytesPerLine, QImage.Format format)'''
    def __init__(self, data, width, height, bytesPerLine, format):
        '''void QImage.__init__(sip.voidptr data, int width, int height, int bytesPerLine, QImage.Format format)'''
    def __init__(self, xpm):
        '''void QImage.__init__(list-of-str xpm)'''
    def __init__(self, fileName, format = None):
        '''void QImage.__init__(str fileName, str format = None)'''
    def __init__(self):
        '''QImage QImage.__init__()'''
        return QImage()
    def __init__(self, variant):
        '''void QImage.__init__(QVariant variant)'''
    def toImageFormat(self, format):
        '''static QImage.Format QImage.toImageFormat(QPixelFormat format)'''
        return QImage.Format()
    def toPixelFormat(self, format):
        '''static QPixelFormat QImage.toPixelFormat(QImage.Format format)'''
        return QPixelFormat()
    def pixelFormat(self):
        '''QPixelFormat QImage.pixelFormat()'''
        return QPixelFormat()
    def setDevicePixelRatio(self, scaleFactor):
        '''void QImage.setDevicePixelRatio(float scaleFactor)'''
    def devicePixelRatio(self):
        '''float QImage.devicePixelRatio()'''
        return float()
    def swap(self, other):
        '''void QImage.swap(QImage other)'''
    def bitPlaneCount(self):
        '''int QImage.bitPlaneCount()'''
        return int()
    def byteCount(self):
        '''int QImage.byteCount()'''
        return int()
    def setColorCount(self):
        '''int QImage.setColorCount()'''
        return int()
    def colorCount(self):
        '''int QImage.colorCount()'''
        return int()
    def cacheKey(self):
        '''int QImage.cacheKey()'''
        return int()
    def trueMatrix(self, w, h):
        '''static QTransform QImage.trueMatrix(int w, int h)'''
        return QTransform()
    def transformed(self, matrix, mode = None):
        '''QImage QImage.transformed(QTransform matrix, Qt.TransformationMode mode = Qt.FastTransformation)'''
        return QImage()
    def createMaskFromColor(self, color, mode = None):
        '''QImage QImage.createMaskFromColor(int color, Qt.MaskMode mode = Qt.MaskInColor)'''
        return QImage()
    def smoothScaled(self, w, h):
        '''QImage QImage.smoothScaled(int w, int h)'''
        return QImage()
    def metric(self, metric):
        '''int QImage.metric(QPaintDevice.PaintDeviceMetric metric)'''
        return int()
    def setText(self, key, value):
        '''void QImage.setText(str key, str value)'''
    def text(self, key = None):
        '''str QImage.text(str key = '')'''
        return str()
    def textKeys(self):
        '''list-of-str QImage.textKeys()'''
        return [str()]
    def setOffset(self):
        '''QPoint QImage.setOffset()'''
        return QPoint()
    def offset(self):
        '''QPoint QImage.offset()'''
        return QPoint()
    def setDotsPerMeterY(self):
        '''int QImage.setDotsPerMeterY()'''
        return int()
    def setDotsPerMeterX(self):
        '''int QImage.setDotsPerMeterX()'''
        return int()
    def dotsPerMeterY(self):
        '''int QImage.dotsPerMeterY()'''
        return int()
    def dotsPerMeterX(self):
        '''int QImage.dotsPerMeterX()'''
        return int()
    def paintEngine(self):
        '''QPaintEngine QImage.paintEngine()'''
        return QPaintEngine()
    def fromData(self, data, format = None):
        '''static QImage QImage.fromData(str data, str format = None)'''
        return QImage()
    def fromData(self, data, format = None):
        '''static QImage QImage.fromData(QByteArray data, str format = None)'''
        return QImage()
    def save(self, fileName, format = None, quality = None):
        '''bool QImage.save(str fileName, str format = None, int quality = -1)'''
        return bool()
    def save(self, device, format = None, quality = None):
        '''bool QImage.save(QIODevice device, str format = None, int quality = -1)'''
        return bool()
    def loadFromData(self, data, format = None):
        '''bool QImage.loadFromData(str data, str format = None)'''
        return bool()
    def loadFromData(self, data, format = None):
        '''bool QImage.loadFromData(QByteArray data, str format = None)'''
        return bool()
    def load(self, device, format):
        '''bool QImage.load(QIODevice device, str format)'''
        return bool()
    def load(self, fileName, format = None):
        '''bool QImage.load(str fileName, str format = None)'''
        return bool()
    def invertPixels(self, mode = None):
        '''void QImage.invertPixels(QImage.InvertMode mode = QImage.InvertRgb)'''
    def rgbSwapped(self):
        '''QImage QImage.rgbSwapped()'''
        return QImage()
    def mirrored(self, horizontal = False, vertical = True):
        '''QImage QImage.mirrored(bool horizontal = False, bool vertical = True)'''
        return QImage()
    def scaledToHeight(self, height, mode = None):
        '''QImage QImage.scaledToHeight(int height, Qt.TransformationMode mode = Qt.FastTransformation)'''
        return QImage()
    def scaledToWidth(self, width, mode = None):
        '''QImage QImage.scaledToWidth(int width, Qt.TransformationMode mode = Qt.FastTransformation)'''
        return QImage()
    def scaled(self, width, height, aspectRatioMode = None, transformMode = None):
        '''QImage QImage.scaled(int width, int height, Qt.AspectRatioMode aspectRatioMode = Qt.IgnoreAspectRatio, Qt.TransformationMode transformMode = Qt.FastTransformation)'''
        return QImage()
    def scaled(self, size, aspectRatioMode = None, transformMode = None):
        '''QImage QImage.scaled(QSize size, Qt.AspectRatioMode aspectRatioMode = Qt.IgnoreAspectRatio, Qt.TransformationMode transformMode = Qt.FastTransformation)'''
        return QImage()
    def createHeuristicMask(self, clipTight = True):
        '''QImage QImage.createHeuristicMask(bool clipTight = True)'''
        return QImage()
    def createAlphaMask(self, flags = None):
        '''QImage QImage.createAlphaMask(Qt.ImageConversionFlags flags = Qt.AutoColor)'''
        return QImage()
    def hasAlphaChannel(self):
        '''bool QImage.hasAlphaChannel()'''
        return bool()
    def fill(self, color):
        '''void QImage.fill(Qt.GlobalColor color)'''
    def fill(self, color):
        '''void QImage.fill(QColor color)'''
    def fill(self, pixel):
        '''void QImage.fill(int pixel)'''
    def setColorTable(self, colors):
        '''void QImage.setColorTable(list-of-int colors)'''
    def colorTable(self):
        '''list-of-int QImage.colorTable()'''
        return [int()]
    def setPixel(self, pt, index_or_rgb):
        '''void QImage.setPixel(QPoint pt, int index_or_rgb)'''
    def setPixel(self, x, y, index_or_rgb):
        '''void QImage.setPixel(int x, int y, int index_or_rgb)'''
    def pixel(self, pt):
        '''int QImage.pixel(QPoint pt)'''
        return int()
    def pixel(self, x, y):
        '''int QImage.pixel(int x, int y)'''
        return int()
    def pixelIndex(self, pt):
        '''int QImage.pixelIndex(QPoint pt)'''
        return int()
    def pixelIndex(self, x, y):
        '''int QImage.pixelIndex(int x, int y)'''
        return int()
    def valid(self, pt):
        '''bool QImage.valid(QPoint pt)'''
        return bool()
    def valid(self, x, y):
        '''bool QImage.valid(int x, int y)'''
        return bool()
    def bytesPerLine(self):
        '''int QImage.bytesPerLine()'''
        return int()
    def constScanLine(self):
        '''int QImage.constScanLine()'''
        return int()
    def scanLine(self):
        '''int QImage.scanLine()'''
        return int()
    def constBits(self):
        '''sip.voidptr QImage.constBits()'''
        return sip.voidptr()
    def bits(self):
        '''sip.voidptr QImage.bits()'''
        return sip.voidptr()
    def isGrayscale(self):
        '''bool QImage.isGrayscale()'''
        return bool()
    def allGray(self):
        '''bool QImage.allGray()'''
        return bool()
    def setColor(self, i, c):
        '''void QImage.setColor(int i, int c)'''
    def color(self, i):
        '''int QImage.color(int i)'''
        return int()
    def depth(self):
        '''int QImage.depth()'''
        return int()
    def rect(self):
        '''QRect QImage.rect()'''
        return QRect()
    def size(self):
        '''QSize QImage.size()'''
        return QSize()
    def height(self):
        '''int QImage.height()'''
        return int()
    def width(self):
        '''int QImage.width()'''
        return int()
    def convertToFormat(self, format, flags = None):
        '''QImage QImage.convertToFormat(QImage.Format format, Qt.ImageConversionFlags flags = Qt.AutoColor)'''
        return QImage()
    def convertToFormat(self, format, colorTable, flags = None):
        '''QImage QImage.convertToFormat(QImage.Format format, list-of-int colorTable, Qt.ImageConversionFlags flags = Qt.AutoColor)'''
        return QImage()
    def format(self):
        '''QImage.Format QImage.format()'''
        return QImage.Format()
    def copy(self, rect = QRect()):
        '''QImage QImage.copy(QRect rect = QRect())'''
        return QImage()
    def copy(self, x, y, w, h):
        '''QImage QImage.copy(int x, int y, int w, int h)'''
        return QImage()
    def isDetached(self):
        '''bool QImage.isDetached()'''
        return bool()
    def detach(self):
        '''void QImage.detach()'''
    def __ne__(self):
        '''QImage QImage.__ne__()'''
        return QImage()
    def __eq__(self):
        '''QImage QImage.__eq__()'''
        return QImage()
    def devType(self):
        '''int QImage.devType()'''
        return int()
    def isNull(self):
        '''bool QImage.isNull()'''
        return bool()


class QImageIOHandler():
    """"""
    # Enum QImageIOHandler.Transformation
    TransformationNone = 0
    TransformationMirror = 0
    TransformationFlip = 0
    TransformationRotate180 = 0
    TransformationRotate90 = 0
    TransformationMirrorAndRotate90 = 0
    TransformationFlipAndRotate90 = 0
    TransformationRotate270 = 0

    # Enum QImageIOHandler.ImageOption
    Size = 0
    ClipRect = 0
    Description = 0
    ScaledClipRect = 0
    ScaledSize = 0
    CompressionRatio = 0
    Gamma = 0
    Quality = 0
    Name = 0
    SubType = 0
    IncrementalReading = 0
    Endianness = 0
    Animation = 0
    BackgroundColor = 0
    SupportedSubTypes = 0
    OptimizedWrite = 0
    ProgressiveScanWrite = 0
    ImageTransformation = 0
    TransformedByDefault = 0

    def __init__(self):
        '''void QImageIOHandler.__init__()'''
    def currentImageRect(self):
        '''QRect QImageIOHandler.currentImageRect()'''
        return QRect()
    def currentImageNumber(self):
        '''int QImageIOHandler.currentImageNumber()'''
        return int()
    def nextImageDelay(self):
        '''int QImageIOHandler.nextImageDelay()'''
        return int()
    def imageCount(self):
        '''int QImageIOHandler.imageCount()'''
        return int()
    def loopCount(self):
        '''int QImageIOHandler.loopCount()'''
        return int()
    def jumpToImage(self, imageNumber):
        '''bool QImageIOHandler.jumpToImage(int imageNumber)'''
        return bool()
    def jumpToNextImage(self):
        '''bool QImageIOHandler.jumpToNextImage()'''
        return bool()
    def supportsOption(self, option):
        '''bool QImageIOHandler.supportsOption(QImageIOHandler.ImageOption option)'''
        return bool()
    def setOption(self, option, value):
        '''void QImageIOHandler.setOption(QImageIOHandler.ImageOption option, QVariant value)'''
    def option(self, option):
        '''QVariant QImageIOHandler.option(QImageIOHandler.ImageOption option)'''
        return QVariant()
    def write(self, image):
        '''bool QImageIOHandler.write(QImage image)'''
        return bool()
    def read(self, image):
        '''abstract bool QImageIOHandler.read(QImage image)'''
        return bool()
    def canRead(self):
        '''abstract bool QImageIOHandler.canRead()'''
        return bool()
    def format(self):
        '''QByteArray QImageIOHandler.format()'''
        return QByteArray()
    def setFormat(self, format):
        '''void QImageIOHandler.setFormat(QByteArray format)'''
    def device(self):
        '''QIODevice QImageIOHandler.device()'''
        return QIODevice()
    def setDevice(self, device):
        '''void QImageIOHandler.setDevice(QIODevice device)'''
    class Transformations():
        """"""
        def __init__(self):
            '''QImageIOHandler.Transformations QImageIOHandler.Transformations.__init__()'''
            return QImageIOHandler.Transformations()
        def __init__(self):
            '''int QImageIOHandler.Transformations.__init__()'''
            return int()
        def __init__(self):
            '''void QImageIOHandler.Transformations.__init__()'''
        def __bool__(self):
            '''int QImageIOHandler.Transformations.__bool__()'''
            return int()
        def __ne__(self, f):
            '''bool QImageIOHandler.Transformations.__ne__(QImageIOHandler.Transformations f)'''
            return bool()
        def __eq__(self, f):
            '''bool QImageIOHandler.Transformations.__eq__(QImageIOHandler.Transformations f)'''
            return bool()
        def __invert__(self):
            '''QImageIOHandler.Transformations QImageIOHandler.Transformations.__invert__()'''
            return QImageIOHandler.Transformations()
        def __and__(self, mask):
            '''QImageIOHandler.Transformations QImageIOHandler.Transformations.__and__(int mask)'''
            return QImageIOHandler.Transformations()
        def __xor__(self, f):
            '''QImageIOHandler.Transformations QImageIOHandler.Transformations.__xor__(QImageIOHandler.Transformations f)'''
            return QImageIOHandler.Transformations()
        def __xor__(self, f):
            '''QImageIOHandler.Transformations QImageIOHandler.Transformations.__xor__(int f)'''
            return QImageIOHandler.Transformations()
        def __or__(self, f):
            '''QImageIOHandler.Transformations QImageIOHandler.Transformations.__or__(QImageIOHandler.Transformations f)'''
            return QImageIOHandler.Transformations()
        def __or__(self, f):
            '''QImageIOHandler.Transformations QImageIOHandler.Transformations.__or__(int f)'''
            return QImageIOHandler.Transformations()
        def __int__(self):
            '''int QImageIOHandler.Transformations.__int__()'''
            return int()
        def __ixor__(self, f):
            '''QImageIOHandler.Transformations QImageIOHandler.Transformations.__ixor__(QImageIOHandler.Transformations f)'''
            return QImageIOHandler.Transformations()
        def __ior__(self, f):
            '''QImageIOHandler.Transformations QImageIOHandler.Transformations.__ior__(QImageIOHandler.Transformations f)'''
            return QImageIOHandler.Transformations()
        def __iand__(self, mask):
            '''QImageIOHandler.Transformations QImageIOHandler.Transformations.__iand__(int mask)'''
            return QImageIOHandler.Transformations()


class QImageReader():
    """"""
    # Enum QImageReader.ImageReaderError
    UnknownError = 0
    FileNotFoundError = 0
    DeviceError = 0
    UnsupportedFormatError = 0
    InvalidDataError = 0

    def __init__(self):
        '''void QImageReader.__init__()'''
    def __init__(self, device, format = QByteArray()):
        '''void QImageReader.__init__(QIODevice device, QByteArray format = QByteArray())'''
    def __init__(self, fileName, format = QByteArray()):
        '''void QImageReader.__init__(str fileName, QByteArray format = QByteArray())'''
    def autoTransform(self):
        '''bool QImageReader.autoTransform()'''
        return bool()
    def setAutoTransform(self, enabled):
        '''void QImageReader.setAutoTransform(bool enabled)'''
    def transformation(self):
        '''QImageIOHandler.Transformations QImageReader.transformation()'''
        return QImageIOHandler.Transformations()
    def supportedSubTypes(self):
        '''list-of-QByteArray QImageReader.supportedSubTypes()'''
        return [QByteArray()]
    def subType(self):
        '''QByteArray QImageReader.subType()'''
        return QByteArray()
    def supportedMimeTypes(self):
        '''static list-of-QByteArray QImageReader.supportedMimeTypes()'''
        return [QByteArray()]
    def decideFormatFromContent(self):
        '''bool QImageReader.decideFormatFromContent()'''
        return bool()
    def setDecideFormatFromContent(self, ignored):
        '''void QImageReader.setDecideFormatFromContent(bool ignored)'''
    def autoDetectImageFormat(self):
        '''bool QImageReader.autoDetectImageFormat()'''
        return bool()
    def setAutoDetectImageFormat(self, enabled):
        '''void QImageReader.setAutoDetectImageFormat(bool enabled)'''
    def supportsOption(self, option):
        '''bool QImageReader.supportsOption(QImageIOHandler.ImageOption option)'''
        return bool()
    def quality(self):
        '''int QImageReader.quality()'''
        return int()
    def setQuality(self, quality):
        '''void QImageReader.setQuality(int quality)'''
    def supportsAnimation(self):
        '''bool QImageReader.supportsAnimation()'''
        return bool()
    def backgroundColor(self):
        '''QColor QImageReader.backgroundColor()'''
        return QColor()
    def setBackgroundColor(self, color):
        '''void QImageReader.setBackgroundColor(QColor color)'''
    def text(self, key):
        '''str QImageReader.text(str key)'''
        return str()
    def textKeys(self):
        '''list-of-str QImageReader.textKeys()'''
        return [str()]
    def supportedImageFormats(self):
        '''static list-of-QByteArray QImageReader.supportedImageFormats()'''
        return [QByteArray()]
    def imageFormat(self, fileName):
        '''static QByteArray QImageReader.imageFormat(str fileName)'''
        return QByteArray()
    def imageFormat(self, device):
        '''static QByteArray QImageReader.imageFormat(QIODevice device)'''
        return QByteArray()
    def imageFormat(self):
        '''QImage.Format QImageReader.imageFormat()'''
        return QImage.Format()
    def errorString(self):
        '''str QImageReader.errorString()'''
        return str()
    def error(self):
        '''QImageReader.ImageReaderError QImageReader.error()'''
        return QImageReader.ImageReaderError()
    def currentImageRect(self):
        '''QRect QImageReader.currentImageRect()'''
        return QRect()
    def currentImageNumber(self):
        '''int QImageReader.currentImageNumber()'''
        return int()
    def nextImageDelay(self):
        '''int QImageReader.nextImageDelay()'''
        return int()
    def imageCount(self):
        '''int QImageReader.imageCount()'''
        return int()
    def loopCount(self):
        '''int QImageReader.loopCount()'''
        return int()
    def jumpToImage(self, imageNumber):
        '''bool QImageReader.jumpToImage(int imageNumber)'''
        return bool()
    def jumpToNextImage(self):
        '''bool QImageReader.jumpToNextImage()'''
        return bool()
    def read(self):
        '''QImage QImageReader.read()'''
        return QImage()
    def read(self, image):
        '''bool QImageReader.read(QImage image)'''
        return bool()
    def canRead(self):
        '''bool QImageReader.canRead()'''
        return bool()
    def scaledClipRect(self):
        '''QRect QImageReader.scaledClipRect()'''
        return QRect()
    def setScaledClipRect(self, rect):
        '''void QImageReader.setScaledClipRect(QRect rect)'''
    def scaledSize(self):
        '''QSize QImageReader.scaledSize()'''
        return QSize()
    def setScaledSize(self, size):
        '''void QImageReader.setScaledSize(QSize size)'''
    def clipRect(self):
        '''QRect QImageReader.clipRect()'''
        return QRect()
    def setClipRect(self, rect):
        '''void QImageReader.setClipRect(QRect rect)'''
    def size(self):
        '''QSize QImageReader.size()'''
        return QSize()
    def fileName(self):
        '''str QImageReader.fileName()'''
        return str()
    def setFileName(self, fileName):
        '''void QImageReader.setFileName(str fileName)'''
    def device(self):
        '''QIODevice QImageReader.device()'''
        return QIODevice()
    def setDevice(self, device):
        '''void QImageReader.setDevice(QIODevice device)'''
    def format(self):
        '''QByteArray QImageReader.format()'''
        return QByteArray()
    def setFormat(self, format):
        '''void QImageReader.setFormat(QByteArray format)'''


class QImageWriter():
    """"""
    # Enum QImageWriter.ImageWriterError
    UnknownError = 0
    DeviceError = 0
    UnsupportedFormatError = 0

    def __init__(self):
        '''void QImageWriter.__init__()'''
    def __init__(self, device, format):
        '''void QImageWriter.__init__(QIODevice device, QByteArray format)'''
    def __init__(self, fileName, format = QByteArray()):
        '''void QImageWriter.__init__(str fileName, QByteArray format = QByteArray())'''
    def setTransformation(self, orientation):
        '''void QImageWriter.setTransformation(QImageIOHandler.Transformations orientation)'''
    def transformation(self):
        '''QImageIOHandler.Transformations QImageWriter.transformation()'''
        return QImageIOHandler.Transformations()
    def progressiveScanWrite(self):
        '''bool QImageWriter.progressiveScanWrite()'''
        return bool()
    def setProgressiveScanWrite(self, progressive):
        '''void QImageWriter.setProgressiveScanWrite(bool progressive)'''
    def optimizedWrite(self):
        '''bool QImageWriter.optimizedWrite()'''
        return bool()
    def setOptimizedWrite(self, optimize):
        '''void QImageWriter.setOptimizedWrite(bool optimize)'''
    def supportedSubTypes(self):
        '''list-of-QByteArray QImageWriter.supportedSubTypes()'''
        return [QByteArray()]
    def subType(self):
        '''QByteArray QImageWriter.subType()'''
        return QByteArray()
    def setSubType(self, type):
        '''void QImageWriter.setSubType(QByteArray type)'''
    def supportedMimeTypes(self):
        '''static list-of-QByteArray QImageWriter.supportedMimeTypes()'''
        return [QByteArray()]
    def compression(self):
        '''int QImageWriter.compression()'''
        return int()
    def setCompression(self, compression):
        '''void QImageWriter.setCompression(int compression)'''
    def supportsOption(self, option):
        '''bool QImageWriter.supportsOption(QImageIOHandler.ImageOption option)'''
        return bool()
    def setText(self, key, text):
        '''void QImageWriter.setText(str key, str text)'''
    def supportedImageFormats(self):
        '''static list-of-QByteArray QImageWriter.supportedImageFormats()'''
        return [QByteArray()]
    def errorString(self):
        '''str QImageWriter.errorString()'''
        return str()
    def error(self):
        '''QImageWriter.ImageWriterError QImageWriter.error()'''
        return QImageWriter.ImageWriterError()
    def write(self, image):
        '''bool QImageWriter.write(QImage image)'''
        return bool()
    def canWrite(self):
        '''bool QImageWriter.canWrite()'''
        return bool()
    def gamma(self):
        '''float QImageWriter.gamma()'''
        return float()
    def setGamma(self, gamma):
        '''void QImageWriter.setGamma(float gamma)'''
    def quality(self):
        '''int QImageWriter.quality()'''
        return int()
    def setQuality(self, quality):
        '''void QImageWriter.setQuality(int quality)'''
    def fileName(self):
        '''str QImageWriter.fileName()'''
        return str()
    def setFileName(self, fileName):
        '''void QImageWriter.setFileName(str fileName)'''
    def device(self):
        '''QIODevice QImageWriter.device()'''
        return QIODevice()
    def setDevice(self, device):
        '''void QImageWriter.setDevice(QIODevice device)'''
    def format(self):
        '''QByteArray QImageWriter.format()'''
        return QByteArray()
    def setFormat(self, format):
        '''void QImageWriter.setFormat(QByteArray format)'''


class QInputMethod(QObject):
    """"""
    # Enum QInputMethod.Action
    Click = 0
    ContextMenu = 0

    inputDirectionChanged = pyqtSignal() # void inputDirectionChanged(Qt::LayoutDirection) - signal
    localeChanged = pyqtSignal() # void localeChanged() - signal
    animatingChanged = pyqtSignal() # void animatingChanged() - signal
    visibleChanged = pyqtSignal() # void visibleChanged() - signal
    keyboardRectangleChanged = pyqtSignal() # void keyboardRectangleChanged() - signal
    cursorRectangleChanged = pyqtSignal() # void cursorRectangleChanged() - signal
    def invokeAction(self, a, cursorPosition):
        '''void QInputMethod.invokeAction(QInputMethod.Action a, int cursorPosition)'''
    def commit(self):
        '''void QInputMethod.commit()'''
    def reset(self):
        '''void QInputMethod.reset()'''
    def update(self, queries):
        '''void QInputMethod.update(Qt.InputMethodQueries queries)'''
    def hide(self):
        '''void QInputMethod.hide()'''
    def show(self):
        '''void QInputMethod.show()'''
    def queryFocusObject(self, query, argument):
        '''static QVariant QInputMethod.queryFocusObject(Qt.InputMethodQuery query, QVariant argument)'''
        return QVariant()
    def setInputItemRectangle(self, rect):
        '''void QInputMethod.setInputItemRectangle(QRectF rect)'''
    def inputItemRectangle(self):
        '''QRectF QInputMethod.inputItemRectangle()'''
        return QRectF()
    def inputDirection(self):
        '''Qt.LayoutDirection QInputMethod.inputDirection()'''
        return Qt.LayoutDirection()
    def locale(self):
        '''QLocale QInputMethod.locale()'''
        return QLocale()
    def isAnimating(self):
        '''bool QInputMethod.isAnimating()'''
        return bool()
    def setVisible(self, visible):
        '''void QInputMethod.setVisible(bool visible)'''
    def isVisible(self):
        '''bool QInputMethod.isVisible()'''
        return bool()
    def keyboardRectangle(self):
        '''QRectF QInputMethod.keyboardRectangle()'''
        return QRectF()
    def cursorRectangle(self):
        '''QRectF QInputMethod.cursorRectangle()'''
        return QRectF()
    def setInputItemTransform(self, transform):
        '''void QInputMethod.setInputItemTransform(QTransform transform)'''
    def inputItemTransform(self):
        '''QTransform QInputMethod.inputItemTransform()'''
        return QTransform()


class QKeySequence():
    """"""
    # Enum QKeySequence.StandardKey
    UnknownKey = 0
    HelpContents = 0
    WhatsThis = 0
    Open = 0
    Close = 0
    Save = 0
    New = 0
    Delete = 0
    Cut = 0
    Copy = 0
    Paste = 0
    Undo = 0
    Redo = 0
    Back = 0
    Forward = 0
    Refresh = 0
    ZoomIn = 0
    ZoomOut = 0
    Print = 0
    AddTab = 0
    NextChild = 0
    PreviousChild = 0
    Find = 0
    FindNext = 0
    FindPrevious = 0
    Replace = 0
    SelectAll = 0
    Bold = 0
    Italic = 0
    Underline = 0
    MoveToNextChar = 0
    MoveToPreviousChar = 0
    MoveToNextWord = 0
    MoveToPreviousWord = 0
    MoveToNextLine = 0
    MoveToPreviousLine = 0
    MoveToNextPage = 0
    MoveToPreviousPage = 0
    MoveToStartOfLine = 0
    MoveToEndOfLine = 0
    MoveToStartOfBlock = 0
    MoveToEndOfBlock = 0
    MoveToStartOfDocument = 0
    MoveToEndOfDocument = 0
    SelectNextChar = 0
    SelectPreviousChar = 0
    SelectNextWord = 0
    SelectPreviousWord = 0
    SelectNextLine = 0
    SelectPreviousLine = 0
    SelectNextPage = 0
    SelectPreviousPage = 0
    SelectStartOfLine = 0
    SelectEndOfLine = 0
    SelectStartOfBlock = 0
    SelectEndOfBlock = 0
    SelectStartOfDocument = 0
    SelectEndOfDocument = 0
    DeleteStartOfWord = 0
    DeleteEndOfWord = 0
    DeleteEndOfLine = 0
    InsertParagraphSeparator = 0
    InsertLineSeparator = 0
    SaveAs = 0
    Preferences = 0
    Quit = 0
    FullScreen = 0
    Deselect = 0
    DeleteCompleteLine = 0
    Backspace = 0

    # Enum QKeySequence.SequenceMatch
    NoMatch = 0
    PartialMatch = 0
    ExactMatch = 0

    # Enum QKeySequence.SequenceFormat
    NativeText = 0
    PortableText = 0

    def __init__(self):
        '''void QKeySequence.__init__()'''
    def __init__(self, ks):
        '''void QKeySequence.__init__(QKeySequence ks)'''
    def __init__(self, key, format = None):
        '''void QKeySequence.__init__(str key, QKeySequence.SequenceFormat format = QKeySequence.NativeText)'''
    def __init__(self, k1, key2 = 0, key3 = 0, key4 = 0):
        '''void QKeySequence.__init__(int k1, int key2 = 0, int key3 = 0, int key4 = 0)'''
    def __init__(self, variant):
        '''void QKeySequence.__init__(QVariant variant)'''
    def listToString(self, list, format = None):
        '''static str QKeySequence.listToString(list-of-QKeySequence list, QKeySequence.SequenceFormat format = QKeySequence.PortableText)'''
        return str()
    def listFromString(self, str, format = None):
        '''static list-of-QKeySequence QKeySequence.listFromString(str str, QKeySequence.SequenceFormat format = QKeySequence.PortableText)'''
        return [QKeySequence()]
    def keyBindings(self, key):
        '''static list-of-QKeySequence QKeySequence.keyBindings(QKeySequence.StandardKey key)'''
        return [QKeySequence()]
    def fromString(self, str, format = None):
        '''static QKeySequence QKeySequence.fromString(str str, QKeySequence.SequenceFormat format = QKeySequence.PortableText)'''
        return QKeySequence()
    def toString(self, format = None):
        '''str QKeySequence.toString(QKeySequence.SequenceFormat format = QKeySequence.PortableText)'''
        return str()
    def swap(self, other):
        '''void QKeySequence.swap(QKeySequence other)'''
    def isDetached(self):
        '''bool QKeySequence.isDetached()'''
        return bool()
    def __ge__(self, other):
        '''bool QKeySequence.__ge__(QKeySequence other)'''
        return bool()
    def __le__(self, other):
        '''bool QKeySequence.__le__(QKeySequence other)'''
        return bool()
    def __gt__(self, other):
        '''bool QKeySequence.__gt__(QKeySequence other)'''
        return bool()
    def __lt__(self, ks):
        '''bool QKeySequence.__lt__(QKeySequence ks)'''
        return bool()
    def __ne__(self, other):
        '''bool QKeySequence.__ne__(QKeySequence other)'''
        return bool()
    def __eq__(self, other):
        '''bool QKeySequence.__eq__(QKeySequence other)'''
        return bool()
    def __getitem__(self, i):
        '''int QKeySequence.__getitem__(int i)'''
        return int()
    def mnemonic(self, text):
        '''static QKeySequence QKeySequence.mnemonic(str text)'''
        return QKeySequence()
    def matches(self, seq):
        '''QKeySequence.SequenceMatch QKeySequence.matches(QKeySequence seq)'''
        return QKeySequence.SequenceMatch()
    def isEmpty(self):
        '''bool QKeySequence.isEmpty()'''
        return bool()
    def __len__(self):
        ''' QKeySequence.__len__()'''
        return ()
    def count(self):
        '''int QKeySequence.count()'''
        return int()


class QMatrix4x4():
    """"""
    def __init__(self):
        '''void QMatrix4x4.__init__()'''
    def __init__(self, values):
        '''void QMatrix4x4.__init__(sequence-of-float values)'''
    def __init__(self, m11, m12, m13, m14, m21, m22, m23, m24, m31, m32, m33, m34, m41, m42, m43, m44):
        '''void QMatrix4x4.__init__(float m11, float m12, float m13, float m14, float m21, float m22, float m23, float m24, float m31, float m32, float m33, float m34, float m41, float m42, float m43, float m44)'''
    def __init__(self, transform):
        '''void QMatrix4x4.__init__(QTransform transform)'''
    def __init__(self):
        '''QMatrix4x4 QMatrix4x4.__init__()'''
        return QMatrix4x4()
    def __div__(self, divisor):
        '''QMatrix4x4 QMatrix4x4.__div__(float divisor)'''
        return QMatrix4x4()
    def __add__(self, m2):
        '''QMatrix4x4 QMatrix4x4.__add__(QMatrix4x4 m2)'''
        return QMatrix4x4()
    def __sub__(self, m2):
        '''QMatrix4x4 QMatrix4x4.__sub__(QMatrix4x4 m2)'''
        return QMatrix4x4()
    def __mul__(self, m2):
        '''QMatrix4x4 QMatrix4x4.__mul__(QMatrix4x4 m2)'''
        return QMatrix4x4()
    def __mul__(self, vector):
        '''QVector3D QMatrix4x4.__mul__(QVector3D vector)'''
        return QVector3D()
    def __mul__(self, vector):
        '''QVector4D QMatrix4x4.__mul__(QVector4D vector)'''
        return QVector4D()
    def __mul__(self, point):
        '''QPoint QMatrix4x4.__mul__(QPoint point)'''
        return QPoint()
    def __mul__(self, point):
        '''QPointF QMatrix4x4.__mul__(QPointF point)'''
        return QPointF()
    def __mul__(self, matrix):
        '''QMatrix4x4 QMatrix4x4.__mul__(QMatrix4x4 matrix)'''
        return QMatrix4x4()
    def __mul__(self, factor):
        '''QMatrix4x4 QMatrix4x4.__mul__(float factor)'''
        return QMatrix4x4()
    def __neg__(self):
        '''QMatrix4x4 QMatrix4x4.__neg__()'''
        return QMatrix4x4()
    def isAffine(self):
        '''bool QMatrix4x4.isAffine()'''
        return bool()
    def viewport(self, left, bottom, width, height, nearPlane = 0, farPlane = 1):
        '''void QMatrix4x4.viewport(float left, float bottom, float width, float height, float nearPlane = 0, float farPlane = 1)'''
    def viewport(self, rect):
        '''void QMatrix4x4.viewport(QRectF rect)'''
    def mapVector(self, vector):
        '''QVector3D QMatrix4x4.mapVector(QVector3D vector)'''
        return QVector3D()
    def map(self, point):
        '''QPoint QMatrix4x4.map(QPoint point)'''
        return QPoint()
    def map(self, point):
        '''QPointF QMatrix4x4.map(QPointF point)'''
        return QPointF()
    def map(self, point):
        '''QVector3D QMatrix4x4.map(QVector3D point)'''
        return QVector3D()
    def map(self, point):
        '''QVector4D QMatrix4x4.map(QVector4D point)'''
        return QVector4D()
    def __ne__(self, other):
        '''bool QMatrix4x4.__ne__(QMatrix4x4 other)'''
        return bool()
    def __eq__(self, other):
        '''bool QMatrix4x4.__eq__(QMatrix4x4 other)'''
        return bool()
    def __idiv__(self, divisor):
        '''QMatrix4x4 QMatrix4x4.__idiv__(float divisor)'''
        return QMatrix4x4()
    def __imul__(self, other):
        '''QMatrix4x4 QMatrix4x4.__imul__(QMatrix4x4 other)'''
        return QMatrix4x4()
    def __imul__(self, factor):
        '''QMatrix4x4 QMatrix4x4.__imul__(float factor)'''
        return QMatrix4x4()
    def __isub__(self, other):
        '''QMatrix4x4 QMatrix4x4.__isub__(QMatrix4x4 other)'''
        return QMatrix4x4()
    def __iadd__(self, other):
        '''QMatrix4x4 QMatrix4x4.__iadd__(QMatrix4x4 other)'''
        return QMatrix4x4()
    def fill(self, value):
        '''void QMatrix4x4.fill(float value)'''
    def setToIdentity(self):
        '''void QMatrix4x4.setToIdentity()'''
    def isIdentity(self):
        '''bool QMatrix4x4.isIdentity()'''
        return bool()
    def setRow(self, index, value):
        '''void QMatrix4x4.setRow(int index, QVector4D value)'''
    def row(self, index):
        '''QVector4D QMatrix4x4.row(int index)'''
        return QVector4D()
    def setColumn(self, index, value):
        '''void QMatrix4x4.setColumn(int index, QVector4D value)'''
    def column(self, index):
        '''QVector4D QMatrix4x4.column(int index)'''
        return QVector4D()
    def __setitem__(self):
        '''float QMatrix4x4.__setitem__()'''
        return float()
    def __getitem__(self):
        '''object QMatrix4x4.__getitem__()'''
        return object()
    def optimize(self):
        '''void QMatrix4x4.optimize()'''
    def data(self):
        '''list-of-float QMatrix4x4.data()'''
        return [float()]
    def mapRect(self, rect):
        '''QRect QMatrix4x4.mapRect(QRect rect)'''
        return QRect()
    def mapRect(self, rect):
        '''QRectF QMatrix4x4.mapRect(QRectF rect)'''
        return QRectF()
    def toTransform(self):
        '''QTransform QMatrix4x4.toTransform()'''
        return QTransform()
    def toTransform(self, distanceToPlane):
        '''QTransform QMatrix4x4.toTransform(float distanceToPlane)'''
        return QTransform()
    def copyDataTo(self):
        '''list-of-float QMatrix4x4.copyDataTo()'''
        return [float()]
    def lookAt(self, eye, center, up):
        '''void QMatrix4x4.lookAt(QVector3D eye, QVector3D center, QVector3D up)'''
    def perspective(self, angle, aspect, nearPlane, farPlane):
        '''void QMatrix4x4.perspective(float angle, float aspect, float nearPlane, float farPlane)'''
    def frustum(self, left, right, bottom, top, nearPlane, farPlane):
        '''void QMatrix4x4.frustum(float left, float right, float bottom, float top, float nearPlane, float farPlane)'''
    def ortho(self, rect):
        '''void QMatrix4x4.ortho(QRect rect)'''
    def ortho(self, rect):
        '''void QMatrix4x4.ortho(QRectF rect)'''
    def ortho(self, left, right, bottom, top, nearPlane, farPlane):
        '''void QMatrix4x4.ortho(float left, float right, float bottom, float top, float nearPlane, float farPlane)'''
    def rotate(self, angle, vector):
        '''void QMatrix4x4.rotate(float angle, QVector3D vector)'''
    def rotate(self, angle, x, y, z = 0):
        '''void QMatrix4x4.rotate(float angle, float x, float y, float z = 0)'''
    def rotate(self, quaternion):
        '''void QMatrix4x4.rotate(QQuaternion quaternion)'''
    def translate(self, vector):
        '''void QMatrix4x4.translate(QVector3D vector)'''
    def translate(self, x, y):
        '''void QMatrix4x4.translate(float x, float y)'''
    def translate(self, x, y, z):
        '''void QMatrix4x4.translate(float x, float y, float z)'''
    def scale(self, vector):
        '''void QMatrix4x4.scale(QVector3D vector)'''
    def scale(self, x, y):
        '''void QMatrix4x4.scale(float x, float y)'''
    def scale(self, x, y, z):
        '''void QMatrix4x4.scale(float x, float y, float z)'''
    def scale(self, factor):
        '''void QMatrix4x4.scale(float factor)'''
    def normalMatrix(self):
        '''QMatrix3x3 QMatrix4x4.normalMatrix()'''
        return QMatrix3x3()
    def transposed(self):
        '''QMatrix4x4 QMatrix4x4.transposed()'''
        return QMatrix4x4()
    def inverted(self, invertible):
        '''QMatrix4x4 QMatrix4x4.inverted(bool invertible)'''
        return QMatrix4x4()
    def determinant(self):
        '''float QMatrix4x4.determinant()'''
        return float()
    def __repr__(self):
        '''str QMatrix4x4.__repr__()'''
        return str()


class QMovie(QObject):
    """"""
    # Enum QMovie.CacheMode
    CacheNone = 0
    CacheAll = 0

    # Enum QMovie.MovieState
    NotRunning = 0
    Paused = 0
    Running = 0

    def __init__(self, parent = None):
        '''void QMovie.__init__(QObject parent = None)'''
    def __init__(self, device, format = QByteArray(), parent = None):
        '''void QMovie.__init__(QIODevice device, QByteArray format = QByteArray(), QObject parent = None)'''
    def __init__(self, fileName, format = QByteArray(), parent = None):
        '''void QMovie.__init__(str fileName, QByteArray format = QByteArray(), QObject parent = None)'''
    def stop(self):
        '''void QMovie.stop()'''
    def setPaused(self, paused):
        '''void QMovie.setPaused(bool paused)'''
    def jumpToNextFrame(self):
        '''bool QMovie.jumpToNextFrame()'''
        return bool()
    def start(self):
        '''void QMovie.start()'''
    frameChanged = pyqtSignal() # void frameChanged(int) - signal
    finished = pyqtSignal() # void finished() - signal
    error = pyqtSignal() # void error(QImageReader::ImageReaderError) - signal
    stateChanged = pyqtSignal() # void stateChanged(QMovie::MovieState) - signal
    updated = pyqtSignal() # void updated(const QRectamp;) - signal
    resized = pyqtSignal() # void resized(const QSizeamp;) - signal
    started = pyqtSignal() # void started() - signal
    def setCacheMode(self, mode):
        '''void QMovie.setCacheMode(QMovie.CacheMode mode)'''
    def cacheMode(self):
        '''QMovie.CacheMode QMovie.cacheMode()'''
        return QMovie.CacheMode()
    def setScaledSize(self, size):
        '''void QMovie.setScaledSize(QSize size)'''
    def scaledSize(self):
        '''QSize QMovie.scaledSize()'''
        return QSize()
    def speed(self):
        '''int QMovie.speed()'''
        return int()
    def setSpeed(self, percentSpeed):
        '''void QMovie.setSpeed(int percentSpeed)'''
    def currentFrameNumber(self):
        '''int QMovie.currentFrameNumber()'''
        return int()
    def nextFrameDelay(self):
        '''int QMovie.nextFrameDelay()'''
        return int()
    def frameCount(self):
        '''int QMovie.frameCount()'''
        return int()
    def loopCount(self):
        '''int QMovie.loopCount()'''
        return int()
    def jumpToFrame(self, frameNumber):
        '''bool QMovie.jumpToFrame(int frameNumber)'''
        return bool()
    def isValid(self):
        '''bool QMovie.isValid()'''
        return bool()
    def currentPixmap(self):
        '''QPixmap QMovie.currentPixmap()'''
        return QPixmap()
    def currentImage(self):
        '''QImage QMovie.currentImage()'''
        return QImage()
    def frameRect(self):
        '''QRect QMovie.frameRect()'''
        return QRect()
    def state(self):
        '''QMovie.MovieState QMovie.state()'''
        return QMovie.MovieState()
    def backgroundColor(self):
        '''QColor QMovie.backgroundColor()'''
        return QColor()
    def setBackgroundColor(self, color):
        '''void QMovie.setBackgroundColor(QColor color)'''
    def format(self):
        '''QByteArray QMovie.format()'''
        return QByteArray()
    def setFormat(self, format):
        '''void QMovie.setFormat(QByteArray format)'''
    def fileName(self):
        '''str QMovie.fileName()'''
        return str()
    def setFileName(self, fileName):
        '''void QMovie.setFileName(str fileName)'''
    def device(self):
        '''QIODevice QMovie.device()'''
        return QIODevice()
    def setDevice(self, device):
        '''void QMovie.setDevice(QIODevice device)'''
    def supportedFormats(self):
        '''static list-of-QByteArray QMovie.supportedFormats()'''
        return [QByteArray()]


class QSurface():
    """"""
    # Enum QSurface.SurfaceType
    RasterSurface = 0
    OpenGLSurface = 0
    RasterGLSurface = 0

    # Enum QSurface.SurfaceClass
    Window = 0
    Offscreen = 0

    def __init__(self, type):
        '''void QSurface.__init__(QSurface.SurfaceClass type)'''
    def __init__(self):
        '''QSurface QSurface.__init__()'''
        return QSurface()
    def supportsOpenGL(self):
        '''bool QSurface.supportsOpenGL()'''
        return bool()
    def size(self):
        '''abstract QSize QSurface.size()'''
        return QSize()
    def surfaceType(self):
        '''abstract QSurface.SurfaceType QSurface.surfaceType()'''
        return QSurface.SurfaceType()
    def format(self):
        '''abstract QSurfaceFormat QSurface.format()'''
        return QSurfaceFormat()
    def surfaceClass(self):
        '''QSurface.SurfaceClass QSurface.surfaceClass()'''
        return QSurface.SurfaceClass()


class QOffscreenSurface(QObject, QSurface):
    """"""
    def __init__(self, screen = None):
        '''void QOffscreenSurface.__init__(QScreen screen = None)'''
    screenChanged = pyqtSignal() # void screenChanged(QScreen*) - signal
    def setScreen(self, screen):
        '''void QOffscreenSurface.setScreen(QScreen screen)'''
    def screen(self):
        '''QScreen QOffscreenSurface.screen()'''
        return QScreen()
    def size(self):
        '''QSize QOffscreenSurface.size()'''
        return QSize()
    def requestedFormat(self):
        '''QSurfaceFormat QOffscreenSurface.requestedFormat()'''
        return QSurfaceFormat()
    def format(self):
        '''QSurfaceFormat QOffscreenSurface.format()'''
        return QSurfaceFormat()
    def setFormat(self, format):
        '''void QOffscreenSurface.setFormat(QSurfaceFormat format)'''
    def isValid(self):
        '''bool QOffscreenSurface.isValid()'''
        return bool()
    def destroy(self):
        '''void QOffscreenSurface.destroy()'''
    def create(self):
        '''void QOffscreenSurface.create()'''
    def surfaceType(self):
        '''QSurface.SurfaceType QOffscreenSurface.surfaceType()'''
        return QSurface.SurfaceType()


class QOpenGLBuffer():
    """"""
    # Enum QOpenGLBuffer.RangeAccessFlag
    RangeRead = 0
    RangeWrite = 0
    RangeInvalidate = 0
    RangeInvalidateBuffer = 0
    RangeFlushExplicit = 0
    RangeUnsynchronized = 0

    # Enum QOpenGLBuffer.Access
    ReadOnly = 0
    WriteOnly = 0
    ReadWrite = 0

    # Enum QOpenGLBuffer.UsagePattern
    StreamDraw = 0
    StreamRead = 0
    StreamCopy = 0
    StaticDraw = 0
    StaticRead = 0
    StaticCopy = 0
    DynamicDraw = 0
    DynamicRead = 0
    DynamicCopy = 0

    # Enum QOpenGLBuffer.Type
    VertexBuffer = 0
    IndexBuffer = 0
    PixelPackBuffer = 0
    PixelUnpackBuffer = 0

    def __init__(self):
        '''void QOpenGLBuffer.__init__()'''
    def __init__(self, type):
        '''void QOpenGLBuffer.__init__(QOpenGLBuffer.Type type)'''
    def __init__(self, other):
        '''void QOpenGLBuffer.__init__(QOpenGLBuffer other)'''
    def mapRange(self, offset, count, access):
        '''sip.voidptr QOpenGLBuffer.mapRange(int offset, int count, QOpenGLBuffer.RangeAccessFlags access)'''
        return sip.voidptr()
    def unmap(self):
        '''bool QOpenGLBuffer.unmap()'''
        return bool()
    def map(self, access):
        '''sip.voidptr QOpenGLBuffer.map(QOpenGLBuffer.Access access)'''
        return sip.voidptr()
    def allocate(self, data, count):
        '''void QOpenGLBuffer.allocate(sip.voidptr data, int count)'''
    def allocate(self, count):
        '''void QOpenGLBuffer.allocate(int count)'''
    def write(self, offset, data, count):
        '''void QOpenGLBuffer.write(int offset, sip.voidptr data, int count)'''
    def read(self, offset, data, count):
        '''bool QOpenGLBuffer.read(int offset, sip.voidptr data, int count)'''
        return bool()
    def __len__(self):
        ''' QOpenGLBuffer.__len__()'''
        return ()
    def size(self):
        '''int QOpenGLBuffer.size()'''
        return int()
    def bufferId(self):
        '''int QOpenGLBuffer.bufferId()'''
        return int()
    def release(self):
        '''void QOpenGLBuffer.release()'''
    def release(self, type):
        '''static void QOpenGLBuffer.release(QOpenGLBuffer.Type type)'''
    def bind(self):
        '''bool QOpenGLBuffer.bind()'''
        return bool()
    def destroy(self):
        '''void QOpenGLBuffer.destroy()'''
    def isCreated(self):
        '''bool QOpenGLBuffer.isCreated()'''
        return bool()
    def create(self):
        '''bool QOpenGLBuffer.create()'''
        return bool()
    def setUsagePattern(self, value):
        '''void QOpenGLBuffer.setUsagePattern(QOpenGLBuffer.UsagePattern value)'''
    def usagePattern(self):
        '''QOpenGLBuffer.UsagePattern QOpenGLBuffer.usagePattern()'''
        return QOpenGLBuffer.UsagePattern()
    def type(self):
        '''QOpenGLBuffer.Type QOpenGLBuffer.type()'''
        return QOpenGLBuffer.Type()
    class RangeAccessFlags():
        """"""
        def __init__(self):
            '''QOpenGLBuffer.RangeAccessFlags QOpenGLBuffer.RangeAccessFlags.__init__()'''
            return QOpenGLBuffer.RangeAccessFlags()
        def __init__(self):
            '''int QOpenGLBuffer.RangeAccessFlags.__init__()'''
            return int()
        def __init__(self):
            '''void QOpenGLBuffer.RangeAccessFlags.__init__()'''
        def __bool__(self):
            '''int QOpenGLBuffer.RangeAccessFlags.__bool__()'''
            return int()
        def __ne__(self, f):
            '''bool QOpenGLBuffer.RangeAccessFlags.__ne__(QOpenGLBuffer.RangeAccessFlags f)'''
            return bool()
        def __eq__(self, f):
            '''bool QOpenGLBuffer.RangeAccessFlags.__eq__(QOpenGLBuffer.RangeAccessFlags f)'''
            return bool()
        def __invert__(self):
            '''QOpenGLBuffer.RangeAccessFlags QOpenGLBuffer.RangeAccessFlags.__invert__()'''
            return QOpenGLBuffer.RangeAccessFlags()
        def __and__(self, mask):
            '''QOpenGLBuffer.RangeAccessFlags QOpenGLBuffer.RangeAccessFlags.__and__(int mask)'''
            return QOpenGLBuffer.RangeAccessFlags()
        def __xor__(self, f):
            '''QOpenGLBuffer.RangeAccessFlags QOpenGLBuffer.RangeAccessFlags.__xor__(QOpenGLBuffer.RangeAccessFlags f)'''
            return QOpenGLBuffer.RangeAccessFlags()
        def __xor__(self, f):
            '''QOpenGLBuffer.RangeAccessFlags QOpenGLBuffer.RangeAccessFlags.__xor__(int f)'''
            return QOpenGLBuffer.RangeAccessFlags()
        def __or__(self, f):
            '''QOpenGLBuffer.RangeAccessFlags QOpenGLBuffer.RangeAccessFlags.__or__(QOpenGLBuffer.RangeAccessFlags f)'''
            return QOpenGLBuffer.RangeAccessFlags()
        def __or__(self, f):
            '''QOpenGLBuffer.RangeAccessFlags QOpenGLBuffer.RangeAccessFlags.__or__(int f)'''
            return QOpenGLBuffer.RangeAccessFlags()
        def __int__(self):
            '''int QOpenGLBuffer.RangeAccessFlags.__int__()'''
            return int()
        def __ixor__(self, f):
            '''QOpenGLBuffer.RangeAccessFlags QOpenGLBuffer.RangeAccessFlags.__ixor__(QOpenGLBuffer.RangeAccessFlags f)'''
            return QOpenGLBuffer.RangeAccessFlags()
        def __ior__(self, f):
            '''QOpenGLBuffer.RangeAccessFlags QOpenGLBuffer.RangeAccessFlags.__ior__(QOpenGLBuffer.RangeAccessFlags f)'''
            return QOpenGLBuffer.RangeAccessFlags()
        def __iand__(self, mask):
            '''QOpenGLBuffer.RangeAccessFlags QOpenGLBuffer.RangeAccessFlags.__iand__(int mask)'''
            return QOpenGLBuffer.RangeAccessFlags()


class QOpenGLContextGroup(QObject):
    """"""
    def currentContextGroup(self):
        '''static QOpenGLContextGroup QOpenGLContextGroup.currentContextGroup()'''
        return QOpenGLContextGroup()
    def shares(self):
        '''list-of-QOpenGLContext QOpenGLContextGroup.shares()'''
        return [QOpenGLContext()]


class QOpenGLContext(QObject):
    """"""
    # Enum QOpenGLContext.OpenGLModuleType
    LibGL = 0
    LibGLES = 0

    def __init__(self, parent = None):
        '''void QOpenGLContext.__init__(QObject parent = None)'''
    def globalShareContext(self):
        '''static QOpenGLContext QOpenGLContext.globalShareContext()'''
        return QOpenGLContext()
    def supportsThreadedOpenGL(self):
        '''static bool QOpenGLContext.supportsThreadedOpenGL()'''
        return bool()
    def nativeHandle(self):
        '''QVariant QOpenGLContext.nativeHandle()'''
        return QVariant()
    def setNativeHandle(self, handle):
        '''void QOpenGLContext.setNativeHandle(QVariant handle)'''
    def isOpenGLES(self):
        '''bool QOpenGLContext.isOpenGLES()'''
        return bool()
    def openGLModuleType(self):
        '''static QOpenGLContext.OpenGLModuleType QOpenGLContext.openGLModuleType()'''
        return QOpenGLContext.OpenGLModuleType()
    def openGLModuleHandle(self):
        '''static sip.voidptr QOpenGLContext.openGLModuleHandle()'''
        return sip.voidptr()
    def versionFunctions(self, versionProfile = None):
        '''object QOpenGLContext.versionFunctions(QOpenGLVersionProfile versionProfile = None)'''
        return object()
    aboutToBeDestroyed = pyqtSignal() # void aboutToBeDestroyed() - signal
    def hasExtension(self, extension):
        '''bool QOpenGLContext.hasExtension(QByteArray extension)'''
        return bool()
    def extensions(self):
        '''set-of-QByteArray QOpenGLContext.extensions()'''
        return set-of-QByteArray()
    def areSharing(self, first, second):
        '''static bool QOpenGLContext.areSharing(QOpenGLContext first, QOpenGLContext second)'''
        return bool()
    def currentContext(self):
        '''static QOpenGLContext QOpenGLContext.currentContext()'''
        return QOpenGLContext()
    def surface(self):
        '''QSurface QOpenGLContext.surface()'''
        return QSurface()
    def swapBuffers(self, surface):
        '''void QOpenGLContext.swapBuffers(QSurface surface)'''
    def doneCurrent(self):
        '''void QOpenGLContext.doneCurrent()'''
    def makeCurrent(self, surface):
        '''bool QOpenGLContext.makeCurrent(QSurface surface)'''
        return bool()
    def defaultFramebufferObject(self):
        '''int QOpenGLContext.defaultFramebufferObject()'''
        return int()
    def screen(self):
        '''QScreen QOpenGLContext.screen()'''
        return QScreen()
    def shareGroup(self):
        '''QOpenGLContextGroup QOpenGLContext.shareGroup()'''
        return QOpenGLContextGroup()
    def shareContext(self):
        '''QOpenGLContext QOpenGLContext.shareContext()'''
        return QOpenGLContext()
    def format(self):
        '''QSurfaceFormat QOpenGLContext.format()'''
        return QSurfaceFormat()
    def isValid(self):
        '''bool QOpenGLContext.isValid()'''
        return bool()
    def create(self):
        '''bool QOpenGLContext.create()'''
        return bool()
    def setScreen(self, screen):
        '''void QOpenGLContext.setScreen(QScreen screen)'''
    def setShareContext(self, shareContext):
        '''void QOpenGLContext.setShareContext(QOpenGLContext shareContext)'''
    def setFormat(self, format):
        '''void QOpenGLContext.setFormat(QSurfaceFormat format)'''


class QOpenGLVersionProfile():
    """"""
    def __init__(self):
        '''void QOpenGLVersionProfile.__init__()'''
    def __init__(self, format):
        '''void QOpenGLVersionProfile.__init__(QSurfaceFormat format)'''
    def __init__(self, other):
        '''void QOpenGLVersionProfile.__init__(QOpenGLVersionProfile other)'''
    def __eq__(self, rhs):
        '''bool QOpenGLVersionProfile.__eq__(QOpenGLVersionProfile rhs)'''
        return bool()
    def __ne__(self, rhs):
        '''bool QOpenGLVersionProfile.__ne__(QOpenGLVersionProfile rhs)'''
        return bool()
    def isValid(self):
        '''bool QOpenGLVersionProfile.isValid()'''
        return bool()
    def isLegacyVersion(self):
        '''bool QOpenGLVersionProfile.isLegacyVersion()'''
        return bool()
    def hasProfiles(self):
        '''bool QOpenGLVersionProfile.hasProfiles()'''
        return bool()
    def setProfile(self, profile):
        '''void QOpenGLVersionProfile.setProfile(QSurfaceFormat.OpenGLContextProfile profile)'''
    def profile(self):
        '''QSurfaceFormat.OpenGLContextProfile QOpenGLVersionProfile.profile()'''
        return QSurfaceFormat.OpenGLContextProfile()
    def setVersion(self, majorVersion, minorVersion):
        '''void QOpenGLVersionProfile.setVersion(int majorVersion, int minorVersion)'''
    def version(self):
        '''tuple-of-int-int QOpenGLVersionProfile.version()'''
        return tuple-of-int-int()


class QOpenGLDebugMessage():
    """"""
    # Enum QOpenGLDebugMessage.Severity
    InvalidSeverity = 0
    HighSeverity = 0
    MediumSeverity = 0
    LowSeverity = 0
    NotificationSeverity = 0
    AnySeverity = 0

    # Enum QOpenGLDebugMessage.Type
    InvalidType = 0
    ErrorType = 0
    DeprecatedBehaviorType = 0
    UndefinedBehaviorType = 0
    PortabilityType = 0
    PerformanceType = 0
    OtherType = 0
    MarkerType = 0
    GroupPushType = 0
    GroupPopType = 0
    AnyType = 0

    # Enum QOpenGLDebugMessage.Source
    InvalidSource = 0
    APISource = 0
    WindowSystemSource = 0
    ShaderCompilerSource = 0
    ThirdPartySource = 0
    ApplicationSource = 0
    OtherSource = 0
    AnySource = 0

    def __init__(self):
        '''void QOpenGLDebugMessage.__init__()'''
    def __init__(self, debugMessage):
        '''void QOpenGLDebugMessage.__init__(QOpenGLDebugMessage debugMessage)'''
    def __ne__(self, debugMessage):
        '''bool QOpenGLDebugMessage.__ne__(QOpenGLDebugMessage debugMessage)'''
        return bool()
    def __eq__(self, debugMessage):
        '''bool QOpenGLDebugMessage.__eq__(QOpenGLDebugMessage debugMessage)'''
        return bool()
    def createThirdPartyMessage(self, text, id = 0, severity = None, type = None):
        '''static QOpenGLDebugMessage QOpenGLDebugMessage.createThirdPartyMessage(str text, int id = 0, QOpenGLDebugMessage.Severity severity = QOpenGLDebugMessage.NotificationSeverity, QOpenGLDebugMessage.Type type = QOpenGLDebugMessage.OtherType)'''
        return QOpenGLDebugMessage()
    def createApplicationMessage(self, text, id = 0, severity = None, type = None):
        '''static QOpenGLDebugMessage QOpenGLDebugMessage.createApplicationMessage(str text, int id = 0, QOpenGLDebugMessage.Severity severity = QOpenGLDebugMessage.NotificationSeverity, QOpenGLDebugMessage.Type type = QOpenGLDebugMessage.OtherType)'''
        return QOpenGLDebugMessage()
    def message(self):
        '''str QOpenGLDebugMessage.message()'''
        return str()
    def id(self):
        '''int QOpenGLDebugMessage.id()'''
        return int()
    def severity(self):
        '''QOpenGLDebugMessage.Severity QOpenGLDebugMessage.severity()'''
        return QOpenGLDebugMessage.Severity()
    def type(self):
        '''QOpenGLDebugMessage.Type QOpenGLDebugMessage.type()'''
        return QOpenGLDebugMessage.Type()
    def source(self):
        '''QOpenGLDebugMessage.Source QOpenGLDebugMessage.source()'''
        return QOpenGLDebugMessage.Source()
    def swap(self, debugMessage):
        '''void QOpenGLDebugMessage.swap(QOpenGLDebugMessage debugMessage)'''
    class Sources():
        """"""
        def __init__(self):
            '''QOpenGLDebugMessage.Sources QOpenGLDebugMessage.Sources.__init__()'''
            return QOpenGLDebugMessage.Sources()
        def __init__(self):
            '''int QOpenGLDebugMessage.Sources.__init__()'''
            return int()
        def __init__(self):
            '''void QOpenGLDebugMessage.Sources.__init__()'''
        def __bool__(self):
            '''int QOpenGLDebugMessage.Sources.__bool__()'''
            return int()
        def __ne__(self, f):
            '''bool QOpenGLDebugMessage.Sources.__ne__(QOpenGLDebugMessage.Sources f)'''
            return bool()
        def __eq__(self, f):
            '''bool QOpenGLDebugMessage.Sources.__eq__(QOpenGLDebugMessage.Sources f)'''
            return bool()
        def __invert__(self):
            '''QOpenGLDebugMessage.Sources QOpenGLDebugMessage.Sources.__invert__()'''
            return QOpenGLDebugMessage.Sources()
        def __and__(self, mask):
            '''QOpenGLDebugMessage.Sources QOpenGLDebugMessage.Sources.__and__(int mask)'''
            return QOpenGLDebugMessage.Sources()
        def __xor__(self, f):
            '''QOpenGLDebugMessage.Sources QOpenGLDebugMessage.Sources.__xor__(QOpenGLDebugMessage.Sources f)'''
            return QOpenGLDebugMessage.Sources()
        def __xor__(self, f):
            '''QOpenGLDebugMessage.Sources QOpenGLDebugMessage.Sources.__xor__(int f)'''
            return QOpenGLDebugMessage.Sources()
        def __or__(self, f):
            '''QOpenGLDebugMessage.Sources QOpenGLDebugMessage.Sources.__or__(QOpenGLDebugMessage.Sources f)'''
            return QOpenGLDebugMessage.Sources()
        def __or__(self, f):
            '''QOpenGLDebugMessage.Sources QOpenGLDebugMessage.Sources.__or__(int f)'''
            return QOpenGLDebugMessage.Sources()
        def __int__(self):
            '''int QOpenGLDebugMessage.Sources.__int__()'''
            return int()
        def __ixor__(self, f):
            '''QOpenGLDebugMessage.Sources QOpenGLDebugMessage.Sources.__ixor__(QOpenGLDebugMessage.Sources f)'''
            return QOpenGLDebugMessage.Sources()
        def __ior__(self, f):
            '''QOpenGLDebugMessage.Sources QOpenGLDebugMessage.Sources.__ior__(QOpenGLDebugMessage.Sources f)'''
            return QOpenGLDebugMessage.Sources()
        def __iand__(self, mask):
            '''QOpenGLDebugMessage.Sources QOpenGLDebugMessage.Sources.__iand__(int mask)'''
            return QOpenGLDebugMessage.Sources()
    class Severities():
        """"""
        def __init__(self):
            '''QOpenGLDebugMessage.Severities QOpenGLDebugMessage.Severities.__init__()'''
            return QOpenGLDebugMessage.Severities()
        def __init__(self):
            '''int QOpenGLDebugMessage.Severities.__init__()'''
            return int()
        def __init__(self):
            '''void QOpenGLDebugMessage.Severities.__init__()'''
        def __bool__(self):
            '''int QOpenGLDebugMessage.Severities.__bool__()'''
            return int()
        def __ne__(self, f):
            '''bool QOpenGLDebugMessage.Severities.__ne__(QOpenGLDebugMessage.Severities f)'''
            return bool()
        def __eq__(self, f):
            '''bool QOpenGLDebugMessage.Severities.__eq__(QOpenGLDebugMessage.Severities f)'''
            return bool()
        def __invert__(self):
            '''QOpenGLDebugMessage.Severities QOpenGLDebugMessage.Severities.__invert__()'''
            return QOpenGLDebugMessage.Severities()
        def __and__(self, mask):
            '''QOpenGLDebugMessage.Severities QOpenGLDebugMessage.Severities.__and__(int mask)'''
            return QOpenGLDebugMessage.Severities()
        def __xor__(self, f):
            '''QOpenGLDebugMessage.Severities QOpenGLDebugMessage.Severities.__xor__(QOpenGLDebugMessage.Severities f)'''
            return QOpenGLDebugMessage.Severities()
        def __xor__(self, f):
            '''QOpenGLDebugMessage.Severities QOpenGLDebugMessage.Severities.__xor__(int f)'''
            return QOpenGLDebugMessage.Severities()
        def __or__(self, f):
            '''QOpenGLDebugMessage.Severities QOpenGLDebugMessage.Severities.__or__(QOpenGLDebugMessage.Severities f)'''
            return QOpenGLDebugMessage.Severities()
        def __or__(self, f):
            '''QOpenGLDebugMessage.Severities QOpenGLDebugMessage.Severities.__or__(int f)'''
            return QOpenGLDebugMessage.Severities()
        def __int__(self):
            '''int QOpenGLDebugMessage.Severities.__int__()'''
            return int()
        def __ixor__(self, f):
            '''QOpenGLDebugMessage.Severities QOpenGLDebugMessage.Severities.__ixor__(QOpenGLDebugMessage.Severities f)'''
            return QOpenGLDebugMessage.Severities()
        def __ior__(self, f):
            '''QOpenGLDebugMessage.Severities QOpenGLDebugMessage.Severities.__ior__(QOpenGLDebugMessage.Severities f)'''
            return QOpenGLDebugMessage.Severities()
        def __iand__(self, mask):
            '''QOpenGLDebugMessage.Severities QOpenGLDebugMessage.Severities.__iand__(int mask)'''
            return QOpenGLDebugMessage.Severities()
    class Types():
        """"""
        def __init__(self):
            '''QOpenGLDebugMessage.Types QOpenGLDebugMessage.Types.__init__()'''
            return QOpenGLDebugMessage.Types()
        def __init__(self):
            '''int QOpenGLDebugMessage.Types.__init__()'''
            return int()
        def __init__(self):
            '''void QOpenGLDebugMessage.Types.__init__()'''
        def __bool__(self):
            '''int QOpenGLDebugMessage.Types.__bool__()'''
            return int()
        def __ne__(self, f):
            '''bool QOpenGLDebugMessage.Types.__ne__(QOpenGLDebugMessage.Types f)'''
            return bool()
        def __eq__(self, f):
            '''bool QOpenGLDebugMessage.Types.__eq__(QOpenGLDebugMessage.Types f)'''
            return bool()
        def __invert__(self):
            '''QOpenGLDebugMessage.Types QOpenGLDebugMessage.Types.__invert__()'''
            return QOpenGLDebugMessage.Types()
        def __and__(self, mask):
            '''QOpenGLDebugMessage.Types QOpenGLDebugMessage.Types.__and__(int mask)'''
            return QOpenGLDebugMessage.Types()
        def __xor__(self, f):
            '''QOpenGLDebugMessage.Types QOpenGLDebugMessage.Types.__xor__(QOpenGLDebugMessage.Types f)'''
            return QOpenGLDebugMessage.Types()
        def __xor__(self, f):
            '''QOpenGLDebugMessage.Types QOpenGLDebugMessage.Types.__xor__(int f)'''
            return QOpenGLDebugMessage.Types()
        def __or__(self, f):
            '''QOpenGLDebugMessage.Types QOpenGLDebugMessage.Types.__or__(QOpenGLDebugMessage.Types f)'''
            return QOpenGLDebugMessage.Types()
        def __or__(self, f):
            '''QOpenGLDebugMessage.Types QOpenGLDebugMessage.Types.__or__(int f)'''
            return QOpenGLDebugMessage.Types()
        def __int__(self):
            '''int QOpenGLDebugMessage.Types.__int__()'''
            return int()
        def __ixor__(self, f):
            '''QOpenGLDebugMessage.Types QOpenGLDebugMessage.Types.__ixor__(QOpenGLDebugMessage.Types f)'''
            return QOpenGLDebugMessage.Types()
        def __ior__(self, f):
            '''QOpenGLDebugMessage.Types QOpenGLDebugMessage.Types.__ior__(QOpenGLDebugMessage.Types f)'''
            return QOpenGLDebugMessage.Types()
        def __iand__(self, mask):
            '''QOpenGLDebugMessage.Types QOpenGLDebugMessage.Types.__iand__(int mask)'''
            return QOpenGLDebugMessage.Types()


class QOpenGLDebugLogger(QObject):
    """"""
    # Enum QOpenGLDebugLogger.LoggingMode
    AsynchronousLogging = 0
    SynchronousLogging = 0

    def __init__(self, parent = None):
        '''void QOpenGLDebugLogger.__init__(QObject parent = None)'''
    messageLogged = pyqtSignal() # void messageLogged(const QOpenGLDebugMessageamp;) - signal
    def stopLogging(self):
        '''void QOpenGLDebugLogger.stopLogging()'''
    def startLogging(self, loggingMode = None):
        '''void QOpenGLDebugLogger.startLogging(QOpenGLDebugLogger.LoggingMode loggingMode = QOpenGLDebugLogger.AsynchronousLogging)'''
    def logMessage(self, debugMessage):
        '''void QOpenGLDebugLogger.logMessage(QOpenGLDebugMessage debugMessage)'''
    def loggedMessages(self):
        '''list-of-QOpenGLDebugMessage QOpenGLDebugLogger.loggedMessages()'''
        return [QOpenGLDebugMessage()]
    def disableMessages(self, sources = None, types = None, severities = None):
        '''void QOpenGLDebugLogger.disableMessages(QOpenGLDebugMessage.Sources sources = QOpenGLDebugMessage.AnySource, QOpenGLDebugMessage.Types types = QOpenGLDebugMessage.AnyType, QOpenGLDebugMessage.Severities severities = QOpenGLDebugMessage.AnySeverity)'''
    def disableMessages(self, ids, sources = None, types = None):
        '''void QOpenGLDebugLogger.disableMessages(list-of-int ids, QOpenGLDebugMessage.Sources sources = QOpenGLDebugMessage.AnySource, QOpenGLDebugMessage.Types types = QOpenGLDebugMessage.AnyType)'''
    def enableMessages(self, sources = None, types = None, severities = None):
        '''void QOpenGLDebugLogger.enableMessages(QOpenGLDebugMessage.Sources sources = QOpenGLDebugMessage.AnySource, QOpenGLDebugMessage.Types types = QOpenGLDebugMessage.AnyType, QOpenGLDebugMessage.Severities severities = QOpenGLDebugMessage.AnySeverity)'''
    def enableMessages(self, ids, sources = None, types = None):
        '''void QOpenGLDebugLogger.enableMessages(list-of-int ids, QOpenGLDebugMessage.Sources sources = QOpenGLDebugMessage.AnySource, QOpenGLDebugMessage.Types types = QOpenGLDebugMessage.AnyType)'''
    def popGroup(self):
        '''void QOpenGLDebugLogger.popGroup()'''
    def pushGroup(self, name, id = 0, source = None):
        '''void QOpenGLDebugLogger.pushGroup(str name, int id = 0, QOpenGLDebugMessage.Source source = QOpenGLDebugMessage.ApplicationSource)'''
    def maximumMessageLength(self):
        '''int QOpenGLDebugLogger.maximumMessageLength()'''
        return int()
    def loggingMode(self):
        '''QOpenGLDebugLogger.LoggingMode QOpenGLDebugLogger.loggingMode()'''
        return QOpenGLDebugLogger.LoggingMode()
    def isLogging(self):
        '''bool QOpenGLDebugLogger.isLogging()'''
        return bool()
    def initialize(self):
        '''bool QOpenGLDebugLogger.initialize()'''
        return bool()


class QOpenGLFramebufferObject():
    """"""
    # Enum QOpenGLFramebufferObject.Attachment
    NoAttachment = 0
    CombinedDepthStencil = 0
    Depth = 0

    def __init__(self, size, target = None):
        '''void QOpenGLFramebufferObject.__init__(QSize size, int target = GL_TEXTURE_2D)'''
    def __init__(self, width, height, target = None):
        '''void QOpenGLFramebufferObject.__init__(int width, int height, int target = GL_TEXTURE_2D)'''
    def __init__(self, size, attachment, target = None, internal_format = None):
        '''void QOpenGLFramebufferObject.__init__(QSize size, QOpenGLFramebufferObject.Attachment attachment, int target = GL_TEXTURE_2D, int internal_format = GL_RGBA8)'''
    def __init__(self, width, height, attachment, target = None, internal_format = None):
        '''void QOpenGLFramebufferObject.__init__(int width, int height, QOpenGLFramebufferObject.Attachment attachment, int target = GL_TEXTURE_2D, int internal_format = GL_RGBA8)'''
    def __init__(self, size, format):
        '''void QOpenGLFramebufferObject.__init__(QSize size, QOpenGLFramebufferObjectFormat format)'''
    def __init__(self, width, height, format):
        '''void QOpenGLFramebufferObject.__init__(int width, int height, QOpenGLFramebufferObjectFormat format)'''
    def takeTexture(self):
        '''int QOpenGLFramebufferObject.takeTexture()'''
        return int()
    def blitFramebuffer(self, target, targetRect, source, sourceRect, buffers = None, filter = None):
        '''static void QOpenGLFramebufferObject.blitFramebuffer(QOpenGLFramebufferObject target, QRect targetRect, QOpenGLFramebufferObject source, QRect sourceRect, int buffers = GL_COLOR_BUFFER_BIT, int filter = GL_NEAREST)'''
    def blitFramebuffer(self, target, source, buffers = None, filter = None):
        '''static void QOpenGLFramebufferObject.blitFramebuffer(QOpenGLFramebufferObject target, QOpenGLFramebufferObject source, int buffers = GL_COLOR_BUFFER_BIT, int filter = GL_NEAREST)'''
    def hasOpenGLFramebufferBlit(self):
        '''static bool QOpenGLFramebufferObject.hasOpenGLFramebufferBlit()'''
        return bool()
    def hasOpenGLFramebufferObjects(self):
        '''static bool QOpenGLFramebufferObject.hasOpenGLFramebufferObjects()'''
        return bool()
    def bindDefault(self):
        '''static bool QOpenGLFramebufferObject.bindDefault()'''
        return bool()
    def handle(self):
        '''int QOpenGLFramebufferObject.handle()'''
        return int()
    def setAttachment(self, attachment):
        '''void QOpenGLFramebufferObject.setAttachment(QOpenGLFramebufferObject.Attachment attachment)'''
    def attachment(self):
        '''QOpenGLFramebufferObject.Attachment QOpenGLFramebufferObject.attachment()'''
        return QOpenGLFramebufferObject.Attachment()
    def toImage(self):
        '''QImage QOpenGLFramebufferObject.toImage()'''
        return QImage()
    def toImage(self, flipped):
        '''QImage QOpenGLFramebufferObject.toImage(bool flipped)'''
        return QImage()
    def size(self):
        '''QSize QOpenGLFramebufferObject.size()'''
        return QSize()
    def texture(self):
        '''int QOpenGLFramebufferObject.texture()'''
        return int()
    def height(self):
        '''int QOpenGLFramebufferObject.height()'''
        return int()
    def width(self):
        '''int QOpenGLFramebufferObject.width()'''
        return int()
    def release(self):
        '''bool QOpenGLFramebufferObject.release()'''
        return bool()
    def bind(self):
        '''bool QOpenGLFramebufferObject.bind()'''
        return bool()
    def isBound(self):
        '''bool QOpenGLFramebufferObject.isBound()'''
        return bool()
    def isValid(self):
        '''bool QOpenGLFramebufferObject.isValid()'''
        return bool()
    def format(self):
        '''QOpenGLFramebufferObjectFormat QOpenGLFramebufferObject.format()'''
        return QOpenGLFramebufferObjectFormat()


class QOpenGLFramebufferObjectFormat():
    """"""
    def __init__(self):
        '''void QOpenGLFramebufferObjectFormat.__init__()'''
    def __init__(self, other):
        '''void QOpenGLFramebufferObjectFormat.__init__(QOpenGLFramebufferObjectFormat other)'''
    def __ne__(self, other):
        '''bool QOpenGLFramebufferObjectFormat.__ne__(QOpenGLFramebufferObjectFormat other)'''
        return bool()
    def __eq__(self, other):
        '''bool QOpenGLFramebufferObjectFormat.__eq__(QOpenGLFramebufferObjectFormat other)'''
        return bool()
    def internalTextureFormat(self):
        '''int QOpenGLFramebufferObjectFormat.internalTextureFormat()'''
        return int()
    def setInternalTextureFormat(self, internalTextureFormat):
        '''void QOpenGLFramebufferObjectFormat.setInternalTextureFormat(int internalTextureFormat)'''
    def textureTarget(self):
        '''int QOpenGLFramebufferObjectFormat.textureTarget()'''
        return int()
    def setTextureTarget(self, target):
        '''void QOpenGLFramebufferObjectFormat.setTextureTarget(int target)'''
    def attachment(self):
        '''QOpenGLFramebufferObject.Attachment QOpenGLFramebufferObjectFormat.attachment()'''
        return QOpenGLFramebufferObject.Attachment()
    def setAttachment(self, attachment):
        '''void QOpenGLFramebufferObjectFormat.setAttachment(QOpenGLFramebufferObject.Attachment attachment)'''
    def mipmap(self):
        '''bool QOpenGLFramebufferObjectFormat.mipmap()'''
        return bool()
    def setMipmap(self, enabled):
        '''void QOpenGLFramebufferObjectFormat.setMipmap(bool enabled)'''
    def samples(self):
        '''int QOpenGLFramebufferObjectFormat.samples()'''
        return int()
    def setSamples(self, samples):
        '''void QOpenGLFramebufferObjectFormat.setSamples(int samples)'''


class QOpenGLPaintDevice(QPaintDevice):
    """"""
    def __init__(self):
        '''void QOpenGLPaintDevice.__init__()'''
    def __init__(self, size):
        '''void QOpenGLPaintDevice.__init__(QSize size)'''
    def __init__(self, width, height):
        '''void QOpenGLPaintDevice.__init__(int width, int height)'''
    def metric(self, metric):
        '''int QOpenGLPaintDevice.metric(QPaintDevice.PaintDeviceMetric metric)'''
        return int()
    def setDevicePixelRatio(self, devicePixelRatio):
        '''void QOpenGLPaintDevice.setDevicePixelRatio(float devicePixelRatio)'''
    def ensureActiveTarget(self):
        '''void QOpenGLPaintDevice.ensureActiveTarget()'''
    def paintFlipped(self):
        '''bool QOpenGLPaintDevice.paintFlipped()'''
        return bool()
    def setPaintFlipped(self, flipped):
        '''void QOpenGLPaintDevice.setPaintFlipped(bool flipped)'''
    def setDotsPerMeterY(self):
        '''float QOpenGLPaintDevice.setDotsPerMeterY()'''
        return float()
    def setDotsPerMeterX(self):
        '''float QOpenGLPaintDevice.setDotsPerMeterX()'''
        return float()
    def dotsPerMeterY(self):
        '''float QOpenGLPaintDevice.dotsPerMeterY()'''
        return float()
    def dotsPerMeterX(self):
        '''float QOpenGLPaintDevice.dotsPerMeterX()'''
        return float()
    def setSize(self, size):
        '''void QOpenGLPaintDevice.setSize(QSize size)'''
    def size(self):
        '''QSize QOpenGLPaintDevice.size()'''
        return QSize()
    def context(self):
        '''QOpenGLContext QOpenGLPaintDevice.context()'''
        return QOpenGLContext()
    def paintEngine(self):
        '''QPaintEngine QOpenGLPaintDevice.paintEngine()'''
        return QPaintEngine()


class QOpenGLPixelTransferOptions():
    """"""
    def __init__(self):
        '''void QOpenGLPixelTransferOptions.__init__()'''
    def __init__(self):
        '''QOpenGLPixelTransferOptions QOpenGLPixelTransferOptions.__init__()'''
        return QOpenGLPixelTransferOptions()
    def isSwapBytesEnabled(self):
        '''bool QOpenGLPixelTransferOptions.isSwapBytesEnabled()'''
        return bool()
    def setSwapBytesEnabled(self, swapBytes):
        '''void QOpenGLPixelTransferOptions.setSwapBytesEnabled(bool swapBytes)'''
    def isLeastSignificantBitFirst(self):
        '''bool QOpenGLPixelTransferOptions.isLeastSignificantBitFirst()'''
        return bool()
    def setLeastSignificantByteFirst(self, lsbFirst):
        '''void QOpenGLPixelTransferOptions.setLeastSignificantByteFirst(bool lsbFirst)'''
    def rowLength(self):
        '''int QOpenGLPixelTransferOptions.rowLength()'''
        return int()
    def setRowLength(self, rowLength):
        '''void QOpenGLPixelTransferOptions.setRowLength(int rowLength)'''
    def imageHeight(self):
        '''int QOpenGLPixelTransferOptions.imageHeight()'''
        return int()
    def setImageHeight(self, imageHeight):
        '''void QOpenGLPixelTransferOptions.setImageHeight(int imageHeight)'''
    def skipPixels(self):
        '''int QOpenGLPixelTransferOptions.skipPixels()'''
        return int()
    def setSkipPixels(self, skipPixels):
        '''void QOpenGLPixelTransferOptions.setSkipPixels(int skipPixels)'''
    def skipRows(self):
        '''int QOpenGLPixelTransferOptions.skipRows()'''
        return int()
    def setSkipRows(self, skipRows):
        '''void QOpenGLPixelTransferOptions.setSkipRows(int skipRows)'''
    def skipImages(self):
        '''int QOpenGLPixelTransferOptions.skipImages()'''
        return int()
    def setSkipImages(self, skipImages):
        '''void QOpenGLPixelTransferOptions.setSkipImages(int skipImages)'''
    def alignment(self):
        '''int QOpenGLPixelTransferOptions.alignment()'''
        return int()
    def setAlignment(self, alignment):
        '''void QOpenGLPixelTransferOptions.setAlignment(int alignment)'''
    def swap(self, other):
        '''void QOpenGLPixelTransferOptions.swap(QOpenGLPixelTransferOptions other)'''


class QOpenGLShader(QObject):
    """"""
    # Enum QOpenGLShader.ShaderTypeBit
    Vertex = 0
    Fragment = 0
    Geometry = 0
    TessellationControl = 0
    TessellationEvaluation = 0
    Compute = 0

    def __init__(self, type, parent = None):
        '''void QOpenGLShader.__init__(QOpenGLShader.ShaderType type, QObject parent = None)'''
    def hasOpenGLShaders(self, type, context = None):
        '''static bool QOpenGLShader.hasOpenGLShaders(QOpenGLShader.ShaderType type, QOpenGLContext context = None)'''
        return bool()
    def shaderId(self):
        '''int QOpenGLShader.shaderId()'''
        return int()
    def log(self):
        '''str QOpenGLShader.log()'''
        return str()
    def isCompiled(self):
        '''bool QOpenGLShader.isCompiled()'''
        return bool()
    def sourceCode(self):
        '''QByteArray QOpenGLShader.sourceCode()'''
        return QByteArray()
    def compileSourceFile(self, fileName):
        '''bool QOpenGLShader.compileSourceFile(str fileName)'''
        return bool()
    def compileSourceCode(self, source):
        '''bool QOpenGLShader.compileSourceCode(QByteArray source)'''
        return bool()
    def compileSourceCode(self, source):
        '''bool QOpenGLShader.compileSourceCode(str source)'''
        return bool()
    def shaderType(self):
        '''QOpenGLShader.ShaderType QOpenGLShader.shaderType()'''
        return QOpenGLShader.ShaderType()
    class ShaderType():
        """"""
        def __init__(self):
            '''QOpenGLShader.ShaderType QOpenGLShader.ShaderType.__init__()'''
            return QOpenGLShader.ShaderType()
        def __init__(self):
            '''int QOpenGLShader.ShaderType.__init__()'''
            return int()
        def __init__(self):
            '''void QOpenGLShader.ShaderType.__init__()'''
        def __bool__(self):
            '''int QOpenGLShader.ShaderType.__bool__()'''
            return int()
        def __ne__(self, f):
            '''bool QOpenGLShader.ShaderType.__ne__(QOpenGLShader.ShaderType f)'''
            return bool()
        def __eq__(self, f):
            '''bool QOpenGLShader.ShaderType.__eq__(QOpenGLShader.ShaderType f)'''
            return bool()
        def __invert__(self):
            '''QOpenGLShader.ShaderType QOpenGLShader.ShaderType.__invert__()'''
            return QOpenGLShader.ShaderType()
        def __and__(self, mask):
            '''QOpenGLShader.ShaderType QOpenGLShader.ShaderType.__and__(int mask)'''
            return QOpenGLShader.ShaderType()
        def __xor__(self, f):
            '''QOpenGLShader.ShaderType QOpenGLShader.ShaderType.__xor__(QOpenGLShader.ShaderType f)'''
            return QOpenGLShader.ShaderType()
        def __xor__(self, f):
            '''QOpenGLShader.ShaderType QOpenGLShader.ShaderType.__xor__(int f)'''
            return QOpenGLShader.ShaderType()
        def __or__(self, f):
            '''QOpenGLShader.ShaderType QOpenGLShader.ShaderType.__or__(QOpenGLShader.ShaderType f)'''
            return QOpenGLShader.ShaderType()
        def __or__(self, f):
            '''QOpenGLShader.ShaderType QOpenGLShader.ShaderType.__or__(int f)'''
            return QOpenGLShader.ShaderType()
        def __int__(self):
            '''int QOpenGLShader.ShaderType.__int__()'''
            return int()
        def __ixor__(self, f):
            '''QOpenGLShader.ShaderType QOpenGLShader.ShaderType.__ixor__(QOpenGLShader.ShaderType f)'''
            return QOpenGLShader.ShaderType()
        def __ior__(self, f):
            '''QOpenGLShader.ShaderType QOpenGLShader.ShaderType.__ior__(QOpenGLShader.ShaderType f)'''
            return QOpenGLShader.ShaderType()
        def __iand__(self, mask):
            '''QOpenGLShader.ShaderType QOpenGLShader.ShaderType.__iand__(int mask)'''
            return QOpenGLShader.ShaderType()


class QOpenGLShaderProgram(QObject):
    """"""
    def __init__(self, parent = None):
        '''void QOpenGLShaderProgram.__init__(QObject parent = None)'''
    def create(self):
        '''bool QOpenGLShaderProgram.create()'''
        return bool()
    def defaultInnerTessellationLevels(self):
        '''list-of-float QOpenGLShaderProgram.defaultInnerTessellationLevels()'''
        return [float()]
    def setDefaultInnerTessellationLevels(self, levels):
        '''void QOpenGLShaderProgram.setDefaultInnerTessellationLevels(list-of-float levels)'''
    def defaultOuterTessellationLevels(self):
        '''list-of-float QOpenGLShaderProgram.defaultOuterTessellationLevels()'''
        return [float()]
    def setDefaultOuterTessellationLevels(self, levels):
        '''void QOpenGLShaderProgram.setDefaultOuterTessellationLevels(list-of-float levels)'''
    def patchVertexCount(self):
        '''int QOpenGLShaderProgram.patchVertexCount()'''
        return int()
    def setPatchVertexCount(self, count):
        '''void QOpenGLShaderProgram.setPatchVertexCount(int count)'''
    def maxGeometryOutputVertices(self):
        '''int QOpenGLShaderProgram.maxGeometryOutputVertices()'''
        return int()
    def hasOpenGLShaderPrograms(self, context = None):
        '''static bool QOpenGLShaderProgram.hasOpenGLShaderPrograms(QOpenGLContext context = None)'''
        return bool()
    def setUniformValueArray(self, location, values):
        '''void QOpenGLShaderProgram.setUniformValueArray(int location, sequence values)'''
    def setUniformValueArray(self, name, values):
        '''void QOpenGLShaderProgram.setUniformValueArray(str name, sequence values)'''
    def setUniformValue(self, location, value):
        '''void QOpenGLShaderProgram.setUniformValue(int location, int value)'''
    def setUniformValue(self, location, value):
        '''void QOpenGLShaderProgram.setUniformValue(int location, float value)'''
    def setUniformValue(self, location, x, y):
        '''void QOpenGLShaderProgram.setUniformValue(int location, float x, float y)'''
    def setUniformValue(self, location, x, y, z):
        '''void QOpenGLShaderProgram.setUniformValue(int location, float x, float y, float z)'''
    def setUniformValue(self, location, x, y, z, w):
        '''void QOpenGLShaderProgram.setUniformValue(int location, float x, float y, float z, float w)'''
    def setUniformValue(self, location, value):
        '''void QOpenGLShaderProgram.setUniformValue(int location, QVector2D value)'''
    def setUniformValue(self, location, value):
        '''void QOpenGLShaderProgram.setUniformValue(int location, QVector3D value)'''
    def setUniformValue(self, location, value):
        '''void QOpenGLShaderProgram.setUniformValue(int location, QVector4D value)'''
    def setUniformValue(self, location, color):
        '''void QOpenGLShaderProgram.setUniformValue(int location, QColor color)'''
    def setUniformValue(self, location, point):
        '''void QOpenGLShaderProgram.setUniformValue(int location, QPoint point)'''
    def setUniformValue(self, location, point):
        '''void QOpenGLShaderProgram.setUniformValue(int location, QPointF point)'''
    def setUniformValue(self, location, size):
        '''void QOpenGLShaderProgram.setUniformValue(int location, QSize size)'''
    def setUniformValue(self, location, size):
        '''void QOpenGLShaderProgram.setUniformValue(int location, QSizeF size)'''
    def setUniformValue(self, location, value):
        '''void QOpenGLShaderProgram.setUniformValue(int location, QMatrix2x2 value)'''
    def setUniformValue(self, location, value):
        '''void QOpenGLShaderProgram.setUniformValue(int location, QMatrix2x3 value)'''
    def setUniformValue(self, location, value):
        '''void QOpenGLShaderProgram.setUniformValue(int location, QMatrix2x4 value)'''
    def setUniformValue(self, location, value):
        '''void QOpenGLShaderProgram.setUniformValue(int location, QMatrix3x2 value)'''
    def setUniformValue(self, location, value):
        '''void QOpenGLShaderProgram.setUniformValue(int location, QMatrix3x3 value)'''
    def setUniformValue(self, location, value):
        '''void QOpenGLShaderProgram.setUniformValue(int location, QMatrix3x4 value)'''
    def setUniformValue(self, location, value):
        '''void QOpenGLShaderProgram.setUniformValue(int location, QMatrix4x2 value)'''
    def setUniformValue(self, location, value):
        '''void QOpenGLShaderProgram.setUniformValue(int location, QMatrix4x3 value)'''
    def setUniformValue(self, location, value):
        '''void QOpenGLShaderProgram.setUniformValue(int location, QMatrix4x4 value)'''
    def setUniformValue(self, location, value):
        '''void QOpenGLShaderProgram.setUniformValue(int location, QTransform value)'''
    def setUniformValue(self, name, value):
        '''void QOpenGLShaderProgram.setUniformValue(str name, int value)'''
    def setUniformValue(self, name, value):
        '''void QOpenGLShaderProgram.setUniformValue(str name, float value)'''
    def setUniformValue(self, name, x, y):
        '''void QOpenGLShaderProgram.setUniformValue(str name, float x, float y)'''
    def setUniformValue(self, name, x, y, z):
        '''void QOpenGLShaderProgram.setUniformValue(str name, float x, float y, float z)'''
    def setUniformValue(self, name, x, y, z, w):
        '''void QOpenGLShaderProgram.setUniformValue(str name, float x, float y, float z, float w)'''
    def setUniformValue(self, name, value):
        '''void QOpenGLShaderProgram.setUniformValue(str name, QVector2D value)'''
    def setUniformValue(self, name, value):
        '''void QOpenGLShaderProgram.setUniformValue(str name, QVector3D value)'''
    def setUniformValue(self, name, value):
        '''void QOpenGLShaderProgram.setUniformValue(str name, QVector4D value)'''
    def setUniformValue(self, name, color):
        '''void QOpenGLShaderProgram.setUniformValue(str name, QColor color)'''
    def setUniformValue(self, name, point):
        '''void QOpenGLShaderProgram.setUniformValue(str name, QPoint point)'''
    def setUniformValue(self, name, point):
        '''void QOpenGLShaderProgram.setUniformValue(str name, QPointF point)'''
    def setUniformValue(self, name, size):
        '''void QOpenGLShaderProgram.setUniformValue(str name, QSize size)'''
    def setUniformValue(self, name, size):
        '''void QOpenGLShaderProgram.setUniformValue(str name, QSizeF size)'''
    def setUniformValue(self, name, value):
        '''void QOpenGLShaderProgram.setUniformValue(str name, QMatrix2x2 value)'''
    def setUniformValue(self, name, value):
        '''void QOpenGLShaderProgram.setUniformValue(str name, QMatrix2x3 value)'''
    def setUniformValue(self, name, value):
        '''void QOpenGLShaderProgram.setUniformValue(str name, QMatrix2x4 value)'''
    def setUniformValue(self, name, value):
        '''void QOpenGLShaderProgram.setUniformValue(str name, QMatrix3x2 value)'''
    def setUniformValue(self, name, value):
        '''void QOpenGLShaderProgram.setUniformValue(str name, QMatrix3x3 value)'''
    def setUniformValue(self, name, value):
        '''void QOpenGLShaderProgram.setUniformValue(str name, QMatrix3x4 value)'''
    def setUniformValue(self, name, value):
        '''void QOpenGLShaderProgram.setUniformValue(str name, QMatrix4x2 value)'''
    def setUniformValue(self, name, value):
        '''void QOpenGLShaderProgram.setUniformValue(str name, QMatrix4x3 value)'''
    def setUniformValue(self, name, value):
        '''void QOpenGLShaderProgram.setUniformValue(str name, QMatrix4x4 value)'''
    def setUniformValue(self, name, value):
        '''void QOpenGLShaderProgram.setUniformValue(str name, QTransform value)'''
    def uniformLocation(self, name):
        '''int QOpenGLShaderProgram.uniformLocation(QByteArray name)'''
        return int()
    def uniformLocation(self, name):
        '''int QOpenGLShaderProgram.uniformLocation(str name)'''
        return int()
    def disableAttributeArray(self, location):
        '''void QOpenGLShaderProgram.disableAttributeArray(int location)'''
    def disableAttributeArray(self, name):
        '''void QOpenGLShaderProgram.disableAttributeArray(str name)'''
    def enableAttributeArray(self, location):
        '''void QOpenGLShaderProgram.enableAttributeArray(int location)'''
    def enableAttributeArray(self, name):
        '''void QOpenGLShaderProgram.enableAttributeArray(str name)'''
    def setAttributeBuffer(self, location, type, offset, tupleSize, stride = 0):
        '''void QOpenGLShaderProgram.setAttributeBuffer(int location, int type, int offset, int tupleSize, int stride = 0)'''
    def setAttributeBuffer(self, name, type, offset, tupleSize, stride = 0):
        '''void QOpenGLShaderProgram.setAttributeBuffer(str name, int type, int offset, int tupleSize, int stride = 0)'''
    def setAttributeArray(self, location, values):
        '''void QOpenGLShaderProgram.setAttributeArray(int location, sequence values)'''
    def setAttributeArray(self, name, values):
        '''void QOpenGLShaderProgram.setAttributeArray(str name, sequence values)'''
    def setAttributeValue(self, location, value):
        '''void QOpenGLShaderProgram.setAttributeValue(int location, float value)'''
    def setAttributeValue(self, location, x, y):
        '''void QOpenGLShaderProgram.setAttributeValue(int location, float x, float y)'''
    def setAttributeValue(self, location, x, y, z):
        '''void QOpenGLShaderProgram.setAttributeValue(int location, float x, float y, float z)'''
    def setAttributeValue(self, location, x, y, z, w):
        '''void QOpenGLShaderProgram.setAttributeValue(int location, float x, float y, float z, float w)'''
    def setAttributeValue(self, location, value):
        '''void QOpenGLShaderProgram.setAttributeValue(int location, QVector2D value)'''
    def setAttributeValue(self, location, value):
        '''void QOpenGLShaderProgram.setAttributeValue(int location, QVector3D value)'''
    def setAttributeValue(self, location, value):
        '''void QOpenGLShaderProgram.setAttributeValue(int location, QVector4D value)'''
    def setAttributeValue(self, location, value):
        '''void QOpenGLShaderProgram.setAttributeValue(int location, QColor value)'''
    def setAttributeValue(self, name, value):
        '''void QOpenGLShaderProgram.setAttributeValue(str name, float value)'''
    def setAttributeValue(self, name, x, y):
        '''void QOpenGLShaderProgram.setAttributeValue(str name, float x, float y)'''
    def setAttributeValue(self, name, x, y, z):
        '''void QOpenGLShaderProgram.setAttributeValue(str name, float x, float y, float z)'''
    def setAttributeValue(self, name, x, y, z, w):
        '''void QOpenGLShaderProgram.setAttributeValue(str name, float x, float y, float z, float w)'''
    def setAttributeValue(self, name, value):
        '''void QOpenGLShaderProgram.setAttributeValue(str name, QVector2D value)'''
    def setAttributeValue(self, name, value):
        '''void QOpenGLShaderProgram.setAttributeValue(str name, QVector3D value)'''
    def setAttributeValue(self, name, value):
        '''void QOpenGLShaderProgram.setAttributeValue(str name, QVector4D value)'''
    def setAttributeValue(self, name, value):
        '''void QOpenGLShaderProgram.setAttributeValue(str name, QColor value)'''
    def attributeLocation(self, name):
        '''int QOpenGLShaderProgram.attributeLocation(QByteArray name)'''
        return int()
    def attributeLocation(self, name):
        '''int QOpenGLShaderProgram.attributeLocation(str name)'''
        return int()
    def bindAttributeLocation(self, name, location):
        '''void QOpenGLShaderProgram.bindAttributeLocation(QByteArray name, int location)'''
    def bindAttributeLocation(self, name, location):
        '''void QOpenGLShaderProgram.bindAttributeLocation(str name, int location)'''
    def programId(self):
        '''int QOpenGLShaderProgram.programId()'''
        return int()
    def release(self):
        '''void QOpenGLShaderProgram.release()'''
    def bind(self):
        '''bool QOpenGLShaderProgram.bind()'''
        return bool()
    def log(self):
        '''str QOpenGLShaderProgram.log()'''
        return str()
    def isLinked(self):
        '''bool QOpenGLShaderProgram.isLinked()'''
        return bool()
    def link(self):
        '''bool QOpenGLShaderProgram.link()'''
        return bool()
    def removeAllShaders(self):
        '''void QOpenGLShaderProgram.removeAllShaders()'''
    def addShaderFromSourceFile(self, type, fileName):
        '''bool QOpenGLShaderProgram.addShaderFromSourceFile(QOpenGLShader.ShaderType type, str fileName)'''
        return bool()
    def addShaderFromSourceCode(self, type, source):
        '''bool QOpenGLShaderProgram.addShaderFromSourceCode(QOpenGLShader.ShaderType type, QByteArray source)'''
        return bool()
    def addShaderFromSourceCode(self, type, source):
        '''bool QOpenGLShaderProgram.addShaderFromSourceCode(QOpenGLShader.ShaderType type, str source)'''
        return bool()
    def shaders(self):
        '''list-of-QOpenGLShader QOpenGLShaderProgram.shaders()'''
        return [QOpenGLShader()]
    def removeShader(self, shader):
        '''void QOpenGLShaderProgram.removeShader(QOpenGLShader shader)'''
    def addShader(self, shader):
        '''bool QOpenGLShaderProgram.addShader(QOpenGLShader shader)'''
        return bool()


class QOpenGLTexture():
    """"""
    # Enum QOpenGLTexture.ComparisonMode
    CompareRefToTexture = 0
    CompareNone = 0

    # Enum QOpenGLTexture.ComparisonFunction
    CompareLessEqual = 0
    CompareGreaterEqual = 0
    CompareLess = 0
    CompareGreater = 0
    CompareEqual = 0
    CommpareNotEqual = 0
    CompareAlways = 0
    CompareNever = 0

    # Enum QOpenGLTexture.CoordinateDirection
    DirectionS = 0
    DirectionT = 0
    DirectionR = 0

    # Enum QOpenGLTexture.WrapMode
    Repeat = 0
    MirroredRepeat = 0
    ClampToEdge = 0
    ClampToBorder = 0

    # Enum QOpenGLTexture.Filter
    Nearest = 0
    Linear = 0
    NearestMipMapNearest = 0
    NearestMipMapLinear = 0
    LinearMipMapNearest = 0
    LinearMipMapLinear = 0

    # Enum QOpenGLTexture.DepthStencilMode
    DepthMode = 0
    StencilMode = 0

    # Enum QOpenGLTexture.SwizzleValue
    RedValue = 0
    GreenValue = 0
    BlueValue = 0
    AlphaValue = 0
    ZeroValue = 0
    OneValue = 0

    # Enum QOpenGLTexture.SwizzleComponent
    SwizzleRed = 0
    SwizzleGreen = 0
    SwizzleBlue = 0
    SwizzleAlpha = 0

    # Enum QOpenGLTexture.Feature
    ImmutableStorage = 0
    ImmutableMultisampleStorage = 0
    TextureRectangle = 0
    TextureArrays = 0
    Texture3D = 0
    TextureMultisample = 0
    TextureBuffer = 0
    TextureCubeMapArrays = 0
    Swizzle = 0
    StencilTexturing = 0
    AnisotropicFiltering = 0
    NPOTTextures = 0
    NPOTTextureRepeat = 0
    Texture1D = 0
    TextureComparisonOperators = 0
    TextureMipMapLevel = 0

    # Enum QOpenGLTexture.PixelType
    NoPixelType = 0
    Int8 = 0
    UInt8 = 0
    Int16 = 0
    UInt16 = 0
    Int32 = 0
    UInt32 = 0
    Float16 = 0
    Float16OES = 0
    Float32 = 0
    UInt32_RGB9_E5 = 0
    UInt32_RG11B10F = 0
    UInt8_RG3B2 = 0
    UInt8_RG3B2_Rev = 0
    UInt16_RGB5A1 = 0
    UInt16_RGB5A1_Rev = 0
    UInt16_R5G6B5 = 0
    UInt16_R5G6B5_Rev = 0
    UInt16_RGBA4 = 0
    UInt16_RGBA4_Rev = 0
    UInt32_RGB10A2 = 0
    UInt32_RGB10A2_Rev = 0
    UInt32_RGBA8 = 0
    UInt32_RGBA8_Rev = 0
    UInt32_D24S8 = 0
    Float32_D32_UInt32_S8_X24 = 0

    # Enum QOpenGLTexture.PixelFormat
    NoSourceFormat = 0
    Red = 0
    RG = 0
    RGB = 0
    BGR = 0
    RGBA = 0
    BGRA = 0
    Red_Integer = 0
    RG_Integer = 0
    RGB_Integer = 0
    BGR_Integer = 0
    RGBA_Integer = 0
    BGRA_Integer = 0
    Depth = 0
    DepthStencil = 0
    Alpha = 0
    Luminance = 0
    LuminanceAlpha = 0
    Stencil = 0

    # Enum QOpenGLTexture.CubeMapFace
    CubeMapPositiveX = 0
    CubeMapNegativeX = 0
    CubeMapPositiveY = 0
    CubeMapNegativeY = 0
    CubeMapPositiveZ = 0
    CubeMapNegativeZ = 0

    # Enum QOpenGLTexture.TextureFormat
    NoFormat = 0
    R8_UNorm = 0
    RG8_UNorm = 0
    RGB8_UNorm = 0
    RGBA8_UNorm = 0
    R16_UNorm = 0
    RG16_UNorm = 0
    RGB16_UNorm = 0
    RGBA16_UNorm = 0
    R8_SNorm = 0
    RG8_SNorm = 0
    RGB8_SNorm = 0
    RGBA8_SNorm = 0
    R16_SNorm = 0
    RG16_SNorm = 0
    RGB16_SNorm = 0
    RGBA16_SNorm = 0
    R8U = 0
    RG8U = 0
    RGB8U = 0
    RGBA8U = 0
    R16U = 0
    RG16U = 0
    RGB16U = 0
    RGBA16U = 0
    R32U = 0
    RG32U = 0
    RGB32U = 0
    RGBA32U = 0
    R8I = 0
    RG8I = 0
    RGB8I = 0
    RGBA8I = 0
    R16I = 0
    RG16I = 0
    RGB16I = 0
    RGBA16I = 0
    R32I = 0
    RG32I = 0
    RGB32I = 0
    RGBA32I = 0
    R16F = 0
    RG16F = 0
    RGB16F = 0
    RGBA16F = 0
    R32F = 0
    RG32F = 0
    RGB32F = 0
    RGBA32F = 0
    RGB9E5 = 0
    RG11B10F = 0
    RG3B2 = 0
    R5G6B5 = 0
    RGB5A1 = 0
    RGBA4 = 0
    RGB10A2 = 0
    D16 = 0
    D24 = 0
    D24S8 = 0
    D32 = 0
    D32F = 0
    D32FS8X24 = 0
    RGB_DXT1 = 0
    RGBA_DXT1 = 0
    RGBA_DXT3 = 0
    RGBA_DXT5 = 0
    R_ATI1N_UNorm = 0
    R_ATI1N_SNorm = 0
    RG_ATI2N_UNorm = 0
    RG_ATI2N_SNorm = 0
    RGB_BP_UNSIGNED_FLOAT = 0
    RGB_BP_SIGNED_FLOAT = 0
    RGB_BP_UNorm = 0
    SRGB8 = 0
    SRGB8_Alpha8 = 0
    SRGB_DXT1 = 0
    SRGB_Alpha_DXT1 = 0
    SRGB_Alpha_DXT3 = 0
    SRGB_Alpha_DXT5 = 0
    SRGB_BP_UNorm = 0
    DepthFormat = 0
    AlphaFormat = 0
    RGBFormat = 0
    RGBAFormat = 0
    LuminanceFormat = 0
    LuminanceAlphaFormat = 0
    S8 = 0
    R11_EAC_UNorm = 0
    R11_EAC_SNorm = 0
    RG11_EAC_UNorm = 0
    RG11_EAC_SNorm = 0
    RGB8_ETC2 = 0
    SRGB8_ETC2 = 0
    RGB8_PunchThrough_Alpha1_ETC2 = 0
    SRGB8_PunchThrough_Alpha1_ETC2 = 0
    RGBA8_ETC2_EAC = 0
    SRGB8_Alpha8_ETC2_EAC = 0

    # Enum QOpenGLTexture.TextureUnitReset
    ResetTextureUnit = 0
    DontResetTextureUnit = 0

    # Enum QOpenGLTexture.MipMapGeneration
    GenerateMipMaps = 0
    DontGenerateMipMaps = 0

    # Enum QOpenGLTexture.BindingTarget
    BindingTarget1D = 0
    BindingTarget1DArray = 0
    BindingTarget2D = 0
    BindingTarget2DArray = 0
    BindingTarget3D = 0
    BindingTargetCubeMap = 0
    BindingTargetCubeMapArray = 0
    BindingTarget2DMultisample = 0
    BindingTarget2DMultisampleArray = 0
    BindingTargetRectangle = 0
    BindingTargetBuffer = 0

    # Enum QOpenGLTexture.Target
    Target1D = 0
    Target1DArray = 0
    Target2D = 0
    Target2DArray = 0
    Target3D = 0
    TargetCubeMap = 0
    TargetCubeMapArray = 0
    Target2DMultisample = 0
    Target2DMultisampleArray = 0
    TargetRectangle = 0
    TargetBuffer = 0

    def __init__(self, target):
        '''void QOpenGLTexture.__init__(QOpenGLTexture.Target target)'''
    def __init__(self, image, genMipMaps = None):
        '''void QOpenGLTexture.__init__(QImage image, QOpenGLTexture.MipMapGeneration genMipMaps = QOpenGLTexture.GenerateMipMaps)'''
    def comparisonMode(self):
        '''QOpenGLTexture.ComparisonMode QOpenGLTexture.comparisonMode()'''
        return QOpenGLTexture.ComparisonMode()
    def setComparisonMode(self, mode):
        '''void QOpenGLTexture.setComparisonMode(QOpenGLTexture.ComparisonMode mode)'''
    def comparisonFunction(self):
        '''QOpenGLTexture.ComparisonFunction QOpenGLTexture.comparisonFunction()'''
        return QOpenGLTexture.ComparisonFunction()
    def setComparisonFunction(self, function):
        '''void QOpenGLTexture.setComparisonFunction(QOpenGLTexture.ComparisonFunction function)'''
    def isFixedSamplePositions(self):
        '''bool QOpenGLTexture.isFixedSamplePositions()'''
        return bool()
    def setFixedSamplePositions(self, fixed):
        '''void QOpenGLTexture.setFixedSamplePositions(bool fixed)'''
    def samples(self):
        '''int QOpenGLTexture.samples()'''
        return int()
    def setSamples(self, samples):
        '''void QOpenGLTexture.setSamples(int samples)'''
    def target(self):
        '''QOpenGLTexture.Target QOpenGLTexture.target()'''
        return QOpenGLTexture.Target()
    def levelofDetailBias(self):
        '''float QOpenGLTexture.levelofDetailBias()'''
        return float()
    def setLevelofDetailBias(self, bias):
        '''void QOpenGLTexture.setLevelofDetailBias(float bias)'''
    def levelOfDetailRange(self):
        '''tuple-of-float-float QOpenGLTexture.levelOfDetailRange()'''
        return tuple-of-float-float()
    def setLevelOfDetailRange(self, min, max):
        '''void QOpenGLTexture.setLevelOfDetailRange(float min, float max)'''
    def maximumLevelOfDetail(self):
        '''float QOpenGLTexture.maximumLevelOfDetail()'''
        return float()
    def setMaximumLevelOfDetail(self, value):
        '''void QOpenGLTexture.setMaximumLevelOfDetail(float value)'''
    def minimumLevelOfDetail(self):
        '''float QOpenGLTexture.minimumLevelOfDetail()'''
        return float()
    def setMinimumLevelOfDetail(self, value):
        '''void QOpenGLTexture.setMinimumLevelOfDetail(float value)'''
    def borderColor(self):
        '''QColor QOpenGLTexture.borderColor()'''
        return QColor()
    def setBorderColor(self, color):
        '''void QOpenGLTexture.setBorderColor(QColor color)'''
    def wrapMode(self, direction):
        '''QOpenGLTexture.WrapMode QOpenGLTexture.wrapMode(QOpenGLTexture.CoordinateDirection direction)'''
        return QOpenGLTexture.WrapMode()
    def setWrapMode(self, mode):
        '''void QOpenGLTexture.setWrapMode(QOpenGLTexture.WrapMode mode)'''
    def setWrapMode(self, direction, mode):
        '''void QOpenGLTexture.setWrapMode(QOpenGLTexture.CoordinateDirection direction, QOpenGLTexture.WrapMode mode)'''
    def maximumAnisotropy(self):
        '''float QOpenGLTexture.maximumAnisotropy()'''
        return float()
    def setMaximumAnisotropy(self, anisotropy):
        '''void QOpenGLTexture.setMaximumAnisotropy(float anisotropy)'''
    def minMagFilters(self):
        '''tuple-of-QOpenGLTexture.Filter-QOpenGLTexture.Filter QOpenGLTexture.minMagFilters()'''
        return tuple-of-QOpenGLTexture.Filter-QOpenGLTexture.Filter()
    def setMinMagFilters(self, minificationFilter, magnificationFilter):
        '''void QOpenGLTexture.setMinMagFilters(QOpenGLTexture.Filter minificationFilter, QOpenGLTexture.Filter magnificationFilter)'''
    def magnificationFilter(self):
        '''QOpenGLTexture.Filter QOpenGLTexture.magnificationFilter()'''
        return QOpenGLTexture.Filter()
    def setMagnificationFilter(self, filter):
        '''void QOpenGLTexture.setMagnificationFilter(QOpenGLTexture.Filter filter)'''
    def minificationFilter(self):
        '''QOpenGLTexture.Filter QOpenGLTexture.minificationFilter()'''
        return QOpenGLTexture.Filter()
    def setMinificationFilter(self, filter):
        '''void QOpenGLTexture.setMinificationFilter(QOpenGLTexture.Filter filter)'''
    def depthStencilMode(self):
        '''QOpenGLTexture.DepthStencilMode QOpenGLTexture.depthStencilMode()'''
        return QOpenGLTexture.DepthStencilMode()
    def setDepthStencilMode(self, mode):
        '''void QOpenGLTexture.setDepthStencilMode(QOpenGLTexture.DepthStencilMode mode)'''
    def swizzleMask(self, component):
        '''QOpenGLTexture.SwizzleValue QOpenGLTexture.swizzleMask(QOpenGLTexture.SwizzleComponent component)'''
        return QOpenGLTexture.SwizzleValue()
    def setSwizzleMask(self, component, value):
        '''void QOpenGLTexture.setSwizzleMask(QOpenGLTexture.SwizzleComponent component, QOpenGLTexture.SwizzleValue value)'''
    def setSwizzleMask(self, r, g, b, a):
        '''void QOpenGLTexture.setSwizzleMask(QOpenGLTexture.SwizzleValue r, QOpenGLTexture.SwizzleValue g, QOpenGLTexture.SwizzleValue b, QOpenGLTexture.SwizzleValue a)'''
    def generateMipMaps(self):
        '''void QOpenGLTexture.generateMipMaps()'''
    def generateMipMaps(self, baseLevel, resetBaseLevel = True):
        '''void QOpenGLTexture.generateMipMaps(int baseLevel, bool resetBaseLevel = True)'''
    def isAutoMipMapGenerationEnabled(self):
        '''bool QOpenGLTexture.isAutoMipMapGenerationEnabled()'''
        return bool()
    def setAutoMipMapGenerationEnabled(self, enabled):
        '''void QOpenGLTexture.setAutoMipMapGenerationEnabled(bool enabled)'''
    def mipLevelRange(self):
        '''tuple-of-int-int QOpenGLTexture.mipLevelRange()'''
        return tuple-of-int-int()
    def setMipLevelRange(self, baseLevel, maxLevel):
        '''void QOpenGLTexture.setMipLevelRange(int baseLevel, int maxLevel)'''
    def mipMaxLevel(self):
        '''int QOpenGLTexture.mipMaxLevel()'''
        return int()
    def setMipMaxLevel(self, maxLevel):
        '''void QOpenGLTexture.setMipMaxLevel(int maxLevel)'''
    def mipBaseLevel(self):
        '''int QOpenGLTexture.mipBaseLevel()'''
        return int()
    def setMipBaseLevel(self, baseLevel):
        '''void QOpenGLTexture.setMipBaseLevel(int baseLevel)'''
    def hasFeature(self, feature):
        '''static bool QOpenGLTexture.hasFeature(QOpenGLTexture.Feature feature)'''
        return bool()
    def setCompressedData(self, mipLevel, layer, cubeFace, dataSize, data, options = None):
        '''void QOpenGLTexture.setCompressedData(int mipLevel, int layer, QOpenGLTexture.CubeMapFace cubeFace, int dataSize, sip.voidptr data, QOpenGLPixelTransferOptions options = None)'''
    def setCompressedData(self, mipLevel, layer, dataSize, data, options = None):
        '''void QOpenGLTexture.setCompressedData(int mipLevel, int layer, int dataSize, sip.voidptr data, QOpenGLPixelTransferOptions options = None)'''
    def setCompressedData(self, mipLevel, dataSize, data, options = None):
        '''void QOpenGLTexture.setCompressedData(int mipLevel, int dataSize, sip.voidptr data, QOpenGLPixelTransferOptions options = None)'''
    def setCompressedData(self, dataSize, data, options = None):
        '''void QOpenGLTexture.setCompressedData(int dataSize, sip.voidptr data, QOpenGLPixelTransferOptions options = None)'''
    def setData(self, mipLevel, layer, cubeFace, sourceFormat, sourceType, data, options = None):
        '''void QOpenGLTexture.setData(int mipLevel, int layer, QOpenGLTexture.CubeMapFace cubeFace, QOpenGLTexture.PixelFormat sourceFormat, QOpenGLTexture.PixelType sourceType, sip.voidptr data, QOpenGLPixelTransferOptions options = None)'''
    def setData(self, mipLevel, layer, sourceFormat, sourceType, data, options = None):
        '''void QOpenGLTexture.setData(int mipLevel, int layer, QOpenGLTexture.PixelFormat sourceFormat, QOpenGLTexture.PixelType sourceType, sip.voidptr data, QOpenGLPixelTransferOptions options = None)'''
    def setData(self, mipLevel, sourceFormat, sourceType, data, options = None):
        '''void QOpenGLTexture.setData(int mipLevel, QOpenGLTexture.PixelFormat sourceFormat, QOpenGLTexture.PixelType sourceType, sip.voidptr data, QOpenGLPixelTransferOptions options = None)'''
    def setData(self, sourceFormat, sourceType, data, options = None):
        '''void QOpenGLTexture.setData(QOpenGLTexture.PixelFormat sourceFormat, QOpenGLTexture.PixelType sourceType, sip.voidptr data, QOpenGLPixelTransferOptions options = None)'''
    def setData(self, image, genMipMaps = None):
        '''void QOpenGLTexture.setData(QImage image, QOpenGLTexture.MipMapGeneration genMipMaps = QOpenGLTexture.GenerateMipMaps)'''
    def isTextureView(self):
        '''bool QOpenGLTexture.isTextureView()'''
        return bool()
    def createTextureView(self, target, viewFormat, minimumMipmapLevel, maximumMipmapLevel, minimumLayer, maximumLayer):
        '''QOpenGLTexture QOpenGLTexture.createTextureView(QOpenGLTexture.Target target, QOpenGLTexture.TextureFormat viewFormat, int minimumMipmapLevel, int maximumMipmapLevel, int minimumLayer, int maximumLayer)'''
        return QOpenGLTexture()
    def isStorageAllocated(self):
        '''bool QOpenGLTexture.isStorageAllocated()'''
        return bool()
    def allocateStorage(self):
        '''void QOpenGLTexture.allocateStorage()'''
    def allocateStorage(self, pixelFormat, pixelType):
        '''void QOpenGLTexture.allocateStorage(QOpenGLTexture.PixelFormat pixelFormat, QOpenGLTexture.PixelType pixelType)'''
    def faces(self):
        '''int QOpenGLTexture.faces()'''
        return int()
    def layers(self):
        '''int QOpenGLTexture.layers()'''
        return int()
    def setLayers(self, layers):
        '''void QOpenGLTexture.setLayers(int layers)'''
    def maximumMipLevels(self):
        '''int QOpenGLTexture.maximumMipLevels()'''
        return int()
    def mipLevels(self):
        '''int QOpenGLTexture.mipLevels()'''
        return int()
    def setMipLevels(self, levels):
        '''void QOpenGLTexture.setMipLevels(int levels)'''
    def depth(self):
        '''int QOpenGLTexture.depth()'''
        return int()
    def height(self):
        '''int QOpenGLTexture.height()'''
        return int()
    def width(self):
        '''int QOpenGLTexture.width()'''
        return int()
    def setSize(self, width, height = 1, depth = 1):
        '''void QOpenGLTexture.setSize(int width, int height = 1, int depth = 1)'''
    def format(self):
        '''QOpenGLTexture.TextureFormat QOpenGLTexture.format()'''
        return QOpenGLTexture.TextureFormat()
    def setFormat(self, format):
        '''void QOpenGLTexture.setFormat(QOpenGLTexture.TextureFormat format)'''
    def boundTextureId(self, target):
        '''static int QOpenGLTexture.boundTextureId(QOpenGLTexture.BindingTarget target)'''
        return int()
    def boundTextureId(self, unit, target):
        '''static int QOpenGLTexture.boundTextureId(int unit, QOpenGLTexture.BindingTarget target)'''
        return int()
    def isBound(self):
        '''bool QOpenGLTexture.isBound()'''
        return bool()
    def isBound(self, unit):
        '''bool QOpenGLTexture.isBound(int unit)'''
        return bool()
    def release(self):
        '''void QOpenGLTexture.release()'''
    def release(self, unit, reset = None):
        '''void QOpenGLTexture.release(int unit, QOpenGLTexture.TextureUnitReset reset = QOpenGLTexture.DontResetTextureUnit)'''
    def bind(self):
        '''void QOpenGLTexture.bind()'''
    def bind(self, unit, reset = None):
        '''void QOpenGLTexture.bind(int unit, QOpenGLTexture.TextureUnitReset reset = QOpenGLTexture.DontResetTextureUnit)'''
    def textureId(self):
        '''int QOpenGLTexture.textureId()'''
        return int()
    def isCreated(self):
        '''bool QOpenGLTexture.isCreated()'''
        return bool()
    def destroy(self):
        '''void QOpenGLTexture.destroy()'''
    def create(self):
        '''bool QOpenGLTexture.create()'''
        return bool()
    class Features():
        """"""
        def __init__(self):
            '''QOpenGLTexture.Features QOpenGLTexture.Features.__init__()'''
            return QOpenGLTexture.Features()
        def __init__(self):
            '''int QOpenGLTexture.Features.__init__()'''
            return int()
        def __init__(self):
            '''void QOpenGLTexture.Features.__init__()'''
        def __bool__(self):
            '''int QOpenGLTexture.Features.__bool__()'''
            return int()
        def __ne__(self, f):
            '''bool QOpenGLTexture.Features.__ne__(QOpenGLTexture.Features f)'''
            return bool()
        def __eq__(self, f):
            '''bool QOpenGLTexture.Features.__eq__(QOpenGLTexture.Features f)'''
            return bool()
        def __invert__(self):
            '''QOpenGLTexture.Features QOpenGLTexture.Features.__invert__()'''
            return QOpenGLTexture.Features()
        def __and__(self, mask):
            '''QOpenGLTexture.Features QOpenGLTexture.Features.__and__(int mask)'''
            return QOpenGLTexture.Features()
        def __xor__(self, f):
            '''QOpenGLTexture.Features QOpenGLTexture.Features.__xor__(QOpenGLTexture.Features f)'''
            return QOpenGLTexture.Features()
        def __xor__(self, f):
            '''QOpenGLTexture.Features QOpenGLTexture.Features.__xor__(int f)'''
            return QOpenGLTexture.Features()
        def __or__(self, f):
            '''QOpenGLTexture.Features QOpenGLTexture.Features.__or__(QOpenGLTexture.Features f)'''
            return QOpenGLTexture.Features()
        def __or__(self, f):
            '''QOpenGLTexture.Features QOpenGLTexture.Features.__or__(int f)'''
            return QOpenGLTexture.Features()
        def __int__(self):
            '''int QOpenGLTexture.Features.__int__()'''
            return int()
        def __ixor__(self, f):
            '''QOpenGLTexture.Features QOpenGLTexture.Features.__ixor__(QOpenGLTexture.Features f)'''
            return QOpenGLTexture.Features()
        def __ior__(self, f):
            '''QOpenGLTexture.Features QOpenGLTexture.Features.__ior__(QOpenGLTexture.Features f)'''
            return QOpenGLTexture.Features()
        def __iand__(self, mask):
            '''QOpenGLTexture.Features QOpenGLTexture.Features.__iand__(int mask)'''
            return QOpenGLTexture.Features()


class QOpenGLTimerQuery(QObject):
    """"""
    def __init__(self, parent = None):
        '''void QOpenGLTimerQuery.__init__(QObject parent = None)'''
    def waitForResult(self):
        '''int QOpenGLTimerQuery.waitForResult()'''
        return int()
    def isResultAvailable(self):
        '''bool QOpenGLTimerQuery.isResultAvailable()'''
        return bool()
    def recordTimestamp(self):
        '''void QOpenGLTimerQuery.recordTimestamp()'''
    def waitForTimestamp(self):
        '''int QOpenGLTimerQuery.waitForTimestamp()'''
        return int()
    def end(self):
        '''void QOpenGLTimerQuery.end()'''
    def begin(self):
        '''void QOpenGLTimerQuery.begin()'''
    def objectId(self):
        '''int QOpenGLTimerQuery.objectId()'''
        return int()
    def isCreated(self):
        '''bool QOpenGLTimerQuery.isCreated()'''
        return bool()
    def destroy(self):
        '''void QOpenGLTimerQuery.destroy()'''
    def create(self):
        '''bool QOpenGLTimerQuery.create()'''
        return bool()


class QOpenGLTimeMonitor(QObject):
    """"""
    def __init__(self, parent = None):
        '''void QOpenGLTimeMonitor.__init__(QObject parent = None)'''
    def reset(self):
        '''void QOpenGLTimeMonitor.reset()'''
    def waitForIntervals(self):
        '''list-of-int QOpenGLTimeMonitor.waitForIntervals()'''
        return [int()]
    def waitForSamples(self):
        '''list-of-int QOpenGLTimeMonitor.waitForSamples()'''
        return [int()]
    def isResultAvailable(self):
        '''bool QOpenGLTimeMonitor.isResultAvailable()'''
        return bool()
    def recordSample(self):
        '''int QOpenGLTimeMonitor.recordSample()'''
        return int()
    def objectIds(self):
        '''list-of-int QOpenGLTimeMonitor.objectIds()'''
        return [int()]
    def isCreated(self):
        '''bool QOpenGLTimeMonitor.isCreated()'''
        return bool()
    def destroy(self):
        '''void QOpenGLTimeMonitor.destroy()'''
    def create(self):
        '''bool QOpenGLTimeMonitor.create()'''
        return bool()
    def sampleCount(self):
        '''int QOpenGLTimeMonitor.sampleCount()'''
        return int()
    def setSampleCount(self, sampleCount):
        '''void QOpenGLTimeMonitor.setSampleCount(int sampleCount)'''


class QAbstractOpenGLFunctions():
    """"""


class QOpenGLVertexArrayObject(QObject):
    """"""
    def __init__(self, parent = None):
        '''void QOpenGLVertexArrayObject.__init__(QObject parent = None)'''
    def release(self):
        '''void QOpenGLVertexArrayObject.release()'''
    def bind(self):
        '''void QOpenGLVertexArrayObject.bind()'''
    def objectId(self):
        '''int QOpenGLVertexArrayObject.objectId()'''
        return int()
    def isCreated(self):
        '''bool QOpenGLVertexArrayObject.isCreated()'''
        return bool()
    def destroy(self):
        '''void QOpenGLVertexArrayObject.destroy()'''
    def create(self):
        '''bool QOpenGLVertexArrayObject.create()'''
        return bool()
    class Binder():
        """"""
        def __init__(self, v):
            '''void QOpenGLVertexArrayObject.Binder.__init__(QOpenGLVertexArrayObject v)'''
        def __exit__(self, type, value, traceback):
            '''void QOpenGLVertexArrayObject.Binder.__exit__(object type, object value, object traceback)'''
        def __enter__(self):
            '''object QOpenGLVertexArrayObject.Binder.__enter__()'''
            return object()
        def rebind(self):
            '''void QOpenGLVertexArrayObject.Binder.rebind()'''
        def release(self):
            '''void QOpenGLVertexArrayObject.Binder.release()'''


class QWindow(QObject, QSurface):
    """"""
    # Enum QWindow.Visibility
    Hidden = 0
    AutomaticVisibility = 0
    Windowed = 0
    Minimized = 0
    Maximized = 0
    FullScreen = 0

    # Enum QWindow.AncestorMode
    ExcludeTransients = 0
    IncludeTransients = 0

    def __init__(self, screen = None):
        '''void QWindow.__init__(QScreen screen = None)'''
    def __init__(self, parent):
        '''void QWindow.__init__(QWindow parent)'''
    opacityChanged = pyqtSignal() # void opacityChanged(qreal) - signal
    activeChanged = pyqtSignal() # void activeChanged() - signal
    visibilityChanged = pyqtSignal() # void visibilityChanged(QWindow::Visibility) - signal
    def fromWinId(self, id):
        '''static QWindow QWindow.fromWinId(sip.voidptr id)'''
        return QWindow()
    def mask(self):
        '''QRegion QWindow.mask()'''
        return QRegion()
    def setMask(self, region):
        '''void QWindow.setMask(QRegion region)'''
    def opacity(self):
        '''float QWindow.opacity()'''
        return float()
    def setVisibility(self, v):
        '''void QWindow.setVisibility(QWindow.Visibility v)'''
    def visibility(self):
        '''QWindow.Visibility QWindow.visibility()'''
        return QWindow.Visibility()
    def tabletEvent(self):
        '''QTabletEvent QWindow.tabletEvent()'''
        return QTabletEvent()
    def touchEvent(self):
        '''QTouchEvent QWindow.touchEvent()'''
        return QTouchEvent()
    def wheelEvent(self):
        '''QWheelEvent QWindow.wheelEvent()'''
        return QWheelEvent()
    def mouseMoveEvent(self):
        '''QMouseEvent QWindow.mouseMoveEvent()'''
        return QMouseEvent()
    def mouseDoubleClickEvent(self):
        '''QMouseEvent QWindow.mouseDoubleClickEvent()'''
        return QMouseEvent()
    def mouseReleaseEvent(self):
        '''QMouseEvent QWindow.mouseReleaseEvent()'''
        return QMouseEvent()
    def mousePressEvent(self):
        '''QMouseEvent QWindow.mousePressEvent()'''
        return QMouseEvent()
    def keyReleaseEvent(self):
        '''QKeyEvent QWindow.keyReleaseEvent()'''
        return QKeyEvent()
    def keyPressEvent(self):
        '''QKeyEvent QWindow.keyPressEvent()'''
        return QKeyEvent()
    def event(self):
        '''QEvent QWindow.event()'''
        return QEvent()
    def hideEvent(self):
        '''QHideEvent QWindow.hideEvent()'''
        return QHideEvent()
    def showEvent(self):
        '''QShowEvent QWindow.showEvent()'''
        return QShowEvent()
    def focusOutEvent(self):
        '''QFocusEvent QWindow.focusOutEvent()'''
        return QFocusEvent()
    def focusInEvent(self):
        '''QFocusEvent QWindow.focusInEvent()'''
        return QFocusEvent()
    def moveEvent(self):
        '''QMoveEvent QWindow.moveEvent()'''
        return QMoveEvent()
    def resizeEvent(self):
        '''QResizeEvent QWindow.resizeEvent()'''
        return QResizeEvent()
    def exposeEvent(self):
        '''QExposeEvent QWindow.exposeEvent()'''
        return QExposeEvent()
    windowTitleChanged = pyqtSignal() # void windowTitleChanged(const QStringamp;) - signal
    focusObjectChanged = pyqtSignal() # void focusObjectChanged(QObject*) - signal
    contentOrientationChanged = pyqtSignal() # void contentOrientationChanged(Qt::ScreenOrientation) - signal
    visibleChanged = pyqtSignal() # void visibleChanged(bool) - signal
    maximumHeightChanged = pyqtSignal() # void maximumHeightChanged(int) - signal
    maximumWidthChanged = pyqtSignal() # void maximumWidthChanged(int) - signal
    minimumHeightChanged = pyqtSignal() # void minimumHeightChanged(int) - signal
    minimumWidthChanged = pyqtSignal() # void minimumWidthChanged(int) - signal
    heightChanged = pyqtSignal() # void heightChanged(int) - signal
    widthChanged = pyqtSignal() # void widthChanged(int) - signal
    yChanged = pyqtSignal() # void yChanged(int) - signal
    xChanged = pyqtSignal() # void xChanged(int) - signal
    windowStateChanged = pyqtSignal() # void windowStateChanged(Qt::WindowState) - signal
    modalityChanged = pyqtSignal() # void modalityChanged(Qt::WindowModality) - signal
    screenChanged = pyqtSignal() # void screenChanged(QScreen*) - signal
    def requestUpdate(self):
        '''void QWindow.requestUpdate()'''
    def alert(self, msec):
        '''void QWindow.alert(int msec)'''
    def setMaximumHeight(self, h):
        '''void QWindow.setMaximumHeight(int h)'''
    def setMaximumWidth(self, w):
        '''void QWindow.setMaximumWidth(int w)'''
    def setMinimumHeight(self, h):
        '''void QWindow.setMinimumHeight(int h)'''
    def setMinimumWidth(self, w):
        '''void QWindow.setMinimumWidth(int w)'''
    def setHeight(self, arg):
        '''void QWindow.setHeight(int arg)'''
    def setWidth(self, arg):
        '''void QWindow.setWidth(int arg)'''
    def setY(self, arg):
        '''void QWindow.setY(int arg)'''
    def setX(self, arg):
        '''void QWindow.setX(int arg)'''
    def setTitle(self):
        '''str QWindow.setTitle()'''
        return str()
    def lower(self):
        '''void QWindow.lower()'''
    def raise_(self):
        '''void QWindow.raise_()'''
    def close(self):
        '''bool QWindow.close()'''
        return bool()
    def showNormal(self):
        '''void QWindow.showNormal()'''
    def showFullScreen(self):
        '''void QWindow.showFullScreen()'''
    def showMaximized(self):
        '''void QWindow.showMaximized()'''
    def showMinimized(self):
        '''void QWindow.showMinimized()'''
    def hide(self):
        '''void QWindow.hide()'''
    def show(self):
        '''void QWindow.show()'''
    def setVisible(self, visible):
        '''void QWindow.setVisible(bool visible)'''
    def unsetCursor(self):
        '''void QWindow.unsetCursor()'''
    def setCursor(self):
        '''QCursor QWindow.setCursor()'''
        return QCursor()
    def cursor(self):
        '''QCursor QWindow.cursor()'''
        return QCursor()
    def mapFromGlobal(self, pos):
        '''QPoint QWindow.mapFromGlobal(QPoint pos)'''
        return QPoint()
    def mapToGlobal(self, pos):
        '''QPoint QWindow.mapToGlobal(QPoint pos)'''
        return QPoint()
    def focusObject(self):
        '''QObject QWindow.focusObject()'''
        return QObject()
    def setScreen(self, screen):
        '''void QWindow.setScreen(QScreen screen)'''
    def screen(self):
        '''QScreen QWindow.screen()'''
        return QScreen()
    def setMouseGrabEnabled(self, grab):
        '''bool QWindow.setMouseGrabEnabled(bool grab)'''
        return bool()
    def setKeyboardGrabEnabled(self, grab):
        '''bool QWindow.setKeyboardGrabEnabled(bool grab)'''
        return bool()
    def destroy(self):
        '''void QWindow.destroy()'''
    def icon(self):
        '''QIcon QWindow.icon()'''
        return QIcon()
    def setIcon(self, icon):
        '''void QWindow.setIcon(QIcon icon)'''
    def filePath(self):
        '''str QWindow.filePath()'''
        return str()
    def setFilePath(self, filePath):
        '''void QWindow.setFilePath(str filePath)'''
    def resize(self, newSize):
        '''void QWindow.resize(QSize newSize)'''
    def resize(self, w, h):
        '''void QWindow.resize(int w, int h)'''
    def setPosition(self, pt):
        '''void QWindow.setPosition(QPoint pt)'''
    def setPosition(self, posx, posy):
        '''void QWindow.setPosition(int posx, int posy)'''
    def position(self):
        '''QPoint QWindow.position()'''
        return QPoint()
    def size(self):
        '''QSize QWindow.size()'''
        return QSize()
    def y(self):
        '''int QWindow.y()'''
        return int()
    def x(self):
        '''int QWindow.x()'''
        return int()
    def height(self):
        '''int QWindow.height()'''
        return int()
    def width(self):
        '''int QWindow.width()'''
        return int()
    def setFramePosition(self, point):
        '''void QWindow.setFramePosition(QPoint point)'''
    def framePosition(self):
        '''QPoint QWindow.framePosition()'''
        return QPoint()
    def frameGeometry(self):
        '''QRect QWindow.frameGeometry()'''
        return QRect()
    def frameMargins(self):
        '''QMargins QWindow.frameMargins()'''
        return QMargins()
    def geometry(self):
        '''QRect QWindow.geometry()'''
        return QRect()
    def setGeometry(self, posx, posy, w, h):
        '''void QWindow.setGeometry(int posx, int posy, int w, int h)'''
    def setGeometry(self, rect):
        '''void QWindow.setGeometry(QRect rect)'''
    def setSizeIncrement(self, size):
        '''void QWindow.setSizeIncrement(QSize size)'''
    def setBaseSize(self, size):
        '''void QWindow.setBaseSize(QSize size)'''
    def setMaximumSize(self, size):
        '''void QWindow.setMaximumSize(QSize size)'''
    def setMinimumSize(self, size):
        '''void QWindow.setMinimumSize(QSize size)'''
    def sizeIncrement(self):
        '''QSize QWindow.sizeIncrement()'''
        return QSize()
    def baseSize(self):
        '''QSize QWindow.baseSize()'''
        return QSize()
    def maximumSize(self):
        '''QSize QWindow.maximumSize()'''
        return QSize()
    def minimumSize(self):
        '''QSize QWindow.minimumSize()'''
        return QSize()
    def maximumHeight(self):
        '''int QWindow.maximumHeight()'''
        return int()
    def maximumWidth(self):
        '''int QWindow.maximumWidth()'''
        return int()
    def minimumHeight(self):
        '''int QWindow.minimumHeight()'''
        return int()
    def minimumWidth(self):
        '''int QWindow.minimumWidth()'''
        return int()
    def isExposed(self):
        '''bool QWindow.isExposed()'''
        return bool()
    def isAncestorOf(self, child, mode = None):
        '''bool QWindow.isAncestorOf(QWindow child, QWindow.AncestorMode mode = QWindow.IncludeTransients)'''
        return bool()
    def transientParent(self):
        '''QWindow QWindow.transientParent()'''
        return QWindow()
    def setTransientParent(self, parent):
        '''void QWindow.setTransientParent(QWindow parent)'''
    def setWindowState(self, state):
        '''void QWindow.setWindowState(Qt.WindowState state)'''
    def windowState(self):
        '''Qt.WindowState QWindow.windowState()'''
        return Qt.WindowState()
    def devicePixelRatio(self):
        '''float QWindow.devicePixelRatio()'''
        return float()
    def contentOrientation(self):
        '''Qt.ScreenOrientation QWindow.contentOrientation()'''
        return Qt.ScreenOrientation()
    def reportContentOrientationChange(self, orientation):
        '''void QWindow.reportContentOrientationChange(Qt.ScreenOrientation orientation)'''
    def isActive(self):
        '''bool QWindow.isActive()'''
        return bool()
    def requestActivate(self):
        '''void QWindow.requestActivate()'''
    def setOpacity(self, level):
        '''void QWindow.setOpacity(float level)'''
    def title(self):
        '''str QWindow.title()'''
        return str()
    def type(self):
        '''Qt.WindowType QWindow.type()'''
        return Qt.WindowType()
    def flags(self):
        '''Qt.WindowFlags QWindow.flags()'''
        return Qt.WindowFlags()
    def setFlags(self, flags):
        '''void QWindow.setFlags(Qt.WindowFlags flags)'''
    def requestedFormat(self):
        '''QSurfaceFormat QWindow.requestedFormat()'''
        return QSurfaceFormat()
    def format(self):
        '''QSurfaceFormat QWindow.format()'''
        return QSurfaceFormat()
    def setFormat(self, format):
        '''void QWindow.setFormat(QSurfaceFormat format)'''
    def setModality(self, modality):
        '''void QWindow.setModality(Qt.WindowModality modality)'''
    def modality(self):
        '''Qt.WindowModality QWindow.modality()'''
        return Qt.WindowModality()
    def isModal(self):
        '''bool QWindow.isModal()'''
        return bool()
    def isTopLevel(self):
        '''bool QWindow.isTopLevel()'''
        return bool()
    def setParent(self, parent):
        '''void QWindow.setParent(QWindow parent)'''
    def parent(self):
        '''QWindow QWindow.parent()'''
        return QWindow()
    def winId(self):
        '''sip.voidptr QWindow.winId()'''
        return sip.voidptr()
    def create(self):
        '''void QWindow.create()'''
    def isVisible(self):
        '''bool QWindow.isVisible()'''
        return bool()
    def surfaceType(self):
        '''QSurface.SurfaceType QWindow.surfaceType()'''
        return QSurface.SurfaceType()
    def setSurfaceType(self, surfaceType):
        '''void QWindow.setSurfaceType(QSurface.SurfaceType surfaceType)'''


class QPaintDeviceWindow(QWindow, QPaintDevice):
    """"""
    def event(self, event):
        '''bool QPaintDeviceWindow.event(QEvent event)'''
        return bool()
    def exposeEvent(self):
        '''QExposeEvent QPaintDeviceWindow.exposeEvent()'''
        return QExposeEvent()
    def metric(self, metric):
        '''int QPaintDeviceWindow.metric(QPaintDevice.PaintDeviceMetric metric)'''
        return int()
    def paintEvent(self, event):
        '''void QPaintDeviceWindow.paintEvent(QPaintEvent event)'''
    def update(self, rect):
        '''void QPaintDeviceWindow.update(QRect rect)'''
    def update(self, region):
        '''void QPaintDeviceWindow.update(QRegion region)'''
    def update(self):
        '''void QPaintDeviceWindow.update()'''


class QOpenGLWindow(QPaintDeviceWindow):
    """"""
    # Enum QOpenGLWindow.UpdateBehavior
    NoPartialUpdate = 0
    PartialUpdateBlit = 0
    PartialUpdateBlend = 0

    def __init__(self, updateBehavior = None, parent = None):
        '''void QOpenGLWindow.__init__(QOpenGLWindow.UpdateBehavior updateBehavior = QOpenGLWindow.NoPartialUpdate, QWindow parent = None)'''
    def __init__(self, shareContext, updateBehavior = None, parent = None):
        '''void QOpenGLWindow.__init__(QOpenGLContext shareContext, QOpenGLWindow.UpdateBehavior updateBehavior = QOpenGLWindow.NoPartialUpdate, QWindow parent = None)'''
    def metric(self, metric):
        '''int QOpenGLWindow.metric(QPaintDevice.PaintDeviceMetric metric)'''
        return int()
    def resizeEvent(self, event):
        '''void QOpenGLWindow.resizeEvent(QResizeEvent event)'''
    def paintEvent(self, event):
        '''void QOpenGLWindow.paintEvent(QPaintEvent event)'''
    def paintOverGL(self):
        '''void QOpenGLWindow.paintOverGL()'''
    def paintUnderGL(self):
        '''void QOpenGLWindow.paintUnderGL()'''
    def paintGL(self):
        '''void QOpenGLWindow.paintGL()'''
    def resizeGL(self, w, h):
        '''void QOpenGLWindow.resizeGL(int w, int h)'''
    def initializeGL(self):
        '''void QOpenGLWindow.initializeGL()'''
    frameSwapped = pyqtSignal() # void frameSwapped() - signal
    def shareContext(self):
        '''QOpenGLContext QOpenGLWindow.shareContext()'''
        return QOpenGLContext()
    def grabFramebuffer(self):
        '''QImage QOpenGLWindow.grabFramebuffer()'''
        return QImage()
    def defaultFramebufferObject(self):
        '''int QOpenGLWindow.defaultFramebufferObject()'''
        return int()
    def context(self):
        '''QOpenGLContext QOpenGLWindow.context()'''
        return QOpenGLContext()
    def doneCurrent(self):
        '''void QOpenGLWindow.doneCurrent()'''
    def makeCurrent(self):
        '''void QOpenGLWindow.makeCurrent()'''
    def isValid(self):
        '''bool QOpenGLWindow.isValid()'''
        return bool()
    def updateBehavior(self):
        '''QOpenGLWindow.UpdateBehavior QOpenGLWindow.updateBehavior()'''
        return QOpenGLWindow.UpdateBehavior()


class QPagedPaintDevice(QPaintDevice):
    """"""
    # Enum QPagedPaintDevice.PageSize
    A4 = 0
    B5 = 0
    Letter = 0
    Legal = 0
    Executive = 0
    A0 = 0
    A1 = 0
    A2 = 0
    A3 = 0
    A5 = 0
    A6 = 0
    A7 = 0
    A8 = 0
    A9 = 0
    B0 = 0
    B1 = 0
    B10 = 0
    B2 = 0
    B3 = 0
    B4 = 0
    B6 = 0
    B7 = 0
    B8 = 0
    B9 = 0
    C5E = 0
    Comm10E = 0
    DLE = 0
    Folio = 0
    Ledger = 0
    Tabloid = 0
    Custom = 0
    A10 = 0
    A3Extra = 0
    A4Extra = 0
    A4Plus = 0
    A4Small = 0
    A5Extra = 0
    B5Extra = 0
    JisB0 = 0
    JisB1 = 0
    JisB2 = 0
    JisB3 = 0
    JisB4 = 0
    JisB5 = 0
    JisB6 = 0
    JisB7 = 0
    JisB8 = 0
    JisB9 = 0
    JisB10 = 0
    AnsiC = 0
    AnsiD = 0
    AnsiE = 0
    LegalExtra = 0
    LetterExtra = 0
    LetterPlus = 0
    LetterSmall = 0
    TabloidExtra = 0
    ArchA = 0
    ArchB = 0
    ArchC = 0
    ArchD = 0
    ArchE = 0
    Imperial7x9 = 0
    Imperial8x10 = 0
    Imperial9x11 = 0
    Imperial9x12 = 0
    Imperial10x11 = 0
    Imperial10x13 = 0
    Imperial10x14 = 0
    Imperial12x11 = 0
    Imperial15x11 = 0
    ExecutiveStandard = 0
    Note = 0
    Quarto = 0
    Statement = 0
    SuperA = 0
    SuperB = 0
    Postcard = 0
    DoublePostcard = 0
    Prc16K = 0
    Prc32K = 0
    Prc32KBig = 0
    FanFoldUS = 0
    FanFoldGerman = 0
    FanFoldGermanLegal = 0
    EnvelopeB4 = 0
    EnvelopeB5 = 0
    EnvelopeB6 = 0
    EnvelopeC0 = 0
    EnvelopeC1 = 0
    EnvelopeC2 = 0
    EnvelopeC3 = 0
    EnvelopeC4 = 0
    EnvelopeC6 = 0
    EnvelopeC65 = 0
    EnvelopeC7 = 0
    Envelope9 = 0
    Envelope11 = 0
    Envelope12 = 0
    Envelope14 = 0
    EnvelopeMonarch = 0
    EnvelopePersonal = 0
    EnvelopeChou3 = 0
    EnvelopeChou4 = 0
    EnvelopeInvite = 0
    EnvelopeItalian = 0
    EnvelopeKaku2 = 0
    EnvelopeKaku3 = 0
    EnvelopePrc1 = 0
    EnvelopePrc2 = 0
    EnvelopePrc3 = 0
    EnvelopePrc4 = 0
    EnvelopePrc5 = 0
    EnvelopePrc6 = 0
    EnvelopePrc7 = 0
    EnvelopePrc8 = 0
    EnvelopePrc9 = 0
    EnvelopePrc10 = 0
    EnvelopeYou4 = 0
    NPaperSize = 0
    AnsiA = 0
    AnsiB = 0
    EnvelopeC5 = 0
    EnvelopeDL = 0
    Envelope10 = 0
    LastPageSize = 0

    def __init__(self):
        '''void QPagedPaintDevice.__init__()'''
    def pageLayout(self):
        '''QPageLayout QPagedPaintDevice.pageLayout()'''
        return QPageLayout()
    def setPageMargins(self, margins):
        '''bool QPagedPaintDevice.setPageMargins(QMarginsF margins)'''
        return bool()
    def setPageMargins(self, margins, units):
        '''bool QPagedPaintDevice.setPageMargins(QMarginsF margins, QPageLayout.Unit units)'''
        return bool()
    def setPageOrientation(self, orientation):
        '''bool QPagedPaintDevice.setPageOrientation(QPageLayout.Orientation orientation)'''
        return bool()
    def setPageLayout(self, pageLayout):
        '''bool QPagedPaintDevice.setPageLayout(QPageLayout pageLayout)'''
        return bool()
    def margins(self):
        '''QPagedPaintDevice.Margins QPagedPaintDevice.margins()'''
        return QPagedPaintDevice.Margins()
    def setMargins(self, margins):
        '''void QPagedPaintDevice.setMargins(QPagedPaintDevice.Margins margins)'''
    def pageSizeMM(self):
        '''QSizeF QPagedPaintDevice.pageSizeMM()'''
        return QSizeF()
    def setPageSizeMM(self, size):
        '''void QPagedPaintDevice.setPageSizeMM(QSizeF size)'''
    def pageSize(self):
        '''QPagedPaintDevice.PageSize QPagedPaintDevice.pageSize()'''
        return QPagedPaintDevice.PageSize()
    def setPageSize(self, size):
        '''void QPagedPaintDevice.setPageSize(QPagedPaintDevice.PageSize size)'''
    def setPageSize(self, pageSize):
        '''bool QPagedPaintDevice.setPageSize(QPageSize pageSize)'''
        return bool()
    def newPage(self):
        '''abstract bool QPagedPaintDevice.newPage()'''
        return bool()
    class Margins():
        """"""
        bottom = None # float - member
        left = None # float - member
        right = None # float - member
        top = None # float - member
        def __init__(self):
            '''void QPagedPaintDevice.Margins.__init__()'''
        def __init__(self):
            '''QPagedPaintDevice.Margins QPagedPaintDevice.Margins.__init__()'''
            return QPagedPaintDevice.Margins()


class QPageLayout():
    """"""
    # Enum QPageLayout.Mode
    StandardMode = 0
    FullPageMode = 0

    # Enum QPageLayout.Orientation
    Portrait = 0
    Landscape = 0

    # Enum QPageLayout.Unit
    Millimeter = 0
    Point = 0
    Inch = 0
    Pica = 0
    Didot = 0
    Cicero = 0

    def __init__(self):
        '''void QPageLayout.__init__()'''
    def __init__(self, pageSize, orientation, margins, units = None, minMargins = None):
        '''void QPageLayout.__init__(QPageSize pageSize, QPageLayout.Orientation orientation, QMarginsF margins, QPageLayout.Unit units = QPageLayout.Point, QMarginsF minMargins = QMarginsF(0,0,0,0))'''
    def __init__(self, other):
        '''void QPageLayout.__init__(QPageLayout other)'''
    def __eq__(self, rhs):
        '''bool QPageLayout.__eq__(QPageLayout rhs)'''
        return bool()
    def __ne__(self, rhs):
        '''bool QPageLayout.__ne__(QPageLayout rhs)'''
        return bool()
    def paintRectPixels(self, resolution):
        '''QRect QPageLayout.paintRectPixels(int resolution)'''
        return QRect()
    def paintRectPoints(self):
        '''QRect QPageLayout.paintRectPoints()'''
        return QRect()
    def paintRect(self):
        '''QRectF QPageLayout.paintRect()'''
        return QRectF()
    def paintRect(self, units):
        '''QRectF QPageLayout.paintRect(QPageLayout.Unit units)'''
        return QRectF()
    def fullRectPixels(self, resolution):
        '''QRect QPageLayout.fullRectPixels(int resolution)'''
        return QRect()
    def fullRectPoints(self):
        '''QRect QPageLayout.fullRectPoints()'''
        return QRect()
    def fullRect(self):
        '''QRectF QPageLayout.fullRect()'''
        return QRectF()
    def fullRect(self, units):
        '''QRectF QPageLayout.fullRect(QPageLayout.Unit units)'''
        return QRectF()
    def maximumMargins(self):
        '''QMarginsF QPageLayout.maximumMargins()'''
        return QMarginsF()
    def minimumMargins(self):
        '''QMarginsF QPageLayout.minimumMargins()'''
        return QMarginsF()
    def setMinimumMargins(self, minMargins):
        '''void QPageLayout.setMinimumMargins(QMarginsF minMargins)'''
    def marginsPixels(self, resolution):
        '''QMargins QPageLayout.marginsPixels(int resolution)'''
        return QMargins()
    def marginsPoints(self):
        '''QMargins QPageLayout.marginsPoints()'''
        return QMargins()
    def margins(self):
        '''QMarginsF QPageLayout.margins()'''
        return QMarginsF()
    def margins(self, units):
        '''QMarginsF QPageLayout.margins(QPageLayout.Unit units)'''
        return QMarginsF()
    def setBottomMargin(self, bottomMargin):
        '''bool QPageLayout.setBottomMargin(float bottomMargin)'''
        return bool()
    def setTopMargin(self, topMargin):
        '''bool QPageLayout.setTopMargin(float topMargin)'''
        return bool()
    def setRightMargin(self, rightMargin):
        '''bool QPageLayout.setRightMargin(float rightMargin)'''
        return bool()
    def setLeftMargin(self, leftMargin):
        '''bool QPageLayout.setLeftMargin(float leftMargin)'''
        return bool()
    def setMargins(self, margins):
        '''bool QPageLayout.setMargins(QMarginsF margins)'''
        return bool()
    def units(self):
        '''QPageLayout.Unit QPageLayout.units()'''
        return QPageLayout.Unit()
    def setUnits(self, units):
        '''void QPageLayout.setUnits(QPageLayout.Unit units)'''
    def orientation(self):
        '''QPageLayout.Orientation QPageLayout.orientation()'''
        return QPageLayout.Orientation()
    def setOrientation(self, orientation):
        '''void QPageLayout.setOrientation(QPageLayout.Orientation orientation)'''
    def pageSize(self):
        '''QPageSize QPageLayout.pageSize()'''
        return QPageSize()
    def setPageSize(self, pageSize, minMargins = None):
        '''void QPageLayout.setPageSize(QPageSize pageSize, QMarginsF minMargins = QMarginsF(0,0,0,0))'''
    def mode(self):
        '''QPageLayout.Mode QPageLayout.mode()'''
        return QPageLayout.Mode()
    def setMode(self, mode):
        '''void QPageLayout.setMode(QPageLayout.Mode mode)'''
    def isValid(self):
        '''bool QPageLayout.isValid()'''
        return bool()
    def isEquivalentTo(self, other):
        '''bool QPageLayout.isEquivalentTo(QPageLayout other)'''
        return bool()
    def swap(self, other):
        '''void QPageLayout.swap(QPageLayout other)'''


class QPageSize():
    """"""
    # Enum QPageSize.SizeMatchPolicy
    FuzzyMatch = 0
    FuzzyOrientationMatch = 0
    ExactMatch = 0

    # Enum QPageSize.Unit
    Millimeter = 0
    Point = 0
    Inch = 0
    Pica = 0
    Didot = 0
    Cicero = 0

    # Enum QPageSize.PageSizeId
    A4 = 0
    B5 = 0
    Letter = 0
    Legal = 0
    Executive = 0
    A0 = 0
    A1 = 0
    A2 = 0
    A3 = 0
    A5 = 0
    A6 = 0
    A7 = 0
    A8 = 0
    A9 = 0
    B0 = 0
    B1 = 0
    B10 = 0
    B2 = 0
    B3 = 0
    B4 = 0
    B6 = 0
    B7 = 0
    B8 = 0
    B9 = 0
    C5E = 0
    Comm10E = 0
    DLE = 0
    Folio = 0
    Ledger = 0
    Tabloid = 0
    Custom = 0
    A10 = 0
    A3Extra = 0
    A4Extra = 0
    A4Plus = 0
    A4Small = 0
    A5Extra = 0
    B5Extra = 0
    JisB0 = 0
    JisB1 = 0
    JisB2 = 0
    JisB3 = 0
    JisB4 = 0
    JisB5 = 0
    JisB6 = 0
    JisB7 = 0
    JisB8 = 0
    JisB9 = 0
    JisB10 = 0
    AnsiC = 0
    AnsiD = 0
    AnsiE = 0
    LegalExtra = 0
    LetterExtra = 0
    LetterPlus = 0
    LetterSmall = 0
    TabloidExtra = 0
    ArchA = 0
    ArchB = 0
    ArchC = 0
    ArchD = 0
    ArchE = 0
    Imperial7x9 = 0
    Imperial8x10 = 0
    Imperial9x11 = 0
    Imperial9x12 = 0
    Imperial10x11 = 0
    Imperial10x13 = 0
    Imperial10x14 = 0
    Imperial12x11 = 0
    Imperial15x11 = 0
    ExecutiveStandard = 0
    Note = 0
    Quarto = 0
    Statement = 0
    SuperA = 0
    SuperB = 0
    Postcard = 0
    DoublePostcard = 0
    Prc16K = 0
    Prc32K = 0
    Prc32KBig = 0
    FanFoldUS = 0
    FanFoldGerman = 0
    FanFoldGermanLegal = 0
    EnvelopeB4 = 0
    EnvelopeB5 = 0
    EnvelopeB6 = 0
    EnvelopeC0 = 0
    EnvelopeC1 = 0
    EnvelopeC2 = 0
    EnvelopeC3 = 0
    EnvelopeC4 = 0
    EnvelopeC6 = 0
    EnvelopeC65 = 0
    EnvelopeC7 = 0
    Envelope9 = 0
    Envelope11 = 0
    Envelope12 = 0
    Envelope14 = 0
    EnvelopeMonarch = 0
    EnvelopePersonal = 0
    EnvelopeChou3 = 0
    EnvelopeChou4 = 0
    EnvelopeInvite = 0
    EnvelopeItalian = 0
    EnvelopeKaku2 = 0
    EnvelopeKaku3 = 0
    EnvelopePrc1 = 0
    EnvelopePrc2 = 0
    EnvelopePrc3 = 0
    EnvelopePrc4 = 0
    EnvelopePrc5 = 0
    EnvelopePrc6 = 0
    EnvelopePrc7 = 0
    EnvelopePrc8 = 0
    EnvelopePrc9 = 0
    EnvelopePrc10 = 0
    EnvelopeYou4 = 0
    NPageSize = 0
    NPaperSize = 0
    AnsiA = 0
    AnsiB = 0
    EnvelopeC5 = 0
    EnvelopeDL = 0
    Envelope10 = 0
    LastPageSize = 0

    def __init__(self):
        '''void QPageSize.__init__()'''
    def __init__(self, pageSizeId):
        '''void QPageSize.__init__(QPageSize.PageSizeId pageSizeId)'''
    def __init__(self, pointSize, name = str(), matchPolicy = None):
        '''void QPageSize.__init__(QSize pointSize, str name = str(), QPageSize.SizeMatchPolicy matchPolicy = QPageSize.FuzzyMatch)'''
    def __init__(self, size, units, name = str(), matchPolicy = None):
        '''void QPageSize.__init__(QSizeF size, QPageSize.Unit units, str name = str(), QPageSize.SizeMatchPolicy matchPolicy = QPageSize.FuzzyMatch)'''
    def __init__(self, other):
        '''void QPageSize.__init__(QPageSize other)'''
    def __eq__(self, rhs):
        '''bool QPageSize.__eq__(QPageSize rhs)'''
        return bool()
    def __ne__(self, rhs):
        '''bool QPageSize.__ne__(QPageSize rhs)'''
        return bool()
    def rectPixels(self, resolution):
        '''QRect QPageSize.rectPixels(int resolution)'''
        return QRect()
    def rectPoints(self):
        '''QRect QPageSize.rectPoints()'''
        return QRect()
    def rect(self, units):
        '''QRectF QPageSize.rect(QPageSize.Unit units)'''
        return QRectF()
    def sizePixels(self, resolution):
        '''QSize QPageSize.sizePixels(int resolution)'''
        return QSize()
    def sizePixels(self, pageSizeId, resolution):
        '''static QSize QPageSize.sizePixels(QPageSize.PageSizeId pageSizeId, int resolution)'''
        return QSize()
    def sizePoints(self):
        '''QSize QPageSize.sizePoints()'''
        return QSize()
    def sizePoints(self, pageSizeId):
        '''static QSize QPageSize.sizePoints(QPageSize.PageSizeId pageSizeId)'''
        return QSize()
    def size(self, units):
        '''QSizeF QPageSize.size(QPageSize.Unit units)'''
        return QSizeF()
    def size(self, pageSizeId, units):
        '''static QSizeF QPageSize.size(QPageSize.PageSizeId pageSizeId, QPageSize.Unit units)'''
        return QSizeF()
    def definitionUnits(self):
        '''QPageSize.Unit QPageSize.definitionUnits()'''
        return QPageSize.Unit()
    def definitionUnits(self, pageSizeId):
        '''static QPageSize.Unit QPageSize.definitionUnits(QPageSize.PageSizeId pageSizeId)'''
        return QPageSize.Unit()
    def definitionSize(self):
        '''QSizeF QPageSize.definitionSize()'''
        return QSizeF()
    def definitionSize(self, pageSizeId):
        '''static QSizeF QPageSize.definitionSize(QPageSize.PageSizeId pageSizeId)'''
        return QSizeF()
    def windowsId(self):
        '''int QPageSize.windowsId()'''
        return int()
    def windowsId(self, pageSizeId):
        '''static int QPageSize.windowsId(QPageSize.PageSizeId pageSizeId)'''
        return int()
    def id(self):
        '''QPageSize.PageSizeId QPageSize.id()'''
        return QPageSize.PageSizeId()
    def id(self, pointSize, matchPolicy = None):
        '''static QPageSize.PageSizeId QPageSize.id(QSize pointSize, QPageSize.SizeMatchPolicy matchPolicy = QPageSize.FuzzyMatch)'''
        return QPageSize.PageSizeId()
    def id(self, size, units, matchPolicy = None):
        '''static QPageSize.PageSizeId QPageSize.id(QSizeF size, QPageSize.Unit units, QPageSize.SizeMatchPolicy matchPolicy = QPageSize.FuzzyMatch)'''
        return QPageSize.PageSizeId()
    def id(self, windowsId):
        '''static QPageSize.PageSizeId QPageSize.id(int windowsId)'''
        return QPageSize.PageSizeId()
    def name(self):
        '''str QPageSize.name()'''
        return str()
    def name(self, pageSizeId):
        '''static str QPageSize.name(QPageSize.PageSizeId pageSizeId)'''
        return str()
    def key(self):
        '''str QPageSize.key()'''
        return str()
    def key(self, pageSizeId):
        '''static str QPageSize.key(QPageSize.PageSizeId pageSizeId)'''
        return str()
    def isValid(self):
        '''bool QPageSize.isValid()'''
        return bool()
    def isEquivalentTo(self, other):
        '''bool QPageSize.isEquivalentTo(QPageSize other)'''
        return bool()
    def swap(self, other):
        '''void QPageSize.swap(QPageSize other)'''


class QPainter():
    """"""
    # Enum QPainter.PixmapFragmentHint
    OpaqueHint = 0

    # Enum QPainter.CompositionMode
    CompositionMode_SourceOver = 0
    CompositionMode_DestinationOver = 0
    CompositionMode_Clear = 0
    CompositionMode_Source = 0
    CompositionMode_Destination = 0
    CompositionMode_SourceIn = 0
    CompositionMode_DestinationIn = 0
    CompositionMode_SourceOut = 0
    CompositionMode_DestinationOut = 0
    CompositionMode_SourceAtop = 0
    CompositionMode_DestinationAtop = 0
    CompositionMode_Xor = 0
    CompositionMode_Plus = 0
    CompositionMode_Multiply = 0
    CompositionMode_Screen = 0
    CompositionMode_Overlay = 0
    CompositionMode_Darken = 0
    CompositionMode_Lighten = 0
    CompositionMode_ColorDodge = 0
    CompositionMode_ColorBurn = 0
    CompositionMode_HardLight = 0
    CompositionMode_SoftLight = 0
    CompositionMode_Difference = 0
    CompositionMode_Exclusion = 0
    RasterOp_SourceOrDestination = 0
    RasterOp_SourceAndDestination = 0
    RasterOp_SourceXorDestination = 0
    RasterOp_NotSourceAndNotDestination = 0
    RasterOp_NotSourceOrNotDestination = 0
    RasterOp_NotSourceXorDestination = 0
    RasterOp_NotSource = 0
    RasterOp_NotSourceAndDestination = 0
    RasterOp_SourceAndNotDestination = 0
    RasterOp_NotSourceOrDestination = 0
    RasterOp_SourceOrNotDestination = 0
    RasterOp_ClearDestination = 0
    RasterOp_SetDestination = 0
    RasterOp_NotDestination = 0

    # Enum QPainter.RenderHint
    Antialiasing = 0
    TextAntialiasing = 0
    SmoothPixmapTransform = 0
    HighQualityAntialiasing = 0
    NonCosmeticDefaultPen = 0
    Qt4CompatiblePainting = 0

    def __init__(self):
        '''void QPainter.__init__()'''
    def __init__(self):
        '''QPaintDevice QPainter.__init__()'''
        return QPaintDevice()
    def drawGlyphRun(self, position, glyphRun):
        '''void QPainter.drawGlyphRun(QPointF position, QGlyphRun glyphRun)'''
    def clipBoundingRect(self):
        '''QRectF QPainter.clipBoundingRect()'''
        return QRectF()
    def drawStaticText(self, topLeftPosition, staticText):
        '''void QPainter.drawStaticText(QPointF topLeftPosition, QStaticText staticText)'''
    def drawStaticText(self, p, staticText):
        '''void QPainter.drawStaticText(QPoint p, QStaticText staticText)'''
    def drawStaticText(self, x, y, staticText):
        '''void QPainter.drawStaticText(int x, int y, QStaticText staticText)'''
    def drawPixmapFragments(self, fragments, pixmap, hints = 0):
        '''void QPainter.drawPixmapFragments(list-of-QPainter.PixmapFragment fragments, QPixmap pixmap, QPainter.PixmapFragmentHints hints = 0)'''
    def endNativePainting(self):
        '''void QPainter.endNativePainting()'''
    def beginNativePainting(self):
        '''void QPainter.beginNativePainting()'''
    def drawRoundedRect(self, rect, xRadius, yRadius, mode = None):
        '''void QPainter.drawRoundedRect(QRectF rect, float xRadius, float yRadius, Qt.SizeMode mode = Qt.AbsoluteSize)'''
    def drawRoundedRect(self, x, y, w, h, xRadius, yRadius, mode = None):
        '''void QPainter.drawRoundedRect(int x, int y, int w, int h, float xRadius, float yRadius, Qt.SizeMode mode = Qt.AbsoluteSize)'''
    def drawRoundedRect(self, rect, xRadius, yRadius, mode = None):
        '''void QPainter.drawRoundedRect(QRect rect, float xRadius, float yRadius, Qt.SizeMode mode = Qt.AbsoluteSize)'''
    def testRenderHint(self, hint):
        '''bool QPainter.testRenderHint(QPainter.RenderHint hint)'''
        return bool()
    def combinedTransform(self):
        '''QTransform QPainter.combinedTransform()'''
        return QTransform()
    def worldTransform(self):
        '''QTransform QPainter.worldTransform()'''
        return QTransform()
    def setWorldTransform(self, matrix, combine = False):
        '''void QPainter.setWorldTransform(QTransform matrix, bool combine = False)'''
    def resetTransform(self):
        '''void QPainter.resetTransform()'''
    def deviceTransform(self):
        '''QTransform QPainter.deviceTransform()'''
        return QTransform()
    def transform(self):
        '''QTransform QPainter.transform()'''
        return QTransform()
    def setTransform(self, transform, combine = False):
        '''void QPainter.setTransform(QTransform transform, bool combine = False)'''
    def setWorldMatrixEnabled(self, enabled):
        '''void QPainter.setWorldMatrixEnabled(bool enabled)'''
    def worldMatrixEnabled(self):
        '''bool QPainter.worldMatrixEnabled()'''
        return bool()
    def setOpacity(self, opacity):
        '''void QPainter.setOpacity(float opacity)'''
    def opacity(self):
        '''float QPainter.opacity()'''
        return float()
    def drawImage(self, targetRect, image, sourceRect, flags = None):
        '''void QPainter.drawImage(QRectF targetRect, QImage image, QRectF sourceRect, Qt.ImageConversionFlags flags = Qt.AutoColor)'''
    def drawImage(self, targetRect, image, sourceRect, flags = None):
        '''void QPainter.drawImage(QRect targetRect, QImage image, QRect sourceRect, Qt.ImageConversionFlags flags = Qt.AutoColor)'''
    def drawImage(self, p, image, sr, flags = None):
        '''void QPainter.drawImage(QPointF p, QImage image, QRectF sr, Qt.ImageConversionFlags flags = Qt.AutoColor)'''
    def drawImage(self, p, image, sr, flags = None):
        '''void QPainter.drawImage(QPoint p, QImage image, QRect sr, Qt.ImageConversionFlags flags = Qt.AutoColor)'''
    def drawImage(self, r, image):
        '''void QPainter.drawImage(QRectF r, QImage image)'''
    def drawImage(self, r, image):
        '''void QPainter.drawImage(QRect r, QImage image)'''
    def drawImage(self, p, image):
        '''void QPainter.drawImage(QPointF p, QImage image)'''
    def drawImage(self, p, image):
        '''void QPainter.drawImage(QPoint p, QImage image)'''
    def drawImage(self, x, y, image, sx = 0, sy = 0, sw = None, sh = None, flags = None):
        '''void QPainter.drawImage(int x, int y, QImage image, int sx = 0, int sy = 0, int sw = -1, int sh = -1, Qt.ImageConversionFlags flags = Qt.AutoColor)'''
    def drawPoint(self, p):
        '''void QPainter.drawPoint(QPointF p)'''
    def drawPoint(self, x, y):
        '''void QPainter.drawPoint(int x, int y)'''
    def drawPoint(self, p):
        '''void QPainter.drawPoint(QPoint p)'''
    def drawRect(self, rect):
        '''void QPainter.drawRect(QRectF rect)'''
    def drawRect(self, x, y, w, h):
        '''void QPainter.drawRect(int x, int y, int w, int h)'''
    def drawRect(self, r):
        '''void QPainter.drawRect(QRect r)'''
    def drawLine(self, l):
        '''void QPainter.drawLine(QLineF l)'''
    def drawLine(self, line):
        '''void QPainter.drawLine(QLine line)'''
    def drawLine(self, x1, y1, x2, y2):
        '''void QPainter.drawLine(int x1, int y1, int x2, int y2)'''
    def drawLine(self, p1, p2):
        '''void QPainter.drawLine(QPoint p1, QPoint p2)'''
    def drawLine(self, p1, p2):
        '''void QPainter.drawLine(QPointF p1, QPointF p2)'''
    def paintEngine(self):
        '''QPaintEngine QPainter.paintEngine()'''
        return QPaintEngine()
    def setRenderHints(self, hints, on = True):
        '''void QPainter.setRenderHints(QPainter.RenderHints hints, bool on = True)'''
    def renderHints(self):
        '''QPainter.RenderHints QPainter.renderHints()'''
        return QPainter.RenderHints()
    def setRenderHint(self, hint, on = True):
        '''void QPainter.setRenderHint(QPainter.RenderHint hint, bool on = True)'''
    def eraseRect(self):
        '''QRectF QPainter.eraseRect()'''
        return QRectF()
    def eraseRect(self, rect):
        '''void QPainter.eraseRect(QRect rect)'''
    def eraseRect(self, x, y, w, h):
        '''void QPainter.eraseRect(int x, int y, int w, int h)'''
    def fillRect(self):
        '''QBrush QPainter.fillRect()'''
        return QBrush()
    def fillRect(self):
        '''QBrush QPainter.fillRect()'''
        return QBrush()
    def fillRect(self, x, y, w, h, b):
        '''void QPainter.fillRect(int x, int y, int w, int h, QBrush b)'''
    def fillRect(self, color):
        '''QRectF QPainter.fillRect(QColor color)'''
        return QRectF()
    def fillRect(self, color):
        '''QRect QPainter.fillRect(QColor color)'''
        return QRect()
    def fillRect(self, x, y, w, h, b):
        '''void QPainter.fillRect(int x, int y, int w, int h, QColor b)'''
    def fillRect(self, x, y, w, h, c):
        '''void QPainter.fillRect(int x, int y, int w, int h, Qt.GlobalColor c)'''
    def fillRect(self, r, c):
        '''void QPainter.fillRect(QRect r, Qt.GlobalColor c)'''
    def fillRect(self, r, c):
        '''void QPainter.fillRect(QRectF r, Qt.GlobalColor c)'''
    def fillRect(self, x, y, w, h, style):
        '''void QPainter.fillRect(int x, int y, int w, int h, Qt.BrushStyle style)'''
    def fillRect(self, r, style):
        '''void QPainter.fillRect(QRect r, Qt.BrushStyle style)'''
    def fillRect(self, r, style):
        '''void QPainter.fillRect(QRectF r, Qt.BrushStyle style)'''
    def boundingRect(self, rect, flags, text):
        '''QRectF QPainter.boundingRect(QRectF rect, int flags, str text)'''
        return QRectF()
    def boundingRect(self, rect, flags, text):
        '''QRect QPainter.boundingRect(QRect rect, int flags, str text)'''
        return QRect()
    def boundingRect(self, rectangle, text, option = QTextOption()):
        '''QRectF QPainter.boundingRect(QRectF rectangle, str text, QTextOption option = QTextOption())'''
        return QRectF()
    def boundingRect(self, x, y, w, h, flags, text):
        '''QRect QPainter.boundingRect(int x, int y, int w, int h, int flags, str text)'''
        return QRect()
    def drawText(self, p, s):
        '''void QPainter.drawText(QPointF p, str s)'''
    def drawText(self, rectangle, flags, text, boundingRect):
        '''void QPainter.drawText(QRectF rectangle, int flags, str text, QRectF boundingRect)'''
    def drawText(self, rectangle, flags, text, boundingRect):
        '''void QPainter.drawText(QRect rectangle, int flags, str text, QRect boundingRect)'''
    def drawText(self, rectangle, text, option = QTextOption()):
        '''void QPainter.drawText(QRectF rectangle, str text, QTextOption option = QTextOption())'''
    def drawText(self, p, s):
        '''void QPainter.drawText(QPoint p, str s)'''
    def drawText(self, x, y, width, height, flags, text, boundingRect):
        '''void QPainter.drawText(int x, int y, int width, int height, int flags, str text, QRect boundingRect)'''
    def drawText(self, x, y, s):
        '''void QPainter.drawText(int x, int y, str s)'''
    def layoutDirection(self):
        '''Qt.LayoutDirection QPainter.layoutDirection()'''
        return Qt.LayoutDirection()
    def setLayoutDirection(self, direction):
        '''void QPainter.setLayoutDirection(Qt.LayoutDirection direction)'''
    def drawPixmap(self, targetRect, pixmap, sourceRect):
        '''void QPainter.drawPixmap(QRectF targetRect, QPixmap pixmap, QRectF sourceRect)'''
    def drawPixmap(self, targetRect, pixmap, sourceRect):
        '''void QPainter.drawPixmap(QRect targetRect, QPixmap pixmap, QRect sourceRect)'''
    def drawPixmap(self, p, pm):
        '''void QPainter.drawPixmap(QPointF p, QPixmap pm)'''
    def drawPixmap(self, p, pm):
        '''void QPainter.drawPixmap(QPoint p, QPixmap pm)'''
    def drawPixmap(self, r, pm):
        '''void QPainter.drawPixmap(QRect r, QPixmap pm)'''
    def drawPixmap(self, x, y, pm):
        '''void QPainter.drawPixmap(int x, int y, QPixmap pm)'''
    def drawPixmap(self, x, y, w, h, pm):
        '''void QPainter.drawPixmap(int x, int y, int w, int h, QPixmap pm)'''
    def drawPixmap(self, x, y, w, h, pm, sx, sy, sw, sh):
        '''void QPainter.drawPixmap(int x, int y, int w, int h, QPixmap pm, int sx, int sy, int sw, int sh)'''
    def drawPixmap(self, x, y, pm, sx, sy, sw, sh):
        '''void QPainter.drawPixmap(int x, int y, QPixmap pm, int sx, int sy, int sw, int sh)'''
    def drawPixmap(self, p, pm, sr):
        '''void QPainter.drawPixmap(QPointF p, QPixmap pm, QRectF sr)'''
    def drawPixmap(self, p, pm, sr):
        '''void QPainter.drawPixmap(QPoint p, QPixmap pm, QRect sr)'''
    def drawPicture(self, p, picture):
        '''void QPainter.drawPicture(QPointF p, QPicture picture)'''
    def drawPicture(self, x, y, p):
        '''void QPainter.drawPicture(int x, int y, QPicture p)'''
    def drawPicture(self, pt, p):
        '''void QPainter.drawPicture(QPoint pt, QPicture p)'''
    def drawTiledPixmap(self, rectangle, pixmap, pos = QPointF()):
        '''void QPainter.drawTiledPixmap(QRectF rectangle, QPixmap pixmap, QPointF pos = QPointF())'''
    def drawTiledPixmap(self, rectangle, pixmap, pos = QPoint()):
        '''void QPainter.drawTiledPixmap(QRect rectangle, QPixmap pixmap, QPoint pos = QPoint())'''
    def drawTiledPixmap(self, x, y, width, height, pixmap, sx = 0, sy = 0):
        '''void QPainter.drawTiledPixmap(int x, int y, int width, int height, QPixmap pixmap, int sx = 0, int sy = 0)'''
    def drawChord(self, rect, a, alen):
        '''void QPainter.drawChord(QRectF rect, int a, int alen)'''
    def drawChord(self, rect, a, alen):
        '''void QPainter.drawChord(QRect rect, int a, int alen)'''
    def drawChord(self, x, y, w, h, a, alen):
        '''void QPainter.drawChord(int x, int y, int w, int h, int a, int alen)'''
    def drawPie(self, rect, a, alen):
        '''void QPainter.drawPie(QRectF rect, int a, int alen)'''
    def drawPie(self, rect, a, alen):
        '''void QPainter.drawPie(QRect rect, int a, int alen)'''
    def drawPie(self, x, y, w, h, a, alen):
        '''void QPainter.drawPie(int x, int y, int w, int h, int a, int alen)'''
    def drawArc(self, rect, a, alen):
        '''void QPainter.drawArc(QRectF rect, int a, int alen)'''
    def drawArc(self, r, a, alen):
        '''void QPainter.drawArc(QRect r, int a, int alen)'''
    def drawArc(self, x, y, w, h, a, alen):
        '''void QPainter.drawArc(int x, int y, int w, int h, int a, int alen)'''
    def drawConvexPolygon(self, point, *args):
        '''void QPainter.drawConvexPolygon(QPointF point, ... *args)'''
    def drawConvexPolygon(self, poly):
        '''void QPainter.drawConvexPolygon(QPolygonF poly)'''
    def drawConvexPolygon(self, point, *args):
        '''void QPainter.drawConvexPolygon(QPoint point, ... *args)'''
    def drawConvexPolygon(self, poly):
        '''void QPainter.drawConvexPolygon(QPolygon poly)'''
    def drawPolygon(self, point, *args):
        '''void QPainter.drawPolygon(QPointF point, ... *args)'''
    def drawPolygon(self, points, fillRule = None):
        '''void QPainter.drawPolygon(QPolygonF points, Qt.FillRule fillRule = Qt.OddEvenFill)'''
    def drawPolygon(self, point, *args):
        '''void QPainter.drawPolygon(QPoint point, ... *args)'''
    def drawPolygon(self, points, fillRule = None):
        '''void QPainter.drawPolygon(QPolygon points, Qt.FillRule fillRule = Qt.OddEvenFill)'''
    def drawPolyline(self, point, *args):
        '''void QPainter.drawPolyline(QPointF point, ... *args)'''
    def drawPolyline(self, polyline):
        '''void QPainter.drawPolyline(QPolygonF polyline)'''
    def drawPolyline(self, point, *args):
        '''void QPainter.drawPolyline(QPoint point, ... *args)'''
    def drawPolyline(self, polyline):
        '''void QPainter.drawPolyline(QPolygon polyline)'''
    def drawEllipse(self, r):
        '''void QPainter.drawEllipse(QRectF r)'''
    def drawEllipse(self, r):
        '''void QPainter.drawEllipse(QRect r)'''
    def drawEllipse(self, x, y, w, h):
        '''void QPainter.drawEllipse(int x, int y, int w, int h)'''
    def drawEllipse(self, center, rx, ry):
        '''void QPainter.drawEllipse(QPointF center, float rx, float ry)'''
    def drawEllipse(self, center, rx, ry):
        '''void QPainter.drawEllipse(QPoint center, int rx, int ry)'''
    def drawRects(self, rect, *args):
        '''void QPainter.drawRects(QRectF rect, ... *args)'''
    def drawRects(self, rects):
        '''void QPainter.drawRects(list-of-QRectF rects)'''
    def drawRects(self, rect, *args):
        '''void QPainter.drawRects(QRect rect, ... *args)'''
    def drawRects(self, rects):
        '''void QPainter.drawRects(list-of-QRect rects)'''
    def drawLines(self, line, *args):
        '''void QPainter.drawLines(QLineF line, ... *args)'''
    def drawLines(self, lines):
        '''void QPainter.drawLines(list-of-QLineF lines)'''
    def drawLines(self, pointPair, *args):
        '''void QPainter.drawLines(QPointF pointPair, ... *args)'''
    def drawLines(self, pointPairs):
        '''void QPainter.drawLines(list-of-QPointF pointPairs)'''
    def drawLines(self, line, *args):
        '''void QPainter.drawLines(QLine line, ... *args)'''
    def drawLines(self, lines):
        '''void QPainter.drawLines(list-of-QLine lines)'''
    def drawLines(self, pointPair, *args):
        '''void QPainter.drawLines(QPoint pointPair, ... *args)'''
    def drawLines(self, pointPairs):
        '''void QPainter.drawLines(list-of-QPoint pointPairs)'''
    def drawPoints(self, point, *args):
        '''void QPainter.drawPoints(QPointF point, ... *args)'''
    def drawPoints(self, points):
        '''void QPainter.drawPoints(QPolygonF points)'''
    def drawPoints(self, point, *args):
        '''void QPainter.drawPoints(QPoint point, ... *args)'''
    def drawPoints(self, points):
        '''void QPainter.drawPoints(QPolygon points)'''
    def drawPath(self, path):
        '''void QPainter.drawPath(QPainterPath path)'''
    def fillPath(self, path, brush):
        '''void QPainter.fillPath(QPainterPath path, QBrush brush)'''
    def strokePath(self, path, pen):
        '''void QPainter.strokePath(QPainterPath path, QPen pen)'''
    def viewTransformEnabled(self):
        '''bool QPainter.viewTransformEnabled()'''
        return bool()
    def setViewTransformEnabled(self, enable):
        '''void QPainter.setViewTransformEnabled(bool enable)'''
    def setViewport(self, viewport):
        '''void QPainter.setViewport(QRect viewport)'''
    def setViewport(self, x, y, w, h):
        '''void QPainter.setViewport(int x, int y, int w, int h)'''
    def viewport(self):
        '''QRect QPainter.viewport()'''
        return QRect()
    def setWindow(self, window):
        '''void QPainter.setWindow(QRect window)'''
    def setWindow(self, x, y, w, h):
        '''void QPainter.setWindow(int x, int y, int w, int h)'''
    def window(self):
        '''QRect QPainter.window()'''
        return QRect()
    def translate(self, offset):
        '''void QPainter.translate(QPointF offset)'''
    def translate(self, dx, dy):
        '''void QPainter.translate(float dx, float dy)'''
    def translate(self, offset):
        '''void QPainter.translate(QPoint offset)'''
    def rotate(self, a):
        '''void QPainter.rotate(float a)'''
    def shear(self, sh, sv):
        '''void QPainter.shear(float sh, float sv)'''
    def scale(self, sx, sy):
        '''void QPainter.scale(float sx, float sy)'''
    def restore(self):
        '''void QPainter.restore()'''
    def save(self):
        '''void QPainter.save()'''
    def hasClipping(self):
        '''bool QPainter.hasClipping()'''
        return bool()
    def setClipping(self, enable):
        '''void QPainter.setClipping(bool enable)'''
    def setClipPath(self, path, operation = None):
        '''void QPainter.setClipPath(QPainterPath path, Qt.ClipOperation operation = Qt.ReplaceClip)'''
    def setClipRegion(self, region, operation = None):
        '''void QPainter.setClipRegion(QRegion region, Qt.ClipOperation operation = Qt.ReplaceClip)'''
    def setClipRect(self, rectangle, operation = None):
        '''void QPainter.setClipRect(QRectF rectangle, Qt.ClipOperation operation = Qt.ReplaceClip)'''
    def setClipRect(self, x, y, width, height, operation = None):
        '''void QPainter.setClipRect(int x, int y, int width, int height, Qt.ClipOperation operation = Qt.ReplaceClip)'''
    def setClipRect(self, rectangle, operation = None):
        '''void QPainter.setClipRect(QRect rectangle, Qt.ClipOperation operation = Qt.ReplaceClip)'''
    def clipPath(self):
        '''QPainterPath QPainter.clipPath()'''
        return QPainterPath()
    def clipRegion(self):
        '''QRegion QPainter.clipRegion()'''
        return QRegion()
    def background(self):
        '''QBrush QPainter.background()'''
        return QBrush()
    def setBackground(self, bg):
        '''void QPainter.setBackground(QBrush bg)'''
    def setBrushOrigin(self):
        '''QPointF QPainter.setBrushOrigin()'''
        return QPointF()
    def setBrushOrigin(self, x, y):
        '''void QPainter.setBrushOrigin(int x, int y)'''
    def setBrushOrigin(self, p):
        '''void QPainter.setBrushOrigin(QPoint p)'''
    def brushOrigin(self):
        '''QPoint QPainter.brushOrigin()'''
        return QPoint()
    def backgroundMode(self):
        '''Qt.BGMode QPainter.backgroundMode()'''
        return Qt.BGMode()
    def setBackgroundMode(self, mode):
        '''void QPainter.setBackgroundMode(Qt.BGMode mode)'''
    def brush(self):
        '''QBrush QPainter.brush()'''
        return QBrush()
    def setBrush(self, brush):
        '''void QPainter.setBrush(QBrush brush)'''
    def setBrush(self, style):
        '''void QPainter.setBrush(Qt.BrushStyle style)'''
    def pen(self):
        '''QPen QPainter.pen()'''
        return QPen()
    def setPen(self, color):
        '''void QPainter.setPen(QColor color)'''
    def setPen(self, pen):
        '''void QPainter.setPen(QPen pen)'''
    def setPen(self, style):
        '''void QPainter.setPen(Qt.PenStyle style)'''
    def fontInfo(self):
        '''QFontInfo QPainter.fontInfo()'''
        return QFontInfo()
    def fontMetrics(self):
        '''QFontMetrics QPainter.fontMetrics()'''
        return QFontMetrics()
    def setFont(self, f):
        '''void QPainter.setFont(QFont f)'''
    def font(self):
        '''QFont QPainter.font()'''
        return QFont()
    def compositionMode(self):
        '''QPainter.CompositionMode QPainter.compositionMode()'''
        return QPainter.CompositionMode()
    def setCompositionMode(self, mode):
        '''void QPainter.setCompositionMode(QPainter.CompositionMode mode)'''
    def isActive(self):
        '''bool QPainter.isActive()'''
        return bool()
    def end(self):
        '''bool QPainter.end()'''
        return bool()
    def begin(self):
        '''QPaintDevice QPainter.begin()'''
        return QPaintDevice()
    def device(self):
        '''QPaintDevice QPainter.device()'''
        return QPaintDevice()
    def __exit__(self, type, value, traceback):
        '''void QPainter.__exit__(object type, object value, object traceback)'''
    def __enter__(self):
        '''object QPainter.__enter__()'''
        return object()
    class PixmapFragment():
        """"""
        height = None # float - member
        opacity = None # float - member
        rotation = None # float - member
        scaleX = None # float - member
        scaleY = None # float - member
        sourceLeft = None # float - member
        sourceTop = None # float - member
        width = None # float - member
        x = None # float - member
        y = None # float - member
        def __init__(self):
            '''void QPainter.PixmapFragment.__init__()'''
        def __init__(self):
            '''QPainter.PixmapFragment QPainter.PixmapFragment.__init__()'''
            return QPainter.PixmapFragment()
        def create(self, pos, sourceRect, scaleX = 1, scaleY = 1, rotation = 0, opacity = 1):
            '''static QPainter.PixmapFragment QPainter.PixmapFragment.create(QPointF pos, QRectF sourceRect, float scaleX = 1, float scaleY = 1, float rotation = 0, float opacity = 1)'''
            return QPainter.PixmapFragment()
    class PixmapFragmentHints():
        """"""
        def __init__(self):
            '''QPainter.PixmapFragmentHints QPainter.PixmapFragmentHints.__init__()'''
            return QPainter.PixmapFragmentHints()
        def __init__(self):
            '''int QPainter.PixmapFragmentHints.__init__()'''
            return int()
        def __init__(self):
            '''void QPainter.PixmapFragmentHints.__init__()'''
        def __bool__(self):
            '''int QPainter.PixmapFragmentHints.__bool__()'''
            return int()
        def __ne__(self, f):
            '''bool QPainter.PixmapFragmentHints.__ne__(QPainter.PixmapFragmentHints f)'''
            return bool()
        def __eq__(self, f):
            '''bool QPainter.PixmapFragmentHints.__eq__(QPainter.PixmapFragmentHints f)'''
            return bool()
        def __invert__(self):
            '''QPainter.PixmapFragmentHints QPainter.PixmapFragmentHints.__invert__()'''
            return QPainter.PixmapFragmentHints()
        def __and__(self, mask):
            '''QPainter.PixmapFragmentHints QPainter.PixmapFragmentHints.__and__(int mask)'''
            return QPainter.PixmapFragmentHints()
        def __xor__(self, f):
            '''QPainter.PixmapFragmentHints QPainter.PixmapFragmentHints.__xor__(QPainter.PixmapFragmentHints f)'''
            return QPainter.PixmapFragmentHints()
        def __xor__(self, f):
            '''QPainter.PixmapFragmentHints QPainter.PixmapFragmentHints.__xor__(int f)'''
            return QPainter.PixmapFragmentHints()
        def __or__(self, f):
            '''QPainter.PixmapFragmentHints QPainter.PixmapFragmentHints.__or__(QPainter.PixmapFragmentHints f)'''
            return QPainter.PixmapFragmentHints()
        def __or__(self, f):
            '''QPainter.PixmapFragmentHints QPainter.PixmapFragmentHints.__or__(int f)'''
            return QPainter.PixmapFragmentHints()
        def __int__(self):
            '''int QPainter.PixmapFragmentHints.__int__()'''
            return int()
        def __ixor__(self, f):
            '''QPainter.PixmapFragmentHints QPainter.PixmapFragmentHints.__ixor__(QPainter.PixmapFragmentHints f)'''
            return QPainter.PixmapFragmentHints()
        def __ior__(self, f):
            '''QPainter.PixmapFragmentHints QPainter.PixmapFragmentHints.__ior__(QPainter.PixmapFragmentHints f)'''
            return QPainter.PixmapFragmentHints()
        def __iand__(self, mask):
            '''QPainter.PixmapFragmentHints QPainter.PixmapFragmentHints.__iand__(int mask)'''
            return QPainter.PixmapFragmentHints()
    class RenderHints():
        """"""
        def __init__(self):
            '''QPainter.RenderHints QPainter.RenderHints.__init__()'''
            return QPainter.RenderHints()
        def __init__(self):
            '''int QPainter.RenderHints.__init__()'''
            return int()
        def __init__(self):
            '''void QPainter.RenderHints.__init__()'''
        def __bool__(self):
            '''int QPainter.RenderHints.__bool__()'''
            return int()
        def __ne__(self, f):
            '''bool QPainter.RenderHints.__ne__(QPainter.RenderHints f)'''
            return bool()
        def __eq__(self, f):
            '''bool QPainter.RenderHints.__eq__(QPainter.RenderHints f)'''
            return bool()
        def __invert__(self):
            '''QPainter.RenderHints QPainter.RenderHints.__invert__()'''
            return QPainter.RenderHints()
        def __and__(self, mask):
            '''QPainter.RenderHints QPainter.RenderHints.__and__(int mask)'''
            return QPainter.RenderHints()
        def __xor__(self, f):
            '''QPainter.RenderHints QPainter.RenderHints.__xor__(QPainter.RenderHints f)'''
            return QPainter.RenderHints()
        def __xor__(self, f):
            '''QPainter.RenderHints QPainter.RenderHints.__xor__(int f)'''
            return QPainter.RenderHints()
        def __or__(self, f):
            '''QPainter.RenderHints QPainter.RenderHints.__or__(QPainter.RenderHints f)'''
            return QPainter.RenderHints()
        def __or__(self, f):
            '''QPainter.RenderHints QPainter.RenderHints.__or__(int f)'''
            return QPainter.RenderHints()
        def __int__(self):
            '''int QPainter.RenderHints.__int__()'''
            return int()
        def __ixor__(self, f):
            '''QPainter.RenderHints QPainter.RenderHints.__ixor__(QPainter.RenderHints f)'''
            return QPainter.RenderHints()
        def __ior__(self, f):
            '''QPainter.RenderHints QPainter.RenderHints.__ior__(QPainter.RenderHints f)'''
            return QPainter.RenderHints()
        def __iand__(self, mask):
            '''QPainter.RenderHints QPainter.RenderHints.__iand__(int mask)'''
            return QPainter.RenderHints()


class QTextItem():
    """"""
    # Enum QTextItem.RenderFlag
    RightToLeft = 0
    Overline = 0
    Underline = 0
    StrikeOut = 0

    def __init__(self):
        '''void QTextItem.__init__()'''
    def __init__(self):
        '''QTextItem QTextItem.__init__()'''
        return QTextItem()
    def font(self):
        '''QFont QTextItem.font()'''
        return QFont()
    def text(self):
        '''str QTextItem.text()'''
        return str()
    def renderFlags(self):
        '''QTextItem.RenderFlags QTextItem.renderFlags()'''
        return QTextItem.RenderFlags()
    def width(self):
        '''float QTextItem.width()'''
        return float()
    def ascent(self):
        '''float QTextItem.ascent()'''
        return float()
    def descent(self):
        '''float QTextItem.descent()'''
        return float()
    class RenderFlags():
        """"""
        def __init__(self):
            '''QTextItem.RenderFlags QTextItem.RenderFlags.__init__()'''
            return QTextItem.RenderFlags()
        def __init__(self):
            '''int QTextItem.RenderFlags.__init__()'''
            return int()
        def __init__(self):
            '''void QTextItem.RenderFlags.__init__()'''
        def __bool__(self):
            '''int QTextItem.RenderFlags.__bool__()'''
            return int()
        def __ne__(self, f):
            '''bool QTextItem.RenderFlags.__ne__(QTextItem.RenderFlags f)'''
            return bool()
        def __eq__(self, f):
            '''bool QTextItem.RenderFlags.__eq__(QTextItem.RenderFlags f)'''
            return bool()
        def __invert__(self):
            '''QTextItem.RenderFlags QTextItem.RenderFlags.__invert__()'''
            return QTextItem.RenderFlags()
        def __and__(self, mask):
            '''QTextItem.RenderFlags QTextItem.RenderFlags.__and__(int mask)'''
            return QTextItem.RenderFlags()
        def __xor__(self, f):
            '''QTextItem.RenderFlags QTextItem.RenderFlags.__xor__(QTextItem.RenderFlags f)'''
            return QTextItem.RenderFlags()
        def __xor__(self, f):
            '''QTextItem.RenderFlags QTextItem.RenderFlags.__xor__(int f)'''
            return QTextItem.RenderFlags()
        def __or__(self, f):
            '''QTextItem.RenderFlags QTextItem.RenderFlags.__or__(QTextItem.RenderFlags f)'''
            return QTextItem.RenderFlags()
        def __or__(self, f):
            '''QTextItem.RenderFlags QTextItem.RenderFlags.__or__(int f)'''
            return QTextItem.RenderFlags()
        def __int__(self):
            '''int QTextItem.RenderFlags.__int__()'''
            return int()
        def __ixor__(self, f):
            '''QTextItem.RenderFlags QTextItem.RenderFlags.__ixor__(QTextItem.RenderFlags f)'''
            return QTextItem.RenderFlags()
        def __ior__(self, f):
            '''QTextItem.RenderFlags QTextItem.RenderFlags.__ior__(QTextItem.RenderFlags f)'''
            return QTextItem.RenderFlags()
        def __iand__(self, mask):
            '''QTextItem.RenderFlags QTextItem.RenderFlags.__iand__(int mask)'''
            return QTextItem.RenderFlags()


class QPaintEngine():
    """"""
    # Enum QPaintEngine.Type
    X11 = 0
    Windows = 0
    QuickDraw = 0
    CoreGraphics = 0
    MacPrinter = 0
    QWindowSystem = 0
    PostScript = 0
    OpenGL = 0
    Picture = 0
    SVG = 0
    Raster = 0
    Direct3D = 0
    Pdf = 0
    OpenVG = 0
    OpenGL2 = 0
    PaintBuffer = 0
    Blitter = 0
    Direct2D = 0
    User = 0
    MaxUser = 0

    # Enum QPaintEngine.PolygonDrawMode
    OddEvenMode = 0
    WindingMode = 0
    ConvexMode = 0
    PolylineMode = 0

    # Enum QPaintEngine.DirtyFlag
    DirtyPen = 0
    DirtyBrush = 0
    DirtyBrushOrigin = 0
    DirtyFont = 0
    DirtyBackground = 0
    DirtyBackgroundMode = 0
    DirtyTransform = 0
    DirtyClipRegion = 0
    DirtyClipPath = 0
    DirtyHints = 0
    DirtyCompositionMode = 0
    DirtyClipEnabled = 0
    DirtyOpacity = 0
    AllDirty = 0

    # Enum QPaintEngine.PaintEngineFeature
    PrimitiveTransform = 0
    PatternTransform = 0
    PixmapTransform = 0
    PatternBrush = 0
    LinearGradientFill = 0
    RadialGradientFill = 0
    ConicalGradientFill = 0
    AlphaBlend = 0
    PorterDuff = 0
    PainterPaths = 0
    Antialiasing = 0
    BrushStroke = 0
    ConstantOpacity = 0
    MaskedBrush = 0
    PaintOutsidePaintEvent = 0
    PerspectiveTransform = 0
    BlendModes = 0
    ObjectBoundingModeGradients = 0
    RasterOpModes = 0
    AllFeatures = 0

    def __init__(self, features = 0):
        '''void QPaintEngine.__init__(QPaintEngine.PaintEngineFeatures features = 0)'''
    def painter(self):
        '''QPainter QPaintEngine.painter()'''
        return QPainter()
    def hasFeature(self, feature):
        '''bool QPaintEngine.hasFeature(QPaintEngine.PaintEngineFeatures feature)'''
        return bool()
    def type(self):
        '''abstract QPaintEngine.Type QPaintEngine.type()'''
        return QPaintEngine.Type()
    def paintDevice(self):
        '''QPaintDevice QPaintEngine.paintDevice()'''
        return QPaintDevice()
    def setPaintDevice(self, device):
        '''void QPaintEngine.setPaintDevice(QPaintDevice device)'''
    def drawImage(self, r, pm, sr, flags = None):
        '''void QPaintEngine.drawImage(QRectF r, QImage pm, QRectF sr, Qt.ImageConversionFlags flags = Qt.AutoColor)'''
    def drawTiledPixmap(self, r, pixmap, s):
        '''void QPaintEngine.drawTiledPixmap(QRectF r, QPixmap pixmap, QPointF s)'''
    def drawTextItem(self, p, textItem):
        '''void QPaintEngine.drawTextItem(QPointF p, QTextItem textItem)'''
    def drawPixmap(self, r, pm, sr):
        '''abstract void QPaintEngine.drawPixmap(QRectF r, QPixmap pm, QRectF sr)'''
    def drawPolygon(self, points, mode):
        '''void QPaintEngine.drawPolygon(QPointF points, QPaintEngine.PolygonDrawMode mode)'''
    def drawPolygon(self, points, mode):
        '''void QPaintEngine.drawPolygon(QPoint points, QPaintEngine.PolygonDrawMode mode)'''
    def drawPoints(self, points):
        '''void QPaintEngine.drawPoints(QPointF points)'''
    def drawPoints(self, points):
        '''void QPaintEngine.drawPoints(QPoint points)'''
    def drawPath(self, path):
        '''void QPaintEngine.drawPath(QPainterPath path)'''
    def drawEllipse(self, r):
        '''void QPaintEngine.drawEllipse(QRectF r)'''
    def drawEllipse(self, r):
        '''void QPaintEngine.drawEllipse(QRect r)'''
    def drawLines(self, lines):
        '''void QPaintEngine.drawLines(QLine lines)'''
    def drawLines(self, lines):
        '''void QPaintEngine.drawLines(QLineF lines)'''
    def drawRects(self, rects):
        '''void QPaintEngine.drawRects(QRect rects)'''
    def drawRects(self, rects):
        '''void QPaintEngine.drawRects(QRectF rects)'''
    def updateState(self, state):
        '''abstract void QPaintEngine.updateState(QPaintEngineState state)'''
    def end(self):
        '''abstract bool QPaintEngine.end()'''
        return bool()
    def begin(self, pdev):
        '''abstract bool QPaintEngine.begin(QPaintDevice pdev)'''
        return bool()
    def setActive(self, newState):
        '''void QPaintEngine.setActive(bool newState)'''
    def isActive(self):
        '''bool QPaintEngine.isActive()'''
        return bool()
    class PaintEngineFeatures():
        """"""
        def __init__(self):
            '''QPaintEngine.PaintEngineFeatures QPaintEngine.PaintEngineFeatures.__init__()'''
            return QPaintEngine.PaintEngineFeatures()
        def __init__(self):
            '''int QPaintEngine.PaintEngineFeatures.__init__()'''
            return int()
        def __init__(self):
            '''void QPaintEngine.PaintEngineFeatures.__init__()'''
        def __bool__(self):
            '''int QPaintEngine.PaintEngineFeatures.__bool__()'''
            return int()
        def __ne__(self, f):
            '''bool QPaintEngine.PaintEngineFeatures.__ne__(QPaintEngine.PaintEngineFeatures f)'''
            return bool()
        def __eq__(self, f):
            '''bool QPaintEngine.PaintEngineFeatures.__eq__(QPaintEngine.PaintEngineFeatures f)'''
            return bool()
        def __invert__(self):
            '''QPaintEngine.PaintEngineFeatures QPaintEngine.PaintEngineFeatures.__invert__()'''
            return QPaintEngine.PaintEngineFeatures()
        def __and__(self, mask):
            '''QPaintEngine.PaintEngineFeatures QPaintEngine.PaintEngineFeatures.__and__(int mask)'''
            return QPaintEngine.PaintEngineFeatures()
        def __xor__(self, f):
            '''QPaintEngine.PaintEngineFeatures QPaintEngine.PaintEngineFeatures.__xor__(QPaintEngine.PaintEngineFeatures f)'''
            return QPaintEngine.PaintEngineFeatures()
        def __xor__(self, f):
            '''QPaintEngine.PaintEngineFeatures QPaintEngine.PaintEngineFeatures.__xor__(int f)'''
            return QPaintEngine.PaintEngineFeatures()
        def __or__(self, f):
            '''QPaintEngine.PaintEngineFeatures QPaintEngine.PaintEngineFeatures.__or__(QPaintEngine.PaintEngineFeatures f)'''
            return QPaintEngine.PaintEngineFeatures()
        def __or__(self, f):
            '''QPaintEngine.PaintEngineFeatures QPaintEngine.PaintEngineFeatures.__or__(int f)'''
            return QPaintEngine.PaintEngineFeatures()
        def __int__(self):
            '''int QPaintEngine.PaintEngineFeatures.__int__()'''
            return int()
        def __ixor__(self, f):
            '''QPaintEngine.PaintEngineFeatures QPaintEngine.PaintEngineFeatures.__ixor__(QPaintEngine.PaintEngineFeatures f)'''
            return QPaintEngine.PaintEngineFeatures()
        def __ior__(self, f):
            '''QPaintEngine.PaintEngineFeatures QPaintEngine.PaintEngineFeatures.__ior__(QPaintEngine.PaintEngineFeatures f)'''
            return QPaintEngine.PaintEngineFeatures()
        def __iand__(self, mask):
            '''QPaintEngine.PaintEngineFeatures QPaintEngine.PaintEngineFeatures.__iand__(int mask)'''
            return QPaintEngine.PaintEngineFeatures()
    class DirtyFlags():
        """"""
        def __init__(self):
            '''QPaintEngine.DirtyFlags QPaintEngine.DirtyFlags.__init__()'''
            return QPaintEngine.DirtyFlags()
        def __init__(self):
            '''int QPaintEngine.DirtyFlags.__init__()'''
            return int()
        def __init__(self):
            '''void QPaintEngine.DirtyFlags.__init__()'''
        def __bool__(self):
            '''int QPaintEngine.DirtyFlags.__bool__()'''
            return int()
        def __ne__(self, f):
            '''bool QPaintEngine.DirtyFlags.__ne__(QPaintEngine.DirtyFlags f)'''
            return bool()
        def __eq__(self, f):
            '''bool QPaintEngine.DirtyFlags.__eq__(QPaintEngine.DirtyFlags f)'''
            return bool()
        def __invert__(self):
            '''QPaintEngine.DirtyFlags QPaintEngine.DirtyFlags.__invert__()'''
            return QPaintEngine.DirtyFlags()
        def __and__(self, mask):
            '''QPaintEngine.DirtyFlags QPaintEngine.DirtyFlags.__and__(int mask)'''
            return QPaintEngine.DirtyFlags()
        def __xor__(self, f):
            '''QPaintEngine.DirtyFlags QPaintEngine.DirtyFlags.__xor__(QPaintEngine.DirtyFlags f)'''
            return QPaintEngine.DirtyFlags()
        def __xor__(self, f):
            '''QPaintEngine.DirtyFlags QPaintEngine.DirtyFlags.__xor__(int f)'''
            return QPaintEngine.DirtyFlags()
        def __or__(self, f):
            '''QPaintEngine.DirtyFlags QPaintEngine.DirtyFlags.__or__(QPaintEngine.DirtyFlags f)'''
            return QPaintEngine.DirtyFlags()
        def __or__(self, f):
            '''QPaintEngine.DirtyFlags QPaintEngine.DirtyFlags.__or__(int f)'''
            return QPaintEngine.DirtyFlags()
        def __int__(self):
            '''int QPaintEngine.DirtyFlags.__int__()'''
            return int()
        def __ixor__(self, f):
            '''QPaintEngine.DirtyFlags QPaintEngine.DirtyFlags.__ixor__(QPaintEngine.DirtyFlags f)'''
            return QPaintEngine.DirtyFlags()
        def __ior__(self, f):
            '''QPaintEngine.DirtyFlags QPaintEngine.DirtyFlags.__ior__(QPaintEngine.DirtyFlags f)'''
            return QPaintEngine.DirtyFlags()
        def __iand__(self, mask):
            '''QPaintEngine.DirtyFlags QPaintEngine.DirtyFlags.__iand__(int mask)'''
            return QPaintEngine.DirtyFlags()


class QPaintEngineState():
    """"""
    def __init__(self):
        '''void QPaintEngineState.__init__()'''
    def __init__(self):
        '''QPaintEngineState QPaintEngineState.__init__()'''
        return QPaintEngineState()
    def penNeedsResolving(self):
        '''bool QPaintEngineState.penNeedsResolving()'''
        return bool()
    def brushNeedsResolving(self):
        '''bool QPaintEngineState.brushNeedsResolving()'''
        return bool()
    def transform(self):
        '''QTransform QPaintEngineState.transform()'''
        return QTransform()
    def painter(self):
        '''QPainter QPaintEngineState.painter()'''
        return QPainter()
    def compositionMode(self):
        '''QPainter.CompositionMode QPaintEngineState.compositionMode()'''
        return QPainter.CompositionMode()
    def renderHints(self):
        '''QPainter.RenderHints QPaintEngineState.renderHints()'''
        return QPainter.RenderHints()
    def isClipEnabled(self):
        '''bool QPaintEngineState.isClipEnabled()'''
        return bool()
    def clipPath(self):
        '''QPainterPath QPaintEngineState.clipPath()'''
        return QPainterPath()
    def clipRegion(self):
        '''QRegion QPaintEngineState.clipRegion()'''
        return QRegion()
    def clipOperation(self):
        '''Qt.ClipOperation QPaintEngineState.clipOperation()'''
        return Qt.ClipOperation()
    def opacity(self):
        '''float QPaintEngineState.opacity()'''
        return float()
    def font(self):
        '''QFont QPaintEngineState.font()'''
        return QFont()
    def backgroundMode(self):
        '''Qt.BGMode QPaintEngineState.backgroundMode()'''
        return Qt.BGMode()
    def backgroundBrush(self):
        '''QBrush QPaintEngineState.backgroundBrush()'''
        return QBrush()
    def brushOrigin(self):
        '''QPointF QPaintEngineState.brushOrigin()'''
        return QPointF()
    def brush(self):
        '''QBrush QPaintEngineState.brush()'''
        return QBrush()
    def pen(self):
        '''QPen QPaintEngineState.pen()'''
        return QPen()
    def state(self):
        '''QPaintEngine.DirtyFlags QPaintEngineState.state()'''
        return QPaintEngine.DirtyFlags()


class QPainterPath():
    """"""
    # Enum QPainterPath.ElementType
    MoveToElement = 0
    LineToElement = 0
    CurveToElement = 0
    CurveToDataElement = 0

    def __init__(self):
        '''void QPainterPath.__init__()'''
    def __init__(self, startPoint):
        '''void QPainterPath.__init__(QPointF startPoint)'''
    def __init__(self, other):
        '''void QPainterPath.__init__(QPainterPath other)'''
    def __mul__(self, m):
        '''QPainterPath QPainterPath.__mul__(QTransform m)'''
        return QPainterPath()
    def swap(self, other):
        '''void QPainterPath.swap(QPainterPath other)'''
    def translated(self, dx, dy):
        '''QPainterPath QPainterPath.translated(float dx, float dy)'''
        return QPainterPath()
    def translated(self, offset):
        '''QPainterPath QPainterPath.translated(QPointF offset)'''
        return QPainterPath()
    def translate(self, dx, dy):
        '''void QPainterPath.translate(float dx, float dy)'''
    def translate(self, offset):
        '''void QPainterPath.translate(QPointF offset)'''
    def __isub__(self, other):
        '''QPainterPath QPainterPath.__isub__(QPainterPath other)'''
        return QPainterPath()
    def __iadd__(self, other):
        '''QPainterPath QPainterPath.__iadd__(QPainterPath other)'''
        return QPainterPath()
    def __ior__(self, other):
        '''QPainterPath QPainterPath.__ior__(QPainterPath other)'''
        return QPainterPath()
    def __iand__(self, other):
        '''QPainterPath QPainterPath.__iand__(QPainterPath other)'''
        return QPainterPath()
    def __sub__(self, other):
        '''QPainterPath QPainterPath.__sub__(QPainterPath other)'''
        return QPainterPath()
    def __add__(self, other):
        '''QPainterPath QPainterPath.__add__(QPainterPath other)'''
        return QPainterPath()
    def __or__(self, other):
        '''QPainterPath QPainterPath.__or__(QPainterPath other)'''
        return QPainterPath()
    def __and__(self, other):
        '''QPainterPath QPainterPath.__and__(QPainterPath other)'''
        return QPainterPath()
    def simplified(self):
        '''QPainterPath QPainterPath.simplified()'''
        return QPainterPath()
    def addRoundedRect(self, rect, xRadius, yRadius, mode = None):
        '''void QPainterPath.addRoundedRect(QRectF rect, float xRadius, float yRadius, Qt.SizeMode mode = Qt.AbsoluteSize)'''
    def addRoundedRect(self, x, y, w, h, xRadius, yRadius, mode = None):
        '''void QPainterPath.addRoundedRect(float x, float y, float w, float h, float xRadius, float yRadius, Qt.SizeMode mode = Qt.AbsoluteSize)'''
    def subtracted(self, r):
        '''QPainterPath QPainterPath.subtracted(QPainterPath r)'''
        return QPainterPath()
    def intersected(self, r):
        '''QPainterPath QPainterPath.intersected(QPainterPath r)'''
        return QPainterPath()
    def united(self, r):
        '''QPainterPath QPainterPath.united(QPainterPath r)'''
        return QPainterPath()
    def slopeAtPercent(self, t):
        '''float QPainterPath.slopeAtPercent(float t)'''
        return float()
    def angleAtPercent(self, t):
        '''float QPainterPath.angleAtPercent(float t)'''
        return float()
    def pointAtPercent(self, t):
        '''QPointF QPainterPath.pointAtPercent(float t)'''
        return QPointF()
    def percentAtLength(self, t):
        '''float QPainterPath.percentAtLength(float t)'''
        return float()
    def length(self):
        '''float QPainterPath.length()'''
        return float()
    def toFillPolygon(self, matrix):
        '''QPolygonF QPainterPath.toFillPolygon(QTransform matrix)'''
        return QPolygonF()
    def toFillPolygons(self, matrix):
        '''list-of-QPolygonF QPainterPath.toFillPolygons(QTransform matrix)'''
        return [QPolygonF()]
    def toSubpathPolygons(self, matrix):
        '''list-of-QPolygonF QPainterPath.toSubpathPolygons(QTransform matrix)'''
        return [QPolygonF()]
    def setElementPositionAt(self, i, x, y):
        '''void QPainterPath.setElementPositionAt(int i, float x, float y)'''
    def elementAt(self, i):
        '''QPainterPath.Element QPainterPath.elementAt(int i)'''
        return QPainterPath.Element()
    def elementCount(self):
        '''int QPainterPath.elementCount()'''
        return int()
    def isEmpty(self):
        '''bool QPainterPath.isEmpty()'''
        return bool()
    def arcMoveTo(self, rect, angle):
        '''void QPainterPath.arcMoveTo(QRectF rect, float angle)'''
    def arcMoveTo(self, x, y, w, h, angle):
        '''void QPainterPath.arcMoveTo(float x, float y, float w, float h, float angle)'''
    def __ne__(self, other):
        '''bool QPainterPath.__ne__(QPainterPath other)'''
        return bool()
    def __eq__(self, other):
        '''bool QPainterPath.__eq__(QPainterPath other)'''
        return bool()
    def toReversed(self):
        '''QPainterPath QPainterPath.toReversed()'''
        return QPainterPath()
    def setFillRule(self, fillRule):
        '''void QPainterPath.setFillRule(Qt.FillRule fillRule)'''
    def fillRule(self):
        '''Qt.FillRule QPainterPath.fillRule()'''
        return Qt.FillRule()
    def controlPointRect(self):
        '''QRectF QPainterPath.controlPointRect()'''
        return QRectF()
    def boundingRect(self):
        '''QRectF QPainterPath.boundingRect()'''
        return QRectF()
    def intersects(self, rect):
        '''bool QPainterPath.intersects(QRectF rect)'''
        return bool()
    def intersects(self, p):
        '''bool QPainterPath.intersects(QPainterPath p)'''
        return bool()
    def contains(self, pt):
        '''bool QPainterPath.contains(QPointF pt)'''
        return bool()
    def contains(self, rect):
        '''bool QPainterPath.contains(QRectF rect)'''
        return bool()
    def contains(self, p):
        '''bool QPainterPath.contains(QPainterPath p)'''
        return bool()
    def connectPath(self, path):
        '''void QPainterPath.connectPath(QPainterPath path)'''
    def addRegion(self, region):
        '''void QPainterPath.addRegion(QRegion region)'''
    def addPath(self, path):
        '''void QPainterPath.addPath(QPainterPath path)'''
    def addText(self, point, f, text):
        '''void QPainterPath.addText(QPointF point, QFont f, str text)'''
    def addText(self, x, y, f, text):
        '''void QPainterPath.addText(float x, float y, QFont f, str text)'''
    def addPolygon(self, polygon):
        '''void QPainterPath.addPolygon(QPolygonF polygon)'''
    def addEllipse(self, rect):
        '''void QPainterPath.addEllipse(QRectF rect)'''
    def addEllipse(self, x, y, w, h):
        '''void QPainterPath.addEllipse(float x, float y, float w, float h)'''
    def addEllipse(self, center, rx, ry):
        '''void QPainterPath.addEllipse(QPointF center, float rx, float ry)'''
    def addRect(self, rect):
        '''void QPainterPath.addRect(QRectF rect)'''
    def addRect(self, x, y, w, h):
        '''void QPainterPath.addRect(float x, float y, float w, float h)'''
    def currentPosition(self):
        '''QPointF QPainterPath.currentPosition()'''
        return QPointF()
    def quadTo(self, ctrlPt, endPt):
        '''void QPainterPath.quadTo(QPointF ctrlPt, QPointF endPt)'''
    def quadTo(self, ctrlPtx, ctrlPty, endPtx, endPty):
        '''void QPainterPath.quadTo(float ctrlPtx, float ctrlPty, float endPtx, float endPty)'''
    def cubicTo(self, ctrlPt1, ctrlPt2, endPt):
        '''void QPainterPath.cubicTo(QPointF ctrlPt1, QPointF ctrlPt2, QPointF endPt)'''
    def cubicTo(self, ctrlPt1x, ctrlPt1y, ctrlPt2x, ctrlPt2y, endPtx, endPty):
        '''void QPainterPath.cubicTo(float ctrlPt1x, float ctrlPt1y, float ctrlPt2x, float ctrlPt2y, float endPtx, float endPty)'''
    def arcTo(self, rect, startAngle, arcLength):
        '''void QPainterPath.arcTo(QRectF rect, float startAngle, float arcLength)'''
    def arcTo(self, x, y, w, h, startAngle, arcLenght):
        '''void QPainterPath.arcTo(float x, float y, float w, float h, float startAngle, float arcLenght)'''
    def lineTo(self, p):
        '''void QPainterPath.lineTo(QPointF p)'''
    def lineTo(self, x, y):
        '''void QPainterPath.lineTo(float x, float y)'''
    def moveTo(self, p):
        '''void QPainterPath.moveTo(QPointF p)'''
    def moveTo(self, x, y):
        '''void QPainterPath.moveTo(float x, float y)'''
    def closeSubpath(self):
        '''void QPainterPath.closeSubpath()'''
    class Element():
        """"""
        type = None # QPainterPath.ElementType - member
        x = None # float - member
        y = None # float - member
        def __init__(self):
            '''void QPainterPath.Element.__init__()'''
        def __init__(self):
            '''QPainterPath.Element QPainterPath.Element.__init__()'''
            return QPainterPath.Element()
        def __ne__(self, e):
            '''bool QPainterPath.Element.__ne__(QPainterPath.Element e)'''
            return bool()
        def __eq__(self, e):
            '''bool QPainterPath.Element.__eq__(QPainterPath.Element e)'''
            return bool()
        def isCurveTo(self):
            '''bool QPainterPath.Element.isCurveTo()'''
            return bool()
        def isLineTo(self):
            '''bool QPainterPath.Element.isLineTo()'''
            return bool()
        def isMoveTo(self):
            '''bool QPainterPath.Element.isMoveTo()'''
            return bool()


class QPainterPathStroker():
    """"""
    def __init__(self):
        '''void QPainterPathStroker.__init__()'''
    def __init__(self, pen):
        '''void QPainterPathStroker.__init__(QPen pen)'''
    def dashOffset(self):
        '''float QPainterPathStroker.dashOffset()'''
        return float()
    def setDashOffset(self, offset):
        '''void QPainterPathStroker.setDashOffset(float offset)'''
    def createStroke(self, path):
        '''QPainterPath QPainterPathStroker.createStroke(QPainterPath path)'''
        return QPainterPath()
    def dashPattern(self):
        '''list-of-float QPainterPathStroker.dashPattern()'''
        return [float()]
    def setDashPattern(self):
        '''Qt.PenStyle QPainterPathStroker.setDashPattern()'''
        return Qt.PenStyle()
    def setDashPattern(self, dashPattern):
        '''void QPainterPathStroker.setDashPattern(list-of-float dashPattern)'''
    def curveThreshold(self):
        '''float QPainterPathStroker.curveThreshold()'''
        return float()
    def setCurveThreshold(self, threshold):
        '''void QPainterPathStroker.setCurveThreshold(float threshold)'''
    def miterLimit(self):
        '''float QPainterPathStroker.miterLimit()'''
        return float()
    def setMiterLimit(self, length):
        '''void QPainterPathStroker.setMiterLimit(float length)'''
    def joinStyle(self):
        '''Qt.PenJoinStyle QPainterPathStroker.joinStyle()'''
        return Qt.PenJoinStyle()
    def setJoinStyle(self, style):
        '''void QPainterPathStroker.setJoinStyle(Qt.PenJoinStyle style)'''
    def capStyle(self):
        '''Qt.PenCapStyle QPainterPathStroker.capStyle()'''
        return Qt.PenCapStyle()
    def setCapStyle(self, style):
        '''void QPainterPathStroker.setCapStyle(Qt.PenCapStyle style)'''
    def width(self):
        '''float QPainterPathStroker.width()'''
        return float()
    def setWidth(self, width):
        '''void QPainterPathStroker.setWidth(float width)'''


class QPalette():
    """"""
    # Enum QPalette.ColorRole
    WindowText = 0
    Foreground = 0
    Button = 0
    Light = 0
    Midlight = 0
    Dark = 0
    Mid = 0
    Text = 0
    BrightText = 0
    ButtonText = 0
    Base = 0
    Window = 0
    Background = 0
    Shadow = 0
    Highlight = 0
    HighlightedText = 0
    Link = 0
    LinkVisited = 0
    AlternateBase = 0
    ToolTipBase = 0
    ToolTipText = 0
    NColorRoles = 0
    NoRole = 0

    # Enum QPalette.ColorGroup
    Active = 0
    Disabled = 0
    Inactive = 0
    NColorGroups = 0
    Current = 0
    All = 0
    Normal = 0

    def __init__(self):
        '''void QPalette.__init__()'''
    def __init__(self, button):
        '''void QPalette.__init__(QColor button)'''
    def __init__(self, button):
        '''void QPalette.__init__(Qt.GlobalColor button)'''
    def __init__(self, button, background):
        '''void QPalette.__init__(QColor button, QColor background)'''
    def __init__(self, foreground, button, light, dark, mid, text, bright_text, base, background):
        '''void QPalette.__init__(QBrush foreground, QBrush button, QBrush light, QBrush dark, QBrush mid, QBrush text, QBrush bright_text, QBrush base, QBrush background)'''
    def __init__(self, palette):
        '''void QPalette.__init__(QPalette palette)'''
    def __init__(self, variant):
        '''void QPalette.__init__(QVariant variant)'''
    def swap(self, other):
        '''void QPalette.swap(QPalette other)'''
    def cacheKey(self):
        '''int QPalette.cacheKey()'''
        return int()
    def isBrushSet(self, cg, cr):
        '''bool QPalette.isBrushSet(QPalette.ColorGroup cg, QPalette.ColorRole cr)'''
        return bool()
    def setColor(self, acg, acr, acolor):
        '''void QPalette.setColor(QPalette.ColorGroup acg, QPalette.ColorRole acr, QColor acolor)'''
    def setColor(self, acr, acolor):
        '''void QPalette.setColor(QPalette.ColorRole acr, QColor acolor)'''
    def resolve(self):
        '''QPalette QPalette.resolve()'''
        return QPalette()
    def resolve(self):
        '''int QPalette.resolve()'''
        return int()
    def resolve(self, mask):
        '''void QPalette.resolve(int mask)'''
    def isCopyOf(self, p):
        '''bool QPalette.isCopyOf(QPalette p)'''
        return bool()
    def __ne__(self, p):
        '''bool QPalette.__ne__(QPalette p)'''
        return bool()
    def __eq__(self, p):
        '''bool QPalette.__eq__(QPalette p)'''
        return bool()
    def toolTipText(self):
        '''QBrush QPalette.toolTipText()'''
        return QBrush()
    def toolTipBase(self):
        '''QBrush QPalette.toolTipBase()'''
        return QBrush()
    def linkVisited(self):
        '''QBrush QPalette.linkVisited()'''
        return QBrush()
    def link(self):
        '''QBrush QPalette.link()'''
        return QBrush()
    def highlightedText(self):
        '''QBrush QPalette.highlightedText()'''
        return QBrush()
    def highlight(self):
        '''QBrush QPalette.highlight()'''
        return QBrush()
    def shadow(self):
        '''QBrush QPalette.shadow()'''
        return QBrush()
    def buttonText(self):
        '''QBrush QPalette.buttonText()'''
        return QBrush()
    def brightText(self):
        '''QBrush QPalette.brightText()'''
        return QBrush()
    def midlight(self):
        '''QBrush QPalette.midlight()'''
        return QBrush()
    def window(self):
        '''QBrush QPalette.window()'''
        return QBrush()
    def alternateBase(self):
        '''QBrush QPalette.alternateBase()'''
        return QBrush()
    def base(self):
        '''QBrush QPalette.base()'''
        return QBrush()
    def text(self):
        '''QBrush QPalette.text()'''
        return QBrush()
    def mid(self):
        '''QBrush QPalette.mid()'''
        return QBrush()
    def dark(self):
        '''QBrush QPalette.dark()'''
        return QBrush()
    def light(self):
        '''QBrush QPalette.light()'''
        return QBrush()
    def button(self):
        '''QBrush QPalette.button()'''
        return QBrush()
    def windowText(self):
        '''QBrush QPalette.windowText()'''
        return QBrush()
    def isEqual(self, cr1, cr2):
        '''bool QPalette.isEqual(QPalette.ColorGroup cr1, QPalette.ColorGroup cr2)'''
        return bool()
    def setColorGroup(self, cr, foreground, button, light, dark, mid, text, bright_text, base, background):
        '''void QPalette.setColorGroup(QPalette.ColorGroup cr, QBrush foreground, QBrush button, QBrush light, QBrush dark, QBrush mid, QBrush text, QBrush bright_text, QBrush base, QBrush background)'''
    def setBrush(self, cg, cr, brush):
        '''void QPalette.setBrush(QPalette.ColorGroup cg, QPalette.ColorRole cr, QBrush brush)'''
    def setBrush(self, acr, abrush):
        '''void QPalette.setBrush(QPalette.ColorRole acr, QBrush abrush)'''
    def brush(self, cg, cr):
        '''QBrush QPalette.brush(QPalette.ColorGroup cg, QPalette.ColorRole cr)'''
        return QBrush()
    def brush(self, cr):
        '''QBrush QPalette.brush(QPalette.ColorRole cr)'''
        return QBrush()
    def color(self, cg, cr):
        '''QColor QPalette.color(QPalette.ColorGroup cg, QPalette.ColorRole cr)'''
        return QColor()
    def color(self, cr):
        '''QColor QPalette.color(QPalette.ColorRole cr)'''
        return QColor()
    def setCurrentColorGroup(self, cg):
        '''void QPalette.setCurrentColorGroup(QPalette.ColorGroup cg)'''
    def currentColorGroup(self):
        '''QPalette.ColorGroup QPalette.currentColorGroup()'''
        return QPalette.ColorGroup()


class QPdfWriter(QObject, QPagedPaintDevice):
    """"""
    def __init__(self, filename):
        '''void QPdfWriter.__init__(str filename)'''
    def __init__(self, device):
        '''void QPdfWriter.__init__(QIODevice device)'''
    def resolution(self):
        '''int QPdfWriter.resolution()'''
        return int()
    def setResolution(self, resolution):
        '''void QPdfWriter.setResolution(int resolution)'''
    def metric(self, id):
        '''int QPdfWriter.metric(QPaintDevice.PaintDeviceMetric id)'''
        return int()
    def paintEngine(self):
        '''QPaintEngine QPdfWriter.paintEngine()'''
        return QPaintEngine()
    def setMargins(self, m):
        '''void QPdfWriter.setMargins(QPagedPaintDevice.Margins m)'''
    def setPageSizeMM(self, size):
        '''void QPdfWriter.setPageSizeMM(QSizeF size)'''
    def setPageSize(self, size):
        '''void QPdfWriter.setPageSize(QPagedPaintDevice.PageSize size)'''
    def newPage(self):
        '''bool QPdfWriter.newPage()'''
        return bool()
    def setCreator(self, creator):
        '''void QPdfWriter.setCreator(str creator)'''
    def creator(self):
        '''str QPdfWriter.creator()'''
        return str()
    def setTitle(self, title):
        '''void QPdfWriter.setTitle(str title)'''
    def title(self):
        '''str QPdfWriter.title()'''
        return str()


class QPen():
    """"""
    def __init__(self):
        '''void QPen.__init__()'''
    def __init__(self):
        '''Qt.PenStyle QPen.__init__()'''
        return Qt.PenStyle()
    def __init__(self, color):
        '''void QPen.__init__(QColor color)'''
    def __init__(self, brush, width, style = None, cap = None, join = None):
        '''void QPen.__init__(QBrush brush, float width, Qt.PenStyle style = Qt.SolidLine, Qt.PenCapStyle cap = Qt.SquareCap, Qt.PenJoinStyle join = Qt.BevelJoin)'''
    def __init__(self, pen):
        '''void QPen.__init__(QPen pen)'''
    def __init__(self, variant):
        '''void QPen.__init__(QVariant variant)'''
    def swap(self, other):
        '''void QPen.swap(QPen other)'''
    def setCosmetic(self, cosmetic):
        '''void QPen.setCosmetic(bool cosmetic)'''
    def isCosmetic(self):
        '''bool QPen.isCosmetic()'''
        return bool()
    def setDashOffset(self, doffset):
        '''void QPen.setDashOffset(float doffset)'''
    def dashOffset(self):
        '''float QPen.dashOffset()'''
        return float()
    def __ne__(self, p):
        '''bool QPen.__ne__(QPen p)'''
        return bool()
    def __eq__(self, p):
        '''bool QPen.__eq__(QPen p)'''
        return bool()
    def setMiterLimit(self, limit):
        '''void QPen.setMiterLimit(float limit)'''
    def miterLimit(self):
        '''float QPen.miterLimit()'''
        return float()
    def setDashPattern(self, pattern):
        '''void QPen.setDashPattern(list-of-float pattern)'''
    def dashPattern(self):
        '''list-of-float QPen.dashPattern()'''
        return [float()]
    def setJoinStyle(self, pcs):
        '''void QPen.setJoinStyle(Qt.PenJoinStyle pcs)'''
    def joinStyle(self):
        '''Qt.PenJoinStyle QPen.joinStyle()'''
        return Qt.PenJoinStyle()
    def setCapStyle(self, pcs):
        '''void QPen.setCapStyle(Qt.PenCapStyle pcs)'''
    def capStyle(self):
        '''Qt.PenCapStyle QPen.capStyle()'''
        return Qt.PenCapStyle()
    def isSolid(self):
        '''bool QPen.isSolid()'''
        return bool()
    def setBrush(self, brush):
        '''void QPen.setBrush(QBrush brush)'''
    def brush(self):
        '''QBrush QPen.brush()'''
        return QBrush()
    def setColor(self, color):
        '''void QPen.setColor(QColor color)'''
    def color(self):
        '''QColor QPen.color()'''
        return QColor()
    def setWidth(self, width):
        '''void QPen.setWidth(int width)'''
    def width(self):
        '''int QPen.width()'''
        return int()
    def setWidthF(self, width):
        '''void QPen.setWidthF(float width)'''
    def widthF(self):
        '''float QPen.widthF()'''
        return float()
    def setStyle(self):
        '''Qt.PenStyle QPen.setStyle()'''
        return Qt.PenStyle()
    def style(self):
        '''Qt.PenStyle QPen.style()'''
        return Qt.PenStyle()


class QPicture(QPaintDevice):
    """"""
    def __init__(self, formatVersion = None):
        '''void QPicture.__init__(int formatVersion = -1)'''
    def __init__(self):
        '''QPicture QPicture.__init__()'''
        return QPicture()
    def swap(self, other):
        '''void QPicture.swap(QPicture other)'''
    def metric(self, m):
        '''int QPicture.metric(QPaintDevice.PaintDeviceMetric m)'''
        return int()
    def paintEngine(self):
        '''QPaintEngine QPicture.paintEngine()'''
        return QPaintEngine()
    def isDetached(self):
        '''bool QPicture.isDetached()'''
        return bool()
    def detach(self):
        '''void QPicture.detach()'''
    def setBoundingRect(self, r):
        '''void QPicture.setBoundingRect(QRect r)'''
    def boundingRect(self):
        '''QRect QPicture.boundingRect()'''
        return QRect()
    def save(self, dev, format = None):
        '''bool QPicture.save(QIODevice dev, str format = None)'''
        return bool()
    def save(self, fileName, format = None):
        '''bool QPicture.save(str fileName, str format = None)'''
        return bool()
    def load(self, dev, format = None):
        '''bool QPicture.load(QIODevice dev, str format = None)'''
        return bool()
    def load(self, fileName, format = None):
        '''bool QPicture.load(str fileName, str format = None)'''
        return bool()
    def play(self, p):
        '''bool QPicture.play(QPainter p)'''
        return bool()
    def setData(self, data):
        '''void QPicture.setData(str data)'''
    def data(self):
        '''str QPicture.data()'''
        return str()
    def size(self):
        '''int QPicture.size()'''
        return int()
    def devType(self):
        '''int QPicture.devType()'''
        return int()
    def isNull(self):
        '''bool QPicture.isNull()'''
        return bool()


class QPictureIO():
    """"""
    def __init__(self):
        '''void QPictureIO.__init__()'''
    def __init__(self, ioDevice, format):
        '''void QPictureIO.__init__(QIODevice ioDevice, str format)'''
    def __init__(self, fileName, format):
        '''void QPictureIO.__init__(str fileName, str format)'''
    def defineIOHandler(self, format, header, flags, read_picture, write_picture):
        '''static void QPictureIO.defineIOHandler(str format, str header, str flags, callable read_picture, callable write_picture)'''
    def outputFormats(self):
        '''static list-of-QByteArray QPictureIO.outputFormats()'''
        return [QByteArray()]
    def inputFormats(self):
        '''static list-of-QByteArray QPictureIO.inputFormats()'''
        return [QByteArray()]
    def pictureFormat(self, fileName):
        '''static QByteArray QPictureIO.pictureFormat(str fileName)'''
        return QByteArray()
    def pictureFormat(self):
        '''static QIODevice QPictureIO.pictureFormat()'''
        return QIODevice()
    def write(self):
        '''bool QPictureIO.write()'''
        return bool()
    def read(self):
        '''bool QPictureIO.read()'''
        return bool()
    def setGamma(self):
        '''float QPictureIO.setGamma()'''
        return float()
    def setParameters(self):
        '''str QPictureIO.setParameters()'''
        return str()
    def setDescription(self):
        '''str QPictureIO.setDescription()'''
        return str()
    def setQuality(self):
        '''int QPictureIO.setQuality()'''
        return int()
    def setFileName(self):
        '''str QPictureIO.setFileName()'''
        return str()
    def setIODevice(self):
        '''QIODevice QPictureIO.setIODevice()'''
        return QIODevice()
    def setFormat(self):
        '''str QPictureIO.setFormat()'''
        return str()
    def setStatus(self):
        '''int QPictureIO.setStatus()'''
        return int()
    def setPicture(self):
        '''QPicture QPictureIO.setPicture()'''
        return QPicture()
    def gamma(self):
        '''float QPictureIO.gamma()'''
        return float()
    def parameters(self):
        '''str QPictureIO.parameters()'''
        return str()
    def description(self):
        '''str QPictureIO.description()'''
        return str()
    def quality(self):
        '''int QPictureIO.quality()'''
        return int()
    def fileName(self):
        '''str QPictureIO.fileName()'''
        return str()
    def ioDevice(self):
        '''QIODevice QPictureIO.ioDevice()'''
        return QIODevice()
    def format(self):
        '''str QPictureIO.format()'''
        return str()
    def status(self):
        '''int QPictureIO.status()'''
        return int()
    def picture(self):
        '''QPicture QPictureIO.picture()'''
        return QPicture()


class QPixelFormat():
    """"""
    # Enum QPixelFormat.ByteOrder
    LittleEndian = 0
    BigEndian = 0
    CurrentSystemEndian = 0

    # Enum QPixelFormat.YUVLayout
    YUV444 = 0
    YUV422 = 0
    YUV411 = 0
    YUV420P = 0
    YUV420SP = 0
    YV12 = 0
    UYVY = 0
    YUYV = 0
    NV12 = 0
    NV21 = 0
    IMC1 = 0
    IMC2 = 0
    IMC3 = 0
    IMC4 = 0
    Y8 = 0
    Y16 = 0

    # Enum QPixelFormat.TypeInterpretation
    UnsignedInteger = 0
    UnsignedShort = 0
    UnsignedByte = 0
    FloatingPoint = 0

    # Enum QPixelFormat.AlphaPremultiplied
    NotPremultiplied = 0
    Premultiplied = 0

    # Enum QPixelFormat.AlphaPosition
    AtBeginning = 0
    AtEnd = 0

    # Enum QPixelFormat.AlphaUsage
    UsesAlpha = 0
    IgnoresAlpha = 0

    # Enum QPixelFormat.ColorModel
    RGB = 0
    BGR = 0
    Indexed = 0
    Grayscale = 0
    CMYK = 0
    HSL = 0
    HSV = 0
    YUV = 0
    Alpha = 0

    def __init__(self):
        '''void QPixelFormat.__init__()'''
    def __init__(self, mdl, firstSize, secondSize, thirdSize, fourthSize, fifthSize, alfa, usage, position, premult, typeInterp, byteOrder = None, subEnum = 0):
        '''void QPixelFormat.__init__(QPixelFormat.ColorModel mdl, int firstSize, int secondSize, int thirdSize, int fourthSize, int fifthSize, int alfa, QPixelFormat.AlphaUsage usage, QPixelFormat.AlphaPosition position, QPixelFormat.AlphaPremultiplied premult, QPixelFormat.TypeInterpretation typeInterp, QPixelFormat.ByteOrder byteOrder = QPixelFormat.CurrentSystemEndian, int subEnum = 0)'''
    def __init__(self):
        '''QPixelFormat QPixelFormat.__init__()'''
        return QPixelFormat()
    def __eq__(self, fmt2):
        '''bool QPixelFormat.__eq__(QPixelFormat fmt2)'''
        return bool()
    def __ne__(self, fmt2):
        '''bool QPixelFormat.__ne__(QPixelFormat fmt2)'''
        return bool()
    def subEnum(self):
        '''int QPixelFormat.subEnum()'''
        return int()
    def yuvLayout(self):
        '''QPixelFormat.YUVLayout QPixelFormat.yuvLayout()'''
        return QPixelFormat.YUVLayout()
    def byteOrder(self):
        '''QPixelFormat.ByteOrder QPixelFormat.byteOrder()'''
        return QPixelFormat.ByteOrder()
    def typeInterpretation(self):
        '''QPixelFormat.TypeInterpretation QPixelFormat.typeInterpretation()'''
        return QPixelFormat.TypeInterpretation()
    def premultiplied(self):
        '''QPixelFormat.AlphaPremultiplied QPixelFormat.premultiplied()'''
        return QPixelFormat.AlphaPremultiplied()
    def alphaPosition(self):
        '''QPixelFormat.AlphaPosition QPixelFormat.alphaPosition()'''
        return QPixelFormat.AlphaPosition()
    def alphaUsage(self):
        '''QPixelFormat.AlphaUsage QPixelFormat.alphaUsage()'''
        return QPixelFormat.AlphaUsage()
    def bitsPerPixel(self):
        '''int QPixelFormat.bitsPerPixel()'''
        return int()
    def alphaSize(self):
        '''int QPixelFormat.alphaSize()'''
        return int()
    def brightnessSize(self):
        '''int QPixelFormat.brightnessSize()'''
        return int()
    def lightnessSize(self):
        '''int QPixelFormat.lightnessSize()'''
        return int()
    def saturationSize(self):
        '''int QPixelFormat.saturationSize()'''
        return int()
    def hueSize(self):
        '''int QPixelFormat.hueSize()'''
        return int()
    def blackSize(self):
        '''int QPixelFormat.blackSize()'''
        return int()
    def yellowSize(self):
        '''int QPixelFormat.yellowSize()'''
        return int()
    def magentaSize(self):
        '''int QPixelFormat.magentaSize()'''
        return int()
    def cyanSize(self):
        '''int QPixelFormat.cyanSize()'''
        return int()
    def blueSize(self):
        '''int QPixelFormat.blueSize()'''
        return int()
    def greenSize(self):
        '''int QPixelFormat.greenSize()'''
        return int()
    def redSize(self):
        '''int QPixelFormat.redSize()'''
        return int()
    def channelCount(self):
        '''int QPixelFormat.channelCount()'''
        return int()
    def colorModel(self):
        '''QPixelFormat.ColorModel QPixelFormat.colorModel()'''
        return QPixelFormat.ColorModel()


class QPixmapCache():
    """"""
    def __init__(self):
        '''void QPixmapCache.__init__()'''
    def __init__(self):
        '''QPixmapCache QPixmapCache.__init__()'''
        return QPixmapCache()
    def setCacheLimit(self):
        '''static int QPixmapCache.setCacheLimit()'''
        return int()
    def replace(self, key, pixmap):
        '''static bool QPixmapCache.replace(QPixmapCache.Key key, QPixmap pixmap)'''
        return bool()
    def remove(self, key):
        '''static void QPixmapCache.remove(str key)'''
    def remove(self, key):
        '''static void QPixmapCache.remove(QPixmapCache.Key key)'''
    def insert(self, key):
        '''static QPixmap QPixmapCache.insert(str key)'''
        return QPixmap()
    def insert(self, pixmap):
        '''static QPixmapCache.Key QPixmapCache.insert(QPixmap pixmap)'''
        return QPixmapCache.Key()
    def find(self, key):
        '''static QPixmap QPixmapCache.find(str key)'''
        return QPixmap()
    def find(self, key):
        '''static QPixmap QPixmapCache.find(QPixmapCache.Key key)'''
        return QPixmap()
    def clear(self):
        '''static void QPixmapCache.clear()'''
    def cacheLimit(self):
        '''static int QPixmapCache.cacheLimit()'''
        return int()
    class Key():
        """"""
        def __init__(self):
            '''void QPixmapCache.Key.__init__()'''
        def __init__(self, other):
            '''void QPixmapCache.Key.__init__(QPixmapCache.Key other)'''
        def __ne__(self, key):
            '''bool QPixmapCache.Key.__ne__(QPixmapCache.Key key)'''
            return bool()
        def __eq__(self, key):
            '''bool QPixmapCache.Key.__eq__(QPixmapCache.Key key)'''
            return bool()


class QPolygon():
    """"""
    def __init__(self):
        '''void QPolygon.__init__()'''
    def __init__(self, a):
        '''void QPolygon.__init__(QPolygon a)'''
    def __init__(self, v):
        '''void QPolygon.__init__(list-of-QPoint v)'''
    def __init__(self, rectangle, closed = False):
        '''void QPolygon.__init__(QRect rectangle, bool closed = False)'''
    def __init__(self, asize):
        '''void QPolygon.__init__(int asize)'''
    def __init__(self, points):
        '''void QPolygon.__init__(list-of-int points)'''
    def __init__(self, variant):
        '''void QPolygon.__init__(QVariant variant)'''
    def __mul__(self, m):
        '''QPolygon QPolygon.__mul__(QTransform m)'''
        return QPolygon()
    def swap(self, other):
        '''void QPolygon.swap(QPolygon other)'''
    def __contains__(self, value):
        '''int QPolygon.__contains__(QPoint value)'''
        return int()
    def __delitem__(self, i):
        '''void QPolygon.__delitem__(int i)'''
    def __delitem__(self, slice):
        '''void QPolygon.__delitem__(slice slice)'''
    def __setitem__(self, i, value):
        '''void QPolygon.__setitem__(int i, QPoint value)'''
    def __setitem__(self, slice, list):
        '''void QPolygon.__setitem__(slice slice, QPolygon list)'''
    def __getitem__(self, i):
        '''QPoint QPolygon.__getitem__(int i)'''
        return QPoint()
    def __getitem__(self, slice):
        '''QPolygon QPolygon.__getitem__(slice slice)'''
        return QPolygon()
    def __lshift__(self, value):
        '''object QPolygon.__lshift__(QPoint value)'''
        return object()
    def __eq__(self, other):
        '''bool QPolygon.__eq__(QPolygon other)'''
        return bool()
    def __iadd__(self, other):
        '''QPolygon QPolygon.__iadd__(QPolygon other)'''
        return QPolygon()
    def __iadd__(self, value):
        '''QPolygon QPolygon.__iadd__(QPoint value)'''
        return QPolygon()
    def __add__(self, other):
        '''QPolygon QPolygon.__add__(QPolygon other)'''
        return QPolygon()
    def __ne__(self, other):
        '''bool QPolygon.__ne__(QPolygon other)'''
        return bool()
    def value(self, i):
        '''QPoint QPolygon.value(int i)'''
        return QPoint()
    def value(self, i, defaultValue):
        '''QPoint QPolygon.value(int i, QPoint defaultValue)'''
        return QPoint()
    def size(self):
        '''int QPolygon.size()'''
        return int()
    def replace(self, i, value):
        '''void QPolygon.replace(int i, QPoint value)'''
    def remove(self, i):
        '''void QPolygon.remove(int i)'''
    def remove(self, i, count):
        '''void QPolygon.remove(int i, int count)'''
    def prepend(self, value):
        '''void QPolygon.prepend(QPoint value)'''
    def mid(self, pos, length = None):
        '''QPolygon QPolygon.mid(int pos, int length = -1)'''
        return QPolygon()
    def lastIndexOf(self, value, from_ = None):
        '''int QPolygon.lastIndexOf(QPoint value, int from = -1)'''
        return int()
    def last(self):
        '''QPoint QPolygon.last()'''
        return QPoint()
    def isEmpty(self):
        '''bool QPolygon.isEmpty()'''
        return bool()
    def insert(self, i, value):
        '''void QPolygon.insert(int i, QPoint value)'''
    def indexOf(self, value, from_ = 0):
        '''int QPolygon.indexOf(QPoint value, int from = 0)'''
        return int()
    def first(self):
        '''QPoint QPolygon.first()'''
        return QPoint()
    def fill(self, value, size = None):
        '''void QPolygon.fill(QPoint value, int size = -1)'''
    def data(self):
        '''sip.voidptr QPolygon.data()'''
        return sip.voidptr()
    def __len__(self):
        ''' QPolygon.__len__()'''
        return ()
    def count(self, value):
        '''int QPolygon.count(QPoint value)'''
        return int()
    def count(self):
        '''int QPolygon.count()'''
        return int()
    def contains(self, value):
        '''bool QPolygon.contains(QPoint value)'''
        return bool()
    def clear(self):
        '''void QPolygon.clear()'''
    def at(self, i):
        '''QPoint QPolygon.at(int i)'''
        return QPoint()
    def append(self, value):
        '''void QPolygon.append(QPoint value)'''
    def translated(self, dx, dy):
        '''QPolygon QPolygon.translated(int dx, int dy)'''
        return QPolygon()
    def translated(self, offset):
        '''QPolygon QPolygon.translated(QPoint offset)'''
        return QPolygon()
    def subtracted(self, r):
        '''QPolygon QPolygon.subtracted(QPolygon r)'''
        return QPolygon()
    def intersected(self, r):
        '''QPolygon QPolygon.intersected(QPolygon r)'''
        return QPolygon()
    def united(self, r):
        '''QPolygon QPolygon.united(QPolygon r)'''
        return QPolygon()
    def containsPoint(self, pt, fillRule):
        '''bool QPolygon.containsPoint(QPoint pt, Qt.FillRule fillRule)'''
        return bool()
    def setPoint(self, index, pt):
        '''void QPolygon.setPoint(int index, QPoint pt)'''
    def setPoint(self, index, x, y):
        '''void QPolygon.setPoint(int index, int x, int y)'''
    def putPoints(self, index, firstx, firsty, *args):
        '''void QPolygon.putPoints(int index, int firstx, int firsty, ... *args)'''
    def putPoints(self, index, nPoints, fromPolygon, from_ = 0):
        '''void QPolygon.putPoints(int index, int nPoints, QPolygon fromPolygon, int from = 0)'''
    def setPoints(self, points):
        '''void QPolygon.setPoints(list-of-int points)'''
    def setPoints(self, firstx, firsty, *args):
        '''void QPolygon.setPoints(int firstx, int firsty, ... *args)'''
    def point(self, index):
        '''QPoint QPolygon.point(int index)'''
        return QPoint()
    def boundingRect(self):
        '''QRect QPolygon.boundingRect()'''
        return QRect()
    def translate(self, dx, dy):
        '''void QPolygon.translate(int dx, int dy)'''
    def translate(self, offset):
        '''void QPolygon.translate(QPoint offset)'''


class QPolygonF():
    """"""
    def __init__(self):
        '''void QPolygonF.__init__()'''
    def __init__(self, a):
        '''void QPolygonF.__init__(QPolygonF a)'''
    def __init__(self, v):
        '''void QPolygonF.__init__(list-of-QPointF v)'''
    def __init__(self, r):
        '''void QPolygonF.__init__(QRectF r)'''
    def __init__(self, a):
        '''void QPolygonF.__init__(QPolygon a)'''
    def __init__(self, asize):
        '''void QPolygonF.__init__(int asize)'''
    def __mul__(self, m):
        '''QPolygonF QPolygonF.__mul__(QTransform m)'''
        return QPolygonF()
    def swap(self, other):
        '''void QPolygonF.swap(QPolygonF other)'''
    def __contains__(self, value):
        '''int QPolygonF.__contains__(QPointF value)'''
        return int()
    def __delitem__(self, i):
        '''void QPolygonF.__delitem__(int i)'''
    def __delitem__(self, slice):
        '''void QPolygonF.__delitem__(slice slice)'''
    def __setitem__(self, i, value):
        '''void QPolygonF.__setitem__(int i, QPointF value)'''
    def __setitem__(self, slice, list):
        '''void QPolygonF.__setitem__(slice slice, QPolygonF list)'''
    def __getitem__(self, i):
        '''QPointF QPolygonF.__getitem__(int i)'''
        return QPointF()
    def __getitem__(self, slice):
        '''QPolygonF QPolygonF.__getitem__(slice slice)'''
        return QPolygonF()
    def __lshift__(self, value):
        '''object QPolygonF.__lshift__(QPointF value)'''
        return object()
    def __eq__(self, other):
        '''bool QPolygonF.__eq__(QPolygonF other)'''
        return bool()
    def __iadd__(self, other):
        '''QPolygonF QPolygonF.__iadd__(QPolygonF other)'''
        return QPolygonF()
    def __iadd__(self, value):
        '''QPolygonF QPolygonF.__iadd__(QPointF value)'''
        return QPolygonF()
    def __add__(self, other):
        '''QPolygonF QPolygonF.__add__(QPolygonF other)'''
        return QPolygonF()
    def __ne__(self, other):
        '''bool QPolygonF.__ne__(QPolygonF other)'''
        return bool()
    def value(self, i):
        '''QPointF QPolygonF.value(int i)'''
        return QPointF()
    def value(self, i, defaultValue):
        '''QPointF QPolygonF.value(int i, QPointF defaultValue)'''
        return QPointF()
    def size(self):
        '''int QPolygonF.size()'''
        return int()
    def replace(self, i, value):
        '''void QPolygonF.replace(int i, QPointF value)'''
    def remove(self, i):
        '''void QPolygonF.remove(int i)'''
    def remove(self, i, count):
        '''void QPolygonF.remove(int i, int count)'''
    def prepend(self, value):
        '''void QPolygonF.prepend(QPointF value)'''
    def mid(self, pos, length = None):
        '''QPolygonF QPolygonF.mid(int pos, int length = -1)'''
        return QPolygonF()
    def lastIndexOf(self, value, from_ = None):
        '''int QPolygonF.lastIndexOf(QPointF value, int from = -1)'''
        return int()
    def last(self):
        '''QPointF QPolygonF.last()'''
        return QPointF()
    def isEmpty(self):
        '''bool QPolygonF.isEmpty()'''
        return bool()
    def insert(self, i, value):
        '''void QPolygonF.insert(int i, QPointF value)'''
    def indexOf(self, value, from_ = 0):
        '''int QPolygonF.indexOf(QPointF value, int from = 0)'''
        return int()
    def first(self):
        '''QPointF QPolygonF.first()'''
        return QPointF()
    def fill(self, value, size = None):
        '''void QPolygonF.fill(QPointF value, int size = -1)'''
    def data(self):
        '''sip.voidptr QPolygonF.data()'''
        return sip.voidptr()
    def __len__(self):
        ''' QPolygonF.__len__()'''
        return ()
    def count(self, value):
        '''int QPolygonF.count(QPointF value)'''
        return int()
    def count(self):
        '''int QPolygonF.count()'''
        return int()
    def contains(self, value):
        '''bool QPolygonF.contains(QPointF value)'''
        return bool()
    def clear(self):
        '''void QPolygonF.clear()'''
    def at(self, i):
        '''QPointF QPolygonF.at(int i)'''
        return QPointF()
    def append(self, value):
        '''void QPolygonF.append(QPointF value)'''
    def translated(self, offset):
        '''QPolygonF QPolygonF.translated(QPointF offset)'''
        return QPolygonF()
    def translated(self, dx, dy):
        '''QPolygonF QPolygonF.translated(float dx, float dy)'''
        return QPolygonF()
    def subtracted(self, r):
        '''QPolygonF QPolygonF.subtracted(QPolygonF r)'''
        return QPolygonF()
    def intersected(self, r):
        '''QPolygonF QPolygonF.intersected(QPolygonF r)'''
        return QPolygonF()
    def united(self, r):
        '''QPolygonF QPolygonF.united(QPolygonF r)'''
        return QPolygonF()
    def containsPoint(self, pt, fillRule):
        '''bool QPolygonF.containsPoint(QPointF pt, Qt.FillRule fillRule)'''
        return bool()
    def boundingRect(self):
        '''QRectF QPolygonF.boundingRect()'''
        return QRectF()
    def isClosed(self):
        '''bool QPolygonF.isClosed()'''
        return bool()
    def toPolygon(self):
        '''QPolygon QPolygonF.toPolygon()'''
        return QPolygon()
    def translate(self, offset):
        '''void QPolygonF.translate(QPointF offset)'''
    def translate(self, dx, dy):
        '''void QPolygonF.translate(float dx, float dy)'''


class QQuaternion():
    """"""
    def __init__(self):
        '''void QQuaternion.__init__()'''
    def __init__(self, aScalar, xpos, ypos, zpos):
        '''void QQuaternion.__init__(float aScalar, float xpos, float ypos, float zpos)'''
    def __init__(self, aScalar, aVector):
        '''void QQuaternion.__init__(float aScalar, QVector3D aVector)'''
    def __init__(self, aVector):
        '''void QQuaternion.__init__(QVector4D aVector)'''
    def __init__(self):
        '''QQuaternion QQuaternion.__init__()'''
        return QQuaternion()
    def __eq__(self, q2):
        '''bool QQuaternion.__eq__(QQuaternion q2)'''
        return bool()
    def __div__(self, divisor):
        '''QQuaternion QQuaternion.__div__(float divisor)'''
        return QQuaternion()
    def __add__(self, q2):
        '''QQuaternion QQuaternion.__add__(QQuaternion q2)'''
        return QQuaternion()
    def __sub__(self, q2):
        '''QQuaternion QQuaternion.__sub__(QQuaternion q2)'''
        return QQuaternion()
    def __mul__(self, q2):
        '''QQuaternion QQuaternion.__mul__(QQuaternion q2)'''
        return QQuaternion()
    def __mul__(self, quaternion):
        '''QQuaternion QQuaternion.__mul__(QQuaternion quaternion)'''
        return QQuaternion()
    def __mul__(self, factor):
        '''QQuaternion QQuaternion.__mul__(float factor)'''
        return QQuaternion()
    def __mul__(self, vec):
        '''QVector3D QQuaternion.__mul__(QVector3D vec)'''
        return QVector3D()
    def __neg__(self):
        '''QQuaternion QQuaternion.__neg__()'''
        return QQuaternion()
    def __ne__(self, q2):
        '''bool QQuaternion.__ne__(QQuaternion q2)'''
        return bool()
    def toEulerAngles(self):
        '''QVector3D QQuaternion.toEulerAngles()'''
        return QVector3D()
    def conjugated(self):
        '''QQuaternion QQuaternion.conjugated()'''
        return QQuaternion()
    def inverted(self):
        '''QQuaternion QQuaternion.inverted()'''
        return QQuaternion()
    def dotProduct(self, q1, q2):
        '''static float QQuaternion.dotProduct(QQuaternion q1, QQuaternion q2)'''
        return float()
    def rotationTo(self, from_, to):
        '''static QQuaternion QQuaternion.rotationTo(QVector3D from, QVector3D to)'''
        return QQuaternion()
    def fromDirection(self, direction, up):
        '''static QQuaternion QQuaternion.fromDirection(QVector3D direction, QVector3D up)'''
        return QQuaternion()
    def fromAxes(self, xAxis, yAxis, zAxis):
        '''static QQuaternion QQuaternion.fromAxes(QVector3D xAxis, QVector3D yAxis, QVector3D zAxis)'''
        return QQuaternion()
    def getAxes(self, xAxis, yAxis, zAxis):
        '''void QQuaternion.getAxes(QVector3D xAxis, QVector3D yAxis, QVector3D zAxis)'''
    def fromRotationMatrix(self, rot3x3):
        '''static QQuaternion QQuaternion.fromRotationMatrix(QMatrix3x3 rot3x3)'''
        return QQuaternion()
    def toRotationMatrix(self):
        '''QMatrix3x3 QQuaternion.toRotationMatrix()'''
        return QMatrix3x3()
    def fromEulerAngles(self, pitch, yaw, roll):
        '''static QQuaternion QQuaternion.fromEulerAngles(float pitch, float yaw, float roll)'''
        return QQuaternion()
    def fromEulerAngles(self, eulerAngles):
        '''static QQuaternion QQuaternion.fromEulerAngles(QVector3D eulerAngles)'''
        return QQuaternion()
    def getEulerAngles(self, pitch, yaw, roll):
        '''void QQuaternion.getEulerAngles(float pitch, float yaw, float roll)'''
    def getAxisAndAngle(self, axis, angle):
        '''void QQuaternion.getAxisAndAngle(QVector3D axis, float angle)'''
    def toVector4D(self):
        '''QVector4D QQuaternion.toVector4D()'''
        return QVector4D()
    def vector(self):
        '''QVector3D QQuaternion.vector()'''
        return QVector3D()
    def setVector(self, aVector):
        '''void QQuaternion.setVector(QVector3D aVector)'''
    def setVector(self, aX, aY, aZ):
        '''void QQuaternion.setVector(float aX, float aY, float aZ)'''
    def __idiv__(self, divisor):
        '''QQuaternion QQuaternion.__idiv__(float divisor)'''
        return QQuaternion()
    def __imul__(self, factor):
        '''QQuaternion QQuaternion.__imul__(float factor)'''
        return QQuaternion()
    def __imul__(self, quaternion):
        '''QQuaternion QQuaternion.__imul__(QQuaternion quaternion)'''
        return QQuaternion()
    def __isub__(self, quaternion):
        '''QQuaternion QQuaternion.__isub__(QQuaternion quaternion)'''
        return QQuaternion()
    def __iadd__(self, quaternion):
        '''QQuaternion QQuaternion.__iadd__(QQuaternion quaternion)'''
        return QQuaternion()
    def conjugate(self):
        '''QQuaternion QQuaternion.conjugate()'''
        return QQuaternion()
    def setScalar(self, aScalar):
        '''void QQuaternion.setScalar(float aScalar)'''
    def setZ(self, aZ):
        '''void QQuaternion.setZ(float aZ)'''
    def setY(self, aY):
        '''void QQuaternion.setY(float aY)'''
    def setX(self, aX):
        '''void QQuaternion.setX(float aX)'''
    def scalar(self):
        '''float QQuaternion.scalar()'''
        return float()
    def z(self):
        '''float QQuaternion.z()'''
        return float()
    def y(self):
        '''float QQuaternion.y()'''
        return float()
    def x(self):
        '''float QQuaternion.x()'''
        return float()
    def isIdentity(self):
        '''bool QQuaternion.isIdentity()'''
        return bool()
    def isNull(self):
        '''bool QQuaternion.isNull()'''
        return bool()
    def nlerp(self, q1, q2, t):
        '''static QQuaternion QQuaternion.nlerp(QQuaternion q1, QQuaternion q2, float t)'''
        return QQuaternion()
    def slerp(self, q1, q2, t):
        '''static QQuaternion QQuaternion.slerp(QQuaternion q1, QQuaternion q2, float t)'''
        return QQuaternion()
    def fromAxisAndAngle(self, axis, angle):
        '''static QQuaternion QQuaternion.fromAxisAndAngle(QVector3D axis, float angle)'''
        return QQuaternion()
    def fromAxisAndAngle(self, x, y, z, angle):
        '''static QQuaternion QQuaternion.fromAxisAndAngle(float x, float y, float z, float angle)'''
        return QQuaternion()
    def rotatedVector(self, vector):
        '''QVector3D QQuaternion.rotatedVector(QVector3D vector)'''
        return QVector3D()
    def normalize(self):
        '''void QQuaternion.normalize()'''
    def normalized(self):
        '''QQuaternion QQuaternion.normalized()'''
        return QQuaternion()
    def lengthSquared(self):
        '''float QQuaternion.lengthSquared()'''
        return float()
    def length(self):
        '''float QQuaternion.length()'''
        return float()
    def __repr__(self):
        '''str QQuaternion.__repr__()'''
        return str()


class QRasterWindow(QPaintDeviceWindow):
    """"""
    def __init__(self, parent = None):
        '''void QRasterWindow.__init__(QWindow parent = None)'''
    def metric(self, metric):
        '''int QRasterWindow.metric(QPaintDevice.PaintDeviceMetric metric)'''
        return int()


class QRawFont():
    """"""
    # Enum QRawFont.LayoutFlag
    SeparateAdvances = 0
    KernedAdvances = 0
    UseDesignMetrics = 0

    # Enum QRawFont.AntialiasingType
    PixelAntialiasing = 0
    SubPixelAntialiasing = 0

    def __init__(self):
        '''void QRawFont.__init__()'''
    def __init__(self, fileName, pixelSize, hintingPreference = None):
        '''void QRawFont.__init__(str fileName, float pixelSize, QFont.HintingPreference hintingPreference = QFont.PreferDefaultHinting)'''
    def __init__(self, fontData, pixelSize, hintingPreference = None):
        '''void QRawFont.__init__(QByteArray fontData, float pixelSize, QFont.HintingPreference hintingPreference = QFont.PreferDefaultHinting)'''
    def __init__(self, other):
        '''void QRawFont.__init__(QRawFont other)'''
    def swap(self, other):
        '''void QRawFont.swap(QRawFont other)'''
    def underlinePosition(self):
        '''float QRawFont.underlinePosition()'''
        return float()
    def lineThickness(self):
        '''float QRawFont.lineThickness()'''
        return float()
    def boundingRect(self, glyphIndex):
        '''QRectF QRawFont.boundingRect(int glyphIndex)'''
        return QRectF()
    def fromFont(self, font, writingSystem = None):
        '''static QRawFont QRawFont.fromFont(QFont font, QFontDatabase.WritingSystem writingSystem = QFontDatabase.Any)'''
        return QRawFont()
    def fontTable(self, tagName):
        '''QByteArray QRawFont.fontTable(str tagName)'''
        return QByteArray()
    def supportedWritingSystems(self):
        '''list-of-QFontDatabase.WritingSystem QRawFont.supportedWritingSystems()'''
        return [QFontDatabase.WritingSystem()]
    def supportsCharacter(self, ucs4):
        '''bool QRawFont.supportsCharacter(int ucs4)'''
        return bool()
    def supportsCharacter(self, character):
        '''bool QRawFont.supportsCharacter(str character)'''
        return bool()
    def loadFromData(self, fontData, pixelSize, hintingPreference):
        '''void QRawFont.loadFromData(QByteArray fontData, float pixelSize, QFont.HintingPreference hintingPreference)'''
    def loadFromFile(self, fileName, pixelSize, hintingPreference):
        '''void QRawFont.loadFromFile(str fileName, float pixelSize, QFont.HintingPreference hintingPreference)'''
    def unitsPerEm(self):
        '''float QRawFont.unitsPerEm()'''
        return float()
    def maxCharWidth(self):
        '''float QRawFont.maxCharWidth()'''
        return float()
    def averageCharWidth(self):
        '''float QRawFont.averageCharWidth()'''
        return float()
    def xHeight(self):
        '''float QRawFont.xHeight()'''
        return float()
    def leading(self):
        '''float QRawFont.leading()'''
        return float()
    def descent(self):
        '''float QRawFont.descent()'''
        return float()
    def ascent(self):
        '''float QRawFont.ascent()'''
        return float()
    def hintingPreference(self):
        '''QFont.HintingPreference QRawFont.hintingPreference()'''
        return QFont.HintingPreference()
    def pixelSize(self):
        '''float QRawFont.pixelSize()'''
        return float()
    def setPixelSize(self, pixelSize):
        '''void QRawFont.setPixelSize(float pixelSize)'''
    def pathForGlyph(self, glyphIndex):
        '''QPainterPath QRawFont.pathForGlyph(int glyphIndex)'''
        return QPainterPath()
    def alphaMapForGlyph(self, glyphIndex, antialiasingType = None, transform = QTransform()):
        '''QImage QRawFont.alphaMapForGlyph(int glyphIndex, QRawFont.AntialiasingType antialiasingType = QRawFont.SubPixelAntialiasing, QTransform transform = QTransform())'''
        return QImage()
    def advancesForGlyphIndexes(self, glyphIndexes):
        '''list-of-QPointF QRawFont.advancesForGlyphIndexes(list-of-int glyphIndexes)'''
        return [QPointF()]
    def advancesForGlyphIndexes(self, glyphIndexes, layoutFlags):
        '''list-of-QPointF QRawFont.advancesForGlyphIndexes(list-of-int glyphIndexes, QRawFont.LayoutFlags layoutFlags)'''
        return [QPointF()]
    def glyphIndexesForString(self, text):
        '''list-of-int QRawFont.glyphIndexesForString(str text)'''
        return [int()]
    def weight(self):
        '''int QRawFont.weight()'''
        return int()
    def style(self):
        '''QFont.Style QRawFont.style()'''
        return QFont.Style()
    def styleName(self):
        '''str QRawFont.styleName()'''
        return str()
    def familyName(self):
        '''str QRawFont.familyName()'''
        return str()
    def __ne__(self, other):
        '''bool QRawFont.__ne__(QRawFont other)'''
        return bool()
    def __eq__(self, other):
        '''bool QRawFont.__eq__(QRawFont other)'''
        return bool()
    def isValid(self):
        '''bool QRawFont.isValid()'''
        return bool()
    class LayoutFlags():
        """"""
        def __init__(self):
            '''QRawFont.LayoutFlags QRawFont.LayoutFlags.__init__()'''
            return QRawFont.LayoutFlags()
        def __init__(self):
            '''int QRawFont.LayoutFlags.__init__()'''
            return int()
        def __init__(self):
            '''void QRawFont.LayoutFlags.__init__()'''
        def __bool__(self):
            '''int QRawFont.LayoutFlags.__bool__()'''
            return int()
        def __ne__(self, f):
            '''bool QRawFont.LayoutFlags.__ne__(QRawFont.LayoutFlags f)'''
            return bool()
        def __eq__(self, f):
            '''bool QRawFont.LayoutFlags.__eq__(QRawFont.LayoutFlags f)'''
            return bool()
        def __invert__(self):
            '''QRawFont.LayoutFlags QRawFont.LayoutFlags.__invert__()'''
            return QRawFont.LayoutFlags()
        def __and__(self, mask):
            '''QRawFont.LayoutFlags QRawFont.LayoutFlags.__and__(int mask)'''
            return QRawFont.LayoutFlags()
        def __xor__(self, f):
            '''QRawFont.LayoutFlags QRawFont.LayoutFlags.__xor__(QRawFont.LayoutFlags f)'''
            return QRawFont.LayoutFlags()
        def __xor__(self, f):
            '''QRawFont.LayoutFlags QRawFont.LayoutFlags.__xor__(int f)'''
            return QRawFont.LayoutFlags()
        def __or__(self, f):
            '''QRawFont.LayoutFlags QRawFont.LayoutFlags.__or__(QRawFont.LayoutFlags f)'''
            return QRawFont.LayoutFlags()
        def __or__(self, f):
            '''QRawFont.LayoutFlags QRawFont.LayoutFlags.__or__(int f)'''
            return QRawFont.LayoutFlags()
        def __int__(self):
            '''int QRawFont.LayoutFlags.__int__()'''
            return int()
        def __ixor__(self, f):
            '''QRawFont.LayoutFlags QRawFont.LayoutFlags.__ixor__(QRawFont.LayoutFlags f)'''
            return QRawFont.LayoutFlags()
        def __ior__(self, f):
            '''QRawFont.LayoutFlags QRawFont.LayoutFlags.__ior__(QRawFont.LayoutFlags f)'''
            return QRawFont.LayoutFlags()
        def __iand__(self, mask):
            '''QRawFont.LayoutFlags QRawFont.LayoutFlags.__iand__(int mask)'''
            return QRawFont.LayoutFlags()


class QRegion():
    """"""
    # Enum QRegion.RegionType
    Rectangle = 0
    Ellipse = 0

    def __init__(self):
        '''void QRegion.__init__()'''
    def __init__(self, x, y, w, h, type = None):
        '''void QRegion.__init__(int x, int y, int w, int h, QRegion.RegionType type = QRegion.Rectangle)'''
    def __init__(self, r, type = None):
        '''void QRegion.__init__(QRect r, QRegion.RegionType type = QRegion.Rectangle)'''
    def __init__(self, a, fillRule = None):
        '''void QRegion.__init__(QPolygon a, Qt.FillRule fillRule = Qt.OddEvenFill)'''
    def __init__(self, bitmap):
        '''void QRegion.__init__(QBitmap bitmap)'''
    def __init__(self, region):
        '''void QRegion.__init__(QRegion region)'''
    def __init__(self, variant):
        '''void QRegion.__init__(QVariant variant)'''
    def __mul__(self, m):
        '''QRegion QRegion.__mul__(QTransform m)'''
        return QRegion()
    def isNull(self):
        '''bool QRegion.isNull()'''
        return bool()
    def swap(self, other):
        '''void QRegion.swap(QRegion other)'''
    def rectCount(self):
        '''int QRegion.rectCount()'''
        return int()
    def intersects(self, r):
        '''bool QRegion.intersects(QRegion r)'''
        return bool()
    def intersects(self, r):
        '''bool QRegion.intersects(QRect r)'''
        return bool()
    def xored(self, r):
        '''QRegion QRegion.xored(QRegion r)'''
        return QRegion()
    def subtracted(self, r):
        '''QRegion QRegion.subtracted(QRegion r)'''
        return QRegion()
    def intersected(self, r):
        '''QRegion QRegion.intersected(QRegion r)'''
        return QRegion()
    def intersected(self, r):
        '''QRegion QRegion.intersected(QRect r)'''
        return QRegion()
    def __ne__(self, r):
        '''bool QRegion.__ne__(QRegion r)'''
        return bool()
    def __eq__(self, r):
        '''bool QRegion.__eq__(QRegion r)'''
        return bool()
    def __ixor__(self, r):
        '''QRegion QRegion.__ixor__(QRegion r)'''
        return QRegion()
    def __isub__(self, r):
        '''QRegion QRegion.__isub__(QRegion r)'''
        return QRegion()
    def __iand__(self, r):
        '''QRegion QRegion.__iand__(QRegion r)'''
        return QRegion()
    def __iand__(self, r):
        '''QRegion QRegion.__iand__(QRect r)'''
        return QRegion()
    def __iadd__(self, r):
        '''QRegion QRegion.__iadd__(QRegion r)'''
        return QRegion()
    def __iadd__(self, r):
        '''QRegion QRegion.__iadd__(QRect r)'''
        return QRegion()
    def __ior__(self, r):
        '''QRegion QRegion.__ior__(QRegion r)'''
        return QRegion()
    def __xor__(self, r):
        '''QRegion QRegion.__xor__(QRegion r)'''
        return QRegion()
    def __sub__(self, r):
        '''QRegion QRegion.__sub__(QRegion r)'''
        return QRegion()
    def __and__(self, r):
        '''QRegion QRegion.__and__(QRegion r)'''
        return QRegion()
    def __and__(self, r):
        '''QRegion QRegion.__and__(QRect r)'''
        return QRegion()
    def __add__(self, r):
        '''QRegion QRegion.__add__(QRegion r)'''
        return QRegion()
    def __add__(self, r):
        '''QRegion QRegion.__add__(QRect r)'''
        return QRegion()
    def __or__(self, r):
        '''QRegion QRegion.__or__(QRegion r)'''
        return QRegion()
    def rects(self):
        '''list-of-QRect QRegion.rects()'''
        return [QRect()]
    def boundingRect(self):
        '''QRect QRegion.boundingRect()'''
        return QRect()
    def united(self, r):
        '''QRegion QRegion.united(QRegion r)'''
        return QRegion()
    def united(self, r):
        '''QRegion QRegion.united(QRect r)'''
        return QRegion()
    def translated(self, dx, dy):
        '''QRegion QRegion.translated(int dx, int dy)'''
        return QRegion()
    def translated(self, p):
        '''QRegion QRegion.translated(QPoint p)'''
        return QRegion()
    def translate(self, dx, dy):
        '''void QRegion.translate(int dx, int dy)'''
    def translate(self, p):
        '''void QRegion.translate(QPoint p)'''
    def __contains__(self, p):
        '''int QRegion.__contains__(QPoint p)'''
        return int()
    def __contains__(self, r):
        '''int QRegion.__contains__(QRect r)'''
        return int()
    def contains(self, p):
        '''bool QRegion.contains(QPoint p)'''
        return bool()
    def contains(self, r):
        '''bool QRegion.contains(QRect r)'''
        return bool()
    def __bool__(self):
        '''int QRegion.__bool__()'''
        return int()
    def isEmpty(self):
        '''bool QRegion.isEmpty()'''
        return bool()


class QScreen(QObject):
    """"""
    availableGeometryChanged = pyqtSignal() # void availableGeometryChanged(const QRectamp;) - signal
    virtualGeometryChanged = pyqtSignal() # void virtualGeometryChanged(const QRectamp;) - signal
    physicalSizeChanged = pyqtSignal() # void physicalSizeChanged(const QSizeFamp;) - signal
    refreshRateChanged = pyqtSignal() # void refreshRateChanged(qreal) - signal
    orientationChanged = pyqtSignal() # void orientationChanged(Qt::ScreenOrientation) - signal
    primaryOrientationChanged = pyqtSignal() # void primaryOrientationChanged(Qt::ScreenOrientation) - signal
    logicalDotsPerInchChanged = pyqtSignal() # void logicalDotsPerInchChanged(qreal) - signal
    physicalDotsPerInchChanged = pyqtSignal() # void physicalDotsPerInchChanged(qreal) - signal
    geometryChanged = pyqtSignal() # void geometryChanged(const QRectamp;) - signal
    def devicePixelRatio(self):
        '''float QScreen.devicePixelRatio()'''
        return float()
    def refreshRate(self):
        '''float QScreen.refreshRate()'''
        return float()
    def grabWindow(self, window, x = 0, y = 0, width = None, height = None):
        '''QPixmap QScreen.grabWindow(sip.voidptr window, int x = 0, int y = 0, int width = -1, int height = -1)'''
        return QPixmap()
    def isLandscape(self, orientation):
        '''bool QScreen.isLandscape(Qt.ScreenOrientation orientation)'''
        return bool()
    def isPortrait(self, orientation):
        '''bool QScreen.isPortrait(Qt.ScreenOrientation orientation)'''
        return bool()
    def mapBetween(self, a, b, rect):
        '''QRect QScreen.mapBetween(Qt.ScreenOrientation a, Qt.ScreenOrientation b, QRect rect)'''
        return QRect()
    def transformBetween(self, a, b, target):
        '''QTransform QScreen.transformBetween(Qt.ScreenOrientation a, Qt.ScreenOrientation b, QRect target)'''
        return QTransform()
    def angleBetween(self, a, b):
        '''int QScreen.angleBetween(Qt.ScreenOrientation a, Qt.ScreenOrientation b)'''
        return int()
    def setOrientationUpdateMask(self, mask):
        '''void QScreen.setOrientationUpdateMask(Qt.ScreenOrientations mask)'''
    def orientationUpdateMask(self):
        '''Qt.ScreenOrientations QScreen.orientationUpdateMask()'''
        return Qt.ScreenOrientations()
    def orientation(self):
        '''Qt.ScreenOrientation QScreen.orientation()'''
        return Qt.ScreenOrientation()
    def primaryOrientation(self):
        '''Qt.ScreenOrientation QScreen.primaryOrientation()'''
        return Qt.ScreenOrientation()
    def nativeOrientation(self):
        '''Qt.ScreenOrientation QScreen.nativeOrientation()'''
        return Qt.ScreenOrientation()
    def availableVirtualGeometry(self):
        '''QRect QScreen.availableVirtualGeometry()'''
        return QRect()
    def availableVirtualSize(self):
        '''QSize QScreen.availableVirtualSize()'''
        return QSize()
    def virtualGeometry(self):
        '''QRect QScreen.virtualGeometry()'''
        return QRect()
    def virtualSize(self):
        '''QSize QScreen.virtualSize()'''
        return QSize()
    def virtualSiblings(self):
        '''list-of-QScreen QScreen.virtualSiblings()'''
        return [QScreen()]
    def availableGeometry(self):
        '''QRect QScreen.availableGeometry()'''
        return QRect()
    def availableSize(self):
        '''QSize QScreen.availableSize()'''
        return QSize()
    def logicalDotsPerInch(self):
        '''float QScreen.logicalDotsPerInch()'''
        return float()
    def logicalDotsPerInchY(self):
        '''float QScreen.logicalDotsPerInchY()'''
        return float()
    def logicalDotsPerInchX(self):
        '''float QScreen.logicalDotsPerInchX()'''
        return float()
    def physicalDotsPerInch(self):
        '''float QScreen.physicalDotsPerInch()'''
        return float()
    def physicalDotsPerInchY(self):
        '''float QScreen.physicalDotsPerInchY()'''
        return float()
    def physicalDotsPerInchX(self):
        '''float QScreen.physicalDotsPerInchX()'''
        return float()
    def physicalSize(self):
        '''QSizeF QScreen.physicalSize()'''
        return QSizeF()
    def geometry(self):
        '''QRect QScreen.geometry()'''
        return QRect()
    def size(self):
        '''QSize QScreen.size()'''
        return QSize()
    def depth(self):
        '''int QScreen.depth()'''
        return int()
    def name(self):
        '''str QScreen.name()'''
        return str()


class QSessionManager(QObject):
    """"""
    # Enum QSessionManager.RestartHint
    RestartIfRunning = 0
    RestartAnyway = 0
    RestartImmediately = 0
    RestartNever = 0

    def requestPhase2(self):
        '''void QSessionManager.requestPhase2()'''
    def isPhase2(self):
        '''bool QSessionManager.isPhase2()'''
        return bool()
    def setManagerProperty(self, name, value):
        '''void QSessionManager.setManagerProperty(str name, str value)'''
    def setManagerProperty(self, name, value):
        '''void QSessionManager.setManagerProperty(str name, list-of-str value)'''
    def discardCommand(self):
        '''list-of-str QSessionManager.discardCommand()'''
        return [str()]
    def setDiscardCommand(self):
        '''list-of-str QSessionManager.setDiscardCommand()'''
        return [str()]
    def restartCommand(self):
        '''list-of-str QSessionManager.restartCommand()'''
        return [str()]
    def setRestartCommand(self):
        '''list-of-str QSessionManager.setRestartCommand()'''
        return [str()]
    def restartHint(self):
        '''QSessionManager.RestartHint QSessionManager.restartHint()'''
        return QSessionManager.RestartHint()
    def setRestartHint(self):
        '''QSessionManager.RestartHint QSessionManager.setRestartHint()'''
        return QSessionManager.RestartHint()
    def cancel(self):
        '''void QSessionManager.cancel()'''
    def release(self):
        '''void QSessionManager.release()'''
    def allowsErrorInteraction(self):
        '''bool QSessionManager.allowsErrorInteraction()'''
        return bool()
    def allowsInteraction(self):
        '''bool QSessionManager.allowsInteraction()'''
        return bool()
    def sessionKey(self):
        '''str QSessionManager.sessionKey()'''
        return str()
    def sessionId(self):
        '''str QSessionManager.sessionId()'''
        return str()


class QStandardItemModel(QAbstractItemModel):
    """"""
    def __init__(self, parent = None):
        '''void QStandardItemModel.__init__(QObject parent = None)'''
    def __init__(self, rows, columns, parent = None):
        '''void QStandardItemModel.__init__(int rows, int columns, QObject parent = None)'''
    itemChanged = pyqtSignal() # void itemChanged(QStandardItem*) - signal
    def sibling(self, row, column, idx):
        '''QModelIndex QStandardItemModel.sibling(int row, int column, QModelIndex idx)'''
        return QModelIndex()
    def dropMimeData(self, data, action, row, column, parent):
        '''bool QStandardItemModel.dropMimeData(QMimeData data, Qt.DropAction action, int row, int column, QModelIndex parent)'''
        return bool()
    def mimeData(self, indexes):
        '''QMimeData QStandardItemModel.mimeData(list-of-QModelIndex indexes)'''
        return QMimeData()
    def mimeTypes(self):
        '''list-of-str QStandardItemModel.mimeTypes()'''
        return [str()]
    def setSortRole(self, role):
        '''void QStandardItemModel.setSortRole(int role)'''
    def sortRole(self):
        '''int QStandardItemModel.sortRole()'''
        return int()
    def findItems(self, text, flags = None, column = 0):
        '''list-of-QStandardItem QStandardItemModel.findItems(str text, Qt.MatchFlags flags = Qt.MatchExactly, int column = 0)'''
        return [QStandardItem()]
    def setItemPrototype(self, item):
        '''void QStandardItemModel.setItemPrototype(QStandardItem item)'''
    def itemPrototype(self):
        '''QStandardItem QStandardItemModel.itemPrototype()'''
        return QStandardItem()
    def takeVerticalHeaderItem(self, row):
        '''QStandardItem QStandardItemModel.takeVerticalHeaderItem(int row)'''
        return QStandardItem()
    def takeHorizontalHeaderItem(self, column):
        '''QStandardItem QStandardItemModel.takeHorizontalHeaderItem(int column)'''
        return QStandardItem()
    def takeColumn(self, column):
        '''list-of-QStandardItem QStandardItemModel.takeColumn(int column)'''
        return [QStandardItem()]
    def takeRow(self, row):
        '''list-of-QStandardItem QStandardItemModel.takeRow(int row)'''
        return [QStandardItem()]
    def takeItem(self, row, column = 0):
        '''QStandardItem QStandardItemModel.takeItem(int row, int column = 0)'''
        return QStandardItem()
    def insertColumn(self, column, items):
        '''void QStandardItemModel.insertColumn(int column, list-of-QStandardItem items)'''
    def insertColumn(self, column, parent = QModelIndex()):
        '''bool QStandardItemModel.insertColumn(int column, QModelIndex parent = QModelIndex())'''
        return bool()
    def insertRow(self, row, items):
        '''void QStandardItemModel.insertRow(int row, list-of-QStandardItem items)'''
    def insertRow(self, arow, aitem):
        '''void QStandardItemModel.insertRow(int arow, QStandardItem aitem)'''
    def insertRow(self, row, parent = QModelIndex()):
        '''bool QStandardItemModel.insertRow(int row, QModelIndex parent = QModelIndex())'''
        return bool()
    def appendColumn(self, items):
        '''void QStandardItemModel.appendColumn(list-of-QStandardItem items)'''
    def appendRow(self, items):
        '''void QStandardItemModel.appendRow(list-of-QStandardItem items)'''
    def appendRow(self, aitem):
        '''void QStandardItemModel.appendRow(QStandardItem aitem)'''
    def setColumnCount(self, columns):
        '''void QStandardItemModel.setColumnCount(int columns)'''
    def setRowCount(self, rows):
        '''void QStandardItemModel.setRowCount(int rows)'''
    def setVerticalHeaderLabels(self, labels):
        '''void QStandardItemModel.setVerticalHeaderLabels(list-of-str labels)'''
    def setHorizontalHeaderLabels(self, labels):
        '''void QStandardItemModel.setHorizontalHeaderLabels(list-of-str labels)'''
    def setVerticalHeaderItem(self, row, item):
        '''void QStandardItemModel.setVerticalHeaderItem(int row, QStandardItem item)'''
    def verticalHeaderItem(self, row):
        '''QStandardItem QStandardItemModel.verticalHeaderItem(int row)'''
        return QStandardItem()
    def setHorizontalHeaderItem(self, column, item):
        '''void QStandardItemModel.setHorizontalHeaderItem(int column, QStandardItem item)'''
    def horizontalHeaderItem(self, column):
        '''QStandardItem QStandardItemModel.horizontalHeaderItem(int column)'''
        return QStandardItem()
    def invisibleRootItem(self):
        '''QStandardItem QStandardItemModel.invisibleRootItem()'''
        return QStandardItem()
    def setItem(self, row, column, item):
        '''void QStandardItemModel.setItem(int row, int column, QStandardItem item)'''
    def setItem(self, arow, aitem):
        '''void QStandardItemModel.setItem(int arow, QStandardItem aitem)'''
    def item(self, row, column = 0):
        '''QStandardItem QStandardItemModel.item(int row, int column = 0)'''
        return QStandardItem()
    def indexFromItem(self, item):
        '''QModelIndex QStandardItemModel.indexFromItem(QStandardItem item)'''
        return QModelIndex()
    def itemFromIndex(self, index):
        '''QStandardItem QStandardItemModel.itemFromIndex(QModelIndex index)'''
        return QStandardItem()
    def sort(self, column, order = None):
        '''void QStandardItemModel.sort(int column, Qt.SortOrder order = Qt.AscendingOrder)'''
    def setItemData(self, index, roles):
        '''bool QStandardItemModel.setItemData(QModelIndex index, dict-of-int-QVariant roles)'''
        return bool()
    def itemData(self, index):
        '''dict-of-int-QVariant QStandardItemModel.itemData(QModelIndex index)'''
        return {int():QVariant()}
    def supportedDropActions(self):
        '''Qt.DropActions QStandardItemModel.supportedDropActions()'''
        return Qt.DropActions()
    def clear(self):
        '''void QStandardItemModel.clear()'''
    def flags(self, index):
        '''Qt.ItemFlags QStandardItemModel.flags(QModelIndex index)'''
        return Qt.ItemFlags()
    def removeColumns(self, column, count, parent = QModelIndex()):
        '''bool QStandardItemModel.removeColumns(int column, int count, QModelIndex parent = QModelIndex())'''
        return bool()
    def removeRows(self, row, count, parent = QModelIndex()):
        '''bool QStandardItemModel.removeRows(int row, int count, QModelIndex parent = QModelIndex())'''
        return bool()
    def insertColumns(self, column, count, parent = QModelIndex()):
        '''bool QStandardItemModel.insertColumns(int column, int count, QModelIndex parent = QModelIndex())'''
        return bool()
    def insertRows(self, row, count, parent = QModelIndex()):
        '''bool QStandardItemModel.insertRows(int row, int count, QModelIndex parent = QModelIndex())'''
        return bool()
    def setHeaderData(self, section, orientation, value, role = None):
        '''bool QStandardItemModel.setHeaderData(int section, Qt.Orientation orientation, QVariant value, int role = Qt.EditRole)'''
        return bool()
    def headerData(self, section, orientation, role = None):
        '''QVariant QStandardItemModel.headerData(int section, Qt.Orientation orientation, int role = Qt.DisplayRole)'''
        return QVariant()
    def setData(self, index, value, role = None):
        '''bool QStandardItemModel.setData(QModelIndex index, QVariant value, int role = Qt.EditRole)'''
        return bool()
    def data(self, index, role = None):
        '''QVariant QStandardItemModel.data(QModelIndex index, int role = Qt.DisplayRole)'''
        return QVariant()
    def hasChildren(self, parent = QModelIndex()):
        '''bool QStandardItemModel.hasChildren(QModelIndex parent = QModelIndex())'''
        return bool()
    def columnCount(self, parent = QModelIndex()):
        '''int QStandardItemModel.columnCount(QModelIndex parent = QModelIndex())'''
        return int()
    def rowCount(self, parent = QModelIndex()):
        '''int QStandardItemModel.rowCount(QModelIndex parent = QModelIndex())'''
        return int()
    def parent(self, child):
        '''QModelIndex QStandardItemModel.parent(QModelIndex child)'''
        return QModelIndex()
    def parent(self):
        '''QObject QStandardItemModel.parent()'''
        return QObject()
    def index(self, row, column, parent = QModelIndex()):
        '''QModelIndex QStandardItemModel.index(int row, int column, QModelIndex parent = QModelIndex())'''
        return QModelIndex()


class QStandardItem():
    """"""
    # Enum QStandardItem.ItemType
    Type = 0
    UserType = 0

    def __init__(self):
        '''void QStandardItem.__init__()'''
    def __init__(self, text):
        '''void QStandardItem.__init__(str text)'''
    def __init__(self, icon, text):
        '''void QStandardItem.__init__(QIcon icon, str text)'''
    def __init__(self, rows, columns = 1):
        '''void QStandardItem.__init__(int rows, int columns = 1)'''
    def __init__(self, other):
        '''void QStandardItem.__init__(QStandardItem other)'''
    def __ge__(self, other):
        '''bool QStandardItem.__ge__(QStandardItem other)'''
        return bool()
    def emitDataChanged(self):
        '''void QStandardItem.emitDataChanged()'''
    def appendRows(self, aitems):
        '''void QStandardItem.appendRows(list-of-QStandardItem aitems)'''
    def appendColumn(self, aitems):
        '''void QStandardItem.appendColumn(list-of-QStandardItem aitems)'''
    def appendRow(self, aitems):
        '''void QStandardItem.appendRow(list-of-QStandardItem aitems)'''
    def appendRow(self, aitem):
        '''void QStandardItem.appendRow(QStandardItem aitem)'''
    def setAccessibleDescription(self, aaccessibleDescription):
        '''void QStandardItem.setAccessibleDescription(str aaccessibleDescription)'''
    def setAccessibleText(self, aaccessibleText):
        '''void QStandardItem.setAccessibleText(str aaccessibleText)'''
    def setCheckState(self, acheckState):
        '''void QStandardItem.setCheckState(Qt.CheckState acheckState)'''
    def setForeground(self, abrush):
        '''void QStandardItem.setForeground(QBrush abrush)'''
    def setBackground(self, abrush):
        '''void QStandardItem.setBackground(QBrush abrush)'''
    def setTextAlignment(self, atextAlignment):
        '''void QStandardItem.setTextAlignment(Qt.Alignment atextAlignment)'''
    def setFont(self, afont):
        '''void QStandardItem.setFont(QFont afont)'''
    def setSizeHint(self, asizeHint):
        '''void QStandardItem.setSizeHint(QSize asizeHint)'''
    def setWhatsThis(self, awhatsThis):
        '''void QStandardItem.setWhatsThis(str awhatsThis)'''
    def setStatusTip(self, astatusTip):
        '''void QStandardItem.setStatusTip(str astatusTip)'''
    def setToolTip(self, atoolTip):
        '''void QStandardItem.setToolTip(str atoolTip)'''
    def setIcon(self, aicon):
        '''void QStandardItem.setIcon(QIcon aicon)'''
    def setText(self, atext):
        '''void QStandardItem.setText(str atext)'''
    def __lt__(self, other):
        '''bool QStandardItem.__lt__(QStandardItem other)'''
        return bool()
    def write(self, out):
        '''void QStandardItem.write(QDataStream out)'''
    def read(self, in_):
        '''void QStandardItem.read(QDataStream in)'''
    def type(self):
        '''int QStandardItem.type()'''
        return int()
    def clone(self):
        '''QStandardItem QStandardItem.clone()'''
        return QStandardItem()
    def sortChildren(self, column, order = None):
        '''void QStandardItem.sortChildren(int column, Qt.SortOrder order = Qt.AscendingOrder)'''
    def takeColumn(self, column):
        '''list-of-QStandardItem QStandardItem.takeColumn(int column)'''
        return [QStandardItem()]
    def takeRow(self, row):
        '''list-of-QStandardItem QStandardItem.takeRow(int row)'''
        return [QStandardItem()]
    def takeChild(self, row, column = 0):
        '''QStandardItem QStandardItem.takeChild(int row, int column = 0)'''
        return QStandardItem()
    def removeColumns(self, column, count):
        '''void QStandardItem.removeColumns(int column, int count)'''
    def removeRows(self, row, count):
        '''void QStandardItem.removeRows(int row, int count)'''
    def removeColumn(self, column):
        '''void QStandardItem.removeColumn(int column)'''
    def removeRow(self, row):
        '''void QStandardItem.removeRow(int row)'''
    def insertColumns(self, column, count):
        '''void QStandardItem.insertColumns(int column, int count)'''
    def insertColumn(self, column, items):
        '''void QStandardItem.insertColumn(int column, list-of-QStandardItem items)'''
    def insertRows(self, row, count):
        '''void QStandardItem.insertRows(int row, int count)'''
    def insertRows(self, row, items):
        '''void QStandardItem.insertRows(int row, list-of-QStandardItem items)'''
    def insertRow(self, row, items):
        '''void QStandardItem.insertRow(int row, list-of-QStandardItem items)'''
    def insertRow(self, arow, aitem):
        '''void QStandardItem.insertRow(int arow, QStandardItem aitem)'''
    def setChild(self, row, column, item):
        '''void QStandardItem.setChild(int row, int column, QStandardItem item)'''
    def setChild(self, arow, aitem):
        '''void QStandardItem.setChild(int arow, QStandardItem aitem)'''
    def child(self, row, column = 0):
        '''QStandardItem QStandardItem.child(int row, int column = 0)'''
        return QStandardItem()
    def hasChildren(self):
        '''bool QStandardItem.hasChildren()'''
        return bool()
    def setColumnCount(self, columns):
        '''void QStandardItem.setColumnCount(int columns)'''
    def columnCount(self):
        '''int QStandardItem.columnCount()'''
        return int()
    def setRowCount(self, rows):
        '''void QStandardItem.setRowCount(int rows)'''
    def rowCount(self):
        '''int QStandardItem.rowCount()'''
        return int()
    def model(self):
        '''QStandardItemModel QStandardItem.model()'''
        return QStandardItemModel()
    def index(self):
        '''QModelIndex QStandardItem.index()'''
        return QModelIndex()
    def column(self):
        '''int QStandardItem.column()'''
        return int()
    def row(self):
        '''int QStandardItem.row()'''
        return int()
    def parent(self):
        '''QStandardItem QStandardItem.parent()'''
        return QStandardItem()
    def setDropEnabled(self, dropEnabled):
        '''void QStandardItem.setDropEnabled(bool dropEnabled)'''
    def isDropEnabled(self):
        '''bool QStandardItem.isDropEnabled()'''
        return bool()
    def setDragEnabled(self, dragEnabled):
        '''void QStandardItem.setDragEnabled(bool dragEnabled)'''
    def isDragEnabled(self):
        '''bool QStandardItem.isDragEnabled()'''
        return bool()
    def setTristate(self, tristate):
        '''void QStandardItem.setTristate(bool tristate)'''
    def isTristate(self):
        '''bool QStandardItem.isTristate()'''
        return bool()
    def setCheckable(self, checkable):
        '''void QStandardItem.setCheckable(bool checkable)'''
    def isCheckable(self):
        '''bool QStandardItem.isCheckable()'''
        return bool()
    def setSelectable(self, selectable):
        '''void QStandardItem.setSelectable(bool selectable)'''
    def isSelectable(self):
        '''bool QStandardItem.isSelectable()'''
        return bool()
    def setEditable(self, editable):
        '''void QStandardItem.setEditable(bool editable)'''
    def isEditable(self):
        '''bool QStandardItem.isEditable()'''
        return bool()
    def setEnabled(self, enabled):
        '''void QStandardItem.setEnabled(bool enabled)'''
    def isEnabled(self):
        '''bool QStandardItem.isEnabled()'''
        return bool()
    def setFlags(self, flags):
        '''void QStandardItem.setFlags(Qt.ItemFlags flags)'''
    def flags(self):
        '''Qt.ItemFlags QStandardItem.flags()'''
        return Qt.ItemFlags()
    def accessibleDescription(self):
        '''str QStandardItem.accessibleDescription()'''
        return str()
    def accessibleText(self):
        '''str QStandardItem.accessibleText()'''
        return str()
    def checkState(self):
        '''Qt.CheckState QStandardItem.checkState()'''
        return Qt.CheckState()
    def foreground(self):
        '''QBrush QStandardItem.foreground()'''
        return QBrush()
    def background(self):
        '''QBrush QStandardItem.background()'''
        return QBrush()
    def textAlignment(self):
        '''Qt.Alignment QStandardItem.textAlignment()'''
        return Qt.Alignment()
    def font(self):
        '''QFont QStandardItem.font()'''
        return QFont()
    def sizeHint(self):
        '''QSize QStandardItem.sizeHint()'''
        return QSize()
    def whatsThis(self):
        '''str QStandardItem.whatsThis()'''
        return str()
    def statusTip(self):
        '''str QStandardItem.statusTip()'''
        return str()
    def toolTip(self):
        '''str QStandardItem.toolTip()'''
        return str()
    def icon(self):
        '''QIcon QStandardItem.icon()'''
        return QIcon()
    def text(self):
        '''str QStandardItem.text()'''
        return str()
    def setData(self, value, role = None):
        '''void QStandardItem.setData(QVariant value, int role = Qt.UserRole+1)'''
    def data(self, role = None):
        '''QVariant QStandardItem.data(int role = Qt.UserRole+1)'''
        return QVariant()


class QStaticText():
    """"""
    # Enum QStaticText.PerformanceHint
    ModerateCaching = 0
    AggressiveCaching = 0

    def __init__(self):
        '''void QStaticText.__init__()'''
    def __init__(self, text):
        '''void QStaticText.__init__(str text)'''
    def __init__(self, other):
        '''void QStaticText.__init__(QStaticText other)'''
    def swap(self, other):
        '''void QStaticText.swap(QStaticText other)'''
    def __ne__(self):
        '''QStaticText QStaticText.__ne__()'''
        return QStaticText()
    def __eq__(self):
        '''QStaticText QStaticText.__eq__()'''
        return QStaticText()
    def performanceHint(self):
        '''QStaticText.PerformanceHint QStaticText.performanceHint()'''
        return QStaticText.PerformanceHint()
    def setPerformanceHint(self, performanceHint):
        '''void QStaticText.setPerformanceHint(QStaticText.PerformanceHint performanceHint)'''
    def prepare(self, matrix = QTransform(), font = QFont()):
        '''void QStaticText.prepare(QTransform matrix = QTransform(), QFont font = QFont())'''
    def size(self):
        '''QSizeF QStaticText.size()'''
        return QSizeF()
    def textOption(self):
        '''QTextOption QStaticText.textOption()'''
        return QTextOption()
    def setTextOption(self, textOption):
        '''void QStaticText.setTextOption(QTextOption textOption)'''
    def textWidth(self):
        '''float QStaticText.textWidth()'''
        return float()
    def setTextWidth(self, textWidth):
        '''void QStaticText.setTextWidth(float textWidth)'''
    def textFormat(self):
        '''Qt.TextFormat QStaticText.textFormat()'''
        return Qt.TextFormat()
    def setTextFormat(self, textFormat):
        '''void QStaticText.setTextFormat(Qt.TextFormat textFormat)'''
    def text(self):
        '''str QStaticText.text()'''
        return str()
    def setText(self, text):
        '''void QStaticText.setText(str text)'''


class QStyleHints(QObject):
    """"""
    startDragTimeChanged = pyqtSignal() # void startDragTimeChanged(int) - signal
    startDragDistanceChanged = pyqtSignal() # void startDragDistanceChanged(int) - signal
    mouseDoubleClickIntervalChanged = pyqtSignal() # void mouseDoubleClickIntervalChanged(int) - signal
    keyboardInputIntervalChanged = pyqtSignal() # void keyboardInputIntervalChanged(int) - signal
    cursorFlashTimeChanged = pyqtSignal() # void cursorFlashTimeChanged(int) - signal
    def singleClickActivation(self):
        '''bool QStyleHints.singleClickActivation()'''
        return bool()
    def tabFocusBehavior(self):
        '''Qt.TabFocusBehavior QStyleHints.tabFocusBehavior()'''
        return Qt.TabFocusBehavior()
    def mousePressAndHoldInterval(self):
        '''int QStyleHints.mousePressAndHoldInterval()'''
        return int()
    def setFocusOnTouchRelease(self):
        '''bool QStyleHints.setFocusOnTouchRelease()'''
        return bool()
    def passwordMaskCharacter(self):
        '''str QStyleHints.passwordMaskCharacter()'''
        return str()
    def useRtlExtensions(self):
        '''bool QStyleHints.useRtlExtensions()'''
        return bool()
    def fontSmoothingGamma(self):
        '''float QStyleHints.fontSmoothingGamma()'''
        return float()
    def passwordMaskDelay(self):
        '''int QStyleHints.passwordMaskDelay()'''
        return int()
    def showIsFullScreen(self):
        '''bool QStyleHints.showIsFullScreen()'''
        return bool()
    def cursorFlashTime(self):
        '''int QStyleHints.cursorFlashTime()'''
        return int()
    def keyboardAutoRepeatRate(self):
        '''int QStyleHints.keyboardAutoRepeatRate()'''
        return int()
    def keyboardInputInterval(self):
        '''int QStyleHints.keyboardInputInterval()'''
        return int()
    def startDragVelocity(self):
        '''int QStyleHints.startDragVelocity()'''
        return int()
    def startDragTime(self):
        '''int QStyleHints.startDragTime()'''
        return int()
    def startDragDistance(self):
        '''int QStyleHints.startDragDistance()'''
        return int()
    def mouseDoubleClickInterval(self):
        '''int QStyleHints.mouseDoubleClickInterval()'''
        return int()


class QSurfaceFormat():
    """"""
    # Enum QSurfaceFormat.OpenGLContextProfile
    NoProfile = 0
    CoreProfile = 0
    CompatibilityProfile = 0

    # Enum QSurfaceFormat.RenderableType
    DefaultRenderableType = 0
    OpenGL = 0
    OpenGLES = 0
    OpenVG = 0

    # Enum QSurfaceFormat.SwapBehavior
    DefaultSwapBehavior = 0
    SingleBuffer = 0
    DoubleBuffer = 0
    TripleBuffer = 0

    # Enum QSurfaceFormat.FormatOption
    StereoBuffers = 0
    DebugContext = 0
    DeprecatedFunctions = 0
    ResetNotification = 0

    def __init__(self):
        '''void QSurfaceFormat.__init__()'''
    def __init__(self, options):
        '''void QSurfaceFormat.__init__(QSurfaceFormat.FormatOptions options)'''
    def __init__(self, other):
        '''void QSurfaceFormat.__init__(QSurfaceFormat other)'''
    def __eq__(self):
        '''QSurfaceFormat QSurfaceFormat.__eq__()'''
        return QSurfaceFormat()
    def __ne__(self):
        '''QSurfaceFormat QSurfaceFormat.__ne__()'''
        return QSurfaceFormat()
    def defaultFormat(self):
        '''static QSurfaceFormat QSurfaceFormat.defaultFormat()'''
        return QSurfaceFormat()
    def setDefaultFormat(self, format):
        '''static void QSurfaceFormat.setDefaultFormat(QSurfaceFormat format)'''
    def setSwapInterval(self, interval):
        '''void QSurfaceFormat.setSwapInterval(int interval)'''
    def swapInterval(self):
        '''int QSurfaceFormat.swapInterval()'''
        return int()
    def options(self):
        '''QSurfaceFormat.FormatOptions QSurfaceFormat.options()'''
        return QSurfaceFormat.FormatOptions()
    def setOptions(self, options):
        '''void QSurfaceFormat.setOptions(QSurfaceFormat.FormatOptions options)'''
    def setVersion(self, major, minor):
        '''void QSurfaceFormat.setVersion(int major, int minor)'''
    def version(self):
        '''tuple-of-int-int QSurfaceFormat.version()'''
        return tuple-of-int-int()
    def stereo(self):
        '''bool QSurfaceFormat.stereo()'''
        return bool()
    def testOption(self, opt):
        '''bool QSurfaceFormat.testOption(QSurfaceFormat.FormatOptions opt)'''
        return bool()
    def testOption(self, option):
        '''bool QSurfaceFormat.testOption(QSurfaceFormat.FormatOption option)'''
        return bool()
    def setOption(self, opt):
        '''void QSurfaceFormat.setOption(QSurfaceFormat.FormatOptions opt)'''
    def setOption(self, option, on = True):
        '''void QSurfaceFormat.setOption(QSurfaceFormat.FormatOption option, bool on = True)'''
    def setStereo(self, enable):
        '''void QSurfaceFormat.setStereo(bool enable)'''
    def minorVersion(self):
        '''int QSurfaceFormat.minorVersion()'''
        return int()
    def setMinorVersion(self, minorVersion):
        '''void QSurfaceFormat.setMinorVersion(int minorVersion)'''
    def majorVersion(self):
        '''int QSurfaceFormat.majorVersion()'''
        return int()
    def setMajorVersion(self, majorVersion):
        '''void QSurfaceFormat.setMajorVersion(int majorVersion)'''
    def renderableType(self):
        '''QSurfaceFormat.RenderableType QSurfaceFormat.renderableType()'''
        return QSurfaceFormat.RenderableType()
    def setRenderableType(self, type):
        '''void QSurfaceFormat.setRenderableType(QSurfaceFormat.RenderableType type)'''
    def profile(self):
        '''QSurfaceFormat.OpenGLContextProfile QSurfaceFormat.profile()'''
        return QSurfaceFormat.OpenGLContextProfile()
    def setProfile(self, profile):
        '''void QSurfaceFormat.setProfile(QSurfaceFormat.OpenGLContextProfile profile)'''
    def hasAlpha(self):
        '''bool QSurfaceFormat.hasAlpha()'''
        return bool()
    def swapBehavior(self):
        '''QSurfaceFormat.SwapBehavior QSurfaceFormat.swapBehavior()'''
        return QSurfaceFormat.SwapBehavior()
    def setSwapBehavior(self, behavior):
        '''void QSurfaceFormat.setSwapBehavior(QSurfaceFormat.SwapBehavior behavior)'''
    def samples(self):
        '''int QSurfaceFormat.samples()'''
        return int()
    def setSamples(self, numSamples):
        '''void QSurfaceFormat.setSamples(int numSamples)'''
    def alphaBufferSize(self):
        '''int QSurfaceFormat.alphaBufferSize()'''
        return int()
    def setAlphaBufferSize(self, size):
        '''void QSurfaceFormat.setAlphaBufferSize(int size)'''
    def blueBufferSize(self):
        '''int QSurfaceFormat.blueBufferSize()'''
        return int()
    def setBlueBufferSize(self, size):
        '''void QSurfaceFormat.setBlueBufferSize(int size)'''
    def greenBufferSize(self):
        '''int QSurfaceFormat.greenBufferSize()'''
        return int()
    def setGreenBufferSize(self, size):
        '''void QSurfaceFormat.setGreenBufferSize(int size)'''
    def redBufferSize(self):
        '''int QSurfaceFormat.redBufferSize()'''
        return int()
    def setRedBufferSize(self, size):
        '''void QSurfaceFormat.setRedBufferSize(int size)'''
    def stencilBufferSize(self):
        '''int QSurfaceFormat.stencilBufferSize()'''
        return int()
    def setStencilBufferSize(self, size):
        '''void QSurfaceFormat.setStencilBufferSize(int size)'''
    def depthBufferSize(self):
        '''int QSurfaceFormat.depthBufferSize()'''
        return int()
    def setDepthBufferSize(self, size):
        '''void QSurfaceFormat.setDepthBufferSize(int size)'''
    class FormatOptions():
        """"""
        def __init__(self):
            '''QSurfaceFormat.FormatOptions QSurfaceFormat.FormatOptions.__init__()'''
            return QSurfaceFormat.FormatOptions()
        def __init__(self):
            '''int QSurfaceFormat.FormatOptions.__init__()'''
            return int()
        def __init__(self):
            '''void QSurfaceFormat.FormatOptions.__init__()'''
        def __bool__(self):
            '''int QSurfaceFormat.FormatOptions.__bool__()'''
            return int()
        def __ne__(self, f):
            '''bool QSurfaceFormat.FormatOptions.__ne__(QSurfaceFormat.FormatOptions f)'''
            return bool()
        def __eq__(self, f):
            '''bool QSurfaceFormat.FormatOptions.__eq__(QSurfaceFormat.FormatOptions f)'''
            return bool()
        def __invert__(self):
            '''QSurfaceFormat.FormatOptions QSurfaceFormat.FormatOptions.__invert__()'''
            return QSurfaceFormat.FormatOptions()
        def __and__(self, mask):
            '''QSurfaceFormat.FormatOptions QSurfaceFormat.FormatOptions.__and__(int mask)'''
            return QSurfaceFormat.FormatOptions()
        def __xor__(self, f):
            '''QSurfaceFormat.FormatOptions QSurfaceFormat.FormatOptions.__xor__(QSurfaceFormat.FormatOptions f)'''
            return QSurfaceFormat.FormatOptions()
        def __xor__(self, f):
            '''QSurfaceFormat.FormatOptions QSurfaceFormat.FormatOptions.__xor__(int f)'''
            return QSurfaceFormat.FormatOptions()
        def __or__(self, f):
            '''QSurfaceFormat.FormatOptions QSurfaceFormat.FormatOptions.__or__(QSurfaceFormat.FormatOptions f)'''
            return QSurfaceFormat.FormatOptions()
        def __or__(self, f):
            '''QSurfaceFormat.FormatOptions QSurfaceFormat.FormatOptions.__or__(int f)'''
            return QSurfaceFormat.FormatOptions()
        def __int__(self):
            '''int QSurfaceFormat.FormatOptions.__int__()'''
            return int()
        def __ixor__(self, f):
            '''QSurfaceFormat.FormatOptions QSurfaceFormat.FormatOptions.__ixor__(QSurfaceFormat.FormatOptions f)'''
            return QSurfaceFormat.FormatOptions()
        def __ior__(self, f):
            '''QSurfaceFormat.FormatOptions QSurfaceFormat.FormatOptions.__ior__(QSurfaceFormat.FormatOptions f)'''
            return QSurfaceFormat.FormatOptions()
        def __iand__(self, mask):
            '''QSurfaceFormat.FormatOptions QSurfaceFormat.FormatOptions.__iand__(int mask)'''
            return QSurfaceFormat.FormatOptions()


class QSyntaxHighlighter(QObject):
    """"""
    def __init__(self, parent):
        '''void QSyntaxHighlighter.__init__(QTextDocument parent)'''
    def __init__(self, parent):
        '''void QSyntaxHighlighter.__init__(QObject parent)'''
    def currentBlock(self):
        '''QTextBlock QSyntaxHighlighter.currentBlock()'''
        return QTextBlock()
    def currentBlockUserData(self):
        '''QTextBlockUserData QSyntaxHighlighter.currentBlockUserData()'''
        return QTextBlockUserData()
    def setCurrentBlockUserData(self, data):
        '''void QSyntaxHighlighter.setCurrentBlockUserData(QTextBlockUserData data)'''
    def setCurrentBlockState(self, newState):
        '''void QSyntaxHighlighter.setCurrentBlockState(int newState)'''
    def currentBlockState(self):
        '''int QSyntaxHighlighter.currentBlockState()'''
        return int()
    def previousBlockState(self):
        '''int QSyntaxHighlighter.previousBlockState()'''
        return int()
    def format(self, pos):
        '''QTextCharFormat QSyntaxHighlighter.format(int pos)'''
        return QTextCharFormat()
    def setFormat(self, start, count, format):
        '''void QSyntaxHighlighter.setFormat(int start, int count, QTextCharFormat format)'''
    def setFormat(self, start, count, color):
        '''void QSyntaxHighlighter.setFormat(int start, int count, QColor color)'''
    def setFormat(self, start, count, font):
        '''void QSyntaxHighlighter.setFormat(int start, int count, QFont font)'''
    def highlightBlock(self, text):
        '''abstract void QSyntaxHighlighter.highlightBlock(str text)'''
    def rehighlightBlock(self, block):
        '''void QSyntaxHighlighter.rehighlightBlock(QTextBlock block)'''
    def rehighlight(self):
        '''void QSyntaxHighlighter.rehighlight()'''
    def document(self):
        '''QTextDocument QSyntaxHighlighter.document()'''
        return QTextDocument()
    def setDocument(self, doc):
        '''void QSyntaxHighlighter.setDocument(QTextDocument doc)'''


class QTextCursor():
    """"""
    # Enum QTextCursor.SelectionType
    WordUnderCursor = 0
    LineUnderCursor = 0
    BlockUnderCursor = 0
    Document = 0

    # Enum QTextCursor.MoveOperation
    NoMove = 0
    Start = 0
    Up = 0
    StartOfLine = 0
    StartOfBlock = 0
    StartOfWord = 0
    PreviousBlock = 0
    PreviousCharacter = 0
    PreviousWord = 0
    Left = 0
    WordLeft = 0
    End = 0
    Down = 0
    EndOfLine = 0
    EndOfWord = 0
    EndOfBlock = 0
    NextBlock = 0
    NextCharacter = 0
    NextWord = 0
    Right = 0
    WordRight = 0
    NextCell = 0
    PreviousCell = 0
    NextRow = 0
    PreviousRow = 0

    # Enum QTextCursor.MoveMode
    MoveAnchor = 0
    KeepAnchor = 0

    def __init__(self):
        '''void QTextCursor.__init__()'''
    def __init__(self, document):
        '''void QTextCursor.__init__(QTextDocument document)'''
    def __init__(self, frame):
        '''void QTextCursor.__init__(QTextFrame frame)'''
    def __init__(self, block):
        '''void QTextCursor.__init__(QTextBlock block)'''
    def __init__(self, cursor):
        '''void QTextCursor.__init__(QTextCursor cursor)'''
    def swap(self, other):
        '''void QTextCursor.swap(QTextCursor other)'''
    def keepPositionOnInsert(self):
        '''bool QTextCursor.keepPositionOnInsert()'''
        return bool()
    def setKeepPositionOnInsert(self, b):
        '''void QTextCursor.setKeepPositionOnInsert(bool b)'''
    def verticalMovementX(self):
        '''int QTextCursor.verticalMovementX()'''
        return int()
    def setVerticalMovementX(self, x):
        '''void QTextCursor.setVerticalMovementX(int x)'''
    def positionInBlock(self):
        '''int QTextCursor.positionInBlock()'''
        return int()
    def document(self):
        '''QTextDocument QTextCursor.document()'''
        return QTextDocument()
    def setVisualNavigation(self, b):
        '''void QTextCursor.setVisualNavigation(bool b)'''
    def visualNavigation(self):
        '''bool QTextCursor.visualNavigation()'''
        return bool()
    def isCopyOf(self, other):
        '''bool QTextCursor.isCopyOf(QTextCursor other)'''
        return bool()
    def __gt__(self, rhs):
        '''bool QTextCursor.__gt__(QTextCursor rhs)'''
        return bool()
    def __ge__(self, rhs):
        '''bool QTextCursor.__ge__(QTextCursor rhs)'''
        return bool()
    def __eq__(self, rhs):
        '''bool QTextCursor.__eq__(QTextCursor rhs)'''
        return bool()
    def __le__(self, rhs):
        '''bool QTextCursor.__le__(QTextCursor rhs)'''
        return bool()
    def __lt__(self, rhs):
        '''bool QTextCursor.__lt__(QTextCursor rhs)'''
        return bool()
    def __ne__(self, rhs):
        '''bool QTextCursor.__ne__(QTextCursor rhs)'''
        return bool()
    def columnNumber(self):
        '''int QTextCursor.columnNumber()'''
        return int()
    def blockNumber(self):
        '''int QTextCursor.blockNumber()'''
        return int()
    def endEditBlock(self):
        '''void QTextCursor.endEditBlock()'''
    def joinPreviousEditBlock(self):
        '''void QTextCursor.joinPreviousEditBlock()'''
    def beginEditBlock(self):
        '''void QTextCursor.beginEditBlock()'''
    def insertImage(self, format):
        '''void QTextCursor.insertImage(QTextImageFormat format)'''
    def insertImage(self, format, alignment):
        '''void QTextCursor.insertImage(QTextImageFormat format, QTextFrameFormat.Position alignment)'''
    def insertImage(self, name):
        '''void QTextCursor.insertImage(str name)'''
    def insertImage(self, image, name = None):
        '''void QTextCursor.insertImage(QImage image, str name = '')'''
    def insertHtml(self, html):
        '''void QTextCursor.insertHtml(str html)'''
    def insertFragment(self, fragment):
        '''void QTextCursor.insertFragment(QTextDocumentFragment fragment)'''
    def currentFrame(self):
        '''QTextFrame QTextCursor.currentFrame()'''
        return QTextFrame()
    def insertFrame(self, format):
        '''QTextFrame QTextCursor.insertFrame(QTextFrameFormat format)'''
        return QTextFrame()
    def currentTable(self):
        '''QTextTable QTextCursor.currentTable()'''
        return QTextTable()
    def insertTable(self, rows, cols, format):
        '''QTextTable QTextCursor.insertTable(int rows, int cols, QTextTableFormat format)'''
        return QTextTable()
    def insertTable(self, rows, cols):
        '''QTextTable QTextCursor.insertTable(int rows, int cols)'''
        return QTextTable()
    def currentList(self):
        '''QTextList QTextCursor.currentList()'''
        return QTextList()
    def createList(self, format):
        '''QTextList QTextCursor.createList(QTextListFormat format)'''
        return QTextList()
    def createList(self, style):
        '''QTextList QTextCursor.createList(QTextListFormat.Style style)'''
        return QTextList()
    def insertList(self, format):
        '''QTextList QTextCursor.insertList(QTextListFormat format)'''
        return QTextList()
    def insertList(self, style):
        '''QTextList QTextCursor.insertList(QTextListFormat.Style style)'''
        return QTextList()
    def insertBlock(self):
        '''void QTextCursor.insertBlock()'''
    def insertBlock(self, format):
        '''void QTextCursor.insertBlock(QTextBlockFormat format)'''
    def insertBlock(self, format, charFormat):
        '''void QTextCursor.insertBlock(QTextBlockFormat format, QTextCharFormat charFormat)'''
    def atEnd(self):
        '''bool QTextCursor.atEnd()'''
        return bool()
    def atStart(self):
        '''bool QTextCursor.atStart()'''
        return bool()
    def atBlockEnd(self):
        '''bool QTextCursor.atBlockEnd()'''
        return bool()
    def atBlockStart(self):
        '''bool QTextCursor.atBlockStart()'''
        return bool()
    def mergeBlockCharFormat(self, modifier):
        '''void QTextCursor.mergeBlockCharFormat(QTextCharFormat modifier)'''
    def setBlockCharFormat(self, format):
        '''void QTextCursor.setBlockCharFormat(QTextCharFormat format)'''
    def blockCharFormat(self):
        '''QTextCharFormat QTextCursor.blockCharFormat()'''
        return QTextCharFormat()
    def mergeBlockFormat(self, modifier):
        '''void QTextCursor.mergeBlockFormat(QTextBlockFormat modifier)'''
    def setBlockFormat(self, format):
        '''void QTextCursor.setBlockFormat(QTextBlockFormat format)'''
    def blockFormat(self):
        '''QTextBlockFormat QTextCursor.blockFormat()'''
        return QTextBlockFormat()
    def mergeCharFormat(self, modifier):
        '''void QTextCursor.mergeCharFormat(QTextCharFormat modifier)'''
    def setCharFormat(self, format):
        '''void QTextCursor.setCharFormat(QTextCharFormat format)'''
    def charFormat(self):
        '''QTextCharFormat QTextCursor.charFormat()'''
        return QTextCharFormat()
    def block(self):
        '''QTextBlock QTextCursor.block()'''
        return QTextBlock()
    def selectedTableCells(self, firstRow, numRows, firstColumn, numColumns):
        '''void QTextCursor.selectedTableCells(int firstRow, int numRows, int firstColumn, int numColumns)'''
    def selection(self):
        '''QTextDocumentFragment QTextCursor.selection()'''
        return QTextDocumentFragment()
    def selectedText(self):
        '''str QTextCursor.selectedText()'''
        return str()
    def selectionEnd(self):
        '''int QTextCursor.selectionEnd()'''
        return int()
    def selectionStart(self):
        '''int QTextCursor.selectionStart()'''
        return int()
    def clearSelection(self):
        '''void QTextCursor.clearSelection()'''
    def removeSelectedText(self):
        '''void QTextCursor.removeSelectedText()'''
    def hasComplexSelection(self):
        '''bool QTextCursor.hasComplexSelection()'''
        return bool()
    def hasSelection(self):
        '''bool QTextCursor.hasSelection()'''
        return bool()
    def select(self, selection):
        '''void QTextCursor.select(QTextCursor.SelectionType selection)'''
    def deletePreviousChar(self):
        '''void QTextCursor.deletePreviousChar()'''
    def deleteChar(self):
        '''void QTextCursor.deleteChar()'''
    def movePosition(self, op, mode = None, n = 1):
        '''bool QTextCursor.movePosition(QTextCursor.MoveOperation op, QTextCursor.MoveMode mode = QTextCursor.MoveAnchor, int n = 1)'''
        return bool()
    def insertText(self, text):
        '''void QTextCursor.insertText(str text)'''
    def insertText(self, text, format):
        '''void QTextCursor.insertText(str text, QTextCharFormat format)'''
    def anchor(self):
        '''int QTextCursor.anchor()'''
        return int()
    def position(self):
        '''int QTextCursor.position()'''
        return int()
    def setPosition(self, pos, mode = None):
        '''void QTextCursor.setPosition(int pos, QTextCursor.MoveMode mode = QTextCursor.MoveAnchor)'''
    def isNull(self):
        '''bool QTextCursor.isNull()'''
        return bool()


class Qt():
    """"""
    def convertFromPlainText(self, plain, mode = None):
        '''static str Qt.convertFromPlainText(str plain, Qt.WhiteSpaceMode mode = Qt.WhiteSpacePre)'''
        return str()
    def mightBeRichText(self):
        '''static str Qt.mightBeRichText()'''
        return str()


class QTextDocument(QObject):
    """"""
    # Enum QTextDocument.Stacks
    UndoStack = 0
    RedoStack = 0
    UndoAndRedoStacks = 0

    # Enum QTextDocument.ResourceType
    HtmlResource = 0
    ImageResource = 0
    StyleSheetResource = 0
    UserResource = 0

    # Enum QTextDocument.FindFlag
    FindBackward = 0
    FindCaseSensitively = 0
    FindWholeWords = 0

    # Enum QTextDocument.MetaInformation
    DocumentTitle = 0
    DocumentUrl = 0

    def __init__(self, parent = None):
        '''void QTextDocument.__init__(QObject parent = None)'''
    def __init__(self, text, parent = None):
        '''void QTextDocument.__init__(str text, QObject parent = None)'''
    baseUrlChanged = pyqtSignal() # void baseUrlChanged(const QUrlamp;) - signal
    def setBaseUrl(self, url):
        '''void QTextDocument.setBaseUrl(QUrl url)'''
    def baseUrl(self):
        '''QUrl QTextDocument.baseUrl()'''
        return QUrl()
    def setDefaultCursorMoveStyle(self, style):
        '''void QTextDocument.setDefaultCursorMoveStyle(Qt.CursorMoveStyle style)'''
    def defaultCursorMoveStyle(self):
        '''Qt.CursorMoveStyle QTextDocument.defaultCursorMoveStyle()'''
        return Qt.CursorMoveStyle()
    def clearUndoRedoStacks(self, stacks = None):
        '''void QTextDocument.clearUndoRedoStacks(QTextDocument.Stacks stacks = QTextDocument.UndoAndRedoStacks)'''
    def availableRedoSteps(self):
        '''int QTextDocument.availableRedoSteps()'''
        return int()
    def availableUndoSteps(self):
        '''int QTextDocument.availableUndoSteps()'''
        return int()
    def characterCount(self):
        '''int QTextDocument.characterCount()'''
        return int()
    def lineCount(self):
        '''int QTextDocument.lineCount()'''
        return int()
    def setDocumentMargin(self, margin):
        '''void QTextDocument.setDocumentMargin(float margin)'''
    def documentMargin(self):
        '''float QTextDocument.documentMargin()'''
        return float()
    def characterAt(self, pos):
        '''str QTextDocument.characterAt(int pos)'''
        return str()
    documentLayoutChanged = pyqtSignal() # void documentLayoutChanged() - signal
    undoCommandAdded = pyqtSignal() # void undoCommandAdded() - signal
    def setIndentWidth(self, width):
        '''void QTextDocument.setIndentWidth(float width)'''
    def indentWidth(self):
        '''float QTextDocument.indentWidth()'''
        return float()
    def lastBlock(self):
        '''QTextBlock QTextDocument.lastBlock()'''
        return QTextBlock()
    def firstBlock(self):
        '''QTextBlock QTextDocument.firstBlock()'''
        return QTextBlock()
    def findBlockByLineNumber(self, blockNumber):
        '''QTextBlock QTextDocument.findBlockByLineNumber(int blockNumber)'''
        return QTextBlock()
    def findBlockByNumber(self, blockNumber):
        '''QTextBlock QTextDocument.findBlockByNumber(int blockNumber)'''
        return QTextBlock()
    def revision(self):
        '''int QTextDocument.revision()'''
        return int()
    def setDefaultTextOption(self, option):
        '''void QTextDocument.setDefaultTextOption(QTextOption option)'''
    def defaultTextOption(self):
        '''QTextOption QTextDocument.defaultTextOption()'''
        return QTextOption()
    def setMaximumBlockCount(self, maximum):
        '''void QTextDocument.setMaximumBlockCount(int maximum)'''
    def maximumBlockCount(self):
        '''int QTextDocument.maximumBlockCount()'''
        return int()
    def defaultStyleSheet(self):
        '''str QTextDocument.defaultStyleSheet()'''
        return str()
    def setDefaultStyleSheet(self, sheet):
        '''void QTextDocument.setDefaultStyleSheet(str sheet)'''
    def blockCount(self):
        '''int QTextDocument.blockCount()'''
        return int()
    def size(self):
        '''QSizeF QTextDocument.size()'''
        return QSizeF()
    def adjustSize(self):
        '''void QTextDocument.adjustSize()'''
    def idealWidth(self):
        '''float QTextDocument.idealWidth()'''
        return float()
    def textWidth(self):
        '''float QTextDocument.textWidth()'''
        return float()
    def setTextWidth(self, width):
        '''void QTextDocument.setTextWidth(float width)'''
    def drawContents(self, p, rect = QRectF()):
        '''void QTextDocument.drawContents(QPainter p, QRectF rect = QRectF())'''
    def loadResource(self, type, name):
        '''QVariant QTextDocument.loadResource(int type, QUrl name)'''
        return QVariant()
    def createObject(self, f):
        '''QTextObject QTextDocument.createObject(QTextFormat f)'''
        return QTextObject()
    def setModified(self, on = True):
        '''void QTextDocument.setModified(bool on = True)'''
    def redo(self):
        '''void QTextDocument.redo()'''
    def redo(self, cursor):
        '''void QTextDocument.redo(QTextCursor cursor)'''
    def undo(self):
        '''void QTextDocument.undo()'''
    def undo(self, cursor):
        '''void QTextDocument.undo(QTextCursor cursor)'''
    undoAvailable = pyqtSignal() # void undoAvailable(bool) - signal
    redoAvailable = pyqtSignal() # void redoAvailable(bool) - signal
    modificationChanged = pyqtSignal() # void modificationChanged(bool) - signal
    cursorPositionChanged = pyqtSignal() # void cursorPositionChanged(const QTextCursoramp;) - signal
    contentsChanged = pyqtSignal() # void contentsChanged() - signal
    contentsChange = pyqtSignal() # void contentsChange(int,int,int) - signal
    blockCountChanged = pyqtSignal() # void blockCountChanged(int) - signal
    def useDesignMetrics(self):
        '''bool QTextDocument.useDesignMetrics()'''
        return bool()
    def setUseDesignMetrics(self, b):
        '''void QTextDocument.setUseDesignMetrics(bool b)'''
    def markContentsDirty(self, from_, length):
        '''void QTextDocument.markContentsDirty(int from, int length)'''
    def allFormats(self):
        '''list-of-QTextFormat QTextDocument.allFormats()'''
        return [QTextFormat()]
    def addResource(self, type, name, resource):
        '''void QTextDocument.addResource(int type, QUrl name, QVariant resource)'''
    def resource(self, type, name):
        '''QVariant QTextDocument.resource(int type, QUrl name)'''
        return QVariant()
    def print_(self, printer):
        '''void QTextDocument.print_(QPagedPaintDevice printer)'''
    def isModified(self):
        '''bool QTextDocument.isModified()'''
        return bool()
    def pageCount(self):
        '''int QTextDocument.pageCount()'''
        return int()
    def defaultFont(self):
        '''QFont QTextDocument.defaultFont()'''
        return QFont()
    def setDefaultFont(self, font):
        '''void QTextDocument.setDefaultFont(QFont font)'''
    def pageSize(self):
        '''QSizeF QTextDocument.pageSize()'''
        return QSizeF()
    def setPageSize(self, size):
        '''void QTextDocument.setPageSize(QSizeF size)'''
    def end(self):
        '''QTextBlock QTextDocument.end()'''
        return QTextBlock()
    def begin(self):
        '''QTextBlock QTextDocument.begin()'''
        return QTextBlock()
    def findBlock(self, pos):
        '''QTextBlock QTextDocument.findBlock(int pos)'''
        return QTextBlock()
    def objectForFormat(self):
        '''QTextFormat QTextDocument.objectForFormat()'''
        return QTextFormat()
    def object(self, objectIndex):
        '''QTextObject QTextDocument.object(int objectIndex)'''
        return QTextObject()
    def rootFrame(self):
        '''QTextFrame QTextDocument.rootFrame()'''
        return QTextFrame()
    def find(self, subString, position = 0, options = 0):
        '''QTextCursor QTextDocument.find(str subString, int position = 0, QTextDocument.FindFlags options = 0)'''
        return QTextCursor()
    def find(self, expr, position = 0, options = 0):
        '''QTextCursor QTextDocument.find(QRegExp expr, int position = 0, QTextDocument.FindFlags options = 0)'''
        return QTextCursor()
    def find(self, expr, position = 0, options = 0):
        '''QTextCursor QTextDocument.find(QRegularExpression expr, int position = 0, QTextDocument.FindFlags options = 0)'''
        return QTextCursor()
    def find(self, subString, cursor, options = 0):
        '''QTextCursor QTextDocument.find(str subString, QTextCursor cursor, QTextDocument.FindFlags options = 0)'''
        return QTextCursor()
    def find(self, expr, cursor, options = 0):
        '''QTextCursor QTextDocument.find(QRegExp expr, QTextCursor cursor, QTextDocument.FindFlags options = 0)'''
        return QTextCursor()
    def find(self, expr, cursor, options = 0):
        '''QTextCursor QTextDocument.find(QRegularExpression expr, QTextCursor cursor, QTextDocument.FindFlags options = 0)'''
        return QTextCursor()
    def setPlainText(self, text):
        '''void QTextDocument.setPlainText(str text)'''
    def toPlainText(self):
        '''str QTextDocument.toPlainText()'''
        return str()
    def setHtml(self, html):
        '''void QTextDocument.setHtml(str html)'''
    def toHtml(self, encoding = QByteArray()):
        '''str QTextDocument.toHtml(QByteArray encoding = QByteArray())'''
        return str()
    def metaInformation(self, info):
        '''str QTextDocument.metaInformation(QTextDocument.MetaInformation info)'''
        return str()
    def setMetaInformation(self, info):
        '''str QTextDocument.setMetaInformation(QTextDocument.MetaInformation info)'''
        return str()
    def documentLayout(self):
        '''QAbstractTextDocumentLayout QTextDocument.documentLayout()'''
        return QAbstractTextDocumentLayout()
    def setDocumentLayout(self, layout):
        '''void QTextDocument.setDocumentLayout(QAbstractTextDocumentLayout layout)'''
    def isRedoAvailable(self):
        '''bool QTextDocument.isRedoAvailable()'''
        return bool()
    def isUndoAvailable(self):
        '''bool QTextDocument.isUndoAvailable()'''
        return bool()
    def isUndoRedoEnabled(self):
        '''bool QTextDocument.isUndoRedoEnabled()'''
        return bool()
    def setUndoRedoEnabled(self, enable):
        '''void QTextDocument.setUndoRedoEnabled(bool enable)'''
    def clear(self):
        '''void QTextDocument.clear()'''
    def isEmpty(self):
        '''bool QTextDocument.isEmpty()'''
        return bool()
    def clone(self, parent = None):
        '''QTextDocument QTextDocument.clone(QObject parent = None)'''
        return QTextDocument()
    class FindFlags():
        """"""
        def __init__(self):
            '''QTextDocument.FindFlags QTextDocument.FindFlags.__init__()'''
            return QTextDocument.FindFlags()
        def __init__(self):
            '''int QTextDocument.FindFlags.__init__()'''
            return int()
        def __init__(self):
            '''void QTextDocument.FindFlags.__init__()'''
        def __bool__(self):
            '''int QTextDocument.FindFlags.__bool__()'''
            return int()
        def __ne__(self, f):
            '''bool QTextDocument.FindFlags.__ne__(QTextDocument.FindFlags f)'''
            return bool()
        def __eq__(self, f):
            '''bool QTextDocument.FindFlags.__eq__(QTextDocument.FindFlags f)'''
            return bool()
        def __invert__(self):
            '''QTextDocument.FindFlags QTextDocument.FindFlags.__invert__()'''
            return QTextDocument.FindFlags()
        def __and__(self, mask):
            '''QTextDocument.FindFlags QTextDocument.FindFlags.__and__(int mask)'''
            return QTextDocument.FindFlags()
        def __xor__(self, f):
            '''QTextDocument.FindFlags QTextDocument.FindFlags.__xor__(QTextDocument.FindFlags f)'''
            return QTextDocument.FindFlags()
        def __xor__(self, f):
            '''QTextDocument.FindFlags QTextDocument.FindFlags.__xor__(int f)'''
            return QTextDocument.FindFlags()
        def __or__(self, f):
            '''QTextDocument.FindFlags QTextDocument.FindFlags.__or__(QTextDocument.FindFlags f)'''
            return QTextDocument.FindFlags()
        def __or__(self, f):
            '''QTextDocument.FindFlags QTextDocument.FindFlags.__or__(int f)'''
            return QTextDocument.FindFlags()
        def __int__(self):
            '''int QTextDocument.FindFlags.__int__()'''
            return int()
        def __ixor__(self, f):
            '''QTextDocument.FindFlags QTextDocument.FindFlags.__ixor__(QTextDocument.FindFlags f)'''
            return QTextDocument.FindFlags()
        def __ior__(self, f):
            '''QTextDocument.FindFlags QTextDocument.FindFlags.__ior__(QTextDocument.FindFlags f)'''
            return QTextDocument.FindFlags()
        def __iand__(self, mask):
            '''QTextDocument.FindFlags QTextDocument.FindFlags.__iand__(int mask)'''
            return QTextDocument.FindFlags()


class QTextDocumentFragment():
    """"""
    def __init__(self):
        '''void QTextDocumentFragment.__init__()'''
    def __init__(self, document):
        '''void QTextDocumentFragment.__init__(QTextDocument document)'''
    def __init__(self, range):
        '''void QTextDocumentFragment.__init__(QTextCursor range)'''
    def __init__(self, rhs):
        '''void QTextDocumentFragment.__init__(QTextDocumentFragment rhs)'''
    def fromHtml(self, html):
        '''static QTextDocumentFragment QTextDocumentFragment.fromHtml(str html)'''
        return QTextDocumentFragment()
    def fromHtml(self, html, resourceProvider):
        '''static QTextDocumentFragment QTextDocumentFragment.fromHtml(str html, QTextDocument resourceProvider)'''
        return QTextDocumentFragment()
    def fromPlainText(self, plainText):
        '''static QTextDocumentFragment QTextDocumentFragment.fromPlainText(str plainText)'''
        return QTextDocumentFragment()
    def toHtml(self, encoding = QByteArray()):
        '''str QTextDocumentFragment.toHtml(QByteArray encoding = QByteArray())'''
        return str()
    def toPlainText(self):
        '''str QTextDocumentFragment.toPlainText()'''
        return str()
    def isEmpty(self):
        '''bool QTextDocumentFragment.isEmpty()'''
        return bool()


class QTextDocumentWriter():
    """"""
    def __init__(self):
        '''void QTextDocumentWriter.__init__()'''
    def __init__(self, device, format):
        '''void QTextDocumentWriter.__init__(QIODevice device, QByteArray format)'''
    def __init__(self, fileName, format = QByteArray()):
        '''void QTextDocumentWriter.__init__(str fileName, QByteArray format = QByteArray())'''
    def supportedDocumentFormats(self):
        '''static list-of-QByteArray QTextDocumentWriter.supportedDocumentFormats()'''
        return [QByteArray()]
    def codec(self):
        '''QTextCodec QTextDocumentWriter.codec()'''
        return QTextCodec()
    def setCodec(self, codec):
        '''void QTextDocumentWriter.setCodec(QTextCodec codec)'''
    def write(self, document):
        '''bool QTextDocumentWriter.write(QTextDocument document)'''
        return bool()
    def write(self, fragment):
        '''bool QTextDocumentWriter.write(QTextDocumentFragment fragment)'''
        return bool()
    def fileName(self):
        '''str QTextDocumentWriter.fileName()'''
        return str()
    def setFileName(self, fileName):
        '''void QTextDocumentWriter.setFileName(str fileName)'''
    def device(self):
        '''QIODevice QTextDocumentWriter.device()'''
        return QIODevice()
    def setDevice(self, device):
        '''void QTextDocumentWriter.setDevice(QIODevice device)'''
    def format(self):
        '''QByteArray QTextDocumentWriter.format()'''
        return QByteArray()
    def setFormat(self, format):
        '''void QTextDocumentWriter.setFormat(QByteArray format)'''


class QTextLength():
    """"""
    # Enum QTextLength.Type
    VariableLength = 0
    FixedLength = 0
    PercentageLength = 0

    def __init__(self):
        '''void QTextLength.__init__()'''
    def __init__(self, atype, avalue):
        '''void QTextLength.__init__(QTextLength.Type atype, float avalue)'''
    def __init__(self, variant):
        '''void QTextLength.__init__(QVariant variant)'''
    def __init__(self):
        '''QTextLength QTextLength.__init__()'''
        return QTextLength()
    def __ne__(self, other):
        '''bool QTextLength.__ne__(QTextLength other)'''
        return bool()
    def __eq__(self, other):
        '''bool QTextLength.__eq__(QTextLength other)'''
        return bool()
    def rawValue(self):
        '''float QTextLength.rawValue()'''
        return float()
    def value(self, maximumLength):
        '''float QTextLength.value(float maximumLength)'''
        return float()
    def type(self):
        '''QTextLength.Type QTextLength.type()'''
        return QTextLength.Type()


class QTextFormat():
    """"""
    # Enum QTextFormat.Property
    ObjectIndex = 0
    CssFloat = 0
    LayoutDirection = 0
    OutlinePen = 0
    BackgroundBrush = 0
    ForegroundBrush = 0
    BlockAlignment = 0
    BlockTopMargin = 0
    BlockBottomMargin = 0
    BlockLeftMargin = 0
    BlockRightMargin = 0
    TextIndent = 0
    BlockIndent = 0
    BlockNonBreakableLines = 0
    BlockTrailingHorizontalRulerWidth = 0
    FontFamily = 0
    FontPointSize = 0
    FontSizeAdjustment = 0
    FontSizeIncrement = 0
    FontWeight = 0
    FontItalic = 0
    FontUnderline = 0
    FontOverline = 0
    FontStrikeOut = 0
    FontFixedPitch = 0
    FontPixelSize = 0
    TextUnderlineColor = 0
    TextVerticalAlignment = 0
    TextOutline = 0
    IsAnchor = 0
    AnchorHref = 0
    AnchorName = 0
    ObjectType = 0
    ListStyle = 0
    ListIndent = 0
    FrameBorder = 0
    FrameMargin = 0
    FramePadding = 0
    FrameWidth = 0
    FrameHeight = 0
    TableColumns = 0
    TableColumnWidthConstraints = 0
    TableCellSpacing = 0
    TableCellPadding = 0
    TableCellRowSpan = 0
    TableCellColumnSpan = 0
    ImageName = 0
    ImageWidth = 0
    ImageHeight = 0
    TextUnderlineStyle = 0
    TableHeaderRowCount = 0
    FullWidthSelection = 0
    PageBreakPolicy = 0
    TextToolTip = 0
    FrameTopMargin = 0
    FrameBottomMargin = 0
    FrameLeftMargin = 0
    FrameRightMargin = 0
    FrameBorderBrush = 0
    FrameBorderStyle = 0
    BackgroundImageUrl = 0
    TabPositions = 0
    FirstFontProperty = 0
    FontCapitalization = 0
    FontLetterSpacing = 0
    FontWordSpacing = 0
    LastFontProperty = 0
    TableCellTopPadding = 0
    TableCellBottomPadding = 0
    TableCellLeftPadding = 0
    TableCellRightPadding = 0
    FontStyleHint = 0
    FontStyleStrategy = 0
    FontKerning = 0
    LineHeight = 0
    LineHeightType = 0
    FontHintingPreference = 0
    ListNumberPrefix = 0
    ListNumberSuffix = 0
    FontStretch = 0
    FontLetterSpacingType = 0
    UserProperty = 0

    # Enum QTextFormat.PageBreakFlag
    PageBreak_Auto = 0
    PageBreak_AlwaysBefore = 0
    PageBreak_AlwaysAfter = 0

    # Enum QTextFormat.ObjectTypes
    NoObject = 0
    ImageObject = 0
    TableObject = 0
    TableCellObject = 0
    UserObject = 0

    # Enum QTextFormat.FormatType
    InvalidFormat = 0
    BlockFormat = 0
    CharFormat = 0
    ListFormat = 0
    TableFormat = 0
    FrameFormat = 0
    UserFormat = 0

    def __init__(self):
        '''void QTextFormat.__init__()'''
    def __init__(self, type):
        '''void QTextFormat.__init__(int type)'''
    def __init__(self, rhs):
        '''void QTextFormat.__init__(QTextFormat rhs)'''
    def __init__(self, variant):
        '''void QTextFormat.__init__(QVariant variant)'''
    def isEmpty(self):
        '''bool QTextFormat.isEmpty()'''
        return bool()
    def swap(self, other):
        '''void QTextFormat.swap(QTextFormat other)'''
    def toTableCellFormat(self):
        '''QTextTableCellFormat QTextFormat.toTableCellFormat()'''
        return QTextTableCellFormat()
    def isTableCellFormat(self):
        '''bool QTextFormat.isTableCellFormat()'''
        return bool()
    def propertyCount(self):
        '''int QTextFormat.propertyCount()'''
        return int()
    def setObjectType(self, atype):
        '''void QTextFormat.setObjectType(int atype)'''
    def clearForeground(self):
        '''void QTextFormat.clearForeground()'''
    def foreground(self):
        '''QBrush QTextFormat.foreground()'''
        return QBrush()
    def setForeground(self, brush):
        '''void QTextFormat.setForeground(QBrush brush)'''
    def clearBackground(self):
        '''void QTextFormat.clearBackground()'''
    def background(self):
        '''QBrush QTextFormat.background()'''
        return QBrush()
    def setBackground(self, brush):
        '''void QTextFormat.setBackground(QBrush brush)'''
    def layoutDirection(self):
        '''Qt.LayoutDirection QTextFormat.layoutDirection()'''
        return Qt.LayoutDirection()
    def setLayoutDirection(self, direction):
        '''void QTextFormat.setLayoutDirection(Qt.LayoutDirection direction)'''
    def __ne__(self, rhs):
        '''bool QTextFormat.__ne__(QTextFormat rhs)'''
        return bool()
    def __eq__(self, rhs):
        '''bool QTextFormat.__eq__(QTextFormat rhs)'''
        return bool()
    def toImageFormat(self):
        '''QTextImageFormat QTextFormat.toImageFormat()'''
        return QTextImageFormat()
    def toFrameFormat(self):
        '''QTextFrameFormat QTextFormat.toFrameFormat()'''
        return QTextFrameFormat()
    def toTableFormat(self):
        '''QTextTableFormat QTextFormat.toTableFormat()'''
        return QTextTableFormat()
    def toListFormat(self):
        '''QTextListFormat QTextFormat.toListFormat()'''
        return QTextListFormat()
    def toCharFormat(self):
        '''QTextCharFormat QTextFormat.toCharFormat()'''
        return QTextCharFormat()
    def toBlockFormat(self):
        '''QTextBlockFormat QTextFormat.toBlockFormat()'''
        return QTextBlockFormat()
    def isTableFormat(self):
        '''bool QTextFormat.isTableFormat()'''
        return bool()
    def isImageFormat(self):
        '''bool QTextFormat.isImageFormat()'''
        return bool()
    def isFrameFormat(self):
        '''bool QTextFormat.isFrameFormat()'''
        return bool()
    def isListFormat(self):
        '''bool QTextFormat.isListFormat()'''
        return bool()
    def isBlockFormat(self):
        '''bool QTextFormat.isBlockFormat()'''
        return bool()
    def isCharFormat(self):
        '''bool QTextFormat.isCharFormat()'''
        return bool()
    def objectType(self):
        '''int QTextFormat.objectType()'''
        return int()
    def properties(self):
        '''dict-of-int-QVariant QTextFormat.properties()'''
        return {int():QVariant()}
    def lengthVectorProperty(self, propertyId):
        '''list-of-QTextLength QTextFormat.lengthVectorProperty(int propertyId)'''
        return [QTextLength()]
    def lengthProperty(self, propertyId):
        '''QTextLength QTextFormat.lengthProperty(int propertyId)'''
        return QTextLength()
    def brushProperty(self, propertyId):
        '''QBrush QTextFormat.brushProperty(int propertyId)'''
        return QBrush()
    def penProperty(self, propertyId):
        '''QPen QTextFormat.penProperty(int propertyId)'''
        return QPen()
    def colorProperty(self, propertyId):
        '''QColor QTextFormat.colorProperty(int propertyId)'''
        return QColor()
    def stringProperty(self, propertyId):
        '''str QTextFormat.stringProperty(int propertyId)'''
        return str()
    def doubleProperty(self, propertyId):
        '''float QTextFormat.doubleProperty(int propertyId)'''
        return float()
    def intProperty(self, propertyId):
        '''int QTextFormat.intProperty(int propertyId)'''
        return int()
    def boolProperty(self, propertyId):
        '''bool QTextFormat.boolProperty(int propertyId)'''
        return bool()
    def hasProperty(self, propertyId):
        '''bool QTextFormat.hasProperty(int propertyId)'''
        return bool()
    def clearProperty(self, propertyId):
        '''void QTextFormat.clearProperty(int propertyId)'''
    def setProperty(self, propertyId, value):
        '''void QTextFormat.setProperty(int propertyId, QVariant value)'''
    def setProperty(self, propertyId, lengths):
        '''void QTextFormat.setProperty(int propertyId, list-of-QTextLength lengths)'''
    def property(self, propertyId):
        '''QVariant QTextFormat.property(int propertyId)'''
        return QVariant()
    def setObjectIndex(self, object):
        '''void QTextFormat.setObjectIndex(int object)'''
    def objectIndex(self):
        '''int QTextFormat.objectIndex()'''
        return int()
    def type(self):
        '''int QTextFormat.type()'''
        return int()
    def isValid(self):
        '''bool QTextFormat.isValid()'''
        return bool()
    def merge(self, other):
        '''void QTextFormat.merge(QTextFormat other)'''
    class PageBreakFlags():
        """"""
        def __init__(self):
            '''QTextFormat.PageBreakFlags QTextFormat.PageBreakFlags.__init__()'''
            return QTextFormat.PageBreakFlags()
        def __init__(self):
            '''int QTextFormat.PageBreakFlags.__init__()'''
            return int()
        def __init__(self):
            '''void QTextFormat.PageBreakFlags.__init__()'''
        def __bool__(self):
            '''int QTextFormat.PageBreakFlags.__bool__()'''
            return int()
        def __ne__(self, f):
            '''bool QTextFormat.PageBreakFlags.__ne__(QTextFormat.PageBreakFlags f)'''
            return bool()
        def __eq__(self, f):
            '''bool QTextFormat.PageBreakFlags.__eq__(QTextFormat.PageBreakFlags f)'''
            return bool()
        def __invert__(self):
            '''QTextFormat.PageBreakFlags QTextFormat.PageBreakFlags.__invert__()'''
            return QTextFormat.PageBreakFlags()
        def __and__(self, mask):
            '''QTextFormat.PageBreakFlags QTextFormat.PageBreakFlags.__and__(int mask)'''
            return QTextFormat.PageBreakFlags()
        def __xor__(self, f):
            '''QTextFormat.PageBreakFlags QTextFormat.PageBreakFlags.__xor__(QTextFormat.PageBreakFlags f)'''
            return QTextFormat.PageBreakFlags()
        def __xor__(self, f):
            '''QTextFormat.PageBreakFlags QTextFormat.PageBreakFlags.__xor__(int f)'''
            return QTextFormat.PageBreakFlags()
        def __or__(self, f):
            '''QTextFormat.PageBreakFlags QTextFormat.PageBreakFlags.__or__(QTextFormat.PageBreakFlags f)'''
            return QTextFormat.PageBreakFlags()
        def __or__(self, f):
            '''QTextFormat.PageBreakFlags QTextFormat.PageBreakFlags.__or__(int f)'''
            return QTextFormat.PageBreakFlags()
        def __int__(self):
            '''int QTextFormat.PageBreakFlags.__int__()'''
            return int()
        def __ixor__(self, f):
            '''QTextFormat.PageBreakFlags QTextFormat.PageBreakFlags.__ixor__(QTextFormat.PageBreakFlags f)'''
            return QTextFormat.PageBreakFlags()
        def __ior__(self, f):
            '''QTextFormat.PageBreakFlags QTextFormat.PageBreakFlags.__ior__(QTextFormat.PageBreakFlags f)'''
            return QTextFormat.PageBreakFlags()
        def __iand__(self, mask):
            '''QTextFormat.PageBreakFlags QTextFormat.PageBreakFlags.__iand__(int mask)'''
            return QTextFormat.PageBreakFlags()


class QTextCharFormat(QTextFormat):
    """"""
    # Enum QTextCharFormat.FontPropertiesInheritanceBehavior
    FontPropertiesSpecifiedOnly = 0
    FontPropertiesAll = 0

    # Enum QTextCharFormat.UnderlineStyle
    NoUnderline = 0
    SingleUnderline = 0
    DashUnderline = 0
    DotLine = 0
    DashDotLine = 0
    DashDotDotLine = 0
    WaveUnderline = 0
    SpellCheckUnderline = 0

    # Enum QTextCharFormat.VerticalAlignment
    AlignNormal = 0
    AlignSuperScript = 0
    AlignSubScript = 0
    AlignMiddle = 0
    AlignTop = 0
    AlignBottom = 0
    AlignBaseline = 0

    def __init__(self):
        '''void QTextCharFormat.__init__()'''
    def __init__(self):
        '''QTextCharFormat QTextCharFormat.__init__()'''
        return QTextCharFormat()
    def fontLetterSpacingType(self):
        '''QFont.SpacingType QTextCharFormat.fontLetterSpacingType()'''
        return QFont.SpacingType()
    def setFontLetterSpacingType(self, letterSpacingType):
        '''void QTextCharFormat.setFontLetterSpacingType(QFont.SpacingType letterSpacingType)'''
    def setFontStretch(self, factor):
        '''void QTextCharFormat.setFontStretch(int factor)'''
    def fontStretch(self):
        '''int QTextCharFormat.fontStretch()'''
        return int()
    def fontHintingPreference(self):
        '''QFont.HintingPreference QTextCharFormat.fontHintingPreference()'''
        return QFont.HintingPreference()
    def setFontHintingPreference(self, hintingPreference):
        '''void QTextCharFormat.setFontHintingPreference(QFont.HintingPreference hintingPreference)'''
    def fontKerning(self):
        '''bool QTextCharFormat.fontKerning()'''
        return bool()
    def setFontKerning(self, enable):
        '''void QTextCharFormat.setFontKerning(bool enable)'''
    def fontStyleStrategy(self):
        '''QFont.StyleStrategy QTextCharFormat.fontStyleStrategy()'''
        return QFont.StyleStrategy()
    def fontStyleHint(self):
        '''QFont.StyleHint QTextCharFormat.fontStyleHint()'''
        return QFont.StyleHint()
    def setFontStyleStrategy(self, strategy):
        '''void QTextCharFormat.setFontStyleStrategy(QFont.StyleStrategy strategy)'''
    def setFontStyleHint(self, hint, strategy = None):
        '''void QTextCharFormat.setFontStyleHint(QFont.StyleHint hint, QFont.StyleStrategy strategy = QFont.PreferDefault)'''
    def fontWordSpacing(self):
        '''float QTextCharFormat.fontWordSpacing()'''
        return float()
    def setFontWordSpacing(self, spacing):
        '''void QTextCharFormat.setFontWordSpacing(float spacing)'''
    def fontLetterSpacing(self):
        '''float QTextCharFormat.fontLetterSpacing()'''
        return float()
    def setFontLetterSpacing(self, spacing):
        '''void QTextCharFormat.setFontLetterSpacing(float spacing)'''
    def fontCapitalization(self):
        '''QFont.Capitalization QTextCharFormat.fontCapitalization()'''
        return QFont.Capitalization()
    def setFontCapitalization(self, capitalization):
        '''void QTextCharFormat.setFontCapitalization(QFont.Capitalization capitalization)'''
    def anchorNames(self):
        '''list-of-str QTextCharFormat.anchorNames()'''
        return [str()]
    def setAnchorNames(self, names):
        '''void QTextCharFormat.setAnchorNames(list-of-str names)'''
    def toolTip(self):
        '''str QTextCharFormat.toolTip()'''
        return str()
    def setToolTip(self, tip):
        '''void QTextCharFormat.setToolTip(str tip)'''
    def underlineStyle(self):
        '''QTextCharFormat.UnderlineStyle QTextCharFormat.underlineStyle()'''
        return QTextCharFormat.UnderlineStyle()
    def setUnderlineStyle(self, style):
        '''void QTextCharFormat.setUnderlineStyle(QTextCharFormat.UnderlineStyle style)'''
    def textOutline(self):
        '''QPen QTextCharFormat.textOutline()'''
        return QPen()
    def setTextOutline(self, pen):
        '''void QTextCharFormat.setTextOutline(QPen pen)'''
    def setTableCellColumnSpan(self, atableCellColumnSpan):
        '''void QTextCharFormat.setTableCellColumnSpan(int atableCellColumnSpan)'''
    def setTableCellRowSpan(self, atableCellRowSpan):
        '''void QTextCharFormat.setTableCellRowSpan(int atableCellRowSpan)'''
    def tableCellColumnSpan(self):
        '''int QTextCharFormat.tableCellColumnSpan()'''
        return int()
    def tableCellRowSpan(self):
        '''int QTextCharFormat.tableCellRowSpan()'''
        return int()
    def anchorHref(self):
        '''str QTextCharFormat.anchorHref()'''
        return str()
    def setAnchorHref(self, value):
        '''void QTextCharFormat.setAnchorHref(str value)'''
    def isAnchor(self):
        '''bool QTextCharFormat.isAnchor()'''
        return bool()
    def setAnchor(self, anchor):
        '''void QTextCharFormat.setAnchor(bool anchor)'''
    def verticalAlignment(self):
        '''QTextCharFormat.VerticalAlignment QTextCharFormat.verticalAlignment()'''
        return QTextCharFormat.VerticalAlignment()
    def setVerticalAlignment(self, alignment):
        '''void QTextCharFormat.setVerticalAlignment(QTextCharFormat.VerticalAlignment alignment)'''
    def fontFixedPitch(self):
        '''bool QTextCharFormat.fontFixedPitch()'''
        return bool()
    def setFontFixedPitch(self, fixedPitch):
        '''void QTextCharFormat.setFontFixedPitch(bool fixedPitch)'''
    def underlineColor(self):
        '''QColor QTextCharFormat.underlineColor()'''
        return QColor()
    def setUnderlineColor(self, color):
        '''void QTextCharFormat.setUnderlineColor(QColor color)'''
    def fontStrikeOut(self):
        '''bool QTextCharFormat.fontStrikeOut()'''
        return bool()
    def setFontStrikeOut(self, strikeOut):
        '''void QTextCharFormat.setFontStrikeOut(bool strikeOut)'''
    def fontOverline(self):
        '''bool QTextCharFormat.fontOverline()'''
        return bool()
    def setFontOverline(self, overline):
        '''void QTextCharFormat.setFontOverline(bool overline)'''
    def fontUnderline(self):
        '''bool QTextCharFormat.fontUnderline()'''
        return bool()
    def setFontUnderline(self, underline):
        '''void QTextCharFormat.setFontUnderline(bool underline)'''
    def fontItalic(self):
        '''bool QTextCharFormat.fontItalic()'''
        return bool()
    def setFontItalic(self, italic):
        '''void QTextCharFormat.setFontItalic(bool italic)'''
    def fontWeight(self):
        '''int QTextCharFormat.fontWeight()'''
        return int()
    def setFontWeight(self, weight):
        '''void QTextCharFormat.setFontWeight(int weight)'''
    def fontPointSize(self):
        '''float QTextCharFormat.fontPointSize()'''
        return float()
    def setFontPointSize(self, size):
        '''void QTextCharFormat.setFontPointSize(float size)'''
    def fontFamily(self):
        '''str QTextCharFormat.fontFamily()'''
        return str()
    def setFontFamily(self, family):
        '''void QTextCharFormat.setFontFamily(str family)'''
    def font(self):
        '''QFont QTextCharFormat.font()'''
        return QFont()
    def setFont(self, font):
        '''void QTextCharFormat.setFont(QFont font)'''
    def setFont(self, font, behavior):
        '''void QTextCharFormat.setFont(QFont font, QTextCharFormat.FontPropertiesInheritanceBehavior behavior)'''
    def isValid(self):
        '''bool QTextCharFormat.isValid()'''
        return bool()


class QTextBlockFormat(QTextFormat):
    """"""
    # Enum QTextBlockFormat.LineHeightTypes
    SingleHeight = 0
    ProportionalHeight = 0
    FixedHeight = 0
    MinimumHeight = 0
    LineDistanceHeight = 0

    def __init__(self):
        '''void QTextBlockFormat.__init__()'''
    def __init__(self):
        '''QTextBlockFormat QTextBlockFormat.__init__()'''
        return QTextBlockFormat()
    def lineHeightType(self):
        '''int QTextBlockFormat.lineHeightType()'''
        return int()
    def lineHeight(self, scriptLineHeight, scaling):
        '''float QTextBlockFormat.lineHeight(float scriptLineHeight, float scaling)'''
        return float()
    def lineHeight(self):
        '''float QTextBlockFormat.lineHeight()'''
        return float()
    def setLineHeight(self, height, heightType):
        '''void QTextBlockFormat.setLineHeight(float height, int heightType)'''
    def tabPositions(self):
        '''list-of-QTextOption.Tab QTextBlockFormat.tabPositions()'''
        return [QTextOption.Tab()]
    def setTabPositions(self, tabs):
        '''void QTextBlockFormat.setTabPositions(list-of-QTextOption.Tab tabs)'''
    def pageBreakPolicy(self):
        '''QTextFormat.PageBreakFlags QTextBlockFormat.pageBreakPolicy()'''
        return QTextFormat.PageBreakFlags()
    def setPageBreakPolicy(self, flags):
        '''void QTextBlockFormat.setPageBreakPolicy(QTextFormat.PageBreakFlags flags)'''
    def setIndent(self, aindent):
        '''void QTextBlockFormat.setIndent(int aindent)'''
    def setAlignment(self, aalignment):
        '''void QTextBlockFormat.setAlignment(Qt.Alignment aalignment)'''
    def nonBreakableLines(self):
        '''bool QTextBlockFormat.nonBreakableLines()'''
        return bool()
    def setNonBreakableLines(self, b):
        '''void QTextBlockFormat.setNonBreakableLines(bool b)'''
    def indent(self):
        '''int QTextBlockFormat.indent()'''
        return int()
    def textIndent(self):
        '''float QTextBlockFormat.textIndent()'''
        return float()
    def setTextIndent(self, margin):
        '''void QTextBlockFormat.setTextIndent(float margin)'''
    def rightMargin(self):
        '''float QTextBlockFormat.rightMargin()'''
        return float()
    def setRightMargin(self, margin):
        '''void QTextBlockFormat.setRightMargin(float margin)'''
    def leftMargin(self):
        '''float QTextBlockFormat.leftMargin()'''
        return float()
    def setLeftMargin(self, margin):
        '''void QTextBlockFormat.setLeftMargin(float margin)'''
    def bottomMargin(self):
        '''float QTextBlockFormat.bottomMargin()'''
        return float()
    def setBottomMargin(self, margin):
        '''void QTextBlockFormat.setBottomMargin(float margin)'''
    def topMargin(self):
        '''float QTextBlockFormat.topMargin()'''
        return float()
    def setTopMargin(self, margin):
        '''void QTextBlockFormat.setTopMargin(float margin)'''
    def alignment(self):
        '''Qt.Alignment QTextBlockFormat.alignment()'''
        return Qt.Alignment()
    def isValid(self):
        '''bool QTextBlockFormat.isValid()'''
        return bool()


class QTextListFormat(QTextFormat):
    """"""
    # Enum QTextListFormat.Style
    ListDisc = 0
    ListCircle = 0
    ListSquare = 0
    ListDecimal = 0
    ListLowerAlpha = 0
    ListUpperAlpha = 0
    ListLowerRoman = 0
    ListUpperRoman = 0

    def __init__(self):
        '''void QTextListFormat.__init__()'''
    def __init__(self):
        '''QTextListFormat QTextListFormat.__init__()'''
        return QTextListFormat()
    def setNumberSuffix(self, ns):
        '''void QTextListFormat.setNumberSuffix(str ns)'''
    def setNumberPrefix(self, np):
        '''void QTextListFormat.setNumberPrefix(str np)'''
    def numberSuffix(self):
        '''str QTextListFormat.numberSuffix()'''
        return str()
    def numberPrefix(self):
        '''str QTextListFormat.numberPrefix()'''
        return str()
    def setIndent(self, aindent):
        '''void QTextListFormat.setIndent(int aindent)'''
    def setStyle(self, astyle):
        '''void QTextListFormat.setStyle(QTextListFormat.Style astyle)'''
    def indent(self):
        '''int QTextListFormat.indent()'''
        return int()
    def style(self):
        '''QTextListFormat.Style QTextListFormat.style()'''
        return QTextListFormat.Style()
    def isValid(self):
        '''bool QTextListFormat.isValid()'''
        return bool()


class QTextImageFormat(QTextCharFormat):
    """"""
    def __init__(self):
        '''void QTextImageFormat.__init__()'''
    def __init__(self):
        '''QTextImageFormat QTextImageFormat.__init__()'''
        return QTextImageFormat()
    def setHeight(self, aheight):
        '''void QTextImageFormat.setHeight(float aheight)'''
    def setWidth(self, awidth):
        '''void QTextImageFormat.setWidth(float awidth)'''
    def setName(self, aname):
        '''void QTextImageFormat.setName(str aname)'''
    def height(self):
        '''float QTextImageFormat.height()'''
        return float()
    def width(self):
        '''float QTextImageFormat.width()'''
        return float()
    def name(self):
        '''str QTextImageFormat.name()'''
        return str()
    def isValid(self):
        '''bool QTextImageFormat.isValid()'''
        return bool()


class QTextFrameFormat(QTextFormat):
    """"""
    # Enum QTextFrameFormat.BorderStyle
    BorderStyle_None = 0
    BorderStyle_Dotted = 0
    BorderStyle_Dashed = 0
    BorderStyle_Solid = 0
    BorderStyle_Double = 0
    BorderStyle_DotDash = 0
    BorderStyle_DotDotDash = 0
    BorderStyle_Groove = 0
    BorderStyle_Ridge = 0
    BorderStyle_Inset = 0
    BorderStyle_Outset = 0

    # Enum QTextFrameFormat.Position
    InFlow = 0
    FloatLeft = 0
    FloatRight = 0

    def __init__(self):
        '''void QTextFrameFormat.__init__()'''
    def __init__(self):
        '''QTextFrameFormat QTextFrameFormat.__init__()'''
        return QTextFrameFormat()
    def setRightMargin(self, amargin):
        '''void QTextFrameFormat.setRightMargin(float amargin)'''
    def setLeftMargin(self, amargin):
        '''void QTextFrameFormat.setLeftMargin(float amargin)'''
    def setBottomMargin(self, amargin):
        '''void QTextFrameFormat.setBottomMargin(float amargin)'''
    def setTopMargin(self, amargin):
        '''void QTextFrameFormat.setTopMargin(float amargin)'''
    def rightMargin(self):
        '''float QTextFrameFormat.rightMargin()'''
        return float()
    def leftMargin(self):
        '''float QTextFrameFormat.leftMargin()'''
        return float()
    def bottomMargin(self):
        '''float QTextFrameFormat.bottomMargin()'''
        return float()
    def topMargin(self):
        '''float QTextFrameFormat.topMargin()'''
        return float()
    def borderStyle(self):
        '''QTextFrameFormat.BorderStyle QTextFrameFormat.borderStyle()'''
        return QTextFrameFormat.BorderStyle()
    def setBorderStyle(self, style):
        '''void QTextFrameFormat.setBorderStyle(QTextFrameFormat.BorderStyle style)'''
    def borderBrush(self):
        '''QBrush QTextFrameFormat.borderBrush()'''
        return QBrush()
    def setBorderBrush(self, brush):
        '''void QTextFrameFormat.setBorderBrush(QBrush brush)'''
    def pageBreakPolicy(self):
        '''QTextFormat.PageBreakFlags QTextFrameFormat.pageBreakPolicy()'''
        return QTextFormat.PageBreakFlags()
    def setPageBreakPolicy(self, flags):
        '''void QTextFrameFormat.setPageBreakPolicy(QTextFormat.PageBreakFlags flags)'''
    def setHeight(self, aheight):
        '''void QTextFrameFormat.setHeight(float aheight)'''
    def setHeight(self, aheight):
        '''void QTextFrameFormat.setHeight(QTextLength aheight)'''
    def setPadding(self, apadding):
        '''void QTextFrameFormat.setPadding(float apadding)'''
    def setMargin(self, amargin):
        '''void QTextFrameFormat.setMargin(float amargin)'''
    def setBorder(self, aborder):
        '''void QTextFrameFormat.setBorder(float aborder)'''
    def height(self):
        '''QTextLength QTextFrameFormat.height()'''
        return QTextLength()
    def width(self):
        '''QTextLength QTextFrameFormat.width()'''
        return QTextLength()
    def setWidth(self, length):
        '''void QTextFrameFormat.setWidth(QTextLength length)'''
    def setWidth(self, awidth):
        '''void QTextFrameFormat.setWidth(float awidth)'''
    def padding(self):
        '''float QTextFrameFormat.padding()'''
        return float()
    def margin(self):
        '''float QTextFrameFormat.margin()'''
        return float()
    def border(self):
        '''float QTextFrameFormat.border()'''
        return float()
    def position(self):
        '''QTextFrameFormat.Position QTextFrameFormat.position()'''
        return QTextFrameFormat.Position()
    def setPosition(self, f):
        '''void QTextFrameFormat.setPosition(QTextFrameFormat.Position f)'''
    def isValid(self):
        '''bool QTextFrameFormat.isValid()'''
        return bool()


class QTextTableFormat(QTextFrameFormat):
    """"""
    def __init__(self):
        '''void QTextTableFormat.__init__()'''
    def __init__(self):
        '''QTextTableFormat QTextTableFormat.__init__()'''
        return QTextTableFormat()
    def headerRowCount(self):
        '''int QTextTableFormat.headerRowCount()'''
        return int()
    def setHeaderRowCount(self, count):
        '''void QTextTableFormat.setHeaderRowCount(int count)'''
    def setAlignment(self, aalignment):
        '''void QTextTableFormat.setAlignment(Qt.Alignment aalignment)'''
    def setCellPadding(self, apadding):
        '''void QTextTableFormat.setCellPadding(float apadding)'''
    def setColumns(self, acolumns):
        '''void QTextTableFormat.setColumns(int acolumns)'''
    def alignment(self):
        '''Qt.Alignment QTextTableFormat.alignment()'''
        return Qt.Alignment()
    def cellPadding(self):
        '''float QTextTableFormat.cellPadding()'''
        return float()
    def setCellSpacing(self, spacing):
        '''void QTextTableFormat.setCellSpacing(float spacing)'''
    def cellSpacing(self):
        '''float QTextTableFormat.cellSpacing()'''
        return float()
    def clearColumnWidthConstraints(self):
        '''void QTextTableFormat.clearColumnWidthConstraints()'''
    def columnWidthConstraints(self):
        '''list-of-QTextLength QTextTableFormat.columnWidthConstraints()'''
        return [QTextLength()]
    def setColumnWidthConstraints(self, constraints):
        '''void QTextTableFormat.setColumnWidthConstraints(list-of-QTextLength constraints)'''
    def columns(self):
        '''int QTextTableFormat.columns()'''
        return int()
    def isValid(self):
        '''bool QTextTableFormat.isValid()'''
        return bool()


class QTextTableCellFormat(QTextCharFormat):
    """"""
    def __init__(self):
        '''void QTextTableCellFormat.__init__()'''
    def __init__(self):
        '''QTextTableCellFormat QTextTableCellFormat.__init__()'''
        return QTextTableCellFormat()
    def setPadding(self, padding):
        '''void QTextTableCellFormat.setPadding(float padding)'''
    def rightPadding(self):
        '''float QTextTableCellFormat.rightPadding()'''
        return float()
    def setRightPadding(self, padding):
        '''void QTextTableCellFormat.setRightPadding(float padding)'''
    def leftPadding(self):
        '''float QTextTableCellFormat.leftPadding()'''
        return float()
    def setLeftPadding(self, padding):
        '''void QTextTableCellFormat.setLeftPadding(float padding)'''
    def bottomPadding(self):
        '''float QTextTableCellFormat.bottomPadding()'''
        return float()
    def setBottomPadding(self, padding):
        '''void QTextTableCellFormat.setBottomPadding(float padding)'''
    def topPadding(self):
        '''float QTextTableCellFormat.topPadding()'''
        return float()
    def setTopPadding(self, padding):
        '''void QTextTableCellFormat.setTopPadding(float padding)'''
    def isValid(self):
        '''bool QTextTableCellFormat.isValid()'''
        return bool()


class QTextInlineObject():
    """"""
    def __init__(self):
        '''void QTextInlineObject.__init__()'''
    def __init__(self):
        '''QTextInlineObject QTextInlineObject.__init__()'''
        return QTextInlineObject()
    def format(self):
        '''QTextFormat QTextInlineObject.format()'''
        return QTextFormat()
    def formatIndex(self):
        '''int QTextInlineObject.formatIndex()'''
        return int()
    def textPosition(self):
        '''int QTextInlineObject.textPosition()'''
        return int()
    def setDescent(self, d):
        '''void QTextInlineObject.setDescent(float d)'''
    def setAscent(self, a):
        '''void QTextInlineObject.setAscent(float a)'''
    def setWidth(self, w):
        '''void QTextInlineObject.setWidth(float w)'''
    def textDirection(self):
        '''Qt.LayoutDirection QTextInlineObject.textDirection()'''
        return Qt.LayoutDirection()
    def height(self):
        '''float QTextInlineObject.height()'''
        return float()
    def descent(self):
        '''float QTextInlineObject.descent()'''
        return float()
    def ascent(self):
        '''float QTextInlineObject.ascent()'''
        return float()
    def width(self):
        '''float QTextInlineObject.width()'''
        return float()
    def rect(self):
        '''QRectF QTextInlineObject.rect()'''
        return QRectF()
    def isValid(self):
        '''bool QTextInlineObject.isValid()'''
        return bool()


class QTextLayout():
    """"""
    # Enum QTextLayout.CursorMode
    SkipCharacters = 0
    SkipWords = 0

    def __init__(self):
        '''void QTextLayout.__init__()'''
    def __init__(self, text):
        '''void QTextLayout.__init__(str text)'''
    def __init__(self, text, font, paintDevice = None):
        '''void QTextLayout.__init__(str text, QFont font, QPaintDevice paintDevice = None)'''
    def __init__(self, b):
        '''void QTextLayout.__init__(QTextBlock b)'''
    def glyphRuns(self, from_ = None, length = None):
        '''list-of-QGlyphRun QTextLayout.glyphRuns(int from = -1, int length = -1)'''
        return [QGlyphRun()]
    def rightCursorPosition(self, oldPos):
        '''int QTextLayout.rightCursorPosition(int oldPos)'''
        return int()
    def leftCursorPosition(self, oldPos):
        '''int QTextLayout.leftCursorPosition(int oldPos)'''
        return int()
    def cursorMoveStyle(self):
        '''Qt.CursorMoveStyle QTextLayout.cursorMoveStyle()'''
        return Qt.CursorMoveStyle()
    def setCursorMoveStyle(self, style):
        '''void QTextLayout.setCursorMoveStyle(Qt.CursorMoveStyle style)'''
    def clearLayout(self):
        '''void QTextLayout.clearLayout()'''
    def maximumWidth(self):
        '''float QTextLayout.maximumWidth()'''
        return float()
    def minimumWidth(self):
        '''float QTextLayout.minimumWidth()'''
        return float()
    def boundingRect(self):
        '''QRectF QTextLayout.boundingRect()'''
        return QRectF()
    def setPosition(self, p):
        '''void QTextLayout.setPosition(QPointF p)'''
    def position(self):
        '''QPointF QTextLayout.position()'''
        return QPointF()
    def drawCursor(self, p, pos, cursorPosition):
        '''void QTextLayout.drawCursor(QPainter p, QPointF pos, int cursorPosition)'''
    def drawCursor(self, p, pos, cursorPosition, width):
        '''void QTextLayout.drawCursor(QPainter p, QPointF pos, int cursorPosition, int width)'''
    def draw(self, p, pos, selections = None, clip = QRectF()):
        '''void QTextLayout.draw(QPainter p, QPointF pos, list-of-QTextLayout.FormatRange selections = list-of-QTextLayout.FormatRange, QRectF clip = QRectF())'''
    def previousCursorPosition(self, oldPos, mode = None):
        '''int QTextLayout.previousCursorPosition(int oldPos, QTextLayout.CursorMode mode = QTextLayout.SkipCharacters)'''
        return int()
    def nextCursorPosition(self, oldPos, mode = None):
        '''int QTextLayout.nextCursorPosition(int oldPos, QTextLayout.CursorMode mode = QTextLayout.SkipCharacters)'''
        return int()
    def isValidCursorPosition(self, pos):
        '''bool QTextLayout.isValidCursorPosition(int pos)'''
        return bool()
    def lineForTextPosition(self, pos):
        '''QTextLine QTextLayout.lineForTextPosition(int pos)'''
        return QTextLine()
    def lineAt(self, i):
        '''QTextLine QTextLayout.lineAt(int i)'''
        return QTextLine()
    def lineCount(self):
        '''int QTextLayout.lineCount()'''
        return int()
    def createLine(self):
        '''QTextLine QTextLayout.createLine()'''
        return QTextLine()
    def endLayout(self):
        '''void QTextLayout.endLayout()'''
    def beginLayout(self):
        '''void QTextLayout.beginLayout()'''
    def cacheEnabled(self):
        '''bool QTextLayout.cacheEnabled()'''
        return bool()
    def setCacheEnabled(self, enable):
        '''void QTextLayout.setCacheEnabled(bool enable)'''
    def clearAdditionalFormats(self):
        '''void QTextLayout.clearAdditionalFormats()'''
    def additionalFormats(self):
        '''list-of-QTextLayout.FormatRange QTextLayout.additionalFormats()'''
        return [QTextLayout.FormatRange()]
    def setAdditionalFormats(self, overrides):
        '''void QTextLayout.setAdditionalFormats(list-of-QTextLayout.FormatRange overrides)'''
    def preeditAreaText(self):
        '''str QTextLayout.preeditAreaText()'''
        return str()
    def preeditAreaPosition(self):
        '''int QTextLayout.preeditAreaPosition()'''
        return int()
    def setPreeditArea(self, position, text):
        '''void QTextLayout.setPreeditArea(int position, str text)'''
    def textOption(self):
        '''QTextOption QTextLayout.textOption()'''
        return QTextOption()
    def setTextOption(self, option):
        '''void QTextLayout.setTextOption(QTextOption option)'''
    def text(self):
        '''str QTextLayout.text()'''
        return str()
    def setText(self, string):
        '''void QTextLayout.setText(str string)'''
    def font(self):
        '''QFont QTextLayout.font()'''
        return QFont()
    def setFont(self, f):
        '''void QTextLayout.setFont(QFont f)'''
    class FormatRange():
        """"""
        format = None # QTextCharFormat - member
        length = None # int - member
        start = None # int - member
        def __init__(self):
            '''void QTextLayout.FormatRange.__init__()'''
        def __init__(self):
            '''QTextLayout.FormatRange QTextLayout.FormatRange.__init__()'''
            return QTextLayout.FormatRange()


class QTextLine():
    """"""
    # Enum QTextLine.CursorPosition
    CursorBetweenCharacters = 0
    CursorOnCharacter = 0

    # Enum QTextLine.Edge
    Leading = 0
    Trailing = 0

    def __init__(self):
        '''void QTextLine.__init__()'''
    def __init__(self):
        '''QTextLine QTextLine.__init__()'''
        return QTextLine()
    def glyphRuns(self, from_ = None, length = None):
        '''list-of-QGlyphRun QTextLine.glyphRuns(int from = -1, int length = -1)'''
        return [QGlyphRun()]
    def horizontalAdvance(self):
        '''float QTextLine.horizontalAdvance()'''
        return float()
    def leadingIncluded(self):
        '''bool QTextLine.leadingIncluded()'''
        return bool()
    def setLeadingIncluded(self, included):
        '''void QTextLine.setLeadingIncluded(bool included)'''
    def leading(self):
        '''float QTextLine.leading()'''
        return float()
    def position(self):
        '''QPointF QTextLine.position()'''
        return QPointF()
    def draw(self, painter, position, selection = None):
        '''void QTextLine.draw(QPainter painter, QPointF position, QTextLayout.FormatRange selection = None)'''
    def lineNumber(self):
        '''int QTextLine.lineNumber()'''
        return int()
    def textLength(self):
        '''int QTextLine.textLength()'''
        return int()
    def textStart(self):
        '''int QTextLine.textStart()'''
        return int()
    def setPosition(self, pos):
        '''void QTextLine.setPosition(QPointF pos)'''
    def setNumColumns(self, columns):
        '''void QTextLine.setNumColumns(int columns)'''
    def setNumColumns(self, columns, alignmentWidth):
        '''void QTextLine.setNumColumns(int columns, float alignmentWidth)'''
    def setLineWidth(self, width):
        '''void QTextLine.setLineWidth(float width)'''
    def xToCursor(self, x, edge = None):
        '''int QTextLine.xToCursor(float x, QTextLine.CursorPosition edge = QTextLine.CursorBetweenCharacters)'''
        return int()
    def cursorToX(self, cursorPos, edge = None):
        '''float QTextLine.cursorToX(int cursorPos, QTextLine.Edge edge = QTextLine.Leading)'''
        return float()
    def naturalTextRect(self):
        '''QRectF QTextLine.naturalTextRect()'''
        return QRectF()
    def naturalTextWidth(self):
        '''float QTextLine.naturalTextWidth()'''
        return float()
    def height(self):
        '''float QTextLine.height()'''
        return float()
    def descent(self):
        '''float QTextLine.descent()'''
        return float()
    def ascent(self):
        '''float QTextLine.ascent()'''
        return float()
    def width(self):
        '''float QTextLine.width()'''
        return float()
    def y(self):
        '''float QTextLine.y()'''
        return float()
    def x(self):
        '''float QTextLine.x()'''
        return float()
    def rect(self):
        '''QRectF QTextLine.rect()'''
        return QRectF()
    def isValid(self):
        '''bool QTextLine.isValid()'''
        return bool()


class QTextObject(QObject):
    """"""
    def __init__(self, doc):
        '''void QTextObject.__init__(QTextDocument doc)'''
    def objectIndex(self):
        '''int QTextObject.objectIndex()'''
        return int()
    def document(self):
        '''QTextDocument QTextObject.document()'''
        return QTextDocument()
    def formatIndex(self):
        '''int QTextObject.formatIndex()'''
        return int()
    def format(self):
        '''QTextFormat QTextObject.format()'''
        return QTextFormat()
    def setFormat(self, format):
        '''void QTextObject.setFormat(QTextFormat format)'''


class QTextBlockGroup(QTextObject):
    """"""
    def __init__(self, doc):
        '''void QTextBlockGroup.__init__(QTextDocument doc)'''
    def blockList(self):
        '''list-of-QTextBlock QTextBlockGroup.blockList()'''
        return [QTextBlock()]
    def blockFormatChanged(self, block):
        '''void QTextBlockGroup.blockFormatChanged(QTextBlock block)'''
    def blockRemoved(self, block):
        '''void QTextBlockGroup.blockRemoved(QTextBlock block)'''
    def blockInserted(self, block):
        '''void QTextBlockGroup.blockInserted(QTextBlock block)'''


class QTextList(QTextBlockGroup):
    """"""
    def __init__(self, doc):
        '''void QTextList.__init__(QTextDocument doc)'''
    def setFormat(self, aformat):
        '''void QTextList.setFormat(QTextListFormat aformat)'''
    def format(self):
        '''QTextListFormat QTextList.format()'''
        return QTextListFormat()
    def add(self, block):
        '''void QTextList.add(QTextBlock block)'''
    def remove(self):
        '''QTextBlock QTextList.remove()'''
        return QTextBlock()
    def removeItem(self, i):
        '''void QTextList.removeItem(int i)'''
    def itemText(self):
        '''QTextBlock QTextList.itemText()'''
        return QTextBlock()
    def itemNumber(self):
        '''QTextBlock QTextList.itemNumber()'''
        return QTextBlock()
    def item(self, i):
        '''QTextBlock QTextList.item(int i)'''
        return QTextBlock()
    def __len__(self):
        ''' QTextList.__len__()'''
        return ()
    def count(self):
        '''int QTextList.count()'''
        return int()


class QTextFrame(QTextObject):
    """"""
    def __init__(self, doc):
        '''void QTextFrame.__init__(QTextDocument doc)'''
    def setFrameFormat(self, aformat):
        '''void QTextFrame.setFrameFormat(QTextFrameFormat aformat)'''
    def end(self):
        '''QTextFrame.iterator QTextFrame.end()'''
        return QTextFrame.iterator()
    def begin(self):
        '''QTextFrame.iterator QTextFrame.begin()'''
        return QTextFrame.iterator()
    def parentFrame(self):
        '''QTextFrame QTextFrame.parentFrame()'''
        return QTextFrame()
    def childFrames(self):
        '''list-of-QTextFrame QTextFrame.childFrames()'''
        return [QTextFrame()]
    def lastPosition(self):
        '''int QTextFrame.lastPosition()'''
        return int()
    def firstPosition(self):
        '''int QTextFrame.firstPosition()'''
        return int()
    def lastCursorPosition(self):
        '''QTextCursor QTextFrame.lastCursorPosition()'''
        return QTextCursor()
    def firstCursorPosition(self):
        '''QTextCursor QTextFrame.firstCursorPosition()'''
        return QTextCursor()
    def frameFormat(self):
        '''QTextFrameFormat QTextFrame.frameFormat()'''
        return QTextFrameFormat()
    class iterator():
        """"""
        def __init__(self):
            '''void QTextFrame.iterator.__init__()'''
        def __init__(self, o):
            '''void QTextFrame.iterator.__init__(QTextFrame.iterator o)'''
        def __isub__(self):
            '''int QTextFrame.iterator.__isub__()'''
            return int()
        def __iadd__(self):
            '''int QTextFrame.iterator.__iadd__()'''
            return int()
        def __ne__(self, o):
            '''bool QTextFrame.iterator.__ne__(QTextFrame.iterator o)'''
            return bool()
        def __eq__(self, o):
            '''bool QTextFrame.iterator.__eq__(QTextFrame.iterator o)'''
            return bool()
        def atEnd(self):
            '''bool QTextFrame.iterator.atEnd()'''
            return bool()
        def currentBlock(self):
            '''QTextBlock QTextFrame.iterator.currentBlock()'''
            return QTextBlock()
        def currentFrame(self):
            '''QTextFrame QTextFrame.iterator.currentFrame()'''
            return QTextFrame()
        def parentFrame(self):
            '''QTextFrame QTextFrame.iterator.parentFrame()'''
            return QTextFrame()


class QTextBlock():
    """"""
    def __init__(self):
        '''void QTextBlock.__init__()'''
    def __init__(self, o):
        '''void QTextBlock.__init__(QTextBlock o)'''
    def __ge__(self, o):
        '''bool QTextBlock.__ge__(QTextBlock o)'''
        return bool()
    def textFormats(self):
        '''list-of-QTextLayout.FormatRange QTextBlock.textFormats()'''
        return [QTextLayout.FormatRange()]
    def textDirection(self):
        '''Qt.LayoutDirection QTextBlock.textDirection()'''
        return Qt.LayoutDirection()
    def lineCount(self):
        '''int QTextBlock.lineCount()'''
        return int()
    def setLineCount(self, count):
        '''void QTextBlock.setLineCount(int count)'''
    def firstLineNumber(self):
        '''int QTextBlock.firstLineNumber()'''
        return int()
    def blockNumber(self):
        '''int QTextBlock.blockNumber()'''
        return int()
    def setVisible(self, visible):
        '''void QTextBlock.setVisible(bool visible)'''
    def isVisible(self):
        '''bool QTextBlock.isVisible()'''
        return bool()
    def setRevision(self, rev):
        '''void QTextBlock.setRevision(int rev)'''
    def revision(self):
        '''int QTextBlock.revision()'''
        return int()
    def clearLayout(self):
        '''void QTextBlock.clearLayout()'''
    def setUserState(self, state):
        '''void QTextBlock.setUserState(int state)'''
    def userState(self):
        '''int QTextBlock.userState()'''
        return int()
    def setUserData(self, data):
        '''void QTextBlock.setUserData(QTextBlockUserData data)'''
    def userData(self):
        '''QTextBlockUserData QTextBlock.userData()'''
        return QTextBlockUserData()
    def previous(self):
        '''QTextBlock QTextBlock.previous()'''
        return QTextBlock()
    def next(self):
        '''QTextBlock QTextBlock.next()'''
        return QTextBlock()
    def end(self):
        '''QTextBlock.iterator QTextBlock.end()'''
        return QTextBlock.iterator()
    def begin(self):
        '''QTextBlock.iterator QTextBlock.begin()'''
        return QTextBlock.iterator()
    def textList(self):
        '''QTextList QTextBlock.textList()'''
        return QTextList()
    def document(self):
        '''QTextDocument QTextBlock.document()'''
        return QTextDocument()
    def text(self):
        '''str QTextBlock.text()'''
        return str()
    def charFormatIndex(self):
        '''int QTextBlock.charFormatIndex()'''
        return int()
    def charFormat(self):
        '''QTextCharFormat QTextBlock.charFormat()'''
        return QTextCharFormat()
    def blockFormatIndex(self):
        '''int QTextBlock.blockFormatIndex()'''
        return int()
    def blockFormat(self):
        '''QTextBlockFormat QTextBlock.blockFormat()'''
        return QTextBlockFormat()
    def layout(self):
        '''QTextLayout QTextBlock.layout()'''
        return QTextLayout()
    def contains(self, position):
        '''bool QTextBlock.contains(int position)'''
        return bool()
    def length(self):
        '''int QTextBlock.length()'''
        return int()
    def position(self):
        '''int QTextBlock.position()'''
        return int()
    def __lt__(self, o):
        '''bool QTextBlock.__lt__(QTextBlock o)'''
        return bool()
    def __ne__(self, o):
        '''bool QTextBlock.__ne__(QTextBlock o)'''
        return bool()
    def __eq__(self, o):
        '''bool QTextBlock.__eq__(QTextBlock o)'''
        return bool()
    def isValid(self):
        '''bool QTextBlock.isValid()'''
        return bool()
    class iterator():
        """"""
        def __init__(self):
            '''void QTextBlock.iterator.__init__()'''
        def __init__(self, o):
            '''void QTextBlock.iterator.__init__(QTextBlock.iterator o)'''
        def __isub__(self):
            '''int QTextBlock.iterator.__isub__()'''
            return int()
        def __iadd__(self):
            '''int QTextBlock.iterator.__iadd__()'''
            return int()
        def __ne__(self, o):
            '''bool QTextBlock.iterator.__ne__(QTextBlock.iterator o)'''
            return bool()
        def __eq__(self, o):
            '''bool QTextBlock.iterator.__eq__(QTextBlock.iterator o)'''
            return bool()
        def atEnd(self):
            '''bool QTextBlock.iterator.atEnd()'''
            return bool()
        def fragment(self):
            '''QTextFragment QTextBlock.iterator.fragment()'''
            return QTextFragment()


class QTextFragment():
    """"""
    def __init__(self):
        '''void QTextFragment.__init__()'''
    def __init__(self, o):
        '''void QTextFragment.__init__(QTextFragment o)'''
    def __ge__(self, o):
        '''bool QTextFragment.__ge__(QTextFragment o)'''
        return bool()
    def glyphRuns(self, from_ = None, length = None):
        '''list-of-QGlyphRun QTextFragment.glyphRuns(int from = -1, int length = -1)'''
        return [QGlyphRun()]
    def text(self):
        '''str QTextFragment.text()'''
        return str()
    def charFormatIndex(self):
        '''int QTextFragment.charFormatIndex()'''
        return int()
    def charFormat(self):
        '''QTextCharFormat QTextFragment.charFormat()'''
        return QTextCharFormat()
    def contains(self, position):
        '''bool QTextFragment.contains(int position)'''
        return bool()
    def length(self):
        '''int QTextFragment.length()'''
        return int()
    def position(self):
        '''int QTextFragment.position()'''
        return int()
    def __lt__(self, o):
        '''bool QTextFragment.__lt__(QTextFragment o)'''
        return bool()
    def __ne__(self, o):
        '''bool QTextFragment.__ne__(QTextFragment o)'''
        return bool()
    def __eq__(self, o):
        '''bool QTextFragment.__eq__(QTextFragment o)'''
        return bool()
    def isValid(self):
        '''bool QTextFragment.isValid()'''
        return bool()


class QTextBlockUserData():
    """"""
    def __init__(self):
        '''void QTextBlockUserData.__init__()'''
    def __init__(self):
        '''QTextBlockUserData QTextBlockUserData.__init__()'''
        return QTextBlockUserData()


class QTextOption():
    """"""
    # Enum QTextOption.TabType
    LeftTab = 0
    RightTab = 0
    CenterTab = 0
    DelimiterTab = 0

    # Enum QTextOption.Flag
    IncludeTrailingSpaces = 0
    ShowTabsAndSpaces = 0
    ShowLineAndParagraphSeparators = 0
    AddSpaceForLineAndParagraphSeparators = 0
    SuppressColors = 0

    # Enum QTextOption.WrapMode
    NoWrap = 0
    WordWrap = 0
    ManualWrap = 0
    WrapAnywhere = 0
    WrapAtWordBoundaryOrAnywhere = 0

    def __init__(self):
        '''void QTextOption.__init__()'''
    def __init__(self, alignment):
        '''void QTextOption.__init__(Qt.Alignment alignment)'''
    def __init__(self, o):
        '''void QTextOption.__init__(QTextOption o)'''
    def tabs(self):
        '''list-of-QTextOption.Tab QTextOption.tabs()'''
        return [QTextOption.Tab()]
    def setTabs(self, tabStops):
        '''void QTextOption.setTabs(list-of-QTextOption.Tab tabStops)'''
    def setTabStop(self, atabStop):
        '''void QTextOption.setTabStop(float atabStop)'''
    def setFlags(self, aflags):
        '''void QTextOption.setFlags(QTextOption.Flags aflags)'''
    def setAlignment(self, aalignment):
        '''void QTextOption.setAlignment(Qt.Alignment aalignment)'''
    def useDesignMetrics(self):
        '''bool QTextOption.useDesignMetrics()'''
        return bool()
    def setUseDesignMetrics(self, b):
        '''void QTextOption.setUseDesignMetrics(bool b)'''
    def tabArray(self):
        '''list-of-float QTextOption.tabArray()'''
        return [float()]
    def setTabArray(self, tabStops):
        '''void QTextOption.setTabArray(list-of-float tabStops)'''
    def tabStop(self):
        '''float QTextOption.tabStop()'''
        return float()
    def flags(self):
        '''QTextOption.Flags QTextOption.flags()'''
        return QTextOption.Flags()
    def wrapMode(self):
        '''QTextOption.WrapMode QTextOption.wrapMode()'''
        return QTextOption.WrapMode()
    def setWrapMode(self, wrap):
        '''void QTextOption.setWrapMode(QTextOption.WrapMode wrap)'''
    def textDirection(self):
        '''Qt.LayoutDirection QTextOption.textDirection()'''
        return Qt.LayoutDirection()
    def setTextDirection(self, aDirection):
        '''void QTextOption.setTextDirection(Qt.LayoutDirection aDirection)'''
    def alignment(self):
        '''Qt.Alignment QTextOption.alignment()'''
        return Qt.Alignment()
    class Tab():
        """"""
        delimiter = None # str - member
        position = None # float - member
        type = None # QTextOption.TabType - member
        def __init__(self):
            '''void QTextOption.Tab.__init__()'''
        def __init__(self, pos, tabType, delim = bytes()):
            '''void QTextOption.Tab.__init__(float pos, QTextOption.TabType tabType, str delim = bytes())'''
        def __init__(self):
            '''QTextOption.Tab QTextOption.Tab.__init__()'''
            return QTextOption.Tab()
        def __ne__(self, other):
            '''bool QTextOption.Tab.__ne__(QTextOption.Tab other)'''
            return bool()
        def __eq__(self, other):
            '''bool QTextOption.Tab.__eq__(QTextOption.Tab other)'''
            return bool()
    class Flags():
        """"""
        def __init__(self):
            '''QTextOption.Flags QTextOption.Flags.__init__()'''
            return QTextOption.Flags()
        def __init__(self):
            '''int QTextOption.Flags.__init__()'''
            return int()
        def __init__(self):
            '''void QTextOption.Flags.__init__()'''
        def __bool__(self):
            '''int QTextOption.Flags.__bool__()'''
            return int()
        def __ne__(self, f):
            '''bool QTextOption.Flags.__ne__(QTextOption.Flags f)'''
            return bool()
        def __eq__(self, f):
            '''bool QTextOption.Flags.__eq__(QTextOption.Flags f)'''
            return bool()
        def __invert__(self):
            '''QTextOption.Flags QTextOption.Flags.__invert__()'''
            return QTextOption.Flags()
        def __and__(self, mask):
            '''QTextOption.Flags QTextOption.Flags.__and__(int mask)'''
            return QTextOption.Flags()
        def __xor__(self, f):
            '''QTextOption.Flags QTextOption.Flags.__xor__(QTextOption.Flags f)'''
            return QTextOption.Flags()
        def __xor__(self, f):
            '''QTextOption.Flags QTextOption.Flags.__xor__(int f)'''
            return QTextOption.Flags()
        def __or__(self, f):
            '''QTextOption.Flags QTextOption.Flags.__or__(QTextOption.Flags f)'''
            return QTextOption.Flags()
        def __or__(self, f):
            '''QTextOption.Flags QTextOption.Flags.__or__(int f)'''
            return QTextOption.Flags()
        def __int__(self):
            '''int QTextOption.Flags.__int__()'''
            return int()
        def __ixor__(self, f):
            '''QTextOption.Flags QTextOption.Flags.__ixor__(QTextOption.Flags f)'''
            return QTextOption.Flags()
        def __ior__(self, f):
            '''QTextOption.Flags QTextOption.Flags.__ior__(QTextOption.Flags f)'''
            return QTextOption.Flags()
        def __iand__(self, mask):
            '''QTextOption.Flags QTextOption.Flags.__iand__(int mask)'''
            return QTextOption.Flags()


class QTextTableCell():
    """"""
    def __init__(self):
        '''void QTextTableCell.__init__()'''
    def __init__(self, o):
        '''void QTextTableCell.__init__(QTextTableCell o)'''
    def __ne__(self, other):
        '''bool QTextTableCell.__ne__(QTextTableCell other)'''
        return bool()
    def __eq__(self, other):
        '''bool QTextTableCell.__eq__(QTextTableCell other)'''
        return bool()
    def tableCellFormatIndex(self):
        '''int QTextTableCell.tableCellFormatIndex()'''
        return int()
    def lastCursorPosition(self):
        '''QTextCursor QTextTableCell.lastCursorPosition()'''
        return QTextCursor()
    def firstCursorPosition(self):
        '''QTextCursor QTextTableCell.firstCursorPosition()'''
        return QTextCursor()
    def isValid(self):
        '''bool QTextTableCell.isValid()'''
        return bool()
    def columnSpan(self):
        '''int QTextTableCell.columnSpan()'''
        return int()
    def rowSpan(self):
        '''int QTextTableCell.rowSpan()'''
        return int()
    def column(self):
        '''int QTextTableCell.column()'''
        return int()
    def row(self):
        '''int QTextTableCell.row()'''
        return int()
    def setFormat(self, format):
        '''void QTextTableCell.setFormat(QTextCharFormat format)'''
    def format(self):
        '''QTextCharFormat QTextTableCell.format()'''
        return QTextCharFormat()


class QTextTable(QTextFrame):
    """"""
    def __init__(self, doc):
        '''void QTextTable.__init__(QTextDocument doc)'''
    def appendColumns(self, count):
        '''void QTextTable.appendColumns(int count)'''
    def appendRows(self, count):
        '''void QTextTable.appendRows(int count)'''
    def setFormat(self, aformat):
        '''void QTextTable.setFormat(QTextTableFormat aformat)'''
    def format(self):
        '''QTextTableFormat QTextTable.format()'''
        return QTextTableFormat()
    def rowEnd(self, c):
        '''QTextCursor QTextTable.rowEnd(QTextCursor c)'''
        return QTextCursor()
    def rowStart(self, c):
        '''QTextCursor QTextTable.rowStart(QTextCursor c)'''
        return QTextCursor()
    def cellAt(self, row, col):
        '''QTextTableCell QTextTable.cellAt(int row, int col)'''
        return QTextTableCell()
    def cellAt(self, position):
        '''QTextTableCell QTextTable.cellAt(int position)'''
        return QTextTableCell()
    def cellAt(self, c):
        '''QTextTableCell QTextTable.cellAt(QTextCursor c)'''
        return QTextTableCell()
    def columns(self):
        '''int QTextTable.columns()'''
        return int()
    def rows(self):
        '''int QTextTable.rows()'''
        return int()
    def splitCell(self, row, col, numRows, numCols):
        '''void QTextTable.splitCell(int row, int col, int numRows, int numCols)'''
    def mergeCells(self, row, col, numRows, numCols):
        '''void QTextTable.mergeCells(int row, int col, int numRows, int numCols)'''
    def mergeCells(self, cursor):
        '''void QTextTable.mergeCells(QTextCursor cursor)'''
    def removeColumns(self, pos, num):
        '''void QTextTable.removeColumns(int pos, int num)'''
    def removeRows(self, pos, num):
        '''void QTextTable.removeRows(int pos, int num)'''
    def insertColumns(self, pos, num):
        '''void QTextTable.insertColumns(int pos, int num)'''
    def insertRows(self, pos, num):
        '''void QTextTable.insertRows(int pos, int num)'''
    def resize(self, rows, cols):
        '''void QTextTable.resize(int rows, int cols)'''


class QTouchDevice():
    """"""
    # Enum QTouchDevice.CapabilityFlag
    Position = 0
    Area = 0
    Pressure = 0
    Velocity = 0
    RawPositions = 0
    NormalizedPosition = 0
    MouseEmulation = 0

    # Enum QTouchDevice.DeviceType
    TouchScreen = 0
    TouchPad = 0

    def __init__(self):
        '''void QTouchDevice.__init__()'''
    def __init__(self):
        '''QTouchDevice QTouchDevice.__init__()'''
        return QTouchDevice()
    def setMaximumTouchPoints(self, max):
        '''void QTouchDevice.setMaximumTouchPoints(int max)'''
    def maximumTouchPoints(self):
        '''int QTouchDevice.maximumTouchPoints()'''
        return int()
    def setCapabilities(self, caps):
        '''void QTouchDevice.setCapabilities(QTouchDevice.Capabilities caps)'''
    def setType(self, devType):
        '''void QTouchDevice.setType(QTouchDevice.DeviceType devType)'''
    def setName(self, name):
        '''void QTouchDevice.setName(str name)'''
    def capabilities(self):
        '''QTouchDevice.Capabilities QTouchDevice.capabilities()'''
        return QTouchDevice.Capabilities()
    def type(self):
        '''QTouchDevice.DeviceType QTouchDevice.type()'''
        return QTouchDevice.DeviceType()
    def name(self):
        '''str QTouchDevice.name()'''
        return str()
    def devices(self):
        '''static list-of-const QTouchDevice QTouchDevice.devices()'''
        return [ QTouchDevice()]
    class Capabilities():
        """"""
        def __init__(self):
            '''QTouchDevice.Capabilities QTouchDevice.Capabilities.__init__()'''
            return QTouchDevice.Capabilities()
        def __init__(self):
            '''int QTouchDevice.Capabilities.__init__()'''
            return int()
        def __init__(self):
            '''void QTouchDevice.Capabilities.__init__()'''
        def __bool__(self):
            '''int QTouchDevice.Capabilities.__bool__()'''
            return int()
        def __ne__(self, f):
            '''bool QTouchDevice.Capabilities.__ne__(QTouchDevice.Capabilities f)'''
            return bool()
        def __eq__(self, f):
            '''bool QTouchDevice.Capabilities.__eq__(QTouchDevice.Capabilities f)'''
            return bool()
        def __invert__(self):
            '''QTouchDevice.Capabilities QTouchDevice.Capabilities.__invert__()'''
            return QTouchDevice.Capabilities()
        def __and__(self, mask):
            '''QTouchDevice.Capabilities QTouchDevice.Capabilities.__and__(int mask)'''
            return QTouchDevice.Capabilities()
        def __xor__(self, f):
            '''QTouchDevice.Capabilities QTouchDevice.Capabilities.__xor__(QTouchDevice.Capabilities f)'''
            return QTouchDevice.Capabilities()
        def __xor__(self, f):
            '''QTouchDevice.Capabilities QTouchDevice.Capabilities.__xor__(int f)'''
            return QTouchDevice.Capabilities()
        def __or__(self, f):
            '''QTouchDevice.Capabilities QTouchDevice.Capabilities.__or__(QTouchDevice.Capabilities f)'''
            return QTouchDevice.Capabilities()
        def __or__(self, f):
            '''QTouchDevice.Capabilities QTouchDevice.Capabilities.__or__(int f)'''
            return QTouchDevice.Capabilities()
        def __int__(self):
            '''int QTouchDevice.Capabilities.__int__()'''
            return int()
        def __ixor__(self, f):
            '''QTouchDevice.Capabilities QTouchDevice.Capabilities.__ixor__(QTouchDevice.Capabilities f)'''
            return QTouchDevice.Capabilities()
        def __ior__(self, f):
            '''QTouchDevice.Capabilities QTouchDevice.Capabilities.__ior__(QTouchDevice.Capabilities f)'''
            return QTouchDevice.Capabilities()
        def __iand__(self, mask):
            '''QTouchDevice.Capabilities QTouchDevice.Capabilities.__iand__(int mask)'''
            return QTouchDevice.Capabilities()


class QTransform():
    """"""
    # Enum QTransform.TransformationType
    TxNone = 0
    TxTranslate = 0
    TxScale = 0
    TxRotate = 0
    TxShear = 0
    TxProject = 0

    def __init__(self):
        '''void QTransform.__init__()'''
    def __init__(self, m11, m12, m13, m21, m22, m23, m31, m32, m33 = 1):
        '''void QTransform.__init__(float m11, float m12, float m13, float m21, float m22, float m23, float m31, float m32, float m33 = 1)'''
    def __init__(self, h11, h12, h13, h21, h22, h23):
        '''void QTransform.__init__(float h11, float h12, float h13, float h21, float h22, float h23)'''
    def __init__(self):
        '''QTransform QTransform.__init__()'''
        return QTransform()
    def __div__(self, n):
        '''QTransform QTransform.__div__(float n)'''
        return QTransform()
    def __add__(self, n):
        '''QTransform QTransform.__add__(float n)'''
        return QTransform()
    def __sub__(self, n):
        '''QTransform QTransform.__sub__(float n)'''
        return QTransform()
    def __isub__(self, num):
        '''QTransform QTransform.__isub__(float num)'''
        return QTransform()
    def __iadd__(self, num):
        '''QTransform QTransform.__iadd__(float num)'''
        return QTransform()
    def __idiv__(self, div):
        '''QTransform QTransform.__idiv__(float div)'''
        return QTransform()
    def fromScale(self, dx, dy):
        '''static QTransform QTransform.fromScale(float dx, float dy)'''
        return QTransform()
    def fromTranslate(self, dx, dy):
        '''static QTransform QTransform.fromTranslate(float dx, float dy)'''
        return QTransform()
    def dy(self):
        '''float QTransform.dy()'''
        return float()
    def dx(self):
        '''float QTransform.dx()'''
        return float()
    def m33(self):
        '''float QTransform.m33()'''
        return float()
    def m32(self):
        '''float QTransform.m32()'''
        return float()
    def m31(self):
        '''float QTransform.m31()'''
        return float()
    def m23(self):
        '''float QTransform.m23()'''
        return float()
    def m22(self):
        '''float QTransform.m22()'''
        return float()
    def m21(self):
        '''float QTransform.m21()'''
        return float()
    def m13(self):
        '''float QTransform.m13()'''
        return float()
    def m12(self):
        '''float QTransform.m12()'''
        return float()
    def m11(self):
        '''float QTransform.m11()'''
        return float()
    def determinant(self):
        '''float QTransform.determinant()'''
        return float()
    def isTranslating(self):
        '''bool QTransform.isTranslating()'''
        return bool()
    def isRotating(self):
        '''bool QTransform.isRotating()'''
        return bool()
    def isScaling(self):
        '''bool QTransform.isScaling()'''
        return bool()
    def isInvertible(self):
        '''bool QTransform.isInvertible()'''
        return bool()
    def isIdentity(self):
        '''bool QTransform.isIdentity()'''
        return bool()
    def isAffine(self):
        '''bool QTransform.isAffine()'''
        return bool()
    def mapRect(self):
        '''QRect QTransform.mapRect()'''
        return QRect()
    def mapRect(self):
        '''QRectF QTransform.mapRect()'''
        return QRectF()
    def mapToPolygon(self, r):
        '''QPolygon QTransform.mapToPolygon(QRect r)'''
        return QPolygon()
    def map(self, x, y, tx, ty):
        '''void QTransform.map(int x, int y, int tx, int ty)'''
    def map(self, x, y, tx, ty):
        '''void QTransform.map(float x, float y, float tx, float ty)'''
    def map(self, p):
        '''QPoint QTransform.map(QPoint p)'''
        return QPoint()
    def map(self, p):
        '''QPointF QTransform.map(QPointF p)'''
        return QPointF()
    def map(self, l):
        '''QLine QTransform.map(QLine l)'''
        return QLine()
    def map(self, l):
        '''QLineF QTransform.map(QLineF l)'''
        return QLineF()
    def map(self, a):
        '''QPolygonF QTransform.map(QPolygonF a)'''
        return QPolygonF()
    def map(self, a):
        '''QPolygon QTransform.map(QPolygon a)'''
        return QPolygon()
    def map(self, r):
        '''QRegion QTransform.map(QRegion r)'''
        return QRegion()
    def map(self, p):
        '''QPainterPath QTransform.map(QPainterPath p)'''
        return QPainterPath()
    def reset(self):
        '''void QTransform.reset()'''
    def __mul__(self, o):
        '''QTransform QTransform.__mul__(QTransform o)'''
        return QTransform()
    def __mul__(self, n):
        '''QTransform QTransform.__mul__(float n)'''
        return QTransform()
    def __imul__(self):
        '''QTransform QTransform.__imul__()'''
        return QTransform()
    def __imul__(self, num):
        '''QTransform QTransform.__imul__(float num)'''
        return QTransform()
    def __ne__(self):
        '''QTransform QTransform.__ne__()'''
        return QTransform()
    def __eq__(self):
        '''QTransform QTransform.__eq__()'''
        return QTransform()
    def quadToQuad(self, one, two, result):
        '''static bool QTransform.quadToQuad(QPolygonF one, QPolygonF two, QTransform result)'''
        return bool()
    def quadToSquare(self, quad, result):
        '''static bool QTransform.quadToSquare(QPolygonF quad, QTransform result)'''
        return bool()
    def squareToQuad(self, square, result):
        '''static bool QTransform.squareToQuad(QPolygonF square, QTransform result)'''
        return bool()
    def rotateRadians(self, angle, axis = None):
        '''QTransform QTransform.rotateRadians(float angle, Qt.Axis axis = Qt.ZAxis)'''
        return QTransform()
    def rotate(self, angle, axis = None):
        '''QTransform QTransform.rotate(float angle, Qt.Axis axis = Qt.ZAxis)'''
        return QTransform()
    def shear(self, sh, sv):
        '''QTransform QTransform.shear(float sh, float sv)'''
        return QTransform()
    def scale(self, sx, sy):
        '''QTransform QTransform.scale(float sx, float sy)'''
        return QTransform()
    def translate(self, dx, dy):
        '''QTransform QTransform.translate(float dx, float dy)'''
        return QTransform()
    def transposed(self):
        '''QTransform QTransform.transposed()'''
        return QTransform()
    def adjoint(self):
        '''QTransform QTransform.adjoint()'''
        return QTransform()
    def inverted(self, invertible):
        '''QTransform QTransform.inverted(bool invertible)'''
        return QTransform()
    def setMatrix(self, m11, m12, m13, m21, m22, m23, m31, m32, m33):
        '''void QTransform.setMatrix(float m11, float m12, float m13, float m21, float m22, float m23, float m31, float m32, float m33)'''
    def type(self):
        '''QTransform.TransformationType QTransform.type()'''
        return QTransform.TransformationType()


class QValidator(QObject):
    """"""
    # Enum QValidator.State
    Invalid = 0
    Intermediate = 0
    Acceptable = 0

    def __init__(self, parent = None):
        '''void QValidator.__init__(QObject parent = None)'''
    changed = pyqtSignal() # void changed() - signal
    def locale(self):
        '''QLocale QValidator.locale()'''
        return QLocale()
    def setLocale(self, locale):
        '''void QValidator.setLocale(QLocale locale)'''
    def fixup(self):
        '''str QValidator.fixup()'''
        return str()
    def validate(self):
        '''abstract int QValidator.validate()'''
        return int()


class QIntValidator(QValidator):
    """"""
    def __init__(self, parent = None):
        '''void QIntValidator.__init__(QObject parent = None)'''
    def __init__(self, bottom, top, parent = None):
        '''void QIntValidator.__init__(int bottom, int top, QObject parent = None)'''
    def top(self):
        '''int QIntValidator.top()'''
        return int()
    def bottom(self):
        '''int QIntValidator.bottom()'''
        return int()
    def setRange(self, bottom, top):
        '''void QIntValidator.setRange(int bottom, int top)'''
    def setTop(self):
        '''int QIntValidator.setTop()'''
        return int()
    def setBottom(self):
        '''int QIntValidator.setBottom()'''
        return int()
    def fixup(self, input):
        '''void QIntValidator.fixup(str input)'''
    def validate(self):
        '''int QIntValidator.validate()'''
        return int()


class QDoubleValidator(QValidator):
    """"""
    # Enum QDoubleValidator.Notation
    StandardNotation = 0
    ScientificNotation = 0

    def __init__(self, parent = None):
        '''void QDoubleValidator.__init__(QObject parent = None)'''
    def __init__(self, bottom, top, decimals, parent = None):
        '''void QDoubleValidator.__init__(float bottom, float top, int decimals, QObject parent = None)'''
    def notation(self):
        '''QDoubleValidator.Notation QDoubleValidator.notation()'''
        return QDoubleValidator.Notation()
    def setNotation(self):
        '''QDoubleValidator.Notation QDoubleValidator.setNotation()'''
        return QDoubleValidator.Notation()
    def decimals(self):
        '''int QDoubleValidator.decimals()'''
        return int()
    def top(self):
        '''float QDoubleValidator.top()'''
        return float()
    def bottom(self):
        '''float QDoubleValidator.bottom()'''
        return float()
    def setDecimals(self):
        '''int QDoubleValidator.setDecimals()'''
        return int()
    def setTop(self):
        '''float QDoubleValidator.setTop()'''
        return float()
    def setBottom(self):
        '''float QDoubleValidator.setBottom()'''
        return float()
    def setRange(self, minimum, maximum, decimals = 0):
        '''void QDoubleValidator.setRange(float minimum, float maximum, int decimals = 0)'''
    def validate(self):
        '''int QDoubleValidator.validate()'''
        return int()


class QRegExpValidator(QValidator):
    """"""
    def __init__(self, parent = None):
        '''void QRegExpValidator.__init__(QObject parent = None)'''
    def __init__(self, rx, parent = None):
        '''void QRegExpValidator.__init__(QRegExp rx, QObject parent = None)'''
    def regExp(self):
        '''QRegExp QRegExpValidator.regExp()'''
        return QRegExp()
    def setRegExp(self, rx):
        '''void QRegExpValidator.setRegExp(QRegExp rx)'''
    def validate(self, input, pos):
        '''QValidator.State QRegExpValidator.validate(str input, int pos)'''
        return QValidator.State()


class QRegularExpressionValidator(QValidator):
    """"""
    def __init__(self, parent = None):
        '''void QRegularExpressionValidator.__init__(QObject parent = None)'''
    def __init__(self, re, parent = None):
        '''void QRegularExpressionValidator.__init__(QRegularExpression re, QObject parent = None)'''
    def setRegularExpression(self, re):
        '''void QRegularExpressionValidator.setRegularExpression(QRegularExpression re)'''
    def regularExpression(self):
        '''QRegularExpression QRegularExpressionValidator.regularExpression()'''
        return QRegularExpression()
    def validate(self, input, pos):
        '''QValidator.State QRegularExpressionValidator.validate(str input, int pos)'''
        return QValidator.State()


class QVector2D():
    """"""
    def __init__(self):
        '''void QVector2D.__init__()'''
    def __init__(self, xpos, ypos):
        '''void QVector2D.__init__(float xpos, float ypos)'''
    def __init__(self, point):
        '''void QVector2D.__init__(QPoint point)'''
    def __init__(self, point):
        '''void QVector2D.__init__(QPointF point)'''
    def __init__(self, vector):
        '''void QVector2D.__init__(QVector3D vector)'''
    def __init__(self, vector):
        '''void QVector2D.__init__(QVector4D vector)'''
    def __init__(self):
        '''QVector2D QVector2D.__init__()'''
        return QVector2D()
    def __eq__(self, v2):
        '''bool QVector2D.__eq__(QVector2D v2)'''
        return bool()
    def __div__(self, divisor):
        '''QVector2D QVector2D.__div__(float divisor)'''
        return QVector2D()
    def __div__(self, divisor):
        '''QVector2D QVector2D.__div__(QVector2D divisor)'''
        return QVector2D()
    def __add__(self, v2):
        '''QVector2D QVector2D.__add__(QVector2D v2)'''
        return QVector2D()
    def __sub__(self, v2):
        '''QVector2D QVector2D.__sub__(QVector2D v2)'''
        return QVector2D()
    def __mul__(self, vector):
        '''QVector2D QVector2D.__mul__(QVector2D vector)'''
        return QVector2D()
    def __mul__(self, factor):
        '''QVector2D QVector2D.__mul__(float factor)'''
        return QVector2D()
    def __mul__(self, v2):
        '''QVector2D QVector2D.__mul__(QVector2D v2)'''
        return QVector2D()
    def __neg__(self):
        '''QVector2D QVector2D.__neg__()'''
        return QVector2D()
    def __ne__(self, v2):
        '''bool QVector2D.__ne__(QVector2D v2)'''
        return bool()
    def __getitem__(self, i):
        '''float QVector2D.__getitem__(int i)'''
        return float()
    def distanceToLine(self, point, direction):
        '''float QVector2D.distanceToLine(QVector2D point, QVector2D direction)'''
        return float()
    def distanceToPoint(self, point):
        '''float QVector2D.distanceToPoint(QVector2D point)'''
        return float()
    def toPointF(self):
        '''QPointF QVector2D.toPointF()'''
        return QPointF()
    def toPoint(self):
        '''QPoint QVector2D.toPoint()'''
        return QPoint()
    def __idiv__(self, divisor):
        '''QVector2D QVector2D.__idiv__(float divisor)'''
        return QVector2D()
    def __idiv__(self, vector):
        '''QVector2D QVector2D.__idiv__(QVector2D vector)'''
        return QVector2D()
    def __imul__(self, factor):
        '''QVector2D QVector2D.__imul__(float factor)'''
        return QVector2D()
    def __imul__(self, vector):
        '''QVector2D QVector2D.__imul__(QVector2D vector)'''
        return QVector2D()
    def __isub__(self, vector):
        '''QVector2D QVector2D.__isub__(QVector2D vector)'''
        return QVector2D()
    def __iadd__(self, vector):
        '''QVector2D QVector2D.__iadd__(QVector2D vector)'''
        return QVector2D()
    def setY(self, aY):
        '''void QVector2D.setY(float aY)'''
    def setX(self, aX):
        '''void QVector2D.setX(float aX)'''
    def y(self):
        '''float QVector2D.y()'''
        return float()
    def x(self):
        '''float QVector2D.x()'''
        return float()
    def isNull(self):
        '''bool QVector2D.isNull()'''
        return bool()
    def toVector4D(self):
        '''QVector4D QVector2D.toVector4D()'''
        return QVector4D()
    def toVector3D(self):
        '''QVector3D QVector2D.toVector3D()'''
        return QVector3D()
    def dotProduct(self, v1, v2):
        '''static float QVector2D.dotProduct(QVector2D v1, QVector2D v2)'''
        return float()
    def normalize(self):
        '''void QVector2D.normalize()'''
    def normalized(self):
        '''QVector2D QVector2D.normalized()'''
        return QVector2D()
    def lengthSquared(self):
        '''float QVector2D.lengthSquared()'''
        return float()
    def length(self):
        '''float QVector2D.length()'''
        return float()
    def __repr__(self):
        '''str QVector2D.__repr__()'''
        return str()


class QVector3D():
    """"""
    def __init__(self):
        '''void QVector3D.__init__()'''
    def __init__(self, xpos, ypos, zpos):
        '''void QVector3D.__init__(float xpos, float ypos, float zpos)'''
    def __init__(self, point):
        '''void QVector3D.__init__(QPoint point)'''
    def __init__(self, point):
        '''void QVector3D.__init__(QPointF point)'''
    def __init__(self, vector):
        '''void QVector3D.__init__(QVector2D vector)'''
    def __init__(self, vector, zpos):
        '''void QVector3D.__init__(QVector2D vector, float zpos)'''
    def __init__(self, vector):
        '''void QVector3D.__init__(QVector4D vector)'''
    def __init__(self):
        '''QVector3D QVector3D.__init__()'''
        return QVector3D()
    def __eq__(self, v2):
        '''bool QVector3D.__eq__(QVector3D v2)'''
        return bool()
    def __div__(self, divisor):
        '''QVector3D QVector3D.__div__(float divisor)'''
        return QVector3D()
    def __div__(self, divisor):
        '''QVector3D QVector3D.__div__(QVector3D divisor)'''
        return QVector3D()
    def __add__(self, v2):
        '''QVector3D QVector3D.__add__(QVector3D v2)'''
        return QVector3D()
    def __sub__(self, v2):
        '''QVector3D QVector3D.__sub__(QVector3D v2)'''
        return QVector3D()
    def __mul__(self, matrix):
        '''QVector3D QVector3D.__mul__(QMatrix4x4 matrix)'''
        return QVector3D()
    def __mul__(self, vector):
        '''QVector3D QVector3D.__mul__(QVector3D vector)'''
        return QVector3D()
    def __mul__(self, factor):
        '''QVector3D QVector3D.__mul__(float factor)'''
        return QVector3D()
    def __mul__(self, v2):
        '''QVector3D QVector3D.__mul__(QVector3D v2)'''
        return QVector3D()
    def __neg__(self):
        '''QVector3D QVector3D.__neg__()'''
        return QVector3D()
    def __ne__(self, v2):
        '''bool QVector3D.__ne__(QVector3D v2)'''
        return bool()
    def unproject(self, modelView, projection, viewport):
        '''QVector3D QVector3D.unproject(QMatrix4x4 modelView, QMatrix4x4 projection, QRect viewport)'''
        return QVector3D()
    def project(self, modelView, projection, viewport):
        '''QVector3D QVector3D.project(QMatrix4x4 modelView, QMatrix4x4 projection, QRect viewport)'''
        return QVector3D()
    def __getitem__(self, i):
        '''float QVector3D.__getitem__(int i)'''
        return float()
    def distanceToPoint(self, point):
        '''float QVector3D.distanceToPoint(QVector3D point)'''
        return float()
    def toPointF(self):
        '''QPointF QVector3D.toPointF()'''
        return QPointF()
    def toPoint(self):
        '''QPoint QVector3D.toPoint()'''
        return QPoint()
    def __idiv__(self, divisor):
        '''QVector3D QVector3D.__idiv__(float divisor)'''
        return QVector3D()
    def __idiv__(self, vector):
        '''QVector3D QVector3D.__idiv__(QVector3D vector)'''
        return QVector3D()
    def __imul__(self, factor):
        '''QVector3D QVector3D.__imul__(float factor)'''
        return QVector3D()
    def __imul__(self, vector):
        '''QVector3D QVector3D.__imul__(QVector3D vector)'''
        return QVector3D()
    def __isub__(self, vector):
        '''QVector3D QVector3D.__isub__(QVector3D vector)'''
        return QVector3D()
    def __iadd__(self, vector):
        '''QVector3D QVector3D.__iadd__(QVector3D vector)'''
        return QVector3D()
    def setZ(self, aZ):
        '''void QVector3D.setZ(float aZ)'''
    def setY(self, aY):
        '''void QVector3D.setY(float aY)'''
    def setX(self, aX):
        '''void QVector3D.setX(float aX)'''
    def z(self):
        '''float QVector3D.z()'''
        return float()
    def y(self):
        '''float QVector3D.y()'''
        return float()
    def x(self):
        '''float QVector3D.x()'''
        return float()
    def isNull(self):
        '''bool QVector3D.isNull()'''
        return bool()
    def toVector4D(self):
        '''QVector4D QVector3D.toVector4D()'''
        return QVector4D()
    def toVector2D(self):
        '''QVector2D QVector3D.toVector2D()'''
        return QVector2D()
    def distanceToLine(self, point, direction):
        '''float QVector3D.distanceToLine(QVector3D point, QVector3D direction)'''
        return float()
    def distanceToPlane(self, plane, normal):
        '''float QVector3D.distanceToPlane(QVector3D plane, QVector3D normal)'''
        return float()
    def distanceToPlane(self, plane1, plane2, plane3):
        '''float QVector3D.distanceToPlane(QVector3D plane1, QVector3D plane2, QVector3D plane3)'''
        return float()
    def normal(self, v1, v2):
        '''static QVector3D QVector3D.normal(QVector3D v1, QVector3D v2)'''
        return QVector3D()
    def normal(self, v1, v2, v3):
        '''static QVector3D QVector3D.normal(QVector3D v1, QVector3D v2, QVector3D v3)'''
        return QVector3D()
    def crossProduct(self, v1, v2):
        '''static QVector3D QVector3D.crossProduct(QVector3D v1, QVector3D v2)'''
        return QVector3D()
    def dotProduct(self, v1, v2):
        '''static float QVector3D.dotProduct(QVector3D v1, QVector3D v2)'''
        return float()
    def normalize(self):
        '''void QVector3D.normalize()'''
    def normalized(self):
        '''QVector3D QVector3D.normalized()'''
        return QVector3D()
    def lengthSquared(self):
        '''float QVector3D.lengthSquared()'''
        return float()
    def length(self):
        '''float QVector3D.length()'''
        return float()
    def __repr__(self):
        '''str QVector3D.__repr__()'''
        return str()


class QVector4D():
    """"""
    def __init__(self):
        '''void QVector4D.__init__()'''
    def __init__(self, xpos, ypos, zpos, wpos):
        '''void QVector4D.__init__(float xpos, float ypos, float zpos, float wpos)'''
    def __init__(self, point):
        '''void QVector4D.__init__(QPoint point)'''
    def __init__(self, point):
        '''void QVector4D.__init__(QPointF point)'''
    def __init__(self, vector):
        '''void QVector4D.__init__(QVector2D vector)'''
    def __init__(self, vector, zpos, wpos):
        '''void QVector4D.__init__(QVector2D vector, float zpos, float wpos)'''
    def __init__(self, vector):
        '''void QVector4D.__init__(QVector3D vector)'''
    def __init__(self, vector, wpos):
        '''void QVector4D.__init__(QVector3D vector, float wpos)'''
    def __init__(self):
        '''QVector4D QVector4D.__init__()'''
        return QVector4D()
    def __eq__(self, v2):
        '''bool QVector4D.__eq__(QVector4D v2)'''
        return bool()
    def __div__(self, divisor):
        '''QVector4D QVector4D.__div__(float divisor)'''
        return QVector4D()
    def __div__(self, divisor):
        '''QVector4D QVector4D.__div__(QVector4D divisor)'''
        return QVector4D()
    def __add__(self, v2):
        '''QVector4D QVector4D.__add__(QVector4D v2)'''
        return QVector4D()
    def __sub__(self, v2):
        '''QVector4D QVector4D.__sub__(QVector4D v2)'''
        return QVector4D()
    def __mul__(self, matrix):
        '''QVector4D QVector4D.__mul__(QMatrix4x4 matrix)'''
        return QVector4D()
    def __mul__(self, vector):
        '''QVector4D QVector4D.__mul__(QVector4D vector)'''
        return QVector4D()
    def __mul__(self, factor):
        '''QVector4D QVector4D.__mul__(float factor)'''
        return QVector4D()
    def __mul__(self, v2):
        '''QVector4D QVector4D.__mul__(QVector4D v2)'''
        return QVector4D()
    def __neg__(self):
        '''QVector4D QVector4D.__neg__()'''
        return QVector4D()
    def __ne__(self, v2):
        '''bool QVector4D.__ne__(QVector4D v2)'''
        return bool()
    def __getitem__(self, i):
        '''float QVector4D.__getitem__(int i)'''
        return float()
    def toPointF(self):
        '''QPointF QVector4D.toPointF()'''
        return QPointF()
    def toPoint(self):
        '''QPoint QVector4D.toPoint()'''
        return QPoint()
    def __idiv__(self, divisor):
        '''QVector4D QVector4D.__idiv__(float divisor)'''
        return QVector4D()
    def __idiv__(self, vector):
        '''QVector4D QVector4D.__idiv__(QVector4D vector)'''
        return QVector4D()
    def __imul__(self, factor):
        '''QVector4D QVector4D.__imul__(float factor)'''
        return QVector4D()
    def __imul__(self, vector):
        '''QVector4D QVector4D.__imul__(QVector4D vector)'''
        return QVector4D()
    def __isub__(self, vector):
        '''QVector4D QVector4D.__isub__(QVector4D vector)'''
        return QVector4D()
    def __iadd__(self, vector):
        '''QVector4D QVector4D.__iadd__(QVector4D vector)'''
        return QVector4D()
    def setW(self, aW):
        '''void QVector4D.setW(float aW)'''
    def setZ(self, aZ):
        '''void QVector4D.setZ(float aZ)'''
    def setY(self, aY):
        '''void QVector4D.setY(float aY)'''
    def setX(self, aX):
        '''void QVector4D.setX(float aX)'''
    def w(self):
        '''float QVector4D.w()'''
        return float()
    def z(self):
        '''float QVector4D.z()'''
        return float()
    def y(self):
        '''float QVector4D.y()'''
        return float()
    def x(self):
        '''float QVector4D.x()'''
        return float()
    def isNull(self):
        '''bool QVector4D.isNull()'''
        return bool()
    def toVector3DAffine(self):
        '''QVector3D QVector4D.toVector3DAffine()'''
        return QVector3D()
    def toVector3D(self):
        '''QVector3D QVector4D.toVector3D()'''
        return QVector3D()
    def toVector2DAffine(self):
        '''QVector2D QVector4D.toVector2DAffine()'''
        return QVector2D()
    def toVector2D(self):
        '''QVector2D QVector4D.toVector2D()'''
        return QVector2D()
    def dotProduct(self, v1, v2):
        '''static float QVector4D.dotProduct(QVector4D v1, QVector4D v2)'''
        return float()
    def normalize(self):
        '''void QVector4D.normalize()'''
    def normalized(self):
        '''QVector4D QVector4D.normalized()'''
        return QVector4D()
    def lengthSquared(self):
        '''float QVector4D.lengthSquared()'''
        return float()
    def length(self):
        '''float QVector4D.length()'''
        return float()
    def __repr__(self):
        '''str QVector4D.__repr__()'''
        return str()


class QPointF():
    """"""
    def __init__(self):
        '''QPainterPath.Element QPointF.__init__()'''
        return QPainterPath.Element()


def qUnpremultiply(p):
    '''static int qUnpremultiply(int p)'''
    return int()

def qPremultiply(x):
    '''static int qPremultiply(int x)'''
    return int()

def qIsGray(rgb):
    '''static bool qIsGray(int rgb)'''
    return bool()

def qGray(r, g, b):
    '''static int qGray(int r, int g, int b)'''
    return int()

def qGray(rgb):
    '''static int qGray(int rgb)'''
    return int()

def qRgba(r, g, b, a):
    '''static int qRgba(int r, int g, int b, int a)'''
    return int()

def qRgb(r, g, b):
    '''static int qRgb(int r, int g, int b)'''
    return int()

def qAlpha(rgb):
    '''static int qAlpha(int rgb)'''
    return int()

def qBlue(rgb):
    '''static int qBlue(int rgb)'''
    return int()

def qGreen(rgb):
    '''static int qGreen(int rgb)'''
    return int()

def qRed(rgb):
    '''static int qRed(int rgb)'''
    return int()

def qPixelFormatAlpha(channelSize, typeInterpretation = None):
    '''static QPixelFormat qPixelFormatAlpha(int channelSize, QPixelFormat.TypeInterpretation typeInterpretation = QPixelFormat.UnsignedInteger)'''
    return QPixelFormat()

def qPixelFormatYuv(layout, alphaSize = 0, alphaUsage = None, alphaPosition = None, premultiplied = None, typeInterpretation = None, byteOrder = None):
    '''static QPixelFormat qPixelFormatYuv(QPixelFormat.YUVLayout layout, int alphaSize = 0, QPixelFormat.AlphaUsage alphaUsage = QPixelFormat.IgnoresAlpha, QPixelFormat.AlphaPosition alphaPosition = QPixelFormat.AtBeginning, QPixelFormat.AlphaPremultiplied premultiplied = QPixelFormat.NotPremultiplied, QPixelFormat.TypeInterpretation typeInterpretation = QPixelFormat.UnsignedByte, QPixelFormat.ByteOrder byteOrder = QPixelFormat.LittleEndian)'''
    return QPixelFormat()

def qPixelFormatHsv(channelSize, alphaSize = 0, alphaUsage = None, alphaPosition = None, typeInterpretation = None):
    '''static QPixelFormat qPixelFormatHsv(int channelSize, int alphaSize = 0, QPixelFormat.AlphaUsage alphaUsage = QPixelFormat.IgnoresAlpha, QPixelFormat.AlphaPosition alphaPosition = QPixelFormat.AtBeginning, QPixelFormat.TypeInterpretation typeInterpretation = QPixelFormat.FloatingPoint)'''
    return QPixelFormat()

def qPixelFormatHsl(channelSize, alphaSize = 0, alphaUsage = None, alphaPosition = None, typeInterpretation = None):
    '''static QPixelFormat qPixelFormatHsl(int channelSize, int alphaSize = 0, QPixelFormat.AlphaUsage alphaUsage = QPixelFormat.IgnoresAlpha, QPixelFormat.AlphaPosition alphaPosition = QPixelFormat.AtBeginning, QPixelFormat.TypeInterpretation typeInterpretation = QPixelFormat.FloatingPoint)'''
    return QPixelFormat()

def qPixelFormatCmyk(channelSize, alphaSize = 0, alphaUsage = None, alphaPosition = None, typeInterpretation = None):
    '''static QPixelFormat qPixelFormatCmyk(int channelSize, int alphaSize = 0, QPixelFormat.AlphaUsage alphaUsage = QPixelFormat.IgnoresAlpha, QPixelFormat.AlphaPosition alphaPosition = QPixelFormat.AtBeginning, QPixelFormat.TypeInterpretation typeInterpretation = QPixelFormat.UnsignedInteger)'''
    return QPixelFormat()

def qPixelFormatGrayscale(channelSize, typeInterpretation = None):
    '''static QPixelFormat qPixelFormatGrayscale(int channelSize, QPixelFormat.TypeInterpretation typeInterpretation = QPixelFormat.UnsignedInteger)'''
    return QPixelFormat()

def qPixelFormatRgba(red, green, blue, alfa, usage, position, premultiplied = None, typeInterpretation = None):
    '''static QPixelFormat qPixelFormatRgba(int red, int green, int blue, int alfa, QPixelFormat.AlphaUsage usage, QPixelFormat.AlphaPosition position, QPixelFormat.AlphaPremultiplied premultiplied = QPixelFormat.NotPremultiplied, QPixelFormat.TypeInterpretation typeInterpretation = QPixelFormat.UnsignedInteger)'''
    return QPixelFormat()

def qFuzzyCompare(m1, m2):
    '''static bool qFuzzyCompare(QMatrix4x4 m1, QMatrix4x4 m2)'''
    return bool()

def qFuzzyCompare(q1, q2):
    '''static bool qFuzzyCompare(QQuaternion q1, QQuaternion q2)'''
    return bool()

def qFuzzyCompare(t1, t2):
    '''static bool qFuzzyCompare(QTransform t1, QTransform t2)'''
    return bool()

def qFuzzyCompare(v1, v2):
    '''static bool qFuzzyCompare(QVector2D v1, QVector2D v2)'''
    return bool()

def qFuzzyCompare(v1, v2):
    '''static bool qFuzzyCompare(QVector3D v1, QVector3D v2)'''
    return bool()

def qFuzzyCompare(v1, v2):
    '''static bool qFuzzyCompare(QVector4D v1, QVector4D v2)'''
    return bool()

