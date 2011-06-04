#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
""":platform: Unix
:synopsis: A file-like object with support for locking.
:deprecated:
"""
"""
Offset is calculated from the start of the file.


"""
SEEK_SET = None
"""
Offset is calculated from the current position in the file.


"""
SEEK_CUR = None
"""
Offset is calculated from the end of the file.

The :mod:`posixfile` module defines the following functions:


"""
SEEK_END = None
def open(filename,mode,bufsize):
	"""
	Create a new posixfile object with the given filename and mode.  The *filename*,
	*mode* and *bufsize* arguments are interpreted the same way as by the built-in
	:func:`open` function.
	
	
	"""
	pass
	
def fileopen(fileobject):
	"""
	Create a new posixfile object with the given standard file object. The resulting
	object has the same filename and mode as the original file object.
	
	The posixfile object defines the following additional methods:
	
	
	"""
	pass
	
