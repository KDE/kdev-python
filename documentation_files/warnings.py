#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
""":synopsis: Issue warning messages and control their disposition.


"""
def warn(message,category,stacklevel):
	"""
	Issue a warning, or maybe ignore it or raise an exception.  The *category*
	argument, if given, must be a warning category class (see above); it defaults to
	:exc:`UserWarning`.  Alternatively *message* can be a :exc:`Warning` instance,
	in which case *category* will be ignored and ``message.__class__`` will be used.
	In this case the message text will be ``str(message)``. This function raises an
	exception if the particular warning issued is changed into an error by the
	warnings filter see above.  The *stacklevel* argument can be used by wrapper
	functions written in Python, like this::
	
	def deprecation(message):
	warnings.warn(message, DeprecationWarning, stacklevel=2)
	
	This makes the warning refer to :func:`deprecation`'s caller, rather than to the
	source of :func:`deprecation` itself (since the latter would defeat the purpose
	of the warning message).
	
	
	"""
	pass
	
def warn_explicit(message,category,filename,lineno,module,registry,module_globals):
	"""
	This is a low-level interface to the functionality of :func:`warn`, passing in
	explicitly the message, category, filename and line number, and optionally the
	module name and the registry (which should be the ``__warningregistry__``
	dictionary of the module).  The module name defaults to the filename with
	``.py`` stripped; if no registry is passed, the warning is never suppressed.
	*message* must be a string and *category* a subclass of :exc:`Warning` or
	*message* may be a :exc:`Warning` instance, in which case *category* will be
	ignored.
	
	*module_globals*, if supplied, should be the global namespace in use by the code
	for which the warning is issued.  (This argument is used to support displaying
	source for modules found in zipfiles or other non-filesystem import
	sources).
	
	"""
	pass
	
def warnpy3k(message,category,stacklevel):
	"""
	Issue a warning related to Python 3.x deprecation. Warnings are only shown
	when Python is started with the -3 option. Like :func:`warn` *message* must
	be a string and *category* a subclass of :exc:`Warning`. :func:`warnpy3k`
	is using :exc:`DeprecationWarning` as default warning class.
	
	"""
	pass
	
def showwarning(message,category,filename,lineno,file,line):
	"""
	Write a warning to a file.  The default implementation calls
	``formatwarning(message, category, filename, lineno, line)`` and writes the
	resulting string to *file*, which defaults to ``sys.stderr``.  You may replace
	this function with an alternative implementation by assigning to
	``warnings.showwarning``.
	*line* is a line of source code to be included in the warning
	message; if *line* is not supplied, :func:`showwarning` will
	try to read the line specified by *filename* and *lineno*.
	
	"""
	pass
	
def formatwarning(message,category,filename,lineno,line):
	"""
	Format a warning the standard way.  This returns a string which may contain
	embedded newlines and ends in a newline.  *line* is a line of source code to
	be included in the warning message; if *line* is not supplied,
	:func:`formatwarning` will try to read the line specified by *filename* and
	*lineno*.
	
	"""
	pass
	
def filterwarnings(action,message,category,module,lineno,append):
	"""
	Insert an entry into the list of :ref:`warnings filter specifications
	<warning-filter>`.  The entry is inserted at the front by default; if
	*append* is true, it is inserted at the end.  This checks the types of the
	arguments, compiles the *message* and *module* regular expressions, and
	inserts them as a tuple in the list of warnings filters.  Entries closer to
	the front of the list override entries later in the list, if both match a
	particular warning.  Omitted arguments default to a value that matches
	everything.
	
	
	"""
	pass
	
def simplefilter(action,category,lineno,append):
	"""
	Insert a simple entry into the list of :ref:`warnings filter specifications
	<warning-filter>`.  The meaning of the function parameters is as for
	:func:`filterwarnings`, but regular expressions are not needed as the filter
	inserted always matches any message in any module as long as the category and
	line number match.
	
	
	"""
	pass
	
def resetwarnings():
	"""
	Reset the warnings filter.  This discards the effect of all previous calls to
	:func:`filterwarnings`, including that of the :option:`-W` command line options
	and calls to :func:`simplefilter`.
	
	
	Available Context Managers
	--------------------------
	
	"""
	pass
	
class catch_warnings:


	"""
	A context manager that copies and, upon exit, restores the warnings filter
	and the :func:`showwarning` function.
	If the *record* argument is :const:`False` (the default) the context manager
	returns :class:`None` on entry. If *record* is :const:`True`, a list is
	returned that is progressively populated with objects as seen by a custom
	:func:`showwarning` function (which also suppresses output to ``sys.stdout``).
	Each object in the list has attributes with the same names as the arguments to
	:func:`showwarning`.
	
	The *module* argument takes a module that will be used instead of the
	module returned when you import :mod:`warnings` whose filter will be
	protected. This argument exists primarily for testing the :mod:`warnings`
	module itself.
	
	"""
	
	
	def __init__(self, ESC,record=False,module=None):
		pass
	
	


