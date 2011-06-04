#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
""":synopsis: High-performance datatypes
"""
class Counter:


	"""
	A :class:`Counter` is a :class:`dict` subclass for counting hashable objects.
	It is an unordered collection where elements are stored as dictionary keys
	and their counts are stored as dictionary values.  Counts are allowed to be
	any integer value including zero or negative counts.  The :class:`Counter`
	class is similar to bags or multisets in other languages.
	
	Elements are counted from an *iterable* or initialized from another
	*mapping* (or counter):
	
	>>> c = Counter()                           # a new, empty counter
	>>> c = Counter('gallahad')                 # a new counter from an iterable
	>>> c = Counter({'red': 4, 'blue': 2})      # a new counter from a mapping
	>>> c = Counter(cats=4, dogs=8)             # a new counter from keyword args
	
	Counter objects have a dictionary interface except that they return a zero
	count for missing items instead of raising a :exc:`KeyError`:
	
	>>> c = Counter(['eggs', 'ham'])
	>>> c['bacon']                              # count of a missing element is zero
	0
	
	Setting a count to zero does not remove an element from a counter.
	Use ``del`` to remove it entirely:
	
	>>> c['sausage'] = 0                        # counter entry with a zero count
	>>> del c['sausage']                        # del actually removes the entry
	
	"""
	
	
	def __init__(self, ):
		pass
	
	def elements(self, ):
		"""
		Return an iterator over elements repeating each as many times as its
		count.  Elements are returned in arbitrary order.  If an element's count
		is less than one, :meth:`elements` will ignore it.
		
		>>> c = Counter(a=4, b=2, c=0, d=-2)
		>>> list(c.elements())
		['a', 'a', 'a', 'a', 'b', 'b']
		
		"""
		pass
		
	def most_common(self, n):
		"""
		Return a list of the *n* most common elements and their counts from the
		most common to the least.  If *n* is not specified, :func:`most_common`
		returns *all* elements in the counter.  Elements with equal counts are
		ordered arbitrarily:
		
		>>> Counter('abracadabra').most_common(3)
		[('a', 5), ('r', 2), ('b', 2)]
		
		"""
		pass
		
	def subtract(self, iterable_or_mapping):
		"""
		Elements are subtracted from an *iterable* or from another *mapping*
		(or counter).  Like :meth:`dict.update` but subtracts counts instead
		of replacing them.  Both inputs and outputs may be zero or negative.
		
		>>> c = Counter(a=4, b=2, c=0, d=-2)
		>>> d = Counter(a=1, b=2, c=3, d=4)
		>>> c.subtract(d)
		Counter({'a': 3, 'b': 0, 'c': -3, 'd': -6})
		
		The usual dictionary methods are available for :class:`Counter` objects
		except for two which work differently for counters.
		
		"""
		pass
		
	def _fromkeys(self, iterable):
		"""
		This class method is not implemented for :class:`Counter` objects.
		
		"""
		pass
		
	def update(self, iterable_or_mapping):
		"""
		Elements are counted from an *iterable* or added-in from another
		*mapping* (or counter).  Like :meth:`dict.update` but adds counts
		instead of replacing them.  Also, the *iterable* is expected to be a
		sequence of elements, not a sequence of ``(key, value)`` pairs.
		
		Common patterns for working with :class:`Counter` objects::
		"""
		pass
		
	


