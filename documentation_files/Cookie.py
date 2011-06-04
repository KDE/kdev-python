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
	
	
	def __init__(self, ):
		pass
	
	def value_decode(self, val):
		"""
		Return a decoded value from a string representation. Return value can be any
		type. This method does nothing in :class:`BaseCookie` --- it exists so it can be
		overridden.
		
		
		"""
		pass
		
	def value_encode(self, val):
		"""
		Return an encoded value. *val* can be any type, but return value must be a
		string. This method does nothing in :class:`BaseCookie` --- it exists so it can
		be overridden
		
		In general, it should be the case that :meth:`value_encode` and
		:meth:`value_decode` are inverses on the range of *value_decode*.
		
		
		"""
		pass
		
	def output(self, attrs,header,sep):
		"""
		Return a string representation suitable to be sent as HTTP headers. *attrs* and
		*header* are sent to each :class:`Morsel`'s :meth:`output` method. *sep* is used
		to join the headers together, and is by default the combination ``'\r\n'``
		(CRLF).
		
		"""
		pass
		
	def js_output(self, attrs):
		"""
		Return an embeddable JavaScript snippet, which, if run on a browser which
		supports JavaScript, will act the same as if the HTTP headers was sent.
		
		The meaning for *attrs* is the same as in :meth:`output`.
		
		
		"""
		pass
		
	def load(self, rawdata):
		"""
		If *rawdata* is a string, parse it as an ``HTTP_COOKIE`` and add the values
		found there as :class:`Morsel`\ s. If it is a dictionary, it is equivalent to::
		
		for k, v in rawdata.items():
		cookie[k] = v
		
		
		.. orsel Objects
		--------------
		
		
		"""
		pass
		
	


class SimpleCookie:


	"""
	This class derives from :class:`BaseCookie` and overrides :meth:`value_decode`
	and :meth:`value_encode` to be the identity and :func:`str` respectively.
	
	
	"""
	
	
	def __init__(self, ):
		pass
	
	


class SerialCookie:


	"""
	This class derives from :class:`BaseCookie` and overrides :meth:`value_decode`
	and :meth:`value_encode` to be the :func:`pickle.loads` and
	:func:`pickle.dumps`.
	
	"""
	
	
	def __init__(self, ):
		pass
	
	


class SmartCookie:


	"""
	This class derives from :class:`BaseCookie`. It overrides :meth:`value_decode`
	to be :func:`pickle.loads` if it is a valid pickle, and otherwise the value
	itself. It overrides :meth:`value_encode` to be :func:`pickle.dumps` unless it
	is a string, in which case it returns the value itself.
	
	"""
	
	
	def __init__(self, ):
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
	
	def set(self, key,value,coded_value):
		"""
		Set the *key*, *value* and *coded_value* members.
		
		
		"""
		pass
		
	def isReservedKey(self, K):
		"""
		Whether *K* is a member of the set of keys of a :class:`Morsel`.
		
		
		"""
		pass
		
	def output(self, attrs,header):
		"""
		Return a string representation of the Morsel, suitable to be sent as an HTTP
		header. By default, all the attributes are included, unless *attrs* is given, in
		which case it should be a list of attributes to use. *header* is by default
		``"Set-Cookie:"``.
		
		
		"""
		pass
		
	def js_output(self, attrs):
		"""
		Return an embeddable JavaScript snippet, which, if run on a browser which
		supports JavaScript, will act the same as if the HTTP header was sent.
		
		The meaning for *attrs* is the same as in :meth:`output`.
		
		
		"""
		pass
		
	def OutputString(self, attrs):
		"""
		Return a string representing the Morsel, without any surrounding HTTP or
		JavaScript.
		
		The meaning for *attrs* is the same as in :meth:`output`.
		
		
		.. xample
		-------
		
		The following example demonstrates how to use the :mod:`Cookie` module.
		
		"""
		pass
		
	


