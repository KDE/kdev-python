class pyqtSignal():
 def connect(self, targetSignal): pass
 def emit(self, *args): pass
from QtCore import *

from QtWidgets import *

import datetime

class QGeoAddress():
    """"""
    def __init__(self):
        '''void QGeoAddress.__init__()'''
    def __init__(self, other):
        '''void QGeoAddress.__init__(QGeoAddress other)'''
    def isTextGenerated(self):
        '''bool QGeoAddress.isTextGenerated()'''
        return bool()
    def clear(self):
        '''void QGeoAddress.clear()'''
    def isEmpty(self):
        '''bool QGeoAddress.isEmpty()'''
        return bool()
    def setStreet(self, street):
        '''void QGeoAddress.setStreet(str street)'''
    def street(self):
        '''str QGeoAddress.street()'''
        return str()
    def setPostalCode(self, postalCode):
        '''void QGeoAddress.setPostalCode(str postalCode)'''
    def postalCode(self):
        '''str QGeoAddress.postalCode()'''
        return str()
    def setDistrict(self, district):
        '''void QGeoAddress.setDistrict(str district)'''
    def district(self):
        '''str QGeoAddress.district()'''
        return str()
    def setCity(self, city):
        '''void QGeoAddress.setCity(str city)'''
    def city(self):
        '''str QGeoAddress.city()'''
        return str()
    def setCounty(self, county):
        '''void QGeoAddress.setCounty(str county)'''
    def county(self):
        '''str QGeoAddress.county()'''
        return str()
    def setState(self, state):
        '''void QGeoAddress.setState(str state)'''
    def state(self):
        '''str QGeoAddress.state()'''
        return str()
    def setCountryCode(self, countryCode):
        '''void QGeoAddress.setCountryCode(str countryCode)'''
    def countryCode(self):
        '''str QGeoAddress.countryCode()'''
        return str()
    def setCountry(self, country):
        '''void QGeoAddress.setCountry(str country)'''
    def country(self):
        '''str QGeoAddress.country()'''
        return str()
    def setText(self, text):
        '''void QGeoAddress.setText(str text)'''
    def text(self):
        '''str QGeoAddress.text()'''
        return str()
    def __ne__(self, other):
        '''bool QGeoAddress.__ne__(QGeoAddress other)'''
        return bool()
    def __eq__(self, other):
        '''bool QGeoAddress.__eq__(QGeoAddress other)'''
        return bool()


class QGeoAreaMonitorInfo():
    """"""
    def __init__(self, name = None):
        '''void QGeoAreaMonitorInfo.__init__(str name = '')'''
    def __init__(self, other):
        '''void QGeoAreaMonitorInfo.__init__(QGeoAreaMonitorInfo other)'''
    def setNotificationParameters(self, parameters):
        '''void QGeoAreaMonitorInfo.setNotificationParameters(dict-of-str-object parameters)'''
    def notificationParameters(self):
        '''dict-of-str-object QGeoAreaMonitorInfo.notificationParameters()'''
        return {str():object()}
    def setPersistent(self, isPersistent):
        '''void QGeoAreaMonitorInfo.setPersistent(bool isPersistent)'''
    def isPersistent(self):
        '''bool QGeoAreaMonitorInfo.isPersistent()'''
        return bool()
    def setExpiration(self, expiry):
        '''void QGeoAreaMonitorInfo.setExpiration(QDateTime expiry)'''
    def expiration(self):
        '''QDateTime QGeoAreaMonitorInfo.expiration()'''
        return QDateTime()
    def setArea(self, newShape):
        '''void QGeoAreaMonitorInfo.setArea(QGeoShape newShape)'''
    def area(self):
        '''QGeoShape QGeoAreaMonitorInfo.area()'''
        return QGeoShape()
    def isValid(self):
        '''bool QGeoAreaMonitorInfo.isValid()'''
        return bool()
    def identifier(self):
        '''str QGeoAreaMonitorInfo.identifier()'''
        return str()
    def setName(self, name):
        '''void QGeoAreaMonitorInfo.setName(str name)'''
    def name(self):
        '''str QGeoAreaMonitorInfo.name()'''
        return str()
    def __ne__(self, other):
        '''bool QGeoAreaMonitorInfo.__ne__(QGeoAreaMonitorInfo other)'''
        return bool()
    def __eq__(self, other):
        '''bool QGeoAreaMonitorInfo.__eq__(QGeoAreaMonitorInfo other)'''
        return bool()


