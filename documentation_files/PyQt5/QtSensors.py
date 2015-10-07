class pyqtSignal():
 def connect(self, targetSignal): pass
 def emit(self, *args): pass
from QtCore import *

from QtWidgets import *

import datetime

class QSensorReading(QObject):
    """"""
    def value(self, index):
        '''QVariant QSensorReading.value(int index)'''
        return QVariant()
    def valueCount(self):
        '''int QSensorReading.valueCount()'''
        return int()
    def setTimestamp(self, timestamp):
        '''void QSensorReading.setTimestamp(int timestamp)'''
    def timestamp(self):
        '''int QSensorReading.timestamp()'''
        return int()


class QAccelerometerReading(QSensorReading):
    """"""
    def setZ(self, z):
        '''void QAccelerometerReading.setZ(float z)'''
    def z(self):
        '''float QAccelerometerReading.z()'''
        return float()
    def setY(self, y):
        '''void QAccelerometerReading.setY(float y)'''
    def y(self):
        '''float QAccelerometerReading.y()'''
        return float()
    def setX(self, x):
        '''void QAccelerometerReading.setX(float x)'''
    def x(self):
        '''float QAccelerometerReading.x()'''
        return float()


class QSensorFilter():
    """"""
    def __init__(self):
        '''void QSensorFilter.__init__()'''
    def __init__(self):
        '''QSensorFilter QSensorFilter.__init__()'''
        return QSensorFilter()
    def filter(self, reading):
        '''abstract bool QSensorFilter.filter(QSensorReading reading)'''
        return bool()


class QAccelerometerFilter(QSensorFilter):
    """"""
    def __init__(self):
        '''void QAccelerometerFilter.__init__()'''
    def __init__(self):
        '''QAccelerometerFilter QAccelerometerFilter.__init__()'''
        return QAccelerometerFilter()
    def filter(self, reading):
        '''abstract bool QAccelerometerFilter.filter(QAccelerometerReading reading)'''
        return bool()


