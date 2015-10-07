class pyqtSignal():
 def connect(self, targetSignal): pass
 def emit(self, *args): pass
from QtCore import *

from QtWidgets import *

import datetime

class QGeoCodeReply(QObject):
    """"""
    # Enum QGeoCodeReply.Error
    NoError = 0
    EngineNotSetError = 0
    CommunicationError = 0
    ParseError = 0
    UnsupportedOptionError = 0
    CombinationError = 0
    UnknownError = 0

    def __init__(self, error, errorString, parent = None):
        '''void QGeoCodeReply.__init__(QGeoCodeReply.Error error, str errorString, QObject parent = None)'''
    def __init__(self, parent = None):
        '''void QGeoCodeReply.__init__(QObject parent = None)'''
    def setOffset(self, offset):
        '''void QGeoCodeReply.setOffset(int offset)'''
    def setLimit(self, limit):
        '''void QGeoCodeReply.setLimit(int limit)'''
    def setLocations(self, locations):
        '''void QGeoCodeReply.setLocations(list-of-QGeoLocation locations)'''
    def addLocation(self, location):
        '''void QGeoCodeReply.addLocation(QGeoLocation location)'''
    def setViewport(self, viewport):
        '''void QGeoCodeReply.setViewport(QGeoShape viewport)'''
    def setFinished(self, finished):
        '''void QGeoCodeReply.setFinished(bool finished)'''
    def setError(self, error, errorString):
        '''void QGeoCodeReply.setError(QGeoCodeReply.Error error, str errorString)'''
    finished = pyqtSignal() # void finished() - signal
    def abort(self):
        '''void QGeoCodeReply.abort()'''
    def offset(self):
        '''int QGeoCodeReply.offset()'''
        return int()
    def limit(self):
        '''int QGeoCodeReply.limit()'''
        return int()
    def locations(self):
        '''list-of-QGeoLocation QGeoCodeReply.locations()'''
        return [QGeoLocation()]
    def viewport(self):
        '''QGeoShape QGeoCodeReply.viewport()'''
        return QGeoShape()
    def errorString(self):
        '''str QGeoCodeReply.errorString()'''
        return str()
    def error(self):
        '''QGeoCodeReply.Error QGeoCodeReply.error()'''
        return QGeoCodeReply.Error()
    error = pyqtSignal() # void error(QGeoCodeReply::Error,const QStringamp; = QString()) - signal
    def isFinished(self):
        '''bool QGeoCodeReply.isFinished()'''
        return bool()


class QGeoCodingManager(QObject):
    """"""
    error = pyqtSignal() # void error(QGeoCodeReply*,QGeoCodeReply::Error,QString = QString()) - signal
    finished = pyqtSignal() # void finished(QGeoCodeReply*) - signal
    def locale(self):
        '''QLocale QGeoCodingManager.locale()'''
        return QLocale()
    def setLocale(self, locale):
        '''void QGeoCodingManager.setLocale(QLocale locale)'''
    def reverseGeocode(self, coordinate, bounds = QGeoShape()):
        '''QGeoCodeReply QGeoCodingManager.reverseGeocode(QGeoCoordinate coordinate, QGeoShape bounds = QGeoShape())'''
        return QGeoCodeReply()
    def geocode(self, address, bounds = QGeoShape()):
        '''QGeoCodeReply QGeoCodingManager.geocode(QGeoAddress address, QGeoShape bounds = QGeoShape())'''
        return QGeoCodeReply()
    def geocode(self, searchString, limit = None, offset = 0, bounds = QGeoShape()):
        '''QGeoCodeReply QGeoCodingManager.geocode(str searchString, int limit = -1, int offset = 0, QGeoShape bounds = QGeoShape())'''
        return QGeoCodeReply()
    def managerVersion(self):
        '''int QGeoCodingManager.managerVersion()'''
        return int()
    def managerName(self):
        '''str QGeoCodingManager.managerName()'''
        return str()


class QGeoCodingManagerEngine(QObject):
    """"""
    def __init__(self, parameters, parent = None):
        '''void QGeoCodingManagerEngine.__init__(dict-of-str-object parameters, QObject parent = None)'''
    error = pyqtSignal() # void error(QGeoCodeReply*,QGeoCodeReply::Error,QString = QString()) - signal
    finished = pyqtSignal() # void finished(QGeoCodeReply*) - signal
    def locale(self):
        '''QLocale QGeoCodingManagerEngine.locale()'''
        return QLocale()
    def setLocale(self, locale):
        '''void QGeoCodingManagerEngine.setLocale(QLocale locale)'''
    def reverseGeocode(self, coordinate, bounds):
        '''QGeoCodeReply QGeoCodingManagerEngine.reverseGeocode(QGeoCoordinate coordinate, QGeoShape bounds)'''
        return QGeoCodeReply()
    def geocode(self, address, bounds):
        '''QGeoCodeReply QGeoCodingManagerEngine.geocode(QGeoAddress address, QGeoShape bounds)'''
        return QGeoCodeReply()
    def geocode(self, address, limit, offset, bounds):
        '''QGeoCodeReply QGeoCodingManagerEngine.geocode(str address, int limit, int offset, QGeoShape bounds)'''
        return QGeoCodeReply()
    def managerVersion(self):
        '''int QGeoCodingManagerEngine.managerVersion()'''
        return int()
    def managerName(self):
        '''str QGeoCodingManagerEngine.managerName()'''
        return str()


class QGeoManeuver():
    """"""
    # Enum QGeoManeuver.InstructionDirection
    NoDirection = 0
    DirectionForward = 0
    DirectionBearRight = 0
    DirectionLightRight = 0
    DirectionRight = 0
    DirectionHardRight = 0
    DirectionUTurnRight = 0
    DirectionUTurnLeft = 0
    DirectionHardLeft = 0
    DirectionLeft = 0
    DirectionLightLeft = 0
    DirectionBearLeft = 0

    def __init__(self):
        '''void QGeoManeuver.__init__()'''
    def __init__(self, other):
        '''void QGeoManeuver.__init__(QGeoManeuver other)'''
    def waypoint(self):
        '''QGeoCoordinate QGeoManeuver.waypoint()'''
        return QGeoCoordinate()
    def setWaypoint(self, coordinate):
        '''void QGeoManeuver.setWaypoint(QGeoCoordinate coordinate)'''
    def distanceToNextInstruction(self):
        '''float QGeoManeuver.distanceToNextInstruction()'''
        return float()
    def setDistanceToNextInstruction(self, distance):
        '''void QGeoManeuver.setDistanceToNextInstruction(float distance)'''
    def timeToNextInstruction(self):
        '''int QGeoManeuver.timeToNextInstruction()'''
        return int()
    def setTimeToNextInstruction(self, secs):
        '''void QGeoManeuver.setTimeToNextInstruction(int secs)'''
    def direction(self):
        '''QGeoManeuver.InstructionDirection QGeoManeuver.direction()'''
        return QGeoManeuver.InstructionDirection()
    def setDirection(self, direction):
        '''void QGeoManeuver.setDirection(QGeoManeuver.InstructionDirection direction)'''
    def instructionText(self):
        '''str QGeoManeuver.instructionText()'''
        return str()
    def setInstructionText(self, instructionText):
        '''void QGeoManeuver.setInstructionText(str instructionText)'''
    def position(self):
        '''QGeoCoordinate QGeoManeuver.position()'''
        return QGeoCoordinate()
    def setPosition(self, position):
        '''void QGeoManeuver.setPosition(QGeoCoordinate position)'''
    def isValid(self):
        '''bool QGeoManeuver.isValid()'''
        return bool()
    def __ne__(self, other):
        '''bool QGeoManeuver.__ne__(QGeoManeuver other)'''
        return bool()
    def __eq__(self, other):
        '''bool QGeoManeuver.__eq__(QGeoManeuver other)'''
        return bool()


class QGeoRoute():
    """"""
    def __init__(self):
        '''void QGeoRoute.__init__()'''
    def __init__(self, other):
        '''void QGeoRoute.__init__(QGeoRoute other)'''
    def path(self):
        '''list-of-QGeoCoordinate QGeoRoute.path()'''
        return [QGeoCoordinate()]
    def setPath(self, path):
        '''void QGeoRoute.setPath(list-of-QGeoCoordinate path)'''
    def travelMode(self):
        '''QGeoRouteRequest.TravelMode QGeoRoute.travelMode()'''
        return QGeoRouteRequest.TravelMode()
    def setTravelMode(self, mode):
        '''void QGeoRoute.setTravelMode(QGeoRouteRequest.TravelMode mode)'''
    def distance(self):
        '''float QGeoRoute.distance()'''
        return float()
    def setDistance(self, distance):
        '''void QGeoRoute.setDistance(float distance)'''
    def travelTime(self):
        '''int QGeoRoute.travelTime()'''
        return int()
    def setTravelTime(self, secs):
        '''void QGeoRoute.setTravelTime(int secs)'''
    def firstRouteSegment(self):
        '''QGeoRouteSegment QGeoRoute.firstRouteSegment()'''
        return QGeoRouteSegment()
    def setFirstRouteSegment(self, routeSegment):
        '''void QGeoRoute.setFirstRouteSegment(QGeoRouteSegment routeSegment)'''
    def bounds(self):
        '''QGeoRectangle QGeoRoute.bounds()'''
        return QGeoRectangle()
    def setBounds(self, bounds):
        '''void QGeoRoute.setBounds(QGeoRectangle bounds)'''
    def request(self):
        '''QGeoRouteRequest QGeoRoute.request()'''
        return QGeoRouteRequest()
    def setRequest(self, request):
        '''void QGeoRoute.setRequest(QGeoRouteRequest request)'''
    def routeId(self):
        '''str QGeoRoute.routeId()'''
        return str()
    def setRouteId(self, id):
        '''void QGeoRoute.setRouteId(str id)'''
    def __ne__(self, other):
        '''bool QGeoRoute.__ne__(QGeoRoute other)'''
        return bool()
    def __eq__(self, other):
        '''bool QGeoRoute.__eq__(QGeoRoute other)'''
        return bool()


class QGeoRouteReply(QObject):
    """"""
    # Enum QGeoRouteReply.Error
    NoError = 0
    EngineNotSetError = 0
    CommunicationError = 0
    ParseError = 0
    UnsupportedOptionError = 0
    UnknownError = 0

    def __init__(self, error, errorString, parent = None):
        '''void QGeoRouteReply.__init__(QGeoRouteReply.Error error, str errorString, QObject parent = None)'''
    def __init__(self, request, parent = None):
        '''void QGeoRouteReply.__init__(QGeoRouteRequest request, QObject parent = None)'''
    def addRoutes(self, routes):
        '''void QGeoRouteReply.addRoutes(list-of-QGeoRoute routes)'''
    def setRoutes(self, routes):
        '''void QGeoRouteReply.setRoutes(list-of-QGeoRoute routes)'''
    def setFinished(self, finished):
        '''void QGeoRouteReply.setFinished(bool finished)'''
    def setError(self, error, errorString):
        '''void QGeoRouteReply.setError(QGeoRouteReply.Error error, str errorString)'''
    finished = pyqtSignal() # void finished() - signal
    def abort(self):
        '''void QGeoRouteReply.abort()'''
    def routes(self):
        '''list-of-QGeoRoute QGeoRouteReply.routes()'''
        return [QGeoRoute()]
    def request(self):
        '''QGeoRouteRequest QGeoRouteReply.request()'''
        return QGeoRouteRequest()
    def errorString(self):
        '''str QGeoRouteReply.errorString()'''
        return str()
    def error(self):
        '''QGeoRouteReply.Error QGeoRouteReply.error()'''
        return QGeoRouteReply.Error()
    error = pyqtSignal() # void error(QGeoRouteReply::Error,const QStringamp; = QString()) - signal
    def isFinished(self):
        '''bool QGeoRouteReply.isFinished()'''
        return bool()


