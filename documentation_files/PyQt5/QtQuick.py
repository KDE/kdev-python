class pyqtSignal():
 def connect(self, targetSignal): pass
 def emit(self, *args): pass
from QtCore import *

from QtWidgets import *

import datetime

class QQuickItem(QObject, QQmlParserStatus):
    """"""
    # Enum QQuickItem.TransformOrigin
    TopLeft = 0
    Top = 0
    TopRight = 0
    Left = 0
    Center = 0
    Right = 0
    BottomLeft = 0
    Bottom = 0
    BottomRight = 0

    # Enum QQuickItem.ItemChange
    ItemChildAddedChange = 0
    ItemChildRemovedChange = 0
    ItemSceneChange = 0
    ItemVisibleHasChanged = 0
    ItemParentHasChanged = 0
    ItemOpacityHasChanged = 0
    ItemActiveFocusHasChanged = 0
    ItemRotationHasChanged = 0
    ItemAntialiasingHasChanged = 0

    # Enum QQuickItem.Flag
    ItemClipsChildrenToShape = 0
    ItemAcceptsInputMethod = 0
    ItemIsFocusScope = 0
    ItemHasContents = 0
    ItemAcceptsDrops = 0

    def __init__(self, parent = None):
        '''void QQuickItem.__init__(QQuickItem parent = None)'''
    def grabToImage(self, targetSize = QSize()):
        '''QQuickItemGrabResult QQuickItem.grabToImage(QSize targetSize = QSize())'''
        return QQuickItemGrabResult()
    def resetAntialiasing(self):
        '''void QQuickItem.resetAntialiasing()'''
    windowChanged = pyqtSignal() # void windowChanged(QQuickWindow*) - signal
    def nextItemInFocusChain(self, forward = True):
        '''QQuickItem QQuickItem.nextItemInFocusChain(bool forward = True)'''
        return QQuickItem()
    def setActiveFocusOnTab(self):
        '''bool QQuickItem.setActiveFocusOnTab()'''
        return bool()
    def activeFocusOnTab(self):
        '''bool QQuickItem.activeFocusOnTab()'''
        return bool()
    def updatePolish(self):
        '''void QQuickItem.updatePolish()'''
    def releaseResources(self):
        '''void QQuickItem.releaseResources()'''
    def updatePaintNode(self):
        '''QQuickItem.UpdatePaintNodeData QQuickItem.updatePaintNode()'''
        return QQuickItem.UpdatePaintNodeData()
    def geometryChanged(self, newGeometry, oldGeometry):
        '''void QQuickItem.geometryChanged(QRectF newGeometry, QRectF oldGeometry)'''
    def childMouseEventFilter(self):
        '''QEvent QQuickItem.childMouseEventFilter()'''
        return QEvent()
    def dropEvent(self):
        '''QDropEvent QQuickItem.dropEvent()'''
        return QDropEvent()
    def dragLeaveEvent(self):
        '''QDragLeaveEvent QQuickItem.dragLeaveEvent()'''
        return QDragLeaveEvent()
    def dragMoveEvent(self):
        '''QDragMoveEvent QQuickItem.dragMoveEvent()'''
        return QDragMoveEvent()
    def dragEnterEvent(self):
        '''QDragEnterEvent QQuickItem.dragEnterEvent()'''
        return QDragEnterEvent()
    def hoverLeaveEvent(self, event):
        '''void QQuickItem.hoverLeaveEvent(QHoverEvent event)'''
    def hoverMoveEvent(self, event):
        '''void QQuickItem.hoverMoveEvent(QHoverEvent event)'''
    def hoverEnterEvent(self, event):
        '''void QQuickItem.hoverEnterEvent(QHoverEvent event)'''
    def touchEvent(self, event):
        '''void QQuickItem.touchEvent(QTouchEvent event)'''
    def wheelEvent(self, event):
        '''void QQuickItem.wheelEvent(QWheelEvent event)'''
    def touchUngrabEvent(self):
        '''void QQuickItem.touchUngrabEvent()'''
    def mouseUngrabEvent(self):
        '''void QQuickItem.mouseUngrabEvent()'''
    def mouseDoubleClickEvent(self, event):
        '''void QQuickItem.mouseDoubleClickEvent(QMouseEvent event)'''
    def mouseReleaseEvent(self, event):
        '''void QQuickItem.mouseReleaseEvent(QMouseEvent event)'''
    def mouseMoveEvent(self, event):
        '''void QQuickItem.mouseMoveEvent(QMouseEvent event)'''
    def mousePressEvent(self, event):
        '''void QQuickItem.mousePressEvent(QMouseEvent event)'''
    def focusOutEvent(self):
        '''QFocusEvent QQuickItem.focusOutEvent()'''
        return QFocusEvent()
    def focusInEvent(self):
        '''QFocusEvent QQuickItem.focusInEvent()'''
        return QFocusEvent()
    def inputMethodEvent(self):
        '''QInputMethodEvent QQuickItem.inputMethodEvent()'''
        return QInputMethodEvent()
    def keyReleaseEvent(self, event):
        '''void QQuickItem.keyReleaseEvent(QKeyEvent event)'''
    def keyPressEvent(self, event):
        '''void QQuickItem.keyPressEvent(QKeyEvent event)'''
    def componentComplete(self):
        '''void QQuickItem.componentComplete()'''
    def classBegin(self):
        '''void QQuickItem.classBegin()'''
    def heightValid(self):
        '''bool QQuickItem.heightValid()'''
        return bool()
    def widthValid(self):
        '''bool QQuickItem.widthValid()'''
        return bool()
    def updateInputMethod(self, queries = None):
        '''void QQuickItem.updateInputMethod(Qt.InputMethodQueries queries = Qt.ImQueryInput)'''
    def itemChange(self):
        '''QQuickItem.ItemChangeData QQuickItem.itemChange()'''
        return QQuickItem.ItemChangeData()
    def isComponentComplete(self):
        '''bool QQuickItem.isComponentComplete()'''
        return bool()
    def event(self):
        '''QEvent QQuickItem.event()'''
        return QEvent()
    def update(self):
        '''void QQuickItem.update()'''
    def textureProvider(self):
        '''QSGTextureProvider QQuickItem.textureProvider()'''
        return QSGTextureProvider()
    def isTextureProvider(self):
        '''bool QQuickItem.isTextureProvider()'''
        return bool()
    def inputMethodQuery(self, query):
        '''QVariant QQuickItem.inputMethodQuery(Qt.InputMethodQuery query)'''
        return QVariant()
    def childAt(self, x, y):
        '''QQuickItem QQuickItem.childAt(float x, float y)'''
        return QQuickItem()
    def forceActiveFocus(self):
        '''void QQuickItem.forceActiveFocus()'''
    def forceActiveFocus(self, reason):
        '''void QQuickItem.forceActiveFocus(Qt.FocusReason reason)'''
    def polish(self):
        '''void QQuickItem.polish()'''
    def mapRectFromScene(self, rect):
        '''QRectF QQuickItem.mapRectFromScene(QRectF rect)'''
        return QRectF()
    def mapRectFromItem(self, item, rect):
        '''QRectF QQuickItem.mapRectFromItem(QQuickItem item, QRectF rect)'''
        return QRectF()
    def mapFromScene(self, point):
        '''QPointF QQuickItem.mapFromScene(QPointF point)'''
        return QPointF()
    def mapFromItem(self, item, point):
        '''QPointF QQuickItem.mapFromItem(QQuickItem item, QPointF point)'''
        return QPointF()
    def mapRectToScene(self, rect):
        '''QRectF QQuickItem.mapRectToScene(QRectF rect)'''
        return QRectF()
    def mapRectToItem(self, item, rect):
        '''QRectF QQuickItem.mapRectToItem(QQuickItem item, QRectF rect)'''
        return QRectF()
    def mapToScene(self, point):
        '''QPointF QQuickItem.mapToScene(QPointF point)'''
        return QPointF()
    def mapToItem(self, item, point):
        '''QPointF QQuickItem.mapToItem(QQuickItem item, QPointF point)'''
        return QPointF()
    def contains(self, point):
        '''bool QQuickItem.contains(QPointF point)'''
        return bool()
    def setKeepTouchGrab(self):
        '''bool QQuickItem.setKeepTouchGrab()'''
        return bool()
    def keepTouchGrab(self):
        '''bool QQuickItem.keepTouchGrab()'''
        return bool()
    def ungrabTouchPoints(self):
        '''void QQuickItem.ungrabTouchPoints()'''
    def grabTouchPoints(self, ids):
        '''void QQuickItem.grabTouchPoints(list-of-int ids)'''
    def setFiltersChildMouseEvents(self, filter):
        '''void QQuickItem.setFiltersChildMouseEvents(bool filter)'''
    def filtersChildMouseEvents(self):
        '''bool QQuickItem.filtersChildMouseEvents()'''
        return bool()
    def setKeepMouseGrab(self):
        '''bool QQuickItem.setKeepMouseGrab()'''
        return bool()
    def keepMouseGrab(self):
        '''bool QQuickItem.keepMouseGrab()'''
        return bool()
    def ungrabMouse(self):
        '''void QQuickItem.ungrabMouse()'''
    def grabMouse(self):
        '''void QQuickItem.grabMouse()'''
    def unsetCursor(self):
        '''void QQuickItem.unsetCursor()'''
    def setCursor(self, cursor):
        '''void QQuickItem.setCursor(QCursor cursor)'''
    def cursor(self):
        '''QCursor QQuickItem.cursor()'''
        return QCursor()
    def setAcceptHoverEvents(self, enabled):
        '''void QQuickItem.setAcceptHoverEvents(bool enabled)'''
    def acceptHoverEvents(self):
        '''bool QQuickItem.acceptHoverEvents()'''
        return bool()
    def setAcceptedMouseButtons(self, buttons):
        '''void QQuickItem.setAcceptedMouseButtons(Qt.MouseButtons buttons)'''
    def acceptedMouseButtons(self):
        '''Qt.MouseButtons QQuickItem.acceptedMouseButtons()'''
        return Qt.MouseButtons()
    def scopedFocusItem(self):
        '''QQuickItem QQuickItem.scopedFocusItem()'''
        return QQuickItem()
    def isFocusScope(self):
        '''bool QQuickItem.isFocusScope()'''
        return bool()
    def setFocus(self):
        '''bool QQuickItem.setFocus()'''
        return bool()
    def setFocus(self, focus, reason):
        '''void QQuickItem.setFocus(bool focus, Qt.FocusReason reason)'''
    def hasFocus(self):
        '''bool QQuickItem.hasFocus()'''
        return bool()
    def hasActiveFocus(self):
        '''bool QQuickItem.hasActiveFocus()'''
        return bool()
    def setFlags(self, flags):
        '''void QQuickItem.setFlags(QQuickItem.Flags flags)'''
    def setFlag(self, flag, enabled = True):
        '''void QQuickItem.setFlag(QQuickItem.Flag flag, bool enabled = True)'''
    def flags(self):
        '''QQuickItem.Flags QQuickItem.flags()'''
        return QQuickItem.Flags()
    def setAntialiasing(self):
        '''bool QQuickItem.setAntialiasing()'''
        return bool()
    def antialiasing(self):
        '''bool QQuickItem.antialiasing()'''
        return bool()
    def setSmooth(self):
        '''bool QQuickItem.setSmooth()'''
        return bool()
    def smooth(self):
        '''bool QQuickItem.smooth()'''
        return bool()
    def setEnabled(self):
        '''bool QQuickItem.setEnabled()'''
        return bool()
    def isEnabled(self):
        '''bool QQuickItem.isEnabled()'''
        return bool()
    def setVisible(self):
        '''bool QQuickItem.setVisible()'''
        return bool()
    def isVisible(self):
        '''bool QQuickItem.isVisible()'''
        return bool()
    def setOpacity(self):
        '''float QQuickItem.setOpacity()'''
        return float()
    def opacity(self):
        '''float QQuickItem.opacity()'''
        return float()
    def setScale(self):
        '''float QQuickItem.setScale()'''
        return float()
    def scale(self):
        '''float QQuickItem.scale()'''
        return float()
    def setRotation(self):
        '''float QQuickItem.setRotation()'''
        return float()
    def rotation(self):
        '''float QQuickItem.rotation()'''
        return float()
    def setZ(self):
        '''float QQuickItem.setZ()'''
        return float()
    def z(self):
        '''float QQuickItem.z()'''
        return float()
    def setTransformOrigin(self):
        '''QQuickItem.TransformOrigin QQuickItem.setTransformOrigin()'''
        return QQuickItem.TransformOrigin()
    def transformOrigin(self):
        '''QQuickItem.TransformOrigin QQuickItem.transformOrigin()'''
        return QQuickItem.TransformOrigin()
    def implicitHeight(self):
        '''float QQuickItem.implicitHeight()'''
        return float()
    def setImplicitHeight(self):
        '''float QQuickItem.setImplicitHeight()'''
        return float()
    def resetHeight(self):
        '''void QQuickItem.resetHeight()'''
    def setHeight(self):
        '''float QQuickItem.setHeight()'''
        return float()
    def height(self):
        '''float QQuickItem.height()'''
        return float()
    def implicitWidth(self):
        '''float QQuickItem.implicitWidth()'''
        return float()
    def setImplicitWidth(self):
        '''float QQuickItem.setImplicitWidth()'''
        return float()
    def resetWidth(self):
        '''void QQuickItem.resetWidth()'''
    def setWidth(self):
        '''float QQuickItem.setWidth()'''
        return float()
    def width(self):
        '''float QQuickItem.width()'''
        return float()
    def setY(self):
        '''float QQuickItem.setY()'''
        return float()
    def setX(self):
        '''float QQuickItem.setX()'''
        return float()
    def y(self):
        '''float QQuickItem.y()'''
        return float()
    def x(self):
        '''float QQuickItem.x()'''
        return float()
    def setBaselineOffset(self):
        '''float QQuickItem.setBaselineOffset()'''
        return float()
    def baselineOffset(self):
        '''float QQuickItem.baselineOffset()'''
        return float()
    def setState(self):
        '''str QQuickItem.setState()'''
        return str()
    def state(self):
        '''str QQuickItem.state()'''
        return str()
    def setClip(self):
        '''bool QQuickItem.setClip()'''
        return bool()
    def clip(self):
        '''bool QQuickItem.clip()'''
        return bool()
    def childItems(self):
        '''list-of-QQuickItem QQuickItem.childItems()'''
        return [QQuickItem()]
    def childrenRect(self):
        '''QRectF QQuickItem.childrenRect()'''
        return QRectF()
    def stackAfter(self):
        '''QQuickItem QQuickItem.stackAfter()'''
        return QQuickItem()
    def stackBefore(self):
        '''QQuickItem QQuickItem.stackBefore()'''
        return QQuickItem()
    def setParentItem(self, parent):
        '''void QQuickItem.setParentItem(QQuickItem parent)'''
    def parentItem(self):
        '''QQuickItem QQuickItem.parentItem()'''
        return QQuickItem()
    def window(self):
        '''QQuickWindow QQuickItem.window()'''
        return QQuickWindow()
    class ItemChangeData():
        """"""
        boolValue = None # bool - member
        item = None # QQuickItem - member
        realValue = None # float - member
        window = None # QQuickWindow - member
        def __init__(self, v):
            '''void QQuickItem.ItemChangeData.__init__(QQuickItem v)'''
        def __init__(self, v):
            '''void QQuickItem.ItemChangeData.__init__(QQuickWindow v)'''
        def __init__(self, v):
            '''void QQuickItem.ItemChangeData.__init__(float v)'''
        def __init__(self, v):
            '''void QQuickItem.ItemChangeData.__init__(bool v)'''
        def __init__(self):
            '''QQuickItem.ItemChangeData QQuickItem.ItemChangeData.__init__()'''
            return QQuickItem.ItemChangeData()
    class Flags():
        """"""
        def __init__(self):
            '''QQuickItem.Flags QQuickItem.Flags.__init__()'''
            return QQuickItem.Flags()
        def __init__(self):
            '''int QQuickItem.Flags.__init__()'''
            return int()
        def __init__(self):
            '''void QQuickItem.Flags.__init__()'''
        def __bool__(self):
            '''int QQuickItem.Flags.__bool__()'''
            return int()
        def __ne__(self, f):
            '''bool QQuickItem.Flags.__ne__(QQuickItem.Flags f)'''
            return bool()
        def __eq__(self, f):
            '''bool QQuickItem.Flags.__eq__(QQuickItem.Flags f)'''
            return bool()
        def __invert__(self):
            '''QQuickItem.Flags QQuickItem.Flags.__invert__()'''
            return QQuickItem.Flags()
        def __and__(self, mask):
            '''QQuickItem.Flags QQuickItem.Flags.__and__(int mask)'''
            return QQuickItem.Flags()
        def __xor__(self, f):
            '''QQuickItem.Flags QQuickItem.Flags.__xor__(QQuickItem.Flags f)'''
            return QQuickItem.Flags()
        def __xor__(self, f):
            '''QQuickItem.Flags QQuickItem.Flags.__xor__(int f)'''
            return QQuickItem.Flags()
        def __or__(self, f):
            '''QQuickItem.Flags QQuickItem.Flags.__or__(QQuickItem.Flags f)'''
            return QQuickItem.Flags()
        def __or__(self, f):
            '''QQuickItem.Flags QQuickItem.Flags.__or__(int f)'''
            return QQuickItem.Flags()
        def __int__(self):
            '''int QQuickItem.Flags.__int__()'''
            return int()
        def __ixor__(self, f):
            '''QQuickItem.Flags QQuickItem.Flags.__ixor__(QQuickItem.Flags f)'''
            return QQuickItem.Flags()
        def __ior__(self, f):
            '''QQuickItem.Flags QQuickItem.Flags.__ior__(QQuickItem.Flags f)'''
            return QQuickItem.Flags()
        def __iand__(self, mask):
            '''QQuickItem.Flags QQuickItem.Flags.__iand__(int mask)'''
            return QQuickItem.Flags()
    class UpdatePaintNodeData():
        """"""
        transformNode = None # QSGTransformNode - member
        def __init__(self):
            '''QQuickItem.UpdatePaintNodeData QQuickItem.UpdatePaintNodeData.__init__()'''
            return QQuickItem.UpdatePaintNodeData()


