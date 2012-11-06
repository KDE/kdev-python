class pyqtSignal():
 def connect(self, targetSignal): pass
 def emit(self, *args): pass
from QtCore import *

class Phonon():
    """"""
    # Enum Phonon.ErrorType
    NoError = 0
    NormalError = 0
    FatalError = 0

    # Enum Phonon.Category
    NoCategory = 0
    NotificationCategory = 0
    MusicCategory = 0
    VideoCategory = 0
    CommunicationCategory = 0
    GameCategory = 0
    AccessibilityCategory = 0

    # Enum Phonon.State
    LoadingState = 0
    StoppedState = 0
    PlayingState = 0
    BufferingState = 0
    PausedState = 0
    ErrorState = 0

    # Enum Phonon.MetaData
    ArtistMetaData = 0
    AlbumMetaData = 0
    TitleMetaData = 0
    DateMetaData = 0
    GenreMetaData = 0
    TracknumberMetaData = 0
    DescriptionMetaData = 0
    MusicBrainzDiscIdMetaData = 0

    # Enum Phonon.DiscType
    NoDisc = 0
    Cd = 0
    Dvd = 0
    Vcd = 0

    def phononVersion(self):
        '''static str Phonon.phononVersion()'''
        return str()
    def categoryToString(self, c):
        '''static QString Phonon.categoryToString(Phonon.Category c)'''
        return QString()
    def createPath(self, source, sink):
        '''static Phonon.Path Phonon.createPath(Phonon.MediaNode source, Phonon.MediaNode sink)'''
        return Phonon.Path()
    def createPlayer(self, category, source = None):
        '''static Phonon.MediaObject Phonon.createPlayer(Phonon.Category category, Phonon.MediaSource source = Phonon.MediaSource())'''
        return Phonon.MediaObject()
    class Effect(QObject, Phonon.MediaNode):
        """"""
        def __init__(self, description, parent = None):
            '''void Phonon.Effect.__init__(Phonon.EffectDescription description, QObject parent = None)'''
        def setParameterValue(self, value):
            '''Phonon.EffectParameter Phonon.Effect.setParameterValue(QVariant value)'''
            return Phonon.EffectParameter()
        def parameterValue(self):
            '''Phonon.EffectParameter Phonon.Effect.parameterValue()'''
            return Phonon.EffectParameter()
        def parameters(self):
            '''list-of-Phonon.EffectParameter Phonon.Effect.parameters()'''
            return [Phonon.EffectParameter()]
        def description(self):
            '''Phonon.EffectDescription Phonon.Effect.description()'''
            return Phonon.EffectDescription()
    class BackendCapabilities():
        """"""
        def availableAudioCaptureDevices(self):
            '''static list-of-Phonon.AudioCaptureDevice Phonon.BackendCapabilities.availableAudioCaptureDevices()'''
            return [Phonon.AudioCaptureDevice()]
        def availableAudioEffects(self):
            '''static list-of-Phonon.EffectDescription Phonon.BackendCapabilities.availableAudioEffects()'''
            return [Phonon.EffectDescription()]
        def availableAudioOutputDevices(self):
            '''static list-of-Phonon.AudioOutputDevice Phonon.BackendCapabilities.availableAudioOutputDevices()'''
            return [Phonon.AudioOutputDevice()]
        def isMimeTypeAvailable(self, mimeType):
            '''static bool Phonon.BackendCapabilities.isMimeTypeAvailable(QString mimeType)'''
            return bool()
        def availableMimeTypes(self):
            '''static QStringList Phonon.BackendCapabilities.availableMimeTypes()'''
            return QStringList()
        def notifier(self):
            '''static Phonon.BackendCapabilities.Notifier Phonon.BackendCapabilities.notifier()'''
            return Phonon.BackendCapabilities.Notifier()
    class VolumeSlider(QWidget):
        """"""
        def __init__(self, parent = None):
            '''void Phonon.VolumeSlider.__init__(QWidget parent = None)'''
        def __init__(self, parent = None):
            '''Phonon.AudioOutput Phonon.VolumeSlider.__init__(QWidget parent = None)'''
            return Phonon.AudioOutput()
        def setAudioOutput(self):
            '''Phonon.AudioOutput Phonon.VolumeSlider.setAudioOutput()'''
            return Phonon.AudioOutput()
        def setIconSize(self, size):
            '''void Phonon.VolumeSlider.setIconSize(QSize size)'''
        def setMuteVisible(self):
            '''bool Phonon.VolumeSlider.setMuteVisible()'''
            return bool()
        def setOrientation(self):
            '''Qt.Orientation Phonon.VolumeSlider.setOrientation()'''
            return Qt.Orientation()
        def setMaximumVolume(self):
            '''float Phonon.VolumeSlider.setMaximumVolume()'''
            return float()
        def audioOutput(self):
            '''Phonon.AudioOutput Phonon.VolumeSlider.audioOutput()'''
            return Phonon.AudioOutput()
        def orientation(self):
            '''Qt.Orientation Phonon.VolumeSlider.orientation()'''
            return Qt.Orientation()
        def maximumVolume(self):
            '''float Phonon.VolumeSlider.maximumVolume()'''
            return float()
        def iconSize(self):
            '''QSize Phonon.VolumeSlider.iconSize()'''
            return QSize()
        def isMuteVisible(self):
            '''bool Phonon.VolumeSlider.isMuteVisible()'''
            return bool()
        def setSingleStep(self, milliseconds):
            '''void Phonon.VolumeSlider.setSingleStep(int milliseconds)'''
        def singleStep(self):
            '''int Phonon.VolumeSlider.singleStep()'''
            return int()
        def setPageStep(self, milliseconds):
            '''void Phonon.VolumeSlider.setPageStep(int milliseconds)'''
        def pageStep(self):
            '''int Phonon.VolumeSlider.pageStep()'''
            return int()
        def setTracking(self, tracking):
            '''void Phonon.VolumeSlider.setTracking(bool tracking)'''
        def hasTracking(self):
            '''bool Phonon.VolumeSlider.hasTracking()'''
            return bool()
    class VideoPlayer(QWidget):
        """"""
        def __init__(self, category, parent = None):
            '''void Phonon.VideoPlayer.__init__(Phonon.Category category, QWidget parent = None)'''
        def __init__(self, parent = None):
            '''void Phonon.VideoPlayer.__init__(QWidget parent = None)'''
        finished = pyqtSignal() # void finished() - signal
        def videoWidget(self):
            '''Phonon.VideoWidget Phonon.VideoPlayer.videoWidget()'''
            return Phonon.VideoWidget()
        def audioOutput(self):
            '''Phonon.AudioOutput Phonon.VideoPlayer.audioOutput()'''
            return Phonon.AudioOutput()
        def mediaObject(self):
            '''Phonon.MediaObject Phonon.VideoPlayer.mediaObject()'''
            return Phonon.MediaObject()
        def setVolume(self, volume):
            '''void Phonon.VideoPlayer.setVolume(float volume)'''
        def seek(self, ms):
            '''void Phonon.VideoPlayer.seek(int ms)'''
        def stop(self):
            '''void Phonon.VideoPlayer.stop()'''
        def pause(self):
            '''void Phonon.VideoPlayer.pause()'''
        def play(self, source):
            '''void Phonon.VideoPlayer.play(Phonon.MediaSource source)'''
        def play(self):
            '''void Phonon.VideoPlayer.play()'''
        def load(self, source):
            '''void Phonon.VideoPlayer.load(Phonon.MediaSource source)'''
        def isPaused(self):
            '''bool Phonon.VideoPlayer.isPaused()'''
            return bool()
        def isPlaying(self):
            '''bool Phonon.VideoPlayer.isPlaying()'''
            return bool()
        def volume(self):
            '''float Phonon.VideoPlayer.volume()'''
            return float()
        def currentTime(self):
            '''int Phonon.VideoPlayer.currentTime()'''
            return int()
        def totalTime(self):
            '''int Phonon.VideoPlayer.totalTime()'''
            return int()
    class AbstractVideoOutput(Phonon.MediaNode):
        """"""
    class VideoWidget(QWidget, Phonon.AbstractVideoOutput):
        """"""
        # Enum Phonon.VideoWidget.ScaleMode
        FitInView = 0
        ScaleAndCrop = 0
    
        # Enum Phonon.VideoWidget.AspectRatio
        AspectRatioAuto = 0
        AspectRatioWidget = 0
        AspectRatio4_3 = 0
        AspectRatio16_9 = 0
    
        def __init__(self, parent = None):
            '''void Phonon.VideoWidget.__init__(QWidget parent = None)'''
        def snapshot(self):
            '''QImage Phonon.VideoWidget.snapshot()'''
            return QImage()
        def event(self):
            '''QEvent Phonon.VideoWidget.event()'''
            return QEvent()
        def mouseMoveEvent(self):
            '''QMouseEvent Phonon.VideoWidget.mouseMoveEvent()'''
            return QMouseEvent()
        def setSaturation(self, value):
            '''void Phonon.VideoWidget.setSaturation(float value)'''
        def setHue(self, value):
            '''void Phonon.VideoWidget.setHue(float value)'''
        def setContrast(self, value):
            '''void Phonon.VideoWidget.setContrast(float value)'''
        def setBrightness(self, value):
            '''void Phonon.VideoWidget.setBrightness(float value)'''
        def setScaleMode(self):
            '''Phonon.VideoWidget.ScaleMode Phonon.VideoWidget.setScaleMode()'''
            return Phonon.VideoWidget.ScaleMode()
        def setAspectRatio(self):
            '''Phonon.VideoWidget.AspectRatio Phonon.VideoWidget.setAspectRatio()'''
            return Phonon.VideoWidget.AspectRatio()
        def enterFullScreen(self):
            '''void Phonon.VideoWidget.enterFullScreen()'''
        def exitFullScreen(self):
            '''void Phonon.VideoWidget.exitFullScreen()'''
        def setFullScreen(self, fullscreen):
            '''void Phonon.VideoWidget.setFullScreen(bool fullscreen)'''
        def saturation(self):
            '''float Phonon.VideoWidget.saturation()'''
            return float()
        def hue(self):
            '''float Phonon.VideoWidget.hue()'''
            return float()
        def contrast(self):
            '''float Phonon.VideoWidget.contrast()'''
            return float()
        def brightness(self):
            '''float Phonon.VideoWidget.brightness()'''
            return float()
        def scaleMode(self):
            '''Phonon.VideoWidget.ScaleMode Phonon.VideoWidget.scaleMode()'''
            return Phonon.VideoWidget.ScaleMode()
        def aspectRatio(self):
            '''Phonon.VideoWidget.AspectRatio Phonon.VideoWidget.aspectRatio()'''
            return Phonon.VideoWidget.AspectRatio()
    class Path():
        """"""
        def __init__(self):
            '''void Phonon.Path.__init__()'''
        def __init__(self):
            '''Phonon.Path Phonon.Path.__init__()'''
            return Phonon.Path()
        def sink(self):
            '''Phonon.MediaNode Phonon.Path.sink()'''
            return Phonon.MediaNode()
        def source(self):
            '''Phonon.MediaNode Phonon.Path.source()'''
            return Phonon.MediaNode()
        def __ne__(self, p):
            '''bool Phonon.Path.__ne__(Phonon.Path p)'''
            return bool()
        def __eq__(self, p):
            '''bool Phonon.Path.__eq__(Phonon.Path p)'''
            return bool()
        def disconnect(self):
            '''bool Phonon.Path.disconnect()'''
            return bool()
        def reconnect(self, source, sink):
            '''bool Phonon.Path.reconnect(Phonon.MediaNode source, Phonon.MediaNode sink)'''
            return bool()
        def effects(self):
            '''list-of-Phonon.Effect Phonon.Path.effects()'''
            return [Phonon.Effect()]
        def removeEffect(self, effect):
            '''bool Phonon.Path.removeEffect(Phonon.Effect effect)'''
            return bool()
        def insertEffect(self, desc, before = None):
            '''Phonon.Effect Phonon.Path.insertEffect(Phonon.EffectDescription desc, Phonon.Effect before = None)'''
            return Phonon.Effect()
        def insertEffect(self, newEffect, before = None):
            '''bool Phonon.Path.insertEffect(Phonon.Effect newEffect, Phonon.Effect before = None)'''
            return bool()
        def isValid(self):
            '''bool Phonon.Path.isValid()'''
            return bool()
    class EffectParameter():
        """"""
        # Enum Phonon.EffectParameter.Hint
        ToggledHint = 0
        LogarithmicHint = 0
        IntegerHint = 0
    
        def __init__(self, parameterId, name, hints, defaultValue, min = QVariant(), max = QVariant(), values = None, description = QString()):
            '''void Phonon.EffectParameter.__init__(int parameterId, QString name, Phonon.EffectParameter.Hints hints, QVariant defaultValue, QVariant min = QVariant(), QVariant max = QVariant(), list-of-QVariant values = [], QString description = QString())'''
        def __init__(self, rhs):
            '''void Phonon.EffectParameter.__init__(Phonon.EffectParameter rhs)'''
        def __hash__(self):
            '''int Phonon.EffectParameter.__hash__()'''
            return int()
        def possibleValues(self):
            '''list-of-QVariant Phonon.EffectParameter.possibleValues()'''
            return [QVariant()]
        def defaultValue(self):
            '''QVariant Phonon.EffectParameter.defaultValue()'''
            return QVariant()
        def maximumValue(self):
            '''QVariant Phonon.EffectParameter.maximumValue()'''
            return QVariant()
        def minimumValue(self):
            '''QVariant Phonon.EffectParameter.minimumValue()'''
            return QVariant()
        def isLogarithmicControl(self):
            '''bool Phonon.EffectParameter.isLogarithmicControl()'''
            return bool()
        def type(self):
            '''Type Phonon.EffectParameter.type()'''
            return Type()
        def description(self):
            '''QString Phonon.EffectParameter.description()'''
            return QString()
        def name(self):
            '''QString Phonon.EffectParameter.name()'''
            return QString()
    class AudioCaptureDevice():
        """"""
        def __init__(self):
            '''void Phonon.AudioCaptureDevice.__init__()'''
        def __init__(self, index, properties):
            '''void Phonon.AudioCaptureDevice.__init__(int index, dict-of-QByteArray-QVariant properties)'''
        def __init__(self):
            '''Phonon.AudioCaptureDevice Phonon.AudioCaptureDevice.__init__()'''
            return Phonon.AudioCaptureDevice()
        def fromIndex(self, index):
            '''static Phonon.AudioCaptureDevice Phonon.AudioCaptureDevice.fromIndex(int index)'''
            return Phonon.AudioCaptureDevice()
        def __eq__(self, otherDescription):
            '''bool Phonon.AudioCaptureDevice.__eq__(Phonon.AudioCaptureDevice otherDescription)'''
            return bool()
        def __ne__(self, otherDescription):
            '''bool Phonon.AudioCaptureDevice.__ne__(Phonon.AudioCaptureDevice otherDescription)'''
            return bool()
        def propertyNames(self):
            '''list-of-QByteArray Phonon.AudioCaptureDevice.propertyNames()'''
            return [QByteArray()]
        def property(self, name):
            '''QVariant Phonon.AudioCaptureDevice.property(str name)'''
            return QVariant()
        def name(self):
            '''QString Phonon.AudioCaptureDevice.name()'''
            return QString()
        def isValid(self):
            '''bool Phonon.AudioCaptureDevice.isValid()'''
            return bool()
        def index(self):
            '''int Phonon.AudioCaptureDevice.index()'''
            return int()
        def description(self):
            '''QString Phonon.AudioCaptureDevice.description()'''
            return QString()
    class EffectWidget(QWidget):
        """"""
        def __init__(self, effect, parent = None):
            '''void Phonon.EffectWidget.__init__(Phonon.Effect effect, QWidget parent = None)'''
    class AudioOutput(Phonon.AbstractAudioOutput):
        """"""
        def __init__(self, category, parent = None):
            '''void Phonon.AudioOutput.__init__(Phonon.Category category, QObject parent = None)'''
        def __init__(self, parent = None):
            '''void Phonon.AudioOutput.__init__(QObject parent = None)'''
        outputDeviceChanged = pyqtSignal() # void outputDeviceChanged(const Phonon::AudioOutputDeviceamp;) - signal
        mutedChanged = pyqtSignal() # void mutedChanged(bool) - signal
        volumeChanged = pyqtSignal() # void volumeChanged(qreal) - signal
        def setMuted(self, mute):
            '''void Phonon.AudioOutput.setMuted(bool mute)'''
        def setOutputDevice(self, newAudioOutputDevice):
            '''bool Phonon.AudioOutput.setOutputDevice(Phonon.AudioOutputDevice newAudioOutputDevice)'''
            return bool()
        def setVolumeDecibel(self, newVolumeDecibel):
            '''void Phonon.AudioOutput.setVolumeDecibel(float newVolumeDecibel)'''
        def setVolume(self, newVolume):
            '''void Phonon.AudioOutput.setVolume(float newVolume)'''
        def setName(self, newName):
            '''void Phonon.AudioOutput.setName(QString newName)'''
        def isMuted(self):
            '''bool Phonon.AudioOutput.isMuted()'''
            return bool()
        def outputDevice(self):
            '''Phonon.AudioOutputDevice Phonon.AudioOutput.outputDevice()'''
            return Phonon.AudioOutputDevice()
        def category(self):
            '''Phonon.Category Phonon.AudioOutput.category()'''
            return Phonon.Category()
        def volumeDecibel(self):
            '''float Phonon.AudioOutput.volumeDecibel()'''
            return float()
        def volume(self):
            '''float Phonon.AudioOutput.volume()'''
            return float()
        def name(self):
            '''QString Phonon.AudioOutput.name()'''
            return QString()
    class MediaNode():
        """"""
        def outputPaths(self):
            '''list-of-Phonon.Path Phonon.MediaNode.outputPaths()'''
            return [Phonon.Path()]
        def inputPaths(self):
            '''list-of-Phonon.Path Phonon.MediaNode.inputPaths()'''
            return [Phonon.Path()]
        def isValid(self):
            '''bool Phonon.MediaNode.isValid()'''
            return bool()
    class SeekSlider(QWidget):
        """"""
        def __init__(self, parent = None):
            '''void Phonon.SeekSlider.__init__(QWidget parent = None)'''
        def __init__(self, media, parent = None):
            '''void Phonon.SeekSlider.__init__(Phonon.MediaObject media, QWidget parent = None)'''
        def setMediaObject(self):
            '''Phonon.MediaObject Phonon.SeekSlider.setMediaObject()'''
            return Phonon.MediaObject()
        def setIconSize(self, size):
            '''void Phonon.SeekSlider.setIconSize(QSize size)'''
        def setIconVisible(self):
            '''bool Phonon.SeekSlider.setIconVisible()'''
            return bool()
        def setOrientation(self):
            '''Qt.Orientation Phonon.SeekSlider.setOrientation()'''
            return Qt.Orientation()
        def mediaObject(self):
            '''Phonon.MediaObject Phonon.SeekSlider.mediaObject()'''
            return Phonon.MediaObject()
        def iconSize(self):
            '''QSize Phonon.SeekSlider.iconSize()'''
            return QSize()
        def isIconVisible(self):
            '''bool Phonon.SeekSlider.isIconVisible()'''
            return bool()
        def orientation(self):
            '''Qt.Orientation Phonon.SeekSlider.orientation()'''
            return Qt.Orientation()
        def setSingleStep(self, milliseconds):
            '''void Phonon.SeekSlider.setSingleStep(int milliseconds)'''
        def singleStep(self):
            '''int Phonon.SeekSlider.singleStep()'''
            return int()
        def setPageStep(self, milliseconds):
            '''void Phonon.SeekSlider.setPageStep(int milliseconds)'''
        def pageStep(self):
            '''int Phonon.SeekSlider.pageStep()'''
            return int()
        def setTracking(self, tracking):
            '''void Phonon.SeekSlider.setTracking(bool tracking)'''
        def hasTracking(self):
            '''bool Phonon.SeekSlider.hasTracking()'''
            return bool()
    class EffectParameter():
        """"""
        class Hints():
            """"""
            def __init__(self):
                '''Phonon.EffectParameter.Hints Phonon.EffectParameter.Hints.__init__()'''
                return Phonon.EffectParameter.Hints()
            def __init__(self):
                '''int Phonon.EffectParameter.Hints.__init__()'''
                return int()
            def __init__(self):
                '''void Phonon.EffectParameter.Hints.__init__()'''
            def __bool__(self):
                '''int Phonon.EffectParameter.Hints.__bool__()'''
                return int()
            def __ne__(self, f):
                '''bool Phonon.EffectParameter.Hints.__ne__(Phonon.EffectParameter.Hints f)'''
                return bool()
            def __eq__(self, f):
                '''bool Phonon.EffectParameter.Hints.__eq__(Phonon.EffectParameter.Hints f)'''
                return bool()
            def __invert__(self):
                '''Phonon.EffectParameter.Hints Phonon.EffectParameter.Hints.__invert__()'''
                return Phonon.EffectParameter.Hints()
            def __and__(self, mask):
                '''Phonon.EffectParameter.Hints Phonon.EffectParameter.Hints.__and__(int mask)'''
                return Phonon.EffectParameter.Hints()
            def __xor__(self, f):
                '''Phonon.EffectParameter.Hints Phonon.EffectParameter.Hints.__xor__(Phonon.EffectParameter.Hints f)'''
                return Phonon.EffectParameter.Hints()
            def __xor__(self, f):
                '''Phonon.EffectParameter.Hints Phonon.EffectParameter.Hints.__xor__(int f)'''
                return Phonon.EffectParameter.Hints()
            def __or__(self, f):
                '''Phonon.EffectParameter.Hints Phonon.EffectParameter.Hints.__or__(Phonon.EffectParameter.Hints f)'''
                return Phonon.EffectParameter.Hints()
            def __or__(self, f):
                '''Phonon.EffectParameter.Hints Phonon.EffectParameter.Hints.__or__(int f)'''
                return Phonon.EffectParameter.Hints()
            def __int__(self):
                '''int Phonon.EffectParameter.Hints.__int__()'''
                return int()
            def __ixor__(self, f):
                '''Phonon.EffectParameter.Hints Phonon.EffectParameter.Hints.__ixor__(Phonon.EffectParameter.Hints f)'''
                return Phonon.EffectParameter.Hints()
            def __ior__(self, f):
                '''Phonon.EffectParameter.Hints Phonon.EffectParameter.Hints.__ior__(Phonon.EffectParameter.Hints f)'''
                return Phonon.EffectParameter.Hints()
            def __iand__(self, mask):
                '''Phonon.EffectParameter.Hints Phonon.EffectParameter.Hints.__iand__(int mask)'''
                return Phonon.EffectParameter.Hints()
    class BackendCapabilities():
        """"""
        class Notifier(QObject):
            """"""
            availableAudioCaptureDevicesChanged = pyqtSignal() # void availableAudioCaptureDevicesChanged() - signal
            availableAudioOutputDevicesChanged = pyqtSignal() # void availableAudioOutputDevicesChanged() - signal
            capabilitiesChanged = pyqtSignal() # void capabilitiesChanged() - signal
    class MediaController(QObject):
        """"""
        # Enum Phonon.MediaController.Feature
        Angles = 0
        Chapters = 0
        Titles = 0
    
        def __init__(self, parent):
            '''void Phonon.MediaController.__init__(Phonon.MediaObject parent)'''
        availableAudioChannelsChanged = pyqtSignal() # void availableAudioChannelsChanged() - signal
        availableSubtitlesChanged = pyqtSignal() # void availableSubtitlesChanged() - signal
        def setCurrentSubtitle(self, stream):
            '''void Phonon.MediaController.setCurrentSubtitle(Phonon.SubtitleDescription stream)'''
        def setCurrentAudioChannel(self, stream):
            '''void Phonon.MediaController.setCurrentAudioChannel(Phonon.AudioChannelDescription stream)'''
        def availableSubtitles(self):
            '''list-of-Phonon.SubtitleDescription Phonon.MediaController.availableSubtitles()'''
            return [Phonon.SubtitleDescription()]
        def availableAudioChannels(self):
            '''list-of-Phonon.AudioChannelDescription Phonon.MediaController.availableAudioChannels()'''
            return [Phonon.AudioChannelDescription()]
        def currentSubtitle(self):
            '''Phonon.SubtitleDescription Phonon.MediaController.currentSubtitle()'''
            return Phonon.SubtitleDescription()
        def currentAudioChannel(self):
            '''Phonon.AudioChannelDescription Phonon.MediaController.currentAudioChannel()'''
            return Phonon.AudioChannelDescription()
        titleChanged = pyqtSignal() # void titleChanged(int) - signal
        availableTitlesChanged = pyqtSignal() # void availableTitlesChanged(int) - signal
        chapterChanged = pyqtSignal() # void chapterChanged(int) - signal
        availableChaptersChanged = pyqtSignal() # void availableChaptersChanged(int) - signal
        angleChanged = pyqtSignal() # void angleChanged(int) - signal
        availableAnglesChanged = pyqtSignal() # void availableAnglesChanged(int) - signal
        def previousTitle(self):
            '''void Phonon.MediaController.previousTitle()'''
        def nextTitle(self):
            '''void Phonon.MediaController.nextTitle()'''
        def setAutoplayTitles(self):
            '''bool Phonon.MediaController.setAutoplayTitles()'''
            return bool()
        def setCurrentTitle(self, titleNumber):
            '''void Phonon.MediaController.setCurrentTitle(int titleNumber)'''
        def setCurrentChapter(self, chapterNumber):
            '''void Phonon.MediaController.setCurrentChapter(int chapterNumber)'''
        def setCurrentAngle(self, angleNumber):
            '''void Phonon.MediaController.setCurrentAngle(int angleNumber)'''
        def autoplayTitles(self):
            '''bool Phonon.MediaController.autoplayTitles()'''
            return bool()
        def currentTitle(self):
            '''int Phonon.MediaController.currentTitle()'''
            return int()
        def availableTitles(self):
            '''int Phonon.MediaController.availableTitles()'''
            return int()
        def currentChapter(self):
            '''int Phonon.MediaController.currentChapter()'''
            return int()
        def availableChapters(self):
            '''int Phonon.MediaController.availableChapters()'''
            return int()
        def currentAngle(self):
            '''int Phonon.MediaController.currentAngle()'''
            return int()
        def availableAngles(self):
            '''int Phonon.MediaController.availableAngles()'''
            return int()
        def supportedFeatures(self):
            '''Phonon.MediaController.Features Phonon.MediaController.supportedFeatures()'''
            return Phonon.MediaController.Features()
    class MediaSource():
        """"""
        # Enum Phonon.MediaSource.Type
        Invalid = 0
        LocalFile = 0
        Url = 0
        Disc = 0
        Stream = 0
        Empty = 0
    
        def __init__(self, fileName):
            '''void Phonon.MediaSource.__init__(QString fileName)'''
        def __init__(self, url):
            '''void Phonon.MediaSource.__init__(QUrl url)'''
        def __init__(self, discType, deviceName = QString()):
            '''void Phonon.MediaSource.__init__(Phonon.DiscType discType, QString deviceName = QString())'''
        def __init__(self, ioDevice):
            '''void Phonon.MediaSource.__init__(QIODevice ioDevice)'''
        def __init__(self, rhs):
            '''void Phonon.MediaSource.__init__(Phonon.MediaSource rhs)'''
        def __ne__(self, rhs):
            '''bool Phonon.MediaSource.__ne__(Phonon.MediaSource rhs)'''
            return bool()
        def deviceName(self):
            '''QString Phonon.MediaSource.deviceName()'''
            return QString()
        def discType(self):
            '''Phonon.DiscType Phonon.MediaSource.discType()'''
            return Phonon.DiscType()
        def url(self):
            '''QUrl Phonon.MediaSource.url()'''
            return QUrl()
        def fileName(self):
            '''QString Phonon.MediaSource.fileName()'''
            return QString()
        def type(self):
            '''Phonon.MediaSource.Type Phonon.MediaSource.type()'''
            return Phonon.MediaSource.Type()
        def autoDelete(self):
            '''bool Phonon.MediaSource.autoDelete()'''
            return bool()
        def setAutoDelete(self, enable):
            '''void Phonon.MediaSource.setAutoDelete(bool enable)'''
        def __eq__(self, rhs):
            '''bool Phonon.MediaSource.__eq__(Phonon.MediaSource rhs)'''
            return bool()
    class AudioOutputDevice():
        """"""
        def __init__(self):
            '''void Phonon.AudioOutputDevice.__init__()'''
        def __init__(self, index, properties):
            '''void Phonon.AudioOutputDevice.__init__(int index, dict-of-QByteArray-QVariant properties)'''
        def __init__(self):
            '''Phonon.AudioOutputDevice Phonon.AudioOutputDevice.__init__()'''
            return Phonon.AudioOutputDevice()
        def fromIndex(self, index):
            '''static Phonon.AudioOutputDevice Phonon.AudioOutputDevice.fromIndex(int index)'''
            return Phonon.AudioOutputDevice()
        def __eq__(self, otherDescription):
            '''bool Phonon.AudioOutputDevice.__eq__(Phonon.AudioOutputDevice otherDescription)'''
            return bool()
        def __ne__(self, otherDescription):
            '''bool Phonon.AudioOutputDevice.__ne__(Phonon.AudioOutputDevice otherDescription)'''
            return bool()
        def propertyNames(self):
            '''list-of-QByteArray Phonon.AudioOutputDevice.propertyNames()'''
            return [QByteArray()]
        def property(self, name):
            '''QVariant Phonon.AudioOutputDevice.property(str name)'''
            return QVariant()
        def name(self):
            '''QString Phonon.AudioOutputDevice.name()'''
            return QString()
        def isValid(self):
            '''bool Phonon.AudioOutputDevice.isValid()'''
            return bool()
        def index(self):
            '''int Phonon.AudioOutputDevice.index()'''
            return int()
        def description(self):
            '''QString Phonon.AudioOutputDevice.description()'''
            return QString()
    class AudioOutputDeviceModel(QAbstractListModel):
        """"""
        def __init__(self, parent = None):
            '''void Phonon.AudioOutputDeviceModel.__init__(QObject parent = None)'''
        def __init__(self, data, parent = None):
            '''void Phonon.AudioOutputDeviceModel.__init__(list-of-Phonon.AudioOutputDevice data, QObject parent = None)'''
        def mimeTypes(self):
            '''QStringList Phonon.AudioOutputDeviceModel.mimeTypes()'''
            return QStringList()
        def removeRows(self, row, count, parent = QModelIndex()):
            '''bool Phonon.AudioOutputDeviceModel.removeRows(int row, int count, QModelIndex parent = QModelIndex())'''
            return bool()
        def dropMimeData(self, data, action, row, column, parent):
            '''bool Phonon.AudioOutputDeviceModel.dropMimeData(QMimeData data, Qt.DropAction action, int row, int column, QModelIndex parent)'''
            return bool()
        def supportedDropActions(self):
            '''Qt.DropActions Phonon.AudioOutputDeviceModel.supportedDropActions()'''
            return Qt.DropActions()
        def mimeData(self, indexes):
            '''QMimeData Phonon.AudioOutputDeviceModel.mimeData(list-of-QModelIndex indexes)'''
            return QMimeData()
        def flags(self, index):
            '''Qt.ItemFlags Phonon.AudioOutputDeviceModel.flags(QModelIndex index)'''
            return Qt.ItemFlags()
        def data(self, index, role = None):
            '''QVariant Phonon.AudioOutputDeviceModel.data(QModelIndex index, int role = Qt.DisplayRole)'''
            return QVariant()
        def rowCount(self, parent = QModelIndex()):
            '''int Phonon.AudioOutputDeviceModel.rowCount(QModelIndex parent = QModelIndex())'''
            return int()
        def modelData(self):
            '''list-of-Phonon.AudioOutputDevice Phonon.AudioOutputDeviceModel.modelData()'''
            return [Phonon.AudioOutputDevice()]
        def modelData(self, index):
            '''Phonon.AudioOutputDevice Phonon.AudioOutputDeviceModel.modelData(QModelIndex index)'''
            return Phonon.AudioOutputDevice()
        def setModelData(self, data):
            '''void Phonon.AudioOutputDeviceModel.setModelData(list-of-Phonon.AudioOutputDevice data)'''
        def moveDown(self, index):
            '''void Phonon.AudioOutputDeviceModel.moveDown(QModelIndex index)'''
        def moveUp(self, index):
            '''void Phonon.AudioOutputDeviceModel.moveUp(QModelIndex index)'''
        def tupleIndexAtPositionIndex(self, positionIndex):
            '''int Phonon.AudioOutputDeviceModel.tupleIndexAtPositionIndex(int positionIndex)'''
            return int()
        def tupleIndexOrder(self):
            '''list-of-int Phonon.AudioOutputDeviceModel.tupleIndexOrder()'''
            return [int()]
    class EffectDescriptionModel(QAbstractListModel):
        """"""
        def __init__(self, parent = None):
            '''void Phonon.EffectDescriptionModel.__init__(QObject parent = None)'''
        def __init__(self, data, parent = None):
            '''void Phonon.EffectDescriptionModel.__init__(list-of-Phonon.EffectDescription data, QObject parent = None)'''
        def mimeTypes(self):
            '''QStringList Phonon.EffectDescriptionModel.mimeTypes()'''
            return QStringList()
        def removeRows(self, row, count, parent = QModelIndex()):
            '''bool Phonon.EffectDescriptionModel.removeRows(int row, int count, QModelIndex parent = QModelIndex())'''
            return bool()
        def dropMimeData(self, data, action, row, column, parent):
            '''bool Phonon.EffectDescriptionModel.dropMimeData(QMimeData data, Qt.DropAction action, int row, int column, QModelIndex parent)'''
            return bool()
        def supportedDropActions(self):
            '''Qt.DropActions Phonon.EffectDescriptionModel.supportedDropActions()'''
            return Qt.DropActions()
        def mimeData(self, indexes):
            '''QMimeData Phonon.EffectDescriptionModel.mimeData(list-of-QModelIndex indexes)'''
            return QMimeData()
        def flags(self, index):
            '''Qt.ItemFlags Phonon.EffectDescriptionModel.flags(QModelIndex index)'''
            return Qt.ItemFlags()
        def data(self, index, role = None):
            '''QVariant Phonon.EffectDescriptionModel.data(QModelIndex index, int role = Qt.DisplayRole)'''
            return QVariant()
        def rowCount(self, parent = QModelIndex()):
            '''int Phonon.EffectDescriptionModel.rowCount(QModelIndex parent = QModelIndex())'''
            return int()
        def modelData(self):
            '''list-of-Phonon.EffectDescription Phonon.EffectDescriptionModel.modelData()'''
            return [Phonon.EffectDescription()]
        def modelData(self, index):
            '''Phonon.EffectDescription Phonon.EffectDescriptionModel.modelData(QModelIndex index)'''
            return Phonon.EffectDescription()
        def setModelData(self, data):
            '''void Phonon.EffectDescriptionModel.setModelData(list-of-Phonon.EffectDescription data)'''
        def moveDown(self, index):
            '''void Phonon.EffectDescriptionModel.moveDown(QModelIndex index)'''
        def moveUp(self, index):
            '''void Phonon.EffectDescriptionModel.moveUp(QModelIndex index)'''
        def tupleIndexAtPositionIndex(self, positionIndex):
            '''int Phonon.EffectDescriptionModel.tupleIndexAtPositionIndex(int positionIndex)'''
            return int()
        def tupleIndexOrder(self):
            '''list-of-int Phonon.EffectDescriptionModel.tupleIndexOrder()'''
            return [int()]
    class MediaController():
        """"""
        class Features():
            """"""
            def __init__(self):
                '''Phonon.MediaController.Features Phonon.MediaController.Features.__init__()'''
                return Phonon.MediaController.Features()
            def __init__(self):
                '''int Phonon.MediaController.Features.__init__()'''
                return int()
            def __init__(self):
                '''void Phonon.MediaController.Features.__init__()'''
            def __bool__(self):
                '''int Phonon.MediaController.Features.__bool__()'''
                return int()
            def __ne__(self, f):
                '''bool Phonon.MediaController.Features.__ne__(Phonon.MediaController.Features f)'''
                return bool()
            def __eq__(self, f):
                '''bool Phonon.MediaController.Features.__eq__(Phonon.MediaController.Features f)'''
                return bool()
            def __invert__(self):
                '''Phonon.MediaController.Features Phonon.MediaController.Features.__invert__()'''
                return Phonon.MediaController.Features()
            def __and__(self, mask):
                '''Phonon.MediaController.Features Phonon.MediaController.Features.__and__(int mask)'''
                return Phonon.MediaController.Features()
            def __xor__(self, f):
                '''Phonon.MediaController.Features Phonon.MediaController.Features.__xor__(Phonon.MediaController.Features f)'''
                return Phonon.MediaController.Features()
            def __xor__(self, f):
                '''Phonon.MediaController.Features Phonon.MediaController.Features.__xor__(int f)'''
                return Phonon.MediaController.Features()
            def __or__(self, f):
                '''Phonon.MediaController.Features Phonon.MediaController.Features.__or__(Phonon.MediaController.Features f)'''
                return Phonon.MediaController.Features()
            def __or__(self, f):
                '''Phonon.MediaController.Features Phonon.MediaController.Features.__or__(int f)'''
                return Phonon.MediaController.Features()
            def __int__(self):
                '''int Phonon.MediaController.Features.__int__()'''
                return int()
            def __ixor__(self, f):
                '''Phonon.MediaController.Features Phonon.MediaController.Features.__ixor__(Phonon.MediaController.Features f)'''
                return Phonon.MediaController.Features()
            def __ior__(self, f):
                '''Phonon.MediaController.Features Phonon.MediaController.Features.__ior__(Phonon.MediaController.Features f)'''
                return Phonon.MediaController.Features()
            def __iand__(self, mask):
                '''Phonon.MediaController.Features Phonon.MediaController.Features.__iand__(int mask)'''
                return Phonon.MediaController.Features()
    class AudioChannelDescription():
        """"""
        def __init__(self):
            '''void Phonon.AudioChannelDescription.__init__()'''
        def __init__(self, index, properties):
            '''void Phonon.AudioChannelDescription.__init__(int index, dict-of-QByteArray-QVariant properties)'''
        def __init__(self):
            '''Phonon.AudioChannelDescription Phonon.AudioChannelDescription.__init__()'''
            return Phonon.AudioChannelDescription()
        def fromIndex(self, index):
            '''static Phonon.AudioChannelDescription Phonon.AudioChannelDescription.fromIndex(int index)'''
            return Phonon.AudioChannelDescription()
        def __eq__(self, otherDescription):
            '''bool Phonon.AudioChannelDescription.__eq__(Phonon.AudioChannelDescription otherDescription)'''
            return bool()
        def __ne__(self, otherDescription):
            '''bool Phonon.AudioChannelDescription.__ne__(Phonon.AudioChannelDescription otherDescription)'''
            return bool()
        def propertyNames(self):
            '''list-of-QByteArray Phonon.AudioChannelDescription.propertyNames()'''
            return [QByteArray()]
        def property(self, name):
            '''QVariant Phonon.AudioChannelDescription.property(str name)'''
            return QVariant()
        def name(self):
            '''QString Phonon.AudioChannelDescription.name()'''
            return QString()
        def isValid(self):
            '''bool Phonon.AudioChannelDescription.isValid()'''
            return bool()
        def index(self):
            '''int Phonon.AudioChannelDescription.index()'''
            return int()
        def description(self):
            '''QString Phonon.AudioChannelDescription.description()'''
            return QString()
    class EffectDescription():
        """"""
        def __init__(self):
            '''void Phonon.EffectDescription.__init__()'''
        def __init__(self, index, properties):
            '''void Phonon.EffectDescription.__init__(int index, dict-of-QByteArray-QVariant properties)'''
        def __init__(self):
            '''Phonon.EffectDescription Phonon.EffectDescription.__init__()'''
            return Phonon.EffectDescription()
        def fromIndex(self, index):
            '''static Phonon.EffectDescription Phonon.EffectDescription.fromIndex(int index)'''
            return Phonon.EffectDescription()
        def __eq__(self, otherDescription):
            '''bool Phonon.EffectDescription.__eq__(Phonon.EffectDescription otherDescription)'''
            return bool()
        def __ne__(self, otherDescription):
            '''bool Phonon.EffectDescription.__ne__(Phonon.EffectDescription otherDescription)'''
            return bool()
        def propertyNames(self):
            '''list-of-QByteArray Phonon.EffectDescription.propertyNames()'''
            return [QByteArray()]
        def property(self, name):
            '''QVariant Phonon.EffectDescription.property(str name)'''
            return QVariant()
        def name(self):
            '''QString Phonon.EffectDescription.name()'''
            return QString()
        def isValid(self):
            '''bool Phonon.EffectDescription.isValid()'''
            return bool()
        def index(self):
            '''int Phonon.EffectDescription.index()'''
            return int()
        def description(self):
            '''QString Phonon.EffectDescription.description()'''
            return QString()
    class SubtitleDescription():
        """"""
        def __init__(self):
            '''void Phonon.SubtitleDescription.__init__()'''
        def __init__(self, index, properties):
            '''void Phonon.SubtitleDescription.__init__(int index, dict-of-QByteArray-QVariant properties)'''
        def __init__(self):
            '''Phonon.SubtitleDescription Phonon.SubtitleDescription.__init__()'''
            return Phonon.SubtitleDescription()
        def fromIndex(self, index):
            '''static Phonon.SubtitleDescription Phonon.SubtitleDescription.fromIndex(int index)'''
            return Phonon.SubtitleDescription()
        def __eq__(self, otherDescription):
            '''bool Phonon.SubtitleDescription.__eq__(Phonon.SubtitleDescription otherDescription)'''
            return bool()
        def __ne__(self, otherDescription):
            '''bool Phonon.SubtitleDescription.__ne__(Phonon.SubtitleDescription otherDescription)'''
            return bool()
        def propertyNames(self):
            '''list-of-QByteArray Phonon.SubtitleDescription.propertyNames()'''
            return [QByteArray()]
        def property(self, name):
            '''QVariant Phonon.SubtitleDescription.property(str name)'''
            return QVariant()
        def name(self):
            '''QString Phonon.SubtitleDescription.name()'''
            return QString()
        def isValid(self):
            '''bool Phonon.SubtitleDescription.isValid()'''
            return bool()
        def index(self):
            '''int Phonon.SubtitleDescription.index()'''
            return int()
        def description(self):
            '''QString Phonon.SubtitleDescription.description()'''
            return QString()
    class AbstractAudioOutput(QObject, Phonon.MediaNode):
        """"""
    class MediaObject(QObject, Phonon.MediaNode):
        """"""
        def __init__(self, parent = None):
            '''void Phonon.MediaObject.__init__(QObject parent = None)'''
        totalTimeChanged = pyqtSignal() # void totalTimeChanged(qint64) - signal
        prefinishMarkReached = pyqtSignal() # void prefinishMarkReached(qint32) - signal
        aboutToFinish = pyqtSignal() # void aboutToFinish() - signal
        currentSourceChanged = pyqtSignal() # void currentSourceChanged(const Phonon::MediaSourceamp;) - signal
        finished = pyqtSignal() # void finished() - signal
        bufferStatus = pyqtSignal() # void bufferStatus(int) - signal
        hasVideoChanged = pyqtSignal() # void hasVideoChanged(bool) - signal
        seekableChanged = pyqtSignal() # void seekableChanged(bool) - signal
        metaDataChanged = pyqtSignal() # void metaDataChanged() - signal
        tick = pyqtSignal() # void tick(qint64) - signal
        stateChanged = pyqtSignal() # void stateChanged(Phonon::State,Phonon::State) - signal
        def clear(self):
            '''void Phonon.MediaObject.clear()'''
        def seek(self, time):
            '''void Phonon.MediaObject.seek(int time)'''
        def stop(self):
            '''void Phonon.MediaObject.stop()'''
        def pause(self):
            '''void Phonon.MediaObject.pause()'''
        def play(self):
            '''void Phonon.MediaObject.play()'''
        def setTickInterval(self, newTickInterval):
            '''void Phonon.MediaObject.setTickInterval(int newTickInterval)'''
        def setTransitionTime(self, msec):
            '''void Phonon.MediaObject.setTransitionTime(int msec)'''
        def transitionTime(self):
            '''int Phonon.MediaObject.transitionTime()'''
            return int()
        def setPrefinishMark(self, msecToEnd):
            '''void Phonon.MediaObject.setPrefinishMark(int msecToEnd)'''
        def prefinishMark(self):
            '''int Phonon.MediaObject.prefinishMark()'''
            return int()
        def remainingTime(self):
            '''int Phonon.MediaObject.remainingTime()'''
            return int()
        def totalTime(self):
            '''int Phonon.MediaObject.totalTime()'''
            return int()
        def currentTime(self):
            '''int Phonon.MediaObject.currentTime()'''
            return int()
        def clearQueue(self):
            '''void Phonon.MediaObject.clearQueue()'''
        def enqueue(self, source):
            '''void Phonon.MediaObject.enqueue(Phonon.MediaSource source)'''
        def enqueue(self, sources):
            '''void Phonon.MediaObject.enqueue(list-of-Phonon.MediaSource sources)'''
        def enqueue(self, urls):
            '''void Phonon.MediaObject.enqueue(list-of-QUrl urls)'''
        def setQueue(self, sources):
            '''void Phonon.MediaObject.setQueue(list-of-Phonon.MediaSource sources)'''
        def setQueue(self, urls):
            '''void Phonon.MediaObject.setQueue(list-of-QUrl urls)'''
        def queue(self):
            '''list-of-Phonon.MediaSource Phonon.MediaObject.queue()'''
            return [Phonon.MediaSource()]
        def setCurrentSource(self, source):
            '''void Phonon.MediaObject.setCurrentSource(Phonon.MediaSource source)'''
        def currentSource(self):
            '''Phonon.MediaSource Phonon.MediaObject.currentSource()'''
            return Phonon.MediaSource()
        def errorType(self):
            '''Phonon.ErrorType Phonon.MediaObject.errorType()'''
            return Phonon.ErrorType()
        def errorString(self):
            '''QString Phonon.MediaObject.errorString()'''
            return QString()
        def metaData(self, key):
            '''QStringList Phonon.MediaObject.metaData(QString key)'''
            return QStringList()
        def metaData(self, key):
            '''QStringList Phonon.MediaObject.metaData(Phonon.MetaData key)'''
            return QStringList()
        def metaData(self):
            '''dict-of-QString-list-of-QString Phonon.MediaObject.metaData()'''
            return dict-of-QString-list-of-QString()
        def tickInterval(self):
            '''int Phonon.MediaObject.tickInterval()'''
            return int()
        def isSeekable(self):
            '''bool Phonon.MediaObject.isSeekable()'''
            return bool()
        def hasVideo(self):
            '''bool Phonon.MediaObject.hasVideo()'''
            return bool()
        def state(self):
            '''Phonon.State Phonon.MediaObject.state()'''
            return Phonon.State()


