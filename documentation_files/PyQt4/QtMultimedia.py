class pyqtSignal():
 def connect(self, targetSignal): pass
 def emit(self, *args): pass
from QtCore import *

class QAbstractVideoBuffer():
    """"""
    # Enum QAbstractVideoBuffer.MapMode
    NotMapped = 0
    ReadOnly = 0
    WriteOnly = 0
    ReadWrite = 0

    # Enum QAbstractVideoBuffer.HandleType
    NoHandle = 0
    GLTextureHandle = 0
    XvShmImageHandle = 0
    CoreImageHandle = 0
    QPixmapHandle = 0
    UserHandle = 0

    def __init__(self, type):
        '''void QAbstractVideoBuffer.__init__(QAbstractVideoBuffer.HandleType type)'''
    def handle(self):
        '''QVariant QAbstractVideoBuffer.handle()'''
        return QVariant()
    def unmap(self):
        '''abstract void QAbstractVideoBuffer.unmap()'''
    def map(self, mode, numBytes, bytesPerLine):
        '''abstract sip.voidptr QAbstractVideoBuffer.map(QAbstractVideoBuffer.MapMode mode, int numBytes, int bytesPerLine)'''
        return sip.voidptr()
    def mapMode(self):
        '''abstract QAbstractVideoBuffer.MapMode QAbstractVideoBuffer.mapMode()'''
        return QAbstractVideoBuffer.MapMode()
    def handleType(self):
        '''QAbstractVideoBuffer.HandleType QAbstractVideoBuffer.handleType()'''
        return QAbstractVideoBuffer.HandleType()


class QAbstractVideoSurface(QObject):
    """"""
    # Enum QAbstractVideoSurface.Error
    NoError = 0
    UnsupportedFormatError = 0
    IncorrectFormatError = 0
    StoppedError = 0
    ResourceError = 0

    def __init__(self, parent = None):
        '''void QAbstractVideoSurface.__init__(QObject parent = None)'''
    def setError(self, error):
        '''void QAbstractVideoSurface.setError(QAbstractVideoSurface.Error error)'''
    supportedFormatsChanged = pyqtSignal() # void supportedFormatsChanged() - signal
    surfaceFormatChanged = pyqtSignal() # void surfaceFormatChanged(const QVideoSurfaceFormatamp;) - signal
    activeChanged = pyqtSignal() # void activeChanged(bool) - signal
    def error(self):
        '''QAbstractVideoSurface.Error QAbstractVideoSurface.error()'''
        return QAbstractVideoSurface.Error()
    def present(self, frame):
        '''abstract bool QAbstractVideoSurface.present(QVideoFrame frame)'''
        return bool()
    def isActive(self):
        '''bool QAbstractVideoSurface.isActive()'''
        return bool()
    def stop(self):
        '''void QAbstractVideoSurface.stop()'''
    def start(self, format):
        '''bool QAbstractVideoSurface.start(QVideoSurfaceFormat format)'''
        return bool()
    def surfaceFormat(self):
        '''QVideoSurfaceFormat QAbstractVideoSurface.surfaceFormat()'''
        return QVideoSurfaceFormat()
    def nearestFormat(self, format):
        '''QVideoSurfaceFormat QAbstractVideoSurface.nearestFormat(QVideoSurfaceFormat format)'''
        return QVideoSurfaceFormat()
    def isFormatSupported(self, format):
        '''bool QAbstractVideoSurface.isFormatSupported(QVideoSurfaceFormat format)'''
        return bool()
    def supportedPixelFormats(self, type = None):
        '''abstract list-of-QVideoFrame.PixelFormat QAbstractVideoSurface.supportedPixelFormats(QAbstractVideoBuffer.HandleType type = QAbstractVideoBuffer.NoHandle)'''
        return [QVideoFrame.PixelFormat()]


class QAudio():
    """"""
    # Enum QAudio.Mode
    AudioInput = 0
    AudioOutput = 0

    # Enum QAudio.State
    ActiveState = 0
    SuspendedState = 0
    StoppedState = 0
    IdleState = 0

    # Enum QAudio.Error
    NoError = 0
    OpenError = 0
    IOError = 0
    UnderrunError = 0
    FatalError = 0



