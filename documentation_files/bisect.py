#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
""":synopsis: Array bisection algorithms for binary searching.
"""
def bisect_left(a,x,lo=0,hi=len(a)):
	"""
	Locate the insertion point for *x* in *a* to maintain sorted order.
	The parameters *lo* and *hi* may be used to specify a subset of the list
	which should be considered; by default the entire list is used.  If *x* is
	already present in *a*, the insertion point will be before (to the left of)
	any existing entries.  The return value is suitable for use as the first
	parameter to ``list.insert()`` assuming that *a* is already sorted.
	
	The returned insertion point *i* partitions the array *a* into two halves so
	that ``all(val < x for val in a[lo:i])`` for the left side and
	``all(val >= x for val in a[i:hi])`` for the right side.
	
	"""
	pass
	
def bisect_right(a,x,lo=0,hi=len(a)):
	"""bisect(a, x, lo=0, hi=len(a))
	
	Similar to :func:`bisect_left`, but returns an insertion point which comes
	after (to the right of) any existing entries of *x* in *a*.
	
	The returned insertion point *i* partitions the array *a* into two halves so
	that ``all(val <= x for val in a[lo:i])`` for the left side and
	``all(val > x for val in a[i:hi])`` for the right side.
	
	"""
	pass
	
def insort_left(a,x,lo=0,hi=len(a)):
	"""
	Insert *x* in *a* in sorted order.  This is equivalent to
	``a.insert(bisect.bisect_left(a, x, lo, hi), x)`` assuming that *a* is
	already sorted.  Keep in mind that the O(log n) search is dominated by
	the slow O(n) insertion step.
	
	"""
	pass
	
def insort_right(a,x,lo=0,hi=len(a)):
	"""insort(a, x, lo=0, hi=len(a))
	
	Similar to :func:`insort_left`, but inserting *x* in *a* after any existing
	entries of *x*.
	
	"""
	pass
	
