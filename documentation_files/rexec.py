#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
""":synopsis: Basic restricted execution framework.
:deprecated:

"""
class RExec:


	"""
	Returns an instance of the :class:`RExec` class.
	
	*hooks* is an instance of the :class:`RHooks` class or a subclass of it. If it
	is omitted or ``None``, the default :class:`RHooks` class is instantiated.
	Whenever the :mod:`rexec` module searches for a module (even a built-in one) or
	reads a module's code, it doesn't actually go out to the file system itself.
	Rather, it calls methods of an :class:`RHooks` instance that was passed to or
	created by its constructor.  (Actually, the :class:`RExec` object doesn't make
	these calls --- they are made by a module loader object that's part of the
	:class:`RExec` object.  This allows another level of flexibility, which can be
	useful when changing the mechanics of :keyword:`import` within the restricted
	environment.)
	
	By providing an alternate :class:`RHooks` object, we can control the file system
	accesses made to import a module, without changing the actual algorithm that
	controls the order in which those accesses are made.  For instance, we could
	substitute an :class:`RHooks` object that passes all filesystem requests to a
	file server elsewhere, via some RPC mechanism such as ILU.  Grail's applet
	loader uses this to support importing applets from a URL for a directory.
	
	If *verbose* is true, additional debugging output may be sent to standard
	output.
	
	It is important to be aware that code running in a restricted environment can
	still call the :func:`sys.exit` function.  To disallow restricted code from
	exiting the interpreter, always protect calls that cause restricted code to run
	with a :keyword:`try`/:keyword:`except` statement that catches the
	:exc:`SystemExit` exception.  Removing the :func:`sys.exit` function from the
	restricted environment is not sufficient --- the restricted code could still use
	``raise SystemExit``.  Removing :exc:`SystemExit` is not a reasonable option;
	some library code makes use of this and would break were it not available.
	
	
	"""
	
	
	def __init__(self, ):
		pass
	
	def r_eval(self, code):
		"""
		*code* must either be a string containing a Python expression, or a compiled
		code object, which will be evaluated in the restricted environment's
		:mod:`__main__` module.  The value of the expression or code object will be
		returned.
		
		
		"""
		pass
		
	def r_exec(self, code):
		"""
		*code* must either be a string containing one or more lines of Python code, or a
		compiled code object, which will be executed in the restricted environment's
		:mod:`__main__` module.
		
		
		"""
		pass
		
	def r_execfile(self, filename):
		"""
		Execute the Python code contained in the file *filename* in the restricted
		environment's :mod:`__main__` module.
		
		Methods whose names begin with ``s_`` are similar to the functions beginning
		with ``r_``, but the code will be granted access to restricted versions of the
		standard I/O streams ``sys.stdin``, ``sys.stderr``, and ``sys.stdout``.
		
		
		"""
		pass
		
	def s_eval(self, code):
		"""
		*code* must be a string containing a Python expression, which will be evaluated
		in the restricted environment.
		
		
		"""
		pass
		
	def s_exec(self, code):
		"""
		*code* must be a string containing one or more lines of Python code, which will
		be executed in the restricted environment.
		
		
		"""
		pass
		
	def s_execfile(self, code):
		"""
		Execute the Python code contained in the file *filename* in the restricted
		environment.
		
		:class:`RExec` objects must also support various methods which will be
		implicitly called by code executing in the restricted environment. Overriding
		these methods in a subclass is used to change the policies enforced by a
		restricted environment.
		
		
		"""
		pass
		
	def r_import(self, modulename,globals,locals,_fromlist):
		"""
		Import the module *modulename*, raising an :exc:`ImportError` exception if the
		module is considered unsafe.
		
		
		"""
		pass
		
	def r_open(self, filename,mode,bufsize):
		"""
		Method called when :func:`open` is called in the restricted environment.  The
		arguments are identical to those of :func:`open`, and a file object (or a class
		instance compatible with file objects) should be returned.  :class:`RExec`'s
		default behaviour is allow opening any file for reading, but forbidding any
		attempt to write a file.  See the example below for an implementation of a less
		restrictive :meth:`r_open`.
		
		
		"""
		pass
		
	def r_reload(self, module):
		"""
		Reload the module object *module*, re-parsing and re-initializing it.
		
		
		"""
		pass
		
	def r_unload(self, module):
		"""
		Unload the module object *module* (remove it from the restricted environment's
		``sys.modules`` dictionary).
		
		And their equivalents with access to restricted standard I/O streams:
		
		
		"""
		pass
		
	def s_import(self, modulename,globals,locals,_fromlist):
		"""
		Import the module *modulename*, raising an :exc:`ImportError` exception if the
		module is considered unsafe.
		
		
		"""
		pass
		
	def s_reload(self, module):
		"""
		Reload the module object *module*, re-parsing and re-initializing it.
		
		
		"""
		pass
		
	def s_unload(self, module):
		"""
		Unload the module object *module*.
		
		.. re the semantics of this?
		
		
		.. efining restricted environments
		--------------------------------
		
		The :class:`RExec` class has the following class attributes, which are used by
		the :meth:`__init__` method.  Changing them on an existing instance won't have
		any effect; instead, create a subclass of :class:`RExec` and assign them new
		values in the class definition. Instances of the new class will then use those
		new values.  All these attributes are tuples of strings.
		
		
		"""
		pass
		
	


