#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
""":synopsis: Facilities to implement read-eval-print loops.



The ``code`` module provides facilities to implement read-eval-print loops in
Python.  Two classes and convenience functions are included which can be used to
build applications which provide an interactive interpreter prompt.


"""
class InteractiveInterpreter:


	"""
	This class deals with parsing and interpreter state (the user's namespace); it
	does not deal with input buffering or prompting or input file naming (the
	filename is always passed in explicitly). The optional *locals* argument
	specifies the dictionary in which code will be executed; it defaults to a newly
	created dictionary with key ``'__name__'`` set to ``'__console__'`` and key
	``'__doc__'`` set to ``None``.
	
	
	"""
	
	
	def __init__(self, locals):
		pass
	
	


class InteractiveConsole:


	"""
	Closely emulate the behavior of the interactive Python interpreter. This class
	builds on :class:`InteractiveInterpreter` and adds prompting using the familiar
	``sys.ps1`` and ``sys.ps2``, and input buffering.
	
	
	"""
	
	
	def __init__(self, locals,filename):
		pass
	
	def interact(banner,readfunc,local):
		"""
		Convenience function to run a read-eval-print loop.  This creates a new instance
		of :class:`InteractiveConsole` and sets *readfunc* to be used as the
		:meth:`raw_input` method, if provided.  If *local* is provided, it is passed to
		the :class:`InteractiveConsole` constructor for use as the default namespace for
		the interpreter loop.  The :meth:`interact` method of the instance is then run
		with *banner* passed as the banner to use, if provided.  The console object is
		discarded after use.
		
		
		"""
		pass
		
	def compile_command(source,filename,symbol):
		"""
		This function is useful for programs that want to emulate Python's interpreter
		main loop (a.k.a. the read-eval-print loop).  The tricky part is to determine
		when the user has entered an incomplete command that can be completed by
		entering more text (as opposed to a complete command or a syntax error).  This
		function *almost* always makes the same decision as the real interpreter main
		loop.
		
		*source* is the source string; *filename* is the optional filename from which
		source was read, defaulting to ``'<input>'``; and *symbol* is the optional
		grammar start symbol, which should be either ``'single'`` (the default) or
		``'eval'``.
		
		Returns a code object (the same as ``compile(source, filename, symbol)``) if the
		command is complete and valid; ``None`` if the command is incomplete; raises
		:exc:`SyntaxError` if the command is complete and contains a syntax error, or
		raises :exc:`OverflowError` or :exc:`ValueError` if the command contains an
		invalid literal.
		
		
		.. nteractive Interpreter Objects
		-------------------------------
		
		
		"""
		pass
		
	


