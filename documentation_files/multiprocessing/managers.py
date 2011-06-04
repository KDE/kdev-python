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
	
	
	def __init__(self, ):
		pass
	
	def start(self, initializer,initargs):
		"""
		Start a subprocess to start the manager.  If *initializer* is not ``None``
		then the subprocess will call ``initializer(*initargs)`` when it starts.
		
		"""
		pass
		
	def get_server(self, ):
		"""
		Returns a :class:`Server` object which represents the actual server under
		the control of the Manager. The :class:`Server` object supports the
		:meth:`serve_forever` method::
		
		>>> from multiprocessing.managers import BaseManager
		>>> manager = BaseManager(address=('', 50000), authkey='abc')
		>>> server = manager.get_server()
		>>> server.serve_forever()
		
		:class:`Server` additionally has an :attr:`address` attribute.
		
		"""
		pass
		
	def connect(self, ):
		"""
		Connect a local manager object to a remote manager process::
		
		>>> from multiprocessing.managers import BaseManager
		>>> m = BaseManager(address=('127.0.0.1', 5000), authkey='abc')
		>>> m.connect()
		
		"""
		pass
		
	def shutdown(self, ):
		"""
		Stop the process used by the manager.  This is only available if
		:meth:`start` has been used to start the server process.
		
		This can be called multiple times.
		
		"""
		pass
		
	def register(self, typeid,callable,proxytype,exposed,method_to_typeid,create_method):
		"""
		A classmethod which can be used for registering a type or callable with
		the manager class.
		
		*typeid* is a "type identifier" which is used to identify a particular
		type of shared object.  This must be a string.
		
		*callable* is a callable used for creating objects for this type
		identifier.  If a manager instance will be created using the
		:meth:`from_address` classmethod or if the *create_method* argument is
		``False`` then this can be left as ``None``.
		
		*proxytype* is a subclass of :class:`BaseProxy` which is used to create
		proxies for shared objects with this *typeid*.  If ``None`` then a proxy
		class is created automatically.
		
		*exposed* is used to specify a sequence of method names which proxies for
		this typeid should be allowed to access using
		:meth:`BaseProxy._callMethod`.  (If *exposed* is ``None`` then
		:attr:`proxytype._exposed_` is used instead if it exists.)  In the case
		where no exposed list is specified, all "public methods" of the shared
		object will be accessible.  (Here a "public method" means any attribute
		which has a :meth:`__call__` method and whose name does not begin with
		``'_'``.)
		
		*method_to_typeid* is a mapping used to specify the return type of those
		exposed methods which should return a proxy.  It maps method names to
		typeid strings.  (If *method_to_typeid* is ``None`` then
		:attr:`proxytype._method_to_typeid_` is used instead if it exists.)  If a
		method's name is not a key of this mapping or if the mapping is ``None``
		then the object returned by the method will be copied by value.
		
		*create_method* determines whether a method should be created with name
		*typeid* which can be used to tell the server process to create a new
		shared object and return a proxy for it.  By default it is ``True``.
		
		:class:`BaseManager` instances also have one read-only property:
		
		"""
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
	
	def BoundedSemaphore(self, value):
		"""
		Create a shared :class:`threading.BoundedSemaphore` object and return a
		proxy for it.
		
		"""
		pass
		
	def Condition(self, lock):
		"""
		Create a shared :class:`threading.Condition` object and return a proxy for
		it.
		
		If *lock* is supplied then it should be a proxy for a
		:class:`threading.Lock` or :class:`threading.RLock` object.
		
		"""
		pass
		
	def Event(self, ):
		"""
		Create a shared :class:`threading.Event` object and return a proxy for it.
		
		"""
		pass
		
	def Lock(self, ):
		"""
		Create a shared :class:`threading.Lock` object and return a proxy for it.
		
		"""
		pass
		
	def Namespace(self, ):
		"""
		Create a shared :class:`Namespace` object and return a proxy for it.
		
		"""
		pass
		
	def Queue(self, maxsize):
		"""
		Create a shared :class:`Queue.Queue` object and return a proxy for it.
		
		"""
		pass
		
	def RLock(self, ):
		"""
		Create a shared :class:`threading.RLock` object and return a proxy for it.
		
		"""
		pass
		
	def Semaphore(self, value):
		"""
		Create a shared :class:`threading.Semaphore` object and return a proxy for
		it.
		
		"""
		pass
		
	def Array(self, typecode,sequence):
		"""
		Create an array and return a proxy for it.
		
		"""
		pass
		
	def Value(self, typecode,value):
		"""
		Create an object with a writable ``value`` attribute and return a proxy
		for it.
		
		"""
		pass
		
	def dict(self, ):
		"""dict(mapping)
		dict(sequence)
		
		Create a shared ``dict`` object and return a proxy for it.
		
		"""
		pass
		
	def list(self, ):
		"""list(sequence)
		
		Create a shared ``list`` object and return a proxy for it.
		
		"""
		pass
		
	


class BaseProxy:


	"""
	Proxy objects are instances of subclasses of :class:`BaseProxy`.
	
	"""
	
	
	def __init__(self, ):
		pass
	
	def _callmethod(self, methodname,args,kwds):
		"""
		Call and return the result of a method of the proxy's referent.
		
		If ``proxy`` is a proxy whose referent is ``obj`` then the expression ::
		
		proxy._callmethod(methodname, args, kwds)
		
		will evaluate the expression ::
		
		getattr(obj, methodname)(*args, **kwds)
		
		in the manager's process.
		
		The returned value will be a copy of the result of the call or a proxy to
		a new shared object -- see documentation for the *method_to_typeid*
		argument of :meth:`BaseManager.register`.
		
		If an exception is raised by the call, then then is re-raised by
		:meth:`_callmethod`.  If some other exception is raised in the manager's
		process then this is converted into a :exc:`RemoteError` exception and is
		raised by :meth:`_callmethod`.
		
		Note in particular that an exception will be raised if *methodname* has
		not been *exposed*
		
		An example of the usage of :meth:`_callmethod`:
		
		"""
		pass
		
	def _getvalue(self, ):
		"""
		Return a copy of the referent.
		
		If the referent is unpicklable then this will raise an exception.
		
		"""
		pass
		
	def __repr__(self, ():
		"""
		Return a representation of the proxy object.
		
		"""
		pass
		
	def __str__(self, ():
		"""
		Return the representation of the referent.
		
		
		Cleanup
		"""
		pass
		
	


