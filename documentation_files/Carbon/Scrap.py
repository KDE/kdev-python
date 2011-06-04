#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
""":platform: Mac
:synopsis: The Scrap Manager provides basic services for implementing cut & paste and
clipboard operations.
:deprecated:


This module is only fully available on Mac OS 9 and earlier under classic PPC
MacPython.  Very limited functionality is available under Carbon MacPython.

"""
def InfoScrap():
	"""
	Return current information about the scrap.  The information is encoded as a
	tuple containing the fields ``(size, handle, count, state, path)``.
	
	+----------+---------------------------------------------+
	| Field    | Meaning                                     |
	+==========+=============================================+
	| *size*   | Size of the scrap in bytes.                 |
	+----------+---------------------------------------------+
	| *handle* | Resource object representing the scrap.     |
	+----------+---------------------------------------------+
	| *count*  | Serial number of the scrap contents.        |
	+----------+---------------------------------------------+
	| *state*  | Integer; positive if in memory, ``0`` if on |
	|          | disk, negative if uninitialized.            |
	+----------+---------------------------------------------+
	| *path*   | Filename of the scrap when stored on disk.  |
	+----------+---------------------------------------------+
	
	
	"""
	pass
	
