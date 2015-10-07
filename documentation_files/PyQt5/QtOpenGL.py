class pyqtSignal():
 def connect(self, targetSignal): pass
 def emit(self, *args): pass
from QtCore import *

from QtWidgets import *

import datetime

class QGL():
    """"""
    # Enum QGL.FormatOption
    DoubleBuffer = 0
    DepthBuffer = 0
    Rgba = 0
    AlphaChannel = 0
    AccumBuffer = 0
    StencilBuffer = 0
    StereoBuffers = 0
    DirectRendering = 0
    HasOverlay = 0
    SampleBuffers = 0
    SingleBuffer = 0
    NoDepthBuffer = 0
    ColorIndex = 0
    NoAlphaChannel = 0
    NoAccumBuffer = 0
    NoStencilBuffer = 0
    NoStereoBuffers = 0
    IndirectRendering = 0
    NoOverlay = 0
    NoSampleBuffers = 0
    DeprecatedFunctions = 0
    NoDeprecatedFunctions = 0

    class FormatOptions():
        """"""
        def __init__(self):
            '''QGL.FormatOptions QGL.FormatOptions.__init__()'''
            return QGL.FormatOptions()
        def __init__(self):
            '''int QGL.FormatOptions.__init__()'''
            return int()
        def __init__(self):
            '''void QGL.FormatOptions.__init__()'''
        def __bool__(self):
            '''int QGL.FormatOptions.__bool__()'''
            return int()
        def __ne__(self, f):
            '''bool QGL.FormatOptions.__ne__(QGL.FormatOptions f)'''
            return bool()
        def __eq__(self, f):
            '''bool QGL.FormatOptions.__eq__(QGL.FormatOptions f)'''
            return bool()
        def __invert__(self):
            '''QGL.FormatOptions QGL.FormatOptions.__invert__()'''
            return QGL.FormatOptions()
        def __and__(self, mask):
            '''QGL.FormatOptions QGL.FormatOptions.__and__(int mask)'''
            return QGL.FormatOptions()
        def __xor__(self, f):
            '''QGL.FormatOptions QGL.FormatOptions.__xor__(QGL.FormatOptions f)'''
            return QGL.FormatOptions()
        def __xor__(self, f):
            '''QGL.FormatOptions QGL.FormatOptions.__xor__(int f)'''
            return QGL.FormatOptions()
        def __or__(self, f):
            '''QGL.FormatOptions QGL.FormatOptions.__or__(QGL.FormatOptions f)'''
            return QGL.FormatOptions()
        def __or__(self, f):
            '''QGL.FormatOptions QGL.FormatOptions.__or__(int f)'''
            return QGL.FormatOptions()
        def __int__(self):
            '''int QGL.FormatOptions.__int__()'''
            return int()
        def __ixor__(self, f):
            '''QGL.FormatOptions QGL.FormatOptions.__ixor__(QGL.FormatOptions f)'''
            return QGL.FormatOptions()
        def __ior__(self, f):
            '''QGL.FormatOptions QGL.FormatOptions.__ior__(QGL.FormatOptions f)'''
            return QGL.FormatOptions()
        def __iand__(self, mask):
            '''QGL.FormatOptions QGL.FormatOptions.__iand__(int mask)'''
            return QGL.FormatOptions()


