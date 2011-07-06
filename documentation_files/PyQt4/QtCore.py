class QSysInfo():
    """"""
    BigEndian = int() # QSysInfo.Endian enum
    LittleEndian = int() # QSysInfo.Endian enum
    ByteOrder = int() # QSysInfo.Endian enum

    WordSize = int() # QSysInfo.Sizes enum

    def __init__():
        """None QSysInfo.__init__()"""
        return None
    def __init__():
        """QSysInfo QSysInfo.__init__()"""
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
    def __init__(_parent):
        """None QObject.__init__(QObject _parent)"""
        return None
    def disconnectNotify(_signal):
        """None QObject.disconnectNotify(SIGNAL() _signal)"""
        return None
    def connectNotify(_signal):
        """None QObject.connectNotify(SIGNAL() _signal)"""
        return None
    def customEvent():
        """QEvent QObject.customEvent()"""
        return QEvent()
    def childEvent():
        """QChildEvent QObject.childEvent()"""
        return QChildEvent()
    def timerEvent():
        """QTimerEvent QObject.timerEvent()"""
        return QTimerEvent()
    def receivers(_signal):
        """int QObject.receivers(SIGNAL() _signal)"""
        return int()
    def sender():
        """QObject QObject.sender()"""
        return QObject()
    def deleteLater():
        """None QObject.deleteLater()"""
        return None
    def inherits(_classname):
        """bool QObject.inherits(str _classname)"""
        return bool()
    def parent():
        """QObject QObject.parent()"""
        return QObject()
    def property(_name):
        """QVariant QObject.property(str _name)"""
        return QVariant()
    def setProperty(_name, _value):
        """bool QObject.setProperty(str _name, QVariant _value)"""
        return bool()
    def dynamicPropertyNames():
        """list-of-QByteArray QObject.dynamicPropertyNames()"""
        return [QByteArray()]
    def dumpObjectTree():
        """None QObject.dumpObjectTree()"""
        return None
    def dumpObjectInfo():
        """None QObject.dumpObjectInfo()"""
        return None
    def disconnect():
        """SLOT() QObject.disconnect()"""
        return SLOT()()
    def disconnect():
        """callable QObject.disconnect()"""
        return callable()
    def connect():
        """Qt.ConnectionType QObject.connect()"""
        return Qt.ConnectionType()
    def connect():
        """Qt.ConnectionType QObject.connect()"""
        return Qt.ConnectionType()
    def connect():
        """Qt.ConnectionType QObject.connect()"""
        return Qt.ConnectionType()
    def removeEventFilter():
        """QObject QObject.removeEventFilter()"""
        return QObject()
    def installEventFilter():
        """QObject QObject.installEventFilter()"""
        return QObject()
    def setParent():
        """QObject QObject.setParent()"""
        return QObject()
    def children():
        """list-of-QObject QObject.children()"""
        return [QObject()]
    def killTimer(_id):
        """None QObject.killTimer(int _id)"""
        return None
    def startTimer(_interval):
        """int QObject.startTimer(int _interval)"""
        return int()
    def moveToThread(_thread):
        """None QObject.moveToThread(QThread _thread)"""
        return None
    def thread():
        """QThread QObject.thread()"""
        return QThread()
    def blockSignals(_b):
        """bool QObject.blockSignals(bool _b)"""
        return bool()
    def signalsBlocked():
        """bool QObject.signalsBlocked()"""
        return bool()
    def isWidgetType():
        """bool QObject.isWidgetType()"""
        return bool()
    def setObjectName(_name):
        """None QObject.setObjectName(QString _name)"""
        return None
    def objectName():
        """QString QObject.objectName()"""
        return QString()
    def emit(*args):
        """SIGNAL() QObject.emit(... *args)"""
        return SIGNAL()()
    def findChildren(_type, _name):
        """list-of-QObject QObject.findChildren(type _type, QString _name)"""
        return [QObject()]
    def findChildren(_type, _regExp):
        """list-of-QObject QObject.findChildren(type _type, QRegExp _regExp)"""
        return [QObject()]
    def findChild(_type, _name):
        """QObject QObject.findChild(type _type, QString _name)"""
        return QObject()
    def trUtf8(_sourceText, _disambiguation, _n):
        """QString QObject.trUtf8(str _sourceText, str _disambiguation, int _n)"""
        return QString()
    def tr(_sourceText, _disambiguation, _n):
        """QString QObject.tr(str _sourceText, str _disambiguation, int _n)"""
        return QString()
    def eventFilter():
        """QEvent QObject.eventFilter()"""
        return QEvent()
    def event():
        """QEvent QObject.event()"""
        return QEvent()
    def __getattr__(_name):
        """object QObject.__getattr__(str _name)"""
        return object()
    def pyqtConfigure():
        """object QObject.pyqtConfigure()"""
        return object()
    def metaObject():
        """QMetaObject QObject.metaObject()"""
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

    def __init__(_parent):
        """None QAbstractAnimation.__init__(QObject _parent)"""
        return None
    def updateDirection(_direction):
        """None QAbstractAnimation.updateDirection(QAbstractAnimation.Direction _direction)"""
        return None
    def updateState(_newState, _oldState):
        """None QAbstractAnimation.updateState(QAbstractAnimation.State _newState, QAbstractAnimation.State _oldState)"""
        return None
    def updateCurrentTime(_currentTime):
        """abstract None QAbstractAnimation.updateCurrentTime(int _currentTime)"""
        return None
    def event(_event):
        """bool QAbstractAnimation.event(QEvent _event)"""
        return bool()
    def setCurrentTime(_msecs):
        """None QAbstractAnimation.setCurrentTime(int _msecs)"""
        return None
    def stop():
        """None QAbstractAnimation.stop()"""
        return None
    def setPaused():
        """bool QAbstractAnimation.setPaused()"""
        return bool()
    def resume():
        """None QAbstractAnimation.resume()"""
        return None
    def pause():
        """None QAbstractAnimation.pause()"""
        return None
    def start(_policy):
        """None QAbstractAnimation.start(QAbstractAnimation.DeletionPolicy _policy)"""
        return None
    def totalDuration():
        """int QAbstractAnimation.totalDuration()"""
        return int()
    def duration():
        """abstract int QAbstractAnimation.duration()"""
        return int()
    def currentLoop():
        """int QAbstractAnimation.currentLoop()"""
        return int()
    def setLoopCount(_loopCount):
        """None QAbstractAnimation.setLoopCount(int _loopCount)"""
        return None
    def loopCount():
        """int QAbstractAnimation.loopCount()"""
        return int()
    def currentLoopTime():
        """int QAbstractAnimation.currentLoopTime()"""
        return int()
    def currentTime():
        """int QAbstractAnimation.currentTime()"""
        return int()
    def setDirection(_direction):
        """None QAbstractAnimation.setDirection(QAbstractAnimation.Direction _direction)"""
        return None
    def direction():
        """QAbstractAnimation.Direction QAbstractAnimation.direction()"""
        return QAbstractAnimation.Direction()
    def group():
        """QAnimationGroup QAbstractAnimation.group()"""
        return QAnimationGroup()
    def state():
        """QAbstractAnimation.State QAbstractAnimation.state()"""
        return QAbstractAnimation.State()


class QAbstractEventDispatcher(QObject):
    """"""
    def __init__(_parent):
        """None QAbstractEventDispatcher.__init__(QObject _parent)"""
        return None
    def closingDown():
        """None QAbstractEventDispatcher.closingDown()"""
        return None
    def startingUp():
        """None QAbstractEventDispatcher.startingUp()"""
        return None
    def flush():
        """abstract None QAbstractEventDispatcher.flush()"""
        return None
    def interrupt():
        """abstract None QAbstractEventDispatcher.interrupt()"""
        return None
    def wakeUp():
        """abstract None QAbstractEventDispatcher.wakeUp()"""
        return None
    def registeredTimers(_object):
        """abstract list-of-tuple-of-int-int QAbstractEventDispatcher.registeredTimers(QObject _object)"""
        return [tuple-of-int-int()]
    def unregisterTimers(_object):
        """abstract bool QAbstractEventDispatcher.unregisterTimers(QObject _object)"""
        return bool()
    def unregisterTimer(_timerId):
        """abstract bool QAbstractEventDispatcher.unregisterTimer(int _timerId)"""
        return bool()
    def registerTimer(_interval, _object):
        """int QAbstractEventDispatcher.registerTimer(int _interval, QObject _object)"""
        return int()
    def registerTimer(_timerId, _interval, _object):
        """abstract None QAbstractEventDispatcher.registerTimer(int _timerId, int _interval, QObject _object)"""
        return None
    def unregisterSocketNotifier(_notifier):
        """abstract None QAbstractEventDispatcher.unregisterSocketNotifier(QSocketNotifier _notifier)"""
        return None
    def registerSocketNotifier(_notifier):
        """abstract None QAbstractEventDispatcher.registerSocketNotifier(QSocketNotifier _notifier)"""
        return None
    def hasPendingEvents():
        """abstract bool QAbstractEventDispatcher.hasPendingEvents()"""
        return bool()
    def processEvents(_flags):
        """abstract bool QAbstractEventDispatcher.processEvents(QEventLoop.ProcessEventsFlags _flags)"""
        return bool()
    def instance(_thread):
        """QAbstractEventDispatcher QAbstractEventDispatcher.instance(QThread _thread)"""
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

    def __init__():
        """None QAbstractFileEngine.__init__()"""
        return None
    def setError(_error, _str):
        """None QAbstractFileEngine.setError(QFile.FileError _error, QString _str)"""
        return None
    def unmap(_ptr):
        """bool QAbstractFileEngine.unmap(sip.voidptr _ptr)"""
        return bool()
    def map(_offset, _size, _flags):
        """sip.voidptr QAbstractFileEngine.map(int _offset, int _size, QFile.MemoryMapFlags _flags)"""
        return sip.voidptr()
    def create(_fileName):
        """QAbstractFileEngine QAbstractFileEngine.create(QString _fileName)"""
        return QAbstractFileEngine()
    def errorString():
        """QString QAbstractFileEngine.errorString()"""
        return QString()
    def error():
        """QFile.FileError QAbstractFileEngine.error()"""
        return QFile.FileError()
    def write(_data):
        """int QAbstractFileEngine.write(str _data)"""
        return int()
    def readLine(_maxlen):
        """str QAbstractFileEngine.readLine(int _maxlen)"""
        return str()
    def read(_maxlen):
        """str QAbstractFileEngine.read(int _maxlen)"""
        return str()
    def handle():
        """int QAbstractFileEngine.handle()"""
        return int()
    def setFileName(_file):
        """None QAbstractFileEngine.setFileName(QString _file)"""
        return None
    def fileTime(_time):
        """QDateTime QAbstractFileEngine.fileTime(QAbstractFileEngine.FileTime _time)"""
        return QDateTime()
    def owner():
        """QAbstractFileEngine.FileOwner QAbstractFileEngine.owner()"""
        return QAbstractFileEngine.FileOwner()
    def ownerId():
        """QAbstractFileEngine.FileOwner QAbstractFileEngine.ownerId()"""
        return QAbstractFileEngine.FileOwner()
    def fileName(_file):
        """QString QAbstractFileEngine.fileName(QAbstractFileEngine.FileName _file)"""
        return QString()
    def setPermissions(_perms):
        """bool QAbstractFileEngine.setPermissions(int _perms)"""
        return bool()
    def fileFlags(_type):
        """QAbstractFileEngine.FileFlags QAbstractFileEngine.fileFlags(QAbstractFileEngine.FileFlags _type)"""
        return QAbstractFileEngine.FileFlags()
    def entryList(_filters, _filterNames):
        """QStringList QAbstractFileEngine.entryList(QDir.Filters _filters, QStringList _filterNames)"""
        return QStringList()
    def isRelativePath():
        """bool QAbstractFileEngine.isRelativePath()"""
        return bool()
    def caseSensitive():
        """bool QAbstractFileEngine.caseSensitive()"""
        return bool()
    def setSize(_size):
        """bool QAbstractFileEngine.setSize(int _size)"""
        return bool()
    def rmdir(_dirName, _recurseParentDirectories):
        """bool QAbstractFileEngine.rmdir(QString _dirName, bool _recurseParentDirectories)"""
        return bool()
    def mkdir(_dirName, _createParentDirectories):
        """bool QAbstractFileEngine.mkdir(QString _dirName, bool _createParentDirectories)"""
        return bool()
    def link(_newName):
        """bool QAbstractFileEngine.link(QString _newName)"""
        return bool()
    def rename(_newName):
        """bool QAbstractFileEngine.rename(QString _newName)"""
        return bool()
    def copy(_newName):
        """bool QAbstractFileEngine.copy(QString _newName)"""
        return bool()
    def remove():
        """bool QAbstractFileEngine.remove()"""
        return bool()
    def isSequential():
        """bool QAbstractFileEngine.isSequential()"""
        return bool()
    def seek(_pos):
        """bool QAbstractFileEngine.seek(int _pos)"""
        return bool()
    def pos():
        """int QAbstractFileEngine.pos()"""
        return int()
    def size():
        """int QAbstractFileEngine.size()"""
        return int()
    def flush():
        """bool QAbstractFileEngine.flush()"""
        return bool()
    def close():
        """bool QAbstractFileEngine.close()"""
        return bool()
    def open(_openMode):
        """bool QAbstractFileEngine.open(QIODevice.OpenMode _openMode)"""
        return bool()
    def atEnd():
        """bool QAbstractFileEngine.atEnd()"""
        return bool()


class QAbstractFileEngineHandler():
    """"""
    def __init__():
        """None QAbstractFileEngineHandler.__init__()"""
        return None
    def __init__():
        """QAbstractFileEngineHandler QAbstractFileEngineHandler.__init__()"""
        return QAbstractFileEngineHandler()
    def create(_fileName):
        """abstract QAbstractFileEngine QAbstractFileEngineHandler.create(QString _fileName)"""
        return QAbstractFileEngine()


class QAbstractFileEngineIterator():
    """"""
    def __init__(_filters, _nameFilters):
        """None QAbstractFileEngineIterator.__init__(QDir.Filters _filters, QStringList _nameFilters)"""
        return None
    def currentFilePath():
        """QString QAbstractFileEngineIterator.currentFilePath()"""
        return QString()
    def currentFileInfo():
        """QFileInfo QAbstractFileEngineIterator.currentFileInfo()"""
        return QFileInfo()
    def currentFileName():
        """abstract QString QAbstractFileEngineIterator.currentFileName()"""
        return QString()
    def filters():
        """QDir.Filters QAbstractFileEngineIterator.filters()"""
        return QDir.Filters()
    def nameFilters():
        """QStringList QAbstractFileEngineIterator.nameFilters()"""
        return QStringList()
    def path():
        """QString QAbstractFileEngineIterator.path()"""
        return QString()
    def hasNext():
        """abstract bool QAbstractFileEngineIterator.hasNext()"""
        return bool()
    def next():
        """abstract QString QAbstractFileEngineIterator.next()"""
        return QString()


class QModelIndex():
    """"""
    def __init__():
        """None QModelIndex.__init__()"""
        return None
    def __init__(_other):
        """None QModelIndex.__init__(QModelIndex _other)"""
        return None
    def __init__():
        """QPersistentModelIndex QModelIndex.__init__()"""
        return QPersistentModelIndex()
    def __ge__(_other):
        """bool QModelIndex.__ge__(QModelIndex _other)"""
        return bool()
    def __hash__():
        """int QModelIndex.__hash__()"""
        return int()
    def __ne__(_other):
        """bool QModelIndex.__ne__(QModelIndex _other)"""
        return bool()
    def __lt__(_other):
        """bool QModelIndex.__lt__(QModelIndex _other)"""
        return bool()
    def __eq__(_other):
        """bool QModelIndex.__eq__(QModelIndex _other)"""
        return bool()
    def sibling(_arow, _acolumn):
        """QModelIndex QModelIndex.sibling(int _arow, int _acolumn)"""
        return QModelIndex()
    def parent():
        """QModelIndex QModelIndex.parent()"""
        return QModelIndex()
    def isValid():
        """bool QModelIndex.isValid()"""
        return bool()
    def model():
        """QAbstractItemModel QModelIndex.model()"""
        return QAbstractItemModel()
    def internalId():
        """int QModelIndex.internalId()"""
        return int()
    def internalPointer():
        """object QModelIndex.internalPointer()"""
        return object()
    def flags():
        """Qt.ItemFlags QModelIndex.flags()"""
        return Qt.ItemFlags()
    def data(_role):
        """QVariant QModelIndex.data(int _role)"""
        return QVariant()
    def column():
        """int QModelIndex.column()"""
        return int()
    def row():
        """int QModelIndex.row()"""
        return int()
    def child(_arow, _acolumn):
        """QModelIndex QModelIndex.child(int _arow, int _acolumn)"""
        return QModelIndex()


class QPersistentModelIndex():
    """"""
    def __init__():
        """None QPersistentModelIndex.__init__()"""
        return None
    def __init__(_index):
        """None QPersistentModelIndex.__init__(QModelIndex _index)"""
        return None
    def __init__(_other):
        """None QPersistentModelIndex.__init__(QPersistentModelIndex _other)"""
        return None
    def __ge__(_other):
        """bool QPersistentModelIndex.__ge__(QPersistentModelIndex _other)"""
        return bool()
    def __hash__():
        """int QPersistentModelIndex.__hash__()"""
        return int()
    def __ne__(_other):
        """bool QPersistentModelIndex.__ne__(QPersistentModelIndex _other)"""
        return bool()
    def __ne__(_other):
        """bool QPersistentModelIndex.__ne__(QModelIndex _other)"""
        return bool()
    def __eq__(_other):
        """bool QPersistentModelIndex.__eq__(QPersistentModelIndex _other)"""
        return bool()
    def __eq__(_other):
        """bool QPersistentModelIndex.__eq__(QModelIndex _other)"""
        return bool()
    def __lt__(_other):
        """bool QPersistentModelIndex.__lt__(QPersistentModelIndex _other)"""
        return bool()
    def isValid():
        """bool QPersistentModelIndex.isValid()"""
        return bool()
    def model():
        """QAbstractItemModel QPersistentModelIndex.model()"""
        return QAbstractItemModel()
    def child(_row, _column):
        """QModelIndex QPersistentModelIndex.child(int _row, int _column)"""
        return QModelIndex()
    def sibling(_row, _column):
        """QModelIndex QPersistentModelIndex.sibling(int _row, int _column)"""
        return QModelIndex()
    def parent():
        """QModelIndex QPersistentModelIndex.parent()"""
        return QModelIndex()
    def flags():
        """Qt.ItemFlags QPersistentModelIndex.flags()"""
        return Qt.ItemFlags()
    def data(_role):
        """QVariant QPersistentModelIndex.data(int _role)"""
        return QVariant()
    def column():
        """int QPersistentModelIndex.column()"""
        return int()
    def row():
        """int QPersistentModelIndex.row()"""
        return int()


class QAbstractItemModel(QObject):
    """"""
    def __init__(_parent):
        """None QAbstractItemModel.__init__(QObject _parent)"""
        return None
    def setRoleNames(_roleNames):
        """None QAbstractItemModel.setRoleNames(dict-of-int-QByteArray _roleNames)"""
        return None
    def endResetModel():
        """None QAbstractItemModel.endResetModel()"""
        return None
    def beginResetModel():
        """None QAbstractItemModel.beginResetModel()"""
        return None
    def endMoveColumns():
        """None QAbstractItemModel.endMoveColumns()"""
        return None
    def beginMoveColumns(_sourceParent, _sourceFirst, _sourceLast, _destinationParent, _destinationColumn):
        """bool QAbstractItemModel.beginMoveColumns(QModelIndex _sourceParent, int _sourceFirst, int _sourceLast, QModelIndex _destinationParent, int _destinationColumn)"""
        return bool()
    def endMoveRows():
        """None QAbstractItemModel.endMoveRows()"""
        return None
    def beginMoveRows(_sourceParent, _sourceFirst, _sourceLast, _destinationParent, _destinationRow):
        """bool QAbstractItemModel.beginMoveRows(QModelIndex _sourceParent, int _sourceFirst, int _sourceLast, QModelIndex _destinationParent, int _destinationRow)"""
        return bool()
    def createIndex(_row, _column, _object):
        """QModelIndex QAbstractItemModel.createIndex(int _row, int _column, object _object)"""
        return QModelIndex()
    def roleNames():
        """dict-of-int-QByteArray QAbstractItemModel.roleNames()"""
        return dict-of-int-QByteArray()
    def supportedDragActions():
        """Qt.DropActions QAbstractItemModel.supportedDragActions()"""
        return Qt.DropActions()
    def setSupportedDragActions():
        """Qt.DropActions QAbstractItemModel.setSupportedDragActions()"""
        return Qt.DropActions()
    def removeColumn(_column, _parent):
        """bool QAbstractItemModel.removeColumn(int _column, QModelIndex _parent)"""
        return bool()
    def removeRow(_row, _parent):
        """bool QAbstractItemModel.removeRow(int _row, QModelIndex _parent)"""
        return bool()
    def insertColumn(_column, _parent):
        """bool QAbstractItemModel.insertColumn(int _column, QModelIndex _parent)"""
        return bool()
    def insertRow(_row, _parent):
        """bool QAbstractItemModel.insertRow(int _row, QModelIndex _parent)"""
        return bool()
    def changePersistentIndexList(_from, _to):
        """None QAbstractItemModel.changePersistentIndexList(list-of-QModelIndex _from, list-of-QModelIndex _to)"""
        return None
    def changePersistentIndex(_from, _to):
        """None QAbstractItemModel.changePersistentIndex(QModelIndex _from, QModelIndex _to)"""
        return None
    def reset():
        """None QAbstractItemModel.reset()"""
        return None
    def persistentIndexList():
        """list-of-QModelIndex QAbstractItemModel.persistentIndexList()"""
        return [QModelIndex()]
    def endRemoveColumns():
        """None QAbstractItemModel.endRemoveColumns()"""
        return None
    def beginRemoveColumns(_parent, _first, _last):
        """None QAbstractItemModel.beginRemoveColumns(QModelIndex _parent, int _first, int _last)"""
        return None
    def endInsertColumns():
        """None QAbstractItemModel.endInsertColumns()"""
        return None
    def beginInsertColumns(_parent, _first, _last):
        """None QAbstractItemModel.beginInsertColumns(QModelIndex _parent, int _first, int _last)"""
        return None
    def endRemoveRows():
        """None QAbstractItemModel.endRemoveRows()"""
        return None
    def beginRemoveRows(_parent, _first, _last):
        """None QAbstractItemModel.beginRemoveRows(QModelIndex _parent, int _first, int _last)"""
        return None
    def endInsertRows():
        """None QAbstractItemModel.endInsertRows()"""
        return None
    def beginInsertRows(_parent, _first, _last):
        """None QAbstractItemModel.beginInsertRows(QModelIndex _parent, int _first, int _last)"""
        return None
    def decodeData(_row, _column, _parent, _stream):
        """bool QAbstractItemModel.decodeData(int _row, int _column, QModelIndex _parent, QDataStream _stream)"""
        return bool()
    def encodeData(_indexes, _stream):
        """None QAbstractItemModel.encodeData(list-of-QModelIndex _indexes, QDataStream _stream)"""
        return None
    def revert():
        """None QAbstractItemModel.revert()"""
        return None
    def submit():
        """bool QAbstractItemModel.submit()"""
        return bool()
    def span(_index):
        """QSize QAbstractItemModel.span(QModelIndex _index)"""
        return QSize()
    def match(_start, _role, _value, _hits, _flags):
        """list-of-QModelIndex QAbstractItemModel.match(QModelIndex _start, int _role, QVariant _value, int _hits, Qt.MatchFlags _flags)"""
        return [QModelIndex()]
    def buddy(_index):
        """QModelIndex QAbstractItemModel.buddy(QModelIndex _index)"""
        return QModelIndex()
    def sort(_column, _order):
        """None QAbstractItemModel.sort(int _column, Qt.SortOrder _order)"""
        return None
    def flags(_index):
        """Qt.ItemFlags QAbstractItemModel.flags(QModelIndex _index)"""
        return Qt.ItemFlags()
    def canFetchMore(_parent):
        """bool QAbstractItemModel.canFetchMore(QModelIndex _parent)"""
        return bool()
    def fetchMore(_parent):
        """None QAbstractItemModel.fetchMore(QModelIndex _parent)"""
        return None
    def removeColumns(_column, _count, _parent):
        """bool QAbstractItemModel.removeColumns(int _column, int _count, QModelIndex _parent)"""
        return bool()
    def removeRows(_row, _count, _parent):
        """bool QAbstractItemModel.removeRows(int _row, int _count, QModelIndex _parent)"""
        return bool()
    def insertColumns(_column, _count, _parent):
        """bool QAbstractItemModel.insertColumns(int _column, int _count, QModelIndex _parent)"""
        return bool()
    def insertRows(_row, _count, _parent):
        """bool QAbstractItemModel.insertRows(int _row, int _count, QModelIndex _parent)"""
        return bool()
    def supportedDropActions():
        """Qt.DropActions QAbstractItemModel.supportedDropActions()"""
        return Qt.DropActions()
    def dropMimeData(_data, _action, _row, _column, _parent):
        """bool QAbstractItemModel.dropMimeData(QMimeData _data, Qt.DropAction _action, int _row, int _column, QModelIndex _parent)"""
        return bool()
    def mimeData(_indexes):
        """QMimeData QAbstractItemModel.mimeData(list-of-QModelIndex _indexes)"""
        return QMimeData()
    def mimeTypes():
        """QStringList QAbstractItemModel.mimeTypes()"""
        return QStringList()
    def setItemData(_index, _roles):
        """bool QAbstractItemModel.setItemData(QModelIndex _index, dict-of-int-QVariant _roles)"""
        return bool()
    def itemData(_index):
        """dict-of-int-QVariant QAbstractItemModel.itemData(QModelIndex _index)"""
        return dict-of-int-QVariant()
    def setHeaderData(_section, _orientation, _value, _role):
        """bool QAbstractItemModel.setHeaderData(int _section, Qt.Orientation _orientation, QVariant _value, int _role)"""
        return bool()
    def headerData(_section, _orientation, _role):
        """QVariant QAbstractItemModel.headerData(int _section, Qt.Orientation _orientation, int _role)"""
        return QVariant()
    def setData(_index, _value, _role):
        """bool QAbstractItemModel.setData(QModelIndex _index, QVariant _value, int _role)"""
        return bool()
    def data(_index, _role):
        """abstract QVariant QAbstractItemModel.data(QModelIndex _index, int _role)"""
        return QVariant()
    def hasChildren(_parent):
        """bool QAbstractItemModel.hasChildren(QModelIndex _parent)"""
        return bool()
    def columnCount(_parent):
        """abstract int QAbstractItemModel.columnCount(QModelIndex _parent)"""
        return int()
    def rowCount(_parent):
        """abstract int QAbstractItemModel.rowCount(QModelIndex _parent)"""
        return int()
    def sibling(_row, _column, _idx):
        """QModelIndex QAbstractItemModel.sibling(int _row, int _column, QModelIndex _idx)"""
        return QModelIndex()
    def parent(_child):
        """abstract QModelIndex QAbstractItemModel.parent(QModelIndex _child)"""
        return QModelIndex()
    def parent():
        """QObject QAbstractItemModel.parent()"""
        return QObject()
    def index(_row, _column, _parent):
        """abstract QModelIndex QAbstractItemModel.index(int _row, int _column, QModelIndex _parent)"""
        return QModelIndex()
    def hasIndex(_row, _column, _parent):
        """bool QAbstractItemModel.hasIndex(int _row, int _column, QModelIndex _parent)"""
        return bool()


class QAbstractTableModel(QAbstractItemModel):
    """"""
    def __init__(_parent):
        """None QAbstractTableModel.__init__(QObject _parent)"""
        return None
    def dropMimeData(_data, _action, _row, _column, _parent):
        """bool QAbstractTableModel.dropMimeData(QMimeData _data, Qt.DropAction _action, int _row, int _column, QModelIndex _parent)"""
        return bool()
    def index(_row, _column, _parent):
        """QModelIndex QAbstractTableModel.index(int _row, int _column, QModelIndex _parent)"""
        return QModelIndex()


class QAbstractListModel(QAbstractItemModel):
    """"""
    def __init__(_parent):
        """None QAbstractListModel.__init__(QObject _parent)"""
        return None
    def dropMimeData(_data, _action, _row, _column, _parent):
        """bool QAbstractListModel.dropMimeData(QMimeData _data, Qt.DropAction _action, int _row, int _column, QModelIndex _parent)"""
        return bool()
    def index(_row, _column, _parent):
        """QModelIndex QAbstractListModel.index(int _row, int _column, QModelIndex _parent)"""
        return QModelIndex()


class QAbstractState(QObject):
    """"""
    def __init__(_parent):
        """None QAbstractState.__init__(QState _parent)"""
        return None
    def event(_e):
        """bool QAbstractState.event(QEvent _e)"""
        return bool()
    def onExit(_event):
        """abstract None QAbstractState.onExit(QEvent _event)"""
        return None
    def onEntry(_event):
        """abstract None QAbstractState.onEntry(QEvent _event)"""
        return None
    def machine():
        """QStateMachine QAbstractState.machine()"""
        return QStateMachine()
    def parentState():
        """QState QAbstractState.parentState()"""
        return QState()


class QAbstractTransition(QObject):
    """"""
    def __init__(_sourceState):
        """None QAbstractTransition.__init__(QState _sourceState)"""
        return None
    def event(_e):
        """bool QAbstractTransition.event(QEvent _e)"""
        return bool()
    def onTransition(_event):
        """abstract None QAbstractTransition.onTransition(QEvent _event)"""
        return None
    def eventTest(_event):
        """abstract bool QAbstractTransition.eventTest(QEvent _event)"""
        return bool()
    def animations():
        """list-of-QAbstractAnimation QAbstractTransition.animations()"""
        return [QAbstractAnimation()]
    def removeAnimation(_animation):
        """None QAbstractTransition.removeAnimation(QAbstractAnimation _animation)"""
        return None
    def addAnimation(_animation):
        """None QAbstractTransition.addAnimation(QAbstractAnimation _animation)"""
        return None
    def machine():
        """QStateMachine QAbstractTransition.machine()"""
        return QStateMachine()
    def setTargetStates(_targets):
        """None QAbstractTransition.setTargetStates(list-of-QAbstractState _targets)"""
        return None
    def targetStates():
        """list-of-QAbstractState QAbstractTransition.targetStates()"""
        return [QAbstractState()]
    def setTargetState(_target):
        """None QAbstractTransition.setTargetState(QAbstractState _target)"""
        return None
    def targetState():
        """QAbstractState QAbstractTransition.targetState()"""
        return QAbstractState()
    def sourceState():
        """QState QAbstractTransition.sourceState()"""
        return QState()


class QAnimationGroup(QAbstractAnimation):
    """"""
    def __init__(_parent):
        """None QAnimationGroup.__init__(QObject _parent)"""
        return None
    def event(_event):
        """bool QAnimationGroup.event(QEvent _event)"""
        return bool()
    def clear():
        """None QAnimationGroup.clear()"""
        return None
    def takeAnimation(_index):
        """QAbstractAnimation QAnimationGroup.takeAnimation(int _index)"""
        return QAbstractAnimation()
    def removeAnimation(_animation):
        """None QAnimationGroup.removeAnimation(QAbstractAnimation _animation)"""
        return None
    def insertAnimation(_index, _animation):
        """None QAnimationGroup.insertAnimation(int _index, QAbstractAnimation _animation)"""
        return None
    def addAnimation(_animation):
        """None QAnimationGroup.addAnimation(QAbstractAnimation _animation)"""
        return None
    def indexOfAnimation(_animation):
        """int QAnimationGroup.indexOfAnimation(QAbstractAnimation _animation)"""
        return int()
    def animationCount():
        """int QAnimationGroup.animationCount()"""
        return int()
    def animationAt(_index):
        """QAbstractAnimation QAnimationGroup.animationAt(int _index)"""
        return QAbstractAnimation()


class QBasicTimer():
    """"""
    def __init__():
        """None QBasicTimer.__init__()"""
        return None
    def __init__():
        """QBasicTimer QBasicTimer.__init__()"""
        return QBasicTimer()
    def stop():
        """None QBasicTimer.stop()"""
        return None
    def start(_msec, _obj):
        """None QBasicTimer.start(int _msec, QObject _obj)"""
        return None
    def timerId():
        """int QBasicTimer.timerId()"""
        return int()
    def isActive():
        """bool QBasicTimer.isActive()"""
        return bool()


class QBitArray():
    """"""
    def __init__():
        """None QBitArray.__init__()"""
        return None
    def __init__(_size, _value):
        """None QBitArray.__init__(int _size, bool _value)"""
        return None
    def __init__(_other):
        """None QBitArray.__init__(QBitArray _other)"""
        return None
    def __or__():
        """QBitArray QBitArray.__or__()"""
        return QBitArray()
    def __and__():
        """QBitArray QBitArray.__and__()"""
        return QBitArray()
    def __xor__():
        """QBitArray QBitArray.__xor__()"""
        return QBitArray()
    def __hash__():
        """int QBitArray.__hash__()"""
        return int()
    def at(_i):
        """bool QBitArray.at(int _i)"""
        return bool()
    def __getitem__(_i):
        """bool QBitArray.__getitem__(int _i)"""
        return bool()
    def toggleBit(_i):
        """bool QBitArray.toggleBit(int _i)"""
        return bool()
    def clearBit(_i):
        """None QBitArray.clearBit(int _i)"""
        return None
    def setBit(_i):
        """None QBitArray.setBit(int _i)"""
        return None
    def setBit(_i, _val):
        """None QBitArray.setBit(int _i, bool _val)"""
        return None
    def testBit(_i):
        """bool QBitArray.testBit(int _i)"""
        return bool()
    def truncate(_pos):
        """None QBitArray.truncate(int _pos)"""
        return None
    def fill(_val, _first, _last):
        """None QBitArray.fill(bool _val, int _first, int _last)"""
        return None
    def fill(_value, _size):
        """bool QBitArray.fill(bool _value, int _size)"""
        return bool()
    def __ne__(_a):
        """bool QBitArray.__ne__(QBitArray _a)"""
        return bool()
    def __eq__(_a):
        """bool QBitArray.__eq__(QBitArray _a)"""
        return bool()
    def __invert__():
        """QBitArray QBitArray.__invert__()"""
        return QBitArray()
    def __ixor__():
        """QBitArray QBitArray.__ixor__()"""
        return QBitArray()
    def __ior__():
        """QBitArray QBitArray.__ior__()"""
        return QBitArray()
    def __iand__():
        """QBitArray QBitArray.__iand__()"""
        return QBitArray()
    def clear():
        """None QBitArray.clear()"""
        return None
    def isDetached():
        """bool QBitArray.isDetached()"""
        return bool()
    def detach():
        """None QBitArray.detach()"""
        return None
    def resize(_size):
        """None QBitArray.resize(int _size)"""
        return None
    def isNull():
        """bool QBitArray.isNull()"""
        return bool()
    def isEmpty():
        """bool QBitArray.isEmpty()"""
        return bool()
    def __len__():
        """ QBitArray.__len__()"""
        return ()
    def count():
        """int QBitArray.count()"""
        return int()
    def count(_on):
        """int QBitArray.count(bool _on)"""
        return int()
    def size():
        """int QBitArray.size()"""
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

    def __init__():
        """None QIODevice.__init__()"""
        return None
    def __init__(_parent):
        """None QIODevice.__init__(QObject _parent)"""
        return None
    def setErrorString(_errorString):
        """None QIODevice.setErrorString(QString _errorString)"""
        return None
    def setOpenMode(_openMode):
        """None QIODevice.setOpenMode(QIODevice.OpenMode _openMode)"""
        return None
    def writeData(_data):
        """abstract int QIODevice.writeData(str _data)"""
        return int()
    def readLineData(_maxlen):
        """str QIODevice.readLineData(int _maxlen)"""
        return str()
    def readData(_maxlen):
        """abstract str QIODevice.readData(int _maxlen)"""
        return str()
    def errorString():
        """QString QIODevice.errorString()"""
        return QString()
    def getChar(_c):
        """bool QIODevice.getChar(str _c)"""
        return bool()
    def putChar(_c):
        """bool QIODevice.putChar(str _c)"""
        return bool()
    def ungetChar(_c):
        """None QIODevice.ungetChar(str _c)"""
        return None
    def waitForBytesWritten(_msecs):
        """bool QIODevice.waitForBytesWritten(int _msecs)"""
        return bool()
    def waitForReadyRead(_msecs):
        """bool QIODevice.waitForReadyRead(int _msecs)"""
        return bool()
    def write(_data):
        """int QIODevice.write(QByteArray _data)"""
        return int()
    def peek(_maxlen):
        """QByteArray QIODevice.peek(int _maxlen)"""
        return QByteArray()
    def canReadLine():
        """bool QIODevice.canReadLine()"""
        return bool()
    def readLine(_maxlen):
        """str QIODevice.readLine(int _maxlen)"""
        return str()
    def readAll():
        """QByteArray QIODevice.readAll()"""
        return QByteArray()
    def read(_maxlen):
        """str QIODevice.read(int _maxlen)"""
        return str()
    def bytesToWrite():
        """int QIODevice.bytesToWrite()"""
        return int()
    def bytesAvailable():
        """int QIODevice.bytesAvailable()"""
        return int()
    def reset():
        """bool QIODevice.reset()"""
        return bool()
    def atEnd():
        """bool QIODevice.atEnd()"""
        return bool()
    def seek(_pos):
        """bool QIODevice.seek(int _pos)"""
        return bool()
    def size():
        """int QIODevice.size()"""
        return int()
    def pos():
        """int QIODevice.pos()"""
        return int()
    def close():
        """None QIODevice.close()"""
        return None
    def open(_mode):
        """bool QIODevice.open(QIODevice.OpenMode _mode)"""
        return bool()
    def isSequential():
        """bool QIODevice.isSequential()"""
        return bool()
    def isWritable():
        """bool QIODevice.isWritable()"""
        return bool()
    def isReadable():
        """bool QIODevice.isReadable()"""
        return bool()
    def isOpen():
        """bool QIODevice.isOpen()"""
        return bool()
    def isTextModeEnabled():
        """bool QIODevice.isTextModeEnabled()"""
        return bool()
    def setTextModeEnabled(_enabled):
        """None QIODevice.setTextModeEnabled(bool _enabled)"""
        return None
    def openMode():
        """QIODevice.OpenMode QIODevice.openMode()"""
        return QIODevice.OpenMode()


