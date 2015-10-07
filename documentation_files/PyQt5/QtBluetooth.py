class pyqtSignal():
 def connect(self, targetSignal): pass
 def emit(self, *args): pass
from QtCore import *

from QtWidgets import *

import datetime

class QBluetooth():
    """"""
    # Enum QBluetooth.Security
    NoSecurity = 0
    Authorization = 0
    Authentication = 0
    Encryption = 0
    Secure = 0

    class SecurityFlags():
        """"""
        def __init__(self):
            '''QBluetooth.SecurityFlags QBluetooth.SecurityFlags.__init__()'''
            return QBluetooth.SecurityFlags()
        def __init__(self):
            '''int QBluetooth.SecurityFlags.__init__()'''
            return int()
        def __init__(self):
            '''void QBluetooth.SecurityFlags.__init__()'''
        def __bool__(self):
            '''int QBluetooth.SecurityFlags.__bool__()'''
            return int()
        def __ne__(self, f):
            '''bool QBluetooth.SecurityFlags.__ne__(QBluetooth.SecurityFlags f)'''
            return bool()
        def __eq__(self, f):
            '''bool QBluetooth.SecurityFlags.__eq__(QBluetooth.SecurityFlags f)'''
            return bool()
        def __invert__(self):
            '''QBluetooth.SecurityFlags QBluetooth.SecurityFlags.__invert__()'''
            return QBluetooth.SecurityFlags()
        def __and__(self, mask):
            '''QBluetooth.SecurityFlags QBluetooth.SecurityFlags.__and__(int mask)'''
            return QBluetooth.SecurityFlags()
        def __xor__(self, f):
            '''QBluetooth.SecurityFlags QBluetooth.SecurityFlags.__xor__(QBluetooth.SecurityFlags f)'''
            return QBluetooth.SecurityFlags()
        def __xor__(self, f):
            '''QBluetooth.SecurityFlags QBluetooth.SecurityFlags.__xor__(int f)'''
            return QBluetooth.SecurityFlags()
        def __or__(self, f):
            '''QBluetooth.SecurityFlags QBluetooth.SecurityFlags.__or__(QBluetooth.SecurityFlags f)'''
            return QBluetooth.SecurityFlags()
        def __or__(self, f):
            '''QBluetooth.SecurityFlags QBluetooth.SecurityFlags.__or__(int f)'''
            return QBluetooth.SecurityFlags()
        def __int__(self):
            '''int QBluetooth.SecurityFlags.__int__()'''
            return int()
        def __ixor__(self, f):
            '''QBluetooth.SecurityFlags QBluetooth.SecurityFlags.__ixor__(QBluetooth.SecurityFlags f)'''
            return QBluetooth.SecurityFlags()
        def __ior__(self, f):
            '''QBluetooth.SecurityFlags QBluetooth.SecurityFlags.__ior__(QBluetooth.SecurityFlags f)'''
            return QBluetooth.SecurityFlags()
        def __iand__(self, mask):
            '''QBluetooth.SecurityFlags QBluetooth.SecurityFlags.__iand__(int mask)'''
            return QBluetooth.SecurityFlags()


class QBluetoothAddress():
    """"""
    def __init__(self):
        '''void QBluetoothAddress.__init__()'''
    def __init__(self, address):
        '''void QBluetoothAddress.__init__(int address)'''
    def __init__(self, address):
        '''void QBluetoothAddress.__init__(str address)'''
    def __init__(self, other):
        '''void QBluetoothAddress.__init__(QBluetoothAddress other)'''
    def __ge__(self, other):
        '''bool QBluetoothAddress.__ge__(QBluetoothAddress other)'''
        return bool()
    def toString(self):
        '''str QBluetoothAddress.toString()'''
        return str()
    def toUInt64(self):
        '''int QBluetoothAddress.toUInt64()'''
        return int()
    def __ne__(self, other):
        '''bool QBluetoothAddress.__ne__(QBluetoothAddress other)'''
        return bool()
    def __eq__(self, other):
        '''bool QBluetoothAddress.__eq__(QBluetoothAddress other)'''
        return bool()
    def __lt__(self, other):
        '''bool QBluetoothAddress.__lt__(QBluetoothAddress other)'''
        return bool()
    def clear(self):
        '''void QBluetoothAddress.clear()'''
    def isNull(self):
        '''bool QBluetoothAddress.isNull()'''
        return bool()


class QBluetoothDeviceDiscoveryAgent(QObject):
    """"""
    # Enum QBluetoothDeviceDiscoveryAgent.InquiryType
    GeneralUnlimitedInquiry = 0
    LimitedInquiry = 0

    # Enum QBluetoothDeviceDiscoveryAgent.Error
    NoError = 0
    InputOutputError = 0
    PoweredOffError = 0
    InvalidBluetoothAdapterError = 0
    UnsupportedPlatformError = 0
    UnknownError = 0

    def __init__(self, parent = None):
        '''void QBluetoothDeviceDiscoveryAgent.__init__(QObject parent = None)'''
    def __init__(self, deviceAdapter, parent = None):
        '''void QBluetoothDeviceDiscoveryAgent.__init__(QBluetoothAddress deviceAdapter, QObject parent = None)'''
    canceled = pyqtSignal() # void canceled() - signal
    finished = pyqtSignal() # void finished() - signal
    deviceDiscovered = pyqtSignal() # void deviceDiscovered(const QBluetoothDeviceInfoamp;) - signal
    def stop(self):
        '''void QBluetoothDeviceDiscoveryAgent.stop()'''
    def start(self):
        '''void QBluetoothDeviceDiscoveryAgent.start()'''
    def discoveredDevices(self):
        '''list-of-QBluetoothDeviceInfo QBluetoothDeviceDiscoveryAgent.discoveredDevices()'''
        return [QBluetoothDeviceInfo()]
    def errorString(self):
        '''str QBluetoothDeviceDiscoveryAgent.errorString()'''
        return str()
    def error(self):
        '''QBluetoothDeviceDiscoveryAgent.Error QBluetoothDeviceDiscoveryAgent.error()'''
        return QBluetoothDeviceDiscoveryAgent.Error()
    error = pyqtSignal() # void error(QBluetoothDeviceDiscoveryAgent::Error) - signal
    def isActive(self):
        '''bool QBluetoothDeviceDiscoveryAgent.isActive()'''
        return bool()
    def setInquiryType(self, type):
        '''void QBluetoothDeviceDiscoveryAgent.setInquiryType(QBluetoothDeviceDiscoveryAgent.InquiryType type)'''
    def inquiryType(self):
        '''QBluetoothDeviceDiscoveryAgent.InquiryType QBluetoothDeviceDiscoveryAgent.inquiryType()'''
        return QBluetoothDeviceDiscoveryAgent.InquiryType()


