#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
""":synopsis: An interface to the curses library, providing portable terminal
handling.
:platform: Unix
"""
"""
Some curses routines  that  return  an integer, such as  :func:`getch`, return
:const:`ERR` upon failure.


"""
ERR = None
"""
Some curses routines  that  return  an integer, such as  :func:`napms`, return
:const:`OK` upon success.


"""
OK = None
"""
A string representing the current version of the module.  Also available as
:const:`__version__`.

Several constants are available to specify character cell attributes:

+------------------+-------------------------------+
| Attribute        | Meaning                       |
+==================+===============================+
| ``A_ALTCHARSET`` | Alternate character set mode. |
+------------------+-------------------------------+
| ``A_BLINK``      | Blink mode.                   |
+------------------+-------------------------------+
| ``A_BOLD``       | Bold mode.                    |
+------------------+-------------------------------+
| ``A_DIM``        | Dim mode.                     |
+------------------+-------------------------------+
| ``A_NORMAL``     | Normal attribute.             |
+------------------+-------------------------------+
| ``A_REVERSE``    | Reverse background and        |
|                  | foreground colors.            |
+------------------+-------------------------------+
| ``A_STANDOUT``   | Standout mode.                |
+------------------+-------------------------------+
| ``A_UNDERLINE``  | Underline mode.               |
+------------------+-------------------------------+

Keys are referred to by integer constants with names starting with  ``KEY_``.
The exact keycaps available are system dependent.

.. able is far too large! should it be alphabetized?

+-------------------+--------------------------------------------+
| Key constant      | Key                                        |
+===================+============================================+
| ``KEY_MIN``       | Minimum key value                          |
+-------------------+--------------------------------------------+
| ``KEY_BREAK``     | Break key (unreliable)                     |
+-------------------+--------------------------------------------+
| ``KEY_DOWN``      | Down-arrow                                 |
+-------------------+--------------------------------------------+
| ``KEY_UP``        | Up-arrow                                   |
+-------------------+--------------------------------------------+
| ``KEY_LEFT``      | Left-arrow                                 |
+-------------------+--------------------------------------------+
| ``KEY_RIGHT``     | Right-arrow                                |
+-------------------+--------------------------------------------+
| ``KEY_HOME``      | Home key (upward+left arrow)               |
+-------------------+--------------------------------------------+
| ``KEY_BACKSPACE`` | Backspace (unreliable)                     |
+-------------------+--------------------------------------------+
| ``KEY_F0``        | Function keys.  Up to 64 function keys are |
|                   | supported.                                 |
+-------------------+--------------------------------------------+
| ``KEY_Fn``        | Value of function key *n*                  |
+-------------------+--------------------------------------------+
| ``KEY_DL``        | Delete line                                |
+-------------------+--------------------------------------------+
| ``KEY_IL``        | Insert line                                |
+-------------------+--------------------------------------------+
| ``KEY_DC``        | Delete character                           |
+-------------------+--------------------------------------------+
| ``KEY_IC``        | Insert char or enter insert mode           |
+-------------------+--------------------------------------------+
| ``KEY_EIC``       | Exit insert char mode                      |
+-------------------+--------------------------------------------+
| ``KEY_CLEAR``     | Clear screen                               |
+-------------------+--------------------------------------------+
| ``KEY_EOS``       | Clear to end of screen                     |
+-------------------+--------------------------------------------+
| ``KEY_EOL``       | Clear to end of line                       |
+-------------------+--------------------------------------------+
| ``KEY_SF``        | Scroll 1 line forward                      |
+-------------------+--------------------------------------------+
| ``KEY_SR``        | Scroll 1 line backward (reverse)           |
+-------------------+--------------------------------------------+
| ``KEY_NPAGE``     | Next page                                  |
+-------------------+--------------------------------------------+
| ``KEY_PPAGE``     | Previous page                              |
+-------------------+--------------------------------------------+
| ``KEY_STAB``      | Set tab                                    |
+-------------------+--------------------------------------------+
| ``KEY_CTAB``      | Clear tab                                  |
+-------------------+--------------------------------------------+
| ``KEY_CATAB``     | Clear all tabs                             |
+-------------------+--------------------------------------------+
| ``KEY_ENTER``     | Enter or send (unreliable)                 |
+-------------------+--------------------------------------------+
| ``KEY_SRESET``    | Soft (partial) reset (unreliable)          |
+-------------------+--------------------------------------------+
| ``KEY_RESET``     | Reset or hard reset (unreliable)           |
+-------------------+--------------------------------------------+
| ``KEY_PRINT``     | Print                                      |
+-------------------+--------------------------------------------+
| ``KEY_LL``        | Home down or bottom (lower left)           |
+-------------------+--------------------------------------------+
| ``KEY_A1``        | Upper left of keypad                       |
+-------------------+--------------------------------------------+
| ``KEY_A3``        | Upper right of keypad                      |
+-------------------+--------------------------------------------+
| ``KEY_B2``        | Center of keypad                           |
+-------------------+--------------------------------------------+
| ``KEY_C1``        | Lower left of keypad                       |
+-------------------+--------------------------------------------+
| ``KEY_C3``        | Lower right of keypad                      |
+-------------------+--------------------------------------------+
| ``KEY_BTAB``      | Back tab                                   |
+-------------------+--------------------------------------------+
| ``KEY_BEG``       | Beg (beginning)                            |
+-------------------+--------------------------------------------+
| ``KEY_CANCEL``    | Cancel                                     |
+-------------------+--------------------------------------------+
| ``KEY_CLOSE``     | Close                                      |
+-------------------+--------------------------------------------+
| ``KEY_COMMAND``   | Cmd (command)                              |
+-------------------+--------------------------------------------+
| ``KEY_COPY``      | Copy                                       |
+-------------------+--------------------------------------------+
| ``KEY_CREATE``    | Create                                     |
+-------------------+--------------------------------------------+
| ``KEY_END``       | End                                        |
+-------------------+--------------------------------------------+
| ``KEY_EXIT``      | Exit                                       |
+-------------------+--------------------------------------------+
| ``KEY_FIND``      | Find                                       |
+-------------------+--------------------------------------------+
| ``KEY_HELP``      | Help                                       |
+-------------------+--------------------------------------------+
| ``KEY_MARK``      | Mark                                       |
+-------------------+--------------------------------------------+
| ``KEY_MESSAGE``   | Message                                    |
+-------------------+--------------------------------------------+
| ``KEY_MOVE``      | Move                                       |
+-------------------+--------------------------------------------+
| ``KEY_NEXT``      | Next                                       |
+-------------------+--------------------------------------------+
| ``KEY_OPEN``      | Open                                       |
+-------------------+--------------------------------------------+
| ``KEY_OPTIONS``   | Options                                    |
+-------------------+--------------------------------------------+
| ``KEY_PREVIOUS``  | Prev (previous)                            |
+-------------------+--------------------------------------------+
| ``KEY_REDO``      | Redo                                       |
+-------------------+--------------------------------------------+
| ``KEY_REFERENCE`` | Ref (reference)                            |
+-------------------+--------------------------------------------+
| ``KEY_REFRESH``   | Refresh                                    |
+-------------------+--------------------------------------------+
| ``KEY_REPLACE``   | Replace                                    |
+-------------------+--------------------------------------------+
| ``KEY_RESTART``   | Restart                                    |
+-------------------+--------------------------------------------+
| ``KEY_RESUME``    | Resume                                     |
+-------------------+--------------------------------------------+
| ``KEY_SAVE``      | Save                                       |
+-------------------+--------------------------------------------+
| ``KEY_SBEG``      | Shifted Beg (beginning)                    |
+-------------------+--------------------------------------------+
| ``KEY_SCANCEL``   | Shifted Cancel                             |
+-------------------+--------------------------------------------+
| ``KEY_SCOMMAND``  | Shifted Command                            |
+-------------------+--------------------------------------------+
| ``KEY_SCOPY``     | Shifted Copy                               |
+-------------------+--------------------------------------------+
| ``KEY_SCREATE``   | Shifted Create                             |
+-------------------+--------------------------------------------+
| ``KEY_SDC``       | Shifted Delete char                        |
+-------------------+--------------------------------------------+
| ``KEY_SDL``       | Shifted Delete line                        |
+-------------------+--------------------------------------------+
| ``KEY_SELECT``    | Select                                     |
+-------------------+--------------------------------------------+
| ``KEY_SEND``      | Shifted End                                |
+-------------------+--------------------------------------------+
| ``KEY_SEOL``      | Shifted Clear line                         |
+-------------------+--------------------------------------------+
| ``KEY_SEXIT``     | Shifted Dxit                               |
+-------------------+--------------------------------------------+
| ``KEY_SFIND``     | Shifted Find                               |
+-------------------+--------------------------------------------+
| ``KEY_SHELP``     | Shifted Help                               |
+-------------------+--------------------------------------------+
| ``KEY_SHOME``     | Shifted Home                               |
+-------------------+--------------------------------------------+
| ``KEY_SIC``       | Shifted Input                              |
+-------------------+--------------------------------------------+
| ``KEY_SLEFT``     | Shifted Left arrow                         |
+-------------------+--------------------------------------------+
| ``KEY_SMESSAGE``  | Shifted Message                            |
+-------------------+--------------------------------------------+
| ``KEY_SMOVE``     | Shifted Move                               |
+-------------------+--------------------------------------------+
| ``KEY_SNEXT``     | Shifted Next                               |
+-------------------+--------------------------------------------+
| ``KEY_SOPTIONS``  | Shifted Options                            |
+-------------------+--------------------------------------------+
| ``KEY_SPREVIOUS`` | Shifted Prev                               |
+-------------------+--------------------------------------------+
| ``KEY_SPRINT``    | Shifted Print                              |
+-------------------+--------------------------------------------+
| ``KEY_SREDO``     | Shifted Redo                               |
+-------------------+--------------------------------------------+
| ``KEY_SREPLACE``  | Shifted Replace                            |
+-------------------+--------------------------------------------+
| ``KEY_SRIGHT``    | Shifted Right arrow                        |
+-------------------+--------------------------------------------+
| ``KEY_SRSUME``    | Shifted Resume                             |
+-------------------+--------------------------------------------+
| ``KEY_SSAVE``     | Shifted Save                               |
+-------------------+--------------------------------------------+
| ``KEY_SSUSPEND``  | Shifted Suspend                            |
+-------------------+--------------------------------------------+
| ``KEY_SUNDO``     | Shifted Undo                               |
+-------------------+--------------------------------------------+
| ``KEY_SUSPEND``   | Suspend                                    |
+-------------------+--------------------------------------------+
| ``KEY_UNDO``      | Undo                                       |
+-------------------+--------------------------------------------+
| ``KEY_MOUSE``     | Mouse event has occurred                   |
+-------------------+--------------------------------------------+
| ``KEY_RESIZE``    | Terminal resize event                      |
+-------------------+--------------------------------------------+
| ``KEY_MAX``       | Maximum key value                          |
+-------------------+--------------------------------------------+

On VT100s and their software emulations, such as X terminal emulators, there are
normally at least four function keys (:const:`KEY_F1`, :const:`KEY_F2`,
:const:`KEY_F3`, :const:`KEY_F4`) available, and the arrow keys mapped to
:const:`KEY_UP`, :const:`KEY_DOWN`, :const:`KEY_LEFT` and :const:`KEY_RIGHT` in
the obvious way.  If your machine has a PC keyboard, it is safe to expect arrow
keys and twelve function keys (older PC keyboards may have only ten function
keys); also, the following keypad mappings are standard:

+------------------+-----------+
| Keycap           | Constant  |
+==================+===========+
| :kbd:`Insert`    | KEY_IC    |
+------------------+-----------+
| :kbd:`Delete`    | KEY_DC    |
+------------------+-----------+
| :kbd:`Home`      | KEY_HOME  |
+------------------+-----------+
| :kbd:`End`       | KEY_END   |
+------------------+-----------+
| :kbd:`Page Up`   | KEY_NPAGE |
+------------------+-----------+
| :kbd:`Page Down` | KEY_PPAGE |
+------------------+-----------+

The following table lists characters from the alternate character set. These are
inherited from the VT100 terminal, and will generally be  available on software
emulations such as X terminals.  When there is no graphic available, curses
falls back on a crude printable ASCII approximation.

"""
version = None
def baudrate():
	"""
	Returns the output speed of the terminal in bits per second.  On software
	terminal emulators it will have a fixed high value. Included for historical
	reasons; in former times, it was used to  write output loops for time delays and
	occasionally to change interfaces depending on the line speed.
	
	
	"""
	pass
	
