#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
""":synopsis: Lexical scanner for Python source code.
"""
"""
Token value used to indicate a comment.


"""
COMMENT = None
"""
Token value used to indicate a non-terminating newline.  The NEWLINE token
indicates the end of a logical line of Python code; NL tokens are generated when
a logical line of code is continued over multiple physical lines.

Another function is provided to reverse the tokenization process. This is useful
for creating tools that tokenize a script, modify the token stream, and write
back the modified script.


"""
NL = None
def generate_tokens(readline):
	"""
	The :func:`generate_tokens` generator requires one argument, *readline*,
	which must be a callable object which provides the same interface as the
	:meth:`readline` method of built-in file objects (see section
	:ref:`bltin-file-objects`).  Each call to the function should return one line
	of input as a string.
	
	The generator produces 5-tuples with these members: the token type; the token
	string; a 2-tuple ``(srow, scol)`` of ints specifying the row and column
	where the token begins in the source; a 2-tuple ``(erow, ecol)`` of ints
	specifying the row and column where the token ends in the source; and the
	line on which the token was found.  The line passed (the last tuple item) is
	the *logical* line; continuation lines are included.
	
	"""
	pass
	
def tokenize(readline,tokeneater):
	"""
	The :func:`tokenize` function accepts two parameters: one representing the input
	stream, and one providing an output mechanism for :func:`tokenize`.
	
	The first parameter, *readline*, must be a callable object which provides the
	same interface as the :meth:`readline` method of built-in file objects (see
	section :ref:`bltin-file-objects`).  Each call to the function should return one
	line of input as a string. Alternately, *readline* may be a callable object that
	signals completion by raising :exc:`StopIteration`.
	
	"""
	pass
	
def untokenize(iterable):
	"""
	Converts tokens back into Python source code.  The *iterable* must return
	sequences with at least two elements, the token type and the token string.  Any
	additional sequence elements are ignored.
	
	The reconstructed script is returned as a single string.  The result is
	guaranteed to tokenize back to match the input so that the conversion is
	lossless and round-trips are assured.  The guarantee applies only to the token
	type and token string as the spacing between tokens (column positions) may
	change.
	
	"""
	pass
	