class QBuffer(QIODevice):
    """"""
    def __init__(_parent):
        """None QBuffer.__init__(QObject _parent)"""
        return None
    def __init__(_byteArray, _parent):
        """None QBuffer.__init__(QByteArray _byteArray, QObject _parent)"""
        return None
    def disconnectNotify():
        """SIGNAL() QBuffer.disconnectNotify()"""
        return SIGNAL()()
    def connectNotify():
        """SIGNAL() QBuffer.connectNotify()"""
        return SIGNAL()()
    def writeData(_data):
        """int QBuffer.writeData(str _data)"""
        return int()
    def readData(_maxlen):
        """str QBuffer.readData(int _maxlen)"""
        return str()
    def canReadLine():
        """bool QBuffer.canReadLine()"""
        return bool()
    def atEnd():
        """bool QBuffer.atEnd()"""
        return bool()
    def seek(_off):
        """bool QBuffer.seek(int _off)"""
        return bool()
    def pos():
        """int QBuffer.pos()"""
        return int()
    def size():
        """int QBuffer.size()"""
        return int()
    def close():
        """None QBuffer.close()"""
        return None
    def open(_openMode):
        """bool QBuffer.open(QIODevice.OpenMode _openMode)"""
        return bool()
    def setData(_data):
        """None QBuffer.setData(QByteArray _data)"""
        return None
    def setData(_adata):
        """None QBuffer.setData(str _adata)"""
        return None
    def setBuffer(_a):
        """None QBuffer.setBuffer(QByteArray _a)"""
        return None
    def data():
        """QByteArray QBuffer.data()"""
        return QByteArray()
    def buffer():
        """QByteArray QBuffer.buffer()"""
        return QByteArray()


class QByteArray():
    """"""
    def __init__():
        """None QByteArray.__init__()"""
        return None
    def __init__(_size, _c):
        """None QByteArray.__init__(int _size, str _c)"""
        return None
    def __init__(_a):
        """None QByteArray.__init__(QByteArray _a)"""
        return None
    def __add__(_a2):
        """QByteArray QByteArray.__add__(QByteArray _a2)"""
        return QByteArray()
    def __add__(_s):
        """QString QByteArray.__add__(QString _s)"""
        return QString()
    def repeated(_times):
        """QByteArray QByteArray.repeated(int _times)"""
        return QByteArray()
    def fromPercentEncoding(_input, _percent):
        """QByteArray QByteArray.fromPercentEncoding(QByteArray _input, str _percent)"""
        return QByteArray()
    def toPercentEncoding(_exclude, _include, _percent):
        """QByteArray QByteArray.toPercentEncoding(QByteArray _exclude, QByteArray _include, str _percent)"""
        return QByteArray()
    def toHex():
        """QByteArray QByteArray.toHex()"""
        return QByteArray()
    def contains(_a):
        """bool QByteArray.contains(QByteArray _a)"""
        return bool()
    def push_front(_a):
        """None QByteArray.push_front(QByteArray _a)"""
        return None
    def push_back(_a):
        """None QByteArray.push_back(QByteArray _a)"""
        return None
    def squeeze():
        """None QByteArray.squeeze()"""
        return None
    def reserve(_size):
        """None QByteArray.reserve(int _size)"""
        return None
    def capacity():
        """int QByteArray.capacity()"""
        return int()
    def data():
        """str QByteArray.data()"""
        return str()
    def isEmpty():
        """bool QByteArray.isEmpty()"""
        return bool()
    def __imul__(_m):
        """QByteArray QByteArray.__imul__(int _m)"""
        return QByteArray()
    def __mul__(_m):
        """QByteArray QByteArray.__mul__(int _m)"""
        return QByteArray()
    def __repr__():
        """str QByteArray.__repr__()"""
        return str()
    def __str__():
        """str QByteArray.__str__()"""
        return str()
    def __hash__():
        """int QByteArray.__hash__()"""
        return int()
    def __contains__(_a):
        """int QByteArray.__contains__(QByteArray _a)"""
        return int()
    def __getitem__(_i):
        """str QByteArray.__getitem__(int _i)"""
        return str()
    def __getitem__(_slice):
        """QByteArray QByteArray.__getitem__(slice _slice)"""
        return QByteArray()
    def at(_i):
        """str QByteArray.at(int _i)"""
        return str()
    def size():
        """int QByteArray.size()"""
        return int()
    def isNull():
        """bool QByteArray.isNull()"""
        return bool()
    def length():
        """int QByteArray.length()"""
        return int()
    def __len__():
        """ QByteArray.__len__()"""
        return ()
    def fromHex(_hexEncoded):
        """QByteArray QByteArray.fromHex(QByteArray _hexEncoded)"""
        return QByteArray()
    def fromRawData():
        """str QByteArray.fromRawData()"""
        return str()
    def fromBase64(_base64):
        """QByteArray QByteArray.fromBase64(QByteArray _base64)"""
        return QByteArray()
    def number(_n, _base):
        """QByteArray QByteArray.number(int _n, int _base)"""
        return QByteArray()
    def number(_n, _format, _precision):
        """QByteArray QByteArray.number(float _n, str _format, int _precision)"""
        return QByteArray()
    def number(_n, _base):
        """QByteArray QByteArray.number(int _n, int _base)"""
        return QByteArray()
    def number(_n, _base):
        """QByteArray QByteArray.number(int _n, int _base)"""
        return QByteArray()
    def setNum(_n, _base):
        """QByteArray QByteArray.setNum(int _n, int _base)"""
        return QByteArray()
    def setNum(_n, _format, _precision):
        """QByteArray QByteArray.setNum(float _n, str _format, int _precision)"""
        return QByteArray()
    def setNum(_n, _base):
        """QByteArray QByteArray.setNum(int _n, int _base)"""
        return QByteArray()
    def setNum(_n, _base):
        """QByteArray QByteArray.setNum(int _n, int _base)"""
        return QByteArray()
    def toBase64():
        """QByteArray QByteArray.toBase64()"""
        return QByteArray()
    def toDouble(_ok):
        """float QByteArray.toDouble(bool _ok)"""
        return float()
    def toFloat(_ok):
        """float QByteArray.toFloat(bool _ok)"""
        return float()
    def toULongLong(_ok, _base):
        """int QByteArray.toULongLong(bool _ok, int _base)"""
        return int()
    def toLongLong(_ok, _base):
        """int QByteArray.toLongLong(bool _ok, int _base)"""
        return int()
    def toULong(_ok, _base):
        """int QByteArray.toULong(bool _ok, int _base)"""
        return int()
    def toLong(_ok, _base):
        """int QByteArray.toLong(bool _ok, int _base)"""
        return int()
    def toUInt(_ok, _base):
        """int QByteArray.toUInt(bool _ok, int _base)"""
        return int()
    def toInt(_ok, _base):
        """int QByteArray.toInt(bool _ok, int _base)"""
        return int()
    def toUShort(_ok, _base):
        """int QByteArray.toUShort(bool _ok, int _base)"""
        return int()
    def toShort(_ok, _base):
        """int QByteArray.toShort(bool _ok, int _base)"""
        return int()
    def __ge__(_s2):
        """bool QByteArray.__ge__(QString _s2)"""
        return bool()
    def __ge__(_a2):
        """bool QByteArray.__ge__(QByteArray _a2)"""
        return bool()
    def __le__(_s2):
        """bool QByteArray.__le__(QString _s2)"""
        return bool()
    def __le__(_a2):
        """bool QByteArray.__le__(QByteArray _a2)"""
        return bool()
    def __gt__(_s2):
        """bool QByteArray.__gt__(QString _s2)"""
        return bool()
    def __gt__(_a2):
        """bool QByteArray.__gt__(QByteArray _a2)"""
        return bool()
    def __lt__(_s2):
        """bool QByteArray.__lt__(QString _s2)"""
        return bool()
    def __lt__(_a2):
        """bool QByteArray.__lt__(QByteArray _a2)"""
        return bool()
    def __ne__(_s2):
        """bool QByteArray.__ne__(QString _s2)"""
        return bool()
    def __ne__(_a2):
        """bool QByteArray.__ne__(QByteArray _a2)"""
        return bool()
    def __eq__(_s2):
        """bool QByteArray.__eq__(QString _s2)"""
        return bool()
    def __eq__(_a2):
        """bool QByteArray.__eq__(QByteArray _a2)"""
        return bool()
    def __iadd__(_a):
        """QByteArray QByteArray.__iadd__(QByteArray _a)"""
        return QByteArray()
    def __iadd__(_s):
        """QByteArray QByteArray.__iadd__(QString _s)"""
        return QByteArray()
    def split(_sep):
        """list-of-QByteArray QByteArray.split(str _sep)"""
        return [QByteArray()]
    def replace(_index, _len, _s):
        """QByteArray QByteArray.replace(int _index, int _len, QByteArray _s)"""
        return QByteArray()
    def replace(_before, _after):
        """QByteArray QByteArray.replace(QByteArray _before, QByteArray _after)"""
        return QByteArray()
    def replace(_before, _after):
        """QByteArray QByteArray.replace(QString _before, QByteArray _after)"""
        return QByteArray()
    def remove(_index, _len):
        """QByteArray QByteArray.remove(int _index, int _len)"""
        return QByteArray()
    def insert(_i, _a):
        """QByteArray QByteArray.insert(int _i, QByteArray _a)"""
        return QByteArray()
    def insert(_i, _s):
        """QByteArray QByteArray.insert(int _i, QString _s)"""
        return QByteArray()
    def append(_a):
        """QByteArray QByteArray.append(QByteArray _a)"""
        return QByteArray()
    def append(_s):
        """QByteArray QByteArray.append(QString _s)"""
        return QByteArray()
    def prepend(_a):
        """QByteArray QByteArray.prepend(QByteArray _a)"""
        return QByteArray()
    def rightJustified(_width, _fill, _truncate):
        """QByteArray QByteArray.rightJustified(int _width, str _fill, bool _truncate)"""
        return QByteArray()
    def leftJustified(_width, _fill, _truncate):
        """QByteArray QByteArray.leftJustified(int _width, str _fill, bool _truncate)"""
        return QByteArray()
    def simplified():
        """QByteArray QByteArray.simplified()"""
        return QByteArray()
    def trimmed():
        """QByteArray QByteArray.trimmed()"""
        return QByteArray()
    def toUpper():
        """QByteArray QByteArray.toUpper()"""
        return QByteArray()
    def toLower():
        """QByteArray QByteArray.toLower()"""
        return QByteArray()
    def chop(_n):
        """None QByteArray.chop(int _n)"""
        return None
    def truncate(_pos):
        """None QByteArray.truncate(int _pos)"""
        return None
    def endsWith(_a):
        """bool QByteArray.endsWith(QByteArray _a)"""
        return bool()
    def startsWith(_a):
        """bool QByteArray.startsWith(QByteArray _a)"""
        return bool()
    def mid(_pos, _length):
        """QByteArray QByteArray.mid(int _pos, int _length)"""
        return QByteArray()
    def right(_len):
        """QByteArray QByteArray.right(int _len)"""
        return QByteArray()
    def left(_len):
        """QByteArray QByteArray.left(int _len)"""
        return QByteArray()
    def count(_a):
        """int QByteArray.count(QByteArray _a)"""
        return int()
    def count():
        """int QByteArray.count()"""
        return int()
    def lastIndexOf(_ba, _from):
        """int QByteArray.lastIndexOf(QByteArray _ba, int _from)"""
        return int()
    def lastIndexOf(_str, _from):
        """int QByteArray.lastIndexOf(QString _str, int _from)"""
        return int()
    def indexOf(_ba, _from):
        """int QByteArray.indexOf(QByteArray _ba, int _from)"""
        return int()
    def indexOf(_str, _from):
        """int QByteArray.indexOf(QString _str, int _from)"""
        return int()
    def clear():
        """None QByteArray.clear()"""
        return None
    def fill(_ch, _size):
        """QByteArray QByteArray.fill(str _ch, int _size)"""
        return QByteArray()
    def resize(_size):
        """None QByteArray.resize(int _size)"""
        return None


class QByteArrayMatcher():
    """"""
    def __init__():
        """None QByteArrayMatcher.__init__()"""
        return None
    def __init__(_pattern):
        """None QByteArrayMatcher.__init__(QByteArray _pattern)"""
        return None
    def __init__(_other):
        """None QByteArrayMatcher.__init__(QByteArrayMatcher _other)"""
        return None
    def pattern():
        """QByteArray QByteArrayMatcher.pattern()"""
        return QByteArray()
    def indexIn(_ba, _from):
        """int QByteArrayMatcher.indexIn(QByteArray _ba, int _from)"""
        return int()
    def setPattern(_pattern):
        """None QByteArrayMatcher.setPattern(QByteArray _pattern)"""
        return None


class QLatin1Char():
    """"""
    def __init__(_c):
        """None QLatin1Char.__init__(str _c)"""
        return None
    def __init__():
        """QLatin1Char QLatin1Char.__init__()"""
        return QLatin1Char()
    def unicode():
        """int QLatin1Char.unicode()"""
        return int()
    def toLatin1():
        """str QLatin1Char.toLatin1()"""
        return str()
    def __repr__():
        """str QLatin1Char.__repr__()"""
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

    def __init__():
        """None QChar.__init__()"""
        return None
    def __init__(_c):
        """None QChar.__init__(str _c)"""
        return None
    def __init__(_ch):
        """None QChar.__init__(QLatin1Char _ch)"""
        return None
    def __init__(_c, _r):
        """None QChar.__init__(str _c, str _r)"""
        return None
    def __init__(_rc):
        """None QChar.__init__(int _rc)"""
        return None
    def __init__(_s):
        """None QChar.__init__(QChar.SpecialCharacter _s)"""
        return None
    def __init__():
        """QChar QChar.__init__()"""
        return QChar()
    def __eq__(_c2):
        """bool QChar.__eq__(QChar _c2)"""
        return bool()
    def __ne__(_c2):
        """bool QChar.__ne__(QChar _c2)"""
        return bool()
    def __lt__(_c2):
        """bool QChar.__lt__(QChar _c2)"""
        return bool()
    def __le__(_c2):
        """bool QChar.__le__(QChar _c2)"""
        return bool()
    def __gt__(_c2):
        """bool QChar.__gt__(QChar _c2)"""
        return bool()
    def __ge__(_c2):
        """bool QChar.__ge__(QChar _c2)"""
        return bool()
    def __add__(_s2):
        """QString QChar.__add__(QString _s2)"""
        return QString()
    def requiresSurrogates(_ucs4):
        """bool QChar.requiresSurrogates(int _ucs4)"""
        return bool()
    def lowSurrogate(_ucs4):
        """int QChar.lowSurrogate(int _ucs4)"""
        return int()
    def highSurrogate(_ucs4):
        """int QChar.highSurrogate(int _ucs4)"""
        return int()
    def surrogateToUcs4(_high, _low):
        """int QChar.surrogateToUcs4(int _high, int _low)"""
        return int()
    def surrogateToUcs4(_high, _low):
        """int QChar.surrogateToUcs4(QChar _high, QChar _low)"""
        return int()
    def isLowSurrogate():
        """bool QChar.isLowSurrogate()"""
        return bool()
    def isLowSurrogate(_ucs4):
        """bool QChar.isLowSurrogate(int _ucs4)"""
        return bool()
    def isHighSurrogate():
        """bool QChar.isHighSurrogate()"""
        return bool()
    def isHighSurrogate(_ucs4):
        """bool QChar.isHighSurrogate(int _ucs4)"""
        return bool()
    def isTitleCase():
        """bool QChar.isTitleCase()"""
        return bool()
    def toCaseFolded():
        """QChar QChar.toCaseFolded()"""
        return QChar()
    def toCaseFolded(_ucs4):
        """int QChar.toCaseFolded(int _ucs4)"""
        return int()
    def toTitleCase():
        """QChar QChar.toTitleCase()"""
        return QChar()
    def toTitleCase(_ucs4):
        """int QChar.toTitleCase(int _ucs4)"""
        return int()
    def setRow(_arow):
        """None QChar.setRow(str _arow)"""
        return None
    def setCell(_acell):
        """None QChar.setCell(str _acell)"""
        return None
    def fromLatin1(_c):
        """QChar QChar.fromLatin1(str _c)"""
        return QChar()
    def toLatin1():
        """str QChar.toLatin1()"""
        return str()
    def row():
        """str QChar.row()"""
        return str()
    def cell():
        """str QChar.cell()"""
        return str()
    def isSymbol():
        """bool QChar.isSymbol()"""
        return bool()
    def isDigit():
        """bool QChar.isDigit()"""
        return bool()
    def isLetterOrNumber():
        """bool QChar.isLetterOrNumber()"""
        return bool()
    def isNumber():
        """bool QChar.isNumber()"""
        return bool()
    def isLetter():
        """bool QChar.isLetter()"""
        return bool()
    def isMark():
        """bool QChar.isMark()"""
        return bool()
    def isSpace():
        """bool QChar.isSpace()"""
        return bool()
    def isPunct():
        """bool QChar.isPunct()"""
        return bool()
    def isPrint():
        """bool QChar.isPrint()"""
        return bool()
    def isNull():
        """bool QChar.isNull()"""
        return bool()
    def fromAscii(_c):
        """QChar QChar.fromAscii(str _c)"""
        return QChar()
    def unicode():
        """int QChar.unicode()"""
        return int()
    def toAscii():
        """str QChar.toAscii()"""
        return str()
    def unicodeVersion():
        """QChar.UnicodeVersion QChar.unicodeVersion()"""
        return QChar.UnicodeVersion()
    def unicodeVersion(_ucs4):
        """QChar.UnicodeVersion QChar.unicodeVersion(int _ucs4)"""
        return QChar.UnicodeVersion()
    def combiningClass():
        """str QChar.combiningClass()"""
        return str()
    def combiningClass(_ucs4):
        """str QChar.combiningClass(int _ucs4)"""
        return str()
    def decompositionTag():
        """QChar.Decomposition QChar.decompositionTag()"""
        return QChar.Decomposition()
    def decompositionTag(_ucs4):
        """QChar.Decomposition QChar.decompositionTag(int _ucs4)"""
        return QChar.Decomposition()
    def decomposition():
        """QString QChar.decomposition()"""
        return QString()
    def decomposition(_ucs4):
        """QString QChar.decomposition(int _ucs4)"""
        return QString()
    def mirroredChar():
        """QChar QChar.mirroredChar()"""
        return QChar()
    def mirroredChar(_ucs4):
        """int QChar.mirroredChar(int _ucs4)"""
        return int()
    def isUpper():
        """bool QChar.isUpper()"""
        return bool()
    def isLower():
        """bool QChar.isLower()"""
        return bool()
    def hasMirrored():
        """bool QChar.hasMirrored()"""
        return bool()
    def joining():
        """QChar.Joining QChar.joining()"""
        return QChar.Joining()
    def joining(_ucs4):
        """QChar.Joining QChar.joining(int _ucs4)"""
        return QChar.Joining()
    def direction():
        """QChar.Direction QChar.direction()"""
        return QChar.Direction()
    def direction(_ucs4):
        """QChar.Direction QChar.direction(int _ucs4)"""
        return QChar.Direction()
    def category():
        """QChar.Category QChar.category()"""
        return QChar.Category()
    def category(_ucs4):
        """QChar.Category QChar.category(int _ucs4)"""
        return QChar.Category()
    def toUpper():
        """QChar QChar.toUpper()"""
        return QChar()
    def toUpper(_ucs4):
        """int QChar.toUpper(int _ucs4)"""
        return int()
    def toLower():
        """QChar QChar.toLower()"""
        return QChar()
    def toLower(_ucs4):
        """int QChar.toLower(int _ucs4)"""
        return int()
    def digitValue():
        """int QChar.digitValue()"""
        return int()
    def digitValue(_ucs4):
        """int QChar.digitValue(int _ucs4)"""
        return int()
    def __hash__():
        """int QChar.__hash__()"""
        return int()
    def __repr__():
        """str QChar.__repr__()"""
        return str()


class QCoreApplication(QObject):
    """"""
    CodecForTr = int() # QCoreApplication.Encoding enum
    UnicodeUTF8 = int() # QCoreApplication.Encoding enum
    DefaultCodec = int() # QCoreApplication.Encoding enum

    def __init__(_argv):
        """None QCoreApplication.__init__(list-of-str _argv)"""
        return None
    def applicationPid():
        """int QCoreApplication.applicationPid()"""
        return int()
    def applicationVersion():
        """QString QCoreApplication.applicationVersion()"""
        return QString()
    def setApplicationVersion(_version):
        """None QCoreApplication.setApplicationVersion(QString _version)"""
        return None
    def event():
        """QEvent QCoreApplication.event()"""
        return QEvent()
    def quit():
        """None QCoreApplication.quit()"""
        return None
    def testAttribute(_attribute):
        """bool QCoreApplication.testAttribute(Qt.ApplicationAttribute _attribute)"""
        return bool()
    def setAttribute(_attribute, _on):
        """None QCoreApplication.setAttribute(Qt.ApplicationAttribute _attribute, bool _on)"""
        return None
    def flush():
        """None QCoreApplication.flush()"""
        return None
    def translate(_context, _sourceText, _disambiguation, _encoding):
        """QString QCoreApplication.translate(str _context, str _sourceText, str _disambiguation, QCoreApplication.Encoding _encoding)"""
        return QString()
    def translate(_context, _sourceText, _disambiguation, _encoding, _n):
        """QString QCoreApplication.translate(str _context, str _sourceText, str _disambiguation, QCoreApplication.Encoding _encoding, int _n)"""
        return QString()
    def removeTranslator():
        """QTranslator QCoreApplication.removeTranslator()"""
        return QTranslator()
    def installTranslator():
        """QTranslator QCoreApplication.installTranslator()"""
        return QTranslator()
    def removeLibraryPath():
        """QString QCoreApplication.removeLibraryPath()"""
        return QString()
    def addLibraryPath():
        """QString QCoreApplication.addLibraryPath()"""
        return QString()
    def libraryPaths():
        """QStringList QCoreApplication.libraryPaths()"""
        return QStringList()
    def setLibraryPaths():
        """QStringList QCoreApplication.setLibraryPaths()"""
        return QStringList()
    def applicationFilePath():
        """QString QCoreApplication.applicationFilePath()"""
        return QString()
    def applicationDirPath():
        """QString QCoreApplication.applicationDirPath()"""
        return QString()
    def closingDown():
        """bool QCoreApplication.closingDown()"""
        return bool()
    def startingUp():
        """bool QCoreApplication.startingUp()"""
        return bool()
    def notify():
        """QEvent QCoreApplication.notify()"""
        return QEvent()
    def hasPendingEvents():
        """bool QCoreApplication.hasPendingEvents()"""
        return bool()
    def removePostedEvents(_receiver):
        """None QCoreApplication.removePostedEvents(QObject _receiver)"""
        return None
    def removePostedEvents(_receiver, _eventType):
        """None QCoreApplication.removePostedEvents(QObject _receiver, int _eventType)"""
        return None
    def sendPostedEvents(_receiver, _event_type):
        """None QCoreApplication.sendPostedEvents(QObject _receiver, int _event_type)"""
        return None
    def sendPostedEvents():
        """None QCoreApplication.sendPostedEvents()"""
        return None
    def postEvent(_receiver, _event):
        """None QCoreApplication.postEvent(QObject _receiver, QEvent _event)"""
        return None
    def postEvent(_receiver, _event, _priority):
        """None QCoreApplication.postEvent(QObject _receiver, QEvent _event, int _priority)"""
        return None
    def sendEvent(_receiver, _event):
        """bool QCoreApplication.sendEvent(QObject _receiver, QEvent _event)"""
        return bool()
    def exit(_returnCode):
        """None QCoreApplication.exit(int _returnCode)"""
        return None
    def processEvents(_flags):
        """None QCoreApplication.processEvents(QEventLoop.ProcessEventsFlags _flags)"""
        return None
    def processEvents(_flags, _maxtime):
        """None QCoreApplication.processEvents(QEventLoop.ProcessEventsFlags _flags, int _maxtime)"""
        return None
    def exec_():
        """int QCoreApplication.exec_()"""
        return int()
    def instance():
        """QCoreApplication QCoreApplication.instance()"""
        return QCoreApplication()
    def arguments():
        """QStringList QCoreApplication.arguments()"""
        return QStringList()
    def applicationName():
        """QString QCoreApplication.applicationName()"""
        return QString()
    def setApplicationName(_application):
        """None QCoreApplication.setApplicationName(QString _application)"""
        return None
    def organizationName():
        """QString QCoreApplication.organizationName()"""
        return QString()
    def setOrganizationName(_orgName):
        """None QCoreApplication.setOrganizationName(QString _orgName)"""
        return None
    def organizationDomain():
        """QString QCoreApplication.organizationDomain()"""
        return QString()
    def setOrganizationDomain(_orgDomain):
        """None QCoreApplication.setOrganizationDomain(QString _orgDomain)"""
        return None
    def argv():
        """list-of-str QCoreApplication.argv()"""
        return [str()]
    def argc():
        """int QCoreApplication.argc()"""
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

    def __init__(_type):
        """None QEvent.__init__(QEvent.Type _type)"""
        return None
    def __init__():
        """QEvent QEvent.__init__()"""
        return QEvent()
    def registerEventType(_hint):
        """int QEvent.registerEventType(int _hint)"""
        return int()
    def ignore():
        """None QEvent.ignore()"""
        return None
    def accept():
        """None QEvent.accept()"""
        return None
    def isAccepted():
        """bool QEvent.isAccepted()"""
        return bool()
    def setAccepted(_accepted):
        """None QEvent.setAccepted(bool _accepted)"""
        return None
    def spontaneous():
        """bool QEvent.spontaneous()"""
        return bool()
    def type():
        """QEvent.Type QEvent.type()"""
        return QEvent.Type()


class QTimerEvent(QEvent):
    """"""
    def __init__(_timerId):
        """None QTimerEvent.__init__(int _timerId)"""
        return None
    def __init__():
        """QTimerEvent QTimerEvent.__init__()"""
        return QTimerEvent()
    def timerId():
        """int QTimerEvent.timerId()"""
        return int()


class QChildEvent(QEvent):
    """"""
    def __init__(_type, _child):
        """None QChildEvent.__init__(QEvent.Type _type, QObject _child)"""
        return None
    def __init__():
        """QChildEvent QChildEvent.__init__()"""
        return QChildEvent()
    def removed():
        """bool QChildEvent.removed()"""
        return bool()
    def polished():
        """bool QChildEvent.polished()"""
        return bool()
    def added():
        """bool QChildEvent.added()"""
        return bool()
    def child():
        """QObject QChildEvent.child()"""
        return QObject()


class QDynamicPropertyChangeEvent(QEvent):
    """"""
    def __init__(_name):
        """None QDynamicPropertyChangeEvent.__init__(QByteArray _name)"""
        return None
    def __init__():
        """QDynamicPropertyChangeEvent QDynamicPropertyChangeEvent.__init__()"""
        return QDynamicPropertyChangeEvent()
    def propertyName():
        """QByteArray QDynamicPropertyChangeEvent.propertyName()"""
        return QByteArray()


class QCryptographicHash():
    """"""
    Md4 = int() # QCryptographicHash.Algorithm enum
    Md5 = int() # QCryptographicHash.Algorithm enum
    Sha1 = int() # QCryptographicHash.Algorithm enum

    def __init__(_method):
        """None QCryptographicHash.__init__(QCryptographicHash.Algorithm _method)"""
        return None
    def hash(_data, _method):
        """QByteArray QCryptographicHash.hash(QByteArray _data, QCryptographicHash.Algorithm _method)"""
        return QByteArray()
    def result():
        """QByteArray QCryptographicHash.result()"""
        return QByteArray()
    def addData(_data):
        """None QCryptographicHash.addData(str _data)"""
        return None
    def addData(_data):
        """None QCryptographicHash.addData(QByteArray _data)"""
        return None
    def reset():
        """None QCryptographicHash.reset()"""
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

    def __init__():
        """None QDataStream.__init__()"""
        return None
    def __init__():
        """QIODevice QDataStream.__init__()"""
        return QIODevice()
    def __init__(_flags):
        """QByteArray QDataStream.__init__(QIODevice.OpenMode _flags)"""
        return QByteArray()
    def __init__():
        """QByteArray QDataStream.__init__()"""
        return QByteArray()
    def __lshift__():
        """QBitArray QDataStream.__lshift__()"""
        return QBitArray()
    def __lshift__():
        """QByteArray QDataStream.__lshift__()"""
        return QByteArray()
    def __lshift__():
        """QChar QDataStream.__lshift__()"""
        return QChar()
    def __lshift__():
        """QDate QDataStream.__lshift__()"""
        return QDate()
    def __lshift__():
        """QTime QDataStream.__lshift__()"""
        return QTime()
    def __lshift__():
        """QDateTime QDataStream.__lshift__()"""
        return QDateTime()
    def __lshift__():
        """QEasingCurve QDataStream.__lshift__()"""
        return QEasingCurve()
    def __lshift__():
        """QLine QDataStream.__lshift__()"""
        return QLine()
    def __lshift__():
        """QLineF QDataStream.__lshift__()"""
        return QLineF()
    def __lshift__():
        """QLocale QDataStream.__lshift__()"""
        return QLocale()
    def __lshift__():
        """QPoint QDataStream.__lshift__()"""
        return QPoint()
    def __lshift__():
        """QPointF QDataStream.__lshift__()"""
        return QPointF()
    def __lshift__():
        """QRect QDataStream.__lshift__()"""
        return QRect()
    def __lshift__():
        """QRectF QDataStream.__lshift__()"""
        return QRectF()
    def __lshift__(_regExp):
        """QDataStream QDataStream.__lshift__(QRegExp _regExp)"""
        return QDataStream()
    def __lshift__():
        """QSize QDataStream.__lshift__()"""
        return QSize()
    def __lshift__():
        """QSizeF QDataStream.__lshift__()"""
        return QSizeF()
    def __lshift__():
        """QString QDataStream.__lshift__()"""
        return QString()
    def __lshift__(_list):
        """QDataStream QDataStream.__lshift__(QStringList _list)"""
        return QDataStream()
    def __lshift__():
        """QUrl QDataStream.__lshift__()"""
        return QUrl()
    def __lshift__():
        """QUuid QDataStream.__lshift__()"""
        return QUuid()
    def __lshift__(_p):
        """QDataStream QDataStream.__lshift__(QVariant _p)"""
        return QDataStream()
    def __lshift__(_p):
        """QDataStream QDataStream.__lshift__(Type _p)"""
        return QDataStream()
    def __rshift__():
        """QBitArray QDataStream.__rshift__()"""
        return QBitArray()
    def __rshift__():
        """QByteArray QDataStream.__rshift__()"""
        return QByteArray()
    def __rshift__():
        """QChar QDataStream.__rshift__()"""
        return QChar()
    def __rshift__():
        """QDate QDataStream.__rshift__()"""
        return QDate()
    def __rshift__():
        """QTime QDataStream.__rshift__()"""
        return QTime()
    def __rshift__():
        """QDateTime QDataStream.__rshift__()"""
        return QDateTime()
    def __rshift__():
        """QEasingCurve QDataStream.__rshift__()"""
        return QEasingCurve()
    def __rshift__():
        """QLine QDataStream.__rshift__()"""
        return QLine()
    def __rshift__():
        """QLineF QDataStream.__rshift__()"""
        return QLineF()
    def __rshift__():
        """QLocale QDataStream.__rshift__()"""
        return QLocale()
    def __rshift__():
        """QPoint QDataStream.__rshift__()"""
        return QPoint()
    def __rshift__():
        """QPointF QDataStream.__rshift__()"""
        return QPointF()
    def __rshift__():
        """QRect QDataStream.__rshift__()"""
        return QRect()
    def __rshift__():
        """QRectF QDataStream.__rshift__()"""
        return QRectF()
    def __rshift__(_regExp):
        """QDataStream QDataStream.__rshift__(QRegExp _regExp)"""
        return QDataStream()
    def __rshift__():
        """QSize QDataStream.__rshift__()"""
        return QSize()
    def __rshift__():
        """QSizeF QDataStream.__rshift__()"""
        return QSizeF()
    def __rshift__():
        """QString QDataStream.__rshift__()"""
        return QString()
    def __rshift__(_list):
        """QDataStream QDataStream.__rshift__(QStringList _list)"""
        return QDataStream()
    def __rshift__():
        """QUrl QDataStream.__rshift__()"""
        return QUrl()
    def __rshift__():
        """QUuid QDataStream.__rshift__()"""
        return QUuid()
    def __rshift__(_p):
        """QDataStream QDataStream.__rshift__(QVariant _p)"""
        return QDataStream()
    def __rshift__(_p):
        """QDataStream QDataStream.__rshift__(Type _p)"""
        return QDataStream()
    def setFloatingPointPrecision(_precision):
        """None QDataStream.setFloatingPointPrecision(QDataStream.FloatingPointPrecision _precision)"""
        return None
    def floatingPointPrecision():
        """QDataStream.FloatingPointPrecision QDataStream.floatingPointPrecision()"""
        return QDataStream.FloatingPointPrecision()
    def writeRawData():
        """str QDataStream.writeRawData()"""
        return str()
    def writeBytes():
        """str QDataStream.writeBytes()"""
        return str()
    def readRawData(_len):
        """str QDataStream.readRawData(int _len)"""
        return str()
    def readBytes():
        """str QDataStream.readBytes()"""
        return str()
    def writeQVariantHash(_qvarhash):
        """None QDataStream.writeQVariantHash(dict-of-QString-QVariant _qvarhash)"""
        return None
    def readQVariantHash():
        """dict-of-QString-QVariant QDataStream.readQVariantHash()"""
        return dict-of-QString-QVariant()
    def writeQVariantMap(_qvarmap):
        """None QDataStream.writeQVariantMap(dict-of-QString-QVariant _qvarmap)"""
        return None
    def readQVariantMap():
        """dict-of-QString-QVariant QDataStream.readQVariantMap()"""
        return dict-of-QString-QVariant()
    def writeQVariantList(_qvarlst):
        """None QDataStream.writeQVariantList(list-of-QVariant _qvarlst)"""
        return None
    def readQVariantList():
        """list-of-QVariant QDataStream.readQVariantList()"""
        return [QVariant()]
    def writeQVariant(_qvar):
        """None QDataStream.writeQVariant(QVariant _qvar)"""
        return None
    def readQVariant():
        """QVariant QDataStream.readQVariant()"""
        return QVariant()
    def writeQStringList(_qstrlst):
        """None QDataStream.writeQStringList(QStringList _qstrlst)"""
        return None
    def readQStringList():
        """QStringList QDataStream.readQStringList()"""
        return QStringList()
    def writeQString(_qstr):
        """None QDataStream.writeQString(QString _qstr)"""
        return None
    def readQString():
        """QString QDataStream.readQString()"""
        return QString()
    def writeString(_str):
        """None QDataStream.writeString(str _str)"""
        return None
    def writeDouble(_f):
        """None QDataStream.writeDouble(float _f)"""
        return None
    def writeFloat(_f):
        """None QDataStream.writeFloat(float _f)"""
        return None
    def writeBool(_i):
        """None QDataStream.writeBool(bool _i)"""
        return None
    def writeUInt64(_i):
        """None QDataStream.writeUInt64(int _i)"""
        return None
    def writeInt64(_i):
        """None QDataStream.writeInt64(int _i)"""
        return None
    def writeUInt32(_i):
        """None QDataStream.writeUInt32(int _i)"""
        return None
    def writeInt32(_i):
        """None QDataStream.writeInt32(int _i)"""
        return None
    def writeUInt16(_i):
        """None QDataStream.writeUInt16(int _i)"""
        return None
    def writeInt16(_i):
        """None QDataStream.writeInt16(int _i)"""
        return None
    def writeUInt8(_i):
        """None QDataStream.writeUInt8(str _i)"""
        return None
    def writeInt8(_i):
        """None QDataStream.writeInt8(str _i)"""
        return None
    def writeInt(_i):
        """None QDataStream.writeInt(int _i)"""
        return None
    def readString():
        """str QDataStream.readString()"""
        return str()
    def readDouble():
        """float QDataStream.readDouble()"""
        return float()
    def readFloat():
        """float QDataStream.readFloat()"""
        return float()
    def readBool():
        """bool QDataStream.readBool()"""
        return bool()
    def readUInt64():
        """int QDataStream.readUInt64()"""
        return int()
    def readInt64():
        """int QDataStream.readInt64()"""
        return int()
    def readUInt32():
        """int QDataStream.readUInt32()"""
        return int()
    def readInt32():
        """int QDataStream.readInt32()"""
        return int()
    def readUInt16():
        """int QDataStream.readUInt16()"""
        return int()
    def readInt16():
        """int QDataStream.readInt16()"""
        return int()
    def readUInt8():
        """str QDataStream.readUInt8()"""
        return str()
    def readInt8():
        """str QDataStream.readInt8()"""
        return str()
    def readInt():
        """int QDataStream.readInt()"""
        return int()
    def skipRawData(_len):
        """int QDataStream.skipRawData(int _len)"""
        return int()
    def setVersion(_v):
        """None QDataStream.setVersion(int _v)"""
        return None
    def version():
        """int QDataStream.version()"""
        return int()
    def setByteOrder():
        """QDataStream.ByteOrder QDataStream.setByteOrder()"""
        return QDataStream.ByteOrder()
    def byteOrder():
        """QDataStream.ByteOrder QDataStream.byteOrder()"""
        return QDataStream.ByteOrder()
    def resetStatus():
        """None QDataStream.resetStatus()"""
        return None
    def setStatus(_status):
        """None QDataStream.setStatus(QDataStream.Status _status)"""
        return None
    def status():
        """QDataStream.Status QDataStream.status()"""
        return QDataStream.Status()
    def atEnd():
        """bool QDataStream.atEnd()"""
        return bool()
    def unsetDevice():
        """None QDataStream.unsetDevice()"""
        return None
    def setDevice():
        """QIODevice QDataStream.setDevice()"""
        return QIODevice()
    def device():
        """QIODevice QDataStream.device()"""
        return QIODevice()