class QGeoRouteRequest():
    """"""
    # Enum QGeoRouteRequest.ManeuverDetail
    NoManeuvers = 0
    BasicManeuvers = 0

    # Enum QGeoRouteRequest.SegmentDetail
    NoSegmentData = 0
    BasicSegmentData = 0

    # Enum QGeoRouteRequest.RouteOptimization
    ShortestRoute = 0
    FastestRoute = 0
    MostEconomicRoute = 0
    MostScenicRoute = 0

    # Enum QGeoRouteRequest.FeatureWeight
    NeutralFeatureWeight = 0
    PreferFeatureWeight = 0
    RequireFeatureWeight = 0
    AvoidFeatureWeight = 0
    DisallowFeatureWeight = 0

    # Enum QGeoRouteRequest.FeatureType
    NoFeature = 0
    TollFeature = 0
    HighwayFeature = 0
    PublicTransitFeature = 0
    FerryFeature = 0
    TunnelFeature = 0
    DirtRoadFeature = 0
    ParksFeature = 0
    MotorPoolLaneFeature = 0

    # Enum QGeoRouteRequest.TravelMode
    CarTravel = 0
    PedestrianTravel = 0
    BicycleTravel = 0
    PublicTransitTravel = 0
    TruckTravel = 0

    def __init__(self, waypoints = None):
        '''void QGeoRouteRequest.__init__(list-of-QGeoCoordinate waypoints = QListlt;QGeoCoordinategt;())'''
    def __init__(self, origin, destination):
        '''void QGeoRouteRequest.__init__(QGeoCoordinate origin, QGeoCoordinate destination)'''
    def __init__(self, other):
        '''void QGeoRouteRequest.__init__(QGeoRouteRequest other)'''
    def maneuverDetail(self):
        '''QGeoRouteRequest.ManeuverDetail QGeoRouteRequest.maneuverDetail()'''
        return QGeoRouteRequest.ManeuverDetail()
    def setManeuverDetail(self, maneuverDetail):
        '''void QGeoRouteRequest.setManeuverDetail(QGeoRouteRequest.ManeuverDetail maneuverDetail)'''
    def segmentDetail(self):
        '''QGeoRouteRequest.SegmentDetail QGeoRouteRequest.segmentDetail()'''
        return QGeoRouteRequest.SegmentDetail()
    def setSegmentDetail(self, segmentDetail):
        '''void QGeoRouteRequest.setSegmentDetail(QGeoRouteRequest.SegmentDetail segmentDetail)'''
    def routeOptimization(self):
        '''QGeoRouteRequest.RouteOptimizations QGeoRouteRequest.routeOptimization()'''
        return QGeoRouteRequest.RouteOptimizations()
    def setRouteOptimization(self, optimization):
        '''void QGeoRouteRequest.setRouteOptimization(QGeoRouteRequest.RouteOptimizations optimization)'''
    def featureTypes(self):
        '''list-of-QGeoRouteRequest.FeatureType QGeoRouteRequest.featureTypes()'''
        return [QGeoRouteRequest.FeatureType()]
    def featureWeight(self, featureType):
        '''QGeoRouteRequest.FeatureWeight QGeoRouteRequest.featureWeight(QGeoRouteRequest.FeatureType featureType)'''
        return QGeoRouteRequest.FeatureWeight()
    def setFeatureWeight(self, featureType, featureWeight):
        '''void QGeoRouteRequest.setFeatureWeight(QGeoRouteRequest.FeatureType featureType, QGeoRouteRequest.FeatureWeight featureWeight)'''
    def travelModes(self):
        '''QGeoRouteRequest.TravelModes QGeoRouteRequest.travelModes()'''
        return QGeoRouteRequest.TravelModes()
    def setTravelModes(self, travelModes):
        '''void QGeoRouteRequest.setTravelModes(QGeoRouteRequest.TravelModes travelModes)'''
    def numberAlternativeRoutes(self):
        '''int QGeoRouteRequest.numberAlternativeRoutes()'''
        return int()
    def setNumberAlternativeRoutes(self, alternatives):
        '''void QGeoRouteRequest.setNumberAlternativeRoutes(int alternatives)'''
    def excludeAreas(self):
        '''list-of-QGeoRectangle QGeoRouteRequest.excludeAreas()'''
        return [QGeoRectangle()]
    def setExcludeAreas(self, areas):
        '''void QGeoRouteRequest.setExcludeAreas(list-of-QGeoRectangle areas)'''
    def waypoints(self):
        '''list-of-QGeoCoordinate QGeoRouteRequest.waypoints()'''
        return [QGeoCoordinate()]
    def setWaypoints(self, waypoints):
        '''void QGeoRouteRequest.setWaypoints(list-of-QGeoCoordinate waypoints)'''
    def __ne__(self, other):
        '''bool QGeoRouteRequest.__ne__(QGeoRouteRequest other)'''
        return bool()
    def __eq__(self, other):
        '''bool QGeoRouteRequest.__eq__(QGeoRouteRequest other)'''
        return bool()
    class ManeuverDetails():
        """"""
        def __init__(self):
            '''QGeoRouteRequest.ManeuverDetails QGeoRouteRequest.ManeuverDetails.__init__()'''
            return QGeoRouteRequest.ManeuverDetails()
        def __init__(self):
            '''int QGeoRouteRequest.ManeuverDetails.__init__()'''
            return int()
        def __init__(self):
            '''void QGeoRouteRequest.ManeuverDetails.__init__()'''
        def __bool__(self):
            '''int QGeoRouteRequest.ManeuverDetails.__bool__()'''
            return int()
        def __ne__(self, f):
            '''bool QGeoRouteRequest.ManeuverDetails.__ne__(QGeoRouteRequest.ManeuverDetails f)'''
            return bool()
        def __eq__(self, f):
            '''bool QGeoRouteRequest.ManeuverDetails.__eq__(QGeoRouteRequest.ManeuverDetails f)'''
            return bool()
        def __invert__(self):
            '''QGeoRouteRequest.ManeuverDetails QGeoRouteRequest.ManeuverDetails.__invert__()'''
            return QGeoRouteRequest.ManeuverDetails()
        def __and__(self, mask):
            '''QGeoRouteRequest.ManeuverDetails QGeoRouteRequest.ManeuverDetails.__and__(int mask)'''
            return QGeoRouteRequest.ManeuverDetails()
        def __xor__(self, f):
            '''QGeoRouteRequest.ManeuverDetails QGeoRouteRequest.ManeuverDetails.__xor__(QGeoRouteRequest.ManeuverDetails f)'''
            return QGeoRouteRequest.ManeuverDetails()
        def __xor__(self, f):
            '''QGeoRouteRequest.ManeuverDetails QGeoRouteRequest.ManeuverDetails.__xor__(int f)'''
            return QGeoRouteRequest.ManeuverDetails()
        def __or__(self, f):
            '''QGeoRouteRequest.ManeuverDetails QGeoRouteRequest.ManeuverDetails.__or__(QGeoRouteRequest.ManeuverDetails f)'''
            return QGeoRouteRequest.ManeuverDetails()
        def __or__(self, f):
            '''QGeoRouteRequest.ManeuverDetails QGeoRouteRequest.ManeuverDetails.__or__(int f)'''
            return QGeoRouteRequest.ManeuverDetails()
        def __int__(self):
            '''int QGeoRouteRequest.ManeuverDetails.__int__()'''
            return int()
        def __ixor__(self, f):
            '''QGeoRouteRequest.ManeuverDetails QGeoRouteRequest.ManeuverDetails.__ixor__(QGeoRouteRequest.ManeuverDetails f)'''
            return QGeoRouteRequest.ManeuverDetails()
        def __ior__(self, f):
            '''QGeoRouteRequest.ManeuverDetails QGeoRouteRequest.ManeuverDetails.__ior__(QGeoRouteRequest.ManeuverDetails f)'''
            return QGeoRouteRequest.ManeuverDetails()
        def __iand__(self, mask):
            '''QGeoRouteRequest.ManeuverDetails QGeoRouteRequest.ManeuverDetails.__iand__(int mask)'''
            return QGeoRouteRequest.ManeuverDetails()
    class RouteOptimizations():
        """"""
        def __init__(self):
            '''QGeoRouteRequest.RouteOptimizations QGeoRouteRequest.RouteOptimizations.__init__()'''
            return QGeoRouteRequest.RouteOptimizations()
        def __init__(self):
            '''int QGeoRouteRequest.RouteOptimizations.__init__()'''
            return int()
        def __init__(self):
            '''void QGeoRouteRequest.RouteOptimizations.__init__()'''
        def __bool__(self):
            '''int QGeoRouteRequest.RouteOptimizations.__bool__()'''
            return int()
        def __ne__(self, f):
            '''bool QGeoRouteRequest.RouteOptimizations.__ne__(QGeoRouteRequest.RouteOptimizations f)'''
            return bool()
        def __eq__(self, f):
            '''bool QGeoRouteRequest.RouteOptimizations.__eq__(QGeoRouteRequest.RouteOptimizations f)'''
            return bool()
        def __invert__(self):
            '''QGeoRouteRequest.RouteOptimizations QGeoRouteRequest.RouteOptimizations.__invert__()'''
            return QGeoRouteRequest.RouteOptimizations()
        def __and__(self, mask):
            '''QGeoRouteRequest.RouteOptimizations QGeoRouteRequest.RouteOptimizations.__and__(int mask)'''
            return QGeoRouteRequest.RouteOptimizations()
        def __xor__(self, f):
            '''QGeoRouteRequest.RouteOptimizations QGeoRouteRequest.RouteOptimizations.__xor__(QGeoRouteRequest.RouteOptimizations f)'''
            return QGeoRouteRequest.RouteOptimizations()
        def __xor__(self, f):
            '''QGeoRouteRequest.RouteOptimizations QGeoRouteRequest.RouteOptimizations.__xor__(int f)'''
            return QGeoRouteRequest.RouteOptimizations()
        def __or__(self, f):
            '''QGeoRouteRequest.RouteOptimizations QGeoRouteRequest.RouteOptimizations.__or__(QGeoRouteRequest.RouteOptimizations f)'''
            return QGeoRouteRequest.RouteOptimizations()
        def __or__(self, f):
            '''QGeoRouteRequest.RouteOptimizations QGeoRouteRequest.RouteOptimizations.__or__(int f)'''
            return QGeoRouteRequest.RouteOptimizations()
        def __int__(self):
            '''int QGeoRouteRequest.RouteOptimizations.__int__()'''
            return int()
        def __ixor__(self, f):
            '''QGeoRouteRequest.RouteOptimizations QGeoRouteRequest.RouteOptimizations.__ixor__(QGeoRouteRequest.RouteOptimizations f)'''
            return QGeoRouteRequest.RouteOptimizations()
        def __ior__(self, f):
            '''QGeoRouteRequest.RouteOptimizations QGeoRouteRequest.RouteOptimizations.__ior__(QGeoRouteRequest.RouteOptimizations f)'''
            return QGeoRouteRequest.RouteOptimizations()
        def __iand__(self, mask):
            '''QGeoRouteRequest.RouteOptimizations QGeoRouteRequest.RouteOptimizations.__iand__(int mask)'''
            return QGeoRouteRequest.RouteOptimizations()
    class FeatureTypes():
        """"""
        def __init__(self):
            '''QGeoRouteRequest.FeatureTypes QGeoRouteRequest.FeatureTypes.__init__()'''
            return QGeoRouteRequest.FeatureTypes()
        def __init__(self):
            '''int QGeoRouteRequest.FeatureTypes.__init__()'''
            return int()
        def __init__(self):
            '''void QGeoRouteRequest.FeatureTypes.__init__()'''
        def __bool__(self):
            '''int QGeoRouteRequest.FeatureTypes.__bool__()'''
            return int()
        def __ne__(self, f):
            '''bool QGeoRouteRequest.FeatureTypes.__ne__(QGeoRouteRequest.FeatureTypes f)'''
            return bool()
        def __eq__(self, f):
            '''bool QGeoRouteRequest.FeatureTypes.__eq__(QGeoRouteRequest.FeatureTypes f)'''
            return bool()
        def __invert__(self):
            '''QGeoRouteRequest.FeatureTypes QGeoRouteRequest.FeatureTypes.__invert__()'''
            return QGeoRouteRequest.FeatureTypes()
        def __and__(self, mask):
            '''QGeoRouteRequest.FeatureTypes QGeoRouteRequest.FeatureTypes.__and__(int mask)'''
            return QGeoRouteRequest.FeatureTypes()
        def __xor__(self, f):
            '''QGeoRouteRequest.FeatureTypes QGeoRouteRequest.FeatureTypes.__xor__(QGeoRouteRequest.FeatureTypes f)'''
            return QGeoRouteRequest.FeatureTypes()
        def __xor__(self, f):
            '''QGeoRouteRequest.FeatureTypes QGeoRouteRequest.FeatureTypes.__xor__(int f)'''
            return QGeoRouteRequest.FeatureTypes()
        def __or__(self, f):
            '''QGeoRouteRequest.FeatureTypes QGeoRouteRequest.FeatureTypes.__or__(QGeoRouteRequest.FeatureTypes f)'''
            return QGeoRouteRequest.FeatureTypes()
        def __or__(self, f):
            '''QGeoRouteRequest.FeatureTypes QGeoRouteRequest.FeatureTypes.__or__(int f)'''
            return QGeoRouteRequest.FeatureTypes()
        def __int__(self):
            '''int QGeoRouteRequest.FeatureTypes.__int__()'''
            return int()
        def __ixor__(self, f):
            '''QGeoRouteRequest.FeatureTypes QGeoRouteRequest.FeatureTypes.__ixor__(QGeoRouteRequest.FeatureTypes f)'''
            return QGeoRouteRequest.FeatureTypes()
        def __ior__(self, f):
            '''QGeoRouteRequest.FeatureTypes QGeoRouteRequest.FeatureTypes.__ior__(QGeoRouteRequest.FeatureTypes f)'''
            return QGeoRouteRequest.FeatureTypes()
        def __iand__(self, mask):
            '''QGeoRouteRequest.FeatureTypes QGeoRouteRequest.FeatureTypes.__iand__(int mask)'''
            return QGeoRouteRequest.FeatureTypes()
    class TravelModes():
        """"""
        def __init__(self):
            '''QGeoRouteRequest.TravelModes QGeoRouteRequest.TravelModes.__init__()'''
            return QGeoRouteRequest.TravelModes()
        def __init__(self):
            '''int QGeoRouteRequest.TravelModes.__init__()'''
            return int()
        def __init__(self):
            '''void QGeoRouteRequest.TravelModes.__init__()'''
        def __bool__(self):
            '''int QGeoRouteRequest.TravelModes.__bool__()'''
            return int()
        def __ne__(self, f):
            '''bool QGeoRouteRequest.TravelModes.__ne__(QGeoRouteRequest.TravelModes f)'''
            return bool()
        def __eq__(self, f):
            '''bool QGeoRouteRequest.TravelModes.__eq__(QGeoRouteRequest.TravelModes f)'''
            return bool()
        def __invert__(self):
            '''QGeoRouteRequest.TravelModes QGeoRouteRequest.TravelModes.__invert__()'''
            return QGeoRouteRequest.TravelModes()
        def __and__(self, mask):
            '''QGeoRouteRequest.TravelModes QGeoRouteRequest.TravelModes.__and__(int mask)'''
            return QGeoRouteRequest.TravelModes()
        def __xor__(self, f):
            '''QGeoRouteRequest.TravelModes QGeoRouteRequest.TravelModes.__xor__(QGeoRouteRequest.TravelModes f)'''
            return QGeoRouteRequest.TravelModes()
        def __xor__(self, f):
            '''QGeoRouteRequest.TravelModes QGeoRouteRequest.TravelModes.__xor__(int f)'''
            return QGeoRouteRequest.TravelModes()
        def __or__(self, f):
            '''QGeoRouteRequest.TravelModes QGeoRouteRequest.TravelModes.__or__(QGeoRouteRequest.TravelModes f)'''
            return QGeoRouteRequest.TravelModes()
        def __or__(self, f):
            '''QGeoRouteRequest.TravelModes QGeoRouteRequest.TravelModes.__or__(int f)'''
            return QGeoRouteRequest.TravelModes()
        def __int__(self):
            '''int QGeoRouteRequest.TravelModes.__int__()'''
            return int()
        def __ixor__(self, f):
            '''QGeoRouteRequest.TravelModes QGeoRouteRequest.TravelModes.__ixor__(QGeoRouteRequest.TravelModes f)'''
            return QGeoRouteRequest.TravelModes()
        def __ior__(self, f):
            '''QGeoRouteRequest.TravelModes QGeoRouteRequest.TravelModes.__ior__(QGeoRouteRequest.TravelModes f)'''
            return QGeoRouteRequest.TravelModes()
        def __iand__(self, mask):
            '''QGeoRouteRequest.TravelModes QGeoRouteRequest.TravelModes.__iand__(int mask)'''
            return QGeoRouteRequest.TravelModes()
    class FeatureWeights():
        """"""
        def __init__(self):
            '''QGeoRouteRequest.FeatureWeights QGeoRouteRequest.FeatureWeights.__init__()'''
            return QGeoRouteRequest.FeatureWeights()
        def __init__(self):
            '''int QGeoRouteRequest.FeatureWeights.__init__()'''
            return int()
        def __init__(self):
            '''void QGeoRouteRequest.FeatureWeights.__init__()'''
        def __bool__(self):
            '''int QGeoRouteRequest.FeatureWeights.__bool__()'''
            return int()
        def __ne__(self, f):
            '''bool QGeoRouteRequest.FeatureWeights.__ne__(QGeoRouteRequest.FeatureWeights f)'''
            return bool()
        def __eq__(self, f):
            '''bool QGeoRouteRequest.FeatureWeights.__eq__(QGeoRouteRequest.FeatureWeights f)'''
            return bool()
        def __invert__(self):
            '''QGeoRouteRequest.FeatureWeights QGeoRouteRequest.FeatureWeights.__invert__()'''
            return QGeoRouteRequest.FeatureWeights()
        def __and__(self, mask):
            '''QGeoRouteRequest.FeatureWeights QGeoRouteRequest.FeatureWeights.__and__(int mask)'''
            return QGeoRouteRequest.FeatureWeights()
        def __xor__(self, f):
            '''QGeoRouteRequest.FeatureWeights QGeoRouteRequest.FeatureWeights.__xor__(QGeoRouteRequest.FeatureWeights f)'''
            return QGeoRouteRequest.FeatureWeights()
        def __xor__(self, f):
            '''QGeoRouteRequest.FeatureWeights QGeoRouteRequest.FeatureWeights.__xor__(int f)'''
            return QGeoRouteRequest.FeatureWeights()
        def __or__(self, f):
            '''QGeoRouteRequest.FeatureWeights QGeoRouteRequest.FeatureWeights.__or__(QGeoRouteRequest.FeatureWeights f)'''
            return QGeoRouteRequest.FeatureWeights()
        def __or__(self, f):
            '''QGeoRouteRequest.FeatureWeights QGeoRouteRequest.FeatureWeights.__or__(int f)'''
            return QGeoRouteRequest.FeatureWeights()
        def __int__(self):
            '''int QGeoRouteRequest.FeatureWeights.__int__()'''
            return int()
        def __ixor__(self, f):
            '''QGeoRouteRequest.FeatureWeights QGeoRouteRequest.FeatureWeights.__ixor__(QGeoRouteRequest.FeatureWeights f)'''
            return QGeoRouteRequest.FeatureWeights()
        def __ior__(self, f):
            '''QGeoRouteRequest.FeatureWeights QGeoRouteRequest.FeatureWeights.__ior__(QGeoRouteRequest.FeatureWeights f)'''
            return QGeoRouteRequest.FeatureWeights()
        def __iand__(self, mask):
            '''QGeoRouteRequest.FeatureWeights QGeoRouteRequest.FeatureWeights.__iand__(int mask)'''
            return QGeoRouteRequest.FeatureWeights()
    class SegmentDetails():
        """"""
        def __init__(self):
            '''QGeoRouteRequest.SegmentDetails QGeoRouteRequest.SegmentDetails.__init__()'''
            return QGeoRouteRequest.SegmentDetails()
        def __init__(self):
            '''int QGeoRouteRequest.SegmentDetails.__init__()'''
            return int()
        def __init__(self):
            '''void QGeoRouteRequest.SegmentDetails.__init__()'''
        def __bool__(self):
            '''int QGeoRouteRequest.SegmentDetails.__bool__()'''
            return int()
        def __ne__(self, f):
            '''bool QGeoRouteRequest.SegmentDetails.__ne__(QGeoRouteRequest.SegmentDetails f)'''
            return bool()
        def __eq__(self, f):
            '''bool QGeoRouteRequest.SegmentDetails.__eq__(QGeoRouteRequest.SegmentDetails f)'''
            return bool()
        def __invert__(self):
            '''QGeoRouteRequest.SegmentDetails QGeoRouteRequest.SegmentDetails.__invert__()'''
            return QGeoRouteRequest.SegmentDetails()
        def __and__(self, mask):
            '''QGeoRouteRequest.SegmentDetails QGeoRouteRequest.SegmentDetails.__and__(int mask)'''
            return QGeoRouteRequest.SegmentDetails()
        def __xor__(self, f):
            '''QGeoRouteRequest.SegmentDetails QGeoRouteRequest.SegmentDetails.__xor__(QGeoRouteRequest.SegmentDetails f)'''
            return QGeoRouteRequest.SegmentDetails()
        def __xor__(self, f):
            '''QGeoRouteRequest.SegmentDetails QGeoRouteRequest.SegmentDetails.__xor__(int f)'''
            return QGeoRouteRequest.SegmentDetails()
        def __or__(self, f):
            '''QGeoRouteRequest.SegmentDetails QGeoRouteRequest.SegmentDetails.__or__(QGeoRouteRequest.SegmentDetails f)'''
            return QGeoRouteRequest.SegmentDetails()
        def __or__(self, f):
            '''QGeoRouteRequest.SegmentDetails QGeoRouteRequest.SegmentDetails.__or__(int f)'''
            return QGeoRouteRequest.SegmentDetails()
        def __int__(self):
            '''int QGeoRouteRequest.SegmentDetails.__int__()'''
            return int()
        def __ixor__(self, f):
            '''QGeoRouteRequest.SegmentDetails QGeoRouteRequest.SegmentDetails.__ixor__(QGeoRouteRequest.SegmentDetails f)'''
            return QGeoRouteRequest.SegmentDetails()
        def __ior__(self, f):
            '''QGeoRouteRequest.SegmentDetails QGeoRouteRequest.SegmentDetails.__ior__(QGeoRouteRequest.SegmentDetails f)'''
            return QGeoRouteRequest.SegmentDetails()
        def __iand__(self, mask):
            '''QGeoRouteRequest.SegmentDetails QGeoRouteRequest.SegmentDetails.__iand__(int mask)'''
            return QGeoRouteRequest.SegmentDetails()


