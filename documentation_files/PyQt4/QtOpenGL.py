class pyqtSignal():
 def connect(self, targetSignal): pass
 def emit(self, *args): pass
from QtCore import *

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

    def setPreferredPaintEngine(self, engineType):
        '''static void QGL.setPreferredPaintEngine(QPaintEngine.Type engineType)'''
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

    def __init__(self, format, device):
        '''void QGLContext.__init__(QGLFormat format, QPaintDevice device)'''
    def areSharing(self, context1, context2):
        '''static bool QGLContext.areSharing(QGLContext context1, QGLContext context2)'''
        return bool()
    def generateFontDisplayLists(self, fnt, listBase):
        '''void QGLContext.generateFontDisplayLists(QFont fnt, int listBase)'''
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
        '''sip.voidptr QGLContext.getProcAddress(QString proc)'''
        return sip.voidptr()
    def textureCacheLimit(self):
        '''static int QGLContext.textureCacheLimit()'''
        return int()
    def setTextureCacheLimit(self, size):
        '''static void QGLContext.setTextureCacheLimit(int size)'''
    def deleteTexture(self, tx_id):
        '''void QGLContext.deleteTexture(int tx_id)'''
    def chooseVisual(self):
        '''sip.voidptr QGLContext.chooseVisual()'''
        return sip.voidptr()
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
        '''int QGLContext.bindTexture(QString fileName)'''
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
    def fontDisplayListBase(self, font, listBase = 2000):
        '''int QGLWidget.fontDisplayListBase(QFont font, int listBase = 2000)'''
        return int()
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
        '''int QGLWidget.bindTexture(QString fileName)'''
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
    def renderText(self, x, y, str, font = QFont(), listBase = 2000):
        '''void QGLWidget.renderText(int x, int y, QString str, QFont font = QFont(), int listBase = 2000)'''
    def renderText(self, x, y, z, str, font = QFont(), listBase = 2000):
        '''void QGLWidget.renderText(float x, float y, float z, QString str, QFont font = QFont(), int listBase = 2000)'''
    def setColormap(self, map):
        '''void QGLWidget.setColormap(QGLColormap map)'''
    def colormap(self):
        '''QGLColormap QGLWidget.colormap()'''
        return QGLColormap()
    def setMouseTracking(self, enable):
        '''void QGLWidget.setMouseTracking(bool enable)'''
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
    def setFormat(self, format):
        '''void QGLWidget.setFormat(QGLFormat format)'''
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


class QGLBuffer():
    """"""
    # Enum QGLBuffer.UsagePattern
    StreamDraw = 0
    StreamRead = 0
    StreamCopy = 0
    StaticDraw = 0
    StaticRead = 0
    StaticCopy = 0
    DynamicDraw = 0
    DynamicRead = 0
    DynamicCopy = 0

    # Enum QGLBuffer.Type
    VertexBuffer = 0
    IndexBuffer = 0
    PixelPackBuffer = 0
    PixelUnpackBuffer = 0

    # Enum QGLBuffer.Access
    ReadOnly = 0
    WriteOnly = 0
    ReadWrite = 0

    def __init__(self):
        '''void QGLBuffer.__init__()'''
    def __init__(self, type):
        '''void QGLBuffer.__init__(QGLBuffer.Type type)'''
    def __init__(self, other):
        '''void QGLBuffer.__init__(QGLBuffer other)'''
    def unmap(self):
        '''bool QGLBuffer.unmap()'''
        return bool()
    def map(self, access):
        '''sip.voidptr QGLBuffer.map(QGLBuffer.Access access)'''
        return sip.voidptr()
    def allocate(self, data, count):
        '''void QGLBuffer.allocate(sip.voidptr data, int count)'''
    def allocate(self, count):
        '''void QGLBuffer.allocate(int count)'''
    def write(self, offset, data, count):
        '''void QGLBuffer.write(int offset, sip.voidptr data, int count)'''
    def read(self, offset, data, count):
        '''bool QGLBuffer.read(int offset, sip.voidptr data, int count)'''
        return bool()
    def size(self):
        '''int QGLBuffer.size()'''
        return int()
    def bufferId(self):
        '''int QGLBuffer.bufferId()'''
        return int()
    def release(self):
        '''void QGLBuffer.release()'''
    def release(self, type):
        '''static void QGLBuffer.release(QGLBuffer.Type type)'''
    def bind(self):
        '''bool QGLBuffer.bind()'''
        return bool()
    def destroy(self):
        '''void QGLBuffer.destroy()'''
    def isCreated(self):
        '''bool QGLBuffer.isCreated()'''
        return bool()
    def create(self):
        '''bool QGLBuffer.create()'''
        return bool()
    def setUsagePattern(self, value):
        '''void QGLBuffer.setUsagePattern(QGLBuffer.UsagePattern value)'''
    def usagePattern(self):
        '''QGLBuffer.UsagePattern QGLBuffer.usagePattern()'''
        return QGLBuffer.UsagePattern()
    def type(self):
        '''QGLBuffer.Type QGLBuffer.type()'''
        return QGLBuffer.Type()