class QDate():
    """"""
    DateFormat = int() # QDate.MonthNameType enum
    StandaloneFormat = int() # QDate.MonthNameType enum

    def __init__():
        """None QDate.__init__()"""
        return None
    def __init__(_y, _m, _d):
        """None QDate.__init__(int _y, int _m, int _d)"""
        return None
    def __init__():
        """QDate QDate.__init__()"""
        return QDate()
    def getDate(_year, _month, _day):
        """None QDate.getDate(int _year, int _month, int _day)"""
        return None
    def setDate(_year, _month, _date):
        """bool QDate.setDate(int _year, int _month, int _date)"""
        return bool()
    def toJulianDay():
        """int QDate.toJulianDay()"""
        return int()
    def fromJulianDay(_jd):
        """QDate QDate.fromJulianDay(int _jd)"""
        return QDate()
    def julianToGregorian(_jd, _y, _m, _d):
        """None QDate.julianToGregorian(int _jd, int _y, int _m, int _d)"""
        return None
    def gregorianToJulian(_y, _m, _d):
        """int QDate.gregorianToJulian(int _y, int _m, int _d)"""
        return int()
    def isLeapYear(_year):
        """bool QDate.isLeapYear(int _year)"""
        return bool()
    def fromString(_string, _format):
        """QDate QDate.fromString(QString _string, Qt.DateFormat _format)"""
        return QDate()
    def fromString(_s, _format):
        """QDate QDate.fromString(QString _s, QString _format)"""
        return QDate()
    def currentDate():
        """QDate QDate.currentDate()"""
        return QDate()
    def __ge__(_other):
        """bool QDate.__ge__(QDate _other)"""
        return bool()
    def __gt__(_other):
        """bool QDate.__gt__(QDate _other)"""
        return bool()
    def __le__(_other):
        """bool QDate.__le__(QDate _other)"""
        return bool()
    def __lt__(_other):
        """bool QDate.__lt__(QDate _other)"""
        return bool()
    def __ne__(_other):
        """bool QDate.__ne__(QDate _other)"""
        return bool()
    def __eq__(_other):
        """bool QDate.__eq__(QDate _other)"""
        return bool()
    def daysTo():
        """QDate QDate.daysTo()"""
        return QDate()
    def addYears(_years):
        """QDate QDate.addYears(int _years)"""
        return QDate()
    def addMonths(_months):
        """QDate QDate.addMonths(int _months)"""
        return QDate()
    def addDays(_days):
        """QDate QDate.addDays(int _days)"""
        return QDate()
    def setYMD(_y, _m, _d):
        """bool QDate.setYMD(int _y, int _m, int _d)"""
        return bool()
    def toString(_format):
        """QString QDate.toString(Qt.DateFormat _format)"""
        return QString()
    def toString(_format):
        """QString QDate.toString(QString _format)"""
        return QString()
    def longDayName(_weekday):
        """QString QDate.longDayName(int _weekday)"""
        return QString()
    def longDayName(_weekday, _type):
        """QString QDate.longDayName(int _weekday, QDate.MonthNameType _type)"""
        return QString()
    def longMonthName(_month):
        """QString QDate.longMonthName(int _month)"""
        return QString()
    def longMonthName(_month, _type):
        """QString QDate.longMonthName(int _month, QDate.MonthNameType _type)"""
        return QString()
    def shortDayName(_weekday):
        """QString QDate.shortDayName(int _weekday)"""
        return QString()
    def shortDayName(_weekday, _type):
        """QString QDate.shortDayName(int _weekday, QDate.MonthNameType _type)"""
        return QString()
    def shortMonthName(_month):
        """QString QDate.shortMonthName(int _month)"""
        return QString()
    def shortMonthName(_month, _type):
        """QString QDate.shortMonthName(int _month, QDate.MonthNameType _type)"""
        return QString()
    def weekNumber(_yearNumber):
        """int QDate.weekNumber(int _yearNumber)"""
        return int()
    def daysInYear():
        """int QDate.daysInYear()"""
        return int()
    def daysInMonth():
        """int QDate.daysInMonth()"""
        return int()
    def dayOfYear():
        """int QDate.dayOfYear()"""
        return int()
    def dayOfWeek():
        """int QDate.dayOfWeek()"""
        return int()
    def day():
        """int QDate.day()"""
        return int()
    def month():
        """int QDate.month()"""
        return int()
    def year():
        """int QDate.year()"""
        return int()
    def isValid():
        """bool QDate.isValid()"""
        return bool()
    def isValid(_y, _m, _d):
        """bool QDate.isValid(int _y, int _m, int _d)"""
        return bool()
    def __bool__():
        """int QDate.__bool__()"""
        return int()
    def isNull():
        """bool QDate.isNull()"""
        return bool()
    def toPyDate():
        """datetime.date QDate.toPyDate()"""
        return datetime.date()
    def __hash__():
        """int QDate.__hash__()"""
        return int()
    def __repr__():
        """str QDate.__repr__()"""
        return str()


class QTime():
    """"""
    def __init__():
        """None QTime.__init__()"""
        return None
    def __init__(_h, _m, _second, _msec):
        """None QTime.__init__(int _h, int _m, int _second, int _msec)"""
        return None
    def __init__():
        """QTime QTime.__init__()"""
        return QTime()
    def elapsed():
        """int QTime.elapsed()"""
        return int()
    def restart():
        """int QTime.restart()"""
        return int()
    def start():
        """None QTime.start()"""
        return None
    def fromString(_string, _format):
        """QTime QTime.fromString(QString _string, Qt.DateFormat _format)"""
        return QTime()
    def fromString(_s, _format):
        """QTime QTime.fromString(QString _s, QString _format)"""
        return QTime()
    def currentTime():
        """QTime QTime.currentTime()"""
        return QTime()
    def __ge__(_other):
        """bool QTime.__ge__(QTime _other)"""
        return bool()
    def __gt__(_other):
        """bool QTime.__gt__(QTime _other)"""
        return bool()
    def __le__(_other):
        """bool QTime.__le__(QTime _other)"""
        return bool()
    def __lt__(_other):
        """bool QTime.__lt__(QTime _other)"""
        return bool()
    def __ne__(_other):
        """bool QTime.__ne__(QTime _other)"""
        return bool()
    def __eq__(_other):
        """bool QTime.__eq__(QTime _other)"""
        return bool()
    def msecsTo():
        """QTime QTime.msecsTo()"""
        return QTime()
    def addMSecs(_ms):
        """QTime QTime.addMSecs(int _ms)"""
        return QTime()
    def secsTo():
        """QTime QTime.secsTo()"""
        return QTime()
    def addSecs(_secs):
        """QTime QTime.addSecs(int _secs)"""
        return QTime()
    def setHMS(_h, _m, _s, _msec):
        """bool QTime.setHMS(int _h, int _m, int _s, int _msec)"""
        return bool()
    def toString(_format):
        """QString QTime.toString(Qt.DateFormat _format)"""
        return QString()
    def toString(_format):
        """QString QTime.toString(QString _format)"""
        return QString()
    def msec():
        """int QTime.msec()"""
        return int()
    def second():
        """int QTime.second()"""
        return int()
    def minute():
        """int QTime.minute()"""
        return int()
    def hour():
        """int QTime.hour()"""
        return int()
    def isValid():
        """bool QTime.isValid()"""
        return bool()
    def isValid(_h, _m, _s, _msec):
        """bool QTime.isValid(int _h, int _m, int _s, int _msec)"""
        return bool()
    def __bool__():
        """int QTime.__bool__()"""
        return int()
    def isNull():
        """bool QTime.isNull()"""
        return bool()
    def toPyTime():
        """datetime.time QTime.toPyTime()"""
        return datetime.time()
    def __hash__():
        """int QTime.__hash__()"""
        return int()
    def __repr__():
        """str QTime.__repr__()"""
        return str()


class QDateTime():
    """"""
    def __init__():
        """None QDateTime.__init__()"""
        return None
    def __init__(_other):
        """None QDateTime.__init__(QDateTime _other)"""
        return None
    def __init__():
        """QDate QDateTime.__init__()"""
        return QDate()
    def __init__(_date, _time, _timeSpec):
        """None QDateTime.__init__(QDate _date, QTime _time, Qt.TimeSpec _timeSpec)"""
        return None
    def __init__(_y, _m, _d, _h, _m_, _s, _msec, _timeSpec):
        """None QDateTime.__init__(int _y, int _m, int _d, int _h, int _m_, int _s, int _msec, int _timeSpec)"""
        return None
    def currentMSecsSinceEpoch():
        """int QDateTime.currentMSecsSinceEpoch()"""
        return int()
    def fromMSecsSinceEpoch(_msecs):
        """QDateTime QDateTime.fromMSecsSinceEpoch(int _msecs)"""
        return QDateTime()
    def currentDateTimeUtc():
        """QDateTime QDateTime.currentDateTimeUtc()"""
        return QDateTime()
    def msecsTo():
        """QDateTime QDateTime.msecsTo()"""
        return QDateTime()
    def setMSecsSinceEpoch(_msecs):
        """None QDateTime.setMSecsSinceEpoch(int _msecs)"""
        return None
    def toMSecsSinceEpoch():
        """int QDateTime.toMSecsSinceEpoch()"""
        return int()
    def fromTime_t(_secsSince1Jan1970UTC):
        """QDateTime QDateTime.fromTime_t(int _secsSince1Jan1970UTC)"""
        return QDateTime()
    def fromString(_string, _format):
        """QDateTime QDateTime.fromString(QString _string, Qt.DateFormat _format)"""
        return QDateTime()
    def fromString(_s, _format):
        """QDateTime QDateTime.fromString(QString _s, QString _format)"""
        return QDateTime()
    def currentDateTime():
        """QDateTime QDateTime.currentDateTime()"""
        return QDateTime()
    def __ge__(_other):
        """bool QDateTime.__ge__(QDateTime _other)"""
        return bool()
    def __gt__(_other):
        """bool QDateTime.__gt__(QDateTime _other)"""
        return bool()
    def __le__(_other):
        """bool QDateTime.__le__(QDateTime _other)"""
        return bool()
    def __lt__(_other):
        """bool QDateTime.__lt__(QDateTime _other)"""
        return bool()
    def __ne__(_other):
        """bool QDateTime.__ne__(QDateTime _other)"""
        return bool()
    def __eq__(_other):
        """bool QDateTime.__eq__(QDateTime _other)"""
        return bool()
    def secsTo():
        """QDateTime QDateTime.secsTo()"""
        return QDateTime()
    def daysTo():
        """QDateTime QDateTime.daysTo()"""
        return QDateTime()
    def toUTC():
        """QDateTime QDateTime.toUTC()"""
        return QDateTime()
    def toLocalTime():
        """QDateTime QDateTime.toLocalTime()"""
        return QDateTime()
    def toTimeSpec(_spec):
        """QDateTime QDateTime.toTimeSpec(Qt.TimeSpec _spec)"""
        return QDateTime()
    def addMSecs(_msecs):
        """QDateTime QDateTime.addMSecs(int _msecs)"""
        return QDateTime()
    def addSecs(_secs):
        """QDateTime QDateTime.addSecs(int _secs)"""
        return QDateTime()
    def addYears(_years):
        """QDateTime QDateTime.addYears(int _years)"""
        return QDateTime()
    def addMonths(_months):
        """QDateTime QDateTime.addMonths(int _months)"""
        return QDateTime()
    def addDays(_days):
        """QDateTime QDateTime.addDays(int _days)"""
        return QDateTime()
    def toString(_format):
        """QString QDateTime.toString(Qt.DateFormat _format)"""
        return QString()
    def toString(_format):
        """QString QDateTime.toString(QString _format)"""
        return QString()
    def setTime_t(_secsSince1Jan1970UTC):
        """None QDateTime.setTime_t(int _secsSince1Jan1970UTC)"""
        return None
    def setTimeSpec(_spec):
        """None QDateTime.setTimeSpec(Qt.TimeSpec _spec)"""
        return None
    def setTime(_time):
        """None QDateTime.setTime(QTime _time)"""
        return None
    def setDate(_date):
        """None QDateTime.setDate(QDate _date)"""
        return None
    def toTime_t():
        """int QDateTime.toTime_t()"""
        return int()
    def timeSpec():
        """Qt.TimeSpec QDateTime.timeSpec()"""
        return Qt.TimeSpec()
    def time():
        """QTime QDateTime.time()"""
        return QTime()
    def date():
        """QDate QDateTime.date()"""
        return QDate()
    def isValid():
        """bool QDateTime.isValid()"""
        return bool()
    def __bool__():
        """int QDateTime.__bool__()"""
        return int()
    def isNull():
        """bool QDateTime.isNull()"""
        return bool()
    def toPyDateTime():
        """datetime.datetime QDateTime.toPyDateTime()"""
        return datetime.datetime()
    def __hash__():
        """int QDateTime.__hash__()"""
        return int()
    def __repr__():
        """str QDateTime.__repr__()"""
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

    def __init__():
        """QDir QDir.__init__()"""
        return QDir()
    def __init__(_path):
        """None QDir.__init__(QString _path)"""
        return None
    def __init__(_path, _nameFilter, _sort, _filters):
        """None QDir.__init__(QString _path, QString _nameFilter, QDir.SortFlags _sort, QDir.Filters _filters)"""
        return None
    def searchPaths(_prefix):
        """QStringList QDir.searchPaths(QString _prefix)"""
        return QStringList()
    def addSearchPath(_prefix, _path):
        """None QDir.addSearchPath(QString _prefix, QString _path)"""
        return None
    def setSearchPaths(_prefix, _searchPaths):
        """None QDir.setSearchPaths(QString _prefix, QStringList _searchPaths)"""
        return None
    def fromNativeSeparators(_pathName):
        """QString QDir.fromNativeSeparators(QString _pathName)"""
        return QString()
    def toNativeSeparators(_pathName):
        """QString QDir.toNativeSeparators(QString _pathName)"""
        return QString()
    def cleanPath(_path):
        """QString QDir.cleanPath(QString _path)"""
        return QString()
    def match(_filters, _fileName):
        """bool QDir.match(QStringList _filters, QString _fileName)"""
        return bool()
    def match(_filter, _fileName):
        """bool QDir.match(QString _filter, QString _fileName)"""
        return bool()
    def tempPath():
        """QString QDir.tempPath()"""
        return QString()
    def temp():
        """QDir QDir.temp()"""
        return QDir()
    def rootPath():
        """QString QDir.rootPath()"""
        return QString()
    def root():
        """QDir QDir.root()"""
        return QDir()
    def homePath():
        """QString QDir.homePath()"""
        return QString()
    def home():
        """QDir QDir.home()"""
        return QDir()
    def currentPath():
        """QString QDir.currentPath()"""
        return QString()
    def current():
        """QDir QDir.current()"""
        return QDir()
    def setCurrent(_path):
        """bool QDir.setCurrent(QString _path)"""
        return bool()
    def separator():
        """QChar QDir.separator()"""
        return QChar()
    def drives():
        """list-of-QFileInfo QDir.drives()"""
        return [QFileInfo()]
    def refresh():
        """None QDir.refresh()"""
        return None
    def rename(_oldName, _newName):
        """bool QDir.rename(QString _oldName, QString _newName)"""
        return bool()
    def remove(_fileName):
        """bool QDir.remove(QString _fileName)"""
        return bool()
    def __ne__(_dir):
        """bool QDir.__ne__(QDir _dir)"""
        return bool()
    def __eq__(_dir):
        """bool QDir.__eq__(QDir _dir)"""
        return bool()
    def makeAbsolute():
        """bool QDir.makeAbsolute()"""
        return bool()
    def isAbsolute():
        """bool QDir.isAbsolute()"""
        return bool()
    def isRelative():
        """bool QDir.isRelative()"""
        return bool()
    def isAbsolutePath(_path):
        """bool QDir.isAbsolutePath(QString _path)"""
        return bool()
    def isRelativePath(_path):
        """bool QDir.isRelativePath(QString _path)"""
        return bool()
    def isRoot():
        """bool QDir.isRoot()"""
        return bool()
    def exists():
        """bool QDir.exists()"""
        return bool()
    def exists(_name):
        """bool QDir.exists(QString _name)"""
        return bool()
    def isReadable():
        """bool QDir.isReadable()"""
        return bool()
    def rmpath(_dirPath):
        """bool QDir.rmpath(QString _dirPath)"""
        return bool()
    def mkpath(_dirPath):
        """bool QDir.mkpath(QString _dirPath)"""
        return bool()
    def rmdir(_dirName):
        """bool QDir.rmdir(QString _dirName)"""
        return bool()
    def mkdir(_dirName):
        """bool QDir.mkdir(QString _dirName)"""
        return bool()
    def entryInfoList(_filters, _sort):
        """list-of-QFileInfo QDir.entryInfoList(QDir.Filters _filters, QDir.SortFlags _sort)"""
        return [QFileInfo()]
    def entryInfoList(_nameFilters, _filters, _sort):
        """list-of-QFileInfo QDir.entryInfoList(QStringList _nameFilters, QDir.Filters _filters, QDir.SortFlags _sort)"""
        return [QFileInfo()]
    def entryList(_filters, _sort):
        """QStringList QDir.entryList(QDir.Filters _filters, QDir.SortFlags _sort)"""
        return QStringList()
    def entryList(_nameFilters, _filters, _sort):
        """QStringList QDir.entryList(QStringList _nameFilters, QDir.Filters _filters, QDir.SortFlags _sort)"""
        return QStringList()
    def nameFiltersFromString(_nameFilter):
        """QStringList QDir.nameFiltersFromString(QString _nameFilter)"""
        return QStringList()
    def __contains__():
        """QString QDir.__contains__()"""
        return QString()
    def __getitem__():
        """int QDir.__getitem__()"""
        return int()
    def __getitem__():
        """slice QDir.__getitem__()"""
        return slice()
    def __len__():
        """ QDir.__len__()"""
        return ()
    def count():
        """int QDir.count()"""
        return int()
    def setSorting(_sort):
        """None QDir.setSorting(QDir.SortFlags _sort)"""
        return None
    def sorting():
        """QDir.SortFlags QDir.sorting()"""
        return QDir.SortFlags()
    def setFilter(_filter):
        """None QDir.setFilter(QDir.Filters _filter)"""
        return None
    def filter():
        """QDir.Filters QDir.filter()"""
        return QDir.Filters()
    def setNameFilters(_nameFilters):
        """None QDir.setNameFilters(QStringList _nameFilters)"""
        return None
    def nameFilters():
        """QStringList QDir.nameFilters()"""
        return QStringList()
    def cdUp():
        """bool QDir.cdUp()"""
        return bool()
    def cd(_dirName):
        """bool QDir.cd(QString _dirName)"""
        return bool()
    def convertSeparators(_pathName):
        """QString QDir.convertSeparators(QString _pathName)"""
        return QString()
    def relativeFilePath(_fileName):
        """QString QDir.relativeFilePath(QString _fileName)"""
        return QString()
    def absoluteFilePath(_fileName):
        """QString QDir.absoluteFilePath(QString _fileName)"""
        return QString()
    def filePath(_fileName):
        """QString QDir.filePath(QString _fileName)"""
        return QString()
    def dirName():
        """QString QDir.dirName()"""
        return QString()
    def addResourceSearchPath(_path):
        """None QDir.addResourceSearchPath(QString _path)"""
        return None
    def canonicalPath():
        """QString QDir.canonicalPath()"""
        return QString()
    def absolutePath():
        """QString QDir.absolutePath()"""
        return QString()
    def path():
        """QString QDir.path()"""
        return QString()
    def setPath(_path):
        """None QDir.setPath(QString _path)"""
        return None


class QDirIterator():
    """"""
    NoIteratorFlags = int() # QDirIterator.IteratorFlag enum
    FollowSymlinks = int() # QDirIterator.IteratorFlag enum
    Subdirectories = int() # QDirIterator.IteratorFlag enum

    def __init__(_dir, _flags):
        """None QDirIterator.__init__(QDir _dir, QDirIterator.IteratorFlags _flags)"""
        return None
    def __init__(_path, _flags):
        """None QDirIterator.__init__(QString _path, QDirIterator.IteratorFlags _flags)"""
        return None
    def __init__(_path, _filters, _flags):
        """None QDirIterator.__init__(QString _path, QDir.Filters _filters, QDirIterator.IteratorFlags _flags)"""
        return None
    def __init__(_path, _nameFilters, _filters, _flags):
        """None QDirIterator.__init__(QString _path, QStringList _nameFilters, QDir.Filters _filters, QDirIterator.IteratorFlags _flags)"""
        return None
    def path():
        """QString QDirIterator.path()"""
        return QString()
    def fileInfo():
        """QFileInfo QDirIterator.fileInfo()"""
        return QFileInfo()
    def filePath():
        """QString QDirIterator.filePath()"""
        return QString()
    def fileName():
        """QString QDirIterator.fileName()"""
        return QString()
    def hasNext():
        """bool QDirIterator.hasNext()"""
        return bool()
    def next():
        """QString QDirIterator.next()"""
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

    def __init__(_type):
        """None QEasingCurve.__init__(QEasingCurve.Type _type)"""
        return None
    def __init__(_other):
        """None QEasingCurve.__init__(QEasingCurve _other)"""
        return None
    def valueForProgress(_progress):
        """float QEasingCurve.valueForProgress(float _progress)"""
        return float()
    def customType():
        """callable QEasingCurve.customType()"""
        return callable()
    def setCustomType(_func):
        """None QEasingCurve.setCustomType(callable _func)"""
        return None
    def setType(_type):
        """None QEasingCurve.setType(QEasingCurve.Type _type)"""
        return None
    def type():
        """QEasingCurve.Type QEasingCurve.type()"""
        return QEasingCurve.Type()
    def setOvershoot(_overshoot):
        """None QEasingCurve.setOvershoot(float _overshoot)"""
        return None
    def overshoot():
        """float QEasingCurve.overshoot()"""
        return float()
    def setPeriod(_period):
        """None QEasingCurve.setPeriod(float _period)"""
        return None
    def period():
        """float QEasingCurve.period()"""
        return float()
    def setAmplitude(_amplitude):
        """None QEasingCurve.setAmplitude(float _amplitude)"""
        return None
    def amplitude():
        """float QEasingCurve.amplitude()"""
        return float()
    def __ne__(_other):
        """bool QEasingCurve.__ne__(QEasingCurve _other)"""
        return bool()
    def __eq__(_other):
        """bool QEasingCurve.__eq__(QEasingCurve _other)"""
        return bool()


class QElapsedTimer():
    """"""
    SystemTime = int() # QElapsedTimer.ClockType enum
    MonotonicClock = int() # QElapsedTimer.ClockType enum
    TickCounter = int() # QElapsedTimer.ClockType enum
    MachAbsoluteTime = int() # QElapsedTimer.ClockType enum

    def __init__():
        """None QElapsedTimer.__init__()"""
        return None
    def __init__():
        """QElapsedTimer QElapsedTimer.__init__()"""
        return QElapsedTimer()
    def __ge__(_v2):
        """bool QElapsedTimer.__ge__(QElapsedTimer _v2)"""
        return bool()
    def __lt__(_v2):
        """bool QElapsedTimer.__lt__(QElapsedTimer _v2)"""
        return bool()
    def __ne__(_other):
        """bool QElapsedTimer.__ne__(QElapsedTimer _other)"""
        return bool()
    def __eq__(_other):
        """bool QElapsedTimer.__eq__(QElapsedTimer _other)"""
        return bool()
    def secsTo(_other):
        """int QElapsedTimer.secsTo(QElapsedTimer _other)"""
        return int()
    def msecsTo(_other):
        """int QElapsedTimer.msecsTo(QElapsedTimer _other)"""
        return int()
    def msecsSinceReference():
        """int QElapsedTimer.msecsSinceReference()"""
        return int()
    def hasExpired(_timeout):
        """bool QElapsedTimer.hasExpired(int _timeout)"""
        return bool()
    def elapsed():
        """int QElapsedTimer.elapsed()"""
        return int()
    def isValid():
        """bool QElapsedTimer.isValid()"""
        return bool()
    def invalidate():
        """None QElapsedTimer.invalidate()"""
        return None
    def restart():
        """int QElapsedTimer.restart()"""
        return int()
    def start():
        """None QElapsedTimer.start()"""
        return None
    def isMonotonic():
        """bool QElapsedTimer.isMonotonic()"""
        return bool()
    def clockType():
        """QElapsedTimer.ClockType QElapsedTimer.clockType()"""
        return QElapsedTimer.ClockType()


class QEventLoop(QObject):
    """"""
    AllEvents = int() # QEventLoop.ProcessEventsFlag enum
    ExcludeUserInputEvents = int() # QEventLoop.ProcessEventsFlag enum
    ExcludeSocketNotifiers = int() # QEventLoop.ProcessEventsFlag enum
    WaitForMoreEvents = int() # QEventLoop.ProcessEventsFlag enum
    X11ExcludeTimers = int() # QEventLoop.ProcessEventsFlag enum
    DeferredDeletion = int() # QEventLoop.ProcessEventsFlag enum

    def __init__(_parent):
        """None QEventLoop.__init__(QObject _parent)"""
        return None
    def quit():
        """None QEventLoop.quit()"""
        return None
    def wakeUp():
        """None QEventLoop.wakeUp()"""
        return None
    def isRunning():
        """bool QEventLoop.isRunning()"""
        return bool()
    def exit(_returnCode):
        """None QEventLoop.exit(int _returnCode)"""
        return None
    def exec_(_flags):
        """int QEventLoop.exec_(QEventLoop.ProcessEventsFlags _flags)"""
        return int()
    def processEvents(_flags):
        """bool QEventLoop.processEvents(QEventLoop.ProcessEventsFlags _flags)"""
        return bool()
    def processEvents(_flags, _maximumTime):
        """None QEventLoop.processEvents(QEventLoop.ProcessEventsFlags _flags, int _maximumTime)"""
        return None


class QEventTransition(QAbstractTransition):
    """"""
    def __init__(_sourceState):
        """None QEventTransition.__init__(QState _sourceState)"""
        return None
    def __init__(_object, _type, _sourceState):
        """None QEventTransition.__init__(QObject _object, QEvent.Type _type, QState _sourceState)"""
        return None
    def event(_e):
        """bool QEventTransition.event(QEvent _e)"""
        return bool()
    def onTransition(_event):
        """None QEventTransition.onTransition(QEvent _event)"""
        return None
    def eventTest(_event):
        """bool QEventTransition.eventTest(QEvent _event)"""
        return bool()
    def setEventType(_type):
        """None QEventTransition.setEventType(QEvent.Type _type)"""
        return None
    def eventType():
        """QEvent.Type QEventTransition.eventType()"""
        return QEvent.Type()
    def setEventSource(_object):
        """None QEventTransition.setEventSource(QObject _object)"""
        return None
    def eventSource():
        """QObject QEventTransition.eventSource()"""
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

    def __init__():
        """None QFile.__init__()"""
        return None
    def __init__(_name):
        """None QFile.__init__(QString _name)"""
        return None
    def __init__(_parent):
        """None QFile.__init__(QObject _parent)"""
        return None
    def __init__(_name, _parent):
        """None QFile.__init__(QString _name, QObject _parent)"""
        return None
    def writeData(_data):
        """int QFile.writeData(str _data)"""
        return int()
    def readLineData(_maxlen):
        """str QFile.readLineData(int _maxlen)"""
        return str()
    def readData(_maxlen):
        """str QFile.readData(int _maxlen)"""
        return str()
    def unmap(_address):
        """bool QFile.unmap(sip.voidptr _address)"""
        return bool()
    def map(_offset, _size, _flags):
        """sip.voidptr QFile.map(int _offset, int _size, QFile.MemoryMapFlags _flags)"""
        return sip.voidptr()
    def symLinkTarget():
        """QString QFile.symLinkTarget()"""
        return QString()
    def symLinkTarget(_fileName):
        """QString QFile.symLinkTarget(QString _fileName)"""
        return QString()
    def fileEngine():
        """QAbstractFileEngine QFile.fileEngine()"""
        return QAbstractFileEngine()
    def handle():
        """int QFile.handle()"""
        return int()
    def setPermissions(_permissionSpec):
        """bool QFile.setPermissions(QFile.Permissions _permissionSpec)"""
        return bool()
    def setPermissions(_filename, _permissionSpec):
        """bool QFile.setPermissions(QString _filename, QFile.Permissions _permissionSpec)"""
        return bool()
    def permissions():
        """QFile.Permissions QFile.permissions()"""
        return QFile.Permissions()
    def permissions(_filename):
        """QFile.Permissions QFile.permissions(QString _filename)"""
        return QFile.Permissions()
    def resize(_sz):
        """bool QFile.resize(int _sz)"""
        return bool()
    def resize(_filename, _sz):
        """bool QFile.resize(QString _filename, int _sz)"""
        return bool()
    def flush():
        """bool QFile.flush()"""
        return bool()
    def atEnd():
        """bool QFile.atEnd()"""
        return bool()
    def seek(_offset):
        """bool QFile.seek(int _offset)"""
        return bool()
    def pos():
        """int QFile.pos()"""
        return int()
    def size():
        """int QFile.size()"""
        return int()
    def close():
        """None QFile.close()"""
        return None
    def open(_flags):
        """bool QFile.open(QIODevice.OpenMode _flags)"""
        return bool()
    def open(_fd, _flags):
        """bool QFile.open(int _fd, QIODevice.OpenMode _flags)"""
        return bool()
    def isSequential():
        """bool QFile.isSequential()"""
        return bool()
    def copy(_newName):
        """bool QFile.copy(QString _newName)"""
        return bool()
    def copy(_fileName, _newName):
        """bool QFile.copy(QString _fileName, QString _newName)"""
        return bool()
    def link(_newName):
        """bool QFile.link(QString _newName)"""
        return bool()
    def link(_oldname, _newName):
        """bool QFile.link(QString _oldname, QString _newName)"""
        return bool()
    def rename(_newName):
        """bool QFile.rename(QString _newName)"""
        return bool()
    def rename(_oldName, _newName):
        """bool QFile.rename(QString _oldName, QString _newName)"""
        return bool()
    def remove():
        """bool QFile.remove()"""
        return bool()
    def remove(_fileName):
        """bool QFile.remove(QString _fileName)"""
        return bool()
    def readLink():
        """QString QFile.readLink()"""
        return QString()
    def readLink(_fileName):
        """QString QFile.readLink(QString _fileName)"""
        return QString()
    def exists():
        """bool QFile.exists()"""
        return bool()
    def exists(_fileName):
        """bool QFile.exists(QString _fileName)"""
        return bool()
    def decodeName(_localFileName):
        """QString QFile.decodeName(QByteArray _localFileName)"""
        return QString()
    def decodeName(_localFileName):
        """QString QFile.decodeName(str _localFileName)"""
        return QString()
    def encodeName(_fileName):
        """QByteArray QFile.encodeName(QString _fileName)"""
        return QByteArray()
    def setFileName(_name):
        """None QFile.setFileName(QString _name)"""
        return None
    def fileName():
        """QString QFile.fileName()"""
        return QString()
    def unsetError():
        """None QFile.unsetError()"""
        return None
    def error():
        """QFile.FileError QFile.error()"""
        return QFile.FileError()


class QFileInfo():
    """"""
    def __init__():
        """None QFileInfo.__init__()"""
        return None
    def __init__(_file):
        """None QFileInfo.__init__(QString _file)"""
        return None
    def __init__(_file):
        """None QFileInfo.__init__(QFile _file)"""
        return None
    def __init__(_dir, _file):
        """None QFileInfo.__init__(QDir _dir, QString _file)"""
        return None
    def __init__(_fileinfo):
        """None QFileInfo.__init__(QFileInfo _fileinfo)"""
        return None
    def isBundle():
        """bool QFileInfo.isBundle()"""
        return bool()
    def bundleName():
        """QString QFileInfo.bundleName()"""
        return QString()
    def symLinkTarget():
        """QString QFileInfo.symLinkTarget()"""
        return QString()
    def setCaching(_on):
        """None QFileInfo.setCaching(bool _on)"""
        return None
    def caching():
        """bool QFileInfo.caching()"""
        return bool()
    def detach():
        """None QFileInfo.detach()"""
        return None
    def lastRead():
        """QDateTime QFileInfo.lastRead()"""
        return QDateTime()
    def lastModified():
        """QDateTime QFileInfo.lastModified()"""
        return QDateTime()
    def created():
        """QDateTime QFileInfo.created()"""
        return QDateTime()
    def size():
        """int QFileInfo.size()"""
        return int()
    def permissions():
        """QFile.Permissions QFileInfo.permissions()"""
        return QFile.Permissions()
    def permission(_permissions):
        """bool QFileInfo.permission(QFile.Permissions _permissions)"""
        return bool()
    def groupId():
        """int QFileInfo.groupId()"""
        return int()
    def group():
        """QString QFileInfo.group()"""
        return QString()
    def ownerId():
        """int QFileInfo.ownerId()"""
        return int()
    def owner():
        """QString QFileInfo.owner()"""
        return QString()
    def readLink():
        """QString QFileInfo.readLink()"""
        return QString()
    def isRoot():
        """bool QFileInfo.isRoot()"""
        return bool()
    def isSymLink():
        """bool QFileInfo.isSymLink()"""
        return bool()
    def isDir():
        """bool QFileInfo.isDir()"""
        return bool()
    def isFile():
        """bool QFileInfo.isFile()"""
        return bool()
    def makeAbsolute():
        """bool QFileInfo.makeAbsolute()"""
        return bool()
    def isAbsolute():
        """bool QFileInfo.isAbsolute()"""
        return bool()
    def isRelative():
        """bool QFileInfo.isRelative()"""
        return bool()
    def isHidden():
        """bool QFileInfo.isHidden()"""
        return bool()
    def isExecutable():
        """bool QFileInfo.isExecutable()"""
        return bool()
    def isWritable():
        """bool QFileInfo.isWritable()"""
        return bool()
    def isReadable():
        """bool QFileInfo.isReadable()"""
        return bool()
    def absoluteDir():
        """QDir QFileInfo.absoluteDir()"""
        return QDir()
    def dir():
        """QDir QFileInfo.dir()"""
        return QDir()
    def canonicalPath():
        """QString QFileInfo.canonicalPath()"""
        return QString()
    def absolutePath():
        """QString QFileInfo.absolutePath()"""
        return QString()
    def path():
        """QString QFileInfo.path()"""
        return QString()
    def completeSuffix():
        """QString QFileInfo.completeSuffix()"""
        return QString()
    def suffix():
        """QString QFileInfo.suffix()"""
        return QString()
    def completeBaseName():
        """QString QFileInfo.completeBaseName()"""
        return QString()
    def baseName():
        """QString QFileInfo.baseName()"""
        return QString()
    def fileName():
        """QString QFileInfo.fileName()"""
        return QString()
    def canonicalFilePath():
        """QString QFileInfo.canonicalFilePath()"""
        return QString()
    def absoluteFilePath():
        """QString QFileInfo.absoluteFilePath()"""
        return QString()
    def filePath():
        """QString QFileInfo.filePath()"""
        return QString()
    def refresh():
        """None QFileInfo.refresh()"""
        return None
    def exists():
        """bool QFileInfo.exists()"""
        return bool()
    def setFile(_file):
        """None QFileInfo.setFile(QString _file)"""
        return None
    def setFile(_file):
        """None QFileInfo.setFile(QFile _file)"""
        return None
    def setFile(_dir, _file):
        """None QFileInfo.setFile(QDir _dir, QString _file)"""
        return None
    def __ne__(_fileinfo):
        """bool QFileInfo.__ne__(QFileInfo _fileinfo)"""
        return bool()
    def __eq__(_fileinfo):
        """bool QFileInfo.__eq__(QFileInfo _fileinfo)"""
        return bool()


class QFileSystemWatcher(QObject):
    """"""
    def __init__(_parent):
        """None QFileSystemWatcher.__init__(QObject _parent)"""
        return None
    def __init__(_paths, _parent):
        """None QFileSystemWatcher.__init__(QStringList _paths, QObject _parent)"""
        return None
    def removePaths(_files):
        """None QFileSystemWatcher.removePaths(QStringList _files)"""
        return None
    def removePath(_file):
        """None QFileSystemWatcher.removePath(QString _file)"""
        return None
    def files():
        """QStringList QFileSystemWatcher.files()"""
        return QStringList()
    def directories():
        """QStringList QFileSystemWatcher.directories()"""
        return QStringList()
    def addPaths(_files):
        """None QFileSystemWatcher.addPaths(QStringList _files)"""
        return None
    def addPath(_file):
        """None QFileSystemWatcher.addPath(QString _file)"""
        return None


