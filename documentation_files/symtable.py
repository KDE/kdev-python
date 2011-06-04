#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
""":synopsis: Interface to the compiler's internal symbol tables.

"""
def symtable(code,filename,compile_type):
	"""
	Return the toplevel :class:`SymbolTable` for the Python source *code*.
	*filename* is the name of the file containing the code.  *compile_type* is
	like the *mode* argument to :func:`compile`.
	
	
	Examining Symbol Tables
	-----------------------
	
	"""
	pass
	
class SymbolTable:


	"""
	A namespace table for a block.  The constructor is not public.
	
	"""
	
	
	def __init__(self, ):
		pass
	
	


class Function:


	"""
	A namespace for a function or method.  This class inherits
	:class:`SymbolTable`.
	
	"""
	
	
	def __init__(self, ):
		pass
	
	


class Class:


	"""
	A namespace of a class.  This class inherits :class:`SymbolTable`.
	
	"""
	
	
	def __init__(self, ):
		pass
	
	


class Symbol:


	"""
	An entry in a :class:`SymbolTable` corresponding to an identifier in the
	source.  The constructor is not public.
	
	"""
	
	
	def __init__(self, ):
		pass
	
	


