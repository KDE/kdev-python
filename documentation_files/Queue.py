#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
""":synopsis: A synchronized queue class.

"""
class Queue:


	"""
	Constructor for a FIFO queue.  *maxsize* is an integer that sets the upperbound
	limit on the number of items that can be placed in the queue.  Insertion will
	block once this size has been reached, until queue items are consumed.  If
	*maxsize* is less than or equal to zero, the queue size is infinite.
	
	"""
	
	
	def __init__(self, maxsize=0):
		pass
	
	


class LifoQueue:


	"""
	Constructor for a LIFO queue.  *maxsize* is an integer that sets the upperbound
	limit on the number of items that can be placed in the queue.  Insertion will
	block once this size has been reached, until queue items are consumed.  If
	*maxsize* is less than or equal to zero, the queue size is infinite.
	
	"""
	
	
	def __init__(self, maxsize=0):
		pass
	
	


class PriorityQueue:


	"""
	Constructor for a priority queue.  *maxsize* is an integer that sets the upperbound
	limit on the number of items that can be placed in the queue.  Insertion will
	block once this size has been reached, until queue items are consumed.  If
	*maxsize* is less than or equal to zero, the queue size is infinite.
	
	The lowest valued entries are retrieved first (the lowest valued entry is the
	one returned by ``sorted(list(entries))[0]``).  A typical pattern for entries
	is a tuple in the form: ``(priority_number, data)``.
	
	"""
	
	
	def __init__(self, maxsize=0):
		pass
	
	


