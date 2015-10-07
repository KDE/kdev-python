class pyqtSignal():
 def connect(self, targetSignal): pass
 def emit(self, *args): pass
from QtCore import *

from QtWidgets import *

import datetime

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
    EGLImageHandle = 0
    UserHandle = 0

    def __init__(self, type):
        '''void QAbstractVideoBuffer.__init__(QAbstractVideoBuffer.HandleType type)'''
    def release(self):
        '''void QAbstractVideoBuffer.release()'''
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


class QVideoFilterRunnable():
    """"""
    # Enum QVideoFilterRunnable.RunFlag
    LastInChain = 0

    def __init__(self):
        '''void QVideoFilterRunnable.__init__()'''
    def __init__(self):
        '''QVideoFilterRunnable QVideoFilterRunnable.__init__()'''
        return QVideoFilterRunnable()
    def run(self, input, surfaceFormat, flags):
        '''abstract QVideoFrame QVideoFilterRunnable.run(QVideoFrame input, QVideoSurfaceFormat surfaceFormat, QVideoFilterRunnable.RunFlags flags)'''
        return QVideoFrame()
    class RunFlags():
        """"""
        def __init__(self):
            '''QVideoFilterRunnable.RunFlags QVideoFilterRunnable.RunFlags.__init__()'''
            return QVideoFilterRunnable.RunFlags()
        def __init__(self):
            '''int QVideoFilterRunnable.RunFlags.__init__()'''
            return int()
        def __init__(self):
            '''void QVideoFilterRunnable.RunFlags.__init__()'''
        def __bool__(self):
            '''int QVideoFilterRunnable.RunFlags.__bool__()'''
            return int()
        def __ne__(self, f):
            '''bool QVideoFilterRunnable.RunFlags.__ne__(QVideoFilterRunnable.RunFlags f)'''
            return bool()
        def __eq__(self, f):
            '''bool QVideoFilterRunnable.RunFlags.__eq__(QVideoFilterRunnable.RunFlags f)'''
            return bool()
        def __invert__(self):
            '''QVideoFilterRunnable.RunFlags QVideoFilterRunnable.RunFlags.__invert__()'''
            return QVideoFilterRunnable.RunFlags()
        def __and__(self, mask):
            '''QVideoFilterRunnable.RunFlags QVideoFilterRunnable.RunFlags.__and__(int mask)'''
            return QVideoFilterRunnable.RunFlags()
        def __xor__(self, f):
            '''QVideoFilterRunnable.RunFlags QVideoFilterRunnable.RunFlags.__xor__(QVideoFilterRunnable.RunFlags f)'''
            return QVideoFilterRunnable.RunFlags()
        def __xor__(self, f):
            '''QVideoFilterRunnable.RunFlags QVideoFilterRunnable.RunFlags.__xor__(int f)'''
            return QVideoFilterRunnable.RunFlags()
        def __or__(self, f):
            '''QVideoFilterRunnable.RunFlags QVideoFilterRunnable.RunFlags.__or__(QVideoFilterRunnable.RunFlags f)'''
            return QVideoFilterRunnable.RunFlags()
        def __or__(self, f):
            '''QVideoFilterRunnable.RunFlags QVideoFilterRunnable.RunFlags.__or__(int f)'''
            return QVideoFilterRunnable.RunFlags()
        def __int__(self):
            '''int QVideoFilterRunnable.RunFlags.__int__()'''
            return int()
        def __ixor__(self, f):
            '''QVideoFilterRunnable.RunFlags QVideoFilterRunnable.RunFlags.__ixor__(QVideoFilterRunnable.RunFlags f)'''
            return QVideoFilterRunnable.RunFlags()
        def __ior__(self, f):
            '''QVideoFilterRunnable.RunFlags QVideoFilterRunnable.RunFlags.__ior__(QVideoFilterRunnable.RunFlags f)'''
            return QVideoFilterRunnable.RunFlags()
        def __iand__(self, mask):
            '''QVideoFilterRunnable.RunFlags QVideoFilterRunnable.RunFlags.__iand__(int mask)'''
            return QVideoFilterRunnable.RunFlags()


class QAbstractVideoFilter(QObject):
    """"""
    def __init__(self, parent = None):
        '''void QAbstractVideoFilter.__init__(QObject parent = None)'''
    activeChanged = pyqtSignal() # void activeChanged() - signal
    def createFilterRunnable(self):
        '''abstract QVideoFilterRunnable QAbstractVideoFilter.createFilterRunnable()'''
        return QVideoFilterRunnable()
    def isActive(self):
        '''bool QAbstractVideoFilter.isActive()'''
        return bool()


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
    nativeResolutionChanged = pyqtSignal() # void nativeResolutionChanged(const QSizeamp;) - signal
    def setNativeResolution(self, resolution):
        '''void QAbstractVideoSurface.setNativeResolution(QSize resolution)'''
    def nativeResolution(self):
        '''QSize QAbstractVideoSurface.nativeResolution()'''
        return QSize()
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



class QAudioBuffer():
    """"""
    def __init__(self):
        '''void QAudioBuffer.__init__()'''
    def __init__(self, data, format, startTime = None):
        '''void QAudioBuffer.__init__(QByteArray data, QAudioFormat format, int startTime = -1)'''
    def __init__(self, numFrames, format, startTime = None):
        '''void QAudioBuffer.__init__(int numFrames, QAudioFormat format, int startTime = -1)'''
    def __init__(self, other):
        '''void QAudioBuffer.__init__(QAudioBuffer other)'''
    def data(self):
        '''sip.voidptr QAudioBuffer.data()'''
        return sip.voidptr()
    def constData(self):
        '''sip.voidptr QAudioBuffer.constData()'''
        return sip.voidptr()
    def startTime(self):
        '''int QAudioBuffer.startTime()'''
        return int()
    def duration(self):
        '''int QAudioBuffer.duration()'''
        return int()
    def byteCount(self):
        '''int QAudioBuffer.byteCount()'''
        return int()
    def sampleCount(self):
        '''int QAudioBuffer.sampleCount()'''
        return int()
    def frameCount(self):
        '''int QAudioBuffer.frameCount()'''
        return int()
    def format(self):
        '''QAudioFormat QAudioBuffer.format()'''
        return QAudioFormat()
    def isValid(self):
        '''bool QAudioBuffer.isValid()'''
        return bool()


class QMediaObject(QObject):
    """"""
    def __init__(self, parent, service):
        '''void QMediaObject.__init__(QObject parent, QMediaService service)'''
    def removePropertyWatch(self, name):
        '''void QMediaObject.removePropertyWatch(QByteArray name)'''
    def addPropertyWatch(self, name):
        '''void QMediaObject.addPropertyWatch(QByteArray name)'''
    availabilityChanged = pyqtSignal() # void availabilityChanged(QMultimedia::AvailabilityStatus) - signal
    metaDataChanged = pyqtSignal() # void metaDataChanged() - signal
    metaDataChanged = pyqtSignal() # void metaDataChanged(const QStringamp;,const QVariantamp;) - signal
    metaDataAvailableChanged = pyqtSignal() # void metaDataAvailableChanged(bool) - signal
    notifyIntervalChanged = pyqtSignal() # void notifyIntervalChanged(int) - signal
    def availableMetaData(self):
        '''list-of-str QMediaObject.availableMetaData()'''
        return [str()]
    def metaData(self, key):
        '''QVariant QMediaObject.metaData(str key)'''
        return QVariant()
    def isMetaDataAvailable(self):
        '''bool QMediaObject.isMetaDataAvailable()'''
        return bool()
    def unbind(self):
        '''QObject QMediaObject.unbind()'''
        return QObject()
    def bind(self):
        '''QObject QMediaObject.bind()'''
        return QObject()
    def setNotifyInterval(self, milliSeconds):
        '''void QMediaObject.setNotifyInterval(int milliSeconds)'''
    def notifyInterval(self):
        '''int QMediaObject.notifyInterval()'''
        return int()
    def service(self):
        '''QMediaService QMediaObject.service()'''
        return QMediaService()
    def availability(self):
        '''QMultimedia.AvailabilityStatus QMediaObject.availability()'''
        return QMultimedia.AvailabilityStatus()
    def isAvailable(self):
        '''bool QMediaObject.isAvailable()'''
        return bool()


class QAudioDecoder(QMediaObject):
    """"""
    # Enum QAudioDecoder.Error
    NoError = 0
    ResourceError = 0
    FormatError = 0
    AccessDeniedError = 0
    ServiceMissingError = 0

    # Enum QAudioDecoder.State
    StoppedState = 0
    DecodingState = 0

    def __init__(self, parent = None):
        '''void QAudioDecoder.__init__(QObject parent = None)'''
    def unbind(self):
        '''QObject QAudioDecoder.unbind()'''
        return QObject()
    def bind(self):
        '''QObject QAudioDecoder.bind()'''
        return QObject()
    durationChanged = pyqtSignal() # void durationChanged(qint64) - signal
    positionChanged = pyqtSignal() # void positionChanged(qint64) - signal
    sourceChanged = pyqtSignal() # void sourceChanged() - signal
    formatChanged = pyqtSignal() # void formatChanged(const QAudioFormatamp;) - signal
    stateChanged = pyqtSignal() # void stateChanged(QAudioDecoder::State) - signal
    finished = pyqtSignal() # void finished() - signal
    bufferReady = pyqtSignal() # void bufferReady() - signal
    bufferAvailableChanged = pyqtSignal() # void bufferAvailableChanged(bool) - signal
    def stop(self):
        '''void QAudioDecoder.stop()'''
    def start(self):
        '''void QAudioDecoder.start()'''
    def duration(self):
        '''int QAudioDecoder.duration()'''
        return int()
    def position(self):
        '''int QAudioDecoder.position()'''
        return int()
    def bufferAvailable(self):
        '''bool QAudioDecoder.bufferAvailable()'''
        return bool()
    def read(self):
        '''QAudioBuffer QAudioDecoder.read()'''
        return QAudioBuffer()
    def errorString(self):
        '''str QAudioDecoder.errorString()'''
        return str()
    def error(self):
        '''QAudioDecoder.Error QAudioDecoder.error()'''
        return QAudioDecoder.Error()
    error = pyqtSignal() # void error(QAudioDecoder::Error) - signal
    def setAudioFormat(self, format):
        '''void QAudioDecoder.setAudioFormat(QAudioFormat format)'''
    def audioFormat(self):
        '''QAudioFormat QAudioDecoder.audioFormat()'''
        return QAudioFormat()
    def setSourceDevice(self, device):
        '''void QAudioDecoder.setSourceDevice(QIODevice device)'''
    def sourceDevice(self):
        '''QIODevice QAudioDecoder.sourceDevice()'''
        return QIODevice()
    def setSourceFilename(self, fileName):
        '''void QAudioDecoder.setSourceFilename(str fileName)'''
    def sourceFilename(self):
        '''str QAudioDecoder.sourceFilename()'''
        return str()
    def state(self):
        '''QAudioDecoder.State QAudioDecoder.state()'''
        return QAudioDecoder.State()
    def hasSupport(self, mimeType, codecs = strList()):
        '''static QMultimedia.SupportEstimate QAudioDecoder.hasSupport(str mimeType, list-of-str codecs = strList())'''
        return QMultimedia.SupportEstimate()


class QAudioDeviceInfo():
    """"""
    def __init__(self):
        '''void QAudioDeviceInfo.__init__()'''
    def __init__(self, other):
        '''void QAudioDeviceInfo.__init__(QAudioDeviceInfo other)'''
    def __ne__(self, other):
        '''bool QAudioDeviceInfo.__ne__(QAudioDeviceInfo other)'''
        return bool()
    def __eq__(self, other):
        '''bool QAudioDeviceInfo.__eq__(QAudioDeviceInfo other)'''
        return bool()
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
    def supportedCodecs(self):
        '''list-of-str QAudioDeviceInfo.supportedCodecs()'''
        return [str()]
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
        '''str QAudioDeviceInfo.deviceName()'''
        return str()
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
    def bytesPerFrame(self):
        '''int QAudioFormat.bytesPerFrame()'''
        return int()
    def durationForFrames(self, frameCount):
        '''int QAudioFormat.durationForFrames(int frameCount)'''
        return int()
    def framesForDuration(self, duration):
        '''int QAudioFormat.framesForDuration(int duration)'''
        return int()
    def framesForBytes(self, byteCount):
        '''int QAudioFormat.framesForBytes(int byteCount)'''
        return int()
    def bytesForFrames(self, frameCount):
        '''int QAudioFormat.bytesForFrames(int frameCount)'''
        return int()
    def durationForBytes(self, byteCount):
        '''int QAudioFormat.durationForBytes(int byteCount)'''
        return int()
    def bytesForDuration(self, duration):
        '''int QAudioFormat.bytesForDuration(int duration)'''
        return int()
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
        '''str QAudioFormat.codec()'''
        return str()
    def setCodec(self, codec):
        '''void QAudioFormat.setCodec(str codec)'''
    def sampleSize(self):
        '''int QAudioFormat.sampleSize()'''
        return int()
    def setSampleSize(self, sampleSize):
        '''void QAudioFormat.setSampleSize(int sampleSize)'''
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
    def volume(self):
        '''float QAudioInput.volume()'''
        return float()
    def setVolume(self, volume):
        '''void QAudioInput.setVolume(float volume)'''
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
    def setCategory(self, category):
        '''void QAudioOutput.setCategory(str category)'''
    def category(self):
        '''str QAudioOutput.category()'''
        return str()
    def volume(self):
        '''float QAudioOutput.volume()'''
        return float()
    def setVolume(self):
        '''float QAudioOutput.setVolume()'''
        return float()
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