def beep():
	"""
	Emit a short attention sound.
	
	
	"""
	pass
	
def can_change_color():
	"""
	Returns true or false, depending on whether the programmer can change the colors
	displayed by the terminal.
	
	
	"""
	pass
	
def cbreak():
	"""
	Enter cbreak mode.  In cbreak mode (sometimes called "rare" mode) normal tty
	line buffering is turned off and characters are available to be read one by one.
	However, unlike raw mode, special characters (interrupt, quit, suspend, and flow
	control) retain their effects on the tty driver and calling program.  Calling
	first :func:`raw` then :func:`cbreak` leaves the terminal in cbreak mode.
	
	
	"""
	pass
	
def color_content(color_number):
	"""
	Returns the intensity of the red, green, and blue (RGB) components in the color
	*color_number*, which must be between ``0`` and :const:`COLORS`.  A 3-tuple is
	returned, containing the R,G,B values for the given color, which will be between
	``0`` (no component) and ``1000`` (maximum amount of component).
	
	
	"""
	pass
	
def color_pair(color_number):
	"""
	Returns the attribute value for displaying text in the specified color.  This
	attribute value can be combined with :const:`A_STANDOUT`, :const:`A_REVERSE`,
	and the other :const:`A_\*` attributes.  :func:`pair_number` is the counterpart
	to this function.
	
	
	"""
	pass
	