class QQuickFramebufferObject(QQuickItem):
    """"""
    def __init__(self, parent = None):
        '''void QQuickFramebufferObject.__init__(QQuickItem parent = None)'''
    def releaseResources(self):
        '''void QQuickFramebufferObject.releaseResources()'''
    def textureProvider(self):
        '''QSGTextureProvider QQuickFramebufferObject.textureProvider()'''
        return QSGTextureProvider()
    def isTextureProvider(self):
        '''bool QQuickFramebufferObject.isTextureProvider()'''
        return bool()
    textureFollowsItemSizeChanged = pyqtSignal() # void textureFollowsItemSizeChanged(bool) - signal
    def updatePaintNode(self):
        '''QQuickItem.UpdatePaintNodeData QQuickFramebufferObject.updatePaintNode()'''
        return QQuickItem.UpdatePaintNodeData()
    def geometryChanged(self, newGeometry, oldGeometry):
        '''void QQuickFramebufferObject.geometryChanged(QRectF newGeometry, QRectF oldGeometry)'''
    def createRenderer(self):
        '''abstract QQuickFramebufferObject.Renderer QQuickFramebufferObject.createRenderer()'''
        return QQuickFramebufferObject.Renderer()
    def setTextureFollowsItemSize(self, follows):
        '''void QQuickFramebufferObject.setTextureFollowsItemSize(bool follows)'''
    def textureFollowsItemSize(self):
        '''bool QQuickFramebufferObject.textureFollowsItemSize()'''
        return bool()
    class Renderer():
        """"""
        def __init__(self):
            '''void QQuickFramebufferObject.Renderer.__init__()'''
        def __init__(self):
            '''QQuickFramebufferObject.Renderer QQuickFramebufferObject.Renderer.__init__()'''
            return QQuickFramebufferObject.Renderer()
        def invalidateFramebufferObject(self):
            '''void QQuickFramebufferObject.Renderer.invalidateFramebufferObject()'''
        def update(self):
            '''void QQuickFramebufferObject.Renderer.update()'''
        def framebufferObject(self):
            '''QOpenGLFramebufferObject QQuickFramebufferObject.Renderer.framebufferObject()'''
            return QOpenGLFramebufferObject()
        def synchronize(self):
            '''QQuickFramebufferObject QQuickFramebufferObject.Renderer.synchronize()'''
            return QQuickFramebufferObject()
        def createFramebufferObject(self, size):
            '''QOpenGLFramebufferObject QQuickFramebufferObject.Renderer.createFramebufferObject(QSize size)'''
            return QOpenGLFramebufferObject()
        def render(self):
            '''abstract void QQuickFramebufferObject.Renderer.render()'''


class QQuickTextureFactory(QObject):
    """"""
    def __init__(self):
        '''void QQuickTextureFactory.__init__()'''
    def image(self):
        '''QImage QQuickTextureFactory.image()'''
        return QImage()
    def textureByteCount(self):
        '''abstract int QQuickTextureFactory.textureByteCount()'''
        return int()
    def textureSize(self):
        '''abstract QSize QQuickTextureFactory.textureSize()'''
        return QSize()
    def createTexture(self, window):
        '''abstract QSGTexture QQuickTextureFactory.createTexture(QQuickWindow window)'''
        return QSGTexture()


class QQuickImageProvider(QQmlImageProviderBase):
    """"""
    def __init__(self, type, flags = 0):
        '''void QQuickImageProvider.__init__(QQmlImageProviderBase.ImageType type, QQmlImageProviderBase.Flags flags = 0)'''
    def __init__(self):
        '''QQuickImageProvider QQuickImageProvider.__init__()'''
        return QQuickImageProvider()
    def requestTexture(self, id, size, requestedSize):
        '''QQuickTextureFactory QQuickImageProvider.requestTexture(str id, QSize size, QSize requestedSize)'''
        return QQuickTextureFactory()
    def requestPixmap(self, id, size, requestedSize):
        '''QPixmap QQuickImageProvider.requestPixmap(str id, QSize size, QSize requestedSize)'''
        return QPixmap()
    def requestImage(self, id, size, requestedSize):
        '''QImage QQuickImageProvider.requestImage(str id, QSize size, QSize requestedSize)'''
        return QImage()
    def flags(self):
        '''QQmlImageProviderBase.Flags QQuickImageProvider.flags()'''
        return QQmlImageProviderBase.Flags()
    def imageType(self):
        '''QQmlImageProviderBase.ImageType QQuickImageProvider.imageType()'''
        return QQmlImageProviderBase.ImageType()


class QQuickItemGrabResult(QObject):
    """"""
    ready = pyqtSignal() # void ready() - signal
    def event(self):
        '''QEvent QQuickItemGrabResult.event()'''
        return QEvent()
    def saveToFile(self, fileName):
        '''bool QQuickItemGrabResult.saveToFile(str fileName)'''
        return bool()
    def url(self):
        '''QUrl QQuickItemGrabResult.url()'''
        return QUrl()
    def image(self):
        '''QImage QQuickItemGrabResult.image()'''
        return QImage()


