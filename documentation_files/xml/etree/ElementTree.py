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
	
def SubElement(parent,tag,attrib,extra):
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
	
	
	def __init__(self, ):
		pass
	
	def clear(self, ):
		"""
		Resets an element.  This function removes all subelements, clears all
		attributes, and sets the text and tail attributes to None.
		
		
		"""
		pass
		
	def get(self, key,default=None):
		"""
		Gets the element attribute named *key*.
		
		Returns the attribute value, or *default* if the attribute was not found.
		
		
		"""
		pass
		
	def items(self, ):
		"""
		Returns the element attributes as a sequence of (name, value) pairs.  The
		attributes are returned in an arbitrary order.
		
		
		"""
		pass
		
	def keys(self, ):
		"""
		Returns the elements attribute names as a list.  The names are returned
		in an arbitrary order.
		
		
		"""
		pass
		
	def set(self, key,value):
		"""
		Set the attribute *key* on the element to *value*.
		
		The following methods work on the element's children (subelements).
		
		
		"""
		pass
		
	def append(self, subelement):
		"""
		Adds the element *subelement* to the end of this elements internal list
		of subelements.
		
		
		"""
		pass
		
	def extend(self, subelements):
		"""
		Appends *subelements* from a sequence object with zero or more elements.
		Raises :exc:`AssertionError` if a subelement is not a valid object.
		
		"""
		pass
		
	def find(self, match):
		"""
		Finds the first subelement matching *match*.  *match* may be a tag name
		or path.  Returns an element instance or ``None``.
		
		
		"""
		pass
		
	def findall(self, match):
		"""
		Finds all matching subelements, by tag name or path.  Returns a list
		containing all matching elements in document order.
		
		
		"""
		pass
		
	def findtext(self, match,default=None):
		"""
		Finds text for the first subelement matching *match*.  *match* may be
		a tag name or path.  Returns the text content of the first matching
		element, or *default* if no element was found.  Note that if the matching
		element has no text content an empty string is returned.
		
		
		"""
		pass
		
	def getchildren(self, ):
		"""
		"""
		pass
		
	def getiterator(self, tag=None):
		"""
		"""
		pass
		
	def insert(self, index,element):
		"""
		Inserts a subelement at the given position in this element.
		
		
		"""
		pass
		
	def iter(self, tag=None):
		"""
		Creates a tree :term:`iterator` with the current element as the root.
		The iterator iterates over this element and all elements below it, in
		document (depth first) order.  If *tag* is not ``None`` or ``'*'``, only
		elements whose tag equals *tag* are returned from the iterator.  If the
		tree structure is modified during iteration, the result is undefined.
		
		
		"""
		pass
		
	def iterfind(self, match):
		"""
		Finds all matching subelements, by tag name or path.  Returns an iterable
		yielding all matching elements in document order.
		
		"""
		pass
		
	def itertext(self, ):
		"""
		Creates a text iterator.  The iterator loops over this element and all
		subelements, in document order, and returns all inner text.
		
		"""
		pass
		
	def makeelement(self, tag,attrib):
		"""
		Creates a new element object of the same type as this element.  Do not
		call this method, use the :func:`SubElement` factory function instead.
		
		
		"""
		pass
		
	def remove(self, subelement):
		"""
		Removes *subelement* from the element.  Unlike the find\* methods this
		method compares elements based on the instance identity, not on tag value
		or contents.
		
		:class:`Element` objects also support the following sequence type methods
		for working with subelements: :meth:`__delitem__`, :meth:`__getitem__`,
		:meth:`__setitem__`, :meth:`__len__`.
		
		Caution: Elements with no subelements will test as ``False``.  This behavior
		will change in future versions.  Use specific ``len(elem)`` or ``elem is
		None`` test instead. ::
		
		element = root.find('foo')
		
		if not element:  # careful!
		print "element not found, or element has no subelements"
		
		if element is None:
		print "element not found"
		
		
		.. lementTree Objects
		"""
		pass
		
	


