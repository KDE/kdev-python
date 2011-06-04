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
	
	def close(self, ):
		"""
		Close the archive file.  You must call :meth:`close` before exiting your program
		or essential records will not be written.
		
		
		"""
		pass
		
	def getinfo(self, name):
		"""
		Return a :class:`ZipInfo` object with information about the archive member
		*name*.  Calling :meth:`getinfo` for a name not currently contained in the
		archive will raise a :exc:`KeyError`.
		
		
		"""
		pass
		
	def infolist(self, ):
		"""
		Return a list containing a :class:`ZipInfo` object for each member of the
		archive.  The objects are in the same order as their entries in the actual ZIP
		file on disk if an existing archive was opened.
		
		
		"""
		pass
		
	def namelist(self, ):
		"""
		Return a list of archive members by name.
		
		
		"""
		pass
		
	def open(self, name,mode,pwd):
		"""
		Extract a member from the archive as a file-like object (ZipExtFile). *name* is
		the name of the file in the archive, or a :class:`ZipInfo` object. The *mode*
		parameter, if included, must be one of the following: ``'r'`` (the  default),
		``'U'``, or ``'rU'``. Choosing ``'U'`` or  ``'rU'`` will enable universal newline
		support in the read-only object. *pwd* is the password used for encrypted files.
		Calling  :meth:`open` on a closed ZipFile will raise a  :exc:`RuntimeError`.
		
		"""
		pass
		
	def extract(self, member,path,pwd):
		"""
		Extract a member from the archive to the current working directory; *member*
		must be its full name or a :class:`ZipInfo` object).  Its file information is
		extracted as accurately as possible.  *path* specifies a different directory
		to extract to.  *member* can be a filename or a :class:`ZipInfo` object.
		*pwd* is the password used for encrypted files.
		
		"""
		pass
		
	def extractall(self, path,members,pwd):
		"""
		Extract all members from the archive to the current working directory.  *path*
		specifies a different directory to extract to.  *members* is optional and must
		be a subset of the list returned by :meth:`namelist`.  *pwd* is the password
		used for encrypted files.
		
		"""
		pass
		
	def printdir(self, ):
		"""
		Print a table of contents for the archive to ``sys.stdout``.
		
		
		"""
		pass
		
	def setpassword(self, pwd):
		"""
		Set *pwd* as default password to extract encrypted files.
		
		"""
		pass
		
	def read(self, name,pwd):
		"""
		Return the bytes of the file *name* in the archive.  *name* is the name of the
		file in the archive, or a :class:`ZipInfo` object.  The archive must be open for
		read or append. *pwd* is the password used for encrypted  files and, if specified,
		it will override the default password set with :meth:`setpassword`.  Calling
		:meth:`read` on a closed ZipFile  will raise a :exc:`RuntimeError`.
		
		"""
		pass
		
	def testzip(self, ):
		"""
		Read all the files in the archive and check their CRC's and file headers.
		Return the name of the first bad file, or else return ``None``. Calling
		:meth:`testzip` on a closed ZipFile will raise a :exc:`RuntimeError`.
		
		
		"""
		pass
		
	def write(self, filename,arcname,compress_type):
		"""
		Write the file named *filename* to the archive, giving it the archive name
		*arcname* (by default, this will be the same as *filename*, but without a drive
		letter and with leading path separators removed).  If given, *compress_type*
		overrides the value given for the *compression* parameter to the constructor for
		the new entry.  The archive must be open with mode ``'w'`` or ``'a'`` -- calling
		:meth:`write` on a ZipFile created with mode ``'r'`` will raise a
		:exc:`RuntimeError`.  Calling  :meth:`write` on a closed ZipFile will raise a
		:exc:`RuntimeError`.
		
		"""
		pass
		
	def writestr(self, zinfo_or_arcname,bytes,compress_type):
		"""
		Write the string *bytes* to the archive; *zinfo_or_arcname* is either the file
		name it will be given in the archive, or a :class:`ZipInfo` instance.  If it's
		an instance, at least the filename, date, and time must be given.  If it's a
		name, the date and time is set to the current date and time. The archive must be
		opened with mode ``'w'`` or ``'a'`` -- calling  :meth:`writestr` on a ZipFile
		created with mode ``'r'``  will raise a :exc:`RuntimeError`.  Calling
		:meth:`writestr` on a closed ZipFile will raise a :exc:`RuntimeError`.
		
		If given, *compress_type* overrides the value given for the *compression*
		parameter to the constructor for the new entry, or in the *zinfo_or_arcname*
		(if that is a :class:`ZipInfo` instance).
		
		"""
		pass
		
	