class QQuickPaintedItem(QQuickItem):
    """"""
    # Enum QQuickPaintedItem.PerformanceHint
    FastFBOResizing = 0

    # Enum QQuickPaintedItem.RenderTarget
    Image = 0
    FramebufferObject = 0
    InvertedYFramebufferObject = 0

    def __init__(self, parent = None):
        '''void QQuickPaintedItem.__init__(QQuickItem parent = None)'''
    def releaseResources(self):
        '''void QQuickPaintedItem.releaseResources()'''
    def textureProvider(self):
        '''QSGTextureProvider QQuickPaintedItem.textureProvider()'''
        return QSGTextureProvider()
    def isTextureProvider(self):
        '''bool QQuickPaintedItem.isTextureProvider()'''
        return bool()
    def updatePaintNode(self):
        '''QQuickItem.UpdatePaintNodeData QQuickPaintedItem.updatePaintNode()'''
        return QQuickItem.UpdatePaintNodeData()
    renderTargetChanged = pyqtSignal() # void renderTargetChanged() - signal
    contentsScaleChanged = pyqtSignal() # void contentsScaleChanged() - signal
    contentsSizeChanged = pyqtSignal() # void contentsSizeChanged() - signal
    fillColorChanged = pyqtSignal() # void fillColorChanged() - signal
    def paint(self, painter):
        '''abstract void QQuickPaintedItem.paint(QPainter painter)'''
    def setRenderTarget(self, target):
        '''void QQuickPaintedItem.setRenderTarget(QQuickPaintedItem.RenderTarget target)'''
    def renderTarget(self):
        '''QQuickPaintedItem.RenderTarget QQuickPaintedItem.renderTarget()'''
        return QQuickPaintedItem.RenderTarget()
    def setFillColor(self):
        '''QColor QQuickPaintedItem.setFillColor()'''
        return QColor()
    def fillColor(self):
        '''QColor QQuickPaintedItem.fillColor()'''
        return QColor()
    def setContentsScale(self):
        '''float QQuickPaintedItem.setContentsScale()'''
        return float()
    def contentsScale(self):
        '''float QQuickPaintedItem.contentsScale()'''
        return float()
    def resetContentsSize(self):
        '''void QQuickPaintedItem.resetContentsSize()'''
    def setContentsSize(self):
        '''QSize QQuickPaintedItem.setContentsSize()'''
        return QSize()
    def contentsSize(self):
        '''QSize QQuickPaintedItem.contentsSize()'''
        return QSize()
    def contentsBoundingRect(self):
        '''QRectF QQuickPaintedItem.contentsBoundingRect()'''
        return QRectF()
    def setPerformanceHints(self, hints):
        '''void QQuickPaintedItem.setPerformanceHints(QQuickPaintedItem.PerformanceHints hints)'''
    def setPerformanceHint(self, hint, enabled = True):
        '''void QQuickPaintedItem.setPerformanceHint(QQuickPaintedItem.PerformanceHint hint, bool enabled = True)'''
    def performanceHints(self):
        '''QQuickPaintedItem.PerformanceHints QQuickPaintedItem.performanceHints()'''
        return QQuickPaintedItem.PerformanceHints()
    def setMipmap(self, enable):
        '''void QQuickPaintedItem.setMipmap(bool enable)'''
    def mipmap(self):
        '''bool QQuickPaintedItem.mipmap()'''
        return bool()
    def setAntialiasing(self, enable):
        '''void QQuickPaintedItem.setAntialiasing(bool enable)'''
    def antialiasing(self):
        '''bool QQuickPaintedItem.antialiasing()'''
        return bool()
    def setOpaquePainting(self, opaque):
        '''void QQuickPaintedItem.setOpaquePainting(bool opaque)'''
    def opaquePainting(self):
        '''bool QQuickPaintedItem.opaquePainting()'''
        return bool()
    def update(self, rect = QRect()):
        '''void QQuickPaintedItem.update(QRect rect = QRect())'''
    class PerformanceHints():
        """"""
        def __init__(self):
            '''QQuickPaintedItem.PerformanceHints QQuickPaintedItem.PerformanceHints.__init__()'''
            return QQuickPaintedItem.PerformanceHints()
        def __init__(self):
            '''int QQuickPaintedItem.PerformanceHints.__init__()'''
            return int()
        def __init__(self):
            '''void QQuickPaintedItem.PerformanceHints.__init__()'''
        def __bool__(self):
            '''int QQuickPaintedItem.PerformanceHints.__bool__()'''
            return int()
        def __ne__(self, f):
            '''bool QQuickPaintedItem.PerformanceHints.__ne__(QQuickPaintedItem.PerformanceHints f)'''
            return bool()
        def __eq__(self, f):
            '''bool QQuickPaintedItem.PerformanceHints.__eq__(QQuickPaintedItem.PerformanceHints f)'''
            return bool()
        def __invert__(self):
            '''QQuickPaintedItem.PerformanceHints QQuickPaintedItem.PerformanceHints.__invert__()'''
            return QQuickPaintedItem.PerformanceHints()
        def __and__(self, mask):
            '''QQuickPaintedItem.PerformanceHints QQuickPaintedItem.PerformanceHints.__and__(int mask)'''
            return QQuickPaintedItem.PerformanceHints()
        def __xor__(self, f):
            '''QQuickPaintedItem.PerformanceHints QQuickPaintedItem.PerformanceHints.__xor__(QQuickPaintedItem.PerformanceHints f)'''
            return QQuickPaintedItem.PerformanceHints()
        def __xor__(self, f):
            '''QQuickPaintedItem.PerformanceHints QQuickPaintedItem.PerformanceHints.__xor__(int f)'''
            return QQuickPaintedItem.PerformanceHints()
        def __or__(self, f):
            '''QQuickPaintedItem.PerformanceHints QQuickPaintedItem.PerformanceHints.__or__(QQuickPaintedItem.PerformanceHints f)'''
            return QQuickPaintedItem.PerformanceHints()
        def __or__(self, f):
            '''QQuickPaintedItem.PerformanceHints QQuickPaintedItem.PerformanceHints.__or__(int f)'''
            return QQuickPaintedItem.PerformanceHints()
        def __int__(self):
            '''int QQuickPaintedItem.PerformanceHints.__int__()'''
            return int()
        def __ixor__(self, f):
            '''QQuickPaintedItem.PerformanceHints QQuickPaintedItem.PerformanceHints.__ixor__(QQuickPaintedItem.PerformanceHints f)'''
            return QQuickPaintedItem.PerformanceHints()
        def __ior__(self, f):
            '''QQuickPaintedItem.PerformanceHints QQuickPaintedItem.PerformanceHints.__ior__(QQuickPaintedItem.PerformanceHints f)'''
            return QQuickPaintedItem.PerformanceHints()
        def __iand__(self, mask):
            '''QQuickPaintedItem.PerformanceHints QQuickPaintedItem.PerformanceHints.__iand__(int mask)'''
            return QQuickPaintedItem.PerformanceHints()


class QQuickRenderControl(QObject):
    """"""
    def __init__(self, parent = None):
        '''void QQuickRenderControl.__init__(QObject parent = None)'''
    sceneChanged = pyqtSignal() # void sceneChanged() - signal
    renderRequested = pyqtSignal() # void renderRequested() - signal
    def prepareThread(self, targetThread):
        '''void QQuickRenderControl.prepareThread(QThread targetThread)'''
    def renderWindow(self, offset):
        '''QWindow QQuickRenderControl.renderWindow(QPoint offset)'''
        return QWindow()
    def renderWindowFor(self, win, offset = None):
        '''static QWindow QQuickRenderControl.renderWindowFor(QQuickWindow win, QPoint offset = None)'''
        return QWindow()
    def grab(self):
        '''QImage QQuickRenderControl.grab()'''
        return QImage()
    def sync(self):
        '''bool QQuickRenderControl.sync()'''
        return bool()
    def render(self):
        '''void QQuickRenderControl.render()'''
    def polishItems(self):
        '''void QQuickRenderControl.polishItems()'''
    def invalidate(self):
        '''void QQuickRenderControl.invalidate()'''
    def initialize(self, gl):
        '''void QQuickRenderControl.initialize(QOpenGLContext gl)'''


class QQuickTextDocument(QObject):
    """"""
    def __init__(self, parent):
        '''void QQuickTextDocument.__init__(QQuickItem parent)'''
    def textDocument(self):
        '''QTextDocument QQuickTextDocument.textDocument()'''
        return QTextDocument()


