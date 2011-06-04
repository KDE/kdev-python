#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
""":synopsis: Miscellaneous operating system interfaces.


This module provides a portable way of using operating system dependent
functionality.  If you just want to read or write a file see :func:`open`, if
you want to manipulate paths, see the :mod:`os.path` module, and if you want to
read all the lines in all the files on the command line see the :mod:`fileinput`
module.  For creating temporary files and directories see the :mod:`tempfile`
module, and for high-level file and directory handling see the :mod:`shutil`
module.

Notes on the availability of these functions:

* The design of all built-in operating system dependent modules of Python is
such that as long as the same functionality is available, it uses the same
interface; for example, the function ``os.stat(path)`` returns stat
information about *path* in the same format (which happens to have originated
with the POSIX interface).

* Extensions peculiar to a particular operating system are also available
through the :mod:`os` module, but using them is of course a threat to
portability.

* An "Availability: Unix" note means that this function is commonly found on
Unix systems.  It does not make any claims about its existence on a specific
operating system.

* If not separately noted, all functions that claim "Availability: Unix" are
supported on Mac OS X, which builds on a Unix core.

.. et their own line and occur at the end of the function
"""
"""
The name of the operating system dependent module imported.  The following
names have currently been registered: ``'posix'``, ``'nt'``,
``'os2'``, ``'ce'``, ``'java'``, ``'riscos'``.


.. rocess Parameters
------------------

These functions and data items provide information and operate on the current
process and user.


"""
name = None
"""
A mapping object representing the string environment. For example,
``environ['HOME']`` is the pathname of your home directory (on some platforms),
and is equivalent to ``getenv("HOME")`` in C.

This mapping is captured the first time the :mod:`os` module is imported,
typically during Python startup as part of processing :file:`site.py`.  Changes
to the environment made after this time are not reflected in ``os.environ``,
except for changes made by modifying ``os.environ`` directly.

If the platform supports the :func:`putenv` function, this mapping may be used
to modify the environment as well as query the environment.  :func:`putenv` will
be called automatically when the mapping is modified.

"""
environ = None
"""SEEK_CUR
SEEK_END

Parameters to the :func:`lseek` function. Their values are 0, 1, and 2,
respectively.

Availability: Windows, Unix.

"""
SEEK_SET = None
"""O_WRONLY
O_RDWR
O_APPEND
O_CREAT
O_EXCL
O_TRUNC

These constants are available on Unix and Windows.


"""
O_RDONLY = None
"""O_RSYNC
O_SYNC
O_NDELAY
O_NONBLOCK
O_NOCTTY
O_SHLOCK
O_EXLOCK

These constants are only available on Unix.


"""
O_DSYNC = None
"""O_NOINHERIT
O_SHORT_LIVED
O_TEMPORARY
O_RANDOM
O_SEQUENTIAL
O_TEXT

These constants are only available on Windows.


"""
O_BINARY = None
"""O_DIRECT
O_DIRECTORY
O_NOFOLLOW
O_NOATIME

These constants are GNU extensions and not present if they are not defined by
the C library.


.. iles and Directories
---------------------

"""
O_ASYNC = None
"""
Value to pass as the *mode* parameter of :func:`access` to test the existence of
*path*.


"""
F_OK = None
"""
Value to include in the *mode* parameter of :func:`access` to test the
readability of *path*.


"""
R_OK = None
"""
Value to include in the *mode* parameter of :func:`access` to test the
writability of *path*.


"""
W_OK = None
"""
Value to include in the *mode* parameter of :func:`access` to determine if
*path* can be executed.


"""
X_OK = None
"""
Dictionary mapping names accepted by :func:`pathconf` and :func:`fpathconf` to
the integer values defined for those names by the host operating system.  This
can be used to determine the set of names known to the system. Availability:
Unix.


"""
pathconf_names = None
"""
The maximum number of unique names that :func:`tmpnam` will generate before
reusing names.


"""
TMP_MAX = None
"""
Exit code that means no error occurred.

Availability: Unix.

"""
EX_OK = None
"""
Exit code that means the command was used incorrectly, such as when the wrong
number of arguments are given.

Availability: Unix.

"""
EX_USAGE = None
"""
Exit code that means the input data was incorrect.

Availability: Unix.

"""
EX_DATAERR = None
"""
Exit code that means an input file did not exist or was not readable.

Availability: Unix.

"""
EX_NOINPUT = None
"""
Exit code that means a specified user did not exist.

Availability: Unix.

"""
EX_NOUSER = None
"""
Exit code that means a specified host did not exist.

Availability: Unix.

"""
EX_NOHOST = None
"""
Exit code that means that a required service is unavailable.

Availability: Unix.

"""
EX_UNAVAILABLE = None
"""
Exit code that means an internal software error was detected.

Availability: Unix.

"""
EX_SOFTWARE = None
"""
Exit code that means an operating system error was detected, such as the
inability to fork or create a pipe.

Availability: Unix.

"""
EX_OSERR = None
"""
Exit code that means some system file did not exist, could not be opened, or had
some other kind of error.

Availability: Unix.

"""
EX_OSFILE = None
"""
Exit code that means a user specified output file could not be created.

Availability: Unix.

"""
EX_CANTCREAT = None
"""
Exit code that means that an error occurred while doing I/O on some file.

Availability: Unix.

"""
EX_IOERR = None
"""
Exit code that means a temporary failure occurred.  This indicates something
that may not really be an error, such as a network connection that couldn't be
made during a retryable operation.

Availability: Unix.

"""
EX_TEMPFAIL = None
"""
Exit code that means that a protocol exchange was illegal, invalid, or not
understood.

Availability: Unix.

"""
EX_PROTOCOL = None
"""
Exit code that means that there were insufficient permissions to perform the
operation (but not intended for file system problems).

Availability: Unix.

"""
EX_NOPERM = None
"""
Exit code that means that some kind of configuration error occurred.

Availability: Unix.

"""
EX_CONFIG = None
"""
Exit code that means something like "an entry was not found".

Availability: Unix.

"""
EX_NOTFOUND = None
"""P_NOWAITO

Possible values for the *mode* parameter to the :func:`spawn\*` family of
functions.  If either of these values is given, the :func:`spawn\*` functions
will return as soon as the new process has been created, with the process id as
the return value.

Availability: Unix, Windows.

"""
P_NOWAIT = None
"""
Possible value for the *mode* parameter to the :func:`spawn\*` family of
functions.  If this is given as *mode*, the :func:`spawn\*` functions will not
return until the new process has run to completion and will return the exit code
of the process the run is successful, or ``-signal`` if a signal kills the
process.

Availability: Unix, Windows.

"""
P_WAIT = None
"""P_OVERLAY

Possible values for the *mode* parameter to the :func:`spawn\*` family of
functions.  These are less portable than those listed above. :const:`P_DETACH`
is similar to :const:`P_NOWAIT`, but the new process is detached from the
console of the calling process. If :const:`P_OVERLAY` is used, the current
process will be replaced; the :func:`spawn\*` function will not return.

Availability: Windows.

"""
P_DETACH = None
"""
The option for :func:`waitpid` to return immediately if no child process status
is available immediately. The function returns ``(0, 0)`` in this case.

Availability: Unix.


"""
WNOHANG = None
"""
This option causes child processes to be reported if they have been continued
from a job control stop since their status was last reported.

Availability: Some Unix systems.

"""
WCONTINUED = None
"""
This option causes child processes to be reported if they have been stopped but
their current state has not been reported since they were stopped.

Availability: Unix.

"""
WUNTRACED = None
"""
Dictionary mapping names accepted by :func:`confstr` to the integer values
defined for those names by the host operating system. This can be used to
determine the set of names known to the system.

Availability: Unix.


"""
confstr_names = None
"""
Dictionary mapping names accepted by :func:`sysconf` to the integer values
defined for those names by the host operating system. This can be used to
determine the set of names known to the system.

Availability: Unix.

The following data values are used to support path manipulation operations.  These
are defined for all platforms.

Higher-level operations on pathnames are defined in the :mod:`os.path` module.


"""
sysconf_names = None
"""
The constant string used by the operating system to refer to the current
directory. This is ``'.'`` for Windows and POSIX. Also available via
:mod:`os.path`.


"""
curdir = None
"""
The constant string used by the operating system to refer to the parent
directory. This is ``'..'`` for Windows and POSIX. Also available via
:mod:`os.path`.


"""
pardir = None
"""
The character used by the operating system to separate pathname components.
This is ``'/'`` for POSIX and ``'\\'`` for Windows.  Note that knowing this
is not sufficient to be able to parse or concatenate pathnames --- use
:func:`os.path.split` and :func:`os.path.join` --- but it is occasionally
useful. Also available via :mod:`os.path`.


"""
sep = None
"""
An alternative character used by the operating system to separate pathname
components, or ``None`` if only one separator character exists.  This is set to
``'/'`` on Windows systems where ``sep`` is a backslash. Also available via
:mod:`os.path`.


"""
altsep = None
"""
The character which separates the base filename from the extension; for example,
the ``'.'`` in :file:`os.py`. Also available via :mod:`os.path`.

"""
extsep = None
"""
The character conventionally used by the operating system to separate search
path components (as in :envvar:`PATH`), such as ``':'`` for POSIX or ``';'`` for
Windows. Also available via :mod:`os.path`.


"""
pathsep = None
"""
The default search path used by :func:`exec\*p\*` and :func:`spawn\*p\*` if the
environment doesn't have a ``'PATH'`` key. Also available via :mod:`os.path`.


"""
defpath = None
"""
The string used to separate (or, rather, terminate) lines on the current
platform.  This may be a single character, such as ``'\n'`` for POSIX, or
multiple characters, for example, ``'\r\n'`` for Windows. Do not use
*os.linesep* as a line terminator when writing files opened in text mode (the
default); use a single ``'\n'`` instead, on all platforms.


"""
linesep = None
"""
The file path of the null device. For example: ``'/dev/null'`` for
POSIX, ``'nul'`` for Windows.  Also available via :mod:`os.path`.

"""
devnull = None
def chdir(path):
	"""fchdir(fd)
	getcwd()
	:noindex:
	
	These functions are described in :ref:`os-file-dir`.
	
	
	"""
	pass
	
