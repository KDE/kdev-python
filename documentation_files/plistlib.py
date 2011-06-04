#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
""":synopsis: Generate and parse Mac OS X plist files.
"""
def readPlist(pathOrFile):
	"""
	Read a plist file. *pathOrFile* may either be a file name or a (readable)
	file object.  Return the unpacked root object (which usually is a
	dictionary).
	
	The XML data is parsed using the Expat parser from :mod:`xml.parsers.expat`
	-- see its documentation for possible exceptions on ill-formed XML.
	Unknown elements will simply be ignored by the plist parser.
	
	
	"""
	pass
	
def writePlist(rootObject,pathOrFile):
	"""
	Write *rootObject* to a plist file. *pathOrFile* may either be a file name
	or a (writable) file object.
	
	A :exc:`TypeError` will be raised if the object is of an unsupported type or
	a container that contains objects of unsupported types.
	
	
	"""
	pass
	
def readPlistFromString(data):
	"""
	Read a plist from a string.  Return the root object.
	
	
	"""
	pass
	
def writePlistToString(rootObject):
	"""
	Return *rootObject* as a plist-formatted string.
	
	
	
	"""
	pass
	
def readPlistFromResource(path,restype='plst',resid=0):
	"""
	Read a plist from the resource with type *restype* from the resource fork of
	*path*.  Availability: Mac OS X.
	
	"""
	pass
	
def writePlistToResource(rootObject,path,restype='plst',resid=0):
	"""
	Write *rootObject* as a resource with type *restype* to the resource fork of
	*path*.  Availability: Mac OS X.
	
	"""
	pass
	
