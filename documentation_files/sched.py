#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
""":synopsis: General purpose event scheduler.
"""
class scheduler:


	"""
	The :class:`scheduler` class defines a generic interface to scheduling events.
	It needs two functions to actually deal with the "outside world" --- *timefunc*
	should be callable without arguments, and return  a number (the "time", in any
	units whatsoever).  The *delayfunc* function should be callable with one
	argument, compatible with the output of *timefunc*, and should delay that many
	time units. *delayfunc* will also be called with the argument ``0`` after each
	event is run to allow other threads an opportunity to run in multi-threaded
	applications.
	
	Example::
	
	>>> import sched, time
	>>> s = sched.scheduler(time.time, time.sleep)
	>>> def print_time(): print "From print_time", time.time()
	*more
	>>> def print_some_times():
	*more     print time.time()
	*more     s.enter(5, 1, print_time, ())
	*more     s.enter(10, 1, print_time, ())
	*more     s.run()
	*more     print time.time()
	*more
	>>> print_some_times()
	930343690.257
	From print_time 930343695.274
	From print_time 930343700.273
	930343700.276
	
	In multi-threaded environments, the :class:`scheduler` class has limitations
	with respect to thread-safety, inability to insert a new task before
	the one currently pending in a running scheduler, and holding up the main
	thread until the event queue is empty.  Instead, the preferred approach
	is to use the :class:`threading.Timer` class instead.
	
	Example::
	
	>>> import time
	>>> from threading import Timer
	>>> def print_time():
	*more     print "From print_time", time.time()
	*more
	>>> def print_some_times():
	*more     print time.time()
	*more     Timer(5, print_time, ()).start()
	*more     Timer(10, print_time, ()).start()
	*more     time.sleep(11)  # sleep while time-delay events execute
	*more     print time.time()
	*more
	>>> print_some_times()
	930343690.257
	From print_time 930343695.274
	From print_time 930343700.273
	930343701.301
	
	
	.. cheduler Objects
	-----------------
	
	:class:`scheduler` instances have the following methods and attributes:
	
	
	"""
	
	
	def __init__(self, timefunc,delayfunc):
		pass
	
	