def ctermid():
	"""
	Return the filename corresponding to the controlling terminal of the process.
	
	Availability: Unix.
	
	
	"""
	pass
	
def getegid():
	"""
	Return the effective group id of the current process.  This corresponds to the
	"set id" bit on the file being executed in the current process.
	
	Availability: Unix.
	
	
	"""
	pass
	
def geteuid():
	"""
	"""
	pass
	
def getgid():
	"""
	"""
	pass
	
def getgroups():
	"""
	Return list of supplemental group ids associated with the current process.
	
	Availability: Unix.
	
	
	"""
	pass
	
def initgroups(username,gid):
	"""
	Call the system initgroups() to initialize the group access list with all of
	the groups of which the specified username is a member, plus the specified
	group id.
	
	Availability: Unix.
	
	"""
	pass
	
def getlogin():
	"""
	Return the name of the user logged in on the controlling terminal of the
	process.  For most purposes, it is more useful to use the environment variable
	:envvar:`LOGNAME` to find out who the user is, or
	``pwd.getpwuid(os.getuid())[0]`` to get the login name of the currently
	effective user id.
	
	Availability: Unix.
	
	
	"""
	pass
	
def getpgid(pid):
	"""
	Return the process group id of the process with process id *pid*. If *pid* is 0,
	the process group id of the current process is returned.
	
	Availability: Unix.
	
	"""
	pass
	
def getpgrp():
	"""
	"""
	pass
	
def getpid():
	"""
	"""
	pass
	
def getppid():
	"""
	"""
	pass
	
def getresuid():
	"""
	Return a tuple (ruid, euid, suid) denoting the current process's
	real, effective, and saved user ids.
	
	Availability: Unix.
	
	"""
	pass
	
def getresgid():
	"""
	Return a tuple (rgid, egid, sgid) denoting the current process's
	real, effective, and saved group ids.
	
	Availability: Unix.
	
	"""
	pass
	
def getuid():
	"""
	"""
	pass
	
def getenv(varname,value):
	"""
	Return the value of the environment variable *varname* if it exists, or *value*
	if it doesn't.  *value* defaults to ``None``.
	
	Availability: most flavors of Unix, Windows.
	
	
	"""
	pass
	
def putenv(varname,value):
	"""
	"""
	pass
	
def setegid(egid):
	"""
	Set the current process's effective group id.
	
	Availability: Unix.
	
	
	"""
	pass
	
def seteuid(euid):
	"""
	Set the current process's effective user id.
	
	Availability: Unix.
	
	
	"""
	pass
	
def setgid(gid):
	"""
	Set the current process' group id.
	
	Availability: Unix.
	
	
	"""
	pass
	
def setgroups(groups):
	"""
	Set the list of supplemental group ids associated with the current process to
	*groups*. *groups* must be a sequence, and each element must be an integer
	identifying a group. This operation is typically available only to the superuser.
	
	Availability: Unix.
	
	"""
	pass
	
def setpgrp():
	"""
	Call the system call :cfunc:`setpgrp` or :cfunc:`setpgrp(0, 0)` depending on
	which version is implemented (if any).  See the Unix manual for the semantics.
	
	Availability: Unix.
	
	
	"""
	pass
	
