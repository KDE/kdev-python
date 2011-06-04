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
	
	
	def __init__(self, request,client_address,server):
		pass
	
	


