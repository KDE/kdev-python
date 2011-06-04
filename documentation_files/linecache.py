#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
""":synopsis: This module provides random access to individual lines from text files.
"""
def getline(filename,lineno,module_globals):
	"""
	Get line *lineno* from file named *filename*. This function will never raise an
	exception --- it will return ``''`` on errors (the terminating newline character
	will be included for lines that are found).
	
	"""
	pass
	
def clearcache():
	"""
	Clear the cache.  Use this function if you no longer need lines from files
	previously read using :func:`getline`.
	
	
	"""
	pass
	