def setpgid(pid,pgrp):
	"""
	Call the system call :cfunc:`setpgid` to set the process group id of the
	process with id *pid* to the process group with id *pgrp*.  See the Unix manual
	for the semantics.
	
	Availability: Unix.
	
	
	"""
	pass
	
def setregid(rgid,egid):
	"""
	Set the current process's real and effective group ids.
	
	Availability: Unix.
	
	
	"""
	pass
	
def setresgid(rgid,egid,sgid):
	"""
	Set the current process's real, effective, and saved group ids.
	
	Availability: Unix.
	
	"""
	pass
	
def setresuid(ruid,euid,suid):
	"""
	Set the current process's real, effective, and saved user ids.
	
	Availability: Unix.
	
	"""
	pass
	
def setreuid(ruid,euid):
	"""
	Set the current process's real and effective user ids.
	
	Availability: Unix.
	
	
	"""
	pass
	
def getsid(pid):
	"""
	Call the system call :cfunc:`getsid`.  See the Unix manual for the semantics.
	
	Availability: Unix.
	
	"""
	pass
	
def setsid():
	"""
	Call the system call :cfunc:`setsid`.  See the Unix manual for the semantics.
	
	Availability: Unix.
	
	
	"""
	pass
	
def setuid(uid):
	"""
	"""
	pass
	
def strerror(code):
	"""
	Return the error message corresponding to the error code in *code*.
	On platforms where :cfunc:`strerror` returns ``NULL`` when given an unknown
	error number, :exc:`ValueError` is raised.
	
	Availability: Unix, Windows.
	
	
	"""
	pass
	
def umask(mask):
	"""
	Set the current numeric umask and return the previous umask.
	
	Availability: Unix, Windows.
	
	
	"""
	pass
	
def uname():
	"""
	"""
	pass
	
def unsetenv(varname):
	"""
	"""
	pass
	
def fdopen(fd,mode,bufsize):
	"""
	"""
	pass
	
def popen(command,mode,bufsize):
	"""
	Open a pipe to or from *command*.  The return value is an open file object
	connected to the pipe, which can be read or written depending on whether *mode*
	is ``'r'`` (default) or ``'w'``. The *bufsize* argument has the same meaning as
	the corresponding argument to the built-in :func:`open` function.  The exit
	status of the command (encoded in the format specified for :func:`wait`) is
	available as the return value of the :meth:`~file.close` method of the file object,
	except that when the exit status is zero (termination without errors), ``None``
	is returned.
	
	Availability: Unix, Windows.
	
	"""
	pass
	
def tmpfile():
	"""
	Return a new file object opened in update mode (``w+b``).  The file has no
	directory entries associated with it and will be automatically deleted once
	there are no file descriptors for the file.
	
	Availability: Unix, Windows.
	
	There are a number of different :func:`popen\*` functions that provide slightly
	different ways to create subprocesses.
	
	"""
	pass
	
def popen2(cmd,mode,bufsize):
	"""
	Execute *cmd* as a sub-process and return the file objects ``(child_stdin,
	child_stdout)``.
	
	"""
	pass
	
def popen3(cmd,mode,bufsize):
	"""
	Execute *cmd* as a sub-process and return the file objects ``(child_stdin,
	child_stdout, child_stderr)``.
	
	"""
	pass
	
def popen4(cmd,mode,bufsize):
	"""
	Execute *cmd* as a sub-process and return the file objects ``(child_stdin,
	child_stdout_and_stderr)``.
	
	"""
	pass
	
def close(fd):
	"""
	Close file descriptor *fd*.
	
	Availability: Unix, Windows.
	
	"""
	pass
	
def closerange(fd_low,fd_high):
	"""
	Close all file descriptors from *fd_low* (inclusive) to *fd_high* (exclusive),
	ignoring errors. Equivalent to::
	
	for fd in xrange(fd_low, fd_high):
	try:
	os.close(fd)
	except OSError:
	pass
	
	Availability: Unix, Windows.
	
	"""
	pass
	
def dup(fd):
	"""
	Return a duplicate of file descriptor *fd*.
	
	Availability: Unix, Windows.
	
	
	"""
	pass
	
def dup2(fd,fd2):
	"""
	Duplicate file descriptor *fd* to *fd2*, closing the latter first if necessary.
	
	Availability: Unix, Windows.
	
	
	"""
	pass
	
def fchmod(fd,mode):
	"""
	Change the mode of the file given by *fd* to the numeric *mode*.  See the docs
	for :func:`chmod` for possible values of *mode*.
	
	Availability: Unix.
	
	"""
	pass
	
def fchown(fd,uid,gid):
	"""
	Change the owner and group id of the file given by *fd* to the numeric *uid*
	and *gid*.  To leave one of the ids unchanged, set it to -1.
	
	Availability: Unix.
	
	"""
	pass
	
def fdatasync(fd):
	"""
	Force write of file with filedescriptor *fd* to disk. Does not force update of
	metadata.
	
	Availability: Unix.
	
	"""
	pass
	
def fpathconf(fd,name):
	"""
	Return system configuration information relevant to an open file. *name*
	specifies the configuration value to retrieve; it may be a string which is the
	name of a defined system value; these names are specified in a number of
	standards (POSIX.1, Unix 95, Unix 98, and others).  Some platforms define
	additional names as well.  The names known to the host operating system are
	given in the ``pathconf_names`` dictionary.  For configuration variables not
	included in that mapping, passing an integer for *name* is also accepted.
	
	If *name* is a string and is not known, :exc:`ValueError` is raised.  If a
	specific value for *name* is not supported by the host system, even if it is
	included in ``pathconf_names``, an :exc:`OSError` is raised with
	:const:`errno.EINVAL` for the error number.
	
	Availability: Unix.
	
	
	"""
	pass
	
def fstat(fd):
	"""
	Return status for file descriptor *fd*, like :func:`~os.stat`.
	
	Availability: Unix, Windows.
	
	
	"""
	pass
	
def fstatvfs(fd):
	"""
	Return information about the filesystem containing the file associated with file
	descriptor *fd*, like :func:`statvfs`.
	
	Availability: Unix.
	
	
	"""
	pass
	
def fsync(fd):
	"""
	Force write of file with filedescriptor *fd* to disk.  On Unix, this calls the
	native :cfunc:`fsync` function; on Windows, the MS :cfunc:`_commit` function.
	
	If you're starting with a Python file object *f*, first do ``f.flush()``, and
	then do ``os.fsync(f.fileno())``, to ensure that all internal buffers associated
	with *f* are written to disk.
	
	Availability: Unix, and Windows starting in 2.2.3.
	
	
	"""
	pass
	
