#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
""":synopsis: Access parse trees for Python source code.
"""
"""
The type of the objects returned by :func:`expr`, :func:`suite` and
:func:`sequence2st`.

ST objects have the following methods:


"""
STType = None
def expr(source):
	"""
	The :func:`expr` function parses the parameter *source* as if it were an input
	to ``compile(source, 'file.py', 'eval')``.  If the parse succeeds, an ST object
	is created to hold the internal parse tree representation, otherwise an
	appropriate exception is raised.
	
	
	"""
	pass
	
def suite(source):
	"""
	The :func:`suite` function parses the parameter *source* as if it were an input
	to ``compile(source, 'file.py', 'exec')``.  If the parse succeeds, an ST object
	is created to hold the internal parse tree representation, otherwise an
	appropriate exception is raised.
	
	
	"""
	pass
	
def sequence2st(sequence):
	"""
	This function accepts a parse tree represented as a sequence and builds an
	internal representation if possible.  If it can validate that the tree conforms
	to the Python grammar and all nodes are valid node types in the host version of
	Python, an ST object is created from the internal representation and returned
	to the called.  If there is a problem creating the internal representation, or
	if the tree cannot be validated, a :exc:`ParserError` exception is raised.  An
	ST object created this way should not be assumed to compile correctly; normal
	exceptions raised by compilation may still be initiated when the ST object is
	passed to :func:`compilest`.  This may indicate problems not related to syntax
	(such as a :exc:`MemoryError` exception), but may also be due to constructs such
	as the result of parsing ``del f(0)``, which escapes the Python parser but is
	checked by the bytecode compiler.
	
	Sequences representing terminal tokens may be represented as either two-element
	lists of the form ``(1, 'name')`` or as three-element lists of the form ``(1,
	'name', 56)``.  If the third element is present, it is assumed to be a valid
	line number.  The line number may be specified for any subset of the terminal
	symbols in the input tree.
	
	
	"""
	pass
	
def tuple2st(sequence):
	"""
	This is the same function as :func:`sequence2st`.  This entry point is
	maintained for backward compatibility.
	
	
	.. onverting ST Objects
	---------------------
	
	ST objects, regardless of the input used to create them, may be converted to
	parse trees represented as list- or tuple- trees, or may be compiled into
	executable code objects.  Parse trees may be extracted with or without line
	numbering information.
	
	
	"""
	pass
	
def st2list(ast,line_info):
	"""
	This function accepts an ST object from the caller in *ast* and returns a
	Python list representing the equivalent parse tree.  The resulting list
	representation can be used for inspection or the creation of a new parse tree in
	list form.  This function does not fail so long as memory is available to build
	the list representation.  If the parse tree will only be used for inspection,
	:func:`st2tuple` should be used instead to reduce memory consumption and
	fragmentation.  When the list representation is required, this function is
	significantly faster than retrieving a tuple representation and converting that
	to nested lists.
	
	If *line_info* is true, line number information will be included for all
	terminal tokens as a third element of the list representing the token.  Note
	that the line number provided specifies the line on which the token *ends*.
	This information is omitted if the flag is false or omitted.
	
	
	"""
	pass
	
def st2tuple(ast,line_info):
	"""
	This function accepts an ST object from the caller in *ast* and returns a
	Python tuple representing the equivalent parse tree.  Other than returning a
	tuple instead of a list, this function is identical to :func:`st2list`.
	
	If *line_info* is true, line number information will be included for all
	terminal tokens as a third element of the list representing the token.  This
	information is omitted if the flag is false or omitted.
	
	
	"""
	pass
	
def compilest(ast,filename='"syntax_tree"'):
	"""
	"""
	pass
	
def isexpr(ast):
	"""
	"""
	pass
	
def issuite(ast):
	"""
	This function mirrors :func:`isexpr` in that it reports whether an ST object
	represents an ``'exec'`` form, commonly known as a "suite."  It is not safe to
	assume that this function is equivalent to ``not isexpr(ast)``, as additional
	syntactic fragments may be supported in the future.
	
	
	.. xceptions and Error Handling
	-----------------------------
	
	The parser module defines a single exception, but may also pass other built-in
	exceptions from other portions of the Python runtime environment.  See each
	function for information about the exceptions it can raise.
	
	
	"""
	pass
	
