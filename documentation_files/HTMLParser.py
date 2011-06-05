#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
""":synopsis: A simple parser that can handle HTML and XHTML.

"""
class HTMLParser:


	"""
	The :class:`HTMLParser` class is instantiated without arguments.
	
	An :class:`HTMLParser` instance is fed HTML data and calls handler functions when tags
	begin and end.  The :class:`HTMLParser` class is meant to be overridden by the
	user to provide a desired behavior.
	
	Unlike the parser in :mod:`htmllib`, this parser does not check that end tags
	match start tags or call the end-tag handler for elements which are closed
	implicitly by closing an outer element.
	
	An exception is defined as well:
	
	
	"""
	
	
	def __init__(self, ):
		pass
	
	def reset(self, ):
		"""
		Reset the instance.  Loses all unprocessed data.  This is called implicitly at
		instantiation time.
		
		
		"""
		pass
		
	def feed(self, data):
		"""
		Feed some text to the parser.  It is processed insofar as it consists of
		complete elements; incomplete data is buffered until more data is fed or
		:meth:`close` is called.
		
		
		"""
		pass
		
	def close(self, ):
		"""
		Force processing of all buffered data as if it were followed by an end-of-file
		mark.  This method may be redefined by a derived class to define additional
		processing at the end of the input, but the redefined version should always call
		the :class:`HTMLParser` base class method :meth:`close`.
		
		
		"""
		pass
		
	def getpos(self, ):
		"""
		Return current line number and offset.
		
		
		"""
		pass
		
	def get_starttag_text(self, ):
		"""
		Return the text of the most recently opened start tag.  This should not normally
		be needed for structured processing, but may be useful in dealing with HTML "as
		deployed" or for re-generating input with minimal changes (whitespace between
		attributes can be preserved, etc.).
		
		
		"""
		pass
		
	def handle_starttag(self, tag,attrs):
		"""
		This method is called to handle the start of a tag.  It is intended to be
		overridden by a derived class; the base class implementation does nothing.
		
		The *tag* argument is the name of the tag converted to lower case. The *attrs*
		argument is a list of ``(name, value)`` pairs containing the attributes found
		inside the tag's ``<>`` brackets.  The *name* will be translated to lower case,
		and quotes in the *value* have been removed, and character and entity references
		have been replaced.  For instance, for the tag ``<A
		HREF="http://www.cwi.nl/">``, this method would be called as
		``handle_starttag('a', [('href', 'http://www.cwi.nl/')])``.
		
		"""
		pass
		
	def handle_startendtag(self, tag,attrs):
		"""
		Similar to :meth:`handle_starttag`, but called when the parser encounters an
		XHTML-style empty tag (``<a more/>``).  This method may be overridden by
		subclasses which require this particular lexical information; the default
		implementation simple calls :meth:`handle_starttag` and :meth:`handle_endtag`.
		
		
		"""
		pass
		
	def handle_endtag(self, tag):
		"""
		This method is called to handle the end tag of an element.  It is intended to be
		overridden by a derived class; the base class implementation does nothing.  The
		*tag* argument is the name of the tag converted to lower case.
		
		
		"""
		pass
		
	def handle_data(self, data):
		"""
		This method is called to process arbitrary data.  It is intended to be
		overridden by a derived class; the base class implementation does nothing.
		
		
		"""
		pass
		
	def handle_charref(self, name):
		"""
		This method is called to process a character reference of the form ``&#ref;``.
		It is intended to be overridden by a derived class; the base class
		implementation does nothing.
		
		
		"""
		pass
		
	def handle_entityref(self, name):
		"""
		This method is called to process a general entity reference of the form
		``&name;`` where *name* is an general entity reference.  It is intended to be
		overridden by a derived class; the base class implementation does nothing.
		
		
		"""
		pass
		
	def handle_comment(self, data):
		"""
		This method is called when a comment is encountered.  The *comment* argument is
		a string containing the text between the ``--`` and ``--`` delimiters, but not
		the delimiters themselves.  For example, the comment ``<!--text-->`` will cause
		this method to be called with the argument ``'text'``.  It is intended to be
		overridden by a derived class; the base class implementation does nothing.
		
		
		"""
		pass
		
	def handle_decl(self, decl):
		"""
		Method called when an SGML ``doctype`` declaration is read by the parser.
		The *decl* parameter will be the entire contents of the declaration inside
		the ``<!more>`` markup.  It is intended to be overridden by a derived class;
		the base class implementation does nothing.
		
		
		"""
		pass
		
	def unknown_decl(self, data):
		"""
		Method called when an unrecognized SGML declaration is read by the parser.
		The *data* parameter will be the entire contents of the declaration inside
		the ``<!more>`` markup.  It is sometimes useful to be overridden by a
		derived class; the base class implementation throws an :exc:`HTMLParseError`.
		
		
		"""
		pass
		
	def handle_pi(self, data):
		"""
		Method called when a processing instruction is encountered.  The *data*
		parameter will contain the entire processing instruction. For example, for the
		processing instruction ``<?proc color='red'>``, this method would be called as
		``handle_pi("proc color='red'")``.  It is intended to be overridden by a derived
		class; the base class implementation does nothing.
		
		"""
		pass
		
	


