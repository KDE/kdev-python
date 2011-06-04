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
	
	def get_type(self, ):
		"""
		Return the type of the symbol table.  Possible values are ``'class'``,
		``'module'``, and ``'function'``.
		
		"""
		pass
		
	def get_id(self, ):
		"""
		Return the table's identifier.
		
		"""
		pass
		
	def get_name(self, ):
		"""
		Return the table's name.  This is the name of the class if the table is
		for a class, the name of the function if the table is for a function, or
		``'top'`` if the table is global (:meth:`get_type` returns ``'module'``).
		
		"""
		pass
		
	def get_lineno(self, ):
		"""
		Return the number of the first line in the block this table represents.
		
		"""
		pass
		
	def is_optimized(self, ):
		"""
		Return ``True`` if the locals in this table can be optimized.
		
		"""
		pass
		
	def is_nested(self, ):
		"""
		Return ``True`` if the block is a nested class or function.
		
		"""
		pass
		
	def has_children(self, ):
		"""
		Return ``True`` if the block has nested namespaces within it.  These can
		be obtained with :meth:`get_children`.
		
		"""
		pass
		
	def has_exec(self, ):
		"""
		Return ``True`` if the block uses ``exec``.
		
		"""
		pass
		
	def has_import_star(self, ):
		"""
		Return ``True`` if the block uses a starred from-import.
		
		"""
		pass
		
	def get_identifiers(self, ):
		"""
		Return a list of names of symbols in this table.
		
		"""
		pass
		
	def lookup(self, name):
		"""
		Lookup *name* in the table and return a :class:`Symbol` instance.
		
		"""
		pass
		
	def get_symbols(self, ):
		"""
		Return a list of :class:`Symbol` instances for names in the table.
		
		"""
		pass
		
	def get_children(self, ):
		"""
		Return a list of the nested symbol tables.
		
		
		"""
		pass
		
	


class Function:


	"""
	A namespace for a function or method.  This class inherits
	:class:`SymbolTable`.
	
	"""
	
	
	def __init__(self, ):
		pass
	
	def get_parameters(self, ):
		"""
		Return a tuple containing names of parameters to this function.
		
		"""
		pass
		
	def get_locals(self, ):
		"""
		Return a tuple containing names of locals in this function.
		
		"""
		pass
		
	def get_globals(self, ):
		"""
		Return a tuple containing names of globals in this function.
		
		"""
		pass
		
	def get_frees(self, ):
		"""
		Return a tuple containing names of free variables in this function.
		
		
		"""
		pass
		
	


class Class:


	"""
	A namespace of a class.  This class inherits :class:`SymbolTable`.
	
	"""
	
	
	def __init__(self, ):
		pass
	
	def get_methods(self, ):
		"""
		Return a tuple containing the names of methods declared in the class.
		
		
		"""
		pass
		
	


class Symbol:


	"""
	An entry in a :class:`SymbolTable` corresponding to an identifier in the
	source.  The constructor is not public.
	
	"""
	
	
	def __init__(self, ):
		pass
	
	def get_name(self, ):
		"""
		Return the symbol's name.
		
		"""
		pass
		
	def is_referenced(self, ):
		"""
		Return ``True`` if the symbol is used in its block.
		
		"""
		pass
		
	def is_imported(self, ):
		"""
		Return ``True`` if the symbol is created from an import statement.
		
		"""
		pass
		
	def is_parameter(self, ):
		"""
		Return ``True`` if the symbol is a parameter.
		
		"""
		pass
		
	def is_global(self, ):
		"""
		Return ``True`` if the symbol is global.
		
		"""
		pass
		
	def is_declared_global(self, ):
		"""
		Return ``True`` if the symbol is declared global with a global statement.
		
		"""
		pass
		
	def is_local(self, ):
		"""
		Return ``True`` if the symbol is local to its block.
		
		"""
		pass
		
	def is_free(self, ):
		"""
		Return ``True`` if the symbol is referenced in its block, but not assigned
		to.
		
		"""
		pass
		
	def is_assigned(self, ):
		"""
		Return ``True`` if the symbol is assigned to in its block.
		
		"""
		pass
		
	def is_namespace(self, ):
		"""
		Return ``True`` if name binding introduces new namespace.
		
		If the name is used as the target of a function or class statement, this
		will be true.
		
		For example::
		
		>>> table = symtable.symtable("def some_func(): pass", "string", "exec")
		>>> table.lookup("some_func").is_namespace()
		True
		
		Note that a single name can be bound to multiple objects.  If the result
		is ``True``, the name may also be bound to other objects, like an int or
		list, that does not introduce a new namespace.
		
		"""
		pass
		
	def get_namespaces(self, ):
		"""
		Return a list of namespaces bound to this name.
		
		"""
		pass
		
	


