#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
""":synopsis: Interface to memory-mapped files for Unix and Windows.


Memory-mapped file objects behave like both strings and like file objects.
Unlike normal string objects, however, these are mutable.  You can use mmap
objects in most places where strings are expected; for example, you can use
the :mod:`re` module to search through a memory-mapped file.  Since they're
mutable, you can change a single character by doing ``obj[index] = 'a'``, or
change a substring by assigning to a slice: ``obj[i1:i2] = '*more'``.  You can
also read and write data starting at the current file position, and
:meth:`seek` through the file to different positions.

A memory-mapped file is created by the :class:`mmap` constructor, which is
different on Unix and on Windows.  In either case you must provide a file
descriptor for a file opened for update. If you wish to map an existing Python
file object, use its :meth:`fileno` method to obtain the correct value for the
*fileno* parameter.  Otherwise, you can open the file using the
:func:`os.open` function, which returns a file descriptor directly (the file
still needs to be closed when done).

For both the Unix and Windows versions of the constructor, *access* may be
specified as an optional keyword parameter. *access* accepts one of three
values: :const:`ACCESS_READ`, :const:`ACCESS_WRITE`, or :const:`ACCESS_COPY`
to specify read-only, write-through or copy-on-write memory respectively.
*access* can be used on both Unix and Windows.  If *access* is not specified,
Windows mmap returns a write-through mapping.  The initial memory values for
all three access types are taken from the specified file.  Assignment to an
:const:`ACCESS_READ` memory map raises a :exc:`TypeError` exception.
Assignment to an :const:`ACCESS_WRITE` memory map affects both memory and the
underlying file.  Assignment to an :const:`ACCESS_COPY` memory map affects
memory but does not update the underlying file.

"""
class mmap:


	"""
	**(Windows version)** Maps *length* bytes from the file specified by the
	file handle *fileno*, and creates a mmap object.  If *length* is larger
	than the current size of the file, the file is extended to contain *length*
	bytes.  If *length* is ``0``, the maximum length of the map is the current
	size of the file, except that if the file is empty Windows raises an
	exception (you cannot create an empty mapping on Windows).
	
	*tagname*, if specified and not ``None``, is a string giving a tag name for
	the mapping.  Windows allows you to have many different mappings against
	the same file.  If you specify the name of an existing tag, that tag is
	opened, otherwise a new tag of this name is created.  If this parameter is
	omitted or ``None``, the mapping is created without a name.  Avoiding the
	use of the tag parameter will assist in keeping your code portable between
	Unix and Windows.
	
	*offset* may be specified as a non-negative integer offset. mmap references
	will be relative to the offset from the beginning of the file. *offset*
	defaults to 0.  *offset* must be a multiple of the ALLOCATIONGRANULARITY.
	
	
	"""
	
	
	def __init__(self, fileno,length,tagname,access,offset):
		pass
	
	


class mmap:


	""":noindex:
	
	**(Unix version)** Maps *length* bytes from the file specified by the file
	descriptor *fileno*, and returns a mmap object.  If *length* is ``0``, the
	maximum length of the map will be the current size of the file when
	:class:`mmap` is called.
	
	*flags* specifies the nature of the mapping. :const:`MAP_PRIVATE` creates a
	private copy-on-write mapping, so changes to the contents of the mmap
	object will be private to this process, and :const:`MAP_SHARED` creates a
	mapping that's shared with all other processes mapping the same areas of
	the file.  The default value is :const:`MAP_SHARED`.
	
	*prot*, if specified, gives the desired memory protection; the two most
	useful values are :const:`PROT_READ` and :const:`PROT_WRITE`, to specify
	that the pages may be read or written.  *prot* defaults to
	:const:`PROT_READ \| PROT_WRITE`.
	
	*access* may be specified in lieu of *flags* and *prot* as an optional
	keyword parameter.  It is an error to specify both *flags*, *prot* and
	*access*.  See the description of *access* above for information on how to
	use this parameter.
	
	*offset* may be specified as a non-negative integer offset. mmap references
	will be relative to the offset from the beginning of the file. *offset*
	defaults to 0.  *offset* must be a multiple of the PAGESIZE or
	ALLOCATIONGRANULARITY.
	
	To ensure validity of the created memory mapping the file specified
	by the descriptor *fileno* is internally automatically synchronized
	with physical backing store on Mac OS X and OpenVMS.
	
	This example shows a simple way of using :class:`mmap`::
	
	import mmap
	
	# write a simple example file
	with open("hello.txt", "wb") as f:
	f.write("Hello Python!\n")
	
	with open("hello.txt", "r+b") as f:
	# memory-map the file, size 0 means whole file
	map = mmap.mmap(f.fileno(), 0)
	# read content via standard file methods
	print map.readline()  # prints "Hello Python!"
	# read content via slice notation
	print map[:5]  # prints "Hello"
	# update content using slice notation;
	# note that new content must have same size
	map[6:] = " world!\n"
	# *more and read again using standard file methods
	map.seek(0)
	print map.readline()  # prints "Hello  world!"
	# close the map
	map.close()
	
	
	The next example demonstrates how to create an anonymous map and exchange
	data between the parent and child processes::
	
	import mmap
	import os
	
	map = mmap.mmap(-1, 13)
	map.write("Hello world!")
	
	pid = os.fork()
	
	if pid == 0: # In a child process
	map.seek(0)
	print map.readline()
	
	map.close()
	
	
	Memory-mapped file objects support the following methods:
	
	
	"""
	
	
	def __init__(self, fileno,length,flags,prot,access,offset):
		pass
	
	


