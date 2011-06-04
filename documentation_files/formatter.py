#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
""":synopsis: Generic output formatter and device interface.


"""
"""
Value which can be used in the font specification passed to the ``push_font()``
method described below, or as the new value to any other ``push_property()``
method.  Pushing the ``AS_IS`` value allows the corresponding ``pop_property()``
method to be called without having to track whether the property was changed.

The following attributes are defined for formatter instance objects:


"""
AS_IS = None
class NullFormatter:


	"""
	A formatter which does nothing.  If *writer* is omitted, a :class:`NullWriter`
	instance is created.  No methods of the writer are called by
	:class:`NullFormatter` instances.  Implementations should inherit from this
	class if implementing a writer interface but don't need to inherit any
	implementation.
	
	
	"""
	
	
	def __init__(self, writer):
		pass
	
	


class AbstractFormatter:


	"""
	The standard formatter.  This implementation has demonstrated wide applicability
	to many writers, and may be used directly in most circumstances.  It has been
	used to implement a full-featured World Wide Web browser.
	
	
	.. he Writer Interface
	--------------------
	
	Interfaces to create writers are dependent on the specific writer class being
	instantiated.  The interfaces described below are the required interfaces which
	all writers must support once initialized. Note that while most applications can
	use the :class:`AbstractFormatter` class as a formatter, the writer must
	typically be provided by the application.
	
	
	"""
	
	
	def __init__(self, writer):
		pass
	
	


class NullWriter:


	"""
	A writer which only provides the interface definition; no actions are taken on
	any methods.  This should be the base class for all writers which do not need to
	inherit any implementation methods.
	
	
	"""
	
	
	def __init__(self, ):
		pass
	
	


class AbstractWriter:


	"""
	A writer which can be used in debugging formatters, but not much else.  Each
	method simply announces itself by printing its name and arguments on standard
	output.
	
	
	"""
	
	
	def __init__(self, ):
		pass
	
	


