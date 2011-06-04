#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
""":synopsis: Abstract Syntax Tree classes and manipulation.

"""
class AST:


	"""
	This is the base of all AST node classes.  The actual node classes are
	derived from the :file:`Parser/Python.asdl` file, which is reproduced
	:ref:`below <abstract-grammar>`.  They are defined in the :mod:`_ast` C
	module and re-exported in :mod:`ast`.
	
	There is one class defined for each left-hand side symbol in the abstract
	grammar (for example, :class:`ast.stmt` or :class:`ast.expr`).  In addition,
	there is one class defined for each constructor on the right-hand side; these
	classes inherit from the classes for the left-hand side trees.  For example,
	:class:`ast.BinOp` inherits from :class:`ast.expr`.  For production rules
	with alternatives (aka "sums"), the left-hand side class is abstract: only
	instances of specific constructor nodes are ever created.
	
	"""
	
	
	def __init__(self, ):
		pass
	
	def parse(self, source,filename='"unknown"',mode='exec'):
		"""
		Parse the source into an AST node.  Equivalent to ``compile(source,
		filename, mode, ast.PyCF_ONLY_AST)``.
		
		
		"""
		pass
		
	def literal_eval(self, node_or_string):
		"""
		Safely evaluate an expression node or a string containing a Python
		expression.  The string or node provided may only consist of the following
		Python literal structures: strings, numbers, tuples, lists, dicts, booleans,
		and ``None``.
		
		This can be used for safely evaluating strings containing Python expressions
		from untrusted sources without the need to parse the values oneself.
		
		
		"""
		pass
		
	def get_docstring(self, node,clean=True):
		"""
		Return the docstring of the given *node* (which must be a
		:class:`FunctionDef`, :class:`ClassDef` or :class:`Module` node), or ``None``
		if it has no docstring.  If *clean* is true, clean up the docstring's
		indentation with :func:`inspect.cleandoc`.
		
		
		"""
		pass
		
	def fix_missing_locations(self, node):
		"""
		When you compile a node tree with :func:`compile`, the compiler expects
		:attr:`lineno` and :attr:`col_offset` attributes for every node that supports
		them.  This is rather tedious to fill in for generated nodes, so this helper
		adds these attributes recursively where not already set, by setting them to
		the values of the parent node.  It works recursively starting at *node*.
		
		
		"""
		pass
		
	def increment_lineno(self, node,n=1):
		"""
		Increment the line number of each node in the tree starting at *node* by *n*.
		This is useful to "move code" to a different location in a file.
		
		
		"""
		pass
		
	def copy_location(self, new_node,old_node):
		"""
		Copy source location (:attr:`lineno` and :attr:`col_offset`) from *old_node*
		to *new_node* if possible, and return *new_node*.
		
		
		"""
		pass
		
	def iter_fields(self, node):
		"""
		Yield a tuple of ``(fieldname, value)`` for each field in ``node._fields``
		that is present on *node*.
		
		
		"""
		pass
		
	def iter_child_nodes(self, node):
		"""
		Yield all direct child nodes of *node*, that is, all fields that are nodes
		and all items of fields that are lists of nodes.
		
		
		"""
		pass
		
	def walk(self, node):
		"""
		Recursively yield all descendant nodes in the tree starting at *node*
		(including *node* itself), in no specified order.  This is useful if you only
		want to modify nodes in place and don't care about the context.
		
		
		"""
		pass
		
	


class NodeVisitor:


	"""
	A node visitor base class that walks the abstract syntax tree and calls a
	visitor function for every node found.  This function may return a value
	which is forwarded by the :meth:`visit` method.
	
	This class is meant to be subclassed, with the subclass adding visitor
	methods.
	
	"""
	
	
	def __init__(self, ):
		pass
	
	def visit(self, node):
		"""
		Visit a node.  The default implementation calls the method called
		:samp:`self.visit_{classname}` where *classname* is the name of the node
		class, or :meth:`generic_visit` if that method doesn't exist.
		
		"""
		pass
		
	def generic_visit(self, node):
		"""
		This visitor calls :meth:`visit` on all children of the node.
		
		Note that child nodes of nodes that have a custom visitor method won't be
		visited unless the visitor calls :meth:`generic_visit` or visits them
		itself.
		
		Don't use the :class:`NodeVisitor` if you want to apply changes to nodes
		during traversal.  For this a special visitor exists
		(:class:`NodeTransformer`) that allows modifications.
		
		
		"""
		pass
		
	


class NodeTransformer:


	"""
	A :class:`NodeVisitor` subclass that walks the abstract syntax tree and
	allows modification of nodes.
	
	The :class:`NodeTransformer` will walk the AST and use the return value of
	the visitor methods to replace or remove the old node.  If the return value
	of the visitor method is ``None``, the node will be removed from its
	location, otherwise it is replaced with the return value.  The return value
	may be the original node in which case no replacement takes place.
	
	Here is an example transformer that rewrites all occurrences of name lookups
	(``foo``) to ``data['foo']``::
	
	class RewriteName(NodeTransformer):
	
	def visit_Name(self, node):
	return copy_location(Subscript(
	value=Name(id='data', ctx=Load()),
	slice=Index(value=Str(s=node.id)),
	ctx=node.ctx
	), node)
	
	Keep in mind that if the node you're operating on has child nodes you must
	either transform the child nodes yourself or call the :meth:`generic_visit`
	method for the node first.
	
	For nodes that were part of a collection of statements (that applies to all
	statement nodes), the visitor may also return a list of nodes rather than
	just a single node.
	
	Usually you use the transformer like this::
	
	node = YourTransformer().visit(node)
	
	
	"""
	
	
	def __init__(self, ):
		pass
	
	


