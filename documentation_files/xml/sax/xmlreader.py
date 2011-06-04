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
	
	def parse(self, source):
		"""
		Process an input source, producing SAX events. The *source* object can be a
		system identifier (a string identifying the input source -- typically a file
		name or an URL), a file-like object, or an :class:`InputSource` object. When
		:meth:`parse` returns, the input is completely processed, and the parser object
		can be discarded or reset. As a limitation, the current implementation only
		accepts byte streams; processing of character streams is for further study.
		
		
		"""
		pass
		
	def getContentHandler(self, ):
		"""
		Return the current :class:`ContentHandler`.
		
		
		"""
		pass
		
	def setContentHandler(self, handler):
		"""
		Set the current :class:`ContentHandler`.  If no :class:`ContentHandler` is set,
		content events will be discarded.
		
		
		"""
		pass
		
	def getDTDHandler(self, ):
		"""
		Return the current :class:`DTDHandler`.
		
		
		"""
		pass
		
	def setDTDHandler(self, handler):
		"""
		Set the current :class:`DTDHandler`.  If no :class:`DTDHandler` is set, DTD
		events will be discarded.
		
		
		"""
		pass
		
	def getEntityResolver(self, ):
		"""
		Return the current :class:`EntityResolver`.
		
		
		"""
		pass
		
	def setEntityResolver(self, handler):
		"""
		Set the current :class:`EntityResolver`.  If no :class:`EntityResolver` is set,
		attempts to resolve an external entity will result in opening the system
		identifier for the entity, and fail if it is not available.
		
		
		"""
		pass
		
	def getErrorHandler(self, ):
		"""
		Return the current :class:`ErrorHandler`.
		
		
		"""
		pass
		
	def setErrorHandler(self, handler):
		"""
		Set the current error handler.  If no :class:`ErrorHandler` is set, errors will
		be raised as exceptions, and warnings will be printed.
		
		
		"""
		pass
		
	def setLocale(self, locale):
		"""
		Allow an application to set the locale for errors and warnings.
		
		SAX parsers are not required to provide localization for errors and warnings; if
		they cannot support the requested locale, however, they must raise a SAX
		exception.  Applications may request a locale change in the middle of a parse.
		
		
		"""
		pass
		
	def getFeature(self, featurename):
		"""
		Return the current setting for feature *featurename*.  If the feature is not
		recognized, :exc:`SAXNotRecognizedException` is raised. The well-known
		featurenames are listed in the module :mod:`xml.sax.handler`.
		
		
		"""
		pass
		
	def setFeature(self, featurename,value):
		"""
		Set the *featurename* to *value*. If the feature is not recognized,
		:exc:`SAXNotRecognizedException` is raised. If the feature or its setting is not
		supported by the parser, *SAXNotSupportedException* is raised.
		
		
		"""
		pass
		
	def getProperty(self, propertyname):
		"""
		Return the current setting for property *propertyname*. If the property is not
		recognized, a :exc:`SAXNotRecognizedException` is raised. The well-known
		propertynames are listed in the module :mod:`xml.sax.handler`.
		
		
		"""
		pass
		
	def setProperty(self, propertyname,value):
		"""
		Set the *propertyname* to *value*. If the property is not recognized,
		:exc:`SAXNotRecognizedException` is raised. If the property or its setting is
		not supported by the parser, *SAXNotSupportedException* is raised.
		
		
		.. ncrementalParser Objects
		-------------------------
		
		Instances of :class:`IncrementalParser` offer the following additional methods:
		
		
		"""
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
	
	def feed(self, data):
		"""
		Process a chunk of *data*.
		
		
		"""
		pass
		
	def close(self, ):
		"""
		Assume the end of the document. That will check well-formedness conditions that
		can be checked only at the end, invoke handlers, and may clean up resources
		allocated during parsing.
		
		
		"""
		pass
		
	def reset(self, ):
		"""
		This method is called after close has been called to reset the parser so that it
		is ready to parse new documents. The results of calling parse or feed after
		close without calling reset are undefined.
		
		
		.. ocator Objects
		---------------
		
		Instances of :class:`Locator` provide these methods:
		
		
		"""
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
	
	def getColumnNumber(self, ):
		"""
		Return the column number where the current event ends.
		
		
		"""
		pass
		
	def getLineNumber(self, ):
		"""
		Return the line number where the current event ends.
		
		
		"""
		pass
		
	def getPublicId(self, ):
		"""
		Return the public identifier for the current event.
		
		
		"""
		pass
		
	def getSystemId(self, ):
		"""
		Return the system identifier for the current event.
		
		
		.. nputSource Objects
		-------------------
		
		
		"""
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
	
	
	def __init__(self, ):
		pass
	
	def setPublicId(self, id):
		"""
		Sets the public identifier of this :class:`InputSource`.
		
		
		"""
		pass
		
	def getPublicId(self, ):
		"""
		Returns the public identifier of this :class:`InputSource`.
		
		
		"""
		pass
		
	def setSystemId(self, id):
		"""
		Sets the system identifier of this :class:`InputSource`.
		
		
		"""
		pass
		
	def getSystemId(self, ):
		"""
		Returns the system identifier of this :class:`InputSource`.
		
		
		"""
		pass
		
	def setEncoding(self, encoding):
		"""
		Sets the character encoding of this :class:`InputSource`.
		
		The encoding must be a string acceptable for an XML encoding declaration (see
		section 4.3.3 of the XML recommendation).
		
		The encoding attribute of the :class:`InputSource` is ignored if the
		:class:`InputSource` also contains a character stream.
		
		
		"""
		pass
		
	def getEncoding(self, ):
		"""
		Get the character encoding of this InputSource.
		
		
		"""
		pass
		
	def setByteStream(self, bytefile):
		"""
		Set the byte stream (a Python file-like object which does not perform
		byte-to-character conversion) for this input source.
		
		The SAX parser will ignore this if there is also a character stream specified,
		but it will use a byte stream in preference to opening a URI connection itself.
		
		If the application knows the character encoding of the byte stream, it should
		set it with the setEncoding method.
		
		
		"""
		pass
		
	def getByteStream(self, ):
		"""
		Get the byte stream for this input source.
		
		The getEncoding method will return the character encoding for this byte stream,
		or None if unknown.
		
		
		"""
		pass
		
	def setCharacterStream(self, charfile):
		"""
		Set the character stream for this input source. (The stream must be a Python 1.6
		Unicode-wrapped file-like that performs conversion to Unicode strings.)
		
		If there is a character stream specified, the SAX parser will ignore any byte
		stream and will not attempt to open a URI connection to the system identifier.
		
		
		"""
		pass
		
	def getCharacterStream(self, ):
		"""
		Get the character stream for this input source.
		
		
		.. he :class:`Attributes` Interface
		---------------------------------
		
		:class:`Attributes` objects implement a portion of the mapping protocol,
		including the methods :meth:`copy`, :meth:`get`, :meth:`has_key`, :meth:`items`,
		:meth:`keys`, and :meth:`values`.  The following methods are also provided:
		
		
		"""
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
	
	
	def __init__(self, ):
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
	
	
	def __init__(self, ):
		pass
	
	


