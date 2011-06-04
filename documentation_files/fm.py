#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
""":platform: IRIX
:synopsis: Font Manager interface for SGI workstations.
:deprecated:

"""
def init():
	"""
	Initialization function. Calls :cfunc:`fminit`. It is normally not necessary to
	call this function, since it is called automatically the first time the
	:mod:`fm` module is imported.
	
	
	"""
	pass
	
def findfont(fontname):
	"""
	Return a font handle object. Calls ``fmfindfont(fontname)``.
	
	
	"""
	pass
	
def enumerate():
	"""
	Returns a list of available font names. This is an interface to
	:cfunc:`fmenumerate`.
	
	
	"""
	pass
	
def prstr(string):
	"""
	Render a string using the current font (see the :func:`setfont` font handle
	method below). Calls ``fmprstr(string)``.
	
	
	"""
	pass
	
def setpath(string):
	"""
	Sets the font search path. Calls ``fmsetpath(string)``. (XXX Does not work!?!)
	
	
	"""
	pass
	
def fontpath():
	"""
	Returns the current font search path.
	
	Font handle objects support the following operations:
	
	
	"""
	pass
	