class QQuickWindow(QWindow):
    """"""
    # Enum QQuickWindow.RenderStage
    BeforeSynchronizingStage = 0
    AfterSynchronizingStage = 0
    BeforeRenderingStage = 0
    AfterRenderingStage = 0
    AfterSwapStage = 0

    # Enum QQuickWindow.SceneGraphError
    ContextNotAvailable = 0

    # Enum QQuickWindow.CreateTextureOption
    TextureHasAlphaChannel = 0
    TextureHasMipmaps = 0
    TextureOwnsGLTexture = 0
    TextureCanUseAtlas = 0

    def __init__(self, parent = None):
        '''void QQuickWindow.__init__(QWindow parent = None)'''
    def isSceneGraphInitialized(self):
        '''bool QQuickWindow.isSceneGraphInitialized()'''
        return bool()
    def effectiveDevicePixelRatio(self):
        '''float QQuickWindow.effectiveDevicePixelRatio()'''
        return float()
    def scheduleRenderJob(self, job, schedule):
        '''void QQuickWindow.scheduleRenderJob(QRunnable job, QQuickWindow.RenderStage schedule)'''
    sceneGraphError = pyqtSignal() # void sceneGraphError(QQuickWindow::SceneGraphError,const QStringamp;) - signal
    sceneGraphAboutToStop = pyqtSignal() # void sceneGraphAboutToStop() - signal
    afterAnimating = pyqtSignal() # void afterAnimating() - signal
    afterSynchronizing = pyqtSignal() # void afterSynchronizing() - signal
    openglContextCreated = pyqtSignal() # void openglContextCreated(QOpenGLContext*) - signal
    def resetOpenGLState(self):
        '''void QQuickWindow.resetOpenGLState()'''
    activeFocusItemChanged = pyqtSignal() # void activeFocusItemChanged() - signal
    def setDefaultAlphaBuffer(self, useAlpha):
        '''static void QQuickWindow.setDefaultAlphaBuffer(bool useAlpha)'''
    def hasDefaultAlphaBuffer(self):
        '''static bool QQuickWindow.hasDefaultAlphaBuffer()'''
        return bool()
    def wheelEvent(self):
        '''QWheelEvent QQuickWindow.wheelEvent()'''
        return QWheelEvent()
    def mouseMoveEvent(self):
        '''QMouseEvent QQuickWindow.mouseMoveEvent()'''
        return QMouseEvent()
    def mouseDoubleClickEvent(self):
        '''QMouseEvent QQuickWindow.mouseDoubleClickEvent()'''
        return QMouseEvent()
    def mouseReleaseEvent(self):
        '''QMouseEvent QQuickWindow.mouseReleaseEvent()'''
        return QMouseEvent()
    def mousePressEvent(self):
        '''QMouseEvent QQuickWindow.mousePressEvent()'''
        return QMouseEvent()
    def keyReleaseEvent(self):
        '''QKeyEvent QQuickWindow.keyReleaseEvent()'''
        return QKeyEvent()
    def keyPressEvent(self):
        '''QKeyEvent QQuickWindow.keyPressEvent()'''
        return QKeyEvent()
    def event(self):
        '''QEvent QQuickWindow.event()'''
        return QEvent()
    def focusOutEvent(self):
        '''QFocusEvent QQuickWindow.focusOutEvent()'''
        return QFocusEvent()
    def focusInEvent(self):
        '''QFocusEvent QQuickWindow.focusInEvent()'''
        return QFocusEvent()
    def hideEvent(self):
        '''QHideEvent QQuickWindow.hideEvent()'''
        return QHideEvent()
    def showEvent(self):
        '''QShowEvent QQuickWindow.showEvent()'''
        return QShowEvent()
    def resizeEvent(self):
        '''QResizeEvent QQuickWindow.resizeEvent()'''
        return QResizeEvent()
    def exposeEvent(self):
        '''QExposeEvent QQuickWindow.exposeEvent()'''
        return QExposeEvent()
    def releaseResources(self):
        '''void QQuickWindow.releaseResources()'''
    def update(self):
        '''void QQuickWindow.update()'''
    colorChanged = pyqtSignal() # void colorChanged(const QColoramp;) - signal
    afterRendering = pyqtSignal() # void afterRendering() - signal
    beforeRendering = pyqtSignal() # void beforeRendering() - signal
    beforeSynchronizing = pyqtSignal() # void beforeSynchronizing() - signal
    sceneGraphInvalidated = pyqtSignal() # void sceneGraphInvalidated() - signal
    sceneGraphInitialized = pyqtSignal() # void sceneGraphInitialized() - signal
    frameSwapped = pyqtSignal() # void frameSwapped() - signal
    def openglContext(self):
        '''QOpenGLContext QQuickWindow.openglContext()'''
        return QOpenGLContext()
    def isPersistentSceneGraph(self):
        '''bool QQuickWindow.isPersistentSceneGraph()'''
        return bool()
    def setPersistentSceneGraph(self, persistent):
        '''void QQuickWindow.setPersistentSceneGraph(bool persistent)'''
    def isPersistentOpenGLContext(self):
        '''bool QQuickWindow.isPersistentOpenGLContext()'''
        return bool()
    def setPersistentOpenGLContext(self, persistent):
        '''void QQuickWindow.setPersistentOpenGLContext(bool persistent)'''
    def color(self):
        '''QColor QQuickWindow.color()'''
        return QColor()
    def setColor(self, color):
        '''void QQuickWindow.setColor(QColor color)'''
    def clearBeforeRendering(self):
        '''bool QQuickWindow.clearBeforeRendering()'''
        return bool()
    def setClearBeforeRendering(self, enabled):
        '''void QQuickWindow.setClearBeforeRendering(bool enabled)'''
    def createTextureFromId(self, id, size, options = None):
        '''QSGTexture QQuickWindow.createTextureFromId(int id, QSize size, QQuickWindow.CreateTextureOptions options = (QQuickWindow::CreateTextureOption)0)'''
        return QSGTexture()
    def createTextureFromImage(self, image):
        '''QSGTexture QQuickWindow.createTextureFromImage(QImage image)'''
        return QSGTexture()
    def createTextureFromImage(self, image, options):
        '''QSGTexture QQuickWindow.createTextureFromImage(QImage image, QQuickWindow.CreateTextureOptions options)'''
        return QSGTexture()
    def incubationController(self):
        '''QQmlIncubationController QQuickWindow.incubationController()'''
        return QQmlIncubationController()
    def renderTargetSize(self):
        '''QSize QQuickWindow.renderTargetSize()'''
        return QSize()
    def renderTargetId(self):
        '''int QQuickWindow.renderTargetId()'''
        return int()
    def renderTarget(self):
        '''QOpenGLFramebufferObject QQuickWindow.renderTarget()'''
        return QOpenGLFramebufferObject()
    def setRenderTarget(self, fbo):
        '''void QQuickWindow.setRenderTarget(QOpenGLFramebufferObject fbo)'''
    def setRenderTarget(self, fboId, size):
        '''void QQuickWindow.setRenderTarget(int fboId, QSize size)'''
    def grabWindow(self):
        '''QImage QQuickWindow.grabWindow()'''
        return QImage()
    def sendEvent(self):
        '''QEvent QQuickWindow.sendEvent()'''
        return QEvent()
    def mouseGrabberItem(self):
        '''QQuickItem QQuickWindow.mouseGrabberItem()'''
        return QQuickItem()
    def focusObject(self):
        '''QObject QQuickWindow.focusObject()'''
        return QObject()
    def activeFocusItem(self):
        '''QQuickItem QQuickWindow.activeFocusItem()'''
        return QQuickItem()
    def contentItem(self):
        '''QQuickItem QQuickWindow.contentItem()'''
        return QQuickItem()
    class CreateTextureOptions():
        """"""
        def __init__(self):
            '''QQuickWindow.CreateTextureOptions QQuickWindow.CreateTextureOptions.__init__()'''
            return QQuickWindow.CreateTextureOptions()
        def __init__(self):
            '''int QQuickWindow.CreateTextureOptions.__init__()'''
            return int()
        def __init__(self):
            '''void QQuickWindow.CreateTextureOptions.__init__()'''
        def __bool__(self):
            '''int QQuickWindow.CreateTextureOptions.__bool__()'''
            return int()
        def __ne__(self, f):
            '''bool QQuickWindow.CreateTextureOptions.__ne__(QQuickWindow.CreateTextureOptions f)'''
            return bool()
        def __eq__(self, f):
            '''bool QQuickWindow.CreateTextureOptions.__eq__(QQuickWindow.CreateTextureOptions f)'''
            return bool()
        def __invert__(self):
            '''QQuickWindow.CreateTextureOptions QQuickWindow.CreateTextureOptions.__invert__()'''
            return QQuickWindow.CreateTextureOptions()
        def __and__(self, mask):
            '''QQuickWindow.CreateTextureOptions QQuickWindow.CreateTextureOptions.__and__(int mask)'''
            return QQuickWindow.CreateTextureOptions()
        def __xor__(self, f):
            '''QQuickWindow.CreateTextureOptions QQuickWindow.CreateTextureOptions.__xor__(QQuickWindow.CreateTextureOptions f)'''
            return QQuickWindow.CreateTextureOptions()
        def __xor__(self, f):
            '''QQuickWindow.CreateTextureOptions QQuickWindow.CreateTextureOptions.__xor__(int f)'''
            return QQuickWindow.CreateTextureOptions()
        def __or__(self, f):
            '''QQuickWindow.CreateTextureOptions QQuickWindow.CreateTextureOptions.__or__(QQuickWindow.CreateTextureOptions f)'''
            return QQuickWindow.CreateTextureOptions()
        def __or__(self, f):
            '''QQuickWindow.CreateTextureOptions QQuickWindow.CreateTextureOptions.__or__(int f)'''
            return QQuickWindow.CreateTextureOptions()
        def __int__(self):
            '''int QQuickWindow.CreateTextureOptions.__int__()'''
            return int()
        def __ixor__(self, f):
            '''QQuickWindow.CreateTextureOptions QQuickWindow.CreateTextureOptions.__ixor__(QQuickWindow.CreateTextureOptions f)'''
            return QQuickWindow.CreateTextureOptions()
        def __ior__(self, f):
            '''QQuickWindow.CreateTextureOptions QQuickWindow.CreateTextureOptions.__ior__(QQuickWindow.CreateTextureOptions f)'''
            return QQuickWindow.CreateTextureOptions()
        def __iand__(self, mask):
            '''QQuickWindow.CreateTextureOptions QQuickWindow.CreateTextureOptions.__iand__(int mask)'''
            return QQuickWindow.CreateTextureOptions()


class QQuickView(QQuickWindow):
    """"""
    # Enum QQuickView.Status
    Null = 0
    Ready = 0
    Loading = 0
    Error = 0

    # Enum QQuickView.ResizeMode
    SizeViewToRootObject = 0
    SizeRootObjectToView = 0

    def __init__(self, parent = None):
        '''void QQuickView.__init__(QWindow parent = None)'''
    def __init__(self, engine, parent):
        '''void QQuickView.__init__(QQmlEngine engine, QWindow parent)'''
    def __init__(self, source, parent = None):
        '''void QQuickView.__init__(QUrl source, QWindow parent = None)'''
    def mouseMoveEvent(self):
        '''QMouseEvent QQuickView.mouseMoveEvent()'''
        return QMouseEvent()
    def mouseReleaseEvent(self):
        '''QMouseEvent QQuickView.mouseReleaseEvent()'''
        return QMouseEvent()
    def mousePressEvent(self):
        '''QMouseEvent QQuickView.mousePressEvent()'''
        return QMouseEvent()
    def keyReleaseEvent(self):
        '''QKeyEvent QQuickView.keyReleaseEvent()'''
        return QKeyEvent()
    def keyPressEvent(self):
        '''QKeyEvent QQuickView.keyPressEvent()'''
        return QKeyEvent()
    def timerEvent(self):
        '''QTimerEvent QQuickView.timerEvent()'''
        return QTimerEvent()
    def resizeEvent(self):
        '''QResizeEvent QQuickView.resizeEvent()'''
        return QResizeEvent()
    statusChanged = pyqtSignal() # void statusChanged(QQuickView::Status) - signal
    def setSource(self):
        '''QUrl QQuickView.setSource()'''
        return QUrl()
    def initialSize(self):
        '''QSize QQuickView.initialSize()'''
        return QSize()
    def errors(self):
        '''list-of-QQmlError QQuickView.errors()'''
        return [QQmlError()]
    def status(self):
        '''QQuickView.Status QQuickView.status()'''
        return QQuickView.Status()
    def setResizeMode(self):
        '''QQuickView.ResizeMode QQuickView.setResizeMode()'''
        return QQuickView.ResizeMode()
    def resizeMode(self):
        '''QQuickView.ResizeMode QQuickView.resizeMode()'''
        return QQuickView.ResizeMode()
    def rootObject(self):
        '''QQuickItem QQuickView.rootObject()'''
        return QQuickItem()
    def rootContext(self):
        '''QQmlContext QQuickView.rootContext()'''
        return QQmlContext()
    def engine(self):
        '''QQmlEngine QQuickView.engine()'''
        return QQmlEngine()
    def source(self):
        '''QUrl QQuickView.source()'''
        return QUrl()


class QSGAbstractRenderer(QObject):
    """"""
    # Enum QSGAbstractRenderer.ClearModeBit
    ClearColorBuffer = 0
    ClearDepthBuffer = 0
    ClearStencilBuffer = 0

    sceneGraphChanged = pyqtSignal() # void sceneGraphChanged() - signal
    def renderScene(self, fboId = 0):
        '''abstract void QSGAbstractRenderer.renderScene(int fboId = 0)'''
    def clearMode(self):
        '''QSGAbstractRenderer.ClearMode QSGAbstractRenderer.clearMode()'''
        return QSGAbstractRenderer.ClearMode()
    def setClearMode(self, mode):
        '''void QSGAbstractRenderer.setClearMode(QSGAbstractRenderer.ClearMode mode)'''
    def clearColor(self):
        '''QColor QSGAbstractRenderer.clearColor()'''
        return QColor()
    def setClearColor(self, color):
        '''void QSGAbstractRenderer.setClearColor(QColor color)'''
    def projectionMatrix(self):
        '''QMatrix4x4 QSGAbstractRenderer.projectionMatrix()'''
        return QMatrix4x4()
    def setProjectionMatrix(self, matrix):
        '''void QSGAbstractRenderer.setProjectionMatrix(QMatrix4x4 matrix)'''
    def setProjectionMatrixToRect(self, rect):
        '''void QSGAbstractRenderer.setProjectionMatrixToRect(QRectF rect)'''
    def viewportRect(self):
        '''QRect QSGAbstractRenderer.viewportRect()'''
        return QRect()
    def setViewportRect(self, rect):
        '''void QSGAbstractRenderer.setViewportRect(QRect rect)'''
    def setViewportRect(self, size):
        '''void QSGAbstractRenderer.setViewportRect(QSize size)'''
    def deviceRect(self):
        '''QRect QSGAbstractRenderer.deviceRect()'''
        return QRect()
    def setDeviceRect(self, rect):
        '''void QSGAbstractRenderer.setDeviceRect(QRect rect)'''
    def setDeviceRect(self, size):
        '''void QSGAbstractRenderer.setDeviceRect(QSize size)'''
    class ClearMode():
        """"""
        def __init__(self):
            '''QSGAbstractRenderer.ClearMode QSGAbstractRenderer.ClearMode.__init__()'''
            return QSGAbstractRenderer.ClearMode()
        def __init__(self):
            '''int QSGAbstractRenderer.ClearMode.__init__()'''
            return int()
        def __init__(self):
            '''void QSGAbstractRenderer.ClearMode.__init__()'''
        def __bool__(self):
            '''int QSGAbstractRenderer.ClearMode.__bool__()'''
            return int()
        def __ne__(self, f):
            '''bool QSGAbstractRenderer.ClearMode.__ne__(QSGAbstractRenderer.ClearMode f)'''
            return bool()
        def __eq__(self, f):
            '''bool QSGAbstractRenderer.ClearMode.__eq__(QSGAbstractRenderer.ClearMode f)'''
            return bool()
        def __invert__(self):
            '''QSGAbstractRenderer.ClearMode QSGAbstractRenderer.ClearMode.__invert__()'''
            return QSGAbstractRenderer.ClearMode()
        def __and__(self, mask):
            '''QSGAbstractRenderer.ClearMode QSGAbstractRenderer.ClearMode.__and__(int mask)'''
            return QSGAbstractRenderer.ClearMode()
        def __xor__(self, f):
            '''QSGAbstractRenderer.ClearMode QSGAbstractRenderer.ClearMode.__xor__(QSGAbstractRenderer.ClearMode f)'''
            return QSGAbstractRenderer.ClearMode()
        def __xor__(self, f):
            '''QSGAbstractRenderer.ClearMode QSGAbstractRenderer.ClearMode.__xor__(int f)'''
            return QSGAbstractRenderer.ClearMode()
        def __or__(self, f):
            '''QSGAbstractRenderer.ClearMode QSGAbstractRenderer.ClearMode.__or__(QSGAbstractRenderer.ClearMode f)'''
            return QSGAbstractRenderer.ClearMode()
        def __or__(self, f):
            '''QSGAbstractRenderer.ClearMode QSGAbstractRenderer.ClearMode.__or__(int f)'''
            return QSGAbstractRenderer.ClearMode()
        def __int__(self):
            '''int QSGAbstractRenderer.ClearMode.__int__()'''
            return int()
        def __ixor__(self, f):
            '''QSGAbstractRenderer.ClearMode QSGAbstractRenderer.ClearMode.__ixor__(QSGAbstractRenderer.ClearMode f)'''
            return QSGAbstractRenderer.ClearMode()
        def __ior__(self, f):
            '''QSGAbstractRenderer.ClearMode QSGAbstractRenderer.ClearMode.__ior__(QSGAbstractRenderer.ClearMode f)'''
            return QSGAbstractRenderer.ClearMode()
        def __iand__(self, mask):
            '''QSGAbstractRenderer.ClearMode QSGAbstractRenderer.ClearMode.__iand__(int mask)'''
            return QSGAbstractRenderer.ClearMode()