class QSensor(QObject):
    """"""
    # Enum QSensor.AxesOrientationMode
    FixedOrientation = 0
    AutomaticOrientation = 0
    UserOrientation = 0

    # Enum QSensor.Feature
    Buffering = 0
    AlwaysOn = 0
    GeoValues = 0
    FieldOfView = 0
    AccelerationMode = 0
    SkipDuplicates = 0
    AxesOrientation = 0
    PressureSensorTemperature = 0

    def __init__(self, type, parent = None):
        '''void QSensor.__init__(QByteArray type, QObject parent = None)'''
    bufferSizeChanged = pyqtSignal() # void bufferSizeChanged(int) - signal
    efficientBufferSizeChanged = pyqtSignal() # void efficientBufferSizeChanged(int) - signal
    maxBufferSizeChanged = pyqtSignal() # void maxBufferSizeChanged(int) - signal
    userOrientationChanged = pyqtSignal() # void userOrientationChanged(int) - signal
    currentOrientationChanged = pyqtSignal() # void currentOrientationChanged(int) - signal
    axesOrientationModeChanged = pyqtSignal() # void axesOrientationModeChanged(QSensor::AxesOrientationMode) - signal
    skipDuplicatesChanged = pyqtSignal() # void skipDuplicatesChanged(bool) - signal
    dataRateChanged = pyqtSignal() # void dataRateChanged() - signal
    alwaysOnChanged = pyqtSignal() # void alwaysOnChanged() - signal
    availableSensorsChanged = pyqtSignal() # void availableSensorsChanged() - signal
    sensorError = pyqtSignal() # void sensorError(int) - signal
    readingChanged = pyqtSignal() # void readingChanged() - signal
    activeChanged = pyqtSignal() # void activeChanged() - signal
    busyChanged = pyqtSignal() # void busyChanged() - signal
    def stop(self):
        '''void QSensor.stop()'''
    def start(self):
        '''bool QSensor.start()'''
        return bool()
    def setBufferSize(self, bufferSize):
        '''void QSensor.setBufferSize(int bufferSize)'''
    def bufferSize(self):
        '''int QSensor.bufferSize()'''
        return int()
    def setEfficientBufferSize(self, efficientBufferSize):
        '''void QSensor.setEfficientBufferSize(int efficientBufferSize)'''
    def efficientBufferSize(self):
        '''int QSensor.efficientBufferSize()'''
        return int()
    def setMaxBufferSize(self, maxBufferSize):
        '''void QSensor.setMaxBufferSize(int maxBufferSize)'''
    def maxBufferSize(self):
        '''int QSensor.maxBufferSize()'''
        return int()
    def setUserOrientation(self, userOrientation):
        '''void QSensor.setUserOrientation(int userOrientation)'''
    def userOrientation(self):
        '''int QSensor.userOrientation()'''
        return int()
    def setCurrentOrientation(self, currentOrientation):
        '''void QSensor.setCurrentOrientation(int currentOrientation)'''
    def currentOrientation(self):
        '''int QSensor.currentOrientation()'''
        return int()
    def setAxesOrientationMode(self, axesOrientationMode):
        '''void QSensor.setAxesOrientationMode(QSensor.AxesOrientationMode axesOrientationMode)'''
    def axesOrientationMode(self):
        '''QSensor.AxesOrientationMode QSensor.axesOrientationMode()'''
        return QSensor.AxesOrientationMode()
    def isFeatureSupported(self, feature):
        '''bool QSensor.isFeatureSupported(QSensor.Feature feature)'''
        return bool()
    def defaultSensorForType(self, type):
        '''static QByteArray QSensor.defaultSensorForType(QByteArray type)'''
        return QByteArray()
    def sensorsForType(self, type):
        '''static list-of-QByteArray QSensor.sensorsForType(QByteArray type)'''
        return [QByteArray()]
    def sensorTypes(self):
        '''static list-of-QByteArray QSensor.sensorTypes()'''
        return [QByteArray()]
    def reading(self):
        '''QSensorReading QSensor.reading()'''
        return QSensorReading()
    def filters(self):
        '''list-of-QSensorFilter QSensor.filters()'''
        return [QSensorFilter()]
    def removeFilter(self, filter):
        '''void QSensor.removeFilter(QSensorFilter filter)'''
    def addFilter(self, filter):
        '''void QSensor.addFilter(QSensorFilter filter)'''
    def error(self):
        '''int QSensor.error()'''
        return int()
    def description(self):
        '''str QSensor.description()'''
        return str()
    def setOutputRange(self, index):
        '''void QSensor.setOutputRange(int index)'''
    def outputRange(self):
        '''int QSensor.outputRange()'''
        return int()
    def outputRanges(self):
        '''list-of-qoutputrange QSensor.outputRanges()'''
        return [qoutputrange()]
    def setDataRate(self, rate):
        '''void QSensor.setDataRate(int rate)'''
    def dataRate(self):
        '''int QSensor.dataRate()'''
        return int()
    def availableDataRates(self):
        '''list-of-tuple-of-int-int QSensor.availableDataRates()'''
        return [tuple-of-int-int()]
    def setSkipDuplicates(self, skipDuplicates):
        '''void QSensor.setSkipDuplicates(bool skipDuplicates)'''
    def skipDuplicates(self):
        '''bool QSensor.skipDuplicates()'''
        return bool()
    def setAlwaysOn(self, alwaysOn):
        '''void QSensor.setAlwaysOn(bool alwaysOn)'''
    def isAlwaysOn(self):
        '''bool QSensor.isAlwaysOn()'''
        return bool()
    def isActive(self):
        '''bool QSensor.isActive()'''
        return bool()
    def setActive(self, active):
        '''void QSensor.setActive(bool active)'''
    def isBusy(self):
        '''bool QSensor.isBusy()'''
        return bool()
    def isConnectedToBackend(self):
        '''bool QSensor.isConnectedToBackend()'''
        return bool()
    def connectToBackend(self):
        '''bool QSensor.connectToBackend()'''
        return bool()
    def type(self):
        '''QByteArray QSensor.type()'''
        return QByteArray()
    def setIdentifier(self, identifier):
        '''void QSensor.setIdentifier(QByteArray identifier)'''
    def identifier(self):
        '''QByteArray QSensor.identifier()'''
        return QByteArray()


