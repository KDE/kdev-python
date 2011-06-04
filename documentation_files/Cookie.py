#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
""":synopsis: Support for HTTP state management (cookies).
"""
class BaseCookie:


	"""
	This class is a dictionary-like object whose keys are strings and whose values
	are :class:`Morsel` instances. Note that upon setting a key to a value, the
	value is first converted to a :class:`Morsel` containing the key and the value.
	
	If *input* is given, it is passed to the :meth:`load` method.
	
	
	"""
	
	
	def __init__(self, input):
		pass
	
	


class SimpleCookie:


	"""
	This class derives from :class:`BaseCookie` and overrides :meth:`value_decode`
	and :meth:`value_encode` to be the identity and :func:`str` respectively.
	
	
	"""
	
	
	def __init__(self, input):
		pass
	
	


class SerialCookie:


	"""
	This class derives from :class:`BaseCookie` and overrides :meth:`value_decode`
	and :meth:`value_encode` to be the :func:`pickle.loads` and
	:func:`pickle.dumps`.
	
	"""
	
	
	def __init__(self, input):
		pass
	
	


class SmartCookie:


	"""
	This class derives from :class:`BaseCookie`. It overrides :meth:`value_decode`
	to be :func:`pickle.loads` if it is a valid pickle, and otherwise the value
	itself. It overrides :meth:`value_encode` to be :func:`pickle.dumps` unless it
	is a string, in which case it returns the value itself.
	
	"""
	
	
	def __init__(self, input):
		pass
	
	


class Morsel:


	"""
	Abstract a key/value pair, which has some :rfc:`2109` attributes.
	
	Morsels are dictionary-like objects, whose set of keys is constant --- the valid
	:rfc:`2109` attributes, which are
	
	* ``expires``
	* ``path``
	* ``comment``
	* ``domain``
	* ``max-age``
	* ``secure``
	* ``version``
	* ``httponly``
	
	The attribute :attr:`httponly` specifies that the cookie is only transfered
	in HTTP requests, and is not accessible through JavaScript. This is intended
	to mitigate some forms of cross-site scripting.
	
	The keys are case-insensitive.
	
	"""
	
	
	def __init__(self, ):
		pass
	
	