class QGeoAreaMonitorSource(QObject):
    """"""
    # Enum QGeoAreaMonitorSource.AreaMonitorFeature
    PersistentAreaMonitorFeature = 0
    AnyAreaMonitorFeature = 0

    # Enum QGeoAreaMonitorSource.Error
    AccessError = 0
    InsufficientPositionInfo = 0
    UnknownSourceError = 0
    NoError = 0

    def __init__(self, parent):
        '''void QGeoAreaMonitorSource.__init__(QObject parent)'''
    monitorExpired = pyqtSignal() # void monitorExpired(const QGeoAreaMonitorInfoamp;) - signal
    areaExited = pyqtSignal() # void areaExited(const QGeoAreaMonitorInfoamp;,const QGeoPositionInfoamp;) - signal
    areaEntered = pyqtSignal() # void areaEntered(const QGeoAreaMonitorInfoamp;,const QGeoPositionInfoamp;) - signal
    def activeMonitors(self):
        '''abstract list-of-QGeoAreaMonitorInfo QGeoAreaMonitorSource.activeMonitors()'''
        return [QGeoAreaMonitorInfo()]
    def activeMonitors(self, lookupArea):
        '''abstract list-of-QGeoAreaMonitorInfo QGeoAreaMonitorSource.activeMonitors(QGeoShape lookupArea)'''
        return [QGeoAreaMonitorInfo()]
    def requestUpdate(self, monitor, signal):
        '''abstract bool QGeoAreaMonitorSource.requestUpdate(QGeoAreaMonitorInfo monitor, str signal)'''
        return bool()
    def stopMonitoring(self, monitor):
        '''abstract bool QGeoAreaMonitorSource.stopMonitoring(QGeoAreaMonitorInfo monitor)'''
        return bool()
    def startMonitoring(self, monitor):
        '''abstract bool QGeoAreaMonitorSource.startMonitoring(QGeoAreaMonitorInfo monitor)'''
        return bool()
    def supportedAreaMonitorFeatures(self):
        '''abstract QGeoAreaMonitorSource.AreaMonitorFeatures QGeoAreaMonitorSource.supportedAreaMonitorFeatures()'''
        return QGeoAreaMonitorSource.AreaMonitorFeatures()
    def error(self):
        '''abstract QGeoAreaMonitorSource.Error QGeoAreaMonitorSource.error()'''
        return QGeoAreaMonitorSource.Error()
    error = pyqtSignal() # void error(QGeoAreaMonitorSource::Error) - signal
    def sourceName(self):
        '''str QGeoAreaMonitorSource.sourceName()'''
        return str()
    def positionInfoSource(self):
        '''QGeoPositionInfoSource QGeoAreaMonitorSource.positionInfoSource()'''
        return QGeoPositionInfoSource()
    def setPositionInfoSource(self, source):
        '''void QGeoAreaMonitorSource.setPositionInfoSource(QGeoPositionInfoSource source)'''
    def availableSources(self):
        '''static list-of-str QGeoAreaMonitorSource.availableSources()'''
        return [str()]
    def createSource(self, sourceName, parent):
        '''static QGeoAreaMonitorSource QGeoAreaMonitorSource.createSource(str sourceName, QObject parent)'''
        return QGeoAreaMonitorSource()
    def createDefaultSource(self, parent):
        '''static QGeoAreaMonitorSource QGeoAreaMonitorSource.createDefaultSource(QObject parent)'''
        return QGeoAreaMonitorSource()
    class AreaMonitorFeatures():
        """"""
        def __init__(self):
            '''QGeoAreaMonitorSource.AreaMonitorFeatures QGeoAreaMonitorSource.AreaMonitorFeatures.__init__()'''
            return QGeoAreaMonitorSource.AreaMonitorFeatures()
        def __init__(self):
            '''int QGeoAreaMonitorSource.AreaMonitorFeatures.__init__()'''
            return int()
        def __init__(self):
            '''void QGeoAreaMonitorSource.AreaMonitorFeatures.__init__()'''
        def __bool__(self):
            '''int QGeoAreaMonitorSource.AreaMonitorFeatures.__bool__()'''
            return int()
        def __ne__(self, f):
            '''bool QGeoAreaMonitorSource.AreaMonitorFeatures.__ne__(QGeoAreaMonitorSource.AreaMonitorFeatures f)'''
            return bool()
        def __eq__(self, f):
            '''bool QGeoAreaMonitorSource.AreaMonitorFeatures.__eq__(QGeoAreaMonitorSource.AreaMonitorFeatures f)'''
            return bool()
        def __invert__(self):
            '''QGeoAreaMonitorSource.AreaMonitorFeatures QGeoAreaMonitorSource.AreaMonitorFeatures.__invert__()'''
            return QGeoAreaMonitorSource.AreaMonitorFeatures()
        def __and__(self, mask):
            '''QGeoAreaMonitorSource.AreaMonitorFeatures QGeoAreaMonitorSource.AreaMonitorFeatures.__and__(int mask)'''
            return QGeoAreaMonitorSource.AreaMonitorFeatures()
        def __xor__(self, f):
            '''QGeoAreaMonitorSource.AreaMonitorFeatures QGeoAreaMonitorSource.AreaMonitorFeatures.__xor__(QGeoAreaMonitorSource.AreaMonitorFeatures f)'''
            return QGeoAreaMonitorSource.AreaMonitorFeatures()
        def __xor__(self, f):
            '''QGeoAreaMonitorSource.AreaMonitorFeatures QGeoAreaMonitorSource.AreaMonitorFeatures.__xor__(int f)'''
            return QGeoAreaMonitorSource.AreaMonitorFeatures()
        def __or__(self, f):
            '''QGeoAreaMonitorSource.AreaMonitorFeatures QGeoAreaMonitorSource.AreaMonitorFeatures.__or__(QGeoAreaMonitorSource.AreaMonitorFeatures f)'''
            return QGeoAreaMonitorSource.AreaMonitorFeatures()
        def __or__(self, f):
            '''QGeoAreaMonitorSource.AreaMonitorFeatures QGeoAreaMonitorSource.AreaMonitorFeatures.__or__(int f)'''
            return QGeoAreaMonitorSource.AreaMonitorFeatures()
        def __int__(self):
            '''int QGeoAreaMonitorSource.AreaMonitorFeatures.__int__()'''
            return int()
        def __ixor__(self, f):
            '''QGeoAreaMonitorSource.AreaMonitorFeatures QGeoAreaMonitorSource.AreaMonitorFeatures.__ixor__(QGeoAreaMonitorSource.AreaMonitorFeatures f)'''
            return QGeoAreaMonitorSource.AreaMonitorFeatures()
        def __ior__(self, f):
            '''QGeoAreaMonitorSource.AreaMonitorFeatures QGeoAreaMonitorSource.AreaMonitorFeatures.__ior__(QGeoAreaMonitorSource.AreaMonitorFeatures f)'''
            return QGeoAreaMonitorSource.AreaMonitorFeatures()
        def __iand__(self, mask):
            '''QGeoAreaMonitorSource.AreaMonitorFeatures QGeoAreaMonitorSource.AreaMonitorFeatures.__iand__(int mask)'''
            return QGeoAreaMonitorSource.AreaMonitorFeatures()


