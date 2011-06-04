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
	
	
	def __init__(self, ):
		pass
	
	def print_exc(self, file=None):
		"""
		Helper to print a traceback from the timed code.
		
		Typical use::
		
		t = Timer(*more)       # outside the try/except
		try:
		t.timeit(*more)    # or t.repeat(*more)
		except:
		t.print_exc()
		
		The advantage over the standard traceback is that source lines in the compiled
		template will be displayed. The optional *file* argument directs where the
		traceback is sent; it defaults to ``sys.stderr``.
		
		
		"""
		pass
		
	def repeat(self, repeat=3,number=1000000):
		"""
		Call :meth:`timeit` a few times.
		
		This is a convenience function that calls the :meth:`timeit` repeatedly,
		returning a list of results.  The first argument specifies how many times to
		call :meth:`timeit`.  The second argument specifies the *number* argument for
		:func:`timeit`.
		
		"""
		pass
		
	def timeit(self, number=1000000):
		"""
		Time *number* executions of the main statement. This executes the setup
		statement once, and then returns the time it takes to execute the main statement
		a number of times, measured in seconds as a float.  The argument is the number
		of times through the loop, defaulting to one million.  The main statement, the
		setup statement and the timer function to be used are passed to the constructor.
		
		"""
		pass
		
	def repeat(self, stmt,setup,timer,repeat=3,number=1000000):
		"""
		Create a :class:`Timer` instance with the given statement, setup code and timer
		function and run its :meth:`repeat` method with the given repeat count and
		*number* executions.
		
		"""
		pass
		
	def timeit(self, stmt,setup,timer,number=1000000):
		"""
		Create a :class:`Timer` instance with the given statement, setup code and timer
		function and run its :meth:`timeit` method with *number* executions.
		
		"""
		pass
		
	


