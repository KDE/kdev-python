#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
""":synopsis: This module provides a basic request handler for HTTP servers.
"""
class SimpleHTTPRequestHandler:


	"""
	This class serves files from the current directory and below, directly
	mapping the directory structure to HTTP requests.
	
	A lot of the work, such as parsing the request, is done by the base class
	:class:`BaseHTTPServer.BaseHTTPRequestHandler`.  This class implements the
	:func:`do_GET` and :func:`do_HEAD` functions.
	
	The following are defined as class-level attributes of
	:class:`SimpleHTTPRequestHandler`:
	
	
	"""
	
	
	def __init__(self, ):
		pass
	
	def do_HEAD(self, ):
		"""
		This method serves the ``'HEAD'`` request type: it sends the headers it
		would send for the equivalent ``GET`` request. See the :meth:`do_GET`
		method for a more complete explanation of the possible headers.
		
		
		"""
		pass
		
	def do_GET(self, ):
		"""
		The request is mapped to a local file by interpreting the request as a
		path relative to the current working directory.
		
		If the request was mapped to a directory, the directory is checked for a
		file named ``index.html`` or ``index.htm`` (in that order). If found, the
		file's contents are returned; otherwise a directory listing is generated
		by calling the :meth:`list_directory` method. This method uses
		:func:`os.listdir` to scan the directory, and returns a ``404`` error
		response if the :func:`listdir` fails.
		
		If the request was mapped to a file, it is opened and the contents are
		returned.  Any :exc:`IOError` exception in opening the requested file is
		mapped to a ``404``, ``'File not found'`` error. Otherwise, the content
		type is guessed by calling the :meth:`guess_type` method, which in turn
		uses the *extensions_map* variable.
		
		A ``'Content-type:'`` header with the guessed content type is output,
		followed by a ``'Content-Length:'`` header with the file's size and a
		``'Last-Modified:'`` header with the file's modification time.
		
		Then follows a blank line signifying the end of the headers, and then the
		contents of the file are output. If the file's MIME type starts with
		``text/`` the file is opened in text mode; otherwise binary mode is used.
		
		The :func:`test` function in the :mod:`SimpleHTTPServer` module is an
		example which creates a server using the :class:`SimpleHTTPRequestHandler`
		as the Handler.
		
		"""
		pass
		
	