class QGLColormap():
    """"""
    def __init__(self):
        '''void QGLColormap.__init__()'''
    def __init__(self):
        '''QGLColormap QGLColormap.__init__()'''
        return QGLColormap()
    def setHandle(self, ahandle):
        '''void QGLColormap.setHandle(int ahandle)'''
    def handle(self):
        '''int QGLColormap.handle()'''
        return int()
    def findNearest(self, color):
        '''int QGLColormap.findNearest(int color)'''
        return int()
    def find(self, color):
        '''int QGLColormap.find(int color)'''
        return int()
    def entryColor(self, idx):
        '''QColor QGLColormap.entryColor(int idx)'''
        return QColor()
    def entryRgb(self, idx):
        '''int QGLColormap.entryRgb(int idx)'''
        return int()
    def setEntry(self, idx, color):
        '''void QGLColormap.setEntry(int idx, int color)'''
    def setEntry(self, idx, color):
        '''void QGLColormap.setEntry(int idx, QColor color)'''
    def setEntries(self, colors, base = 0):
        '''void QGLColormap.setEntries(list-of-int colors, int base = 0)'''
    def size(self):
        '''int QGLColormap.size()'''
        return int()
    def isEmpty(self):
        '''bool QGLColormap.isEmpty()'''
        return bool()
    def detach(self):
        '''void QGLColormap.detach()'''