class QAudioDeviceInfo():
    """"""
    def __init__(self):
        '''void QAudioDeviceInfo.__init__()'''
    def __init__(self, other):
        '''void QAudioDeviceInfo.__init__(QAudioDeviceInfo other)'''
    def supportedChannelCounts(self):
        '''list-of-int QAudioDeviceInfo.supportedChannelCounts()'''
        return [int()]
    def supportedSampleRates(self):
        '''list-of-int QAudioDeviceInfo.supportedSampleRates()'''
        return [int()]
    def availableDevices(self, mode):
        '''static list-of-QAudioDeviceInfo QAudioDeviceInfo.availableDevices(QAudio.Mode mode)'''
        return [QAudioDeviceInfo()]
    def defaultOutputDevice(self):
        '''static QAudioDeviceInfo QAudioDeviceInfo.defaultOutputDevice()'''
        return QAudioDeviceInfo()
    def defaultInputDevice(self):
        '''static QAudioDeviceInfo QAudioDeviceInfo.defaultInputDevice()'''
        return QAudioDeviceInfo()
    def supportedSampleTypes(self):
        '''list-of-QAudioFormat.SampleType QAudioDeviceInfo.supportedSampleTypes()'''
        return [QAudioFormat.SampleType()]
    def supportedByteOrders(self):
        '''list-of-QAudioFormat.Endian QAudioDeviceInfo.supportedByteOrders()'''
        return [QAudioFormat.Endian()]
    def supportedSampleSizes(self):
        '''list-of-int QAudioDeviceInfo.supportedSampleSizes()'''
        return [int()]
    def supportedChannels(self):
        '''list-of-int QAudioDeviceInfo.supportedChannels()'''
        return [int()]
    def supportedFrequencies(self):
        '''list-of-int QAudioDeviceInfo.supportedFrequencies()'''
        return [int()]
    def supportedCodecs(self):
        '''QStringList QAudioDeviceInfo.supportedCodecs()'''
        return QStringList()
    def nearestFormat(self, format):
        '''QAudioFormat QAudioDeviceInfo.nearestFormat(QAudioFormat format)'''
        return QAudioFormat()
    def preferredFormat(self):
        '''QAudioFormat QAudioDeviceInfo.preferredFormat()'''
        return QAudioFormat()
    def isFormatSupported(self, format):
        '''bool QAudioDeviceInfo.isFormatSupported(QAudioFormat format)'''
        return bool()
    def deviceName(self):
        '''QString QAudioDeviceInfo.deviceName()'''
        return QString()
    def isNull(self):
        '''bool QAudioDeviceInfo.isNull()'''
        return bool()


class QAudioFormat():
    """"""
    # Enum QAudioFormat.Endian
    BigEndian = 0
    LittleEndian = 0

    # Enum QAudioFormat.SampleType
    Unknown = 0
    SignedInt = 0
    UnSignedInt = 0
    Float = 0

    def __init__(self):
        '''void QAudioFormat.__init__()'''
    def __init__(self, other):
        '''void QAudioFormat.__init__(QAudioFormat other)'''
    def channelCount(self):
        '''int QAudioFormat.channelCount()'''
        return int()
    def setChannelCount(self, channelCount):
        '''void QAudioFormat.setChannelCount(int channelCount)'''
    def sampleRate(self):
        '''int QAudioFormat.sampleRate()'''
        return int()
    def setSampleRate(self, sampleRate):
        '''void QAudioFormat.setSampleRate(int sampleRate)'''
    def sampleType(self):
        '''QAudioFormat.SampleType QAudioFormat.sampleType()'''
        return QAudioFormat.SampleType()
    def setSampleType(self, sampleType):
        '''void QAudioFormat.setSampleType(QAudioFormat.SampleType sampleType)'''
    def byteOrder(self):
        '''QAudioFormat.Endian QAudioFormat.byteOrder()'''
        return QAudioFormat.Endian()
    def setByteOrder(self, byteOrder):
        '''void QAudioFormat.setByteOrder(QAudioFormat.Endian byteOrder)'''
    def codec(self):
        '''QString QAudioFormat.codec()'''
        return QString()
    def setCodec(self, codec):
        '''void QAudioFormat.setCodec(QString codec)'''
    def sampleSize(self):
        '''int QAudioFormat.sampleSize()'''
        return int()
    def setSampleSize(self, sampleSize):
        '''void QAudioFormat.setSampleSize(int sampleSize)'''
    def channels(self):
        '''int QAudioFormat.channels()'''
        return int()
    def setChannels(self, channels):
        '''void QAudioFormat.setChannels(int channels)'''
    def frequency(self):
        '''int QAudioFormat.frequency()'''
        return int()
    def setFrequency(self, frequency):
        '''void QAudioFormat.setFrequency(int frequency)'''
    def isValid(self):
        '''bool QAudioFormat.isValid()'''
        return bool()
    def __ne__(self, other):
        '''bool QAudioFormat.__ne__(QAudioFormat other)'''
        return bool()
    def __eq__(self, other):
        '''bool QAudioFormat.__eq__(QAudioFormat other)'''
        return bool()