class QSGEngine(QObject):
    """"""
    # Enum QSGEngine.CreateTextureOption
    TextureHasAlphaChannel = 0
    TextureOwnsGLTexture = 0
    TextureCanUseAtlas = 0

    def __init__(self, parent = None):
        '''void QSGEngine.__init__(QObject parent = None)'''
    def createTextureFromId(self, id, size, options = None):
        '''QSGTexture QSGEngine.createTextureFromId(int id, QSize size, QSGEngine.CreateTextureOptions options = (QSGEngine::CreateTextureOption)0)'''
        return QSGTexture()
    def createTextureFromImage(self, image, options = None):
        '''QSGTexture QSGEngine.createTextureFromImage(QImage image, QSGEngine.CreateTextureOptions options = (QSGEngine::CreateTextureOption)0)'''
        return QSGTexture()
    def createRenderer(self):
        '''QSGAbstractRenderer QSGEngine.createRenderer()'''
        return QSGAbstractRenderer()
    def invalidate(self):
        '''void QSGEngine.invalidate()'''
    def initialize(self, context):
        '''void QSGEngine.initialize(QOpenGLContext context)'''
    class CreateTextureOptions():
        """"""
        def __init__(self):
            '''QSGEngine.CreateTextureOptions QSGEngine.CreateTextureOptions.__init__()'''
            return QSGEngine.CreateTextureOptions()
        def __init__(self):
            '''int QSGEngine.CreateTextureOptions.__init__()'''
            return int()
        def __init__(self):
            '''void QSGEngine.CreateTextureOptions.__init__()'''
        def __bool__(self):
            '''int QSGEngine.CreateTextureOptions.__bool__()'''
            return int()
        def __ne__(self, f):
            '''bool QSGEngine.CreateTextureOptions.__ne__(QSGEngine.CreateTextureOptions f)'''
            return bool()
        def __eq__(self, f):
            '''bool QSGEngine.CreateTextureOptions.__eq__(QSGEngine.CreateTextureOptions f)'''
            return bool()
        def __invert__(self):
            '''QSGEngine.CreateTextureOptions QSGEngine.CreateTextureOptions.__invert__()'''
            return QSGEngine.CreateTextureOptions()
        def __and__(self, mask):
            '''QSGEngine.CreateTextureOptions QSGEngine.CreateTextureOptions.__and__(int mask)'''
            return QSGEngine.CreateTextureOptions()
        def __xor__(self, f):
            '''QSGEngine.CreateTextureOptions QSGEngine.CreateTextureOptions.__xor__(QSGEngine.CreateTextureOptions f)'''
            return QSGEngine.CreateTextureOptions()
        def __xor__(self, f):
            '''QSGEngine.CreateTextureOptions QSGEngine.CreateTextureOptions.__xor__(int f)'''
            return QSGEngine.CreateTextureOptions()
        def __or__(self, f):
            '''QSGEngine.CreateTextureOptions QSGEngine.CreateTextureOptions.__or__(QSGEngine.CreateTextureOptions f)'''
            return QSGEngine.CreateTextureOptions()
        def __or__(self, f):
            '''QSGEngine.CreateTextureOptions QSGEngine.CreateTextureOptions.__or__(int f)'''
            return QSGEngine.CreateTextureOptions()
        def __int__(self):
            '''int QSGEngine.CreateTextureOptions.__int__()'''
            return int()
        def __ixor__(self, f):
            '''QSGEngine.CreateTextureOptions QSGEngine.CreateTextureOptions.__ixor__(QSGEngine.CreateTextureOptions f)'''
            return QSGEngine.CreateTextureOptions()
        def __ior__(self, f):
            '''QSGEngine.CreateTextureOptions QSGEngine.CreateTextureOptions.__ior__(QSGEngine.CreateTextureOptions f)'''
            return QSGEngine.CreateTextureOptions()
        def __iand__(self, mask):
            '''QSGEngine.CreateTextureOptions QSGEngine.CreateTextureOptions.__iand__(int mask)'''
            return QSGEngine.CreateTextureOptions()


class QSGMaterial():
    """"""
    # Enum QSGMaterial.Flag
    Blending = 0
    RequiresDeterminant = 0
    RequiresFullMatrixExceptTranslate = 0
    RequiresFullMatrix = 0
    CustomCompileStep = 0

    def __init__(self):
        '''void QSGMaterial.__init__()'''
    def setFlag(self, flags, enabled = True):
        '''void QSGMaterial.setFlag(QSGMaterial.Flags flags, bool enabled = True)'''
    def flags(self):
        '''QSGMaterial.Flags QSGMaterial.flags()'''
        return QSGMaterial.Flags()
    def compare(self, other):
        '''int QSGMaterial.compare(QSGMaterial other)'''
        return int()
    def createShader(self):
        '''abstract QSGMaterialShader QSGMaterial.createShader()'''
        return QSGMaterialShader()
    def type(self):
        '''abstract QSGMaterialType QSGMaterial.type()'''
        return QSGMaterialType()
    class Flags():
        """"""
        def __init__(self):
            '''QSGMaterial.Flags QSGMaterial.Flags.__init__()'''
            return QSGMaterial.Flags()
        def __init__(self):
            '''int QSGMaterial.Flags.__init__()'''
            return int()
        def __init__(self):
            '''void QSGMaterial.Flags.__init__()'''
        def __bool__(self):
            '''int QSGMaterial.Flags.__bool__()'''
            return int()
        def __ne__(self, f):
            '''bool QSGMaterial.Flags.__ne__(QSGMaterial.Flags f)'''
            return bool()
        def __eq__(self, f):
            '''bool QSGMaterial.Flags.__eq__(QSGMaterial.Flags f)'''
            return bool()
        def __invert__(self):
            '''QSGMaterial.Flags QSGMaterial.Flags.__invert__()'''
            return QSGMaterial.Flags()
        def __and__(self, mask):
            '''QSGMaterial.Flags QSGMaterial.Flags.__and__(int mask)'''
            return QSGMaterial.Flags()
        def __xor__(self, f):
            '''QSGMaterial.Flags QSGMaterial.Flags.__xor__(QSGMaterial.Flags f)'''
            return QSGMaterial.Flags()
        def __xor__(self, f):
            '''QSGMaterial.Flags QSGMaterial.Flags.__xor__(int f)'''
            return QSGMaterial.Flags()
        def __or__(self, f):
            '''QSGMaterial.Flags QSGMaterial.Flags.__or__(QSGMaterial.Flags f)'''
            return QSGMaterial.Flags()
        def __or__(self, f):
            '''QSGMaterial.Flags QSGMaterial.Flags.__or__(int f)'''
            return QSGMaterial.Flags()
        def __int__(self):
            '''int QSGMaterial.Flags.__int__()'''
            return int()
        def __ixor__(self, f):
            '''QSGMaterial.Flags QSGMaterial.Flags.__ixor__(QSGMaterial.Flags f)'''
            return QSGMaterial.Flags()
        def __ior__(self, f):
            '''QSGMaterial.Flags QSGMaterial.Flags.__ior__(QSGMaterial.Flags f)'''
            return QSGMaterial.Flags()
        def __iand__(self, mask):
            '''QSGMaterial.Flags QSGMaterial.Flags.__iand__(int mask)'''
            return QSGMaterial.Flags()


class QSGFlatColorMaterial(QSGMaterial):
    """"""
    def __init__(self):
        '''void QSGFlatColorMaterial.__init__()'''
    def compare(self, other):
        '''int QSGFlatColorMaterial.compare(QSGMaterial other)'''
        return int()
    def color(self):
        '''QColor QSGFlatColorMaterial.color()'''
        return QColor()
    def setColor(self, color):
        '''void QSGFlatColorMaterial.setColor(QColor color)'''
    def createShader(self):
        '''QSGMaterialShader QSGFlatColorMaterial.createShader()'''
        return QSGMaterialShader()
    def type(self):
        '''QSGMaterialType QSGFlatColorMaterial.type()'''
        return QSGMaterialType()


