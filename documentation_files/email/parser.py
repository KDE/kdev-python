#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
""":synopsis: Parse flat text email messages to produce a message object structure.


Message object structures can be created in one of two ways: they can be created
from whole cloth by instantiating :class:`~email.message.Message` objects and
stringing them together via :meth:`attach` and :meth:`set_payload` calls, or they
can be created by parsing a flat text representation of the email message.

The :mod:`email` package provides a standard parser that understands most email
document structures, including MIME documents.  You can pass the parser a string
or a file object, and the parser will return to you the root
:class:`~email.message.Message` instance of the object structure.  For simple,
non-MIME messages the payload of this root object will likely be a string
containing the text of the message.  For MIME messages, the root object will
return ``True`` from its :meth:`is_multipart` method, and the subparts can be
accessed via the :meth:`get_payload` and :meth:`walk` methods.

There are actually two parser interfaces available for use, the classic
:class:`Parser` API and the incremental :class:`FeedParser` API.  The classic
:class:`Parser` API is fine if you have the entire text of the message in memory
as a string, or if the entire message lives in a file on the file system.
:class:`FeedParser` is more appropriate for when you're reading the message from
a stream which might block waiting for more input (e.g. reading an email message
from a socket).  The :class:`FeedParser` can consume and parse the message
incrementally, and only returns the root object when you close the parser [#]_.

Note that the parser can be extended in limited ways, and of course you can
implement your own parser completely from scratch.  There is no magical
connection between the :mod:`email` package's bundled parser and the
:class:`~email.message.Message` class, so your custom parser can create message
object trees any way it finds necessary.


FeedParser API
^^^^^^^^^^^^^^

"""
class FeedParser:


	"""
	Create a :class:`FeedParser` instance.  Optional *_factory* is a no-argument
	callable that will be called whenever a new message object is needed.  It
	defaults to the :class:`email.message.Message` class.
	
	
	"""
	
	
	def __init__(self, ):
		pass
	
	def feed(self, data):
		"""
		Feed the :class:`FeedParser` some more data.  *data* should be a string
		containing one or more lines.  The lines can be partial and the
		:class:`FeedParser` will stitch such partial lines together properly.  The
		lines in the string can have any of the common three line endings,
		carriage return, newline, or carriage return and newline (they can even be
		mixed).
		
		
		"""
		pass
		
	def close(self, ):
		"""
		Closing a :class:`FeedParser` completes the parsing of all previously fed
		data, and returns the root message object.  It is undefined what happens
		if you feed more data to a closed :class:`FeedParser`.
		
		
		Parser class API
		"""
		pass
		
	


class Parser:


	"""
	The constructor for the :class:`Parser` class takes an optional argument
	*_class*.  This must be a callable factory (such as a function or a class), and
	it is used whenever a sub-message object needs to be created.  It defaults to
	:class:`~email.message.Message` (see :mod:`email.message`).  The factory will
	be called without arguments.
	
	The optional *strict* flag is ignored.
	
	"""
	
	
	def __init__(self, ):
		pass
	
	def parse(self, fp,headersonly):
		"""
		Read all the data from the file-like object *fp*, parse the resulting
		text, and return the root message object.  *fp* must support both the
		:meth:`readline` and the :meth:`read` methods on file-like objects.
		
		The text contained in *fp* must be formatted as a block of :rfc:`2822`
		style headers and header continuation lines, optionally preceded by a
		envelope header.  The header block is terminated either by the end of the
		data or by a blank line.  Following the header block is the body of the
		message (which may contain MIME-encoded subparts).
		
		Optional *headersonly* is as with the :meth:`parse` method.
		
		"""
		pass
		
	def parsestr(self, text,headersonly):
		"""
		Similar to the :meth:`parse` method, except it takes a string object
		instead of a file-like object.  Calling this method on a string is exactly
		equivalent to wrapping *text* in a :class:`StringIO` instance first and
		calling :meth:`parse`.
		
		Optional *headersonly* is a flag specifying whether to stop parsing after
		reading the headers or not.  The default is ``False``, meaning it parses
		the entire contents of the file.
		
		"""
		pass
		
	def message__from_string(self, s,__class,strict):
		"""
		Return a message object structure from a string.  This is exactly equivalent to
		``Parser().parsestr(s)``.  Optional *_class* and *strict* are interpreted as
		with the :class:`Parser` class constructor.
		
		"""
		pass
		
	def message__from_file(self, fp,__class,strict):
		"""
		Return a message object structure tree from an open file object.  This is
		exactly equivalent to ``Parser().parse(fp)``.  Optional *_class* and *strict*
		are interpreted as with the :class:`Parser` class constructor.
		
		"""
		pass
		
	


