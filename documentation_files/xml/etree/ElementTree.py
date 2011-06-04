#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
""":synopsis: Implementation of the ElementTree API.
"""
def Comment(text=None):
	"""
	Comment element factory.  This factory function creates a special element
	that will be serialized as an XML comment by the standard serializer.  The
	comment string can be either a bytestring or a Unicode string.  *text* is a
	string containing the comment string.  Returns an element instance
	representing a comment.
	
	
	"""
	pass
	
def dump(elem):
	"""
	Writes an element tree or element structure to sys.stdout.  This function
	should be used for debugging only.
	
	The exact output format is implementation dependent.  In this version, it's
	written as an ordinary XML file.
	
	*elem* is an element tree or an individual element.
	
	
	"""
	pass
	
def _fromstring(text):
	"""
	Parses an XML section from a string constant.  Same as :func:`XML`.  *text*
	is a string containing XML data.  Returns an :class:`Element` instance.
	
	
	"""
	pass
	
def _fromstringlist(sequence,parser=None):
	"""
	Parses an XML document from a sequence of string fragments.  *sequence* is a
	list or other sequence containing XML data fragments.  *parser* is an
	optional parser instance.  If not given, the standard :class:`XMLParser`
	parser is used.  Returns an :class:`Element` instance.
	
	"""
	pass
	
def iselement(element):
	"""
	Checks if an object appears to be a valid element object.  *element* is an
	element instance.  Returns a true value if this is an element object.
	
	
	"""
	pass
	
def iterparse(source,events=None,parser=None):
	"""
	Parses an XML section into an element tree incrementally, and reports what's
	going on to the user.  *source* is a filename or file object containing XML
	data.  *events* is a list of events to report back.  If omitted, only "end"
	events are reported.  *parser* is an optional parser instance.  If not
	given, the standard :class:`XMLParser` parser is used.  Returns an
	:term:`iterator` providing ``(event, elem)`` pairs.
	
	"""
	pass
	
def parse(source,parser=None):
	"""
	Parses an XML section into an element tree.  *source* is a filename or file
	object containing XML data.  *parser* is an optional parser instance.  If
	not given, the standard :class:`XMLParser` parser is used.  Returns an
	:class:`ElementTree` instance.
	
	
	"""
	pass
	
def ProcessingInstruction(target,text=None):
	"""
	PI element factory.  This factory function creates a special element that
	will be serialized as an XML processing instruction.  *target* is a string
	containing the PI target.  *text* is a string containing the PI contents, if
	given.  Returns an element instance, representing a processing instruction.
	
	
	"""
	pass
	
def register_namespace(prefix,uri):
	"""
	Registers a namespace prefix.  The registry is global, and any existing
	mapping for either the given prefix or the namespace URI will be removed.
	*prefix* is a namespace prefix.  *uri* is a namespace uri.  Tags and
	attributes in this namespace will be serialized with the given prefix, if at
	all possible.
	
	"""
	pass
	
def SubElement(parent,tag,attrib={},extra):
	"""
	Subelement factory.  This function creates an element instance, and appends
	it to an existing element.
	
	The element name, attribute names, and attribute values can be either
	bytestrings or Unicode strings.  *parent* is the parent element.  *tag* is
	the subelement name.  *attrib* is an optional dictionary, containing element
	attributes.  *extra* contains additional attributes, given as keyword
	arguments.  Returns an element instance.
	
	
	"""
	pass
	
def tostring(element,encoding="us_ascii",method="xml"):
	"""
	Generates a string representation of an XML element, including all
	subelements.  *element* is an :class:`Element` instance.  *encoding* [1]_ is
	the output encoding (default is US-ASCII).  *method* is either ``"xml"``,
	``"html"`` or ``"text"`` (default is ``"xml"``).  Returns an encoded string
	containing the XML data.
	
	
	"""
	pass
	
def tostringlist(element,encoding="us_ascii",method="xml"):
	"""
	Generates a string representation of an XML element, including all
	subelements.  *element* is an :class:`Element` instance.  *encoding* [1]_ is
	the output encoding (default is US-ASCII).   *method* is either ``"xml"``,
	``"html"`` or ``"text"`` (default is ``"xml"``).  Returns a list of encoded
	strings containing the XML data.  It does not guarantee any specific
	sequence, except that ``"".join(tostringlist(element)) ==
	tostring(element)``.
	
	"""
	pass
	
def XML(text,parser=None):
	"""
	Parses an XML section from a string constant.  This function can be used to
	embed "XML literals" in Python code.  *text* is a string containing XML
	data.  *parser* is an optional parser instance.  If not given, the standard
	:class:`XMLParser` parser is used.  Returns an :class:`Element` instance.
	
	
	"""
	pass
	
def XMLID(text,parser=None):
	"""
	Parses an XML section from a string constant, and also returns a dictionary
	which maps from element id:s to elements.  *text* is a string containing XML
	data.  *parser* is an optional parser instance.  If not given, the standard
	:class:`XMLParser` parser is used.  Returns a tuple containing an
	:class:`Element` instance and a dictionary.
	
	
	.. lement Objects
	---------------
	
	
	"""
	pass
	
class Element:


	"""
	Element class.  This class defines the Element interface, and provides a
	reference implementation of this interface.
	
	The element name, attribute names, and attribute values can be either
	bytestrings or Unicode strings.  *tag* is the element name.  *attrib* is
	an optional dictionary, containing element attributes.  *extra* contains
	additional attributes, given as keyword arguments.
	
	
	"""
	
	
	def __init__(self, tag,attrib={},extra):
		pass
	
	


class ElementTree:


	"""
	ElementTree wrapper class.  This class represents an entire element
	hierarchy, and adds some extra support for serialization to and from
	standard XML.
	
	*element* is the root element.  The tree is initialized with the contents
	of the XML *file* if given.
	
	
	"""
	
	
	def __init__(self, element=None,file=None):
		pass
	
	


class QName:


	"""
	QName wrapper.  This can be used to wrap a QName attribute value, in order
	to get proper namespace handling on output.  *text_or_uri* is a string
	containing the QName value, in the form {uri}local, or, if the tag argument
	is given, the URI part of a QName.  If *tag* is given, the first argument is
	interpreted as an URI, and this argument is interpreted as a local name.
	:class:`QName` instances are opaque.
	
	
	.. reeBuilder Objects
	-------------------
	
	
	"""
	
	
	def __init__(self, text_or_uri,tag=None):
		pass
	
	


class TreeBuilder:


	"""
	Generic element structure builder.  This builder converts a sequence of
	start, data, and end method calls to a well-formed element structure.  You
	can use this class to build an element structure using a custom XML parser,
	or a parser for some other XML-like format.  The *element_factory* is called
	to create new :class:`Element` instances when given.
	
	
	"""
	
	
	def __init__(self, element_factory=None):
		pass
	
	


class XMLParser:


	"""
	:class:`Element` structure builder for XML source data, based on the expat
	parser.  *html* are predefined HTML entities.  This flag is not supported by
	the current implementation.  *target* is the target object.  If omitted, the
	builder uses an instance of the standard TreeBuilder class.  *encoding* [1]_
	is optional.  If given, the value overrides the encoding specified in the
	XML file.
	
	
	"""
	
	
	def __init__(self, html=0,target=None,encoding=None):
		pass
	
	


