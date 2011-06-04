#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
""":synopsis: Emacs-like input editing in a curses window.
"""
def rectangle(win,uly,ulx,lry,lrx):
	"""
	Draw a rectangle.  The first argument must be a window object; the remaining
	arguments are coordinates relative to that window.  The second and third
	arguments are the y and x coordinates of the upper left hand corner of the
	rectangle to be drawn; the fourth and fifth arguments are the y and x
	coordinates of the lower right hand corner. The rectangle will be drawn using
	VT100/IBM PC forms characters on terminals that make this possible (including
	xterm and most other software terminal emulators).  Otherwise it will be drawn
	with ASCII  dashes, vertical bars, and plus signs.
	
	
	.. extbox objects
	---------------
	
	You can instantiate a :class:`Textbox` object as follows:
	
	
	"""
	pass
	
class Textbox:


	"""
	Return a textbox widget object.  The *win* argument should be a curses
	:class:`WindowObject` in which the textbox is to be contained. The edit cursor
	of the textbox is initially located at the upper left hand corner of the
	containing window, with coordinates ``(0, 0)``. The instance's
	:attr:`stripspaces` flag is initially on.
	
	:class:`Textbox` objects have the following methods:
	
	
	"""
	
	
	def __init__(self, ):
		pass
	
	def edit(self, validator):
		"""
		This is the entry point you will normally use.  It accepts editing
		keystrokes until one of the termination keystrokes is entered.  If
		*validator* is supplied, it must be a function.  It will be called for
		each keystroke entered with the keystroke as a parameter; command dispatch
		is done on the result. This method returns the window contents as a
		string; whether blanks in the window are included is affected by the
		:attr:`stripspaces` member.
		
		
		"""
		pass
		
	def do_command(self, ch):
		"""
		Process a single command keystroke.  Here are the supported special
		keystrokes:
		
		+------------------+-------------------------------------------+
		| Keystroke        | Action                                    |
		+==================+===========================================+
		| :kbd:`Control-A` | Go to left edge of window.                |
		+------------------+-------------------------------------------+
		| :kbd:`Control-B` | Cursor left, wrapping to previous line if |
		|                  | appropriate.                              |
		+------------------+-------------------------------------------+
		| :kbd:`Control-D` | Delete character under cursor.            |
		+------------------+-------------------------------------------+
		| :kbd:`Control-E` | Go to right edge (stripspaces off) or end |
		|                  | of line (stripspaces on).                 |
		+------------------+-------------------------------------------+
		| :kbd:`Control-F` | Cursor right, wrapping to next line when  |
		|                  | appropriate.                              |
		+------------------+-------------------------------------------+
		| :kbd:`Control-G` | Terminate, returning the window contents. |
		+------------------+-------------------------------------------+
		| :kbd:`Control-H` | Delete character backward.                |
		+------------------+-------------------------------------------+
		| :kbd:`Control-J` | Terminate if the window is 1 line,        |
		|                  | otherwise insert newline.                 |
		+------------------+-------------------------------------------+
		| :kbd:`Control-K` | If line is blank, delete it, otherwise    |
		|                  | clear to end of line.                     |
		+------------------+-------------------------------------------+
		| :kbd:`Control-L` | Refresh screen.                           |
		+------------------+-------------------------------------------+
		| :kbd:`Control-N` | Cursor down; move down one line.          |
		+------------------+-------------------------------------------+
		| :kbd:`Control-O` | Insert a blank line at cursor location.   |
		+------------------+-------------------------------------------+
		| :kbd:`Control-P` | Cursor up; move up one line.              |
		+------------------+-------------------------------------------+
		
		Move operations do nothing if the cursor is at an edge where the movement
		is not possible.  The following synonyms are supported where possible:
		
		+------------------------+------------------+
		| Constant               | Keystroke        |
		+========================+==================+
		| :const:`KEY_LEFT`      | :kbd:`Control-B` |
		+------------------------+------------------+
		| :const:`KEY_RIGHT`     | :kbd:`Control-F` |
		+------------------------+------------------+
		| :const:`KEY_UP`        | :kbd:`Control-P` |
		+------------------------+------------------+
		| :const:`KEY_DOWN`      | :kbd:`Control-N` |
		+------------------------+------------------+
		| :const:`KEY_BACKSPACE` | :kbd:`Control-h` |
		+------------------------+------------------+
		
		All other keystrokes are treated as a command to insert the given
		character and move right (with line wrapping).
		
		
		"""
		pass
		
	def gather(self, ):
		"""
		This method returns the window contents as a string; whether blanks in the
		window are included is affected by the :attr:`stripspaces` member.
		
		
		"""
		pass
		
	


