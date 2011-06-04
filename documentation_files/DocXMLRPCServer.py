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
	
	
	def __init__(self, ):
		pass
	
	def set_server_title(self, server_title):
		"""
		Set the title used in the generated HTML documentation. This title will be used
		inside the HTML "title" element.
		
		
		"""
		pass
		
	def set_server_name(self, server_name):
		"""
		Set the name used in the generated HTML documentation. This name will appear at
		the top of the generated documentation inside a "h1" element.
		
		
		"""
		pass
		
	def set_server_documentation(self, server_documentation):
		"""
		Set the description used in the generated HTML documentation. This description
		will appear as a paragraph, below the server name, in the documentation.
		
		
		DocCGIXMLRPCRequestHandler
		--------------------------
		
		The :class:`DocCGIXMLRPCRequestHandler` class is derived from
		:class:`SimpleXMLRPCServer.CGIXMLRPCRequestHandler` and provides a means of
		creating self-documenting, XML-RPC CGI scripts. HTTP POST requests are handled
		as XML-RPC method calls. HTTP GET requests are handled by generating pydoc-style
		HTML documentation. This allows a server to provide its own web-based
		documentation.
		
		
		"""
		pass
		
	


class DocCGIXMLRPCRequestHandler:


	"""
	Create a new instance to handle XML-RPC requests in a CGI environment.
	
	
	"""
	
	
	def __init__(self, ):
		pass
	
	def set_server_title(self, server_title):
		"""
		Set the title used in the generated HTML documentation. This title will be used
		inside the HTML "title" element.
		
		
		"""
		pass
		
	def set_server_name(self, server_name):
		"""
		Set the name used in the generated HTML documentation. This name will appear at
		the top of the generated documentation inside a "h1" element.
		
		
		"""
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
	
	


