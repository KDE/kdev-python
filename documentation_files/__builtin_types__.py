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
	
	
	def __init__(self, ):
		pass
	
	def isdisjoint(self, other):
		"""
		Return True if the set has no elements in common with *other*.  Sets are
		disjoint if and only if their intersection is the empty set.
		
		"""
		pass
		
	def issubset(self, other):
		"""set <= other
		
		Test whether every element in the set is in *other*.
		
		"""
		pass
		
	def set"other(self, ():
		"""
		Test whether the set is a true subset of *other*, that is,
		``set <= other and set != other``.
		
		"""
		pass
		
	def issuperset(self, other):
		"""set >= other
		
		Test whether every element in *other* is in the set.
		
		"""
		pass
		
	def set"other(self, ():
		"""
		Test whether the set is a true superset of *other*, that is, ``set >=
		other and set != other``.
		
		"""
		pass
		
	def union(self, other,more):
		"""set | other | more
		
		Return a new set with elements from the set and all others.
		
		"""
		pass
		
	def intersection(self, other,more):
		"""set & other & more
		
		Return a new set with elements common to the set and all others.
		
		"""
		pass
		
	def difference(self, other,more):
		"""set - other - more
		
		Return a new set with elements in the set that are not in the others.
		
		"""
		pass
		
	def symmetric_difference(self, other):
		"""set ^ other
		
		Return a new set with elements in either the set or *other* but not both.
		
		"""
		pass
		
	def copy(self, ):
		"""
		Return a new set with a shallow copy of *s*.
		
		
		Note, the non-operator versions of :meth:`union`, :meth:`intersection`,
		:meth:`difference`, and :meth:`symmetric_difference`, :meth:`issubset`, and
		:meth:`issuperset` methods will accept any iterable as an argument.  In
		contrast, their operator based counterparts require their arguments to be
		sets.  This precludes error-prone constructions like ``set('abc') & 'cbs'``
		in favor of the more readable ``set('abc').intersection('cbs')``.
		
		Both :class:`set` and :class:`frozenset` support set to set comparisons. Two
		sets are equal if and only if every element of each set is contained in the
		other (each is a subset of the other). A set is less than another set if and
		only if the first set is a proper subset of the second set (is a subset, but
		is not equal). A set is greater than another set if and only if the first set
		is a proper superset of the second set (is a superset, but is not equal).
		
		Instances of :class:`set` are compared to instances of :class:`frozenset`
		based on their members.  For example, ``set('abc') == frozenset('abc')``
		returns ``True`` and so does ``set('abc') in set([frozenset('abc')])``.
		
		The subset and equality comparisons do not generalize to a complete ordering
		function.  For example, any two disjoint sets are not equal and are not
		subsets of each other, so *all* of the following return ``False``: ``a<b``,
		``a==b``, or ``a>b``. Accordingly, sets do not implement the :meth:`__cmp__`
		method.
		
		Since sets only define partial ordering (subset relationships), the output of
		the :meth:`list.sort` method is undefined for lists of sets.
		
		Set elements, like dictionary keys, must be :term:`hashable`.
		
		Binary operations that mix :class:`set` instances with :class:`frozenset`
		return the type of the first operand.  For example: ``frozenset('ab') |
		set('bc')`` returns an instance of :class:`frozenset`.
		
		The following table lists operations available for :class:`set` that do not
		apply to immutable instances of :class:`frozenset`:
		
		"""
		pass
		
	def update(self, other,more):
		"""set |= other | more
		
		Update the set, adding elements from all others.
		
		"""
		pass
		
	def intersection_update(self, other,more):
		"""set &= other & more
		
		Update the set, keeping only elements found in it and all others.
		
		"""
		pass
		
	def difference_update(self, other,more):
		"""set -= other | more
		
		Update the set, removing elements found in others.
		
		"""
		pass
		
	def symmetric_difference_update(self, other):
		"""set ^= other
		
		Update the set, keeping only elements found in either set, but not in both.
		
		"""
		pass
		
	def add(self, elem):
		"""
		Add element *elem* to the set.
		
		"""
		pass
		
	def remove(self, elem):
		"""
		Remove element *elem* from the set.  Raises :exc:`KeyError` if *elem* is
		not contained in the set.
		
		"""
		pass
		
	def discard(self, elem):
		"""
		Remove element *elem* from the set if it is present.
		
		"""
		pass
		
	def pop(self, ):
		"""
		Remove and return an arbitrary element from the set.  Raises
		:exc:`KeyError` if the set is empty.
		
		"""
		pass
		
	def clear(self, ):
		"""
		Remove all elements from the set.
		
		
		Note, the non-operator versions of the :meth:`update`,
		:meth:`intersection_update`, :meth:`difference_update`, and
		:meth:`symmetric_difference_update` methods will accept any iterable as an
		argument.
		
		Note, the *elem* argument to the :meth:`__contains__`, :meth:`remove`, and
		:meth:`discard` methods may be a set.  To support searching for an equivalent
		frozenset, the *elem* set is temporarily mutated during the search and then
		restored.  During the search, the *elem* set should not be read or mutated
		since it does not have a meaningful value.
		
		
		"""
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
	
	
	def __init__(self, ):
		pass
	
	def clear(self, ):
		"""
		Remove all items from the dictionary.
		
		"""
		pass
		
	def copy(self, ):
		"""
		Return a shallow copy of the dictionary.
		
		"""
		pass
		
	def _fromkeys(self, seq,value):
		"""
		Create a new dictionary with keys from *seq* and values set to *value*.
		
		:func:`fromkeys` is a class method that returns a new dictionary. *value*
		defaults to ``None``.
		
		"""
		pass
		
	def get(self, key,default):
		"""
		Return the value for *key* if *key* is in the dictionary, else *default*.
		If *default* is not given, it defaults to ``None``, so that this method
		never raises a :exc:`KeyError`.
		
		"""
		pass
		
	def has_key(self, key):
		"""
		Test for the presence of *key* in the dictionary.  :meth:`has_key` is
		deprecated in favor of ``key in d``.
		
		"""
		pass
		
	def items(self, ):
		"""
		Return a copy of the dictionary's list of ``(key, value)`` pairs.
		
		"""
		pass
		
	def iteritems(self, ):
		"""
		Return an iterator over the dictionary's ``(key, value)`` pairs.  See the
		note for :meth:`dict.items`.
		
		Using :meth:`iteritems` while adding or deleting entries in the dictionary
		may raise a :exc:`RuntimeError` or fail to iterate over all entries.
		
		"""
		pass
		
	def iterkeys(self, ):
		"""
		Return an iterator over the dictionary's keys.  See the note for
		:meth:`dict.items`.
		
		Using :meth:`iterkeys` while adding or deleting entries in the dictionary
		may raise a :exc:`RuntimeError` or fail to iterate over all entries.
		
		"""
		pass
		
	def itervalues(self, ):
		"""
		Return an iterator over the dictionary's values.  See the note for
		:meth:`dict.items`.
		
		Using :meth:`itervalues` while adding or deleting entries in the
		dictionary may raise a :exc:`RuntimeError` or fail to iterate over all
		entries.
		
		"""
		pass
		
	def keys(self, ):
		"""
		Return a copy of the dictionary's list of keys.  See the note for
		:meth:`dict.items`.
		
		"""
		pass
		
	def pop(self, key,default):
		"""
		If *key* is in the dictionary, remove it and return its value, else return
		*default*.  If *default* is not given and *key* is not in the dictionary,
		a :exc:`KeyError` is raised.
		
		"""
		pass
		
	def popitem(self, ):
		"""
		Remove and return an arbitrary ``(key, value)`` pair from the dictionary.
		
		:func:`popitem` is useful to destructively iterate over a dictionary, as
		often used in set algorithms.  If the dictionary is empty, calling
		:func:`popitem` raises a :exc:`KeyError`.
		
		"""
		pass
		
	def setdefault(self, key,default):
		"""
		If *key* is in the dictionary, return its value.  If not, insert *key*
		with a value of *default* and return *default*.  *default* defaults to
		``None``.
		
		"""
		pass
		
	def update(self, other):
		"""
		Update the dictionary with the key/value pairs from *other*, overwriting
		existing keys.  Return ``None``.
		
		:func:`update` accepts either another dictionary object or an iterable of
		key/value pairs (as tuples or other iterables of length two).  If keyword
		arguments are specified, the dictionary is then updated with those
		key/value pairs: ``d.update(red=1, blue=2)``.
		
		"""
		pass
		
	def values(self, ):
		"""
		Return a copy of the dictionary's list of values.  See the note for
		:meth:`dict.items`.
		
		"""
		pass
		
	def viewitems(self, ):
		"""
		Return a new view of the dictionary's items (``(key, value)`` pairs).  See
		below for documentation of view objects.
		
		"""
		pass
		
	def viewkeys(self, ):
		"""
		Return a new view of the dictionary's keys.  See below for documentation of
		view objects.
		
		"""
		pass
		
	def viewvalues(self, ):
		"""
		Return a new view of the dictionary's values.  See below for documentation of
		view objects.
		
		"""
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
	
	
	def __init__(self, ):
		pass
	
	def tobytes(self, ):
		"""
		Return the data in the buffer as a bytestring (an object of class
		:class:`str`). ::
		
		>>> m = memoryview("abc")
		>>> m.tobytes()
		'abc'
		
		"""
		pass
		
	def tolist(self, ):
		"""
		Return the data in the buffer as a list of integers. ::
		
		>>> memoryview("abc").tolist()
		[97, 98, 99]
		
		There are also several readonly attributes available:
		
		"""
		pass
		
	