class QAudioInput(QObject):
    """"""
    def __init__(self, format = QAudioFormat(), parent = None):
        '''void QAudioInput.__init__(QAudioFormat format = QAudioFormat(), QObject parent = None)'''
    def __init__(self, audioDevice, format = QAudioFormat(), parent = None):
        '''void QAudioInput.__init__(QAudioDeviceInfo audioDevice, QAudioFormat format = QAudioFormat(), QObject parent = None)'''
    notify = pyqtSignal() # void notify() - signal
    stateChanged = pyqtSignal() # void stateChanged(QAudio::State) - signal
    def state(self):
        '''QAudio.State QAudioInput.state()'''
        return QAudio.State()
    def error(self):
        '''QAudio.Error QAudioInput.error()'''
        return QAudio.Error()
    def elapsedUSecs(self):
        '''int QAudioInput.elapsedUSecs()'''
        return int()
    def processedUSecs(self):
        '''int QAudioInput.processedUSecs()'''
        return int()
    def notifyInterval(self):
        '''int QAudioInput.notifyInterval()'''
        return int()
    def setNotifyInterval(self, milliSeconds):
        '''void QAudioInput.setNotifyInterval(int milliSeconds)'''
    def periodSize(self):
        '''int QAudioInput.periodSize()'''
        return int()
    def bytesReady(self):
        '''int QAudioInput.bytesReady()'''
        return int()
    def bufferSize(self):
        '''int QAudioInput.bufferSize()'''
        return int()
    def setBufferSize(self, bytes):
        '''void QAudioInput.setBufferSize(int bytes)'''
    def resume(self):
        '''void QAudioInput.resume()'''
    def suspend(self):
        '''void QAudioInput.suspend()'''
    def reset(self):
        '''void QAudioInput.reset()'''
    def stop(self):
        '''void QAudioInput.stop()'''
    def start(self, device):
        '''void QAudioInput.start(QIODevice device)'''
    def start(self):
        '''QIODevice QAudioInput.start()'''
        return QIODevice()
    def format(self):
        '''QAudioFormat QAudioInput.format()'''
        return QAudioFormat()


class QAudioOutput(QObject):
    """"""
    def __init__(self, format = QAudioFormat(), parent = None):
        '''void QAudioOutput.__init__(QAudioFormat format = QAudioFormat(), QObject parent = None)'''
    def __init__(self, audioDevice, format = QAudioFormat(), parent = None):
        '''void QAudioOutput.__init__(QAudioDeviceInfo audioDevice, QAudioFormat format = QAudioFormat(), QObject parent = None)'''
    notify = pyqtSignal() # void notify() - signal
    stateChanged = pyqtSignal() # void stateChanged(QAudio::State) - signal
    def state(self):
        '''QAudio.State QAudioOutput.state()'''
        return QAudio.State()
    def error(self):
        '''QAudio.Error QAudioOutput.error()'''
        return QAudio.Error()
    def elapsedUSecs(self):
        '''int QAudioOutput.elapsedUSecs()'''
        return int()
    def processedUSecs(self):
        '''int QAudioOutput.processedUSecs()'''
        return int()
    def notifyInterval(self):
        '''int QAudioOutput.notifyInterval()'''
        return int()
    def setNotifyInterval(self, milliSeconds):
        '''void QAudioOutput.setNotifyInterval(int milliSeconds)'''
    def periodSize(self):
        '''int QAudioOutput.periodSize()'''
        return int()
    def bytesFree(self):
        '''int QAudioOutput.bytesFree()'''
        return int()
    def bufferSize(self):
        '''int QAudioOutput.bufferSize()'''
        return int()
    def setBufferSize(self, bytes):
        '''void QAudioOutput.setBufferSize(int bytes)'''
    def resume(self):
        '''void QAudioOutput.resume()'''
    def suspend(self):
        '''void QAudioOutput.suspend()'''
    def reset(self):
        '''void QAudioOutput.reset()'''
    def stop(self):
        '''void QAudioOutput.stop()'''
    def start(self, device):
        '''void QAudioOutput.start(QIODevice device)'''
    def start(self):
        '''QIODevice QAudioOutput.start()'''
        return QIODevice()
    def format(self):
        '''QAudioFormat QAudioOutput.format()'''
        return QAudioFormat()