class QAccelerometer(QSensor):
    """"""
    # Enum QAccelerometer.AccelerationMode
    Combined = 0
    Gravity = 0
    User = 0

    def __init__(self, parent = None):
        '''void QAccelerometer.__init__(QObject parent = None)'''
    accelerationModeChanged = pyqtSignal() # void accelerationModeChanged(QAccelerometer::AccelerationMode) - signal
    def reading(self):
        '''QAccelerometerReading QAccelerometer.reading()'''
        return QAccelerometerReading()
    def setAccelerationMode(self, accelerationMode):
        '''void QAccelerometer.setAccelerationMode(QAccelerometer.AccelerationMode accelerationMode)'''
    def accelerationMode(self):
        '''QAccelerometer.AccelerationMode QAccelerometer.accelerationMode()'''
        return QAccelerometer.AccelerationMode()


class QAltimeterReading(QSensorReading):
    """"""
    def setAltitude(self, altitude):
        '''void QAltimeterReading.setAltitude(float altitude)'''
    def altitude(self):
        '''float QAltimeterReading.altitude()'''
        return float()


class QAltimeterFilter(QSensorFilter):
    """"""
    def __init__(self):
        '''void QAltimeterFilter.__init__()'''
    def __init__(self):
        '''QAltimeterFilter QAltimeterFilter.__init__()'''
        return QAltimeterFilter()
    def filter(self, reading):
        '''abstract bool QAltimeterFilter.filter(QAltimeterReading reading)'''
        return bool()


class QAltimeter(QSensor):
    """"""
    def __init__(self, parent = None):
        '''void QAltimeter.__init__(QObject parent = None)'''
    def reading(self):
        '''QAltimeterReading QAltimeter.reading()'''
        return QAltimeterReading()


class QAmbientLightReading(QSensorReading):
    """"""
    # Enum QAmbientLightReading.LightLevel
    Undefined = 0
    Dark = 0
    Twilight = 0
    Light = 0
    Bright = 0
    Sunny = 0

    def setLightLevel(self, lightLevel):
        '''void QAmbientLightReading.setLightLevel(QAmbientLightReading.LightLevel lightLevel)'''
    def lightLevel(self):
        '''QAmbientLightReading.LightLevel QAmbientLightReading.lightLevel()'''
        return QAmbientLightReading.LightLevel()


class QAmbientLightFilter(QSensorFilter):
    """"""
    def __init__(self):
        '''void QAmbientLightFilter.__init__()'''
    def __init__(self):
        '''QAmbientLightFilter QAmbientLightFilter.__init__()'''
        return QAmbientLightFilter()
    def filter(self, reading):
        '''abstract bool QAmbientLightFilter.filter(QAmbientLightReading reading)'''
        return bool()


class QAmbientLightSensor(QSensor):
    """"""
    def __init__(self, parent = None):
        '''void QAmbientLightSensor.__init__(QObject parent = None)'''
    def reading(self):
        '''QAmbientLightReading QAmbientLightSensor.reading()'''
        return QAmbientLightReading()


class QAmbientTemperatureReading(QSensorReading):
    """"""
    def setTemperature(self, temperature):
        '''void QAmbientTemperatureReading.setTemperature(float temperature)'''
    def temperature(self):
        '''float QAmbientTemperatureReading.temperature()'''
        return float()


class QAmbientTemperatureFilter(QSensorFilter):
    """"""
    def __init__(self):
        '''void QAmbientTemperatureFilter.__init__()'''
    def __init__(self):
        '''QAmbientTemperatureFilter QAmbientTemperatureFilter.__init__()'''
        return QAmbientTemperatureFilter()
    def filter(self, reading):
        '''abstract bool QAmbientTemperatureFilter.filter(QAmbientTemperatureReading reading)'''
        return bool()