class QFinalState(QAbstractState):
    """"""
    def __init__(_parent):
        """None QFinalState.__init__(QState _parent)"""
        return None
    def event(_e):
        """bool QFinalState.event(QEvent _e)"""
        return bool()
    def onExit(_event):
        """None QFinalState.onExit(QEvent _event)"""
        return None
    def onEntry(_event):
        """None QFinalState.onEntry(QEvent _event)"""
        return None


class QFSFileEngine(QAbstractFileEngine):
    """"""
    def __init__():
        """None QFSFileEngine.__init__()"""
        return None
    def __init__(_file):
        """None QFSFileEngine.__init__(QString _file)"""
        return None
    def drives():
        """list-of-QFileInfo QFSFileEngine.drives()"""
        return [QFileInfo()]
    def tempPath():
        """QString QFSFileEngine.tempPath()"""
        return QString()
    def rootPath():
        """QString QFSFileEngine.rootPath()"""
        return QString()
    def homePath():
        """QString QFSFileEngine.homePath()"""
        return QString()
    def currentPath(_fileName):
        """QString QFSFileEngine.currentPath(QString _fileName)"""
        return QString()
    def setCurrentPath(_path):
        """bool QFSFileEngine.setCurrentPath(QString _path)"""
        return bool()
    def write(_data):
        """int QFSFileEngine.write(str _data)"""
        return int()
    def readLine(_maxlen):
        """str QFSFileEngine.readLine(int _maxlen)"""
        return str()
    def read(_maxlen):
        """str QFSFileEngine.read(int _maxlen)"""
        return str()
    def handle():
        """int QFSFileEngine.handle()"""
        return int()
    def setFileName(_file):
        """None QFSFileEngine.setFileName(QString _file)"""
        return None
    def fileTime(_time):
        """QDateTime QFSFileEngine.fileTime(QAbstractFileEngine.FileTime _time)"""
        return QDateTime()
    def owner():
        """QAbstractFileEngine.FileOwner QFSFileEngine.owner()"""
        return QAbstractFileEngine.FileOwner()
    def ownerId():
        """QAbstractFileEngine.FileOwner QFSFileEngine.ownerId()"""
        return QAbstractFileEngine.FileOwner()
    def fileName(_file):
        """QString QFSFileEngine.fileName(QAbstractFileEngine.FileName _file)"""
        return QString()
    def setPermissions(_perms):
        """bool QFSFileEngine.setPermissions(int _perms)"""
        return bool()
    def fileFlags(_type):
        """QAbstractFileEngine.FileFlags QFSFileEngine.fileFlags(QAbstractFileEngine.FileFlags _type)"""
        return QAbstractFileEngine.FileFlags()
    def entryList(_filters, _filterNames):
        """QStringList QFSFileEngine.entryList(QDir.Filters _filters, QStringList _filterNames)"""
        return QStringList()
    def isRelativePath():
        """bool QFSFileEngine.isRelativePath()"""
        return bool()
    def caseSensitive():
        """bool QFSFileEngine.caseSensitive()"""
        return bool()
    def setSize(_size):
        """bool QFSFileEngine.setSize(int _size)"""
        return bool()
    def rmdir(_dirName, _recurseParentDirectories):
        """bool QFSFileEngine.rmdir(QString _dirName, bool _recurseParentDirectories)"""
        return bool()
    def mkdir(_dirName, _createParentDirectories):
        """bool QFSFileEngine.mkdir(QString _dirName, bool _createParentDirectories)"""
        return bool()
    def link(_newName):
        """bool QFSFileEngine.link(QString _newName)"""
        return bool()
    def rename(_newName):
        """bool QFSFileEngine.rename(QString _newName)"""
        return bool()
    def copy(_newName):
        """bool QFSFileEngine.copy(QString _newName)"""
        return bool()
    def remove():
        """bool QFSFileEngine.remove()"""
        return bool()
    def isSequential():
        """bool QFSFileEngine.isSequential()"""
        return bool()
    def seek():
        """int QFSFileEngine.seek()"""
        return int()
    def pos():
        """int QFSFileEngine.pos()"""
        return int()
    def size():
        """int QFSFileEngine.size()"""
        return int()
    def flush():
        """bool QFSFileEngine.flush()"""
        return bool()
    def close():
        """bool QFSFileEngine.close()"""
        return bool()
    def open(_openMode):
        """bool QFSFileEngine.open(QIODevice.OpenMode _openMode)"""
        return bool()
    def open(_flags, _fd):
        """bool QFSFileEngine.open(QIODevice.OpenMode _flags, int _fd)"""
        return bool()


class QHistoryState(QAbstractState):
    """"""
    ShallowHistory = int() # QHistoryState.HistoryType enum
    DeepHistory = int() # QHistoryState.HistoryType enum

    def __init__(_parent):
        """None QHistoryState.__init__(QState _parent)"""
        return None
    def __init__(_type, _parent):
        """None QHistoryState.__init__(QHistoryState.HistoryType _type, QState _parent)"""
        return None
    def event(_e):
        """bool QHistoryState.event(QEvent _e)"""
        return bool()
    def onExit(_event):
        """None QHistoryState.onExit(QEvent _event)"""
        return None
    def onEntry(_event):
        """None QHistoryState.onEntry(QEvent _event)"""
        return None
    def setHistoryType(_type):
        """None QHistoryState.setHistoryType(QHistoryState.HistoryType _type)"""
        return None
    def historyType():
        """QHistoryState.HistoryType QHistoryState.historyType()"""
        return QHistoryState.HistoryType()
    def setDefaultState(_state):
        """None QHistoryState.setDefaultState(QAbstractState _state)"""
        return None
    def defaultState():
        """QAbstractState QHistoryState.defaultState()"""
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

    def __init__():
        """QLibraryInfo QLibraryInfo.__init__()"""
        return QLibraryInfo()
    def buildDate():
        """QDate QLibraryInfo.buildDate()"""
        return QDate()
    def location():
        """QLibraryInfo.LibraryLocation QLibraryInfo.location()"""
        return QLibraryInfo.LibraryLocation()
    def buildKey():
        """QString QLibraryInfo.buildKey()"""
        return QString()
    def licensedProducts():
        """QString QLibraryInfo.licensedProducts()"""
        return QString()
    def licensee():
        """QString QLibraryInfo.licensee()"""
        return QString()


class QLine():
    """"""
    def __init__():
        """None QLine.__init__()"""
        return None
    def __init__(_pt1_, _pt2_):
        """None QLine.__init__(QPoint _pt1_, QPoint _pt2_)"""
        return None
    def __init__(_x1pos, _y1pos, _x2pos, _y2pos):
        """None QLine.__init__(int _x1pos, int _y1pos, int _x2pos, int _y2pos)"""
        return None
    def __init__():
        """QLine QLine.__init__()"""
        return QLine()
    def setLine(_aX1, _aY1, _aX2, _aY2):
        """None QLine.setLine(int _aX1, int _aY1, int _aX2, int _aY2)"""
        return None
    def setPoints(_aP1, _aP2):
        """None QLine.setPoints(QPoint _aP1, QPoint _aP2)"""
        return None
    def setP2(_aP2):
        """None QLine.setP2(QPoint _aP2)"""
        return None
    def setP1(_aP1):
        """None QLine.setP1(QPoint _aP1)"""
        return None
    def translated(_p):
        """QLine QLine.translated(QPoint _p)"""
        return QLine()
    def translated(_adx, _ady):
        """QLine QLine.translated(int _adx, int _ady)"""
        return QLine()
    def __eq__(_d):
        """bool QLine.__eq__(QLine _d)"""
        return bool()
    def translate(_point):
        """None QLine.translate(QPoint _point)"""
        return None
    def translate(_adx, _ady):
        """None QLine.translate(int _adx, int _ady)"""
        return None
    def dy():
        """int QLine.dy()"""
        return int()
    def dx():
        """int QLine.dx()"""
        return int()
    def p2():
        """QPoint QLine.p2()"""
        return QPoint()
    def p1():
        """QPoint QLine.p1()"""
        return QPoint()
    def y2():
        """int QLine.y2()"""
        return int()
    def x2():
        """int QLine.x2()"""
        return int()
    def y1():
        """int QLine.y1()"""
        return int()
    def x1():
        """int QLine.x1()"""
        return int()
    def __bool__():
        """int QLine.__bool__()"""
        return int()
    def isNull():
        """bool QLine.isNull()"""
        return bool()
    def __repr__():
        """str QLine.__repr__()"""
        return str()
    def __ne__(_d):
        """bool QLine.__ne__(QLine _d)"""
        return bool()


class QLineF():
    """"""
    NoIntersection = int() # QLineF.IntersectType enum
    BoundedIntersection = int() # QLineF.IntersectType enum
    UnboundedIntersection = int() # QLineF.IntersectType enum

    def __init__(_line):
        """None QLineF.__init__(QLine _line)"""
        return None
    def __init__():
        """None QLineF.__init__()"""
        return None
    def __init__(_apt1, _apt2):
        """None QLineF.__init__(QPointF _apt1, QPointF _apt2)"""
        return None
    def __init__(_x1pos, _y1pos, _x2pos, _y2pos):
        """None QLineF.__init__(float _x1pos, float _y1pos, float _x2pos, float _y2pos)"""
        return None
    def __init__():
        """QLineF QLineF.__init__()"""
        return QLineF()
    def setLine(_aX1, _aY1, _aX2, _aY2):
        """None QLineF.setLine(float _aX1, float _aY1, float _aX2, float _aY2)"""
        return None
    def setPoints(_aP1, _aP2):
        """None QLineF.setPoints(QPointF _aP1, QPointF _aP2)"""
        return None
    def setP2(_aP2):
        """None QLineF.setP2(QPointF _aP2)"""
        return None
    def setP1(_aP1):
        """None QLineF.setP1(QPointF _aP1)"""
        return None
    def translated(_p):
        """QLineF QLineF.translated(QPointF _p)"""
        return QLineF()
    def translated(_adx, _ady):
        """QLineF QLineF.translated(float _adx, float _ady)"""
        return QLineF()
    def angleTo(_l):
        """float QLineF.angleTo(QLineF _l)"""
        return float()
    def setAngle(_angle):
        """None QLineF.setAngle(float _angle)"""
        return None
    def fromPolar(_length, _angle):
        """QLineF QLineF.fromPolar(float _length, float _angle)"""
        return QLineF()
    def __eq__(_d):
        """bool QLineF.__eq__(QLineF _d)"""
        return bool()
    def toLine():
        """QLine QLineF.toLine()"""
        return QLine()
    def pointAt(_t):
        """QPointF QLineF.pointAt(float _t)"""
        return QPointF()
    def setLength(_len):
        """None QLineF.setLength(float _len)"""
        return None
    def translate(_point):
        """None QLineF.translate(QPointF _point)"""
        return None
    def translate(_adx, _ady):
        """None QLineF.translate(float _adx, float _ady)"""
        return None
    def normalVector():
        """QLineF QLineF.normalVector()"""
        return QLineF()
    def dy():
        """float QLineF.dy()"""
        return float()
    def dx():
        """float QLineF.dx()"""
        return float()
    def p2():
        """QPointF QLineF.p2()"""
        return QPointF()
    def p1():
        """QPointF QLineF.p1()"""
        return QPointF()
    def y2():
        """float QLineF.y2()"""
        return float()
    def x2():
        """float QLineF.x2()"""
        return float()
    def y1():
        """float QLineF.y1()"""
        return float()
    def x1():
        """float QLineF.x1()"""
        return float()
    def __repr__():
        """str QLineF.__repr__()"""
        return str()
    def __ne__(_d):
        """bool QLineF.__ne__(QLineF _d)"""
        return bool()
    def angle(_l):
        """float QLineF.angle(QLineF _l)"""
        return float()
    def angle():
        """float QLineF.angle()"""
        return float()
    def intersect(_l, _intersectionPoint):
        """QLineF.IntersectType QLineF.intersect(QLineF _l, QPointF _intersectionPoint)"""
        return QLineF.IntersectType()
    def unitVector():
        """QLineF QLineF.unitVector()"""
        return QLineF()
    def length():
        """float QLineF.length()"""
        return float()
    def __bool__():
        """int QLineF.__bool__()"""
        return int()
    def isNull():
        """bool QLineF.isNull()"""
        return bool()


class QLibrary(QObject):
    """"""
    ResolveAllSymbolsHint = int() # QLibrary.LoadHint enum
    ExportExternalSymbolsHint = int() # QLibrary.LoadHint enum
    LoadArchiveMemberHint = int() # QLibrary.LoadHint enum

    def __init__(_parent):
        """None QLibrary.__init__(QObject _parent)"""
        return None
    def __init__(_fileName, _parent):
        """None QLibrary.__init__(QString _fileName, QObject _parent)"""
        return None
    def __init__(_fileName, _verNum, _parent):
        """None QLibrary.__init__(QString _fileName, int _verNum, QObject _parent)"""
        return None
    def __init__(_fileName, _version, _parent):
        """None QLibrary.__init__(QString _fileName, QString _version, QObject _parent)"""
        return None
    def setLoadHints(_hints):
        """None QLibrary.setLoadHints(QLibrary.LoadHints _hints)"""
        return None
    def setFileNameAndVersion(_fileName, _verNum):
        """None QLibrary.setFileNameAndVersion(QString _fileName, int _verNum)"""
        return None
    def setFileNameAndVersion(_fileName, _version):
        """None QLibrary.setFileNameAndVersion(QString _fileName, QString _version)"""
        return None
    def setFileName(_fileName):
        """None QLibrary.setFileName(QString _fileName)"""
        return None
    def isLibrary(_fileName):
        """bool QLibrary.isLibrary(QString _fileName)"""
        return bool()
    def unload():
        """bool QLibrary.unload()"""
        return bool()
    def resolve(_symbol):
        """sip.voidptr QLibrary.resolve(str _symbol)"""
        return sip.voidptr()
    def resolve(_fileName, _symbol):
        """sip.voidptr QLibrary.resolve(QString _fileName, str _symbol)"""
        return sip.voidptr()
    def resolve(_fileName, _verNum, _symbol):
        """sip.voidptr QLibrary.resolve(QString _fileName, int _verNum, str _symbol)"""
        return sip.voidptr()
    def resolve(_fileName, _version, _symbol):
        """sip.voidptr QLibrary.resolve(QString _fileName, QString _version, str _symbol)"""
        return sip.voidptr()
    def loadHints():
        """QLibrary.LoadHints QLibrary.loadHints()"""
        return QLibrary.LoadHints()
    def load():
        """bool QLibrary.load()"""
        return bool()
    def isLoaded():
        """bool QLibrary.isLoaded()"""
        return bool()
    def fileName():
        """QString QLibrary.fileName()"""
        return QString()
    def errorString():
        """QString QLibrary.errorString()"""
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

    def __init__():
        """None QLocale.__init__()"""
        return None
    def __init__(_name):
        """None QLocale.__init__(QString _name)"""
        return None
    def __init__(_language, _country):
        """None QLocale.__init__(QLocale.Language _language, QLocale.Country _country)"""
        return None
    def __init__(_other):
        """None QLocale.__init__(QLocale _other)"""
        return None
    def textDirection():
        """Qt.LayoutDirection QLocale.textDirection()"""
        return Qt.LayoutDirection()
    def pmText():
        """QString QLocale.pmText()"""
        return QString()
    def amText():
        """QString QLocale.amText()"""
        return QString()
    def standaloneDayName(_format):
        """int QLocale.standaloneDayName(QLocale.FormatType _format)"""
        return int()
    def standaloneMonthName(_format):
        """int QLocale.standaloneMonthName(QLocale.FormatType _format)"""
        return int()
    def positiveSign():
        """QChar QLocale.positiveSign()"""
        return QChar()
    def measurementSystem():
        """QLocale.MeasurementSystem QLocale.measurementSystem()"""
        return QLocale.MeasurementSystem()
    def countriesForLanguage(_lang):
        """list-of-QLocale.Country QLocale.countriesForLanguage(QLocale.Language _lang)"""
        return [QLocale.Country()]
    def numberOptions():
        """QLocale.NumberOptions QLocale.numberOptions()"""
        return QLocale.NumberOptions()
    def setNumberOptions(_options):
        """None QLocale.setNumberOptions(QLocale.NumberOptions _options)"""
        return None
    def dayName(_format):
        """int QLocale.dayName(QLocale.FormatType _format)"""
        return int()
    def monthName(_format):
        """int QLocale.monthName(QLocale.FormatType _format)"""
        return int()
    def exponential():
        """QChar QLocale.exponential()"""
        return QChar()
    def negativeSign():
        """QChar QLocale.negativeSign()"""
        return QChar()
    def zeroDigit():
        """QChar QLocale.zeroDigit()"""
        return QChar()
    def percent():
        """QChar QLocale.percent()"""
        return QChar()
    def groupSeparator():
        """QChar QLocale.groupSeparator()"""
        return QChar()
    def decimalPoint():
        """QChar QLocale.decimalPoint()"""
        return QChar()
    def toDateTime(_string, _format):
        """QDateTime QLocale.toDateTime(QString _string, QLocale.FormatType _format)"""
        return QDateTime()
    def toDateTime(_string, _format):
        """QDateTime QLocale.toDateTime(QString _string, QString _format)"""
        return QDateTime()
    def toTime(_string, _format):
        """QTime QLocale.toTime(QString _string, QLocale.FormatType _format)"""
        return QTime()
    def toTime(_string, _format):
        """QTime QLocale.toTime(QString _string, QString _format)"""
        return QTime()
    def toDate(_string, _format):
        """QDate QLocale.toDate(QString _string, QLocale.FormatType _format)"""
        return QDate()
    def toDate(_string, _format):
        """QDate QLocale.toDate(QString _string, QString _format)"""
        return QDate()
    def dateTimeFormat(_format):
        """QString QLocale.dateTimeFormat(QLocale.FormatType _format)"""
        return QString()
    def timeFormat(_format):
        """QString QLocale.timeFormat(QLocale.FormatType _format)"""
        return QString()
    def dateFormat(_format):
        """QString QLocale.dateFormat(QLocale.FormatType _format)"""
        return QString()
    def system():
        """QLocale QLocale.system()"""
        return QLocale()
    def c():
        """QLocale QLocale.c()"""
        return QLocale()
    def setDefault(_locale):
        """None QLocale.setDefault(QLocale _locale)"""
        return None
    def countryToString(_country):
        """QString QLocale.countryToString(QLocale.Country _country)"""
        return QString()
    def languageToString(_language):
        """QString QLocale.languageToString(QLocale.Language _language)"""
        return QString()
    def __ne__(_other):
        """bool QLocale.__ne__(QLocale _other)"""
        return bool()
    def __eq__(_other):
        """bool QLocale.__eq__(QLocale _other)"""
        return bool()
    def toString(_i):
        """QString QLocale.toString(int _i)"""
        return QString()
    def toString(_i, _format, _precision):
        """QString QLocale.toString(float _i, str _format, int _precision)"""
        return QString()
    def toString(_i):
        """QString QLocale.toString(int _i)"""
        return QString()
    def toString(_i):
        """QString QLocale.toString(int _i)"""
        return QString()
    def toString(_dateTime, _format):
        """QString QLocale.toString(QDateTime _dateTime, QString _format)"""
        return QString()
    def toString(_dateTime, _format):
        """QString QLocale.toString(QDateTime _dateTime, QLocale.FormatType _format)"""
        return QString()
    def toString(_date, _formatStr):
        """QString QLocale.toString(QDate _date, QString _formatStr)"""
        return QString()
    def toString(_date, _format):
        """QString QLocale.toString(QDate _date, QLocale.FormatType _format)"""
        return QString()
    def toString(_time, _formatStr):
        """QString QLocale.toString(QTime _time, QString _formatStr)"""
        return QString()
    def toString(_time, _format):
        """QString QLocale.toString(QTime _time, QLocale.FormatType _format)"""
        return QString()
    def toDouble(_s, _ok):
        """float QLocale.toDouble(QString _s, bool _ok)"""
        return float()
    def toFloat(_s, _ok):
        """float QLocale.toFloat(QString _s, bool _ok)"""
        return float()
    def toULongLong(_s, _ok, _base):
        """int QLocale.toULongLong(QString _s, bool _ok, int _base)"""
        return int()
    def toLongLong(_s, _ok, _base):
        """int QLocale.toLongLong(QString _s, bool _ok, int _base)"""
        return int()
    def toUInt(_s, _ok, _base):
        """int QLocale.toUInt(QString _s, bool _ok, int _base)"""
        return int()
    def toInt(_s, _ok, _base):
        """int QLocale.toInt(QString _s, bool _ok, int _base)"""
        return int()
    def toUShort(_s, _ok, _base):
        """int QLocale.toUShort(QString _s, bool _ok, int _base)"""
        return int()
    def toShort(_s, _ok, _base):
        """int QLocale.toShort(QString _s, bool _ok, int _base)"""
        return int()
    def name():
        """QString QLocale.name()"""
        return QString()
    def country():
        """QLocale.Country QLocale.country()"""
        return QLocale.Country()
    def language():
        """QLocale.Language QLocale.language()"""
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

    def __init__():
        """None QSystemLocale.__init__()"""
        return None
    def __init__():
        """QSystemLocale QSystemLocale.__init__()"""
        return QSystemLocale()
    def fallbackLocale():
        """QLocale QSystemLocale.fallbackLocale()"""
        return QLocale()
    def query(_type, _in):
        """QVariant QSystemLocale.query(QSystemLocale.QueryType _type, QVariant _in)"""
        return QVariant()


class QMargins():
    """"""
    def __init__():
        """None QMargins.__init__()"""
        return None
    def __init__(_aleft, _atop, _aright, _abottom):
        """None QMargins.__init__(int _aleft, int _atop, int _aright, int _abottom)"""
        return None
    def __init__():
        """QMargins QMargins.__init__()"""
        return QMargins()
    def __eq__(_m2):
        """bool QMargins.__eq__(QMargins _m2)"""
        return bool()
    def __ne__(_m2):
        """bool QMargins.__ne__(QMargins _m2)"""
        return bool()
    def setBottom(_abottom):
        """None QMargins.setBottom(int _abottom)"""
        return None
    def setRight(_aright):
        """None QMargins.setRight(int _aright)"""
        return None
    def setTop(_atop):
        """None QMargins.setTop(int _atop)"""
        return None
    def setLeft(_aleft):
        """None QMargins.setLeft(int _aleft)"""
        return None
    def bottom():
        """int QMargins.bottom()"""
        return int()
    def right():
        """int QMargins.right()"""
        return int()
    def top():
        """int QMargins.top()"""
        return int()
    def left():
        """int QMargins.left()"""
        return int()
    def isNull():
        """bool QMargins.isNull()"""
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

    def __init__():
        """None QMetaMethod.__init__()"""
        return None
    def __init__():
        """QMetaMethod QMetaMethod.__init__()"""
        return QMetaMethod()
    def methodIndex():
        """int QMetaMethod.methodIndex()"""
        return int()
    def invoke(_object, _connectionType, _returnValue, _value0, _value1, _value2, _value3, _value4, _value5, _value6, _value7, _value8, _value9):
        """object QMetaMethod.invoke(QObject _object, Qt.ConnectionType _connectionType, QGenericReturnArgument _returnValue, QGenericArgument _value0, QGenericArgument _value1, QGenericArgument _value2, QGenericArgument _value3, QGenericArgument _value4, QGenericArgument _value5, QGenericArgument _value6, QGenericArgument _value7, QGenericArgument _value8, QGenericArgument _value9)"""
        return object()
    def invoke(_object, _returnValue, _value0, _value1, _value2, _value3, _value4, _value5, _value6, _value7, _value8, _value9):
        """object QMetaMethod.invoke(QObject _object, QGenericReturnArgument _returnValue, QGenericArgument _value0, QGenericArgument _value1, QGenericArgument _value2, QGenericArgument _value3, QGenericArgument _value4, QGenericArgument _value5, QGenericArgument _value6, QGenericArgument _value7, QGenericArgument _value8, QGenericArgument _value9)"""
        return object()
    def invoke(_object, _connectionType, _value0, _value1, _value2, _value3, _value4, _value5, _value6, _value7, _value8, _value9):
        """object QMetaMethod.invoke(QObject _object, Qt.ConnectionType _connectionType, QGenericArgument _value0, QGenericArgument _value1, QGenericArgument _value2, QGenericArgument _value3, QGenericArgument _value4, QGenericArgument _value5, QGenericArgument _value6, QGenericArgument _value7, QGenericArgument _value8, QGenericArgument _value9)"""
        return object()
    def invoke(_object, _value0, _value1, _value2, _value3, _value4, _value5, _value6, _value7, _value8, _value9):
        """object QMetaMethod.invoke(QObject _object, QGenericArgument _value0, QGenericArgument _value1, QGenericArgument _value2, QGenericArgument _value3, QGenericArgument _value4, QGenericArgument _value5, QGenericArgument _value6, QGenericArgument _value7, QGenericArgument _value8, QGenericArgument _value9)"""
        return object()
    def methodType():
        """QMetaMethod.MethodType QMetaMethod.methodType()"""
        return QMetaMethod.MethodType()
    def access():
        """QMetaMethod.Access QMetaMethod.access()"""
        return QMetaMethod.Access()
    def tag():
        """str QMetaMethod.tag()"""
        return str()
    def parameterNames():
        """list-of-QByteArray QMetaMethod.parameterNames()"""
        return [QByteArray()]
    def parameterTypes():
        """list-of-QByteArray QMetaMethod.parameterTypes()"""
        return [QByteArray()]
    def typeName():
        """str QMetaMethod.typeName()"""
        return str()
    def signature():
        """str QMetaMethod.signature()"""
        return str()


class QMetaEnum():
    """"""
    def __init__():
        """None QMetaEnum.__init__()"""
        return None
    def __init__():
        """QMetaEnum QMetaEnum.__init__()"""
        return QMetaEnum()
    def isValid():
        """bool QMetaEnum.isValid()"""
        return bool()
    def valueToKeys(_value):
        """QByteArray QMetaEnum.valueToKeys(int _value)"""
        return QByteArray()
    def keysToValue(_keys):
        """int QMetaEnum.keysToValue(str _keys)"""
        return int()
    def valueToKey(_value):
        """str QMetaEnum.valueToKey(int _value)"""
        return str()
    def keyToValue(_key):
        """int QMetaEnum.keyToValue(str _key)"""
        return int()
    def scope():
        """str QMetaEnum.scope()"""
        return str()
    def value(_index):
        """int QMetaEnum.value(int _index)"""
        return int()
    def key(_index):
        """str QMetaEnum.key(int _index)"""
        return str()
    def keyCount():
        """int QMetaEnum.keyCount()"""
        return int()
    def isFlag():
        """bool QMetaEnum.isFlag()"""
        return bool()
    def name():
        """str QMetaEnum.name()"""
        return str()


class QMetaProperty():
    """"""
    def __init__():
        """None QMetaProperty.__init__()"""
        return None
    def __init__():
        """QMetaProperty QMetaProperty.__init__()"""
        return QMetaProperty()
    def isFinal():
        """bool QMetaProperty.isFinal()"""
        return bool()
    def isConstant():
        """bool QMetaProperty.isConstant()"""
        return bool()
    def propertyIndex():
        """int QMetaProperty.propertyIndex()"""
        return int()
    def notifySignalIndex():
        """int QMetaProperty.notifySignalIndex()"""
        return int()
    def notifySignal():
        """QMetaMethod QMetaProperty.notifySignal()"""
        return QMetaMethod()
    def hasNotifySignal():
        """bool QMetaProperty.hasNotifySignal()"""
        return bool()
    def userType():
        """int QMetaProperty.userType()"""
        return int()
    def isUser(_object):
        """bool QMetaProperty.isUser(QObject _object)"""
        return bool()
    def isResettable():
        """bool QMetaProperty.isResettable()"""
        return bool()
    def isValid():
        """bool QMetaProperty.isValid()"""
        return bool()
    def hasStdCppSet():
        """bool QMetaProperty.hasStdCppSet()"""
        return bool()
    def reset(_obj):
        """bool QMetaProperty.reset(QObject _obj)"""
        return bool()
    def write(_obj, _value):
        """bool QMetaProperty.write(QObject _obj, QVariant _value)"""
        return bool()
    def read(_obj):
        """QVariant QMetaProperty.read(QObject _obj)"""
        return QVariant()
    def enumerator():
        """QMetaEnum QMetaProperty.enumerator()"""
        return QMetaEnum()
    def isEnumType():
        """bool QMetaProperty.isEnumType()"""
        return bool()
    def isFlagType():
        """bool QMetaProperty.isFlagType()"""
        return bool()
    def isEditable(_object):
        """bool QMetaProperty.isEditable(QObject _object)"""
        return bool()
    def isStored(_object):
        """bool QMetaProperty.isStored(QObject _object)"""
        return bool()
    def isScriptable(_object):
        """bool QMetaProperty.isScriptable(QObject _object)"""
        return bool()
    def isDesignable(_object):
        """bool QMetaProperty.isDesignable(QObject _object)"""
        return bool()
    def isWritable():
        """bool QMetaProperty.isWritable()"""
        return bool()
    def isReadable():
        """bool QMetaProperty.isReadable()"""
        return bool()
    def type():
        """Type QMetaProperty.type()"""
        return Type()
    def typeName():
        """str QMetaProperty.typeName()"""
        return str()
    def name():
        """str QMetaProperty.name()"""
        return str()


class QMetaClassInfo():
    """"""
    def __init__():
        """None QMetaClassInfo.__init__()"""
        return None
    def __init__():
        """QMetaClassInfo QMetaClassInfo.__init__()"""
        return QMetaClassInfo()
    def value():
        """str QMetaClassInfo.value()"""
        return str()
    def name():
        """str QMetaClassInfo.name()"""
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

    def __init__():
        """None QMetaType.__init__()"""
        return None
    def __init__():
        """QMetaType QMetaType.__init__()"""
        return QMetaType()
    def isRegistered(_type):
        """bool QMetaType.isRegistered(int _type)"""
        return bool()
    def typeName(_type):
        """str QMetaType.typeName(int _type)"""
        return str()
    def type(_typeName):
        """int QMetaType.type(str _typeName)"""
        return int()


class QMimeData(QObject):
    """"""
    def __init__():
        """None QMimeData.__init__()"""
        return None
    def retrieveData(_mimetype, _preferredType):
        """QVariant QMimeData.retrieveData(QString _mimetype, Type _preferredType)"""
        return QVariant()
    def removeFormat(_mimetype):
        """None QMimeData.removeFormat(QString _mimetype)"""
        return None
    def clear():
        """None QMimeData.clear()"""
        return None
    def formats():
        """QStringList QMimeData.formats()"""
        return QStringList()
    def hasFormat(_mimetype):
        """bool QMimeData.hasFormat(QString _mimetype)"""
        return bool()
    def setData(_mimetype, _data):
        """None QMimeData.setData(QString _mimetype, QByteArray _data)"""
        return None
    def data(_mimetype):
        """QByteArray QMimeData.data(QString _mimetype)"""
        return QByteArray()
    def hasColor():
        """bool QMimeData.hasColor()"""
        return bool()
    def setColorData(_color):
        """None QMimeData.setColorData(QVariant _color)"""
        return None
    def colorData():
        """QVariant QMimeData.colorData()"""
        return QVariant()
    def hasImage():
        """bool QMimeData.hasImage()"""
        return bool()
    def setImageData(_image):
        """None QMimeData.setImageData(QVariant _image)"""
        return None
    def imageData():
        """QVariant QMimeData.imageData()"""
        return QVariant()
    def hasHtml():
        """bool QMimeData.hasHtml()"""
        return bool()
    def setHtml(_html):
        """None QMimeData.setHtml(QString _html)"""
        return None
    def html():
        """QString QMimeData.html()"""
        return QString()
    def hasText():
        """bool QMimeData.hasText()"""
        return bool()
    def setText(_text):
        """None QMimeData.setText(QString _text)"""
        return None
    def text():
        """QString QMimeData.text()"""
        return QString()
    def hasUrls():
        """bool QMimeData.hasUrls()"""
        return bool()
    def setUrls(_urls):
        """None QMimeData.setUrls(list-of-QUrl _urls)"""
        return None
    def urls():
        """list-of-QUrl QMimeData.urls()"""
        return [QUrl()]


class QMutex():
    """"""
    NonRecursive = int() # QMutex.RecursionMode enum
    Recursive = int() # QMutex.RecursionMode enum

    def __init__(_mode):
        """None QMutex.__init__(QMutex.RecursionMode _mode)"""
        return None
    def unlock():
        """None QMutex.unlock()"""
        return None
    def tryLock():
        """bool QMutex.tryLock()"""
        return bool()
    def tryLock(_timeout):
        """bool QMutex.tryLock(int _timeout)"""
        return bool()
    def lock():
        """None QMutex.lock()"""
        return None


class QMutexLocker():
    """"""
    def __init__(_m):
        """None QMutexLocker.__init__(QMutex _m)"""
        return None
    def __exit__(_type, _value, _traceback):
        """None QMutexLocker.__exit__(object _type, object _value, object _traceback)"""
        return None
    def __enter__():
        """object QMutexLocker.__enter__()"""
        return object()
    def mutex():
        """QMutex QMutexLocker.mutex()"""
        return QMutex()
    def relock():
        """None QMutexLocker.relock()"""
        return None
    def unlock():
        """None QMutexLocker.unlock()"""
        return None


class QObjectCleanupHandler(QObject):
    """"""
    def __init__():
        """None QObjectCleanupHandler.__init__()"""
        return None
    def clear():
        """None QObjectCleanupHandler.clear()"""
        return None
    def isEmpty():
        """bool QObjectCleanupHandler.isEmpty()"""
        return bool()
    def remove(_object):
        """None QObjectCleanupHandler.remove(QObject _object)"""
        return None
    def add(_object):
        """QObject QObjectCleanupHandler.add(QObject _object)"""
        return QObject()


class QMetaObject():
    """"""
    def __init__():
        """None QMetaObject.__init__()"""
        return None
    def __init__():
        """QMetaObject QMetaObject.__init__()"""
        return QMetaObject()
    def newInstance(_value0, _value1, _value2, _value3, _value4, _value5, _value6, _value7, _value8, _value9):
        """QObject QMetaObject.newInstance(QGenericArgument _value0, QGenericArgument _value1, QGenericArgument _value2, QGenericArgument _value3, QGenericArgument _value4, QGenericArgument _value5, QGenericArgument _value6, QGenericArgument _value7, QGenericArgument _value8, QGenericArgument _value9)"""
        return QObject()
    def constructor(_index):
        """QMetaMethod QMetaObject.constructor(int _index)"""
        return QMetaMethod()
    def indexOfConstructor(_constructor):
        """int QMetaObject.indexOfConstructor(str _constructor)"""
        return int()
    def constructorCount():
        """int QMetaObject.constructorCount()"""
        return int()
    def invokeMethod(_obj, _member, _type, _ret, _value0, _value1, _value2, _value3, _value4, _value5, _value6, _value7, _value8, _value9):
        """object QMetaObject.invokeMethod(QObject _obj, str _member, Qt.ConnectionType _type, QGenericReturnArgument _ret, QGenericArgument _value0, QGenericArgument _value1, QGenericArgument _value2, QGenericArgument _value3, QGenericArgument _value4, QGenericArgument _value5, QGenericArgument _value6, QGenericArgument _value7, QGenericArgument _value8, QGenericArgument _value9)"""
        return object()
    def invokeMethod(_obj, _member, _ret, _value0, _value1, _value2, _value3, _value4, _value5, _value6, _value7, _value8, _value9):
        """object QMetaObject.invokeMethod(QObject _obj, str _member, QGenericReturnArgument _ret, QGenericArgument _value0, QGenericArgument _value1, QGenericArgument _value2, QGenericArgument _value3, QGenericArgument _value4, QGenericArgument _value5, QGenericArgument _value6, QGenericArgument _value7, QGenericArgument _value8, QGenericArgument _value9)"""
        return object()
    def invokeMethod(_obj, _member, _type, _value0, _value1, _value2, _value3, _value4, _value5, _value6, _value7, _value8, _value9):
        """object QMetaObject.invokeMethod(QObject _obj, str _member, Qt.ConnectionType _type, QGenericArgument _value0, QGenericArgument _value1, QGenericArgument _value2, QGenericArgument _value3, QGenericArgument _value4, QGenericArgument _value5, QGenericArgument _value6, QGenericArgument _value7, QGenericArgument _value8, QGenericArgument _value9)"""
        return object()
    def invokeMethod(_obj, _member, _value0, _value1, _value2, _value3, _value4, _value5, _value6, _value7, _value8, _value9):
        """object QMetaObject.invokeMethod(QObject _obj, str _member, QGenericArgument _value0, QGenericArgument _value1, QGenericArgument _value2, QGenericArgument _value3, QGenericArgument _value4, QGenericArgument _value5, QGenericArgument _value6, QGenericArgument _value7, QGenericArgument _value8, QGenericArgument _value9)"""
        return object()
    def normalizedType(_type):
        """QByteArray QMetaObject.normalizedType(str _type)"""
        return QByteArray()
    def normalizedSignature(_method):
        """QByteArray QMetaObject.normalizedSignature(str _method)"""
        return QByteArray()
    def connectSlotsByName(_o):
        """None QMetaObject.connectSlotsByName(QObject _o)"""
        return None
    def checkConnectArgs(_signal, _method):
        """bool QMetaObject.checkConnectArgs(str _signal, str _method)"""
        return bool()
    def classInfo(_index):
        """QMetaClassInfo QMetaObject.classInfo(int _index)"""
        return QMetaClassInfo()
    def property(_index):
        """QMetaProperty QMetaObject.property(int _index)"""
        return QMetaProperty()
    def enumerator(_index):
        """QMetaEnum QMetaObject.enumerator(int _index)"""
        return QMetaEnum()
    def method(_index):
        """QMetaMethod QMetaObject.method(int _index)"""
        return QMetaMethod()
    def indexOfClassInfo(_name):
        """int QMetaObject.indexOfClassInfo(str _name)"""
        return int()
    def indexOfProperty(_name):
        """int QMetaObject.indexOfProperty(str _name)"""
        return int()
    def indexOfEnumerator(_name):
        """int QMetaObject.indexOfEnumerator(str _name)"""
        return int()
    def indexOfSlot(_slot):
        """int QMetaObject.indexOfSlot(str _slot)"""
        return int()
    def indexOfSignal(_signal):
        """int QMetaObject.indexOfSignal(str _signal)"""
        return int()
    def indexOfMethod(_method):
        """int QMetaObject.indexOfMethod(str _method)"""
        return int()
    def classInfoCount():
        """int QMetaObject.classInfoCount()"""
        return int()
    def propertyCount():
        """int QMetaObject.propertyCount()"""
        return int()
    def enumeratorCount():
        """int QMetaObject.enumeratorCount()"""
        return int()
    def methodCount():
        """int QMetaObject.methodCount()"""
        return int()
    def classInfoOffset():
        """int QMetaObject.classInfoOffset()"""
        return int()
    def propertyOffset():
        """int QMetaObject.propertyOffset()"""
        return int()
    def enumeratorOffset():
        """int QMetaObject.enumeratorOffset()"""
        return int()
    def methodOffset():
        """int QMetaObject.methodOffset()"""
        return int()
    def userProperty():
        """QMetaProperty QMetaObject.userProperty()"""
        return QMetaProperty()
    def superClass():
        """QMetaObject QMetaObject.superClass()"""
        return QMetaObject()
    def className():
        """str QMetaObject.className()"""
        return str()


