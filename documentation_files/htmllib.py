#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
""":synopsis: A parser for HTML documents.
:deprecated:

"""
class HTMLParser:


	"""
	This is the basic HTML parser class.  It supports all entity names required by
	the XHTML 1.0 Recommendation (http://www.w3.org/TR/xhtml1).   It also defines
	handlers for all HTML 2.0 and many HTML 3.0 and 3.2 elements.
	
	
	"""
	
	
	def __init__(self, ):
		pass
	
	def anchor_bgn(self, href,name,type):
		"""
		This method is called at the start of an anchor region.  The arguments
		correspond to the attributes of the ``<A>`` tag with the same names.  The
		default implementation maintains a list of hyperlinks (defined by the ``HREF``
		attribute for ``<A>`` tags) within the document.  The list of hyperlinks is
		available as the data attribute :attr:`anchorlist`.
		
		
		"""
		pass
		
	def anchor_end(self, ):
		"""
		This method is called at the end of an anchor region.  The default
		implementation adds a textual footnote marker using an index into the list of
		hyperlinks created by :meth:`anchor_bgn`.
		
		
		"""
		pass
		
	def handle_image(self, source,alt,ismap,align,width,height):
		"""
		This method is called to handle images.  The default implementation simply
		passes the *alt* value to the :meth:`handle_data` method.
		
		
		"""
		pass
		
	def save_bgn(self, ):
		"""
		Begins saving character data in a buffer instead of sending it to the formatter
		object.  Retrieve the stored data via :meth:`save_end`. Use of the
		:meth:`save_bgn` / :meth:`save_end` pair may not be nested.
		
		
		"""
		pass
		
	def save_end(self, ):
		"""
		Ends buffering character data and returns all data saved since the preceding
		call to :meth:`save_bgn`.  If the :attr:`nofill` flag is false, whitespace is
		collapsed to single spaces.  A call to this method without a preceding call to
		:meth:`save_bgn` will raise a :exc:`TypeError` exception.
		
		
		:mod:`htmlentitydefs` --- Definitions of HTML general entities
		==============================================================
		
		"""
		pass
		
	


