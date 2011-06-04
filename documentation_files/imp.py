#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
""":synopsis: Access the implementation of the import statement.


"""
"""
The module was found as a source file.


"""
PY_SOURCE = None
"""
The module was found as a compiled code object file.


"""
PY_COMPILED = None
"""
The module was found as dynamically loadable shared library.


"""
C_EXTENSION = None
"""
The module was found as a package directory.


"""
PKG_DIRECTORY = None
"""
The module was found as a built-in module.


"""
C_BUILTIN = None
"""
The module was found as a frozen module (see :func:`init_frozen`).

The following constant and functions are obsolete; their functionality is
available through :func:`find_module` or :func:`load_module`. They are kept
around for backward compatibility:


"""
PY_FROZEN = None
"""
Unused.


"""
SEARCH_ERROR = None
def get_magic():
	"""
	"""
	pass
	
def get_suffixes():
	"""
	Return a list of 3-element tuples, each describing a particular type of
	module. Each triple has the form ``(suffix, mode, type)``, where *suffix* is
	a string to be appended to the module name to form the filename to search
	for, *mode* is the mode string to pass to the built-in :func:`open` function
	to open the file (this can be ``'r'`` for text files or ``'rb'`` for binary
	files), and *type* is the file type, which has one of the values
	:const:`PY_SOURCE`, :const:`PY_COMPILED`, or :const:`C_EXTENSION`, described
	below.
	
	
	"""
	pass
	
def find_module(name,path):
	"""
	Try to find the module *name*.  If *path* is omitted or ``None``, the list of
	directory names given by ``sys.path`` is searched, but first a few special
	places are searched: the function tries to find a built-in module with the
	given name (:const:`C_BUILTIN`), then a frozen module (:const:`PY_FROZEN`),
	and on some systems some other places are looked in as well (on Windows, it
	looks in the registry which may point to a specific file).
	
	Otherwise, *path* must be a list of directory names; each directory is
	searched for files with any of the suffixes returned by :func:`get_suffixes`
	above.  Invalid names in the list are silently ignored (but all list items
	must be strings).
	
	If search is successful, the return value is a 3-element tuple ``(file,
	pathname, description)``:
	
	*file* is an open file object positioned at the beginning, *pathname* is the
	pathname of the file found, and *description* is a 3-element tuple as
	contained in the list returned by :func:`get_suffixes` describing the kind of
	module found.
	
	If the module does not live in a file, the returned *file* is ``None``,
	*pathname* is the empty string, and the *description* tuple contains empty
	strings for its suffix and mode; the module type is indicated as given in
	parentheses above.  If the search is unsuccessful, :exc:`ImportError` is
	raised.  Other exceptions indicate problems with the arguments or
	environment.
	
	If the module is a package, *file* is ``None``, *pathname* is the package
	path and the last item in the *description* tuple is :const:`PKG_DIRECTORY`.
	
	This function does not handle hierarchical module names (names containing
	dots).  In order to find *P*.*M*, that is, submodule *M* of package *P*, use
	:func:`find_module` and :func:`load_module` to find and load package *P*, and
	then use :func:`find_module` with the *path* argument set to ``P.__path__``.
	When *P* itself has a dotted name, apply this recipe recursively.
	
	
	"""
	pass
	
def load_module(name,file,pathname,description):
	"""
	"""
	pass
	
def new_module(name):
	"""
	Return a new empty module object called *name*.  This object is *not* inserted
	in ``sys.modules``.
	
	
	"""
	pass
	
def lock_held():
	"""
	Return ``True`` if the import lock is currently held, else ``False``. On
	platforms without threads, always return ``False``.
	
	On platforms with threads, a thread executing an import holds an internal lock
	until the import is complete. This lock blocks other threads from doing an
	import until the original import completes, which in turn prevents other threads
	from seeing incomplete module objects constructed by the original thread while
	in the process of completing its import (and the imports, if any, triggered by
	that).
	
	
	"""
	pass
	
