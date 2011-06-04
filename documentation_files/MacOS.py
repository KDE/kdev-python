#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
""":platform: Mac
:synopsis: Access to Mac OS-specific interpreter features.
:deprecated:


This module provides access to MacOS specific functionality in the Python
interpreter, such as how the interpreter eventloop functions and the like. Use
with care.

"""
"""
Always ``'macho'``, from Python 2.4 on. In earlier versions of Python the value
could also be ``'ppc'`` for the classic Mac OS 8 runtime model or ``'carbon'``
for the Mac OS 9 runtime model.


"""
runtimemodel = None
"""
The way the interpreter has been linked. As extension modules may be
incompatible between linking models, packages could use this information to give
more decent error messages. The value is one of ``'static'`` for a statically
linked Python, ``'framework'`` for Python in a Mac OS X framework, ``'shared'``
for Python in a standard Unix shared library. Older Pythons could also have the
value ``'cfm'`` for Mac OS 9-compatible Python.


"""
linkmodel = None
def GetErrorString(errno):
	"""
	Return the textual description of MacOS error code *errno*.
	
	
	"""
	pass
	
def DebugStr(message,object):
	"""
	On Mac OS X the string is simply printed to stderr (on older Mac OS systems more
	elaborate functionality was available), but it provides a convenient location to
	attach a breakpoint in a low-level debugger like :program:`gdb`.
	
	"""
	pass
	
def SysBeep():
	"""
	Ring the bell.
	
	"""
	pass
	
def GetTicks():
	"""
	Get the number of clock ticks (1/60th of a second) since system boot.
	
	
	"""
	pass
	
def GetCreatorAndType(file):
	"""
	Return the file creator and file type as two four-character strings. The *file*
	parameter can be a pathname or an ``FSSpec`` or  ``FSRef`` object.
	
	"""
	pass
	
def SetCreatorAndType(file,creator,type):
	"""
	Set the file creator and file type. The *file* parameter can be a pathname or an
	``FSSpec`` or  ``FSRef`` object. *creator* and *type* must be four character
	strings.
	
	"""
	pass
	
def openrf(name,mode):
	"""
	Open the resource fork of a file. Arguments are the same as for the built-in
	function :func:`open`. The object returned has file-like semantics, but it is
	not a Python file object, so there may be subtle differences.
	
	
	"""
	pass
	
def WMAvailable():
	"""
	Checks whether the current process has access to the window manager. The method
	will return ``False`` if the window manager is not available, for instance when
	running on Mac OS X Server or when logged in via ssh, or when the current
	interpreter is not running from a fullblown application bundle. A script runs
	from an application bundle either when it has been started with
	:program:`pythonw` instead of :program:`python` or when running  as an applet.
	
	"""
	pass
	
def splash(resourceid):
	"""
	Opens a splash screen by resource id. Use resourceid ``0`` to close
	the splash screen.
	
	"""
	pass
	
