#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
""":synopsis: Measure the execution time of small code snippets.


"""
class Timer:


	"""
	Class for timing execution speed of small code snippets.
	
	The constructor takes a statement to be timed, an additional statement used for
	setup, and a timer function.  Both statements default to ``'pass'``; the timer
	function is platform-dependent (see the module doc string).  *stmt* and *setup*
	may also contain multiple statements separated by ``;`` or newlines, as long as
	they don't contain multi-line string literals.
	
	To measure the execution time of the first statement, use the :meth:`timeit`
	method.  The :meth:`repeat` method is a convenience to call :meth:`timeit`
	multiple times and return a list of results.
	
	"""
	
	
	def __init__(self, stmt='pass',setup='pass',timer="timerfunction"):
		pass
	
	def repeat(stmt,setup,timer,repeat=3,number=1000000):
		"""
		Create a :class:`Timer` instance with the given statement, setup code and timer
		function and run its :meth:`repeat` method with the given repeat count and
		*number* executions.
		
		"""
		pass
		
	def timeit(stmt,setup,timer,number=1000000):
		"""
		Create a :class:`Timer` instance with the given statement, setup code and timer
		function and run its :meth:`timeit` method with *number* executions.
		
		"""
		pass
		
	