class QAmbientTemperatureSensor(QSensor):
    """"""
    def __init__(self, parent = None):
        '''void QAmbientTemperatureSensor.__init__(QObject parent = None)'''
    def reading(self):
        '''QAmbientTemperatureReading QAmbientTemperatureSensor.reading()'''
        return QAmbientTemperatureReading()


class QCompassReading(QSensorReading):
    """"""
    def setCalibrationLevel(self, calibrationLevel):
        '''void QCompassReading.setCalibrationLevel(float calibrationLevel)'''
    def calibrationLevel(self):
        '''float QCompassReading.calibrationLevel()'''
        return float()
    def setAzimuth(self, azimuth):
        '''void QCompassReading.setAzimuth(float azimuth)'''
    def azimuth(self):
        '''float QCompassReading.azimuth()'''
        return float()


class QCompassFilter(QSensorFilter):
    """"""
    def __init__(self):
        '''void QCompassFilter.__init__()'''
    def __init__(self):
        '''QCompassFilter QCompassFilter.__init__()'''
        return QCompassFilter()
    def filter(self, reading):
        '''abstract bool QCompassFilter.filter(QCompassReading reading)'''
        return bool()


class QCompass(QSensor):
    """"""
    def __init__(self, parent = None):
        '''void QCompass.__init__(QObject parent = None)'''
    def reading(self):
        '''QCompassReading QCompass.reading()'''
        return QCompassReading()


class QDistanceReading(QSensorReading):
    """"""
    def setDistance(self, distance):
        '''void QDistanceReading.setDistance(float distance)'''
    def distance(self):
        '''float QDistanceReading.distance()'''
        return float()


class QDistanceFilter(QSensorFilter):
    """"""
    def __init__(self):
        '''void QDistanceFilter.__init__()'''
    def __init__(self):
        '''QDistanceFilter QDistanceFilter.__init__()'''
        return QDistanceFilter()
    def filter(self, reading):
        '''abstract bool QDistanceFilter.filter(QDistanceReading reading)'''
        return bool()


class QDistanceSensor(QSensor):
    """"""
    def __init__(self, parent = None):
        '''void QDistanceSensor.__init__(QObject parent = None)'''
    def reading(self):
        '''QDistanceReading QDistanceSensor.reading()'''
        return QDistanceReading()


class QGyroscopeReading(QSensorReading):
    """"""
    def setZ(self, z):
        '''void QGyroscopeReading.setZ(float z)'''
    def z(self):
        '''float QGyroscopeReading.z()'''
        return float()
    def setY(self, y):
        '''void QGyroscopeReading.setY(float y)'''
    def y(self):
        '''float QGyroscopeReading.y()'''
        return float()
    def setX(self, x):
        '''void QGyroscopeReading.setX(float x)'''
    def x(self):
        '''float QGyroscopeReading.x()'''
        return float()


class QGyroscopeFilter(QSensorFilter):
    """"""
    def __init__(self):
        '''void QGyroscopeFilter.__init__()'''
    def __init__(self):
        '''QGyroscopeFilter QGyroscopeFilter.__init__()'''
        return QGyroscopeFilter()
    def filter(self, reading):
        '''abstract bool QGyroscopeFilter.filter(QGyroscopeReading reading)'''
        return bool()


class QGyroscope(QSensor):
    """"""
    def __init__(self, parent = None):
        '''void QGyroscope.__init__(QObject parent = None)'''
    def reading(self):
        '''QGyroscopeReading QGyroscope.reading()'''
        return QGyroscopeReading()


class QHolsterReading(QSensorReading):
    """"""
    def setHolstered(self, holstered):
        '''void QHolsterReading.setHolstered(bool holstered)'''
    def holstered(self):
        '''bool QHolsterReading.holstered()'''
        return bool()


