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
	
	def Lock(self, ):
		"""
		A factory function that returns a new primitive lock object.  Once a thread has
		acquired it, subsequent attempts to acquire it block, until it is released; any
		thread may release it.
		
		See :ref:`lock-objects`.
		
		
		"""
		pass
		
	def RLock(self, ):
		"""
		A factory function that returns a new reentrant lock object. A reentrant lock
		must be released by the thread that acquired it. Once a thread has acquired a
		reentrant lock, the same thread may acquire it again without blocking; the
		thread must release it once for each time it has acquired it.
		
		See :ref:`rlock-objects`.
		
		
		"""
		pass
		
	def Semaphore(self, value):
		""":noindex:
		
		A factory function that returns a new semaphore object.  A semaphore manages a
		counter representing the number of :meth:`release` calls minus the number of
		:meth:`acquire` calls, plus an initial value. The :meth:`acquire` method blocks
		if necessary until it can return without making the counter negative.  If not
		given, *value* defaults to 1.
		
		See :ref:`semaphore-objects`.
		
		
		"""
		pass
		
	def BoundedSemaphore(self, value):
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
	
	def start(self, ):
		"""
		Start the thread's activity.
		
		It must be called at most once per thread object.  It arranges for the
		object's :meth:`run` method to be invoked in a separate thread of control.
		
		This method will raise a :exc:`RuntimeError` if called more than once
		on the same thread object.
		
		"""
		pass
		
	def run(self, ):
		"""
		Method representing the thread's activity.
		
		You may override this method in a subclass.  The standard :meth:`run`
		method invokes the callable object passed to the object's constructor as
		the *target* argument, if any, with sequential and keyword arguments taken
		from the *args* and *kwargs* arguments, respectively.
		
		"""
		pass
		
	def join(self, timeout):
		"""
		Wait until the thread terminates. This blocks the calling thread until the
		thread whose :meth:`join` method is called terminates -- either normally
		or through an unhandled exception -- or until the optional timeout occurs.
		
		When the *timeout* argument is present and not ``None``, it should be a
		floating point number specifying a timeout for the operation in seconds
		(or fractions thereof). As :meth:`join` always returns ``None``, you must
		call :meth:`isAlive` after :meth:`join` to decide whether a timeout
		happened -- if the thread is still alive, the :meth:`join` call timed out.
		
		When the *timeout* argument is not present or ``None``, the operation will
		block until the thread terminates.
		
		A thread can be :meth:`join`\ ed many times.
		
		:meth:`join` raises a :exc:`RuntimeError` if an attempt is made to join
		the current thread as that would cause a deadlock. It is also an error to
		:meth:`join` a thread before it has been started and attempts to do so
		raises the same exception.
		
		"""
		pass
		
	def getName(self, ):
		"""setName()
		
		Old API for :attr:`~Thread.name`.
		
		"""
		pass
		
	def is_alive(self, ):
		"""isAlive()
		
		Return whether the thread is alive.
		
		This method returns ``True`` just before the :meth:`run` method starts
		until just after the :meth:`run` method terminates.  The module function
		:func:`.enumerate` returns a list of all alive threads.
		
		"""
		pass
		
	def isDaemon(self, ):
		"""setDaemon()
		
		Old API for :attr:`~Thread.daemon`.
		
		"""
		pass
		
	


