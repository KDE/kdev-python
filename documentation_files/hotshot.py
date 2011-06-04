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
	
	
	def __init__(self, logfile,lineevents,linetimings):
		pass
	
	