def curs_set(visibility):
	"""
	Sets the cursor state.  *visibility* can be set to 0, 1, or 2, for invisible,
	normal, or very visible.  If the terminal supports the visibility requested, the
	previous cursor state is returned; otherwise, an exception is raised.  On many
	terminals, the "visible" mode is an underline cursor and the "very visible" mode
	is a block cursor.
	
	
	"""
	pass
	
def def_prog_mode():
	"""
	Saves the current terminal mode as the "program" mode, the mode when the running
	program is using curses.  (Its counterpart is the "shell" mode, for when the
	program is not in curses.)  Subsequent calls to :func:`reset_prog_mode` will
	restore this mode.
	
	
	"""
	pass
	
def def_shell_mode():
	"""
	Saves the current terminal mode as the "shell" mode, the mode when the running
	program is not using curses.  (Its counterpart is the "program" mode, when the
	program is using curses capabilities.) Subsequent calls to
	:func:`reset_shell_mode` will restore this mode.
	
	
	"""
	pass
	
def delay_output(ms):
	"""
	Inserts an *ms* millisecond pause in output.
	
	
	"""
	pass
	
def doupdate():
	"""
	Update the physical screen.  The curses library keeps two data structures, one
	representing the current physical screen contents and a virtual screen
	representing the desired next state.  The :func:`doupdate` ground updates the
	physical screen to match the virtual screen.
	
	The virtual screen may be updated by a :meth:`noutrefresh` call after write
	operations such as :meth:`addstr` have been performed on a window.  The normal
	:meth:`refresh` call is simply :meth:`noutrefresh` followed by :func:`doupdate`;
	if you have to update multiple windows, you can speed performance and perhaps
	reduce screen flicker by issuing :meth:`noutrefresh` calls on all windows,
	followed by a single :func:`doupdate`.
	
	
	"""
	pass
	