class QAudioProbe(QObject):
    """"""
    def __init__(self, parent = None):
        '''void QAudioProbe.__init__(QObject parent = None)'''
    flush = pyqtSignal() # void flush() - signal
    audioBufferProbed = pyqtSignal() # void audioBufferProbed(const QAudioBufferamp;) - signal
    def isActive(self):
        '''bool QAudioProbe.isActive()'''
        return bool()
    def setSource(self, source):
        '''bool QAudioProbe.setSource(QMediaObject source)'''
        return bool()
    def setSource(self, source):
        '''bool QAudioProbe.setSource(QMediaRecorder source)'''
        return bool()


class QMediaBindableInterface():
    """"""
    def __init__(self):
        '''void QMediaBindableInterface.__init__()'''
    def __init__(self):
        '''QMediaBindableInterface QMediaBindableInterface.__init__()'''
        return QMediaBindableInterface()
    def setMediaObject(self, object):
        '''abstract bool QMediaBindableInterface.setMediaObject(QMediaObject object)'''
        return bool()
    def mediaObject(self):
        '''abstract QMediaObject QMediaBindableInterface.mediaObject()'''
        return QMediaObject()


class QMediaRecorder(QObject, QMediaBindableInterface):
    """"""
    # Enum QMediaRecorder.Error
    NoError = 0
    ResourceError = 0
    FormatError = 0
    OutOfSpaceError = 0

    # Enum QMediaRecorder.Status
    UnavailableStatus = 0
    UnloadedStatus = 0
    LoadingStatus = 0
    LoadedStatus = 0
    StartingStatus = 0
    RecordingStatus = 0
    PausedStatus = 0
    FinalizingStatus = 0

    # Enum QMediaRecorder.State
    StoppedState = 0
    RecordingState = 0
    PausedState = 0

    def __init__(self, mediaObject, parent = None):
        '''void QMediaRecorder.__init__(QMediaObject mediaObject, QObject parent = None)'''
    def setMediaObject(self, object):
        '''bool QMediaRecorder.setMediaObject(QMediaObject object)'''
        return bool()
    availabilityChanged = pyqtSignal() # void availabilityChanged(QMultimedia::AvailabilityStatus) - signal
    metaDataChanged = pyqtSignal() # void metaDataChanged(const QStringamp;,const QVariantamp;) - signal
    metaDataWritableChanged = pyqtSignal() # void metaDataWritableChanged(bool) - signal
    metaDataAvailableChanged = pyqtSignal() # void metaDataAvailableChanged(bool) - signal
    actualLocationChanged = pyqtSignal() # void actualLocationChanged(const QUrlamp;) - signal
    volumeChanged = pyqtSignal() # void volumeChanged(qreal) - signal
    mutedChanged = pyqtSignal() # void mutedChanged(bool) - signal
    durationChanged = pyqtSignal() # void durationChanged(qint64) - signal
    statusChanged = pyqtSignal() # void statusChanged(QMediaRecorder::Status) - signal
    stateChanged = pyqtSignal() # void stateChanged(QMediaRecorder::State) - signal
    def setVolume(self, volume):
        '''void QMediaRecorder.setVolume(float volume)'''
    def setMuted(self, muted):
        '''void QMediaRecorder.setMuted(bool muted)'''
    def stop(self):
        '''void QMediaRecorder.stop()'''
    def pause(self):
        '''void QMediaRecorder.pause()'''
    def record(self):
        '''void QMediaRecorder.record()'''
    def availableMetaData(self):
        '''list-of-str QMediaRecorder.availableMetaData()'''
        return [str()]
    def setMetaData(self, key, value):
        '''void QMediaRecorder.setMetaData(str key, QVariant value)'''
    def metaData(self, key):
        '''QVariant QMediaRecorder.metaData(str key)'''
        return QVariant()
    def isMetaDataWritable(self):
        '''bool QMediaRecorder.isMetaDataWritable()'''
        return bool()
    def isMetaDataAvailable(self):
        '''bool QMediaRecorder.isMetaDataAvailable()'''
        return bool()
    def setEncodingSettings(self, audio, video = QVideoEncoderSettings(), container = str()):
        '''void QMediaRecorder.setEncodingSettings(QAudioEncoderSettings audio, QVideoEncoderSettings video = QVideoEncoderSettings(), str container = str())'''
    def setContainerFormat(self, container):
        '''void QMediaRecorder.setContainerFormat(str container)'''
    def setVideoSettings(self, videoSettings):
        '''void QMediaRecorder.setVideoSettings(QVideoEncoderSettings videoSettings)'''
    def setAudioSettings(self, audioSettings):
        '''void QMediaRecorder.setAudioSettings(QAudioEncoderSettings audioSettings)'''
    def containerFormat(self):
        '''str QMediaRecorder.containerFormat()'''
        return str()
    def videoSettings(self):
        '''QVideoEncoderSettings QMediaRecorder.videoSettings()'''
        return QVideoEncoderSettings()
    def audioSettings(self):
        '''QAudioEncoderSettings QMediaRecorder.audioSettings()'''
        return QAudioEncoderSettings()
    def supportedFrameRates(self, settings = QVideoEncoderSettings(), continuous = None):
        '''list-of-float QMediaRecorder.supportedFrameRates(QVideoEncoderSettings settings = QVideoEncoderSettings(), bool continuous)'''
        return [float()]
    def supportedResolutions(self, settings = QVideoEncoderSettings(), continuous = None):
        '''list-of-QSize QMediaRecorder.supportedResolutions(QVideoEncoderSettings settings = QVideoEncoderSettings(), bool continuous)'''
        return [QSize()]
    def videoCodecDescription(self, codecName):
        '''str QMediaRecorder.videoCodecDescription(str codecName)'''
        return str()
    def supportedVideoCodecs(self):
        '''list-of-str QMediaRecorder.supportedVideoCodecs()'''
        return [str()]
    def supportedAudioSampleRates(self, settings = QAudioEncoderSettings(), continuous = None):
        '''list-of-int QMediaRecorder.supportedAudioSampleRates(QAudioEncoderSettings settings = QAudioEncoderSettings(), bool continuous)'''
        return [int()]
    def audioCodecDescription(self, codecName):
        '''str QMediaRecorder.audioCodecDescription(str codecName)'''
        return str()
    def supportedAudioCodecs(self):
        '''list-of-str QMediaRecorder.supportedAudioCodecs()'''
        return [str()]
    def containerDescription(self, format):
        '''str QMediaRecorder.containerDescription(str format)'''
        return str()
    def supportedContainers(self):
        '''list-of-str QMediaRecorder.supportedContainers()'''
        return [str()]
    def volume(self):
        '''float QMediaRecorder.volume()'''
        return float()
    def isMuted(self):
        '''bool QMediaRecorder.isMuted()'''
        return bool()
    def duration(self):
        '''int QMediaRecorder.duration()'''
        return int()
    def errorString(self):
        '''str QMediaRecorder.errorString()'''
        return str()
    def error(self):
        '''QMediaRecorder.Error QMediaRecorder.error()'''
        return QMediaRecorder.Error()
    error = pyqtSignal() # void error(QMediaRecorder::Error) - signal
    def status(self):
        '''QMediaRecorder.Status QMediaRecorder.status()'''
        return QMediaRecorder.Status()
    def state(self):
        '''QMediaRecorder.State QMediaRecorder.state()'''
        return QMediaRecorder.State()
    def actualLocation(self):
        '''QUrl QMediaRecorder.actualLocation()'''
        return QUrl()
    def setOutputLocation(self, location):
        '''bool QMediaRecorder.setOutputLocation(QUrl location)'''
        return bool()
    def outputLocation(self):
        '''QUrl QMediaRecorder.outputLocation()'''
        return QUrl()
    def availability(self):
        '''QMultimedia.AvailabilityStatus QMediaRecorder.availability()'''
        return QMultimedia.AvailabilityStatus()
    def isAvailable(self):
        '''bool QMediaRecorder.isAvailable()'''
        return bool()
    def mediaObject(self):
        '''QMediaObject QMediaRecorder.mediaObject()'''
        return QMediaObject()


class QAudioRecorder(QMediaRecorder):
    """"""
    def __init__(self, parent = None):
        '''void QAudioRecorder.__init__(QObject parent = None)'''
    availableAudioInputsChanged = pyqtSignal() # void availableAudioInputsChanged() - signal
    audioInputChanged = pyqtSignal() # void audioInputChanged(const QStringamp;) - signal
    def setAudioInput(self, name):
        '''void QAudioRecorder.setAudioInput(str name)'''
    def audioInput(self):
        '''str QAudioRecorder.audioInput()'''
        return str()
    def audioInputDescription(self, name):
        '''str QAudioRecorder.audioInputDescription(str name)'''
        return str()
    def defaultAudioInput(self):
        '''str QAudioRecorder.defaultAudioInput()'''
        return str()
    def audioInputs(self):
        '''list-of-str QAudioRecorder.audioInputs()'''
        return [str()]


