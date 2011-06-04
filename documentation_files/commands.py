#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
""":platform: Unix
:synopsis: Utility functions for running external commands.
:deprecated:

"""
def getstatusoutput(cmd):
	"""
	Execute the string *cmd* in a shell with :func:`os.popen` and return a 2-tuple
	``(status, output)``.  *cmd* is actually run as ``{ cmd ; } 2>&1``, so that the
	returned output will contain output or error messages. A trailing newline is
	stripped from the output. The exit status for the command can be interpreted
	according to the rules for the C function :cfunc:`wait`.
	
	
	"""
	pass
	
def getoutput(cmd):
	"""
	Like :func:`getstatusoutput`, except the exit status is ignored and the return
	value is a string containing the command's output.
	
	
	"""
	pass
	
def getstatus(file):
	"""
	Return the output of ``ls -ld file`` as a string.  This function uses the
	:func:`getoutput` function, and properly escapes backslashes and dollar signs in
	the argument.
	
	"""
	pass
	