class QGeoRouteSegment():
    """"""
    def __init__(self):
        '''void QGeoRouteSegment.__init__()'''
    def __init__(self, other):
        '''void QGeoRouteSegment.__init__(QGeoRouteSegment other)'''
    def maneuver(self):
        '''QGeoManeuver QGeoRouteSegment.maneuver()'''
        return QGeoManeuver()
    def setManeuver(self, maneuver):
        '''void QGeoRouteSegment.setManeuver(QGeoManeuver maneuver)'''
    def path(self):
        '''list-of-QGeoCoordinate QGeoRouteSegment.path()'''
        return [QGeoCoordinate()]
    def setPath(self, path):
        '''void QGeoRouteSegment.setPath(list-of-QGeoCoordinate path)'''
    def distance(self):
        '''float QGeoRouteSegment.distance()'''
        return float()
    def setDistance(self, distance):
        '''void QGeoRouteSegment.setDistance(float distance)'''
    def travelTime(self):
        '''int QGeoRouteSegment.travelTime()'''
        return int()
    def setTravelTime(self, secs):
        '''void QGeoRouteSegment.setTravelTime(int secs)'''
    def nextRouteSegment(self):
        '''QGeoRouteSegment QGeoRouteSegment.nextRouteSegment()'''
        return QGeoRouteSegment()
    def setNextRouteSegment(self, routeSegment):
        '''void QGeoRouteSegment.setNextRouteSegment(QGeoRouteSegment routeSegment)'''
    def isValid(self):
        '''bool QGeoRouteSegment.isValid()'''
        return bool()
    def __ne__(self, other):
        '''bool QGeoRouteSegment.__ne__(QGeoRouteSegment other)'''
        return bool()
    def __eq__(self, other):
        '''bool QGeoRouteSegment.__eq__(QGeoRouteSegment other)'''
        return bool()


class QGeoRoutingManager(QObject):
    """"""
    error = pyqtSignal() # void error(QGeoRouteReply*,QGeoRouteReply::Error,QString = QString()) - signal
    finished = pyqtSignal() # void finished(QGeoRouteReply*) - signal
    def measurementSystem(self):
        '''QLocale.MeasurementSystem QGeoRoutingManager.measurementSystem()'''
        return QLocale.MeasurementSystem()
    def setMeasurementSystem(self, system):
        '''void QGeoRoutingManager.setMeasurementSystem(QLocale.MeasurementSystem system)'''
    def locale(self):
        '''QLocale QGeoRoutingManager.locale()'''
        return QLocale()
    def setLocale(self, locale):
        '''void QGeoRoutingManager.setLocale(QLocale locale)'''
    def supportedManeuverDetails(self):
        '''QGeoRouteRequest.ManeuverDetails QGeoRoutingManager.supportedManeuverDetails()'''
        return QGeoRouteRequest.ManeuverDetails()
    def supportedSegmentDetails(self):
        '''QGeoRouteRequest.SegmentDetails QGeoRoutingManager.supportedSegmentDetails()'''
        return QGeoRouteRequest.SegmentDetails()
    def supportedRouteOptimizations(self):
        '''QGeoRouteRequest.RouteOptimizations QGeoRoutingManager.supportedRouteOptimizations()'''
        return QGeoRouteRequest.RouteOptimizations()
    def supportedFeatureWeights(self):
        '''QGeoRouteRequest.FeatureWeights QGeoRoutingManager.supportedFeatureWeights()'''
        return QGeoRouteRequest.FeatureWeights()
    def supportedFeatureTypes(self):
        '''QGeoRouteRequest.FeatureTypes QGeoRoutingManager.supportedFeatureTypes()'''
        return QGeoRouteRequest.FeatureTypes()
    def supportedTravelModes(self):
        '''QGeoRouteRequest.TravelModes QGeoRoutingManager.supportedTravelModes()'''
        return QGeoRouteRequest.TravelModes()
    def updateRoute(self, route, position):
        '''QGeoRouteReply QGeoRoutingManager.updateRoute(QGeoRoute route, QGeoCoordinate position)'''
        return QGeoRouteReply()
    def calculateRoute(self, request):
        '''QGeoRouteReply QGeoRoutingManager.calculateRoute(QGeoRouteRequest request)'''
        return QGeoRouteReply()
    def managerVersion(self):
        '''int QGeoRoutingManager.managerVersion()'''
        return int()
    def managerName(self):
        '''str QGeoRoutingManager.managerName()'''
        return str()


