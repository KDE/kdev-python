#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
"""
.. *************
Built-in Types
**************

The following sections describe the standard types that are built into the
interpreter.

"""
class set:


	"""frozenset([iterable])
	
	Return a new set or frozenset object whose elements are taken from
	*iterable*.  The elements of a set must be hashable.  To represent sets of
	sets, the inner sets must be :class:`frozenset` objects.  If *iterable* is
	not specified, a new empty set is returned.
	
	Instances of :class:`set` and :class:`frozenset` provide the following
	operations:
	
	"""
	
	
	def __init__(self, iterable):
		pass
	
	


class dict:


	"""
	Return a new dictionary initialized from an optional positional argument or from
	a set of keyword arguments. If no arguments are given, return a new empty
	dictionary. If the positional argument *arg* is a mapping object, return a
	dictionary mapping the same keys to the same values as does the mapping object.
	Otherwise the positional argument must be a sequence, a container that supports
	iteration, or an iterator object.  The elements of the argument must each also
	be of one of those kinds, and each must in turn contain exactly two objects.
	The first is used as a key in the new dictionary, and the second as the key's
	value.  If a given key is seen more than once, the last value associated with it
	is retained in the new dictionary.
	
	If keyword arguments are given, the keywords themselves with their associated
	values are added as items to the dictionary. If a key is specified both in the
	positional argument and as a keyword argument, the value associated with the
	keyword is retained in the dictionary. For example, these all return a
	dictionary equal to ``{"one": 1, "two": 2}``:
	
	* ``dict(one=1, two=2)``
	* ``dict({'one': 1, 'two': 2})``
	* ``dict(zip(('one', 'two'), (1, 2)))``
	* ``dict([['two', 2], ['one', 1]])``
	
	The first example only works for keys that are valid Python
	identifiers; the others work with any valid keys.
	
	"""
	
	
	def __init__(self, arg):
		pass
	
	


class memoryview:


	"""
	Create a :class:`memoryview` that references *obj*.  *obj* must support the
	buffer protocol.  Built-in objects that support the buffer protocol include
	:class:`str` and :class:`bytearray` (but not :class:`unicode`).
	
	A :class:`memoryview` has the notion of an *element*, which is the
	atomic memory unit handled by the originating object *obj*.  For many
	simple types such as :class:`str` and :class:`bytearray`, an element
	is a single byte, but other third-party types may expose larger elements.
	
	``len(view)`` returns the total number of elements in the memoryview,
	*view*.  The :class:`~memoryview.itemsize` attribute will give you the
	number of bytes in a single element.
	
	A :class:`memoryview` supports slicing to expose its data.  Taking a single
	index will return a single element as a :class:`str` object.  Full
	slicing will result in a subview::
	
	>>> v = memoryview('abcefg')
	>>> v[1]
	'b'
	>>> v[-1]
	'g'
	>>> v[1:4]
	<memory at 0x77ab28>
	>>> v[1:4].tobytes()
	'bce'
	
	If the object the memoryview is over supports changing its data, the
	memoryview supports slice assignment::
	
	>>> data = bytearray('abcefg')
	>>> v = memoryview(data)
	>>> v.readonly
	False
	>>> v[0] = 'z'
	>>> data
	bytearray(b'zbcefg')
	>>> v[1:4] = '123'
	>>> data
	bytearray(b'z123fg')
	>>> v[2] = 'spam'
	Traceback (most recent call last):
	File "<stdin>", line 1, in <module>
	ValueError: cannot modify size of memoryview object
	
	Notice how the size of the memoryview object cannot be changed.
	
	:class:`memoryview` has two methods:
	
	"""
	
	
	def __init__(self, obj):
		pass
	
	


