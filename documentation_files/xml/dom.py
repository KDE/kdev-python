#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
""":synopsis: Document Object Model API for Python.
"""
"""
The value used to indicate that no namespace is associated with a node in the
DOM.  This is typically found as the :attr:`namespaceURI` of a node, or used as
the *namespaceURI* parameter to a namespaces-specific method.

"""
EMPTY_NAMESPACE = None
"""
The namespace URI associated with the reserved prefix ``xml``, as defined by
`Namespaces in XML <http://www.w3.org/TR/REC-xml-names/>`_ (section 4).

"""
XML_NAMESPACE = None
"""
The namespace URI for namespace declarations, as defined by `Document Object
Model (DOM) Level 2 Core Specification
<http://www.w3.org/TR/DOM-Level-2-Core/core.html>`_ (section 1.1.8).

"""
XMLNS_NAMESPACE = None
"""
The URI of the XHTML namespace as defined by `XHTML 1.0: The Extensible
HyperText Markup Language <http://www.w3.org/TR/xhtml1/>`_ (section 3.1.1).

"""
XHTML_NAMESPACE = None
def registerDOMImplementation(name,factory):
	"""
	Register the *factory* function with the name *name*.  The factory function
	should return an object which implements the :class:`DOMImplementation`
	interface.  The factory function can return the same object every time, or a new
	one for each call, as appropriate for the specific implementation (e.g. if that
	implementation supports some customization).
	
	
	"""
	pass
	
def getDOMImplementation(name,features):
	"""
	Return a suitable DOM implementation. The *name* is either well-known, the
	module name of a DOM implementation, or ``None``. If it is not ``None``, imports
	the corresponding module and returns a :class:`DOMImplementation` object if the
	import succeeds.  If no name is given, and if the environment variable
	:envvar:`PYTHON_DOM` is set, this variable is used to find the implementation.
	
	If name is not given, this examines the available implementations to find one
	with the required feature set.  If no implementation can be found, raise an
	:exc:`ImportError`.  The features list must be a sequence of ``(feature,
	version)`` pairs which are passed to the :meth:`hasFeature` method on available
	:class:`DOMImplementation` objects.
	
	Some convenience constants are also provided:
	
	
	"""
	pass
	