class QGeoRoutingManagerEngine(QObject):
    """"""
    def __init__(self, parameters, parent = None):
        '''void QGeoRoutingManagerEngine.__init__(dict-of-str-object parameters, QObject parent = None)'''
    def setSupportedManeuverDetails(self, maneuverDetails):
        '''void QGeoRoutingManagerEngine.setSupportedManeuverDetails(QGeoRouteRequest.ManeuverDetails maneuverDetails)'''
    def setSupportedSegmentDetails(self, segmentDetails):
        '''void QGeoRoutingManagerEngine.setSupportedSegmentDetails(QGeoRouteRequest.SegmentDetails segmentDetails)'''
    def setSupportedRouteOptimizations(self, optimizations):
        '''void QGeoRoutingManagerEngine.setSupportedRouteOptimizations(QGeoRouteRequest.RouteOptimizations optimizations)'''
    def setSupportedFeatureWeights(self, featureWeights):
        '''void QGeoRoutingManagerEngine.setSupportedFeatureWeights(QGeoRouteRequest.FeatureWeights featureWeights)'''
    def setSupportedFeatureTypes(self, featureTypes):
        '''void QGeoRoutingManagerEngine.setSupportedFeatureTypes(QGeoRouteRequest.FeatureTypes featureTypes)'''
    def setSupportedTravelModes(self, travelModes):
        '''void QGeoRoutingManagerEngine.setSupportedTravelModes(QGeoRouteRequest.TravelModes travelModes)'''
    error = pyqtSignal() # void error(QGeoRouteReply*,QGeoRouteReply::Error,QString = QString()) - signal
    finished = pyqtSignal() # void finished(QGeoRouteReply*) - signal
    def measurementSystem(self):
        '''QLocale.MeasurementSystem QGeoRoutingManagerEngine.measurementSystem()'''
        return QLocale.MeasurementSystem()
    def setMeasurementSystem(self, system):
        '''void QGeoRoutingManagerEngine.setMeasurementSystem(QLocale.MeasurementSystem system)'''
    def locale(self):
        '''QLocale QGeoRoutingManagerEngine.locale()'''
        return QLocale()
    def setLocale(self, locale):
        '''void QGeoRoutingManagerEngine.setLocale(QLocale locale)'''
    def supportedManeuverDetails(self):
        '''QGeoRouteRequest.ManeuverDetails QGeoRoutingManagerEngine.supportedManeuverDetails()'''
        return QGeoRouteRequest.ManeuverDetails()
    def supportedSegmentDetails(self):
        '''QGeoRouteRequest.SegmentDetails QGeoRoutingManagerEngine.supportedSegmentDetails()'''
        return QGeoRouteRequest.SegmentDetails()
    def supportedRouteOptimizations(self):
        '''QGeoRouteRequest.RouteOptimizations QGeoRoutingManagerEngine.supportedRouteOptimizations()'''
        return QGeoRouteRequest.RouteOptimizations()
    def supportedFeatureWeights(self):
        '''QGeoRouteRequest.FeatureWeights QGeoRoutingManagerEngine.supportedFeatureWeights()'''
        return QGeoRouteRequest.FeatureWeights()
    def supportedFeatureTypes(self):
        '''QGeoRouteRequest.FeatureTypes QGeoRoutingManagerEngine.supportedFeatureTypes()'''
        return QGeoRouteRequest.FeatureTypes()
    def supportedTravelModes(self):
        '''QGeoRouteRequest.TravelModes QGeoRoutingManagerEngine.supportedTravelModes()'''
        return QGeoRouteRequest.TravelModes()
    def updateRoute(self, route, position):
        '''QGeoRouteReply QGeoRoutingManagerEngine.updateRoute(QGeoRoute route, QGeoCoordinate position)'''
        return QGeoRouteReply()
    def calculateRoute(self, request):
        '''abstract QGeoRouteReply QGeoRoutingManagerEngine.calculateRoute(QGeoRouteRequest request)'''
        return QGeoRouteReply()
    def managerVersion(self):
        '''int QGeoRoutingManagerEngine.managerVersion()'''
        return int()
    def managerName(self):
        '''str QGeoRoutingManagerEngine.managerName()'''
        return str()


