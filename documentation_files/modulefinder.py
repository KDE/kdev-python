#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
""":synopsis: Find modules used by a script.


"""
def AddPackagePath(pkg_name,path):
	"""
	Record that the package named *pkg_name* can be found in the specified *path*.
	
	
	"""
	pass
	
def ReplacePackage(oldname,newname):
	"""
	Allows specifying that the module named *oldname* is in fact the package named
	*newname*.  The most common usage would be  to handle how the :mod:`_xmlplus`
	package replaces the :mod:`xml` package.
	
	
	"""
	pass
	
class ModuleFinder:


	"""
	This class provides :meth:`run_script` and :meth:`report` methods to determine
	the set of modules imported by a script. *path* can be a list of directories to
	search for modules; if not specified, ``sys.path`` is used.  *debug* sets the
	debugging level; higher values make the class print  debugging messages about
	what it's doing. *excludes* is a list of module names to exclude from the
	analysis. *replace_paths* is a list of ``(oldpath, newpath)`` tuples that will
	be replaced in module paths.
	
	
	"""
	
	
	def __init__(self, path=None,debug=0,excludes=[],replace_paths=[]):
		pass
	
	


