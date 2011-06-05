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
	of the form 'Process-N\ :sub:`1`:N\ :sub:`2`:more:N\ :sub:`k`' where N\
	:sub:`1`,N\ :sub:`2`,more,N\ :sub:`k` is a sequence of integers whose length
	is determined by the *generation* of the process.  *args* is the argument
	tuple for the target invocation.  *kwargs* is a dictionary of keyword
	arguments for the target invocation.  By default, no arguments are passed to
	*target*.
	
	If a subclass overrides the constructor, it must make sure it invokes the
	base class constructor (:meth:`Process.__init__`) before doing anything else
	to the process.
	
	"""
	
	
	def __init__(self, ):
		pass
	
	def run(self, ):
		"""
		Method representing the process's activity.
		
		You may override this method in a subclass.  The standard :meth:`run`
		method invokes the callable object passed to the object's constructor as
		the target argument, if any, with sequential and keyword arguments taken
		from the *args* and *kwargs* arguments, respectively.
		
		"""
		pass
		
	def start(self, ):
		"""
		Start the process's activity.
		
		This must be called at most once per process object.  It arranges for the
		object's :meth:`run` method to be invoked in a separate process.
		
		"""
		pass
		
	def join(self, timeout):
		"""
		Block the calling thread until the process whose :meth:`join` method is
		called terminates or until the optional timeout occurs.
		
		If *timeout* is ``None`` then there is no timeout.
		
		A process can be joined many times.
		
		A process cannot join itself because this would cause a deadlock.  It is
		an error to attempt to join a process before it has been started.
		
		"""
		pass
		
	def is_alive(self, ):
		"""
		Return whether the process is alive.
		
		Roughly, a process object is alive from the moment the :meth:`start`
		method returns until the child process terminates.
		
		"""
		pass
		
	def terminate(self, ):
		"""
		Terminate the process.  On Unix this is done using the ``SIGTERM`` signal;
		on Windows :cfunc:`TerminateProcess` is used.  Note that exit handlers and
		finally clauses, etc., will not be executed.
		
		Note that descendant processes of the process will *not* be terminated --
		they will simply become orphaned.
		
		"""
		pass
		
	def Pipe(self, duplex):
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
	
	
	def __init__(self, ):
		pass
	
	def qsize(self, ):
		"""
		Return the approximate size of the queue.  Because of
		multithreading/multiprocessing semantics, this number is not reliable.
		
		Note that this may raise :exc:`NotImplementedError` on Unix platforms like
		Mac OS X where ``sem_getvalue()`` is not implemented.
		
		"""
		pass
		
	def empty(self, ):
		"""
		Return ``True`` if the queue is empty, ``False`` otherwise.  Because of
		multithreading/multiprocessing semantics, this is not reliable.
		
		"""
		pass
		
	def full(self, ):
		"""
		Return ``True`` if the queue is full, ``False`` otherwise.  Because of
		multithreading/multiprocessing semantics, this is not reliable.
		
		"""
		pass
		
	def put(self, item,block,timeout):
		"""
		Put item into the queue.  If the optional argument *block* is ``True``
		(the default) and *timeout* is ``None`` (the default), block if necessary until
		a free slot is available.  If *timeout* is a positive number, it blocks at
		most *timeout* seconds and raises the :exc:`Queue.Full` exception if no
		free slot was available within that time.  Otherwise (*block* is
		``False``), put an item on the queue if a free slot is immediately
		available, else raise the :exc:`Queue.Full` exception (*timeout* is
		ignored in that case).
		
		"""
		pass
		
	def put_nowait(self, item):
		"""
		Equivalent to ``put(item, False)``.
		
		"""
		pass
		
	def get(self, block,timeout):
		"""
		Remove and return an item from the queue.  If optional args *block* is
		``True`` (the default) and *timeout* is ``None`` (the default), block if
		necessary until an item is available.  If *timeout* is a positive number,
		it blocks at most *timeout* seconds and raises the :exc:`Queue.Empty`
		exception if no item was available within that time.  Otherwise (block is
		``False``), return an item if one is immediately available, else raise the
		:exc:`Queue.Empty` exception (*timeout* is ignored in that case).
		
		"""
		pass
		
	def get_nowait(self, ):
		"""get_no_wait()
		
		Equivalent to ``get(False)``.
		
		:class:`multiprocessing.Queue` has a few additional methods not found in
		:class:`Queue.Queue`.  These methods are usually unnecessary for most
		code:
		
		"""
		pass
		
	def close(self, ):
		"""
		Indicate that no more data will be put on this queue by the current
		process.  The background thread will quit once it has flushed all buffered
		data to the pipe.  This is called automatically when the queue is garbage
		collected.
		
		"""
		pass
		
	def join_thread(self, ):
		"""
		Join the background thread.  This can only be used after :meth:`close` has
		been called.  It blocks until the background thread exits, ensuring that
		all data in the buffer has been flushed to the pipe.
		
		By default if a process is not the creator of the queue then on exit it
		will attempt to join the queue's background thread.  The process can call
		:meth:`cancel_join_thread` to make :meth:`join_thread` do nothing.
		
		"""
		pass
		
	def cancel_join_thread(self, ):
		"""
		Prevent :meth:`join_thread` from blocking.  In particular, this prevents
		the background thread from being joined automatically when the process
		exits -- see :meth:`join_thread`.
		
		
		"""
		pass
		
	


class JoinableQueue:


	"""
	:class:`JoinableQueue`, a :class:`Queue` subclass, is a queue which
	additionally has :meth:`task_done` and :meth:`join` methods.
	
	"""
	
	
	def __init__(self, ):
		pass
	
	def task_done(self, ):
		"""
		Indicate that a formerly enqueued task is complete. Used by queue consumer
		threads.  For each :meth:`~Queue.get` used to fetch a task, a subsequent
		call to :meth:`task_done` tells the queue that the processing on the task
		is complete.
		
		If a :meth:`~Queue.join` is currently blocking, it will resume when all
		items have been processed (meaning that a :meth:`task_done` call was
		received for every item that had been :meth:`~Queue.put` into the queue).
		
		Raises a :exc:`ValueError` if called more times than there were items
		placed in the queue.
		
		
		"""
		pass
		
	def join(self, ):
		"""
		Block until all items in the queue have been gotten and processed.
		
		The count of unfinished tasks goes up whenever an item is added to the
		queue.  The count goes down whenever a consumer thread calls
		:meth:`task_done` to indicate that the item was retrieved and all work on
		it is complete.  When the count of unfinished tasks drops to zero,
		:meth:`~Queue.join` unblocks.
		
		
		Miscellaneous
		"""
		pass
		
	def active_children(self, ):
		"""
		Return list of all live children of the current process.
		
		Calling this has the side affect of "joining" any processes which have
		already finished.
		
		"""
		pass
		
	def cpu_count(self, ):
		"""
		Return the number of CPUs in the system.  May raise
		:exc:`NotImplementedError`.
		
		"""
		pass
		
	def current_process(self, ):
		"""
		Return the :class:`Process` object corresponding to the current process.
		
		An analogue of :func:`threading.current_thread`.
		
		"""
		pass
		
	def freeze_support(self, ):
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
		
	def set_executable(self, ):
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
	
	def send(self, obj):
		"""
		Send an object to the other end of the connection which should be read
		using :meth:`recv`.
		
		The object must be picklable.  Very large pickles (approximately 32 MB+,
		though it depends on the OS) may raise a ValueError exception.
		
		"""
		pass
		
	def recv(self, ):
		"""
		Return an object sent from the other end of the connection using
		:meth:`send`.  Raises :exc:`EOFError` if there is nothing left to receive
		and the other end was closed.
		
		"""
		pass
		
	def fileno(self, ):
		"""
		Returns the file descriptor or handle used by the connection.
		
		"""
		pass
		
	def close(self, ):
		"""
		Close the connection.
		
		This is called automatically when the connection is garbage collected.
		
		"""
		pass
		
	def poll(self, timeout):
		"""
		Return whether there is any data available to be read.
		
		If *timeout* is not specified then it will return immediately.  If
		*timeout* is a number then this specifies the maximum time in seconds to
		block.  If *timeout* is ``None`` then an infinite timeout is used.
		
		"""
		pass
		
	def send_bytes(self, buffer,offset,size):
		"""
		Send byte data from an object supporting the buffer interface as a
		complete message.
		
		If *offset* is given then data is read from that position in *buffer*.  If
		*size* is given then that many bytes will be read from buffer.  Very large
		buffers (approximately 32 MB+, though it depends on the OS) may raise a
		ValueError exception
		
		"""
		pass
		
	def recv_bytes(self, maxlength):
		"""
		Return a complete message of byte data sent from the other end of the
		connection as a string.  Raises :exc:`EOFError` if there is nothing left
		to receive and the other end has closed.
		
		If *maxlength* is specified and the message is longer than *maxlength*
		then :exc:`IOError` is raised and the connection will no longer be
		readable.
		
		"""
		pass
		
	def recv_bytes_into(self, buffer,offset):
		"""
		Read into *buffer* a complete message of byte data sent from the other end
		of the connection and return the number of bytes in the message.  Raises
		:exc:`EOFError` if there is nothing left to receive and the other end was
		closed.
		
		*buffer* must be an object satisfying the writable buffer interface.  If
		*offset* is given then the message will be written into the buffer from
		that position.  Offset must be a non-negative integer less than the
		length of *buffer* (in bytes).
		
		If the buffer is too short then a :exc:`BufferTooShort` exception is
		raised and the complete message is available as ``e.args[0]`` where ``e``
		is the exception instance.
		
		
		For example:
		"""
		pass
		
	


class BoundedSemaphore:


	"""
	A bounded semaphore object: a clone of :class:`threading.BoundedSemaphore`.
	
	(On Mac OS X, this is indistinguishable from :class:`Semaphore` because
	``sem_getvalue()`` is not implemented on that platform).
	
	"""
	
	
	def __init__(self, ):
		pass
	
	


class Condition:


	"""
	A condition variable: a clone of :class:`threading.Condition`.
	
	If *lock* is specified then it should be a :class:`Lock` or :class:`RLock`
	object from :mod:`multiprocessing`.
	
	"""
	
	
	def __init__(self, ):
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
	
	
	def __init__(self, ):
		pass
	
	def Value(self, typecode_or_type,args,lock):
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
		
	def Array(self, typecode_or_type,size_or_initializer,more,lock=True):
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
		
	


