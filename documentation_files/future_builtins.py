#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
""""""
def ascii(object):
	"""
	Returns the same as :func:`repr`.  In Python 3, :func:`repr` will return
	printable Unicode characters unescaped, while :func:`ascii` will always
	backslash-escape them.  Using :func:`future_builtins.ascii` instead of
	:func:`repr` in 2.6 code makes it clear that you need a pure ASCII return
	value.
	
	"""
	pass
	
def filter(function,iterable):
	"""
	Works like :func:`itertools.ifilter`.
	
	"""
	pass
	
def hex(object):
	"""
	Works like the built-in :func:`hex`, but instead of :meth:`__hex__` it will
	use the :meth:`__index__` method on its argument to get an integer that is
	then converted to hexadecimal.
	
	"""
	pass
	
def map(function,iterable,more):
	"""
	Works like :func:`itertools.imap`.
	
	"""
	pass
	
def oct(object):
	"""
	Works like the built-in :func:`oct`, but instead of :meth:`__oct__` it will
	use the :meth:`__index__` method on its argument to get an integer that is
	then converted to octal.
	
	"""
	pass
	
