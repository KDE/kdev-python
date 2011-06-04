#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
"""

The visitor pattern is *more  The :mod:`compiler` package uses a variant on the
visitor pattern that takes advantage of Python's introspection features to
eliminate the need for much of the visitor's infrastructure.

The classes being visited do not need to be programmed to accept visitors.  The
visitor need only define visit methods for classes it is specifically interested
in; a default visit method can handle the rest.

XXX The magic :meth:`visit` method for visitors.


"""
class ASTVisitor:


	"""
	The :class:`ASTVisitor` is responsible for walking over the tree in the correct
	order.  A walk begins with a call to :meth:`preorder`.  For each node, it checks
	the *visitor* argument to :meth:`preorder` for a method named 'visitNodeType,'
	where NodeType is the name of the node's class, e.g. for a :class:`While` node a
	:meth:`visitWhile` would be called.  If the method exists, it is called with the
	node as its first argument.
	
	The visitor method for a particular node type can control how child nodes are
	visited during the walk.  The :class:`ASTVisitor` modifies the visitor argument
	by adding a visit method to the visitor; this method can be used to visit a
	particular child node.  If no visitor is found for a particular node type, the
	:meth:`default` method is called.
	
	:class:`ASTVisitor` objects have the following methods:
	
	XXX describe extra arguments
	
	
	"""
	
	
	def __init__(self, ):
		pass
	
	


