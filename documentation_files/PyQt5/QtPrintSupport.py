class pyqtSignal():
 def connect(self, targetSignal): pass
 def emit(self, *args): pass
from QtCore import *

from QtWidgets import *

import datetime

class QAbstractPrintDialog(QDialog):
    """"""
    # Enum QAbstractPrintDialog.PrintDialogOption
    __kdevpythondocumentation_builtin_None = 0
    None_ = 0
    PrintToFile = 0
    PrintSelection = 0
    PrintPageRange = 0
    PrintCollateCopies = 0
    PrintShowPageSize = 0
    PrintCurrentPage = 0

    # Enum QAbstractPrintDialog.PrintRange
    AllPages = 0
    Selection = 0
    PageRange = 0
    CurrentPage = 0

    def __init__(self, printer, parent = None):
        '''void QAbstractPrintDialog.__init__(QPrinter printer, QWidget parent = None)'''
    def setOptionTabs(self, tabs):
        '''void QAbstractPrintDialog.setOptionTabs(list-of-QWidget tabs)'''
    def printer(self):
        '''QPrinter QAbstractPrintDialog.printer()'''
        return QPrinter()
    def toPage(self):
        '''int QAbstractPrintDialog.toPage()'''
        return int()
    def fromPage(self):
        '''int QAbstractPrintDialog.fromPage()'''
        return int()
    def setFromTo(self, fromPage, toPage):
        '''void QAbstractPrintDialog.setFromTo(int fromPage, int toPage)'''
    def maxPage(self):
        '''int QAbstractPrintDialog.maxPage()'''
        return int()
    def minPage(self):
        '''int QAbstractPrintDialog.minPage()'''
        return int()
    def setMinMax(self, min, max):
        '''void QAbstractPrintDialog.setMinMax(int min, int max)'''
    def printRange(self):
        '''QAbstractPrintDialog.PrintRange QAbstractPrintDialog.printRange()'''
        return QAbstractPrintDialog.PrintRange()
    def setPrintRange(self, range):
        '''void QAbstractPrintDialog.setPrintRange(QAbstractPrintDialog.PrintRange range)'''
    def exec_(self):
        '''abstract int QAbstractPrintDialog.exec_()'''
        return int()
    class PrintDialogOptions():
        """"""
        def __init__(self):
            '''QAbstractPrintDialog.PrintDialogOptions QAbstractPrintDialog.PrintDialogOptions.__init__()'''
            return QAbstractPrintDialog.PrintDialogOptions()
        def __init__(self):
            '''int QAbstractPrintDialog.PrintDialogOptions.__init__()'''
            return int()
        def __init__(self):
            '''void QAbstractPrintDialog.PrintDialogOptions.__init__()'''
        def __bool__(self):
            '''int QAbstractPrintDialog.PrintDialogOptions.__bool__()'''
            return int()
        def __ne__(self, f):
            '''bool QAbstractPrintDialog.PrintDialogOptions.__ne__(QAbstractPrintDialog.PrintDialogOptions f)'''
            return bool()
        def __eq__(self, f):
            '''bool QAbstractPrintDialog.PrintDialogOptions.__eq__(QAbstractPrintDialog.PrintDialogOptions f)'''
            return bool()
        def __invert__(self):
            '''QAbstractPrintDialog.PrintDialogOptions QAbstractPrintDialog.PrintDialogOptions.__invert__()'''
            return QAbstractPrintDialog.PrintDialogOptions()
        def __and__(self, mask):
            '''QAbstractPrintDialog.PrintDialogOptions QAbstractPrintDialog.PrintDialogOptions.__and__(int mask)'''
            return QAbstractPrintDialog.PrintDialogOptions()
        def __xor__(self, f):
            '''QAbstractPrintDialog.PrintDialogOptions QAbstractPrintDialog.PrintDialogOptions.__xor__(QAbstractPrintDialog.PrintDialogOptions f)'''
            return QAbstractPrintDialog.PrintDialogOptions()
        def __xor__(self, f):
            '''QAbstractPrintDialog.PrintDialogOptions QAbstractPrintDialog.PrintDialogOptions.__xor__(int f)'''
            return QAbstractPrintDialog.PrintDialogOptions()
        def __or__(self, f):
            '''QAbstractPrintDialog.PrintDialogOptions QAbstractPrintDialog.PrintDialogOptions.__or__(QAbstractPrintDialog.PrintDialogOptions f)'''
            return QAbstractPrintDialog.PrintDialogOptions()
        def __or__(self, f):
            '''QAbstractPrintDialog.PrintDialogOptions QAbstractPrintDialog.PrintDialogOptions.__or__(int f)'''
            return QAbstractPrintDialog.PrintDialogOptions()
        def __int__(self):
            '''int QAbstractPrintDialog.PrintDialogOptions.__int__()'''
            return int()
        def __ixor__(self, f):
            '''QAbstractPrintDialog.PrintDialogOptions QAbstractPrintDialog.PrintDialogOptions.__ixor__(QAbstractPrintDialog.PrintDialogOptions f)'''
            return QAbstractPrintDialog.PrintDialogOptions()
        def __ior__(self, f):
            '''QAbstractPrintDialog.PrintDialogOptions QAbstractPrintDialog.PrintDialogOptions.__ior__(QAbstractPrintDialog.PrintDialogOptions f)'''
            return QAbstractPrintDialog.PrintDialogOptions()
        def __iand__(self, mask):
            '''QAbstractPrintDialog.PrintDialogOptions QAbstractPrintDialog.PrintDialogOptions.__iand__(int mask)'''
            return QAbstractPrintDialog.PrintDialogOptions()