def echo():
	"""
	Enter echo mode.  In echo mode, each character input is echoed to the screen as
	it is entered.
	
	
	"""
	pass
	
def endwin():
	"""
	De-initialize the library, and return terminal to normal status.
	
	
	"""
	pass
	
def erasechar():
	"""
	Returns the user's current erase character.  Under Unix operating systems this
	is a property of the controlling tty of the curses program, and is not set by
	the curses library itself.
	
	
	"""
	pass
	
def filter():
	"""
	The :func:`.filter` routine, if used, must be called before :func:`initscr` is
	called.  The effect is that, during those calls, LINES is set to 1; the
	capabilities clear, cup, cud, cud1, cuu1, cuu, vpa are disabled; and the home
	string is set to the value of cr. The effect is that the cursor is confined to
	the current line, and so are screen updates.  This may be used for enabling
	character-at-a-time  line editing without touching the rest of the screen.
	
	
	"""
	pass
	
def flash():
	"""
	Flash the screen.  That is, change it to reverse-video and then change it back
	in a short interval.  Some people prefer such as 'visible bell' to the audible
	attention signal produced by :func:`beep`.
	
	
	"""
	pass
	
def flushinp():
	"""
	Flush all input buffers.  This throws away any  typeahead  that  has been typed
	by the user and has not yet been processed by the program.
	
	
	"""
	pass
	
