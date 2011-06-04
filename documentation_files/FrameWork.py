#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
""":platform: Mac
:synopsis: Interactive application framework.
:deprecated:


The :mod:`FrameWork` module contains classes that together provide a framework
for an interactive Macintosh application. The programmer builds an application
by creating subclasses that override various methods of the bases classes,
thereby implementing the functionality wanted. Overriding functionality can
often be done on various different levels, i.e. to handle clicks in a single
dialog window in a non-standard way it is not necessary to override the complete
event handling.

"""
def Application():
	"""
	An object representing the complete application. See below for a description of
	the methods. The default :meth:`__init__` routine creates an empty window
	dictionary and a menu bar with an apple menu.
	
	
	"""
	pass
	
def MenuBar():
	"""
	An object representing the menubar. This object is usually not created by the
	user.
	
	
	"""
	pass
	
def Menu(bar,title,after):
	"""
	An object representing a menu. Upon creation you pass the ``MenuBar`` the menu
	appears in, the *title* string and a position (1-based) *after* where the menu
	should appear (default: at the end).
	
	
	"""
	pass
	
def MenuItem(menu,title,shortcut,callback):
	"""
	Create a menu item object. The arguments are the menu to create, the item title
	string and optionally the keyboard shortcut and a callback routine. The callback
	is called with the arguments menu-id, item number within menu (1-based), current
	front window and the event record.
	
	Instead of a callable object the callback can also be a string. In this case
	menu selection causes the lookup of a method in the topmost window and the
	application. The method name is the callback string with ``'domenu_'``
	prepended.
	
	Calling the ``MenuBar`` :meth:`fixmenudimstate` method sets the correct dimming
	for all menu items based on the current front window.
	
	
	"""
	pass
	
def Separator(menu):
	"""
	Add a separator to the end of a menu.
	
	
	"""
	pass
	
def SubMenu(menu,label):
	"""
	Create a submenu named *label* under menu *menu*. The menu object is returned.
	
	
	"""
	pass
	
def Window(parent):
	"""
	Creates a (modeless) window. *Parent* is the application object to which the
	window belongs. The window is not displayed until later.
	
	
	"""
	pass
	
def DialogWindow(parent):
	"""
	Creates a modeless dialog window.
	
	
	"""
	pass
	
def windowbounds(width,height):
	"""
	Return a ``(left, top, right, bottom)`` tuple suitable for creation of a window
	of given width and height. The window will be staggered with respect to previous
	windows, and an attempt is made to keep the whole window on-screen. However, the
	window will however always be the exact size given, so parts may be offscreen.
	
	
	"""
	pass
	
def setwatchcursor():
	"""
	Set the mouse cursor to a watch.
	
	
	"""
	pass
	
def setarrowcursor():
	"""
	Set the mouse cursor to an arrow.
	
	
	.. pplication Objects
	-------------------
	
	Application objects have the following methods, among others:
	
	
	"""
	pass
	