class QGLFormat():
    """"""
    # Enum QGLFormat.OpenGLContextProfile
    NoProfile = 0
    CoreProfile = 0
    CompatibilityProfile = 0

    # Enum QGLFormat.OpenGLVersionFlag
    OpenGL_Version_None = 0
    OpenGL_Version_1_1 = 0
    OpenGL_Version_1_2 = 0
    OpenGL_Version_1_3 = 0
    OpenGL_Version_1_4 = 0
    OpenGL_Version_1_5 = 0
    OpenGL_Version_2_0 = 0
    OpenGL_Version_2_1 = 0
    OpenGL_Version_3_0 = 0
    OpenGL_Version_3_1 = 0
    OpenGL_Version_3_2 = 0
    OpenGL_Version_3_3 = 0
    OpenGL_Version_4_0 = 0
    OpenGL_Version_4_1 = 0
    OpenGL_Version_4_2 = 0
    OpenGL_Version_4_3 = 0
    OpenGL_ES_Common_Version_1_0 = 0
    OpenGL_ES_CommonLite_Version_1_0 = 0
    OpenGL_ES_Common_Version_1_1 = 0
    OpenGL_ES_CommonLite_Version_1_1 = 0
    OpenGL_ES_Version_2_0 = 0

    def __init__(self):
        '''void QGLFormat.__init__()'''
    def __init__(self, options, plane = 0):
        '''void QGLFormat.__init__(QGL.FormatOptions options, int plane = 0)'''
    def __init__(self, other):
        '''void QGLFormat.__init__(QGLFormat other)'''
    def __eq__(self):
        '''QGLFormat QGLFormat.__eq__()'''
        return QGLFormat()
    def __ne__(self):
        '''QGLFormat QGLFormat.__ne__()'''
        return QGLFormat()
    def profile(self):
        '''QGLFormat.OpenGLContextProfile QGLFormat.profile()'''
        return QGLFormat.OpenGLContextProfile()
    def setProfile(self, profile):
        '''void QGLFormat.setProfile(QGLFormat.OpenGLContextProfile profile)'''
    def minorVersion(self):
        '''int QGLFormat.minorVersion()'''
        return int()
    def majorVersion(self):
        '''int QGLFormat.majorVersion()'''
        return int()
    def setVersion(self, major, minor):
        '''void QGLFormat.setVersion(int major, int minor)'''
    def openGLVersionFlags(self):
        '''static QGLFormat.OpenGLVersionFlags QGLFormat.openGLVersionFlags()'''
        return QGLFormat.OpenGLVersionFlags()
    def swapInterval(self):
        '''int QGLFormat.swapInterval()'''
        return int()
    def setSwapInterval(self, interval):
        '''void QGLFormat.setSwapInterval(int interval)'''
    def blueBufferSize(self):
        '''int QGLFormat.blueBufferSize()'''
        return int()
    def setBlueBufferSize(self, size):
        '''void QGLFormat.setBlueBufferSize(int size)'''
    def greenBufferSize(self):
        '''int QGLFormat.greenBufferSize()'''
        return int()
    def setGreenBufferSize(self, size):
        '''void QGLFormat.setGreenBufferSize(int size)'''
    def redBufferSize(self):
        '''int QGLFormat.redBufferSize()'''
        return int()
    def setRedBufferSize(self, size):
        '''void QGLFormat.setRedBufferSize(int size)'''
    def sampleBuffers(self):
        '''bool QGLFormat.sampleBuffers()'''
        return bool()
    def hasOverlay(self):
        '''bool QGLFormat.hasOverlay()'''
        return bool()
    def directRendering(self):
        '''bool QGLFormat.directRendering()'''
        return bool()
    def stereo(self):
        '''bool QGLFormat.stereo()'''
        return bool()
    def stencil(self):
        '''bool QGLFormat.stencil()'''
        return bool()
    def accum(self):
        '''bool QGLFormat.accum()'''
        return bool()
    def alpha(self):
        '''bool QGLFormat.alpha()'''
        return bool()
    def rgba(self):
        '''bool QGLFormat.rgba()'''
        return bool()
    def depth(self):
        '''bool QGLFormat.depth()'''
        return bool()
    def doubleBuffer(self):
        '''bool QGLFormat.doubleBuffer()'''
        return bool()
    def hasOpenGLOverlays(self):
        '''static bool QGLFormat.hasOpenGLOverlays()'''
        return bool()
    def hasOpenGL(self):
        '''static bool QGLFormat.hasOpenGL()'''
        return bool()
    def setDefaultOverlayFormat(self, f):
        '''static void QGLFormat.setDefaultOverlayFormat(QGLFormat f)'''
    def defaultOverlayFormat(self):
        '''static QGLFormat QGLFormat.defaultOverlayFormat()'''
        return QGLFormat()
    def setDefaultFormat(self, f):
        '''static void QGLFormat.setDefaultFormat(QGLFormat f)'''
    def defaultFormat(self):
        '''static QGLFormat QGLFormat.defaultFormat()'''
        return QGLFormat()
    def testOption(self, opt):
        '''bool QGLFormat.testOption(QGL.FormatOptions opt)'''
        return bool()
    def setOption(self, opt):
        '''void QGLFormat.setOption(QGL.FormatOptions opt)'''
    def setPlane(self, plane):
        '''void QGLFormat.setPlane(int plane)'''
    def plane(self):
        '''int QGLFormat.plane()'''
        return int()
    def setOverlay(self, enable):
        '''void QGLFormat.setOverlay(bool enable)'''
    def setDirectRendering(self, enable):
        '''void QGLFormat.setDirectRendering(bool enable)'''
    def setStereo(self, enable):
        '''void QGLFormat.setStereo(bool enable)'''
    def setStencil(self, enable):
        '''void QGLFormat.setStencil(bool enable)'''
    def setAccum(self, enable):
        '''void QGLFormat.setAccum(bool enable)'''
    def setAlpha(self, enable):
        '''void QGLFormat.setAlpha(bool enable)'''
    def setRgba(self, enable):
        '''void QGLFormat.setRgba(bool enable)'''
    def setDepth(self, enable):
        '''void QGLFormat.setDepth(bool enable)'''
    def setDoubleBuffer(self, enable):
        '''void QGLFormat.setDoubleBuffer(bool enable)'''
    def samples(self):
        '''int QGLFormat.samples()'''
        return int()
    def setSamples(self, numSamples):
        '''void QGLFormat.setSamples(int numSamples)'''
    def setSampleBuffers(self, enable):
        '''void QGLFormat.setSampleBuffers(bool enable)'''
    def stencilBufferSize(self):
        '''int QGLFormat.stencilBufferSize()'''
        return int()
    def setStencilBufferSize(self, size):
        '''void QGLFormat.setStencilBufferSize(int size)'''
    def alphaBufferSize(self):
        '''int QGLFormat.alphaBufferSize()'''
        return int()
    def setAlphaBufferSize(self, size):
        '''void QGLFormat.setAlphaBufferSize(int size)'''
    def accumBufferSize(self):
        '''int QGLFormat.accumBufferSize()'''
        return int()
    def setAccumBufferSize(self, size):
        '''void QGLFormat.setAccumBufferSize(int size)'''
    def depthBufferSize(self):
        '''int QGLFormat.depthBufferSize()'''
        return int()
    def setDepthBufferSize(self, size):
        '''void QGLFormat.setDepthBufferSize(int size)'''
    class OpenGLVersionFlags():
        """"""
        def __init__(self):
            '''QGLFormat.OpenGLVersionFlags QGLFormat.OpenGLVersionFlags.__init__()'''
            return QGLFormat.OpenGLVersionFlags()
        def __init__(self):
            '''int QGLFormat.OpenGLVersionFlags.__init__()'''
            return int()
        def __init__(self):
            '''void QGLFormat.OpenGLVersionFlags.__init__()'''
        def __bool__(self):
            '''int QGLFormat.OpenGLVersionFlags.__bool__()'''
            return int()
        def __ne__(self, f):
            '''bool QGLFormat.OpenGLVersionFlags.__ne__(QGLFormat.OpenGLVersionFlags f)'''
            return bool()
        def __eq__(self, f):
            '''bool QGLFormat.OpenGLVersionFlags.__eq__(QGLFormat.OpenGLVersionFlags f)'''
            return bool()
        def __invert__(self):
            '''QGLFormat.OpenGLVersionFlags QGLFormat.OpenGLVersionFlags.__invert__()'''
            return QGLFormat.OpenGLVersionFlags()
        def __and__(self, mask):
            '''QGLFormat.OpenGLVersionFlags QGLFormat.OpenGLVersionFlags.__and__(int mask)'''
            return QGLFormat.OpenGLVersionFlags()
        def __xor__(self, f):
            '''QGLFormat.OpenGLVersionFlags QGLFormat.OpenGLVersionFlags.__xor__(QGLFormat.OpenGLVersionFlags f)'''
            return QGLFormat.OpenGLVersionFlags()
        def __xor__(self, f):
            '''QGLFormat.OpenGLVersionFlags QGLFormat.OpenGLVersionFlags.__xor__(int f)'''
            return QGLFormat.OpenGLVersionFlags()
        def __or__(self, f):
            '''QGLFormat.OpenGLVersionFlags QGLFormat.OpenGLVersionFlags.__or__(QGLFormat.OpenGLVersionFlags f)'''
            return QGLFormat.OpenGLVersionFlags()
        def __or__(self, f):
            '''QGLFormat.OpenGLVersionFlags QGLFormat.OpenGLVersionFlags.__or__(int f)'''
            return QGLFormat.OpenGLVersionFlags()
        def __int__(self):
            '''int QGLFormat.OpenGLVersionFlags.__int__()'''
            return int()
        def __ixor__(self, f):
            '''QGLFormat.OpenGLVersionFlags QGLFormat.OpenGLVersionFlags.__ixor__(QGLFormat.OpenGLVersionFlags f)'''
            return QGLFormat.OpenGLVersionFlags()
        def __ior__(self, f):
            '''QGLFormat.OpenGLVersionFlags QGLFormat.OpenGLVersionFlags.__ior__(QGLFormat.OpenGLVersionFlags f)'''
            return QGLFormat.OpenGLVersionFlags()
        def __iand__(self, mask):
            '''QGLFormat.OpenGLVersionFlags QGLFormat.OpenGLVersionFlags.__iand__(int mask)'''
            return QGLFormat.OpenGLVersionFlags()