def getmouse():
	"""
	After :meth:`getch` returns :const:`KEY_MOUSE` to signal a mouse event, this
	method should be call to retrieve the queued mouse event, represented as a
	5-tuple ``(id, x, y, z, bstate)``. *id* is an ID value used to distinguish
	multiple devices, and *x*, *y*, *z* are the event's coordinates.  (*z* is
	currently unused.).  *bstate* is an integer value whose bits will be set to
	indicate the type of event, and will be the bitwise OR of one or more of the
	following constants, where *n* is the button number from 1 to 4:
	:const:`BUTTONn_PRESSED`, :const:`BUTTONn_RELEASED`, :const:`BUTTONn_CLICKED`,
	:const:`BUTTONn_DOUBLE_CLICKED`, :const:`BUTTONn_TRIPLE_CLICKED`,
	:const:`BUTTON_SHIFT`, :const:`BUTTON_CTRL`, :const:`BUTTON_ALT`.
	
	
	"""
	pass
	
def getsyx():
	"""
	Returns the current coordinates of the virtual screen cursor in y and x.  If
	leaveok is currently true, then -1,-1 is returned.
	
	
	"""
	pass
	
def getwin(file):
	"""
	Reads window related data stored in the file by an earlier :func:`putwin` call.
	The routine then creates and initializes a new window using that data, returning
	the new window object.
	
	
	"""
	pass
	
def has_colors():
	"""
	Returns true if the terminal can display colors; otherwise, it returns false.
	
	
	"""
	pass
	
def has_ic():
	"""
	Returns true if the terminal has insert- and delete- character capabilities.
	This function is included for historical reasons only, as all modern software
	terminal emulators have such capabilities.
	
	
	"""
	pass
	
def has_il():
	"""
	Returns true if the terminal has insert- and delete-line  capabilities,  or  can
	simulate  them  using scrolling regions. This function is included for
	historical reasons only, as all modern software terminal emulators have such
	capabilities.
	
	
	"""
	pass
	
def has_key(ch):
	"""
	Takes a key value *ch*, and returns true if the current terminal type recognizes
	a key with that value.
	
	
	"""
	pass
	
def halfdelay(tenths):
	"""
	Used for half-delay mode, which is similar to cbreak mode in that characters
	typed by the user are immediately available to the program. However, after
	blocking for *tenths* tenths of seconds, an exception is raised if nothing has
	been typed.  The value of *tenths* must be a number between 1 and 255.  Use
	:func:`nocbreak` to leave half-delay mode.
	
	
	"""
	pass
	
