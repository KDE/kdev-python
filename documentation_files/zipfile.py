#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
""":synopsis: Read and write ZIP-format archive files.
"""
class ZipFile:


	""":noindex:
	
	The class for reading and writing ZIP files.  See section
	:ref:`zipfile-objects` for constructor details.
	
	
	"""
	
	
	def __init__(self, ):
		pass
	
	


class PyZipFile:


	"""
	Class for creating ZIP archives containing Python libraries.
	
	
	"""
	
	
	def __init__(self, ):
		pass
	
	


class ZipInfo:


	"""
	Class used to represent information about a member of an archive. Instances
	of this class are returned by the :meth:`getinfo` and :meth:`infolist`
	methods of :class:`ZipFile` objects.  Most users of the :mod:`zipfile` module
	will not need to create these, but only use those created by this
	module. *filename* should be the full name of the archive member, and
	*date_time* should be a tuple containing six fields which describe the time
	of the last modification to the file; the fields are described in section
	:ref:`zipinfo-objects`.
	
	
	"""
	
	
	def __init__(self, filename,date_time):
		pass
	
	def is_zipfile(filename):
		"""
		Returns ``True`` if *filename* is a valid ZIP file based on its magic number,
		otherwise returns ``False``.  *filename* may be a file or file-like object too.
		
		"""
		pass
		
	"""
	The numeric constant for an uncompressed archive member.
	
	
	"""
	ZIP_STORED = None
	"""
	The numeric constant for the usual ZIP compression method.  This requires the
	zlib module.  No other compression methods are currently supported.
	
	
	"""
	ZIP_DEFLATED = None
	


class ZipFile:


	"""
	Open a ZIP file, where *file* can be either a path to a file (a string) or a
	file-like object.  The *mode* parameter should be ``'r'`` to read an existing
	file, ``'w'`` to truncate and write a new file, or ``'a'`` to append to an
	existing file.  If *mode* is ``'a'`` and *file* refers to an existing ZIP
	file, then additional files are added to it.  If *file* does not refer to a
	ZIP file, then a new ZIP archive is appended to the file.  This is meant for
	adding a ZIP archive to another file (such as :file:`python.exe`).
	
	"""
	
	
	def __init__(self, file,mode,compression,allowZip64):
		pass
	
	