def acquire_lock():
	"""
	Acquire the interpreter's import lock for the current thread.  This lock should
	be used by import hooks to ensure thread-safety when importing modules.
	
	Once a thread has acquired the import lock, the same thread may acquire it
	again without blocking; the thread must release it once for each time it has
	acquired it.
	
	On platforms without threads, this function does nothing.
	
	"""
	pass
	
def release_lock():
	"""
	Release the interpreter's import lock. On platforms without threads, this
	function does nothing.
	
	"""
	pass
	
def init_builtin(name):
	"""
	Initialize the built-in module called *name* and return its module object along
	with storing it in ``sys.modules``.  If the module was already initialized, it
	will be initialized *again*.  Re-initialization involves the copying of the
	built-in module's ``__dict__`` from the cached module over the module's entry in
	``sys.modules``.  If there is no built-in module called *name*, ``None`` is
	returned.
	
	
	"""
	pass
	
def init_frozen(name):
	"""
	Initialize the frozen module called *name* and return its module object.  If
	the module was already initialized, it will be initialized *again*.  If there
	is no frozen module called *name*, ``None`` is returned.  (Frozen modules are
	modules written in Python whose compiled byte-code object is incorporated
	into a custom-built Python interpreter by Python's :program:`freeze`
	utility. See :file:`Tools/freeze/` for now.)
	
	
	"""
	pass
	
def is_builtin(name):
	"""
	Return ``1`` if there is a built-in module called *name* which can be
	initialized again.  Return ``-1`` if there is a built-in module called *name*
	which cannot be initialized again (see :func:`init_builtin`).  Return ``0`` if
	there is no built-in module called *name*.
	
	
	"""
	pass
	
def is_frozen(name):
	"""
	Return ``True`` if there is a frozen module (see :func:`init_frozen`) called
	*name*, or ``False`` if there is no such module.
	
	
	"""
	pass
	
def load_compiled(name,pathname,file):
	"""
	"""
	pass
	
def load_dynamic(name,pathname,file):
	"""
	Load and initialize a module implemented as a dynamically loadable shared
	library and return its module object.  If the module was already initialized, it
	will be initialized *again*. Re-initialization involves copying the ``__dict__``
	attribute of the cached instance of the module over the value used in the module
	cached in ``sys.modules``.  The *pathname* argument must point to the shared
	library.  The *name* argument is used to construct the name of the
	initialization function: an external C function called ``initname()`` in the
	shared library is called.  The optional *file* argument is ignored.  (Note:
	using shared libraries is highly system dependent, and not all systems support
	it.)
	
	
	"""
	pass
	
def load_source(name,pathname,file):
	"""
	Load and initialize a module implemented as a Python source file and return its
	module object.  If the module was already initialized, it will be initialized
	*again*.  The *name* argument is used to create or access a module object.  The
	*pathname* argument points to the source file.  The *file* argument is the
	source file, open for reading as text, from the beginning. It must currently be
	a real file object, not a user-defined class emulating a file.  Note that if a
	properly matching byte-compiled file (with suffix :file:`.pyc` or :file:`.pyo`)
	exists, it will be used instead of parsing the given source file.
	
	
	"""
	pass
	
class NullImporter:


	"""
	The :class:`NullImporter` type is a :pep:`302` import hook that handles
	non-directory path strings by failing to find any modules.  Calling this type
	with an existing directory or empty string raises :exc:`ImportError`.
	Otherwise, a :class:`NullImporter` instance is returned.
	
	Python adds instances of this type to ``sys.path_importer_cache`` for any path
	entries that are not directories and are not handled by any other path hooks on
	``sys.path_hooks``.  Instances have only one method:
	
	
	"""
	
	
	def __init__(self, ):
		pass
	
	def find_module(self, fullname,path):
		"""
		This method always returns ``None``, indicating that the requested module could
		not be found.
		
		"""
		pass
		
	


