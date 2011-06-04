#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
""":synopsis: Create pools of processes.

One can create a pool of processes which will carry out tasks submitted to it
with the :class:`Pool` class.

"""
class multiprocessing:


	"""
	A process pool object which controls a pool of worker processes to which jobs
	can be submitted.  It supports asynchronous results with timeouts and
	callbacks and has a parallel map implementation.
	
	*processes* is the number of worker processes to use.  If *processes* is
	``None`` then the number returned by :func:`cpu_count` is used.  If
	*initializer* is not ``None`` then each worker process will call
	``initializer(*initargs)`` when it starts.
	
	"""
	
	
	def __init__(self, ):
		pass
	
	


class AsyncResult:


	"""
	The class of the result returned by :meth:`Pool.apply_async` and
	:meth:`Pool.map_async`.
	
	"""
	
	
	def __init__(self, ):
		pass
	
	def get(self, timeout):
		"""
		Return the result when it arrives.  If *timeout* is not ``None`` and the
		result does not arrive within *timeout* seconds then
		:exc:`multiprocessing.TimeoutError` is raised.  If the remote call raised
		an exception then that exception will be reraised by :meth:`get`.
		
		"""
		pass
		
	def wait(self, timeout):
		"""
		Wait until the result is available or until *timeout* seconds pass.
		
		"""
		pass
		
	def ready(self, ):
		"""
		Return whether the call has completed.
		
		"""
		pass
		
	def successful(self, ):
		"""
		Return whether the call completed without raising an exception.  Will
		raise :exc:`AssertionError` if the result is not ready.
		
		The following example demonstrates the use of a pool::
		"""
		pass
		
	