class QHolsterFilter(QSensorFilter):
    """"""
    def __init__(self):
        '''void QHolsterFilter.__init__()'''
    def __init__(self):
        '''QHolsterFilter QHolsterFilter.__init__()'''
        return QHolsterFilter()
    def filter(self, reading):
        '''abstract bool QHolsterFilter.filter(QHolsterReading reading)'''
        return bool()


class QHolsterSensor(QSensor):
    """"""
    def __init__(self, parent = None):
        '''void QHolsterSensor.__init__(QObject parent = None)'''
    def reading(self):
        '''QHolsterReading QHolsterSensor.reading()'''
        return QHolsterReading()


class QIRProximityReading(QSensorReading):
    """"""
    def setReflectance(self, reflectance):
        '''void QIRProximityReading.setReflectance(float reflectance)'''
    def reflectance(self):
        '''float QIRProximityReading.reflectance()'''
        return float()


class QIRProximityFilter(QSensorFilter):
    """"""
    def __init__(self):
        '''void QIRProximityFilter.__init__()'''
    def __init__(self):
        '''QIRProximityFilter QIRProximityFilter.__init__()'''
        return QIRProximityFilter()
    def filter(self, reading):
        '''abstract bool QIRProximityFilter.filter(QIRProximityReading reading)'''
        return bool()


class QIRProximitySensor(QSensor):
    """"""
    def __init__(self, parent = None):
        '''void QIRProximitySensor.__init__(QObject parent = None)'''
    def reading(self):
        '''QIRProximityReading QIRProximitySensor.reading()'''
        return QIRProximityReading()


class QLightReading(QSensorReading):
    """"""
    def setLux(self, lux):
        '''void QLightReading.setLux(float lux)'''
    def lux(self):
        '''float QLightReading.lux()'''
        return float()


class QLightFilter(QSensorFilter):
    """"""
    def __init__(self):
        '''void QLightFilter.__init__()'''
    def __init__(self):
        '''QLightFilter QLightFilter.__init__()'''
        return QLightFilter()
    def filter(self, reading):
        '''abstract bool QLightFilter.filter(QLightReading reading)'''
        return bool()


class QLightSensor(QSensor):
    """"""
    def __init__(self, parent = None):
        '''void QLightSensor.__init__(QObject parent = None)'''
    fieldOfViewChanged = pyqtSignal() # void fieldOfViewChanged(qreal) - signal
    def setFieldOfView(self, fieldOfView):
        '''void QLightSensor.setFieldOfView(float fieldOfView)'''
    def fieldOfView(self):
        '''float QLightSensor.fieldOfView()'''
        return float()
    def reading(self):
        '''QLightReading QLightSensor.reading()'''
        return QLightReading()


class QMagnetometerReading(QSensorReading):
    """"""
    def setCalibrationLevel(self, calibrationLevel):
        '''void QMagnetometerReading.setCalibrationLevel(float calibrationLevel)'''
    def calibrationLevel(self):
        '''float QMagnetometerReading.calibrationLevel()'''
        return float()
    def setZ(self, z):
        '''void QMagnetometerReading.setZ(float z)'''
    def z(self):
        '''float QMagnetometerReading.z()'''
        return float()
    def setY(self, y):
        '''void QMagnetometerReading.setY(float y)'''
    def y(self):
        '''float QMagnetometerReading.y()'''
        return float()
    def setX(self, x):
        '''void QMagnetometerReading.setX(float x)'''
    def x(self):
        '''float QMagnetometerReading.x()'''
        return float()


class QMagnetometerFilter(QSensorFilter):
    """"""
    def __init__(self):
        '''void QMagnetometerFilter.__init__()'''
    def __init__(self):
        '''QMagnetometerFilter QMagnetometerFilter.__init__()'''
        return QMagnetometerFilter()
    def filter(self, reading):
        '''abstract bool QMagnetometerFilter.filter(QMagnetometerReading reading)'''
        return bool()


