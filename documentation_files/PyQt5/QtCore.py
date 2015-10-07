class pyqtSignal():
 def connect(self, targetSignal): pass
 def emit(self, *args): pass
from QtCore import *

from QtWidgets import *

import datetime

class Qt():
    """"""
    # Enum Qt.ItemSelectionOperation
    ReplaceSelection = 0
    AddToSelection = 0

    # Enum Qt.TabFocusBehavior
    NoTabFocus = 0
    TabFocusTextControls = 0
    TabFocusListControls = 0
    TabFocusAllControls = 0

    # Enum Qt.MouseEventFlag
    MouseEventCreatedDoubleClick = 0

    # Enum Qt.MouseEventSource
    MouseEventNotSynthesized = 0
    MouseEventSynthesizedBySystem = 0
    MouseEventSynthesizedByQt = 0

    # Enum Qt.ScrollPhase
    ScrollBegin = 0
    ScrollUpdate = 0
    ScrollEnd = 0

    # Enum Qt.NativeGestureType
    BeginNativeGesture = 0
    EndNativeGesture = 0
    PanNativeGesture = 0
    ZoomNativeGesture = 0
    SmartZoomNativeGesture = 0
    RotateNativeGesture = 0
    SwipeNativeGesture = 0

    # Enum Qt.Edge
    TopEdge = 0
    LeftEdge = 0
    RightEdge = 0
    BottomEdge = 0

    # Enum Qt.ApplicationState
    ApplicationSuspended = 0
    ApplicationHidden = 0
    ApplicationInactive = 0
    ApplicationActive = 0

    # Enum Qt.HitTestAccuracy
    ExactHit = 0
    FuzzyHit = 0

    # Enum Qt.WhiteSpaceMode
    WhiteSpaceNormal = 0
    WhiteSpacePre = 0
    WhiteSpaceNoWrap = 0
    WhiteSpaceModeUndefined = 0

    # Enum Qt.FindChildOption
    FindDirectChildrenOnly = 0
    FindChildrenRecursively = 0

    # Enum Qt.ScreenOrientation
    PrimaryOrientation = 0
    PortraitOrientation = 0
    LandscapeOrientation = 0
    InvertedPortraitOrientation = 0
    InvertedLandscapeOrientation = 0

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
    ImhSensitiveData = 0
    ImhDate = 0
    ImhTime = 0
    ImhPreferLatin = 0
    ImhLatinOnly = 0
    ImhMultiLine = 0

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
    AA_X11InitThreads = 0
    AA_Use96Dpi = 0
    AA_SynthesizeTouchForUnhandledMouseEvents = 0
    AA_SynthesizeMouseForUnhandledTouchEvents = 0
    AA_UseHighDpiPixmaps = 0
    AA_ForceRasterWidgets = 0
    AA_UseDesktopOpenGL = 0
    AA_UseOpenGLES = 0
    AA_UseSoftwareOpenGL = 0
    AA_ShareOpenGLContexts = 0
    AA_SetPalette = 0

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
    ItemNeverHasChildren = 0
    ItemIsUserTristate = 0

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
    ImEnabled = 0
    ImCursorRectangle = 0
    ImHints = 0
    ImPreferredLanguage = 0
    ImPlatformData = 0
    ImQueryInput = 0
    ImQueryAll = 0
    ImAbsolutePosition = 0
    ImTextBeforeCursor = 0
    ImTextAfterCursor = 0

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
    TimeZone = 0

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
    RFC2822Date = 0

    # Enum Qt.ToolBarArea
    LeftToolBarArea = 0
    RightToolBarArea = 0
    TopToolBarArea = 0
    BottomToolBarArea = 0
    ToolBarArea_Mask = 0
    AllToolBarAreas = 0
    NoToolBarArea = 0

    # Enum Qt.TimerType
    PreciseTimer = 0
    CoarseTimer = 0
    VeryCoarseTimer = 0

    # Enum Qt.DockWidgetArea
    LeftDockWidgetArea = 0
    RightDockWidgetArea = 0
    TopDockWidgetArea = 0
    BottomDockWidgetArea = 0
    DockWidgetArea_Mask = 0
    AllDockWidgetAreas = 0
    NoDockWidgetArea = 0

    # Enum Qt.AspectRatioMode
    IgnoreAspectRatio = 0
    KeepAspectRatio = 0
    KeepAspectRatioByExpanding = 0

    # Enum Qt.TextFormat
    PlainText = 0
    RichText = 0
    AutoText = 0

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
    Key_TouchpadToggle = 0
    Key_TouchpadOn = 0
    Key_TouchpadOff = 0
    Key_MicMute = 0
    Key_Red = 0
    Key_Green = 0
    Key_Yellow = 0
    Key_Blue = 0
    Key_ChannelUp = 0
    Key_ChannelDown = 0
    Key_Guide = 0
    Key_Info = 0
    Key_Settings = 0
    Key_Exit = 0
    Key_MicVolumeUp = 0
    Key_MicVolumeDown = 0
    Key_New = 0
    Key_Open = 0
    Key_Find = 0
    Key_Undo = 0
    Key_Redo = 0

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
    NoOpaqueDetection = 0
    NoFormatConversion = 0

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
    WA_X11DoNotAcceptFocus = 0
    WA_MacNoShadow = 0
    WA_AlwaysStackOnTop = 0

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
    WindowTransparentForInput = 0
    WindowOverridesSystemGestures = 0
    WindowDoesNotAcceptFocus = 0
    NoDropShadowWindowHint = 0
    WindowFullscreenButtonHint = 0
    ForeignWindow = 0
    BypassWindowManagerHint = 0
    CoverWindow = 0
    MaximizeUsingFullscreenGeometryHint = 0

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
    AlignBaseline = 0

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
    AllButtons = 0
    LeftButton = 0
    RightButton = 0
    MidButton = 0
    MiddleButton = 0
    XButton1 = 0
    XButton2 = 0
    BackButton = 0
    ExtraButton1 = 0
    ForwardButton = 0
    ExtraButton2 = 0
    TaskButton = 0
    ExtraButton3 = 0
    ExtraButton4 = 0
    ExtraButton5 = 0
    ExtraButton6 = 0
    ExtraButton7 = 0
    ExtraButton8 = 0
    ExtraButton9 = 0
    ExtraButton10 = 0
    ExtraButton11 = 0
    ExtraButton12 = 0
    ExtraButton13 = 0
    ExtraButton14 = 0
    ExtraButton15 = 0
    ExtraButton16 = 0
    ExtraButton17 = 0
    ExtraButton18 = 0
    ExtraButton19 = 0
    ExtraButton20 = 0
    ExtraButton21 = 0
    ExtraButton22 = 0
    ExtraButton23 = 0
    ExtraButton24 = 0

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
    class FindChildOptions():
        """"""
        def __init__(self):
            '''Qt.FindChildOptions Qt.FindChildOptions.__init__()'''
            return Qt.FindChildOptions()
        def __init__(self):
            '''int Qt.FindChildOptions.__init__()'''
            return int()
        def __init__(self):
            '''void Qt.FindChildOptions.__init__()'''
        def __bool__(self):
            '''int Qt.FindChildOptions.__bool__()'''
            return int()
        def __ne__(self, f):
            '''bool Qt.FindChildOptions.__ne__(Qt.FindChildOptions f)'''
            return bool()
        def __eq__(self, f):
            '''bool Qt.FindChildOptions.__eq__(Qt.FindChildOptions f)'''
            return bool()
        def __invert__(self):
            '''Qt.FindChildOptions Qt.FindChildOptions.__invert__()'''
            return Qt.FindChildOptions()
        def __and__(self, mask):
            '''Qt.FindChildOptions Qt.FindChildOptions.__and__(int mask)'''
            return Qt.FindChildOptions()
        def __xor__(self, f):
            '''Qt.FindChildOptions Qt.FindChildOptions.__xor__(Qt.FindChildOptions f)'''
            return Qt.FindChildOptions()
        def __xor__(self, f):
            '''Qt.FindChildOptions Qt.FindChildOptions.__xor__(int f)'''
            return Qt.FindChildOptions()
        def __or__(self, f):
            '''Qt.FindChildOptions Qt.FindChildOptions.__or__(Qt.FindChildOptions f)'''
            return Qt.FindChildOptions()
        def __or__(self, f):
            '''Qt.FindChildOptions Qt.FindChildOptions.__or__(int f)'''
            return Qt.FindChildOptions()
        def __int__(self):
            '''int Qt.FindChildOptions.__int__()'''
            return int()
        def __ixor__(self, f):
            '''Qt.FindChildOptions Qt.FindChildOptions.__ixor__(Qt.FindChildOptions f)'''
            return Qt.FindChildOptions()
        def __ior__(self, f):
            '''Qt.FindChildOptions Qt.FindChildOptions.__ior__(Qt.FindChildOptions f)'''
            return Qt.FindChildOptions()
        def __iand__(self, mask):
            '''Qt.FindChildOptions Qt.FindChildOptions.__iand__(int mask)'''
            return Qt.FindChildOptions()
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
    class MouseEventFlags():
        """"""
        def __init__(self):
            '''Qt.MouseEventFlags Qt.MouseEventFlags.__init__()'''
            return Qt.MouseEventFlags()
        def __init__(self):
            '''int Qt.MouseEventFlags.__init__()'''
            return int()
        def __init__(self):
            '''void Qt.MouseEventFlags.__init__()'''
        def __bool__(self):
            '''int Qt.MouseEventFlags.__bool__()'''
            return int()
        def __ne__(self, f):
            '''bool Qt.MouseEventFlags.__ne__(Qt.MouseEventFlags f)'''
            return bool()
        def __eq__(self, f):
            '''bool Qt.MouseEventFlags.__eq__(Qt.MouseEventFlags f)'''
            return bool()
        def __invert__(self):
            '''Qt.MouseEventFlags Qt.MouseEventFlags.__invert__()'''
            return Qt.MouseEventFlags()
        def __and__(self, mask):
            '''Qt.MouseEventFlags Qt.MouseEventFlags.__and__(int mask)'''
            return Qt.MouseEventFlags()
        def __xor__(self, f):
            '''Qt.MouseEventFlags Qt.MouseEventFlags.__xor__(Qt.MouseEventFlags f)'''
            return Qt.MouseEventFlags()
        def __xor__(self, f):
            '''Qt.MouseEventFlags Qt.MouseEventFlags.__xor__(int f)'''
            return Qt.MouseEventFlags()
        def __or__(self, f):
            '''Qt.MouseEventFlags Qt.MouseEventFlags.__or__(Qt.MouseEventFlags f)'''
            return Qt.MouseEventFlags()
        def __or__(self, f):
            '''Qt.MouseEventFlags Qt.MouseEventFlags.__or__(int f)'''
            return Qt.MouseEventFlags()
        def __int__(self):
            '''int Qt.MouseEventFlags.__int__()'''
            return int()
        def __ixor__(self, f):
            '''Qt.MouseEventFlags Qt.MouseEventFlags.__ixor__(Qt.MouseEventFlags f)'''
            return Qt.MouseEventFlags()
        def __ior__(self, f):
            '''Qt.MouseEventFlags Qt.MouseEventFlags.__ior__(Qt.MouseEventFlags f)'''
            return Qt.MouseEventFlags()
        def __iand__(self, mask):
            '''Qt.MouseEventFlags Qt.MouseEventFlags.__iand__(int mask)'''
            return Qt.MouseEventFlags()
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
    class ApplicationStates():
        """"""
        def __init__(self):
            '''Qt.ApplicationStates Qt.ApplicationStates.__init__()'''
            return Qt.ApplicationStates()
        def __init__(self):
            '''int Qt.ApplicationStates.__init__()'''
            return int()
        def __init__(self):
            '''void Qt.ApplicationStates.__init__()'''
        def __bool__(self):
            '''int Qt.ApplicationStates.__bool__()'''
            return int()
        def __ne__(self, f):
            '''bool Qt.ApplicationStates.__ne__(Qt.ApplicationStates f)'''
            return bool()
        def __eq__(self, f):
            '''bool Qt.ApplicationStates.__eq__(Qt.ApplicationStates f)'''
            return bool()
        def __invert__(self):
            '''Qt.ApplicationStates Qt.ApplicationStates.__invert__()'''
            return Qt.ApplicationStates()
        def __and__(self, mask):
            '''Qt.ApplicationStates Qt.ApplicationStates.__and__(int mask)'''
            return Qt.ApplicationStates()
        def __xor__(self, f):
            '''Qt.ApplicationStates Qt.ApplicationStates.__xor__(Qt.ApplicationStates f)'''
            return Qt.ApplicationStates()
        def __xor__(self, f):
            '''Qt.ApplicationStates Qt.ApplicationStates.__xor__(int f)'''
            return Qt.ApplicationStates()
        def __or__(self, f):
            '''Qt.ApplicationStates Qt.ApplicationStates.__or__(Qt.ApplicationStates f)'''
            return Qt.ApplicationStates()
        def __or__(self, f):
            '''Qt.ApplicationStates Qt.ApplicationStates.__or__(int f)'''
            return Qt.ApplicationStates()
        def __int__(self):
            '''int Qt.ApplicationStates.__int__()'''
            return int()
        def __ixor__(self, f):
            '''Qt.ApplicationStates Qt.ApplicationStates.__ixor__(Qt.ApplicationStates f)'''
            return Qt.ApplicationStates()
        def __ior__(self, f):
            '''Qt.ApplicationStates Qt.ApplicationStates.__ior__(Qt.ApplicationStates f)'''
            return Qt.ApplicationStates()
        def __iand__(self, mask):
            '''Qt.ApplicationStates Qt.ApplicationStates.__iand__(int mask)'''
            return Qt.ApplicationStates()
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
    class ScreenOrientations():
        """"""
        def __init__(self):
            '''Qt.ScreenOrientations Qt.ScreenOrientations.__init__()'''
            return Qt.ScreenOrientations()
        def __init__(self):
            '''int Qt.ScreenOrientations.__init__()'''
            return int()
        def __init__(self):
            '''void Qt.ScreenOrientations.__init__()'''
        def __bool__(self):
            '''int Qt.ScreenOrientations.__bool__()'''
            return int()
        def __ne__(self, f):
            '''bool Qt.ScreenOrientations.__ne__(Qt.ScreenOrientations f)'''
            return bool()
        def __eq__(self, f):
            '''bool Qt.ScreenOrientations.__eq__(Qt.ScreenOrientations f)'''
            return bool()
        def __invert__(self):
            '''Qt.ScreenOrientations Qt.ScreenOrientations.__invert__()'''
            return Qt.ScreenOrientations()
        def __and__(self, mask):
            '''Qt.ScreenOrientations Qt.ScreenOrientations.__and__(int mask)'''
            return Qt.ScreenOrientations()
        def __xor__(self, f):
            '''Qt.ScreenOrientations Qt.ScreenOrientations.__xor__(Qt.ScreenOrientations f)'''
            return Qt.ScreenOrientations()
        def __xor__(self, f):
            '''Qt.ScreenOrientations Qt.ScreenOrientations.__xor__(int f)'''
            return Qt.ScreenOrientations()
        def __or__(self, f):
            '''Qt.ScreenOrientations Qt.ScreenOrientations.__or__(Qt.ScreenOrientations f)'''
            return Qt.ScreenOrientations()
        def __or__(self, f):
            '''Qt.ScreenOrientations Qt.ScreenOrientations.__or__(int f)'''
            return Qt.ScreenOrientations()
        def __int__(self):
            '''int Qt.ScreenOrientations.__int__()'''
            return int()
        def __ixor__(self, f):
            '''Qt.ScreenOrientations Qt.ScreenOrientations.__ixor__(Qt.ScreenOrientations f)'''
            return Qt.ScreenOrientations()
        def __ior__(self, f):
            '''Qt.ScreenOrientations Qt.ScreenOrientations.__ior__(Qt.ScreenOrientations f)'''
            return Qt.ScreenOrientations()
        def __iand__(self, mask):
            '''Qt.ScreenOrientations Qt.ScreenOrientations.__iand__(int mask)'''
            return Qt.ScreenOrientations()
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
    class Edges():
        """"""
        def __init__(self):
            '''Qt.Edges Qt.Edges.__init__()'''
            return Qt.Edges()
        def __init__(self):
            '''int Qt.Edges.__init__()'''
            return int()
        def __init__(self):
            '''void Qt.Edges.__init__()'''
        def __bool__(self):
            '''int Qt.Edges.__bool__()'''
            return int()
        def __ne__(self, f):
            '''bool Qt.Edges.__ne__(Qt.Edges f)'''
            return bool()
        def __eq__(self, f):
            '''bool Qt.Edges.__eq__(Qt.Edges f)'''
            return bool()
        def __invert__(self):
            '''Qt.Edges Qt.Edges.__invert__()'''
            return Qt.Edges()
        def __and__(self, mask):
            '''Qt.Edges Qt.Edges.__and__(int mask)'''
            return Qt.Edges()
        def __xor__(self, f):
            '''Qt.Edges Qt.Edges.__xor__(Qt.Edges f)'''
            return Qt.Edges()
        def __xor__(self, f):
            '''Qt.Edges Qt.Edges.__xor__(int f)'''
            return Qt.Edges()
        def __or__(self, f):
            '''Qt.Edges Qt.Edges.__or__(Qt.Edges f)'''
            return Qt.Edges()
        def __or__(self, f):
            '''Qt.Edges Qt.Edges.__or__(int f)'''
            return Qt.Edges()
        def __int__(self):
            '''int Qt.Edges.__int__()'''
            return int()
        def __ixor__(self, f):
            '''Qt.Edges Qt.Edges.__ixor__(Qt.Edges f)'''
            return Qt.Edges()
        def __ior__(self, f):
            '''Qt.Edges Qt.Edges.__ior__(Qt.Edges f)'''
            return Qt.Edges()
        def __iand__(self, mask):
            '''Qt.Edges Qt.Edges.__iand__(int mask)'''
            return Qt.Edges()
    class InputMethodQueries():
        """"""
        def __init__(self):
            '''Qt.InputMethodQueries Qt.InputMethodQueries.__init__()'''
            return Qt.InputMethodQueries()
        def __init__(self):
            '''int Qt.InputMethodQueries.__init__()'''
            return int()
        def __init__(self):
            '''void Qt.InputMethodQueries.__init__()'''
        def __bool__(self):
            '''int Qt.InputMethodQueries.__bool__()'''
            return int()
        def __ne__(self, f):
            '''bool Qt.InputMethodQueries.__ne__(Qt.InputMethodQueries f)'''
            return bool()
        def __eq__(self, f):
            '''bool Qt.InputMethodQueries.__eq__(Qt.InputMethodQueries f)'''
            return bool()
        def __invert__(self):
            '''Qt.InputMethodQueries Qt.InputMethodQueries.__invert__()'''
            return Qt.InputMethodQueries()
        def __and__(self, mask):
            '''Qt.InputMethodQueries Qt.InputMethodQueries.__and__(int mask)'''
            return Qt.InputMethodQueries()
        def __xor__(self, f):
            '''Qt.InputMethodQueries Qt.InputMethodQueries.__xor__(Qt.InputMethodQueries f)'''
            return Qt.InputMethodQueries()
        def __xor__(self, f):
            '''Qt.InputMethodQueries Qt.InputMethodQueries.__xor__(int f)'''
            return Qt.InputMethodQueries()
        def __or__(self, f):
            '''Qt.InputMethodQueries Qt.InputMethodQueries.__or__(Qt.InputMethodQueries f)'''
            return Qt.InputMethodQueries()
        def __or__(self, f):
            '''Qt.InputMethodQueries Qt.InputMethodQueries.__or__(int f)'''
            return Qt.InputMethodQueries()
        def __int__(self):
            '''int Qt.InputMethodQueries.__int__()'''
            return int()
        def __ixor__(self, f):
            '''Qt.InputMethodQueries Qt.InputMethodQueries.__ixor__(Qt.InputMethodQueries f)'''
            return Qt.InputMethodQueries()
        def __ior__(self, f):
            '''Qt.InputMethodQueries Qt.InputMethodQueries.__ior__(Qt.InputMethodQueries f)'''
            return Qt.InputMethodQueries()
        def __iand__(self, mask):
            '''Qt.InputMethodQueries Qt.InputMethodQueries.__iand__(int mask)'''
            return Qt.InputMethodQueries()
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
    def disconnect(self):
        ''' QObject.disconnect()'''
        return ()
    def isSignalConnected(self, signal):
        '''bool QObject.isSignalConnected(QMetaMethod signal)'''
        return bool()
    def senderSignalIndex(self):
        '''int QObject.senderSignalIndex()'''
        return int()
    def disconnectNotify(self, signal):
        '''void QObject.disconnectNotify(QMetaMethod signal)'''
    def connectNotify(self, signal):
        '''void QObject.connectNotify(QMetaMethod signal)'''
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
        '''int QObject.receivers(signal signal)'''
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
    objectNameChanged = pyqtSignal() # void objectNameChanged(const QStringamp;) - signal
    destroyed = pyqtSignal() # void destroyed(QObject* = 0) - signal
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
    def startTimer(self, interval, timerType = None):
        '''int QObject.startTimer(int interval, Qt.TimerType timerType = Qt.CoarseTimer)'''
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
    def isWindowType(self):
        '''bool QObject.isWindowType()'''
        return bool()
    def isWidgetType(self):
        '''bool QObject.isWidgetType()'''
        return bool()
    def setObjectName(self, name):
        '''void QObject.setObjectName(str name)'''
    def objectName(self):
        '''str QObject.objectName()'''
        return str()
    def findChildren(self, type, name = None, options = None):
        '''list-of-QObject QObject.findChildren(type type, str name = '', Qt.FindChildOptions options = Qt.FindChildrenRecursively)'''
        return [QObject()]
    def findChildren(self, types, name = None, options = None):
        '''list-of-QObject QObject.findChildren(tuple types, str name = '', Qt.FindChildOptions options = Qt.FindChildrenRecursively)'''
        return [QObject()]
    def findChildren(self, type, regExp, options = None):
        '''list-of-QObject QObject.findChildren(type type, QRegExp regExp, Qt.FindChildOptions options = Qt.FindChildrenRecursively)'''
        return [QObject()]
    def findChildren(self, types, regExp, options = None):
        '''list-of-QObject QObject.findChildren(tuple types, QRegExp regExp, Qt.FindChildOptions options = Qt.FindChildrenRecursively)'''
        return [QObject()]
    def findChildren(self, type, re, options = None):
        '''list-of-QObject QObject.findChildren(type type, QRegularExpression re, Qt.FindChildOptions options = Qt.FindChildrenRecursively)'''
        return [QObject()]
    def findChildren(self, types, re, options = None):
        '''list-of-QObject QObject.findChildren(tuple types, QRegularExpression re, Qt.FindChildOptions options = Qt.FindChildrenRecursively)'''
        return [QObject()]
    def findChild(self, type, name = None, options = None):
        '''QObject QObject.findChild(type type, str name = '', Qt.FindChildOptions options = Qt.FindChildrenRecursively)'''
        return QObject()
    def findChild(self, types, name = None, options = None):
        '''QObject QObject.findChild(tuple types, str name = '', Qt.FindChildOptions options = Qt.FindChildrenRecursively)'''
        return QObject()
    def tr(self, sourceText, disambiguation = None, n = None):
        '''str QObject.tr(str sourceText, str disambiguation = None, int n = -1)'''
        return str()
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
    def start(self, policy = None):
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
    def filterNativeEvent(self, eventType, message, result):
        '''bool QAbstractEventDispatcher.filterNativeEvent(QByteArray eventType, sip.voidptr message, int result)'''
        return bool()
    def removeNativeEventFilter(self, filterObj):
        '''void QAbstractEventDispatcher.removeNativeEventFilter(QAbstractNativeEventFilter filterObj)'''
    def installNativeEventFilter(self, filterObj):
        '''void QAbstractEventDispatcher.installNativeEventFilter(QAbstractNativeEventFilter filterObj)'''
    def remainingTime(self, timerId):
        '''abstract int QAbstractEventDispatcher.remainingTime(int timerId)'''
        return int()
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
        '''abstract list-of-QAbstractEventDispatcher.TimerInfo QAbstractEventDispatcher.registeredTimers(QObject object)'''
        return [QAbstractEventDispatcher.TimerInfo()]
    def unregisterTimers(self, object):
        '''abstract bool QAbstractEventDispatcher.unregisterTimers(QObject object)'''
        return bool()
    def unregisterTimer(self, timerId):
        '''abstract bool QAbstractEventDispatcher.unregisterTimer(int timerId)'''
        return bool()
    def registerTimer(self, interval, timerType, object):
        '''int QAbstractEventDispatcher.registerTimer(int interval, Qt.TimerType timerType, QObject object)'''
        return int()
    def registerTimer(self, timerId, interval, timerType, object):
        '''abstract void QAbstractEventDispatcher.registerTimer(int timerId, int interval, Qt.TimerType timerType, QObject object)'''
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
    class TimerInfo():
        """"""
        interval = None # int - member
        timerId = None # int - member
        timerType = None # Qt.TimerType - member
        def __init__(self, id, i, t):
            '''void QAbstractEventDispatcher.TimerInfo.__init__(int id, int i, Qt.TimerType t)'''
        def __init__(self):
            '''QAbstractEventDispatcher.TimerInfo QAbstractEventDispatcher.TimerInfo.__init__()'''
            return QAbstractEventDispatcher.TimerInfo()


class QModelIndex():
    """"""
    def __init__(self):
        '''void QModelIndex.__init__()'''
    def __init__(self):
        '''QModelIndex QModelIndex.__init__()'''
        return QModelIndex()
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
    def data(self, role = None):
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
    def swap(self, other):
        '''void QPersistentModelIndex.swap(QPersistentModelIndex other)'''
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
    def data(self, role = None):
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
    # Enum QAbstractItemModel.LayoutChangeHint
    NoLayoutChangeHint = 0
    VerticalSortHint = 0
    HorizontalSortHint = 0

    def __init__(self, parent = None):
        '''void QAbstractItemModel.__init__(QObject parent = None)'''
    def moveColumn(self, sourceParent, sourceColumn, destinationParent, destinationChild):
        '''bool QAbstractItemModel.moveColumn(QModelIndex sourceParent, int sourceColumn, QModelIndex destinationParent, int destinationChild)'''
        return bool()
    def moveRow(self, sourceParent, sourceRow, destinationParent, destinationChild):
        '''bool QAbstractItemModel.moveRow(QModelIndex sourceParent, int sourceRow, QModelIndex destinationParent, int destinationChild)'''
        return bool()
    def moveColumns(self, sourceParent, sourceColumn, count, destinationParent, destinationChild):
        '''bool QAbstractItemModel.moveColumns(QModelIndex sourceParent, int sourceColumn, int count, QModelIndex destinationParent, int destinationChild)'''
        return bool()
    def moveRows(self, sourceParent, sourceRow, count, destinationParent, destinationChild):
        '''bool QAbstractItemModel.moveRows(QModelIndex sourceParent, int sourceRow, int count, QModelIndex destinationParent, int destinationChild)'''
        return bool()
    def canDropMimeData(self, data, action, row, column, parent):
        '''bool QAbstractItemModel.canDropMimeData(QMimeData data, Qt.DropAction action, int row, int column, QModelIndex parent)'''
        return bool()
    def resetInternalData(self):
        '''void QAbstractItemModel.resetInternalData()'''
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
    columnsMoved = pyqtSignal() # void columnsMoved(const QModelIndexamp;,int,int,const QModelIndexamp;,int) - signal
    columnsAboutToBeMoved = pyqtSignal() # void columnsAboutToBeMoved(const QModelIndexamp;,int,int,const QModelIndexamp;,int) - signal
    rowsMoved = pyqtSignal() # void rowsMoved(const QModelIndexamp;,int,int,const QModelIndexamp;,int) - signal
    rowsAboutToBeMoved = pyqtSignal() # void rowsAboutToBeMoved(const QModelIndexamp;,int,int,const QModelIndexamp;,int) - signal
    def createIndex(self, row, column, object = 0):
        '''QModelIndex QAbstractItemModel.createIndex(int row, int column, object object = 0)'''
        return QModelIndex()
    def roleNames(self):
        '''dict-of-int-QByteArray QAbstractItemModel.roleNames()'''
        return {int():QByteArray()}
    def supportedDragActions(self):
        '''Qt.DropActions QAbstractItemModel.supportedDragActions()'''
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
    def revert(self):
        '''void QAbstractItemModel.revert()'''
    def submit(self):
        '''bool QAbstractItemModel.submit()'''
        return bool()
    modelReset = pyqtSignal() # void modelReset() - signal
    modelAboutToBeReset = pyqtSignal() # void modelAboutToBeReset() - signal
    columnsRemoved = pyqtSignal() # void columnsRemoved(const QModelIndexamp;,int,int) - signal
    columnsAboutToBeRemoved = pyqtSignal() # void columnsAboutToBeRemoved(const QModelIndexamp;,int,int) - signal
    columnsInserted = pyqtSignal() # void columnsInserted(const QModelIndexamp;,int,int) - signal
    columnsAboutToBeInserted = pyqtSignal() # void columnsAboutToBeInserted(const QModelIndexamp;,int,int) - signal
    rowsRemoved = pyqtSignal() # void rowsRemoved(const QModelIndexamp;,int,int) - signal
    rowsAboutToBeRemoved = pyqtSignal() # void rowsAboutToBeRemoved(const QModelIndexamp;,int,int) - signal
    rowsInserted = pyqtSignal() # void rowsInserted(const QModelIndexamp;,int,int) - signal
    rowsAboutToBeInserted = pyqtSignal() # void rowsAboutToBeInserted(const QModelIndexamp;,int,int) - signal
    layoutChanged = pyqtSignal() # void layoutChanged(const QListlt;QPersistentModelIndexgt;amp; = QListlt;QPersistentModelIndexgt;(),QAbstractItemModel::LayoutChangeHint = QAbstractItemModel.NoLayoutChangeHint) - signal
    layoutAboutToBeChanged = pyqtSignal() # void layoutAboutToBeChanged(const QListlt;QPersistentModelIndexgt;amp; = QListlt;QPersistentModelIndexgt;(),QAbstractItemModel::LayoutChangeHint = QAbstractItemModel.NoLayoutChangeHint) - signal
    headerDataChanged = pyqtSignal() # void headerDataChanged(Qt::Orientation,int,int) - signal
    dataChanged = pyqtSignal() # void dataChanged(const QModelIndexamp;,const QModelIndexamp;,const QVectorlt;intgt;amp; = QVectorlt;intgt;()) - signal
    def span(self, index):
        '''QSize QAbstractItemModel.span(QModelIndex index)'''
        return QSize()
    def match(self, start, role, value, hits = 1, flags = None):
        '''list-of-QModelIndex QAbstractItemModel.match(QModelIndex start, int role, QVariant value, int hits = 1, Qt.MatchFlags flags = Qt.MatchStartsWith|Qt.MatchWrap)'''
        return [QModelIndex()]
    def buddy(self, index):
        '''QModelIndex QAbstractItemModel.buddy(QModelIndex index)'''
        return QModelIndex()
    def sort(self, column, order = None):
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
        '''list-of-str QAbstractItemModel.mimeTypes()'''
        return [str()]
    def setItemData(self, index, roles):
        '''bool QAbstractItemModel.setItemData(QModelIndex index, dict-of-int-object roles)'''
        return bool()
    def itemData(self, index):
        '''dict-of-int-object QAbstractItemModel.itemData(QModelIndex index)'''
        return {int():object()}
    def setHeaderData(self, section, orientation, value, role = None):
        '''bool QAbstractItemModel.setHeaderData(int section, Qt.Orientation orientation, QVariant value, int role = Qt.EditRole)'''
        return bool()
    def headerData(self, section, orientation, role = None):
        '''QVariant QAbstractItemModel.headerData(int section, Qt.Orientation orientation, int role = Qt.DisplayRole)'''
        return QVariant()
    def setData(self, index, value, role = None):
        '''bool QAbstractItemModel.setData(QModelIndex index, QVariant value, int role = Qt.EditRole)'''
        return bool()
    def data(self, index, role = None):
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
    def sibling(self, row, column, idx):
        '''QModelIndex QAbstractTableModel.sibling(int row, int column, QModelIndex idx)'''
        return QModelIndex()
    def parent(self):
        '''QObject QAbstractTableModel.parent()'''
        return QObject()
    def flags(self, index):
        '''Qt.ItemFlags QAbstractTableModel.flags(QModelIndex index)'''
        return Qt.ItemFlags()
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
    def sibling(self, row, column, idx):
        '''QModelIndex QAbstractListModel.sibling(int row, int column, QModelIndex idx)'''
        return QModelIndex()
    def parent(self):
        '''QObject QAbstractListModel.parent()'''
        return QObject()
    def flags(self, index):
        '''Qt.ItemFlags QAbstractListModel.flags(QModelIndex index)'''
        return Qt.ItemFlags()
    def dropMimeData(self, data, action, row, column, parent):
        '''bool QAbstractListModel.dropMimeData(QMimeData data, Qt.DropAction action, int row, int column, QModelIndex parent)'''
        return bool()
    def index(self, row, column = 0, parent = QModelIndex()):
        '''QModelIndex QAbstractListModel.index(int row, int column = 0, QModelIndex parent = QModelIndex())'''
        return QModelIndex()


class QAbstractNativeEventFilter():
    """"""
    def __init__(self):
        '''void QAbstractNativeEventFilter.__init__()'''
    def nativeEventFilter(self, eventType, message, result):
        '''abstract bool QAbstractNativeEventFilter.nativeEventFilter(QByteArray eventType, sip.voidptr message, int result)'''
        return bool()