def init_color(color_number,r,g,b):
	"""
	Changes the definition of a color, taking the number of the color to be changed
	followed by three RGB values (for the amounts of red, green, and blue
	components).  The value of *color_number* must be between ``0`` and
	:const:`COLORS`.  Each of *r*, *g*, *b*, must be a value between ``0`` and
	``1000``.  When :func:`init_color` is used, all occurrences of that color on the
	screen immediately change to the new definition.  This function is a no-op on
	most terminals; it is active only if :func:`can_change_color` returns ``1``.
	
	
	"""
	pass
	
def init_pair(pair_number,fg,bg):
	"""
	Changes the definition of a color-pair.  It takes three arguments: the number of
	the color-pair to be changed, the foreground color number, and the background
	color number.  The value of *pair_number* must be between ``1`` and
	``COLOR_PAIRS - 1`` (the ``0`` color pair is wired to white on black and cannot
	be changed).  The value of *fg* and *bg* arguments must be between ``0`` and
	:const:`COLORS`.  If the color-pair was previously initialized, the screen is
	refreshed and all occurrences of that color-pair are changed to the new
	definition.
	
	
	"""
	pass
	
def initscr():
	"""
	Initialize the library. Returns a :class:`WindowObject` which represents the
	whole screen.
	
	"""
	pass
	
def isendwin():
	"""
	Returns true if :func:`endwin` has been called (that is, the  curses library has
	been deinitialized).
	
	
	"""
	pass
	
def keyname(k):
	"""
	Return the name of the key numbered *k*.  The name of a key generating printable
	ASCII character is the key's character.  The name of a control-key combination
	is a two-character string consisting of a caret followed by the corresponding
	printable ASCII character.  The name of an alt-key combination (128-255) is a
	string consisting of the prefix 'M-' followed by the name of the corresponding
	ASCII character.
	
	
	"""
	pass
	
def killchar():
	"""
	Returns the user's current line kill character. Under Unix operating systems
	this is a property of the controlling tty of the curses program, and is not set
	by the curses library itself.
	
	
	"""
	pass
	
def longname():
	"""
	Returns a string containing the terminfo long name field describing the current
	terminal.  The maximum length of a verbose description is 128 characters.  It is
	defined only after the call to :func:`initscr`.
	
	
	"""
	pass
	
def meta(yes):
	"""
	If *yes* is 1, allow 8-bit characters to be input. If *yes* is 0,  allow only
	7-bit chars.
	
	
	"""
	pass
	
def mouseinterval(interval):
	"""
	Sets the maximum time in milliseconds that can elapse between press and release
	events in order for them to be recognized as a click, and returns the previous
	interval value.  The default value is 200 msec, or one fifth of a second.
	
	
	"""
	pass
	
def mousemask(mousemask):
	"""
	Sets the mouse events to be reported, and returns a tuple ``(availmask,
	oldmask)``.   *availmask* indicates which of the specified mouse events can be
	reported; on complete failure it returns 0.  *oldmask* is the previous value of
	the given window's mouse event mask.  If this function is never called, no mouse
	events are ever reported.
	
	
	"""
	pass
	
def napms(ms):
	"""
	Sleep for *ms* milliseconds.
	
	
	"""
	pass
	
def newpad(nlines,ncols):
	"""
	Creates and returns a pointer to a new pad data structure with the given number
	of lines and columns.  A pad is returned as a window object.
	
	A pad is like a window, except that it is not restricted by the screen size, and
	is not necessarily associated with a particular part of the screen.  Pads can be
	used when a large window is needed, and only a part of the window will be on the
	screen at one time.  Automatic refreshes of pads (such as from scrolling or
	echoing of input) do not occur.  The :meth:`refresh` and :meth:`noutrefresh`
	methods of a pad require 6 arguments to specify the part of the pad to be
	displayed and the location on the screen to be used for the display. The
	arguments are pminrow, pmincol, sminrow, smincol, smaxrow, smaxcol; the p
	arguments refer to the upper left corner of the pad region to be displayed and
	the s arguments define a clipping box on the screen within which the pad region
	is to be displayed.
	
	
	"""
	pass
	
