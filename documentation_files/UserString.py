#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
""":synopsis: Class wrapper for string objects.
"""
class UserString:


	"""
	Class that simulates a string or a Unicode string object.  The instance's
	content is kept in a regular string or Unicode string object, which is
	accessible via the :attr:`data` attribute of :class:`UserString` instances.  The
	instance's contents are initially set to a copy of *sequence*.  *sequence* can
	be either a regular Python string or Unicode string, an instance of
	:class:`UserString` (or a subclass) or an arbitrary sequence which can be
	converted into a string using the built-in :func:`str` function.
	
	"""
	
	
	def __init__(self, sequence):
		pass
	
	


class MutableString:


	"""
	This class is derived from the :class:`UserString` above and redefines strings
	to be *mutable*.  Mutable strings can't be used as dictionary keys, because
	dictionaries require *immutable* objects as keys.  The main intention of this
	class is to serve as an educational example for inheritance and necessity to
	remove (override) the :meth:`__hash__` method in order to trap attempts to use a
	mutable object as dictionary key, which would be otherwise very error prone and
	hard to track down.
	
	"""
	
	
	def __init__(self, sequence):
		pass
	
	