class QCamera(QMediaObject):
    """"""
    # Enum QCamera.Position
    UnspecifiedPosition = 0
    BackFace = 0
    FrontFace = 0

    # Enum QCamera.LockType
    NoLock = 0
    LockExposure = 0
    LockWhiteBalance = 0
    LockFocus = 0

    # Enum QCamera.LockChangeReason
    UserRequest = 0
    LockAcquired = 0
    LockFailed = 0
    LockLost = 0
    LockTemporaryLost = 0

    # Enum QCamera.LockStatus
    Unlocked = 0
    Searching = 0
    Locked = 0

    # Enum QCamera.Error
    NoError = 0
    CameraError = 0
    InvalidRequestError = 0
    ServiceMissingError = 0
    NotSupportedFeatureError = 0

    # Enum QCamera.CaptureMode
    CaptureViewfinder = 0
    CaptureStillImage = 0
    CaptureVideo = 0

    # Enum QCamera.State
    UnloadedState = 0
    LoadedState = 0
    ActiveState = 0

    # Enum QCamera.Status
    UnavailableStatus = 0
    UnloadedStatus = 0
    LoadingStatus = 0
    UnloadingStatus = 0
    LoadedStatus = 0
    StandbyStatus = 0
    StartingStatus = 0
    StoppingStatus = 0
    ActiveStatus = 0

    def __init__(self, parent = None):
        '''void QCamera.__init__(QObject parent = None)'''
    def __init__(self, device, parent = None):
        '''void QCamera.__init__(QByteArray device, QObject parent = None)'''
    def __init__(self, cameraInfo, parent = None):
        '''void QCamera.__init__(QCameraInfo cameraInfo, QObject parent = None)'''
    def __init__(self, position, parent = None):
        '''void QCamera.__init__(QCamera.Position position, QObject parent = None)'''
    def supportedViewfinderPixelFormats(self, settings = QCameraViewfinderSettings()):
        '''list-of-QVideoFrame.PixelFormat QCamera.supportedViewfinderPixelFormats(QCameraViewfinderSettings settings = QCameraViewfinderSettings())'''
        return [QVideoFrame.PixelFormat()]
    def supportedViewfinderFrameRateRanges(self, settings = QCameraViewfinderSettings()):
        '''list-of-QCamera.FrameRateRange QCamera.supportedViewfinderFrameRateRanges(QCameraViewfinderSettings settings = QCameraViewfinderSettings())'''
        return [QCamera.FrameRateRange()]
    def supportedViewfinderResolutions(self, settings = QCameraViewfinderSettings()):
        '''list-of-QSize QCamera.supportedViewfinderResolutions(QCameraViewfinderSettings settings = QCameraViewfinderSettings())'''
        return [QSize()]
    def supportedViewfinderSettings(self, settings = QCameraViewfinderSettings()):
        '''list-of-QCameraViewfinderSettings QCamera.supportedViewfinderSettings(QCameraViewfinderSettings settings = QCameraViewfinderSettings())'''
        return [QCameraViewfinderSettings()]
    def setViewfinderSettings(self, settings):
        '''void QCamera.setViewfinderSettings(QCameraViewfinderSettings settings)'''
    def viewfinderSettings(self):
        '''QCameraViewfinderSettings QCamera.viewfinderSettings()'''
        return QCameraViewfinderSettings()
    lockStatusChanged = pyqtSignal() # void lockStatusChanged(QCamera::LockStatus,QCamera::LockChangeReason) - signal
    lockStatusChanged = pyqtSignal() # void lockStatusChanged(QCamera::LockType,QCamera::LockStatus,QCamera::LockChangeReason) - signal
    lockFailed = pyqtSignal() # void lockFailed() - signal
    locked = pyqtSignal() # void locked() - signal
    statusChanged = pyqtSignal() # void statusChanged(QCamera::Status) - signal
    captureModeChanged = pyqtSignal() # void captureModeChanged(QCamera::CaptureModes) - signal
    stateChanged = pyqtSignal() # void stateChanged(QCamera::State) - signal
    def unlock(self):
        '''void QCamera.unlock()'''
    def unlock(self, locks):
        '''void QCamera.unlock(QCamera.LockTypes locks)'''
    def searchAndLock(self):
        '''void QCamera.searchAndLock()'''
    def searchAndLock(self, locks):
        '''void QCamera.searchAndLock(QCamera.LockTypes locks)'''
    def stop(self):
        '''void QCamera.stop()'''
    def start(self):
        '''void QCamera.start()'''
    def unload(self):
        '''void QCamera.unload()'''
    def load(self):
        '''void QCamera.load()'''
    def setCaptureMode(self, mode):
        '''void QCamera.setCaptureMode(QCamera.CaptureModes mode)'''
    def lockStatus(self):
        '''QCamera.LockStatus QCamera.lockStatus()'''
        return QCamera.LockStatus()
    def lockStatus(self, lock):
        '''QCamera.LockStatus QCamera.lockStatus(QCamera.LockType lock)'''
        return QCamera.LockStatus()
    def requestedLocks(self):
        '''QCamera.LockTypes QCamera.requestedLocks()'''
        return QCamera.LockTypes()
    def supportedLocks(self):
        '''QCamera.LockTypes QCamera.supportedLocks()'''
        return QCamera.LockTypes()
    def errorString(self):
        '''str QCamera.errorString()'''
        return str()
    def error(self):
        '''QCamera.Error QCamera.error()'''
        return QCamera.Error()
    error = pyqtSignal() # void error(QCamera::Error) - signal
    def setViewfinder(self, viewfinder):
        '''void QCamera.setViewfinder(QVideoWidget viewfinder)'''
    def setViewfinder(self, viewfinder):
        '''void QCamera.setViewfinder(QGraphicsVideoItem viewfinder)'''
    def setViewfinder(self, surface):
        '''void QCamera.setViewfinder(QAbstractVideoSurface surface)'''
    def imageProcessing(self):
        '''QCameraImageProcessing QCamera.imageProcessing()'''
        return QCameraImageProcessing()
    def focus(self):
        '''QCameraFocus QCamera.focus()'''
        return QCameraFocus()
    def exposure(self):
        '''QCameraExposure QCamera.exposure()'''
        return QCameraExposure()
    def isCaptureModeSupported(self, mode):
        '''bool QCamera.isCaptureModeSupported(QCamera.CaptureModes mode)'''
        return bool()
    def captureMode(self):
        '''QCamera.CaptureModes QCamera.captureMode()'''
        return QCamera.CaptureModes()
    def status(self):
        '''QCamera.Status QCamera.status()'''
        return QCamera.Status()
    def state(self):
        '''QCamera.State QCamera.state()'''
        return QCamera.State()
    def availability(self):
        '''QMultimedia.AvailabilityStatus QCamera.availability()'''
        return QMultimedia.AvailabilityStatus()
    def deviceDescription(self, device):
        '''static str QCamera.deviceDescription(QByteArray device)'''
        return str()
    def availableDevices(self):
        '''static list-of-QByteArray QCamera.availableDevices()'''
        return [QByteArray()]
    class FrameRateRange():
        """"""
        maximumFrameRate = None # float - member
        minimumFrameRate = None # float - member
        def __init__(self, minimum, maximum):
            '''void QCamera.FrameRateRange.__init__(float minimum, float maximum)'''
        def __init__(self):
            '''void QCamera.FrameRateRange.__init__()'''
        def __init__(self):
            '''QCamera.FrameRateRange QCamera.FrameRateRange.__init__()'''
            return QCamera.FrameRateRange()
        def __eq__(self, r2):
            '''bool QCamera.FrameRateRange.__eq__(QCamera.FrameRateRange r2)'''
            return bool()
        def __ne__(self, r2):
            '''bool QCamera.FrameRateRange.__ne__(QCamera.FrameRateRange r2)'''
            return bool()
    class CaptureModes():
        """"""
        def __init__(self):
            '''QCamera.CaptureModes QCamera.CaptureModes.__init__()'''
            return QCamera.CaptureModes()
        def __init__(self):
            '''int QCamera.CaptureModes.__init__()'''
            return int()
        def __init__(self):
            '''void QCamera.CaptureModes.__init__()'''
        def __bool__(self):
            '''int QCamera.CaptureModes.__bool__()'''
            return int()
        def __ne__(self, f):
            '''bool QCamera.CaptureModes.__ne__(QCamera.CaptureModes f)'''
            return bool()
        def __eq__(self, f):
            '''bool QCamera.CaptureModes.__eq__(QCamera.CaptureModes f)'''
            return bool()
        def __invert__(self):
            '''QCamera.CaptureModes QCamera.CaptureModes.__invert__()'''
            return QCamera.CaptureModes()
        def __and__(self, mask):
            '''QCamera.CaptureModes QCamera.CaptureModes.__and__(int mask)'''
            return QCamera.CaptureModes()
        def __xor__(self, f):
            '''QCamera.CaptureModes QCamera.CaptureModes.__xor__(QCamera.CaptureModes f)'''
            return QCamera.CaptureModes()
        def __xor__(self, f):
            '''QCamera.CaptureModes QCamera.CaptureModes.__xor__(int f)'''
            return QCamera.CaptureModes()
        def __or__(self, f):
            '''QCamera.CaptureModes QCamera.CaptureModes.__or__(QCamera.CaptureModes f)'''
            return QCamera.CaptureModes()
        def __or__(self, f):
            '''QCamera.CaptureModes QCamera.CaptureModes.__or__(int f)'''
            return QCamera.CaptureModes()
        def __int__(self):
            '''int QCamera.CaptureModes.__int__()'''
            return int()
        def __ixor__(self, f):
            '''QCamera.CaptureModes QCamera.CaptureModes.__ixor__(QCamera.CaptureModes f)'''
            return QCamera.CaptureModes()
        def __ior__(self, f):
            '''QCamera.CaptureModes QCamera.CaptureModes.__ior__(QCamera.CaptureModes f)'''
            return QCamera.CaptureModes()
        def __iand__(self, mask):
            '''QCamera.CaptureModes QCamera.CaptureModes.__iand__(int mask)'''
            return QCamera.CaptureModes()
    class LockTypes():
        """"""
        def __init__(self):
            '''QCamera.LockTypes QCamera.LockTypes.__init__()'''
            return QCamera.LockTypes()
        def __init__(self):
            '''int QCamera.LockTypes.__init__()'''
            return int()
        def __init__(self):
            '''void QCamera.LockTypes.__init__()'''
        def __bool__(self):
            '''int QCamera.LockTypes.__bool__()'''
            return int()
        def __ne__(self, f):
            '''bool QCamera.LockTypes.__ne__(QCamera.LockTypes f)'''
            return bool()
        def __eq__(self, f):
            '''bool QCamera.LockTypes.__eq__(QCamera.LockTypes f)'''
            return bool()
        def __invert__(self):
            '''QCamera.LockTypes QCamera.LockTypes.__invert__()'''
            return QCamera.LockTypes()
        def __and__(self, mask):
            '''QCamera.LockTypes QCamera.LockTypes.__and__(int mask)'''
            return QCamera.LockTypes()
        def __xor__(self, f):
            '''QCamera.LockTypes QCamera.LockTypes.__xor__(QCamera.LockTypes f)'''
            return QCamera.LockTypes()
        def __xor__(self, f):
            '''QCamera.LockTypes QCamera.LockTypes.__xor__(int f)'''
            return QCamera.LockTypes()
        def __or__(self, f):
            '''QCamera.LockTypes QCamera.LockTypes.__or__(QCamera.LockTypes f)'''
            return QCamera.LockTypes()
        def __or__(self, f):
            '''QCamera.LockTypes QCamera.LockTypes.__or__(int f)'''
            return QCamera.LockTypes()
        def __int__(self):
            '''int QCamera.LockTypes.__int__()'''
            return int()
        def __ixor__(self, f):
            '''QCamera.LockTypes QCamera.LockTypes.__ixor__(QCamera.LockTypes f)'''
            return QCamera.LockTypes()
        def __ior__(self, f):
            '''QCamera.LockTypes QCamera.LockTypes.__ior__(QCamera.LockTypes f)'''
            return QCamera.LockTypes()
        def __iand__(self, mask):
            '''QCamera.LockTypes QCamera.LockTypes.__iand__(int mask)'''
            return QCamera.LockTypes()


class QCameraExposure(QObject):
    """"""
    # Enum QCameraExposure.MeteringMode
    MeteringMatrix = 0
    MeteringAverage = 0
    MeteringSpot = 0

    # Enum QCameraExposure.ExposureMode
    ExposureAuto = 0
    ExposureManual = 0
    ExposurePortrait = 0
    ExposureNight = 0
    ExposureBacklight = 0
    ExposureSpotlight = 0
    ExposureSports = 0
    ExposureSnow = 0
    ExposureBeach = 0
    ExposureLargeAperture = 0
    ExposureSmallAperture = 0
    ExposureAction = 0
    ExposureLandscape = 0
    ExposureNightPortrait = 0
    ExposureTheatre = 0
    ExposureSunset = 0
    ExposureSteadyPhoto = 0
    ExposureFireworks = 0
    ExposureParty = 0
    ExposureCandlelight = 0
    ExposureBarcode = 0
    ExposureModeVendor = 0

    # Enum QCameraExposure.FlashMode
    FlashAuto = 0
    FlashOff = 0
    FlashOn = 0
    FlashRedEyeReduction = 0
    FlashFill = 0
    FlashTorch = 0
    FlashVideoLight = 0
    FlashSlowSyncFrontCurtain = 0
    FlashSlowSyncRearCurtain = 0
    FlashManual = 0

    exposureCompensationChanged = pyqtSignal() # void exposureCompensationChanged(qreal) - signal
    isoSensitivityChanged = pyqtSignal() # void isoSensitivityChanged(int) - signal
    shutterSpeedRangeChanged = pyqtSignal() # void shutterSpeedRangeChanged() - signal
    shutterSpeedChanged = pyqtSignal() # void shutterSpeedChanged(qreal) - signal
    apertureRangeChanged = pyqtSignal() # void apertureRangeChanged() - signal
    apertureChanged = pyqtSignal() # void apertureChanged(qreal) - signal
    flashReady = pyqtSignal() # void flashReady(bool) - signal
    def setAutoShutterSpeed(self):
        '''void QCameraExposure.setAutoShutterSpeed()'''
    def setManualShutterSpeed(self, seconds):
        '''void QCameraExposure.setManualShutterSpeed(float seconds)'''
    def setAutoAperture(self):
        '''void QCameraExposure.setAutoAperture()'''
    def setManualAperture(self, aperture):
        '''void QCameraExposure.setManualAperture(float aperture)'''
    def setAutoIsoSensitivity(self):
        '''void QCameraExposure.setAutoIsoSensitivity()'''
    def setManualIsoSensitivity(self, iso):
        '''void QCameraExposure.setManualIsoSensitivity(int iso)'''
    def setExposureCompensation(self, ev):
        '''void QCameraExposure.setExposureCompensation(float ev)'''
    def setMeteringMode(self, mode):
        '''void QCameraExposure.setMeteringMode(QCameraExposure.MeteringMode mode)'''
    def setExposureMode(self, mode):
        '''void QCameraExposure.setExposureMode(QCameraExposure.ExposureMode mode)'''
    def setFlashMode(self, mode):
        '''void QCameraExposure.setFlashMode(QCameraExposure.FlashModes mode)'''
    def supportedShutterSpeeds(self, continuous):
        '''list-of-float QCameraExposure.supportedShutterSpeeds(bool continuous)'''
        return [float()]
    def supportedApertures(self, continuous):
        '''list-of-float QCameraExposure.supportedApertures(bool continuous)'''
        return [float()]
    def supportedIsoSensitivities(self, continuous):
        '''list-of-int QCameraExposure.supportedIsoSensitivities(bool continuous)'''
        return [int()]
    def requestedShutterSpeed(self):
        '''float QCameraExposure.requestedShutterSpeed()'''
        return float()
    def requestedAperture(self):
        '''float QCameraExposure.requestedAperture()'''
        return float()
    def requestedIsoSensitivity(self):
        '''int QCameraExposure.requestedIsoSensitivity()'''
        return int()
    def shutterSpeed(self):
        '''float QCameraExposure.shutterSpeed()'''
        return float()
    def aperture(self):
        '''float QCameraExposure.aperture()'''
        return float()
    def isoSensitivity(self):
        '''int QCameraExposure.isoSensitivity()'''
        return int()
    def setSpotMeteringPoint(self, point):
        '''void QCameraExposure.setSpotMeteringPoint(QPointF point)'''
    def spotMeteringPoint(self):
        '''QPointF QCameraExposure.spotMeteringPoint()'''
        return QPointF()
    def isMeteringModeSupported(self, mode):
        '''bool QCameraExposure.isMeteringModeSupported(QCameraExposure.MeteringMode mode)'''
        return bool()
    def meteringMode(self):
        '''QCameraExposure.MeteringMode QCameraExposure.meteringMode()'''
        return QCameraExposure.MeteringMode()
    def exposureCompensation(self):
        '''float QCameraExposure.exposureCompensation()'''
        return float()
    def isExposureModeSupported(self, mode):
        '''bool QCameraExposure.isExposureModeSupported(QCameraExposure.ExposureMode mode)'''
        return bool()
    def exposureMode(self):
        '''QCameraExposure.ExposureMode QCameraExposure.exposureMode()'''
        return QCameraExposure.ExposureMode()
    def isFlashReady(self):
        '''bool QCameraExposure.isFlashReady()'''
        return bool()
    def isFlashModeSupported(self, mode):
        '''bool QCameraExposure.isFlashModeSupported(QCameraExposure.FlashModes mode)'''
        return bool()
    def flashMode(self):
        '''QCameraExposure.FlashModes QCameraExposure.flashMode()'''
        return QCameraExposure.FlashModes()
    def isAvailable(self):
        '''bool QCameraExposure.isAvailable()'''
        return bool()
    class FlashModes():
        """"""
        def __init__(self):
            '''QCameraExposure.FlashModes QCameraExposure.FlashModes.__init__()'''
            return QCameraExposure.FlashModes()
        def __init__(self):
            '''int QCameraExposure.FlashModes.__init__()'''
            return int()
        def __init__(self):
            '''void QCameraExposure.FlashModes.__init__()'''
        def __bool__(self):
            '''int QCameraExposure.FlashModes.__bool__()'''
            return int()
        def __ne__(self, f):
            '''bool QCameraExposure.FlashModes.__ne__(QCameraExposure.FlashModes f)'''
            return bool()
        def __eq__(self, f):
            '''bool QCameraExposure.FlashModes.__eq__(QCameraExposure.FlashModes f)'''
            return bool()
        def __invert__(self):
            '''QCameraExposure.FlashModes QCameraExposure.FlashModes.__invert__()'''
            return QCameraExposure.FlashModes()
        def __and__(self, mask):
            '''QCameraExposure.FlashModes QCameraExposure.FlashModes.__and__(int mask)'''
            return QCameraExposure.FlashModes()
        def __xor__(self, f):
            '''QCameraExposure.FlashModes QCameraExposure.FlashModes.__xor__(QCameraExposure.FlashModes f)'''
            return QCameraExposure.FlashModes()
        def __xor__(self, f):
            '''QCameraExposure.FlashModes QCameraExposure.FlashModes.__xor__(int f)'''
            return QCameraExposure.FlashModes()
        def __or__(self, f):
            '''QCameraExposure.FlashModes QCameraExposure.FlashModes.__or__(QCameraExposure.FlashModes f)'''
            return QCameraExposure.FlashModes()
        def __or__(self, f):
            '''QCameraExposure.FlashModes QCameraExposure.FlashModes.__or__(int f)'''
            return QCameraExposure.FlashModes()
        def __int__(self):
            '''int QCameraExposure.FlashModes.__int__()'''
            return int()
        def __ixor__(self, f):
            '''QCameraExposure.FlashModes QCameraExposure.FlashModes.__ixor__(QCameraExposure.FlashModes f)'''
            return QCameraExposure.FlashModes()
        def __ior__(self, f):
            '''QCameraExposure.FlashModes QCameraExposure.FlashModes.__ior__(QCameraExposure.FlashModes f)'''
            return QCameraExposure.FlashModes()
        def __iand__(self, mask):
            '''QCameraExposure.FlashModes QCameraExposure.FlashModes.__iand__(int mask)'''
            return QCameraExposure.FlashModes()


