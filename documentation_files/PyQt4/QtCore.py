class QSysInfo():
    """"""
    BigEndian = int() # QSysInfo.Endian enum
    LittleEndian = int() # QSysInfo.Endian enum
    ByteOrder = int() # QSysInfo.Endian enum

    WordSize = int() # QSysInfo.Sizes enum

    def __init__(self):
        """None QSysInfo.__init__(None self)"""
        return None
    def __init__(self):
        """QSysInfo QSysInfo.__init__(None self)"""
        return QSysInfo()


class Qt():
    """"""
    NavigationModeNone = int() # Qt.NavigationMode enum
    NavigationModeKeypadTabOrder = int() # Qt.NavigationMode enum
    NavigationModeKeypadDirectional = int() # Qt.NavigationMode enum
    NavigationModeCursorAuto = int() # Qt.NavigationMode enum
    NavigationModeCursorForceVisible = int() # Qt.NavigationMode enum

    DontStartGestureOnChildren = int() # Qt.GestureFlag enum
    ReceivePartialGestures = int() # Qt.GestureFlag enum
    IgnoredGesturesPropagateToParent = int() # Qt.GestureFlag enum

    TapGesture = int() # Qt.GestureType enum
    TapAndHoldGesture = int() # Qt.GestureType enum
    PanGesture = int() # Qt.GestureType enum
    PinchGesture = int() # Qt.GestureType enum
    SwipeGesture = int() # Qt.GestureType enum
    CustomGesture = int() # Qt.GestureType enum

    GestureStarted = int() # Qt.GestureState enum
    GestureUpdated = int() # Qt.GestureState enum
    GestureFinished = int() # Qt.GestureState enum
    GestureCanceled = int() # Qt.GestureState enum

    TouchPointPressed = int() # Qt.TouchPointState enum
    TouchPointMoved = int() # Qt.TouchPointState enum
    TouchPointStationary = int() # Qt.TouchPointState enum
    TouchPointReleased = int() # Qt.TouchPointState enum

    DeviceCoordinates = int() # Qt.CoordinateSystem enum
    LogicalCoordinates = int() # Qt.CoordinateSystem enum

    AnchorLeft = int() # Qt.AnchorPoint enum
    AnchorHorizontalCenter = int() # Qt.AnchorPoint enum
    AnchorRight = int() # Qt.AnchorPoint enum
    AnchorTop = int() # Qt.AnchorPoint enum
    AnchorVerticalCenter = int() # Qt.AnchorPoint enum
    AnchorBottom = int() # Qt.AnchorPoint enum

    ImhNone = int() # Qt.InputMethodHint enum
    ImhHiddenText = int() # Qt.InputMethodHint enum
    ImhNoAutoUppercase = int() # Qt.InputMethodHint enum
    ImhPreferNumbers = int() # Qt.InputMethodHint enum
    ImhPreferUppercase = int() # Qt.InputMethodHint enum
    ImhPreferLowercase = int() # Qt.InputMethodHint enum
    ImhNoPredictiveText = int() # Qt.InputMethodHint enum
    ImhDigitsOnly = int() # Qt.InputMethodHint enum
    ImhFormattedNumbersOnly = int() # Qt.InputMethodHint enum
    ImhUppercaseOnly = int() # Qt.InputMethodHint enum
    ImhLowercaseOnly = int() # Qt.InputMethodHint enum
    ImhDialableCharactersOnly = int() # Qt.InputMethodHint enum
    ImhEmailCharactersOnly = int() # Qt.InputMethodHint enum
    ImhUrlCharactersOnly = int() # Qt.InputMethodHint enum
    ImhExclusiveInputMask = int() # Qt.InputMethodHint enum

    StretchTile = int() # Qt.TileRule enum
    RepeatTile = int() # Qt.TileRule enum
    RoundTile = int() # Qt.TileRule enum

    NoSection = int() # Qt.WindowFrameSection enum
    LeftSection = int() # Qt.WindowFrameSection enum
    TopLeftSection = int() # Qt.WindowFrameSection enum
    TopSection = int() # Qt.WindowFrameSection enum
    TopRightSection = int() # Qt.WindowFrameSection enum
    RightSection = int() # Qt.WindowFrameSection enum
    BottomRightSection = int() # Qt.WindowFrameSection enum
    BottomSection = int() # Qt.WindowFrameSection enum
    BottomLeftSection = int() # Qt.WindowFrameSection enum
    TitleBarArea = int() # Qt.WindowFrameSection enum

    MinimumSize = int() # Qt.SizeHint enum
    PreferredSize = int() # Qt.SizeHint enum
    MaximumSize = int() # Qt.SizeHint enum
    MinimumDescent = int() # Qt.SizeHint enum

    AbsoluteSize = int() # Qt.SizeMode enum
    RelativeSize = int() # Qt.SizeMode enum

    HighEventPriority = int() # Qt.EventPriority enum
    NormalEventPriority = int() # Qt.EventPriority enum
    LowEventPriority = int() # Qt.EventPriority enum

    XAxis = int() # Qt.Axis enum
    YAxis = int() # Qt.Axis enum
    ZAxis = int() # Qt.Axis enum

    MaskInColor = int() # Qt.MaskMode enum
    MaskOutColor = int() # Qt.MaskMode enum

    NoTextInteraction = int() # Qt.TextInteractionFlag enum
    TextSelectableByMouse = int() # Qt.TextInteractionFlag enum
    TextSelectableByKeyboard = int() # Qt.TextInteractionFlag enum
    LinksAccessibleByMouse = int() # Qt.TextInteractionFlag enum
    LinksAccessibleByKeyboard = int() # Qt.TextInteractionFlag enum
    TextEditable = int() # Qt.TextInteractionFlag enum
    TextEditorInteraction = int() # Qt.TextInteractionFlag enum
    TextBrowserInteraction = int() # Qt.TextInteractionFlag enum

    ContainsItemShape = int() # Qt.ItemSelectionMode enum
    IntersectsItemShape = int() # Qt.ItemSelectionMode enum
    ContainsItemBoundingRect = int() # Qt.ItemSelectionMode enum
    IntersectsItemBoundingRect = int() # Qt.ItemSelectionMode enum

    AA_ImmediateWidgetCreation = int() # Qt.ApplicationAttribute enum
    AA_MSWindowsUseDirect3DByDefault = int() # Qt.ApplicationAttribute enum
    AA_DontShowIconsInMenus = int() # Qt.ApplicationAttribute enum
    AA_NativeWindows = int() # Qt.ApplicationAttribute enum
    AA_DontCreateNativeWidgetSiblings = int() # Qt.ApplicationAttribute enum
    AA_MacPluginApplication = int() # Qt.ApplicationAttribute enum
    AA_DontUseNativeMenuBar = int() # Qt.ApplicationAttribute enum
    AA_MacDontSwapCtrlAndMeta = int() # Qt.ApplicationAttribute enum
    AA_S60DontConstructApplicationPanes = int() # Qt.ApplicationAttribute enum

    NonModal = int() # Qt.WindowModality enum
    WindowModal = int() # Qt.WindowModality enum
    ApplicationModal = int() # Qt.WindowModality enum

    MatchExactly = int() # Qt.MatchFlag enum
    MatchFixedString = int() # Qt.MatchFlag enum
    MatchContains = int() # Qt.MatchFlag enum
    MatchStartsWith = int() # Qt.MatchFlag enum
    MatchEndsWith = int() # Qt.MatchFlag enum
    MatchRegExp = int() # Qt.MatchFlag enum
    MatchWildcard = int() # Qt.MatchFlag enum
    MatchCaseSensitive = int() # Qt.MatchFlag enum
    MatchWrap = int() # Qt.MatchFlag enum
    MatchRecursive = int() # Qt.MatchFlag enum

    NoItemFlags = int() # Qt.ItemFlag enum
    ItemIsSelectable = int() # Qt.ItemFlag enum
    ItemIsEditable = int() # Qt.ItemFlag enum
    ItemIsDragEnabled = int() # Qt.ItemFlag enum
    ItemIsDropEnabled = int() # Qt.ItemFlag enum
    ItemIsUserCheckable = int() # Qt.ItemFlag enum
    ItemIsEnabled = int() # Qt.ItemFlag enum
    ItemIsTristate = int() # Qt.ItemFlag enum

    DisplayRole = int() # Qt.ItemDataRole enum
    DecorationRole = int() # Qt.ItemDataRole enum
    EditRole = int() # Qt.ItemDataRole enum
    ToolTipRole = int() # Qt.ItemDataRole enum
    StatusTipRole = int() # Qt.ItemDataRole enum
    WhatsThisRole = int() # Qt.ItemDataRole enum
    FontRole = int() # Qt.ItemDataRole enum
    TextAlignmentRole = int() # Qt.ItemDataRole enum
    BackgroundRole = int() # Qt.ItemDataRole enum
    BackgroundColorRole = int() # Qt.ItemDataRole enum
    ForegroundRole = int() # Qt.ItemDataRole enum
    TextColorRole = int() # Qt.ItemDataRole enum
    CheckStateRole = int() # Qt.ItemDataRole enum
    AccessibleTextRole = int() # Qt.ItemDataRole enum
    AccessibleDescriptionRole = int() # Qt.ItemDataRole enum
    SizeHintRole = int() # Qt.ItemDataRole enum
    UserRole = int() # Qt.ItemDataRole enum

    Unchecked = int() # Qt.CheckState enum
    PartiallyChecked = int() # Qt.CheckState enum
    Checked = int() # Qt.CheckState enum

    CopyAction = int() # Qt.DropAction enum
    MoveAction = int() # Qt.DropAction enum
    LinkAction = int() # Qt.DropAction enum
    ActionMask = int() # Qt.DropAction enum
    TargetMoveAction = int() # Qt.DropAction enum
    IgnoreAction = int() # Qt.DropAction enum

    LeftToRight = int() # Qt.LayoutDirection enum
    RightToLeft = int() # Qt.LayoutDirection enum
    LayoutDirectionAuto = int() # Qt.LayoutDirection enum

    ToolButtonIconOnly = int() # Qt.ToolButtonStyle enum
    ToolButtonTextOnly = int() # Qt.ToolButtonStyle enum
    ToolButtonTextBesideIcon = int() # Qt.ToolButtonStyle enum
    ToolButtonTextUnderIcon = int() # Qt.ToolButtonStyle enum
    ToolButtonFollowStyle = int() # Qt.ToolButtonStyle enum

    ImMicroFocus = int() # Qt.InputMethodQuery enum
    ImFont = int() # Qt.InputMethodQuery enum
    ImCursorPosition = int() # Qt.InputMethodQuery enum
    ImSurroundingText = int() # Qt.InputMethodQuery enum
    ImCurrentSelection = int() # Qt.InputMethodQuery enum
    ImMaximumTextLength = int() # Qt.InputMethodQuery enum
    ImAnchorPosition = int() # Qt.InputMethodQuery enum

    NoContextMenu = int() # Qt.ContextMenuPolicy enum
    PreventContextMenu = int() # Qt.ContextMenuPolicy enum
    DefaultContextMenu = int() # Qt.ContextMenuPolicy enum
    ActionsContextMenu = int() # Qt.ContextMenuPolicy enum
    CustomContextMenu = int() # Qt.ContextMenuPolicy enum

    MouseFocusReason = int() # Qt.FocusReason enum
    TabFocusReason = int() # Qt.FocusReason enum
    BacktabFocusReason = int() # Qt.FocusReason enum
    ActiveWindowFocusReason = int() # Qt.FocusReason enum
    PopupFocusReason = int() # Qt.FocusReason enum
    ShortcutFocusReason = int() # Qt.FocusReason enum
    MenuBarFocusReason = int() # Qt.FocusReason enum
    OtherFocusReason = int() # Qt.FocusReason enum
    NoFocusReason = int() # Qt.FocusReason enum

    FastTransformation = int() # Qt.TransformationMode enum
    SmoothTransformation = int() # Qt.TransformationMode enum

    NoClip = int() # Qt.ClipOperation enum
    ReplaceClip = int() # Qt.ClipOperation enum
    IntersectClip = int() # Qt.ClipOperation enum
    UniteClip = int() # Qt.ClipOperation enum

    OddEvenFill = int() # Qt.FillRule enum
    WindingFill = int() # Qt.FillRule enum

    WidgetShortcut = int() # Qt.ShortcutContext enum
    WindowShortcut = int() # Qt.ShortcutContext enum
    ApplicationShortcut = int() # Qt.ShortcutContext enum
    WidgetWithChildrenShortcut = int() # Qt.ShortcutContext enum

    AutoConnection = int() # Qt.ConnectionType enum
    DirectConnection = int() # Qt.ConnectionType enum
    QueuedConnection = int() # Qt.ConnectionType enum
    AutoCompatConnection = int() # Qt.ConnectionType enum
    BlockingQueuedConnection = int() # Qt.ConnectionType enum
    UniqueConnection = int() # Qt.ConnectionType enum

    TopLeftCorner = int() # Qt.Corner enum
    TopRightCorner = int() # Qt.Corner enum
    BottomLeftCorner = int() # Qt.Corner enum
    BottomRightCorner = int() # Qt.Corner enum

    CaseInsensitive = int() # Qt.CaseSensitivity enum
    CaseSensitive = int() # Qt.CaseSensitivity enum

    ScrollBarAsNeeded = int() # Qt.ScrollBarPolicy enum
    ScrollBarAlwaysOff = int() # Qt.ScrollBarPolicy enum
    ScrollBarAlwaysOn = int() # Qt.ScrollBarPolicy enum

    Monday = int() # Qt.DayOfWeek enum
    Tuesday = int() # Qt.DayOfWeek enum
    Wednesday = int() # Qt.DayOfWeek enum
    Thursday = int() # Qt.DayOfWeek enum
    Friday = int() # Qt.DayOfWeek enum
    Saturday = int() # Qt.DayOfWeek enum
    Sunday = int() # Qt.DayOfWeek enum

    LocalTime = int() # Qt.TimeSpec enum
    UTC = int() # Qt.TimeSpec enum
    OffsetFromUTC = int() # Qt.TimeSpec enum

    TextDate = int() # Qt.DateFormat enum
    ISODate = int() # Qt.DateFormat enum
    LocalDate = int() # Qt.DateFormat enum
    SystemLocaleDate = int() # Qt.DateFormat enum
    LocaleDate = int() # Qt.DateFormat enum
    SystemLocaleShortDate = int() # Qt.DateFormat enum
    SystemLocaleLongDate = int() # Qt.DateFormat enum
    DefaultLocaleShortDate = int() # Qt.DateFormat enum
    DefaultLocaleLongDate = int() # Qt.DateFormat enum

    LeftToolBarArea = int() # Qt.ToolBarArea enum
    RightToolBarArea = int() # Qt.ToolBarArea enum
    TopToolBarArea = int() # Qt.ToolBarArea enum
    BottomToolBarArea = int() # Qt.ToolBarArea enum
    ToolBarArea_Mask = int() # Qt.ToolBarArea enum
    AllToolBarAreas = int() # Qt.ToolBarArea enum
    NoToolBarArea = int() # Qt.ToolBarArea enum

    LeftDockWidgetArea = int() # Qt.DockWidgetArea enum
    RightDockWidgetArea = int() # Qt.DockWidgetArea enum
    TopDockWidgetArea = int() # Qt.DockWidgetArea enum
    BottomDockWidgetArea = int() # Qt.DockWidgetArea enum
    DockWidgetArea_Mask = int() # Qt.DockWidgetArea enum
    AllDockWidgetAreas = int() # Qt.DockWidgetArea enum
    NoDockWidgetArea = int() # Qt.DockWidgetArea enum

    AnchorName = int() # Qt.AnchorAttribute enum
    AnchorHref = int() # Qt.AnchorAttribute enum

    IgnoreAspectRatio = int() # Qt.AspectRatioMode enum
    KeepAspectRatio = int() # Qt.AspectRatioMode enum
    KeepAspectRatioByExpanding = int() # Qt.AspectRatioMode enum

    PlainText = int() # Qt.TextFormat enum
    RichText = int() # Qt.TextFormat enum
    AutoText = int() # Qt.TextFormat enum
    LogText = int() # Qt.TextFormat enum

    ArrowCursor = int() # Qt.CursorShape enum
    UpArrowCursor = int() # Qt.CursorShape enum
    CrossCursor = int() # Qt.CursorShape enum
    WaitCursor = int() # Qt.CursorShape enum
    IBeamCursor = int() # Qt.CursorShape enum
    SizeVerCursor = int() # Qt.CursorShape enum
    SizeHorCursor = int() # Qt.CursorShape enum
    SizeBDiagCursor = int() # Qt.CursorShape enum
    SizeFDiagCursor = int() # Qt.CursorShape enum
    SizeAllCursor = int() # Qt.CursorShape enum
    BlankCursor = int() # Qt.CursorShape enum
    SplitVCursor = int() # Qt.CursorShape enum
    SplitHCursor = int() # Qt.CursorShape enum
    PointingHandCursor = int() # Qt.CursorShape enum
    ForbiddenCursor = int() # Qt.CursorShape enum
    OpenHandCursor = int() # Qt.CursorShape enum
    ClosedHandCursor = int() # Qt.CursorShape enum
    WhatsThisCursor = int() # Qt.CursorShape enum
    BusyCursor = int() # Qt.CursorShape enum
    LastCursor = int() # Qt.CursorShape enum
    BitmapCursor = int() # Qt.CursorShape enum
    CustomCursor = int() # Qt.CursorShape enum
    DragCopyCursor = int() # Qt.CursorShape enum
    DragMoveCursor = int() # Qt.CursorShape enum
    DragLinkCursor = int() # Qt.CursorShape enum

    UI_General = int() # Qt.UIEffect enum
    UI_AnimateMenu = int() # Qt.UIEffect enum
    UI_FadeMenu = int() # Qt.UIEffect enum
    UI_AnimateCombo = int() # Qt.UIEffect enum
    UI_AnimateTooltip = int() # Qt.UIEffect enum
    UI_FadeTooltip = int() # Qt.UIEffect enum
    UI_AnimateToolBox = int() # Qt.UIEffect enum

    NoBrush = int() # Qt.BrushStyle enum
    SolidPattern = int() # Qt.BrushStyle enum
    Dense1Pattern = int() # Qt.BrushStyle enum
    Dense2Pattern = int() # Qt.BrushStyle enum
    Dense3Pattern = int() # Qt.BrushStyle enum
    Dense4Pattern = int() # Qt.BrushStyle enum
    Dense5Pattern = int() # Qt.BrushStyle enum
    Dense6Pattern = int() # Qt.BrushStyle enum
    Dense7Pattern = int() # Qt.BrushStyle enum
    HorPattern = int() # Qt.BrushStyle enum
    VerPattern = int() # Qt.BrushStyle enum
    CrossPattern = int() # Qt.BrushStyle enum
    BDiagPattern = int() # Qt.BrushStyle enum
    FDiagPattern = int() # Qt.BrushStyle enum
    DiagCrossPattern = int() # Qt.BrushStyle enum
    LinearGradientPattern = int() # Qt.BrushStyle enum
    RadialGradientPattern = int() # Qt.BrushStyle enum
    ConicalGradientPattern = int() # Qt.BrushStyle enum
    TexturePattern = int() # Qt.BrushStyle enum

    MiterJoin = int() # Qt.PenJoinStyle enum
    BevelJoin = int() # Qt.PenJoinStyle enum
    RoundJoin = int() # Qt.PenJoinStyle enum
    MPenJoinStyle = int() # Qt.PenJoinStyle enum
    SvgMiterJoin = int() # Qt.PenJoinStyle enum

    FlatCap = int() # Qt.PenCapStyle enum
    SquareCap = int() # Qt.PenCapStyle enum
    RoundCap = int() # Qt.PenCapStyle enum
    MPenCapStyle = int() # Qt.PenCapStyle enum

    NoPen = int() # Qt.PenStyle enum
    SolidLine = int() # Qt.PenStyle enum
    DashLine = int() # Qt.PenStyle enum
    DotLine = int() # Qt.PenStyle enum
    DashDotLine = int() # Qt.PenStyle enum
    DashDotDotLine = int() # Qt.PenStyle enum
    CustomDashLine = int() # Qt.PenStyle enum
    MPenStyle = int() # Qt.PenStyle enum

    NoArrow = int() # Qt.ArrowType enum
    UpArrow = int() # Qt.ArrowType enum
    DownArrow = int() # Qt.ArrowType enum
    LeftArrow = int() # Qt.ArrowType enum
    RightArrow = int() # Qt.ArrowType enum

    Key_Escape = int() # Qt.Key enum
    Key_Tab = int() # Qt.Key enum
    Key_Backtab = int() # Qt.Key enum
    Key_Backspace = int() # Qt.Key enum
    Key_Return = int() # Qt.Key enum
    Key_Enter = int() # Qt.Key enum
    Key_Insert = int() # Qt.Key enum
    Key_Delete = int() # Qt.Key enum
    Key_Pause = int() # Qt.Key enum
    Key_Print = int() # Qt.Key enum
    Key_SysReq = int() # Qt.Key enum
    Key_Clear = int() # Qt.Key enum
    Key_Home = int() # Qt.Key enum
    Key_End = int() # Qt.Key enum
    Key_Left = int() # Qt.Key enum
    Key_Up = int() # Qt.Key enum
    Key_Right = int() # Qt.Key enum
    Key_Down = int() # Qt.Key enum
    Key_PageUp = int() # Qt.Key enum
    Key_PageDown = int() # Qt.Key enum
    Key_Shift = int() # Qt.Key enum
    Key_Control = int() # Qt.Key enum
    Key_Meta = int() # Qt.Key enum
    Key_Alt = int() # Qt.Key enum
    Key_CapsLock = int() # Qt.Key enum
    Key_NumLock = int() # Qt.Key enum
    Key_ScrollLock = int() # Qt.Key enum
    Key_F1 = int() # Qt.Key enum
    Key_F2 = int() # Qt.Key enum
    Key_F3 = int() # Qt.Key enum
    Key_F4 = int() # Qt.Key enum
    Key_F5 = int() # Qt.Key enum
    Key_F6 = int() # Qt.Key enum
    Key_F7 = int() # Qt.Key enum
    Key_F8 = int() # Qt.Key enum
    Key_F9 = int() # Qt.Key enum
    Key_F10 = int() # Qt.Key enum
    Key_F11 = int() # Qt.Key enum
    Key_F12 = int() # Qt.Key enum
    Key_F13 = int() # Qt.Key enum
    Key_F14 = int() # Qt.Key enum
    Key_F15 = int() # Qt.Key enum
    Key_F16 = int() # Qt.Key enum
    Key_F17 = int() # Qt.Key enum
    Key_F18 = int() # Qt.Key enum
    Key_F19 = int() # Qt.Key enum
    Key_F20 = int() # Qt.Key enum
    Key_F21 = int() # Qt.Key enum
    Key_F22 = int() # Qt.Key enum
    Key_F23 = int() # Qt.Key enum
    Key_F24 = int() # Qt.Key enum
    Key_F25 = int() # Qt.Key enum
    Key_F26 = int() # Qt.Key enum
    Key_F27 = int() # Qt.Key enum
    Key_F28 = int() # Qt.Key enum
    Key_F29 = int() # Qt.Key enum
    Key_F30 = int() # Qt.Key enum
    Key_F31 = int() # Qt.Key enum
    Key_F32 = int() # Qt.Key enum
    Key_F33 = int() # Qt.Key enum
    Key_F34 = int() # Qt.Key enum
    Key_F35 = int() # Qt.Key enum
    Key_Super_L = int() # Qt.Key enum
    Key_Super_R = int() # Qt.Key enum
    Key_Menu = int() # Qt.Key enum
    Key_Hyper_L = int() # Qt.Key enum
    Key_Hyper_R = int() # Qt.Key enum
    Key_Help = int() # Qt.Key enum
    Key_Direction_L = int() # Qt.Key enum
    Key_Direction_R = int() # Qt.Key enum
    Key_Space = int() # Qt.Key enum
    Key_Any = int() # Qt.Key enum
    Key_Exclam = int() # Qt.Key enum
    Key_QuoteDbl = int() # Qt.Key enum
    Key_NumberSign = int() # Qt.Key enum
    Key_Dollar = int() # Qt.Key enum
    Key_Percent = int() # Qt.Key enum
    Key_Ampersand = int() # Qt.Key enum
    Key_Apostrophe = int() # Qt.Key enum
    Key_ParenLeft = int() # Qt.Key enum
    Key_ParenRight = int() # Qt.Key enum
    Key_Asterisk = int() # Qt.Key enum
    Key_Plus = int() # Qt.Key enum
    Key_Comma = int() # Qt.Key enum
    Key_Minus = int() # Qt.Key enum
    Key_Period = int() # Qt.Key enum
    Key_Slash = int() # Qt.Key enum
    Key_0 = int() # Qt.Key enum
    Key_1 = int() # Qt.Key enum
    Key_2 = int() # Qt.Key enum
    Key_3 = int() # Qt.Key enum
    Key_4 = int() # Qt.Key enum
    Key_5 = int() # Qt.Key enum
    Key_6 = int() # Qt.Key enum
    Key_7 = int() # Qt.Key enum
    Key_8 = int() # Qt.Key enum
    Key_9 = int() # Qt.Key enum
    Key_Colon = int() # Qt.Key enum
    Key_Semicolon = int() # Qt.Key enum
    Key_Less = int() # Qt.Key enum
    Key_Equal = int() # Qt.Key enum
    Key_Greater = int() # Qt.Key enum
    Key_Question = int() # Qt.Key enum
    Key_At = int() # Qt.Key enum
    Key_A = int() # Qt.Key enum
    Key_B = int() # Qt.Key enum
    Key_C = int() # Qt.Key enum
    Key_D = int() # Qt.Key enum
    Key_E = int() # Qt.Key enum
    Key_F = int() # Qt.Key enum
    Key_G = int() # Qt.Key enum
    Key_H = int() # Qt.Key enum
    Key_I = int() # Qt.Key enum
    Key_J = int() # Qt.Key enum
    Key_K = int() # Qt.Key enum
    Key_L = int() # Qt.Key enum
    Key_M = int() # Qt.Key enum
    Key_N = int() # Qt.Key enum
    Key_O = int() # Qt.Key enum
    Key_P = int() # Qt.Key enum
    Key_Q = int() # Qt.Key enum
    Key_R = int() # Qt.Key enum
    Key_S = int() # Qt.Key enum
    Key_T = int() # Qt.Key enum
    Key_U = int() # Qt.Key enum
    Key_V = int() # Qt.Key enum
    Key_W = int() # Qt.Key enum
    Key_X = int() # Qt.Key enum
    Key_Y = int() # Qt.Key enum
    Key_Z = int() # Qt.Key enum
    Key_BracketLeft = int() # Qt.Key enum
    Key_Backslash = int() # Qt.Key enum
    Key_BracketRight = int() # Qt.Key enum
    Key_AsciiCircum = int() # Qt.Key enum
    Key_Underscore = int() # Qt.Key enum
    Key_QuoteLeft = int() # Qt.Key enum
    Key_BraceLeft = int() # Qt.Key enum
    Key_Bar = int() # Qt.Key enum
    Key_BraceRight = int() # Qt.Key enum
    Key_AsciiTilde = int() # Qt.Key enum
    Key_nobreakspace = int() # Qt.Key enum
    Key_exclamdown = int() # Qt.Key enum
    Key_cent = int() # Qt.Key enum
    Key_sterling = int() # Qt.Key enum
    Key_currency = int() # Qt.Key enum
    Key_yen = int() # Qt.Key enum
    Key_brokenbar = int() # Qt.Key enum
    Key_section = int() # Qt.Key enum
    Key_diaeresis = int() # Qt.Key enum
    Key_copyright = int() # Qt.Key enum
    Key_ordfeminine = int() # Qt.Key enum
    Key_guillemotleft = int() # Qt.Key enum
    Key_notsign = int() # Qt.Key enum
    Key_hyphen = int() # Qt.Key enum
    Key_registered = int() # Qt.Key enum
    Key_macron = int() # Qt.Key enum
    Key_degree = int() # Qt.Key enum
    Key_plusminus = int() # Qt.Key enum
    Key_twosuperior = int() # Qt.Key enum
    Key_threesuperior = int() # Qt.Key enum
    Key_acute = int() # Qt.Key enum
    Key_mu = int() # Qt.Key enum
    Key_paragraph = int() # Qt.Key enum
    Key_periodcentered = int() # Qt.Key enum
    Key_cedilla = int() # Qt.Key enum
    Key_onesuperior = int() # Qt.Key enum
    Key_masculine = int() # Qt.Key enum
    Key_guillemotright = int() # Qt.Key enum
    Key_onequarter = int() # Qt.Key enum
    Key_onehalf = int() # Qt.Key enum
    Key_threequarters = int() # Qt.Key enum
    Key_questiondown = int() # Qt.Key enum
    Key_Agrave = int() # Qt.Key enum
    Key_Aacute = int() # Qt.Key enum
    Key_Acircumflex = int() # Qt.Key enum
    Key_Atilde = int() # Qt.Key enum
    Key_Adiaeresis = int() # Qt.Key enum
    Key_Aring = int() # Qt.Key enum
    Key_AE = int() # Qt.Key enum
    Key_Ccedilla = int() # Qt.Key enum
    Key_Egrave = int() # Qt.Key enum
    Key_Eacute = int() # Qt.Key enum
    Key_Ecircumflex = int() # Qt.Key enum
    Key_Ediaeresis = int() # Qt.Key enum
    Key_Igrave = int() # Qt.Key enum
    Key_Iacute = int() # Qt.Key enum
    Key_Icircumflex = int() # Qt.Key enum
    Key_Idiaeresis = int() # Qt.Key enum
    Key_ETH = int() # Qt.Key enum
    Key_Ntilde = int() # Qt.Key enum
    Key_Ograve = int() # Qt.Key enum
    Key_Oacute = int() # Qt.Key enum
    Key_Ocircumflex = int() # Qt.Key enum
    Key_Otilde = int() # Qt.Key enum
    Key_Odiaeresis = int() # Qt.Key enum
    Key_multiply = int() # Qt.Key enum
    Key_Ooblique = int() # Qt.Key enum
    Key_Ugrave = int() # Qt.Key enum
    Key_Uacute = int() # Qt.Key enum
    Key_Ucircumflex = int() # Qt.Key enum
    Key_Udiaeresis = int() # Qt.Key enum
    Key_Yacute = int() # Qt.Key enum
    Key_THORN = int() # Qt.Key enum
    Key_ssharp = int() # Qt.Key enum
    Key_division = int() # Qt.Key enum
    Key_ydiaeresis = int() # Qt.Key enum
    Key_AltGr = int() # Qt.Key enum
    Key_Multi_key = int() # Qt.Key enum
    Key_Codeinput = int() # Qt.Key enum
    Key_SingleCandidate = int() # Qt.Key enum
    Key_MultipleCandidate = int() # Qt.Key enum
    Key_PreviousCandidate = int() # Qt.Key enum
    Key_Mode_switch = int() # Qt.Key enum
    Key_Kanji = int() # Qt.Key enum
    Key_Muhenkan = int() # Qt.Key enum
    Key_Henkan = int() # Qt.Key enum
    Key_Romaji = int() # Qt.Key enum
    Key_Hiragana = int() # Qt.Key enum
    Key_Katakana = int() # Qt.Key enum
    Key_Hiragana_Katakana = int() # Qt.Key enum
    Key_Zenkaku = int() # Qt.Key enum
    Key_Hankaku = int() # Qt.Key enum
    Key_Zenkaku_Hankaku = int() # Qt.Key enum
    Key_Touroku = int() # Qt.Key enum
    Key_Massyo = int() # Qt.Key enum
    Key_Kana_Lock = int() # Qt.Key enum
    Key_Kana_Shift = int() # Qt.Key enum
    Key_Eisu_Shift = int() # Qt.Key enum
    Key_Eisu_toggle = int() # Qt.Key enum
    Key_Hangul = int() # Qt.Key enum
    Key_Hangul_Start = int() # Qt.Key enum
    Key_Hangul_End = int() # Qt.Key enum
    Key_Hangul_Hanja = int() # Qt.Key enum
    Key_Hangul_Jamo = int() # Qt.Key enum
    Key_Hangul_Romaja = int() # Qt.Key enum
    Key_Hangul_Jeonja = int() # Qt.Key enum
    Key_Hangul_Banja = int() # Qt.Key enum
    Key_Hangul_PreHanja = int() # Qt.Key enum
    Key_Hangul_PostHanja = int() # Qt.Key enum
    Key_Hangul_Special = int() # Qt.Key enum
    Key_Dead_Grave = int() # Qt.Key enum
    Key_Dead_Acute = int() # Qt.Key enum
    Key_Dead_Circumflex = int() # Qt.Key enum
    Key_Dead_Tilde = int() # Qt.Key enum
    Key_Dead_Macron = int() # Qt.Key enum
    Key_Dead_Breve = int() # Qt.Key enum
    Key_Dead_Abovedot = int() # Qt.Key enum
    Key_Dead_Diaeresis = int() # Qt.Key enum
    Key_Dead_Abovering = int() # Qt.Key enum
    Key_Dead_Doubleacute = int() # Qt.Key enum
    Key_Dead_Caron = int() # Qt.Key enum
    Key_Dead_Cedilla = int() # Qt.Key enum
    Key_Dead_Ogonek = int() # Qt.Key enum
    Key_Dead_Iota = int() # Qt.Key enum
    Key_Dead_Voiced_Sound = int() # Qt.Key enum
    Key_Dead_Semivoiced_Sound = int() # Qt.Key enum
    Key_Dead_Belowdot = int() # Qt.Key enum
    Key_Dead_Hook = int() # Qt.Key enum
    Key_Dead_Horn = int() # Qt.Key enum
    Key_Back = int() # Qt.Key enum
    Key_Forward = int() # Qt.Key enum
    Key_Stop = int() # Qt.Key enum
    Key_Refresh = int() # Qt.Key enum
    Key_VolumeDown = int() # Qt.Key enum
    Key_VolumeMute = int() # Qt.Key enum
    Key_VolumeUp = int() # Qt.Key enum
    Key_BassBoost = int() # Qt.Key enum
    Key_BassUp = int() # Qt.Key enum
    Key_BassDown = int() # Qt.Key enum
    Key_TrebleUp = int() # Qt.Key enum
    Key_TrebleDown = int() # Qt.Key enum
    Key_MediaPlay = int() # Qt.Key enum
    Key_MediaStop = int() # Qt.Key enum
    Key_MediaPrevious = int() # Qt.Key enum
    Key_MediaNext = int() # Qt.Key enum
    Key_MediaRecord = int() # Qt.Key enum
    Key_HomePage = int() # Qt.Key enum
    Key_Favorites = int() # Qt.Key enum
    Key_Search = int() # Qt.Key enum
    Key_Standby = int() # Qt.Key enum
    Key_OpenUrl = int() # Qt.Key enum
    Key_LaunchMail = int() # Qt.Key enum
    Key_LaunchMedia = int() # Qt.Key enum
    Key_Launch0 = int() # Qt.Key enum
    Key_Launch1 = int() # Qt.Key enum
    Key_Launch2 = int() # Qt.Key enum
    Key_Launch3 = int() # Qt.Key enum
    Key_Launch4 = int() # Qt.Key enum
    Key_Launch5 = int() # Qt.Key enum
    Key_Launch6 = int() # Qt.Key enum
    Key_Launch7 = int() # Qt.Key enum
    Key_Launch8 = int() # Qt.Key enum
    Key_Launch9 = int() # Qt.Key enum
    Key_LaunchA = int() # Qt.Key enum
    Key_LaunchB = int() # Qt.Key enum
    Key_LaunchC = int() # Qt.Key enum
    Key_LaunchD = int() # Qt.Key enum
    Key_LaunchE = int() # Qt.Key enum
    Key_LaunchF = int() # Qt.Key enum
    Key_MediaLast = int() # Qt.Key enum
    Key_Select = int() # Qt.Key enum
    Key_Yes = int() # Qt.Key enum
    Key_No = int() # Qt.Key enum
    Key_Context1 = int() # Qt.Key enum
    Key_Context2 = int() # Qt.Key enum
    Key_Context3 = int() # Qt.Key enum
    Key_Context4 = int() # Qt.Key enum
    Key_Call = int() # Qt.Key enum
    Key_Hangup = int() # Qt.Key enum
    Key_Flip = int() # Qt.Key enum
    Key_unknown = int() # Qt.Key enum
    Key_Execute = int() # Qt.Key enum
    Key_Printer = int() # Qt.Key enum
    Key_Play = int() # Qt.Key enum
    Key_Sleep = int() # Qt.Key enum
    Key_Zoom = int() # Qt.Key enum
    Key_Cancel = int() # Qt.Key enum
    Key_MonBrightnessUp = int() # Qt.Key enum
    Key_MonBrightnessDown = int() # Qt.Key enum
    Key_KeyboardLightOnOff = int() # Qt.Key enum
    Key_KeyboardBrightnessUp = int() # Qt.Key enum
    Key_KeyboardBrightnessDown = int() # Qt.Key enum
    Key_PowerOff = int() # Qt.Key enum
    Key_WakeUp = int() # Qt.Key enum
    Key_Eject = int() # Qt.Key enum
    Key_ScreenSaver = int() # Qt.Key enum
    Key_WWW = int() # Qt.Key enum
    Key_Memo = int() # Qt.Key enum
    Key_LightBulb = int() # Qt.Key enum
    Key_Shop = int() # Qt.Key enum
    Key_History = int() # Qt.Key enum
    Key_AddFavorite = int() # Qt.Key enum
    Key_HotLinks = int() # Qt.Key enum
    Key_BrightnessAdjust = int() # Qt.Key enum
    Key_Finance = int() # Qt.Key enum
    Key_Community = int() # Qt.Key enum
    Key_AudioRewind = int() # Qt.Key enum
    Key_BackForward = int() # Qt.Key enum
    Key_ApplicationLeft = int() # Qt.Key enum
    Key_ApplicationRight = int() # Qt.Key enum
    Key_Book = int() # Qt.Key enum
    Key_CD = int() # Qt.Key enum
    Key_Calculator = int() # Qt.Key enum
    Key_ToDoList = int() # Qt.Key enum
    Key_ClearGrab = int() # Qt.Key enum
    Key_Close = int() # Qt.Key enum
    Key_Copy = int() # Qt.Key enum
    Key_Cut = int() # Qt.Key enum
    Key_Display = int() # Qt.Key enum
    Key_DOS = int() # Qt.Key enum
    Key_Documents = int() # Qt.Key enum
    Key_Excel = int() # Qt.Key enum
    Key_Explorer = int() # Qt.Key enum
    Key_Game = int() # Qt.Key enum
    Key_Go = int() # Qt.Key enum
    Key_iTouch = int() # Qt.Key enum
    Key_LogOff = int() # Qt.Key enum
    Key_Market = int() # Qt.Key enum
    Key_Meeting = int() # Qt.Key enum
    Key_MenuKB = int() # Qt.Key enum
    Key_MenuPB = int() # Qt.Key enum
    Key_MySites = int() # Qt.Key enum
    Key_News = int() # Qt.Key enum
    Key_OfficeHome = int() # Qt.Key enum
    Key_Option = int() # Qt.Key enum
    Key_Paste = int() # Qt.Key enum
    Key_Phone = int() # Qt.Key enum
    Key_Calendar = int() # Qt.Key enum
    Key_Reply = int() # Qt.Key enum
    Key_Reload = int() # Qt.Key enum
    Key_RotateWindows = int() # Qt.Key enum
    Key_RotationPB = int() # Qt.Key enum
    Key_RotationKB = int() # Qt.Key enum
    Key_Save = int() # Qt.Key enum
    Key_Send = int() # Qt.Key enum
    Key_Spell = int() # Qt.Key enum
    Key_SplitScreen = int() # Qt.Key enum
    Key_Support = int() # Qt.Key enum
    Key_TaskPane = int() # Qt.Key enum
    Key_Terminal = int() # Qt.Key enum
    Key_Tools = int() # Qt.Key enum
    Key_Travel = int() # Qt.Key enum
    Key_Video = int() # Qt.Key enum
    Key_Word = int() # Qt.Key enum
    Key_Xfer = int() # Qt.Key enum
    Key_ZoomIn = int() # Qt.Key enum
    Key_ZoomOut = int() # Qt.Key enum
    Key_Away = int() # Qt.Key enum
    Key_Messenger = int() # Qt.Key enum
    Key_WebCam = int() # Qt.Key enum
    Key_MailForward = int() # Qt.Key enum
    Key_Pictures = int() # Qt.Key enum
    Key_Music = int() # Qt.Key enum
    Key_Battery = int() # Qt.Key enum
    Key_Bluetooth = int() # Qt.Key enum
    Key_WLAN = int() # Qt.Key enum
    Key_UWB = int() # Qt.Key enum
    Key_AudioForward = int() # Qt.Key enum
    Key_AudioRepeat = int() # Qt.Key enum
    Key_AudioRandomPlay = int() # Qt.Key enum
    Key_Subtitle = int() # Qt.Key enum
    Key_AudioCycleTrack = int() # Qt.Key enum
    Key_Time = int() # Qt.Key enum
    Key_Hibernate = int() # Qt.Key enum
    Key_View = int() # Qt.Key enum
    Key_TopMenu = int() # Qt.Key enum
    Key_PowerDown = int() # Qt.Key enum
    Key_Suspend = int() # Qt.Key enum
    Key_ContrastAdjust = int() # Qt.Key enum
    Key_MediaPause = int() # Qt.Key enum
    Key_MediaTogglePlayPause = int() # Qt.Key enum
    Key_LaunchG = int() # Qt.Key enum
    Key_LaunchH = int() # Qt.Key enum
    Key_ToggleCallHangup = int() # Qt.Key enum
    Key_VoiceDial = int() # Qt.Key enum
    Key_LastNumberRedial = int() # Qt.Key enum
    Key_Camera = int() # Qt.Key enum
    Key_CameraFocus = int() # Qt.Key enum

    TransparentMode = int() # Qt.BGMode enum
    OpaqueMode = int() # Qt.BGMode enum

    ColorMode_Mask = int() # Qt.ImageConversionFlag enum
    AutoColor = int() # Qt.ImageConversionFlag enum
    ColorOnly = int() # Qt.ImageConversionFlag enum
    MonoOnly = int() # Qt.ImageConversionFlag enum
    AlphaDither_Mask = int() # Qt.ImageConversionFlag enum
    ThresholdAlphaDither = int() # Qt.ImageConversionFlag enum
    OrderedAlphaDither = int() # Qt.ImageConversionFlag enum
    DiffuseAlphaDither = int() # Qt.ImageConversionFlag enum
    NoAlpha = int() # Qt.ImageConversionFlag enum
    Dither_Mask = int() # Qt.ImageConversionFlag enum
    DiffuseDither = int() # Qt.ImageConversionFlag enum
    OrderedDither = int() # Qt.ImageConversionFlag enum
    ThresholdDither = int() # Qt.ImageConversionFlag enum
    DitherMode_Mask = int() # Qt.ImageConversionFlag enum
    AutoDither = int() # Qt.ImageConversionFlag enum
    PreferDither = int() # Qt.ImageConversionFlag enum
    AvoidDither = int() # Qt.ImageConversionFlag enum

    WA_Disabled = int() # Qt.WidgetAttribute enum
    WA_UnderMouse = int() # Qt.WidgetAttribute enum
    WA_MouseTracking = int() # Qt.WidgetAttribute enum
    WA_OpaquePaintEvent = int() # Qt.WidgetAttribute enum
    WA_StaticContents = int() # Qt.WidgetAttribute enum
    WA_LaidOut = int() # Qt.WidgetAttribute enum
    WA_PaintOnScreen = int() # Qt.WidgetAttribute enum
    WA_NoSystemBackground = int() # Qt.WidgetAttribute enum
    WA_UpdatesDisabled = int() # Qt.WidgetAttribute enum
    WA_Mapped = int() # Qt.WidgetAttribute enum
    WA_MacNoClickThrough = int() # Qt.WidgetAttribute enum
    WA_PaintOutsidePaintEvent = int() # Qt.WidgetAttribute enum
    WA_InputMethodEnabled = int() # Qt.WidgetAttribute enum
    WA_WState_Visible = int() # Qt.WidgetAttribute enum
    WA_WState_Hidden = int() # Qt.WidgetAttribute enum
    WA_ForceDisabled = int() # Qt.WidgetAttribute enum
    WA_KeyCompression = int() # Qt.WidgetAttribute enum
    WA_PendingMoveEvent = int() # Qt.WidgetAttribute enum
    WA_PendingResizeEvent = int() # Qt.WidgetAttribute enum
    WA_SetPalette = int() # Qt.WidgetAttribute enum
    WA_SetFont = int() # Qt.WidgetAttribute enum
    WA_SetCursor = int() # Qt.WidgetAttribute enum
    WA_NoChildEventsFromChildren = int() # Qt.WidgetAttribute enum
    WA_WindowModified = int() # Qt.WidgetAttribute enum
    WA_Resized = int() # Qt.WidgetAttribute enum
    WA_Moved = int() # Qt.WidgetAttribute enum
    WA_PendingUpdate = int() # Qt.WidgetAttribute enum
    WA_InvalidSize = int() # Qt.WidgetAttribute enum
    WA_MacMetalStyle = int() # Qt.WidgetAttribute enum
    WA_CustomWhatsThis = int() # Qt.WidgetAttribute enum
    WA_LayoutOnEntireRect = int() # Qt.WidgetAttribute enum
    WA_OutsideWSRange = int() # Qt.WidgetAttribute enum
    WA_GrabbedShortcut = int() # Qt.WidgetAttribute enum
    WA_TransparentForMouseEvents = int() # Qt.WidgetAttribute enum
    WA_PaintUnclipped = int() # Qt.WidgetAttribute enum
    WA_SetWindowIcon = int() # Qt.WidgetAttribute enum
    WA_NoMouseReplay = int() # Qt.WidgetAttribute enum
    WA_DeleteOnClose = int() # Qt.WidgetAttribute enum
    WA_RightToLeft = int() # Qt.WidgetAttribute enum
    WA_SetLayoutDirection = int() # Qt.WidgetAttribute enum
    WA_NoChildEventsForParent = int() # Qt.WidgetAttribute enum
    WA_ForceUpdatesDisabled = int() # Qt.WidgetAttribute enum
    WA_WState_Created = int() # Qt.WidgetAttribute enum
    WA_WState_CompressKeys = int() # Qt.WidgetAttribute enum
    WA_WState_InPaintEvent = int() # Qt.WidgetAttribute enum
    WA_WState_Reparented = int() # Qt.WidgetAttribute enum
    WA_WState_ConfigPending = int() # Qt.WidgetAttribute enum
    WA_WState_Polished = int() # Qt.WidgetAttribute enum
    WA_WState_OwnSizePolicy = int() # Qt.WidgetAttribute enum
    WA_WState_ExplicitShowHide = int() # Qt.WidgetAttribute enum
    WA_MouseNoMask = int() # Qt.WidgetAttribute enum
    WA_GroupLeader = int() # Qt.WidgetAttribute enum
    WA_NoMousePropagation = int() # Qt.WidgetAttribute enum
    WA_Hover = int() # Qt.WidgetAttribute enum
    WA_InputMethodTransparent = int() # Qt.WidgetAttribute enum
    WA_QuitOnClose = int() # Qt.WidgetAttribute enum
    WA_KeyboardFocusChange = int() # Qt.WidgetAttribute enum
    WA_AcceptDrops = int() # Qt.WidgetAttribute enum
    WA_WindowPropagation = int() # Qt.WidgetAttribute enum
    WA_NoX11EventCompression = int() # Qt.WidgetAttribute enum
    WA_TintedBackground = int() # Qt.WidgetAttribute enum
    WA_X11OpenGLOverlay = int() # Qt.WidgetAttribute enum
    WA_AttributeCount = int() # Qt.WidgetAttribute enum
    WA_AlwaysShowToolTips = int() # Qt.WidgetAttribute enum
    WA_MacOpaqueSizeGrip = int() # Qt.WidgetAttribute enum
    WA_SetStyle = int() # Qt.WidgetAttribute enum
    WA_MacBrushedMetal = int() # Qt.WidgetAttribute enum
    WA_SetLocale = int() # Qt.WidgetAttribute enum
    WA_MacShowFocusRect = int() # Qt.WidgetAttribute enum
    WA_MacNormalSize = int() # Qt.WidgetAttribute enum
    WA_MacSmallSize = int() # Qt.WidgetAttribute enum
    WA_MacMiniSize = int() # Qt.WidgetAttribute enum
    WA_LayoutUsesWidgetRect = int() # Qt.WidgetAttribute enum
    WA_StyledBackground = int() # Qt.WidgetAttribute enum
    WA_MSWindowsUseDirect3D = int() # Qt.WidgetAttribute enum
    WA_MacAlwaysShowToolWindow = int() # Qt.WidgetAttribute enum
    WA_StyleSheet = int() # Qt.WidgetAttribute enum
    WA_ShowWithoutActivating = int() # Qt.WidgetAttribute enum
    WA_NativeWindow = int() # Qt.WidgetAttribute enum
    WA_DontCreateNativeAncestors = int() # Qt.WidgetAttribute enum
    WA_MacVariableSize = int() # Qt.WidgetAttribute enum
    WA_X11NetWmWindowTypeDesktop = int() # Qt.WidgetAttribute enum
    WA_X11NetWmWindowTypeDock = int() # Qt.WidgetAttribute enum
    WA_X11NetWmWindowTypeToolBar = int() # Qt.WidgetAttribute enum
    WA_X11NetWmWindowTypeMenu = int() # Qt.WidgetAttribute enum
    WA_X11NetWmWindowTypeUtility = int() # Qt.WidgetAttribute enum
    WA_X11NetWmWindowTypeSplash = int() # Qt.WidgetAttribute enum
    WA_X11NetWmWindowTypeDialog = int() # Qt.WidgetAttribute enum
    WA_X11NetWmWindowTypeDropDownMenu = int() # Qt.WidgetAttribute enum
    WA_X11NetWmWindowTypePopupMenu = int() # Qt.WidgetAttribute enum
    WA_X11NetWmWindowTypeToolTip = int() # Qt.WidgetAttribute enum
    WA_X11NetWmWindowTypeNotification = int() # Qt.WidgetAttribute enum
    WA_X11NetWmWindowTypeCombo = int() # Qt.WidgetAttribute enum
    WA_X11NetWmWindowTypeDND = int() # Qt.WidgetAttribute enum
    WA_MacFrameworkScaled = int() # Qt.WidgetAttribute enum
    WA_TranslucentBackground = int() # Qt.WidgetAttribute enum
    WA_AcceptTouchEvents = int() # Qt.WidgetAttribute enum
    WA_TouchPadAcceptSingleTouchEvents = int() # Qt.WidgetAttribute enum
    WA_MergeSoftkeys = int() # Qt.WidgetAttribute enum
    WA_MergeSoftkeysRecursively = int() # Qt.WidgetAttribute enum
    WA_X11DoNotAcceptFocus = int() # Qt.WidgetAttribute enum

    WindowNoState = int() # Qt.WindowState enum
    WindowMinimized = int() # Qt.WindowState enum
    WindowMaximized = int() # Qt.WindowState enum
    WindowFullScreen = int() # Qt.WindowState enum
    WindowActive = int() # Qt.WindowState enum

    Widget = int() # Qt.WindowType enum
    Window = int() # Qt.WindowType enum
    Dialog = int() # Qt.WindowType enum
    Sheet = int() # Qt.WindowType enum
    Drawer = int() # Qt.WindowType enum
    Popup = int() # Qt.WindowType enum
    Tool = int() # Qt.WindowType enum
    ToolTip = int() # Qt.WindowType enum
    SplashScreen = int() # Qt.WindowType enum
    Desktop = int() # Qt.WindowType enum
    SubWindow = int() # Qt.WindowType enum
    WindowType_Mask = int() # Qt.WindowType enum
    MSWindowsFixedSizeDialogHint = int() # Qt.WindowType enum
    MSWindowsOwnDC = int() # Qt.WindowType enum
    X11BypassWindowManagerHint = int() # Qt.WindowType enum
    FramelessWindowHint = int() # Qt.WindowType enum
    CustomizeWindowHint = int() # Qt.WindowType enum
    WindowTitleHint = int() # Qt.WindowType enum
    WindowSystemMenuHint = int() # Qt.WindowType enum
    WindowMinimizeButtonHint = int() # Qt.WindowType enum
    WindowMaximizeButtonHint = int() # Qt.WindowType enum
    WindowMinMaxButtonsHint = int() # Qt.WindowType enum
    WindowContextHelpButtonHint = int() # Qt.WindowType enum
    WindowShadeButtonHint = int() # Qt.WindowType enum
    WindowStaysOnTopHint = int() # Qt.WindowType enum
    WindowOkButtonHint = int() # Qt.WindowType enum
    WindowCancelButtonHint = int() # Qt.WindowType enum
    WindowStaysOnBottomHint = int() # Qt.WindowType enum
    WindowCloseButtonHint = int() # Qt.WindowType enum
    MacWindowToolBarButtonHint = int() # Qt.WindowType enum
    BypassGraphicsProxyWidget = int() # Qt.WindowType enum
    WindowSoftkeysVisibleHint = int() # Qt.WindowType enum
    WindowSoftkeysRespondHint = int() # Qt.WindowType enum

    ElideLeft = int() # Qt.TextElideMode enum
    ElideRight = int() # Qt.TextElideMode enum
    ElideMiddle = int() # Qt.TextElideMode enum
    ElideNone = int() # Qt.TextElideMode enum

    TextSingleLine = int() # Qt.TextFlag enum
    TextDontClip = int() # Qt.TextFlag enum
    TextExpandTabs = int() # Qt.TextFlag enum
    TextShowMnemonic = int() # Qt.TextFlag enum
    TextWordWrap = int() # Qt.TextFlag enum
    TextWrapAnywhere = int() # Qt.TextFlag enum
    TextDontPrint = int() # Qt.TextFlag enum
    TextIncludeTrailingSpaces = int() # Qt.TextFlag enum
    TextHideMnemonic = int() # Qt.TextFlag enum
    TextJustificationForced = int() # Qt.TextFlag enum

    AlignLeft = int() # Qt.AlignmentFlag enum
    AlignLeading = int() # Qt.AlignmentFlag enum
    AlignRight = int() # Qt.AlignmentFlag enum
    AlignTrailing = int() # Qt.AlignmentFlag enum
    AlignHCenter = int() # Qt.AlignmentFlag enum
    AlignJustify = int() # Qt.AlignmentFlag enum
    AlignAbsolute = int() # Qt.AlignmentFlag enum
    AlignHorizontal_Mask = int() # Qt.AlignmentFlag enum
    AlignTop = int() # Qt.AlignmentFlag enum
    AlignBottom = int() # Qt.AlignmentFlag enum
    AlignVCenter = int() # Qt.AlignmentFlag enum
    AlignVertical_Mask = int() # Qt.AlignmentFlag enum
    AlignCenter = int() # Qt.AlignmentFlag enum

    AscendingOrder = int() # Qt.SortOrder enum
    DescendingOrder = int() # Qt.SortOrder enum

    NoFocus = int() # Qt.FocusPolicy enum
    TabFocus = int() # Qt.FocusPolicy enum
    ClickFocus = int() # Qt.FocusPolicy enum
    StrongFocus = int() # Qt.FocusPolicy enum
    WheelFocus = int() # Qt.FocusPolicy enum

    Horizontal = int() # Qt.Orientation enum
    Vertical = int() # Qt.Orientation enum

    NoButton = int() # Qt.MouseButton enum
    LeftButton = int() # Qt.MouseButton enum
    RightButton = int() # Qt.MouseButton enum
    MidButton = int() # Qt.MouseButton enum
    MiddleButton = int() # Qt.MouseButton enum
    XButton1 = int() # Qt.MouseButton enum
    XButton2 = int() # Qt.MouseButton enum
    MouseButtonMask = int() # Qt.MouseButton enum

    META = int() # Qt.Modifier enum
    SHIFT = int() # Qt.Modifier enum
    CTRL = int() # Qt.Modifier enum
    ALT = int() # Qt.Modifier enum
    MODIFIER_MASK = int() # Qt.Modifier enum
    UNICODE_ACCEL = int() # Qt.Modifier enum

    NoModifier = int() # Qt.KeyboardModifier enum
    ShiftModifier = int() # Qt.KeyboardModifier enum
    ControlModifier = int() # Qt.KeyboardModifier enum
    AltModifier = int() # Qt.KeyboardModifier enum
    MetaModifier = int() # Qt.KeyboardModifier enum
    KeypadModifier = int() # Qt.KeyboardModifier enum
    GroupSwitchModifier = int() # Qt.KeyboardModifier enum
    KeyboardModifierMask = int() # Qt.KeyboardModifier enum

    color0 = int() # Qt.GlobalColor enum
    color1 = int() # Qt.GlobalColor enum
    black = int() # Qt.GlobalColor enum
    white = int() # Qt.GlobalColor enum
    darkGray = int() # Qt.GlobalColor enum
    gray = int() # Qt.GlobalColor enum
    lightGray = int() # Qt.GlobalColor enum
    red = int() # Qt.GlobalColor enum
    green = int() # Qt.GlobalColor enum
    blue = int() # Qt.GlobalColor enum
    cyan = int() # Qt.GlobalColor enum
    magenta = int() # Qt.GlobalColor enum
    yellow = int() # Qt.GlobalColor enum
    darkRed = int() # Qt.GlobalColor enum
    darkGreen = int() # Qt.GlobalColor enum
    darkBlue = int() # Qt.GlobalColor enum
    darkCyan = int() # Qt.GlobalColor enum
    darkMagenta = int() # Qt.GlobalColor enum
    darkYellow = int() # Qt.GlobalColor enum
    transparent = int() # Qt.GlobalColor enum



class QObject():
    """"""
    staticMetaObject = None # QMetaObject member
    def __init__(self, _parent):
        """None QObject.__init__(None self, QObject _parent)"""
        return None
    def disconnectNotify(self, _signal):
        """None QObject.disconnectNotify(None self, SIGNAL() _signal)"""
        return None
    def connectNotify(self, _signal):
        """None QObject.connectNotify(None self, SIGNAL() _signal)"""
        return None
    def customEvent(self):
        """QEvent QObject.customEvent(None self)"""
        return QEvent()
    def childEvent(self):
        """QChildEvent QObject.childEvent(None self)"""
        return QChildEvent()
    def timerEvent(self):
        """QTimerEvent QObject.timerEvent(None self)"""
        return QTimerEvent()
    def receivers(self, _signal):
        """int QObject.receivers(None self, SIGNAL() _signal)"""
        return int()
    def sender(self):
        """QObject QObject.sender(None self)"""
        return QObject()
    def deleteLater(self):
        """None QObject.deleteLater(None self)"""
        return None
    def inherits(self, _classname):
        """bool QObject.inherits(None self, str _classname)"""
        return bool()
    def parent(self):
        """QObject QObject.parent(None self)"""
        return QObject()
    def property(self, _name):
        """QVariant QObject.property(None self, str _name)"""
        return QVariant()
    def setProperty(self, _name, _value):
        """bool QObject.setProperty(None self, str _name, QVariant _value)"""
        return bool()
    def dynamicPropertyNames(self):
        """list-of-QByteArray QObject.dynamicPropertyNames(None self)"""
        return [QByteArray()]
    def dumpObjectTree(self):
        """None QObject.dumpObjectTree(None self)"""
        return None
    def dumpObjectInfo(self):
        """None QObject.dumpObjectInfo(None self)"""
        return None
    def disconnect(self):
        """SLOT() QObject.disconnect(None self)"""
        return SLOT()()
    def disconnect(self):
        """callable QObject.disconnect(None self)"""
        return callable()
    def connect(self):
        """Qt.ConnectionType QObject.connect(None self)"""
        return Qt.ConnectionType()
    def connect(self):
        """Qt.ConnectionType QObject.connect(None self)"""
        return Qt.ConnectionType()
    def connect(self):
        """Qt.ConnectionType QObject.connect(None self)"""
        return Qt.ConnectionType()
    def removeEventFilter(self):
        """QObject QObject.removeEventFilter(None self)"""
        return QObject()
    def installEventFilter(self):
        """QObject QObject.installEventFilter(None self)"""
        return QObject()
    def setParent(self):
        """QObject QObject.setParent(None self)"""
        return QObject()
    def children(self):
        """list-of-QObject QObject.children(None self)"""
        return [QObject()]
    def killTimer(self, _id):
        """None QObject.killTimer(None self, int _id)"""
        return None
    def startTimer(self, _interval):
        """int QObject.startTimer(None self, int _interval)"""
        return int()
    def moveToThread(self, _thread):
        """None QObject.moveToThread(None self, QThread _thread)"""
        return None
    def thread(self):
        """QThread QObject.thread(None self)"""
        return QThread()
    def blockSignals(self, _b):
        """bool QObject.blockSignals(None self, bool _b)"""
        return bool()
    def signalsBlocked(self):
        """bool QObject.signalsBlocked(None self)"""
        return bool()
    def isWidgetType(self):
        """bool QObject.isWidgetType(None self)"""
        return bool()
    def setObjectName(self, _name):
        """None QObject.setObjectName(None self, QString _name)"""
        return None
    def objectName(self):
        """QString QObject.objectName(None self)"""
        return QString()
    def emit(self, *args):
        """SIGNAL() QObject.emit(None self, ... *args)"""
        return SIGNAL()()
    def findChildren(self, _type, _name):
        """list-of-QObject QObject.findChildren(None self, type _type, QString _name)"""
        return [QObject()]
    def findChildren(self, _type, _regExp):
        """list-of-QObject QObject.findChildren(None self, type _type, QRegExp _regExp)"""
        return [QObject()]
    def findChild(self, _type, _name):
        """QObject QObject.findChild(None self, type _type, QString _name)"""
        return QObject()
    def trUtf8(self, _sourceText, _disambiguation, _n):
        """QString QObject.trUtf8(None self, str _sourceText, str _disambiguation, int _n)"""
        return QString()
    def tr(self, _sourceText, _disambiguation, _n):
        """QString QObject.tr(None self, str _sourceText, str _disambiguation, int _n)"""
        return QString()
    def eventFilter(self):
        """QEvent QObject.eventFilter(None self)"""
        return QEvent()
    def event(self):
        """QEvent QObject.event(None self)"""
        return QEvent()
    def __getattr__(self, _name):
        """object QObject.__getattr__(None self, str _name)"""
        return object()
    def pyqtConfigure(self):
        """object QObject.pyqtConfigure(None self)"""
        return object()
    def metaObject(self):
        """QMetaObject QObject.metaObject(None self)"""
        return QMetaObject()


class QAbstractAnimation(QObject):
    """"""
    KeepWhenStopped = int() # QAbstractAnimation.DeletionPolicy enum
    DeleteWhenStopped = int() # QAbstractAnimation.DeletionPolicy enum

    Stopped = int() # QAbstractAnimation.State enum
    Paused = int() # QAbstractAnimation.State enum
    Running = int() # QAbstractAnimation.State enum

    Forward = int() # QAbstractAnimation.Direction enum
    Backward = int() # QAbstractAnimation.Direction enum

    def __init__(self, _parent):
        """None QAbstractAnimation.__init__(None self, QObject _parent)"""
        return None
    def updateDirection(self, _direction):
        """None QAbstractAnimation.updateDirection(None self, QAbstractAnimation.Direction _direction)"""
        return None
    def updateState(self, _newState, _oldState):
        """None QAbstractAnimation.updateState(None self, QAbstractAnimation.State _newState, QAbstractAnimation.State _oldState)"""
        return None
    def updateCurrentTime(self, _currentTime):
        """abstract None QAbstractAnimation.updateCurrentTime(None self, int _currentTime)"""
        return None
    def event(self, _event):
        """bool QAbstractAnimation.event(None self, QEvent _event)"""
        return bool()
    def setCurrentTime(self, _msecs):
        """None QAbstractAnimation.setCurrentTime(None self, int _msecs)"""
        return None
    def stop(self):
        """None QAbstractAnimation.stop(None self)"""
        return None
    def setPaused(self):
        """bool QAbstractAnimation.setPaused(None self)"""
        return bool()
    def resume(self):
        """None QAbstractAnimation.resume(None self)"""
        return None
    def pause(self):
        """None QAbstractAnimation.pause(None self)"""
        return None
    def start(self, _policy):
        """None QAbstractAnimation.start(None self, QAbstractAnimation.DeletionPolicy _policy)"""
        return None
    def totalDuration(self):
        """int QAbstractAnimation.totalDuration(None self)"""
        return int()
    def duration(self):
        """abstract int QAbstractAnimation.duration(None self)"""
        return int()
    def currentLoop(self):
        """int QAbstractAnimation.currentLoop(None self)"""
        return int()
    def setLoopCount(self, _loopCount):
        """None QAbstractAnimation.setLoopCount(None self, int _loopCount)"""
        return None
    def loopCount(self):
        """int QAbstractAnimation.loopCount(None self)"""
        return int()
    def currentLoopTime(self):
        """int QAbstractAnimation.currentLoopTime(None self)"""
        return int()
    def currentTime(self):
        """int QAbstractAnimation.currentTime(None self)"""
        return int()
    def setDirection(self, _direction):
        """None QAbstractAnimation.setDirection(None self, QAbstractAnimation.Direction _direction)"""
        return None
    def direction(self):
        """QAbstractAnimation.Direction QAbstractAnimation.direction(None self)"""
        return QAbstractAnimation.Direction()
    def group(self):
        """QAnimationGroup QAbstractAnimation.group(None self)"""
        return QAnimationGroup()
    def state(self):
        """QAbstractAnimation.State QAbstractAnimation.state(None self)"""
        return QAbstractAnimation.State()


class QAbstractEventDispatcher(QObject):
    """"""
    def __init__(self, _parent):
        """None QAbstractEventDispatcher.__init__(None self, QObject _parent)"""
        return None
    def closingDown(self):
        """None QAbstractEventDispatcher.closingDown(None self)"""
        return None
    def startingUp(self):
        """None QAbstractEventDispatcher.startingUp(None self)"""
        return None
    def flush(self):
        """abstract None QAbstractEventDispatcher.flush(None self)"""
        return None
    def interrupt(self):
        """abstract None QAbstractEventDispatcher.interrupt(None self)"""
        return None
    def wakeUp(self):
        """abstract None QAbstractEventDispatcher.wakeUp(None self)"""
        return None
    def registeredTimers(self, _object):
        """abstract list-of-tuple-of-int-int QAbstractEventDispatcher.registeredTimers(None self, QObject _object)"""
        return [tuple-of-int-int()]
    def unregisterTimers(self, _object):
        """abstract bool QAbstractEventDispatcher.unregisterTimers(None self, QObject _object)"""
        return bool()
    def unregisterTimer(self, _timerId):
        """abstract bool QAbstractEventDispatcher.unregisterTimer(None self, int _timerId)"""
        return bool()
    def registerTimer(self, _interval, _object):
        """int QAbstractEventDispatcher.registerTimer(None self, int _interval, QObject _object)"""
        return int()
    def registerTimer(self, _timerId, _interval, _object):
        """abstract None QAbstractEventDispatcher.registerTimer(None self, int _timerId, int _interval, QObject _object)"""
        return None
    def unregisterSocketNotifier(self, _notifier):
        """abstract None QAbstractEventDispatcher.unregisterSocketNotifier(None self, QSocketNotifier _notifier)"""
        return None
    def registerSocketNotifier(self, _notifier):
        """abstract None QAbstractEventDispatcher.registerSocketNotifier(None self, QSocketNotifier _notifier)"""
        return None
    def hasPendingEvents(self):
        """abstract bool QAbstractEventDispatcher.hasPendingEvents(None self)"""
        return bool()
    def processEvents(self, _flags):
        """abstract bool QAbstractEventDispatcher.processEvents(None self, QEventLoop.ProcessEventsFlags _flags)"""
        return bool()
    def instance(self, _thread):
        """QAbstractEventDispatcher QAbstractEventDispatcher.instance(None self, QThread _thread)"""
        return QAbstractEventDispatcher()


class QAbstractFileEngine():
    """"""
    CreationTime = int() # QAbstractFileEngine.FileTime enum
    ModificationTime = int() # QAbstractFileEngine.FileTime enum
    AccessTime = int() # QAbstractFileEngine.FileTime enum

    OwnerUser = int() # QAbstractFileEngine.FileOwner enum
    OwnerGroup = int() # QAbstractFileEngine.FileOwner enum

    DefaultName = int() # QAbstractFileEngine.FileName enum
    BaseName = int() # QAbstractFileEngine.FileName enum
    PathName = int() # QAbstractFileEngine.FileName enum
    AbsoluteName = int() # QAbstractFileEngine.FileName enum
    AbsolutePathName = int() # QAbstractFileEngine.FileName enum
    LinkName = int() # QAbstractFileEngine.FileName enum
    CanonicalName = int() # QAbstractFileEngine.FileName enum
    CanonicalPathName = int() # QAbstractFileEngine.FileName enum
    BundleName = int() # QAbstractFileEngine.FileName enum

    ReadOwnerPerm = int() # QAbstractFileEngine.FileFlag enum
    WriteOwnerPerm = int() # QAbstractFileEngine.FileFlag enum
    ExeOwnerPerm = int() # QAbstractFileEngine.FileFlag enum
    ReadUserPerm = int() # QAbstractFileEngine.FileFlag enum
    WriteUserPerm = int() # QAbstractFileEngine.FileFlag enum
    ExeUserPerm = int() # QAbstractFileEngine.FileFlag enum
    ReadGroupPerm = int() # QAbstractFileEngine.FileFlag enum
    WriteGroupPerm = int() # QAbstractFileEngine.FileFlag enum
    ExeGroupPerm = int() # QAbstractFileEngine.FileFlag enum
    ReadOtherPerm = int() # QAbstractFileEngine.FileFlag enum
    WriteOtherPerm = int() # QAbstractFileEngine.FileFlag enum
    ExeOtherPerm = int() # QAbstractFileEngine.FileFlag enum
    LinkType = int() # QAbstractFileEngine.FileFlag enum
    FileType = int() # QAbstractFileEngine.FileFlag enum
    DirectoryType = int() # QAbstractFileEngine.FileFlag enum
    HiddenFlag = int() # QAbstractFileEngine.FileFlag enum
    LocalDiskFlag = int() # QAbstractFileEngine.FileFlag enum
    ExistsFlag = int() # QAbstractFileEngine.FileFlag enum
    RootFlag = int() # QAbstractFileEngine.FileFlag enum
    PermsMask = int() # QAbstractFileEngine.FileFlag enum
    TypesMask = int() # QAbstractFileEngine.FileFlag enum
    FlagsMask = int() # QAbstractFileEngine.FileFlag enum
    FileInfoAll = int() # QAbstractFileEngine.FileFlag enum
    BundleType = int() # QAbstractFileEngine.FileFlag enum
    Refresh = int() # QAbstractFileEngine.FileFlag enum

    def __init__(self):
        """None QAbstractFileEngine.__init__(None self)"""
        return None
    def setError(self, _error, _str):
        """None QAbstractFileEngine.setError(None self, QFile.FileError _error, QString _str)"""
        return None
    def unmap(self, _ptr):
        """bool QAbstractFileEngine.unmap(None self, sip.voidptr _ptr)"""
        return bool()
    def map(self, _offset, _size, _flags):
        """sip.voidptr QAbstractFileEngine.map(None self, int _offset, int _size, QFile.MemoryMapFlags _flags)"""
        return sip.voidptr()
    def create(self, _fileName):
        """QAbstractFileEngine QAbstractFileEngine.create(None self, QString _fileName)"""
        return QAbstractFileEngine()
    def errorString(self):
        """QString QAbstractFileEngine.errorString(None self)"""
        return QString()
    def error(self):
        """QFile.FileError QAbstractFileEngine.error(None self)"""
        return QFile.FileError()
    def write(self, _data):
        """int QAbstractFileEngine.write(None self, str _data)"""
        return int()
    def readLine(self, _maxlen):
        """str QAbstractFileEngine.readLine(None self, int _maxlen)"""
        return str()
    def read(self, _maxlen):
        """str QAbstractFileEngine.read(None self, int _maxlen)"""
        return str()
    def handle(self):
        """int QAbstractFileEngine.handle(None self)"""
        return int()
    def setFileName(self, _file):
        """None QAbstractFileEngine.setFileName(None self, QString _file)"""
        return None
    def fileTime(self, _time):
        """QDateTime QAbstractFileEngine.fileTime(None self, QAbstractFileEngine.FileTime _time)"""
        return QDateTime()
    def owner(self):
        """QAbstractFileEngine.FileOwner QAbstractFileEngine.owner(None self)"""
        return QAbstractFileEngine.FileOwner()
    def ownerId(self):
        """QAbstractFileEngine.FileOwner QAbstractFileEngine.ownerId(None self)"""
        return QAbstractFileEngine.FileOwner()
    def fileName(self, _file):
        """QString QAbstractFileEngine.fileName(None self, QAbstractFileEngine.FileName _file)"""
        return QString()
    def setPermissions(self, _perms):
        """bool QAbstractFileEngine.setPermissions(None self, int _perms)"""
        return bool()
    def fileFlags(self, _type):
        """QAbstractFileEngine.FileFlags QAbstractFileEngine.fileFlags(None self, QAbstractFileEngine.FileFlags _type)"""
        return QAbstractFileEngine.FileFlags()
    def entryList(self, _filters, _filterNames):
        """QStringList QAbstractFileEngine.entryList(None self, QDir.Filters _filters, QStringList _filterNames)"""
        return QStringList()
    def isRelativePath(self):
        """bool QAbstractFileEngine.isRelativePath(None self)"""
        return bool()
    def caseSensitive(self):
        """bool QAbstractFileEngine.caseSensitive(None self)"""
        return bool()
    def setSize(self, _size):
        """bool QAbstractFileEngine.setSize(None self, int _size)"""
        return bool()
    def rmdir(self, _dirName, _recurseParentDirectories):
        """bool QAbstractFileEngine.rmdir(None self, QString _dirName, bool _recurseParentDirectories)"""
        return bool()
    def mkdir(self, _dirName, _createParentDirectories):
        """bool QAbstractFileEngine.mkdir(None self, QString _dirName, bool _createParentDirectories)"""
        return bool()
    def link(self, _newName):
        """bool QAbstractFileEngine.link(None self, QString _newName)"""
        return bool()
    def rename(self, _newName):
        """bool QAbstractFileEngine.rename(None self, QString _newName)"""
        return bool()
    def copy(self, _newName):
        """bool QAbstractFileEngine.copy(None self, QString _newName)"""
        return bool()
    def remove(self):
        """bool QAbstractFileEngine.remove(None self)"""
        return bool()
    def isSequential(self):
        """bool QAbstractFileEngine.isSequential(None self)"""
        return bool()
    def seek(self, _pos):
        """bool QAbstractFileEngine.seek(None self, int _pos)"""
        return bool()
    def pos(self):
        """int QAbstractFileEngine.pos(None self)"""
        return int()
    def size(self):
        """int QAbstractFileEngine.size(None self)"""
        return int()
    def flush(self):
        """bool QAbstractFileEngine.flush(None self)"""
        return bool()
    def close(self):
        """bool QAbstractFileEngine.close(None self)"""
        return bool()
    def open(self, _openMode):
        """bool QAbstractFileEngine.open(None self, QIODevice.OpenMode _openMode)"""
        return bool()
    def atEnd(self):
        """bool QAbstractFileEngine.atEnd(None self)"""
        return bool()


class QAbstractFileEngineHandler():
    """"""
    def __init__(self):
        """None QAbstractFileEngineHandler.__init__(None self)"""
        return None
    def __init__(self):
        """QAbstractFileEngineHandler QAbstractFileEngineHandler.__init__(None self)"""
        return QAbstractFileEngineHandler()
    def create(self, _fileName):
        """abstract QAbstractFileEngine QAbstractFileEngineHandler.create(None self, QString _fileName)"""
        return QAbstractFileEngine()


class QAbstractFileEngineIterator():
    """"""
    def __init__(self, _filters, _nameFilters):
        """None QAbstractFileEngineIterator.__init__(None self, QDir.Filters _filters, QStringList _nameFilters)"""
        return None
    def currentFilePath(self):
        """QString QAbstractFileEngineIterator.currentFilePath(None self)"""
        return QString()
    def currentFileInfo(self):
        """QFileInfo QAbstractFileEngineIterator.currentFileInfo(None self)"""
        return QFileInfo()
    def currentFileName(self):
        """abstract QString QAbstractFileEngineIterator.currentFileName(None self)"""
        return QString()
    def filters(self):
        """QDir.Filters QAbstractFileEngineIterator.filters(None self)"""
        return QDir.Filters()
    def nameFilters(self):
        """QStringList QAbstractFileEngineIterator.nameFilters(None self)"""
        return QStringList()
    def path(self):
        """QString QAbstractFileEngineIterator.path(None self)"""
        return QString()
    def hasNext(self):
        """abstract bool QAbstractFileEngineIterator.hasNext(None self)"""
        return bool()
    def next(self):
        """abstract QString QAbstractFileEngineIterator.next(None self)"""
        return QString()


class QModelIndex():
    """"""
    def __init__(self):
        """None QModelIndex.__init__(None self)"""
        return None
    def __init__(self, _other):
        """None QModelIndex.__init__(None self, QModelIndex _other)"""
        return None
    def __init__(self):
        """QPersistentModelIndex QModelIndex.__init__(None self)"""
        return QPersistentModelIndex()
    def __ge__(self, _other):
        """bool QModelIndex.__ge__(None self, QModelIndex _other)"""
        return bool()
    def __hash__(self):
        """int QModelIndex.__hash__(None self)"""
        return int()
    def __ne__(self, _other):
        """bool QModelIndex.__ne__(None self, QModelIndex _other)"""
        return bool()
    def __lt__(self, _other):
        """bool QModelIndex.__lt__(None self, QModelIndex _other)"""
        return bool()
    def __eq__(self, _other):
        """bool QModelIndex.__eq__(None self, QModelIndex _other)"""
        return bool()
    def sibling(self, _arow, _acolumn):
        """QModelIndex QModelIndex.sibling(None self, int _arow, int _acolumn)"""
        return QModelIndex()
    def parent(self):
        """QModelIndex QModelIndex.parent(None self)"""
        return QModelIndex()
    def isValid(self):
        """bool QModelIndex.isValid(None self)"""
        return bool()
    def model(self):
        """QAbstractItemModel QModelIndex.model(None self)"""
        return QAbstractItemModel()
    def internalId(self):
        """int QModelIndex.internalId(None self)"""
        return int()
    def internalPointer(self):
        """object QModelIndex.internalPointer(None self)"""
        return object()
    def flags(self):
        """Qt.ItemFlags QModelIndex.flags(None self)"""
        return Qt.ItemFlags()
    def data(self, _role):
        """QVariant QModelIndex.data(None self, int _role)"""
        return QVariant()
    def column(self):
        """int QModelIndex.column(None self)"""
        return int()
    def row(self):
        """int QModelIndex.row(None self)"""
        return int()
    def child(self, _arow, _acolumn):
        """QModelIndex QModelIndex.child(None self, int _arow, int _acolumn)"""
        return QModelIndex()


class QPersistentModelIndex():
    """"""
    def __init__(self):
        """None QPersistentModelIndex.__init__(None self)"""
        return None
    def __init__(self, _index):
        """None QPersistentModelIndex.__init__(None self, QModelIndex _index)"""
        return None
    def __init__(self, _other):
        """None QPersistentModelIndex.__init__(None self, QPersistentModelIndex _other)"""
        return None
    def __ge__(self, _other):
        """bool QPersistentModelIndex.__ge__(None self, QPersistentModelIndex _other)"""
        return bool()
    def __hash__(self):
        """int QPersistentModelIndex.__hash__(None self)"""
        return int()
    def __ne__(self, _other):
        """bool QPersistentModelIndex.__ne__(None self, QPersistentModelIndex _other)"""
        return bool()
    def __ne__(self, _other):
        """bool QPersistentModelIndex.__ne__(None self, QModelIndex _other)"""
        return bool()
    def __eq__(self, _other):
        """bool QPersistentModelIndex.__eq__(None self, QPersistentModelIndex _other)"""
        return bool()
    def __eq__(self, _other):
        """bool QPersistentModelIndex.__eq__(None self, QModelIndex _other)"""
        return bool()
    def __lt__(self, _other):
        """bool QPersistentModelIndex.__lt__(None self, QPersistentModelIndex _other)"""
        return bool()
    def isValid(self):
        """bool QPersistentModelIndex.isValid(None self)"""
        return bool()
    def model(self):
        """QAbstractItemModel QPersistentModelIndex.model(None self)"""
        return QAbstractItemModel()
    def child(self, _row, _column):
        """QModelIndex QPersistentModelIndex.child(None self, int _row, int _column)"""
        return QModelIndex()
    def sibling(self, _row, _column):
        """QModelIndex QPersistentModelIndex.sibling(None self, int _row, int _column)"""
        return QModelIndex()
    def parent(self):
        """QModelIndex QPersistentModelIndex.parent(None self)"""
        return QModelIndex()
    def flags(self):
        """Qt.ItemFlags QPersistentModelIndex.flags(None self)"""
        return Qt.ItemFlags()
    def data(self, _role):
        """QVariant QPersistentModelIndex.data(None self, int _role)"""
        return QVariant()
    def column(self):
        """int QPersistentModelIndex.column(None self)"""
        return int()
    def row(self):
        """int QPersistentModelIndex.row(None self)"""
        return int()


class QAbstractItemModel(QObject):
    """"""
    def __init__(self, _parent):
        """None QAbstractItemModel.__init__(None self, QObject _parent)"""
        return None
    def setRoleNames(self, _roleNames):
        """None QAbstractItemModel.setRoleNames(None self, dict-of-int-QByteArray _roleNames)"""
        return None
    def endResetModel(self):
        """None QAbstractItemModel.endResetModel(None self)"""
        return None
    def beginResetModel(self):
        """None QAbstractItemModel.beginResetModel(None self)"""
        return None
    def endMoveColumns(self):
        """None QAbstractItemModel.endMoveColumns(None self)"""
        return None
    def beginMoveColumns(self, _sourceParent, _sourceFirst, _sourceLast, _destinationParent, _destinationColumn):
        """bool QAbstractItemModel.beginMoveColumns(None self, QModelIndex _sourceParent, int _sourceFirst, int _sourceLast, QModelIndex _destinationParent, int _destinationColumn)"""
        return bool()
    def endMoveRows(self):
        """None QAbstractItemModel.endMoveRows(None self)"""
        return None
    def beginMoveRows(self, _sourceParent, _sourceFirst, _sourceLast, _destinationParent, _destinationRow):
        """bool QAbstractItemModel.beginMoveRows(None self, QModelIndex _sourceParent, int _sourceFirst, int _sourceLast, QModelIndex _destinationParent, int _destinationRow)"""
        return bool()
    def createIndex(self, _row, _column, _object):
        """QModelIndex QAbstractItemModel.createIndex(None self, int _row, int _column, object _object)"""
        return QModelIndex()
    def roleNames(self):
        """dict-of-int-QByteArray QAbstractItemModel.roleNames(None self)"""
        return dict-of-int-QByteArray()
    def supportedDragActions(self):
        """Qt.DropActions QAbstractItemModel.supportedDragActions(None self)"""
        return Qt.DropActions()
    def setSupportedDragActions(self):
        """Qt.DropActions QAbstractItemModel.setSupportedDragActions(None self)"""
        return Qt.DropActions()
    def removeColumn(self, _column, _parent):
        """bool QAbstractItemModel.removeColumn(None self, int _column, QModelIndex _parent)"""
        return bool()
    def removeRow(self, _row, _parent):
        """bool QAbstractItemModel.removeRow(None self, int _row, QModelIndex _parent)"""
        return bool()
    def insertColumn(self, _column, _parent):
        """bool QAbstractItemModel.insertColumn(None self, int _column, QModelIndex _parent)"""
        return bool()
    def insertRow(self, _row, _parent):
        """bool QAbstractItemModel.insertRow(None self, int _row, QModelIndex _parent)"""
        return bool()
    def changePersistentIndexList(self, _from, _to):
        """None QAbstractItemModel.changePersistentIndexList(None self, list-of-QModelIndex _from, list-of-QModelIndex _to)"""
        return None
    def changePersistentIndex(self, _from, _to):
        """None QAbstractItemModel.changePersistentIndex(None self, QModelIndex _from, QModelIndex _to)"""
        return None
    def reset(self):
        """None QAbstractItemModel.reset(None self)"""
        return None
    def persistentIndexList(self):
        """list-of-QModelIndex QAbstractItemModel.persistentIndexList(None self)"""
        return [QModelIndex()]
    def endRemoveColumns(self):
        """None QAbstractItemModel.endRemoveColumns(None self)"""
        return None
    def beginRemoveColumns(self, _parent, _first, _last):
        """None QAbstractItemModel.beginRemoveColumns(None self, QModelIndex _parent, int _first, int _last)"""
        return None
    def endInsertColumns(self):
        """None QAbstractItemModel.endInsertColumns(None self)"""
        return None
    def beginInsertColumns(self, _parent, _first, _last):
        """None QAbstractItemModel.beginInsertColumns(None self, QModelIndex _parent, int _first, int _last)"""
        return None
    def endRemoveRows(self):
        """None QAbstractItemModel.endRemoveRows(None self)"""
        return None
    def beginRemoveRows(self, _parent, _first, _last):
        """None QAbstractItemModel.beginRemoveRows(None self, QModelIndex _parent, int _first, int _last)"""
        return None
    def endInsertRows(self):
        """None QAbstractItemModel.endInsertRows(None self)"""
        return None
    def beginInsertRows(self, _parent, _first, _last):
        """None QAbstractItemModel.beginInsertRows(None self, QModelIndex _parent, int _first, int _last)"""
        return None
    def decodeData(self, _row, _column, _parent, _stream):
        """bool QAbstractItemModel.decodeData(None self, int _row, int _column, QModelIndex _parent, QDataStream _stream)"""
        return bool()
    def encodeData(self, _indexes, _stream):
        """None QAbstractItemModel.encodeData(None self, list-of-QModelIndex _indexes, QDataStream _stream)"""
        return None
    def revert(self):
        """None QAbstractItemModel.revert(None self)"""
        return None
    def submit(self):
        """bool QAbstractItemModel.submit(None self)"""
        return bool()
    def span(self, _index):
        """QSize QAbstractItemModel.span(None self, QModelIndex _index)"""
        return QSize()
    def match(self, _start, _role, _value, _hits, _flags):
        """list-of-QModelIndex QAbstractItemModel.match(None self, QModelIndex _start, int _role, QVariant _value, int _hits, Qt.MatchFlags _flags)"""
        return [QModelIndex()]
    def buddy(self, _index):
        """QModelIndex QAbstractItemModel.buddy(None self, QModelIndex _index)"""
        return QModelIndex()
    def sort(self, _column, _order):
        """None QAbstractItemModel.sort(None self, int _column, Qt.SortOrder _order)"""
        return None
    def flags(self, _index):
        """Qt.ItemFlags QAbstractItemModel.flags(None self, QModelIndex _index)"""
        return Qt.ItemFlags()
    def canFetchMore(self, _parent):
        """bool QAbstractItemModel.canFetchMore(None self, QModelIndex _parent)"""
        return bool()
    def fetchMore(self, _parent):
        """None QAbstractItemModel.fetchMore(None self, QModelIndex _parent)"""
        return None
    def removeColumns(self, _column, _count, _parent):
        """bool QAbstractItemModel.removeColumns(None self, int _column, int _count, QModelIndex _parent)"""
        return bool()
    def removeRows(self, _row, _count, _parent):
        """bool QAbstractItemModel.removeRows(None self, int _row, int _count, QModelIndex _parent)"""
        return bool()
    def insertColumns(self, _column, _count, _parent):
        """bool QAbstractItemModel.insertColumns(None self, int _column, int _count, QModelIndex _parent)"""
        return bool()
    def insertRows(self, _row, _count, _parent):
        """bool QAbstractItemModel.insertRows(None self, int _row, int _count, QModelIndex _parent)"""
        return bool()
    def supportedDropActions(self):
        """Qt.DropActions QAbstractItemModel.supportedDropActions(None self)"""
        return Qt.DropActions()
    def dropMimeData(self, _data, _action, _row, _column, _parent):
        """bool QAbstractItemModel.dropMimeData(None self, QMimeData _data, Qt.DropAction _action, int _row, int _column, QModelIndex _parent)"""
        return bool()
    def mimeData(self, _indexes):
        """QMimeData QAbstractItemModel.mimeData(None self, list-of-QModelIndex _indexes)"""
        return QMimeData()
    def mimeTypes(self):
        """QStringList QAbstractItemModel.mimeTypes(None self)"""
        return QStringList()
    def setItemData(self, _index, _roles):
        """bool QAbstractItemModel.setItemData(None self, QModelIndex _index, dict-of-int-QVariant _roles)"""
        return bool()
    def itemData(self, _index):
        """dict-of-int-QVariant QAbstractItemModel.itemData(None self, QModelIndex _index)"""
        return dict-of-int-QVariant()
    def setHeaderData(self, _section, _orientation, _value, _role):
        """bool QAbstractItemModel.setHeaderData(None self, int _section, Qt.Orientation _orientation, QVariant _value, int _role)"""
        return bool()
    def headerData(self, _section, _orientation, _role):
        """QVariant QAbstractItemModel.headerData(None self, int _section, Qt.Orientation _orientation, int _role)"""
        return QVariant()
    def setData(self, _index, _value, _role):
        """bool QAbstractItemModel.setData(None self, QModelIndex _index, QVariant _value, int _role)"""
        return bool()
    def data(self, _index, _role):
        """abstract QVariant QAbstractItemModel.data(None self, QModelIndex _index, int _role)"""
        return QVariant()
    def hasChildren(self, _parent):
        """bool QAbstractItemModel.hasChildren(None self, QModelIndex _parent)"""
        return bool()
    def columnCount(self, _parent):
        """abstract int QAbstractItemModel.columnCount(None self, QModelIndex _parent)"""
        return int()
    def rowCount(self, _parent):
        """abstract int QAbstractItemModel.rowCount(None self, QModelIndex _parent)"""
        return int()
    def sibling(self, _row, _column, _idx):
        """QModelIndex QAbstractItemModel.sibling(None self, int _row, int _column, QModelIndex _idx)"""
        return QModelIndex()
    def parent(self, _child):
        """abstract QModelIndex QAbstractItemModel.parent(None self, QModelIndex _child)"""
        return QModelIndex()
    def parent(self):
        """QObject QAbstractItemModel.parent(None self)"""
        return QObject()
    def index(self, _row, _column, _parent):
        """abstract QModelIndex QAbstractItemModel.index(None self, int _row, int _column, QModelIndex _parent)"""
        return QModelIndex()
    def hasIndex(self, _row, _column, _parent):
        """bool QAbstractItemModel.hasIndex(None self, int _row, int _column, QModelIndex _parent)"""
        return bool()


class QAbstractTableModel(QAbstractItemModel):
    """"""
    def __init__(self, _parent):
        """None QAbstractTableModel.__init__(None self, QObject _parent)"""
        return None
    def dropMimeData(self, _data, _action, _row, _column, _parent):
        """bool QAbstractTableModel.dropMimeData(None self, QMimeData _data, Qt.DropAction _action, int _row, int _column, QModelIndex _parent)"""
        return bool()
    def index(self, _row, _column, _parent):
        """QModelIndex QAbstractTableModel.index(None self, int _row, int _column, QModelIndex _parent)"""
        return QModelIndex()


class QAbstractListModel(QAbstractItemModel):
    """"""
    def __init__(self, _parent):
        """None QAbstractListModel.__init__(None self, QObject _parent)"""
        return None
    def dropMimeData(self, _data, _action, _row, _column, _parent):
        """bool QAbstractListModel.dropMimeData(None self, QMimeData _data, Qt.DropAction _action, int _row, int _column, QModelIndex _parent)"""
        return bool()
    def index(self, _row, _column, _parent):
        """QModelIndex QAbstractListModel.index(None self, int _row, int _column, QModelIndex _parent)"""
        return QModelIndex()


class QAbstractState(QObject):
    """"""
    def __init__(self, _parent):
        """None QAbstractState.__init__(None self, QState _parent)"""
        return None
    def event(self, _e):
        """bool QAbstractState.event(None self, QEvent _e)"""
        return bool()
    def onExit(self, _event):
        """abstract None QAbstractState.onExit(None self, QEvent _event)"""
        return None
    def onEntry(self, _event):
        """abstract None QAbstractState.onEntry(None self, QEvent _event)"""
        return None
    def machine(self):
        """QStateMachine QAbstractState.machine(None self)"""
        return QStateMachine()
    def parentState(self):
        """QState QAbstractState.parentState(None self)"""
        return QState()


class QAbstractTransition(QObject):
    """"""
    def __init__(self, _sourceState):
        """None QAbstractTransition.__init__(None self, QState _sourceState)"""
        return None
    def event(self, _e):
        """bool QAbstractTransition.event(None self, QEvent _e)"""
        return bool()
    def onTransition(self, _event):
        """abstract None QAbstractTransition.onTransition(None self, QEvent _event)"""
        return None
    def eventTest(self, _event):
        """abstract bool QAbstractTransition.eventTest(None self, QEvent _event)"""
        return bool()
    def animations(self):
        """list-of-QAbstractAnimation QAbstractTransition.animations(None self)"""
        return [QAbstractAnimation()]
    def removeAnimation(self, _animation):
        """None QAbstractTransition.removeAnimation(None self, QAbstractAnimation _animation)"""
        return None
    def addAnimation(self, _animation):
        """None QAbstractTransition.addAnimation(None self, QAbstractAnimation _animation)"""
        return None
    def machine(self):
        """QStateMachine QAbstractTransition.machine(None self)"""
        return QStateMachine()
    def setTargetStates(self, _targets):
        """None QAbstractTransition.setTargetStates(None self, list-of-QAbstractState _targets)"""
        return None
    def targetStates(self):
        """list-of-QAbstractState QAbstractTransition.targetStates(None self)"""
        return [QAbstractState()]
    def setTargetState(self, _target):
        """None QAbstractTransition.setTargetState(None self, QAbstractState _target)"""
        return None
    def targetState(self):
        """QAbstractState QAbstractTransition.targetState(None self)"""
        return QAbstractState()
    def sourceState(self):
        """QState QAbstractTransition.sourceState(None self)"""
        return QState()


class QAnimationGroup(QAbstractAnimation):
    """"""
    def __init__(self, _parent):
        """None QAnimationGroup.__init__(None self, QObject _parent)"""
        return None
    def event(self, _event):
        """bool QAnimationGroup.event(None self, QEvent _event)"""
        return bool()
    def clear(self):
        """None QAnimationGroup.clear(None self)"""
        return None
    def takeAnimation(self, _index):
        """QAbstractAnimation QAnimationGroup.takeAnimation(None self, int _index)"""
        return QAbstractAnimation()
    def removeAnimation(self, _animation):
        """None QAnimationGroup.removeAnimation(None self, QAbstractAnimation _animation)"""
        return None
    def insertAnimation(self, _index, _animation):
        """None QAnimationGroup.insertAnimation(None self, int _index, QAbstractAnimation _animation)"""
        return None
    def addAnimation(self, _animation):
        """None QAnimationGroup.addAnimation(None self, QAbstractAnimation _animation)"""
        return None
    def indexOfAnimation(self, _animation):
        """int QAnimationGroup.indexOfAnimation(None self, QAbstractAnimation _animation)"""
        return int()
    def animationCount(self):
        """int QAnimationGroup.animationCount(None self)"""
        return int()
    def animationAt(self, _index):
        """QAbstractAnimation QAnimationGroup.animationAt(None self, int _index)"""
        return QAbstractAnimation()


class QBasicTimer():
    """"""
    def __init__(self):
        """None QBasicTimer.__init__(None self)"""
        return None
    def __init__(self):
        """QBasicTimer QBasicTimer.__init__(None self)"""
        return QBasicTimer()
    def stop(self):
        """None QBasicTimer.stop(None self)"""
        return None
    def start(self, _msec, _obj):
        """None QBasicTimer.start(None self, int _msec, QObject _obj)"""
        return None
    def timerId(self):
        """int QBasicTimer.timerId(None self)"""
        return int()
    def isActive(self):
        """bool QBasicTimer.isActive(None self)"""
        return bool()


class QBitArray():
    """"""
    def __init__(self):
        """None QBitArray.__init__(None self)"""
        return None
    def __init__(self, _size, _value):
        """None QBitArray.__init__(None self, int _size, bool _value)"""
        return None
    def __init__(self, _other):
        """None QBitArray.__init__(None self, QBitArray _other)"""
        return None
    def __or__(self):
        """QBitArray QBitArray.__or__(None self)"""
        return QBitArray()
    def __and__(self):
        """QBitArray QBitArray.__and__(None self)"""
        return QBitArray()
    def __xor__(self):
        """QBitArray QBitArray.__xor__(None self)"""
        return QBitArray()
    def __hash__(self):
        """int QBitArray.__hash__(None self)"""
        return int()
    def at(self, _i):
        """bool QBitArray.at(None self, int _i)"""
        return bool()
    def __getitem__(self, _i):
        """bool QBitArray.__getitem__(None self, int _i)"""
        return bool()
    def toggleBit(self, _i):
        """bool QBitArray.toggleBit(None self, int _i)"""
        return bool()
    def clearBit(self, _i):
        """None QBitArray.clearBit(None self, int _i)"""
        return None
    def setBit(self, _i):
        """None QBitArray.setBit(None self, int _i)"""
        return None
    def setBit(self, _i, _val):
        """None QBitArray.setBit(None self, int _i, bool _val)"""
        return None
    def testBit(self, _i):
        """bool QBitArray.testBit(None self, int _i)"""
        return bool()
    def truncate(self, _pos):
        """None QBitArray.truncate(None self, int _pos)"""
        return None
    def fill(self, _val, _first, _last):
        """None QBitArray.fill(None self, bool _val, int _first, int _last)"""
        return None
    def fill(self, _value, _size):
        """bool QBitArray.fill(None self, bool _value, int _size)"""
        return bool()
    def __ne__(self, _a):
        """bool QBitArray.__ne__(None self, QBitArray _a)"""
        return bool()
    def __eq__(self, _a):
        """bool QBitArray.__eq__(None self, QBitArray _a)"""
        return bool()
    def __invert__(self):
        """QBitArray QBitArray.__invert__(None self)"""
        return QBitArray()
    def __ixor__(self):
        """QBitArray QBitArray.__ixor__(None self)"""
        return QBitArray()
    def __ior__(self):
        """QBitArray QBitArray.__ior__(None self)"""
        return QBitArray()
    def __iand__(self):
        """QBitArray QBitArray.__iand__(None self)"""
        return QBitArray()
    def clear(self):
        """None QBitArray.clear(None self)"""
        return None
    def isDetached(self):
        """bool QBitArray.isDetached(None self)"""
        return bool()
    def detach(self):
        """None QBitArray.detach(None self)"""
        return None
    def resize(self, _size):
        """None QBitArray.resize(None self, int _size)"""
        return None
    def isNull(self):
        """bool QBitArray.isNull(None self)"""
        return bool()
    def isEmpty(self):
        """bool QBitArray.isEmpty(None self)"""
        return bool()
    def __len__(self):
        """ QBitArray.__len__(None self)"""
        return ()
    def count(self):
        """int QBitArray.count(None self)"""
        return int()
    def count(self, _on):
        """int QBitArray.count(None self, bool _on)"""
        return int()
    def size(self):
        """int QBitArray.size(None self)"""
        return int()


class QIODevice(QObject):
    """"""
    NotOpen = int() # QIODevice.OpenModeFlag enum
    ReadOnly = int() # QIODevice.OpenModeFlag enum
    WriteOnly = int() # QIODevice.OpenModeFlag enum
    ReadWrite = int() # QIODevice.OpenModeFlag enum
    Append = int() # QIODevice.OpenModeFlag enum
    Truncate = int() # QIODevice.OpenModeFlag enum
    Text = int() # QIODevice.OpenModeFlag enum
    Unbuffered = int() # QIODevice.OpenModeFlag enum

    def __init__(self):
        """None QIODevice.__init__(None self)"""
        return None
    def __init__(self, _parent):
        """None QIODevice.__init__(None self, QObject _parent)"""
        return None
    def setErrorString(self, _errorString):
        """None QIODevice.setErrorString(None self, QString _errorString)"""
        return None
    def setOpenMode(self, _openMode):
        """None QIODevice.setOpenMode(None self, QIODevice.OpenMode _openMode)"""
        return None
    def writeData(self, _data):
        """abstract int QIODevice.writeData(None self, str _data)"""
        return int()
    def readLineData(self, _maxlen):
        """str QIODevice.readLineData(None self, int _maxlen)"""
        return str()
    def readData(self, _maxlen):
        """abstract str QIODevice.readData(None self, int _maxlen)"""
        return str()
    def errorString(self):
        """QString QIODevice.errorString(None self)"""
        return QString()
    def getChar(self, _c):
        """bool QIODevice.getChar(None self, str _c)"""
        return bool()
    def putChar(self, _c):
        """bool QIODevice.putChar(None self, str _c)"""
        return bool()
    def ungetChar(self, _c):
        """None QIODevice.ungetChar(None self, str _c)"""
        return None
    def waitForBytesWritten(self, _msecs):
        """bool QIODevice.waitForBytesWritten(None self, int _msecs)"""
        return bool()
    def waitForReadyRead(self, _msecs):
        """bool QIODevice.waitForReadyRead(None self, int _msecs)"""
        return bool()
    def write(self, _data):
        """int QIODevice.write(None self, QByteArray _data)"""
        return int()
    def peek(self, _maxlen):
        """QByteArray QIODevice.peek(None self, int _maxlen)"""
        return QByteArray()
    def canReadLine(self):
        """bool QIODevice.canReadLine(None self)"""
        return bool()
    def readLine(self, _maxlen):
        """str QIODevice.readLine(None self, int _maxlen)"""
        return str()
    def readAll(self):
        """QByteArray QIODevice.readAll(None self)"""
        return QByteArray()
    def read(self, _maxlen):
        """str QIODevice.read(None self, int _maxlen)"""
        return str()
    def bytesToWrite(self):
        """int QIODevice.bytesToWrite(None self)"""
        return int()
    def bytesAvailable(self):
        """int QIODevice.bytesAvailable(None self)"""
        return int()
    def reset(self):
        """bool QIODevice.reset(None self)"""
        return bool()
    def atEnd(self):
        """bool QIODevice.atEnd(None self)"""
        return bool()
    def seek(self, _pos):
        """bool QIODevice.seek(None self, int _pos)"""
        return bool()
    def size(self):
        """int QIODevice.size(None self)"""
        return int()
    def pos(self):
        """int QIODevice.pos(None self)"""
        return int()
    def close(self):
        """None QIODevice.close(None self)"""
        return None
    def open(self, _mode):
        """bool QIODevice.open(None self, QIODevice.OpenMode _mode)"""
        return bool()
    def isSequential(self):
        """bool QIODevice.isSequential(None self)"""
        return bool()
    def isWritable(self):
        """bool QIODevice.isWritable(None self)"""
        return bool()
    def isReadable(self):
        """bool QIODevice.isReadable(None self)"""
        return bool()
    def isOpen(self):
        """bool QIODevice.isOpen(None self)"""
        return bool()
    def isTextModeEnabled(self):
        """bool QIODevice.isTextModeEnabled(None self)"""
        return bool()
    def setTextModeEnabled(self, _enabled):
        """None QIODevice.setTextModeEnabled(None self, bool _enabled)"""
        return None
    def openMode(self):
        """QIODevice.OpenMode QIODevice.openMode(None self)"""
        return QIODevice.OpenMode()


class QBuffer(QIODevice):
    """"""
    def __init__(self, _parent):
        """None QBuffer.__init__(None self, QObject _parent)"""
        return None
    def __init__(self, _byteArray, _parent):
        """None QBuffer.__init__(None self, QByteArray _byteArray, QObject _parent)"""
        return None
    def disconnectNotify(self):
        """SIGNAL() QBuffer.disconnectNotify(None self)"""
        return SIGNAL()()
    def connectNotify(self):
        """SIGNAL() QBuffer.connectNotify(None self)"""
        return SIGNAL()()
    def writeData(self, _data):
        """int QBuffer.writeData(None self, str _data)"""
        return int()
    def readData(self, _maxlen):
        """str QBuffer.readData(None self, int _maxlen)"""
        return str()
    def canReadLine(self):
        """bool QBuffer.canReadLine(None self)"""
        return bool()
    def atEnd(self):
        """bool QBuffer.atEnd(None self)"""
        return bool()
    def seek(self, _off):
        """bool QBuffer.seek(None self, int _off)"""
        return bool()
    def pos(self):
        """int QBuffer.pos(None self)"""
        return int()
    def size(self):
        """int QBuffer.size(None self)"""
        return int()
    def close(self):
        """None QBuffer.close(None self)"""
        return None
    def open(self, _openMode):
        """bool QBuffer.open(None self, QIODevice.OpenMode _openMode)"""
        return bool()
    def setData(self, _data):
        """None QBuffer.setData(None self, QByteArray _data)"""
        return None
    def setData(self, _adata):
        """None QBuffer.setData(None self, str _adata)"""
        return None
    def setBuffer(self, _a):
        """None QBuffer.setBuffer(None self, QByteArray _a)"""
        return None
    def data(self):
        """QByteArray QBuffer.data(None self)"""
        return QByteArray()
    def buffer(self):
        """QByteArray QBuffer.buffer(None self)"""
        return QByteArray()


class QByteArray():
    """"""
    def __init__(self):
        """None QByteArray.__init__(None self)"""
        return None
    def __init__(self, _size, _c):
        """None QByteArray.__init__(None self, int _size, str _c)"""
        return None
    def __init__(self, _a):
        """None QByteArray.__init__(None self, QByteArray _a)"""
        return None
    def __add__(self, _a2):
        """QByteArray QByteArray.__add__(None self, QByteArray _a2)"""
        return QByteArray()
    def __add__(self, _s):
        """QString QByteArray.__add__(None self, QString _s)"""
        return QString()
    def repeated(self, _times):
        """QByteArray QByteArray.repeated(None self, int _times)"""
        return QByteArray()
    def fromPercentEncoding(self, _input, _percent):
        """QByteArray QByteArray.fromPercentEncoding(None self, QByteArray _input, str _percent)"""
        return QByteArray()
    def toPercentEncoding(self, _exclude, _include, _percent):
        """QByteArray QByteArray.toPercentEncoding(None self, QByteArray _exclude, QByteArray _include, str _percent)"""
        return QByteArray()
    def toHex(self):
        """QByteArray QByteArray.toHex(None self)"""
        return QByteArray()
    def contains(self, _a):
        """bool QByteArray.contains(None self, QByteArray _a)"""
        return bool()
    def push_front(self, _a):
        """None QByteArray.push_front(None self, QByteArray _a)"""
        return None
    def push_back(self, _a):
        """None QByteArray.push_back(None self, QByteArray _a)"""
        return None
    def squeeze(self):
        """None QByteArray.squeeze(None self)"""
        return None
    def reserve(self, _size):
        """None QByteArray.reserve(None self, int _size)"""
        return None
    def capacity(self):
        """int QByteArray.capacity(None self)"""
        return int()
    def data(self):
        """str QByteArray.data(None self)"""
        return str()
    def isEmpty(self):
        """bool QByteArray.isEmpty(None self)"""
        return bool()
    def __imul__(self, _m):
        """QByteArray QByteArray.__imul__(None self, int _m)"""
        return QByteArray()
    def __mul__(self, _m):
        """QByteArray QByteArray.__mul__(None self, int _m)"""
        return QByteArray()
    def __repr__(self):
        """str QByteArray.__repr__(None self)"""
        return str()
    def __str__(self):
        """str QByteArray.__str__(None self)"""
        return str()
    def __hash__(self):
        """int QByteArray.__hash__(None self)"""
        return int()
    def __contains__(self, _a):
        """int QByteArray.__contains__(None self, QByteArray _a)"""
        return int()
    def __getitem__(self, _i):
        """str QByteArray.__getitem__(None self, int _i)"""
        return str()
    def __getitem__(self, _slice):
        """QByteArray QByteArray.__getitem__(None self, slice _slice)"""
        return QByteArray()
    def at(self, _i):
        """str QByteArray.at(None self, int _i)"""
        return str()
    def size(self):
        """int QByteArray.size(None self)"""
        return int()
    def isNull(self):
        """bool QByteArray.isNull(None self)"""
        return bool()
    def length(self):
        """int QByteArray.length(None self)"""
        return int()
    def __len__(self):
        """ QByteArray.__len__(None self)"""
        return ()
    def fromHex(self, _hexEncoded):
        """QByteArray QByteArray.fromHex(None self, QByteArray _hexEncoded)"""
        return QByteArray()
    def fromRawData(self):
        """str QByteArray.fromRawData(None self)"""
        return str()
    def fromBase64(self, _base64):
        """QByteArray QByteArray.fromBase64(None self, QByteArray _base64)"""
        return QByteArray()
    def number(self, _n, _base):
        """QByteArray QByteArray.number(None self, int _n, int _base)"""
        return QByteArray()
    def number(self, _n, _format, _precision):
        """QByteArray QByteArray.number(None self, float _n, str _format, int _precision)"""
        return QByteArray()
    def number(self, _n, _base):
        """QByteArray QByteArray.number(None self, int _n, int _base)"""
        return QByteArray()
    def number(self, _n, _base):
        """QByteArray QByteArray.number(None self, int _n, int _base)"""
        return QByteArray()
    def setNum(self, _n, _base):
        """QByteArray QByteArray.setNum(None self, int _n, int _base)"""
        return QByteArray()
    def setNum(self, _n, _format, _precision):
        """QByteArray QByteArray.setNum(None self, float _n, str _format, int _precision)"""
        return QByteArray()
    def setNum(self, _n, _base):
        """QByteArray QByteArray.setNum(None self, int _n, int _base)"""
        return QByteArray()
    def setNum(self, _n, _base):
        """QByteArray QByteArray.setNum(None self, int _n, int _base)"""
        return QByteArray()
    def toBase64(self):
        """QByteArray QByteArray.toBase64(None self)"""
        return QByteArray()
    def toDouble(self, _ok):
        """float QByteArray.toDouble(None self, bool _ok)"""
        return float()
    def toFloat(self, _ok):
        """float QByteArray.toFloat(None self, bool _ok)"""
        return float()
    def toULongLong(self, _ok, _base):
        """int QByteArray.toULongLong(None self, bool _ok, int _base)"""
        return int()
    def toLongLong(self, _ok, _base):
        """int QByteArray.toLongLong(None self, bool _ok, int _base)"""
        return int()
    def toULong(self, _ok, _base):
        """int QByteArray.toULong(None self, bool _ok, int _base)"""
        return int()
    def toLong(self, _ok, _base):
        """int QByteArray.toLong(None self, bool _ok, int _base)"""
        return int()
    def toUInt(self, _ok, _base):
        """int QByteArray.toUInt(None self, bool _ok, int _base)"""
        return int()
    def toInt(self, _ok, _base):
        """int QByteArray.toInt(None self, bool _ok, int _base)"""
        return int()
    def toUShort(self, _ok, _base):
        """int QByteArray.toUShort(None self, bool _ok, int _base)"""
        return int()
    def toShort(self, _ok, _base):
        """int QByteArray.toShort(None self, bool _ok, int _base)"""
        return int()
    def __ge__(self, _s2):
        """bool QByteArray.__ge__(None self, QString _s2)"""
        return bool()
    def __ge__(self, _a2):
        """bool QByteArray.__ge__(None self, QByteArray _a2)"""
        return bool()
    def __le__(self, _s2):
        """bool QByteArray.__le__(None self, QString _s2)"""
        return bool()
    def __le__(self, _a2):
        """bool QByteArray.__le__(None self, QByteArray _a2)"""
        return bool()
    def __gt__(self, _s2):
        """bool QByteArray.__gt__(None self, QString _s2)"""
        return bool()
    def __gt__(self, _a2):
        """bool QByteArray.__gt__(None self, QByteArray _a2)"""
        return bool()
    def __lt__(self, _s2):
        """bool QByteArray.__lt__(None self, QString _s2)"""
        return bool()
    def __lt__(self, _a2):
        """bool QByteArray.__lt__(None self, QByteArray _a2)"""
        return bool()
    def __ne__(self, _s2):
        """bool QByteArray.__ne__(None self, QString _s2)"""
        return bool()
    def __ne__(self, _a2):
        """bool QByteArray.__ne__(None self, QByteArray _a2)"""
        return bool()
    def __eq__(self, _s2):
        """bool QByteArray.__eq__(None self, QString _s2)"""
        return bool()
    def __eq__(self, _a2):
        """bool QByteArray.__eq__(None self, QByteArray _a2)"""
        return bool()
    def __iadd__(self, _a):
        """QByteArray QByteArray.__iadd__(None self, QByteArray _a)"""
        return QByteArray()
    def __iadd__(self, _s):
        """QByteArray QByteArray.__iadd__(None self, QString _s)"""
        return QByteArray()
    def split(self, _sep):
        """list-of-QByteArray QByteArray.split(None self, str _sep)"""
        return [QByteArray()]
    def replace(self, _index, _len, _s):
        """QByteArray QByteArray.replace(None self, int _index, int _len, QByteArray _s)"""
        return QByteArray()
    def replace(self, _before, _after):
        """QByteArray QByteArray.replace(None self, QByteArray _before, QByteArray _after)"""
        return QByteArray()
    def replace(self, _before, _after):
        """QByteArray QByteArray.replace(None self, QString _before, QByteArray _after)"""
        return QByteArray()
    def remove(self, _index, _len):
        """QByteArray QByteArray.remove(None self, int _index, int _len)"""
        return QByteArray()
    def insert(self, _i, _a):
        """QByteArray QByteArray.insert(None self, int _i, QByteArray _a)"""
        return QByteArray()
    def insert(self, _i, _s):
        """QByteArray QByteArray.insert(None self, int _i, QString _s)"""
        return QByteArray()
    def append(self, _a):
        """QByteArray QByteArray.append(None self, QByteArray _a)"""
        return QByteArray()
    def append(self, _s):
        """QByteArray QByteArray.append(None self, QString _s)"""
        return QByteArray()
    def prepend(self, _a):
        """QByteArray QByteArray.prepend(None self, QByteArray _a)"""
        return QByteArray()
    def rightJustified(self, _width, _fill, _truncate):
        """QByteArray QByteArray.rightJustified(None self, int _width, str _fill, bool _truncate)"""
        return QByteArray()
    def leftJustified(self, _width, _fill, _truncate):
        """QByteArray QByteArray.leftJustified(None self, int _width, str _fill, bool _truncate)"""
        return QByteArray()
    def simplified(self):
        """QByteArray QByteArray.simplified(None self)"""
        return QByteArray()
    def trimmed(self):
        """QByteArray QByteArray.trimmed(None self)"""
        return QByteArray()
    def toUpper(self):
        """QByteArray QByteArray.toUpper(None self)"""
        return QByteArray()
    def toLower(self):
        """QByteArray QByteArray.toLower(None self)"""
        return QByteArray()
    def chop(self, _n):
        """None QByteArray.chop(None self, int _n)"""
        return None
    def truncate(self, _pos):
        """None QByteArray.truncate(None self, int _pos)"""
        return None
    def endsWith(self, _a):
        """bool QByteArray.endsWith(None self, QByteArray _a)"""
        return bool()
    def startsWith(self, _a):
        """bool QByteArray.startsWith(None self, QByteArray _a)"""
        return bool()
    def mid(self, _pos, _length):
        """QByteArray QByteArray.mid(None self, int _pos, int _length)"""
        return QByteArray()
    def right(self, _len):
        """QByteArray QByteArray.right(None self, int _len)"""
        return QByteArray()
    def left(self, _len):
        """QByteArray QByteArray.left(None self, int _len)"""
        return QByteArray()
    def count(self, _a):
        """int QByteArray.count(None self, QByteArray _a)"""
        return int()
    def count(self):
        """int QByteArray.count(None self)"""
        return int()
    def lastIndexOf(self, _ba, _from):
        """int QByteArray.lastIndexOf(None self, QByteArray _ba, int _from)"""
        return int()
    def lastIndexOf(self, _str, _from):
        """int QByteArray.lastIndexOf(None self, QString _str, int _from)"""
        return int()
    def indexOf(self, _ba, _from):
        """int QByteArray.indexOf(None self, QByteArray _ba, int _from)"""
        return int()
    def indexOf(self, _str, _from):
        """int QByteArray.indexOf(None self, QString _str, int _from)"""
        return int()
    def clear(self):
        """None QByteArray.clear(None self)"""
        return None
    def fill(self, _ch, _size):
        """QByteArray QByteArray.fill(None self, str _ch, int _size)"""
        return QByteArray()
    def resize(self, _size):
        """None QByteArray.resize(None self, int _size)"""
        return None


class QByteArrayMatcher():
    """"""
    def __init__(self):
        """None QByteArrayMatcher.__init__(None self)"""
        return None
    def __init__(self, _pattern):
        """None QByteArrayMatcher.__init__(None self, QByteArray _pattern)"""
        return None
    def __init__(self, _other):
        """None QByteArrayMatcher.__init__(None self, QByteArrayMatcher _other)"""
        return None
    def pattern(self):
        """QByteArray QByteArrayMatcher.pattern(None self)"""
        return QByteArray()
    def indexIn(self, _ba, _from):
        """int QByteArrayMatcher.indexIn(None self, QByteArray _ba, int _from)"""
        return int()
    def setPattern(self, _pattern):
        """None QByteArrayMatcher.setPattern(None self, QByteArray _pattern)"""
        return None


class QLatin1Char():
    """"""
    def __init__(self, _c):
        """None QLatin1Char.__init__(None self, str _c)"""
        return None
    def __init__(self):
        """QLatin1Char QLatin1Char.__init__(None self)"""
        return QLatin1Char()
    def unicode(self):
        """int QLatin1Char.unicode(None self)"""
        return int()
    def toLatin1(self):
        """str QLatin1Char.toLatin1(None self)"""
        return str()
    def __repr__(self):
        """str QLatin1Char.__repr__(None self)"""
        return str()


class QChar():
    """"""
    Unicode_Unassigned = int() # QChar.UnicodeVersion enum
    Unicode_1_1 = int() # QChar.UnicodeVersion enum
    Unicode_2_0 = int() # QChar.UnicodeVersion enum
    Unicode_2_1_2 = int() # QChar.UnicodeVersion enum
    Unicode_3_0 = int() # QChar.UnicodeVersion enum
    Unicode_3_1 = int() # QChar.UnicodeVersion enum
    Unicode_3_2 = int() # QChar.UnicodeVersion enum
    Unicode_4_0 = int() # QChar.UnicodeVersion enum
    Unicode_4_1 = int() # QChar.UnicodeVersion enum
    Unicode_5_0 = int() # QChar.UnicodeVersion enum

    Combining_BelowLeftAttached = int() # QChar.CombiningClass enum
    Combining_BelowAttached = int() # QChar.CombiningClass enum
    Combining_BelowRightAttached = int() # QChar.CombiningClass enum
    Combining_LeftAttached = int() # QChar.CombiningClass enum
    Combining_RightAttached = int() # QChar.CombiningClass enum
    Combining_AboveLeftAttached = int() # QChar.CombiningClass enum
    Combining_AboveAttached = int() # QChar.CombiningClass enum
    Combining_AboveRightAttached = int() # QChar.CombiningClass enum
    Combining_BelowLeft = int() # QChar.CombiningClass enum
    Combining_Below = int() # QChar.CombiningClass enum
    Combining_BelowRight = int() # QChar.CombiningClass enum
    Combining_Left = int() # QChar.CombiningClass enum
    Combining_Right = int() # QChar.CombiningClass enum
    Combining_AboveLeft = int() # QChar.CombiningClass enum
    Combining_Above = int() # QChar.CombiningClass enum
    Combining_AboveRight = int() # QChar.CombiningClass enum
    Combining_DoubleBelow = int() # QChar.CombiningClass enum
    Combining_DoubleAbove = int() # QChar.CombiningClass enum
    Combining_IotaSubscript = int() # QChar.CombiningClass enum

    OtherJoining = int() # QChar.Joining enum
    Dual = int() # QChar.Joining enum
    Right = int() # QChar.Joining enum
    Center = int() # QChar.Joining enum

    NoDecomposition = int() # QChar.Decomposition enum
    Canonical = int() # QChar.Decomposition enum
    Font = int() # QChar.Decomposition enum
    NoBreak = int() # QChar.Decomposition enum
    Initial = int() # QChar.Decomposition enum
    Medial = int() # QChar.Decomposition enum
    Final = int() # QChar.Decomposition enum
    Isolated = int() # QChar.Decomposition enum
    Circle = int() # QChar.Decomposition enum
    Super = int() # QChar.Decomposition enum
    Sub = int() # QChar.Decomposition enum
    Vertical = int() # QChar.Decomposition enum
    Wide = int() # QChar.Decomposition enum
    Narrow = int() # QChar.Decomposition enum
    Small = int() # QChar.Decomposition enum
    Square = int() # QChar.Decomposition enum
    Compat = int() # QChar.Decomposition enum
    Fraction = int() # QChar.Decomposition enum

    DirL = int() # QChar.Direction enum
    DirR = int() # QChar.Direction enum
    DirEN = int() # QChar.Direction enum
    DirES = int() # QChar.Direction enum
    DirET = int() # QChar.Direction enum
    DirAN = int() # QChar.Direction enum
    DirCS = int() # QChar.Direction enum
    DirB = int() # QChar.Direction enum
    DirS = int() # QChar.Direction enum
    DirWS = int() # QChar.Direction enum
    DirON = int() # QChar.Direction enum
    DirLRE = int() # QChar.Direction enum
    DirLRO = int() # QChar.Direction enum
    DirAL = int() # QChar.Direction enum
    DirRLE = int() # QChar.Direction enum
    DirRLO = int() # QChar.Direction enum
    DirPDF = int() # QChar.Direction enum
    DirNSM = int() # QChar.Direction enum
    DirBN = int() # QChar.Direction enum

    NoCategory = int() # QChar.Category enum
    Mark_NonSpacing = int() # QChar.Category enum
    Mark_SpacingCombining = int() # QChar.Category enum
    Mark_Enclosing = int() # QChar.Category enum
    Number_DecimalDigit = int() # QChar.Category enum
    Number_Letter = int() # QChar.Category enum
    Number_Other = int() # QChar.Category enum
    Separator_Space = int() # QChar.Category enum
    Separator_Line = int() # QChar.Category enum
    Separator_Paragraph = int() # QChar.Category enum
    Other_Control = int() # QChar.Category enum
    Other_Format = int() # QChar.Category enum
    Other_Surrogate = int() # QChar.Category enum
    Other_PrivateUse = int() # QChar.Category enum
    Other_NotAssigned = int() # QChar.Category enum
    Letter_Uppercase = int() # QChar.Category enum
    Letter_Lowercase = int() # QChar.Category enum
    Letter_Titlecase = int() # QChar.Category enum
    Letter_Modifier = int() # QChar.Category enum
    Letter_Other = int() # QChar.Category enum
    Punctuation_Connector = int() # QChar.Category enum
    Punctuation_Dash = int() # QChar.Category enum
    Punctuation_Open = int() # QChar.Category enum
    Punctuation_Close = int() # QChar.Category enum
    Punctuation_InitialQuote = int() # QChar.Category enum
    Punctuation_FinalQuote = int() # QChar.Category enum
    Punctuation_Other = int() # QChar.Category enum
    Symbol_Math = int() # QChar.Category enum
    Symbol_Currency = int() # QChar.Category enum
    Symbol_Modifier = int() # QChar.Category enum
    Symbol_Other = int() # QChar.Category enum
    Punctuation_Dask = int() # QChar.Category enum

    Null = int() # QChar.SpecialCharacter enum
    Nbsp = int() # QChar.SpecialCharacter enum
    ReplacementCharacter = int() # QChar.SpecialCharacter enum
    ObjectReplacementCharacter = int() # QChar.SpecialCharacter enum
    ByteOrderMark = int() # QChar.SpecialCharacter enum
    ByteOrderSwapped = int() # QChar.SpecialCharacter enum
    ParagraphSeparator = int() # QChar.SpecialCharacter enum
    LineSeparator = int() # QChar.SpecialCharacter enum

    def __init__(self):
        """None QChar.__init__(None self)"""
        return None
    def __init__(self, _c):
        """None QChar.__init__(None self, str _c)"""
        return None
    def __init__(self, _ch):
        """None QChar.__init__(None self, QLatin1Char _ch)"""
        return None
    def __init__(self, _c, _r):
        """None QChar.__init__(None self, str _c, str _r)"""
        return None
    def __init__(self, _rc):
        """None QChar.__init__(None self, int _rc)"""
        return None
    def __init__(self, _s):
        """None QChar.__init__(None self, QChar.SpecialCharacter _s)"""
        return None
    def __init__(self):
        """QChar QChar.__init__(None self)"""
        return QChar()
    def __eq__(self, _c2):
        """bool QChar.__eq__(None self, QChar _c2)"""
        return bool()
    def __ne__(self, _c2):
        """bool QChar.__ne__(None self, QChar _c2)"""
        return bool()
    def __lt__(self, _c2):
        """bool QChar.__lt__(None self, QChar _c2)"""
        return bool()
    def __le__(self, _c2):
        """bool QChar.__le__(None self, QChar _c2)"""
        return bool()
    def __gt__(self, _c2):
        """bool QChar.__gt__(None self, QChar _c2)"""
        return bool()
    def __ge__(self, _c2):
        """bool QChar.__ge__(None self, QChar _c2)"""
        return bool()
    def __add__(self, _s2):
        """QString QChar.__add__(None self, QString _s2)"""
        return QString()
    def requiresSurrogates(self, _ucs4):
        """bool QChar.requiresSurrogates(None self, int _ucs4)"""
        return bool()
    def lowSurrogate(self, _ucs4):
        """int QChar.lowSurrogate(None self, int _ucs4)"""
        return int()
    def highSurrogate(self, _ucs4):
        """int QChar.highSurrogate(None self, int _ucs4)"""
        return int()
    def surrogateToUcs4(self, _high, _low):
        """int QChar.surrogateToUcs4(None self, int _high, int _low)"""
        return int()
    def surrogateToUcs4(self, _high, _low):
        """int QChar.surrogateToUcs4(None self, QChar _high, QChar _low)"""
        return int()
    def isLowSurrogate(self):
        """bool QChar.isLowSurrogate(None self)"""
        return bool()
    def isLowSurrogate(self, _ucs4):
        """bool QChar.isLowSurrogate(None self, int _ucs4)"""
        return bool()
    def isHighSurrogate(self):
        """bool QChar.isHighSurrogate(None self)"""
        return bool()
    def isHighSurrogate(self, _ucs4):
        """bool QChar.isHighSurrogate(None self, int _ucs4)"""
        return bool()
    def isTitleCase(self):
        """bool QChar.isTitleCase(None self)"""
        return bool()
    def toCaseFolded(self):
        """QChar QChar.toCaseFolded(None self)"""
        return QChar()
    def toCaseFolded(self, _ucs4):
        """int QChar.toCaseFolded(None self, int _ucs4)"""
        return int()
    def toTitleCase(self):
        """QChar QChar.toTitleCase(None self)"""
        return QChar()
    def toTitleCase(self, _ucs4):
        """int QChar.toTitleCase(None self, int _ucs4)"""
        return int()
    def setRow(self, _arow):
        """None QChar.setRow(None self, str _arow)"""
        return None
    def setCell(self, _acell):
        """None QChar.setCell(None self, str _acell)"""
        return None
    def fromLatin1(self, _c):
        """QChar QChar.fromLatin1(None self, str _c)"""
        return QChar()
    def toLatin1(self):
        """str QChar.toLatin1(None self)"""
        return str()
    def row(self):
        """str QChar.row(None self)"""
        return str()
    def cell(self):
        """str QChar.cell(None self)"""
        return str()
    def isSymbol(self):
        """bool QChar.isSymbol(None self)"""
        return bool()
    def isDigit(self):
        """bool QChar.isDigit(None self)"""
        return bool()
    def isLetterOrNumber(self):
        """bool QChar.isLetterOrNumber(None self)"""
        return bool()
    def isNumber(self):
        """bool QChar.isNumber(None self)"""
        return bool()
    def isLetter(self):
        """bool QChar.isLetter(None self)"""
        return bool()
    def isMark(self):
        """bool QChar.isMark(None self)"""
        return bool()
    def isSpace(self):
        """bool QChar.isSpace(None self)"""
        return bool()
    def isPunct(self):
        """bool QChar.isPunct(None self)"""
        return bool()
    def isPrint(self):
        """bool QChar.isPrint(None self)"""
        return bool()
    def isNull(self):
        """bool QChar.isNull(None self)"""
        return bool()
    def fromAscii(self, _c):
        """QChar QChar.fromAscii(None self, str _c)"""
        return QChar()
    def unicode(self):
        """int QChar.unicode(None self)"""
        return int()
    def toAscii(self):
        """str QChar.toAscii(None self)"""
        return str()
    def unicodeVersion(self):
        """QChar.UnicodeVersion QChar.unicodeVersion(None self)"""
        return QChar.UnicodeVersion()
    def unicodeVersion(self, _ucs4):
        """QChar.UnicodeVersion QChar.unicodeVersion(None self, int _ucs4)"""
        return QChar.UnicodeVersion()
    def combiningClass(self):
        """str QChar.combiningClass(None self)"""
        return str()
    def combiningClass(self, _ucs4):
        """str QChar.combiningClass(None self, int _ucs4)"""
        return str()
    def decompositionTag(self):
        """QChar.Decomposition QChar.decompositionTag(None self)"""
        return QChar.Decomposition()
    def decompositionTag(self, _ucs4):
        """QChar.Decomposition QChar.decompositionTag(None self, int _ucs4)"""
        return QChar.Decomposition()
    def decomposition(self):
        """QString QChar.decomposition(None self)"""
        return QString()
    def decomposition(self, _ucs4):
        """QString QChar.decomposition(None self, int _ucs4)"""
        return QString()
    def mirroredChar(self):
        """QChar QChar.mirroredChar(None self)"""
        return QChar()
    def mirroredChar(self, _ucs4):
        """int QChar.mirroredChar(None self, int _ucs4)"""
        return int()
    def isUpper(self):
        """bool QChar.isUpper(None self)"""
        return bool()
    def isLower(self):
        """bool QChar.isLower(None self)"""
        return bool()
    def hasMirrored(self):
        """bool QChar.hasMirrored(None self)"""
        return bool()
    def joining(self):
        """QChar.Joining QChar.joining(None self)"""
        return QChar.Joining()
    def joining(self, _ucs4):
        """QChar.Joining QChar.joining(None self, int _ucs4)"""
        return QChar.Joining()
    def direction(self):
        """QChar.Direction QChar.direction(None self)"""
        return QChar.Direction()
    def direction(self, _ucs4):
        """QChar.Direction QChar.direction(None self, int _ucs4)"""
        return QChar.Direction()
    def category(self):
        """QChar.Category QChar.category(None self)"""
        return QChar.Category()
    def category(self, _ucs4):
        """QChar.Category QChar.category(None self, int _ucs4)"""
        return QChar.Category()
    def toUpper(self):
        """QChar QChar.toUpper(None self)"""
        return QChar()
    def toUpper(self, _ucs4):
        """int QChar.toUpper(None self, int _ucs4)"""
        return int()
    def toLower(self):
        """QChar QChar.toLower(None self)"""
        return QChar()
    def toLower(self, _ucs4):
        """int QChar.toLower(None self, int _ucs4)"""
        return int()
    def digitValue(self):
        """int QChar.digitValue(None self)"""
        return int()
    def digitValue(self, _ucs4):
        """int QChar.digitValue(None self, int _ucs4)"""
        return int()
    def __hash__(self):
        """int QChar.__hash__(None self)"""
        return int()
    def __repr__(self):
        """str QChar.__repr__(None self)"""
        return str()


class QCoreApplication(QObject):
    """"""
    CodecForTr = int() # QCoreApplication.Encoding enum
    UnicodeUTF8 = int() # QCoreApplication.Encoding enum
    DefaultCodec = int() # QCoreApplication.Encoding enum

    def __init__(self, _argv):
        """None QCoreApplication.__init__(None self, list-of-str _argv)"""
        return None
    def applicationPid(self):
        """int QCoreApplication.applicationPid(None self)"""
        return int()
    def applicationVersion(self):
        """QString QCoreApplication.applicationVersion(None self)"""
        return QString()
    def setApplicationVersion(self, _version):
        """None QCoreApplication.setApplicationVersion(None self, QString _version)"""
        return None
    def event(self):
        """QEvent QCoreApplication.event(None self)"""
        return QEvent()
    def quit(self):
        """None QCoreApplication.quit(None self)"""
        return None
    def testAttribute(self, _attribute):
        """bool QCoreApplication.testAttribute(None self, Qt.ApplicationAttribute _attribute)"""
        return bool()
    def setAttribute(self, _attribute, _on):
        """None QCoreApplication.setAttribute(None self, Qt.ApplicationAttribute _attribute, bool _on)"""
        return None
    def flush(self):
        """None QCoreApplication.flush(None self)"""
        return None
    def translate(self, _context, _sourceText, _disambiguation, _encoding):
        """QString QCoreApplication.translate(None self, str _context, str _sourceText, str _disambiguation, QCoreApplication.Encoding _encoding)"""
        return QString()
    def translate(self, _context, _sourceText, _disambiguation, _encoding, _n):
        """QString QCoreApplication.translate(None self, str _context, str _sourceText, str _disambiguation, QCoreApplication.Encoding _encoding, int _n)"""
        return QString()
    def removeTranslator(self):
        """QTranslator QCoreApplication.removeTranslator(None self)"""
        return QTranslator()
    def installTranslator(self):
        """QTranslator QCoreApplication.installTranslator(None self)"""
        return QTranslator()
    def removeLibraryPath(self):
        """QString QCoreApplication.removeLibraryPath(None self)"""
        return QString()
    def addLibraryPath(self):
        """QString QCoreApplication.addLibraryPath(None self)"""
        return QString()
    def libraryPaths(self):
        """QStringList QCoreApplication.libraryPaths(None self)"""
        return QStringList()
    def setLibraryPaths(self):
        """QStringList QCoreApplication.setLibraryPaths(None self)"""
        return QStringList()
    def applicationFilePath(self):
        """QString QCoreApplication.applicationFilePath(None self)"""
        return QString()
    def applicationDirPath(self):
        """QString QCoreApplication.applicationDirPath(None self)"""
        return QString()
    def closingDown(self):
        """bool QCoreApplication.closingDown(None self)"""
        return bool()
    def startingUp(self):
        """bool QCoreApplication.startingUp(None self)"""
        return bool()
    def notify(self):
        """QEvent QCoreApplication.notify(None self)"""
        return QEvent()
    def hasPendingEvents(self):
        """bool QCoreApplication.hasPendingEvents(None self)"""
        return bool()
    def removePostedEvents(self, _receiver):
        """None QCoreApplication.removePostedEvents(None self, QObject _receiver)"""
        return None
    def removePostedEvents(self, _receiver, _eventType):
        """None QCoreApplication.removePostedEvents(None self, QObject _receiver, int _eventType)"""
        return None
    def sendPostedEvents(self, _receiver, _event_type):
        """None QCoreApplication.sendPostedEvents(None self, QObject _receiver, int _event_type)"""
        return None
    def sendPostedEvents(self):
        """None QCoreApplication.sendPostedEvents(None self)"""
        return None
    def postEvent(self, _receiver, _event):
        """None QCoreApplication.postEvent(None self, QObject _receiver, QEvent _event)"""
        return None
    def postEvent(self, _receiver, _event, _priority):
        """None QCoreApplication.postEvent(None self, QObject _receiver, QEvent _event, int _priority)"""
        return None
    def sendEvent(self, _receiver, _event):
        """bool QCoreApplication.sendEvent(None self, QObject _receiver, QEvent _event)"""
        return bool()
    def exit(self, _returnCode):
        """None QCoreApplication.exit(None self, int _returnCode)"""
        return None
    def processEvents(self, _flags):
        """None QCoreApplication.processEvents(None self, QEventLoop.ProcessEventsFlags _flags)"""
        return None
    def processEvents(self, _flags, _maxtime):
        """None QCoreApplication.processEvents(None self, QEventLoop.ProcessEventsFlags _flags, int _maxtime)"""
        return None
    def exec_(self):
        """int QCoreApplication.exec_(None self)"""
        return int()
    def instance(self):
        """QCoreApplication QCoreApplication.instance(None self)"""
        return QCoreApplication()
    def arguments(self):
        """QStringList QCoreApplication.arguments(None self)"""
        return QStringList()
    def applicationName(self):
        """QString QCoreApplication.applicationName(None self)"""
        return QString()
    def setApplicationName(self, _application):
        """None QCoreApplication.setApplicationName(None self, QString _application)"""
        return None
    def organizationName(self):
        """QString QCoreApplication.organizationName(None self)"""
        return QString()
    def setOrganizationName(self, _orgName):
        """None QCoreApplication.setOrganizationName(None self, QString _orgName)"""
        return None
    def organizationDomain(self):
        """QString QCoreApplication.organizationDomain(None self)"""
        return QString()
    def setOrganizationDomain(self, _orgDomain):
        """None QCoreApplication.setOrganizationDomain(None self, QString _orgDomain)"""
        return None
    def argv(self):
        """list-of-str QCoreApplication.argv(None self)"""
        return [str()]
    def argc(self):
        """int QCoreApplication.argc(None self)"""
        return int()


class QEvent():
    """"""
    __kdevpythondocumentation_builtin_None = int() # QEvent.Type enum
    Timer = int() # QEvent.Type enum
    MouseButtonPress = int() # QEvent.Type enum
    MouseButtonRelease = int() # QEvent.Type enum
    MouseButtonDblClick = int() # QEvent.Type enum
    MouseMove = int() # QEvent.Type enum
    KeyPress = int() # QEvent.Type enum
    KeyRelease = int() # QEvent.Type enum
    FocusIn = int() # QEvent.Type enum
    FocusOut = int() # QEvent.Type enum
    Enter = int() # QEvent.Type enum
    Leave = int() # QEvent.Type enum
    Paint = int() # QEvent.Type enum
    Move = int() # QEvent.Type enum
    Resize = int() # QEvent.Type enum
    Show = int() # QEvent.Type enum
    Hide = int() # QEvent.Type enum
    Close = int() # QEvent.Type enum
    ParentChange = int() # QEvent.Type enum
    ParentAboutToChange = int() # QEvent.Type enum
    WindowActivate = int() # QEvent.Type enum
    WindowDeactivate = int() # QEvent.Type enum
    ShowToParent = int() # QEvent.Type enum
    HideToParent = int() # QEvent.Type enum
    Wheel = int() # QEvent.Type enum
    WindowTitleChange = int() # QEvent.Type enum
    WindowIconChange = int() # QEvent.Type enum
    ApplicationWindowIconChange = int() # QEvent.Type enum
    ApplicationFontChange = int() # QEvent.Type enum
    ApplicationLayoutDirectionChange = int() # QEvent.Type enum
    ApplicationPaletteChange = int() # QEvent.Type enum
    PaletteChange = int() # QEvent.Type enum
    Clipboard = int() # QEvent.Type enum
    MetaCall = int() # QEvent.Type enum
    SockAct = int() # QEvent.Type enum
    WinEventAct = int() # QEvent.Type enum
    DeferredDelete = int() # QEvent.Type enum
    DragEnter = int() # QEvent.Type enum
    DragMove = int() # QEvent.Type enum
    DragLeave = int() # QEvent.Type enum
    Drop = int() # QEvent.Type enum
    ChildAdded = int() # QEvent.Type enum
    ChildPolished = int() # QEvent.Type enum
    ChildRemoved = int() # QEvent.Type enum
    PolishRequest = int() # QEvent.Type enum
    Polish = int() # QEvent.Type enum
    LayoutRequest = int() # QEvent.Type enum
    UpdateRequest = int() # QEvent.Type enum
    UpdateLater = int() # QEvent.Type enum
    ContextMenu = int() # QEvent.Type enum
    InputMethod = int() # QEvent.Type enum
    AccessibilityPrepare = int() # QEvent.Type enum
    TabletMove = int() # QEvent.Type enum
    LocaleChange = int() # QEvent.Type enum
    LanguageChange = int() # QEvent.Type enum
    LayoutDirectionChange = int() # QEvent.Type enum
    TabletPress = int() # QEvent.Type enum
    TabletRelease = int() # QEvent.Type enum
    OkRequest = int() # QEvent.Type enum
    IconDrag = int() # QEvent.Type enum
    FontChange = int() # QEvent.Type enum
    EnabledChange = int() # QEvent.Type enum
    ActivationChange = int() # QEvent.Type enum
    StyleChange = int() # QEvent.Type enum
    IconTextChange = int() # QEvent.Type enum
    ModifiedChange = int() # QEvent.Type enum
    MouseTrackingChange = int() # QEvent.Type enum
    WindowBlocked = int() # QEvent.Type enum
    WindowUnblocked = int() # QEvent.Type enum
    WindowStateChange = int() # QEvent.Type enum
    ToolTip = int() # QEvent.Type enum
    WhatsThis = int() # QEvent.Type enum
    StatusTip = int() # QEvent.Type enum
    ActionChanged = int() # QEvent.Type enum
    ActionAdded = int() # QEvent.Type enum
    ActionRemoved = int() # QEvent.Type enum
    FileOpen = int() # QEvent.Type enum
    Shortcut = int() # QEvent.Type enum
    ShortcutOverride = int() # QEvent.Type enum
    WhatsThisClicked = int() # QEvent.Type enum
    ToolBarChange = int() # QEvent.Type enum
    ApplicationActivate = int() # QEvent.Type enum
    ApplicationActivated = int() # QEvent.Type enum
    ApplicationDeactivate = int() # QEvent.Type enum
    ApplicationDeactivated = int() # QEvent.Type enum
    QueryWhatsThis = int() # QEvent.Type enum
    EnterWhatsThisMode = int() # QEvent.Type enum
    LeaveWhatsThisMode = int() # QEvent.Type enum
    ZOrderChange = int() # QEvent.Type enum
    HoverEnter = int() # QEvent.Type enum
    HoverLeave = int() # QEvent.Type enum
    HoverMove = int() # QEvent.Type enum
    AccessibilityHelp = int() # QEvent.Type enum
    AccessibilityDescription = int() # QEvent.Type enum
    MenubarUpdated = int() # QEvent.Type enum
    GraphicsSceneMouseMove = int() # QEvent.Type enum
    GraphicsSceneMousePress = int() # QEvent.Type enum
    GraphicsSceneMouseRelease = int() # QEvent.Type enum
    GraphicsSceneMouseDoubleClick = int() # QEvent.Type enum
    GraphicsSceneContextMenu = int() # QEvent.Type enum
    GraphicsSceneHoverEnter = int() # QEvent.Type enum
    GraphicsSceneHoverMove = int() # QEvent.Type enum
    GraphicsSceneHoverLeave = int() # QEvent.Type enum
    GraphicsSceneHelp = int() # QEvent.Type enum
    GraphicsSceneDragEnter = int() # QEvent.Type enum
    GraphicsSceneDragMove = int() # QEvent.Type enum
    GraphicsSceneDragLeave = int() # QEvent.Type enum
    GraphicsSceneDrop = int() # QEvent.Type enum
    GraphicsSceneWheel = int() # QEvent.Type enum
    GraphicsSceneResize = int() # QEvent.Type enum
    GraphicsSceneMove = int() # QEvent.Type enum
    KeyboardLayoutChange = int() # QEvent.Type enum
    DynamicPropertyChange = int() # QEvent.Type enum
    TabletEnterProximity = int() # QEvent.Type enum
    TabletLeaveProximity = int() # QEvent.Type enum
    CursorChange = int() # QEvent.Type enum
    ToolTipChange = int() # QEvent.Type enum
    GrabMouse = int() # QEvent.Type enum
    UngrabMouse = int() # QEvent.Type enum
    GrabKeyboard = int() # QEvent.Type enum
    UngrabKeyboard = int() # QEvent.Type enum
    StateMachineSignal = int() # QEvent.Type enum
    StateMachineWrapped = int() # QEvent.Type enum
    TouchBegin = int() # QEvent.Type enum
    TouchUpdate = int() # QEvent.Type enum
    TouchEnd = int() # QEvent.Type enum
    RequestSoftwareInputPanel = int() # QEvent.Type enum
    CloseSoftwareInputPanel = int() # QEvent.Type enum
    WinIdChange = int() # QEvent.Type enum
    Gesture = int() # QEvent.Type enum
    GestureOverride = int() # QEvent.Type enum
    User = int() # QEvent.Type enum
    MaxUser = int() # QEvent.Type enum

    def __init__(self, _type):
        """None QEvent.__init__(None self, QEvent.Type _type)"""
        return None
    def __init__(self):
        """QEvent QEvent.__init__(None self)"""
        return QEvent()
    def registerEventType(self, _hint):
        """int QEvent.registerEventType(None self, int _hint)"""
        return int()
    def ignore(self):
        """None QEvent.ignore(None self)"""
        return None
    def accept(self):
        """None QEvent.accept(None self)"""
        return None
    def isAccepted(self):
        """bool QEvent.isAccepted(None self)"""
        return bool()
    def setAccepted(self, _accepted):
        """None QEvent.setAccepted(None self, bool _accepted)"""
        return None
    def spontaneous(self):
        """bool QEvent.spontaneous(None self)"""
        return bool()
    def type(self):
        """QEvent.Type QEvent.type(None self)"""
        return QEvent.Type()


class QTimerEvent(QEvent):
    """"""
    def __init__(self, _timerId):
        """None QTimerEvent.__init__(None self, int _timerId)"""
        return None
    def __init__(self):
        """QTimerEvent QTimerEvent.__init__(None self)"""
        return QTimerEvent()
    def timerId(self):
        """int QTimerEvent.timerId(None self)"""
        return int()


class QChildEvent(QEvent):
    """"""
    def __init__(self, _type, _child):
        """None QChildEvent.__init__(None self, QEvent.Type _type, QObject _child)"""
        return None
    def __init__(self):
        """QChildEvent QChildEvent.__init__(None self)"""
        return QChildEvent()
    def removed(self):
        """bool QChildEvent.removed(None self)"""
        return bool()
    def polished(self):
        """bool QChildEvent.polished(None self)"""
        return bool()
    def added(self):
        """bool QChildEvent.added(None self)"""
        return bool()
    def child(self):
        """QObject QChildEvent.child(None self)"""
        return QObject()


class QDynamicPropertyChangeEvent(QEvent):
    """"""
    def __init__(self, _name):
        """None QDynamicPropertyChangeEvent.__init__(None self, QByteArray _name)"""
        return None
    def __init__(self):
        """QDynamicPropertyChangeEvent QDynamicPropertyChangeEvent.__init__(None self)"""
        return QDynamicPropertyChangeEvent()
    def propertyName(self):
        """QByteArray QDynamicPropertyChangeEvent.propertyName(None self)"""
        return QByteArray()


class QCryptographicHash():
    """"""
    Md4 = int() # QCryptographicHash.Algorithm enum
    Md5 = int() # QCryptographicHash.Algorithm enum
    Sha1 = int() # QCryptographicHash.Algorithm enum

    def __init__(self, _method):
        """None QCryptographicHash.__init__(None self, QCryptographicHash.Algorithm _method)"""
        return None
    def hash(self, _data, _method):
        """QByteArray QCryptographicHash.hash(None self, QByteArray _data, QCryptographicHash.Algorithm _method)"""
        return QByteArray()
    def result(self):
        """QByteArray QCryptographicHash.result(None self)"""
        return QByteArray()
    def addData(self, _data):
        """None QCryptographicHash.addData(None self, str _data)"""
        return None
    def addData(self, _data):
        """None QCryptographicHash.addData(None self, QByteArray _data)"""
        return None
    def reset(self):
        """None QCryptographicHash.reset(None self)"""
        return None


class QDataStream():
    """"""
    SinglePrecision = int() # QDataStream.FloatingPointPrecision enum
    DoublePrecision = int() # QDataStream.FloatingPointPrecision enum

    Ok = int() # QDataStream.Status enum
    ReadPastEnd = int() # QDataStream.Status enum
    ReadCorruptData = int() # QDataStream.Status enum

    BigEndian = int() # QDataStream.ByteOrder enum
    LittleEndian = int() # QDataStream.ByteOrder enum

    Qt_1_0 = int() # QDataStream.Version enum
    Qt_2_0 = int() # QDataStream.Version enum
    Qt_2_1 = int() # QDataStream.Version enum
    Qt_3_0 = int() # QDataStream.Version enum
    Qt_3_1 = int() # QDataStream.Version enum
    Qt_3_3 = int() # QDataStream.Version enum
    Qt_4_0 = int() # QDataStream.Version enum
    Qt_4_1 = int() # QDataStream.Version enum
    Qt_4_2 = int() # QDataStream.Version enum
    Qt_4_3 = int() # QDataStream.Version enum
    Qt_4_4 = int() # QDataStream.Version enum
    Qt_4_5 = int() # QDataStream.Version enum
    Qt_4_6 = int() # QDataStream.Version enum
    Qt_4_7 = int() # QDataStream.Version enum

    def __init__(self):
        """None QDataStream.__init__(None self)"""
        return None
    def __init__(self):
        """QIODevice QDataStream.__init__(None self)"""
        return QIODevice()
    def __init__(self, _flags):
        """QByteArray QDataStream.__init__(None self, QIODevice.OpenMode _flags)"""
        return QByteArray()
    def __init__(self):
        """QByteArray QDataStream.__init__(None self)"""
        return QByteArray()
    def __lshift__(self):
        """QBitArray QDataStream.__lshift__(None self)"""
        return QBitArray()
    def __lshift__(self):
        """QByteArray QDataStream.__lshift__(None self)"""
        return QByteArray()
    def __lshift__(self):
        """QChar QDataStream.__lshift__(None self)"""
        return QChar()
    def __lshift__(self):
        """QDate QDataStream.__lshift__(None self)"""
        return QDate()
    def __lshift__(self):
        """QTime QDataStream.__lshift__(None self)"""
        return QTime()
    def __lshift__(self):
        """QDateTime QDataStream.__lshift__(None self)"""
        return QDateTime()
    def __lshift__(self):
        """QEasingCurve QDataStream.__lshift__(None self)"""
        return QEasingCurve()
    def __lshift__(self):
        """QLine QDataStream.__lshift__(None self)"""
        return QLine()
    def __lshift__(self):
        """QLineF QDataStream.__lshift__(None self)"""
        return QLineF()
    def __lshift__(self):
        """QLocale QDataStream.__lshift__(None self)"""
        return QLocale()
    def __lshift__(self):
        """QPoint QDataStream.__lshift__(None self)"""
        return QPoint()
    def __lshift__(self):
        """QPointF QDataStream.__lshift__(None self)"""
        return QPointF()
    def __lshift__(self):
        """QRect QDataStream.__lshift__(None self)"""
        return QRect()
    def __lshift__(self):
        """QRectF QDataStream.__lshift__(None self)"""
        return QRectF()
    def __lshift__(self, _regExp):
        """QDataStream QDataStream.__lshift__(None self, QRegExp _regExp)"""
        return QDataStream()
    def __lshift__(self):
        """QSize QDataStream.__lshift__(None self)"""
        return QSize()
    def __lshift__(self):
        """QSizeF QDataStream.__lshift__(None self)"""
        return QSizeF()
    def __lshift__(self):
        """QString QDataStream.__lshift__(None self)"""
        return QString()
    def __lshift__(self, _list):
        """QDataStream QDataStream.__lshift__(None self, QStringList _list)"""
        return QDataStream()
    def __lshift__(self):
        """QUrl QDataStream.__lshift__(None self)"""
        return QUrl()
    def __lshift__(self):
        """QUuid QDataStream.__lshift__(None self)"""
        return QUuid()
    def __lshift__(self, _p):
        """QDataStream QDataStream.__lshift__(None self, QVariant _p)"""
        return QDataStream()
    def __lshift__(self, _p):
        """QDataStream QDataStream.__lshift__(None self, Type _p)"""
        return QDataStream()
    def __rshift__(self):
        """QBitArray QDataStream.__rshift__(None self)"""
        return QBitArray()
    def __rshift__(self):
        """QByteArray QDataStream.__rshift__(None self)"""
        return QByteArray()
    def __rshift__(self):
        """QChar QDataStream.__rshift__(None self)"""
        return QChar()
    def __rshift__(self):
        """QDate QDataStream.__rshift__(None self)"""
        return QDate()
    def __rshift__(self):
        """QTime QDataStream.__rshift__(None self)"""
        return QTime()
    def __rshift__(self):
        """QDateTime QDataStream.__rshift__(None self)"""
        return QDateTime()
    def __rshift__(self):
        """QEasingCurve QDataStream.__rshift__(None self)"""
        return QEasingCurve()
    def __rshift__(self):
        """QLine QDataStream.__rshift__(None self)"""
        return QLine()
    def __rshift__(self):
        """QLineF QDataStream.__rshift__(None self)"""
        return QLineF()
    def __rshift__(self):
        """QLocale QDataStream.__rshift__(None self)"""
        return QLocale()
    def __rshift__(self):
        """QPoint QDataStream.__rshift__(None self)"""
        return QPoint()
    def __rshift__(self):
        """QPointF QDataStream.__rshift__(None self)"""
        return QPointF()
    def __rshift__(self):
        """QRect QDataStream.__rshift__(None self)"""
        return QRect()
    def __rshift__(self):
        """QRectF QDataStream.__rshift__(None self)"""
        return QRectF()
    def __rshift__(self, _regExp):
        """QDataStream QDataStream.__rshift__(None self, QRegExp _regExp)"""
        return QDataStream()
    def __rshift__(self):
        """QSize QDataStream.__rshift__(None self)"""
        return QSize()
    def __rshift__(self):
        """QSizeF QDataStream.__rshift__(None self)"""
        return QSizeF()
    def __rshift__(self):
        """QString QDataStream.__rshift__(None self)"""
        return QString()
    def __rshift__(self, _list):
        """QDataStream QDataStream.__rshift__(None self, QStringList _list)"""
        return QDataStream()
    def __rshift__(self):
        """QUrl QDataStream.__rshift__(None self)"""
        return QUrl()
    def __rshift__(self):
        """QUuid QDataStream.__rshift__(None self)"""
        return QUuid()
    def __rshift__(self, _p):
        """QDataStream QDataStream.__rshift__(None self, QVariant _p)"""
        return QDataStream()
    def __rshift__(self, _p):
        """QDataStream QDataStream.__rshift__(None self, Type _p)"""
        return QDataStream()
    def setFloatingPointPrecision(self, _precision):
        """None QDataStream.setFloatingPointPrecision(None self, QDataStream.FloatingPointPrecision _precision)"""
        return None
    def floatingPointPrecision(self):
        """QDataStream.FloatingPointPrecision QDataStream.floatingPointPrecision(None self)"""
        return QDataStream.FloatingPointPrecision()
    def writeRawData(self):
        """str QDataStream.writeRawData(None self)"""
        return str()
    def writeBytes(self):
        """str QDataStream.writeBytes(None self)"""
        return str()
    def readRawData(self, _len):
        """str QDataStream.readRawData(None self, int _len)"""
        return str()
    def readBytes(self):
        """str QDataStream.readBytes(None self)"""
        return str()
    def writeQVariantHash(self, _qvarhash):
        """None QDataStream.writeQVariantHash(None self, dict-of-QString-QVariant _qvarhash)"""
        return None
    def readQVariantHash(self):
        """dict-of-QString-QVariant QDataStream.readQVariantHash(None self)"""
        return dict-of-QString-QVariant()
    def writeQVariantMap(self, _qvarmap):
        """None QDataStream.writeQVariantMap(None self, dict-of-QString-QVariant _qvarmap)"""
        return None
    def readQVariantMap(self):
        """dict-of-QString-QVariant QDataStream.readQVariantMap(None self)"""
        return dict-of-QString-QVariant()
    def writeQVariantList(self, _qvarlst):
        """None QDataStream.writeQVariantList(None self, list-of-QVariant _qvarlst)"""
        return None
    def readQVariantList(self):
        """list-of-QVariant QDataStream.readQVariantList(None self)"""
        return [QVariant()]
    def writeQVariant(self, _qvar):
        """None QDataStream.writeQVariant(None self, QVariant _qvar)"""
        return None
    def readQVariant(self):
        """QVariant QDataStream.readQVariant(None self)"""
        return QVariant()
    def writeQStringList(self, _qstrlst):
        """None QDataStream.writeQStringList(None self, QStringList _qstrlst)"""
        return None
    def readQStringList(self):
        """QStringList QDataStream.readQStringList(None self)"""
        return QStringList()
    def writeQString(self, _qstr):
        """None QDataStream.writeQString(None self, QString _qstr)"""
        return None
    def readQString(self):
        """QString QDataStream.readQString(None self)"""
        return QString()
    def writeString(self, _str):
        """None QDataStream.writeString(None self, str _str)"""
        return None
    def writeDouble(self, _f):
        """None QDataStream.writeDouble(None self, float _f)"""
        return None
    def writeFloat(self, _f):
        """None QDataStream.writeFloat(None self, float _f)"""
        return None
    def writeBool(self, _i):
        """None QDataStream.writeBool(None self, bool _i)"""
        return None
    def writeUInt64(self, _i):
        """None QDataStream.writeUInt64(None self, int _i)"""
        return None
    def writeInt64(self, _i):
        """None QDataStream.writeInt64(None self, int _i)"""
        return None
    def writeUInt32(self, _i):
        """None QDataStream.writeUInt32(None self, int _i)"""
        return None
    def writeInt32(self, _i):
        """None QDataStream.writeInt32(None self, int _i)"""
        return None
    def writeUInt16(self, _i):
        """None QDataStream.writeUInt16(None self, int _i)"""
        return None
    def writeInt16(self, _i):
        """None QDataStream.writeInt16(None self, int _i)"""
        return None
    def writeUInt8(self, _i):
        """None QDataStream.writeUInt8(None self, str _i)"""
        return None
    def writeInt8(self, _i):
        """None QDataStream.writeInt8(None self, str _i)"""
        return None
    def writeInt(self, _i):
        """None QDataStream.writeInt(None self, int _i)"""
        return None
    def readString(self):
        """str QDataStream.readString(None self)"""
        return str()
    def readDouble(self):
        """float QDataStream.readDouble(None self)"""
        return float()
    def readFloat(self):
        """float QDataStream.readFloat(None self)"""
        return float()
    def readBool(self):
        """bool QDataStream.readBool(None self)"""
        return bool()
    def readUInt64(self):
        """int QDataStream.readUInt64(None self)"""
        return int()
    def readInt64(self):
        """int QDataStream.readInt64(None self)"""
        return int()
    def readUInt32(self):
        """int QDataStream.readUInt32(None self)"""
        return int()
    def readInt32(self):
        """int QDataStream.readInt32(None self)"""
        return int()
    def readUInt16(self):
        """int QDataStream.readUInt16(None self)"""
        return int()
    def readInt16(self):
        """int QDataStream.readInt16(None self)"""
        return int()
    def readUInt8(self):
        """str QDataStream.readUInt8(None self)"""
        return str()
    def readInt8(self):
        """str QDataStream.readInt8(None self)"""
        return str()
    def readInt(self):
        """int QDataStream.readInt(None self)"""
        return int()
    def skipRawData(self, _len):
        """int QDataStream.skipRawData(None self, int _len)"""
        return int()
    def setVersion(self, _v):
        """None QDataStream.setVersion(None self, int _v)"""
        return None
    def version(self):
        """int QDataStream.version(None self)"""
        return int()
    def setByteOrder(self):
        """QDataStream.ByteOrder QDataStream.setByteOrder(None self)"""
        return QDataStream.ByteOrder()
    def byteOrder(self):
        """QDataStream.ByteOrder QDataStream.byteOrder(None self)"""
        return QDataStream.ByteOrder()
    def resetStatus(self):
        """None QDataStream.resetStatus(None self)"""
        return None
    def setStatus(self, _status):
        """None QDataStream.setStatus(None self, QDataStream.Status _status)"""
        return None
    def status(self):
        """QDataStream.Status QDataStream.status(None self)"""
        return QDataStream.Status()
    def atEnd(self):
        """bool QDataStream.atEnd(None self)"""
        return bool()
    def unsetDevice(self):
        """None QDataStream.unsetDevice(None self)"""
        return None
    def setDevice(self):
        """QIODevice QDataStream.setDevice(None self)"""
        return QIODevice()
    def device(self):
        """QIODevice QDataStream.device(None self)"""
        return QIODevice()


class QDate():
    """"""
    DateFormat = int() # QDate.MonthNameType enum
    StandaloneFormat = int() # QDate.MonthNameType enum

    def __init__(self):
        """None QDate.__init__(None self)"""
        return None
    def __init__(self, _y, _m, _d):
        """None QDate.__init__(None self, int _y, int _m, int _d)"""
        return None
    def __init__(self):
        """QDate QDate.__init__(None self)"""
        return QDate()
    def getDate(self, _year, _month, _day):
        """None QDate.getDate(None self, int _year, int _month, int _day)"""
        return None
    def setDate(self, _year, _month, _date):
        """bool QDate.setDate(None self, int _year, int _month, int _date)"""
        return bool()
    def toJulianDay(self):
        """int QDate.toJulianDay(None self)"""
        return int()
    def fromJulianDay(self, _jd):
        """QDate QDate.fromJulianDay(None self, int _jd)"""
        return QDate()
    def julianToGregorian(self, _jd, _y, _m, _d):
        """None QDate.julianToGregorian(None self, int _jd, int _y, int _m, int _d)"""
        return None
    def gregorianToJulian(self, _y, _m, _d):
        """int QDate.gregorianToJulian(None self, int _y, int _m, int _d)"""
        return int()
    def isLeapYear(self, _year):
        """bool QDate.isLeapYear(None self, int _year)"""
        return bool()
    def fromString(self, _string, _format):
        """QDate QDate.fromString(None self, QString _string, Qt.DateFormat _format)"""
        return QDate()
    def fromString(self, _s, _format):
        """QDate QDate.fromString(None self, QString _s, QString _format)"""
        return QDate()
    def currentDate(self):
        """QDate QDate.currentDate(None self)"""
        return QDate()
    def __ge__(self, _other):
        """bool QDate.__ge__(None self, QDate _other)"""
        return bool()
    def __gt__(self, _other):
        """bool QDate.__gt__(None self, QDate _other)"""
        return bool()
    def __le__(self, _other):
        """bool QDate.__le__(None self, QDate _other)"""
        return bool()
    def __lt__(self, _other):
        """bool QDate.__lt__(None self, QDate _other)"""
        return bool()
    def __ne__(self, _other):
        """bool QDate.__ne__(None self, QDate _other)"""
        return bool()
    def __eq__(self, _other):
        """bool QDate.__eq__(None self, QDate _other)"""
        return bool()
    def daysTo(self):
        """QDate QDate.daysTo(None self)"""
        return QDate()
    def addYears(self, _years):
        """QDate QDate.addYears(None self, int _years)"""
        return QDate()
    def addMonths(self, _months):
        """QDate QDate.addMonths(None self, int _months)"""
        return QDate()
    def addDays(self, _days):
        """QDate QDate.addDays(None self, int _days)"""
        return QDate()
    def setYMD(self, _y, _m, _d):
        """bool QDate.setYMD(None self, int _y, int _m, int _d)"""
        return bool()
    def toString(self, _format):
        """QString QDate.toString(None self, Qt.DateFormat _format)"""
        return QString()
    def toString(self, _format):
        """QString QDate.toString(None self, QString _format)"""
        return QString()
    def longDayName(self, _weekday):
        """QString QDate.longDayName(None self, int _weekday)"""
        return QString()
    def longDayName(self, _weekday, _type):
        """QString QDate.longDayName(None self, int _weekday, QDate.MonthNameType _type)"""
        return QString()
    def longMonthName(self, _month):
        """QString QDate.longMonthName(None self, int _month)"""
        return QString()
    def longMonthName(self, _month, _type):
        """QString QDate.longMonthName(None self, int _month, QDate.MonthNameType _type)"""
        return QString()
    def shortDayName(self, _weekday):
        """QString QDate.shortDayName(None self, int _weekday)"""
        return QString()
    def shortDayName(self, _weekday, _type):
        """QString QDate.shortDayName(None self, int _weekday, QDate.MonthNameType _type)"""
        return QString()
    def shortMonthName(self, _month):
        """QString QDate.shortMonthName(None self, int _month)"""
        return QString()
    def shortMonthName(self, _month, _type):
        """QString QDate.shortMonthName(None self, int _month, QDate.MonthNameType _type)"""
        return QString()
    def weekNumber(self, _yearNumber):
        """int QDate.weekNumber(None self, int _yearNumber)"""
        return int()
    def daysInYear(self):
        """int QDate.daysInYear(None self)"""
        return int()
    def daysInMonth(self):
        """int QDate.daysInMonth(None self)"""
        return int()
    def dayOfYear(self):
        """int QDate.dayOfYear(None self)"""
        return int()
    def dayOfWeek(self):
        """int QDate.dayOfWeek(None self)"""
        return int()
    def day(self):
        """int QDate.day(None self)"""
        return int()
    def month(self):
        """int QDate.month(None self)"""
        return int()
    def year(self):
        """int QDate.year(None self)"""
        return int()
    def isValid(self):
        """bool QDate.isValid(None self)"""
        return bool()
    def isValid(self, _y, _m, _d):
        """bool QDate.isValid(None self, int _y, int _m, int _d)"""
        return bool()
    def __bool__(self):
        """int QDate.__bool__(None self)"""
        return int()
    def isNull(self):
        """bool QDate.isNull(None self)"""
        return bool()
    def toPyDate(self):
        """datetime.date QDate.toPyDate(None self)"""
        return datetime.date()
    def __hash__(self):
        """int QDate.__hash__(None self)"""
        return int()
    def __repr__(self):
        """str QDate.__repr__(None self)"""
        return str()


class QTime():
    """"""
    def __init__(self):
        """None QTime.__init__(None self)"""
        return None
    def __init__(self, _h, _m, _second, _msec):
        """None QTime.__init__(None self, int _h, int _m, int _second, int _msec)"""
        return None
    def __init__(self):
        """QTime QTime.__init__(None self)"""
        return QTime()
    def elapsed(self):
        """int QTime.elapsed(None self)"""
        return int()
    def restart(self):
        """int QTime.restart(None self)"""
        return int()
    def start(self):
        """None QTime.start(None self)"""
        return None
    def fromString(self, _string, _format):
        """QTime QTime.fromString(None self, QString _string, Qt.DateFormat _format)"""
        return QTime()
    def fromString(self, _s, _format):
        """QTime QTime.fromString(None self, QString _s, QString _format)"""
        return QTime()
    def currentTime(self):
        """QTime QTime.currentTime(None self)"""
        return QTime()
    def __ge__(self, _other):
        """bool QTime.__ge__(None self, QTime _other)"""
        return bool()
    def __gt__(self, _other):
        """bool QTime.__gt__(None self, QTime _other)"""
        return bool()
    def __le__(self, _other):
        """bool QTime.__le__(None self, QTime _other)"""
        return bool()
    def __lt__(self, _other):
        """bool QTime.__lt__(None self, QTime _other)"""
        return bool()
    def __ne__(self, _other):
        """bool QTime.__ne__(None self, QTime _other)"""
        return bool()
    def __eq__(self, _other):
        """bool QTime.__eq__(None self, QTime _other)"""
        return bool()
    def msecsTo(self):
        """QTime QTime.msecsTo(None self)"""
        return QTime()
    def addMSecs(self, _ms):
        """QTime QTime.addMSecs(None self, int _ms)"""
        return QTime()
    def secsTo(self):
        """QTime QTime.secsTo(None self)"""
        return QTime()
    def addSecs(self, _secs):
        """QTime QTime.addSecs(None self, int _secs)"""
        return QTime()
    def setHMS(self, _h, _m, _s, _msec):
        """bool QTime.setHMS(None self, int _h, int _m, int _s, int _msec)"""
        return bool()
    def toString(self, _format):
        """QString QTime.toString(None self, Qt.DateFormat _format)"""
        return QString()
    def toString(self, _format):
        """QString QTime.toString(None self, QString _format)"""
        return QString()
    def msec(self):
        """int QTime.msec(None self)"""
        return int()
    def second(self):
        """int QTime.second(None self)"""
        return int()
    def minute(self):
        """int QTime.minute(None self)"""
        return int()
    def hour(self):
        """int QTime.hour(None self)"""
        return int()
    def isValid(self):
        """bool QTime.isValid(None self)"""
        return bool()
    def isValid(self, _h, _m, _s, _msec):
        """bool QTime.isValid(None self, int _h, int _m, int _s, int _msec)"""
        return bool()
    def __bool__(self):
        """int QTime.__bool__(None self)"""
        return int()
    def isNull(self):
        """bool QTime.isNull(None self)"""
        return bool()
    def toPyTime(self):
        """datetime.time QTime.toPyTime(None self)"""
        return datetime.time()
    def __hash__(self):
        """int QTime.__hash__(None self)"""
        return int()
    def __repr__(self):
        """str QTime.__repr__(None self)"""
        return str()


class QDateTime():
    """"""
    def __init__(self):
        """None QDateTime.__init__(None self)"""
        return None
    def __init__(self, _other):
        """None QDateTime.__init__(None self, QDateTime _other)"""
        return None
    def __init__(self):
        """QDate QDateTime.__init__(None self)"""
        return QDate()
    def __init__(self, _date, _time, _timeSpec):
        """None QDateTime.__init__(None self, QDate _date, QTime _time, Qt.TimeSpec _timeSpec)"""
        return None
    def __init__(self, _y, _m, _d, _h, _m_, _s, _msec, _timeSpec):
        """None QDateTime.__init__(None self, int _y, int _m, int _d, int _h, int _m_, int _s, int _msec, int _timeSpec)"""
        return None
    def currentMSecsSinceEpoch(self):
        """int QDateTime.currentMSecsSinceEpoch(None self)"""
        return int()
    def fromMSecsSinceEpoch(self, _msecs):
        """QDateTime QDateTime.fromMSecsSinceEpoch(None self, int _msecs)"""
        return QDateTime()
    def currentDateTimeUtc(self):
        """QDateTime QDateTime.currentDateTimeUtc(None self)"""
        return QDateTime()
    def msecsTo(self):
        """QDateTime QDateTime.msecsTo(None self)"""
        return QDateTime()
    def setMSecsSinceEpoch(self, _msecs):
        """None QDateTime.setMSecsSinceEpoch(None self, int _msecs)"""
        return None
    def toMSecsSinceEpoch(self):
        """int QDateTime.toMSecsSinceEpoch(None self)"""
        return int()
    def fromTime_t(self, _secsSince1Jan1970UTC):
        """QDateTime QDateTime.fromTime_t(None self, int _secsSince1Jan1970UTC)"""
        return QDateTime()
    def fromString(self, _string, _format):
        """QDateTime QDateTime.fromString(None self, QString _string, Qt.DateFormat _format)"""
        return QDateTime()
    def fromString(self, _s, _format):
        """QDateTime QDateTime.fromString(None self, QString _s, QString _format)"""
        return QDateTime()
    def currentDateTime(self):
        """QDateTime QDateTime.currentDateTime(None self)"""
        return QDateTime()
    def __ge__(self, _other):
        """bool QDateTime.__ge__(None self, QDateTime _other)"""
        return bool()
    def __gt__(self, _other):
        """bool QDateTime.__gt__(None self, QDateTime _other)"""
        return bool()
    def __le__(self, _other):
        """bool QDateTime.__le__(None self, QDateTime _other)"""
        return bool()
    def __lt__(self, _other):
        """bool QDateTime.__lt__(None self, QDateTime _other)"""
        return bool()
    def __ne__(self, _other):
        """bool QDateTime.__ne__(None self, QDateTime _other)"""
        return bool()
    def __eq__(self, _other):
        """bool QDateTime.__eq__(None self, QDateTime _other)"""
        return bool()
    def secsTo(self):
        """QDateTime QDateTime.secsTo(None self)"""
        return QDateTime()
    def daysTo(self):
        """QDateTime QDateTime.daysTo(None self)"""
        return QDateTime()
    def toUTC(self):
        """QDateTime QDateTime.toUTC(None self)"""
        return QDateTime()
    def toLocalTime(self):
        """QDateTime QDateTime.toLocalTime(None self)"""
        return QDateTime()
    def toTimeSpec(self, _spec):
        """QDateTime QDateTime.toTimeSpec(None self, Qt.TimeSpec _spec)"""
        return QDateTime()
    def addMSecs(self, _msecs):
        """QDateTime QDateTime.addMSecs(None self, int _msecs)"""
        return QDateTime()
    def addSecs(self, _secs):
        """QDateTime QDateTime.addSecs(None self, int _secs)"""
        return QDateTime()
    def addYears(self, _years):
        """QDateTime QDateTime.addYears(None self, int _years)"""
        return QDateTime()
    def addMonths(self, _months):
        """QDateTime QDateTime.addMonths(None self, int _months)"""
        return QDateTime()
    def addDays(self, _days):
        """QDateTime QDateTime.addDays(None self, int _days)"""
        return QDateTime()
    def toString(self, _format):
        """QString QDateTime.toString(None self, Qt.DateFormat _format)"""
        return QString()
    def toString(self, _format):
        """QString QDateTime.toString(None self, QString _format)"""
        return QString()
    def setTime_t(self, _secsSince1Jan1970UTC):
        """None QDateTime.setTime_t(None self, int _secsSince1Jan1970UTC)"""
        return None
    def setTimeSpec(self, _spec):
        """None QDateTime.setTimeSpec(None self, Qt.TimeSpec _spec)"""
        return None
    def setTime(self, _time):
        """None QDateTime.setTime(None self, QTime _time)"""
        return None
    def setDate(self, _date):
        """None QDateTime.setDate(None self, QDate _date)"""
        return None
    def toTime_t(self):
        """int QDateTime.toTime_t(None self)"""
        return int()
    def timeSpec(self):
        """Qt.TimeSpec QDateTime.timeSpec(None self)"""
        return Qt.TimeSpec()
    def time(self):
        """QTime QDateTime.time(None self)"""
        return QTime()
    def date(self):
        """QDate QDateTime.date(None self)"""
        return QDate()
    def isValid(self):
        """bool QDateTime.isValid(None self)"""
        return bool()
    def __bool__(self):
        """int QDateTime.__bool__(None self)"""
        return int()
    def isNull(self):
        """bool QDateTime.isNull(None self)"""
        return bool()
    def toPyDateTime(self):
        """datetime.datetime QDateTime.toPyDateTime(None self)"""
        return datetime.datetime()
    def __hash__(self):
        """int QDateTime.__hash__(None self)"""
        return int()
    def __repr__(self):
        """str QDateTime.__repr__(None self)"""
        return str()


class QDir():
    """"""
    Name = int() # QDir.SortFlag enum
    Time = int() # QDir.SortFlag enum
    Size = int() # QDir.SortFlag enum
    Unsorted = int() # QDir.SortFlag enum
    SortByMask = int() # QDir.SortFlag enum
    DirsFirst = int() # QDir.SortFlag enum
    Reversed = int() # QDir.SortFlag enum
    IgnoreCase = int() # QDir.SortFlag enum
    DirsLast = int() # QDir.SortFlag enum
    LocaleAware = int() # QDir.SortFlag enum
    Type = int() # QDir.SortFlag enum
    NoSort = int() # QDir.SortFlag enum

    Dirs = int() # QDir.Filter enum
    Files = int() # QDir.Filter enum
    Drives = int() # QDir.Filter enum
    NoSymLinks = int() # QDir.Filter enum
    AllEntries = int() # QDir.Filter enum
    TypeMask = int() # QDir.Filter enum
    Readable = int() # QDir.Filter enum
    Writable = int() # QDir.Filter enum
    Executable = int() # QDir.Filter enum
    PermissionMask = int() # QDir.Filter enum
    Modified = int() # QDir.Filter enum
    Hidden = int() # QDir.Filter enum
    System = int() # QDir.Filter enum
    AccessMask = int() # QDir.Filter enum
    AllDirs = int() # QDir.Filter enum
    CaseSensitive = int() # QDir.Filter enum
    NoDotAndDotDot = int() # QDir.Filter enum
    NoFilter = int() # QDir.Filter enum
    NoDot = int() # QDir.Filter enum
    NoDotDot = int() # QDir.Filter enum

    def __init__(self):
        """QDir QDir.__init__(None self)"""
        return QDir()
    def __init__(self, _path):
        """None QDir.__init__(None self, QString _path)"""
        return None
    def __init__(self, _path, _nameFilter, _sort, _filters):
        """None QDir.__init__(None self, QString _path, QString _nameFilter, QDir.SortFlags _sort, QDir.Filters _filters)"""
        return None
    def searchPaths(self, _prefix):
        """QStringList QDir.searchPaths(None self, QString _prefix)"""
        return QStringList()
    def addSearchPath(self, _prefix, _path):
        """None QDir.addSearchPath(None self, QString _prefix, QString _path)"""
        return None
    def setSearchPaths(self, _prefix, _searchPaths):
        """None QDir.setSearchPaths(None self, QString _prefix, QStringList _searchPaths)"""
        return None
    def fromNativeSeparators(self, _pathName):
        """QString QDir.fromNativeSeparators(None self, QString _pathName)"""
        return QString()
    def toNativeSeparators(self, _pathName):
        """QString QDir.toNativeSeparators(None self, QString _pathName)"""
        return QString()
    def cleanPath(self, _path):
        """QString QDir.cleanPath(None self, QString _path)"""
        return QString()
    def match(self, _filters, _fileName):
        """bool QDir.match(None self, QStringList _filters, QString _fileName)"""
        return bool()
    def match(self, _filter, _fileName):
        """bool QDir.match(None self, QString _filter, QString _fileName)"""
        return bool()
    def tempPath(self):
        """QString QDir.tempPath(None self)"""
        return QString()
    def temp(self):
        """QDir QDir.temp(None self)"""
        return QDir()
    def rootPath(self):
        """QString QDir.rootPath(None self)"""
        return QString()
    def root(self):
        """QDir QDir.root(None self)"""
        return QDir()
    def homePath(self):
        """QString QDir.homePath(None self)"""
        return QString()
    def home(self):
        """QDir QDir.home(None self)"""
        return QDir()
    def currentPath(self):
        """QString QDir.currentPath(None self)"""
        return QString()
    def current(self):
        """QDir QDir.current(None self)"""
        return QDir()
    def setCurrent(self, _path):
        """bool QDir.setCurrent(None self, QString _path)"""
        return bool()
    def separator(self):
        """QChar QDir.separator(None self)"""
        return QChar()
    def drives(self):
        """list-of-QFileInfo QDir.drives(None self)"""
        return [QFileInfo()]
    def refresh(self):
        """None QDir.refresh(None self)"""
        return None
    def rename(self, _oldName, _newName):
        """bool QDir.rename(None self, QString _oldName, QString _newName)"""
        return bool()
    def remove(self, _fileName):
        """bool QDir.remove(None self, QString _fileName)"""
        return bool()
    def __ne__(self, _dir):
        """bool QDir.__ne__(None self, QDir _dir)"""
        return bool()
    def __eq__(self, _dir):
        """bool QDir.__eq__(None self, QDir _dir)"""
        return bool()
    def makeAbsolute(self):
        """bool QDir.makeAbsolute(None self)"""
        return bool()
    def isAbsolute(self):
        """bool QDir.isAbsolute(None self)"""
        return bool()
    def isRelative(self):
        """bool QDir.isRelative(None self)"""
        return bool()
    def isAbsolutePath(self, _path):
        """bool QDir.isAbsolutePath(None self, QString _path)"""
        return bool()
    def isRelativePath(self, _path):
        """bool QDir.isRelativePath(None self, QString _path)"""
        return bool()
    def isRoot(self):
        """bool QDir.isRoot(None self)"""
        return bool()
    def exists(self):
        """bool QDir.exists(None self)"""
        return bool()
    def exists(self, _name):
        """bool QDir.exists(None self, QString _name)"""
        return bool()
    def isReadable(self):
        """bool QDir.isReadable(None self)"""
        return bool()
    def rmpath(self, _dirPath):
        """bool QDir.rmpath(None self, QString _dirPath)"""
        return bool()
    def mkpath(self, _dirPath):
        """bool QDir.mkpath(None self, QString _dirPath)"""
        return bool()
    def rmdir(self, _dirName):
        """bool QDir.rmdir(None self, QString _dirName)"""
        return bool()
    def mkdir(self, _dirName):
        """bool QDir.mkdir(None self, QString _dirName)"""
        return bool()
    def entryInfoList(self, _filters, _sort):
        """list-of-QFileInfo QDir.entryInfoList(None self, QDir.Filters _filters, QDir.SortFlags _sort)"""
        return [QFileInfo()]
    def entryInfoList(self, _nameFilters, _filters, _sort):
        """list-of-QFileInfo QDir.entryInfoList(None self, QStringList _nameFilters, QDir.Filters _filters, QDir.SortFlags _sort)"""
        return [QFileInfo()]
    def entryList(self, _filters, _sort):
        """QStringList QDir.entryList(None self, QDir.Filters _filters, QDir.SortFlags _sort)"""
        return QStringList()
    def entryList(self, _nameFilters, _filters, _sort):
        """QStringList QDir.entryList(None self, QStringList _nameFilters, QDir.Filters _filters, QDir.SortFlags _sort)"""
        return QStringList()
    def nameFiltersFromString(self, _nameFilter):
        """QStringList QDir.nameFiltersFromString(None self, QString _nameFilter)"""
        return QStringList()
    def __contains__(self):
        """QString QDir.__contains__(None self)"""
        return QString()
    def __getitem__(self):
        """int QDir.__getitem__(None self)"""
        return int()
    def __getitem__(self):
        """slice QDir.__getitem__(None self)"""
        return slice()
    def __len__(self):
        """ QDir.__len__(None self)"""
        return ()
    def count(self):
        """int QDir.count(None self)"""
        return int()
    def setSorting(self, _sort):
        """None QDir.setSorting(None self, QDir.SortFlags _sort)"""
        return None
    def sorting(self):
        """QDir.SortFlags QDir.sorting(None self)"""
        return QDir.SortFlags()
    def setFilter(self, _filter):
        """None QDir.setFilter(None self, QDir.Filters _filter)"""
        return None
    def filter(self):
        """QDir.Filters QDir.filter(None self)"""
        return QDir.Filters()
    def setNameFilters(self, _nameFilters):
        """None QDir.setNameFilters(None self, QStringList _nameFilters)"""
        return None
    def nameFilters(self):
        """QStringList QDir.nameFilters(None self)"""
        return QStringList()
    def cdUp(self):
        """bool QDir.cdUp(None self)"""
        return bool()
    def cd(self, _dirName):
        """bool QDir.cd(None self, QString _dirName)"""
        return bool()
    def convertSeparators(self, _pathName):
        """QString QDir.convertSeparators(None self, QString _pathName)"""
        return QString()
    def relativeFilePath(self, _fileName):
        """QString QDir.relativeFilePath(None self, QString _fileName)"""
        return QString()
    def absoluteFilePath(self, _fileName):
        """QString QDir.absoluteFilePath(None self, QString _fileName)"""
        return QString()
    def filePath(self, _fileName):
        """QString QDir.filePath(None self, QString _fileName)"""
        return QString()
    def dirName(self):
        """QString QDir.dirName(None self)"""
        return QString()
    def addResourceSearchPath(self, _path):
        """None QDir.addResourceSearchPath(None self, QString _path)"""
        return None
    def canonicalPath(self):
        """QString QDir.canonicalPath(None self)"""
        return QString()
    def absolutePath(self):
        """QString QDir.absolutePath(None self)"""
        return QString()
    def path(self):
        """QString QDir.path(None self)"""
        return QString()
    def setPath(self, _path):
        """None QDir.setPath(None self, QString _path)"""
        return None


class QDirIterator():
    """"""
    NoIteratorFlags = int() # QDirIterator.IteratorFlag enum
    FollowSymlinks = int() # QDirIterator.IteratorFlag enum
    Subdirectories = int() # QDirIterator.IteratorFlag enum

    def __init__(self, _dir, _flags):
        """None QDirIterator.__init__(None self, QDir _dir, QDirIterator.IteratorFlags _flags)"""
        return None
    def __init__(self, _path, _flags):
        """None QDirIterator.__init__(None self, QString _path, QDirIterator.IteratorFlags _flags)"""
        return None
    def __init__(self, _path, _filters, _flags):
        """None QDirIterator.__init__(None self, QString _path, QDir.Filters _filters, QDirIterator.IteratorFlags _flags)"""
        return None
    def __init__(self, _path, _nameFilters, _filters, _flags):
        """None QDirIterator.__init__(None self, QString _path, QStringList _nameFilters, QDir.Filters _filters, QDirIterator.IteratorFlags _flags)"""
        return None
    def path(self):
        """QString QDirIterator.path(None self)"""
        return QString()
    def fileInfo(self):
        """QFileInfo QDirIterator.fileInfo(None self)"""
        return QFileInfo()
    def filePath(self):
        """QString QDirIterator.filePath(None self)"""
        return QString()
    def fileName(self):
        """QString QDirIterator.fileName(None self)"""
        return QString()
    def hasNext(self):
        """bool QDirIterator.hasNext(None self)"""
        return bool()
    def next(self):
        """QString QDirIterator.next(None self)"""
        return QString()


class QEasingCurve():
    """"""
    Linear = int() # QEasingCurve.Type enum
    InQuad = int() # QEasingCurve.Type enum
    OutQuad = int() # QEasingCurve.Type enum
    InOutQuad = int() # QEasingCurve.Type enum
    OutInQuad = int() # QEasingCurve.Type enum
    InCubic = int() # QEasingCurve.Type enum
    OutCubic = int() # QEasingCurve.Type enum
    InOutCubic = int() # QEasingCurve.Type enum
    OutInCubic = int() # QEasingCurve.Type enum
    InQuart = int() # QEasingCurve.Type enum
    OutQuart = int() # QEasingCurve.Type enum
    InOutQuart = int() # QEasingCurve.Type enum
    OutInQuart = int() # QEasingCurve.Type enum
    InQuint = int() # QEasingCurve.Type enum
    OutQuint = int() # QEasingCurve.Type enum
    InOutQuint = int() # QEasingCurve.Type enum
    OutInQuint = int() # QEasingCurve.Type enum
    InSine = int() # QEasingCurve.Type enum
    OutSine = int() # QEasingCurve.Type enum
    InOutSine = int() # QEasingCurve.Type enum
    OutInSine = int() # QEasingCurve.Type enum
    InExpo = int() # QEasingCurve.Type enum
    OutExpo = int() # QEasingCurve.Type enum
    InOutExpo = int() # QEasingCurve.Type enum
    OutInExpo = int() # QEasingCurve.Type enum
    InCirc = int() # QEasingCurve.Type enum
    OutCirc = int() # QEasingCurve.Type enum
    InOutCirc = int() # QEasingCurve.Type enum
    OutInCirc = int() # QEasingCurve.Type enum
    InElastic = int() # QEasingCurve.Type enum
    OutElastic = int() # QEasingCurve.Type enum
    InOutElastic = int() # QEasingCurve.Type enum
    OutInElastic = int() # QEasingCurve.Type enum
    InBack = int() # QEasingCurve.Type enum
    OutBack = int() # QEasingCurve.Type enum
    InOutBack = int() # QEasingCurve.Type enum
    OutInBack = int() # QEasingCurve.Type enum
    InBounce = int() # QEasingCurve.Type enum
    OutBounce = int() # QEasingCurve.Type enum
    InOutBounce = int() # QEasingCurve.Type enum
    OutInBounce = int() # QEasingCurve.Type enum
    InCurve = int() # QEasingCurve.Type enum
    OutCurve = int() # QEasingCurve.Type enum
    SineCurve = int() # QEasingCurve.Type enum
    CosineCurve = int() # QEasingCurve.Type enum
    Custom = int() # QEasingCurve.Type enum

    def __init__(self, _type):
        """None QEasingCurve.__init__(None self, QEasingCurve.Type _type)"""
        return None
    def __init__(self, _other):
        """None QEasingCurve.__init__(None self, QEasingCurve _other)"""
        return None
    def valueForProgress(self, _progress):
        """float QEasingCurve.valueForProgress(None self, float _progress)"""
        return float()
    def customType(self):
        """callable QEasingCurve.customType(None self)"""
        return callable()
    def setCustomType(self, _func):
        """None QEasingCurve.setCustomType(None self, callable _func)"""
        return None
    def setType(self, _type):
        """None QEasingCurve.setType(None self, QEasingCurve.Type _type)"""
        return None
    def type(self):
        """QEasingCurve.Type QEasingCurve.type(None self)"""
        return QEasingCurve.Type()
    def setOvershoot(self, _overshoot):
        """None QEasingCurve.setOvershoot(None self, float _overshoot)"""
        return None
    def overshoot(self):
        """float QEasingCurve.overshoot(None self)"""
        return float()
    def setPeriod(self, _period):
        """None QEasingCurve.setPeriod(None self, float _period)"""
        return None
    def period(self):
        """float QEasingCurve.period(None self)"""
        return float()
    def setAmplitude(self, _amplitude):
        """None QEasingCurve.setAmplitude(None self, float _amplitude)"""
        return None
    def amplitude(self):
        """float QEasingCurve.amplitude(None self)"""
        return float()
    def __ne__(self, _other):
        """bool QEasingCurve.__ne__(None self, QEasingCurve _other)"""
        return bool()
    def __eq__(self, _other):
        """bool QEasingCurve.__eq__(None self, QEasingCurve _other)"""
        return bool()


class QElapsedTimer():
    """"""
    SystemTime = int() # QElapsedTimer.ClockType enum
    MonotonicClock = int() # QElapsedTimer.ClockType enum
    TickCounter = int() # QElapsedTimer.ClockType enum
    MachAbsoluteTime = int() # QElapsedTimer.ClockType enum

    def __init__(self):
        """None QElapsedTimer.__init__(None self)"""
        return None
    def __init__(self):
        """QElapsedTimer QElapsedTimer.__init__(None self)"""
        return QElapsedTimer()
    def __ge__(self, _v2):
        """bool QElapsedTimer.__ge__(None self, QElapsedTimer _v2)"""
        return bool()
    def __lt__(self, _v2):
        """bool QElapsedTimer.__lt__(None self, QElapsedTimer _v2)"""
        return bool()
    def __ne__(self, _other):
        """bool QElapsedTimer.__ne__(None self, QElapsedTimer _other)"""
        return bool()
    def __eq__(self, _other):
        """bool QElapsedTimer.__eq__(None self, QElapsedTimer _other)"""
        return bool()
    def secsTo(self, _other):
        """int QElapsedTimer.secsTo(None self, QElapsedTimer _other)"""
        return int()
    def msecsTo(self, _other):
        """int QElapsedTimer.msecsTo(None self, QElapsedTimer _other)"""
        return int()
    def msecsSinceReference(self):
        """int QElapsedTimer.msecsSinceReference(None self)"""
        return int()
    def hasExpired(self, _timeout):
        """bool QElapsedTimer.hasExpired(None self, int _timeout)"""
        return bool()
    def elapsed(self):
        """int QElapsedTimer.elapsed(None self)"""
        return int()
    def isValid(self):
        """bool QElapsedTimer.isValid(None self)"""
        return bool()
    def invalidate(self):
        """None QElapsedTimer.invalidate(None self)"""
        return None
    def restart(self):
        """int QElapsedTimer.restart(None self)"""
        return int()
    def start(self):
        """None QElapsedTimer.start(None self)"""
        return None
    def isMonotonic(self):
        """bool QElapsedTimer.isMonotonic(None self)"""
        return bool()
    def clockType(self):
        """QElapsedTimer.ClockType QElapsedTimer.clockType(None self)"""
        return QElapsedTimer.ClockType()


class QEventLoop(QObject):
    """"""
    AllEvents = int() # QEventLoop.ProcessEventsFlag enum
    ExcludeUserInputEvents = int() # QEventLoop.ProcessEventsFlag enum
    ExcludeSocketNotifiers = int() # QEventLoop.ProcessEventsFlag enum
    WaitForMoreEvents = int() # QEventLoop.ProcessEventsFlag enum
    X11ExcludeTimers = int() # QEventLoop.ProcessEventsFlag enum
    DeferredDeletion = int() # QEventLoop.ProcessEventsFlag enum

    def __init__(self, _parent):
        """None QEventLoop.__init__(None self, QObject _parent)"""
        return None
    def quit(self):
        """None QEventLoop.quit(None self)"""
        return None
    def wakeUp(self):
        """None QEventLoop.wakeUp(None self)"""
        return None
    def isRunning(self):
        """bool QEventLoop.isRunning(None self)"""
        return bool()
    def exit(self, _returnCode):
        """None QEventLoop.exit(None self, int _returnCode)"""
        return None
    def exec_(self, _flags):
        """int QEventLoop.exec_(None self, QEventLoop.ProcessEventsFlags _flags)"""
        return int()
    def processEvents(self, _flags):
        """bool QEventLoop.processEvents(None self, QEventLoop.ProcessEventsFlags _flags)"""
        return bool()
    def processEvents(self, _flags, _maximumTime):
        """None QEventLoop.processEvents(None self, QEventLoop.ProcessEventsFlags _flags, int _maximumTime)"""
        return None


class QEventTransition(QAbstractTransition):
    """"""
    def __init__(self, _sourceState):
        """None QEventTransition.__init__(None self, QState _sourceState)"""
        return None
    def __init__(self, _object, _type, _sourceState):
        """None QEventTransition.__init__(None self, QObject _object, QEvent.Type _type, QState _sourceState)"""
        return None
    def event(self, _e):
        """bool QEventTransition.event(None self, QEvent _e)"""
        return bool()
    def onTransition(self, _event):
        """None QEventTransition.onTransition(None self, QEvent _event)"""
        return None
    def eventTest(self, _event):
        """bool QEventTransition.eventTest(None self, QEvent _event)"""
        return bool()
    def setEventType(self, _type):
        """None QEventTransition.setEventType(None self, QEvent.Type _type)"""
        return None
    def eventType(self):
        """QEvent.Type QEventTransition.eventType(None self)"""
        return QEvent.Type()
    def setEventSource(self, _object):
        """None QEventTransition.setEventSource(None self, QObject _object)"""
        return None
    def eventSource(self):
        """QObject QEventTransition.eventSource(None self)"""
        return QObject()


class QFile(QIODevice):
    """"""
    ReadOwner = int() # QFile.Permission enum
    WriteOwner = int() # QFile.Permission enum
    ExeOwner = int() # QFile.Permission enum
    ReadUser = int() # QFile.Permission enum
    WriteUser = int() # QFile.Permission enum
    ExeUser = int() # QFile.Permission enum
    ReadGroup = int() # QFile.Permission enum
    WriteGroup = int() # QFile.Permission enum
    ExeGroup = int() # QFile.Permission enum
    ReadOther = int() # QFile.Permission enum
    WriteOther = int() # QFile.Permission enum
    ExeOther = int() # QFile.Permission enum

    NoOptions = int() # QFile.MemoryMapFlags enum

    NoError = int() # QFile.FileError enum
    ReadError = int() # QFile.FileError enum
    WriteError = int() # QFile.FileError enum
    FatalError = int() # QFile.FileError enum
    ResourceError = int() # QFile.FileError enum
    OpenError = int() # QFile.FileError enum
    AbortError = int() # QFile.FileError enum
    TimeOutError = int() # QFile.FileError enum
    UnspecifiedError = int() # QFile.FileError enum
    RemoveError = int() # QFile.FileError enum
    RenameError = int() # QFile.FileError enum
    PositionError = int() # QFile.FileError enum
    ResizeError = int() # QFile.FileError enum
    PermissionsError = int() # QFile.FileError enum
    CopyError = int() # QFile.FileError enum

    def __init__(self):
        """None QFile.__init__(None self)"""
        return None
    def __init__(self, _name):
        """None QFile.__init__(None self, QString _name)"""
        return None
    def __init__(self, _parent):
        """None QFile.__init__(None self, QObject _parent)"""
        return None
    def __init__(self, _name, _parent):
        """None QFile.__init__(None self, QString _name, QObject _parent)"""
        return None
    def writeData(self, _data):
        """int QFile.writeData(None self, str _data)"""
        return int()
    def readLineData(self, _maxlen):
        """str QFile.readLineData(None self, int _maxlen)"""
        return str()
    def readData(self, _maxlen):
        """str QFile.readData(None self, int _maxlen)"""
        return str()
    def unmap(self, _address):
        """bool QFile.unmap(None self, sip.voidptr _address)"""
        return bool()
    def map(self, _offset, _size, _flags):
        """sip.voidptr QFile.map(None self, int _offset, int _size, QFile.MemoryMapFlags _flags)"""
        return sip.voidptr()
    def symLinkTarget(self):
        """QString QFile.symLinkTarget(None self)"""
        return QString()
    def symLinkTarget(self, _fileName):
        """QString QFile.symLinkTarget(None self, QString _fileName)"""
        return QString()
    def fileEngine(self):
        """QAbstractFileEngine QFile.fileEngine(None self)"""
        return QAbstractFileEngine()
    def handle(self):
        """int QFile.handle(None self)"""
        return int()
    def setPermissions(self, _permissionSpec):
        """bool QFile.setPermissions(None self, QFile.Permissions _permissionSpec)"""
        return bool()
    def setPermissions(self, _filename, _permissionSpec):
        """bool QFile.setPermissions(None self, QString _filename, QFile.Permissions _permissionSpec)"""
        return bool()
    def permissions(self):
        """QFile.Permissions QFile.permissions(None self)"""
        return QFile.Permissions()
    def permissions(self, _filename):
        """QFile.Permissions QFile.permissions(None self, QString _filename)"""
        return QFile.Permissions()
    def resize(self, _sz):
        """bool QFile.resize(None self, int _sz)"""
        return bool()
    def resize(self, _filename, _sz):
        """bool QFile.resize(None self, QString _filename, int _sz)"""
        return bool()
    def flush(self):
        """bool QFile.flush(None self)"""
        return bool()
    def atEnd(self):
        """bool QFile.atEnd(None self)"""
        return bool()
    def seek(self, _offset):
        """bool QFile.seek(None self, int _offset)"""
        return bool()
    def pos(self):
        """int QFile.pos(None self)"""
        return int()
    def size(self):
        """int QFile.size(None self)"""
        return int()
    def close(self):
        """None QFile.close(None self)"""
        return None
    def open(self, _flags):
        """bool QFile.open(None self, QIODevice.OpenMode _flags)"""
        return bool()
    def open(self, _fd, _flags):
        """bool QFile.open(None self, int _fd, QIODevice.OpenMode _flags)"""
        return bool()
    def isSequential(self):
        """bool QFile.isSequential(None self)"""
        return bool()
    def copy(self, _newName):
        """bool QFile.copy(None self, QString _newName)"""
        return bool()
    def copy(self, _fileName, _newName):
        """bool QFile.copy(None self, QString _fileName, QString _newName)"""
        return bool()
    def link(self, _newName):
        """bool QFile.link(None self, QString _newName)"""
        return bool()
    def link(self, _oldname, _newName):
        """bool QFile.link(None self, QString _oldname, QString _newName)"""
        return bool()
    def rename(self, _newName):
        """bool QFile.rename(None self, QString _newName)"""
        return bool()
    def rename(self, _oldName, _newName):
        """bool QFile.rename(None self, QString _oldName, QString _newName)"""
        return bool()
    def remove(self):
        """bool QFile.remove(None self)"""
        return bool()
    def remove(self, _fileName):
        """bool QFile.remove(None self, QString _fileName)"""
        return bool()
    def readLink(self):
        """QString QFile.readLink(None self)"""
        return QString()
    def readLink(self, _fileName):
        """QString QFile.readLink(None self, QString _fileName)"""
        return QString()
    def exists(self):
        """bool QFile.exists(None self)"""
        return bool()
    def exists(self, _fileName):
        """bool QFile.exists(None self, QString _fileName)"""
        return bool()
    def decodeName(self, _localFileName):
        """QString QFile.decodeName(None self, QByteArray _localFileName)"""
        return QString()
    def decodeName(self, _localFileName):
        """QString QFile.decodeName(None self, str _localFileName)"""
        return QString()
    def encodeName(self, _fileName):
        """QByteArray QFile.encodeName(None self, QString _fileName)"""
        return QByteArray()
    def setFileName(self, _name):
        """None QFile.setFileName(None self, QString _name)"""
        return None
    def fileName(self):
        """QString QFile.fileName(None self)"""
        return QString()
    def unsetError(self):
        """None QFile.unsetError(None self)"""
        return None
    def error(self):
        """QFile.FileError QFile.error(None self)"""
        return QFile.FileError()


class QFileInfo():
    """"""
    def __init__(self):
        """None QFileInfo.__init__(None self)"""
        return None
    def __init__(self, _file):
        """None QFileInfo.__init__(None self, QString _file)"""
        return None
    def __init__(self, _file):
        """None QFileInfo.__init__(None self, QFile _file)"""
        return None
    def __init__(self, _dir, _file):
        """None QFileInfo.__init__(None self, QDir _dir, QString _file)"""
        return None
    def __init__(self, _fileinfo):
        """None QFileInfo.__init__(None self, QFileInfo _fileinfo)"""
        return None
    def isBundle(self):
        """bool QFileInfo.isBundle(None self)"""
        return bool()
    def bundleName(self):
        """QString QFileInfo.bundleName(None self)"""
        return QString()
    def symLinkTarget(self):
        """QString QFileInfo.symLinkTarget(None self)"""
        return QString()
    def setCaching(self, _on):
        """None QFileInfo.setCaching(None self, bool _on)"""
        return None
    def caching(self):
        """bool QFileInfo.caching(None self)"""
        return bool()
    def detach(self):
        """None QFileInfo.detach(None self)"""
        return None
    def lastRead(self):
        """QDateTime QFileInfo.lastRead(None self)"""
        return QDateTime()
    def lastModified(self):
        """QDateTime QFileInfo.lastModified(None self)"""
        return QDateTime()
    def created(self):
        """QDateTime QFileInfo.created(None self)"""
        return QDateTime()
    def size(self):
        """int QFileInfo.size(None self)"""
        return int()
    def permissions(self):
        """QFile.Permissions QFileInfo.permissions(None self)"""
        return QFile.Permissions()
    def permission(self, _permissions):
        """bool QFileInfo.permission(None self, QFile.Permissions _permissions)"""
        return bool()
    def groupId(self):
        """int QFileInfo.groupId(None self)"""
        return int()
    def group(self):
        """QString QFileInfo.group(None self)"""
        return QString()
    def ownerId(self):
        """int QFileInfo.ownerId(None self)"""
        return int()
    def owner(self):
        """QString QFileInfo.owner(None self)"""
        return QString()
    def readLink(self):
        """QString QFileInfo.readLink(None self)"""
        return QString()
    def isRoot(self):
        """bool QFileInfo.isRoot(None self)"""
        return bool()
    def isSymLink(self):
        """bool QFileInfo.isSymLink(None self)"""
        return bool()
    def isDir(self):
        """bool QFileInfo.isDir(None self)"""
        return bool()
    def isFile(self):
        """bool QFileInfo.isFile(None self)"""
        return bool()
    def makeAbsolute(self):
        """bool QFileInfo.makeAbsolute(None self)"""
        return bool()
    def isAbsolute(self):
        """bool QFileInfo.isAbsolute(None self)"""
        return bool()
    def isRelative(self):
        """bool QFileInfo.isRelative(None self)"""
        return bool()
    def isHidden(self):
        """bool QFileInfo.isHidden(None self)"""
        return bool()
    def isExecutable(self):
        """bool QFileInfo.isExecutable(None self)"""
        return bool()
    def isWritable(self):
        """bool QFileInfo.isWritable(None self)"""
        return bool()
    def isReadable(self):
        """bool QFileInfo.isReadable(None self)"""
        return bool()
    def absoluteDir(self):
        """QDir QFileInfo.absoluteDir(None self)"""
        return QDir()
    def dir(self):
        """QDir QFileInfo.dir(None self)"""
        return QDir()
    def canonicalPath(self):
        """QString QFileInfo.canonicalPath(None self)"""
        return QString()
    def absolutePath(self):
        """QString QFileInfo.absolutePath(None self)"""
        return QString()
    def path(self):
        """QString QFileInfo.path(None self)"""
        return QString()
    def completeSuffix(self):
        """QString QFileInfo.completeSuffix(None self)"""
        return QString()
    def suffix(self):
        """QString QFileInfo.suffix(None self)"""
        return QString()
    def completeBaseName(self):
        """QString QFileInfo.completeBaseName(None self)"""
        return QString()
    def baseName(self):
        """QString QFileInfo.baseName(None self)"""
        return QString()
    def fileName(self):
        """QString QFileInfo.fileName(None self)"""
        return QString()
    def canonicalFilePath(self):
        """QString QFileInfo.canonicalFilePath(None self)"""
        return QString()
    def absoluteFilePath(self):
        """QString QFileInfo.absoluteFilePath(None self)"""
        return QString()
    def filePath(self):
        """QString QFileInfo.filePath(None self)"""
        return QString()
    def refresh(self):
        """None QFileInfo.refresh(None self)"""
        return None
    def exists(self):
        """bool QFileInfo.exists(None self)"""
        return bool()
    def setFile(self, _file):
        """None QFileInfo.setFile(None self, QString _file)"""
        return None
    def setFile(self, _file):
        """None QFileInfo.setFile(None self, QFile _file)"""
        return None
    def setFile(self, _dir, _file):
        """None QFileInfo.setFile(None self, QDir _dir, QString _file)"""
        return None
    def __ne__(self, _fileinfo):
        """bool QFileInfo.__ne__(None self, QFileInfo _fileinfo)"""
        return bool()
    def __eq__(self, _fileinfo):
        """bool QFileInfo.__eq__(None self, QFileInfo _fileinfo)"""
        return bool()


class QFileSystemWatcher(QObject):
    """"""
    def __init__(self, _parent):
        """None QFileSystemWatcher.__init__(None self, QObject _parent)"""
        return None
    def __init__(self, _paths, _parent):
        """None QFileSystemWatcher.__init__(None self, QStringList _paths, QObject _parent)"""
        return None
    def removePaths(self, _files):
        """None QFileSystemWatcher.removePaths(None self, QStringList _files)"""
        return None
    def removePath(self, _file):
        """None QFileSystemWatcher.removePath(None self, QString _file)"""
        return None
    def files(self):
        """QStringList QFileSystemWatcher.files(None self)"""
        return QStringList()
    def directories(self):
        """QStringList QFileSystemWatcher.directories(None self)"""
        return QStringList()
    def addPaths(self, _files):
        """None QFileSystemWatcher.addPaths(None self, QStringList _files)"""
        return None
    def addPath(self, _file):
        """None QFileSystemWatcher.addPath(None self, QString _file)"""
        return None


class QFinalState(QAbstractState):
    """"""
    def __init__(self, _parent):
        """None QFinalState.__init__(None self, QState _parent)"""
        return None
    def event(self, _e):
        """bool QFinalState.event(None self, QEvent _e)"""
        return bool()
    def onExit(self, _event):
        """None QFinalState.onExit(None self, QEvent _event)"""
        return None
    def onEntry(self, _event):
        """None QFinalState.onEntry(None self, QEvent _event)"""
        return None


class QFSFileEngine(QAbstractFileEngine):
    """"""
    def __init__(self):
        """None QFSFileEngine.__init__(None self)"""
        return None
    def __init__(self, _file):
        """None QFSFileEngine.__init__(None self, QString _file)"""
        return None
    def drives(self):
        """list-of-QFileInfo QFSFileEngine.drives(None self)"""
        return [QFileInfo()]
    def tempPath(self):
        """QString QFSFileEngine.tempPath(None self)"""
        return QString()
    def rootPath(self):
        """QString QFSFileEngine.rootPath(None self)"""
        return QString()
    def homePath(self):
        """QString QFSFileEngine.homePath(None self)"""
        return QString()
    def currentPath(self, _fileName):
        """QString QFSFileEngine.currentPath(None self, QString _fileName)"""
        return QString()
    def setCurrentPath(self, _path):
        """bool QFSFileEngine.setCurrentPath(None self, QString _path)"""
        return bool()
    def write(self, _data):
        """int QFSFileEngine.write(None self, str _data)"""
        return int()
    def readLine(self, _maxlen):
        """str QFSFileEngine.readLine(None self, int _maxlen)"""
        return str()
    def read(self, _maxlen):
        """str QFSFileEngine.read(None self, int _maxlen)"""
        return str()
    def handle(self):
        """int QFSFileEngine.handle(None self)"""
        return int()
    def setFileName(self, _file):
        """None QFSFileEngine.setFileName(None self, QString _file)"""
        return None
    def fileTime(self, _time):
        """QDateTime QFSFileEngine.fileTime(None self, QAbstractFileEngine.FileTime _time)"""
        return QDateTime()
    def owner(self):
        """QAbstractFileEngine.FileOwner QFSFileEngine.owner(None self)"""
        return QAbstractFileEngine.FileOwner()
    def ownerId(self):
        """QAbstractFileEngine.FileOwner QFSFileEngine.ownerId(None self)"""
        return QAbstractFileEngine.FileOwner()
    def fileName(self, _file):
        """QString QFSFileEngine.fileName(None self, QAbstractFileEngine.FileName _file)"""
        return QString()
    def setPermissions(self, _perms):
        """bool QFSFileEngine.setPermissions(None self, int _perms)"""
        return bool()
    def fileFlags(self, _type):
        """QAbstractFileEngine.FileFlags QFSFileEngine.fileFlags(None self, QAbstractFileEngine.FileFlags _type)"""
        return QAbstractFileEngine.FileFlags()
    def entryList(self, _filters, _filterNames):
        """QStringList QFSFileEngine.entryList(None self, QDir.Filters _filters, QStringList _filterNames)"""
        return QStringList()
    def isRelativePath(self):
        """bool QFSFileEngine.isRelativePath(None self)"""
        return bool()
    def caseSensitive(self):
        """bool QFSFileEngine.caseSensitive(None self)"""
        return bool()
    def setSize(self, _size):
        """bool QFSFileEngine.setSize(None self, int _size)"""
        return bool()
    def rmdir(self, _dirName, _recurseParentDirectories):
        """bool QFSFileEngine.rmdir(None self, QString _dirName, bool _recurseParentDirectories)"""
        return bool()
    def mkdir(self, _dirName, _createParentDirectories):
        """bool QFSFileEngine.mkdir(None self, QString _dirName, bool _createParentDirectories)"""
        return bool()
    def link(self, _newName):
        """bool QFSFileEngine.link(None self, QString _newName)"""
        return bool()
    def rename(self, _newName):
        """bool QFSFileEngine.rename(None self, QString _newName)"""
        return bool()
    def copy(self, _newName):
        """bool QFSFileEngine.copy(None self, QString _newName)"""
        return bool()
    def remove(self):
        """bool QFSFileEngine.remove(None self)"""
        return bool()
    def isSequential(self):
        """bool QFSFileEngine.isSequential(None self)"""
        return bool()
    def seek(self):
        """int QFSFileEngine.seek(None self)"""
        return int()
    def pos(self):
        """int QFSFileEngine.pos(None self)"""
        return int()
    def size(self):
        """int QFSFileEngine.size(None self)"""
        return int()
    def flush(self):
        """bool QFSFileEngine.flush(None self)"""
        return bool()
    def close(self):
        """bool QFSFileEngine.close(None self)"""
        return bool()
    def open(self, _openMode):
        """bool QFSFileEngine.open(None self, QIODevice.OpenMode _openMode)"""
        return bool()
    def open(self, _flags, _fd):
        """bool QFSFileEngine.open(None self, QIODevice.OpenMode _flags, int _fd)"""
        return bool()


class QHistoryState(QAbstractState):
    """"""
    ShallowHistory = int() # QHistoryState.HistoryType enum
    DeepHistory = int() # QHistoryState.HistoryType enum

    def __init__(self, _parent):
        """None QHistoryState.__init__(None self, QState _parent)"""
        return None
    def __init__(self, _type, _parent):
        """None QHistoryState.__init__(None self, QHistoryState.HistoryType _type, QState _parent)"""
        return None
    def event(self, _e):
        """bool QHistoryState.event(None self, QEvent _e)"""
        return bool()
    def onExit(self, _event):
        """None QHistoryState.onExit(None self, QEvent _event)"""
        return None
    def onEntry(self, _event):
        """None QHistoryState.onEntry(None self, QEvent _event)"""
        return None
    def setHistoryType(self, _type):
        """None QHistoryState.setHistoryType(None self, QHistoryState.HistoryType _type)"""
        return None
    def historyType(self):
        """QHistoryState.HistoryType QHistoryState.historyType(None self)"""
        return QHistoryState.HistoryType()
    def setDefaultState(self, _state):
        """None QHistoryState.setDefaultState(None self, QAbstractState _state)"""
        return None
    def defaultState(self):
        """QAbstractState QHistoryState.defaultState(None self)"""
        return QAbstractState()


class QLibraryInfo():
    """"""
    PrefixPath = int() # QLibraryInfo.LibraryLocation enum
    DocumentationPath = int() # QLibraryInfo.LibraryLocation enum
    HeadersPath = int() # QLibraryInfo.LibraryLocation enum
    LibrariesPath = int() # QLibraryInfo.LibraryLocation enum
    BinariesPath = int() # QLibraryInfo.LibraryLocation enum
    PluginsPath = int() # QLibraryInfo.LibraryLocation enum
    DataPath = int() # QLibraryInfo.LibraryLocation enum
    TranslationsPath = int() # QLibraryInfo.LibraryLocation enum
    SettingsPath = int() # QLibraryInfo.LibraryLocation enum
    DemosPath = int() # QLibraryInfo.LibraryLocation enum
    ExamplesPath = int() # QLibraryInfo.LibraryLocation enum
    ImportsPath = int() # QLibraryInfo.LibraryLocation enum

    def __init__(self):
        """QLibraryInfo QLibraryInfo.__init__(None self)"""
        return QLibraryInfo()
    def buildDate(self):
        """QDate QLibraryInfo.buildDate(None self)"""
        return QDate()
    def location(self):
        """QLibraryInfo.LibraryLocation QLibraryInfo.location(None self)"""
        return QLibraryInfo.LibraryLocation()
    def buildKey(self):
        """QString QLibraryInfo.buildKey(None self)"""
        return QString()
    def licensedProducts(self):
        """QString QLibraryInfo.licensedProducts(None self)"""
        return QString()
    def licensee(self):
        """QString QLibraryInfo.licensee(None self)"""
        return QString()


class QLine():
    """"""
    def __init__(self):
        """None QLine.__init__(None self)"""
        return None
    def __init__(self, _pt1_, _pt2_):
        """None QLine.__init__(None self, QPoint _pt1_, QPoint _pt2_)"""
        return None
    def __init__(self, _x1pos, _y1pos, _x2pos, _y2pos):
        """None QLine.__init__(None self, int _x1pos, int _y1pos, int _x2pos, int _y2pos)"""
        return None
    def __init__(self):
        """QLine QLine.__init__(None self)"""
        return QLine()
    def setLine(self, _aX1, _aY1, _aX2, _aY2):
        """None QLine.setLine(None self, int _aX1, int _aY1, int _aX2, int _aY2)"""
        return None
    def setPoints(self, _aP1, _aP2):
        """None QLine.setPoints(None self, QPoint _aP1, QPoint _aP2)"""
        return None
    def setP2(self, _aP2):
        """None QLine.setP2(None self, QPoint _aP2)"""
        return None
    def setP1(self, _aP1):
        """None QLine.setP1(None self, QPoint _aP1)"""
        return None
    def translated(self, _p):
        """QLine QLine.translated(None self, QPoint _p)"""
        return QLine()
    def translated(self, _adx, _ady):
        """QLine QLine.translated(None self, int _adx, int _ady)"""
        return QLine()
    def __eq__(self, _d):
        """bool QLine.__eq__(None self, QLine _d)"""
        return bool()
    def translate(self, _point):
        """None QLine.translate(None self, QPoint _point)"""
        return None
    def translate(self, _adx, _ady):
        """None QLine.translate(None self, int _adx, int _ady)"""
        return None
    def dy(self):
        """int QLine.dy(None self)"""
        return int()
    def dx(self):
        """int QLine.dx(None self)"""
        return int()
    def p2(self):
        """QPoint QLine.p2(None self)"""
        return QPoint()
    def p1(self):
        """QPoint QLine.p1(None self)"""
        return QPoint()
    def y2(self):
        """int QLine.y2(None self)"""
        return int()
    def x2(self):
        """int QLine.x2(None self)"""
        return int()
    def y1(self):
        """int QLine.y1(None self)"""
        return int()
    def x1(self):
        """int QLine.x1(None self)"""
        return int()
    def __bool__(self):
        """int QLine.__bool__(None self)"""
        return int()
    def isNull(self):
        """bool QLine.isNull(None self)"""
        return bool()
    def __repr__(self):
        """str QLine.__repr__(None self)"""
        return str()
    def __ne__(self, _d):
        """bool QLine.__ne__(None self, QLine _d)"""
        return bool()


class QLineF():
    """"""
    NoIntersection = int() # QLineF.IntersectType enum
    BoundedIntersection = int() # QLineF.IntersectType enum
    UnboundedIntersection = int() # QLineF.IntersectType enum

    def __init__(self, _line):
        """None QLineF.__init__(None self, QLine _line)"""
        return None
    def __init__(self):
        """None QLineF.__init__(None self)"""
        return None
    def __init__(self, _apt1, _apt2):
        """None QLineF.__init__(None self, QPointF _apt1, QPointF _apt2)"""
        return None
    def __init__(self, _x1pos, _y1pos, _x2pos, _y2pos):
        """None QLineF.__init__(None self, float _x1pos, float _y1pos, float _x2pos, float _y2pos)"""
        return None
    def __init__(self):
        """QLineF QLineF.__init__(None self)"""
        return QLineF()
    def setLine(self, _aX1, _aY1, _aX2, _aY2):
        """None QLineF.setLine(None self, float _aX1, float _aY1, float _aX2, float _aY2)"""
        return None
    def setPoints(self, _aP1, _aP2):
        """None QLineF.setPoints(None self, QPointF _aP1, QPointF _aP2)"""
        return None
    def setP2(self, _aP2):
        """None QLineF.setP2(None self, QPointF _aP2)"""
        return None
    def setP1(self, _aP1):
        """None QLineF.setP1(None self, QPointF _aP1)"""
        return None
    def translated(self, _p):
        """QLineF QLineF.translated(None self, QPointF _p)"""
        return QLineF()
    def translated(self, _adx, _ady):
        """QLineF QLineF.translated(None self, float _adx, float _ady)"""
        return QLineF()
    def angleTo(self, _l):
        """float QLineF.angleTo(None self, QLineF _l)"""
        return float()
    def setAngle(self, _angle):
        """None QLineF.setAngle(None self, float _angle)"""
        return None
    def fromPolar(self, _length, _angle):
        """QLineF QLineF.fromPolar(None self, float _length, float _angle)"""
        return QLineF()
    def __eq__(self, _d):
        """bool QLineF.__eq__(None self, QLineF _d)"""
        return bool()
    def toLine(self):
        """QLine QLineF.toLine(None self)"""
        return QLine()
    def pointAt(self, _t):
        """QPointF QLineF.pointAt(None self, float _t)"""
        return QPointF()
    def setLength(self, _len):
        """None QLineF.setLength(None self, float _len)"""
        return None
    def translate(self, _point):
        """None QLineF.translate(None self, QPointF _point)"""
        return None
    def translate(self, _adx, _ady):
        """None QLineF.translate(None self, float _adx, float _ady)"""
        return None
    def normalVector(self):
        """QLineF QLineF.normalVector(None self)"""
        return QLineF()
    def dy(self):
        """float QLineF.dy(None self)"""
        return float()
    def dx(self):
        """float QLineF.dx(None self)"""
        return float()
    def p2(self):
        """QPointF QLineF.p2(None self)"""
        return QPointF()
    def p1(self):
        """QPointF QLineF.p1(None self)"""
        return QPointF()
    def y2(self):
        """float QLineF.y2(None self)"""
        return float()
    def x2(self):
        """float QLineF.x2(None self)"""
        return float()
    def y1(self):
        """float QLineF.y1(None self)"""
        return float()
    def x1(self):
        """float QLineF.x1(None self)"""
        return float()
    def __repr__(self):
        """str QLineF.__repr__(None self)"""
        return str()
    def __ne__(self, _d):
        """bool QLineF.__ne__(None self, QLineF _d)"""
        return bool()
    def angle(self, _l):
        """float QLineF.angle(None self, QLineF _l)"""
        return float()
    def angle(self):
        """float QLineF.angle(None self)"""
        return float()
    def intersect(self, _l, _intersectionPoint):
        """QLineF.IntersectType QLineF.intersect(None self, QLineF _l, QPointF _intersectionPoint)"""
        return QLineF.IntersectType()
    def unitVector(self):
        """QLineF QLineF.unitVector(None self)"""
        return QLineF()
    def length(self):
        """float QLineF.length(None self)"""
        return float()
    def __bool__(self):
        """int QLineF.__bool__(None self)"""
        return int()
    def isNull(self):
        """bool QLineF.isNull(None self)"""
        return bool()


class QLibrary(QObject):
    """"""
    ResolveAllSymbolsHint = int() # QLibrary.LoadHint enum
    ExportExternalSymbolsHint = int() # QLibrary.LoadHint enum
    LoadArchiveMemberHint = int() # QLibrary.LoadHint enum

    def __init__(self, _parent):
        """None QLibrary.__init__(None self, QObject _parent)"""
        return None
    def __init__(self, _fileName, _parent):
        """None QLibrary.__init__(None self, QString _fileName, QObject _parent)"""
        return None
    def __init__(self, _fileName, _verNum, _parent):
        """None QLibrary.__init__(None self, QString _fileName, int _verNum, QObject _parent)"""
        return None
    def __init__(self, _fileName, _version, _parent):
        """None QLibrary.__init__(None self, QString _fileName, QString _version, QObject _parent)"""
        return None
    def setLoadHints(self, _hints):
        """None QLibrary.setLoadHints(None self, QLibrary.LoadHints _hints)"""
        return None
    def setFileNameAndVersion(self, _fileName, _verNum):
        """None QLibrary.setFileNameAndVersion(None self, QString _fileName, int _verNum)"""
        return None
    def setFileNameAndVersion(self, _fileName, _version):
        """None QLibrary.setFileNameAndVersion(None self, QString _fileName, QString _version)"""
        return None
    def setFileName(self, _fileName):
        """None QLibrary.setFileName(None self, QString _fileName)"""
        return None
    def isLibrary(self, _fileName):
        """bool QLibrary.isLibrary(None self, QString _fileName)"""
        return bool()
    def unload(self):
        """bool QLibrary.unload(None self)"""
        return bool()
    def resolve(self, _symbol):
        """sip.voidptr QLibrary.resolve(None self, str _symbol)"""
        return sip.voidptr()
    def resolve(self, _fileName, _symbol):
        """sip.voidptr QLibrary.resolve(None self, QString _fileName, str _symbol)"""
        return sip.voidptr()
    def resolve(self, _fileName, _verNum, _symbol):
        """sip.voidptr QLibrary.resolve(None self, QString _fileName, int _verNum, str _symbol)"""
        return sip.voidptr()
    def resolve(self, _fileName, _version, _symbol):
        """sip.voidptr QLibrary.resolve(None self, QString _fileName, QString _version, str _symbol)"""
        return sip.voidptr()
    def loadHints(self):
        """QLibrary.LoadHints QLibrary.loadHints(None self)"""
        return QLibrary.LoadHints()
    def load(self):
        """bool QLibrary.load(None self)"""
        return bool()
    def isLoaded(self):
        """bool QLibrary.isLoaded(None self)"""
        return bool()
    def fileName(self):
        """QString QLibrary.fileName(None self)"""
        return QString()
    def errorString(self):
        """QString QLibrary.errorString(None self)"""
        return QString()


class QLocale():
    """"""
    MetricSystem = int() # QLocale.MeasurementSystem enum
    ImperialSystem = int() # QLocale.MeasurementSystem enum

    LongFormat = int() # QLocale.FormatType enum
    ShortFormat = int() # QLocale.FormatType enum
    NarrowFormat = int() # QLocale.FormatType enum

    OmitGroupSeparator = int() # QLocale.NumberOption enum
    RejectGroupSeparator = int() # QLocale.NumberOption enum

    AnyCountry = int() # QLocale.Country enum
    Afghanistan = int() # QLocale.Country enum
    Albania = int() # QLocale.Country enum
    Algeria = int() # QLocale.Country enum
    AmericanSamoa = int() # QLocale.Country enum
    Andorra = int() # QLocale.Country enum
    Angola = int() # QLocale.Country enum
    Anguilla = int() # QLocale.Country enum
    Antarctica = int() # QLocale.Country enum
    AntiguaAndBarbuda = int() # QLocale.Country enum
    Argentina = int() # QLocale.Country enum
    Armenia = int() # QLocale.Country enum
    Aruba = int() # QLocale.Country enum
    Australia = int() # QLocale.Country enum
    Austria = int() # QLocale.Country enum
    Azerbaijan = int() # QLocale.Country enum
    Bahamas = int() # QLocale.Country enum
    Bahrain = int() # QLocale.Country enum
    Bangladesh = int() # QLocale.Country enum
    Barbados = int() # QLocale.Country enum
    Belarus = int() # QLocale.Country enum
    Belgium = int() # QLocale.Country enum
    Belize = int() # QLocale.Country enum
    Benin = int() # QLocale.Country enum
    Bermuda = int() # QLocale.Country enum
    Bhutan = int() # QLocale.Country enum
    Bolivia = int() # QLocale.Country enum
    BosniaAndHerzegowina = int() # QLocale.Country enum
    Botswana = int() # QLocale.Country enum
    BouvetIsland = int() # QLocale.Country enum
    Brazil = int() # QLocale.Country enum
    BritishIndianOceanTerritory = int() # QLocale.Country enum
    BruneiDarussalam = int() # QLocale.Country enum
    Bulgaria = int() # QLocale.Country enum
    BurkinaFaso = int() # QLocale.Country enum
    Burundi = int() # QLocale.Country enum
    Cambodia = int() # QLocale.Country enum
    Cameroon = int() # QLocale.Country enum
    Canada = int() # QLocale.Country enum
    CapeVerde = int() # QLocale.Country enum
    CaymanIslands = int() # QLocale.Country enum
    CentralAfricanRepublic = int() # QLocale.Country enum
    Chad = int() # QLocale.Country enum
    Chile = int() # QLocale.Country enum
    China = int() # QLocale.Country enum
    ChristmasIsland = int() # QLocale.Country enum
    CocosIslands = int() # QLocale.Country enum
    Colombia = int() # QLocale.Country enum
    Comoros = int() # QLocale.Country enum
    DemocraticRepublicOfCongo = int() # QLocale.Country enum
    PeoplesRepublicOfCongo = int() # QLocale.Country enum
    CookIslands = int() # QLocale.Country enum
    CostaRica = int() # QLocale.Country enum
    IvoryCoast = int() # QLocale.Country enum
    Croatia = int() # QLocale.Country enum
    Cuba = int() # QLocale.Country enum
    Cyprus = int() # QLocale.Country enum
    CzechRepublic = int() # QLocale.Country enum
    Denmark = int() # QLocale.Country enum
    Djibouti = int() # QLocale.Country enum
    Dominica = int() # QLocale.Country enum
    DominicanRepublic = int() # QLocale.Country enum
    EastTimor = int() # QLocale.Country enum
    Ecuador = int() # QLocale.Country enum
    Egypt = int() # QLocale.Country enum
    ElSalvador = int() # QLocale.Country enum
    EquatorialGuinea = int() # QLocale.Country enum
    Eritrea = int() # QLocale.Country enum
    Estonia = int() # QLocale.Country enum
    Ethiopia = int() # QLocale.Country enum
    FalklandIslands = int() # QLocale.Country enum
    FaroeIslands = int() # QLocale.Country enum
    FijiCountry = int() # QLocale.Country enum
    Finland = int() # QLocale.Country enum
    France = int() # QLocale.Country enum
    MetropolitanFrance = int() # QLocale.Country enum
    FrenchGuiana = int() # QLocale.Country enum
    FrenchPolynesia = int() # QLocale.Country enum
    FrenchSouthernTerritories = int() # QLocale.Country enum
    Gabon = int() # QLocale.Country enum
    Gambia = int() # QLocale.Country enum
    Georgia = int() # QLocale.Country enum
    Germany = int() # QLocale.Country enum
    Ghana = int() # QLocale.Country enum
    Gibraltar = int() # QLocale.Country enum
    Greece = int() # QLocale.Country enum
    Greenland = int() # QLocale.Country enum
    Grenada = int() # QLocale.Country enum
    Guadeloupe = int() # QLocale.Country enum
    Guam = int() # QLocale.Country enum
    Guatemala = int() # QLocale.Country enum
    Guinea = int() # QLocale.Country enum
    GuineaBissau = int() # QLocale.Country enum
    Guyana = int() # QLocale.Country enum
    Haiti = int() # QLocale.Country enum
    HeardAndMcDonaldIslands = int() # QLocale.Country enum
    Honduras = int() # QLocale.Country enum
    HongKong = int() # QLocale.Country enum
    Hungary = int() # QLocale.Country enum
    Iceland = int() # QLocale.Country enum
    India = int() # QLocale.Country enum
    Indonesia = int() # QLocale.Country enum
    Iran = int() # QLocale.Country enum
    Iraq = int() # QLocale.Country enum
    Ireland = int() # QLocale.Country enum
    Israel = int() # QLocale.Country enum
    Italy = int() # QLocale.Country enum
    Jamaica = int() # QLocale.Country enum
    Japan = int() # QLocale.Country enum
    Jordan = int() # QLocale.Country enum
    Kazakhstan = int() # QLocale.Country enum
    Kenya = int() # QLocale.Country enum
    Kiribati = int() # QLocale.Country enum
    DemocraticRepublicOfKorea = int() # QLocale.Country enum
    RepublicOfKorea = int() # QLocale.Country enum
    Kuwait = int() # QLocale.Country enum
    Kyrgyzstan = int() # QLocale.Country enum
    Lao = int() # QLocale.Country enum
    Latvia = int() # QLocale.Country enum
    Lebanon = int() # QLocale.Country enum
    Lesotho = int() # QLocale.Country enum
    Liberia = int() # QLocale.Country enum
    LibyanArabJamahiriya = int() # QLocale.Country enum
    Liechtenstein = int() # QLocale.Country enum
    Lithuania = int() # QLocale.Country enum
    Luxembourg = int() # QLocale.Country enum
    Macau = int() # QLocale.Country enum
    Macedonia = int() # QLocale.Country enum
    Madagascar = int() # QLocale.Country enum
    Malawi = int() # QLocale.Country enum
    Malaysia = int() # QLocale.Country enum
    Maldives = int() # QLocale.Country enum
    Mali = int() # QLocale.Country enum
    Malta = int() # QLocale.Country enum
    MarshallIslands = int() # QLocale.Country enum
    Martinique = int() # QLocale.Country enum
    Mauritania = int() # QLocale.Country enum
    Mauritius = int() # QLocale.Country enum
    Mayotte = int() # QLocale.Country enum
    Mexico = int() # QLocale.Country enum
    Micronesia = int() # QLocale.Country enum
    Moldova = int() # QLocale.Country enum
    Monaco = int() # QLocale.Country enum
    Mongolia = int() # QLocale.Country enum
    Montserrat = int() # QLocale.Country enum
    Morocco = int() # QLocale.Country enum
    Mozambique = int() # QLocale.Country enum
    Myanmar = int() # QLocale.Country enum
    Namibia = int() # QLocale.Country enum
    NauruCountry = int() # QLocale.Country enum
    Nepal = int() # QLocale.Country enum
    Netherlands = int() # QLocale.Country enum
    NetherlandsAntilles = int() # QLocale.Country enum
    NewCaledonia = int() # QLocale.Country enum
    NewZealand = int() # QLocale.Country enum
    Nicaragua = int() # QLocale.Country enum
    Niger = int() # QLocale.Country enum
    Nigeria = int() # QLocale.Country enum
    Niue = int() # QLocale.Country enum
    NorfolkIsland = int() # QLocale.Country enum
    NorthernMarianaIslands = int() # QLocale.Country enum
    Norway = int() # QLocale.Country enum
    Oman = int() # QLocale.Country enum
    Pakistan = int() # QLocale.Country enum
    Palau = int() # QLocale.Country enum
    PalestinianTerritory = int() # QLocale.Country enum
    Panama = int() # QLocale.Country enum
    PapuaNewGuinea = int() # QLocale.Country enum
    Paraguay = int() # QLocale.Country enum
    Peru = int() # QLocale.Country enum
    Philippines = int() # QLocale.Country enum
    Pitcairn = int() # QLocale.Country enum
    Poland = int() # QLocale.Country enum
    Portugal = int() # QLocale.Country enum
    PuertoRico = int() # QLocale.Country enum
    Qatar = int() # QLocale.Country enum
    Reunion = int() # QLocale.Country enum
    Romania = int() # QLocale.Country enum
    RussianFederation = int() # QLocale.Country enum
    Rwanda = int() # QLocale.Country enum
    SaintKittsAndNevis = int() # QLocale.Country enum
    StLucia = int() # QLocale.Country enum
    StVincentAndTheGrenadines = int() # QLocale.Country enum
    Samoa = int() # QLocale.Country enum
    SanMarino = int() # QLocale.Country enum
    SaoTomeAndPrincipe = int() # QLocale.Country enum
    SaudiArabia = int() # QLocale.Country enum
    Senegal = int() # QLocale.Country enum
    Seychelles = int() # QLocale.Country enum
    SierraLeone = int() # QLocale.Country enum
    Singapore = int() # QLocale.Country enum
    Slovakia = int() # QLocale.Country enum
    Slovenia = int() # QLocale.Country enum
    SolomonIslands = int() # QLocale.Country enum
    Somalia = int() # QLocale.Country enum
    SouthAfrica = int() # QLocale.Country enum
    SouthGeorgiaAndTheSouthSandwichIslands = int() # QLocale.Country enum
    Spain = int() # QLocale.Country enum
    SriLanka = int() # QLocale.Country enum
    StHelena = int() # QLocale.Country enum
    StPierreAndMiquelon = int() # QLocale.Country enum
    Sudan = int() # QLocale.Country enum
    Suriname = int() # QLocale.Country enum
    SvalbardAndJanMayenIslands = int() # QLocale.Country enum
    Swaziland = int() # QLocale.Country enum
    Sweden = int() # QLocale.Country enum
    Switzerland = int() # QLocale.Country enum
    SyrianArabRepublic = int() # QLocale.Country enum
    Taiwan = int() # QLocale.Country enum
    Tajikistan = int() # QLocale.Country enum
    Tanzania = int() # QLocale.Country enum
    Thailand = int() # QLocale.Country enum
    Togo = int() # QLocale.Country enum
    Tokelau = int() # QLocale.Country enum
    TongaCountry = int() # QLocale.Country enum
    TrinidadAndTobago = int() # QLocale.Country enum
    Tunisia = int() # QLocale.Country enum
    Turkey = int() # QLocale.Country enum
    Turkmenistan = int() # QLocale.Country enum
    TurksAndCaicosIslands = int() # QLocale.Country enum
    Tuvalu = int() # QLocale.Country enum
    Uganda = int() # QLocale.Country enum
    Ukraine = int() # QLocale.Country enum
    UnitedArabEmirates = int() # QLocale.Country enum
    UnitedKingdom = int() # QLocale.Country enum
    UnitedStates = int() # QLocale.Country enum
    UnitedStatesMinorOutlyingIslands = int() # QLocale.Country enum
    Uruguay = int() # QLocale.Country enum
    Uzbekistan = int() # QLocale.Country enum
    Vanuatu = int() # QLocale.Country enum
    VaticanCityState = int() # QLocale.Country enum
    Venezuela = int() # QLocale.Country enum
    VietNam = int() # QLocale.Country enum
    BritishVirginIslands = int() # QLocale.Country enum
    USVirginIslands = int() # QLocale.Country enum
    WallisAndFutunaIslands = int() # QLocale.Country enum
    WesternSahara = int() # QLocale.Country enum
    Yemen = int() # QLocale.Country enum
    Yugoslavia = int() # QLocale.Country enum
    Zambia = int() # QLocale.Country enum
    Zimbabwe = int() # QLocale.Country enum
    SerbiaAndMontenegro = int() # QLocale.Country enum
    Montenegro = int() # QLocale.Country enum
    Serbia = int() # QLocale.Country enum
    SaintBarthelemy = int() # QLocale.Country enum
    SaintMartin = int() # QLocale.Country enum
    LatinAmericaAndTheCaribbean = int() # QLocale.Country enum
    LastCountry = int() # QLocale.Country enum

    C = int() # QLocale.Language enum
    Abkhazian = int() # QLocale.Language enum
    Afan = int() # QLocale.Language enum
    Afar = int() # QLocale.Language enum
    Afrikaans = int() # QLocale.Language enum
    Albanian = int() # QLocale.Language enum
    Amharic = int() # QLocale.Language enum
    Arabic = int() # QLocale.Language enum
    Armenian = int() # QLocale.Language enum
    Assamese = int() # QLocale.Language enum
    Aymara = int() # QLocale.Language enum
    Azerbaijani = int() # QLocale.Language enum
    Bashkir = int() # QLocale.Language enum
    Basque = int() # QLocale.Language enum
    Bengali = int() # QLocale.Language enum
    Bhutani = int() # QLocale.Language enum
    Bihari = int() # QLocale.Language enum
    Bislama = int() # QLocale.Language enum
    Breton = int() # QLocale.Language enum
    Bulgarian = int() # QLocale.Language enum
    Burmese = int() # QLocale.Language enum
    Byelorussian = int() # QLocale.Language enum
    Cambodian = int() # QLocale.Language enum
    Catalan = int() # QLocale.Language enum
    Chinese = int() # QLocale.Language enum
    Corsican = int() # QLocale.Language enum
    Croatian = int() # QLocale.Language enum
    Czech = int() # QLocale.Language enum
    Danish = int() # QLocale.Language enum
    Dutch = int() # QLocale.Language enum
    English = int() # QLocale.Language enum
    Esperanto = int() # QLocale.Language enum
    Estonian = int() # QLocale.Language enum
    Faroese = int() # QLocale.Language enum
    FijiLanguage = int() # QLocale.Language enum
    Finnish = int() # QLocale.Language enum
    French = int() # QLocale.Language enum
    Frisian = int() # QLocale.Language enum
    Gaelic = int() # QLocale.Language enum
    Galician = int() # QLocale.Language enum
    Georgian = int() # QLocale.Language enum
    German = int() # QLocale.Language enum
    Greek = int() # QLocale.Language enum
    Greenlandic = int() # QLocale.Language enum
    Guarani = int() # QLocale.Language enum
    Gujarati = int() # QLocale.Language enum
    Hausa = int() # QLocale.Language enum
    Hebrew = int() # QLocale.Language enum
    Hindi = int() # QLocale.Language enum
    Hungarian = int() # QLocale.Language enum
    Icelandic = int() # QLocale.Language enum
    Indonesian = int() # QLocale.Language enum
    Interlingua = int() # QLocale.Language enum
    Interlingue = int() # QLocale.Language enum
    Inuktitut = int() # QLocale.Language enum
    Inupiak = int() # QLocale.Language enum
    Irish = int() # QLocale.Language enum
    Italian = int() # QLocale.Language enum
    Japanese = int() # QLocale.Language enum
    Javanese = int() # QLocale.Language enum
    Kannada = int() # QLocale.Language enum
    Kashmiri = int() # QLocale.Language enum
    Kazakh = int() # QLocale.Language enum
    Kinyarwanda = int() # QLocale.Language enum
    Kirghiz = int() # QLocale.Language enum
    Korean = int() # QLocale.Language enum
    Kurdish = int() # QLocale.Language enum
    Kurundi = int() # QLocale.Language enum
    Laothian = int() # QLocale.Language enum
    Latin = int() # QLocale.Language enum
    Latvian = int() # QLocale.Language enum
    Lingala = int() # QLocale.Language enum
    Lithuanian = int() # QLocale.Language enum
    Macedonian = int() # QLocale.Language enum
    Malagasy = int() # QLocale.Language enum
    Malay = int() # QLocale.Language enum
    Malayalam = int() # QLocale.Language enum
    Maltese = int() # QLocale.Language enum
    Maori = int() # QLocale.Language enum
    Marathi = int() # QLocale.Language enum
    Moldavian = int() # QLocale.Language enum
    Mongolian = int() # QLocale.Language enum
    NauruLanguage = int() # QLocale.Language enum
    Nepali = int() # QLocale.Language enum
    Norwegian = int() # QLocale.Language enum
    Occitan = int() # QLocale.Language enum
    Oriya = int() # QLocale.Language enum
    Pashto = int() # QLocale.Language enum
    Persian = int() # QLocale.Language enum
    Polish = int() # QLocale.Language enum
    Portuguese = int() # QLocale.Language enum
    Punjabi = int() # QLocale.Language enum
    Quechua = int() # QLocale.Language enum
    RhaetoRomance = int() # QLocale.Language enum
    Romanian = int() # QLocale.Language enum
    Russian = int() # QLocale.Language enum
    Samoan = int() # QLocale.Language enum
    Sangho = int() # QLocale.Language enum
    Sanskrit = int() # QLocale.Language enum
    Serbian = int() # QLocale.Language enum
    SerboCroatian = int() # QLocale.Language enum
    Sesotho = int() # QLocale.Language enum
    Setswana = int() # QLocale.Language enum
    Shona = int() # QLocale.Language enum
    Sindhi = int() # QLocale.Language enum
    Singhalese = int() # QLocale.Language enum
    Siswati = int() # QLocale.Language enum
    Slovak = int() # QLocale.Language enum
    Slovenian = int() # QLocale.Language enum
    Somali = int() # QLocale.Language enum
    Spanish = int() # QLocale.Language enum
    Sundanese = int() # QLocale.Language enum
    Swahili = int() # QLocale.Language enum
    Swedish = int() # QLocale.Language enum
    Tagalog = int() # QLocale.Language enum
    Tajik = int() # QLocale.Language enum
    Tamil = int() # QLocale.Language enum
    Tatar = int() # QLocale.Language enum
    Telugu = int() # QLocale.Language enum
    Thai = int() # QLocale.Language enum
    Tibetan = int() # QLocale.Language enum
    Tigrinya = int() # QLocale.Language enum
    TongaLanguage = int() # QLocale.Language enum
    Tsonga = int() # QLocale.Language enum
    Turkish = int() # QLocale.Language enum
    Turkmen = int() # QLocale.Language enum
    Twi = int() # QLocale.Language enum
    Uigur = int() # QLocale.Language enum
    Ukrainian = int() # QLocale.Language enum
    Urdu = int() # QLocale.Language enum
    Uzbek = int() # QLocale.Language enum
    Vietnamese = int() # QLocale.Language enum
    Volapuk = int() # QLocale.Language enum
    Welsh = int() # QLocale.Language enum
    Wolof = int() # QLocale.Language enum
    Xhosa = int() # QLocale.Language enum
    Yiddish = int() # QLocale.Language enum
    Yoruba = int() # QLocale.Language enum
    Zhuang = int() # QLocale.Language enum
    Zulu = int() # QLocale.Language enum
    Nynorsk = int() # QLocale.Language enum
    Bosnian = int() # QLocale.Language enum
    Divehi = int() # QLocale.Language enum
    Manx = int() # QLocale.Language enum
    Cornish = int() # QLocale.Language enum
    LastLanguage = int() # QLocale.Language enum
    NorwegianBokmal = int() # QLocale.Language enum
    NorwegianNynorsk = int() # QLocale.Language enum
    Akan = int() # QLocale.Language enum
    Konkani = int() # QLocale.Language enum
    Ga = int() # QLocale.Language enum
    Igbo = int() # QLocale.Language enum
    Kamba = int() # QLocale.Language enum
    Syriac = int() # QLocale.Language enum
    Blin = int() # QLocale.Language enum
    Geez = int() # QLocale.Language enum
    Koro = int() # QLocale.Language enum
    Sidamo = int() # QLocale.Language enum
    Atsam = int() # QLocale.Language enum
    Tigre = int() # QLocale.Language enum
    Jju = int() # QLocale.Language enum
    Friulian = int() # QLocale.Language enum
    Venda = int() # QLocale.Language enum
    Ewe = int() # QLocale.Language enum
    Walamo = int() # QLocale.Language enum
    Hawaiian = int() # QLocale.Language enum
    Tyap = int() # QLocale.Language enum
    Chewa = int() # QLocale.Language enum
    Filipino = int() # QLocale.Language enum
    SwissGerman = int() # QLocale.Language enum
    SichuanYi = int() # QLocale.Language enum
    Kpelle = int() # QLocale.Language enum
    LowGerman = int() # QLocale.Language enum
    SouthNdebele = int() # QLocale.Language enum
    NorthernSotho = int() # QLocale.Language enum
    NorthernSami = int() # QLocale.Language enum
    Taroko = int() # QLocale.Language enum
    Gusii = int() # QLocale.Language enum
    Taita = int() # QLocale.Language enum
    Fulah = int() # QLocale.Language enum
    Kikuyu = int() # QLocale.Language enum
    Samburu = int() # QLocale.Language enum
    Sena = int() # QLocale.Language enum
    NorthNdebele = int() # QLocale.Language enum
    Rombo = int() # QLocale.Language enum
    Tachelhit = int() # QLocale.Language enum
    Kabyle = int() # QLocale.Language enum
    Nyankole = int() # QLocale.Language enum
    Bena = int() # QLocale.Language enum
    Vunjo = int() # QLocale.Language enum
    Bambara = int() # QLocale.Language enum
    Embu = int() # QLocale.Language enum
    Cherokee = int() # QLocale.Language enum
    Morisyen = int() # QLocale.Language enum
    Makonde = int() # QLocale.Language enum
    Langi = int() # QLocale.Language enum
    Ganda = int() # QLocale.Language enum
    Bemba = int() # QLocale.Language enum
    Kabuverdianu = int() # QLocale.Language enum
    Meru = int() # QLocale.Language enum
    Kalenjin = int() # QLocale.Language enum
    Nama = int() # QLocale.Language enum
    Machame = int() # QLocale.Language enum
    Colognian = int() # QLocale.Language enum
    Masai = int() # QLocale.Language enum
    Soga = int() # QLocale.Language enum
    Luyia = int() # QLocale.Language enum
    Asu = int() # QLocale.Language enum
    Teso = int() # QLocale.Language enum
    Saho = int() # QLocale.Language enum
    KoyraChiini = int() # QLocale.Language enum
    Rwa = int() # QLocale.Language enum
    Luo = int() # QLocale.Language enum
    Chiga = int() # QLocale.Language enum
    CentralMoroccoTamazight = int() # QLocale.Language enum
    KoyraboroSenni = int() # QLocale.Language enum
    Shambala = int() # QLocale.Language enum

    def __init__(self):
        """None QLocale.__init__(None self)"""
        return None
    def __init__(self, _name):
        """None QLocale.__init__(None self, QString _name)"""
        return None
    def __init__(self, _language, _country):
        """None QLocale.__init__(None self, QLocale.Language _language, QLocale.Country _country)"""
        return None
    def __init__(self, _other):
        """None QLocale.__init__(None self, QLocale _other)"""
        return None
    def textDirection(self):
        """Qt.LayoutDirection QLocale.textDirection(None self)"""
        return Qt.LayoutDirection()
    def pmText(self):
        """QString QLocale.pmText(None self)"""
        return QString()
    def amText(self):
        """QString QLocale.amText(None self)"""
        return QString()
    def standaloneDayName(self, _format):
        """int QLocale.standaloneDayName(None self, QLocale.FormatType _format)"""
        return int()
    def standaloneMonthName(self, _format):
        """int QLocale.standaloneMonthName(None self, QLocale.FormatType _format)"""
        return int()
    def positiveSign(self):
        """QChar QLocale.positiveSign(None self)"""
        return QChar()
    def measurementSystem(self):
        """QLocale.MeasurementSystem QLocale.measurementSystem(None self)"""
        return QLocale.MeasurementSystem()
    def countriesForLanguage(self, _lang):
        """list-of-QLocale.Country QLocale.countriesForLanguage(None self, QLocale.Language _lang)"""
        return [QLocale.Country()]
    def numberOptions(self):
        """QLocale.NumberOptions QLocale.numberOptions(None self)"""
        return QLocale.NumberOptions()
    def setNumberOptions(self, _options):
        """None QLocale.setNumberOptions(None self, QLocale.NumberOptions _options)"""
        return None
    def dayName(self, _format):
        """int QLocale.dayName(None self, QLocale.FormatType _format)"""
        return int()
    def monthName(self, _format):
        """int QLocale.monthName(None self, QLocale.FormatType _format)"""
        return int()
    def exponential(self):
        """QChar QLocale.exponential(None self)"""
        return QChar()
    def negativeSign(self):
        """QChar QLocale.negativeSign(None self)"""
        return QChar()
    def zeroDigit(self):
        """QChar QLocale.zeroDigit(None self)"""
        return QChar()
    def percent(self):
        """QChar QLocale.percent(None self)"""
        return QChar()
    def groupSeparator(self):
        """QChar QLocale.groupSeparator(None self)"""
        return QChar()
    def decimalPoint(self):
        """QChar QLocale.decimalPoint(None self)"""
        return QChar()
    def toDateTime(self, _string, _format):
        """QDateTime QLocale.toDateTime(None self, QString _string, QLocale.FormatType _format)"""
        return QDateTime()
    def toDateTime(self, _string, _format):
        """QDateTime QLocale.toDateTime(None self, QString _string, QString _format)"""
        return QDateTime()
    def toTime(self, _string, _format):
        """QTime QLocale.toTime(None self, QString _string, QLocale.FormatType _format)"""
        return QTime()
    def toTime(self, _string, _format):
        """QTime QLocale.toTime(None self, QString _string, QString _format)"""
        return QTime()
    def toDate(self, _string, _format):
        """QDate QLocale.toDate(None self, QString _string, QLocale.FormatType _format)"""
        return QDate()
    def toDate(self, _string, _format):
        """QDate QLocale.toDate(None self, QString _string, QString _format)"""
        return QDate()
    def dateTimeFormat(self, _format):
        """QString QLocale.dateTimeFormat(None self, QLocale.FormatType _format)"""
        return QString()
    def timeFormat(self, _format):
        """QString QLocale.timeFormat(None self, QLocale.FormatType _format)"""
        return QString()
    def dateFormat(self, _format):
        """QString QLocale.dateFormat(None self, QLocale.FormatType _format)"""
        return QString()
    def system(self):
        """QLocale QLocale.system(None self)"""
        return QLocale()
    def c(self):
        """QLocale QLocale.c(None self)"""
        return QLocale()
    def setDefault(self, _locale):
        """None QLocale.setDefault(None self, QLocale _locale)"""
        return None
    def countryToString(self, _country):
        """QString QLocale.countryToString(None self, QLocale.Country _country)"""
        return QString()
    def languageToString(self, _language):
        """QString QLocale.languageToString(None self, QLocale.Language _language)"""
        return QString()
    def __ne__(self, _other):
        """bool QLocale.__ne__(None self, QLocale _other)"""
        return bool()
    def __eq__(self, _other):
        """bool QLocale.__eq__(None self, QLocale _other)"""
        return bool()
    def toString(self, _i):
        """QString QLocale.toString(None self, int _i)"""
        return QString()
    def toString(self, _i, _format, _precision):
        """QString QLocale.toString(None self, float _i, str _format, int _precision)"""
        return QString()
    def toString(self, _i):
        """QString QLocale.toString(None self, int _i)"""
        return QString()
    def toString(self, _i):
        """QString QLocale.toString(None self, int _i)"""
        return QString()
    def toString(self, _dateTime, _format):
        """QString QLocale.toString(None self, QDateTime _dateTime, QString _format)"""
        return QString()
    def toString(self, _dateTime, _format):
        """QString QLocale.toString(None self, QDateTime _dateTime, QLocale.FormatType _format)"""
        return QString()
    def toString(self, _date, _formatStr):
        """QString QLocale.toString(None self, QDate _date, QString _formatStr)"""
        return QString()
    def toString(self, _date, _format):
        """QString QLocale.toString(None self, QDate _date, QLocale.FormatType _format)"""
        return QString()
    def toString(self, _time, _formatStr):
        """QString QLocale.toString(None self, QTime _time, QString _formatStr)"""
        return QString()
    def toString(self, _time, _format):
        """QString QLocale.toString(None self, QTime _time, QLocale.FormatType _format)"""
        return QString()
    def toDouble(self, _s, _ok):
        """float QLocale.toDouble(None self, QString _s, bool _ok)"""
        return float()
    def toFloat(self, _s, _ok):
        """float QLocale.toFloat(None self, QString _s, bool _ok)"""
        return float()
    def toULongLong(self, _s, _ok, _base):
        """int QLocale.toULongLong(None self, QString _s, bool _ok, int _base)"""
        return int()
    def toLongLong(self, _s, _ok, _base):
        """int QLocale.toLongLong(None self, QString _s, bool _ok, int _base)"""
        return int()
    def toUInt(self, _s, _ok, _base):
        """int QLocale.toUInt(None self, QString _s, bool _ok, int _base)"""
        return int()
    def toInt(self, _s, _ok, _base):
        """int QLocale.toInt(None self, QString _s, bool _ok, int _base)"""
        return int()
    def toUShort(self, _s, _ok, _base):
        """int QLocale.toUShort(None self, QString _s, bool _ok, int _base)"""
        return int()
    def toShort(self, _s, _ok, _base):
        """int QLocale.toShort(None self, QString _s, bool _ok, int _base)"""
        return int()
    def name(self):
        """QString QLocale.name(None self)"""
        return QString()
    def country(self):
        """QLocale.Country QLocale.country(None self)"""
        return QLocale.Country()
    def language(self):
        """QLocale.Language QLocale.language(None self)"""
        return QLocale.Language()


class QSystemLocale():
    """"""
    LanguageId = int() # QSystemLocale.QueryType enum
    CountryId = int() # QSystemLocale.QueryType enum
    DecimalPoint = int() # QSystemLocale.QueryType enum
    GroupSeparator = int() # QSystemLocale.QueryType enum
    ZeroDigit = int() # QSystemLocale.QueryType enum
    NegativeSign = int() # QSystemLocale.QueryType enum
    DateFormatLong = int() # QSystemLocale.QueryType enum
    DateFormatShort = int() # QSystemLocale.QueryType enum
    TimeFormatLong = int() # QSystemLocale.QueryType enum
    TimeFormatShort = int() # QSystemLocale.QueryType enum
    DayNameLong = int() # QSystemLocale.QueryType enum
    DayNameShort = int() # QSystemLocale.QueryType enum
    MonthNameLong = int() # QSystemLocale.QueryType enum
    MonthNameShort = int() # QSystemLocale.QueryType enum
    DateToStringLong = int() # QSystemLocale.QueryType enum
    DateToStringShort = int() # QSystemLocale.QueryType enum
    TimeToStringLong = int() # QSystemLocale.QueryType enum
    TimeToStringShort = int() # QSystemLocale.QueryType enum
    DateTimeFormatLong = int() # QSystemLocale.QueryType enum
    DateTimeFormatShort = int() # QSystemLocale.QueryType enum
    DateTimeToStringLong = int() # QSystemLocale.QueryType enum
    DateTimeToStringShort = int() # QSystemLocale.QueryType enum
    MeasurementSystem = int() # QSystemLocale.QueryType enum
    PositiveSign = int() # QSystemLocale.QueryType enum
    AMText = int() # QSystemLocale.QueryType enum
    PMText = int() # QSystemLocale.QueryType enum

    def __init__(self):
        """None QSystemLocale.__init__(None self)"""
        return None
    def __init__(self):
        """QSystemLocale QSystemLocale.__init__(None self)"""
        return QSystemLocale()
    def fallbackLocale(self):
        """QLocale QSystemLocale.fallbackLocale(None self)"""
        return QLocale()
    def query(self, _type, _in):
        """QVariant QSystemLocale.query(None self, QSystemLocale.QueryType _type, QVariant _in)"""
        return QVariant()


class QMargins():
    """"""
    def __init__(self):
        """None QMargins.__init__(None self)"""
        return None
    def __init__(self, _aleft, _atop, _aright, _abottom):
        """None QMargins.__init__(None self, int _aleft, int _atop, int _aright, int _abottom)"""
        return None
    def __init__(self):
        """QMargins QMargins.__init__(None self)"""
        return QMargins()
    def __eq__(self, _m2):
        """bool QMargins.__eq__(None self, QMargins _m2)"""
        return bool()
    def __ne__(self, _m2):
        """bool QMargins.__ne__(None self, QMargins _m2)"""
        return bool()
    def setBottom(self, _abottom):
        """None QMargins.setBottom(None self, int _abottom)"""
        return None
    def setRight(self, _aright):
        """None QMargins.setRight(None self, int _aright)"""
        return None
    def setTop(self, _atop):
        """None QMargins.setTop(None self, int _atop)"""
        return None
    def setLeft(self, _aleft):
        """None QMargins.setLeft(None self, int _aleft)"""
        return None
    def bottom(self):
        """int QMargins.bottom(None self)"""
        return int()
    def right(self):
        """int QMargins.right(None self)"""
        return int()
    def top(self):
        """int QMargins.top(None self)"""
        return int()
    def left(self):
        """int QMargins.left(None self)"""
        return int()
    def isNull(self):
        """bool QMargins.isNull(None self)"""
        return bool()


class QMetaMethod():
    """"""
    Method = int() # QMetaMethod.MethodType enum
    Signal = int() # QMetaMethod.MethodType enum
    Slot = int() # QMetaMethod.MethodType enum
    Constructor = int() # QMetaMethod.MethodType enum

    Private = int() # QMetaMethod.Access enum
    Protected = int() # QMetaMethod.Access enum
    Public = int() # QMetaMethod.Access enum

    def __init__(self):
        """None QMetaMethod.__init__(None self)"""
        return None
    def __init__(self):
        """QMetaMethod QMetaMethod.__init__(None self)"""
        return QMetaMethod()
    def methodIndex(self):
        """int QMetaMethod.methodIndex(None self)"""
        return int()
    def invoke(self, _object, _connectionType, _returnValue, _value0, _value1, _value2, _value3, _value4, _value5, _value6, _value7, _value8, _value9):
        """object QMetaMethod.invoke(None self, QObject _object, Qt.ConnectionType _connectionType, QGenericReturnArgument _returnValue, QGenericArgument _value0, QGenericArgument _value1, QGenericArgument _value2, QGenericArgument _value3, QGenericArgument _value4, QGenericArgument _value5, QGenericArgument _value6, QGenericArgument _value7, QGenericArgument _value8, QGenericArgument _value9)"""
        return object()
    def invoke(self, _object, _returnValue, _value0, _value1, _value2, _value3, _value4, _value5, _value6, _value7, _value8, _value9):
        """object QMetaMethod.invoke(None self, QObject _object, QGenericReturnArgument _returnValue, QGenericArgument _value0, QGenericArgument _value1, QGenericArgument _value2, QGenericArgument _value3, QGenericArgument _value4, QGenericArgument _value5, QGenericArgument _value6, QGenericArgument _value7, QGenericArgument _value8, QGenericArgument _value9)"""
        return object()
    def invoke(self, _object, _connectionType, _value0, _value1, _value2, _value3, _value4, _value5, _value6, _value7, _value8, _value9):
        """object QMetaMethod.invoke(None self, QObject _object, Qt.ConnectionType _connectionType, QGenericArgument _value0, QGenericArgument _value1, QGenericArgument _value2, QGenericArgument _value3, QGenericArgument _value4, QGenericArgument _value5, QGenericArgument _value6, QGenericArgument _value7, QGenericArgument _value8, QGenericArgument _value9)"""
        return object()
    def invoke(self, _object, _value0, _value1, _value2, _value3, _value4, _value5, _value6, _value7, _value8, _value9):
        """object QMetaMethod.invoke(None self, QObject _object, QGenericArgument _value0, QGenericArgument _value1, QGenericArgument _value2, QGenericArgument _value3, QGenericArgument _value4, QGenericArgument _value5, QGenericArgument _value6, QGenericArgument _value7, QGenericArgument _value8, QGenericArgument _value9)"""
        return object()
    def methodType(self):
        """QMetaMethod.MethodType QMetaMethod.methodType(None self)"""
        return QMetaMethod.MethodType()
    def access(self):
        """QMetaMethod.Access QMetaMethod.access(None self)"""
        return QMetaMethod.Access()
    def tag(self):
        """str QMetaMethod.tag(None self)"""
        return str()
    def parameterNames(self):
        """list-of-QByteArray QMetaMethod.parameterNames(None self)"""
        return [QByteArray()]
    def parameterTypes(self):
        """list-of-QByteArray QMetaMethod.parameterTypes(None self)"""
        return [QByteArray()]
    def typeName(self):
        """str QMetaMethod.typeName(None self)"""
        return str()
    def signature(self):
        """str QMetaMethod.signature(None self)"""
        return str()


class QMetaEnum():
    """"""
    def __init__(self):
        """None QMetaEnum.__init__(None self)"""
        return None
    def __init__(self):
        """QMetaEnum QMetaEnum.__init__(None self)"""
        return QMetaEnum()
    def isValid(self):
        """bool QMetaEnum.isValid(None self)"""
        return bool()
    def valueToKeys(self, _value):
        """QByteArray QMetaEnum.valueToKeys(None self, int _value)"""
        return QByteArray()
    def keysToValue(self, _keys):
        """int QMetaEnum.keysToValue(None self, str _keys)"""
        return int()
    def valueToKey(self, _value):
        """str QMetaEnum.valueToKey(None self, int _value)"""
        return str()
    def keyToValue(self, _key):
        """int QMetaEnum.keyToValue(None self, str _key)"""
        return int()
    def scope(self):
        """str QMetaEnum.scope(None self)"""
        return str()
    def value(self, _index):
        """int QMetaEnum.value(None self, int _index)"""
        return int()
    def key(self, _index):
        """str QMetaEnum.key(None self, int _index)"""
        return str()
    def keyCount(self):
        """int QMetaEnum.keyCount(None self)"""
        return int()
    def isFlag(self):
        """bool QMetaEnum.isFlag(None self)"""
        return bool()
    def name(self):
        """str QMetaEnum.name(None self)"""
        return str()


class QMetaProperty():
    """"""
    def __init__(self):
        """None QMetaProperty.__init__(None self)"""
        return None
    def __init__(self):
        """QMetaProperty QMetaProperty.__init__(None self)"""
        return QMetaProperty()
    def isFinal(self):
        """bool QMetaProperty.isFinal(None self)"""
        return bool()
    def isConstant(self):
        """bool QMetaProperty.isConstant(None self)"""
        return bool()
    def propertyIndex(self):
        """int QMetaProperty.propertyIndex(None self)"""
        return int()
    def notifySignalIndex(self):
        """int QMetaProperty.notifySignalIndex(None self)"""
        return int()
    def notifySignal(self):
        """QMetaMethod QMetaProperty.notifySignal(None self)"""
        return QMetaMethod()
    def hasNotifySignal(self):
        """bool QMetaProperty.hasNotifySignal(None self)"""
        return bool()
    def userType(self):
        """int QMetaProperty.userType(None self)"""
        return int()
    def isUser(self, _object):
        """bool QMetaProperty.isUser(None self, QObject _object)"""
        return bool()
    def isResettable(self):
        """bool QMetaProperty.isResettable(None self)"""
        return bool()
    def isValid(self):
        """bool QMetaProperty.isValid(None self)"""
        return bool()
    def hasStdCppSet(self):
        """bool QMetaProperty.hasStdCppSet(None self)"""
        return bool()
    def reset(self, _obj):
        """bool QMetaProperty.reset(None self, QObject _obj)"""
        return bool()
    def write(self, _obj, _value):
        """bool QMetaProperty.write(None self, QObject _obj, QVariant _value)"""
        return bool()
    def read(self, _obj):
        """QVariant QMetaProperty.read(None self, QObject _obj)"""
        return QVariant()
    def enumerator(self):
        """QMetaEnum QMetaProperty.enumerator(None self)"""
        return QMetaEnum()
    def isEnumType(self):
        """bool QMetaProperty.isEnumType(None self)"""
        return bool()
    def isFlagType(self):
        """bool QMetaProperty.isFlagType(None self)"""
        return bool()
    def isEditable(self, _object):
        """bool QMetaProperty.isEditable(None self, QObject _object)"""
        return bool()
    def isStored(self, _object):
        """bool QMetaProperty.isStored(None self, QObject _object)"""
        return bool()
    def isScriptable(self, _object):
        """bool QMetaProperty.isScriptable(None self, QObject _object)"""
        return bool()
    def isDesignable(self, _object):
        """bool QMetaProperty.isDesignable(None self, QObject _object)"""
        return bool()
    def isWritable(self):
        """bool QMetaProperty.isWritable(None self)"""
        return bool()
    def isReadable(self):
        """bool QMetaProperty.isReadable(None self)"""
        return bool()
    def type(self):
        """Type QMetaProperty.type(None self)"""
        return Type()
    def typeName(self):
        """str QMetaProperty.typeName(None self)"""
        return str()
    def name(self):
        """str QMetaProperty.name(None self)"""
        return str()


class QMetaClassInfo():
    """"""
    def __init__(self):
        """None QMetaClassInfo.__init__(None self)"""
        return None
    def __init__(self):
        """QMetaClassInfo QMetaClassInfo.__init__(None self)"""
        return QMetaClassInfo()
    def value(self):
        """str QMetaClassInfo.value(None self)"""
        return str()
    def name(self):
        """str QMetaClassInfo.name(None self)"""
        return str()


class QMetaType():
    """"""
    Void = int() # QMetaType.Type enum
    Bool = int() # QMetaType.Type enum
    Int = int() # QMetaType.Type enum
    UInt = int() # QMetaType.Type enum
    LongLong = int() # QMetaType.Type enum
    ULongLong = int() # QMetaType.Type enum
    Double = int() # QMetaType.Type enum
    QChar = int() # QMetaType.Type enum
    QVariantMap = int() # QMetaType.Type enum
    QVariantList = int() # QMetaType.Type enum
    QVariantHash = int() # QMetaType.Type enum
    QString = int() # QMetaType.Type enum
    QStringList = int() # QMetaType.Type enum
    QByteArray = int() # QMetaType.Type enum
    QBitArray = int() # QMetaType.Type enum
    QDate = int() # QMetaType.Type enum
    QTime = int() # QMetaType.Type enum
    QDateTime = int() # QMetaType.Type enum
    QUrl = int() # QMetaType.Type enum
    QLocale = int() # QMetaType.Type enum
    QRect = int() # QMetaType.Type enum
    QRectF = int() # QMetaType.Type enum
    QSize = int() # QMetaType.Type enum
    QSizeF = int() # QMetaType.Type enum
    QLine = int() # QMetaType.Type enum
    QLineF = int() # QMetaType.Type enum
    QPoint = int() # QMetaType.Type enum
    QPointF = int() # QMetaType.Type enum
    QRegExp = int() # QMetaType.Type enum
    LastCoreType = int() # QMetaType.Type enum
    FirstGuiType = int() # QMetaType.Type enum
    QFont = int() # QMetaType.Type enum
    QPixmap = int() # QMetaType.Type enum
    QBrush = int() # QMetaType.Type enum
    QColor = int() # QMetaType.Type enum
    QPalette = int() # QMetaType.Type enum
    QIcon = int() # QMetaType.Type enum
    QImage = int() # QMetaType.Type enum
    QPolygon = int() # QMetaType.Type enum
    QRegion = int() # QMetaType.Type enum
    QBitmap = int() # QMetaType.Type enum
    QCursor = int() # QMetaType.Type enum
    QSizePolicy = int() # QMetaType.Type enum
    QKeySequence = int() # QMetaType.Type enum
    QPen = int() # QMetaType.Type enum
    QTextLength = int() # QMetaType.Type enum
    QTextFormat = int() # QMetaType.Type enum
    QMatrix = int() # QMetaType.Type enum
    QTransform = int() # QMetaType.Type enum
    VoidStar = int() # QMetaType.Type enum
    Long = int() # QMetaType.Type enum
    Short = int() # QMetaType.Type enum
    Char = int() # QMetaType.Type enum
    ULong = int() # QMetaType.Type enum
    UShort = int() # QMetaType.Type enum
    UChar = int() # QMetaType.Type enum
    Float = int() # QMetaType.Type enum
    QObjectStar = int() # QMetaType.Type enum
    QWidgetStar = int() # QMetaType.Type enum
    QMatrix4x4 = int() # QMetaType.Type enum
    QVector2D = int() # QMetaType.Type enum
    QVector3D = int() # QMetaType.Type enum
    QVector4D = int() # QMetaType.Type enum
    QQuaternion = int() # QMetaType.Type enum
    QEasingCurve = int() # QMetaType.Type enum
    QVariant = int() # QMetaType.Type enum
    User = int() # QMetaType.Type enum

    def __init__(self):
        """None QMetaType.__init__(None self)"""
        return None
    def __init__(self):
        """QMetaType QMetaType.__init__(None self)"""
        return QMetaType()
    def isRegistered(self, _type):
        """bool QMetaType.isRegistered(None self, int _type)"""
        return bool()
    def typeName(self, _type):
        """str QMetaType.typeName(None self, int _type)"""
        return str()
    def type(self, _typeName):
        """int QMetaType.type(None self, str _typeName)"""
        return int()


class QMimeData(QObject):
    """"""
    def __init__(self):
        """None QMimeData.__init__(None self)"""
        return None
    def retrieveData(self, _mimetype, _preferredType):
        """QVariant QMimeData.retrieveData(None self, QString _mimetype, Type _preferredType)"""
        return QVariant()
    def removeFormat(self, _mimetype):
        """None QMimeData.removeFormat(None self, QString _mimetype)"""
        return None
    def clear(self):
        """None QMimeData.clear(None self)"""
        return None
    def formats(self):
        """QStringList QMimeData.formats(None self)"""
        return QStringList()
    def hasFormat(self, _mimetype):
        """bool QMimeData.hasFormat(None self, QString _mimetype)"""
        return bool()
    def setData(self, _mimetype, _data):
        """None QMimeData.setData(None self, QString _mimetype, QByteArray _data)"""
        return None
    def data(self, _mimetype):
        """QByteArray QMimeData.data(None self, QString _mimetype)"""
        return QByteArray()
    def hasColor(self):
        """bool QMimeData.hasColor(None self)"""
        return bool()
    def setColorData(self, _color):
        """None QMimeData.setColorData(None self, QVariant _color)"""
        return None
    def colorData(self):
        """QVariant QMimeData.colorData(None self)"""
        return QVariant()
    def hasImage(self):
        """bool QMimeData.hasImage(None self)"""
        return bool()
    def setImageData(self, _image):
        """None QMimeData.setImageData(None self, QVariant _image)"""
        return None
    def imageData(self):
        """QVariant QMimeData.imageData(None self)"""
        return QVariant()
    def hasHtml(self):
        """bool QMimeData.hasHtml(None self)"""
        return bool()
    def setHtml(self, _html):
        """None QMimeData.setHtml(None self, QString _html)"""
        return None
    def html(self):
        """QString QMimeData.html(None self)"""
        return QString()
    def hasText(self):
        """bool QMimeData.hasText(None self)"""
        return bool()
    def setText(self, _text):
        """None QMimeData.setText(None self, QString _text)"""
        return None
    def text(self):
        """QString QMimeData.text(None self)"""
        return QString()
    def hasUrls(self):
        """bool QMimeData.hasUrls(None self)"""
        return bool()
    def setUrls(self, _urls):
        """None QMimeData.setUrls(None self, list-of-QUrl _urls)"""
        return None
    def urls(self):
        """list-of-QUrl QMimeData.urls(None self)"""
        return [QUrl()]


class QMutex():
    """"""
    NonRecursive = int() # QMutex.RecursionMode enum
    Recursive = int() # QMutex.RecursionMode enum

    def __init__(self, _mode):
        """None QMutex.__init__(None self, QMutex.RecursionMode _mode)"""
        return None
    def unlock(self):
        """None QMutex.unlock(None self)"""
        return None
    def tryLock(self):
        """bool QMutex.tryLock(None self)"""
        return bool()
    def tryLock(self, _timeout):
        """bool QMutex.tryLock(None self, int _timeout)"""
        return bool()
    def lock(self):
        """None QMutex.lock(None self)"""
        return None


class QMutexLocker():
    """"""
    def __init__(self, _m):
        """None QMutexLocker.__init__(None self, QMutex _m)"""
        return None
    def __exit__(self, _type, _value, _traceback):
        """None QMutexLocker.__exit__(None self, object _type, object _value, object _traceback)"""
        return None
    def __enter__(self):
        """object QMutexLocker.__enter__(None self)"""
        return object()
    def mutex(self):
        """QMutex QMutexLocker.mutex(None self)"""
        return QMutex()
    def relock(self):
        """None QMutexLocker.relock(None self)"""
        return None
    def unlock(self):
        """None QMutexLocker.unlock(None self)"""
        return None


class QObjectCleanupHandler(QObject):
    """"""
    def __init__(self):
        """None QObjectCleanupHandler.__init__(None self)"""
        return None
    def clear(self):
        """None QObjectCleanupHandler.clear(None self)"""
        return None
    def isEmpty(self):
        """bool QObjectCleanupHandler.isEmpty(None self)"""
        return bool()
    def remove(self, _object):
        """None QObjectCleanupHandler.remove(None self, QObject _object)"""
        return None
    def add(self, _object):
        """QObject QObjectCleanupHandler.add(None self, QObject _object)"""
        return QObject()


class QMetaObject():
    """"""
    def __init__(self):
        """None QMetaObject.__init__(None self)"""
        return None
    def __init__(self):
        """QMetaObject QMetaObject.__init__(None self)"""
        return QMetaObject()
    def newInstance(self, _value0, _value1, _value2, _value3, _value4, _value5, _value6, _value7, _value8, _value9):
        """QObject QMetaObject.newInstance(None self, QGenericArgument _value0, QGenericArgument _value1, QGenericArgument _value2, QGenericArgument _value3, QGenericArgument _value4, QGenericArgument _value5, QGenericArgument _value6, QGenericArgument _value7, QGenericArgument _value8, QGenericArgument _value9)"""
        return QObject()
    def constructor(self, _index):
        """QMetaMethod QMetaObject.constructor(None self, int _index)"""
        return QMetaMethod()
    def indexOfConstructor(self, _constructor):
        """int QMetaObject.indexOfConstructor(None self, str _constructor)"""
        return int()
    def constructorCount(self):
        """int QMetaObject.constructorCount(None self)"""
        return int()
    def invokeMethod(self, _obj, _member, _type, _ret, _value0, _value1, _value2, _value3, _value4, _value5, _value6, _value7, _value8, _value9):
        """object QMetaObject.invokeMethod(None self, QObject _obj, str _member, Qt.ConnectionType _type, QGenericReturnArgument _ret, QGenericArgument _value0, QGenericArgument _value1, QGenericArgument _value2, QGenericArgument _value3, QGenericArgument _value4, QGenericArgument _value5, QGenericArgument _value6, QGenericArgument _value7, QGenericArgument _value8, QGenericArgument _value9)"""
        return object()
    def invokeMethod(self, _obj, _member, _ret, _value0, _value1, _value2, _value3, _value4, _value5, _value6, _value7, _value8, _value9):
        """object QMetaObject.invokeMethod(None self, QObject _obj, str _member, QGenericReturnArgument _ret, QGenericArgument _value0, QGenericArgument _value1, QGenericArgument _value2, QGenericArgument _value3, QGenericArgument _value4, QGenericArgument _value5, QGenericArgument _value6, QGenericArgument _value7, QGenericArgument _value8, QGenericArgument _value9)"""
        return object()
    def invokeMethod(self, _obj, _member, _type, _value0, _value1, _value2, _value3, _value4, _value5, _value6, _value7, _value8, _value9):
        """object QMetaObject.invokeMethod(None self, QObject _obj, str _member, Qt.ConnectionType _type, QGenericArgument _value0, QGenericArgument _value1, QGenericArgument _value2, QGenericArgument _value3, QGenericArgument _value4, QGenericArgument _value5, QGenericArgument _value6, QGenericArgument _value7, QGenericArgument _value8, QGenericArgument _value9)"""
        return object()
    def invokeMethod(self, _obj, _member, _value0, _value1, _value2, _value3, _value4, _value5, _value6, _value7, _value8, _value9):
        """object QMetaObject.invokeMethod(None self, QObject _obj, str _member, QGenericArgument _value0, QGenericArgument _value1, QGenericArgument _value2, QGenericArgument _value3, QGenericArgument _value4, QGenericArgument _value5, QGenericArgument _value6, QGenericArgument _value7, QGenericArgument _value8, QGenericArgument _value9)"""
        return object()
    def normalizedType(self, _type):
        """QByteArray QMetaObject.normalizedType(None self, str _type)"""
        return QByteArray()
    def normalizedSignature(self, _method):
        """QByteArray QMetaObject.normalizedSignature(None self, str _method)"""
        return QByteArray()
    def connectSlotsByName(self, _o):
        """None QMetaObject.connectSlotsByName(None self, QObject _o)"""
        return None
    def checkConnectArgs(self, _signal, _method):
        """bool QMetaObject.checkConnectArgs(None self, str _signal, str _method)"""
        return bool()
    def classInfo(self, _index):
        """QMetaClassInfo QMetaObject.classInfo(None self, int _index)"""
        return QMetaClassInfo()
    def property(self, _index):
        """QMetaProperty QMetaObject.property(None self, int _index)"""
        return QMetaProperty()
    def enumerator(self, _index):
        """QMetaEnum QMetaObject.enumerator(None self, int _index)"""
        return QMetaEnum()
    def method(self, _index):
        """QMetaMethod QMetaObject.method(None self, int _index)"""
        return QMetaMethod()
    def indexOfClassInfo(self, _name):
        """int QMetaObject.indexOfClassInfo(None self, str _name)"""
        return int()
    def indexOfProperty(self, _name):
        """int QMetaObject.indexOfProperty(None self, str _name)"""
        return int()
    def indexOfEnumerator(self, _name):
        """int QMetaObject.indexOfEnumerator(None self, str _name)"""
        return int()
    def indexOfSlot(self, _slot):
        """int QMetaObject.indexOfSlot(None self, str _slot)"""
        return int()
    def indexOfSignal(self, _signal):
        """int QMetaObject.indexOfSignal(None self, str _signal)"""
        return int()
    def indexOfMethod(self, _method):
        """int QMetaObject.indexOfMethod(None self, str _method)"""
        return int()
    def classInfoCount(self):
        """int QMetaObject.classInfoCount(None self)"""
        return int()
    def propertyCount(self):
        """int QMetaObject.propertyCount(None self)"""
        return int()
    def enumeratorCount(self):
        """int QMetaObject.enumeratorCount(None self)"""
        return int()
    def methodCount(self):
        """int QMetaObject.methodCount(None self)"""
        return int()
    def classInfoOffset(self):
        """int QMetaObject.classInfoOffset(None self)"""
        return int()
    def propertyOffset(self):
        """int QMetaObject.propertyOffset(None self)"""
        return int()
    def enumeratorOffset(self):
        """int QMetaObject.enumeratorOffset(None self)"""
        return int()
    def methodOffset(self):
        """int QMetaObject.methodOffset(None self)"""
        return int()
    def userProperty(self):
        """QMetaProperty QMetaObject.userProperty(None self)"""
        return QMetaProperty()
    def superClass(self):
        """QMetaObject QMetaObject.superClass(None self)"""
        return QMetaObject()
    def className(self):
        """str QMetaObject.className(None self)"""
        return str()


class QGenericArgument():
    """"""


class QGenericReturnArgument():
    """"""


class QParallelAnimationGroup(QAnimationGroup):
    """"""
    def __init__(self, _parent):
        """None QParallelAnimationGroup.__init__(None self, QObject _parent)"""
        return None
    def updateDirection(self, _direction):
        """None QParallelAnimationGroup.updateDirection(None self, QAbstractAnimation.Direction _direction)"""
        return None
    def updateState(self, _newState, _oldState):
        """None QParallelAnimationGroup.updateState(None self, QAbstractAnimation.State _newState, QAbstractAnimation.State _oldState)"""
        return None
    def updateCurrentTime(self, _currentTime):
        """None QParallelAnimationGroup.updateCurrentTime(None self, int _currentTime)"""
        return None
    def event(self, _event):
        """bool QParallelAnimationGroup.event(None self, QEvent _event)"""
        return bool()
    def duration(self):
        """int QParallelAnimationGroup.duration(None self)"""
        return int()


class QPauseAnimation(QAbstractAnimation):
    """"""
    def __init__(self, _parent):
        """None QPauseAnimation.__init__(None self, QObject _parent)"""
        return None
    def __init__(self, _msecs, _parent):
        """None QPauseAnimation.__init__(None self, int _msecs, QObject _parent)"""
        return None
    def updateCurrentTime(self):
        """int QPauseAnimation.updateCurrentTime(None self)"""
        return int()
    def event(self, _e):
        """bool QPauseAnimation.event(None self, QEvent _e)"""
        return bool()
    def setDuration(self, _msecs):
        """None QPauseAnimation.setDuration(None self, int _msecs)"""
        return None
    def duration(self):
        """int QPauseAnimation.duration(None self)"""
        return int()


class QVariantAnimation(QAbstractAnimation):
    """"""
    def __init__(self, _parent):
        """None QVariantAnimation.__init__(None self, QObject _parent)"""
        return None
    def interpolated(self, _from, _to, _progress):
        """QVariant QVariantAnimation.interpolated(None self, QVariant _from, QVariant _to, float _progress)"""
        return QVariant()
    def updateCurrentValue(self, _value):
        """abstract None QVariantAnimation.updateCurrentValue(None self, QVariant _value)"""
        return None
    def updateState(self, _newState, _oldState):
        """None QVariantAnimation.updateState(None self, QAbstractAnimation.State _newState, QAbstractAnimation.State _oldState)"""
        return None
    def updateCurrentTime(self):
        """int QVariantAnimation.updateCurrentTime(None self)"""
        return int()
    def event(self, _event):
        """bool QVariantAnimation.event(None self, QEvent _event)"""
        return bool()
    def setEasingCurve(self, _easing):
        """None QVariantAnimation.setEasingCurve(None self, QEasingCurve _easing)"""
        return None
    def easingCurve(self):
        """QEasingCurve QVariantAnimation.easingCurve(None self)"""
        return QEasingCurve()
    def setDuration(self, _msecs):
        """None QVariantAnimation.setDuration(None self, int _msecs)"""
        return None
    def duration(self):
        """int QVariantAnimation.duration(None self)"""
        return int()
    def currentValue(self):
        """QVariant QVariantAnimation.currentValue(None self)"""
        return QVariant()
    def setKeyValues(self, _values):
        """None QVariantAnimation.setKeyValues(None self, list-of-tuple-of-float-QVariant _values)"""
        return None
    def keyValues(self):
        """list-of-tuple-of-float-QVariant QVariantAnimation.keyValues(None self)"""
        return [tuple-of-float-QVariant()]
    def setKeyValueAt(self, _step, _value):
        """None QVariantAnimation.setKeyValueAt(None self, float _step, QVariant _value)"""
        return None
    def keyValueAt(self, _step):
        """QVariant QVariantAnimation.keyValueAt(None self, float _step)"""
        return QVariant()
    def setEndValue(self, _value):
        """None QVariantAnimation.setEndValue(None self, QVariant _value)"""
        return None
    def endValue(self):
        """QVariant QVariantAnimation.endValue(None self)"""
        return QVariant()
    def setStartValue(self, _value):
        """None QVariantAnimation.setStartValue(None self, QVariant _value)"""
        return None
    def startValue(self):
        """QVariant QVariantAnimation.startValue(None self)"""
        return QVariant()


class QPropertyAnimation(QVariantAnimation):
    """"""
    def __init__(self, _parent):
        """None QPropertyAnimation.__init__(None self, QObject _parent)"""
        return None
    def __init__(self, _target, _propertyName, _parent):
        """None QPropertyAnimation.__init__(None self, QObject _target, QByteArray _propertyName, QObject _parent)"""
        return None
    def updateState(self, _newState, _oldState):
        """None QPropertyAnimation.updateState(None self, QAbstractAnimation.State _newState, QAbstractAnimation.State _oldState)"""
        return None
    def updateCurrentValue(self, _value):
        """None QPropertyAnimation.updateCurrentValue(None self, QVariant _value)"""
        return None
    def event(self, _event):
        """bool QPropertyAnimation.event(None self, QEvent _event)"""
        return bool()
    def setPropertyName(self, _propertyName):
        """None QPropertyAnimation.setPropertyName(None self, QByteArray _propertyName)"""
        return None
    def propertyName(self):
        """QByteArray QPropertyAnimation.propertyName(None self)"""
        return QByteArray()
    def setTargetObject(self, _target):
        """None QPropertyAnimation.setTargetObject(None self, QObject _target)"""
        return None
    def targetObject(self):
        """QObject QPropertyAnimation.targetObject(None self)"""
        return QObject()


class QPluginLoader(QObject):
    """"""
    def __init__(self, _parent):
        """None QPluginLoader.__init__(None self, QObject _parent)"""
        return None
    def __init__(self, _fileName, _parent):
        """None QPluginLoader.__init__(None self, QString _fileName, QObject _parent)"""
        return None
    def loadHints(self):
        """QLibrary.LoadHints QPluginLoader.loadHints(None self)"""
        return QLibrary.LoadHints()
    def setLoadHints(self, _loadHints):
        """None QPluginLoader.setLoadHints(None self, QLibrary.LoadHints _loadHints)"""
        return None
    def errorString(self):
        """QString QPluginLoader.errorString(None self)"""
        return QString()
    def fileName(self):
        """QString QPluginLoader.fileName(None self)"""
        return QString()
    def setFileName(self, _fileName):
        """None QPluginLoader.setFileName(None self, QString _fileName)"""
        return None
    def isLoaded(self):
        """bool QPluginLoader.isLoaded(None self)"""
        return bool()
    def unload(self):
        """bool QPluginLoader.unload(None self)"""
        return bool()
    def load(self):
        """bool QPluginLoader.load(None self)"""
        return bool()
    def staticInstances(self):
        """list-of-QObject QPluginLoader.staticInstances(None self)"""
        return [QObject()]
    def instance(self):
        """QObject QPluginLoader.instance(None self)"""
        return QObject()


class QPoint():
    """"""
    def __init__(self):
        """None QPoint.__init__(None self)"""
        return None
    def __init__(self, _xpos, _ypos):
        """None QPoint.__init__(None self, int _xpos, int _ypos)"""
        return None
    def __init__(self):
        """QPoint QPoint.__init__(None self)"""
        return QPoint()
    def __eq__(self, _p2):
        """bool QPoint.__eq__(None self, QPoint _p2)"""
        return bool()
    def __ne__(self, _p2):
        """bool QPoint.__ne__(None self, QPoint _p2)"""
        return bool()
    def __add__(self, _p2):
        """QPoint QPoint.__add__(None self, QPoint _p2)"""
        return QPoint()
    def __sub__(self, _p2):
        """QPoint QPoint.__sub__(None self, QPoint _p2)"""
        return QPoint()
    def __mul__(self, _c):
        """QPoint QPoint.__mul__(None self, float _c)"""
        return QPoint()
    def __neg__(self):
        """QPoint QPoint.__neg__(None self)"""
        return QPoint()
    def __div__(self, _c):
        """QPoint QPoint.__div__(None self, float _c)"""
        return QPoint()
    def __idiv__(self, _c):
        """QPoint QPoint.__idiv__(None self, float _c)"""
        return QPoint()
    def __imul__(self, _c):
        """QPoint QPoint.__imul__(None self, float _c)"""
        return QPoint()
    def __isub__(self, _p):
        """QPoint QPoint.__isub__(None self, QPoint _p)"""
        return QPoint()
    def __iadd__(self, _p):
        """QPoint QPoint.__iadd__(None self, QPoint _p)"""
        return QPoint()
    def setY(self, _ypos):
        """None QPoint.setY(None self, int _ypos)"""
        return None
    def setX(self, _xpos):
        """None QPoint.setX(None self, int _xpos)"""
        return None
    def y(self):
        """int QPoint.y(None self)"""
        return int()
    def x(self):
        """int QPoint.x(None self)"""
        return int()
    def __bool__(self):
        """int QPoint.__bool__(None self)"""
        return int()
    def isNull(self):
        """bool QPoint.isNull(None self)"""
        return bool()
    def __repr__(self):
        """str QPoint.__repr__(None self)"""
        return str()
    def manhattanLength(self):
        """int QPoint.manhattanLength(None self)"""
        return int()


class QPointF():
    """"""
    def __init__(self):
        """None QPointF.__init__(None self)"""
        return None
    def __init__(self, _xpos, _ypos):
        """None QPointF.__init__(None self, float _xpos, float _ypos)"""
        return None
    def __init__(self, _p):
        """None QPointF.__init__(None self, QPoint _p)"""
        return None
    def __init__(self):
        """QPointF QPointF.__init__(None self)"""
        return QPointF()
    def __eq__(self, _p2):
        """bool QPointF.__eq__(None self, QPointF _p2)"""
        return bool()
    def __ne__(self, _p2):
        """bool QPointF.__ne__(None self, QPointF _p2)"""
        return bool()
    def __add__(self, _p2):
        """QPointF QPointF.__add__(None self, QPointF _p2)"""
        return QPointF()
    def __sub__(self, _p2):
        """QPointF QPointF.__sub__(None self, QPointF _p2)"""
        return QPointF()
    def __mul__(self, _c):
        """QPointF QPointF.__mul__(None self, float _c)"""
        return QPointF()
    def __neg__(self):
        """QPointF QPointF.__neg__(None self)"""
        return QPointF()
    def __div__(self, _c):
        """QPointF QPointF.__div__(None self, float _c)"""
        return QPointF()
    def manhattanLength(self):
        """float QPointF.manhattanLength(None self)"""
        return float()
    def toPoint(self):
        """QPoint QPointF.toPoint(None self)"""
        return QPoint()
    def __idiv__(self, _c):
        """QPointF QPointF.__idiv__(None self, float _c)"""
        return QPointF()
    def __imul__(self, _c):
        """QPointF QPointF.__imul__(None self, float _c)"""
        return QPointF()
    def __isub__(self, _p):
        """QPointF QPointF.__isub__(None self, QPointF _p)"""
        return QPointF()
    def __iadd__(self, _p):
        """QPointF QPointF.__iadd__(None self, QPointF _p)"""
        return QPointF()
    def setY(self, _ypos):
        """None QPointF.setY(None self, float _ypos)"""
        return None
    def setX(self, _xpos):
        """None QPointF.setX(None self, float _xpos)"""
        return None
    def y(self):
        """float QPointF.y(None self)"""
        return float()
    def x(self):
        """float QPointF.x(None self)"""
        return float()
    def __bool__(self):
        """int QPointF.__bool__(None self)"""
        return int()
    def isNull(self):
        """bool QPointF.isNull(None self)"""
        return bool()
    def __repr__(self):
        """str QPointF.__repr__(None self)"""
        return str()


class QProcess(QIODevice):
    """"""
    SeparateChannels = int() # QProcess.ProcessChannelMode enum
    MergedChannels = int() # QProcess.ProcessChannelMode enum
    ForwardedChannels = int() # QProcess.ProcessChannelMode enum

    StandardOutput = int() # QProcess.ProcessChannel enum
    StandardError = int() # QProcess.ProcessChannel enum

    NotRunning = int() # QProcess.ProcessState enum
    Starting = int() # QProcess.ProcessState enum
    Running = int() # QProcess.ProcessState enum

    FailedToStart = int() # QProcess.ProcessError enum
    Crashed = int() # QProcess.ProcessError enum
    Timedout = int() # QProcess.ProcessError enum
    ReadError = int() # QProcess.ProcessError enum
    WriteError = int() # QProcess.ProcessError enum
    UnknownError = int() # QProcess.ProcessError enum

    NormalExit = int() # QProcess.ExitStatus enum
    CrashExit = int() # QProcess.ExitStatus enum

    def __init__(self, _parent):
        """None QProcess.__init__(None self, QObject _parent)"""
        return None
    def processEnvironment(self):
        """QProcessEnvironment QProcess.processEnvironment(None self)"""
        return QProcessEnvironment()
    def setProcessEnvironment(self, _environment):
        """None QProcess.setProcessEnvironment(None self, QProcessEnvironment _environment)"""
        return None
    def writeData(self, _data):
        """int QProcess.writeData(None self, str _data)"""
        return int()
    def readData(self, _maxlen):
        """str QProcess.readData(None self, int _maxlen)"""
        return str()
    def setupChildProcess(self):
        """None QProcess.setupChildProcess(None self)"""
        return None
    def setProcessState(self, _state):
        """None QProcess.setProcessState(None self, QProcess.ProcessState _state)"""
        return None
    def kill(self):
        """None QProcess.kill(None self)"""
        return None
    def terminate(self):
        """None QProcess.terminate(None self)"""
        return None
    def setStandardOutputProcess(self, _destination):
        """None QProcess.setStandardOutputProcess(None self, QProcess _destination)"""
        return None
    def setStandardErrorFile(self, _fileName, _mode):
        """None QProcess.setStandardErrorFile(None self, QString _fileName, QIODevice.OpenMode _mode)"""
        return None
    def setStandardOutputFile(self, _fileName, _mode):
        """None QProcess.setStandardOutputFile(None self, QString _fileName, QIODevice.OpenMode _mode)"""
        return None
    def setStandardInputFile(self, _fileName):
        """None QProcess.setStandardInputFile(None self, QString _fileName)"""
        return None
    def setProcessChannelMode(self, _mode):
        """None QProcess.setProcessChannelMode(None self, QProcess.ProcessChannelMode _mode)"""
        return None
    def processChannelMode(self):
        """QProcess.ProcessChannelMode QProcess.processChannelMode(None self)"""
        return QProcess.ProcessChannelMode()
    def systemEnvironment(self):
        """QStringList QProcess.systemEnvironment(None self)"""
        return QStringList()
    def startDetached(self, _program, _arguments, _workingDirectory, _pid):
        """bool QProcess.startDetached(None self, QString _program, QStringList _arguments, QString _workingDirectory, int _pid)"""
        return bool()
    def startDetached(self, _program, _arguments):
        """bool QProcess.startDetached(None self, QString _program, QStringList _arguments)"""
        return bool()
    def startDetached(self, _program):
        """bool QProcess.startDetached(None self, QString _program)"""
        return bool()
    def execute(self, _program, _arguments):
        """int QProcess.execute(None self, QString _program, QStringList _arguments)"""
        return int()
    def execute(self, _program):
        """int QProcess.execute(None self, QString _program)"""
        return int()
    def atEnd(self):
        """bool QProcess.atEnd(None self)"""
        return bool()
    def close(self):
        """None QProcess.close(None self)"""
        return None
    def canReadLine(self):
        """bool QProcess.canReadLine(None self)"""
        return bool()
    def isSequential(self):
        """bool QProcess.isSequential(None self)"""
        return bool()
    def bytesToWrite(self):
        """int QProcess.bytesToWrite(None self)"""
        return int()
    def bytesAvailable(self):
        """int QProcess.bytesAvailable(None self)"""
        return int()
    def exitStatus(self):
        """QProcess.ExitStatus QProcess.exitStatus(None self)"""
        return QProcess.ExitStatus()
    def exitCode(self):
        """int QProcess.exitCode(None self)"""
        return int()
    def readAllStandardError(self):
        """QByteArray QProcess.readAllStandardError(None self)"""
        return QByteArray()
    def readAllStandardOutput(self):
        """QByteArray QProcess.readAllStandardOutput(None self)"""
        return QByteArray()
    def waitForFinished(self, _msecs):
        """bool QProcess.waitForFinished(None self, int _msecs)"""
        return bool()
    def waitForBytesWritten(self, _msecs):
        """bool QProcess.waitForBytesWritten(None self, int _msecs)"""
        return bool()
    def waitForReadyRead(self, _msecs):
        """bool QProcess.waitForReadyRead(None self, int _msecs)"""
        return bool()
    def waitForStarted(self, _msecs):
        """bool QProcess.waitForStarted(None self, int _msecs)"""
        return bool()
    def pid(self):
        """int QProcess.pid(None self)"""
        return int()
    def state(self):
        """QProcess.ProcessState QProcess.state(None self)"""
        return QProcess.ProcessState()
    def error(self):
        """QProcess.ProcessError QProcess.error(None self)"""
        return QProcess.ProcessError()
    def environment(self):
        """QStringList QProcess.environment(None self)"""
        return QStringList()
    def setEnvironment(self, _environment):
        """None QProcess.setEnvironment(None self, QStringList _environment)"""
        return None
    def setWorkingDirectory(self, _dir):
        """None QProcess.setWorkingDirectory(None self, QString _dir)"""
        return None
    def workingDirectory(self):
        """QString QProcess.workingDirectory(None self)"""
        return QString()
    def closeWriteChannel(self):
        """None QProcess.closeWriteChannel(None self)"""
        return None
    def closeReadChannel(self, _channel):
        """None QProcess.closeReadChannel(None self, QProcess.ProcessChannel _channel)"""
        return None
    def setReadChannel(self, _channel):
        """None QProcess.setReadChannel(None self, QProcess.ProcessChannel _channel)"""
        return None
    def readChannel(self):
        """QProcess.ProcessChannel QProcess.readChannel(None self)"""
        return QProcess.ProcessChannel()
    def setReadChannelMode(self, _mode):
        """None QProcess.setReadChannelMode(None self, QProcess.ProcessChannelMode _mode)"""
        return None
    def readChannelMode(self):
        """QProcess.ProcessChannelMode QProcess.readChannelMode(None self)"""
        return QProcess.ProcessChannelMode()
    def start(self, _program, _arguments, _mode):
        """None QProcess.start(None self, QString _program, QStringList _arguments, QIODevice.OpenMode _mode)"""
        return None
    def start(self, _program, _mode):
        """None QProcess.start(None self, QString _program, QIODevice.OpenMode _mode)"""
        return None


class QProcessEnvironment():
    """"""
    def __init__(self):
        """None QProcessEnvironment.__init__(None self)"""
        return None
    def __init__(self, _other):
        """None QProcessEnvironment.__init__(None self, QProcessEnvironment _other)"""
        return None
    def systemEnvironment(self):
        """QProcessEnvironment QProcessEnvironment.systemEnvironment(None self)"""
        return QProcessEnvironment()
    def toStringList(self):
        """QStringList QProcessEnvironment.toStringList(None self)"""
        return QStringList()
    def value(self, _name, _defaultValue):
        """QString QProcessEnvironment.value(None self, QString _name, QString _defaultValue)"""
        return QString()
    def remove(self, _name):
        """None QProcessEnvironment.remove(None self, QString _name)"""
        return None
    def insert(self, _name, _value):
        """None QProcessEnvironment.insert(None self, QString _name, QString _value)"""
        return None
    def contains(self, _name):
        """bool QProcessEnvironment.contains(None self, QString _name)"""
        return bool()
    def clear(self):
        """None QProcessEnvironment.clear(None self)"""
        return None
    def isEmpty(self):
        """bool QProcessEnvironment.isEmpty(None self)"""
        return bool()
    def __ne__(self, _other):
        """bool QProcessEnvironment.__ne__(None self, QProcessEnvironment _other)"""
        return bool()
    def __eq__(self, _other):
        """bool QProcessEnvironment.__eq__(None self, QProcessEnvironment _other)"""
        return bool()


class QReadWriteLock():
    """"""
    NonRecursive = int() # QReadWriteLock.RecursionMode enum
    Recursive = int() # QReadWriteLock.RecursionMode enum

    def __init__(self):
        """None QReadWriteLock.__init__(None self)"""
        return None
    def __init__(self, _recursionMode):
        """None QReadWriteLock.__init__(None self, QReadWriteLock.RecursionMode _recursionMode)"""
        return None
    def unlock(self):
        """None QReadWriteLock.unlock(None self)"""
        return None
    def tryLockForWrite(self):
        """bool QReadWriteLock.tryLockForWrite(None self)"""
        return bool()
    def tryLockForWrite(self, _timeout):
        """bool QReadWriteLock.tryLockForWrite(None self, int _timeout)"""
        return bool()
    def lockForWrite(self):
        """None QReadWriteLock.lockForWrite(None self)"""
        return None
    def tryLockForRead(self):
        """bool QReadWriteLock.tryLockForRead(None self)"""
        return bool()
    def tryLockForRead(self, _timeout):
        """bool QReadWriteLock.tryLockForRead(None self, int _timeout)"""
        return bool()
    def lockForRead(self):
        """None QReadWriteLock.lockForRead(None self)"""
        return None


class QReadLocker():
    """"""
    def __init__(self, _areadWriteLock):
        """None QReadLocker.__init__(None self, QReadWriteLock _areadWriteLock)"""
        return None
    def __exit__(self, _type, _value, _traceback):
        """None QReadLocker.__exit__(None self, object _type, object _value, object _traceback)"""
        return None
    def __enter__(self):
        """object QReadLocker.__enter__(None self)"""
        return object()
    def readWriteLock(self):
        """QReadWriteLock QReadLocker.readWriteLock(None self)"""
        return QReadWriteLock()
    def relock(self):
        """None QReadLocker.relock(None self)"""
        return None
    def unlock(self):
        """None QReadLocker.unlock(None self)"""
        return None


class QWriteLocker():
    """"""
    def __init__(self, _areadWriteLock):
        """None QWriteLocker.__init__(None self, QReadWriteLock _areadWriteLock)"""
        return None
    def __exit__(self, _type, _value, _traceback):
        """None QWriteLocker.__exit__(None self, object _type, object _value, object _traceback)"""
        return None
    def __enter__(self):
        """object QWriteLocker.__enter__(None self)"""
        return object()
    def readWriteLock(self):
        """QReadWriteLock QWriteLocker.readWriteLock(None self)"""
        return QReadWriteLock()
    def relock(self):
        """None QWriteLocker.relock(None self)"""
        return None
    def unlock(self):
        """None QWriteLocker.unlock(None self)"""
        return None


class QRect():
    """"""
    def __init__(self):
        """None QRect.__init__(None self)"""
        return None
    def __init__(self, _aleft, _atop, _awidth, _aheight):
        """None QRect.__init__(None self, int _aleft, int _atop, int _awidth, int _aheight)"""
        return None
    def __init__(self, _atopLeft, _abottomRight):
        """None QRect.__init__(None self, QPoint _atopLeft, QPoint _abottomRight)"""
        return None
    def __init__(self, _atopLeft, _asize):
        """None QRect.__init__(None self, QPoint _atopLeft, QSize _asize)"""
        return None
    def __init__(self):
        """QRect QRect.__init__(None self)"""
        return QRect()
    def __eq__(self, _r2):
        """bool QRect.__eq__(None self, QRect _r2)"""
        return bool()
    def __ne__(self, _r2):
        """bool QRect.__ne__(None self, QRect _r2)"""
        return bool()
    def united(self, _r):
        """QRect QRect.united(None self, QRect _r)"""
        return QRect()
    def intersected(self, _other):
        """QRect QRect.intersected(None self, QRect _other)"""
        return QRect()
    def unite(self, _r):
        """QRect QRect.unite(None self, QRect _r)"""
        return QRect()
    def intersect(self, _r):
        """QRect QRect.intersect(None self, QRect _r)"""
        return QRect()
    def __iand__(self, _r):
        """QRect QRect.__iand__(None self, QRect _r)"""
        return QRect()
    def __ior__(self, _r):
        """QRect QRect.__ior__(None self, QRect _r)"""
        return QRect()
    def setSize(self, _s):
        """None QRect.setSize(None self, QSize _s)"""
        return None
    def setHeight(self, _h):
        """None QRect.setHeight(None self, int _h)"""
        return None
    def setWidth(self, _w):
        """None QRect.setWidth(None self, int _w)"""
        return None
    def adjust(self, _dx1, _dy1, _dx2, _dy2):
        """None QRect.adjust(None self, int _dx1, int _dy1, int _dx2, int _dy2)"""
        return None
    def adjusted(self, _xp1, _yp1, _xp2, _yp2):
        """QRect QRect.adjusted(None self, int _xp1, int _yp1, int _xp2, int _yp2)"""
        return QRect()
    def setCoords(self, _xp1, _yp1, _xp2, _yp2):
        """None QRect.setCoords(None self, int _xp1, int _yp1, int _xp2, int _yp2)"""
        return None
    def getCoords(self, _xp1, _yp1, _xp2, _yp2):
        """None QRect.getCoords(None self, int _xp1, int _yp1, int _xp2, int _yp2)"""
        return None
    def setRect(self, _ax, _ay, _aw, _ah):
        """None QRect.setRect(None self, int _ax, int _ay, int _aw, int _ah)"""
        return None
    def getRect(self, _ax, _ay, _aw, _ah):
        """None QRect.getRect(None self, int _ax, int _ay, int _aw, int _ah)"""
        return None
    def moveBottomLeft(self, _p):
        """None QRect.moveBottomLeft(None self, QPoint _p)"""
        return None
    def moveTopRight(self, _p):
        """None QRect.moveTopRight(None self, QPoint _p)"""
        return None
    def moveBottomRight(self, _p):
        """None QRect.moveBottomRight(None self, QPoint _p)"""
        return None
    def moveTopLeft(self, _p):
        """None QRect.moveTopLeft(None self, QPoint _p)"""
        return None
    def moveBottom(self, _pos):
        """None QRect.moveBottom(None self, int _pos)"""
        return None
    def moveRight(self, _pos):
        """None QRect.moveRight(None self, int _pos)"""
        return None
    def moveTop(self, _pos):
        """None QRect.moveTop(None self, int _pos)"""
        return None
    def moveLeft(self, _pos):
        """None QRect.moveLeft(None self, int _pos)"""
        return None
    def moveTo(self, _ax, _ay):
        """None QRect.moveTo(None self, int _ax, int _ay)"""
        return None
    def moveTo(self, _p):
        """None QRect.moveTo(None self, QPoint _p)"""
        return None
    def translated(self, _dx, _dy):
        """QRect QRect.translated(None self, int _dx, int _dy)"""
        return QRect()
    def translated(self, _p):
        """QRect QRect.translated(None self, QPoint _p)"""
        return QRect()
    def translate(self, _dx, _dy):
        """None QRect.translate(None self, int _dx, int _dy)"""
        return None
    def translate(self, _p):
        """None QRect.translate(None self, QPoint _p)"""
        return None
    def size(self):
        """QSize QRect.size(None self)"""
        return QSize()
    def height(self):
        """int QRect.height(None self)"""
        return int()
    def width(self):
        """int QRect.width(None self)"""
        return int()
    def center(self):
        """QPoint QRect.center(None self)"""
        return QPoint()
    def bottomLeft(self):
        """QPoint QRect.bottomLeft(None self)"""
        return QPoint()
    def topRight(self):
        """QPoint QRect.topRight(None self)"""
        return QPoint()
    def bottomRight(self):
        """QPoint QRect.bottomRight(None self)"""
        return QPoint()
    def topLeft(self):
        """QPoint QRect.topLeft(None self)"""
        return QPoint()
    def setY(self, _ay):
        """None QRect.setY(None self, int _ay)"""
        return None
    def setX(self, _ax):
        """None QRect.setX(None self, int _ax)"""
        return None
    def setBottomLeft(self, _p):
        """None QRect.setBottomLeft(None self, QPoint _p)"""
        return None
    def setTopRight(self, _p):
        """None QRect.setTopRight(None self, QPoint _p)"""
        return None
    def setBottomRight(self, _p):
        """None QRect.setBottomRight(None self, QPoint _p)"""
        return None
    def setTopLeft(self, _p):
        """None QRect.setTopLeft(None self, QPoint _p)"""
        return None
    def setBottom(self, _pos):
        """None QRect.setBottom(None self, int _pos)"""
        return None
    def setRight(self, _pos):
        """None QRect.setRight(None self, int _pos)"""
        return None
    def setTop(self, _pos):
        """None QRect.setTop(None self, int _pos)"""
        return None
    def setLeft(self, _pos):
        """None QRect.setLeft(None self, int _pos)"""
        return None
    def y(self):
        """int QRect.y(None self)"""
        return int()
    def x(self):
        """int QRect.x(None self)"""
        return int()
    def bottom(self):
        """int QRect.bottom(None self)"""
        return int()
    def right(self):
        """int QRect.right(None self)"""
        return int()
    def top(self):
        """int QRect.top(None self)"""
        return int()
    def left(self):
        """int QRect.left(None self)"""
        return int()
    def __bool__(self):
        """int QRect.__bool__(None self)"""
        return int()
    def isValid(self):
        """bool QRect.isValid(None self)"""
        return bool()
    def isEmpty(self):
        """bool QRect.isEmpty(None self)"""
        return bool()
    def isNull(self):
        """bool QRect.isNull(None self)"""
        return bool()
    def __repr__(self):
        """str QRect.__repr__(None self)"""
        return str()
    def intersects(self, _r):
        """bool QRect.intersects(None self, QRect _r)"""
        return bool()
    def __contains__(self, _p):
        """int QRect.__contains__(None self, QPoint _p)"""
        return int()
    def __contains__(self, _r):
        """int QRect.__contains__(None self, QRect _r)"""
        return int()
    def contains(self, _point, _proper):
        """bool QRect.contains(None self, QPoint _point, bool _proper)"""
        return bool()
    def contains(self, _rectangle, _proper):
        """bool QRect.contains(None self, QRect _rectangle, bool _proper)"""
        return bool()
    def contains(self, _ax, _ay, _aproper):
        """bool QRect.contains(None self, int _ax, int _ay, bool _aproper)"""
        return bool()
    def contains(self, _ax, _ay):
        """bool QRect.contains(None self, int _ax, int _ay)"""
        return bool()
    def __and__(self, _r):
        """QRect QRect.__and__(None self, QRect _r)"""
        return QRect()
    def __or__(self, _r):
        """QRect QRect.__or__(None self, QRect _r)"""
        return QRect()
    def moveCenter(self, _p):
        """None QRect.moveCenter(None self, QPoint _p)"""
        return None
    def normalized(self):
        """QRect QRect.normalized(None self)"""
        return QRect()


class QRectF():
    """"""
    def __init__(self):
        """None QRectF.__init__(None self)"""
        return None
    def __init__(self, _atopLeft, _asize):
        """None QRectF.__init__(None self, QPointF _atopLeft, QSizeF _asize)"""
        return None
    def __init__(self, _atopLeft, _abottomRight):
        """None QRectF.__init__(None self, QPointF _atopLeft, QPointF _abottomRight)"""
        return None
    def __init__(self, _aleft, _atop, _awidth, _aheight):
        """None QRectF.__init__(None self, float _aleft, float _atop, float _awidth, float _aheight)"""
        return None
    def __init__(self, _r):
        """None QRectF.__init__(None self, QRect _r)"""
        return None
    def __init__(self):
        """QRectF QRectF.__init__(None self)"""
        return QRectF()
    def __eq__(self, _r2):
        """bool QRectF.__eq__(None self, QRectF _r2)"""
        return bool()
    def __ne__(self, _r2):
        """bool QRectF.__ne__(None self, QRectF _r2)"""
        return bool()
    def united(self, _r):
        """QRectF QRectF.united(None self, QRectF _r)"""
        return QRectF()
    def intersected(self, _r):
        """QRectF QRectF.intersected(None self, QRectF _r)"""
        return QRectF()
    def toRect(self):
        """QRect QRectF.toRect(None self)"""
        return QRect()
    def toAlignedRect(self):
        """QRect QRectF.toAlignedRect(None self)"""
        return QRect()
    def unite(self, _r):
        """QRectF QRectF.unite(None self, QRectF _r)"""
        return QRectF()
    def intersect(self, _r):
        """QRectF QRectF.intersect(None self, QRectF _r)"""
        return QRectF()
    def __iand__(self, _r):
        """QRectF QRectF.__iand__(None self, QRectF _r)"""
        return QRectF()
    def __ior__(self, _r):
        """QRectF QRectF.__ior__(None self, QRectF _r)"""
        return QRectF()
    def setSize(self, _s):
        """None QRectF.setSize(None self, QSizeF _s)"""
        return None
    def setHeight(self, _ah):
        """None QRectF.setHeight(None self, float _ah)"""
        return None
    def setWidth(self, _aw):
        """None QRectF.setWidth(None self, float _aw)"""
        return None
    def adjusted(self, _xp1, _yp1, _xp2, _yp2):
        """QRectF QRectF.adjusted(None self, float _xp1, float _yp1, float _xp2, float _yp2)"""
        return QRectF()
    def adjust(self, _xp1, _yp1, _xp2, _yp2):
        """None QRectF.adjust(None self, float _xp1, float _yp1, float _xp2, float _yp2)"""
        return None
    def setCoords(self, _xp1, _yp1, _xp2, _yp2):
        """None QRectF.setCoords(None self, float _xp1, float _yp1, float _xp2, float _yp2)"""
        return None
    def getCoords(self, _xp1, _yp1, _xp2, _yp2):
        """None QRectF.getCoords(None self, float _xp1, float _yp1, float _xp2, float _yp2)"""
        return None
    def setRect(self, _ax, _ay, _aaw, _aah):
        """None QRectF.setRect(None self, float _ax, float _ay, float _aaw, float _aah)"""
        return None
    def getRect(self, _ax, _ay, _aaw, _aah):
        """None QRectF.getRect(None self, float _ax, float _ay, float _aaw, float _aah)"""
        return None
    def translated(self, _dx, _dy):
        """QRectF QRectF.translated(None self, float _dx, float _dy)"""
        return QRectF()
    def translated(self, _p):
        """QRectF QRectF.translated(None self, QPointF _p)"""
        return QRectF()
    def moveTo(self, _ax, _ay):
        """None QRectF.moveTo(None self, float _ax, float _ay)"""
        return None
    def moveTo(self, _p):
        """None QRectF.moveTo(None self, QPointF _p)"""
        return None
    def translate(self, _dx, _dy):
        """None QRectF.translate(None self, float _dx, float _dy)"""
        return None
    def translate(self, _p):
        """None QRectF.translate(None self, QPointF _p)"""
        return None
    def size(self):
        """QSizeF QRectF.size(None self)"""
        return QSizeF()
    def height(self):
        """float QRectF.height(None self)"""
        return float()
    def width(self):
        """float QRectF.width(None self)"""
        return float()
    def moveCenter(self, _p):
        """None QRectF.moveCenter(None self, QPointF _p)"""
        return None
    def moveBottomRight(self, _p):
        """None QRectF.moveBottomRight(None self, QPointF _p)"""
        return None
    def moveBottomLeft(self, _p):
        """None QRectF.moveBottomLeft(None self, QPointF _p)"""
        return None
    def moveTopRight(self, _p):
        """None QRectF.moveTopRight(None self, QPointF _p)"""
        return None
    def moveTopLeft(self, _p):
        """None QRectF.moveTopLeft(None self, QPointF _p)"""
        return None
    def moveBottom(self, _pos):
        """None QRectF.moveBottom(None self, float _pos)"""
        return None
    def moveRight(self, _pos):
        """None QRectF.moveRight(None self, float _pos)"""
        return None
    def moveTop(self, _pos):
        """None QRectF.moveTop(None self, float _pos)"""
        return None
    def moveLeft(self, _pos):
        """None QRectF.moveLeft(None self, float _pos)"""
        return None
    def center(self):
        """QPointF QRectF.center(None self)"""
        return QPointF()
    def setBottomRight(self, _p):
        """None QRectF.setBottomRight(None self, QPointF _p)"""
        return None
    def setBottomLeft(self, _p):
        """None QRectF.setBottomLeft(None self, QPointF _p)"""
        return None
    def setTopRight(self, _p):
        """None QRectF.setTopRight(None self, QPointF _p)"""
        return None
    def setTopLeft(self, _p):
        """None QRectF.setTopLeft(None self, QPointF _p)"""
        return None
    def setBottom(self, _pos):
        """None QRectF.setBottom(None self, float _pos)"""
        return None
    def setTop(self, _pos):
        """None QRectF.setTop(None self, float _pos)"""
        return None
    def setRight(self, _pos):
        """None QRectF.setRight(None self, float _pos)"""
        return None
    def setLeft(self, _pos):
        """None QRectF.setLeft(None self, float _pos)"""
        return None
    def y(self):
        """float QRectF.y(None self)"""
        return float()
    def x(self):
        """float QRectF.x(None self)"""
        return float()
    def __bool__(self):
        """int QRectF.__bool__(None self)"""
        return int()
    def isValid(self):
        """bool QRectF.isValid(None self)"""
        return bool()
    def isEmpty(self):
        """bool QRectF.isEmpty(None self)"""
        return bool()
    def isNull(self):
        """bool QRectF.isNull(None self)"""
        return bool()
    def intersects(self, _r):
        """bool QRectF.intersects(None self, QRectF _r)"""
        return bool()
    def __contains__(self, _p):
        """int QRectF.__contains__(None self, QPointF _p)"""
        return int()
    def __contains__(self, _r):
        """int QRectF.__contains__(None self, QRectF _r)"""
        return int()
    def contains(self, _p):
        """bool QRectF.contains(None self, QPointF _p)"""
        return bool()
    def contains(self, _r):
        """bool QRectF.contains(None self, QRectF _r)"""
        return bool()
    def contains(self, _ax, _ay):
        """bool QRectF.contains(None self, float _ax, float _ay)"""
        return bool()
    def __and__(self, _r):
        """QRectF QRectF.__and__(None self, QRectF _r)"""
        return QRectF()
    def __or__(self, _r):
        """QRectF QRectF.__or__(None self, QRectF _r)"""
        return QRectF()
    def bottomLeft(self):
        """QPointF QRectF.bottomLeft(None self)"""
        return QPointF()
    def topRight(self):
        """QPointF QRectF.topRight(None self)"""
        return QPointF()
    def bottomRight(self):
        """QPointF QRectF.bottomRight(None self)"""
        return QPointF()
    def topLeft(self):
        """QPointF QRectF.topLeft(None self)"""
        return QPointF()
    def setY(self, _pos):
        """None QRectF.setY(None self, float _pos)"""
        return None
    def setX(self, _pos):
        """None QRectF.setX(None self, float _pos)"""
        return None
    def bottom(self):
        """float QRectF.bottom(None self)"""
        return float()
    def right(self):
        """float QRectF.right(None self)"""
        return float()
    def top(self):
        """float QRectF.top(None self)"""
        return float()
    def left(self):
        """float QRectF.left(None self)"""
        return float()
    def normalized(self):
        """QRectF QRectF.normalized(None self)"""
        return QRectF()
    def __repr__(self):
        """str QRectF.__repr__(None self)"""
        return str()


class QRegExp():
    """"""
    CaretAtZero = int() # QRegExp.CaretMode enum
    CaretAtOffset = int() # QRegExp.CaretMode enum
    CaretWontMatch = int() # QRegExp.CaretMode enum

    RegExp = int() # QRegExp.PatternSyntax enum
    RegExp2 = int() # QRegExp.PatternSyntax enum
    Wildcard = int() # QRegExp.PatternSyntax enum
    FixedString = int() # QRegExp.PatternSyntax enum
    WildcardUnix = int() # QRegExp.PatternSyntax enum
    W3CXmlSchema11 = int() # QRegExp.PatternSyntax enum

    def __init__(self):
        """None QRegExp.__init__(None self)"""
        return None
    def __init__(self, _pattern, _cs, _syntax):
        """None QRegExp.__init__(None self, QString _pattern, Qt.CaseSensitivity _cs, QRegExp.PatternSyntax _syntax)"""
        return None
    def __init__(self, _rx):
        """None QRegExp.__init__(None self, QRegExp _rx)"""
        return None
    def captureCount(self):
        """int QRegExp.captureCount(None self)"""
        return int()
    def escape(self, _str):
        """QString QRegExp.escape(None self, QString _str)"""
        return QString()
    def errorString(self):
        """QString QRegExp.errorString(None self)"""
        return QString()
    def pos(self, _nth):
        """int QRegExp.pos(None self, int _nth)"""
        return int()
    def cap(self, _nth):
        """QString QRegExp.cap(None self, int _nth)"""
        return QString()
    def capturedTexts(self):
        """QStringList QRegExp.capturedTexts(None self)"""
        return QStringList()
    def numCaptures(self):
        """int QRegExp.numCaptures(None self)"""
        return int()
    def matchedLength(self):
        """int QRegExp.matchedLength(None self)"""
        return int()
    def lastIndexIn(self, _str, _offset, _caretMode):
        """int QRegExp.lastIndexIn(None self, QString _str, int _offset, QRegExp.CaretMode _caretMode)"""
        return int()
    def indexIn(self, _str, _offset, _caretMode):
        """int QRegExp.indexIn(None self, QString _str, int _offset, QRegExp.CaretMode _caretMode)"""
        return int()
    def exactMatch(self, _str):
        """bool QRegExp.exactMatch(None self, QString _str)"""
        return bool()
    def setMinimal(self, _minimal):
        """None QRegExp.setMinimal(None self, bool _minimal)"""
        return None
    def isMinimal(self):
        """bool QRegExp.isMinimal(None self)"""
        return bool()
    def setPatternSyntax(self, _syntax):
        """None QRegExp.setPatternSyntax(None self, QRegExp.PatternSyntax _syntax)"""
        return None
    def patternSyntax(self):
        """QRegExp.PatternSyntax QRegExp.patternSyntax(None self)"""
        return QRegExp.PatternSyntax()
    def setCaseSensitivity(self, _cs):
        """None QRegExp.setCaseSensitivity(None self, Qt.CaseSensitivity _cs)"""
        return None
    def caseSensitivity(self):
        """Qt.CaseSensitivity QRegExp.caseSensitivity(None self)"""
        return Qt.CaseSensitivity()
    def setPattern(self, _pattern):
        """None QRegExp.setPattern(None self, QString _pattern)"""
        return None
    def pattern(self):
        """QString QRegExp.pattern(None self)"""
        return QString()
    def isValid(self):
        """bool QRegExp.isValid(None self)"""
        return bool()
    def isEmpty(self):
        """bool QRegExp.isEmpty(None self)"""
        return bool()
    def __ne__(self, _rx):
        """bool QRegExp.__ne__(None self, QRegExp _rx)"""
        return bool()
    def __eq__(self, _rx):
        """bool QRegExp.__eq__(None self, QRegExp _rx)"""
        return bool()
    def __repr__(self):
        """str QRegExp.__repr__(None self)"""
        return str()


class QResource():
    """"""
    def __init__(self, _fileName, _locale):
        """None QResource.__init__(None self, QString _fileName, QLocale _locale)"""
        return None
    def isFile(self):
        """bool QResource.isFile(None self)"""
        return bool()
    def isDir(self):
        """bool QResource.isDir(None self)"""
        return bool()
    def children(self):
        """QStringList QResource.children(None self)"""
        return QStringList()
    def unregisterResourceData(self, _rccData, _mapRoot):
        """bool QResource.unregisterResourceData(None self, str _rccData, QString _mapRoot)"""
        return bool()
    def unregisterResource(self, _rccFileName, _mapRoot):
        """bool QResource.unregisterResource(None self, QString _rccFileName, QString _mapRoot)"""
        return bool()
    def searchPaths(self):
        """QStringList QResource.searchPaths(None self)"""
        return QStringList()
    def registerResourceData(self, _rccData, _mapRoot):
        """bool QResource.registerResourceData(None self, str _rccData, QString _mapRoot)"""
        return bool()
    def registerResource(self, _rccFileName, _mapRoot):
        """bool QResource.registerResource(None self, QString _rccFileName, QString _mapRoot)"""
        return bool()
    def addSearchPath(self, _path):
        """None QResource.addSearchPath(None self, QString _path)"""
        return None
    def size(self):
        """int QResource.size(None self)"""
        return int()
    def setLocale(self, _locale):
        """None QResource.setLocale(None self, QLocale _locale)"""
        return None
    def setFileName(self, _file):
        """None QResource.setFileName(None self, QString _file)"""
        return None
    def locale(self):
        """QLocale QResource.locale(None self)"""
        return QLocale()
    def isValid(self):
        """bool QResource.isValid(None self)"""
        return bool()
    def isCompressed(self):
        """bool QResource.isCompressed(None self)"""
        return bool()
    def fileName(self):
        """QString QResource.fileName(None self)"""
        return QString()
    def data(self):
        """str QResource.data(None self)"""
        return str()
    def absoluteFilePath(self):
        """QString QResource.absoluteFilePath(None self)"""
        return QString()


class QRunnable():
    """"""
    def __init__(self):
        """None QRunnable.__init__(None self)"""
        return None
    def __init__(self):
        """QRunnable QRunnable.__init__(None self)"""
        return QRunnable()
    def setAutoDelete(self, __autoDelete):
        """None QRunnable.setAutoDelete(None self, bool __autoDelete)"""
        return None
    def autoDelete(self):
        """bool QRunnable.autoDelete(None self)"""
        return bool()
    def run(self):
        """abstract None QRunnable.run(None self)"""
        return None


class QSemaphore():
    """"""
    def __init__(self, _n):
        """None QSemaphore.__init__(None self, int _n)"""
        return None
    def available(self):
        """int QSemaphore.available(None self)"""
        return int()
    def release(self, _n):
        """None QSemaphore.release(None self, int _n)"""
        return None
    def tryAcquire(self, _n):
        """bool QSemaphore.tryAcquire(None self, int _n)"""
        return bool()
    def tryAcquire(self, _n, _timeout):
        """bool QSemaphore.tryAcquire(None self, int _n, int _timeout)"""
        return bool()
    def acquire(self, _n):
        """None QSemaphore.acquire(None self, int _n)"""
        return None


class QSequentialAnimationGroup(QAnimationGroup):
    """"""
    def __init__(self, _parent):
        """None QSequentialAnimationGroup.__init__(None self, QObject _parent)"""
        return None
    def updateDirection(self, _direction):
        """None QSequentialAnimationGroup.updateDirection(None self, QAbstractAnimation.Direction _direction)"""
        return None
    def updateState(self, _newState, _oldState):
        """None QSequentialAnimationGroup.updateState(None self, QAbstractAnimation.State _newState, QAbstractAnimation.State _oldState)"""
        return None
    def updateCurrentTime(self):
        """int QSequentialAnimationGroup.updateCurrentTime(None self)"""
        return int()
    def event(self, _event):
        """bool QSequentialAnimationGroup.event(None self, QEvent _event)"""
        return bool()
    def duration(self):
        """int QSequentialAnimationGroup.duration(None self)"""
        return int()
    def currentAnimation(self):
        """QAbstractAnimation QSequentialAnimationGroup.currentAnimation(None self)"""
        return QAbstractAnimation()
    def insertPause(self, _index, _msecs):
        """QPauseAnimation QSequentialAnimationGroup.insertPause(None self, int _index, int _msecs)"""
        return QPauseAnimation()
    def addPause(self, _msecs):
        """QPauseAnimation QSequentialAnimationGroup.addPause(None self, int _msecs)"""
        return QPauseAnimation()


class QSettings(QObject):
    """"""
    UserScope = int() # QSettings.Scope enum
    SystemScope = int() # QSettings.Scope enum

    NativeFormat = int() # QSettings.Format enum
    IniFormat = int() # QSettings.Format enum
    InvalidFormat = int() # QSettings.Format enum

    NoError = int() # QSettings.Status enum
    AccessError = int() # QSettings.Status enum
    FormatError = int() # QSettings.Status enum

    def __init__(self, _organization, _application, _parent):
        """None QSettings.__init__(None self, QString _organization, QString _application, QObject _parent)"""
        return None
    def __init__(self, _scope, _organization, _application, _parent):
        """None QSettings.__init__(None self, QSettings.Scope _scope, QString _organization, QString _application, QObject _parent)"""
        return None
    def __init__(self, _format, _scope, _organization, _application, _parent):
        """None QSettings.__init__(None self, QSettings.Format _format, QSettings.Scope _scope, QString _organization, QString _application, QObject _parent)"""
        return None
    def __init__(self, _fileName, _format, _parent):
        """None QSettings.__init__(None self, QString _fileName, QSettings.Format _format, QObject _parent)"""
        return None
    def __init__(self, _parent):
        """None QSettings.__init__(None self, QObject _parent)"""
        return None
    def event(self, _event):
        """bool QSettings.event(None self, QEvent _event)"""
        return bool()
    def iniCodec(self):
        """QTextCodec QSettings.iniCodec(None self)"""
        return QTextCodec()
    def setIniCodec(self, _codec):
        """None QSettings.setIniCodec(None self, QTextCodec _codec)"""
        return None
    def setIniCodec(self, _codecName):
        """None QSettings.setIniCodec(None self, str _codecName)"""
        return None
    def defaultFormat(self):
        """QSettings.Format QSettings.defaultFormat(None self)"""
        return QSettings.Format()
    def setDefaultFormat(self, _format):
        """None QSettings.setDefaultFormat(None self, QSettings.Format _format)"""
        return None
    def applicationName(self):
        """QString QSettings.applicationName(None self)"""
        return QString()
    def organizationName(self):
        """QString QSettings.organizationName(None self)"""
        return QString()
    def scope(self):
        """QSettings.Scope QSettings.scope(None self)"""
        return QSettings.Scope()
    def format(self):
        """QSettings.Format QSettings.format(None self)"""
        return QSettings.Format()
    def setPath(self, _format, _scope, _path):
        """None QSettings.setPath(None self, QSettings.Format _format, QSettings.Scope _scope, QString _path)"""
        return None
    def setUserIniPath(self, _dir):
        """None QSettings.setUserIniPath(None self, QString _dir)"""
        return None
    def setSystemIniPath(self, _dir):
        """None QSettings.setSystemIniPath(None self, QString _dir)"""
        return None
    def fileName(self):
        """QString QSettings.fileName(None self)"""
        return QString()
    def fallbacksEnabled(self):
        """bool QSettings.fallbacksEnabled(None self)"""
        return bool()
    def setFallbacksEnabled(self, _b):
        """None QSettings.setFallbacksEnabled(None self, bool _b)"""
        return None
    def contains(self, _key):
        """bool QSettings.contains(None self, QString _key)"""
        return bool()
    def remove(self, _key):
        """None QSettings.remove(None self, QString _key)"""
        return None
    def value(self, _key, _defaultValue, _type):
        """object QSettings.value(None self, QString _key, QVariant _defaultValue, object _type)"""
        return object()
    def setValue(self, _key, _value):
        """None QSettings.setValue(None self, QString _key, QVariant _value)"""
        return None
    def isWritable(self):
        """bool QSettings.isWritable(None self)"""
        return bool()
    def childGroups(self):
        """QStringList QSettings.childGroups(None self)"""
        return QStringList()
    def childKeys(self):
        """QStringList QSettings.childKeys(None self)"""
        return QStringList()
    def allKeys(self):
        """QStringList QSettings.allKeys(None self)"""
        return QStringList()
    def setArrayIndex(self, _i):
        """None QSettings.setArrayIndex(None self, int _i)"""
        return None
    def endArray(self):
        """None QSettings.endArray(None self)"""
        return None
    def beginWriteArray(self, _prefix, _size):
        """None QSettings.beginWriteArray(None self, QString _prefix, int _size)"""
        return None
    def beginReadArray(self, _prefix):
        """int QSettings.beginReadArray(None self, QString _prefix)"""
        return int()
    def group(self):
        """QString QSettings.group(None self)"""
        return QString()
    def endGroup(self):
        """None QSettings.endGroup(None self)"""
        return None
    def beginGroup(self, _prefix):
        """None QSettings.beginGroup(None self, QString _prefix)"""
        return None
    def status(self):
        """QSettings.Status QSettings.status(None self)"""
        return QSettings.Status()
    def sync(self):
        """None QSettings.sync(None self)"""
        return None
    def clear(self):
        """None QSettings.clear(None self)"""
        return None


class QSharedMemory(QObject):
    """"""
    NoError = int() # QSharedMemory.SharedMemoryError enum
    PermissionDenied = int() # QSharedMemory.SharedMemoryError enum
    InvalidSize = int() # QSharedMemory.SharedMemoryError enum
    KeyError = int() # QSharedMemory.SharedMemoryError enum
    AlreadyExists = int() # QSharedMemory.SharedMemoryError enum
    NotFound = int() # QSharedMemory.SharedMemoryError enum
    LockError = int() # QSharedMemory.SharedMemoryError enum
    OutOfResources = int() # QSharedMemory.SharedMemoryError enum
    UnknownError = int() # QSharedMemory.SharedMemoryError enum

    ReadOnly = int() # QSharedMemory.AccessMode enum
    ReadWrite = int() # QSharedMemory.AccessMode enum

    def __init__(self, _parent):
        """None QSharedMemory.__init__(None self, QObject _parent)"""
        return None
    def __init__(self, _key, _parent):
        """None QSharedMemory.__init__(None self, QString _key, QObject _parent)"""
        return None
    def errorString(self):
        """QString QSharedMemory.errorString(None self)"""
        return QString()
    def error(self):
        """QSharedMemory.SharedMemoryError QSharedMemory.error(None self)"""
        return QSharedMemory.SharedMemoryError()
    def unlock(self):
        """bool QSharedMemory.unlock(None self)"""
        return bool()
    def lock(self):
        """bool QSharedMemory.lock(None self)"""
        return bool()
    def constData(self):
        """sip.voidptr QSharedMemory.constData(None self)"""
        return sip.voidptr()
    def data(self):
        """sip.voidptr QSharedMemory.data(None self)"""
        return sip.voidptr()
    def detach(self):
        """bool QSharedMemory.detach(None self)"""
        return bool()
    def isAttached(self):
        """bool QSharedMemory.isAttached(None self)"""
        return bool()
    def attach(self, _mode):
        """bool QSharedMemory.attach(None self, QSharedMemory.AccessMode _mode)"""
        return bool()
    def size(self):
        """int QSharedMemory.size(None self)"""
        return int()
    def create(self, _size, _mode):
        """bool QSharedMemory.create(None self, int _size, QSharedMemory.AccessMode _mode)"""
        return bool()
    def key(self):
        """QString QSharedMemory.key(None self)"""
        return QString()
    def setKey(self, _key):
        """None QSharedMemory.setKey(None self, QString _key)"""
        return None


class QSignalMapper(QObject):
    """"""
    def __init__(self, _parent):
        """None QSignalMapper.__init__(None self, QObject _parent)"""
        return None
    def map(self):
        """None QSignalMapper.map(None self)"""
        return None
    def map(self, _sender):
        """None QSignalMapper.map(None self, QObject _sender)"""
        return None
    def mapping(self, _id):
        """QObject QSignalMapper.mapping(None self, int _id)"""
        return QObject()
    def mapping(self, _text):
        """QObject QSignalMapper.mapping(None self, QString _text)"""
        return QObject()
    def mapping(self, _widget):
        """QObject QSignalMapper.mapping(None self, QWidget _widget)"""
        return QObject()
    def mapping(self, _object):
        """QObject QSignalMapper.mapping(None self, QObject _object)"""
        return QObject()
    def removeMappings(self, _sender):
        """None QSignalMapper.removeMappings(None self, QObject _sender)"""
        return None
    def setMapping(self, _sender, _id):
        """None QSignalMapper.setMapping(None self, QObject _sender, int _id)"""
        return None
    def setMapping(self, _sender, _text):
        """None QSignalMapper.setMapping(None self, QObject _sender, QString _text)"""
        return None
    def setMapping(self, _sender, _widget):
        """None QSignalMapper.setMapping(None self, QObject _sender, QWidget _widget)"""
        return None
    def setMapping(self, _sender, _object):
        """None QSignalMapper.setMapping(None self, QObject _sender, QObject _object)"""
        return None


class QSignalTransition(QAbstractTransition):
    """"""
    def __init__(self, _sourceState):
        """None QSignalTransition.__init__(None self, QState _sourceState)"""
        return None
    def __init__(self, _sender, _signal, _sourceState):
        """None QSignalTransition.__init__(None self, QObject _sender, SIGNAL() _signal, QState _sourceState)"""
        return None
    def __init__(self, _signal, _sourceState):
        """None QSignalTransition.__init__(None self, signal _signal, QState _sourceState)"""
        return None
    def event(self, _e):
        """bool QSignalTransition.event(None self, QEvent _e)"""
        return bool()
    def onTransition(self, _event):
        """None QSignalTransition.onTransition(None self, QEvent _event)"""
        return None
    def eventTest(self, _event):
        """bool QSignalTransition.eventTest(None self, QEvent _event)"""
        return bool()
    def setSignal(self, _signal):
        """None QSignalTransition.setSignal(None self, QByteArray _signal)"""
        return None
    def signal(self):
        """QByteArray QSignalTransition.signal(None self)"""
        return QByteArray()
    def setSenderObject(self, _sender):
        """None QSignalTransition.setSenderObject(None self, QObject _sender)"""
        return None
    def senderObject(self):
        """QObject QSignalTransition.senderObject(None self)"""
        return QObject()


class QSize():
    """"""
    def __init__(self):
        """None QSize.__init__(None self)"""
        return None
    def __init__(self, _w, _h):
        """None QSize.__init__(None self, int _w, int _h)"""
        return None
    def __init__(self):
        """QSize QSize.__init__(None self)"""
        return QSize()
    def __eq__(self, _s2):
        """bool QSize.__eq__(None self, QSize _s2)"""
        return bool()
    def __ne__(self, _s2):
        """bool QSize.__ne__(None self, QSize _s2)"""
        return bool()
    def __add__(self, _s2):
        """QSize QSize.__add__(None self, QSize _s2)"""
        return QSize()
    def __sub__(self, _s2):
        """QSize QSize.__sub__(None self, QSize _s2)"""
        return QSize()
    def __mul__(self, _c):
        """QSize QSize.__mul__(None self, float _c)"""
        return QSize()
    def __mul__(self, _s):
        """QSize QSize.__mul__(None self, QSize _s)"""
        return QSize()
    def __div__(self, _c):
        """QSize QSize.__div__(None self, float _c)"""
        return QSize()
    def boundedTo(self, _otherSize):
        """QSize QSize.boundedTo(None self, QSize _otherSize)"""
        return QSize()
    def expandedTo(self, _otherSize):
        """QSize QSize.expandedTo(None self, QSize _otherSize)"""
        return QSize()
    def __idiv__(self, _c):
        """QSize QSize.__idiv__(None self, float _c)"""
        return QSize()
    def __imul__(self, _c):
        """QSize QSize.__imul__(None self, float _c)"""
        return QSize()
    def __isub__(self, _s):
        """QSize QSize.__isub__(None self, QSize _s)"""
        return QSize()
    def __iadd__(self, _s):
        """QSize QSize.__iadd__(None self, QSize _s)"""
        return QSize()
    def setHeight(self, _h):
        """None QSize.setHeight(None self, int _h)"""
        return None
    def setWidth(self, _w):
        """None QSize.setWidth(None self, int _w)"""
        return None
    def height(self):
        """int QSize.height(None self)"""
        return int()
    def width(self):
        """int QSize.width(None self)"""
        return int()
    def __bool__(self):
        """int QSize.__bool__(None self)"""
        return int()
    def isValid(self):
        """bool QSize.isValid(None self)"""
        return bool()
    def isEmpty(self):
        """bool QSize.isEmpty(None self)"""
        return bool()
    def isNull(self):
        """bool QSize.isNull(None self)"""
        return bool()
    def __repr__(self):
        """str QSize.__repr__(None self)"""
        return str()
    def scale(self, _s, _mode):
        """None QSize.scale(None self, QSize _s, Qt.AspectRatioMode _mode)"""
        return None
    def scale(self, _w, _h, _mode):
        """None QSize.scale(None self, int _w, int _h, Qt.AspectRatioMode _mode)"""
        return None
    def transpose(self):
        """None QSize.transpose(None self)"""
        return None


class QSizeF():
    """"""
    def __init__(self):
        """None QSizeF.__init__(None self)"""
        return None
    def __init__(self, _sz):
        """None QSizeF.__init__(None self, QSize _sz)"""
        return None
    def __init__(self, _w, _h):
        """None QSizeF.__init__(None self, float _w, float _h)"""
        return None
    def __init__(self):
        """QSizeF QSizeF.__init__(None self)"""
        return QSizeF()
    def __eq__(self, _s2):
        """bool QSizeF.__eq__(None self, QSizeF _s2)"""
        return bool()
    def __ne__(self, _s2):
        """bool QSizeF.__ne__(None self, QSizeF _s2)"""
        return bool()
    def __add__(self, _s2):
        """QSizeF QSizeF.__add__(None self, QSizeF _s2)"""
        return QSizeF()
    def __sub__(self, _s2):
        """QSizeF QSizeF.__sub__(None self, QSizeF _s2)"""
        return QSizeF()
    def __mul__(self, _c):
        """QSizeF QSizeF.__mul__(None self, float _c)"""
        return QSizeF()
    def __mul__(self, _s):
        """QSizeF QSizeF.__mul__(None self, QSizeF _s)"""
        return QSizeF()
    def __div__(self, _c):
        """QSizeF QSizeF.__div__(None self, float _c)"""
        return QSizeF()
    def toSize(self):
        """QSize QSizeF.toSize(None self)"""
        return QSize()
    def boundedTo(self, _otherSize):
        """QSizeF QSizeF.boundedTo(None self, QSizeF _otherSize)"""
        return QSizeF()
    def expandedTo(self, _otherSize):
        """QSizeF QSizeF.expandedTo(None self, QSizeF _otherSize)"""
        return QSizeF()
    def __idiv__(self, _c):
        """QSizeF QSizeF.__idiv__(None self, float _c)"""
        return QSizeF()
    def __imul__(self, _c):
        """QSizeF QSizeF.__imul__(None self, float _c)"""
        return QSizeF()
    def __isub__(self, _s):
        """QSizeF QSizeF.__isub__(None self, QSizeF _s)"""
        return QSizeF()
    def __iadd__(self, _s):
        """QSizeF QSizeF.__iadd__(None self, QSizeF _s)"""
        return QSizeF()
    def setHeight(self, _h):
        """None QSizeF.setHeight(None self, float _h)"""
        return None
    def setWidth(self, _w):
        """None QSizeF.setWidth(None self, float _w)"""
        return None
    def height(self):
        """float QSizeF.height(None self)"""
        return float()
    def width(self):
        """float QSizeF.width(None self)"""
        return float()
    def __bool__(self):
        """int QSizeF.__bool__(None self)"""
        return int()
    def isValid(self):
        """bool QSizeF.isValid(None self)"""
        return bool()
    def isEmpty(self):
        """bool QSizeF.isEmpty(None self)"""
        return bool()
    def isNull(self):
        """bool QSizeF.isNull(None self)"""
        return bool()
    def __repr__(self):
        """str QSizeF.__repr__(None self)"""
        return str()
    def scale(self, _s, _mode):
        """None QSizeF.scale(None self, QSizeF _s, Qt.AspectRatioMode _mode)"""
        return None
    def scale(self, _w, _h, _mode):
        """None QSizeF.scale(None self, float _w, float _h, Qt.AspectRatioMode _mode)"""
        return None
    def transpose(self):
        """None QSizeF.transpose(None self)"""
        return None


class QSocketNotifier(QObject):
    """"""
    Read = int() # QSocketNotifier.Type enum
    Write = int() # QSocketNotifier.Type enum
    Exception = int() # QSocketNotifier.Type enum

    def __init__(self, _socket, _type, _parent):
        """None QSocketNotifier.__init__(None self, int _socket, QSocketNotifier.Type _type, QObject _parent)"""
        return None
    def event(self):
        """QEvent QSocketNotifier.event(None self)"""
        return QEvent()
    def setEnabled(self):
        """bool QSocketNotifier.setEnabled(None self)"""
        return bool()
    def isEnabled(self):
        """bool QSocketNotifier.isEnabled(None self)"""
        return bool()
    def type(self):
        """QSocketNotifier.Type QSocketNotifier.type(None self)"""
        return QSocketNotifier.Type()
    def socket(self):
        """int QSocketNotifier.socket(None self)"""
        return int()


class QState(QAbstractState):
    """"""
    ExclusiveStates = int() # QState.ChildMode enum
    ParallelStates = int() # QState.ChildMode enum

    def __init__(self, _parent):
        """None QState.__init__(None self, QState _parent)"""
        return None
    def __init__(self, _childMode, _parent):
        """None QState.__init__(None self, QState.ChildMode _childMode, QState _parent)"""
        return None
    def event(self, _e):
        """bool QState.event(None self, QEvent _e)"""
        return bool()
    def onExit(self, _event):
        """None QState.onExit(None self, QEvent _event)"""
        return None
    def onEntry(self, _event):
        """None QState.onEntry(None self, QEvent _event)"""
        return None
    def assignProperty(self, _object, _name, _value):
        """None QState.assignProperty(None self, QObject _object, str _name, QVariant _value)"""
        return None
    def setChildMode(self, _mode):
        """None QState.setChildMode(None self, QState.ChildMode _mode)"""
        return None
    def childMode(self):
        """QState.ChildMode QState.childMode(None self)"""
        return QState.ChildMode()
    def setInitialState(self, _state):
        """None QState.setInitialState(None self, QAbstractState _state)"""
        return None
    def initialState(self):
        """QAbstractState QState.initialState(None self)"""
        return QAbstractState()
    def transitions(self):
        """list-of-QAbstractTransition QState.transitions(None self)"""
        return [QAbstractTransition()]
    def removeTransition(self, _transition):
        """None QState.removeTransition(None self, QAbstractTransition _transition)"""
        return None
    def addTransition(self, _transition):
        """None QState.addTransition(None self, QAbstractTransition _transition)"""
        return None
    def addTransition(self, _sender, _signal, _target):
        """QSignalTransition QState.addTransition(None self, QObject _sender, SIGNAL() _signal, QAbstractState _target)"""
        return QSignalTransition()
    def addTransition(self, _signal, _target):
        """QSignalTransition QState.addTransition(None self, signal _signal, QAbstractState _target)"""
        return QSignalTransition()
    def addTransition(self, _target):
        """QAbstractTransition QState.addTransition(None self, QAbstractState _target)"""
        return QAbstractTransition()
    def setErrorState(self, _state):
        """None QState.setErrorState(None self, QAbstractState _state)"""
        return None
    def errorState(self):
        """QAbstractState QState.errorState(None self)"""
        return QAbstractState()


class QStateMachine(QState):
    """"""
    NoError = int() # QStateMachine.Error enum
    NoInitialStateError = int() # QStateMachine.Error enum
    NoDefaultStateInHistoryStateError = int() # QStateMachine.Error enum
    NoCommonAncestorForTransitionError = int() # QStateMachine.Error enum

    DontRestoreProperties = int() # QStateMachine.RestorePolicy enum
    RestoreProperties = int() # QStateMachine.RestorePolicy enum

    NormalPriority = int() # QStateMachine.EventPriority enum
    HighPriority = int() # QStateMachine.EventPriority enum

    def __init__(self, _parent):
        """None QStateMachine.__init__(None self, QObject _parent)"""
        return None
    def event(self, _e):
        """bool QStateMachine.event(None self, QEvent _e)"""
        return bool()
    def onExit(self, _event):
        """None QStateMachine.onExit(None self, QEvent _event)"""
        return None
    def onEntry(self, _event):
        """None QStateMachine.onEntry(None self, QEvent _event)"""
        return None
    def stop(self):
        """None QStateMachine.stop(None self)"""
        return None
    def start(self):
        """None QStateMachine.start(None self)"""
        return None
    def eventFilter(self, _watched, _event):
        """bool QStateMachine.eventFilter(None self, QObject _watched, QEvent _event)"""
        return bool()
    def configuration(self):
        """list-of-QAbstractState QStateMachine.configuration(None self)"""
        return [QAbstractState()]
    def cancelDelayedEvent(self, _id):
        """bool QStateMachine.cancelDelayedEvent(None self, int _id)"""
        return bool()
    def postDelayedEvent(self, _event, _delay):
        """int QStateMachine.postDelayedEvent(None self, QEvent _event, int _delay)"""
        return int()
    def postEvent(self, _event, _priority):
        """None QStateMachine.postEvent(None self, QEvent _event, QStateMachine.EventPriority _priority)"""
        return None
    def setGlobalRestorePolicy(self, _restorePolicy):
        """None QStateMachine.setGlobalRestorePolicy(None self, QStateMachine.RestorePolicy _restorePolicy)"""
        return None
    def globalRestorePolicy(self):
        """QStateMachine.RestorePolicy QStateMachine.globalRestorePolicy(None self)"""
        return QStateMachine.RestorePolicy()
    def removeDefaultAnimation(self, _animation):
        """None QStateMachine.removeDefaultAnimation(None self, QAbstractAnimation _animation)"""
        return None
    def defaultAnimations(self):
        """list-of-QAbstractAnimation QStateMachine.defaultAnimations(None self)"""
        return [QAbstractAnimation()]
    def addDefaultAnimation(self, _animation):
        """None QStateMachine.addDefaultAnimation(None self, QAbstractAnimation _animation)"""
        return None
    def setAnimated(self, _enabled):
        """None QStateMachine.setAnimated(None self, bool _enabled)"""
        return None
    def isAnimated(self):
        """bool QStateMachine.isAnimated(None self)"""
        return bool()
    def isRunning(self):
        """bool QStateMachine.isRunning(None self)"""
        return bool()
    def clearError(self):
        """None QStateMachine.clearError(None self)"""
        return None
    def errorString(self):
        """QString QStateMachine.errorString(None self)"""
        return QString()
    def error(self):
        """QStateMachine.Error QStateMachine.error(None self)"""
        return QStateMachine.Error()
    def removeState(self, _state):
        """None QStateMachine.removeState(None self, QAbstractState _state)"""
        return None
    def addState(self, _state):
        """None QStateMachine.addState(None self, QAbstractState _state)"""
        return None


class QString():
    """"""
    NormalizationForm_D = int() # QString.NormalizationForm enum
    NormalizationForm_C = int() # QString.NormalizationForm enum
    NormalizationForm_KD = int() # QString.NormalizationForm enum
    NormalizationForm_KC = int() # QString.NormalizationForm enum

    KeepEmptyParts = int() # QString.SplitBehavior enum
    SkipEmptyParts = int() # QString.SplitBehavior enum

    SectionDefault = int() # QString.SectionFlag enum
    SectionSkipEmpty = int() # QString.SectionFlag enum
    SectionIncludeLeadingSep = int() # QString.SectionFlag enum
    SectionIncludeTrailingSep = int() # QString.SectionFlag enum
    SectionCaseInsensitiveSeps = int() # QString.SectionFlag enum

    def __init__(self):
        """None QString.__init__(None self)"""
        return None
    def __init__(self, _size, _c):
        """None QString.__init__(None self, int _size, QChar _c)"""
        return None
    def __init__(self, _s):
        """None QString.__init__(None self, QString _s)"""
        return None
    def __init__(self, _a):
        """None QString.__init__(None self, QByteArray _a)"""
        return None
    def __init__(self):
        """QUuid QString.__init__(None self)"""
        return QUuid()
    def __add__(self, _s2):
        """QString QString.__add__(None self, QString _s2)"""
        return QString()
    def __add__(self, _ba):
        """QString QString.__add__(None self, QByteArray _ba)"""
        return QString()
    def repeated(self, _times):
        """QString QString.repeated(None self, int _times)"""
        return QString()
    def toCaseFolded(self):
        """QString QString.toCaseFolded(None self)"""
        return QString()
    def reserve(self, _asize):
        """None QString.reserve(None self, int _asize)"""
        return None
    def capacity(self):
        """int QString.capacity(None self)"""
        return int()
    def clear(self):
        """None QString.clear(None self)"""
        return None
    def isEmpty(self):
        """bool QString.isEmpty(None self)"""
        return bool()
    def __imul__(self, _m):
        """QString QString.__imul__(None self, int _m)"""
        return QString()
    def __mul__(self, _m):
        """QString QString.__mul__(None self, int _m)"""
        return QString()
    def __hash__(self):
        """int QString.__hash__(None self)"""
        return int()
    def __str__(self):
        """str QString.__str__(None self)"""
        return str()
    def __unicode__(self):
        """unicode QString.__unicode__(None self)"""
        return unicode()
    def __contains__(self, _s):
        """int QString.__contains__(None self, QString _s)"""
        return int()
    def __getitem__(self, _i):
        """QString QString.__getitem__(None self, int _i)"""
        return QString()
    def __getitem__(self, _slice):
        """QString QString.__getitem__(None self, slice _slice)"""
        return QString()
    def at(self, _i):
        """QChar QString.at(None self, int _i)"""
        return QChar()
    def length(self):
        """int QString.length(None self)"""
        return int()
    def isRightToLeft(self):
        """bool QString.isRightToLeft(None self)"""
        return bool()
    def isSimpleText(self):
        """bool QString.isSimpleText(None self)"""
        return bool()
    def isNull(self):
        """bool QString.isNull(None self)"""
        return bool()
    def push_front(self, _s):
        """None QString.push_front(None self, QString _s)"""
        return None
    def push_back(self, _s):
        """None QString.push_back(None self, QString _s)"""
        return None
    def __ge__(self, _s):
        """bool QString.__ge__(None self, QString _s)"""
        return bool()
    def __ge__(self, _s):
        """bool QString.__ge__(None self, QLatin1String _s)"""
        return bool()
    def __ge__(self, _s):
        """bool QString.__ge__(None self, QByteArray _s)"""
        return bool()
    def __le__(self, _s):
        """bool QString.__le__(None self, QString _s)"""
        return bool()
    def __le__(self, _s):
        """bool QString.__le__(None self, QLatin1String _s)"""
        return bool()
    def __le__(self, _s):
        """bool QString.__le__(None self, QByteArray _s)"""
        return bool()
    def __ne__(self, _s):
        """bool QString.__ne__(None self, QString _s)"""
        return bool()
    def __ne__(self, _s):
        """bool QString.__ne__(None self, QLatin1String _s)"""
        return bool()
    def __ne__(self, _s):
        """bool QString.__ne__(None self, QByteArray _s)"""
        return bool()
    def __ne__(self, _s2):
        """bool QString.__ne__(None self, QStringRef _s2)"""
        return bool()
    def __gt__(self, _s):
        """bool QString.__gt__(None self, QString _s)"""
        return bool()
    def __gt__(self, _s):
        """bool QString.__gt__(None self, QLatin1String _s)"""
        return bool()
    def __gt__(self, _s):
        """bool QString.__gt__(None self, QByteArray _s)"""
        return bool()
    def __lt__(self, _s):
        """bool QString.__lt__(None self, QString _s)"""
        return bool()
    def __lt__(self, _s):
        """bool QString.__lt__(None self, QLatin1String _s)"""
        return bool()
    def __lt__(self, _s):
        """bool QString.__lt__(None self, QByteArray _s)"""
        return bool()
    def __eq__(self, _s):
        """bool QString.__eq__(None self, QString _s)"""
        return bool()
    def __eq__(self, _s):
        """bool QString.__eq__(None self, QLatin1String _s)"""
        return bool()
    def __eq__(self, _s):
        """bool QString.__eq__(None self, QByteArray _s)"""
        return bool()
    def __eq__(self, _s2):
        """bool QString.__eq__(None self, QStringRef _s2)"""
        return bool()
    def number(self, _n, _base):
        """QString QString.number(None self, int _n, int _base)"""
        return QString()
    def number(self, _n, _format, _precision):
        """QString QString.number(None self, float _n, str _format, int _precision)"""
        return QString()
    def number(self, _n, _base):
        """QString QString.number(None self, int _n, int _base)"""
        return QString()
    def number(self, _n, _base):
        """QString QString.number(None self, int _n, int _base)"""
        return QString()
    def setNum(self, _n, _base):
        """QString QString.setNum(None self, int _n, int _base)"""
        return QString()
    def setNum(self, _n, _format, _precision):
        """QString QString.setNum(None self, float _n, str _format, int _precision)"""
        return QString()
    def setNum(self, _n, _base):
        """QString QString.setNum(None self, int _n, int _base)"""
        return QString()
    def setNum(self, _n, _base):
        """QString QString.setNum(None self, int _n, int _base)"""
        return QString()
    def toDouble(self, _ok):
        """float QString.toDouble(None self, bool _ok)"""
        return float()
    def toFloat(self, _ok):
        """float QString.toFloat(None self, bool _ok)"""
        return float()
    def toULongLong(self, _ok, _base):
        """int QString.toULongLong(None self, bool _ok, int _base)"""
        return int()
    def toLongLong(self, _ok, _base):
        """int QString.toLongLong(None self, bool _ok, int _base)"""
        return int()
    def toULong(self, _ok, _base):
        """int QString.toULong(None self, bool _ok, int _base)"""
        return int()
    def toLong(self, _ok, _base):
        """int QString.toLong(None self, bool _ok, int _base)"""
        return int()
    def toUInt(self, _ok, _base):
        """int QString.toUInt(None self, bool _ok, int _base)"""
        return int()
    def toInt(self, _ok, _base):
        """int QString.toInt(None self, bool _ok, int _base)"""
        return int()
    def toUShort(self, _ok, _base):
        """int QString.toUShort(None self, bool _ok, int _base)"""
        return int()
    def toShort(self, _ok, _base):
        """int QString.toShort(None self, bool _ok, int _base)"""
        return int()
    def localeAwareCompare(self, _s):
        """int QString.localeAwareCompare(None self, QString _s)"""
        return int()
    def localeAwareCompare(self, _s):
        """int QString.localeAwareCompare(None self, QStringRef _s)"""
        return int()
    def localeAwareCompare(self, _s1, _s2):
        """int QString.localeAwareCompare(None self, QString _s1, QString _s2)"""
        return int()
    def localeAwareCompare(self, _s1, _s2):
        """int QString.localeAwareCompare(None self, QString _s1, QStringRef _s2)"""
        return int()
    def compare(self, _s):
        """int QString.compare(None self, QString _s)"""
        return int()
    def compare(self, _s, _cs):
        """int QString.compare(None self, QString _s, Qt.CaseSensitivity _cs)"""
        return int()
    def compare(self, _other, _cs):
        """int QString.compare(None self, QLatin1String _other, Qt.CaseSensitivity _cs)"""
        return int()
    def compare(self, _ref, _cs):
        """int QString.compare(None self, QStringRef _ref, Qt.CaseSensitivity _cs)"""
        return int()
    def compare(self, _s1, _s2):
        """int QString.compare(None self, QString _s1, QString _s2)"""
        return int()
    def compare(self, _s1, _s2, _cs):
        """int QString.compare(None self, QString _s1, QString _s2, Qt.CaseSensitivity _cs)"""
        return int()
    def compare(self, _s1, _s2, _cs):
        """int QString.compare(None self, QString _s1, QLatin1String _s2, Qt.CaseSensitivity _cs)"""
        return int()
    def compare(self, _s1, _s2, _cs):
        """int QString.compare(None self, QLatin1String _s1, QString _s2, Qt.CaseSensitivity _cs)"""
        return int()
    def compare(self, _s1, _s2, _cs):
        """int QString.compare(None self, QString _s1, QStringRef _s2, Qt.CaseSensitivity _cs)"""
        return int()
    def fromLocal8Bit(self, _str, _size):
        """QString QString.fromLocal8Bit(None self, str _str, int _size)"""
        return QString()
    def fromUtf8(self, _str, _size):
        """QString QString.fromUtf8(None self, str _str, int _size)"""
        return QString()
    def fromLatin1(self, _str, _size):
        """QString QString.fromLatin1(None self, str _str, int _size)"""
        return QString()
    def fromAscii(self, _str, _size):
        """QString QString.fromAscii(None self, str _str, int _size)"""
        return QString()
    def toLocal8Bit(self):
        """QByteArray QString.toLocal8Bit(None self)"""
        return QByteArray()
    def toUtf8(self):
        """QByteArray QString.toUtf8(None self)"""
        return QByteArray()
    def toLatin1(self):
        """QByteArray QString.toLatin1(None self)"""
        return QByteArray()
    def toAscii(self):
        """QByteArray QString.toAscii(None self)"""
        return QByteArray()
    def normalized(self, _mode):
        """QString QString.normalized(None self, QString.NormalizationForm _mode)"""
        return QString()
    def normalized(self, _mode, _version):
        """QString QString.normalized(None self, QString.NormalizationForm _mode, QChar.UnicodeVersion _version)"""
        return QString()
    def split(self, _sep, _behavior, _cs):
        """QStringList QString.split(None self, QString _sep, QString.SplitBehavior _behavior, Qt.CaseSensitivity _cs)"""
        return QStringList()
    def split(self, _sep, _behavior):
        """QStringList QString.split(None self, QRegExp _sep, QString.SplitBehavior _behavior)"""
        return QStringList()
    def replace(self, _i, _len, _after):
        """QString QString.replace(None self, int _i, int _len, QString _after)"""
        return QString()
    def replace(self, _before, _after, _cs):
        """QString QString.replace(None self, QString _before, QString _after, Qt.CaseSensitivity _cs)"""
        return QString()
    def replace(self, _rx, _after):
        """QString QString.replace(None self, QRegExp _rx, QString _after)"""
        return QString()
    def replace(self, _before, _after, _cs):
        """QString QString.replace(None self, QLatin1String _before, QLatin1String _after, Qt.CaseSensitivity _cs)"""
        return QString()
    def replace(self, _before, _after, _cs):
        """QString QString.replace(None self, QLatin1String _before, QString _after, Qt.CaseSensitivity _cs)"""
        return QString()
    def replace(self, _before, _after, _cs):
        """QString QString.replace(None self, QString _before, QLatin1String _after, Qt.CaseSensitivity _cs)"""
        return QString()
    def remove(self, _i, _len):
        """QString QString.remove(None self, int _i, int _len)"""
        return QString()
    def remove(self, _str, _cs):
        """QString QString.remove(None self, QString _str, Qt.CaseSensitivity _cs)"""
        return QString()
    def remove(self, _rx):
        """QString QString.remove(None self, QRegExp _rx)"""
        return QString()
    def __iadd__(self, _c):
        """QString QString.__iadd__(None self, QChar.SpecialCharacter _c)"""
        return QString()
    def __iadd__(self, _s):
        """QString QString.__iadd__(None self, QString _s)"""
        return QString()
    def __iadd__(self, _s):
        """QString QString.__iadd__(None self, QLatin1String _s)"""
        return QString()
    def __iadd__(self, _s):
        """QString QString.__iadd__(None self, QByteArray _s)"""
        return QString()
    def prepend(self, _s):
        """QString QString.prepend(None self, QString _s)"""
        return QString()
    def prepend(self, _s):
        """QString QString.prepend(None self, QLatin1String _s)"""
        return QString()
    def prepend(self, _s):
        """QString QString.prepend(None self, QByteArray _s)"""
        return QString()
    def append(self, _s):
        """QString QString.append(None self, QString _s)"""
        return QString()
    def append(self, _s):
        """QString QString.append(None self, QLatin1String _s)"""
        return QString()
    def append(self, _s):
        """QString QString.append(None self, QByteArray _s)"""
        return QString()
    def insert(self, _i, _s):
        """QString QString.insert(None self, int _i, QString _s)"""
        return QString()
    def insert(self, _i, _s):
        """QString QString.insert(None self, int _i, QLatin1String _s)"""
        return QString()
    def simplified(self):
        """QString QString.simplified(None self)"""
        return QString()
    def trimmed(self):
        """QString QString.trimmed(None self)"""
        return QString()
    def toUpper(self):
        """QString QString.toUpper(None self)"""
        return QString()
    def toLower(self):
        """QString QString.toLower(None self)"""
        return QString()
    def rightJustified(self, _width, _fillChar, _truncate):
        """QString QString.rightJustified(None self, int _width, QChar _fillChar, bool _truncate)"""
        return QString()
    def leftJustified(self, _width, _fillChar, _truncate):
        """QString QString.leftJustified(None self, int _width, QChar _fillChar, bool _truncate)"""
        return QString()
    def endsWith(self, _s, _cs):
        """bool QString.endsWith(None self, QString _s, Qt.CaseSensitivity _cs)"""
        return bool()
    def endsWith(self, _s, _cs):
        """bool QString.endsWith(None self, QLatin1String _s, Qt.CaseSensitivity _cs)"""
        return bool()
    def startsWith(self, _s, _cs):
        """bool QString.startsWith(None self, QString _s, Qt.CaseSensitivity _cs)"""
        return bool()
    def startsWith(self, _s, _cs):
        """bool QString.startsWith(None self, QLatin1String _s, Qt.CaseSensitivity _cs)"""
        return bool()
    def mid(self, _position, _n):
        """QString QString.mid(None self, int _position, int _n)"""
        return QString()
    def right(self, _len):
        """QString QString.right(None self, int _len)"""
        return QString()
    def left(self, _len):
        """QString QString.left(None self, int _len)"""
        return QString()
    def section(self, _sep, _start, _end, _flags):
        """QString QString.section(None self, QString _sep, int _start, int _end, QString.SectionFlags _flags)"""
        return QString()
    def section(self, _reg, _start, _end, _flags):
        """QString QString.section(None self, QRegExp _reg, int _start, int _end, QString.SectionFlags _flags)"""
        return QString()
    def contains(self, _str, _cs):
        """bool QString.contains(None self, QString _str, Qt.CaseSensitivity _cs)"""
        return bool()
    def contains(self, _rx):
        """bool QString.contains(None self, QRegExp _rx)"""
        return bool()
    def lastIndexOf(self, _str, _from, _cs):
        """int QString.lastIndexOf(None self, QString _str, int _from, Qt.CaseSensitivity _cs)"""
        return int()
    def lastIndexOf(self, _str, _from, _cs):
        """int QString.lastIndexOf(None self, QLatin1String _str, int _from, Qt.CaseSensitivity _cs)"""
        return int()
    def lastIndexOf(self, _rx, _from):
        """int QString.lastIndexOf(None self, QRegExp _rx, int _from)"""
        return int()
    def indexOf(self, _str, _from, _cs):
        """int QString.indexOf(None self, QString _str, int _from, Qt.CaseSensitivity _cs)"""
        return int()
    def indexOf(self, _str, _from, _cs):
        """int QString.indexOf(None self, QLatin1String _str, int _from, Qt.CaseSensitivity _cs)"""
        return int()
    def indexOf(self, _rx, _from):
        """int QString.indexOf(None self, QRegExp _rx, int _from)"""
        return int()
    def arg(self, _a, _fieldWidth, _base, _fillChar):
        """QString QString.arg(None self, int _a, int _fieldWidth, int _base, QChar _fillChar)"""
        return QString()
    def arg(self, _a, _fieldWidth, _format, _precision, _fillChar):
        """QString QString.arg(None self, float _a, int _fieldWidth, str _format, int _precision, QChar _fillChar)"""
        return QString()
    def arg(self, _a, _fieldWidth, _base, _fillChar):
        """QString QString.arg(None self, int _a, int _fieldWidth, int _base, QChar _fillChar)"""
        return QString()
    def arg(self, _a, _fieldWidth, _base, _fillChar):
        """QString QString.arg(None self, int _a, int _fieldWidth, int _base, QChar _fillChar)"""
        return QString()
    def arg(self, _a, _fieldWidth, _fillChar):
        """QString QString.arg(None self, QString _a, int _fieldWidth, QChar _fillChar)"""
        return QString()
    def arg(self, _a1, _a2):
        """QString QString.arg(None self, QString _a1, QString _a2)"""
        return QString()
    def arg(self, _a1, _a2, _a3):
        """QString QString.arg(None self, QString _a1, QString _a2, QString _a3)"""
        return QString()
    def arg(self, _a1, _a2, _a3, _a4):
        """QString QString.arg(None self, QString _a1, QString _a2, QString _a3, QString _a4)"""
        return QString()
    def arg(self, _a1, _a2, _a3, _a4, _a5):
        """QString QString.arg(None self, QString _a1, QString _a2, QString _a3, QString _a4, QString _a5)"""
        return QString()
    def arg(self, _a1, _a2, _a3, _a4, _a5, _a6):
        """QString QString.arg(None self, QString _a1, QString _a2, QString _a3, QString _a4, QString _a5, QString _a6)"""
        return QString()
    def arg(self, _a1, _a2, _a3, _a4, _a5, _a6, _a7):
        """QString QString.arg(None self, QString _a1, QString _a2, QString _a3, QString _a4, QString _a5, QString _a6, QString _a7)"""
        return QString()
    def arg(self, _a1, _a2, _a3, _a4, _a5, _a6, _a7, _a8):
        """QString QString.arg(None self, QString _a1, QString _a2, QString _a3, QString _a4, QString _a5, QString _a6, QString _a7, QString _a8)"""
        return QString()
    def arg(self, _a1, _a2, _a3, _a4, _a5, _a6, _a7, _a8, _a9):
        """QString QString.arg(None self, QString _a1, QString _a2, QString _a3, QString _a4, QString _a5, QString _a6, QString _a7, QString _a8, QString _a9)"""
        return QString()
    def squeeze(self):
        """None QString.squeeze(None self)"""
        return None
    def chop(self, _n):
        """None QString.chop(None self, int _n)"""
        return None
    def truncate(self, _pos):
        """None QString.truncate(None self, int _pos)"""
        return None
    def fill(self, _ch, _size):
        """QString QString.fill(None self, QChar _ch, int _size)"""
        return QString()
    def resize(self, _size):
        """None QString.resize(None self, int _size)"""
        return None
    def __len__(self):
        """ QString.__len__(None self)"""
        return ()
    def count(self):
        """int QString.count(None self)"""
        return int()
    def count(self, _str, _cs):
        """int QString.count(None self, QString _str, Qt.CaseSensitivity _cs)"""
        return int()
    def count(self):
        """QRegExp QString.count(None self)"""
        return QRegExp()
    def size(self):
        """int QString.size(None self)"""
        return int()
    def __repr__(self):
        """str QString.__repr__(None self)"""
        return str()


class QLatin1String():
    """"""
    def __init__(self, _s):
        """None QLatin1String.__init__(None self, str _s)"""
        return None
    def __init__(self):
        """QLatin1String QLatin1String.__init__(None self)"""
        return QLatin1String()
    def __le__(self, _s):
        """bool QLatin1String.__le__(None self, QString _s)"""
        return bool()
    def __le__(self, _s2):
        """bool QLatin1String.__le__(None self, QLatin1String _s2)"""
        return bool()
    def __ge__(self, _s):
        """bool QLatin1String.__ge__(None self, QString _s)"""
        return bool()
    def __ge__(self, _s2):
        """bool QLatin1String.__ge__(None self, QLatin1String _s2)"""
        return bool()
    def __lt__(self, _s):
        """bool QLatin1String.__lt__(None self, QString _s)"""
        return bool()
    def __lt__(self, _s2):
        """bool QLatin1String.__lt__(None self, QLatin1String _s2)"""
        return bool()
    def __gt__(self, _s):
        """bool QLatin1String.__gt__(None self, QString _s)"""
        return bool()
    def __gt__(self, _s2):
        """bool QLatin1String.__gt__(None self, QLatin1String _s2)"""
        return bool()
    def __ne__(self, _s):
        """bool QLatin1String.__ne__(None self, QString _s)"""
        return bool()
    def __ne__(self, _s2):
        """bool QLatin1String.__ne__(None self, QLatin1String _s2)"""
        return bool()
    def __ne__(self, _s2):
        """bool QLatin1String.__ne__(None self, QStringRef _s2)"""
        return bool()
    def __eq__(self, _s):
        """bool QLatin1String.__eq__(None self, QString _s)"""
        return bool()
    def __eq__(self, _s2):
        """bool QLatin1String.__eq__(None self, QLatin1String _s2)"""
        return bool()
    def __eq__(self, _s2):
        """bool QLatin1String.__eq__(None self, QStringRef _s2)"""
        return bool()
    def latin1(self):
        """str QLatin1String.latin1(None self)"""
        return str()
    def __repr__(self):
        """str QLatin1String.__repr__(None self)"""
        return str()


class QStringRef():
    """"""
    def __init__(self):
        """None QStringRef.__init__(None self)"""
        return None
    def __init__(self, _aString, _aPosition, _aSize):
        """None QStringRef.__init__(None self, QString _aString, int _aPosition, int _aSize)"""
        return None
    def __init__(self, _aString):
        """None QStringRef.__init__(None self, QString _aString)"""
        return None
    def __init__(self, _other):
        """None QStringRef.__init__(None self, QStringRef _other)"""
        return None
    def __eq__(self, _s2):
        """bool QStringRef.__eq__(None self, QStringRef _s2)"""
        return bool()
    def __eq__(self, _s2):
        """bool QStringRef.__eq__(None self, QString _s2)"""
        return bool()
    def __eq__(self, _s2):
        """bool QStringRef.__eq__(None self, QLatin1String _s2)"""
        return bool()
    def __ne__(self, _s2):
        """bool QStringRef.__ne__(None self, QStringRef _s2)"""
        return bool()
    def __ne__(self, _s2):
        """bool QStringRef.__ne__(None self, QString _s2)"""
        return bool()
    def __ne__(self, _s2):
        """bool QStringRef.__ne__(None self, QLatin1String _s2)"""
        return bool()
    def __lt__(self, _s2):
        """bool QStringRef.__lt__(None self, QStringRef _s2)"""
        return bool()
    def __le__(self, _s2):
        """bool QStringRef.__le__(None self, QStringRef _s2)"""
        return bool()
    def __gt__(self, _s2):
        """bool QStringRef.__gt__(None self, QStringRef _s2)"""
        return bool()
    def __ge__(self, _s2):
        """bool QStringRef.__ge__(None self, QStringRef _s2)"""
        return bool()
    def __str__(self):
        """str QStringRef.__str__(None self)"""
        return str()
    def __unicode__(self):
        """unicode QStringRef.__unicode__(None self)"""
        return unicode()
    def localeAwareCompare(self, _s):
        """int QStringRef.localeAwareCompare(None self, QString _s)"""
        return int()
    def localeAwareCompare(self, _s):
        """int QStringRef.localeAwareCompare(None self, QStringRef _s)"""
        return int()
    def localeAwareCompare(self, _s1, _s2):
        """int QStringRef.localeAwareCompare(None self, QStringRef _s1, QString _s2)"""
        return int()
    def localeAwareCompare(self, _s1, _s2):
        """int QStringRef.localeAwareCompare(None self, QStringRef _s1, QStringRef _s2)"""
        return int()
    def compare(self, _other, _cs):
        """int QStringRef.compare(None self, QString _other, Qt.CaseSensitivity _cs)"""
        return int()
    def compare(self, _other, _cs):
        """int QStringRef.compare(None self, QStringRef _other, Qt.CaseSensitivity _cs)"""
        return int()
    def compare(self, _other, _cs):
        """int QStringRef.compare(None self, QLatin1String _other, Qt.CaseSensitivity _cs)"""
        return int()
    def compare(self, _s1, _s2, _cs):
        """int QStringRef.compare(None self, QStringRef _s1, QString _s2, Qt.CaseSensitivity _cs)"""
        return int()
    def compare(self, _s1, _s2, _cs):
        """int QStringRef.compare(None self, QStringRef _s1, QStringRef _s2, Qt.CaseSensitivity _cs)"""
        return int()
    def compare(self, _s1, _s2, _cs):
        """int QStringRef.compare(None self, QStringRef _s1, QLatin1String _s2, Qt.CaseSensitivity _cs)"""
        return int()
    def at(self, _i):
        """QChar QStringRef.at(None self, int _i)"""
        return QChar()
    def appendTo(self, _string):
        """QStringRef QStringRef.appendTo(None self, QString _string)"""
        return QStringRef()
    def isNull(self):
        """bool QStringRef.isNull(None self)"""
        return bool()
    def isEmpty(self):
        """bool QStringRef.isEmpty(None self)"""
        return bool()
    def toString(self):
        """QString QStringRef.toString(None self)"""
        return QString()
    def clear(self):
        """None QStringRef.clear(None self)"""
        return None
    def constData(self):
        """QChar QStringRef.constData(None self)"""
        return QChar()
    def data(self):
        """QChar QStringRef.data(None self)"""
        return QChar()
    def unicode(self):
        """QChar QStringRef.unicode(None self)"""
        return QChar()
    def length(self):
        """int QStringRef.length(None self)"""
        return int()
    def __len__(self):
        """ QStringRef.__len__(None self)"""
        return ()
    def count(self):
        """int QStringRef.count(None self)"""
        return int()
    def size(self):
        """int QStringRef.size(None self)"""
        return int()
    def position(self):
        """int QStringRef.position(None self)"""
        return int()
    def string(self):
        """QString QStringRef.string(None self)"""
        return QString()


class QStringList():
    """"""
    def __init__(self):
        """None QStringList.__init__(None self)"""
        return None
    def __init__(self, _i):
        """None QStringList.__init__(None self, QString _i)"""
        return None
    def __init__(self, _l):
        """None QStringList.__init__(None self, QStringList _l)"""
        return None
    def __iadd__(self, _other):
        """QStringList QStringList.__iadd__(None self, QStringList _other)"""
        return QStringList()
    def __iadd__(self, _value):
        """QStringList QStringList.__iadd__(None self, QString _value)"""
        return QStringList()
    def mid(self, _pos, _length):
        """QStringList QStringList.mid(None self, int _pos, int _length)"""
        return QStringList()
    def last(self):
        """QString QStringList.last(None self)"""
        return QString()
    def first(self):
        """QString QStringList.first(None self)"""
        return QString()
    def __len__(self):
        """ QStringList.__len__(None self)"""
        return ()
    def count(self, _str):
        """int QStringList.count(None self, QString _str)"""
        return int()
    def count(self):
        """int QStringList.count(None self)"""
        return int()
    def swap(self, _i, _j):
        """None QStringList.swap(None self, int _i, int _j)"""
        return None
    def move(self, _from, _to):
        """None QStringList.move(None self, int _from, int _to)"""
        return None
    def takeLast(self):
        """QString QStringList.takeLast(None self)"""
        return QString()
    def takeFirst(self):
        """QString QStringList.takeFirst(None self)"""
        return QString()
    def takeAt(self, _i):
        """QString QStringList.takeAt(None self, int _i)"""
        return QString()
    def removeAll(self, _str):
        """int QStringList.removeAll(None self, QString _str)"""
        return int()
    def removeAt(self, _i):
        """None QStringList.removeAt(None self, int _i)"""
        return None
    def replace(self, _i, _str):
        """None QStringList.replace(None self, int _i, QString _str)"""
        return None
    def insert(self, _i, _str):
        """None QStringList.insert(None self, int _i, QString _str)"""
        return None
    def prepend(self, _str):
        """None QStringList.prepend(None self, QString _str)"""
        return None
    def append(self, _str):
        """None QStringList.append(None self, QString _str)"""
        return None
    def isEmpty(self):
        """bool QStringList.isEmpty(None self)"""
        return bool()
    def clear(self):
        """None QStringList.clear(None self)"""
        return None
    def __ne__(self, _other):
        """bool QStringList.__ne__(None self, QStringList _other)"""
        return bool()
    def __eq__(self, _other):
        """bool QStringList.__eq__(None self, QStringList _other)"""
        return bool()
    def __imul__(self, _by):
        """QStringList QStringList.__imul__(None self, int _by)"""
        return QStringList()
    def __mul__(self, _by):
        """QStringList QStringList.__mul__(None self, int _by)"""
        return QStringList()
    def __add__(self, _other):
        """QStringList QStringList.__add__(None self, QStringList _other)"""
        return QStringList()
    def __contains__(self, _str):
        """int QStringList.__contains__(None self, QString _str)"""
        return int()
    def __getitem__(self, _i):
        """QString QStringList.__getitem__(None self, int _i)"""
        return QString()
    def __getitem__(self, _slice):
        """QStringList QStringList.__getitem__(None self, slice _slice)"""
        return QStringList()
    def __delitem__(self, _i):
        """None QStringList.__delitem__(None self, int _i)"""
        return None
    def __delitem__(self, _slice):
        """None QStringList.__delitem__(None self, slice _slice)"""
        return None
    def __setitem__(self, _i, _str):
        """None QStringList.__setitem__(None self, int _i, QString _str)"""
        return None
    def __setitem__(self, _slice, _list):
        """None QStringList.__setitem__(None self, slice _slice, QStringList _list)"""
        return None
    def removeDuplicates(self):
        """int QStringList.removeDuplicates(None self)"""
        return int()
    def lastIndexOf(self, _value, _from):
        """int QStringList.lastIndexOf(None self, QString _value, int _from)"""
        return int()
    def lastIndexOf(self, _rx, _from):
        """int QStringList.lastIndexOf(None self, QRegExp _rx, int _from)"""
        return int()
    def indexOf(self, _value, _from):
        """int QStringList.indexOf(None self, QString _value, int _from)"""
        return int()
    def indexOf(self, _rx, _from):
        """int QStringList.indexOf(None self, QRegExp _rx, int _from)"""
        return int()
    def replaceInStrings(self, _before, _after, _cs):
        """QStringList QStringList.replaceInStrings(None self, QString _before, QString _after, Qt.CaseSensitivity _cs)"""
        return QStringList()
    def replaceInStrings(self, _rx, _after):
        """QStringList QStringList.replaceInStrings(None self, QRegExp _rx, QString _after)"""
        return QStringList()
    def contains(self, _str, _cs):
        """bool QStringList.contains(None self, QString _str, Qt.CaseSensitivity _cs)"""
        return bool()
    def filter(self, _str, _cs):
        """QStringList QStringList.filter(None self, QString _str, Qt.CaseSensitivity _cs)"""
        return QStringList()
    def filter(self, _rx):
        """QStringList QStringList.filter(None self, QRegExp _rx)"""
        return QStringList()
    def join(self, _sep):
        """QString QStringList.join(None self, QString _sep)"""
        return QString()
    def sort(self):
        """None QStringList.sort(None self)"""
        return None
    def __lshift__(self, _str):
        """QStringList QStringList.__lshift__(None self, QString _str)"""
        return QStringList()
    def __lshift__(self, _l):
        """QStringList QStringList.__lshift__(None self, QStringList _l)"""
        return QStringList()


class QStringMatcher():
    """"""
    def __init__(self):
        """None QStringMatcher.__init__(None self)"""
        return None
    def __init__(self, _pattern, _cs):
        """None QStringMatcher.__init__(None self, QString _pattern, Qt.CaseSensitivity _cs)"""
        return None
    def __init__(self, _other):
        """None QStringMatcher.__init__(None self, QStringMatcher _other)"""
        return None
    def caseSensitivity(self):
        """Qt.CaseSensitivity QStringMatcher.caseSensitivity(None self)"""
        return Qt.CaseSensitivity()
    def pattern(self):
        """QString QStringMatcher.pattern(None self)"""
        return QString()
    def indexIn(self, _str, _from):
        """int QStringMatcher.indexIn(None self, QString _str, int _from)"""
        return int()
    def setCaseSensitivity(self, _cs):
        """None QStringMatcher.setCaseSensitivity(None self, Qt.CaseSensitivity _cs)"""
        return None
    def setPattern(self, _pattern):
        """None QStringMatcher.setPattern(None self, QString _pattern)"""
        return None


class QSystemSemaphore():
    """"""
    NoError = int() # QSystemSemaphore.SystemSemaphoreError enum
    PermissionDenied = int() # QSystemSemaphore.SystemSemaphoreError enum
    KeyError = int() # QSystemSemaphore.SystemSemaphoreError enum
    AlreadyExists = int() # QSystemSemaphore.SystemSemaphoreError enum
    NotFound = int() # QSystemSemaphore.SystemSemaphoreError enum
    OutOfResources = int() # QSystemSemaphore.SystemSemaphoreError enum
    UnknownError = int() # QSystemSemaphore.SystemSemaphoreError enum

    Open = int() # QSystemSemaphore.AccessMode enum
    Create = int() # QSystemSemaphore.AccessMode enum

    def __init__(self, _key, _initialValue, _mode):
        """None QSystemSemaphore.__init__(None self, QString _key, int _initialValue, QSystemSemaphore.AccessMode _mode)"""
        return None
    def errorString(self):
        """QString QSystemSemaphore.errorString(None self)"""
        return QString()
    def error(self):
        """QSystemSemaphore.SystemSemaphoreError QSystemSemaphore.error(None self)"""
        return QSystemSemaphore.SystemSemaphoreError()
    def release(self, _n):
        """bool QSystemSemaphore.release(None self, int _n)"""
        return bool()
    def acquire(self):
        """bool QSystemSemaphore.acquire(None self)"""
        return bool()
    def key(self):
        """QString QSystemSemaphore.key(None self)"""
        return QString()
    def setKey(self, _key, _initialValue, _mode):
        """None QSystemSemaphore.setKey(None self, QString _key, int _initialValue, QSystemSemaphore.AccessMode _mode)"""
        return None


class QTemporaryFile(QFile):
    """"""
    def __init__(self):
        """None QTemporaryFile.__init__(None self)"""
        return None
    def __init__(self, _templateName):
        """None QTemporaryFile.__init__(None self, QString _templateName)"""
        return None
    def __init__(self, _parent):
        """None QTemporaryFile.__init__(None self, QObject _parent)"""
        return None
    def __init__(self, _templateName, _parent):
        """None QTemporaryFile.__init__(None self, QString _templateName, QObject _parent)"""
        return None
    def fileEngine(self):
        """QAbstractFileEngine QTemporaryFile.fileEngine(None self)"""
        return QAbstractFileEngine()
    def createLocalFile(self, _fileName):
        """QTemporaryFile QTemporaryFile.createLocalFile(None self, QString _fileName)"""
        return QTemporaryFile()
    def createLocalFile(self, _file):
        """QTemporaryFile QTemporaryFile.createLocalFile(None self, QFile _file)"""
        return QTemporaryFile()
    def setFileTemplate(self, _name):
        """None QTemporaryFile.setFileTemplate(None self, QString _name)"""
        return None
    def fileTemplate(self):
        """QString QTemporaryFile.fileTemplate(None self)"""
        return QString()
    def fileName(self):
        """QString QTemporaryFile.fileName(None self)"""
        return QString()
    def open(self):
        """bool QTemporaryFile.open(None self)"""
        return bool()
    def open(self, _flags):
        """bool QTemporaryFile.open(None self, QIODevice.OpenMode _flags)"""
        return bool()
    def setAutoRemove(self, _b):
        """None QTemporaryFile.setAutoRemove(None self, bool _b)"""
        return None
    def autoRemove(self):
        """bool QTemporaryFile.autoRemove(None self)"""
        return bool()


class QTextBoundaryFinder():
    """"""
    Grapheme = int() # QTextBoundaryFinder.BoundaryType enum
    Word = int() # QTextBoundaryFinder.BoundaryType enum
    Line = int() # QTextBoundaryFinder.BoundaryType enum
    Sentence = int() # QTextBoundaryFinder.BoundaryType enum

    NotAtBoundary = int() # QTextBoundaryFinder.BoundaryReason enum
    StartWord = int() # QTextBoundaryFinder.BoundaryReason enum
    EndWord = int() # QTextBoundaryFinder.BoundaryReason enum

    def __init__(self):
        """None QTextBoundaryFinder.__init__(None self)"""
        return None
    def __init__(self, _other):
        """None QTextBoundaryFinder.__init__(None self, QTextBoundaryFinder _other)"""
        return None
    def __init__(self, _type, _string):
        """None QTextBoundaryFinder.__init__(None self, QTextBoundaryFinder.BoundaryType _type, QString _string)"""
        return None
    def boundaryReasons(self):
        """QTextBoundaryFinder.BoundaryReasons QTextBoundaryFinder.boundaryReasons(None self)"""
        return QTextBoundaryFinder.BoundaryReasons()
    def isAtBoundary(self):
        """bool QTextBoundaryFinder.isAtBoundary(None self)"""
        return bool()
    def toPreviousBoundary(self):
        """int QTextBoundaryFinder.toPreviousBoundary(None self)"""
        return int()
    def toNextBoundary(self):
        """int QTextBoundaryFinder.toNextBoundary(None self)"""
        return int()
    def setPosition(self, _position):
        """None QTextBoundaryFinder.setPosition(None self, int _position)"""
        return None
    def position(self):
        """int QTextBoundaryFinder.position(None self)"""
        return int()
    def toEnd(self):
        """None QTextBoundaryFinder.toEnd(None self)"""
        return None
    def toStart(self):
        """None QTextBoundaryFinder.toStart(None self)"""
        return None
    def string(self):
        """QString QTextBoundaryFinder.string(None self)"""
        return QString()
    def type(self):
        """QTextBoundaryFinder.BoundaryType QTextBoundaryFinder.type(None self)"""
        return QTextBoundaryFinder.BoundaryType()
    def isValid(self):
        """bool QTextBoundaryFinder.isValid(None self)"""
        return bool()


class QTextCodec():
    """"""
    DefaultConversion = int() # QTextCodec.ConversionFlag enum
    ConvertInvalidToNull = int() # QTextCodec.ConversionFlag enum
    IgnoreHeader = int() # QTextCodec.ConversionFlag enum

    def __init__(self):
        """None QTextCodec.__init__(None self)"""
        return None
    def setCodecForCStrings(self, _c):
        """None QTextCodec.setCodecForCStrings(None self, QTextCodec _c)"""
        return None
    def codecForCStrings(self):
        """QTextCodec QTextCodec.codecForCStrings(None self)"""
        return QTextCodec()
    def setCodecForTr(self, _c):
        """None QTextCodec.setCodecForTr(None self, QTextCodec _c)"""
        return None
    def codecForTr(self):
        """QTextCodec QTextCodec.codecForTr(None self)"""
        return QTextCodec()
    def convertToUnicode(self, _in, _state):
        """abstract QString QTextCodec.convertToUnicode(None self, str _in, QTextCodec.ConverterState _state)"""
        return QString()
    def mibEnum(self):
        """abstract int QTextCodec.mibEnum(None self)"""
        return int()
    def aliases(self):
        """list-of-QByteArray QTextCodec.aliases(None self)"""
        return [QByteArray()]
    def name(self):
        """abstract QByteArray QTextCodec.name(None self)"""
        return QByteArray()
    def fromUnicode(self, _uc):
        """QByteArray QTextCodec.fromUnicode(None self, QString _uc)"""
        return QByteArray()
    def toUnicode(self):
        """QByteArray QTextCodec.toUnicode(None self)"""
        return QByteArray()
    def toUnicode(self, _chars):
        """QString QTextCodec.toUnicode(None self, str _chars)"""
        return QString()
    def toUnicode(self, _in, _state):
        """QString QTextCodec.toUnicode(None self, str _in, QTextCodec.ConverterState _state)"""
        return QString()
    def canEncode(self):
        """QString QTextCodec.canEncode(None self)"""
        return QString()
    def makeEncoder(self):
        """QTextEncoder QTextCodec.makeEncoder(None self)"""
        return QTextEncoder()
    def makeEncoder(self, _flags):
        """QTextEncoder QTextCodec.makeEncoder(None self, QTextCodec.ConversionFlags _flags)"""
        return QTextEncoder()
    def makeDecoder(self):
        """QTextDecoder QTextCodec.makeDecoder(None self)"""
        return QTextDecoder()
    def makeDecoder(self, _flags):
        """QTextDecoder QTextCodec.makeDecoder(None self, QTextCodec.ConversionFlags _flags)"""
        return QTextDecoder()
    def setCodecForLocale(self, _c):
        """None QTextCodec.setCodecForLocale(None self, QTextCodec _c)"""
        return None
    def codecForLocale(self):
        """QTextCodec QTextCodec.codecForLocale(None self)"""
        return QTextCodec()
    def availableMibs(self):
        """list-of-int QTextCodec.availableMibs(None self)"""
        return [int()]
    def availableCodecs(self):
        """list-of-QByteArray QTextCodec.availableCodecs(None self)"""
        return [QByteArray()]
    def codecForUtfText(self, _ba):
        """QTextCodec QTextCodec.codecForUtfText(None self, QByteArray _ba)"""
        return QTextCodec()
    def codecForUtfText(self, _ba, _defaultCodec):
        """QTextCodec QTextCodec.codecForUtfText(None self, QByteArray _ba, QTextCodec _defaultCodec)"""
        return QTextCodec()
    def codecForHtml(self, _ba):
        """QTextCodec QTextCodec.codecForHtml(None self, QByteArray _ba)"""
        return QTextCodec()
    def codecForHtml(self, _ba, _defaultCodec):
        """QTextCodec QTextCodec.codecForHtml(None self, QByteArray _ba, QTextCodec _defaultCodec)"""
        return QTextCodec()
    def codecForMib(self, _mib):
        """QTextCodec QTextCodec.codecForMib(None self, int _mib)"""
        return QTextCodec()
    def codecForName(self, _name):
        """QTextCodec QTextCodec.codecForName(None self, QByteArray _name)"""
        return QTextCodec()
    def codecForName(self, _name):
        """QTextCodec QTextCodec.codecForName(None self, str _name)"""
        return QTextCodec()


class QTextEncoder():
    """"""
    def __init__(self, _codec):
        """None QTextEncoder.__init__(None self, QTextCodec _codec)"""
        return None
    def __init__(self, _codec, _flags):
        """None QTextEncoder.__init__(None self, QTextCodec _codec, QTextCodec.ConversionFlags _flags)"""
        return None
    def fromUnicode(self, _str):
        """QByteArray QTextEncoder.fromUnicode(None self, QString _str)"""
        return QByteArray()


class QTextDecoder():
    """"""
    def __init__(self, _codec):
        """None QTextDecoder.__init__(None self, QTextCodec _codec)"""
        return None
    def __init__(self, _codec, _flags):
        """None QTextDecoder.__init__(None self, QTextCodec _codec, QTextCodec.ConversionFlags _flags)"""
        return None
    def toUnicode(self, _chars):
        """QString QTextDecoder.toUnicode(None self, str _chars)"""
        return QString()
    def toUnicode(self, _target, _chars):
        """None QTextDecoder.toUnicode(None self, QString _target, str _chars)"""
        return None
    def toUnicode(self, _ba):
        """QString QTextDecoder.toUnicode(None self, QByteArray _ba)"""
        return QString()


class QTextStream():
    """"""
    Ok = int() # QTextStream.Status enum
    ReadPastEnd = int() # QTextStream.Status enum
    ReadCorruptData = int() # QTextStream.Status enum

    ShowBase = int() # QTextStream.NumberFlag enum
    ForcePoint = int() # QTextStream.NumberFlag enum
    ForceSign = int() # QTextStream.NumberFlag enum
    UppercaseBase = int() # QTextStream.NumberFlag enum
    UppercaseDigits = int() # QTextStream.NumberFlag enum

    AlignLeft = int() # QTextStream.FieldAlignment enum
    AlignRight = int() # QTextStream.FieldAlignment enum
    AlignCenter = int() # QTextStream.FieldAlignment enum
    AlignAccountingStyle = int() # QTextStream.FieldAlignment enum

    SmartNotation = int() # QTextStream.RealNumberNotation enum
    FixedNotation = int() # QTextStream.RealNumberNotation enum
    ScientificNotation = int() # QTextStream.RealNumberNotation enum

    def __init__(self):
        """None QTextStream.__init__(None self)"""
        return None
    def __init__(self, _device):
        """None QTextStream.__init__(None self, QIODevice _device)"""
        return None
    def __init__(self, _string, _mode):
        """None QTextStream.__init__(None self, QString _string, QIODevice.OpenMode _mode)"""
        return None
    def __init__(self, _array, _mode):
        """None QTextStream.__init__(None self, QByteArray _array, QIODevice.OpenMode _mode)"""
        return None
    def locale(self):
        """QLocale QTextStream.locale(None self)"""
        return QLocale()
    def setLocale(self, _locale):
        """None QTextStream.setLocale(None self, QLocale _locale)"""
        return None
    def __lshift__(self, _f):
        """QTextStream QTextStream.__lshift__(None self, float _f)"""
        return QTextStream()
    def __lshift__(self, _b):
        """QTextStream QTextStream.__lshift__(None self, bool _b)"""
        return QTextStream()
    def __lshift__(self, _i):
        """QTextStream QTextStream.__lshift__(None self, int _i)"""
        return QTextStream()
    def __lshift__(self, _i):
        """QTextStream QTextStream.__lshift__(None self, int _i)"""
        return QTextStream()
    def __lshift__(self, _i):
        """QTextStream QTextStream.__lshift__(None self, int _i)"""
        return QTextStream()
    def __lshift__(self, _s):
        """QTextStream QTextStream.__lshift__(None self, QString _s)"""
        return QTextStream()
    def __lshift__(self, _array):
        """QTextStream QTextStream.__lshift__(None self, QByteArray _array)"""
        return QTextStream()
    def __lshift__(self, _m):
        """QTextStream QTextStream.__lshift__(None self, QTextStreamManipulator _m)"""
        return QTextStream()
    def __rshift__(self, _ch):
        """QTextStream QTextStream.__rshift__(None self, QChar _ch)"""
        return QTextStream()
    def __rshift__(self, _s):
        """QTextStream QTextStream.__rshift__(None self, QString _s)"""
        return QTextStream()
    def __rshift__(self, _array):
        """QTextStream QTextStream.__rshift__(None self, QByteArray _array)"""
        return QTextStream()
    def pos(self):
        """int QTextStream.pos(None self)"""
        return int()
    def resetStatus(self):
        """None QTextStream.resetStatus(None self)"""
        return None
    def setStatus(self, _status):
        """None QTextStream.setStatus(None self, QTextStream.Status _status)"""
        return None
    def status(self):
        """QTextStream.Status QTextStream.status(None self)"""
        return QTextStream.Status()
    def realNumberPrecision(self):
        """int QTextStream.realNumberPrecision(None self)"""
        return int()
    def setRealNumberPrecision(self, _precision):
        """None QTextStream.setRealNumberPrecision(None self, int _precision)"""
        return None
    def realNumberNotation(self):
        """QTextStream.RealNumberNotation QTextStream.realNumberNotation(None self)"""
        return QTextStream.RealNumberNotation()
    def setRealNumberNotation(self, _notation):
        """None QTextStream.setRealNumberNotation(None self, QTextStream.RealNumberNotation _notation)"""
        return None
    def integerBase(self):
        """int QTextStream.integerBase(None self)"""
        return int()
    def setIntegerBase(self, _base):
        """None QTextStream.setIntegerBase(None self, int _base)"""
        return None
    def numberFlags(self):
        """QTextStream.NumberFlags QTextStream.numberFlags(None self)"""
        return QTextStream.NumberFlags()
    def setNumberFlags(self, _flags):
        """None QTextStream.setNumberFlags(None self, QTextStream.NumberFlags _flags)"""
        return None
    def fieldWidth(self):
        """int QTextStream.fieldWidth(None self)"""
        return int()
    def setFieldWidth(self, _width):
        """None QTextStream.setFieldWidth(None self, int _width)"""
        return None
    def padChar(self):
        """QChar QTextStream.padChar(None self)"""
        return QChar()
    def setPadChar(self, _ch):
        """None QTextStream.setPadChar(None self, QChar _ch)"""
        return None
    def fieldAlignment(self):
        """QTextStream.FieldAlignment QTextStream.fieldAlignment(None self)"""
        return QTextStream.FieldAlignment()
    def setFieldAlignment(self, _alignment):
        """None QTextStream.setFieldAlignment(None self, QTextStream.FieldAlignment _alignment)"""
        return None
    def readAll(self):
        """QString QTextStream.readAll(None self)"""
        return QString()
    def readLine(self, _maxLength):
        """QString QTextStream.readLine(None self, int _maxLength)"""
        return QString()
    def read(self, _maxlen):
        """QString QTextStream.read(None self, int _maxlen)"""
        return QString()
    def skipWhiteSpace(self):
        """None QTextStream.skipWhiteSpace(None self)"""
        return None
    def seek(self, _pos):
        """bool QTextStream.seek(None self, int _pos)"""
        return bool()
    def flush(self):
        """None QTextStream.flush(None self)"""
        return None
    def reset(self):
        """None QTextStream.reset(None self)"""
        return None
    def atEnd(self):
        """bool QTextStream.atEnd(None self)"""
        return bool()
    def string(self):
        """QString QTextStream.string(None self)"""
        return QString()
    def setString(self, _string, _mode):
        """None QTextStream.setString(None self, QString _string, QIODevice.OpenMode _mode)"""
        return None
    def device(self):
        """QIODevice QTextStream.device(None self)"""
        return QIODevice()
    def setDevice(self, _device):
        """None QTextStream.setDevice(None self, QIODevice _device)"""
        return None
    def generateByteOrderMark(self):
        """bool QTextStream.generateByteOrderMark(None self)"""
        return bool()
    def setGenerateByteOrderMark(self, _generate):
        """None QTextStream.setGenerateByteOrderMark(None self, bool _generate)"""
        return None
    def autoDetectUnicode(self):
        """bool QTextStream.autoDetectUnicode(None self)"""
        return bool()
    def setAutoDetectUnicode(self, _enabled):
        """None QTextStream.setAutoDetectUnicode(None self, bool _enabled)"""
        return None
    def codec(self):
        """QTextCodec QTextStream.codec(None self)"""
        return QTextCodec()
    def setCodec(self, _codec):
        """None QTextStream.setCodec(None self, QTextCodec _codec)"""
        return None
    def setCodec(self, _codecName):
        """None QTextStream.setCodec(None self, str _codecName)"""
        return None


class QThread(QObject):
    """"""
    IdlePriority = int() # QThread.Priority enum
    LowestPriority = int() # QThread.Priority enum
    LowPriority = int() # QThread.Priority enum
    NormalPriority = int() # QThread.Priority enum
    HighPriority = int() # QThread.Priority enum
    HighestPriority = int() # QThread.Priority enum
    TimeCriticalPriority = int() # QThread.Priority enum
    InheritPriority = int() # QThread.Priority enum

    def __init__(self, _parent):
        """None QThread.__init__(None self, QObject _parent)"""
        return None
    def usleep(self):
        """int QThread.usleep(None self)"""
        return int()
    def msleep(self):
        """int QThread.msleep(None self)"""
        return int()
    def sleep(self):
        """int QThread.sleep(None self)"""
        return int()
    def setTerminationEnabled(self, _enabled):
        """None QThread.setTerminationEnabled(None self, bool _enabled)"""
        return None
    def exec_(self):
        """int QThread.exec_(None self)"""
        return int()
    def run(self):
        """None QThread.run(None self)"""
        return None
    def wait(self, _msecs):
        """bool QThread.wait(None self, int _msecs)"""
        return bool()
    def quit(self):
        """None QThread.quit(None self)"""
        return None
    def terminate(self):
        """None QThread.terminate(None self)"""
        return None
    def start(self, _priority):
        """None QThread.start(None self, QThread.Priority _priority)"""
        return None
    def exit(self, _returnCode):
        """None QThread.exit(None self, int _returnCode)"""
        return None
    def stackSize(self):
        """int QThread.stackSize(None self)"""
        return int()
    def setStackSize(self, _stackSize):
        """None QThread.setStackSize(None self, int _stackSize)"""
        return None
    def priority(self):
        """QThread.Priority QThread.priority(None self)"""
        return QThread.Priority()
    def setPriority(self, _priority):
        """None QThread.setPriority(None self, QThread.Priority _priority)"""
        return None
    def isRunning(self):
        """bool QThread.isRunning(None self)"""
        return bool()
    def isFinished(self):
        """bool QThread.isFinished(None self)"""
        return bool()
    def yieldCurrentThread(self):
        """None QThread.yieldCurrentThread(None self)"""
        return None
    def idealThreadCount(self):
        """int QThread.idealThreadCount(None self)"""
        return int()
    def currentThreadId(self):
        """int QThread.currentThreadId(None self)"""
        return int()
    def currentThread(self):
        """QThread QThread.currentThread(None self)"""
        return QThread()


class QThreadPool(QObject):
    """"""
    def __init__(self, _parent):
        """None QThreadPool.__init__(None self, QObject _parent)"""
        return None
    def waitForDone(self):
        """None QThreadPool.waitForDone(None self)"""
        return None
    def releaseThread(self):
        """None QThreadPool.releaseThread(None self)"""
        return None
    def reserveThread(self):
        """None QThreadPool.reserveThread(None self)"""
        return None
    def activeThreadCount(self):
        """int QThreadPool.activeThreadCount(None self)"""
        return int()
    def setMaxThreadCount(self, _maxThreadCount):
        """None QThreadPool.setMaxThreadCount(None self, int _maxThreadCount)"""
        return None
    def maxThreadCount(self):
        """int QThreadPool.maxThreadCount(None self)"""
        return int()
    def setExpiryTimeout(self, _expiryTimeout):
        """None QThreadPool.setExpiryTimeout(None self, int _expiryTimeout)"""
        return None
    def expiryTimeout(self):
        """int QThreadPool.expiryTimeout(None self)"""
        return int()
    def tryStart(self, _runnable):
        """bool QThreadPool.tryStart(None self, QRunnable _runnable)"""
        return bool()
    def start(self, _runnable, _priority):
        """None QThreadPool.start(None self, QRunnable _runnable, int _priority)"""
        return None
    def globalInstance(self):
        """QThreadPool QThreadPool.globalInstance(None self)"""
        return QThreadPool()


class QTimeLine(QObject):
    """"""
    NotRunning = int() # QTimeLine.State enum
    Paused = int() # QTimeLine.State enum
    Running = int() # QTimeLine.State enum

    Forward = int() # QTimeLine.Direction enum
    Backward = int() # QTimeLine.Direction enum

    EaseInCurve = int() # QTimeLine.CurveShape enum
    EaseOutCurve = int() # QTimeLine.CurveShape enum
    EaseInOutCurve = int() # QTimeLine.CurveShape enum
    LinearCurve = int() # QTimeLine.CurveShape enum
    SineCurve = int() # QTimeLine.CurveShape enum
    CosineCurve = int() # QTimeLine.CurveShape enum

    def __init__(self, _duration, _parent):
        """None QTimeLine.__init__(None self, int _duration, QObject _parent)"""
        return None
    def setEasingCurve(self, _curve):
        """None QTimeLine.setEasingCurve(None self, QEasingCurve _curve)"""
        return None
    def easingCurve(self):
        """QEasingCurve QTimeLine.easingCurve(None self)"""
        return QEasingCurve()
    def timerEvent(self, _event):
        """None QTimeLine.timerEvent(None self, QTimerEvent _event)"""
        return None
    def toggleDirection(self):
        """None QTimeLine.toggleDirection(None self)"""
        return None
    def stop(self):
        """None QTimeLine.stop(None self)"""
        return None
    def start(self):
        """None QTimeLine.start(None self)"""
        return None
    def setPaused(self, _paused):
        """None QTimeLine.setPaused(None self, bool _paused)"""
        return None
    def setCurrentTime(self, _msec):
        """None QTimeLine.setCurrentTime(None self, int _msec)"""
        return None
    def resume(self):
        """None QTimeLine.resume(None self)"""
        return None
    def valueForTime(self, _msec):
        """float QTimeLine.valueForTime(None self, int _msec)"""
        return float()
    def frameForTime(self, _msec):
        """int QTimeLine.frameForTime(None self, int _msec)"""
        return int()
    def currentValue(self):
        """float QTimeLine.currentValue(None self)"""
        return float()
    def currentFrame(self):
        """int QTimeLine.currentFrame(None self)"""
        return int()
    def currentTime(self):
        """int QTimeLine.currentTime(None self)"""
        return int()
    def setCurveShape(self, _shape):
        """None QTimeLine.setCurveShape(None self, QTimeLine.CurveShape _shape)"""
        return None
    def curveShape(self):
        """QTimeLine.CurveShape QTimeLine.curveShape(None self)"""
        return QTimeLine.CurveShape()
    def setUpdateInterval(self, _interval):
        """None QTimeLine.setUpdateInterval(None self, int _interval)"""
        return None
    def updateInterval(self):
        """int QTimeLine.updateInterval(None self)"""
        return int()
    def setFrameRange(self, _startFrame, _endFrame):
        """None QTimeLine.setFrameRange(None self, int _startFrame, int _endFrame)"""
        return None
    def setEndFrame(self, _frame):
        """None QTimeLine.setEndFrame(None self, int _frame)"""
        return None
    def endFrame(self):
        """int QTimeLine.endFrame(None self)"""
        return int()
    def setStartFrame(self, _frame):
        """None QTimeLine.setStartFrame(None self, int _frame)"""
        return None
    def startFrame(self):
        """int QTimeLine.startFrame(None self)"""
        return int()
    def setDuration(self, _duration):
        """None QTimeLine.setDuration(None self, int _duration)"""
        return None
    def duration(self):
        """int QTimeLine.duration(None self)"""
        return int()
    def setDirection(self, _direction):
        """None QTimeLine.setDirection(None self, QTimeLine.Direction _direction)"""
        return None
    def direction(self):
        """QTimeLine.Direction QTimeLine.direction(None self)"""
        return QTimeLine.Direction()
    def setLoopCount(self, _count):
        """None QTimeLine.setLoopCount(None self, int _count)"""
        return None
    def loopCount(self):
        """int QTimeLine.loopCount(None self)"""
        return int()
    def state(self):
        """QTimeLine.State QTimeLine.state(None self)"""
        return QTimeLine.State()


class QTimer(QObject):
    """"""
    def __init__(self, _parent):
        """None QTimer.__init__(None self, QObject _parent)"""
        return None
    def timerEvent(self):
        """QTimerEvent QTimer.timerEvent(None self)"""
        return QTimerEvent()
    def stop(self):
        """None QTimer.stop(None self)"""
        return None
    def start(self, _msec):
        """None QTimer.start(None self, int _msec)"""
        return None
    def start(self):
        """None QTimer.start(None self)"""
        return None
    def singleShot(self, _msec, _receiver, _member):
        """None QTimer.singleShot(None self, int _msec, QObject _receiver, SLOT()SLOT() _member)"""
        return None
    def singleShot(self, _msec, _receiver):
        """None QTimer.singleShot(None self, int _msec, callable _receiver)"""
        return None
    def setSingleShot(self, _asingleShot):
        """None QTimer.setSingleShot(None self, bool _asingleShot)"""
        return None
    def isSingleShot(self):
        """bool QTimer.isSingleShot(None self)"""
        return bool()
    def interval(self):
        """int QTimer.interval(None self)"""
        return int()
    def setInterval(self, _msec):
        """None QTimer.setInterval(None self, int _msec)"""
        return None
    def timerId(self):
        """int QTimer.timerId(None self)"""
        return int()
    def isActive(self):
        """bool QTimer.isActive(None self)"""
        return bool()


class QTranslator(QObject):
    """"""
    def __init__(self, _parent):
        """None QTranslator.__init__(None self, QObject _parent)"""
        return None
    def loadFromData(self, _data):
        """bool QTranslator.loadFromData(None self, str _data)"""
        return bool()
    def load(self, _fileName, _directory, _searchDelimiters, _suffix):
        """bool QTranslator.load(None self, QString _fileName, QString _directory, QString _searchDelimiters, QString _suffix)"""
        return bool()
    def isEmpty(self):
        """bool QTranslator.isEmpty(None self)"""
        return bool()
    def translate(self, _context, _sourceText, _disambiguation):
        """QString QTranslator.translate(None self, str _context, str _sourceText, str _disambiguation)"""
        return QString()
    def translate(self, _context, _sourceText, _comment, _n):
        """QString QTranslator.translate(None self, str _context, str _sourceText, str _comment, int _n)"""
        return QString()


class QUrl():
    """"""
    TolerantMode = int() # QUrl.ParsingMode enum
    StrictMode = int() # QUrl.ParsingMode enum

    __kdevpythondocumentation_builtin_None = int() # QUrl.FormattingOption enum
    RemoveScheme = int() # QUrl.FormattingOption enum
    RemovePassword = int() # QUrl.FormattingOption enum
    RemoveUserInfo = int() # QUrl.FormattingOption enum
    RemovePort = int() # QUrl.FormattingOption enum
    RemoveAuthority = int() # QUrl.FormattingOption enum
    RemovePath = int() # QUrl.FormattingOption enum
    RemoveQuery = int() # QUrl.FormattingOption enum
    RemoveFragment = int() # QUrl.FormattingOption enum
    StripTrailingSlash = int() # QUrl.FormattingOption enum

    def __init__(self):
        """None QUrl.__init__(None self)"""
        return None
    def __init__(self, _url):
        """None QUrl.__init__(None self, QString _url)"""
        return None
    def __init__(self, _copy):
        """None QUrl.__init__(None self, QUrl _copy)"""
        return None
    def __init__(self, _url, _mode):
        """None QUrl.__init__(None self, QString _url, QUrl.ParsingMode _mode)"""
        return None
    def __ge__(self, _url):
        """bool QUrl.__ge__(None self, QUrl _url)"""
        return bool()
    def fromUserInput(self, _userInput):
        """QUrl QUrl.fromUserInput(None self, QString _userInput)"""
        return QUrl()
    def encodedFragment(self):
        """QByteArray QUrl.encodedFragment(None self)"""
        return QByteArray()
    def setEncodedFragment(self, _fragment):
        """None QUrl.setEncodedFragment(None self, QByteArray _fragment)"""
        return None
    def removeAllEncodedQueryItems(self, _key):
        """None QUrl.removeAllEncodedQueryItems(None self, QByteArray _key)"""
        return None
    def removeEncodedQueryItem(self, _key):
        """None QUrl.removeEncodedQueryItem(None self, QByteArray _key)"""
        return None
    def allEncodedQueryItemValues(self, _key):
        """list-of-QByteArray QUrl.allEncodedQueryItemValues(None self, QByteArray _key)"""
        return [QByteArray()]
    def encodedQueryItemValue(self, _key):
        """QByteArray QUrl.encodedQueryItemValue(None self, QByteArray _key)"""
        return QByteArray()
    def hasEncodedQueryItem(self, _key):
        """bool QUrl.hasEncodedQueryItem(None self, QByteArray _key)"""
        return bool()
    def encodedQueryItems(self):
        """list-of-tuple-of-QByteArray-QByteArray QUrl.encodedQueryItems(None self)"""
        return [tuple-of-QByteArray-QByteArray()]
    def addEncodedQueryItem(self, _key, _value):
        """None QUrl.addEncodedQueryItem(None self, QByteArray _key, QByteArray _value)"""
        return None
    def setEncodedQueryItems(self, _query):
        """None QUrl.setEncodedQueryItems(None self, list-of-tuple-of-QByteArray-QByteArray _query)"""
        return None
    def encodedPath(self):
        """QByteArray QUrl.encodedPath(None self)"""
        return QByteArray()
    def setEncodedPath(self, _path):
        """None QUrl.setEncodedPath(None self, QByteArray _path)"""
        return None
    def encodedHost(self):
        """QByteArray QUrl.encodedHost(None self)"""
        return QByteArray()
    def setEncodedHost(self, _host):
        """None QUrl.setEncodedHost(None self, QByteArray _host)"""
        return None
    def encodedPassword(self):
        """QByteArray QUrl.encodedPassword(None self)"""
        return QByteArray()
    def setEncodedPassword(self, _password):
        """None QUrl.setEncodedPassword(None self, QByteArray _password)"""
        return None
    def encodedUserName(self):
        """QByteArray QUrl.encodedUserName(None self)"""
        return QByteArray()
    def setEncodedUserName(self, _userName):
        """None QUrl.setEncodedUserName(None self, QByteArray _userName)"""
        return None
    def setIdnWhitelist(self):
        """QStringList QUrl.setIdnWhitelist(None self)"""
        return QStringList()
    def idnWhitelist(self):
        """QStringList QUrl.idnWhitelist(None self)"""
        return QStringList()
    def toAce(self):
        """QString QUrl.toAce(None self)"""
        return QString()
    def fromAce(self):
        """QByteArray QUrl.fromAce(None self)"""
        return QByteArray()
    def errorString(self):
        """QString QUrl.errorString(None self)"""
        return QString()
    def hasFragment(self):
        """bool QUrl.hasFragment(None self)"""
        return bool()
    def hasQuery(self):
        """bool QUrl.hasQuery(None self)"""
        return bool()
    def toPunycode(self):
        """QString QUrl.toPunycode(None self)"""
        return QString()
    def fromPunycode(self):
        """QByteArray QUrl.fromPunycode(None self)"""
        return QByteArray()
    def toPercentEncoding(self, _input, _exclude, _include):
        """QByteArray QUrl.toPercentEncoding(None self, QString _input, QByteArray _exclude, QByteArray _include)"""
        return QByteArray()
    def fromPercentEncoding(self):
        """QByteArray QUrl.fromPercentEncoding(None self)"""
        return QByteArray()
    def __ne__(self, _url):
        """bool QUrl.__ne__(None self, QUrl _url)"""
        return bool()
    def __eq__(self, _url):
        """bool QUrl.__eq__(None self, QUrl _url)"""
        return bool()
    def __lt__(self, _url):
        """bool QUrl.__lt__(None self, QUrl _url)"""
        return bool()
    def isDetached(self):
        """bool QUrl.isDetached(None self)"""
        return bool()
    def detach(self):
        """None QUrl.detach(None self)"""
        return None
    def fromEncoded(self, _url):
        """QUrl QUrl.fromEncoded(None self, QByteArray _url)"""
        return QUrl()
    def fromEncoded(self, _url, _mode):
        """QUrl QUrl.fromEncoded(None self, QByteArray _url, QUrl.ParsingMode _mode)"""
        return QUrl()
    def toEncoded(self, _options):
        """QByteArray QUrl.toEncoded(None self, QUrl.FormattingOptions _options)"""
        return QByteArray()
    def toString(self, _options):
        """QString QUrl.toString(None self, QUrl.FormattingOptions _options)"""
        return QString()
    def toLocalFile(self):
        """QString QUrl.toLocalFile(None self)"""
        return QString()
    def fromLocalFile(self, _localfile):
        """QUrl QUrl.fromLocalFile(None self, QString _localfile)"""
        return QUrl()
    def isParentOf(self, _url):
        """bool QUrl.isParentOf(None self, QUrl _url)"""
        return bool()
    def isRelative(self):
        """bool QUrl.isRelative(None self)"""
        return bool()
    def resolved(self, _relative):
        """QUrl QUrl.resolved(None self, QUrl _relative)"""
        return QUrl()
    def fragment(self):
        """QString QUrl.fragment(None self)"""
        return QString()
    def setFragment(self, _fragment):
        """None QUrl.setFragment(None self, QString _fragment)"""
        return None
    def removeAllQueryItems(self, _key):
        """None QUrl.removeAllQueryItems(None self, QString _key)"""
        return None
    def removeQueryItem(self, _key):
        """None QUrl.removeQueryItem(None self, QString _key)"""
        return None
    def allQueryItemValues(self, _key):
        """QStringList QUrl.allQueryItemValues(None self, QString _key)"""
        return QStringList()
    def queryItemValue(self, _key):
        """QString QUrl.queryItemValue(None self, QString _key)"""
        return QString()
    def hasQueryItem(self, _key):
        """bool QUrl.hasQueryItem(None self, QString _key)"""
        return bool()
    def queryItems(self):
        """list-of-tuple-of-QString-QString QUrl.queryItems(None self)"""
        return [tuple-of-QString-QString()]
    def addQueryItem(self, _key, _value):
        """None QUrl.addQueryItem(None self, QString _key, QString _value)"""
        return None
    def setQueryItems(self, _query):
        """None QUrl.setQueryItems(None self, list-of-tuple-of-QString-QString _query)"""
        return None
    def queryPairDelimiter(self):
        """str QUrl.queryPairDelimiter(None self)"""
        return str()
    def queryValueDelimiter(self):
        """str QUrl.queryValueDelimiter(None self)"""
        return str()
    def setQueryDelimiters(self, _valueDelimiter, _pairDelimiter):
        """None QUrl.setQueryDelimiters(None self, str _valueDelimiter, str _pairDelimiter)"""
        return None
    def encodedQuery(self):
        """QByteArray QUrl.encodedQuery(None self)"""
        return QByteArray()
    def setEncodedQuery(self, _query):
        """None QUrl.setEncodedQuery(None self, QByteArray _query)"""
        return None
    def path(self):
        """QString QUrl.path(None self)"""
        return QString()
    def setPath(self, _path):
        """None QUrl.setPath(None self, QString _path)"""
        return None
    def port(self):
        """int QUrl.port(None self)"""
        return int()
    def port(self, _defaultPort):
        """int QUrl.port(None self, int _defaultPort)"""
        return int()
    def setPort(self, _port):
        """None QUrl.setPort(None self, int _port)"""
        return None
    def host(self):
        """QString QUrl.host(None self)"""
        return QString()
    def setHost(self, _host):
        """None QUrl.setHost(None self, QString _host)"""
        return None
    def password(self):
        """QString QUrl.password(None self)"""
        return QString()
    def setPassword(self, _password):
        """None QUrl.setPassword(None self, QString _password)"""
        return None
    def userName(self):
        """QString QUrl.userName(None self)"""
        return QString()
    def setUserName(self, _userName):
        """None QUrl.setUserName(None self, QString _userName)"""
        return None
    def userInfo(self):
        """QString QUrl.userInfo(None self)"""
        return QString()
    def setUserInfo(self, _userInfo):
        """None QUrl.setUserInfo(None self, QString _userInfo)"""
        return None
    def authority(self):
        """QString QUrl.authority(None self)"""
        return QString()
    def setAuthority(self, _authority):
        """None QUrl.setAuthority(None self, QString _authority)"""
        return None
    def scheme(self):
        """QString QUrl.scheme(None self)"""
        return QString()
    def setScheme(self, _scheme):
        """None QUrl.setScheme(None self, QString _scheme)"""
        return None
    def clear(self):
        """None QUrl.clear(None self)"""
        return None
    def isEmpty(self):
        """bool QUrl.isEmpty(None self)"""
        return bool()
    def isValid(self):
        """bool QUrl.isValid(None self)"""
        return bool()
    def setEncodedUrl(self, _url):
        """None QUrl.setEncodedUrl(None self, QByteArray _url)"""
        return None
    def setEncodedUrl(self, _url, _mode):
        """None QUrl.setEncodedUrl(None self, QByteArray _url, QUrl.ParsingMode _mode)"""
        return None
    def setUrl(self, _url):
        """None QUrl.setUrl(None self, QString _url)"""
        return None
    def setUrl(self, _url, _mode):
        """None QUrl.setUrl(None self, QString _url, QUrl.ParsingMode _mode)"""
        return None
    def __hash__(self):
        """int QUrl.__hash__(None self)"""
        return int()
    def __repr__(self):
        """str QUrl.__repr__(None self)"""
        return str()


class QUuid():
    """"""
    VerUnknown = int() # QUuid.Version enum
    Time = int() # QUuid.Version enum
    EmbeddedPOSIX = int() # QUuid.Version enum
    Name = int() # QUuid.Version enum
    Random = int() # QUuid.Version enum

    VarUnknown = int() # QUuid.Variant enum
    NCS = int() # QUuid.Variant enum
    DCE = int() # QUuid.Variant enum
    Microsoft = int() # QUuid.Variant enum
    Reserved = int() # QUuid.Variant enum

    def __init__(self):
        """None QUuid.__init__(None self)"""
        return None
    def __init__(self, _l, _w1, _w2, _b1, _b2, _b3, _b4, _b5, _b6, _b7, _b8):
        """None QUuid.__init__(None self, int _l, int _w1, int _w2, str _b1, str _b2, str _b3, str _b4, str _b5, str _b6, str _b7, str _b8)"""
        return None
    def __init__(self):
        """QString QUuid.__init__(None self)"""
        return QString()
    def __init__(self):
        """QUuid QUuid.__init__(None self)"""
        return QUuid()
    def __ge__(self, _other):
        """bool QUuid.__ge__(None self, QUuid _other)"""
        return bool()
    def __le__(self, _other):
        """bool QUuid.__le__(None self, QUuid _other)"""
        return bool()
    def version(self):
        """QUuid.Version QUuid.version(None self)"""
        return QUuid.Version()
    def variant(self):
        """QUuid.Variant QUuid.variant(None self)"""
        return QUuid.Variant()
    def createUuid(self):
        """QUuid QUuid.createUuid(None self)"""
        return QUuid()
    def __gt__(self, _other):
        """bool QUuid.__gt__(None self, QUuid _other)"""
        return bool()
    def __lt__(self, _other):
        """bool QUuid.__lt__(None self, QUuid _other)"""
        return bool()
    def __ne__(self, _orig):
        """bool QUuid.__ne__(None self, QUuid _orig)"""
        return bool()
    def __eq__(self, _orig):
        """bool QUuid.__eq__(None self, QUuid _orig)"""
        return bool()
    def isNull(self):
        """bool QUuid.isNull(None self)"""
        return bool()
    def toString(self):
        """QString QUuid.toString(None self)"""
        return QString()
    def __repr__(self):
        """str QUuid.__repr__(None self)"""
        return str()


class QVariant():
    """"""
    Invalid = int() # QVariant.Type enum
    Bool = int() # QVariant.Type enum
    Int = int() # QVariant.Type enum
    UInt = int() # QVariant.Type enum
    LongLong = int() # QVariant.Type enum
    ULongLong = int() # QVariant.Type enum
    Double = int() # QVariant.Type enum
    Char = int() # QVariant.Type enum
    Map = int() # QVariant.Type enum
    List = int() # QVariant.Type enum
    String = int() # QVariant.Type enum
    StringList = int() # QVariant.Type enum
    ByteArray = int() # QVariant.Type enum
    BitArray = int() # QVariant.Type enum
    Date = int() # QVariant.Type enum
    Time = int() # QVariant.Type enum
    DateTime = int() # QVariant.Type enum
    Url = int() # QVariant.Type enum
    Locale = int() # QVariant.Type enum
    Rect = int() # QVariant.Type enum
    RectF = int() # QVariant.Type enum
    Size = int() # QVariant.Type enum
    SizeF = int() # QVariant.Type enum
    Line = int() # QVariant.Type enum
    LineF = int() # QVariant.Type enum
    Point = int() # QVariant.Type enum
    PointF = int() # QVariant.Type enum
    RegExp = int() # QVariant.Type enum
    Font = int() # QVariant.Type enum
    Pixmap = int() # QVariant.Type enum
    Brush = int() # QVariant.Type enum
    Color = int() # QVariant.Type enum
    Palette = int() # QVariant.Type enum
    Icon = int() # QVariant.Type enum
    Image = int() # QVariant.Type enum
    Polygon = int() # QVariant.Type enum
    Region = int() # QVariant.Type enum
    Bitmap = int() # QVariant.Type enum
    Cursor = int() # QVariant.Type enum
    SizePolicy = int() # QVariant.Type enum
    KeySequence = int() # QVariant.Type enum
    Pen = int() # QVariant.Type enum
    TextLength = int() # QVariant.Type enum
    TextFormat = int() # QVariant.Type enum
    Matrix = int() # QVariant.Type enum
    Transform = int() # QVariant.Type enum
    Hash = int() # QVariant.Type enum
    Matrix4x4 = int() # QVariant.Type enum
    Vector2D = int() # QVariant.Type enum
    Vector3D = int() # QVariant.Type enum
    Vector4D = int() # QVariant.Type enum
    Quaternion = int() # QVariant.Type enum
    EasingCurve = int() # QVariant.Type enum
    UserType = int() # QVariant.Type enum

    def __init__(self):
        """None QVariant.__init__(None self)"""
        return None
    def __init__(self, _type):
        """None QVariant.__init__(None self, Type _type)"""
        return None
    def __init__(self, _typeOrUserType, _copy):
        """None QVariant.__init__(None self, int _typeOrUserType, sip.voidptr _copy)"""
        return None
    def __init__(self, _other):
        """None QVariant.__init__(None self, QVariant _other)"""
        return None
    def __init__(self):
        """object QVariant.__init__(None self)"""
        return object()
    def toEasingCurve(self):
        """QEasingCurve QVariant.toEasingCurve(None self)"""
        return QEasingCurve()
    def toReal(self, _ok):
        """float QVariant.toReal(None self, bool _ok)"""
        return float()
    def toFloat(self, _ok):
        """float QVariant.toFloat(None self, bool _ok)"""
        return float()
    def __ne__(self, _v):
        """bool QVariant.__ne__(None self, QVariant _v)"""
        return bool()
    def __eq__(self, _v):
        """bool QVariant.__eq__(None self, QVariant _v)"""
        return bool()
    def data(self):
        """sip.voidptr QVariant.data(None self)"""
        return sip.voidptr()
    def nameToType(self, _name):
        """Type QVariant.nameToType(None self, str _name)"""
        return Type()
    def typeToName(self, _type):
        """str QVariant.typeToName(None self, Type _type)"""
        return str()
    def save(self, _ds):
        """None QVariant.save(None self, QDataStream _ds)"""
        return None
    def load(self, _ds):
        """None QVariant.load(None self, QDataStream _ds)"""
        return None
    def toPyObject(self):
        """object QVariant.toPyObject(None self)"""
        return object()
    def toRegExp(self):
        """QRegExp QVariant.toRegExp(None self)"""
        return QRegExp()
    def toLocale(self):
        """QLocale QVariant.toLocale(None self)"""
        return QLocale()
    def toUrl(self):
        """QUrl QVariant.toUrl(None self)"""
        return QUrl()
    def toRectF(self):
        """QRectF QVariant.toRectF(None self)"""
        return QRectF()
    def toRect(self):
        """QRect QVariant.toRect(None self)"""
        return QRect()
    def toLineF(self):
        """QLineF QVariant.toLineF(None self)"""
        return QLineF()
    def toLine(self):
        """QLine QVariant.toLine(None self)"""
        return QLine()
    def toSizeF(self):
        """QSizeF QVariant.toSizeF(None self)"""
        return QSizeF()
    def toSize(self):
        """QSize QVariant.toSize(None self)"""
        return QSize()
    def toPointF(self):
        """QPointF QVariant.toPointF(None self)"""
        return QPointF()
    def toPoint(self):
        """QPoint QVariant.toPoint(None self)"""
        return QPoint()
    def toHash(self):
        """dict-of-QString-QVariant QVariant.toHash(None self)"""
        return dict-of-QString-QVariant()
    def toMap(self):
        """dict-of-QString-QVariant QVariant.toMap(None self)"""
        return dict-of-QString-QVariant()
    def toList(self):
        """list-of-QVariant QVariant.toList(None self)"""
        return [QVariant()]
    def toDateTime(self):
        """QDateTime QVariant.toDateTime(None self)"""
        return QDateTime()
    def toTime(self):
        """QTime QVariant.toTime(None self)"""
        return QTime()
    def toDate(self):
        """QDate QVariant.toDate(None self)"""
        return QDate()
    def toChar(self):
        """QChar QVariant.toChar(None self)"""
        return QChar()
    def toStringList(self):
        """QStringList QVariant.toStringList(None self)"""
        return QStringList()
    def toString(self):
        """QString QVariant.toString(None self)"""
        return QString()
    def toBitArray(self):
        """QBitArray QVariant.toBitArray(None self)"""
        return QBitArray()
    def toByteArray(self):
        """QByteArray QVariant.toByteArray(None self)"""
        return QByteArray()
    def toDouble(self, _ok):
        """float QVariant.toDouble(None self, bool _ok)"""
        return float()
    def toBool(self):
        """bool QVariant.toBool(None self)"""
        return bool()
    def toULongLong(self, _ok):
        """int QVariant.toULongLong(None self, bool _ok)"""
        return int()
    def toLongLong(self, _ok):
        """int QVariant.toLongLong(None self, bool _ok)"""
        return int()
    def toUInt(self, _ok):
        """int QVariant.toUInt(None self, bool _ok)"""
        return int()
    def toInt(self, _ok):
        """int QVariant.toInt(None self, bool _ok)"""
        return int()
    def isDetached(self):
        """bool QVariant.isDetached(None self)"""
        return bool()
    def detach(self):
        """None QVariant.detach(None self)"""
        return None
    def clear(self):
        """None QVariant.clear(None self)"""
        return None
    def isNull(self):
        """bool QVariant.isNull(None self)"""
        return bool()
    def isValid(self):
        """bool QVariant.isValid(None self)"""
        return bool()
    def convert(self, _t):
        """bool QVariant.convert(None self, Type _t)"""
        return bool()
    def canConvert(self, _t):
        """bool QVariant.canConvert(None self, Type _t)"""
        return bool()
    def typeName(self):
        """str QVariant.typeName(None self)"""
        return str()
    def userType(self):
        """int QVariant.userType(None self)"""
        return int()
    def type(self):
        """Type QVariant.type(None self)"""
        return Type()
    def fromMap(self, _map):
        """QVariant QVariant.fromMap(None self, dict-of-QString-QVariant _map)"""
        return QVariant()
    def fromList(self, _list):
        """QVariant QVariant.fromList(None self, list-of-QVariant _list)"""
        return QVariant()


class QWaitCondition():
    """"""
    def __init__(self):
        """None QWaitCondition.__init__(None self)"""
        return None
    def wakeAll(self):
        """None QWaitCondition.wakeAll(None self)"""
        return None
    def wakeOne(self):
        """None QWaitCondition.wakeOne(None self)"""
        return None
    def wait(self, _mutex, _msecs):
        """bool QWaitCondition.wait(None self, QMutex _mutex, int _msecs)"""
        return bool()
    def wait(self, _readWriteLock, _msecs):
        """bool QWaitCondition.wait(None self, QReadWriteLock _readWriteLock, int _msecs)"""
        return bool()


class QXmlStreamAttribute():
    """"""
    def __init__(self):
        """None QXmlStreamAttribute.__init__(None self)"""
        return None
    def __init__(self, _qualifiedName, _value):
        """None QXmlStreamAttribute.__init__(None self, QString _qualifiedName, QString _value)"""
        return None
    def __init__(self, _namespaceUri, _name, _value):
        """None QXmlStreamAttribute.__init__(None self, QString _namespaceUri, QString _name, QString _value)"""
        return None
    def __init__(self):
        """QXmlStreamAttribute QXmlStreamAttribute.__init__(None self)"""
        return QXmlStreamAttribute()
    def __ne__(self, _other):
        """bool QXmlStreamAttribute.__ne__(None self, QXmlStreamAttribute _other)"""
        return bool()
    def __eq__(self, _other):
        """bool QXmlStreamAttribute.__eq__(None self, QXmlStreamAttribute _other)"""
        return bool()
    def isDefault(self):
        """bool QXmlStreamAttribute.isDefault(None self)"""
        return bool()
    def value(self):
        """QStringRef QXmlStreamAttribute.value(None self)"""
        return QStringRef()
    def prefix(self):
        """QStringRef QXmlStreamAttribute.prefix(None self)"""
        return QStringRef()
    def qualifiedName(self):
        """QStringRef QXmlStreamAttribute.qualifiedName(None self)"""
        return QStringRef()
    def name(self):
        """QStringRef QXmlStreamAttribute.name(None self)"""
        return QStringRef()
    def namespaceUri(self):
        """QStringRef QXmlStreamAttribute.namespaceUri(None self)"""
        return QStringRef()


class QXmlStreamAttributes():
    """"""
    def __init__(self):
        """None QXmlStreamAttributes.__init__(None self)"""
        return None
    def __init__(self):
        """QXmlStreamAttributes QXmlStreamAttributes.__init__(None self)"""
        return QXmlStreamAttributes()
    def __contains__(self, _value):
        """int QXmlStreamAttributes.__contains__(None self, QXmlStreamAttribute _value)"""
        return int()
    def __delitem__(self, _i):
        """None QXmlStreamAttributes.__delitem__(None self, int _i)"""
        return None
    def __delitem__(self, _slice):
        """None QXmlStreamAttributes.__delitem__(None self, slice _slice)"""
        return None
    def __setitem__(self, _i, _value):
        """None QXmlStreamAttributes.__setitem__(None self, int _i, QXmlStreamAttribute _value)"""
        return None
    def __setitem__(self, _slice, _list):
        """None QXmlStreamAttributes.__setitem__(None self, slice _slice, QXmlStreamAttributes _list)"""
        return None
    def __getitem__(self, _i):
        """QXmlStreamAttribute QXmlStreamAttributes.__getitem__(None self, int _i)"""
        return QXmlStreamAttribute()
    def __getitem__(self, _slice):
        """QXmlStreamAttributes QXmlStreamAttributes.__getitem__(None self, slice _slice)"""
        return QXmlStreamAttributes()
    def __eq__(self, _other):
        """bool QXmlStreamAttributes.__eq__(None self, QXmlStreamAttributes _other)"""
        return bool()
    def __iadd__(self, _other):
        """QXmlStreamAttributes QXmlStreamAttributes.__iadd__(None self, QXmlStreamAttributes _other)"""
        return QXmlStreamAttributes()
    def __iadd__(self, _value):
        """QXmlStreamAttributes QXmlStreamAttributes.__iadd__(None self, QXmlStreamAttribute _value)"""
        return QXmlStreamAttributes()
    def __ne__(self, _other):
        """bool QXmlStreamAttributes.__ne__(None self, QXmlStreamAttributes _other)"""
        return bool()
    def size(self):
        """int QXmlStreamAttributes.size(None self)"""
        return int()
    def replace(self, _i, _value):
        """None QXmlStreamAttributes.replace(None self, int _i, QXmlStreamAttribute _value)"""
        return None
    def remove(self, _i):
        """None QXmlStreamAttributes.remove(None self, int _i)"""
        return None
    def remove(self, _i, _count):
        """None QXmlStreamAttributes.remove(None self, int _i, int _count)"""
        return None
    def prepend(self, _value):
        """None QXmlStreamAttributes.prepend(None self, QXmlStreamAttribute _value)"""
        return None
    def lastIndexOf(self, _value, _from):
        """int QXmlStreamAttributes.lastIndexOf(None self, QXmlStreamAttribute _value, int _from)"""
        return int()
    def last(self):
        """QXmlStreamAttribute QXmlStreamAttributes.last(None self)"""
        return QXmlStreamAttribute()
    def isEmpty(self):
        """bool QXmlStreamAttributes.isEmpty(None self)"""
        return bool()
    def insert(self, _i, _value):
        """None QXmlStreamAttributes.insert(None self, int _i, QXmlStreamAttribute _value)"""
        return None
    def indexOf(self, _value, _from):
        """int QXmlStreamAttributes.indexOf(None self, QXmlStreamAttribute _value, int _from)"""
        return int()
    def first(self):
        """QXmlStreamAttribute QXmlStreamAttributes.first(None self)"""
        return QXmlStreamAttribute()
    def fill(self, _value, _size):
        """None QXmlStreamAttributes.fill(None self, QXmlStreamAttribute _value, int _size)"""
        return None
    def data(self):
        """sip.voidptr QXmlStreamAttributes.data(None self)"""
        return sip.voidptr()
    def __len__(self):
        """ QXmlStreamAttributes.__len__(None self)"""
        return ()
    def count(self, _value):
        """int QXmlStreamAttributes.count(None self, QXmlStreamAttribute _value)"""
        return int()
    def count(self):
        """int QXmlStreamAttributes.count(None self)"""
        return int()
    def contains(self, _value):
        """bool QXmlStreamAttributes.contains(None self, QXmlStreamAttribute _value)"""
        return bool()
    def clear(self):
        """None QXmlStreamAttributes.clear(None self)"""
        return None
    def at(self, _i):
        """QXmlStreamAttribute QXmlStreamAttributes.at(None self, int _i)"""
        return QXmlStreamAttribute()
    def hasAttribute(self, _qualifiedName):
        """bool QXmlStreamAttributes.hasAttribute(None self, QString _qualifiedName)"""
        return bool()
    def hasAttribute(self, _namespaceUri, _name):
        """bool QXmlStreamAttributes.hasAttribute(None self, QString _namespaceUri, QString _name)"""
        return bool()
    def append(self, _namespaceUri, _name, _value):
        """None QXmlStreamAttributes.append(None self, QString _namespaceUri, QString _name, QString _value)"""
        return None
    def append(self, _qualifiedName, _value):
        """None QXmlStreamAttributes.append(None self, QString _qualifiedName, QString _value)"""
        return None
    def append(self, _attribute):
        """None QXmlStreamAttributes.append(None self, QXmlStreamAttribute _attribute)"""
        return None
    def value(self, _namespaceUri, _name):
        """QStringRef QXmlStreamAttributes.value(None self, QString _namespaceUri, QString _name)"""
        return QStringRef()
    def value(self, _qualifiedName):
        """QStringRef QXmlStreamAttributes.value(None self, QString _qualifiedName)"""
        return QStringRef()


class QXmlStreamNamespaceDeclaration():
    """"""
    def __init__(self):
        """None QXmlStreamNamespaceDeclaration.__init__(None self)"""
        return None
    def __init__(self):
        """QXmlStreamNamespaceDeclaration QXmlStreamNamespaceDeclaration.__init__(None self)"""
        return QXmlStreamNamespaceDeclaration()
    def __init__(self, _prefix, _namespaceUri):
        """None QXmlStreamNamespaceDeclaration.__init__(None self, QString _prefix, QString _namespaceUri)"""
        return None
    def __ne__(self, _other):
        """bool QXmlStreamNamespaceDeclaration.__ne__(None self, QXmlStreamNamespaceDeclaration _other)"""
        return bool()
    def __eq__(self, _other):
        """bool QXmlStreamNamespaceDeclaration.__eq__(None self, QXmlStreamNamespaceDeclaration _other)"""
        return bool()
    def namespaceUri(self):
        """QStringRef QXmlStreamNamespaceDeclaration.namespaceUri(None self)"""
        return QStringRef()
    def prefix(self):
        """QStringRef QXmlStreamNamespaceDeclaration.prefix(None self)"""
        return QStringRef()


class QXmlStreamNotationDeclaration():
    """"""
    def __init__(self):
        """None QXmlStreamNotationDeclaration.__init__(None self)"""
        return None
    def __init__(self):
        """QXmlStreamNotationDeclaration QXmlStreamNotationDeclaration.__init__(None self)"""
        return QXmlStreamNotationDeclaration()
    def __ne__(self, _other):
        """bool QXmlStreamNotationDeclaration.__ne__(None self, QXmlStreamNotationDeclaration _other)"""
        return bool()
    def __eq__(self, _other):
        """bool QXmlStreamNotationDeclaration.__eq__(None self, QXmlStreamNotationDeclaration _other)"""
        return bool()
    def publicId(self):
        """QStringRef QXmlStreamNotationDeclaration.publicId(None self)"""
        return QStringRef()
    def systemId(self):
        """QStringRef QXmlStreamNotationDeclaration.systemId(None self)"""
        return QStringRef()
    def name(self):
        """QStringRef QXmlStreamNotationDeclaration.name(None self)"""
        return QStringRef()


class QXmlStreamEntityDeclaration():
    """"""
    def __init__(self):
        """None QXmlStreamEntityDeclaration.__init__(None self)"""
        return None
    def __init__(self):
        """QXmlStreamEntityDeclaration QXmlStreamEntityDeclaration.__init__(None self)"""
        return QXmlStreamEntityDeclaration()
    def __ne__(self, _other):
        """bool QXmlStreamEntityDeclaration.__ne__(None self, QXmlStreamEntityDeclaration _other)"""
        return bool()
    def __eq__(self, _other):
        """bool QXmlStreamEntityDeclaration.__eq__(None self, QXmlStreamEntityDeclaration _other)"""
        return bool()
    def value(self):
        """QStringRef QXmlStreamEntityDeclaration.value(None self)"""
        return QStringRef()
    def publicId(self):
        """QStringRef QXmlStreamEntityDeclaration.publicId(None self)"""
        return QStringRef()
    def systemId(self):
        """QStringRef QXmlStreamEntityDeclaration.systemId(None self)"""
        return QStringRef()
    def notationName(self):
        """QStringRef QXmlStreamEntityDeclaration.notationName(None self)"""
        return QStringRef()
    def name(self):
        """QStringRef QXmlStreamEntityDeclaration.name(None self)"""
        return QStringRef()


class QXmlStreamEntityResolver():
    """"""
    def __init__(self):
        """None QXmlStreamEntityResolver.__init__(None self)"""
        return None
    def __init__(self):
        """QXmlStreamEntityResolver QXmlStreamEntityResolver.__init__(None self)"""
        return QXmlStreamEntityResolver()
    def resolveUndeclaredEntity(self, _name):
        """QString QXmlStreamEntityResolver.resolveUndeclaredEntity(None self, QString _name)"""
        return QString()


class QXmlStreamReader():
    """"""
    ErrorOnUnexpectedElement = int() # QXmlStreamReader.ReadElementTextBehaviour enum
    IncludeChildElements = int() # QXmlStreamReader.ReadElementTextBehaviour enum
    SkipChildElements = int() # QXmlStreamReader.ReadElementTextBehaviour enum

    NoError = int() # QXmlStreamReader.Error enum
    UnexpectedElementError = int() # QXmlStreamReader.Error enum
    CustomError = int() # QXmlStreamReader.Error enum
    NotWellFormedError = int() # QXmlStreamReader.Error enum
    PrematureEndOfDocumentError = int() # QXmlStreamReader.Error enum

    NoToken = int() # QXmlStreamReader.TokenType enum
    Invalid = int() # QXmlStreamReader.TokenType enum
    StartDocument = int() # QXmlStreamReader.TokenType enum
    EndDocument = int() # QXmlStreamReader.TokenType enum
    StartElement = int() # QXmlStreamReader.TokenType enum
    EndElement = int() # QXmlStreamReader.TokenType enum
    Characters = int() # QXmlStreamReader.TokenType enum
    Comment = int() # QXmlStreamReader.TokenType enum
    DTD = int() # QXmlStreamReader.TokenType enum
    EntityReference = int() # QXmlStreamReader.TokenType enum
    ProcessingInstruction = int() # QXmlStreamReader.TokenType enum

    def __init__(self):
        """None QXmlStreamReader.__init__(None self)"""
        return None
    def __init__(self, _device):
        """None QXmlStreamReader.__init__(None self, QIODevice _device)"""
        return None
    def __init__(self, _data):
        """None QXmlStreamReader.__init__(None self, QByteArray _data)"""
        return None
    def __init__(self, _data):
        """None QXmlStreamReader.__init__(None self, QString _data)"""
        return None
    def skipCurrentElement(self):
        """None QXmlStreamReader.skipCurrentElement(None self)"""
        return None
    def readNextStartElement(self):
        """bool QXmlStreamReader.readNextStartElement(None self)"""
        return bool()
    def entityResolver(self):
        """QXmlStreamEntityResolver QXmlStreamReader.entityResolver(None self)"""
        return QXmlStreamEntityResolver()
    def setEntityResolver(self, _resolver):
        """None QXmlStreamReader.setEntityResolver(None self, QXmlStreamEntityResolver _resolver)"""
        return None
    def hasError(self):
        """bool QXmlStreamReader.hasError(None self)"""
        return bool()
    def error(self):
        """QXmlStreamReader.Error QXmlStreamReader.error(None self)"""
        return QXmlStreamReader.Error()
    def errorString(self):
        """QString QXmlStreamReader.errorString(None self)"""
        return QString()
    def raiseError(self, _message):
        """None QXmlStreamReader.raiseError(None self, QString _message)"""
        return None
    def dtdSystemId(self):
        """QStringRef QXmlStreamReader.dtdSystemId(None self)"""
        return QStringRef()
    def dtdPublicId(self):
        """QStringRef QXmlStreamReader.dtdPublicId(None self)"""
        return QStringRef()
    def dtdName(self):
        """QStringRef QXmlStreamReader.dtdName(None self)"""
        return QStringRef()
    def entityDeclarations(self):
        """list-of-QXmlStreamEntityDeclaration QXmlStreamReader.entityDeclarations(None self)"""
        return [QXmlStreamEntityDeclaration()]
    def notationDeclarations(self):
        """list-of-QXmlStreamNotationDeclaration QXmlStreamReader.notationDeclarations(None self)"""
        return [QXmlStreamNotationDeclaration()]
    def addExtraNamespaceDeclarations(self, _extraNamespaceDeclaractions):
        """None QXmlStreamReader.addExtraNamespaceDeclarations(None self, list-of-QXmlStreamNamespaceDeclaration _extraNamespaceDeclaractions)"""
        return None
    def addExtraNamespaceDeclaration(self, _extraNamespaceDeclaraction):
        """None QXmlStreamReader.addExtraNamespaceDeclaration(None self, QXmlStreamNamespaceDeclaration _extraNamespaceDeclaraction)"""
        return None
    def namespaceDeclarations(self):
        """list-of-QXmlStreamNamespaceDeclaration QXmlStreamReader.namespaceDeclarations(None self)"""
        return [QXmlStreamNamespaceDeclaration()]
    def text(self):
        """QStringRef QXmlStreamReader.text(None self)"""
        return QStringRef()
    def processingInstructionData(self):
        """QStringRef QXmlStreamReader.processingInstructionData(None self)"""
        return QStringRef()
    def processingInstructionTarget(self):
        """QStringRef QXmlStreamReader.processingInstructionTarget(None self)"""
        return QStringRef()
    def prefix(self):
        """QStringRef QXmlStreamReader.prefix(None self)"""
        return QStringRef()
    def qualifiedName(self):
        """QStringRef QXmlStreamReader.qualifiedName(None self)"""
        return QStringRef()
    def namespaceUri(self):
        """QStringRef QXmlStreamReader.namespaceUri(None self)"""
        return QStringRef()
    def name(self):
        """QStringRef QXmlStreamReader.name(None self)"""
        return QStringRef()
    def readElementText(self):
        """QString QXmlStreamReader.readElementText(None self)"""
        return QString()
    def readElementText(self, _behaviour):
        """QString QXmlStreamReader.readElementText(None self, QXmlStreamReader.ReadElementTextBehaviour _behaviour)"""
        return QString()
    def attributes(self):
        """QXmlStreamAttributes QXmlStreamReader.attributes(None self)"""
        return QXmlStreamAttributes()
    def characterOffset(self):
        """int QXmlStreamReader.characterOffset(None self)"""
        return int()
    def columnNumber(self):
        """int QXmlStreamReader.columnNumber(None self)"""
        return int()
    def lineNumber(self):
        """int QXmlStreamReader.lineNumber(None self)"""
        return int()
    def documentEncoding(self):
        """QStringRef QXmlStreamReader.documentEncoding(None self)"""
        return QStringRef()
    def documentVersion(self):
        """QStringRef QXmlStreamReader.documentVersion(None self)"""
        return QStringRef()
    def isStandaloneDocument(self):
        """bool QXmlStreamReader.isStandaloneDocument(None self)"""
        return bool()
    def isProcessingInstruction(self):
        """bool QXmlStreamReader.isProcessingInstruction(None self)"""
        return bool()
    def isEntityReference(self):
        """bool QXmlStreamReader.isEntityReference(None self)"""
        return bool()
    def isDTD(self):
        """bool QXmlStreamReader.isDTD(None self)"""
        return bool()
    def isComment(self):
        """bool QXmlStreamReader.isComment(None self)"""
        return bool()
    def isCDATA(self):
        """bool QXmlStreamReader.isCDATA(None self)"""
        return bool()
    def isWhitespace(self):
        """bool QXmlStreamReader.isWhitespace(None self)"""
        return bool()
    def isCharacters(self):
        """bool QXmlStreamReader.isCharacters(None self)"""
        return bool()
    def isEndElement(self):
        """bool QXmlStreamReader.isEndElement(None self)"""
        return bool()
    def isStartElement(self):
        """bool QXmlStreamReader.isStartElement(None self)"""
        return bool()
    def isEndDocument(self):
        """bool QXmlStreamReader.isEndDocument(None self)"""
        return bool()
    def isStartDocument(self):
        """bool QXmlStreamReader.isStartDocument(None self)"""
        return bool()
    def namespaceProcessing(self):
        """bool QXmlStreamReader.namespaceProcessing(None self)"""
        return bool()
    def setNamespaceProcessing(self):
        """bool QXmlStreamReader.setNamespaceProcessing(None self)"""
        return bool()
    def tokenString(self):
        """QString QXmlStreamReader.tokenString(None self)"""
        return QString()
    def tokenType(self):
        """QXmlStreamReader.TokenType QXmlStreamReader.tokenType(None self)"""
        return QXmlStreamReader.TokenType()
    def readNext(self):
        """QXmlStreamReader.TokenType QXmlStreamReader.readNext(None self)"""
        return QXmlStreamReader.TokenType()
    def atEnd(self):
        """bool QXmlStreamReader.atEnd(None self)"""
        return bool()
    def clear(self):
        """None QXmlStreamReader.clear(None self)"""
        return None
    def addData(self, _data):
        """None QXmlStreamReader.addData(None self, QByteArray _data)"""
        return None
    def addData(self, _data):
        """None QXmlStreamReader.addData(None self, QString _data)"""
        return None
    def device(self):
        """QIODevice QXmlStreamReader.device(None self)"""
        return QIODevice()
    def setDevice(self, _device):
        """None QXmlStreamReader.setDevice(None self, QIODevice _device)"""
        return None


class QXmlStreamWriter():
    """"""
    def __init__(self):
        """None QXmlStreamWriter.__init__(None self)"""
        return None
    def __init__(self, _device):
        """None QXmlStreamWriter.__init__(None self, QIODevice _device)"""
        return None
    def __init__(self, _array):
        """None QXmlStreamWriter.__init__(None self, QByteArray _array)"""
        return None
    def __init__(self, _string):
        """None QXmlStreamWriter.__init__(None self, QString _string)"""
        return None
    def writeCurrentToken(self, _reader):
        """None QXmlStreamWriter.writeCurrentToken(None self, QXmlStreamReader _reader)"""
        return None
    def writeStartElement(self, _qualifiedName):
        """None QXmlStreamWriter.writeStartElement(None self, QString _qualifiedName)"""
        return None
    def writeStartElement(self, _namespaceUri, _name):
        """None QXmlStreamWriter.writeStartElement(None self, QString _namespaceUri, QString _name)"""
        return None
    def writeStartDocument(self):
        """None QXmlStreamWriter.writeStartDocument(None self)"""
        return None
    def writeStartDocument(self, _version):
        """None QXmlStreamWriter.writeStartDocument(None self, QString _version)"""
        return None
    def writeStartDocument(self, _version, _standalone):
        """None QXmlStreamWriter.writeStartDocument(None self, QString _version, bool _standalone)"""
        return None
    def writeProcessingInstruction(self, _target, _data):
        """None QXmlStreamWriter.writeProcessingInstruction(None self, QString _target, QString _data)"""
        return None
    def writeDefaultNamespace(self, _namespaceUri):
        """None QXmlStreamWriter.writeDefaultNamespace(None self, QString _namespaceUri)"""
        return None
    def writeNamespace(self, _namespaceUri, _prefix):
        """None QXmlStreamWriter.writeNamespace(None self, QString _namespaceUri, QString _prefix)"""
        return None
    def writeEntityReference(self, _name):
        """None QXmlStreamWriter.writeEntityReference(None self, QString _name)"""
        return None
    def writeEndElement(self):
        """None QXmlStreamWriter.writeEndElement(None self)"""
        return None
    def writeEndDocument(self):
        """None QXmlStreamWriter.writeEndDocument(None self)"""
        return None
    def writeTextElement(self, _qualifiedName, _text):
        """None QXmlStreamWriter.writeTextElement(None self, QString _qualifiedName, QString _text)"""
        return None
    def writeTextElement(self, _namespaceUri, _name, _text):
        """None QXmlStreamWriter.writeTextElement(None self, QString _namespaceUri, QString _name, QString _text)"""
        return None
    def writeEmptyElement(self, _qualifiedName):
        """None QXmlStreamWriter.writeEmptyElement(None self, QString _qualifiedName)"""
        return None
    def writeEmptyElement(self, _namespaceUri, _name):
        """None QXmlStreamWriter.writeEmptyElement(None self, QString _namespaceUri, QString _name)"""
        return None
    def writeDTD(self, _dtd):
        """None QXmlStreamWriter.writeDTD(None self, QString _dtd)"""
        return None
    def writeComment(self, _text):
        """None QXmlStreamWriter.writeComment(None self, QString _text)"""
        return None
    def writeCharacters(self, _text):
        """None QXmlStreamWriter.writeCharacters(None self, QString _text)"""
        return None
    def writeCDATA(self, _text):
        """None QXmlStreamWriter.writeCDATA(None self, QString _text)"""
        return None
    def writeAttributes(self, _attributes):
        """None QXmlStreamWriter.writeAttributes(None self, QXmlStreamAttributes _attributes)"""
        return None
    def writeAttribute(self, _qualifiedName, _value):
        """None QXmlStreamWriter.writeAttribute(None self, QString _qualifiedName, QString _value)"""
        return None
    def writeAttribute(self, _namespaceUri, _name, _value):
        """None QXmlStreamWriter.writeAttribute(None self, QString _namespaceUri, QString _name, QString _value)"""
        return None
    def writeAttribute(self, _attribute):
        """None QXmlStreamWriter.writeAttribute(None self, QXmlStreamAttribute _attribute)"""
        return None
    def autoFormattingIndent(self):
        """int QXmlStreamWriter.autoFormattingIndent(None self)"""
        return int()
    def setAutoFormattingIndent(self, _spaces):
        """None QXmlStreamWriter.setAutoFormattingIndent(None self, int _spaces)"""
        return None
    def autoFormatting(self):
        """bool QXmlStreamWriter.autoFormatting(None self)"""
        return bool()
    def setAutoFormatting(self):
        """bool QXmlStreamWriter.setAutoFormatting(None self)"""
        return bool()
    def codec(self):
        """QTextCodec QXmlStreamWriter.codec(None self)"""
        return QTextCodec()
    def setCodec(self, _codec):
        """None QXmlStreamWriter.setCodec(None self, QTextCodec _codec)"""
        return None
    def setCodec(self, _codecName):
        """None QXmlStreamWriter.setCodec(None self, str _codecName)"""
        return None
    def device(self):
        """QIODevice QXmlStreamWriter.device(None self)"""
        return QIODevice()
    def setDevice(self, _device):
        """None QXmlStreamWriter.setDevice(None self, QIODevice _device)"""
        return None


class QPyNullVariant():
    """"""
    def __init__(self, _type):
        """None QPyNullVariant.__init__(None self, object _type)"""
        return None
    def isNull(self):
        """bool QPyNullVariant.isNull(None self)"""
        return bool()
    def typeName(self):
        """str QPyNullVariant.typeName(None self)"""
        return str()
    def userType(self):
        """int QPyNullVariant.userType(None self)"""
        return int()
    def type(self):
        """Type QPyNullVariant.type(None self)"""
        return Type()


PYQT_VERSION = None # int member

PYQT_VERSION_STR = None # str member

QT_VERSION = None # int member

QT_VERSION_STR = None # str member

def qSetRealNumberPrecision(_precision):
    """QTextStreamManipulator .qSetRealNumberPrecision(int _precision)"""
    return QTextStreamManipulator()

def qSetPadChar(_ch):
    """QTextStreamManipulator .qSetPadChar(QChar _ch)"""
    return QTextStreamManipulator()

def qSetFieldWidth(_width):
    """QTextStreamManipulator .qSetFieldWidth(int _width)"""
    return QTextStreamManipulator()

def ws(_s):
    """QTextStream .ws(QTextStream _s)"""
    return QTextStream()

def bom(_s):
    """QTextStream .bom(QTextStream _s)"""
    return QTextStream()

def reset(_s):
    """QTextStream .reset(QTextStream _s)"""
    return QTextStream()

def flush(_s):
    """QTextStream .flush(QTextStream _s)"""
    return QTextStream()

def endl(_s):
    """QTextStream .endl(QTextStream _s)"""
    return QTextStream()

def center(_s):
    """QTextStream .center(QTextStream _s)"""
    return QTextStream()

def right(_s):
    """QTextStream .right(QTextStream _s)"""
    return QTextStream()

def left(_s):
    """QTextStream .left(QTextStream _s)"""
    return QTextStream()

def scientific(_s):
    """QTextStream .scientific(QTextStream _s)"""
    return QTextStream()

def fixed(_s):
    """QTextStream .fixed(QTextStream _s)"""
    return QTextStream()

def lowercasedigits(_s):
    """QTextStream .lowercasedigits(QTextStream _s)"""
    return QTextStream()

def lowercasebase(_s):
    """QTextStream .lowercasebase(QTextStream _s)"""
    return QTextStream()

def uppercasedigits(_s):
    """QTextStream .uppercasedigits(QTextStream _s)"""
    return QTextStream()

def uppercasebase(_s):
    """QTextStream .uppercasebase(QTextStream _s)"""
    return QTextStream()

def noforcepoint(_s):
    """QTextStream .noforcepoint(QTextStream _s)"""
    return QTextStream()

def noforcesign(_s):
    """QTextStream .noforcesign(QTextStream _s)"""
    return QTextStream()

def noshowbase(_s):
    """QTextStream .noshowbase(QTextStream _s)"""
    return QTextStream()

def forcepoint(_s):
    """QTextStream .forcepoint(QTextStream _s)"""
    return QTextStream()

def forcesign(_s):
    """QTextStream .forcesign(QTextStream _s)"""
    return QTextStream()

def showbase(_s):
    """QTextStream .showbase(QTextStream _s)"""
    return QTextStream()

def hex_(_s):
    """QTextStream .hex_(QTextStream _s)"""
    return QTextStream()

def hex(_s):
    """QTextStream .hex(QTextStream _s)"""
    return QTextStream()

def dec(_s):
    """QTextStream .dec(QTextStream _s)"""
    return QTextStream()

def oct_(_s):
    """QTextStream .oct_(QTextStream _s)"""
    return QTextStream()

def oct(_s):
    """QTextStream .oct(QTextStream _s)"""
    return QTextStream()

def bin_(_s):
    """QTextStream .bin_(QTextStream _s)"""
    return QTextStream()

def bin(_s):
    """QTextStream .bin(QTextStream _s)"""
    return QTextStream()

def Q_RETURN_ARG(_type):
    """QGenericReturnArgument .Q_RETURN_ARG(object _type)"""
    return QGenericReturnArgument()

def Q_ARG(_type, _data):
    """QGenericArgument .Q_ARG(object _type, object _data)"""
    return QGenericArgument()

def pyqtSignature(_signature, _result):
    """object .pyqtSignature(str _signature, str _result)"""
    return object()

def pyqtSlot(_signature, _name, _result):
    """object .pyqtSlot(str _signature, str _name, str _result)"""
    return object()

def SIGNAL():
    """str .SIGNAL()"""
    return str()

def SLOT():
    """str .SLOT()"""
    return str()

def QT_TRANSLATE_NOOP():
    """str .QT_TRANSLATE_NOOP()"""
    return str()

def QT_TR_NOOP_UTF8():
    """str .QT_TR_NOOP_UTF8()"""
    return str()

def QT_TR_NOOP():
    """str .QT_TR_NOOP()"""
    return str()

def Q_FLAGS(*args):
    """ .Q_FLAGS(... *args)"""
    return ()

def Q_ENUMS(*args):
    """ .Q_ENUMS(... *args)"""
    return ()

def qQNaN():
    """float .qQNaN()"""
    return float()

def qSNaN():
    """float .qSNaN()"""
    return float()

def qInf():
    """float .qInf()"""
    return float()

def qIsNaN(_d):
    """bool .qIsNaN(float _d)"""
    return bool()

def qIsFinite(_d):
    """bool .qIsFinite(float _d)"""
    return bool()

def qIsInf(_d):
    """bool .qIsInf(float _d)"""
    return bool()

def pyqtRestoreInputHook():
    """None .pyqtRestoreInputHook()"""
    return None

def pyqtRemoveInputHook():
    """None .pyqtRemoveInputHook()"""
    return None

def qRemovePostRoutine():
    """callable .qRemovePostRoutine()"""
    return callable()

def qAddPostRoutine():
    """callable .qAddPostRoutine()"""
    return callable()

def qUncompress(_data):
    """QByteArray .qUncompress(QByteArray _data)"""
    return QByteArray()

def qCompress(_data, _compressionLevel):
    """QByteArray .qCompress(QByteArray _data, int _compressionLevel)"""
    return QByteArray()

def qChecksum(_s):
    """int .qChecksum(str _s)"""
    return int()

def qSwap(_value1, _value2):
    """None .qSwap(QBitArray _value1, QBitArray _value2)"""
    return None

def qSwap(_value1, _value2):
    """None .qSwap(QByteArray _value1, QByteArray _value2)"""
    return None

def qSwap(_value1, _value2):
    """None .qSwap(QString _value1, QString _value2)"""
    return None

def qSwap(_value1, _value2):
    """None .qSwap(QUrl _value1, QUrl _value2)"""
    return None

def qSwap(_value1, _value2):
    """None .qSwap(QVariant _value1, QVariant _value2)"""
    return None

def qrand():
    """int .qrand()"""
    return int()

def qsrand(_seed):
    """None .qsrand(int _seed)"""
    return None

def qIsNull(_d):
    """bool .qIsNull(float _d)"""
    return bool()

def qFuzzyCompare(_p1, _p2):
    """bool .qFuzzyCompare(float _p1, float _p2)"""
    return bool()

def qUnregisterResourceData():
    """str .qUnregisterResourceData()"""
    return str()

def qRegisterResourceData():
    """str .qRegisterResourceData()"""
    return str()

def qInstallMsgHandler():
    """callable .qInstallMsgHandler()"""
    return callable()

def qErrnoWarning(_code, _msg):
    """None .qErrnoWarning(int _code, str _msg)"""
    return None

def qErrnoWarning(_msg):
    """None .qErrnoWarning(str _msg)"""
    return None

def qFatal():
    """str .qFatal()"""
    return str()

def qCritical():
    """str .qCritical()"""
    return str()

def qWarning():
    """str .qWarning()"""
    return str()

def qDebug():
    """str .qDebug()"""
    return str()

def qSharedBuild():
    """bool .qSharedBuild()"""
    return bool()

def qVersion():
    """str .qVersion()"""
    return str()

def qRound64(_d):
    """int .qRound64(float _d)"""
    return int()

def qRound(_d):
    """int .qRound(float _d)"""
    return int()

def qAbs(_t):
    """float .qAbs(float _t)"""
    return float()