def ftruncate(fd,length):
	"""
	Truncate the file corresponding to file descriptor *fd*, so that it is at most
	*length* bytes in size.
	
	Availability: Unix.
	
	
	"""
	pass
	
def isatty(fd):
	"""
	Return ``True`` if the file descriptor *fd* is open and connected to a
	tty(-like) device, else ``False``.
	
	Availability: Unix.
	
	
	"""
	pass
	
def lseek(fd,pos,how):
	"""
	Set the current position of file descriptor *fd* to position *pos*, modified
	by *how*: :const:`SEEK_SET` or ``0`` to set the position relative to the
	beginning of the file; :const:`SEEK_CUR` or ``1`` to set it relative to the
	current position; :const:`os.SEEK_END` or ``2`` to set it relative to the end of
	the file.
	
	Availability: Unix, Windows.
	
	
	"""
	pass
	
def open(file,flags,mode):
	"""
	Open the file *file* and set various flags according to *flags* and possibly its
	mode according to *mode*. The default *mode* is ``0777`` (octal), and the
	current umask value is first masked out.  Return the file descriptor for the
	newly opened file.
	
	For a description of the flag and mode values, see the C run-time documentation;
	flag constants (like :const:`O_RDONLY` and :const:`O_WRONLY`) are defined in
	this module too (see :ref:`open-constants`).  In particular, on Windows adding
	:const:`O_BINARY` is needed to open files in binary mode.
	
	Availability: Unix, Windows.
	
	"""
	pass
	
def openpty():
	"""
	"""
	pass
	
def pipe():
	"""
	Create a pipe.  Return a pair of file descriptors ``(r, w)`` usable for reading
	and writing, respectively.
	
	Availability: Unix, Windows.
	
	
	"""
	pass
	
def read(fd,n):
	"""
	Read at most *n* bytes from file descriptor *fd*. Return a string containing the
	bytes read.  If the end of the file referred to by *fd* has been reached, an
	empty string is returned.
	
	Availability: Unix, Windows.
	
	"""
	pass
	
def tcgetpgrp(fd):
	"""
	Return the process group associated with the terminal given by *fd* (an open
	file descriptor as returned by :func:`os.open`).
	
	Availability: Unix.
	
	
	"""
	pass
	
def tcsetpgrp(fd,pg):
	"""
	Set the process group associated with the terminal given by *fd* (an open file
	descriptor as returned by :func:`os.open`) to *pg*.
	
	Availability: Unix.
	
	
	"""
	pass
	
def ttyname(fd):
	"""
	Return a string which specifies the terminal device associated with
	file descriptor *fd*.  If *fd* is not associated with a terminal device, an
	exception is raised.
	
	Availability: Unix.
	
	
	"""
	pass
	
def write(fd,str):
	"""
	Write the string *str* to file descriptor *fd*. Return the number of bytes
	actually written.
	
	Availability: Unix, Windows.
	
	"""
	pass
	
def access(path,mode):
	"""
	Use the real uid/gid to test for access to *path*.  Note that most operations
	will use the effective uid/gid, therefore this routine can be used in a
	suid/sgid environment to test if the invoking user has the specified access to
	*path*.  *mode* should be :const:`F_OK` to test the existence of *path*, or it
	can be the inclusive OR of one or more of :const:`R_OK`, :const:`W_OK`, and
	:const:`X_OK` to test permissions.  Return :const:`True` if access is allowed,
	:const:`False` if not. See the Unix man page :manpage:`access(2)` for more
	information.
	
	Availability: Unix, Windows.
	
	"""
	pass
	
def chdir(path):
	"""
	"""
	pass
	
def fchdir(fd):
	"""
	Change the current working directory to the directory represented by the file
	descriptor *fd*.  The descriptor must refer to an opened directory, not an open
	file.
	
	Availability: Unix.
	
	"""
	pass
	
def getcwd():
	"""
	Return a string representing the current working directory.
	
	Availability: Unix, Windows.
	
	
	"""
	pass
	
def getcwdu():
	"""
	Return a Unicode object representing the current working directory.
	
	Availability: Unix, Windows.
	
	"""
	pass
	
def chflags(path,flags):
	"""
	Set the flags of *path* to the numeric *flags*. *flags* may take a combination
	(bitwise OR) of the following values (as defined in the :mod:`stat` module):
	
	* :data:`stat.UF_NODUMP`
	* :data:`stat.UF_IMMUTABLE`
	* :data:`stat.UF_APPEND`
	* :data:`stat.UF_OPAQUE`
	* :data:`stat.UF_NOUNLINK`
	* :data:`stat.SF_ARCHIVED`
	* :data:`stat.SF_IMMUTABLE`
	* :data:`stat.SF_APPEND`
	* :data:`stat.SF_NOUNLINK`
	* :data:`stat.SF_SNAPSHOT`
	
	Availability: Unix.
	
	"""
	pass
	
def chroot(path):
	"""
	Change the root directory of the current process to *path*. Availability:
	Unix.
	
	"""
	pass
	
def chmod(path,mode):
	"""
	Change the mode of *path* to the numeric *mode*. *mode* may take one of the
	following values (as defined in the :mod:`stat` module) or bitwise ORed
	combinations of them:
	
	
	* :data:`stat.S_ISUID`
	* :data:`stat.S_ISGID`
	* :data:`stat.S_ENFMT`
	* :data:`stat.S_ISVTX`
	* :data:`stat.S_IREAD`
	* :data:`stat.S_IWRITE`
	* :data:`stat.S_IEXEC`
	* :data:`stat.S_IRWXU`
	* :data:`stat.S_IRUSR`
	* :data:`stat.S_IWUSR`
	* :data:`stat.S_IXUSR`
	* :data:`stat.S_IRWXG`
	* :data:`stat.S_IRGRP`
	* :data:`stat.S_IWGRP`
	* :data:`stat.S_IXGRP`
	* :data:`stat.S_IRWXO`
	* :data:`stat.S_IROTH`
	* :data:`stat.S_IWOTH`
	* :data:`stat.S_IXOTH`
	
	Availability: Unix, Windows.
	
	"""
	pass
	
def chown(path,uid,gid):
	"""
	Change the owner and group id of *path* to the numeric *uid* and *gid*. To leave
	one of the ids unchanged, set it to -1.
	
	Availability: Unix.
	
	
	"""
	pass
	
def lchflags(path,flags):
	"""
	Set the flags of *path* to the numeric *flags*, like :func:`chflags`, but do not
	follow symbolic links.
	
	Availability: Unix.
	
	"""
	pass
	