class QAbstractProxyModel(QAbstractItemModel):
    """"""
    def __init__(self, parent = None):
        '''void QAbstractProxyModel.__init__(QObject parent = None)'''
    def supportedDragActions(self):
        '''Qt.DropActions QAbstractProxyModel.supportedDragActions()'''
        return Qt.DropActions()
    def dropMimeData(self, data, action, row, column, parent):
        '''bool QAbstractProxyModel.dropMimeData(QMimeData data, Qt.DropAction action, int row, int column, QModelIndex parent)'''
        return bool()
    def canDropMimeData(self, data, action, row, column, parent):
        '''bool QAbstractProxyModel.canDropMimeData(QMimeData data, Qt.DropAction action, int row, int column, QModelIndex parent)'''
        return bool()
    sourceModelChanged = pyqtSignal() # void sourceModelChanged() - signal
    def resetInternalData(self):
        '''void QAbstractProxyModel.resetInternalData()'''
    def sibling(self, row, column, idx):
        '''QModelIndex QAbstractProxyModel.sibling(int row, int column, QModelIndex idx)'''
        return QModelIndex()
    def supportedDropActions(self):
        '''Qt.DropActions QAbstractProxyModel.supportedDropActions()'''
        return Qt.DropActions()
    def mimeTypes(self):
        '''list-of-str QAbstractProxyModel.mimeTypes()'''
        return [str()]
    def mimeData(self, indexes):
        '''QMimeData QAbstractProxyModel.mimeData(list-of-QModelIndex indexes)'''
        return QMimeData()
    def hasChildren(self, parent = QModelIndex()):
        '''bool QAbstractProxyModel.hasChildren(QModelIndex parent = QModelIndex())'''
        return bool()
    def span(self, index):
        '''QSize QAbstractProxyModel.span(QModelIndex index)'''
        return QSize()
    def sort(self, column, order = None):
        '''void QAbstractProxyModel.sort(int column, Qt.SortOrder order = Qt.AscendingOrder)'''
    def fetchMore(self, parent):
        '''void QAbstractProxyModel.fetchMore(QModelIndex parent)'''
    def canFetchMore(self, parent):
        '''bool QAbstractProxyModel.canFetchMore(QModelIndex parent)'''
        return bool()
    def buddy(self, index):
        '''QModelIndex QAbstractProxyModel.buddy(QModelIndex index)'''
        return QModelIndex()
    def setItemData(self, index, roles):
        '''bool QAbstractProxyModel.setItemData(QModelIndex index, dict-of-int-object roles)'''
        return bool()
    def flags(self, index):
        '''Qt.ItemFlags QAbstractProxyModel.flags(QModelIndex index)'''
        return Qt.ItemFlags()
    def itemData(self, index):
        '''dict-of-int-object QAbstractProxyModel.itemData(QModelIndex index)'''
        return {int():object()}
    def setHeaderData(self, section, orientation, value, role = None):
        '''bool QAbstractProxyModel.setHeaderData(int section, Qt.Orientation orientation, QVariant value, int role = Qt.EditRole)'''
        return bool()
    def headerData(self, section, orientation, role = None):
        '''QVariant QAbstractProxyModel.headerData(int section, Qt.Orientation orientation, int role = Qt.DisplayRole)'''
        return QVariant()
    def setData(self, index, value, role = None):
        '''bool QAbstractProxyModel.setData(QModelIndex index, QVariant value, int role = Qt.EditRole)'''
        return bool()
    def data(self, proxyIndex, role = None):
        '''QVariant QAbstractProxyModel.data(QModelIndex proxyIndex, int role = Qt.DisplayRole)'''
        return QVariant()
    def revert(self):
        '''void QAbstractProxyModel.revert()'''
    def submit(self):
        '''bool QAbstractProxyModel.submit()'''
        return bool()
    def mapSelectionFromSource(self, selection):
        '''QItemSelection QAbstractProxyModel.mapSelectionFromSource(QItemSelection selection)'''
        return QItemSelection()
    def mapSelectionToSource(self, selection):
        '''QItemSelection QAbstractProxyModel.mapSelectionToSource(QItemSelection selection)'''
        return QItemSelection()
    def mapFromSource(self, sourceIndex):
        '''abstract QModelIndex QAbstractProxyModel.mapFromSource(QModelIndex sourceIndex)'''
        return QModelIndex()
    def mapToSource(self, proxyIndex):
        '''abstract QModelIndex QAbstractProxyModel.mapToSource(QModelIndex proxyIndex)'''
        return QModelIndex()
    def sourceModel(self):
        '''QAbstractItemModel QAbstractProxyModel.sourceModel()'''
        return QAbstractItemModel()
    def setSourceModel(self, sourceModel):
        '''void QAbstractProxyModel.setSourceModel(QAbstractItemModel sourceModel)'''


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
    activeChanged = pyqtSignal() # void activeChanged(bool) - signal
    def active(self):
        '''bool QAbstractState.active()'''
        return bool()
    def machine(self):
        '''QStateMachine QAbstractState.machine()'''
        return QStateMachine()
    def parentState(self):
        '''QState QAbstractState.parentState()'''
        return QState()


class QAbstractTransition(QObject):
    """"""
    # Enum QAbstractTransition.TransitionType
    ExternalTransition = 0
    InternalTransition = 0

    def __init__(self, sourceState = None):
        '''void QAbstractTransition.__init__(QState sourceState = None)'''
    def setTransitionType(self, type):
        '''void QAbstractTransition.setTransitionType(QAbstractTransition.TransitionType type)'''
    def transitionType(self):
        '''QAbstractTransition.TransitionType QAbstractTransition.transitionType()'''
        return QAbstractTransition.TransitionType()
    def event(self, e):
        '''bool QAbstractTransition.event(QEvent e)'''
        return bool()
    def onTransition(self, event):
        '''abstract void QAbstractTransition.onTransition(QEvent event)'''
    def eventTest(self, event):
        '''abstract bool QAbstractTransition.eventTest(QEvent event)'''
        return bool()
    targetStatesChanged = pyqtSignal() # void targetStatesChanged() - signal
    targetStateChanged = pyqtSignal() # void targetStateChanged() - signal
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
    def start(self, msec, timerType, obj):
        '''void QBasicTimer.start(int msec, Qt.TimerType timerType, QObject obj)'''
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
    def fill(self, value, size = None):
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
        '''void QIODevice.setErrorString(str errorString)'''
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
        '''str QIODevice.errorString()'''
        return str()
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
        '''QMetaMethod QBuffer.disconnectNotify()'''
        return QMetaMethod()
    def connectNotify(self):
        '''QMetaMethod QBuffer.connectNotify()'''
        return QMetaMethod()
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
    # Enum QByteArray.Base64Option
    Base64Encoding = 0
    Base64UrlEncoding = 0
    KeepTrailingEquals = 0
    OmitTrailingEquals = 0

    def __init__(self):
        '''void QByteArray.__init__()'''
    def __init__(self, size, c):
        '''void QByteArray.__init__(int size, str c)'''
    def __init__(self, a):
        '''void QByteArray.__init__(QByteArray a)'''
    def __add__(self, a2):
        '''QByteArray QByteArray.__add__(QByteArray a2)'''
        return QByteArray()
    def swap(self, other):
        '''void QByteArray.swap(QByteArray other)'''
    def repeated(self, times):
        '''QByteArray QByteArray.repeated(int times)'''
        return QByteArray()
    def fromPercentEncoding(self, input, percent = None):
        '''static QByteArray QByteArray.fromPercentEncoding(QByteArray input, str percent = '%')'''
        return QByteArray()
    def toPercentEncoding(self, exclude = QByteArray(), include = QByteArray(), percent = None):
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
    def fromBase64(self, base64, options):
        '''static QByteArray QByteArray.fromBase64(QByteArray base64, QByteArray.Base64Options options)'''
        return QByteArray()
    def number(self, n, base = 10):
        '''static QByteArray QByteArray.number(int n, int base = 10)'''
        return QByteArray()
    def number(self, n, format = None, precision = 6):
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
    def setNum(self, n, format = None, precision = 6):
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
    def toBase64(self, options):
        '''QByteArray QByteArray.toBase64(QByteArray.Base64Options options)'''
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
        '''bool QByteArray.__ge__(str s2)'''
        return bool()
    def __ge__(self, a2):
        '''bool QByteArray.__ge__(QByteArray a2)'''
        return bool()
    def __le__(self, s2):
        '''bool QByteArray.__le__(str s2)'''
        return bool()
    def __le__(self, a2):
        '''bool QByteArray.__le__(QByteArray a2)'''
        return bool()
    def __gt__(self, s2):
        '''bool QByteArray.__gt__(str s2)'''
        return bool()
    def __gt__(self, a2):
        '''bool QByteArray.__gt__(QByteArray a2)'''
        return bool()
    def __lt__(self, s2):
        '''bool QByteArray.__lt__(str s2)'''
        return bool()
    def __lt__(self, a2):
        '''bool QByteArray.__lt__(QByteArray a2)'''
        return bool()
    def __ne__(self, s2):
        '''bool QByteArray.__ne__(str s2)'''
        return bool()
    def __ne__(self, a2):
        '''bool QByteArray.__ne__(QByteArray a2)'''
        return bool()
    def __eq__(self, s2):
        '''bool QByteArray.__eq__(str s2)'''
        return bool()
    def __eq__(self, a2):
        '''bool QByteArray.__eq__(QByteArray a2)'''
        return bool()
    def __iadd__(self, a):
        '''QByteArray QByteArray.__iadd__(QByteArray a)'''
        return QByteArray()
    def __iadd__(self, s):
        '''QByteArray QByteArray.__iadd__(str s)'''
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
        '''QByteArray QByteArray.replace(str before, QByteArray after)'''
        return QByteArray()
    def remove(self, index, len):
        '''QByteArray QByteArray.remove(int index, int len)'''
        return QByteArray()
    def insert(self, i, a):
        '''QByteArray QByteArray.insert(int i, QByteArray a)'''
        return QByteArray()
    def insert(self, i, s):
        '''QByteArray QByteArray.insert(int i, str s)'''
        return QByteArray()
    def append(self, a):
        '''QByteArray QByteArray.append(QByteArray a)'''
        return QByteArray()
    def append(self, s):
        '''QByteArray QByteArray.append(str s)'''
        return QByteArray()
    def prepend(self, a):
        '''QByteArray QByteArray.prepend(QByteArray a)'''
        return QByteArray()
    def rightJustified(self, width, fill = None, truncate = False):
        '''QByteArray QByteArray.rightJustified(int width, str fill = ' ', bool truncate = False)'''
        return QByteArray()
    def leftJustified(self, width, fill = None, truncate = False):
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
    def mid(self, pos, length = None):
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
    def lastIndexOf(self, ba, from_ = None):
        '''int QByteArray.lastIndexOf(QByteArray ba, int from = -1)'''
        return int()
    def lastIndexOf(self, str, from_ = None):
        '''int QByteArray.lastIndexOf(str str, int from = -1)'''
        return int()
    def indexOf(self, ba, from_ = 0):
        '''int QByteArray.indexOf(QByteArray ba, int from = 0)'''
        return int()
    def indexOf(self, str, from_ = 0):
        '''int QByteArray.indexOf(str str, int from = 0)'''
        return int()
    def clear(self):
        '''void QByteArray.clear()'''
    def fill(self, ch, size = None):
        '''QByteArray QByteArray.fill(str ch, int size = -1)'''
        return QByteArray()
    def resize(self, size):
        '''void QByteArray.resize(int size)'''
    class Base64Options():
        """"""
        def __init__(self):
            '''QByteArray.Base64Options QByteArray.Base64Options.__init__()'''
            return QByteArray.Base64Options()
        def __init__(self):
            '''int QByteArray.Base64Options.__init__()'''
            return int()
        def __init__(self):
            '''void QByteArray.Base64Options.__init__()'''
        def __bool__(self):
            '''int QByteArray.Base64Options.__bool__()'''
            return int()
        def __ne__(self, f):
            '''bool QByteArray.Base64Options.__ne__(QByteArray.Base64Options f)'''
            return bool()
        def __eq__(self, f):
            '''bool QByteArray.Base64Options.__eq__(QByteArray.Base64Options f)'''
            return bool()
        def __invert__(self):
            '''QByteArray.Base64Options QByteArray.Base64Options.__invert__()'''
            return QByteArray.Base64Options()
        def __and__(self, mask):
            '''QByteArray.Base64Options QByteArray.Base64Options.__and__(int mask)'''
            return QByteArray.Base64Options()
        def __xor__(self, f):
            '''QByteArray.Base64Options QByteArray.Base64Options.__xor__(QByteArray.Base64Options f)'''
            return QByteArray.Base64Options()
        def __xor__(self, f):
            '''QByteArray.Base64Options QByteArray.Base64Options.__xor__(int f)'''
            return QByteArray.Base64Options()
        def __or__(self, f):
            '''QByteArray.Base64Options QByteArray.Base64Options.__or__(QByteArray.Base64Options f)'''
            return QByteArray.Base64Options()
        def __or__(self, f):
            '''QByteArray.Base64Options QByteArray.Base64Options.__or__(int f)'''
            return QByteArray.Base64Options()
        def __int__(self):
            '''int QByteArray.Base64Options.__int__()'''
            return int()
        def __ixor__(self, f):
            '''QByteArray.Base64Options QByteArray.Base64Options.__ixor__(QByteArray.Base64Options f)'''
            return QByteArray.Base64Options()
        def __ior__(self, f):
            '''QByteArray.Base64Options QByteArray.Base64Options.__ior__(QByteArray.Base64Options f)'''
            return QByteArray.Base64Options()
        def __iand__(self, mask):
            '''QByteArray.Base64Options QByteArray.Base64Options.__iand__(int mask)'''
            return QByteArray.Base64Options()


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


class QCollatorSortKey():
    """"""
    def __init__(self, other):
        '''void QCollatorSortKey.__init__(QCollatorSortKey other)'''
    def __ge__(self, rhs):
        '''bool QCollatorSortKey.__ge__(QCollatorSortKey rhs)'''
        return bool()
    def __lt__(self, rhs):
        '''bool QCollatorSortKey.__lt__(QCollatorSortKey rhs)'''
        return bool()
    def compare(self, key):
        '''int QCollatorSortKey.compare(QCollatorSortKey key)'''
        return int()
    def swap(self, other):
        '''void QCollatorSortKey.swap(QCollatorSortKey other)'''


class QCollator():
    """"""
    def __init__(self, locale = QLocale()):
        '''void QCollator.__init__(QLocale locale = QLocale())'''
    def __init__(self):
        '''QCollator QCollator.__init__()'''
        return QCollator()
    def sortKey(self, string):
        '''QCollatorSortKey QCollator.sortKey(str string)'''
        return QCollatorSortKey()
    def compare(self, s1, s2):
        '''int QCollator.compare(str s1, str s2)'''
        return int()
    def ignorePunctuation(self):
        '''bool QCollator.ignorePunctuation()'''
        return bool()
    def setIgnorePunctuation(self, on):
        '''void QCollator.setIgnorePunctuation(bool on)'''
    def numericMode(self):
        '''bool QCollator.numericMode()'''
        return bool()
    def setNumericMode(self, on):
        '''void QCollator.setNumericMode(bool on)'''
    def setCaseSensitivity(self, cs):
        '''void QCollator.setCaseSensitivity(Qt.CaseSensitivity cs)'''
    def caseSensitivity(self):
        '''Qt.CaseSensitivity QCollator.caseSensitivity()'''
        return Qt.CaseSensitivity()
    def locale(self):
        '''QLocale QCollator.locale()'''
        return QLocale()
    def setLocale(self, locale):
        '''void QCollator.setLocale(QLocale locale)'''
    def swap(self, other):
        '''void QCollator.swap(QCollator other)'''


class QCommandLineOption():
    """"""
    def __init__(self, name):
        '''void QCommandLineOption.__init__(str name)'''
    def __init__(self, names):
        '''void QCommandLineOption.__init__(list-of-str names)'''
    def __init__(self, name, description, valueName = str(), defaultValue = str()):
        '''void QCommandLineOption.__init__(str name, str description, str valueName = str(), str defaultValue = str())'''
    def __init__(self, names, description, valueName = str(), defaultValue = str()):
        '''void QCommandLineOption.__init__(list-of-str names, str description, str valueName = str(), str defaultValue = str())'''
    def __init__(self, other):
        '''void QCommandLineOption.__init__(QCommandLineOption other)'''
    def defaultValues(self):
        '''list-of-str QCommandLineOption.defaultValues()'''
        return [str()]
    def setDefaultValues(self, defaultValues):
        '''void QCommandLineOption.setDefaultValues(list-of-str defaultValues)'''
    def setDefaultValue(self, defaultValue):
        '''void QCommandLineOption.setDefaultValue(str defaultValue)'''
    def description(self):
        '''str QCommandLineOption.description()'''
        return str()
    def setDescription(self, description):
        '''void QCommandLineOption.setDescription(str description)'''
    def valueName(self):
        '''str QCommandLineOption.valueName()'''
        return str()
    def setValueName(self, name):
        '''void QCommandLineOption.setValueName(str name)'''
    def names(self):
        '''list-of-str QCommandLineOption.names()'''
        return [str()]
    def swap(self, other):
        '''void QCommandLineOption.swap(QCommandLineOption other)'''


class QCommandLineParser():
    """"""
    # Enum QCommandLineParser.SingleDashWordOptionMode
    ParseAsCompactedShortOptions = 0
    ParseAsLongOptions = 0

    def __init__(self):
        '''void QCommandLineParser.__init__()'''
    def showVersion(self):
        '''void QCommandLineParser.showVersion()'''
    def addOptions(self, options):
        '''bool QCommandLineParser.addOptions(list-of-QCommandLineOption options)'''
        return bool()
    def helpText(self):
        '''str QCommandLineParser.helpText()'''
        return str()
    def showHelp(self, exitCode = 0):
        '''void QCommandLineParser.showHelp(int exitCode = 0)'''
    def unknownOptionNames(self):
        '''list-of-str QCommandLineParser.unknownOptionNames()'''
        return [str()]
    def optionNames(self):
        '''list-of-str QCommandLineParser.optionNames()'''
        return [str()]
    def positionalArguments(self):
        '''list-of-str QCommandLineParser.positionalArguments()'''
        return [str()]
    def values(self, name):
        '''list-of-str QCommandLineParser.values(str name)'''
        return [str()]
    def values(self, option):
        '''list-of-str QCommandLineParser.values(QCommandLineOption option)'''
        return [str()]
    def value(self, name):
        '''str QCommandLineParser.value(str name)'''
        return str()
    def value(self, option):
        '''str QCommandLineParser.value(QCommandLineOption option)'''
        return str()
    def isSet(self, name):
        '''bool QCommandLineParser.isSet(str name)'''
        return bool()
    def isSet(self, option):
        '''bool QCommandLineParser.isSet(QCommandLineOption option)'''
        return bool()
    def errorText(self):
        '''str QCommandLineParser.errorText()'''
        return str()
    def parse(self, arguments):
        '''bool QCommandLineParser.parse(list-of-str arguments)'''
        return bool()
    def process(self, arguments):
        '''void QCommandLineParser.process(list-of-str arguments)'''
    def process(self, app):
        '''void QCommandLineParser.process(QCoreApplication app)'''
    def clearPositionalArguments(self):
        '''void QCommandLineParser.clearPositionalArguments()'''
    def addPositionalArgument(self, name, description, syntax = str()):
        '''void QCommandLineParser.addPositionalArgument(str name, str description, str syntax = str())'''
    def applicationDescription(self):
        '''str QCommandLineParser.applicationDescription()'''
        return str()
    def setApplicationDescription(self, description):
        '''void QCommandLineParser.setApplicationDescription(str description)'''
    def addHelpOption(self):
        '''QCommandLineOption QCommandLineParser.addHelpOption()'''
        return QCommandLineOption()
    def addVersionOption(self):
        '''QCommandLineOption QCommandLineParser.addVersionOption()'''
        return QCommandLineOption()
    def addOption(self, commandLineOption):
        '''bool QCommandLineParser.addOption(QCommandLineOption commandLineOption)'''
        return bool()
    def setSingleDashWordOptionMode(self, parsingMode):
        '''void QCommandLineParser.setSingleDashWordOptionMode(QCommandLineParser.SingleDashWordOptionMode parsingMode)'''


class QCoreApplication(QObject):
    """"""
    def __init__(self, argv):
        '''void QCoreApplication.__init__(list-of-str argv)'''
    def isSetuidAllowed(self):
        '''static bool QCoreApplication.isSetuidAllowed()'''
        return bool()
    def setSetuidAllowed(self, allow):
        '''static void QCoreApplication.setSetuidAllowed(bool allow)'''
    def removeNativeEventFilter(self, filterObj):
        '''void QCoreApplication.removeNativeEventFilter(QAbstractNativeEventFilter filterObj)'''
    def installNativeEventFilter(self, filterObj):
        '''void QCoreApplication.installNativeEventFilter(QAbstractNativeEventFilter filterObj)'''
    def setQuitLockEnabled(self, enabled):
        '''static void QCoreApplication.setQuitLockEnabled(bool enabled)'''
    def isQuitLockEnabled(self):
        '''static bool QCoreApplication.isQuitLockEnabled()'''
        return bool()
    def setEventDispatcher(self, eventDispatcher):
        '''static void QCoreApplication.setEventDispatcher(QAbstractEventDispatcher eventDispatcher)'''
    def eventDispatcher(self):
        '''static QAbstractEventDispatcher QCoreApplication.eventDispatcher()'''
        return QAbstractEventDispatcher()
    def applicationPid(self):
        '''static int QCoreApplication.applicationPid()'''
        return int()
    def applicationVersion(self):
        '''static str QCoreApplication.applicationVersion()'''
        return str()
    def setApplicationVersion(self, version):
        '''static void QCoreApplication.setApplicationVersion(str version)'''
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
    def translate(self, context, sourceText, disambiguation = None, n = None):
        '''static str QCoreApplication.translate(str context, str sourceText, str disambiguation = None, int n = -1)'''
        return str()
    def removeTranslator(self, messageFile):
        '''static bool QCoreApplication.removeTranslator(QTranslator messageFile)'''
        return bool()
    def installTranslator(self, messageFile):
        '''static bool QCoreApplication.installTranslator(QTranslator messageFile)'''
        return bool()
    def removeLibraryPath(self):
        '''static str QCoreApplication.removeLibraryPath()'''
        return str()
    def addLibraryPath(self):
        '''static str QCoreApplication.addLibraryPath()'''
        return str()
    def libraryPaths(self):
        '''static list-of-str QCoreApplication.libraryPaths()'''
        return [str()]
    def setLibraryPaths(self):
        '''static list-of-str QCoreApplication.setLibraryPaths()'''
        return [str()]
    def applicationFilePath(self):
        '''static str QCoreApplication.applicationFilePath()'''
        return str()
    def applicationDirPath(self):
        '''static str QCoreApplication.applicationDirPath()'''
        return str()
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
    def removePostedEvents(self, receiver, eventType = 0):
        '''static void QCoreApplication.removePostedEvents(QObject receiver, int eventType = 0)'''
    def sendPostedEvents(self, receiver = None, eventType = 0):
        '''static void QCoreApplication.sendPostedEvents(QObject receiver = None, int eventType = 0)'''
    def postEvent(self, receiver, event, priority = None):
        '''static void QCoreApplication.postEvent(QObject receiver, QEvent event, int priority = Qt.NormalEventPriority)'''
    def sendEvent(self, receiver, event):
        '''static bool QCoreApplication.sendEvent(QObject receiver, QEvent event)'''
        return bool()
    def exit(self, returnCode = 0):
        '''static void QCoreApplication.exit(int returnCode = 0)'''
    def processEvents(self, flags = None):
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
        '''static list-of-str QCoreApplication.arguments()'''
        return [str()]
    def applicationName(self):
        '''static str QCoreApplication.applicationName()'''
        return str()
    def setApplicationName(self, application):
        '''static void QCoreApplication.setApplicationName(str application)'''
    def organizationName(self):
        '''static str QCoreApplication.organizationName()'''
        return str()
    def setOrganizationName(self, orgName):
        '''static void QCoreApplication.setOrganizationName(str orgName)'''
    def organizationDomain(self):
        '''static str QCoreApplication.organizationDomain()'''
        return str()
    def setOrganizationDomain(self, orgDomain):
        '''static void QCoreApplication.setOrganizationDomain(str orgDomain)'''


