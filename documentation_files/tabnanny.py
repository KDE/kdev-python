#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
""":synopsis: Tool for detecting white space related problems in Python source files in a
directory tree.
"""
"""
Flag indicating whether to print verbose messages. This is incremented by the
``-v`` option if called as a script.


"""
verbose = None
"""
Flag indicating whether to print only the filenames of files containing
whitespace related problems.  This is set to true by the ``-q`` option if called
as a script.


"""
filename_only = None
def check(file_or_dir):
	"""
	If *file_or_dir* is a directory and not a symbolic link, then recursively
	descend the directory tree named by *file_or_dir*, checking all :file:`.py`
	files along the way.  If *file_or_dir* is an ordinary Python source file, it is
	checked for whitespace related problems.  The diagnostic messages are written to
	standard output using the print statement.
	
	
	"""
	pass
	
def tokeneater(type,token,start,end,line):
	"""
	This function is used by :func:`check` as a callback parameter to the function
	:func:`tokenize.tokenize`.
	
	.. rrprint, format_witnesses, Whitespace, check_equal, indents,
	reset_globals
	
	
	"""
	pass
	
