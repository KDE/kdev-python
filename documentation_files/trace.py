#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
""":synopsis: Trace or track Python statement execution.


The :mod:`trace` module allows you to trace program execution, generate
annotated statement coverage listings, print caller/callee relationships and
list functions executed during a program run.  It can be used in another program
or from the command line.

"""
class Trace:


	"""
	Create an object to trace execution of a single statement or expression.  All
	parameters are optional.  *count* enables counting of line numbers.  *trace*
	enables line execution tracing.  *countfuncs* enables listing of the
	functions called during the run.  *countcallers* enables call relationship
	tracking.  *ignoremods* is a list of modules or packages to ignore.
	*ignoredirs* is a list of directories whose modules or packages should be
	ignored.  *infile* is the name of the file from which to read stored count
	information.  *outfile* is the name of the file in which to write updated
	count information.  *timing* enables a timestamp relative to when tracing was
	started to be displayed.
	
	"""
	
	
	def __init__(self, ):
		pass
	
	def run(self, cmd):
		"""
		Execute the command and gather statistics from the execution with
		the current tracing parameters.  *cmd* must be a string or code object,
		suitable for passing into :func:`exec`.
		
		"""
		pass
		
	def runctx(self, cmd,globals=None,locals=None):
		"""
		Execute the command and gather statistics from the execution with the
		current tracing parameters, in the defined global and local
		environments.  If not defined, *globals* and *locals* default to empty
		dictionaries.
		
		"""
		pass
		
	def runfunc(self, func,args,kwds):
		"""
		Call *func* with the given arguments under control of the :class:`Trace`
		object with the current tracing parameters.
		
		"""
		pass
		
	def results(self, ):
		"""
		Return a :class:`CoverageResults` object that contains the cumulative
		results of all previous calls to ``run``, ``runctx`` and ``runfunc``
		for the given :class:`Trace` instance.  Does not reset the accumulated
		trace results.
		
		"""
		pass
		
	


class CoverageResults:


	"""
	A container for coverage results, created by :meth:`Trace.results`.  Should
	not be created directly by the user.
	
	"""
	
	
	def __init__(self, ):
		pass
	
	def update(self, other):
		"""
		Merge in data from another :class:`CoverageResults` object.
		
		"""
		pass
		
	def write_results(self, show_missing=True,summary=False,coverdir=None):
		"""
		Write coverage results.  Set *show_missing* to show lines that had no
		hits.  Set *summary* to include in the output the coverage summary per
		module.  *coverdir* specifies the directory into which the coverage
		result files will be output.  If ``None``, the results for each source
		file are placed in its directory.
		
		A simple example demonstrating the use of the programmatic interface::
		"""
		pass
		
	