class QEvent():
    """"""
    # Enum QEvent.Type
    None_ = 0
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
    ThreadChange = 0
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
    NonClientAreaMouseMove = 0
    NonClientAreaMouseButtonPress = 0
    NonClientAreaMouseButtonRelease = 0
    NonClientAreaMouseButtonDblClick = 0
    MacSizeChange = 0
    ContentsRectChange = 0
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
    FocusAboutToChange = 0
    ScrollPrepare = 0
    Scroll = 0
    Expose = 0
    InputMethodQuery = 0
    OrientationChange = 0
    TouchCancel = 0
    PlatformPanel = 0
    ApplicationStateChange = 0
    ReadOnlyChange = 0
    PlatformSurface = 0
    User = 0
    MaxUser = 0

    def __init__(self, type):
        '''void QEvent.__init__(QEvent.Type type)'''
    def __init__(self, other):
        '''void QEvent.__init__(QEvent other)'''
    def registerEventType(self, hint = None):
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
    Sha224 = 0
    Sha256 = 0
    Sha384 = 0
    Sha512 = 0
    Sha3_224 = 0
    Sha3_256 = 0
    Sha3_384 = 0
    Sha3_512 = 0

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
    def addData(self, device):
        '''bool QCryptographicHash.addData(QIODevice device)'''
        return bool()
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
    Qt_4_9 = 0
    Qt_5_0 = 0
    Qt_5_1 = 0
    Qt_5_2 = 0
    Qt_5_3 = 0
    Qt_5_4 = 0
    Qt_5_5 = 0

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
        '''QMargins QDataStream.__lshift__()'''
        return QMargins()
    def __lshift__(self):
        '''QMarginsF QDataStream.__lshift__()'''
        return QMarginsF()
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
    def __lshift__(self, re):
        '''QDataStream QDataStream.__lshift__(QRegularExpression re)'''
        return QDataStream()
    def __lshift__(self):
        '''QSize QDataStream.__lshift__()'''
        return QSize()
    def __lshift__(self):
        '''QSizeF QDataStream.__lshift__()'''
        return QSizeF()
    def __lshift__(self, tz):
        '''QDataStream QDataStream.__lshift__(QTimeZone tz)'''
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
        '''QDataStream QDataStream.__lshift__(QVariant.Type p)'''
        return QDataStream()
    def __rshift__(self):
        '''QBitArray QDataStream.__rshift__()'''
        return QBitArray()
    def __rshift__(self):
        '''QByteArray QDataStream.__rshift__()'''
        return QByteArray()
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
        '''QMargins QDataStream.__rshift__()'''
        return QMargins()
    def __rshift__(self):
        '''QMarginsF QDataStream.__rshift__()'''
        return QMarginsF()
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
    def __rshift__(self, re):
        '''QDataStream QDataStream.__rshift__(QRegularExpression re)'''
        return QDataStream()
    def __rshift__(self):
        '''QSize QDataStream.__rshift__()'''
        return QSize()
    def __rshift__(self):
        '''QSizeF QDataStream.__rshift__()'''
        return QSizeF()
    def __rshift__(self, tz):
        '''QDataStream QDataStream.__rshift__(QTimeZone tz)'''
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
        '''QDataStream QDataStream.__rshift__(QVariant.Type p)'''
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
        '''void QDataStream.writeQVariantHash(dict-of-str-object qvarhash)'''
    def readQVariantHash(self):
        '''dict-of-str-object QDataStream.readQVariantHash()'''
        return {str():object()}
    def writeQVariantMap(self, qvarmap):
        '''void QDataStream.writeQVariantMap(dict-of-str-object qvarmap)'''
    def readQVariantMap(self):
        '''dict-of-str-object QDataStream.readQVariantMap()'''
        return {str():object()}
    def writeQVariantList(self, qvarlst):
        '''void QDataStream.writeQVariantList(list-of-object qvarlst)'''
    def readQVariantList(self):
        '''list-of-object QDataStream.readQVariantList()'''
        return [object()]
    def writeQVariant(self, qvar):
        '''void QDataStream.writeQVariant(QVariant qvar)'''
    def readQVariant(self):
        '''QVariant QDataStream.readQVariant()'''
        return QVariant()
    def writeQStringList(self, qstrlst):
        '''void QDataStream.writeQStringList(list-of-str qstrlst)'''
    def readQStringList(self):
        '''list-of-str QDataStream.readQStringList()'''
        return [str()]
    def writeQString(self, qstr):
        '''void QDataStream.writeQString(str qstr)'''
    def readQString(self):
        '''str QDataStream.readQString()'''
        return str()
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
        '''void QDataStream.writeUInt8(int i)'''
    def writeInt8(self, i):
        '''void QDataStream.writeInt8(int i)'''
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
        '''int QDataStream.readUInt8()'''
        return int()
    def readInt8(self):
        '''int QDataStream.readInt8()'''
        return int()
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
    def isLeapYear(self, year):
        '''static bool QDate.isLeapYear(int year)'''
        return bool()
    def fromString(self, string, format = None):
        '''static QDate QDate.fromString(str string, Qt.DateFormat format = Qt.TextDate)'''
        return QDate()
    def fromString(self, s, format):
        '''static QDate QDate.fromString(str s, str format)'''
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
    def toString(self, format = None):
        '''str QDate.toString(Qt.DateFormat format = Qt.TextDate)'''
        return str()
    def toString(self, format):
        '''str QDate.toString(str format)'''
        return str()
    def longDayName(self, weekday, type = None):
        '''static str QDate.longDayName(int weekday, QDate.MonthNameType type = QDate.DateFormat)'''
        return str()
    def longMonthName(self, month, type = None):
        '''static str QDate.longMonthName(int month, QDate.MonthNameType type = QDate.DateFormat)'''
        return str()
    def shortDayName(self, weekday, type = None):
        '''static str QDate.shortDayName(int weekday, QDate.MonthNameType type = QDate.DateFormat)'''
        return str()
    def shortMonthName(self, month, type = None):
        '''static str QDate.shortMonthName(int month, QDate.MonthNameType type = QDate.DateFormat)'''
        return str()
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
    def msecsSinceStartOfDay(self):
        '''int QTime.msecsSinceStartOfDay()'''
        return int()
    def fromMSecsSinceStartOfDay(self, msecs):
        '''static QTime QTime.fromMSecsSinceStartOfDay(int msecs)'''
        return QTime()
    def elapsed(self):
        '''int QTime.elapsed()'''
        return int()
    def restart(self):
        '''int QTime.restart()'''
        return int()
    def start(self):
        '''void QTime.start()'''
    def fromString(self, string, format = None):
        '''static QTime QTime.fromString(str string, Qt.DateFormat format = Qt.TextDate)'''
        return QTime()
    def fromString(self, s, format):
        '''static QTime QTime.fromString(str s, str format)'''
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
    def toString(self, format = None):
        '''str QTime.toString(Qt.DateFormat format = Qt.TextDate)'''
        return str()
    def toString(self, format):
        '''str QTime.toString(str format)'''
        return str()
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
    def __init__(self, date, time, timeSpec = None):
        '''void QDateTime.__init__(QDate date, QTime time, Qt.TimeSpec timeSpec = Qt.LocalTime)'''
    def __init__(self, y, m, d, h, m_, s = 0, msec = 0, timeSpec = 0):
        '''void QDateTime.__init__(int y, int m, int d, int h, int m, int s = 0, int msec = 0, int timeSpec = 0)'''
    def __init__(self, date, time, spec, offsetSeconds):
        '''void QDateTime.__init__(QDate date, QTime time, Qt.TimeSpec spec, int offsetSeconds)'''
    def __init__(self, date, time, timeZone):
        '''void QDateTime.__init__(QDate date, QTime time, QTimeZone timeZone)'''
    def toTimeZone(self, toZone):
        '''QDateTime QDateTime.toTimeZone(QTimeZone toZone)'''
        return QDateTime()
    def toOffsetFromUtc(self, offsetSeconds):
        '''QDateTime QDateTime.toOffsetFromUtc(int offsetSeconds)'''
        return QDateTime()
    def setTimeZone(self, toZone):
        '''void QDateTime.setTimeZone(QTimeZone toZone)'''
    def setOffsetFromUtc(self, offsetSeconds):
        '''void QDateTime.setOffsetFromUtc(int offsetSeconds)'''
    def isDaylightTime(self):
        '''bool QDateTime.isDaylightTime()'''
        return bool()
    def timeZoneAbbreviation(self):
        '''str QDateTime.timeZoneAbbreviation()'''
        return str()
    def timeZone(self):
        '''QTimeZone QDateTime.timeZone()'''
        return QTimeZone()
    def offsetFromUtc(self):
        '''int QDateTime.offsetFromUtc()'''
        return int()
    def swap(self, other):
        '''void QDateTime.swap(QDateTime other)'''
    def currentMSecsSinceEpoch(self):
        '''static int QDateTime.currentMSecsSinceEpoch()'''
        return int()
    def fromMSecsSinceEpoch(self, msecs):
        '''static QDateTime QDateTime.fromMSecsSinceEpoch(int msecs)'''
        return QDateTime()
    def fromMSecsSinceEpoch(self, msecs, spec, offsetSeconds = 0):
        '''static QDateTime QDateTime.fromMSecsSinceEpoch(int msecs, Qt.TimeSpec spec, int offsetSeconds = 0)'''
        return QDateTime()
    def fromMSecsSinceEpoch(self, msecs, timeZone):
        '''static QDateTime QDateTime.fromMSecsSinceEpoch(int msecs, QTimeZone timeZone)'''
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
    def fromTime_t(self, secsSince1Jan1970UTC, spec, offsetSeconds = 0):
        '''static QDateTime QDateTime.fromTime_t(int secsSince1Jan1970UTC, Qt.TimeSpec spec, int offsetSeconds = 0)'''
        return QDateTime()
    def fromTime_t(self, secsSince1Jan1970UTC, timeZone):
        '''static QDateTime QDateTime.fromTime_t(int secsSince1Jan1970UTC, QTimeZone timeZone)'''
        return QDateTime()
    def fromString(self, string, format = None):
        '''static QDateTime QDateTime.fromString(str string, Qt.DateFormat format = Qt.TextDate)'''
        return QDateTime()
    def fromString(self, s, format):
        '''static QDateTime QDateTime.fromString(str s, str format)'''
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
    def toString(self, format = None):
        '''str QDateTime.toString(Qt.DateFormat format = Qt.TextDate)'''
        return str()
    def toString(self, format):
        '''str QDateTime.toString(str format)'''
        return str()
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
    def __init__(self, path = None):
        '''void QDir.__init__(str path = '')'''
    def __init__(self, path, nameFilter, sort = None, filters = None):
        '''void QDir.__init__(str path, str nameFilter, QDir.SortFlags sort = QDir.Name|QDir.IgnoreCase, QDir.Filters filters = QDir.AllEntries)'''
    def swap(self, other):
        '''void QDir.swap(QDir other)'''
    def removeRecursively(self):
        '''bool QDir.removeRecursively()'''
        return bool()
    def searchPaths(self, prefix):
        '''static list-of-str QDir.searchPaths(str prefix)'''
        return [str()]
    def addSearchPath(self, prefix, path):
        '''static void QDir.addSearchPath(str prefix, str path)'''
    def setSearchPaths(self, prefix, searchPaths):
        '''static void QDir.setSearchPaths(str prefix, list-of-str searchPaths)'''
    def fromNativeSeparators(self, pathName):
        '''static str QDir.fromNativeSeparators(str pathName)'''
        return str()
    def toNativeSeparators(self, pathName):
        '''static str QDir.toNativeSeparators(str pathName)'''
        return str()
    def cleanPath(self, path):
        '''static str QDir.cleanPath(str path)'''
        return str()
    def match(self, filters, fileName):
        '''static bool QDir.match(list-of-str filters, str fileName)'''
        return bool()
    def match(self, filter, fileName):
        '''static bool QDir.match(str filter, str fileName)'''
        return bool()
    def tempPath(self):
        '''static str QDir.tempPath()'''
        return str()
    def temp(self):
        '''static QDir QDir.temp()'''
        return QDir()
    def rootPath(self):
        '''static str QDir.rootPath()'''
        return str()
    def root(self):
        '''static QDir QDir.root()'''
        return QDir()
    def homePath(self):
        '''static str QDir.homePath()'''
        return str()
    def home(self):
        '''static QDir QDir.home()'''
        return QDir()
    def currentPath(self):
        '''static str QDir.currentPath()'''
        return str()
    def current(self):
        '''static QDir QDir.current()'''
        return QDir()
    def setCurrent(self, path):
        '''static bool QDir.setCurrent(str path)'''
        return bool()
    def separator(self):
        '''static str QDir.separator()'''
        return str()
    def drives(self):
        '''static list-of-QFileInfo QDir.drives()'''
        return [QFileInfo()]
    def refresh(self):
        '''void QDir.refresh()'''
    def rename(self, oldName, newName):
        '''bool QDir.rename(str oldName, str newName)'''
        return bool()
    def remove(self, fileName):
        '''bool QDir.remove(str fileName)'''
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
        '''static bool QDir.isAbsolutePath(str path)'''
        return bool()
    def isRelativePath(self, path):
        '''static bool QDir.isRelativePath(str path)'''
        return bool()
    def isRoot(self):
        '''bool QDir.isRoot()'''
        return bool()
    def exists(self):
        '''bool QDir.exists()'''
        return bool()
    def exists(self, name):
        '''bool QDir.exists(str name)'''
        return bool()
    def isReadable(self):
        '''bool QDir.isReadable()'''
        return bool()
    def rmpath(self, dirPath):
        '''bool QDir.rmpath(str dirPath)'''
        return bool()
    def mkpath(self, dirPath):
        '''bool QDir.mkpath(str dirPath)'''
        return bool()
    def rmdir(self, dirName):
        '''bool QDir.rmdir(str dirName)'''
        return bool()
    def mkdir(self, dirName):
        '''bool QDir.mkdir(str dirName)'''
        return bool()
    def entryInfoList(self, filters = None, sort = None):
        '''list-of-QFileInfo QDir.entryInfoList(QDir.Filters filters = QDir.NoFilter, QDir.SortFlags sort = QDir.NoSort)'''
        return [QFileInfo()]
    def entryInfoList(self, nameFilters, filters = None, sort = None):
        '''list-of-QFileInfo QDir.entryInfoList(list-of-str nameFilters, QDir.Filters filters = QDir.NoFilter, QDir.SortFlags sort = QDir.NoSort)'''
        return [QFileInfo()]
    def entryList(self, filters = None, sort = None):
        '''list-of-str QDir.entryList(QDir.Filters filters = QDir.NoFilter, QDir.SortFlags sort = QDir.NoSort)'''
        return [str()]
    def entryList(self, nameFilters, filters = None, sort = None):
        '''list-of-str QDir.entryList(list-of-str nameFilters, QDir.Filters filters = QDir.NoFilter, QDir.SortFlags sort = QDir.NoSort)'''
        return [str()]
    def nameFiltersFromString(self, nameFilter):
        '''static list-of-str QDir.nameFiltersFromString(str nameFilter)'''
        return [str()]
    def __contains__(self):
        '''str QDir.__contains__()'''
        return str()
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
        '''void QDir.setNameFilters(list-of-str nameFilters)'''
    def nameFilters(self):
        '''list-of-str QDir.nameFilters()'''
        return [str()]
    def cdUp(self):
        '''bool QDir.cdUp()'''
        return bool()
    def cd(self, dirName):
        '''bool QDir.cd(str dirName)'''
        return bool()
    def relativeFilePath(self, fileName):
        '''str QDir.relativeFilePath(str fileName)'''
        return str()
    def absoluteFilePath(self, fileName):
        '''str QDir.absoluteFilePath(str fileName)'''
        return str()
    def filePath(self, fileName):
        '''str QDir.filePath(str fileName)'''
        return str()
    def dirName(self):
        '''str QDir.dirName()'''
        return str()
    def canonicalPath(self):
        '''str QDir.canonicalPath()'''
        return str()
    def absolutePath(self):
        '''str QDir.absolutePath()'''
        return str()
    def path(self):
        '''str QDir.path()'''
        return str()
    def setPath(self, path):
        '''void QDir.setPath(str path)'''
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

    def __init__(self, dir, flags = None):
        '''void QDirIterator.__init__(QDir dir, QDirIterator.IteratorFlags flags = QDirIterator.NoIteratorFlags)'''
    def __init__(self, path, flags = None):
        '''void QDirIterator.__init__(str path, QDirIterator.IteratorFlags flags = QDirIterator.NoIteratorFlags)'''
    def __init__(self, path, filters, flags = None):
        '''void QDirIterator.__init__(str path, QDir.Filters filters, QDirIterator.IteratorFlags flags = QDirIterator.NoIteratorFlags)'''
    def __init__(self, path, nameFilters, filters = None, flags = None):
        '''void QDirIterator.__init__(str path, list-of-str nameFilters, QDir.Filters filters = QDir.NoFilter, QDirIterator.IteratorFlags flags = QDirIterator.NoIteratorFlags)'''
    def path(self):
        '''str QDirIterator.path()'''
        return str()
    def fileInfo(self):
        '''QFileInfo QDirIterator.fileInfo()'''
        return QFileInfo()
    def filePath(self):
        '''str QDirIterator.filePath()'''
        return str()
    def fileName(self):
        '''str QDirIterator.fileName()'''
        return str()
    def hasNext(self):
        '''bool QDirIterator.hasNext()'''
        return bool()
    def next(self):
        '''str QDirIterator.next()'''
        return str()
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
    BezierSpline = 0
    TCBSpline = 0
    Custom = 0

    def __init__(self, type = None):
        '''void QEasingCurve.__init__(QEasingCurve.Type type = QEasingCurve.Linear)'''
    def __init__(self, other):
        '''void QEasingCurve.__init__(QEasingCurve other)'''
    def toCubicSpline(self):
        '''list-of-QPointF QEasingCurve.toCubicSpline()'''
        return [QPointF()]
    def addTCBSegment(self, nextPoint, t, c, b):
        '''void QEasingCurve.addTCBSegment(QPointF nextPoint, float t, float c, float b)'''
    def addCubicBezierSegment(self, c1, c2, endPoint):
        '''void QEasingCurve.addCubicBezierSegment(QPointF c1, QPointF c2, QPointF endPoint)'''
    def swap(self, other):
        '''void QEasingCurve.swap(QEasingCurve other)'''
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

    def __init__(self, parent = None):
        '''void QEventLoop.__init__(QObject parent = None)'''
    def event(self, event):
        '''bool QEventLoop.event(QEvent event)'''
        return bool()
    def quit(self):
        '''void QEventLoop.quit()'''
    def wakeUp(self):
        '''void QEventLoop.wakeUp()'''
    def isRunning(self):
        '''bool QEventLoop.isRunning()'''
        return bool()
    def exit(self, returnCode = 0):
        '''void QEventLoop.exit(int returnCode = 0)'''
    def exec_(self, flags = None):
        '''int QEventLoop.exec_(QEventLoop.ProcessEventsFlags flags = QEventLoop.AllEvents)'''
        return int()
    def processEvents(self, flags = None):
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


class QEventLoopLocker():
    """"""
    def __init__(self):
        '''void QEventLoopLocker.__init__()'''
    def __init__(self, loop):
        '''void QEventLoopLocker.__init__(QEventLoop loop)'''
    def __init__(self, thread):
        '''void QEventLoopLocker.__init__(QThread thread)'''


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


class QFileDevice(QIODevice):
    """"""
    # Enum QFileDevice.MemoryMapFlags
    NoOptions = 0
    MapPrivateOption = 0

    # Enum QFileDevice.FileHandleFlag
    AutoCloseHandle = 0
    DontCloseHandle = 0

    # Enum QFileDevice.Permission
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

    # Enum QFileDevice.FileError
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

    def readLineData(self, maxlen):
        '''str QFileDevice.readLineData(int maxlen)'''
        return str()
    def writeData(self, data):
        '''int QFileDevice.writeData(str data)'''
        return int()
    def readData(self, maxlen):
        '''str QFileDevice.readData(int maxlen)'''
        return str()
    def unmap(self, address):
        '''bool QFileDevice.unmap(sip.voidptr address)'''
        return bool()
    def map(self, offset, size, flags = None):
        '''sip.voidptr QFileDevice.map(int offset, int size, QFileDevice.MemoryMapFlags flags = QFileDevice.NoOptions)'''
        return sip.voidptr()
    def setPermissions(self, permissionSpec):
        '''bool QFileDevice.setPermissions(QFileDevice.Permissions permissionSpec)'''
        return bool()
    def permissions(self):
        '''QFileDevice.Permissions QFileDevice.permissions()'''
        return QFileDevice.Permissions()
    def resize(self, sz):
        '''bool QFileDevice.resize(int sz)'''
        return bool()
    def size(self):
        '''int QFileDevice.size()'''
        return int()
    def flush(self):
        '''bool QFileDevice.flush()'''
        return bool()
    def atEnd(self):
        '''bool QFileDevice.atEnd()'''
        return bool()
    def seek(self, offset):
        '''bool QFileDevice.seek(int offset)'''
        return bool()
    def pos(self):
        '''int QFileDevice.pos()'''
        return int()
    def fileName(self):
        '''str QFileDevice.fileName()'''
        return str()
    def handle(self):
        '''int QFileDevice.handle()'''
        return int()
    def isSequential(self):
        '''bool QFileDevice.isSequential()'''
        return bool()
    def close(self):
        '''void QFileDevice.close()'''
    def unsetError(self):
        '''void QFileDevice.unsetError()'''
    def error(self):
        '''QFileDevice.FileError QFileDevice.error()'''
        return QFileDevice.FileError()
    class FileHandleFlags():
        """"""
        def __init__(self):
            '''QFileDevice.FileHandleFlags QFileDevice.FileHandleFlags.__init__()'''
            return QFileDevice.FileHandleFlags()
        def __init__(self):
            '''int QFileDevice.FileHandleFlags.__init__()'''
            return int()
        def __init__(self):
            '''void QFileDevice.FileHandleFlags.__init__()'''
        def __bool__(self):
            '''int QFileDevice.FileHandleFlags.__bool__()'''
            return int()
        def __ne__(self, f):
            '''bool QFileDevice.FileHandleFlags.__ne__(QFileDevice.FileHandleFlags f)'''
            return bool()
        def __eq__(self, f):
            '''bool QFileDevice.FileHandleFlags.__eq__(QFileDevice.FileHandleFlags f)'''
            return bool()
        def __invert__(self):
            '''QFileDevice.FileHandleFlags QFileDevice.FileHandleFlags.__invert__()'''
            return QFileDevice.FileHandleFlags()
        def __and__(self, mask):
            '''QFileDevice.FileHandleFlags QFileDevice.FileHandleFlags.__and__(int mask)'''
            return QFileDevice.FileHandleFlags()
        def __xor__(self, f):
            '''QFileDevice.FileHandleFlags QFileDevice.FileHandleFlags.__xor__(QFileDevice.FileHandleFlags f)'''
            return QFileDevice.FileHandleFlags()
        def __xor__(self, f):
            '''QFileDevice.FileHandleFlags QFileDevice.FileHandleFlags.__xor__(int f)'''
            return QFileDevice.FileHandleFlags()
        def __or__(self, f):
            '''QFileDevice.FileHandleFlags QFileDevice.FileHandleFlags.__or__(QFileDevice.FileHandleFlags f)'''
            return QFileDevice.FileHandleFlags()
        def __or__(self, f):
            '''QFileDevice.FileHandleFlags QFileDevice.FileHandleFlags.__or__(int f)'''
            return QFileDevice.FileHandleFlags()
        def __int__(self):
            '''int QFileDevice.FileHandleFlags.__int__()'''
            return int()
        def __ixor__(self, f):
            '''QFileDevice.FileHandleFlags QFileDevice.FileHandleFlags.__ixor__(QFileDevice.FileHandleFlags f)'''
            return QFileDevice.FileHandleFlags()
        def __ior__(self, f):
            '''QFileDevice.FileHandleFlags QFileDevice.FileHandleFlags.__ior__(QFileDevice.FileHandleFlags f)'''
            return QFileDevice.FileHandleFlags()
        def __iand__(self, mask):
            '''QFileDevice.FileHandleFlags QFileDevice.FileHandleFlags.__iand__(int mask)'''
            return QFileDevice.FileHandleFlags()
    class Permissions():
        """"""
        def __init__(self):
            '''QFileDevice.Permissions QFileDevice.Permissions.__init__()'''
            return QFileDevice.Permissions()
        def __init__(self):
            '''int QFileDevice.Permissions.__init__()'''
            return int()
        def __init__(self):
            '''void QFileDevice.Permissions.__init__()'''
        def __bool__(self):
            '''int QFileDevice.Permissions.__bool__()'''
            return int()
        def __ne__(self, f):
            '''bool QFileDevice.Permissions.__ne__(QFileDevice.Permissions f)'''
            return bool()
        def __eq__(self, f):
            '''bool QFileDevice.Permissions.__eq__(QFileDevice.Permissions f)'''
            return bool()
        def __invert__(self):
            '''QFileDevice.Permissions QFileDevice.Permissions.__invert__()'''
            return QFileDevice.Permissions()
        def __and__(self, mask):
            '''QFileDevice.Permissions QFileDevice.Permissions.__and__(int mask)'''
            return QFileDevice.Permissions()
        def __xor__(self, f):
            '''QFileDevice.Permissions QFileDevice.Permissions.__xor__(QFileDevice.Permissions f)'''
            return QFileDevice.Permissions()
        def __xor__(self, f):
            '''QFileDevice.Permissions QFileDevice.Permissions.__xor__(int f)'''
            return QFileDevice.Permissions()
        def __or__(self, f):
            '''QFileDevice.Permissions QFileDevice.Permissions.__or__(QFileDevice.Permissions f)'''
            return QFileDevice.Permissions()
        def __or__(self, f):
            '''QFileDevice.Permissions QFileDevice.Permissions.__or__(int f)'''
            return QFileDevice.Permissions()
        def __int__(self):
            '''int QFileDevice.Permissions.__int__()'''
            return int()
        def __ixor__(self, f):
            '''QFileDevice.Permissions QFileDevice.Permissions.__ixor__(QFileDevice.Permissions f)'''
            return QFileDevice.Permissions()
        def __ior__(self, f):
            '''QFileDevice.Permissions QFileDevice.Permissions.__ior__(QFileDevice.Permissions f)'''
            return QFileDevice.Permissions()
        def __iand__(self, mask):
            '''QFileDevice.Permissions QFileDevice.Permissions.__iand__(int mask)'''
            return QFileDevice.Permissions()


class QFile(QFileDevice):
    """"""
    def __init__(self):
        '''void QFile.__init__()'''
    def __init__(self, name):
        '''void QFile.__init__(str name)'''
    def __init__(self, parent):
        '''void QFile.__init__(QObject parent)'''
    def __init__(self, name, parent):
        '''void QFile.__init__(str name, QObject parent)'''
    def setPermissions(self, permissionSpec):
        '''bool QFile.setPermissions(QFileDevice.Permissions permissionSpec)'''
        return bool()
    def setPermissions(self, filename, permissionSpec):
        '''static bool QFile.setPermissions(str filename, QFileDevice.Permissions permissionSpec)'''
        return bool()
    def permissions(self):
        '''QFileDevice.Permissions QFile.permissions()'''
        return QFileDevice.Permissions()
    def permissions(self, filename):
        '''static QFileDevice.Permissions QFile.permissions(str filename)'''
        return QFileDevice.Permissions()
    def resize(self, sz):
        '''bool QFile.resize(int sz)'''
        return bool()
    def resize(self, filename, sz):
        '''static bool QFile.resize(str filename, int sz)'''
        return bool()
    def size(self):
        '''int QFile.size()'''
        return int()
    def open(self, flags):
        '''bool QFile.open(QIODevice.OpenMode flags)'''
        return bool()
    def open(self, fd, ioFlags, handleFlags = None):
        '''bool QFile.open(int fd, QIODevice.OpenMode ioFlags, QFileDevice.FileHandleFlags handleFlags = QFileDevice.DontCloseHandle)'''
        return bool()
    def copy(self, newName):
        '''bool QFile.copy(str newName)'''
        return bool()
    def copy(self, fileName, newName):
        '''static bool QFile.copy(str fileName, str newName)'''
        return bool()
    def link(self, newName):
        '''bool QFile.link(str newName)'''
        return bool()
    def link(self, oldname, newName):
        '''static bool QFile.link(str oldname, str newName)'''
        return bool()
    def rename(self, newName):
        '''bool QFile.rename(str newName)'''
        return bool()
    def rename(self, oldName, newName):
        '''static bool QFile.rename(str oldName, str newName)'''
        return bool()
    def remove(self):
        '''bool QFile.remove()'''
        return bool()
    def remove(self, fileName):
        '''static bool QFile.remove(str fileName)'''
        return bool()
    def symLinkTarget(self):
        '''str QFile.symLinkTarget()'''
        return str()
    def symLinkTarget(self, fileName):
        '''static str QFile.symLinkTarget(str fileName)'''
        return str()
    def exists(self):
        '''bool QFile.exists()'''
        return bool()
    def exists(self, fileName):
        '''static bool QFile.exists(str fileName)'''
        return bool()
    def decodeName(self, localFileName):
        '''static str QFile.decodeName(QByteArray localFileName)'''
        return str()
    def decodeName(self, localFileName):
        '''static str QFile.decodeName(str localFileName)'''
        return str()
    def encodeName(self, fileName):
        '''static QByteArray QFile.encodeName(str fileName)'''
        return QByteArray()
    def setFileName(self, name):
        '''void QFile.setFileName(str name)'''
    def fileName(self):
        '''str QFile.fileName()'''
        return str()


class QFileInfo():
    """"""
    def __init__(self):
        '''void QFileInfo.__init__()'''
    def __init__(self, file):
        '''void QFileInfo.__init__(str file)'''
    def __init__(self, file):
        '''void QFileInfo.__init__(QFile file)'''
    def __init__(self, dir, file):
        '''void QFileInfo.__init__(QDir dir, str file)'''
    def __init__(self, fileinfo):
        '''void QFileInfo.__init__(QFileInfo fileinfo)'''
    def swap(self, other):
        '''void QFileInfo.swap(QFileInfo other)'''
    def isNativePath(self):
        '''bool QFileInfo.isNativePath()'''
        return bool()
    def isBundle(self):
        '''bool QFileInfo.isBundle()'''
        return bool()
    def bundleName(self):
        '''str QFileInfo.bundleName()'''
        return str()
    def symLinkTarget(self):
        '''str QFileInfo.symLinkTarget()'''
        return str()
    def setCaching(self, on):
        '''void QFileInfo.setCaching(bool on)'''
    def caching(self):
        '''bool QFileInfo.caching()'''
        return bool()
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
        '''QFileDevice.Permissions QFileInfo.permissions()'''
        return QFileDevice.Permissions()
    def permission(self, permissions):
        '''bool QFileInfo.permission(QFileDevice.Permissions permissions)'''
        return bool()
    def groupId(self):
        '''int QFileInfo.groupId()'''
        return int()
    def group(self):
        '''str QFileInfo.group()'''
        return str()
    def ownerId(self):
        '''int QFileInfo.ownerId()'''
        return int()
    def owner(self):
        '''str QFileInfo.owner()'''
        return str()
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
        '''str QFileInfo.canonicalPath()'''
        return str()
    def absolutePath(self):
        '''str QFileInfo.absolutePath()'''
        return str()
    def path(self):
        '''str QFileInfo.path()'''
        return str()
    def completeSuffix(self):
        '''str QFileInfo.completeSuffix()'''
        return str()
    def suffix(self):
        '''str QFileInfo.suffix()'''
        return str()
    def completeBaseName(self):
        '''str QFileInfo.completeBaseName()'''
        return str()
    def baseName(self):
        '''str QFileInfo.baseName()'''
        return str()
    def fileName(self):
        '''str QFileInfo.fileName()'''
        return str()
    def canonicalFilePath(self):
        '''str QFileInfo.canonicalFilePath()'''
        return str()
    def absoluteFilePath(self):
        '''str QFileInfo.absoluteFilePath()'''
        return str()
    def filePath(self):
        '''str QFileInfo.filePath()'''
        return str()
    def refresh(self):
        '''void QFileInfo.refresh()'''
    def exists(self):
        '''bool QFileInfo.exists()'''
        return bool()
    def exists(self, file):
        '''static bool QFileInfo.exists(str file)'''
        return bool()
    def setFile(self, file):
        '''void QFileInfo.setFile(str file)'''
    def setFile(self, file):
        '''void QFileInfo.setFile(QFile file)'''
    def setFile(self, dir, file):
        '''void QFileInfo.setFile(QDir dir, str file)'''
    def __ne__(self, fileinfo):
        '''bool QFileInfo.__ne__(QFileInfo fileinfo)'''
        return bool()
    def __eq__(self, fileinfo):
        '''bool QFileInfo.__eq__(QFileInfo fileinfo)'''
        return bool()


class QFileSelector(QObject):
    """"""
    def __init__(self, parent = None):
        '''void QFileSelector.__init__(QObject parent = None)'''
    def allSelectors(self):
        '''list-of-str QFileSelector.allSelectors()'''
        return [str()]
    def setExtraSelectors(self, list):
        '''void QFileSelector.setExtraSelectors(list-of-str list)'''
    def extraSelectors(self):
        '''list-of-str QFileSelector.extraSelectors()'''
        return [str()]
    def select(self, filePath):
        '''str QFileSelector.select(str filePath)'''
        return str()
    def select(self, filePath):
        '''QUrl QFileSelector.select(QUrl filePath)'''
        return QUrl()


class QFileSystemWatcher(QObject):
    """"""
    def __init__(self, parent = None):
        '''void QFileSystemWatcher.__init__(QObject parent = None)'''
    def __init__(self, paths, parent = None):
        '''void QFileSystemWatcher.__init__(list-of-str paths, QObject parent = None)'''
    fileChanged = pyqtSignal() # void fileChanged(const QStringamp;) - signal
    directoryChanged = pyqtSignal() # void directoryChanged(const QStringamp;) - signal
    def removePaths(self, files):
        '''list-of-str QFileSystemWatcher.removePaths(list-of-str files)'''
        return [str()]
    def removePath(self, file):
        '''bool QFileSystemWatcher.removePath(str file)'''
        return bool()
    def files(self):
        '''list-of-str QFileSystemWatcher.files()'''
        return [str()]
    def directories(self):
        '''list-of-str QFileSystemWatcher.directories()'''
        return [str()]
    def addPaths(self, files):
        '''list-of-str QFileSystemWatcher.addPaths(list-of-str files)'''
        return [str()]
    def addPath(self, file):
        '''bool QFileSystemWatcher.addPath(str file)'''
        return bool()


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


class QHistoryState(QAbstractState):
    """"""
    # Enum QHistoryState.HistoryType
    ShallowHistory = 0
    DeepHistory = 0

    def __init__(self, parent = None):
        '''void QHistoryState.__init__(QState parent = None)'''
    def __init__(self, type, parent = None):
        '''void QHistoryState.__init__(QHistoryState.HistoryType type, QState parent = None)'''
    historyTypeChanged = pyqtSignal() # void historyTypeChanged() - signal
    defaultStateChanged = pyqtSignal() # void defaultStateChanged() - signal
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


class QIdentityProxyModel(QAbstractProxyModel):
    """"""
    def __init__(self, parent = None):
        '''void QIdentityProxyModel.__init__(QObject parent = None)'''
    def sibling(self, row, column, idx):
        '''QModelIndex QIdentityProxyModel.sibling(int row, int column, QModelIndex idx)'''
        return QModelIndex()
    def headerData(self, section, orientation, role = None):
        '''QVariant QIdentityProxyModel.headerData(int section, Qt.Orientation orientation, int role = Qt.DisplayRole)'''
        return QVariant()
    def removeRows(self, row, count, parent = QModelIndex()):
        '''bool QIdentityProxyModel.removeRows(int row, int count, QModelIndex parent = QModelIndex())'''
        return bool()
    def removeColumns(self, column, count, parent = QModelIndex()):
        '''bool QIdentityProxyModel.removeColumns(int column, int count, QModelIndex parent = QModelIndex())'''
        return bool()
    def insertRows(self, row, count, parent = QModelIndex()):
        '''bool QIdentityProxyModel.insertRows(int row, int count, QModelIndex parent = QModelIndex())'''
        return bool()
    def insertColumns(self, column, count, parent = QModelIndex()):
        '''bool QIdentityProxyModel.insertColumns(int column, int count, QModelIndex parent = QModelIndex())'''
        return bool()
    def setSourceModel(self, sourceModel):
        '''void QIdentityProxyModel.setSourceModel(QAbstractItemModel sourceModel)'''
    def match(self, start, role, value, hits = 1, flags = None):
        '''list-of-QModelIndex QIdentityProxyModel.match(QModelIndex start, int role, QVariant value, int hits = 1, Qt.MatchFlags flags = Qt.MatchStartsWith|Qt.MatchWrap)'''
        return [QModelIndex()]
    def mapSelectionToSource(self, selection):
        '''QItemSelection QIdentityProxyModel.mapSelectionToSource(QItemSelection selection)'''
        return QItemSelection()
    def mapSelectionFromSource(self, selection):
        '''QItemSelection QIdentityProxyModel.mapSelectionFromSource(QItemSelection selection)'''
        return QItemSelection()
    def dropMimeData(self, data, action, row, column, parent):
        '''bool QIdentityProxyModel.dropMimeData(QMimeData data, Qt.DropAction action, int row, int column, QModelIndex parent)'''
        return bool()
    def rowCount(self, parent = QModelIndex()):
        '''int QIdentityProxyModel.rowCount(QModelIndex parent = QModelIndex())'''
        return int()
    def parent(self, child):
        '''QModelIndex QIdentityProxyModel.parent(QModelIndex child)'''
        return QModelIndex()
    def mapToSource(self, proxyIndex):
        '''QModelIndex QIdentityProxyModel.mapToSource(QModelIndex proxyIndex)'''
        return QModelIndex()
    def mapFromSource(self, sourceIndex):
        '''QModelIndex QIdentityProxyModel.mapFromSource(QModelIndex sourceIndex)'''
        return QModelIndex()
    def index(self, row, column, parent = QModelIndex()):
        '''QModelIndex QIdentityProxyModel.index(int row, int column, QModelIndex parent = QModelIndex())'''
        return QModelIndex()
    def columnCount(self, parent = QModelIndex()):
        '''int QIdentityProxyModel.columnCount(QModelIndex parent = QModelIndex())'''
        return int()


class QItemSelectionRange():
    """"""
    def __init__(self):
        '''void QItemSelectionRange.__init__()'''
    def __init__(self, other):
        '''void QItemSelectionRange.__init__(QItemSelectionRange other)'''
    def __init__(self, atopLeft, abottomRight):
        '''void QItemSelectionRange.__init__(QModelIndex atopLeft, QModelIndex abottomRight)'''
    def __init__(self, index):
        '''void QItemSelectionRange.__init__(QModelIndex index)'''
    def __ge__(self, other):
        '''bool QItemSelectionRange.__ge__(QItemSelectionRange other)'''
        return bool()
    def __lt__(self, other):
        '''bool QItemSelectionRange.__lt__(QItemSelectionRange other)'''
        return bool()
    def isEmpty(self):
        '''bool QItemSelectionRange.isEmpty()'''
        return bool()
    def __hash__(self):
        '''int QItemSelectionRange.__hash__()'''
        return int()
    def intersected(self, other):
        '''QItemSelectionRange QItemSelectionRange.intersected(QItemSelectionRange other)'''
        return QItemSelectionRange()
    def indexes(self):
        '''list-of-QModelIndex QItemSelectionRange.indexes()'''
        return [QModelIndex()]
    def isValid(self):
        '''bool QItemSelectionRange.isValid()'''
        return bool()
    def __ne__(self, other):
        '''bool QItemSelectionRange.__ne__(QItemSelectionRange other)'''
        return bool()
    def __eq__(self, other):
        '''bool QItemSelectionRange.__eq__(QItemSelectionRange other)'''
        return bool()
    def intersects(self, other):
        '''bool QItemSelectionRange.intersects(QItemSelectionRange other)'''
        return bool()
    def contains(self, index):
        '''bool QItemSelectionRange.contains(QModelIndex index)'''
        return bool()
    def contains(self, row, column, parentIndex):
        '''bool QItemSelectionRange.contains(int row, int column, QModelIndex parentIndex)'''
        return bool()
    def model(self):
        '''QAbstractItemModel QItemSelectionRange.model()'''
        return QAbstractItemModel()
    def parent(self):
        '''QModelIndex QItemSelectionRange.parent()'''
        return QModelIndex()
    def bottomRight(self):
        '''QPersistentModelIndex QItemSelectionRange.bottomRight()'''
        return QPersistentModelIndex()
    def topLeft(self):
        '''QPersistentModelIndex QItemSelectionRange.topLeft()'''
        return QPersistentModelIndex()
    def height(self):
        '''int QItemSelectionRange.height()'''
        return int()
    def width(self):
        '''int QItemSelectionRange.width()'''
        return int()
    def right(self):
        '''int QItemSelectionRange.right()'''
        return int()
    def bottom(self):
        '''int QItemSelectionRange.bottom()'''
        return int()
    def left(self):
        '''int QItemSelectionRange.left()'''
        return int()
    def top(self):
        '''int QItemSelectionRange.top()'''
        return int()


