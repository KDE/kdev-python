#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
""":synopsis: Encode and decode files in binhex4 format.


This module encodes and decodes files in binhex4 format, a format allowing
representation of Macintosh files in ASCII.  On the Macintosh, both forks of a
file and the finder information are encoded (or decoded), on other platforms
only the data fork is handled.

"""
def binhex(input,output):
	"""
	Convert a binary file with filename *input* to binhex file *output*. The
	*output* parameter can either be a filename or a file-like object (any object
	supporting a :meth:`write` and :meth:`close` method).
	
	
	"""
	pass
	
def hexbin(input,output):
	"""
	Decode a binhex file *input*. *input* may be a filename or a file-like object
	supporting :meth:`read` and :meth:`close` methods. The resulting file is written
	to a file named *output*, unless the argument is omitted in which case the
	output filename is read from the binhex file.
	
	The following exception is also defined:
	
	
	"""
	pass
	
