#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
""":synopsis: Utilities for the import system.

This module provides utilities for the import system, in particular package
support.

"""
def extend_path(path,name):
	"""
	Extend the search path for the modules which comprise a package.  Intended
	use is to place the following code in a package's :file:`__init__.py`::
	
	from pkgutil import extend_path
	__path__ = extend_path(__path__, __name__)
	
	This will add to the package's ``__path__`` all subdirectories of directories
	on ``sys.path`` named after the package.  This is useful if one wants to
	distribute different parts of a single logical package as multiple
	directories.
	
	It also looks for :file:`\*.pkg` files beginning where ``*`` matches the
	*name* argument.  This feature is similar to :file:`\*.pth` files (see the
	:mod:`site` module for more information), except that it doesn't special-case
	lines starting with ``import``.  A :file:`\*.pkg` file is trusted at face
	value: apart from checking for duplicates, all entries found in a
	:file:`\*.pkg` file are added to the path, regardless of whether they exist
	on the filesystem.  (This is a feature.)
	
	If the input path is not a list (as is the case for frozen packages) it is
	returned unchanged.  The input path is not modified; an extended copy is
	returned.  Items are only appended to the copy at the end.
	
	It is assumed that :data:`sys.path` is a sequence.  Items of :data:`sys.path`
	that are not (Unicode or 8-bit) strings referring to existing directories are
	ignored.  Unicode items on :data:`sys.path` that cause errors when used as
	filenames may cause this function to raise an exception (in line with
	:func:`os.path.isdir` behavior).
	
	
	"""
	pass
	
class ImpImporter:


	"""
	:pep:`302` Importer that wraps Python's "classic" import algorithm.
	
	If *dirname* is a string, a :pep:`302` importer is created that searches that
	directory.  If *dirname* is ``None``, a :pep:`302` importer is created that
	searches the current :data:`sys.path`, plus any modules that are frozen or
	built-in.
	
	Note that :class:`ImpImporter` does not currently support being used by
	placement on :data:`sys.meta_path`.
	
	
	"""
	
	
	def __init__(self, ):
		pass
	
	


class ImpLoader:


	"""
	:pep:`302` Loader that wraps Python's "classic" import algorithm.
	
	
	"""
	
	
	def __init__(self, ):
		pass
	
	def find_loader(self, fullname):
		"""
		Find a :pep:`302` "loader" object for *fullname*.
		
		If *fullname* contains dots, path must be the containing package's
		``__path__``.  Returns ``None`` if the module cannot be found or imported.
		This function uses :func:`iter_importers`, and is thus subject to the same
		limitations regarding platform-specific special import locations such as the
		Windows registry.
		
		
		"""
		pass
		
	def get_importer(self, path_item):
		"""
		Retrieve a :pep:`302` importer for the given *path_item*.
		
		The returned importer is cached in :data:`sys.path_importer_cache` if it was
		newly created by a path hook.
		
		If there is no importer, a wrapper around the basic import machinery is
		returned.  This wrapper is never inserted into the importer cache (``None``
		is inserted instead).
		
		The cache (or part of it) can be cleared manually if a rescan of
		:data:`sys.path_hooks` is necessary.
		
		
		"""
		pass
		
	def get_loader(self, module_or_name):
		"""
		Get a :pep:`302` "loader" object for *module_or_name*.
		
		If the module or package is accessible via the normal import mechanism, a
		wrapper around the relevant part of that machinery is returned.  Returns
		``None`` if the module cannot be found or imported.  If the named module is
		not already imported, its containing package (if any) is imported, in order
		to establish the package ``__path__``.
		
		This function uses :func:`iter_importers`, and is thus subject to the same
		limitations regarding platform-specific special import locations such as the
		Windows registry.
		
		
		"""
		pass
		
	def iter_importers(self, fullname=''):
		"""
		Yield :pep:`302` importers for the given module name.
		
		If fullname contains a '.', the importers will be for the package containing
		fullname, otherwise they will be importers for :data:`sys.meta_path`,
		:data:`sys.path`, and Python's "classic" import machinery, in that order.  If
		the named module is in a package, that package is imported as a side effect
		of invoking this function.
		
		Non-:pep:`302` mechanisms (e.g. the Windows registry) used by the standard
		import machinery to find files in alternative locations are partially
		supported, but are searched *after* :data:`sys.path`.  Normally, these
		locations are searched *before* :data:`sys.path`, preventing :data:`sys.path`
		entries from shadowing them.
		
		For this to cause a visible difference in behaviour, there must be a module
		or package name that is accessible via both :data:`sys.path` and one of the
		non-:pep:`302` file system mechanisms.  In this case, the emulation will find
		the former version, while the builtin import mechanism will find the latter.
		
		Items of the following types can be affected by this discrepancy:
		``imp.C_EXTENSION``, ``imp.PY_SOURCE``, ``imp.PY_COMPILED``,
		``imp.PKG_DIRECTORY``.
		
		
		"""
		pass
		
	def iter_modules(self, path=None,prefix=''):
		"""
		Yields ``(module_loader, name, ispkg)`` for all submodules on *path*, or, if
		path is ``None``, all top-level modules on ``sys.path``.
		
		*path* should be either ``None`` or a list of paths to look for modules in.
		
		*prefix* is a string to output on the front of every module name on output.
		
		
		"""
		pass
		
	def walk_packages(self, path=None,prefix='',onerror=None):
		"""
		Yields ``(module_loader, name, ispkg)`` for all modules recursively on
		*path*, or, if path is ``None``, all accessible modules.
		
		*path* should be either ``None`` or a list of paths to look for modules in.
		
		*prefix* is a string to output on the front of every module name on output.
		
		Note that this function must import all *packages* (*not* all modules!) on
		the given *path*, in order to access the ``__path__`` attribute to find
		submodules.
		
		*onerror* is a function which gets called with one argument (the name of the
		package which was being imported) if any exception occurs while trying to
		import a package.  If no *onerror* function is supplied, :exc:`ImportError`\s
		are caught and ignored, while all other exceptions are propagated,
		terminating the search.
		
		Examples::
		
		# list all modules python can access
		walk_packages()
		
		# list all submodules of ctypes
		walk_packages(ctypes.__path__, ctypes.__name__ + '.')
		
		
		"""
		pass
		
	