class QMagnetometer(QSensor):
    """"""
    def __init__(self, parent = None):
        '''void QMagnetometer.__init__(QObject parent = None)'''
    returnGeoValuesChanged = pyqtSignal() # void returnGeoValuesChanged(bool) - signal
    def setReturnGeoValues(self, returnGeoValues):
        '''void QMagnetometer.setReturnGeoValues(bool returnGeoValues)'''
    def returnGeoValues(self):
        '''bool QMagnetometer.returnGeoValues()'''
        return bool()
    def reading(self):
        '''QMagnetometerReading QMagnetometer.reading()'''
        return QMagnetometerReading()


class QOrientationReading(QSensorReading):
    """"""
    # Enum QOrientationReading.Orientation
    Undefined = 0
    TopUp = 0
    TopDown = 0
    LeftUp = 0
    RightUp = 0
    FaceUp = 0
    FaceDown = 0

    def setOrientation(self, orientation):
        '''void QOrientationReading.setOrientation(QOrientationReading.Orientation orientation)'''
    def orientation(self):
        '''QOrientationReading.Orientation QOrientationReading.orientation()'''
        return QOrientationReading.Orientation()


class QOrientationFilter(QSensorFilter):
    """"""
    def __init__(self):
        '''void QOrientationFilter.__init__()'''
    def __init__(self):
        '''QOrientationFilter QOrientationFilter.__init__()'''
        return QOrientationFilter()
    def filter(self, reading):
        '''abstract bool QOrientationFilter.filter(QOrientationReading reading)'''
        return bool()


class QOrientationSensor(QSensor):
    """"""
    def __init__(self, parent = None):
        '''void QOrientationSensor.__init__(QObject parent = None)'''
    def reading(self):
        '''QOrientationReading QOrientationSensor.reading()'''
        return QOrientationReading()


class QPressureReading(QSensorReading):
    """"""
    def setTemperature(self, temperature):
        '''void QPressureReading.setTemperature(float temperature)'''
    def temperature(self):
        '''float QPressureReading.temperature()'''
        return float()
    def setPressure(self, pressure):
        '''void QPressureReading.setPressure(float pressure)'''
    def pressure(self):
        '''float QPressureReading.pressure()'''
        return float()


class QPressureFilter(QSensorFilter):
    """"""
    def __init__(self):
        '''void QPressureFilter.__init__()'''
    def __init__(self):
        '''QPressureFilter QPressureFilter.__init__()'''
        return QPressureFilter()
    def filter(self, reading):
        '''abstract bool QPressureFilter.filter(QPressureReading reading)'''
        return bool()


class QPressureSensor(QSensor):
    """"""
    def __init__(self, parent = None):
        '''void QPressureSensor.__init__(QObject parent = None)'''
    def reading(self):
        '''QPressureReading QPressureSensor.reading()'''
        return QPressureReading()


class QProximityReading(QSensorReading):
    """"""
    def setClose(self, close):
        '''void QProximityReading.setClose(bool close)'''
    def close(self):
        '''bool QProximityReading.close()'''
        return bool()


class QProximityFilter(QSensorFilter):
    """"""
    def __init__(self):
        '''void QProximityFilter.__init__()'''
    def __init__(self):
        '''QProximityFilter QProximityFilter.__init__()'''
        return QProximityFilter()
    def filter(self, reading):
        '''abstract bool QProximityFilter.filter(QProximityReading reading)'''
        return bool()


class QProximitySensor(QSensor):
    """"""
    def __init__(self, parent = None):
        '''void QProximitySensor.__init__(QObject parent = None)'''
    def reading(self):
        '''QProximityReading QProximitySensor.reading()'''
        return QProximityReading()


class qoutputrange():
    """"""
    accuracy = None # float - member
    maximum = None # float - member
    minimum = None # float - member
    def __init__(self):
        '''void qoutputrange.__init__()'''
    def __init__(self):
        '''qoutputrange qoutputrange.__init__()'''
        return qoutputrange()