def lchmod(path,mode):
	"""
	Change the mode of *path* to the numeric *mode*. If path is a symlink, this
	affects the symlink rather than the target. See the docs for :func:`chmod`
	for possible values of *mode*.
	
	Availability: Unix.
	
	"""
	pass
	
def lchown(path,uid,gid):
	"""
	Change the owner and group id of *path* to the numeric *uid* and *gid*. This
	function will not follow symbolic links.
	
	Availability: Unix.
	
	"""
	pass
	
def link(source,link_name):
	"""
	Create a hard link pointing to *source* named *link_name*.
	
	Availability: Unix.
	
	
	"""
	pass
	
def listdir(path):
	"""
	Return a list containing the names of the entries in the directory given by
	*path*.  The list is in arbitrary order.  It does not include the special
	entries ``'.'`` and ``'..'`` even if they are present in the
	directory.
	
	Availability: Unix, Windows.
	
	"""
	pass
	
def lstat(path):
	"""
	Perform the equivalent of an :cfunc:`lstat` system call on the given path.
	Similar to :func:`~os.stat`, but does not follow symbolic links.  On
	platforms that do not support symbolic links, this is an alias for
	:func:`~os.stat`.
	
	
	"""
	pass
	
def mkfifo(path,mode):
	"""
	Create a FIFO (a named pipe) named *path* with numeric mode *mode*.  The default
	*mode* is ``0666`` (octal).  The current umask value is first masked out from
	the mode.
	
	Availability: Unix.
	
	FIFOs are pipes that can be accessed like regular files.  FIFOs exist until they
	are deleted (for example with :func:`os.unlink`). Generally, FIFOs are used as
	rendezvous between "client" and "server" type processes: the server opens the
	FIFO for reading, and the client opens it for writing.  Note that :func:`mkfifo`
	doesn't open the FIFO --- it just creates the rendezvous point.
	
	
	"""
	pass
	
def mknod(filename,mode=0600,device):
	"""
	Create a filesystem node (file, device special file or named pipe) named
	*filename*. *mode* specifies both the permissions to use and the type of node to
	be created, being combined (bitwise OR) with one of ``stat.S_IFREG``,
	``stat.S_IFCHR``, ``stat.S_IFBLK``,
	and ``stat.S_IFIFO`` (those constants are available in :mod:`stat`).
	For ``stat.S_IFCHR`` and
	``stat.S_IFBLK``, *device* defines the newly created device special file (probably using
	:func:`os.makedev`), otherwise it is ignored.
	
	"""
	pass
	
def major(device):
	"""
	Extract the device major number from a raw device number (usually the
	:attr:`st_dev` or :attr:`st_rdev` field from :ctype:`stat`).
	
	"""
	pass
	
def minor(device):
	"""
	Extract the device minor number from a raw device number (usually the
	:attr:`st_dev` or :attr:`st_rdev` field from :ctype:`stat`).
	
	"""
	pass
	
def makedev(major,minor):
	"""
	Compose a raw device number from the major and minor device numbers.
	
	"""
	pass
	
def mkdir(path,mode):
	"""
	Create a directory named *path* with numeric mode *mode*. The default *mode* is
	``0777`` (octal).  On some systems, *mode* is ignored.  Where it is used, the
	current umask value is first masked out.  If the directory already exists,
	:exc:`OSError` is raised.
	
	It is also possible to create temporary directories; see the
	:mod:`tempfile` module's :func:`tempfile.mkdtemp` function.
	
	Availability: Unix, Windows.
	
	
	"""
	pass
	
def makedirs(path,mode):
	"""
	"""
	pass
	
def pathconf(path,name):
	"""
	Return system configuration information relevant to a named file. *name*
	specifies the configuration value to retrieve; it may be a string which is the
	name of a defined system value; these names are specified in a number of
	standards (POSIX.1, Unix 95, Unix 98, and others).  Some platforms define
	additional names as well.  The names known to the host operating system are
	given in the ``pathconf_names`` dictionary.  For configuration variables not
	included in that mapping, passing an integer for *name* is also accepted.
	
	If *name* is a string and is not known, :exc:`ValueError` is raised.  If a
	specific value for *name* is not supported by the host system, even if it is
	included in ``pathconf_names``, an :exc:`OSError` is raised with
	:const:`errno.EINVAL` for the error number.
	
	Availability: Unix.
	
	
	"""
	pass
	
def readlink(path):
	"""
	Return a string representing the path to which the symbolic link points.  The
	result may be either an absolute or relative pathname; if it is relative, it may
	be converted to an absolute pathname using ``os.path.join(os.path.dirname(path),
	result)``.
	
	"""
	pass
	
def remove(path):
	"""
	Remove (delete) the file *path*.  If *path* is a directory, :exc:`OSError` is
	raised; see :func:`rmdir` below to remove a directory.  This is identical to
	the :func:`unlink` function documented below.  On Windows, attempting to
	remove a file that is in use causes an exception to be raised; on Unix, the
	directory entry is removed but the storage allocated to the file is not made
	available until the original file is no longer in use.
	
	Availability: Unix, Windows.
	
	
	"""
	pass
	
def removedirs(path):
	"""
	"""
	pass
	
def rename(src,dst):
	"""
	Rename the file or directory *src* to *dst*.  If *dst* is a directory,
	:exc:`OSError` will be raised.  On Unix, if *dst* exists and is a file, it will
	be replaced silently if the user has permission.  The operation may fail on some
	Unix flavors if *src* and *dst* are on different filesystems.  If successful,
	the renaming will be an atomic operation (this is a POSIX requirement).  On
	Windows, if *dst* already exists, :exc:`OSError` will be raised even if it is a
	file; there may be no way to implement an atomic rename when *dst* names an
	existing file.
	
	Availability: Unix, Windows.
	
	
	"""
	pass
	
def renames(old,new):
	"""
	Recursive directory or file renaming function. Works like :func:`rename`, except
	creation of any intermediate directories needed to make the new pathname good is
	attempted first. After the rename, directories corresponding to rightmost path
	segments of the old name will be pruned away using :func:`removedirs`.
	
	"""
	pass
	
def rmdir(path):
	"""
	Remove (delete) the directory *path*.  Only works when the directory is
	empty, otherwise, :exc:`OSError` is raised.  In order to remove whole
	directory trees, :func:`shutil.rmtree` can be used.
	
	Availability: Unix, Windows.
	
	
	"""
	pass
	
