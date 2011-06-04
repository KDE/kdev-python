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
	
	
	def __init__(self, hooks,verbose):
		pass
	
	