class QSGGeometry():
    """"""
    # Enum QSGGeometry.DataPattern
    AlwaysUploadPattern = 0
    StreamPattern = 0
    DynamicPattern = 0
    StaticPattern = 0

    GL_POINTS = None # int - member
    GL_LINES = None # int - member
    GL_LINE_LOOP = None # int - member
    GL_LINE_STRIP = None # int - member
    GL_TRIANGLES = None # int - member
    GL_TRIANGLE_STRIP = None # int - member
    GL_TRIANGLE_FAN = None # int - member
    GL_BYTE = None # int - member
    GL_DOUBLE = None # int - member
    GL_FLOAT = None # int - member
    GL_INT = None # int - member
    def __init__(self, attribs, vertexCount, indexCount = 0, indexType = None):
        '''void QSGGeometry.__init__(QSGGeometry.AttributeSet attribs, int vertexCount, int indexCount = 0, int indexType = GL_UNSIGNED_SHORT)'''
    def __init__(self):
        '''QSGGeometry QSGGeometry.__init__()'''
        return QSGGeometry()
    def sizeOfIndex(self):
        '''int QSGGeometry.sizeOfIndex()'''
        return int()
    def vertexDataAsColoredPoint2D(self):
        '''array-of-QSGGeometry.ColoredPoint2D QSGGeometry.vertexDataAsColoredPoint2D()'''
        return array-of-QSGGeometry.ColoredPoint2D()
    def vertexDataAsTexturedPoint2D(self):
        '''array-of-QSGGeometry.TexturedPoint2D QSGGeometry.vertexDataAsTexturedPoint2D()'''
        return array-of-QSGGeometry.TexturedPoint2D()
    def vertexDataAsPoint2D(self):
        '''array-of-QSGGeometry.Point2D QSGGeometry.vertexDataAsPoint2D()'''
        return array-of-QSGGeometry.Point2D()
    def indexDataAsUShort(self):
        '''array-of-unsigned-short QSGGeometry.indexDataAsUShort()'''
        return array-of-unsigned-short()
    def indexDataAsUInt(self):
        '''array-of-unsigned-int QSGGeometry.indexDataAsUInt()'''
        return array-of-unsigned-int()
    def setLineWidth(self, w):
        '''void QSGGeometry.setLineWidth(float w)'''
    def lineWidth(self):
        '''float QSGGeometry.lineWidth()'''
        return float()
    def markVertexDataDirty(self):
        '''void QSGGeometry.markVertexDataDirty()'''
    def markIndexDataDirty(self):
        '''void QSGGeometry.markIndexDataDirty()'''
    def vertexDataPattern(self):
        '''QSGGeometry.DataPattern QSGGeometry.vertexDataPattern()'''
        return QSGGeometry.DataPattern()
    def setVertexDataPattern(self, p):
        '''void QSGGeometry.setVertexDataPattern(QSGGeometry.DataPattern p)'''
    def indexDataPattern(self):
        '''QSGGeometry.DataPattern QSGGeometry.indexDataPattern()'''
        return QSGGeometry.DataPattern()
    def setIndexDataPattern(self, p):
        '''void QSGGeometry.setIndexDataPattern(QSGGeometry.DataPattern p)'''
    def updateTexturedRectGeometry(self, g, rect, sourceRect):
        '''static void QSGGeometry.updateTexturedRectGeometry(QSGGeometry g, QRectF rect, QRectF sourceRect)'''
    def updateRectGeometry(self, g, rect):
        '''static void QSGGeometry.updateRectGeometry(QSGGeometry g, QRectF rect)'''
    def sizeOfVertex(self):
        '''int QSGGeometry.sizeOfVertex()'''
        return int()
    def attributes(self):
        '''read-only-array-of-QSGGeometry.Attribute QSGGeometry.attributes()'''
        return read-only-array-of-QSGGeometry.Attribute()
    def attributeCount(self):
        '''int QSGGeometry.attributeCount()'''
        return int()
    def indexData(self):
        '''sip.voidptr QSGGeometry.indexData()'''
        return sip.voidptr()
    def indexCount(self):
        '''int QSGGeometry.indexCount()'''
        return int()
    def indexType(self):
        '''int QSGGeometry.indexType()'''
        return int()
    def vertexData(self):
        '''sip.voidptr QSGGeometry.vertexData()'''
        return sip.voidptr()
    def vertexCount(self):
        '''int QSGGeometry.vertexCount()'''
        return int()
    def allocate(self, vertexCount, indexCount = 0):
        '''void QSGGeometry.allocate(int vertexCount, int indexCount = 0)'''
    def drawingMode(self):
        '''int QSGGeometry.drawingMode()'''
        return int()
    def setDrawingMode(self, mode):
        '''void QSGGeometry.setDrawingMode(int mode)'''
    def defaultAttributes_ColoredPoint2D(self):
        '''static QSGGeometry.AttributeSet QSGGeometry.defaultAttributes_ColoredPoint2D()'''
        return QSGGeometry.AttributeSet()
    def defaultAttributes_TexturedPoint2D(self):
        '''static QSGGeometry.AttributeSet QSGGeometry.defaultAttributes_TexturedPoint2D()'''
        return QSGGeometry.AttributeSet()
    def defaultAttributes_Point2D(self):
        '''static QSGGeometry.AttributeSet QSGGeometry.defaultAttributes_Point2D()'''
        return QSGGeometry.AttributeSet()
    class Point2D():
        """"""
        x = None # float - member
        y = None # float - member
        def __init__(self):
            '''void QSGGeometry.Point2D.__init__()'''
        def __init__(self):
            '''QSGGeometry.Point2D QSGGeometry.Point2D.__init__()'''
            return QSGGeometry.Point2D()
        def set(self, nx, ny):
            '''void QSGGeometry.Point2D.set(float nx, float ny)'''
    class TexturedPoint2D():
        """"""
        tx = None # float - member
        ty = None # float - member
        x = None # float - member
        y = None # float - member
        def __init__(self):
            '''void QSGGeometry.TexturedPoint2D.__init__()'''
        def __init__(self):
            '''QSGGeometry.TexturedPoint2D QSGGeometry.TexturedPoint2D.__init__()'''
            return QSGGeometry.TexturedPoint2D()
        def set(self, nx, ny, ntx, nty):
            '''void QSGGeometry.TexturedPoint2D.set(float nx, float ny, float ntx, float nty)'''
    class Attribute():
        """"""
        isVertexCoordinate = None # int - member
        position = None # int - member
        tupleSize = None # int - member
        type = None # int - member
        def __init__(self):
            '''void QSGGeometry.Attribute.__init__()'''
        def __init__(self):
            '''QSGGeometry.Attribute QSGGeometry.Attribute.__init__()'''
            return QSGGeometry.Attribute()
        def create(self, pos, tupleSize, primitiveType, isPosition = False):
            '''static QSGGeometry.Attribute QSGGeometry.Attribute.create(int pos, int tupleSize, int primitiveType, bool isPosition = False)'''
            return QSGGeometry.Attribute()
    class ColoredPoint2D():
        """"""
        a = None # int - member
        b = None # int - member
        g = None # int - member
        r = None # int - member
        x = None # float - member
        y = None # float - member
        def __init__(self):
            '''void QSGGeometry.ColoredPoint2D.__init__()'''
        def __init__(self):
            '''QSGGeometry.ColoredPoint2D QSGGeometry.ColoredPoint2D.__init__()'''
            return QSGGeometry.ColoredPoint2D()
        def set(self, nx, ny, nr, ng, nb, na):
            '''void QSGGeometry.ColoredPoint2D.set(float nx, float ny, int nr, int ng, int nb, int na)'''
    class AttributeSet():
        """"""
        attributes = None # read-only-array-of-QSGGeometry.Attribute - member
        count = None # int - member
        stride = None # int - member
        def __init__(self, attributes, stride = 0):
            '''void QSGGeometry.AttributeSet.__init__(sequence-of-QSGGeometry.Attribute attributes, int stride = 0)'''


class QSGMaterialShader():
    """"""
    def __init__(self):
        '''void QSGMaterialShader.__init__()'''
    def setShaderSourceFiles(self, type, sourceFiles):
        '''void QSGMaterialShader.setShaderSourceFiles(QOpenGLShader.ShaderType type, list-of-str sourceFiles)'''
    def setShaderSourceFile(self, type, sourceFile):
        '''void QSGMaterialShader.setShaderSourceFile(QOpenGLShader.ShaderType type, str sourceFile)'''
    def fragmentShader(self):
        '''str QSGMaterialShader.fragmentShader()'''
        return str()
    def vertexShader(self):
        '''str QSGMaterialShader.vertexShader()'''
        return str()
    def initialize(self):
        '''void QSGMaterialShader.initialize()'''
    def compile(self):
        '''void QSGMaterialShader.compile()'''
    def program(self):
        '''QOpenGLShaderProgram QSGMaterialShader.program()'''
        return QOpenGLShaderProgram()
    def attributeNames(self):
        '''abstract list-of-str QSGMaterialShader.attributeNames()'''
        return [str()]
    def updateState(self, state, newMaterial, oldMaterial):
        '''void QSGMaterialShader.updateState(QSGMaterialShader.RenderState state, QSGMaterial newMaterial, QSGMaterial oldMaterial)'''
    def deactivate(self):
        '''void QSGMaterialShader.deactivate()'''
    def activate(self):
        '''void QSGMaterialShader.activate()'''
    class RenderState():
        """"""
        class DirtyStates():
            """"""
            def __init__(self):
                '''QSGMaterialShader.RenderState.DirtyStates QSGMaterialShader.RenderState.DirtyStates.__init__()'''
                return QSGMaterialShader.RenderState.DirtyStates()
            def __init__(self):
                '''int QSGMaterialShader.RenderState.DirtyStates.__init__()'''
                return int()
            def __init__(self):
                '''void QSGMaterialShader.RenderState.DirtyStates.__init__()'''
            def __bool__(self):
                '''int QSGMaterialShader.RenderState.DirtyStates.__bool__()'''
                return int()
            def __ne__(self, f):
                '''bool QSGMaterialShader.RenderState.DirtyStates.__ne__(QSGMaterialShader.RenderState.DirtyStates f)'''
                return bool()
            def __eq__(self, f):
                '''bool QSGMaterialShader.RenderState.DirtyStates.__eq__(QSGMaterialShader.RenderState.DirtyStates f)'''
                return bool()
            def __invert__(self):
                '''QSGMaterialShader.RenderState.DirtyStates QSGMaterialShader.RenderState.DirtyStates.__invert__()'''
                return QSGMaterialShader.RenderState.DirtyStates()
            def __and__(self, mask):
                '''QSGMaterialShader.RenderState.DirtyStates QSGMaterialShader.RenderState.DirtyStates.__and__(int mask)'''
                return QSGMaterialShader.RenderState.DirtyStates()
            def __xor__(self, f):
                '''QSGMaterialShader.RenderState.DirtyStates QSGMaterialShader.RenderState.DirtyStates.__xor__(QSGMaterialShader.RenderState.DirtyStates f)'''
                return QSGMaterialShader.RenderState.DirtyStates()
            def __xor__(self, f):
                '''QSGMaterialShader.RenderState.DirtyStates QSGMaterialShader.RenderState.DirtyStates.__xor__(int f)'''
                return QSGMaterialShader.RenderState.DirtyStates()
            def __or__(self, f):
                '''QSGMaterialShader.RenderState.DirtyStates QSGMaterialShader.RenderState.DirtyStates.__or__(QSGMaterialShader.RenderState.DirtyStates f)'''
                return QSGMaterialShader.RenderState.DirtyStates()
            def __or__(self, f):
                '''QSGMaterialShader.RenderState.DirtyStates QSGMaterialShader.RenderState.DirtyStates.__or__(int f)'''
                return QSGMaterialShader.RenderState.DirtyStates()
            def __int__(self):
                '''int QSGMaterialShader.RenderState.DirtyStates.__int__()'''
                return int()
            def __ixor__(self, f):
                '''QSGMaterialShader.RenderState.DirtyStates QSGMaterialShader.RenderState.DirtyStates.__ixor__(QSGMaterialShader.RenderState.DirtyStates f)'''
                return QSGMaterialShader.RenderState.DirtyStates()
            def __ior__(self, f):
                '''QSGMaterialShader.RenderState.DirtyStates QSGMaterialShader.RenderState.DirtyStates.__ior__(QSGMaterialShader.RenderState.DirtyStates f)'''
                return QSGMaterialShader.RenderState.DirtyStates()
            def __iand__(self, mask):
                '''QSGMaterialShader.RenderState.DirtyStates QSGMaterialShader.RenderState.DirtyStates.__iand__(int mask)'''
                return QSGMaterialShader.RenderState.DirtyStates()
    class RenderState():
        """"""
        # Enum QSGMaterialShader.RenderState.DirtyState
        DirtyMatrix = 0
        DirtyOpacity = 0
    
        def __init__(self):
            '''void QSGMaterialShader.RenderState.__init__()'''
        def __init__(self):
            '''QSGMaterialShader.RenderState QSGMaterialShader.RenderState.__init__()'''
            return QSGMaterialShader.RenderState()
        def devicePixelRatio(self):
            '''float QSGMaterialShader.RenderState.devicePixelRatio()'''
            return float()
        def projectionMatrix(self):
            '''QMatrix4x4 QSGMaterialShader.RenderState.projectionMatrix()'''
            return QMatrix4x4()
        def context(self):
            '''QOpenGLContext QSGMaterialShader.RenderState.context()'''
            return QOpenGLContext()
        def determinant(self):
            '''float QSGMaterialShader.RenderState.determinant()'''
            return float()
        def deviceRect(self):
            '''QRect QSGMaterialShader.RenderState.deviceRect()'''
            return QRect()
        def viewportRect(self):
            '''QRect QSGMaterialShader.RenderState.viewportRect()'''
            return QRect()
        def modelViewMatrix(self):
            '''QMatrix4x4 QSGMaterialShader.RenderState.modelViewMatrix()'''
            return QMatrix4x4()
        def combinedMatrix(self):
            '''QMatrix4x4 QSGMaterialShader.RenderState.combinedMatrix()'''
            return QMatrix4x4()
        def opacity(self):
            '''float QSGMaterialShader.RenderState.opacity()'''
            return float()
        def isOpacityDirty(self):
            '''bool QSGMaterialShader.RenderState.isOpacityDirty()'''
            return bool()
        def isMatrixDirty(self):
            '''bool QSGMaterialShader.RenderState.isMatrixDirty()'''
            return bool()
        def dirtyStates(self):
            '''QSGMaterialShader.RenderState.DirtyStates QSGMaterialShader.RenderState.dirtyStates()'''
            return QSGMaterialShader.RenderState.DirtyStates()


