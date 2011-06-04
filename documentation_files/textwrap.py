#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
""":synopsis: Text wrapping and filling
"""
def wrap(text,width,more):
	"""
	Wraps the single paragraph in *text* (a string) so every line is at most *width*
	characters long.  Returns a list of output lines, without final newlines.
	
	Optional keyword arguments correspond to the instance attributes of
	:class:`TextWrapper`, documented below.  *width* defaults to ``70``.
	
	
	"""
	pass
	
def fill(text,width,more):
	"""
	Wraps the single paragraph in *text*, and returns a single string containing the
	wrapped paragraph.  :func:`fill` is shorthand for  ::
	
	"\n".join(wrap(text, *more))
	
	In particular, :func:`fill` accepts exactly the same keyword arguments as
	:func:`wrap`.
	
	Both :func:`wrap` and :func:`fill` work by creating a :class:`TextWrapper`
	instance and calling a single method on it.  That instance is not reused, so for
	applications that wrap/fill many text strings, it will be more efficient for you
	to create your own :class:`TextWrapper` object.
	
	Text is preferably wrapped on whitespaces and right after the hyphens in
	hyphenated words; only then will long words be broken if necessary, unless
	:attr:`TextWrapper.break_long_words` is set to false.
	
	An additional utility function, :func:`dedent`, is provided to remove
	indentation from strings that have unwanted whitespace to the left of the text.
	
	
	"""
	pass
	
def dedent(text):
	"""
	Remove any common leading whitespace from every line in *text*.
	
	This can be used to make triple-quoted strings line up with the left edge of the
	display, while still presenting them in the source code in indented form.
	
	Note that tabs and spaces are both treated as whitespace, but they are not
	equal: the lines ``"  hello"`` and ``"\thello"`` are considered to have no
	common leading whitespace.  (This behaviour is new in Python 2.5; older versions
	of this module incorrectly expanded tabs before searching for common leading
	whitespace.)
	
	For example::
	
	def test():
	# end first line with \ to avoid the empty line!
	s = '''\
	hello
	world
	'''
	print repr(s)          # prints '    hello\n      world\n    '
	print repr(dedent(s))  # prints 'hello\n  world\n'
	
	
	"""
	pass
	
class TextWrapper:


	"""
	The :class:`TextWrapper` constructor accepts a number of optional keyword
	arguments.  Each argument corresponds to one instance attribute, so for example
	::
	
	wrapper = TextWrapper(initial_indent="* ")
	
	is the same as  ::
	
	wrapper = TextWrapper()
	wrapper.initial_indent = "* "
	
	You can re-use the same :class:`TextWrapper` object many times, and you can
	change any of its options through direct assignment to instance attributes
	between uses.
	
	The :class:`TextWrapper` instance attributes (and keyword arguments to the
	constructor) are as follows:
	
	
	"""
	
	
	def __init__(self, more):
		pass
	
	


