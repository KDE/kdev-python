#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
""":synopsis: Compare files efficiently.
"""
def cmp(f1,f2,shallow):
	"""
	Compare the files named *f1* and *f2*, returning ``True`` if they seem equal,
	``False`` otherwise.
	
	Unless *shallow* is given and is false, files with identical :func:`os.stat`
	signatures are taken to be equal.
	
	Files that were compared using this function will not be compared again unless
	their :func:`os.stat` signature changes.
	
	Note that no external programs are called from this function, giving it
	portability and efficiency.
	
	
	"""
	pass
	
def cmpfiles(dir1,dir2,common,shallow):
	"""
	Compare the files in the two directories *dir1* and *dir2* whose names are
	given by *common*.
	
	Returns three lists of file names: *match*, *mismatch*,
	*errors*.  *match* contains the list of files that match, *mismatch* contains
	the names of those that don't, and *errors* lists the names of files which
	could not be compared.  Files are listed in *errors* if they don't exist in
	one of the directories, the user lacks permission to read them or if the
	comparison could not be done for some other reason.
	
	The *shallow* parameter has the same meaning and default value as for
	:func:`filecmp.cmp`.
	
	For example, ``cmpfiles('a', 'b', ['c', 'd/e'])`` will compare ``a/c`` with
	``b/c`` and ``a/d/e`` with ``b/d/e``.  ``'c'`` and ``'d/e'`` will each be in
	one of the three returned lists.
	
	
	Example::
	
	>>> import filecmp
	>>> filecmp.cmp('undoc.rst', 'undoc.rst')
	True
	>>> filecmp.cmp('undoc.rst', 'index.rst')
	False
	
	
	.. he :class:`dircmp` class
	-------------------------
	
	:class:`dircmp` instances are built using this constructor:
	
	
	"""
	pass
	
class dircmp:


	"""
	Construct a new directory comparison object, to compare the directories *a* and
	*b*. *ignore* is a list of names to ignore, and defaults to ``['RCS', 'CVS',
	'tags']``. *hide* is a list of names to hide, and defaults to ``[os.curdir,
	os.pardir]``.
	
	The :class:`dircmp` class provides the following methods:
	
	
	"""
	
	
	def __init__(self, ):
		pass
	
	def report(self, ):
		"""
		Print (to ``sys.stdout``) a comparison between *a* and *b*.
		
		
		"""
		pass
		
	def report_partial_closure(self, ):
		"""
		Print a comparison between *a* and *b* and common immediate
		subdirectories.
		
		
		"""
		pass
		
	def report_full_closure(self, ):
		"""
		Print a comparison between *a* and *b* and common subdirectories
		(recursively).
		
		The :class:`dircmp` offers a number of interesting attributes that may be
		used to get various bits of information about the directory trees being
		compared.
		
		Note that via :meth:`__getattr__` hooks, all attributes are computed lazily,
		so there is no speed penalty if only those attributes which are lightweight
		to compute are used.
		
		
		"""
		pass
		
	


