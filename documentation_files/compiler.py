#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
""":synopsis: Python code compiler written in Python.
:deprecated:


The top-level of the package defines four functions.  If you import
:mod:`compiler`, you will get these functions and a collection of modules
contained in the package.


"""
def parse(buf):
	"""
	Returns an abstract syntax tree for the Python source code in *buf*. The
	function raises :exc:`SyntaxError` if there is an error in the source code.  The
	return value is a :class:`compiler.ast.Module` instance that contains the tree.
	
	
	"""
	pass
	
def parseFile(path):
	"""
	Return an abstract syntax tree for the Python source code in the file specified
	by *path*.  It is equivalent to ``parse(open(path).read())``.
	
	
	"""
	pass
	
def walk(ast,visitor,verbose):
	"""
	Do a pre-order walk over the abstract syntax tree *ast*.  Call the appropriate
	method on the *visitor* instance for each node encountered.
	
	
	"""
	pass
	
def compile(source,filename,mode,flags=None,dont_inherit=None):
	"""
	Compile the string *source*, a Python module, statement or expression, into a
	code object that can be executed by the exec statement or :func:`eval`. This
	function is a replacement for the built-in :func:`compile` function.
	
	The *filename* will be used for run-time error messages.
	
	The *mode* must be 'exec' to compile a module, 'single' to compile a single
	(interactive) statement, or 'eval' to compile an expression.
	
	The *flags* and *dont_inherit* arguments affect future-related statements, but
	are not supported yet.
	
	
	"""
	pass
	
def compileFile(source):
	"""
	Compiles the file *source* and generates a .pyc file.
	
	The :mod:`compiler` package contains the following modules: :mod:`ast`,
	:mod:`consts`, :mod:`future`, :mod:`misc`, :mod:`pyassem`, :mod:`pycodegen`,
	:mod:`symbols`, :mod:`transformer`, and :mod:`visitor`.
	
	
	Limitations
	===========
	
	There are some problems with the error checking of the compiler package.  The
	interpreter detects syntax errors in two distinct phases.  One set of errors is
	detected by the interpreter's parser, the other set by the compiler.  The
	compiler package relies on the interpreter's parser, so it get the first phases
	of error checking for free.  It implements the second phase itself, and that
	implementation is incomplete.  For example, the compiler package does not raise
	an error if a name appears more than once in an argument list:  ``def f(x, x):
	more``
	
	A future version of the compiler should fix these problems.
	
	
	Python Abstract Syntax
	======================
	
	The :mod:`compiler.ast` module defines an abstract syntax for Python.  In the
	abstract syntax tree, each node represents a syntactic construct.  The root of
	the tree is :class:`Module` object.
	
	The abstract syntax offers a higher level interface to parsed Python source
	code.  The :mod:`parser` module and the compiler written in C for the Python
	interpreter use a concrete syntax tree.  The concrete syntax is tied closely to
	the grammar description used for the Python parser.  Instead of a single node
	for a construct, there are often several levels of nested nodes that are
	introduced by Python's precedence rules.
	
	The abstract syntax tree is created by the :mod:`compiler.transformer` module.
	The transformer relies on the built-in Python parser to generate a concrete
	syntax tree.  It generates an abstract syntax tree from the concrete tree.
	
	"""
	pass
	
