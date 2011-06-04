#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
""":synopsis: Space efficient arrays of uniformly typed numeric values.


"""
class array:


	"""
	A new array whose items are restricted by *typecode*, and initialized
	from the optional *initializer* value, which must be a list, string, or iterable
	over elements of the appropriate type.
	
	"""
	
	
	def __init__(self, ):
		pass
	
	def append(self, x):
		"""
		Append a new item with value *x* to the end of the array.
		
		
		"""
		pass
		
	def buffer_info(self, ):
		"""
		Return a tuple ``(address, length)`` giving the current memory address and the
		length in elements of the buffer used to hold array's contents.  The size of the
		memory buffer in bytes can be computed as ``array.buffer_info()[1] *
		array.itemsize``.  This is occasionally useful when working with low-level (and
		inherently unsafe) I/O interfaces that require memory addresses, such as certain
		:cfunc:`ioctl` operations.  The returned numbers are valid as long as the array
		exists and no length-changing operations are applied to it.
		
		"""
		pass
		
	def byteswap(self, ):
		"""
		"Byteswap" all items of the array.  This is only supported for values which are
		1, 2, 4, or 8 bytes in size; for other types of values, :exc:`RuntimeError` is
		raised.  It is useful when reading data from a file written on a machine with a
		different byte order.
		
		
		"""
		pass
		
	def count(self, x):
		"""
		Return the number of occurrences of *x* in the array.
		
		
		"""
		pass
		
	def extend(self, iterable):
		"""
		Append items from *iterable* to the end of the array.  If *iterable* is another
		array, it must have *exactly* the same type code; if not, :exc:`TypeError` will
		be raised.  If *iterable* is not an array, it must be iterable and its elements
		must be the right type to be appended to the array.
		
		"""
		pass
		
	def _fromfile(self, f,n):
		"""
		Read *n* items (as machine values) from the file object *f* and append them to
		the end of the array.  If less than *n* items are available, :exc:`EOFError` is
		raised, but the items that were available are still inserted into the array.
		*f* must be a real built-in file object; something else with a :meth:`read`
		method won't do.
		
		
		"""
		pass
		
	def _fromlist(self, list):
		"""
		Append items from the list.  This is equivalent to ``for x in list:
		a.append(x)`` except that if there is a type error, the array is unchanged.
		
		
		"""
		pass
		
	def _fromstring(self, s):
		"""
		Appends items from the string, interpreting the string as an array of machine
		values (as if it had been read from a file using the :meth:`fromfile` method).
		
		
		"""
		pass
		
	def _fromunicode(self, s):
		"""
		Extends this array with data from the given unicode string.  The array must
		be a type ``'u'`` array; otherwise a :exc:`ValueError` is raised.  Use
		``array.fromstring(unicodestring.encode(enc))`` to append Unicode data to an
		array of some other type.
		
		
		"""
		pass
		
	def index(self, x):
		"""
		Return the smallest *i* such that *i* is the index of the first occurrence of
		*x* in the array.
		
		
		"""
		pass
		
	def insert(self, i,x):
		"""
		Insert a new item with value *x* in the array before position *i*. Negative
		values are treated as being relative to the end of the array.
		
		
		"""
		pass
		
	def pop(self, i):
		"""
		Removes the item with the index *i* from the array and returns it. The optional
		argument defaults to ``-1``, so that by default the last item is removed and
		returned.
		
		
		"""
		pass
		
	def read(self, f,n):
		"""
		"""
		pass
		
	def remove(self, x):
		"""
		Remove the first occurrence of *x* from the array.
		
		
		"""
		pass
		
	def reverse(self, ):
		"""
		Reverse the order of the items in the array.
		
		
		"""
		pass
		
	def tofile(self, f):
		"""
		Write all items (as machine values) to the file object *f*.
		
		
		"""
		pass
		
	def tolist(self, ):
		"""
		Convert the array to an ordinary list with the same items.
		
		
		"""
		pass
		
	def tostring(self, ):
		"""
		Convert the array to an array of machine values and return the string
		representation (the same sequence of bytes that would be written to a file by
		the :meth:`tofile` method.)
		
		
		"""
		pass
		
	def tounicode(self, ):
		"""
		Convert the array to a unicode string.  The array must be a type ``'u'`` array;
		otherwise a :exc:`ValueError` is raised. Use ``array.tostring().decode(enc)`` to
		obtain a unicode string from an array of some other type.
		
		
		"""
		pass
		
	def write(self, f):
		"""
		"""
		pass
		
	"""
	Obsolete alias for :class:`array`.
	
	Array objects support the ordinary sequence operations of indexing, slicing,
	concatenation, and multiplication.  When using slice assignment, the assigned
	value must be an array object with the same type code; in all other cases,
	:exc:`TypeError` is raised. Array objects also implement the buffer interface,
	and may be used wherever buffer objects are supported.
	
	The following data items and methods are also supported:
	
	"""
	ArrayType = None
	