class QCameraFocusZone():
    """"""
    # Enum QCameraFocusZone.FocusZoneStatus
    Invalid = 0
    Unused = 0
    Selected = 0
    Focused = 0

    def __init__(self, other):
        '''void QCameraFocusZone.__init__(QCameraFocusZone other)'''
    def status(self):
        '''QCameraFocusZone.FocusZoneStatus QCameraFocusZone.status()'''
        return QCameraFocusZone.FocusZoneStatus()
    def area(self):
        '''QRectF QCameraFocusZone.area()'''
        return QRectF()
    def isValid(self):
        '''bool QCameraFocusZone.isValid()'''
        return bool()
    def __ne__(self, other):
        '''bool QCameraFocusZone.__ne__(QCameraFocusZone other)'''
        return bool()
    def __eq__(self, other):
        '''bool QCameraFocusZone.__eq__(QCameraFocusZone other)'''
        return bool()


class QCameraFocus(QObject):
    """"""
    # Enum QCameraFocus.FocusPointMode
    FocusPointAuto = 0
    FocusPointCenter = 0
    FocusPointFaceDetection = 0
    FocusPointCustom = 0

    # Enum QCameraFocus.FocusMode
    ManualFocus = 0
    HyperfocalFocus = 0
    InfinityFocus = 0
    AutoFocus = 0
    ContinuousFocus = 0
    MacroFocus = 0

    maximumDigitalZoomChanged = pyqtSignal() # void maximumDigitalZoomChanged(qreal) - signal
    maximumOpticalZoomChanged = pyqtSignal() # void maximumOpticalZoomChanged(qreal) - signal
    focusZonesChanged = pyqtSignal() # void focusZonesChanged() - signal
    digitalZoomChanged = pyqtSignal() # void digitalZoomChanged(qreal) - signal
    opticalZoomChanged = pyqtSignal() # void opticalZoomChanged(qreal) - signal
    def zoomTo(self, opticalZoom, digitalZoom):
        '''void QCameraFocus.zoomTo(float opticalZoom, float digitalZoom)'''
    def digitalZoom(self):
        '''float QCameraFocus.digitalZoom()'''
        return float()
    def opticalZoom(self):
        '''float QCameraFocus.opticalZoom()'''
        return float()
    def maximumDigitalZoom(self):
        '''float QCameraFocus.maximumDigitalZoom()'''
        return float()
    def maximumOpticalZoom(self):
        '''float QCameraFocus.maximumOpticalZoom()'''
        return float()
    def focusZones(self):
        '''list-of-QCameraFocusZone QCameraFocus.focusZones()'''
        return [QCameraFocusZone()]
    def setCustomFocusPoint(self, point):
        '''void QCameraFocus.setCustomFocusPoint(QPointF point)'''
    def customFocusPoint(self):
        '''QPointF QCameraFocus.customFocusPoint()'''
        return QPointF()
    def isFocusPointModeSupported(self):
        '''QCameraFocus.FocusPointMode QCameraFocus.isFocusPointModeSupported()'''
        return QCameraFocus.FocusPointMode()
    def setFocusPointMode(self, mode):
        '''void QCameraFocus.setFocusPointMode(QCameraFocus.FocusPointMode mode)'''
    def focusPointMode(self):
        '''QCameraFocus.FocusPointMode QCameraFocus.focusPointMode()'''
        return QCameraFocus.FocusPointMode()
    def isFocusModeSupported(self, mode):
        '''bool QCameraFocus.isFocusModeSupported(QCameraFocus.FocusModes mode)'''
        return bool()
    def setFocusMode(self, mode):
        '''void QCameraFocus.setFocusMode(QCameraFocus.FocusModes mode)'''
    def focusMode(self):
        '''QCameraFocus.FocusModes QCameraFocus.focusMode()'''
        return QCameraFocus.FocusModes()
    def isAvailable(self):
        '''bool QCameraFocus.isAvailable()'''
        return bool()
    class FocusModes():
        """"""
        def __init__(self):
            '''QCameraFocus.FocusModes QCameraFocus.FocusModes.__init__()'''
            return QCameraFocus.FocusModes()
        def __init__(self):
            '''int QCameraFocus.FocusModes.__init__()'''
            return int()
        def __init__(self):
            '''void QCameraFocus.FocusModes.__init__()'''
        def __bool__(self):
            '''int QCameraFocus.FocusModes.__bool__()'''
            return int()
        def __ne__(self, f):
            '''bool QCameraFocus.FocusModes.__ne__(QCameraFocus.FocusModes f)'''
            return bool()
        def __eq__(self, f):
            '''bool QCameraFocus.FocusModes.__eq__(QCameraFocus.FocusModes f)'''
            return bool()
        def __invert__(self):
            '''QCameraFocus.FocusModes QCameraFocus.FocusModes.__invert__()'''
            return QCameraFocus.FocusModes()
        def __and__(self, mask):
            '''QCameraFocus.FocusModes QCameraFocus.FocusModes.__and__(int mask)'''
            return QCameraFocus.FocusModes()
        def __xor__(self, f):
            '''QCameraFocus.FocusModes QCameraFocus.FocusModes.__xor__(QCameraFocus.FocusModes f)'''
            return QCameraFocus.FocusModes()
        def __xor__(self, f):
            '''QCameraFocus.FocusModes QCameraFocus.FocusModes.__xor__(int f)'''
            return QCameraFocus.FocusModes()
        def __or__(self, f):
            '''QCameraFocus.FocusModes QCameraFocus.FocusModes.__or__(QCameraFocus.FocusModes f)'''
            return QCameraFocus.FocusModes()
        def __or__(self, f):
            '''QCameraFocus.FocusModes QCameraFocus.FocusModes.__or__(int f)'''
            return QCameraFocus.FocusModes()
        def __int__(self):
            '''int QCameraFocus.FocusModes.__int__()'''
            return int()
        def __ixor__(self, f):
            '''QCameraFocus.FocusModes QCameraFocus.FocusModes.__ixor__(QCameraFocus.FocusModes f)'''
            return QCameraFocus.FocusModes()
        def __ior__(self, f):
            '''QCameraFocus.FocusModes QCameraFocus.FocusModes.__ior__(QCameraFocus.FocusModes f)'''
            return QCameraFocus.FocusModes()
        def __iand__(self, mask):
            '''QCameraFocus.FocusModes QCameraFocus.FocusModes.__iand__(int mask)'''
            return QCameraFocus.FocusModes()


class QCameraImageCapture(QObject, QMediaBindableInterface):
    """"""
    # Enum QCameraImageCapture.CaptureDestination
    CaptureToFile = 0
    CaptureToBuffer = 0

    # Enum QCameraImageCapture.DriveMode
    SingleImageCapture = 0

    # Enum QCameraImageCapture.Error
    NoError = 0
    NotReadyError = 0
    ResourceError = 0
    OutOfSpaceError = 0
    NotSupportedFeatureError = 0
    FormatError = 0

    def __init__(self, mediaObject, parent = None):
        '''void QCameraImageCapture.__init__(QMediaObject mediaObject, QObject parent = None)'''
    def setMediaObject(self):
        '''QMediaObject QCameraImageCapture.setMediaObject()'''
        return QMediaObject()
    imageSaved = pyqtSignal() # void imageSaved(int,const QStringamp;) - signal
    imageAvailable = pyqtSignal() # void imageAvailable(int,const QVideoFrameamp;) - signal
    imageMetadataAvailable = pyqtSignal() # void imageMetadataAvailable(int,const QStringamp;,const QVariantamp;) - signal
    imageCaptured = pyqtSignal() # void imageCaptured(int,const QImageamp;) - signal
    imageExposed = pyqtSignal() # void imageExposed(int) - signal
    captureDestinationChanged = pyqtSignal() # void captureDestinationChanged(QCameraImageCapture::CaptureDestinations) - signal
    bufferFormatChanged = pyqtSignal() # void bufferFormatChanged(QVideoFrame::PixelFormat) - signal
    readyForCaptureChanged = pyqtSignal() # void readyForCaptureChanged(bool) - signal
    def cancelCapture(self):
        '''void QCameraImageCapture.cancelCapture()'''
    def capture(self, file = str()):
        '''int QCameraImageCapture.capture(str file = str())'''
        return int()
    def setCaptureDestination(self, destination):
        '''void QCameraImageCapture.setCaptureDestination(QCameraImageCapture.CaptureDestinations destination)'''
    def captureDestination(self):
        '''QCameraImageCapture.CaptureDestinations QCameraImageCapture.captureDestination()'''
        return QCameraImageCapture.CaptureDestinations()
    def isCaptureDestinationSupported(self, destination):
        '''bool QCameraImageCapture.isCaptureDestinationSupported(QCameraImageCapture.CaptureDestinations destination)'''
        return bool()
    def setBufferFormat(self, format):
        '''void QCameraImageCapture.setBufferFormat(QVideoFrame.PixelFormat format)'''
    def bufferFormat(self):
        '''QVideoFrame.PixelFormat QCameraImageCapture.bufferFormat()'''
        return QVideoFrame.PixelFormat()
    def supportedBufferFormats(self):
        '''list-of-QVideoFrame.PixelFormat QCameraImageCapture.supportedBufferFormats()'''
        return [QVideoFrame.PixelFormat()]
    def setEncodingSettings(self, settings):
        '''void QCameraImageCapture.setEncodingSettings(QImageEncoderSettings settings)'''
    def encodingSettings(self):
        '''QImageEncoderSettings QCameraImageCapture.encodingSettings()'''
        return QImageEncoderSettings()
    def supportedResolutions(self, settings = QImageEncoderSettings(), continuous = None):
        '''list-of-QSize QCameraImageCapture.supportedResolutions(QImageEncoderSettings settings = QImageEncoderSettings(), bool continuous)'''
        return [QSize()]
    def imageCodecDescription(self, codecName):
        '''str QCameraImageCapture.imageCodecDescription(str codecName)'''
        return str()
    def supportedImageCodecs(self):
        '''list-of-str QCameraImageCapture.supportedImageCodecs()'''
        return [str()]
    def isReadyForCapture(self):
        '''bool QCameraImageCapture.isReadyForCapture()'''
        return bool()
    def errorString(self):
        '''str QCameraImageCapture.errorString()'''
        return str()
    def error(self):
        '''QCameraImageCapture.Error QCameraImageCapture.error()'''
        return QCameraImageCapture.Error()
    error = pyqtSignal() # void error(int,QCameraImageCapture::Error,const QStringamp;) - signal
    def mediaObject(self):
        '''QMediaObject QCameraImageCapture.mediaObject()'''
        return QMediaObject()
    def availability(self):
        '''QMultimedia.AvailabilityStatus QCameraImageCapture.availability()'''
        return QMultimedia.AvailabilityStatus()
    def isAvailable(self):
        '''bool QCameraImageCapture.isAvailable()'''
        return bool()
    class CaptureDestinations():
        """"""
        def __init__(self):
            '''QCameraImageCapture.CaptureDestinations QCameraImageCapture.CaptureDestinations.__init__()'''
            return QCameraImageCapture.CaptureDestinations()
        def __init__(self):
            '''int QCameraImageCapture.CaptureDestinations.__init__()'''
            return int()
        def __init__(self):
            '''void QCameraImageCapture.CaptureDestinations.__init__()'''
        def __bool__(self):
            '''int QCameraImageCapture.CaptureDestinations.__bool__()'''
            return int()
        def __ne__(self, f):
            '''bool QCameraImageCapture.CaptureDestinations.__ne__(QCameraImageCapture.CaptureDestinations f)'''
            return bool()
        def __eq__(self, f):
            '''bool QCameraImageCapture.CaptureDestinations.__eq__(QCameraImageCapture.CaptureDestinations f)'''
            return bool()
        def __invert__(self):
            '''QCameraImageCapture.CaptureDestinations QCameraImageCapture.CaptureDestinations.__invert__()'''
            return QCameraImageCapture.CaptureDestinations()
        def __and__(self, mask):
            '''QCameraImageCapture.CaptureDestinations QCameraImageCapture.CaptureDestinations.__and__(int mask)'''
            return QCameraImageCapture.CaptureDestinations()
        def __xor__(self, f):
            '''QCameraImageCapture.CaptureDestinations QCameraImageCapture.CaptureDestinations.__xor__(QCameraImageCapture.CaptureDestinations f)'''
            return QCameraImageCapture.CaptureDestinations()
        def __xor__(self, f):
            '''QCameraImageCapture.CaptureDestinations QCameraImageCapture.CaptureDestinations.__xor__(int f)'''
            return QCameraImageCapture.CaptureDestinations()
        def __or__(self, f):
            '''QCameraImageCapture.CaptureDestinations QCameraImageCapture.CaptureDestinations.__or__(QCameraImageCapture.CaptureDestinations f)'''
            return QCameraImageCapture.CaptureDestinations()
        def __or__(self, f):
            '''QCameraImageCapture.CaptureDestinations QCameraImageCapture.CaptureDestinations.__or__(int f)'''
            return QCameraImageCapture.CaptureDestinations()
        def __int__(self):
            '''int QCameraImageCapture.CaptureDestinations.__int__()'''
            return int()
        def __ixor__(self, f):
            '''QCameraImageCapture.CaptureDestinations QCameraImageCapture.CaptureDestinations.__ixor__(QCameraImageCapture.CaptureDestinations f)'''
            return QCameraImageCapture.CaptureDestinations()
        def __ior__(self, f):
            '''QCameraImageCapture.CaptureDestinations QCameraImageCapture.CaptureDestinations.__ior__(QCameraImageCapture.CaptureDestinations f)'''
            return QCameraImageCapture.CaptureDestinations()
        def __iand__(self, mask):
            '''QCameraImageCapture.CaptureDestinations QCameraImageCapture.CaptureDestinations.__iand__(int mask)'''
            return QCameraImageCapture.CaptureDestinations()