def stat(path):
	"""
	Perform the equivalent of a :cfunc:`stat` system call on the given path.
	(This function follows symlinks; to stat a symlink use :func:`lstat`.)
	
	The return value is an object whose attributes correspond to the members
	of the :ctype:`stat` structure, namely:
	
	* :attr:`st_mode` - protection bits,
	* :attr:`st_ino` - inode number,
	* :attr:`st_dev` - device,
	* :attr:`st_nlink` - number of hard links,
	* :attr:`st_uid` - user id of owner,
	* :attr:`st_gid` - group id of owner,
	* :attr:`st_size` - size of file, in bytes,
	* :attr:`st_atime` - time of most recent access,
	* :attr:`st_mtime` - time of most recent content modification,
	* :attr:`st_ctime` - platform dependent; time of most recent metadata change on
	Unix, or the time of creation on Windows)
	
	"""
	pass
	
def stat_float_times(newvalue):
	"""
	Determine whether :class:`stat_result` represents time stamps as float objects.
	If *newvalue* is ``True``, future calls to :func:`~os.stat` return floats, if it is
	``False``, future calls return ints. If *newvalue* is omitted, return the
	current setting.
	
	For compatibility with older Python versions, accessing :class:`stat_result` as
	a tuple always returns integers.
	
	"""
	pass
	
def statvfs(path):
	"""
	Perform a :cfunc:`statvfs` system call on the given path.  The return value is
	an object whose attributes describe the filesystem on the given path, and
	correspond to the members of the :ctype:`statvfs` structure, namely:
	:attr:`f_bsize`, :attr:`f_frsize`, :attr:`f_blocks`, :attr:`f_bfree`,
	:attr:`f_bavail`, :attr:`f_files`, :attr:`f_ffree`, :attr:`f_favail`,
	:attr:`f_flag`, :attr:`f_namemax`.
	
	"""
	pass
	
def symlink(source,link_name):
	"""
	Create a symbolic link pointing to *source* named *link_name*.
	
	Availability: Unix.
	
	
	"""
	pass
	
def tempnam(dir,prefix):
	"""
	Return a unique path name that is reasonable for creating a temporary file.
	This will be an absolute path that names a potential directory entry in the
	directory *dir* or a common location for temporary files if *dir* is omitted or
	``None``.  If given and not ``None``, *prefix* is used to provide a short prefix
	to the filename.  Applications are responsible for properly creating and
	managing files created using paths returned by :func:`tempnam`; no automatic
	cleanup is provided. On Unix, the environment variable :envvar:`TMPDIR`
	overrides *dir*, while on Windows :envvar:`TMP` is used.  The specific
	behavior of this function depends on the C library implementation; some aspects
	are underspecified in system documentation.
	
	"""
	pass
	
def tmpnam():
	"""
	Return a unique path name that is reasonable for creating a temporary file.
	This will be an absolute path that names a potential directory entry in a common
	location for temporary files.  Applications are responsible for properly
	creating and managing files created using paths returned by :func:`tmpnam`; no
	automatic cleanup is provided.
	
	"""
	pass
	
def unlink(path):
	"""
	Remove (delete) the file *path*.  This is the same function as
	:func:`remove`; the :func:`unlink` name is its traditional Unix
	name.
	
	Availability: Unix, Windows.
	
	
	"""
	pass
	
def utime(path,times):
	"""
	Set the access and modified times of the file specified by *path*. If *times*
	is ``None``, then the file's access and modified times are set to the current
	time. (The effect is similar to running the Unix program :program:`touch` on
	the path.)  Otherwise, *times* must be a 2-tuple of numbers, of the form
	``(atime, mtime)`` which is used to set the access and modified times,
	respectively. Whether a directory can be given for *path* depends on whether
	the operating system implements directories as files (for example, Windows
	does not).  Note that the exact times you set here may not be returned by a
	subsequent :func:`~os.stat` call, depending on the resolution with which your
	operating system records access and modification times; see :func:`~os.stat`.
	
	"""
	pass
	
def walk(top,topdown=True,onerror=None,followlinks=False):
	"""
	"""
	pass
	
def abort():
	"""
	Generate a :const:`SIGABRT` signal to the current process.  On Unix, the default
	behavior is to produce a core dump; on Windows, the process immediately returns
	an exit code of ``3``.  Be aware that programs which use :func:`signal.signal`
	to register a handler for :const:`SIGABRT` will behave differently.
	
	Availability: Unix, Windows.
	
	
	"""
	pass
	
def execl(path,arg0,arg1,more):
	"""execle(path, arg0, arg1, *more, env)
	execlp(file, arg0, arg1, *more)
	execlpe(file, arg0, arg1, *more, env)
	execv(path, args)
	execve(path, args, env)
	execvp(file, args)
	execvpe(file, args, env)
	
	These functions all execute a new program, replacing the current process; they
	do not return.  On Unix, the new executable is loaded into the current process,
	and will have the same process id as the caller.  Errors will be reported as
	:exc:`OSError` exceptions.
	
	The current process is replaced immediately. Open file objects and
	descriptors are not flushed, so if there may be data buffered
	on these open files, you should flush them using
	:func:`sys.stdout.flush` or :func:`os.fsync` before calling an
	:func:`exec\*` function.
	
	The "l" and "v" variants of the :func:`exec\*` functions differ in how
	command-line arguments are passed.  The "l" variants are perhaps the easiest
	to work with if the number of parameters is fixed when the code is written; the
	individual parameters simply become additional parameters to the :func:`execl\*`
	functions.  The "v" variants are good when the number of parameters is
	variable, with the arguments being passed in a list or tuple as the *args*
	parameter.  In either case, the arguments to the child process should start with
	the name of the command being run, but this is not enforced.
	
	The variants which include a "p" near the end (:func:`execlp`,
	:func:`execlpe`, :func:`execvp`, and :func:`execvpe`) will use the
	:envvar:`PATH` environment variable to locate the program *file*.  When the
	environment is being replaced (using one of the :func:`exec\*e` variants,
	discussed in the next paragraph), the new environment is used as the source of
	the :envvar:`PATH` variable. The other variants, :func:`execl`, :func:`execle`,
	:func:`execv`, and :func:`execve`, will not use the :envvar:`PATH` variable to
	locate the executable; *path* must contain an appropriate absolute or relative
	path.
	
	For :func:`execle`, :func:`execlpe`, :func:`execve`, and :func:`execvpe` (note
	that these all end in "e"), the *env* parameter must be a mapping which is
	used to define the environment variables for the new process (these are used
	instead of the current process' environment); the functions :func:`execl`,
	:func:`execlp`, :func:`execv`, and :func:`execvp` all cause the new process to
	inherit the environment of the current process.
	
	Availability: Unix, Windows.
	
	
	"""
	pass
	
def _exit(n):
	"""
	Exit the process with status *n*, without calling cleanup handlers, flushing
	stdio buffers, etc.
	
	Availability: Unix, Windows.
	
	"""
	pass
	
