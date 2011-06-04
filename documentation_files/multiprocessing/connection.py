#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
""":synopsis: API for dealing with sockets.

Usually message passing between processes is done using queues or by using
:class:`Connection` objects returned by :func:`Pipe`.

However, the :mod:`multiprocessing.connection` module allows some extra
flexibility.  It basically gives a high level message oriented API for dealing
with sockets or Windows named pipes, and also has support for *digest
authentication* using the :mod:`hmac` module.


"""
class Listener:


	"""
	A wrapper for a bound socket or Windows named pipe which is 'listening' for
	connections.
	
	*address* is the address to be used by the bound socket or named pipe of the
	listener object.
	
	"""
	
	
	def __init__(self, ):
		pass
	
	def accept(self, ):
		"""
		Accept a connection on the bound socket or named pipe of the listener
		object and return a :class:`Connection` object.  If authentication is
		attempted and fails, then :exc:`AuthenticationError` is raised.
		
		"""
		pass
		
	def close(self, ):
		"""
		Close the bound socket or named pipe of the listener object.  This is
		called automatically when the listener is garbage collected.  However it
		is advisable to call it explicitly.
		
		Listener objects have the following read-only properties:
		
		"""
		pass
		
	def get_logger(self, ):
		"""
		Returns the logger used by :mod:`multiprocessing`.  If necessary, a new one
		will be created.
		
		When first created the logger has level :data:`logging.NOTSET` and no
		default handler. Messages sent to this logger will not by default propagate
		to the root logger.
		
		Note that on Windows child processes will only inherit the level of the
		parent process's logger -- any other customization of the logger will not be
		inherited.
		
		"""
		pass
		
	def log_to_stderr(self, ):
		"""
		This function performs a call to :func:`get_logger` but in addition to
		returning the logger created by get_logger, it adds a handler which sends
		output to :data:`sys.stderr` using format
		``'[%(levelname)s/%(processName)s] %(message)s'``.
		
		Below is an example session with logging turned on::
		
		>>> import multiprocessing, logging
		>>> logger = multiprocessing.log_to_stderr()
		>>> logger.setLevel(logging.INFO)
		>>> logger.warning('doomed')
		[WARNING/MainProcess] doomed
		>>> m = multiprocessing.Manager()
		[INFO/SyncManager-*more] child process calling self.run()
		[INFO/SyncManager-*more] created temp directory /*more/pymp-*more
		[INFO/SyncManager-*more] manager serving at '/*more/listener-*more'
		>>> del m
		[INFO/MainProcess] sending shutdown message to manager
		[INFO/SyncManager-*more] manager exiting with exitcode 0
		
		In addition to having these two logging functions, the multiprocessing also
		exposes two additional logging level attributes. These are  :const:`SUBWARNING`
		and :const:`SUBDEBUG`. The table below illustrates where theses fit in the
		normal level hierarchy.
		
		+----------------+----------------+
		| Level          | Numeric value  |
		+================+================+
		| ``SUBWARNING`` | 25             |
		+----------------+----------------+
		| ``SUBDEBUG``   | 5              |
		+----------------+----------------+
		
		For a full table of logging levels, see the :mod:`logging` module.
		
		These additional logging levels are used primarily for certain debug messages
		within the multiprocessing module. Below is the same example as above, except
		with :const:`SUBDEBUG` enabled::
		
		>>> import multiprocessing, logging
		>>> logger = multiprocessing.log_to_stderr()
		>>> logger.setLevel(multiprocessing.SUBDEBUG)
		>>> logger.warning('doomed')
		[WARNING/MainProcess] doomed
		>>> m = multiprocessing.Manager()
		[INFO/SyncManager-*more] child process calling self.run()
		[INFO/SyncManager-*more] created temp directory /*more/pymp-*more
		[INFO/SyncManager-*more] manager serving at '/*more/pymp-djGBXN/listener-*more'
		>>> del m
		[SUBDEBUG/MainProcess] finalizer calling *more
		[INFO/MainProcess] sending shutdown message to manager
		[DEBUG/SyncManager-*more] manager received shutdown message
		[SUBDEBUG/SyncManager-*more] calling <Finalize object, callback=unlink, *more
		[SUBDEBUG/SyncManager-*more] finalizer calling <built-in function unlink> *more
		[SUBDEBUG/SyncManager-*more] calling <Finalize object, dead>
		[SUBDEBUG/SyncManager-*more] finalizer calling <function rmtree at 0x5aa730> *more
		[INFO/SyncManager-*more] manager exiting with exitcode 0
		
		The :mod:`multiprocessing.dummy` module
		~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
		
		"""
		pass
		
	