class QCameraImageProcessing(QObject):
    """"""
    # Enum QCameraImageProcessing.ColorFilter
    ColorFilterNone = 0
    ColorFilterGrayscale = 0
    ColorFilterNegative = 0
    ColorFilterSolarize = 0
    ColorFilterSepia = 0
    ColorFilterPosterize = 0
    ColorFilterWhiteboard = 0
    ColorFilterBlackboard = 0
    ColorFilterAqua = 0
    ColorFilterVendor = 0

    # Enum QCameraImageProcessing.WhiteBalanceMode
    WhiteBalanceAuto = 0
    WhiteBalanceManual = 0
    WhiteBalanceSunlight = 0
    WhiteBalanceCloudy = 0
    WhiteBalanceShade = 0
    WhiteBalanceTungsten = 0
    WhiteBalanceFluorescent = 0
    WhiteBalanceFlash = 0
    WhiteBalanceSunset = 0
    WhiteBalanceVendor = 0

    def isColorFilterSupported(self, filter):
        '''bool QCameraImageProcessing.isColorFilterSupported(QCameraImageProcessing.ColorFilter filter)'''
        return bool()
    def setColorFilter(self, filter):
        '''void QCameraImageProcessing.setColorFilter(QCameraImageProcessing.ColorFilter filter)'''
    def colorFilter(self):
        '''QCameraImageProcessing.ColorFilter QCameraImageProcessing.colorFilter()'''
        return QCameraImageProcessing.ColorFilter()
    def setDenoisingLevel(self, value):
        '''void QCameraImageProcessing.setDenoisingLevel(float value)'''
    def denoisingLevel(self):
        '''float QCameraImageProcessing.denoisingLevel()'''
        return float()
    def setSharpeningLevel(self, value):
        '''void QCameraImageProcessing.setSharpeningLevel(float value)'''
    def sharpeningLevel(self):
        '''float QCameraImageProcessing.sharpeningLevel()'''
        return float()
    def setSaturation(self, value):
        '''void QCameraImageProcessing.setSaturation(float value)'''
    def saturation(self):
        '''float QCameraImageProcessing.saturation()'''
        return float()
    def setContrast(self, value):
        '''void QCameraImageProcessing.setContrast(float value)'''
    def contrast(self):
        '''float QCameraImageProcessing.contrast()'''
        return float()
    def setManualWhiteBalance(self, colorTemperature):
        '''void QCameraImageProcessing.setManualWhiteBalance(float colorTemperature)'''
    def manualWhiteBalance(self):
        '''float QCameraImageProcessing.manualWhiteBalance()'''
        return float()
    def isWhiteBalanceModeSupported(self, mode):
        '''bool QCameraImageProcessing.isWhiteBalanceModeSupported(QCameraImageProcessing.WhiteBalanceMode mode)'''
        return bool()
    def setWhiteBalanceMode(self, mode):
        '''void QCameraImageProcessing.setWhiteBalanceMode(QCameraImageProcessing.WhiteBalanceMode mode)'''
    def whiteBalanceMode(self):
        '''QCameraImageProcessing.WhiteBalanceMode QCameraImageProcessing.whiteBalanceMode()'''
        return QCameraImageProcessing.WhiteBalanceMode()
    def isAvailable(self):
        '''bool QCameraImageProcessing.isAvailable()'''
        return bool()


class QCameraInfo():
    """"""
    def __init__(self, name = QByteArray()):
        '''void QCameraInfo.__init__(QByteArray name = QByteArray())'''
    def __init__(self, camera):
        '''void QCameraInfo.__init__(QCamera camera)'''
    def __init__(self, other):
        '''void QCameraInfo.__init__(QCameraInfo other)'''
    def __ne__(self, other):
        '''bool QCameraInfo.__ne__(QCameraInfo other)'''
        return bool()
    def __eq__(self, other):
        '''bool QCameraInfo.__eq__(QCameraInfo other)'''
        return bool()
    def availableCameras(self, position = None):
        '''static list-of-QCameraInfo QCameraInfo.availableCameras(QCamera.Position position = QCamera.UnspecifiedPosition)'''
        return [QCameraInfo()]
    def defaultCamera(self):
        '''static QCameraInfo QCameraInfo.defaultCamera()'''
        return QCameraInfo()
    def orientation(self):
        '''int QCameraInfo.orientation()'''
        return int()
    def position(self):
        '''QCamera.Position QCameraInfo.position()'''
        return QCamera.Position()
    def description(self):
        '''str QCameraInfo.description()'''
        return str()
    def deviceName(self):
        '''str QCameraInfo.deviceName()'''
        return str()
    def isNull(self):
        '''bool QCameraInfo.isNull()'''
        return bool()


class QCameraViewfinderSettings():
    """"""
    def __init__(self):
        '''void QCameraViewfinderSettings.__init__()'''
    def __init__(self, other):
        '''void QCameraViewfinderSettings.__init__(QCameraViewfinderSettings other)'''
    def __eq__(self, rhs):
        '''bool QCameraViewfinderSettings.__eq__(QCameraViewfinderSettings rhs)'''
        return bool()
    def __ne__(self, rhs):
        '''bool QCameraViewfinderSettings.__ne__(QCameraViewfinderSettings rhs)'''
        return bool()
    def setPixelAspectRatio(self, ratio):
        '''void QCameraViewfinderSettings.setPixelAspectRatio(QSize ratio)'''
    def setPixelAspectRatio(self, horizontal, vertical):
        '''void QCameraViewfinderSettings.setPixelAspectRatio(int horizontal, int vertical)'''
    def pixelAspectRatio(self):
        '''QSize QCameraViewfinderSettings.pixelAspectRatio()'''
        return QSize()
    def setPixelFormat(self, format):
        '''void QCameraViewfinderSettings.setPixelFormat(QVideoFrame.PixelFormat format)'''
    def pixelFormat(self):
        '''QVideoFrame.PixelFormat QCameraViewfinderSettings.pixelFormat()'''
        return QVideoFrame.PixelFormat()
    def setMaximumFrameRate(self, rate):
        '''void QCameraViewfinderSettings.setMaximumFrameRate(float rate)'''
    def maximumFrameRate(self):
        '''float QCameraViewfinderSettings.maximumFrameRate()'''
        return float()
    def setMinimumFrameRate(self, rate):
        '''void QCameraViewfinderSettings.setMinimumFrameRate(float rate)'''
    def minimumFrameRate(self):
        '''float QCameraViewfinderSettings.minimumFrameRate()'''
        return float()
    def setResolution(self):
        '''QSize QCameraViewfinderSettings.setResolution()'''
        return QSize()
    def setResolution(self, width, height):
        '''void QCameraViewfinderSettings.setResolution(int width, int height)'''
    def resolution(self):
        '''QSize QCameraViewfinderSettings.resolution()'''
        return QSize()
    def isNull(self):
        '''bool QCameraViewfinderSettings.isNull()'''
        return bool()
    def swap(self, other):
        '''void QCameraViewfinderSettings.swap(QCameraViewfinderSettings other)'''


class QMediaContent():
    """"""
    def __init__(self):
        '''void QMediaContent.__init__()'''
    def __init__(self, contentUrl):
        '''void QMediaContent.__init__(QUrl contentUrl)'''
    def __init__(self, contentRequest):
        '''void QMediaContent.__init__(QNetworkRequest contentRequest)'''
    def __init__(self, contentResource):
        '''void QMediaContent.__init__(QMediaResource contentResource)'''
    def __init__(self, resources):
        '''void QMediaContent.__init__(list-of-QMediaResource resources)'''
    def __init__(self, other):
        '''void QMediaContent.__init__(QMediaContent other)'''
    def __init__(self, playlist, contentUrl = QUrl()):
        '''void QMediaContent.__init__(QMediaPlaylist playlist, QUrl contentUrl = QUrl())'''
    def playlist(self):
        '''QMediaPlaylist QMediaContent.playlist()'''
        return QMediaPlaylist()
    def resources(self):
        '''list-of-QMediaResource QMediaContent.resources()'''
        return [QMediaResource()]
    def canonicalResource(self):
        '''QMediaResource QMediaContent.canonicalResource()'''
        return QMediaResource()
    def canonicalRequest(self):
        '''QNetworkRequest QMediaContent.canonicalRequest()'''
        return QNetworkRequest()
    def canonicalUrl(self):
        '''QUrl QMediaContent.canonicalUrl()'''
        return QUrl()
    def isNull(self):
        '''bool QMediaContent.isNull()'''
        return bool()
    def __ne__(self, other):
        '''bool QMediaContent.__ne__(QMediaContent other)'''
        return bool()
    def __eq__(self, other):
        '''bool QMediaContent.__eq__(QMediaContent other)'''
        return bool()


class QMediaControl(QObject):
    """"""
    def __init__(self, parent = None):
        '''void QMediaControl.__init__(QObject parent = None)'''


class QAudioEncoderSettings():
    """"""
    def __init__(self):
        '''void QAudioEncoderSettings.__init__()'''
    def __init__(self, other):
        '''void QAudioEncoderSettings.__init__(QAudioEncoderSettings other)'''
    def setEncodingOptions(self, options):
        '''void QAudioEncoderSettings.setEncodingOptions(dict-of-str-object options)'''
    def setEncodingOption(self, option, value):
        '''void QAudioEncoderSettings.setEncodingOption(str option, QVariant value)'''
    def encodingOptions(self):
        '''dict-of-str-object QAudioEncoderSettings.encodingOptions()'''
        return {str():object()}
    def encodingOption(self, option):
        '''QVariant QAudioEncoderSettings.encodingOption(str option)'''
        return QVariant()
    def setQuality(self, quality):
        '''void QAudioEncoderSettings.setQuality(QMultimedia.EncodingQuality quality)'''
    def quality(self):
        '''QMultimedia.EncodingQuality QAudioEncoderSettings.quality()'''
        return QMultimedia.EncodingQuality()
    def setSampleRate(self, rate):
        '''void QAudioEncoderSettings.setSampleRate(int rate)'''
    def sampleRate(self):
        '''int QAudioEncoderSettings.sampleRate()'''
        return int()
    def setChannelCount(self, channels):
        '''void QAudioEncoderSettings.setChannelCount(int channels)'''
    def channelCount(self):
        '''int QAudioEncoderSettings.channelCount()'''
        return int()
    def setBitRate(self, bitrate):
        '''void QAudioEncoderSettings.setBitRate(int bitrate)'''
    def bitRate(self):
        '''int QAudioEncoderSettings.bitRate()'''
        return int()
    def setCodec(self, codec):
        '''void QAudioEncoderSettings.setCodec(str codec)'''
    def codec(self):
        '''str QAudioEncoderSettings.codec()'''
        return str()
    def setEncodingMode(self):
        '''QMultimedia.EncodingMode QAudioEncoderSettings.setEncodingMode()'''
        return QMultimedia.EncodingMode()
    def encodingMode(self):
        '''QMultimedia.EncodingMode QAudioEncoderSettings.encodingMode()'''
        return QMultimedia.EncodingMode()
    def isNull(self):
        '''bool QAudioEncoderSettings.isNull()'''
        return bool()
    def __ne__(self, other):
        '''bool QAudioEncoderSettings.__ne__(QAudioEncoderSettings other)'''
        return bool()
    def __eq__(self, other):
        '''bool QAudioEncoderSettings.__eq__(QAudioEncoderSettings other)'''
        return bool()