class QGeoShape():
    """"""
    # Enum QGeoShape.ShapeType
    UnknownType = 0
    RectangleType = 0
    CircleType = 0

    def __init__(self):
        '''void QGeoShape.__init__()'''
    def __init__(self, other):
        '''void QGeoShape.__init__(QGeoShape other)'''
    def toString(self):
        '''str QGeoShape.toString()'''
        return str()
    def center(self):
        '''QGeoCoordinate QGeoShape.center()'''
        return QGeoCoordinate()
    def extendShape(self, coordinate):
        '''void QGeoShape.extendShape(QGeoCoordinate coordinate)'''
    def __ne__(self, other):
        '''bool QGeoShape.__ne__(QGeoShape other)'''
        return bool()
    def __eq__(self, other):
        '''bool QGeoShape.__eq__(QGeoShape other)'''
        return bool()
    def contains(self, coordinate):
        '''bool QGeoShape.contains(QGeoCoordinate coordinate)'''
        return bool()
    def isEmpty(self):
        '''bool QGeoShape.isEmpty()'''
        return bool()
    def isValid(self):
        '''bool QGeoShape.isValid()'''
        return bool()
    def type(self):
        '''QGeoShape.ShapeType QGeoShape.type()'''
        return QGeoShape.ShapeType()


class QGeoCircle(QGeoShape):
    """"""
    def __init__(self):
        '''void QGeoCircle.__init__()'''
    def __init__(self, center, radius = None):
        '''void QGeoCircle.__init__(QGeoCoordinate center, float radius = -1)'''
    def __init__(self, other):
        '''void QGeoCircle.__init__(QGeoCircle other)'''
    def __init__(self, other):
        '''void QGeoCircle.__init__(QGeoShape other)'''
    def toString(self):
        '''str QGeoCircle.toString()'''
        return str()
    def translated(self, degreesLatitude, degreesLongitude):
        '''QGeoCircle QGeoCircle.translated(float degreesLatitude, float degreesLongitude)'''
        return QGeoCircle()
    def translate(self, degreesLatitude, degreesLongitude):
        '''void QGeoCircle.translate(float degreesLatitude, float degreesLongitude)'''
    def radius(self):
        '''float QGeoCircle.radius()'''
        return float()
    def setRadius(self, radius):
        '''void QGeoCircle.setRadius(float radius)'''
    def center(self):
        '''QGeoCoordinate QGeoCircle.center()'''
        return QGeoCoordinate()
    def setCenter(self, center):
        '''void QGeoCircle.setCenter(QGeoCoordinate center)'''
    def __ne__(self, other):
        '''bool QGeoCircle.__ne__(QGeoCircle other)'''
        return bool()
    def __eq__(self, other):
        '''bool QGeoCircle.__eq__(QGeoCircle other)'''
        return bool()


