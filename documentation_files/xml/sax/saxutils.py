#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
""":synopsis: Convenience functions and classes for use with SAX.
"""
def escape(data,entities):
	"""
	Escape ``'&'``, ``'<'``, and ``'>'`` in a string of data.
	
	You can escape other strings of data by passing a dictionary as the optional
	*entities* parameter.  The keys and values must all be strings; each key will be
	replaced with its corresponding value.  The characters ``'&'``, ``'<'`` and
	``'>'`` are always escaped, even if *entities* is provided.
	
	
	"""
	pass
	
def unescape(data,entities):
	"""
	Unescape ``'&amp;'``, ``'&lt;'``, and ``'&gt;'`` in a string of data.
	
	You can unescape other strings of data by passing a dictionary as the optional
	*entities* parameter.  The keys and values must all be strings; each key will be
	replaced with its corresponding value.  ``'&amp'``, ``'&lt;'``, and ``'&gt;'``
	are always unescaped, even if *entities* is provided.
	
	"""
	pass
	
def quoteattr(data,entities):
	"""
	Similar to :func:`escape`, but also prepares *data* to be used as an
	attribute value.  The return value is a quoted version of *data* with any
	additional required replacements. :func:`quoteattr` will select a quote
	character based on the content of *data*, attempting to avoid encoding any
	quote characters in the string.  If both single- and double-quote characters
	are already in *data*, the double-quote characters will be encoded and *data*
	will be wrapped in double-quotes.  The resulting string can be used directly
	as an attribute value::
	
	>>> print "<element attr=%s>" % quoteattr("ab ' cd \" ef")
	<element attr="ab ' cd &quot; ef">
	
	This function is useful when generating attribute values for HTML or any SGML
	using the reference concrete syntax.
	
	"""
	pass
	
class XMLGenerator:


	"""
	This class implements the :class:`ContentHandler` interface by writing SAX
	events back into an XML document. In other words, using an :class:`XMLGenerator`
	as the content handler will reproduce the original document being parsed. *out*
	should be a file-like object which will default to *sys.stdout*. *encoding* is
	the encoding of the output stream which defaults to ``'iso-8859-1'``.
	
	
	"""
	
	
	def __init__(self, out,encoding):
		pass
	
	


class XMLFilterBase:


	"""
	This class is designed to sit between an :class:`XMLReader` and the client
	application's event handlers.  By default, it does nothing but pass requests up
	to the reader and events on to the handlers unmodified, but subclasses can
	override specific methods to modify the event stream or the configuration
	requests as they pass through.
	
	
	"""
	
	
	def __init__(self, base):
		pass
	
	


