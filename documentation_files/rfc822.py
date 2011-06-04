#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
""":synopsis: Parse 2822 style mail messages.
:deprecated:


"""
class Message:


	"""
	A :class:`Message` instance is instantiated with an input object as parameter.
	Message relies only on the input object having a :meth:`readline` method; in
	particular, ordinary file objects qualify.  Instantiation reads headers from the
	input object up to a delimiter line (normally a blank line) and stores them in
	the instance.  The message body, following the headers, is not consumed.
	
	This class can work with any input object that supports a :meth:`readline`
	method.  If the input object has seek and tell capability, the
	:meth:`rewindbody` method will work; also, illegal lines will be pushed back
	onto the input stream.  If the input object lacks seek but has an :meth:`unread`
	method that can push back a line of input, :class:`Message` will use that to
	push back illegal lines.  Thus this class can be used to parse messages coming
	from a buffered stream.
	
	The optional *seekable* argument is provided as a workaround for certain stdio
	libraries in which :cfunc:`tell` discards buffered data before discovering that
	the :cfunc:`lseek` system call doesn't work.  For maximum portability, you
	should set the seekable argument to zero to prevent that initial :meth:`tell`
	when passing in an unseekable object such as a file object created from a socket
	object.
	
	Input lines as read from the file may either be terminated by CR-LF or by a
	single linefeed; a terminating CR-LF is replaced by a single linefeed before the
	line is stored.
	
	All header matching is done independent of upper or lower case; e.g.
	``m['From']``, ``m['from']`` and ``m['FROM']`` all yield the same result.
	
	
	"""
	
	
	def __init__(self, file,seekable):
		pass
	
	


class AddressList:


	"""
	You may instantiate the :class:`AddressList` helper class using a single string
	parameter, a comma-separated list of :rfc:`2822` addresses to be parsed.  (The
	parameter ``None`` yields an empty list.)
	
	
	"""
	
	
	def __init__(self, field):
		pass
	
	def quote(str):
		"""
		Return a new string with backslashes in *str* replaced by two backslashes and
		double quotes replaced by backslash-double quote.
		
		
		"""
		pass
		
	def unquote(str):
		"""
		Return a new string which is an *unquoted* version of *str*. If *str* ends and
		begins with double quotes, they are stripped off.  Likewise if *str* ends and
		begins with angle brackets, they are stripped off.
		
		
		"""
		pass
		
	def parseaddr(address):
		"""
		Parse *address*, which should be the value of some address-containing field such
		as :mailheader:`To` or :mailheader:`Cc`, into its constituent "realname" and
		"email address" parts. Returns a tuple of that information, unless the parse
		fails, in which case a 2-tuple ``(None, None)`` is returned.
		
		
		"""
		pass
		
	def dump_address_pair(pair):
		"""
		The inverse of :meth:`parseaddr`, this takes a 2-tuple of the form ``(realname,
		email_address)`` and returns the string value suitable for a :mailheader:`To` or
		:mailheader:`Cc` header.  If the first element of *pair* is false, then the
		second element is returned unmodified.
		
		
		"""
		pass
		
	def parsedate(date):
		"""
		Attempts to parse a date according to the rules in :rfc:`2822`. however, some
		mailers don't follow that format as specified, so :func:`parsedate` tries to
		guess correctly in such cases.  *date* is a string containing an :rfc:`2822`
		date, such as  ``'Mon, 20 Nov 1995 19:12:08 -0500'``.  If it succeeds in parsing
		the date, :func:`parsedate` returns a 9-tuple that can be passed directly to
		:func:`time.mktime`; otherwise ``None`` will be returned.  Note that indexes 6,
		7, and 8 of the result tuple are not usable.
		
		
		"""
		pass
		
	def parsedate_tz(date):
		"""
		Performs the same function as :func:`parsedate`, but returns either ``None`` or
		a 10-tuple; the first 9 elements make up a tuple that can be passed directly to
		:func:`time.mktime`, and the tenth is the offset of the date's timezone from UTC
		(which is the official term for Greenwich Mean Time).  (Note that the sign of
		the timezone offset is the opposite of the sign of the ``time.timezone``
		variable for the same timezone; the latter variable follows the POSIX standard
		while this module follows :rfc:`2822`.)  If the input string has no timezone,
		the last element of the tuple returned is ``None``.  Note that indexes 6, 7, and
		8 of the result tuple are not usable.
		
		
		"""
		pass
		
	def mktime_tz(tuple):
		"""
		Turn a 10-tuple as returned by :func:`parsedate_tz` into a UTC timestamp.  If
		the timezone item in the tuple is ``None``, assume local time.  Minor
		deficiency: this first interprets the first 8 elements as a local time and then
		compensates for the timezone difference; this may yield a slight error around
		daylight savings time switch dates.  Not enough to worry about for common use.
		
		
		"""
		pass
		
	


