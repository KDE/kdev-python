#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
""":synopsis: Portable parser for command line options; support both short and long option
names.

"""
def getopt(args,options,long_options):
	"""
	Parses command line options and parameter list.  *args* is the argument list to
	be parsed, without the leading reference to the running program. Typically, this
	means ``sys.argv[1:]``. *options* is the string of option letters that the
	script wants to recognize, with options that require an argument followed by a
	colon (``':'``; i.e., the same format that Unix :cfunc:`getopt` uses).
	
	"""
	pass
	
def gnu_getopt(args,options,long_options):
	"""
	This function works like :func:`getopt`, except that GNU style scanning mode is
	used by default. This means that option and non-option arguments may be
	intermixed. The :func:`getopt` function stops processing options as soon as a
	non-option argument is encountered.
	
	If the first character of the option string is ``'+'``, or if the environment
	variable :envvar:`POSIXLY_CORRECT` is set, then option processing stops as
	soon as a non-option argument is encountered.
	
	"""
	pass
	