class QGLFramebufferObject(QPaintDevice):
    """"""
    # Enum QGLFramebufferObject.Attachment
    NoAttachment = 0
    CombinedDepthStencil = 0
    Depth = 0

    def __init__(self, size, target = None):
        '''void QGLFramebufferObject.__init__(QSize size, int target = GL_TEXTURE_2D)'''
    def __init__(self, width, height, target = None):
        '''void QGLFramebufferObject.__init__(int width, int height, int target = GL_TEXTURE_2D)'''
    def __init__(self, size, attachment, target = None, internalFormat = None):
        '''void QGLFramebufferObject.__init__(QSize size, QGLFramebufferObject.Attachment attachment, int target = GL_TEXTURE_2D, int internalFormat = GL_RGBA8)'''
    def __init__(self, width, height, attachment, target = None, internalFormat = None):
        '''void QGLFramebufferObject.__init__(int width, int height, QGLFramebufferObject.Attachment attachment, int target = GL_TEXTURE_2D, int internalFormat = GL_RGBA8)'''
    def __init__(self, size, format):
        '''void QGLFramebufferObject.__init__(QSize size, QGLFramebufferObjectFormat format)'''
    def __init__(self, width, height, format):
        '''void QGLFramebufferObject.__init__(int width, int height, QGLFramebufferObjectFormat format)'''
    def blitFramebuffer(self, target, targetRect, source, sourceRect, buffers = None, filter = None):
        '''static void QGLFramebufferObject.blitFramebuffer(QGLFramebufferObject target, QRect targetRect, QGLFramebufferObject source, QRect sourceRect, int buffers = GL_COLOR_BUFFER_BIT, int filter = GL_NEAREST)'''
    def hasOpenGLFramebufferBlit(self):
        '''static bool QGLFramebufferObject.hasOpenGLFramebufferBlit()'''
        return bool()
    def format(self):
        '''QGLFramebufferObjectFormat QGLFramebufferObject.format()'''
        return QGLFramebufferObjectFormat()
    def metric(self, metric):
        '''int QGLFramebufferObject.metric(QPaintDevice.PaintDeviceMetric metric)'''
        return int()
    def hasOpenGLFramebufferObjects(self):
        '''static bool QGLFramebufferObject.hasOpenGLFramebufferObjects()'''
        return bool()
    def handle(self):
        '''int QGLFramebufferObject.handle()'''
        return int()
    def paintEngine(self):
        '''QPaintEngine QGLFramebufferObject.paintEngine()'''
        return QPaintEngine()
    def toImage(self):
        '''QImage QGLFramebufferObject.toImage()'''
        return QImage()
    def size(self):
        '''QSize QGLFramebufferObject.size()'''
        return QSize()
    def drawTexture(self, target, textureId, textureTarget = None):
        '''void QGLFramebufferObject.drawTexture(QRectF target, int textureId, int textureTarget = GL_TEXTURE_2D)'''
    def drawTexture(self, point, textureId, textureTarget = None):
        '''void QGLFramebufferObject.drawTexture(QPointF point, int textureId, int textureTarget = GL_TEXTURE_2D)'''
    def texture(self):
        '''int QGLFramebufferObject.texture()'''
        return int()
    def release(self):
        '''bool QGLFramebufferObject.release()'''
        return bool()
    def isBound(self):
        '''bool QGLFramebufferObject.isBound()'''
        return bool()
    def bind(self):
        '''bool QGLFramebufferObject.bind()'''
        return bool()
    def isValid(self):
        '''bool QGLFramebufferObject.isValid()'''
        return bool()
    def attachment(self):
        '''QGLFramebufferObject.Attachment QGLFramebufferObject.attachment()'''
        return QGLFramebufferObject.Attachment()


class QGLFramebufferObjectFormat():
    """"""
    def __init__(self):
        '''void QGLFramebufferObjectFormat.__init__()'''
    def __init__(self, other):
        '''void QGLFramebufferObjectFormat.__init__(QGLFramebufferObjectFormat other)'''
    def mipmap(self):
        '''bool QGLFramebufferObjectFormat.mipmap()'''
        return bool()
    def setMipmap(self, enabled):
        '''void QGLFramebufferObjectFormat.setMipmap(bool enabled)'''
    def __ne__(self, other):
        '''bool QGLFramebufferObjectFormat.__ne__(QGLFramebufferObjectFormat other)'''
        return bool()
    def __eq__(self, other):
        '''bool QGLFramebufferObjectFormat.__eq__(QGLFramebufferObjectFormat other)'''
        return bool()
    def internalTextureFormat(self):
        '''int QGLFramebufferObjectFormat.internalTextureFormat()'''
        return int()
    def setInternalTextureFormat(self, internalTextureFormat):
        '''void QGLFramebufferObjectFormat.setInternalTextureFormat(int internalTextureFormat)'''
    def textureTarget(self):
        '''int QGLFramebufferObjectFormat.textureTarget()'''
        return int()
    def setTextureTarget(self, target):
        '''void QGLFramebufferObjectFormat.setTextureTarget(int target)'''
    def attachment(self):
        '''QGLFramebufferObject.Attachment QGLFramebufferObjectFormat.attachment()'''
        return QGLFramebufferObject.Attachment()
    def setAttachment(self, attachment):
        '''void QGLFramebufferObjectFormat.setAttachment(QGLFramebufferObject.Attachment attachment)'''
    def samples(self):
        '''int QGLFramebufferObjectFormat.samples()'''
        return int()
    def setSamples(self, samples):
        '''void QGLFramebufferObjectFormat.setSamples(int samples)'''


