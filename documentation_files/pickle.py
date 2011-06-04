#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
""":synopsis: Convert Python objects to streams of bytes and back.
"""
"""
The highest protocol version available.  This value can be passed as a
*protocol* value.

"""
HIGHEST_PROTOCOL = None
def dump(obj,file,protocol):
	"""
	Write a pickled representation of *obj* to the open file object *file*.  This is
	equivalent to ``Pickler(file, protocol).dump(obj)``.
	
	If the *protocol* parameter is omitted, protocol 0 is used. If *protocol* is
	specified as a negative value or :const:`HIGHEST_PROTOCOL`, the highest protocol
	version will be used.
	
	"""
	pass
	
def load(file):
	"""
	Read a string from the open file object *file* and interpret it as a pickle data
	stream, reconstructing and returning the original object hierarchy.  This is
	equivalent to ``Unpickler(file).load()``.
	
	*file* must have two methods, a :meth:`read` method that takes an integer
	argument, and a :meth:`readline` method that requires no arguments.  Both
	methods should return a string.  Thus *file* can be a file object opened for
	reading, a :mod:`StringIO` object, or any other custom object that meets this
	interface.
	
	This function automatically determines whether the data stream was written in
	binary mode or not.
	
	
	"""
	pass
	
def dumps(obj,protocol):
	"""
	Return the pickled representation of the object as a string, instead of writing
	it to a file.
	
	If the *protocol* parameter is omitted, protocol 0 is used. If *protocol* is
	specified as a negative value or :const:`HIGHEST_PROTOCOL`, the highest protocol
	version will be used.
	
	"""
	pass
	
def loads(string):
	"""
	Read a pickled object hierarchy from a string.  Characters in the string past
	the pickled object's representation are ignored.
	
	The :mod:`pickle` module also defines three exceptions:
	
	
	"""
	pass
	
class Pickler:


	"""
	This takes a file-like object to which it will write a pickle data stream.
	
	If the *protocol* parameter is omitted, protocol 0 is used. If *protocol* is
	specified as a negative value or :const:`HIGHEST_PROTOCOL`, the highest
	protocol version will be used.
	
	"""
	
	
	def __init__(self, file,protocol):
		pass
	
	


class Unpickler:


	"""
	This takes a file-like object from which it will read a pickle data stream.
	This class automatically determines whether the data stream was written in
	binary mode or not, so it does not need a flag as in the :class:`Pickler`
	factory.
	
	*file* must have two methods, a :meth:`read` method that takes an integer
	argument, and a :meth:`readline` method that requires no arguments.  Both
	methods should return a string.  Thus *file* can be a file object opened for
	reading, a :mod:`StringIO` object, or any other custom object that meets this
	interface.
	
	:class:`Unpickler` objects have one (or two) public methods:
	
	
	"""
	
	
	def __init__(self, file):
		pass
	
	


