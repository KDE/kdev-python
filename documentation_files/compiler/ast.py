#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
"""

The :mod:`compiler.ast` module is generated from a text file that describes each
node type and its elements.  Each node type is represented as a class that
inherits from the abstract base class :class:`compiler.ast.Node` and defines a
set of named attributes for child nodes.


"""
class Node:


	"""
	The :class:`Node` instances are created automatically by the parser generator.
	The recommended interface for specific :class:`Node` instances is to use the
	public attributes to access child nodes.  A public attribute may be bound to a
	single node or to a sequence of nodes, depending on the :class:`Node` type.  For
	example, the :attr:`bases` attribute of the :class:`Class` node, is bound to a
	list of base class nodes, and the :attr:`doc` attribute is bound to a single
	node.
	
	Each :class:`Node` instance has a :attr:`lineno` attribute which may be
	``None``.  XXX Not sure what the rules are for which nodes will have a useful
	lineno.
	
	All :class:`Node` objects offer the following methods:
	
	
	"""
	
	
	def __init__(self, ):
		pass
	
	


