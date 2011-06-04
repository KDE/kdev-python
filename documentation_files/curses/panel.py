#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
""":synopsis: A panel stack extension that adds depth to  curses windows.
"""
def bottom_panel():
	"""
	Returns the bottom panel in the panel stack.
	
	
	"""
	pass
	
def new_panel(win):
	"""
	Returns a panel object, associating it with the given window *win*. Be aware
	that you need to keep the returned panel object referenced explicitly.  If you
	don't, the panel object is garbage collected and removed from the panel stack.
	
	
	"""
	pass
	
def top_panel():
	"""
	Returns the top panel in the panel stack.
	
	
	"""
	pass
	
def update_panels():
	"""
	Updates the virtual screen after changes in the panel stack. This does not call
	:func:`curses.doupdate`, so you'll have to do this yourself.
	
	
	.. anel Objects
	-------------
	
	Panel objects, as returned by :func:`new_panel` above, are windows with a
	stacking order. There's always a window associated with a panel which determines
	the content, while the panel methods are responsible for the window's depth in
	the panel stack.
	
	Panel objects have the following methods:
	
	
	"""
	pass
	
