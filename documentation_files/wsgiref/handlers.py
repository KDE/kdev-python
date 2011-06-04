#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
""":synopsis: WSGI server/gateway base classes.


This module provides base handler classes for implementing WSGI servers and
gateways.  These base classes handle most of the work of communicating with a
WSGI application, as long as they are given a CGI-like environment, along with
input, output, and error streams.


"""
class CGIHandler:


	"""
	CGI-based invocation via ``sys.stdin``, ``sys.stdout``, ``sys.stderr`` and
	``os.environ``.  This is useful when you have a WSGI application and want to run
	it as a CGI script.  Simply invoke ``CGIHandler().run(app)``, where ``app`` is
	the WSGI application object you wish to invoke.
	
	This class is a subclass of :class:`BaseCGIHandler` that sets ``wsgi.run_once``
	to true, ``wsgi.multithread`` to false, and ``wsgi.multiprocess`` to true, and
	always uses :mod:`sys` and :mod:`os` to obtain the necessary CGI streams and
	environment.
	
	
	"""
	
	
	def __init__(self, ):
		pass
	
	


class BaseCGIHandler:


	"""
	Similar to :class:`CGIHandler`, but instead of using the :mod:`sys` and
	:mod:`os` modules, the CGI environment and I/O streams are specified explicitly.
	The *multithread* and *multiprocess* values are used to set the
	``wsgi.multithread`` and ``wsgi.multiprocess`` flags for any applications run by
	the handler instance.
	
	This class is a subclass of :class:`SimpleHandler` intended for use with
	software other than HTTP "origin servers".  If you are writing a gateway
	protocol implementation (such as CGI, FastCGI, SCGI, etc.) that uses a
	``Status:`` header to send an HTTP status, you probably want to subclass this
	instead of :class:`SimpleHandler`.
	
	
	"""
	
	
	def __init__(self, stdin,stdout,stderr,environ,multithread=True,multiprocess=False):
		pass
	
	


class SimpleHandler:


	"""
	Similar to :class:`BaseCGIHandler`, but designed for use with HTTP origin
	servers.  If you are writing an HTTP server implementation, you will probably
	want to subclass this instead of :class:`BaseCGIHandler`
	
	This class is a subclass of :class:`BaseHandler`.  It overrides the
	:meth:`__init__`, :meth:`get_stdin`, :meth:`get_stderr`, :meth:`add_cgi_vars`,
	:meth:`_write`, and :meth:`_flush` methods to support explicitly setting the
	environment and streams via the constructor.  The supplied environment and
	streams are stored in the :attr:`stdin`, :attr:`stdout`, :attr:`stderr`, and
	:attr:`environ` attributes.
	
	
	"""
	
	
	def __init__(self, stdin,stdout,stderr,environ,multithread=True,multiprocess=False):
		pass
	
	


class BaseHandler:


	"""
	This is an abstract base class for running WSGI applications.  Each instance
	will handle a single HTTP request, although in principle you could create a
	subclass that was reusable for multiple requests.
	
	:class:`BaseHandler` instances have only one method intended for external use:
	
	
	"""
	
	
	def __init__(self, ):
		pass
	
	