class QItemSelectionModel(QObject):
    """"""
    # Enum QItemSelectionModel.SelectionFlag
    NoUpdate = 0
    Clear = 0
    Select = 0
    Deselect = 0
    Toggle = 0
    Current = 0
    Rows = 0
    Columns = 0
    SelectCurrent = 0
    ToggleCurrent = 0
    ClearAndSelect = 0

    def __init__(self, model = None):
        '''void QItemSelectionModel.__init__(QAbstractItemModel model = None)'''
    def __init__(self, model, parent):
        '''void QItemSelectionModel.__init__(QAbstractItemModel model, QObject parent)'''
    modelChanged = pyqtSignal() # void modelChanged(QAbstractItemModel*) - signal
    def setModel(self, model):
        '''void QItemSelectionModel.setModel(QAbstractItemModel model)'''
    def selectedColumns(self, row = 0):
        '''list-of-QModelIndex QItemSelectionModel.selectedColumns(int row = 0)'''
        return [QModelIndex()]
    def selectedRows(self, column = 0):
        '''list-of-QModelIndex QItemSelectionModel.selectedRows(int column = 0)'''
        return [QModelIndex()]
    def hasSelection(self):
        '''bool QItemSelectionModel.hasSelection()'''
        return bool()
    def emitSelectionChanged(self, newSelection, oldSelection):
        '''void QItemSelectionModel.emitSelectionChanged(QItemSelection newSelection, QItemSelection oldSelection)'''
    currentColumnChanged = pyqtSignal() # void currentColumnChanged(const QModelIndexamp;,const QModelIndexamp;) - signal
    currentRowChanged = pyqtSignal() # void currentRowChanged(const QModelIndexamp;,const QModelIndexamp;) - signal
    currentChanged = pyqtSignal() # void currentChanged(const QModelIndexamp;,const QModelIndexamp;) - signal
    selectionChanged = pyqtSignal() # void selectionChanged(const QItemSelectionamp;,const QItemSelectionamp;) - signal
    def clearCurrentIndex(self):
        '''void QItemSelectionModel.clearCurrentIndex()'''
    def setCurrentIndex(self, index, command):
        '''void QItemSelectionModel.setCurrentIndex(QModelIndex index, QItemSelectionModel.SelectionFlags command)'''
    def select(self, index, command):
        '''void QItemSelectionModel.select(QModelIndex index, QItemSelectionModel.SelectionFlags command)'''
    def select(self, selection, command):
        '''void QItemSelectionModel.select(QItemSelection selection, QItemSelectionModel.SelectionFlags command)'''
    def reset(self):
        '''void QItemSelectionModel.reset()'''
    def clearSelection(self):
        '''void QItemSelectionModel.clearSelection()'''
    def clear(self):
        '''void QItemSelectionModel.clear()'''
    def model(self):
        '''QAbstractItemModel QItemSelectionModel.model()'''
        return QAbstractItemModel()
    def selection(self):
        '''QItemSelection QItemSelectionModel.selection()'''
        return QItemSelection()
    def selectedIndexes(self):
        '''list-of-QModelIndex QItemSelectionModel.selectedIndexes()'''
        return [QModelIndex()]
    def columnIntersectsSelection(self, column, parent):
        '''bool QItemSelectionModel.columnIntersectsSelection(int column, QModelIndex parent)'''
        return bool()
    def rowIntersectsSelection(self, row, parent):
        '''bool QItemSelectionModel.rowIntersectsSelection(int row, QModelIndex parent)'''
        return bool()
    def isColumnSelected(self, column, parent):
        '''bool QItemSelectionModel.isColumnSelected(int column, QModelIndex parent)'''
        return bool()
    def isRowSelected(self, row, parent):
        '''bool QItemSelectionModel.isRowSelected(int row, QModelIndex parent)'''
        return bool()
    def isSelected(self, index):
        '''bool QItemSelectionModel.isSelected(QModelIndex index)'''
        return bool()
    def currentIndex(self):
        '''QModelIndex QItemSelectionModel.currentIndex()'''
        return QModelIndex()
    class SelectionFlags():
        """"""
        def __init__(self):
            '''QItemSelectionModel.SelectionFlags QItemSelectionModel.SelectionFlags.__init__()'''
            return QItemSelectionModel.SelectionFlags()
        def __init__(self):
            '''int QItemSelectionModel.SelectionFlags.__init__()'''
            return int()
        def __init__(self):
            '''void QItemSelectionModel.SelectionFlags.__init__()'''
        def __bool__(self):
            '''int QItemSelectionModel.SelectionFlags.__bool__()'''
            return int()
        def __ne__(self, f):
            '''bool QItemSelectionModel.SelectionFlags.__ne__(QItemSelectionModel.SelectionFlags f)'''
            return bool()
        def __eq__(self, f):
            '''bool QItemSelectionModel.SelectionFlags.__eq__(QItemSelectionModel.SelectionFlags f)'''
            return bool()
        def __invert__(self):
            '''QItemSelectionModel.SelectionFlags QItemSelectionModel.SelectionFlags.__invert__()'''
            return QItemSelectionModel.SelectionFlags()
        def __and__(self, mask):
            '''QItemSelectionModel.SelectionFlags QItemSelectionModel.SelectionFlags.__and__(int mask)'''
            return QItemSelectionModel.SelectionFlags()
        def __xor__(self, f):
            '''QItemSelectionModel.SelectionFlags QItemSelectionModel.SelectionFlags.__xor__(QItemSelectionModel.SelectionFlags f)'''
            return QItemSelectionModel.SelectionFlags()
        def __xor__(self, f):
            '''QItemSelectionModel.SelectionFlags QItemSelectionModel.SelectionFlags.__xor__(int f)'''
            return QItemSelectionModel.SelectionFlags()
        def __or__(self, f):
            '''QItemSelectionModel.SelectionFlags QItemSelectionModel.SelectionFlags.__or__(QItemSelectionModel.SelectionFlags f)'''
            return QItemSelectionModel.SelectionFlags()
        def __or__(self, f):
            '''QItemSelectionModel.SelectionFlags QItemSelectionModel.SelectionFlags.__or__(int f)'''
            return QItemSelectionModel.SelectionFlags()
        def __int__(self):
            '''int QItemSelectionModel.SelectionFlags.__int__()'''
            return int()
        def __ixor__(self, f):
            '''QItemSelectionModel.SelectionFlags QItemSelectionModel.SelectionFlags.__ixor__(QItemSelectionModel.SelectionFlags f)'''
            return QItemSelectionModel.SelectionFlags()
        def __ior__(self, f):
            '''QItemSelectionModel.SelectionFlags QItemSelectionModel.SelectionFlags.__ior__(QItemSelectionModel.SelectionFlags f)'''
            return QItemSelectionModel.SelectionFlags()
        def __iand__(self, mask):
            '''QItemSelectionModel.SelectionFlags QItemSelectionModel.SelectionFlags.__iand__(int mask)'''
            return QItemSelectionModel.SelectionFlags()


class QItemSelection():
    """"""
    def __init__(self):
        '''void QItemSelection.__init__()'''
    def __init__(self, topLeft, bottomRight):
        '''void QItemSelection.__init__(QModelIndex topLeft, QModelIndex bottomRight)'''
    def __init__(self):
        '''QItemSelection QItemSelection.__init__()'''
        return QItemSelection()
    def __iadd__(self, other):
        '''QItemSelection QItemSelection.__iadd__(QItemSelection other)'''
        return QItemSelection()
    def __iadd__(self, value):
        '''QItemSelection QItemSelection.__iadd__(QItemSelectionRange value)'''
        return QItemSelection()
    def lastIndexOf(self, value, from_ = None):
        '''int QItemSelection.lastIndexOf(QItemSelectionRange value, int from = -1)'''
        return int()
    def indexOf(self, value, from_ = 0):
        '''int QItemSelection.indexOf(QItemSelectionRange value, int from = 0)'''
        return int()
    def last(self):
        '''QItemSelectionRange QItemSelection.last()'''
        return QItemSelectionRange()
    def first(self):
        '''QItemSelectionRange QItemSelection.first()'''
        return QItemSelectionRange()
    def __len__(self):
        ''' QItemSelection.__len__()'''
        return ()
    def count(self, range):
        '''int QItemSelection.count(QItemSelectionRange range)'''
        return int()
    def count(self):
        '''int QItemSelection.count()'''
        return int()
    def swap(self, i, j):
        '''void QItemSelection.swap(int i, int j)'''
    def move(self, from_, to):
        '''void QItemSelection.move(int from, int to)'''
    def takeLast(self):
        '''QItemSelectionRange QItemSelection.takeLast()'''
        return QItemSelectionRange()
    def takeFirst(self):
        '''QItemSelectionRange QItemSelection.takeFirst()'''
        return QItemSelectionRange()
    def takeAt(self, i):
        '''QItemSelectionRange QItemSelection.takeAt(int i)'''
        return QItemSelectionRange()
    def removeAll(self, range):
        '''int QItemSelection.removeAll(QItemSelectionRange range)'''
        return int()
    def removeAt(self, i):
        '''void QItemSelection.removeAt(int i)'''
    def replace(self, i, range):
        '''void QItemSelection.replace(int i, QItemSelectionRange range)'''
    def insert(self, i, range):
        '''void QItemSelection.insert(int i, QItemSelectionRange range)'''
    def prepend(self, range):
        '''void QItemSelection.prepend(QItemSelectionRange range)'''
    def append(self, range):
        '''void QItemSelection.append(QItemSelectionRange range)'''
    def isEmpty(self):
        '''bool QItemSelection.isEmpty()'''
        return bool()
    def clear(self):
        '''void QItemSelection.clear()'''
    def __eq__(self, other):
        '''bool QItemSelection.__eq__(QItemSelection other)'''
        return bool()
    def __ne__(self, other):
        '''bool QItemSelection.__ne__(QItemSelection other)'''
        return bool()
    def __getitem__(self, i):
        '''QItemSelectionRange QItemSelection.__getitem__(int i)'''
        return QItemSelectionRange()
    def __getitem__(self, slice):
        '''QItemSelection QItemSelection.__getitem__(slice slice)'''
        return QItemSelection()
    def __delitem__(self, i):
        '''void QItemSelection.__delitem__(int i)'''
    def __delitem__(self, slice):
        '''void QItemSelection.__delitem__(slice slice)'''
    def __setitem__(self, i, range):
        '''void QItemSelection.__setitem__(int i, QItemSelectionRange range)'''
    def __setitem__(self, slice, list):
        '''void QItemSelection.__setitem__(slice slice, QItemSelection list)'''
    def split(self, range, other, result):
        '''static void QItemSelection.split(QItemSelectionRange range, QItemSelectionRange other, QItemSelection result)'''
    def merge(self, other, command):
        '''void QItemSelection.merge(QItemSelection other, QItemSelectionModel.SelectionFlags command)'''
    def indexes(self):
        '''list-of-QModelIndex QItemSelection.indexes()'''
        return [QModelIndex()]
    def __contains__(self, index):
        '''int QItemSelection.__contains__(QModelIndex index)'''
        return int()
    def contains(self, index):
        '''bool QItemSelection.contains(QModelIndex index)'''
        return bool()
    def select(self, topLeft, bottomRight):
        '''void QItemSelection.select(QModelIndex topLeft, QModelIndex bottomRight)'''


class QJsonParseError():
    """"""
    # Enum QJsonParseError.ParseError
    NoError = 0
    UnterminatedObject = 0
    MissingNameSeparator = 0
    UnterminatedArray = 0
    MissingValueSeparator = 0
    IllegalValue = 0
    TerminationByNumber = 0
    IllegalNumber = 0
    IllegalEscapeSequence = 0
    IllegalUTF8String = 0
    UnterminatedString = 0
    MissingObject = 0
    DeepNesting = 0
    DocumentTooLarge = 0
    GarbageAtEnd = 0

    error = None # QJsonParseError.ParseError - member
    offset = None # int - member
    def __init__(self):
        '''void QJsonParseError.__init__()'''
    def __init__(self):
        '''QJsonParseError QJsonParseError.__init__()'''
        return QJsonParseError()
    def errorString(self):
        '''str QJsonParseError.errorString()'''
        return str()


class QJsonDocument():
    """"""
    # Enum QJsonDocument.JsonFormat
    Indented = 0
    Compact = 0

    # Enum QJsonDocument.DataValidation
    Validate = 0
    BypassValidation = 0

    def __init__(self):
        '''void QJsonDocument.__init__()'''
    def __init__(self, object):
        '''void QJsonDocument.__init__(dict-of-str-QJsonValue object)'''
    def __init__(self, array):
        '''void QJsonDocument.__init__(list-of-QJsonValue array)'''
    def __init__(self, other):
        '''void QJsonDocument.__init__(QJsonDocument other)'''
    def isNull(self):
        '''bool QJsonDocument.isNull()'''
        return bool()
    def __ne__(self, other):
        '''bool QJsonDocument.__ne__(QJsonDocument other)'''
        return bool()
    def __eq__(self, other):
        '''bool QJsonDocument.__eq__(QJsonDocument other)'''
        return bool()
    def setArray(self, array):
        '''void QJsonDocument.setArray(list-of-QJsonValue array)'''
    def setObject(self, object):
        '''void QJsonDocument.setObject(dict-of-str-QJsonValue object)'''
    def array(self):
        '''list-of-QJsonValue QJsonDocument.array()'''
        return [QJsonValue()]
    def object(self):
        '''dict-of-str-QJsonValue QJsonDocument.object()'''
        return {str():QJsonValue()}
    def isObject(self):
        '''bool QJsonDocument.isObject()'''
        return bool()
    def isArray(self):
        '''bool QJsonDocument.isArray()'''
        return bool()
    def isEmpty(self):
        '''bool QJsonDocument.isEmpty()'''
        return bool()
    def toJson(self):
        '''QByteArray QJsonDocument.toJson()'''
        return QByteArray()
    def toJson(self, format):
        '''QByteArray QJsonDocument.toJson(QJsonDocument.JsonFormat format)'''
        return QByteArray()
    def fromJson(self, json, error = None):
        '''static QJsonDocument QJsonDocument.fromJson(QByteArray json, QJsonParseError error = None)'''
        return QJsonDocument()
    def toVariant(self):
        '''QVariant QJsonDocument.toVariant()'''
        return QVariant()
    def fromVariant(self, variant):
        '''static QJsonDocument QJsonDocument.fromVariant(QVariant variant)'''
        return QJsonDocument()
    def toBinaryData(self):
        '''QByteArray QJsonDocument.toBinaryData()'''
        return QByteArray()
    def fromBinaryData(self, data, validation = None):
        '''static QJsonDocument QJsonDocument.fromBinaryData(QByteArray data, QJsonDocument.DataValidation validation = QJsonDocument.Validate)'''
        return QJsonDocument()
    def rawData(self, size):
        '''str QJsonDocument.rawData(int size)'''
        return str()
    def fromRawData(self, data, size, validation = None):
        '''static QJsonDocument QJsonDocument.fromRawData(str data, int size, QJsonDocument.DataValidation validation = QJsonDocument.Validate)'''
        return QJsonDocument()


class QJsonValue():
    """"""
    # Enum QJsonValue.Type
    Null = 0
    Bool = 0
    Double = 0
    String = 0
    Array = 0
    Object = 0
    Undefined = 0

    def __init__(self, type = None):
        '''void QJsonValue.__init__(QJsonValue.Type type = QJsonValue.Null)'''
    def __init__(self, other):
        '''void QJsonValue.__init__(QJsonValue other)'''
    def __ne__(self, other):
        '''bool QJsonValue.__ne__(QJsonValue other)'''
        return bool()
    def __eq__(self, other):
        '''bool QJsonValue.__eq__(QJsonValue other)'''
        return bool()
    def toObject(self):
        '''dict-of-str-QJsonValue QJsonValue.toObject()'''
        return {str():QJsonValue()}
    def toObject(self, defaultValue):
        '''dict-of-str-QJsonValue QJsonValue.toObject(dict-of-str-QJsonValue defaultValue)'''
        return {str():QJsonValue()}
    def toArray(self):
        '''list-of-QJsonValue QJsonValue.toArray()'''
        return [QJsonValue()]
    def toArray(self, defaultValue):
        '''list-of-QJsonValue QJsonValue.toArray(list-of-QJsonValue defaultValue)'''
        return [QJsonValue()]
    def toString(self, defaultValue = str()):
        '''str QJsonValue.toString(str defaultValue = str())'''
        return str()
    def toDouble(self, defaultValue = 0):
        '''float QJsonValue.toDouble(float defaultValue = 0)'''
        return float()
    def toInt(self, defaultValue = 0):
        '''int QJsonValue.toInt(int defaultValue = 0)'''
        return int()
    def toBool(self, defaultValue = False):
        '''bool QJsonValue.toBool(bool defaultValue = False)'''
        return bool()
    def isUndefined(self):
        '''bool QJsonValue.isUndefined()'''
        return bool()
    def isObject(self):
        '''bool QJsonValue.isObject()'''
        return bool()
    def isArray(self):
        '''bool QJsonValue.isArray()'''
        return bool()
    def isString(self):
        '''bool QJsonValue.isString()'''
        return bool()
    def isDouble(self):
        '''bool QJsonValue.isDouble()'''
        return bool()
    def isBool(self):
        '''bool QJsonValue.isBool()'''
        return bool()
    def isNull(self):
        '''bool QJsonValue.isNull()'''
        return bool()
    def type(self):
        '''QJsonValue.Type QJsonValue.type()'''
        return QJsonValue.Type()
    def toVariant(self):
        '''QVariant QJsonValue.toVariant()'''
        return QVariant()
    def fromVariant(self, variant):
        '''static QJsonValue QJsonValue.fromVariant(QVariant variant)'''
        return QJsonValue()


class QLibrary(QObject):
    """"""
    # Enum QLibrary.LoadHint
    ResolveAllSymbolsHint = 0
    ExportExternalSymbolsHint = 0
    LoadArchiveMemberHint = 0
    PreventUnloadHint = 0
    DeepBindHint = 0

    def __init__(self, parent = None):
        '''void QLibrary.__init__(QObject parent = None)'''
    def __init__(self, fileName, parent = None):
        '''void QLibrary.__init__(str fileName, QObject parent = None)'''
    def __init__(self, fileName, verNum, parent = None):
        '''void QLibrary.__init__(str fileName, int verNum, QObject parent = None)'''
    def __init__(self, fileName, version, parent = None):
        '''void QLibrary.__init__(str fileName, str version, QObject parent = None)'''
    def setLoadHints(self, hints):
        '''void QLibrary.setLoadHints(QLibrary.LoadHints hints)'''
    def setFileNameAndVersion(self, fileName, verNum):
        '''void QLibrary.setFileNameAndVersion(str fileName, int verNum)'''
    def setFileNameAndVersion(self, fileName, version):
        '''void QLibrary.setFileNameAndVersion(str fileName, str version)'''
    def setFileName(self, fileName):
        '''void QLibrary.setFileName(str fileName)'''
    def isLibrary(self, fileName):
        '''static bool QLibrary.isLibrary(str fileName)'''
        return bool()
    def unload(self):
        '''bool QLibrary.unload()'''
        return bool()
    def resolve(self, symbol):
        '''sip.voidptr QLibrary.resolve(str symbol)'''
        return sip.voidptr()
    def resolve(self, fileName, symbol):
        '''static sip.voidptr QLibrary.resolve(str fileName, str symbol)'''
        return sip.voidptr()
    def resolve(self, fileName, verNum, symbol):
        '''static sip.voidptr QLibrary.resolve(str fileName, int verNum, str symbol)'''
        return sip.voidptr()
    def resolve(self, fileName, version, symbol):
        '''static sip.voidptr QLibrary.resolve(str fileName, str version, str symbol)'''
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
        '''str QLibrary.fileName()'''
        return str()
    def errorString(self):
        '''str QLibrary.errorString()'''
        return str()
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
    ExamplesPath = 0
    ImportsPath = 0
    TestsPath = 0
    LibraryExecutablesPath = 0
    Qml2ImportsPath = 0
    ArchDataPath = 0

    def __init__(self):
        '''QLibraryInfo QLibraryInfo.__init__()'''
        return QLibraryInfo()
    def isDebugBuild(self):
        '''static bool QLibraryInfo.isDebugBuild()'''
        return bool()
    def buildDate(self):
        '''static QDate QLibraryInfo.buildDate()'''
        return QDate()
    def location(self):
        '''static QLibraryInfo.LibraryLocation QLibraryInfo.location()'''
        return QLibraryInfo.LibraryLocation()
    def licensedProducts(self):
        '''static str QLibraryInfo.licensedProducts()'''
        return str()
    def licensee(self):
        '''static str QLibraryInfo.licensee()'''
        return str()


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
    def angle(self):
        '''float QLineF.angle()'''
        return float()
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
    ArmenianScript = 0
    BengaliScript = 0
    CherokeeScript = 0
    DevanagariScript = 0
    EthiopicScript = 0
    GeorgianScript = 0
    GreekScript = 0
    GujaratiScript = 0
    HebrewScript = 0
    JapaneseScript = 0
    KhmerScript = 0
    KannadaScript = 0
    KoreanScript = 0
    LaoScript = 0
    MalayalamScript = 0
    MyanmarScript = 0
    OriyaScript = 0
    TamilScript = 0
    TeluguScript = 0
    ThaanaScript = 0
    ThaiScript = 0
    TibetanScript = 0
    SinhalaScript = 0
    SyriacScript = 0
    YiScript = 0
    VaiScript = 0
    AvestanScript = 0
    BalineseScript = 0
    BamumScript = 0
    BatakScript = 0
    BopomofoScript = 0
    BrahmiScript = 0
    BugineseScript = 0
    BuhidScript = 0
    CanadianAboriginalScript = 0
    CarianScript = 0
    ChakmaScript = 0
    ChamScript = 0
    CopticScript = 0
    CypriotScript = 0
    EgyptianHieroglyphsScript = 0
    FraserScript = 0
    GlagoliticScript = 0
    GothicScript = 0
    HanScript = 0
    HangulScript = 0
    HanunooScript = 0
    ImperialAramaicScript = 0
    InscriptionalPahlaviScript = 0
    InscriptionalParthianScript = 0
    JavaneseScript = 0
    KaithiScript = 0
    KatakanaScript = 0
    KayahLiScript = 0
    KharoshthiScript = 0
    LannaScript = 0
    LepchaScript = 0
    LimbuScript = 0
    LinearBScript = 0
    LycianScript = 0
    LydianScript = 0
    MandaeanScript = 0
    MeiteiMayekScript = 0
    MeroiticScript = 0
    MeroiticCursiveScript = 0
    NkoScript = 0
    NewTaiLueScript = 0
    OghamScript = 0
    OlChikiScript = 0
    OldItalicScript = 0
    OldPersianScript = 0
    OldSouthArabianScript = 0
    OrkhonScript = 0
    OsmanyaScript = 0
    PhagsPaScript = 0
    PhoenicianScript = 0
    PollardPhoneticScript = 0
    RejangScript = 0
    RunicScript = 0
    SamaritanScript = 0
    SaurashtraScript = 0
    SharadaScript = 0
    ShavianScript = 0
    SoraSompengScript = 0
    CuneiformScript = 0
    SundaneseScript = 0
    SylotiNagriScript = 0
    TagalogScript = 0
    TagbanwaScript = 0
    TaiLeScript = 0
    TaiVietScript = 0
    TakriScript = 0
    UgariticScript = 0
    BrailleScript = 0
    HiraganaScript = 0
    CaucasianAlbanianScript = 0
    BassaVahScript = 0
    DuployanScript = 0
    ElbasanScript = 0
    GranthaScript = 0
    PahawhHmongScript = 0
    KhojkiScript = 0
    LinearAScript = 0
    MahajaniScript = 0
    ManichaeanScript = 0
    MendeKikakuiScript = 0
    ModiScript = 0
    MroScript = 0
    OldNorthArabianScript = 0
    NabataeanScript = 0
    PalmyreneScript = 0
    PauCinHauScript = 0
    OldPermicScript = 0
    PsalterPahlaviScript = 0
    SiddhamScript = 0
    KhudawadiScript = 0
    TirhutaScript = 0
    VarangKshitiScript = 0

    # Enum QLocale.MeasurementSystem
    MetricSystem = 0
    ImperialSystem = 0
    ImperialUSSystem = 0
    ImperialUKSystem = 0

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
    Finland = 0
    France = 0
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
    Latvia = 0
    Lebanon = 0
    Lesotho = 0
    Liberia = 0
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
    BritishVirginIslands = 0
    WallisAndFutunaIslands = 0
    WesternSahara = 0
    Yemen = 0
    Zambia = 0
    Zimbabwe = 0
    Montenegro = 0
    Serbia = 0
    SaintBarthelemy = 0
    SaintMartin = 0
    LatinAmericaAndTheCaribbean = 0
    LastCountry = 0
    Brunei = 0
    CongoKinshasa = 0
    CongoBrazzaville = 0
    Fiji = 0
    Guernsey = 0
    NorthKorea = 0
    SouthKorea = 0
    Laos = 0
    Libya = 0
    CuraSao = 0
    PalestinianTerritories = 0
    Russia = 0
    SaintLucia = 0
    SaintVincentAndTheGrenadines = 0
    SaintHelena = 0
    SaintPierreAndMiquelon = 0
    Syria = 0
    Tonga = 0
    Vietnam = 0
    UnitedStatesVirginIslands = 0
    CanaryIslands = 0
    ClippertonIsland = 0
    AscensionIsland = 0
    AlandIslands = 0
    DiegoGarcia = 0
    CeutaAndMelilla = 0
    IsleOfMan = 0
    Jersey = 0
    TristanDaCunha = 0
    SouthSudan = 0
    Bonaire = 0
    SintMaarten = 0
    Kosovo = 0

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
    Sanskrit = 0
    Serbian = 0
    SerboCroatian = 0
    Shona = 0
    Sindhi = 0
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
    Rundi = 0
    Bodo = 0
    Aghem = 0
    Basaa = 0
    Zarma = 0
    Duala = 0
    JolaFonyi = 0
    Ewondo = 0
    Bafia = 0
    LubaKatanga = 0
    MakhuwaMeetto = 0
    Mundang = 0
    Kwasio = 0
    Nuer = 0
    Sakha = 0
    Sangu = 0
    CongoSwahili = 0
    Tasawaq = 0
    Vai = 0
    Walser = 0
    Yangben = 0
    Oromo = 0
    Dzongkha = 0
    Belarusian = 0
    Khmer = 0
    Fijian = 0
    WesternFrisian = 0
    Lao = 0
    Marshallese = 0
    Romansh = 0
    Sango = 0
    Ossetic = 0
    SouthernSotho = 0
    Tswana = 0
    Sinhala = 0
    Swati = 0
    Sardinian = 0
    Tongan = 0
    Tahitian = 0
    Nyanja = 0
    Avaric = 0
    Chamorro = 0
    Chechen = 0
    Church = 0
    Chuvash = 0
    Cree = 0
    Haitian = 0
    Herero = 0
    HiriMotu = 0
    Kanuri = 0
    Komi = 0
    Kongo = 0
    Kwanyama = 0
    Limburgish = 0
    Luxembourgish = 0
    Navaho = 0
    Ndonga = 0
    Ojibwa = 0
    Pali = 0
    Walloon = 0
    Avestan = 0
    Asturian = 0
    Ngomba = 0
    Kako = 0
    Meta = 0
    Ngiemboon = 0
    Uighur = 0
    Aragonese = 0
    Akkadian = 0
    AncientEgyptian = 0
    AncientGreek = 0
    Aramaic = 0
    Balinese = 0
    Bamun = 0
    BatakToba = 0
    Buginese = 0
    Buhid = 0
    Carian = 0
    Chakma = 0
    ClassicalMandaic = 0
    Coptic = 0
    Dogri = 0
    EasternCham = 0
    EasternKayah = 0
    Etruscan = 0
    Gothic = 0
    Hanunoo = 0
    Ingush = 0
    LargeFloweryMiao = 0
    Lepcha = 0
    Limbu = 0
    Lisu = 0
    Lu = 0
    Lycian = 0
    Lydian = 0
    Mandingo = 0
    Manipuri = 0
    Meroitic = 0
    NorthernThai = 0
    OldIrish = 0
    OldNorse = 0
    OldPersian = 0
    OldTurkish = 0
    Pahlavi = 0
    Parthian = 0
    Phoenician = 0
    PrakritLanguage = 0
    Rejang = 0
    Sabaean = 0
    Samaritan = 0
    Santali = 0
    Saurashtra = 0
    Sora = 0
    Sylheti = 0
    Tagbanwa = 0
    TaiDam = 0
    TaiNua = 0
    Ugaritic = 0
    Akoose = 0
    Lakota = 0
    StandardMoroccanTamazight = 0
    Mapuche = 0
    CentralKurdish = 0
    LowerSorbian = 0
    UpperSorbian = 0
    Kenyang = 0
    Mohawk = 0
    Nko = 0
    Prussian = 0
    Kiche = 0
    SouthernSami = 0
    LuleSami = 0
    InariSami = 0
    SkoltSami = 0
    Warlpiri = 0
    ManichaeanMiddlePersian = 0
    Mende = 0
    AncientNorthArabian = 0
    LinearA = 0
    HmongNjua = 0
    Ho = 0
    Lezghian = 0
    Bassa = 0
    Mono = 0
    TedimChin = 0
    Maithili = 0

    def __init__(self):
        '''void QLocale.__init__()'''
    def __init__(self, name):
        '''void QLocale.__init__(str name)'''
    def __init__(self, language, country = None):
        '''void QLocale.__init__(QLocale.Language language, QLocale.Country country = QLocale.AnyCountry)'''
    def __init__(self, other):
        '''void QLocale.__init__(QLocale other)'''
    def __init__(self, language, script, country):
        '''void QLocale.__init__(QLocale.Language language, QLocale.Script script, QLocale.Country country)'''
    def createSeparatedList(self, list):
        '''str QLocale.createSeparatedList(list-of-str list)'''
        return str()
    def quoteString(self, str, style = None):
        '''str QLocale.quoteString(str str, QLocale.QuotationStyle style = QLocale.StandardQuotation)'''
        return str()
    def matchingLocales(self, language, script, country):
        '''static list-of-QLocale QLocale.matchingLocales(QLocale.Language language, QLocale.Script script, QLocale.Country country)'''
        return [QLocale()]
    def scriptToString(self, script):
        '''static str QLocale.scriptToString(QLocale.Script script)'''
        return str()
    def uiLanguages(self):
        '''list-of-str QLocale.uiLanguages()'''
        return [str()]
    def toCurrencyString(self, value, symbol = None):
        '''str QLocale.toCurrencyString(int value, str symbol = '')'''
        return str()
    def toCurrencyString(self, value, symbol = None):
        '''str QLocale.toCurrencyString(float value, str symbol = '')'''
        return str()
    def toCurrencyString(self, value, symbol = None):
        '''str QLocale.toCurrencyString(int value, str symbol = '')'''
        return str()
    def toCurrencyString(self, value, symbol = None):
        '''str QLocale.toCurrencyString(int value, str symbol = '')'''
        return str()
    def currencySymbol(self, format = None):
        '''str QLocale.currencySymbol(QLocale.CurrencySymbolFormat format = QLocale.CurrencySymbol)'''
        return str()
    def toLower(self, str):
        '''str QLocale.toLower(str str)'''
        return str()
    def toUpper(self, str):
        '''str QLocale.toUpper(str str)'''
        return str()
    def weekdays(self):
        '''list-of-Qt.DayOfWeek QLocale.weekdays()'''
        return [Qt.DayOfWeek()]
    def firstDayOfWeek(self):
        '''Qt.DayOfWeek QLocale.firstDayOfWeek()'''
        return Qt.DayOfWeek()
    def nativeCountryName(self):
        '''str QLocale.nativeCountryName()'''
        return str()
    def nativeLanguageName(self):
        '''str QLocale.nativeLanguageName()'''
        return str()
    def bcp47Name(self):
        '''str QLocale.bcp47Name()'''
        return str()
    def script(self):
        '''QLocale.Script QLocale.script()'''
        return QLocale.Script()
    def textDirection(self):
        '''Qt.LayoutDirection QLocale.textDirection()'''
        return Qt.LayoutDirection()
    def pmText(self):
        '''str QLocale.pmText()'''
        return str()
    def amText(self):
        '''str QLocale.amText()'''
        return str()
    def standaloneDayName(self, format = None):
        '''int QLocale.standaloneDayName(QLocale.FormatType format = QLocale.LongFormat)'''
        return int()
    def standaloneMonthName(self, format = None):
        '''int QLocale.standaloneMonthName(QLocale.FormatType format = QLocale.LongFormat)'''
        return int()
    def positiveSign(self):
        '''str QLocale.positiveSign()'''
        return str()
    def measurementSystem(self):
        '''QLocale.MeasurementSystem QLocale.measurementSystem()'''
        return QLocale.MeasurementSystem()
    def numberOptions(self):
        '''QLocale.NumberOptions QLocale.numberOptions()'''
        return QLocale.NumberOptions()
    def setNumberOptions(self, options):
        '''void QLocale.setNumberOptions(QLocale.NumberOptions options)'''
    def dayName(self, format = None):
        '''int QLocale.dayName(QLocale.FormatType format = QLocale.LongFormat)'''
        return int()
    def monthName(self, format = None):
        '''int QLocale.monthName(QLocale.FormatType format = QLocale.LongFormat)'''
        return int()
    def exponential(self):
        '''str QLocale.exponential()'''
        return str()
    def negativeSign(self):
        '''str QLocale.negativeSign()'''
        return str()
    def zeroDigit(self):
        '''str QLocale.zeroDigit()'''
        return str()
    def percent(self):
        '''str QLocale.percent()'''
        return str()
    def groupSeparator(self):
        '''str QLocale.groupSeparator()'''
        return str()
    def decimalPoint(self):
        '''str QLocale.decimalPoint()'''
        return str()
    def toDateTime(self, string, format = None):
        '''QDateTime QLocale.toDateTime(str string, QLocale.FormatType format = QLocale.LongFormat)'''
        return QDateTime()
    def toDateTime(self, string, format):
        '''QDateTime QLocale.toDateTime(str string, str format)'''
        return QDateTime()
    def toTime(self, string, format = None):
        '''QTime QLocale.toTime(str string, QLocale.FormatType format = QLocale.LongFormat)'''
        return QTime()
    def toTime(self, string, format):
        '''QTime QLocale.toTime(str string, str format)'''
        return QTime()
    def toDate(self, string, format = None):
        '''QDate QLocale.toDate(str string, QLocale.FormatType format = QLocale.LongFormat)'''
        return QDate()
    def toDate(self, string, format):
        '''QDate QLocale.toDate(str string, str format)'''
        return QDate()
    def dateTimeFormat(self, format = None):
        '''str QLocale.dateTimeFormat(QLocale.FormatType format = QLocale.LongFormat)'''
        return str()
    def timeFormat(self, format = None):
        '''str QLocale.timeFormat(QLocale.FormatType format = QLocale.LongFormat)'''
        return str()
    def dateFormat(self, format = None):
        '''str QLocale.dateFormat(QLocale.FormatType format = QLocale.LongFormat)'''
        return str()
    def system(self):
        '''static QLocale QLocale.system()'''
        return QLocale()
    def c(self):
        '''static QLocale QLocale.c()'''
        return QLocale()
    def setDefault(self, locale):
        '''static void QLocale.setDefault(QLocale locale)'''
    def countryToString(self, country):
        '''static str QLocale.countryToString(QLocale.Country country)'''
        return str()
    def languageToString(self, language):
        '''static str QLocale.languageToString(QLocale.Language language)'''
        return str()
    def __ne__(self, other):
        '''bool QLocale.__ne__(QLocale other)'''
        return bool()
    def __eq__(self, other):
        '''bool QLocale.__eq__(QLocale other)'''
        return bool()
    def toString(self, i):
        '''str QLocale.toString(int i)'''
        return str()
    def toString(self, i, format = None, precision = 6):
        '''str QLocale.toString(float i, str format = 'g', int precision = 6)'''
        return str()
    def toString(self, i):
        '''str QLocale.toString(int i)'''
        return str()
    def toString(self, i):
        '''str QLocale.toString(int i)'''
        return str()
    def toString(self, dateTime, format):
        '''str QLocale.toString(QDateTime dateTime, str format)'''
        return str()
    def toString(self, dateTime, format = None):
        '''str QLocale.toString(QDateTime dateTime, QLocale.FormatType format = QLocale.LongFormat)'''
        return str()
    def toString(self, date, formatStr):
        '''str QLocale.toString(QDate date, str formatStr)'''
        return str()
    def toString(self, date, format = None):
        '''str QLocale.toString(QDate date, QLocale.FormatType format = QLocale.LongFormat)'''
        return str()
    def toString(self, time, formatStr):
        '''str QLocale.toString(QTime time, str formatStr)'''
        return str()
    def toString(self, time, format = None):
        '''str QLocale.toString(QTime time, QLocale.FormatType format = QLocale.LongFormat)'''
        return str()
    def toDouble(self, s, ok):
        '''float QLocale.toDouble(str s, bool ok)'''
        return float()
    def toFloat(self, s, ok):
        '''float QLocale.toFloat(str s, bool ok)'''
        return float()
    def toULongLong(self, s, ok):
        '''int QLocale.toULongLong(str s, bool ok)'''
        return int()
    def toLongLong(self, s, ok):
        '''int QLocale.toLongLong(str s, bool ok)'''
        return int()
    def toUInt(self, s, ok):
        '''int QLocale.toUInt(str s, bool ok)'''
        return int()
    def toInt(self, s, ok):
        '''int QLocale.toInt(str s, bool ok)'''
        return int()
    def toUShort(self, s, ok):
        '''int QLocale.toUShort(str s, bool ok)'''
        return int()
    def toShort(self, s, ok):
        '''int QLocale.toShort(str s, bool ok)'''
        return int()
    def name(self):
        '''str QLocale.name()'''
        return str()
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


