#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
""":synopsis: Basic XML-RPC server implementation.
"""
class SimpleXMLRPCServer:


	"""
	Create a new server instance.  This class provides methods for registration of
	functions that can be called by the XML-RPC protocol.  The *requestHandler*
	parameter should be a factory for request handler instances; it defaults to
	:class:`SimpleXMLRPCRequestHandler`.  The *addr* and *requestHandler* parameters
	are passed to the :class:`SocketServer.TCPServer` constructor.  If *logRequests*
	is true (the default), requests will be logged; setting this parameter to false
	will turn off logging.   The *allow_none* and *encoding* parameters are passed
	on to  :mod:`xmlrpclib` and control the XML-RPC responses that will be returned
	from the server. The *bind_and_activate* parameter controls whether
	:meth:`server_bind` and :meth:`server_activate` are called immediately by the
	constructor; it defaults to true. Setting it to false allows code to manipulate
	the *allow_reuse_address* class variable before the address is bound.
	
	"""
	
	
	def __init__(self, ):
		pass
	
	def register_function(self, function,name):
		"""
		Register a function that can respond to XML-RPC requests.  If *name* is given,
		it will be the method name associated with *function*, otherwise
		``function.__name__`` will be used.  *name* can be either a normal or Unicode
		string, and may contain characters not legal in Python identifiers, including
		the period character.
		
		
		"""
		pass
		
	def register_instance(self, instance,allow_dotted_names):
		"""
		Register an object which is used to expose method names which have not been
		registered using :meth:`register_function`.  If *instance* contains a
		:meth:`_dispatch` method, it is called with the requested method name and the
		parameters from the request.  Its API is ``def _dispatch(self, method, params)``
		(note that *params* does not represent a variable argument list).  If it calls
		an underlying function to perform its task, that function is called as
		``func(*params)``, expanding the parameter list. The return value from
		:meth:`_dispatch` is returned to the client as the result.  If *instance* does
		not have a :meth:`_dispatch` method, it is searched for an attribute matching
		the name of the requested method.
		
		If the optional *allow_dotted_names* argument is true and the instance does not
		have a :meth:`_dispatch` method, then if the requested method name contains
		periods, each component of the method name is searched for individually, with
		the effect that a simple hierarchical search is performed.  The value found from
		this search is then called with the parameters from the request, and the return
		value is passed back to the client.
		
		"""
		pass
		
	def register_introspection_functions(self, ):
		"""
		Registers the XML-RPC introspection functions ``system.listMethods``,
		``system.methodHelp`` and ``system.methodSignature``.
		
		"""
		pass
		
	def register_multicall_functions(self, ):
		"""
		Registers the XML-RPC multicall function system.multicall.
		
		
		"""
		pass
		
	


class CGIXMLRPCRequestHandler:


	"""
	Create a new instance to handle XML-RPC requests in a CGI environment.  The
	*allow_none* and *encoding* parameters are passed on to  :mod:`xmlrpclib` and
	control the XML-RPC responses that will be returned  from the server.
	
	"""
	
	
	def __init__(self, ):
		pass
	
	def register_function(self, function,name):
		"""
		Register a function that can respond to XML-RPC requests. If  *name* is given,
		it will be the method name associated with  function, otherwise
		*function.__name__* will be used. *name* can be either a normal or Unicode
		string, and may contain  characters not legal in Python identifiers, including
		the period character.
		
		
		"""
		pass
		
	def register_instance(self, instance):
		"""
		Register an object which is used to expose method names  which have not been
		registered using :meth:`register_function`. If  instance contains a
		:meth:`_dispatch` method, it is called with the  requested method name and the
		parameters from the  request; the return value is returned to the client as the
		result. If instance does not have a :meth:`_dispatch` method, it is searched
		for an attribute matching the name of the requested method; if  the requested
		method name contains periods, each  component of the method name is searched for
		individually,  with the effect that a simple hierarchical search is performed.
		The value found from this search is then called with the  parameters from the
		request, and the return value is passed  back to the client.
		
		
		"""
		pass
		
	def register_introspection_functions(self, ):
		"""
		Register the XML-RPC introspection functions  ``system.listMethods``,
		``system.methodHelp`` and  ``system.methodSignature``.
		
		
		"""
		pass
		
	def register_multicall_functions(self, ):
		"""
		Register the XML-RPC multicall function ``system.multicall``.
		
		
		"""
		pass
		
	


class SimpleXMLRPCRequestHandler:


	"""
	Create a new request handler instance.  This request handler supports ``POST``
	requests and modifies logging so that the *logRequests* parameter to the
	:class:`SimpleXMLRPCServer` constructor parameter is honored.
	
	
	.. impleXMLRPCServer Objects
	--------------------------
	
	The :class:`SimpleXMLRPCServer` class is based on
	:class:`SocketServer.TCPServer` and provides a means of creating simple, stand
	alone XML-RPC servers.
	
	
	"""
	
	
	def __init__(self, ):
		pass
	
	


