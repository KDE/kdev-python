#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
""":synopsis: WSGI response header tools.


This module provides a single class, :class:`Headers`, for convenient
manipulation of WSGI response headers using a mapping-like interface.


"""
class Headers:


	"""
	Create a mapping-like object wrapping *headers*, which must be a list of header
	name/value tuples as described in :pep:`333`.  Any changes made to the new
	:class:`Headers` object will directly update the *headers* list it was created
	with.
	
	:class:`Headers` objects support typical mapping operations including
	:meth:`__getitem__`, :meth:`get`, :meth:`__setitem__`, :meth:`setdefault`,
	:meth:`__delitem__`, :meth:`__contains__` and :meth:`has_key`.  For each of
	these methods, the key is the header name (treated case-insensitively), and the
	value is the first value associated with that header name.  Setting a header
	deletes any existing values for that header, then adds a new value at the end of
	the wrapped header list.  Headers' existing order is generally maintained, with
	new headers added to the end of the wrapped list.
	
	Unlike a dictionary, :class:`Headers` objects do not raise an error when you try
	to get or delete a key that isn't in the wrapped header list. Getting a
	nonexistent header just returns ``None``, and deleting a nonexistent header does
	nothing.
	
	:class:`Headers` objects also support :meth:`keys`, :meth:`values`, and
	:meth:`items` methods.  The lists returned by :meth:`keys` and :meth:`items` can
	include the same key more than once if there is a multi-valued header.  The
	``len()`` of a :class:`Headers` object is the same as the length of its
	:meth:`items`, which is the same as the length of the wrapped header list.  In
	fact, the :meth:`items` method just returns a copy of the wrapped header list.
	
	Calling ``str()`` on a :class:`Headers` object returns a formatted string
	suitable for transmission as HTTP response headers.  Each header is placed on a
	line with its value, separated by a colon and a space. Each line is terminated
	by a carriage return and line feed, and the string is terminated with a blank
	line.
	
	In addition to their mapping interface and formatting features, :class:`Headers`
	objects also have the following methods for querying and adding multi-valued
	headers, and for adding headers with MIME parameters:
	
	
	"""
	
	
	def __init__(self, ):
		pass
	
	def get_all(self, name):
		"""
		Return a list of all the values for the named header.
		
		The returned list will be sorted in the order they appeared in the original
		header list or were added to this instance, and may contain duplicates.  Any
		fields deleted and re-inserted are always appended to the header list.  If no
		fields exist with the given name, returns an empty list.
		
		
		"""
		pass
		
	def add_header(self, name,value,_params):
		"""
		Add a (possibly multi-valued) header, with optional MIME parameters specified
		via keyword arguments.
		
		*name* is the header field to add.  Keyword arguments can be used to set MIME
		parameters for the header field.  Each parameter must be a string or ``None``.
		Underscores in parameter names are converted to dashes, since dashes are illegal
		in Python identifiers, but many MIME parameter names include dashes.  If the
		parameter value is a string, it is added to the header value parameters in the
		form ``name="value"``. If it is ``None``, only the parameter name is added.
		(This is used for MIME parameters without a value.)  Example usage::
		
		h.add_header('content-disposition', 'attachment', filename='bud.gif')
		
		The above will add a header that looks like this::
		
		Content-Disposition: attachment; filename="bud.gif"
		
		
		:mod:`wsgiref.simple_server` -- a simple WSGI HTTP server
		"""
		pass
		
	


