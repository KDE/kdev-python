#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
""":synopsis: Basic HTTP server (base class for SimpleHTTPServer and CGIHTTPServer).

"""
class HTTPServer:


	"""
	This class builds on the :class:`TCPServer` class by storing the server
	address as instance variables named :attr:`server_name` and
	:attr:`server_port`. The server is accessible by the handler, typically
	through the handler's :attr:`server` instance variable.
	
	
	"""
	
	
	def __init__(self, server_address,RequestHandlerClass):
		pass
	
	


class BaseHTTPRequestHandler:


	"""
	This class is used to handle the HTTP requests that arrive at the server. By
	itself, it cannot respond to any actual HTTP requests; it must be subclassed
	to handle each request method (e.g. GET or
	POST). :class:`BaseHTTPRequestHandler` provides a number of class and
	instance variables, and methods for use by subclasses.
	
	The handler will parse the request and the headers, then call a method
	specific to the request type. The method name is constructed from the
	request. For example, for the request method ``SPAM``, the :meth:`do_SPAM`
	method will be called with no arguments. All of the relevant information is
	stored in instance variables of the handler.  Subclasses should not need to
	override or extend the :meth:`__init__` method.
	
	:class:`BaseHTTPRequestHandler` has the following instance variables:
	
	
	"""
	
	
	def __init__(self, request,client_address,server):
		pass
	
	


