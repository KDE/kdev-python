#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
""":synopsis: High performance logging profiler, mostly written in C.
"""
class Profile:


	"""
	The profiler object. The argument *logfile* is the name of a log file to use for
	logged profile data. The argument *lineevents* specifies whether to generate
	events for every source line, or just on function call/return. It defaults to
	``0`` (only log function call/return). The argument *linetimings* specifies
	whether to record timing information. It defaults to ``1`` (store timing
	information).
	
	
	.. rofile Objects
	---------------
	
	Profile objects have the following methods:
	
	
	"""
	
	
	def __init__(self, ):
		pass
	
	def addinfo(self, key,value):
		"""
		Add an arbitrary labelled value to the profile output.
		
		
		"""
		pass
		
	def close(self, ):
		"""
		Close the logfile and terminate the profiler.
		
		
		"""
		pass
		
	def fileno(self, ):
		"""
		Return the file descriptor of the profiler's log file.
		
		
		"""
		pass
		
	def run(self, cmd):
		"""
		Profile an :keyword:`exec`\ -compatible string in the script environment. The
		globals from the :mod:`__main__` module are used as both the globals and locals
		for the script.
		
		
		"""
		pass
		
	def runcall(self, func,args,keywords):
		"""
		Profile a single call of a callable. Additional positional and keyword arguments
		may be passed along; the result of the call is returned, and exceptions are
		allowed to propagate cleanly, while ensuring that profiling is disabled on the
		way out.
		
		
		"""
		pass
		
	def runctx(self, cmd,globals,locals):
		"""
		Evaluate an :keyword:`exec`\ -compatible string in a specific environment. The
		string is compiled before profiling begins.
		
		
		"""
		pass
		
	def start(self, ):
		"""
		Start the profiler.
		
		
		"""
		pass
		
	def stop(self, ):
		"""
		Stop the profiler.
		
		
		Using hotshot data
		------------------
		
		"""
		pass
		
	