class QGeoCoordinate():
    """"""
    # Enum QGeoCoordinate.CoordinateFormat
    Degrees = 0
    DegreesWithHemisphere = 0
    DegreesMinutes = 0
    DegreesMinutesWithHemisphere = 0
    DegreesMinutesSeconds = 0
    DegreesMinutesSecondsWithHemisphere = 0

    # Enum QGeoCoordinate.CoordinateType
    InvalidCoordinate = 0
    Coordinate2D = 0
    Coordinate3D = 0

    def __init__(self):
        '''void QGeoCoordinate.__init__()'''
    def __init__(self, latitude, longitude):
        '''void QGeoCoordinate.__init__(float latitude, float longitude)'''
    def __init__(self, latitude, longitude, altitude):
        '''void QGeoCoordinate.__init__(float latitude, float longitude, float altitude)'''
    def __init__(self, other):
        '''void QGeoCoordinate.__init__(QGeoCoordinate other)'''
    def toString(self, format = None):
        '''str QGeoCoordinate.toString(QGeoCoordinate.CoordinateFormat format = QGeoCoordinate.DegreesMinutesSecondsWithHemisphere)'''
        return str()
    def atDistanceAndAzimuth(self, distance, azimuth, distanceUp = 0):
        '''QGeoCoordinate QGeoCoordinate.atDistanceAndAzimuth(float distance, float azimuth, float distanceUp = 0)'''
        return QGeoCoordinate()
    def azimuthTo(self, other):
        '''float QGeoCoordinate.azimuthTo(QGeoCoordinate other)'''
        return float()
    def distanceTo(self, other):
        '''float QGeoCoordinate.distanceTo(QGeoCoordinate other)'''
        return float()
    def altitude(self):
        '''float QGeoCoordinate.altitude()'''
        return float()
    def setAltitude(self, altitude):
        '''void QGeoCoordinate.setAltitude(float altitude)'''
    def longitude(self):
        '''float QGeoCoordinate.longitude()'''
        return float()
    def setLongitude(self, longitude):
        '''void QGeoCoordinate.setLongitude(float longitude)'''
    def latitude(self):
        '''float QGeoCoordinate.latitude()'''
        return float()
    def setLatitude(self, latitude):
        '''void QGeoCoordinate.setLatitude(float latitude)'''
    def type(self):
        '''QGeoCoordinate.CoordinateType QGeoCoordinate.type()'''
        return QGeoCoordinate.CoordinateType()
    def isValid(self):
        '''bool QGeoCoordinate.isValid()'''
        return bool()
    def __ne__(self, other):
        '''bool QGeoCoordinate.__ne__(QGeoCoordinate other)'''
        return bool()
    def __eq__(self, other):
        '''bool QGeoCoordinate.__eq__(QGeoCoordinate other)'''
        return bool()


class QGeoLocation():
    """"""
    def __init__(self):
        '''void QGeoLocation.__init__()'''
    def __init__(self, other):
        '''void QGeoLocation.__init__(QGeoLocation other)'''
    def isEmpty(self):
        '''bool QGeoLocation.isEmpty()'''
        return bool()
    def setBoundingBox(self, box):
        '''void QGeoLocation.setBoundingBox(QGeoRectangle box)'''
    def boundingBox(self):
        '''QGeoRectangle QGeoLocation.boundingBox()'''
        return QGeoRectangle()
    def setCoordinate(self, position):
        '''void QGeoLocation.setCoordinate(QGeoCoordinate position)'''
    def coordinate(self):
        '''QGeoCoordinate QGeoLocation.coordinate()'''
        return QGeoCoordinate()
    def setAddress(self, address):
        '''void QGeoLocation.setAddress(QGeoAddress address)'''
    def address(self):
        '''QGeoAddress QGeoLocation.address()'''
        return QGeoAddress()
    def __ne__(self, other):
        '''bool QGeoLocation.__ne__(QGeoLocation other)'''
        return bool()
    def __eq__(self, other):
        '''bool QGeoLocation.__eq__(QGeoLocation other)'''
        return bool()