class QGenericArgument():
    """"""


class QGenericReturnArgument():
    """"""


class QParallelAnimationGroup(QAnimationGroup):
    """"""
    def __init__(_parent):
        """None QParallelAnimationGroup.__init__(QObject _parent)"""
        return None
    def updateDirection(_direction):
        """None QParallelAnimationGroup.updateDirection(QAbstractAnimation.Direction _direction)"""
        return None
    def updateState(_newState, _oldState):
        """None QParallelAnimationGroup.updateState(QAbstractAnimation.State _newState, QAbstractAnimation.State _oldState)"""
        return None
    def updateCurrentTime(_currentTime):
        """None QParallelAnimationGroup.updateCurrentTime(int _currentTime)"""
        return None
    def event(_event):
        """bool QParallelAnimationGroup.event(QEvent _event)"""
        return bool()
    def duration():
        """int QParallelAnimationGroup.duration()"""
        return int()


class QPauseAnimation(QAbstractAnimation):
    """"""
    def __init__(_parent):
        """None QPauseAnimation.__init__(QObject _parent)"""
        return None
    def __init__(_msecs, _parent):
        """None QPauseAnimation.__init__(int _msecs, QObject _parent)"""
        return None
    def updateCurrentTime():
        """int QPauseAnimation.updateCurrentTime()"""
        return int()
    def event(_e):
        """bool QPauseAnimation.event(QEvent _e)"""
        return bool()
    def setDuration(_msecs):
        """None QPauseAnimation.setDuration(int _msecs)"""
        return None
    def duration():
        """int QPauseAnimation.duration()"""
        return int()


class QVariantAnimation(QAbstractAnimation):
    """"""
    def __init__(_parent):
        """None QVariantAnimation.__init__(QObject _parent)"""
        return None
    def interpolated(_from, _to, _progress):
        """QVariant QVariantAnimation.interpolated(QVariant _from, QVariant _to, float _progress)"""
        return QVariant()
    def updateCurrentValue(_value):
        """abstract None QVariantAnimation.updateCurrentValue(QVariant _value)"""
        return None
    def updateState(_newState, _oldState):
        """None QVariantAnimation.updateState(QAbstractAnimation.State _newState, QAbstractAnimation.State _oldState)"""
        return None
    def updateCurrentTime():
        """int QVariantAnimation.updateCurrentTime()"""
        return int()
    def event(_event):
        """bool QVariantAnimation.event(QEvent _event)"""
        return bool()
    def setEasingCurve(_easing):
        """None QVariantAnimation.setEasingCurve(QEasingCurve _easing)"""
        return None
    def easingCurve():
        """QEasingCurve QVariantAnimation.easingCurve()"""
        return QEasingCurve()
    def setDuration(_msecs):
        """None QVariantAnimation.setDuration(int _msecs)"""
        return None
    def duration():
        """int QVariantAnimation.duration()"""
        return int()
    def currentValue():
        """QVariant QVariantAnimation.currentValue()"""
        return QVariant()
    def setKeyValues(_values):
        """None QVariantAnimation.setKeyValues(list-of-tuple-of-float-QVariant _values)"""
        return None
    def keyValues():
        """list-of-tuple-of-float-QVariant QVariantAnimation.keyValues()"""
        return [tuple-of-float-QVariant()]
    def setKeyValueAt(_step, _value):
        """None QVariantAnimation.setKeyValueAt(float _step, QVariant _value)"""
        return None
    def keyValueAt(_step):
        """QVariant QVariantAnimation.keyValueAt(float _step)"""
        return QVariant()
    def setEndValue(_value):
        """None QVariantAnimation.setEndValue(QVariant _value)"""
        return None
    def endValue():
        """QVariant QVariantAnimation.endValue()"""
        return QVariant()
    def setStartValue(_value):
        """None QVariantAnimation.setStartValue(QVariant _value)"""
        return None
    def startValue():
        """QVariant QVariantAnimation.startValue()"""
        return QVariant()


class QPropertyAnimation(QVariantAnimation):
    """"""
    def __init__(_parent):
        """None QPropertyAnimation.__init__(QObject _parent)"""
        return None
    def __init__(_target, _propertyName, _parent):
        """None QPropertyAnimation.__init__(QObject _target, QByteArray _propertyName, QObject _parent)"""
        return None
    def updateState(_newState, _oldState):
        """None QPropertyAnimation.updateState(QAbstractAnimation.State _newState, QAbstractAnimation.State _oldState)"""
        return None
    def updateCurrentValue(_value):
        """None QPropertyAnimation.updateCurrentValue(QVariant _value)"""
        return None
    def event(_event):
        """bool QPropertyAnimation.event(QEvent _event)"""
        return bool()
    def setPropertyName(_propertyName):
        """None QPropertyAnimation.setPropertyName(QByteArray _propertyName)"""
        return None
    def propertyName():
        """QByteArray QPropertyAnimation.propertyName()"""
        return QByteArray()
    def setTargetObject(_target):
        """None QPropertyAnimation.setTargetObject(QObject _target)"""
        return None
    def targetObject():
        """QObject QPropertyAnimation.targetObject()"""
        return QObject()


class QPluginLoader(QObject):
    """"""
    def __init__(_parent):
        """None QPluginLoader.__init__(QObject _parent)"""
        return None
    def __init__(_fileName, _parent):
        """None QPluginLoader.__init__(QString _fileName, QObject _parent)"""
        return None
    def loadHints():
        """QLibrary.LoadHints QPluginLoader.loadHints()"""
        return QLibrary.LoadHints()
    def setLoadHints(_loadHints):
        """None QPluginLoader.setLoadHints(QLibrary.LoadHints _loadHints)"""
        return None
    def errorString():
        """QString QPluginLoader.errorString()"""
        return QString()
    def fileName():
        """QString QPluginLoader.fileName()"""
        return QString()
    def setFileName(_fileName):
        """None QPluginLoader.setFileName(QString _fileName)"""
        return None
    def isLoaded():
        """bool QPluginLoader.isLoaded()"""
        return bool()
    def unload():
        """bool QPluginLoader.unload()"""
        return bool()
    def load():
        """bool QPluginLoader.load()"""
        return bool()
    def staticInstances():
        """list-of-QObject QPluginLoader.staticInstances()"""
        return [QObject()]
    def instance():
        """QObject QPluginLoader.instance()"""
        return QObject()


class QPoint():
    """"""
    def __init__():
        """None QPoint.__init__()"""
        return None
    def __init__(_xpos, _ypos):
        """None QPoint.__init__(int _xpos, int _ypos)"""
        return None
    def __init__():
        """QPoint QPoint.__init__()"""
        return QPoint()
    def __eq__(_p2):
        """bool QPoint.__eq__(QPoint _p2)"""
        return bool()
    def __ne__(_p2):
        """bool QPoint.__ne__(QPoint _p2)"""
        return bool()
    def __add__(_p2):
        """QPoint QPoint.__add__(QPoint _p2)"""
        return QPoint()
    def __sub__(_p2):
        """QPoint QPoint.__sub__(QPoint _p2)"""
        return QPoint()
    def __mul__(_c):
        """QPoint QPoint.__mul__(float _c)"""
        return QPoint()
    def __neg__():
        """QPoint QPoint.__neg__()"""
        return QPoint()
    def __div__(_c):
        """QPoint QPoint.__div__(float _c)"""
        return QPoint()
    def __idiv__(_c):
        """QPoint QPoint.__idiv__(float _c)"""
        return QPoint()
    def __imul__(_c):
        """QPoint QPoint.__imul__(float _c)"""
        return QPoint()
    def __isub__(_p):
        """QPoint QPoint.__isub__(QPoint _p)"""
        return QPoint()
    def __iadd__(_p):
        """QPoint QPoint.__iadd__(QPoint _p)"""
        return QPoint()
    def setY(_ypos):
        """None QPoint.setY(int _ypos)"""
        return None
    def setX(_xpos):
        """None QPoint.setX(int _xpos)"""
        return None
    def y():
        """int QPoint.y()"""
        return int()
    def x():
        """int QPoint.x()"""
        return int()
    def __bool__():
        """int QPoint.__bool__()"""
        return int()
    def isNull():
        """bool QPoint.isNull()"""
        return bool()
    def __repr__():
        """str QPoint.__repr__()"""
        return str()
    def manhattanLength():
        """int QPoint.manhattanLength()"""
        return int()


class QPointF():
    """"""
    def __init__():
        """None QPointF.__init__()"""
        return None
    def __init__(_xpos, _ypos):
        """None QPointF.__init__(float _xpos, float _ypos)"""
        return None
    def __init__(_p):
        """None QPointF.__init__(QPoint _p)"""
        return None
    def __init__():
        """QPointF QPointF.__init__()"""
        return QPointF()
    def __eq__(_p2):
        """bool QPointF.__eq__(QPointF _p2)"""
        return bool()
    def __ne__(_p2):
        """bool QPointF.__ne__(QPointF _p2)"""
        return bool()
    def __add__(_p2):
        """QPointF QPointF.__add__(QPointF _p2)"""
        return QPointF()
    def __sub__(_p2):
        """QPointF QPointF.__sub__(QPointF _p2)"""
        return QPointF()
    def __mul__(_c):
        """QPointF QPointF.__mul__(float _c)"""
        return QPointF()
    def __neg__():
        """QPointF QPointF.__neg__()"""
        return QPointF()
    def __div__(_c):
        """QPointF QPointF.__div__(float _c)"""
        return QPointF()
    def manhattanLength():
        """float QPointF.manhattanLength()"""
        return float()
    def toPoint():
        """QPoint QPointF.toPoint()"""
        return QPoint()
    def __idiv__(_c):
        """QPointF QPointF.__idiv__(float _c)"""
        return QPointF()
    def __imul__(_c):
        """QPointF QPointF.__imul__(float _c)"""
        return QPointF()
    def __isub__(_p):
        """QPointF QPointF.__isub__(QPointF _p)"""
        return QPointF()
    def __iadd__(_p):
        """QPointF QPointF.__iadd__(QPointF _p)"""
        return QPointF()
    def setY(_ypos):
        """None QPointF.setY(float _ypos)"""
        return None
    def setX(_xpos):
        """None QPointF.setX(float _xpos)"""
        return None
    def y():
        """float QPointF.y()"""
        return float()
    def x():
        """float QPointF.x()"""
        return float()
    def __bool__():
        """int QPointF.__bool__()"""
        return int()
    def isNull():
        """bool QPointF.isNull()"""
        return bool()
    def __repr__():
        """str QPointF.__repr__()"""
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

    def __init__(_parent):
        """None QProcess.__init__(QObject _parent)"""
        return None
    def processEnvironment():
        """QProcessEnvironment QProcess.processEnvironment()"""
        return QProcessEnvironment()
    def setProcessEnvironment(_environment):
        """None QProcess.setProcessEnvironment(QProcessEnvironment _environment)"""
        return None
    def writeData(_data):
        """int QProcess.writeData(str _data)"""
        return int()
    def readData(_maxlen):
        """str QProcess.readData(int _maxlen)"""
        return str()
    def setupChildProcess():
        """None QProcess.setupChildProcess()"""
        return None
    def setProcessState(_state):
        """None QProcess.setProcessState(QProcess.ProcessState _state)"""
        return None
    def kill():
        """None QProcess.kill()"""
        return None
    def terminate():
        """None QProcess.terminate()"""
        return None
    def setStandardOutputProcess(_destination):
        """None QProcess.setStandardOutputProcess(QProcess _destination)"""
        return None
    def setStandardErrorFile(_fileName, _mode):
        """None QProcess.setStandardErrorFile(QString _fileName, QIODevice.OpenMode _mode)"""
        return None
    def setStandardOutputFile(_fileName, _mode):
        """None QProcess.setStandardOutputFile(QString _fileName, QIODevice.OpenMode _mode)"""
        return None
    def setStandardInputFile(_fileName):
        """None QProcess.setStandardInputFile(QString _fileName)"""
        return None
    def setProcessChannelMode(_mode):
        """None QProcess.setProcessChannelMode(QProcess.ProcessChannelMode _mode)"""
        return None
    def processChannelMode():
        """QProcess.ProcessChannelMode QProcess.processChannelMode()"""
        return QProcess.ProcessChannelMode()
    def systemEnvironment():
        """QStringList QProcess.systemEnvironment()"""
        return QStringList()
    def startDetached(_program, _arguments, _workingDirectory, _pid):
        """bool QProcess.startDetached(QString _program, QStringList _arguments, QString _workingDirectory, int _pid)"""
        return bool()
    def startDetached(_program, _arguments):
        """bool QProcess.startDetached(QString _program, QStringList _arguments)"""
        return bool()
    def startDetached(_program):
        """bool QProcess.startDetached(QString _program)"""
        return bool()
    def execute(_program, _arguments):
        """int QProcess.execute(QString _program, QStringList _arguments)"""
        return int()
    def execute(_program):
        """int QProcess.execute(QString _program)"""
        return int()
    def atEnd():
        """bool QProcess.atEnd()"""
        return bool()
    def close():
        """None QProcess.close()"""
        return None
    def canReadLine():
        """bool QProcess.canReadLine()"""
        return bool()
    def isSequential():
        """bool QProcess.isSequential()"""
        return bool()
    def bytesToWrite():
        """int QProcess.bytesToWrite()"""
        return int()
    def bytesAvailable():
        """int QProcess.bytesAvailable()"""
        return int()
    def exitStatus():
        """QProcess.ExitStatus QProcess.exitStatus()"""
        return QProcess.ExitStatus()
    def exitCode():
        """int QProcess.exitCode()"""
        return int()
    def readAllStandardError():
        """QByteArray QProcess.readAllStandardError()"""
        return QByteArray()
    def readAllStandardOutput():
        """QByteArray QProcess.readAllStandardOutput()"""
        return QByteArray()
    def waitForFinished(_msecs):
        """bool QProcess.waitForFinished(int _msecs)"""
        return bool()
    def waitForBytesWritten(_msecs):
        """bool QProcess.waitForBytesWritten(int _msecs)"""
        return bool()
    def waitForReadyRead(_msecs):
        """bool QProcess.waitForReadyRead(int _msecs)"""
        return bool()
    def waitForStarted(_msecs):
        """bool QProcess.waitForStarted(int _msecs)"""
        return bool()
    def pid():
        """int QProcess.pid()"""
        return int()
    def state():
        """QProcess.ProcessState QProcess.state()"""
        return QProcess.ProcessState()
    def error():
        """QProcess.ProcessError QProcess.error()"""
        return QProcess.ProcessError()
    def environment():
        """QStringList QProcess.environment()"""
        return QStringList()
    def setEnvironment(_environment):
        """None QProcess.setEnvironment(QStringList _environment)"""
        return None
    def setWorkingDirectory(_dir):
        """None QProcess.setWorkingDirectory(QString _dir)"""
        return None
    def workingDirectory():
        """QString QProcess.workingDirectory()"""
        return QString()
    def closeWriteChannel():
        """None QProcess.closeWriteChannel()"""
        return None
    def closeReadChannel(_channel):
        """None QProcess.closeReadChannel(QProcess.ProcessChannel _channel)"""
        return None
    def setReadChannel(_channel):
        """None QProcess.setReadChannel(QProcess.ProcessChannel _channel)"""
        return None
    def readChannel():
        """QProcess.ProcessChannel QProcess.readChannel()"""
        return QProcess.ProcessChannel()
    def setReadChannelMode(_mode):
        """None QProcess.setReadChannelMode(QProcess.ProcessChannelMode _mode)"""
        return None
    def readChannelMode():
        """QProcess.ProcessChannelMode QProcess.readChannelMode()"""
        return QProcess.ProcessChannelMode()
    def start(_program, _arguments, _mode):
        """None QProcess.start(QString _program, QStringList _arguments, QIODevice.OpenMode _mode)"""
        return None
    def start(_program, _mode):
        """None QProcess.start(QString _program, QIODevice.OpenMode _mode)"""
        return None


class QProcessEnvironment():
    """"""
    def __init__():
        """None QProcessEnvironment.__init__()"""
        return None
    def __init__(_other):
        """None QProcessEnvironment.__init__(QProcessEnvironment _other)"""
        return None
    def systemEnvironment():
        """QProcessEnvironment QProcessEnvironment.systemEnvironment()"""
        return QProcessEnvironment()
    def toStringList():
        """QStringList QProcessEnvironment.toStringList()"""
        return QStringList()
    def value(_name, _defaultValue):
        """QString QProcessEnvironment.value(QString _name, QString _defaultValue)"""
        return QString()
    def remove(_name):
        """None QProcessEnvironment.remove(QString _name)"""
        return None
    def insert(_name, _value):
        """None QProcessEnvironment.insert(QString _name, QString _value)"""
        return None
    def contains(_name):
        """bool QProcessEnvironment.contains(QString _name)"""
        return bool()
    def clear():
        """None QProcessEnvironment.clear()"""
        return None
    def isEmpty():
        """bool QProcessEnvironment.isEmpty()"""
        return bool()
    def __ne__(_other):
        """bool QProcessEnvironment.__ne__(QProcessEnvironment _other)"""
        return bool()
    def __eq__(_other):
        """bool QProcessEnvironment.__eq__(QProcessEnvironment _other)"""
        return bool()


class QReadWriteLock():
    """"""
    NonRecursive = int() # QReadWriteLock.RecursionMode enum
    Recursive = int() # QReadWriteLock.RecursionMode enum

    def __init__():
        """None QReadWriteLock.__init__()"""
        return None
    def __init__(_recursionMode):
        """None QReadWriteLock.__init__(QReadWriteLock.RecursionMode _recursionMode)"""
        return None
    def unlock():
        """None QReadWriteLock.unlock()"""
        return None
    def tryLockForWrite():
        """bool QReadWriteLock.tryLockForWrite()"""
        return bool()
    def tryLockForWrite(_timeout):
        """bool QReadWriteLock.tryLockForWrite(int _timeout)"""
        return bool()
    def lockForWrite():
        """None QReadWriteLock.lockForWrite()"""
        return None
    def tryLockForRead():
        """bool QReadWriteLock.tryLockForRead()"""
        return bool()
    def tryLockForRead(_timeout):
        """bool QReadWriteLock.tryLockForRead(int _timeout)"""
        return bool()
    def lockForRead():
        """None QReadWriteLock.lockForRead()"""
        return None


class QReadLocker():
    """"""
    def __init__(_areadWriteLock):
        """None QReadLocker.__init__(QReadWriteLock _areadWriteLock)"""
        return None
    def __exit__(_type, _value, _traceback):
        """None QReadLocker.__exit__(object _type, object _value, object _traceback)"""
        return None
    def __enter__():
        """object QReadLocker.__enter__()"""
        return object()
    def readWriteLock():
        """QReadWriteLock QReadLocker.readWriteLock()"""
        return QReadWriteLock()
    def relock():
        """None QReadLocker.relock()"""
        return None
    def unlock():
        """None QReadLocker.unlock()"""
        return None


class QWriteLocker():
    """"""
    def __init__(_areadWriteLock):
        """None QWriteLocker.__init__(QReadWriteLock _areadWriteLock)"""
        return None
    def __exit__(_type, _value, _traceback):
        """None QWriteLocker.__exit__(object _type, object _value, object _traceback)"""
        return None
    def __enter__():
        """object QWriteLocker.__enter__()"""
        return object()
    def readWriteLock():
        """QReadWriteLock QWriteLocker.readWriteLock()"""
        return QReadWriteLock()
    def relock():
        """None QWriteLocker.relock()"""
        return None
    def unlock():
        """None QWriteLocker.unlock()"""
        return None


class QRect():
    """"""
    def __init__():
        """None QRect.__init__()"""
        return None
    def __init__(_aleft, _atop, _awidth, _aheight):
        """None QRect.__init__(int _aleft, int _atop, int _awidth, int _aheight)"""
        return None
    def __init__(_atopLeft, _abottomRight):
        """None QRect.__init__(QPoint _atopLeft, QPoint _abottomRight)"""
        return None
    def __init__(_atopLeft, _asize):
        """None QRect.__init__(QPoint _atopLeft, QSize _asize)"""
        return None
    def __init__():
        """QRect QRect.__init__()"""
        return QRect()
    def __eq__(_r2):
        """bool QRect.__eq__(QRect _r2)"""
        return bool()
    def __ne__(_r2):
        """bool QRect.__ne__(QRect _r2)"""
        return bool()
    def united(_r):
        """QRect QRect.united(QRect _r)"""
        return QRect()
    def intersected(_other):
        """QRect QRect.intersected(QRect _other)"""
        return QRect()
    def unite(_r):
        """QRect QRect.unite(QRect _r)"""
        return QRect()
    def intersect(_r):
        """QRect QRect.intersect(QRect _r)"""
        return QRect()
    def __iand__(_r):
        """QRect QRect.__iand__(QRect _r)"""
        return QRect()
    def __ior__(_r):
        """QRect QRect.__ior__(QRect _r)"""
        return QRect()
    def setSize(_s):
        """None QRect.setSize(QSize _s)"""
        return None
    def setHeight(_h):
        """None QRect.setHeight(int _h)"""
        return None
    def setWidth(_w):
        """None QRect.setWidth(int _w)"""
        return None
    def adjust(_dx1, _dy1, _dx2, _dy2):
        """None QRect.adjust(int _dx1, int _dy1, int _dx2, int _dy2)"""
        return None
    def adjusted(_xp1, _yp1, _xp2, _yp2):
        """QRect QRect.adjusted(int _xp1, int _yp1, int _xp2, int _yp2)"""
        return QRect()
    def setCoords(_xp1, _yp1, _xp2, _yp2):
        """None QRect.setCoords(int _xp1, int _yp1, int _xp2, int _yp2)"""
        return None
    def getCoords(_xp1, _yp1, _xp2, _yp2):
        """None QRect.getCoords(int _xp1, int _yp1, int _xp2, int _yp2)"""
        return None
    def setRect(_ax, _ay, _aw, _ah):
        """None QRect.setRect(int _ax, int _ay, int _aw, int _ah)"""
        return None
    def getRect(_ax, _ay, _aw, _ah):
        """None QRect.getRect(int _ax, int _ay, int _aw, int _ah)"""
        return None
    def moveBottomLeft(_p):
        """None QRect.moveBottomLeft(QPoint _p)"""
        return None
    def moveTopRight(_p):
        """None QRect.moveTopRight(QPoint _p)"""
        return None
    def moveBottomRight(_p):
        """None QRect.moveBottomRight(QPoint _p)"""
        return None
    def moveTopLeft(_p):
        """None QRect.moveTopLeft(QPoint _p)"""
        return None
    def moveBottom(_pos):
        """None QRect.moveBottom(int _pos)"""
        return None
    def moveRight(_pos):
        """None QRect.moveRight(int _pos)"""
        return None
    def moveTop(_pos):
        """None QRect.moveTop(int _pos)"""
        return None
    def moveLeft(_pos):
        """None QRect.moveLeft(int _pos)"""
        return None
    def moveTo(_ax, _ay):
        """None QRect.moveTo(int _ax, int _ay)"""
        return None
    def moveTo(_p):
        """None QRect.moveTo(QPoint _p)"""
        return None
    def translated(_dx, _dy):
        """QRect QRect.translated(int _dx, int _dy)"""
        return QRect()
    def translated(_p):
        """QRect QRect.translated(QPoint _p)"""
        return QRect()
    def translate(_dx, _dy):
        """None QRect.translate(int _dx, int _dy)"""
        return None
    def translate(_p):
        """None QRect.translate(QPoint _p)"""
        return None
    def size():
        """QSize QRect.size()"""
        return QSize()
    def height():
        """int QRect.height()"""
        return int()
    def width():
        """int QRect.width()"""
        return int()
    def center():
        """QPoint QRect.center()"""
        return QPoint()
    def bottomLeft():
        """QPoint QRect.bottomLeft()"""
        return QPoint()
    def topRight():
        """QPoint QRect.topRight()"""
        return QPoint()
    def bottomRight():
        """QPoint QRect.bottomRight()"""
        return QPoint()
    def topLeft():
        """QPoint QRect.topLeft()"""
        return QPoint()
    def setY(_ay):
        """None QRect.setY(int _ay)"""
        return None
    def setX(_ax):
        """None QRect.setX(int _ax)"""
        return None
    def setBottomLeft(_p):
        """None QRect.setBottomLeft(QPoint _p)"""
        return None
    def setTopRight(_p):
        """None QRect.setTopRight(QPoint _p)"""
        return None
    def setBottomRight(_p):
        """None QRect.setBottomRight(QPoint _p)"""
        return None
    def setTopLeft(_p):
        """None QRect.setTopLeft(QPoint _p)"""
        return None
    def setBottom(_pos):
        """None QRect.setBottom(int _pos)"""
        return None
    def setRight(_pos):
        """None QRect.setRight(int _pos)"""
        return None
    def setTop(_pos):
        """None QRect.setTop(int _pos)"""
        return None
    def setLeft(_pos):
        """None QRect.setLeft(int _pos)"""
        return None
    def y():
        """int QRect.y()"""
        return int()
    def x():
        """int QRect.x()"""
        return int()
    def bottom():
        """int QRect.bottom()"""
        return int()
    def right():
        """int QRect.right()"""
        return int()
    def top():
        """int QRect.top()"""
        return int()
    def left():
        """int QRect.left()"""
        return int()
    def __bool__():
        """int QRect.__bool__()"""
        return int()
    def isValid():
        """bool QRect.isValid()"""
        return bool()
    def isEmpty():
        """bool QRect.isEmpty()"""
        return bool()
    def isNull():
        """bool QRect.isNull()"""
        return bool()
    def __repr__():
        """str QRect.__repr__()"""
        return str()
    def intersects(_r):
        """bool QRect.intersects(QRect _r)"""
        return bool()
    def __contains__(_p):
        """int QRect.__contains__(QPoint _p)"""
        return int()
    def __contains__(_r):
        """int QRect.__contains__(QRect _r)"""
        return int()
    def contains(_point, _proper):
        """bool QRect.contains(QPoint _point, bool _proper)"""
        return bool()
    def contains(_rectangle, _proper):
        """bool QRect.contains(QRect _rectangle, bool _proper)"""
        return bool()
    def contains(_ax, _ay, _aproper):
        """bool QRect.contains(int _ax, int _ay, bool _aproper)"""
        return bool()
    def contains(_ax, _ay):
        """bool QRect.contains(int _ax, int _ay)"""
        return bool()
    def __and__(_r):
        """QRect QRect.__and__(QRect _r)"""
        return QRect()
    def __or__(_r):
        """QRect QRect.__or__(QRect _r)"""
        return QRect()
    def moveCenter(_p):
        """None QRect.moveCenter(QPoint _p)"""
        return None
    def normalized():
        """QRect QRect.normalized()"""
        return QRect()


class QRectF():
    """"""
    def __init__():
        """None QRectF.__init__()"""
        return None
    def __init__(_atopLeft, _asize):
        """None QRectF.__init__(QPointF _atopLeft, QSizeF _asize)"""
        return None
    def __init__(_atopLeft, _abottomRight):
        """None QRectF.__init__(QPointF _atopLeft, QPointF _abottomRight)"""
        return None
    def __init__(_aleft, _atop, _awidth, _aheight):
        """None QRectF.__init__(float _aleft, float _atop, float _awidth, float _aheight)"""
        return None
    def __init__(_r):
        """None QRectF.__init__(QRect _r)"""
        return None
    def __init__():
        """QRectF QRectF.__init__()"""
        return QRectF()
    def __eq__(_r2):
        """bool QRectF.__eq__(QRectF _r2)"""
        return bool()
    def __ne__(_r2):
        """bool QRectF.__ne__(QRectF _r2)"""
        return bool()
    def united(_r):
        """QRectF QRectF.united(QRectF _r)"""
        return QRectF()
    def intersected(_r):
        """QRectF QRectF.intersected(QRectF _r)"""
        return QRectF()
    def toRect():
        """QRect QRectF.toRect()"""
        return QRect()
    def toAlignedRect():
        """QRect QRectF.toAlignedRect()"""
        return QRect()
    def unite(_r):
        """QRectF QRectF.unite(QRectF _r)"""
        return QRectF()
    def intersect(_r):
        """QRectF QRectF.intersect(QRectF _r)"""
        return QRectF()
    def __iand__(_r):
        """QRectF QRectF.__iand__(QRectF _r)"""
        return QRectF()
    def __ior__(_r):
        """QRectF QRectF.__ior__(QRectF _r)"""
        return QRectF()
    def setSize(_s):
        """None QRectF.setSize(QSizeF _s)"""
        return None
    def setHeight(_ah):
        """None QRectF.setHeight(float _ah)"""
        return None
    def setWidth(_aw):
        """None QRectF.setWidth(float _aw)"""
        return None
    def adjusted(_xp1, _yp1, _xp2, _yp2):
        """QRectF QRectF.adjusted(float _xp1, float _yp1, float _xp2, float _yp2)"""
        return QRectF()
    def adjust(_xp1, _yp1, _xp2, _yp2):
        """None QRectF.adjust(float _xp1, float _yp1, float _xp2, float _yp2)"""
        return None
    def setCoords(_xp1, _yp1, _xp2, _yp2):
        """None QRectF.setCoords(float _xp1, float _yp1, float _xp2, float _yp2)"""
        return None
    def getCoords(_xp1, _yp1, _xp2, _yp2):
        """None QRectF.getCoords(float _xp1, float _yp1, float _xp2, float _yp2)"""
        return None
    def setRect(_ax, _ay, _aaw, _aah):
        """None QRectF.setRect(float _ax, float _ay, float _aaw, float _aah)"""
        return None
    def getRect(_ax, _ay, _aaw, _aah):
        """None QRectF.getRect(float _ax, float _ay, float _aaw, float _aah)"""
        return None
    def translated(_dx, _dy):
        """QRectF QRectF.translated(float _dx, float _dy)"""
        return QRectF()
    def translated(_p):
        """QRectF QRectF.translated(QPointF _p)"""
        return QRectF()
    def moveTo(_ax, _ay):
        """None QRectF.moveTo(float _ax, float _ay)"""
        return None
    def moveTo(_p):
        """None QRectF.moveTo(QPointF _p)"""
        return None
    def translate(_dx, _dy):
        """None QRectF.translate(float _dx, float _dy)"""
        return None
    def translate(_p):
        """None QRectF.translate(QPointF _p)"""
        return None
    def size():
        """QSizeF QRectF.size()"""
        return QSizeF()
    def height():
        """float QRectF.height()"""
        return float()
    def width():
        """float QRectF.width()"""
        return float()
    def moveCenter(_p):
        """None QRectF.moveCenter(QPointF _p)"""
        return None
    def moveBottomRight(_p):
        """None QRectF.moveBottomRight(QPointF _p)"""
        return None
    def moveBottomLeft(_p):
        """None QRectF.moveBottomLeft(QPointF _p)"""
        return None
    def moveTopRight(_p):
        """None QRectF.moveTopRight(QPointF _p)"""
        return None
    def moveTopLeft(_p):
        """None QRectF.moveTopLeft(QPointF _p)"""
        return None
    def moveBottom(_pos):
        """None QRectF.moveBottom(float _pos)"""
        return None
    def moveRight(_pos):
        """None QRectF.moveRight(float _pos)"""
        return None
    def moveTop(_pos):
        """None QRectF.moveTop(float _pos)"""
        return None
    def moveLeft(_pos):
        """None QRectF.moveLeft(float _pos)"""
        return None
    def center():
        """QPointF QRectF.center()"""
        return QPointF()
    def setBottomRight(_p):
        """None QRectF.setBottomRight(QPointF _p)"""
        return None
    def setBottomLeft(_p):
        """None QRectF.setBottomLeft(QPointF _p)"""
        return None
    def setTopRight(_p):
        """None QRectF.setTopRight(QPointF _p)"""
        return None
    def setTopLeft(_p):
        """None QRectF.setTopLeft(QPointF _p)"""
        return None
    def setBottom(_pos):
        """None QRectF.setBottom(float _pos)"""
        return None
    def setTop(_pos):
        """None QRectF.setTop(float _pos)"""
        return None
    def setRight(_pos):
        """None QRectF.setRight(float _pos)"""
        return None
    def setLeft(_pos):
        """None QRectF.setLeft(float _pos)"""
        return None
    def y():
        """float QRectF.y()"""
        return float()
    def x():
        """float QRectF.x()"""
        return float()
    def __bool__():
        """int QRectF.__bool__()"""
        return int()
    def isValid():
        """bool QRectF.isValid()"""
        return bool()
    def isEmpty():
        """bool QRectF.isEmpty()"""
        return bool()
    def isNull():
        """bool QRectF.isNull()"""
        return bool()
    def intersects(_r):
        """bool QRectF.intersects(QRectF _r)"""
        return bool()
    def __contains__(_p):
        """int QRectF.__contains__(QPointF _p)"""
        return int()
    def __contains__(_r):
        """int QRectF.__contains__(QRectF _r)"""
        return int()
    def contains(_p):
        """bool QRectF.contains(QPointF _p)"""
        return bool()
    def contains(_r):
        """bool QRectF.contains(QRectF _r)"""
        return bool()
    def contains(_ax, _ay):
        """bool QRectF.contains(float _ax, float _ay)"""
        return bool()
    def __and__(_r):
        """QRectF QRectF.__and__(QRectF _r)"""
        return QRectF()
    def __or__(_r):
        """QRectF QRectF.__or__(QRectF _r)"""
        return QRectF()
    def bottomLeft():
        """QPointF QRectF.bottomLeft()"""
        return QPointF()
    def topRight():
        """QPointF QRectF.topRight()"""
        return QPointF()
    def bottomRight():
        """QPointF QRectF.bottomRight()"""
        return QPointF()
    def topLeft():
        """QPointF QRectF.topLeft()"""
        return QPointF()
    def setY(_pos):
        """None QRectF.setY(float _pos)"""
        return None
    def setX(_pos):
        """None QRectF.setX(float _pos)"""
        return None
    def bottom():
        """float QRectF.bottom()"""
        return float()
    def right():
        """float QRectF.right()"""
        return float()
    def top():
        """float QRectF.top()"""
        return float()
    def left():
        """float QRectF.left()"""
        return float()
    def normalized():
        """QRectF QRectF.normalized()"""
        return QRectF()
    def __repr__():
        """str QRectF.__repr__()"""
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

    def __init__():
        """None QRegExp.__init__()"""
        return None
    def __init__(_pattern, _cs, _syntax):
        """None QRegExp.__init__(QString _pattern, Qt.CaseSensitivity _cs, QRegExp.PatternSyntax _syntax)"""
        return None
    def __init__(_rx):
        """None QRegExp.__init__(QRegExp _rx)"""
        return None
    def captureCount():
        """int QRegExp.captureCount()"""
        return int()
    def escape(_str):
        """QString QRegExp.escape(QString _str)"""
        return QString()
    def errorString():
        """QString QRegExp.errorString()"""
        return QString()
    def pos(_nth):
        """int QRegExp.pos(int _nth)"""
        return int()
    def cap(_nth):
        """QString QRegExp.cap(int _nth)"""
        return QString()
    def capturedTexts():
        """QStringList QRegExp.capturedTexts()"""
        return QStringList()
    def numCaptures():
        """int QRegExp.numCaptures()"""
        return int()
    def matchedLength():
        """int QRegExp.matchedLength()"""
        return int()
    def lastIndexIn(_str, _offset, _caretMode):
        """int QRegExp.lastIndexIn(QString _str, int _offset, QRegExp.CaretMode _caretMode)"""
        return int()
    def indexIn(_str, _offset, _caretMode):
        """int QRegExp.indexIn(QString _str, int _offset, QRegExp.CaretMode _caretMode)"""
        return int()
    def exactMatch(_str):
        """bool QRegExp.exactMatch(QString _str)"""
        return bool()
    def setMinimal(_minimal):
        """None QRegExp.setMinimal(bool _minimal)"""
        return None
    def isMinimal():
        """bool QRegExp.isMinimal()"""
        return bool()
    def setPatternSyntax(_syntax):
        """None QRegExp.setPatternSyntax(QRegExp.PatternSyntax _syntax)"""
        return None
    def patternSyntax():
        """QRegExp.PatternSyntax QRegExp.patternSyntax()"""
        return QRegExp.PatternSyntax()
    def setCaseSensitivity(_cs):
        """None QRegExp.setCaseSensitivity(Qt.CaseSensitivity _cs)"""
        return None
    def caseSensitivity():
        """Qt.CaseSensitivity QRegExp.caseSensitivity()"""
        return Qt.CaseSensitivity()
    def setPattern(_pattern):
        """None QRegExp.setPattern(QString _pattern)"""
        return None
    def pattern():
        """QString QRegExp.pattern()"""
        return QString()
    def isValid():
        """bool QRegExp.isValid()"""
        return bool()
    def isEmpty():
        """bool QRegExp.isEmpty()"""
        return bool()
    def __ne__(_rx):
        """bool QRegExp.__ne__(QRegExp _rx)"""
        return bool()
    def __eq__(_rx):
        """bool QRegExp.__eq__(QRegExp _rx)"""
        return bool()
    def __repr__():
        """str QRegExp.__repr__()"""
        return str()