def newwin(nlines,ncols,begin_y,begin_x):
	"""
	Return a new window, whose left-upper corner is at  ``(begin_y, begin_x)``, and
	whose height/width is  *nlines*/*ncols*.
	
	By default, the window will extend from the  specified position to the lower
	right corner of the screen.
	
	
	"""
	pass
	
def nl():
	"""
	Enter newline mode.  This mode translates the return key into newline on input,
	and translates newline into return and line-feed on output. Newline mode is
	initially on.
	
	
	"""
	pass
	
def nocbreak():
	"""
	Leave cbreak mode.  Return to normal "cooked" mode with line buffering.
	
	
	"""
	pass
	
def noecho():
	"""
	Leave echo mode.  Echoing of input characters is turned off.
	
	
	"""
	pass
	
def nonl():
	"""
	Leave newline mode.  Disable translation of return into newline on input, and
	disable low-level translation of newline into newline/return on output (but this
	does not change the behavior of ``addch('\n')``, which always does the
	equivalent of return and line feed on the virtual screen).  With translation
	off, curses can sometimes speed up vertical motion a little; also, it will be
	able to detect the return key on input.
	
	
	"""
	pass
	
def noqiflush():
	"""
	When the noqiflush routine is used, normal flush of input and output queues
	associated with the INTR, QUIT and SUSP characters will not be done.  You may
	want to call :func:`noqiflush` in a signal handler if you want output to
	continue as though the interrupt had not occurred, after the handler exits.
	
	
	"""
	pass
	
def noraw():
	"""
	Leave raw mode. Return to normal "cooked" mode with line buffering.
	
	
	"""
	pass
	
def pair_content(pair_number):
	"""
	Returns a tuple ``(fg, bg)`` containing the colors for the requested color pair.
	The value of *pair_number* must be between ``1`` and ``COLOR_PAIRS - 1``.
	
	
	"""
	pass
	
def pair_number(attr):
	"""
	Returns the number of the color-pair set by the attribute value *attr*.
	:func:`color_pair` is the counterpart to this function.
	
	
	"""
	pass
	
def putp(string):
	"""
	Equivalent to ``tputs(str, 1, putchar)``; emits the value of a specified
	terminfo capability for the current terminal.  Note that the output of putp
	always goes to standard output.
	
	
	"""
	pass
	
def qiflush(flag):
	"""
	If *flag* is false, the effect is the same as calling :func:`noqiflush`. If
	*flag* is true, or no argument is provided, the queues will be flushed when
	these control characters are read.
	
	
	"""
	pass
	
def raw():
	"""
	Enter raw mode.  In raw mode, normal line buffering and  processing of
	interrupt, quit, suspend, and flow control keys are turned off; characters are
	presented to curses input functions one by one.
	
	
	"""
	pass
	
def reset_prog_mode():
	"""
	Restores the  terminal  to "program" mode, as previously saved  by
	:func:`def_prog_mode`.
	
	
	"""
	pass
	
def reset_shell_mode():
	"""
	Restores the  terminal  to "shell" mode, as previously saved  by
	:func:`def_shell_mode`.
	
	
	"""
	pass
	
def setsyx(y,x):
	"""
	Sets the virtual screen cursor to *y*, *x*. If *y* and *x* are both -1, then
	leaveok is set.
	
	
	"""
	pass
	
def setupterm(termstr,fd):
	"""
	Initializes the terminal.  *termstr* is a string giving the terminal name; if
	omitted, the value of the TERM environment variable will be used.  *fd* is the
	file descriptor to which any initialization sequences will be sent; if not
	supplied, the file descriptor for ``sys.stdout`` will be used.
	
	
	"""
	pass
	