class QGeoPositionInfo():
    """"""
    # Enum QGeoPositionInfo.Attribute
    Direction = 0
    GroundSpeed = 0
    VerticalSpeed = 0
    MagneticVariation = 0
    HorizontalAccuracy = 0
    VerticalAccuracy = 0

    def __init__(self):
        '''void QGeoPositionInfo.__init__()'''
    def __init__(self, coordinate, updateTime):
        '''void QGeoPositionInfo.__init__(QGeoCoordinate coordinate, QDateTime updateTime)'''
    def __init__(self, other):
        '''void QGeoPositionInfo.__init__(QGeoPositionInfo other)'''
    def hasAttribute(self, attribute):
        '''bool QGeoPositionInfo.hasAttribute(QGeoPositionInfo.Attribute attribute)'''
        return bool()
    def removeAttribute(self, attribute):
        '''void QGeoPositionInfo.removeAttribute(QGeoPositionInfo.Attribute attribute)'''
    def attribute(self, attribute):
        '''float QGeoPositionInfo.attribute(QGeoPositionInfo.Attribute attribute)'''
        return float()
    def setAttribute(self, attribute, value):
        '''void QGeoPositionInfo.setAttribute(QGeoPositionInfo.Attribute attribute, float value)'''
    def coordinate(self):
        '''QGeoCoordinate QGeoPositionInfo.coordinate()'''
        return QGeoCoordinate()
    def setCoordinate(self, coordinate):
        '''void QGeoPositionInfo.setCoordinate(QGeoCoordinate coordinate)'''
    def timestamp(self):
        '''QDateTime QGeoPositionInfo.timestamp()'''
        return QDateTime()
    def setTimestamp(self, timestamp):
        '''void QGeoPositionInfo.setTimestamp(QDateTime timestamp)'''
    def isValid(self):
        '''bool QGeoPositionInfo.isValid()'''
        return bool()
    def __ne__(self, other):
        '''bool QGeoPositionInfo.__ne__(QGeoPositionInfo other)'''
        return bool()
    def __eq__(self, other):
        '''bool QGeoPositionInfo.__eq__(QGeoPositionInfo other)'''
        return bool()


class QGeoPositionInfoSource(QObject):
    """"""
    # Enum QGeoPositionInfoSource.PositioningMethod
    NoPositioningMethods = 0
    SatellitePositioningMethods = 0
    NonSatellitePositioningMethods = 0
    AllPositioningMethods = 0

    # Enum QGeoPositionInfoSource.Error
    AccessError = 0
    ClosedError = 0
    UnknownSourceError = 0
    NoError = 0

    def __init__(self, parent):
        '''void QGeoPositionInfoSource.__init__(QObject parent)'''
    updateTimeout = pyqtSignal() # void updateTimeout() - signal
    positionUpdated = pyqtSignal() # void positionUpdated(const QGeoPositionInfoamp;) - signal
    def requestUpdate(self, timeout = 0):
        '''abstract void QGeoPositionInfoSource.requestUpdate(int timeout = 0)'''
    def stopUpdates(self):
        '''abstract void QGeoPositionInfoSource.stopUpdates()'''
    def startUpdates(self):
        '''abstract void QGeoPositionInfoSource.startUpdates()'''
    def error(self):
        '''abstract QGeoPositionInfoSource.Error QGeoPositionInfoSource.error()'''
        return QGeoPositionInfoSource.Error()
    error = pyqtSignal() # void error(QGeoPositionInfoSource::Error) - signal
    def availableSources(self):
        '''static list-of-str QGeoPositionInfoSource.availableSources()'''
        return [str()]
    def createSource(self, sourceName, parent):
        '''static QGeoPositionInfoSource QGeoPositionInfoSource.createSource(str sourceName, QObject parent)'''
        return QGeoPositionInfoSource()
    def createDefaultSource(self, parent):
        '''static QGeoPositionInfoSource QGeoPositionInfoSource.createDefaultSource(QObject parent)'''
        return QGeoPositionInfoSource()
    def sourceName(self):
        '''str QGeoPositionInfoSource.sourceName()'''
        return str()
    def minimumUpdateInterval(self):
        '''abstract int QGeoPositionInfoSource.minimumUpdateInterval()'''
        return int()
    def supportedPositioningMethods(self):
        '''abstract QGeoPositionInfoSource.PositioningMethods QGeoPositionInfoSource.supportedPositioningMethods()'''
        return QGeoPositionInfoSource.PositioningMethods()
    def lastKnownPosition(self, fromSatellitePositioningMethodsOnly = False):
        '''abstract QGeoPositionInfo QGeoPositionInfoSource.lastKnownPosition(bool fromSatellitePositioningMethodsOnly = False)'''
        return QGeoPositionInfo()
    def preferredPositioningMethods(self):
        '''QGeoPositionInfoSource.PositioningMethods QGeoPositionInfoSource.preferredPositioningMethods()'''
        return QGeoPositionInfoSource.PositioningMethods()
    def setPreferredPositioningMethods(self, methods):
        '''void QGeoPositionInfoSource.setPreferredPositioningMethods(QGeoPositionInfoSource.PositioningMethods methods)'''
    def updateInterval(self):
        '''int QGeoPositionInfoSource.updateInterval()'''
        return int()
    def setUpdateInterval(self, msec):
        '''void QGeoPositionInfoSource.setUpdateInterval(int msec)'''
    class PositioningMethods():
        """"""
        def __init__(self):
            '''QGeoPositionInfoSource.PositioningMethods QGeoPositionInfoSource.PositioningMethods.__init__()'''
            return QGeoPositionInfoSource.PositioningMethods()
        def __init__(self):
            '''int QGeoPositionInfoSource.PositioningMethods.__init__()'''
            return int()
        def __init__(self):
            '''void QGeoPositionInfoSource.PositioningMethods.__init__()'''
        def __bool__(self):
            '''int QGeoPositionInfoSource.PositioningMethods.__bool__()'''
            return int()
        def __ne__(self, f):
            '''bool QGeoPositionInfoSource.PositioningMethods.__ne__(QGeoPositionInfoSource.PositioningMethods f)'''
            return bool()
        def __eq__(self, f):
            '''bool QGeoPositionInfoSource.PositioningMethods.__eq__(QGeoPositionInfoSource.PositioningMethods f)'''
            return bool()
        def __invert__(self):
            '''QGeoPositionInfoSource.PositioningMethods QGeoPositionInfoSource.PositioningMethods.__invert__()'''
            return QGeoPositionInfoSource.PositioningMethods()
        def __and__(self, mask):
            '''QGeoPositionInfoSource.PositioningMethods QGeoPositionInfoSource.PositioningMethods.__and__(int mask)'''
            return QGeoPositionInfoSource.PositioningMethods()
        def __xor__(self, f):
            '''QGeoPositionInfoSource.PositioningMethods QGeoPositionInfoSource.PositioningMethods.__xor__(QGeoPositionInfoSource.PositioningMethods f)'''
            return QGeoPositionInfoSource.PositioningMethods()
        def __xor__(self, f):
            '''QGeoPositionInfoSource.PositioningMethods QGeoPositionInfoSource.PositioningMethods.__xor__(int f)'''
            return QGeoPositionInfoSource.PositioningMethods()
        def __or__(self, f):
            '''QGeoPositionInfoSource.PositioningMethods QGeoPositionInfoSource.PositioningMethods.__or__(QGeoPositionInfoSource.PositioningMethods f)'''
            return QGeoPositionInfoSource.PositioningMethods()
        def __or__(self, f):
            '''QGeoPositionInfoSource.PositioningMethods QGeoPositionInfoSource.PositioningMethods.__or__(int f)'''
            return QGeoPositionInfoSource.PositioningMethods()
        def __int__(self):
            '''int QGeoPositionInfoSource.PositioningMethods.__int__()'''
            return int()
        def __ixor__(self, f):
            '''QGeoPositionInfoSource.PositioningMethods QGeoPositionInfoSource.PositioningMethods.__ixor__(QGeoPositionInfoSource.PositioningMethods f)'''
            return QGeoPositionInfoSource.PositioningMethods()
        def __ior__(self, f):
            '''QGeoPositionInfoSource.PositioningMethods QGeoPositionInfoSource.PositioningMethods.__ior__(QGeoPositionInfoSource.PositioningMethods f)'''
            return QGeoPositionInfoSource.PositioningMethods()
        def __iand__(self, mask):
            '''QGeoPositionInfoSource.PositioningMethods QGeoPositionInfoSource.PositioningMethods.__iand__(int mask)'''
            return QGeoPositionInfoSource.PositioningMethods()


