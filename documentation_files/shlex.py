#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
""":synopsis: Simple lexical analysis for Unix shell-like languages.
"""
def split(s,comments,posix):
	"""
	Split the string *s* using shell-like syntax. If *comments* is :const:`False`
	(the default), the parsing of comments in the given string will be disabled
	(setting the :attr:`commenters` member of the :class:`shlex` instance to the
	empty string).  This function operates in POSIX mode by default, but uses
	non-POSIX mode if the *posix* argument is false.
	
	"""
	pass
	
class shlex:


	"""
	A :class:`shlex` instance or subclass instance is a lexical analyzer object.
	The initialization argument, if present, specifies where to read characters
	from. It must be a file-/stream-like object with :meth:`read` and
	:meth:`readline` methods, or a string (strings are accepted since Python 2.3).
	If no argument is given, input will be taken from ``sys.stdin``.  The second
	optional argument is a filename string, which sets the initial value of the
	:attr:`infile` member.  If the *instream* argument is omitted or equal to
	``sys.stdin``, this second argument defaults to "stdin".  The *posix* argument
	was introduced in Python 2.3, and defines the operational mode.  When *posix* is
	not true (default), the :class:`shlex` instance will operate in compatibility
	mode.  When operating in POSIX mode, :class:`shlex` will try to be as close as
	possible to the POSIX shell parsing rules.
	
	
	"""
	
	
	def __init__(self, ):
		pass
	
	def get_token(self, ):
		"""
		Return a token.  If tokens have been stacked using :meth:`push_token`, pop a
		token off the stack.  Otherwise, read one from the input stream.  If reading
		encounters an immediate end-of-file, :attr:`self.eof` is returned (the empty
		string (``''``) in non-POSIX mode, and ``None`` in POSIX mode).
		
		
		"""
		pass
		
	def push_token(self, str):
		"""
		Push the argument onto the token stack.
		
		
		"""
		pass
		
	def read_token(self, ):
		"""
		Read a raw token.  Ignore the pushback stack, and do not interpret source
		requests.  (This is not ordinarily a useful entry point, and is documented here
		only for the sake of completeness.)
		
		
		"""
		pass
		
	def sourcehook(self, filename):
		"""
		When :class:`shlex` detects a source request (see :attr:`source` below) this
		method is given the following token as argument, and expected to return a tuple
		consisting of a filename and an open file-like object.
		
		Normally, this method first strips any quotes off the argument.  If the result
		is an absolute pathname, or there was no previous source request in effect, or
		the previous source was a stream (such as ``sys.stdin``), the result is left
		alone.  Otherwise, if the result is a relative pathname, the directory part of
		the name of the file immediately before it on the source inclusion stack is
		prepended (this behavior is like the way the C preprocessor handles ``#include
		"file.h"``).
		
		The result of the manipulations is treated as a filename, and returned as the
		first component of the tuple, with :func:`open` called on it to yield the second
		component. (Note: this is the reverse of the order of arguments in instance
		initialization!)
		
		This hook is exposed so that you can use it to implement directory search paths,
		addition of file extensions, and other namespace hacks. There is no
		corresponding 'close' hook, but a shlex instance will call the :meth:`close`
		method of the sourced input stream when it returns EOF.
		
		For more explicit control of source stacking, use the :meth:`push_source` and
		:meth:`pop_source` methods.
		
		
		"""
		pass
		
	def push_source(self, stream,filename):
		"""
		Push an input source stream onto the input stack.  If the filename argument is
		specified it will later be available for use in error messages.  This is the
		same method used internally by the :meth:`sourcehook` method.
		
		"""
		pass
		
	def pop_source(self, ):
		"""
		Pop the last-pushed input source from the input stack. This is the same method
		used internally when the lexer reaches EOF on a stacked input stream.
		
		"""
		pass
		
	def error_leader(self, file,line):
		"""
		This method generates an error message leader in the format of a Unix C compiler
		error label; the format is ``'"%s", line %d: '``, where the ``%s`` is replaced
		with the name of the current source file and the ``%d`` with the current input
		line number (the optional arguments can be used to override these).
		
		This convenience is provided to encourage :mod:`shlex` users to generate error
		messages in the standard, parseable format understood by Emacs and other Unix
		tools.
		
		Instances of :class:`shlex` subclasses have some public instance variables which
		either control lexical analysis or can be used for debugging:
		
		
		"""
		pass
		
	


