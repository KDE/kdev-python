#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
""":synopsis: Read and write tar-format archive files.


"""
def open(name=None,mode='r',fileobj=None,bufsize=10240,ESCESCkwargs):
	"""
	Return a :class:`TarFile` object for the pathname *name*. For detailed
	information on :class:`TarFile` objects and the keyword arguments that are
	allowed, see :ref:`tarfile-objects`.
	
	*mode* has to be a string of the form ``'filemode[:compression]'``, it defaults
	to ``'r'``. Here is a full list of mode combinations:
	
	+------------------+---------------------------------------------+
	| mode             | action                                      |
	+==================+=============================================+
	| ``'r' or 'r:*'`` | Open for reading with transparent           |
	|                  | compression (recommended).                  |
	+------------------+---------------------------------------------+
	| ``'r:'``         | Open for reading exclusively without        |
	|                  | compression.                                |
	+------------------+---------------------------------------------+
	| ``'r:gz'``       | Open for reading with gzip compression.     |
	+------------------+---------------------------------------------+
	| ``'r:bz2'``      | Open for reading with bzip2 compression.    |
	+------------------+---------------------------------------------+
	| ``'a' or 'a:'``  | Open for appending with no compression. The |
	|                  | file is created if it does not exist.       |
	+------------------+---------------------------------------------+
	| ``'w' or 'w:'``  | Open for uncompressed writing.              |
	+------------------+---------------------------------------------+
	| ``'w:gz'``       | Open for gzip compressed writing.           |
	+------------------+---------------------------------------------+
	| ``'w:bz2'``      | Open for bzip2 compressed writing.          |
	+------------------+---------------------------------------------+
	
	Note that ``'a:gz'`` or ``'a:bz2'`` is not possible. If *mode* is not suitable
	to open a certain (compressed) file for reading, :exc:`ReadError` is raised. Use
	*mode* ``'r'`` to avoid this.  If a compression method is not supported,
	:exc:`CompressionError` is raised.
	
	If *fileobj* is specified, it is used as an alternative to a file object opened
	for *name*. It is supposed to be at position 0.
	
	For special purposes, there is a second format for *mode*:
	``'filemode|[compression]'``.  :func:`tarfile.open` will return a :class:`TarFile`
	object that processes its data as a stream of blocks.  No random seeking will
	be done on the file. If given, *fileobj* may be any object that has a
	:meth:`read` or :meth:`write` method (depending on the *mode*). *bufsize*
	specifies the blocksize and defaults to ``20 * 512`` bytes. Use this variant
	in combination with e.g. ``sys.stdin``, a socket file object or a tape
	device. However, such a :class:`TarFile` object is limited in that it does
	not allow to be accessed randomly, see :ref:`tar-examples`.  The currently
	possible modes:
	
	+-------------+--------------------------------------------+
	| Mode        | Action                                     |
	+=============+============================================+
	| ``'r|*'``   | Open a *stream* of tar blocks for reading  |
	|             | with transparent compression.              |
	+-------------+--------------------------------------------+
	| ``'r|'``    | Open a *stream* of uncompressed tar blocks |
	|             | for reading.                               |
	+-------------+--------------------------------------------+
	| ``'r|gz'``  | Open a gzip compressed *stream* for        |
	|             | reading.                                   |
	+-------------+--------------------------------------------+
	| ``'r|bz2'`` | Open a bzip2 compressed *stream* for       |
	|             | reading.                                   |
	+-------------+--------------------------------------------+
	| ``'w|'``    | Open an uncompressed *stream* for writing. |
	+-------------+--------------------------------------------+
	| ``'w|gz'``  | Open an gzip compressed *stream* for       |
	|             | writing.                                   |
	+-------------+--------------------------------------------+
	| ``'w|bz2'`` | Open an bzip2 compressed *stream* for      |
	|             | writing.                                   |
	+-------------+--------------------------------------------+
	
	
	"""
	pass
	
class TarFile:


	"""
	Class for reading and writing tar archives. Do not use this class directly,
	better use :func:`tarfile.open` instead. See :ref:`tarfile-objects`.
	
	
	"""
	
	
	def __init__(self, ):
		pass
	
	def is_tarfile(name):
		"""
		Return :const:`True` if *name* is a tar archive file, that the :mod:`tarfile`
		module can read.
		
		
		"""
		pass
		
	


class TarFileCompat:


	"""
	Class for limited access to tar archives with a :mod:`zipfile`\ -like interface.
	Please consult the documentation of the :mod:`zipfile` module for more details.
	*compression* must be one of the following constants:
	
	
	"""
	
	
	def __init__(self, filename,mode='r',compression=TAR_PLAIN):
		pass
	
	"""
	Constant for an uncompressed tar archive.
	
	
	"""
	TAR_PLAIN = None
	"""
	Constant for a :mod:`gzip` compressed tar archive.
	
	
	"""
	TAR_GZIPPED = None
	"""
	POSIX.1-1988 (ustar) format.
	
	
	"""
	USTAR_FORMAT = None
	"""
	GNU tar format.
	
	
	"""
	GNU_FORMAT = None
	"""
	POSIX.1-2001 (pax) format.
	
	
	"""
	PAX_FORMAT = None
	"""
	The default format for creating archives. This is currently :const:`GNU_FORMAT`.
	
	
	The following variables are available on module level:
	
	
	"""
	DEFAULT_FORMAT = None
	"""
	The default character encoding i.e. the value from either
	:func:`sys.getfilesystemencoding` or :func:`sys.getdefaultencoding`.
	
	
	"""
	ENCODING = None
	


class TarFile:


	"""
	All following arguments are optional and can be accessed as instance attributes
	as well.
	
	*name* is the pathname of the archive. It can be omitted if *fileobj* is given.
	In this case, the file object's :attr:`name` attribute is used if it exists.
	
	*mode* is either ``'r'`` to read from an existing archive, ``'a'`` to append
	data to an existing file or ``'w'`` to create a new file overwriting an existing
	one.
	
	If *fileobj* is given, it is used for reading or writing data. If it can be
	determined, *mode* is overridden by *fileobj*'s mode. *fileobj* will be used
	from position 0.
	
	"""
	
	
	def __init__(self, name=None,mode='r',fileobj=None,format=DEFAULT_FORMAT,tarinfo=TarInfo,dereference=False,ignore_zeros=False,encoding=ENCODING,errors=None,pax_headers=None,debug=0,errorlevel=0):
		pass
	
	


class TarInfo:


	"""
	Create a :class:`TarInfo` object.
	
	
	"""
	
	
	def __init__(self, name=""):
		pass
	
	