class QBluetoothDeviceInfo():
    """"""
    # Enum QBluetoothDeviceInfo.CoreConfiguration
    UnknownCoreConfiguration = 0
    LowEnergyCoreConfiguration = 0
    BaseRateCoreConfiguration = 0
    BaseRateAndLowEnergyCoreConfiguration = 0

    # Enum QBluetoothDeviceInfo.DataCompleteness
    DataComplete = 0
    DataIncomplete = 0
    DataUnavailable = 0

    # Enum QBluetoothDeviceInfo.ServiceClass
    NoService = 0
    PositioningService = 0
    NetworkingService = 0
    RenderingService = 0
    CapturingService = 0
    ObjectTransferService = 0
    AudioService = 0
    TelephonyService = 0
    InformationService = 0
    AllServices = 0

    # Enum QBluetoothDeviceInfo.MinorHealthClass
    UncategorizedHealthDevice = 0
    HealthBloodPressureMonitor = 0
    HealthThermometer = 0
    HealthWeightScale = 0
    HealthGlucoseMeter = 0
    HealthPulseOximeter = 0
    HealthDataDisplay = 0
    HealthStepCounter = 0

    # Enum QBluetoothDeviceInfo.MinorToyClass
    UncategorizedToy = 0
    ToyRobot = 0
    ToyVehicle = 0
    ToyDoll = 0
    ToyController = 0
    ToyGame = 0

    # Enum QBluetoothDeviceInfo.MinorWearableClass
    UncategorizedWearableDevice = 0
    WearableWristWatch = 0
    WearablePager = 0
    WearableJacket = 0
    WearableHelmet = 0
    WearableGlasses = 0

    # Enum QBluetoothDeviceInfo.MinorImagingClass
    UncategorizedImagingDevice = 0
    ImageDisplay = 0
    ImageCamera = 0
    ImageScanner = 0
    ImagePrinter = 0

    # Enum QBluetoothDeviceInfo.MinorPeripheralClass
    UncategorizedPeripheral = 0
    KeyboardPeripheral = 0
    PointingDevicePeripheral = 0
    KeyboardWithPointingDevicePeripheral = 0
    JoystickPeripheral = 0
    GamepadPeripheral = 0
    RemoteControlPeripheral = 0
    SensingDevicePeripheral = 0
    DigitizerTabletPeripheral = 0
    CardReaderPeripheral = 0

    # Enum QBluetoothDeviceInfo.MinorAudioVideoClass
    UncategorizedAudioVideoDevice = 0
    WearableHeadsetDevice = 0
    HandsFreeDevice = 0
    Microphone = 0
    Loudspeaker = 0
    Headphones = 0
    PortableAudioDevice = 0
    CarAudio = 0
    SetTopBox = 0
    HiFiAudioDevice = 0
    Vcr = 0
    VideoCamera = 0
    Camcorder = 0
    VideoMonitor = 0
    VideoDisplayAndLoudspeaker = 0
    VideoConferencing = 0
    GamingDevice = 0

    # Enum QBluetoothDeviceInfo.MinorNetworkClass
    NetworkFullService = 0
    NetworkLoadFactorOne = 0
    NetworkLoadFactorTwo = 0
    NetworkLoadFactorThree = 0
    NetworkLoadFactorFour = 0
    NetworkLoadFactorFive = 0
    NetworkLoadFactorSix = 0
    NetworkNoService = 0

    # Enum QBluetoothDeviceInfo.MinorPhoneClass
    UncategorizedPhone = 0
    CellularPhone = 0
    CordlessPhone = 0
    SmartPhone = 0
    WiredModemOrVoiceGatewayPhone = 0
    CommonIsdnAccessPhone = 0

    # Enum QBluetoothDeviceInfo.MinorComputerClass
    UncategorizedComputer = 0
    DesktopComputer = 0
    ServerComputer = 0
    LaptopComputer = 0
    HandheldClamShellComputer = 0
    HandheldComputer = 0
    WearableComputer = 0

    # Enum QBluetoothDeviceInfo.MinorMiscellaneousClass
    UncategorizedMiscellaneous = 0

    # Enum QBluetoothDeviceInfo.MajorDeviceClass
    MiscellaneousDevice = 0
    ComputerDevice = 0
    PhoneDevice = 0
    LANAccessDevice = 0
    AudioVideoDevice = 0
    PeripheralDevice = 0
    ImagingDevice = 0
    WearableDevice = 0
    ToyDevice = 0
    HealthDevice = 0
    UncategorizedDevice = 0

    def __init__(self):
        '''void QBluetoothDeviceInfo.__init__()'''
    def __init__(self, address, name, classOfDevice):
        '''void QBluetoothDeviceInfo.__init__(QBluetoothAddress address, str name, int classOfDevice)'''
    def __init__(self, uuid, name, classOfDevice):
        '''void QBluetoothDeviceInfo.__init__(QBluetoothUuid uuid, str name, int classOfDevice)'''
    def __init__(self, other):
        '''void QBluetoothDeviceInfo.__init__(QBluetoothDeviceInfo other)'''
    def deviceUuid(self):
        '''QBluetoothUuid QBluetoothDeviceInfo.deviceUuid()'''
        return QBluetoothUuid()
    def setDeviceUuid(self, uuid):
        '''void QBluetoothDeviceInfo.setDeviceUuid(QBluetoothUuid uuid)'''
    def coreConfigurations(self):
        '''QBluetoothDeviceInfo.CoreConfigurations QBluetoothDeviceInfo.coreConfigurations()'''
        return QBluetoothDeviceInfo.CoreConfigurations()
    def setCoreConfigurations(self, coreConfigs):
        '''void QBluetoothDeviceInfo.setCoreConfigurations(QBluetoothDeviceInfo.CoreConfigurations coreConfigs)'''
    def serviceUuidsCompleteness(self):
        '''QBluetoothDeviceInfo.DataCompleteness QBluetoothDeviceInfo.serviceUuidsCompleteness()'''
        return QBluetoothDeviceInfo.DataCompleteness()
    def serviceUuids(self, completeness):
        '''list-of-QBluetoothUuid QBluetoothDeviceInfo.serviceUuids(QBluetoothDeviceInfo.DataCompleteness completeness)'''
        return [QBluetoothUuid()]
    def setServiceUuids(self, uuids, completeness):
        '''void QBluetoothDeviceInfo.setServiceUuids(list-of-QBluetoothUuid uuids, QBluetoothDeviceInfo.DataCompleteness completeness)'''
    def setRssi(self, signal):
        '''void QBluetoothDeviceInfo.setRssi(int signal)'''
    def rssi(self):
        '''int QBluetoothDeviceInfo.rssi()'''
        return int()
    def minorDeviceClass(self):
        '''int QBluetoothDeviceInfo.minorDeviceClass()'''
        return int()
    def majorDeviceClass(self):
        '''QBluetoothDeviceInfo.MajorDeviceClass QBluetoothDeviceInfo.majorDeviceClass()'''
        return QBluetoothDeviceInfo.MajorDeviceClass()
    def serviceClasses(self):
        '''QBluetoothDeviceInfo.ServiceClasses QBluetoothDeviceInfo.serviceClasses()'''
        return QBluetoothDeviceInfo.ServiceClasses()
    def name(self):
        '''str QBluetoothDeviceInfo.name()'''
        return str()
    def address(self):
        '''QBluetoothAddress QBluetoothDeviceInfo.address()'''
        return QBluetoothAddress()
    def __ne__(self, other):
        '''bool QBluetoothDeviceInfo.__ne__(QBluetoothDeviceInfo other)'''
        return bool()
    def __eq__(self, other):
        '''bool QBluetoothDeviceInfo.__eq__(QBluetoothDeviceInfo other)'''
        return bool()
    def setCached(self, cached):
        '''void QBluetoothDeviceInfo.setCached(bool cached)'''
    def isCached(self):
        '''bool QBluetoothDeviceInfo.isCached()'''
        return bool()
    def isValid(self):
        '''bool QBluetoothDeviceInfo.isValid()'''
        return bool()
    class CoreConfigurations():
        """"""
        def __init__(self):
            '''QBluetoothDeviceInfo.CoreConfigurations QBluetoothDeviceInfo.CoreConfigurations.__init__()'''
            return QBluetoothDeviceInfo.CoreConfigurations()
        def __init__(self):
            '''int QBluetoothDeviceInfo.CoreConfigurations.__init__()'''
            return int()
        def __init__(self):
            '''void QBluetoothDeviceInfo.CoreConfigurations.__init__()'''
        def __bool__(self):
            '''int QBluetoothDeviceInfo.CoreConfigurations.__bool__()'''
            return int()
        def __ne__(self, f):
            '''bool QBluetoothDeviceInfo.CoreConfigurations.__ne__(QBluetoothDeviceInfo.CoreConfigurations f)'''
            return bool()
        def __eq__(self, f):
            '''bool QBluetoothDeviceInfo.CoreConfigurations.__eq__(QBluetoothDeviceInfo.CoreConfigurations f)'''
            return bool()
        def __invert__(self):
            '''QBluetoothDeviceInfo.CoreConfigurations QBluetoothDeviceInfo.CoreConfigurations.__invert__()'''
            return QBluetoothDeviceInfo.CoreConfigurations()
        def __and__(self, mask):
            '''QBluetoothDeviceInfo.CoreConfigurations QBluetoothDeviceInfo.CoreConfigurations.__and__(int mask)'''
            return QBluetoothDeviceInfo.CoreConfigurations()
        def __xor__(self, f):
            '''QBluetoothDeviceInfo.CoreConfigurations QBluetoothDeviceInfo.CoreConfigurations.__xor__(QBluetoothDeviceInfo.CoreConfigurations f)'''
            return QBluetoothDeviceInfo.CoreConfigurations()
        def __xor__(self, f):
            '''QBluetoothDeviceInfo.CoreConfigurations QBluetoothDeviceInfo.CoreConfigurations.__xor__(int f)'''
            return QBluetoothDeviceInfo.CoreConfigurations()
        def __or__(self, f):
            '''QBluetoothDeviceInfo.CoreConfigurations QBluetoothDeviceInfo.CoreConfigurations.__or__(QBluetoothDeviceInfo.CoreConfigurations f)'''
            return QBluetoothDeviceInfo.CoreConfigurations()
        def __or__(self, f):
            '''QBluetoothDeviceInfo.CoreConfigurations QBluetoothDeviceInfo.CoreConfigurations.__or__(int f)'''
            return QBluetoothDeviceInfo.CoreConfigurations()
        def __int__(self):
            '''int QBluetoothDeviceInfo.CoreConfigurations.__int__()'''
            return int()
        def __ixor__(self, f):
            '''QBluetoothDeviceInfo.CoreConfigurations QBluetoothDeviceInfo.CoreConfigurations.__ixor__(QBluetoothDeviceInfo.CoreConfigurations f)'''
            return QBluetoothDeviceInfo.CoreConfigurations()
        def __ior__(self, f):
            '''QBluetoothDeviceInfo.CoreConfigurations QBluetoothDeviceInfo.CoreConfigurations.__ior__(QBluetoothDeviceInfo.CoreConfigurations f)'''
            return QBluetoothDeviceInfo.CoreConfigurations()
        def __iand__(self, mask):
            '''QBluetoothDeviceInfo.CoreConfigurations QBluetoothDeviceInfo.CoreConfigurations.__iand__(int mask)'''
            return QBluetoothDeviceInfo.CoreConfigurations()
    class ServiceClasses():
        """"""
        def __init__(self):
            '''QBluetoothDeviceInfo.ServiceClasses QBluetoothDeviceInfo.ServiceClasses.__init__()'''
            return QBluetoothDeviceInfo.ServiceClasses()
        def __init__(self):
            '''int QBluetoothDeviceInfo.ServiceClasses.__init__()'''
            return int()
        def __init__(self):
            '''void QBluetoothDeviceInfo.ServiceClasses.__init__()'''
        def __bool__(self):
            '''int QBluetoothDeviceInfo.ServiceClasses.__bool__()'''
            return int()
        def __ne__(self, f):
            '''bool QBluetoothDeviceInfo.ServiceClasses.__ne__(QBluetoothDeviceInfo.ServiceClasses f)'''
            return bool()
        def __eq__(self, f):
            '''bool QBluetoothDeviceInfo.ServiceClasses.__eq__(QBluetoothDeviceInfo.ServiceClasses f)'''
            return bool()
        def __invert__(self):
            '''QBluetoothDeviceInfo.ServiceClasses QBluetoothDeviceInfo.ServiceClasses.__invert__()'''
            return QBluetoothDeviceInfo.ServiceClasses()
        def __and__(self, mask):
            '''QBluetoothDeviceInfo.ServiceClasses QBluetoothDeviceInfo.ServiceClasses.__and__(int mask)'''
            return QBluetoothDeviceInfo.ServiceClasses()
        def __xor__(self, f):
            '''QBluetoothDeviceInfo.ServiceClasses QBluetoothDeviceInfo.ServiceClasses.__xor__(QBluetoothDeviceInfo.ServiceClasses f)'''
            return QBluetoothDeviceInfo.ServiceClasses()
        def __xor__(self, f):
            '''QBluetoothDeviceInfo.ServiceClasses QBluetoothDeviceInfo.ServiceClasses.__xor__(int f)'''
            return QBluetoothDeviceInfo.ServiceClasses()
        def __or__(self, f):
            '''QBluetoothDeviceInfo.ServiceClasses QBluetoothDeviceInfo.ServiceClasses.__or__(QBluetoothDeviceInfo.ServiceClasses f)'''
            return QBluetoothDeviceInfo.ServiceClasses()
        def __or__(self, f):
            '''QBluetoothDeviceInfo.ServiceClasses QBluetoothDeviceInfo.ServiceClasses.__or__(int f)'''
            return QBluetoothDeviceInfo.ServiceClasses()
        def __int__(self):
            '''int QBluetoothDeviceInfo.ServiceClasses.__int__()'''
            return int()
        def __ixor__(self, f):
            '''QBluetoothDeviceInfo.ServiceClasses QBluetoothDeviceInfo.ServiceClasses.__ixor__(QBluetoothDeviceInfo.ServiceClasses f)'''
            return QBluetoothDeviceInfo.ServiceClasses()
        def __ior__(self, f):
            '''QBluetoothDeviceInfo.ServiceClasses QBluetoothDeviceInfo.ServiceClasses.__ior__(QBluetoothDeviceInfo.ServiceClasses f)'''
            return QBluetoothDeviceInfo.ServiceClasses()
        def __iand__(self, mask):
            '''QBluetoothDeviceInfo.ServiceClasses QBluetoothDeviceInfo.ServiceClasses.__iand__(int mask)'''
            return QBluetoothDeviceInfo.ServiceClasses()


