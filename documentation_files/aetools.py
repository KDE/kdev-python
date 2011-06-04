#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
""":platform: Mac
:synopsis: Basic support for sending Apple Events
:deprecated:
"""
def packevent(ae,parameters,attributes):
	"""
	Stores parameters and attributes in a pre-created ``Carbon.AE.AEDesc`` object.
	``parameters`` and ``attributes`` are  dictionaries mapping 4-character OSA
	parameter keys to Python objects. The objects are packed using
	``aepack.pack()``.
	
	
	"""
	pass
	
def unpackevent(ae,formodulename):
	"""
	Recursively unpacks a ``Carbon.AE.AEDesc`` event to Python objects. The function
	returns the parameter dictionary and the attribute dictionary. The
	``formodulename`` argument is used by generated stub packages to control where
	AppleScript classes are looked up.
	
	
	"""
	pass
	
def keysubst(arguments,keydict):
	"""
	Converts a Python keyword argument dictionary ``arguments`` to the format
	required by ``packevent`` by replacing the keys, which are Python identifiers,
	by the four-character OSA keys according to the mapping specified in
	``keydict``. Used by the generated suite packages.
	
	
	"""
	pass
	
def enumsubst(arguments,key,edict):
	"""
	If the ``arguments`` dictionary contains an entry for ``key`` convert the value
	for that entry according to dictionary ``edict``. This converts human-readable
	Python enumeration names to the OSA 4-character codes. Used by the generated
	suite packages.
	
	The :mod:`aetools` module defines the following class:
	
	
	"""
	pass
	
class TalkTo:


	"""
	Base class for the proxy used to talk to an application. ``signature`` overrides
	the class attribute ``_signature`` (which is usually set by subclasses) and is
	the 4-char creator code defining the application to talk to. ``start`` can be
	set to true to enable running the application on class instantiation.
	``timeout`` can be specified to change the default timeout used while waiting
	for an AppleEvent reply.
	
	
	"""
	
	
	def __init__(self, signature=None,start=0,timeout=0):
		pass
	
	


