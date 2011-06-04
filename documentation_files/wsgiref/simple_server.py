#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
""":synopsis: A simple WSGI HTTP server.


This module implements a simple HTTP server (based on :mod:`BaseHTTPServer`)
that serves WSGI applications.  Each server instance serves a single WSGI
application on a given host and port.  If you want to serve multiple
applications on a single host and port, you should create a WSGI application
that parses ``PATH_INFO`` to select which application to invoke for each
request.  (E.g., using the :func:`shift_path_info` function from
:mod:`wsgiref.util`.)


"""
class WSGIServer:


	"""
	Create a :class:`WSGIServer` instance.  *server_address* should be a
	``(host,port)`` tuple, and *RequestHandlerClass* should be the subclass of
	:class:`BaseHTTPServer.BaseHTTPRequestHandler` that will be used to process
	requests.
	
	You do not normally need to call this constructor, as the :func:`make_server`
	function can handle all the details for you.
	
	:class:`WSGIServer` is a subclass of :class:`BaseHTTPServer.HTTPServer`, so all
	of its methods (such as :meth:`serve_forever` and :meth:`handle_request`) are
	available. :class:`WSGIServer` also provides these WSGI-specific methods:
	
	
	"""
	
	
	def __init__(self, server_address,RequestHandlerClass):
		pass
	
	


class WSGIRequestHandler:


	"""
	Create an HTTP handler for the given *request* (i.e. a socket), *client_address*
	(a ``(host,port)`` tuple), and *server* (:class:`WSGIServer` instance).
	
	You do not need to create instances of this class directly; they are
	automatically created as needed by :class:`WSGIServer` objects.  You can,
	however, subclass this class and supply it as a *handler_class* to the
	:func:`make_server` function.  Some possibly relevant methods for overriding in
	subclasses:
	
	
	"""
	
	
	def __init__(self, request,client_address,server):
		pass
	
	


