#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
""":synopsis: Base classes for SAX event handlers.
"""
class ContentHandler:


	"""
	This is the main callback interface in SAX, and the one most important to
	applications. The order of events in this interface mirrors the order of the
	information in the document.
	
	
	"""
	
	
	def __init__(self, ):
		pass
	
	


class DTDHandler:


	"""
	Handle DTD events.
	
	This interface specifies only those DTD events required for basic parsing
	(unparsed entities and attributes).
	
	
	"""
	
	
	def __init__(self, ):
		pass
	
	


class EntityResolver:


	"""
	Basic interface for resolving entities. If you create an object implementing
	this interface, then register the object with your Parser, the parser will call
	the method in your object to resolve all external entities.
	
	
	"""
	
	
	def __init__(self, ):
		pass
	
	


class ErrorHandler:


	"""
	Interface used by the parser to present error and warning messages to the
	application.  The methods of this object control whether errors are immediately
	converted to exceptions or are handled in some other way.
	
	In addition to these classes, :mod:`xml.sax.handler` provides symbolic constants
	for the feature and property names.
	
	
	"""
	
	
	def __init__(self, ):
		pass
	
	"""
	| value: ``"http://xml.org/sax/features/namespaces"``
	| true: Perform Namespace processing.
	| false: Optionally do not perform Namespace processing (implies
	namespace-prefixes; default).
	| access: (parsing) read-only; (not parsing) read/write
	
	
	"""
	feature_namespaces = None
	"""
	| value: ``"http://xml.org/sax/features/namespace-prefixes"``
	| true: Report the original prefixed names and attributes used for Namespace
	declarations.
	| false: Do not report attributes used for Namespace declarations, and
	optionally do not report original prefixed names (default).
	| access: (parsing) read-only; (not parsing) read/write
	
	
	"""
	feature_namespace_prefixes = None
	"""
	| value: ``"http://xml.org/sax/features/string-interning"``
	| true: All element names, prefixes, attribute names, Namespace URIs, and
	local names are interned using the built-in intern function.
	| false: Names are not necessarily interned, although they may be (default).
	| access: (parsing) read-only; (not parsing) read/write
	
	
	"""
	feature_string_interning = None
	"""
	| value: ``"http://xml.org/sax/features/validation"``
	| true: Report all validation errors (implies external-general-entities and
	external-parameter-entities).
	| false: Do not report validation errors.
	| access: (parsing) read-only; (not parsing) read/write
	
	
	"""
	feature_validation = None
	"""
	| value: ``"http://xml.org/sax/features/external-general-entities"``
	| true: Include all external general (text) entities.
	| false: Do not include external general entities.
	| access: (parsing) read-only; (not parsing) read/write
	
	
	"""
	feature_external_ges = None
	"""
	| value: ``"http://xml.org/sax/features/external-parameter-entities"``
	| true: Include all external parameter entities, including the external DTD
	subset.
	| false: Do not include any external parameter entities, even the external
	DTD subset.
	| access: (parsing) read-only; (not parsing) read/write
	
	
	"""
	feature_external_pes = None
	"""
	List of all features.
	
	
	"""
	all_features = None
	"""
	| value: ``"http://xml.org/sax/properties/lexical-handler"``
	| data type: xml.sax.sax2lib.LexicalHandler (not supported in Python 2)
	| description: An optional extension handler for lexical events like
	comments.
	| access: read/write
	
	
	"""
	property_lexical_handler = None
	"""
	| value: ``"http://xml.org/sax/properties/declaration-handler"``
	| data type: xml.sax.sax2lib.DeclHandler (not supported in Python 2)
	| description: An optional extension handler for DTD-related events other
	than notations and unparsed entities.
	| access: read/write
	
	
	"""
	property_declaration_handler = None
	"""
	| value: ``"http://xml.org/sax/properties/dom-node"``
	| data type: org.w3c.dom.Node (not supported in Python 2)
	| description: When parsing, the current DOM node being visited if this is
	a DOM iterator; when not parsing, the root DOM node for iteration.
	| access: (parsing) read-only; (not parsing) read/write
	
	
	"""
	property_dom_node = None
	"""
	| value: ``"http://xml.org/sax/properties/xml-string"``
	| data type: String
	| description: The literal string of characters that was the source for the
	current event.
	| access: read-only
	
	
	"""
	property_xml_string = None
	"""
	List of all known property names.
	
	
	.. ontentHandler Objects
	----------------------
	
	Users are expected to subclass :class:`ContentHandler` to support their
	application.  The following methods are called by the parser on the appropriate
	events in the input document:
	
	
	"""
	all_properties = None
	


