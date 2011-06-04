#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
""":synopsis: Heap queue algorithm (a.k.a. priority queue).
"""
def heappush(heap,item):
	"""
	Push the value *item* onto the *heap*, maintaining the heap invariant.
	
	
	"""
	pass
	
def heappop(heap):
	"""
	Pop and return the smallest item from the *heap*, maintaining the heap
	invariant.  If the heap is empty, :exc:`IndexError` is raised.
	
	"""
	pass
	
def heappushpop(heap,item):
	"""
	Push *item* on the heap, then pop and return the smallest item from the
	*heap*.  The combined action runs more efficiently than :func:`heappush`
	followed by a separate call to :func:`heappop`.
	
	"""
	pass
	
def heapify(x):
	"""
	Transform list *x* into a heap, in-place, in linear time.
	
	
	"""
	pass
	
def heapreplace(heap,item):
	"""
	Pop and return the smallest item from the *heap*, and also push the new *item*.
	The heap size doesn't change. If the heap is empty, :exc:`IndexError` is raised.
	
	This one step operation is more efficient than a :func:`heappop` followed by
	:func:`heappush` and can be more appropriate when using a fixed-size heap.
	The pop/push combination always returns an element from the heap and replaces
	it with *item*.
	
	The value returned may be larger than the *item* added.  If that isn't
	desired, consider using :func:`heappushpop` instead.  Its push/pop
	combination returns the smaller of the two values, leaving the larger value
	on the heap.
	
	
	The module also offers three general purpose functions based on heaps.
	
	
	"""
	pass
	
def merge(iterables):
	"""
	Merge multiple sorted inputs into a single sorted output (for example, merge
	timestamped entries from multiple log files).  Returns an :term:`iterator`
	over the sorted values.
	
	Similar to ``sorted(itertools.chain(*iterables))`` but returns an iterable, does
	not pull the data into memory all at once, and assumes that each of the input
	streams is already sorted (smallest to largest).
	
	"""
	pass
	
def nlargest(n,iterable,key):
	"""
	Return a list with the *n* largest elements from the dataset defined by
	*iterable*.  *key*, if provided, specifies a function of one argument that is
	used to extract a comparison key from each element in the iterable:
	``key=str.lower`` Equivalent to:  ``sorted(iterable, key=key,
	reverse=True)[:n]``
	
	"""
	pass
	
def nsmallest(n,iterable,key):
	"""
	Return a list with the *n* smallest elements from the dataset defined by
	*iterable*.  *key*, if provided, specifies a function of one argument that is
	used to extract a comparison key from each element in the iterable:
	``key=str.lower`` Equivalent to:  ``sorted(iterable, key=key)[:n]``
	
	"""
	pass
	
