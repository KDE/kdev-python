class pyqtSignal():
 def connect(self, targetSignal): pass
 def emit(self, *args): pass
from QtCore import *

class QSysInfo():
    """"""
    # Enum QSysInfo.Endian
    BigEndian = 0
    LittleEndian = 0
    ByteOrder = 0

    # Enum QSysInfo.Sizes
    WordSize = 0

    def __init__(self):
        '''void QSysInfo.__init__()'''
    def __init__(self):
        '''QSysInfo QSysInfo.__init__()'''
        return QSysInfo()


class Qt():
    """"""
    # Enum Qt.CursorMoveStyle
    LogicalMoveStyle = 0
    VisualMoveStyle = 0

    # Enum Qt.NavigationMode
    NavigationModeNone = 0
    NavigationModeKeypadTabOrder = 0
    NavigationModeKeypadDirectional = 0
    NavigationModeCursorAuto = 0
    NavigationModeCursorForceVisible = 0

    # Enum Qt.GestureFlag
    DontStartGestureOnChildren = 0
    ReceivePartialGestures = 0
    IgnoredGesturesPropagateToParent = 0

    # Enum Qt.GestureType
    TapGesture = 0
    TapAndHoldGesture = 0
    PanGesture = 0
    PinchGesture = 0
    SwipeGesture = 0
    CustomGesture = 0

    # Enum Qt.GestureState
    GestureStarted = 0
    GestureUpdated = 0
    GestureFinished = 0
    GestureCanceled = 0

    # Enum Qt.TouchPointState
    TouchPointPressed = 0
    TouchPointMoved = 0
    TouchPointStationary = 0
    TouchPointReleased = 0

    # Enum Qt.CoordinateSystem
    DeviceCoordinates = 0
    LogicalCoordinates = 0

    # Enum Qt.AnchorPoint
    AnchorLeft = 0
    AnchorHorizontalCenter = 0
    AnchorRight = 0
    AnchorTop = 0
    AnchorVerticalCenter = 0
    AnchorBottom = 0

    # Enum Qt.InputMethodHint
    ImhNone = 0
    ImhHiddenText = 0
    ImhNoAutoUppercase = 0
    ImhPreferNumbers = 0
    ImhPreferUppercase = 0
    ImhPreferLowercase = 0
    ImhNoPredictiveText = 0
    ImhDigitsOnly = 0
    ImhFormattedNumbersOnly = 0
    ImhUppercaseOnly = 0
    ImhLowercaseOnly = 0
    ImhDialableCharactersOnly = 0
    ImhEmailCharactersOnly = 0
    ImhUrlCharactersOnly = 0
    ImhExclusiveInputMask = 0

    # Enum Qt.TileRule
    StretchTile = 0
    RepeatTile = 0
    RoundTile = 0

    # Enum Qt.WindowFrameSection
    NoSection = 0
    LeftSection = 0
    TopLeftSection = 0
    TopSection = 0
    TopRightSection = 0
    RightSection = 0
    BottomRightSection = 0
    BottomSection = 0
    BottomLeftSection = 0
    TitleBarArea = 0

    # Enum Qt.SizeHint
    MinimumSize = 0
    PreferredSize = 0
    MaximumSize = 0
    MinimumDescent = 0

    # Enum Qt.SizeMode
    AbsoluteSize = 0
    RelativeSize = 0

    # Enum Qt.EventPriority
    HighEventPriority = 0
    NormalEventPriority = 0
    LowEventPriority = 0

    # Enum Qt.Axis
    XAxis = 0
    YAxis = 0
    ZAxis = 0

    # Enum Qt.MaskMode
    MaskInColor = 0
    MaskOutColor = 0

    # Enum Qt.TextInteractionFlag
    NoTextInteraction = 0
    TextSelectableByMouse = 0
    TextSelectableByKeyboard = 0
    LinksAccessibleByMouse = 0
    LinksAccessibleByKeyboard = 0
    TextEditable = 0
    TextEditorInteraction = 0
    TextBrowserInteraction = 0

    # Enum Qt.ItemSelectionMode
    ContainsItemShape = 0
    IntersectsItemShape = 0
    ContainsItemBoundingRect = 0
    IntersectsItemBoundingRect = 0

    # Enum Qt.ApplicationAttribute
    AA_ImmediateWidgetCreation = 0
    AA_MSWindowsUseDirect3DByDefault = 0
    AA_DontShowIconsInMenus = 0
    AA_NativeWindows = 0
    AA_DontCreateNativeWidgetSiblings = 0
    AA_MacPluginApplication = 0
    AA_DontUseNativeMenuBar = 0
    AA_MacDontSwapCtrlAndMeta = 0
    AA_S60DontConstructApplicationPanes = 0
    AA_S60DisablePartialScreenInputMode = 0
    AA_X11InitThreads = 0
    AA_CaptureMultimediaKeys = 0

    # Enum Qt.WindowModality
    NonModal = 0
    WindowModal = 0
    ApplicationModal = 0

    # Enum Qt.MatchFlag
    MatchExactly = 0
    MatchFixedString = 0
    MatchContains = 0
    MatchStartsWith = 0
    MatchEndsWith = 0
    MatchRegExp = 0
    MatchWildcard = 0
    MatchCaseSensitive = 0
    MatchWrap = 0
    MatchRecursive = 0

    # Enum Qt.ItemFlag
    NoItemFlags = 0
    ItemIsSelectable = 0
    ItemIsEditable = 0
    ItemIsDragEnabled = 0
    ItemIsDropEnabled = 0
    ItemIsUserCheckable = 0
    ItemIsEnabled = 0
    ItemIsTristate = 0

    # Enum Qt.ItemDataRole
    DisplayRole = 0
    DecorationRole = 0
    EditRole = 0
    ToolTipRole = 0
    StatusTipRole = 0
    WhatsThisRole = 0
    FontRole = 0
    TextAlignmentRole = 0
    BackgroundRole = 0
    BackgroundColorRole = 0
    ForegroundRole = 0
    TextColorRole = 0
    CheckStateRole = 0
    AccessibleTextRole = 0
    AccessibleDescriptionRole = 0
    SizeHintRole = 0
    InitialSortOrderRole = 0
    UserRole = 0

    # Enum Qt.CheckState
    Unchecked = 0
    PartiallyChecked = 0
    Checked = 0

    # Enum Qt.DropAction
    CopyAction = 0
    MoveAction = 0
    LinkAction = 0
    ActionMask = 0
    TargetMoveAction = 0
    IgnoreAction = 0

    # Enum Qt.LayoutDirection
    LeftToRight = 0
    RightToLeft = 0
    LayoutDirectionAuto = 0

    # Enum Qt.ToolButtonStyle
    ToolButtonIconOnly = 0
    ToolButtonTextOnly = 0
    ToolButtonTextBesideIcon = 0
    ToolButtonTextUnderIcon = 0
    ToolButtonFollowStyle = 0

    # Enum Qt.InputMethodQuery
    ImMicroFocus = 0
    ImFont = 0
    ImCursorPosition = 0
    ImSurroundingText = 0
    ImCurrentSelection = 0
    ImMaximumTextLength = 0
    ImAnchorPosition = 0

    # Enum Qt.ContextMenuPolicy
    NoContextMenu = 0
    PreventContextMenu = 0
    DefaultContextMenu = 0
    ActionsContextMenu = 0
    CustomContextMenu = 0

    # Enum Qt.FocusReason
    MouseFocusReason = 0
    TabFocusReason = 0
    BacktabFocusReason = 0
    ActiveWindowFocusReason = 0
    PopupFocusReason = 0
    ShortcutFocusReason = 0
    MenuBarFocusReason = 0
    OtherFocusReason = 0
    NoFocusReason = 0

    # Enum Qt.TransformationMode
    FastTransformation = 0
    SmoothTransformation = 0

    # Enum Qt.ClipOperation
    NoClip = 0
    ReplaceClip = 0
    IntersectClip = 0
    UniteClip = 0

    # Enum Qt.FillRule
    OddEvenFill = 0
    WindingFill = 0

    # Enum Qt.ShortcutContext
    WidgetShortcut = 0
    WindowShortcut = 0
    ApplicationShortcut = 0
    WidgetWithChildrenShortcut = 0

    # Enum Qt.ConnectionType
    AutoConnection = 0
    DirectConnection = 0
    QueuedConnection = 0
    AutoCompatConnection = 0
    BlockingQueuedConnection = 0
    UniqueConnection = 0

    # Enum Qt.Corner
    TopLeftCorner = 0
    TopRightCorner = 0
    BottomLeftCorner = 0
    BottomRightCorner = 0

    # Enum Qt.CaseSensitivity
    CaseInsensitive = 0
    CaseSensitive = 0

    # Enum Qt.ScrollBarPolicy
    ScrollBarAsNeeded = 0
    ScrollBarAlwaysOff = 0
    ScrollBarAlwaysOn = 0

    # Enum Qt.DayOfWeek
    Monday = 0
    Tuesday = 0
    Wednesday = 0
    Thursday = 0
    Friday = 0
    Saturday = 0
    Sunday = 0

    # Enum Qt.TimeSpec
    LocalTime = 0
    UTC = 0
    OffsetFromUTC = 0

    # Enum Qt.DateFormat
    TextDate = 0
    ISODate = 0
    LocalDate = 0
    SystemLocaleDate = 0
    LocaleDate = 0
    SystemLocaleShortDate = 0
    SystemLocaleLongDate = 0
    DefaultLocaleShortDate = 0
    DefaultLocaleLongDate = 0

    # Enum Qt.ToolBarArea
    LeftToolBarArea = 0
    RightToolBarArea = 0
    TopToolBarArea = 0
    BottomToolBarArea = 0
    ToolBarArea_Mask = 0
    AllToolBarAreas = 0
    NoToolBarArea = 0

    # Enum Qt.DockWidgetArea
    LeftDockWidgetArea = 0
    RightDockWidgetArea = 0
    TopDockWidgetArea = 0
    BottomDockWidgetArea = 0
    DockWidgetArea_Mask = 0
    AllDockWidgetAreas = 0
    NoDockWidgetArea = 0

    # Enum Qt.AnchorAttribute
    AnchorName = 0
    AnchorHref = 0

    # Enum Qt.AspectRatioMode
    IgnoreAspectRatio = 0
    KeepAspectRatio = 0
    KeepAspectRatioByExpanding = 0

    # Enum Qt.TextFormat
    PlainText = 0
    RichText = 0
    AutoText = 0
    LogText = 0

    # Enum Qt.CursorShape
    ArrowCursor = 0
    UpArrowCursor = 0
    CrossCursor = 0
    WaitCursor = 0
    IBeamCursor = 0
    SizeVerCursor = 0
    SizeHorCursor = 0
    SizeBDiagCursor = 0
    SizeFDiagCursor = 0
    SizeAllCursor = 0
    BlankCursor = 0
    SplitVCursor = 0
    SplitHCursor = 0
    PointingHandCursor = 0
    ForbiddenCursor = 0
    OpenHandCursor = 0
    ClosedHandCursor = 0
    WhatsThisCursor = 0
    BusyCursor = 0
    LastCursor = 0
    BitmapCursor = 0
    CustomCursor = 0
    DragCopyCursor = 0
    DragMoveCursor = 0
    DragLinkCursor = 0

    # Enum Qt.UIEffect
    UI_General = 0
    UI_AnimateMenu = 0
    UI_FadeMenu = 0
    UI_AnimateCombo = 0
    UI_AnimateTooltip = 0
    UI_FadeTooltip = 0
    UI_AnimateToolBox = 0

    # Enum Qt.BrushStyle
    NoBrush = 0
    SolidPattern = 0
    Dense1Pattern = 0
    Dense2Pattern = 0
    Dense3Pattern = 0
    Dense4Pattern = 0
    Dense5Pattern = 0
    Dense6Pattern = 0
    Dense7Pattern = 0
    HorPattern = 0
    VerPattern = 0
    CrossPattern = 0
    BDiagPattern = 0
    FDiagPattern = 0
    DiagCrossPattern = 0
    LinearGradientPattern = 0
    RadialGradientPattern = 0
    ConicalGradientPattern = 0
    TexturePattern = 0

    # Enum Qt.PenJoinStyle
    MiterJoin = 0
    BevelJoin = 0
    RoundJoin = 0
    MPenJoinStyle = 0
    SvgMiterJoin = 0

    # Enum Qt.PenCapStyle
    FlatCap = 0
    SquareCap = 0
    RoundCap = 0
    MPenCapStyle = 0

    # Enum Qt.PenStyle
    NoPen = 0
    SolidLine = 0
    DashLine = 0
    DotLine = 0
    DashDotLine = 0
    DashDotDotLine = 0
    CustomDashLine = 0
    MPenStyle = 0

    # Enum Qt.ArrowType
    NoArrow = 0
    UpArrow = 0
    DownArrow = 0
    LeftArrow = 0
    RightArrow = 0

    # Enum Qt.Key
    Key_Escape = 0
    Key_Tab = 0
    Key_Backtab = 0
    Key_Backspace = 0
    Key_Return = 0
    Key_Enter = 0
    Key_Insert = 0
    Key_Delete = 0
    Key_Pause = 0
    Key_Print = 0
    Key_SysReq = 0
    Key_Clear = 0
    Key_Home = 0
    Key_End = 0
    Key_Left = 0
    Key_Up = 0
    Key_Right = 0
    Key_Down = 0
    Key_PageUp = 0
    Key_PageDown = 0
    Key_Shift = 0
    Key_Control = 0
    Key_Meta = 0
    Key_Alt = 0
    Key_CapsLock = 0
    Key_NumLock = 0
    Key_ScrollLock = 0
    Key_F1 = 0
    Key_F2 = 0
    Key_F3 = 0
    Key_F4 = 0
    Key_F5 = 0
    Key_F6 = 0
    Key_F7 = 0
    Key_F8 = 0
    Key_F9 = 0
    Key_F10 = 0
    Key_F11 = 0
    Key_F12 = 0
    Key_F13 = 0
    Key_F14 = 0
    Key_F15 = 0
    Key_F16 = 0
    Key_F17 = 0
    Key_F18 = 0
    Key_F19 = 0
    Key_F20 = 0
    Key_F21 = 0
    Key_F22 = 0
    Key_F23 = 0
    Key_F24 = 0
    Key_F25 = 0
    Key_F26 = 0
    Key_F27 = 0
    Key_F28 = 0
    Key_F29 = 0
    Key_F30 = 0
    Key_F31 = 0
    Key_F32 = 0
    Key_F33 = 0
    Key_F34 = 0
    Key_F35 = 0
    Key_Super_L = 0
    Key_Super_R = 0
    Key_Menu = 0
    Key_Hyper_L = 0
    Key_Hyper_R = 0
    Key_Help = 0
    Key_Direction_L = 0
    Key_Direction_R = 0
    Key_Space = 0
    Key_Any = 0
    Key_Exclam = 0
    Key_QuoteDbl = 0
    Key_NumberSign = 0
    Key_Dollar = 0
    Key_Percent = 0
    Key_Ampersand = 0
    Key_Apostrophe = 0
    Key_ParenLeft = 0
    Key_ParenRight = 0
    Key_Asterisk = 0
    Key_Plus = 0
    Key_Comma = 0
    Key_Minus = 0
    Key_Period = 0
    Key_Slash = 0
    Key_0 = 0
    Key_1 = 0
    Key_2 = 0
    Key_3 = 0
    Key_4 = 0
    Key_5 = 0
    Key_6 = 0
    Key_7 = 0
    Key_8 = 0
    Key_9 = 0
    Key_Colon = 0
    Key_Semicolon = 0
    Key_Less = 0
    Key_Equal = 0
    Key_Greater = 0
    Key_Question = 0
    Key_At = 0
    Key_A = 0
    Key_B = 0
    Key_C = 0
    Key_D = 0
    Key_E = 0
    Key_F = 0
    Key_G = 0
    Key_H = 0
    Key_I = 0
    Key_J = 0
    Key_K = 0
    Key_L = 0
    Key_M = 0
    Key_N = 0
    Key_O = 0
    Key_P = 0
    Key_Q = 0
    Key_R = 0
    Key_S = 0
    Key_T = 0
    Key_U = 0
    Key_V = 0
    Key_W = 0
    Key_X = 0
    Key_Y = 0
    Key_Z = 0
    Key_BracketLeft = 0
    Key_Backslash = 0
    Key_BracketRight = 0
    Key_AsciiCircum = 0
    Key_Underscore = 0
    Key_QuoteLeft = 0
    Key_BraceLeft = 0
    Key_Bar = 0
    Key_BraceRight = 0
    Key_AsciiTilde = 0
    Key_nobreakspace = 0
    Key_exclamdown = 0
    Key_cent = 0
    Key_sterling = 0
    Key_currency = 0
    Key_yen = 0
    Key_brokenbar = 0
    Key_section = 0
    Key_diaeresis = 0
    Key_copyright = 0
    Key_ordfeminine = 0
    Key_guillemotleft = 0
    Key_notsign = 0
    Key_hyphen = 0
    Key_registered = 0
    Key_macron = 0
    Key_degree = 0
    Key_plusminus = 0
    Key_twosuperior = 0
    Key_threesuperior = 0
    Key_acute = 0
    Key_mu = 0
    Key_paragraph = 0
    Key_periodcentered = 0
    Key_cedilla = 0
    Key_onesuperior = 0
    Key_masculine = 0
    Key_guillemotright = 0
    Key_onequarter = 0
    Key_onehalf = 0
    Key_threequarters = 0
    Key_questiondown = 0
    Key_Agrave = 0
    Key_Aacute = 0
    Key_Acircumflex = 0
    Key_Atilde = 0
    Key_Adiaeresis = 0
    Key_Aring = 0
    Key_AE = 0
    Key_Ccedilla = 0
    Key_Egrave = 0
    Key_Eacute = 0
    Key_Ecircumflex = 0
    Key_Ediaeresis = 0
    Key_Igrave = 0
    Key_Iacute = 0
    Key_Icircumflex = 0
    Key_Idiaeresis = 0
    Key_ETH = 0
    Key_Ntilde = 0
    Key_Ograve = 0
    Key_Oacute = 0
    Key_Ocircumflex = 0
    Key_Otilde = 0
    Key_Odiaeresis = 0
    Key_multiply = 0
    Key_Ooblique = 0
    Key_Ugrave = 0
    Key_Uacute = 0
    Key_Ucircumflex = 0
    Key_Udiaeresis = 0
    Key_Yacute = 0
    Key_THORN = 0
    Key_ssharp = 0
    Key_division = 0
    Key_ydiaeresis = 0
    Key_AltGr = 0
    Key_Multi_key = 0
    Key_Codeinput = 0
    Key_SingleCandidate = 0
    Key_MultipleCandidate = 0
    Key_PreviousCandidate = 0
    Key_Mode_switch = 0
    Key_Kanji = 0
    Key_Muhenkan = 0
    Key_Henkan = 0
    Key_Romaji = 0
    Key_Hiragana = 0
    Key_Katakana = 0
    Key_Hiragana_Katakana = 0
    Key_Zenkaku = 0
    Key_Hankaku = 0
    Key_Zenkaku_Hankaku = 0
    Key_Touroku = 0
    Key_Massyo = 0
    Key_Kana_Lock = 0
    Key_Kana_Shift = 0
    Key_Eisu_Shift = 0
    Key_Eisu_toggle = 0
    Key_Hangul = 0
    Key_Hangul_Start = 0
    Key_Hangul_End = 0
    Key_Hangul_Hanja = 0
    Key_Hangul_Jamo = 0
    Key_Hangul_Romaja = 0
    Key_Hangul_Jeonja = 0
    Key_Hangul_Banja = 0
    Key_Hangul_PreHanja = 0
    Key_Hangul_PostHanja = 0
    Key_Hangul_Special = 0
    Key_Dead_Grave = 0
    Key_Dead_Acute = 0
    Key_Dead_Circumflex = 0
    Key_Dead_Tilde = 0
    Key_Dead_Macron = 0
    Key_Dead_Breve = 0
    Key_Dead_Abovedot = 0
    Key_Dead_Diaeresis = 0
    Key_Dead_Abovering = 0
    Key_Dead_Doubleacute = 0
    Key_Dead_Caron = 0
    Key_Dead_Cedilla = 0
    Key_Dead_Ogonek = 0
    Key_Dead_Iota = 0
    Key_Dead_Voiced_Sound = 0
    Key_Dead_Semivoiced_Sound = 0
    Key_Dead_Belowdot = 0
    Key_Dead_Hook = 0
    Key_Dead_Horn = 0
    Key_Back = 0
    Key_Forward = 0
    Key_Stop = 0
    Key_Refresh = 0
    Key_VolumeDown = 0
    Key_VolumeMute = 0
    Key_VolumeUp = 0
    Key_BassBoost = 0
    Key_BassUp = 0
    Key_BassDown = 0
    Key_TrebleUp = 0
    Key_TrebleDown = 0
    Key_MediaPlay = 0
    Key_MediaStop = 0
    Key_MediaPrevious = 0
    Key_MediaNext = 0
    Key_MediaRecord = 0
    Key_HomePage = 0
    Key_Favorites = 0
    Key_Search = 0
    Key_Standby = 0
    Key_OpenUrl = 0
    Key_LaunchMail = 0
    Key_LaunchMedia = 0
    Key_Launch0 = 0
    Key_Launch1 = 0
    Key_Launch2 = 0
    Key_Launch3 = 0
    Key_Launch4 = 0
    Key_Launch5 = 0
    Key_Launch6 = 0
    Key_Launch7 = 0
    Key_Launch8 = 0
    Key_Launch9 = 0
    Key_LaunchA = 0
    Key_LaunchB = 0
    Key_LaunchC = 0
    Key_LaunchD = 0
    Key_LaunchE = 0
    Key_LaunchF = 0
    Key_MediaLast = 0
    Key_Select = 0
    Key_Yes = 0
    Key_No = 0
    Key_Context1 = 0
    Key_Context2 = 0
    Key_Context3 = 0
    Key_Context4 = 0
    Key_Call = 0
    Key_Hangup = 0
    Key_Flip = 0
    Key_unknown = 0
    Key_Execute = 0
    Key_Printer = 0
    Key_Play = 0
    Key_Sleep = 0
    Key_Zoom = 0
    Key_Cancel = 0
    Key_MonBrightnessUp = 0
    Key_MonBrightnessDown = 0
    Key_KeyboardLightOnOff = 0
    Key_KeyboardBrightnessUp = 0
    Key_KeyboardBrightnessDown = 0
    Key_PowerOff = 0
    Key_WakeUp = 0
    Key_Eject = 0
    Key_ScreenSaver = 0
    Key_WWW = 0
    Key_Memo = 0
    Key_LightBulb = 0
    Key_Shop = 0
    Key_History = 0
    Key_AddFavorite = 0
    Key_HotLinks = 0
    Key_BrightnessAdjust = 0
    Key_Finance = 0
    Key_Community = 0
    Key_AudioRewind = 0
    Key_BackForward = 0
    Key_ApplicationLeft = 0
    Key_ApplicationRight = 0
    Key_Book = 0
    Key_CD = 0
    Key_Calculator = 0
    Key_ToDoList = 0
    Key_ClearGrab = 0
    Key_Close = 0
    Key_Copy = 0
    Key_Cut = 0
    Key_Display = 0
    Key_DOS = 0
    Key_Documents = 0
    Key_Excel = 0
    Key_Explorer = 0
    Key_Game = 0
    Key_Go = 0
    Key_iTouch = 0
    Key_LogOff = 0
    Key_Market = 0
    Key_Meeting = 0
    Key_MenuKB = 0
    Key_MenuPB = 0
    Key_MySites = 0
    Key_News = 0
    Key_OfficeHome = 0
    Key_Option = 0
    Key_Paste = 0
    Key_Phone = 0
    Key_Calendar = 0
    Key_Reply = 0
    Key_Reload = 0
    Key_RotateWindows = 0
    Key_RotationPB = 0
    Key_RotationKB = 0
    Key_Save = 0
    Key_Send = 0
    Key_Spell = 0
    Key_SplitScreen = 0
    Key_Support = 0
    Key_TaskPane = 0
    Key_Terminal = 0
    Key_Tools = 0
    Key_Travel = 0
    Key_Video = 0
    Key_Word = 0
    Key_Xfer = 0
    Key_ZoomIn = 0
    Key_ZoomOut = 0
    Key_Away = 0
    Key_Messenger = 0
    Key_WebCam = 0
    Key_MailForward = 0
    Key_Pictures = 0
    Key_Music = 0
    Key_Battery = 0
    Key_Bluetooth = 0
    Key_WLAN = 0
    Key_UWB = 0
    Key_AudioForward = 0
    Key_AudioRepeat = 0
    Key_AudioRandomPlay = 0
    Key_Subtitle = 0
    Key_AudioCycleTrack = 0
    Key_Time = 0
    Key_Hibernate = 0
    Key_View = 0
    Key_TopMenu = 0
    Key_PowerDown = 0
    Key_Suspend = 0
    Key_ContrastAdjust = 0
    Key_MediaPause = 0
    Key_MediaTogglePlayPause = 0
    Key_LaunchG = 0
    Key_LaunchH = 0
    Key_ToggleCallHangup = 0
    Key_VoiceDial = 0
    Key_LastNumberRedial = 0
    Key_Camera = 0
    Key_CameraFocus = 0

    # Enum Qt.BGMode
    TransparentMode = 0
    OpaqueMode = 0

    # Enum Qt.ImageConversionFlag
    AutoColor = 0
    ColorOnly = 0
    MonoOnly = 0
    ThresholdAlphaDither = 0
    OrderedAlphaDither = 0
    DiffuseAlphaDither = 0
    DiffuseDither = 0
    OrderedDither = 0
    ThresholdDither = 0
    AutoDither = 0
    PreferDither = 0
    AvoidDither = 0

    # Enum Qt.WidgetAttribute
    WA_Disabled = 0
    WA_UnderMouse = 0
    WA_MouseTracking = 0
    WA_OpaquePaintEvent = 0
    WA_StaticContents = 0
    WA_LaidOut = 0
    WA_PaintOnScreen = 0
    WA_NoSystemBackground = 0
    WA_UpdatesDisabled = 0
    WA_Mapped = 0
    WA_MacNoClickThrough = 0
    WA_PaintOutsidePaintEvent = 0
    WA_InputMethodEnabled = 0
    WA_WState_Visible = 0
    WA_WState_Hidden = 0
    WA_ForceDisabled = 0
    WA_KeyCompression = 0
    WA_PendingMoveEvent = 0
    WA_PendingResizeEvent = 0
    WA_SetPalette = 0
    WA_SetFont = 0
    WA_SetCursor = 0
    WA_NoChildEventsFromChildren = 0
    WA_WindowModified = 0
    WA_Resized = 0
    WA_Moved = 0
    WA_PendingUpdate = 0
    WA_InvalidSize = 0
    WA_MacMetalStyle = 0
    WA_CustomWhatsThis = 0
    WA_LayoutOnEntireRect = 0
    WA_OutsideWSRange = 0
    WA_GrabbedShortcut = 0
    WA_TransparentForMouseEvents = 0
    WA_PaintUnclipped = 0
    WA_SetWindowIcon = 0
    WA_NoMouseReplay = 0
    WA_DeleteOnClose = 0
    WA_RightToLeft = 0
    WA_SetLayoutDirection = 0
    WA_NoChildEventsForParent = 0
    WA_ForceUpdatesDisabled = 0
    WA_WState_Created = 0
    WA_WState_CompressKeys = 0
    WA_WState_InPaintEvent = 0
    WA_WState_Reparented = 0
    WA_WState_ConfigPending = 0
    WA_WState_Polished = 0
    WA_WState_OwnSizePolicy = 0
    WA_WState_ExplicitShowHide = 0
    WA_MouseNoMask = 0
    WA_GroupLeader = 0
    WA_NoMousePropagation = 0
    WA_Hover = 0
    WA_InputMethodTransparent = 0
    WA_QuitOnClose = 0
    WA_KeyboardFocusChange = 0
    WA_AcceptDrops = 0
    WA_WindowPropagation = 0
    WA_NoX11EventCompression = 0
    WA_TintedBackground = 0
    WA_X11OpenGLOverlay = 0
    WA_AttributeCount = 0
    WA_AlwaysShowToolTips = 0
    WA_MacOpaqueSizeGrip = 0
    WA_SetStyle = 0
    WA_MacBrushedMetal = 0
    WA_SetLocale = 0
    WA_MacShowFocusRect = 0
    WA_MacNormalSize = 0
    WA_MacSmallSize = 0
    WA_MacMiniSize = 0
    WA_LayoutUsesWidgetRect = 0
    WA_StyledBackground = 0
    WA_MSWindowsUseDirect3D = 0
    WA_MacAlwaysShowToolWindow = 0
    WA_StyleSheet = 0
    WA_ShowWithoutActivating = 0
    WA_NativeWindow = 0
    WA_DontCreateNativeAncestors = 0
    WA_MacVariableSize = 0
    WA_X11NetWmWindowTypeDesktop = 0
    WA_X11NetWmWindowTypeDock = 0
    WA_X11NetWmWindowTypeToolBar = 0
    WA_X11NetWmWindowTypeMenu = 0
    WA_X11NetWmWindowTypeUtility = 0
    WA_X11NetWmWindowTypeSplash = 0
    WA_X11NetWmWindowTypeDialog = 0
    WA_X11NetWmWindowTypeDropDownMenu = 0
    WA_X11NetWmWindowTypePopupMenu = 0
    WA_X11NetWmWindowTypeToolTip = 0
    WA_X11NetWmWindowTypeNotification = 0
    WA_X11NetWmWindowTypeCombo = 0
    WA_X11NetWmWindowTypeDND = 0
    WA_MacFrameworkScaled = 0
    WA_TranslucentBackground = 0
    WA_AcceptTouchEvents = 0
    WA_TouchPadAcceptSingleTouchEvents = 0
    WA_MergeSoftkeys = 0
    WA_MergeSoftkeysRecursively = 0
    WA_X11DoNotAcceptFocus = 0
    WA_LockPortraitOrientation = 0
    WA_LockLandscapeOrientation = 0
    WA_AutoOrientation = 0
    WA_MacNoShadow = 0

    # Enum Qt.WindowState
    WindowNoState = 0
    WindowMinimized = 0
    WindowMaximized = 0
    WindowFullScreen = 0
    WindowActive = 0

    # Enum Qt.WindowType
    Widget = 0
    Window = 0
    Dialog = 0
    Sheet = 0
    Drawer = 0
    Popup = 0
    Tool = 0
    ToolTip = 0
    SplashScreen = 0
    Desktop = 0
    SubWindow = 0
    WindowType_Mask = 0
    MSWindowsFixedSizeDialogHint = 0
    MSWindowsOwnDC = 0
    X11BypassWindowManagerHint = 0
    FramelessWindowHint = 0
    CustomizeWindowHint = 0
    WindowTitleHint = 0
    WindowSystemMenuHint = 0
    WindowMinimizeButtonHint = 0
    WindowMaximizeButtonHint = 0
    WindowMinMaxButtonsHint = 0
    WindowContextHelpButtonHint = 0
    WindowShadeButtonHint = 0
    WindowStaysOnTopHint = 0
    WindowOkButtonHint = 0
    WindowCancelButtonHint = 0
    WindowStaysOnBottomHint = 0
    WindowCloseButtonHint = 0
    MacWindowToolBarButtonHint = 0
    BypassGraphicsProxyWidget = 0
    WindowSoftkeysVisibleHint = 0
    WindowSoftkeysRespondHint = 0

    # Enum Qt.TextElideMode
    ElideLeft = 0
    ElideRight = 0
    ElideMiddle = 0
    ElideNone = 0

    # Enum Qt.TextFlag
    TextSingleLine = 0
    TextDontClip = 0
    TextExpandTabs = 0
    TextShowMnemonic = 0
    TextWordWrap = 0
    TextWrapAnywhere = 0
    TextDontPrint = 0
    TextIncludeTrailingSpaces = 0
    TextHideMnemonic = 0
    TextJustificationForced = 0

    # Enum Qt.AlignmentFlag
    AlignLeft = 0
    AlignLeading = 0
    AlignRight = 0
    AlignTrailing = 0
    AlignHCenter = 0
    AlignJustify = 0
    AlignAbsolute = 0
    AlignHorizontal_Mask = 0
    AlignTop = 0
    AlignBottom = 0
    AlignVCenter = 0
    AlignVertical_Mask = 0
    AlignCenter = 0

    # Enum Qt.SortOrder
    AscendingOrder = 0
    DescendingOrder = 0

    # Enum Qt.FocusPolicy
    NoFocus = 0
    TabFocus = 0
    ClickFocus = 0
    StrongFocus = 0
    WheelFocus = 0

    # Enum Qt.Orientation
    Horizontal = 0
    Vertical = 0

    # Enum Qt.MouseButton
    NoButton = 0
    LeftButton = 0
    RightButton = 0
    MidButton = 0
    MiddleButton = 0
    XButton1 = 0
    XButton2 = 0
    MouseButtonMask = 0

    # Enum Qt.Modifier
    META = 0
    SHIFT = 0
    CTRL = 0
    ALT = 0
    MODIFIER_MASK = 0
    UNICODE_ACCEL = 0

    # Enum Qt.KeyboardModifier
    NoModifier = 0
    ShiftModifier = 0
    ControlModifier = 0
    AltModifier = 0
    MetaModifier = 0
    KeypadModifier = 0
    GroupSwitchModifier = 0
    KeyboardModifierMask = 0

    # Enum Qt.GlobalColor
    color0 = 0
    color1 = 0
    black = 0
    white = 0
    darkGray = 0
    gray = 0
    lightGray = 0
    red = 0
    green = 0
    blue = 0
    cyan = 0
    magenta = 0
    yellow = 0
    darkRed = 0
    darkGreen = 0
    darkBlue = 0
    darkCyan = 0
    darkMagenta = 0
    darkYellow = 0
    transparent = 0

    class WindowFlags():
        """"""
        def __init__(self):
            '''Qt.WindowFlags Qt.WindowFlags.__init__()'''
            return Qt.WindowFlags()
        def __init__(self):
            '''int Qt.WindowFlags.__init__()'''
            return int()
        def __init__(self):
            '''void Qt.WindowFlags.__init__()'''
        def __bool__(self):
            '''int Qt.WindowFlags.__bool__()'''
            return int()
        def __ne__(self, f):
            '''bool Qt.WindowFlags.__ne__(Qt.WindowFlags f)'''
            return bool()
        def __eq__(self, f):
            '''bool Qt.WindowFlags.__eq__(Qt.WindowFlags f)'''
            return bool()
        def __invert__(self):
            '''Qt.WindowFlags Qt.WindowFlags.__invert__()'''
            return Qt.WindowFlags()
        def __and__(self, mask):
            '''Qt.WindowFlags Qt.WindowFlags.__and__(int mask)'''
            return Qt.WindowFlags()
        def __xor__(self, f):
            '''Qt.WindowFlags Qt.WindowFlags.__xor__(Qt.WindowFlags f)'''
            return Qt.WindowFlags()
        def __xor__(self, f):
            '''Qt.WindowFlags Qt.WindowFlags.__xor__(int f)'''
            return Qt.WindowFlags()
        def __or__(self, f):
            '''Qt.WindowFlags Qt.WindowFlags.__or__(Qt.WindowFlags f)'''
            return Qt.WindowFlags()
        def __or__(self, f):
            '''Qt.WindowFlags Qt.WindowFlags.__or__(int f)'''
            return Qt.WindowFlags()
        def __int__(self):
            '''int Qt.WindowFlags.__int__()'''
            return int()
        def __ixor__(self, f):
            '''Qt.WindowFlags Qt.WindowFlags.__ixor__(Qt.WindowFlags f)'''
            return Qt.WindowFlags()
        def __ior__(self, f):
            '''Qt.WindowFlags Qt.WindowFlags.__ior__(Qt.WindowFlags f)'''
            return Qt.WindowFlags()
        def __iand__(self, mask):
            '''Qt.WindowFlags Qt.WindowFlags.__iand__(int mask)'''
            return Qt.WindowFlags()
    class ToolBarAreas():
        """"""
        def __init__(self):
            '''Qt.ToolBarAreas Qt.ToolBarAreas.__init__()'''
            return Qt.ToolBarAreas()
        def __init__(self):
            '''int Qt.ToolBarAreas.__init__()'''
            return int()
        def __init__(self):
            '''void Qt.ToolBarAreas.__init__()'''
        def __bool__(self):
            '''int Qt.ToolBarAreas.__bool__()'''
            return int()
        def __ne__(self, f):
            '''bool Qt.ToolBarAreas.__ne__(Qt.ToolBarAreas f)'''
            return bool()
        def __eq__(self, f):
            '''bool Qt.ToolBarAreas.__eq__(Qt.ToolBarAreas f)'''
            return bool()
        def __invert__(self):
            '''Qt.ToolBarAreas Qt.ToolBarAreas.__invert__()'''
            return Qt.ToolBarAreas()
        def __and__(self, mask):
            '''Qt.ToolBarAreas Qt.ToolBarAreas.__and__(int mask)'''
            return Qt.ToolBarAreas()
        def __xor__(self, f):
            '''Qt.ToolBarAreas Qt.ToolBarAreas.__xor__(Qt.ToolBarAreas f)'''
            return Qt.ToolBarAreas()
        def __xor__(self, f):
            '''Qt.ToolBarAreas Qt.ToolBarAreas.__xor__(int f)'''
            return Qt.ToolBarAreas()
        def __or__(self, f):
            '''Qt.ToolBarAreas Qt.ToolBarAreas.__or__(Qt.ToolBarAreas f)'''
            return Qt.ToolBarAreas()
        def __or__(self, f):
            '''Qt.ToolBarAreas Qt.ToolBarAreas.__or__(int f)'''
            return Qt.ToolBarAreas()
        def __int__(self):
            '''int Qt.ToolBarAreas.__int__()'''
            return int()
        def __ixor__(self, f):
            '''Qt.ToolBarAreas Qt.ToolBarAreas.__ixor__(Qt.ToolBarAreas f)'''
            return Qt.ToolBarAreas()
        def __ior__(self, f):
            '''Qt.ToolBarAreas Qt.ToolBarAreas.__ior__(Qt.ToolBarAreas f)'''
            return Qt.ToolBarAreas()
        def __iand__(self, mask):
            '''Qt.ToolBarAreas Qt.ToolBarAreas.__iand__(int mask)'''
            return Qt.ToolBarAreas()
    class InputMethodHints():
        """"""
        def __init__(self):
            '''Qt.InputMethodHints Qt.InputMethodHints.__init__()'''
            return Qt.InputMethodHints()
        def __init__(self):
            '''int Qt.InputMethodHints.__init__()'''
            return int()
        def __init__(self):
            '''void Qt.InputMethodHints.__init__()'''
        def __bool__(self):
            '''int Qt.InputMethodHints.__bool__()'''
            return int()
        def __ne__(self, f):
            '''bool Qt.InputMethodHints.__ne__(Qt.InputMethodHints f)'''
            return bool()
        def __eq__(self, f):
            '''bool Qt.InputMethodHints.__eq__(Qt.InputMethodHints f)'''
            return bool()
        def __invert__(self):
            '''Qt.InputMethodHints Qt.InputMethodHints.__invert__()'''
            return Qt.InputMethodHints()
        def __and__(self, mask):
            '''Qt.InputMethodHints Qt.InputMethodHints.__and__(int mask)'''
            return Qt.InputMethodHints()
        def __xor__(self, f):
            '''Qt.InputMethodHints Qt.InputMethodHints.__xor__(Qt.InputMethodHints f)'''
            return Qt.InputMethodHints()
        def __xor__(self, f):
            '''Qt.InputMethodHints Qt.InputMethodHints.__xor__(int f)'''
            return Qt.InputMethodHints()
        def __or__(self, f):
            '''Qt.InputMethodHints Qt.InputMethodHints.__or__(Qt.InputMethodHints f)'''
            return Qt.InputMethodHints()
        def __or__(self, f):
            '''Qt.InputMethodHints Qt.InputMethodHints.__or__(int f)'''
            return Qt.InputMethodHints()
        def __int__(self):
            '''int Qt.InputMethodHints.__int__()'''
            return int()
        def __ixor__(self, f):
            '''Qt.InputMethodHints Qt.InputMethodHints.__ixor__(Qt.InputMethodHints f)'''
            return Qt.InputMethodHints()
        def __ior__(self, f):
            '''Qt.InputMethodHints Qt.InputMethodHints.__ior__(Qt.InputMethodHints f)'''
            return Qt.InputMethodHints()
        def __iand__(self, mask):
            '''Qt.InputMethodHints Qt.InputMethodHints.__iand__(int mask)'''
            return Qt.InputMethodHints()
    class MatchFlags():
        """"""
        def __init__(self):
            '''Qt.MatchFlags Qt.MatchFlags.__init__()'''
            return Qt.MatchFlags()
        def __init__(self):
            '''int Qt.MatchFlags.__init__()'''
            return int()
        def __init__(self):
            '''void Qt.MatchFlags.__init__()'''
        def __bool__(self):
            '''int Qt.MatchFlags.__bool__()'''
            return int()
        def __ne__(self, f):
            '''bool Qt.MatchFlags.__ne__(Qt.MatchFlags f)'''
            return bool()
        def __eq__(self, f):
            '''bool Qt.MatchFlags.__eq__(Qt.MatchFlags f)'''
            return bool()
        def __invert__(self):
            '''Qt.MatchFlags Qt.MatchFlags.__invert__()'''
            return Qt.MatchFlags()
        def __and__(self, mask):
            '''Qt.MatchFlags Qt.MatchFlags.__and__(int mask)'''
            return Qt.MatchFlags()
        def __xor__(self, f):
            '''Qt.MatchFlags Qt.MatchFlags.__xor__(Qt.MatchFlags f)'''
            return Qt.MatchFlags()
        def __xor__(self, f):
            '''Qt.MatchFlags Qt.MatchFlags.__xor__(int f)'''
            return Qt.MatchFlags()
        def __or__(self, f):
            '''Qt.MatchFlags Qt.MatchFlags.__or__(Qt.MatchFlags f)'''
            return Qt.MatchFlags()
        def __or__(self, f):
            '''Qt.MatchFlags Qt.MatchFlags.__or__(int f)'''
            return Qt.MatchFlags()
        def __int__(self):
            '''int Qt.MatchFlags.__int__()'''
            return int()
        def __ixor__(self, f):
            '''Qt.MatchFlags Qt.MatchFlags.__ixor__(Qt.MatchFlags f)'''
            return Qt.MatchFlags()
        def __ior__(self, f):
            '''Qt.MatchFlags Qt.MatchFlags.__ior__(Qt.MatchFlags f)'''
            return Qt.MatchFlags()
        def __iand__(self, mask):
            '''Qt.MatchFlags Qt.MatchFlags.__iand__(int mask)'''
            return Qt.MatchFlags()
    class ItemFlags():
        """"""
        def __init__(self):
            '''Qt.ItemFlags Qt.ItemFlags.__init__()'''
            return Qt.ItemFlags()
        def __init__(self):
            '''int Qt.ItemFlags.__init__()'''
            return int()
        def __init__(self):
            '''void Qt.ItemFlags.__init__()'''
        def __bool__(self):
            '''int Qt.ItemFlags.__bool__()'''
            return int()
        def __ne__(self, f):
            '''bool Qt.ItemFlags.__ne__(Qt.ItemFlags f)'''
            return bool()
        def __eq__(self, f):
            '''bool Qt.ItemFlags.__eq__(Qt.ItemFlags f)'''
            return bool()
        def __invert__(self):
            '''Qt.ItemFlags Qt.ItemFlags.__invert__()'''
            return Qt.ItemFlags()
        def __and__(self, mask):
            '''Qt.ItemFlags Qt.ItemFlags.__and__(int mask)'''
            return Qt.ItemFlags()
        def __xor__(self, f):
            '''Qt.ItemFlags Qt.ItemFlags.__xor__(Qt.ItemFlags f)'''
            return Qt.ItemFlags()
        def __xor__(self, f):
            '''Qt.ItemFlags Qt.ItemFlags.__xor__(int f)'''
            return Qt.ItemFlags()
        def __or__(self, f):
            '''Qt.ItemFlags Qt.ItemFlags.__or__(Qt.ItemFlags f)'''
            return Qt.ItemFlags()
        def __or__(self, f):
            '''Qt.ItemFlags Qt.ItemFlags.__or__(int f)'''
            return Qt.ItemFlags()
        def __int__(self):
            '''int Qt.ItemFlags.__int__()'''
            return int()
        def __ixor__(self, f):
            '''Qt.ItemFlags Qt.ItemFlags.__ixor__(Qt.ItemFlags f)'''
            return Qt.ItemFlags()
        def __ior__(self, f):
            '''Qt.ItemFlags Qt.ItemFlags.__ior__(Qt.ItemFlags f)'''
            return Qt.ItemFlags()
        def __iand__(self, mask):
            '''Qt.ItemFlags Qt.ItemFlags.__iand__(int mask)'''
            return Qt.ItemFlags()
    class MouseButtons():
        """"""
        def __init__(self):
            '''Qt.MouseButtons Qt.MouseButtons.__init__()'''
            return Qt.MouseButtons()
        def __init__(self):
            '''int Qt.MouseButtons.__init__()'''
            return int()
        def __init__(self):
            '''void Qt.MouseButtons.__init__()'''
        def __bool__(self):
            '''int Qt.MouseButtons.__bool__()'''
            return int()
        def __ne__(self, f):
            '''bool Qt.MouseButtons.__ne__(Qt.MouseButtons f)'''
            return bool()
        def __eq__(self, f):
            '''bool Qt.MouseButtons.__eq__(Qt.MouseButtons f)'''
            return bool()
        def __invert__(self):
            '''Qt.MouseButtons Qt.MouseButtons.__invert__()'''
            return Qt.MouseButtons()
        def __and__(self, mask):
            '''Qt.MouseButtons Qt.MouseButtons.__and__(int mask)'''
            return Qt.MouseButtons()
        def __xor__(self, f):
            '''Qt.MouseButtons Qt.MouseButtons.__xor__(Qt.MouseButtons f)'''
            return Qt.MouseButtons()
        def __xor__(self, f):
            '''Qt.MouseButtons Qt.MouseButtons.__xor__(int f)'''
            return Qt.MouseButtons()
        def __or__(self, f):
            '''Qt.MouseButtons Qt.MouseButtons.__or__(Qt.MouseButtons f)'''
            return Qt.MouseButtons()
        def __or__(self, f):
            '''Qt.MouseButtons Qt.MouseButtons.__or__(int f)'''
            return Qt.MouseButtons()
        def __int__(self):
            '''int Qt.MouseButtons.__int__()'''
            return int()
        def __ixor__(self, f):
            '''Qt.MouseButtons Qt.MouseButtons.__ixor__(Qt.MouseButtons f)'''
            return Qt.MouseButtons()
        def __ior__(self, f):
            '''Qt.MouseButtons Qt.MouseButtons.__ior__(Qt.MouseButtons f)'''
            return Qt.MouseButtons()
        def __iand__(self, mask):
            '''Qt.MouseButtons Qt.MouseButtons.__iand__(int mask)'''
            return Qt.MouseButtons()
    class KeyboardModifiers():
        """"""
        def __init__(self):
            '''Qt.KeyboardModifiers Qt.KeyboardModifiers.__init__()'''
            return Qt.KeyboardModifiers()
        def __init__(self):
            '''int Qt.KeyboardModifiers.__init__()'''
            return int()
        def __init__(self):
            '''void Qt.KeyboardModifiers.__init__()'''
        def __bool__(self):
            '''int Qt.KeyboardModifiers.__bool__()'''
            return int()
        def __ne__(self, f):
            '''bool Qt.KeyboardModifiers.__ne__(Qt.KeyboardModifiers f)'''
            return bool()
        def __eq__(self, f):
            '''bool Qt.KeyboardModifiers.__eq__(Qt.KeyboardModifiers f)'''
            return bool()
        def __invert__(self):
            '''Qt.KeyboardModifiers Qt.KeyboardModifiers.__invert__()'''
            return Qt.KeyboardModifiers()
        def __and__(self, mask):
            '''Qt.KeyboardModifiers Qt.KeyboardModifiers.__and__(int mask)'''
            return Qt.KeyboardModifiers()
        def __xor__(self, f):
            '''Qt.KeyboardModifiers Qt.KeyboardModifiers.__xor__(Qt.KeyboardModifiers f)'''
            return Qt.KeyboardModifiers()
        def __xor__(self, f):
            '''Qt.KeyboardModifiers Qt.KeyboardModifiers.__xor__(int f)'''
            return Qt.KeyboardModifiers()
        def __or__(self, f):
            '''Qt.KeyboardModifiers Qt.KeyboardModifiers.__or__(Qt.KeyboardModifiers f)'''
            return Qt.KeyboardModifiers()
        def __or__(self, f):
            '''Qt.KeyboardModifiers Qt.KeyboardModifiers.__or__(int f)'''
            return Qt.KeyboardModifiers()
        def __int__(self):
            '''int Qt.KeyboardModifiers.__int__()'''
            return int()
        def __ixor__(self, f):
            '''Qt.KeyboardModifiers Qt.KeyboardModifiers.__ixor__(Qt.KeyboardModifiers f)'''
            return Qt.KeyboardModifiers()
        def __ior__(self, f):
            '''Qt.KeyboardModifiers Qt.KeyboardModifiers.__ior__(Qt.KeyboardModifiers f)'''
            return Qt.KeyboardModifiers()
        def __iand__(self, mask):
            '''Qt.KeyboardModifiers Qt.KeyboardModifiers.__iand__(int mask)'''
            return Qt.KeyboardModifiers()
    class DropActions():
        """"""
        def __init__(self):
            '''Qt.DropActions Qt.DropActions.__init__()'''
            return Qt.DropActions()
        def __init__(self):
            '''int Qt.DropActions.__init__()'''
            return int()
        def __init__(self):
            '''void Qt.DropActions.__init__()'''
        def __bool__(self):
            '''int Qt.DropActions.__bool__()'''
            return int()
        def __ne__(self, f):
            '''bool Qt.DropActions.__ne__(Qt.DropActions f)'''
            return bool()
        def __eq__(self, f):
            '''bool Qt.DropActions.__eq__(Qt.DropActions f)'''
            return bool()
        def __invert__(self):
            '''Qt.DropActions Qt.DropActions.__invert__()'''
            return Qt.DropActions()
        def __and__(self, mask):
            '''Qt.DropActions Qt.DropActions.__and__(int mask)'''
            return Qt.DropActions()
        def __xor__(self, f):
            '''Qt.DropActions Qt.DropActions.__xor__(Qt.DropActions f)'''
            return Qt.DropActions()
        def __xor__(self, f):
            '''Qt.DropActions Qt.DropActions.__xor__(int f)'''
            return Qt.DropActions()
        def __or__(self, f):
            '''Qt.DropActions Qt.DropActions.__or__(Qt.DropActions f)'''
            return Qt.DropActions()
        def __or__(self, f):
            '''Qt.DropActions Qt.DropActions.__or__(int f)'''
            return Qt.DropActions()
        def __int__(self):
            '''int Qt.DropActions.__int__()'''
            return int()
        def __ixor__(self, f):
            '''Qt.DropActions Qt.DropActions.__ixor__(Qt.DropActions f)'''
            return Qt.DropActions()
        def __ior__(self, f):
            '''Qt.DropActions Qt.DropActions.__ior__(Qt.DropActions f)'''
            return Qt.DropActions()
        def __iand__(self, mask):
            '''Qt.DropActions Qt.DropActions.__iand__(int mask)'''
            return Qt.DropActions()
    class DockWidgetAreas():
        """"""
        def __init__(self):
            '''Qt.DockWidgetAreas Qt.DockWidgetAreas.__init__()'''
            return Qt.DockWidgetAreas()
        def __init__(self):
            '''int Qt.DockWidgetAreas.__init__()'''
            return int()
        def __init__(self):
            '''void Qt.DockWidgetAreas.__init__()'''
        def __bool__(self):
            '''int Qt.DockWidgetAreas.__bool__()'''
            return int()
        def __ne__(self, f):
            '''bool Qt.DockWidgetAreas.__ne__(Qt.DockWidgetAreas f)'''
            return bool()
        def __eq__(self, f):
            '''bool Qt.DockWidgetAreas.__eq__(Qt.DockWidgetAreas f)'''
            return bool()
        def __invert__(self):
            '''Qt.DockWidgetAreas Qt.DockWidgetAreas.__invert__()'''
            return Qt.DockWidgetAreas()
        def __and__(self, mask):
            '''Qt.DockWidgetAreas Qt.DockWidgetAreas.__and__(int mask)'''
            return Qt.DockWidgetAreas()
        def __xor__(self, f):
            '''Qt.DockWidgetAreas Qt.DockWidgetAreas.__xor__(Qt.DockWidgetAreas f)'''
            return Qt.DockWidgetAreas()
        def __xor__(self, f):
            '''Qt.DockWidgetAreas Qt.DockWidgetAreas.__xor__(int f)'''
            return Qt.DockWidgetAreas()
        def __or__(self, f):
            '''Qt.DockWidgetAreas Qt.DockWidgetAreas.__or__(Qt.DockWidgetAreas f)'''
            return Qt.DockWidgetAreas()
        def __or__(self, f):
            '''Qt.DockWidgetAreas Qt.DockWidgetAreas.__or__(int f)'''
            return Qt.DockWidgetAreas()
        def __int__(self):
            '''int Qt.DockWidgetAreas.__int__()'''
            return int()
        def __ixor__(self, f):
            '''Qt.DockWidgetAreas Qt.DockWidgetAreas.__ixor__(Qt.DockWidgetAreas f)'''
            return Qt.DockWidgetAreas()
        def __ior__(self, f):
            '''Qt.DockWidgetAreas Qt.DockWidgetAreas.__ior__(Qt.DockWidgetAreas f)'''
            return Qt.DockWidgetAreas()
        def __iand__(self, mask):
            '''Qt.DockWidgetAreas Qt.DockWidgetAreas.__iand__(int mask)'''
            return Qt.DockWidgetAreas()
    class Orientations():
        """"""
        def __init__(self):
            '''Qt.Orientations Qt.Orientations.__init__()'''
            return Qt.Orientations()
        def __init__(self):
            '''int Qt.Orientations.__init__()'''
            return int()
        def __init__(self):
            '''void Qt.Orientations.__init__()'''
        def __bool__(self):
            '''int Qt.Orientations.__bool__()'''
            return int()
        def __ne__(self, f):
            '''bool Qt.Orientations.__ne__(Qt.Orientations f)'''
            return bool()
        def __eq__(self, f):
            '''bool Qt.Orientations.__eq__(Qt.Orientations f)'''
            return bool()
        def __invert__(self):
            '''Qt.Orientations Qt.Orientations.__invert__()'''
            return Qt.Orientations()
        def __and__(self, mask):
            '''Qt.Orientations Qt.Orientations.__and__(int mask)'''
            return Qt.Orientations()
        def __xor__(self, f):
            '''Qt.Orientations Qt.Orientations.__xor__(Qt.Orientations f)'''
            return Qt.Orientations()
        def __xor__(self, f):
            '''Qt.Orientations Qt.Orientations.__xor__(int f)'''
            return Qt.Orientations()
        def __or__(self, f):
            '''Qt.Orientations Qt.Orientations.__or__(Qt.Orientations f)'''
            return Qt.Orientations()
        def __or__(self, f):
            '''Qt.Orientations Qt.Orientations.__or__(int f)'''
            return Qt.Orientations()
        def __int__(self):
            '''int Qt.Orientations.__int__()'''
            return int()
        def __ixor__(self, f):
            '''Qt.Orientations Qt.Orientations.__ixor__(Qt.Orientations f)'''
            return Qt.Orientations()
        def __ior__(self, f):
            '''Qt.Orientations Qt.Orientations.__ior__(Qt.Orientations f)'''
            return Qt.Orientations()
        def __iand__(self, mask):
            '''Qt.Orientations Qt.Orientations.__iand__(int mask)'''
            return Qt.Orientations()
    class TextInteractionFlags():
        """"""
        def __init__(self):
            '''Qt.TextInteractionFlags Qt.TextInteractionFlags.__init__()'''
            return Qt.TextInteractionFlags()
        def __init__(self):
            '''int Qt.TextInteractionFlags.__init__()'''
            return int()
        def __init__(self):
            '''void Qt.TextInteractionFlags.__init__()'''
        def __bool__(self):
            '''int Qt.TextInteractionFlags.__bool__()'''
            return int()
        def __ne__(self, f):
            '''bool Qt.TextInteractionFlags.__ne__(Qt.TextInteractionFlags f)'''
            return bool()
        def __eq__(self, f):
            '''bool Qt.TextInteractionFlags.__eq__(Qt.TextInteractionFlags f)'''
            return bool()
        def __invert__(self):
            '''Qt.TextInteractionFlags Qt.TextInteractionFlags.__invert__()'''
            return Qt.TextInteractionFlags()
        def __and__(self, mask):
            '''Qt.TextInteractionFlags Qt.TextInteractionFlags.__and__(int mask)'''
            return Qt.TextInteractionFlags()
        def __xor__(self, f):
            '''Qt.TextInteractionFlags Qt.TextInteractionFlags.__xor__(Qt.TextInteractionFlags f)'''
            return Qt.TextInteractionFlags()
        def __xor__(self, f):
            '''Qt.TextInteractionFlags Qt.TextInteractionFlags.__xor__(int f)'''
            return Qt.TextInteractionFlags()
        def __or__(self, f):
            '''Qt.TextInteractionFlags Qt.TextInteractionFlags.__or__(Qt.TextInteractionFlags f)'''
            return Qt.TextInteractionFlags()
        def __or__(self, f):
            '''Qt.TextInteractionFlags Qt.TextInteractionFlags.__or__(int f)'''
            return Qt.TextInteractionFlags()
        def __int__(self):
            '''int Qt.TextInteractionFlags.__int__()'''
            return int()
        def __ixor__(self, f):
            '''Qt.TextInteractionFlags Qt.TextInteractionFlags.__ixor__(Qt.TextInteractionFlags f)'''
            return Qt.TextInteractionFlags()
        def __ior__(self, f):
            '''Qt.TextInteractionFlags Qt.TextInteractionFlags.__ior__(Qt.TextInteractionFlags f)'''
            return Qt.TextInteractionFlags()
        def __iand__(self, mask):
            '''Qt.TextInteractionFlags Qt.TextInteractionFlags.__iand__(int mask)'''
            return Qt.TextInteractionFlags()
    class GestureFlags():
        """"""
        def __init__(self):
            '''Qt.GestureFlags Qt.GestureFlags.__init__()'''
            return Qt.GestureFlags()
        def __init__(self):
            '''int Qt.GestureFlags.__init__()'''
            return int()
        def __init__(self):
            '''void Qt.GestureFlags.__init__()'''
        def __bool__(self):
            '''int Qt.GestureFlags.__bool__()'''
            return int()
        def __ne__(self, f):
            '''bool Qt.GestureFlags.__ne__(Qt.GestureFlags f)'''
            return bool()
        def __eq__(self, f):
            '''bool Qt.GestureFlags.__eq__(Qt.GestureFlags f)'''
            return bool()
        def __invert__(self):
            '''Qt.GestureFlags Qt.GestureFlags.__invert__()'''
            return Qt.GestureFlags()
        def __and__(self, mask):
            '''Qt.GestureFlags Qt.GestureFlags.__and__(int mask)'''
            return Qt.GestureFlags()
        def __xor__(self, f):
            '''Qt.GestureFlags Qt.GestureFlags.__xor__(Qt.GestureFlags f)'''
            return Qt.GestureFlags()
        def __xor__(self, f):
            '''Qt.GestureFlags Qt.GestureFlags.__xor__(int f)'''
            return Qt.GestureFlags()
        def __or__(self, f):
            '''Qt.GestureFlags Qt.GestureFlags.__or__(Qt.GestureFlags f)'''
            return Qt.GestureFlags()
        def __or__(self, f):
            '''Qt.GestureFlags Qt.GestureFlags.__or__(int f)'''
            return Qt.GestureFlags()
        def __int__(self):
            '''int Qt.GestureFlags.__int__()'''
            return int()
        def __ixor__(self, f):
            '''Qt.GestureFlags Qt.GestureFlags.__ixor__(Qt.GestureFlags f)'''
            return Qt.GestureFlags()
        def __ior__(self, f):
            '''Qt.GestureFlags Qt.GestureFlags.__ior__(Qt.GestureFlags f)'''
            return Qt.GestureFlags()
        def __iand__(self, mask):
            '''Qt.GestureFlags Qt.GestureFlags.__iand__(int mask)'''
            return Qt.GestureFlags()
    class Alignment():
        """"""
        def __init__(self):
            '''Qt.Alignment Qt.Alignment.__init__()'''
            return Qt.Alignment()
        def __init__(self):
            '''int Qt.Alignment.__init__()'''
            return int()
        def __init__(self):
            '''void Qt.Alignment.__init__()'''
        def __bool__(self):
            '''int Qt.Alignment.__bool__()'''
            return int()
        def __ne__(self, f):
            '''bool Qt.Alignment.__ne__(Qt.Alignment f)'''
            return bool()
        def __eq__(self, f):
            '''bool Qt.Alignment.__eq__(Qt.Alignment f)'''
            return bool()
        def __invert__(self):
            '''Qt.Alignment Qt.Alignment.__invert__()'''
            return Qt.Alignment()
        def __and__(self, mask):
            '''Qt.Alignment Qt.Alignment.__and__(int mask)'''
            return Qt.Alignment()
        def __xor__(self, f):
            '''Qt.Alignment Qt.Alignment.__xor__(Qt.Alignment f)'''
            return Qt.Alignment()
        def __xor__(self, f):
            '''Qt.Alignment Qt.Alignment.__xor__(int f)'''
            return Qt.Alignment()
        def __or__(self, f):
            '''Qt.Alignment Qt.Alignment.__or__(Qt.Alignment f)'''
            return Qt.Alignment()
        def __or__(self, f):
            '''Qt.Alignment Qt.Alignment.__or__(int f)'''
            return Qt.Alignment()
        def __int__(self):
            '''int Qt.Alignment.__int__()'''
            return int()
        def __ixor__(self, f):
            '''Qt.Alignment Qt.Alignment.__ixor__(Qt.Alignment f)'''
            return Qt.Alignment()
        def __ior__(self, f):
            '''Qt.Alignment Qt.Alignment.__ior__(Qt.Alignment f)'''
            return Qt.Alignment()
        def __iand__(self, mask):
            '''Qt.Alignment Qt.Alignment.__iand__(int mask)'''
            return Qt.Alignment()
    class ImageConversionFlags():
        """"""
        def __init__(self):
            '''Qt.ImageConversionFlags Qt.ImageConversionFlags.__init__()'''
            return Qt.ImageConversionFlags()
        def __init__(self):
            '''int Qt.ImageConversionFlags.__init__()'''
            return int()
        def __init__(self):
            '''void Qt.ImageConversionFlags.__init__()'''
        def __bool__(self):
            '''int Qt.ImageConversionFlags.__bool__()'''
            return int()
        def __ne__(self, f):
            '''bool Qt.ImageConversionFlags.__ne__(Qt.ImageConversionFlags f)'''
            return bool()
        def __eq__(self, f):
            '''bool Qt.ImageConversionFlags.__eq__(Qt.ImageConversionFlags f)'''
            return bool()
        def __invert__(self):
            '''Qt.ImageConversionFlags Qt.ImageConversionFlags.__invert__()'''
            return Qt.ImageConversionFlags()
        def __and__(self, mask):
            '''Qt.ImageConversionFlags Qt.ImageConversionFlags.__and__(int mask)'''
            return Qt.ImageConversionFlags()
        def __xor__(self, f):
            '''Qt.ImageConversionFlags Qt.ImageConversionFlags.__xor__(Qt.ImageConversionFlags f)'''
            return Qt.ImageConversionFlags()
        def __xor__(self, f):
            '''Qt.ImageConversionFlags Qt.ImageConversionFlags.__xor__(int f)'''
            return Qt.ImageConversionFlags()
        def __or__(self, f):
            '''Qt.ImageConversionFlags Qt.ImageConversionFlags.__or__(Qt.ImageConversionFlags f)'''
            return Qt.ImageConversionFlags()
        def __or__(self, f):
            '''Qt.ImageConversionFlags Qt.ImageConversionFlags.__or__(int f)'''
            return Qt.ImageConversionFlags()
        def __int__(self):
            '''int Qt.ImageConversionFlags.__int__()'''
            return int()
        def __ixor__(self, f):
            '''Qt.ImageConversionFlags Qt.ImageConversionFlags.__ixor__(Qt.ImageConversionFlags f)'''
            return Qt.ImageConversionFlags()
        def __ior__(self, f):
            '''Qt.ImageConversionFlags Qt.ImageConversionFlags.__ior__(Qt.ImageConversionFlags f)'''
            return Qt.ImageConversionFlags()
        def __iand__(self, mask):
            '''Qt.ImageConversionFlags Qt.ImageConversionFlags.__iand__(int mask)'''
            return Qt.ImageConversionFlags()
    class TouchPointStates():
        """"""
        def __init__(self):
            '''Qt.TouchPointStates Qt.TouchPointStates.__init__()'''
            return Qt.TouchPointStates()
        def __init__(self):
            '''int Qt.TouchPointStates.__init__()'''
            return int()
        def __init__(self):
            '''void Qt.TouchPointStates.__init__()'''
        def __bool__(self):
            '''int Qt.TouchPointStates.__bool__()'''
            return int()
        def __ne__(self, f):
            '''bool Qt.TouchPointStates.__ne__(Qt.TouchPointStates f)'''
            return bool()
        def __eq__(self, f):
            '''bool Qt.TouchPointStates.__eq__(Qt.TouchPointStates f)'''
            return bool()
        def __invert__(self):
            '''Qt.TouchPointStates Qt.TouchPointStates.__invert__()'''
            return Qt.TouchPointStates()
        def __and__(self, mask):
            '''Qt.TouchPointStates Qt.TouchPointStates.__and__(int mask)'''
            return Qt.TouchPointStates()
        def __xor__(self, f):
            '''Qt.TouchPointStates Qt.TouchPointStates.__xor__(Qt.TouchPointStates f)'''
            return Qt.TouchPointStates()
        def __xor__(self, f):
            '''Qt.TouchPointStates Qt.TouchPointStates.__xor__(int f)'''
            return Qt.TouchPointStates()
        def __or__(self, f):
            '''Qt.TouchPointStates Qt.TouchPointStates.__or__(Qt.TouchPointStates f)'''
            return Qt.TouchPointStates()
        def __or__(self, f):
            '''Qt.TouchPointStates Qt.TouchPointStates.__or__(int f)'''
            return Qt.TouchPointStates()
        def __int__(self):
            '''int Qt.TouchPointStates.__int__()'''
            return int()
        def __ixor__(self, f):
            '''Qt.TouchPointStates Qt.TouchPointStates.__ixor__(Qt.TouchPointStates f)'''
            return Qt.TouchPointStates()
        def __ior__(self, f):
            '''Qt.TouchPointStates Qt.TouchPointStates.__ior__(Qt.TouchPointStates f)'''
            return Qt.TouchPointStates()
        def __iand__(self, mask):
            '''Qt.TouchPointStates Qt.TouchPointStates.__iand__(int mask)'''
            return Qt.TouchPointStates()
    class WindowStates():
        """"""
        def __init__(self):
            '''Qt.WindowStates Qt.WindowStates.__init__()'''
            return Qt.WindowStates()
        def __init__(self):
            '''int Qt.WindowStates.__init__()'''
            return int()
        def __init__(self):
            '''void Qt.WindowStates.__init__()'''
        def __bool__(self):
            '''int Qt.WindowStates.__bool__()'''
            return int()
        def __ne__(self, f):
            '''bool Qt.WindowStates.__ne__(Qt.WindowStates f)'''
            return bool()
        def __eq__(self, f):
            '''bool Qt.WindowStates.__eq__(Qt.WindowStates f)'''
            return bool()
        def __invert__(self):
            '''Qt.WindowStates Qt.WindowStates.__invert__()'''
            return Qt.WindowStates()
        def __and__(self, mask):
            '''Qt.WindowStates Qt.WindowStates.__and__(int mask)'''
            return Qt.WindowStates()
        def __xor__(self, f):
            '''Qt.WindowStates Qt.WindowStates.__xor__(Qt.WindowStates f)'''
            return Qt.WindowStates()
        def __xor__(self, f):
            '''Qt.WindowStates Qt.WindowStates.__xor__(int f)'''
            return Qt.WindowStates()
        def __or__(self, f):
            '''Qt.WindowStates Qt.WindowStates.__or__(Qt.WindowStates f)'''
            return Qt.WindowStates()
        def __or__(self, f):
            '''Qt.WindowStates Qt.WindowStates.__or__(int f)'''
            return Qt.WindowStates()
        def __int__(self):
            '''int Qt.WindowStates.__int__()'''
            return int()
        def __ixor__(self, f):
            '''Qt.WindowStates Qt.WindowStates.__ixor__(Qt.WindowStates f)'''
            return Qt.WindowStates()
        def __ior__(self, f):
            '''Qt.WindowStates Qt.WindowStates.__ior__(Qt.WindowStates f)'''
            return Qt.WindowStates()
        def __iand__(self, mask):
            '''Qt.WindowStates Qt.WindowStates.__iand__(int mask)'''
            return Qt.WindowStates()


class QObject():
    """"""
    staticMetaObject = None # QMetaObject - member
    def __init__(self, parent = None):
        '''void QObject.__init__(QObject parent = None)'''
    def senderSignalIndex(self):
        '''int QObject.senderSignalIndex()'''
        return int()
    def disconnectNotify(self, signal):
        '''void QObject.disconnectNotify(SIGNAL() signal)'''
    def connectNotify(self, signal):
        '''void QObject.connectNotify(SIGNAL() signal)'''
    def customEvent(self):
        '''QEvent QObject.customEvent()'''
        return QEvent()
    def childEvent(self):
        '''QChildEvent QObject.childEvent()'''
        return QChildEvent()
    def timerEvent(self):
        '''QTimerEvent QObject.timerEvent()'''
        return QTimerEvent()
    def receivers(self, signal):
        '''int QObject.receivers(SIGNAL() signal)'''
        return int()
    def sender(self):
        '''QObject QObject.sender()'''
        return QObject()
    def deleteLater(self):
        '''void QObject.deleteLater()'''
    def inherits(self, classname):
        '''bool QObject.inherits(str classname)'''
        return bool()
    def parent(self):
        '''QObject QObject.parent()'''
        return QObject()
    destroyed = pyqtSignal() # void destroyed(QObject * = 0) - signal
    def property(self, name):
        '''QVariant QObject.property(str name)'''
        return QVariant()
    def setProperty(self, name, value):
        '''bool QObject.setProperty(str name, QVariant value)'''
        return bool()
    def dynamicPropertyNames(self):
        '''list-of-QByteArray QObject.dynamicPropertyNames()'''
        return [QByteArray()]
    def dumpObjectTree(self):
        '''void QObject.dumpObjectTree()'''
    def dumpObjectInfo(self):
        '''void QObject.dumpObjectInfo()'''
    def disconnect(self):
        '''static SLOT() QObject.disconnect()'''
        return SLOT()()
    def disconnect(self):
        '''static callable QObject.disconnect()'''
        return callable()
    def connect(self):
        '''static Qt.ConnectionType QObject.connect()'''
        return Qt.ConnectionType()
    def connect(self):
        '''static Qt.ConnectionType QObject.connect()'''
        return Qt.ConnectionType()
    def connect(self):
        '''Qt.ConnectionType QObject.connect()'''
        return Qt.ConnectionType()
    def removeEventFilter(self):
        '''QObject QObject.removeEventFilter()'''
        return QObject()
    def installEventFilter(self):
        '''QObject QObject.installEventFilter()'''
        return QObject()
    def setParent(self):
        '''QObject QObject.setParent()'''
        return QObject()
    def children(self):
        '''list-of-QObject QObject.children()'''
        return [QObject()]
    def killTimer(self, id):
        '''void QObject.killTimer(int id)'''
    def startTimer(self, interval):
        '''int QObject.startTimer(int interval)'''
        return int()
    def moveToThread(self, thread):
        '''void QObject.moveToThread(QThread thread)'''
    def thread(self):
        '''QThread QObject.thread()'''
        return QThread()
    def blockSignals(self, b):
        '''bool QObject.blockSignals(bool b)'''
        return bool()
    def signalsBlocked(self):
        '''bool QObject.signalsBlocked()'''
        return bool()
    def isWidgetType(self):
        '''bool QObject.isWidgetType()'''
        return bool()
    def setObjectName(self, name):
        '''void QObject.setObjectName(QString name)'''
    def objectName(self):
        '''QString QObject.objectName()'''
        return QString()
    def emit(self, *args):
        '''SIGNAL() QObject.emit(... *args)'''
        return SIGNAL()()
    def findChildren(self, type, name = QString()):
        '''list-of-QObject QObject.findChildren(type type, QString name = QString())'''
        return [QObject()]
    def findChildren(self, types, name = QString()):
        '''list-of-QObject QObject.findChildren(tuple types, QString name = QString())'''
        return [QObject()]
    def findChildren(self, type, regExp):
        '''list-of-QObject QObject.findChildren(type type, QRegExp regExp)'''
        return [QObject()]
    def findChildren(self, types, regExp):
        '''list-of-QObject QObject.findChildren(tuple types, QRegExp regExp)'''
        return [QObject()]
    def findChild(self, type, name = QString()):
        '''QObject QObject.findChild(type type, QString name = QString())'''
        return QObject()
    def findChild(self, types, name = QString()):
        '''QObject QObject.findChild(tuple types, QString name = QString())'''
        return QObject()
    def trUtf8(self, sourceText, disambiguation = None, n = -1):
        '''QString QObject.trUtf8(str sourceText, str disambiguation = None, int n = -1)'''
        return QString()
    def tr(self, sourceText, disambiguation = None, n = -1):
        '''QString QObject.tr(str sourceText, str disambiguation = None, int n = -1)'''
        return QString()
    def eventFilter(self):
        '''QEvent QObject.eventFilter()'''
        return QEvent()
    def event(self):
        '''QEvent QObject.event()'''
        return QEvent()
    def __getattr__(self, name):
        '''object QObject.__getattr__(str name)'''
        return object()
    def pyqtConfigure(self):
        '''object QObject.pyqtConfigure()'''
        return object()
    def metaObject(self):
        '''QMetaObject QObject.metaObject()'''
        return QMetaObject()


class QAbstractAnimation(QObject):
    """"""
    # Enum QAbstractAnimation.DeletionPolicy
    KeepWhenStopped = 0
    DeleteWhenStopped = 0

    # Enum QAbstractAnimation.State
    Stopped = 0
    Paused = 0
    Running = 0

    # Enum QAbstractAnimation.Direction
    Forward = 0
    Backward = 0

    def __init__(self, parent = None):
        '''void QAbstractAnimation.__init__(QObject parent = None)'''
    def updateDirection(self, direction):
        '''void QAbstractAnimation.updateDirection(QAbstractAnimation.Direction direction)'''
    def updateState(self, newState, oldState):
        '''void QAbstractAnimation.updateState(QAbstractAnimation.State newState, QAbstractAnimation.State oldState)'''
    def updateCurrentTime(self, currentTime):
        '''abstract void QAbstractAnimation.updateCurrentTime(int currentTime)'''
    def event(self, event):
        '''bool QAbstractAnimation.event(QEvent event)'''
        return bool()
    def setCurrentTime(self, msecs):
        '''void QAbstractAnimation.setCurrentTime(int msecs)'''
    def stop(self):
        '''void QAbstractAnimation.stop()'''
    def setPaused(self):
        '''bool QAbstractAnimation.setPaused()'''
        return bool()
    def resume(self):
        '''void QAbstractAnimation.resume()'''
    def pause(self):
        '''void QAbstractAnimation.pause()'''
    def start(self, policy = QAbstractAnimation.KeepWhenStopped):
        '''void QAbstractAnimation.start(QAbstractAnimation.DeletionPolicy policy = QAbstractAnimation.KeepWhenStopped)'''
    directionChanged = pyqtSignal() # void directionChanged(QAbstractAnimation::Direction) - signal
    currentLoopChanged = pyqtSignal() # void currentLoopChanged(int) - signal
    stateChanged = pyqtSignal() # void stateChanged(QAbstractAnimation::State,QAbstractAnimation::State) - signal
    finished = pyqtSignal() # void finished() - signal
    def totalDuration(self):
        '''int QAbstractAnimation.totalDuration()'''
        return int()
    def duration(self):
        '''abstract int QAbstractAnimation.duration()'''
        return int()
    def currentLoop(self):
        '''int QAbstractAnimation.currentLoop()'''
        return int()
    def setLoopCount(self, loopCount):
        '''void QAbstractAnimation.setLoopCount(int loopCount)'''
    def loopCount(self):
        '''int QAbstractAnimation.loopCount()'''
        return int()
    def currentLoopTime(self):
        '''int QAbstractAnimation.currentLoopTime()'''
        return int()
    def currentTime(self):
        '''int QAbstractAnimation.currentTime()'''
        return int()
    def setDirection(self, direction):
        '''void QAbstractAnimation.setDirection(QAbstractAnimation.Direction direction)'''
    def direction(self):
        '''QAbstractAnimation.Direction QAbstractAnimation.direction()'''
        return QAbstractAnimation.Direction()
    def group(self):
        '''QAnimationGroup QAbstractAnimation.group()'''
        return QAnimationGroup()
    def state(self):
        '''QAbstractAnimation.State QAbstractAnimation.state()'''
        return QAbstractAnimation.State()


class QAbstractEventDispatcher(QObject):
    """"""
    def __init__(self, parent = None):
        '''void QAbstractEventDispatcher.__init__(QObject parent = None)'''
    awake = pyqtSignal() # void awake() - signal
    aboutToBlock = pyqtSignal() # void aboutToBlock() - signal
    def filterEvent(self, message):
        '''bool QAbstractEventDispatcher.filterEvent(sip.voidptr message)'''
        return bool()
    def setEventFilter(self, filter):
        '''callable QAbstractEventDispatcher.setEventFilter(callable filter)'''
        return callable()
    def closingDown(self):
        '''void QAbstractEventDispatcher.closingDown()'''
    def startingUp(self):
        '''void QAbstractEventDispatcher.startingUp()'''
    def flush(self):
        '''abstract void QAbstractEventDispatcher.flush()'''
    def interrupt(self):
        '''abstract void QAbstractEventDispatcher.interrupt()'''
    def wakeUp(self):
        '''abstract void QAbstractEventDispatcher.wakeUp()'''
    def registeredTimers(self, object):
        '''abstract list-of-tuple-of-int-int QAbstractEventDispatcher.registeredTimers(QObject object)'''
        return [tuple-of-int-int()]
    def unregisterTimers(self, object):
        '''abstract bool QAbstractEventDispatcher.unregisterTimers(QObject object)'''
        return bool()
    def unregisterTimer(self, timerId):
        '''abstract bool QAbstractEventDispatcher.unregisterTimer(int timerId)'''
        return bool()
    def registerTimer(self, interval, object):
        '''int QAbstractEventDispatcher.registerTimer(int interval, QObject object)'''
        return int()
    def registerTimer(self, timerId, interval, object):
        '''abstract void QAbstractEventDispatcher.registerTimer(int timerId, int interval, QObject object)'''
    def unregisterSocketNotifier(self, notifier):
        '''abstract void QAbstractEventDispatcher.unregisterSocketNotifier(QSocketNotifier notifier)'''
    def registerSocketNotifier(self, notifier):
        '''abstract void QAbstractEventDispatcher.registerSocketNotifier(QSocketNotifier notifier)'''
    def hasPendingEvents(self):
        '''abstract bool QAbstractEventDispatcher.hasPendingEvents()'''
        return bool()
    def processEvents(self, flags):
        '''abstract bool QAbstractEventDispatcher.processEvents(QEventLoop.ProcessEventsFlags flags)'''
        return bool()
    def instance(self, thread = None):
        '''static QAbstractEventDispatcher QAbstractEventDispatcher.instance(QThread thread = None)'''
        return QAbstractEventDispatcher()


class QAbstractFileEngine():
    """"""
    # Enum QAbstractFileEngine.FileTime
    CreationTime = 0
    ModificationTime = 0
    AccessTime = 0

    # Enum QAbstractFileEngine.FileOwner
    OwnerUser = 0
    OwnerGroup = 0

    # Enum QAbstractFileEngine.FileName
    DefaultName = 0
    BaseName = 0
    PathName = 0
    AbsoluteName = 0
    AbsolutePathName = 0
    LinkName = 0
    CanonicalName = 0
    CanonicalPathName = 0
    BundleName = 0

    # Enum QAbstractFileEngine.FileFlag
    ReadOwnerPerm = 0
    WriteOwnerPerm = 0
    ExeOwnerPerm = 0
    ReadUserPerm = 0
    WriteUserPerm = 0
    ExeUserPerm = 0
    ReadGroupPerm = 0
    WriteGroupPerm = 0
    ExeGroupPerm = 0
    ReadOtherPerm = 0
    WriteOtherPerm = 0
    ExeOtherPerm = 0
    LinkType = 0
    FileType = 0
    DirectoryType = 0
    HiddenFlag = 0
    LocalDiskFlag = 0
    ExistsFlag = 0
    RootFlag = 0
    PermsMask = 0
    TypesMask = 0
    FlagsMask = 0
    FileInfoAll = 0
    BundleType = 0
    Refresh = 0

    def __init__(self):
        '''void QAbstractFileEngine.__init__()'''
    def setError(self, error, str):
        '''void QAbstractFileEngine.setError(QFile.FileError error, QString str)'''
    def unmap(self, ptr):
        '''bool QAbstractFileEngine.unmap(sip.voidptr ptr)'''
        return bool()
    def map(self, offset, size, flags):
        '''sip.voidptr QAbstractFileEngine.map(int offset, int size, QFile.MemoryMapFlags flags)'''
        return sip.voidptr()
    def create(self, fileName):
        '''static QAbstractFileEngine QAbstractFileEngine.create(QString fileName)'''
        return QAbstractFileEngine()
    def errorString(self):
        '''QString QAbstractFileEngine.errorString()'''
        return QString()
    def error(self):
        '''QFile.FileError QAbstractFileEngine.error()'''
        return QFile.FileError()
    def write(self, data):
        '''int QAbstractFileEngine.write(str data)'''
        return int()
    def readLine(self, maxlen):
        '''str QAbstractFileEngine.readLine(int maxlen)'''
        return str()
    def read(self, maxlen):
        '''str QAbstractFileEngine.read(int maxlen)'''
        return str()
    def beginEntryList(self, filters, filterNames):
        '''QAbstractFileEngineIterator QAbstractFileEngine.beginEntryList(QDir.Filters filters, QStringList filterNames)'''
        return QAbstractFileEngineIterator()
    def handle(self):
        '''int QAbstractFileEngine.handle()'''
        return int()
    def setFileName(self, file):
        '''void QAbstractFileEngine.setFileName(QString file)'''
    def fileTime(self, time):
        '''QDateTime QAbstractFileEngine.fileTime(QAbstractFileEngine.FileTime time)'''
        return QDateTime()
    def owner(self):
        '''QAbstractFileEngine.FileOwner QAbstractFileEngine.owner()'''
        return QAbstractFileEngine.FileOwner()
    def ownerId(self):
        '''QAbstractFileEngine.FileOwner QAbstractFileEngine.ownerId()'''
        return QAbstractFileEngine.FileOwner()
    def fileName(self, file = QAbstractFileEngine.DefaultName):
        '''QString QAbstractFileEngine.fileName(QAbstractFileEngine.FileName file = QAbstractFileEngine.DefaultName)'''
        return QString()
    def setPermissions(self, perms):
        '''bool QAbstractFileEngine.setPermissions(int perms)'''
        return bool()
    def fileFlags(self, type = QAbstractFileEngine.FileInfoAll):
        '''QAbstractFileEngine.FileFlags QAbstractFileEngine.fileFlags(QAbstractFileEngine.FileFlags type = QAbstractFileEngine.FileInfoAll)'''
        return QAbstractFileEngine.FileFlags()
    def entryList(self, filters, filterNames):
        '''QStringList QAbstractFileEngine.entryList(QDir.Filters filters, QStringList filterNames)'''
        return QStringList()
    def isRelativePath(self):
        '''bool QAbstractFileEngine.isRelativePath()'''
        return bool()
    def caseSensitive(self):
        '''bool QAbstractFileEngine.caseSensitive()'''
        return bool()
    def setSize(self, size):
        '''bool QAbstractFileEngine.setSize(int size)'''
        return bool()
    def rmdir(self, dirName, recurseParentDirectories):
        '''bool QAbstractFileEngine.rmdir(QString dirName, bool recurseParentDirectories)'''
        return bool()
    def mkdir(self, dirName, createParentDirectories):
        '''bool QAbstractFileEngine.mkdir(QString dirName, bool createParentDirectories)'''
        return bool()
    def link(self, newName):
        '''bool QAbstractFileEngine.link(QString newName)'''
        return bool()
    def rename(self, newName):
        '''bool QAbstractFileEngine.rename(QString newName)'''
        return bool()
    def copy(self, newName):
        '''bool QAbstractFileEngine.copy(QString newName)'''
        return bool()
    def remove(self):
        '''bool QAbstractFileEngine.remove()'''
        return bool()
    def isSequential(self):
        '''bool QAbstractFileEngine.isSequential()'''
        return bool()
    def seek(self, pos):
        '''bool QAbstractFileEngine.seek(int pos)'''
        return bool()
    def pos(self):
        '''int QAbstractFileEngine.pos()'''
        return int()
    def size(self):
        '''int QAbstractFileEngine.size()'''
        return int()
    def flush(self):
        '''bool QAbstractFileEngine.flush()'''
        return bool()
    def close(self):
        '''bool QAbstractFileEngine.close()'''
        return bool()
    def open(self, openMode):
        '''bool QAbstractFileEngine.open(QIODevice.OpenMode openMode)'''
        return bool()
    def atEnd(self):
        '''bool QAbstractFileEngine.atEnd()'''
        return bool()
    class FileFlags():
        """"""
        def __init__(self):
            '''QAbstractFileEngine.FileFlags QAbstractFileEngine.FileFlags.__init__()'''
            return QAbstractFileEngine.FileFlags()
        def __init__(self):
            '''int QAbstractFileEngine.FileFlags.__init__()'''
            return int()
        def __init__(self):
            '''void QAbstractFileEngine.FileFlags.__init__()'''
        def __bool__(self):
            '''int QAbstractFileEngine.FileFlags.__bool__()'''
            return int()
        def __ne__(self, f):
            '''bool QAbstractFileEngine.FileFlags.__ne__(QAbstractFileEngine.FileFlags f)'''
            return bool()
        def __eq__(self, f):
            '''bool QAbstractFileEngine.FileFlags.__eq__(QAbstractFileEngine.FileFlags f)'''
            return bool()
        def __invert__(self):
            '''QAbstractFileEngine.FileFlags QAbstractFileEngine.FileFlags.__invert__()'''
            return QAbstractFileEngine.FileFlags()
        def __and__(self, mask):
            '''QAbstractFileEngine.FileFlags QAbstractFileEngine.FileFlags.__and__(int mask)'''
            return QAbstractFileEngine.FileFlags()
        def __xor__(self, f):
            '''QAbstractFileEngine.FileFlags QAbstractFileEngine.FileFlags.__xor__(QAbstractFileEngine.FileFlags f)'''
            return QAbstractFileEngine.FileFlags()
        def __xor__(self, f):
            '''QAbstractFileEngine.FileFlags QAbstractFileEngine.FileFlags.__xor__(int f)'''
            return QAbstractFileEngine.FileFlags()
        def __or__(self, f):
            '''QAbstractFileEngine.FileFlags QAbstractFileEngine.FileFlags.__or__(QAbstractFileEngine.FileFlags f)'''
            return QAbstractFileEngine.FileFlags()
        def __or__(self, f):
            '''QAbstractFileEngine.FileFlags QAbstractFileEngine.FileFlags.__or__(int f)'''
            return QAbstractFileEngine.FileFlags()
        def __int__(self):
            '''int QAbstractFileEngine.FileFlags.__int__()'''
            return int()
        def __ixor__(self, f):
            '''QAbstractFileEngine.FileFlags QAbstractFileEngine.FileFlags.__ixor__(QAbstractFileEngine.FileFlags f)'''
            return QAbstractFileEngine.FileFlags()
        def __ior__(self, f):
            '''QAbstractFileEngine.FileFlags QAbstractFileEngine.FileFlags.__ior__(QAbstractFileEngine.FileFlags f)'''
            return QAbstractFileEngine.FileFlags()
        def __iand__(self, mask):
            '''QAbstractFileEngine.FileFlags QAbstractFileEngine.FileFlags.__iand__(int mask)'''
            return QAbstractFileEngine.FileFlags()


class QAbstractFileEngineHandler():
    """"""
    def __init__(self):
        '''void QAbstractFileEngineHandler.__init__()'''
    def __init__(self):
        '''QAbstractFileEngineHandler QAbstractFileEngineHandler.__init__()'''
        return QAbstractFileEngineHandler()
    def create(self, fileName):
        '''abstract QAbstractFileEngine QAbstractFileEngineHandler.create(QString fileName)'''
        return QAbstractFileEngine()


class QAbstractFileEngineIterator():
    """"""
    def __init__(self, filters, nameFilters):
        '''void QAbstractFileEngineIterator.__init__(QDir.Filters filters, QStringList nameFilters)'''
    def currentFilePath(self):
        '''QString QAbstractFileEngineIterator.currentFilePath()'''
        return QString()
    def currentFileInfo(self):
        '''QFileInfo QAbstractFileEngineIterator.currentFileInfo()'''
        return QFileInfo()
    def currentFileName(self):
        '''abstract QString QAbstractFileEngineIterator.currentFileName()'''
        return QString()
    def filters(self):
        '''QDir.Filters QAbstractFileEngineIterator.filters()'''
        return QDir.Filters()
    def nameFilters(self):
        '''QStringList QAbstractFileEngineIterator.nameFilters()'''
        return QStringList()
    def path(self):
        '''QString QAbstractFileEngineIterator.path()'''
        return QString()
    def hasNext(self):
        '''abstract bool QAbstractFileEngineIterator.hasNext()'''
        return bool()
    def next(self):
        '''abstract QString QAbstractFileEngineIterator.next()'''
        return QString()


class QModelIndex():
    """"""
    def __init__(self):
        '''void QModelIndex.__init__()'''
    def __init__(self, other):
        '''void QModelIndex.__init__(QModelIndex other)'''
    def __init__(self):
        '''QPersistentModelIndex QModelIndex.__init__()'''
        return QPersistentModelIndex()
    def __ge__(self, other):
        '''bool QModelIndex.__ge__(QModelIndex other)'''
        return bool()
    def __hash__(self):
        '''int QModelIndex.__hash__()'''
        return int()
    def __ne__(self, other):
        '''bool QModelIndex.__ne__(QModelIndex other)'''
        return bool()
    def __lt__(self, other):
        '''bool QModelIndex.__lt__(QModelIndex other)'''
        return bool()
    def __eq__(self, other):
        '''bool QModelIndex.__eq__(QModelIndex other)'''
        return bool()
    def sibling(self, arow, acolumn):
        '''QModelIndex QModelIndex.sibling(int arow, int acolumn)'''
        return QModelIndex()
    def parent(self):
        '''QModelIndex QModelIndex.parent()'''
        return QModelIndex()
    def isValid(self):
        '''bool QModelIndex.isValid()'''
        return bool()
    def model(self):
        '''QAbstractItemModel QModelIndex.model()'''
        return QAbstractItemModel()
    def internalId(self):
        '''int QModelIndex.internalId()'''
        return int()
    def internalPointer(self):
        '''object QModelIndex.internalPointer()'''
        return object()
    def flags(self):
        '''Qt.ItemFlags QModelIndex.flags()'''
        return Qt.ItemFlags()
    def data(self, role = Qt.DisplayRole):
        '''QVariant QModelIndex.data(int role = Qt.DisplayRole)'''
        return QVariant()
    def column(self):
        '''int QModelIndex.column()'''
        return int()
    def row(self):
        '''int QModelIndex.row()'''
        return int()
    def child(self, arow, acolumn):
        '''QModelIndex QModelIndex.child(int arow, int acolumn)'''
        return QModelIndex()


class QPersistentModelIndex():
    """"""
    def __init__(self):
        '''void QPersistentModelIndex.__init__()'''
    def __init__(self, index):
        '''void QPersistentModelIndex.__init__(QModelIndex index)'''
    def __init__(self, other):
        '''void QPersistentModelIndex.__init__(QPersistentModelIndex other)'''
    def __ge__(self, other):
        '''bool QPersistentModelIndex.__ge__(QPersistentModelIndex other)'''
        return bool()
    def __hash__(self):
        '''int QPersistentModelIndex.__hash__()'''
        return int()
    def __ne__(self, other):
        '''bool QPersistentModelIndex.__ne__(QPersistentModelIndex other)'''
        return bool()
    def __ne__(self, other):
        '''bool QPersistentModelIndex.__ne__(QModelIndex other)'''
        return bool()
    def __eq__(self, other):
        '''bool QPersistentModelIndex.__eq__(QPersistentModelIndex other)'''
        return bool()
    def __eq__(self, other):
        '''bool QPersistentModelIndex.__eq__(QModelIndex other)'''
        return bool()
    def __lt__(self, other):
        '''bool QPersistentModelIndex.__lt__(QPersistentModelIndex other)'''
        return bool()
    def isValid(self):
        '''bool QPersistentModelIndex.isValid()'''
        return bool()
    def model(self):
        '''QAbstractItemModel QPersistentModelIndex.model()'''
        return QAbstractItemModel()
    def child(self, row, column):
        '''QModelIndex QPersistentModelIndex.child(int row, int column)'''
        return QModelIndex()
    def sibling(self, row, column):
        '''QModelIndex QPersistentModelIndex.sibling(int row, int column)'''
        return QModelIndex()
    def parent(self):
        '''QModelIndex QPersistentModelIndex.parent()'''
        return QModelIndex()
    def flags(self):
        '''Qt.ItemFlags QPersistentModelIndex.flags()'''
        return Qt.ItemFlags()
    def data(self, role = Qt.DisplayRole):
        '''QVariant QPersistentModelIndex.data(int role = Qt.DisplayRole)'''
        return QVariant()
    def column(self):
        '''int QPersistentModelIndex.column()'''
        return int()
    def row(self):
        '''int QPersistentModelIndex.row()'''
        return int()


class QAbstractItemModel(QObject):
    """"""
    def __init__(self, parent = None):
        '''void QAbstractItemModel.__init__(QObject parent = None)'''
    def setRoleNames(self, roleNames):
        '''void QAbstractItemModel.setRoleNames(dict-of-int-QByteArray roleNames)'''
    def endResetModel(self):
        '''void QAbstractItemModel.endResetModel()'''
    def beginResetModel(self):
        '''void QAbstractItemModel.beginResetModel()'''
    def endMoveColumns(self):
        '''void QAbstractItemModel.endMoveColumns()'''
    def beginMoveColumns(self, sourceParent, sourceFirst, sourceLast, destinationParent, destinationColumn):
        '''bool QAbstractItemModel.beginMoveColumns(QModelIndex sourceParent, int sourceFirst, int sourceLast, QModelIndex destinationParent, int destinationColumn)'''
        return bool()
    def endMoveRows(self):
        '''void QAbstractItemModel.endMoveRows()'''
    def beginMoveRows(self, sourceParent, sourceFirst, sourceLast, destinationParent, destinationRow):
        '''bool QAbstractItemModel.beginMoveRows(QModelIndex sourceParent, int sourceFirst, int sourceLast, QModelIndex destinationParent, int destinationRow)'''
        return bool()
    columnsMoved = pyqtSignal() # void columnsMoved(const QModelIndex&,int,int,const QModelIndex&,int) - signal
    columnsAboutToBeMoved = pyqtSignal() # void columnsAboutToBeMoved(const QModelIndex&,int,int,const QModelIndex&,int) - signal
    rowsMoved = pyqtSignal() # void rowsMoved(const QModelIndex&,int,int,const QModelIndex&,int) - signal
    rowsAboutToBeMoved = pyqtSignal() # void rowsAboutToBeMoved(const QModelIndex&,int,int,const QModelIndex&,int) - signal
    def createIndex(self, row, column, object = 0):
        '''QModelIndex QAbstractItemModel.createIndex(int row, int column, object object = 0)'''
        return QModelIndex()
    def roleNames(self):
        '''dict-of-int-QByteArray QAbstractItemModel.roleNames()'''
        return dict-of-int-QByteArray()
    def supportedDragActions(self):
        '''Qt.DropActions QAbstractItemModel.supportedDragActions()'''
        return Qt.DropActions()
    def setSupportedDragActions(self):
        '''Qt.DropActions QAbstractItemModel.setSupportedDragActions()'''
        return Qt.DropActions()
    def removeColumn(self, column, parent = QModelIndex()):
        '''bool QAbstractItemModel.removeColumn(int column, QModelIndex parent = QModelIndex())'''
        return bool()
    def removeRow(self, row, parent = QModelIndex()):
        '''bool QAbstractItemModel.removeRow(int row, QModelIndex parent = QModelIndex())'''
        return bool()
    def insertColumn(self, column, parent = QModelIndex()):
        '''bool QAbstractItemModel.insertColumn(int column, QModelIndex parent = QModelIndex())'''
        return bool()
    def insertRow(self, row, parent = QModelIndex()):
        '''bool QAbstractItemModel.insertRow(int row, QModelIndex parent = QModelIndex())'''
        return bool()
    def changePersistentIndexList(self, from_, to):
        '''void QAbstractItemModel.changePersistentIndexList(list-of-QModelIndex from, list-of-QModelIndex to)'''
    def changePersistentIndex(self, from_, to):
        '''void QAbstractItemModel.changePersistentIndex(QModelIndex from, QModelIndex to)'''
    def reset(self):
        '''void QAbstractItemModel.reset()'''
    def persistentIndexList(self):
        '''list-of-QModelIndex QAbstractItemModel.persistentIndexList()'''
        return [QModelIndex()]
    def endRemoveColumns(self):
        '''void QAbstractItemModel.endRemoveColumns()'''
    def beginRemoveColumns(self, parent, first, last):
        '''void QAbstractItemModel.beginRemoveColumns(QModelIndex parent, int first, int last)'''
    def endInsertColumns(self):
        '''void QAbstractItemModel.endInsertColumns()'''
    def beginInsertColumns(self, parent, first, last):
        '''void QAbstractItemModel.beginInsertColumns(QModelIndex parent, int first, int last)'''
    def endRemoveRows(self):
        '''void QAbstractItemModel.endRemoveRows()'''
    def beginRemoveRows(self, parent, first, last):
        '''void QAbstractItemModel.beginRemoveRows(QModelIndex parent, int first, int last)'''
    def endInsertRows(self):
        '''void QAbstractItemModel.endInsertRows()'''
    def beginInsertRows(self, parent, first, last):
        '''void QAbstractItemModel.beginInsertRows(QModelIndex parent, int first, int last)'''
    def decodeData(self, row, column, parent, stream):
        '''bool QAbstractItemModel.decodeData(int row, int column, QModelIndex parent, QDataStream stream)'''
        return bool()
    def encodeData(self, indexes, stream):
        '''void QAbstractItemModel.encodeData(list-of-QModelIndex indexes, QDataStream stream)'''
    def resetInternalData(self):
        '''void QAbstractItemModel.resetInternalData()'''
    def revert(self):
        '''void QAbstractItemModel.revert()'''
    def submit(self):
        '''bool QAbstractItemModel.submit()'''
        return bool()
    modelReset = pyqtSignal() # void modelReset() - signal
    modelAboutToBeReset = pyqtSignal() # void modelAboutToBeReset() - signal
    columnsRemoved = pyqtSignal() # void columnsRemoved(const QModelIndex&,int,int) - signal
    columnsAboutToBeRemoved = pyqtSignal() # void columnsAboutToBeRemoved(const QModelIndex&,int,int) - signal
    columnsInserted = pyqtSignal() # void columnsInserted(const QModelIndex&,int,int) - signal
    columnsAboutToBeInserted = pyqtSignal() # void columnsAboutToBeInserted(const QModelIndex&,int,int) - signal
    rowsRemoved = pyqtSignal() # void rowsRemoved(const QModelIndex&,int,int) - signal
    rowsAboutToBeRemoved = pyqtSignal() # void rowsAboutToBeRemoved(const QModelIndex&,int,int) - signal
    rowsInserted = pyqtSignal() # void rowsInserted(const QModelIndex&,int,int) - signal
    rowsAboutToBeInserted = pyqtSignal() # void rowsAboutToBeInserted(const QModelIndex&,int,int) - signal
    layoutChanged = pyqtSignal() # void layoutChanged() - signal
    layoutAboutToBeChanged = pyqtSignal() # void layoutAboutToBeChanged() - signal
    headerDataChanged = pyqtSignal() # void headerDataChanged(Qt::Orientation,int,int) - signal
    dataChanged = pyqtSignal() # void dataChanged(const QModelIndex&,const QModelIndex&) - signal
    def span(self, index):
        '''QSize QAbstractItemModel.span(QModelIndex index)'''
        return QSize()
    def match(self, start, role, value, hits = 1, flags = Qt.MatchStartsWith|Qt.MatchWrap):
        '''list-of-QModelIndex QAbstractItemModel.match(QModelIndex start, int role, QVariant value, int hits = 1, Qt.MatchFlags flags = Qt.MatchStartsWith|Qt.MatchWrap)'''
        return [QModelIndex()]
    def buddy(self, index):
        '''QModelIndex QAbstractItemModel.buddy(QModelIndex index)'''
        return QModelIndex()
    def sort(self, column, order = Qt.AscendingOrder):
        '''void QAbstractItemModel.sort(int column, Qt.SortOrder order = Qt.AscendingOrder)'''
    def flags(self, index):
        '''Qt.ItemFlags QAbstractItemModel.flags(QModelIndex index)'''
        return Qt.ItemFlags()
    def canFetchMore(self, parent):
        '''bool QAbstractItemModel.canFetchMore(QModelIndex parent)'''
        return bool()
    def fetchMore(self, parent):
        '''void QAbstractItemModel.fetchMore(QModelIndex parent)'''
    def removeColumns(self, column, count, parent = QModelIndex()):
        '''bool QAbstractItemModel.removeColumns(int column, int count, QModelIndex parent = QModelIndex())'''
        return bool()
    def removeRows(self, row, count, parent = QModelIndex()):
        '''bool QAbstractItemModel.removeRows(int row, int count, QModelIndex parent = QModelIndex())'''
        return bool()
    def insertColumns(self, column, count, parent = QModelIndex()):
        '''bool QAbstractItemModel.insertColumns(int column, int count, QModelIndex parent = QModelIndex())'''
        return bool()
    def insertRows(self, row, count, parent = QModelIndex()):
        '''bool QAbstractItemModel.insertRows(int row, int count, QModelIndex parent = QModelIndex())'''
        return bool()
    def supportedDropActions(self):
        '''Qt.DropActions QAbstractItemModel.supportedDropActions()'''
        return Qt.DropActions()
    def dropMimeData(self, data, action, row, column, parent):
        '''bool QAbstractItemModel.dropMimeData(QMimeData data, Qt.DropAction action, int row, int column, QModelIndex parent)'''
        return bool()
    def mimeData(self, indexes):
        '''QMimeData QAbstractItemModel.mimeData(list-of-QModelIndex indexes)'''
        return QMimeData()
    def mimeTypes(self):
        '''QStringList QAbstractItemModel.mimeTypes()'''
        return QStringList()
    def setItemData(self, index, roles):
        '''bool QAbstractItemModel.setItemData(QModelIndex index, dict-of-int-QVariant roles)'''
        return bool()
    def itemData(self, index):
        '''dict-of-int-QVariant QAbstractItemModel.itemData(QModelIndex index)'''
        return dict-of-int-QVariant()
    def setHeaderData(self, section, orientation, value, role = Qt.EditRole):
        '''bool QAbstractItemModel.setHeaderData(int section, Qt.Orientation orientation, QVariant value, int role = Qt.EditRole)'''
        return bool()
    def headerData(self, section, orientation, role = Qt.DisplayRole):
        '''QVariant QAbstractItemModel.headerData(int section, Qt.Orientation orientation, int role = Qt.DisplayRole)'''
        return QVariant()
    def setData(self, index, value, role = Qt.EditRole):
        '''bool QAbstractItemModel.setData(QModelIndex index, QVariant value, int role = Qt.EditRole)'''
        return bool()
    def data(self, index, role = Qt.DisplayRole):
        '''abstract QVariant QAbstractItemModel.data(QModelIndex index, int role = Qt.DisplayRole)'''
        return QVariant()
    def hasChildren(self, parent = QModelIndex()):
        '''bool QAbstractItemModel.hasChildren(QModelIndex parent = QModelIndex())'''
        return bool()
    def columnCount(self, parent = QModelIndex()):
        '''abstract int QAbstractItemModel.columnCount(QModelIndex parent = QModelIndex())'''
        return int()
    def rowCount(self, parent = QModelIndex()):
        '''abstract int QAbstractItemModel.rowCount(QModelIndex parent = QModelIndex())'''
        return int()
    def sibling(self, row, column, idx):
        '''QModelIndex QAbstractItemModel.sibling(int row, int column, QModelIndex idx)'''
        return QModelIndex()
    def parent(self, child):
        '''abstract QModelIndex QAbstractItemModel.parent(QModelIndex child)'''
        return QModelIndex()
    def parent(self):
        '''QObject QAbstractItemModel.parent()'''
        return QObject()
    def index(self, row, column, parent = QModelIndex()):
        '''abstract QModelIndex QAbstractItemModel.index(int row, int column, QModelIndex parent = QModelIndex())'''
        return QModelIndex()
    def hasIndex(self, row, column, parent = QModelIndex()):
        '''bool QAbstractItemModel.hasIndex(int row, int column, QModelIndex parent = QModelIndex())'''
        return bool()


class QAbstractTableModel(QAbstractItemModel):
    """"""
    def __init__(self, parent = None):
        '''void QAbstractTableModel.__init__(QObject parent = None)'''
    def dropMimeData(self, data, action, row, column, parent):
        '''bool QAbstractTableModel.dropMimeData(QMimeData data, Qt.DropAction action, int row, int column, QModelIndex parent)'''
        return bool()
    def index(self, row, column, parent = QModelIndex()):
        '''QModelIndex QAbstractTableModel.index(int row, int column, QModelIndex parent = QModelIndex())'''
        return QModelIndex()


class QAbstractListModel(QAbstractItemModel):
    """"""
    def __init__(self, parent = None):
        '''void QAbstractListModel.__init__(QObject parent = None)'''
    def dropMimeData(self, data, action, row, column, parent):
        '''bool QAbstractListModel.dropMimeData(QMimeData data, Qt.DropAction action, int row, int column, QModelIndex parent)'''
        return bool()
    def index(self, row, column = 0, parent = QModelIndex()):
        '''QModelIndex QAbstractListModel.index(int row, int column = 0, QModelIndex parent = QModelIndex())'''
        return QModelIndex()


class QAbstractState(QObject):
    """"""
    def __init__(self, parent = None):
        '''void QAbstractState.__init__(QState parent = None)'''
    def event(self, e):
        '''bool QAbstractState.event(QEvent e)'''
        return bool()
    def onExit(self, event):
        '''abstract void QAbstractState.onExit(QEvent event)'''
    def onEntry(self, event):
        '''abstract void QAbstractState.onEntry(QEvent event)'''
    exited = pyqtSignal() # void exited() - signal
    entered = pyqtSignal() # void entered() - signal
    def machine(self):
        '''QStateMachine QAbstractState.machine()'''
        return QStateMachine()
    def parentState(self):
        '''QState QAbstractState.parentState()'''
        return QState()


class QAbstractTransition(QObject):
    """"""
    def __init__(self, sourceState = None):
        '''void QAbstractTransition.__init__(QState sourceState = None)'''
    def event(self, e):
        '''bool QAbstractTransition.event(QEvent e)'''
        return bool()
    def onTransition(self, event):
        '''abstract void QAbstractTransition.onTransition(QEvent event)'''
    def eventTest(self, event):
        '''abstract bool QAbstractTransition.eventTest(QEvent event)'''
        return bool()
    triggered = pyqtSignal() # void triggered() - signal
    def animations(self):
        '''list-of-QAbstractAnimation QAbstractTransition.animations()'''
        return [QAbstractAnimation()]
    def removeAnimation(self, animation):
        '''void QAbstractTransition.removeAnimation(QAbstractAnimation animation)'''
    def addAnimation(self, animation):
        '''void QAbstractTransition.addAnimation(QAbstractAnimation animation)'''
    def machine(self):
        '''QStateMachine QAbstractTransition.machine()'''
        return QStateMachine()
    def setTargetStates(self, targets):
        '''void QAbstractTransition.setTargetStates(list-of-QAbstractState targets)'''
    def targetStates(self):
        '''list-of-QAbstractState QAbstractTransition.targetStates()'''
        return [QAbstractState()]
    def setTargetState(self, target):
        '''void QAbstractTransition.setTargetState(QAbstractState target)'''
    def targetState(self):
        '''QAbstractState QAbstractTransition.targetState()'''
        return QAbstractState()
    def sourceState(self):
        '''QState QAbstractTransition.sourceState()'''
        return QState()


class QAnimationGroup(QAbstractAnimation):
    """"""
    def __init__(self, parent = None):
        '''void QAnimationGroup.__init__(QObject parent = None)'''
    def event(self, event):
        '''bool QAnimationGroup.event(QEvent event)'''
        return bool()
    def clear(self):
        '''void QAnimationGroup.clear()'''
    def takeAnimation(self, index):
        '''QAbstractAnimation QAnimationGroup.takeAnimation(int index)'''
        return QAbstractAnimation()
    def removeAnimation(self, animation):
        '''void QAnimationGroup.removeAnimation(QAbstractAnimation animation)'''
    def insertAnimation(self, index, animation):
        '''void QAnimationGroup.insertAnimation(int index, QAbstractAnimation animation)'''
    def addAnimation(self, animation):
        '''void QAnimationGroup.addAnimation(QAbstractAnimation animation)'''
    def indexOfAnimation(self, animation):
        '''int QAnimationGroup.indexOfAnimation(QAbstractAnimation animation)'''
        return int()
    def animationCount(self):
        '''int QAnimationGroup.animationCount()'''
        return int()
    def animationAt(self, index):
        '''QAbstractAnimation QAnimationGroup.animationAt(int index)'''
        return QAbstractAnimation()


class QBasicTimer():
    """"""
    def __init__(self):
        '''void QBasicTimer.__init__()'''
    def __init__(self):
        '''QBasicTimer QBasicTimer.__init__()'''
        return QBasicTimer()
    def stop(self):
        '''void QBasicTimer.stop()'''
    def start(self, msec, obj):
        '''void QBasicTimer.start(int msec, QObject obj)'''
    def timerId(self):
        '''int QBasicTimer.timerId()'''
        return int()
    def isActive(self):
        '''bool QBasicTimer.isActive()'''
        return bool()


class QBitArray():
    """"""
    def __init__(self):
        '''void QBitArray.__init__()'''
    def __init__(self, size, value = False):
        '''void QBitArray.__init__(int size, bool value = False)'''
    def __init__(self, other):
        '''void QBitArray.__init__(QBitArray other)'''
    def __or__(self):
        '''QBitArray QBitArray.__or__()'''
        return QBitArray()
    def __and__(self):
        '''QBitArray QBitArray.__and__()'''
        return QBitArray()
    def __xor__(self):
        '''QBitArray QBitArray.__xor__()'''
        return QBitArray()
    def swap(self, other):
        '''void QBitArray.swap(QBitArray other)'''
    def __hash__(self):
        '''int QBitArray.__hash__()'''
        return int()
    def at(self, i):
        '''bool QBitArray.at(int i)'''
        return bool()
    def __getitem__(self, i):
        '''bool QBitArray.__getitem__(int i)'''
        return bool()
    def toggleBit(self, i):
        '''bool QBitArray.toggleBit(int i)'''
        return bool()
    def clearBit(self, i):
        '''void QBitArray.clearBit(int i)'''
    def setBit(self, i):
        '''void QBitArray.setBit(int i)'''
    def setBit(self, i, val):
        '''void QBitArray.setBit(int i, bool val)'''
    def testBit(self, i):
        '''bool QBitArray.testBit(int i)'''
        return bool()
    def truncate(self, pos):
        '''void QBitArray.truncate(int pos)'''
    def fill(self, val, first, last):
        '''void QBitArray.fill(bool val, int first, int last)'''
    def fill(self, value, size = -1):
        '''bool QBitArray.fill(bool value, int size = -1)'''
        return bool()
    def __ne__(self, a):
        '''bool QBitArray.__ne__(QBitArray a)'''
        return bool()
    def __eq__(self, a):
        '''bool QBitArray.__eq__(QBitArray a)'''
        return bool()
    def __invert__(self):
        '''QBitArray QBitArray.__invert__()'''
        return QBitArray()
    def __ixor__(self):
        '''QBitArray QBitArray.__ixor__()'''
        return QBitArray()
    def __ior__(self):
        '''QBitArray QBitArray.__ior__()'''
        return QBitArray()
    def __iand__(self):
        '''QBitArray QBitArray.__iand__()'''
        return QBitArray()
    def clear(self):
        '''void QBitArray.clear()'''
    def isDetached(self):
        '''bool QBitArray.isDetached()'''
        return bool()
    def detach(self):
        '''void QBitArray.detach()'''
    def resize(self, size):
        '''void QBitArray.resize(int size)'''
    def isNull(self):
        '''bool QBitArray.isNull()'''
        return bool()
    def isEmpty(self):
        '''bool QBitArray.isEmpty()'''
        return bool()
    def __len__(self):
        ''' QBitArray.__len__()'''
        return ()
    def count(self):
        '''int QBitArray.count()'''
        return int()
    def count(self, on):
        '''int QBitArray.count(bool on)'''
        return int()
    def size(self):
        '''int QBitArray.size()'''
        return int()


class QIODevice(QObject):
    """"""
    # Enum QIODevice.OpenModeFlag
    NotOpen = 0
    ReadOnly = 0
    WriteOnly = 0
    ReadWrite = 0
    Append = 0
    Truncate = 0
    Text = 0
    Unbuffered = 0

    def __init__(self):
        '''void QIODevice.__init__()'''
    def __init__(self, parent):
        '''void QIODevice.__init__(QObject parent)'''
    def setErrorString(self, errorString):
        '''void QIODevice.setErrorString(QString errorString)'''
    def setOpenMode(self, openMode):
        '''void QIODevice.setOpenMode(QIODevice.OpenMode openMode)'''
    def writeData(self, data):
        '''abstract int QIODevice.writeData(str data)'''
        return int()
    def readLineData(self, maxlen):
        '''str QIODevice.readLineData(int maxlen)'''
        return str()
    def readData(self, maxlen):
        '''abstract str QIODevice.readData(int maxlen)'''
        return str()
    readChannelFinished = pyqtSignal() # void readChannelFinished() - signal
    aboutToClose = pyqtSignal() # void aboutToClose() - signal
    bytesWritten = pyqtSignal() # void bytesWritten(qint64) - signal
    readyRead = pyqtSignal() # void readyRead() - signal
    def errorString(self):
        '''QString QIODevice.errorString()'''
        return QString()
    def getChar(self, c):
        '''bool QIODevice.getChar(str c)'''
        return bool()
    def putChar(self, c):
        '''bool QIODevice.putChar(str c)'''
        return bool()
    def ungetChar(self, c):
        '''void QIODevice.ungetChar(str c)'''
    def waitForBytesWritten(self, msecs):
        '''bool QIODevice.waitForBytesWritten(int msecs)'''
        return bool()
    def waitForReadyRead(self, msecs):
        '''bool QIODevice.waitForReadyRead(int msecs)'''
        return bool()
    def write(self, data):
        '''int QIODevice.write(QByteArray data)'''
        return int()
    def peek(self, maxlen):
        '''QByteArray QIODevice.peek(int maxlen)'''
        return QByteArray()
    def canReadLine(self):
        '''bool QIODevice.canReadLine()'''
        return bool()
    def readLine(self, maxlen = 0):
        '''str QIODevice.readLine(int maxlen = 0)'''
        return str()
    def readAll(self):
        '''QByteArray QIODevice.readAll()'''
        return QByteArray()
    def read(self, maxlen):
        '''str QIODevice.read(int maxlen)'''
        return str()
    def bytesToWrite(self):
        '''int QIODevice.bytesToWrite()'''
        return int()
    def bytesAvailable(self):
        '''int QIODevice.bytesAvailable()'''
        return int()
    def reset(self):
        '''bool QIODevice.reset()'''
        return bool()
    def atEnd(self):
        '''bool QIODevice.atEnd()'''
        return bool()
    def seek(self, pos):
        '''bool QIODevice.seek(int pos)'''
        return bool()
    def size(self):
        '''int QIODevice.size()'''
        return int()
    def pos(self):
        '''int QIODevice.pos()'''
        return int()
    def close(self):
        '''void QIODevice.close()'''
    def open(self, mode):
        '''bool QIODevice.open(QIODevice.OpenMode mode)'''
        return bool()
    def isSequential(self):
        '''bool QIODevice.isSequential()'''
        return bool()
    def isWritable(self):
        '''bool QIODevice.isWritable()'''
        return bool()
    def isReadable(self):
        '''bool QIODevice.isReadable()'''
        return bool()
    def isOpen(self):
        '''bool QIODevice.isOpen()'''
        return bool()
    def isTextModeEnabled(self):
        '''bool QIODevice.isTextModeEnabled()'''
        return bool()
    def setTextModeEnabled(self, enabled):
        '''void QIODevice.setTextModeEnabled(bool enabled)'''
    def openMode(self):
        '''QIODevice.OpenMode QIODevice.openMode()'''
        return QIODevice.OpenMode()
    class OpenMode():
        """"""
        def __init__(self):
            '''QIODevice.OpenMode QIODevice.OpenMode.__init__()'''
            return QIODevice.OpenMode()
        def __init__(self):
            '''int QIODevice.OpenMode.__init__()'''
            return int()
        def __init__(self):
            '''void QIODevice.OpenMode.__init__()'''
        def __bool__(self):
            '''int QIODevice.OpenMode.__bool__()'''
            return int()
        def __ne__(self, f):
            '''bool QIODevice.OpenMode.__ne__(QIODevice.OpenMode f)'''
            return bool()
        def __eq__(self, f):
            '''bool QIODevice.OpenMode.__eq__(QIODevice.OpenMode f)'''
            return bool()
        def __invert__(self):
            '''QIODevice.OpenMode QIODevice.OpenMode.__invert__()'''
            return QIODevice.OpenMode()
        def __and__(self, mask):
            '''QIODevice.OpenMode QIODevice.OpenMode.__and__(int mask)'''
            return QIODevice.OpenMode()
        def __xor__(self, f):
            '''QIODevice.OpenMode QIODevice.OpenMode.__xor__(QIODevice.OpenMode f)'''
            return QIODevice.OpenMode()
        def __xor__(self, f):
            '''QIODevice.OpenMode QIODevice.OpenMode.__xor__(int f)'''
            return QIODevice.OpenMode()
        def __or__(self, f):
            '''QIODevice.OpenMode QIODevice.OpenMode.__or__(QIODevice.OpenMode f)'''
            return QIODevice.OpenMode()
        def __or__(self, f):
            '''QIODevice.OpenMode QIODevice.OpenMode.__or__(int f)'''
            return QIODevice.OpenMode()
        def __int__(self):
            '''int QIODevice.OpenMode.__int__()'''
            return int()
        def __ixor__(self, f):
            '''QIODevice.OpenMode QIODevice.OpenMode.__ixor__(QIODevice.OpenMode f)'''
            return QIODevice.OpenMode()
        def __ior__(self, f):
            '''QIODevice.OpenMode QIODevice.OpenMode.__ior__(QIODevice.OpenMode f)'''
            return QIODevice.OpenMode()
        def __iand__(self, mask):
            '''QIODevice.OpenMode QIODevice.OpenMode.__iand__(int mask)'''
            return QIODevice.OpenMode()


class QBuffer(QIODevice):
    """"""
    def __init__(self, parent = None):
        '''void QBuffer.__init__(QObject parent = None)'''
    def __init__(self, byteArray, parent = None):
        '''void QBuffer.__init__(QByteArray byteArray, QObject parent = None)'''
    def disconnectNotify(self):
        '''SIGNAL() QBuffer.disconnectNotify()'''
        return SIGNAL()()
    def connectNotify(self):
        '''SIGNAL() QBuffer.connectNotify()'''
        return SIGNAL()()
    def writeData(self, data):
        '''int QBuffer.writeData(str data)'''
        return int()
    def readData(self, maxlen):
        '''str QBuffer.readData(int maxlen)'''
        return str()
    def canReadLine(self):
        '''bool QBuffer.canReadLine()'''
        return bool()
    def atEnd(self):
        '''bool QBuffer.atEnd()'''
        return bool()
    def seek(self, off):
        '''bool QBuffer.seek(int off)'''
        return bool()
    def pos(self):
        '''int QBuffer.pos()'''
        return int()
    def size(self):
        '''int QBuffer.size()'''
        return int()
    def close(self):
        '''void QBuffer.close()'''
    def open(self, openMode):
        '''bool QBuffer.open(QIODevice.OpenMode openMode)'''
        return bool()
    def setData(self, data):
        '''void QBuffer.setData(QByteArray data)'''
    def setData(self, adata):
        '''void QBuffer.setData(str adata)'''
    def setBuffer(self, a):
        '''void QBuffer.setBuffer(QByteArray a)'''
    def data(self):
        '''QByteArray QBuffer.data()'''
        return QByteArray()
    def buffer(self):
        '''QByteArray QBuffer.buffer()'''
        return QByteArray()


class QByteArray():
    """"""
    def __init__(self):
        '''void QByteArray.__init__()'''
    def __init__(self, size, c):
        '''void QByteArray.__init__(int size, str c)'''
    def __init__(self, a):
        '''void QByteArray.__init__(QByteArray a)'''
    def __add__(self, a2):
        '''QByteArray QByteArray.__add__(QByteArray a2)'''
        return QByteArray()
    def __add__(self, s):
        '''QString QByteArray.__add__(QString s)'''
        return QString()
    def swap(self, other):
        '''void QByteArray.swap(QByteArray other)'''
    def repeated(self, times):
        '''QByteArray QByteArray.repeated(int times)'''
        return QByteArray()
    def fromPercentEncoding(self, input, percent = '%'):
        '''static QByteArray QByteArray.fromPercentEncoding(QByteArray input, str percent = '%')'''
        return QByteArray()
    def toPercentEncoding(self, exclude = QByteArray(), include = QByteArray(), percent = '%'):
        '''QByteArray QByteArray.toPercentEncoding(QByteArray exclude = QByteArray(), QByteArray include = QByteArray(), str percent = '%')'''
        return QByteArray()
    def toHex(self):
        '''QByteArray QByteArray.toHex()'''
        return QByteArray()
    def contains(self, a):
        '''bool QByteArray.contains(QByteArray a)'''
        return bool()
    def push_front(self, a):
        '''void QByteArray.push_front(QByteArray a)'''
    def push_back(self, a):
        '''void QByteArray.push_back(QByteArray a)'''
    def squeeze(self):
        '''void QByteArray.squeeze()'''
    def reserve(self, size):
        '''void QByteArray.reserve(int size)'''
    def capacity(self):
        '''int QByteArray.capacity()'''
        return int()
    def data(self):
        '''str QByteArray.data()'''
        return str()
    def isEmpty(self):
        '''bool QByteArray.isEmpty()'''
        return bool()
    def __imul__(self, m):
        '''QByteArray QByteArray.__imul__(int m)'''
        return QByteArray()
    def __mul__(self, m):
        '''QByteArray QByteArray.__mul__(int m)'''
        return QByteArray()
    def __repr__(self):
        '''str QByteArray.__repr__()'''
        return str()
    def __str__(self):
        '''str QByteArray.__str__()'''
        return str()
    def __hash__(self):
        '''int QByteArray.__hash__()'''
        return int()
    def __contains__(self, a):
        '''int QByteArray.__contains__(QByteArray a)'''
        return int()
    def __getitem__(self, i):
        '''str QByteArray.__getitem__(int i)'''
        return str()
    def __getitem__(self, slice):
        '''QByteArray QByteArray.__getitem__(slice slice)'''
        return QByteArray()
    def at(self, i):
        '''str QByteArray.at(int i)'''
        return str()
    def size(self):
        '''int QByteArray.size()'''
        return int()
    def isNull(self):
        '''bool QByteArray.isNull()'''
        return bool()
    def length(self):
        '''int QByteArray.length()'''
        return int()
    def __len__(self):
        ''' QByteArray.__len__()'''
        return ()
    def fromHex(self, hexEncoded):
        '''static QByteArray QByteArray.fromHex(QByteArray hexEncoded)'''
        return QByteArray()
    def fromRawData(self):
        '''static str QByteArray.fromRawData()'''
        return str()
    def fromBase64(self, base64):
        '''static QByteArray QByteArray.fromBase64(QByteArray base64)'''
        return QByteArray()
    def number(self, n, base = 10):
        '''static QByteArray QByteArray.number(int n, int base = 10)'''
        return QByteArray()
    def number(self, n, format = 'g', precision = 6):
        '''static QByteArray QByteArray.number(float n, str format = 'g', int precision = 6)'''
        return QByteArray()
    def number(self, n, base = 10):
        '''static QByteArray QByteArray.number(int n, int base = 10)'''
        return QByteArray()
    def number(self, n, base = 10):
        '''static QByteArray QByteArray.number(int n, int base = 10)'''
        return QByteArray()
    def setNum(self, n, base = 10):
        '''QByteArray QByteArray.setNum(int n, int base = 10)'''
        return QByteArray()
    def setNum(self, n, format = 'g', precision = 6):
        '''QByteArray QByteArray.setNum(float n, str format = 'g', int precision = 6)'''
        return QByteArray()
    def setNum(self, n, base = 10):
        '''QByteArray QByteArray.setNum(int n, int base = 10)'''
        return QByteArray()
    def setNum(self, n, base = 10):
        '''QByteArray QByteArray.setNum(int n, int base = 10)'''
        return QByteArray()
    def toBase64(self):
        '''QByteArray QByteArray.toBase64()'''
        return QByteArray()
    def toDouble(self, ok):
        '''float QByteArray.toDouble(bool ok)'''
        return float()
    def toFloat(self, ok):
        '''float QByteArray.toFloat(bool ok)'''
        return float()
    def toULongLong(self, ok, base = 10):
        '''int QByteArray.toULongLong(bool ok, int base = 10)'''
        return int()
    def toLongLong(self, ok, base = 10):
        '''int QByteArray.toLongLong(bool ok, int base = 10)'''
        return int()
    def toULong(self, ok, base = 10):
        '''int QByteArray.toULong(bool ok, int base = 10)'''
        return int()
    def toLong(self, ok, base = 10):
        '''int QByteArray.toLong(bool ok, int base = 10)'''
        return int()
    def toUInt(self, ok, base = 10):
        '''int QByteArray.toUInt(bool ok, int base = 10)'''
        return int()
    def toInt(self, ok, base = 10):
        '''int QByteArray.toInt(bool ok, int base = 10)'''
        return int()
    def toUShort(self, ok, base = 10):
        '''int QByteArray.toUShort(bool ok, int base = 10)'''
        return int()
    def toShort(self, ok, base = 10):
        '''int QByteArray.toShort(bool ok, int base = 10)'''
        return int()
    def __ge__(self, s2):
        '''bool QByteArray.__ge__(QString s2)'''
        return bool()
    def __ge__(self, a2):
        '''bool QByteArray.__ge__(QByteArray a2)'''
        return bool()
    def __le__(self, s2):
        '''bool QByteArray.__le__(QString s2)'''
        return bool()
    def __le__(self, a2):
        '''bool QByteArray.__le__(QByteArray a2)'''
        return bool()
    def __gt__(self, s2):
        '''bool QByteArray.__gt__(QString s2)'''
        return bool()
    def __gt__(self, a2):
        '''bool QByteArray.__gt__(QByteArray a2)'''
        return bool()
    def __lt__(self, s2):
        '''bool QByteArray.__lt__(QString s2)'''
        return bool()
    def __lt__(self, a2):
        '''bool QByteArray.__lt__(QByteArray a2)'''
        return bool()
    def __ne__(self, s2):
        '''bool QByteArray.__ne__(QString s2)'''
        return bool()
    def __ne__(self, a2):
        '''bool QByteArray.__ne__(QByteArray a2)'''
        return bool()
    def __eq__(self, s2):
        '''bool QByteArray.__eq__(QString s2)'''
        return bool()
    def __eq__(self, a2):
        '''bool QByteArray.__eq__(QByteArray a2)'''
        return bool()
    def __iadd__(self, a):
        '''QByteArray QByteArray.__iadd__(QByteArray a)'''
        return QByteArray()
    def __iadd__(self, s):
        '''QByteArray QByteArray.__iadd__(QString s)'''
        return QByteArray()
    def split(self, sep):
        '''list-of-QByteArray QByteArray.split(str sep)'''
        return [QByteArray()]
    def replace(self, index, len, s):
        '''QByteArray QByteArray.replace(int index, int len, QByteArray s)'''
        return QByteArray()
    def replace(self, before, after):
        '''QByteArray QByteArray.replace(QByteArray before, QByteArray after)'''
        return QByteArray()
    def replace(self, before, after):
        '''QByteArray QByteArray.replace(QString before, QByteArray after)'''
        return QByteArray()
    def remove(self, index, len):
        '''QByteArray QByteArray.remove(int index, int len)'''
        return QByteArray()
    def insert(self, i, a):
        '''QByteArray QByteArray.insert(int i, QByteArray a)'''
        return QByteArray()
    def insert(self, i, s):
        '''QByteArray QByteArray.insert(int i, QString s)'''
        return QByteArray()
    def append(self, a):
        '''QByteArray QByteArray.append(QByteArray a)'''
        return QByteArray()
    def append(self, s):
        '''QByteArray QByteArray.append(QString s)'''
        return QByteArray()
    def prepend(self, a):
        '''QByteArray QByteArray.prepend(QByteArray a)'''
        return QByteArray()
    def rightJustified(self, width, fill = ' ', truncate = False):
        '''QByteArray QByteArray.rightJustified(int width, str fill = ' ', bool truncate = False)'''
        return QByteArray()
    def leftJustified(self, width, fill = ' ', truncate = False):
        '''QByteArray QByteArray.leftJustified(int width, str fill = ' ', bool truncate = False)'''
        return QByteArray()
    def simplified(self):
        '''QByteArray QByteArray.simplified()'''
        return QByteArray()
    def trimmed(self):
        '''QByteArray QByteArray.trimmed()'''
        return QByteArray()
    def toUpper(self):
        '''QByteArray QByteArray.toUpper()'''
        return QByteArray()
    def toLower(self):
        '''QByteArray QByteArray.toLower()'''
        return QByteArray()
    def chop(self, n):
        '''void QByteArray.chop(int n)'''
    def truncate(self, pos):
        '''void QByteArray.truncate(int pos)'''
    def endsWith(self, a):
        '''bool QByteArray.endsWith(QByteArray a)'''
        return bool()
    def startsWith(self, a):
        '''bool QByteArray.startsWith(QByteArray a)'''
        return bool()
    def mid(self, pos, length = -1):
        '''QByteArray QByteArray.mid(int pos, int length = -1)'''
        return QByteArray()
    def right(self, len):
        '''QByteArray QByteArray.right(int len)'''
        return QByteArray()
    def left(self, len):
        '''QByteArray QByteArray.left(int len)'''
        return QByteArray()
    def count(self, a):
        '''int QByteArray.count(QByteArray a)'''
        return int()
    def count(self):
        '''int QByteArray.count()'''
        return int()
    def lastIndexOf(self, ba, from_ = -1):
        '''int QByteArray.lastIndexOf(QByteArray ba, int from = -1)'''
        return int()
    def lastIndexOf(self, str, from_ = -1):
        '''int QByteArray.lastIndexOf(QString str, int from = -1)'''
        return int()
    def indexOf(self, ba, from_ = 0):
        '''int QByteArray.indexOf(QByteArray ba, int from = 0)'''
        return int()
    def indexOf(self, str, from_ = 0):
        '''int QByteArray.indexOf(QString str, int from = 0)'''
        return int()
    def clear(self):
        '''void QByteArray.clear()'''
    def fill(self, ch, size = -1):
        '''QByteArray QByteArray.fill(str ch, int size = -1)'''
        return QByteArray()
    def resize(self, size):
        '''void QByteArray.resize(int size)'''


class QByteArrayMatcher():
    """"""
    def __init__(self):
        '''void QByteArrayMatcher.__init__()'''
    def __init__(self, pattern):
        '''void QByteArrayMatcher.__init__(QByteArray pattern)'''
    def __init__(self, other):
        '''void QByteArrayMatcher.__init__(QByteArrayMatcher other)'''
    def pattern(self):
        '''QByteArray QByteArrayMatcher.pattern()'''
        return QByteArray()
    def indexIn(self, ba, from_ = 0):
        '''int QByteArrayMatcher.indexIn(QByteArray ba, int from = 0)'''
        return int()
    def setPattern(self, pattern):
        '''void QByteArrayMatcher.setPattern(QByteArray pattern)'''


class QLatin1Char():
    """"""
    def __init__(self, c):
        '''void QLatin1Char.__init__(str c)'''
    def __init__(self):
        '''QLatin1Char QLatin1Char.__init__()'''
        return QLatin1Char()
    def unicode(self):
        '''int QLatin1Char.unicode()'''
        return int()
    def toLatin1(self):
        '''str QLatin1Char.toLatin1()'''
        return str()
    def __repr__(self):
        '''str QLatin1Char.__repr__()'''
        return str()


class QChar():
    """"""
    # Enum QChar.UnicodeVersion
    Unicode_Unassigned = 0
    Unicode_1_1 = 0
    Unicode_2_0 = 0
    Unicode_2_1_2 = 0
    Unicode_3_0 = 0
    Unicode_3_1 = 0
    Unicode_3_2 = 0
    Unicode_4_0 = 0
    Unicode_4_1 = 0
    Unicode_5_0 = 0

    # Enum QChar.CombiningClass
    Combining_BelowLeftAttached = 0
    Combining_BelowAttached = 0
    Combining_BelowRightAttached = 0
    Combining_LeftAttached = 0
    Combining_RightAttached = 0
    Combining_AboveLeftAttached = 0
    Combining_AboveAttached = 0
    Combining_AboveRightAttached = 0
    Combining_BelowLeft = 0
    Combining_Below = 0
    Combining_BelowRight = 0
    Combining_Left = 0
    Combining_Right = 0
    Combining_AboveLeft = 0
    Combining_Above = 0
    Combining_AboveRight = 0
    Combining_DoubleBelow = 0
    Combining_DoubleAbove = 0
    Combining_IotaSubscript = 0

    # Enum QChar.Joining
    OtherJoining = 0
    Dual = 0
    Right = 0
    Center = 0

    # Enum QChar.Decomposition
    NoDecomposition = 0
    Canonical = 0
    Font = 0
    NoBreak = 0
    Initial = 0
    Medial = 0
    Final = 0
    Isolated = 0
    Circle = 0
    Super = 0
    Sub = 0
    Vertical = 0
    Wide = 0
    Narrow = 0
    Small = 0
    Square = 0
    Compat = 0
    Fraction = 0

    # Enum QChar.Direction
    DirL = 0
    DirR = 0
    DirEN = 0
    DirES = 0
    DirET = 0
    DirAN = 0
    DirCS = 0
    DirB = 0
    DirS = 0
    DirWS = 0
    DirON = 0
    DirLRE = 0
    DirLRO = 0
    DirAL = 0
    DirRLE = 0
    DirRLO = 0
    DirPDF = 0
    DirNSM = 0
    DirBN = 0

    # Enum QChar.Category
    NoCategory = 0
    Mark_NonSpacing = 0
    Mark_SpacingCombining = 0
    Mark_Enclosing = 0
    Number_DecimalDigit = 0
    Number_Letter = 0
    Number_Other = 0
    Separator_Space = 0
    Separator_Line = 0
    Separator_Paragraph = 0
    Other_Control = 0
    Other_Format = 0
    Other_Surrogate = 0
    Other_PrivateUse = 0
    Other_NotAssigned = 0
    Letter_Uppercase = 0
    Letter_Lowercase = 0
    Letter_Titlecase = 0
    Letter_Modifier = 0
    Letter_Other = 0
    Punctuation_Connector = 0
    Punctuation_Dash = 0
    Punctuation_Open = 0
    Punctuation_Close = 0
    Punctuation_InitialQuote = 0
    Punctuation_FinalQuote = 0
    Punctuation_Other = 0
    Symbol_Math = 0
    Symbol_Currency = 0
    Symbol_Modifier = 0
    Symbol_Other = 0
    Punctuation_Dask = 0

    # Enum QChar.SpecialCharacter
    Null = 0
    Nbsp = 0
    ReplacementCharacter = 0
    ObjectReplacementCharacter = 0
    ByteOrderMark = 0
    ByteOrderSwapped = 0
    ParagraphSeparator = 0
    LineSeparator = 0

    def __init__(self):
        '''void QChar.__init__()'''
    def __init__(self, c):
        '''void QChar.__init__(str c)'''
    def __init__(self, ch):
        '''void QChar.__init__(QLatin1Char ch)'''
    def __init__(self, c, r):
        '''void QChar.__init__(str c, str r)'''
    def __init__(self, rc):
        '''void QChar.__init__(int rc)'''
    def __init__(self, s):
        '''void QChar.__init__(QChar.SpecialCharacter s)'''
    def __init__(self):
        '''QChar QChar.__init__()'''
        return QChar()
    def __eq__(self, c2):
        '''bool QChar.__eq__(QChar c2)'''
        return bool()
    def __ne__(self, c2):
        '''bool QChar.__ne__(QChar c2)'''
        return bool()
    def __lt__(self, c2):
        '''bool QChar.__lt__(QChar c2)'''
        return bool()
    def __le__(self, c2):
        '''bool QChar.__le__(QChar c2)'''
        return bool()
    def __gt__(self, c2):
        '''bool QChar.__gt__(QChar c2)'''
        return bool()
    def __ge__(self, c2):
        '''bool QChar.__ge__(QChar c2)'''
        return bool()
    def __add__(self, s2):
        '''QString QChar.__add__(QString s2)'''
        return QString()
    def currentUnicodeVersion(self):
        '''static QChar.UnicodeVersion QChar.currentUnicodeVersion()'''
        return QChar.UnicodeVersion()
    def requiresSurrogates(self, ucs4):
        '''static bool QChar.requiresSurrogates(int ucs4)'''
        return bool()
    def lowSurrogate(self, ucs4):
        '''static int QChar.lowSurrogate(int ucs4)'''
        return int()
    def highSurrogate(self, ucs4):
        '''static int QChar.highSurrogate(int ucs4)'''
        return int()
    def surrogateToUcs4(self, high, low):
        '''static int QChar.surrogateToUcs4(int high, int low)'''
        return int()
    def surrogateToUcs4(self, high, low):
        '''static int QChar.surrogateToUcs4(QChar high, QChar low)'''
        return int()
    def isLowSurrogate(self):
        '''bool QChar.isLowSurrogate()'''
        return bool()
    def isLowSurrogate(self, ucs4):
        '''static bool QChar.isLowSurrogate(int ucs4)'''
        return bool()
    def isHighSurrogate(self):
        '''bool QChar.isHighSurrogate()'''
        return bool()
    def isHighSurrogate(self, ucs4):
        '''static bool QChar.isHighSurrogate(int ucs4)'''
        return bool()
    def isTitleCase(self):
        '''bool QChar.isTitleCase()'''
        return bool()
    def toCaseFolded(self):
        '''QChar QChar.toCaseFolded()'''
        return QChar()
    def toCaseFolded(self, ucs4):
        '''static int QChar.toCaseFolded(int ucs4)'''
        return int()
    def toTitleCase(self):
        '''QChar QChar.toTitleCase()'''
        return QChar()
    def toTitleCase(self, ucs4):
        '''static int QChar.toTitleCase(int ucs4)'''
        return int()
    def setRow(self, arow):
        '''void QChar.setRow(str arow)'''
    def setCell(self, acell):
        '''void QChar.setCell(str acell)'''
    def fromLatin1(self, c):
        '''static QChar QChar.fromLatin1(str c)'''
        return QChar()
    def toLatin1(self):
        '''str QChar.toLatin1()'''
        return str()
    def row(self):
        '''str QChar.row()'''
        return str()
    def cell(self):
        '''str QChar.cell()'''
        return str()
    def isSymbol(self):
        '''bool QChar.isSymbol()'''
        return bool()
    def isDigit(self):
        '''bool QChar.isDigit()'''
        return bool()
    def isLetterOrNumber(self):
        '''bool QChar.isLetterOrNumber()'''
        return bool()
    def isNumber(self):
        '''bool QChar.isNumber()'''
        return bool()
    def isLetter(self):
        '''bool QChar.isLetter()'''
        return bool()
    def isMark(self):
        '''bool QChar.isMark()'''
        return bool()
    def isSpace(self):
        '''bool QChar.isSpace()'''
        return bool()
    def isPunct(self):
        '''bool QChar.isPunct()'''
        return bool()
    def isPrint(self):
        '''bool QChar.isPrint()'''
        return bool()
    def isNull(self):
        '''bool QChar.isNull()'''
        return bool()
    def fromAscii(self, c):
        '''static QChar QChar.fromAscii(str c)'''
        return QChar()
    def unicode(self):
        '''int QChar.unicode()'''
        return int()
    def toAscii(self):
        '''str QChar.toAscii()'''
        return str()
    def unicodeVersion(self):
        '''QChar.UnicodeVersion QChar.unicodeVersion()'''
        return QChar.UnicodeVersion()
    def unicodeVersion(self, ucs4):
        '''static QChar.UnicodeVersion QChar.unicodeVersion(int ucs4)'''
        return QChar.UnicodeVersion()
    def combiningClass(self):
        '''str QChar.combiningClass()'''
        return str()
    def combiningClass(self, ucs4):
        '''static str QChar.combiningClass(int ucs4)'''
        return str()
    def decompositionTag(self):
        '''QChar.Decomposition QChar.decompositionTag()'''
        return QChar.Decomposition()
    def decompositionTag(self, ucs4):
        '''static QChar.Decomposition QChar.decompositionTag(int ucs4)'''
        return QChar.Decomposition()
    def decomposition(self):
        '''QString QChar.decomposition()'''
        return QString()
    def decomposition(self, ucs4):
        '''static QString QChar.decomposition(int ucs4)'''
        return QString()
    def mirroredChar(self):
        '''QChar QChar.mirroredChar()'''
        return QChar()
    def mirroredChar(self, ucs4):
        '''static int QChar.mirroredChar(int ucs4)'''
        return int()
    def isUpper(self):
        '''bool QChar.isUpper()'''
        return bool()
    def isLower(self):
        '''bool QChar.isLower()'''
        return bool()
    def hasMirrored(self):
        '''bool QChar.hasMirrored()'''
        return bool()
    def joining(self):
        '''QChar.Joining QChar.joining()'''
        return QChar.Joining()
    def joining(self, ucs4):
        '''static QChar.Joining QChar.joining(int ucs4)'''
        return QChar.Joining()
    def direction(self):
        '''QChar.Direction QChar.direction()'''
        return QChar.Direction()
    def direction(self, ucs4):
        '''static QChar.Direction QChar.direction(int ucs4)'''
        return QChar.Direction()
    def category(self):
        '''QChar.Category QChar.category()'''
        return QChar.Category()
    def category(self, ucs4):
        '''static QChar.Category QChar.category(int ucs4)'''
        return QChar.Category()
    def toUpper(self):
        '''QChar QChar.toUpper()'''
        return QChar()
    def toUpper(self, ucs4):
        '''static int QChar.toUpper(int ucs4)'''
        return int()
    def toLower(self):
        '''QChar QChar.toLower()'''
        return QChar()
    def toLower(self, ucs4):
        '''static int QChar.toLower(int ucs4)'''
        return int()
    def digitValue(self):
        '''int QChar.digitValue()'''
        return int()
    def digitValue(self, ucs4):
        '''static int QChar.digitValue(int ucs4)'''
        return int()
    def __hash__(self):
        '''int QChar.__hash__()'''
        return int()
    def __repr__(self):
        '''str QChar.__repr__()'''
        return str()


class QCoreApplication(QObject):
    """"""
    # Enum QCoreApplication.Encoding
    CodecForTr = 0
    UnicodeUTF8 = 0
    DefaultCodec = 0

    def __init__(self, argv):
        '''void QCoreApplication.__init__(list-of-str argv)'''
    def applicationPid(self):
        '''static int QCoreApplication.applicationPid()'''
        return int()
    def applicationVersion(self):
        '''static QString QCoreApplication.applicationVersion()'''
        return QString()
    def setApplicationVersion(self, version):
        '''static void QCoreApplication.setApplicationVersion(QString version)'''
    def event(self):
        '''QEvent QCoreApplication.event()'''
        return QEvent()
    aboutToQuit = pyqtSignal() # void aboutToQuit() - signal
    def quit(self):
        '''static void QCoreApplication.quit()'''
    def testAttribute(self, attribute):
        '''static bool QCoreApplication.testAttribute(Qt.ApplicationAttribute attribute)'''
        return bool()
    def setAttribute(self, attribute, on = True):
        '''static void QCoreApplication.setAttribute(Qt.ApplicationAttribute attribute, bool on = True)'''
    def flush(self):
        '''static void QCoreApplication.flush()'''
    def translate(self, context, sourceText, disambiguation = None, encoding = QCoreApplication.CodecForTr):
        '''static QString QCoreApplication.translate(str context, str sourceText, str disambiguation = None, QCoreApplication.Encoding encoding = QCoreApplication.CodecForTr)'''
        return QString()
    def translate(self, context, sourceText, disambiguation, encoding, n):
        '''static QString QCoreApplication.translate(str context, str sourceText, str disambiguation, QCoreApplication.Encoding encoding, int n)'''
        return QString()
    def removeTranslator(self):
        '''static QTranslator QCoreApplication.removeTranslator()'''
        return QTranslator()
    def installTranslator(self):
        '''static QTranslator QCoreApplication.installTranslator()'''
        return QTranslator()
    def removeLibraryPath(self):
        '''static QString QCoreApplication.removeLibraryPath()'''
        return QString()
    def addLibraryPath(self):
        '''static QString QCoreApplication.addLibraryPath()'''
        return QString()
    def libraryPaths(self):
        '''static QStringList QCoreApplication.libraryPaths()'''
        return QStringList()
    def setLibraryPaths(self):
        '''static QStringList QCoreApplication.setLibraryPaths()'''
        return QStringList()
    def applicationFilePath(self):
        '''static QString QCoreApplication.applicationFilePath()'''
        return QString()
    def applicationDirPath(self):
        '''static QString QCoreApplication.applicationDirPath()'''
        return QString()
    def closingDown(self):
        '''static bool QCoreApplication.closingDown()'''
        return bool()
    def startingUp(self):
        '''static bool QCoreApplication.startingUp()'''
        return bool()
    def notify(self):
        '''QEvent QCoreApplication.notify()'''
        return QEvent()
    def hasPendingEvents(self):
        '''static bool QCoreApplication.hasPendingEvents()'''
        return bool()
    def removePostedEvents(self, receiver):
        '''static void QCoreApplication.removePostedEvents(QObject receiver)'''
    def removePostedEvents(self, receiver, eventType):
        '''static void QCoreApplication.removePostedEvents(QObject receiver, int eventType)'''
    def sendPostedEvents(self, receiver, event_type):
        '''static void QCoreApplication.sendPostedEvents(QObject receiver, int event_type)'''
    def sendPostedEvents(self):
        '''static void QCoreApplication.sendPostedEvents()'''
    def postEvent(self, receiver, event):
        '''static void QCoreApplication.postEvent(QObject receiver, QEvent event)'''
    def postEvent(self, receiver, event, priority):
        '''static void QCoreApplication.postEvent(QObject receiver, QEvent event, int priority)'''
    def sendEvent(self, receiver, event):
        '''static bool QCoreApplication.sendEvent(QObject receiver, QEvent event)'''
        return bool()
    def exit(self, returnCode = 0):
        '''static void QCoreApplication.exit(int returnCode = 0)'''
    def processEvents(self, flags = QEventLoop.AllEvents):
        '''static void QCoreApplication.processEvents(QEventLoop.ProcessEventsFlags flags = QEventLoop.AllEvents)'''
    def processEvents(self, flags, maxtime):
        '''static void QCoreApplication.processEvents(QEventLoop.ProcessEventsFlags flags, int maxtime)'''
    def exec_(self):
        '''static int QCoreApplication.exec_()'''
        return int()
    def instance(self):
        '''static QCoreApplication QCoreApplication.instance()'''
        return QCoreApplication()
    def arguments(self):
        '''static QStringList QCoreApplication.arguments()'''
        return QStringList()
    def applicationName(self):
        '''static QString QCoreApplication.applicationName()'''
        return QString()
    def setApplicationName(self, application):
        '''static void QCoreApplication.setApplicationName(QString application)'''
    def organizationName(self):
        '''static QString QCoreApplication.organizationName()'''
        return QString()
    def setOrganizationName(self, orgName):
        '''static void QCoreApplication.setOrganizationName(QString orgName)'''
    def organizationDomain(self):
        '''static QString QCoreApplication.organizationDomain()'''
        return QString()
    def setOrganizationDomain(self, orgDomain):
        '''static void QCoreApplication.setOrganizationDomain(QString orgDomain)'''
    def argv(self):
        '''static list-of-str QCoreApplication.argv()'''
        return [str()]
    def argc(self):
        '''static int QCoreApplication.argc()'''
        return int()


class QEvent():
    """"""
    # Enum QEvent.Type
    __kdevpythondocumentation_builtin_None = 0
    Timer = 0
    MouseButtonPress = 0
    MouseButtonRelease = 0
    MouseButtonDblClick = 0
    MouseMove = 0
    KeyPress = 0
    KeyRelease = 0
    FocusIn = 0
    FocusOut = 0
    Enter = 0
    Leave = 0
    Paint = 0
    Move = 0
    Resize = 0
    Show = 0
    Hide = 0
    Close = 0
    ParentChange = 0
    ParentAboutToChange = 0
    WindowActivate = 0
    WindowDeactivate = 0
    ShowToParent = 0
    HideToParent = 0
    Wheel = 0
    WindowTitleChange = 0
    WindowIconChange = 0
    ApplicationWindowIconChange = 0
    ApplicationFontChange = 0
    ApplicationLayoutDirectionChange = 0
    ApplicationPaletteChange = 0
    PaletteChange = 0
    Clipboard = 0
    MetaCall = 0
    SockAct = 0
    WinEventAct = 0
    DeferredDelete = 0
    DragEnter = 0
    DragMove = 0
    DragLeave = 0
    Drop = 0
    ChildAdded = 0
    ChildPolished = 0
    ChildRemoved = 0
    PolishRequest = 0
    Polish = 0
    LayoutRequest = 0
    UpdateRequest = 0
    UpdateLater = 0
    ContextMenu = 0
    InputMethod = 0
    AccessibilityPrepare = 0
    TabletMove = 0
    LocaleChange = 0
    LanguageChange = 0
    LayoutDirectionChange = 0
    TabletPress = 0
    TabletRelease = 0
    OkRequest = 0
    IconDrag = 0
    FontChange = 0
    EnabledChange = 0
    ActivationChange = 0
    StyleChange = 0
    IconTextChange = 0
    ModifiedChange = 0
    MouseTrackingChange = 0
    WindowBlocked = 0
    WindowUnblocked = 0
    WindowStateChange = 0
    ToolTip = 0
    WhatsThis = 0
    StatusTip = 0
    ActionChanged = 0
    ActionAdded = 0
    ActionRemoved = 0
    FileOpen = 0
    Shortcut = 0
    ShortcutOverride = 0
    WhatsThisClicked = 0
    ToolBarChange = 0
    ApplicationActivate = 0
    ApplicationActivated = 0
    ApplicationDeactivate = 0
    ApplicationDeactivated = 0
    QueryWhatsThis = 0
    EnterWhatsThisMode = 0
    LeaveWhatsThisMode = 0
    ZOrderChange = 0
    HoverEnter = 0
    HoverLeave = 0
    HoverMove = 0
    AccessibilityHelp = 0
    AccessibilityDescription = 0
    MenubarUpdated = 0
    GraphicsSceneMouseMove = 0
    GraphicsSceneMousePress = 0
    GraphicsSceneMouseRelease = 0
    GraphicsSceneMouseDoubleClick = 0
    GraphicsSceneContextMenu = 0
    GraphicsSceneHoverEnter = 0
    GraphicsSceneHoverMove = 0
    GraphicsSceneHoverLeave = 0
    GraphicsSceneHelp = 0
    GraphicsSceneDragEnter = 0
    GraphicsSceneDragMove = 0
    GraphicsSceneDragLeave = 0
    GraphicsSceneDrop = 0
    GraphicsSceneWheel = 0
    GraphicsSceneResize = 0
    GraphicsSceneMove = 0
    KeyboardLayoutChange = 0
    DynamicPropertyChange = 0
    TabletEnterProximity = 0
    TabletLeaveProximity = 0
    CursorChange = 0
    ToolTipChange = 0
    GrabMouse = 0
    UngrabMouse = 0
    GrabKeyboard = 0
    UngrabKeyboard = 0
    StateMachineSignal = 0
    StateMachineWrapped = 0
    TouchBegin = 0
    TouchUpdate = 0
    TouchEnd = 0
    RequestSoftwareInputPanel = 0
    CloseSoftwareInputPanel = 0
    WinIdChange = 0
    Gesture = 0
    GestureOverride = 0
    User = 0
    MaxUser = 0

    def __init__(self, type):
        '''void QEvent.__init__(QEvent.Type type)'''
    def __init__(self):
        '''QEvent QEvent.__init__()'''
        return QEvent()
    def registerEventType(self, hint = -1):
        '''static int QEvent.registerEventType(int hint = -1)'''
        return int()
    def ignore(self):
        '''void QEvent.ignore()'''
    def accept(self):
        '''void QEvent.accept()'''
    def isAccepted(self):
        '''bool QEvent.isAccepted()'''
        return bool()
    def setAccepted(self, accepted):
        '''void QEvent.setAccepted(bool accepted)'''
    def spontaneous(self):
        '''bool QEvent.spontaneous()'''
        return bool()
    def type(self):
        '''QEvent.Type QEvent.type()'''
        return QEvent.Type()


class QTimerEvent(QEvent):
    """"""
    def __init__(self, timerId):
        '''void QTimerEvent.__init__(int timerId)'''
    def __init__(self):
        '''QTimerEvent QTimerEvent.__init__()'''
        return QTimerEvent()
    def timerId(self):
        '''int QTimerEvent.timerId()'''
        return int()


class QChildEvent(QEvent):
    """"""
    def __init__(self, type, child):
        '''void QChildEvent.__init__(QEvent.Type type, QObject child)'''
    def __init__(self):
        '''QChildEvent QChildEvent.__init__()'''
        return QChildEvent()
    def removed(self):
        '''bool QChildEvent.removed()'''
        return bool()
    def polished(self):
        '''bool QChildEvent.polished()'''
        return bool()
    def added(self):
        '''bool QChildEvent.added()'''
        return bool()
    def child(self):
        '''QObject QChildEvent.child()'''
        return QObject()


class QDynamicPropertyChangeEvent(QEvent):
    """"""
    def __init__(self, name):
        '''void QDynamicPropertyChangeEvent.__init__(QByteArray name)'''
    def __init__(self):
        '''QDynamicPropertyChangeEvent QDynamicPropertyChangeEvent.__init__()'''
        return QDynamicPropertyChangeEvent()
    def propertyName(self):
        '''QByteArray QDynamicPropertyChangeEvent.propertyName()'''
        return QByteArray()


class QCryptographicHash():
    """"""
    # Enum QCryptographicHash.Algorithm
    Md4 = 0
    Md5 = 0
    Sha1 = 0

    def __init__(self, method):
        '''void QCryptographicHash.__init__(QCryptographicHash.Algorithm method)'''
    def hash(self, data, method):
        '''static QByteArray QCryptographicHash.hash(QByteArray data, QCryptographicHash.Algorithm method)'''
        return QByteArray()
    def result(self):
        '''QByteArray QCryptographicHash.result()'''
        return QByteArray()
    def addData(self, data):
        '''void QCryptographicHash.addData(str data)'''
    def addData(self, data):
        '''void QCryptographicHash.addData(QByteArray data)'''
    def reset(self):
        '''void QCryptographicHash.reset()'''


class QDataStream():
    """"""
    # Enum QDataStream.FloatingPointPrecision
    SinglePrecision = 0
    DoublePrecision = 0

    # Enum QDataStream.Status
    Ok = 0
    ReadPastEnd = 0
    ReadCorruptData = 0
    WriteFailed = 0

    # Enum QDataStream.ByteOrder
    BigEndian = 0
    LittleEndian = 0

    # Enum QDataStream.Version
    Qt_1_0 = 0
    Qt_2_0 = 0
    Qt_2_1 = 0
    Qt_3_0 = 0
    Qt_3_1 = 0
    Qt_3_3 = 0
    Qt_4_0 = 0
    Qt_4_1 = 0
    Qt_4_2 = 0
    Qt_4_3 = 0
    Qt_4_4 = 0
    Qt_4_5 = 0
    Qt_4_6 = 0
    Qt_4_7 = 0
    Qt_4_8 = 0

    def __init__(self):
        '''void QDataStream.__init__()'''
    def __init__(self):
        '''QIODevice QDataStream.__init__()'''
        return QIODevice()
    def __init__(self, flags):
        '''QByteArray QDataStream.__init__(QIODevice.OpenMode flags)'''
        return QByteArray()
    def __init__(self):
        '''QByteArray QDataStream.__init__()'''
        return QByteArray()
    def __lshift__(self):
        '''QBitArray QDataStream.__lshift__()'''
        return QBitArray()
    def __lshift__(self):
        '''QByteArray QDataStream.__lshift__()'''
        return QByteArray()
    def __lshift__(self):
        '''QChar QDataStream.__lshift__()'''
        return QChar()
    def __lshift__(self):
        '''QDate QDataStream.__lshift__()'''
        return QDate()
    def __lshift__(self):
        '''QTime QDataStream.__lshift__()'''
        return QTime()
    def __lshift__(self):
        '''QDateTime QDataStream.__lshift__()'''
        return QDateTime()
    def __lshift__(self):
        '''QEasingCurve QDataStream.__lshift__()'''
        return QEasingCurve()
    def __lshift__(self):
        '''QLine QDataStream.__lshift__()'''
        return QLine()
    def __lshift__(self):
        '''QLineF QDataStream.__lshift__()'''
        return QLineF()
    def __lshift__(self):
        '''QLocale QDataStream.__lshift__()'''
        return QLocale()
    def __lshift__(self):
        '''QPoint QDataStream.__lshift__()'''
        return QPoint()
    def __lshift__(self):
        '''QPointF QDataStream.__lshift__()'''
        return QPointF()
    def __lshift__(self):
        '''QRect QDataStream.__lshift__()'''
        return QRect()
    def __lshift__(self):
        '''QRectF QDataStream.__lshift__()'''
        return QRectF()
    def __lshift__(self, regExp):
        '''QDataStream QDataStream.__lshift__(QRegExp regExp)'''
        return QDataStream()
    def __lshift__(self):
        '''QSize QDataStream.__lshift__()'''
        return QSize()
    def __lshift__(self):
        '''QSizeF QDataStream.__lshift__()'''
        return QSizeF()
    def __lshift__(self):
        '''QString QDataStream.__lshift__()'''
        return QString()
    def __lshift__(self, list):
        '''QDataStream QDataStream.__lshift__(QStringList list)'''
        return QDataStream()
    def __lshift__(self):
        '''QUrl QDataStream.__lshift__()'''
        return QUrl()
    def __lshift__(self):
        '''QUuid QDataStream.__lshift__()'''
        return QUuid()
    def __lshift__(self, p):
        '''QDataStream QDataStream.__lshift__(QVariant p)'''
        return QDataStream()
    def __lshift__(self, p):
        '''QDataStream QDataStream.__lshift__(Type p)'''
        return QDataStream()
    def __rshift__(self):
        '''QBitArray QDataStream.__rshift__()'''
        return QBitArray()
    def __rshift__(self):
        '''QByteArray QDataStream.__rshift__()'''
        return QByteArray()
    def __rshift__(self):
        '''QChar QDataStream.__rshift__()'''
        return QChar()
    def __rshift__(self):
        '''QDate QDataStream.__rshift__()'''
        return QDate()
    def __rshift__(self):
        '''QTime QDataStream.__rshift__()'''
        return QTime()
    def __rshift__(self):
        '''QDateTime QDataStream.__rshift__()'''
        return QDateTime()
    def __rshift__(self):
        '''QEasingCurve QDataStream.__rshift__()'''
        return QEasingCurve()
    def __rshift__(self):
        '''QLine QDataStream.__rshift__()'''
        return QLine()
    def __rshift__(self):
        '''QLineF QDataStream.__rshift__()'''
        return QLineF()
    def __rshift__(self):
        '''QLocale QDataStream.__rshift__()'''
        return QLocale()
    def __rshift__(self):
        '''QPoint QDataStream.__rshift__()'''
        return QPoint()
    def __rshift__(self):
        '''QPointF QDataStream.__rshift__()'''
        return QPointF()
    def __rshift__(self):
        '''QRect QDataStream.__rshift__()'''
        return QRect()
    def __rshift__(self):
        '''QRectF QDataStream.__rshift__()'''
        return QRectF()
    def __rshift__(self, regExp):
        '''QDataStream QDataStream.__rshift__(QRegExp regExp)'''
        return QDataStream()
    def __rshift__(self):
        '''QSize QDataStream.__rshift__()'''
        return QSize()
    def __rshift__(self):
        '''QSizeF QDataStream.__rshift__()'''
        return QSizeF()
    def __rshift__(self):
        '''QString QDataStream.__rshift__()'''
        return QString()
    def __rshift__(self, list):
        '''QDataStream QDataStream.__rshift__(QStringList list)'''
        return QDataStream()
    def __rshift__(self):
        '''QUrl QDataStream.__rshift__()'''
        return QUrl()
    def __rshift__(self):
        '''QUuid QDataStream.__rshift__()'''
        return QUuid()
    def __rshift__(self, p):
        '''QDataStream QDataStream.__rshift__(QVariant p)'''
        return QDataStream()
    def __rshift__(self, p):
        '''QDataStream QDataStream.__rshift__(Type p)'''
        return QDataStream()
    def setFloatingPointPrecision(self, precision):
        '''void QDataStream.setFloatingPointPrecision(QDataStream.FloatingPointPrecision precision)'''
    def floatingPointPrecision(self):
        '''QDataStream.FloatingPointPrecision QDataStream.floatingPointPrecision()'''
        return QDataStream.FloatingPointPrecision()
    def writeRawData(self):
        '''str QDataStream.writeRawData()'''
        return str()
    def writeBytes(self):
        '''str QDataStream.writeBytes()'''
        return str()
    def readRawData(self, len):
        '''str QDataStream.readRawData(int len)'''
        return str()
    def readBytes(self):
        '''str QDataStream.readBytes()'''
        return str()
    def writeQVariantHash(self, qvarhash):
        '''void QDataStream.writeQVariantHash(dict-of-QString-QVariant qvarhash)'''
    def readQVariantHash(self):
        '''dict-of-QString-QVariant QDataStream.readQVariantHash()'''
        return dict-of-QString-QVariant()
    def writeQVariantMap(self, qvarmap):
        '''void QDataStream.writeQVariantMap(dict-of-QString-QVariant qvarmap)'''
    def readQVariantMap(self):
        '''dict-of-QString-QVariant QDataStream.readQVariantMap()'''
        return dict-of-QString-QVariant()
    def writeQVariantList(self, qvarlst):
        '''void QDataStream.writeQVariantList(list-of-QVariant qvarlst)'''
    def readQVariantList(self):
        '''list-of-QVariant QDataStream.readQVariantList()'''
        return [QVariant()]
    def writeQVariant(self, qvar):
        '''void QDataStream.writeQVariant(QVariant qvar)'''
    def readQVariant(self):
        '''QVariant QDataStream.readQVariant()'''
        return QVariant()
    def writeQStringList(self, qstrlst):
        '''void QDataStream.writeQStringList(QStringList qstrlst)'''
    def readQStringList(self):
        '''QStringList QDataStream.readQStringList()'''
        return QStringList()
    def writeQString(self, qstr):
        '''void QDataStream.writeQString(QString qstr)'''
    def readQString(self):
        '''QString QDataStream.readQString()'''
        return QString()
    def writeString(self, str):
        '''void QDataStream.writeString(str str)'''
    def writeDouble(self, f):
        '''void QDataStream.writeDouble(float f)'''
    def writeFloat(self, f):
        '''void QDataStream.writeFloat(float f)'''
    def writeBool(self, i):
        '''void QDataStream.writeBool(bool i)'''
    def writeUInt64(self, i):
        '''void QDataStream.writeUInt64(int i)'''
    def writeInt64(self, i):
        '''void QDataStream.writeInt64(int i)'''
    def writeUInt32(self, i):
        '''void QDataStream.writeUInt32(int i)'''
    def writeInt32(self, i):
        '''void QDataStream.writeInt32(int i)'''
    def writeUInt16(self, i):
        '''void QDataStream.writeUInt16(int i)'''
    def writeInt16(self, i):
        '''void QDataStream.writeInt16(int i)'''
    def writeUInt8(self, i):
        '''void QDataStream.writeUInt8(str i)'''
    def writeInt8(self, i):
        '''void QDataStream.writeInt8(str i)'''
    def writeInt(self, i):
        '''void QDataStream.writeInt(int i)'''
    def readString(self):
        '''str QDataStream.readString()'''
        return str()
    def readDouble(self):
        '''float QDataStream.readDouble()'''
        return float()
    def readFloat(self):
        '''float QDataStream.readFloat()'''
        return float()
    def readBool(self):
        '''bool QDataStream.readBool()'''
        return bool()
    def readUInt64(self):
        '''int QDataStream.readUInt64()'''
        return int()
    def readInt64(self):
        '''int QDataStream.readInt64()'''
        return int()
    def readUInt32(self):
        '''int QDataStream.readUInt32()'''
        return int()
    def readInt32(self):
        '''int QDataStream.readInt32()'''
        return int()
    def readUInt16(self):
        '''int QDataStream.readUInt16()'''
        return int()
    def readInt16(self):
        '''int QDataStream.readInt16()'''
        return int()
    def readUInt8(self):
        '''str QDataStream.readUInt8()'''
        return str()
    def readInt8(self):
        '''str QDataStream.readInt8()'''
        return str()
    def readInt(self):
        '''int QDataStream.readInt()'''
        return int()
    def skipRawData(self, len):
        '''int QDataStream.skipRawData(int len)'''
        return int()
    def setVersion(self, v):
        '''void QDataStream.setVersion(int v)'''
    def version(self):
        '''int QDataStream.version()'''
        return int()
    def setByteOrder(self):
        '''QDataStream.ByteOrder QDataStream.setByteOrder()'''
        return QDataStream.ByteOrder()
    def byteOrder(self):
        '''QDataStream.ByteOrder QDataStream.byteOrder()'''
        return QDataStream.ByteOrder()
    def resetStatus(self):
        '''void QDataStream.resetStatus()'''
    def setStatus(self, status):
        '''void QDataStream.setStatus(QDataStream.Status status)'''
    def status(self):
        '''QDataStream.Status QDataStream.status()'''
        return QDataStream.Status()
    def atEnd(self):
        '''bool QDataStream.atEnd()'''
        return bool()
    def unsetDevice(self):
        '''void QDataStream.unsetDevice()'''
    def setDevice(self):
        '''QIODevice QDataStream.setDevice()'''
        return QIODevice()
    def device(self):
        '''QIODevice QDataStream.device()'''
        return QIODevice()


class QDate():
    """"""
    # Enum QDate.MonthNameType
    DateFormat = 0
    StandaloneFormat = 0

    def __init__(self):
        '''void QDate.__init__()'''
    def __init__(self, y, m, d):
        '''void QDate.__init__(int y, int m, int d)'''
    def __init__(self):
        '''QDate QDate.__init__()'''
        return QDate()
    def getDate(self, year, month, day):
        '''void QDate.getDate(int year, int month, int day)'''
    def setDate(self, year, month, date):
        '''bool QDate.setDate(int year, int month, int date)'''
        return bool()
    def toJulianDay(self):
        '''int QDate.toJulianDay()'''
        return int()
    def fromJulianDay(self, jd):
        '''static QDate QDate.fromJulianDay(int jd)'''
        return QDate()
    def julianToGregorian(self, jd, y, m, d):
        '''static void QDate.julianToGregorian(int jd, int y, int m, int d)'''
    def gregorianToJulian(self, y, m, d):
        '''static int QDate.gregorianToJulian(int y, int m, int d)'''
        return int()
    def isLeapYear(self, year):
        '''static bool QDate.isLeapYear(int year)'''
        return bool()
    def fromString(self, string, format = Qt.TextDate):
        '''static QDate QDate.fromString(QString string, Qt.DateFormat format = Qt.TextDate)'''
        return QDate()
    def fromString(self, s, format):
        '''static QDate QDate.fromString(QString s, QString format)'''
        return QDate()
    def currentDate(self):
        '''static QDate QDate.currentDate()'''
        return QDate()
    def __ge__(self, other):
        '''bool QDate.__ge__(QDate other)'''
        return bool()
    def __gt__(self, other):
        '''bool QDate.__gt__(QDate other)'''
        return bool()
    def __le__(self, other):
        '''bool QDate.__le__(QDate other)'''
        return bool()
    def __lt__(self, other):
        '''bool QDate.__lt__(QDate other)'''
        return bool()
    def __ne__(self, other):
        '''bool QDate.__ne__(QDate other)'''
        return bool()
    def __eq__(self, other):
        '''bool QDate.__eq__(QDate other)'''
        return bool()
    def daysTo(self):
        '''QDate QDate.daysTo()'''
        return QDate()
    def addYears(self, years):
        '''QDate QDate.addYears(int years)'''
        return QDate()
    def addMonths(self, months):
        '''QDate QDate.addMonths(int months)'''
        return QDate()
    def addDays(self, days):
        '''QDate QDate.addDays(int days)'''
        return QDate()
    def setYMD(self, y, m, d):
        '''bool QDate.setYMD(int y, int m, int d)'''
        return bool()
    def toString(self, format = Qt.TextDate):
        '''QString QDate.toString(Qt.DateFormat format = Qt.TextDate)'''
        return QString()
    def toString(self, format):
        '''QString QDate.toString(QString format)'''
        return QString()
    def longDayName(self, weekday):
        '''static QString QDate.longDayName(int weekday)'''
        return QString()
    def longDayName(self, weekday, type):
        '''static QString QDate.longDayName(int weekday, QDate.MonthNameType type)'''
        return QString()
    def longMonthName(self, month):
        '''static QString QDate.longMonthName(int month)'''
        return QString()
    def longMonthName(self, month, type):
        '''static QString QDate.longMonthName(int month, QDate.MonthNameType type)'''
        return QString()
    def shortDayName(self, weekday):
        '''static QString QDate.shortDayName(int weekday)'''
        return QString()
    def shortDayName(self, weekday, type):
        '''static QString QDate.shortDayName(int weekday, QDate.MonthNameType type)'''
        return QString()
    def shortMonthName(self, month):
        '''static QString QDate.shortMonthName(int month)'''
        return QString()
    def shortMonthName(self, month, type):
        '''static QString QDate.shortMonthName(int month, QDate.MonthNameType type)'''
        return QString()
    def weekNumber(self, yearNumber):
        '''int QDate.weekNumber(int yearNumber)'''
        return int()
    def daysInYear(self):
        '''int QDate.daysInYear()'''
        return int()
    def daysInMonth(self):
        '''int QDate.daysInMonth()'''
        return int()
    def dayOfYear(self):
        '''int QDate.dayOfYear()'''
        return int()
    def dayOfWeek(self):
        '''int QDate.dayOfWeek()'''
        return int()
    def day(self):
        '''int QDate.day()'''
        return int()
    def month(self):
        '''int QDate.month()'''
        return int()
    def year(self):
        '''int QDate.year()'''
        return int()
    def isValid(self):
        '''bool QDate.isValid()'''
        return bool()
    def isValid(self, y, m, d):
        '''static bool QDate.isValid(int y, int m, int d)'''
        return bool()
    def __bool__(self):
        '''int QDate.__bool__()'''
        return int()
    def isNull(self):
        '''bool QDate.isNull()'''
        return bool()
    def toPyDate(self):
        '''datetime.date QDate.toPyDate()'''
        return datetime.date()
    def __hash__(self):
        '''int QDate.__hash__()'''
        return int()
    def __repr__(self):
        '''str QDate.__repr__()'''
        return str()


class QTime():
    """"""
    def __init__(self):
        '''void QTime.__init__()'''
    def __init__(self, h, m, second = 0, msec = 0):
        '''void QTime.__init__(int h, int m, int second = 0, int msec = 0)'''
    def __init__(self):
        '''QTime QTime.__init__()'''
        return QTime()
    def elapsed(self):
        '''int QTime.elapsed()'''
        return int()
    def restart(self):
        '''int QTime.restart()'''
        return int()
    def start(self):
        '''void QTime.start()'''
    def fromString(self, string, format = Qt.TextDate):
        '''static QTime QTime.fromString(QString string, Qt.DateFormat format = Qt.TextDate)'''
        return QTime()
    def fromString(self, s, format):
        '''static QTime QTime.fromString(QString s, QString format)'''
        return QTime()
    def currentTime(self):
        '''static QTime QTime.currentTime()'''
        return QTime()
    def __ge__(self, other):
        '''bool QTime.__ge__(QTime other)'''
        return bool()
    def __gt__(self, other):
        '''bool QTime.__gt__(QTime other)'''
        return bool()
    def __le__(self, other):
        '''bool QTime.__le__(QTime other)'''
        return bool()
    def __lt__(self, other):
        '''bool QTime.__lt__(QTime other)'''
        return bool()
    def __ne__(self, other):
        '''bool QTime.__ne__(QTime other)'''
        return bool()
    def __eq__(self, other):
        '''bool QTime.__eq__(QTime other)'''
        return bool()
    def msecsTo(self):
        '''QTime QTime.msecsTo()'''
        return QTime()
    def addMSecs(self, ms):
        '''QTime QTime.addMSecs(int ms)'''
        return QTime()
    def secsTo(self):
        '''QTime QTime.secsTo()'''
        return QTime()
    def addSecs(self, secs):
        '''QTime QTime.addSecs(int secs)'''
        return QTime()
    def setHMS(self, h, m, s, msec = 0):
        '''bool QTime.setHMS(int h, int m, int s, int msec = 0)'''
        return bool()
    def toString(self, format = Qt.TextDate):
        '''QString QTime.toString(Qt.DateFormat format = Qt.TextDate)'''
        return QString()
    def toString(self, format):
        '''QString QTime.toString(QString format)'''
        return QString()
    def msec(self):
        '''int QTime.msec()'''
        return int()
    def second(self):
        '''int QTime.second()'''
        return int()
    def minute(self):
        '''int QTime.minute()'''
        return int()
    def hour(self):
        '''int QTime.hour()'''
        return int()
    def isValid(self):
        '''bool QTime.isValid()'''
        return bool()
    def isValid(self, h, m, s, msec = 0):
        '''static bool QTime.isValid(int h, int m, int s, int msec = 0)'''
        return bool()
    def __bool__(self):
        '''int QTime.__bool__()'''
        return int()
    def isNull(self):
        '''bool QTime.isNull()'''
        return bool()
    def toPyTime(self):
        '''datetime.time QTime.toPyTime()'''
        return datetime.time()
    def __hash__(self):
        '''int QTime.__hash__()'''
        return int()
    def __repr__(self):
        '''str QTime.__repr__()'''
        return str()


class QDateTime():
    """"""
    def __init__(self):
        '''void QDateTime.__init__()'''
    def __init__(self, other):
        '''void QDateTime.__init__(QDateTime other)'''
    def __init__(self):
        '''QDate QDateTime.__init__()'''
        return QDate()
    def __init__(self, date, time, timeSpec = Qt.LocalTime):
        '''void QDateTime.__init__(QDate date, QTime time, Qt.TimeSpec timeSpec = Qt.LocalTime)'''
    def __init__(self, y, m, d, h, m_, s = 0, msec = 0, timeSpec = 0):
        '''void QDateTime.__init__(int y, int m, int d, int h, int m, int s = 0, int msec = 0, int timeSpec = 0)'''
    def currentMSecsSinceEpoch(self):
        '''static int QDateTime.currentMSecsSinceEpoch()'''
        return int()
    def fromMSecsSinceEpoch(self, msecs):
        '''static QDateTime QDateTime.fromMSecsSinceEpoch(int msecs)'''
        return QDateTime()
    def currentDateTimeUtc(self):
        '''static QDateTime QDateTime.currentDateTimeUtc()'''
        return QDateTime()
    def msecsTo(self):
        '''QDateTime QDateTime.msecsTo()'''
        return QDateTime()
    def setMSecsSinceEpoch(self, msecs):
        '''void QDateTime.setMSecsSinceEpoch(int msecs)'''
    def toMSecsSinceEpoch(self):
        '''int QDateTime.toMSecsSinceEpoch()'''
        return int()
    def fromTime_t(self, secsSince1Jan1970UTC):
        '''static QDateTime QDateTime.fromTime_t(int secsSince1Jan1970UTC)'''
        return QDateTime()
    def fromString(self, string, format = Qt.TextDate):
        '''static QDateTime QDateTime.fromString(QString string, Qt.DateFormat format = Qt.TextDate)'''
        return QDateTime()
    def fromString(self, s, format):
        '''static QDateTime QDateTime.fromString(QString s, QString format)'''
        return QDateTime()
    def currentDateTime(self):
        '''static QDateTime QDateTime.currentDateTime()'''
        return QDateTime()
    def __ge__(self, other):
        '''bool QDateTime.__ge__(QDateTime other)'''
        return bool()
    def __gt__(self, other):
        '''bool QDateTime.__gt__(QDateTime other)'''
        return bool()
    def __le__(self, other):
        '''bool QDateTime.__le__(QDateTime other)'''
        return bool()
    def __lt__(self, other):
        '''bool QDateTime.__lt__(QDateTime other)'''
        return bool()
    def __ne__(self, other):
        '''bool QDateTime.__ne__(QDateTime other)'''
        return bool()
    def __eq__(self, other):
        '''bool QDateTime.__eq__(QDateTime other)'''
        return bool()
    def secsTo(self):
        '''QDateTime QDateTime.secsTo()'''
        return QDateTime()
    def daysTo(self):
        '''QDateTime QDateTime.daysTo()'''
        return QDateTime()
    def toUTC(self):
        '''QDateTime QDateTime.toUTC()'''
        return QDateTime()
    def toLocalTime(self):
        '''QDateTime QDateTime.toLocalTime()'''
        return QDateTime()
    def toTimeSpec(self, spec):
        '''QDateTime QDateTime.toTimeSpec(Qt.TimeSpec spec)'''
        return QDateTime()
    def addMSecs(self, msecs):
        '''QDateTime QDateTime.addMSecs(int msecs)'''
        return QDateTime()
    def addSecs(self, secs):
        '''QDateTime QDateTime.addSecs(int secs)'''
        return QDateTime()
    def addYears(self, years):
        '''QDateTime QDateTime.addYears(int years)'''
        return QDateTime()
    def addMonths(self, months):
        '''QDateTime QDateTime.addMonths(int months)'''
        return QDateTime()
    def addDays(self, days):
        '''QDateTime QDateTime.addDays(int days)'''
        return QDateTime()
    def toString(self, format = Qt.TextDate):
        '''QString QDateTime.toString(Qt.DateFormat format = Qt.TextDate)'''
        return QString()
    def toString(self, format):
        '''QString QDateTime.toString(QString format)'''
        return QString()
    def setTime_t(self, secsSince1Jan1970UTC):
        '''void QDateTime.setTime_t(int secsSince1Jan1970UTC)'''
    def setTimeSpec(self, spec):
        '''void QDateTime.setTimeSpec(Qt.TimeSpec spec)'''
    def setTime(self, time):
        '''void QDateTime.setTime(QTime time)'''
    def setDate(self, date):
        '''void QDateTime.setDate(QDate date)'''
    def toTime_t(self):
        '''int QDateTime.toTime_t()'''
        return int()
    def timeSpec(self):
        '''Qt.TimeSpec QDateTime.timeSpec()'''
        return Qt.TimeSpec()
    def time(self):
        '''QTime QDateTime.time()'''
        return QTime()
    def date(self):
        '''QDate QDateTime.date()'''
        return QDate()
    def isValid(self):
        '''bool QDateTime.isValid()'''
        return bool()
    def __bool__(self):
        '''int QDateTime.__bool__()'''
        return int()
    def isNull(self):
        '''bool QDateTime.isNull()'''
        return bool()
    def toPyDateTime(self):
        '''datetime.datetime QDateTime.toPyDateTime()'''
        return datetime.datetime()
    def __hash__(self):
        '''int QDateTime.__hash__()'''
        return int()
    def __repr__(self):
        '''str QDateTime.__repr__()'''
        return str()


class QDir():
    """"""
    # Enum QDir.SortFlag
    Name = 0
    Time = 0
    Size = 0
    Unsorted = 0
    SortByMask = 0
    DirsFirst = 0
    Reversed = 0
    IgnoreCase = 0
    DirsLast = 0
    LocaleAware = 0
    Type = 0
    NoSort = 0

    # Enum QDir.Filter
    Dirs = 0
    Files = 0
    Drives = 0
    NoSymLinks = 0
    AllEntries = 0
    TypeMask = 0
    Readable = 0
    Writable = 0
    Executable = 0
    PermissionMask = 0
    Modified = 0
    Hidden = 0
    System = 0
    AccessMask = 0
    AllDirs = 0
    CaseSensitive = 0
    NoDotAndDotDot = 0
    NoFilter = 0
    NoDot = 0
    NoDotDot = 0

    def __init__(self):
        '''QDir QDir.__init__()'''
        return QDir()
    def __init__(self, path = QString()):
        '''void QDir.__init__(QString path = QString())'''
    def __init__(self, path, nameFilter, sort = QDir.Name|QDir.IgnoreCase, filters = QDir.TypeMask):
        '''void QDir.__init__(QString path, QString nameFilter, QDir.SortFlags sort = QDir.Name|QDir.IgnoreCase, QDir.Filters filters = QDir.TypeMask)'''
    def searchPaths(self, prefix):
        '''static QStringList QDir.searchPaths(QString prefix)'''
        return QStringList()
    def addSearchPath(self, prefix, path):
        '''static void QDir.addSearchPath(QString prefix, QString path)'''
    def setSearchPaths(self, prefix, searchPaths):
        '''static void QDir.setSearchPaths(QString prefix, QStringList searchPaths)'''
    def fromNativeSeparators(self, pathName):
        '''static QString QDir.fromNativeSeparators(QString pathName)'''
        return QString()
    def toNativeSeparators(self, pathName):
        '''static QString QDir.toNativeSeparators(QString pathName)'''
        return QString()
    def cleanPath(self, path):
        '''static QString QDir.cleanPath(QString path)'''
        return QString()
    def match(self, filters, fileName):
        '''static bool QDir.match(QStringList filters, QString fileName)'''
        return bool()
    def match(self, filter, fileName):
        '''static bool QDir.match(QString filter, QString fileName)'''
        return bool()
    def tempPath(self):
        '''static QString QDir.tempPath()'''
        return QString()
    def temp(self):
        '''static QDir QDir.temp()'''
        return QDir()
    def rootPath(self):
        '''static QString QDir.rootPath()'''
        return QString()
    def root(self):
        '''static QDir QDir.root()'''
        return QDir()
    def homePath(self):
        '''static QString QDir.homePath()'''
        return QString()
    def home(self):
        '''static QDir QDir.home()'''
        return QDir()
    def currentPath(self):
        '''static QString QDir.currentPath()'''
        return QString()
    def current(self):
        '''static QDir QDir.current()'''
        return QDir()
    def setCurrent(self, path):
        '''static bool QDir.setCurrent(QString path)'''
        return bool()
    def separator(self):
        '''static QChar QDir.separator()'''
        return QChar()
    def drives(self):
        '''static list-of-QFileInfo QDir.drives()'''
        return [QFileInfo()]
    def refresh(self):
        '''void QDir.refresh()'''
    def rename(self, oldName, newName):
        '''bool QDir.rename(QString oldName, QString newName)'''
        return bool()
    def remove(self, fileName):
        '''bool QDir.remove(QString fileName)'''
        return bool()
    def __ne__(self, dir):
        '''bool QDir.__ne__(QDir dir)'''
        return bool()
    def __eq__(self, dir):
        '''bool QDir.__eq__(QDir dir)'''
        return bool()
    def makeAbsolute(self):
        '''bool QDir.makeAbsolute()'''
        return bool()
    def isAbsolute(self):
        '''bool QDir.isAbsolute()'''
        return bool()
    def isRelative(self):
        '''bool QDir.isRelative()'''
        return bool()
    def isAbsolutePath(self, path):
        '''static bool QDir.isAbsolutePath(QString path)'''
        return bool()
    def isRelativePath(self, path):
        '''static bool QDir.isRelativePath(QString path)'''
        return bool()
    def isRoot(self):
        '''bool QDir.isRoot()'''
        return bool()
    def exists(self):
        '''bool QDir.exists()'''
        return bool()
    def exists(self, name):
        '''bool QDir.exists(QString name)'''
        return bool()
    def isReadable(self):
        '''bool QDir.isReadable()'''
        return bool()
    def rmpath(self, dirPath):
        '''bool QDir.rmpath(QString dirPath)'''
        return bool()
    def mkpath(self, dirPath):
        '''bool QDir.mkpath(QString dirPath)'''
        return bool()
    def rmdir(self, dirName):
        '''bool QDir.rmdir(QString dirName)'''
        return bool()
    def mkdir(self, dirName):
        '''bool QDir.mkdir(QString dirName)'''
        return bool()
    def entryInfoList(self, filters = QDir.NoFilter, sort = QDir.NoSort):
        '''list-of-QFileInfo QDir.entryInfoList(QDir.Filters filters = QDir.NoFilter, QDir.SortFlags sort = QDir.NoSort)'''
        return [QFileInfo()]
    def entryInfoList(self, nameFilters, filters = QDir.NoFilter, sort = QDir.NoSort):
        '''list-of-QFileInfo QDir.entryInfoList(QStringList nameFilters, QDir.Filters filters = QDir.NoFilter, QDir.SortFlags sort = QDir.NoSort)'''
        return [QFileInfo()]
    def entryList(self, filters = QDir.NoFilter, sort = QDir.NoSort):
        '''QStringList QDir.entryList(QDir.Filters filters = QDir.NoFilter, QDir.SortFlags sort = QDir.NoSort)'''
        return QStringList()
    def entryList(self, nameFilters, filters = QDir.NoFilter, sort = QDir.NoSort):
        '''QStringList QDir.entryList(QStringList nameFilters, QDir.Filters filters = QDir.NoFilter, QDir.SortFlags sort = QDir.NoSort)'''
        return QStringList()
    def nameFiltersFromString(self, nameFilter):
        '''static QStringList QDir.nameFiltersFromString(QString nameFilter)'''
        return QStringList()
    def __contains__(self):
        '''QString QDir.__contains__()'''
        return QString()
    def __getitem__(self):
        '''int QDir.__getitem__()'''
        return int()
    def __getitem__(self):
        '''slice QDir.__getitem__()'''
        return slice()
    def __len__(self):
        ''' QDir.__len__()'''
        return ()
    def count(self):
        '''int QDir.count()'''
        return int()
    def setSorting(self, sort):
        '''void QDir.setSorting(QDir.SortFlags sort)'''
    def sorting(self):
        '''QDir.SortFlags QDir.sorting()'''
        return QDir.SortFlags()
    def setFilter(self, filter):
        '''void QDir.setFilter(QDir.Filters filter)'''
    def filter(self):
        '''QDir.Filters QDir.filter()'''
        return QDir.Filters()
    def setNameFilters(self, nameFilters):
        '''void QDir.setNameFilters(QStringList nameFilters)'''
    def nameFilters(self):
        '''QStringList QDir.nameFilters()'''
        return QStringList()
    def cdUp(self):
        '''bool QDir.cdUp()'''
        return bool()
    def cd(self, dirName):
        '''bool QDir.cd(QString dirName)'''
        return bool()
    def convertSeparators(self, pathName):
        '''static QString QDir.convertSeparators(QString pathName)'''
        return QString()
    def relativeFilePath(self, fileName):
        '''QString QDir.relativeFilePath(QString fileName)'''
        return QString()
    def absoluteFilePath(self, fileName):
        '''QString QDir.absoluteFilePath(QString fileName)'''
        return QString()
    def filePath(self, fileName):
        '''QString QDir.filePath(QString fileName)'''
        return QString()
    def dirName(self):
        '''QString QDir.dirName()'''
        return QString()
    def addResourceSearchPath(self, path):
        '''static void QDir.addResourceSearchPath(QString path)'''
    def canonicalPath(self):
        '''QString QDir.canonicalPath()'''
        return QString()
    def absolutePath(self):
        '''QString QDir.absolutePath()'''
        return QString()
    def path(self):
        '''QString QDir.path()'''
        return QString()
    def setPath(self, path):
        '''void QDir.setPath(QString path)'''
    class Filters():
        """"""
        def __init__(self):
            '''QDir.Filters QDir.Filters.__init__()'''
            return QDir.Filters()
        def __init__(self):
            '''int QDir.Filters.__init__()'''
            return int()
        def __init__(self):
            '''void QDir.Filters.__init__()'''
        def __bool__(self):
            '''int QDir.Filters.__bool__()'''
            return int()
        def __ne__(self, f):
            '''bool QDir.Filters.__ne__(QDir.Filters f)'''
            return bool()
        def __eq__(self, f):
            '''bool QDir.Filters.__eq__(QDir.Filters f)'''
            return bool()
        def __invert__(self):
            '''QDir.Filters QDir.Filters.__invert__()'''
            return QDir.Filters()
        def __and__(self, mask):
            '''QDir.Filters QDir.Filters.__and__(int mask)'''
            return QDir.Filters()
        def __xor__(self, f):
            '''QDir.Filters QDir.Filters.__xor__(QDir.Filters f)'''
            return QDir.Filters()
        def __xor__(self, f):
            '''QDir.Filters QDir.Filters.__xor__(int f)'''
            return QDir.Filters()
        def __or__(self, f):
            '''QDir.Filters QDir.Filters.__or__(QDir.Filters f)'''
            return QDir.Filters()
        def __or__(self, f):
            '''QDir.Filters QDir.Filters.__or__(int f)'''
            return QDir.Filters()
        def __int__(self):
            '''int QDir.Filters.__int__()'''
            return int()
        def __ixor__(self, f):
            '''QDir.Filters QDir.Filters.__ixor__(QDir.Filters f)'''
            return QDir.Filters()
        def __ior__(self, f):
            '''QDir.Filters QDir.Filters.__ior__(QDir.Filters f)'''
            return QDir.Filters()
        def __iand__(self, mask):
            '''QDir.Filters QDir.Filters.__iand__(int mask)'''
            return QDir.Filters()
    class SortFlags():
        """"""
        def __init__(self):
            '''QDir.SortFlags QDir.SortFlags.__init__()'''
            return QDir.SortFlags()
        def __init__(self):
            '''int QDir.SortFlags.__init__()'''
            return int()
        def __init__(self):
            '''void QDir.SortFlags.__init__()'''
        def __bool__(self):
            '''int QDir.SortFlags.__bool__()'''
            return int()
        def __ne__(self, f):
            '''bool QDir.SortFlags.__ne__(QDir.SortFlags f)'''
            return bool()
        def __eq__(self, f):
            '''bool QDir.SortFlags.__eq__(QDir.SortFlags f)'''
            return bool()
        def __invert__(self):
            '''QDir.SortFlags QDir.SortFlags.__invert__()'''
            return QDir.SortFlags()
        def __and__(self, mask):
            '''QDir.SortFlags QDir.SortFlags.__and__(int mask)'''
            return QDir.SortFlags()
        def __xor__(self, f):
            '''QDir.SortFlags QDir.SortFlags.__xor__(QDir.SortFlags f)'''
            return QDir.SortFlags()
        def __xor__(self, f):
            '''QDir.SortFlags QDir.SortFlags.__xor__(int f)'''
            return QDir.SortFlags()
        def __or__(self, f):
            '''QDir.SortFlags QDir.SortFlags.__or__(QDir.SortFlags f)'''
            return QDir.SortFlags()
        def __or__(self, f):
            '''QDir.SortFlags QDir.SortFlags.__or__(int f)'''
            return QDir.SortFlags()
        def __int__(self):
            '''int QDir.SortFlags.__int__()'''
            return int()
        def __ixor__(self, f):
            '''QDir.SortFlags QDir.SortFlags.__ixor__(QDir.SortFlags f)'''
            return QDir.SortFlags()
        def __ior__(self, f):
            '''QDir.SortFlags QDir.SortFlags.__ior__(QDir.SortFlags f)'''
            return QDir.SortFlags()
        def __iand__(self, mask):
            '''QDir.SortFlags QDir.SortFlags.__iand__(int mask)'''
            return QDir.SortFlags()


class QDirIterator():
    """"""
    # Enum QDirIterator.IteratorFlag
    NoIteratorFlags = 0
    FollowSymlinks = 0
    Subdirectories = 0

    def __init__(self, dir, flags = QDirIterator.NoIteratorFlags):
        '''void QDirIterator.__init__(QDir dir, QDirIterator.IteratorFlags flags = QDirIterator.NoIteratorFlags)'''
    def __init__(self, path, flags = QDirIterator.NoIteratorFlags):
        '''void QDirIterator.__init__(QString path, QDirIterator.IteratorFlags flags = QDirIterator.NoIteratorFlags)'''
    def __init__(self, path, filters, flags = QDirIterator.NoIteratorFlags):
        '''void QDirIterator.__init__(QString path, QDir.Filters filters, QDirIterator.IteratorFlags flags = QDirIterator.NoIteratorFlags)'''
    def __init__(self, path, nameFilters, filters = QDir.NoFilter, flags = QDirIterator.NoIteratorFlags):
        '''void QDirIterator.__init__(QString path, QStringList nameFilters, QDir.Filters filters = QDir.NoFilter, QDirIterator.IteratorFlags flags = QDirIterator.NoIteratorFlags)'''
    def path(self):
        '''QString QDirIterator.path()'''
        return QString()
    def fileInfo(self):
        '''QFileInfo QDirIterator.fileInfo()'''
        return QFileInfo()
    def filePath(self):
        '''QString QDirIterator.filePath()'''
        return QString()
    def fileName(self):
        '''QString QDirIterator.fileName()'''
        return QString()
    def hasNext(self):
        '''bool QDirIterator.hasNext()'''
        return bool()
    def next(self):
        '''QString QDirIterator.next()'''
        return QString()
    class IteratorFlags():
        """"""
        def __init__(self):
            '''QDirIterator.IteratorFlags QDirIterator.IteratorFlags.__init__()'''
            return QDirIterator.IteratorFlags()
        def __init__(self):
            '''int QDirIterator.IteratorFlags.__init__()'''
            return int()
        def __init__(self):
            '''void QDirIterator.IteratorFlags.__init__()'''
        def __bool__(self):
            '''int QDirIterator.IteratorFlags.__bool__()'''
            return int()
        def __ne__(self, f):
            '''bool QDirIterator.IteratorFlags.__ne__(QDirIterator.IteratorFlags f)'''
            return bool()
        def __eq__(self, f):
            '''bool QDirIterator.IteratorFlags.__eq__(QDirIterator.IteratorFlags f)'''
            return bool()
        def __invert__(self):
            '''QDirIterator.IteratorFlags QDirIterator.IteratorFlags.__invert__()'''
            return QDirIterator.IteratorFlags()
        def __and__(self, mask):
            '''QDirIterator.IteratorFlags QDirIterator.IteratorFlags.__and__(int mask)'''
            return QDirIterator.IteratorFlags()
        def __xor__(self, f):
            '''QDirIterator.IteratorFlags QDirIterator.IteratorFlags.__xor__(QDirIterator.IteratorFlags f)'''
            return QDirIterator.IteratorFlags()
        def __xor__(self, f):
            '''QDirIterator.IteratorFlags QDirIterator.IteratorFlags.__xor__(int f)'''
            return QDirIterator.IteratorFlags()
        def __or__(self, f):
            '''QDirIterator.IteratorFlags QDirIterator.IteratorFlags.__or__(QDirIterator.IteratorFlags f)'''
            return QDirIterator.IteratorFlags()
        def __or__(self, f):
            '''QDirIterator.IteratorFlags QDirIterator.IteratorFlags.__or__(int f)'''
            return QDirIterator.IteratorFlags()
        def __int__(self):
            '''int QDirIterator.IteratorFlags.__int__()'''
            return int()
        def __ixor__(self, f):
            '''QDirIterator.IteratorFlags QDirIterator.IteratorFlags.__ixor__(QDirIterator.IteratorFlags f)'''
            return QDirIterator.IteratorFlags()
        def __ior__(self, f):
            '''QDirIterator.IteratorFlags QDirIterator.IteratorFlags.__ior__(QDirIterator.IteratorFlags f)'''
            return QDirIterator.IteratorFlags()
        def __iand__(self, mask):
            '''QDirIterator.IteratorFlags QDirIterator.IteratorFlags.__iand__(int mask)'''
            return QDirIterator.IteratorFlags()


class QEasingCurve():
    """"""
    # Enum QEasingCurve.Type
    Linear = 0
    InQuad = 0
    OutQuad = 0
    InOutQuad = 0
    OutInQuad = 0
    InCubic = 0
    OutCubic = 0
    InOutCubic = 0
    OutInCubic = 0
    InQuart = 0
    OutQuart = 0
    InOutQuart = 0
    OutInQuart = 0
    InQuint = 0
    OutQuint = 0
    InOutQuint = 0
    OutInQuint = 0
    InSine = 0
    OutSine = 0
    InOutSine = 0
    OutInSine = 0
    InExpo = 0
    OutExpo = 0
    InOutExpo = 0
    OutInExpo = 0
    InCirc = 0
    OutCirc = 0
    InOutCirc = 0
    OutInCirc = 0
    InElastic = 0
    OutElastic = 0
    InOutElastic = 0
    OutInElastic = 0
    InBack = 0
    OutBack = 0
    InOutBack = 0
    OutInBack = 0
    InBounce = 0
    OutBounce = 0
    InOutBounce = 0
    OutInBounce = 0
    InCurve = 0
    OutCurve = 0
    SineCurve = 0
    CosineCurve = 0
    Custom = 0

    def __init__(self, type = QEasingCurve.Linear):
        '''void QEasingCurve.__init__(QEasingCurve.Type type = QEasingCurve.Linear)'''
    def __init__(self, other):
        '''void QEasingCurve.__init__(QEasingCurve other)'''
    def valueForProgress(self, progress):
        '''float QEasingCurve.valueForProgress(float progress)'''
        return float()
    def customType(self):
        '''callable QEasingCurve.customType()'''
        return callable()
    def setCustomType(self, func):
        '''void QEasingCurve.setCustomType(callable func)'''
    def setType(self, type):
        '''void QEasingCurve.setType(QEasingCurve.Type type)'''
    def type(self):
        '''QEasingCurve.Type QEasingCurve.type()'''
        return QEasingCurve.Type()
    def setOvershoot(self, overshoot):
        '''void QEasingCurve.setOvershoot(float overshoot)'''
    def overshoot(self):
        '''float QEasingCurve.overshoot()'''
        return float()
    def setPeriod(self, period):
        '''void QEasingCurve.setPeriod(float period)'''
    def period(self):
        '''float QEasingCurve.period()'''
        return float()
    def setAmplitude(self, amplitude):
        '''void QEasingCurve.setAmplitude(float amplitude)'''
    def amplitude(self):
        '''float QEasingCurve.amplitude()'''
        return float()
    def __ne__(self, other):
        '''bool QEasingCurve.__ne__(QEasingCurve other)'''
        return bool()
    def __eq__(self, other):
        '''bool QEasingCurve.__eq__(QEasingCurve other)'''
        return bool()


class QElapsedTimer():
    """"""
    # Enum QElapsedTimer.ClockType
    SystemTime = 0
    MonotonicClock = 0
    TickCounter = 0
    MachAbsoluteTime = 0
    PerformanceCounter = 0

    def __init__(self):
        '''void QElapsedTimer.__init__()'''
    def __init__(self):
        '''QElapsedTimer QElapsedTimer.__init__()'''
        return QElapsedTimer()
    def __ge__(self, v2):
        '''bool QElapsedTimer.__ge__(QElapsedTimer v2)'''
        return bool()
    def __lt__(self, v2):
        '''bool QElapsedTimer.__lt__(QElapsedTimer v2)'''
        return bool()
    def nsecsElapsed(self):
        '''int QElapsedTimer.nsecsElapsed()'''
        return int()
    def __ne__(self, other):
        '''bool QElapsedTimer.__ne__(QElapsedTimer other)'''
        return bool()
    def __eq__(self, other):
        '''bool QElapsedTimer.__eq__(QElapsedTimer other)'''
        return bool()
    def secsTo(self, other):
        '''int QElapsedTimer.secsTo(QElapsedTimer other)'''
        return int()
    def msecsTo(self, other):
        '''int QElapsedTimer.msecsTo(QElapsedTimer other)'''
        return int()
    def msecsSinceReference(self):
        '''int QElapsedTimer.msecsSinceReference()'''
        return int()
    def hasExpired(self, timeout):
        '''bool QElapsedTimer.hasExpired(int timeout)'''
        return bool()
    def elapsed(self):
        '''int QElapsedTimer.elapsed()'''
        return int()
    def isValid(self):
        '''bool QElapsedTimer.isValid()'''
        return bool()
    def invalidate(self):
        '''void QElapsedTimer.invalidate()'''
    def restart(self):
        '''int QElapsedTimer.restart()'''
        return int()
    def start(self):
        '''void QElapsedTimer.start()'''
    def isMonotonic(self):
        '''static bool QElapsedTimer.isMonotonic()'''
        return bool()
    def clockType(self):
        '''static QElapsedTimer.ClockType QElapsedTimer.clockType()'''
        return QElapsedTimer.ClockType()


class QEventLoop(QObject):
    """"""
    # Enum QEventLoop.ProcessEventsFlag
    AllEvents = 0
    ExcludeUserInputEvents = 0
    ExcludeSocketNotifiers = 0
    WaitForMoreEvents = 0
    X11ExcludeTimers = 0
    DeferredDeletion = 0

    def __init__(self, parent = None):
        '''void QEventLoop.__init__(QObject parent = None)'''
    def quit(self):
        '''void QEventLoop.quit()'''
    def wakeUp(self):
        '''void QEventLoop.wakeUp()'''
    def isRunning(self):
        '''bool QEventLoop.isRunning()'''
        return bool()
    def exit(self, returnCode = 0):
        '''void QEventLoop.exit(int returnCode = 0)'''
    def exec_(self, flags = QEventLoop.AllEvents):
        '''int QEventLoop.exec_(QEventLoop.ProcessEventsFlags flags = QEventLoop.AllEvents)'''
        return int()
    def processEvents(self, flags = QEventLoop.AllEvents):
        '''bool QEventLoop.processEvents(QEventLoop.ProcessEventsFlags flags = QEventLoop.AllEvents)'''
        return bool()
    def processEvents(self, flags, maximumTime):
        '''void QEventLoop.processEvents(QEventLoop.ProcessEventsFlags flags, int maximumTime)'''
    class ProcessEventsFlags():
        """"""
        def __init__(self):
            '''QEventLoop.ProcessEventsFlags QEventLoop.ProcessEventsFlags.__init__()'''
            return QEventLoop.ProcessEventsFlags()
        def __init__(self):
            '''int QEventLoop.ProcessEventsFlags.__init__()'''
            return int()
        def __init__(self):
            '''void QEventLoop.ProcessEventsFlags.__init__()'''
        def __bool__(self):
            '''int QEventLoop.ProcessEventsFlags.__bool__()'''
            return int()
        def __ne__(self, f):
            '''bool QEventLoop.ProcessEventsFlags.__ne__(QEventLoop.ProcessEventsFlags f)'''
            return bool()
        def __eq__(self, f):
            '''bool QEventLoop.ProcessEventsFlags.__eq__(QEventLoop.ProcessEventsFlags f)'''
            return bool()
        def __invert__(self):
            '''QEventLoop.ProcessEventsFlags QEventLoop.ProcessEventsFlags.__invert__()'''
            return QEventLoop.ProcessEventsFlags()
        def __and__(self, mask):
            '''QEventLoop.ProcessEventsFlags QEventLoop.ProcessEventsFlags.__and__(int mask)'''
            return QEventLoop.ProcessEventsFlags()
        def __xor__(self, f):
            '''QEventLoop.ProcessEventsFlags QEventLoop.ProcessEventsFlags.__xor__(QEventLoop.ProcessEventsFlags f)'''
            return QEventLoop.ProcessEventsFlags()
        def __xor__(self, f):
            '''QEventLoop.ProcessEventsFlags QEventLoop.ProcessEventsFlags.__xor__(int f)'''
            return QEventLoop.ProcessEventsFlags()
        def __or__(self, f):
            '''QEventLoop.ProcessEventsFlags QEventLoop.ProcessEventsFlags.__or__(QEventLoop.ProcessEventsFlags f)'''
            return QEventLoop.ProcessEventsFlags()
        def __or__(self, f):
            '''QEventLoop.ProcessEventsFlags QEventLoop.ProcessEventsFlags.__or__(int f)'''
            return QEventLoop.ProcessEventsFlags()
        def __int__(self):
            '''int QEventLoop.ProcessEventsFlags.__int__()'''
            return int()
        def __ixor__(self, f):
            '''QEventLoop.ProcessEventsFlags QEventLoop.ProcessEventsFlags.__ixor__(QEventLoop.ProcessEventsFlags f)'''
            return QEventLoop.ProcessEventsFlags()
        def __ior__(self, f):
            '''QEventLoop.ProcessEventsFlags QEventLoop.ProcessEventsFlags.__ior__(QEventLoop.ProcessEventsFlags f)'''
            return QEventLoop.ProcessEventsFlags()
        def __iand__(self, mask):
            '''QEventLoop.ProcessEventsFlags QEventLoop.ProcessEventsFlags.__iand__(int mask)'''
            return QEventLoop.ProcessEventsFlags()


class QEventTransition(QAbstractTransition):
    """"""
    def __init__(self, sourceState = None):
        '''void QEventTransition.__init__(QState sourceState = None)'''
    def __init__(self, object, type, sourceState = None):
        '''void QEventTransition.__init__(QObject object, QEvent.Type type, QState sourceState = None)'''
    def event(self, e):
        '''bool QEventTransition.event(QEvent e)'''
        return bool()
    def onTransition(self, event):
        '''void QEventTransition.onTransition(QEvent event)'''
    def eventTest(self, event):
        '''bool QEventTransition.eventTest(QEvent event)'''
        return bool()
    def setEventType(self, type):
        '''void QEventTransition.setEventType(QEvent.Type type)'''
    def eventType(self):
        '''QEvent.Type QEventTransition.eventType()'''
        return QEvent.Type()
    def setEventSource(self, object):
        '''void QEventTransition.setEventSource(QObject object)'''
    def eventSource(self):
        '''QObject QEventTransition.eventSource()'''
        return QObject()


class QFile(QIODevice):
    """"""
    # Enum QFile.FileHandleFlag
    AutoCloseHandle = 0
    DontCloseHandle = 0

    # Enum QFile.Permission
    ReadOwner = 0
    WriteOwner = 0
    ExeOwner = 0
    ReadUser = 0
    WriteUser = 0
    ExeUser = 0
    ReadGroup = 0
    WriteGroup = 0
    ExeGroup = 0
    ReadOther = 0
    WriteOther = 0
    ExeOther = 0

    # Enum QFile.MemoryMapFlags
    NoOptions = 0

    # Enum QFile.FileError
    NoError = 0
    ReadError = 0
    WriteError = 0
    FatalError = 0
    ResourceError = 0
    OpenError = 0
    AbortError = 0
    TimeOutError = 0
    UnspecifiedError = 0
    RemoveError = 0
    RenameError = 0
    PositionError = 0
    ResizeError = 0
    PermissionsError = 0
    CopyError = 0

    def __init__(self):
        '''void QFile.__init__()'''
    def __init__(self, name):
        '''void QFile.__init__(QString name)'''
    def __init__(self, parent):
        '''void QFile.__init__(QObject parent)'''
    def __init__(self, name, parent):
        '''void QFile.__init__(QString name, QObject parent)'''
    def writeData(self, data):
        '''int QFile.writeData(str data)'''
        return int()
    def readLineData(self, maxlen):
        '''str QFile.readLineData(int maxlen)'''
        return str()
    def readData(self, maxlen):
        '''str QFile.readData(int maxlen)'''
        return str()
    def unmap(self, address):
        '''bool QFile.unmap(sip.voidptr address)'''
        return bool()
    def map(self, offset, size, flags = QFile.NoOptions):
        '''sip.voidptr QFile.map(int offset, int size, QFile.MemoryMapFlags flags = QFile.NoOptions)'''
        return sip.voidptr()
    def symLinkTarget(self):
        '''QString QFile.symLinkTarget()'''
        return QString()
    def symLinkTarget(self, fileName):
        '''static QString QFile.symLinkTarget(QString fileName)'''
        return QString()
    def fileEngine(self):
        '''QAbstractFileEngine QFile.fileEngine()'''
        return QAbstractFileEngine()
    def handle(self):
        '''int QFile.handle()'''
        return int()
    def setPermissions(self, permissionSpec):
        '''bool QFile.setPermissions(QFile.Permissions permissionSpec)'''
        return bool()
    def setPermissions(self, filename, permissionSpec):
        '''static bool QFile.setPermissions(QString filename, QFile.Permissions permissionSpec)'''
        return bool()
    def permissions(self):
        '''QFile.Permissions QFile.permissions()'''
        return QFile.Permissions()
    def permissions(self, filename):
        '''static QFile.Permissions QFile.permissions(QString filename)'''
        return QFile.Permissions()
    def resize(self, sz):
        '''bool QFile.resize(int sz)'''
        return bool()
    def resize(self, filename, sz):
        '''static bool QFile.resize(QString filename, int sz)'''
        return bool()
    def flush(self):
        '''bool QFile.flush()'''
        return bool()
    def atEnd(self):
        '''bool QFile.atEnd()'''
        return bool()
    def seek(self, offset):
        '''bool QFile.seek(int offset)'''
        return bool()
    def pos(self):
        '''int QFile.pos()'''
        return int()
    def size(self):
        '''int QFile.size()'''
        return int()
    def close(self):
        '''void QFile.close()'''
    def open(self, flags):
        '''bool QFile.open(QIODevice.OpenMode flags)'''
        return bool()
    def open(self, fd, flags):
        '''bool QFile.open(int fd, QIODevice.OpenMode flags)'''
        return bool()
    def open(self, fd, flags, handleFlags):
        '''bool QFile.open(int fd, QIODevice.OpenMode flags, QFile.FileHandleFlags handleFlags)'''
        return bool()
    def isSequential(self):
        '''bool QFile.isSequential()'''
        return bool()
    def copy(self, newName):
        '''bool QFile.copy(QString newName)'''
        return bool()
    def copy(self, fileName, newName):
        '''static bool QFile.copy(QString fileName, QString newName)'''
        return bool()
    def link(self, newName):
        '''bool QFile.link(QString newName)'''
        return bool()
    def link(self, oldname, newName):
        '''static bool QFile.link(QString oldname, QString newName)'''
        return bool()
    def rename(self, newName):
        '''bool QFile.rename(QString newName)'''
        return bool()
    def rename(self, oldName, newName):
        '''static bool QFile.rename(QString oldName, QString newName)'''
        return bool()
    def remove(self):
        '''bool QFile.remove()'''
        return bool()
    def remove(self, fileName):
        '''static bool QFile.remove(QString fileName)'''
        return bool()
    def readLink(self):
        '''QString QFile.readLink()'''
        return QString()
    def readLink(self, fileName):
        '''static QString QFile.readLink(QString fileName)'''
        return QString()
    def exists(self):
        '''bool QFile.exists()'''
        return bool()
    def exists(self, fileName):
        '''static bool QFile.exists(QString fileName)'''
        return bool()
    def decodeName(self, localFileName):
        '''static QString QFile.decodeName(QByteArray localFileName)'''
        return QString()
    def decodeName(self, localFileName):
        '''static QString QFile.decodeName(str localFileName)'''
        return QString()
    def encodeName(self, fileName):
        '''static QByteArray QFile.encodeName(QString fileName)'''
        return QByteArray()
    def setFileName(self, name):
        '''void QFile.setFileName(QString name)'''
    def fileName(self):
        '''QString QFile.fileName()'''
        return QString()
    def unsetError(self):
        '''void QFile.unsetError()'''
    def error(self):
        '''QFile.FileError QFile.error()'''
        return QFile.FileError()
    class FileHandleFlags():
        """"""
        def __init__(self):
            '''QFile.FileHandleFlags QFile.FileHandleFlags.__init__()'''
            return QFile.FileHandleFlags()
        def __init__(self):
            '''int QFile.FileHandleFlags.__init__()'''
            return int()
        def __init__(self):
            '''void QFile.FileHandleFlags.__init__()'''
        def __bool__(self):
            '''int QFile.FileHandleFlags.__bool__()'''
            return int()
        def __ne__(self, f):
            '''bool QFile.FileHandleFlags.__ne__(QFile.FileHandleFlags f)'''
            return bool()
        def __eq__(self, f):
            '''bool QFile.FileHandleFlags.__eq__(QFile.FileHandleFlags f)'''
            return bool()
        def __invert__(self):
            '''QFile.FileHandleFlags QFile.FileHandleFlags.__invert__()'''
            return QFile.FileHandleFlags()
        def __and__(self, mask):
            '''QFile.FileHandleFlags QFile.FileHandleFlags.__and__(int mask)'''
            return QFile.FileHandleFlags()
        def __xor__(self, f):
            '''QFile.FileHandleFlags QFile.FileHandleFlags.__xor__(QFile.FileHandleFlags f)'''
            return QFile.FileHandleFlags()
        def __xor__(self, f):
            '''QFile.FileHandleFlags QFile.FileHandleFlags.__xor__(int f)'''
            return QFile.FileHandleFlags()
        def __or__(self, f):
            '''QFile.FileHandleFlags QFile.FileHandleFlags.__or__(QFile.FileHandleFlags f)'''
            return QFile.FileHandleFlags()
        def __or__(self, f):
            '''QFile.FileHandleFlags QFile.FileHandleFlags.__or__(int f)'''
            return QFile.FileHandleFlags()
        def __int__(self):
            '''int QFile.FileHandleFlags.__int__()'''
            return int()
        def __ixor__(self, f):
            '''QFile.FileHandleFlags QFile.FileHandleFlags.__ixor__(QFile.FileHandleFlags f)'''
            return QFile.FileHandleFlags()
        def __ior__(self, f):
            '''QFile.FileHandleFlags QFile.FileHandleFlags.__ior__(QFile.FileHandleFlags f)'''
            return QFile.FileHandleFlags()
        def __iand__(self, mask):
            '''QFile.FileHandleFlags QFile.FileHandleFlags.__iand__(int mask)'''
            return QFile.FileHandleFlags()
    class Permissions():
        """"""
        def __init__(self):
            '''QFile.Permissions QFile.Permissions.__init__()'''
            return QFile.Permissions()
        def __init__(self):
            '''int QFile.Permissions.__init__()'''
            return int()
        def __init__(self):
            '''void QFile.Permissions.__init__()'''
        def __bool__(self):
            '''int QFile.Permissions.__bool__()'''
            return int()
        def __ne__(self, f):
            '''bool QFile.Permissions.__ne__(QFile.Permissions f)'''
            return bool()
        def __eq__(self, f):
            '''bool QFile.Permissions.__eq__(QFile.Permissions f)'''
            return bool()
        def __invert__(self):
            '''QFile.Permissions QFile.Permissions.__invert__()'''
            return QFile.Permissions()
        def __and__(self, mask):
            '''QFile.Permissions QFile.Permissions.__and__(int mask)'''
            return QFile.Permissions()
        def __xor__(self, f):
            '''QFile.Permissions QFile.Permissions.__xor__(QFile.Permissions f)'''
            return QFile.Permissions()
        def __xor__(self, f):
            '''QFile.Permissions QFile.Permissions.__xor__(int f)'''
            return QFile.Permissions()
        def __or__(self, f):
            '''QFile.Permissions QFile.Permissions.__or__(QFile.Permissions f)'''
            return QFile.Permissions()
        def __or__(self, f):
            '''QFile.Permissions QFile.Permissions.__or__(int f)'''
            return QFile.Permissions()
        def __int__(self):
            '''int QFile.Permissions.__int__()'''
            return int()
        def __ixor__(self, f):
            '''QFile.Permissions QFile.Permissions.__ixor__(QFile.Permissions f)'''
            return QFile.Permissions()
        def __ior__(self, f):
            '''QFile.Permissions QFile.Permissions.__ior__(QFile.Permissions f)'''
            return QFile.Permissions()
        def __iand__(self, mask):
            '''QFile.Permissions QFile.Permissions.__iand__(int mask)'''
            return QFile.Permissions()


class QFileInfo():
    """"""
    def __init__(self):
        '''void QFileInfo.__init__()'''
    def __init__(self, file):
        '''void QFileInfo.__init__(QString file)'''
    def __init__(self, file):
        '''void QFileInfo.__init__(QFile file)'''
    def __init__(self, dir, file):
        '''void QFileInfo.__init__(QDir dir, QString file)'''
    def __init__(self, fileinfo):
        '''void QFileInfo.__init__(QFileInfo fileinfo)'''
    def isBundle(self):
        '''bool QFileInfo.isBundle()'''
        return bool()
    def bundleName(self):
        '''QString QFileInfo.bundleName()'''
        return QString()
    def symLinkTarget(self):
        '''QString QFileInfo.symLinkTarget()'''
        return QString()
    def setCaching(self, on):
        '''void QFileInfo.setCaching(bool on)'''
    def caching(self):
        '''bool QFileInfo.caching()'''
        return bool()
    def detach(self):
        '''void QFileInfo.detach()'''
    def lastRead(self):
        '''QDateTime QFileInfo.lastRead()'''
        return QDateTime()
    def lastModified(self):
        '''QDateTime QFileInfo.lastModified()'''
        return QDateTime()
    def created(self):
        '''QDateTime QFileInfo.created()'''
        return QDateTime()
    def size(self):
        '''int QFileInfo.size()'''
        return int()
    def permissions(self):
        '''QFile.Permissions QFileInfo.permissions()'''
        return QFile.Permissions()
    def permission(self, permissions):
        '''bool QFileInfo.permission(QFile.Permissions permissions)'''
        return bool()
    def groupId(self):
        '''int QFileInfo.groupId()'''
        return int()
    def group(self):
        '''QString QFileInfo.group()'''
        return QString()
    def ownerId(self):
        '''int QFileInfo.ownerId()'''
        return int()
    def owner(self):
        '''QString QFileInfo.owner()'''
        return QString()
    def readLink(self):
        '''QString QFileInfo.readLink()'''
        return QString()
    def isRoot(self):
        '''bool QFileInfo.isRoot()'''
        return bool()
    def isSymLink(self):
        '''bool QFileInfo.isSymLink()'''
        return bool()
    def isDir(self):
        '''bool QFileInfo.isDir()'''
        return bool()
    def isFile(self):
        '''bool QFileInfo.isFile()'''
        return bool()
    def makeAbsolute(self):
        '''bool QFileInfo.makeAbsolute()'''
        return bool()
    def isAbsolute(self):
        '''bool QFileInfo.isAbsolute()'''
        return bool()
    def isRelative(self):
        '''bool QFileInfo.isRelative()'''
        return bool()
    def isHidden(self):
        '''bool QFileInfo.isHidden()'''
        return bool()
    def isExecutable(self):
        '''bool QFileInfo.isExecutable()'''
        return bool()
    def isWritable(self):
        '''bool QFileInfo.isWritable()'''
        return bool()
    def isReadable(self):
        '''bool QFileInfo.isReadable()'''
        return bool()
    def absoluteDir(self):
        '''QDir QFileInfo.absoluteDir()'''
        return QDir()
    def dir(self):
        '''QDir QFileInfo.dir()'''
        return QDir()
    def canonicalPath(self):
        '''QString QFileInfo.canonicalPath()'''
        return QString()
    def absolutePath(self):
        '''QString QFileInfo.absolutePath()'''
        return QString()
    def path(self):
        '''QString QFileInfo.path()'''
        return QString()
    def completeSuffix(self):
        '''QString QFileInfo.completeSuffix()'''
        return QString()
    def suffix(self):
        '''QString QFileInfo.suffix()'''
        return QString()
    def completeBaseName(self):
        '''QString QFileInfo.completeBaseName()'''
        return QString()
    def baseName(self):
        '''QString QFileInfo.baseName()'''
        return QString()
    def fileName(self):
        '''QString QFileInfo.fileName()'''
        return QString()
    def canonicalFilePath(self):
        '''QString QFileInfo.canonicalFilePath()'''
        return QString()
    def absoluteFilePath(self):
        '''QString QFileInfo.absoluteFilePath()'''
        return QString()
    def filePath(self):
        '''QString QFileInfo.filePath()'''
        return QString()
    def refresh(self):
        '''void QFileInfo.refresh()'''
    def exists(self):
        '''bool QFileInfo.exists()'''
        return bool()
    def setFile(self, file):
        '''void QFileInfo.setFile(QString file)'''
    def setFile(self, file):
        '''void QFileInfo.setFile(QFile file)'''
    def setFile(self, dir, file):
        '''void QFileInfo.setFile(QDir dir, QString file)'''
    def __ne__(self, fileinfo):
        '''bool QFileInfo.__ne__(QFileInfo fileinfo)'''
        return bool()
    def __eq__(self, fileinfo):
        '''bool QFileInfo.__eq__(QFileInfo fileinfo)'''
        return bool()


class QFileSystemWatcher(QObject):
    """"""
    def __init__(self, parent = None):
        '''void QFileSystemWatcher.__init__(QObject parent = None)'''
    def __init__(self, paths, parent = None):
        '''void QFileSystemWatcher.__init__(QStringList paths, QObject parent = None)'''
    fileChanged = pyqtSignal() # void fileChanged(const QString&) - signal
    directoryChanged = pyqtSignal() # void directoryChanged(const QString&) - signal
    def removePaths(self, files):
        '''void QFileSystemWatcher.removePaths(QStringList files)'''
    def removePath(self, file):
        '''void QFileSystemWatcher.removePath(QString file)'''
    def files(self):
        '''QStringList QFileSystemWatcher.files()'''
        return QStringList()
    def directories(self):
        '''QStringList QFileSystemWatcher.directories()'''
        return QStringList()
    def addPaths(self, files):
        '''void QFileSystemWatcher.addPaths(QStringList files)'''
    def addPath(self, file):
        '''void QFileSystemWatcher.addPath(QString file)'''


class QFinalState(QAbstractState):
    """"""
    def __init__(self, parent = None):
        '''void QFinalState.__init__(QState parent = None)'''
    def event(self, e):
        '''bool QFinalState.event(QEvent e)'''
        return bool()
    def onExit(self, event):
        '''void QFinalState.onExit(QEvent event)'''
    def onEntry(self, event):
        '''void QFinalState.onEntry(QEvent event)'''


class QFSFileEngine(QAbstractFileEngine):
    """"""
    def __init__(self):
        '''void QFSFileEngine.__init__()'''
    def __init__(self, file):
        '''void QFSFileEngine.__init__(QString file)'''
    def drives(self):
        '''static list-of-QFileInfo QFSFileEngine.drives()'''
        return [QFileInfo()]
    def tempPath(self):
        '''static QString QFSFileEngine.tempPath()'''
        return QString()
    def rootPath(self):
        '''static QString QFSFileEngine.rootPath()'''
        return QString()
    def homePath(self):
        '''static QString QFSFileEngine.homePath()'''
        return QString()
    def currentPath(self, fileName = QString()):
        '''static QString QFSFileEngine.currentPath(QString fileName = QString())'''
        return QString()
    def setCurrentPath(self, path):
        '''static bool QFSFileEngine.setCurrentPath(QString path)'''
        return bool()
    def write(self, data):
        '''int QFSFileEngine.write(str data)'''
        return int()
    def readLine(self, maxlen):
        '''str QFSFileEngine.readLine(int maxlen)'''
        return str()
    def read(self, maxlen):
        '''str QFSFileEngine.read(int maxlen)'''
        return str()
    def handle(self):
        '''int QFSFileEngine.handle()'''
        return int()
    def setFileName(self, file):
        '''void QFSFileEngine.setFileName(QString file)'''
    def fileTime(self, time):
        '''QDateTime QFSFileEngine.fileTime(QAbstractFileEngine.FileTime time)'''
        return QDateTime()
    def owner(self):
        '''QAbstractFileEngine.FileOwner QFSFileEngine.owner()'''
        return QAbstractFileEngine.FileOwner()
    def ownerId(self):
        '''QAbstractFileEngine.FileOwner QFSFileEngine.ownerId()'''
        return QAbstractFileEngine.FileOwner()
    def fileName(self, file):
        '''QString QFSFileEngine.fileName(QAbstractFileEngine.FileName file)'''
        return QString()
    def setPermissions(self, perms):
        '''bool QFSFileEngine.setPermissions(int perms)'''
        return bool()
    def fileFlags(self, type):
        '''QAbstractFileEngine.FileFlags QFSFileEngine.fileFlags(QAbstractFileEngine.FileFlags type)'''
        return QAbstractFileEngine.FileFlags()
    def entryList(self, filters, filterNames):
        '''QStringList QFSFileEngine.entryList(QDir.Filters filters, QStringList filterNames)'''
        return QStringList()
    def isRelativePath(self):
        '''bool QFSFileEngine.isRelativePath()'''
        return bool()
    def caseSensitive(self):
        '''bool QFSFileEngine.caseSensitive()'''
        return bool()
    def setSize(self, size):
        '''bool QFSFileEngine.setSize(int size)'''
        return bool()
    def rmdir(self, dirName, recurseParentDirectories):
        '''bool QFSFileEngine.rmdir(QString dirName, bool recurseParentDirectories)'''
        return bool()
    def mkdir(self, dirName, createParentDirectories):
        '''bool QFSFileEngine.mkdir(QString dirName, bool createParentDirectories)'''
        return bool()
    def link(self, newName):
        '''bool QFSFileEngine.link(QString newName)'''
        return bool()
    def rename(self, newName):
        '''bool QFSFileEngine.rename(QString newName)'''
        return bool()
    def copy(self, newName):
        '''bool QFSFileEngine.copy(QString newName)'''
        return bool()
    def remove(self):
        '''bool QFSFileEngine.remove()'''
        return bool()
    def isSequential(self):
        '''bool QFSFileEngine.isSequential()'''
        return bool()
    def seek(self):
        '''int QFSFileEngine.seek()'''
        return int()
    def pos(self):
        '''int QFSFileEngine.pos()'''
        return int()
    def size(self):
        '''int QFSFileEngine.size()'''
        return int()
    def flush(self):
        '''bool QFSFileEngine.flush()'''
        return bool()
    def close(self):
        '''bool QFSFileEngine.close()'''
        return bool()
    def open(self, openMode):
        '''bool QFSFileEngine.open(QIODevice.OpenMode openMode)'''
        return bool()
    def open(self, openMode, fd, handleFlags):
        '''bool QFSFileEngine.open(QIODevice.OpenMode openMode, int fd, QFile.FileHandleFlags handleFlags)'''
        return bool()
    def open(self, flags, fd):
        '''bool QFSFileEngine.open(QIODevice.OpenMode flags, int fd)'''
        return bool()


class QHistoryState(QAbstractState):
    """"""
    # Enum QHistoryState.HistoryType
    ShallowHistory = 0
    DeepHistory = 0

    def __init__(self, parent = None):
        '''void QHistoryState.__init__(QState parent = None)'''
    def __init__(self, type, parent = None):
        '''void QHistoryState.__init__(QHistoryState.HistoryType type, QState parent = None)'''
    def event(self, e):
        '''bool QHistoryState.event(QEvent e)'''
        return bool()
    def onExit(self, event):
        '''void QHistoryState.onExit(QEvent event)'''
    def onEntry(self, event):
        '''void QHistoryState.onEntry(QEvent event)'''
    def setHistoryType(self, type):
        '''void QHistoryState.setHistoryType(QHistoryState.HistoryType type)'''
    def historyType(self):
        '''QHistoryState.HistoryType QHistoryState.historyType()'''
        return QHistoryState.HistoryType()
    def setDefaultState(self, state):
        '''void QHistoryState.setDefaultState(QAbstractState state)'''
    def defaultState(self):
        '''QAbstractState QHistoryState.defaultState()'''
        return QAbstractState()


class QLibraryInfo():
    """"""
    # Enum QLibraryInfo.LibraryLocation
    PrefixPath = 0
    DocumentationPath = 0
    HeadersPath = 0
    LibrariesPath = 0
    BinariesPath = 0
    PluginsPath = 0
    DataPath = 0
    TranslationsPath = 0
    SettingsPath = 0
    DemosPath = 0
    ExamplesPath = 0
    ImportsPath = 0

    def __init__(self):
        '''QLibraryInfo QLibraryInfo.__init__()'''
        return QLibraryInfo()
    def buildDate(self):
        '''static QDate QLibraryInfo.buildDate()'''
        return QDate()
    def location(self):
        '''static QLibraryInfo.LibraryLocation QLibraryInfo.location()'''
        return QLibraryInfo.LibraryLocation()
    def buildKey(self):
        '''static QString QLibraryInfo.buildKey()'''
        return QString()
    def licensedProducts(self):
        '''static QString QLibraryInfo.licensedProducts()'''
        return QString()
    def licensee(self):
        '''static QString QLibraryInfo.licensee()'''
        return QString()


class QLine():
    """"""
    def __init__(self):
        '''void QLine.__init__()'''
    def __init__(self, pt1_, pt2_):
        '''void QLine.__init__(QPoint pt1_, QPoint pt2_)'''
    def __init__(self, x1pos, y1pos, x2pos, y2pos):
        '''void QLine.__init__(int x1pos, int y1pos, int x2pos, int y2pos)'''
    def __init__(self):
        '''QLine QLine.__init__()'''
        return QLine()
    def setLine(self, aX1, aY1, aX2, aY2):
        '''void QLine.setLine(int aX1, int aY1, int aX2, int aY2)'''
    def setPoints(self, aP1, aP2):
        '''void QLine.setPoints(QPoint aP1, QPoint aP2)'''
    def setP2(self, aP2):
        '''void QLine.setP2(QPoint aP2)'''
    def setP1(self, aP1):
        '''void QLine.setP1(QPoint aP1)'''
    def translated(self, p):
        '''QLine QLine.translated(QPoint p)'''
        return QLine()
    def translated(self, adx, ady):
        '''QLine QLine.translated(int adx, int ady)'''
        return QLine()
    def __eq__(self, d):
        '''bool QLine.__eq__(QLine d)'''
        return bool()
    def translate(self, point):
        '''void QLine.translate(QPoint point)'''
    def translate(self, adx, ady):
        '''void QLine.translate(int adx, int ady)'''
    def dy(self):
        '''int QLine.dy()'''
        return int()
    def dx(self):
        '''int QLine.dx()'''
        return int()
    def p2(self):
        '''QPoint QLine.p2()'''
        return QPoint()
    def p1(self):
        '''QPoint QLine.p1()'''
        return QPoint()
    def y2(self):
        '''int QLine.y2()'''
        return int()
    def x2(self):
        '''int QLine.x2()'''
        return int()
    def y1(self):
        '''int QLine.y1()'''
        return int()
    def x1(self):
        '''int QLine.x1()'''
        return int()
    def __bool__(self):
        '''int QLine.__bool__()'''
        return int()
    def isNull(self):
        '''bool QLine.isNull()'''
        return bool()
    def __repr__(self):
        '''str QLine.__repr__()'''
        return str()
    def __ne__(self, d):
        '''bool QLine.__ne__(QLine d)'''
        return bool()


class QLineF():
    """"""
    # Enum QLineF.IntersectType
    NoIntersection = 0
    BoundedIntersection = 0
    UnboundedIntersection = 0

    def __init__(self, line):
        '''void QLineF.__init__(QLine line)'''
    def __init__(self):
        '''void QLineF.__init__()'''
    def __init__(self, apt1, apt2):
        '''void QLineF.__init__(QPointF apt1, QPointF apt2)'''
    def __init__(self, x1pos, y1pos, x2pos, y2pos):
        '''void QLineF.__init__(float x1pos, float y1pos, float x2pos, float y2pos)'''
    def __init__(self):
        '''QLineF QLineF.__init__()'''
        return QLineF()
    def setLine(self, aX1, aY1, aX2, aY2):
        '''void QLineF.setLine(float aX1, float aY1, float aX2, float aY2)'''
    def setPoints(self, aP1, aP2):
        '''void QLineF.setPoints(QPointF aP1, QPointF aP2)'''
    def setP2(self, aP2):
        '''void QLineF.setP2(QPointF aP2)'''
    def setP1(self, aP1):
        '''void QLineF.setP1(QPointF aP1)'''
    def translated(self, p):
        '''QLineF QLineF.translated(QPointF p)'''
        return QLineF()
    def translated(self, adx, ady):
        '''QLineF QLineF.translated(float adx, float ady)'''
        return QLineF()
    def angleTo(self, l):
        '''float QLineF.angleTo(QLineF l)'''
        return float()
    def setAngle(self, angle):
        '''void QLineF.setAngle(float angle)'''
    def fromPolar(self, length, angle):
        '''static QLineF QLineF.fromPolar(float length, float angle)'''
        return QLineF()
    def __eq__(self, d):
        '''bool QLineF.__eq__(QLineF d)'''
        return bool()
    def toLine(self):
        '''QLine QLineF.toLine()'''
        return QLine()
    def pointAt(self, t):
        '''QPointF QLineF.pointAt(float t)'''
        return QPointF()
    def setLength(self, len):
        '''void QLineF.setLength(float len)'''
    def translate(self, point):
        '''void QLineF.translate(QPointF point)'''
    def translate(self, adx, ady):
        '''void QLineF.translate(float adx, float ady)'''
    def normalVector(self):
        '''QLineF QLineF.normalVector()'''
        return QLineF()
    def dy(self):
        '''float QLineF.dy()'''
        return float()
    def dx(self):
        '''float QLineF.dx()'''
        return float()
    def p2(self):
        '''QPointF QLineF.p2()'''
        return QPointF()
    def p1(self):
        '''QPointF QLineF.p1()'''
        return QPointF()
    def y2(self):
        '''float QLineF.y2()'''
        return float()
    def x2(self):
        '''float QLineF.x2()'''
        return float()
    def y1(self):
        '''float QLineF.y1()'''
        return float()
    def x1(self):
        '''float QLineF.x1()'''
        return float()
    def __repr__(self):
        '''str QLineF.__repr__()'''
        return str()
    def __ne__(self, d):
        '''bool QLineF.__ne__(QLineF d)'''
        return bool()
    def angle(self, l):
        '''float QLineF.angle(QLineF l)'''
        return float()
    def angle(self):
        '''float QLineF.angle()'''
        return float()
    def intersect(self, l, intersectionPoint):
        '''QLineF.IntersectType QLineF.intersect(QLineF l, QPointF intersectionPoint)'''
        return QLineF.IntersectType()
    def unitVector(self):
        '''QLineF QLineF.unitVector()'''
        return QLineF()
    def length(self):
        '''float QLineF.length()'''
        return float()
    def __bool__(self):
        '''int QLineF.__bool__()'''
        return int()
    def isNull(self):
        '''bool QLineF.isNull()'''
        return bool()


class QLibrary(QObject):
    """"""
    # Enum QLibrary.LoadHint
    ResolveAllSymbolsHint = 0
    ExportExternalSymbolsHint = 0
    LoadArchiveMemberHint = 0

    def __init__(self, parent = None):
        '''void QLibrary.__init__(QObject parent = None)'''
    def __init__(self, fileName, parent = None):
        '''void QLibrary.__init__(QString fileName, QObject parent = None)'''
    def __init__(self, fileName, verNum, parent = None):
        '''void QLibrary.__init__(QString fileName, int verNum, QObject parent = None)'''
    def __init__(self, fileName, version, parent = None):
        '''void QLibrary.__init__(QString fileName, QString version, QObject parent = None)'''
    def setLoadHints(self, hints):
        '''void QLibrary.setLoadHints(QLibrary.LoadHints hints)'''
    def setFileNameAndVersion(self, fileName, verNum):
        '''void QLibrary.setFileNameAndVersion(QString fileName, int verNum)'''
    def setFileNameAndVersion(self, fileName, version):
        '''void QLibrary.setFileNameAndVersion(QString fileName, QString version)'''
    def setFileName(self, fileName):
        '''void QLibrary.setFileName(QString fileName)'''
    def isLibrary(self, fileName):
        '''static bool QLibrary.isLibrary(QString fileName)'''
        return bool()
    def unload(self):
        '''bool QLibrary.unload()'''
        return bool()
    def resolve(self, symbol):
        '''sip.voidptr QLibrary.resolve(str symbol)'''
        return sip.voidptr()
    def resolve(self, fileName, symbol):
        '''static sip.voidptr QLibrary.resolve(QString fileName, str symbol)'''
        return sip.voidptr()
    def resolve(self, fileName, verNum, symbol):
        '''static sip.voidptr QLibrary.resolve(QString fileName, int verNum, str symbol)'''
        return sip.voidptr()
    def resolve(self, fileName, version, symbol):
        '''static sip.voidptr QLibrary.resolve(QString fileName, QString version, str symbol)'''
        return sip.voidptr()
    def loadHints(self):
        '''QLibrary.LoadHints QLibrary.loadHints()'''
        return QLibrary.LoadHints()
    def load(self):
        '''bool QLibrary.load()'''
        return bool()
    def isLoaded(self):
        '''bool QLibrary.isLoaded()'''
        return bool()
    def fileName(self):
        '''QString QLibrary.fileName()'''
        return QString()
    def errorString(self):
        '''QString QLibrary.errorString()'''
        return QString()
    class LoadHints():
        """"""
        def __init__(self):
            '''QLibrary.LoadHints QLibrary.LoadHints.__init__()'''
            return QLibrary.LoadHints()
        def __init__(self):
            '''int QLibrary.LoadHints.__init__()'''
            return int()
        def __init__(self):
            '''void QLibrary.LoadHints.__init__()'''
        def __bool__(self):
            '''int QLibrary.LoadHints.__bool__()'''
            return int()
        def __ne__(self, f):
            '''bool QLibrary.LoadHints.__ne__(QLibrary.LoadHints f)'''
            return bool()
        def __eq__(self, f):
            '''bool QLibrary.LoadHints.__eq__(QLibrary.LoadHints f)'''
            return bool()
        def __invert__(self):
            '''QLibrary.LoadHints QLibrary.LoadHints.__invert__()'''
            return QLibrary.LoadHints()
        def __and__(self, mask):
            '''QLibrary.LoadHints QLibrary.LoadHints.__and__(int mask)'''
            return QLibrary.LoadHints()
        def __xor__(self, f):
            '''QLibrary.LoadHints QLibrary.LoadHints.__xor__(QLibrary.LoadHints f)'''
            return QLibrary.LoadHints()
        def __xor__(self, f):
            '''QLibrary.LoadHints QLibrary.LoadHints.__xor__(int f)'''
            return QLibrary.LoadHints()
        def __or__(self, f):
            '''QLibrary.LoadHints QLibrary.LoadHints.__or__(QLibrary.LoadHints f)'''
            return QLibrary.LoadHints()
        def __or__(self, f):
            '''QLibrary.LoadHints QLibrary.LoadHints.__or__(int f)'''
            return QLibrary.LoadHints()
        def __int__(self):
            '''int QLibrary.LoadHints.__int__()'''
            return int()
        def __ixor__(self, f):
            '''QLibrary.LoadHints QLibrary.LoadHints.__ixor__(QLibrary.LoadHints f)'''
            return QLibrary.LoadHints()
        def __ior__(self, f):
            '''QLibrary.LoadHints QLibrary.LoadHints.__ior__(QLibrary.LoadHints f)'''
            return QLibrary.LoadHints()
        def __iand__(self, mask):
            '''QLibrary.LoadHints QLibrary.LoadHints.__iand__(int mask)'''
            return QLibrary.LoadHints()


class QLocale():
    """"""
    # Enum QLocale.QuotationStyle
    StandardQuotation = 0
    AlternateQuotation = 0

    # Enum QLocale.CurrencySymbolFormat
    CurrencyIsoCode = 0
    CurrencySymbol = 0
    CurrencyDisplayName = 0

    # Enum QLocale.Script
    AnyScript = 0
    ArabicScript = 0
    CyrillicScript = 0
    DeseretScript = 0
    GurmukhiScript = 0
    SimplifiedHanScript = 0
    TraditionalHanScript = 0
    LatinScript = 0
    MongolianScript = 0
    TifinaghScript = 0
    SimplifiedChineseScript = 0
    TraditionalChineseScript = 0

    # Enum QLocale.MeasurementSystem
    MetricSystem = 0
    ImperialSystem = 0

    # Enum QLocale.FormatType
    LongFormat = 0
    ShortFormat = 0
    NarrowFormat = 0

    # Enum QLocale.NumberOption
    OmitGroupSeparator = 0
    RejectGroupSeparator = 0

    # Enum QLocale.Country
    AnyCountry = 0
    Afghanistan = 0
    Albania = 0
    Algeria = 0
    AmericanSamoa = 0
    Andorra = 0
    Angola = 0
    Anguilla = 0
    Antarctica = 0
    AntiguaAndBarbuda = 0
    Argentina = 0
    Armenia = 0
    Aruba = 0
    Australia = 0
    Austria = 0
    Azerbaijan = 0
    Bahamas = 0
    Bahrain = 0
    Bangladesh = 0
    Barbados = 0
    Belarus = 0
    Belgium = 0
    Belize = 0
    Benin = 0
    Bermuda = 0
    Bhutan = 0
    Bolivia = 0
    BosniaAndHerzegowina = 0
    Botswana = 0
    BouvetIsland = 0
    Brazil = 0
    BritishIndianOceanTerritory = 0
    BruneiDarussalam = 0
    Bulgaria = 0
    BurkinaFaso = 0
    Burundi = 0
    Cambodia = 0
    Cameroon = 0
    Canada = 0
    CapeVerde = 0
    CaymanIslands = 0
    CentralAfricanRepublic = 0
    Chad = 0
    Chile = 0
    China = 0
    ChristmasIsland = 0
    CocosIslands = 0
    Colombia = 0
    Comoros = 0
    DemocraticRepublicOfCongo = 0
    PeoplesRepublicOfCongo = 0
    CookIslands = 0
    CostaRica = 0
    IvoryCoast = 0
    Croatia = 0
    Cuba = 0
    Cyprus = 0
    CzechRepublic = 0
    Denmark = 0
    Djibouti = 0
    Dominica = 0
    DominicanRepublic = 0
    EastTimor = 0
    Ecuador = 0
    Egypt = 0
    ElSalvador = 0
    EquatorialGuinea = 0
    Eritrea = 0
    Estonia = 0
    Ethiopia = 0
    FalklandIslands = 0
    FaroeIslands = 0
    FijiCountry = 0
    Finland = 0
    France = 0
    MetropolitanFrance = 0
    FrenchGuiana = 0
    FrenchPolynesia = 0
    FrenchSouthernTerritories = 0
    Gabon = 0
    Gambia = 0
    Georgia = 0
    Germany = 0
    Ghana = 0
    Gibraltar = 0
    Greece = 0
    Greenland = 0
    Grenada = 0
    Guadeloupe = 0
    Guam = 0
    Guatemala = 0
    Guinea = 0
    GuineaBissau = 0
    Guyana = 0
    Haiti = 0
    HeardAndMcDonaldIslands = 0
    Honduras = 0
    HongKong = 0
    Hungary = 0
    Iceland = 0
    India = 0
    Indonesia = 0
    Iran = 0
    Iraq = 0
    Ireland = 0
    Israel = 0
    Italy = 0
    Jamaica = 0
    Japan = 0
    Jordan = 0
    Kazakhstan = 0
    Kenya = 0
    Kiribati = 0
    DemocraticRepublicOfKorea = 0
    RepublicOfKorea = 0
    Kuwait = 0
    Kyrgyzstan = 0
    Lao = 0
    Latvia = 0
    Lebanon = 0
    Lesotho = 0
    Liberia = 0
    LibyanArabJamahiriya = 0
    Liechtenstein = 0
    Lithuania = 0
    Luxembourg = 0
    Macau = 0
    Macedonia = 0
    Madagascar = 0
    Malawi = 0
    Malaysia = 0
    Maldives = 0
    Mali = 0
    Malta = 0
    MarshallIslands = 0
    Martinique = 0
    Mauritania = 0
    Mauritius = 0
    Mayotte = 0
    Mexico = 0
    Micronesia = 0
    Moldova = 0
    Monaco = 0
    Mongolia = 0
    Montserrat = 0
    Morocco = 0
    Mozambique = 0
    Myanmar = 0
    Namibia = 0
    NauruCountry = 0
    Nepal = 0
    Netherlands = 0
    NetherlandsAntilles = 0
    NewCaledonia = 0
    NewZealand = 0
    Nicaragua = 0
    Niger = 0
    Nigeria = 0
    Niue = 0
    NorfolkIsland = 0
    NorthernMarianaIslands = 0
    Norway = 0
    Oman = 0
    Pakistan = 0
    Palau = 0
    PalestinianTerritory = 0
    Panama = 0
    PapuaNewGuinea = 0
    Paraguay = 0
    Peru = 0
    Philippines = 0
    Pitcairn = 0
    Poland = 0
    Portugal = 0
    PuertoRico = 0
    Qatar = 0
    Reunion = 0
    Romania = 0
    RussianFederation = 0
    Rwanda = 0
    SaintKittsAndNevis = 0
    StLucia = 0
    StVincentAndTheGrenadines = 0
    Samoa = 0
    SanMarino = 0
    SaoTomeAndPrincipe = 0
    SaudiArabia = 0
    Senegal = 0
    Seychelles = 0
    SierraLeone = 0
    Singapore = 0
    Slovakia = 0
    Slovenia = 0
    SolomonIslands = 0
    Somalia = 0
    SouthAfrica = 0
    SouthGeorgiaAndTheSouthSandwichIslands = 0
    Spain = 0
    SriLanka = 0
    StHelena = 0
    StPierreAndMiquelon = 0
    Sudan = 0
    Suriname = 0
    SvalbardAndJanMayenIslands = 0
    Swaziland = 0
    Sweden = 0
    Switzerland = 0
    SyrianArabRepublic = 0
    Taiwan = 0
    Tajikistan = 0
    Tanzania = 0
    Thailand = 0
    Togo = 0
    Tokelau = 0
    TongaCountry = 0
    TrinidadAndTobago = 0
    Tunisia = 0
    Turkey = 0
    Turkmenistan = 0
    TurksAndCaicosIslands = 0
    Tuvalu = 0
    Uganda = 0
    Ukraine = 0
    UnitedArabEmirates = 0
    UnitedKingdom = 0
    UnitedStates = 0
    UnitedStatesMinorOutlyingIslands = 0
    Uruguay = 0
    Uzbekistan = 0
    Vanuatu = 0
    VaticanCityState = 0
    Venezuela = 0
    VietNam = 0
    BritishVirginIslands = 0
    USVirginIslands = 0
    WallisAndFutunaIslands = 0
    WesternSahara = 0
    Yemen = 0
    Yugoslavia = 0
    Zambia = 0
    Zimbabwe = 0
    SerbiaAndMontenegro = 0
    Montenegro = 0
    Serbia = 0
    SaintBarthelemy = 0
    SaintMartin = 0
    LatinAmericaAndTheCaribbean = 0
    LastCountry = 0

    # Enum QLocale.Language
    C = 0
    Abkhazian = 0
    Afan = 0
    Afar = 0
    Afrikaans = 0
    Albanian = 0
    Amharic = 0
    Arabic = 0
    Armenian = 0
    Assamese = 0
    Aymara = 0
    Azerbaijani = 0
    Bashkir = 0
    Basque = 0
    Bengali = 0
    Bhutani = 0
    Bihari = 0
    Bislama = 0
    Breton = 0
    Bulgarian = 0
    Burmese = 0
    Byelorussian = 0
    Cambodian = 0
    Catalan = 0
    Chinese = 0
    Corsican = 0
    Croatian = 0
    Czech = 0
    Danish = 0
    Dutch = 0
    English = 0
    Esperanto = 0
    Estonian = 0
    Faroese = 0
    FijiLanguage = 0
    Finnish = 0
    French = 0
    Frisian = 0
    Gaelic = 0
    Galician = 0
    Georgian = 0
    German = 0
    Greek = 0
    Greenlandic = 0
    Guarani = 0
    Gujarati = 0
    Hausa = 0
    Hebrew = 0
    Hindi = 0
    Hungarian = 0
    Icelandic = 0
    Indonesian = 0
    Interlingua = 0
    Interlingue = 0
    Inuktitut = 0
    Inupiak = 0
    Irish = 0
    Italian = 0
    Japanese = 0
    Javanese = 0
    Kannada = 0
    Kashmiri = 0
    Kazakh = 0
    Kinyarwanda = 0
    Kirghiz = 0
    Korean = 0
    Kurdish = 0
    Kurundi = 0
    Laothian = 0
    Latin = 0
    Latvian = 0
    Lingala = 0
    Lithuanian = 0
    Macedonian = 0
    Malagasy = 0
    Malay = 0
    Malayalam = 0
    Maltese = 0
    Maori = 0
    Marathi = 0
    Moldavian = 0
    Mongolian = 0
    NauruLanguage = 0
    Nepali = 0
    Norwegian = 0
    Occitan = 0
    Oriya = 0
    Pashto = 0
    Persian = 0
    Polish = 0
    Portuguese = 0
    Punjabi = 0
    Quechua = 0
    RhaetoRomance = 0
    Romanian = 0
    Russian = 0
    Samoan = 0
    Sangho = 0
    Sanskrit = 0
    Serbian = 0
    SerboCroatian = 0
    Sesotho = 0
    Setswana = 0
    Shona = 0
    Sindhi = 0
    Singhalese = 0
    Siswati = 0
    Slovak = 0
    Slovenian = 0
    Somali = 0
    Spanish = 0
    Sundanese = 0
    Swahili = 0
    Swedish = 0
    Tagalog = 0
    Tajik = 0
    Tamil = 0
    Tatar = 0
    Telugu = 0
    Thai = 0
    Tibetan = 0
    Tigrinya = 0
    TongaLanguage = 0
    Tsonga = 0
    Turkish = 0
    Turkmen = 0
    Twi = 0
    Uigur = 0
    Ukrainian = 0
    Urdu = 0
    Uzbek = 0
    Vietnamese = 0
    Volapuk = 0
    Welsh = 0
    Wolof = 0
    Xhosa = 0
    Yiddish = 0
    Yoruba = 0
    Zhuang = 0
    Zulu = 0
    Nynorsk = 0
    Bosnian = 0
    Divehi = 0
    Manx = 0
    Cornish = 0
    LastLanguage = 0
    NorwegianBokmal = 0
    NorwegianNynorsk = 0
    Akan = 0
    Konkani = 0
    Ga = 0
    Igbo = 0
    Kamba = 0
    Syriac = 0
    Blin = 0
    Geez = 0
    Koro = 0
    Sidamo = 0
    Atsam = 0
    Tigre = 0
    Jju = 0
    Friulian = 0
    Venda = 0
    Ewe = 0
    Walamo = 0
    Hawaiian = 0
    Tyap = 0
    Chewa = 0
    Filipino = 0
    SwissGerman = 0
    SichuanYi = 0
    Kpelle = 0
    LowGerman = 0
    SouthNdebele = 0
    NorthernSotho = 0
    NorthernSami = 0
    Taroko = 0
    Gusii = 0
    Taita = 0
    Fulah = 0
    Kikuyu = 0
    Samburu = 0
    Sena = 0
    NorthNdebele = 0
    Rombo = 0
    Tachelhit = 0
    Kabyle = 0
    Nyankole = 0
    Bena = 0
    Vunjo = 0
    Bambara = 0
    Embu = 0
    Cherokee = 0
    Morisyen = 0
    Makonde = 0
    Langi = 0
    Ganda = 0
    Bemba = 0
    Kabuverdianu = 0
    Meru = 0
    Kalenjin = 0
    Nama = 0
    Machame = 0
    Colognian = 0
    Masai = 0
    Soga = 0
    Luyia = 0
    Asu = 0
    Teso = 0
    Saho = 0
    KoyraChiini = 0
    Rwa = 0
    Luo = 0
    Chiga = 0
    CentralMoroccoTamazight = 0
    KoyraboroSenni = 0
    Shambala = 0
    AnyLanguage = 0

    def __init__(self):
        '''void QLocale.__init__()'''
    def __init__(self, name):
        '''void QLocale.__init__(QString name)'''
    def __init__(self, language, country = QLocale.AnyCountry):
        '''void QLocale.__init__(QLocale.Language language, QLocale.Country country = QLocale.AnyCountry)'''
    def __init__(self, other):
        '''void QLocale.__init__(QLocale other)'''
    def __init__(self, language, script, country):
        '''void QLocale.__init__(QLocale.Language language, QLocale.Script script, QLocale.Country country)'''
    def createSeparatedList(self, list):
        '''QString QLocale.createSeparatedList(QStringList list)'''
        return QString()
    def quoteString(self, str, style = QLocale.StandardQuotation):
        '''QString QLocale.quoteString(QString str, QLocale.QuotationStyle style = QLocale.StandardQuotation)'''
        return QString()
    def matchingLocales(self, language, script, country):
        '''static list-of-QLocale QLocale.matchingLocales(QLocale.Language language, QLocale.Script script, QLocale.Country country)'''
        return [QLocale()]
    def scriptToString(self, script):
        '''static QString QLocale.scriptToString(QLocale.Script script)'''
        return QString()
    def uiLanguages(self):
        '''QStringList QLocale.uiLanguages()'''
        return QStringList()
    def toCurrencyString(self, value, symbol = QString()):
        '''QString QLocale.toCurrencyString(int value, QString symbol = QString())'''
        return QString()
    def toCurrencyString(self, value, symbol = QString()):
        '''QString QLocale.toCurrencyString(float value, QString symbol = QString())'''
        return QString()
    def toCurrencyString(self, value, symbol = QString()):
        '''QString QLocale.toCurrencyString(int value, QString symbol = QString())'''
        return QString()
    def toCurrencyString(self, value, symbol = QString()):
        '''QString QLocale.toCurrencyString(int value, QString symbol = QString())'''
        return QString()
    def currencySymbol(self, format = QLocale.CurrencySymbol):
        '''QString QLocale.currencySymbol(QLocale.CurrencySymbolFormat format = QLocale.CurrencySymbol)'''
        return QString()
    def toLower(self, str):
        '''QString QLocale.toLower(QString str)'''
        return QString()
    def toUpper(self, str):
        '''QString QLocale.toUpper(QString str)'''
        return QString()
    def weekdays(self):
        '''list-of-Qt.DayOfWeek QLocale.weekdays()'''
        return [Qt.DayOfWeek()]
    def firstDayOfWeek(self):
        '''Qt.DayOfWeek QLocale.firstDayOfWeek()'''
        return Qt.DayOfWeek()
    def nativeCountryName(self):
        '''QString QLocale.nativeCountryName()'''
        return QString()
    def nativeLanguageName(self):
        '''QString QLocale.nativeLanguageName()'''
        return QString()
    def bcp47Name(self):
        '''QString QLocale.bcp47Name()'''
        return QString()
    def script(self):
        '''QLocale.Script QLocale.script()'''
        return QLocale.Script()
    def textDirection(self):
        '''Qt.LayoutDirection QLocale.textDirection()'''
        return Qt.LayoutDirection()
    def pmText(self):
        '''QString QLocale.pmText()'''
        return QString()
    def amText(self):
        '''QString QLocale.amText()'''
        return QString()
    def standaloneDayName(self, format = QLocale.LongFormat):
        '''int QLocale.standaloneDayName(QLocale.FormatType format = QLocale.LongFormat)'''
        return int()
    def standaloneMonthName(self, format = QLocale.LongFormat):
        '''int QLocale.standaloneMonthName(QLocale.FormatType format = QLocale.LongFormat)'''
        return int()
    def positiveSign(self):
        '''QChar QLocale.positiveSign()'''
        return QChar()
    def measurementSystem(self):
        '''QLocale.MeasurementSystem QLocale.measurementSystem()'''
        return QLocale.MeasurementSystem()
    def countriesForLanguage(self, lang):
        '''static list-of-QLocale.Country QLocale.countriesForLanguage(QLocale.Language lang)'''
        return [QLocale.Country()]
    def numberOptions(self):
        '''QLocale.NumberOptions QLocale.numberOptions()'''
        return QLocale.NumberOptions()
    def setNumberOptions(self, options):
        '''void QLocale.setNumberOptions(QLocale.NumberOptions options)'''
    def dayName(self, format = QLocale.LongFormat):
        '''int QLocale.dayName(QLocale.FormatType format = QLocale.LongFormat)'''
        return int()
    def monthName(self, format = QLocale.LongFormat):
        '''int QLocale.monthName(QLocale.FormatType format = QLocale.LongFormat)'''
        return int()
    def exponential(self):
        '''QChar QLocale.exponential()'''
        return QChar()
    def negativeSign(self):
        '''QChar QLocale.negativeSign()'''
        return QChar()
    def zeroDigit(self):
        '''QChar QLocale.zeroDigit()'''
        return QChar()
    def percent(self):
        '''QChar QLocale.percent()'''
        return QChar()
    def groupSeparator(self):
        '''QChar QLocale.groupSeparator()'''
        return QChar()
    def decimalPoint(self):
        '''QChar QLocale.decimalPoint()'''
        return QChar()
    def toDateTime(self, string, format = QLocale.LongFormat):
        '''QDateTime QLocale.toDateTime(QString string, QLocale.FormatType format = QLocale.LongFormat)'''
        return QDateTime()
    def toDateTime(self, string, format):
        '''QDateTime QLocale.toDateTime(QString string, QString format)'''
        return QDateTime()
    def toTime(self, string, format = QLocale.LongFormat):
        '''QTime QLocale.toTime(QString string, QLocale.FormatType format = QLocale.LongFormat)'''
        return QTime()
    def toTime(self, string, format):
        '''QTime QLocale.toTime(QString string, QString format)'''
        return QTime()
    def toDate(self, string, format = QLocale.LongFormat):
        '''QDate QLocale.toDate(QString string, QLocale.FormatType format = QLocale.LongFormat)'''
        return QDate()
    def toDate(self, string, format):
        '''QDate QLocale.toDate(QString string, QString format)'''
        return QDate()
    def dateTimeFormat(self, format = QLocale.LongFormat):
        '''QString QLocale.dateTimeFormat(QLocale.FormatType format = QLocale.LongFormat)'''
        return QString()
    def timeFormat(self, format = QLocale.LongFormat):
        '''QString QLocale.timeFormat(QLocale.FormatType format = QLocale.LongFormat)'''
        return QString()
    def dateFormat(self, format = QLocale.LongFormat):
        '''QString QLocale.dateFormat(QLocale.FormatType format = QLocale.LongFormat)'''
        return QString()
    def system(self):
        '''static QLocale QLocale.system()'''
        return QLocale()
    def c(self):
        '''static QLocale QLocale.c()'''
        return QLocale()
    def setDefault(self, locale):
        '''static void QLocale.setDefault(QLocale locale)'''
    def countryToString(self, country):
        '''static QString QLocale.countryToString(QLocale.Country country)'''
        return QString()
    def languageToString(self, language):
        '''static QString QLocale.languageToString(QLocale.Language language)'''
        return QString()
    def __ne__(self, other):
        '''bool QLocale.__ne__(QLocale other)'''
        return bool()
    def __eq__(self, other):
        '''bool QLocale.__eq__(QLocale other)'''
        return bool()
    def toString(self, i):
        '''QString QLocale.toString(int i)'''
        return QString()
    def toString(self, i, format = 'g', precision = 6):
        '''QString QLocale.toString(float i, str format = 'g', int precision = 6)'''
        return QString()
    def toString(self, i):
        '''QString QLocale.toString(int i)'''
        return QString()
    def toString(self, i):
        '''QString QLocale.toString(int i)'''
        return QString()
    def toString(self, dateTime, format):
        '''QString QLocale.toString(QDateTime dateTime, QString format)'''
        return QString()
    def toString(self, dateTime, format = QLocale.LongFormat):
        '''QString QLocale.toString(QDateTime dateTime, QLocale.FormatType format = QLocale.LongFormat)'''
        return QString()
    def toString(self, date, formatStr):
        '''QString QLocale.toString(QDate date, QString formatStr)'''
        return QString()
    def toString(self, date, format = QLocale.LongFormat):
        '''QString QLocale.toString(QDate date, QLocale.FormatType format = QLocale.LongFormat)'''
        return QString()
    def toString(self, time, formatStr):
        '''QString QLocale.toString(QTime time, QString formatStr)'''
        return QString()
    def toString(self, time, format = QLocale.LongFormat):
        '''QString QLocale.toString(QTime time, QLocale.FormatType format = QLocale.LongFormat)'''
        return QString()
    def toDouble(self, s, ok):
        '''float QLocale.toDouble(QString s, bool ok)'''
        return float()
    def toFloat(self, s, ok):
        '''float QLocale.toFloat(QString s, bool ok)'''
        return float()
    def toULongLong(self, s, ok, base = 0):
        '''int QLocale.toULongLong(QString s, bool ok, int base = 0)'''
        return int()
    def toLongLong(self, s, ok, base = 0):
        '''int QLocale.toLongLong(QString s, bool ok, int base = 0)'''
        return int()
    def toUInt(self, s, ok, base = 0):
        '''int QLocale.toUInt(QString s, bool ok, int base = 0)'''
        return int()
    def toInt(self, s, ok, base = 0):
        '''int QLocale.toInt(QString s, bool ok, int base = 0)'''
        return int()
    def toUShort(self, s, ok, base = 0):
        '''int QLocale.toUShort(QString s, bool ok, int base = 0)'''
        return int()
    def toShort(self, s, ok, base = 0):
        '''int QLocale.toShort(QString s, bool ok, int base = 0)'''
        return int()
    def name(self):
        '''QString QLocale.name()'''
        return QString()
    def country(self):
        '''QLocale.Country QLocale.country()'''
        return QLocale.Country()
    def language(self):
        '''QLocale.Language QLocale.language()'''
        return QLocale.Language()
    class NumberOptions():
        """"""
        def __init__(self):
            '''QLocale.NumberOptions QLocale.NumberOptions.__init__()'''
            return QLocale.NumberOptions()
        def __init__(self):
            '''int QLocale.NumberOptions.__init__()'''
            return int()
        def __init__(self):
            '''void QLocale.NumberOptions.__init__()'''
        def __bool__(self):
            '''int QLocale.NumberOptions.__bool__()'''
            return int()
        def __ne__(self, f):
            '''bool QLocale.NumberOptions.__ne__(QLocale.NumberOptions f)'''
            return bool()
        def __eq__(self, f):
            '''bool QLocale.NumberOptions.__eq__(QLocale.NumberOptions f)'''
            return bool()
        def __invert__(self):
            '''QLocale.NumberOptions QLocale.NumberOptions.__invert__()'''
            return QLocale.NumberOptions()
        def __and__(self, mask):
            '''QLocale.NumberOptions QLocale.NumberOptions.__and__(int mask)'''
            return QLocale.NumberOptions()
        def __xor__(self, f):
            '''QLocale.NumberOptions QLocale.NumberOptions.__xor__(QLocale.NumberOptions f)'''
            return QLocale.NumberOptions()
        def __xor__(self, f):
            '''QLocale.NumberOptions QLocale.NumberOptions.__xor__(int f)'''
            return QLocale.NumberOptions()
        def __or__(self, f):
            '''QLocale.NumberOptions QLocale.NumberOptions.__or__(QLocale.NumberOptions f)'''
            return QLocale.NumberOptions()
        def __or__(self, f):
            '''QLocale.NumberOptions QLocale.NumberOptions.__or__(int f)'''
            return QLocale.NumberOptions()
        def __int__(self):
            '''int QLocale.NumberOptions.__int__()'''
            return int()
        def __ixor__(self, f):
            '''QLocale.NumberOptions QLocale.NumberOptions.__ixor__(QLocale.NumberOptions f)'''
            return QLocale.NumberOptions()
        def __ior__(self, f):
            '''QLocale.NumberOptions QLocale.NumberOptions.__ior__(QLocale.NumberOptions f)'''
            return QLocale.NumberOptions()
        def __iand__(self, mask):
            '''QLocale.NumberOptions QLocale.NumberOptions.__iand__(int mask)'''
            return QLocale.NumberOptions()


class QSystemLocale():
    """"""
    # Enum QSystemLocale.QueryType
    LanguageId = 0
    ScriptId = 0
    CountryId = 0
    DecimalPoint = 0
    GroupSeparator = 0
    ZeroDigit = 0
    NegativeSign = 0
    DateFormatLong = 0
    DateFormatShort = 0
    TimeFormatLong = 0
    TimeFormatShort = 0
    DayNameLong = 0
    DayNameShort = 0
    MonthNameLong = 0
    MonthNameShort = 0
    DateToStringLong = 0
    DateToStringShort = 0
    TimeToStringLong = 0
    TimeToStringShort = 0
    DateTimeFormatLong = 0
    DateTimeFormatShort = 0
    DateTimeToStringLong = 0
    DateTimeToStringShort = 0
    MeasurementSystem = 0
    PositiveSign = 0
    AMText = 0
    PMText = 0
    FirstDayOfWeek = 0
    Weekdays = 0
    CurrencySymbol = 0
    CurrencyToString = 0
    UILanguages = 0
    StringToStandardQuotation = 0
    StringToAlternateQuotation = 0
    ListToSeparatedString = 0
    LocaleChanged = 0
    NativeLanguageName = 0
    NativeCountryName = 0

    def __init__(self):
        '''void QSystemLocale.__init__()'''
    def __init__(self):
        '''QSystemLocale QSystemLocale.__init__()'''
        return QSystemLocale()
    def fallbackLocale(self):
        '''QLocale QSystemLocale.fallbackLocale()'''
        return QLocale()
    def query(self, type, in_):
        '''QVariant QSystemLocale.query(QSystemLocale.QueryType type, QVariant in)'''
        return QVariant()


class QMargins():
    """"""
    def __init__(self):
        '''void QMargins.__init__()'''
    def __init__(self, aleft, atop, aright, abottom):
        '''void QMargins.__init__(int aleft, int atop, int aright, int abottom)'''
    def __init__(self):
        '''QMargins QMargins.__init__()'''
        return QMargins()
    def __eq__(self, m2):
        '''bool QMargins.__eq__(QMargins m2)'''
        return bool()
    def __ne__(self, m2):
        '''bool QMargins.__ne__(QMargins m2)'''
        return bool()
    def setBottom(self, abottom):
        '''void QMargins.setBottom(int abottom)'''
    def setRight(self, aright):
        '''void QMargins.setRight(int aright)'''
    def setTop(self, atop):
        '''void QMargins.setTop(int atop)'''
    def setLeft(self, aleft):
        '''void QMargins.setLeft(int aleft)'''
    def bottom(self):
        '''int QMargins.bottom()'''
        return int()
    def right(self):
        '''int QMargins.right()'''
        return int()
    def top(self):
        '''int QMargins.top()'''
        return int()
    def left(self):
        '''int QMargins.left()'''
        return int()
    def isNull(self):
        '''bool QMargins.isNull()'''
        return bool()


class QMetaMethod():
    """"""
    # Enum QMetaMethod.MethodType
    Method = 0
    Signal = 0
    Slot = 0
    Constructor = 0

    # Enum QMetaMethod.Access
    Private = 0
    Protected = 0
    Public = 0

    def __init__(self):
        '''void QMetaMethod.__init__()'''
    def __init__(self):
        '''QMetaMethod QMetaMethod.__init__()'''
        return QMetaMethod()
    def methodIndex(self):
        '''int QMetaMethod.methodIndex()'''
        return int()
    def invoke(self, object, connectionType, returnValue, value0 = QGenericArgument(0,0), value1 = QGenericArgument(0,0), value2 = QGenericArgument(0,0), value3 = QGenericArgument(0,0), value4 = QGenericArgument(0,0), value5 = QGenericArgument(0,0), value6 = QGenericArgument(0,0), value7 = QGenericArgument(0,0), value8 = QGenericArgument(0,0), value9 = QGenericArgument(0,0)):
        '''object QMetaMethod.invoke(QObject object, Qt.ConnectionType connectionType, QGenericReturnArgument returnValue, QGenericArgument value0 = QGenericArgument(0,0), QGenericArgument value1 = QGenericArgument(0,0), QGenericArgument value2 = QGenericArgument(0,0), QGenericArgument value3 = QGenericArgument(0,0), QGenericArgument value4 = QGenericArgument(0,0), QGenericArgument value5 = QGenericArgument(0,0), QGenericArgument value6 = QGenericArgument(0,0), QGenericArgument value7 = QGenericArgument(0,0), QGenericArgument value8 = QGenericArgument(0,0), QGenericArgument value9 = QGenericArgument(0,0))'''
        return object()
    def invoke(self, object, returnValue, value0 = QGenericArgument(0,0), value1 = QGenericArgument(0,0), value2 = QGenericArgument(0,0), value3 = QGenericArgument(0,0), value4 = QGenericArgument(0,0), value5 = QGenericArgument(0,0), value6 = QGenericArgument(0,0), value7 = QGenericArgument(0,0), value8 = QGenericArgument(0,0), value9 = QGenericArgument(0,0)):
        '''object QMetaMethod.invoke(QObject object, QGenericReturnArgument returnValue, QGenericArgument value0 = QGenericArgument(0,0), QGenericArgument value1 = QGenericArgument(0,0), QGenericArgument value2 = QGenericArgument(0,0), QGenericArgument value3 = QGenericArgument(0,0), QGenericArgument value4 = QGenericArgument(0,0), QGenericArgument value5 = QGenericArgument(0,0), QGenericArgument value6 = QGenericArgument(0,0), QGenericArgument value7 = QGenericArgument(0,0), QGenericArgument value8 = QGenericArgument(0,0), QGenericArgument value9 = QGenericArgument(0,0))'''
        return object()
    def invoke(self, object, connectionType, value0 = QGenericArgument(0,0), value1 = QGenericArgument(0,0), value2 = QGenericArgument(0,0), value3 = QGenericArgument(0,0), value4 = QGenericArgument(0,0), value5 = QGenericArgument(0,0), value6 = QGenericArgument(0,0), value7 = QGenericArgument(0,0), value8 = QGenericArgument(0,0), value9 = QGenericArgument(0,0)):
        '''object QMetaMethod.invoke(QObject object, Qt.ConnectionType connectionType, QGenericArgument value0 = QGenericArgument(0,0), QGenericArgument value1 = QGenericArgument(0,0), QGenericArgument value2 = QGenericArgument(0,0), QGenericArgument value3 = QGenericArgument(0,0), QGenericArgument value4 = QGenericArgument(0,0), QGenericArgument value5 = QGenericArgument(0,0), QGenericArgument value6 = QGenericArgument(0,0), QGenericArgument value7 = QGenericArgument(0,0), QGenericArgument value8 = QGenericArgument(0,0), QGenericArgument value9 = QGenericArgument(0,0))'''
        return object()
    def invoke(self, object, value0 = QGenericArgument(0,0), value1 = QGenericArgument(0,0), value2 = QGenericArgument(0,0), value3 = QGenericArgument(0,0), value4 = QGenericArgument(0,0), value5 = QGenericArgument(0,0), value6 = QGenericArgument(0,0), value7 = QGenericArgument(0,0), value8 = QGenericArgument(0,0), value9 = QGenericArgument(0,0)):
        '''object QMetaMethod.invoke(QObject object, QGenericArgument value0 = QGenericArgument(0,0), QGenericArgument value1 = QGenericArgument(0,0), QGenericArgument value2 = QGenericArgument(0,0), QGenericArgument value3 = QGenericArgument(0,0), QGenericArgument value4 = QGenericArgument(0,0), QGenericArgument value5 = QGenericArgument(0,0), QGenericArgument value6 = QGenericArgument(0,0), QGenericArgument value7 = QGenericArgument(0,0), QGenericArgument value8 = QGenericArgument(0,0), QGenericArgument value9 = QGenericArgument(0,0))'''
        return object()
    def methodType(self):
        '''QMetaMethod.MethodType QMetaMethod.methodType()'''
        return QMetaMethod.MethodType()
    def access(self):
        '''QMetaMethod.Access QMetaMethod.access()'''
        return QMetaMethod.Access()
    def tag(self):
        '''str QMetaMethod.tag()'''
        return str()
    def parameterNames(self):
        '''list-of-QByteArray QMetaMethod.parameterNames()'''
        return [QByteArray()]
    def parameterTypes(self):
        '''list-of-QByteArray QMetaMethod.parameterTypes()'''
        return [QByteArray()]
    def typeName(self):
        '''str QMetaMethod.typeName()'''
        return str()
    def signature(self):
        '''str QMetaMethod.signature()'''
        return str()


class QMetaEnum():
    """"""
    def __init__(self):
        '''void QMetaEnum.__init__()'''
    def __init__(self):
        '''QMetaEnum QMetaEnum.__init__()'''
        return QMetaEnum()
    def isValid(self):
        '''bool QMetaEnum.isValid()'''
        return bool()
    def valueToKeys(self, value):
        '''QByteArray QMetaEnum.valueToKeys(int value)'''
        return QByteArray()
    def keysToValue(self, keys):
        '''int QMetaEnum.keysToValue(str keys)'''
        return int()
    def valueToKey(self, value):
        '''str QMetaEnum.valueToKey(int value)'''
        return str()
    def keyToValue(self, key):
        '''int QMetaEnum.keyToValue(str key)'''
        return int()
    def scope(self):
        '''str QMetaEnum.scope()'''
        return str()
    def value(self, index):
        '''int QMetaEnum.value(int index)'''
        return int()
    def key(self, index):
        '''str QMetaEnum.key(int index)'''
        return str()
    def keyCount(self):
        '''int QMetaEnum.keyCount()'''
        return int()
    def isFlag(self):
        '''bool QMetaEnum.isFlag()'''
        return bool()
    def name(self):
        '''str QMetaEnum.name()'''
        return str()


class QMetaProperty():
    """"""
    def __init__(self):
        '''void QMetaProperty.__init__()'''
    def __init__(self):
        '''QMetaProperty QMetaProperty.__init__()'''
        return QMetaProperty()
    def isFinal(self):
        '''bool QMetaProperty.isFinal()'''
        return bool()
    def isConstant(self):
        '''bool QMetaProperty.isConstant()'''
        return bool()
    def propertyIndex(self):
        '''int QMetaProperty.propertyIndex()'''
        return int()
    def notifySignalIndex(self):
        '''int QMetaProperty.notifySignalIndex()'''
        return int()
    def notifySignal(self):
        '''QMetaMethod QMetaProperty.notifySignal()'''
        return QMetaMethod()
    def hasNotifySignal(self):
        '''bool QMetaProperty.hasNotifySignal()'''
        return bool()
    def userType(self):
        '''int QMetaProperty.userType()'''
        return int()
    def isUser(self, object = None):
        '''bool QMetaProperty.isUser(QObject object = None)'''
        return bool()
    def isResettable(self):
        '''bool QMetaProperty.isResettable()'''
        return bool()
    def isValid(self):
        '''bool QMetaProperty.isValid()'''
        return bool()
    def hasStdCppSet(self):
        '''bool QMetaProperty.hasStdCppSet()'''
        return bool()
    def reset(self, obj):
        '''bool QMetaProperty.reset(QObject obj)'''
        return bool()
    def write(self, obj, value):
        '''bool QMetaProperty.write(QObject obj, QVariant value)'''
        return bool()
    def read(self, obj):
        '''QVariant QMetaProperty.read(QObject obj)'''
        return QVariant()
    def enumerator(self):
        '''QMetaEnum QMetaProperty.enumerator()'''
        return QMetaEnum()
    def isEnumType(self):
        '''bool QMetaProperty.isEnumType()'''
        return bool()
    def isFlagType(self):
        '''bool QMetaProperty.isFlagType()'''
        return bool()
    def isEditable(self, object = None):
        '''bool QMetaProperty.isEditable(QObject object = None)'''
        return bool()
    def isStored(self, object = None):
        '''bool QMetaProperty.isStored(QObject object = None)'''
        return bool()
    def isScriptable(self, object = None):
        '''bool QMetaProperty.isScriptable(QObject object = None)'''
        return bool()
    def isDesignable(self, object = None):
        '''bool QMetaProperty.isDesignable(QObject object = None)'''
        return bool()
    def isWritable(self):
        '''bool QMetaProperty.isWritable()'''
        return bool()
    def isReadable(self):
        '''bool QMetaProperty.isReadable()'''
        return bool()
    def type(self):
        '''Type QMetaProperty.type()'''
        return Type()
    def typeName(self):
        '''str QMetaProperty.typeName()'''
        return str()
    def name(self):
        '''str QMetaProperty.name()'''
        return str()


class QMetaClassInfo():
    """"""
    def __init__(self):
        '''void QMetaClassInfo.__init__()'''
    def __init__(self):
        '''QMetaClassInfo QMetaClassInfo.__init__()'''
        return QMetaClassInfo()
    def value(self):
        '''str QMetaClassInfo.value()'''
        return str()
    def name(self):
        '''str QMetaClassInfo.name()'''
        return str()


class QMetaType():
    """"""
    # Enum QMetaType.Type
    Void = 0
    Bool = 0
    Int = 0
    UInt = 0
    LongLong = 0
    ULongLong = 0
    Double = 0
    QChar = 0
    QVariantMap = 0
    QVariantList = 0
    QVariantHash = 0
    QString = 0
    QStringList = 0
    QByteArray = 0
    QBitArray = 0
    QDate = 0
    QTime = 0
    QDateTime = 0
    QUrl = 0
    QLocale = 0
    QRect = 0
    QRectF = 0
    QSize = 0
    QSizeF = 0
    QLine = 0
    QLineF = 0
    QPoint = 0
    QPointF = 0
    QRegExp = 0
    LastCoreType = 0
    FirstGuiType = 0
    QFont = 0
    QPixmap = 0
    QBrush = 0
    QColor = 0
    QPalette = 0
    QIcon = 0
    QImage = 0
    QPolygon = 0
    QRegion = 0
    QBitmap = 0
    QCursor = 0
    QSizePolicy = 0
    QKeySequence = 0
    QPen = 0
    QTextLength = 0
    QTextFormat = 0
    QMatrix = 0
    QTransform = 0
    VoidStar = 0
    Long = 0
    Short = 0
    Char = 0
    ULong = 0
    UShort = 0
    UChar = 0
    Float = 0
    QObjectStar = 0
    QWidgetStar = 0
    QMatrix4x4 = 0
    QVector2D = 0
    QVector3D = 0
    QVector4D = 0
    QQuaternion = 0
    QEasingCurve = 0
    QVariant = 0
    User = 0

    def __init__(self):
        '''void QMetaType.__init__()'''
    def __init__(self):
        '''QMetaType QMetaType.__init__()'''
        return QMetaType()
    def isRegistered(self, type):
        '''static bool QMetaType.isRegistered(int type)'''
        return bool()
    def typeName(self, type):
        '''static str QMetaType.typeName(int type)'''
        return str()
    def type(self, typeName):
        '''static int QMetaType.type(str typeName)'''
        return int()


class QMimeData(QObject):
    """"""
    def __init__(self):
        '''void QMimeData.__init__()'''
    def retrieveData(self, mimetype, preferredType):
        '''QVariant QMimeData.retrieveData(QString mimetype, Type preferredType)'''
        return QVariant()
    def removeFormat(self, mimetype):
        '''void QMimeData.removeFormat(QString mimetype)'''
    def clear(self):
        '''void QMimeData.clear()'''
    def formats(self):
        '''QStringList QMimeData.formats()'''
        return QStringList()
    def hasFormat(self, mimetype):
        '''bool QMimeData.hasFormat(QString mimetype)'''
        return bool()
    def setData(self, mimetype, data):
        '''void QMimeData.setData(QString mimetype, QByteArray data)'''
    def data(self, mimetype):
        '''QByteArray QMimeData.data(QString mimetype)'''
        return QByteArray()
    def hasColor(self):
        '''bool QMimeData.hasColor()'''
        return bool()
    def setColorData(self, color):
        '''void QMimeData.setColorData(QVariant color)'''
    def colorData(self):
        '''QVariant QMimeData.colorData()'''
        return QVariant()
    def hasImage(self):
        '''bool QMimeData.hasImage()'''
        return bool()
    def setImageData(self, image):
        '''void QMimeData.setImageData(QVariant image)'''
    def imageData(self):
        '''QVariant QMimeData.imageData()'''
        return QVariant()
    def hasHtml(self):
        '''bool QMimeData.hasHtml()'''
        return bool()
    def setHtml(self, html):
        '''void QMimeData.setHtml(QString html)'''
    def html(self):
        '''QString QMimeData.html()'''
        return QString()
    def hasText(self):
        '''bool QMimeData.hasText()'''
        return bool()
    def setText(self, text):
        '''void QMimeData.setText(QString text)'''
    def text(self):
        '''QString QMimeData.text()'''
        return QString()
    def hasUrls(self):
        '''bool QMimeData.hasUrls()'''
        return bool()
    def setUrls(self, urls):
        '''void QMimeData.setUrls(list-of-QUrl urls)'''
    def urls(self):
        '''list-of-QUrl QMimeData.urls()'''
        return [QUrl()]


class QMutex():
    """"""
    # Enum QMutex.RecursionMode
    NonRecursive = 0
    Recursive = 0

    def __init__(self, mode = QMutex.NonRecursive):
        '''void QMutex.__init__(QMutex.RecursionMode mode = QMutex.NonRecursive)'''
    def unlock(self):
        '''void QMutex.unlock()'''
    def tryLock(self):
        '''bool QMutex.tryLock()'''
        return bool()
    def tryLock(self, timeout):
        '''bool QMutex.tryLock(int timeout)'''
        return bool()
    def lock(self):
        '''void QMutex.lock()'''


class QMutexLocker():
    """"""
    def __init__(self, m):
        '''void QMutexLocker.__init__(QMutex m)'''
    def __exit__(self, type, value, traceback):
        '''void QMutexLocker.__exit__(object type, object value, object traceback)'''
    def __enter__(self):
        '''object QMutexLocker.__enter__()'''
        return object()
    def mutex(self):
        '''QMutex QMutexLocker.mutex()'''
        return QMutex()
    def relock(self):
        '''void QMutexLocker.relock()'''
    def unlock(self):
        '''void QMutexLocker.unlock()'''


class QObjectCleanupHandler(QObject):
    """"""
    def __init__(self):
        '''void QObjectCleanupHandler.__init__()'''
    def clear(self):
        '''void QObjectCleanupHandler.clear()'''
    def isEmpty(self):
        '''bool QObjectCleanupHandler.isEmpty()'''
        return bool()
    def remove(self, object):
        '''void QObjectCleanupHandler.remove(QObject object)'''
    def add(self, object):
        '''QObject QObjectCleanupHandler.add(QObject object)'''
        return QObject()


class QMetaObject():
    """"""
    def __init__(self):
        '''void QMetaObject.__init__()'''
    def __init__(self):
        '''QMetaObject QMetaObject.__init__()'''
        return QMetaObject()
    def newInstance(self, value0 = QGenericArgument(0,0), value1 = QGenericArgument(0,0), value2 = QGenericArgument(0,0), value3 = QGenericArgument(0,0), value4 = QGenericArgument(0,0), value5 = QGenericArgument(0,0), value6 = QGenericArgument(0,0), value7 = QGenericArgument(0,0), value8 = QGenericArgument(0,0), value9 = QGenericArgument(0,0)):
        '''QObject QMetaObject.newInstance(QGenericArgument value0 = QGenericArgument(0,0), QGenericArgument value1 = QGenericArgument(0,0), QGenericArgument value2 = QGenericArgument(0,0), QGenericArgument value3 = QGenericArgument(0,0), QGenericArgument value4 = QGenericArgument(0,0), QGenericArgument value5 = QGenericArgument(0,0), QGenericArgument value6 = QGenericArgument(0,0), QGenericArgument value7 = QGenericArgument(0,0), QGenericArgument value8 = QGenericArgument(0,0), QGenericArgument value9 = QGenericArgument(0,0))'''
        return QObject()
    def constructor(self, index):
        '''QMetaMethod QMetaObject.constructor(int index)'''
        return QMetaMethod()
    def indexOfConstructor(self, constructor):
        '''int QMetaObject.indexOfConstructor(str constructor)'''
        return int()
    def constructorCount(self):
        '''int QMetaObject.constructorCount()'''
        return int()
    def invokeMethod(self, obj, member, type, ret, value0 = QGenericArgument(0,0), value1 = QGenericArgument(0,0), value2 = QGenericArgument(0,0), value3 = QGenericArgument(0,0), value4 = QGenericArgument(0,0), value5 = QGenericArgument(0,0), value6 = QGenericArgument(0,0), value7 = QGenericArgument(0,0), value8 = QGenericArgument(0,0), value9 = QGenericArgument(0,0)):
        '''static object QMetaObject.invokeMethod(QObject obj, str member, Qt.ConnectionType type, QGenericReturnArgument ret, QGenericArgument value0 = QGenericArgument(0,0), QGenericArgument value1 = QGenericArgument(0,0), QGenericArgument value2 = QGenericArgument(0,0), QGenericArgument value3 = QGenericArgument(0,0), QGenericArgument value4 = QGenericArgument(0,0), QGenericArgument value5 = QGenericArgument(0,0), QGenericArgument value6 = QGenericArgument(0,0), QGenericArgument value7 = QGenericArgument(0,0), QGenericArgument value8 = QGenericArgument(0,0), QGenericArgument value9 = QGenericArgument(0,0))'''
        return object()
    def invokeMethod(self, obj, member, ret, value0 = QGenericArgument(0,0), value1 = QGenericArgument(0,0), value2 = QGenericArgument(0,0), value3 = QGenericArgument(0,0), value4 = QGenericArgument(0,0), value5 = QGenericArgument(0,0), value6 = QGenericArgument(0,0), value7 = QGenericArgument(0,0), value8 = QGenericArgument(0,0), value9 = QGenericArgument(0,0)):
        '''static object QMetaObject.invokeMethod(QObject obj, str member, QGenericReturnArgument ret, QGenericArgument value0 = QGenericArgument(0,0), QGenericArgument value1 = QGenericArgument(0,0), QGenericArgument value2 = QGenericArgument(0,0), QGenericArgument value3 = QGenericArgument(0,0), QGenericArgument value4 = QGenericArgument(0,0), QGenericArgument value5 = QGenericArgument(0,0), QGenericArgument value6 = QGenericArgument(0,0), QGenericArgument value7 = QGenericArgument(0,0), QGenericArgument value8 = QGenericArgument(0,0), QGenericArgument value9 = QGenericArgument(0,0))'''
        return object()
    def invokeMethod(self, obj, member, type, value0 = QGenericArgument(0,0), value1 = QGenericArgument(0,0), value2 = QGenericArgument(0,0), value3 = QGenericArgument(0,0), value4 = QGenericArgument(0,0), value5 = QGenericArgument(0,0), value6 = QGenericArgument(0,0), value7 = QGenericArgument(0,0), value8 = QGenericArgument(0,0), value9 = QGenericArgument(0,0)):
        '''static object QMetaObject.invokeMethod(QObject obj, str member, Qt.ConnectionType type, QGenericArgument value0 = QGenericArgument(0,0), QGenericArgument value1 = QGenericArgument(0,0), QGenericArgument value2 = QGenericArgument(0,0), QGenericArgument value3 = QGenericArgument(0,0), QGenericArgument value4 = QGenericArgument(0,0), QGenericArgument value5 = QGenericArgument(0,0), QGenericArgument value6 = QGenericArgument(0,0), QGenericArgument value7 = QGenericArgument(0,0), QGenericArgument value8 = QGenericArgument(0,0), QGenericArgument value9 = QGenericArgument(0,0))'''
        return object()
    def invokeMethod(self, obj, member, value0 = QGenericArgument(0,0), value1 = QGenericArgument(0,0), value2 = QGenericArgument(0,0), value3 = QGenericArgument(0,0), value4 = QGenericArgument(0,0), value5 = QGenericArgument(0,0), value6 = QGenericArgument(0,0), value7 = QGenericArgument(0,0), value8 = QGenericArgument(0,0), value9 = QGenericArgument(0,0)):
        '''static object QMetaObject.invokeMethod(QObject obj, str member, QGenericArgument value0 = QGenericArgument(0,0), QGenericArgument value1 = QGenericArgument(0,0), QGenericArgument value2 = QGenericArgument(0,0), QGenericArgument value3 = QGenericArgument(0,0), QGenericArgument value4 = QGenericArgument(0,0), QGenericArgument value5 = QGenericArgument(0,0), QGenericArgument value6 = QGenericArgument(0,0), QGenericArgument value7 = QGenericArgument(0,0), QGenericArgument value8 = QGenericArgument(0,0), QGenericArgument value9 = QGenericArgument(0,0))'''
        return object()
    def normalizedType(self, type):
        '''static QByteArray QMetaObject.normalizedType(str type)'''
        return QByteArray()
    def normalizedSignature(self, method):
        '''static QByteArray QMetaObject.normalizedSignature(str method)'''
        return QByteArray()
    def connectSlotsByName(self, o):
        '''static void QMetaObject.connectSlotsByName(QObject o)'''
    def checkConnectArgs(self, signal, method):
        '''static bool QMetaObject.checkConnectArgs(str signal, str method)'''
        return bool()
    def classInfo(self, index):
        '''QMetaClassInfo QMetaObject.classInfo(int index)'''
        return QMetaClassInfo()
    def property(self, index):
        '''QMetaProperty QMetaObject.property(int index)'''
        return QMetaProperty()
    def enumerator(self, index):
        '''QMetaEnum QMetaObject.enumerator(int index)'''
        return QMetaEnum()
    def method(self, index):
        '''QMetaMethod QMetaObject.method(int index)'''
        return QMetaMethod()
    def indexOfClassInfo(self, name):
        '''int QMetaObject.indexOfClassInfo(str name)'''
        return int()
    def indexOfProperty(self, name):
        '''int QMetaObject.indexOfProperty(str name)'''
        return int()
    def indexOfEnumerator(self, name):
        '''int QMetaObject.indexOfEnumerator(str name)'''
        return int()
    def indexOfSlot(self, slot):
        '''int QMetaObject.indexOfSlot(str slot)'''
        return int()
    def indexOfSignal(self, signal):
        '''int QMetaObject.indexOfSignal(str signal)'''
        return int()
    def indexOfMethod(self, method):
        '''int QMetaObject.indexOfMethod(str method)'''
        return int()
    def classInfoCount(self):
        '''int QMetaObject.classInfoCount()'''
        return int()
    def propertyCount(self):
        '''int QMetaObject.propertyCount()'''
        return int()
    def enumeratorCount(self):
        '''int QMetaObject.enumeratorCount()'''
        return int()
    def methodCount(self):
        '''int QMetaObject.methodCount()'''
        return int()
    def classInfoOffset(self):
        '''int QMetaObject.classInfoOffset()'''
        return int()
    def propertyOffset(self):
        '''int QMetaObject.propertyOffset()'''
        return int()
    def enumeratorOffset(self):
        '''int QMetaObject.enumeratorOffset()'''
        return int()
    def methodOffset(self):
        '''int QMetaObject.methodOffset()'''
        return int()
    def userProperty(self):
        '''QMetaProperty QMetaObject.userProperty()'''
        return QMetaProperty()
    def superClass(self):
        '''QMetaObject QMetaObject.superClass()'''
        return QMetaObject()
    def className(self):
        '''str QMetaObject.className()'''
        return str()


class QGenericArgument():
    """"""


class QGenericReturnArgument():
    """"""


class QParallelAnimationGroup(QAnimationGroup):
    """"""
    def __init__(self, parent = None):
        '''void QParallelAnimationGroup.__init__(QObject parent = None)'''
    def updateDirection(self, direction):
        '''void QParallelAnimationGroup.updateDirection(QAbstractAnimation.Direction direction)'''
    def updateState(self, newState, oldState):
        '''void QParallelAnimationGroup.updateState(QAbstractAnimation.State newState, QAbstractAnimation.State oldState)'''
    def updateCurrentTime(self, currentTime):
        '''void QParallelAnimationGroup.updateCurrentTime(int currentTime)'''
    def event(self, event):
        '''bool QParallelAnimationGroup.event(QEvent event)'''
        return bool()
    def duration(self):
        '''int QParallelAnimationGroup.duration()'''
        return int()


class QPauseAnimation(QAbstractAnimation):
    """"""
    def __init__(self, parent = None):
        '''void QPauseAnimation.__init__(QObject parent = None)'''
    def __init__(self, msecs, parent = None):
        '''void QPauseAnimation.__init__(int msecs, QObject parent = None)'''
    def updateCurrentTime(self):
        '''int QPauseAnimation.updateCurrentTime()'''
        return int()
    def event(self, e):
        '''bool QPauseAnimation.event(QEvent e)'''
        return bool()
    def setDuration(self, msecs):
        '''void QPauseAnimation.setDuration(int msecs)'''
    def duration(self):
        '''int QPauseAnimation.duration()'''
        return int()


class QVariantAnimation(QAbstractAnimation):
    """"""
    def __init__(self, parent = None):
        '''void QVariantAnimation.__init__(QObject parent = None)'''
    def interpolated(self, from_, to, progress):
        '''QVariant QVariantAnimation.interpolated(QVariant from, QVariant to, float progress)'''
        return QVariant()
    def updateCurrentValue(self, value):
        '''abstract void QVariantAnimation.updateCurrentValue(QVariant value)'''
    def updateState(self, newState, oldState):
        '''void QVariantAnimation.updateState(QAbstractAnimation.State newState, QAbstractAnimation.State oldState)'''
    def updateCurrentTime(self):
        '''int QVariantAnimation.updateCurrentTime()'''
        return int()
    def event(self, event):
        '''bool QVariantAnimation.event(QEvent event)'''
        return bool()
    valueChanged = pyqtSignal() # void valueChanged(const QVariant&) - signal
    def setEasingCurve(self, easing):
        '''void QVariantAnimation.setEasingCurve(QEasingCurve easing)'''
    def easingCurve(self):
        '''QEasingCurve QVariantAnimation.easingCurve()'''
        return QEasingCurve()
    def setDuration(self, msecs):
        '''void QVariantAnimation.setDuration(int msecs)'''
    def duration(self):
        '''int QVariantAnimation.duration()'''
        return int()
    def currentValue(self):
        '''QVariant QVariantAnimation.currentValue()'''
        return QVariant()
    def setKeyValues(self, values):
        '''void QVariantAnimation.setKeyValues(list-of-tuple-of-float-QVariant values)'''
    def keyValues(self):
        '''list-of-tuple-of-float-QVariant QVariantAnimation.keyValues()'''
        return [tuple-of-float-QVariant()]
    def setKeyValueAt(self, step, value):
        '''void QVariantAnimation.setKeyValueAt(float step, QVariant value)'''
    def keyValueAt(self, step):
        '''QVariant QVariantAnimation.keyValueAt(float step)'''
        return QVariant()
    def setEndValue(self, value):
        '''void QVariantAnimation.setEndValue(QVariant value)'''
    def endValue(self):
        '''QVariant QVariantAnimation.endValue()'''
        return QVariant()
    def setStartValue(self, value):
        '''void QVariantAnimation.setStartValue(QVariant value)'''
    def startValue(self):
        '''QVariant QVariantAnimation.startValue()'''
        return QVariant()


class QPropertyAnimation(QVariantAnimation):
    """"""
    def __init__(self, parent = None):
        '''void QPropertyAnimation.__init__(QObject parent = None)'''
    def __init__(self, target, propertyName, parent = None):
        '''void QPropertyAnimation.__init__(QObject target, QByteArray propertyName, QObject parent = None)'''
    def updateState(self, newState, oldState):
        '''void QPropertyAnimation.updateState(QAbstractAnimation.State newState, QAbstractAnimation.State oldState)'''
    def updateCurrentValue(self, value):
        '''void QPropertyAnimation.updateCurrentValue(QVariant value)'''
    def event(self, event):
        '''bool QPropertyAnimation.event(QEvent event)'''
        return bool()
    def setPropertyName(self, propertyName):
        '''void QPropertyAnimation.setPropertyName(QByteArray propertyName)'''
    def propertyName(self):
        '''QByteArray QPropertyAnimation.propertyName()'''
        return QByteArray()
    def setTargetObject(self, target):
        '''void QPropertyAnimation.setTargetObject(QObject target)'''
    def targetObject(self):
        '''QObject QPropertyAnimation.targetObject()'''
        return QObject()


class QPluginLoader(QObject):
    """"""
    def __init__(self, parent = None):
        '''void QPluginLoader.__init__(QObject parent = None)'''
    def __init__(self, fileName, parent = None):
        '''void QPluginLoader.__init__(QString fileName, QObject parent = None)'''
    def loadHints(self):
        '''QLibrary.LoadHints QPluginLoader.loadHints()'''
        return QLibrary.LoadHints()
    def setLoadHints(self, loadHints):
        '''void QPluginLoader.setLoadHints(QLibrary.LoadHints loadHints)'''
    def errorString(self):
        '''QString QPluginLoader.errorString()'''
        return QString()
    def fileName(self):
        '''QString QPluginLoader.fileName()'''
        return QString()
    def setFileName(self, fileName):
        '''void QPluginLoader.setFileName(QString fileName)'''
    def isLoaded(self):
        '''bool QPluginLoader.isLoaded()'''
        return bool()
    def unload(self):
        '''bool QPluginLoader.unload()'''
        return bool()
    def load(self):
        '''bool QPluginLoader.load()'''
        return bool()
    def staticInstances(self):
        '''static list-of-QObject QPluginLoader.staticInstances()'''
        return [QObject()]
    def instance(self):
        '''QObject QPluginLoader.instance()'''
        return QObject()


class QPoint():
    """"""
    def __init__(self):
        '''void QPoint.__init__()'''
    def __init__(self, xpos, ypos):
        '''void QPoint.__init__(int xpos, int ypos)'''
    def __init__(self):
        '''QPoint QPoint.__init__()'''
        return QPoint()
    def __eq__(self, p2):
        '''bool QPoint.__eq__(QPoint p2)'''
        return bool()
    def __ne__(self, p2):
        '''bool QPoint.__ne__(QPoint p2)'''
        return bool()
    def __add__(self, p2):
        '''QPoint QPoint.__add__(QPoint p2)'''
        return QPoint()
    def __sub__(self, p2):
        '''QPoint QPoint.__sub__(QPoint p2)'''
        return QPoint()
    def __mul__(self, c):
        '''QPoint QPoint.__mul__(int c)'''
        return QPoint()
    def __mul__(self, p):
        '''QPoint QPoint.__mul__(QPoint p)'''
        return QPoint()
    def __mul__(self, c):
        '''QPoint QPoint.__mul__(float c)'''
        return QPoint()
    def __mul__(self, p):
        '''QPoint QPoint.__mul__(QPoint p)'''
        return QPoint()
    def __neg__(self):
        '''QPoint QPoint.__neg__()'''
        return QPoint()
    def __div__(self, c):
        '''QPoint QPoint.__div__(float c)'''
        return QPoint()
    def __idiv__(self, c):
        '''QPoint QPoint.__idiv__(float c)'''
        return QPoint()
    def __imul__(self, c):
        '''QPoint QPoint.__imul__(int c)'''
        return QPoint()
    def __imul__(self, c):
        '''QPoint QPoint.__imul__(float c)'''
        return QPoint()
    def __isub__(self, p):
        '''QPoint QPoint.__isub__(QPoint p)'''
        return QPoint()
    def __iadd__(self, p):
        '''QPoint QPoint.__iadd__(QPoint p)'''
        return QPoint()
    def setY(self, ypos):
        '''void QPoint.setY(int ypos)'''
    def setX(self, xpos):
        '''void QPoint.setX(int xpos)'''
    def y(self):
        '''int QPoint.y()'''
        return int()
    def x(self):
        '''int QPoint.x()'''
        return int()
    def __bool__(self):
        '''int QPoint.__bool__()'''
        return int()
    def isNull(self):
        '''bool QPoint.isNull()'''
        return bool()
    def __repr__(self):
        '''str QPoint.__repr__()'''
        return str()
    def manhattanLength(self):
        '''int QPoint.manhattanLength()'''
        return int()


class QPointF():
    """"""
    def __init__(self):
        '''void QPointF.__init__()'''
    def __init__(self, xpos, ypos):
        '''void QPointF.__init__(float xpos, float ypos)'''
    def __init__(self, p):
        '''void QPointF.__init__(QPoint p)'''
    def __init__(self):
        '''QPointF QPointF.__init__()'''
        return QPointF()
    def __eq__(self, p2):
        '''bool QPointF.__eq__(QPointF p2)'''
        return bool()
    def __ne__(self, p2):
        '''bool QPointF.__ne__(QPointF p2)'''
        return bool()
    def __add__(self, p2):
        '''QPointF QPointF.__add__(QPointF p2)'''
        return QPointF()
    def __sub__(self, p2):
        '''QPointF QPointF.__sub__(QPointF p2)'''
        return QPointF()
    def __mul__(self, c):
        '''QPointF QPointF.__mul__(float c)'''
        return QPointF()
    def __neg__(self):
        '''QPointF QPointF.__neg__()'''
        return QPointF()
    def __div__(self, c):
        '''QPointF QPointF.__div__(float c)'''
        return QPointF()
    def manhattanLength(self):
        '''float QPointF.manhattanLength()'''
        return float()
    def toPoint(self):
        '''QPoint QPointF.toPoint()'''
        return QPoint()
    def __idiv__(self, c):
        '''QPointF QPointF.__idiv__(float c)'''
        return QPointF()
    def __imul__(self, c):
        '''QPointF QPointF.__imul__(float c)'''
        return QPointF()
    def __isub__(self, p):
        '''QPointF QPointF.__isub__(QPointF p)'''
        return QPointF()
    def __iadd__(self, p):
        '''QPointF QPointF.__iadd__(QPointF p)'''
        return QPointF()
    def setY(self, ypos):
        '''void QPointF.setY(float ypos)'''
    def setX(self, xpos):
        '''void QPointF.setX(float xpos)'''
    def y(self):
        '''float QPointF.y()'''
        return float()
    def x(self):
        '''float QPointF.x()'''
        return float()
    def __bool__(self):
        '''int QPointF.__bool__()'''
        return int()
    def isNull(self):
        '''bool QPointF.isNull()'''
        return bool()
    def __repr__(self):
        '''str QPointF.__repr__()'''
        return str()


class QProcess(QIODevice):
    """"""
    # Enum QProcess.ProcessChannelMode
    SeparateChannels = 0
    MergedChannels = 0
    ForwardedChannels = 0

    # Enum QProcess.ProcessChannel
    StandardOutput = 0
    StandardError = 0

    # Enum QProcess.ProcessState
    NotRunning = 0
    Starting = 0
    Running = 0

    # Enum QProcess.ProcessError
    FailedToStart = 0
    Crashed = 0
    Timedout = 0
    ReadError = 0
    WriteError = 0
    UnknownError = 0

    # Enum QProcess.ExitStatus
    NormalExit = 0
    CrashExit = 0

    def __init__(self, parent = None):
        '''void QProcess.__init__(QObject parent = None)'''
    def processEnvironment(self):
        '''QProcessEnvironment QProcess.processEnvironment()'''
        return QProcessEnvironment()
    def setProcessEnvironment(self, environment):
        '''void QProcess.setProcessEnvironment(QProcessEnvironment environment)'''
    def writeData(self, data):
        '''int QProcess.writeData(str data)'''
        return int()
    def readData(self, maxlen):
        '''str QProcess.readData(int maxlen)'''
        return str()
    def setupChildProcess(self):
        '''void QProcess.setupChildProcess()'''
    def setProcessState(self, state):
        '''void QProcess.setProcessState(QProcess.ProcessState state)'''
    readyReadStandardError = pyqtSignal() # void readyReadStandardError() - signal
    readyReadStandardOutput = pyqtSignal() # void readyReadStandardOutput() - signal
    stateChanged = pyqtSignal() # void stateChanged(QProcess::ProcessState) - signal
    finished = pyqtSignal() # void finished(int,QProcess::ExitStatus) - signal
    finished = pyqtSignal() # void finished(int) - signal
    started = pyqtSignal() # void started() - signal
    def kill(self):
        '''void QProcess.kill()'''
    def terminate(self):
        '''void QProcess.terminate()'''
    def setStandardOutputProcess(self, destination):
        '''void QProcess.setStandardOutputProcess(QProcess destination)'''
    def setStandardErrorFile(self, fileName, mode = QIODevice.Truncate):
        '''void QProcess.setStandardErrorFile(QString fileName, QIODevice.OpenMode mode = QIODevice.Truncate)'''
    def setStandardOutputFile(self, fileName, mode = QIODevice.Truncate):
        '''void QProcess.setStandardOutputFile(QString fileName, QIODevice.OpenMode mode = QIODevice.Truncate)'''
    def setStandardInputFile(self, fileName):
        '''void QProcess.setStandardInputFile(QString fileName)'''
    def setProcessChannelMode(self, mode):
        '''void QProcess.setProcessChannelMode(QProcess.ProcessChannelMode mode)'''
    def processChannelMode(self):
        '''QProcess.ProcessChannelMode QProcess.processChannelMode()'''
        return QProcess.ProcessChannelMode()
    def systemEnvironment(self):
        '''static QStringList QProcess.systemEnvironment()'''
        return QStringList()
    def startDetached(self, program, arguments, workingDirectory, pid):
        '''static bool QProcess.startDetached(QString program, QStringList arguments, QString workingDirectory, int pid)'''
        return bool()
    def startDetached(self, program, arguments):
        '''static bool QProcess.startDetached(QString program, QStringList arguments)'''
        return bool()
    def startDetached(self, program):
        '''static bool QProcess.startDetached(QString program)'''
        return bool()
    def execute(self, program, arguments):
        '''static int QProcess.execute(QString program, QStringList arguments)'''
        return int()
    def execute(self, program):
        '''static int QProcess.execute(QString program)'''
        return int()
    def atEnd(self):
        '''bool QProcess.atEnd()'''
        return bool()
    def close(self):
        '''void QProcess.close()'''
    def canReadLine(self):
        '''bool QProcess.canReadLine()'''
        return bool()
    def isSequential(self):
        '''bool QProcess.isSequential()'''
        return bool()
    def bytesToWrite(self):
        '''int QProcess.bytesToWrite()'''
        return int()
    def bytesAvailable(self):
        '''int QProcess.bytesAvailable()'''
        return int()
    def exitStatus(self):
        '''QProcess.ExitStatus QProcess.exitStatus()'''
        return QProcess.ExitStatus()
    def exitCode(self):
        '''int QProcess.exitCode()'''
        return int()
    def readAllStandardError(self):
        '''QByteArray QProcess.readAllStandardError()'''
        return QByteArray()
    def readAllStandardOutput(self):
        '''QByteArray QProcess.readAllStandardOutput()'''
        return QByteArray()
    def waitForFinished(self, msecs = 30000):
        '''bool QProcess.waitForFinished(int msecs = 30000)'''
        return bool()
    def waitForBytesWritten(self, msecs = 30000):
        '''bool QProcess.waitForBytesWritten(int msecs = 30000)'''
        return bool()
    def waitForReadyRead(self, msecs = 30000):
        '''bool QProcess.waitForReadyRead(int msecs = 30000)'''
        return bool()
    def waitForStarted(self, msecs = 30000):
        '''bool QProcess.waitForStarted(int msecs = 30000)'''
        return bool()
    def pid(self):
        '''int QProcess.pid()'''
        return int()
    def state(self):
        '''QProcess.ProcessState QProcess.state()'''
        return QProcess.ProcessState()
    def error(self):
        '''QProcess.ProcessError QProcess.error()'''
        return QProcess.ProcessError()
    error = pyqtSignal() # void error(QProcess::ProcessError) - signal
    def environment(self):
        '''QStringList QProcess.environment()'''
        return QStringList()
    def setEnvironment(self, environment):
        '''void QProcess.setEnvironment(QStringList environment)'''
    def setWorkingDirectory(self, dir):
        '''void QProcess.setWorkingDirectory(QString dir)'''
    def workingDirectory(self):
        '''QString QProcess.workingDirectory()'''
        return QString()
    def closeWriteChannel(self):
        '''void QProcess.closeWriteChannel()'''
    def closeReadChannel(self, channel):
        '''void QProcess.closeReadChannel(QProcess.ProcessChannel channel)'''
    def setReadChannel(self, channel):
        '''void QProcess.setReadChannel(QProcess.ProcessChannel channel)'''
    def readChannel(self):
        '''QProcess.ProcessChannel QProcess.readChannel()'''
        return QProcess.ProcessChannel()
    def setReadChannelMode(self, mode):
        '''void QProcess.setReadChannelMode(QProcess.ProcessChannelMode mode)'''
    def readChannelMode(self):
        '''QProcess.ProcessChannelMode QProcess.readChannelMode()'''
        return QProcess.ProcessChannelMode()
    def start(self, program, arguments, mode = QIODevice.ReadWrite):
        '''void QProcess.start(QString program, QStringList arguments, QIODevice.OpenMode mode = QIODevice.ReadWrite)'''
    def start(self, program, mode = QIODevice.ReadWrite):
        '''void QProcess.start(QString program, QIODevice.OpenMode mode = QIODevice.ReadWrite)'''


class QProcessEnvironment():
    """"""
    def __init__(self):
        '''void QProcessEnvironment.__init__()'''
    def __init__(self, other):
        '''void QProcessEnvironment.__init__(QProcessEnvironment other)'''
    def keys(self):
        '''QStringList QProcessEnvironment.keys()'''
        return QStringList()
    def systemEnvironment(self):
        '''static QProcessEnvironment QProcessEnvironment.systemEnvironment()'''
        return QProcessEnvironment()
    def toStringList(self):
        '''QStringList QProcessEnvironment.toStringList()'''
        return QStringList()
    def value(self, name, defaultValue = QString()):
        '''QString QProcessEnvironment.value(QString name, QString defaultValue = QString())'''
        return QString()
    def remove(self, name):
        '''void QProcessEnvironment.remove(QString name)'''
    def insert(self, name, value):
        '''void QProcessEnvironment.insert(QString name, QString value)'''
    def insert(self, e):
        '''void QProcessEnvironment.insert(QProcessEnvironment e)'''
    def contains(self, name):
        '''bool QProcessEnvironment.contains(QString name)'''
        return bool()
    def clear(self):
        '''void QProcessEnvironment.clear()'''
    def isEmpty(self):
        '''bool QProcessEnvironment.isEmpty()'''
        return bool()
    def __ne__(self, other):
        '''bool QProcessEnvironment.__ne__(QProcessEnvironment other)'''
        return bool()
    def __eq__(self, other):
        '''bool QProcessEnvironment.__eq__(QProcessEnvironment other)'''
        return bool()


class QReadWriteLock():
    """"""
    # Enum QReadWriteLock.RecursionMode
    NonRecursive = 0
    Recursive = 0

    def __init__(self):
        '''void QReadWriteLock.__init__()'''
    def __init__(self, recursionMode):
        '''void QReadWriteLock.__init__(QReadWriteLock.RecursionMode recursionMode)'''
    def unlock(self):
        '''void QReadWriteLock.unlock()'''
    def tryLockForWrite(self):
        '''bool QReadWriteLock.tryLockForWrite()'''
        return bool()
    def tryLockForWrite(self, timeout):
        '''bool QReadWriteLock.tryLockForWrite(int timeout)'''
        return bool()
    def lockForWrite(self):
        '''void QReadWriteLock.lockForWrite()'''
    def tryLockForRead(self):
        '''bool QReadWriteLock.tryLockForRead()'''
        return bool()
    def tryLockForRead(self, timeout):
        '''bool QReadWriteLock.tryLockForRead(int timeout)'''
        return bool()
    def lockForRead(self):
        '''void QReadWriteLock.lockForRead()'''


class QReadLocker():
    """"""
    def __init__(self, areadWriteLock):
        '''void QReadLocker.__init__(QReadWriteLock areadWriteLock)'''
    def __exit__(self, type, value, traceback):
        '''void QReadLocker.__exit__(object type, object value, object traceback)'''
    def __enter__(self):
        '''object QReadLocker.__enter__()'''
        return object()
    def readWriteLock(self):
        '''QReadWriteLock QReadLocker.readWriteLock()'''
        return QReadWriteLock()
    def relock(self):
        '''void QReadLocker.relock()'''
    def unlock(self):
        '''void QReadLocker.unlock()'''


class QWriteLocker():
    """"""
    def __init__(self, areadWriteLock):
        '''void QWriteLocker.__init__(QReadWriteLock areadWriteLock)'''
    def __exit__(self, type, value, traceback):
        '''void QWriteLocker.__exit__(object type, object value, object traceback)'''
    def __enter__(self):
        '''object QWriteLocker.__enter__()'''
        return object()
    def readWriteLock(self):
        '''QReadWriteLock QWriteLocker.readWriteLock()'''
        return QReadWriteLock()
    def relock(self):
        '''void QWriteLocker.relock()'''
    def unlock(self):
        '''void QWriteLocker.unlock()'''


class QRect():
    """"""
    def __init__(self):
        '''void QRect.__init__()'''
    def __init__(self, aleft, atop, awidth, aheight):
        '''void QRect.__init__(int aleft, int atop, int awidth, int aheight)'''
    def __init__(self, atopLeft, abottomRight):
        '''void QRect.__init__(QPoint atopLeft, QPoint abottomRight)'''
    def __init__(self, atopLeft, asize):
        '''void QRect.__init__(QPoint atopLeft, QSize asize)'''
    def __init__(self):
        '''QRect QRect.__init__()'''
        return QRect()
    def __eq__(self, r2):
        '''bool QRect.__eq__(QRect r2)'''
        return bool()
    def __ne__(self, r2):
        '''bool QRect.__ne__(QRect r2)'''
        return bool()
    def united(self, r):
        '''QRect QRect.united(QRect r)'''
        return QRect()
    def intersected(self, other):
        '''QRect QRect.intersected(QRect other)'''
        return QRect()
    def unite(self, r):
        '''QRect QRect.unite(QRect r)'''
        return QRect()
    def intersect(self, r):
        '''QRect QRect.intersect(QRect r)'''
        return QRect()
    def __iand__(self, r):
        '''QRect QRect.__iand__(QRect r)'''
        return QRect()
    def __ior__(self, r):
        '''QRect QRect.__ior__(QRect r)'''
        return QRect()
    def setSize(self, s):
        '''void QRect.setSize(QSize s)'''
    def setHeight(self, h):
        '''void QRect.setHeight(int h)'''
    def setWidth(self, w):
        '''void QRect.setWidth(int w)'''
    def adjust(self, dx1, dy1, dx2, dy2):
        '''void QRect.adjust(int dx1, int dy1, int dx2, int dy2)'''
    def adjusted(self, xp1, yp1, xp2, yp2):
        '''QRect QRect.adjusted(int xp1, int yp1, int xp2, int yp2)'''
        return QRect()
    def setCoords(self, xp1, yp1, xp2, yp2):
        '''void QRect.setCoords(int xp1, int yp1, int xp2, int yp2)'''
    def getCoords(self, xp1, yp1, xp2, yp2):
        '''void QRect.getCoords(int xp1, int yp1, int xp2, int yp2)'''
    def setRect(self, ax, ay, aw, ah):
        '''void QRect.setRect(int ax, int ay, int aw, int ah)'''
    def getRect(self, ax, ay, aw, ah):
        '''void QRect.getRect(int ax, int ay, int aw, int ah)'''
    def moveBottomLeft(self, p):
        '''void QRect.moveBottomLeft(QPoint p)'''
    def moveTopRight(self, p):
        '''void QRect.moveTopRight(QPoint p)'''
    def moveBottomRight(self, p):
        '''void QRect.moveBottomRight(QPoint p)'''
    def moveTopLeft(self, p):
        '''void QRect.moveTopLeft(QPoint p)'''
    def moveBottom(self, pos):
        '''void QRect.moveBottom(int pos)'''
    def moveRight(self, pos):
        '''void QRect.moveRight(int pos)'''
    def moveTop(self, pos):
        '''void QRect.moveTop(int pos)'''
    def moveLeft(self, pos):
        '''void QRect.moveLeft(int pos)'''
    def moveTo(self, ax, ay):
        '''void QRect.moveTo(int ax, int ay)'''
    def moveTo(self, p):
        '''void QRect.moveTo(QPoint p)'''
    def translated(self, dx, dy):
        '''QRect QRect.translated(int dx, int dy)'''
        return QRect()
    def translated(self, p):
        '''QRect QRect.translated(QPoint p)'''
        return QRect()
    def translate(self, dx, dy):
        '''void QRect.translate(int dx, int dy)'''
    def translate(self, p):
        '''void QRect.translate(QPoint p)'''
    def size(self):
        '''QSize QRect.size()'''
        return QSize()
    def height(self):
        '''int QRect.height()'''
        return int()
    def width(self):
        '''int QRect.width()'''
        return int()
    def center(self):
        '''QPoint QRect.center()'''
        return QPoint()
    def bottomLeft(self):
        '''QPoint QRect.bottomLeft()'''
        return QPoint()
    def topRight(self):
        '''QPoint QRect.topRight()'''
        return QPoint()
    def bottomRight(self):
        '''QPoint QRect.bottomRight()'''
        return QPoint()
    def topLeft(self):
        '''QPoint QRect.topLeft()'''
        return QPoint()
    def setY(self, ay):
        '''void QRect.setY(int ay)'''
    def setX(self, ax):
        '''void QRect.setX(int ax)'''
    def setBottomLeft(self, p):
        '''void QRect.setBottomLeft(QPoint p)'''
    def setTopRight(self, p):
        '''void QRect.setTopRight(QPoint p)'''
    def setBottomRight(self, p):
        '''void QRect.setBottomRight(QPoint p)'''
    def setTopLeft(self, p):
        '''void QRect.setTopLeft(QPoint p)'''
    def setBottom(self, pos):
        '''void QRect.setBottom(int pos)'''
    def setRight(self, pos):
        '''void QRect.setRight(int pos)'''
    def setTop(self, pos):
        '''void QRect.setTop(int pos)'''
    def setLeft(self, pos):
        '''void QRect.setLeft(int pos)'''
    def y(self):
        '''int QRect.y()'''
        return int()
    def x(self):
        '''int QRect.x()'''
        return int()
    def bottom(self):
        '''int QRect.bottom()'''
        return int()
    def right(self):
        '''int QRect.right()'''
        return int()
    def top(self):
        '''int QRect.top()'''
        return int()
    def left(self):
        '''int QRect.left()'''
        return int()
    def __bool__(self):
        '''int QRect.__bool__()'''
        return int()
    def isValid(self):
        '''bool QRect.isValid()'''
        return bool()
    def isEmpty(self):
        '''bool QRect.isEmpty()'''
        return bool()
    def isNull(self):
        '''bool QRect.isNull()'''
        return bool()
    def __repr__(self):
        '''str QRect.__repr__()'''
        return str()
    def intersects(self, r):
        '''bool QRect.intersects(QRect r)'''
        return bool()
    def __contains__(self, p):
        '''int QRect.__contains__(QPoint p)'''
        return int()
    def __contains__(self, r):
        '''int QRect.__contains__(QRect r)'''
        return int()
    def contains(self, point, proper = False):
        '''bool QRect.contains(QPoint point, bool proper = False)'''
        return bool()
    def contains(self, rectangle, proper = False):
        '''bool QRect.contains(QRect rectangle, bool proper = False)'''
        return bool()
    def contains(self, ax, ay, aproper):
        '''bool QRect.contains(int ax, int ay, bool aproper)'''
        return bool()
    def contains(self, ax, ay):
        '''bool QRect.contains(int ax, int ay)'''
        return bool()
    def __and__(self, r):
        '''QRect QRect.__and__(QRect r)'''
        return QRect()
    def __or__(self, r):
        '''QRect QRect.__or__(QRect r)'''
        return QRect()
    def moveCenter(self, p):
        '''void QRect.moveCenter(QPoint p)'''
    def normalized(self):
        '''QRect QRect.normalized()'''
        return QRect()


class QRectF():
    """"""
    def __init__(self):
        '''void QRectF.__init__()'''
    def __init__(self, atopLeft, asize):
        '''void QRectF.__init__(QPointF atopLeft, QSizeF asize)'''
    def __init__(self, atopLeft, abottomRight):
        '''void QRectF.__init__(QPointF atopLeft, QPointF abottomRight)'''
    def __init__(self, aleft, atop, awidth, aheight):
        '''void QRectF.__init__(float aleft, float atop, float awidth, float aheight)'''
    def __init__(self, r):
        '''void QRectF.__init__(QRect r)'''
    def __init__(self):
        '''QRectF QRectF.__init__()'''
        return QRectF()
    def __eq__(self, r2):
        '''bool QRectF.__eq__(QRectF r2)'''
        return bool()
    def __ne__(self, r2):
        '''bool QRectF.__ne__(QRectF r2)'''
        return bool()
    def united(self, r):
        '''QRectF QRectF.united(QRectF r)'''
        return QRectF()
    def intersected(self, r):
        '''QRectF QRectF.intersected(QRectF r)'''
        return QRectF()
    def toRect(self):
        '''QRect QRectF.toRect()'''
        return QRect()
    def toAlignedRect(self):
        '''QRect QRectF.toAlignedRect()'''
        return QRect()
    def unite(self, r):
        '''QRectF QRectF.unite(QRectF r)'''
        return QRectF()
    def intersect(self, r):
        '''QRectF QRectF.intersect(QRectF r)'''
        return QRectF()
    def __iand__(self, r):
        '''QRectF QRectF.__iand__(QRectF r)'''
        return QRectF()
    def __ior__(self, r):
        '''QRectF QRectF.__ior__(QRectF r)'''
        return QRectF()
    def setSize(self, s):
        '''void QRectF.setSize(QSizeF s)'''
    def setHeight(self, ah):
        '''void QRectF.setHeight(float ah)'''
    def setWidth(self, aw):
        '''void QRectF.setWidth(float aw)'''
    def adjusted(self, xp1, yp1, xp2, yp2):
        '''QRectF QRectF.adjusted(float xp1, float yp1, float xp2, float yp2)'''
        return QRectF()
    def adjust(self, xp1, yp1, xp2, yp2):
        '''void QRectF.adjust(float xp1, float yp1, float xp2, float yp2)'''
    def setCoords(self, xp1, yp1, xp2, yp2):
        '''void QRectF.setCoords(float xp1, float yp1, float xp2, float yp2)'''
    def getCoords(self, xp1, yp1, xp2, yp2):
        '''void QRectF.getCoords(float xp1, float yp1, float xp2, float yp2)'''
    def setRect(self, ax, ay, aaw, aah):
        '''void QRectF.setRect(float ax, float ay, float aaw, float aah)'''
    def getRect(self, ax, ay, aaw, aah):
        '''void QRectF.getRect(float ax, float ay, float aaw, float aah)'''
    def translated(self, dx, dy):
        '''QRectF QRectF.translated(float dx, float dy)'''
        return QRectF()
    def translated(self, p):
        '''QRectF QRectF.translated(QPointF p)'''
        return QRectF()
    def moveTo(self, ax, ay):
        '''void QRectF.moveTo(float ax, float ay)'''
    def moveTo(self, p):
        '''void QRectF.moveTo(QPointF p)'''
    def translate(self, dx, dy):
        '''void QRectF.translate(float dx, float dy)'''
    def translate(self, p):
        '''void QRectF.translate(QPointF p)'''
    def size(self):
        '''QSizeF QRectF.size()'''
        return QSizeF()
    def height(self):
        '''float QRectF.height()'''
        return float()
    def width(self):
        '''float QRectF.width()'''
        return float()
    def moveCenter(self, p):
        '''void QRectF.moveCenter(QPointF p)'''
    def moveBottomRight(self, p):
        '''void QRectF.moveBottomRight(QPointF p)'''
    def moveBottomLeft(self, p):
        '''void QRectF.moveBottomLeft(QPointF p)'''
    def moveTopRight(self, p):
        '''void QRectF.moveTopRight(QPointF p)'''
    def moveTopLeft(self, p):
        '''void QRectF.moveTopLeft(QPointF p)'''
    def moveBottom(self, pos):
        '''void QRectF.moveBottom(float pos)'''
    def moveRight(self, pos):
        '''void QRectF.moveRight(float pos)'''
    def moveTop(self, pos):
        '''void QRectF.moveTop(float pos)'''
    def moveLeft(self, pos):
        '''void QRectF.moveLeft(float pos)'''
    def center(self):
        '''QPointF QRectF.center()'''
        return QPointF()
    def setBottomRight(self, p):
        '''void QRectF.setBottomRight(QPointF p)'''
    def setBottomLeft(self, p):
        '''void QRectF.setBottomLeft(QPointF p)'''
    def setTopRight(self, p):
        '''void QRectF.setTopRight(QPointF p)'''
    def setTopLeft(self, p):
        '''void QRectF.setTopLeft(QPointF p)'''
    def setBottom(self, pos):
        '''void QRectF.setBottom(float pos)'''
    def setTop(self, pos):
        '''void QRectF.setTop(float pos)'''
    def setRight(self, pos):
        '''void QRectF.setRight(float pos)'''
    def setLeft(self, pos):
        '''void QRectF.setLeft(float pos)'''
    def y(self):
        '''float QRectF.y()'''
        return float()
    def x(self):
        '''float QRectF.x()'''
        return float()
    def __bool__(self):
        '''int QRectF.__bool__()'''
        return int()
    def isValid(self):
        '''bool QRectF.isValid()'''
        return bool()
    def isEmpty(self):
        '''bool QRectF.isEmpty()'''
        return bool()
    def isNull(self):
        '''bool QRectF.isNull()'''
        return bool()
    def intersects(self, r):
        '''bool QRectF.intersects(QRectF r)'''
        return bool()
    def __contains__(self, p):
        '''int QRectF.__contains__(QPointF p)'''
        return int()
    def __contains__(self, r):
        '''int QRectF.__contains__(QRectF r)'''
        return int()
    def contains(self, p):
        '''bool QRectF.contains(QPointF p)'''
        return bool()
    def contains(self, r):
        '''bool QRectF.contains(QRectF r)'''
        return bool()
    def contains(self, ax, ay):
        '''bool QRectF.contains(float ax, float ay)'''
        return bool()
    def __and__(self, r):
        '''QRectF QRectF.__and__(QRectF r)'''
        return QRectF()
    def __or__(self, r):
        '''QRectF QRectF.__or__(QRectF r)'''
        return QRectF()
    def bottomLeft(self):
        '''QPointF QRectF.bottomLeft()'''
        return QPointF()
    def topRight(self):
        '''QPointF QRectF.topRight()'''
        return QPointF()
    def bottomRight(self):
        '''QPointF QRectF.bottomRight()'''
        return QPointF()
    def topLeft(self):
        '''QPointF QRectF.topLeft()'''
        return QPointF()
    def setY(self, pos):
        '''void QRectF.setY(float pos)'''
    def setX(self, pos):
        '''void QRectF.setX(float pos)'''
    def bottom(self):
        '''float QRectF.bottom()'''
        return float()
    def right(self):
        '''float QRectF.right()'''
        return float()
    def top(self):
        '''float QRectF.top()'''
        return float()
    def left(self):
        '''float QRectF.left()'''
        return float()
    def normalized(self):
        '''QRectF QRectF.normalized()'''
        return QRectF()
    def __repr__(self):
        '''str QRectF.__repr__()'''
        return str()


class QRegExp():
    """"""
    # Enum QRegExp.CaretMode
    CaretAtZero = 0
    CaretAtOffset = 0
    CaretWontMatch = 0

    # Enum QRegExp.PatternSyntax
    RegExp = 0
    RegExp2 = 0
    Wildcard = 0
    FixedString = 0
    WildcardUnix = 0
    W3CXmlSchema11 = 0

    def __init__(self):
        '''void QRegExp.__init__()'''
    def __init__(self, pattern, cs = Qt.CaseSensitive, syntax = QRegExp.RegExp):
        '''void QRegExp.__init__(QString pattern, Qt.CaseSensitivity cs = Qt.CaseSensitive, QRegExp.PatternSyntax syntax = QRegExp.RegExp)'''
    def __init__(self, rx):
        '''void QRegExp.__init__(QRegExp rx)'''
    def swap(self, other):
        '''void QRegExp.swap(QRegExp other)'''
    def captureCount(self):
        '''int QRegExp.captureCount()'''
        return int()
    def escape(self, str):
        '''static QString QRegExp.escape(QString str)'''
        return QString()
    def errorString(self):
        '''QString QRegExp.errorString()'''
        return QString()
    def pos(self, nth = 0):
        '''int QRegExp.pos(int nth = 0)'''
        return int()
    def cap(self, nth = 0):
        '''QString QRegExp.cap(int nth = 0)'''
        return QString()
    def capturedTexts(self):
        '''QStringList QRegExp.capturedTexts()'''
        return QStringList()
    def numCaptures(self):
        '''int QRegExp.numCaptures()'''
        return int()
    def matchedLength(self):
        '''int QRegExp.matchedLength()'''
        return int()
    def lastIndexIn(self, str, offset = -1, caretMode = QRegExp.CaretAtZero):
        '''int QRegExp.lastIndexIn(QString str, int offset = -1, QRegExp.CaretMode caretMode = QRegExp.CaretAtZero)'''
        return int()
    def indexIn(self, str, offset = 0, caretMode = QRegExp.CaretAtZero):
        '''int QRegExp.indexIn(QString str, int offset = 0, QRegExp.CaretMode caretMode = QRegExp.CaretAtZero)'''
        return int()
    def exactMatch(self, str):
        '''bool QRegExp.exactMatch(QString str)'''
        return bool()
    def setMinimal(self, minimal):
        '''void QRegExp.setMinimal(bool minimal)'''
    def isMinimal(self):
        '''bool QRegExp.isMinimal()'''
        return bool()
    def setPatternSyntax(self, syntax):
        '''void QRegExp.setPatternSyntax(QRegExp.PatternSyntax syntax)'''
    def patternSyntax(self):
        '''QRegExp.PatternSyntax QRegExp.patternSyntax()'''
        return QRegExp.PatternSyntax()
    def setCaseSensitivity(self, cs):
        '''void QRegExp.setCaseSensitivity(Qt.CaseSensitivity cs)'''
    def caseSensitivity(self):
        '''Qt.CaseSensitivity QRegExp.caseSensitivity()'''
        return Qt.CaseSensitivity()
    def setPattern(self, pattern):
        '''void QRegExp.setPattern(QString pattern)'''
    def pattern(self):
        '''QString QRegExp.pattern()'''
        return QString()
    def isValid(self):
        '''bool QRegExp.isValid()'''
        return bool()
    def isEmpty(self):
        '''bool QRegExp.isEmpty()'''
        return bool()
    def __ne__(self, rx):
        '''bool QRegExp.__ne__(QRegExp rx)'''
        return bool()
    def __eq__(self, rx):
        '''bool QRegExp.__eq__(QRegExp rx)'''
        return bool()
    def __repr__(self):
        '''str QRegExp.__repr__()'''
        return str()


class QResource():
    """"""
    def __init__(self, fileName = QString(), locale = QLocale()):
        '''void QResource.__init__(QString fileName = QString(), QLocale locale = QLocale())'''
    def isFile(self):
        '''bool QResource.isFile()'''
        return bool()
    def isDir(self):
        '''bool QResource.isDir()'''
        return bool()
    def children(self):
        '''QStringList QResource.children()'''
        return QStringList()
    def unregisterResourceData(self, rccData, mapRoot = QString()):
        '''static bool QResource.unregisterResourceData(str rccData, QString mapRoot = QString())'''
        return bool()
    def unregisterResource(self, rccFileName, mapRoot = QString()):
        '''static bool QResource.unregisterResource(QString rccFileName, QString mapRoot = QString())'''
        return bool()
    def searchPaths(self):
        '''static QStringList QResource.searchPaths()'''
        return QStringList()
    def registerResourceData(self, rccData, mapRoot = QString()):
        '''static bool QResource.registerResourceData(str rccData, QString mapRoot = QString())'''
        return bool()
    def registerResource(self, rccFileName, mapRoot = QString()):
        '''static bool QResource.registerResource(QString rccFileName, QString mapRoot = QString())'''
        return bool()
    def addSearchPath(self, path):
        '''static void QResource.addSearchPath(QString path)'''
    def size(self):
        '''int QResource.size()'''
        return int()
    def setLocale(self, locale):
        '''void QResource.setLocale(QLocale locale)'''
    def setFileName(self, file):
        '''void QResource.setFileName(QString file)'''
    def locale(self):
        '''QLocale QResource.locale()'''
        return QLocale()
    def isValid(self):
        '''bool QResource.isValid()'''
        return bool()
    def isCompressed(self):
        '''bool QResource.isCompressed()'''
        return bool()
    def fileName(self):
        '''QString QResource.fileName()'''
        return QString()
    def data(self):
        '''str QResource.data()'''
        return str()
    def absoluteFilePath(self):
        '''QString QResource.absoluteFilePath()'''
        return QString()


class QRunnable():
    """"""
    def __init__(self):
        '''void QRunnable.__init__()'''
    def __init__(self):
        '''QRunnable QRunnable.__init__()'''
        return QRunnable()
    def setAutoDelete(self, _autoDelete):
        '''void QRunnable.setAutoDelete(bool _autoDelete)'''
    def autoDelete(self):
        '''bool QRunnable.autoDelete()'''
        return bool()
    def run(self):
        '''abstract void QRunnable.run()'''


class QSemaphore():
    """"""
    def __init__(self, n = 0):
        '''void QSemaphore.__init__(int n = 0)'''
    def available(self):
        '''int QSemaphore.available()'''
        return int()
    def release(self, n = 1):
        '''void QSemaphore.release(int n = 1)'''
    def tryAcquire(self, n = 1):
        '''bool QSemaphore.tryAcquire(int n = 1)'''
        return bool()
    def tryAcquire(self, n, timeout):
        '''bool QSemaphore.tryAcquire(int n, int timeout)'''
        return bool()
    def acquire(self, n = 1):
        '''void QSemaphore.acquire(int n = 1)'''


class QSequentialAnimationGroup(QAnimationGroup):
    """"""
    def __init__(self, parent = None):
        '''void QSequentialAnimationGroup.__init__(QObject parent = None)'''
    def updateDirection(self, direction):
        '''void QSequentialAnimationGroup.updateDirection(QAbstractAnimation.Direction direction)'''
    def updateState(self, newState, oldState):
        '''void QSequentialAnimationGroup.updateState(QAbstractAnimation.State newState, QAbstractAnimation.State oldState)'''
    def updateCurrentTime(self):
        '''int QSequentialAnimationGroup.updateCurrentTime()'''
        return int()
    def event(self, event):
        '''bool QSequentialAnimationGroup.event(QEvent event)'''
        return bool()
    currentAnimationChanged = pyqtSignal() # void currentAnimationChanged(QAbstractAnimation *) - signal
    def duration(self):
        '''int QSequentialAnimationGroup.duration()'''
        return int()
    def currentAnimation(self):
        '''QAbstractAnimation QSequentialAnimationGroup.currentAnimation()'''
        return QAbstractAnimation()
    def insertPause(self, index, msecs):
        '''QPauseAnimation QSequentialAnimationGroup.insertPause(int index, int msecs)'''
        return QPauseAnimation()
    def addPause(self, msecs):
        '''QPauseAnimation QSequentialAnimationGroup.addPause(int msecs)'''
        return QPauseAnimation()


class QSettings(QObject):
    """"""
    # Enum QSettings.Scope
    UserScope = 0
    SystemScope = 0

    # Enum QSettings.Format
    NativeFormat = 0
    IniFormat = 0
    InvalidFormat = 0

    # Enum QSettings.Status
    NoError = 0
    AccessError = 0
    FormatError = 0

    def __init__(self, organization, application = QString(), parent = None):
        '''void QSettings.__init__(QString organization, QString application = QString(), QObject parent = None)'''
    def __init__(self, scope, organization, application = QString(), parent = None):
        '''void QSettings.__init__(QSettings.Scope scope, QString organization, QString application = QString(), QObject parent = None)'''
    def __init__(self, format, scope, organization, application = QString(), parent = None):
        '''void QSettings.__init__(QSettings.Format format, QSettings.Scope scope, QString organization, QString application = QString(), QObject parent = None)'''
    def __init__(self, fileName, format, parent = None):
        '''void QSettings.__init__(QString fileName, QSettings.Format format, QObject parent = None)'''
    def __init__(self, parent = None):
        '''void QSettings.__init__(QObject parent = None)'''
    def event(self, event):
        '''bool QSettings.event(QEvent event)'''
        return bool()
    def iniCodec(self):
        '''QTextCodec QSettings.iniCodec()'''
        return QTextCodec()
    def setIniCodec(self, codec):
        '''void QSettings.setIniCodec(QTextCodec codec)'''
    def setIniCodec(self, codecName):
        '''void QSettings.setIniCodec(str codecName)'''
    def defaultFormat(self):
        '''static QSettings.Format QSettings.defaultFormat()'''
        return QSettings.Format()
    def setDefaultFormat(self, format):
        '''static void QSettings.setDefaultFormat(QSettings.Format format)'''
    def applicationName(self):
        '''QString QSettings.applicationName()'''
        return QString()
    def organizationName(self):
        '''QString QSettings.organizationName()'''
        return QString()
    def scope(self):
        '''QSettings.Scope QSettings.scope()'''
        return QSettings.Scope()
    def format(self):
        '''QSettings.Format QSettings.format()'''
        return QSettings.Format()
    def setPath(self, format, scope, path):
        '''static void QSettings.setPath(QSettings.Format format, QSettings.Scope scope, QString path)'''
    def setUserIniPath(self, dir):
        '''static void QSettings.setUserIniPath(QString dir)'''
    def setSystemIniPath(self, dir):
        '''static void QSettings.setSystemIniPath(QString dir)'''
    def fileName(self):
        '''QString QSettings.fileName()'''
        return QString()
    def fallbacksEnabled(self):
        '''bool QSettings.fallbacksEnabled()'''
        return bool()
    def setFallbacksEnabled(self, b):
        '''void QSettings.setFallbacksEnabled(bool b)'''
    def contains(self, key):
        '''bool QSettings.contains(QString key)'''
        return bool()
    def remove(self, key):
        '''void QSettings.remove(QString key)'''
    def value(self, key, defaultValue = QVariant(), type = None):
        '''object QSettings.value(QString key, QVariant defaultValue = QVariant(), object type = None)'''
        return object()
    def setValue(self, key, value):
        '''void QSettings.setValue(QString key, QVariant value)'''
    def isWritable(self):
        '''bool QSettings.isWritable()'''
        return bool()
    def childGroups(self):
        '''QStringList QSettings.childGroups()'''
        return QStringList()
    def childKeys(self):
        '''QStringList QSettings.childKeys()'''
        return QStringList()
    def allKeys(self):
        '''QStringList QSettings.allKeys()'''
        return QStringList()
    def setArrayIndex(self, i):
        '''void QSettings.setArrayIndex(int i)'''
    def endArray(self):
        '''void QSettings.endArray()'''
    def beginWriteArray(self, prefix, size = -1):
        '''void QSettings.beginWriteArray(QString prefix, int size = -1)'''
    def beginReadArray(self, prefix):
        '''int QSettings.beginReadArray(QString prefix)'''
        return int()
    def group(self):
        '''QString QSettings.group()'''
        return QString()
    def endGroup(self):
        '''void QSettings.endGroup()'''
    def beginGroup(self, prefix):
        '''void QSettings.beginGroup(QString prefix)'''
    def status(self):
        '''QSettings.Status QSettings.status()'''
        return QSettings.Status()
    def sync(self):
        '''void QSettings.sync()'''
    def clear(self):
        '''void QSettings.clear()'''


class QSharedMemory(QObject):
    """"""
    # Enum QSharedMemory.SharedMemoryError
    NoError = 0
    PermissionDenied = 0
    InvalidSize = 0
    KeyError = 0
    AlreadyExists = 0
    NotFound = 0
    LockError = 0
    OutOfResources = 0
    UnknownError = 0

    # Enum QSharedMemory.AccessMode
    ReadOnly = 0
    ReadWrite = 0

    def __init__(self, parent = None):
        '''void QSharedMemory.__init__(QObject parent = None)'''
    def __init__(self, key, parent = None):
        '''void QSharedMemory.__init__(QString key, QObject parent = None)'''
    def nativeKey(self):
        '''QString QSharedMemory.nativeKey()'''
        return QString()
    def setNativeKey(self, key):
        '''void QSharedMemory.setNativeKey(QString key)'''
    def errorString(self):
        '''QString QSharedMemory.errorString()'''
        return QString()
    def error(self):
        '''QSharedMemory.SharedMemoryError QSharedMemory.error()'''
        return QSharedMemory.SharedMemoryError()
    def unlock(self):
        '''bool QSharedMemory.unlock()'''
        return bool()
    def lock(self):
        '''bool QSharedMemory.lock()'''
        return bool()
    def constData(self):
        '''sip.voidptr QSharedMemory.constData()'''
        return sip.voidptr()
    def data(self):
        '''sip.voidptr QSharedMemory.data()'''
        return sip.voidptr()
    def detach(self):
        '''bool QSharedMemory.detach()'''
        return bool()
    def isAttached(self):
        '''bool QSharedMemory.isAttached()'''
        return bool()
    def attach(self, mode = QSharedMemory.ReadWrite):
        '''bool QSharedMemory.attach(QSharedMemory.AccessMode mode = QSharedMemory.ReadWrite)'''
        return bool()
    def size(self):
        '''int QSharedMemory.size()'''
        return int()
    def create(self, size, mode = QSharedMemory.ReadWrite):
        '''bool QSharedMemory.create(int size, QSharedMemory.AccessMode mode = QSharedMemory.ReadWrite)'''
        return bool()
    def key(self):
        '''QString QSharedMemory.key()'''
        return QString()
    def setKey(self, key):
        '''void QSharedMemory.setKey(QString key)'''


class QSignalMapper(QObject):
    """"""
    def __init__(self, parent = None):
        '''void QSignalMapper.__init__(QObject parent = None)'''
    def map(self):
        '''void QSignalMapper.map()'''
    def map(self, sender):
        '''void QSignalMapper.map(QObject sender)'''
    mapped = pyqtSignal() # void mapped(int) - signal
    mapped = pyqtSignal() # void mapped(const QString&) - signal
    mapped = pyqtSignal() # void mapped(QWidget *) - signal
    mapped = pyqtSignal() # void mapped(QObject *) - signal
    def mapping(self, id):
        '''QObject QSignalMapper.mapping(int id)'''
        return QObject()
    def mapping(self, text):
        '''QObject QSignalMapper.mapping(QString text)'''
        return QObject()
    def mapping(self, widget):
        '''QObject QSignalMapper.mapping(QWidget widget)'''
        return QObject()
    def mapping(self, object):
        '''QObject QSignalMapper.mapping(QObject object)'''
        return QObject()
    def removeMappings(self, sender):
        '''void QSignalMapper.removeMappings(QObject sender)'''
    def setMapping(self, sender, id):
        '''void QSignalMapper.setMapping(QObject sender, int id)'''
    def setMapping(self, sender, text):
        '''void QSignalMapper.setMapping(QObject sender, QString text)'''
    def setMapping(self, sender, widget):
        '''void QSignalMapper.setMapping(QObject sender, QWidget widget)'''
    def setMapping(self, sender, object):
        '''void QSignalMapper.setMapping(QObject sender, QObject object)'''


class QSignalTransition(QAbstractTransition):
    """"""
    def __init__(self, sourceState = None):
        '''void QSignalTransition.__init__(QState sourceState = None)'''
    def __init__(self, sender, signal, sourceState = None):
        '''void QSignalTransition.__init__(QObject sender, SIGNAL() signal, QState sourceState = None)'''
    def __init__(self, signal, sourceState = None):
        '''void QSignalTransition.__init__(signal signal, QState sourceState = None)'''
    def event(self, e):
        '''bool QSignalTransition.event(QEvent e)'''
        return bool()
    def onTransition(self, event):
        '''void QSignalTransition.onTransition(QEvent event)'''
    def eventTest(self, event):
        '''bool QSignalTransition.eventTest(QEvent event)'''
        return bool()
    def setSignal(self, signal):
        '''void QSignalTransition.setSignal(QByteArray signal)'''
    def signal(self):
        '''QByteArray QSignalTransition.signal()'''
        return QByteArray()
    def setSenderObject(self, sender):
        '''void QSignalTransition.setSenderObject(QObject sender)'''
    def senderObject(self):
        '''QObject QSignalTransition.senderObject()'''
        return QObject()


class QSize():
    """"""
    def __init__(self):
        '''void QSize.__init__()'''
    def __init__(self, w, h):
        '''void QSize.__init__(int w, int h)'''
    def __init__(self):
        '''QSize QSize.__init__()'''
        return QSize()
    def __eq__(self, s2):
        '''bool QSize.__eq__(QSize s2)'''
        return bool()
    def __ne__(self, s2):
        '''bool QSize.__ne__(QSize s2)'''
        return bool()
    def __add__(self, s2):
        '''QSize QSize.__add__(QSize s2)'''
        return QSize()
    def __sub__(self, s2):
        '''QSize QSize.__sub__(QSize s2)'''
        return QSize()
    def __mul__(self, c):
        '''QSize QSize.__mul__(float c)'''
        return QSize()
    def __mul__(self, s):
        '''QSize QSize.__mul__(QSize s)'''
        return QSize()
    def __div__(self, c):
        '''QSize QSize.__div__(float c)'''
        return QSize()
    def boundedTo(self, otherSize):
        '''QSize QSize.boundedTo(QSize otherSize)'''
        return QSize()
    def expandedTo(self, otherSize):
        '''QSize QSize.expandedTo(QSize otherSize)'''
        return QSize()
    def __idiv__(self, c):
        '''QSize QSize.__idiv__(float c)'''
        return QSize()
    def __imul__(self, c):
        '''QSize QSize.__imul__(float c)'''
        return QSize()
    def __isub__(self, s):
        '''QSize QSize.__isub__(QSize s)'''
        return QSize()
    def __iadd__(self, s):
        '''QSize QSize.__iadd__(QSize s)'''
        return QSize()
    def setHeight(self, h):
        '''void QSize.setHeight(int h)'''
    def setWidth(self, w):
        '''void QSize.setWidth(int w)'''
    def height(self):
        '''int QSize.height()'''
        return int()
    def width(self):
        '''int QSize.width()'''
        return int()
    def __bool__(self):
        '''int QSize.__bool__()'''
        return int()
    def isValid(self):
        '''bool QSize.isValid()'''
        return bool()
    def isEmpty(self):
        '''bool QSize.isEmpty()'''
        return bool()
    def isNull(self):
        '''bool QSize.isNull()'''
        return bool()
    def __repr__(self):
        '''str QSize.__repr__()'''
        return str()
    def scale(self, s, mode):
        '''void QSize.scale(QSize s, Qt.AspectRatioMode mode)'''
    def scale(self, w, h, mode):
        '''void QSize.scale(int w, int h, Qt.AspectRatioMode mode)'''
    def transpose(self):
        '''void QSize.transpose()'''


class QSizeF():
    """"""
    def __init__(self):
        '''void QSizeF.__init__()'''
    def __init__(self, sz):
        '''void QSizeF.__init__(QSize sz)'''
    def __init__(self, w, h):
        '''void QSizeF.__init__(float w, float h)'''
    def __init__(self):
        '''QSizeF QSizeF.__init__()'''
        return QSizeF()
    def __eq__(self, s2):
        '''bool QSizeF.__eq__(QSizeF s2)'''
        return bool()
    def __ne__(self, s2):
        '''bool QSizeF.__ne__(QSizeF s2)'''
        return bool()
    def __add__(self, s2):
        '''QSizeF QSizeF.__add__(QSizeF s2)'''
        return QSizeF()
    def __sub__(self, s2):
        '''QSizeF QSizeF.__sub__(QSizeF s2)'''
        return QSizeF()
    def __mul__(self, c):
        '''QSizeF QSizeF.__mul__(float c)'''
        return QSizeF()
    def __mul__(self, s):
        '''QSizeF QSizeF.__mul__(QSizeF s)'''
        return QSizeF()
    def __div__(self, c):
        '''QSizeF QSizeF.__div__(float c)'''
        return QSizeF()
    def toSize(self):
        '''QSize QSizeF.toSize()'''
        return QSize()
    def boundedTo(self, otherSize):
        '''QSizeF QSizeF.boundedTo(QSizeF otherSize)'''
        return QSizeF()
    def expandedTo(self, otherSize):
        '''QSizeF QSizeF.expandedTo(QSizeF otherSize)'''
        return QSizeF()
    def __idiv__(self, c):
        '''QSizeF QSizeF.__idiv__(float c)'''
        return QSizeF()
    def __imul__(self, c):
        '''QSizeF QSizeF.__imul__(float c)'''
        return QSizeF()
    def __isub__(self, s):
        '''QSizeF QSizeF.__isub__(QSizeF s)'''
        return QSizeF()
    def __iadd__(self, s):
        '''QSizeF QSizeF.__iadd__(QSizeF s)'''
        return QSizeF()
    def setHeight(self, h):
        '''void QSizeF.setHeight(float h)'''
    def setWidth(self, w):
        '''void QSizeF.setWidth(float w)'''
    def height(self):
        '''float QSizeF.height()'''
        return float()
    def width(self):
        '''float QSizeF.width()'''
        return float()
    def __bool__(self):
        '''int QSizeF.__bool__()'''
        return int()
    def isValid(self):
        '''bool QSizeF.isValid()'''
        return bool()
    def isEmpty(self):
        '''bool QSizeF.isEmpty()'''
        return bool()
    def isNull(self):
        '''bool QSizeF.isNull()'''
        return bool()
    def __repr__(self):
        '''str QSizeF.__repr__()'''
        return str()
    def scale(self, s, mode):
        '''void QSizeF.scale(QSizeF s, Qt.AspectRatioMode mode)'''
    def scale(self, w, h, mode):
        '''void QSizeF.scale(float w, float h, Qt.AspectRatioMode mode)'''
    def transpose(self):
        '''void QSizeF.transpose()'''


class QSocketNotifier(QObject):
    """"""
    # Enum QSocketNotifier.Type
    Read = 0
    Write = 0
    Exception = 0

    def __init__(self, socket, type, parent = None):
        '''void QSocketNotifier.__init__(int socket, QSocketNotifier.Type type, QObject parent = None)'''
    def event(self):
        '''QEvent QSocketNotifier.event()'''
        return QEvent()
    activated = pyqtSignal() # void activated(int) - signal
    def setEnabled(self):
        '''bool QSocketNotifier.setEnabled()'''
        return bool()
    def isEnabled(self):
        '''bool QSocketNotifier.isEnabled()'''
        return bool()
    def type(self):
        '''QSocketNotifier.Type QSocketNotifier.type()'''
        return QSocketNotifier.Type()
    def socket(self):
        '''int QSocketNotifier.socket()'''
        return int()


class QState(QAbstractState):
    """"""
    # Enum QState.ChildMode
    ExclusiveStates = 0
    ParallelStates = 0

    def __init__(self, parent = None):
        '''void QState.__init__(QState parent = None)'''
    def __init__(self, childMode, parent = None):
        '''void QState.__init__(QState.ChildMode childMode, QState parent = None)'''
    def event(self, e):
        '''bool QState.event(QEvent e)'''
        return bool()
    def onExit(self, event):
        '''void QState.onExit(QEvent event)'''
    def onEntry(self, event):
        '''void QState.onEntry(QEvent event)'''
    propertiesAssigned = pyqtSignal() # void propertiesAssigned() - signal
    finished = pyqtSignal() # void finished() - signal
    def assignProperty(self, object, name, value):
        '''void QState.assignProperty(QObject object, str name, QVariant value)'''
    def setChildMode(self, mode):
        '''void QState.setChildMode(QState.ChildMode mode)'''
    def childMode(self):
        '''QState.ChildMode QState.childMode()'''
        return QState.ChildMode()
    def setInitialState(self, state):
        '''void QState.setInitialState(QAbstractState state)'''
    def initialState(self):
        '''QAbstractState QState.initialState()'''
        return QAbstractState()
    def transitions(self):
        '''list-of-QAbstractTransition QState.transitions()'''
        return [QAbstractTransition()]
    def removeTransition(self, transition):
        '''void QState.removeTransition(QAbstractTransition transition)'''
    def addTransition(self, transition):
        '''void QState.addTransition(QAbstractTransition transition)'''
    def addTransition(self, sender, signal, target):
        '''QSignalTransition QState.addTransition(QObject sender, SIGNAL() signal, QAbstractState target)'''
        return QSignalTransition()
    def addTransition(self, signal, target):
        '''QSignalTransition QState.addTransition(signal signal, QAbstractState target)'''
        return QSignalTransition()
    def addTransition(self, target):
        '''QAbstractTransition QState.addTransition(QAbstractState target)'''
        return QAbstractTransition()
    def setErrorState(self, state):
        '''void QState.setErrorState(QAbstractState state)'''
    def errorState(self):
        '''QAbstractState QState.errorState()'''
        return QAbstractState()


class QStateMachine(QState):
    """"""
    # Enum QStateMachine.Error
    NoError = 0
    NoInitialStateError = 0
    NoDefaultStateInHistoryStateError = 0
    NoCommonAncestorForTransitionError = 0

    # Enum QStateMachine.RestorePolicy
    DontRestoreProperties = 0
    RestoreProperties = 0

    # Enum QStateMachine.EventPriority
    NormalPriority = 0
    HighPriority = 0

    def __init__(self, parent = None):
        '''void QStateMachine.__init__(QObject parent = None)'''
    def event(self, e):
        '''bool QStateMachine.event(QEvent e)'''
        return bool()
    def onExit(self, event):
        '''void QStateMachine.onExit(QEvent event)'''
    def onEntry(self, event):
        '''void QStateMachine.onEntry(QEvent event)'''
    stopped = pyqtSignal() # void stopped() - signal
    started = pyqtSignal() # void started() - signal
    def stop(self):
        '''void QStateMachine.stop()'''
    def start(self):
        '''void QStateMachine.start()'''
    def eventFilter(self, watched, event):
        '''bool QStateMachine.eventFilter(QObject watched, QEvent event)'''
        return bool()
    def configuration(self):
        '''list-of-QAbstractState QStateMachine.configuration()'''
        return [QAbstractState()]
    def cancelDelayedEvent(self, id):
        '''bool QStateMachine.cancelDelayedEvent(int id)'''
        return bool()
    def postDelayedEvent(self, event, delay):
        '''int QStateMachine.postDelayedEvent(QEvent event, int delay)'''
        return int()
    def postEvent(self, event, priority = QStateMachine.NormalPriority):
        '''void QStateMachine.postEvent(QEvent event, QStateMachine.EventPriority priority = QStateMachine.NormalPriority)'''
    def setGlobalRestorePolicy(self, restorePolicy):
        '''void QStateMachine.setGlobalRestorePolicy(QStateMachine.RestorePolicy restorePolicy)'''
    def globalRestorePolicy(self):
        '''QStateMachine.RestorePolicy QStateMachine.globalRestorePolicy()'''
        return QStateMachine.RestorePolicy()
    def removeDefaultAnimation(self, animation):
        '''void QStateMachine.removeDefaultAnimation(QAbstractAnimation animation)'''
    def defaultAnimations(self):
        '''list-of-QAbstractAnimation QStateMachine.defaultAnimations()'''
        return [QAbstractAnimation()]
    def addDefaultAnimation(self, animation):
        '''void QStateMachine.addDefaultAnimation(QAbstractAnimation animation)'''
    def setAnimated(self, enabled):
        '''void QStateMachine.setAnimated(bool enabled)'''
    def isAnimated(self):
        '''bool QStateMachine.isAnimated()'''
        return bool()
    def isRunning(self):
        '''bool QStateMachine.isRunning()'''
        return bool()
    def clearError(self):
        '''void QStateMachine.clearError()'''
    def errorString(self):
        '''QString QStateMachine.errorString()'''
        return QString()
    def error(self):
        '''QStateMachine.Error QStateMachine.error()'''
        return QStateMachine.Error()
    def removeState(self, state):
        '''void QStateMachine.removeState(QAbstractState state)'''
    def addState(self, state):
        '''void QStateMachine.addState(QAbstractState state)'''
    class WrappedEvent(QEvent):
        """"""
        def event(self):
            '''QEvent QStateMachine.WrappedEvent.event()'''
            return QEvent()
        def object(self):
            '''QObject QStateMachine.WrappedEvent.object()'''
            return QObject()
    class SignalEvent(QEvent):
        """"""
        def arguments(self):
            '''list-of-QVariant QStateMachine.SignalEvent.arguments()'''
            return [QVariant()]
        def signalIndex(self):
            '''int QStateMachine.SignalEvent.signalIndex()'''
            return int()
        def sender(self):
            '''QObject QStateMachine.SignalEvent.sender()'''
            return QObject()


class QString():
    """"""
    # Enum QString.NormalizationForm
    NormalizationForm_D = 0
    NormalizationForm_C = 0
    NormalizationForm_KD = 0
    NormalizationForm_KC = 0

    # Enum QString.SplitBehavior
    KeepEmptyParts = 0
    SkipEmptyParts = 0

    # Enum QString.SectionFlag
    SectionDefault = 0
    SectionSkipEmpty = 0
    SectionIncludeLeadingSep = 0
    SectionIncludeTrailingSep = 0
    SectionCaseInsensitiveSeps = 0

    def __init__(self):
        '''void QString.__init__()'''
    def __init__(self, size, c):
        '''void QString.__init__(int size, QChar c)'''
    def __init__(self, s):
        '''void QString.__init__(QString s)'''
    def __init__(self, a):
        '''void QString.__init__(QByteArray a)'''
    def __init__(self):
        '''QUuid QString.__init__()'''
        return QUuid()
    def __add__(self, s2):
        '''QString QString.__add__(QString s2)'''
        return QString()
    def __add__(self, ba):
        '''QString QString.__add__(QByteArray ba)'''
        return QString()
    def swap(self, other):
        '''void QString.swap(QString other)'''
    def repeated(self, times):
        '''QString QString.repeated(int times)'''
        return QString()
    def toCaseFolded(self):
        '''QString QString.toCaseFolded()'''
        return QString()
    def reserve(self, asize):
        '''void QString.reserve(int asize)'''
    def capacity(self):
        '''int QString.capacity()'''
        return int()
    def clear(self):
        '''void QString.clear()'''
    def isEmpty(self):
        '''bool QString.isEmpty()'''
        return bool()
    def __imul__(self, m):
        '''QString QString.__imul__(int m)'''
        return QString()
    def __mul__(self, m):
        '''QString QString.__mul__(int m)'''
        return QString()
    def __hash__(self):
        '''int QString.__hash__()'''
        return int()
    def __str__(self):
        '''str QString.__str__()'''
        return str()
    def __unicode__(self):
        '''unicode QString.__unicode__()'''
        return unicode()
    def __contains__(self, s):
        '''int QString.__contains__(QString s)'''
        return int()
    def __getitem__(self, i):
        '''QString QString.__getitem__(int i)'''
        return QString()
    def __getitem__(self, slice):
        '''QString QString.__getitem__(slice slice)'''
        return QString()
    def at(self, i):
        '''QChar QString.at(int i)'''
        return QChar()
    def length(self):
        '''int QString.length()'''
        return int()
    def isRightToLeft(self):
        '''bool QString.isRightToLeft()'''
        return bool()
    def isSimpleText(self):
        '''bool QString.isSimpleText()'''
        return bool()
    def isNull(self):
        '''bool QString.isNull()'''
        return bool()
    def push_front(self, s):
        '''void QString.push_front(QString s)'''
    def push_back(self, s):
        '''void QString.push_back(QString s)'''
    def __ge__(self, s):
        '''bool QString.__ge__(QString s)'''
        return bool()
    def __ge__(self, s):
        '''bool QString.__ge__(QLatin1String s)'''
        return bool()
    def __ge__(self, s):
        '''bool QString.__ge__(QByteArray s)'''
        return bool()
    def __le__(self, s):
        '''bool QString.__le__(QString s)'''
        return bool()
    def __le__(self, s):
        '''bool QString.__le__(QLatin1String s)'''
        return bool()
    def __le__(self, s):
        '''bool QString.__le__(QByteArray s)'''
        return bool()
    def __ne__(self, s):
        '''bool QString.__ne__(QString s)'''
        return bool()
    def __ne__(self, s):
        '''bool QString.__ne__(QLatin1String s)'''
        return bool()
    def __ne__(self, s):
        '''bool QString.__ne__(QByteArray s)'''
        return bool()
    def __ne__(self, s2):
        '''bool QString.__ne__(QStringRef s2)'''
        return bool()
    def __gt__(self, s):
        '''bool QString.__gt__(QString s)'''
        return bool()
    def __gt__(self, s):
        '''bool QString.__gt__(QLatin1String s)'''
        return bool()
    def __gt__(self, s):
        '''bool QString.__gt__(QByteArray s)'''
        return bool()
    def __lt__(self, s):
        '''bool QString.__lt__(QString s)'''
        return bool()
    def __lt__(self, s):
        '''bool QString.__lt__(QLatin1String s)'''
        return bool()
    def __lt__(self, s):
        '''bool QString.__lt__(QByteArray s)'''
        return bool()
    def __eq__(self, s):
        '''bool QString.__eq__(QString s)'''
        return bool()
    def __eq__(self, s):
        '''bool QString.__eq__(QLatin1String s)'''
        return bool()
    def __eq__(self, s):
        '''bool QString.__eq__(QByteArray s)'''
        return bool()
    def __eq__(self, s2):
        '''bool QString.__eq__(QStringRef s2)'''
        return bool()
    def number(self, n, base = 10):
        '''static QString QString.number(int n, int base = 10)'''
        return QString()
    def number(self, n, format = 'g', precision = 6):
        '''static QString QString.number(float n, str format = 'g', int precision = 6)'''
        return QString()
    def number(self, n, base = 10):
        '''static QString QString.number(int n, int base = 10)'''
        return QString()
    def number(self, n, base = 10):
        '''static QString QString.number(int n, int base = 10)'''
        return QString()
    def setNum(self, n, base = 10):
        '''QString QString.setNum(int n, int base = 10)'''
        return QString()
    def setNum(self, n, format = 'g', precision = 6):
        '''QString QString.setNum(float n, str format = 'g', int precision = 6)'''
        return QString()
    def setNum(self, n, base = 10):
        '''QString QString.setNum(int n, int base = 10)'''
        return QString()
    def setNum(self, n, base = 10):
        '''QString QString.setNum(int n, int base = 10)'''
        return QString()
    def toDouble(self, ok):
        '''float QString.toDouble(bool ok)'''
        return float()
    def toFloat(self, ok):
        '''float QString.toFloat(bool ok)'''
        return float()
    def toULongLong(self, ok, base = 10):
        '''int QString.toULongLong(bool ok, int base = 10)'''
        return int()
    def toLongLong(self, ok, base = 10):
        '''int QString.toLongLong(bool ok, int base = 10)'''
        return int()
    def toULong(self, ok, base = 10):
        '''int QString.toULong(bool ok, int base = 10)'''
        return int()
    def toLong(self, ok, base = 10):
        '''int QString.toLong(bool ok, int base = 10)'''
        return int()
    def toUInt(self, ok, base = 10):
        '''int QString.toUInt(bool ok, int base = 10)'''
        return int()
    def toInt(self, ok, base = 10):
        '''int QString.toInt(bool ok, int base = 10)'''
        return int()
    def toUShort(self, ok, base = 10):
        '''int QString.toUShort(bool ok, int base = 10)'''
        return int()
    def toShort(self, ok, base = 10):
        '''int QString.toShort(bool ok, int base = 10)'''
        return int()
    def localeAwareCompare(self, s):
        '''int QString.localeAwareCompare(QString s)'''
        return int()
    def localeAwareCompare(self, s):
        '''int QString.localeAwareCompare(QStringRef s)'''
        return int()
    def localeAwareCompare(self, s1, s2):
        '''static int QString.localeAwareCompare(QString s1, QString s2)'''
        return int()
    def localeAwareCompare(self, s1, s2):
        '''static int QString.localeAwareCompare(QString s1, QStringRef s2)'''
        return int()
    def compare(self, s):
        '''int QString.compare(QString s)'''
        return int()
    def compare(self, s, cs):
        '''int QString.compare(QString s, Qt.CaseSensitivity cs)'''
        return int()
    def compare(self, other, cs = Qt.CaseSensitive):
        '''int QString.compare(QLatin1String other, Qt.CaseSensitivity cs = Qt.CaseSensitive)'''
        return int()
    def compare(self, ref, cs = Qt.CaseSensitive):
        '''int QString.compare(QStringRef ref, Qt.CaseSensitivity cs = Qt.CaseSensitive)'''
        return int()
    def compare(self, s1, s2):
        '''static int QString.compare(QString s1, QString s2)'''
        return int()
    def compare(self, s1, s2, cs):
        '''static int QString.compare(QString s1, QString s2, Qt.CaseSensitivity cs)'''
        return int()
    def compare(self, s1, s2, cs = Qt.CaseSensitive):
        '''static int QString.compare(QString s1, QLatin1String s2, Qt.CaseSensitivity cs = Qt.CaseSensitive)'''
        return int()
    def compare(self, s1, s2, cs = Qt.CaseSensitive):
        '''static int QString.compare(QLatin1String s1, QString s2, Qt.CaseSensitivity cs = Qt.CaseSensitive)'''
        return int()
    def compare(self, s1, s2, cs = Qt.CaseSensitive):
        '''static int QString.compare(QString s1, QStringRef s2, Qt.CaseSensitivity cs = Qt.CaseSensitive)'''
        return int()
    def fromLocal8Bit(self, str, size = -1):
        '''static QString QString.fromLocal8Bit(str str, int size = -1)'''
        return QString()
    def fromUtf8(self, str, size = -1):
        '''static QString QString.fromUtf8(str str, int size = -1)'''
        return QString()
    def fromLatin1(self, str, size = -1):
        '''static QString QString.fromLatin1(str str, int size = -1)'''
        return QString()
    def fromAscii(self, str, size = -1):
        '''static QString QString.fromAscii(str str, int size = -1)'''
        return QString()
    def toLocal8Bit(self):
        '''QByteArray QString.toLocal8Bit()'''
        return QByteArray()
    def toUtf8(self):
        '''QByteArray QString.toUtf8()'''
        return QByteArray()
    def toLatin1(self):
        '''QByteArray QString.toLatin1()'''
        return QByteArray()
    def toAscii(self):
        '''QByteArray QString.toAscii()'''
        return QByteArray()
    def normalized(self, mode):
        '''QString QString.normalized(QString.NormalizationForm mode)'''
        return QString()
    def normalized(self, mode, version):
        '''QString QString.normalized(QString.NormalizationForm mode, QChar.UnicodeVersion version)'''
        return QString()
    def split(self, sep, behavior = QString.KeepEmptyParts, cs = Qt.CaseSensitive):
        '''QStringList QString.split(QString sep, QString.SplitBehavior behavior = QString.KeepEmptyParts, Qt.CaseSensitivity cs = Qt.CaseSensitive)'''
        return QStringList()
    def split(self, sep, behavior = QString.KeepEmptyParts):
        '''QStringList QString.split(QRegExp sep, QString.SplitBehavior behavior = QString.KeepEmptyParts)'''
        return QStringList()
    def replace(self, i, len, after):
        '''QString QString.replace(int i, int len, QString after)'''
        return QString()
    def replace(self, before, after, cs = Qt.CaseSensitive):
        '''QString QString.replace(QString before, QString after, Qt.CaseSensitivity cs = Qt.CaseSensitive)'''
        return QString()
    def replace(self, rx, after):
        '''QString QString.replace(QRegExp rx, QString after)'''
        return QString()
    def replace(self, before, after, cs = Qt.CaseSensitive):
        '''QString QString.replace(QLatin1String before, QLatin1String after, Qt.CaseSensitivity cs = Qt.CaseSensitive)'''
        return QString()
    def replace(self, before, after, cs = Qt.CaseSensitive):
        '''QString QString.replace(QLatin1String before, QString after, Qt.CaseSensitivity cs = Qt.CaseSensitive)'''
        return QString()
    def replace(self, before, after, cs = Qt.CaseSensitive):
        '''QString QString.replace(QString before, QLatin1String after, Qt.CaseSensitivity cs = Qt.CaseSensitive)'''
        return QString()
    def remove(self, i, len):
        '''QString QString.remove(int i, int len)'''
        return QString()
    def remove(self, str, cs = Qt.CaseSensitive):
        '''QString QString.remove(QString str, Qt.CaseSensitivity cs = Qt.CaseSensitive)'''
        return QString()
    def remove(self, rx):
        '''QString QString.remove(QRegExp rx)'''
        return QString()
    def __iadd__(self, c):
        '''QString QString.__iadd__(QChar.SpecialCharacter c)'''
        return QString()
    def __iadd__(self, s):
        '''QString QString.__iadd__(QString s)'''
        return QString()
    def __iadd__(self, s):
        '''QString QString.__iadd__(QLatin1String s)'''
        return QString()
    def __iadd__(self, s):
        '''QString QString.__iadd__(QByteArray s)'''
        return QString()
    def prepend(self, s):
        '''QString QString.prepend(QString s)'''
        return QString()
    def prepend(self, s):
        '''QString QString.prepend(QLatin1String s)'''
        return QString()
    def prepend(self, s):
        '''QString QString.prepend(QByteArray s)'''
        return QString()
    def append(self, s):
        '''QString QString.append(QString s)'''
        return QString()
    def append(self, s):
        '''QString QString.append(QLatin1String s)'''
        return QString()
    def append(self, s):
        '''QString QString.append(QByteArray s)'''
        return QString()
    def insert(self, i, s):
        '''QString QString.insert(int i, QString s)'''
        return QString()
    def insert(self, i, s):
        '''QString QString.insert(int i, QLatin1String s)'''
        return QString()
    def simplified(self):
        '''QString QString.simplified()'''
        return QString()
    def trimmed(self):
        '''QString QString.trimmed()'''
        return QString()
    def toUpper(self):
        '''QString QString.toUpper()'''
        return QString()
    def toLower(self):
        '''QString QString.toLower()'''
        return QString()
    def rightJustified(self, width, fillChar = QLatin1Char(' '), truncate = False):
        '''QString QString.rightJustified(int width, QChar fillChar = QLatin1Char(' '), bool truncate = False)'''
        return QString()
    def leftJustified(self, width, fillChar = QLatin1Char(' '), truncate = False):
        '''QString QString.leftJustified(int width, QChar fillChar = QLatin1Char(' '), bool truncate = False)'''
        return QString()
    def endsWith(self, s, cs = Qt.CaseSensitive):
        '''bool QString.endsWith(QString s, Qt.CaseSensitivity cs = Qt.CaseSensitive)'''
        return bool()
    def endsWith(self, s, cs = Qt.CaseSensitive):
        '''bool QString.endsWith(QStringRef s, Qt.CaseSensitivity cs = Qt.CaseSensitive)'''
        return bool()
    def endsWith(self, s, cs = Qt.CaseSensitive):
        '''bool QString.endsWith(QLatin1String s, Qt.CaseSensitivity cs = Qt.CaseSensitive)'''
        return bool()
    def startsWith(self, s, cs = Qt.CaseSensitive):
        '''bool QString.startsWith(QString s, Qt.CaseSensitivity cs = Qt.CaseSensitive)'''
        return bool()
    def startsWith(self, s, cs = Qt.CaseSensitive):
        '''bool QString.startsWith(QStringRef s, Qt.CaseSensitivity cs = Qt.CaseSensitive)'''
        return bool()
    def startsWith(self, s, cs = Qt.CaseSensitive):
        '''bool QString.startsWith(QLatin1String s, Qt.CaseSensitivity cs = Qt.CaseSensitive)'''
        return bool()
    def mid(self, position, n = -1):
        '''QString QString.mid(int position, int n = -1)'''
        return QString()
    def right(self, len):
        '''QString QString.right(int len)'''
        return QString()
    def left(self, len):
        '''QString QString.left(int len)'''
        return QString()
    def section(self, sep, start, end = -1, flags = QString.SectionDefault):
        '''QString QString.section(QString sep, int start, int end = -1, QString.SectionFlags flags = QString.SectionDefault)'''
        return QString()
    def section(self, reg, start, end = -1, flags = QString.SectionDefault):
        '''QString QString.section(QRegExp reg, int start, int end = -1, QString.SectionFlags flags = QString.SectionDefault)'''
        return QString()
    def contains(self, str, cs = Qt.CaseSensitive):
        '''bool QString.contains(QString str, Qt.CaseSensitivity cs = Qt.CaseSensitive)'''
        return bool()
    def contains(self, s, cs = Qt.CaseSensitive):
        '''bool QString.contains(QStringRef s, Qt.CaseSensitivity cs = Qt.CaseSensitive)'''
        return bool()
    def contains(self, rx):
        '''bool QString.contains(QRegExp rx)'''
        return bool()
    def lastIndexOf(self, str, from_ = -1, cs = Qt.CaseSensitive):
        '''int QString.lastIndexOf(QString str, int from = -1, Qt.CaseSensitivity cs = Qt.CaseSensitive)'''
        return int()
    def lastIndexOf(self, str, from_ = -1, cs = Qt.CaseSensitive):
        '''int QString.lastIndexOf(QStringRef str, int from = -1, Qt.CaseSensitivity cs = Qt.CaseSensitive)'''
        return int()
    def lastIndexOf(self, str, from_ = -1, cs = Qt.CaseSensitive):
        '''int QString.lastIndexOf(QLatin1String str, int from = -1, Qt.CaseSensitivity cs = Qt.CaseSensitive)'''
        return int()
    def lastIndexOf(self, rx, from_ = -1):
        '''int QString.lastIndexOf(QRegExp rx, int from = -1)'''
        return int()
    def indexOf(self, str, from_ = 0, cs = Qt.CaseSensitive):
        '''int QString.indexOf(QString str, int from = 0, Qt.CaseSensitivity cs = Qt.CaseSensitive)'''
        return int()
    def indexOf(self, str, from_ = 0, cs = Qt.CaseSensitive):
        '''int QString.indexOf(QStringRef str, int from = 0, Qt.CaseSensitivity cs = Qt.CaseSensitive)'''
        return int()
    def indexOf(self, str, from_ = 0, cs = Qt.CaseSensitive):
        '''int QString.indexOf(QLatin1String str, int from = 0, Qt.CaseSensitivity cs = Qt.CaseSensitive)'''
        return int()
    def indexOf(self, rx, from_ = 0):
        '''int QString.indexOf(QRegExp rx, int from = 0)'''
        return int()
    def arg(self, a, fieldWidth = 0, base = 10, fillChar = QLatin1Char(' ')):
        '''QString QString.arg(int a, int fieldWidth = 0, int base = 10, QChar fillChar = QLatin1Char(' '))'''
        return QString()
    def arg(self, a, fieldWidth = 0, format = 'g', precision = -1, fillChar = QLatin1Char(' ')):
        '''QString QString.arg(float a, int fieldWidth = 0, str format = 'g', int precision = -1, QChar fillChar = QLatin1Char(' '))'''
        return QString()
    def arg(self, a, fieldWidth = 0, base = 10, fillChar = QLatin1Char(' ')):
        '''QString QString.arg(int a, int fieldWidth = 0, int base = 10, QChar fillChar = QLatin1Char(' '))'''
        return QString()
    def arg(self, a, fieldWidth = 0, base = 10, fillChar = QLatin1Char(' ')):
        '''QString QString.arg(int a, int fieldWidth = 0, int base = 10, QChar fillChar = QLatin1Char(' '))'''
        return QString()
    def arg(self, a, fieldWidth = 0, fillChar = QLatin1Char(' ')):
        '''QString QString.arg(QString a, int fieldWidth = 0, QChar fillChar = QLatin1Char(' '))'''
        return QString()
    def arg(self, a1, a2):
        '''QString QString.arg(QString a1, QString a2)'''
        return QString()
    def arg(self, a1, a2, a3):
        '''QString QString.arg(QString a1, QString a2, QString a3)'''
        return QString()
    def arg(self, a1, a2, a3, a4):
        '''QString QString.arg(QString a1, QString a2, QString a3, QString a4)'''
        return QString()
    def arg(self, a1, a2, a3, a4, a5):
        '''QString QString.arg(QString a1, QString a2, QString a3, QString a4, QString a5)'''
        return QString()
    def arg(self, a1, a2, a3, a4, a5, a6):
        '''QString QString.arg(QString a1, QString a2, QString a3, QString a4, QString a5, QString a6)'''
        return QString()
    def arg(self, a1, a2, a3, a4, a5, a6, a7):
        '''QString QString.arg(QString a1, QString a2, QString a3, QString a4, QString a5, QString a6, QString a7)'''
        return QString()
    def arg(self, a1, a2, a3, a4, a5, a6, a7, a8):
        '''QString QString.arg(QString a1, QString a2, QString a3, QString a4, QString a5, QString a6, QString a7, QString a8)'''
        return QString()
    def arg(self, a1, a2, a3, a4, a5, a6, a7, a8, a9):
        '''QString QString.arg(QString a1, QString a2, QString a3, QString a4, QString a5, QString a6, QString a7, QString a8, QString a9)'''
        return QString()
    def squeeze(self):
        '''void QString.squeeze()'''
    def chop(self, n):
        '''void QString.chop(int n)'''
    def truncate(self, pos):
        '''void QString.truncate(int pos)'''
    def fill(self, ch, size = -1):
        '''QString QString.fill(QChar ch, int size = -1)'''
        return QString()
    def resize(self, size):
        '''void QString.resize(int size)'''
    def __len__(self):
        ''' QString.__len__()'''
        return ()
    def count(self):
        '''int QString.count()'''
        return int()
    def count(self, str, cs = Qt.CaseSensitive):
        '''int QString.count(QString str, Qt.CaseSensitivity cs = Qt.CaseSensitive)'''
        return int()
    def count(self, str, cs = Qt.CaseSensitive):
        '''int QString.count(QStringRef str, Qt.CaseSensitivity cs = Qt.CaseSensitive)'''
        return int()
    def count(self):
        '''QRegExp QString.count()'''
        return QRegExp()
    def size(self):
        '''int QString.size()'''
        return int()
    def __repr__(self):
        '''str QString.__repr__()'''
        return str()
    class SectionFlags():
        """"""
        def __init__(self):
            '''QString.SectionFlags QString.SectionFlags.__init__()'''
            return QString.SectionFlags()
        def __init__(self):
            '''int QString.SectionFlags.__init__()'''
            return int()
        def __init__(self):
            '''void QString.SectionFlags.__init__()'''
        def __bool__(self):
            '''int QString.SectionFlags.__bool__()'''
            return int()
        def __ne__(self, f):
            '''bool QString.SectionFlags.__ne__(QString.SectionFlags f)'''
            return bool()
        def __eq__(self, f):
            '''bool QString.SectionFlags.__eq__(QString.SectionFlags f)'''
            return bool()
        def __invert__(self):
            '''QString.SectionFlags QString.SectionFlags.__invert__()'''
            return QString.SectionFlags()
        def __and__(self, mask):
            '''QString.SectionFlags QString.SectionFlags.__and__(int mask)'''
            return QString.SectionFlags()
        def __xor__(self, f):
            '''QString.SectionFlags QString.SectionFlags.__xor__(QString.SectionFlags f)'''
            return QString.SectionFlags()
        def __xor__(self, f):
            '''QString.SectionFlags QString.SectionFlags.__xor__(int f)'''
            return QString.SectionFlags()
        def __or__(self, f):
            '''QString.SectionFlags QString.SectionFlags.__or__(QString.SectionFlags f)'''
            return QString.SectionFlags()
        def __or__(self, f):
            '''QString.SectionFlags QString.SectionFlags.__or__(int f)'''
            return QString.SectionFlags()
        def __int__(self):
            '''int QString.SectionFlags.__int__()'''
            return int()
        def __ixor__(self, f):
            '''QString.SectionFlags QString.SectionFlags.__ixor__(QString.SectionFlags f)'''
            return QString.SectionFlags()
        def __ior__(self, f):
            '''QString.SectionFlags QString.SectionFlags.__ior__(QString.SectionFlags f)'''
            return QString.SectionFlags()
        def __iand__(self, mask):
            '''QString.SectionFlags QString.SectionFlags.__iand__(int mask)'''
            return QString.SectionFlags()


class QLatin1String():
    """"""
    def __init__(self, s):
        '''void QLatin1String.__init__(str s)'''
    def __init__(self):
        '''QLatin1String QLatin1String.__init__()'''
        return QLatin1String()
    def __le__(self, s):
        '''bool QLatin1String.__le__(QString s)'''
        return bool()
    def __le__(self, s2):
        '''bool QLatin1String.__le__(QLatin1String s2)'''
        return bool()
    def __ge__(self, s):
        '''bool QLatin1String.__ge__(QString s)'''
        return bool()
    def __ge__(self, s2):
        '''bool QLatin1String.__ge__(QLatin1String s2)'''
        return bool()
    def __lt__(self, s):
        '''bool QLatin1String.__lt__(QString s)'''
        return bool()
    def __lt__(self, s2):
        '''bool QLatin1String.__lt__(QLatin1String s2)'''
        return bool()
    def __gt__(self, s):
        '''bool QLatin1String.__gt__(QString s)'''
        return bool()
    def __gt__(self, s2):
        '''bool QLatin1String.__gt__(QLatin1String s2)'''
        return bool()
    def __ne__(self, s):
        '''bool QLatin1String.__ne__(QString s)'''
        return bool()
    def __ne__(self, s2):
        '''bool QLatin1String.__ne__(QLatin1String s2)'''
        return bool()
    def __ne__(self, s2):
        '''bool QLatin1String.__ne__(QStringRef s2)'''
        return bool()
    def __eq__(self, s):
        '''bool QLatin1String.__eq__(QString s)'''
        return bool()
    def __eq__(self, s2):
        '''bool QLatin1String.__eq__(QLatin1String s2)'''
        return bool()
    def __eq__(self, s2):
        '''bool QLatin1String.__eq__(QStringRef s2)'''
        return bool()
    def latin1(self):
        '''str QLatin1String.latin1()'''
        return str()
    def __repr__(self):
        '''str QLatin1String.__repr__()'''
        return str()


class QStringRef():
    """"""
    def __init__(self):
        '''void QStringRef.__init__()'''
    def __init__(self, aString, aPosition, aSize):
        '''void QStringRef.__init__(QString aString, int aPosition, int aSize)'''
    def __init__(self, aString):
        '''void QStringRef.__init__(QString aString)'''
    def __init__(self, other):
        '''void QStringRef.__init__(QStringRef other)'''
    def __eq__(self, s2):
        '''bool QStringRef.__eq__(QStringRef s2)'''
        return bool()
    def __eq__(self, s2):
        '''bool QStringRef.__eq__(QString s2)'''
        return bool()
    def __eq__(self, s2):
        '''bool QStringRef.__eq__(QLatin1String s2)'''
        return bool()
    def __ne__(self, s2):
        '''bool QStringRef.__ne__(QStringRef s2)'''
        return bool()
    def __ne__(self, s2):
        '''bool QStringRef.__ne__(QString s2)'''
        return bool()
    def __ne__(self, s2):
        '''bool QStringRef.__ne__(QLatin1String s2)'''
        return bool()
    def __lt__(self, s2):
        '''bool QStringRef.__lt__(QStringRef s2)'''
        return bool()
    def __le__(self, s2):
        '''bool QStringRef.__le__(QStringRef s2)'''
        return bool()
    def __gt__(self, s2):
        '''bool QStringRef.__gt__(QStringRef s2)'''
        return bool()
    def __ge__(self, s2):
        '''bool QStringRef.__ge__(QStringRef s2)'''
        return bool()
    def contains(self, str, cs = Qt.CaseSensitive):
        '''bool QStringRef.contains(QString str, Qt.CaseSensitivity cs = Qt.CaseSensitive)'''
        return bool()
    def contains(self, str, cs = Qt.CaseSensitive):
        '''bool QStringRef.contains(QLatin1String str, Qt.CaseSensitivity cs = Qt.CaseSensitive)'''
        return bool()
    def contains(self, str, cs = Qt.CaseSensitive):
        '''bool QStringRef.contains(QStringRef str, Qt.CaseSensitivity cs = Qt.CaseSensitive)'''
        return bool()
    def toUcs4(self):
        '''list-of-int QStringRef.toUcs4()'''
        return [int()]
    def toLocal8Bit(self):
        '''QByteArray QStringRef.toLocal8Bit()'''
        return QByteArray()
    def toUtf8(self):
        '''QByteArray QStringRef.toUtf8()'''
        return QByteArray()
    def toLatin1(self):
        '''QByteArray QStringRef.toLatin1()'''
        return QByteArray()
    def toAscii(self):
        '''QByteArray QStringRef.toAscii()'''
        return QByteArray()
    def endsWith(self, str, cs = Qt.CaseSensitive):
        '''bool QStringRef.endsWith(QString str, Qt.CaseSensitivity cs = Qt.CaseSensitive)'''
        return bool()
    def endsWith(self, str, cs = Qt.CaseSensitive):
        '''bool QStringRef.endsWith(QLatin1String str, Qt.CaseSensitivity cs = Qt.CaseSensitive)'''
        return bool()
    def endsWith(self, str, cs = Qt.CaseSensitive):
        '''bool QStringRef.endsWith(QStringRef str, Qt.CaseSensitivity cs = Qt.CaseSensitive)'''
        return bool()
    def startsWith(self, str, cs = Qt.CaseSensitive):
        '''bool QStringRef.startsWith(QString str, Qt.CaseSensitivity cs = Qt.CaseSensitive)'''
        return bool()
    def startsWith(self, str, cs = Qt.CaseSensitive):
        '''bool QStringRef.startsWith(QLatin1String str, Qt.CaseSensitivity cs = Qt.CaseSensitive)'''
        return bool()
    def startsWith(self, str, cs = Qt.CaseSensitive):
        '''bool QStringRef.startsWith(QStringRef str, Qt.CaseSensitivity cs = Qt.CaseSensitive)'''
        return bool()
    def lastIndexOf(self, str, from_ = -1, cs = Qt.CaseSensitive):
        '''int QStringRef.lastIndexOf(QString str, int from = -1, Qt.CaseSensitivity cs = Qt.CaseSensitive)'''
        return int()
    def lastIndexOf(self, str, from_ = -1, cs = Qt.CaseSensitive):
        '''int QStringRef.lastIndexOf(QLatin1String str, int from = -1, Qt.CaseSensitivity cs = Qt.CaseSensitive)'''
        return int()
    def lastIndexOf(self, str, from_ = -1, cs = Qt.CaseSensitive):
        '''int QStringRef.lastIndexOf(QStringRef str, int from = -1, Qt.CaseSensitivity cs = Qt.CaseSensitive)'''
        return int()
    def indexOf(self, str, from_ = 0, cs = Qt.CaseSensitive):
        '''int QStringRef.indexOf(QString str, int from = 0, Qt.CaseSensitivity cs = Qt.CaseSensitive)'''
        return int()
    def indexOf(self, str, from_ = 0, cs = Qt.CaseSensitive):
        '''int QStringRef.indexOf(QLatin1String str, int from = 0, Qt.CaseSensitivity cs = Qt.CaseSensitive)'''
        return int()
    def indexOf(self, str, from_ = 0, cs = Qt.CaseSensitive):
        '''int QStringRef.indexOf(QStringRef str, int from = 0, Qt.CaseSensitivity cs = Qt.CaseSensitive)'''
        return int()
    def __str__(self):
        '''str QStringRef.__str__()'''
        return str()
    def __unicode__(self):
        '''unicode QStringRef.__unicode__()'''
        return unicode()
    def localeAwareCompare(self, s):
        '''int QStringRef.localeAwareCompare(QString s)'''
        return int()
    def localeAwareCompare(self, s):
        '''int QStringRef.localeAwareCompare(QStringRef s)'''
        return int()
    def localeAwareCompare(self, s1, s2):
        '''static int QStringRef.localeAwareCompare(QStringRef s1, QString s2)'''
        return int()
    def localeAwareCompare(self, s1, s2):
        '''static int QStringRef.localeAwareCompare(QStringRef s1, QStringRef s2)'''
        return int()
    def compare(self, other, cs = Qt.CaseSensitive):
        '''int QStringRef.compare(QString other, Qt.CaseSensitivity cs = Qt.CaseSensitive)'''
        return int()
    def compare(self, other, cs = Qt.CaseSensitive):
        '''int QStringRef.compare(QStringRef other, Qt.CaseSensitivity cs = Qt.CaseSensitive)'''
        return int()
    def compare(self, other, cs = Qt.CaseSensitive):
        '''int QStringRef.compare(QLatin1String other, Qt.CaseSensitivity cs = Qt.CaseSensitive)'''
        return int()
    def compare(self, s1, s2, cs = Qt.CaseSensitive):
        '''static int QStringRef.compare(QStringRef s1, QString s2, Qt.CaseSensitivity cs = Qt.CaseSensitive)'''
        return int()
    def compare(self, s1, s2, cs = Qt.CaseSensitive):
        '''static int QStringRef.compare(QStringRef s1, QStringRef s2, Qt.CaseSensitivity cs = Qt.CaseSensitive)'''
        return int()
    def compare(self, s1, s2, cs = Qt.CaseSensitive):
        '''static int QStringRef.compare(QStringRef s1, QLatin1String s2, Qt.CaseSensitivity cs = Qt.CaseSensitive)'''
        return int()
    def at(self, i):
        '''QChar QStringRef.at(int i)'''
        return QChar()
    def appendTo(self, string):
        '''QStringRef QStringRef.appendTo(QString string)'''
        return QStringRef()
    def isNull(self):
        '''bool QStringRef.isNull()'''
        return bool()
    def isEmpty(self):
        '''bool QStringRef.isEmpty()'''
        return bool()
    def toString(self):
        '''QString QStringRef.toString()'''
        return QString()
    def clear(self):
        '''void QStringRef.clear()'''
    def constData(self):
        '''QChar QStringRef.constData()'''
        return QChar()
    def data(self):
        '''QChar QStringRef.data()'''
        return QChar()
    def unicode(self):
        '''QChar QStringRef.unicode()'''
        return QChar()
    def length(self):
        '''int QStringRef.length()'''
        return int()
    def __len__(self):
        ''' QStringRef.__len__()'''
        return ()
    def count(self):
        '''int QStringRef.count()'''
        return int()
    def count(self, str, cs = Qt.CaseSensitive):
        '''int QStringRef.count(QString str, Qt.CaseSensitivity cs = Qt.CaseSensitive)'''
        return int()
    def count(self, str, cs = Qt.CaseSensitive):
        '''int QStringRef.count(QStringRef str, Qt.CaseSensitivity cs = Qt.CaseSensitive)'''
        return int()
    def size(self):
        '''int QStringRef.size()'''
        return int()
    def position(self):
        '''int QStringRef.position()'''
        return int()
    def string(self):
        '''QString QStringRef.string()'''
        return QString()


class QStringList():
    """"""
    def __init__(self):
        '''void QStringList.__init__()'''
    def __init__(self, i):
        '''void QStringList.__init__(QString i)'''
    def __init__(self, l):
        '''void QStringList.__init__(QStringList l)'''
    def __iadd__(self, other):
        '''QStringList QStringList.__iadd__(QStringList other)'''
        return QStringList()
    def __iadd__(self, value):
        '''QStringList QStringList.__iadd__(QString value)'''
        return QStringList()
    def mid(self, pos, length = -1):
        '''QStringList QStringList.mid(int pos, int length = -1)'''
        return QStringList()
    def last(self):
        '''QString QStringList.last()'''
        return QString()
    def first(self):
        '''QString QStringList.first()'''
        return QString()
    def __len__(self):
        ''' QStringList.__len__()'''
        return ()
    def count(self, str):
        '''int QStringList.count(QString str)'''
        return int()
    def count(self):
        '''int QStringList.count()'''
        return int()
    def swap(self, i, j):
        '''void QStringList.swap(int i, int j)'''
    def move(self, from_, to):
        '''void QStringList.move(int from, int to)'''
    def takeLast(self):
        '''QString QStringList.takeLast()'''
        return QString()
    def takeFirst(self):
        '''QString QStringList.takeFirst()'''
        return QString()
    def takeAt(self, i):
        '''QString QStringList.takeAt(int i)'''
        return QString()
    def removeAll(self, str):
        '''int QStringList.removeAll(QString str)'''
        return int()
    def removeAt(self, i):
        '''void QStringList.removeAt(int i)'''
    def replace(self, i, str):
        '''void QStringList.replace(int i, QString str)'''
    def insert(self, i, str):
        '''void QStringList.insert(int i, QString str)'''
    def prepend(self, str):
        '''void QStringList.prepend(QString str)'''
    def append(self, str):
        '''void QStringList.append(QString str)'''
    def isEmpty(self):
        '''bool QStringList.isEmpty()'''
        return bool()
    def clear(self):
        '''void QStringList.clear()'''
    def __ne__(self, other):
        '''bool QStringList.__ne__(QStringList other)'''
        return bool()
    def __eq__(self, other):
        '''bool QStringList.__eq__(QStringList other)'''
        return bool()
    def __imul__(self, by):
        '''QStringList QStringList.__imul__(int by)'''
        return QStringList()
    def __mul__(self, by):
        '''QStringList QStringList.__mul__(int by)'''
        return QStringList()
    def __add__(self, other):
        '''QStringList QStringList.__add__(QStringList other)'''
        return QStringList()
    def __contains__(self, str):
        '''int QStringList.__contains__(QString str)'''
        return int()
    def __getitem__(self, i):
        '''QString QStringList.__getitem__(int i)'''
        return QString()
    def __getitem__(self, slice):
        '''QStringList QStringList.__getitem__(slice slice)'''
        return QStringList()
    def __delitem__(self, i):
        '''void QStringList.__delitem__(int i)'''
    def __delitem__(self, slice):
        '''void QStringList.__delitem__(slice slice)'''
    def __setitem__(self, i, str):
        '''void QStringList.__setitem__(int i, QString str)'''
    def __setitem__(self, slice, list):
        '''void QStringList.__setitem__(slice slice, QStringList list)'''
    def removeDuplicates(self):
        '''int QStringList.removeDuplicates()'''
        return int()
    def lastIndexOf(self, value, from_ = -1):
        '''int QStringList.lastIndexOf(QString value, int from = -1)'''
        return int()
    def lastIndexOf(self, rx, from_ = -1):
        '''int QStringList.lastIndexOf(QRegExp rx, int from = -1)'''
        return int()
    def indexOf(self, value, from_ = 0):
        '''int QStringList.indexOf(QString value, int from = 0)'''
        return int()
    def indexOf(self, rx, from_ = 0):
        '''int QStringList.indexOf(QRegExp rx, int from = 0)'''
        return int()
    def replaceInStrings(self, before, after, cs = Qt.CaseSensitive):
        '''QStringList QStringList.replaceInStrings(QString before, QString after, Qt.CaseSensitivity cs = Qt.CaseSensitive)'''
        return QStringList()
    def replaceInStrings(self, rx, after):
        '''QStringList QStringList.replaceInStrings(QRegExp rx, QString after)'''
        return QStringList()
    def contains(self, str, cs = Qt.CaseSensitive):
        '''bool QStringList.contains(QString str, Qt.CaseSensitivity cs = Qt.CaseSensitive)'''
        return bool()
    def filter(self, str, cs = Qt.CaseSensitive):
        '''QStringList QStringList.filter(QString str, Qt.CaseSensitivity cs = Qt.CaseSensitive)'''
        return QStringList()
    def filter(self, rx):
        '''QStringList QStringList.filter(QRegExp rx)'''
        return QStringList()
    def join(self, sep):
        '''QString QStringList.join(QString sep)'''
        return QString()
    def sort(self):
        '''void QStringList.sort()'''
    def __lshift__(self, str):
        '''QStringList QStringList.__lshift__(QString str)'''
        return QStringList()
    def __lshift__(self, l):
        '''QStringList QStringList.__lshift__(QStringList l)'''
        return QStringList()


class QStringMatcher():
    """"""
    def __init__(self):
        '''void QStringMatcher.__init__()'''
    def __init__(self, pattern, cs = Qt.CaseSensitive):
        '''void QStringMatcher.__init__(QString pattern, Qt.CaseSensitivity cs = Qt.CaseSensitive)'''
    def __init__(self, other):
        '''void QStringMatcher.__init__(QStringMatcher other)'''
    def caseSensitivity(self):
        '''Qt.CaseSensitivity QStringMatcher.caseSensitivity()'''
        return Qt.CaseSensitivity()
    def pattern(self):
        '''QString QStringMatcher.pattern()'''
        return QString()
    def indexIn(self, str, from_ = 0):
        '''int QStringMatcher.indexIn(QString str, int from = 0)'''
        return int()
    def setCaseSensitivity(self, cs):
        '''void QStringMatcher.setCaseSensitivity(Qt.CaseSensitivity cs)'''
    def setPattern(self, pattern):
        '''void QStringMatcher.setPattern(QString pattern)'''


class QSystemSemaphore():
    """"""
    # Enum QSystemSemaphore.SystemSemaphoreError
    NoError = 0
    PermissionDenied = 0
    KeyError = 0
    AlreadyExists = 0
    NotFound = 0
    OutOfResources = 0
    UnknownError = 0

    # Enum QSystemSemaphore.AccessMode
    Open = 0
    Create = 0

    def __init__(self, key, initialValue = 0, mode = QSystemSemaphore.Open):
        '''void QSystemSemaphore.__init__(QString key, int initialValue = 0, QSystemSemaphore.AccessMode mode = QSystemSemaphore.Open)'''
    def errorString(self):
        '''QString QSystemSemaphore.errorString()'''
        return QString()
    def error(self):
        '''QSystemSemaphore.SystemSemaphoreError QSystemSemaphore.error()'''
        return QSystemSemaphore.SystemSemaphoreError()
    def release(self, n = 1):
        '''bool QSystemSemaphore.release(int n = 1)'''
        return bool()
    def acquire(self):
        '''bool QSystemSemaphore.acquire()'''
        return bool()
    def key(self):
        '''QString QSystemSemaphore.key()'''
        return QString()
    def setKey(self, key, initialValue = 0, mode = QSystemSemaphore.Open):
        '''void QSystemSemaphore.setKey(QString key, int initialValue = 0, QSystemSemaphore.AccessMode mode = QSystemSemaphore.Open)'''


class QTemporaryFile(QFile):
    """"""
    def __init__(self):
        '''void QTemporaryFile.__init__()'''
    def __init__(self, templateName):
        '''void QTemporaryFile.__init__(QString templateName)'''
    def __init__(self, parent):
        '''void QTemporaryFile.__init__(QObject parent)'''
    def __init__(self, templateName, parent):
        '''void QTemporaryFile.__init__(QString templateName, QObject parent)'''
    def fileEngine(self):
        '''QAbstractFileEngine QTemporaryFile.fileEngine()'''
        return QAbstractFileEngine()
    def createLocalFile(self, fileName):
        '''static QTemporaryFile QTemporaryFile.createLocalFile(QString fileName)'''
        return QTemporaryFile()
    def createLocalFile(self, file):
        '''static QTemporaryFile QTemporaryFile.createLocalFile(QFile file)'''
        return QTemporaryFile()
    def setFileTemplate(self, name):
        '''void QTemporaryFile.setFileTemplate(QString name)'''
    def fileTemplate(self):
        '''QString QTemporaryFile.fileTemplate()'''
        return QString()
    def fileName(self):
        '''QString QTemporaryFile.fileName()'''
        return QString()
    def open(self):
        '''bool QTemporaryFile.open()'''
        return bool()
    def open(self, flags):
        '''bool QTemporaryFile.open(QIODevice.OpenMode flags)'''
        return bool()
    def setAutoRemove(self, b):
        '''void QTemporaryFile.setAutoRemove(bool b)'''
    def autoRemove(self):
        '''bool QTemporaryFile.autoRemove()'''
        return bool()


class QTextBoundaryFinder():
    """"""
    # Enum QTextBoundaryFinder.BoundaryType
    Grapheme = 0
    Word = 0
    Line = 0
    Sentence = 0

    # Enum QTextBoundaryFinder.BoundaryReason
    NotAtBoundary = 0
    StartWord = 0
    EndWord = 0

    def __init__(self):
        '''void QTextBoundaryFinder.__init__()'''
    def __init__(self, other):
        '''void QTextBoundaryFinder.__init__(QTextBoundaryFinder other)'''
    def __init__(self, type, string):
        '''void QTextBoundaryFinder.__init__(QTextBoundaryFinder.BoundaryType type, QString string)'''
    def boundaryReasons(self):
        '''QTextBoundaryFinder.BoundaryReasons QTextBoundaryFinder.boundaryReasons()'''
        return QTextBoundaryFinder.BoundaryReasons()
    def isAtBoundary(self):
        '''bool QTextBoundaryFinder.isAtBoundary()'''
        return bool()
    def toPreviousBoundary(self):
        '''int QTextBoundaryFinder.toPreviousBoundary()'''
        return int()
    def toNextBoundary(self):
        '''int QTextBoundaryFinder.toNextBoundary()'''
        return int()
    def setPosition(self, position):
        '''void QTextBoundaryFinder.setPosition(int position)'''
    def position(self):
        '''int QTextBoundaryFinder.position()'''
        return int()
    def toEnd(self):
        '''void QTextBoundaryFinder.toEnd()'''
    def toStart(self):
        '''void QTextBoundaryFinder.toStart()'''
    def string(self):
        '''QString QTextBoundaryFinder.string()'''
        return QString()
    def type(self):
        '''QTextBoundaryFinder.BoundaryType QTextBoundaryFinder.type()'''
        return QTextBoundaryFinder.BoundaryType()
    def isValid(self):
        '''bool QTextBoundaryFinder.isValid()'''
        return bool()
    class BoundaryReasons():
        """"""
        def __init__(self):
            '''QTextBoundaryFinder.BoundaryReasons QTextBoundaryFinder.BoundaryReasons.__init__()'''
            return QTextBoundaryFinder.BoundaryReasons()
        def __init__(self):
            '''int QTextBoundaryFinder.BoundaryReasons.__init__()'''
            return int()
        def __init__(self):
            '''void QTextBoundaryFinder.BoundaryReasons.__init__()'''
        def __bool__(self):
            '''int QTextBoundaryFinder.BoundaryReasons.__bool__()'''
            return int()
        def __ne__(self, f):
            '''bool QTextBoundaryFinder.BoundaryReasons.__ne__(QTextBoundaryFinder.BoundaryReasons f)'''
            return bool()
        def __eq__(self, f):
            '''bool QTextBoundaryFinder.BoundaryReasons.__eq__(QTextBoundaryFinder.BoundaryReasons f)'''
            return bool()
        def __invert__(self):
            '''QTextBoundaryFinder.BoundaryReasons QTextBoundaryFinder.BoundaryReasons.__invert__()'''
            return QTextBoundaryFinder.BoundaryReasons()
        def __and__(self, mask):
            '''QTextBoundaryFinder.BoundaryReasons QTextBoundaryFinder.BoundaryReasons.__and__(int mask)'''
            return QTextBoundaryFinder.BoundaryReasons()
        def __xor__(self, f):
            '''QTextBoundaryFinder.BoundaryReasons QTextBoundaryFinder.BoundaryReasons.__xor__(QTextBoundaryFinder.BoundaryReasons f)'''
            return QTextBoundaryFinder.BoundaryReasons()
        def __xor__(self, f):
            '''QTextBoundaryFinder.BoundaryReasons QTextBoundaryFinder.BoundaryReasons.__xor__(int f)'''
            return QTextBoundaryFinder.BoundaryReasons()
        def __or__(self, f):
            '''QTextBoundaryFinder.BoundaryReasons QTextBoundaryFinder.BoundaryReasons.__or__(QTextBoundaryFinder.BoundaryReasons f)'''
            return QTextBoundaryFinder.BoundaryReasons()
        def __or__(self, f):
            '''QTextBoundaryFinder.BoundaryReasons QTextBoundaryFinder.BoundaryReasons.__or__(int f)'''
            return QTextBoundaryFinder.BoundaryReasons()
        def __int__(self):
            '''int QTextBoundaryFinder.BoundaryReasons.__int__()'''
            return int()
        def __ixor__(self, f):
            '''QTextBoundaryFinder.BoundaryReasons QTextBoundaryFinder.BoundaryReasons.__ixor__(QTextBoundaryFinder.BoundaryReasons f)'''
            return QTextBoundaryFinder.BoundaryReasons()
        def __ior__(self, f):
            '''QTextBoundaryFinder.BoundaryReasons QTextBoundaryFinder.BoundaryReasons.__ior__(QTextBoundaryFinder.BoundaryReasons f)'''
            return QTextBoundaryFinder.BoundaryReasons()
        def __iand__(self, mask):
            '''QTextBoundaryFinder.BoundaryReasons QTextBoundaryFinder.BoundaryReasons.__iand__(int mask)'''
            return QTextBoundaryFinder.BoundaryReasons()


class QTextCodec():
    """"""
    # Enum QTextCodec.ConversionFlag
    DefaultConversion = 0
    ConvertInvalidToNull = 0
    IgnoreHeader = 0

    def __init__(self):
        '''void QTextCodec.__init__()'''
    def setCodecForCStrings(self, c):
        '''static void QTextCodec.setCodecForCStrings(QTextCodec c)'''
    def codecForCStrings(self):
        '''static QTextCodec QTextCodec.codecForCStrings()'''
        return QTextCodec()
    def setCodecForTr(self, c):
        '''static void QTextCodec.setCodecForTr(QTextCodec c)'''
    def codecForTr(self):
        '''static QTextCodec QTextCodec.codecForTr()'''
        return QTextCodec()
    def convertToUnicode(self, in_, state):
        '''abstract QString QTextCodec.convertToUnicode(str in, QTextCodec.ConverterState state)'''
        return QString()
    def mibEnum(self):
        '''abstract int QTextCodec.mibEnum()'''
        return int()
    def aliases(self):
        '''list-of-QByteArray QTextCodec.aliases()'''
        return [QByteArray()]
    def name(self):
        '''abstract QByteArray QTextCodec.name()'''
        return QByteArray()
    def fromUnicode(self, uc):
        '''QByteArray QTextCodec.fromUnicode(QString uc)'''
        return QByteArray()
    def toUnicode(self):
        '''QByteArray QTextCodec.toUnicode()'''
        return QByteArray()
    def toUnicode(self, chars):
        '''QString QTextCodec.toUnicode(str chars)'''
        return QString()
    def toUnicode(self, in_, state = None):
        '''QString QTextCodec.toUnicode(str in, QTextCodec.ConverterState state = None)'''
        return QString()
    def canEncode(self):
        '''QString QTextCodec.canEncode()'''
        return QString()
    def makeEncoder(self):
        '''QTextEncoder QTextCodec.makeEncoder()'''
        return QTextEncoder()
    def makeEncoder(self, flags):
        '''QTextEncoder QTextCodec.makeEncoder(QTextCodec.ConversionFlags flags)'''
        return QTextEncoder()
    def makeDecoder(self):
        '''QTextDecoder QTextCodec.makeDecoder()'''
        return QTextDecoder()
    def makeDecoder(self, flags):
        '''QTextDecoder QTextCodec.makeDecoder(QTextCodec.ConversionFlags flags)'''
        return QTextDecoder()
    def setCodecForLocale(self, c):
        '''static void QTextCodec.setCodecForLocale(QTextCodec c)'''
    def codecForLocale(self):
        '''static QTextCodec QTextCodec.codecForLocale()'''
        return QTextCodec()
    def availableMibs(self):
        '''static list-of-int QTextCodec.availableMibs()'''
        return [int()]
    def availableCodecs(self):
        '''static list-of-QByteArray QTextCodec.availableCodecs()'''
        return [QByteArray()]
    def codecForUtfText(self, ba):
        '''static QTextCodec QTextCodec.codecForUtfText(QByteArray ba)'''
        return QTextCodec()
    def codecForUtfText(self, ba, defaultCodec):
        '''static QTextCodec QTextCodec.codecForUtfText(QByteArray ba, QTextCodec defaultCodec)'''
        return QTextCodec()
    def codecForHtml(self, ba):
        '''static QTextCodec QTextCodec.codecForHtml(QByteArray ba)'''
        return QTextCodec()
    def codecForHtml(self, ba, defaultCodec):
        '''static QTextCodec QTextCodec.codecForHtml(QByteArray ba, QTextCodec defaultCodec)'''
        return QTextCodec()
    def codecForMib(self, mib):
        '''static QTextCodec QTextCodec.codecForMib(int mib)'''
        return QTextCodec()
    def codecForName(self, name):
        '''static QTextCodec QTextCodec.codecForName(QByteArray name)'''
        return QTextCodec()
    def codecForName(self, name):
        '''static QTextCodec QTextCodec.codecForName(str name)'''
        return QTextCodec()
    class ConversionFlags():
        """"""
        def __init__(self):
            '''QTextCodec.ConversionFlags QTextCodec.ConversionFlags.__init__()'''
            return QTextCodec.ConversionFlags()
        def __init__(self):
            '''int QTextCodec.ConversionFlags.__init__()'''
            return int()
        def __init__(self):
            '''void QTextCodec.ConversionFlags.__init__()'''
        def __bool__(self):
            '''int QTextCodec.ConversionFlags.__bool__()'''
            return int()
        def __ne__(self, f):
            '''bool QTextCodec.ConversionFlags.__ne__(QTextCodec.ConversionFlags f)'''
            return bool()
        def __eq__(self, f):
            '''bool QTextCodec.ConversionFlags.__eq__(QTextCodec.ConversionFlags f)'''
            return bool()
        def __invert__(self):
            '''QTextCodec.ConversionFlags QTextCodec.ConversionFlags.__invert__()'''
            return QTextCodec.ConversionFlags()
        def __and__(self, mask):
            '''QTextCodec.ConversionFlags QTextCodec.ConversionFlags.__and__(int mask)'''
            return QTextCodec.ConversionFlags()
        def __xor__(self, f):
            '''QTextCodec.ConversionFlags QTextCodec.ConversionFlags.__xor__(QTextCodec.ConversionFlags f)'''
            return QTextCodec.ConversionFlags()
        def __xor__(self, f):
            '''QTextCodec.ConversionFlags QTextCodec.ConversionFlags.__xor__(int f)'''
            return QTextCodec.ConversionFlags()
        def __or__(self, f):
            '''QTextCodec.ConversionFlags QTextCodec.ConversionFlags.__or__(QTextCodec.ConversionFlags f)'''
            return QTextCodec.ConversionFlags()
        def __or__(self, f):
            '''QTextCodec.ConversionFlags QTextCodec.ConversionFlags.__or__(int f)'''
            return QTextCodec.ConversionFlags()
        def __int__(self):
            '''int QTextCodec.ConversionFlags.__int__()'''
            return int()
        def __ixor__(self, f):
            '''QTextCodec.ConversionFlags QTextCodec.ConversionFlags.__ixor__(QTextCodec.ConversionFlags f)'''
            return QTextCodec.ConversionFlags()
        def __ior__(self, f):
            '''QTextCodec.ConversionFlags QTextCodec.ConversionFlags.__ior__(QTextCodec.ConversionFlags f)'''
            return QTextCodec.ConversionFlags()
        def __iand__(self, mask):
            '''QTextCodec.ConversionFlags QTextCodec.ConversionFlags.__iand__(int mask)'''
            return QTextCodec.ConversionFlags()
    class ConverterState():
        """"""
        def __init__(self, flags = QTextCodec.DefaultConversion):
            '''void QTextCodec.ConverterState.__init__(QTextCodec.ConversionFlags flags = QTextCodec.DefaultConversion)'''


class QTextEncoder():
    """"""
    def __init__(self, codec):
        '''void QTextEncoder.__init__(QTextCodec codec)'''
    def __init__(self, codec, flags):
        '''void QTextEncoder.__init__(QTextCodec codec, QTextCodec.ConversionFlags flags)'''
    def fromUnicode(self, str):
        '''QByteArray QTextEncoder.fromUnicode(QString str)'''
        return QByteArray()


class QTextDecoder():
    """"""
    def __init__(self, codec):
        '''void QTextDecoder.__init__(QTextCodec codec)'''
    def __init__(self, codec, flags):
        '''void QTextDecoder.__init__(QTextCodec codec, QTextCodec.ConversionFlags flags)'''
    def toUnicode(self, chars):
        '''QString QTextDecoder.toUnicode(str chars)'''
        return QString()
    def toUnicode(self, target, chars):
        '''void QTextDecoder.toUnicode(QString target, str chars)'''
    def toUnicode(self, ba):
        '''QString QTextDecoder.toUnicode(QByteArray ba)'''
        return QString()


class QTextStream():
    """"""
    # Enum QTextStream.Status
    Ok = 0
    ReadPastEnd = 0
    ReadCorruptData = 0
    WriteFailed = 0

    # Enum QTextStream.NumberFlag
    ShowBase = 0
    ForcePoint = 0
    ForceSign = 0
    UppercaseBase = 0
    UppercaseDigits = 0

    # Enum QTextStream.FieldAlignment
    AlignLeft = 0
    AlignRight = 0
    AlignCenter = 0
    AlignAccountingStyle = 0

    # Enum QTextStream.RealNumberNotation
    SmartNotation = 0
    FixedNotation = 0
    ScientificNotation = 0

    def __init__(self):
        '''void QTextStream.__init__()'''
    def __init__(self, device):
        '''void QTextStream.__init__(QIODevice device)'''
    def __init__(self, string, mode = QIODevice.ReadWrite):
        '''void QTextStream.__init__(QString string, QIODevice.OpenMode mode = QIODevice.ReadWrite)'''
    def __init__(self, array, mode = QIODevice.ReadWrite):
        '''void QTextStream.__init__(QByteArray array, QIODevice.OpenMode mode = QIODevice.ReadWrite)'''
    def locale(self):
        '''QLocale QTextStream.locale()'''
        return QLocale()
    def setLocale(self, locale):
        '''void QTextStream.setLocale(QLocale locale)'''
    def __lshift__(self, f):
        '''QTextStream QTextStream.__lshift__(float f)'''
        return QTextStream()
    def __lshift__(self, b):
        '''QTextStream QTextStream.__lshift__(bool b)'''
        return QTextStream()
    def __lshift__(self, i):
        '''QTextStream QTextStream.__lshift__(int i)'''
        return QTextStream()
    def __lshift__(self, i):
        '''QTextStream QTextStream.__lshift__(int i)'''
        return QTextStream()
    def __lshift__(self, i):
        '''QTextStream QTextStream.__lshift__(int i)'''
        return QTextStream()
    def __lshift__(self, s):
        '''QTextStream QTextStream.__lshift__(QString s)'''
        return QTextStream()
    def __lshift__(self, array):
        '''QTextStream QTextStream.__lshift__(QByteArray array)'''
        return QTextStream()
    def __lshift__(self, m):
        '''QTextStream QTextStream.__lshift__(QTextStreamManipulator m)'''
        return QTextStream()
    def __rshift__(self, ch):
        '''QTextStream QTextStream.__rshift__(QChar ch)'''
        return QTextStream()
    def __rshift__(self, s):
        '''QTextStream QTextStream.__rshift__(QString s)'''
        return QTextStream()
    def __rshift__(self, array):
        '''QTextStream QTextStream.__rshift__(QByteArray array)'''
        return QTextStream()
    def pos(self):
        '''int QTextStream.pos()'''
        return int()
    def resetStatus(self):
        '''void QTextStream.resetStatus()'''
    def setStatus(self, status):
        '''void QTextStream.setStatus(QTextStream.Status status)'''
    def status(self):
        '''QTextStream.Status QTextStream.status()'''
        return QTextStream.Status()
    def realNumberPrecision(self):
        '''int QTextStream.realNumberPrecision()'''
        return int()
    def setRealNumberPrecision(self, precision):
        '''void QTextStream.setRealNumberPrecision(int precision)'''
    def realNumberNotation(self):
        '''QTextStream.RealNumberNotation QTextStream.realNumberNotation()'''
        return QTextStream.RealNumberNotation()
    def setRealNumberNotation(self, notation):
        '''void QTextStream.setRealNumberNotation(QTextStream.RealNumberNotation notation)'''
    def integerBase(self):
        '''int QTextStream.integerBase()'''
        return int()
    def setIntegerBase(self, base):
        '''void QTextStream.setIntegerBase(int base)'''
    def numberFlags(self):
        '''QTextStream.NumberFlags QTextStream.numberFlags()'''
        return QTextStream.NumberFlags()
    def setNumberFlags(self, flags):
        '''void QTextStream.setNumberFlags(QTextStream.NumberFlags flags)'''
    def fieldWidth(self):
        '''int QTextStream.fieldWidth()'''
        return int()
    def setFieldWidth(self, width):
        '''void QTextStream.setFieldWidth(int width)'''
    def padChar(self):
        '''QChar QTextStream.padChar()'''
        return QChar()
    def setPadChar(self, ch):
        '''void QTextStream.setPadChar(QChar ch)'''
    def fieldAlignment(self):
        '''QTextStream.FieldAlignment QTextStream.fieldAlignment()'''
        return QTextStream.FieldAlignment()
    def setFieldAlignment(self, alignment):
        '''void QTextStream.setFieldAlignment(QTextStream.FieldAlignment alignment)'''
    def readAll(self):
        '''QString QTextStream.readAll()'''
        return QString()
    def readLine(self, maxLength = 0):
        '''QString QTextStream.readLine(int maxLength = 0)'''
        return QString()
    def read(self, maxlen):
        '''QString QTextStream.read(int maxlen)'''
        return QString()
    def skipWhiteSpace(self):
        '''void QTextStream.skipWhiteSpace()'''
    def seek(self, pos):
        '''bool QTextStream.seek(int pos)'''
        return bool()
    def flush(self):
        '''void QTextStream.flush()'''
    def reset(self):
        '''void QTextStream.reset()'''
    def atEnd(self):
        '''bool QTextStream.atEnd()'''
        return bool()
    def string(self):
        '''QString QTextStream.string()'''
        return QString()
    def setString(self, string, mode = QIODevice.ReadWrite):
        '''void QTextStream.setString(QString string, QIODevice.OpenMode mode = QIODevice.ReadWrite)'''
    def device(self):
        '''QIODevice QTextStream.device()'''
        return QIODevice()
    def setDevice(self, device):
        '''void QTextStream.setDevice(QIODevice device)'''
    def generateByteOrderMark(self):
        '''bool QTextStream.generateByteOrderMark()'''
        return bool()
    def setGenerateByteOrderMark(self, generate):
        '''void QTextStream.setGenerateByteOrderMark(bool generate)'''
    def autoDetectUnicode(self):
        '''bool QTextStream.autoDetectUnicode()'''
        return bool()
    def setAutoDetectUnicode(self, enabled):
        '''void QTextStream.setAutoDetectUnicode(bool enabled)'''
    def codec(self):
        '''QTextCodec QTextStream.codec()'''
        return QTextCodec()
    def setCodec(self, codec):
        '''void QTextStream.setCodec(QTextCodec codec)'''
    def setCodec(self, codecName):
        '''void QTextStream.setCodec(str codecName)'''
    class NumberFlags():
        """"""
        def __init__(self):
            '''QTextStream.NumberFlags QTextStream.NumberFlags.__init__()'''
            return QTextStream.NumberFlags()
        def __init__(self):
            '''int QTextStream.NumberFlags.__init__()'''
            return int()
        def __init__(self):
            '''void QTextStream.NumberFlags.__init__()'''
        def __bool__(self):
            '''int QTextStream.NumberFlags.__bool__()'''
            return int()
        def __ne__(self, f):
            '''bool QTextStream.NumberFlags.__ne__(QTextStream.NumberFlags f)'''
            return bool()
        def __eq__(self, f):
            '''bool QTextStream.NumberFlags.__eq__(QTextStream.NumberFlags f)'''
            return bool()
        def __invert__(self):
            '''QTextStream.NumberFlags QTextStream.NumberFlags.__invert__()'''
            return QTextStream.NumberFlags()
        def __and__(self, mask):
            '''QTextStream.NumberFlags QTextStream.NumberFlags.__and__(int mask)'''
            return QTextStream.NumberFlags()
        def __xor__(self, f):
            '''QTextStream.NumberFlags QTextStream.NumberFlags.__xor__(QTextStream.NumberFlags f)'''
            return QTextStream.NumberFlags()
        def __xor__(self, f):
            '''QTextStream.NumberFlags QTextStream.NumberFlags.__xor__(int f)'''
            return QTextStream.NumberFlags()
        def __or__(self, f):
            '''QTextStream.NumberFlags QTextStream.NumberFlags.__or__(QTextStream.NumberFlags f)'''
            return QTextStream.NumberFlags()
        def __or__(self, f):
            '''QTextStream.NumberFlags QTextStream.NumberFlags.__or__(int f)'''
            return QTextStream.NumberFlags()
        def __int__(self):
            '''int QTextStream.NumberFlags.__int__()'''
            return int()
        def __ixor__(self, f):
            '''QTextStream.NumberFlags QTextStream.NumberFlags.__ixor__(QTextStream.NumberFlags f)'''
            return QTextStream.NumberFlags()
        def __ior__(self, f):
            '''QTextStream.NumberFlags QTextStream.NumberFlags.__ior__(QTextStream.NumberFlags f)'''
            return QTextStream.NumberFlags()
        def __iand__(self, mask):
            '''QTextStream.NumberFlags QTextStream.NumberFlags.__iand__(int mask)'''
            return QTextStream.NumberFlags()


class QThread(QObject):
    """"""
    # Enum QThread.Priority
    IdlePriority = 0
    LowestPriority = 0
    LowPriority = 0
    NormalPriority = 0
    HighPriority = 0
    HighestPriority = 0
    TimeCriticalPriority = 0
    InheritPriority = 0

    def __init__(self, parent = None):
        '''void QThread.__init__(QObject parent = None)'''
    def usleep(self):
        '''static int QThread.usleep()'''
        return int()
    def msleep(self):
        '''static int QThread.msleep()'''
        return int()
    def sleep(self):
        '''static int QThread.sleep()'''
        return int()
    def setTerminationEnabled(self, enabled = True):
        '''static void QThread.setTerminationEnabled(bool enabled = True)'''
    def exec_(self):
        '''int QThread.exec_()'''
        return int()
    def run(self):
        '''void QThread.run()'''
    terminated = pyqtSignal() # void terminated() - signal
    finished = pyqtSignal() # void finished() - signal
    started = pyqtSignal() # void started() - signal
    def wait(self, msecs = ULONG_MAX):
        '''bool QThread.wait(int msecs = ULONG_MAX)'''
        return bool()
    def quit(self):
        '''void QThread.quit()'''
    def terminate(self):
        '''void QThread.terminate()'''
    def start(self, priority = QThread.InheritPriority):
        '''void QThread.start(QThread.Priority priority = QThread.InheritPriority)'''
    def exit(self, returnCode = 0):
        '''void QThread.exit(int returnCode = 0)'''
    def stackSize(self):
        '''int QThread.stackSize()'''
        return int()
    def setStackSize(self, stackSize):
        '''void QThread.setStackSize(int stackSize)'''
    def priority(self):
        '''QThread.Priority QThread.priority()'''
        return QThread.Priority()
    def setPriority(self, priority):
        '''void QThread.setPriority(QThread.Priority priority)'''
    def isRunning(self):
        '''bool QThread.isRunning()'''
        return bool()
    def isFinished(self):
        '''bool QThread.isFinished()'''
        return bool()
    def yieldCurrentThread(self):
        '''static void QThread.yieldCurrentThread()'''
    def idealThreadCount(self):
        '''static int QThread.idealThreadCount()'''
        return int()
    def currentThreadId(self):
        '''static int QThread.currentThreadId()'''
        return int()
    def currentThread(self):
        '''static QThread QThread.currentThread()'''
        return QThread()


class QThreadPool(QObject):
    """"""
    def __init__(self, parent = None):
        '''void QThreadPool.__init__(QObject parent = None)'''
    def waitForDone(self):
        '''void QThreadPool.waitForDone()'''
    def waitForDone(self, msecs):
        '''bool QThreadPool.waitForDone(int msecs)'''
        return bool()
    def releaseThread(self):
        '''void QThreadPool.releaseThread()'''
    def reserveThread(self):
        '''void QThreadPool.reserveThread()'''
    def activeThreadCount(self):
        '''int QThreadPool.activeThreadCount()'''
        return int()
    def setMaxThreadCount(self, maxThreadCount):
        '''void QThreadPool.setMaxThreadCount(int maxThreadCount)'''
    def maxThreadCount(self):
        '''int QThreadPool.maxThreadCount()'''
        return int()
    def setExpiryTimeout(self, expiryTimeout):
        '''void QThreadPool.setExpiryTimeout(int expiryTimeout)'''
    def expiryTimeout(self):
        '''int QThreadPool.expiryTimeout()'''
        return int()
    def tryStart(self, runnable):
        '''bool QThreadPool.tryStart(QRunnable runnable)'''
        return bool()
    def start(self, runnable, priority = 0):
        '''void QThreadPool.start(QRunnable runnable, int priority = 0)'''
    def globalInstance(self):
        '''static QThreadPool QThreadPool.globalInstance()'''
        return QThreadPool()


class QTimeLine(QObject):
    """"""
    # Enum QTimeLine.State
    NotRunning = 0
    Paused = 0
    Running = 0

    # Enum QTimeLine.Direction
    Forward = 0
    Backward = 0

    # Enum QTimeLine.CurveShape
    EaseInCurve = 0
    EaseOutCurve = 0
    EaseInOutCurve = 0
    LinearCurve = 0
    SineCurve = 0
    CosineCurve = 0

    def __init__(self, duration = 1000, parent = None):
        '''void QTimeLine.__init__(int duration = 1000, QObject parent = None)'''
    def setEasingCurve(self, curve):
        '''void QTimeLine.setEasingCurve(QEasingCurve curve)'''
    def easingCurve(self):
        '''QEasingCurve QTimeLine.easingCurve()'''
        return QEasingCurve()
    def timerEvent(self, event):
        '''void QTimeLine.timerEvent(QTimerEvent event)'''
    valueChanged = pyqtSignal() # void valueChanged(qreal) - signal
    stateChanged = pyqtSignal() # void stateChanged(QTimeLine::State) - signal
    frameChanged = pyqtSignal() # void frameChanged(int) - signal
    finished = pyqtSignal() # void finished() - signal
    def toggleDirection(self):
        '''void QTimeLine.toggleDirection()'''
    def stop(self):
        '''void QTimeLine.stop()'''
    def start(self):
        '''void QTimeLine.start()'''
    def setPaused(self, paused):
        '''void QTimeLine.setPaused(bool paused)'''
    def setCurrentTime(self, msec):
        '''void QTimeLine.setCurrentTime(int msec)'''
    def resume(self):
        '''void QTimeLine.resume()'''
    def valueForTime(self, msec):
        '''float QTimeLine.valueForTime(int msec)'''
        return float()
    def frameForTime(self, msec):
        '''int QTimeLine.frameForTime(int msec)'''
        return int()
    def currentValue(self):
        '''float QTimeLine.currentValue()'''
        return float()
    def currentFrame(self):
        '''int QTimeLine.currentFrame()'''
        return int()
    def currentTime(self):
        '''int QTimeLine.currentTime()'''
        return int()
    def setCurveShape(self, shape):
        '''void QTimeLine.setCurveShape(QTimeLine.CurveShape shape)'''
    def curveShape(self):
        '''QTimeLine.CurveShape QTimeLine.curveShape()'''
        return QTimeLine.CurveShape()
    def setUpdateInterval(self, interval):
        '''void QTimeLine.setUpdateInterval(int interval)'''
    def updateInterval(self):
        '''int QTimeLine.updateInterval()'''
        return int()
    def setFrameRange(self, startFrame, endFrame):
        '''void QTimeLine.setFrameRange(int startFrame, int endFrame)'''
    def setEndFrame(self, frame):
        '''void QTimeLine.setEndFrame(int frame)'''
    def endFrame(self):
        '''int QTimeLine.endFrame()'''
        return int()
    def setStartFrame(self, frame):
        '''void QTimeLine.setStartFrame(int frame)'''
    def startFrame(self):
        '''int QTimeLine.startFrame()'''
        return int()
    def setDuration(self, duration):
        '''void QTimeLine.setDuration(int duration)'''
    def duration(self):
        '''int QTimeLine.duration()'''
        return int()
    def setDirection(self, direction):
        '''void QTimeLine.setDirection(QTimeLine.Direction direction)'''
    def direction(self):
        '''QTimeLine.Direction QTimeLine.direction()'''
        return QTimeLine.Direction()
    def setLoopCount(self, count):
        '''void QTimeLine.setLoopCount(int count)'''
    def loopCount(self):
        '''int QTimeLine.loopCount()'''
        return int()
    def state(self):
        '''QTimeLine.State QTimeLine.state()'''
        return QTimeLine.State()


class QTimer(QObject):
    """"""
    def __init__(self, parent = None):
        '''void QTimer.__init__(QObject parent = None)'''
    def timerEvent(self):
        '''QTimerEvent QTimer.timerEvent()'''
        return QTimerEvent()
    timeout = pyqtSignal() # void timeout() - signal
    def stop(self):
        '''void QTimer.stop()'''
    def start(self, msec):
        '''void QTimer.start(int msec)'''
    def start(self):
        '''void QTimer.start()'''
    def singleShot(self, msec, receiver, member):
        '''static void QTimer.singleShot(int msec, QObject receiver, SLOT()SLOT() member)'''
    def singleShot(self, msec, receiver):
        '''static void QTimer.singleShot(int msec, callable receiver)'''
    def setSingleShot(self, asingleShot):
        '''void QTimer.setSingleShot(bool asingleShot)'''
    def isSingleShot(self):
        '''bool QTimer.isSingleShot()'''
        return bool()
    def interval(self):
        '''int QTimer.interval()'''
        return int()
    def setInterval(self, msec):
        '''void QTimer.setInterval(int msec)'''
    def timerId(self):
        '''int QTimer.timerId()'''
        return int()
    def isActive(self):
        '''bool QTimer.isActive()'''
        return bool()


class QTranslator(QObject):
    """"""
    def __init__(self, parent = None):
        '''void QTranslator.__init__(QObject parent = None)'''
    def loadFromData(self, data):
        '''bool QTranslator.loadFromData(str data)'''
        return bool()
    def load(self, fileName, directory = QString(), searchDelimiters = QString(), suffix = QString()):
        '''bool QTranslator.load(QString fileName, QString directory = QString(), QString searchDelimiters = QString(), QString suffix = QString())'''
        return bool()
    def load(self, locale, fileName, prefix = QString(), directory = QString(), suffix = QString()):
        '''bool QTranslator.load(QLocale locale, QString fileName, QString prefix = QString(), QString directory = QString(), QString suffix = QString())'''
        return bool()
    def isEmpty(self):
        '''bool QTranslator.isEmpty()'''
        return bool()
    def translate(self, context, sourceText, disambiguation = None):
        '''QString QTranslator.translate(str context, str sourceText, str disambiguation = None)'''
        return QString()
    def translate(self, context, sourceText, comment, n):
        '''QString QTranslator.translate(str context, str sourceText, str comment, int n)'''
        return QString()


class QUrl():
    """"""
    # Enum QUrl.ParsingMode
    TolerantMode = 0
    StrictMode = 0

    # Enum QUrl.FormattingOption
    __kdevpythondocumentation_builtin_None = 0
    RemoveScheme = 0
    RemovePassword = 0
    RemoveUserInfo = 0
    RemovePort = 0
    RemoveAuthority = 0
    RemovePath = 0
    RemoveQuery = 0
    RemoveFragment = 0
    StripTrailingSlash = 0

    def __init__(self):
        '''void QUrl.__init__()'''
    def __init__(self, url):
        '''void QUrl.__init__(QString url)'''
    def __init__(self, copy):
        '''void QUrl.__init__(QUrl copy)'''
    def __init__(self, url, mode):
        '''void QUrl.__init__(QString url, QUrl.ParsingMode mode)'''
    def __ge__(self, url):
        '''bool QUrl.__ge__(QUrl url)'''
        return bool()
    def isLocalFile(self):
        '''bool QUrl.isLocalFile()'''
        return bool()
    def topLevelDomain(self):
        '''QString QUrl.topLevelDomain()'''
        return QString()
    def swap(self, other):
        '''void QUrl.swap(QUrl other)'''
    def fromUserInput(self, userInput):
        '''static QUrl QUrl.fromUserInput(QString userInput)'''
        return QUrl()
    def encodedFragment(self):
        '''QByteArray QUrl.encodedFragment()'''
        return QByteArray()
    def setEncodedFragment(self, fragment):
        '''void QUrl.setEncodedFragment(QByteArray fragment)'''
    def removeAllEncodedQueryItems(self, key):
        '''void QUrl.removeAllEncodedQueryItems(QByteArray key)'''
    def removeEncodedQueryItem(self, key):
        '''void QUrl.removeEncodedQueryItem(QByteArray key)'''
    def allEncodedQueryItemValues(self, key):
        '''list-of-QByteArray QUrl.allEncodedQueryItemValues(QByteArray key)'''
        return [QByteArray()]
    def encodedQueryItemValue(self, key):
        '''QByteArray QUrl.encodedQueryItemValue(QByteArray key)'''
        return QByteArray()
    def hasEncodedQueryItem(self, key):
        '''bool QUrl.hasEncodedQueryItem(QByteArray key)'''
        return bool()
    def encodedQueryItems(self):
        '''list-of-tuple-of-QByteArray-QByteArray QUrl.encodedQueryItems()'''
        return [tuple-of-QByteArray-QByteArray()]
    def addEncodedQueryItem(self, key, value):
        '''void QUrl.addEncodedQueryItem(QByteArray key, QByteArray value)'''
    def setEncodedQueryItems(self, query):
        '''void QUrl.setEncodedQueryItems(list-of-tuple-of-QByteArray-QByteArray query)'''
    def encodedPath(self):
        '''QByteArray QUrl.encodedPath()'''
        return QByteArray()
    def setEncodedPath(self, path):
        '''void QUrl.setEncodedPath(QByteArray path)'''
    def encodedHost(self):
        '''QByteArray QUrl.encodedHost()'''
        return QByteArray()
    def setEncodedHost(self, host):
        '''void QUrl.setEncodedHost(QByteArray host)'''
    def encodedPassword(self):
        '''QByteArray QUrl.encodedPassword()'''
        return QByteArray()
    def setEncodedPassword(self, password):
        '''void QUrl.setEncodedPassword(QByteArray password)'''
    def encodedUserName(self):
        '''QByteArray QUrl.encodedUserName()'''
        return QByteArray()
    def setEncodedUserName(self, userName):
        '''void QUrl.setEncodedUserName(QByteArray userName)'''
    def setIdnWhitelist(self):
        '''static QStringList QUrl.setIdnWhitelist()'''
        return QStringList()
    def idnWhitelist(self):
        '''static QStringList QUrl.idnWhitelist()'''
        return QStringList()
    def toAce(self):
        '''static QString QUrl.toAce()'''
        return QString()
    def fromAce(self):
        '''static QByteArray QUrl.fromAce()'''
        return QByteArray()
    def errorString(self):
        '''QString QUrl.errorString()'''
        return QString()
    def hasFragment(self):
        '''bool QUrl.hasFragment()'''
        return bool()
    def hasQuery(self):
        '''bool QUrl.hasQuery()'''
        return bool()
    def toPunycode(self):
        '''static QString QUrl.toPunycode()'''
        return QString()
    def fromPunycode(self):
        '''static QByteArray QUrl.fromPunycode()'''
        return QByteArray()
    def toPercentEncoding(self, input, exclude = QByteArray(), include = QByteArray()):
        '''static QByteArray QUrl.toPercentEncoding(QString input, QByteArray exclude = QByteArray(), QByteArray include = QByteArray())'''
        return QByteArray()
    def fromPercentEncoding(self):
        '''static QByteArray QUrl.fromPercentEncoding()'''
        return QByteArray()
    def __ne__(self, url):
        '''bool QUrl.__ne__(QUrl url)'''
        return bool()
    def __eq__(self, url):
        '''bool QUrl.__eq__(QUrl url)'''
        return bool()
    def __lt__(self, url):
        '''bool QUrl.__lt__(QUrl url)'''
        return bool()
    def isDetached(self):
        '''bool QUrl.isDetached()'''
        return bool()
    def detach(self):
        '''void QUrl.detach()'''
    def fromEncoded(self, url):
        '''static QUrl QUrl.fromEncoded(QByteArray url)'''
        return QUrl()
    def fromEncoded(self, url, mode):
        '''static QUrl QUrl.fromEncoded(QByteArray url, QUrl.ParsingMode mode)'''
        return QUrl()
    def toEncoded(self, options = QUrl.None):
        '''QByteArray QUrl.toEncoded(QUrl.FormattingOptions options = QUrl.None)'''
        return QByteArray()
    def toString(self, options = QUrl.None):
        '''QString QUrl.toString(QUrl.FormattingOptions options = QUrl.None)'''
        return QString()
    def toLocalFile(self):
        '''QString QUrl.toLocalFile()'''
        return QString()
    def fromLocalFile(self, localfile):
        '''static QUrl QUrl.fromLocalFile(QString localfile)'''
        return QUrl()
    def isParentOf(self, url):
        '''bool QUrl.isParentOf(QUrl url)'''
        return bool()
    def isRelative(self):
        '''bool QUrl.isRelative()'''
        return bool()
    def resolved(self, relative):
        '''QUrl QUrl.resolved(QUrl relative)'''
        return QUrl()
    def fragment(self):
        '''QString QUrl.fragment()'''
        return QString()
    def setFragment(self, fragment):
        '''void QUrl.setFragment(QString fragment)'''
    def removeAllQueryItems(self, key):
        '''void QUrl.removeAllQueryItems(QString key)'''
    def removeQueryItem(self, key):
        '''void QUrl.removeQueryItem(QString key)'''
    def allQueryItemValues(self, key):
        '''QStringList QUrl.allQueryItemValues(QString key)'''
        return QStringList()
    def queryItemValue(self, key):
        '''QString QUrl.queryItemValue(QString key)'''
        return QString()
    def hasQueryItem(self, key):
        '''bool QUrl.hasQueryItem(QString key)'''
        return bool()
    def queryItems(self):
        '''list-of-tuple-of-QString-QString QUrl.queryItems()'''
        return [tuple-of-QString-QString()]
    def addQueryItem(self, key, value):
        '''void QUrl.addQueryItem(QString key, QString value)'''
    def setQueryItems(self, query):
        '''void QUrl.setQueryItems(list-of-tuple-of-QString-QString query)'''
    def queryPairDelimiter(self):
        '''str QUrl.queryPairDelimiter()'''
        return str()
    def queryValueDelimiter(self):
        '''str QUrl.queryValueDelimiter()'''
        return str()
    def setQueryDelimiters(self, valueDelimiter, pairDelimiter):
        '''void QUrl.setQueryDelimiters(str valueDelimiter, str pairDelimiter)'''
    def encodedQuery(self):
        '''QByteArray QUrl.encodedQuery()'''
        return QByteArray()
    def setEncodedQuery(self, query):
        '''void QUrl.setEncodedQuery(QByteArray query)'''
    def path(self):
        '''QString QUrl.path()'''
        return QString()
    def setPath(self, path):
        '''void QUrl.setPath(QString path)'''
    def port(self):
        '''int QUrl.port()'''
        return int()
    def port(self, defaultPort):
        '''int QUrl.port(int defaultPort)'''
        return int()
    def setPort(self, port):
        '''void QUrl.setPort(int port)'''
    def host(self):
        '''QString QUrl.host()'''
        return QString()
    def setHost(self, host):
        '''void QUrl.setHost(QString host)'''
    def password(self):
        '''QString QUrl.password()'''
        return QString()
    def setPassword(self, password):
        '''void QUrl.setPassword(QString password)'''
    def userName(self):
        '''QString QUrl.userName()'''
        return QString()
    def setUserName(self, userName):
        '''void QUrl.setUserName(QString userName)'''
    def userInfo(self):
        '''QString QUrl.userInfo()'''
        return QString()
    def setUserInfo(self, userInfo):
        '''void QUrl.setUserInfo(QString userInfo)'''
    def authority(self):
        '''QString QUrl.authority()'''
        return QString()
    def setAuthority(self, authority):
        '''void QUrl.setAuthority(QString authority)'''
    def scheme(self):
        '''QString QUrl.scheme()'''
        return QString()
    def setScheme(self, scheme):
        '''void QUrl.setScheme(QString scheme)'''
    def clear(self):
        '''void QUrl.clear()'''
    def isEmpty(self):
        '''bool QUrl.isEmpty()'''
        return bool()
    def isValid(self):
        '''bool QUrl.isValid()'''
        return bool()
    def setEncodedUrl(self, url):
        '''void QUrl.setEncodedUrl(QByteArray url)'''
    def setEncodedUrl(self, url, mode):
        '''void QUrl.setEncodedUrl(QByteArray url, QUrl.ParsingMode mode)'''
    def setUrl(self, url):
        '''void QUrl.setUrl(QString url)'''
    def setUrl(self, url, mode):
        '''void QUrl.setUrl(QString url, QUrl.ParsingMode mode)'''
    def __hash__(self):
        '''int QUrl.__hash__()'''
        return int()
    def __repr__(self):
        '''str QUrl.__repr__()'''
        return str()
    class FormattingOptions():
        """"""
        def __init__(self):
            '''QUrl.FormattingOptions QUrl.FormattingOptions.__init__()'''
            return QUrl.FormattingOptions()
        def __init__(self):
            '''int QUrl.FormattingOptions.__init__()'''
            return int()
        def __init__(self):
            '''void QUrl.FormattingOptions.__init__()'''
        def __bool__(self):
            '''int QUrl.FormattingOptions.__bool__()'''
            return int()
        def __ne__(self, f):
            '''bool QUrl.FormattingOptions.__ne__(QUrl.FormattingOptions f)'''
            return bool()
        def __eq__(self, f):
            '''bool QUrl.FormattingOptions.__eq__(QUrl.FormattingOptions f)'''
            return bool()
        def __invert__(self):
            '''QUrl.FormattingOptions QUrl.FormattingOptions.__invert__()'''
            return QUrl.FormattingOptions()
        def __and__(self, mask):
            '''QUrl.FormattingOptions QUrl.FormattingOptions.__and__(int mask)'''
            return QUrl.FormattingOptions()
        def __xor__(self, f):
            '''QUrl.FormattingOptions QUrl.FormattingOptions.__xor__(QUrl.FormattingOptions f)'''
            return QUrl.FormattingOptions()
        def __xor__(self, f):
            '''QUrl.FormattingOptions QUrl.FormattingOptions.__xor__(int f)'''
            return QUrl.FormattingOptions()
        def __or__(self, f):
            '''QUrl.FormattingOptions QUrl.FormattingOptions.__or__(QUrl.FormattingOptions f)'''
            return QUrl.FormattingOptions()
        def __or__(self, f):
            '''QUrl.FormattingOptions QUrl.FormattingOptions.__or__(int f)'''
            return QUrl.FormattingOptions()
        def __int__(self):
            '''int QUrl.FormattingOptions.__int__()'''
            return int()
        def __ixor__(self, f):
            '''QUrl.FormattingOptions QUrl.FormattingOptions.__ixor__(QUrl.FormattingOptions f)'''
            return QUrl.FormattingOptions()
        def __ior__(self, f):
            '''QUrl.FormattingOptions QUrl.FormattingOptions.__ior__(QUrl.FormattingOptions f)'''
            return QUrl.FormattingOptions()
        def __iand__(self, mask):
            '''QUrl.FormattingOptions QUrl.FormattingOptions.__iand__(int mask)'''
            return QUrl.FormattingOptions()


class QUuid():
    """"""
    # Enum QUuid.Version
    VerUnknown = 0
    Time = 0
    EmbeddedPOSIX = 0
    Name = 0
    Random = 0

    # Enum QUuid.Variant
    VarUnknown = 0
    NCS = 0
    DCE = 0
    Microsoft = 0
    Reserved = 0

    def __init__(self):
        '''void QUuid.__init__()'''
    def __init__(self, l, w1, w2, b1, b2, b3, b4, b5, b6, b7, b8):
        '''void QUuid.__init__(int l, int w1, int w2, str b1, str b2, str b3, str b4, str b5, str b6, str b7, str b8)'''
    def __init__(self):
        '''QString QUuid.__init__()'''
        return QString()
    def __init__(self):
        '''QByteArray QUuid.__init__()'''
        return QByteArray()
    def __init__(self):
        '''QUuid QUuid.__init__()'''
        return QUuid()
    def __ge__(self, other):
        '''bool QUuid.__ge__(QUuid other)'''
        return bool()
    def __le__(self, other):
        '''bool QUuid.__le__(QUuid other)'''
        return bool()
    def fromRfc4122(self):
        '''static QByteArray QUuid.fromRfc4122()'''
        return QByteArray()
    def toRfc4122(self):
        '''QByteArray QUuid.toRfc4122()'''
        return QByteArray()
    def toByteArray(self):
        '''QByteArray QUuid.toByteArray()'''
        return QByteArray()
    def version(self):
        '''QUuid.Version QUuid.version()'''
        return QUuid.Version()
    def variant(self):
        '''QUuid.Variant QUuid.variant()'''
        return QUuid.Variant()
    def createUuid(self):
        '''static QUuid QUuid.createUuid()'''
        return QUuid()
    def __gt__(self, other):
        '''bool QUuid.__gt__(QUuid other)'''
        return bool()
    def __lt__(self, other):
        '''bool QUuid.__lt__(QUuid other)'''
        return bool()
    def __ne__(self, orig):
        '''bool QUuid.__ne__(QUuid orig)'''
        return bool()
    def __eq__(self, orig):
        '''bool QUuid.__eq__(QUuid orig)'''
        return bool()
    def isNull(self):
        '''bool QUuid.isNull()'''
        return bool()
    def toString(self):
        '''QString QUuid.toString()'''
        return QString()
    def __repr__(self):
        '''str QUuid.__repr__()'''
        return str()


class QVariant():
    """"""
    # Enum QVariant.Type
    Invalid = 0
    Bool = 0
    Int = 0
    UInt = 0
    LongLong = 0
    ULongLong = 0
    Double = 0
    Char = 0
    Map = 0
    List = 0
    String = 0
    StringList = 0
    ByteArray = 0
    BitArray = 0
    Date = 0
    Time = 0
    DateTime = 0
    Url = 0
    Locale = 0
    Rect = 0
    RectF = 0
    Size = 0
    SizeF = 0
    Line = 0
    LineF = 0
    Point = 0
    PointF = 0
    RegExp = 0
    Font = 0
    Pixmap = 0
    Brush = 0
    Color = 0
    Palette = 0
    Icon = 0
    Image = 0
    Polygon = 0
    Region = 0
    Bitmap = 0
    Cursor = 0
    SizePolicy = 0
    KeySequence = 0
    Pen = 0
    TextLength = 0
    TextFormat = 0
    Matrix = 0
    Transform = 0
    Hash = 0
    Matrix4x4 = 0
    Vector2D = 0
    Vector3D = 0
    Vector4D = 0
    Quaternion = 0
    EasingCurve = 0
    UserType = 0

    def __init__(self):
        '''void QVariant.__init__()'''
    def __init__(self, type):
        '''void QVariant.__init__(Type type)'''
    def __init__(self, typeOrUserType, copy):
        '''void QVariant.__init__(int typeOrUserType, sip.voidptr copy)'''
    def __init__(self, other):
        '''void QVariant.__init__(QVariant other)'''
    def __init__(self):
        '''object QVariant.__init__()'''
        return object()
    def swap(self, other):
        '''void QVariant.swap(QVariant other)'''
    def toEasingCurve(self):
        '''QEasingCurve QVariant.toEasingCurve()'''
        return QEasingCurve()
    def toReal(self, ok):
        '''float QVariant.toReal(bool ok)'''
        return float()
    def toFloat(self, ok):
        '''float QVariant.toFloat(bool ok)'''
        return float()
    def __ne__(self, v):
        '''bool QVariant.__ne__(QVariant v)'''
        return bool()
    def __eq__(self, v):
        '''bool QVariant.__eq__(QVariant v)'''
        return bool()
    def data(self):
        '''sip.voidptr QVariant.data()'''
        return sip.voidptr()
    def nameToType(self, name):
        '''static Type QVariant.nameToType(str name)'''
        return Type()
    def typeToName(self, type):
        '''static str QVariant.typeToName(Type type)'''
        return str()
    def save(self, ds):
        '''void QVariant.save(QDataStream ds)'''
    def load(self, ds):
        '''void QVariant.load(QDataStream ds)'''
    def toPyObject(self):
        '''object QVariant.toPyObject()'''
        return object()
    def toRegExp(self):
        '''QRegExp QVariant.toRegExp()'''
        return QRegExp()
    def toLocale(self):
        '''QLocale QVariant.toLocale()'''
        return QLocale()
    def toUrl(self):
        '''QUrl QVariant.toUrl()'''
        return QUrl()
    def toRectF(self):
        '''QRectF QVariant.toRectF()'''
        return QRectF()
    def toRect(self):
        '''QRect QVariant.toRect()'''
        return QRect()
    def toLineF(self):
        '''QLineF QVariant.toLineF()'''
        return QLineF()
    def toLine(self):
        '''QLine QVariant.toLine()'''
        return QLine()
    def toSizeF(self):
        '''QSizeF QVariant.toSizeF()'''
        return QSizeF()
    def toSize(self):
        '''QSize QVariant.toSize()'''
        return QSize()
    def toPointF(self):
        '''QPointF QVariant.toPointF()'''
        return QPointF()
    def toPoint(self):
        '''QPoint QVariant.toPoint()'''
        return QPoint()
    def toHash(self):
        '''dict-of-QString-QVariant QVariant.toHash()'''
        return dict-of-QString-QVariant()
    def toMap(self):
        '''dict-of-QString-QVariant QVariant.toMap()'''
        return dict-of-QString-QVariant()
    def toList(self):
        '''list-of-QVariant QVariant.toList()'''
        return [QVariant()]
    def toDateTime(self):
        '''QDateTime QVariant.toDateTime()'''
        return QDateTime()
    def toTime(self):
        '''QTime QVariant.toTime()'''
        return QTime()
    def toDate(self):
        '''QDate QVariant.toDate()'''
        return QDate()
    def toChar(self):
        '''QChar QVariant.toChar()'''
        return QChar()
    def toStringList(self):
        '''QStringList QVariant.toStringList()'''
        return QStringList()
    def toString(self):
        '''QString QVariant.toString()'''
        return QString()
    def toBitArray(self):
        '''QBitArray QVariant.toBitArray()'''
        return QBitArray()
    def toByteArray(self):
        '''QByteArray QVariant.toByteArray()'''
        return QByteArray()
    def toDouble(self, ok):
        '''float QVariant.toDouble(bool ok)'''
        return float()
    def toBool(self):
        '''bool QVariant.toBool()'''
        return bool()
    def toULongLong(self, ok):
        '''int QVariant.toULongLong(bool ok)'''
        return int()
    def toLongLong(self, ok):
        '''int QVariant.toLongLong(bool ok)'''
        return int()
    def toUInt(self, ok):
        '''int QVariant.toUInt(bool ok)'''
        return int()
    def toInt(self, ok):
        '''int QVariant.toInt(bool ok)'''
        return int()
    def isDetached(self):
        '''bool QVariant.isDetached()'''
        return bool()
    def detach(self):
        '''void QVariant.detach()'''
    def clear(self):
        '''void QVariant.clear()'''
    def isNull(self):
        '''bool QVariant.isNull()'''
        return bool()
    def isValid(self):
        '''bool QVariant.isValid()'''
        return bool()
    def convert(self, t):
        '''bool QVariant.convert(Type t)'''
        return bool()
    def canConvert(self, t):
        '''bool QVariant.canConvert(Type t)'''
        return bool()
    def typeName(self):
        '''str QVariant.typeName()'''
        return str()
    def userType(self):
        '''int QVariant.userType()'''
        return int()
    def type(self):
        '''Type QVariant.type()'''
        return Type()
    def fromMap(self, map):
        '''static QVariant QVariant.fromMap(dict-of-QString-QVariant map)'''
        return QVariant()
    def fromList(self, list):
        '''static QVariant QVariant.fromList(list-of-QVariant list)'''
        return QVariant()


class QWaitCondition():
    """"""
    def __init__(self):
        '''void QWaitCondition.__init__()'''
    def wakeAll(self):
        '''void QWaitCondition.wakeAll()'''
    def wakeOne(self):
        '''void QWaitCondition.wakeOne()'''
    def wait(self, mutex, msecs = ULONG_MAX):
        '''bool QWaitCondition.wait(QMutex mutex, int msecs = ULONG_MAX)'''
        return bool()
    def wait(self, readWriteLock, msecs = ULONG_MAX):
        '''bool QWaitCondition.wait(QReadWriteLock readWriteLock, int msecs = ULONG_MAX)'''
        return bool()


class QXmlStreamAttribute():
    """"""
    def __init__(self):
        '''void QXmlStreamAttribute.__init__()'''
    def __init__(self, qualifiedName, value):
        '''void QXmlStreamAttribute.__init__(QString qualifiedName, QString value)'''
    def __init__(self, namespaceUri, name, value):
        '''void QXmlStreamAttribute.__init__(QString namespaceUri, QString name, QString value)'''
    def __init__(self):
        '''QXmlStreamAttribute QXmlStreamAttribute.__init__()'''
        return QXmlStreamAttribute()
    def __ne__(self, other):
        '''bool QXmlStreamAttribute.__ne__(QXmlStreamAttribute other)'''
        return bool()
    def __eq__(self, other):
        '''bool QXmlStreamAttribute.__eq__(QXmlStreamAttribute other)'''
        return bool()
    def isDefault(self):
        '''bool QXmlStreamAttribute.isDefault()'''
        return bool()
    def value(self):
        '''QStringRef QXmlStreamAttribute.value()'''
        return QStringRef()
    def prefix(self):
        '''QStringRef QXmlStreamAttribute.prefix()'''
        return QStringRef()
    def qualifiedName(self):
        '''QStringRef QXmlStreamAttribute.qualifiedName()'''
        return QStringRef()
    def name(self):
        '''QStringRef QXmlStreamAttribute.name()'''
        return QStringRef()
    def namespaceUri(self):
        '''QStringRef QXmlStreamAttribute.namespaceUri()'''
        return QStringRef()


class QXmlStreamAttributes():
    """"""
    def __init__(self):
        '''void QXmlStreamAttributes.__init__()'''
    def __init__(self):
        '''QXmlStreamAttributes QXmlStreamAttributes.__init__()'''
        return QXmlStreamAttributes()
    def __contains__(self, value):
        '''int QXmlStreamAttributes.__contains__(QXmlStreamAttribute value)'''
        return int()
    def __delitem__(self, i):
        '''void QXmlStreamAttributes.__delitem__(int i)'''
    def __delitem__(self, slice):
        '''void QXmlStreamAttributes.__delitem__(slice slice)'''
    def __setitem__(self, i, value):
        '''void QXmlStreamAttributes.__setitem__(int i, QXmlStreamAttribute value)'''
    def __setitem__(self, slice, list):
        '''void QXmlStreamAttributes.__setitem__(slice slice, QXmlStreamAttributes list)'''
    def __getitem__(self, i):
        '''QXmlStreamAttribute QXmlStreamAttributes.__getitem__(int i)'''
        return QXmlStreamAttribute()
    def __getitem__(self, slice):
        '''QXmlStreamAttributes QXmlStreamAttributes.__getitem__(slice slice)'''
        return QXmlStreamAttributes()
    def __eq__(self, other):
        '''bool QXmlStreamAttributes.__eq__(QXmlStreamAttributes other)'''
        return bool()
    def __iadd__(self, other):
        '''QXmlStreamAttributes QXmlStreamAttributes.__iadd__(QXmlStreamAttributes other)'''
        return QXmlStreamAttributes()
    def __iadd__(self, value):
        '''QXmlStreamAttributes QXmlStreamAttributes.__iadd__(QXmlStreamAttribute value)'''
        return QXmlStreamAttributes()
    def __ne__(self, other):
        '''bool QXmlStreamAttributes.__ne__(QXmlStreamAttributes other)'''
        return bool()
    def size(self):
        '''int QXmlStreamAttributes.size()'''
        return int()
    def replace(self, i, value):
        '''void QXmlStreamAttributes.replace(int i, QXmlStreamAttribute value)'''
    def remove(self, i):
        '''void QXmlStreamAttributes.remove(int i)'''
    def remove(self, i, count):
        '''void QXmlStreamAttributes.remove(int i, int count)'''
    def prepend(self, value):
        '''void QXmlStreamAttributes.prepend(QXmlStreamAttribute value)'''
    def lastIndexOf(self, value, from_ = -1):
        '''int QXmlStreamAttributes.lastIndexOf(QXmlStreamAttribute value, int from = -1)'''
        return int()
    def last(self):
        '''QXmlStreamAttribute QXmlStreamAttributes.last()'''
        return QXmlStreamAttribute()
    def isEmpty(self):
        '''bool QXmlStreamAttributes.isEmpty()'''
        return bool()
    def insert(self, i, value):
        '''void QXmlStreamAttributes.insert(int i, QXmlStreamAttribute value)'''
    def indexOf(self, value, from_ = 0):
        '''int QXmlStreamAttributes.indexOf(QXmlStreamAttribute value, int from = 0)'''
        return int()
    def first(self):
        '''QXmlStreamAttribute QXmlStreamAttributes.first()'''
        return QXmlStreamAttribute()
    def fill(self, value, size = -1):
        '''void QXmlStreamAttributes.fill(QXmlStreamAttribute value, int size = -1)'''
    def data(self):
        '''sip.voidptr QXmlStreamAttributes.data()'''
        return sip.voidptr()
    def __len__(self):
        ''' QXmlStreamAttributes.__len__()'''
        return ()
    def count(self, value):
        '''int QXmlStreamAttributes.count(QXmlStreamAttribute value)'''
        return int()
    def count(self):
        '''int QXmlStreamAttributes.count()'''
        return int()
    def contains(self, value):
        '''bool QXmlStreamAttributes.contains(QXmlStreamAttribute value)'''
        return bool()
    def clear(self):
        '''void QXmlStreamAttributes.clear()'''
    def at(self, i):
        '''QXmlStreamAttribute QXmlStreamAttributes.at(int i)'''
        return QXmlStreamAttribute()
    def hasAttribute(self, qualifiedName):
        '''bool QXmlStreamAttributes.hasAttribute(QString qualifiedName)'''
        return bool()
    def hasAttribute(self, namespaceUri, name):
        '''bool QXmlStreamAttributes.hasAttribute(QString namespaceUri, QString name)'''
        return bool()
    def append(self, namespaceUri, name, value):
        '''void QXmlStreamAttributes.append(QString namespaceUri, QString name, QString value)'''
    def append(self, qualifiedName, value):
        '''void QXmlStreamAttributes.append(QString qualifiedName, QString value)'''
    def append(self, attribute):
        '''void QXmlStreamAttributes.append(QXmlStreamAttribute attribute)'''
    def value(self, namespaceUri, name):
        '''QStringRef QXmlStreamAttributes.value(QString namespaceUri, QString name)'''
        return QStringRef()
    def value(self, qualifiedName):
        '''QStringRef QXmlStreamAttributes.value(QString qualifiedName)'''
        return QStringRef()


class QXmlStreamNamespaceDeclaration():
    """"""
    def __init__(self):
        '''void QXmlStreamNamespaceDeclaration.__init__()'''
    def __init__(self):
        '''QXmlStreamNamespaceDeclaration QXmlStreamNamespaceDeclaration.__init__()'''
        return QXmlStreamNamespaceDeclaration()
    def __init__(self, prefix, namespaceUri):
        '''void QXmlStreamNamespaceDeclaration.__init__(QString prefix, QString namespaceUri)'''
    def __ne__(self, other):
        '''bool QXmlStreamNamespaceDeclaration.__ne__(QXmlStreamNamespaceDeclaration other)'''
        return bool()
    def __eq__(self, other):
        '''bool QXmlStreamNamespaceDeclaration.__eq__(QXmlStreamNamespaceDeclaration other)'''
        return bool()
    def namespaceUri(self):
        '''QStringRef QXmlStreamNamespaceDeclaration.namespaceUri()'''
        return QStringRef()
    def prefix(self):
        '''QStringRef QXmlStreamNamespaceDeclaration.prefix()'''
        return QStringRef()


class QXmlStreamNotationDeclaration():
    """"""
    def __init__(self):
        '''void QXmlStreamNotationDeclaration.__init__()'''
    def __init__(self):
        '''QXmlStreamNotationDeclaration QXmlStreamNotationDeclaration.__init__()'''
        return QXmlStreamNotationDeclaration()
    def __ne__(self, other):
        '''bool QXmlStreamNotationDeclaration.__ne__(QXmlStreamNotationDeclaration other)'''
        return bool()
    def __eq__(self, other):
        '''bool QXmlStreamNotationDeclaration.__eq__(QXmlStreamNotationDeclaration other)'''
        return bool()
    def publicId(self):
        '''QStringRef QXmlStreamNotationDeclaration.publicId()'''
        return QStringRef()
    def systemId(self):
        '''QStringRef QXmlStreamNotationDeclaration.systemId()'''
        return QStringRef()
    def name(self):
        '''QStringRef QXmlStreamNotationDeclaration.name()'''
        return QStringRef()


class QXmlStreamEntityDeclaration():
    """"""
    def __init__(self):
        '''void QXmlStreamEntityDeclaration.__init__()'''
    def __init__(self):
        '''QXmlStreamEntityDeclaration QXmlStreamEntityDeclaration.__init__()'''
        return QXmlStreamEntityDeclaration()
    def __ne__(self, other):
        '''bool QXmlStreamEntityDeclaration.__ne__(QXmlStreamEntityDeclaration other)'''
        return bool()
    def __eq__(self, other):
        '''bool QXmlStreamEntityDeclaration.__eq__(QXmlStreamEntityDeclaration other)'''
        return bool()
    def value(self):
        '''QStringRef QXmlStreamEntityDeclaration.value()'''
        return QStringRef()
    def publicId(self):
        '''QStringRef QXmlStreamEntityDeclaration.publicId()'''
        return QStringRef()
    def systemId(self):
        '''QStringRef QXmlStreamEntityDeclaration.systemId()'''
        return QStringRef()
    def notationName(self):
        '''QStringRef QXmlStreamEntityDeclaration.notationName()'''
        return QStringRef()
    def name(self):
        '''QStringRef QXmlStreamEntityDeclaration.name()'''
        return QStringRef()


class QXmlStreamEntityResolver():
    """"""
    def __init__(self):
        '''void QXmlStreamEntityResolver.__init__()'''
    def __init__(self):
        '''QXmlStreamEntityResolver QXmlStreamEntityResolver.__init__()'''
        return QXmlStreamEntityResolver()
    def resolveUndeclaredEntity(self, name):
        '''QString QXmlStreamEntityResolver.resolveUndeclaredEntity(QString name)'''
        return QString()


class QXmlStreamReader():
    """"""
    # Enum QXmlStreamReader.ReadElementTextBehaviour
    ErrorOnUnexpectedElement = 0
    IncludeChildElements = 0
    SkipChildElements = 0

    # Enum QXmlStreamReader.Error
    NoError = 0
    UnexpectedElementError = 0
    CustomError = 0
    NotWellFormedError = 0
    PrematureEndOfDocumentError = 0

    # Enum QXmlStreamReader.TokenType
    NoToken = 0
    Invalid = 0
    StartDocument = 0
    EndDocument = 0
    StartElement = 0
    EndElement = 0
    Characters = 0
    Comment = 0
    DTD = 0
    EntityReference = 0
    ProcessingInstruction = 0

    def __init__(self):
        '''void QXmlStreamReader.__init__()'''
    def __init__(self, device):
        '''void QXmlStreamReader.__init__(QIODevice device)'''
    def __init__(self, data):
        '''void QXmlStreamReader.__init__(QByteArray data)'''
    def __init__(self, data):
        '''void QXmlStreamReader.__init__(QString data)'''
    def skipCurrentElement(self):
        '''void QXmlStreamReader.skipCurrentElement()'''
    def readNextStartElement(self):
        '''bool QXmlStreamReader.readNextStartElement()'''
        return bool()
    def entityResolver(self):
        '''QXmlStreamEntityResolver QXmlStreamReader.entityResolver()'''
        return QXmlStreamEntityResolver()
    def setEntityResolver(self, resolver):
        '''void QXmlStreamReader.setEntityResolver(QXmlStreamEntityResolver resolver)'''
    def hasError(self):
        '''bool QXmlStreamReader.hasError()'''
        return bool()
    def error(self):
        '''QXmlStreamReader.Error QXmlStreamReader.error()'''
        return QXmlStreamReader.Error()
    def errorString(self):
        '''QString QXmlStreamReader.errorString()'''
        return QString()
    def raiseError(self, message = QString()):
        '''void QXmlStreamReader.raiseError(QString message = QString())'''
    def dtdSystemId(self):
        '''QStringRef QXmlStreamReader.dtdSystemId()'''
        return QStringRef()
    def dtdPublicId(self):
        '''QStringRef QXmlStreamReader.dtdPublicId()'''
        return QStringRef()
    def dtdName(self):
        '''QStringRef QXmlStreamReader.dtdName()'''
        return QStringRef()
    def entityDeclarations(self):
        '''list-of-QXmlStreamEntityDeclaration QXmlStreamReader.entityDeclarations()'''
        return [QXmlStreamEntityDeclaration()]
    def notationDeclarations(self):
        '''list-of-QXmlStreamNotationDeclaration QXmlStreamReader.notationDeclarations()'''
        return [QXmlStreamNotationDeclaration()]
    def addExtraNamespaceDeclarations(self, extraNamespaceDeclaractions):
        '''void QXmlStreamReader.addExtraNamespaceDeclarations(list-of-QXmlStreamNamespaceDeclaration extraNamespaceDeclaractions)'''
    def addExtraNamespaceDeclaration(self, extraNamespaceDeclaraction):
        '''void QXmlStreamReader.addExtraNamespaceDeclaration(QXmlStreamNamespaceDeclaration extraNamespaceDeclaraction)'''
    def namespaceDeclarations(self):
        '''list-of-QXmlStreamNamespaceDeclaration QXmlStreamReader.namespaceDeclarations()'''
        return [QXmlStreamNamespaceDeclaration()]
    def text(self):
        '''QStringRef QXmlStreamReader.text()'''
        return QStringRef()
    def processingInstructionData(self):
        '''QStringRef QXmlStreamReader.processingInstructionData()'''
        return QStringRef()
    def processingInstructionTarget(self):
        '''QStringRef QXmlStreamReader.processingInstructionTarget()'''
        return QStringRef()
    def prefix(self):
        '''QStringRef QXmlStreamReader.prefix()'''
        return QStringRef()
    def qualifiedName(self):
        '''QStringRef QXmlStreamReader.qualifiedName()'''
        return QStringRef()
    def namespaceUri(self):
        '''QStringRef QXmlStreamReader.namespaceUri()'''
        return QStringRef()
    def name(self):
        '''QStringRef QXmlStreamReader.name()'''
        return QStringRef()
    def readElementText(self):
        '''QString QXmlStreamReader.readElementText()'''
        return QString()
    def readElementText(self, behaviour):
        '''QString QXmlStreamReader.readElementText(QXmlStreamReader.ReadElementTextBehaviour behaviour)'''
        return QString()
    def attributes(self):
        '''QXmlStreamAttributes QXmlStreamReader.attributes()'''
        return QXmlStreamAttributes()
    def characterOffset(self):
        '''int QXmlStreamReader.characterOffset()'''
        return int()
    def columnNumber(self):
        '''int QXmlStreamReader.columnNumber()'''
        return int()
    def lineNumber(self):
        '''int QXmlStreamReader.lineNumber()'''
        return int()
    def documentEncoding(self):
        '''QStringRef QXmlStreamReader.documentEncoding()'''
        return QStringRef()
    def documentVersion(self):
        '''QStringRef QXmlStreamReader.documentVersion()'''
        return QStringRef()
    def isStandaloneDocument(self):
        '''bool QXmlStreamReader.isStandaloneDocument()'''
        return bool()
    def isProcessingInstruction(self):
        '''bool QXmlStreamReader.isProcessingInstruction()'''
        return bool()
    def isEntityReference(self):
        '''bool QXmlStreamReader.isEntityReference()'''
        return bool()
    def isDTD(self):
        '''bool QXmlStreamReader.isDTD()'''
        return bool()
    def isComment(self):
        '''bool QXmlStreamReader.isComment()'''
        return bool()
    def isCDATA(self):
        '''bool QXmlStreamReader.isCDATA()'''
        return bool()
    def isWhitespace(self):
        '''bool QXmlStreamReader.isWhitespace()'''
        return bool()
    def isCharacters(self):
        '''bool QXmlStreamReader.isCharacters()'''
        return bool()
    def isEndElement(self):
        '''bool QXmlStreamReader.isEndElement()'''
        return bool()
    def isStartElement(self):
        '''bool QXmlStreamReader.isStartElement()'''
        return bool()
    def isEndDocument(self):
        '''bool QXmlStreamReader.isEndDocument()'''
        return bool()
    def isStartDocument(self):
        '''bool QXmlStreamReader.isStartDocument()'''
        return bool()
    def namespaceProcessing(self):
        '''bool QXmlStreamReader.namespaceProcessing()'''
        return bool()
    def setNamespaceProcessing(self):
        '''bool QXmlStreamReader.setNamespaceProcessing()'''
        return bool()
    def tokenString(self):
        '''QString QXmlStreamReader.tokenString()'''
        return QString()
    def tokenType(self):
        '''QXmlStreamReader.TokenType QXmlStreamReader.tokenType()'''
        return QXmlStreamReader.TokenType()
    def readNext(self):
        '''QXmlStreamReader.TokenType QXmlStreamReader.readNext()'''
        return QXmlStreamReader.TokenType()
    def atEnd(self):
        '''bool QXmlStreamReader.atEnd()'''
        return bool()
    def clear(self):
        '''void QXmlStreamReader.clear()'''
    def addData(self, data):
        '''void QXmlStreamReader.addData(QByteArray data)'''
    def addData(self, data):
        '''void QXmlStreamReader.addData(QString data)'''
    def device(self):
        '''QIODevice QXmlStreamReader.device()'''
        return QIODevice()
    def setDevice(self, device):
        '''void QXmlStreamReader.setDevice(QIODevice device)'''


class QXmlStreamWriter():
    """"""
    def __init__(self):
        '''void QXmlStreamWriter.__init__()'''
    def __init__(self, device):
        '''void QXmlStreamWriter.__init__(QIODevice device)'''
    def __init__(self, array):
        '''void QXmlStreamWriter.__init__(QByteArray array)'''
    def __init__(self, string):
        '''void QXmlStreamWriter.__init__(QString string)'''
    def hasError(self):
        '''bool QXmlStreamWriter.hasError()'''
        return bool()
    def writeCurrentToken(self, reader):
        '''void QXmlStreamWriter.writeCurrentToken(QXmlStreamReader reader)'''
    def writeStartElement(self, qualifiedName):
        '''void QXmlStreamWriter.writeStartElement(QString qualifiedName)'''
    def writeStartElement(self, namespaceUri, name):
        '''void QXmlStreamWriter.writeStartElement(QString namespaceUri, QString name)'''
    def writeStartDocument(self):
        '''void QXmlStreamWriter.writeStartDocument()'''
    def writeStartDocument(self, version):
        '''void QXmlStreamWriter.writeStartDocument(QString version)'''
    def writeStartDocument(self, version, standalone):
        '''void QXmlStreamWriter.writeStartDocument(QString version, bool standalone)'''
    def writeProcessingInstruction(self, target, data = QString()):
        '''void QXmlStreamWriter.writeProcessingInstruction(QString target, QString data = QString())'''
    def writeDefaultNamespace(self, namespaceUri):
        '''void QXmlStreamWriter.writeDefaultNamespace(QString namespaceUri)'''
    def writeNamespace(self, namespaceUri, prefix = QString()):
        '''void QXmlStreamWriter.writeNamespace(QString namespaceUri, QString prefix = QString())'''
    def writeEntityReference(self, name):
        '''void QXmlStreamWriter.writeEntityReference(QString name)'''
    def writeEndElement(self):
        '''void QXmlStreamWriter.writeEndElement()'''
    def writeEndDocument(self):
        '''void QXmlStreamWriter.writeEndDocument()'''
    def writeTextElement(self, qualifiedName, text):
        '''void QXmlStreamWriter.writeTextElement(QString qualifiedName, QString text)'''
    def writeTextElement(self, namespaceUri, name, text):
        '''void QXmlStreamWriter.writeTextElement(QString namespaceUri, QString name, QString text)'''
    def writeEmptyElement(self, qualifiedName):
        '''void QXmlStreamWriter.writeEmptyElement(QString qualifiedName)'''
    def writeEmptyElement(self, namespaceUri, name):
        '''void QXmlStreamWriter.writeEmptyElement(QString namespaceUri, QString name)'''
    def writeDTD(self, dtd):
        '''void QXmlStreamWriter.writeDTD(QString dtd)'''
    def writeComment(self, text):
        '''void QXmlStreamWriter.writeComment(QString text)'''
    def writeCharacters(self, text):
        '''void QXmlStreamWriter.writeCharacters(QString text)'''
    def writeCDATA(self, text):
        '''void QXmlStreamWriter.writeCDATA(QString text)'''
    def writeAttributes(self, attributes):
        '''void QXmlStreamWriter.writeAttributes(QXmlStreamAttributes attributes)'''
    def writeAttribute(self, qualifiedName, value):
        '''void QXmlStreamWriter.writeAttribute(QString qualifiedName, QString value)'''
    def writeAttribute(self, namespaceUri, name, value):
        '''void QXmlStreamWriter.writeAttribute(QString namespaceUri, QString name, QString value)'''
    def writeAttribute(self, attribute):
        '''void QXmlStreamWriter.writeAttribute(QXmlStreamAttribute attribute)'''
    def autoFormattingIndent(self):
        '''int QXmlStreamWriter.autoFormattingIndent()'''
        return int()
    def setAutoFormattingIndent(self, spaces):
        '''void QXmlStreamWriter.setAutoFormattingIndent(int spaces)'''
    def autoFormatting(self):
        '''bool QXmlStreamWriter.autoFormatting()'''
        return bool()
    def setAutoFormatting(self):
        '''bool QXmlStreamWriter.setAutoFormatting()'''
        return bool()
    def codec(self):
        '''QTextCodec QXmlStreamWriter.codec()'''
        return QTextCodec()
    def setCodec(self, codec):
        '''void QXmlStreamWriter.setCodec(QTextCodec codec)'''
    def setCodec(self, codecName):
        '''void QXmlStreamWriter.setCodec(str codecName)'''
    def device(self):
        '''QIODevice QXmlStreamWriter.device()'''
        return QIODevice()
    def setDevice(self, device):
        '''void QXmlStreamWriter.setDevice(QIODevice device)'''


class QPyNullVariant():
    """"""
    def __init__(self, type):
        '''void QPyNullVariant.__init__(object type)'''
    def isNull(self):
        '''bool QPyNullVariant.isNull()'''
        return bool()
    def typeName(self):
        '''str QPyNullVariant.typeName()'''
        return str()
    def userType(self):
        '''int QPyNullVariant.userType()'''
        return int()
    def type(self):
        '''Type QPyNullVariant.type()'''
        return Type()


# Enum Type
Invalid = 0
Bool = 0
Int = 0
UInt = 0
LongLong = 0
ULongLong = 0
Double = 0
Char = 0
Map = 0
List = 0
String = 0
StringList = 0
ByteArray = 0
BitArray = 0
Date = 0
Time = 0
DateTime = 0
Url = 0
Locale = 0
Rect = 0
RectF = 0
Size = 0
SizeF = 0
Line = 0
LineF = 0
Point = 0
PointF = 0
RegExp = 0
Font = 0
Pixmap = 0
Brush = 0
Color = 0
Palette = 0
Icon = 0
Image = 0
Polygon = 0
Region = 0
Bitmap = 0
Cursor = 0
SizePolicy = 0
KeySequence = 0
Pen = 0
TextLength = 0
TextFormat = 0
Matrix = 0
Transform = 0
Hash = 0
Matrix4x4 = 0
Vector2D = 0
Vector3D = 0
Vector4D = 0
Quaternion = 0
EasingCurve = 0
UserType = 0


# Enum QtMsgType
QtDebugMsg = 0
QtWarningMsg = 0
QtCriticalMsg = 0
QtFatalMsg = 0
QtSystemMsg = 0


PYQT_VERSION = None # int member

PYQT_VERSION_STR = None # str member

QT_VERSION = None # int member

QT_VERSION_STR = None # str member

def qSetRealNumberPrecision(precision):
    '''static QTextStreamManipulator qSetRealNumberPrecision(int precision)'''
    return QTextStreamManipulator()

def qSetPadChar(ch):
    '''static QTextStreamManipulator qSetPadChar(QChar ch)'''
    return QTextStreamManipulator()

def qSetFieldWidth(width):
    '''static QTextStreamManipulator qSetFieldWidth(int width)'''
    return QTextStreamManipulator()

def ws(s):
    '''static QTextStream ws(QTextStream s)'''
    return QTextStream()

def bom(s):
    '''static QTextStream bom(QTextStream s)'''
    return QTextStream()

def reset(s):
    '''static QTextStream reset(QTextStream s)'''
    return QTextStream()

def flush(s):
    '''static QTextStream flush(QTextStream s)'''
    return QTextStream()

def endl(s):
    '''static QTextStream endl(QTextStream s)'''
    return QTextStream()

def center(s):
    '''static QTextStream center(QTextStream s)'''
    return QTextStream()

def right(s):
    '''static QTextStream right(QTextStream s)'''
    return QTextStream()

def left(s):
    '''static QTextStream left(QTextStream s)'''
    return QTextStream()

def scientific(s):
    '''static QTextStream scientific(QTextStream s)'''
    return QTextStream()

def fixed(s):
    '''static QTextStream fixed(QTextStream s)'''
    return QTextStream()

def lowercasedigits(s):
    '''static QTextStream lowercasedigits(QTextStream s)'''
    return QTextStream()

def lowercasebase(s):
    '''static QTextStream lowercasebase(QTextStream s)'''
    return QTextStream()

def uppercasedigits(s):
    '''static QTextStream uppercasedigits(QTextStream s)'''
    return QTextStream()

def uppercasebase(s):
    '''static QTextStream uppercasebase(QTextStream s)'''
    return QTextStream()

def noforcepoint(s):
    '''static QTextStream noforcepoint(QTextStream s)'''
    return QTextStream()

def noforcesign(s):
    '''static QTextStream noforcesign(QTextStream s)'''
    return QTextStream()

def noshowbase(s):
    '''static QTextStream noshowbase(QTextStream s)'''
    return QTextStream()

def forcepoint(s):
    '''static QTextStream forcepoint(QTextStream s)'''
    return QTextStream()

def forcesign(s):
    '''static QTextStream forcesign(QTextStream s)'''
    return QTextStream()

def showbase(s):
    '''static QTextStream showbase(QTextStream s)'''
    return QTextStream()

def hex_(s):
    '''static QTextStream hex_(QTextStream s)'''
    return QTextStream()

def hex(s):
    '''static QTextStream hex(QTextStream s)'''
    return QTextStream()

def dec(s):
    '''static QTextStream dec(QTextStream s)'''
    return QTextStream()

def oct_(s):
    '''static QTextStream oct_(QTextStream s)'''
    return QTextStream()

def oct(s):
    '''static QTextStream oct(QTextStream s)'''
    return QTextStream()

def bin_(s):
    '''static QTextStream bin_(QTextStream s)'''
    return QTextStream()

def bin(s):
    '''static QTextStream bin(QTextStream s)'''
    return QTextStream()

def Q_RETURN_ARG(type):
    '''static QGenericReturnArgument Q_RETURN_ARG(object type)'''
    return QGenericReturnArgument()

def Q_ARG(type, data):
    '''static QGenericArgument Q_ARG(object type, object data)'''
    return QGenericArgument()

def pyqtSignature(signature, result = None):
    '''static object pyqtSignature(str signature, str result = None)'''
    return object()

def pyqtSlot(signature, name = None, result = None):
    '''static object pyqtSlot(str signature, str name = None, str result = None)'''
    return object()

def SIGNAL():
    '''static str SIGNAL()'''
    return str()

def SLOT():
    '''static str SLOT()'''
    return str()

def QT_TRANSLATE_NOOP():
    '''static str QT_TRANSLATE_NOOP()'''
    return str()

def QT_TR_NOOP_UTF8():
    '''static str QT_TR_NOOP_UTF8()'''
    return str()

def QT_TR_NOOP():
    '''static str QT_TR_NOOP()'''
    return str()

def Q_FLAGS(*args):
    '''static  Q_FLAGS(... *args)'''
    return ()

def Q_ENUMS(*args):
    '''static  Q_ENUMS(... *args)'''
    return ()

def Q_CLASSINFO(name, value):
    '''static  Q_CLASSINFO(str name, str value)'''
    return ()

def qQNaN():
    '''static float qQNaN()'''
    return float()

def qSNaN():
    '''static float qSNaN()'''
    return float()

def qInf():
    '''static float qInf()'''
    return float()

def qIsNaN(d):
    '''static bool qIsNaN(float d)'''
    return bool()

def qIsFinite(d):
    '''static bool qIsFinite(float d)'''
    return bool()

def qIsInf(d):
    '''static bool qIsInf(float d)'''
    return bool()

def pyqtRestoreInputHook():
    '''static void pyqtRestoreInputHook()'''


def pyqtRemoveInputHook():
    '''static void pyqtRemoveInputHook()'''


def qRemovePostRoutine():
    '''static callable qRemovePostRoutine()'''
    return callable()

def qAddPostRoutine():
    '''static callable qAddPostRoutine()'''
    return callable()

def qUncompress(data):
    '''static QByteArray qUncompress(QByteArray data)'''
    return QByteArray()

def qCompress(data, compressionLevel = -1):
    '''static QByteArray qCompress(QByteArray data, int compressionLevel = -1)'''
    return QByteArray()

def qChecksum(s):
    '''static int qChecksum(str s)'''
    return int()

def qSwap(value1, value2):
    '''static void qSwap(QBitArray value1, QBitArray value2)'''


def qSwap(value1, value2):
    '''static void qSwap(QByteArray value1, QByteArray value2)'''


def qSwap(value1, value2):
    '''static void qSwap(QString value1, QString value2)'''


def qSwap(value1, value2):
    '''static void qSwap(QUrl value1, QUrl value2)'''


def qSwap(value1, value2):
    '''static void qSwap(QVariant value1, QVariant value2)'''


def qrand():
    '''static int qrand()'''
    return int()

def qsrand(seed):
    '''static void qsrand(int seed)'''


def qIsNull(d):
    '''static bool qIsNull(float d)'''
    return bool()

def qFuzzyCompare(p1, p2):
    '''static bool qFuzzyCompare(float p1, float p2)'''
    return bool()

def qUnregisterResourceData():
    '''static str qUnregisterResourceData()'''
    return str()

def qRegisterResourceData():
    '''static str qRegisterResourceData()'''
    return str()

def qInstallMsgHandler():
    '''static callable qInstallMsgHandler()'''
    return callable()

def qErrnoWarning(code, msg):
    '''static void qErrnoWarning(int code, str msg)'''


def qErrnoWarning(msg):
    '''static void qErrnoWarning(str msg)'''


def qFatal():
    '''static str qFatal()'''
    return str()

def qCritical():
    '''static str qCritical()'''
    return str()

def qWarning():
    '''static str qWarning()'''
    return str()

def qDebug():
    '''static str qDebug()'''
    return str()

def qSharedBuild():
    '''static bool qSharedBuild()'''
    return bool()

def qVersion():
    '''static str qVersion()'''
    return str()

def qRound64(d):
    '''static int qRound64(float d)'''
    return int()

def qRound(d):
    '''static int qRound(float d)'''
    return int()

def qAbs(t):
    '''static float qAbs(float t)'''
    return float()