class QSGMaterialType():
    """"""
    def __init__(self):
        '''void QSGMaterialType.__init__()'''
    def __init__(self):
        '''QSGMaterialType QSGMaterialType.__init__()'''
        return QSGMaterialType()


class QSGNode():
    """"""
    # Enum QSGNode.DirtyStateBit
    DirtyMatrix = 0
    DirtyNodeAdded = 0
    DirtyNodeRemoved = 0
    DirtyGeometry = 0
    DirtyMaterial = 0
    DirtyOpacity = 0

    # Enum QSGNode.Flag
    OwnedByParent = 0
    UsePreprocess = 0
    OwnsGeometry = 0
    OwnsMaterial = 0
    OwnsOpaqueMaterial = 0

    # Enum QSGNode.NodeType
    BasicNodeType = 0
    GeometryNodeType = 0
    TransformNodeType = 0
    ClipNodeType = 0
    OpacityNodeType = 0

    def __init__(self):
        '''void QSGNode.__init__()'''
    def preprocess(self):
        '''void QSGNode.preprocess()'''
    def setFlags(self, enabled = True):
        '''QSGNode.Flags QSGNode.setFlags(bool enabled = True)'''
        return QSGNode.Flags()
    def setFlag(self, enabled = True):
        '''QSGNode.Flag QSGNode.setFlag(bool enabled = True)'''
        return QSGNode.Flag()
    def flags(self):
        '''QSGNode.Flags QSGNode.flags()'''
        return QSGNode.Flags()
    def isSubtreeBlocked(self):
        '''bool QSGNode.isSubtreeBlocked()'''
        return bool()
    def markDirty(self, bits):
        '''void QSGNode.markDirty(QSGNode.DirtyState bits)'''
    def type(self):
        '''QSGNode.NodeType QSGNode.type()'''
        return QSGNode.NodeType()
    def previousSibling(self):
        '''QSGNode QSGNode.previousSibling()'''
        return QSGNode()
    def nextSibling(self):
        '''QSGNode QSGNode.nextSibling()'''
        return QSGNode()
    def lastChild(self):
        '''QSGNode QSGNode.lastChild()'''
        return QSGNode()
    def firstChild(self):
        '''QSGNode QSGNode.firstChild()'''
        return QSGNode()
    def childAtIndex(self, i):
        '''QSGNode QSGNode.childAtIndex(int i)'''
        return QSGNode()
    def __len__(self):
        ''' QSGNode.__len__()'''
        return ()
    def childCount(self):
        '''int QSGNode.childCount()'''
        return int()
    def insertChildNodeAfter(self, node, after):
        '''void QSGNode.insertChildNodeAfter(QSGNode node, QSGNode after)'''
    def insertChildNodeBefore(self, node, before):
        '''void QSGNode.insertChildNodeBefore(QSGNode node, QSGNode before)'''
    def appendChildNode(self, node):
        '''void QSGNode.appendChildNode(QSGNode node)'''
    def prependChildNode(self, node):
        '''void QSGNode.prependChildNode(QSGNode node)'''
    def removeAllChildNodes(self):
        '''void QSGNode.removeAllChildNodes()'''
    def removeChildNode(self, node):
        '''void QSGNode.removeChildNode(QSGNode node)'''
    def parent(self):
        '''QSGNode QSGNode.parent()'''
        return QSGNode()
    class Flags():
        """"""
        def __init__(self):
            '''QSGNode.Flags QSGNode.Flags.__init__()'''
            return QSGNode.Flags()
        def __init__(self):
            '''int QSGNode.Flags.__init__()'''
            return int()
        def __init__(self):
            '''void QSGNode.Flags.__init__()'''
        def __bool__(self):
            '''int QSGNode.Flags.__bool__()'''
            return int()
        def __ne__(self, f):
            '''bool QSGNode.Flags.__ne__(QSGNode.Flags f)'''
            return bool()
        def __eq__(self, f):
            '''bool QSGNode.Flags.__eq__(QSGNode.Flags f)'''
            return bool()
        def __invert__(self):
            '''QSGNode.Flags QSGNode.Flags.__invert__()'''
            return QSGNode.Flags()
        def __and__(self, mask):
            '''QSGNode.Flags QSGNode.Flags.__and__(int mask)'''
            return QSGNode.Flags()
        def __xor__(self, f):
            '''QSGNode.Flags QSGNode.Flags.__xor__(QSGNode.Flags f)'''
            return QSGNode.Flags()
        def __xor__(self, f):
            '''QSGNode.Flags QSGNode.Flags.__xor__(int f)'''
            return QSGNode.Flags()
        def __or__(self, f):
            '''QSGNode.Flags QSGNode.Flags.__or__(QSGNode.Flags f)'''
            return QSGNode.Flags()
        def __or__(self, f):
            '''QSGNode.Flags QSGNode.Flags.__or__(int f)'''
            return QSGNode.Flags()
        def __int__(self):
            '''int QSGNode.Flags.__int__()'''
            return int()
        def __ixor__(self, f):
            '''QSGNode.Flags QSGNode.Flags.__ixor__(QSGNode.Flags f)'''
            return QSGNode.Flags()
        def __ior__(self, f):
            '''QSGNode.Flags QSGNode.Flags.__ior__(QSGNode.Flags f)'''
            return QSGNode.Flags()
        def __iand__(self, mask):
            '''QSGNode.Flags QSGNode.Flags.__iand__(int mask)'''
            return QSGNode.Flags()
    class DirtyState():
        """"""
        def __init__(self):
            '''QSGNode.DirtyState QSGNode.DirtyState.__init__()'''
            return QSGNode.DirtyState()
        def __init__(self):
            '''int QSGNode.DirtyState.__init__()'''
            return int()
        def __init__(self):
            '''void QSGNode.DirtyState.__init__()'''
        def __bool__(self):
            '''int QSGNode.DirtyState.__bool__()'''
            return int()
        def __ne__(self, f):
            '''bool QSGNode.DirtyState.__ne__(QSGNode.DirtyState f)'''
            return bool()
        def __eq__(self, f):
            '''bool QSGNode.DirtyState.__eq__(QSGNode.DirtyState f)'''
            return bool()
        def __invert__(self):
            '''QSGNode.DirtyState QSGNode.DirtyState.__invert__()'''
            return QSGNode.DirtyState()
        def __and__(self, mask):
            '''QSGNode.DirtyState QSGNode.DirtyState.__and__(int mask)'''
            return QSGNode.DirtyState()
        def __xor__(self, f):
            '''QSGNode.DirtyState QSGNode.DirtyState.__xor__(QSGNode.DirtyState f)'''
            return QSGNode.DirtyState()
        def __xor__(self, f):
            '''QSGNode.DirtyState QSGNode.DirtyState.__xor__(int f)'''
            return QSGNode.DirtyState()
        def __or__(self, f):
            '''QSGNode.DirtyState QSGNode.DirtyState.__or__(QSGNode.DirtyState f)'''
            return QSGNode.DirtyState()
        def __or__(self, f):
            '''QSGNode.DirtyState QSGNode.DirtyState.__or__(int f)'''
            return QSGNode.DirtyState()
        def __int__(self):
            '''int QSGNode.DirtyState.__int__()'''
            return int()
        def __ixor__(self, f):
            '''QSGNode.DirtyState QSGNode.DirtyState.__ixor__(QSGNode.DirtyState f)'''
            return QSGNode.DirtyState()
        def __ior__(self, f):
            '''QSGNode.DirtyState QSGNode.DirtyState.__ior__(QSGNode.DirtyState f)'''
            return QSGNode.DirtyState()
        def __iand__(self, mask):
            '''QSGNode.DirtyState QSGNode.DirtyState.__iand__(int mask)'''
            return QSGNode.DirtyState()


class QSGBasicGeometryNode(QSGNode):
    """"""
    def geometry(self):
        '''QSGGeometry QSGBasicGeometryNode.geometry()'''
        return QSGGeometry()
    def setGeometry(self, geometry):
        '''void QSGBasicGeometryNode.setGeometry(QSGGeometry geometry)'''


class QSGGeometryNode(QSGBasicGeometryNode):
    """"""
    def __init__(self):
        '''void QSGGeometryNode.__init__()'''
    def opaqueMaterial(self):
        '''QSGMaterial QSGGeometryNode.opaqueMaterial()'''
        return QSGMaterial()
    def setOpaqueMaterial(self, material):
        '''void QSGGeometryNode.setOpaqueMaterial(QSGMaterial material)'''
    def material(self):
        '''QSGMaterial QSGGeometryNode.material()'''
        return QSGMaterial()
    def setMaterial(self, material):
        '''void QSGGeometryNode.setMaterial(QSGMaterial material)'''


class QSGClipNode(QSGBasicGeometryNode):
    """"""
    def __init__(self):
        '''void QSGClipNode.__init__()'''
    def clipRect(self):
        '''QRectF QSGClipNode.clipRect()'''
        return QRectF()
    def setClipRect(self):
        '''QRectF QSGClipNode.setClipRect()'''
        return QRectF()
    def isRectangular(self):
        '''bool QSGClipNode.isRectangular()'''
        return bool()
    def setIsRectangular(self, rectHint):
        '''void QSGClipNode.setIsRectangular(bool rectHint)'''


class QSGTransformNode(QSGNode):
    """"""
    def __init__(self):
        '''void QSGTransformNode.__init__()'''
    def matrix(self):
        '''QMatrix4x4 QSGTransformNode.matrix()'''
        return QMatrix4x4()
    def setMatrix(self, matrix):
        '''void QSGTransformNode.setMatrix(QMatrix4x4 matrix)'''


class QSGOpacityNode(QSGNode):
    """"""
    def __init__(self):
        '''void QSGOpacityNode.__init__()'''
    def opacity(self):
        '''float QSGOpacityNode.opacity()'''
        return float()
    def setOpacity(self, opacity):
        '''void QSGOpacityNode.setOpacity(float opacity)'''


class QSGSimpleRectNode(QSGGeometryNode):
    """"""
    def __init__(self, rect, color):
        '''void QSGSimpleRectNode.__init__(QRectF rect, QColor color)'''
    def __init__(self):
        '''void QSGSimpleRectNode.__init__()'''
    def color(self):
        '''QColor QSGSimpleRectNode.color()'''
        return QColor()
    def setColor(self, color):
        '''void QSGSimpleRectNode.setColor(QColor color)'''
    def rect(self):
        '''QRectF QSGSimpleRectNode.rect()'''
        return QRectF()
    def setRect(self, rect):
        '''void QSGSimpleRectNode.setRect(QRectF rect)'''
    def setRect(self, x, y, w, h):
        '''void QSGSimpleRectNode.setRect(float x, float y, float w, float h)'''