class QGeoServiceProvider(QObject):
    """"""
    # Enum QGeoServiceProvider.PlacesFeature
    NoPlacesFeatures = 0
    OnlinePlacesFeature = 0
    OfflinePlacesFeature = 0
    SavePlaceFeature = 0
    RemovePlaceFeature = 0
    SaveCategoryFeature = 0
    RemoveCategoryFeature = 0
    PlaceRecommendationsFeature = 0
    SearchSuggestionsFeature = 0
    LocalizedPlacesFeature = 0
    NotificationsFeature = 0
    PlaceMatchingFeature = 0
    AnyPlacesFeatures = 0

    # Enum QGeoServiceProvider.MappingFeature
    NoMappingFeatures = 0
    OnlineMappingFeature = 0
    OfflineMappingFeature = 0
    LocalizedMappingFeature = 0
    AnyMappingFeatures = 0

    # Enum QGeoServiceProvider.GeocodingFeature
    NoGeocodingFeatures = 0
    OnlineGeocodingFeature = 0
    OfflineGeocodingFeature = 0
    ReverseGeocodingFeature = 0
    LocalizedGeocodingFeature = 0
    AnyGeocodingFeatures = 0

    # Enum QGeoServiceProvider.RoutingFeature
    NoRoutingFeatures = 0
    OnlineRoutingFeature = 0
    OfflineRoutingFeature = 0
    LocalizedRoutingFeature = 0
    RouteUpdatesFeature = 0
    AlternativeRoutesFeature = 0
    ExcludeAreasRoutingFeature = 0
    AnyRoutingFeatures = 0

    # Enum QGeoServiceProvider.Error
    NoError = 0
    NotSupportedError = 0
    UnknownParameterError = 0
    MissingRequiredParameterError = 0
    ConnectionError = 0

    def __init__(self, providerName, parameters = None, allowExperimental = False):
        '''void QGeoServiceProvider.__init__(str providerName, dict-of-str-object parameters = QMaplt;str,QVariantgt;(), bool allowExperimental = False)'''
    def setAllowExperimental(self, allow):
        '''void QGeoServiceProvider.setAllowExperimental(bool allow)'''
    def setLocale(self, locale):
        '''void QGeoServiceProvider.setLocale(QLocale locale)'''
    def setParameters(self, parameters):
        '''void QGeoServiceProvider.setParameters(dict-of-str-object parameters)'''
    def errorString(self):
        '''str QGeoServiceProvider.errorString()'''
        return str()
    def error(self):
        '''QGeoServiceProvider.Error QGeoServiceProvider.error()'''
        return QGeoServiceProvider.Error()
    def placeManager(self):
        '''QPlaceManager QGeoServiceProvider.placeManager()'''
        return QPlaceManager()
    def routingManager(self):
        '''QGeoRoutingManager QGeoServiceProvider.routingManager()'''
        return QGeoRoutingManager()
    def geocodingManager(self):
        '''QGeoCodingManager QGeoServiceProvider.geocodingManager()'''
        return QGeoCodingManager()
    def placesFeatures(self):
        '''QGeoServiceProvider.PlacesFeatures QGeoServiceProvider.placesFeatures()'''
        return QGeoServiceProvider.PlacesFeatures()
    def mappingFeatures(self):
        '''QGeoServiceProvider.MappingFeatures QGeoServiceProvider.mappingFeatures()'''
        return QGeoServiceProvider.MappingFeatures()
    def geocodingFeatures(self):
        '''QGeoServiceProvider.GeocodingFeatures QGeoServiceProvider.geocodingFeatures()'''
        return QGeoServiceProvider.GeocodingFeatures()
    def routingFeatures(self):
        '''QGeoServiceProvider.RoutingFeatures QGeoServiceProvider.routingFeatures()'''
        return QGeoServiceProvider.RoutingFeatures()
    def availableServiceProviders(self):
        '''static list-of-str QGeoServiceProvider.availableServiceProviders()'''
        return [str()]
    class GeocodingFeatures():
        """"""
        def __init__(self):
            '''QGeoServiceProvider.GeocodingFeatures QGeoServiceProvider.GeocodingFeatures.__init__()'''
            return QGeoServiceProvider.GeocodingFeatures()
        def __init__(self):
            '''int QGeoServiceProvider.GeocodingFeatures.__init__()'''
            return int()
        def __init__(self):
            '''void QGeoServiceProvider.GeocodingFeatures.__init__()'''
        def __bool__(self):
            '''int QGeoServiceProvider.GeocodingFeatures.__bool__()'''
            return int()
        def __ne__(self, f):
            '''bool QGeoServiceProvider.GeocodingFeatures.__ne__(QGeoServiceProvider.GeocodingFeatures f)'''
            return bool()
        def __eq__(self, f):
            '''bool QGeoServiceProvider.GeocodingFeatures.__eq__(QGeoServiceProvider.GeocodingFeatures f)'''
            return bool()
        def __invert__(self):
            '''QGeoServiceProvider.GeocodingFeatures QGeoServiceProvider.GeocodingFeatures.__invert__()'''
            return QGeoServiceProvider.GeocodingFeatures()
        def __and__(self, mask):
            '''QGeoServiceProvider.GeocodingFeatures QGeoServiceProvider.GeocodingFeatures.__and__(int mask)'''
            return QGeoServiceProvider.GeocodingFeatures()
        def __xor__(self, f):
            '''QGeoServiceProvider.GeocodingFeatures QGeoServiceProvider.GeocodingFeatures.__xor__(QGeoServiceProvider.GeocodingFeatures f)'''
            return QGeoServiceProvider.GeocodingFeatures()
        def __xor__(self, f):
            '''QGeoServiceProvider.GeocodingFeatures QGeoServiceProvider.GeocodingFeatures.__xor__(int f)'''
            return QGeoServiceProvider.GeocodingFeatures()
        def __or__(self, f):
            '''QGeoServiceProvider.GeocodingFeatures QGeoServiceProvider.GeocodingFeatures.__or__(QGeoServiceProvider.GeocodingFeatures f)'''
            return QGeoServiceProvider.GeocodingFeatures()
        def __or__(self, f):
            '''QGeoServiceProvider.GeocodingFeatures QGeoServiceProvider.GeocodingFeatures.__or__(int f)'''
            return QGeoServiceProvider.GeocodingFeatures()
        def __int__(self):
            '''int QGeoServiceProvider.GeocodingFeatures.__int__()'''
            return int()
        def __ixor__(self, f):
            '''QGeoServiceProvider.GeocodingFeatures QGeoServiceProvider.GeocodingFeatures.__ixor__(QGeoServiceProvider.GeocodingFeatures f)'''
            return QGeoServiceProvider.GeocodingFeatures()
        def __ior__(self, f):
            '''QGeoServiceProvider.GeocodingFeatures QGeoServiceProvider.GeocodingFeatures.__ior__(QGeoServiceProvider.GeocodingFeatures f)'''
            return QGeoServiceProvider.GeocodingFeatures()
        def __iand__(self, mask):
            '''QGeoServiceProvider.GeocodingFeatures QGeoServiceProvider.GeocodingFeatures.__iand__(int mask)'''
            return QGeoServiceProvider.GeocodingFeatures()
    class RoutingFeatures():
        """"""
        def __init__(self):
            '''QGeoServiceProvider.RoutingFeatures QGeoServiceProvider.RoutingFeatures.__init__()'''
            return QGeoServiceProvider.RoutingFeatures()
        def __init__(self):
            '''int QGeoServiceProvider.RoutingFeatures.__init__()'''
            return int()
        def __init__(self):
            '''void QGeoServiceProvider.RoutingFeatures.__init__()'''
        def __bool__(self):
            '''int QGeoServiceProvider.RoutingFeatures.__bool__()'''
            return int()
        def __ne__(self, f):
            '''bool QGeoServiceProvider.RoutingFeatures.__ne__(QGeoServiceProvider.RoutingFeatures f)'''
            return bool()
        def __eq__(self, f):
            '''bool QGeoServiceProvider.RoutingFeatures.__eq__(QGeoServiceProvider.RoutingFeatures f)'''
            return bool()
        def __invert__(self):
            '''QGeoServiceProvider.RoutingFeatures QGeoServiceProvider.RoutingFeatures.__invert__()'''
            return QGeoServiceProvider.RoutingFeatures()
        def __and__(self, mask):
            '''QGeoServiceProvider.RoutingFeatures QGeoServiceProvider.RoutingFeatures.__and__(int mask)'''
            return QGeoServiceProvider.RoutingFeatures()
        def __xor__(self, f):
            '''QGeoServiceProvider.RoutingFeatures QGeoServiceProvider.RoutingFeatures.__xor__(QGeoServiceProvider.RoutingFeatures f)'''
            return QGeoServiceProvider.RoutingFeatures()
        def __xor__(self, f):
            '''QGeoServiceProvider.RoutingFeatures QGeoServiceProvider.RoutingFeatures.__xor__(int f)'''
            return QGeoServiceProvider.RoutingFeatures()
        def __or__(self, f):
            '''QGeoServiceProvider.RoutingFeatures QGeoServiceProvider.RoutingFeatures.__or__(QGeoServiceProvider.RoutingFeatures f)'''
            return QGeoServiceProvider.RoutingFeatures()
        def __or__(self, f):
            '''QGeoServiceProvider.RoutingFeatures QGeoServiceProvider.RoutingFeatures.__or__(int f)'''
            return QGeoServiceProvider.RoutingFeatures()
        def __int__(self):
            '''int QGeoServiceProvider.RoutingFeatures.__int__()'''
            return int()
        def __ixor__(self, f):
            '''QGeoServiceProvider.RoutingFeatures QGeoServiceProvider.RoutingFeatures.__ixor__(QGeoServiceProvider.RoutingFeatures f)'''
            return QGeoServiceProvider.RoutingFeatures()
        def __ior__(self, f):
            '''QGeoServiceProvider.RoutingFeatures QGeoServiceProvider.RoutingFeatures.__ior__(QGeoServiceProvider.RoutingFeatures f)'''
            return QGeoServiceProvider.RoutingFeatures()
        def __iand__(self, mask):
            '''QGeoServiceProvider.RoutingFeatures QGeoServiceProvider.RoutingFeatures.__iand__(int mask)'''
            return QGeoServiceProvider.RoutingFeatures()
    class MappingFeatures():
        """"""
        def __init__(self):
            '''QGeoServiceProvider.MappingFeatures QGeoServiceProvider.MappingFeatures.__init__()'''
            return QGeoServiceProvider.MappingFeatures()
        def __init__(self):
            '''int QGeoServiceProvider.MappingFeatures.__init__()'''
            return int()
        def __init__(self):
            '''void QGeoServiceProvider.MappingFeatures.__init__()'''
        def __bool__(self):
            '''int QGeoServiceProvider.MappingFeatures.__bool__()'''
            return int()
        def __ne__(self, f):
            '''bool QGeoServiceProvider.MappingFeatures.__ne__(QGeoServiceProvider.MappingFeatures f)'''
            return bool()
        def __eq__(self, f):
            '''bool QGeoServiceProvider.MappingFeatures.__eq__(QGeoServiceProvider.MappingFeatures f)'''
            return bool()
        def __invert__(self):
            '''QGeoServiceProvider.MappingFeatures QGeoServiceProvider.MappingFeatures.__invert__()'''
            return QGeoServiceProvider.MappingFeatures()
        def __and__(self, mask):
            '''QGeoServiceProvider.MappingFeatures QGeoServiceProvider.MappingFeatures.__and__(int mask)'''
            return QGeoServiceProvider.MappingFeatures()
        def __xor__(self, f):
            '''QGeoServiceProvider.MappingFeatures QGeoServiceProvider.MappingFeatures.__xor__(QGeoServiceProvider.MappingFeatures f)'''
            return QGeoServiceProvider.MappingFeatures()
        def __xor__(self, f):
            '''QGeoServiceProvider.MappingFeatures QGeoServiceProvider.MappingFeatures.__xor__(int f)'''
            return QGeoServiceProvider.MappingFeatures()
        def __or__(self, f):
            '''QGeoServiceProvider.MappingFeatures QGeoServiceProvider.MappingFeatures.__or__(QGeoServiceProvider.MappingFeatures f)'''
            return QGeoServiceProvider.MappingFeatures()
        def __or__(self, f):
            '''QGeoServiceProvider.MappingFeatures QGeoServiceProvider.MappingFeatures.__or__(int f)'''
            return QGeoServiceProvider.MappingFeatures()
        def __int__(self):
            '''int QGeoServiceProvider.MappingFeatures.__int__()'''
            return int()
        def __ixor__(self, f):
            '''QGeoServiceProvider.MappingFeatures QGeoServiceProvider.MappingFeatures.__ixor__(QGeoServiceProvider.MappingFeatures f)'''
            return QGeoServiceProvider.MappingFeatures()
        def __ior__(self, f):
            '''QGeoServiceProvider.MappingFeatures QGeoServiceProvider.MappingFeatures.__ior__(QGeoServiceProvider.MappingFeatures f)'''
            return QGeoServiceProvider.MappingFeatures()
        def __iand__(self, mask):
            '''QGeoServiceProvider.MappingFeatures QGeoServiceProvider.MappingFeatures.__iand__(int mask)'''
            return QGeoServiceProvider.MappingFeatures()
    class PlacesFeatures():
        """"""
        def __init__(self):
            '''QGeoServiceProvider.PlacesFeatures QGeoServiceProvider.PlacesFeatures.__init__()'''
            return QGeoServiceProvider.PlacesFeatures()
        def __init__(self):
            '''int QGeoServiceProvider.PlacesFeatures.__init__()'''
            return int()
        def __init__(self):
            '''void QGeoServiceProvider.PlacesFeatures.__init__()'''
        def __bool__(self):
            '''int QGeoServiceProvider.PlacesFeatures.__bool__()'''
            return int()
        def __ne__(self, f):
            '''bool QGeoServiceProvider.PlacesFeatures.__ne__(QGeoServiceProvider.PlacesFeatures f)'''
            return bool()
        def __eq__(self, f):
            '''bool QGeoServiceProvider.PlacesFeatures.__eq__(QGeoServiceProvider.PlacesFeatures f)'''
            return bool()
        def __invert__(self):
            '''QGeoServiceProvider.PlacesFeatures QGeoServiceProvider.PlacesFeatures.__invert__()'''
            return QGeoServiceProvider.PlacesFeatures()
        def __and__(self, mask):
            '''QGeoServiceProvider.PlacesFeatures QGeoServiceProvider.PlacesFeatures.__and__(int mask)'''
            return QGeoServiceProvider.PlacesFeatures()
        def __xor__(self, f):
            '''QGeoServiceProvider.PlacesFeatures QGeoServiceProvider.PlacesFeatures.__xor__(QGeoServiceProvider.PlacesFeatures f)'''
            return QGeoServiceProvider.PlacesFeatures()
        def __xor__(self, f):
            '''QGeoServiceProvider.PlacesFeatures QGeoServiceProvider.PlacesFeatures.__xor__(int f)'''
            return QGeoServiceProvider.PlacesFeatures()
        def __or__(self, f):
            '''QGeoServiceProvider.PlacesFeatures QGeoServiceProvider.PlacesFeatures.__or__(QGeoServiceProvider.PlacesFeatures f)'''
            return QGeoServiceProvider.PlacesFeatures()
        def __or__(self, f):
            '''QGeoServiceProvider.PlacesFeatures QGeoServiceProvider.PlacesFeatures.__or__(int f)'''
            return QGeoServiceProvider.PlacesFeatures()
        def __int__(self):
            '''int QGeoServiceProvider.PlacesFeatures.__int__()'''
            return int()
        def __ixor__(self, f):
            '''QGeoServiceProvider.PlacesFeatures QGeoServiceProvider.PlacesFeatures.__ixor__(QGeoServiceProvider.PlacesFeatures f)'''
            return QGeoServiceProvider.PlacesFeatures()
        def __ior__(self, f):
            '''QGeoServiceProvider.PlacesFeatures QGeoServiceProvider.PlacesFeatures.__ior__(QGeoServiceProvider.PlacesFeatures f)'''
            return QGeoServiceProvider.PlacesFeatures()
        def __iand__(self, mask):
            '''QGeoServiceProvider.PlacesFeatures QGeoServiceProvider.PlacesFeatures.__iand__(int mask)'''
            return QGeoServiceProvider.PlacesFeatures()


class QLocation():
    """"""
    # Enum QLocation.Visibility
    UnspecifiedVisibility = 0
    DeviceVisibility = 0
    PrivateVisibility = 0
    PublicVisibility = 0

    class VisibilityScope():
        """"""
        def __init__(self):
            '''QLocation.VisibilityScope QLocation.VisibilityScope.__init__()'''
            return QLocation.VisibilityScope()
        def __init__(self):
            '''int QLocation.VisibilityScope.__init__()'''
            return int()
        def __init__(self):
            '''void QLocation.VisibilityScope.__init__()'''
        def __bool__(self):
            '''int QLocation.VisibilityScope.__bool__()'''
            return int()
        def __ne__(self, f):
            '''bool QLocation.VisibilityScope.__ne__(QLocation.VisibilityScope f)'''
            return bool()
        def __eq__(self, f):
            '''bool QLocation.VisibilityScope.__eq__(QLocation.VisibilityScope f)'''
            return bool()
        def __invert__(self):
            '''QLocation.VisibilityScope QLocation.VisibilityScope.__invert__()'''
            return QLocation.VisibilityScope()
        def __and__(self, mask):
            '''QLocation.VisibilityScope QLocation.VisibilityScope.__and__(int mask)'''
            return QLocation.VisibilityScope()
        def __xor__(self, f):
            '''QLocation.VisibilityScope QLocation.VisibilityScope.__xor__(QLocation.VisibilityScope f)'''
            return QLocation.VisibilityScope()
        def __xor__(self, f):
            '''QLocation.VisibilityScope QLocation.VisibilityScope.__xor__(int f)'''
            return QLocation.VisibilityScope()
        def __or__(self, f):
            '''QLocation.VisibilityScope QLocation.VisibilityScope.__or__(QLocation.VisibilityScope f)'''
            return QLocation.VisibilityScope()
        def __or__(self, f):
            '''QLocation.VisibilityScope QLocation.VisibilityScope.__or__(int f)'''
            return QLocation.VisibilityScope()
        def __int__(self):
            '''int QLocation.VisibilityScope.__int__()'''
            return int()
        def __ixor__(self, f):
            '''QLocation.VisibilityScope QLocation.VisibilityScope.__ixor__(QLocation.VisibilityScope f)'''
            return QLocation.VisibilityScope()
        def __ior__(self, f):
            '''QLocation.VisibilityScope QLocation.VisibilityScope.__ior__(QLocation.VisibilityScope f)'''
            return QLocation.VisibilityScope()
        def __iand__(self, mask):
            '''QLocation.VisibilityScope QLocation.VisibilityScope.__iand__(int mask)'''
            return QLocation.VisibilityScope()


