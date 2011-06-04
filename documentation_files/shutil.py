#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
""":synopsis: High-level file operations, including copying.
"""
def copyfileobj(fsrc,fdst,length):
	"""
	Copy the contents of the file-like object *fsrc* to the file-like object *fdst*.
	The integer *length*, if given, is the buffer size. In particular, a negative
	*length* value means to copy the data without looping over the source data in
	chunks; by default the data is read in chunks to avoid uncontrolled memory
	consumption. Note that if the current file position of the *fsrc* object is not
	0, only the contents from the current file position to the end of the file will
	be copied.
	
	
	"""
	pass
	
def copyfile(src,dst):
	"""
	Copy the contents (no metadata) of the file named *src* to a file named *dst*.
	*dst* must be the complete target file name; look at :func:`copy` for a copy that
	accepts a target directory path.  If *src* and *dst* are the same files,
	:exc:`Error` is raised.
	The destination location must be writable; otherwise,  an :exc:`IOError` exception
	will be raised. If *dst* already exists, it will be replaced.   Special files
	such as character or block devices and pipes cannot be copied with this
	function.  *src* and *dst* are path names given as strings.
	
	
	"""
	pass
	
def copymode(src,dst):
	"""
	Copy the permission bits from *src* to *dst*.  The file contents, owner, and
	group are unaffected.  *src* and *dst* are path names given as strings.
	
	
	"""
	pass
	
def copystat(src,dst):
	"""
	Copy the permission bits, last access time, last modification time, and flags
	from *src* to *dst*.  The file contents, owner, and group are unaffected.  *src*
	and *dst* are path names given as strings.
	
	
	"""
	pass
	
def copy(src,dst):
	"""
	Copy the file *src* to the file or directory *dst*.  If *dst* is a directory, a
	file with the same basename as *src*  is created (or overwritten) in the
	directory specified.  Permission bits are copied.  *src* and *dst* are path
	names given as strings.
	
	
	"""
	pass
	
def copy2(src,dst):
	"""
	Similar to :func:`copy`, but metadata is copied as well -- in fact, this is just
	:func:`copy` followed by :func:`copystat`.  This is similar to the
	Unix command :program:`cp -p`.
	
	
	"""
	pass
	
def ignore_patterns(ESCpatterns):
	"""
	This factory function creates a function that can be used as a callable for
	:func:`copytree`\'s *ignore* argument, ignoring files and directories that
	match one of the glob-style *patterns* provided.  See the example below.
	
	"""
	pass
	
def copytree(src,dst,symlinks=False,ignore=None):
	"""
	Recursively copy an entire directory tree rooted at *src*.  The destination
	directory, named by *dst*, must not already exist; it will be created as well
	as missing parent directories.  Permissions and times of directories are
	copied with :func:`copystat`, individual files are copied using
	:func:`copy2`.
	
	If *symlinks* is true, symbolic links in the source tree are represented as
	symbolic links in the new tree; if false or omitted, the contents of the
	linked files are copied to the new tree.
	
	If *ignore* is given, it must be a callable that will receive as its
	arguments the directory being visited by :func:`copytree`, and a list of its
	contents, as returned by :func:`os.listdir`.  Since :func:`copytree` is
	called recursively, the *ignore* callable will be called once for each
	directory that is copied.  The callable must return a sequence of directory
	and file names relative to the current directory (i.e. a subset of the items
	in its second argument); these names will then be ignored in the copy
	process.  :func:`ignore_patterns` can be used to create such a callable that
	ignores names based on glob-style patterns.
	
	If exception(s) occur, an :exc:`Error` is raised with a list of reasons.
	
	The source code for this should be considered an example rather than the
	ultimate tool.
	
	"""
	pass
	
def rmtree(path,ignore_errors,onerror):
	"""
	"""
	pass
	
def move(src,dst):
	"""
	Recursively move a file or directory to another location.
	
	If the destination is on the current filesystem, then simply use rename.
	Otherwise, copy src (with :func:`copy2`) to the dst and then remove src.
	
	"""
	pass
	
def make_archive(base_name,format,root_dir,base_dir,verbose,dry_run,owner,group,logger):
	"""
	Create an archive file (eg. zip or tar) and returns its name.
	
	*base_name* is the name of the file to create, including the path, minus
	any format-specific extension. *format* is the archive format: one of
	"zip", "tar", "bztar" or "gztar".
	
	*root_dir* is a directory that will be the root directory of the
	archive; ie. we typically chdir into *root_dir* before creating the
	archive.
	
	*base_dir* is the directory where we start archiving from;
	ie. *base_dir* will be the common prefix of all files and
	directories in the archive.
	
	*root_dir* and *base_dir* both default to the current directory.
	
	*owner* and *group* are used when creating a tar archive. By default,
	uses the current owner and group.
	
	"""
	pass
	
def get_archive_formats():
	"""
	Returns a list of supported formats for archiving.
	Each element of the returned sequence is a tuple ``(name, description)``
	
	By default :mod:`shutil` provides these formats:
	
	- *gztar*: gzip'ed tar-file
	- *bztar*: bzip2'ed tar-file
	- *tar*: uncompressed tar file
	- *zip*: ZIP file
	
	You can register new formats or provide your own archiver for any existing
	formats, by using :func:`register_archive_format`.
	
	"""
	pass
	
def register_archive_format(name,function,extra_args,description):
	"""
	Registers an archiver for the format *name*. *function* is a callable that
	will be used to invoke the archiver.
	
	If given, *extra_args* is a sequence of ``(name, value)`` that will be
	used as extra keywords arguments when the archiver callable is used.
	
	*description* is used by :func:`get_archive_formats` which returns the
	list of archivers. Defaults to an empty list.
	
	"""
	pass
	
def unregister_archive_format(name):
	"""
	Remove the archive format *name* from the list of supported formats.
	
	"""
	pass
	