class QResource():
    """"""
    def __init__(_fileName, _locale):
        """None QResource.__init__(QString _fileName, QLocale _locale)"""
        return None
    def isFile():
        """bool QResource.isFile()"""
        return bool()
    def isDir():
        """bool QResource.isDir()"""
        return bool()
    def children():
        """QStringList QResource.children()"""
        return QStringList()
    def unregisterResourceData(_rccData, _mapRoot):
        """bool QResource.unregisterResourceData(str _rccData, QString _mapRoot)"""
        return bool()
    def unregisterResource(_rccFileName, _mapRoot):
        """bool QResource.unregisterResource(QString _rccFileName, QString _mapRoot)"""
        return bool()
    def searchPaths():
        """QStringList QResource.searchPaths()"""
        return QStringList()
    def registerResourceData(_rccData, _mapRoot):
        """bool QResource.registerResourceData(str _rccData, QString _mapRoot)"""
        return bool()
    def registerResource(_rccFileName, _mapRoot):
        """bool QResource.registerResource(QString _rccFileName, QString _mapRoot)"""
        return bool()
    def addSearchPath(_path):
        """None QResource.addSearchPath(QString _path)"""
        return None
    def size():
        """int QResource.size()"""
        return int()
    def setLocale(_locale):
        """None QResource.setLocale(QLocale _locale)"""
        return None
    def setFileName(_file):
        """None QResource.setFileName(QString _file)"""
        return None
    def locale():
        """QLocale QResource.locale()"""
        return QLocale()
    def isValid():
        """bool QResource.isValid()"""
        return bool()
    def isCompressed():
        """bool QResource.isCompressed()"""
        return bool()
    def fileName():
        """QString QResource.fileName()"""
        return QString()
    def data():
        """str QResource.data()"""
        return str()
    def absoluteFilePath():
        """QString QResource.absoluteFilePath()"""
        return QString()


class QRunnable():
    """"""
    def __init__():
        """None QRunnable.__init__()"""
        return None
    def __init__():
        """QRunnable QRunnable.__init__()"""
        return QRunnable()
    def setAutoDelete(__autoDelete):
        """None QRunnable.setAutoDelete(bool __autoDelete)"""
        return None
    def autoDelete():
        """bool QRunnable.autoDelete()"""
        return bool()
    def run():
        """abstract None QRunnable.run()"""
        return None


class QSemaphore():
    """"""
    def __init__(_n):
        """None QSemaphore.__init__(int _n)"""
        return None
    def available():
        """int QSemaphore.available()"""
        return int()
    def release(_n):
        """None QSemaphore.release(int _n)"""
        return None
    def tryAcquire(_n):
        """bool QSemaphore.tryAcquire(int _n)"""
        return bool()
    def tryAcquire(_n, _timeout):
        """bool QSemaphore.tryAcquire(int _n, int _timeout)"""
        return bool()
    def acquire(_n):
        """None QSemaphore.acquire(int _n)"""
        return None


class QSequentialAnimationGroup(QAnimationGroup):
    """"""
    def __init__(_parent):
        """None QSequentialAnimationGroup.__init__(QObject _parent)"""
        return None
    def updateDirection(_direction):
        """None QSequentialAnimationGroup.updateDirection(QAbstractAnimation.Direction _direction)"""
        return None
    def updateState(_newState, _oldState):
        """None QSequentialAnimationGroup.updateState(QAbstractAnimation.State _newState, QAbstractAnimation.State _oldState)"""
        return None
    def updateCurrentTime():
        """int QSequentialAnimationGroup.updateCurrentTime()"""
        return int()
    def event(_event):
        """bool QSequentialAnimationGroup.event(QEvent _event)"""
        return bool()
    def duration():
        """int QSequentialAnimationGroup.duration()"""
        return int()
    def currentAnimation():
        """QAbstractAnimation QSequentialAnimationGroup.currentAnimation()"""
        return QAbstractAnimation()
    def insertPause(_index, _msecs):
        """QPauseAnimation QSequentialAnimationGroup.insertPause(int _index, int _msecs)"""
        return QPauseAnimation()
    def addPause(_msecs):
        """QPauseAnimation QSequentialAnimationGroup.addPause(int _msecs)"""
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

    def __init__(_organization, _application, _parent):
        """None QSettings.__init__(QString _organization, QString _application, QObject _parent)"""
        return None
    def __init__(_scope, _organization, _application, _parent):
        """None QSettings.__init__(QSettings.Scope _scope, QString _organization, QString _application, QObject _parent)"""
        return None
    def __init__(_format, _scope, _organization, _application, _parent):
        """None QSettings.__init__(QSettings.Format _format, QSettings.Scope _scope, QString _organization, QString _application, QObject _parent)"""
        return None
    def __init__(_fileName, _format, _parent):
        """None QSettings.__init__(QString _fileName, QSettings.Format _format, QObject _parent)"""
        return None
    def __init__(_parent):
        """None QSettings.__init__(QObject _parent)"""
        return None
    def event(_event):
        """bool QSettings.event(QEvent _event)"""
        return bool()
    def iniCodec():
        """QTextCodec QSettings.iniCodec()"""
        return QTextCodec()
    def setIniCodec(_codec):
        """None QSettings.setIniCodec(QTextCodec _codec)"""
        return None
    def setIniCodec(_codecName):
        """None QSettings.setIniCodec(str _codecName)"""
        return None
    def defaultFormat():
        """QSettings.Format QSettings.defaultFormat()"""
        return QSettings.Format()
    def setDefaultFormat(_format):
        """None QSettings.setDefaultFormat(QSettings.Format _format)"""
        return None
    def applicationName():
        """QString QSettings.applicationName()"""
        return QString()
    def organizationName():
        """QString QSettings.organizationName()"""
        return QString()
    def scope():
        """QSettings.Scope QSettings.scope()"""
        return QSettings.Scope()
    def format():
        """QSettings.Format QSettings.format()"""
        return QSettings.Format()
    def setPath(_format, _scope, _path):
        """None QSettings.setPath(QSettings.Format _format, QSettings.Scope _scope, QString _path)"""
        return None
    def setUserIniPath(_dir):
        """None QSettings.setUserIniPath(QString _dir)"""
        return None
    def setSystemIniPath(_dir):
        """None QSettings.setSystemIniPath(QString _dir)"""
        return None
    def fileName():
        """QString QSettings.fileName()"""
        return QString()
    def fallbacksEnabled():
        """bool QSettings.fallbacksEnabled()"""
        return bool()
    def setFallbacksEnabled(_b):
        """None QSettings.setFallbacksEnabled(bool _b)"""
        return None
    def contains(_key):
        """bool QSettings.contains(QString _key)"""
        return bool()
    def remove(_key):
        """None QSettings.remove(QString _key)"""
        return None
    def value(_key, _defaultValue, _type):
        """object QSettings.value(QString _key, QVariant _defaultValue, object _type)"""
        return object()
    def setValue(_key, _value):
        """None QSettings.setValue(QString _key, QVariant _value)"""
        return None
    def isWritable():
        """bool QSettings.isWritable()"""
        return bool()
    def childGroups():
        """QStringList QSettings.childGroups()"""
        return QStringList()
    def childKeys():
        """QStringList QSettings.childKeys()"""
        return QStringList()
    def allKeys():
        """QStringList QSettings.allKeys()"""
        return QStringList()
    def setArrayIndex(_i):
        """None QSettings.setArrayIndex(int _i)"""
        return None
    def endArray():
        """None QSettings.endArray()"""
        return None
    def beginWriteArray(_prefix, _size):
        """None QSettings.beginWriteArray(QString _prefix, int _size)"""
        return None
    def beginReadArray(_prefix):
        """int QSettings.beginReadArray(QString _prefix)"""
        return int()
    def group():
        """QString QSettings.group()"""
        return QString()
    def endGroup():
        """None QSettings.endGroup()"""
        return None
    def beginGroup(_prefix):
        """None QSettings.beginGroup(QString _prefix)"""
        return None
    def status():
        """QSettings.Status QSettings.status()"""
        return QSettings.Status()
    def sync():
        """None QSettings.sync()"""
        return None
    def clear():
        """None QSettings.clear()"""
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

    def __init__(_parent):
        """None QSharedMemory.__init__(QObject _parent)"""
        return None
    def __init__(_key, _parent):
        """None QSharedMemory.__init__(QString _key, QObject _parent)"""
        return None
    def errorString():
        """QString QSharedMemory.errorString()"""
        return QString()
    def error():
        """QSharedMemory.SharedMemoryError QSharedMemory.error()"""
        return QSharedMemory.SharedMemoryError()
    def unlock():
        """bool QSharedMemory.unlock()"""
        return bool()
    def lock():
        """bool QSharedMemory.lock()"""
        return bool()
    def constData():
        """sip.voidptr QSharedMemory.constData()"""
        return sip.voidptr()
    def data():
        """sip.voidptr QSharedMemory.data()"""
        return sip.voidptr()
    def detach():
        """bool QSharedMemory.detach()"""
        return bool()
    def isAttached():
        """bool QSharedMemory.isAttached()"""
        return bool()
    def attach(_mode):
        """bool QSharedMemory.attach(QSharedMemory.AccessMode _mode)"""
        return bool()
    def size():
        """int QSharedMemory.size()"""
        return int()
    def create(_size, _mode):
        """bool QSharedMemory.create(int _size, QSharedMemory.AccessMode _mode)"""
        return bool()
    def key():
        """QString QSharedMemory.key()"""
        return QString()
    def setKey(_key):
        """None QSharedMemory.setKey(QString _key)"""
        return None


class QSignalMapper(QObject):
    """"""
    def __init__(_parent):
        """None QSignalMapper.__init__(QObject _parent)"""
        return None
    def map():
        """None QSignalMapper.map()"""
        return None
    def map(_sender):
        """None QSignalMapper.map(QObject _sender)"""
        return None
    def mapping(_id):
        """QObject QSignalMapper.mapping(int _id)"""
        return QObject()
    def mapping(_text):
        """QObject QSignalMapper.mapping(QString _text)"""
        return QObject()
    def mapping(_widget):
        """QObject QSignalMapper.mapping(QWidget _widget)"""
        return QObject()
    def mapping(_object):
        """QObject QSignalMapper.mapping(QObject _object)"""
        return QObject()
    def removeMappings(_sender):
        """None QSignalMapper.removeMappings(QObject _sender)"""
        return None
    def setMapping(_sender, _id):
        """None QSignalMapper.setMapping(QObject _sender, int _id)"""
        return None
    def setMapping(_sender, _text):
        """None QSignalMapper.setMapping(QObject _sender, QString _text)"""
        return None
    def setMapping(_sender, _widget):
        """None QSignalMapper.setMapping(QObject _sender, QWidget _widget)"""
        return None
    def setMapping(_sender, _object):
        """None QSignalMapper.setMapping(QObject _sender, QObject _object)"""
        return None


class QSignalTransition(QAbstractTransition):
    """"""
    def __init__(_sourceState):
        """None QSignalTransition.__init__(QState _sourceState)"""
        return None
    def __init__(_sender, _signal, _sourceState):
        """None QSignalTransition.__init__(QObject _sender, SIGNAL() _signal, QState _sourceState)"""
        return None
    def __init__(_signal, _sourceState):
        """None QSignalTransition.__init__(signal _signal, QState _sourceState)"""
        return None
    def event(_e):
        """bool QSignalTransition.event(QEvent _e)"""
        return bool()
    def onTransition(_event):
        """None QSignalTransition.onTransition(QEvent _event)"""
        return None
    def eventTest(_event):
        """bool QSignalTransition.eventTest(QEvent _event)"""
        return bool()
    def setSignal(_signal):
        """None QSignalTransition.setSignal(QByteArray _signal)"""
        return None
    def signal():
        """QByteArray QSignalTransition.signal()"""
        return QByteArray()
    def setSenderObject(_sender):
        """None QSignalTransition.setSenderObject(QObject _sender)"""
        return None
    def senderObject():
        """QObject QSignalTransition.senderObject()"""
        return QObject()


class QSize():
    """"""
    def __init__():
        """None QSize.__init__()"""
        return None
    def __init__(_w, _h):
        """None QSize.__init__(int _w, int _h)"""
        return None
    def __init__():
        """QSize QSize.__init__()"""
        return QSize()
    def __eq__(_s2):
        """bool QSize.__eq__(QSize _s2)"""
        return bool()
    def __ne__(_s2):
        """bool QSize.__ne__(QSize _s2)"""
        return bool()
    def __add__(_s2):
        """QSize QSize.__add__(QSize _s2)"""
        return QSize()
    def __sub__(_s2):
        """QSize QSize.__sub__(QSize _s2)"""
        return QSize()
    def __mul__(_c):
        """QSize QSize.__mul__(float _c)"""
        return QSize()
    def __mul__(_s):
        """QSize QSize.__mul__(QSize _s)"""
        return QSize()
    def __div__(_c):
        """QSize QSize.__div__(float _c)"""
        return QSize()
    def boundedTo(_otherSize):
        """QSize QSize.boundedTo(QSize _otherSize)"""
        return QSize()
    def expandedTo(_otherSize):
        """QSize QSize.expandedTo(QSize _otherSize)"""
        return QSize()
    def __idiv__(_c):
        """QSize QSize.__idiv__(float _c)"""
        return QSize()
    def __imul__(_c):
        """QSize QSize.__imul__(float _c)"""
        return QSize()
    def __isub__(_s):
        """QSize QSize.__isub__(QSize _s)"""
        return QSize()
    def __iadd__(_s):
        """QSize QSize.__iadd__(QSize _s)"""
        return QSize()
    def setHeight(_h):
        """None QSize.setHeight(int _h)"""
        return None
    def setWidth(_w):
        """None QSize.setWidth(int _w)"""
        return None
    def height():
        """int QSize.height()"""
        return int()
    def width():
        """int QSize.width()"""
        return int()
    def __bool__():
        """int QSize.__bool__()"""
        return int()
    def isValid():
        """bool QSize.isValid()"""
        return bool()
    def isEmpty():
        """bool QSize.isEmpty()"""
        return bool()
    def isNull():
        """bool QSize.isNull()"""
        return bool()
    def __repr__():
        """str QSize.__repr__()"""
        return str()
    def scale(_s, _mode):
        """None QSize.scale(QSize _s, Qt.AspectRatioMode _mode)"""
        return None
    def scale(_w, _h, _mode):
        """None QSize.scale(int _w, int _h, Qt.AspectRatioMode _mode)"""
        return None
    def transpose():
        """None QSize.transpose()"""
        return None


class QSizeF():
    """"""
    def __init__():
        """None QSizeF.__init__()"""
        return None
    def __init__(_sz):
        """None QSizeF.__init__(QSize _sz)"""
        return None
    def __init__(_w, _h):
        """None QSizeF.__init__(float _w, float _h)"""
        return None
    def __init__():
        """QSizeF QSizeF.__init__()"""
        return QSizeF()
    def __eq__(_s2):
        """bool QSizeF.__eq__(QSizeF _s2)"""
        return bool()
    def __ne__(_s2):
        """bool QSizeF.__ne__(QSizeF _s2)"""
        return bool()
    def __add__(_s2):
        """QSizeF QSizeF.__add__(QSizeF _s2)"""
        return QSizeF()
    def __sub__(_s2):
        """QSizeF QSizeF.__sub__(QSizeF _s2)"""
        return QSizeF()
    def __mul__(_c):
        """QSizeF QSizeF.__mul__(float _c)"""
        return QSizeF()
    def __mul__(_s):
        """QSizeF QSizeF.__mul__(QSizeF _s)"""
        return QSizeF()
    def __div__(_c):
        """QSizeF QSizeF.__div__(float _c)"""
        return QSizeF()
    def toSize():
        """QSize QSizeF.toSize()"""
        return QSize()
    def boundedTo(_otherSize):
        """QSizeF QSizeF.boundedTo(QSizeF _otherSize)"""
        return QSizeF()
    def expandedTo(_otherSize):
        """QSizeF QSizeF.expandedTo(QSizeF _otherSize)"""
        return QSizeF()
    def __idiv__(_c):
        """QSizeF QSizeF.__idiv__(float _c)"""
        return QSizeF()
    def __imul__(_c):
        """QSizeF QSizeF.__imul__(float _c)"""
        return QSizeF()
    def __isub__(_s):
        """QSizeF QSizeF.__isub__(QSizeF _s)"""
        return QSizeF()
    def __iadd__(_s):
        """QSizeF QSizeF.__iadd__(QSizeF _s)"""
        return QSizeF()
    def setHeight(_h):
        """None QSizeF.setHeight(float _h)"""
        return None
    def setWidth(_w):
        """None QSizeF.setWidth(float _w)"""
        return None
    def height():
        """float QSizeF.height()"""
        return float()
    def width():
        """float QSizeF.width()"""
        return float()
    def __bool__():
        """int QSizeF.__bool__()"""
        return int()
    def isValid():
        """bool QSizeF.isValid()"""
        return bool()
    def isEmpty():
        """bool QSizeF.isEmpty()"""
        return bool()
    def isNull():
        """bool QSizeF.isNull()"""
        return bool()
    def __repr__():
        """str QSizeF.__repr__()"""
        return str()
    def scale(_s, _mode):
        """None QSizeF.scale(QSizeF _s, Qt.AspectRatioMode _mode)"""
        return None
    def scale(_w, _h, _mode):
        """None QSizeF.scale(float _w, float _h, Qt.AspectRatioMode _mode)"""
        return None
    def transpose():
        """None QSizeF.transpose()"""
        return None


class QSocketNotifier(QObject):
    """"""
    Read = int() # QSocketNotifier.Type enum
    Write = int() # QSocketNotifier.Type enum
    Exception = int() # QSocketNotifier.Type enum

    def __init__(_socket, _type, _parent):
        """None QSocketNotifier.__init__(int _socket, QSocketNotifier.Type _type, QObject _parent)"""
        return None
    def event():
        """QEvent QSocketNotifier.event()"""
        return QEvent()
    def setEnabled():
        """bool QSocketNotifier.setEnabled()"""
        return bool()
    def isEnabled():
        """bool QSocketNotifier.isEnabled()"""
        return bool()
    def type():
        """QSocketNotifier.Type QSocketNotifier.type()"""
        return QSocketNotifier.Type()
    def socket():
        """int QSocketNotifier.socket()"""
        return int()


class QState(QAbstractState):
    """"""
    ExclusiveStates = int() # QState.ChildMode enum
    ParallelStates = int() # QState.ChildMode enum

    def __init__(_parent):
        """None QState.__init__(QState _parent)"""
        return None
    def __init__(_childMode, _parent):
        """None QState.__init__(QState.ChildMode _childMode, QState _parent)"""
        return None
    def event(_e):
        """bool QState.event(QEvent _e)"""
        return bool()
    def onExit(_event):
        """None QState.onExit(QEvent _event)"""
        return None
    def onEntry(_event):
        """None QState.onEntry(QEvent _event)"""
        return None
    def assignProperty(_object, _name, _value):
        """None QState.assignProperty(QObject _object, str _name, QVariant _value)"""
        return None
    def setChildMode(_mode):
        """None QState.setChildMode(QState.ChildMode _mode)"""
        return None
    def childMode():
        """QState.ChildMode QState.childMode()"""
        return QState.ChildMode()
    def setInitialState(_state):
        """None QState.setInitialState(QAbstractState _state)"""
        return None
    def initialState():
        """QAbstractState QState.initialState()"""
        return QAbstractState()
    def transitions():
        """list-of-QAbstractTransition QState.transitions()"""
        return [QAbstractTransition()]
    def removeTransition(_transition):
        """None QState.removeTransition(QAbstractTransition _transition)"""
        return None
    def addTransition(_transition):
        """None QState.addTransition(QAbstractTransition _transition)"""
        return None
    def addTransition(_sender, _signal, _target):
        """QSignalTransition QState.addTransition(QObject _sender, SIGNAL() _signal, QAbstractState _target)"""
        return QSignalTransition()
    def addTransition(_signal, _target):
        """QSignalTransition QState.addTransition(signal _signal, QAbstractState _target)"""
        return QSignalTransition()
    def addTransition(_target):
        """QAbstractTransition QState.addTransition(QAbstractState _target)"""
        return QAbstractTransition()
    def setErrorState(_state):
        """None QState.setErrorState(QAbstractState _state)"""
        return None
    def errorState():
        """QAbstractState QState.errorState()"""
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

    def __init__(_parent):
        """None QStateMachine.__init__(QObject _parent)"""
        return None
    def event(_e):
        """bool QStateMachine.event(QEvent _e)"""
        return bool()
    def onExit(_event):
        """None QStateMachine.onExit(QEvent _event)"""
        return None
    def onEntry(_event):
        """None QStateMachine.onEntry(QEvent _event)"""
        return None
    def stop():
        """None QStateMachine.stop()"""
        return None
    def start():
        """None QStateMachine.start()"""
        return None
    def eventFilter(_watched, _event):
        """bool QStateMachine.eventFilter(QObject _watched, QEvent _event)"""
        return bool()
    def configuration():
        """list-of-QAbstractState QStateMachine.configuration()"""
        return [QAbstractState()]
    def cancelDelayedEvent(_id):
        """bool QStateMachine.cancelDelayedEvent(int _id)"""
        return bool()
    def postDelayedEvent(_event, _delay):
        """int QStateMachine.postDelayedEvent(QEvent _event, int _delay)"""
        return int()
    def postEvent(_event, _priority):
        """None QStateMachine.postEvent(QEvent _event, QStateMachine.EventPriority _priority)"""
        return None
    def setGlobalRestorePolicy(_restorePolicy):
        """None QStateMachine.setGlobalRestorePolicy(QStateMachine.RestorePolicy _restorePolicy)"""
        return None
    def globalRestorePolicy():
        """QStateMachine.RestorePolicy QStateMachine.globalRestorePolicy()"""
        return QStateMachine.RestorePolicy()
    def removeDefaultAnimation(_animation):
        """None QStateMachine.removeDefaultAnimation(QAbstractAnimation _animation)"""
        return None
    def defaultAnimations():
        """list-of-QAbstractAnimation QStateMachine.defaultAnimations()"""
        return [QAbstractAnimation()]
    def addDefaultAnimation(_animation):
        """None QStateMachine.addDefaultAnimation(QAbstractAnimation _animation)"""
        return None
    def setAnimated(_enabled):
        """None QStateMachine.setAnimated(bool _enabled)"""
        return None
    def isAnimated():
        """bool QStateMachine.isAnimated()"""
        return bool()
    def isRunning():
        """bool QStateMachine.isRunning()"""
        return bool()
    def clearError():
        """None QStateMachine.clearError()"""
        return None
    def errorString():
        """QString QStateMachine.errorString()"""
        return QString()
    def error():
        """QStateMachine.Error QStateMachine.error()"""
        return QStateMachine.Error()
    def removeState(_state):
        """None QStateMachine.removeState(QAbstractState _state)"""
        return None
    def addState(_state):
        """None QStateMachine.addState(QAbstractState _state)"""
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

    def __init__():
        """None QString.__init__()"""
        return None
    def __init__(_size, _c):
        """None QString.__init__(int _size, QChar _c)"""
        return None
    def __init__(_s):
        """None QString.__init__(QString _s)"""
        return None
    def __init__(_a):
        """None QString.__init__(QByteArray _a)"""
        return None
    def __init__():
        """QUuid QString.__init__()"""
        return QUuid()
    def __add__(_s2):
        """QString QString.__add__(QString _s2)"""
        return QString()
    def __add__(_ba):
        """QString QString.__add__(QByteArray _ba)"""
        return QString()
    def repeated(_times):
        """QString QString.repeated(int _times)"""
        return QString()
    def toCaseFolded():
        """QString QString.toCaseFolded()"""
        return QString()
    def reserve(_asize):
        """None QString.reserve(int _asize)"""
        return None
    def capacity():
        """int QString.capacity()"""
        return int()
    def clear():
        """None QString.clear()"""
        return None
    def isEmpty():
        """bool QString.isEmpty()"""
        return bool()
    def __imul__(_m):
        """QString QString.__imul__(int _m)"""
        return QString()
    def __mul__(_m):
        """QString QString.__mul__(int _m)"""
        return QString()
    def __hash__():
        """int QString.__hash__()"""
        return int()
    def __str__():
        """str QString.__str__()"""
        return str()
    def __unicode__():
        """unicode QString.__unicode__()"""
        return unicode()
    def __contains__(_s):
        """int QString.__contains__(QString _s)"""
        return int()
    def __getitem__(_i):
        """QString QString.__getitem__(int _i)"""
        return QString()
    def __getitem__(_slice):
        """QString QString.__getitem__(slice _slice)"""
        return QString()
    def at(_i):
        """QChar QString.at(int _i)"""
        return QChar()
    def length():
        """int QString.length()"""
        return int()
    def isRightToLeft():
        """bool QString.isRightToLeft()"""
        return bool()
    def isSimpleText():
        """bool QString.isSimpleText()"""
        return bool()
    def isNull():
        """bool QString.isNull()"""
        return bool()
    def push_front(_s):
        """None QString.push_front(QString _s)"""
        return None
    def push_back(_s):
        """None QString.push_back(QString _s)"""
        return None
    def __ge__(_s):
        """bool QString.__ge__(QString _s)"""
        return bool()
    def __ge__(_s):
        """bool QString.__ge__(QLatin1String _s)"""
        return bool()
    def __ge__(_s):
        """bool QString.__ge__(QByteArray _s)"""
        return bool()
    def __le__(_s):
        """bool QString.__le__(QString _s)"""
        return bool()
    def __le__(_s):
        """bool QString.__le__(QLatin1String _s)"""
        return bool()
    def __le__(_s):
        """bool QString.__le__(QByteArray _s)"""
        return bool()
    def __ne__(_s):
        """bool QString.__ne__(QString _s)"""
        return bool()
    def __ne__(_s):
        """bool QString.__ne__(QLatin1String _s)"""
        return bool()
    def __ne__(_s):
        """bool QString.__ne__(QByteArray _s)"""
        return bool()
    def __ne__(_s2):
        """bool QString.__ne__(QStringRef _s2)"""
        return bool()
    def __gt__(_s):
        """bool QString.__gt__(QString _s)"""
        return bool()
    def __gt__(_s):
        """bool QString.__gt__(QLatin1String _s)"""
        return bool()
    def __gt__(_s):
        """bool QString.__gt__(QByteArray _s)"""
        return bool()
    def __lt__(_s):
        """bool QString.__lt__(QString _s)"""
        return bool()
    def __lt__(_s):
        """bool QString.__lt__(QLatin1String _s)"""
        return bool()
    def __lt__(_s):
        """bool QString.__lt__(QByteArray _s)"""
        return bool()
    def __eq__(_s):
        """bool QString.__eq__(QString _s)"""
        return bool()
    def __eq__(_s):
        """bool QString.__eq__(QLatin1String _s)"""
        return bool()
    def __eq__(_s):
        """bool QString.__eq__(QByteArray _s)"""
        return bool()
    def __eq__(_s2):
        """bool QString.__eq__(QStringRef _s2)"""
        return bool()
    def number(_n, _base):
        """QString QString.number(int _n, int _base)"""
        return QString()
    def number(_n, _format, _precision):
        """QString QString.number(float _n, str _format, int _precision)"""
        return QString()
    def number(_n, _base):
        """QString QString.number(int _n, int _base)"""
        return QString()
    def number(_n, _base):
        """QString QString.number(int _n, int _base)"""
        return QString()
    def setNum(_n, _base):
        """QString QString.setNum(int _n, int _base)"""
        return QString()
    def setNum(_n, _format, _precision):
        """QString QString.setNum(float _n, str _format, int _precision)"""
        return QString()
    def setNum(_n, _base):
        """QString QString.setNum(int _n, int _base)"""
        return QString()
    def setNum(_n, _base):
        """QString QString.setNum(int _n, int _base)"""
        return QString()
    def toDouble(_ok):
        """float QString.toDouble(bool _ok)"""
        return float()
    def toFloat(_ok):
        """float QString.toFloat(bool _ok)"""
        return float()
    def toULongLong(_ok, _base):
        """int QString.toULongLong(bool _ok, int _base)"""
        return int()
    def toLongLong(_ok, _base):
        """int QString.toLongLong(bool _ok, int _base)"""
        return int()
    def toULong(_ok, _base):
        """int QString.toULong(bool _ok, int _base)"""
        return int()
    def toLong(_ok, _base):
        """int QString.toLong(bool _ok, int _base)"""
        return int()
    def toUInt(_ok, _base):
        """int QString.toUInt(bool _ok, int _base)"""
        return int()
    def toInt(_ok, _base):
        """int QString.toInt(bool _ok, int _base)"""
        return int()
    def toUShort(_ok, _base):
        """int QString.toUShort(bool _ok, int _base)"""
        return int()
    def toShort(_ok, _base):
        """int QString.toShort(bool _ok, int _base)"""
        return int()
    def localeAwareCompare(_s):
        """int QString.localeAwareCompare(QString _s)"""
        return int()
    def localeAwareCompare(_s):
        """int QString.localeAwareCompare(QStringRef _s)"""
        return int()
    def localeAwareCompare(_s1, _s2):
        """int QString.localeAwareCompare(QString _s1, QString _s2)"""
        return int()
    def localeAwareCompare(_s1, _s2):
        """int QString.localeAwareCompare(QString _s1, QStringRef _s2)"""
        return int()
    def compare(_s):
        """int QString.compare(QString _s)"""
        return int()
    def compare(_s, _cs):
        """int QString.compare(QString _s, Qt.CaseSensitivity _cs)"""
        return int()
    def compare(_other, _cs):
        """int QString.compare(QLatin1String _other, Qt.CaseSensitivity _cs)"""
        return int()
    def compare(_ref, _cs):
        """int QString.compare(QStringRef _ref, Qt.CaseSensitivity _cs)"""
        return int()
    def compare(_s1, _s2):
        """int QString.compare(QString _s1, QString _s2)"""
        return int()
    def compare(_s1, _s2, _cs):
        """int QString.compare(QString _s1, QString _s2, Qt.CaseSensitivity _cs)"""
        return int()
    def compare(_s1, _s2, _cs):
        """int QString.compare(QString _s1, QLatin1String _s2, Qt.CaseSensitivity _cs)"""
        return int()
    def compare(_s1, _s2, _cs):
        """int QString.compare(QLatin1String _s1, QString _s2, Qt.CaseSensitivity _cs)"""
        return int()
    def compare(_s1, _s2, _cs):
        """int QString.compare(QString _s1, QStringRef _s2, Qt.CaseSensitivity _cs)"""
        return int()
    def fromLocal8Bit(_str, _size):
        """QString QString.fromLocal8Bit(str _str, int _size)"""
        return QString()
    def fromUtf8(_str, _size):
        """QString QString.fromUtf8(str _str, int _size)"""
        return QString()
    def fromLatin1(_str, _size):
        """QString QString.fromLatin1(str _str, int _size)"""
        return QString()
    def fromAscii(_str, _size):
        """QString QString.fromAscii(str _str, int _size)"""
        return QString()
    def toLocal8Bit():
        """QByteArray QString.toLocal8Bit()"""
        return QByteArray()
    def toUtf8():
        """QByteArray QString.toUtf8()"""
        return QByteArray()
    def toLatin1():
        """QByteArray QString.toLatin1()"""
        return QByteArray()
    def toAscii():
        """QByteArray QString.toAscii()"""
        return QByteArray()
    def normalized(_mode):
        """QString QString.normalized(QString.NormalizationForm _mode)"""
        return QString()
    def normalized(_mode, _version):
        """QString QString.normalized(QString.NormalizationForm _mode, QChar.UnicodeVersion _version)"""
        return QString()
    def split(_sep, _behavior, _cs):
        """QStringList QString.split(QString _sep, QString.SplitBehavior _behavior, Qt.CaseSensitivity _cs)"""
        return QStringList()
    def split(_sep, _behavior):
        """QStringList QString.split(QRegExp _sep, QString.SplitBehavior _behavior)"""
        return QStringList()
    def replace(_i, _len, _after):
        """QString QString.replace(int _i, int _len, QString _after)"""
        return QString()
    def replace(_before, _after, _cs):
        """QString QString.replace(QString _before, QString _after, Qt.CaseSensitivity _cs)"""
        return QString()
    def replace(_rx, _after):
        """QString QString.replace(QRegExp _rx, QString _after)"""
        return QString()
    def replace(_before, _after, _cs):
        """QString QString.replace(QLatin1String _before, QLatin1String _after, Qt.CaseSensitivity _cs)"""
        return QString()
    def replace(_before, _after, _cs):
        """QString QString.replace(QLatin1String _before, QString _after, Qt.CaseSensitivity _cs)"""
        return QString()
    def replace(_before, _after, _cs):
        """QString QString.replace(QString _before, QLatin1String _after, Qt.CaseSensitivity _cs)"""
        return QString()
    def remove(_i, _len):
        """QString QString.remove(int _i, int _len)"""
        return QString()
    def remove(_str, _cs):
        """QString QString.remove(QString _str, Qt.CaseSensitivity _cs)"""
        return QString()
    def remove(_rx):
        """QString QString.remove(QRegExp _rx)"""
        return QString()
    def __iadd__(_c):
        """QString QString.__iadd__(QChar.SpecialCharacter _c)"""
        return QString()
    def __iadd__(_s):
        """QString QString.__iadd__(QString _s)"""
        return QString()
    def __iadd__(_s):
        """QString QString.__iadd__(QLatin1String _s)"""
        return QString()
    def __iadd__(_s):
        """QString QString.__iadd__(QByteArray _s)"""
        return QString()
    def prepend(_s):
        """QString QString.prepend(QString _s)"""
        return QString()
    def prepend(_s):
        """QString QString.prepend(QLatin1String _s)"""
        return QString()
    def prepend(_s):
        """QString QString.prepend(QByteArray _s)"""
        return QString()
    def append(_s):
        """QString QString.append(QString _s)"""
        return QString()
    def append(_s):
        """QString QString.append(QLatin1String _s)"""
        return QString()
    def append(_s):
        """QString QString.append(QByteArray _s)"""
        return QString()
    def insert(_i, _s):
        """QString QString.insert(int _i, QString _s)"""
        return QString()
    def insert(_i, _s):
        """QString QString.insert(int _i, QLatin1String _s)"""
        return QString()
    def simplified():
        """QString QString.simplified()"""
        return QString()
    def trimmed():
        """QString QString.trimmed()"""
        return QString()
    def toUpper():
        """QString QString.toUpper()"""
        return QString()
    def toLower():
        """QString QString.toLower()"""
        return QString()
    def rightJustified(_width, _fillChar, _truncate):
        """QString QString.rightJustified(int _width, QChar _fillChar, bool _truncate)"""
        return QString()
    def leftJustified(_width, _fillChar, _truncate):
        """QString QString.leftJustified(int _width, QChar _fillChar, bool _truncate)"""
        return QString()
    def endsWith(_s, _cs):
        """bool QString.endsWith(QString _s, Qt.CaseSensitivity _cs)"""
        return bool()
    def endsWith(_s, _cs):
        """bool QString.endsWith(QLatin1String _s, Qt.CaseSensitivity _cs)"""
        return bool()
    def startsWith(_s, _cs):
        """bool QString.startsWith(QString _s, Qt.CaseSensitivity _cs)"""
        return bool()
    def startsWith(_s, _cs):
        """bool QString.startsWith(QLatin1String _s, Qt.CaseSensitivity _cs)"""
        return bool()
    def mid(_position, _n):
        """QString QString.mid(int _position, int _n)"""
        return QString()
    def right(_len):
        """QString QString.right(int _len)"""
        return QString()
    def left(_len):
        """QString QString.left(int _len)"""
        return QString()
    def section(_sep, _start, _end, _flags):
        """QString QString.section(QString _sep, int _start, int _end, QString.SectionFlags _flags)"""
        return QString()
    def section(_reg, _start, _end, _flags):
        """QString QString.section(QRegExp _reg, int _start, int _end, QString.SectionFlags _flags)"""
        return QString()
    def contains(_str, _cs):
        """bool QString.contains(QString _str, Qt.CaseSensitivity _cs)"""
        return bool()
    def contains(_rx):
        """bool QString.contains(QRegExp _rx)"""
        return bool()
    def lastIndexOf(_str, _from, _cs):
        """int QString.lastIndexOf(QString _str, int _from, Qt.CaseSensitivity _cs)"""
        return int()
    def lastIndexOf(_str, _from, _cs):
        """int QString.lastIndexOf(QLatin1String _str, int _from, Qt.CaseSensitivity _cs)"""
        return int()
    def lastIndexOf(_rx, _from):
        """int QString.lastIndexOf(QRegExp _rx, int _from)"""
        return int()
    def indexOf(_str, _from, _cs):
        """int QString.indexOf(QString _str, int _from, Qt.CaseSensitivity _cs)"""
        return int()
    def indexOf(_str, _from, _cs):
        """int QString.indexOf(QLatin1String _str, int _from, Qt.CaseSensitivity _cs)"""
        return int()
    def indexOf(_rx, _from):
        """int QString.indexOf(QRegExp _rx, int _from)"""
        return int()
    def arg(_a, _fieldWidth, _base, _fillChar):
        """QString QString.arg(int _a, int _fieldWidth, int _base, QChar _fillChar)"""
        return QString()
    def arg(_a, _fieldWidth, _format, _precision, _fillChar):
        """QString QString.arg(float _a, int _fieldWidth, str _format, int _precision, QChar _fillChar)"""
        return QString()
    def arg(_a, _fieldWidth, _base, _fillChar):
        """QString QString.arg(int _a, int _fieldWidth, int _base, QChar _fillChar)"""
        return QString()
    def arg(_a, _fieldWidth, _base, _fillChar):
        """QString QString.arg(int _a, int _fieldWidth, int _base, QChar _fillChar)"""
        return QString()
    def arg(_a, _fieldWidth, _fillChar):
        """QString QString.arg(QString _a, int _fieldWidth, QChar _fillChar)"""
        return QString()
    def arg(_a1, _a2):
        """QString QString.arg(QString _a1, QString _a2)"""
        return QString()
    def arg(_a1, _a2, _a3):
        """QString QString.arg(QString _a1, QString _a2, QString _a3)"""
        return QString()
    def arg(_a1, _a2, _a3, _a4):
        """QString QString.arg(QString _a1, QString _a2, QString _a3, QString _a4)"""
        return QString()
    def arg(_a1, _a2, _a3, _a4, _a5):
        """QString QString.arg(QString _a1, QString _a2, QString _a3, QString _a4, QString _a5)"""
        return QString()
    def arg(_a1, _a2, _a3, _a4, _a5, _a6):
        """QString QString.arg(QString _a1, QString _a2, QString _a3, QString _a4, QString _a5, QString _a6)"""
        return QString()
    def arg(_a1, _a2, _a3, _a4, _a5, _a6, _a7):
        """QString QString.arg(QString _a1, QString _a2, QString _a3, QString _a4, QString _a5, QString _a6, QString _a7)"""
        return QString()
    def arg(_a1, _a2, _a3, _a4, _a5, _a6, _a7, _a8):
        """QString QString.arg(QString _a1, QString _a2, QString _a3, QString _a4, QString _a5, QString _a6, QString _a7, QString _a8)"""
        return QString()
    def arg(_a1, _a2, _a3, _a4, _a5, _a6, _a7, _a8, _a9):
        """QString QString.arg(QString _a1, QString _a2, QString _a3, QString _a4, QString _a5, QString _a6, QString _a7, QString _a8, QString _a9)"""
        return QString()
    def squeeze():
        """None QString.squeeze()"""
        return None
    def chop(_n):
        """None QString.chop(int _n)"""
        return None
    def truncate(_pos):
        """None QString.truncate(int _pos)"""
        return None
    def fill(_ch, _size):
        """QString QString.fill(QChar _ch, int _size)"""
        return QString()
    def resize(_size):
        """None QString.resize(int _size)"""
        return None
    def __len__():
        """ QString.__len__()"""
        return ()
    def count():
        """int QString.count()"""
        return int()
    def count(_str, _cs):
        """int QString.count(QString _str, Qt.CaseSensitivity _cs)"""
        return int()
    def count():
        """QRegExp QString.count()"""
        return QRegExp()
    def size():
        """int QString.size()"""
        return int()
    def __repr__():
        """str QString.__repr__()"""
        return str()