class QPlace():
    """"""
    def __init__(self):
        '''void QPlace.__init__()'''
    def __init__(self, other):
        '''void QPlace.__init__(QPlace other)'''
    def isEmpty(self):
        '''bool QPlace.isEmpty()'''
        return bool()
    def setVisibility(self, visibility):
        '''void QPlace.setVisibility(QLocation.Visibility visibility)'''
    def visibility(self):
        '''QLocation.Visibility QPlace.visibility()'''
        return QLocation.Visibility()
    def removeContactDetails(self, contactType):
        '''void QPlace.removeContactDetails(str contactType)'''
    def appendContactDetail(self, contactType, detail):
        '''void QPlace.appendContactDetail(str contactType, QPlaceContactDetail detail)'''
    def setContactDetails(self, contactType, details):
        '''void QPlace.setContactDetails(str contactType, list-of-QPlaceContactDetail details)'''
    def contactDetails(self, contactType):
        '''list-of-QPlaceContactDetail QPlace.contactDetails(str contactType)'''
        return [QPlaceContactDetail()]
    def contactTypes(self):
        '''list-of-str QPlace.contactTypes()'''
        return [str()]
    def removeExtendedAttribute(self, attributeType):
        '''void QPlace.removeExtendedAttribute(str attributeType)'''
    def setExtendedAttribute(self, attributeType, attribute):
        '''void QPlace.setExtendedAttribute(str attributeType, QPlaceAttribute attribute)'''
    def extendedAttribute(self, attributeType):
        '''QPlaceAttribute QPlace.extendedAttribute(str attributeType)'''
        return QPlaceAttribute()
    def extendedAttributeTypes(self):
        '''list-of-str QPlace.extendedAttributeTypes()'''
        return [str()]
    def setDetailsFetched(self, fetched):
        '''void QPlace.setDetailsFetched(bool fetched)'''
    def detailsFetched(self):
        '''bool QPlace.detailsFetched()'''
        return bool()
    def primaryWebsite(self):
        '''QUrl QPlace.primaryWebsite()'''
        return QUrl()
    def primaryEmail(self):
        '''str QPlace.primaryEmail()'''
        return str()
    def primaryFax(self):
        '''str QPlace.primaryFax()'''
        return str()
    def primaryPhone(self):
        '''str QPlace.primaryPhone()'''
        return str()
    def setPlaceId(self, identifier):
        '''void QPlace.setPlaceId(str identifier)'''
    def placeId(self):
        '''str QPlace.placeId()'''
        return str()
    def setName(self, name):
        '''void QPlace.setName(str name)'''
    def name(self):
        '''str QPlace.name()'''
        return str()
    def setTotalContentCount(self, type, total):
        '''void QPlace.setTotalContentCount(QPlaceContent.Type type, int total)'''
    def totalContentCount(self, type):
        '''int QPlace.totalContentCount(QPlaceContent.Type type)'''
        return int()
    def insertContent(self, type, content):
        '''void QPlace.insertContent(QPlaceContent.Type type, dict-of-int-QPlaceContent content)'''
    def setContent(self, type, content):
        '''void QPlace.setContent(QPlaceContent.Type type, dict-of-int-QPlaceContent content)'''
    def content(self, type):
        '''dict-of-int-QPlaceContent QPlace.content(QPlaceContent.Type type)'''
        return {int():QPlaceContent()}
    def setIcon(self, icon):
        '''void QPlace.setIcon(QPlaceIcon icon)'''
    def icon(self):
        '''QPlaceIcon QPlace.icon()'''
        return QPlaceIcon()
    def setAttribution(self, attribution):
        '''void QPlace.setAttribution(str attribution)'''
    def attribution(self):
        '''str QPlace.attribution()'''
        return str()
    def setSupplier(self, supplier):
        '''void QPlace.setSupplier(QPlaceSupplier supplier)'''
    def supplier(self):
        '''QPlaceSupplier QPlace.supplier()'''
        return QPlaceSupplier()
    def setRatings(self, ratings):
        '''void QPlace.setRatings(QPlaceRatings ratings)'''
    def ratings(self):
        '''QPlaceRatings QPlace.ratings()'''
        return QPlaceRatings()
    def setLocation(self, location):
        '''void QPlace.setLocation(QGeoLocation location)'''
    def location(self):
        '''QGeoLocation QPlace.location()'''
        return QGeoLocation()
    def setCategories(self, categories):
        '''void QPlace.setCategories(list-of-QPlaceCategory categories)'''
    def setCategory(self, category):
        '''void QPlace.setCategory(QPlaceCategory category)'''
    def categories(self):
        '''list-of-QPlaceCategory QPlace.categories()'''
        return [QPlaceCategory()]
    def __ne__(self, other):
        '''bool QPlace.__ne__(QPlace other)'''
        return bool()
    def __eq__(self, other):
        '''bool QPlace.__eq__(QPlace other)'''
        return bool()


class QPlaceAttribute():
    """"""
    OpeningHours = None # str - member
    Payment = None # str - member
    Provider = None # str - member
    def __init__(self):
        '''void QPlaceAttribute.__init__()'''
    def __init__(self, other):
        '''void QPlaceAttribute.__init__(QPlaceAttribute other)'''
    def isEmpty(self):
        '''bool QPlaceAttribute.isEmpty()'''
        return bool()
    def setText(self, text):
        '''void QPlaceAttribute.setText(str text)'''
    def text(self):
        '''str QPlaceAttribute.text()'''
        return str()
    def setLabel(self, label):
        '''void QPlaceAttribute.setLabel(str label)'''
    def label(self):
        '''str QPlaceAttribute.label()'''
        return str()
    def __ne__(self, other):
        '''bool QPlaceAttribute.__ne__(QPlaceAttribute other)'''
        return bool()
    def __eq__(self, other):
        '''bool QPlaceAttribute.__eq__(QPlaceAttribute other)'''
        return bool()


class QPlaceCategory():
    """"""
    def __init__(self):
        '''void QPlaceCategory.__init__()'''
    def __init__(self, other):
        '''void QPlaceCategory.__init__(QPlaceCategory other)'''
    def isEmpty(self):
        '''bool QPlaceCategory.isEmpty()'''
        return bool()
    def setIcon(self, icon):
        '''void QPlaceCategory.setIcon(QPlaceIcon icon)'''
    def icon(self):
        '''QPlaceIcon QPlaceCategory.icon()'''
        return QPlaceIcon()
    def setVisibility(self, visibility):
        '''void QPlaceCategory.setVisibility(QLocation.Visibility visibility)'''
    def visibility(self):
        '''QLocation.Visibility QPlaceCategory.visibility()'''
        return QLocation.Visibility()
    def setName(self, name):
        '''void QPlaceCategory.setName(str name)'''
    def name(self):
        '''str QPlaceCategory.name()'''
        return str()
    def setCategoryId(self, identifier):
        '''void QPlaceCategory.setCategoryId(str identifier)'''
    def categoryId(self):
        '''str QPlaceCategory.categoryId()'''
        return str()
    def __ne__(self, other):
        '''bool QPlaceCategory.__ne__(QPlaceCategory other)'''
        return bool()
    def __eq__(self, other):
        '''bool QPlaceCategory.__eq__(QPlaceCategory other)'''
        return bool()


class QPlaceContactDetail():
    """"""
    Email = None # str - member
    Fax = None # str - member
    Phone = None # str - member
    Website = None # str - member
    def __init__(self):
        '''void QPlaceContactDetail.__init__()'''
    def __init__(self, other):
        '''void QPlaceContactDetail.__init__(QPlaceContactDetail other)'''
    def clear(self):
        '''void QPlaceContactDetail.clear()'''
    def setValue(self, value):
        '''void QPlaceContactDetail.setValue(str value)'''
    def value(self):
        '''str QPlaceContactDetail.value()'''
        return str()
    def setLabel(self, label):
        '''void QPlaceContactDetail.setLabel(str label)'''
    def label(self):
        '''str QPlaceContactDetail.label()'''
        return str()
    def __ne__(self, other):
        '''bool QPlaceContactDetail.__ne__(QPlaceContactDetail other)'''
        return bool()
    def __eq__(self, other):
        '''bool QPlaceContactDetail.__eq__(QPlaceContactDetail other)'''
        return bool()


class QPlaceContent():
    """"""
    # Enum QPlaceContent.Type
    NoType = 0
    ImageType = 0
    ReviewType = 0
    EditorialType = 0

    def __init__(self):
        '''void QPlaceContent.__init__()'''
    def __init__(self, other):
        '''void QPlaceContent.__init__(QPlaceContent other)'''
    def setAttribution(self, attribution):
        '''void QPlaceContent.setAttribution(str attribution)'''
    def attribution(self):
        '''str QPlaceContent.attribution()'''
        return str()
    def setUser(self, user):
        '''void QPlaceContent.setUser(QPlaceUser user)'''
    def user(self):
        '''QPlaceUser QPlaceContent.user()'''
        return QPlaceUser()
    def setSupplier(self, supplier):
        '''void QPlaceContent.setSupplier(QPlaceSupplier supplier)'''
    def supplier(self):
        '''QPlaceSupplier QPlaceContent.supplier()'''
        return QPlaceSupplier()
    def type(self):
        '''QPlaceContent.Type QPlaceContent.type()'''
        return QPlaceContent.Type()
    def __ne__(self, other):
        '''bool QPlaceContent.__ne__(QPlaceContent other)'''
        return bool()
    def __eq__(self, other):
        '''bool QPlaceContent.__eq__(QPlaceContent other)'''
        return bool()


class QPlaceReply(QObject):
    """"""
    # Enum QPlaceReply.Type
    Reply = 0
    DetailsReply = 0
    SearchReply = 0
    SearchSuggestionReply = 0
    ContentReply = 0
    IdReply = 0
    MatchReply = 0

    # Enum QPlaceReply.Error
    NoError = 0
    PlaceDoesNotExistError = 0
    CategoryDoesNotExistError = 0
    CommunicationError = 0
    ParseError = 0
    PermissionsError = 0
    UnsupportedError = 0
    BadArgumentError = 0
    CancelError = 0
    UnknownError = 0

    def __init__(self, parent = None):
        '''void QPlaceReply.__init__(QObject parent = None)'''
    def setError(self, error, errorString):
        '''void QPlaceReply.setError(QPlaceReply.Error error, str errorString)'''
    def setFinished(self, finished):
        '''void QPlaceReply.setFinished(bool finished)'''
    finished = pyqtSignal() # void finished() - signal
    def abort(self):
        '''void QPlaceReply.abort()'''
    def error(self):
        '''QPlaceReply.Error QPlaceReply.error()'''
        return QPlaceReply.Error()
    error = pyqtSignal() # void error(QPlaceReply::Error,const QStringamp; = QString()) - signal
    def errorString(self):
        '''str QPlaceReply.errorString()'''
        return str()
    def type(self):
        '''QPlaceReply.Type QPlaceReply.type()'''
        return QPlaceReply.Type()
    def isFinished(self):
        '''bool QPlaceReply.isFinished()'''
        return bool()


class QPlaceContentReply(QPlaceReply):
    """"""
    def __init__(self, parent = None):
        '''void QPlaceContentReply.__init__(QObject parent = None)'''
    def setNextPageRequest(self, next):
        '''void QPlaceContentReply.setNextPageRequest(QPlaceContentRequest next)'''
    def setPreviousPageRequest(self, previous):
        '''void QPlaceContentReply.setPreviousPageRequest(QPlaceContentRequest previous)'''
    def setRequest(self, request):
        '''void QPlaceContentReply.setRequest(QPlaceContentRequest request)'''
    def setTotalCount(self, total):
        '''void QPlaceContentReply.setTotalCount(int total)'''
    def setContent(self, content):
        '''void QPlaceContentReply.setContent(dict-of-int-QPlaceContent content)'''
    def nextPageRequest(self):
        '''QPlaceContentRequest QPlaceContentReply.nextPageRequest()'''
        return QPlaceContentRequest()
    def previousPageRequest(self):
        '''QPlaceContentRequest QPlaceContentReply.previousPageRequest()'''
        return QPlaceContentRequest()
    def request(self):
        '''QPlaceContentRequest QPlaceContentReply.request()'''
        return QPlaceContentRequest()
    def totalCount(self):
        '''int QPlaceContentReply.totalCount()'''
        return int()
    def content(self):
        '''dict-of-int-QPlaceContent QPlaceContentReply.content()'''
        return {int():QPlaceContent()}
    def type(self):
        '''QPlaceReply.Type QPlaceContentReply.type()'''
        return QPlaceReply.Type()


class QPlaceContentRequest():
    """"""
    def __init__(self):
        '''void QPlaceContentRequest.__init__()'''
    def __init__(self, other):
        '''void QPlaceContentRequest.__init__(QPlaceContentRequest other)'''
    def clear(self):
        '''void QPlaceContentRequest.clear()'''
    def setLimit(self, limit):
        '''void QPlaceContentRequest.setLimit(int limit)'''
    def limit(self):
        '''int QPlaceContentRequest.limit()'''
        return int()
    def setContentContext(self, context):
        '''void QPlaceContentRequest.setContentContext(QVariant context)'''
    def contentContext(self):
        '''QVariant QPlaceContentRequest.contentContext()'''
        return QVariant()
    def setPlaceId(self, identifier):
        '''void QPlaceContentRequest.setPlaceId(str identifier)'''
    def placeId(self):
        '''str QPlaceContentRequest.placeId()'''
        return str()
    def setContentType(self, type):
        '''void QPlaceContentRequest.setContentType(QPlaceContent.Type type)'''
    def contentType(self):
        '''QPlaceContent.Type QPlaceContentRequest.contentType()'''
        return QPlaceContent.Type()
    def __ne__(self, other):
        '''bool QPlaceContentRequest.__ne__(QPlaceContentRequest other)'''
        return bool()
    def __eq__(self, other):
        '''bool QPlaceContentRequest.__eq__(QPlaceContentRequest other)'''
        return bool()


class QPlaceDetailsReply(QPlaceReply):
    """"""
    def __init__(self, parent = None):
        '''void QPlaceDetailsReply.__init__(QObject parent = None)'''
    def setPlace(self, place):
        '''void QPlaceDetailsReply.setPlace(QPlace place)'''
    def place(self):
        '''QPlace QPlaceDetailsReply.place()'''
        return QPlace()
    def type(self):
        '''QPlaceReply.Type QPlaceDetailsReply.type()'''
        return QPlaceReply.Type()