def start_color():
	"""
	Must be called if the programmer wants to use colors, and before any other color
	manipulation routine is called.  It is good practice to call this routine right
	after :func:`initscr`.
	
	:func:`start_color` initializes eight basic colors (black, red,  green, yellow,
	blue, magenta, cyan, and white), and two global variables in the :mod:`curses`
	module, :const:`COLORS` and :const:`COLOR_PAIRS`, containing the maximum number
	of colors and color-pairs the terminal can support.  It also restores the colors
	on the terminal to the values they had when the terminal was just turned on.
	
	
	"""
	pass
	
def termattrs():
	"""
	Returns a logical OR of all video attributes supported by the terminal.  This
	information is useful when a curses program needs complete control over the
	appearance of the screen.
	
	
	"""
	pass
	
def termname():
	"""
	Returns the value of the environment variable TERM, truncated to 14 characters.
	
	
	"""
	pass
	
def tigetflag(capname):
	"""
	Returns the value of the Boolean capability corresponding to the terminfo
	capability name *capname*.  The value ``-1`` is returned if *capname* is not a
	Boolean capability, or ``0`` if it is canceled or absent from the terminal
	description.
	
	
	"""
	pass
	
def tigetnum(capname):
	"""
	Returns the value of the numeric capability corresponding to the terminfo
	capability name *capname*.  The value ``-2`` is returned if *capname* is not a
	numeric capability, or ``-1`` if it is canceled or absent from the terminal
	description.
	
	
	"""
	pass
	
def tigetstr(capname):
	"""
	Returns the value of the string capability corresponding to the terminfo
	capability name *capname*.  ``None`` is returned if *capname* is not a string
	capability, or is canceled or absent from the terminal description.
	
	
	"""
	pass
	
def tparm(str,more):
	"""
	Instantiates the string *str* with the supplied parameters, where  *str* should
	be a parameterized string obtained from the terminfo  database.  E.g.
	``tparm(tigetstr("cup"), 5, 3)`` could result in  ``'\033[6;4H'``, the exact
	result depending on terminal type.
	
	
	"""
	pass
	
def typeahead(fd):
	"""
	Specifies that the file descriptor *fd* be used for typeahead checking.  If *fd*
	is ``-1``, then no typeahead checking is done.
	
	The curses library does "line-breakout optimization" by looking for typeahead
	periodically while updating the screen.  If input is found, and it is coming
	from a tty, the current update is postponed until refresh or doupdate is called
	again, allowing faster response to commands typed in advance. This function
	allows specifying a different file descriptor for typeahead checking.
	
	
	"""
	pass
	
def unctrl(ch):
	"""
	Returns a string which is a printable representation of the character *ch*.
	Control characters are displayed as a caret followed by the character, for
	example as ``^C``. Printing characters are left as they are.
	
	
	"""
	pass
	
def ungetch(ch):
	"""
	Push *ch* so the next :meth:`getch` will return it.
	
	"""
	pass
	
def ungetmouse(id,x,y,z,bstate):
	"""
	Push a :const:`KEY_MOUSE` event onto the input queue, associating the given
	state data with it.
	
	
	"""
	pass
	
def use_env(flag):
	"""
	If used, this function should be called before :func:`initscr` or newterm are
	called.  When *flag* is false, the values of lines and columns specified in the
	terminfo database will be used, even if environment variables :envvar:`LINES`
	and :envvar:`COLUMNS` (used by default) are set, or if curses is running in a
	window (in which case default behavior would be to use the window size if
	:envvar:`LINES` and :envvar:`COLUMNS` are not set).
	
	
	"""
	pass
	
def use_default_colors():
	"""
	Allow use of default values for colors on terminals supporting this feature. Use
	this to support transparency in your application.  The default color is assigned
	to the color number -1. After calling this function,  ``init_pair(x,
	curses.COLOR_RED, -1)`` initializes, for instance, color pair *x* to a red
	foreground color on the default background.
	
	
	.. indow Objects
	--------------
	
	Window objects, as returned by :func:`initscr` and :func:`newwin` above, have
	the following methods:
	
	
	"""
	pass
	