class QLockFile():
    """"""
    # Enum QLockFile.LockError
    NoError = 0
    LockFailedError = 0
    PermissionError = 0
    UnknownError = 0

    def __init__(self, fileName):
        '''void QLockFile.__init__(str fileName)'''
    def error(self):
        '''QLockFile.LockError QLockFile.error()'''
        return QLockFile.LockError()
    def removeStaleLockFile(self):
        '''bool QLockFile.removeStaleLockFile()'''
        return bool()
    def getLockInfo(self, pid, hostname, appname):
        '''bool QLockFile.getLockInfo(int pid, str hostname, str appname)'''
        return bool()
    def isLocked(self):
        '''bool QLockFile.isLocked()'''
        return bool()
    def staleLockTime(self):
        '''int QLockFile.staleLockTime()'''
        return int()
    def setStaleLockTime(self):
        '''int QLockFile.setStaleLockTime()'''
        return int()
    def unlock(self):
        '''void QLockFile.unlock()'''
    def tryLock(self, timeout = 0):
        '''bool QLockFile.tryLock(int timeout = 0)'''
        return bool()
    def lock(self):
        '''bool QLockFile.lock()'''
        return bool()


class QMessageLogContext():
    """"""
    category = None # str - member
    file = None # str - member
    function = None # str - member
    line = None # int - member


class QMessageLogger():
    """"""
    def __init__(self):
        '''void QMessageLogger.__init__()'''
    def __init__(self, file, line, function):
        '''void QMessageLogger.__init__(str file, int line, str function)'''
    def __init__(self, file, line, function, category):
        '''void QMessageLogger.__init__(str file, int line, str function, str category)'''
    def info(self, msg):
        '''void QMessageLogger.info(str msg)'''
    def fatal(self, msg):
        '''void QMessageLogger.fatal(str msg)'''
    def critical(self, msg):
        '''void QMessageLogger.critical(str msg)'''
    def warning(self, msg):
        '''void QMessageLogger.warning(str msg)'''
    def debug(self, msg):
        '''void QMessageLogger.debug(str msg)'''


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
    def __add__(self, m2):
        '''QMargins QMargins.__add__(QMargins m2)'''
        return QMargins()
    def __add__(self, rhs):
        '''QMargins QMargins.__add__(int rhs)'''
        return QMargins()
    def __add__(self, rhs):
        '''QMargins QMargins.__add__(QMargins rhs)'''
        return QMargins()
    def __add__(self, rectangle):
        '''QRect QMargins.__add__(QRect rectangle)'''
        return QRect()
    def __sub__(self, m2):
        '''QMargins QMargins.__sub__(QMargins m2)'''
        return QMargins()
    def __sub__(self, rhs):
        '''QMargins QMargins.__sub__(int rhs)'''
        return QMargins()
    def __mul__(self, factor):
        '''QMargins QMargins.__mul__(int factor)'''
        return QMargins()
    def __mul__(self, factor):
        '''QMargins QMargins.__mul__(float factor)'''
        return QMargins()
    def __div__(self, divisor):
        '''QMargins QMargins.__div__(int divisor)'''
        return QMargins()
    def __div__(self, divisor):
        '''QMargins QMargins.__div__(float divisor)'''
        return QMargins()
    def __neg__(self):
        '''QMargins QMargins.__neg__()'''
        return QMargins()
    def __pos__(self):
        '''QMargins QMargins.__pos__()'''
        return QMargins()
    def __idiv__(self, divisor):
        '''QMargins QMargins.__idiv__(int divisor)'''
        return QMargins()
    def __idiv__(self, divisor):
        '''QMargins QMargins.__idiv__(float divisor)'''
        return QMargins()
    def __imul__(self, factor):
        '''QMargins QMargins.__imul__(int factor)'''
        return QMargins()
    def __imul__(self, factor):
        '''QMargins QMargins.__imul__(float factor)'''
        return QMargins()
    def __isub__(self, margins):
        '''QMargins QMargins.__isub__(QMargins margins)'''
        return QMargins()
    def __isub__(self, margin):
        '''QMargins QMargins.__isub__(int margin)'''
        return QMargins()
    def __iadd__(self, margins):
        '''QMargins QMargins.__iadd__(QMargins margins)'''
        return QMargins()
    def __iadd__(self, margin):
        '''QMargins QMargins.__iadd__(int margin)'''
        return QMargins()
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


class QMarginsF():
    """"""
    def __init__(self):
        '''void QMarginsF.__init__()'''
    def __init__(self, aleft, atop, aright, abottom):
        '''void QMarginsF.__init__(float aleft, float atop, float aright, float abottom)'''
    def __init__(self, margins):
        '''void QMarginsF.__init__(QMargins margins)'''
    def __init__(self):
        '''QMarginsF QMarginsF.__init__()'''
        return QMarginsF()
    def __eq__(self, rhs):
        '''bool QMarginsF.__eq__(QMarginsF rhs)'''
        return bool()
    def __ne__(self, rhs):
        '''bool QMarginsF.__ne__(QMarginsF rhs)'''
        return bool()
    def __add__(self, rhs):
        '''QMarginsF QMarginsF.__add__(QMarginsF rhs)'''
        return QMarginsF()
    def __add__(self, rhs):
        '''QMarginsF QMarginsF.__add__(float rhs)'''
        return QMarginsF()
    def __add__(self, rhs):
        '''QMarginsF QMarginsF.__add__(QMarginsF rhs)'''
        return QMarginsF()
    def __add__(self, rhs):
        '''QRectF QMarginsF.__add__(QRectF rhs)'''
        return QRectF()
    def __sub__(self, rhs):
        '''QMarginsF QMarginsF.__sub__(QMarginsF rhs)'''
        return QMarginsF()
    def __sub__(self, rhs):
        '''QMarginsF QMarginsF.__sub__(float rhs)'''
        return QMarginsF()
    def __mul__(self, rhs):
        '''QMarginsF QMarginsF.__mul__(float rhs)'''
        return QMarginsF()
    def __mul__(self, rhs):
        '''QMarginsF QMarginsF.__mul__(QMarginsF rhs)'''
        return QMarginsF()
    def __div__(self, divisor):
        '''QMarginsF QMarginsF.__div__(float divisor)'''
        return QMarginsF()
    def __neg__(self):
        '''QMarginsF QMarginsF.__neg__()'''
        return QMarginsF()
    def __pos__(self):
        '''QMarginsF QMarginsF.__pos__()'''
        return QMarginsF()
    def toMargins(self):
        '''QMargins QMarginsF.toMargins()'''
        return QMargins()
    def __idiv__(self, divisor):
        '''QMarginsF QMarginsF.__idiv__(float divisor)'''
        return QMarginsF()
    def __imul__(self, factor):
        '''QMarginsF QMarginsF.__imul__(float factor)'''
        return QMarginsF()
    def __isub__(self, margins):
        '''QMarginsF QMarginsF.__isub__(QMarginsF margins)'''
        return QMarginsF()
    def __isub__(self, subtrahend):
        '''QMarginsF QMarginsF.__isub__(float subtrahend)'''
        return QMarginsF()
    def __iadd__(self, margins):
        '''QMarginsF QMarginsF.__iadd__(QMarginsF margins)'''
        return QMarginsF()
    def __iadd__(self, addend):
        '''QMarginsF QMarginsF.__iadd__(float addend)'''
        return QMarginsF()
    def setBottom(self, abottom):
        '''void QMarginsF.setBottom(float abottom)'''
    def setRight(self, aright):
        '''void QMarginsF.setRight(float aright)'''
    def setTop(self, atop):
        '''void QMarginsF.setTop(float atop)'''
    def setLeft(self, aleft):
        '''void QMarginsF.setLeft(float aleft)'''
    def bottom(self):
        '''float QMarginsF.bottom()'''
        return float()
    def right(self):
        '''float QMarginsF.right()'''
        return float()
    def top(self):
        '''float QMarginsF.top()'''
        return float()
    def left(self):
        '''float QMarginsF.left()'''
        return float()
    def isNull(self):
        '''bool QMarginsF.isNull()'''
        return bool()


class QMessageAuthenticationCode():
    """"""
    def __init__(self, method, key = QByteArray()):
        '''void QMessageAuthenticationCode.__init__(QCryptographicHash.Algorithm method, QByteArray key = QByteArray())'''
    def hash(self, message, key, method):
        '''static QByteArray QMessageAuthenticationCode.hash(QByteArray message, QByteArray key, QCryptographicHash.Algorithm method)'''
        return QByteArray()
    def result(self):
        '''QByteArray QMessageAuthenticationCode.result()'''
        return QByteArray()
    def addData(self, data, length):
        '''void QMessageAuthenticationCode.addData(str data, int length)'''
    def addData(self, data):
        '''void QMessageAuthenticationCode.addData(QByteArray data)'''
    def addData(self, device):
        '''bool QMessageAuthenticationCode.addData(QIODevice device)'''
        return bool()
    def setKey(self, key):
        '''void QMessageAuthenticationCode.setKey(QByteArray key)'''
    def reset(self):
        '''void QMessageAuthenticationCode.reset()'''


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
    def __eq__(self, m2):
        '''bool QMetaMethod.__eq__(QMetaMethod m2)'''
        return bool()
    def __ne__(self, m2):
        '''bool QMetaMethod.__ne__(QMetaMethod m2)'''
        return bool()
    def parameterType(self, index):
        '''int QMetaMethod.parameterType(int index)'''
        return int()
    def parameterCount(self):
        '''int QMetaMethod.parameterCount()'''
        return int()
    def returnType(self):
        '''int QMetaMethod.returnType()'''
        return int()
    def name(self):
        '''QByteArray QMetaMethod.name()'''
        return QByteArray()
    def methodSignature(self):
        '''QByteArray QMetaMethod.methodSignature()'''
        return QByteArray()
    def isValid(self):
        '''bool QMetaMethod.isValid()'''
        return bool()
    def methodIndex(self):
        '''int QMetaMethod.methodIndex()'''
        return int()
    def invoke(self, object, connectionType, returnValue, value0 = None, value1 = None, value2 = None, value3 = None, value4 = None, value5 = None, value6 = None, value7 = None, value8 = None, value9 = None):
        '''object QMetaMethod.invoke(QObject object, Qt.ConnectionType connectionType, QGenericReturnArgument returnValue, QGenericArgument value0 = QGenericArgument(0,0), QGenericArgument value1 = QGenericArgument(0,0), QGenericArgument value2 = QGenericArgument(0,0), QGenericArgument value3 = QGenericArgument(0,0), QGenericArgument value4 = QGenericArgument(0,0), QGenericArgument value5 = QGenericArgument(0,0), QGenericArgument value6 = QGenericArgument(0,0), QGenericArgument value7 = QGenericArgument(0,0), QGenericArgument value8 = QGenericArgument(0,0), QGenericArgument value9 = QGenericArgument(0,0))'''
        return object()
    def invoke(self, object, returnValue, value0 = None, value1 = None, value2 = None, value3 = None, value4 = None, value5 = None, value6 = None, value7 = None, value8 = None, value9 = None):
        '''object QMetaMethod.invoke(QObject object, QGenericReturnArgument returnValue, QGenericArgument value0 = QGenericArgument(0,0), QGenericArgument value1 = QGenericArgument(0,0), QGenericArgument value2 = QGenericArgument(0,0), QGenericArgument value3 = QGenericArgument(0,0), QGenericArgument value4 = QGenericArgument(0,0), QGenericArgument value5 = QGenericArgument(0,0), QGenericArgument value6 = QGenericArgument(0,0), QGenericArgument value7 = QGenericArgument(0,0), QGenericArgument value8 = QGenericArgument(0,0), QGenericArgument value9 = QGenericArgument(0,0))'''
        return object()
    def invoke(self, object, connectionType, value0 = None, value1 = None, value2 = None, value3 = None, value4 = None, value5 = None, value6 = None, value7 = None, value8 = None, value9 = None):
        '''object QMetaMethod.invoke(QObject object, Qt.ConnectionType connectionType, QGenericArgument value0 = QGenericArgument(0,0), QGenericArgument value1 = QGenericArgument(0,0), QGenericArgument value2 = QGenericArgument(0,0), QGenericArgument value3 = QGenericArgument(0,0), QGenericArgument value4 = QGenericArgument(0,0), QGenericArgument value5 = QGenericArgument(0,0), QGenericArgument value6 = QGenericArgument(0,0), QGenericArgument value7 = QGenericArgument(0,0), QGenericArgument value8 = QGenericArgument(0,0), QGenericArgument value9 = QGenericArgument(0,0))'''
        return object()
    def invoke(self, object, value0 = None, value1 = None, value2 = None, value3 = None, value4 = None, value5 = None, value6 = None, value7 = None, value8 = None, value9 = None):
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
    def keysToValue(self, keys, ok):
        '''int QMetaEnum.keysToValue(str keys, bool ok)'''
        return int()
    def valueToKey(self, value):
        '''str QMetaEnum.valueToKey(int value)'''
        return str()
    def keyToValue(self, key, ok):
        '''int QMetaEnum.keyToValue(str key, bool ok)'''
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
        '''QVariant.Type QMetaProperty.type()'''
        return QVariant.Type()
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
    # Enum QMetaType.TypeFlag
    NeedsConstruction = 0
    NeedsDestruction = 0
    MovableType = 0
    IsGadget = 0

    # Enum QMetaType.Type
    UnknownType = 0
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
    QMatrix4x4 = 0
    QVector2D = 0
    QVector3D = 0
    QVector4D = 0
    QQuaternion = 0
    QEasingCurve = 0
    QVariant = 0
    QUuid = 0
    QModelIndex = 0
    QPolygonF = 0
    SChar = 0
    QRegularExpression = 0
    QJsonValue = 0
    QJsonObject = 0
    QJsonArray = 0
    QJsonDocument = 0
    QByteArrayList = 0
    QPersistentModelIndex = 0
    User = 0

    def __init__(self, type):
        '''void QMetaType.__init__(int type)'''
    def metaObjectForType(self, type):
        '''static QMetaObject QMetaType.metaObjectForType(int type)'''
        return QMetaObject()
    def flags(self):
        '''QMetaType.TypeFlags QMetaType.flags()'''
        return QMetaType.TypeFlags()
    def isValid(self):
        '''bool QMetaType.isValid()'''
        return bool()
    def typeFlags(self, type):
        '''static QMetaType.TypeFlags QMetaType.typeFlags(int type)'''
        return QMetaType.TypeFlags()
    def isRegistered(self, type):
        '''static bool QMetaType.isRegistered(int type)'''
        return bool()
    def isRegistered(self):
        '''bool QMetaType.isRegistered()'''
        return bool()
    def typeName(self, type):
        '''static str QMetaType.typeName(int type)'''
        return str()
    def type(self, typeName):
        '''static int QMetaType.type(str typeName)'''
        return int()
    class TypeFlags():
        """"""
        def __init__(self):
            '''QMetaType.TypeFlags QMetaType.TypeFlags.__init__()'''
            return QMetaType.TypeFlags()
        def __init__(self):
            '''int QMetaType.TypeFlags.__init__()'''
            return int()
        def __init__(self):
            '''void QMetaType.TypeFlags.__init__()'''
        def __bool__(self):
            '''int QMetaType.TypeFlags.__bool__()'''
            return int()
        def __ne__(self, f):
            '''bool QMetaType.TypeFlags.__ne__(QMetaType.TypeFlags f)'''
            return bool()
        def __eq__(self, f):
            '''bool QMetaType.TypeFlags.__eq__(QMetaType.TypeFlags f)'''
            return bool()
        def __invert__(self):
            '''QMetaType.TypeFlags QMetaType.TypeFlags.__invert__()'''
            return QMetaType.TypeFlags()
        def __and__(self, mask):
            '''QMetaType.TypeFlags QMetaType.TypeFlags.__and__(int mask)'''
            return QMetaType.TypeFlags()
        def __xor__(self, f):
            '''QMetaType.TypeFlags QMetaType.TypeFlags.__xor__(QMetaType.TypeFlags f)'''
            return QMetaType.TypeFlags()
        def __xor__(self, f):
            '''QMetaType.TypeFlags QMetaType.TypeFlags.__xor__(int f)'''
            return QMetaType.TypeFlags()
        def __or__(self, f):
            '''QMetaType.TypeFlags QMetaType.TypeFlags.__or__(QMetaType.TypeFlags f)'''
            return QMetaType.TypeFlags()
        def __or__(self, f):
            '''QMetaType.TypeFlags QMetaType.TypeFlags.__or__(int f)'''
            return QMetaType.TypeFlags()
        def __int__(self):
            '''int QMetaType.TypeFlags.__int__()'''
            return int()
        def __ixor__(self, f):
            '''QMetaType.TypeFlags QMetaType.TypeFlags.__ixor__(QMetaType.TypeFlags f)'''
            return QMetaType.TypeFlags()
        def __ior__(self, f):
            '''QMetaType.TypeFlags QMetaType.TypeFlags.__ior__(QMetaType.TypeFlags f)'''
            return QMetaType.TypeFlags()
        def __iand__(self, mask):
            '''QMetaType.TypeFlags QMetaType.TypeFlags.__iand__(int mask)'''
            return QMetaType.TypeFlags()


class QMimeData(QObject):
    """"""
    def __init__(self):
        '''void QMimeData.__init__()'''
    def retrieveData(self, mimetype, preferredType):
        '''QVariant QMimeData.retrieveData(str mimetype, QVariant.Type preferredType)'''
        return QVariant()
    def removeFormat(self, mimetype):
        '''void QMimeData.removeFormat(str mimetype)'''
    def clear(self):
        '''void QMimeData.clear()'''
    def formats(self):
        '''list-of-str QMimeData.formats()'''
        return [str()]
    def hasFormat(self, mimetype):
        '''bool QMimeData.hasFormat(str mimetype)'''
        return bool()
    def setData(self, mimetype, data):
        '''void QMimeData.setData(str mimetype, QByteArray data)'''
    def data(self, mimetype):
        '''QByteArray QMimeData.data(str mimetype)'''
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
        '''void QMimeData.setHtml(str html)'''
    def html(self):
        '''str QMimeData.html()'''
        return str()
    def hasText(self):
        '''bool QMimeData.hasText()'''
        return bool()
    def setText(self, text):
        '''void QMimeData.setText(str text)'''
    def text(self):
        '''str QMimeData.text()'''
        return str()
    def hasUrls(self):
        '''bool QMimeData.hasUrls()'''
        return bool()
    def setUrls(self, urls):
        '''void QMimeData.setUrls(list-of-QUrl urls)'''
    def urls(self):
        '''list-of-QUrl QMimeData.urls()'''
        return [QUrl()]


class QMimeDatabase():
    """"""
    # Enum QMimeDatabase.MatchMode
    MatchDefault = 0
    MatchExtension = 0
    MatchContent = 0

    def __init__(self):
        '''void QMimeDatabase.__init__()'''
    def allMimeTypes(self):
        '''list-of-QMimeType QMimeDatabase.allMimeTypes()'''
        return [QMimeType()]
    def suffixForFileName(self, fileName):
        '''str QMimeDatabase.suffixForFileName(str fileName)'''
        return str()
    def mimeTypeForFileNameAndData(self, fileName, device):
        '''QMimeType QMimeDatabase.mimeTypeForFileNameAndData(str fileName, QIODevice device)'''
        return QMimeType()
    def mimeTypeForFileNameAndData(self, fileName, data):
        '''QMimeType QMimeDatabase.mimeTypeForFileNameAndData(str fileName, QByteArray data)'''
        return QMimeType()
    def mimeTypeForUrl(self, url):
        '''QMimeType QMimeDatabase.mimeTypeForUrl(QUrl url)'''
        return QMimeType()
    def mimeTypeForData(self, data):
        '''QMimeType QMimeDatabase.mimeTypeForData(QByteArray data)'''
        return QMimeType()
    def mimeTypeForData(self, device):
        '''QMimeType QMimeDatabase.mimeTypeForData(QIODevice device)'''
        return QMimeType()
    def mimeTypesForFileName(self, fileName):
        '''list-of-QMimeType QMimeDatabase.mimeTypesForFileName(str fileName)'''
        return [QMimeType()]
    def mimeTypeForFile(self, fileName, mode = None):
        '''QMimeType QMimeDatabase.mimeTypeForFile(str fileName, QMimeDatabase.MatchMode mode = QMimeDatabase.MatchDefault)'''
        return QMimeType()
    def mimeTypeForFile(self, fileInfo, mode = None):
        '''QMimeType QMimeDatabase.mimeTypeForFile(QFileInfo fileInfo, QMimeDatabase.MatchMode mode = QMimeDatabase.MatchDefault)'''
        return QMimeType()
    def mimeTypeForName(self, nameOrAlias):
        '''QMimeType QMimeDatabase.mimeTypeForName(str nameOrAlias)'''
        return QMimeType()


class QMimeType():
    """"""
    def __init__(self):
        '''void QMimeType.__init__()'''
    def __init__(self, other):
        '''void QMimeType.__init__(QMimeType other)'''
    def filterString(self):
        '''str QMimeType.filterString()'''
        return str()
    def inherits(self, mimeTypeName):
        '''bool QMimeType.inherits(str mimeTypeName)'''
        return bool()
    def preferredSuffix(self):
        '''str QMimeType.preferredSuffix()'''
        return str()
    def suffixes(self):
        '''list-of-str QMimeType.suffixes()'''
        return [str()]
    def aliases(self):
        '''list-of-str QMimeType.aliases()'''
        return [str()]
    def allAncestors(self):
        '''list-of-str QMimeType.allAncestors()'''
        return [str()]
    def parentMimeTypes(self):
        '''list-of-str QMimeType.parentMimeTypes()'''
        return [str()]
    def globPatterns(self):
        '''list-of-str QMimeType.globPatterns()'''
        return [str()]
    def iconName(self):
        '''str QMimeType.iconName()'''
        return str()
    def genericIconName(self):
        '''str QMimeType.genericIconName()'''
        return str()
    def comment(self):
        '''str QMimeType.comment()'''
        return str()
    def name(self):
        '''str QMimeType.name()'''
        return str()
    def isDefault(self):
        '''bool QMimeType.isDefault()'''
        return bool()
    def isValid(self):
        '''bool QMimeType.isValid()'''
        return bool()
    def __ne__(self, other):
        '''bool QMimeType.__ne__(QMimeType other)'''
        return bool()
    def __eq__(self, other):
        '''bool QMimeType.__eq__(QMimeType other)'''
        return bool()
    def swap(self, other):
        '''void QMimeType.swap(QMimeType other)'''


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


class QMutex():
    """"""
    # Enum QMutex.RecursionMode
    NonRecursive = 0
    Recursive = 0

    def __init__(self, mode = None):
        '''void QMutex.__init__(QMutex.RecursionMode mode = QMutex.NonRecursive)'''
    def isRecursive(self):
        '''bool QMutex.isRecursive()'''
        return bool()
    def unlock(self):
        '''void QMutex.unlock()'''
    def tryLock(self, timeout = 0):
        '''bool QMutex.tryLock(int timeout = 0)'''
        return bool()
    def lock(self):
        '''void QMutex.lock()'''


class QSignalBlocker():
    """"""
    def __init__(self, o):
        '''void QSignalBlocker.__init__(QObject o)'''
    def __exit__(self, type, value, traceback):
        '''void QSignalBlocker.__exit__(object type, object value, object traceback)'''
    def __enter__(self):
        '''object QSignalBlocker.__enter__()'''
        return object()
    def unblock(self):
        '''void QSignalBlocker.unblock()'''
    def reblock(self):
        '''void QSignalBlocker.reblock()'''


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
    def constructor(self, index):
        '''QMetaMethod QMetaObject.constructor(int index)'''
        return QMetaMethod()
    def indexOfConstructor(self, constructor):
        '''int QMetaObject.indexOfConstructor(str constructor)'''
        return int()
    def constructorCount(self):
        '''int QMetaObject.constructorCount()'''
        return int()
    def invokeMethod(self, obj, member, type, ret, value0 = None, value1 = None, value2 = None, value3 = None, value4 = None, value5 = None, value6 = None, value7 = None, value8 = None, value9 = None):
        '''static object QMetaObject.invokeMethod(QObject obj, str member, Qt.ConnectionType type, QGenericReturnArgument ret, QGenericArgument value0 = QGenericArgument(0,0), QGenericArgument value1 = QGenericArgument(0,0), QGenericArgument value2 = QGenericArgument(0,0), QGenericArgument value3 = QGenericArgument(0,0), QGenericArgument value4 = QGenericArgument(0,0), QGenericArgument value5 = QGenericArgument(0,0), QGenericArgument value6 = QGenericArgument(0,0), QGenericArgument value7 = QGenericArgument(0,0), QGenericArgument value8 = QGenericArgument(0,0), QGenericArgument value9 = QGenericArgument(0,0))'''
        return object()
    def invokeMethod(self, obj, member, ret, value0 = None, value1 = None, value2 = None, value3 = None, value4 = None, value5 = None, value6 = None, value7 = None, value8 = None, value9 = None):
        '''static object QMetaObject.invokeMethod(QObject obj, str member, QGenericReturnArgument ret, QGenericArgument value0 = QGenericArgument(0,0), QGenericArgument value1 = QGenericArgument(0,0), QGenericArgument value2 = QGenericArgument(0,0), QGenericArgument value3 = QGenericArgument(0,0), QGenericArgument value4 = QGenericArgument(0,0), QGenericArgument value5 = QGenericArgument(0,0), QGenericArgument value6 = QGenericArgument(0,0), QGenericArgument value7 = QGenericArgument(0,0), QGenericArgument value8 = QGenericArgument(0,0), QGenericArgument value9 = QGenericArgument(0,0))'''
        return object()
    def invokeMethod(self, obj, member, type, value0 = None, value1 = None, value2 = None, value3 = None, value4 = None, value5 = None, value6 = None, value7 = None, value8 = None, value9 = None):
        '''static object QMetaObject.invokeMethod(QObject obj, str member, Qt.ConnectionType type, QGenericArgument value0 = QGenericArgument(0,0), QGenericArgument value1 = QGenericArgument(0,0), QGenericArgument value2 = QGenericArgument(0,0), QGenericArgument value3 = QGenericArgument(0,0), QGenericArgument value4 = QGenericArgument(0,0), QGenericArgument value5 = QGenericArgument(0,0), QGenericArgument value6 = QGenericArgument(0,0), QGenericArgument value7 = QGenericArgument(0,0), QGenericArgument value8 = QGenericArgument(0,0), QGenericArgument value9 = QGenericArgument(0,0))'''
        return object()
    def invokeMethod(self, obj, member, value0 = None, value1 = None, value2 = None, value3 = None, value4 = None, value5 = None, value6 = None, value7 = None, value8 = None, value9 = None):
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
    def checkConnectArgs(self, signal, method):
        '''static bool QMetaObject.checkConnectArgs(QMetaMethod signal, QMetaMethod method)'''
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
        '''void QVariantAnimation.updateCurrentValue(QVariant value)'''
    def updateState(self, newState, oldState):
        '''void QVariantAnimation.updateState(QAbstractAnimation.State newState, QAbstractAnimation.State oldState)'''
    def updateCurrentTime(self):
        '''int QVariantAnimation.updateCurrentTime()'''
        return int()
    def event(self, event):
        '''bool QVariantAnimation.event(QEvent event)'''
        return bool()
    valueChanged = pyqtSignal() # void valueChanged(const QVariantamp;) - signal
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
        '''void QPluginLoader.__init__(str fileName, QObject parent = None)'''
    def loadHints(self):
        '''QLibrary.LoadHints QPluginLoader.loadHints()'''
        return QLibrary.LoadHints()
    def setLoadHints(self, loadHints):
        '''void QPluginLoader.setLoadHints(QLibrary.LoadHints loadHints)'''
    def errorString(self):
        '''str QPluginLoader.errorString()'''
        return str()
    def fileName(self):
        '''str QPluginLoader.fileName()'''
        return str()
    def setFileName(self, fileName):
        '''void QPluginLoader.setFileName(str fileName)'''
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
    def __div__(self, c):
        '''QPoint QPoint.__div__(float c)'''
        return QPoint()
    def __neg__(self):
        '''QPoint QPoint.__neg__()'''
        return QPoint()
    def __pos__(self):
        '''QPoint QPoint.__pos__()'''
        return QPoint()
    def dotProduct(self, p1, p2):
        '''static int QPoint.dotProduct(QPoint p1, QPoint p2)'''
        return int()
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
    def __mul__(self, p):
        '''QPointF QPointF.__mul__(QPointF p)'''
        return QPointF()
    def __div__(self, c):
        '''QPointF QPointF.__div__(float c)'''
        return QPointF()
    def __neg__(self):
        '''QPointF QPointF.__neg__()'''
        return QPointF()
    def __pos__(self):
        '''QPointF QPointF.__pos__()'''
        return QPointF()
    def dotProduct(self, p1, p2):
        '''static float QPointF.dotProduct(QPointF p1, QPointF p2)'''
        return float()
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
    # Enum QProcess.InputChannelMode
    ManagedInputChannel = 0
    ForwardedInputChannel = 0

    # Enum QProcess.ProcessChannelMode
    SeparateChannels = 0
    MergedChannels = 0
    ForwardedChannels = 0
    ForwardedOutputChannel = 0
    ForwardedErrorChannel = 0

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
    def processId(self):
        '''int QProcess.processId()'''
        return int()
    def nullDevice(self):
        '''static str QProcess.nullDevice()'''
        return str()
    def setInputChannelMode(self, mode):
        '''void QProcess.setInputChannelMode(QProcess.InputChannelMode mode)'''
    def inputChannelMode(self):
        '''QProcess.InputChannelMode QProcess.inputChannelMode()'''
        return QProcess.InputChannelMode()
    def open(self, mode = None):
        '''bool QProcess.open(QIODevice.OpenMode mode = QIODevice.ReadWrite)'''
        return bool()
    def setArguments(self, arguments):
        '''void QProcess.setArguments(list-of-str arguments)'''
    def arguments(self):
        '''list-of-str QProcess.arguments()'''
        return [str()]
    def setProgram(self, program):
        '''void QProcess.setProgram(str program)'''
    def program(self):
        '''str QProcess.program()'''
        return str()
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
    started = pyqtSignal() # void started() - signal
    def kill(self):
        '''void QProcess.kill()'''
    def terminate(self):
        '''void QProcess.terminate()'''
    def setStandardOutputProcess(self, destination):
        '''void QProcess.setStandardOutputProcess(QProcess destination)'''
    def setStandardErrorFile(self, fileName, mode = None):
        '''void QProcess.setStandardErrorFile(str fileName, QIODevice.OpenMode mode = QIODevice.Truncate)'''
    def setStandardOutputFile(self, fileName, mode = None):
        '''void QProcess.setStandardOutputFile(str fileName, QIODevice.OpenMode mode = QIODevice.Truncate)'''
    def setStandardInputFile(self, fileName):
        '''void QProcess.setStandardInputFile(str fileName)'''
    def setProcessChannelMode(self, mode):
        '''void QProcess.setProcessChannelMode(QProcess.ProcessChannelMode mode)'''
    def processChannelMode(self):
        '''QProcess.ProcessChannelMode QProcess.processChannelMode()'''
        return QProcess.ProcessChannelMode()
    def systemEnvironment(self):
        '''static list-of-str QProcess.systemEnvironment()'''
        return [str()]
    def startDetached(self, program, arguments, workingDirectory, pid):
        '''static bool QProcess.startDetached(str program, list-of-str arguments, str workingDirectory, int pid)'''
        return bool()
    def startDetached(self, program, arguments):
        '''static bool QProcess.startDetached(str program, list-of-str arguments)'''
        return bool()
    def startDetached(self, program):
        '''static bool QProcess.startDetached(str program)'''
        return bool()
    def execute(self, program, arguments):
        '''static int QProcess.execute(str program, list-of-str arguments)'''
        return int()
    def execute(self, program):
        '''static int QProcess.execute(str program)'''
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
    def setWorkingDirectory(self, dir):
        '''void QProcess.setWorkingDirectory(str dir)'''
    def workingDirectory(self):
        '''str QProcess.workingDirectory()'''
        return str()
    def closeWriteChannel(self):
        '''void QProcess.closeWriteChannel()'''
    def closeReadChannel(self, channel):
        '''void QProcess.closeReadChannel(QProcess.ProcessChannel channel)'''
    def setReadChannel(self, channel):
        '''void QProcess.setReadChannel(QProcess.ProcessChannel channel)'''
    def readChannel(self):
        '''QProcess.ProcessChannel QProcess.readChannel()'''
        return QProcess.ProcessChannel()
    def start(self, program, arguments, mode = None):
        '''void QProcess.start(str program, list-of-str arguments, QIODevice.OpenMode mode = QIODevice.ReadWrite)'''
    def start(self, command, mode = None):
        '''void QProcess.start(str command, QIODevice.OpenMode mode = QIODevice.ReadWrite)'''
    def start(self, mode = None):
        '''void QProcess.start(QIODevice.OpenMode mode = QIODevice.ReadWrite)'''


