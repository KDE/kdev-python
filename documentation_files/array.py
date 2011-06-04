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
	
	
	def __init__(self, typecode,initializer):
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
	