def fork():
	"""
	Fork a child process.  Return ``0`` in the child and the child's process id in the
	parent.  If an error occurs :exc:`OSError` is raised.
	
	Note that some platforms including FreeBSD <= 6.3, Cygwin and OS/2 EMX have
	known issues when using fork() from a thread.
	
	Availability: Unix.
	
	
	"""
	pass
	
def forkpty():
	"""
	Fork a child process, using a new pseudo-terminal as the child's controlling
	terminal. Return a pair of ``(pid, fd)``, where *pid* is ``0`` in the child, the
	new child's process id in the parent, and *fd* is the file descriptor of the
	master end of the pseudo-terminal.  For a more portable approach, use the
	:mod:`pty` module.  If an error occurs :exc:`OSError` is raised.
	
	Availability: some flavors of Unix.
	
	
	"""
	pass
	
def kill(pid,sig):
	"""
	"""
	pass
	
def killpg(pgid,sig):
	"""
	"""
	pass
	
def nice(increment):
	"""
	Add *increment* to the process's "niceness".  Return the new niceness.
	
	Availability: Unix.
	
	
	"""
	pass
	
def plock(op):
	"""
	Lock program segments into memory.  The value of *op* (defined in
	``<sys/lock.h>``) determines which segments are locked.
	
	Availability: Unix.
	
	
	"""
	pass
	
def popen(more):
	"""popen2(*more)
	popen3(*more)
	popen4(*more)
	:noindex:
	
	Run child processes, returning opened pipes for communications.  These functions
	are described in section :ref:`os-newstreams`.
	
	
	"""
	pass
	
def spawnl(mode,path,more):
	"""spawnle(mode, path, *more, env)
	spawnlp(mode, file, *more)
	spawnlpe(mode, file, *more, env)
	spawnv(mode, path, args)
	spawnve(mode, path, args, env)
	spawnvp(mode, file, args)
	spawnvpe(mode, file, args, env)
	
	Execute the program *path* in a new process.
	
	(Note that the :mod:`subprocess` module provides more powerful facilities for
	spawning new processes and retrieving their results; using that module is
	preferable to using these functions.  Check especially the
	:ref:`subprocess-replacements` section.)
	
	If *mode* is :const:`P_NOWAIT`, this function returns the process id of the new
	process; if *mode* is :const:`P_WAIT`, returns the process's exit code if it
	exits normally, or ``-signal``, where *signal* is the signal that killed the
	process.  On Windows, the process id will actually be the process handle, so can
	be used with the :func:`waitpid` function.
	
	The "l" and "v" variants of the :func:`spawn\*` functions differ in how
	command-line arguments are passed.  The "l" variants are perhaps the easiest
	to work with if the number of parameters is fixed when the code is written; the
	individual parameters simply become additional parameters to the
	:func:`spawnl\*` functions.  The "v" variants are good when the number of
	parameters is variable, with the arguments being passed in a list or tuple as
	the *args* parameter.  In either case, the arguments to the child process must
	start with the name of the command being run.
	
	The variants which include a second "p" near the end (:func:`spawnlp`,
	:func:`spawnlpe`, :func:`spawnvp`, and :func:`spawnvpe`) will use the
	:envvar:`PATH` environment variable to locate the program *file*.  When the
	environment is being replaced (using one of the :func:`spawn\*e` variants,
	discussed in the next paragraph), the new environment is used as the source of
	the :envvar:`PATH` variable.  The other variants, :func:`spawnl`,
	:func:`spawnle`, :func:`spawnv`, and :func:`spawnve`, will not use the
	:envvar:`PATH` variable to locate the executable; *path* must contain an
	appropriate absolute or relative path.
	
	For :func:`spawnle`, :func:`spawnlpe`, :func:`spawnve`, and :func:`spawnvpe`
	(note that these all end in "e"), the *env* parameter must be a mapping
	which is used to define the environment variables for the new process (they are
	used instead of the current process' environment); the functions
	:func:`spawnl`, :func:`spawnlp`, :func:`spawnv`, and :func:`spawnvp` all cause
	the new process to inherit the environment of the current process.  Note that
	keys and values in the *env* dictionary must be strings; invalid keys or
	values will cause the function to fail, with a return value of ``127``.
	
	As an example, the following calls to :func:`spawnlp` and :func:`spawnvpe` are
	equivalent::
	
	import os
	os.spawnlp(os.P_WAIT, 'cp', 'cp', 'index.html', '/dev/null')
	
	L = ['cp', 'index.html', '/dev/null']
	os.spawnvpe(os.P_WAIT, 'cp', L, os.environ)
	
	Availability: Unix, Windows.  :func:`spawnlp`, :func:`spawnlpe`, :func:`spawnvp`
	and :func:`spawnvpe` are not available on Windows.
	
	"""
	pass
	
def startfile(path,operation):
	"""
	Start a file with its associated application.
	
	When *operation* is not specified or ``'open'``, this acts like double-clicking
	the file in Windows Explorer, or giving the file name as an argument to the
	:program:`start` command from the interactive command shell: the file is opened
	with whatever application (if any) its extension is associated.
	
	When another *operation* is given, it must be a "command verb" that specifies
	what should be done with the file. Common verbs documented by Microsoft are
	``'print'`` and  ``'edit'`` (to be used on files) as well as ``'explore'`` and
	``'find'`` (to be used on directories).
	
	:func:`startfile` returns as soon as the associated application is launched.
	There is no option to wait for the application to close, and no way to retrieve
	the application's exit status.  The *path* parameter is relative to the current
	directory.  If you want to use an absolute path, make sure the first character
	is not a slash (``'/'``); the underlying Win32 :cfunc:`ShellExecute` function
	doesn't work if it is.  Use the :func:`os.path.normpath` function to ensure that
	the path is properly encoded for Win32.
	
	Availability: Windows.
	
	"""
	pass
	
def system(command):
	"""
	Execute the command (a string) in a subshell.  This is implemented by calling
	the Standard C function :cfunc:`system`, and has the same limitations.
	Changes to :data:`sys.stdin`, etc. are not reflected in the environment of the
	executed command.
	
	On Unix, the return value is the exit status of the process encoded in the
	format specified for :func:`wait`.  Note that POSIX does not specify the meaning
	of the return value of the C :cfunc:`system` function, so the return value of
	the Python function is system-dependent.
	
	On Windows, the return value is that returned by the system shell after running
	*command*, given by the Windows environment variable :envvar:`COMSPEC`: on
	:program:`command.com` systems (Windows 95, 98 and ME) this is always ``0``; on
	:program:`cmd.exe` systems (Windows NT, 2000 and XP) this is the exit status of
	the command run; on systems using a non-native shell, consult your shell
	documentation.
	
	The :mod:`subprocess` module provides more powerful facilities for spawning new
	processes and retrieving their results; using that module is preferable to using
	this function.  See the
	:ref:`subprocess-replacements` section in the :mod:`subprocess` documentation
	for some helpful recipes.
	
	Availability: Unix, Windows.
	
	
	"""
	pass
	
