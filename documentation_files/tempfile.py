#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
""":synopsis: Generate temporary files and directories.


"""
"""
When set to a value other than ``None``, this variable defines the
default value for the *dir* argument to all the functions defined in this
module.

If ``tempdir`` is unset or ``None`` at any call to any of the above
functions, Python searches a standard list of directories and sets
*tempdir* to the first one which the calling user can create files in.
The list is:

#. The directory named by the :envvar:`TMPDIR` environment variable.

#. The directory named by the :envvar:`TEMP` environment variable.

#. The directory named by the :envvar:`TMP` environment variable.

#. A platform-specific location:

* On RiscOS, the directory named by the :envvar:`Wimp$ScrapDir` environment
variable.

* On Windows, the directories :file:`C:\\TEMP`, :file:`C:\\TMP`,
:file:`\\TEMP`, and :file:`\\TMP`, in that order.

* On all other platforms, the directories :file:`/tmp`, :file:`/var/tmp`, and
:file:`/usr/tmp`, in that order.

#. As a last resort, the current working directory.


"""
tempdir = None
"""
"""
template = None
def TemporaryFile(mode='w+b',bufsize=_1,suffix='',prefix='tmp',dir=None):
	"""
	Return a file-like object that can be used as a temporary storage area.
	The file is created using :func:`mkstemp`. It will be destroyed as soon
	as it is closed (including an implicit close when the object is garbage
	collected).  Under Unix, the directory entry for the file is removed
	immediately after the file is created.  Other platforms do not support
	this; your code should not rely on a temporary file created using this
	function having or not having a visible name in the file system.
	
	The *mode* parameter defaults to ``'w+b'`` so that the file created can
	be read and written without being closed.  Binary mode is used so that it
	behaves consistently on all platforms without regard for the data that is
	stored.  *bufsize* defaults to ``-1``, meaning that the operating system
	default is used.
	
	The *dir*, *prefix* and *suffix* parameters are passed to :func:`mkstemp`.
	
	The returned object is a true file object on POSIX platforms.  On other
	platforms, it is a file-like object whose :attr:`!file` attribute is the
	underlying true file object. This file-like object can be used in a
	:keyword:`with` statement, just like a normal file.
	
	
	"""
	pass
	
def NamedTemporaryFile(mode='w+b',bufsize=_1,suffix='',prefix='tmp',dir=None,delete=True):
	"""
	This function operates exactly as :func:`TemporaryFile` does, except that
	the file is guaranteed to have a visible name in the file system (on
	Unix, the directory entry is not unlinked).  That name can be retrieved
	from the :attr:`name` member of the file object.  Whether the name can be
	used to open the file a second time, while the named temporary file is
	still open, varies across platforms (it can be so used on Unix; it cannot
	on Windows NT or later).  If *delete* is true (the default), the file is
	deleted as soon as it is closed.
	
	The returned object is always a file-like object whose :attr:`!file`
	attribute is the underlying true file object. This file-like object can
	be used in a :keyword:`with` statement, just like a normal file.
	
	"""
	pass
	
def SpooledTemporaryFile(max_size=0,mode='w+b',bufsize=_1,suffix='',prefix='tmp',dir=None):
	"""
	This function operates exactly as :func:`TemporaryFile` does, except that
	data is spooled in memory until the file size exceeds *max_size*, or
	until the file's :func:`fileno` method is called, at which point the
	contents are written to disk and operation proceeds as with
	:func:`TemporaryFile`.
	
	The resulting file has one additional method, :func:`rollover`, which
	causes the file to roll over to an on-disk file regardless of its size.
	
	The returned object is a file-like object whose :attr:`_file` attribute
	is either a :class:`StringIO` object or a true file object, depending on
	whether :func:`rollover` has been called. This file-like object can be
	used in a :keyword:`with` statement, just like a normal file.
	
	"""
	pass
	
def mkstemp(suffix='',prefix='tmp',dir=None,text=False):
	"""
	Creates a temporary file in the most secure manner possible.  There are
	no race conditions in the file's creation, assuming that the platform
	properly implements the :const:`os.O_EXCL` flag for :func:`os.open`.  The
	file is readable and writable only by the creating user ID.  If the
	platform uses permission bits to indicate whether a file is executable,
	the file is executable by no one.  The file descriptor is not inherited
	by child processes.
	
	Unlike :func:`TemporaryFile`, the user of :func:`mkstemp` is responsible
	for deleting the temporary file when done with it.
	
	If *suffix* is specified, the file name will end with that suffix,
	otherwise there will be no suffix.  :func:`mkstemp` does not put a dot
	between the file name and the suffix; if you need one, put it at the
	beginning of *suffix*.
	
	If *prefix* is specified, the file name will begin with that prefix;
	otherwise, a default prefix is used.
	
	If *dir* is specified, the file will be created in that directory;
	otherwise, a default directory is used.  The default directory is chosen
	from a platform-dependent list, but the user of the application can
	control the directory location by setting the *TMPDIR*, *TEMP* or *TMP*
	environment variables.  There is thus no guarantee that the generated
	filename will have any nice properties, such as not requiring quoting
	when passed to external commands via ``os.popen()``.
	
	If *text* is specified, it indicates whether to open the file in binary
	mode (the default) or text mode.  On some platforms, this makes no
	difference.
	
	:func:`mkstemp` returns a tuple containing an OS-level handle to an open
	file (as would be returned by :func:`os.open`) and the absolute pathname
	of that file, in that order.
	
	"""
	pass
	
def mkdtemp(suffix='',prefix='tmp',dir=None):
	"""
	Creates a temporary directory in the most secure manner possible. There
	are no race conditions in the directory's creation.  The directory is
	readable, writable, and searchable only by the creating user ID.
	
	The user of :func:`mkdtemp` is responsible for deleting the temporary
	directory and its contents when done with it.
	
	The *prefix*, *suffix*, and *dir* arguments are the same as for
	:func:`mkstemp`.
	
	:func:`mkdtemp` returns the absolute pathname of the new directory.
	
	"""
	pass
	
def mktemp(suffix='',prefix='tmp',dir=None):
	"""
	"""
	pass
	
def gettempdir():
	"""
	Return the directory currently selected to create temporary files in. If
	:data:`tempdir` is not ``None``, this simply returns its contents; otherwise,
	the search described above is performed, and the result returned.
	
	"""
	pass
	
def gettempprefix():
	"""
	Return the filename prefix used to create temporary files.  This does not
	contain the directory component.  Using this function is preferred over reading
	the *template* variable directly.
	
	"""
	pass
	