class QVideoFrame():
    """"""
    # Enum QVideoFrame.PixelFormat
    Format_Invalid = 0
    Format_ARGB32 = 0
    Format_ARGB32_Premultiplied = 0
    Format_RGB32 = 0
    Format_RGB24 = 0
    Format_RGB565 = 0
    Format_RGB555 = 0
    Format_ARGB8565_Premultiplied = 0
    Format_BGRA32 = 0
    Format_BGRA32_Premultiplied = 0
    Format_BGR32 = 0
    Format_BGR24 = 0
    Format_BGR565 = 0
    Format_BGR555 = 0
    Format_BGRA5658_Premultiplied = 0
    Format_AYUV444 = 0
    Format_AYUV444_Premultiplied = 0
    Format_YUV444 = 0
    Format_YUV420P = 0
    Format_YV12 = 0
    Format_UYVY = 0
    Format_YUYV = 0
    Format_NV12 = 0
    Format_NV21 = 0
    Format_IMC1 = 0
    Format_IMC2 = 0
    Format_IMC3 = 0
    Format_IMC4 = 0
    Format_Y8 = 0
    Format_Y16 = 0
    Format_User = 0

    # Enum QVideoFrame.FieldType
    ProgressiveFrame = 0
    TopField = 0
    BottomField = 0
    InterlacedFrame = 0

    def __init__(self):
        '''void QVideoFrame.__init__()'''
    def __init__(self, buffer, size, format):
        '''void QVideoFrame.__init__(QAbstractVideoBuffer buffer, QSize size, QVideoFrame.PixelFormat format)'''
    def __init__(self, bytes, size, bytesPerLine, format):
        '''void QVideoFrame.__init__(int bytes, QSize size, int bytesPerLine, QVideoFrame.PixelFormat format)'''
    def __init__(self, image):
        '''void QVideoFrame.__init__(QImage image)'''
    def __init__(self, other):
        '''void QVideoFrame.__init__(QVideoFrame other)'''
    def imageFormatFromPixelFormat(self, format):
        '''static QImage.Format QVideoFrame.imageFormatFromPixelFormat(QVideoFrame.PixelFormat format)'''
        return QImage.Format()
    def pixelFormatFromImageFormat(self, format):
        '''static QVideoFrame.PixelFormat QVideoFrame.pixelFormatFromImageFormat(QImage.Format format)'''
        return QVideoFrame.PixelFormat()
    def setEndTime(self, time):
        '''void QVideoFrame.setEndTime(int time)'''
    def endTime(self):
        '''int QVideoFrame.endTime()'''
        return int()
    def setStartTime(self, time):
        '''void QVideoFrame.setStartTime(int time)'''
    def startTime(self):
        '''int QVideoFrame.startTime()'''
        return int()
    def handle(self):
        '''QVariant QVideoFrame.handle()'''
        return QVariant()
    def mappedBytes(self):
        '''int QVideoFrame.mappedBytes()'''
        return int()
    def bits(self):
        '''sip.voidptr QVideoFrame.bits()'''
        return sip.voidptr()
    def bytesPerLine(self):
        '''int QVideoFrame.bytesPerLine()'''
        return int()
    def unmap(self):
        '''void QVideoFrame.unmap()'''
    def map(self, mode):
        '''bool QVideoFrame.map(QAbstractVideoBuffer.MapMode mode)'''
        return bool()
    def mapMode(self):
        '''QAbstractVideoBuffer.MapMode QVideoFrame.mapMode()'''
        return QAbstractVideoBuffer.MapMode()
    def isWritable(self):
        '''bool QVideoFrame.isWritable()'''
        return bool()
    def isReadable(self):
        '''bool QVideoFrame.isReadable()'''
        return bool()
    def isMapped(self):
        '''bool QVideoFrame.isMapped()'''
        return bool()
    def setFieldType(self):
        '''QVideoFrame.FieldType QVideoFrame.setFieldType()'''
        return QVideoFrame.FieldType()
    def fieldType(self):
        '''QVideoFrame.FieldType QVideoFrame.fieldType()'''
        return QVideoFrame.FieldType()
    def height(self):
        '''int QVideoFrame.height()'''
        return int()
    def width(self):
        '''int QVideoFrame.width()'''
        return int()
    def size(self):
        '''QSize QVideoFrame.size()'''
        return QSize()
    def handleType(self):
        '''QAbstractVideoBuffer.HandleType QVideoFrame.handleType()'''
        return QAbstractVideoBuffer.HandleType()
    def pixelFormat(self):
        '''QVideoFrame.PixelFormat QVideoFrame.pixelFormat()'''
        return QVideoFrame.PixelFormat()
    def isValid(self):
        '''bool QVideoFrame.isValid()'''
        return bool()


