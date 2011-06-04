#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
""":synopsis: Only as much of an SGML parser as needed to parse HTML.
:deprecated:

"""
class SGMLParser:


	"""
	The :class:`SGMLParser` class is instantiated without arguments. The parser is
	hardcoded to recognize the following constructs:
	
	* Opening and closing tags of the form ``<tag attr="value" *more>`` and
	``</tag>``, respectively.
	
	* Numeric character references of the form ``&#name;``.
	
	* Entity references of the form ``&name;``.
	
	* SGML comments of the form ``<!--text-->``.  Note that spaces, tabs, and
	newlines are allowed between the trailing ``>`` and the immediately preceding
	``--``.
	
	A single exception is defined as well:
	
	
	"""
	
	
	def __init__(self, ):
		pass
	
	def reset(self, ):
		"""
		Reset the instance.  Loses all unprocessed data.  This is called implicitly at
		instantiation time.
		
		
		"""
		pass
		
	def setnomoretags(self, ):
		"""
		Stop processing tags.  Treat all following input as literal input (CDATA).
		(This is only provided so the HTML tag ``<PLAINTEXT>`` can be implemented.)
		
		
		"""
		pass
		
	def setliteral(self, ):
		"""
		Enter literal mode (CDATA mode).
		
		
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
		:meth:`close`.
		
		
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
		
	def handle_starttag(self, tag,method,attributes):
		"""
		This method is called to handle start tags for which either a :meth:`start_tag`
		or :meth:`do_tag` method has been defined.  The *tag* argument is the name of
		the tag converted to lower case, and the *method* argument is the bound method
		which should be used to support semantic interpretation of the start tag. The
		*attributes* argument is a list of ``(name, value)`` pairs containing the
		attributes found inside the tag's ``<>`` brackets.
		
		The *name* has been translated to lower case. Double quotes and backslashes in
		the *value* have been interpreted, as well as known character references and
		known entity references terminated by a semicolon (normally, entity references
		can be terminated by any non-alphanumerical character, but this would break the
		very common case of ``<A HREF="url?spam=1&eggs=2">`` when ``eggs`` is a valid
		entity name).
		
		For instance, for the tag ``<A HREF="http://www.cwi.nl/">``, this method would
		be called as ``unknown_starttag('a', [('href', 'http://www.cwi.nl/')])``.  The
		base implementation simply calls *method* with *attributes* as the only
		argument.
		
		"""
		pass
		
	def handle_endtag(self, tag,method):
		"""
		This method is called to handle endtags for which an :meth:`end_tag` method has
		been defined.  The *tag* argument is the name of the tag converted to lower
		case, and the *method* argument is the bound method which should be used to
		support semantic interpretation of the end tag.  If no :meth:`end_tag` method is
		defined for the closing element, this handler is not called.  The base
		implementation simply calls *method*.
		
		
		"""
		pass
		
	def handle_data(self, data):
		"""
		This method is called to process arbitrary data.  It is intended to be
		overridden by a derived class; the base class implementation does nothing.
		
		
		"""
		pass
		
	def handle_charref(self, ref):
		"""
		This method is called to process a character reference of the form ``&#ref;``.
		The base implementation uses :meth:`convert_charref` to convert the reference to
		a string.  If that method returns a string, it is passed to :meth:`handle_data`,
		otherwise ``unknown_charref(ref)`` is called to handle the error.
		
		"""
		pass
		
	def convert_charref(self, ref):
		"""
		Convert a character reference to a string, or ``None``.  *ref* is the reference
		passed in as a string.  In the base implementation, *ref* must be a decimal
		number in the range 0-255.  It converts the code point found using the
		:meth:`convert_codepoint` method. If *ref* is invalid or out of range, this
		method returns ``None``.  This method is called by the default
		:meth:`handle_charref` implementation and by the attribute value parser.
		
		"""
		pass
		
	def convert_codepoint(self, codepoint):
		"""
		Convert a codepoint to a :class:`str` value.  Encodings can be handled here if
		appropriate, though the rest of :mod:`sgmllib` is oblivious on this matter.
		
		"""
		pass
		
	def handle_entityref(self, ref):
		"""
		This method is called to process a general entity reference of the form
		``&ref;`` where *ref* is an general entity reference.  It converts *ref* by
		passing it to :meth:`convert_entityref`.  If a translation is returned, it calls
		the method :meth:`handle_data` with the translation; otherwise, it calls the
		method ``unknown_entityref(ref)``. The default :attr:`entitydefs` defines
		translations for ``&amp;``, ``&apos``, ``&gt;``, ``&lt;``, and ``&quot;``.
		
		"""
		pass
		
	def convert_entityref(self, ref):
		"""
		Convert a named entity reference to a :class:`str` value, or ``None``.  The
		resulting value will not be parsed.  *ref* will be only the name of the entity.
		The default implementation looks for *ref* in the instance (or class) variable
		:attr:`entitydefs` which should be a mapping from entity names to corresponding
		translations.  If no translation is available for *ref*, this method returns
		``None``.  This method is called by the default :meth:`handle_entityref`
		implementation and by the attribute value parser.
		
		"""
		pass
		
	def handle_comment(self, comment):
		"""
		This method is called when a comment is encountered.  The *comment* argument is
		a string containing the text between the ``<!--`` and ``-->`` delimiters, but
		not the delimiters themselves.  For example, the comment ``<!--text-->`` will
		cause this method to be called with the argument ``'text'``.  The default method
		does nothing.
		
		
		"""
		pass
		
	def handle_decl(self, data):
		"""
		Method called when an SGML declaration is read by the parser.  In practice, the
		``DOCTYPE`` declaration is the only thing observed in HTML, but the parser does
		not discriminate among different (or broken) declarations.  Internal subsets in
		a ``DOCTYPE`` declaration are not supported.  The *data* parameter will be the
		entire contents of the declaration inside the ``<!``*more\ ``>`` markup.  The
		default implementation does nothing.
		
		
		"""
		pass
		
	def report_unbalanced(self, tag):
		"""
		This method is called when an end tag is found which does not correspond to any
		open element.
		
		
		"""
		pass
		
	def unknown_starttag(self, tag,attributes):
		"""
		This method is called to process an unknown start tag.  It is intended to be
		overridden by a derived class; the base class implementation does nothing.
		
		
		"""
		pass
		
	def unknown_endtag(self, tag):
		"""
		This method is called to process an unknown end tag.  It is intended to be
		overridden by a derived class; the base class implementation does nothing.
		
		
		"""
		pass
		
	def unknown_charref(self, ref):
		"""
		This method is called to process unresolvable numeric character references.
		Refer to :meth:`handle_charref` to determine what is handled by default.  It is
		intended to be overridden by a derived class; the base class implementation does
		nothing.
		
		
		"""
		pass
		
	def unknown_entityref(self, ref):
		"""
		This method is called to process an unknown entity reference.  It is intended to
		be overridden by a derived class; the base class implementation does nothing.
		
		Apart from overriding or extending the methods listed above, derived classes may
		also define methods of the following form to define processing of specific tags.
		Tag names in the input stream are case independent; the *tag* occurring in
		method names must be in lower case:
		
		
		"""
		pass
		
	def start_tag(self, attributes):
		""":noindex:
		
		This method is called to process an opening tag *tag*.  It has preference over
		:meth:`do_tag`.  The *attributes* argument has the same meaning as described for
		:meth:`handle_starttag` above.
		
		
		"""
		pass
		
	def do_tag(self, attributes):
		""":noindex:
		
		This method is called to process an opening tag *tag*  for which no
		:meth:`start_tag` method is defined.   The *attributes* argument has the same
		meaning as described for :meth:`handle_starttag` above.
		
		
		"""
		pass
		
	