class QBluetoothHostInfo():
    """"""
    def __init__(self):
        '''void QBluetoothHostInfo.__init__()'''
    def __init__(self, other):
        '''void QBluetoothHostInfo.__init__(QBluetoothHostInfo other)'''
    def __ne__(self, other):
        '''bool QBluetoothHostInfo.__ne__(QBluetoothHostInfo other)'''
        return bool()
    def __eq__(self, other):
        '''bool QBluetoothHostInfo.__eq__(QBluetoothHostInfo other)'''
        return bool()
    def setName(self, name):
        '''void QBluetoothHostInfo.setName(str name)'''
    def name(self):
        '''str QBluetoothHostInfo.name()'''
        return str()
    def setAddress(self, address):
        '''void QBluetoothHostInfo.setAddress(QBluetoothAddress address)'''
    def address(self):
        '''QBluetoothAddress QBluetoothHostInfo.address()'''
        return QBluetoothAddress()


class QBluetoothLocalDevice(QObject):
    """"""
    # Enum QBluetoothLocalDevice.Error
    NoError = 0
    PairingError = 0
    UnknownError = 0

    # Enum QBluetoothLocalDevice.HostMode
    HostPoweredOff = 0
    HostConnectable = 0
    HostDiscoverable = 0
    HostDiscoverableLimitedInquiry = 0

    # Enum QBluetoothLocalDevice.Pairing
    Unpaired = 0
    Paired = 0
    AuthorizedPaired = 0

    def __init__(self, parent = None):
        '''void QBluetoothLocalDevice.__init__(QObject parent = None)'''
    def __init__(self, address, parent = None):
        '''void QBluetoothLocalDevice.__init__(QBluetoothAddress address, QObject parent = None)'''
    deviceDisconnected = pyqtSignal() # void deviceDisconnected(const QBluetoothAddressamp;) - signal
    deviceConnected = pyqtSignal() # void deviceConnected(const QBluetoothAddressamp;) - signal
    error = pyqtSignal() # void error(QBluetoothLocalDevice::Error) - signal
    pairingDisplayConfirmation = pyqtSignal() # void pairingDisplayConfirmation(const QBluetoothAddressamp;,QString) - signal
    pairingDisplayPinCode = pyqtSignal() # void pairingDisplayPinCode(const QBluetoothAddressamp;,QString) - signal
    pairingFinished = pyqtSignal() # void pairingFinished(const QBluetoothAddressamp;,QBluetoothLocalDevice::Pairing) - signal
    hostModeStateChanged = pyqtSignal() # void hostModeStateChanged(QBluetoothLocalDevice::HostMode) - signal
    def pairingConfirmation(self, confirmation):
        '''void QBluetoothLocalDevice.pairingConfirmation(bool confirmation)'''
    def connectedDevices(self):
        '''list-of-QBluetoothAddress QBluetoothLocalDevice.connectedDevices()'''
        return [QBluetoothAddress()]
    def allDevices(self):
        '''static list-of-QBluetoothHostInfo QBluetoothLocalDevice.allDevices()'''
        return [QBluetoothHostInfo()]
    def address(self):
        '''QBluetoothAddress QBluetoothLocalDevice.address()'''
        return QBluetoothAddress()
    def name(self):
        '''str QBluetoothLocalDevice.name()'''
        return str()
    def powerOn(self):
        '''void QBluetoothLocalDevice.powerOn()'''
    def hostMode(self):
        '''QBluetoothLocalDevice.HostMode QBluetoothLocalDevice.hostMode()'''
        return QBluetoothLocalDevice.HostMode()
    def setHostMode(self, mode):
        '''void QBluetoothLocalDevice.setHostMode(QBluetoothLocalDevice.HostMode mode)'''
    def pairingStatus(self, address):
        '''QBluetoothLocalDevice.Pairing QBluetoothLocalDevice.pairingStatus(QBluetoothAddress address)'''
        return QBluetoothLocalDevice.Pairing()
    def requestPairing(self, address, pairing):
        '''void QBluetoothLocalDevice.requestPairing(QBluetoothAddress address, QBluetoothLocalDevice.Pairing pairing)'''
    def isValid(self):
        '''bool QBluetoothLocalDevice.isValid()'''
        return bool()