class QVideoEncoderSettings():
    """"""
    def __init__(self):
        '''void QVideoEncoderSettings.__init__()'''
    def __init__(self, other):
        '''void QVideoEncoderSettings.__init__(QVideoEncoderSettings other)'''
    def setEncodingOptions(self, options):
        '''void QVideoEncoderSettings.setEncodingOptions(dict-of-str-object options)'''
    def setEncodingOption(self, option, value):
        '''void QVideoEncoderSettings.setEncodingOption(str option, QVariant value)'''
    def encodingOptions(self):
        '''dict-of-str-object QVideoEncoderSettings.encodingOptions()'''
        return {str():object()}
    def encodingOption(self, option):
        '''QVariant QVideoEncoderSettings.encodingOption(str option)'''
        return QVariant()
    def setQuality(self, quality):
        '''void QVideoEncoderSettings.setQuality(QMultimedia.EncodingQuality quality)'''
    def quality(self):
        '''QMultimedia.EncodingQuality QVideoEncoderSettings.quality()'''
        return QMultimedia.EncodingQuality()
    def setBitRate(self, bitrate):
        '''void QVideoEncoderSettings.setBitRate(int bitrate)'''
    def bitRate(self):
        '''int QVideoEncoderSettings.bitRate()'''
        return int()
    def setFrameRate(self, rate):
        '''void QVideoEncoderSettings.setFrameRate(float rate)'''
    def frameRate(self):
        '''float QVideoEncoderSettings.frameRate()'''
        return float()
    def setResolution(self):
        '''QSize QVideoEncoderSettings.setResolution()'''
        return QSize()
    def setResolution(self, width, height):
        '''void QVideoEncoderSettings.setResolution(int width, int height)'''
    def resolution(self):
        '''QSize QVideoEncoderSettings.resolution()'''
        return QSize()
    def setCodec(self):
        '''str QVideoEncoderSettings.setCodec()'''
        return str()
    def codec(self):
        '''str QVideoEncoderSettings.codec()'''
        return str()
    def setEncodingMode(self):
        '''QMultimedia.EncodingMode QVideoEncoderSettings.setEncodingMode()'''
        return QMultimedia.EncodingMode()
    def encodingMode(self):
        '''QMultimedia.EncodingMode QVideoEncoderSettings.encodingMode()'''
        return QMultimedia.EncodingMode()
    def isNull(self):
        '''bool QVideoEncoderSettings.isNull()'''
        return bool()
    def __ne__(self, other):
        '''bool QVideoEncoderSettings.__ne__(QVideoEncoderSettings other)'''
        return bool()
    def __eq__(self, other):
        '''bool QVideoEncoderSettings.__eq__(QVideoEncoderSettings other)'''
        return bool()


class QImageEncoderSettings():
    """"""
    def __init__(self):
        '''void QImageEncoderSettings.__init__()'''
    def __init__(self, other):
        '''void QImageEncoderSettings.__init__(QImageEncoderSettings other)'''
    def setEncodingOptions(self, options):
        '''void QImageEncoderSettings.setEncodingOptions(dict-of-str-object options)'''
    def setEncodingOption(self, option, value):
        '''void QImageEncoderSettings.setEncodingOption(str option, QVariant value)'''
    def encodingOptions(self):
        '''dict-of-str-object QImageEncoderSettings.encodingOptions()'''
        return {str():object()}
    def encodingOption(self, option):
        '''QVariant QImageEncoderSettings.encodingOption(str option)'''
        return QVariant()
    def setQuality(self, quality):
        '''void QImageEncoderSettings.setQuality(QMultimedia.EncodingQuality quality)'''
    def quality(self):
        '''QMultimedia.EncodingQuality QImageEncoderSettings.quality()'''
        return QMultimedia.EncodingQuality()
    def setResolution(self):
        '''QSize QImageEncoderSettings.setResolution()'''
        return QSize()
    def setResolution(self, width, height):
        '''void QImageEncoderSettings.setResolution(int width, int height)'''
    def resolution(self):
        '''QSize QImageEncoderSettings.resolution()'''
        return QSize()
    def setCodec(self):
        '''str QImageEncoderSettings.setCodec()'''
        return str()
    def codec(self):
        '''str QImageEncoderSettings.codec()'''
        return str()
    def isNull(self):
        '''bool QImageEncoderSettings.isNull()'''
        return bool()
    def __ne__(self, other):
        '''bool QImageEncoderSettings.__ne__(QImageEncoderSettings other)'''
        return bool()
    def __eq__(self, other):
        '''bool QImageEncoderSettings.__eq__(QImageEncoderSettings other)'''
        return bool()


class QMediaMetaData():
    """"""
    AlbumArtist = None # str - member
    AlbumTitle = None # str - member
    AudioBitRate = None # str - member
    AudioCodec = None # str - member
    Author = None # str - member
    AverageLevel = None # str - member
    CameraManufacturer = None # str - member
    CameraModel = None # str - member
    Category = None # str - member
    ChannelCount = None # str - member
    ChapterNumber = None # str - member
    Comment = None # str - member
    Composer = None # str - member
    Conductor = None # str - member
    Contrast = None # str - member
    ContributingArtist = None # str - member
    Copyright = None # str - member
    CoverArtImage = None # str - member
    CoverArtUrlLarge = None # str - member
    CoverArtUrlSmall = None # str - member
    Date = None # str - member
    DateTimeDigitized = None # str - member
    DateTimeOriginal = None # str - member
    Description = None # str - member
    DeviceSettingDescription = None # str - member
    DigitalZoomRatio = None # str - member
    Director = None # str - member
    Duration = None # str - member
    Event = None # str - member
    ExposureBiasValue = None # str - member
    ExposureMode = None # str - member
    ExposureProgram = None # str - member
    ExposureTime = None # str - member
    FNumber = None # str - member
    Flash = None # str - member
    FocalLength = None # str - member
    FocalLengthIn35mmFilm = None # str - member
    GPSAltitude = None # str - member
    GPSAreaInformation = None # str - member
    GPSDOP = None # str - member
    GPSImgDirection = None # str - member
    GPSImgDirectionRef = None # str - member
    GPSLatitude = None # str - member
    GPSLongitude = None # str - member
    GPSMapDatum = None # str - member
    GPSProcessingMethod = None # str - member
    GPSSatellites = None # str - member
    GPSSpeed = None # str - member
    GPSStatus = None # str - member
    GPSTimeStamp = None # str - member
    GPSTrack = None # str - member
    GPSTrackRef = None # str - member
    GainControl = None # str - member
    Genre = None # str - member
    ISOSpeedRatings = None # str - member
    Keywords = None # str - member
    Language = None # str - member
    LeadPerformer = None # str - member
    LightSource = None # str - member
    Lyrics = None # str - member
    MediaType = None # str - member
    MeteringMode = None # str - member
    Mood = None # str - member
    Orientation = None # str - member
    ParentalRating = None # str - member
    PeakValue = None # str - member
    PixelAspectRatio = None # str - member
    PosterImage = None # str - member
    PosterUrl = None # str - member
    Publisher = None # str - member
    RatingOrganization = None # str - member
    Resolution = None # str - member
    SampleRate = None # str - member
    Saturation = None # str - member
    SceneCaptureType = None # str - member
    Sharpness = None # str - member
    Size = None # str - member
    SubTitle = None # str - member
    Subject = None # str - member
    SubjectDistance = None # str - member
    ThumbnailImage = None # str - member
    Title = None # str - member
    TrackCount = None # str - member
    TrackNumber = None # str - member
    UserRating = None # str - member
    VideoBitRate = None # str - member
    VideoCodec = None # str - member
    VideoFrameRate = None # str - member
    WhiteBalance = None # str - member
    Writer = None # str - member
    Year = None # str - member


class QMediaPlayer(QMediaObject):
    """"""
    # Enum QMediaPlayer.Error
    NoError = 0
    ResourceError = 0
    FormatError = 0
    NetworkError = 0
    AccessDeniedError = 0
    ServiceMissingError = 0

    # Enum QMediaPlayer.Flag
    LowLatency = 0
    StreamPlayback = 0
    VideoSurface = 0

    # Enum QMediaPlayer.MediaStatus
    UnknownMediaStatus = 0
    NoMedia = 0
    LoadingMedia = 0
    LoadedMedia = 0
    StalledMedia = 0
    BufferingMedia = 0
    BufferedMedia = 0
    EndOfMedia = 0
    InvalidMedia = 0

    # Enum QMediaPlayer.State
    StoppedState = 0
    PlayingState = 0
    PausedState = 0

    def __init__(self, parent = None, flags = 0):
        '''void QMediaPlayer.__init__(QObject parent = None, QMediaPlayer.Flags flags = 0)'''
    def unbind(self):
        '''QObject QMediaPlayer.unbind()'''
        return QObject()
    def bind(self):
        '''QObject QMediaPlayer.bind()'''
        return QObject()
    networkConfigurationChanged = pyqtSignal() # void networkConfigurationChanged(const QNetworkConfigurationamp;) - signal
    playbackRateChanged = pyqtSignal() # void playbackRateChanged(qreal) - signal
    seekableChanged = pyqtSignal() # void seekableChanged(bool) - signal
    bufferStatusChanged = pyqtSignal() # void bufferStatusChanged(int) - signal
    videoAvailableChanged = pyqtSignal() # void videoAvailableChanged(bool) - signal
    audioAvailableChanged = pyqtSignal() # void audioAvailableChanged(bool) - signal
    mutedChanged = pyqtSignal() # void mutedChanged(bool) - signal
    volumeChanged = pyqtSignal() # void volumeChanged(int) - signal
    positionChanged = pyqtSignal() # void positionChanged(qint64) - signal
    durationChanged = pyqtSignal() # void durationChanged(qint64) - signal
    mediaStatusChanged = pyqtSignal() # void mediaStatusChanged(QMediaPlayer::MediaStatus) - signal
    stateChanged = pyqtSignal() # void stateChanged(QMediaPlayer::State) - signal
    currentMediaChanged = pyqtSignal() # void currentMediaChanged(const QMediaContentamp;) - signal
    mediaChanged = pyqtSignal() # void mediaChanged(const QMediaContentamp;) - signal
    def setNetworkConfigurations(self, configurations):
        '''void QMediaPlayer.setNetworkConfigurations(list-of-QNetworkConfiguration configurations)'''
    def setPlaylist(self, playlist):
        '''void QMediaPlayer.setPlaylist(QMediaPlaylist playlist)'''
    def setMedia(self, media, stream = None):
        '''void QMediaPlayer.setMedia(QMediaContent media, QIODevice stream = None)'''
    def setPlaybackRate(self, rate):
        '''void QMediaPlayer.setPlaybackRate(float rate)'''
    def setMuted(self, muted):
        '''void QMediaPlayer.setMuted(bool muted)'''
    def setVolume(self, volume):
        '''void QMediaPlayer.setVolume(int volume)'''
    def setPosition(self, position):
        '''void QMediaPlayer.setPosition(int position)'''
    def stop(self):
        '''void QMediaPlayer.stop()'''
    def pause(self):
        '''void QMediaPlayer.pause()'''
    def play(self):
        '''void QMediaPlayer.play()'''
    def availability(self):
        '''QMultimedia.AvailabilityStatus QMediaPlayer.availability()'''
        return QMultimedia.AvailabilityStatus()
    def currentNetworkConfiguration(self):
        '''QNetworkConfiguration QMediaPlayer.currentNetworkConfiguration()'''
        return QNetworkConfiguration()
    def errorString(self):
        '''str QMediaPlayer.errorString()'''
        return str()
    def error(self):
        '''QMediaPlayer.Error QMediaPlayer.error()'''
        return QMediaPlayer.Error()
    error = pyqtSignal() # void error(QMediaPlayer::Error) - signal
    def playbackRate(self):
        '''float QMediaPlayer.playbackRate()'''
        return float()
    def isSeekable(self):
        '''bool QMediaPlayer.isSeekable()'''
        return bool()
    def bufferStatus(self):
        '''int QMediaPlayer.bufferStatus()'''
        return int()
    def isVideoAvailable(self):
        '''bool QMediaPlayer.isVideoAvailable()'''
        return bool()
    def isAudioAvailable(self):
        '''bool QMediaPlayer.isAudioAvailable()'''
        return bool()
    def isMuted(self):
        '''bool QMediaPlayer.isMuted()'''
        return bool()
    def volume(self):
        '''int QMediaPlayer.volume()'''
        return int()
    def position(self):
        '''int QMediaPlayer.position()'''
        return int()
    def duration(self):
        '''int QMediaPlayer.duration()'''
        return int()
    def mediaStatus(self):
        '''QMediaPlayer.MediaStatus QMediaPlayer.mediaStatus()'''
        return QMediaPlayer.MediaStatus()
    def state(self):
        '''QMediaPlayer.State QMediaPlayer.state()'''
        return QMediaPlayer.State()
    def currentMedia(self):
        '''QMediaContent QMediaPlayer.currentMedia()'''
        return QMediaContent()
    def playlist(self):
        '''QMediaPlaylist QMediaPlayer.playlist()'''
        return QMediaPlaylist()
    def mediaStream(self):
        '''QIODevice QMediaPlayer.mediaStream()'''
        return QIODevice()
    def media(self):
        '''QMediaContent QMediaPlayer.media()'''
        return QMediaContent()
    def setVideoOutput(self):
        '''QVideoWidget QMediaPlayer.setVideoOutput()'''
        return QVideoWidget()
    def setVideoOutput(self):
        '''QGraphicsVideoItem QMediaPlayer.setVideoOutput()'''
        return QGraphicsVideoItem()
    def setVideoOutput(self, surface):
        '''void QMediaPlayer.setVideoOutput(QAbstractVideoSurface surface)'''
    def supportedMimeTypes(self, flags = 0):
        '''static list-of-str QMediaPlayer.supportedMimeTypes(QMediaPlayer.Flags flags = 0)'''
        return [str()]
    def hasSupport(self, mimeType, codecs = strList(), flags = 0):
        '''static QMultimedia.SupportEstimate QMediaPlayer.hasSupport(str mimeType, list-of-str codecs = strList(), QMediaPlayer.Flags flags = 0)'''
        return QMultimedia.SupportEstimate()
    class Flags():
        """"""
        def __init__(self):
            '''QMediaPlayer.Flags QMediaPlayer.Flags.__init__()'''
            return QMediaPlayer.Flags()
        def __init__(self):
            '''int QMediaPlayer.Flags.__init__()'''
            return int()
        def __init__(self):
            '''void QMediaPlayer.Flags.__init__()'''
        def __bool__(self):
            '''int QMediaPlayer.Flags.__bool__()'''
            return int()
        def __ne__(self, f):
            '''bool QMediaPlayer.Flags.__ne__(QMediaPlayer.Flags f)'''
            return bool()
        def __eq__(self, f):
            '''bool QMediaPlayer.Flags.__eq__(QMediaPlayer.Flags f)'''
            return bool()
        def __invert__(self):
            '''QMediaPlayer.Flags QMediaPlayer.Flags.__invert__()'''
            return QMediaPlayer.Flags()
        def __and__(self, mask):
            '''QMediaPlayer.Flags QMediaPlayer.Flags.__and__(int mask)'''
            return QMediaPlayer.Flags()
        def __xor__(self, f):
            '''QMediaPlayer.Flags QMediaPlayer.Flags.__xor__(QMediaPlayer.Flags f)'''
            return QMediaPlayer.Flags()
        def __xor__(self, f):
            '''QMediaPlayer.Flags QMediaPlayer.Flags.__xor__(int f)'''
            return QMediaPlayer.Flags()
        def __or__(self, f):
            '''QMediaPlayer.Flags QMediaPlayer.Flags.__or__(QMediaPlayer.Flags f)'''
            return QMediaPlayer.Flags()
        def __or__(self, f):
            '''QMediaPlayer.Flags QMediaPlayer.Flags.__or__(int f)'''
            return QMediaPlayer.Flags()
        def __int__(self):
            '''int QMediaPlayer.Flags.__int__()'''
            return int()
        def __ixor__(self, f):
            '''QMediaPlayer.Flags QMediaPlayer.Flags.__ixor__(QMediaPlayer.Flags f)'''
            return QMediaPlayer.Flags()
        def __ior__(self, f):
            '''QMediaPlayer.Flags QMediaPlayer.Flags.__ior__(QMediaPlayer.Flags f)'''
            return QMediaPlayer.Flags()
        def __iand__(self, mask):
            '''QMediaPlayer.Flags QMediaPlayer.Flags.__iand__(int mask)'''
            return QMediaPlayer.Flags()


