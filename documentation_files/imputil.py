#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
""":synopsis: Manage and augment the import process.
:deprecated:

"""
class ImportManager:


	"""
	Manage the import process.
	
	"""
	
	
	def __init__(self, ):
		pass
	
	def install(self, namespace):
		"""
		Install this ImportManager into the specified namespace.
		
		"""
		pass
		
	def uninstall(self, ):
		"""
		Restore the previous import mechanism.
		
		"""
		pass
		
	def add_suffix(self, suffix,importFunc):
		"""
		Undocumented.
		
		
		"""
		pass
		
	


class Importer:


	"""
	Base class for replacing standard import functions.
	
	"""
	
	
	def __init__(self, ):
		pass
	
	def import_top(self, name):
		"""
		Import a top-level module.
		
		"""
		pass
		
	def get_code(self, parent,modname,fqname):
		"""
		Find and retrieve the code for the given module.
		
		*parent* specifies a parent module to define a context for importing.
		It may be ``None``, indicating no particular context for the search.
		
		*modname* specifies a single module (not dotted) within the parent.
		
		*fqname* specifies the fully-qualified module name. This is a
		(potentially) dotted name from the "root" of the module namespace
		down to the modname.
		
		If there is no parent, then modname==fqname.
		
		This method should return ``None``, or a 3-tuple.
		
		* If the module was not found, then ``None`` should be returned.
		
		* The first item of the 2- or 3-tuple should be the integer 0 or 1,
		specifying whether the module that was found is a package or not.
		
		* The second item is the code object for the module (it will be
		executed within the new module's namespace). This item can also
		be a fully-loaded module object (e.g. loaded from a shared lib).
		
		* The third item is a dictionary of name/value pairs that will be
		inserted into new module before the code object is executed. This
		is provided in case the module's code expects certain values (such
		as where the module was found). When the second item is a module
		object, then these names/values will be inserted *after* the module
		has been loaded/initialized.
		
		
		"""
		pass
		
	


class BuiltinImporter:


	"""
	Emulate the import mechanism for built-in and frozen modules.  This is a
	sub-class of the :class:`Importer` class.
	
	"""
	
	
	def __init__(self, ):
		pass
	
	def get_code(self, parent,modname,fqname):
		"""
		Undocumented.
		
		"""
		pass
		
	def py_suffix_importer(self, filename,finfo,fqname):
		"""
		Undocumented.
		
		"""
		pass
		
	


class DynLoadSuffixImporter:


	"""
	Undocumented.
	
	"""
	
	
	def __init__(self, ):
		pass
	
	def import_file(self, filename,finfo,fqname):
		"""
		Undocumented.
		
		.. xamples
		"""
		pass
		
	


