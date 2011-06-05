#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
""":synopsis: WSGI environment utilities.


This module provides a variety of utility functions for working with WSGI
environments.  A WSGI environment is a dictionary containing HTTP request
variables as described in :pep:`333`.  All of the functions taking an *environ*
parameter expect a WSGI-compliant dictionary to be supplied; please see
:pep:`333` for a detailed specification.


"""
def guess_scheme(environ):
	"""
	Return a guess for whether ``wsgi.url_scheme`` should be "http" or "https", by
	checking for a ``HTTPS`` environment variable in the *environ* dictionary.  The
	return value is a string.
	
	This function is useful when creating a gateway that wraps CGI or a CGI-like
	protocol such as FastCGI.  Typically, servers providing such protocols will
	include a ``HTTPS`` variable with a value of "1" "yes", or "on" when a request
	is received via SSL.  So, this function returns "https" if such a value is
	found, and "http" otherwise.
	
	
	"""
	pass
	
def request_uri(environ,include_query=1):
	"""
	Return the full request URI, optionally including the query string, using the
	algorithm found in the "URL Reconstruction" section of :pep:`333`.  If
	*include_query* is false, the query string is not included in the resulting URI.
	
	
	"""
	pass
	
def application_uri(environ):
	"""
	Similar to :func:`request_uri`, except that the ``PATH_INFO`` and
	``QUERY_STRING`` variables are ignored.  The result is the base URI of the
	application object addressed by the request.
	
	
	"""
	pass
	
def shift_path_info(environ):
	"""
	Shift a single name from ``PATH_INFO`` to ``SCRIPT_NAME`` and return the name.
	The *environ* dictionary is *modified* in-place; use a copy if you need to keep
	the original ``PATH_INFO`` or ``SCRIPT_NAME`` intact.
	
	If there are no remaining path segments in ``PATH_INFO``, ``None`` is returned.
	
	Typically, this routine is used to process each portion of a request URI path,
	for example to treat the path as a series of dictionary keys. This routine
	modifies the passed-in environment to make it suitable for invoking another WSGI
	application that is located at the target URI. For example, if there is a WSGI
	application at ``/foo``, and the request URI path is ``/foo/bar/baz``, and the
	WSGI application at ``/foo`` calls :func:`shift_path_info`, it will receive the
	string "bar", and the environment will be updated to be suitable for passing to
	a WSGI application at ``/foo/bar``.  That is, ``SCRIPT_NAME`` will change from
	``/foo`` to ``/foo/bar``, and ``PATH_INFO`` will change from ``/bar/baz`` to
	``/baz``.
	
	When ``PATH_INFO`` is just a "/", this routine returns an empty string and
	appends a trailing slash to ``SCRIPT_NAME``, even though empty path segments are
	normally ignored, and ``SCRIPT_NAME`` doesn't normally end in a slash.  This is
	intentional behavior, to ensure that an application can tell the difference
	between URIs ending in ``/x`` from ones ending in ``/x/`` when using this
	routine to do object traversal.
	
	
	"""
	pass
	
def setup_testing_defaults(environ):
	"""
	Update *environ* with trivial defaults for testing purposes.
	
	This routine adds various parameters required for WSGI, including ``HTTP_HOST``,
	``SERVER_NAME``, ``SERVER_PORT``, ``REQUEST_METHOD``, ``SCRIPT_NAME``,
	``PATH_INFO``, and all of the :pep:`333`\ -defined ``wsgi.*`` variables.  It
	only supplies default values, and does not replace any existing settings for
	these variables.
	
	This routine is intended to make it easier for unit tests of WSGI servers and
	applications to set up dummy environments.  It should NOT be used by actual WSGI
	servers or applications, since the data is fake!
	
	Example usage::
	
	from wsgiref.util import setup_testing_defaults
	from wsgiref.simple_server import make_server
	
	# A relatively simple WSGI application. It's going to print out the
	# environment dictionary after being updated by setup_testing_defaults
	def simple_app(environ, start_response):
	setup_testing_defaults(environ)
	
	status = '200 OK'
	headers = [('Content-type', 'text/plain')]
	
	start_response(status, headers)
	
	ret = ["%s: %s\n" % (key, value)
	for key, value in environ.iteritems()]
	return ret
	
	httpd = make_server('', 8000, simple_app)
	print "Serving on port 8000more"
	httpd.serve_forever()
	
	
	In addition to the environment functions above, the :mod:`wsgiref.util` module
	also provides these miscellaneous utilities:
	
	
	"""
	pass
	
def is_hop_by_hop(header_name):
	"""
	Return true if 'header_name' is an HTTP/1.1 "Hop-by-Hop" header, as defined by
	:rfc:`2616`.
	
	
	"""
	pass
	
class FileWrapper:


	"""
	A wrapper to convert a file-like object to an :term:`iterator`.  The resulting objects
	support both :meth:`__getitem__` and :meth:`__iter__` iteration styles, for
	compatibility with Python 2.1 and Jython. As the object is iterated over, the
	optional *blksize* parameter will be repeatedly passed to the *filelike*
	object's :meth:`read` method to obtain strings to yield.  When :meth:`read`
	returns an empty string, iteration is ended and is not resumable.
	
	If *filelike* has a :meth:`close` method, the returned object will also have a
	:meth:`close` method, and it will invoke the *filelike* object's :meth:`close`
	method when called.
	
	Example usage::
	
	from StringIO import StringIO
	from wsgiref.util import FileWrapper
	
	# We're using a StringIO-buffer for as the file-like object
	filelike = StringIO("This is an example file-like object"*10)
	wrapper = FileWrapper(filelike, blksize=5)
	
	for chunk in wrapper:
	print chunk
	
	
	
	:mod:`wsgiref.headers` -- WSGI response header tools
	----------------------------------------------------
	
	"""
	
	
	def __init__(self, ):
		pass
	
	