class QProcessEnvironment():
    """"""
    def __init__(self):
        '''void QProcessEnvironment.__init__()'''
    def __init__(self, other):
        '''void QProcessEnvironment.__init__(QProcessEnvironment other)'''
    def swap(self, other):
        '''void QProcessEnvironment.swap(QProcessEnvironment other)'''
    def keys(self):
        '''list-of-str QProcessEnvironment.keys()'''
        return [str()]
    def systemEnvironment(self):
        '''static QProcessEnvironment QProcessEnvironment.systemEnvironment()'''
        return QProcessEnvironment()
    def toStringList(self):
        '''list-of-str QProcessEnvironment.toStringList()'''
        return [str()]
    def value(self, name, defaultValue = None):
        '''str QProcessEnvironment.value(str name, str defaultValue = '')'''
        return str()
    def remove(self, name):
        '''void QProcessEnvironment.remove(str name)'''
    def insert(self, name, value):
        '''void QProcessEnvironment.insert(str name, str value)'''
    def insert(self, e):
        '''void QProcessEnvironment.insert(QProcessEnvironment e)'''
    def contains(self, name):
        '''bool QProcessEnvironment.contains(str name)'''
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

    def __init__(self, recursionMode = None):
        '''void QReadWriteLock.__init__(QReadWriteLock.RecursionMode recursionMode = QReadWriteLock.NonRecursive)'''
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
    def __add__(self, margins):
        '''QRect QRect.__add__(QMargins margins)'''
        return QRect()
    def __sub__(self, rhs):
        '''QRect QRect.__sub__(QMargins rhs)'''
        return QRect()
    def __isub__(self, margins):
        '''QRect QRect.__isub__(QMargins margins)'''
        return QRect()
    def __iadd__(self, margins):
        '''QRect QRect.__iadd__(QMargins margins)'''
        return QRect()
    def marginsRemoved(self, margins):
        '''QRect QRect.marginsRemoved(QMargins margins)'''
        return QRect()
    def marginsAdded(self, margins):
        '''QRect QRect.marginsAdded(QMargins margins)'''
        return QRect()
    def united(self, r):
        '''QRect QRect.united(QRect r)'''
        return QRect()
    def intersected(self, other):
        '''QRect QRect.intersected(QRect other)'''
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
    def __add__(self, rhs):
        '''QRectF QRectF.__add__(QMarginsF rhs)'''
        return QRectF()
    def __sub__(self, rhs):
        '''QRectF QRectF.__sub__(QMarginsF rhs)'''
        return QRectF()
    def __isub__(self, margins):
        '''QRectF QRectF.__isub__(QMarginsF margins)'''
        return QRectF()
    def __iadd__(self, margins):
        '''QRectF QRectF.__iadd__(QMarginsF margins)'''
        return QRectF()
    def marginsRemoved(self, margins):
        '''QRectF QRectF.marginsRemoved(QMarginsF margins)'''
        return QRectF()
    def marginsAdded(self, margins):
        '''QRectF QRectF.marginsAdded(QMarginsF margins)'''
        return QRectF()
    def toRect(self):
        '''QRect QRectF.toRect()'''
        return QRect()
    def toAlignedRect(self):
        '''QRect QRectF.toAlignedRect()'''
        return QRect()
    def united(self, r):
        '''QRectF QRectF.united(QRectF r)'''
        return QRectF()
    def intersected(self, r):
        '''QRectF QRectF.intersected(QRectF r)'''
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
    def __init__(self, pattern, cs = None, syntax = None):
        '''void QRegExp.__init__(str pattern, Qt.CaseSensitivity cs = Qt.CaseSensitive, QRegExp.PatternSyntax syntax = QRegExp.RegExp)'''
    def __init__(self, rx):
        '''void QRegExp.__init__(QRegExp rx)'''
    def swap(self, other):
        '''void QRegExp.swap(QRegExp other)'''
    def captureCount(self):
        '''int QRegExp.captureCount()'''
        return int()
    def escape(self, str):
        '''static str QRegExp.escape(str str)'''
        return str()
    def errorString(self):
        '''str QRegExp.errorString()'''
        return str()
    def pos(self, nth = 0):
        '''int QRegExp.pos(int nth = 0)'''
        return int()
    def cap(self, nth = 0):
        '''str QRegExp.cap(int nth = 0)'''
        return str()
    def capturedTexts(self):
        '''list-of-str QRegExp.capturedTexts()'''
        return [str()]
    def matchedLength(self):
        '''int QRegExp.matchedLength()'''
        return int()
    def lastIndexIn(self, str, offset = None, caretMode = None):
        '''int QRegExp.lastIndexIn(str str, int offset = -1, QRegExp.CaretMode caretMode = QRegExp.CaretAtZero)'''
        return int()
    def indexIn(self, str, offset = 0, caretMode = None):
        '''int QRegExp.indexIn(str str, int offset = 0, QRegExp.CaretMode caretMode = QRegExp.CaretAtZero)'''
        return int()
    def exactMatch(self, str):
        '''bool QRegExp.exactMatch(str str)'''
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
        '''void QRegExp.setPattern(str pattern)'''
    def pattern(self):
        '''str QRegExp.pattern()'''
        return str()
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


class QRegularExpression():
    """"""
    # Enum QRegularExpression.MatchOption
    NoMatchOption = 0
    AnchoredMatchOption = 0
    DontCheckSubjectStringMatchOption = 0

    # Enum QRegularExpression.MatchType
    NormalMatch = 0
    PartialPreferCompleteMatch = 0
    PartialPreferFirstMatch = 0
    NoMatch = 0

    # Enum QRegularExpression.PatternOption
    NoPatternOption = 0
    CaseInsensitiveOption = 0
    DotMatchesEverythingOption = 0
    MultilineOption = 0
    ExtendedPatternSyntaxOption = 0
    InvertedGreedinessOption = 0
    DontCaptureOption = 0
    UseUnicodePropertiesOption = 0
    OptimizeOnFirstUsageOption = 0
    DontAutomaticallyOptimizeOption = 0

    def __init__(self):
        '''void QRegularExpression.__init__()'''
    def __init__(self, pattern, options = None):
        '''void QRegularExpression.__init__(str pattern, QRegularExpression.PatternOptions options = QRegularExpression.NoPatternOption)'''
    def __init__(self, re):
        '''void QRegularExpression.__init__(QRegularExpression re)'''
    def optimize(self):
        '''void QRegularExpression.optimize()'''
    def __ne__(self, re):
        '''bool QRegularExpression.__ne__(QRegularExpression re)'''
        return bool()
    def __eq__(self, re):
        '''bool QRegularExpression.__eq__(QRegularExpression re)'''
        return bool()
    def namedCaptureGroups(self):
        '''list-of-str QRegularExpression.namedCaptureGroups()'''
        return [str()]
    def escape(self, str):
        '''static str QRegularExpression.escape(str str)'''
        return str()
    def globalMatch(self, subject, offset = 0, matchType = None, matchOptions = None):
        '''QRegularExpressionMatchIterator QRegularExpression.globalMatch(str subject, int offset = 0, QRegularExpression.MatchType matchType = QRegularExpression.NormalMatch, QRegularExpression.MatchOptions matchOptions = QRegularExpression.NoMatchOption)'''
        return QRegularExpressionMatchIterator()
    def match(self, subject, offset = 0, matchType = None, matchOptions = None):
        '''QRegularExpressionMatch QRegularExpression.match(str subject, int offset = 0, QRegularExpression.MatchType matchType = QRegularExpression.NormalMatch, QRegularExpression.MatchOptions matchOptions = QRegularExpression.NoMatchOption)'''
        return QRegularExpressionMatch()
    def captureCount(self):
        '''int QRegularExpression.captureCount()'''
        return int()
    def errorString(self):
        '''str QRegularExpression.errorString()'''
        return str()
    def patternErrorOffset(self):
        '''int QRegularExpression.patternErrorOffset()'''
        return int()
    def isValid(self):
        '''bool QRegularExpression.isValid()'''
        return bool()
    def setPattern(self, pattern):
        '''void QRegularExpression.setPattern(str pattern)'''
    def pattern(self):
        '''str QRegularExpression.pattern()'''
        return str()
    def swap(self, re):
        '''void QRegularExpression.swap(QRegularExpression re)'''
    def __repr__(self):
        '''str QRegularExpression.__repr__()'''
        return str()
    def setPatternOptions(self, options):
        '''void QRegularExpression.setPatternOptions(QRegularExpression.PatternOptions options)'''
    def patternOptions(self):
        '''QRegularExpression.PatternOptions QRegularExpression.patternOptions()'''
        return QRegularExpression.PatternOptions()
    class MatchOptions():
        """"""
        def __init__(self):
            '''QRegularExpression.MatchOptions QRegularExpression.MatchOptions.__init__()'''
            return QRegularExpression.MatchOptions()
        def __init__(self):
            '''int QRegularExpression.MatchOptions.__init__()'''
            return int()
        def __init__(self):
            '''void QRegularExpression.MatchOptions.__init__()'''
        def __bool__(self):
            '''int QRegularExpression.MatchOptions.__bool__()'''
            return int()
        def __ne__(self, f):
            '''bool QRegularExpression.MatchOptions.__ne__(QRegularExpression.MatchOptions f)'''
            return bool()
        def __eq__(self, f):
            '''bool QRegularExpression.MatchOptions.__eq__(QRegularExpression.MatchOptions f)'''
            return bool()
        def __invert__(self):
            '''QRegularExpression.MatchOptions QRegularExpression.MatchOptions.__invert__()'''
            return QRegularExpression.MatchOptions()
        def __and__(self, mask):
            '''QRegularExpression.MatchOptions QRegularExpression.MatchOptions.__and__(int mask)'''
            return QRegularExpression.MatchOptions()
        def __xor__(self, f):
            '''QRegularExpression.MatchOptions QRegularExpression.MatchOptions.__xor__(QRegularExpression.MatchOptions f)'''
            return QRegularExpression.MatchOptions()
        def __xor__(self, f):
            '''QRegularExpression.MatchOptions QRegularExpression.MatchOptions.__xor__(int f)'''
            return QRegularExpression.MatchOptions()
        def __or__(self, f):
            '''QRegularExpression.MatchOptions QRegularExpression.MatchOptions.__or__(QRegularExpression.MatchOptions f)'''
            return QRegularExpression.MatchOptions()
        def __or__(self, f):
            '''QRegularExpression.MatchOptions QRegularExpression.MatchOptions.__or__(int f)'''
            return QRegularExpression.MatchOptions()
        def __int__(self):
            '''int QRegularExpression.MatchOptions.__int__()'''
            return int()
        def __ixor__(self, f):
            '''QRegularExpression.MatchOptions QRegularExpression.MatchOptions.__ixor__(QRegularExpression.MatchOptions f)'''
            return QRegularExpression.MatchOptions()
        def __ior__(self, f):
            '''QRegularExpression.MatchOptions QRegularExpression.MatchOptions.__ior__(QRegularExpression.MatchOptions f)'''
            return QRegularExpression.MatchOptions()
        def __iand__(self, mask):
            '''QRegularExpression.MatchOptions QRegularExpression.MatchOptions.__iand__(int mask)'''
            return QRegularExpression.MatchOptions()
    class PatternOptions():
        """"""
        def __init__(self):
            '''QRegularExpression.PatternOptions QRegularExpression.PatternOptions.__init__()'''
            return QRegularExpression.PatternOptions()
        def __init__(self):
            '''int QRegularExpression.PatternOptions.__init__()'''
            return int()
        def __init__(self):
            '''void QRegularExpression.PatternOptions.__init__()'''
        def __bool__(self):
            '''int QRegularExpression.PatternOptions.__bool__()'''
            return int()
        def __ne__(self, f):
            '''bool QRegularExpression.PatternOptions.__ne__(QRegularExpression.PatternOptions f)'''
            return bool()
        def __eq__(self, f):
            '''bool QRegularExpression.PatternOptions.__eq__(QRegularExpression.PatternOptions f)'''
            return bool()
        def __invert__(self):
            '''QRegularExpression.PatternOptions QRegularExpression.PatternOptions.__invert__()'''
            return QRegularExpression.PatternOptions()
        def __and__(self, mask):
            '''QRegularExpression.PatternOptions QRegularExpression.PatternOptions.__and__(int mask)'''
            return QRegularExpression.PatternOptions()
        def __xor__(self, f):
            '''QRegularExpression.PatternOptions QRegularExpression.PatternOptions.__xor__(QRegularExpression.PatternOptions f)'''
            return QRegularExpression.PatternOptions()
        def __xor__(self, f):
            '''QRegularExpression.PatternOptions QRegularExpression.PatternOptions.__xor__(int f)'''
            return QRegularExpression.PatternOptions()
        def __or__(self, f):
            '''QRegularExpression.PatternOptions QRegularExpression.PatternOptions.__or__(QRegularExpression.PatternOptions f)'''
            return QRegularExpression.PatternOptions()
        def __or__(self, f):
            '''QRegularExpression.PatternOptions QRegularExpression.PatternOptions.__or__(int f)'''
            return QRegularExpression.PatternOptions()
        def __int__(self):
            '''int QRegularExpression.PatternOptions.__int__()'''
            return int()
        def __ixor__(self, f):
            '''QRegularExpression.PatternOptions QRegularExpression.PatternOptions.__ixor__(QRegularExpression.PatternOptions f)'''
            return QRegularExpression.PatternOptions()
        def __ior__(self, f):
            '''QRegularExpression.PatternOptions QRegularExpression.PatternOptions.__ior__(QRegularExpression.PatternOptions f)'''
            return QRegularExpression.PatternOptions()
        def __iand__(self, mask):
            '''QRegularExpression.PatternOptions QRegularExpression.PatternOptions.__iand__(int mask)'''
            return QRegularExpression.PatternOptions()


class QRegularExpressionMatch():
    """"""
    def __init__(self):
        '''void QRegularExpressionMatch.__init__()'''
    def __init__(self, match):
        '''void QRegularExpressionMatch.__init__(QRegularExpressionMatch match)'''
    def capturedEnd(self, nth = 0):
        '''int QRegularExpressionMatch.capturedEnd(int nth = 0)'''
        return int()
    def capturedEnd(self, name):
        '''int QRegularExpressionMatch.capturedEnd(str name)'''
        return int()
    def capturedLength(self, nth = 0):
        '''int QRegularExpressionMatch.capturedLength(int nth = 0)'''
        return int()
    def capturedLength(self, name):
        '''int QRegularExpressionMatch.capturedLength(str name)'''
        return int()
    def capturedStart(self, nth = 0):
        '''int QRegularExpressionMatch.capturedStart(int nth = 0)'''
        return int()
    def capturedStart(self, name):
        '''int QRegularExpressionMatch.capturedStart(str name)'''
        return int()
    def capturedTexts(self):
        '''list-of-str QRegularExpressionMatch.capturedTexts()'''
        return [str()]
    def captured(self, nth = 0):
        '''str QRegularExpressionMatch.captured(int nth = 0)'''
        return str()
    def captured(self, name):
        '''str QRegularExpressionMatch.captured(str name)'''
        return str()
    def lastCapturedIndex(self):
        '''int QRegularExpressionMatch.lastCapturedIndex()'''
        return int()
    def isValid(self):
        '''bool QRegularExpressionMatch.isValid()'''
        return bool()
    def hasPartialMatch(self):
        '''bool QRegularExpressionMatch.hasPartialMatch()'''
        return bool()
    def hasMatch(self):
        '''bool QRegularExpressionMatch.hasMatch()'''
        return bool()
    def matchOptions(self):
        '''QRegularExpression.MatchOptions QRegularExpressionMatch.matchOptions()'''
        return QRegularExpression.MatchOptions()
    def matchType(self):
        '''QRegularExpression.MatchType QRegularExpressionMatch.matchType()'''
        return QRegularExpression.MatchType()
    def regularExpression(self):
        '''QRegularExpression QRegularExpressionMatch.regularExpression()'''
        return QRegularExpression()
    def swap(self, match):
        '''void QRegularExpressionMatch.swap(QRegularExpressionMatch match)'''


class QRegularExpressionMatchIterator():
    """"""
    def __init__(self):
        '''void QRegularExpressionMatchIterator.__init__()'''
    def __init__(self, iterator):
        '''void QRegularExpressionMatchIterator.__init__(QRegularExpressionMatchIterator iterator)'''
    def matchOptions(self):
        '''QRegularExpression.MatchOptions QRegularExpressionMatchIterator.matchOptions()'''
        return QRegularExpression.MatchOptions()
    def matchType(self):
        '''QRegularExpression.MatchType QRegularExpressionMatchIterator.matchType()'''
        return QRegularExpression.MatchType()
    def regularExpression(self):
        '''QRegularExpression QRegularExpressionMatchIterator.regularExpression()'''
        return QRegularExpression()
    def peekNext(self):
        '''QRegularExpressionMatch QRegularExpressionMatchIterator.peekNext()'''
        return QRegularExpressionMatch()
    def next(self):
        '''QRegularExpressionMatch QRegularExpressionMatchIterator.next()'''
        return QRegularExpressionMatch()
    def hasNext(self):
        '''bool QRegularExpressionMatchIterator.hasNext()'''
        return bool()
    def isValid(self):
        '''bool QRegularExpressionMatchIterator.isValid()'''
        return bool()
    def swap(self, iterator):
        '''void QRegularExpressionMatchIterator.swap(QRegularExpressionMatchIterator iterator)'''


class QResource():
    """"""
    def __init__(self, fileName = None, locale = QLocale()):
        '''void QResource.__init__(str fileName = '', QLocale locale = QLocale())'''
    def isFile(self):
        '''bool QResource.isFile()'''
        return bool()
    def isDir(self):
        '''bool QResource.isDir()'''
        return bool()
    def children(self):
        '''list-of-str QResource.children()'''
        return [str()]
    def unregisterResourceData(self, rccData, mapRoot = None):
        '''static bool QResource.unregisterResourceData(str rccData, str mapRoot = '')'''
        return bool()
    def unregisterResource(self, rccFileName, mapRoot = None):
        '''static bool QResource.unregisterResource(str rccFileName, str mapRoot = '')'''
        return bool()
    def registerResourceData(self, rccData, mapRoot = None):
        '''static bool QResource.registerResourceData(str rccData, str mapRoot = '')'''
        return bool()
    def registerResource(self, rccFileName, mapRoot = None):
        '''static bool QResource.registerResource(str rccFileName, str mapRoot = '')'''
        return bool()
    def size(self):
        '''int QResource.size()'''
        return int()
    def setLocale(self, locale):
        '''void QResource.setLocale(QLocale locale)'''
    def setFileName(self, file):
        '''void QResource.setFileName(str file)'''
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
        '''str QResource.fileName()'''
        return str()
    def data(self):
        '''str QResource.data()'''
        return str()
    def absoluteFilePath(self):
        '''str QResource.absoluteFilePath()'''
        return str()


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


class QSaveFile(QFileDevice):
    """"""
    def __init__(self, name):
        '''void QSaveFile.__init__(str name)'''
    def __init__(self, parent = None):
        '''void QSaveFile.__init__(QObject parent = None)'''
    def __init__(self, name, parent):
        '''void QSaveFile.__init__(str name, QObject parent)'''
    def writeData(self, data):
        '''int QSaveFile.writeData(str data)'''
        return int()
    def directWriteFallback(self):
        '''bool QSaveFile.directWriteFallback()'''
        return bool()
    def setDirectWriteFallback(self, enabled):
        '''void QSaveFile.setDirectWriteFallback(bool enabled)'''
    def cancelWriting(self):
        '''void QSaveFile.cancelWriting()'''
    def commit(self):
        '''bool QSaveFile.commit()'''
        return bool()
    def open(self, mode):
        '''bool QSaveFile.open(QIODevice.OpenMode mode)'''
        return bool()
    def setFileName(self, name):
        '''void QSaveFile.setFileName(str name)'''
    def fileName(self):
        '''str QSaveFile.fileName()'''
        return str()


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
    currentAnimationChanged = pyqtSignal() # void currentAnimationChanged(QAbstractAnimation*) - signal
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

    def __init__(self, organization, application = None, parent = None):
        '''void QSettings.__init__(str organization, str application = '', QObject parent = None)'''
    def __init__(self, scope, organization, application = None, parent = None):
        '''void QSettings.__init__(QSettings.Scope scope, str organization, str application = '', QObject parent = None)'''
    def __init__(self, format, scope, organization, application = None, parent = None):
        '''void QSettings.__init__(QSettings.Format format, QSettings.Scope scope, str organization, str application = '', QObject parent = None)'''
    def __init__(self, fileName, format, parent = None):
        '''void QSettings.__init__(str fileName, QSettings.Format format, QObject parent = None)'''
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
        '''str QSettings.applicationName()'''
        return str()
    def organizationName(self):
        '''str QSettings.organizationName()'''
        return str()
    def scope(self):
        '''QSettings.Scope QSettings.scope()'''
        return QSettings.Scope()
    def format(self):
        '''QSettings.Format QSettings.format()'''
        return QSettings.Format()
    def setPath(self, format, scope, path):
        '''static void QSettings.setPath(QSettings.Format format, QSettings.Scope scope, str path)'''
    def fileName(self):
        '''str QSettings.fileName()'''
        return str()
    def fallbacksEnabled(self):
        '''bool QSettings.fallbacksEnabled()'''
        return bool()
    def setFallbacksEnabled(self, b):
        '''void QSettings.setFallbacksEnabled(bool b)'''
    def contains(self, key):
        '''bool QSettings.contains(str key)'''
        return bool()
    def remove(self, key):
        '''void QSettings.remove(str key)'''
    def value(self, key, defaultValue = None, type = None):
        '''object QSettings.value(str key, QVariant defaultValue = None, object type = None)'''
        return object()
    def setValue(self, key, value):
        '''void QSettings.setValue(str key, QVariant value)'''
    def isWritable(self):
        '''bool QSettings.isWritable()'''
        return bool()
    def childGroups(self):
        '''list-of-str QSettings.childGroups()'''
        return [str()]
    def childKeys(self):
        '''list-of-str QSettings.childKeys()'''
        return [str()]
    def allKeys(self):
        '''list-of-str QSettings.allKeys()'''
        return [str()]
    def setArrayIndex(self, i):
        '''void QSettings.setArrayIndex(int i)'''
    def endArray(self):
        '''void QSettings.endArray()'''
    def beginWriteArray(self, prefix, size = None):
        '''void QSettings.beginWriteArray(str prefix, int size = -1)'''
    def beginReadArray(self, prefix):
        '''int QSettings.beginReadArray(str prefix)'''
        return int()
    def group(self):
        '''str QSettings.group()'''
        return str()
    def endGroup(self):
        '''void QSettings.endGroup()'''
    def beginGroup(self, prefix):
        '''void QSettings.beginGroup(str prefix)'''
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
        '''void QSharedMemory.__init__(str key, QObject parent = None)'''
    def nativeKey(self):
        '''str QSharedMemory.nativeKey()'''
        return str()
    def setNativeKey(self, key):
        '''void QSharedMemory.setNativeKey(str key)'''
    def errorString(self):
        '''str QSharedMemory.errorString()'''
        return str()
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
    def attach(self, mode = None):
        '''bool QSharedMemory.attach(QSharedMemory.AccessMode mode = QSharedMemory.ReadWrite)'''
        return bool()
    def size(self):
        '''int QSharedMemory.size()'''
        return int()
    def create(self, size, mode = None):
        '''bool QSharedMemory.create(int size, QSharedMemory.AccessMode mode = QSharedMemory.ReadWrite)'''
        return bool()
    def key(self):
        '''str QSharedMemory.key()'''
        return str()
    def setKey(self, key):
        '''void QSharedMemory.setKey(str key)'''


class QSignalMapper(QObject):
    """"""
    def __init__(self, parent = None):
        '''void QSignalMapper.__init__(QObject parent = None)'''
    def map(self):
        '''void QSignalMapper.map()'''
    def map(self, sender):
        '''void QSignalMapper.map(QObject sender)'''
    mapped = pyqtSignal() # void mapped(int) - signal
    mapped = pyqtSignal() # void mapped(const QStringamp;) - signal
    mapped = pyqtSignal() # void mapped(QWidget*) - signal
    mapped = pyqtSignal() # void mapped(QObject*) - signal
    def mapping(self, id):
        '''QObject QSignalMapper.mapping(int id)'''
        return QObject()
    def mapping(self, text):
        '''QObject QSignalMapper.mapping(str text)'''
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
        '''void QSignalMapper.setMapping(QObject sender, str text)'''
    def setMapping(self, sender, widget):
        '''void QSignalMapper.setMapping(QObject sender, QWidget widget)'''
    def setMapping(self, sender, object):
        '''void QSignalMapper.setMapping(QObject sender, QObject object)'''


class QSignalTransition(QAbstractTransition):
    """"""
    def __init__(self, sourceState = None):
        '''void QSignalTransition.__init__(QState sourceState = None)'''
    def __init__(self, signal, sourceState = None):
        '''void QSignalTransition.__init__(signal signal, QState sourceState = None)'''
    signalChanged = pyqtSignal() # void signalChanged() - signal
    senderObjectChanged = pyqtSignal() # void senderObjectChanged() - signal
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
    def transposed(self):
        '''QSize QSize.transposed()'''
        return QSize()
    def scaled(self, s, mode):
        '''QSize QSize.scaled(QSize s, Qt.AspectRatioMode mode)'''
        return QSize()
    def scaled(self, w, h, mode):
        '''QSize QSize.scaled(int w, int h, Qt.AspectRatioMode mode)'''
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
    def transposed(self):
        '''QSizeF QSizeF.transposed()'''
        return QSizeF()
    def scaled(self, s, mode):
        '''QSizeF QSizeF.scaled(QSizeF s, Qt.AspectRatioMode mode)'''
        return QSizeF()
    def scaled(self, w, h, mode):
        '''QSizeF QSizeF.scaled(float w, float h, Qt.AspectRatioMode mode)'''
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

    def __init__(self, socket, parent = None):
        '''QSocketNotifier.Type QSocketNotifier.__init__(sip.voidptr socket, QObject parent = None)'''
        return QSocketNotifier.Type()
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
        '''sip.voidptr QSocketNotifier.socket()'''
        return sip.voidptr()


