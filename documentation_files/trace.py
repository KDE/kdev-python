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
	
	
	def __init__(self, count=1,trace=1,countfuncs=0,countcallers=0,ignoremods=[],ignoredirs=[],infile=None,outfile=None,timing=False):
		pass
	
	


class CoverageResults:


	"""
	A container for coverage results, created by :meth:`Trace.results`.  Should
	not be created directly by the user.
	
	"""
	
	
	def __init__(self, ):
		pass
	
	