class QGLContext():
    """"""
    # Enum QGLContext.BindOption
    NoBindOption = 0
    InvertedYBindOption = 0
    MipmapBindOption = 0
    PremultipliedAlphaBindOption = 0
    LinearFilteringBindOption = 0
    DefaultBindOption = 0

    def __init__(self, format):
        '''void QGLContext.__init__(QGLFormat format)'''
    def moveToThread(self, thread):
        '''void QGLContext.moveToThread(QThread thread)'''
    def areSharing(self, context1, context2):
        '''static bool QGLContext.areSharing(QGLContext context1, QGLContext context2)'''
        return bool()
    def setInitialized(self, on):
        '''void QGLContext.setInitialized(bool on)'''
    def initialized(self):
        '''bool QGLContext.initialized()'''
        return bool()
    def setWindowCreated(self, on):
        '''void QGLContext.setWindowCreated(bool on)'''
    def windowCreated(self):
        '''bool QGLContext.windowCreated()'''
        return bool()
    def deviceIsPixmap(self):
        '''bool QGLContext.deviceIsPixmap()'''
        return bool()
    def chooseContext(self, shareContext = None):
        '''bool QGLContext.chooseContext(QGLContext shareContext = None)'''
        return bool()
    def currentContext(self):
        '''static QGLContext QGLContext.currentContext()'''
        return QGLContext()
    def overlayTransparentColor(self):
        '''QColor QGLContext.overlayTransparentColor()'''
        return QColor()
    def device(self):
        '''QPaintDevice QGLContext.device()'''
        return QPaintDevice()
    def getProcAddress(self, proc):
        '''sip.voidptr QGLContext.getProcAddress(str proc)'''
        return sip.voidptr()
    def textureCacheLimit(self):
        '''static int QGLContext.textureCacheLimit()'''
        return int()
    def setTextureCacheLimit(self, size):
        '''static void QGLContext.setTextureCacheLimit(int size)'''
    def deleteTexture(self, tx_id):
        '''void QGLContext.deleteTexture(int tx_id)'''
    def drawTexture(self, target, textureId, textureTarget = None):
        '''void QGLContext.drawTexture(QRectF target, int textureId, int textureTarget = GL_TEXTURE_2D)'''
    def drawTexture(self, point, textureId, textureTarget = None):
        '''void QGLContext.drawTexture(QPointF point, int textureId, int textureTarget = GL_TEXTURE_2D)'''
    def bindTexture(self, image, target = None, format = None):
        '''int QGLContext.bindTexture(QImage image, int target = GL_TEXTURE_2D, int format = GL_RGBA)'''
        return int()
    def bindTexture(self, pixmap, target = None, format = None):
        '''int QGLContext.bindTexture(QPixmap pixmap, int target = GL_TEXTURE_2D, int format = GL_RGBA)'''
        return int()
    def bindTexture(self, fileName):
        '''int QGLContext.bindTexture(str fileName)'''
        return int()
    def bindTexture(self, image, target, format, options):
        '''int QGLContext.bindTexture(QImage image, int target, int format, QGLContext.BindOptions options)'''
        return int()
    def bindTexture(self, pixmap, target, format, options):
        '''int QGLContext.bindTexture(QPixmap pixmap, int target, int format, QGLContext.BindOptions options)'''
        return int()
    def swapBuffers(self):
        '''void QGLContext.swapBuffers()'''
    def doneCurrent(self):
        '''void QGLContext.doneCurrent()'''
    def makeCurrent(self):
        '''void QGLContext.makeCurrent()'''
    def setFormat(self, format):
        '''void QGLContext.setFormat(QGLFormat format)'''
    def requestedFormat(self):
        '''QGLFormat QGLContext.requestedFormat()'''
        return QGLFormat()
    def format(self):
        '''QGLFormat QGLContext.format()'''
        return QGLFormat()
    def reset(self):
        '''void QGLContext.reset()'''
    def isSharing(self):
        '''bool QGLContext.isSharing()'''
        return bool()
    def isValid(self):
        '''bool QGLContext.isValid()'''
        return bool()
    def create(self, shareContext = None):
        '''bool QGLContext.create(QGLContext shareContext = None)'''
        return bool()
    class BindOptions():
        """"""
        def __init__(self):
            '''QGLContext.BindOptions QGLContext.BindOptions.__init__()'''
            return QGLContext.BindOptions()
        def __init__(self):
            '''int QGLContext.BindOptions.__init__()'''
            return int()
        def __init__(self):
            '''void QGLContext.BindOptions.__init__()'''
        def __bool__(self):
            '''int QGLContext.BindOptions.__bool__()'''
            return int()
        def __ne__(self, f):
            '''bool QGLContext.BindOptions.__ne__(QGLContext.BindOptions f)'''
            return bool()
        def __eq__(self, f):
            '''bool QGLContext.BindOptions.__eq__(QGLContext.BindOptions f)'''
            return bool()
        def __invert__(self):
            '''QGLContext.BindOptions QGLContext.BindOptions.__invert__()'''
            return QGLContext.BindOptions()
        def __and__(self, mask):
            '''QGLContext.BindOptions QGLContext.BindOptions.__and__(int mask)'''
            return QGLContext.BindOptions()
        def __xor__(self, f):
            '''QGLContext.BindOptions QGLContext.BindOptions.__xor__(QGLContext.BindOptions f)'''
            return QGLContext.BindOptions()
        def __xor__(self, f):
            '''QGLContext.BindOptions QGLContext.BindOptions.__xor__(int f)'''
            return QGLContext.BindOptions()
        def __or__(self, f):
            '''QGLContext.BindOptions QGLContext.BindOptions.__or__(QGLContext.BindOptions f)'''
            return QGLContext.BindOptions()
        def __or__(self, f):
            '''QGLContext.BindOptions QGLContext.BindOptions.__or__(int f)'''
            return QGLContext.BindOptions()
        def __int__(self):
            '''int QGLContext.BindOptions.__int__()'''
            return int()
        def __ixor__(self, f):
            '''QGLContext.BindOptions QGLContext.BindOptions.__ixor__(QGLContext.BindOptions f)'''
            return QGLContext.BindOptions()
        def __ior__(self, f):
            '''QGLContext.BindOptions QGLContext.BindOptions.__ior__(QGLContext.BindOptions f)'''
            return QGLContext.BindOptions()
        def __iand__(self, mask):
            '''QGLContext.BindOptions QGLContext.BindOptions.__iand__(int mask)'''
            return QGLContext.BindOptions()


