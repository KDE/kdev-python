#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
""":synopsis: Convert Python objects to streams of bytes and back (with different
constraints).


This module contains functions that can read and write Python values in a binary
format.  The format is specific to Python, but independent of machine
architecture issues (e.g., you can write a Python value to a file on a PC,
transport the file to a Sun, and read it back there).  Details of the format are
undocumented on purpose; it may change between Python versions (although it
rarely does). [#]_

"""
"""
Indicates the format that the module uses. Version 0 is the historical format,
version 1 (added in Python 2.4) shares interned strings and version 2 (added in
Python 2.5) uses a binary format for floating point numbers. The current version
is 2.

"""
version = None
def dump(value,file,version):
	"""
	Write the value on the open file.  The value must be a supported type.  The
	file must be an open file object such as ``sys.stdout`` or returned by
	:func:`open` or :func:`os.popen`.  It must be opened in binary mode (``'wb'``
	or ``'w+b'``).
	
	If the value has (or contains an object that has) an unsupported type, a
	:exc:`ValueError` exception is raised --- but garbage data will also be written
	to the file.  The object will not be properly read back by :func:`load`.
	
	"""
	pass
	
def load(file):
	"""
	Read one value from the open file and return it.  If no valid value is read
	(e.g. because the data has a different Python version's incompatible marshal
	format), raise :exc:`EOFError`, :exc:`ValueError` or :exc:`TypeError`.  The
	file must be an open file object opened in binary mode (``'rb'`` or
	``'r+b'``).
	
	"""
	pass
	
def dumps(value,version):
	"""
	Return the string that would be written to a file by ``dump(value, file)``.  The
	value must be a supported type.  Raise a :exc:`ValueError` exception if value
	has (or contains an object that has) an unsupported type.
	
	"""
	pass
	
def loads(string):
	"""
	Convert the string to a value.  If no valid value is found, raise
	:exc:`EOFError`, :exc:`ValueError` or :exc:`TypeError`.  Extra characters in the
	string are ignored.
	
	
	In addition, the following constants are defined:
	
	"""
	pass
	
