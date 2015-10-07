class pyqtSignal():
 def connect(self, targetSignal): pass
 def emit(self, *args): pass
from QtCore import *

from QtWidgets import *

import datetime

class QSerialPort(QIODevice):
    """"""
    # Enum QSerialPort.SerialPortError
    NoError = 0
    DeviceNotFoundError = 0
    PermissionError = 0
    OpenError = 0
    ParityError = 0
    FramingError = 0
    BreakConditionError = 0
    WriteError = 0
    ReadError = 0
    ResourceError = 0
    UnsupportedOperationError = 0
    TimeoutError = 0
    NotOpenError = 0
    UnknownError = 0

    # Enum QSerialPort.DataErrorPolicy
    SkipPolicy = 0
    PassZeroPolicy = 0
    IgnorePolicy = 0
    StopReceivingPolicy = 0
    UnknownPolicy = 0

    # Enum QSerialPort.PinoutSignal
    NoSignal = 0
    TransmittedDataSignal = 0
    ReceivedDataSignal = 0
    DataTerminalReadySignal = 0
    DataCarrierDetectSignal = 0
    DataSetReadySignal = 0
    RingIndicatorSignal = 0
    RequestToSendSignal = 0
    ClearToSendSignal = 0
    SecondaryTransmittedDataSignal = 0
    SecondaryReceivedDataSignal = 0

    # Enum QSerialPort.FlowControl
    NoFlowControl = 0
    HardwareControl = 0
    SoftwareControl = 0
    UnknownFlowControl = 0

    # Enum QSerialPort.StopBits
    OneStop = 0
    OneAndHalfStop = 0
    TwoStop = 0
    UnknownStopBits = 0

    # Enum QSerialPort.Parity
    NoParity = 0
    EvenParity = 0
    OddParity = 0
    SpaceParity = 0
    MarkParity = 0
    UnknownParity = 0

    # Enum QSerialPort.DataBits
    Data5 = 0
    Data6 = 0
    Data7 = 0
    Data8 = 0
    UnknownDataBits = 0

    # Enum QSerialPort.BaudRate
    Baud1200 = 0
    Baud2400 = 0
    Baud4800 = 0
    Baud9600 = 0
    Baud19200 = 0
    Baud38400 = 0
    Baud57600 = 0
    Baud115200 = 0
    UnknownBaud = 0

    # Enum QSerialPort.Direction
    Input = 0
    Output = 0
    AllDirections = 0

    def __init__(self, parent = None):
        '''void QSerialPort.__init__(QObject parent = None)'''
    def __init__(self, name, parent = None):
        '''void QSerialPort.__init__(str name, QObject parent = None)'''
    def __init__(self, info, parent = None):
        '''void QSerialPort.__init__(QSerialPortInfo info, QObject parent = None)'''
    breakEnabledChanged = pyqtSignal() # void breakEnabledChanged(bool) - signal
    def isBreakEnabled(self):
        '''bool QSerialPort.isBreakEnabled()'''
        return bool()
    def handle(self):
        '''int QSerialPort.handle()'''
        return int()
    def writeData(self, data):
        '''int QSerialPort.writeData(str data)'''
        return int()
    def readLineData(self, maxlen):
        '''str QSerialPort.readLineData(int maxlen)'''
        return str()
    def readData(self, maxlen):
        '''str QSerialPort.readData(int maxlen)'''
        return str()
    settingsRestoredOnCloseChanged = pyqtSignal() # void settingsRestoredOnCloseChanged(bool) - signal
    requestToSendChanged = pyqtSignal() # void requestToSendChanged(bool) - signal
    dataTerminalReadyChanged = pyqtSignal() # void dataTerminalReadyChanged(bool) - signal
    dataErrorPolicyChanged = pyqtSignal() # void dataErrorPolicyChanged(QSerialPort::DataErrorPolicy) - signal
    flowControlChanged = pyqtSignal() # void flowControlChanged(QSerialPort::FlowControl) - signal
    stopBitsChanged = pyqtSignal() # void stopBitsChanged(QSerialPort::StopBits) - signal
    parityChanged = pyqtSignal() # void parityChanged(QSerialPort::Parity) - signal
    dataBitsChanged = pyqtSignal() # void dataBitsChanged(QSerialPort::DataBits) - signal
    baudRateChanged = pyqtSignal() # void baudRateChanged(qint32,QSerialPort::Directions) - signal
    def setBreakEnabled(self, enabled = True):
        '''bool QSerialPort.setBreakEnabled(bool enabled = True)'''
        return bool()
    def sendBreak(self, duration = 0):
        '''bool QSerialPort.sendBreak(int duration = 0)'''
        return bool()
    def waitForBytesWritten(self, msecs):
        '''bool QSerialPort.waitForBytesWritten(int msecs)'''
        return bool()
    def waitForReadyRead(self, msecs):
        '''bool QSerialPort.waitForReadyRead(int msecs)'''
        return bool()
    def canReadLine(self):
        '''bool QSerialPort.canReadLine()'''
        return bool()
    def bytesToWrite(self):
        '''int QSerialPort.bytesToWrite()'''
        return int()
    def bytesAvailable(self):
        '''int QSerialPort.bytesAvailable()'''
        return int()
    def isSequential(self):
        '''bool QSerialPort.isSequential()'''
        return bool()
    def setReadBufferSize(self, size):
        '''void QSerialPort.setReadBufferSize(int size)'''
    def readBufferSize(self):
        '''int QSerialPort.readBufferSize()'''
        return int()
    def clearError(self):
        '''void QSerialPort.clearError()'''
    def error(self):
        '''QSerialPort.SerialPortError QSerialPort.error()'''
        return QSerialPort.SerialPortError()
    error = pyqtSignal() # void error(QSerialPort::SerialPortError) - signal
    def dataErrorPolicy(self):
        '''QSerialPort.DataErrorPolicy QSerialPort.dataErrorPolicy()'''
        return QSerialPort.DataErrorPolicy()
    def setDataErrorPolicy(self, policy = None):
        '''bool QSerialPort.setDataErrorPolicy(QSerialPort.DataErrorPolicy policy = QSerialPort.IgnorePolicy)'''
        return bool()
    def atEnd(self):
        '''bool QSerialPort.atEnd()'''
        return bool()
    def clear(self, dir = None):
        '''bool QSerialPort.clear(QSerialPort.Directions dir = QSerialPort.AllDirections)'''
        return bool()
    def flush(self):
        '''bool QSerialPort.flush()'''
        return bool()
    def pinoutSignals(self):
        '''QSerialPort.PinoutSignals QSerialPort.pinoutSignals()'''
        return QSerialPort.PinoutSignals()
    def isRequestToSend(self):
        '''bool QSerialPort.isRequestToSend()'''
        return bool()
    def setRequestToSend(self, set):
        '''bool QSerialPort.setRequestToSend(bool set)'''
        return bool()
    def isDataTerminalReady(self):
        '''bool QSerialPort.isDataTerminalReady()'''
        return bool()
    def setDataTerminalReady(self, set):
        '''bool QSerialPort.setDataTerminalReady(bool set)'''
        return bool()
    def flowControl(self):
        '''QSerialPort.FlowControl QSerialPort.flowControl()'''
        return QSerialPort.FlowControl()
    def setFlowControl(self, flow):
        '''bool QSerialPort.setFlowControl(QSerialPort.FlowControl flow)'''
        return bool()
    def stopBits(self):
        '''QSerialPort.StopBits QSerialPort.stopBits()'''
        return QSerialPort.StopBits()
    def setStopBits(self, stopBits):
        '''bool QSerialPort.setStopBits(QSerialPort.StopBits stopBits)'''
        return bool()
    def parity(self):
        '''QSerialPort.Parity QSerialPort.parity()'''
        return QSerialPort.Parity()
    def setParity(self, parity):
        '''bool QSerialPort.setParity(QSerialPort.Parity parity)'''
        return bool()
    def dataBits(self):
        '''QSerialPort.DataBits QSerialPort.dataBits()'''
        return QSerialPort.DataBits()
    def setDataBits(self, dataBits):
        '''bool QSerialPort.setDataBits(QSerialPort.DataBits dataBits)'''
        return bool()
    def baudRate(self, dir = None):
        '''int QSerialPort.baudRate(QSerialPort.Directions dir = QSerialPort.AllDirections)'''
        return int()
    def setBaudRate(self, baudRate, dir = None):
        '''bool QSerialPort.setBaudRate(int baudRate, QSerialPort.Directions dir = QSerialPort.AllDirections)'''
        return bool()
    def settingsRestoredOnClose(self):
        '''bool QSerialPort.settingsRestoredOnClose()'''
        return bool()
    def setSettingsRestoredOnClose(self, restore):
        '''void QSerialPort.setSettingsRestoredOnClose(bool restore)'''
    def close(self):
        '''void QSerialPort.close()'''
    def open(self, mode):
        '''bool QSerialPort.open(QIODevice.OpenMode mode)'''
        return bool()
    def setPort(self, info):
        '''void QSerialPort.setPort(QSerialPortInfo info)'''
    def portName(self):
        '''str QSerialPort.portName()'''
        return str()
    def setPortName(self, name):
        '''void QSerialPort.setPortName(str name)'''
    class PinoutSignals():
        """"""
        def __init__(self):
            '''QSerialPort.PinoutSignals QSerialPort.PinoutSignals.__init__()'''
            return QSerialPort.PinoutSignals()
        def __init__(self):
            '''int QSerialPort.PinoutSignals.__init__()'''
            return int()
        def __init__(self):
            '''void QSerialPort.PinoutSignals.__init__()'''
        def __bool__(self):
            '''int QSerialPort.PinoutSignals.__bool__()'''
            return int()
        def __ne__(self, f):
            '''bool QSerialPort.PinoutSignals.__ne__(QSerialPort.PinoutSignals f)'''
            return bool()
        def __eq__(self, f):
            '''bool QSerialPort.PinoutSignals.__eq__(QSerialPort.PinoutSignals f)'''
            return bool()
        def __invert__(self):
            '''QSerialPort.PinoutSignals QSerialPort.PinoutSignals.__invert__()'''
            return QSerialPort.PinoutSignals()
        def __and__(self, mask):
            '''QSerialPort.PinoutSignals QSerialPort.PinoutSignals.__and__(int mask)'''
            return QSerialPort.PinoutSignals()
        def __xor__(self, f):
            '''QSerialPort.PinoutSignals QSerialPort.PinoutSignals.__xor__(QSerialPort.PinoutSignals f)'''
            return QSerialPort.PinoutSignals()
        def __xor__(self, f):
            '''QSerialPort.PinoutSignals QSerialPort.PinoutSignals.__xor__(int f)'''
            return QSerialPort.PinoutSignals()
        def __or__(self, f):
            '''QSerialPort.PinoutSignals QSerialPort.PinoutSignals.__or__(QSerialPort.PinoutSignals f)'''
            return QSerialPort.PinoutSignals()
        def __or__(self, f):
            '''QSerialPort.PinoutSignals QSerialPort.PinoutSignals.__or__(int f)'''
            return QSerialPort.PinoutSignals()
        def __int__(self):
            '''int QSerialPort.PinoutSignals.__int__()'''
            return int()
        def __ixor__(self, f):
            '''QSerialPort.PinoutSignals QSerialPort.PinoutSignals.__ixor__(QSerialPort.PinoutSignals f)'''
            return QSerialPort.PinoutSignals()
        def __ior__(self, f):
            '''QSerialPort.PinoutSignals QSerialPort.PinoutSignals.__ior__(QSerialPort.PinoutSignals f)'''
            return QSerialPort.PinoutSignals()
        def __iand__(self, mask):
            '''QSerialPort.PinoutSignals QSerialPort.PinoutSignals.__iand__(int mask)'''
            return QSerialPort.PinoutSignals()
    class Directions():
        """"""
        def __init__(self):
            '''QSerialPort.Directions QSerialPort.Directions.__init__()'''
            return QSerialPort.Directions()
        def __init__(self):
            '''int QSerialPort.Directions.__init__()'''
            return int()
        def __init__(self):
            '''void QSerialPort.Directions.__init__()'''
        def __bool__(self):
            '''int QSerialPort.Directions.__bool__()'''
            return int()
        def __ne__(self, f):
            '''bool QSerialPort.Directions.__ne__(QSerialPort.Directions f)'''
            return bool()
        def __eq__(self, f):
            '''bool QSerialPort.Directions.__eq__(QSerialPort.Directions f)'''
            return bool()
        def __invert__(self):
            '''QSerialPort.Directions QSerialPort.Directions.__invert__()'''
            return QSerialPort.Directions()
        def __and__(self, mask):
            '''QSerialPort.Directions QSerialPort.Directions.__and__(int mask)'''
            return QSerialPort.Directions()
        def __xor__(self, f):
            '''QSerialPort.Directions QSerialPort.Directions.__xor__(QSerialPort.Directions f)'''
            return QSerialPort.Directions()
        def __xor__(self, f):
            '''QSerialPort.Directions QSerialPort.Directions.__xor__(int f)'''
            return QSerialPort.Directions()
        def __or__(self, f):
            '''QSerialPort.Directions QSerialPort.Directions.__or__(QSerialPort.Directions f)'''
            return QSerialPort.Directions()
        def __or__(self, f):
            '''QSerialPort.Directions QSerialPort.Directions.__or__(int f)'''
            return QSerialPort.Directions()
        def __int__(self):
            '''int QSerialPort.Directions.__int__()'''
            return int()
        def __ixor__(self, f):
            '''QSerialPort.Directions QSerialPort.Directions.__ixor__(QSerialPort.Directions f)'''
            return QSerialPort.Directions()
        def __ior__(self, f):
            '''QSerialPort.Directions QSerialPort.Directions.__ior__(QSerialPort.Directions f)'''
            return QSerialPort.Directions()
        def __iand__(self, mask):
            '''QSerialPort.Directions QSerialPort.Directions.__iand__(int mask)'''
            return QSerialPort.Directions()


