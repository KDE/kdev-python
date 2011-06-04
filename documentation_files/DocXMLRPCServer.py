#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
""":synopsis: Self-documenting XML-RPC server implementation.
"""
class DocXMLRPCServer:


	"""
	Create a new server instance. All parameters have the same meaning as for
	:class:`SimpleXMLRPCServer.SimpleXMLRPCServer`; *requestHandler* defaults to
	:class:`DocXMLRPCRequestHandler`.
	
	
	"""
	
	
	def __init__(self, addr,requestHandler,logRequests,allow_none,encoding,bind_and_activate):
		pass
	
	


class DocCGIXMLRPCRequestHandler:


	"""
	Create a new instance to handle XML-RPC requests in a CGI environment.
	
	
	"""
	
	
	def __init__(self, ):
		pass
	
	


class DocXMLRPCRequestHandler:


	"""
	Create a new request handler instance. This request handler supports XML-RPC
	POST requests, documentation GET requests, and modifies logging so that the
	*logRequests* parameter to the :class:`DocXMLRPCServer` constructor parameter is
	honored.
	
	
	.. ocXMLRPCServer Objects
	-----------------------
	
	The :class:`DocXMLRPCServer` class is derived from
	:class:`SimpleXMLRPCServer.SimpleXMLRPCServer` and provides a means of creating
	self-documenting, stand alone XML-RPC servers. HTTP POST requests are handled as
	XML-RPC method calls. HTTP GET requests are handled by generating pydoc-style
	HTML documentation. This allows a server to provide its own web-based
	documentation.
	
	
	"""
	
	
	def __init__(self, ):
		pass
	
	


