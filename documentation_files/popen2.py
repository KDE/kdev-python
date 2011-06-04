#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
""":synopsis: Subprocesses with accessible standard I/O streams.
:deprecated:
"""
def popen2(cmd,bufsize,mode):
	"""
	Executes *cmd* as a sub-process.  Returns the file objects ``(child_stdout,
	child_stdin)``.
	
	
	"""
	pass
	
def popen3(cmd,bufsize,mode):
	"""
	Executes *cmd* as a sub-process.  Returns the file objects ``(child_stdout,
	child_stdin, child_stderr)``.
	
	
	"""
	pass
	
def popen4(cmd,bufsize,mode):
	"""
	Executes *cmd* as a sub-process.  Returns the file objects
	``(child_stdout_and_stderr, child_stdin)``.
	
	"""
	pass
	
class Popen3:


	"""
	This class represents a child process.  Normally, :class:`Popen3` instances are
	created using the :func:`popen2` and :func:`popen3` factory functions described
	above.
	
	If not using one of the helper functions to create :class:`Popen3` objects, the
	parameter *cmd* is the shell command to execute in a sub-process.  The
	*capturestderr* flag, if true, specifies that the object should capture standard
	error output of the child process. The default is false.  If the *bufsize*
	parameter is specified, it specifies the size of the I/O buffers to/from the
	child process.
	
	
	"""
	
	
	def __init__(self, cmd,capturestderr,bufsize):
		pass
	
	


class Popen4:


	"""
	Similar to :class:`Popen3`, but always captures standard error into the same
	file object as standard output.  These are typically created using
	:func:`popen4`.
	
	"""
	
	
	def __init__(self, cmd,bufsize):
		pass
	
	