class QPageSetupDialog(QDialog):
    """"""
    def __init__(self, printer, parent = None):
        '''void QPageSetupDialog.__init__(QPrinter printer, QWidget parent = None)'''
    def __init__(self, parent = None):
        '''void QPageSetupDialog.__init__(QWidget parent = None)'''
    def printer(self):
        '''QPrinter QPageSetupDialog.printer()'''
        return QPrinter()
    def done(self, result):
        '''void QPageSetupDialog.done(int result)'''
    def open(self):
        '''void QPageSetupDialog.open()'''
    def open(self, slot):
        '''void QPageSetupDialog.open(slot slot)'''
    def exec_(self):
        '''int QPageSetupDialog.exec_()'''
        return int()
    def setVisible(self, visible):
        '''void QPageSetupDialog.setVisible(bool visible)'''


class QPrintDialog(QAbstractPrintDialog):
    """"""
    def __init__(self, printer, parent = None):
        '''void QPrintDialog.__init__(QPrinter printer, QWidget parent = None)'''
    def __init__(self, parent = None):
        '''void QPrintDialog.__init__(QWidget parent = None)'''
    accepted = pyqtSignal() # void accepted() - signal
    accepted = pyqtSignal() # void accepted(QPrinter*) - signal
    def open(self):
        '''void QPrintDialog.open()'''
    def open(self, slot):
        '''void QPrintDialog.open(slot slot)'''
    def setVisible(self, visible):
        '''void QPrintDialog.setVisible(bool visible)'''
    def options(self):
        '''QAbstractPrintDialog.PrintDialogOptions QPrintDialog.options()'''
        return QAbstractPrintDialog.PrintDialogOptions()
    def setOptions(self, options):
        '''void QPrintDialog.setOptions(QAbstractPrintDialog.PrintDialogOptions options)'''
    def testOption(self, option):
        '''bool QPrintDialog.testOption(QAbstractPrintDialog.PrintDialogOption option)'''
        return bool()
    def setOption(self, option, on = True):
        '''void QPrintDialog.setOption(QAbstractPrintDialog.PrintDialogOption option, bool on = True)'''
    def done(self, result):
        '''void QPrintDialog.done(int result)'''
    def accept(self):
        '''void QPrintDialog.accept()'''
    def exec_(self):
        '''int QPrintDialog.exec_()'''
        return int()