class QBluetoothServer(QObject):
    """"""
    # Enum QBluetoothServer.Error
    NoError = 0
    UnknownError = 0
    PoweredOffError = 0
    InputOutputError = 0
    ServiceAlreadyRegisteredError = 0
    UnsupportedProtocolError = 0

    def __init__(self, serverType, parent = None):
        '''void QBluetoothServer.__init__(QBluetoothServiceInfo.Protocol serverType, QObject parent = None)'''
    newConnection = pyqtSignal() # void newConnection() - signal
    def error(self):
        '''QBluetoothServer.Error QBluetoothServer.error()'''
        return QBluetoothServer.Error()
    error = pyqtSignal() # void error(QBluetoothServer::Error) - signal
    def serverType(self):
        '''QBluetoothServiceInfo.Protocol QBluetoothServer.serverType()'''
        return QBluetoothServiceInfo.Protocol()
    def securityFlags(self):
        '''QBluetooth.SecurityFlags QBluetoothServer.securityFlags()'''
        return QBluetooth.SecurityFlags()
    def setSecurityFlags(self, security):
        '''void QBluetoothServer.setSecurityFlags(QBluetooth.SecurityFlags security)'''
    def serverPort(self):
        '''int QBluetoothServer.serverPort()'''
        return int()
    def serverAddress(self):
        '''QBluetoothAddress QBluetoothServer.serverAddress()'''
        return QBluetoothAddress()
    def nextPendingConnection(self):
        '''QBluetoothSocket QBluetoothServer.nextPendingConnection()'''
        return QBluetoothSocket()
    def hasPendingConnections(self):
        '''bool QBluetoothServer.hasPendingConnections()'''
        return bool()
    def maxPendingConnections(self):
        '''int QBluetoothServer.maxPendingConnections()'''
        return int()
    def setMaxPendingConnections(self, numConnections):
        '''void QBluetoothServer.setMaxPendingConnections(int numConnections)'''
    def isListening(self):
        '''bool QBluetoothServer.isListening()'''
        return bool()
    def listen(self, address = QBluetoothAddress(), port = 0):
        '''bool QBluetoothServer.listen(QBluetoothAddress address = QBluetoothAddress(), int port = 0)'''
        return bool()
    def listen(self, uuid, serviceName = None):
        '''QBluetoothServiceInfo QBluetoothServer.listen(QBluetoothUuid uuid, str serviceName = '')'''
        return QBluetoothServiceInfo()
    def close(self):
        '''void QBluetoothServer.close()'''


class QBluetoothServiceDiscoveryAgent(QObject):
    """"""
    # Enum QBluetoothServiceDiscoveryAgent.DiscoveryMode
    MinimalDiscovery = 0
    FullDiscovery = 0

    # Enum QBluetoothServiceDiscoveryAgent.Error
    NoError = 0
    InputOutputError = 0
    PoweredOffError = 0
    InvalidBluetoothAdapterError = 0
    UnknownError = 0

    def __init__(self, parent = None):
        '''void QBluetoothServiceDiscoveryAgent.__init__(QObject parent = None)'''
    def __init__(self, deviceAdapter, parent = None):
        '''void QBluetoothServiceDiscoveryAgent.__init__(QBluetoothAddress deviceAdapter, QObject parent = None)'''
    canceled = pyqtSignal() # void canceled() - signal
    finished = pyqtSignal() # void finished() - signal
    serviceDiscovered = pyqtSignal() # void serviceDiscovered(const QBluetoothServiceInfoamp;) - signal
    def clear(self):
        '''void QBluetoothServiceDiscoveryAgent.clear()'''
    def stop(self):
        '''void QBluetoothServiceDiscoveryAgent.stop()'''
    def start(self, mode = None):
        '''void QBluetoothServiceDiscoveryAgent.start(QBluetoothServiceDiscoveryAgent.DiscoveryMode mode = QBluetoothServiceDiscoveryAgent.MinimalDiscovery)'''
    def remoteAddress(self):
        '''QBluetoothAddress QBluetoothServiceDiscoveryAgent.remoteAddress()'''
        return QBluetoothAddress()
    def setRemoteAddress(self, address):
        '''bool QBluetoothServiceDiscoveryAgent.setRemoteAddress(QBluetoothAddress address)'''
        return bool()
    def uuidFilter(self):
        '''list-of-QBluetoothUuid QBluetoothServiceDiscoveryAgent.uuidFilter()'''
        return [QBluetoothUuid()]
    def setUuidFilter(self, uuids):
        '''void QBluetoothServiceDiscoveryAgent.setUuidFilter(list-of-QBluetoothUuid uuids)'''
    def setUuidFilter(self, uuid):
        '''void QBluetoothServiceDiscoveryAgent.setUuidFilter(QBluetoothUuid uuid)'''
    def discoveredServices(self):
        '''list-of-QBluetoothServiceInfo QBluetoothServiceDiscoveryAgent.discoveredServices()'''
        return [QBluetoothServiceInfo()]
    def errorString(self):
        '''str QBluetoothServiceDiscoveryAgent.errorString()'''
        return str()
    def error(self):
        '''QBluetoothServiceDiscoveryAgent.Error QBluetoothServiceDiscoveryAgent.error()'''
        return QBluetoothServiceDiscoveryAgent.Error()
    error = pyqtSignal() # void error(QBluetoothServiceDiscoveryAgent::Error) - signal
    def isActive(self):
        '''bool QBluetoothServiceDiscoveryAgent.isActive()'''
        return bool()


class QBluetoothServiceInfo():
    """"""
    # Enum QBluetoothServiceInfo.Protocol
    UnknownProtocol = 0
    L2capProtocol = 0
    RfcommProtocol = 0

    # Enum QBluetoothServiceInfo.AttributeId
    ServiceRecordHandle = 0
    ServiceClassIds = 0
    ServiceRecordState = 0
    ServiceId = 0
    ProtocolDescriptorList = 0
    BrowseGroupList = 0
    LanguageBaseAttributeIdList = 0
    ServiceInfoTimeToLive = 0
    ServiceAvailability = 0
    BluetoothProfileDescriptorList = 0
    DocumentationUrl = 0
    ClientExecutableUrl = 0
    IconUrl = 0
    AdditionalProtocolDescriptorList = 0
    PrimaryLanguageBase = 0
    ServiceName = 0
    ServiceDescription = 0
    ServiceProvider = 0

    def __init__(self):
        '''void QBluetoothServiceInfo.__init__()'''
    def __init__(self, other):
        '''void QBluetoothServiceInfo.__init__(QBluetoothServiceInfo other)'''
    def serviceClassUuids(self):
        '''list-of-QBluetoothUuid QBluetoothServiceInfo.serviceClassUuids()'''
        return [QBluetoothUuid()]
    def serviceUuid(self):
        '''QBluetoothUuid QBluetoothServiceInfo.serviceUuid()'''
        return QBluetoothUuid()
    def setServiceUuid(self, uuid):
        '''void QBluetoothServiceInfo.setServiceUuid(QBluetoothUuid uuid)'''
    def serviceAvailability(self):
        '''int QBluetoothServiceInfo.serviceAvailability()'''
        return int()
    def setServiceAvailability(self, availability):
        '''void QBluetoothServiceInfo.setServiceAvailability(int availability)'''
    def serviceProvider(self):
        '''str QBluetoothServiceInfo.serviceProvider()'''
        return str()
    def setServiceProvider(self, provider):
        '''void QBluetoothServiceInfo.setServiceProvider(str provider)'''
    def serviceDescription(self):
        '''str QBluetoothServiceInfo.serviceDescription()'''
        return str()
    def setServiceDescription(self, description):
        '''void QBluetoothServiceInfo.setServiceDescription(str description)'''
    def serviceName(self):
        '''str QBluetoothServiceInfo.serviceName()'''
        return str()
    def setServiceName(self, name):
        '''void QBluetoothServiceInfo.setServiceName(str name)'''
    def setAttribute(self, attributeId, value):
        '''void QBluetoothServiceInfo.setAttribute(int attributeId, QBluetoothUuid value)'''
    def setAttribute(self, attributeId, value):
        '''void QBluetoothServiceInfo.setAttribute(int attributeId, list-of-object value)'''
    def setAttribute(self, attributeId, value):
        '''void QBluetoothServiceInfo.setAttribute(int attributeId, QVariant value)'''
    def unregisterService(self):
        '''bool QBluetoothServiceInfo.unregisterService()'''
        return bool()
    def registerService(self, localAdapter = QBluetoothAddress()):
        '''bool QBluetoothServiceInfo.registerService(QBluetoothAddress localAdapter = QBluetoothAddress())'''
        return bool()
    def isRegistered(self):
        '''bool QBluetoothServiceInfo.isRegistered()'''
        return bool()
    def protocolDescriptor(self, protocol):
        '''list-of-object QBluetoothServiceInfo.protocolDescriptor(QBluetoothUuid.ProtocolUuid protocol)'''
        return [object()]
    def serverChannel(self):
        '''int QBluetoothServiceInfo.serverChannel()'''
        return int()
    def protocolServiceMultiplexer(self):
        '''int QBluetoothServiceInfo.protocolServiceMultiplexer()'''
        return int()
    def socketProtocol(self):
        '''QBluetoothServiceInfo.Protocol QBluetoothServiceInfo.socketProtocol()'''
        return QBluetoothServiceInfo.Protocol()
    def removeAttribute(self, attributeId):
        '''void QBluetoothServiceInfo.removeAttribute(int attributeId)'''
    def contains(self, attributeId):
        '''bool QBluetoothServiceInfo.contains(int attributeId)'''
        return bool()
    def attributes(self):
        '''list-of-int QBluetoothServiceInfo.attributes()'''
        return [int()]
    def attribute(self, attributeId):
        '''QVariant QBluetoothServiceInfo.attribute(int attributeId)'''
        return QVariant()
    def device(self):
        '''QBluetoothDeviceInfo QBluetoothServiceInfo.device()'''
        return QBluetoothDeviceInfo()
    def setDevice(self, info):
        '''void QBluetoothServiceInfo.setDevice(QBluetoothDeviceInfo info)'''
    def isComplete(self):
        '''bool QBluetoothServiceInfo.isComplete()'''
        return bool()
    def isValid(self):
        '''bool QBluetoothServiceInfo.isValid()'''
        return bool()