class QGLWidget(QWidget):
    """"""
    def __init__(self, parent = None, shareWidget = None, flags = 0):
        '''void QGLWidget.__init__(QWidget parent = None, QGLWidget shareWidget = None, Qt.WindowFlags flags = 0)'''
    def __init__(self, context, parent = None, shareWidget = None, flags = 0):
        '''void QGLWidget.__init__(QGLContext context, QWidget parent = None, QGLWidget shareWidget = None, Qt.WindowFlags flags = 0)'''
    def __init__(self, format, parent = None, shareWidget = None, flags = 0):
        '''void QGLWidget.__init__(QGLFormat format, QWidget parent = None, QGLWidget shareWidget = None, Qt.WindowFlags flags = 0)'''
    def glDraw(self):
        '''void QGLWidget.glDraw()'''
    def glInit(self):
        '''void QGLWidget.glInit()'''
    def resizeEvent(self):
        '''QResizeEvent QGLWidget.resizeEvent()'''
        return QResizeEvent()
    def paintEvent(self):
        '''QPaintEvent QGLWidget.paintEvent()'''
        return QPaintEvent()
    def autoBufferSwap(self):
        '''bool QGLWidget.autoBufferSwap()'''
        return bool()
    def setAutoBufferSwap(self, on):
        '''void QGLWidget.setAutoBufferSwap(bool on)'''
    def paintOverlayGL(self):
        '''void QGLWidget.paintOverlayGL()'''
    def resizeOverlayGL(self, w, h):
        '''void QGLWidget.resizeOverlayGL(int w, int h)'''
    def initializeOverlayGL(self):
        '''void QGLWidget.initializeOverlayGL()'''
    def paintGL(self):
        '''void QGLWidget.paintGL()'''
    def resizeGL(self, w, h):
        '''void QGLWidget.resizeGL(int w, int h)'''
    def initializeGL(self):
        '''void QGLWidget.initializeGL()'''
    def event(self):
        '''QEvent QGLWidget.event()'''
        return QEvent()
    def updateOverlayGL(self):
        '''void QGLWidget.updateOverlayGL()'''
    def updateGL(self):
        '''void QGLWidget.updateGL()'''
    def deleteTexture(self, tx_id):
        '''void QGLWidget.deleteTexture(int tx_id)'''
    def drawTexture(self, target, textureId, textureTarget = None):
        '''void QGLWidget.drawTexture(QRectF target, int textureId, int textureTarget = GL_TEXTURE_2D)'''
    def drawTexture(self, point, textureId, textureTarget = None):
        '''void QGLWidget.drawTexture(QPointF point, int textureId, int textureTarget = GL_TEXTURE_2D)'''
    def bindTexture(self, image, target = None, format = None):
        '''int QGLWidget.bindTexture(QImage image, int target = GL_TEXTURE_2D, int format = GL_RGBA)'''
        return int()
    def bindTexture(self, pixmap, target = None, format = None):
        '''int QGLWidget.bindTexture(QPixmap pixmap, int target = GL_TEXTURE_2D, int format = GL_RGBA)'''
        return int()
    def bindTexture(self, fileName):
        '''int QGLWidget.bindTexture(str fileName)'''
        return int()
    def bindTexture(self, image, target, format, options):
        '''int QGLWidget.bindTexture(QImage image, int target, int format, QGLContext.BindOptions options)'''
        return int()
    def bindTexture(self, pixmap, target, format, options):
        '''int QGLWidget.bindTexture(QPixmap pixmap, int target, int format, QGLContext.BindOptions options)'''
        return int()
    def paintEngine(self):
        '''QPaintEngine QGLWidget.paintEngine()'''
        return QPaintEngine()
    def renderText(self, x, y, str, font = QFont()):
        '''void QGLWidget.renderText(int x, int y, str str, QFont font = QFont())'''
    def renderText(self, x, y, z, str, font = QFont()):
        '''void QGLWidget.renderText(float x, float y, float z, str str, QFont font = QFont())'''
    def convertToGLFormat(self, img):
        '''static QImage QGLWidget.convertToGLFormat(QImage img)'''
        return QImage()
    def overlayContext(self):
        '''QGLContext QGLWidget.overlayContext()'''
        return QGLContext()
    def makeOverlayCurrent(self):
        '''void QGLWidget.makeOverlayCurrent()'''
    def grabFrameBuffer(self, withAlpha = False):
        '''QImage QGLWidget.grabFrameBuffer(bool withAlpha = False)'''
        return QImage()
    def renderPixmap(self, width = 0, height = 0, useContext = False):
        '''QPixmap QGLWidget.renderPixmap(int width = 0, int height = 0, bool useContext = False)'''
        return QPixmap()
    def setContext(self, context, shareContext = None, deleteOldContext = True):
        '''void QGLWidget.setContext(QGLContext context, QGLContext shareContext = None, bool deleteOldContext = True)'''
    def context(self):
        '''QGLContext QGLWidget.context()'''
        return QGLContext()
    def format(self):
        '''QGLFormat QGLWidget.format()'''
        return QGLFormat()
    def swapBuffers(self):
        '''void QGLWidget.swapBuffers()'''
    def doubleBuffer(self):
        '''bool QGLWidget.doubleBuffer()'''
        return bool()
    def doneCurrent(self):
        '''void QGLWidget.doneCurrent()'''
    def makeCurrent(self):
        '''void QGLWidget.makeCurrent()'''
    def isSharing(self):
        '''bool QGLWidget.isSharing()'''
        return bool()
    def isValid(self):
        '''bool QGLWidget.isValid()'''
        return bool()
    def qglClearColor(self, c):
        '''void QGLWidget.qglClearColor(QColor c)'''
    def qglColor(self, c):
        '''void QGLWidget.qglColor(QColor c)'''