class QPrintEngine():
    """"""
    # Enum QPrintEngine.PrintEnginePropertyKey
    PPK_CollateCopies = 0
    PPK_ColorMode = 0
    PPK_Creator = 0
    PPK_DocumentName = 0
    PPK_FullPage = 0
    PPK_NumberOfCopies = 0
    PPK_Orientation = 0
    PPK_OutputFileName = 0
    PPK_PageOrder = 0
    PPK_PageRect = 0
    PPK_PageSize = 0
    PPK_PaperRect = 0
    PPK_PaperSource = 0
    PPK_PrinterName = 0
    PPK_PrinterProgram = 0
    PPK_Resolution = 0
    PPK_SelectionOption = 0
    PPK_SupportedResolutions = 0
    PPK_WindowsPageSize = 0
    PPK_FontEmbedding = 0
    PPK_Duplex = 0
    PPK_PaperSources = 0
    PPK_CustomPaperSize = 0
    PPK_PageMargins = 0
    PPK_PaperSize = 0
    PPK_CopyCount = 0
    PPK_SupportsMultipleCopies = 0
    PPK_PaperName = 0
    PPK_QPageSize = 0
    PPK_QPageMargins = 0
    PPK_QPageLayout = 0
    PPK_CustomBase = 0

    def __init__(self):
        '''void QPrintEngine.__init__()'''
    def __init__(self):
        '''QPrintEngine QPrintEngine.__init__()'''
        return QPrintEngine()
    def printerState(self):
        '''abstract QPrinter.PrinterState QPrintEngine.printerState()'''
        return QPrinter.PrinterState()
    def metric(self):
        '''abstract QPaintDevice.PaintDeviceMetric QPrintEngine.metric()'''
        return QPaintDevice.PaintDeviceMetric()
    def abort(self):
        '''abstract bool QPrintEngine.abort()'''
        return bool()
    def newPage(self):
        '''abstract bool QPrintEngine.newPage()'''
        return bool()
    def property(self, key):
        '''abstract QVariant QPrintEngine.property(QPrintEngine.PrintEnginePropertyKey key)'''
        return QVariant()
    def setProperty(self, key, value):
        '''abstract void QPrintEngine.setProperty(QPrintEngine.PrintEnginePropertyKey key, QVariant value)'''