def times():
	"""
	Return a 5-tuple of floating point numbers indicating accumulated (processor
	or other) times, in seconds.  The items are: user time, system time,
	children's user time, children's system time, and elapsed real time since a
	fixed point in the past, in that order.  See the Unix manual page
	:manpage:`times(2)` or the corresponding Windows Platform API documentation.
	On Windows, only the first two items are filled, the others are zero.
	
	Availability: Unix, Windows
	
	
	"""
	pass
	
def wait():
	"""
	Wait for completion of a child process, and return a tuple containing its pid
	and exit status indication: a 16-bit number, whose low byte is the signal number
	that killed the process, and whose high byte is the exit status (if the signal
	number is zero); the high bit of the low byte is set if a core file was
	produced.
	
	Availability: Unix.
	
	
	"""
	pass
	
def waitpid(pid,options):
	"""
	The details of this function differ on Unix and Windows.
	
	On Unix: Wait for completion of a child process given by process id *pid*, and
	return a tuple containing its process id and exit status indication (encoded as
	for :func:`wait`).  The semantics of the call are affected by the value of the
	integer *options*, which should be ``0`` for normal operation.
	
	If *pid* is greater than ``0``, :func:`waitpid` requests status information for
	that specific process.  If *pid* is ``0``, the request is for the status of any
	child in the process group of the current process.  If *pid* is ``-1``, the
	request pertains to any child of the current process.  If *pid* is less than
	``-1``, status is requested for any process in the process group ``-pid`` (the
	absolute value of *pid*).
	
	An :exc:`OSError` is raised with the value of errno when the syscall
	returns -1.
	
	On Windows: Wait for completion of a process given by process handle *pid*, and
	return a tuple containing *pid*, and its exit status shifted left by 8 bits
	(shifting makes cross-platform use of the function easier). A *pid* less than or
	equal to ``0`` has no special meaning on Windows, and raises an exception. The
	value of integer *options* has no effect. *pid* can refer to any process whose
	id is known, not necessarily a child process. The :func:`spawn` functions called
	with :const:`P_NOWAIT` return suitable process handles.
	
	
	"""
	pass
	
def wait3(options):
	"""
	Similar to :func:`waitpid`, except no process id argument is given and a
	3-element tuple containing the child's process id, exit status indication, and
	resource usage information is returned.  Refer to :mod:`resource`.\
	:func:`getrusage` for details on resource usage information.  The option
	argument is the same as that provided to :func:`waitpid` and :func:`wait4`.
	
	Availability: Unix.
	
	"""
	pass
	
def wait4(pid,options):
	"""
	Similar to :func:`waitpid`, except a 3-element tuple, containing the child's
	process id, exit status indication, and resource usage information is returned.
	Refer to :mod:`resource`.\ :func:`getrusage` for details on resource usage
	information.  The arguments to :func:`wait4` are the same as those provided to
	:func:`waitpid`.
	
	Availability: Unix.
	
	"""
	pass
	
def WCOREDUMP(status):
	"""
	Return ``True`` if a core dump was generated for the process, otherwise
	return ``False``.
	
	Availability: Unix.
	
	"""
	pass
	
def WIFCONTINUED(status):
	"""
	Return ``True`` if the process has been continued from a job control stop,
	otherwise return ``False``.
	
	Availability: Unix.
	
	"""
	pass
	
def WIFSTOPPED(status):
	"""
	Return ``True`` if the process has been stopped, otherwise return
	``False``.
	
	Availability: Unix.
	
	
	"""
	pass
	
def WIFSIGNALED(status):
	"""
	Return ``True`` if the process exited due to a signal, otherwise return
	``False``.
	
	Availability: Unix.
	
	
	"""
	pass
	
def WIFEXITED(status):
	"""
	Return ``True`` if the process exited using the :manpage:`exit(2)` system call,
	otherwise return ``False``.
	
	Availability: Unix.
	
	
	"""
	pass
	
def WEXITSTATUS(status):
	"""
	If ``WIFEXITED(status)`` is true, return the integer parameter to the
	:manpage:`exit(2)` system call.  Otherwise, the return value is meaningless.
	
	Availability: Unix.
	
	
	"""
	pass
	
def WSTOPSIG(status):
	"""
	Return the signal which caused the process to stop.
	
	Availability: Unix.
	
	
	"""
	pass
	
def WTERMSIG(status):
	"""
	Return the signal which caused the process to exit.
	
	Availability: Unix.
	
	
	.. iscellaneous System Information
	--------------------------------
	
	
	"""
	pass
	
def confstr(name):
	"""
	Return string-valued system configuration values. *name* specifies the
	configuration value to retrieve; it may be a string which is the name of a
	defined system value; these names are specified in a number of standards (POSIX,
	Unix 95, Unix 98, and others).  Some platforms define additional names as well.
	The names known to the host operating system are given as the keys of the
	``confstr_names`` dictionary.  For configuration variables not included in that
	mapping, passing an integer for *name* is also accepted.
	
	If the configuration value specified by *name* isn't defined, ``None`` is
	returned.
	
	If *name* is a string and is not known, :exc:`ValueError` is raised.  If a
	specific value for *name* is not supported by the host system, even if it is
	included in ``confstr_names``, an :exc:`OSError` is raised with
	:const:`errno.EINVAL` for the error number.
	
	Availability: Unix
	
	
	"""
	pass
	
def getloadavg():
	"""
	Return the number of processes in the system run queue averaged over the last
	1, 5, and 15 minutes or raises :exc:`OSError` if the load average was
	unobtainable.
	
	Availability: Unix.
	
	"""
	pass
	
def sysconf(name):
	"""
	Return integer-valued system configuration values. If the configuration value
	specified by *name* isn't defined, ``-1`` is returned.  The comments regarding
	the *name* parameter for :func:`confstr` apply here as well; the dictionary that
	provides information on the known names is given by ``sysconf_names``.
	
	Availability: Unix.
	
	
	"""
	pass
	
def urandom(n):
	"""
	Return a string of *n* random bytes suitable for cryptographic use.
	
	This function returns random bytes from an OS-specific randomness source.  The
	returned data should be unpredictable enough for cryptographic applications,
	though its exact quality depends on the OS implementation.  On a UNIX-like
	system this will query /dev/urandom, and on Windows it will use CryptGenRandom.
	If a randomness source is not found, :exc:`NotImplementedError` will be raised.
	
	"""
	pass
	
