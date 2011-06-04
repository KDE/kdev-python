#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
""":synopsis: Package containing SAX2 base classes and convenience functions.
"""
def make_parser(parser_list):
	"""
	Create and return a SAX :class:`XMLReader` object.  The first parser found will
	be used.  If *parser_list* is provided, it must be a sequence of strings which
	name modules that have a function named :func:`create_parser`.  Modules listed
	in *parser_list* will be used before modules in the default list of parsers.
	
	
	"""
	pass
	
def parse(filename_or_stream,handler,error_handler):
	"""
	Create a SAX parser and use it to parse a document.  The document, passed in as
	*filename_or_stream*, can be a filename or a file object.  The *handler*
	parameter needs to be a SAX :class:`ContentHandler` instance.  If
	*error_handler* is given, it must be a SAX :class:`ErrorHandler` instance; if
	omitted,  :exc:`SAXParseException` will be raised on all errors.  There is no
	return value; all work must be done by the *handler* passed in.
	
	
	"""
	pass
	
def parseString(string,handler,error_handler):
	"""
	Similar to :func:`parse`, but parses from a buffer *string* received as a
	parameter.
	
	A typical SAX application uses three kinds of objects: readers, handlers and
	input sources.  "Reader" in this context is another term for parser, i.e. some
	piece of code that reads the bytes or characters from the input source, and
	produces a sequence of events. The events then get distributed to the handler
	objects, i.e. the reader invokes a method on the handler.  A SAX application
	must therefore obtain a reader object, create or open the input sources, create
	the handlers, and connect these objects all together.  As the final step of
	preparation, the reader is called to parse the input. During parsing, methods on
	the handler objects are called based on structural and syntactic events from the
	input data.
	
	For these objects, only the interfaces are relevant; they are normally not
	instantiated by the application itself.  Since Python does not have an explicit
	notion of interface, they are formally introduced as classes, but applications
	may use implementations which do not inherit from the provided classes.  The
	:class:`InputSource`, :class:`Locator`, :class:`Attributes`,
	:class:`AttributesNS`, and :class:`XMLReader` interfaces are defined in the
	module :mod:`xml.sax.xmlreader`.  The handler interfaces are defined in
	:mod:`xml.sax.handler`.  For convenience, :class:`InputSource` (which is often
	instantiated directly) and the handler classes are also available from
	:mod:`xml.sax`.  These interfaces are described below.
	
	In addition to these classes, :mod:`xml.sax` provides the following exception
	classes.
	
	
	"""
	pass
	