class QPrinter(QPagedPaintDevice):
    """"""
    # Enum QPrinter.DuplexMode
    DuplexNone = 0
    DuplexAuto = 0
    DuplexLongSide = 0
    DuplexShortSide = 0

    # Enum QPrinter.Unit
    Millimeter = 0
    Point = 0
    Inch = 0
    Pica = 0
    Didot = 0
    Cicero = 0
    DevicePixel = 0

    # Enum QPrinter.PrintRange
    AllPages = 0
    Selection = 0
    PageRange = 0
    CurrentPage = 0

    # Enum QPrinter.OutputFormat
    NativeFormat = 0
    PdfFormat = 0

    # Enum QPrinter.PrinterState
    Idle = 0
    Active = 0
    Aborted = 0
    Error = 0

    # Enum QPrinter.PaperSource
    OnlyOne = 0
    Lower = 0
    Middle = 0
    Manual = 0
    Envelope = 0
    EnvelopeManual = 0
    Auto = 0
    Tractor = 0
    SmallFormat = 0
    LargeFormat = 0
    LargeCapacity = 0
    Cassette = 0
    FormSource = 0
    MaxPageSource = 0
    Upper = 0
    CustomSource = 0
    LastPaperSource = 0

    # Enum QPrinter.ColorMode
    GrayScale = 0
    Color = 0

    # Enum QPrinter.PageOrder
    FirstPageFirst = 0
    LastPageFirst = 0

    # Enum QPrinter.Orientation
    Portrait = 0
    Landscape = 0

    # Enum QPrinter.PrinterMode
    ScreenResolution = 0
    PrinterResolution = 0
    HighResolution = 0

    def __init__(self, mode = None):
        '''void QPrinter.__init__(QPrinter.PrinterMode mode = QPrinter.ScreenResolution)'''
    def __init__(self, printer, mode = None):
        '''void QPrinter.__init__(QPrinterInfo printer, QPrinter.PrinterMode mode = QPrinter.ScreenResolution)'''
    def paperName(self):
        '''str QPrinter.paperName()'''
        return str()
    def setPaperName(self, paperName):
        '''void QPrinter.setPaperName(str paperName)'''
    def setEngines(self, printEngine, paintEngine):
        '''void QPrinter.setEngines(QPrintEngine printEngine, QPaintEngine paintEngine)'''
    def metric(self):
        '''QPaintDevice.PaintDeviceMetric QPrinter.metric()'''
        return QPaintDevice.PaintDeviceMetric()
    def getPageMargins(self, left, top, right, bottom, unit):
        '''void QPrinter.getPageMargins(float left, float top, float right, float bottom, QPrinter.Unit unit)'''
    def setPageMargins(self, left, top, right, bottom, unit):
        '''void QPrinter.setPageMargins(float left, float top, float right, float bottom, QPrinter.Unit unit)'''
    def setMargins(self, m):
        '''void QPrinter.setMargins(QPagedPaintDevice.Margins m)'''
    def printRange(self):
        '''QPrinter.PrintRange QPrinter.printRange()'''
        return QPrinter.PrintRange()
    def setPrintRange(self, range):
        '''void QPrinter.setPrintRange(QPrinter.PrintRange range)'''
    def toPage(self):
        '''int QPrinter.toPage()'''
        return int()
    def fromPage(self):
        '''int QPrinter.fromPage()'''
        return int()
    def setFromTo(self, fromPage, toPage):
        '''void QPrinter.setFromTo(int fromPage, int toPage)'''
    def printEngine(self):
        '''QPrintEngine QPrinter.printEngine()'''
        return QPrintEngine()
    def paintEngine(self):
        '''QPaintEngine QPrinter.paintEngine()'''
        return QPaintEngine()
    def printerState(self):
        '''QPrinter.PrinterState QPrinter.printerState()'''
        return QPrinter.PrinterState()
    def abort(self):
        '''bool QPrinter.abort()'''
        return bool()
    def newPage(self):
        '''bool QPrinter.newPage()'''
        return bool()
    def setPrinterSelectionOption(self):
        '''str QPrinter.setPrinterSelectionOption()'''
        return str()
    def printerSelectionOption(self):
        '''str QPrinter.printerSelectionOption()'''
        return str()
    def pageRect(self):
        '''QRect QPrinter.pageRect()'''
        return QRect()
    def pageRect(self):
        '''QPrinter.Unit QPrinter.pageRect()'''
        return QPrinter.Unit()
    def paperRect(self):
        '''QRect QPrinter.paperRect()'''
        return QRect()
    def paperRect(self):
        '''QPrinter.Unit QPrinter.paperRect()'''
        return QPrinter.Unit()
    def doubleSidedPrinting(self):
        '''bool QPrinter.doubleSidedPrinting()'''
        return bool()
    def setDoubleSidedPrinting(self, enable):
        '''void QPrinter.setDoubleSidedPrinting(bool enable)'''
    def fontEmbeddingEnabled(self):
        '''bool QPrinter.fontEmbeddingEnabled()'''
        return bool()
    def setFontEmbeddingEnabled(self, enable):
        '''void QPrinter.setFontEmbeddingEnabled(bool enable)'''
    def supportedResolutions(self):
        '''list-of-int QPrinter.supportedResolutions()'''
        return [int()]
    def duplex(self):
        '''QPrinter.DuplexMode QPrinter.duplex()'''
        return QPrinter.DuplexMode()
    def setDuplex(self, duplex):
        '''void QPrinter.setDuplex(QPrinter.DuplexMode duplex)'''
    def paperSource(self):
        '''QPrinter.PaperSource QPrinter.paperSource()'''
        return QPrinter.PaperSource()
    def setPaperSource(self):
        '''QPrinter.PaperSource QPrinter.setPaperSource()'''
        return QPrinter.PaperSource()
    def supportsMultipleCopies(self):
        '''bool QPrinter.supportsMultipleCopies()'''
        return bool()
    def copyCount(self):
        '''int QPrinter.copyCount()'''
        return int()
    def setCopyCount(self):
        '''int QPrinter.setCopyCount()'''
        return int()
    def fullPage(self):
        '''bool QPrinter.fullPage()'''
        return bool()
    def setFullPage(self):
        '''bool QPrinter.setFullPage()'''
        return bool()
    def collateCopies(self):
        '''bool QPrinter.collateCopies()'''
        return bool()
    def setCollateCopies(self, collate):
        '''void QPrinter.setCollateCopies(bool collate)'''
    def colorMode(self):
        '''QPrinter.ColorMode QPrinter.colorMode()'''
        return QPrinter.ColorMode()
    def setColorMode(self):
        '''QPrinter.ColorMode QPrinter.setColorMode()'''
        return QPrinter.ColorMode()
    def resolution(self):
        '''int QPrinter.resolution()'''
        return int()
    def setResolution(self):
        '''int QPrinter.setResolution()'''
        return int()
    def pageOrder(self):
        '''QPrinter.PageOrder QPrinter.pageOrder()'''
        return QPrinter.PageOrder()
    def setPageOrder(self):
        '''QPrinter.PageOrder QPrinter.setPageOrder()'''
        return QPrinter.PageOrder()
    def paperSize(self):
        '''QPagedPaintDevice.PageSize QPrinter.paperSize()'''
        return QPagedPaintDevice.PageSize()
    def paperSize(self, unit):
        '''QSizeF QPrinter.paperSize(QPrinter.Unit unit)'''
        return QSizeF()
    def setPaperSize(self):
        '''QPagedPaintDevice.PageSize QPrinter.setPaperSize()'''
        return QPagedPaintDevice.PageSize()
    def setPaperSize(self, paperSize, unit):
        '''void QPrinter.setPaperSize(QSizeF paperSize, QPrinter.Unit unit)'''
    def setPageSizeMM(self, size):
        '''void QPrinter.setPageSizeMM(QSizeF size)'''
    def orientation(self):
        '''QPrinter.Orientation QPrinter.orientation()'''
        return QPrinter.Orientation()
    def setOrientation(self):
        '''QPrinter.Orientation QPrinter.setOrientation()'''
        return QPrinter.Orientation()
    def creator(self):
        '''str QPrinter.creator()'''
        return str()
    def setCreator(self):
        '''str QPrinter.setCreator()'''
        return str()
    def docName(self):
        '''str QPrinter.docName()'''
        return str()
    def setDocName(self):
        '''str QPrinter.setDocName()'''
        return str()
    def printProgram(self):
        '''str QPrinter.printProgram()'''
        return str()
    def setPrintProgram(self):
        '''str QPrinter.setPrintProgram()'''
        return str()
    def outputFileName(self):
        '''str QPrinter.outputFileName()'''
        return str()
    def setOutputFileName(self):
        '''str QPrinter.setOutputFileName()'''
        return str()
    def isValid(self):
        '''bool QPrinter.isValid()'''
        return bool()
    def printerName(self):
        '''str QPrinter.printerName()'''
        return str()
    def setPrinterName(self):
        '''str QPrinter.setPrinterName()'''
        return str()
    def outputFormat(self):
        '''QPrinter.OutputFormat QPrinter.outputFormat()'''
        return QPrinter.OutputFormat()
    def setOutputFormat(self, format):
        '''void QPrinter.setOutputFormat(QPrinter.OutputFormat format)'''