class QBluetoothSocket(QIODevice):
    """"""
    # Enum QBluetoothSocket.SocketError
    NoSocketError = 0
    UnknownSocketError = 0
    HostNotFoundError = 0
    ServiceNotFoundError = 0
    NetworkError = 0
    UnsupportedProtocolError = 0
    OperationError = 0

    # Enum QBluetoothSocket.SocketState
    UnconnectedState = 0
    ServiceLookupState = 0
    ConnectingState = 0
    ConnectedState = 0
    BoundState = 0
    ClosingState = 0
    ListeningState = 0

    def __init__(self, socketType, parent = None):
        '''void QBluetoothSocket.__init__(QBluetoothServiceInfo.Protocol socketType, QObject parent = None)'''
    def __init__(self, parent = None):
        '''void QBluetoothSocket.__init__(QObject parent = None)'''
    def doDeviceDiscovery(self, service, openMode):
        '''void QBluetoothSocket.doDeviceDiscovery(QBluetoothServiceInfo service, QIODevice.OpenMode openMode)'''
    def setSocketError(self, error):
        '''void QBluetoothSocket.setSocketError(QBluetoothSocket.SocketError error)'''
    def setSocketState(self, state):
        '''void QBluetoothSocket.setSocketState(QBluetoothSocket.SocketState state)'''
    def writeData(self, data):
        '''int QBluetoothSocket.writeData(str data)'''
        return int()
    def readData(self, maxlen):
        '''str QBluetoothSocket.readData(int maxlen)'''
        return str()
    stateChanged = pyqtSignal() # void stateChanged(QBluetoothSocket::SocketState) - signal
    disconnected = pyqtSignal() # void disconnected() - signal
    connected = pyqtSignal() # void connected() - signal
    def errorString(self):
        '''str QBluetoothSocket.errorString()'''
        return str()
    def error(self):
        '''QBluetoothSocket.SocketError QBluetoothSocket.error()'''
        return QBluetoothSocket.SocketError()
    error = pyqtSignal() # void error(QBluetoothSocket::SocketError) - signal
    def state(self):
        '''QBluetoothSocket.SocketState QBluetoothSocket.state()'''
        return QBluetoothSocket.SocketState()
    def socketType(self):
        '''QBluetoothServiceInfo.Protocol QBluetoothSocket.socketType()'''
        return QBluetoothServiceInfo.Protocol()
    def socketDescriptor(self):
        '''int QBluetoothSocket.socketDescriptor()'''
        return int()
    def setSocketDescriptor(self, socketDescriptor, socketType, state = None, mode = None):
        '''bool QBluetoothSocket.setSocketDescriptor(int socketDescriptor, QBluetoothServiceInfo.Protocol socketType, QBluetoothSocket.SocketState state = QBluetoothSocket.ConnectedState, QIODevice.OpenMode mode = QIODevice.ReadWrite)'''
        return bool()
    def peerPort(self):
        '''int QBluetoothSocket.peerPort()'''
        return int()
    def peerAddress(self):
        '''QBluetoothAddress QBluetoothSocket.peerAddress()'''
        return QBluetoothAddress()
    def peerName(self):
        '''str QBluetoothSocket.peerName()'''
        return str()
    def localPort(self):
        '''int QBluetoothSocket.localPort()'''
        return int()
    def localAddress(self):
        '''QBluetoothAddress QBluetoothSocket.localAddress()'''
        return QBluetoothAddress()
    def localName(self):
        '''str QBluetoothSocket.localName()'''
        return str()
    def disconnectFromService(self):
        '''void QBluetoothSocket.disconnectFromService()'''
    def connectToService(self, service, mode = None):
        '''void QBluetoothSocket.connectToService(QBluetoothServiceInfo service, QIODevice.OpenMode mode = QIODevice.ReadWrite)'''
    def connectToService(self, address, uuid, mode = None):
        '''void QBluetoothSocket.connectToService(QBluetoothAddress address, QBluetoothUuid uuid, QIODevice.OpenMode mode = QIODevice.ReadWrite)'''
    def connectToService(self, address, port, mode = None):
        '''void QBluetoothSocket.connectToService(QBluetoothAddress address, int port, QIODevice.OpenMode mode = QIODevice.ReadWrite)'''
    def canReadLine(self):
        '''bool QBluetoothSocket.canReadLine()'''
        return bool()
    def bytesToWrite(self):
        '''int QBluetoothSocket.bytesToWrite()'''
        return int()
    def bytesAvailable(self):
        '''int QBluetoothSocket.bytesAvailable()'''
        return int()
    def isSequential(self):
        '''bool QBluetoothSocket.isSequential()'''
        return bool()
    def close(self):
        '''void QBluetoothSocket.close()'''
    def abort(self):
        '''void QBluetoothSocket.abort()'''


class QBluetoothTransferManager(QObject):
    """"""
    def __init__(self, parent = None):
        '''void QBluetoothTransferManager.__init__(QObject parent = None)'''
    finished = pyqtSignal() # void finished(QBluetoothTransferReply*) - signal
    def put(self, request, data):
        '''QBluetoothTransferReply QBluetoothTransferManager.put(QBluetoothTransferRequest request, QIODevice data)'''
        return QBluetoothTransferReply()


class QBluetoothTransferReply(QObject):
    """"""
    # Enum QBluetoothTransferReply.TransferError
    NoError = 0
    UnknownError = 0
    FileNotFoundError = 0
    HostNotFoundError = 0
    UserCanceledTransferError = 0
    IODeviceNotReadableError = 0
    ResourceBusyError = 0
    SessionError = 0

    def __init__(self, parent = None):
        '''void QBluetoothTransferReply.__init__(QObject parent = None)'''
    def setRequest(self, request):
        '''void QBluetoothTransferReply.setRequest(QBluetoothTransferRequest request)'''
    def setManager(self, manager):
        '''void QBluetoothTransferReply.setManager(QBluetoothTransferManager manager)'''
    transferProgress = pyqtSignal() # void transferProgress(qint64,qint64) - signal
    finished = pyqtSignal() # void finished(QBluetoothTransferReply*) - signal
    def abort(self):
        '''void QBluetoothTransferReply.abort()'''
    def request(self):
        '''QBluetoothTransferRequest QBluetoothTransferReply.request()'''
        return QBluetoothTransferRequest()
    def errorString(self):
        '''abstract str QBluetoothTransferReply.errorString()'''
        return str()
    def error(self):
        '''abstract QBluetoothTransferReply.TransferError QBluetoothTransferReply.error()'''
        return QBluetoothTransferReply.TransferError()
    error = pyqtSignal() # void error(QBluetoothTransferReply::TransferError) - signal
    def manager(self):
        '''QBluetoothTransferManager QBluetoothTransferReply.manager()'''
        return QBluetoothTransferManager()
    def isRunning(self):
        '''abstract bool QBluetoothTransferReply.isRunning()'''
        return bool()
    def isFinished(self):
        '''abstract bool QBluetoothTransferReply.isFinished()'''
        return bool()


class QBluetoothTransferRequest():
    """"""
    # Enum QBluetoothTransferRequest.Attribute
    DescriptionAttribute = 0
    TimeAttribute = 0
    TypeAttribute = 0
    LengthAttribute = 0
    NameAttribute = 0

    def __init__(self, address = QBluetoothAddress()):
        '''void QBluetoothTransferRequest.__init__(QBluetoothAddress address = QBluetoothAddress())'''
    def __init__(self, other):
        '''void QBluetoothTransferRequest.__init__(QBluetoothTransferRequest other)'''
    def __eq__(self, other):
        '''bool QBluetoothTransferRequest.__eq__(QBluetoothTransferRequest other)'''
        return bool()
    def __ne__(self, other):
        '''bool QBluetoothTransferRequest.__ne__(QBluetoothTransferRequest other)'''
        return bool()
    def address(self):
        '''QBluetoothAddress QBluetoothTransferRequest.address()'''
        return QBluetoothAddress()
    def setAttribute(self, code, value):
        '''void QBluetoothTransferRequest.setAttribute(QBluetoothTransferRequest.Attribute code, QVariant value)'''
    def attribute(self, code, defaultValue = QVariant()):
        '''QVariant QBluetoothTransferRequest.attribute(QBluetoothTransferRequest.Attribute code, QVariant defaultValue = QVariant())'''
        return QVariant()


