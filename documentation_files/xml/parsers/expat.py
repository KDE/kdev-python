#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
""":synopsis: An interface to the Expat non-validating XML parser.
"""
"""
The type of the return values from the :func:`ParserCreate` function.

The :mod:`xml.parsers.expat` module contains two functions:


"""
XMLParserType = None
""":noindex:

The element named by the model name was declared to have a content model of
``ANY``.


"""
XML_CTYPE_ANY = None
""":noindex:

The named element allows a choice from a number of options; this is used for
content models such as ``(A | B | C)``.


"""
XML_CTYPE_CHOICE = None
""":noindex:

Elements which are declared to be ``EMPTY`` have this model type.


"""
XML_CTYPE_EMPTY = None
""":noindex:


"""
XML_CTYPE_MIXED = None
""":noindex:


"""
XML_CTYPE_NAME = None
""":noindex:

Models which represent a series of models which follow one after the other are
indicated with this model type.  This is used for models such as ``(A, B, C)``.

The constants in the quantifier group are:


"""
XML_CTYPE_SEQ = None
""":noindex:

No modifier is given, so it can appear exactly once, as for ``A``.


"""
XML_CQUANT_NONE = None
""":noindex:

The model is optional: it can appear once or not at all, as for ``A?``.


"""
XML_CQUANT_OPT = None
""":noindex:

The model must occur one or more times (like ``A+``).


"""
XML_CQUANT_PLUS = None
""":noindex:

The model must occur zero or more times, as for ``A*``.


.. xpat error constants
---------------------

The following constants are provided in the ``errors`` object of the
:mod:`xml.parsers.expat` module.  These constants are useful in interpreting
some of the attributes of the :exc:`ExpatError` exception objects raised when an
error has occurred.

The ``errors`` object has the following attributes:


"""
XML_CQUANT_REP = None
""":noindex:


"""
XML_ERROR_ASYNC_ENTITY = None
""":noindex:

An entity reference in an attribute value referred to an external entity instead
of an internal entity.


"""
XML_ERROR_ATTRIBUTE_EXTERNAL_ENTITY_REF = None
""":noindex:

A character reference referred to a character which is illegal in XML (for
example, character ``0``, or '``&#0;``').


"""
XML_ERROR_BAD_CHAR_REF = None
""":noindex:

An entity reference referred to an entity which was declared with a notation, so
cannot be parsed.


"""
XML_ERROR_BINARY_ENTITY_REF = None
""":noindex:

An attribute was used more than once in a start tag.


"""
XML_ERROR_DUPLICATE_ATTRIBUTE = None
""":noindex:


"""
XML_ERROR_INCORRECT_ENCODING = None
""":noindex:

Raised when an input byte could not properly be assigned to a character; for
example, a NUL byte (value ``0``) in a UTF-8 input stream.


"""
XML_ERROR_INVALID_TOKEN = None
""":noindex:

Something other than whitespace occurred after the document element.


"""
XML_ERROR_JUNK_AFTER_DOC_ELEMENT = None
""":noindex:

An XML declaration was found somewhere other than the start of the input data.


"""
XML_ERROR_MISPLACED_XML_PI = None
""":noindex:

The document contains no elements (XML requires all documents to contain exactly
one top-level element)..


"""
XML_ERROR_NO_ELEMENTS = None
""":noindex:

Expat was not able to allocate memory internally.


"""
XML_ERROR_NO_MEMORY = None
""":noindex:

A parameter entity reference was found where it was not allowed.


"""
XML_ERROR_PARAM_ENTITY_REF = None
""":noindex:

An incomplete character was found in the input.


"""
XML_ERROR_PARTIAL_CHAR = None
""":noindex:

An entity reference contained another reference to the same entity; possibly via
a different name, and possibly indirectly.


"""
XML_ERROR_RECURSIVE_ENTITY_REF = None
""":noindex:

Some unspecified syntax error was encountered.


"""
XML_ERROR_SYNTAX = None
""":noindex:

An end tag did not match the innermost open start tag.


"""
XML_ERROR_TAG_MISMATCH = None
""":noindex:

Some token (such as a start tag) was not closed before the end of the stream or
the next token was encountered.


"""
XML_ERROR_UNCLOSED_TOKEN = None
""":noindex:

A reference was made to a entity which was not defined.


"""
XML_ERROR_UNDEFINED_ENTITY = None
""":noindex:

The document encoding is not supported by Expat.


"""
XML_ERROR_UNKNOWN_ENCODING = None
""":noindex:

A CDATA marked section was not closed.


"""
XML_ERROR_UNCLOSED_CDATA_SECTION = None
""":noindex:


"""
XML_ERROR_EXTERNAL_ENTITY_HANDLING = None
""":noindex:

The parser determined that the document was not "standalone" though it declared
itself to be in the XML declaration, and the :attr:`NotStandaloneHandler` was
set and returned ``0``.


"""
XML_ERROR_NOT_STANDALONE = None
""":noindex:


"""
XML_ERROR_UNEXPECTED_STATE = None
""":noindex:


"""
XML_ERROR_ENTITY_DECLARED_IN_PE = None
""":noindex:

An operation was requested that requires DTD support to be compiled in, but
Expat was configured without DTD support.  This should never be reported by a
standard build of the :mod:`xml.parsers.expat` module.


"""
XML_ERROR_FEATURE_REQUIRES_XML_DTD = None
""":noindex:

A behavioral change was requested after parsing started that can only be changed
before parsing has started.  This is (currently) only raised by
:meth:`UseForeignDTD`.


"""
XML_ERROR_CANT_CHANGE_FEATURE_ONCE_PARSING = None
""":noindex:

An undeclared prefix was found when namespace processing was enabled.


"""
XML_ERROR_UNBOUND_PREFIX = None
""":noindex:

The document attempted to remove the namespace declaration associated with a
prefix.


"""
XML_ERROR_UNDECLARING_PREFIX = None
""":noindex:

A parameter entity contained incomplete markup.


"""
XML_ERROR_INCOMPLETE_PE = None
""":noindex:

The document contained no document element at all.


"""
XML_ERROR_XML_DECL = None
""":noindex:

There was an error parsing a text declaration in an external entity.


"""
XML_ERROR_TEXT_DECL = None
""":noindex:

Characters were found in the public id that are not allowed.


"""
XML_ERROR_PUBLICID = None
""":noindex:

The requested operation was made on a suspended parser, but isn't allowed.  This
includes attempts to provide additional input or to stop the parser.


"""
XML_ERROR_SUSPENDED = None
""":noindex:

An attempt to resume the parser was made when the parser had not been suspended.


"""
XML_ERROR_NOT_SUSPENDED = None
""":noindex:

This should not be reported to Python applications.


"""
XML_ERROR_ABORTED = None
""":noindex:

The requested operation was made on a parser which was finished parsing input,
but isn't allowed.  This includes attempts to provide additional input or to
stop the parser.


"""
XML_ERROR_FINISHED = None
""":noindex:


"""
XML_ERROR_SUSPEND_PE = None
def ErrorString(errno):
	"""
	Returns an explanatory string for a given error number *errno*.
	
	
	"""
	pass
	