class QPlaceEditorial(QPlaceContent):
    """"""
    def __init__(self):
        '''void QPlaceEditorial.__init__()'''
    def __init__(self, other):
        '''void QPlaceEditorial.__init__(QPlaceContent other)'''
    def __init__(self):
        '''QPlaceEditorial QPlaceEditorial.__init__()'''
        return QPlaceEditorial()
    def setLanguage(self, data):
        '''void QPlaceEditorial.setLanguage(str data)'''
    def language(self):
        '''str QPlaceEditorial.language()'''
        return str()
    def setTitle(self, data):
        '''void QPlaceEditorial.setTitle(str data)'''
    def title(self):
        '''str QPlaceEditorial.title()'''
        return str()
    def setText(self, text):
        '''void QPlaceEditorial.setText(str text)'''
    def text(self):
        '''str QPlaceEditorial.text()'''
        return str()


class QPlaceIcon():
    """"""
    SingleUrl = None # str - member
    def __init__(self):
        '''void QPlaceIcon.__init__()'''
    def __init__(self, other):
        '''void QPlaceIcon.__init__(QPlaceIcon other)'''
    def isEmpty(self):
        '''bool QPlaceIcon.isEmpty()'''
        return bool()
    def setParameters(self, parameters):
        '''void QPlaceIcon.setParameters(dict-of-str-object parameters)'''
    def parameters(self):
        '''dict-of-str-object QPlaceIcon.parameters()'''
        return {str():object()}
    def setManager(self, manager):
        '''void QPlaceIcon.setManager(QPlaceManager manager)'''
    def manager(self):
        '''QPlaceManager QPlaceIcon.manager()'''
        return QPlaceManager()
    def url(self, size = QSize()):
        '''QUrl QPlaceIcon.url(QSize size = QSize())'''
        return QUrl()
    def __ne__(self, other):
        '''bool QPlaceIcon.__ne__(QPlaceIcon other)'''
        return bool()
    def __eq__(self, other):
        '''bool QPlaceIcon.__eq__(QPlaceIcon other)'''
        return bool()


class QPlaceIdReply(QPlaceReply):
    """"""
    # Enum QPlaceIdReply.OperationType
    SavePlace = 0
    SaveCategory = 0
    RemovePlace = 0
    RemoveCategory = 0

    def __init__(self, operationType, parent = None):
        '''void QPlaceIdReply.__init__(QPlaceIdReply.OperationType operationType, QObject parent = None)'''
    def setId(self, identifier):
        '''void QPlaceIdReply.setId(str identifier)'''
    def id(self):
        '''str QPlaceIdReply.id()'''
        return str()
    def operationType(self):
        '''QPlaceIdReply.OperationType QPlaceIdReply.operationType()'''
        return QPlaceIdReply.OperationType()
    def type(self):
        '''QPlaceReply.Type QPlaceIdReply.type()'''
        return QPlaceReply.Type()


class QPlaceImage(QPlaceContent):
    """"""
    def __init__(self):
        '''void QPlaceImage.__init__()'''
    def __init__(self, other):
        '''void QPlaceImage.__init__(QPlaceContent other)'''
    def __init__(self):
        '''QPlaceImage QPlaceImage.__init__()'''
        return QPlaceImage()
    def setMimeType(self, data):
        '''void QPlaceImage.setMimeType(str data)'''
    def mimeType(self):
        '''str QPlaceImage.mimeType()'''
        return str()
    def setImageId(self, identifier):
        '''void QPlaceImage.setImageId(str identifier)'''
    def imageId(self):
        '''str QPlaceImage.imageId()'''
        return str()
    def setUrl(self, url):
        '''void QPlaceImage.setUrl(QUrl url)'''
    def url(self):
        '''QUrl QPlaceImage.url()'''
        return QUrl()


class QPlaceManager(QObject):
    """"""
    dataChanged = pyqtSignal() # void dataChanged() - signal
    categoryRemoved = pyqtSignal() # void categoryRemoved(const QStringamp;,const QStringamp;) - signal
    categoryUpdated = pyqtSignal() # void categoryUpdated(const QPlaceCategoryamp;,const QStringamp;) - signal
    categoryAdded = pyqtSignal() # void categoryAdded(const QPlaceCategoryamp;,const QStringamp;) - signal
    placeRemoved = pyqtSignal() # void placeRemoved(const QStringamp;) - signal
    placeUpdated = pyqtSignal() # void placeUpdated(const QStringamp;) - signal
    placeAdded = pyqtSignal() # void placeAdded(const QStringamp;) - signal
    error = pyqtSignal() # void error(QPlaceReply*,QPlaceReply::Error,const QStringamp; = QString()) - signal
    finished = pyqtSignal() # void finished(QPlaceReply*) - signal
    def matchingPlaces(self, request):
        '''QPlaceMatchReply QPlaceManager.matchingPlaces(QPlaceMatchRequest request)'''
        return QPlaceMatchReply()
    def compatiblePlace(self, place):
        '''QPlace QPlaceManager.compatiblePlace(QPlace place)'''
        return QPlace()
    def setLocales(self, locale):
        '''void QPlaceManager.setLocales(list-of-QLocale locale)'''
    def setLocale(self, locale):
        '''void QPlaceManager.setLocale(QLocale locale)'''
    def locales(self):
        '''list-of-QLocale QPlaceManager.locales()'''
        return [QLocale()]
    def childCategories(self, parentId = str()):
        '''list-of-QPlaceCategory QPlaceManager.childCategories(str parentId = str())'''
        return [QPlaceCategory()]
    def category(self, categoryId):
        '''QPlaceCategory QPlaceManager.category(str categoryId)'''
        return QPlaceCategory()
    def childCategoryIds(self, parentId = str()):
        '''list-of-str QPlaceManager.childCategoryIds(str parentId = str())'''
        return [str()]
    def parentCategoryId(self, categoryId):
        '''str QPlaceManager.parentCategoryId(str categoryId)'''
        return str()
    def initializeCategories(self):
        '''QPlaceReply QPlaceManager.initializeCategories()'''
        return QPlaceReply()
    def removeCategory(self, categoryId):
        '''QPlaceIdReply QPlaceManager.removeCategory(str categoryId)'''
        return QPlaceIdReply()
    def saveCategory(self, category, parentId = str()):
        '''QPlaceIdReply QPlaceManager.saveCategory(QPlaceCategory category, str parentId = str())'''
        return QPlaceIdReply()
    def removePlace(self, placeId):
        '''QPlaceIdReply QPlaceManager.removePlace(str placeId)'''
        return QPlaceIdReply()
    def savePlace(self, place):
        '''QPlaceIdReply QPlaceManager.savePlace(QPlace place)'''
        return QPlaceIdReply()
    def searchSuggestions(self, request):
        '''QPlaceSearchSuggestionReply QPlaceManager.searchSuggestions(QPlaceSearchRequest request)'''
        return QPlaceSearchSuggestionReply()
    def search(self, query):
        '''QPlaceSearchReply QPlaceManager.search(QPlaceSearchRequest query)'''
        return QPlaceSearchReply()
    def getPlaceContent(self, request):
        '''QPlaceContentReply QPlaceManager.getPlaceContent(QPlaceContentRequest request)'''
        return QPlaceContentReply()
    def getPlaceDetails(self, placeId):
        '''QPlaceDetailsReply QPlaceManager.getPlaceDetails(str placeId)'''
        return QPlaceDetailsReply()
    def managerVersion(self):
        '''int QPlaceManager.managerVersion()'''
        return int()
    def managerName(self):
        '''str QPlaceManager.managerName()'''
        return str()


class QPlaceManagerEngine(QObject):
    """"""
    def __init__(self, parameters, parent = None):
        '''void QPlaceManagerEngine.__init__(dict-of-str-object parameters, QObject parent = None)'''
    def manager(self):
        '''QPlaceManager QPlaceManagerEngine.manager()'''
        return QPlaceManager()
    dataChanged = pyqtSignal() # void dataChanged() - signal
    categoryRemoved = pyqtSignal() # void categoryRemoved(const QStringamp;,const QStringamp;) - signal
    categoryUpdated = pyqtSignal() # void categoryUpdated(const QPlaceCategoryamp;,const QStringamp;) - signal
    categoryAdded = pyqtSignal() # void categoryAdded(const QPlaceCategoryamp;,const QStringamp;) - signal
    placeRemoved = pyqtSignal() # void placeRemoved(const QStringamp;) - signal
    placeUpdated = pyqtSignal() # void placeUpdated(const QStringamp;) - signal
    placeAdded = pyqtSignal() # void placeAdded(const QStringamp;) - signal
    error = pyqtSignal() # void error(QPlaceReply*,QPlaceReply::Error,const QStringamp; = QString()) - signal
    finished = pyqtSignal() # void finished(QPlaceReply*) - signal
    def matchingPlaces(self, request):
        '''QPlaceMatchReply QPlaceManagerEngine.matchingPlaces(QPlaceMatchRequest request)'''
        return QPlaceMatchReply()
    def compatiblePlace(self, original):
        '''QPlace QPlaceManagerEngine.compatiblePlace(QPlace original)'''
        return QPlace()
    def constructIconUrl(self, icon, size):
        '''QUrl QPlaceManagerEngine.constructIconUrl(QPlaceIcon icon, QSize size)'''
        return QUrl()
    def setLocales(self, locales):
        '''void QPlaceManagerEngine.setLocales(list-of-QLocale locales)'''
    def locales(self):
        '''list-of-QLocale QPlaceManagerEngine.locales()'''
        return [QLocale()]
    def childCategories(self, parentId):
        '''list-of-QPlaceCategory QPlaceManagerEngine.childCategories(str parentId)'''
        return [QPlaceCategory()]
    def category(self, categoryId):
        '''QPlaceCategory QPlaceManagerEngine.category(str categoryId)'''
        return QPlaceCategory()
    def childCategoryIds(self, categoryId):
        '''list-of-str QPlaceManagerEngine.childCategoryIds(str categoryId)'''
        return [str()]
    def parentCategoryId(self, categoryId):
        '''str QPlaceManagerEngine.parentCategoryId(str categoryId)'''
        return str()
    def initializeCategories(self):
        '''QPlaceReply QPlaceManagerEngine.initializeCategories()'''
        return QPlaceReply()
    def removeCategory(self, categoryId):
        '''QPlaceIdReply QPlaceManagerEngine.removeCategory(str categoryId)'''
        return QPlaceIdReply()
    def saveCategory(self, category, parentId):
        '''QPlaceIdReply QPlaceManagerEngine.saveCategory(QPlaceCategory category, str parentId)'''
        return QPlaceIdReply()
    def removePlace(self, placeId):
        '''QPlaceIdReply QPlaceManagerEngine.removePlace(str placeId)'''
        return QPlaceIdReply()
    def savePlace(self, place):
        '''QPlaceIdReply QPlaceManagerEngine.savePlace(QPlace place)'''
        return QPlaceIdReply()
    def searchSuggestions(self, request):
        '''QPlaceSearchSuggestionReply QPlaceManagerEngine.searchSuggestions(QPlaceSearchRequest request)'''
        return QPlaceSearchSuggestionReply()
    def search(self, request):
        '''QPlaceSearchReply QPlaceManagerEngine.search(QPlaceSearchRequest request)'''
        return QPlaceSearchReply()
    def getPlaceContent(self, request):
        '''QPlaceContentReply QPlaceManagerEngine.getPlaceContent(QPlaceContentRequest request)'''
        return QPlaceContentReply()
    def getPlaceDetails(self, placeId):
        '''QPlaceDetailsReply QPlaceManagerEngine.getPlaceDetails(str placeId)'''
        return QPlaceDetailsReply()
    def managerVersion(self):
        '''int QPlaceManagerEngine.managerVersion()'''
        return int()
    def managerName(self):
        '''str QPlaceManagerEngine.managerName()'''
        return str()


class QPlaceMatchReply(QPlaceReply):
    """"""
    def __init__(self, parent = None):
        '''void QPlaceMatchReply.__init__(QObject parent = None)'''
    def setRequest(self, request):
        '''void QPlaceMatchReply.setRequest(QPlaceMatchRequest request)'''
    def setPlaces(self, results):
        '''void QPlaceMatchReply.setPlaces(list-of-QPlace results)'''
    def request(self):
        '''QPlaceMatchRequest QPlaceMatchReply.request()'''
        return QPlaceMatchRequest()
    def places(self):
        '''list-of-QPlace QPlaceMatchReply.places()'''
        return [QPlace()]
    def type(self):
        '''QPlaceReply.Type QPlaceMatchReply.type()'''
        return QPlaceReply.Type()


