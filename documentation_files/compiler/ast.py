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
	
	def getChildren(self, ):
		"""
		Returns a flattened list of the child nodes and objects in the order they
		occur.  Specifically, the order of the nodes is the order in which they
		appear in the Python grammar.  Not all of the children are :class:`Node`
		instances.  The names of functions and classes, for example, are plain
		strings.
		
		
		"""
		pass
		
	def getChildNodes(self, ):
		"""
		Returns a flattened list of the child nodes in the order they occur.  This
		method is like :meth:`getChildren`, except that it only returns those
		children that are :class:`Node` instances.
		
		
		Two examples illustrate the general structure of :class:`Node` classes.  The
		"""
		pass
		
	


