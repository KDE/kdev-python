#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
""":synopsis: Alternate repr() implementation with size limits.
"""
class Repr:


	"""
	Class which provides formatting services useful in implementing functions
	similar to the built-in :func:`repr`; size limits for  different object types
	are added to avoid the generation of representations which are excessively long.
	
	
	"""
	
	
	def __init__(self, ):
		pass
	
	def repr(obj):
		"""
		This is the :meth:`~Repr.repr` method of ``aRepr``.  It returns a string
		similar to that returned by the built-in function of the same name, but with
		limits on most sizes.
		
		
		.. epr Objects
		------------
		
		:class:`Repr` instances provide several members which can be used to provide
		size limits for the representations of different object types,  and methods
		which format specific object types.
		
		
		"""
		pass
		
	"""
	This is an instance of :class:`Repr` which is used to provide the :func:`.repr`
	function described below.  Changing the attributes of this object will affect
	the size limits used by :func:`.repr` and the Python debugger.
	
	
	"""
	aRepr = None
	


