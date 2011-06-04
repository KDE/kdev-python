#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
""":synopsis: Register and execute cleanup functions.
"""
def register(func,args,kargs):
	"""
	Register *func* as a function to be executed at termination.  Any optional
	arguments that are to be passed to *func* must be passed as arguments to
	:func:`register`.
	
	At normal program termination (for instance, if :func:`sys.exit` is called or
	the main module's execution completes), all functions registered are called in
	last in, first out order.  The assumption is that lower level modules will
	normally be imported before higher level modules and thus must be cleaned up
	later.
	
	If an exception is raised during execution of the exit handlers, a traceback is
	printed (unless :exc:`SystemExit` is raised) and the exception information is
	saved.  After all exit handlers have had a chance to run the last exception to
	be raised is re-raised.
	
	"""
	pass
	
