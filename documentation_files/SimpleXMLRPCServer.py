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
	
	
	def __init__(self, addr,requestHandler,logRequests,allow_none,encoding,bind_and_activate):
		pass
	
	


class CGIXMLRPCRequestHandler:


	"""
	Create a new instance to handle XML-RPC requests in a CGI environment.  The
	*allow_none* and *encoding* parameters are passed on to  :mod:`xmlrpclib` and
	control the XML-RPC responses that will be returned  from the server.
	
	"""
	
	
	def __init__(self, allow_none,encoding):
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
	
	


