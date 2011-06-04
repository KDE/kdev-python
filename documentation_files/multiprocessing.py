#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
""":synopsis: Process-based "threading" interface.

"""
class Process:


	"""
	Process objects represent activity that is run in a separate process. The
	:class:`Process` class has equivalents of all the methods of
	:class:`threading.Thread`.
	
	The constructor should always be called with keyword arguments. *group*
	should always be ``None``; it exists solely for compatibility with
	:class:`threading.Thread`.  *target* is the callable object to be invoked by
	the :meth:`run()` method.  It defaults to ``None``, meaning nothing is
	called. *name* is the process name.  By default, a unique name is constructed
	of the form 'Process-N\ :sub:`1`:N\ :sub:`2`:*more:N\ :sub:`k`' where N\
	:sub:`1`,N\ :sub:`2`,*more,N\ :sub:`k` is a sequence of integers whose length
	is determined by the *generation* of the process.  *args* is the argument
	tuple for the target invocation.  *kwargs* is a dictionary of keyword
	arguments for the target invocation.  By default, no arguments are passed to
	*target*.
	
	If a subclass overrides the constructor, it must make sure it invokes the
	base class constructor (:meth:`Process.__init__`) before doing anything else
	to the process.
	
	"""
	
	
	def __init__(self, group,target,name,args,kwargs):
		pass
	
	def Pipe(duplex):
		"""
		Returns a pair ``(conn1, conn2)`` of :class:`Connection` objects representing
		the ends of a pipe.
		
		If *duplex* is ``True`` (the default) then the pipe is bidirectional.  If
		*duplex* is ``False`` then the pipe is unidirectional: ``conn1`` can only be
		used for receiving messages and ``conn2`` can only be used for sending
		messages.
		
		
		"""
		pass
		
	


class Queue:


	"""
	Returns a process shared queue implemented using a pipe and a few
	locks/semaphores.  When a process first puts an item on the queue a feeder
	thread is started which transfers objects from a buffer into the pipe.
	
	The usual :exc:`Queue.Empty` and :exc:`Queue.Full` exceptions from the
	standard library's :mod:`Queue` module are raised to signal timeouts.
	
	:class:`Queue` implements all the methods of :class:`Queue.Queue` except for
	:meth:`~Queue.Queue.task_done` and :meth:`~Queue.Queue.join`.
	
	"""
	
	
	def __init__(self, maxsize):
		pass
	
	


class JoinableQueue:


	"""
	:class:`JoinableQueue`, a :class:`Queue` subclass, is a queue which
	additionally has :meth:`task_done` and :meth:`join` methods.
	
	"""
	
	
	def __init__(self, maxsize):
		pass
	
	def active_children():
		"""
		Return list of all live children of the current process.
		
		Calling this has the side affect of "joining" any processes which have
		already finished.
		
		"""
		pass
		
	def cpu_count():
		"""
		Return the number of CPUs in the system.  May raise
		:exc:`NotImplementedError`.
		
		"""
		pass
		
	def current_process():
		"""
		Return the :class:`Process` object corresponding to the current process.
		
		An analogue of :func:`threading.current_thread`.
		
		"""
		pass
		
	def freeze_support():
		"""
		Add support for when a program which uses :mod:`multiprocessing` has been
		frozen to produce a Windows executable.  (Has been tested with **py2exe**,
		**PyInstaller** and **cx_Freeze**.)
		
		One needs to call this function straight after the ``if __name__ ==
		'__main__'`` line of the main module.  For example::
		
		from multiprocessing import Process, freeze_support
		
		def f():
		print 'hello world!'
		
		if __name__ == '__main__':
		freeze_support()
		Process(target=f).start()
		
		If the ``freeze_support()`` line is omitted then trying to run the frozen
		executable will raise :exc:`RuntimeError`.
		
		If the module is being run normally by the Python interpreter then
		:func:`freeze_support` has no effect.
		
		"""
		pass
		
	def set_executable():
		"""
		Sets the path of the Python interpreter to use when starting a child process.
		(By default :data:`sys.executable` is used).  Embedders will probably need to
		do some thing like ::
		
		setExecutable(os.path.join(sys.exec_prefix, 'pythonw.exe'))
		
		before they can create child processes.  (Windows only)
		
		
		"""
		pass
		
	