class QBluetoothUuid(QUuid):
    """"""
    # Enum QBluetoothUuid.DescriptorType
    UnknownDescriptorType = 0
    CharacteristicExtendedProperties = 0
    CharacteristicUserDescription = 0
    ClientCharacteristicConfiguration = 0
    ServerCharacteristicConfiguration = 0
    CharacteristicPresentationFormat = 0
    CharacteristicAggregateFormat = 0
    ValidRange = 0
    ExternalReportReference = 0
    ReportReference = 0
    EnvironmentalSensingConfiguration = 0
    EnvironmentalSensingMeasurement = 0
    EnvironmentalSensingTriggerSetting = 0

    # Enum QBluetoothUuid.CharacteristicType
    DeviceName = 0
    Appearance = 0
    PeripheralPrivacyFlag = 0
    ReconnectionAddress = 0
    PeripheralPreferredConnectionParameters = 0
    ServiceChanged = 0
    AlertLevel = 0
    TxPowerLevel = 0
    DateTime = 0
    DayOfWeek = 0
    DayDateTime = 0
    ExactTime256 = 0
    DSTOffset = 0
    TimeZone = 0
    LocalTimeInformation = 0
    TimeWithDST = 0
    TimeAccuracy = 0
    TimeSource = 0
    ReferenceTimeInformation = 0
    TimeUpdateControlPoint = 0
    TimeUpdateState = 0
    GlucoseMeasurement = 0
    BatteryLevel = 0
    TemperatureMeasurement = 0
    TemperatureType = 0
    IntermediateTemperature = 0
    MeasurementInterval = 0
    BootKeyboardInputReport = 0
    SystemID = 0
    ModelNumberString = 0
    SerialNumberString = 0
    FirmwareRevisionString = 0
    HardwareRevisionString = 0
    SoftwareRevisionString = 0
    ManufacturerNameString = 0
    IEEE1107320601RegulatoryCertificationDataList = 0
    CurrentTime = 0
    ScanRefresh = 0
    BootKeyboardOutputReport = 0
    BootMouseInputReport = 0
    GlucoseMeasurementContext = 0
    BloodPressureMeasurement = 0
    IntermediateCuffPressure = 0
    HeartRateMeasurement = 0
    BodySensorLocation = 0
    HeartRateControlPoint = 0
    AlertStatus = 0
    RingerControlPoint = 0
    RingerSetting = 0
    AlertCategoryIDBitMask = 0
    AlertCategoryID = 0
    AlertNotificationControlPoint = 0
    UnreadAlertStatus = 0
    NewAlert = 0
    SupportedNewAlertCategory = 0
    SupportedUnreadAlertCategory = 0
    BloodPressureFeature = 0
    HIDInformation = 0
    ReportMap = 0
    HIDControlPoint = 0
    Report = 0
    ProtocolMode = 0
    ScanIntervalWindow = 0
    PnPID = 0
    GlucoseFeature = 0
    RecordAccessControlPoint = 0
    RSCMeasurement = 0
    RSCFeature = 0
    SCControlPoint = 0
    CSCMeasurement = 0
    CSCFeature = 0
    SensorLocation = 0
    CyclingPowerMeasurement = 0
    CyclingPowerVector = 0
    CyclingPowerFeature = 0
    CyclingPowerControlPoint = 0
    LocationAndSpeed = 0
    Navigation = 0
    PositionQuality = 0
    LNFeature = 0
    LNControlPoint = 0
    MagneticDeclination = 0
    Elevation = 0
    Pressure = 0
    Temperature = 0
    Humidity = 0
    TrueWindSpeed = 0
    TrueWindDirection = 0
    ApparentWindSpeed = 0
    ApparentWindDirection = 0
    GustFactor = 0
    PollenConcentration = 0
    UVIndex = 0
    Irradiance = 0
    Rainfall = 0
    WindChill = 0
    HeatIndex = 0
    DewPoint = 0
    DescriptorValueChanged = 0
    AerobicHeartRateLowerLimit = 0
    AerobicThreshold = 0
    Age = 0
    AnaerobicHeartRateLowerLimit = 0
    AnaerobicHeartRateUpperLimit = 0
    AnaerobicThreshold = 0
    AerobicHeartRateUpperLimit = 0
    DateOfBirth = 0
    DateOfThresholdAssessment = 0
    EmailAddress = 0
    FatBurnHeartRateLowerLimit = 0
    FatBurnHeartRateUpperLimit = 0
    FirstName = 0
    FiveZoneHeartRateLimits = 0
    Gender = 0
    HeartRateMax = 0
    Height = 0
    HipCircumference = 0
    LastName = 0
    MaximumRecommendedHeartRate = 0
    RestingHeartRate = 0
    SportTypeForAerobicAnaerobicThresholds = 0
    ThreeZoneHeartRateLimits = 0
    TwoZoneHeartRateLimits = 0
    VO2Max = 0
    WaistCircumference = 0
    Weight = 0
    DatabaseChangeIncrement = 0
    UserIndex = 0
    BodyCompositionFeature = 0
    BodyCompositionMeasurement = 0
    WeightMeasurement = 0
    WeightScaleFeature = 0
    UserControlPoint = 0
    MagneticFluxDensity2D = 0
    MagneticFluxDensity3D = 0
    Language = 0
    BarometricPressureTrend = 0

    # Enum QBluetoothUuid.ServiceClassUuid
    ServiceDiscoveryServer = 0
    BrowseGroupDescriptor = 0
    PublicBrowseGroup = 0
    SerialPort = 0
    LANAccessUsingPPP = 0
    DialupNetworking = 0
    IrMCSync = 0
    ObexObjectPush = 0
    OBEXFileTransfer = 0
    IrMCSyncCommand = 0
    Headset = 0
    AudioSource = 0
    AudioSink = 0
    AV_RemoteControlTarget = 0
    AdvancedAudioDistribution = 0
    AV_RemoteControl = 0
    AV_RemoteControlController = 0
    HeadsetAG = 0
    PANU = 0
    NAP = 0
    GN = 0
    DirectPrinting = 0
    ReferencePrinting = 0
    ImagingResponder = 0
    ImagingAutomaticArchive = 0
    ImagingReferenceObjects = 0
    Handsfree = 0
    HandsfreeAudioGateway = 0
    DirectPrintingReferenceObjectsService = 0
    ReflectedUI = 0
    BasicPrinting = 0
    PrintingStatus = 0
    HumanInterfaceDeviceService = 0
    HardcopyCableReplacement = 0
    HCRPrint = 0
    HCRScan = 0
    SIMAccess = 0
    PhonebookAccessPCE = 0
    PhonebookAccessPSE = 0
    PhonebookAccess = 0
    HeadsetHS = 0
    MessageAccessServer = 0
    MessageNotificationServer = 0
    MessageAccessProfile = 0
    PnPInformation = 0
    GenericNetworking = 0
    GenericFileTransfer = 0
    GenericAudio = 0
    GenericTelephony = 0
    VideoSource = 0
    VideoSink = 0
    VideoDistribution = 0
    HDP = 0
    HDPSource = 0
    HDPSink = 0
    BasicImage = 0
    GNSS = 0
    GNSSServer = 0
    Display3D = 0
    Glasses3D = 0
    Synchronization3D = 0
    MPSProfile = 0
    MPSService = 0
    GenericAccess = 0
    GenericAttribute = 0
    ImmediateAlert = 0
    LinkLoss = 0
    TxPower = 0
    CurrentTimeService = 0
    ReferenceTimeUpdateService = 0
    NextDSTChangeService = 0
    Glucose = 0
    HealthThermometer = 0
    DeviceInformation = 0
    HeartRate = 0
    PhoneAlertStatusService = 0
    BatteryService = 0
    BloodPressure = 0
    AlertNotificationService = 0
    HumanInterfaceDevice = 0
    ScanParameters = 0
    RunningSpeedAndCadence = 0
    CyclingSpeedAndCadence = 0
    CyclingPower = 0
    LocationAndNavigation = 0
    EnvironmentalSensing = 0
    BodyComposition = 0
    UserData = 0
    WeightScale = 0
    BondManagement = 0
    ContinuousGlucoseMonitoring = 0

    # Enum QBluetoothUuid.ProtocolUuid
    Sdp = 0
    Udp = 0
    Rfcomm = 0
    Tcp = 0
    TcsBin = 0
    TcsAt = 0
    Att = 0
    Obex = 0
    Ip = 0
    Ftp = 0
    Http = 0
    Wsp = 0
    Bnep = 0
    Upnp = 0
    Hidp = 0
    HardcopyControlChannel = 0
    HardcopyDataChannel = 0
    HardcopyNotification = 0
    Avctp = 0
    Avdtp = 0
    Cmtp = 0
    UdiCPlain = 0
    McapControlChannel = 0
    McapDataChannel = 0
    L2cap = 0

    def __init__(self):
        '''void QBluetoothUuid.__init__()'''
    def __init__(self, uuid):
        '''void QBluetoothUuid.__init__(int uuid)'''
    def __init__(self, uuid):
        '''void QBluetoothUuid.__init__(16-tuple-of-int uuid)'''
    def __init__(self, uuid):
        '''void QBluetoothUuid.__init__(str uuid)'''
    def __init__(self, uuid):
        '''void QBluetoothUuid.__init__(QBluetoothUuid uuid)'''
    def __init__(self, uuid):
        '''void QBluetoothUuid.__init__(QUuid uuid)'''
    def __ne__(self, other):
        '''bool QBluetoothUuid.__ne__(QBluetoothUuid other)'''
        return bool()
    def descriptorToString(self, uuid):
        '''static str QBluetoothUuid.descriptorToString(QBluetoothUuid.DescriptorType uuid)'''
        return str()
    def characteristicToString(self, uuid):
        '''static str QBluetoothUuid.characteristicToString(QBluetoothUuid.CharacteristicType uuid)'''
        return str()
    def protocolToString(self, uuid):
        '''static str QBluetoothUuid.protocolToString(QBluetoothUuid.ProtocolUuid uuid)'''
        return str()
    def serviceClassToString(self, uuid):
        '''static str QBluetoothUuid.serviceClassToString(QBluetoothUuid.ServiceClassUuid uuid)'''
        return str()
    def toUInt128(self):
        '''16-tuple-of-int QBluetoothUuid.toUInt128()'''
        return 16-tuple-of-int()
    def toUInt32(self, ok):
        '''int QBluetoothUuid.toUInt32(bool ok)'''
        return int()
    def toUInt16(self, ok):
        '''int QBluetoothUuid.toUInt16(bool ok)'''
        return int()
    def minimumSize(self):
        '''int QBluetoothUuid.minimumSize()'''
        return int()
    def __eq__(self, other):
        '''bool QBluetoothUuid.__eq__(QBluetoothUuid other)'''
        return bool()


