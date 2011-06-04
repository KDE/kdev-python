#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
""":synopsis: Interface to the creation of runtime implementation objects.
:deprecated:

"""
def instance(_class,dict):
	"""
	This function creates an instance of *class* with dictionary *dict* without
	calling the :meth:`__init__` constructor.  If *dict* is omitted or ``None``, a
	new, empty dictionary is created for the new instance.  Note that there are no
	guarantees that the object will be in a consistent state.
	
	
	"""
	pass
	
def instancemethod(function,instance,_class):
	"""
	This function will return a method object, bound to *instance*, or unbound if
	*instance* is ``None``.  *function* must be callable.
	
	
	"""
	pass
	
def function(code,globals,name,argdefs,closure):
	"""
	Returns a (Python) function with the given code and globals. If *name* is given,
	it must be a string or ``None``.  If it is a string, the function will have the
	given name, otherwise the function name will be taken from ``code.co_name``.  If
	*argdefs* is given, it must be a tuple and will be used to determine the default
	values of parameters.  If *closure* is given, it must be ``None`` or a tuple of
	cell objects containing objects to bind to the names in ``code.co_freevars``.
	
	
	"""
	pass
	
def code(argcount,nlocals,stacksize,flags,codestring,constants,names,varnames,filename,name,firstlineno,lnotab):
	"""
	This function is an interface to the :cfunc:`PyCode_New` C function.
	
	.. s still undocumented!
	
	
	"""
	pass
	
def module(name,doc):
	"""
	This function returns a new module object with name *name*. *name* must be a
	string. The optional *doc* argument can have any type.
	
	
	"""
	pass
	