class QSortFilterProxyModel(QAbstractProxyModel):
    """"""
    def __init__(self, parent = None):
        '''void QSortFilterProxyModel.__init__(QObject parent = None)'''
    def invalidateFilter(self):
        '''void QSortFilterProxyModel.invalidateFilter()'''
    def invalidate(self):
        '''void QSortFilterProxyModel.invalidate()'''
    def sibling(self, row, column, idx):
        '''QModelIndex QSortFilterProxyModel.sibling(int row, int column, QModelIndex idx)'''
        return QModelIndex()
    def setSortLocaleAware(self, on):
        '''void QSortFilterProxyModel.setSortLocaleAware(bool on)'''
    def isSortLocaleAware(self):
        '''bool QSortFilterProxyModel.isSortLocaleAware()'''
        return bool()
    def supportedDropActions(self):
        '''Qt.DropActions QSortFilterProxyModel.supportedDropActions()'''
        return Qt.DropActions()
    def mimeTypes(self):
        '''list-of-str QSortFilterProxyModel.mimeTypes()'''
        return [str()]
    def setFilterRole(self, role):
        '''void QSortFilterProxyModel.setFilterRole(int role)'''
    def filterRole(self):
        '''int QSortFilterProxyModel.filterRole()'''
        return int()
    def sortOrder(self):
        '''Qt.SortOrder QSortFilterProxyModel.sortOrder()'''
        return Qt.SortOrder()
    def sortColumn(self):
        '''int QSortFilterProxyModel.sortColumn()'''
        return int()
    def setSortRole(self, role):
        '''void QSortFilterProxyModel.setSortRole(int role)'''
    def sortRole(self):
        '''int QSortFilterProxyModel.sortRole()'''
        return int()
    def setDynamicSortFilter(self, enable):
        '''void QSortFilterProxyModel.setDynamicSortFilter(bool enable)'''
    def dynamicSortFilter(self):
        '''bool QSortFilterProxyModel.dynamicSortFilter()'''
        return bool()
    def setSortCaseSensitivity(self, cs):
        '''void QSortFilterProxyModel.setSortCaseSensitivity(Qt.CaseSensitivity cs)'''
    def sortCaseSensitivity(self):
        '''Qt.CaseSensitivity QSortFilterProxyModel.sortCaseSensitivity()'''
        return Qt.CaseSensitivity()
    def sort(self, column, order = None):
        '''void QSortFilterProxyModel.sort(int column, Qt.SortOrder order = Qt.AscendingOrder)'''
    def match(self, start, role, value, hits = 1, flags = None):
        '''list-of-QModelIndex QSortFilterProxyModel.match(QModelIndex start, int role, QVariant value, int hits = 1, Qt.MatchFlags flags = Qt.MatchStartsWith|Qt.MatchWrap)'''
        return [QModelIndex()]
    def span(self, index):
        '''QSize QSortFilterProxyModel.span(QModelIndex index)'''
        return QSize()
    def buddy(self, index):
        '''QModelIndex QSortFilterProxyModel.buddy(QModelIndex index)'''
        return QModelIndex()
    def flags(self, index):
        '''Qt.ItemFlags QSortFilterProxyModel.flags(QModelIndex index)'''
        return Qt.ItemFlags()
    def canFetchMore(self, parent):
        '''bool QSortFilterProxyModel.canFetchMore(QModelIndex parent)'''
        return bool()
    def fetchMore(self, parent):
        '''void QSortFilterProxyModel.fetchMore(QModelIndex parent)'''
    def removeColumns(self, column, count, parent = QModelIndex()):
        '''bool QSortFilterProxyModel.removeColumns(int column, int count, QModelIndex parent = QModelIndex())'''
        return bool()
    def removeRows(self, row, count, parent = QModelIndex()):
        '''bool QSortFilterProxyModel.removeRows(int row, int count, QModelIndex parent = QModelIndex())'''
        return bool()
    def insertColumns(self, column, count, parent = QModelIndex()):
        '''bool QSortFilterProxyModel.insertColumns(int column, int count, QModelIndex parent = QModelIndex())'''
        return bool()
    def insertRows(self, row, count, parent = QModelIndex()):
        '''bool QSortFilterProxyModel.insertRows(int row, int count, QModelIndex parent = QModelIndex())'''
        return bool()
    def dropMimeData(self, data, action, row, column, parent):
        '''bool QSortFilterProxyModel.dropMimeData(QMimeData data, Qt.DropAction action, int row, int column, QModelIndex parent)'''
        return bool()
    def mimeData(self, indexes):
        '''QMimeData QSortFilterProxyModel.mimeData(list-of-QModelIndex indexes)'''
        return QMimeData()
    def setHeaderData(self, section, orientation, value, role = None):
        '''bool QSortFilterProxyModel.setHeaderData(int section, Qt.Orientation orientation, QVariant value, int role = Qt.EditRole)'''
        return bool()
    def headerData(self, section, orientation, role = None):
        '''QVariant QSortFilterProxyModel.headerData(int section, Qt.Orientation orientation, int role = Qt.DisplayRole)'''
        return QVariant()
    def setData(self, index, value, role = None):
        '''bool QSortFilterProxyModel.setData(QModelIndex index, QVariant value, int role = Qt.EditRole)'''
        return bool()
    def data(self, index, role = None):
        '''QVariant QSortFilterProxyModel.data(QModelIndex index, int role = Qt.DisplayRole)'''
        return QVariant()
    def hasChildren(self, parent = QModelIndex()):
        '''bool QSortFilterProxyModel.hasChildren(QModelIndex parent = QModelIndex())'''
        return bool()
    def columnCount(self, parent = QModelIndex()):
        '''int QSortFilterProxyModel.columnCount(QModelIndex parent = QModelIndex())'''
        return int()
    def rowCount(self, parent = QModelIndex()):
        '''int QSortFilterProxyModel.rowCount(QModelIndex parent = QModelIndex())'''
        return int()
    def parent(self, child):
        '''QModelIndex QSortFilterProxyModel.parent(QModelIndex child)'''
        return QModelIndex()
    def parent(self):
        '''QObject QSortFilterProxyModel.parent()'''
        return QObject()
    def index(self, row, column, parent = QModelIndex()):
        '''QModelIndex QSortFilterProxyModel.index(int row, int column, QModelIndex parent = QModelIndex())'''
        return QModelIndex()
    def lessThan(self, left, right):
        '''bool QSortFilterProxyModel.lessThan(QModelIndex left, QModelIndex right)'''
        return bool()
    def filterAcceptsColumn(self, source_column, source_parent):
        '''bool QSortFilterProxyModel.filterAcceptsColumn(int source_column, QModelIndex source_parent)'''
        return bool()
    def filterAcceptsRow(self, source_row, source_parent):
        '''bool QSortFilterProxyModel.filterAcceptsRow(int source_row, QModelIndex source_parent)'''
        return bool()
    def setFilterFixedString(self, pattern):
        '''void QSortFilterProxyModel.setFilterFixedString(str pattern)'''
    def setFilterWildcard(self, pattern):
        '''void QSortFilterProxyModel.setFilterWildcard(str pattern)'''
    def setFilterCaseSensitivity(self, cs):
        '''void QSortFilterProxyModel.setFilterCaseSensitivity(Qt.CaseSensitivity cs)'''
    def filterCaseSensitivity(self):
        '''Qt.CaseSensitivity QSortFilterProxyModel.filterCaseSensitivity()'''
        return Qt.CaseSensitivity()
    def setFilterKeyColumn(self, column):
        '''void QSortFilterProxyModel.setFilterKeyColumn(int column)'''
    def filterKeyColumn(self):
        '''int QSortFilterProxyModel.filterKeyColumn()'''
        return int()
    def setFilterRegExp(self, regExp):
        '''void QSortFilterProxyModel.setFilterRegExp(QRegExp regExp)'''
    def setFilterRegExp(self, pattern):
        '''void QSortFilterProxyModel.setFilterRegExp(str pattern)'''
    def filterRegExp(self):
        '''QRegExp QSortFilterProxyModel.filterRegExp()'''
        return QRegExp()
    def mapSelectionFromSource(self, sourceSelection):
        '''QItemSelection QSortFilterProxyModel.mapSelectionFromSource(QItemSelection sourceSelection)'''
        return QItemSelection()
    def mapSelectionToSource(self, proxySelection):
        '''QItemSelection QSortFilterProxyModel.mapSelectionToSource(QItemSelection proxySelection)'''
        return QItemSelection()
    def mapFromSource(self, sourceIndex):
        '''QModelIndex QSortFilterProxyModel.mapFromSource(QModelIndex sourceIndex)'''
        return QModelIndex()
    def mapToSource(self, proxyIndex):
        '''QModelIndex QSortFilterProxyModel.mapToSource(QModelIndex proxyIndex)'''
        return QModelIndex()
    def setSourceModel(self, sourceModel):
        '''void QSortFilterProxyModel.setSourceModel(QAbstractItemModel sourceModel)'''


class QStandardPaths():
    """"""
    # Enum QStandardPaths.LocateOption
    LocateFile = 0
    LocateDirectory = 0

    # Enum QStandardPaths.StandardLocation
    DesktopLocation = 0
    DocumentsLocation = 0
    FontsLocation = 0
    ApplicationsLocation = 0
    MusicLocation = 0
    MoviesLocation = 0
    PicturesLocation = 0
    TempLocation = 0
    HomeLocation = 0
    DataLocation = 0
    CacheLocation = 0
    GenericDataLocation = 0
    RuntimeLocation = 0
    ConfigLocation = 0
    DownloadLocation = 0
    GenericCacheLocation = 0
    GenericConfigLocation = 0
    AppDataLocation = 0
    AppLocalDataLocation = 0
    AppConfigLocation = 0

    def __init__(self):
        '''QStandardPaths QStandardPaths.__init__()'''
        return QStandardPaths()
    def setTestModeEnabled(self, testMode):
        '''static void QStandardPaths.setTestModeEnabled(bool testMode)'''
    def enableTestMode(self, testMode):
        '''static void QStandardPaths.enableTestMode(bool testMode)'''
    def findExecutable(self, executableName, paths = strList()):
        '''static str QStandardPaths.findExecutable(str executableName, list-of-str paths = strList())'''
        return str()
    def displayName(self, type):
        '''static str QStandardPaths.displayName(QStandardPaths.StandardLocation type)'''
        return str()
    def locateAll(self, type, fileName, options = None):
        '''static list-of-str QStandardPaths.locateAll(QStandardPaths.StandardLocation type, str fileName, QStandardPaths.LocateOptions options = QStandardPaths.LocateFile)'''
        return [str()]
    def locate(self, type, fileName, options = None):
        '''static str QStandardPaths.locate(QStandardPaths.StandardLocation type, str fileName, QStandardPaths.LocateOptions options = QStandardPaths.LocateFile)'''
        return str()
    def standardLocations(self, type):
        '''static list-of-str QStandardPaths.standardLocations(QStandardPaths.StandardLocation type)'''
        return [str()]
    def writableLocation(self, type):
        '''static str QStandardPaths.writableLocation(QStandardPaths.StandardLocation type)'''
        return str()
    class LocateOptions():
        """"""
        def __init__(self):
            '''QStandardPaths.LocateOptions QStandardPaths.LocateOptions.__init__()'''
            return QStandardPaths.LocateOptions()
        def __init__(self):
            '''int QStandardPaths.LocateOptions.__init__()'''
            return int()
        def __init__(self):
            '''void QStandardPaths.LocateOptions.__init__()'''
        def __bool__(self):
            '''int QStandardPaths.LocateOptions.__bool__()'''
            return int()
        def __ne__(self, f):
            '''bool QStandardPaths.LocateOptions.__ne__(QStandardPaths.LocateOptions f)'''
            return bool()
        def __eq__(self, f):
            '''bool QStandardPaths.LocateOptions.__eq__(QStandardPaths.LocateOptions f)'''
            return bool()
        def __invert__(self):
            '''QStandardPaths.LocateOptions QStandardPaths.LocateOptions.__invert__()'''
            return QStandardPaths.LocateOptions()
        def __and__(self, mask):
            '''QStandardPaths.LocateOptions QStandardPaths.LocateOptions.__and__(int mask)'''
            return QStandardPaths.LocateOptions()
        def __xor__(self, f):
            '''QStandardPaths.LocateOptions QStandardPaths.LocateOptions.__xor__(QStandardPaths.LocateOptions f)'''
            return QStandardPaths.LocateOptions()
        def __xor__(self, f):
            '''QStandardPaths.LocateOptions QStandardPaths.LocateOptions.__xor__(int f)'''
            return QStandardPaths.LocateOptions()
        def __or__(self, f):
            '''QStandardPaths.LocateOptions QStandardPaths.LocateOptions.__or__(QStandardPaths.LocateOptions f)'''
            return QStandardPaths.LocateOptions()
        def __or__(self, f):
            '''QStandardPaths.LocateOptions QStandardPaths.LocateOptions.__or__(int f)'''
            return QStandardPaths.LocateOptions()
        def __int__(self):
            '''int QStandardPaths.LocateOptions.__int__()'''
            return int()
        def __ixor__(self, f):
            '''QStandardPaths.LocateOptions QStandardPaths.LocateOptions.__ixor__(QStandardPaths.LocateOptions f)'''
            return QStandardPaths.LocateOptions()
        def __ior__(self, f):
            '''QStandardPaths.LocateOptions QStandardPaths.LocateOptions.__ior__(QStandardPaths.LocateOptions f)'''
            return QStandardPaths.LocateOptions()
        def __iand__(self, mask):
            '''QStandardPaths.LocateOptions QStandardPaths.LocateOptions.__iand__(int mask)'''
            return QStandardPaths.LocateOptions()


class QState(QAbstractState):
    """"""
    # Enum QState.RestorePolicy
    DontRestoreProperties = 0
    RestoreProperties = 0

    # Enum QState.ChildMode
    ExclusiveStates = 0
    ParallelStates = 0

    def __init__(self, parent = None):
        '''void QState.__init__(QState parent = None)'''
    def __init__(self, childMode, parent = None):
        '''void QState.__init__(QState.ChildMode childMode, QState parent = None)'''
    errorStateChanged = pyqtSignal() # void errorStateChanged() - signal
    initialStateChanged = pyqtSignal() # void initialStateChanged() - signal
    childModeChanged = pyqtSignal() # void childModeChanged() - signal
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

    # Enum QStateMachine.EventPriority
    NormalPriority = 0
    HighPriority = 0

    def __init__(self, parent = None):
        '''void QStateMachine.__init__(QObject parent = None)'''
    def __init__(self, childMode, parent = None):
        '''void QStateMachine.__init__(QState.ChildMode childMode, QObject parent = None)'''
    def event(self, e):
        '''bool QStateMachine.event(QEvent e)'''
        return bool()
    def onExit(self, event):
        '''void QStateMachine.onExit(QEvent event)'''
    def onEntry(self, event):
        '''void QStateMachine.onEntry(QEvent event)'''
    runningChanged = pyqtSignal() # void runningChanged(bool) - signal
    stopped = pyqtSignal() # void stopped() - signal
    started = pyqtSignal() # void started() - signal
    def setRunning(self, running):
        '''void QStateMachine.setRunning(bool running)'''
    def stop(self):
        '''void QStateMachine.stop()'''
    def start(self):
        '''void QStateMachine.start()'''
    def eventFilter(self, watched, event):
        '''bool QStateMachine.eventFilter(QObject watched, QEvent event)'''
        return bool()
    def configuration(self):
        '''set-of-QAbstractState QStateMachine.configuration()'''
        return set-of-QAbstractState()
    def cancelDelayedEvent(self, id):
        '''bool QStateMachine.cancelDelayedEvent(int id)'''
        return bool()
    def postDelayedEvent(self, event, delay):
        '''int QStateMachine.postDelayedEvent(QEvent event, int delay)'''
        return int()
    def postEvent(self, event, priority = None):
        '''void QStateMachine.postEvent(QEvent event, QStateMachine.EventPriority priority = QStateMachine.NormalPriority)'''
    def setGlobalRestorePolicy(self, restorePolicy):
        '''void QStateMachine.setGlobalRestorePolicy(QState.RestorePolicy restorePolicy)'''
    def globalRestorePolicy(self):
        '''QState.RestorePolicy QStateMachine.globalRestorePolicy()'''
        return QState.RestorePolicy()
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
        '''str QStateMachine.errorString()'''
        return str()
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


class QStorageInfo():
    """"""
    def __init__(self):
        '''void QStorageInfo.__init__()'''
    def __init__(self, path):
        '''void QStorageInfo.__init__(str path)'''
    def __init__(self, dir):
        '''void QStorageInfo.__init__(QDir dir)'''
    def __init__(self, other):
        '''void QStorageInfo.__init__(QStorageInfo other)'''
    def __eq__(self, second):
        '''bool QStorageInfo.__eq__(QStorageInfo second)'''
        return bool()
    def __ne__(self, second):
        '''bool QStorageInfo.__ne__(QStorageInfo second)'''
        return bool()
    def isRoot(self):
        '''bool QStorageInfo.isRoot()'''
        return bool()
    def root(self):
        '''static QStorageInfo QStorageInfo.root()'''
        return QStorageInfo()
    def mountedVolumes(self):
        '''static list-of-QStorageInfo QStorageInfo.mountedVolumes()'''
        return [QStorageInfo()]
    def refresh(self):
        '''void QStorageInfo.refresh()'''
    def isValid(self):
        '''bool QStorageInfo.isValid()'''
        return bool()
    def isReady(self):
        '''bool QStorageInfo.isReady()'''
        return bool()
    def isReadOnly(self):
        '''bool QStorageInfo.isReadOnly()'''
        return bool()
    def bytesAvailable(self):
        '''int QStorageInfo.bytesAvailable()'''
        return int()
    def bytesFree(self):
        '''int QStorageInfo.bytesFree()'''
        return int()
    def bytesTotal(self):
        '''int QStorageInfo.bytesTotal()'''
        return int()
    def displayName(self):
        '''str QStorageInfo.displayName()'''
        return str()
    def name(self):
        '''str QStorageInfo.name()'''
        return str()
    def fileSystemType(self):
        '''QByteArray QStorageInfo.fileSystemType()'''
        return QByteArray()
    def device(self):
        '''QByteArray QStorageInfo.device()'''
        return QByteArray()
    def rootPath(self):
        '''str QStorageInfo.rootPath()'''
        return str()
    def setPath(self, path):
        '''void QStorageInfo.setPath(str path)'''
    def swap(self, other):
        '''void QStorageInfo.swap(QStorageInfo other)'''


class QStringListModel(QAbstractListModel):
    """"""
    def __init__(self, parent = None):
        '''void QStringListModel.__init__(QObject parent = None)'''
    def __init__(self, strings, parent = None):
        '''void QStringListModel.__init__(list-of-str strings, QObject parent = None)'''
    def sibling(self, row, column, idx):
        '''QModelIndex QStringListModel.sibling(int row, int column, QModelIndex idx)'''
        return QModelIndex()
    def supportedDropActions(self):
        '''Qt.DropActions QStringListModel.supportedDropActions()'''
        return Qt.DropActions()
    def sort(self, column, order = None):
        '''void QStringListModel.sort(int column, Qt.SortOrder order = Qt.AscendingOrder)'''
    def setStringList(self, strings):
        '''void QStringListModel.setStringList(list-of-str strings)'''
    def stringList(self):
        '''list-of-str QStringListModel.stringList()'''
        return [str()]
    def removeRows(self, row, count, parent = QModelIndex()):
        '''bool QStringListModel.removeRows(int row, int count, QModelIndex parent = QModelIndex())'''
        return bool()
    def insertRows(self, row, count, parent = QModelIndex()):
        '''bool QStringListModel.insertRows(int row, int count, QModelIndex parent = QModelIndex())'''
        return bool()
    def flags(self, index):
        '''Qt.ItemFlags QStringListModel.flags(QModelIndex index)'''
        return Qt.ItemFlags()
    def setData(self, index, value, role = None):
        '''bool QStringListModel.setData(QModelIndex index, QVariant value, int role = Qt.EditRole)'''
        return bool()
    def data(self, index, role):
        '''QVariant QStringListModel.data(QModelIndex index, int role)'''
        return QVariant()
    def rowCount(self, parent = QModelIndex()):
        '''int QStringListModel.rowCount(QModelIndex parent = QModelIndex())'''
        return int()


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

    def __init__(self, key, initialValue = 0, mode = None):
        '''void QSystemSemaphore.__init__(str key, int initialValue = 0, QSystemSemaphore.AccessMode mode = QSystemSemaphore.Open)'''
    def errorString(self):
        '''str QSystemSemaphore.errorString()'''
        return str()
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
        '''str QSystemSemaphore.key()'''
        return str()
    def setKey(self, key, initialValue = 0, mode = None):
        '''void QSystemSemaphore.setKey(str key, int initialValue = 0, QSystemSemaphore.AccessMode mode = QSystemSemaphore.Open)'''


class QTemporaryDir():
    """"""
    def __init__(self):
        '''void QTemporaryDir.__init__()'''
    def __init__(self, templateName):
        '''void QTemporaryDir.__init__(str templateName)'''
    def path(self):
        '''str QTemporaryDir.path()'''
        return str()
    def remove(self):
        '''bool QTemporaryDir.remove()'''
        return bool()
    def setAutoRemove(self, b):
        '''void QTemporaryDir.setAutoRemove(bool b)'''
    def autoRemove(self):
        '''bool QTemporaryDir.autoRemove()'''
        return bool()
    def isValid(self):
        '''bool QTemporaryDir.isValid()'''
        return bool()


class QTemporaryFile(QFile):
    """"""
    def __init__(self):
        '''void QTemporaryFile.__init__()'''
    def __init__(self, templateName):
        '''void QTemporaryFile.__init__(str templateName)'''
    def __init__(self, parent):
        '''void QTemporaryFile.__init__(QObject parent)'''
    def __init__(self, templateName, parent):
        '''void QTemporaryFile.__init__(str templateName, QObject parent)'''
    def createNativeFile(self, fileName):
        '''static QTemporaryFile QTemporaryFile.createNativeFile(str fileName)'''
        return QTemporaryFile()
    def createNativeFile(self, file):
        '''static QTemporaryFile QTemporaryFile.createNativeFile(QFile file)'''
        return QTemporaryFile()
    def setFileTemplate(self, name):
        '''void QTemporaryFile.setFileTemplate(str name)'''
    def fileTemplate(self):
        '''str QTemporaryFile.fileTemplate()'''
        return str()
    def fileName(self):
        '''str QTemporaryFile.fileName()'''
        return str()
    def open(self):
        '''bool QTemporaryFile.open()'''
        return bool()
    def open(self, mode):
        '''bool QTemporaryFile.open(QIODevice.OpenMode mode)'''
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
    SoftHyphen = 0
    BreakOpportunity = 0
    StartOfItem = 0
    EndOfItem = 0
    MandatoryBreak = 0

    def __init__(self):
        '''void QTextBoundaryFinder.__init__()'''
    def __init__(self, other):
        '''void QTextBoundaryFinder.__init__(QTextBoundaryFinder other)'''
    def __init__(self, type, string):
        '''void QTextBoundaryFinder.__init__(QTextBoundaryFinder.BoundaryType type, str string)'''
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
        '''str QTextBoundaryFinder.string()'''
        return str()
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
    def convertToUnicode(self, in_, state):
        '''abstract str QTextCodec.convertToUnicode(str in, QTextCodec.ConverterState state)'''
        return str()
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
        '''QByteArray QTextCodec.fromUnicode(str uc)'''
        return QByteArray()
    def toUnicode(self):
        '''QByteArray QTextCodec.toUnicode()'''
        return QByteArray()
    def toUnicode(self, chars):
        '''str QTextCodec.toUnicode(str chars)'''
        return str()
    def toUnicode(self, in_, state = None):
        '''str QTextCodec.toUnicode(str in, QTextCodec.ConverterState state = None)'''
        return str()
    def canEncode(self):
        '''str QTextCodec.canEncode()'''
        return str()
    def makeEncoder(self, flags = None):
        '''QTextEncoder QTextCodec.makeEncoder(QTextCodec.ConversionFlags flags = QTextCodec.DefaultConversion)'''
        return QTextEncoder()
    def makeDecoder(self, flags = None):
        '''QTextDecoder QTextCodec.makeDecoder(QTextCodec.ConversionFlags flags = QTextCodec.DefaultConversion)'''
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
        def __init__(self, flags = None):
            '''void QTextCodec.ConverterState.__init__(QTextCodec.ConversionFlags flags = QTextCodec.DefaultConversion)'''


class QTextEncoder():
    """"""
    def __init__(self, codec):
        '''void QTextEncoder.__init__(QTextCodec codec)'''
    def __init__(self, codec, flags):
        '''void QTextEncoder.__init__(QTextCodec codec, QTextCodec.ConversionFlags flags)'''
    def fromUnicode(self, str):
        '''QByteArray QTextEncoder.fromUnicode(str str)'''
        return QByteArray()


class QTextDecoder():
    """"""
    def __init__(self, codec):
        '''void QTextDecoder.__init__(QTextCodec codec)'''
    def __init__(self, codec, flags):
        '''void QTextDecoder.__init__(QTextCodec codec, QTextCodec.ConversionFlags flags)'''
    def toUnicode(self, chars):
        '''str QTextDecoder.toUnicode(str chars)'''
        return str()
    def toUnicode(self, ba):
        '''str QTextDecoder.toUnicode(QByteArray ba)'''
        return str()


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
    def __init__(self, array, mode = None):
        '''void QTextStream.__init__(QByteArray array, QIODevice.OpenMode mode = QIODevice.ReadWrite)'''
    def locale(self):
        '''QLocale QTextStream.locale()'''
        return QLocale()
    def setLocale(self, locale):
        '''void QTextStream.setLocale(QLocale locale)'''
    def __lshift__(self, f):
        '''QTextStream QTextStream.__lshift__(float f)'''
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
        '''QTextStream QTextStream.__lshift__(str s)'''
        return QTextStream()
    def __lshift__(self, array):
        '''QTextStream QTextStream.__lshift__(QByteArray array)'''
        return QTextStream()
    def __lshift__(self, m):
        '''QTextStream QTextStream.__lshift__(QTextStreamManipulator m)'''
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
        '''str QTextStream.padChar()'''
        return str()
    def setPadChar(self, ch):
        '''void QTextStream.setPadChar(str ch)'''
    def fieldAlignment(self):
        '''QTextStream.FieldAlignment QTextStream.fieldAlignment()'''
        return QTextStream.FieldAlignment()
    def setFieldAlignment(self, alignment):
        '''void QTextStream.setFieldAlignment(QTextStream.FieldAlignment alignment)'''
    def readAll(self):
        '''str QTextStream.readAll()'''
        return str()
    def readLine(self, maxLength = 0):
        '''str QTextStream.readLine(int maxLength = 0)'''
        return str()
    def read(self, maxlen):
        '''str QTextStream.read(int maxlen)'''
        return str()
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
    def loopLevel(self):
        '''int QThread.loopLevel()'''
        return int()
    def isInterruptionRequested(self):
        '''bool QThread.isInterruptionRequested()'''
        return bool()
    def requestInterruption(self):
        '''void QThread.requestInterruption()'''
    def setEventDispatcher(self, eventDispatcher):
        '''void QThread.setEventDispatcher(QAbstractEventDispatcher eventDispatcher)'''
    def eventDispatcher(self):
        '''QAbstractEventDispatcher QThread.eventDispatcher()'''
        return QAbstractEventDispatcher()
    def usleep(self):
        '''static int QThread.usleep()'''
        return int()
    def msleep(self):
        '''static int QThread.msleep()'''
        return int()
    def sleep(self):
        '''static int QThread.sleep()'''
        return int()
    def event(self, event):
        '''bool QThread.event(QEvent event)'''
        return bool()
    def setTerminationEnabled(self, enabled = True):
        '''static void QThread.setTerminationEnabled(bool enabled = True)'''
    def exec_(self):
        '''int QThread.exec_()'''
        return int()
    def run(self):
        '''void QThread.run()'''
    finished = pyqtSignal() # void finished() - signal
    started = pyqtSignal() # void started() - signal
    def wait(self, msecs = None):
        '''bool QThread.wait(int msecs = ULONG_MAX)'''
        return bool()
    def quit(self):
        '''void QThread.quit()'''
    def terminate(self):
        '''void QThread.terminate()'''
    def start(self, priority = None):
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
        '''static sip.voidptr QThread.currentThreadId()'''
        return sip.voidptr()
    def currentThread(self):
        '''static QThread QThread.currentThread()'''
        return QThread()


class QThreadPool(QObject):
    """"""
    def __init__(self, parent = None):
        '''void QThreadPool.__init__(QObject parent = None)'''
    def cancel(self, runnable):
        '''void QThreadPool.cancel(QRunnable runnable)'''
    def clear(self):
        '''void QThreadPool.clear()'''
    def waitForDone(self, msecs = None):
        '''bool QThreadPool.waitForDone(int msecs = -1)'''
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
    def remainingTime(self):
        '''int QTimer.remainingTime()'''
        return int()
    def timerType(self):
        '''Qt.TimerType QTimer.timerType()'''
        return Qt.TimerType()
    def setTimerType(self, atype):
        '''void QTimer.setTimerType(Qt.TimerType atype)'''
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
    def singleShot(self, msec, slot):
        '''static void QTimer.singleShot(int msec, callable-or-signal slot)'''
    def singleShot(self, msec, timerType, slot):
        '''static void QTimer.singleShot(int msec, Qt.TimerType timerType, callable-or-signal slot)'''
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


class QTimeZone():
    """"""
    # Enum QTimeZone.NameType
    DefaultName = 0
    LongName = 0
    ShortName = 0
    OffsetName = 0

    # Enum QTimeZone.TimeType
    StandardTime = 0
    DaylightTime = 0
    GenericTime = 0

    def __init__(self):
        '''void QTimeZone.__init__()'''
    def __init__(self, ianaId):
        '''void QTimeZone.__init__(QByteArray ianaId)'''
    def __init__(self, offsetSeconds):
        '''void QTimeZone.__init__(int offsetSeconds)'''
    def __init__(self, zoneId, offsetSeconds, name, abbreviation, country = None, comment = str()):
        '''void QTimeZone.__init__(QByteArray zoneId, int offsetSeconds, str name, str abbreviation, QLocale.Country country = QLocale.AnyCountry, str comment = str())'''
    def __init__(self, other):
        '''void QTimeZone.__init__(QTimeZone other)'''
    def utc(self):
        '''static QTimeZone QTimeZone.utc()'''
        return QTimeZone()
    def systemTimeZone(self):
        '''static QTimeZone QTimeZone.systemTimeZone()'''
        return QTimeZone()
    def windowsIdToIanaIds(self, windowsId):
        '''static list-of-QByteArray QTimeZone.windowsIdToIanaIds(QByteArray windowsId)'''
        return [QByteArray()]
    def windowsIdToIanaIds(self, windowsId, country):
        '''static list-of-QByteArray QTimeZone.windowsIdToIanaIds(QByteArray windowsId, QLocale.Country country)'''
        return [QByteArray()]
    def windowsIdToDefaultIanaId(self, windowsId):
        '''static QByteArray QTimeZone.windowsIdToDefaultIanaId(QByteArray windowsId)'''
        return QByteArray()
    def windowsIdToDefaultIanaId(self, windowsId, country):
        '''static QByteArray QTimeZone.windowsIdToDefaultIanaId(QByteArray windowsId, QLocale.Country country)'''
        return QByteArray()
    def ianaIdToWindowsId(self, ianaId):
        '''static QByteArray QTimeZone.ianaIdToWindowsId(QByteArray ianaId)'''
        return QByteArray()
    def availableTimeZoneIds(self):
        '''static list-of-QByteArray QTimeZone.availableTimeZoneIds()'''
        return [QByteArray()]
    def availableTimeZoneIds(self, country):
        '''static list-of-QByteArray QTimeZone.availableTimeZoneIds(QLocale.Country country)'''
        return [QByteArray()]
    def availableTimeZoneIds(self, offsetSeconds):
        '''static list-of-QByteArray QTimeZone.availableTimeZoneIds(int offsetSeconds)'''
        return [QByteArray()]
    def isTimeZoneIdAvailable(self, ianaId):
        '''static bool QTimeZone.isTimeZoneIdAvailable(QByteArray ianaId)'''
        return bool()
    def systemTimeZoneId(self):
        '''static QByteArray QTimeZone.systemTimeZoneId()'''
        return QByteArray()
    def transitions(self, fromDateTime, toDateTime):
        '''list-of-QTimeZone.OffsetData QTimeZone.transitions(QDateTime fromDateTime, QDateTime toDateTime)'''
        return [QTimeZone.OffsetData()]
    def previousTransition(self, beforeDateTime):
        '''QTimeZone.OffsetData QTimeZone.previousTransition(QDateTime beforeDateTime)'''
        return QTimeZone.OffsetData()
    def nextTransition(self, afterDateTime):
        '''QTimeZone.OffsetData QTimeZone.nextTransition(QDateTime afterDateTime)'''
        return QTimeZone.OffsetData()
    def hasTransitions(self):
        '''bool QTimeZone.hasTransitions()'''
        return bool()
    def offsetData(self, forDateTime):
        '''QTimeZone.OffsetData QTimeZone.offsetData(QDateTime forDateTime)'''
        return QTimeZone.OffsetData()
    def isDaylightTime(self, atDateTime):
        '''bool QTimeZone.isDaylightTime(QDateTime atDateTime)'''
        return bool()
    def hasDaylightTime(self):
        '''bool QTimeZone.hasDaylightTime()'''
        return bool()
    def daylightTimeOffset(self, atDateTime):
        '''int QTimeZone.daylightTimeOffset(QDateTime atDateTime)'''
        return int()
    def standardTimeOffset(self, atDateTime):
        '''int QTimeZone.standardTimeOffset(QDateTime atDateTime)'''
        return int()
    def offsetFromUtc(self, atDateTime):
        '''int QTimeZone.offsetFromUtc(QDateTime atDateTime)'''
        return int()
    def abbreviation(self, atDateTime):
        '''str QTimeZone.abbreviation(QDateTime atDateTime)'''
        return str()
    def displayName(self, atDateTime, nameType = None, locale = QLocale()):
        '''str QTimeZone.displayName(QDateTime atDateTime, QTimeZone.NameType nameType = QTimeZone.DefaultName, QLocale locale = QLocale())'''
        return str()
    def displayName(self, timeType, nameType = None, locale = QLocale()):
        '''str QTimeZone.displayName(QTimeZone.TimeType timeType, QTimeZone.NameType nameType = QTimeZone.DefaultName, QLocale locale = QLocale())'''
        return str()
    def comment(self):
        '''str QTimeZone.comment()'''
        return str()
    def country(self):
        '''QLocale.Country QTimeZone.country()'''
        return QLocale.Country()
    def id(self):
        '''QByteArray QTimeZone.id()'''
        return QByteArray()
    def isValid(self):
        '''bool QTimeZone.isValid()'''
        return bool()
    def __ne__(self, other):
        '''bool QTimeZone.__ne__(QTimeZone other)'''
        return bool()
    def __eq__(self, other):
        '''bool QTimeZone.__eq__(QTimeZone other)'''
        return bool()
    def swap(self, other):
        '''void QTimeZone.swap(QTimeZone other)'''
    class OffsetData():
        """"""
        abbreviation = None # str - member
        atUtc = None # QDateTime - member
        daylightTimeOffset = None # int - member
        offsetFromUtc = None # int - member
        standardTimeOffset = None # int - member
        def __init__(self):
            '''void QTimeZone.OffsetData.__init__()'''
        def __init__(self):
            '''QTimeZone.OffsetData QTimeZone.OffsetData.__init__()'''
            return QTimeZone.OffsetData()


class QTranslator(QObject):
    """"""
    def __init__(self, parent = None):
        '''void QTranslator.__init__(QObject parent = None)'''
    def loadFromData(self, data, directory = str()):
        '''bool QTranslator.loadFromData(str data, str directory = str())'''
        return bool()
    def load(self, fileName, directory = None, searchDelimiters = None, suffix = None):
        '''bool QTranslator.load(str fileName, str directory = '', str searchDelimiters = '', str suffix = '')'''
        return bool()
    def load(self, locale, fileName, prefix = None, directory = None, suffix = None):
        '''bool QTranslator.load(QLocale locale, str fileName, str prefix = '', str directory = '', str suffix = '')'''
        return bool()
    def isEmpty(self):
        '''bool QTranslator.isEmpty()'''
        return bool()
    def translate(self, context, sourceText, disambiguation = None, n = None):
        '''str QTranslator.translate(str context, str sourceText, str disambiguation = None, int n = -1)'''
        return str()


