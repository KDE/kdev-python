#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
""":synopsis: support for importing Python modules from ZIP archives.
"""
class zipimporter:


	"""
	Create a new zipimporter instance. *archivepath* must be a path to a ZIP
	file, or to a specific path within a ZIP file.  For example, an *archivepath*
	of :file:`foo/bar.zip/lib` will look for modules in the :file:`lib` directory
	inside the ZIP file :file:`foo/bar.zip` (provided that it exists).
	
	:exc:`ZipImportError` is raised if *archivepath* doesn't point to a valid ZIP
	archive.
	
	"""
	
	
	def __init__(self, ):
		pass
	
	def find_module(self, fullname,path):
		"""
		Search for a module specified by *fullname*. *fullname* must be the fully
		qualified (dotted) module name. It returns the zipimporter instance itself
		if the module was found, or :const:`None` if it wasn't. The optional
		*path* argument is ignored---it's there for compatibility with the
		importer protocol.
		
		
		"""
		pass
		
	def get_code(self, fullname):
		"""
		Return the code object for the specified module. Raise
		:exc:`ZipImportError` if the module couldn't be found.
		
		
		"""
		pass
		
	def get_data(self, pathname):
		"""
		Return the data associated with *pathname*. Raise :exc:`IOError` if the
		file wasn't found.
		
		
		"""
		pass
		
	def get_filename(self, fullname):
		"""
		Return the value ``__file__`` would be set to if the specified module
		was imported. Raise :exc:`ZipImportError` if the module couldn't be
		found.
		
		"""
		pass
		
	def get_source(self, fullname):
		"""
		Return the source code for the specified module. Raise
		:exc:`ZipImportError` if the module couldn't be found, return
		:const:`None` if the archive does contain the module, but has no source
		for it.
		
		
		"""
		pass
		
	def is_package(self, fullname):
		"""
		Return True if the module specified by *fullname* is a package. Raise
		:exc:`ZipImportError` if the module couldn't be found.
		
		
		"""
		pass
		
	def load_module(self, fullname):
		"""
		Load the module specified by *fullname*. *fullname* must be the fully
		qualified (dotted) module name. It returns the imported module, or raises
		:exc:`ZipImportError` if it wasn't found.
		
		
		"""
		pass
		
	


