#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
""":synopsis: Supports information extraction for a Python class browser.
"""
def readmodule(module,path=None):
	"""
	Read a module and return a dictionary mapping class names to class
	descriptor objects.  The parameter *module* should be the name of a
	module as a string; it may be the name of a module within a package.  The
	*path* parameter should be a sequence, and is used to augment the value
	of ``sys.path``, which is used to locate module source code.
	
	
	"""
	pass
	
def readmodule_ex(module,path=None):
	"""
	Like :func:`readmodule`, but the returned dictionary, in addition to
	mapping class names to class descriptor objects, also maps top-level
	function names to function descriptor objects.  Moreover, if the module
	being read is a package, the key ``'__path__'`` in the returned
	dictionary has as its value a list which contains the package search
	path.
	
	
	.. lass Objects
	-------------
	
	The :class:`Class` objects used as values in the dictionary returned by
	:func:`readmodule` and :func:`readmodule_ex` provide the following data
	members:
	
	
	"""
	pass
	
