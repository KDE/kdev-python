#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
""":synopsis: Read and write tar-format archive files.


"""
def open(name=None,mode='r',fileobj=None,bufsize=10240,kwargs=None):
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
	
	def is_tarfile(self, name):
		"""
		Return :const:`True` if *name* is a tar archive file, that the :mod:`tarfile`
		module can read.
		
		
		"""
		pass
		
	def open(self, more):
		"""
		Alternative constructor. The :func:`tarfile.open` function is actually a
		shortcut to this classmethod.
		
		
		"""
		pass
		
	def getmember(self, name):
		"""
		Return a :class:`TarInfo` object for member *name*. If *name* can not be found
		in the archive, :exc:`KeyError` is raised.
		
		"""
		pass
		
	def getmembers(self, ):
		"""
		Return the members of the archive as a list of :class:`TarInfo` objects. The
		list has the same order as the members in the archive.
		
		
		"""
		pass
		
	def getnames(self, ):
		"""
		Return the members as a list of their names. It has the same order as the list
		returned by :meth:`getmembers`.
		
		
		"""
		pass
		
	def list(self, verbose=True):
		"""
		Print a table of contents to ``sys.stdout``. If *verbose* is :const:`False`,
		only the names of the members are printed. If it is :const:`True`, output
		similar to that of :program:`ls -l` is produced.
		
		
		"""
		pass
		
	def next(self, ):
		"""
		Return the next member of the archive as a :class:`TarInfo` object, when
		:class:`TarFile` is opened for reading. Return :const:`None` if there is no more
		available.
		
		
		"""
		pass
		
	def extract(self, member,path=""):
		"""
		Extract a member from the archive to the current working directory, using its
		full name. Its file information is extracted as accurately as possible. *member*
		may be a filename or a :class:`TarInfo` object. You can specify a different
		directory using *path*.
		
		"""
		pass
		
	def extractfile(self, member):
		"""
		Extract a member from the archive as a file object. *member* may be a filename
		or a :class:`TarInfo` object. If *member* is a regular file, a file-like object
		is returned. If *member* is a link, a file-like object is constructed from the
		link's target. If *member* is none of the above, :const:`None` is returned.
		
		"""
		pass
		
	def add(self, name,arcname=None,recursive=True,exclude=None,filter=None):
		"""
		Add the file *name* to the archive. *name* may be any type of file (directory,
		fifo, symbolic link, etc.). If given, *arcname* specifies an alternative name
		for the file in the archive. Directories are added recursively by default. This
		can be avoided by setting *recursive* to :const:`False`. If *exclude* is given
		it must be a function that takes one filename argument and returns a boolean
		value. Depending on this value the respective file is either excluded
		(:const:`True`) or added (:const:`False`). If *filter* is specified it must
		be a function that takes a :class:`TarInfo` object argument and returns the
		changed :class:`TarInfo` object. If it instead returns :const:`None` the :class:`TarInfo`
		object will be excluded from the archive. See :ref:`tar-examples` for an
		example.
		
		"""
		pass
		
	def addfile(self, tarinfo,fileobj=None):
		"""
		Add the :class:`TarInfo` object *tarinfo* to the archive. If *fileobj* is given,
		``tarinfo.size`` bytes are read from it and added to the archive.  You can
		create :class:`TarInfo` objects using :meth:`gettarinfo`.
		
		"""
		pass
		
	def gettarinfo(self, name=None,arcname=None,fileobj=None):
		"""
		Create a :class:`TarInfo` object for either the file *name* or the file object
		*fileobj* (using :func:`os.fstat` on its file descriptor).  You can modify some
		of the :class:`TarInfo`'s attributes before you add it using :meth:`addfile`.
		If given, *arcname* specifies an alternative name for the file in the archive.
		
		
		"""
		pass
		
	def close(self, ):
		"""
		Close the :class:`TarFile`. In write mode, two finishing zero blocks are
		appended to the archive.
		
		
		"""
		pass
		
	