def ParserCreate(encoding,namespace_separator):
	"""
	Creates and returns a new :class:`xmlparser` object.   *encoding*, if specified,
	must be a string naming the encoding  used by the XML data.  Expat doesn't
	support as many encodings as Python does, and its repertoire of encodings can't
	be extended; it supports UTF-8, UTF-16, ISO-8859-1 (Latin1), and ASCII.  If
	*encoding* [1]_ is given it will override the implicit or explicit encoding of the
	document.
	
	Expat can optionally do XML namespace processing for you, enabled by providing a
	value for *namespace_separator*.  The value must be a one-character string; a
	:exc:`ValueError` will be raised if the string has an illegal length (``None``
	is considered the same as omission).  When namespace processing is enabled,
	element type names and attribute names that belong to a namespace will be
	expanded.  The element name passed to the element handlers
	:attr:`StartElementHandler` and :attr:`EndElementHandler` will be the
	concatenation of the namespace URI, the namespace separator character, and the
	local part of the name.  If the namespace separator is a zero byte (``chr(0)``)
	then the namespace URI and the local part will be concatenated without any
	separator.
	
	For example, if *namespace_separator* is set to a space character (``' '``) and
	the following document is parsed::
	
	<?xml version="1.0"?>
	<root xmlns    = "http://default-namespace.org/"
	xmlns:py = "http://www.python.org/ns/">
	<py:elem1 />
	<elem2 xmlns="" />
	</root>
	
	:attr:`StartElementHandler` will receive the following strings for each
	element::
	
	http://default-namespace.org/ root
	http://www.python.org/ns/ elem1
	elem2
	
	
	"""
	pass
	
