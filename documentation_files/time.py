#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
""":synopsis: Time access and conversions.


This module provides various time-related functions. For related
functionality, see also the :mod:`datetime` and :mod:`calendar` modules.

Although this module is always available,
not all functions are available on all platforms.  Most of the functions
defined in this module call platform C library functions with the same name.  It
may sometimes be helpful to consult the platform documentation, because the
semantics of these functions varies among platforms.

An explanation of some terminology and conventions is in order.

"""
"""
Boolean value indicating whether two-digit year values will be accepted.  This
is true by default, but will be set to false if the environment variable
:envvar:`PYTHONY2K` has been set to a non-empty string.  It may also be modified
at run time.


"""
accept2dyear = None
"""
The offset of the local DST timezone, in seconds west of UTC, if one is defined.
This is negative if the local DST timezone is east of UTC (as in Western Europe,
including the UK).  Only use this if ``daylight`` is nonzero.


"""
altzone = None
"""
Nonzero if a DST timezone is defined.


"""
daylight = None
def asctime(t):
	"""
	Convert a tuple or :class:`struct_time` representing a time as returned by
	:func:`gmtime` or :func:`localtime` to a 24-character string of the following
	form: ``'Sun Jun 20 23:21:05 1993'``.  If *t* is not provided, the current time
	as returned by :func:`localtime` is used. Locale information is not used by
	:func:`asctime`.
	
	"""
	pass
	
def clock():
	"""
	"""
	pass
	
def ctime(secs):
	"""
	Convert a time expressed in seconds since the epoch to a string representing
	local time. If *secs* is not provided or :const:`None`, the current time as
	returned by :func:`time` is used.  ``ctime(secs)`` is equivalent to
	``asctime(localtime(secs))``. Locale information is not used by :func:`ctime`.
	
	"""
	pass
	
def gmtime(secs):
	"""
	Convert a time expressed in seconds since the epoch to a :class:`struct_time` in
	UTC in which the dst flag is always zero.  If *secs* is not provided or
	:const:`None`, the current time as returned by :func:`time` is used.  Fractions
	of a second are ignored.  See above for a description of the
	:class:`struct_time` object. See :func:`calendar.timegm` for the inverse of this
	function.
	
	"""
	pass
	
def localtime(secs):
	"""
	Like :func:`gmtime` but converts to local time.  If *secs* is not provided or
	:const:`None`, the current time as returned by :func:`time` is used.  The dst
	flag is set to ``1`` when DST applies to the given time.
	
	"""
	pass
	
def mktime(t):
	"""
	This is the inverse function of :func:`localtime`.  Its argument is the
	:class:`struct_time` or full 9-tuple (since the dst flag is needed; use ``-1``
	as the dst flag if it is unknown) which expresses the time in *local* time, not
	UTC.  It returns a floating point number, for compatibility with :func:`time`.
	If the input value cannot be represented as a valid time, either
	:exc:`OverflowError` or :exc:`ValueError` will be raised (which depends on
	whether the invalid value is caught by Python or the underlying C libraries).
	The earliest date for which it can generate a time is platform-dependent.
	
	
	"""
	pass
	
def sleep(secs):
	"""
	Suspend execution for the given number of seconds.  The argument may be a
	floating point number to indicate a more precise sleep time. The actual
	suspension time may be less than that requested because any caught signal will
	terminate the :func:`sleep` following execution of that signal's catching
	routine.  Also, the suspension time may be longer than requested by an arbitrary
	amount because of the scheduling of other activity in the system.
	
	
	"""
	pass
	
def strftime(format,t):
	"""
	Convert a tuple or :class:`struct_time` representing a time as returned by
	:func:`gmtime` or :func:`localtime` to a string as specified by the *format*
	argument.  If *t* is not provided, the current time as returned by
	:func:`localtime` is used.  *format* must be a string.  :exc:`ValueError` is
	raised if any field in *t* is outside of the allowed range.
	
	"""
	pass
	
