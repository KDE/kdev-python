#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
""":synopsis: A standard way to reference site-specific modules.


**This module is automatically imported during initialization.** The automatic
import can be suppressed using the interpreter's :option:`-S` option.

"""
"""
A list of prefixes for site package directories

"""
PREFIXES = None
"""
Flag showing the status of the user site directory. True means the
user site directory is enabled and added to sys.path. When the flag
is None the user site directory is disabled for security reasons.

"""
ENABLE_USER_SITE = None
"""
Path to the user site directory for the current Python version or None

"""
USER_SITE = None
"""
Path to the base directory for user site directories

"""
USER_BASE = None
def addsitedir(sitedir,known_paths=None):
	"""
	Adds a directory to sys.path and processes its pth files.
	
	"""
	pass
	
def getsitepackages():
	"""
	Returns a list containing all global site-packages directories
	(and possibly site-python).
	
	"""
	pass
	
def getuserbase():
	"""
	Returns the "user base" directory path.
	
	The "user base" directory can be used to store data. If the global
	variable ``USER_BASE`` is not initialized yet, this function will also set
	it.
	
	"""
	pass
	
def getusersitepackages():
	"""
	Returns the user-specific site-packages directory path.
	
	If the global variable ``USER_SITE`` is not initialized yet, this
	function will also set it.
	
	"""
	pass
	
