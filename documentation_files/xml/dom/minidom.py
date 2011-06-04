#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
""":synopsis: Lightweight Document Object Model (DOM) implementation.
"""
def parse(filename_or_file,parser,bufsize):
	"""
	Return a :class:`Document` from the given input. *filename_or_file* may be
	either a file name, or a file-like object. *parser*, if given, must be a SAX2
	parser object. This function will change the document handler of the parser and
	activate namespace support; other parser configuration (like setting an entity
	resolver) must have been done in advance.
	
	If you have XML in a string, you can use the :func:`parseString` function
	instead:
	
	
	"""
	pass
	
def parseString(string,parser):
	"""
	Return a :class:`Document` that represents the *string*. This method creates a
	:class:`StringIO` object for the string and passes that on to :func:`parse`.
	
	Both functions return a :class:`Document` object representing the content of the
	document.
	
	What the :func:`parse` and :func:`parseString` functions do is connect an XML
	parser with a "DOM builder" that can accept parse events from any SAX parser and
	convert them into a DOM tree.  The name of the functions are perhaps misleading,
	but are easy to grasp when learning the interfaces.  The parsing of the document
	will be completed before these functions return; it's simply that these
	functions do not provide a parser implementation themselves.
	
	You can also create a :class:`Document` by calling a method on a "DOM
	Implementation" object.  You can get this object either by calling the
	:func:`getDOMImplementation` function in the :mod:`xml.dom` package or the
	:mod:`xml.dom.minidom` module. Using the implementation from the
	:mod:`xml.dom.minidom` module will always return a :class:`Document` instance
	from the minidom implementation, while the version from :mod:`xml.dom` may
	provide an alternate implementation (this is likely if you have the `PyXML
	package <http://pyxml.sourceforge.net/>`_ installed).  Once you have a
	:class:`Document`, you can add child nodes to it to populate the DOM::
	
	from xml.dom.minidom import getDOMImplementation
	
	impl = getDOMImplementation()
	
	newdoc = impl.createDocument(None, "some_tag", None)
	top_element = newdoc.documentElement
	text = newdoc.createTextNode('Some textual content.')
	top_element.appendChild(text)
	
	Once you have a DOM document object, you can access the parts of your XML
	document through its properties and methods.  These properties are defined in
	the DOM specification.  The main property of the document object is the
	:attr:`documentElement` property.  It gives you the main element in the XML
	document: the one that holds all others.  Here is an example program::
	
	dom3 = parseString("<myxml>Some data</myxml>")
	assert dom3.documentElement.tagName == "myxml"
	
	When you are finished with a DOM tree, you may optionally call the
	:meth:`unlink` method to encourage early cleanup of the now-unneeded
	objects.  :meth:`unlink` is a :mod:`xml.dom.minidom`\ -specific
	extension to the DOM API that renders the node and its descendants are
	essentially useless.  Otherwise, Python's garbage collector will
	eventually take care of the objects in the tree.
	
	"""
	pass
	
