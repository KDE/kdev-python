#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
""":synopsis: Statistics object for use with the profiler.


"""
class Stats:


	"""
	This class constructor creates an instance of a "statistics object" from a
	*filename* (or set of filenames).  :class:`Stats` objects are manipulated by
	methods, in order to print useful reports.  You may specify an alternate output
	stream by giving the keyword argument, ``stream``.
	
	The file selected by the above constructor must have been created by the
	corresponding version of :mod:`profile` or :mod:`cProfile`.  To be specific,
	there is *no* file compatibility guaranteed with future versions of this
	profiler, and there is no compatibility with files produced by other profilers.
	If several files are provided, all the statistics for identical functions will
	be coalesced, so that an overall view of several processes can be considered in
	a single report.  If additional files need to be combined with data in an
	existing :class:`Stats` object, the :meth:`add` method can be used.
	
	.. he old system profiler).
	
	"""
	
	
	def __init__(self, filename,stream=sys):
		pass
	
	