class TarFileCompat:


	"""
	Class for limited access to tar archives with a :mod:`zipfile`\ -like interface.
	Please consult the documentation of the :mod:`zipfile` module for more details.
	*compression* must be one of the following constants:
	
	
	"""
	
	
	def __init__(self, ):
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
	
	
	def __init__(self, ):
		pass
	
	def is_tarfile(self, name):
		"""
		Return :const:`True` if *name* is a tar archive file, that the :mod:`tarfile`
		module can read.
		
		
		"""
		pass
		
	def open(self, more):
		"""
		Alternative constructor. The :func:`tarfile.open` function is actually a
		shortcut to this classmethod.
		
		
		"""
		pass
		
	def getmember(self, name):
		"""
		Return a :class:`TarInfo` object for member *name*. If *name* can not be found
		in the archive, :exc:`KeyError` is raised.
		
		"""
		pass
		
	def getmembers(self, ):
		"""
		Return the members of the archive as a list of :class:`TarInfo` objects. The
		list has the same order as the members in the archive.
		
		
		"""
		pass
		
	def getnames(self, ):
		"""
		Return the members as a list of their names. It has the same order as the list
		returned by :meth:`getmembers`.
		
		
		"""
		pass
		
	def list(self, verbose=True):
		"""
		Print a table of contents to ``sys.stdout``. If *verbose* is :const:`False`,
		only the names of the members are printed. If it is :const:`True`, output
		similar to that of :program:`ls -l` is produced.
		
		
		"""
		pass
		
	def next(self, ):
		"""
		Return the next member of the archive as a :class:`TarInfo` object, when
		:class:`TarFile` is opened for reading. Return :const:`None` if there is no more
		available.
		
		
		"""
		pass
		
	def extract(self, member,path=""):
		"""
		Extract a member from the archive to the current working directory, using its
		full name. Its file information is extracted as accurately as possible. *member*
		may be a filename or a :class:`TarInfo` object. You can specify a different
		directory using *path*.
		
		"""
		pass
		
	def extractfile(self, member):
		"""
		Extract a member from the archive as a file object. *member* may be a filename
		or a :class:`TarInfo` object. If *member* is a regular file, a file-like object
		is returned. If *member* is a link, a file-like object is constructed from the
		link's target. If *member* is none of the above, :const:`None` is returned.
		
		"""
		pass
		
	def add(self, name,arcname=None,recursive=True,exclude=None,filter=None):
		"""
		Add the file *name* to the archive. *name* may be any type of file (directory,
		fifo, symbolic link, etc.). If given, *arcname* specifies an alternative name
		for the file in the archive. Directories are added recursively by default. This
		can be avoided by setting *recursive* to :const:`False`. If *exclude* is given
		it must be a function that takes one filename argument and returns a boolean
		value. Depending on this value the respective file is either excluded
		(:const:`True`) or added (:const:`False`). If *filter* is specified it must
		be a function that takes a :class:`TarInfo` object argument and returns the
		changed :class:`TarInfo` object. If it instead returns :const:`None` the :class:`TarInfo`
		object will be excluded from the archive. See :ref:`tar-examples` for an
		example.
		
		"""
		pass
		
	def addfile(self, tarinfo,fileobj=None):
		"""
		Add the :class:`TarInfo` object *tarinfo* to the archive. If *fileobj* is given,
		``tarinfo.size`` bytes are read from it and added to the archive.  You can
		create :class:`TarInfo` objects using :meth:`gettarinfo`.
		
		"""
		pass
		
	def gettarinfo(self, name=None,arcname=None,fileobj=None):
		"""
		Create a :class:`TarInfo` object for either the file *name* or the file object
		*fileobj* (using :func:`os.fstat` on its file descriptor).  You can modify some
		of the :class:`TarInfo`'s attributes before you add it using :meth:`addfile`.
		If given, *arcname* specifies an alternative name for the file in the archive.
		
		
		"""
		pass
		
	def close(self, ):
		"""
		Close the :class:`TarFile`. In write mode, two finishing zero blocks are
		appended to the archive.
		
		
		"""
		pass
		
	


class TarInfo:


	"""
	Create a :class:`TarInfo` object.
	
	
	"""
	
	
	def __init__(self, ):
		pass
	
	def _frombuf(self, buf):
		"""
		Create and return a :class:`TarInfo` object from string buffer *buf*.
		
		"""
		pass
		
	def _fromtarfile(self, tarfile):
		"""
		Read the next member from the :class:`TarFile` object *tarfile* and return it as
		a :class:`TarInfo` object.
		
		"""
		pass
		
	def tobuf(self, format=DEFAULT_FORMAT,encoding=ENCODING,errors='strict'):
		"""
		Create a string buffer from a :class:`TarInfo` object. For information on the
		arguments see the constructor of the :class:`TarFile` class.
		
		"""
		pass
		
	def isfile(self, ):
		"""
		Return :const:`True` if the :class:`Tarinfo` object is a regular file.
		
		
		"""
		pass
		
	def isreg(self, ):
		"""
		Same as :meth:`isfile`.
		
		
		"""
		pass
		
	def isdir(self, ):
		"""
		Return :const:`True` if it is a directory.
		
		
		"""
		pass
		
	def issym(self, ):
		"""
		Return :const:`True` if it is a symbolic link.
		
		
		"""
		pass
		
	def islnk(self, ):
		"""
		Return :const:`True` if it is a hard link.
		
		
		"""
		pass
		
	def ischr(self, ):
		"""
		Return :const:`True` if it is a character device.
		
		
		"""
		pass
		
	def isblk(self, ):
		"""
		Return :const:`True` if it is a block device.
		
		
		"""
		pass
		
	def isfifo(self, ):
		"""
		Return :const:`True` if it is a FIFO.
		
		
		"""
		pass
		
	