class QGLPixelBuffer(QPaintDevice):
    """"""
    def __init__(self, size, format = None, shareWidget = None):
        '''void QGLPixelBuffer.__init__(QSize size, QGLFormat format = QGLFormat.defaultFormat(), QGLWidget shareWidget = None)'''
    def __init__(self, width, height, format = None, shareWidget = None):
        '''void QGLPixelBuffer.__init__(int width, int height, QGLFormat format = QGLFormat.defaultFormat(), QGLWidget shareWidget = None)'''
    def devType(self):
        '''int QGLPixelBuffer.devType()'''
        return int()
    def metric(self, metric):
        '''int QGLPixelBuffer.metric(QPaintDevice.PaintDeviceMetric metric)'''
        return int()
    def hasOpenGLPbuffers(self):
        '''static bool QGLPixelBuffer.hasOpenGLPbuffers()'''
        return bool()
    def format(self):
        '''QGLFormat QGLPixelBuffer.format()'''
        return QGLFormat()
    def paintEngine(self):
        '''QPaintEngine QGLPixelBuffer.paintEngine()'''
        return QPaintEngine()
    def toImage(self):
        '''QImage QGLPixelBuffer.toImage()'''
        return QImage()
    def handle(self):
        '''int QGLPixelBuffer.handle()'''
        return int()
    def size(self):
        '''QSize QGLPixelBuffer.size()'''
        return QSize()
    def deleteTexture(self, texture_id):
        '''void QGLPixelBuffer.deleteTexture(int texture_id)'''
    def drawTexture(self, target, textureId, textureTarget = None):
        '''void QGLPixelBuffer.drawTexture(QRectF target, int textureId, int textureTarget = GL_TEXTURE_2D)'''
    def drawTexture(self, point, textureId, textureTarget = None):
        '''void QGLPixelBuffer.drawTexture(QPointF point, int textureId, int textureTarget = GL_TEXTURE_2D)'''
    def bindTexture(self, image, target = None):
        '''int QGLPixelBuffer.bindTexture(QImage image, int target = GL_TEXTURE_2D)'''
        return int()
    def bindTexture(self, pixmap, target = None):
        '''int QGLPixelBuffer.bindTexture(QPixmap pixmap, int target = GL_TEXTURE_2D)'''
        return int()
    def bindTexture(self, fileName):
        '''int QGLPixelBuffer.bindTexture(QString fileName)'''
        return int()
    def updateDynamicTexture(self, texture_id):
        '''void QGLPixelBuffer.updateDynamicTexture(int texture_id)'''
    def releaseFromDynamicTexture(self):
        '''void QGLPixelBuffer.releaseFromDynamicTexture()'''
    def bindToDynamicTexture(self, texture):
        '''bool QGLPixelBuffer.bindToDynamicTexture(int texture)'''
        return bool()
    def generateDynamicTexture(self):
        '''int QGLPixelBuffer.generateDynamicTexture()'''
        return int()
    def doneCurrent(self):
        '''bool QGLPixelBuffer.doneCurrent()'''
        return bool()
    def makeCurrent(self):
        '''bool QGLPixelBuffer.makeCurrent()'''
        return bool()
    def isValid(self):
        '''bool QGLPixelBuffer.isValid()'''
        return bool()


