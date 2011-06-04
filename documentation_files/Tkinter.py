#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
""":synopsis: Interface to Tcl/Tk for graphical user interfaces
"""
class Tk:


	"""
	The :class:`Tk` class is instantiated without arguments. This creates a toplevel
	widget of Tk which usually is the main window of an application. Each instance
	has its own associated Tcl interpreter.
	
	.. ollowing keyword arguments are currently recognized:
	
	"""
	
	
	def __init__(self, screenName=None,baseName=None,_className='Tk',useTk=1):
		pass
	
	def Tcl(screenName=None,baseName=None,_className='Tk',useTk=0):
		"""
		The :func:`Tcl` function is a factory function which creates an object much like
		that created by the :class:`Tk` class, except that it does not initialize the Tk
		subsystem.  This is most often useful when driving the Tcl interpreter in an
		environment where one doesn't want to create extraneous toplevel windows, or
		where one cannot (such as Unix/Linux systems without an X server).  An object
		created by the :func:`Tcl` object can have a Toplevel window created (and the Tk
		subsystem initialized) by calling its :meth:`loadtk` method.
		
		"""
		pass
		
	


