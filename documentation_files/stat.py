#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
""":synopsis: Utilities for interpreting the results of os.stat(), os.lstat() and os.fstat().
"""
"""
Inode protection mode.


"""
ST_MODE = None
"""
Inode number.


"""
ST_INO = None
"""
Device inode resides on.


"""
ST_DEV = None
"""
Number of links to the inode.


"""
ST_NLINK = None
"""
User id of the owner.


"""
ST_UID = None
"""
Group id of the owner.


"""
ST_GID = None
"""
Size in bytes of a plain file; amount of data waiting on some special files.


"""
ST_SIZE = None
"""
Time of last access.


"""
ST_ATIME = None
"""
Time of last modification.


"""
ST_MTIME = None
"""
The "ctime" as reported by the operating system.  On some systems (like Unix) is
the time of the last metadata change, and, on others (like Windows), is the
creation time (see platform documentation for details).

The interpretation of "file size" changes according to the file type.  For plain
files this is the size of the file in bytes.  For FIFOs and sockets under most
flavors of Unix (including Linux in particular), the "size" is the number of
bytes waiting to be read at the time of the call to :func:`os.stat`,
:func:`os.fstat`, or :func:`os.lstat`; this can sometimes be useful, especially
for polling one of these special files after a non-blocking open.  The meaning
of the size field for other character and block devices varies more, depending
on the implementation of the underlying system call.

The variables below define the flags used in the :data:`ST_MODE` field.

Use of the functions above is more portable than use of the first set of flags:

"""
ST_CTIME = None
"""
Bit mask for the file type bit fields.

"""
S_IFMT = None
"""
Socket.

"""
S_IFSOCK = None
"""
Symbolic link.

"""
S_IFLNK = None
"""
Regular file.

"""
S_IFREG = None
"""
Block device.

"""
S_IFBLK = None
"""
Directory.

"""
S_IFDIR = None
"""
Character device.

"""
S_IFCHR = None
"""
FIFO.

The following flags can also be used in the *mode* argument of :func:`os.chmod`:

"""
S_IFIFO = None
"""
Set UID bit.

"""
S_ISUID = None
"""
Set-group-ID bit.  This bit has several special uses.  For a directory
it indicates that BSD semantics is to be used for that directory:
files created there inherit their group ID from the directory, not
from the effective group ID of the creating process, and directories
created there will also get the :data:`S_ISGID` bit set.  For a
file that does not have the group execution bit (:data:`S_IXGRP`)
set, the set-group-ID bit indicates mandatory file/record locking
(see also :data:`S_ENFMT`).

"""
S_ISGID = None
"""
Sticky bit.  When this bit is set on a directory it means that a file
in that directory can be renamed or deleted only by the owner of the
file, by the owner of the directory, or by a privileged process.

"""
S_ISVTX = None
"""
Mask for file owner permissions.

"""
S_IRWXU = None
"""
Owner has read permission.

"""
S_IRUSR = None
"""
Owner has write permission.

"""
S_IWUSR = None
"""
Owner has execute permission.

"""
S_IXUSR = None
"""
Mask for group permissions.

"""
S_IRWXG = None
"""
Group has read permission.

"""
S_IRGRP = None
"""
Group has write permission.

"""
S_IWGRP = None
"""
Group has execute permission.

"""
S_IXGRP = None
"""
Mask for permissions for others (not in group).

"""
S_IRWXO = None
"""
Others have read permission.

"""
S_IROTH = None
"""
Others have write permission.

"""
S_IWOTH = None
"""
Others have execute permission.

"""
S_IXOTH = None
"""
System V file locking enforcement.  This flag is shared with :data:`S_ISGID`:
file/record locking is enforced on files that do not have the group
execution bit (:data:`S_IXGRP`) set.

"""
S_ENFMT = None
"""
Unix V7 synonym for :data:`S_IRUSR`.

"""
S_IREAD = None
"""
Unix V7 synonym for :data:`S_IWUSR`.

"""
S_IWRITE = None
"""
Unix V7 synonym for :data:`S_IXUSR`.

The following flags can be used in the *flags* argument of :func:`os.chflags`:

"""
S_IEXEC = None
"""
Do not dump the file.

"""
UF_NODUMP = None
"""
The file may not be changed.

"""
UF_IMMUTABLE = None
"""
The file may only be appended to.

"""
UF_APPEND = None
"""
The file may not be renamed or deleted.

"""
UF_OPAQUE = None
"""
The directory is opaque when viewed through a union stack.

"""
UF_NOUNLINK = None
"""
The file may be archived.

"""
SF_ARCHIVED = None
"""
The file may not be changed.

"""
SF_IMMUTABLE = None
"""
The file may only be appended to.

"""
SF_APPEND = None
"""
The file may not be renamed or deleted.

"""
SF_NOUNLINK = None
def S_ISDIR(mode):
	"""
	Return non-zero if the mode is from a directory.
	
	
	"""
	pass
	
def S_ISCHR(mode):
	"""
	Return non-zero if the mode is from a character special device file.
	
	
	"""
	pass
	
def S_ISBLK(mode):
	"""
	Return non-zero if the mode is from a block special device file.
	
	
	"""
	pass
	
def S_ISREG(mode):
	"""
	Return non-zero if the mode is from a regular file.
	
	
	"""
	pass
	
def S_ISFIFO(mode):
	"""
	Return non-zero if the mode is from a FIFO (named pipe).
	
	
	"""
	pass
	
def S_ISLNK(mode):
	"""
	Return non-zero if the mode is from a symbolic link.
	
	
	"""
	pass
	
def S_ISSOCK(mode):
	"""
	Return non-zero if the mode is from a socket.
	
	Two additional functions are defined for more general manipulation of the file's
	mode:
	
	
	"""
	pass
	
def S_IMODE(mode):
	"""
	Return the portion of the file's mode that can be set by :func:`os.chmod`\
	---that is, the file's permission bits, plus the sticky bit, set-group-id, and
	set-user-id bits (on systems that support them).
	
	
	"""
	pass
	
def S_IFMT(mode):
	"""
	Return the portion of the file's mode that describes the file type (used by the
	:func:`S_IS\*` functions above).
	
	Normally, you would use the :func:`os.path.is\*` functions for testing the type
	of a file; the functions here are useful when you are doing multiple tests of
	the same file and wish to avoid the overhead of the :cfunc:`stat` system call
	for each test.  These are also useful when checking for information about a file
	that isn't handled by :mod:`os.path`, like the tests for block and character
	devices.
	
	Example::
	
	import os, sys
	from stat import *
	
	def walktree(top, callback):
	'''recursively descend the directory tree rooted at top,
	calling the callback function for each regular file'''
	
	for f in os.listdir(top):
	pathname = os.path.join(top, f)
	mode = os.stat(pathname)[ST_MODE]
	if S_ISDIR(mode):
	# It's a directory, recurse into it
	walktree(pathname, callback)
	elif S_ISREG(mode):
	# It's a file, call the callback function
	callback(pathname)
	else:
	# Unknown file type, print a message
	print 'Skipping %s' % pathname
	
	def visitfile(file):
	print 'visiting', file
	
	if __name__ == '__main__':
	walktree(sys.argv[1], visitfile)
	
	All the variables below are simply symbolic indexes into the 10-tuple returned
	by :func:`os.stat`, :func:`os.fstat` or :func:`os.lstat`.
	
	
	"""
	pass
	
