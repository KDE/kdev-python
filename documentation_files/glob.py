#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
""":synopsis: Unix shell style pathname pattern expansion.


"""
def glob(pathname):
	"""
	Return a possibly-empty list of path names that match *pathname*, which must be
	a string containing a path specification. *pathname* can be either absolute
	(like :file:`/usr/src/Python-1.5/Makefile`) or relative (like
	:file:`../../Tools/\*/\*.gif`), and can contain shell-style wildcards. Broken
	symlinks are included in the results (as in the shell).
	
	
	"""
	pass
	
def iglob(pathname):
	"""
	Return an :term:`iterator` which yields the same values as :func:`glob`
	without actually storing them all simultaneously.
	
	"""
	pass
	
