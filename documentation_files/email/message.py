#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
""":synopsis: The base class representing email messages.


The central class in the :mod:`email` package is the :class:`Message` class,
imported from the :mod:`email.message` module.  It is the base class for the
:mod:`email` object model.  :class:`Message` provides the core functionality for
setting and querying header fields, and for accessing message bodies.

Conceptually, a :class:`Message` object consists of *headers* and *payloads*.
Headers are :rfc:`2822` style field names and values where the field name and
value are separated by a colon.  The colon is not part of either the field name
or the field value.

Headers are stored and returned in case-preserving form but are matched
case-insensitively.  There may also be a single envelope header, also known as
the *Unix-From* header or the ``From_`` header.  The payload is either a string
in the case of simple message objects or a list of :class:`Message` objects for
MIME container documents (e.g. :mimetype:`multipart/\*` and
:mimetype:`message/rfc822`).

:class:`Message` objects provide a mapping style interface for accessing the
message headers, and an explicit interface for accessing both the headers and
the payload.  It provides convenience methods for generating a flat text
representation of the message object tree, for accessing commonly used header
parameters, and for recursively walking over the object tree.

Here are the methods of the :class:`Message` class:


"""
class Message:


	"""
	The constructor takes no arguments.
	
	
	"""
	
	
	def __init__(self, ):
		pass
	
	