class QUrl():
    """"""
    # Enum QUrl.UserInputResolutionOption
    DefaultResolution = 0
    AssumeLocalFile = 0

    # Enum QUrl.ComponentFormattingOption
    PrettyDecoded = 0
    EncodeSpaces = 0
    EncodeUnicode = 0
    EncodeDelimiters = 0
    EncodeReserved = 0
    DecodeReserved = 0
    FullyEncoded = 0
    FullyDecoded = 0

    # Enum QUrl.UrlFormattingOption
    __kdevpythondocumentation_builtin_None = 0
    RemoveScheme = 0
    RemovePassword = 0
    RemoveUserInfo = 0
    RemovePort = 0
    RemoveAuthority = 0
    RemovePath = 0
    RemoveQuery = 0
    RemoveFragment = 0
    PreferLocalFile = 0
    StripTrailingSlash = 0
    RemoveFilename = 0
    NormalizePathSegments = 0

    # Enum QUrl.ParsingMode
    TolerantMode = 0
    StrictMode = 0
    DecodedMode = 0

    def __init__(self):
        '''void QUrl.__init__()'''
    def __init__(self, url, mode = None):
        '''void QUrl.__init__(str url, QUrl.ParsingMode mode = QUrl.TolerantMode)'''
    def __init__(self, copy):
        '''void QUrl.__init__(QUrl copy)'''
    def __ge__(self, url):
        '''bool QUrl.__ge__(QUrl url)'''
        return bool()
    def matches(self, url, options):
        '''bool QUrl.matches(QUrl url, QUrl.FormattingOptions options)'''
        return bool()
    def fileName(self, options = None):
        '''str QUrl.fileName(QUrl.ComponentFormattingOptions options = QUrl.FullyDecoded)'''
        return str()
    def adjusted(self, options):
        '''QUrl QUrl.adjusted(QUrl.FormattingOptions options)'''
        return QUrl()
    def fromStringList(self, uris, mode = None):
        '''static list-of-QUrl QUrl.fromStringList(list-of-str uris, QUrl.ParsingMode mode = QUrl.TolerantMode)'''
        return [QUrl()]
    def toStringList(self, uris, options = None):
        '''static list-of-str QUrl.toStringList(list-of-QUrl uris, QUrl.FormattingOptions options = QUrl.PrettyDecoded)'''
        return [str()]
    def query(self, options = None):
        '''str QUrl.query(QUrl.ComponentFormattingOptions options = QUrl.PrettyDecoded)'''
        return str()
    def setQuery(self, query, mode = None):
        '''void QUrl.setQuery(str query, QUrl.ParsingMode mode = QUrl.TolerantMode)'''
    def setQuery(self, query):
        '''void QUrl.setQuery(QUrlQuery query)'''
    def toDisplayString(self, options = None):
        '''str QUrl.toDisplayString(QUrl.FormattingOptions options = QUrl.PrettyDecoded)'''
        return str()
    def isLocalFile(self):
        '''bool QUrl.isLocalFile()'''
        return bool()
    def topLevelDomain(self, options = None):
        '''str QUrl.topLevelDomain(QUrl.ComponentFormattingOptions options = QUrl.FullyDecoded)'''
        return str()
    def swap(self, other):
        '''void QUrl.swap(QUrl other)'''
    def fromUserInput(self, userInput):
        '''static QUrl QUrl.fromUserInput(str userInput)'''
        return QUrl()
    def fromUserInput(self, userInput, workingDirectory, options = None):
        '''static QUrl QUrl.fromUserInput(str userInput, str workingDirectory, QUrl.UserInputResolutionOptions options = QUrl.DefaultResolution)'''
        return QUrl()
    def setIdnWhitelist(self):
        '''static list-of-str QUrl.setIdnWhitelist()'''
        return [str()]
    def idnWhitelist(self):
        '''static list-of-str QUrl.idnWhitelist()'''
        return [str()]
    def toAce(self):
        '''static str QUrl.toAce()'''
        return str()
    def fromAce(self):
        '''static QByteArray QUrl.fromAce()'''
        return QByteArray()
    def errorString(self):
        '''str QUrl.errorString()'''
        return str()
    def hasFragment(self):
        '''bool QUrl.hasFragment()'''
        return bool()
    def hasQuery(self):
        '''bool QUrl.hasQuery()'''
        return bool()
    def toPercentEncoding(self, input, exclude = QByteArray(), include = QByteArray()):
        '''static QByteArray QUrl.toPercentEncoding(str input, QByteArray exclude = QByteArray(), QByteArray include = QByteArray())'''
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
    def fromEncoded(self, u, mode = None):
        '''static QUrl QUrl.fromEncoded(QByteArray u, QUrl.ParsingMode mode = QUrl.TolerantMode)'''
        return QUrl()
    def toEncoded(self, options = None):
        '''QByteArray QUrl.toEncoded(QUrl.FormattingOptions options = QUrl.FullyEncoded)'''
        return QByteArray()
    def toString(self, options = None):
        '''str QUrl.toString(QUrl.FormattingOptions options = QUrl.PrettyDecoded)'''
        return str()
    def toLocalFile(self):
        '''str QUrl.toLocalFile()'''
        return str()
    def fromLocalFile(self, localfile):
        '''static QUrl QUrl.fromLocalFile(str localfile)'''
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
    def fragment(self, options = None):
        '''str QUrl.fragment(QUrl.ComponentFormattingOptions options = QUrl.PrettyDecoded)'''
        return str()
    def setFragment(self, fragment, mode = None):
        '''void QUrl.setFragment(str fragment, QUrl.ParsingMode mode = QUrl.TolerantMode)'''
    def path(self, options = None):
        '''str QUrl.path(QUrl.ComponentFormattingOptions options = QUrl.FullyDecoded)'''
        return str()
    def setPath(self, path, mode = None):
        '''void QUrl.setPath(str path, QUrl.ParsingMode mode = QUrl.DecodedMode)'''
    def port(self, defaultPort = None):
        '''int QUrl.port(int defaultPort = -1)'''
        return int()
    def setPort(self, port):
        '''void QUrl.setPort(int port)'''
    def host(self, options = None):
        '''str QUrl.host(QUrl.ComponentFormattingOptions options = QUrl.FullyDecoded)'''
        return str()
    def setHost(self, host, mode = None):
        '''void QUrl.setHost(str host, QUrl.ParsingMode mode = QUrl.DecodedMode)'''
    def password(self, options = None):
        '''str QUrl.password(QUrl.ComponentFormattingOptions options = QUrl.FullyDecoded)'''
        return str()
    def setPassword(self, password, mode = None):
        '''void QUrl.setPassword(str password, QUrl.ParsingMode mode = QUrl.DecodedMode)'''
    def userName(self, options = None):
        '''str QUrl.userName(QUrl.ComponentFormattingOptions options = QUrl.FullyDecoded)'''
        return str()
    def setUserName(self, userName, mode = None):
        '''void QUrl.setUserName(str userName, QUrl.ParsingMode mode = QUrl.DecodedMode)'''
    def userInfo(self, options = None):
        '''str QUrl.userInfo(QUrl.ComponentFormattingOptions options = QUrl.PrettyDecoded)'''
        return str()
    def setUserInfo(self, userInfo, mode = None):
        '''void QUrl.setUserInfo(str userInfo, QUrl.ParsingMode mode = QUrl.TolerantMode)'''
    def authority(self, options = None):
        '''str QUrl.authority(QUrl.ComponentFormattingOptions options = QUrl.PrettyDecoded)'''
        return str()
    def setAuthority(self, authority, mode = None):
        '''void QUrl.setAuthority(str authority, QUrl.ParsingMode mode = QUrl.TolerantMode)'''
    def scheme(self):
        '''str QUrl.scheme()'''
        return str()
    def setScheme(self, scheme):
        '''void QUrl.setScheme(str scheme)'''
    def clear(self):
        '''void QUrl.clear()'''
    def isEmpty(self):
        '''bool QUrl.isEmpty()'''
        return bool()
    def isValid(self):
        '''bool QUrl.isValid()'''
        return bool()
    def setUrl(self, url, mode = None):
        '''void QUrl.setUrl(str url, QUrl.ParsingMode mode = QUrl.TolerantMode)'''
    def url(self, options = None):
        '''str QUrl.url(QUrl.FormattingOptions options = QUrl.PrettyDecoded)'''
        return str()
    def __repr__(self):
        '''str QUrl.__repr__()'''
        return str()
    def __hash__(self):
        '''int QUrl.__hash__()'''
        return int()
    class ComponentFormattingOptions():
        """"""
        def __init__(self):
            '''QUrl.ComponentFormattingOptions QUrl.ComponentFormattingOptions.__init__()'''
            return QUrl.ComponentFormattingOptions()
        def __init__(self):
            '''int QUrl.ComponentFormattingOptions.__init__()'''
            return int()
        def __init__(self):
            '''void QUrl.ComponentFormattingOptions.__init__()'''
        def __bool__(self):
            '''int QUrl.ComponentFormattingOptions.__bool__()'''
            return int()
        def __ne__(self, f):
            '''bool QUrl.ComponentFormattingOptions.__ne__(QUrl.ComponentFormattingOptions f)'''
            return bool()
        def __eq__(self, f):
            '''bool QUrl.ComponentFormattingOptions.__eq__(QUrl.ComponentFormattingOptions f)'''
            return bool()
        def __invert__(self):
            '''QUrl.ComponentFormattingOptions QUrl.ComponentFormattingOptions.__invert__()'''
            return QUrl.ComponentFormattingOptions()
        def __and__(self, mask):
            '''QUrl.ComponentFormattingOptions QUrl.ComponentFormattingOptions.__and__(int mask)'''
            return QUrl.ComponentFormattingOptions()
        def __xor__(self, f):
            '''QUrl.ComponentFormattingOptions QUrl.ComponentFormattingOptions.__xor__(QUrl.ComponentFormattingOptions f)'''
            return QUrl.ComponentFormattingOptions()
        def __xor__(self, f):
            '''QUrl.ComponentFormattingOptions QUrl.ComponentFormattingOptions.__xor__(int f)'''
            return QUrl.ComponentFormattingOptions()
        def __or__(self, f):
            '''QUrl.ComponentFormattingOptions QUrl.ComponentFormattingOptions.__or__(QUrl.ComponentFormattingOptions f)'''
            return QUrl.ComponentFormattingOptions()
        def __or__(self, f):
            '''QUrl.ComponentFormattingOptions QUrl.ComponentFormattingOptions.__or__(int f)'''
            return QUrl.ComponentFormattingOptions()
        def __int__(self):
            '''int QUrl.ComponentFormattingOptions.__int__()'''
            return int()
        def __ixor__(self, f):
            '''QUrl.ComponentFormattingOptions QUrl.ComponentFormattingOptions.__ixor__(QUrl.ComponentFormattingOptions f)'''
            return QUrl.ComponentFormattingOptions()
        def __ior__(self, f):
            '''QUrl.ComponentFormattingOptions QUrl.ComponentFormattingOptions.__ior__(QUrl.ComponentFormattingOptions f)'''
            return QUrl.ComponentFormattingOptions()
        def __iand__(self, mask):
            '''QUrl.ComponentFormattingOptions QUrl.ComponentFormattingOptions.__iand__(int mask)'''
            return QUrl.ComponentFormattingOptions()
    class UserInputResolutionOptions():
        """"""
        def __init__(self):
            '''QUrl.UserInputResolutionOptions QUrl.UserInputResolutionOptions.__init__()'''
            return QUrl.UserInputResolutionOptions()
        def __init__(self):
            '''int QUrl.UserInputResolutionOptions.__init__()'''
            return int()
        def __init__(self):
            '''void QUrl.UserInputResolutionOptions.__init__()'''
        def __bool__(self):
            '''int QUrl.UserInputResolutionOptions.__bool__()'''
            return int()
        def __ne__(self, f):
            '''bool QUrl.UserInputResolutionOptions.__ne__(QUrl.UserInputResolutionOptions f)'''
            return bool()
        def __eq__(self, f):
            '''bool QUrl.UserInputResolutionOptions.__eq__(QUrl.UserInputResolutionOptions f)'''
            return bool()
        def __invert__(self):
            '''QUrl.UserInputResolutionOptions QUrl.UserInputResolutionOptions.__invert__()'''
            return QUrl.UserInputResolutionOptions()
        def __and__(self, mask):
            '''QUrl.UserInputResolutionOptions QUrl.UserInputResolutionOptions.__and__(int mask)'''
            return QUrl.UserInputResolutionOptions()
        def __xor__(self, f):
            '''QUrl.UserInputResolutionOptions QUrl.UserInputResolutionOptions.__xor__(QUrl.UserInputResolutionOptions f)'''
            return QUrl.UserInputResolutionOptions()
        def __xor__(self, f):
            '''QUrl.UserInputResolutionOptions QUrl.UserInputResolutionOptions.__xor__(int f)'''
            return QUrl.UserInputResolutionOptions()
        def __or__(self, f):
            '''QUrl.UserInputResolutionOptions QUrl.UserInputResolutionOptions.__or__(QUrl.UserInputResolutionOptions f)'''
            return QUrl.UserInputResolutionOptions()
        def __or__(self, f):
            '''QUrl.UserInputResolutionOptions QUrl.UserInputResolutionOptions.__or__(int f)'''
            return QUrl.UserInputResolutionOptions()
        def __int__(self):
            '''int QUrl.UserInputResolutionOptions.__int__()'''
            return int()
        def __ixor__(self, f):
            '''QUrl.UserInputResolutionOptions QUrl.UserInputResolutionOptions.__ixor__(QUrl.UserInputResolutionOptions f)'''
            return QUrl.UserInputResolutionOptions()
        def __ior__(self, f):
            '''QUrl.UserInputResolutionOptions QUrl.UserInputResolutionOptions.__ior__(QUrl.UserInputResolutionOptions f)'''
            return QUrl.UserInputResolutionOptions()
        def __iand__(self, mask):
            '''QUrl.UserInputResolutionOptions QUrl.UserInputResolutionOptions.__iand__(int mask)'''
            return QUrl.UserInputResolutionOptions()
    class FormattingOptions():
        """"""
        def __init__(self):
            '''QUrl.FormattingOptions QUrl.FormattingOptions.__init__()'''
            return QUrl.FormattingOptions()


class QUrlQuery():
    """"""
    def __init__(self):
        '''void QUrlQuery.__init__()'''
    def __init__(self, url):
        '''void QUrlQuery.__init__(QUrl url)'''
    def __init__(self, queryString):
        '''void QUrlQuery.__init__(str queryString)'''
    def __init__(self, other):
        '''void QUrlQuery.__init__(QUrlQuery other)'''
    def defaultQueryPairDelimiter(self):
        '''static str QUrlQuery.defaultQueryPairDelimiter()'''
        return str()
    def defaultQueryValueDelimiter(self):
        '''static str QUrlQuery.defaultQueryValueDelimiter()'''
        return str()
    def removeAllQueryItems(self, key):
        '''void QUrlQuery.removeAllQueryItems(str key)'''
    def allQueryItemValues(self, key, options = None):
        '''list-of-str QUrlQuery.allQueryItemValues(str key, QUrl.ComponentFormattingOptions options = QUrl.PrettyDecoded)'''
        return [str()]
    def queryItemValue(self, key, options = None):
        '''str QUrlQuery.queryItemValue(str key, QUrl.ComponentFormattingOptions options = QUrl.PrettyDecoded)'''
        return str()
    def removeQueryItem(self, key):
        '''void QUrlQuery.removeQueryItem(str key)'''
    def addQueryItem(self, key, value):
        '''void QUrlQuery.addQueryItem(str key, str value)'''
    def hasQueryItem(self, key):
        '''bool QUrlQuery.hasQueryItem(str key)'''
        return bool()
    def queryItems(self, options = None):
        '''list-of-tuple-of-QString-QString QUrlQuery.queryItems(QUrl.ComponentFormattingOptions options = QUrl.PrettyDecoded)'''
        return [tuple-of-str-str()]
    def setQueryItems(self, query):
        '''void QUrlQuery.setQueryItems(list-of-tuple-of-QString-QString query)'''
    def queryPairDelimiter(self):
        '''str QUrlQuery.queryPairDelimiter()'''
        return str()
    def queryValueDelimiter(self):
        '''str QUrlQuery.queryValueDelimiter()'''
        return str()
    def setQueryDelimiters(self, valueDelimiter, pairDelimiter):
        '''void QUrlQuery.setQueryDelimiters(str valueDelimiter, str pairDelimiter)'''
    def toString(self, options = None):
        '''str QUrlQuery.toString(QUrl.ComponentFormattingOptions options = QUrl.PrettyDecoded)'''
        return str()
    def setQuery(self, queryString):
        '''void QUrlQuery.setQuery(str queryString)'''
    def query(self, options = None):
        '''str QUrlQuery.query(QUrl.ComponentFormattingOptions options = QUrl.PrettyDecoded)'''
        return str()
    def clear(self):
        '''void QUrlQuery.clear()'''
    def isDetached(self):
        '''bool QUrlQuery.isDetached()'''
        return bool()
    def isEmpty(self):
        '''bool QUrlQuery.isEmpty()'''
        return bool()
    def swap(self, other):
        '''void QUrlQuery.swap(QUrlQuery other)'''
    def __ne__(self, other):
        '''bool QUrlQuery.__ne__(QUrlQuery other)'''
        return bool()
    def __eq__(self, other):
        '''bool QUrlQuery.__eq__(QUrlQuery other)'''
        return bool()


class QUuid():
    """"""
    # Enum QUuid.Version
    VerUnknown = 0
    Time = 0
    EmbeddedPOSIX = 0
    Md5 = 0
    Name = 0
    Random = 0
    Sha1 = 0

    # Enum QUuid.Variant
    VarUnknown = 0
    NCS = 0
    DCE = 0
    Microsoft = 0
    Reserved = 0

    def __init__(self):
        '''void QUuid.__init__()'''
    def __init__(self, l, w1, w2, b1, b2, b3, b4, b5, b6, b7, b8):
        '''void QUuid.__init__(int l, int w1, int w2, int b1, int b2, int b3, int b4, int b5, int b6, int b7, int b8)'''
    def __init__(self):
        '''str QUuid.__init__()'''
        return str()
    def __init__(self):
        '''QByteArray QUuid.__init__()'''
        return QByteArray()
    def __init__(self):
        '''QUuid QUuid.__init__()'''
        return QUuid()
    def __le__(self, rhs):
        '''bool QUuid.__le__(QUuid rhs)'''
        return bool()
    def __ge__(self, rhs):
        '''bool QUuid.__ge__(QUuid rhs)'''
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
    def createUuidV5(self, ns, baseData):
        '''static QUuid QUuid.createUuidV5(QUuid ns, QByteArray baseData)'''
        return QUuid()
    def createUuidV5(self, ns, baseData):
        '''static QUuid QUuid.createUuidV5(QUuid ns, str baseData)'''
        return QUuid()
    def createUuidV3(self, ns, baseData):
        '''static QUuid QUuid.createUuidV3(QUuid ns, QByteArray baseData)'''
        return QUuid()
    def createUuidV3(self, ns, baseData):
        '''static QUuid QUuid.createUuidV3(QUuid ns, str baseData)'''
        return QUuid()
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
        '''str QUuid.toString()'''
        return str()
    def __repr__(self):
        '''str QUuid.__repr__()'''
        return str()
    def __hash__(self):
        '''int QUuid.__hash__()'''
        return int()


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
    Uuid = 0
    ModelIndex = 0
    PolygonF = 0
    RegularExpression = 0
    PersistentModelIndex = 0
    UserType = 0

    def __init__(self):
        '''void QVariant.__init__()'''
    def __init__(self, type):
        '''void QVariant.__init__(QVariant.Type type)'''
    def __init__(self):
        '''object QVariant.__init__()'''
        return object()
    def __init__(self, other):
        '''void QVariant.__init__(QVariant other)'''
    def __ge__(self, v):
        '''bool QVariant.__ge__(QVariant v)'''
        return bool()
    def __gt__(self, v):
        '''bool QVariant.__gt__(QVariant v)'''
        return bool()
    def __le__(self, v):
        '''bool QVariant.__le__(QVariant v)'''
        return bool()
    def __lt__(self, v):
        '''bool QVariant.__lt__(QVariant v)'''
        return bool()
    def swap(self, other):
        '''void QVariant.swap(QVariant other)'''
    def __ne__(self, v):
        '''bool QVariant.__ne__(QVariant v)'''
        return bool()
    def __eq__(self, v):
        '''bool QVariant.__eq__(QVariant v)'''
        return bool()
    def nameToType(self, name):
        '''static QVariant.Type QVariant.nameToType(str name)'''
        return QVariant.Type()
    def typeToName(self, typeId):
        '''static str QVariant.typeToName(int typeId)'''
        return str()
    def save(self, ds):
        '''void QVariant.save(QDataStream ds)'''
    def load(self, ds):
        '''void QVariant.load(QDataStream ds)'''
    def clear(self):
        '''void QVariant.clear()'''
    def isNull(self):
        '''bool QVariant.isNull()'''
        return bool()
    def isValid(self):
        '''bool QVariant.isValid()'''
        return bool()
    def convert(self, targetTypeId):
        '''bool QVariant.convert(int targetTypeId)'''
        return bool()
    def canConvert(self, targetTypeId):
        '''bool QVariant.canConvert(int targetTypeId)'''
        return bool()
    def typeName(self):
        '''str QVariant.typeName()'''
        return str()
    def userType(self):
        '''int QVariant.userType()'''
        return int()
    def type(self):
        '''QVariant.Type QVariant.type()'''
        return QVariant.Type()
    def value(self):
        '''object QVariant.value()'''
        return object()


class QWaitCondition():
    """"""
    def __init__(self):
        '''void QWaitCondition.__init__()'''
    def wakeAll(self):
        '''void QWaitCondition.wakeAll()'''
    def wakeOne(self):
        '''void QWaitCondition.wakeOne()'''
    def wait(self, mutex, msecs = None):
        '''bool QWaitCondition.wait(QMutex mutex, int msecs = ULONG_MAX)'''
        return bool()
    def wait(self, readWriteLock, msecs = None):
        '''bool QWaitCondition.wait(QReadWriteLock readWriteLock, int msecs = ULONG_MAX)'''
        return bool()


class QXmlStreamAttribute():
    """"""
    def __init__(self):
        '''void QXmlStreamAttribute.__init__()'''
    def __init__(self, qualifiedName, value):
        '''void QXmlStreamAttribute.__init__(str qualifiedName, str value)'''
    def __init__(self, namespaceUri, name, value):
        '''void QXmlStreamAttribute.__init__(str namespaceUri, str name, str value)'''
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
        return strRef()
    def prefix(self):
        '''QStringRef QXmlStreamAttribute.prefix()'''
        return strRef()
    def qualifiedName(self):
        '''QStringRef QXmlStreamAttribute.qualifiedName()'''
        return strRef()
    def name(self):
        '''QStringRef QXmlStreamAttribute.name()'''
        return strRef()
    def namespaceUri(self):
        '''QStringRef QXmlStreamAttribute.namespaceUri()'''
        return strRef()


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
    def lastIndexOf(self, value, from_ = None):
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
    def fill(self, value, size = None):
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
        '''bool QXmlStreamAttributes.hasAttribute(str qualifiedName)'''
        return bool()
    def hasAttribute(self, namespaceUri, name):
        '''bool QXmlStreamAttributes.hasAttribute(str namespaceUri, str name)'''
        return bool()
    def append(self, namespaceUri, name, value):
        '''void QXmlStreamAttributes.append(str namespaceUri, str name, str value)'''
    def append(self, qualifiedName, value):
        '''void QXmlStreamAttributes.append(str qualifiedName, str value)'''
    def append(self, attribute):
        '''void QXmlStreamAttributes.append(QXmlStreamAttribute attribute)'''
    def value(self, namespaceUri, name):
        '''QStringRef QXmlStreamAttributes.value(str namespaceUri, str name)'''
        return strRef()
    def value(self, qualifiedName):
        '''QStringRef QXmlStreamAttributes.value(str qualifiedName)'''
        return strRef()


class QXmlStreamNamespaceDeclaration():
    """"""
    def __init__(self):
        '''void QXmlStreamNamespaceDeclaration.__init__()'''
    def __init__(self):
        '''QXmlStreamNamespaceDeclaration QXmlStreamNamespaceDeclaration.__init__()'''
        return QXmlStreamNamespaceDeclaration()
    def __init__(self, prefix, namespaceUri):
        '''void QXmlStreamNamespaceDeclaration.__init__(str prefix, str namespaceUri)'''
    def __ne__(self, other):
        '''bool QXmlStreamNamespaceDeclaration.__ne__(QXmlStreamNamespaceDeclaration other)'''
        return bool()
    def __eq__(self, other):
        '''bool QXmlStreamNamespaceDeclaration.__eq__(QXmlStreamNamespaceDeclaration other)'''
        return bool()
    def namespaceUri(self):
        '''QStringRef QXmlStreamNamespaceDeclaration.namespaceUri()'''
        return strRef()
    def prefix(self):
        '''QStringRef QXmlStreamNamespaceDeclaration.prefix()'''
        return strRef()


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
        return strRef()
    def systemId(self):
        '''QStringRef QXmlStreamNotationDeclaration.systemId()'''
        return strRef()
    def name(self):
        '''QStringRef QXmlStreamNotationDeclaration.name()'''
        return strRef()


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
        return strRef()
    def publicId(self):
        '''QStringRef QXmlStreamEntityDeclaration.publicId()'''
        return strRef()
    def systemId(self):
        '''QStringRef QXmlStreamEntityDeclaration.systemId()'''
        return strRef()
    def notationName(self):
        '''QStringRef QXmlStreamEntityDeclaration.notationName()'''
        return strRef()
    def name(self):
        '''QStringRef QXmlStreamEntityDeclaration.name()'''
        return strRef()


class QXmlStreamEntityResolver():
    """"""
    def __init__(self):
        '''void QXmlStreamEntityResolver.__init__()'''
    def __init__(self):
        '''QXmlStreamEntityResolver QXmlStreamEntityResolver.__init__()'''
        return QXmlStreamEntityResolver()
    def resolveUndeclaredEntity(self, name):
        '''str QXmlStreamEntityResolver.resolveUndeclaredEntity(str name)'''
        return str()


class QXmlStreamReader():
    """"""
    # Enum QXmlStreamReader.Error
    NoError = 0
    UnexpectedElementError = 0
    CustomError = 0
    NotWellFormedError = 0
    PrematureEndOfDocumentError = 0

    # Enum QXmlStreamReader.ReadElementTextBehaviour
    ErrorOnUnexpectedElement = 0
    IncludeChildElements = 0
    SkipChildElements = 0

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
        '''void QXmlStreamReader.__init__(str data)'''
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
        '''str QXmlStreamReader.errorString()'''
        return str()
    def raiseError(self, message = None):
        '''void QXmlStreamReader.raiseError(str message = '')'''
    def dtdSystemId(self):
        '''QStringRef QXmlStreamReader.dtdSystemId()'''
        return strRef()
    def dtdPublicId(self):
        '''QStringRef QXmlStreamReader.dtdPublicId()'''
        return strRef()
    def dtdName(self):
        '''QStringRef QXmlStreamReader.dtdName()'''
        return strRef()
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
        return strRef()
    def processingInstructionData(self):
        '''QStringRef QXmlStreamReader.processingInstructionData()'''
        return strRef()
    def processingInstructionTarget(self):
        '''QStringRef QXmlStreamReader.processingInstructionTarget()'''
        return strRef()
    def prefix(self):
        '''QStringRef QXmlStreamReader.prefix()'''
        return strRef()
    def qualifiedName(self):
        '''QStringRef QXmlStreamReader.qualifiedName()'''
        return strRef()
    def namespaceUri(self):
        '''QStringRef QXmlStreamReader.namespaceUri()'''
        return strRef()
    def name(self):
        '''QStringRef QXmlStreamReader.name()'''
        return strRef()
    def readElementText(self, behaviour = None):
        '''str QXmlStreamReader.readElementText(QXmlStreamReader.ReadElementTextBehaviour behaviour = QXmlStreamReader.ErrorOnUnexpectedElement)'''
        return str()
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
        return strRef()
    def documentVersion(self):
        '''QStringRef QXmlStreamReader.documentVersion()'''
        return strRef()
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
        '''str QXmlStreamReader.tokenString()'''
        return str()
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
        '''void QXmlStreamReader.addData(str data)'''
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
    def hasError(self):
        '''bool QXmlStreamWriter.hasError()'''
        return bool()
    def writeCurrentToken(self, reader):
        '''void QXmlStreamWriter.writeCurrentToken(QXmlStreamReader reader)'''
    def writeStartElement(self, qualifiedName):
        '''void QXmlStreamWriter.writeStartElement(str qualifiedName)'''
    def writeStartElement(self, namespaceUri, name):
        '''void QXmlStreamWriter.writeStartElement(str namespaceUri, str name)'''
    def writeStartDocument(self):
        '''void QXmlStreamWriter.writeStartDocument()'''
    def writeStartDocument(self, version):
        '''void QXmlStreamWriter.writeStartDocument(str version)'''
    def writeStartDocument(self, version, standalone):
        '''void QXmlStreamWriter.writeStartDocument(str version, bool standalone)'''
    def writeProcessingInstruction(self, target, data = None):
        '''void QXmlStreamWriter.writeProcessingInstruction(str target, str data = '')'''
    def writeDefaultNamespace(self, namespaceUri):
        '''void QXmlStreamWriter.writeDefaultNamespace(str namespaceUri)'''
    def writeNamespace(self, namespaceUri, prefix = None):
        '''void QXmlStreamWriter.writeNamespace(str namespaceUri, str prefix = '')'''
    def writeEntityReference(self, name):
        '''void QXmlStreamWriter.writeEntityReference(str name)'''
    def writeEndElement(self):
        '''void QXmlStreamWriter.writeEndElement()'''
    def writeEndDocument(self):
        '''void QXmlStreamWriter.writeEndDocument()'''
    def writeTextElement(self, qualifiedName, text):
        '''void QXmlStreamWriter.writeTextElement(str qualifiedName, str text)'''
    def writeTextElement(self, namespaceUri, name, text):
        '''void QXmlStreamWriter.writeTextElement(str namespaceUri, str name, str text)'''
    def writeEmptyElement(self, qualifiedName):
        '''void QXmlStreamWriter.writeEmptyElement(str qualifiedName)'''
    def writeEmptyElement(self, namespaceUri, name):
        '''void QXmlStreamWriter.writeEmptyElement(str namespaceUri, str name)'''
    def writeDTD(self, dtd):
        '''void QXmlStreamWriter.writeDTD(str dtd)'''
    def writeComment(self, text):
        '''void QXmlStreamWriter.writeComment(str text)'''
    def writeCharacters(self, text):
        '''void QXmlStreamWriter.writeCharacters(str text)'''
    def writeCDATA(self, text):
        '''void QXmlStreamWriter.writeCDATA(str text)'''
    def writeAttributes(self, attributes):
        '''void QXmlStreamWriter.writeAttributes(QXmlStreamAttributes attributes)'''
    def writeAttribute(self, qualifiedName, value):
        '''void QXmlStreamWriter.writeAttribute(str qualifiedName, str value)'''
    def writeAttribute(self, namespaceUri, name, value):
        '''void QXmlStreamWriter.writeAttribute(str namespaceUri, str name, str value)'''
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


# Enum QtMsgType
QtDebugMsg = 0
QtWarningMsg = 0
QtCriticalMsg = 0
QtFatalMsg = 0
QtSystemMsg = 0
QtInfoMsg = 0


PYQT_VERSION = None # int member

PYQT_VERSION_STR = None # str member

QT_VERSION = None # int member

QT_VERSION_STR = None # str member

def qSetRealNumberPrecision(precision):
    '''static QTextStreamManipulator qSetRealNumberPrecision(int precision)'''
    return QTextStreamManipulator()

def qSetPadChar(ch):
    '''static QTextStreamManipulator qSetPadChar(str ch)'''
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

def dec(s):
    '''static QTextStream dec(QTextStream s)'''
    return QTextStream()

def oct_(s):
    '''static QTextStream oct_(QTextStream s)'''
    return QTextStream()

def bin_(s):
    '''static QTextStream bin_(QTextStream s)'''
    return QTextStream()

def Q_RETURN_ARG(type):
    '''static QGenericReturnArgument Q_RETURN_ARG(object type)'''
    return QGenericReturnArgument()

def Q_ARG(type, data):
    '''static QGenericArgument Q_ARG(object type, object data)'''
    return QGenericArgument()

def pyqtSlot(signature, name = None, result = None):
    '''static object pyqtSlot(str signature, str name = None, str result = None)'''
    return object()

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

def qFloatDistance(a, b):
    '''static int qFloatDistance(float a, float b)'''
    return int()

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

def qFormatLogMessage(type, context, buf):
    '''static str qFormatLogMessage(QtMsgType type, QMessageLogContext context, str buf)'''
    return str()

def qSetMessagePattern(messagePattern):
    '''static void qSetMessagePattern(str messagePattern)'''


def qInstallMessageHandler():
    '''static callable qInstallMessageHandler()'''
    return callable()

def qWarning(msg):
    '''static void qWarning(str msg)'''


def qFatal(msg):
    '''static void qFatal(str msg)'''


def qErrnoWarning(code, msg):
    '''static void qErrnoWarning(int code, str msg)'''


def qErrnoWarning(msg):
    '''static void qErrnoWarning(str msg)'''


def qDebug(msg):
    '''static void qDebug(str msg)'''


def qCritical(msg):
    '''static void qCritical(str msg)'''


def pyqtRestoreInputHook():
    '''static void pyqtRestoreInputHook()'''


def pyqtRemoveInputHook():
    '''static void pyqtRemoveInputHook()'''


def qAddPreRoutine():
    '''static callable qAddPreRoutine()'''
    return callable()

def qRemovePostRoutine():
    '''static callable qRemovePostRoutine()'''
    return callable()

def qAddPostRoutine():
    '''static callable qAddPostRoutine()'''
    return callable()

def qUncompress(data):
    '''static QByteArray qUncompress(QByteArray data)'''
    return QByteArray()

def qCompress(data, compressionLevel = None):
    '''static QByteArray qCompress(QByteArray data, int compressionLevel = -1)'''
    return QByteArray()

def qChecksum(s):
    '''static int qChecksum(str s)'''
    return int()

def pyqtPickleProtocol():
    '''static int-or-None pyqtPickleProtocol()'''
    return int() if True else None()

def pyqtSetPickleProtocol():
    '''static int-or-None pyqtSetPickleProtocol()'''
    return int() if True else None()

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

