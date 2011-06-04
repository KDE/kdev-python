#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
""":platform: IRIX
:synopsis: FORMS library for applications with graphical user interfaces.
:deprecated:


"""
def make_form(type,width,height):
	"""
	Create a form with given type, width and height.  This returns a :dfn:`form`
	object, whose methods are described below.
	
	
	"""
	pass
	
def do_forms():
	"""
	The standard FORMS main loop.  Returns a Python object representing the FORMS
	object needing interaction, or the special value :const:`FL.EVENT`.
	
	
	"""
	pass
	
def check_forms():
	"""
	Check for FORMS events.  Returns what :func:`do_forms` above returns, or
	``None`` if there is no event that immediately needs interaction.
	
	
	"""
	pass
	
def set_event_call_back(function):
	"""
	Set the event callback function.
	
	
	"""
	pass
	
def set_graphics_mode(rgbmode,doublebuffering):
	"""
	Set the graphics modes.
	
	
	"""
	pass
	
def get_rgbmode():
	"""
	Return the current rgb mode.  This is the value of the C global variable
	:cdata:`fl_rgbmode`.
	
	
	"""
	pass
	
def show_message(str1,str2,str3):
	"""
	Show a dialog box with a three-line message and an OK button.
	
	
	"""
	pass
	
def show_question(str1,str2,str3):
	"""
	Show a dialog box with a three-line message and YES and NO buttons. It returns
	``1`` if the user pressed YES, ``0`` if NO.
	
	
	"""
	pass
	
def show_choice(str1,str2,str3,but1,but2,but3):
	"""
	Show a dialog box with a three-line message and up to three buttons. It returns
	the number of the button clicked by the user (``1``, ``2`` or ``3``).
	
	
	"""
	pass
	
def show_input(prompt,default):
	"""
	Show a dialog box with a one-line prompt message and text field in which the
	user can enter a string.  The second argument is the default input string.  It
	returns the string value as edited by the user.
	
	
	"""
	pass
	
def show_file_selector(message,directory,pattern,default):
	"""
	Show a dialog box in which the user can select a file.  It returns the absolute
	filename selected by the user, or ``None`` if the user presses Cancel.
	
	
	"""
	pass
	
def get_directory():
	"""get_pattern()
	get_filename()
	
	These functions return the directory, pattern and filename (the tail part only)
	selected by the user in the last :func:`show_file_selector` call.
	
	
	"""
	pass
	
def qdevice(dev):
	"""unqdevice(dev)
	isqueued(dev)
	qtest()
	qread()
	qreset()
	qenter(dev, val)
	get_mouse()
	tie(button, valuator1, valuator2)
	
	These functions are the FORMS interfaces to the corresponding GL functions.  Use
	these if you want to handle some GL events yourself when using
	:func:`fl.do_events`.  When a GL event is detected that FORMS cannot handle,
	:func:`fl.do_forms` returns the special value :const:`FL.EVENT` and you should
	call :func:`fl.qread` to read the event from the queue.  Don't use the
	equivalent GL functions!
	
	"""
	pass
	
def color():
	"""mapcolor()
	getmcolor()
	
	See the description in the FORMS documentation of :cfunc:`fl_color`,
	:cfunc:`fl_mapcolor` and :cfunc:`fl_getmcolor`.
	
	
	.. orm Objects
	"""
	pass
	