class QGLShader(QObject):
    """"""
    # Enum QGLShader.ShaderTypeBit
    Vertex = 0
    Fragment = 0
    Geometry = 0

    def __init__(self, type, parent = None):
        '''void QGLShader.__init__(QGLShader.ShaderType type, QObject parent = None)'''
    def __init__(self, type, context, parent = None):
        '''void QGLShader.__init__(QGLShader.ShaderType type, QGLContext context, QObject parent = None)'''
    def hasOpenGLShaders(self, type, context = None):
        '''static bool QGLShader.hasOpenGLShaders(QGLShader.ShaderType type, QGLContext context = None)'''
        return bool()
    def shaderId(self):
        '''int QGLShader.shaderId()'''
        return int()
    def log(self):
        '''QString QGLShader.log()'''
        return QString()
    def isCompiled(self):
        '''bool QGLShader.isCompiled()'''
        return bool()
    def sourceCode(self):
        '''QByteArray QGLShader.sourceCode()'''
        return QByteArray()
    def compileSourceFile(self, fileName):
        '''bool QGLShader.compileSourceFile(QString fileName)'''
        return bool()
    def compileSourceCode(self, source):
        '''bool QGLShader.compileSourceCode(QByteArray source)'''
        return bool()
    def compileSourceCode(self, source):
        '''bool QGLShader.compileSourceCode(QString source)'''
        return bool()
    def shaderType(self):
        '''QGLShader.ShaderType QGLShader.shaderType()'''
        return QGLShader.ShaderType()
    class ShaderType():
        """"""
        def __init__(self):
            '''QGLShader.ShaderType QGLShader.ShaderType.__init__()'''
            return QGLShader.ShaderType()
        def __init__(self):
            '''int QGLShader.ShaderType.__init__()'''
            return int()
        def __init__(self):
            '''void QGLShader.ShaderType.__init__()'''
        def __bool__(self):
            '''int QGLShader.ShaderType.__bool__()'''
            return int()
        def __ne__(self, f):
            '''bool QGLShader.ShaderType.__ne__(QGLShader.ShaderType f)'''
            return bool()
        def __eq__(self, f):
            '''bool QGLShader.ShaderType.__eq__(QGLShader.ShaderType f)'''
            return bool()
        def __invert__(self):
            '''QGLShader.ShaderType QGLShader.ShaderType.__invert__()'''
            return QGLShader.ShaderType()
        def __and__(self, mask):
            '''QGLShader.ShaderType QGLShader.ShaderType.__and__(int mask)'''
            return QGLShader.ShaderType()
        def __xor__(self, f):
            '''QGLShader.ShaderType QGLShader.ShaderType.__xor__(QGLShader.ShaderType f)'''
            return QGLShader.ShaderType()
        def __xor__(self, f):
            '''QGLShader.ShaderType QGLShader.ShaderType.__xor__(int f)'''
            return QGLShader.ShaderType()
        def __or__(self, f):
            '''QGLShader.ShaderType QGLShader.ShaderType.__or__(QGLShader.ShaderType f)'''
            return QGLShader.ShaderType()
        def __or__(self, f):
            '''QGLShader.ShaderType QGLShader.ShaderType.__or__(int f)'''
            return QGLShader.ShaderType()
        def __int__(self):
            '''int QGLShader.ShaderType.__int__()'''
            return int()
        def __ixor__(self, f):
            '''QGLShader.ShaderType QGLShader.ShaderType.__ixor__(QGLShader.ShaderType f)'''
            return QGLShader.ShaderType()
        def __ior__(self, f):
            '''QGLShader.ShaderType QGLShader.ShaderType.__ior__(QGLShader.ShaderType f)'''
            return QGLShader.ShaderType()
        def __iand__(self, mask):
            '''QGLShader.ShaderType QGLShader.ShaderType.__iand__(int mask)'''
            return QGLShader.ShaderType()


