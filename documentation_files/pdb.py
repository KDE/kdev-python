#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
""":synopsis: The Python debugger for interactive interpreters.


"""
def run(statement,globals,locals):
	"""
	Execute the *statement* (given as a string) under debugger control.  The
	debugger prompt appears before any code is executed; you can set breakpoints and
	type ``continue``, or you can step through the statement using ``step`` or
	``next`` (all these commands are explained below).  The optional *globals* and
	*locals* arguments specify the environment in which the code is executed; by
	default the dictionary of the module :mod:`__main__` is used.  (See the
	explanation of the :keyword:`exec` statement or the :func:`eval` built-in
	function.)
	
	
	"""
	pass
	
def runeval(expression,globals,locals):
	"""
	Evaluate the *expression* (given as a string) under debugger control.  When
	:func:`runeval` returns, it returns the value of the expression.  Otherwise this
	function is similar to :func:`run`.
	
	
	"""
	pass
	
def runcall(function,argument,more):
	"""
	Call the *function* (a function or method object, not a string) with the given
	arguments.  When :func:`runcall` returns, it returns whatever the function call
	returned.  The debugger prompt appears as soon as the function is entered.
	
	
	"""
	pass
	
def set_trace():
	"""
	Enter the debugger at the calling stack frame.  This is useful to hard-code a
	breakpoint at a given point in a program, even if the code is not otherwise
	being debugged (e.g. when an assertion fails).
	
	
	"""
	pass
	
def post_mortem(traceback):
	"""
	Enter post-mortem debugging of the given *traceback* object.  If no
	*traceback* is given, it uses the one of the exception that is currently
	being handled (an exception must be being handled if the default is to be
	used).
	
	
	"""
	pass
	
def pm():
	"""
	Enter post-mortem debugging of the traceback found in
	:data:`sys.last_traceback`.
	
	
	The ``run*`` functions and :func:`set_trace` are aliases for instantiating the
	:class:`Pdb` class and calling the method of the same name.  If you want to
	access further features, you have to do this yourself:
	
	"""
	pass
	
class Pdb:


	"""
	:class:`Pdb` is the debugger class.
	
	The *completekey*, *stdin* and *stdout* arguments are passed to the
	underlying :class:`cmd.Cmd` class; see the description there.
	
	The *skip* argument, if given, must be an iterable of glob-style module name
	patterns.  The debugger will not step into frames that originate in a module
	that matches one of these patterns. [1]_
	
	Example call to enable tracing with *skip*::
	
	import pdb; pdb.Pdb(skip=['django.*']).set_trace()
	
	"""
	
	
	def __init__(self, completekey='tab',stdin=None,stdout=None,skip=None):
		pass
	
	