class QSGSimpleTextureNode(QSGGeometryNode):
    """"""
    # Enum QSGSimpleTextureNode.TextureCoordinatesTransformFlag
    NoTransform = 0
    MirrorHorizontally = 0
    MirrorVertically = 0

    def __init__(self):
        '''void QSGSimpleTextureNode.__init__()'''
    def sourceRect(self):
        '''QRectF QSGSimpleTextureNode.sourceRect()'''
        return QRectF()
    def setSourceRect(self, r):
        '''void QSGSimpleTextureNode.setSourceRect(QRectF r)'''
    def setSourceRect(self, x, y, w, h):
        '''void QSGSimpleTextureNode.setSourceRect(float x, float y, float w, float h)'''
    def ownsTexture(self):
        '''bool QSGSimpleTextureNode.ownsTexture()'''
        return bool()
    def setOwnsTexture(self, owns):
        '''void QSGSimpleTextureNode.setOwnsTexture(bool owns)'''
    def textureCoordinatesTransform(self):
        '''QSGSimpleTextureNode.TextureCoordinatesTransformMode QSGSimpleTextureNode.textureCoordinatesTransform()'''
        return QSGSimpleTextureNode.TextureCoordinatesTransformMode()
    def setTextureCoordinatesTransform(self, mode):
        '''void QSGSimpleTextureNode.setTextureCoordinatesTransform(QSGSimpleTextureNode.TextureCoordinatesTransformMode mode)'''
    def filtering(self):
        '''QSGTexture.Filtering QSGSimpleTextureNode.filtering()'''
        return QSGTexture.Filtering()
    def setFiltering(self, filtering):
        '''void QSGSimpleTextureNode.setFiltering(QSGTexture.Filtering filtering)'''
    def texture(self):
        '''QSGTexture QSGSimpleTextureNode.texture()'''
        return QSGTexture()
    def setTexture(self, texture):
        '''void QSGSimpleTextureNode.setTexture(QSGTexture texture)'''
    def rect(self):
        '''QRectF QSGSimpleTextureNode.rect()'''
        return QRectF()
    def setRect(self, rect):
        '''void QSGSimpleTextureNode.setRect(QRectF rect)'''
    def setRect(self, x, y, w, h):
        '''void QSGSimpleTextureNode.setRect(float x, float y, float w, float h)'''
    class TextureCoordinatesTransformMode():
        """"""
        def __init__(self):
            '''QSGSimpleTextureNode.TextureCoordinatesTransformMode QSGSimpleTextureNode.TextureCoordinatesTransformMode.__init__()'''
            return QSGSimpleTextureNode.TextureCoordinatesTransformMode()
        def __init__(self):
            '''int QSGSimpleTextureNode.TextureCoordinatesTransformMode.__init__()'''
            return int()
        def __init__(self):
            '''void QSGSimpleTextureNode.TextureCoordinatesTransformMode.__init__()'''
        def __bool__(self):
            '''int QSGSimpleTextureNode.TextureCoordinatesTransformMode.__bool__()'''
            return int()
        def __ne__(self, f):
            '''bool QSGSimpleTextureNode.TextureCoordinatesTransformMode.__ne__(QSGSimpleTextureNode.TextureCoordinatesTransformMode f)'''
            return bool()
        def __eq__(self, f):
            '''bool QSGSimpleTextureNode.TextureCoordinatesTransformMode.__eq__(QSGSimpleTextureNode.TextureCoordinatesTransformMode f)'''
            return bool()
        def __invert__(self):
            '''QSGSimpleTextureNode.TextureCoordinatesTransformMode QSGSimpleTextureNode.TextureCoordinatesTransformMode.__invert__()'''
            return QSGSimpleTextureNode.TextureCoordinatesTransformMode()
        def __and__(self, mask):
            '''QSGSimpleTextureNode.TextureCoordinatesTransformMode QSGSimpleTextureNode.TextureCoordinatesTransformMode.__and__(int mask)'''
            return QSGSimpleTextureNode.TextureCoordinatesTransformMode()
        def __xor__(self, f):
            '''QSGSimpleTextureNode.TextureCoordinatesTransformMode QSGSimpleTextureNode.TextureCoordinatesTransformMode.__xor__(QSGSimpleTextureNode.TextureCoordinatesTransformMode f)'''
            return QSGSimpleTextureNode.TextureCoordinatesTransformMode()
        def __xor__(self, f):
            '''QSGSimpleTextureNode.TextureCoordinatesTransformMode QSGSimpleTextureNode.TextureCoordinatesTransformMode.__xor__(int f)'''
            return QSGSimpleTextureNode.TextureCoordinatesTransformMode()
        def __or__(self, f):
            '''QSGSimpleTextureNode.TextureCoordinatesTransformMode QSGSimpleTextureNode.TextureCoordinatesTransformMode.__or__(QSGSimpleTextureNode.TextureCoordinatesTransformMode f)'''
            return QSGSimpleTextureNode.TextureCoordinatesTransformMode()
        def __or__(self, f):
            '''QSGSimpleTextureNode.TextureCoordinatesTransformMode QSGSimpleTextureNode.TextureCoordinatesTransformMode.__or__(int f)'''
            return QSGSimpleTextureNode.TextureCoordinatesTransformMode()
        def __int__(self):
            '''int QSGSimpleTextureNode.TextureCoordinatesTransformMode.__int__()'''
            return int()
        def __ixor__(self, f):
            '''QSGSimpleTextureNode.TextureCoordinatesTransformMode QSGSimpleTextureNode.TextureCoordinatesTransformMode.__ixor__(QSGSimpleTextureNode.TextureCoordinatesTransformMode f)'''
            return QSGSimpleTextureNode.TextureCoordinatesTransformMode()
        def __ior__(self, f):
            '''QSGSimpleTextureNode.TextureCoordinatesTransformMode QSGSimpleTextureNode.TextureCoordinatesTransformMode.__ior__(QSGSimpleTextureNode.TextureCoordinatesTransformMode f)'''
            return QSGSimpleTextureNode.TextureCoordinatesTransformMode()
        def __iand__(self, mask):
            '''QSGSimpleTextureNode.TextureCoordinatesTransformMode QSGSimpleTextureNode.TextureCoordinatesTransformMode.__iand__(int mask)'''
            return QSGSimpleTextureNode.TextureCoordinatesTransformMode()


class QSGTexture(QObject):
    """"""
    # Enum QSGTexture.Filtering
    __kdevpythondocumentation_builtin_None = 0
    Nearest = 0
    Linear = 0

    # Enum QSGTexture.WrapMode
    Repeat = 0
    ClampToEdge = 0

    def __init__(self):
        '''void QSGTexture.__init__()'''
    def convertToNormalizedSourceRect(self, rect):
        '''QRectF QSGTexture.convertToNormalizedSourceRect(QRectF rect)'''
        return QRectF()
    def verticalWrapMode(self):
        '''QSGTexture.WrapMode QSGTexture.verticalWrapMode()'''
        return QSGTexture.WrapMode()
    def setVerticalWrapMode(self, vwrap):
        '''void QSGTexture.setVerticalWrapMode(QSGTexture.WrapMode vwrap)'''
    def horizontalWrapMode(self):
        '''QSGTexture.WrapMode QSGTexture.horizontalWrapMode()'''
        return QSGTexture.WrapMode()
    def setHorizontalWrapMode(self, hwrap):
        '''void QSGTexture.setHorizontalWrapMode(QSGTexture.WrapMode hwrap)'''
    def filtering(self):
        '''QSGTexture.Filtering QSGTexture.filtering()'''
        return QSGTexture.Filtering()
    def setFiltering(self, filter):
        '''void QSGTexture.setFiltering(QSGTexture.Filtering filter)'''
    def mipmapFiltering(self):
        '''QSGTexture.Filtering QSGTexture.mipmapFiltering()'''
        return QSGTexture.Filtering()
    def setMipmapFiltering(self, filter):
        '''void QSGTexture.setMipmapFiltering(QSGTexture.Filtering filter)'''
    def updateBindOptions(self, force = False):
        '''void QSGTexture.updateBindOptions(bool force = False)'''
    def bind(self):
        '''abstract void QSGTexture.bind()'''
    def removedFromAtlas(self):
        '''QSGTexture QSGTexture.removedFromAtlas()'''
        return QSGTexture()
    def isAtlasTexture(self):
        '''bool QSGTexture.isAtlasTexture()'''
        return bool()
    def normalizedTextureSubRect(self):
        '''QRectF QSGTexture.normalizedTextureSubRect()'''
        return QRectF()
    def hasMipmaps(self):
        '''abstract bool QSGTexture.hasMipmaps()'''
        return bool()
    def hasAlphaChannel(self):
        '''abstract bool QSGTexture.hasAlphaChannel()'''
        return bool()
    def textureSize(self):
        '''abstract QSize QSGTexture.textureSize()'''
        return QSize()
    def textureId(self):
        '''abstract int QSGTexture.textureId()'''
        return int()


class QSGDynamicTexture(QSGTexture):
    """"""
    def __init__(self):
        '''void QSGDynamicTexture.__init__()'''
    def updateTexture(self):
        '''abstract bool QSGDynamicTexture.updateTexture()'''
        return bool()


class QSGOpaqueTextureMaterial(QSGMaterial):
    """"""
    def __init__(self):
        '''void QSGOpaqueTextureMaterial.__init__()'''
    def verticalWrapMode(self):
        '''QSGTexture.WrapMode QSGOpaqueTextureMaterial.verticalWrapMode()'''
        return QSGTexture.WrapMode()
    def setVerticalWrapMode(self, mode):
        '''void QSGOpaqueTextureMaterial.setVerticalWrapMode(QSGTexture.WrapMode mode)'''
    def horizontalWrapMode(self):
        '''QSGTexture.WrapMode QSGOpaqueTextureMaterial.horizontalWrapMode()'''
        return QSGTexture.WrapMode()
    def setHorizontalWrapMode(self, mode):
        '''void QSGOpaqueTextureMaterial.setHorizontalWrapMode(QSGTexture.WrapMode mode)'''
    def filtering(self):
        '''QSGTexture.Filtering QSGOpaqueTextureMaterial.filtering()'''
        return QSGTexture.Filtering()
    def setFiltering(self, filtering):
        '''void QSGOpaqueTextureMaterial.setFiltering(QSGTexture.Filtering filtering)'''
    def mipmapFiltering(self):
        '''QSGTexture.Filtering QSGOpaqueTextureMaterial.mipmapFiltering()'''
        return QSGTexture.Filtering()
    def setMipmapFiltering(self, filtering):
        '''void QSGOpaqueTextureMaterial.setMipmapFiltering(QSGTexture.Filtering filtering)'''
    def texture(self):
        '''QSGTexture QSGOpaqueTextureMaterial.texture()'''
        return QSGTexture()
    def setTexture(self, texture):
        '''void QSGOpaqueTextureMaterial.setTexture(QSGTexture texture)'''
    def compare(self, other):
        '''int QSGOpaqueTextureMaterial.compare(QSGMaterial other)'''
        return int()
    def createShader(self):
        '''QSGMaterialShader QSGOpaqueTextureMaterial.createShader()'''
        return QSGMaterialShader()
    def type(self):
        '''QSGMaterialType QSGOpaqueTextureMaterial.type()'''
        return QSGMaterialType()


class QSGTextureMaterial(QSGOpaqueTextureMaterial):
    """"""
    def __init__(self):
        '''void QSGTextureMaterial.__init__()'''
    def createShader(self):
        '''QSGMaterialShader QSGTextureMaterial.createShader()'''
        return QSGMaterialShader()
    def type(self):
        '''QSGMaterialType QSGTextureMaterial.type()'''
        return QSGMaterialType()


class QSGTextureProvider(QObject):
    """"""
    def __init__(self):
        '''void QSGTextureProvider.__init__()'''
    textureChanged = pyqtSignal() # void textureChanged() - signal
    def texture(self):
        '''abstract QSGTexture QSGTextureProvider.texture()'''
        return QSGTexture()


class QSGVertexColorMaterial(QSGMaterial):
    """"""
    def __init__(self):
        '''void QSGVertexColorMaterial.__init__()'''
    def createShader(self):
        '''QSGMaterialShader QSGVertexColorMaterial.createShader()'''
        return QSGMaterialShader()
    def type(self):
        '''QSGMaterialType QSGVertexColorMaterial.type()'''
        return QSGMaterialType()
    def compare(self, other):
        '''int QSGVertexColorMaterial.compare(QSGMaterial other)'''
        return int()