class QGLShaderProgram(QObject):
    """"""
    def __init__(self, parent = None):
        '''void QGLShaderProgram.__init__(QObject parent = None)'''
    def __init__(self, context, parent = None):
        '''void QGLShaderProgram.__init__(QGLContext context, QObject parent = None)'''
    def setAttributeBuffer(self, location, type, offset, tupleSize, stride = 0):
        '''void QGLShaderProgram.setAttributeBuffer(int location, int type, int offset, int tupleSize, int stride = 0)'''
    def setAttributeBuffer(self, name, type, offset, tupleSize, stride = 0):
        '''void QGLShaderProgram.setAttributeBuffer(str name, int type, int offset, int tupleSize, int stride = 0)'''
    def geometryOutputType(self):
        '''int QGLShaderProgram.geometryOutputType()'''
        return int()
    def setGeometryOutputType(self, outputType):
        '''void QGLShaderProgram.setGeometryOutputType(int outputType)'''
    def geometryInputType(self):
        '''int QGLShaderProgram.geometryInputType()'''
        return int()
    def setGeometryInputType(self, inputType):
        '''void QGLShaderProgram.setGeometryInputType(int inputType)'''
    def geometryOutputVertexCount(self):
        '''int QGLShaderProgram.geometryOutputVertexCount()'''
        return int()
    def setGeometryOutputVertexCount(self, count):
        '''void QGLShaderProgram.setGeometryOutputVertexCount(int count)'''
    def hasOpenGLShaderPrograms(self, context = None):
        '''static bool QGLShaderProgram.hasOpenGLShaderPrograms(QGLContext context = None)'''
        return bool()
    def setUniformValue(self, location, value):
        '''void QGLShaderProgram.setUniformValue(int location, int value)'''
    def setUniformValue(self, location, value):
        '''void QGLShaderProgram.setUniformValue(int location, float value)'''
    def setUniformValue(self, location, x, y):
        '''void QGLShaderProgram.setUniformValue(int location, float x, float y)'''
    def setUniformValue(self, location, x, y, z):
        '''void QGLShaderProgram.setUniformValue(int location, float x, float y, float z)'''
    def setUniformValue(self, location, x, y, z, w):
        '''void QGLShaderProgram.setUniformValue(int location, float x, float y, float z, float w)'''
    def setUniformValue(self, location, value):
        '''void QGLShaderProgram.setUniformValue(int location, QVector2D value)'''
    def setUniformValue(self, location, value):
        '''void QGLShaderProgram.setUniformValue(int location, QVector3D value)'''
    def setUniformValue(self, location, value):
        '''void QGLShaderProgram.setUniformValue(int location, QVector4D value)'''
    def setUniformValue(self, location, color):
        '''void QGLShaderProgram.setUniformValue(int location, QColor color)'''
    def setUniformValue(self, location, point):
        '''void QGLShaderProgram.setUniformValue(int location, QPoint point)'''
    def setUniformValue(self, location, point):
        '''void QGLShaderProgram.setUniformValue(int location, QPointF point)'''
    def setUniformValue(self, location, size):
        '''void QGLShaderProgram.setUniformValue(int location, QSize size)'''
    def setUniformValue(self, location, size):
        '''void QGLShaderProgram.setUniformValue(int location, QSizeF size)'''
    def setUniformValue(self, location, value):
        '''void QGLShaderProgram.setUniformValue(int location, QMatrix2x2 value)'''
    def setUniformValue(self, location, value):
        '''void QGLShaderProgram.setUniformValue(int location, QMatrix2x3 value)'''
    def setUniformValue(self, location, value):
        '''void QGLShaderProgram.setUniformValue(int location, QMatrix2x4 value)'''
    def setUniformValue(self, location, value):
        '''void QGLShaderProgram.setUniformValue(int location, QMatrix3x2 value)'''
    def setUniformValue(self, location, value):
        '''void QGLShaderProgram.setUniformValue(int location, QMatrix3x3 value)'''
    def setUniformValue(self, location, value):
        '''void QGLShaderProgram.setUniformValue(int location, QMatrix3x4 value)'''
    def setUniformValue(self, location, value):
        '''void QGLShaderProgram.setUniformValue(int location, QMatrix4x2 value)'''
    def setUniformValue(self, location, value):
        '''void QGLShaderProgram.setUniformValue(int location, QMatrix4x3 value)'''
    def setUniformValue(self, location, value):
        '''void QGLShaderProgram.setUniformValue(int location, QMatrix4x4 value)'''
    def setUniformValue(self, location, value):
        '''void QGLShaderProgram.setUniformValue(int location, QTransform value)'''
    def setUniformValue(self, name, value):
        '''void QGLShaderProgram.setUniformValue(str name, int value)'''
    def setUniformValue(self, name, value):
        '''void QGLShaderProgram.setUniformValue(str name, float value)'''
    def setUniformValue(self, name, x, y):
        '''void QGLShaderProgram.setUniformValue(str name, float x, float y)'''
    def setUniformValue(self, name, x, y, z):
        '''void QGLShaderProgram.setUniformValue(str name, float x, float y, float z)'''
    def setUniformValue(self, name, x, y, z, w):
        '''void QGLShaderProgram.setUniformValue(str name, float x, float y, float z, float w)'''
    def setUniformValue(self, name, value):
        '''void QGLShaderProgram.setUniformValue(str name, QVector2D value)'''
    def setUniformValue(self, name, value):
        '''void QGLShaderProgram.setUniformValue(str name, QVector3D value)'''
    def setUniformValue(self, name, value):
        '''void QGLShaderProgram.setUniformValue(str name, QVector4D value)'''
    def setUniformValue(self, name, color):
        '''void QGLShaderProgram.setUniformValue(str name, QColor color)'''
    def setUniformValue(self, name, point):
        '''void QGLShaderProgram.setUniformValue(str name, QPoint point)'''
    def setUniformValue(self, name, point):
        '''void QGLShaderProgram.setUniformValue(str name, QPointF point)'''
    def setUniformValue(self, name, size):
        '''void QGLShaderProgram.setUniformValue(str name, QSize size)'''
    def setUniformValue(self, name, size):
        '''void QGLShaderProgram.setUniformValue(str name, QSizeF size)'''
    def setUniformValue(self, name, value):
        '''void QGLShaderProgram.setUniformValue(str name, QMatrix2x2 value)'''
    def setUniformValue(self, name, value):
        '''void QGLShaderProgram.setUniformValue(str name, QMatrix2x3 value)'''
    def setUniformValue(self, name, value):
        '''void QGLShaderProgram.setUniformValue(str name, QMatrix2x4 value)'''
    def setUniformValue(self, name, value):
        '''void QGLShaderProgram.setUniformValue(str name, QMatrix3x2 value)'''
    def setUniformValue(self, name, value):
        '''void QGLShaderProgram.setUniformValue(str name, QMatrix3x3 value)'''
    def setUniformValue(self, name, value):
        '''void QGLShaderProgram.setUniformValue(str name, QMatrix3x4 value)'''
    def setUniformValue(self, name, value):
        '''void QGLShaderProgram.setUniformValue(str name, QMatrix4x2 value)'''
    def setUniformValue(self, name, value):
        '''void QGLShaderProgram.setUniformValue(str name, QMatrix4x3 value)'''
    def setUniformValue(self, name, value):
        '''void QGLShaderProgram.setUniformValue(str name, QMatrix4x4 value)'''
    def setUniformValue(self, name, value):
        '''void QGLShaderProgram.setUniformValue(str name, QTransform value)'''
    def setUniformValueArray(self, location, values):
        '''void QGLShaderProgram.setUniformValueArray(int location, sequence values)'''
    def setUniformValueArray(self, name, values):
        '''void QGLShaderProgram.setUniformValueArray(str name, sequence values)'''
    def uniformLocation(self, name):
        '''int QGLShaderProgram.uniformLocation(QByteArray name)'''
        return int()
    def uniformLocation(self, name):
        '''int QGLShaderProgram.uniformLocation(QString name)'''
        return int()
    def disableAttributeArray(self, location):
        '''void QGLShaderProgram.disableAttributeArray(int location)'''
    def disableAttributeArray(self, name):
        '''void QGLShaderProgram.disableAttributeArray(str name)'''
    def enableAttributeArray(self, location):
        '''void QGLShaderProgram.enableAttributeArray(int location)'''
    def enableAttributeArray(self, name):
        '''void QGLShaderProgram.enableAttributeArray(str name)'''
    def setAttributeValue(self, location, value):
        '''void QGLShaderProgram.setAttributeValue(int location, float value)'''
    def setAttributeValue(self, location, x, y):
        '''void QGLShaderProgram.setAttributeValue(int location, float x, float y)'''
    def setAttributeValue(self, location, x, y, z):
        '''void QGLShaderProgram.setAttributeValue(int location, float x, float y, float z)'''
    def setAttributeValue(self, location, x, y, z, w):
        '''void QGLShaderProgram.setAttributeValue(int location, float x, float y, float z, float w)'''
    def setAttributeValue(self, location, value):
        '''void QGLShaderProgram.setAttributeValue(int location, QVector2D value)'''
    def setAttributeValue(self, location, value):
        '''void QGLShaderProgram.setAttributeValue(int location, QVector3D value)'''
    def setAttributeValue(self, location, value):
        '''void QGLShaderProgram.setAttributeValue(int location, QVector4D value)'''
    def setAttributeValue(self, location, value):
        '''void QGLShaderProgram.setAttributeValue(int location, QColor value)'''
    def setAttributeValue(self, name, value):
        '''void QGLShaderProgram.setAttributeValue(str name, float value)'''
    def setAttributeValue(self, name, x, y):
        '''void QGLShaderProgram.setAttributeValue(str name, float x, float y)'''
    def setAttributeValue(self, name, x, y, z):
        '''void QGLShaderProgram.setAttributeValue(str name, float x, float y, float z)'''
    def setAttributeValue(self, name, x, y, z, w):
        '''void QGLShaderProgram.setAttributeValue(str name, float x, float y, float z, float w)'''
    def setAttributeValue(self, name, value):
        '''void QGLShaderProgram.setAttributeValue(str name, QVector2D value)'''
    def setAttributeValue(self, name, value):
        '''void QGLShaderProgram.setAttributeValue(str name, QVector3D value)'''
    def setAttributeValue(self, name, value):
        '''void QGLShaderProgram.setAttributeValue(str name, QVector4D value)'''
    def setAttributeValue(self, name, value):
        '''void QGLShaderProgram.setAttributeValue(str name, QColor value)'''
    def setAttributeArray(self, location, values):
        '''void QGLShaderProgram.setAttributeArray(int location, sequence values)'''
    def setAttributeArray(self, name, values):
        '''void QGLShaderProgram.setAttributeArray(str name, sequence values)'''
    def attributeLocation(self, name):
        '''int QGLShaderProgram.attributeLocation(QByteArray name)'''
        return int()
    def attributeLocation(self, name):
        '''int QGLShaderProgram.attributeLocation(QString name)'''
        return int()
    def bindAttributeLocation(self, name, location):
        '''void QGLShaderProgram.bindAttributeLocation(QByteArray name, int location)'''
    def bindAttributeLocation(self, name, location):
        '''void QGLShaderProgram.bindAttributeLocation(QString name, int location)'''
    def programId(self):
        '''int QGLShaderProgram.programId()'''
        return int()
    def release(self):
        '''void QGLShaderProgram.release()'''
    def bind(self):
        '''bool QGLShaderProgram.bind()'''
        return bool()
    def log(self):
        '''QString QGLShaderProgram.log()'''
        return QString()
    def isLinked(self):
        '''bool QGLShaderProgram.isLinked()'''
        return bool()
    def link(self):
        '''bool QGLShaderProgram.link()'''
        return bool()
    def removeAllShaders(self):
        '''void QGLShaderProgram.removeAllShaders()'''
    def addShaderFromSourceFile(self, type, fileName):
        '''bool QGLShaderProgram.addShaderFromSourceFile(QGLShader.ShaderType type, QString fileName)'''
        return bool()
    def addShaderFromSourceCode(self, type, source):
        '''bool QGLShaderProgram.addShaderFromSourceCode(QGLShader.ShaderType type, QByteArray source)'''
        return bool()
    def addShaderFromSourceCode(self, type, source):
        '''bool QGLShaderProgram.addShaderFromSourceCode(QGLShader.ShaderType type, QString source)'''
        return bool()
    def shaders(self):
        '''list-of-QGLShader QGLShaderProgram.shaders()'''
        return [QGLShader()]
    def removeShader(self, shader):
        '''void QGLShaderProgram.removeShader(QGLShader shader)'''
    def addShader(self, shader):
        '''bool QGLShaderProgram.addShader(QGLShader shader)'''
        return bool()


