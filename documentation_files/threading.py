#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
""":synopsis: Higher-level threading interface.


This module constructs higher-level threading interfaces on top of the  lower
level :mod:`thread` module.
See also the :mod:`mutex` and :mod:`Queue` modules.

The :mod:`dummy_threading` module is provided for situations where
:mod:`threading` cannot be used because :mod:`thread` is missing.

"""
def active_count():
	"""activeCount()
	
	Return the number of :class:`Thread` objects currently alive.  The returned
	count is equal to the length of the list returned by :func:`.enumerate`.
	
	
	"""
	pass
	
def Condition():
	""":noindex:
	
	A factory function that returns a new condition variable object. A condition
	variable allows one or more threads to wait until they are notified by another
	thread.
	
	See :ref:`condition-objects`.
	
	
	"""
	pass
	
def current_thread():
	"""currentThread()
	
	Return the current :class:`Thread` object, corresponding to the caller's thread
	of control.  If the caller's thread of control was not created through the
	:mod:`threading` module, a dummy thread object with limited functionality is
	returned.
	
	
	"""
	pass
	
def enumerate():
	"""
	Return a list of all :class:`Thread` objects currently alive.  The list
	includes daemonic threads, dummy thread objects created by
	:func:`current_thread`, and the main thread.  It excludes terminated threads
	and threads that have not yet been started.
	
	
	"""
	pass
	
def Event():
	""":noindex:
	
	A factory function that returns a new event object.  An event manages a flag
	that can be set to true with the :meth:`~Event.set` method and reset to false
	with the :meth:`clear` method.  The :meth:`wait` method blocks until the flag
	is true.
	
	See :ref:`event-objects`.
	
	
	"""
	pass
	
class local:


	"""
	A class that represents thread-local data.  Thread-local data are data whose
	values are thread specific.  To manage thread-local data, just create an
	instance of :class:`local` (or a subclass) and store attributes on it::
	
	mydata = threading.local()
	mydata.x = 1
	
	The instance's values will be different for separate threads.
	
	For more details and extensive examples, see the documentation string of the
	:mod:`_threading_local` module.
	
	"""
	
	
	def __init__(self, ):
		pass
	
	def Lock():
		"""
		A factory function that returns a new primitive lock object.  Once a thread has
		acquired it, subsequent attempts to acquire it block, until it is released; any
		thread may release it.
		
		See :ref:`lock-objects`.
		
		
		"""
		pass
		
	def RLock():
		"""
		A factory function that returns a new reentrant lock object. A reentrant lock
		must be released by the thread that acquired it. Once a thread has acquired a
		reentrant lock, the same thread may acquire it again without blocking; the
		thread must release it once for each time it has acquired it.
		
		See :ref:`rlock-objects`.
		
		
		"""
		pass
		
	def Semaphore(value):
		""":noindex:
		
		A factory function that returns a new semaphore object.  A semaphore manages a
		counter representing the number of :meth:`release` calls minus the number of
		:meth:`acquire` calls, plus an initial value. The :meth:`acquire` method blocks
		if necessary until it can return without making the counter negative.  If not
		given, *value* defaults to 1.
		
		See :ref:`semaphore-objects`.
		
		
		"""
		pass
		
	def BoundedSemaphore(value):
		"""
		A factory function that returns a new bounded semaphore object.  A bounded
		semaphore checks to make sure its current value doesn't exceed its initial
		value.  If it does, :exc:`ValueError` is raised. In most situations semaphores
		are used to guard resources with limited capacity.  If the semaphore is released
		too many times it's a sign of a bug.  If not given, *value* defaults to 1.
		
		
		"""
		pass
		
	


class Thread:


	""":noindex:
	
	A class that represents a thread of control.  This class can be safely
	subclassed in a limited fashion.
	
	See :ref:`thread-objects`.
	
	
	"""
	
	
	def __init__(self, ):
		pass
	
	


class Timer:


	""":noindex:
	
	A thread that executes a function after a specified interval has passed.
	
	See :ref:`timer-objects`.
	
	
	"""
	
	
	def __init__(self, ):
		pass
	
	def settrace(func):
		"""
		"""
		pass
		
	def setprofile(func):
		"""
		"""
		pass
		
	def stack_size(size):
		"""
		Return the thread stack size used when creating new threads.  The optional
		*size* argument specifies the stack size to be used for subsequently created
		threads, and must be 0 (use platform or configured default) or a positive
		integer value of at least 32,768 (32kB). If changing the thread stack size is
		unsupported, a :exc:`ThreadError` is raised.  If the specified stack size is
		invalid, a :exc:`ValueError` is raised and the stack size is unmodified.  32kB
		is currently the minimum supported stack size value to guarantee sufficient
		stack space for the interpreter itself.  Note that some platforms may have
		particular restrictions on values for the stack size, such as requiring a
		minimum stack size > 32kB or requiring allocation in multiples of the system
		memory page size - platform documentation should be referred to for more
		information (4kB pages are common; using multiples of 4096 for the stack size is
		the suggested approach in the absence of more specific information).
		Availability: Windows, systems with POSIX threads.
		
		"""
		pass
		
	


class Thread:


	"""
	This constructor should always be called with keyword arguments.  Arguments
	are:
	
	*group* should be ``None``; reserved for future extension when a
	:class:`ThreadGroup` class is implemented.
	
	*target* is the callable object to be invoked by the :meth:`run` method.
	Defaults to ``None``, meaning nothing is called.
	
	*name* is the thread name.  By default, a unique name is constructed of the
	form "Thread-*N*" where *N* is a small decimal number.
	
	*args* is the argument tuple for the target invocation.  Defaults to ``()``.
	
	*kwargs* is a dictionary of keyword arguments for the target invocation.
	Defaults to ``{}``.
	
	If the subclass overrides the constructor, it must make sure to invoke the
	base class constructor (``Thread.__init__()``) before doing anything else to
	the thread.
	
	"""
	
	
	def __init__(self, group=None,target=None,name=None,args=[],kwargs={}):
		pass
	
	


class Condition:


	"""
	If the *lock* argument is given and not ``None``, it must be a :class:`Lock`
	or :class:`RLock` object, and it is used as the underlying lock.  Otherwise,
	a new :class:`RLock` object is created and used as the underlying lock.
	
	"""
	
	
	def __init__(self, lock):
		pass
	
	


class Semaphore:


	"""
	The optional argument gives the initial *value* for the internal counter; it
	defaults to ``1``. If the *value* given is less than 0, :exc:`ValueError` is
	raised.
	
	"""
	
	
	def __init__(self, value):
		pass
	
	


class Event:


	"""
	The internal flag is initially false.
	
	"""
	
	
	def __init__(self, ):
		pass
	
	


class Timer:


	"""
	Create a timer that will run *function* with arguments *args* and  keyword
	arguments *kwargs*, after *interval* seconds have passed.
	
	"""
	
	
	def __init__(self, interval,function,args=[],kwargs={}):
		pass
	
	


