#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
""":synopsis: Share data between process with shared objects.

Manager processes will be shutdown as soon as they are garbage collected or
their parent process exits.  The manager classes are defined in the
:mod:`multiprocessing.managers` module:

"""
class BaseManager:


	"""
	Create a BaseManager object.
	
	Once created one should call :meth:`start` or ``get_server().serve_forever()`` to ensure
	that the manager object refers to a started manager process.
	
	*address* is the address on which the manager process listens for new
	connections.  If *address* is ``None`` then an arbitrary one is chosen.
	
	*authkey* is the authentication key which will be used to check the validity
	of incoming connections to the server process.  If *authkey* is ``None`` then
	``current_process().authkey``.  Otherwise *authkey* is used and it
	must be a string.
	
	"""
	
	
	def __init__(self, address,authkey):
		pass
	
	


class SyncManager:


	"""
	A subclass of :class:`BaseManager` which can be used for the synchronization
	of processes.  Objects of this type are returned by
	:func:`multiprocessing.Manager`.
	
	It also supports creation of shared lists and dictionaries.
	
	"""
	
	
	def __init__(self, ):
		pass
	
	


class BaseProxy:


	"""
	Proxy objects are instances of subclasses of :class:`BaseProxy`.
	
	"""
	
	
	def __init__(self, ):
		pass
	
	


