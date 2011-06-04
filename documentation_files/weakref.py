#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
""":synopsis: Support for weak references and weak dictionaries.
"""
class ref:


	"""
	Return a weak reference to *object*.  The original object can be retrieved by
	calling the reference object if the referent is still alive; if the referent is
	no longer alive, calling the reference object will cause :const:`None` to be
	returned.  If *callback* is provided and not :const:`None`, and the returned
	weakref object is still alive, the callback will be called when the object is
	about to be finalized; the weak reference object will be passed as the only
	parameter to the callback; the referent will no longer be available.
	
	It is allowable for many weak references to be constructed for the same object.
	Callbacks registered for each weak reference will be called from the most
	recently registered callback to the oldest registered callback.
	
	Exceptions raised by the callback will be noted on the standard error output,
	but cannot be propagated; they are handled in exactly the same way as exceptions
	raised from an object's :meth:`__del__` method.
	
	Weak references are :term:`hashable` if the *object* is hashable.  They will maintain
	their hash value even after the *object* was deleted.  If :func:`hash` is called
	the first time only after the *object* was deleted, the call will raise
	:exc:`TypeError`.
	
	Weak references support tests for equality, but not ordering.  If the referents
	are still alive, two references have the same equality relationship as their
	referents (regardless of the *callback*).  If either referent has been deleted,
	the references are equal only if the reference objects are the same object.
	
	"""
	
	
	def __init__(self, ):
		pass
	
	def proxy(self, object,callback):
		"""
		Return a proxy to *object* which uses a weak reference.  This supports use of
		the proxy in most contexts instead of requiring the explicit dereferencing used
		with weak reference objects.  The returned object will have a type of either
		``ProxyType`` or ``CallableProxyType``, depending on whether *object* is
		callable.  Proxy objects are not :term:`hashable` regardless of the referent; this
		avoids a number of problems related to their fundamentally mutable nature, and
		prevent their use as dictionary keys.  *callback* is the same as the parameter
		of the same name to the :func:`ref` function.
		
		
		"""
		pass
		
	def getweakrefcount(self, object):
		"""
		Return the number of weak references and proxies which refer to *object*.
		
		
		"""
		pass
		
	def getweakrefs(self, object):
		"""
		Return a list of all weak reference and proxy objects which refer to *object*.
		
		
		"""
		pass
		
	


class WeakKeyDictionary:


	"""
	Mapping class that references keys weakly.  Entries in the dictionary will be
	discarded when there is no longer a strong reference to the key.  This can be
	used to associate additional data with an object owned by other parts of an
	application without adding attributes to those objects.  This can be especially
	useful with objects that override attribute accesses.
	
	"""
	
	
	def __init__(self, ):
		pass
	
	def iterkeyrefs(self, ):
		"""
		Return an :term:`iterator` that yields the weak references to the keys.
		
		"""
		pass
		
	def keyrefs(self, ):
		"""
		Return a list of weak references to the keys.
		
		"""
		pass
		
	


class WeakValueDictionary:


	"""
	Mapping class that references values weakly.  Entries in the dictionary will be
	discarded when no strong reference to the value exists any more.
	
	"""
	
	
	def __init__(self, ):
		pass
	
	def itervaluerefs(self, ):
		"""
		Return an :term:`iterator` that yields the weak references to the values.
		
		"""
		pass
		
	def valuerefs(self, ):
		"""
		Return a list of weak references to the values.
		
		"""
		pass
		
	


class WeakSet:


	"""
	Set class that keeps weak references to its elements.  An element will be
	discarded when no strong reference to it exists any more.
	
	"""
	
	
	def __init__(self, ):
		pass
	
	"""
	The type object for weak references objects.
	
	
	"""
	ReferenceType = None
	"""
	The type object for proxies of objects which are not callable.
	
	
	"""
	ProxyType = None
	"""
	The type object for proxies of callable objects.
	
	
	"""
	CallableProxyType = None
	"""
	Sequence containing all the type objects for proxies.  This can make it simpler
	to test if an object is a proxy without being dependent on naming both proxy
	types.
	
	
	"""
	ProxyTypes = None
	


