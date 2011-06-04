#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
""":synopsis: Implementation of sets of unique elements.
:deprecated:
"""
class Set:


	"""
	Constructs a new empty :class:`Set` object.  If the optional *iterable*
	parameter is supplied, updates the set with elements obtained from iteration.
	All of the elements in *iterable* should be immutable or be transformable to an
	immutable using the protocol described in section :ref:`immutable-transforms`.
	
	
	"""
	
	
	def __init__(self, ):
		pass
	
	


class ImmutableSet:


	"""
	Constructs a new empty :class:`ImmutableSet` object.  If the optional *iterable*
	parameter is supplied, updates the set with elements obtained from iteration.
	All of the elements in *iterable* should be immutable or be transformable to an
	immutable using the protocol described in section :ref:`immutable-transforms`.
	
	Because :class:`ImmutableSet` objects provide a :meth:`__hash__` method, they
	can be used as set elements or as dictionary keys.  :class:`ImmutableSet`
	objects do not have methods for adding or removing elements, so all of the
	elements must be known when the constructor is called.
	
	
	.. et Objects
	-----------
	
	Instances of :class:`Set` and :class:`ImmutableSet` both provide the following
	operations:
	
	+-------------------------------+------------+---------------------------------+
	| Operation                     | Equivalent | Result                          |
	+===============================+============+=================================+
	| ``len(s)``                    |            | cardinality of set *s*          |
	+-------------------------------+------------+---------------------------------+
	| ``x in s``                    |            | test *x* for membership in *s*  |
	+-------------------------------+------------+---------------------------------+
	| ``x not in s``                |            | test *x* for non-membership in  |
	|                               |            | *s*                             |
	+-------------------------------+------------+---------------------------------+
	| ``s.issubset(t)``             | ``s <= t`` | test whether every element in   |
	|                               |            | *s* is in *t*                   |
	+-------------------------------+------------+---------------------------------+
	| ``s.issuperset(t)``           | ``s >= t`` | test whether every element in   |
	|                               |            | *t* is in *s*                   |
	+-------------------------------+------------+---------------------------------+
	| ``s.union(t)``                | ``s | t``  | new set with elements from both |
	|                               |            | *s* and *t*                     |
	+-------------------------------+------------+---------------------------------+
	| ``s.intersection(t)``         | ``s & t``  | new set with elements common to |
	|                               |            | *s* and *t*                     |
	+-------------------------------+------------+---------------------------------+
	| ``s.difference(t)``           | ``s - t``  | new set with elements in *s*    |
	|                               |            | but not in *t*                  |
	+-------------------------------+------------+---------------------------------+
	| ``s.symmetric_difference(t)`` | ``s ^ t``  | new set with elements in either |
	|                               |            | *s* or *t* but not both         |
	+-------------------------------+------------+---------------------------------+
	| ``s.copy()``                  |            | new set with a shallow copy of  |
	|                               |            | *s*                             |
	+-------------------------------+------------+---------------------------------+
	
	Note, the non-operator versions of :meth:`union`, :meth:`intersection`,
	:meth:`difference`, and :meth:`symmetric_difference` will accept any iterable as
	an argument. In contrast, their operator based counterparts require their
	arguments to be sets.  This precludes error-prone constructions like
	``Set('abc') & 'cbs'`` in favor of the more readable
	``Set('abc').intersection('cbs')``.
	
	"""
	
	
	def __init__(self, ):
		pass
	
	