class deque:


	"""
	Returns a new deque object initialized left-to-right (using :meth:`append`) with
	data from *iterable*.  If *iterable* is not specified, the new deque is empty.
	
	Deques are a generalization of stacks and queues (the name is pronounced "deck"
	and is short for "double-ended queue").  Deques support thread-safe, memory
	efficient appends and pops from either side of the deque with approximately the
	same O(1) performance in either direction.
	
	Though :class:`list` objects support similar operations, they are optimized for
	fast fixed-length operations and incur O(n) memory movement costs for
	``pop(0)`` and ``insert(0, v)`` operations which change both the size and
	position of the underlying data representation.
	
	"""
	
	
	def __init__(self, ):
		pass
	
	def append(self, x):
		"""
		Add *x* to the right side of the deque.
		
		
		"""
		pass
		
	def appendleft(self, x):
		"""
		Add *x* to the left side of the deque.
		
		
		"""
		pass
		
	def clear(self, ):
		"""
		Remove all elements from the deque leaving it with length 0.
		
		
		"""
		pass
		
	def count(self, x):
		"""
		Count the number of deque elements equal to *x*.
		
		"""
		pass
		
	def extend(self, iterable):
		"""
		Extend the right side of the deque by appending elements from the iterable
		argument.
		
		
		"""
		pass
		
	def extendleft(self, iterable):
		"""
		Extend the left side of the deque by appending elements from *iterable*.
		Note, the series of left appends results in reversing the order of
		elements in the iterable argument.
		
		
		"""
		pass
		
	def pop(self, ):
		"""
		Remove and return an element from the right side of the deque. If no
		elements are present, raises an :exc:`IndexError`.
		
		
		"""
		pass
		
	def popleft(self, ):
		"""
		Remove and return an element from the left side of the deque. If no
		elements are present, raises an :exc:`IndexError`.
		
		
		"""
		pass
		
	def remove(self, value):
		"""
		Removed the first occurrence of *value*.  If not found, raises a
		:exc:`ValueError`.
		
		"""
		pass
		
	def reverse(self, ):
		"""
		Reverse the elements of the deque in-place and then return ``None``.
		
		"""
		pass
		
	def rotate(self, n):
		"""
		Rotate the deque *n* steps to the right.  If *n* is negative, rotate to
		the left.  Rotating one step to the right is equivalent to:
		``d.appendleft(d.pop())``.
		
		
		Deque objects also provide one read-only attribute:
		
		"""
		pass
		
	


class defaultdict:


	"""
	Returns a new dictionary-like object.  :class:`defaultdict` is a subclass of the
	built-in :class:`dict` class.  It overrides one method and adds one writable
	instance variable.  The remaining functionality is the same as for the
	:class:`dict` class and is not documented here.
	
	The first argument provides the initial value for the :attr:`default_factory`
	attribute; it defaults to ``None``. All remaining arguments are treated the same
	as if they were passed to the :class:`dict` constructor, including keyword
	arguments.
	
	"""
	
	
	def __init__(self, ):
		pass
	
	def __missing__(self, key):
		"""
		If the :attr:`default_factory` attribute is ``None``, this raises a
		:exc:`KeyError` exception with the *key* as argument.
		
		If :attr:`default_factory` is not ``None``, it is called without arguments
		to provide a default value for the given *key*, this value is inserted in
		the dictionary for the *key*, and returned.
		
		If calling :attr:`default_factory` raises an exception this exception is
		propagated unchanged.
		
		This method is called by the :meth:`__getitem__` method of the
		:class:`dict` class when the requested key is not found; whatever it
		returns or raises is then returned or raised by :meth:`__getitem__`.
		
		
		:class:`defaultdict` objects support the following instance variable:
		
		
		"""
		pass
		
	def namedtuple(self, typename,field_names,verbose=False,rename=False):
		"""
		Returns a new tuple subclass named *typename*.  The new subclass is used to
		create tuple-like objects that have fields accessible by attribute lookup as
		well as being indexable and iterable.  Instances of the subclass also have a
		helpful docstring (with typename and field_names) and a helpful :meth:`__repr__`
		method which lists the tuple contents in a ``name=value`` format.
		
		The *field_names* are a sequence of strings such as ``['x', 'y']``.
		Alternatively, *field_names* can be a single string with each fieldname
		separated by whitespace and/or commas, for example ``'x y'`` or ``'x, y'``.
		
		Any valid Python identifier may be used for a fieldname except for names
		starting with an underscore.  Valid identifiers consist of letters, digits,
		and underscores but do not start with a digit or underscore and cannot be
		a :mod:`keyword` such as *class*, *for*, *return*, *global*, *pass*, *print*,
		or *raise*.
		
		If *rename* is true, invalid fieldnames are automatically replaced
		with positional names.  For example, ``['abc', 'def', 'ghi', 'abc']`` is
		converted to ``['abc', '_1', 'ghi', '_3']``, eliminating the keyword
		``def`` and the duplicate fieldname ``abc``.
		
		If *verbose* is true, the class definition is printed just before being built.
		
		Named tuple instances do not have per-instance dictionaries, so they are
		lightweight and require no more memory than regular tuples.
		
		"""
		pass
		
	


