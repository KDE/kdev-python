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
	more
	>>> def print_some_times():
	more     print time.time()
	more     s.enter(5, 1, print_time, ())
	more     s.enter(10, 1, print_time, ())
	more     s.run()
	more     print time.time()
	more
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
	more     print "From print_time", time.time()
	more
	>>> def print_some_times():
	more     print time.time()
	more     Timer(5, print_time, ()).start()
	more     Timer(10, print_time, ()).start()
	more     time.sleep(11)  # sleep while time-delay events execute
	more     print time.time()
	more
	>>> print_some_times()
	930343690.257
	From print_time 930343695.274
	From print_time 930343700.273
	930343701.301
	
	
	.. cheduler Objects
	-----------------
	
	:class:`scheduler` instances have the following methods and attributes:
	
	
	"""
	
	
	def __init__(self, ):
		pass
	
	def enterabs(self, time,priority,action,argument):
		"""
		Schedule a new event. The *time* argument should be a numeric type compatible
		with the return value of the *timefunc* function passed  to the constructor.
		Events scheduled for the same *time* will be executed in the order of their
		*priority*.
		
		Executing the event means executing ``action(*argument)``.  *argument* must be a
		sequence holding the parameters for *action*.
		
		Return value is an event which may be used for later cancellation of the event
		(see :meth:`cancel`).
		
		
		"""
		pass
		
	def enter(self, delay,priority,action,argument):
		"""
		Schedule an event for *delay* more time units. Other then the relative time, the
		other arguments, the effect and the return value are the same as those for
		:meth:`enterabs`.
		
		
		"""
		pass
		
	def cancel(self, event):
		"""
		Remove the event from the queue. If *event* is not an event currently in the
		queue, this method will raise a :exc:`ValueError`.
		
		
		"""
		pass
		
	def empty(self, ):
		"""
		Return true if the event queue is empty.
		
		
		"""
		pass
		
	def run(self, ):
		"""
		Run all scheduled events. This function will wait  (using the :func:`delayfunc`
		function passed to the constructor) for the next event, then execute it and so
		on until there are no more scheduled events.
		
		Either *action* or *delayfunc* can raise an exception.  In either case, the
		scheduler will maintain a consistent state and propagate the exception.  If an
		exception is raised by *action*, the event will not be attempted in future calls
		to :meth:`run`.
		
		If a sequence of events takes longer to run than the time available before the
		next event, the scheduler will simply fall behind.  No events will be dropped;
		the calling code is responsible for canceling  events which are no longer
		pertinent.
		
		"""
		pass
		
	


