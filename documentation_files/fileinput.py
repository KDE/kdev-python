#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
""":synopsis: Loop over standard input or a list of files.
"""
def input(files,inplace,backup,mode,openhook):
	"""
	Create an instance of the :class:`FileInput` class.  The instance will be used
	as global state for the functions of this module, and is also returned to use
	during iteration.  The parameters to this function will be passed along to the
	constructor of the :class:`FileInput` class.
	
	"""
	pass
	
def filename():
	"""
	Return the name of the file currently being read.  Before the first line has
	been read, returns ``None``.
	
	
	"""
	pass
	
def fileno():
	"""
	Return the integer "file descriptor" for the current file. When no file is
	opened (before the first line and between files), returns ``-1``.
	
	"""
	pass
	
def lineno():
	"""
	Return the cumulative line number of the line that has just been read.  Before
	the first line has been read, returns ``0``.  After the last line of the last
	file has been read, returns the line number of that line.
	
	
	"""
	pass
	
def filelineno():
	"""
	Return the line number in the current file.  Before the first line has been
	read, returns ``0``.  After the last line of the last file has been read,
	returns the line number of that line within the file.
	
	
	"""
	pass
	
def isfirstline():
	"""
	Returns true if the line just read is the first line of its file, otherwise
	returns false.
	
	
	"""
	pass
	
def isstdin():
	"""
	Returns true if the last line was read from ``sys.stdin``, otherwise returns
	false.
	
	
	"""
	pass
	
def nextfile():
	"""
	Close the current file so that the next iteration will read the first line from
	the next file (if any); lines not read from the file will not count towards the
	cumulative line count.  The filename is not changed until after the first line
	of the next file has been read.  Before the first line has been read, this
	function has no effect; it cannot be used to skip the first file.  After the
	last line of the last file has been read, this function has no effect.
	
	
	"""
	pass
	
def close():
	"""
	Close the sequence.
	
	The class which implements the sequence behavior provided by the module is
	available for subclassing as well:
	
	
	"""
	pass
	
class FileInput:


	"""
	Class :class:`FileInput` is the implementation; its methods :meth:`filename`,
	:meth:`fileno`, :meth:`lineno`, :meth:`filelineno`, :meth:`isfirstline`,
	:meth:`isstdin`, :meth:`nextfile` and :meth:`close` correspond to the functions
	of the same name in the module. In addition it has a :meth:`readline` method
	which returns the next input line, and a :meth:`__getitem__` method which
	implements the sequence behavior.  The sequence must be accessed in strictly
	sequential order; random access and :meth:`readline` cannot be mixed.
	
	With *mode* you can specify which file mode will be passed to :func:`open`. It
	must be one of ``'r'``, ``'rU'``, ``'U'`` and ``'rb'``.
	
	The *openhook*, when given, must be a function that takes two arguments,
	*filename* and *mode*, and returns an accordingly opened file-like object. You
	cannot use *inplace* and *openhook* together.
	
	"""
	
	
	def __init__(self, ):
		pass
	
	def hook_compressed(self, filename,mode):
		"""
		Transparently opens files compressed with gzip and bzip2 (recognized by the
		extensions ``'.gz'`` and ``'.bz2'``) using the :mod:`gzip` and :mod:`bz2`
		modules.  If the filename extension is not ``'.gz'`` or ``'.bz2'``, the file is
		opened normally (ie, using :func:`open` without any decompression).
		
		Usage example:  ``fi = fileinput.FileInput(openhook=fileinput.hook_compressed)``
		
		"""
		pass
		
	def hook_encoded(self, encoding):
		"""
		Returns a hook which opens each file with :func:`codecs.open`, using the given
		*encoding* to read the file.
		
		Usage example: ``fi =
		fileinput.FileInput(openhook=fileinput.hook_encoded("iso-8859-1"))``
		
		"""
		pass
		
	


