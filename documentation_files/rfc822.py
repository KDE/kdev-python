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
	
	
	def __init__(self, ):
		pass
	
	def rewindbody(self, ):
		"""
		Seek to the start of the message body.  This only works if the file object is
		seekable.
		
		
		"""
		pass
		
	def isheader(self, line):
		"""
		Returns a line's canonicalized fieldname (the dictionary key that will be used
		to index it) if the line is a legal :rfc:`2822` header; otherwise returns
		``None`` (implying that parsing should stop here and the line be pushed back on
		the input stream).  It is sometimes useful to override this method in a
		subclass.
		
		
		"""
		pass
		
	def islast(self, line):
		"""
		Return true if the given line is a delimiter on which Message should stop.  The
		delimiter line is consumed, and the file object's read location positioned
		immediately after it.  By default this method just checks that the line is
		blank, but you can override it in a subclass.
		
		
		"""
		pass
		
	def iscomment(self, line):
		"""
		Return ``True`` if the given line should be ignored entirely, just skipped. By
		default this is a stub that always returns ``False``, but you can override it in
		a subclass.
		
		
		"""
		pass
		
	def getallmatchingheaders(self, name):
		"""
		Return a list of lines consisting of all headers matching *name*, if any.  Each
		physical line, whether it is a continuation line or not, is a separate list
		item.  Return the empty list if no header matches *name*.
		
		
		"""
		pass
		
	def getfirstmatchingheader(self, name):
		"""
		Return a list of lines comprising the first header matching *name*, and its
		continuation line(s), if any.  Return ``None`` if there is no header matching
		*name*.
		
		
		"""
		pass
		
	def getrawheader(self, name):
		"""
		Return a single string consisting of the text after the colon in the first
		header matching *name*.  This includes leading whitespace, the trailing
		linefeed, and internal linefeeds and whitespace if there any continuation
		line(s) were present.  Return ``None`` if there is no header matching *name*.
		
		
		"""
		pass
		
	def getheader(self, name,default):
		"""
		Return a single string consisting of the last header matching *name*,
		but strip leading and trailing whitespace.
		Internal whitespace is not stripped.  The optional *default* argument can be
		used to specify a different default to be returned when there is no header
		matching *name*; it defaults to ``None``.
		This is the preferred way to get parsed headers.
		
		
		"""
		pass
		
	def get(self, name,default):
		"""
		An alias for :meth:`getheader`, to make the interface more compatible  with
		regular dictionaries.
		
		
		"""
		pass
		
	def getaddr(self, name):
		"""
		Return a pair ``(full name, email address)`` parsed from the string returned by
		``getheader(name)``.  If no header matching *name* exists, return ``(None,
		None)``; otherwise both the full name and the address are (possibly empty)
		strings.
		
		Example: If *m*'s first :mailheader:`From` header contains the string
		``'jack@cwi.nl (Jack Jansen)'``, then ``m.getaddr('From')`` will yield the pair
		``('Jack Jansen', 'jack@cwi.nl')``. If the header contained ``'Jack Jansen
		<jack@cwi.nl>'`` instead, it would yield the exact same result.
		
		
		"""
		pass
		
	def getaddrlist(self, name):
		"""
		This is similar to ``getaddr(list)``, but parses a header containing a list of
		email addresses (e.g. a :mailheader:`To` header) and returns a list of ``(full
		name, email address)`` pairs (even if there was only one address in the header).
		If there is no header matching *name*, return an empty list.
		
		If multiple headers exist that match the named header (e.g. if there are several
		:mailheader:`Cc` headers), all are parsed for addresses. Any continuation lines
		the named headers contain are also parsed.
		
		
		"""
		pass
		
	def getdate(self, name):
		"""
		Retrieve a header using :meth:`getheader` and parse it into a 9-tuple compatible
		with :func:`time.mktime`; note that fields 6, 7, and 8  are not usable.  If
		there is no header matching *name*, or it is unparsable, return ``None``.
		
		Date parsing appears to be a black art, and not all mailers adhere to the
		standard.  While it has been tested and found correct on a large collection of
		email from many sources, it is still possible that this function may
		occasionally yield an incorrect result.
		
		
		"""
		pass
		
	def getdate_tz(self, name):
		"""
		Retrieve a header using :meth:`getheader` and parse it into a 10-tuple; the
		first 9 elements will make a tuple compatible with :func:`time.mktime`, and the
		10th is a number giving the offset of the date's timezone from UTC.  Note that
		fields 6, 7, and 8  are not usable.  Similarly to :meth:`getdate`, if there is
		no header matching *name*, or it is unparsable, return ``None``.
		
		:class:`Message` instances also support a limited mapping interface. In
		particular: ``m[name]`` is like ``m.getheader(name)`` but raises :exc:`KeyError`
		if there is no matching header; and ``len(m)``, ``m.get(name[, default])``,
		``name in m``, ``m.keys()``, ``m.values()`` ``m.items()``, and
		``m.setdefault(name[, default])`` act as expected, with the one difference
		that :meth:`setdefault` uses an empty string as the default value.
		:class:`Message` instances also support the mapping writable interface ``m[name]
		= value`` and ``del m[name]``.  :class:`Message` objects do not support the
		:meth:`clear`, :meth:`copy`, :meth:`popitem`, or :meth:`update` methods of the
		mapping interface.  (Support for :meth:`get` and :meth:`setdefault` was only
		added in Python 2.2.)
		
		Finally, :class:`Message` instances have some public instance variables:
		
		
		"""
		pass
		
	