class QGeoRectangle(QGeoShape):
    """"""
    def __init__(self):
        '''void QGeoRectangle.__init__()'''
    def __init__(self, center, degreesWidth, degreesHeight):
        '''void QGeoRectangle.__init__(QGeoCoordinate center, float degreesWidth, float degreesHeight)'''
    def __init__(self, topLeft, bottomRight):
        '''void QGeoRectangle.__init__(QGeoCoordinate topLeft, QGeoCoordinate bottomRight)'''
    def __init__(self, coordinates):
        '''void QGeoRectangle.__init__(list-of-QGeoCoordinate coordinates)'''
    def __init__(self, other):
        '''void QGeoRectangle.__init__(QGeoRectangle other)'''
    def __init__(self, other):
        '''void QGeoRectangle.__init__(QGeoShape other)'''
    def toString(self):
        '''str QGeoRectangle.toString()'''
        return str()
    def __or__(self, rectangle):
        '''QGeoRectangle QGeoRectangle.__or__(QGeoRectangle rectangle)'''
        return QGeoRectangle()
    def __ior__(self, rectangle):
        '''QGeoRectangle QGeoRectangle.__ior__(QGeoRectangle rectangle)'''
        return QGeoRectangle()
    def united(self, rectangle):
        '''QGeoRectangle QGeoRectangle.united(QGeoRectangle rectangle)'''
        return QGeoRectangle()
    def translated(self, degreesLatitude, degreesLongitude):
        '''QGeoRectangle QGeoRectangle.translated(float degreesLatitude, float degreesLongitude)'''
        return QGeoRectangle()
    def translate(self, degreesLatitude, degreesLongitude):
        '''void QGeoRectangle.translate(float degreesLatitude, float degreesLongitude)'''
    def intersects(self, rectangle):
        '''bool QGeoRectangle.intersects(QGeoRectangle rectangle)'''
        return bool()
    def contains(self, rectangle):
        '''bool QGeoRectangle.contains(QGeoRectangle rectangle)'''
        return bool()
    def height(self):
        '''float QGeoRectangle.height()'''
        return float()
    def setHeight(self, degreesHeight):
        '''void QGeoRectangle.setHeight(float degreesHeight)'''
    def width(self):
        '''float QGeoRectangle.width()'''
        return float()
    def setWidth(self, degreesWidth):
        '''void QGeoRectangle.setWidth(float degreesWidth)'''
    def center(self):
        '''QGeoCoordinate QGeoRectangle.center()'''
        return QGeoCoordinate()
    def setCenter(self, center):
        '''void QGeoRectangle.setCenter(QGeoCoordinate center)'''
    def bottomRight(self):
        '''QGeoCoordinate QGeoRectangle.bottomRight()'''
        return QGeoCoordinate()
    def setBottomRight(self, bottomRight):
        '''void QGeoRectangle.setBottomRight(QGeoCoordinate bottomRight)'''
    def bottomLeft(self):
        '''QGeoCoordinate QGeoRectangle.bottomLeft()'''
        return QGeoCoordinate()
    def setBottomLeft(self, bottomLeft):
        '''void QGeoRectangle.setBottomLeft(QGeoCoordinate bottomLeft)'''
    def topRight(self):
        '''QGeoCoordinate QGeoRectangle.topRight()'''
        return QGeoCoordinate()
    def setTopRight(self, topRight):
        '''void QGeoRectangle.setTopRight(QGeoCoordinate topRight)'''
    def topLeft(self):
        '''QGeoCoordinate QGeoRectangle.topLeft()'''
        return QGeoCoordinate()
    def setTopLeft(self, topLeft):
        '''void QGeoRectangle.setTopLeft(QGeoCoordinate topLeft)'''
    def __ne__(self, other):
        '''bool QGeoRectangle.__ne__(QGeoRectangle other)'''
        return bool()
    def __eq__(self, other):
        '''bool QGeoRectangle.__eq__(QGeoRectangle other)'''
        return bool()


