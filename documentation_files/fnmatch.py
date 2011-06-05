#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
""":synopsis: Unix shell style filename pattern matching.


"""
def fnmatch(filename,pattern):
	"""
	Test whether the *filename* string matches the *pattern* string, returning
	:const:`True` or :const:`False`.  If the operating system is case-insensitive,
	then both parameters will be normalized to all lower- or upper-case before
	the comparison is performed.  :func:`fnmatchcase` can be used to perform a
	case-sensitive comparison, regardless of whether that's standard for the
	operating system.
	
	This example will print all file names in the current directory with the
	extension ``.txt``::
	
	import fnmatch
	import os
	
	for file in os.listdir('.'):
	if fnmatch.fnmatch(file, '*.txt'):
	print file
	
	
	"""
	pass
	
def fnmatchcase(filename,pattern):
	"""
	Test whether *filename* matches *pattern*, returning :const:`True` or
	:const:`False`; the comparison is case-sensitive.
	
	
	"""
	pass
	
def filter(names,pattern):
	"""
	Return the subset of the list of *names* that match *pattern*. It is the same as
	``[n for n in names if fnmatch(n, pattern)]``, but implemented more efficiently.
	
	"""
	pass
	
def translate(pattern):
	"""
	Return the shell-style *pattern* converted to a regular expression.
	
	Be aware there is no way to quote meta-characters.
	
	Example:
	
	>>> import fnmatch, re
	>>>
	>>> regex = fnmatch.translate('*.txt')
	>>> regex
	'.*\\.txt$'
	>>> reobj = re.compile(regex)
	>>> reobj.match('foobar.txt')
	<_sre.SRE_Match object at 0xmore>
	
	
	"""
	pass
	