class QLowEnergyCharacteristic():
    """"""
    # Enum QLowEnergyCharacteristic.PropertyType
    Unknown = 0
    Broadcasting = 0
    Read = 0
    WriteNoResponse = 0
    Write = 0
    Notify = 0
    Indicate = 0
    WriteSigned = 0
    ExtendedProperty = 0

    def __init__(self):
        '''void QLowEnergyCharacteristic.__init__()'''
    def __init__(self, other):
        '''void QLowEnergyCharacteristic.__init__(QLowEnergyCharacteristic other)'''
    def isValid(self):
        '''bool QLowEnergyCharacteristic.isValid()'''
        return bool()
    def descriptors(self):
        '''list-of-QLowEnergyDescriptor QLowEnergyCharacteristic.descriptors()'''
        return [QLowEnergyDescriptor()]
    def descriptor(self, uuid):
        '''QLowEnergyDescriptor QLowEnergyCharacteristic.descriptor(QBluetoothUuid uuid)'''
        return QLowEnergyDescriptor()
    def handle(self):
        '''int QLowEnergyCharacteristic.handle()'''
        return int()
    def properties(self):
        '''QLowEnergyCharacteristic.PropertyTypes QLowEnergyCharacteristic.properties()'''
        return QLowEnergyCharacteristic.PropertyTypes()
    def value(self):
        '''QByteArray QLowEnergyCharacteristic.value()'''
        return QByteArray()
    def uuid(self):
        '''QBluetoothUuid QLowEnergyCharacteristic.uuid()'''
        return QBluetoothUuid()
    def name(self):
        '''str QLowEnergyCharacteristic.name()'''
        return str()
    def __ne__(self, other):
        '''bool QLowEnergyCharacteristic.__ne__(QLowEnergyCharacteristic other)'''
        return bool()
    def __eq__(self, other):
        '''bool QLowEnergyCharacteristic.__eq__(QLowEnergyCharacteristic other)'''
        return bool()
    class PropertyTypes():
        """"""
        def __init__(self):
            '''QLowEnergyCharacteristic.PropertyTypes QLowEnergyCharacteristic.PropertyTypes.__init__()'''
            return QLowEnergyCharacteristic.PropertyTypes()
        def __init__(self):
            '''int QLowEnergyCharacteristic.PropertyTypes.__init__()'''
            return int()
        def __init__(self):
            '''void QLowEnergyCharacteristic.PropertyTypes.__init__()'''
        def __bool__(self):
            '''int QLowEnergyCharacteristic.PropertyTypes.__bool__()'''
            return int()
        def __ne__(self, f):
            '''bool QLowEnergyCharacteristic.PropertyTypes.__ne__(QLowEnergyCharacteristic.PropertyTypes f)'''
            return bool()
        def __eq__(self, f):
            '''bool QLowEnergyCharacteristic.PropertyTypes.__eq__(QLowEnergyCharacteristic.PropertyTypes f)'''
            return bool()
        def __invert__(self):
            '''QLowEnergyCharacteristic.PropertyTypes QLowEnergyCharacteristic.PropertyTypes.__invert__()'''
            return QLowEnergyCharacteristic.PropertyTypes()
        def __and__(self, mask):
            '''QLowEnergyCharacteristic.PropertyTypes QLowEnergyCharacteristic.PropertyTypes.__and__(int mask)'''
            return QLowEnergyCharacteristic.PropertyTypes()
        def __xor__(self, f):
            '''QLowEnergyCharacteristic.PropertyTypes QLowEnergyCharacteristic.PropertyTypes.__xor__(QLowEnergyCharacteristic.PropertyTypes f)'''
            return QLowEnergyCharacteristic.PropertyTypes()
        def __xor__(self, f):
            '''QLowEnergyCharacteristic.PropertyTypes QLowEnergyCharacteristic.PropertyTypes.__xor__(int f)'''
            return QLowEnergyCharacteristic.PropertyTypes()
        def __or__(self, f):
            '''QLowEnergyCharacteristic.PropertyTypes QLowEnergyCharacteristic.PropertyTypes.__or__(QLowEnergyCharacteristic.PropertyTypes f)'''
            return QLowEnergyCharacteristic.PropertyTypes()
        def __or__(self, f):
            '''QLowEnergyCharacteristic.PropertyTypes QLowEnergyCharacteristic.PropertyTypes.__or__(int f)'''
            return QLowEnergyCharacteristic.PropertyTypes()
        def __int__(self):
            '''int QLowEnergyCharacteristic.PropertyTypes.__int__()'''
            return int()
        def __ixor__(self, f):
            '''QLowEnergyCharacteristic.PropertyTypes QLowEnergyCharacteristic.PropertyTypes.__ixor__(QLowEnergyCharacteristic.PropertyTypes f)'''
            return QLowEnergyCharacteristic.PropertyTypes()
        def __ior__(self, f):
            '''QLowEnergyCharacteristic.PropertyTypes QLowEnergyCharacteristic.PropertyTypes.__ior__(QLowEnergyCharacteristic.PropertyTypes f)'''
            return QLowEnergyCharacteristic.PropertyTypes()
        def __iand__(self, mask):
            '''QLowEnergyCharacteristic.PropertyTypes QLowEnergyCharacteristic.PropertyTypes.__iand__(int mask)'''
            return QLowEnergyCharacteristic.PropertyTypes()


class QLowEnergyController(QObject):
    """"""
    # Enum QLowEnergyController.RemoteAddressType
    PublicAddress = 0
    RandomAddress = 0

    # Enum QLowEnergyController.ControllerState
    UnconnectedState = 0
    ConnectingState = 0
    ConnectedState = 0
    DiscoveringState = 0
    DiscoveredState = 0
    ClosingState = 0

    # Enum QLowEnergyController.Error
    NoError = 0
    UnknownError = 0
    UnknownRemoteDeviceError = 0
    NetworkError = 0
    InvalidBluetoothAdapterError = 0
    ConnectionError = 0

    def __init__(self, remoteDevice, parent = None):
        '''void QLowEnergyController.__init__(QBluetoothDeviceInfo remoteDevice, QObject parent = None)'''
    def __init__(self, remoteDevice, parent = None):
        '''void QLowEnergyController.__init__(QBluetoothAddress remoteDevice, QObject parent = None)'''
    def __init__(self, remoteDevice, localDevice, parent = None):
        '''void QLowEnergyController.__init__(QBluetoothAddress remoteDevice, QBluetoothAddress localDevice, QObject parent = None)'''
    discoveryFinished = pyqtSignal() # void discoveryFinished() - signal
    serviceDiscovered = pyqtSignal() # void serviceDiscovered(const QBluetoothUuidamp;) - signal
    stateChanged = pyqtSignal() # void stateChanged(QLowEnergyController::ControllerState) - signal
    disconnected = pyqtSignal() # void disconnected() - signal
    connected = pyqtSignal() # void connected() - signal
    def remoteName(self):
        '''str QLowEnergyController.remoteName()'''
        return str()
    def errorString(self):
        '''str QLowEnergyController.errorString()'''
        return str()
    def error(self):
        '''QLowEnergyController.Error QLowEnergyController.error()'''
        return QLowEnergyController.Error()
    error = pyqtSignal() # void error(QLowEnergyController::Error) - signal
    def createServiceObject(self, service, parent = None):
        '''QLowEnergyService QLowEnergyController.createServiceObject(QBluetoothUuid service, QObject parent = None)'''
        return QLowEnergyService()
    def services(self):
        '''list-of-QBluetoothUuid QLowEnergyController.services()'''
        return [QBluetoothUuid()]
    def discoverServices(self):
        '''void QLowEnergyController.discoverServices()'''
    def disconnectFromDevice(self):
        '''void QLowEnergyController.disconnectFromDevice()'''
    def connectToDevice(self):
        '''void QLowEnergyController.connectToDevice()'''
    def setRemoteAddressType(self, type):
        '''void QLowEnergyController.setRemoteAddressType(QLowEnergyController.RemoteAddressType type)'''
    def remoteAddressType(self):
        '''QLowEnergyController.RemoteAddressType QLowEnergyController.remoteAddressType()'''
        return QLowEnergyController.RemoteAddressType()
    def state(self):
        '''QLowEnergyController.ControllerState QLowEnergyController.state()'''
        return QLowEnergyController.ControllerState()
    def remoteAddress(self):
        '''QBluetoothAddress QLowEnergyController.remoteAddress()'''
        return QBluetoothAddress()
    def localAddress(self):
        '''QBluetoothAddress QLowEnergyController.localAddress()'''
        return QBluetoothAddress()