class AddressList:


	"""
	You may instantiate the :class:`AddressList` helper class using a single string
	parameter, a comma-separated list of :rfc:`2822` addresses to be parsed.  (The
	parameter ``None`` yields an empty list.)
	
	
	"""
	
	
	def __init__(self, ):
		pass
	
	def quote(self, str):
		"""
		Return a new string with backslashes in *str* replaced by two backslashes and
		double quotes replaced by backslash-double quote.
		
		
		"""
		pass
		
	def unquote(self, str):
		"""
		Return a new string which is an *unquoted* version of *str*. If *str* ends and
		begins with double quotes, they are stripped off.  Likewise if *str* ends and
		begins with angle brackets, they are stripped off.
		
		
		"""
		pass
		
	def parseaddr(self, address):
		"""
		Parse *address*, which should be the value of some address-containing field such
		as :mailheader:`To` or :mailheader:`Cc`, into its constituent "realname" and
		"email address" parts. Returns a tuple of that information, unless the parse
		fails, in which case a 2-tuple ``(None, None)`` is returned.
		
		
		"""
		pass
		
	def dump_address_pair(self, pair):
		"""
		The inverse of :meth:`parseaddr`, this takes a 2-tuple of the form ``(realname,
		email_address)`` and returns the string value suitable for a :mailheader:`To` or
		:mailheader:`Cc` header.  If the first element of *pair* is false, then the
		second element is returned unmodified.
		
		
		"""
		pass
		
	def parsedate(self, date):
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
		
	def parsedate_tz(self, date):
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
		
	def mktime_tz(self, tuple):
		"""
		Turn a 10-tuple as returned by :func:`parsedate_tz` into a UTC timestamp.  If
		the timezone item in the tuple is ``None``, assume local time.  Minor
		deficiency: this first interprets the first 8 elements as a local time and then
		compensates for the timezone difference; this may yield a slight error around
		daylight savings time switch dates.  Not enough to worry about for common use.
		
		
		"""
		pass
		
	def __len__(self, ):
		"""
		Return the number of addresses in the address list.
		
		
		"""
		pass
		
	def __str__(self, ):
		"""
		Return a canonicalized string representation of the address list. Addresses are
		rendered in "name" <host@domain> form, comma-separated.
		
		
		"""
		pass
		
	def __add__(self, alist):
		"""
		Return a new :class:`AddressList` instance that contains all addresses in both
		:class:`AddressList` operands, with duplicates removed (set union).
		
		
		"""
		pass
		
	def __iadd__(self, alist):
		"""
		In-place version of :meth:`__add__`; turns this :class:`AddressList` instance
		into the union of itself and the right-hand instance, *alist*.
		
		
		"""
		pass
		
	def __sub__(self, alist):
		"""
		Return a new :class:`AddressList` instance that contains every address in the
		left-hand :class:`AddressList` operand that is not present in the right-hand
		address operand (set difference).
		
		
		"""
		pass
		
	def __isub__(self, alist):
		"""
		In-place version of :meth:`__sub__`, removing addresses in this list which are
		also in *alist*.
		
		Finally, :class:`AddressList` instances have one public instance variable:
		
		
		"""
		pass
		
	