class QGeoSatelliteInfo():
    """"""
    # Enum QGeoSatelliteInfo.SatelliteSystem
    Undefined = 0
    GPS = 0
    GLONASS = 0

    # Enum QGeoSatelliteInfo.Attribute
    Elevation = 0
    Azimuth = 0

    def __init__(self):
        '''void QGeoSatelliteInfo.__init__()'''
    def __init__(self, other):
        '''void QGeoSatelliteInfo.__init__(QGeoSatelliteInfo other)'''
    def hasAttribute(self, attribute):
        '''bool QGeoSatelliteInfo.hasAttribute(QGeoSatelliteInfo.Attribute attribute)'''
        return bool()
    def removeAttribute(self, attribute):
        '''void QGeoSatelliteInfo.removeAttribute(QGeoSatelliteInfo.Attribute attribute)'''
    def attribute(self, attribute):
        '''float QGeoSatelliteInfo.attribute(QGeoSatelliteInfo.Attribute attribute)'''
        return float()
    def setAttribute(self, attribute, value):
        '''void QGeoSatelliteInfo.setAttribute(QGeoSatelliteInfo.Attribute attribute, float value)'''
    def signalStrength(self):
        '''int QGeoSatelliteInfo.signalStrength()'''
        return int()
    def setSignalStrength(self, signalStrength):
        '''void QGeoSatelliteInfo.setSignalStrength(int signalStrength)'''
    def satelliteIdentifier(self):
        '''int QGeoSatelliteInfo.satelliteIdentifier()'''
        return int()
    def setSatelliteIdentifier(self, satId):
        '''void QGeoSatelliteInfo.setSatelliteIdentifier(int satId)'''
    def satelliteSystem(self):
        '''QGeoSatelliteInfo.SatelliteSystem QGeoSatelliteInfo.satelliteSystem()'''
        return QGeoSatelliteInfo.SatelliteSystem()
    def setSatelliteSystem(self, system):
        '''void QGeoSatelliteInfo.setSatelliteSystem(QGeoSatelliteInfo.SatelliteSystem system)'''
    def __ne__(self, other):
        '''bool QGeoSatelliteInfo.__ne__(QGeoSatelliteInfo other)'''
        return bool()
    def __eq__(self, other):
        '''bool QGeoSatelliteInfo.__eq__(QGeoSatelliteInfo other)'''
        return bool()