class QSerialPortInfo():
    """"""
    def __init__(self):
        '''void QSerialPortInfo.__init__()'''
    def __init__(self, port):
        '''void QSerialPortInfo.__init__(QSerialPort port)'''
    def __init__(self, name):
        '''void QSerialPortInfo.__init__(str name)'''
    def __init__(self, other):
        '''void QSerialPortInfo.__init__(QSerialPortInfo other)'''
    def serialNumber(self):
        '''str QSerialPortInfo.serialNumber()'''
        return str()
    def isNull(self):
        '''bool QSerialPortInfo.isNull()'''
        return bool()
    def availablePorts(self):
        '''static list-of-QSerialPortInfo QSerialPortInfo.availablePorts()'''
        return [QSerialPortInfo()]
    def standardBaudRates(self):
        '''static list-of-int QSerialPortInfo.standardBaudRates()'''
        return [int()]
    def isValid(self):
        '''bool QSerialPortInfo.isValid()'''
        return bool()
    def isBusy(self):
        '''bool QSerialPortInfo.isBusy()'''
        return bool()
    def hasProductIdentifier(self):
        '''bool QSerialPortInfo.hasProductIdentifier()'''
        return bool()
    def hasVendorIdentifier(self):
        '''bool QSerialPortInfo.hasVendorIdentifier()'''
        return bool()
    def productIdentifier(self):
        '''int QSerialPortInfo.productIdentifier()'''
        return int()
    def vendorIdentifier(self):
        '''int QSerialPortInfo.vendorIdentifier()'''
        return int()
    def manufacturer(self):
        '''str QSerialPortInfo.manufacturer()'''
        return str()
    def description(self):
        '''str QSerialPortInfo.description()'''
        return str()
    def systemLocation(self):
        '''str QSerialPortInfo.systemLocation()'''
        return str()
    def portName(self):
        '''str QSerialPortInfo.portName()'''
        return str()
    def swap(self, other):
        '''void QSerialPortInfo.swap(QSerialPortInfo other)'''


