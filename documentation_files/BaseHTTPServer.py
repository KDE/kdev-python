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
	
	
	def __init__(self, ):
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
	
	
	def __init__(self, ):
		pass
	
	def handle(self, ):
		"""
		Calls :meth:`handle_one_request` once (or, if persistent connections are
		enabled, multiple times) to handle incoming HTTP requests. You should
		never need to override it; instead, implement appropriate :meth:`do_\*`
		methods.
		
		
		"""
		pass
		
	def handle_one_request(self, ):
		"""
		This method will parse and dispatch the request to the appropriate
		:meth:`do_\*` method.  You should never need to override it.
		
		
		"""
		pass
		
	def send_error(self, code,message):
		"""
		Sends and logs a complete error reply to the client. The numeric *code*
		specifies the HTTP error code, with *message* as optional, more specific text. A
		complete set of headers is sent, followed by text composed using the
		:attr:`error_message_format` class variable.
		
		
		"""
		pass
		
	def send_response(self, code,message):
		"""
		Sends a response header and logs the accepted request. The HTTP response
		line is sent, followed by *Server* and *Date* headers. The values for
		these two headers are picked up from the :meth:`version_string` and
		:meth:`date_time_string` methods, respectively.
		
		
		"""
		pass
		
	def send_header(self, keyword,value):
		"""
		Writes a specific HTTP header to the output stream. *keyword* should
		specify the header keyword, with *value* specifying its value.
		
		
		"""
		pass
		
	def end_headers(self, ):
		"""
		Sends a blank line, indicating the end of the HTTP headers in the
		response.
		
		
		"""
		pass
		
	def log_request(self, code,size):
		"""
		Logs an accepted (successful) request. *code* should specify the numeric
		HTTP code associated with the response. If a size of the response is
		available, then it should be passed as the *size* parameter.
		
		
		"""
		pass
		
	def log_error(self, more):
		"""
		Logs an error when a request cannot be fulfilled. By default, it passes
		the message to :meth:`log_message`, so it takes the same arguments
		(*format* and additional values).
		
		
		"""
		pass
		
	def log_message(self, format,more):
		"""
		Logs an arbitrary message to ``sys.stderr``. This is typically overridden
		to create custom error logging mechanisms. The *format* argument is a
		standard printf-style format string, where the additional arguments to
		:meth:`log_message` are applied as inputs to the formatting. The client
		address and current date and time are prefixed to every message logged.
		
		
		"""
		pass
		
	def version_string(self, ):
		"""
		Returns the server software's version string. This is a combination of the
		:attr:`server_version` and :attr:`sys_version` class variables.
		
		
		"""
		pass
		
	def date_time_string(self, timestamp):
		"""
		Returns the date and time given by *timestamp* (which must be in the
		format returned by :func:`time.time`), formatted for a message header. If
		*timestamp* is omitted, it uses the current date and time.
		
		The result looks like ``'Sun, 06 Nov 1994 08:49:37 GMT'``.
		
		"""
		pass
		
	def log_date_time_string(self, ):
		"""
		Returns the current date and time, formatted for logging.
		
		
		"""
		pass
		
	def address_string(self, ):
		"""
		Returns the client address, formatted for logging. A name lookup is
		performed on the client's IP address.
		
		
		More examples
		"""
		pass
		
	