class PyZipFile:


	"""
	Class for creating ZIP archives containing Python libraries.
	
	
	"""
	
	
	def __init__(self, ):
		pass
	
	def writepy(self, pathname,basename):
		"""
		Search for files :file:`\*.py` and add the corresponding file to the archive.
		The corresponding file is a :file:`\*.pyo` file if available, else a
		:file:`\*.pyc` file, compiling if necessary.  If the pathname is a file, the
		filename must end with :file:`.py`, and just the (corresponding
		:file:`\*.py[co]`) file is added at the top level (no path information).  If the
		pathname is a file that does not end with :file:`.py`, a :exc:`RuntimeError`
		will be raised.  If it is a directory, and the directory is not a package
		directory, then all the files :file:`\*.py[co]` are added at the top level.  If
		the directory is a package directory, then all :file:`\*.py[co]` are added under
		the package name as a file path, and if any subdirectories are package
		directories, all of these are added recursively.  *basename* is intended for
		internal use only.  The :meth:`writepy` method makes archives with file names
		like this::
		
		string.pyc                                # Top level name
		test/__init__.pyc                         # Package directory
		test/test_support.pyc                          # Module test.test_support
		test/bogus/__init__.pyc                   # Subpackage directory
		test/bogus/myfile.pyc                     # Submodule test.bogus.myfile
		
		
		.. ipInfo Objects
		---------------
		
		Instances of the :class:`ZipInfo` class are returned by the :meth:`getinfo` and
		:meth:`infolist` methods of :class:`ZipFile` objects.  Each object stores
		information about a single member of the ZIP archive.
		
		Instances have the following attributes:
		
		
		"""
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
	
	
	def __init__(self, ):
		pass
	
	def is_zipfile(self, filename):
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
	
	
	def __init__(self, ):
		pass
	
	def close(self, ):
		"""
		Close the archive file.  You must call :meth:`close` before exiting your program
		or essential records will not be written.
		
		
		"""
		pass
		
	def getinfo(self, name):
		"""
		Return a :class:`ZipInfo` object with information about the archive member
		*name*.  Calling :meth:`getinfo` for a name not currently contained in the
		archive will raise a :exc:`KeyError`.
		
		
		"""
		pass
		
	def infolist(self, ):
		"""
		Return a list containing a :class:`ZipInfo` object for each member of the
		archive.  The objects are in the same order as their entries in the actual ZIP
		file on disk if an existing archive was opened.
		
		
		"""
		pass
		
	def namelist(self, ):
		"""
		Return a list of archive members by name.
		
		
		"""
		pass
		
	def open(self, name,mode,pwd):
		"""
		Extract a member from the archive as a file-like object (ZipExtFile). *name* is
		the name of the file in the archive, or a :class:`ZipInfo` object. The *mode*
		parameter, if included, must be one of the following: ``'r'`` (the  default),
		``'U'``, or ``'rU'``. Choosing ``'U'`` or  ``'rU'`` will enable universal newline
		support in the read-only object. *pwd* is the password used for encrypted files.
		Calling  :meth:`open` on a closed ZipFile will raise a  :exc:`RuntimeError`.
		
		"""
		pass
		
	def extract(self, member,path,pwd):
		"""
		Extract a member from the archive to the current working directory; *member*
		must be its full name or a :class:`ZipInfo` object).  Its file information is
		extracted as accurately as possible.  *path* specifies a different directory
		to extract to.  *member* can be a filename or a :class:`ZipInfo` object.
		*pwd* is the password used for encrypted files.
		
		"""
		pass
		
	def extractall(self, path,members,pwd):
		"""
		Extract all members from the archive to the current working directory.  *path*
		specifies a different directory to extract to.  *members* is optional and must
		be a subset of the list returned by :meth:`namelist`.  *pwd* is the password
		used for encrypted files.
		
		"""
		pass
		
	def printdir(self, ):
		"""
		Print a table of contents for the archive to ``sys.stdout``.
		
		
		"""
		pass
		
	def setpassword(self, pwd):
		"""
		Set *pwd* as default password to extract encrypted files.
		
		"""
		pass
		
	def read(self, name,pwd):
		"""
		Return the bytes of the file *name* in the archive.  *name* is the name of the
		file in the archive, or a :class:`ZipInfo` object.  The archive must be open for
		read or append. *pwd* is the password used for encrypted  files and, if specified,
		it will override the default password set with :meth:`setpassword`.  Calling
		:meth:`read` on a closed ZipFile  will raise a :exc:`RuntimeError`.
		
		"""
		pass
		
	def testzip(self, ):
		"""
		Read all the files in the archive and check their CRC's and file headers.
		Return the name of the first bad file, or else return ``None``. Calling
		:meth:`testzip` on a closed ZipFile will raise a :exc:`RuntimeError`.
		
		
		"""
		pass
		
	def write(self, filename,arcname,compress_type):
		"""
		Write the file named *filename* to the archive, giving it the archive name
		*arcname* (by default, this will be the same as *filename*, but without a drive
		letter and with leading path separators removed).  If given, *compress_type*
		overrides the value given for the *compression* parameter to the constructor for
		the new entry.  The archive must be open with mode ``'w'`` or ``'a'`` -- calling
		:meth:`write` on a ZipFile created with mode ``'r'`` will raise a
		:exc:`RuntimeError`.  Calling  :meth:`write` on a closed ZipFile will raise a
		:exc:`RuntimeError`.
		
		"""
		pass
		
	def writestr(self, zinfo_or_arcname,bytes,compress_type):
		"""
		Write the string *bytes* to the archive; *zinfo_or_arcname* is either the file
		name it will be given in the archive, or a :class:`ZipInfo` instance.  If it's
		an instance, at least the filename, date, and time must be given.  If it's a
		name, the date and time is set to the current date and time. The archive must be
		opened with mode ``'w'`` or ``'a'`` -- calling  :meth:`writestr` on a ZipFile
		created with mode ``'r'``  will raise a :exc:`RuntimeError`.  Calling
		:meth:`writestr` on a closed ZipFile will raise a :exc:`RuntimeError`.
		
		If given, *compress_type* overrides the value given for the *compression*
		parameter to the constructor for the new entry, or in the *zinfo_or_arcname*
		(if that is a :class:`ZipInfo` instance).
		
		"""
		pass
		
	