class QGeoSatelliteInfoSource(QObject):
    """"""
    # Enum QGeoSatelliteInfoSource.Error
    AccessError = 0
    ClosedError = 0
    NoError = 0
    UnknownSourceError = 0

    def __init__(self, parent):
        '''void QGeoSatelliteInfoSource.__init__(QObject parent)'''
    requestTimeout = pyqtSignal() # void requestTimeout() - signal
    satellitesInUseUpdated = pyqtSignal() # void satellitesInUseUpdated(const QListlt;QGeoSatelliteInfogt;amp;) - signal
    satellitesInViewUpdated = pyqtSignal() # void satellitesInViewUpdated(const QListlt;QGeoSatelliteInfogt;amp;) - signal
    def requestUpdate(self, timeout = 0):
        '''abstract void QGeoSatelliteInfoSource.requestUpdate(int timeout = 0)'''
    def stopUpdates(self):
        '''abstract void QGeoSatelliteInfoSource.stopUpdates()'''
    def startUpdates(self):
        '''abstract void QGeoSatelliteInfoSource.startUpdates()'''
    def error(self):
        '''abstract QGeoSatelliteInfoSource.Error QGeoSatelliteInfoSource.error()'''
        return QGeoSatelliteInfoSource.Error()
    error = pyqtSignal() # void error(QGeoSatelliteInfoSource::Error) - signal
    def minimumUpdateInterval(self):
        '''abstract int QGeoSatelliteInfoSource.minimumUpdateInterval()'''
        return int()
    def updateInterval(self):
        '''int QGeoSatelliteInfoSource.updateInterval()'''
        return int()
    def setUpdateInterval(self, msec):
        '''void QGeoSatelliteInfoSource.setUpdateInterval(int msec)'''
    def sourceName(self):
        '''str QGeoSatelliteInfoSource.sourceName()'''
        return str()
    def availableSources(self):
        '''static list-of-str QGeoSatelliteInfoSource.availableSources()'''
        return [str()]
    def createSource(self, sourceName, parent):
        '''static QGeoSatelliteInfoSource QGeoSatelliteInfoSource.createSource(str sourceName, QObject parent)'''
        return QGeoSatelliteInfoSource()
    def createDefaultSource(self, parent):
        '''static QGeoSatelliteInfoSource QGeoSatelliteInfoSource.createDefaultSource(QObject parent)'''
        return QGeoSatelliteInfoSource()


class QNmeaPositionInfoSource(QGeoPositionInfoSource):
    """"""
    # Enum QNmeaPositionInfoSource.UpdateMode
    RealTimeMode = 0
    SimulationMode = 0

    def __init__(self, updateMode, parent = None):
        '''void QNmeaPositionInfoSource.__init__(QNmeaPositionInfoSource.UpdateMode updateMode, QObject parent = None)'''
    def userEquivalentRangeError(self):
        '''float QNmeaPositionInfoSource.userEquivalentRangeError()'''
        return float()
    def setUserEquivalentRangeError(self, uere):
        '''void QNmeaPositionInfoSource.setUserEquivalentRangeError(float uere)'''
    def parsePosInfoFromNmeaData(self, data, size, posInfo, hasFix):
        '''bool QNmeaPositionInfoSource.parsePosInfoFromNmeaData(str data, int size, QGeoPositionInfo posInfo, bool hasFix)'''
        return bool()
    def requestUpdate(self, timeout = 0):
        '''void QNmeaPositionInfoSource.requestUpdate(int timeout = 0)'''
    def stopUpdates(self):
        '''void QNmeaPositionInfoSource.stopUpdates()'''
    def startUpdates(self):
        '''void QNmeaPositionInfoSource.startUpdates()'''
    def error(self):
        '''QGeoPositionInfoSource.Error QNmeaPositionInfoSource.error()'''
        return QGeoPositionInfoSource.Error()
    def minimumUpdateInterval(self):
        '''int QNmeaPositionInfoSource.minimumUpdateInterval()'''
        return int()
    def supportedPositioningMethods(self):
        '''QGeoPositionInfoSource.PositioningMethods QNmeaPositionInfoSource.supportedPositioningMethods()'''
        return QGeoPositionInfoSource.PositioningMethods()
    def lastKnownPosition(self, fromSatellitePositioningMethodsOnly = False):
        '''QGeoPositionInfo QNmeaPositionInfoSource.lastKnownPosition(bool fromSatellitePositioningMethodsOnly = False)'''
        return QGeoPositionInfo()
    def setUpdateInterval(self, msec):
        '''void QNmeaPositionInfoSource.setUpdateInterval(int msec)'''
    def device(self):
        '''QIODevice QNmeaPositionInfoSource.device()'''
        return QIODevice()
    def setDevice(self, source):
        '''void QNmeaPositionInfoSource.setDevice(QIODevice source)'''
    def updateMode(self):
        '''QNmeaPositionInfoSource.UpdateMode QNmeaPositionInfoSource.updateMode()'''
        return QNmeaPositionInfoSource.UpdateMode()