class QPlaceMatchRequest():
    """"""
    AlternativeId = None # str - member
    def __init__(self):
        '''void QPlaceMatchRequest.__init__()'''
    def __init__(self, other):
        '''void QPlaceMatchRequest.__init__(QPlaceMatchRequest other)'''
    def clear(self):
        '''void QPlaceMatchRequest.clear()'''
    def setParameters(self, parameters):
        '''void QPlaceMatchRequest.setParameters(dict-of-str-object parameters)'''
    def parameters(self):
        '''dict-of-str-object QPlaceMatchRequest.parameters()'''
        return {str():object()}
    def setResults(self, results):
        '''void QPlaceMatchRequest.setResults(list-of-QPlaceSearchResult results)'''
    def setPlaces(self, places):
        '''void QPlaceMatchRequest.setPlaces(list-of-QPlace places)'''
    def places(self):
        '''list-of-QPlace QPlaceMatchRequest.places()'''
        return [QPlace()]
    def __ne__(self, other):
        '''bool QPlaceMatchRequest.__ne__(QPlaceMatchRequest other)'''
        return bool()
    def __eq__(self, other):
        '''bool QPlaceMatchRequest.__eq__(QPlaceMatchRequest other)'''
        return bool()


class QPlaceSearchResult():
    """"""
    # Enum QPlaceSearchResult.SearchResultType
    UnknownSearchResult = 0
    PlaceResult = 0
    ProposedSearchResult = 0

    def __init__(self):
        '''void QPlaceSearchResult.__init__()'''
    def __init__(self, other):
        '''void QPlaceSearchResult.__init__(QPlaceSearchResult other)'''
    def setIcon(self, icon):
        '''void QPlaceSearchResult.setIcon(QPlaceIcon icon)'''
    def icon(self):
        '''QPlaceIcon QPlaceSearchResult.icon()'''
        return QPlaceIcon()
    def setTitle(self, title):
        '''void QPlaceSearchResult.setTitle(str title)'''
    def title(self):
        '''str QPlaceSearchResult.title()'''
        return str()
    def type(self):
        '''QPlaceSearchResult.SearchResultType QPlaceSearchResult.type()'''
        return QPlaceSearchResult.SearchResultType()
    def __ne__(self, other):
        '''bool QPlaceSearchResult.__ne__(QPlaceSearchResult other)'''
        return bool()
    def __eq__(self, other):
        '''bool QPlaceSearchResult.__eq__(QPlaceSearchResult other)'''
        return bool()


class QPlaceProposedSearchResult(QPlaceSearchResult):
    """"""
    def __init__(self):
        '''void QPlaceProposedSearchResult.__init__()'''
    def __init__(self, other):
        '''void QPlaceProposedSearchResult.__init__(QPlaceSearchResult other)'''
    def __init__(self):
        '''QPlaceProposedSearchResult QPlaceProposedSearchResult.__init__()'''
        return QPlaceProposedSearchResult()
    def setSearchRequest(self, request):
        '''void QPlaceProposedSearchResult.setSearchRequest(QPlaceSearchRequest request)'''
    def searchRequest(self):
        '''QPlaceSearchRequest QPlaceProposedSearchResult.searchRequest()'''
        return QPlaceSearchRequest()


class QPlaceRatings():
    """"""
    def __init__(self):
        '''void QPlaceRatings.__init__()'''
    def __init__(self, other):
        '''void QPlaceRatings.__init__(QPlaceRatings other)'''
    def isEmpty(self):
        '''bool QPlaceRatings.isEmpty()'''
        return bool()
    def setMaximum(self, max):
        '''void QPlaceRatings.setMaximum(float max)'''
    def maximum(self):
        '''float QPlaceRatings.maximum()'''
        return float()
    def setCount(self, count):
        '''void QPlaceRatings.setCount(int count)'''
    def count(self):
        '''int QPlaceRatings.count()'''
        return int()
    def setAverage(self, average):
        '''void QPlaceRatings.setAverage(float average)'''
    def average(self):
        '''float QPlaceRatings.average()'''
        return float()
    def __ne__(self, other):
        '''bool QPlaceRatings.__ne__(QPlaceRatings other)'''
        return bool()
    def __eq__(self, other):
        '''bool QPlaceRatings.__eq__(QPlaceRatings other)'''
        return bool()


class QPlaceResult(QPlaceSearchResult):
    """"""
    def __init__(self):
        '''void QPlaceResult.__init__()'''
    def __init__(self, other):
        '''void QPlaceResult.__init__(QPlaceSearchResult other)'''
    def __init__(self):
        '''QPlaceResult QPlaceResult.__init__()'''
        return QPlaceResult()
    def setSponsored(self, sponsored):
        '''void QPlaceResult.setSponsored(bool sponsored)'''
    def isSponsored(self):
        '''bool QPlaceResult.isSponsored()'''
        return bool()
    def setPlace(self, place):
        '''void QPlaceResult.setPlace(QPlace place)'''
    def place(self):
        '''QPlace QPlaceResult.place()'''
        return QPlace()
    def setDistance(self, distance):
        '''void QPlaceResult.setDistance(float distance)'''
    def distance(self):
        '''float QPlaceResult.distance()'''
        return float()


class QPlaceReview(QPlaceContent):
    """"""
    def __init__(self):
        '''void QPlaceReview.__init__()'''
    def __init__(self, other):
        '''void QPlaceReview.__init__(QPlaceContent other)'''
    def __init__(self):
        '''QPlaceReview QPlaceReview.__init__()'''
        return QPlaceReview()
    def setTitle(self, data):
        '''void QPlaceReview.setTitle(str data)'''
    def title(self):
        '''str QPlaceReview.title()'''
        return str()
    def setReviewId(self, identifier):
        '''void QPlaceReview.setReviewId(str identifier)'''
    def reviewId(self):
        '''str QPlaceReview.reviewId()'''
        return str()
    def setRating(self, data):
        '''void QPlaceReview.setRating(float data)'''
    def rating(self):
        '''float QPlaceReview.rating()'''
        return float()
    def setLanguage(self, data):
        '''void QPlaceReview.setLanguage(str data)'''
    def language(self):
        '''str QPlaceReview.language()'''
        return str()
    def setText(self, text):
        '''void QPlaceReview.setText(str text)'''
    def text(self):
        '''str QPlaceReview.text()'''
        return str()
    def setDateTime(self, dt):
        '''void QPlaceReview.setDateTime(QDateTime dt)'''
    def dateTime(self):
        '''QDateTime QPlaceReview.dateTime()'''
        return QDateTime()


class QPlaceSearchReply(QPlaceReply):
    """"""
    def __init__(self, parent = None):
        '''void QPlaceSearchReply.__init__(QObject parent = None)'''
    def setNextPageRequest(self, next):
        '''void QPlaceSearchReply.setNextPageRequest(QPlaceSearchRequest next)'''
    def setPreviousPageRequest(self, previous):
        '''void QPlaceSearchReply.setPreviousPageRequest(QPlaceSearchRequest previous)'''
    def setRequest(self, request):
        '''void QPlaceSearchReply.setRequest(QPlaceSearchRequest request)'''
    def setResults(self, results):
        '''void QPlaceSearchReply.setResults(list-of-QPlaceSearchResult results)'''
    def nextPageRequest(self):
        '''QPlaceSearchRequest QPlaceSearchReply.nextPageRequest()'''
        return QPlaceSearchRequest()
    def previousPageRequest(self):
        '''QPlaceSearchRequest QPlaceSearchReply.previousPageRequest()'''
        return QPlaceSearchRequest()
    def request(self):
        '''QPlaceSearchRequest QPlaceSearchReply.request()'''
        return QPlaceSearchRequest()
    def results(self):
        '''list-of-QPlaceSearchResult QPlaceSearchReply.results()'''
        return [QPlaceSearchResult()]
    def type(self):
        '''QPlaceReply.Type QPlaceSearchReply.type()'''
        return QPlaceReply.Type()


class QPlaceSearchRequest():
    """"""
    # Enum QPlaceSearchRequest.RelevanceHint
    UnspecifiedHint = 0
    DistanceHint = 0
    LexicalPlaceNameHint = 0

    def __init__(self):
        '''void QPlaceSearchRequest.__init__()'''
    def __init__(self, other):
        '''void QPlaceSearchRequest.__init__(QPlaceSearchRequest other)'''
    def clear(self):
        '''void QPlaceSearchRequest.clear()'''
    def setLimit(self, limit):
        '''void QPlaceSearchRequest.setLimit(int limit)'''
    def limit(self):
        '''int QPlaceSearchRequest.limit()'''
        return int()
    def setRelevanceHint(self, hint):
        '''void QPlaceSearchRequest.setRelevanceHint(QPlaceSearchRequest.RelevanceHint hint)'''
    def relevanceHint(self):
        '''QPlaceSearchRequest.RelevanceHint QPlaceSearchRequest.relevanceHint()'''
        return QPlaceSearchRequest.RelevanceHint()
    def setVisibilityScope(self, visibilityScopes):
        '''void QPlaceSearchRequest.setVisibilityScope(QLocation.VisibilityScope visibilityScopes)'''
    def visibilityScope(self):
        '''QLocation.VisibilityScope QPlaceSearchRequest.visibilityScope()'''
        return QLocation.VisibilityScope()
    def setSearchContext(self, context):
        '''void QPlaceSearchRequest.setSearchContext(QVariant context)'''
    def searchContext(self):
        '''QVariant QPlaceSearchRequest.searchContext()'''
        return QVariant()
    def setRecommendationId(self, recommendationId):
        '''void QPlaceSearchRequest.setRecommendationId(str recommendationId)'''
    def recommendationId(self):
        '''str QPlaceSearchRequest.recommendationId()'''
        return str()
    def setSearchArea(self, area):
        '''void QPlaceSearchRequest.setSearchArea(QGeoShape area)'''
    def searchArea(self):
        '''QGeoShape QPlaceSearchRequest.searchArea()'''
        return QGeoShape()
    def setCategories(self, categories):
        '''void QPlaceSearchRequest.setCategories(list-of-QPlaceCategory categories)'''
    def setCategory(self, category):
        '''void QPlaceSearchRequest.setCategory(QPlaceCategory category)'''
    def categories(self):
        '''list-of-QPlaceCategory QPlaceSearchRequest.categories()'''
        return [QPlaceCategory()]
    def setSearchTerm(self, term):
        '''void QPlaceSearchRequest.setSearchTerm(str term)'''
    def searchTerm(self):
        '''str QPlaceSearchRequest.searchTerm()'''
        return str()
    def __ne__(self, other):
        '''bool QPlaceSearchRequest.__ne__(QPlaceSearchRequest other)'''
        return bool()
    def __eq__(self, other):
        '''bool QPlaceSearchRequest.__eq__(QPlaceSearchRequest other)'''
        return bool()


class QPlaceSearchSuggestionReply(QPlaceReply):
    """"""
    def __init__(self, parent = None):
        '''void QPlaceSearchSuggestionReply.__init__(QObject parent = None)'''
    def setSuggestions(self, suggestions):
        '''void QPlaceSearchSuggestionReply.setSuggestions(list-of-str suggestions)'''
    def type(self):
        '''QPlaceReply.Type QPlaceSearchSuggestionReply.type()'''
        return QPlaceReply.Type()
    def suggestions(self):
        '''list-of-str QPlaceSearchSuggestionReply.suggestions()'''
        return [str()]


class QPlaceSupplier():
    """"""
    def __init__(self):
        '''void QPlaceSupplier.__init__()'''
    def __init__(self, other):
        '''void QPlaceSupplier.__init__(QPlaceSupplier other)'''
    def isEmpty(self):
        '''bool QPlaceSupplier.isEmpty()'''
        return bool()
    def setIcon(self, icon):
        '''void QPlaceSupplier.setIcon(QPlaceIcon icon)'''
    def icon(self):
        '''QPlaceIcon QPlaceSupplier.icon()'''
        return QPlaceIcon()
    def setUrl(self, data):
        '''void QPlaceSupplier.setUrl(QUrl data)'''
    def url(self):
        '''QUrl QPlaceSupplier.url()'''
        return QUrl()
    def setSupplierId(self, identifier):
        '''void QPlaceSupplier.setSupplierId(str identifier)'''
    def supplierId(self):
        '''str QPlaceSupplier.supplierId()'''
        return str()
    def setName(self, data):
        '''void QPlaceSupplier.setName(str data)'''
    def name(self):
        '''str QPlaceSupplier.name()'''
        return str()
    def __ne__(self, other):
        '''bool QPlaceSupplier.__ne__(QPlaceSupplier other)'''
        return bool()
    def __eq__(self, other):
        '''bool QPlaceSupplier.__eq__(QPlaceSupplier other)'''
        return bool()


class QPlaceUser():
    """"""
    def __init__(self):
        '''void QPlaceUser.__init__()'''
    def __init__(self, other):
        '''void QPlaceUser.__init__(QPlaceUser other)'''
    def setName(self, name):
        '''void QPlaceUser.setName(str name)'''
    def name(self):
        '''str QPlaceUser.name()'''
        return str()
    def setUserId(self, identifier):
        '''void QPlaceUser.setUserId(str identifier)'''
    def userId(self):
        '''str QPlaceUser.userId()'''
        return str()
    def __ne__(self, other):
        '''bool QPlaceUser.__ne__(QPlaceUser other)'''
        return bool()
    def __eq__(self, other):
        '''bool QPlaceUser.__eq__(QPlaceUser other)'''
        return bool()