class QPrinterInfo():
    """"""
    def __init__(self):
        '''void QPrinterInfo.__init__()'''
    def __init__(self, src):
        '''void QPrinterInfo.__init__(QPrinterInfo src)'''
    def __init__(self, printer):
        '''void QPrinterInfo.__init__(QPrinter printer)'''
    def supportedDuplexModes(self):
        '''list-of-QPrinter.DuplexMode QPrinterInfo.supportedDuplexModes()'''
        return [QPrinter.DuplexMode()]
    def defaultDuplexMode(self):
        '''QPrinter.DuplexMode QPrinterInfo.defaultDuplexMode()'''
        return QPrinter.DuplexMode()
    def defaultPrinterName(self):
        '''static str QPrinterInfo.defaultPrinterName()'''
        return str()
    def availablePrinterNames(self):
        '''static list-of-str QPrinterInfo.availablePrinterNames()'''
        return [str()]
    def supportedResolutions(self):
        '''list-of-int QPrinterInfo.supportedResolutions()'''
        return [int()]
    def maximumPhysicalPageSize(self):
        '''QPageSize QPrinterInfo.maximumPhysicalPageSize()'''
        return QPageSize()
    def minimumPhysicalPageSize(self):
        '''QPageSize QPrinterInfo.minimumPhysicalPageSize()'''
        return QPageSize()
    def supportsCustomPageSizes(self):
        '''bool QPrinterInfo.supportsCustomPageSizes()'''
        return bool()
    def defaultPageSize(self):
        '''QPageSize QPrinterInfo.defaultPageSize()'''
        return QPageSize()
    def supportedPageSizes(self):
        '''list-of-QPageSize QPrinterInfo.supportedPageSizes()'''
        return [QPageSize()]
    def state(self):
        '''QPrinter.PrinterState QPrinterInfo.state()'''
        return QPrinter.PrinterState()
    def isRemote(self):
        '''bool QPrinterInfo.isRemote()'''
        return bool()
    def printerInfo(self, printerName):
        '''static QPrinterInfo QPrinterInfo.printerInfo(str printerName)'''
        return QPrinterInfo()
    def makeAndModel(self):
        '''str QPrinterInfo.makeAndModel()'''
        return str()
    def location(self):
        '''str QPrinterInfo.location()'''
        return str()
    def description(self):
        '''str QPrinterInfo.description()'''
        return str()
    def defaultPrinter(self):
        '''static QPrinterInfo QPrinterInfo.defaultPrinter()'''
        return QPrinterInfo()
    def availablePrinters(self):
        '''static list-of-QPrinterInfo QPrinterInfo.availablePrinters()'''
        return [QPrinterInfo()]
    def supportedSizesWithNames(self):
        '''list-of-tuple-of-QString-QSizeF QPrinterInfo.supportedSizesWithNames()'''
        return [tuple-of-str-QSizeF()]
    def supportedPaperSizes(self):
        '''list-of-QPagedPaintDevice.PageSize QPrinterInfo.supportedPaperSizes()'''
        return [QPagedPaintDevice.PageSize()]
    def isDefault(self):
        '''bool QPrinterInfo.isDefault()'''
        return bool()
    def isNull(self):
        '''bool QPrinterInfo.isNull()'''
        return bool()
    def printerName(self):
        '''str QPrinterInfo.printerName()'''
        return str()