class QLowEnergyDescriptor():
    """"""
    def __init__(self):
        '''void QLowEnergyDescriptor.__init__()'''
    def __init__(self, other):
        '''void QLowEnergyDescriptor.__init__(QLowEnergyDescriptor other)'''
    def type(self):
        '''QBluetoothUuid.DescriptorType QLowEnergyDescriptor.type()'''
        return QBluetoothUuid.DescriptorType()
    def name(self):
        '''str QLowEnergyDescriptor.name()'''
        return str()
    def handle(self):
        '''int QLowEnergyDescriptor.handle()'''
        return int()
    def uuid(self):
        '''QBluetoothUuid QLowEnergyDescriptor.uuid()'''
        return QBluetoothUuid()
    def value(self):
        '''QByteArray QLowEnergyDescriptor.value()'''
        return QByteArray()
    def isValid(self):
        '''bool QLowEnergyDescriptor.isValid()'''
        return bool()
    def __ne__(self, other):
        '''bool QLowEnergyDescriptor.__ne__(QLowEnergyDescriptor other)'''
        return bool()
    def __eq__(self, other):
        '''bool QLowEnergyDescriptor.__eq__(QLowEnergyDescriptor other)'''
        return bool()


class QLowEnergyService(QObject):
    """"""
    # Enum QLowEnergyService.WriteMode
    WriteWithResponse = 0
    WriteWithoutResponse = 0

    # Enum QLowEnergyService.ServiceState
    InvalidService = 0
    DiscoveryRequired = 0
    DiscoveringServices = 0
    ServiceDiscovered = 0

    # Enum QLowEnergyService.ServiceError
    NoError = 0
    OperationError = 0
    CharacteristicWriteError = 0
    DescriptorWriteError = 0
    CharacteristicReadError = 0
    DescriptorReadError = 0
    UnknownError = 0

    # Enum QLowEnergyService.ServiceType
    PrimaryService = 0
    IncludedService = 0

    descriptorRead = pyqtSignal() # void descriptorRead(const QLowEnergyDescriptoramp;,const QByteArrayamp;) - signal
    characteristicRead = pyqtSignal() # void characteristicRead(const QLowEnergyCharacteristicamp;,const QByteArrayamp;) - signal
    def readDescriptor(self, descriptor):
        '''void QLowEnergyService.readDescriptor(QLowEnergyDescriptor descriptor)'''
    def readCharacteristic(self, characteristic):
        '''void QLowEnergyService.readCharacteristic(QLowEnergyCharacteristic characteristic)'''
    descriptorWritten = pyqtSignal() # void descriptorWritten(const QLowEnergyDescriptoramp;,const QByteArrayamp;) - signal
    characteristicWritten = pyqtSignal() # void characteristicWritten(const QLowEnergyCharacteristicamp;,const QByteArrayamp;) - signal
    characteristicChanged = pyqtSignal() # void characteristicChanged(const QLowEnergyCharacteristicamp;,const QByteArrayamp;) - signal
    stateChanged = pyqtSignal() # void stateChanged(QLowEnergyService::ServiceState) - signal
    def writeDescriptor(self, descriptor, newValue):
        '''void QLowEnergyService.writeDescriptor(QLowEnergyDescriptor descriptor, QByteArray newValue)'''
    def writeCharacteristic(self, characteristic, newValue, mode = None):
        '''void QLowEnergyService.writeCharacteristic(QLowEnergyCharacteristic characteristic, QByteArray newValue, QLowEnergyService.WriteMode mode = QLowEnergyService.WriteWithResponse)'''
    def contains(self, characteristic):
        '''bool QLowEnergyService.contains(QLowEnergyCharacteristic characteristic)'''
        return bool()
    def contains(self, descriptor):
        '''bool QLowEnergyService.contains(QLowEnergyDescriptor descriptor)'''
        return bool()
    def error(self):
        '''QLowEnergyService.ServiceError QLowEnergyService.error()'''
        return QLowEnergyService.ServiceError()
    error = pyqtSignal() # void error(QLowEnergyService::ServiceError) - signal
    def discoverDetails(self):
        '''void QLowEnergyService.discoverDetails()'''
    def serviceName(self):
        '''str QLowEnergyService.serviceName()'''
        return str()
    def serviceUuid(self):
        '''QBluetoothUuid QLowEnergyService.serviceUuid()'''
        return QBluetoothUuid()
    def characteristics(self):
        '''list-of-QLowEnergyCharacteristic QLowEnergyService.characteristics()'''
        return [QLowEnergyCharacteristic()]
    def characteristic(self, uuid):
        '''QLowEnergyCharacteristic QLowEnergyService.characteristic(QBluetoothUuid uuid)'''
        return QLowEnergyCharacteristic()
    def state(self):
        '''QLowEnergyService.ServiceState QLowEnergyService.state()'''
        return QLowEnergyService.ServiceState()
    def type(self):
        '''QLowEnergyService.ServiceTypes QLowEnergyService.type()'''
        return QLowEnergyService.ServiceTypes()
    def includedServices(self):
        '''list-of-QBluetoothUuid QLowEnergyService.includedServices()'''
        return [QBluetoothUuid()]
    class ServiceTypes():
        """"""
        def __init__(self):
            '''QLowEnergyService.ServiceTypes QLowEnergyService.ServiceTypes.__init__()'''
            return QLowEnergyService.ServiceTypes()
        def __init__(self):
            '''int QLowEnergyService.ServiceTypes.__init__()'''
            return int()
        def __init__(self):
            '''void QLowEnergyService.ServiceTypes.__init__()'''
        def __bool__(self):
            '''int QLowEnergyService.ServiceTypes.__bool__()'''
            return int()
        def __ne__(self, f):
            '''bool QLowEnergyService.ServiceTypes.__ne__(QLowEnergyService.ServiceTypes f)'''
            return bool()
        def __eq__(self, f):
            '''bool QLowEnergyService.ServiceTypes.__eq__(QLowEnergyService.ServiceTypes f)'''
            return bool()
        def __invert__(self):
            '''QLowEnergyService.ServiceTypes QLowEnergyService.ServiceTypes.__invert__()'''
            return QLowEnergyService.ServiceTypes()
        def __and__(self, mask):
            '''QLowEnergyService.ServiceTypes QLowEnergyService.ServiceTypes.__and__(int mask)'''
            return QLowEnergyService.ServiceTypes()
        def __xor__(self, f):
            '''QLowEnergyService.ServiceTypes QLowEnergyService.ServiceTypes.__xor__(QLowEnergyService.ServiceTypes f)'''
            return QLowEnergyService.ServiceTypes()
        def __xor__(self, f):
            '''QLowEnergyService.ServiceTypes QLowEnergyService.ServiceTypes.__xor__(int f)'''
            return QLowEnergyService.ServiceTypes()
        def __or__(self, f):
            '''QLowEnergyService.ServiceTypes QLowEnergyService.ServiceTypes.__or__(QLowEnergyService.ServiceTypes f)'''
            return QLowEnergyService.ServiceTypes()
        def __or__(self, f):
            '''QLowEnergyService.ServiceTypes QLowEnergyService.ServiceTypes.__or__(int f)'''
            return QLowEnergyService.ServiceTypes()
        def __int__(self):
            '''int QLowEnergyService.ServiceTypes.__int__()'''
            return int()
        def __ixor__(self, f):
            '''QLowEnergyService.ServiceTypes QLowEnergyService.ServiceTypes.__ixor__(QLowEnergyService.ServiceTypes f)'''
            return QLowEnergyService.ServiceTypes()
        def __ior__(self, f):
            '''QLowEnergyService.ServiceTypes QLowEnergyService.ServiceTypes.__ior__(QLowEnergyService.ServiceTypes f)'''
            return QLowEnergyService.ServiceTypes()
        def __iand__(self, mask):
            '''QLowEnergyService.ServiceTypes QLowEnergyService.ServiceTypes.__iand__(int mask)'''
            return QLowEnergyService.ServiceTypes()


