#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
""":synopsis: Encode and decode files in uuencode format.
"""
def encode(in_file,out_file,name,mode):
	"""
	Uuencode file *in_file* into file *out_file*.  The uuencoded file will have the
	header specifying *name* and *mode* as the defaults for the results of decoding
	the file. The default defaults are taken from *in_file*, or ``'-'`` and ``0666``
	respectively.
	
	
	"""
	pass
	
def decode(in_file,out_file,mode,quiet):
	"""
	This call decodes uuencoded file *in_file* placing the result on file
	*out_file*. If *out_file* is a pathname, *mode* is used to set the permission
	bits if the file must be created. Defaults for *out_file* and *mode* are taken
	from the uuencode header.  However, if the file specified in the header already
	exists, a :exc:`uu.Error` is raised.
	
	:func:`decode` may print a warning to standard error if the input was produced
	by an incorrect uuencoder and Python could recover from that error.  Setting
	*quiet* to a true value silences this warning.
	
	
	"""
	pass
	