class ElementTree:


	"""
	ElementTree wrapper class.  This class represents an entire element
	hierarchy, and adds some extra support for serialization to and from
	standard XML.
	
	*element* is the root element.  The tree is initialized with the contents
	of the XML *file* if given.
	
	
	"""
	
	
	def __init__(self, ):
		pass
	
	def _setroot(self, element):
		"""
		Replaces the root element for this tree.  This discards the current
		contents of the tree, and replaces it with the given element.  Use with
		care.  *element* is an element instance.
		
		
		"""
		pass
		
	def find(self, match):
		"""
		Finds the first toplevel element matching *match*.  *match* may be a tag
		name or path.  Same as getroot().find(match).  Returns the first matching
		element, or ``None`` if no element was found.
		
		
		"""
		pass
		
	def findall(self, match):
		"""
		Finds all matching subelements, by tag name or path.  Same as
		getroot().findall(match).  *match* may be a tag name or path.  Returns a
		list containing all matching elements, in document order.
		
		
		"""
		pass
		
	def findtext(self, match,default=None):
		"""
		Finds the element text for the first toplevel element with given tag.
		Same as getroot().findtext(match).  *match* may be a tag name or path.
		*default* is the value to return if the element was not found.  Returns
		the text content of the first matching element, or the default value no
		element was found.  Note that if the element is found, but has no text
		content, this method returns an empty string.
		
		
		"""
		pass
		
	def getiterator(self, tag=None):
		"""
		"""
		pass
		
	def getroot(self, ):
		"""
		Returns the root element for this tree.
		
		
		"""
		pass
		
	def iter(self, tag=None):
		"""
		Creates and returns a tree iterator for the root element.  The iterator
		loops over all elements in this tree, in section order.  *tag* is the tag
		to look for (default is to return all elements)
		
		
		"""
		pass
		
	def iterfind(self, match):
		"""
		Finds all matching subelements, by tag name or path.  Same as
		getroot().iterfind(match). Returns an iterable yielding all matching
		elements in document order.
		
		"""
		pass
		
	def parse(self, source,parser=None):
		"""
		Loads an external XML section into this element tree.  *source* is a file
		name or file object.  *parser* is an optional parser instance.  If not
		given, the standard XMLParser parser is used.  Returns the section
		root element.
		
		
		"""
		pass
		
	def write(self, file,encoding="us_ascii",xml_declaration=None,method="xml"):
		"""
		Writes the element tree to a file, as XML.  *file* is a file name, or a
		file object opened for writing.  *encoding* [1]_ is the output encoding
		(default is US-ASCII).  *xml_declaration* controls if an XML declaration
		should be added to the file.  Use False for never, True for always, None
		for only if not US-ASCII or UTF-8 (default is None).  *method* is either
		``"xml"``, ``"html"`` or ``"text"`` (default is ``"xml"``).  Returns an
		encoded string.
		
		This is the XML file that is going to be manipulated::
		"""
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
	
	
	def __init__(self, ):
		pass
	
	


class TreeBuilder:


	"""
	Generic element structure builder.  This builder converts a sequence of
	start, data, and end method calls to a well-formed element structure.  You
	can use this class to build an element structure using a custom XML parser,
	or a parser for some other XML-like format.  The *element_factory* is called
	to create new :class:`Element` instances when given.
	
	
	"""
	
	
	def __init__(self, ):
		pass
	
	def close(self, ):
		"""
		Flushes the builder buffers, and returns the toplevel document
		element.  Returns an :class:`Element` instance.
		
		
		"""
		pass
		
	def data(self, data):
		"""
		Adds text to the current element.  *data* is a string.  This should be
		either a bytestring, or a Unicode string.
		
		
		"""
		pass
		
	def end(self, tag):
		"""
		Closes the current element.  *tag* is the element name.  Returns the
		closed element.
		
		
		"""
		pass
		
	def start(self, tag,attrs):
		"""
		Opens a new element.  *tag* is the element name.  *attrs* is a dictionary
		containing element attributes.  Returns the opened element.
		
		
		In addition, a custom :class:`TreeBuilder` object can provide the
		following method:
		
		"""
		pass
		
	def doctype(self, name,pubid,system):
		"""
		Handles a doctype declaration.  *name* is the doctype name.  *pubid* is
		the public identifier.  *system* is the system identifier.  This method
		does not exist on the default :class:`TreeBuilder` class.
		
		"""
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
	
	
	def __init__(self, ):
		pass
	
	def close(self, ):
		"""
		Finishes feeding data to the parser.  Returns an element structure.
		
		
		"""
		pass
		
	def doctype(self, name,pubid,system):
		"""
		"""
		pass
		
	def feed(self, data):
		"""
		Feeds data to the parser.  *data* is encoded data.
		
		:meth:`XMLParser.feed` calls *target*\'s :meth:`start` method
		"""
		pass
		
	