def strptime(string,format):
	"""
	Parse a string representing a time according to a format.  The return  value is
	a :class:`struct_time` as returned by :func:`gmtime` or :func:`localtime`.
	
	The *format* parameter uses the same directives as those used by
	:func:`strftime`; it defaults to ``"%a %b %d %H:%M:%S %Y"`` which matches the
	formatting returned by :func:`ctime`. If *string* cannot be parsed according to
	*format*, or if it has excess data after parsing, :exc:`ValueError` is raised.
	The default values used to fill in any missing data when more accurate values
	cannot be inferred are ``(1900, 1, 1, 0, 0, 0, 0, 1, -1)``.
	
	For example:
	
	>>> import time
	>>> time.strptime("30 Nov 00", "%d %b %y")   # doctest: +NORMALIZE_WHITESPACE
	time.struct_time(tm_year=2000, tm_mon=11, tm_mday=30, tm_hour=0, tm_min=0,
	tm_sec=0, tm_wday=3, tm_yday=335, tm_isdst=-1)
	
	Support for the ``%Z`` directive is based on the values contained in ``tzname``
	and whether ``daylight`` is true.  Because of this, it is platform-specific
	except for recognizing UTC and GMT which are always known (and are considered to
	be non-daylight savings timezones).
	
	Only the directives specified in the documentation are supported.  Because
	``strftime()`` is implemented per platform it can sometimes offer more
	directives than those listed.  But ``strptime()`` is independent of any platform
	and thus does not necessarily support all directives available that are not
	documented as supported.
	
	
	"""
	pass
	
class struct_time:


	"""
	The type of the time value sequence returned by :func:`gmtime`,
	:func:`localtime`, and :func:`strptime`.  It is an object with a :term:`named
	tuple` interface: values can be accessed by index and by attribute name.  The
	following values are present:
	
	+-------+-------------------+---------------------------------+
	| Index | Attribute         | Values                          |
	+=======+===================+=================================+
	| 0     | :attr:`tm_year`   | (for example, 1993)             |
	+-------+-------------------+---------------------------------+
	| 1     | :attr:`tm_mon`    | range [1, 12]                   |
	+-------+-------------------+---------------------------------+
	| 2     | :attr:`tm_mday`   | range [1, 31]                   |
	+-------+-------------------+---------------------------------+
	| 3     | :attr:`tm_hour`   | range [0, 23]                   |
	+-------+-------------------+---------------------------------+
	| 4     | :attr:`tm_min`    | range [0, 59]                   |
	+-------+-------------------+---------------------------------+
	| 5     | :attr:`tm_sec`    | range [0, 61]; see **(1)** in   |
	|       |                   | :func:`strftime` description    |
	+-------+-------------------+---------------------------------+
	| 6     | :attr:`tm_wday`   | range [0, 6], Monday is 0       |
	+-------+-------------------+---------------------------------+
	| 7     | :attr:`tm_yday`   | range [1, 366]                  |
	+-------+-------------------+---------------------------------+
	| 8     | :attr:`tm_isdst`  | 0, 1 or -1; see below           |
	+-------+-------------------+---------------------------------+
	
	"""
	
	
	def __init__(self, ):
		pass
	
	def time():
		"""
		Return the time as a floating point number expressed in seconds since the epoch,
		in UTC.  Note that even though the time is always returned as a floating point
		number, not all systems provide time with a better precision than 1 second.
		While this function normally returns non-decreasing values, it can return a
		lower value than a previous call if the system clock has been set back between
		the two calls.
		
		
		"""
		pass
		
	def tzset():
		"""
		Resets the time conversion rules used by the library routines. The environment
		variable :envvar:`TZ` specifies how this is done.
		
		"""
		pass
		
	"""
	The offset of the local (non-DST) timezone, in seconds west of UTC (negative in
	most of Western Europe, positive in the US, zero in the UK).
	
	
	"""
	timezone = None
	"""
	A tuple of two strings: the first is the name of the local non-DST timezone, the
	second is the name of the local DST timezone.  If no DST timezone is defined,
	the second string should not be used.
	
	
	"""
	tzname = None
	