class QLatin1String():
    """"""
    def __init__(_s):
        """None QLatin1String.__init__(str _s)"""
        return None
    def __init__():
        """QLatin1String QLatin1String.__init__()"""
        return QLatin1String()
    def __le__(_s):
        """bool QLatin1String.__le__(QString _s)"""
        return bool()
    def __le__(_s2):
        """bool QLatin1String.__le__(QLatin1String _s2)"""
        return bool()
    def __ge__(_s):
        """bool QLatin1String.__ge__(QString _s)"""
        return bool()
    def __ge__(_s2):
        """bool QLatin1String.__ge__(QLatin1String _s2)"""
        return bool()
    def __lt__(_s):
        """bool QLatin1String.__lt__(QString _s)"""
        return bool()
    def __lt__(_s2):
        """bool QLatin1String.__lt__(QLatin1String _s2)"""
        return bool()
    def __gt__(_s):
        """bool QLatin1String.__gt__(QString _s)"""
        return bool()
    def __gt__(_s2):
        """bool QLatin1String.__gt__(QLatin1String _s2)"""
        return bool()
    def __ne__(_s):
        """bool QLatin1String.__ne__(QString _s)"""
        return bool()
    def __ne__(_s2):
        """bool QLatin1String.__ne__(QLatin1String _s2)"""
        return bool()
    def __ne__(_s2):
        """bool QLatin1String.__ne__(QStringRef _s2)"""
        return bool()
    def __eq__(_s):
        """bool QLatin1String.__eq__(QString _s)"""
        return bool()
    def __eq__(_s2):
        """bool QLatin1String.__eq__(QLatin1String _s2)"""
        return bool()
    def __eq__(_s2):
        """bool QLatin1String.__eq__(QStringRef _s2)"""
        return bool()
    def latin1():
        """str QLatin1String.latin1()"""
        return str()
    def __repr__():
        """str QLatin1String.__repr__()"""
        return str()


class QStringRef():
    """"""
    def __init__():
        """None QStringRef.__init__()"""
        return None
    def __init__(_aString, _aPosition, _aSize):
        """None QStringRef.__init__(QString _aString, int _aPosition, int _aSize)"""
        return None
    def __init__(_aString):
        """None QStringRef.__init__(QString _aString)"""
        return None
    def __init__(_other):
        """None QStringRef.__init__(QStringRef _other)"""
        return None
    def __eq__(_s2):
        """bool QStringRef.__eq__(QStringRef _s2)"""
        return bool()
    def __eq__(_s2):
        """bool QStringRef.__eq__(QString _s2)"""
        return bool()
    def __eq__(_s2):
        """bool QStringRef.__eq__(QLatin1String _s2)"""
        return bool()
    def __ne__(_s2):
        """bool QStringRef.__ne__(QStringRef _s2)"""
        return bool()
    def __ne__(_s2):
        """bool QStringRef.__ne__(QString _s2)"""
        return bool()
    def __ne__(_s2):
        """bool QStringRef.__ne__(QLatin1String _s2)"""
        return bool()
    def __lt__(_s2):
        """bool QStringRef.__lt__(QStringRef _s2)"""
        return bool()
    def __le__(_s2):
        """bool QStringRef.__le__(QStringRef _s2)"""
        return bool()
    def __gt__(_s2):
        """bool QStringRef.__gt__(QStringRef _s2)"""
        return bool()
    def __ge__(_s2):
        """bool QStringRef.__ge__(QStringRef _s2)"""
        return bool()
    def __str__():
        """str QStringRef.__str__()"""
        return str()
    def __unicode__():
        """unicode QStringRef.__unicode__()"""
        return unicode()
    def localeAwareCompare(_s):
        """int QStringRef.localeAwareCompare(QString _s)"""
        return int()
    def localeAwareCompare(_s):
        """int QStringRef.localeAwareCompare(QStringRef _s)"""
        return int()
    def localeAwareCompare(_s1, _s2):
        """int QStringRef.localeAwareCompare(QStringRef _s1, QString _s2)"""
        return int()
    def localeAwareCompare(_s1, _s2):
        """int QStringRef.localeAwareCompare(QStringRef _s1, QStringRef _s2)"""
        return int()
    def compare(_other, _cs):
        """int QStringRef.compare(QString _other, Qt.CaseSensitivity _cs)"""
        return int()
    def compare(_other, _cs):
        """int QStringRef.compare(QStringRef _other, Qt.CaseSensitivity _cs)"""
        return int()
    def compare(_other, _cs):
        """int QStringRef.compare(QLatin1String _other, Qt.CaseSensitivity _cs)"""
        return int()
    def compare(_s1, _s2, _cs):
        """int QStringRef.compare(QStringRef _s1, QString _s2, Qt.CaseSensitivity _cs)"""
        return int()
    def compare(_s1, _s2, _cs):
        """int QStringRef.compare(QStringRef _s1, QStringRef _s2, Qt.CaseSensitivity _cs)"""
        return int()
    def compare(_s1, _s2, _cs):
        """int QStringRef.compare(QStringRef _s1, QLatin1String _s2, Qt.CaseSensitivity _cs)"""
        return int()
    def at(_i):
        """QChar QStringRef.at(int _i)"""
        return QChar()
    def appendTo(_string):
        """QStringRef QStringRef.appendTo(QString _string)"""
        return QStringRef()
    def isNull():
        """bool QStringRef.isNull()"""
        return bool()
    def isEmpty():
        """bool QStringRef.isEmpty()"""
        return bool()
    def toString():
        """QString QStringRef.toString()"""
        return QString()
    def clear():
        """None QStringRef.clear()"""
        return None
    def constData():
        """QChar QStringRef.constData()"""
        return QChar()
    def data():
        """QChar QStringRef.data()"""
        return QChar()
    def unicode():
        """QChar QStringRef.unicode()"""
        return QChar()
    def length():
        """int QStringRef.length()"""
        return int()
    def __len__():
        """ QStringRef.__len__()"""
        return ()
    def count():
        """int QStringRef.count()"""
        return int()
    def size():
        """int QStringRef.size()"""
        return int()
    def position():
        """int QStringRef.position()"""
        return int()
    def string():
        """QString QStringRef.string()"""
        return QString()


class QStringList():
    """"""
    def __init__():
        """None QStringList.__init__()"""
        return None
    def __init__(_i):
        """None QStringList.__init__(QString _i)"""
        return None
    def __init__(_l):
        """None QStringList.__init__(QStringList _l)"""
        return None
    def __iadd__(_other):
        """QStringList QStringList.__iadd__(QStringList _other)"""
        return QStringList()
    def __iadd__(_value):
        """QStringList QStringList.__iadd__(QString _value)"""
        return QStringList()
    def mid(_pos, _length):
        """QStringList QStringList.mid(int _pos, int _length)"""
        return QStringList()
    def last():
        """QString QStringList.last()"""
        return QString()
    def first():
        """QString QStringList.first()"""
        return QString()
    def __len__():
        """ QStringList.__len__()"""
        return ()
    def count(_str):
        """int QStringList.count(QString _str)"""
        return int()
    def count():
        """int QStringList.count()"""
        return int()
    def swap(_i, _j):
        """None QStringList.swap(int _i, int _j)"""
        return None
    def move(_from, _to):
        """None QStringList.move(int _from, int _to)"""
        return None
    def takeLast():
        """QString QStringList.takeLast()"""
        return QString()
    def takeFirst():
        """QString QStringList.takeFirst()"""
        return QString()
    def takeAt(_i):
        """QString QStringList.takeAt(int _i)"""
        return QString()
    def removeAll(_str):
        """int QStringList.removeAll(QString _str)"""
        return int()
    def removeAt(_i):
        """None QStringList.removeAt(int _i)"""
        return None
    def replace(_i, _str):
        """None QStringList.replace(int _i, QString _str)"""
        return None
    def insert(_i, _str):
        """None QStringList.insert(int _i, QString _str)"""
        return None
    def prepend(_str):
        """None QStringList.prepend(QString _str)"""
        return None
    def append(_str):
        """None QStringList.append(QString _str)"""
        return None
    def isEmpty():
        """bool QStringList.isEmpty()"""
        return bool()
    def clear():
        """None QStringList.clear()"""
        return None
    def __ne__(_other):
        """bool QStringList.__ne__(QStringList _other)"""
        return bool()
    def __eq__(_other):
        """bool QStringList.__eq__(QStringList _other)"""
        return bool()
    def __imul__(_by):
        """QStringList QStringList.__imul__(int _by)"""
        return QStringList()
    def __mul__(_by):
        """QStringList QStringList.__mul__(int _by)"""
        return QStringList()
    def __add__(_other):
        """QStringList QStringList.__add__(QStringList _other)"""
        return QStringList()
    def __contains__(_str):
        """int QStringList.__contains__(QString _str)"""
        return int()
    def __getitem__(_i):
        """QString QStringList.__getitem__(int _i)"""
        return QString()
    def __getitem__(_slice):
        """QStringList QStringList.__getitem__(slice _slice)"""
        return QStringList()
    def __delitem__(_i):
        """None QStringList.__delitem__(int _i)"""
        return None
    def __delitem__(_slice):
        """None QStringList.__delitem__(slice _slice)"""
        return None
    def __setitem__(_i, _str):
        """None QStringList.__setitem__(int _i, QString _str)"""
        return None
    def __setitem__(_slice, _list):
        """None QStringList.__setitem__(slice _slice, QStringList _list)"""
        return None
    def removeDuplicates():
        """int QStringList.removeDuplicates()"""
        return int()
    def lastIndexOf(_value, _from):
        """int QStringList.lastIndexOf(QString _value, int _from)"""
        return int()
    def lastIndexOf(_rx, _from):
        """int QStringList.lastIndexOf(QRegExp _rx, int _from)"""
        return int()
    def indexOf(_value, _from):
        """int QStringList.indexOf(QString _value, int _from)"""
        return int()
    def indexOf(_rx, _from):
        """int QStringList.indexOf(QRegExp _rx, int _from)"""
        return int()
    def replaceInStrings(_before, _after, _cs):
        """QStringList QStringList.replaceInStrings(QString _before, QString _after, Qt.CaseSensitivity _cs)"""
        return QStringList()
    def replaceInStrings(_rx, _after):
        """QStringList QStringList.replaceInStrings(QRegExp _rx, QString _after)"""
        return QStringList()
    def contains(_str, _cs):
        """bool QStringList.contains(QString _str, Qt.CaseSensitivity _cs)"""
        return bool()
    def filter(_str, _cs):
        """QStringList QStringList.filter(QString _str, Qt.CaseSensitivity _cs)"""
        return QStringList()
    def filter(_rx):
        """QStringList QStringList.filter(QRegExp _rx)"""
        return QStringList()
    def join(_sep):
        """QString QStringList.join(QString _sep)"""
        return QString()
    def sort():
        """None QStringList.sort()"""
        return None
    def __lshift__(_str):
        """QStringList QStringList.__lshift__(QString _str)"""
        return QStringList()
    def __lshift__(_l):
        """QStringList QStringList.__lshift__(QStringList _l)"""
        return QStringList()


class QStringMatcher():
    """"""
    def __init__():
        """None QStringMatcher.__init__()"""
        return None
    def __init__(_pattern, _cs):
        """None QStringMatcher.__init__(QString _pattern, Qt.CaseSensitivity _cs)"""
        return None
    def __init__(_other):
        """None QStringMatcher.__init__(QStringMatcher _other)"""
        return None
    def caseSensitivity():
        """Qt.CaseSensitivity QStringMatcher.caseSensitivity()"""
        return Qt.CaseSensitivity()
    def pattern():
        """QString QStringMatcher.pattern()"""
        return QString()
    def indexIn(_str, _from):
        """int QStringMatcher.indexIn(QString _str, int _from)"""
        return int()
    def setCaseSensitivity(_cs):
        """None QStringMatcher.setCaseSensitivity(Qt.CaseSensitivity _cs)"""
        return None
    def setPattern(_pattern):
        """None QStringMatcher.setPattern(QString _pattern)"""
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

    def __init__(_key, _initialValue, _mode):
        """None QSystemSemaphore.__init__(QString _key, int _initialValue, QSystemSemaphore.AccessMode _mode)"""
        return None
    def errorString():
        """QString QSystemSemaphore.errorString()"""
        return QString()
    def error():
        """QSystemSemaphore.SystemSemaphoreError QSystemSemaphore.error()"""
        return QSystemSemaphore.SystemSemaphoreError()
    def release(_n):
        """bool QSystemSemaphore.release(int _n)"""
        return bool()
    def acquire():
        """bool QSystemSemaphore.acquire()"""
        return bool()
    def key():
        """QString QSystemSemaphore.key()"""
        return QString()
    def setKey(_key, _initialValue, _mode):
        """None QSystemSemaphore.setKey(QString _key, int _initialValue, QSystemSemaphore.AccessMode _mode)"""
        return None


class QTemporaryFile(QFile):
    """"""
    def __init__():
        """None QTemporaryFile.__init__()"""
        return None
    def __init__(_templateName):
        """None QTemporaryFile.__init__(QString _templateName)"""
        return None
    def __init__(_parent):
        """None QTemporaryFile.__init__(QObject _parent)"""
        return None
    def __init__(_templateName, _parent):
        """None QTemporaryFile.__init__(QString _templateName, QObject _parent)"""
        return None
    def fileEngine():
        """QAbstractFileEngine QTemporaryFile.fileEngine()"""
        return QAbstractFileEngine()
    def createLocalFile(_fileName):
        """QTemporaryFile QTemporaryFile.createLocalFile(QString _fileName)"""
        return QTemporaryFile()
    def createLocalFile(_file):
        """QTemporaryFile QTemporaryFile.createLocalFile(QFile _file)"""
        return QTemporaryFile()
    def setFileTemplate(_name):
        """None QTemporaryFile.setFileTemplate(QString _name)"""
        return None
    def fileTemplate():
        """QString QTemporaryFile.fileTemplate()"""
        return QString()
    def fileName():
        """QString QTemporaryFile.fileName()"""
        return QString()
    def open():
        """bool QTemporaryFile.open()"""
        return bool()
    def open(_flags):
        """bool QTemporaryFile.open(QIODevice.OpenMode _flags)"""
        return bool()
    def setAutoRemove(_b):
        """None QTemporaryFile.setAutoRemove(bool _b)"""
        return None
    def autoRemove():
        """bool QTemporaryFile.autoRemove()"""
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

    def __init__():
        """None QTextBoundaryFinder.__init__()"""
        return None
    def __init__(_other):
        """None QTextBoundaryFinder.__init__(QTextBoundaryFinder _other)"""
        return None
    def __init__(_type, _string):
        """None QTextBoundaryFinder.__init__(QTextBoundaryFinder.BoundaryType _type, QString _string)"""
        return None
    def boundaryReasons():
        """QTextBoundaryFinder.BoundaryReasons QTextBoundaryFinder.boundaryReasons()"""
        return QTextBoundaryFinder.BoundaryReasons()
    def isAtBoundary():
        """bool QTextBoundaryFinder.isAtBoundary()"""
        return bool()
    def toPreviousBoundary():
        """int QTextBoundaryFinder.toPreviousBoundary()"""
        return int()
    def toNextBoundary():
        """int QTextBoundaryFinder.toNextBoundary()"""
        return int()
    def setPosition(_position):
        """None QTextBoundaryFinder.setPosition(int _position)"""
        return None
    def position():
        """int QTextBoundaryFinder.position()"""
        return int()
    def toEnd():
        """None QTextBoundaryFinder.toEnd()"""
        return None
    def toStart():
        """None QTextBoundaryFinder.toStart()"""
        return None
    def string():
        """QString QTextBoundaryFinder.string()"""
        return QString()
    def type():
        """QTextBoundaryFinder.BoundaryType QTextBoundaryFinder.type()"""
        return QTextBoundaryFinder.BoundaryType()
    def isValid():
        """bool QTextBoundaryFinder.isValid()"""
        return bool()


class QTextCodec():
    """"""
    DefaultConversion = int() # QTextCodec.ConversionFlag enum
    ConvertInvalidToNull = int() # QTextCodec.ConversionFlag enum
    IgnoreHeader = int() # QTextCodec.ConversionFlag enum

    def __init__():
        """None QTextCodec.__init__()"""
        return None
    def setCodecForCStrings(_c):
        """None QTextCodec.setCodecForCStrings(QTextCodec _c)"""
        return None
    def codecForCStrings():
        """QTextCodec QTextCodec.codecForCStrings()"""
        return QTextCodec()
    def setCodecForTr(_c):
        """None QTextCodec.setCodecForTr(QTextCodec _c)"""
        return None
    def codecForTr():
        """QTextCodec QTextCodec.codecForTr()"""
        return QTextCodec()
    def convertToUnicode(_in, _state):
        """abstract QString QTextCodec.convertToUnicode(str _in, QTextCodec.ConverterState _state)"""
        return QString()
    def mibEnum():
        """abstract int QTextCodec.mibEnum()"""
        return int()
    def aliases():
        """list-of-QByteArray QTextCodec.aliases()"""
        return [QByteArray()]
    def name():
        """abstract QByteArray QTextCodec.name()"""
        return QByteArray()
    def fromUnicode(_uc):
        """QByteArray QTextCodec.fromUnicode(QString _uc)"""
        return QByteArray()
    def toUnicode():
        """QByteArray QTextCodec.toUnicode()"""
        return QByteArray()
    def toUnicode(_chars):
        """QString QTextCodec.toUnicode(str _chars)"""
        return QString()
    def toUnicode(_in, _state):
        """QString QTextCodec.toUnicode(str _in, QTextCodec.ConverterState _state)"""
        return QString()
    def canEncode():
        """QString QTextCodec.canEncode()"""
        return QString()
    def makeEncoder():
        """QTextEncoder QTextCodec.makeEncoder()"""
        return QTextEncoder()
    def makeEncoder(_flags):
        """QTextEncoder QTextCodec.makeEncoder(QTextCodec.ConversionFlags _flags)"""
        return QTextEncoder()
    def makeDecoder():
        """QTextDecoder QTextCodec.makeDecoder()"""
        return QTextDecoder()
    def makeDecoder(_flags):
        """QTextDecoder QTextCodec.makeDecoder(QTextCodec.ConversionFlags _flags)"""
        return QTextDecoder()
    def setCodecForLocale(_c):
        """None QTextCodec.setCodecForLocale(QTextCodec _c)"""
        return None
    def codecForLocale():
        """QTextCodec QTextCodec.codecForLocale()"""
        return QTextCodec()
    def availableMibs():
        """list-of-int QTextCodec.availableMibs()"""
        return [int()]
    def availableCodecs():
        """list-of-QByteArray QTextCodec.availableCodecs()"""
        return [QByteArray()]
    def codecForUtfText(_ba):
        """QTextCodec QTextCodec.codecForUtfText(QByteArray _ba)"""
        return QTextCodec()
    def codecForUtfText(_ba, _defaultCodec):
        """QTextCodec QTextCodec.codecForUtfText(QByteArray _ba, QTextCodec _defaultCodec)"""
        return QTextCodec()
    def codecForHtml(_ba):
        """QTextCodec QTextCodec.codecForHtml(QByteArray _ba)"""
        return QTextCodec()
    def codecForHtml(_ba, _defaultCodec):
        """QTextCodec QTextCodec.codecForHtml(QByteArray _ba, QTextCodec _defaultCodec)"""
        return QTextCodec()
    def codecForMib(_mib):
        """QTextCodec QTextCodec.codecForMib(int _mib)"""
        return QTextCodec()
    def codecForName(_name):
        """QTextCodec QTextCodec.codecForName(QByteArray _name)"""
        return QTextCodec()
    def codecForName(_name):
        """QTextCodec QTextCodec.codecForName(str _name)"""
        return QTextCodec()


class QTextEncoder():
    """"""
    def __init__(_codec):
        """None QTextEncoder.__init__(QTextCodec _codec)"""
        return None
    def __init__(_codec, _flags):
        """None QTextEncoder.__init__(QTextCodec _codec, QTextCodec.ConversionFlags _flags)"""
        return None
    def fromUnicode(_str):
        """QByteArray QTextEncoder.fromUnicode(QString _str)"""
        return QByteArray()


class QTextDecoder():
    """"""
    def __init__(_codec):
        """None QTextDecoder.__init__(QTextCodec _codec)"""
        return None
    def __init__(_codec, _flags):
        """None QTextDecoder.__init__(QTextCodec _codec, QTextCodec.ConversionFlags _flags)"""
        return None
    def toUnicode(_chars):
        """QString QTextDecoder.toUnicode(str _chars)"""
        return QString()
    def toUnicode(_target, _chars):
        """None QTextDecoder.toUnicode(QString _target, str _chars)"""
        return None
    def toUnicode(_ba):
        """QString QTextDecoder.toUnicode(QByteArray _ba)"""
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

    def __init__():
        """None QTextStream.__init__()"""
        return None
    def __init__(_device):
        """None QTextStream.__init__(QIODevice _device)"""
        return None
    def __init__(_string, _mode):
        """None QTextStream.__init__(QString _string, QIODevice.OpenMode _mode)"""
        return None
    def __init__(_array, _mode):
        """None QTextStream.__init__(QByteArray _array, QIODevice.OpenMode _mode)"""
        return None
    def locale():
        """QLocale QTextStream.locale()"""
        return QLocale()
    def setLocale(_locale):
        """None QTextStream.setLocale(QLocale _locale)"""
        return None
    def __lshift__(_f):
        """QTextStream QTextStream.__lshift__(float _f)"""
        return QTextStream()
    def __lshift__(_b):
        """QTextStream QTextStream.__lshift__(bool _b)"""
        return QTextStream()
    def __lshift__(_i):
        """QTextStream QTextStream.__lshift__(int _i)"""
        return QTextStream()
    def __lshift__(_i):
        """QTextStream QTextStream.__lshift__(int _i)"""
        return QTextStream()
    def __lshift__(_i):
        """QTextStream QTextStream.__lshift__(int _i)"""
        return QTextStream()
    def __lshift__(_s):
        """QTextStream QTextStream.__lshift__(QString _s)"""
        return QTextStream()
    def __lshift__(_array):
        """QTextStream QTextStream.__lshift__(QByteArray _array)"""
        return QTextStream()
    def __lshift__(_m):
        """QTextStream QTextStream.__lshift__(QTextStreamManipulator _m)"""
        return QTextStream()
    def __rshift__(_ch):
        """QTextStream QTextStream.__rshift__(QChar _ch)"""
        return QTextStream()
    def __rshift__(_s):
        """QTextStream QTextStream.__rshift__(QString _s)"""
        return QTextStream()
    def __rshift__(_array):
        """QTextStream QTextStream.__rshift__(QByteArray _array)"""
        return QTextStream()
    def pos():
        """int QTextStream.pos()"""
        return int()
    def resetStatus():
        """None QTextStream.resetStatus()"""
        return None
    def setStatus(_status):
        """None QTextStream.setStatus(QTextStream.Status _status)"""
        return None
    def status():
        """QTextStream.Status QTextStream.status()"""
        return QTextStream.Status()
    def realNumberPrecision():
        """int QTextStream.realNumberPrecision()"""
        return int()
    def setRealNumberPrecision(_precision):
        """None QTextStream.setRealNumberPrecision(int _precision)"""
        return None
    def realNumberNotation():
        """QTextStream.RealNumberNotation QTextStream.realNumberNotation()"""
        return QTextStream.RealNumberNotation()
    def setRealNumberNotation(_notation):
        """None QTextStream.setRealNumberNotation(QTextStream.RealNumberNotation _notation)"""
        return None
    def integerBase():
        """int QTextStream.integerBase()"""
        return int()
    def setIntegerBase(_base):
        """None QTextStream.setIntegerBase(int _base)"""
        return None
    def numberFlags():
        """QTextStream.NumberFlags QTextStream.numberFlags()"""
        return QTextStream.NumberFlags()
    def setNumberFlags(_flags):
        """None QTextStream.setNumberFlags(QTextStream.NumberFlags _flags)"""
        return None
    def fieldWidth():
        """int QTextStream.fieldWidth()"""
        return int()
    def setFieldWidth(_width):
        """None QTextStream.setFieldWidth(int _width)"""
        return None
    def padChar():
        """QChar QTextStream.padChar()"""
        return QChar()
    def setPadChar(_ch):
        """None QTextStream.setPadChar(QChar _ch)"""
        return None
    def fieldAlignment():
        """QTextStream.FieldAlignment QTextStream.fieldAlignment()"""
        return QTextStream.FieldAlignment()
    def setFieldAlignment(_alignment):
        """None QTextStream.setFieldAlignment(QTextStream.FieldAlignment _alignment)"""
        return None
    def readAll():
        """QString QTextStream.readAll()"""
        return QString()
    def readLine(_maxLength):
        """QString QTextStream.readLine(int _maxLength)"""
        return QString()
    def read(_maxlen):
        """QString QTextStream.read(int _maxlen)"""
        return QString()
    def skipWhiteSpace():
        """None QTextStream.skipWhiteSpace()"""
        return None
    def seek(_pos):
        """bool QTextStream.seek(int _pos)"""
        return bool()
    def flush():
        """None QTextStream.flush()"""
        return None
    def reset():
        """None QTextStream.reset()"""
        return None
    def atEnd():
        """bool QTextStream.atEnd()"""
        return bool()
    def string():
        """QString QTextStream.string()"""
        return QString()
    def setString(_string, _mode):
        """None QTextStream.setString(QString _string, QIODevice.OpenMode _mode)"""
        return None
    def device():
        """QIODevice QTextStream.device()"""
        return QIODevice()
    def setDevice(_device):
        """None QTextStream.setDevice(QIODevice _device)"""
        return None
    def generateByteOrderMark():
        """bool QTextStream.generateByteOrderMark()"""
        return bool()
    def setGenerateByteOrderMark(_generate):
        """None QTextStream.setGenerateByteOrderMark(bool _generate)"""
        return None
    def autoDetectUnicode():
        """bool QTextStream.autoDetectUnicode()"""
        return bool()
    def setAutoDetectUnicode(_enabled):
        """None QTextStream.setAutoDetectUnicode(bool _enabled)"""
        return None
    def codec():
        """QTextCodec QTextStream.codec()"""
        return QTextCodec()
    def setCodec(_codec):
        """None QTextStream.setCodec(QTextCodec _codec)"""
        return None
    def setCodec(_codecName):
        """None QTextStream.setCodec(str _codecName)"""
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

    def __init__(_parent):
        """None QThread.__init__(QObject _parent)"""
        return None
    def usleep():
        """int QThread.usleep()"""
        return int()
    def msleep():
        """int QThread.msleep()"""
        return int()
    def sleep():
        """int QThread.sleep()"""
        return int()
    def setTerminationEnabled(_enabled):
        """None QThread.setTerminationEnabled(bool _enabled)"""
        return None
    def exec_():
        """int QThread.exec_()"""
        return int()
    def run():
        """None QThread.run()"""
        return None
    def wait(_msecs):
        """bool QThread.wait(int _msecs)"""
        return bool()
    def quit():
        """None QThread.quit()"""
        return None
    def terminate():
        """None QThread.terminate()"""
        return None
    def start(_priority):
        """None QThread.start(QThread.Priority _priority)"""
        return None
    def exit(_returnCode):
        """None QThread.exit(int _returnCode)"""
        return None
    def stackSize():
        """int QThread.stackSize()"""
        return int()
    def setStackSize(_stackSize):
        """None QThread.setStackSize(int _stackSize)"""
        return None
    def priority():
        """QThread.Priority QThread.priority()"""
        return QThread.Priority()
    def setPriority(_priority):
        """None QThread.setPriority(QThread.Priority _priority)"""
        return None
    def isRunning():
        """bool QThread.isRunning()"""
        return bool()
    def isFinished():
        """bool QThread.isFinished()"""
        return bool()
    def yieldCurrentThread():
        """None QThread.yieldCurrentThread()"""
        return None
    def idealThreadCount():
        """int QThread.idealThreadCount()"""
        return int()
    def currentThreadId():
        """int QThread.currentThreadId()"""
        return int()
    def currentThread():
        """QThread QThread.currentThread()"""
        return QThread()


class QThreadPool(QObject):
    """"""
    def __init__(_parent):
        """None QThreadPool.__init__(QObject _parent)"""
        return None
    def waitForDone():
        """None QThreadPool.waitForDone()"""
        return None
    def releaseThread():
        """None QThreadPool.releaseThread()"""
        return None
    def reserveThread():
        """None QThreadPool.reserveThread()"""
        return None
    def activeThreadCount():
        """int QThreadPool.activeThreadCount()"""
        return int()
    def setMaxThreadCount(_maxThreadCount):
        """None QThreadPool.setMaxThreadCount(int _maxThreadCount)"""
        return None
    def maxThreadCount():
        """int QThreadPool.maxThreadCount()"""
        return int()
    def setExpiryTimeout(_expiryTimeout):
        """None QThreadPool.setExpiryTimeout(int _expiryTimeout)"""
        return None
    def expiryTimeout():
        """int QThreadPool.expiryTimeout()"""
        return int()
    def tryStart(_runnable):
        """bool QThreadPool.tryStart(QRunnable _runnable)"""
        return bool()
    def start(_runnable, _priority):
        """None QThreadPool.start(QRunnable _runnable, int _priority)"""
        return None
    def globalInstance():
        """QThreadPool QThreadPool.globalInstance()"""
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

    def __init__(_duration, _parent):
        """None QTimeLine.__init__(int _duration, QObject _parent)"""
        return None
    def setEasingCurve(_curve):
        """None QTimeLine.setEasingCurve(QEasingCurve _curve)"""
        return None
    def easingCurve():
        """QEasingCurve QTimeLine.easingCurve()"""
        return QEasingCurve()
    def timerEvent(_event):
        """None QTimeLine.timerEvent(QTimerEvent _event)"""
        return None
    def toggleDirection():
        """None QTimeLine.toggleDirection()"""
        return None
    def stop():
        """None QTimeLine.stop()"""
        return None
    def start():
        """None QTimeLine.start()"""
        return None
    def setPaused(_paused):
        """None QTimeLine.setPaused(bool _paused)"""
        return None
    def setCurrentTime(_msec):
        """None QTimeLine.setCurrentTime(int _msec)"""
        return None
    def resume():
        """None QTimeLine.resume()"""
        return None
    def valueForTime(_msec):
        """float QTimeLine.valueForTime(int _msec)"""
        return float()
    def frameForTime(_msec):
        """int QTimeLine.frameForTime(int _msec)"""
        return int()
    def currentValue():
        """float QTimeLine.currentValue()"""
        return float()
    def currentFrame():
        """int QTimeLine.currentFrame()"""
        return int()
    def currentTime():
        """int QTimeLine.currentTime()"""
        return int()
    def setCurveShape(_shape):
        """None QTimeLine.setCurveShape(QTimeLine.CurveShape _shape)"""
        return None
    def curveShape():
        """QTimeLine.CurveShape QTimeLine.curveShape()"""
        return QTimeLine.CurveShape()
    def setUpdateInterval(_interval):
        """None QTimeLine.setUpdateInterval(int _interval)"""
        return None
    def updateInterval():
        """int QTimeLine.updateInterval()"""
        return int()
    def setFrameRange(_startFrame, _endFrame):
        """None QTimeLine.setFrameRange(int _startFrame, int _endFrame)"""
        return None
    def setEndFrame(_frame):
        """None QTimeLine.setEndFrame(int _frame)"""
        return None
    def endFrame():
        """int QTimeLine.endFrame()"""
        return int()
    def setStartFrame(_frame):
        """None QTimeLine.setStartFrame(int _frame)"""
        return None
    def startFrame():
        """int QTimeLine.startFrame()"""
        return int()
    def setDuration(_duration):
        """None QTimeLine.setDuration(int _duration)"""
        return None
    def duration():
        """int QTimeLine.duration()"""
        return int()
    def setDirection(_direction):
        """None QTimeLine.setDirection(QTimeLine.Direction _direction)"""
        return None
    def direction():
        """QTimeLine.Direction QTimeLine.direction()"""
        return QTimeLine.Direction()
    def setLoopCount(_count):
        """None QTimeLine.setLoopCount(int _count)"""
        return None
    def loopCount():
        """int QTimeLine.loopCount()"""
        return int()
    def state():
        """QTimeLine.State QTimeLine.state()"""
        return QTimeLine.State()


class QTimer(QObject):
    """"""
    def __init__(_parent):
        """None QTimer.__init__(QObject _parent)"""
        return None
    def timerEvent():
        """QTimerEvent QTimer.timerEvent()"""
        return QTimerEvent()
    def stop():
        """None QTimer.stop()"""
        return None
    def start(_msec):
        """None QTimer.start(int _msec)"""
        return None
    def start():
        """None QTimer.start()"""
        return None
    def singleShot(_msec, _receiver, _member):
        """None QTimer.singleShot(int _msec, QObject _receiver, SLOT()SLOT() _member)"""
        return None
    def singleShot(_msec, _receiver):
        """None QTimer.singleShot(int _msec, callable _receiver)"""
        return None
    def setSingleShot(_asingleShot):
        """None QTimer.setSingleShot(bool _asingleShot)"""
        return None
    def isSingleShot():
        """bool QTimer.isSingleShot()"""
        return bool()
    def interval():
        """int QTimer.interval()"""
        return int()
    def setInterval(_msec):
        """None QTimer.setInterval(int _msec)"""
        return None
    def timerId():
        """int QTimer.timerId()"""
        return int()
    def isActive():
        """bool QTimer.isActive()"""
        return bool()