class QMediaPlaylist(QObject, QMediaBindableInterface):
    """"""
    # Enum QMediaPlaylist.Error
    NoError = 0
    FormatError = 0
    FormatNotSupportedError = 0
    NetworkError = 0
    AccessDeniedError = 0

    # Enum QMediaPlaylist.PlaybackMode
    CurrentItemOnce = 0
    CurrentItemInLoop = 0
    Sequential = 0
    Loop = 0
    Random = 0

    def __init__(self, parent = None):
        '''void QMediaPlaylist.__init__(QObject parent = None)'''
    def setMediaObject(self, object):
        '''bool QMediaPlaylist.setMediaObject(QMediaObject object)'''
        return bool()
    loadFailed = pyqtSignal() # void loadFailed() - signal
    loaded = pyqtSignal() # void loaded() - signal
    mediaChanged = pyqtSignal() # void mediaChanged(int,int) - signal
    mediaRemoved = pyqtSignal() # void mediaRemoved(int,int) - signal
    mediaAboutToBeRemoved = pyqtSignal() # void mediaAboutToBeRemoved(int,int) - signal
    mediaInserted = pyqtSignal() # void mediaInserted(int,int) - signal
    mediaAboutToBeInserted = pyqtSignal() # void mediaAboutToBeInserted(int,int) - signal
    currentMediaChanged = pyqtSignal() # void currentMediaChanged(const QMediaContentamp;) - signal
    playbackModeChanged = pyqtSignal() # void playbackModeChanged(QMediaPlaylist::PlaybackMode) - signal
    currentIndexChanged = pyqtSignal() # void currentIndexChanged(int) - signal
    def setCurrentIndex(self, index):
        '''void QMediaPlaylist.setCurrentIndex(int index)'''
    def previous(self):
        '''void QMediaPlaylist.previous()'''
    def next(self):
        '''void QMediaPlaylist.next()'''
    def shuffle(self):
        '''void QMediaPlaylist.shuffle()'''
    def errorString(self):
        '''str QMediaPlaylist.errorString()'''
        return str()
    def error(self):
        '''QMediaPlaylist.Error QMediaPlaylist.error()'''
        return QMediaPlaylist.Error()
    def save(self, location, format = None):
        '''bool QMediaPlaylist.save(QUrl location, str format = None)'''
        return bool()
    def save(self, device, format):
        '''bool QMediaPlaylist.save(QIODevice device, str format)'''
        return bool()
    def load(self, request, format = None):
        '''void QMediaPlaylist.load(QNetworkRequest request, str format = None)'''
    def load(self, location, format = None):
        '''void QMediaPlaylist.load(QUrl location, str format = None)'''
    def load(self, device, format = None):
        '''void QMediaPlaylist.load(QIODevice device, str format = None)'''
    def clear(self):
        '''bool QMediaPlaylist.clear()'''
        return bool()
    def removeMedia(self, pos):
        '''bool QMediaPlaylist.removeMedia(int pos)'''
        return bool()
    def removeMedia(self, start, end):
        '''bool QMediaPlaylist.removeMedia(int start, int end)'''
        return bool()
    def insertMedia(self, index, content):
        '''bool QMediaPlaylist.insertMedia(int index, QMediaContent content)'''
        return bool()
    def insertMedia(self, index, items):
        '''bool QMediaPlaylist.insertMedia(int index, list-of-QMediaContent items)'''
        return bool()
    def addMedia(self, content):
        '''bool QMediaPlaylist.addMedia(QMediaContent content)'''
        return bool()
    def addMedia(self, items):
        '''bool QMediaPlaylist.addMedia(list-of-QMediaContent items)'''
        return bool()
    def isReadOnly(self):
        '''bool QMediaPlaylist.isReadOnly()'''
        return bool()
    def isEmpty(self):
        '''bool QMediaPlaylist.isEmpty()'''
        return bool()
    def mediaCount(self):
        '''int QMediaPlaylist.mediaCount()'''
        return int()
    def media(self, index):
        '''QMediaContent QMediaPlaylist.media(int index)'''
        return QMediaContent()
    def previousIndex(self, steps = 1):
        '''int QMediaPlaylist.previousIndex(int steps = 1)'''
        return int()
    def nextIndex(self, steps = 1):
        '''int QMediaPlaylist.nextIndex(int steps = 1)'''
        return int()
    def currentMedia(self):
        '''QMediaContent QMediaPlaylist.currentMedia()'''
        return QMediaContent()
    def currentIndex(self):
        '''int QMediaPlaylist.currentIndex()'''
        return int()
    def setPlaybackMode(self, mode):
        '''void QMediaPlaylist.setPlaybackMode(QMediaPlaylist.PlaybackMode mode)'''
    def playbackMode(self):
        '''QMediaPlaylist.PlaybackMode QMediaPlaylist.playbackMode()'''
        return QMediaPlaylist.PlaybackMode()
    def mediaObject(self):
        '''QMediaObject QMediaPlaylist.mediaObject()'''
        return QMediaObject()


class QMediaResource():
    """"""
    def __init__(self):
        '''void QMediaResource.__init__()'''
    def __init__(self, url, mimeType = str()):
        '''void QMediaResource.__init__(QUrl url, str mimeType = str())'''
    def __init__(self, request, mimeType = str()):
        '''void QMediaResource.__init__(QNetworkRequest request, str mimeType = str())'''
    def __init__(self, other):
        '''void QMediaResource.__init__(QMediaResource other)'''
    def setResolution(self, resolution):
        '''void QMediaResource.setResolution(QSize resolution)'''
    def setResolution(self, width, height):
        '''void QMediaResource.setResolution(int width, int height)'''
    def resolution(self):
        '''QSize QMediaResource.resolution()'''
        return QSize()
    def setVideoBitRate(self, rate):
        '''void QMediaResource.setVideoBitRate(int rate)'''
    def videoBitRate(self):
        '''int QMediaResource.videoBitRate()'''
        return int()
    def setChannelCount(self, channels):
        '''void QMediaResource.setChannelCount(int channels)'''
    def channelCount(self):
        '''int QMediaResource.channelCount()'''
        return int()
    def setSampleRate(self, frequency):
        '''void QMediaResource.setSampleRate(int frequency)'''
    def sampleRate(self):
        '''int QMediaResource.sampleRate()'''
        return int()
    def setAudioBitRate(self, rate):
        '''void QMediaResource.setAudioBitRate(int rate)'''
    def audioBitRate(self):
        '''int QMediaResource.audioBitRate()'''
        return int()
    def setDataSize(self, size):
        '''void QMediaResource.setDataSize(int size)'''
    def dataSize(self):
        '''int QMediaResource.dataSize()'''
        return int()
    def setVideoCodec(self, codec):
        '''void QMediaResource.setVideoCodec(str codec)'''
    def videoCodec(self):
        '''str QMediaResource.videoCodec()'''
        return str()
    def setAudioCodec(self, codec):
        '''void QMediaResource.setAudioCodec(str codec)'''
    def audioCodec(self):
        '''str QMediaResource.audioCodec()'''
        return str()
    def setLanguage(self, language):
        '''void QMediaResource.setLanguage(str language)'''
    def language(self):
        '''str QMediaResource.language()'''
        return str()
    def mimeType(self):
        '''str QMediaResource.mimeType()'''
        return str()
    def request(self):
        '''QNetworkRequest QMediaResource.request()'''
        return QNetworkRequest()
    def url(self):
        '''QUrl QMediaResource.url()'''
        return QUrl()
    def __ne__(self, other):
        '''bool QMediaResource.__ne__(QMediaResource other)'''
        return bool()
    def __eq__(self, other):
        '''bool QMediaResource.__eq__(QMediaResource other)'''
        return bool()
    def isNull(self):
        '''bool QMediaResource.isNull()'''
        return bool()


class QMediaService(QObject):
    """"""
    def __init__(self, parent):
        '''void QMediaService.__init__(QObject parent)'''
    def releaseControl(self, control):
        '''abstract void QMediaService.releaseControl(QMediaControl control)'''
    def requestControl(self, name):
        '''abstract QMediaControl QMediaService.requestControl(str name)'''
        return QMediaControl()


class QMediaTimeInterval():
    """"""
    def __init__(self):
        '''void QMediaTimeInterval.__init__()'''
    def __init__(self, start, end):
        '''void QMediaTimeInterval.__init__(int start, int end)'''
    def __init__(self):
        '''QMediaTimeInterval QMediaTimeInterval.__init__()'''
        return QMediaTimeInterval()
    def __eq__(self):
        '''QMediaTimeInterval QMediaTimeInterval.__eq__()'''
        return QMediaTimeInterval()
    def __ne__(self):
        '''QMediaTimeInterval QMediaTimeInterval.__ne__()'''
        return QMediaTimeInterval()
    def translated(self, offset):
        '''QMediaTimeInterval QMediaTimeInterval.translated(int offset)'''
        return QMediaTimeInterval()
    def normalized(self):
        '''QMediaTimeInterval QMediaTimeInterval.normalized()'''
        return QMediaTimeInterval()
    def isNormal(self):
        '''bool QMediaTimeInterval.isNormal()'''
        return bool()
    def contains(self, time):
        '''bool QMediaTimeInterval.contains(int time)'''
        return bool()
    def end(self):
        '''int QMediaTimeInterval.end()'''
        return int()
    def start(self):
        '''int QMediaTimeInterval.start()'''
        return int()


class QMediaTimeRange():
    """"""
    def __init__(self):
        '''void QMediaTimeRange.__init__()'''
    def __init__(self, start, end):
        '''void QMediaTimeRange.__init__(int start, int end)'''
    def __init__(self):
        '''QMediaTimeInterval QMediaTimeRange.__init__()'''
        return QMediaTimeInterval()
    def __init__(self, range):
        '''void QMediaTimeRange.__init__(QMediaTimeRange range)'''
    def __eq__(self):
        '''QMediaTimeRange QMediaTimeRange.__eq__()'''
        return QMediaTimeRange()
    def __ne__(self):
        '''QMediaTimeRange QMediaTimeRange.__ne__()'''
        return QMediaTimeRange()
    def __add__(self):
        '''QMediaTimeRange QMediaTimeRange.__add__()'''
        return QMediaTimeRange()
    def __sub__(self):
        '''QMediaTimeRange QMediaTimeRange.__sub__()'''
        return QMediaTimeRange()
    def clear(self):
        '''void QMediaTimeRange.clear()'''
    def __isub__(self):
        '''QMediaTimeRange QMediaTimeRange.__isub__()'''
        return QMediaTimeRange()
    def __isub__(self):
        '''QMediaTimeInterval QMediaTimeRange.__isub__()'''
        return QMediaTimeInterval()
    def __iadd__(self):
        '''QMediaTimeRange QMediaTimeRange.__iadd__()'''
        return QMediaTimeRange()
    def __iadd__(self):
        '''QMediaTimeInterval QMediaTimeRange.__iadd__()'''
        return QMediaTimeInterval()
    def removeTimeRange(self):
        '''QMediaTimeRange QMediaTimeRange.removeTimeRange()'''
        return QMediaTimeRange()
    def removeInterval(self, start, end):
        '''void QMediaTimeRange.removeInterval(int start, int end)'''
    def removeInterval(self, interval):
        '''void QMediaTimeRange.removeInterval(QMediaTimeInterval interval)'''
    def addTimeRange(self):
        '''QMediaTimeRange QMediaTimeRange.addTimeRange()'''
        return QMediaTimeRange()
    def addInterval(self, start, end):
        '''void QMediaTimeRange.addInterval(int start, int end)'''
    def addInterval(self, interval):
        '''void QMediaTimeRange.addInterval(QMediaTimeInterval interval)'''
    def contains(self, time):
        '''bool QMediaTimeRange.contains(int time)'''
        return bool()
    def isContinuous(self):
        '''bool QMediaTimeRange.isContinuous()'''
        return bool()
    def isEmpty(self):
        '''bool QMediaTimeRange.isEmpty()'''
        return bool()
    def intervals(self):
        '''list-of-QMediaTimeInterval QMediaTimeRange.intervals()'''
        return [QMediaTimeInterval()]
    def latestTime(self):
        '''int QMediaTimeRange.latestTime()'''
        return int()
    def earliestTime(self):
        '''int QMediaTimeRange.earliestTime()'''
        return int()


