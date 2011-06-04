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
	
	
	def __init__(self, headers):
		pass
	
	


