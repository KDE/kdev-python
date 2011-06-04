#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
""":synopsis: Python profiler


The primary entry point for the profiler is the global function
:func:`profile.run` (resp. :func:`cProfile.run`). It is typically used to create
any profile information.  The reports are formatted and printed using methods of
the class :class:`pstats.Stats`.  The following is a description of all of these
standard entry points and functions.  For a more in-depth view of some of the
code, consider reading the later section on Profiler Extensions, which includes
discussion of how to derive "better" profilers from the classes presented, or
reading the source code for these modules.


"""
def run(command,filename):
	"""
	This function takes a single argument that can be passed to the
	:keyword:`exec` statement, and an optional file name.  In all cases this
	routine attempts to :keyword:`exec` its first argument, and gather profiling
	statistics from the execution. If no file name is present, then this function
	automatically prints a simple profiling report, sorted by the standard name
	string (file/line/function-name) that is presented in each line.  The
	following is a typical output from such a call::
	
	2706 function calls (2004 primitive calls) in 4.504 CPU seconds
	
	Ordered by: standard name
	
	ncalls  tottime  percall  cumtime  percall filename:lineno(function)
	2    0.006    0.003    0.953    0.477 pobject.py:75(save_objects)
	43/3    0.533    0.012    0.749    0.250 pobject.py:99(evaluate)
	*more
	
	The first line indicates that 2706 calls were monitored.  Of those calls, 2004
	were :dfn:`primitive`.  We define :dfn:`primitive` to mean that the call was not
	induced via recursion. The next line: ``Ordered by: standard name``, indicates
	that the text string in the far right column was used to sort the output. The
	column headings include:
	
	ncalls
	for the number of calls,
	
	tottime
	for the total time spent in the given function (and excluding time made in calls
	to sub-functions),
	
	percall
	is the quotient of ``tottime`` divided by ``ncalls``
	
	cumtime
	is the total time spent in this and all subfunctions (from invocation till
	exit). This figure is accurate *even* for recursive functions.
	
	percall
	is the quotient of ``cumtime`` divided by primitive calls
	
	filename:lineno(function)
	provides the respective data of each function
	
	When there are two numbers in the first column (for example, ``43/3``), then the
	latter is the number of primitive calls, and the former is the actual number of
	calls.  Note that when the function does not recurse, these two values are the
	same, and only the single figure is printed.
	
	
	"""
	pass
	
def runctx(command,globals,locals,filename):
	"""
	This function is similar to :func:`run`, with added arguments to supply the
	globals and locals dictionaries for the *command* string.
	
	Analysis of the profiler data is done using the :class:`Stats` class.
	
	"""
	pass
	