class Timer:


	""":noindex:
	
	A thread that executes a function after a specified interval has passed.
	
	See :ref:`timer-objects`.
	
	
	"""
	
	
	def __init__(self, ):
		pass
	
	def settrace(self, func):
		"""
		"""
		pass
		
	def setprofile(self, func):
		"""
		"""
		pass
		
	def stack_size(self, size):
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
		
	def cancel(self, ):
		"""
		Stop the timer, and cancel the execution of the timer's action.  This will
		only work if the timer is still in its waiting stage.
		
		
		.. sing locks, conditions, and semaphores in the :keyword:`with` statement
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
	
	
	def __init__(self, ):
		pass
	
	def start(self, ):
		"""
		Start the thread's activity.
		
		It must be called at most once per thread object.  It arranges for the
		object's :meth:`run` method to be invoked in a separate thread of control.
		
		This method will raise a :exc:`RuntimeError` if called more than once
		on the same thread object.
		
		"""
		pass
		
	def run(self, ):
		"""
		Method representing the thread's activity.
		
		You may override this method in a subclass.  The standard :meth:`run`
		method invokes the callable object passed to the object's constructor as
		the *target* argument, if any, with sequential and keyword arguments taken
		from the *args* and *kwargs* arguments, respectively.
		
		"""
		pass
		
	def join(self, timeout):
		"""
		Wait until the thread terminates. This blocks the calling thread until the
		thread whose :meth:`join` method is called terminates -- either normally
		or through an unhandled exception -- or until the optional timeout occurs.
		
		When the *timeout* argument is present and not ``None``, it should be a
		floating point number specifying a timeout for the operation in seconds
		(or fractions thereof). As :meth:`join` always returns ``None``, you must
		call :meth:`isAlive` after :meth:`join` to decide whether a timeout
		happened -- if the thread is still alive, the :meth:`join` call timed out.
		
		When the *timeout* argument is not present or ``None``, the operation will
		block until the thread terminates.
		
		A thread can be :meth:`join`\ ed many times.
		
		:meth:`join` raises a :exc:`RuntimeError` if an attempt is made to join
		the current thread as that would cause a deadlock. It is also an error to
		:meth:`join` a thread before it has been started and attempts to do so
		raises the same exception.
		
		"""
		pass
		
	def getName(self, ):
		"""setName()
		
		Old API for :attr:`~Thread.name`.
		
		"""
		pass
		
	def is_alive(self, ):
		"""isAlive()
		
		Return whether the thread is alive.
		
		This method returns ``True`` just before the :meth:`run` method starts
		until just after the :meth:`run` method terminates.  The module function
		:func:`.enumerate` returns a list of all alive threads.
		
		"""
		pass
		
	def isDaemon(self, ):
		"""setDaemon()
		
		Old API for :attr:`~Thread.daemon`.
		
		"""
		pass
		
	


class Condition:


	"""
	If the *lock* argument is given and not ``None``, it must be a :class:`Lock`
	or :class:`RLock` object, and it is used as the underlying lock.  Otherwise,
	a new :class:`RLock` object is created and used as the underlying lock.
	
	"""
	
	
	def __init__(self, ):
		pass
	
	def acquire(self, args):
		"""
		Acquire the underlying lock. This method calls the corresponding method on
		the underlying lock; the return value is whatever that method returns.
		
		"""
		pass
		
	def release(self, ):
		"""
		Release the underlying lock. This method calls the corresponding method on
		the underlying lock; there is no return value.
		
		"""
		pass
		
	def wait(self, timeout):
		"""
		Wait until notified or until a timeout occurs. If the calling thread has not
		acquired the lock when this method is called, a :exc:`RuntimeError` is raised.
		
		This method releases the underlying lock, and then blocks until it is
		awakened by a :meth:`notify` or :meth:`notifyAll` call for the same
		condition variable in another thread, or until the optional timeout
		occurs.  Once awakened or timed out, it re-acquires the lock and returns.
		
		When the *timeout* argument is present and not ``None``, it should be a
		floating point number specifying a timeout for the operation in seconds
		(or fractions thereof).
		
		When the underlying lock is an :class:`RLock`, it is not released using
		its :meth:`release` method, since this may not actually unlock the lock
		when it was acquired multiple times recursively.  Instead, an internal
		interface of the :class:`RLock` class is used, which really unlocks it
		even when it has been recursively acquired several times. Another internal
		interface is then used to restore the recursion level when the lock is
		reacquired.
		
		"""
		pass
		
	def notify(self, ):
		"""
		Wake up a thread waiting on this condition, if any.  If the calling thread
		has not acquired the lock when this method is called, a
		:exc:`RuntimeError` is raised.
		
		This method wakes up one of the threads waiting for the condition
		variable, if any are waiting; it is a no-op if no threads are waiting.
		
		The current implementation wakes up exactly one thread, if any are
		waiting.  However, it's not safe to rely on this behavior.  A future,
		optimized implementation may occasionally wake up more than one thread.
		
		Note: the awakened thread does not actually return from its :meth:`wait`
		call until it can reacquire the lock.  Since :meth:`notify` does not
		release the lock, its caller should.
		
		"""
		pass
		
	def notify_all(self, ):
		"""notifyAll()
		
		Wake up all threads waiting on this condition.  This method acts like
		:meth:`notify`, but wakes up all waiting threads instead of one. If the
		calling thread has not acquired the lock when this method is called, a
		:exc:`RuntimeError` is raised.
		
		
		.. emaphore Objects
		"""
		pass
		
	


class Semaphore:


	"""
	The optional argument gives the initial *value* for the internal counter; it
	defaults to ``1``. If the *value* given is less than 0, :exc:`ValueError` is
	raised.
	
	"""
	
	
	def __init__(self, ):
		pass
	
	def acquire(self, blocking):
		"""
		Acquire a semaphore.
		
		When invoked without arguments: if the internal counter is larger than
		zero on entry, decrement it by one and return immediately.  If it is zero
		on entry, block, waiting until some other thread has called
		:meth:`release` to make it larger than zero.  This is done with proper
		interlocking so that if multiple :meth:`acquire` calls are blocked,
		:meth:`release` will wake exactly one of them up.  The implementation may
		pick one at random, so the order in which blocked threads are awakened
		should not be relied on.  There is no return value in this case.
		
		When invoked with *blocking* set to true, do the same thing as when called
		without arguments, and return true.
		
		When invoked with *blocking* set to false, do not block.  If a call
		without an argument would block, return false immediately; otherwise, do
		the same thing as when called without arguments, and return true.
		
		"""
		pass
		
	def release(self, ):
		"""
		Release a semaphore, incrementing the internal counter by one.  When it
		was zero on entry and another thread is waiting for it to become larger
		than zero again, wake up that thread.
		
		
		.. class:`Semaphore` Example
		"""
		pass
		
	


class Event:


	"""
	The internal flag is initially false.
	
	"""
	
	
	def __init__(self, ):
		pass
	
	def is_set(self, ):
		"""isSet()
		
		Return true if and only if the internal flag is true.
		
		"""
		pass
		
	def set(self, ):
		"""
		Set the internal flag to true. All threads waiting for it to become true
		are awakened. Threads that call :meth:`wait` once the flag is true will
		not block at all.
		
		"""
		pass
		
	def clear(self, ):
		"""
		Reset the internal flag to false. Subsequently, threads calling
		:meth:`wait` will block until :meth:`.set` is called to set the internal
		flag to true again.
		
		"""
		pass
		
	def wait(self, timeout):
		"""
		Block until the internal flag is true.  If the internal flag is true on
		entry, return immediately.  Otherwise, block until another thread calls
		:meth:`.set` to set the flag to true, or until the optional timeout
		occurs.
		
		When the timeout argument is present and not ``None``, it should be a
		floating point number specifying a timeout for the operation in seconds
		(or fractions thereof).
		
		This method returns the internal flag on exit, so it will always return
		``True`` except if a timeout is given and the operation times out.
		
		"""
		pass
		
	


class Timer:


	"""
	Create a timer that will run *function* with arguments *args* and  keyword
	arguments *kwargs*, after *interval* seconds have passed.
	
	"""
	
	
	def __init__(self, ):
		pass
	
	def settrace(self, func):
		"""
		"""
		pass
		
	def setprofile(self, func):
		"""
		"""
		pass
		
	def stack_size(self, size):
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
		
	def cancel(self, ):
		"""
		Stop the timer, and cancel the execution of the timer's action.  This will
		only work if the timer is still in its waiting stage.
		
		
		.. sing locks, conditions, and semaphores in the :keyword:`with` statement
		"""
		pass
		
	