class QMultimedia():
    """"""
    # Enum QMultimedia.AvailabilityStatus
    Available = 0
    ServiceMissing = 0
    Busy = 0
    ResourceError = 0

    # Enum QMultimedia.EncodingMode
    ConstantQualityEncoding = 0
    ConstantBitRateEncoding = 0
    AverageBitRateEncoding = 0
    TwoPassEncoding = 0

    # Enum QMultimedia.EncodingQuality
    VeryLowQuality = 0
    LowQuality = 0
    NormalQuality = 0
    HighQuality = 0
    VeryHighQuality = 0

    # Enum QMultimedia.SupportEstimate
    NotSupported = 0
    MaybeSupported = 0
    ProbablySupported = 0
    PreferredService = 0



class QRadioData(QObject, QMediaBindableInterface):
    """"""
    # Enum QRadioData.ProgramType
    Undefined = 0
    News = 0
    CurrentAffairs = 0
    Information = 0
    Sport = 0
    Education = 0
    Drama = 0
    Culture = 0
    Science = 0
    Varied = 0
    PopMusic = 0
    RockMusic = 0
    EasyListening = 0
    LightClassical = 0
    SeriousClassical = 0
    OtherMusic = 0
    Weather = 0
    Finance = 0
    ChildrensProgrammes = 0
    SocialAffairs = 0
    Religion = 0
    PhoneIn = 0
    Travel = 0
    Leisure = 0
    JazzMusic = 0
    CountryMusic = 0
    NationalMusic = 0
    OldiesMusic = 0
    FolkMusic = 0
    Documentary = 0
    AlarmTest = 0
    Alarm = 0
    Talk = 0
    ClassicRock = 0
    AdultHits = 0
    SoftRock = 0
    Top40 = 0
    Soft = 0
    Nostalgia = 0
    Classical = 0
    RhythmAndBlues = 0
    SoftRhythmAndBlues = 0
    Language = 0
    ReligiousMusic = 0
    ReligiousTalk = 0
    Personality = 0
    Public = 0
    College = 0

    # Enum QRadioData.Error
    NoError = 0
    ResourceError = 0
    OpenError = 0
    OutOfRangeError = 0

    def __init__(self, mediaObject, parent = None):
        '''void QRadioData.__init__(QMediaObject mediaObject, QObject parent = None)'''
    def setMediaObject(self):
        '''QMediaObject QRadioData.setMediaObject()'''
        return QMediaObject()
    alternativeFrequenciesEnabledChanged = pyqtSignal() # void alternativeFrequenciesEnabledChanged(bool) - signal
    radioTextChanged = pyqtSignal() # void radioTextChanged(QString) - signal
    stationNameChanged = pyqtSignal() # void stationNameChanged(QString) - signal
    programTypeNameChanged = pyqtSignal() # void programTypeNameChanged(QString) - signal
    programTypeChanged = pyqtSignal() # void programTypeChanged(QRadioData::ProgramType) - signal
    stationIdChanged = pyqtSignal() # void stationIdChanged(QString) - signal
    def setAlternativeFrequenciesEnabled(self, enabled):
        '''void QRadioData.setAlternativeFrequenciesEnabled(bool enabled)'''
    def errorString(self):
        '''str QRadioData.errorString()'''
        return str()
    def error(self):
        '''QRadioData.Error QRadioData.error()'''
        return QRadioData.Error()
    error = pyqtSignal() # void error(QRadioData::Error) - signal
    def isAlternativeFrequenciesEnabled(self):
        '''bool QRadioData.isAlternativeFrequenciesEnabled()'''
        return bool()
    def radioText(self):
        '''str QRadioData.radioText()'''
        return str()
    def stationName(self):
        '''str QRadioData.stationName()'''
        return str()
    def programTypeName(self):
        '''str QRadioData.programTypeName()'''
        return str()
    def programType(self):
        '''QRadioData.ProgramType QRadioData.programType()'''
        return QRadioData.ProgramType()
    def stationId(self):
        '''str QRadioData.stationId()'''
        return str()
    def availability(self):
        '''QMultimedia.AvailabilityStatus QRadioData.availability()'''
        return QMultimedia.AvailabilityStatus()
    def mediaObject(self):
        '''QMediaObject QRadioData.mediaObject()'''
        return QMediaObject()


class QRadioTuner(QMediaObject):
    """"""
    # Enum QRadioTuner.SearchMode
    SearchFast = 0
    SearchGetStationId = 0

    # Enum QRadioTuner.StereoMode
    ForceStereo = 0
    ForceMono = 0
    Auto = 0

    # Enum QRadioTuner.Error
    NoError = 0
    ResourceError = 0
    OpenError = 0
    OutOfRangeError = 0

    # Enum QRadioTuner.Band
    AM = 0
    FM = 0
    SW = 0
    LW = 0
    FM2 = 0

    # Enum QRadioTuner.State
    ActiveState = 0
    StoppedState = 0

    def __init__(self, parent = None):
        '''void QRadioTuner.__init__(QObject parent = None)'''
    antennaConnectedChanged = pyqtSignal() # void antennaConnectedChanged(bool) - signal
    stationFound = pyqtSignal() # void stationFound(int,QString) - signal
    mutedChanged = pyqtSignal() # void mutedChanged(bool) - signal
    volumeChanged = pyqtSignal() # void volumeChanged(int) - signal
    signalStrengthChanged = pyqtSignal() # void signalStrengthChanged(int) - signal
    searchingChanged = pyqtSignal() # void searchingChanged(bool) - signal
    stereoStatusChanged = pyqtSignal() # void stereoStatusChanged(bool) - signal
    frequencyChanged = pyqtSignal() # void frequencyChanged(int) - signal
    bandChanged = pyqtSignal() # void bandChanged(QRadioTuner::Band) - signal
    stateChanged = pyqtSignal() # void stateChanged(QRadioTuner::State) - signal
    def stop(self):
        '''void QRadioTuner.stop()'''
    def start(self):
        '''void QRadioTuner.start()'''
    def setMuted(self, muted):
        '''void QRadioTuner.setMuted(bool muted)'''
    def setVolume(self, volume):
        '''void QRadioTuner.setVolume(int volume)'''
    def setFrequency(self, frequency):
        '''void QRadioTuner.setFrequency(int frequency)'''
    def setBand(self, band):
        '''void QRadioTuner.setBand(QRadioTuner.Band band)'''
    def cancelSearch(self):
        '''void QRadioTuner.cancelSearch()'''
    def searchAllStations(self, searchMode = None):
        '''void QRadioTuner.searchAllStations(QRadioTuner.SearchMode searchMode = QRadioTuner.SearchFast)'''
    def searchBackward(self):
        '''void QRadioTuner.searchBackward()'''
    def searchForward(self):
        '''void QRadioTuner.searchForward()'''
    def radioData(self):
        '''QRadioData QRadioTuner.radioData()'''
        return QRadioData()
    def errorString(self):
        '''str QRadioTuner.errorString()'''
        return str()
    def error(self):
        '''QRadioTuner.Error QRadioTuner.error()'''
        return QRadioTuner.Error()
    error = pyqtSignal() # void error(QRadioTuner::Error) - signal
    def isAntennaConnected(self):
        '''bool QRadioTuner.isAntennaConnected()'''
        return bool()
    def isSearching(self):
        '''bool QRadioTuner.isSearching()'''
        return bool()
    def isMuted(self):
        '''bool QRadioTuner.isMuted()'''
        return bool()
    def volume(self):
        '''int QRadioTuner.volume()'''
        return int()
    def signalStrength(self):
        '''int QRadioTuner.signalStrength()'''
        return int()
    def stereoMode(self):
        '''QRadioTuner.StereoMode QRadioTuner.stereoMode()'''
        return QRadioTuner.StereoMode()
    def setStereoMode(self, mode):
        '''void QRadioTuner.setStereoMode(QRadioTuner.StereoMode mode)'''
    def isStereo(self):
        '''bool QRadioTuner.isStereo()'''
        return bool()
    def frequencyRange(self, band):
        '''tuple-of-int-int QRadioTuner.frequencyRange(QRadioTuner.Band band)'''
        return tuple-of-int-int()
    def frequencyStep(self, band):
        '''int QRadioTuner.frequencyStep(QRadioTuner.Band band)'''
        return int()
    def frequency(self):
        '''int QRadioTuner.frequency()'''
        return int()
    def isBandSupported(self, b):
        '''bool QRadioTuner.isBandSupported(QRadioTuner.Band b)'''
        return bool()
    def band(self):
        '''QRadioTuner.Band QRadioTuner.band()'''
        return QRadioTuner.Band()
    def state(self):
        '''QRadioTuner.State QRadioTuner.state()'''
        return QRadioTuner.State()
    def availability(self):
        '''QMultimedia.AvailabilityStatus QRadioTuner.availability()'''
        return QMultimedia.AvailabilityStatus()


class QSound(QObject):
    """"""
    # Enum QSound.Loop
    Infinite = 0

    def __init__(self, filename, parent = None):
        '''void QSound.__init__(str filename, QObject parent = None)'''
    def stop(self):
        '''void QSound.stop()'''
    def isFinished(self):
        '''bool QSound.isFinished()'''
        return bool()
    def fileName(self):
        '''str QSound.fileName()'''
        return str()
    def setLoops(self):
        '''int QSound.setLoops()'''
        return int()
    def loopsRemaining(self):
        '''int QSound.loopsRemaining()'''
        return int()
    def loops(self):
        '''int QSound.loops()'''
        return int()
    def play(self, filename):
        '''static void QSound.play(str filename)'''
    def play(self):
        '''void QSound.play()'''


class QSoundEffect(QObject):
    """"""
    # Enum QSoundEffect.Status
    Null = 0
    Loading = 0
    Ready = 0
    Error = 0

    # Enum QSoundEffect.Loop
    Infinite = 0

    def __init__(self, parent = None):
        '''void QSoundEffect.__init__(QObject parent = None)'''
    def stop(self):
        '''void QSoundEffect.stop()'''
    def play(self):
        '''void QSoundEffect.play()'''
    categoryChanged = pyqtSignal() # void categoryChanged() - signal
    statusChanged = pyqtSignal() # void statusChanged() - signal
    playingChanged = pyqtSignal() # void playingChanged() - signal
    loadedChanged = pyqtSignal() # void loadedChanged() - signal
    mutedChanged = pyqtSignal() # void mutedChanged() - signal
    volumeChanged = pyqtSignal() # void volumeChanged() - signal
    loopsRemainingChanged = pyqtSignal() # void loopsRemainingChanged() - signal
    loopCountChanged = pyqtSignal() # void loopCountChanged() - signal
    sourceChanged = pyqtSignal() # void sourceChanged() - signal
    def setCategory(self, category):
        '''void QSoundEffect.setCategory(str category)'''
    def category(self):
        '''str QSoundEffect.category()'''
        return str()
    def status(self):
        '''QSoundEffect.Status QSoundEffect.status()'''
        return QSoundEffect.Status()
    def isPlaying(self):
        '''bool QSoundEffect.isPlaying()'''
        return bool()
    def isLoaded(self):
        '''bool QSoundEffect.isLoaded()'''
        return bool()
    def setMuted(self, muted):
        '''void QSoundEffect.setMuted(bool muted)'''
    def isMuted(self):
        '''bool QSoundEffect.isMuted()'''
        return bool()
    def setVolume(self, volume):
        '''void QSoundEffect.setVolume(float volume)'''
    def volume(self):
        '''float QSoundEffect.volume()'''
        return float()
    def setLoopCount(self, loopCount):
        '''void QSoundEffect.setLoopCount(int loopCount)'''
    def loopsRemaining(self):
        '''int QSoundEffect.loopsRemaining()'''
        return int()
    def loopCount(self):
        '''int QSoundEffect.loopCount()'''
        return int()
    def setSource(self, url):
        '''void QSoundEffect.setSource(QUrl url)'''
    def source(self):
        '''QUrl QSoundEffect.source()'''
        return QUrl()
    def supportedMimeTypes(self):
        '''static list-of-str QSoundEffect.supportedMimeTypes()'''
        return [str()]


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
    Format_Jpeg = 0
    Format_CameraRaw = 0
    Format_AdobeDng = 0
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
    def __ne__(self, other):
        '''bool QVideoFrame.__ne__(QVideoFrame other)'''
        return bool()
    def __eq__(self, other):
        '''bool QVideoFrame.__eq__(QVideoFrame other)'''
        return bool()
    def planeCount(self):
        '''int QVideoFrame.planeCount()'''
        return int()
    def setMetaData(self, key, value):
        '''void QVideoFrame.setMetaData(str key, QVariant value)'''
    def metaData(self, key):
        '''QVariant QVideoFrame.metaData(str key)'''
        return QVariant()
    def availableMetaData(self):
        '''dict-of-str-object QVideoFrame.availableMetaData()'''
        return {str():object()}
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
    def bits(self, plane):
        '''sip.voidptr QVideoFrame.bits(int plane)'''
        return sip.voidptr()
    def bytesPerLine(self):
        '''int QVideoFrame.bytesPerLine()'''
        return int()
    def bytesPerLine(self, plane):
        '''int QVideoFrame.bytesPerLine(int plane)'''
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


class QVideoProbe(QObject):
    """"""
    def __init__(self, parent = None):
        '''void QVideoProbe.__init__(QObject parent = None)'''
    flush = pyqtSignal() # void flush() - signal
    videoFrameProbed = pyqtSignal() # void videoFrameProbed(const QVideoFrameamp;) - signal
    def isActive(self):
        '''bool QVideoProbe.isActive()'''
        return bool()
    def setSource(self, source):
        '''bool QVideoProbe.setSource(QMediaObject source)'''
        return bool()
    def setSource(self, source):
        '''bool QVideoProbe.setSource(QMediaRecorder source)'''
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


