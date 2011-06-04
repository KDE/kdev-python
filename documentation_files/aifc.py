#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
""":synopsis: Read and write audio files in AIFF or AIFC format.


"""
def open(file,mode):
	"""
	Open an AIFF or AIFF-C file and return an object instance with methods that are
	described below.  The argument *file* is either a string naming a file or a file
	object.  *mode* must be ``'r'`` or ``'rb'`` when the file must be opened for
	reading, or ``'w'``  or ``'wb'`` when the file must be opened for writing.  If
	omitted, ``file.mode`` is used if it exists, otherwise ``'rb'`` is used.  When
	used for writing, the file object should be seekable, unless you know ahead of
	time how many samples you are going to write in total and use
	:meth:`writeframesraw` and :meth:`setnframes`.
	
	Objects returned by :func:`.open` when a file is opened for reading have the
	following methods:
	
	
	"""
	pass
	