class OrderedDict:


	"""
	Return an instance of a dict subclass, supporting the usual :class:`dict`
	methods.  An *OrderedDict* is a dict that remembers the order that keys
	were first inserted. If a new entry overwrites an existing entry, the
	original insertion position is left unchanged.  Deleting an entry and
	reinserting it will move it to the end.
	
	"""
	
	
	def __init__(self, ):
		pass
	
	def popitem(self, last=True):
		"""
		The :meth:`popitem` method for ordered dictionaries returns and removes
		a (key, value) pair.  The pairs are returned in LIFO order if *last* is
		true or FIFO order if false.
		
		In addition to the usual mapping methods, ordered dictionaries also support
		reverse iteration using :func:`reversed`.
		
		Equality tests between :class:`OrderedDict` objects are order-sensitive
		and are implemented as ``list(od1.items())==list(od2.items())``.
		Equality tests between :class:`OrderedDict` objects and other
		:class:`Mapping` objects are order-insensitive like regular dictionaries.
		This allows :class:`OrderedDict` objects to be substituted anywhere a
		regular dictionary is used.
		
		The :class:`OrderedDict` constructor and :meth:`update` method both accept
		keyword arguments, but their order is lost because Python's function call
		semantics pass-in keyword arguments using a regular unordered dictionary.
		
		"""
		pass
		
	


class Container:


	"""Hashable
	Sized
	Callable
	
	ABCs for classes that provide respectively the methods :meth:`__contains__`,
	:meth:`__hash__`, :meth:`__len__`, and :meth:`__call__`.
	
	"""
	
	
	def __init__(self, ):
		pass
	
	


class Iterable:


	"""
	ABC for classes that provide the :meth:`__iter__` method.
	See also the definition of :term:`iterable`.
	
	"""
	
	
	def __init__(self, ):
		pass
	
	


class Iterator:


	"""
	ABC for classes that provide the :meth:`__iter__` and :meth:`next` methods.
	See also the definition of :term:`iterator`.
	
	"""
	
	
	def __init__(self, ):
		pass
	
	


class Sequence:


	"""MutableSequence
	
	ABCs for read-only and mutable :term:`sequences <sequence>`.
	
	"""
	
	
	def __init__(self, ):
		pass
	
	


class Set:


	"""MutableSet
	
	ABCs for read-only and mutable sets.
	
	"""
	
	
	def __init__(self, ):
		pass
	
	


class Mapping:


	"""MutableMapping
	
	ABCs for read-only and mutable :term:`mappings <mapping>`.
	
	"""
	
	
	def __init__(self, ):
		pass
	
	


class MappingView:


	"""ItemsView
	KeysView
	ValuesView
	
	ABCs for mapping, items, keys, and values :term:`views <view>`.
	
	
	These ABCs allow us to ask classes or instances if they provide
	particular functionality, for example::
	
	size = None
	if isinstance(myvar, collections.Sized):
	size = len(myvar)
	
	Several of the ABCs are also useful as mixins that make it easier to develop
	classes supporting container APIs.  For example, to write a class supporting
	the full :class:`Set` API, it only necessary to supply the three underlying
	abstract methods: :meth:`__contains__`, :meth:`__iter__`, and :meth:`__len__`.
	The ABC supplies the remaining methods such as :meth:`__and__` and
	:meth:`isdisjoint` ::
	
	class ListBasedSet(collections.Set):
	''' Alternate set implementation favoring space over speed
	and not requiring the set elements to be hashable. '''
	def __init__(self, iterable):
	self.elements = lst = []
	for value in iterable:
	if value not in lst:
	lst.append(value)
	def __iter__(self):
	return iter(self.elements)
	def __contains__(self, value):
	return value in self.elements
	def __len__(self):
	return len(self.elements)
	
	s1 = ListBasedSet('abcdef')
	s2 = ListBasedSet('defghi')
	overlap = s1 & s2            # The __and__() method is supported automatically
	
	Notes on using :class:`Set` and :class:`MutableSet` as a mixin:
	
	(1)
	Since some set operations create new sets, the default mixin methods need
	a way to create new instances from an iterable. The class constructor is
	assumed to have a signature in the form ``ClassName(iterable)``.
	That assumption is factored-out to an internal classmethod called
	:meth:`_from_iterable` which calls ``cls(iterable)`` to produce a new set.
	If the :class:`Set` mixin is being used in a class with a different
	constructor signature, you will need to override :meth:`_from_iterable`
	with a classmethod that can construct new instances from
	an iterable argument.
	
	(2)
	To override the comparisons (presumably for speed, as the
	semantics are fixed), redefine :meth:`__le__` and
	then the other operations will automatically follow suit.
	
	(3)
	The :class:`Set` mixin provides a :meth:`_hash` method to compute a hash value
	for the set; however, :meth:`__hash__` is not defined because not all sets
	are hashable or immutable.  To add set hashabilty using mixins,
	inherit from both :meth:`Set` and :meth:`Hashable`, then define
	``__hash__ = Set._hash``.
	
	"""
	
	
	def __init__(self, ):
		pass
	
	