class Connection:


	"""
	"""
	
	
	def __init__(self, ):
		pass
	
	


class BoundedSemaphore:


	"""
	A bounded semaphore object: a clone of :class:`threading.BoundedSemaphore`.
	
	(On Mac OS X, this is indistinguishable from :class:`Semaphore` because
	``sem_getvalue()`` is not implemented on that platform).
	
	"""
	
	
	def __init__(self, value):
		pass
	
	


class Condition:


	"""
	A condition variable: a clone of :class:`threading.Condition`.
	
	If *lock* is specified then it should be a :class:`Lock` or :class:`RLock`
	object from :mod:`multiprocessing`.
	
	"""
	
	
	def __init__(self, lock):
		pass
	
	


class Event:


	"""
	A clone of :class:`threading.Event`.
	This method returns the state of the internal semaphore on exit, so it
	will always return ``True`` except if a timeout is given and the operation
	times out.
	
	"""
	
	
	def __init__(self, ):
		pass
	
	


class Lock:


	"""
	A non-recursive lock object: a clone of :class:`threading.Lock`.
	
	"""
	
	
	def __init__(self, ):
		pass
	
	


class RLock:


	"""
	A recursive lock object: a clone of :class:`threading.RLock`.
	
	"""
	
	
	def __init__(self, ):
		pass
	
	


class Semaphore:


	"""
	A semaphore object: a clone of :class:`threading.Semaphore`.
	
	"""
	
	
	def __init__(self, value):
		pass
	
	def Value(typecode_or_type,args,lock):
		"""
		Return a :mod:`ctypes` object allocated from shared memory.  By default the
		return value is actually a synchronized wrapper for the object.
		
		*typecode_or_type* determines the type of the returned object: it is either a
		ctypes type or a one character typecode of the kind used by the :mod:`array`
		module.  *\*args* is passed on to the constructor for the type.
		
		If *lock* is ``True`` (the default) then a new lock object is created to
		synchronize access to the value.  If *lock* is a :class:`Lock` or
		:class:`RLock` object then that will be used to synchronize access to the
		value.  If *lock* is ``False`` then access to the returned object will not be
		automatically protected by a lock, so it will not necessarily be
		"process-safe".
		
		Note that *lock* is a keyword-only argument.
		
		"""
		pass
		
	def Array(typecode_or_type,size_or_initializer,,lock=True):
		"""
		Return a ctypes array allocated from shared memory.  By default the return
		value is actually a synchronized wrapper for the array.
		
		*typecode_or_type* determines the type of the elements of the returned array:
		it is either a ctypes type or a one character typecode of the kind used by
		the :mod:`array` module.  If *size_or_initializer* is an integer, then it
		determines the length of the array, and the array will be initially zeroed.
		Otherwise, *size_or_initializer* is a sequence which is used to initialize
		the array and whose length determines the length of the array.
		
		If *lock* is ``True`` (the default) then a new lock object is created to
		synchronize access to the value.  If *lock* is a :class:`Lock` or
		:class:`RLock` object then that will be used to synchronize access to the
		value.  If *lock* is ``False`` then access to the returned object will not be
		automatically protected by a lock, so it will not necessarily be
		"process-safe".
		
		Note that *lock* is a keyword only argument.
		
		Note that an array of :data:`ctypes.c_char` has *value* and *raw*
		attributes which allow one to use it to store and retrieve strings.
		
		
		The :mod:`multiprocessing.sharedctypes` module
		>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
		
		"""
		pass
		
	


