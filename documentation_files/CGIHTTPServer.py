#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
""":synopsis: This module provides a request handler for HTTP servers which can run CGI
scripts.
"""
class CGIHTTPRequestHandler:


	"""
	This class is used to serve either files or output of CGI scripts from  the
	current directory and below. Note that mapping HTTP hierarchic structure to
	local directory structure is exactly as in
	:class:`SimpleHTTPServer.SimpleHTTPRequestHandler`.
	
	The class will however, run the CGI script, instead of serving it as a file, if
	it guesses it to be a CGI script. Only directory-based CGI are used --- the
	other common server configuration is to treat special extensions as denoting CGI
	scripts.
	
	The :func:`do_GET` and :func:`do_HEAD` functions are modified to run CGI scripts
	and serve the output, instead of serving files, if the request leads to
	somewhere below the ``cgi_directories`` path.
	
	The :class:`CGIHTTPRequestHandler` defines the following data member:
	
	
	"""
	
	
	def __init__(self, request,client_address,server):
		pass
	
	


