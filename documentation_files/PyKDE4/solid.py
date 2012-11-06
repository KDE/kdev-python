class pyqtSignal():
 def connect(self, targetSignal): pass
 def emit(self, *args): pass
from QtCore import *

class Solid():
    """"""
    # Enum Solid.ErrorType
    NoError = 0
    UnauthorizedOperation = 0
    DeviceBusy = 0
    OperationFailed = 0
    UserCanceled = 0
    InvalidOption = 0
    MissingDriver = 0

    class Processor(Solid.DeviceInterface):
        """"""
        # Enum Solid.Processor.InstructionSet
        NoExtensions = 0
        IntelMmx = 0
        IntelSse = 0
        IntelSse2 = 0
        IntelSse3 = 0
        IntelSse4 = 0
        Amd3DNow = 0
        AltiVec = 0
    
        def instructionSets(self):
            '''Solid.Processor.InstructionSets Solid.Processor.instructionSets()'''
            return Solid.Processor.InstructionSets()
        def canChangeFrequency(self):
            '''bool Solid.Processor.canChangeFrequency()'''
            return bool()
        def maxSpeed(self):
            '''int Solid.Processor.maxSpeed()'''
            return int()
        def number(self):
            '''int Solid.Processor.number()'''
            return int()
        def deviceInterfaceType(self):
            '''static Solid.DeviceInterface.Type Solid.Processor.deviceInterfaceType()'''
            return Solid.DeviceInterface.Type()
    class StorageDrive(Solid.DeviceInterface):
        """"""
        # Enum Solid.StorageDrive.DriveType
        HardDisk = 0
        CdromDrive = 0
        Floppy = 0
        Tape = 0
        CompactFlash = 0
        MemoryStick = 0
        SmartMedia = 0
        SdMmc = 0
        Xd = 0
    
        # Enum Solid.StorageDrive.Bus
        Ide = 0
        Usb = 0
        Ieee1394 = 0
        Scsi = 0
        Sata = 0
        Platform = 0
    
        def isInUse(self):
            '''bool Solid.StorageDrive.isInUse()'''
            return bool()
        def size(self):
            '''int Solid.StorageDrive.size()'''
            return int()
        def isHotpluggable(self):
            '''bool Solid.StorageDrive.isHotpluggable()'''
            return bool()
        def isRemovable(self):
            '''bool Solid.StorageDrive.isRemovable()'''
            return bool()
        def driveType(self):
            '''Solid.StorageDrive.DriveType Solid.StorageDrive.driveType()'''
            return Solid.StorageDrive.DriveType()
        def bus(self):
            '''Solid.StorageDrive.Bus Solid.StorageDrive.bus()'''
            return Solid.StorageDrive.Bus()
        def deviceInterfaceType(self):
            '''static Solid.DeviceInterface.Type Solid.StorageDrive.deviceInterfaceType()'''
            return Solid.DeviceInterface.Type()
    class Video(Solid.DeviceInterface):
        """"""
        def driverHandle(self, driver):
            '''QVariant Solid.Video.driverHandle(QString driver)'''
            return QVariant()
        def supportedDrivers(self, protocol = QString()):
            '''QStringList Solid.Video.supportedDrivers(QString protocol = QString())'''
            return QStringList()
        def supportedProtocols(self):
            '''QStringList Solid.Video.supportedProtocols()'''
            return QStringList()
        def deviceInterfaceType(self):
            '''static Solid.DeviceInterface.Type Solid.Video.deviceInterfaceType()'''
            return Solid.DeviceInterface.Type()
    class OpticalDrive(Solid.StorageDrive):
        """"""
        # Enum Solid.OpticalDrive.MediumType
        Cdr = 0
        Cdrw = 0
        Dvd = 0
        Dvdr = 0
        Dvdrw = 0
        Dvdram = 0
        Dvdplusr = 0
        Dvdplusrw = 0
        Dvdplusdl = 0
        Dvdplusdlrw = 0
        Bd = 0
        Bdr = 0
        Bdre = 0
        HdDvd = 0
        HdDvdr = 0
        HdDvdrw = 0
    
        ejectRequested = pyqtSignal() # void ejectRequested(const QStringamp;) - signal
        ejectDone = pyqtSignal() # void ejectDone(Solid::ErrorType,QVariant,const QStringamp;) - signal
        ejectPressed = pyqtSignal() # void ejectPressed(const QStringamp;) - signal
        def eject(self):
            '''bool Solid.OpticalDrive.eject()'''
            return bool()
        def writeSpeeds(self):
            '''list-of-int Solid.OpticalDrive.writeSpeeds()'''
            return [int()]
        def writeSpeed(self):
            '''int Solid.OpticalDrive.writeSpeed()'''
            return int()
        def readSpeed(self):
            '''int Solid.OpticalDrive.readSpeed()'''
            return int()
        def supportedMedia(self):
            '''Solid.OpticalDrive.MediumTypes Solid.OpticalDrive.supportedMedia()'''
            return Solid.OpticalDrive.MediumTypes()
        def deviceInterfaceType(self):
            '''static Solid.DeviceInterface.Type Solid.OpticalDrive.deviceInterfaceType()'''
            return Solid.DeviceInterface.Type()
    class SmartCardReader(Solid.DeviceInterface):
        """"""
        # Enum Solid.SmartCardReader.ReaderType
        UnknownReaderType = 0
        CardReader = 0
        CryptoToken = 0
    
        def readerType(self):
            '''Solid.SmartCardReader.ReaderType Solid.SmartCardReader.readerType()'''
            return Solid.SmartCardReader.ReaderType()
        def deviceInterfaceType(self):
            '''static Solid.DeviceInterface.Type Solid.SmartCardReader.deviceInterfaceType()'''
            return Solid.DeviceInterface.Type()
    class AcAdapter(Solid.DeviceInterface):
        """"""
        plugStateChanged = pyqtSignal() # void plugStateChanged(bool,const QStringamp;) - signal
        def isPlugged(self):
            '''bool Solid.AcAdapter.isPlugged()'''
            return bool()
        def deviceInterfaceType(self):
            '''static Solid.DeviceInterface.Type Solid.AcAdapter.deviceInterfaceType()'''
            return Solid.DeviceInterface.Type()
    class NetworkShare(Solid.DeviceInterface):
        """"""
        # Enum Solid.NetworkShare.ShareType
        Unknown = 0
        Nfs = 0
        Cifs = 0
        Upnp = 0
    
        def url(self):
            '''QUrl Solid.NetworkShare.url()'''
            return QUrl()
        def type(self):
            '''Solid.NetworkShare.ShareType Solid.NetworkShare.type()'''
            return Solid.NetworkShare.ShareType()
        def deviceInterfaceType(self):
            '''static Solid.DeviceInterface.Type Solid.NetworkShare.deviceInterfaceType()'''
            return Solid.DeviceInterface.Type()
    class StorageVolume(Solid.DeviceInterface):
        """"""
        # Enum Solid.StorageVolume.UsageType
        Other = 0
        Unused = 0
        FileSystem = 0
        PartitionTable = 0
        Raid = 0
        Encrypted = 0
    
        def encryptedContainer(self):
            '''Solid.Device Solid.StorageVolume.encryptedContainer()'''
            return Solid.Device()
        def size(self):
            '''int Solid.StorageVolume.size()'''
            return int()
        def uuid(self):
            '''QString Solid.StorageVolume.uuid()'''
            return QString()
        def label(self):
            '''QString Solid.StorageVolume.label()'''
            return QString()
        def fsType(self):
            '''QString Solid.StorageVolume.fsType()'''
            return QString()
        def usage(self):
            '''Solid.StorageVolume.UsageType Solid.StorageVolume.usage()'''
            return Solid.StorageVolume.UsageType()
        def isIgnored(self):
            '''bool Solid.StorageVolume.isIgnored()'''
            return bool()
        def deviceInterfaceType(self):
            '''static Solid.DeviceInterface.Type Solid.StorageVolume.deviceInterfaceType()'''
            return Solid.DeviceInterface.Type()
    class OpticalDisc():
        """"""
        class ContentTypes():
            """"""
            def __init__(self):
                '''Solid.OpticalDisc.ContentTypes Solid.OpticalDisc.ContentTypes.__init__()'''
                return Solid.OpticalDisc.ContentTypes()
            def __init__(self):
                '''int Solid.OpticalDisc.ContentTypes.__init__()'''
                return int()
            def __init__(self):
                '''void Solid.OpticalDisc.ContentTypes.__init__()'''
            def __bool__(self):
                '''int Solid.OpticalDisc.ContentTypes.__bool__()'''
                return int()
            def __ne__(self, f):
                '''bool Solid.OpticalDisc.ContentTypes.__ne__(Solid.OpticalDisc.ContentTypes f)'''
                return bool()
            def __eq__(self, f):
                '''bool Solid.OpticalDisc.ContentTypes.__eq__(Solid.OpticalDisc.ContentTypes f)'''
                return bool()
            def __invert__(self):
                '''Solid.OpticalDisc.ContentTypes Solid.OpticalDisc.ContentTypes.__invert__()'''
                return Solid.OpticalDisc.ContentTypes()
            def __and__(self, mask):
                '''Solid.OpticalDisc.ContentTypes Solid.OpticalDisc.ContentTypes.__and__(int mask)'''
                return Solid.OpticalDisc.ContentTypes()
            def __xor__(self, f):
                '''Solid.OpticalDisc.ContentTypes Solid.OpticalDisc.ContentTypes.__xor__(Solid.OpticalDisc.ContentTypes f)'''
                return Solid.OpticalDisc.ContentTypes()
            def __xor__(self, f):
                '''Solid.OpticalDisc.ContentTypes Solid.OpticalDisc.ContentTypes.__xor__(int f)'''
                return Solid.OpticalDisc.ContentTypes()
            def __or__(self, f):
                '''Solid.OpticalDisc.ContentTypes Solid.OpticalDisc.ContentTypes.__or__(Solid.OpticalDisc.ContentTypes f)'''
                return Solid.OpticalDisc.ContentTypes()
            def __or__(self, f):
                '''Solid.OpticalDisc.ContentTypes Solid.OpticalDisc.ContentTypes.__or__(int f)'''
                return Solid.OpticalDisc.ContentTypes()
            def __int__(self):
                '''int Solid.OpticalDisc.ContentTypes.__int__()'''
                return int()
            def __ixor__(self, f):
                '''Solid.OpticalDisc.ContentTypes Solid.OpticalDisc.ContentTypes.__ixor__(Solid.OpticalDisc.ContentTypes f)'''
                return Solid.OpticalDisc.ContentTypes()
            def __ior__(self, f):
                '''Solid.OpticalDisc.ContentTypes Solid.OpticalDisc.ContentTypes.__ior__(Solid.OpticalDisc.ContentTypes f)'''
                return Solid.OpticalDisc.ContentTypes()
            def __iand__(self, mask):
                '''Solid.OpticalDisc.ContentTypes Solid.OpticalDisc.ContentTypes.__iand__(int mask)'''
                return Solid.OpticalDisc.ContentTypes()
    class OpticalDisc(Solid.StorageVolume):
        """"""
        # Enum Solid.OpticalDisc.DiscType
        UnknownDiscType = 0
        CdRom = 0
        CdRecordable = 0
        CdRewritable = 0
        DvdRom = 0
        DvdRam = 0
        DvdRecordable = 0
        DvdRewritable = 0
        DvdPlusRecordable = 0
        DvdPlusRewritable = 0
        DvdPlusRecordableDuallayer = 0
        DvdPlusRewritableDuallayer = 0
        BluRayRom = 0
        BluRayRecordable = 0
        BluRayRewritable = 0
        HdDvdRom = 0
        HdDvdRecordable = 0
        HdDvdRewritable = 0
    
        # Enum Solid.OpticalDisc.ContentType
        NoContent = 0
        Audio = 0
        Data = 0
        VideoCd = 0
        SuperVideoCd = 0
        VideoDvd = 0
        VideoBluRay = 0
    
        def capacity(self):
            '''int Solid.OpticalDisc.capacity()'''
            return int()
        def isRewritable(self):
            '''bool Solid.OpticalDisc.isRewritable()'''
            return bool()
        def isBlank(self):
            '''bool Solid.OpticalDisc.isBlank()'''
            return bool()
        def isAppendable(self):
            '''bool Solid.OpticalDisc.isAppendable()'''
            return bool()
        def discType(self):
            '''Solid.OpticalDisc.DiscType Solid.OpticalDisc.discType()'''
            return Solid.OpticalDisc.DiscType()
        def availableContent(self):
            '''Solid.OpticalDisc.ContentTypes Solid.OpticalDisc.availableContent()'''
            return Solid.OpticalDisc.ContentTypes()
        def deviceInterfaceType(self):
            '''static Solid.DeviceInterface.Type Solid.OpticalDisc.deviceInterfaceType()'''
            return Solid.DeviceInterface.Type()
    class Block(Solid.DeviceInterface):
        """"""
        def device(self):
            '''QString Solid.Block.device()'''
            return QString()
        def deviceMinor(self):
            '''int Solid.Block.deviceMinor()'''
            return int()
        def deviceMajor(self):
            '''int Solid.Block.deviceMajor()'''
            return int()
        def deviceInterfaceType(self):
            '''static Solid.DeviceInterface.Type Solid.Block.deviceInterfaceType()'''
            return Solid.DeviceInterface.Type()
    class Networking():
        """"""
        class Notifier(QObject):
            """"""
            def __init__(self):
                '''void Solid.Networking.Notifier.__init__()'''
    class AudioInterface():
        """"""
        class AudioInterfaceTypes():
            """"""
            def __init__(self):
                '''Solid.AudioInterface.AudioInterfaceTypes Solid.AudioInterface.AudioInterfaceTypes.__init__()'''
                return Solid.AudioInterface.AudioInterfaceTypes()
            def __init__(self):
                '''int Solid.AudioInterface.AudioInterfaceTypes.__init__()'''
                return int()
            def __init__(self):
                '''void Solid.AudioInterface.AudioInterfaceTypes.__init__()'''
            def __bool__(self):
                '''int Solid.AudioInterface.AudioInterfaceTypes.__bool__()'''
                return int()
            def __ne__(self, f):
                '''bool Solid.AudioInterface.AudioInterfaceTypes.__ne__(Solid.AudioInterface.AudioInterfaceTypes f)'''
                return bool()
            def __eq__(self, f):
                '''bool Solid.AudioInterface.AudioInterfaceTypes.__eq__(Solid.AudioInterface.AudioInterfaceTypes f)'''
                return bool()
            def __invert__(self):
                '''Solid.AudioInterface.AudioInterfaceTypes Solid.AudioInterface.AudioInterfaceTypes.__invert__()'''
                return Solid.AudioInterface.AudioInterfaceTypes()
            def __and__(self, mask):
                '''Solid.AudioInterface.AudioInterfaceTypes Solid.AudioInterface.AudioInterfaceTypes.__and__(int mask)'''
                return Solid.AudioInterface.AudioInterfaceTypes()
            def __xor__(self, f):
                '''Solid.AudioInterface.AudioInterfaceTypes Solid.AudioInterface.AudioInterfaceTypes.__xor__(Solid.AudioInterface.AudioInterfaceTypes f)'''
                return Solid.AudioInterface.AudioInterfaceTypes()
            def __xor__(self, f):
                '''Solid.AudioInterface.AudioInterfaceTypes Solid.AudioInterface.AudioInterfaceTypes.__xor__(int f)'''
                return Solid.AudioInterface.AudioInterfaceTypes()
            def __or__(self, f):
                '''Solid.AudioInterface.AudioInterfaceTypes Solid.AudioInterface.AudioInterfaceTypes.__or__(Solid.AudioInterface.AudioInterfaceTypes f)'''
                return Solid.AudioInterface.AudioInterfaceTypes()
            def __or__(self, f):
                '''Solid.AudioInterface.AudioInterfaceTypes Solid.AudioInterface.AudioInterfaceTypes.__or__(int f)'''
                return Solid.AudioInterface.AudioInterfaceTypes()
            def __int__(self):
                '''int Solid.AudioInterface.AudioInterfaceTypes.__int__()'''
                return int()
            def __ixor__(self, f):
                '''Solid.AudioInterface.AudioInterfaceTypes Solid.AudioInterface.AudioInterfaceTypes.__ixor__(Solid.AudioInterface.AudioInterfaceTypes f)'''
                return Solid.AudioInterface.AudioInterfaceTypes()
            def __ior__(self, f):
                '''Solid.AudioInterface.AudioInterfaceTypes Solid.AudioInterface.AudioInterfaceTypes.__ior__(Solid.AudioInterface.AudioInterfaceTypes f)'''
                return Solid.AudioInterface.AudioInterfaceTypes()
            def __iand__(self, mask):
                '''Solid.AudioInterface.AudioInterfaceTypes Solid.AudioInterface.AudioInterfaceTypes.__iand__(int mask)'''
                return Solid.AudioInterface.AudioInterfaceTypes()
    class Battery(Solid.DeviceInterface):
        """"""
        # Enum Solid.Battery.ChargeState
        NoCharge = 0
        Charging = 0
        Discharging = 0
    
        # Enum Solid.Battery.BatteryType
        UnknownBattery = 0
        PdaBattery = 0
        UpsBattery = 0
        PrimaryBattery = 0
        MouseBattery = 0
        KeyboardBattery = 0
        KeyboardMouseBattery = 0
        CameraBattery = 0
        PhoneBattery = 0
        MonitorBattery = 0
    
        plugStateChanged = pyqtSignal() # void plugStateChanged(bool,const QStringamp;) - signal
        chargeStateChanged = pyqtSignal() # void chargeStateChanged(int,const QStringamp;) - signal
        chargePercentChanged = pyqtSignal() # void chargePercentChanged(int,const QStringamp;) - signal
        def chargeState(self):
            '''Solid.Battery.ChargeState Solid.Battery.chargeState()'''
            return Solid.Battery.ChargeState()
        def isRechargeable(self):
            '''bool Solid.Battery.isRechargeable()'''
            return bool()
        def chargePercent(self):
            '''int Solid.Battery.chargePercent()'''
            return int()
        def type(self):
            '''Solid.Battery.BatteryType Solid.Battery.type()'''
            return Solid.Battery.BatteryType()
        def isPlugged(self):
            '''bool Solid.Battery.isPlugged()'''
            return bool()
        def deviceInterfaceType(self):
            '''static Solid.DeviceInterface.Type Solid.Battery.deviceInterfaceType()'''
            return Solid.DeviceInterface.Type()
    class Networking():
        """"""
        # Enum Solid.Networking.ManagementPolicy
        Manual = 0
        OnNextStatusChange = 0
        Managed = 0
    
        # Enum Solid.Networking.Status
        Unknown = 0
        Unconnected = 0
        Disconnecting = 0
        Connecting = 0
        Connected = 0
    
        def notifier(self):
            '''static Solid.Networking.Notifier Solid.Networking.notifier()'''
            return Solid.Networking.Notifier()
        def status(self):
            '''static Solid.Networking.Status Solid.Networking.status()'''
            return Solid.Networking.Status()
    class Camera(Solid.DeviceInterface):
        """"""
        def driverHandle(self, driver):
            '''QVariant Solid.Camera.driverHandle(QString driver)'''
            return QVariant()
        def supportedDrivers(self, protocol = QString()):
            '''QStringList Solid.Camera.supportedDrivers(QString protocol = QString())'''
            return QStringList()
        def supportedProtocols(self):
            '''QStringList Solid.Camera.supportedProtocols()'''
            return QStringList()
        def deviceInterfaceType(self):
            '''static Solid.DeviceInterface.Type Solid.Camera.deviceInterfaceType()'''
            return Solid.DeviceInterface.Type()
    class InternetGateway(Solid.DeviceInterface):
        """"""
        # Enum Solid.InternetGateway.NetworkProtocol
        TCP = 0
        UDP = 0
    
        # Enum Solid.InternetGateway.InternetStatus
        InternetEnabled = 0
        InternetDisabled = 0
        UnknownStatus = 0
    
        currentConnectionsDataIsReady = pyqtSignal() # void currentConnectionsDataIsReady(QStringList) - signal
        enabledForInternet = pyqtSignal() # void enabledForInternet(bool) - signal
        portMappingDeleted = pyqtSignal() # void portMappingDeleted(const QStringamp;,qint16,const Solid::InternetGateway::NetworkProtocolamp;) - signal
        portMappingAdded = pyqtSignal() # void portMappingAdded(const QStringamp;,qint16,const Solid::InternetGateway::NetworkProtocolamp;,qint16,const QStringamp;) - signal
        def setEnabledForInternet(self, enabled):
            '''void Solid.InternetGateway.setEnabledForInternet(bool enabled)'''
        def isEnabledForInternet(self):
            '''Solid.InternetGateway.InternetStatus Solid.InternetGateway.isEnabledForInternet()'''
            return Solid.InternetGateway.InternetStatus()
        def deletePortMapping(self, remoteHost, externalPort, mappingProtocol):
            '''void Solid.InternetGateway.deletePortMapping(QString remoteHost, int externalPort, Solid.InternetGateway.NetworkProtocol mappingProtocol)'''
        def addPortMapping(self, remoteHost, externalPort, mappingProtocol, internalPort, internalClient):
            '''void Solid.InternetGateway.addPortMapping(QString remoteHost, int externalPort, Solid.InternetGateway.NetworkProtocol mappingProtocol, int internalPort, QString internalClient)'''
        def currentConnections(self):
            '''QStringList Solid.InternetGateway.currentConnections()'''
            return QStringList()
        def requestCurrentConnections(self):
            '''void Solid.InternetGateway.requestCurrentConnections()'''
        def deviceInterfaceType(self):
            '''static Solid.DeviceInterface.Type Solid.InternetGateway.deviceInterfaceType()'''
            return Solid.DeviceInterface.Type()
    class SerialInterface(Solid.DeviceInterface):
        """"""
        # Enum Solid.SerialInterface.SerialType
        Unknown = 0
        Platform = 0
        Usb = 0
    
        def port(self):
            '''int Solid.SerialInterface.port()'''
            return int()
        def serialType(self):
            '''Solid.SerialInterface.SerialType Solid.SerialInterface.serialType()'''
            return Solid.SerialInterface.SerialType()
        def driverHandle(self):
            '''QVariant Solid.SerialInterface.driverHandle()'''
            return QVariant()
        def deviceInterfaceType(self):
            '''static Solid.DeviceInterface.Type Solid.SerialInterface.deviceInterfaceType()'''
            return Solid.DeviceInterface.Type()
    class OpticalDrive():
        """"""
        class MediumTypes():
            """"""
            def __init__(self):
                '''Solid.OpticalDrive.MediumTypes Solid.OpticalDrive.MediumTypes.__init__()'''
                return Solid.OpticalDrive.MediumTypes()
            def __init__(self):
                '''int Solid.OpticalDrive.MediumTypes.__init__()'''
                return int()
            def __init__(self):
                '''void Solid.OpticalDrive.MediumTypes.__init__()'''
            def __bool__(self):
                '''int Solid.OpticalDrive.MediumTypes.__bool__()'''
                return int()
            def __ne__(self, f):
                '''bool Solid.OpticalDrive.MediumTypes.__ne__(Solid.OpticalDrive.MediumTypes f)'''
                return bool()
            def __eq__(self, f):
                '''bool Solid.OpticalDrive.MediumTypes.__eq__(Solid.OpticalDrive.MediumTypes f)'''
                return bool()
            def __invert__(self):
                '''Solid.OpticalDrive.MediumTypes Solid.OpticalDrive.MediumTypes.__invert__()'''
                return Solid.OpticalDrive.MediumTypes()
            def __and__(self, mask):
                '''Solid.OpticalDrive.MediumTypes Solid.OpticalDrive.MediumTypes.__and__(int mask)'''
                return Solid.OpticalDrive.MediumTypes()
            def __xor__(self, f):
                '''Solid.OpticalDrive.MediumTypes Solid.OpticalDrive.MediumTypes.__xor__(Solid.OpticalDrive.MediumTypes f)'''
                return Solid.OpticalDrive.MediumTypes()
            def __xor__(self, f):
                '''Solid.OpticalDrive.MediumTypes Solid.OpticalDrive.MediumTypes.__xor__(int f)'''
                return Solid.OpticalDrive.MediumTypes()
            def __or__(self, f):
                '''Solid.OpticalDrive.MediumTypes Solid.OpticalDrive.MediumTypes.__or__(Solid.OpticalDrive.MediumTypes f)'''
                return Solid.OpticalDrive.MediumTypes()
            def __or__(self, f):
                '''Solid.OpticalDrive.MediumTypes Solid.OpticalDrive.MediumTypes.__or__(int f)'''
                return Solid.OpticalDrive.MediumTypes()
            def __int__(self):
                '''int Solid.OpticalDrive.MediumTypes.__int__()'''
                return int()
            def __ixor__(self, f):
                '''Solid.OpticalDrive.MediumTypes Solid.OpticalDrive.MediumTypes.__ixor__(Solid.OpticalDrive.MediumTypes f)'''
                return Solid.OpticalDrive.MediumTypes()
            def __ior__(self, f):
                '''Solid.OpticalDrive.MediumTypes Solid.OpticalDrive.MediumTypes.__ior__(Solid.OpticalDrive.MediumTypes f)'''
                return Solid.OpticalDrive.MediumTypes()
            def __iand__(self, mask):
                '''Solid.OpticalDrive.MediumTypes Solid.OpticalDrive.MediumTypes.__iand__(int mask)'''
                return Solid.OpticalDrive.MediumTypes()
    class Device():
        """"""
        def __init__(self, udi = QString()):
            '''void Solid.Device.__init__(QString udi = QString())'''
        def __init__(self, device):
            '''void Solid.Device.__init__(Solid.Device device)'''
        def description(self):
            '''QString Solid.Device.description()'''
            return QString()
        def emblems(self):
            '''QStringList Solid.Device.emblems()'''
            return QStringList()
        def asDeviceInterface(self, type):
            '''Solid.DeviceInterface Solid.Device.asDeviceInterface(Solid.DeviceInterface.Type type)'''
            return Solid.DeviceInterface()
        def isDeviceInterface(self, type):
            '''bool Solid.Device.isDeviceInterface(Solid.DeviceInterface.Type type)'''
            return bool()
        def icon(self):
            '''QString Solid.Device.icon()'''
            return QString()
        def product(self):
            '''QString Solid.Device.product()'''
            return QString()
        def vendor(self):
            '''QString Solid.Device.vendor()'''
            return QString()
        def parent(self):
            '''Solid.Device Solid.Device.parent()'''
            return Solid.Device()
        def parentUdi(self):
            '''QString Solid.Device.parentUdi()'''
            return QString()
        def udi(self):
            '''QString Solid.Device.udi()'''
            return QString()
        def isValid(self):
            '''bool Solid.Device.isValid()'''
            return bool()
        def listFromQuery(self, predicate, parentUdi = QString()):
            '''static list-of-Solid.Device Solid.Device.listFromQuery(Solid.Predicate predicate, QString parentUdi = QString())'''
            return [Solid.Device()]
        def listFromQuery(self, predicate, parentUdi = QString()):
            '''static list-of-Solid.Device Solid.Device.listFromQuery(QString predicate, QString parentUdi = QString())'''
            return [Solid.Device()]
        def listFromType(self, type, parentUdi = QString()):
            '''static list-of-Solid.Device Solid.Device.listFromType(Solid.DeviceInterface.Type type, QString parentUdi = QString())'''
            return [Solid.Device()]
        def allDevices(self):
            '''static list-of-Solid.Device Solid.Device.allDevices()'''
            return [Solid.Device()]
    class DvbInterface(Solid.DeviceInterface):
        """"""
        # Enum Solid.DvbInterface.DeviceType
        DvbUnknown = 0
        DvbAudio = 0
        DvbCa = 0
        DvbDemux = 0
        DvbDvr = 0
        DvbFrontend = 0
        DvbNet = 0
        DvbOsd = 0
        DvbSec = 0
        DvbVideo = 0
    
        def deviceIndex(self):
            '''int Solid.DvbInterface.deviceIndex()'''
            return int()
        def deviceType(self):
            '''Solid.DvbInterface.DeviceType Solid.DvbInterface.deviceType()'''
            return Solid.DvbInterface.DeviceType()
        def deviceAdapter(self):
            '''int Solid.DvbInterface.deviceAdapter()'''
            return int()
        def device(self):
            '''QString Solid.DvbInterface.device()'''
            return QString()
        def deviceInterfaceType(self):
            '''static Solid.DeviceInterface.Type Solid.DvbInterface.deviceInterfaceType()'''
            return Solid.DeviceInterface.Type()
    class NetworkInterface(Solid.DeviceInterface):
        """"""
        def macAddress(self):
            '''int Solid.NetworkInterface.macAddress()'''
            return int()
        def hwAddress(self):
            '''QString Solid.NetworkInterface.hwAddress()'''
            return QString()
        def isWireless(self):
            '''bool Solid.NetworkInterface.isWireless()'''
            return bool()
        def ifaceName(self):
            '''QString Solid.NetworkInterface.ifaceName()'''
            return QString()
        def deviceInterfaceType(self):
            '''static Solid.DeviceInterface.Type Solid.NetworkInterface.deviceInterfaceType()'''
            return Solid.DeviceInterface.Type()
    class DeviceNotifier(QObject):
        """"""
        def __init__(self):
            '''void Solid.DeviceNotifier.__init__()'''
        deviceRemoved = pyqtSignal() # void deviceRemoved(const QStringamp;) - signal
        deviceAdded = pyqtSignal() # void deviceAdded(const QStringamp;) - signal
        def instance(self):
            '''static Solid.DeviceNotifier Solid.DeviceNotifier.instance()'''
            return Solid.DeviceNotifier()
    class Processor():
        """"""
        class InstructionSets():
            """"""
            def __init__(self):
                '''Solid.Processor.InstructionSets Solid.Processor.InstructionSets.__init__()'''
                return Solid.Processor.InstructionSets()
            def __init__(self):
                '''int Solid.Processor.InstructionSets.__init__()'''
                return int()
            def __init__(self):
                '''void Solid.Processor.InstructionSets.__init__()'''
            def __bool__(self):
                '''int Solid.Processor.InstructionSets.__bool__()'''
                return int()
            def __ne__(self, f):
                '''bool Solid.Processor.InstructionSets.__ne__(Solid.Processor.InstructionSets f)'''
                return bool()
            def __eq__(self, f):
                '''bool Solid.Processor.InstructionSets.__eq__(Solid.Processor.InstructionSets f)'''
                return bool()
            def __invert__(self):
                '''Solid.Processor.InstructionSets Solid.Processor.InstructionSets.__invert__()'''
                return Solid.Processor.InstructionSets()
            def __and__(self, mask):
                '''Solid.Processor.InstructionSets Solid.Processor.InstructionSets.__and__(int mask)'''
                return Solid.Processor.InstructionSets()
            def __xor__(self, f):
                '''Solid.Processor.InstructionSets Solid.Processor.InstructionSets.__xor__(Solid.Processor.InstructionSets f)'''
                return Solid.Processor.InstructionSets()
            def __xor__(self, f):
                '''Solid.Processor.InstructionSets Solid.Processor.InstructionSets.__xor__(int f)'''
                return Solid.Processor.InstructionSets()
            def __or__(self, f):
                '''Solid.Processor.InstructionSets Solid.Processor.InstructionSets.__or__(Solid.Processor.InstructionSets f)'''
                return Solid.Processor.InstructionSets()
            def __or__(self, f):
                '''Solid.Processor.InstructionSets Solid.Processor.InstructionSets.__or__(int f)'''
                return Solid.Processor.InstructionSets()
            def __int__(self):
                '''int Solid.Processor.InstructionSets.__int__()'''
                return int()
            def __ixor__(self, f):
                '''Solid.Processor.InstructionSets Solid.Processor.InstructionSets.__ixor__(Solid.Processor.InstructionSets f)'''
                return Solid.Processor.InstructionSets()
            def __ior__(self, f):
                '''Solid.Processor.InstructionSets Solid.Processor.InstructionSets.__ior__(Solid.Processor.InstructionSets f)'''
                return Solid.Processor.InstructionSets()
            def __iand__(self, mask):
                '''Solid.Processor.InstructionSets Solid.Processor.InstructionSets.__iand__(int mask)'''
                return Solid.Processor.InstructionSets()
    class AudioInterface(Solid.DeviceInterface):
        """"""
        # Enum Solid.AudioInterface.SoundcardType
        InternalSoundcard = 0
        UsbSoundcard = 0
        FirewireSoundcard = 0
        Headset = 0
        Modem = 0
    
        # Enum Solid.AudioInterface.AudioInterfaceType
        UnknownAudioInterfaceType = 0
        AudioControl = 0
        AudioInput = 0
        AudioOutput = 0
    
        # Enum Solid.AudioInterface.AudioDriver
        Alsa = 0
        OpenSoundSystem = 0
        UnknownAudioDriver = 0
    
        def soundcardType(self):
            '''Solid.AudioInterface.SoundcardType Solid.AudioInterface.soundcardType()'''
            return Solid.AudioInterface.SoundcardType()
        def deviceType(self):
            '''Solid.AudioInterface.AudioInterfaceTypes Solid.AudioInterface.deviceType()'''
            return Solid.AudioInterface.AudioInterfaceTypes()
        def name(self):
            '''QString Solid.AudioInterface.name()'''
            return QString()
        def driverHandle(self):
            '''QVariant Solid.AudioInterface.driverHandle()'''
            return QVariant()
        def driver(self):
            '''Solid.AudioInterface.AudioDriver Solid.AudioInterface.driver()'''
            return Solid.AudioInterface.AudioDriver()
        def deviceInterfaceType(self):
            '''static Solid.DeviceInterface.Type Solid.AudioInterface.deviceInterfaceType()'''
            return Solid.DeviceInterface.Type()
    class PowerManagement():
        """"""
        # Enum Solid.PowerManagement.SleepState
        StandbyState = 0
        SuspendState = 0
        HibernateState = 0
    
        def stopSuppressingScreenPowerManagement(self, cookie):
            '''static bool Solid.PowerManagement.stopSuppressingScreenPowerManagement(int cookie)'''
            return bool()
        def beginSuppressingScreenPowerManagement(self, reason = QString()):
            '''static int Solid.PowerManagement.beginSuppressingScreenPowerManagement(QString reason = QString())'''
            return int()
        def stopSuppressingSleep(self, cookie):
            '''static bool Solid.PowerManagement.stopSuppressingSleep(int cookie)'''
            return bool()
        def beginSuppressingSleep(self, reason = QString()):
            '''static int Solid.PowerManagement.beginSuppressingSleep(QString reason = QString())'''
            return int()
        def requestSleep(self, state, receiver, member):
            '''static void Solid.PowerManagement.requestSleep(Solid.PowerManagement.SleepState state, QObject receiver, str member)'''
        def supportedSleepStates(self):
            '''static unknown-type Solid.PowerManagement.supportedSleepStates()'''
            return unknown-type()
        def appShouldConserveResources(self):
            '''static bool Solid.PowerManagement.appShouldConserveResources()'''
            return bool()
    class StorageAccess(Solid.DeviceInterface):
        """"""
        def isIgnored(self):
            '''bool Solid.StorageAccess.isIgnored()'''
            return bool()
        teardownRequested = pyqtSignal() # void teardownRequested(const QStringamp;) - signal
        setupRequested = pyqtSignal() # void setupRequested(const QStringamp;) - signal
        teardownDone = pyqtSignal() # void teardownDone(Solid::ErrorType,QVariant,const QStringamp;) - signal
        setupDone = pyqtSignal() # void setupDone(Solid::ErrorType,QVariant,const QStringamp;) - signal
        accessibilityChanged = pyqtSignal() # void accessibilityChanged(bool,const QStringamp;) - signal
        def teardown(self):
            '''bool Solid.StorageAccess.teardown()'''
            return bool()
        def setup(self):
            '''bool Solid.StorageAccess.setup()'''
            return bool()
        def filePath(self):
            '''QString Solid.StorageAccess.filePath()'''
            return QString()
        def isAccessible(self):
            '''bool Solid.StorageAccess.isAccessible()'''
            return bool()
        def deviceInterfaceType(self):
            '''static Solid.DeviceInterface.Type Solid.StorageAccess.deviceInterfaceType()'''
            return Solid.DeviceInterface.Type()
    class DeviceInterface(QObject):
        """"""
        # Enum Solid.DeviceInterface.Type
        Unknown = 0
        GenericInterface = 0
        Processor = 0
        Block = 0
        StorageAccess = 0
        StorageDrive = 0
        OpticalDrive = 0
        StorageVolume = 0
        OpticalDisc = 0
        Camera = 0
        PortableMediaPlayer = 0
        NetworkInterface = 0
        AcAdapter = 0
        Battery = 0
        Button = 0
        AudioInterface = 0
        DvbInterface = 0
        Video = 0
        SerialInterface = 0
        SmartCardReader = 0
        InternetGateway = 0
        NetworkShare = 0
        Last = 0
    
        def typeDescription(self, type):
            '''static QString Solid.DeviceInterface.typeDescription(Solid.DeviceInterface.Type type)'''
            return QString()
        def stringToType(self, type):
            '''static Solid.DeviceInterface.Type Solid.DeviceInterface.stringToType(QString type)'''
            return Solid.DeviceInterface.Type()
        def typeToString(self, type):
            '''static QString Solid.DeviceInterface.typeToString(Solid.DeviceInterface.Type type)'''
            return QString()
        def isValid(self):
            '''bool Solid.DeviceInterface.isValid()'''
            return bool()
    class Predicate():
        """"""
        # Enum Solid.Predicate.Type
        PropertyCheck = 0
        Conjunction = 0
        Disjunction = 0
        InterfaceCheck = 0
    
        # Enum Solid.Predicate.ComparisonOperator
        Equals = 0
        Mask = 0
    
        def __init__(self):
            '''void Solid.Predicate.__init__()'''
        def __init__(self, other):
            '''void Solid.Predicate.__init__(Solid.Predicate other)'''
        def __init__(self, ifaceName, property, value, compOperator = None):
            '''void Solid.Predicate.__init__(QString ifaceName, QString property, QVariant value, Solid.Predicate.ComparisonOperator compOperator = Solid.Predicate.Equals)'''
        def __init__(self, ifaceType):
            '''void Solid.Predicate.__init__(Solid.DeviceInterface.Type ifaceType)'''
        def __init__(self, ifaceName):
            '''void Solid.Predicate.__init__(QString ifaceName)'''
        def secondOperand(self):
            '''Solid.Predicate Solid.Predicate.secondOperand()'''
            return Solid.Predicate()
        def firstOperand(self):
            '''Solid.Predicate Solid.Predicate.firstOperand()'''
            return Solid.Predicate()
        def comparisonOperator(self):
            '''Solid.Predicate.ComparisonOperator Solid.Predicate.comparisonOperator()'''
            return Solid.Predicate.ComparisonOperator()
        def matchingValue(self):
            '''QVariant Solid.Predicate.matchingValue()'''
            return QVariant()
        def propertyName(self):
            '''QString Solid.Predicate.propertyName()'''
            return QString()
        def interfaceType(self):
            '''Solid.DeviceInterface.Type Solid.Predicate.interfaceType()'''
            return Solid.DeviceInterface.Type()
        def type(self):
            '''Solid.Predicate.Type Solid.Predicate.type()'''
            return Solid.Predicate.Type()
        def fromString(self, predicate):
            '''static Solid.Predicate Solid.Predicate.fromString(QString predicate)'''
            return Solid.Predicate()
        def toString(self):
            '''QString Solid.Predicate.toString()'''
            return QString()
        def usedTypes(self):
            '''unknown-type Solid.Predicate.usedTypes()'''
            return unknown-type()
        def matches(self, device):
            '''bool Solid.Predicate.matches(Solid.Device device)'''
            return bool()
        def isValid(self):
            '''bool Solid.Predicate.isValid()'''
            return bool()
        def __ior__(self, other):
            '''Solid.Predicate Solid.Predicate.__ior__(Solid.Predicate other)'''
            return Solid.Predicate()
        def __or__(self, other):
            '''Solid.Predicate Solid.Predicate.__or__(Solid.Predicate other)'''
            return Solid.Predicate()
        def __iand__(self, other):
            '''Solid.Predicate Solid.Predicate.__iand__(Solid.Predicate other)'''
            return Solid.Predicate()
        def __and__(self, other):
            '''Solid.Predicate Solid.Predicate.__and__(Solid.Predicate other)'''
            return Solid.Predicate()
    class GenericInterface(Solid.DeviceInterface):
        """"""
        # Enum Solid.GenericInterface.PropertyChange
        PropertyModified = 0
        PropertyAdded = 0
        PropertyRemoved = 0
    
        conditionRaised = pyqtSignal() # void conditionRaised(const QStringamp;,const QStringamp;) - signal
        def propertyExists(self, key):
            '''bool Solid.GenericInterface.propertyExists(QString key)'''
            return bool()
        def allProperties(self):
            '''dict-of-QString-QVariant Solid.GenericInterface.allProperties()'''
            return dict-of-QString-QVariant()
        def property(self, key):
            '''QVariant Solid.GenericInterface.property(QString key)'''
            return QVariant()
        def deviceInterfaceType(self):
            '''static Solid.DeviceInterface.Type Solid.GenericInterface.deviceInterfaceType()'''
            return Solid.DeviceInterface.Type()
    class Button(Solid.DeviceInterface):
        """"""
        # Enum Solid.Button.ButtonType
        LidButton = 0
        PowerButton = 0
        SleepButton = 0
        UnknownButtonType = 0
        TabletButton = 0
    
        pressed = pyqtSignal() # void pressed(Solid::Button::ButtonType,const QStringamp;) - signal
        def stateValue(self):
            '''bool Solid.Button.stateValue()'''
            return bool()
        def hasState(self):
            '''bool Solid.Button.hasState()'''
            return bool()
        def type(self):
            '''Solid.Button.ButtonType Solid.Button.type()'''
            return Solid.Button.ButtonType()
        def deviceInterfaceType(self):
            '''static Solid.DeviceInterface.Type Solid.Button.deviceInterfaceType()'''
            return Solid.DeviceInterface.Type()
    class PortableMediaPlayer(Solid.DeviceInterface):
        """"""
        def driverHandle(self, driver):
            '''QVariant Solid.PortableMediaPlayer.driverHandle(QString driver)'''
            return QVariant()
        def supportedDrivers(self, protocol = QString()):
            '''QStringList Solid.PortableMediaPlayer.supportedDrivers(QString protocol = QString())'''
            return QStringList()
        def supportedProtocols(self):
            '''QStringList Solid.PortableMediaPlayer.supportedProtocols()'''
            return QStringList()
        def deviceInterfaceType(self):
            '''static Solid.DeviceInterface.Type Solid.PortableMediaPlayer.deviceInterfaceType()'''
            return Solid.DeviceInterface.Type()