class QTapReading(QSensorReading):
    """"""
    # Enum QTapReading.TapDirection
    Undefined = 0
    X = 0
    Y = 0
    Z = 0
    X_Pos = 0
    Y_Pos = 0
    Z_Pos = 0
    X_Neg = 0
    Y_Neg = 0
    Z_Neg = 0
    X_Both = 0
    Y_Both = 0
    Z_Both = 0

    def setDoubleTap(self, doubleTap):
        '''void QTapReading.setDoubleTap(bool doubleTap)'''
    def isDoubleTap(self):
        '''bool QTapReading.isDoubleTap()'''
        return bool()
    def setTapDirection(self, tapDirection):
        '''void QTapReading.setTapDirection(QTapReading.TapDirection tapDirection)'''
    def tapDirection(self):
        '''QTapReading.TapDirection QTapReading.tapDirection()'''
        return QTapReading.TapDirection()


class QTapFilter(QSensorFilter):
    """"""
    def __init__(self):
        '''void QTapFilter.__init__()'''
    def __init__(self):
        '''QTapFilter QTapFilter.__init__()'''
        return QTapFilter()
    def filter(self, reading):
        '''abstract bool QTapFilter.filter(QTapReading reading)'''
        return bool()


class QTapSensor(QSensor):
    """"""
    def __init__(self, parent = None):
        '''void QTapSensor.__init__(QObject parent = None)'''
    returnDoubleTapEventsChanged = pyqtSignal() # void returnDoubleTapEventsChanged(bool) - signal
    def setReturnDoubleTapEvents(self, returnDoubleTapEvents):
        '''void QTapSensor.setReturnDoubleTapEvents(bool returnDoubleTapEvents)'''
    def returnDoubleTapEvents(self):
        '''bool QTapSensor.returnDoubleTapEvents()'''
        return bool()
    def reading(self):
        '''QTapReading QTapSensor.reading()'''
        return QTapReading()


class QTiltReading(QSensorReading):
    """"""
    def setXRotation(self, x):
        '''void QTiltReading.setXRotation(float x)'''
    def xRotation(self):
        '''float QTiltReading.xRotation()'''
        return float()
    def setYRotation(self, y):
        '''void QTiltReading.setYRotation(float y)'''
    def yRotation(self):
        '''float QTiltReading.yRotation()'''
        return float()


class QTiltFilter(QSensorFilter):
    """"""
    def __init__(self):
        '''void QTiltFilter.__init__()'''
    def __init__(self):
        '''QTiltFilter QTiltFilter.__init__()'''
        return QTiltFilter()
    def filter(self, reading):
        '''abstract bool QTiltFilter.filter(QTiltReading reading)'''
        return bool()


class QTiltSensor(QSensor):
    """"""
    def __init__(self, parent = None):
        '''void QTiltSensor.__init__(QObject parent = None)'''
    def calibrate(self):
        '''void QTiltSensor.calibrate()'''
    def reading(self):
        '''QTiltReading QTiltSensor.reading()'''
        return QTiltReading()


class QRotationReading(QSensorReading):
    """"""
    def setFromEuler(self, x, y, z):
        '''void QRotationReading.setFromEuler(float x, float y, float z)'''
    def z(self):
        '''float QRotationReading.z()'''
        return float()
    def y(self):
        '''float QRotationReading.y()'''
        return float()
    def x(self):
        '''float QRotationReading.x()'''
        return float()


class QRotationFilter(QSensorFilter):
    """"""
    def __init__(self):
        '''void QRotationFilter.__init__()'''
    def __init__(self):
        '''QRotationFilter QRotationFilter.__init__()'''
        return QRotationFilter()
    def filter(self, reading):
        '''abstract bool QRotationFilter.filter(QRotationReading reading)'''
        return bool()


class QRotationSensor(QSensor):
    """"""
    def __init__(self, parent = None):
        '''void QRotationSensor.__init__(QObject parent = None)'''
    hasZChanged = pyqtSignal() # void hasZChanged(bool) - signal
    def setHasZ(self, hasZ):
        '''void QRotationSensor.setHasZ(bool hasZ)'''
    def hasZ(self):
        '''bool QRotationSensor.hasZ()'''
        return bool()
    def reading(self):
        '''QRotationReading QRotationSensor.reading()'''
        return QRotationReading()


