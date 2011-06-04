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
	
	
	def __init__(self, win):
		pass
	
	


