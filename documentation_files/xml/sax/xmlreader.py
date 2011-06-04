#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
""":synopsis: Interface which SAX-compliant XML parsers must implement.
"""
class XMLReader:


	"""
	Base class which can be inherited by SAX parsers.
	
	
	"""
	
	
	def __init__(self, ):
		pass
	
	


class IncrementalParser:


	"""
	In some cases, it is desirable not to parse an input source at once, but to feed
	chunks of the document as they get available. Note that the reader will normally
	not read the entire file, but read it in chunks as well; still :meth:`parse`
	won't return until the entire document is processed. So these interfaces should
	be used if the blocking behaviour of :meth:`parse` is not desirable.
	
	When the parser is instantiated it is ready to begin accepting data from the
	feed method immediately. After parsing has been finished with a call to close
	the reset method must be called to make the parser ready to accept new data,
	either from feed or using the parse method.
	
	Note that these methods must *not* be called during parsing, that is, after
	parse has been called and before it returns.
	
	By default, the class also implements the parse method of the XMLReader
	interface using the feed, close and reset methods of the IncrementalParser
	interface as a convenience to SAX 2.0 driver writers.
	
	
	"""
	
	
	def __init__(self, ):
		pass
	
	


class Locator:


	"""
	Interface for associating a SAX event with a document location. A locator object
	will return valid results only during calls to DocumentHandler methods; at any
	other time, the results are unpredictable. If information is not available,
	methods may return ``None``.
	
	
	"""
	
	
	def __init__(self, ):
		pass
	
	


class InputSource:


	"""
	Encapsulation of the information needed by the :class:`XMLReader` to read
	entities.
	
	This class may include information about the public identifier, system
	identifier, byte stream (possibly with character encoding information) and/or
	the character stream of an entity.
	
	Applications will create objects of this class for use in the
	:meth:`XMLReader.parse` method and for returning from
	EntityResolver.resolveEntity.
	
	An :class:`InputSource` belongs to the application, the :class:`XMLReader` is
	not allowed to modify :class:`InputSource` objects passed to it from the
	application, although it may make copies and modify those.
	
	
	"""
	
	
	def __init__(self, systemId):
		pass
	
	


class AttributesImpl:


	"""
	This is an implementation of the :class:`Attributes` interface (see section
	:ref:`attributes-objects`).  This is a dictionary-like object which
	represents the element attributes in a :meth:`startElement` call. In addition
	to the most useful dictionary operations, it supports a number of other
	methods as described by the interface. Objects of this class should be
	instantiated by readers; *attrs* must be a dictionary-like object containing
	a mapping from attribute names to attribute values.
	
	
	"""
	
	
	def __init__(self, attrs):
		pass
	
	


class AttributesNSImpl:


	"""
	Namespace-aware variant of :class:`AttributesImpl`, which will be passed to
	:meth:`startElementNS`. It is derived from :class:`AttributesImpl`, but
	understands attribute names as two-tuples of *namespaceURI* and
	*localname*. In addition, it provides a number of methods expecting qualified
	names as they appear in the original document.  This class implements the
	:class:`AttributesNS` interface (see section :ref:`attributes-ns-objects`).
	
	
	.. MLReader Objects
	-----------------
	
	The :class:`XMLReader` interface supports the following methods:
	
	
	"""
	
	
	def __init__(self, attrs,qnames):
		pass
	
	