class QTranslator(QObject):
    """"""
    def __init__(_parent):
        """None QTranslator.__init__(QObject _parent)"""
        return None
    def loadFromData(_data):
        """bool QTranslator.loadFromData(str _data)"""
        return bool()
    def load(_fileName, _directory, _searchDelimiters, _suffix):
        """bool QTranslator.load(QString _fileName, QString _directory, QString _searchDelimiters, QString _suffix)"""
        return bool()
    def isEmpty():
        """bool QTranslator.isEmpty()"""
        return bool()
    def translate(_context, _sourceText, _disambiguation):
        """QString QTranslator.translate(str _context, str _sourceText, str _disambiguation)"""
        return QString()
    def translate(_context, _sourceText, _comment, _n):
        """QString QTranslator.translate(str _context, str _sourceText, str _comment, int _n)"""
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

    def __init__():
        """None QUrl.__init__()"""
        return None
    def __init__(_url):
        """None QUrl.__init__(QString _url)"""
        return None
    def __init__(_copy):
        """None QUrl.__init__(QUrl _copy)"""
        return None
    def __init__(_url, _mode):
        """None QUrl.__init__(QString _url, QUrl.ParsingMode _mode)"""
        return None
    def __ge__(_url):
        """bool QUrl.__ge__(QUrl _url)"""
        return bool()
    def fromUserInput(_userInput):
        """QUrl QUrl.fromUserInput(QString _userInput)"""
        return QUrl()
    def encodedFragment():
        """QByteArray QUrl.encodedFragment()"""
        return QByteArray()
    def setEncodedFragment(_fragment):
        """None QUrl.setEncodedFragment(QByteArray _fragment)"""
        return None
    def removeAllEncodedQueryItems(_key):
        """None QUrl.removeAllEncodedQueryItems(QByteArray _key)"""
        return None
    def removeEncodedQueryItem(_key):
        """None QUrl.removeEncodedQueryItem(QByteArray _key)"""
        return None
    def allEncodedQueryItemValues(_key):
        """list-of-QByteArray QUrl.allEncodedQueryItemValues(QByteArray _key)"""
        return [QByteArray()]
    def encodedQueryItemValue(_key):
        """QByteArray QUrl.encodedQueryItemValue(QByteArray _key)"""
        return QByteArray()
    def hasEncodedQueryItem(_key):
        """bool QUrl.hasEncodedQueryItem(QByteArray _key)"""
        return bool()
    def encodedQueryItems():
        """list-of-tuple-of-QByteArray-QByteArray QUrl.encodedQueryItems()"""
        return [tuple-of-QByteArray-QByteArray()]
    def addEncodedQueryItem(_key, _value):
        """None QUrl.addEncodedQueryItem(QByteArray _key, QByteArray _value)"""
        return None
    def setEncodedQueryItems(_query):
        """None QUrl.setEncodedQueryItems(list-of-tuple-of-QByteArray-QByteArray _query)"""
        return None
    def encodedPath():
        """QByteArray QUrl.encodedPath()"""
        return QByteArray()
    def setEncodedPath(_path):
        """None QUrl.setEncodedPath(QByteArray _path)"""
        return None
    def encodedHost():
        """QByteArray QUrl.encodedHost()"""
        return QByteArray()
    def setEncodedHost(_host):
        """None QUrl.setEncodedHost(QByteArray _host)"""
        return None
    def encodedPassword():
        """QByteArray QUrl.encodedPassword()"""
        return QByteArray()
    def setEncodedPassword(_password):
        """None QUrl.setEncodedPassword(QByteArray _password)"""
        return None
    def encodedUserName():
        """QByteArray QUrl.encodedUserName()"""
        return QByteArray()
    def setEncodedUserName(_userName):
        """None QUrl.setEncodedUserName(QByteArray _userName)"""
        return None
    def setIdnWhitelist():
        """QStringList QUrl.setIdnWhitelist()"""
        return QStringList()
    def idnWhitelist():
        """QStringList QUrl.idnWhitelist()"""
        return QStringList()
    def toAce():
        """QString QUrl.toAce()"""
        return QString()
    def fromAce():
        """QByteArray QUrl.fromAce()"""
        return QByteArray()
    def errorString():
        """QString QUrl.errorString()"""
        return QString()
    def hasFragment():
        """bool QUrl.hasFragment()"""
        return bool()
    def hasQuery():
        """bool QUrl.hasQuery()"""
        return bool()
    def toPunycode():
        """QString QUrl.toPunycode()"""
        return QString()
    def fromPunycode():
        """QByteArray QUrl.fromPunycode()"""
        return QByteArray()
    def toPercentEncoding(_input, _exclude, _include):
        """QByteArray QUrl.toPercentEncoding(QString _input, QByteArray _exclude, QByteArray _include)"""
        return QByteArray()
    def fromPercentEncoding():
        """QByteArray QUrl.fromPercentEncoding()"""
        return QByteArray()
    def __ne__(_url):
        """bool QUrl.__ne__(QUrl _url)"""
        return bool()
    def __eq__(_url):
        """bool QUrl.__eq__(QUrl _url)"""
        return bool()
    def __lt__(_url):
        """bool QUrl.__lt__(QUrl _url)"""
        return bool()
    def isDetached():
        """bool QUrl.isDetached()"""
        return bool()
    def detach():
        """None QUrl.detach()"""
        return None
    def fromEncoded(_url):
        """QUrl QUrl.fromEncoded(QByteArray _url)"""
        return QUrl()
    def fromEncoded(_url, _mode):
        """QUrl QUrl.fromEncoded(QByteArray _url, QUrl.ParsingMode _mode)"""
        return QUrl()
    def toEncoded(_options):
        """QByteArray QUrl.toEncoded(QUrl.FormattingOptions _options)"""
        return QByteArray()
    def toString(_options):
        """QString QUrl.toString(QUrl.FormattingOptions _options)"""
        return QString()
    def toLocalFile():
        """QString QUrl.toLocalFile()"""
        return QString()
    def fromLocalFile(_localfile):
        """QUrl QUrl.fromLocalFile(QString _localfile)"""
        return QUrl()
    def isParentOf(_url):
        """bool QUrl.isParentOf(QUrl _url)"""
        return bool()
    def isRelative():
        """bool QUrl.isRelative()"""
        return bool()
    def resolved(_relative):
        """QUrl QUrl.resolved(QUrl _relative)"""
        return QUrl()
    def fragment():
        """QString QUrl.fragment()"""
        return QString()
    def setFragment(_fragment):
        """None QUrl.setFragment(QString _fragment)"""
        return None
    def removeAllQueryItems(_key):
        """None QUrl.removeAllQueryItems(QString _key)"""
        return None
    def removeQueryItem(_key):
        """None QUrl.removeQueryItem(QString _key)"""
        return None
    def allQueryItemValues(_key):
        """QStringList QUrl.allQueryItemValues(QString _key)"""
        return QStringList()
    def queryItemValue(_key):
        """QString QUrl.queryItemValue(QString _key)"""
        return QString()
    def hasQueryItem(_key):
        """bool QUrl.hasQueryItem(QString _key)"""
        return bool()
    def queryItems():
        """list-of-tuple-of-QString-QString QUrl.queryItems()"""
        return [tuple-of-QString-QString()]
    def addQueryItem(_key, _value):
        """None QUrl.addQueryItem(QString _key, QString _value)"""
        return None
    def setQueryItems(_query):
        """None QUrl.setQueryItems(list-of-tuple-of-QString-QString _query)"""
        return None
    def queryPairDelimiter():
        """str QUrl.queryPairDelimiter()"""
        return str()
    def queryValueDelimiter():
        """str QUrl.queryValueDelimiter()"""
        return str()
    def setQueryDelimiters(_valueDelimiter, _pairDelimiter):
        """None QUrl.setQueryDelimiters(str _valueDelimiter, str _pairDelimiter)"""
        return None
    def encodedQuery():
        """QByteArray QUrl.encodedQuery()"""
        return QByteArray()
    def setEncodedQuery(_query):
        """None QUrl.setEncodedQuery(QByteArray _query)"""
        return None
    def path():
        """QString QUrl.path()"""
        return QString()
    def setPath(_path):
        """None QUrl.setPath(QString _path)"""
        return None
    def port():
        """int QUrl.port()"""
        return int()
    def port(_defaultPort):
        """int QUrl.port(int _defaultPort)"""
        return int()
    def setPort(_port):
        """None QUrl.setPort(int _port)"""
        return None
    def host():
        """QString QUrl.host()"""
        return QString()
    def setHost(_host):
        """None QUrl.setHost(QString _host)"""
        return None
    def password():
        """QString QUrl.password()"""
        return QString()
    def setPassword(_password):
        """None QUrl.setPassword(QString _password)"""
        return None
    def userName():
        """QString QUrl.userName()"""
        return QString()
    def setUserName(_userName):
        """None QUrl.setUserName(QString _userName)"""
        return None
    def userInfo():
        """QString QUrl.userInfo()"""
        return QString()
    def setUserInfo(_userInfo):
        """None QUrl.setUserInfo(QString _userInfo)"""
        return None
    def authority():
        """QString QUrl.authority()"""
        return QString()
    def setAuthority(_authority):
        """None QUrl.setAuthority(QString _authority)"""
        return None
    def scheme():
        """QString QUrl.scheme()"""
        return QString()
    def setScheme(_scheme):
        """None QUrl.setScheme(QString _scheme)"""
        return None
    def clear():
        """None QUrl.clear()"""
        return None
    def isEmpty():
        """bool QUrl.isEmpty()"""
        return bool()
    def isValid():
        """bool QUrl.isValid()"""
        return bool()
    def setEncodedUrl(_url):
        """None QUrl.setEncodedUrl(QByteArray _url)"""
        return None
    def setEncodedUrl(_url, _mode):
        """None QUrl.setEncodedUrl(QByteArray _url, QUrl.ParsingMode _mode)"""
        return None
    def setUrl(_url):
        """None QUrl.setUrl(QString _url)"""
        return None
    def setUrl(_url, _mode):
        """None QUrl.setUrl(QString _url, QUrl.ParsingMode _mode)"""
        return None
    def __hash__():
        """int QUrl.__hash__()"""
        return int()
    def __repr__():
        """str QUrl.__repr__()"""
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

    def __init__():
        """None QUuid.__init__()"""
        return None
    def __init__(_l, _w1, _w2, _b1, _b2, _b3, _b4, _b5, _b6, _b7, _b8):
        """None QUuid.__init__(int _l, int _w1, int _w2, str _b1, str _b2, str _b3, str _b4, str _b5, str _b6, str _b7, str _b8)"""
        return None
    def __init__():
        """QString QUuid.__init__()"""
        return QString()
    def __init__():
        """QUuid QUuid.__init__()"""
        return QUuid()
    def __ge__(_other):
        """bool QUuid.__ge__(QUuid _other)"""
        return bool()
    def __le__(_other):
        """bool QUuid.__le__(QUuid _other)"""
        return bool()
    def version():
        """QUuid.Version QUuid.version()"""
        return QUuid.Version()
    def variant():
        """QUuid.Variant QUuid.variant()"""
        return QUuid.Variant()
    def createUuid():
        """QUuid QUuid.createUuid()"""
        return QUuid()
    def __gt__(_other):
        """bool QUuid.__gt__(QUuid _other)"""
        return bool()
    def __lt__(_other):
        """bool QUuid.__lt__(QUuid _other)"""
        return bool()
    def __ne__(_orig):
        """bool QUuid.__ne__(QUuid _orig)"""
        return bool()
    def __eq__(_orig):
        """bool QUuid.__eq__(QUuid _orig)"""
        return bool()
    def isNull():
        """bool QUuid.isNull()"""
        return bool()
    def toString():
        """QString QUuid.toString()"""
        return QString()
    def __repr__():
        """str QUuid.__repr__()"""
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

    def __init__():
        """None QVariant.__init__()"""
        return None
    def __init__(_type):
        """None QVariant.__init__(Type _type)"""
        return None
    def __init__(_typeOrUserType, _copy):
        """None QVariant.__init__(int _typeOrUserType, sip.voidptr _copy)"""
        return None
    def __init__(_other):
        """None QVariant.__init__(QVariant _other)"""
        return None
    def __init__():
        """object QVariant.__init__()"""
        return object()
    def toEasingCurve():
        """QEasingCurve QVariant.toEasingCurve()"""
        return QEasingCurve()
    def toReal(_ok):
        """float QVariant.toReal(bool _ok)"""
        return float()
    def toFloat(_ok):
        """float QVariant.toFloat(bool _ok)"""
        return float()
    def __ne__(_v):
        """bool QVariant.__ne__(QVariant _v)"""
        return bool()
    def __eq__(_v):
        """bool QVariant.__eq__(QVariant _v)"""
        return bool()
    def data():
        """sip.voidptr QVariant.data()"""
        return sip.voidptr()
    def nameToType(_name):
        """Type QVariant.nameToType(str _name)"""
        return Type()
    def typeToName(_type):
        """str QVariant.typeToName(Type _type)"""
        return str()
    def save(_ds):
        """None QVariant.save(QDataStream _ds)"""
        return None
    def load(_ds):
        """None QVariant.load(QDataStream _ds)"""
        return None
    def toPyObject():
        """object QVariant.toPyObject()"""
        return object()
    def toRegExp():
        """QRegExp QVariant.toRegExp()"""
        return QRegExp()
    def toLocale():
        """QLocale QVariant.toLocale()"""
        return QLocale()
    def toUrl():
        """QUrl QVariant.toUrl()"""
        return QUrl()
    def toRectF():
        """QRectF QVariant.toRectF()"""
        return QRectF()
    def toRect():
        """QRect QVariant.toRect()"""
        return QRect()
    def toLineF():
        """QLineF QVariant.toLineF()"""
        return QLineF()
    def toLine():
        """QLine QVariant.toLine()"""
        return QLine()
    def toSizeF():
        """QSizeF QVariant.toSizeF()"""
        return QSizeF()
    def toSize():
        """QSize QVariant.toSize()"""
        return QSize()
    def toPointF():
        """QPointF QVariant.toPointF()"""
        return QPointF()
    def toPoint():
        """QPoint QVariant.toPoint()"""
        return QPoint()
    def toHash():
        """dict-of-QString-QVariant QVariant.toHash()"""
        return dict-of-QString-QVariant()
    def toMap():
        """dict-of-QString-QVariant QVariant.toMap()"""
        return dict-of-QString-QVariant()
    def toList():
        """list-of-QVariant QVariant.toList()"""
        return [QVariant()]
    def toDateTime():
        """QDateTime QVariant.toDateTime()"""
        return QDateTime()
    def toTime():
        """QTime QVariant.toTime()"""
        return QTime()
    def toDate():
        """QDate QVariant.toDate()"""
        return QDate()
    def toChar():
        """QChar QVariant.toChar()"""
        return QChar()
    def toStringList():
        """QStringList QVariant.toStringList()"""
        return QStringList()
    def toString():
        """QString QVariant.toString()"""
        return QString()
    def toBitArray():
        """QBitArray QVariant.toBitArray()"""
        return QBitArray()
    def toByteArray():
        """QByteArray QVariant.toByteArray()"""
        return QByteArray()
    def toDouble(_ok):
        """float QVariant.toDouble(bool _ok)"""
        return float()
    def toBool():
        """bool QVariant.toBool()"""
        return bool()
    def toULongLong(_ok):
        """int QVariant.toULongLong(bool _ok)"""
        return int()
    def toLongLong(_ok):
        """int QVariant.toLongLong(bool _ok)"""
        return int()
    def toUInt(_ok):
        """int QVariant.toUInt(bool _ok)"""
        return int()
    def toInt(_ok):
        """int QVariant.toInt(bool _ok)"""
        return int()
    def isDetached():
        """bool QVariant.isDetached()"""
        return bool()
    def detach():
        """None QVariant.detach()"""
        return None
    def clear():
        """None QVariant.clear()"""
        return None
    def isNull():
        """bool QVariant.isNull()"""
        return bool()
    def isValid():
        """bool QVariant.isValid()"""
        return bool()
    def convert(_t):
        """bool QVariant.convert(Type _t)"""
        return bool()
    def canConvert(_t):
        """bool QVariant.canConvert(Type _t)"""
        return bool()
    def typeName():
        """str QVariant.typeName()"""
        return str()
    def userType():
        """int QVariant.userType()"""
        return int()
    def type():
        """Type QVariant.type()"""
        return Type()
    def fromMap(_map):
        """QVariant QVariant.fromMap(dict-of-QString-QVariant _map)"""
        return QVariant()
    def fromList(_list):
        """QVariant QVariant.fromList(list-of-QVariant _list)"""
        return QVariant()


class QWaitCondition():
    """"""
    def __init__():
        """None QWaitCondition.__init__()"""
        return None
    def wakeAll():
        """None QWaitCondition.wakeAll()"""
        return None
    def wakeOne():
        """None QWaitCondition.wakeOne()"""
        return None
    def wait(_mutex, _msecs):
        """bool QWaitCondition.wait(QMutex _mutex, int _msecs)"""
        return bool()
    def wait(_readWriteLock, _msecs):
        """bool QWaitCondition.wait(QReadWriteLock _readWriteLock, int _msecs)"""
        return bool()


class QXmlStreamAttribute():
    """"""
    def __init__():
        """None QXmlStreamAttribute.__init__()"""
        return None
    def __init__(_qualifiedName, _value):
        """None QXmlStreamAttribute.__init__(QString _qualifiedName, QString _value)"""
        return None
    def __init__(_namespaceUri, _name, _value):
        """None QXmlStreamAttribute.__init__(QString _namespaceUri, QString _name, QString _value)"""
        return None
    def __init__():
        """QXmlStreamAttribute QXmlStreamAttribute.__init__()"""
        return QXmlStreamAttribute()
    def __ne__(_other):
        """bool QXmlStreamAttribute.__ne__(QXmlStreamAttribute _other)"""
        return bool()
    def __eq__(_other):
        """bool QXmlStreamAttribute.__eq__(QXmlStreamAttribute _other)"""
        return bool()
    def isDefault():
        """bool QXmlStreamAttribute.isDefault()"""
        return bool()
    def value():
        """QStringRef QXmlStreamAttribute.value()"""
        return QStringRef()
    def prefix():
        """QStringRef QXmlStreamAttribute.prefix()"""
        return QStringRef()
    def qualifiedName():
        """QStringRef QXmlStreamAttribute.qualifiedName()"""
        return QStringRef()
    def name():
        """QStringRef QXmlStreamAttribute.name()"""
        return QStringRef()
    def namespaceUri():
        """QStringRef QXmlStreamAttribute.namespaceUri()"""
        return QStringRef()


class QXmlStreamAttributes():
    """"""
    def __init__():
        """None QXmlStreamAttributes.__init__()"""
        return None
    def __init__():
        """QXmlStreamAttributes QXmlStreamAttributes.__init__()"""
        return QXmlStreamAttributes()
    def __contains__(_value):
        """int QXmlStreamAttributes.__contains__(QXmlStreamAttribute _value)"""
        return int()
    def __delitem__(_i):
        """None QXmlStreamAttributes.__delitem__(int _i)"""
        return None
    def __delitem__(_slice):
        """None QXmlStreamAttributes.__delitem__(slice _slice)"""
        return None
    def __setitem__(_i, _value):
        """None QXmlStreamAttributes.__setitem__(int _i, QXmlStreamAttribute _value)"""
        return None
    def __setitem__(_slice, _list):
        """None QXmlStreamAttributes.__setitem__(slice _slice, QXmlStreamAttributes _list)"""
        return None
    def __getitem__(_i):
        """QXmlStreamAttribute QXmlStreamAttributes.__getitem__(int _i)"""
        return QXmlStreamAttribute()
    def __getitem__(_slice):
        """QXmlStreamAttributes QXmlStreamAttributes.__getitem__(slice _slice)"""
        return QXmlStreamAttributes()
    def __eq__(_other):
        """bool QXmlStreamAttributes.__eq__(QXmlStreamAttributes _other)"""
        return bool()
    def __iadd__(_other):
        """QXmlStreamAttributes QXmlStreamAttributes.__iadd__(QXmlStreamAttributes _other)"""
        return QXmlStreamAttributes()
    def __iadd__(_value):
        """QXmlStreamAttributes QXmlStreamAttributes.__iadd__(QXmlStreamAttribute _value)"""
        return QXmlStreamAttributes()
    def __ne__(_other):
        """bool QXmlStreamAttributes.__ne__(QXmlStreamAttributes _other)"""
        return bool()
    def size():
        """int QXmlStreamAttributes.size()"""
        return int()
    def replace(_i, _value):
        """None QXmlStreamAttributes.replace(int _i, QXmlStreamAttribute _value)"""
        return None
    def remove(_i):
        """None QXmlStreamAttributes.remove(int _i)"""
        return None
    def remove(_i, _count):
        """None QXmlStreamAttributes.remove(int _i, int _count)"""
        return None
    def prepend(_value):
        """None QXmlStreamAttributes.prepend(QXmlStreamAttribute _value)"""
        return None
    def lastIndexOf(_value, _from):
        """int QXmlStreamAttributes.lastIndexOf(QXmlStreamAttribute _value, int _from)"""
        return int()
    def last():
        """QXmlStreamAttribute QXmlStreamAttributes.last()"""
        return QXmlStreamAttribute()
    def isEmpty():
        """bool QXmlStreamAttributes.isEmpty()"""
        return bool()
    def insert(_i, _value):
        """None QXmlStreamAttributes.insert(int _i, QXmlStreamAttribute _value)"""
        return None
    def indexOf(_value, _from):
        """int QXmlStreamAttributes.indexOf(QXmlStreamAttribute _value, int _from)"""
        return int()
    def first():
        """QXmlStreamAttribute QXmlStreamAttributes.first()"""
        return QXmlStreamAttribute()
    def fill(_value, _size):
        """None QXmlStreamAttributes.fill(QXmlStreamAttribute _value, int _size)"""
        return None
    def data():
        """sip.voidptr QXmlStreamAttributes.data()"""
        return sip.voidptr()
    def __len__():
        """ QXmlStreamAttributes.__len__()"""
        return ()
    def count(_value):
        """int QXmlStreamAttributes.count(QXmlStreamAttribute _value)"""
        return int()
    def count():
        """int QXmlStreamAttributes.count()"""
        return int()
    def contains(_value):
        """bool QXmlStreamAttributes.contains(QXmlStreamAttribute _value)"""
        return bool()
    def clear():
        """None QXmlStreamAttributes.clear()"""
        return None
    def at(_i):
        """QXmlStreamAttribute QXmlStreamAttributes.at(int _i)"""
        return QXmlStreamAttribute()
    def hasAttribute(_qualifiedName):
        """bool QXmlStreamAttributes.hasAttribute(QString _qualifiedName)"""
        return bool()
    def hasAttribute(_namespaceUri, _name):
        """bool QXmlStreamAttributes.hasAttribute(QString _namespaceUri, QString _name)"""
        return bool()
    def append(_namespaceUri, _name, _value):
        """None QXmlStreamAttributes.append(QString _namespaceUri, QString _name, QString _value)"""
        return None
    def append(_qualifiedName, _value):
        """None QXmlStreamAttributes.append(QString _qualifiedName, QString _value)"""
        return None
    def append(_attribute):
        """None QXmlStreamAttributes.append(QXmlStreamAttribute _attribute)"""
        return None
    def value(_namespaceUri, _name):
        """QStringRef QXmlStreamAttributes.value(QString _namespaceUri, QString _name)"""
        return QStringRef()
    def value(_qualifiedName):
        """QStringRef QXmlStreamAttributes.value(QString _qualifiedName)"""
        return QStringRef()


class QXmlStreamNamespaceDeclaration():
    """"""
    def __init__():
        """None QXmlStreamNamespaceDeclaration.__init__()"""
        return None
    def __init__():
        """QXmlStreamNamespaceDeclaration QXmlStreamNamespaceDeclaration.__init__()"""
        return QXmlStreamNamespaceDeclaration()
    def __init__(_prefix, _namespaceUri):
        """None QXmlStreamNamespaceDeclaration.__init__(QString _prefix, QString _namespaceUri)"""
        return None
    def __ne__(_other):
        """bool QXmlStreamNamespaceDeclaration.__ne__(QXmlStreamNamespaceDeclaration _other)"""
        return bool()
    def __eq__(_other):
        """bool QXmlStreamNamespaceDeclaration.__eq__(QXmlStreamNamespaceDeclaration _other)"""
        return bool()
    def namespaceUri():
        """QStringRef QXmlStreamNamespaceDeclaration.namespaceUri()"""
        return QStringRef()
    def prefix():
        """QStringRef QXmlStreamNamespaceDeclaration.prefix()"""
        return QStringRef()


class QXmlStreamNotationDeclaration():
    """"""
    def __init__():
        """None QXmlStreamNotationDeclaration.__init__()"""
        return None
    def __init__():
        """QXmlStreamNotationDeclaration QXmlStreamNotationDeclaration.__init__()"""
        return QXmlStreamNotationDeclaration()
    def __ne__(_other):
        """bool QXmlStreamNotationDeclaration.__ne__(QXmlStreamNotationDeclaration _other)"""
        return bool()
    def __eq__(_other):
        """bool QXmlStreamNotationDeclaration.__eq__(QXmlStreamNotationDeclaration _other)"""
        return bool()
    def publicId():
        """QStringRef QXmlStreamNotationDeclaration.publicId()"""
        return QStringRef()
    def systemId():
        """QStringRef QXmlStreamNotationDeclaration.systemId()"""
        return QStringRef()
    def name():
        """QStringRef QXmlStreamNotationDeclaration.name()"""
        return QStringRef()


class QXmlStreamEntityDeclaration():
    """"""
    def __init__():
        """None QXmlStreamEntityDeclaration.__init__()"""
        return None
    def __init__():
        """QXmlStreamEntityDeclaration QXmlStreamEntityDeclaration.__init__()"""
        return QXmlStreamEntityDeclaration()
    def __ne__(_other):
        """bool QXmlStreamEntityDeclaration.__ne__(QXmlStreamEntityDeclaration _other)"""
        return bool()
    def __eq__(_other):
        """bool QXmlStreamEntityDeclaration.__eq__(QXmlStreamEntityDeclaration _other)"""
        return bool()
    def value():
        """QStringRef QXmlStreamEntityDeclaration.value()"""
        return QStringRef()
    def publicId():
        """QStringRef QXmlStreamEntityDeclaration.publicId()"""
        return QStringRef()
    def systemId():
        """QStringRef QXmlStreamEntityDeclaration.systemId()"""
        return QStringRef()
    def notationName():
        """QStringRef QXmlStreamEntityDeclaration.notationName()"""
        return QStringRef()
    def name():
        """QStringRef QXmlStreamEntityDeclaration.name()"""
        return QStringRef()


class QXmlStreamEntityResolver():
    """"""
    def __init__():
        """None QXmlStreamEntityResolver.__init__()"""
        return None
    def __init__():
        """QXmlStreamEntityResolver QXmlStreamEntityResolver.__init__()"""
        return QXmlStreamEntityResolver()
    def resolveUndeclaredEntity(_name):
        """QString QXmlStreamEntityResolver.resolveUndeclaredEntity(QString _name)"""
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

    def __init__():
        """None QXmlStreamReader.__init__()"""
        return None
    def __init__(_device):
        """None QXmlStreamReader.__init__(QIODevice _device)"""
        return None
    def __init__(_data):
        """None QXmlStreamReader.__init__(QByteArray _data)"""
        return None
    def __init__(_data):
        """None QXmlStreamReader.__init__(QString _data)"""
        return None
    def skipCurrentElement():
        """None QXmlStreamReader.skipCurrentElement()"""
        return None
    def readNextStartElement():
        """bool QXmlStreamReader.readNextStartElement()"""
        return bool()
    def entityResolver():
        """QXmlStreamEntityResolver QXmlStreamReader.entityResolver()"""
        return QXmlStreamEntityResolver()
    def setEntityResolver(_resolver):
        """None QXmlStreamReader.setEntityResolver(QXmlStreamEntityResolver _resolver)"""
        return None
    def hasError():
        """bool QXmlStreamReader.hasError()"""
        return bool()
    def error():
        """QXmlStreamReader.Error QXmlStreamReader.error()"""
        return QXmlStreamReader.Error()
    def errorString():
        """QString QXmlStreamReader.errorString()"""
        return QString()
    def raiseError(_message):
        """None QXmlStreamReader.raiseError(QString _message)"""
        return None
    def dtdSystemId():
        """QStringRef QXmlStreamReader.dtdSystemId()"""
        return QStringRef()
    def dtdPublicId():
        """QStringRef QXmlStreamReader.dtdPublicId()"""
        return QStringRef()
    def dtdName():
        """QStringRef QXmlStreamReader.dtdName()"""
        return QStringRef()
    def entityDeclarations():
        """list-of-QXmlStreamEntityDeclaration QXmlStreamReader.entityDeclarations()"""
        return [QXmlStreamEntityDeclaration()]
    def notationDeclarations():
        """list-of-QXmlStreamNotationDeclaration QXmlStreamReader.notationDeclarations()"""
        return [QXmlStreamNotationDeclaration()]
    def addExtraNamespaceDeclarations(_extraNamespaceDeclaractions):
        """None QXmlStreamReader.addExtraNamespaceDeclarations(list-of-QXmlStreamNamespaceDeclaration _extraNamespaceDeclaractions)"""
        return None
    def addExtraNamespaceDeclaration(_extraNamespaceDeclaraction):
        """None QXmlStreamReader.addExtraNamespaceDeclaration(QXmlStreamNamespaceDeclaration _extraNamespaceDeclaraction)"""
        return None
    def namespaceDeclarations():
        """list-of-QXmlStreamNamespaceDeclaration QXmlStreamReader.namespaceDeclarations()"""
        return [QXmlStreamNamespaceDeclaration()]
    def text():
        """QStringRef QXmlStreamReader.text()"""
        return QStringRef()
    def processingInstructionData():
        """QStringRef QXmlStreamReader.processingInstructionData()"""
        return QStringRef()
    def processingInstructionTarget():
        """QStringRef QXmlStreamReader.processingInstructionTarget()"""
        return QStringRef()
    def prefix():
        """QStringRef QXmlStreamReader.prefix()"""
        return QStringRef()
    def qualifiedName():
        """QStringRef QXmlStreamReader.qualifiedName()"""
        return QStringRef()
    def namespaceUri():
        """QStringRef QXmlStreamReader.namespaceUri()"""
        return QStringRef()
    def name():
        """QStringRef QXmlStreamReader.name()"""
        return QStringRef()
    def readElementText():
        """QString QXmlStreamReader.readElementText()"""
        return QString()
    def readElementText(_behaviour):
        """QString QXmlStreamReader.readElementText(QXmlStreamReader.ReadElementTextBehaviour _behaviour)"""
        return QString()
    def attributes():
        """QXmlStreamAttributes QXmlStreamReader.attributes()"""
        return QXmlStreamAttributes()
    def characterOffset():
        """int QXmlStreamReader.characterOffset()"""
        return int()
    def columnNumber():
        """int QXmlStreamReader.columnNumber()"""
        return int()
    def lineNumber():
        """int QXmlStreamReader.lineNumber()"""
        return int()
    def documentEncoding():
        """QStringRef QXmlStreamReader.documentEncoding()"""
        return QStringRef()
    def documentVersion():
        """QStringRef QXmlStreamReader.documentVersion()"""
        return QStringRef()
    def isStandaloneDocument():
        """bool QXmlStreamReader.isStandaloneDocument()"""
        return bool()
    def isProcessingInstruction():
        """bool QXmlStreamReader.isProcessingInstruction()"""
        return bool()
    def isEntityReference():
        """bool QXmlStreamReader.isEntityReference()"""
        return bool()
    def isDTD():
        """bool QXmlStreamReader.isDTD()"""
        return bool()
    def isComment():
        """bool QXmlStreamReader.isComment()"""
        return bool()
    def isCDATA():
        """bool QXmlStreamReader.isCDATA()"""
        return bool()
    def isWhitespace():
        """bool QXmlStreamReader.isWhitespace()"""
        return bool()
    def isCharacters():
        """bool QXmlStreamReader.isCharacters()"""
        return bool()
    def isEndElement():
        """bool QXmlStreamReader.isEndElement()"""
        return bool()
    def isStartElement():
        """bool QXmlStreamReader.isStartElement()"""
        return bool()
    def isEndDocument():
        """bool QXmlStreamReader.isEndDocument()"""
        return bool()
    def isStartDocument():
        """bool QXmlStreamReader.isStartDocument()"""
        return bool()
    def namespaceProcessing():
        """bool QXmlStreamReader.namespaceProcessing()"""
        return bool()
    def setNamespaceProcessing():
        """bool QXmlStreamReader.setNamespaceProcessing()"""
        return bool()
    def tokenString():
        """QString QXmlStreamReader.tokenString()"""
        return QString()
    def tokenType():
        """QXmlStreamReader.TokenType QXmlStreamReader.tokenType()"""
        return QXmlStreamReader.TokenType()
    def readNext():
        """QXmlStreamReader.TokenType QXmlStreamReader.readNext()"""
        return QXmlStreamReader.TokenType()
    def atEnd():
        """bool QXmlStreamReader.atEnd()"""
        return bool()
    def clear():
        """None QXmlStreamReader.clear()"""
        return None
    def addData(_data):
        """None QXmlStreamReader.addData(QByteArray _data)"""
        return None
    def addData(_data):
        """None QXmlStreamReader.addData(QString _data)"""
        return None
    def device():
        """QIODevice QXmlStreamReader.device()"""
        return QIODevice()
    def setDevice(_device):
        """None QXmlStreamReader.setDevice(QIODevice _device)"""
        return None


class QXmlStreamWriter():
    """"""
    def __init__():
        """None QXmlStreamWriter.__init__()"""
        return None
    def __init__(_device):
        """None QXmlStreamWriter.__init__(QIODevice _device)"""
        return None
    def __init__(_array):
        """None QXmlStreamWriter.__init__(QByteArray _array)"""
        return None
    def __init__(_string):
        """None QXmlStreamWriter.__init__(QString _string)"""
        return None
    def writeCurrentToken(_reader):
        """None QXmlStreamWriter.writeCurrentToken(QXmlStreamReader _reader)"""
        return None
    def writeStartElement(_qualifiedName):
        """None QXmlStreamWriter.writeStartElement(QString _qualifiedName)"""
        return None
    def writeStartElement(_namespaceUri, _name):
        """None QXmlStreamWriter.writeStartElement(QString _namespaceUri, QString _name)"""
        return None
    def writeStartDocument():
        """None QXmlStreamWriter.writeStartDocument()"""
        return None
    def writeStartDocument(_version):
        """None QXmlStreamWriter.writeStartDocument(QString _version)"""
        return None
    def writeStartDocument(_version, _standalone):
        """None QXmlStreamWriter.writeStartDocument(QString _version, bool _standalone)"""
        return None
    def writeProcessingInstruction(_target, _data):
        """None QXmlStreamWriter.writeProcessingInstruction(QString _target, QString _data)"""
        return None
    def writeDefaultNamespace(_namespaceUri):
        """None QXmlStreamWriter.writeDefaultNamespace(QString _namespaceUri)"""
        return None
    def writeNamespace(_namespaceUri, _prefix):
        """None QXmlStreamWriter.writeNamespace(QString _namespaceUri, QString _prefix)"""
        return None
    def writeEntityReference(_name):
        """None QXmlStreamWriter.writeEntityReference(QString _name)"""
        return None
    def writeEndElement():
        """None QXmlStreamWriter.writeEndElement()"""
        return None
    def writeEndDocument():
        """None QXmlStreamWriter.writeEndDocument()"""
        return None
    def writeTextElement(_qualifiedName, _text):
        """None QXmlStreamWriter.writeTextElement(QString _qualifiedName, QString _text)"""
        return None
    def writeTextElement(_namespaceUri, _name, _text):
        """None QXmlStreamWriter.writeTextElement(QString _namespaceUri, QString _name, QString _text)"""
        return None
    def writeEmptyElement(_qualifiedName):
        """None QXmlStreamWriter.writeEmptyElement(QString _qualifiedName)"""
        return None
    def writeEmptyElement(_namespaceUri, _name):
        """None QXmlStreamWriter.writeEmptyElement(QString _namespaceUri, QString _name)"""
        return None
    def writeDTD(_dtd):
        """None QXmlStreamWriter.writeDTD(QString _dtd)"""
        return None
    def writeComment(_text):
        """None QXmlStreamWriter.writeComment(QString _text)"""
        return None
    def writeCharacters(_text):
        """None QXmlStreamWriter.writeCharacters(QString _text)"""
        return None
    def writeCDATA(_text):
        """None QXmlStreamWriter.writeCDATA(QString _text)"""
        return None
    def writeAttributes(_attributes):
        """None QXmlStreamWriter.writeAttributes(QXmlStreamAttributes _attributes)"""
        return None
    def writeAttribute(_qualifiedName, _value):
        """None QXmlStreamWriter.writeAttribute(QString _qualifiedName, QString _value)"""
        return None
    def writeAttribute(_namespaceUri, _name, _value):
        """None QXmlStreamWriter.writeAttribute(QString _namespaceUri, QString _name, QString _value)"""
        return None
    def writeAttribute(_attribute):
        """None QXmlStreamWriter.writeAttribute(QXmlStreamAttribute _attribute)"""
        return None
    def autoFormattingIndent():
        """int QXmlStreamWriter.autoFormattingIndent()"""
        return int()
    def setAutoFormattingIndent(_spaces):
        """None QXmlStreamWriter.setAutoFormattingIndent(int _spaces)"""
        return None
    def autoFormatting():
        """bool QXmlStreamWriter.autoFormatting()"""
        return bool()
    def setAutoFormatting():
        """bool QXmlStreamWriter.setAutoFormatting()"""
        return bool()
    def codec():
        """QTextCodec QXmlStreamWriter.codec()"""
        return QTextCodec()
    def setCodec(_codec):
        """None QXmlStreamWriter.setCodec(QTextCodec _codec)"""
        return None
    def setCodec(_codecName):
        """None QXmlStreamWriter.setCodec(str _codecName)"""
        return None
    def device():
        """QIODevice QXmlStreamWriter.device()"""
        return QIODevice()
    def setDevice(_device):
        """None QXmlStreamWriter.setDevice(QIODevice _device)"""
        return None


class QPyNullVariant():
    """"""
    def __init__(_type):
        """None QPyNullVariant.__init__(object _type)"""
        return None
    def isNull():
        """bool QPyNullVariant.isNull()"""
        return bool()
    def typeName():
        """str QPyNullVariant.typeName()"""
        return str()
    def userType():
        """int QPyNullVariant.userType()"""
        return int()
    def type():
        """Type QPyNullVariant.type()"""
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

