#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
""":platform: Mac
:synopsis: Convenience routines for file manipulation.
:deprecated:


This module contains some convenience routines for file-manipulation on the
Macintosh. All file parameters can be specified as pathnames, :class:`FSRef` or
:class:`FSSpec` objects.  This module expects a filesystem which supports forked
files, so it should not be used on UFS partitions.

"""
"""
The buffer size for ``copy``, default 1 megabyte.

Note that the process of creating finder aliases is not specified in the Apple
documentation. Hence, aliases created with :func:`mkalias` could conceivably
have incompatible behaviour in some cases.


:mod:`findertools` --- The :program:`finder`'s Apple Events interface
======================================================================

"""
BUFSIZ = None
def copy(src,dst,createpath,copytimes):
	"""
	Copy file *src* to *dst*.  If *createpath* is non-zero the folders leading to
	*dst* are created if necessary. The method copies data and resource fork and
	some finder information (creator, type, flags) and optionally the creation,
	modification and backup times (default is to copy them). Custom icons, comments
	and icon position are not copied.
	
	"""
	pass
	
def copytree(src,dst):
	"""
	Recursively copy a file tree from *src* to *dst*, creating folders as needed.
	*src* and *dst* should be specified as pathnames.
	
	"""
	pass
	
def mkalias(src,dst):
	"""
	Create a finder alias *dst* pointing to *src*.
	
	"""
	pass
	
def touched(dst):
	"""
	Tell the finder that some bits of finder-information such as creator or type for
	file *dst* has changed. The file can be specified by pathname or fsspec. This
	call should tell the finder to redraw the files icon.
	
	"""
	pass
	