class QVideoSurfaceFormat():
    """"""
    # Enum QVideoSurfaceFormat.YCbCrColorSpace
    YCbCr_Undefined = 0
    YCbCr_BT601 = 0
    YCbCr_BT709 = 0
    YCbCr_xvYCC601 = 0
    YCbCr_xvYCC709 = 0
    YCbCr_JPEG = 0

    # Enum QVideoSurfaceFormat.Direction
    TopToBottom = 0
    BottomToTop = 0

    def __init__(self):
        '''void QVideoSurfaceFormat.__init__()'''
    def __init__(self, size, format, type = None):
        '''void QVideoSurfaceFormat.__init__(QSize size, QVideoFrame.PixelFormat format, QAbstractVideoBuffer.HandleType type = QAbstractVideoBuffer.NoHandle)'''
    def __init__(self, format):
        '''void QVideoSurfaceFormat.__init__(QVideoSurfaceFormat format)'''
    def setProperty(self, name, value):
        '''void QVideoSurfaceFormat.setProperty(str name, QVariant value)'''
    def property(self, name):
        '''QVariant QVideoSurfaceFormat.property(str name)'''
        return QVariant()
    def propertyNames(self):
        '''list-of-QByteArray QVideoSurfaceFormat.propertyNames()'''
        return [QByteArray()]
    def sizeHint(self):
        '''QSize QVideoSurfaceFormat.sizeHint()'''
        return QSize()
    def setYCbCrColorSpace(self, colorSpace):
        '''void QVideoSurfaceFormat.setYCbCrColorSpace(QVideoSurfaceFormat.YCbCrColorSpace colorSpace)'''
    def yCbCrColorSpace(self):
        '''QVideoSurfaceFormat.YCbCrColorSpace QVideoSurfaceFormat.yCbCrColorSpace()'''
        return QVideoSurfaceFormat.YCbCrColorSpace()
    def setPixelAspectRatio(self, ratio):
        '''void QVideoSurfaceFormat.setPixelAspectRatio(QSize ratio)'''
    def setPixelAspectRatio(self, width, height):
        '''void QVideoSurfaceFormat.setPixelAspectRatio(int width, int height)'''
    def pixelAspectRatio(self):
        '''QSize QVideoSurfaceFormat.pixelAspectRatio()'''
        return QSize()
    def setFrameRate(self, rate):
        '''void QVideoSurfaceFormat.setFrameRate(float rate)'''
    def frameRate(self):
        '''float QVideoSurfaceFormat.frameRate()'''
        return float()
    def setScanLineDirection(self, direction):
        '''void QVideoSurfaceFormat.setScanLineDirection(QVideoSurfaceFormat.Direction direction)'''
    def scanLineDirection(self):
        '''QVideoSurfaceFormat.Direction QVideoSurfaceFormat.scanLineDirection()'''
        return QVideoSurfaceFormat.Direction()
    def setViewport(self, viewport):
        '''void QVideoSurfaceFormat.setViewport(QRect viewport)'''
    def viewport(self):
        '''QRect QVideoSurfaceFormat.viewport()'''
        return QRect()
    def frameHeight(self):
        '''int QVideoSurfaceFormat.frameHeight()'''
        return int()
    def frameWidth(self):
        '''int QVideoSurfaceFormat.frameWidth()'''
        return int()
    def setFrameSize(self, size):
        '''void QVideoSurfaceFormat.setFrameSize(QSize size)'''
    def setFrameSize(self, width, height):
        '''void QVideoSurfaceFormat.setFrameSize(int width, int height)'''
    def frameSize(self):
        '''QSize QVideoSurfaceFormat.frameSize()'''
        return QSize()
    def handleType(self):
        '''QAbstractVideoBuffer.HandleType QVideoSurfaceFormat.handleType()'''
        return QAbstractVideoBuffer.HandleType()
    def pixelFormat(self):
        '''QVideoFrame.PixelFormat QVideoSurfaceFormat.pixelFormat()'''
        return QVideoFrame.PixelFormat()
    def isValid(self):
        '''bool QVideoSurfaceFormat.isValid()'''
        return bool()
    def __ne__(self, format):
        '''bool QVideoSurfaceFormat.__ne__(QVideoSurfaceFormat format)'''
        return bool()
    def __eq__(self, format):
        '''bool QVideoSurfaceFormat.__eq__(QVideoSurfaceFormat format)'''
        return bool()


