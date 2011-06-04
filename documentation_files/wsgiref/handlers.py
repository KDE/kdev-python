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
	
	
	def __init__(self, ):
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
	
	
	def __init__(self, ):
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
	
	def run(self, app):
		"""
		Run the specified WSGI application, *app*.
		
		All of the other :class:`BaseHandler` methods are invoked by this method in the
		process of running the application, and thus exist primarily to allow
		customizing the process.
		
		The following methods MUST be overridden in a subclass:
		
		
		"""
		pass
		
	def _write(self, data):
		"""
		Buffer the string *data* for transmission to the client.  It's okay if this
		method actually transmits the data; :class:`BaseHandler` just separates write
		and flush operations for greater efficiency when the underlying system actually
		has such a distinction.
		
		
		"""
		pass
		
	def _flush(self, ):
		"""
		Force buffered data to be transmitted to the client.  It's okay if this method
		is a no-op (i.e., if :meth:`_write` actually sends the data).
		
		
		"""
		pass
		
	def get_stdin(self, ):
		"""
		Return an input stream object suitable for use as the ``wsgi.input`` of the
		request currently being processed.
		
		
		"""
		pass
		
	def get_stderr(self, ):
		"""
		Return an output stream object suitable for use as the ``wsgi.errors`` of the
		request currently being processed.
		
		
		"""
		pass
		
	def add_cgi_vars(self, ):
		"""
		Insert CGI variables for the current request into the :attr:`environ` attribute.
		
		Here are some other methods and attributes you may wish to override. This list
		is only a summary, however, and does not include every method that can be
		overridden.  You should consult the docstrings and source code for additional
		information before attempting to create a customized :class:`BaseHandler`
		subclass.
		
		Attributes and methods for customizing the WSGI environment:
		
		
		"""
		pass
		
	def get_scheme(self, ):
		"""
		Return the URL scheme being used for the current request.  The default
		implementation uses the :func:`guess_scheme` function from :mod:`wsgiref.util`
		to guess whether the scheme should be "http" or "https", based on the current
		request's :attr:`environ` variables.
		
		
		"""
		pass
		
	def setup_environ(self, ):
		"""
		Set the :attr:`environ` attribute to a fully-populated WSGI environment.  The
		default implementation uses all of the above methods and attributes, plus the
		:meth:`get_stdin`, :meth:`get_stderr`, and :meth:`add_cgi_vars` methods and the
		:attr:`wsgi_file_wrapper` attribute.  It also inserts a ``SERVER_SOFTWARE`` key
		if not present, as long as the :attr:`origin_server` attribute is a true value
		and the :attr:`server_software` attribute is set.
		
		Methods and attributes for customizing exception handling:
		
		
		"""
		pass
		
	def log_exception(self, exc_info):
		"""
		Log the *exc_info* tuple in the server log.  *exc_info* is a ``(type, value,
		traceback)`` tuple.  The default implementation simply writes the traceback to
		the request's ``wsgi.errors`` stream and flushes it.  Subclasses can override
		this method to change the format or retarget the output, mail the traceback to
		an administrator, or whatever other action may be deemed suitable.
		
		
		"""
		pass
		
	def error_output(self, environ,start_response):
		"""
		This method is a WSGI application to generate an error page for the user.  It is
		only invoked if an error occurs before headers are sent to the client.
		
		This method can access the current error information using ``sys.exc_info()``,
		and should pass that information to *start_response* when calling it (as
		described in the "Error Handling" section of :pep:`333`).
		
		The default implementation just uses the :attr:`error_status`,
		:attr:`error_headers`, and :attr:`error_body` attributes to generate an output
		page.  Subclasses can override this to produce more dynamic error output.
		
		Note, however, that it's not recommended from a security perspective to spit out
		diagnostics to any old user; ideally, you should have to do something special to
		enable diagnostic output, which is why the default implementation doesn't
		include any.
		
		
		"""
		pass
		
	def sendfile(self, ):
		"""
		Override to implement platform-specific file transmission.  This method is
		called only if the application's return value is an instance of the class
		specified by the :attr:`wsgi_file_wrapper` attribute.  It should return a true
		value if it was able to successfully transmit the file, so that the default
		transmission code will not be executed. The default implementation of this
		method just returns a false value.
		
		Miscellaneous methods and attributes:
		
		
		"""
		pass
		
	