class QPrintPreviewDialog(QDialog):
    """"""
    def __init__(self, parent = None, flags = 0):
        '''void QPrintPreviewDialog.__init__(QWidget parent = None, Qt.WindowFlags flags = 0)'''
    def __init__(self, printer, parent = None, flags = 0):
        '''void QPrintPreviewDialog.__init__(QPrinter printer, QWidget parent = None, Qt.WindowFlags flags = 0)'''
    paintRequested = pyqtSignal() # void paintRequested(QPrinter*) - signal
    def done(self, result):
        '''void QPrintPreviewDialog.done(int result)'''
    def printer(self):
        '''QPrinter QPrintPreviewDialog.printer()'''
        return QPrinter()
    def open(self):
        '''void QPrintPreviewDialog.open()'''
    def open(self, slot):
        '''void QPrintPreviewDialog.open(slot slot)'''
    def setVisible(self, visible):
        '''void QPrintPreviewDialog.setVisible(bool visible)'''


class QPrintPreviewWidget(QWidget):
    """"""
    # Enum QPrintPreviewWidget.ZoomMode
    CustomZoom = 0
    FitToWidth = 0
    FitInView = 0

    # Enum QPrintPreviewWidget.ViewMode
    SinglePageView = 0
    FacingPagesView = 0
    AllPagesView = 0

    def __init__(self, printer, parent = None, flags = 0):
        '''void QPrintPreviewWidget.__init__(QPrinter printer, QWidget parent = None, Qt.WindowFlags flags = 0)'''
    def __init__(self, parent = None, flags = 0):
        '''void QPrintPreviewWidget.__init__(QWidget parent = None, Qt.WindowFlags flags = 0)'''
    def pageCount(self):
        '''int QPrintPreviewWidget.pageCount()'''
        return int()
    previewChanged = pyqtSignal() # void previewChanged() - signal
    paintRequested = pyqtSignal() # void paintRequested(QPrinter*) - signal
    def updatePreview(self):
        '''void QPrintPreviewWidget.updatePreview()'''
    def setAllPagesViewMode(self):
        '''void QPrintPreviewWidget.setAllPagesViewMode()'''
    def setFacingPagesViewMode(self):
        '''void QPrintPreviewWidget.setFacingPagesViewMode()'''
    def setSinglePageViewMode(self):
        '''void QPrintPreviewWidget.setSinglePageViewMode()'''
    def setPortraitOrientation(self):
        '''void QPrintPreviewWidget.setPortraitOrientation()'''
    def setLandscapeOrientation(self):
        '''void QPrintPreviewWidget.setLandscapeOrientation()'''
    def fitInView(self):
        '''void QPrintPreviewWidget.fitInView()'''
    def fitToWidth(self):
        '''void QPrintPreviewWidget.fitToWidth()'''
    def setCurrentPage(self, pageNumber):
        '''void QPrintPreviewWidget.setCurrentPage(int pageNumber)'''
    def setZoomMode(self, zoomMode):
        '''void QPrintPreviewWidget.setZoomMode(QPrintPreviewWidget.ZoomMode zoomMode)'''
    def setViewMode(self, viewMode):
        '''void QPrintPreviewWidget.setViewMode(QPrintPreviewWidget.ViewMode viewMode)'''
    def setOrientation(self, orientation):
        '''void QPrintPreviewWidget.setOrientation(QPrinter.Orientation orientation)'''
    def setZoomFactor(self, zoomFactor):
        '''void QPrintPreviewWidget.setZoomFactor(float zoomFactor)'''
    def zoomOut(self, factor = None):
        '''void QPrintPreviewWidget.zoomOut(float factor = 1.1)'''
    def zoomIn(self, factor = None):
        '''void QPrintPreviewWidget.zoomIn(float factor = 1.1)'''
    def print_(self):
        '''void QPrintPreviewWidget.print_()'''
    def setVisible(self, visible):
        '''void QPrintPreviewWidget.setVisible(bool visible)'''
    def currentPage(self):
        '''int QPrintPreviewWidget.currentPage()'''
        return int()
    def zoomMode(self):
        '''QPrintPreviewWidget.ZoomMode QPrintPreviewWidget.zoomMode()'''
        return QPrintPreviewWidget.ZoomMode()
    def viewMode(self):
        '''QPrintPreviewWidget.ViewMode QPrintPreviewWidget.viewMode()'''
        return QPrintPreviewWidget.ViewMode()
    def orientation(self):
        '''QPrinter.Orientation QPrintPreviewWidget.orientation()'''
        return QPrinter.Orientation()
    def zoomFactor(self):
        '''float QPrintPreviewWidget.zoomFactor()'''
        return float()


