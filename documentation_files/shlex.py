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
	
	
	def __init__(self, instream,infile,posix):
		pass
	
	


