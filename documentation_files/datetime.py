#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
""":synopsis: Basic date and time types.
"""
"""
The smallest year number allowed in a :class:`date` or :class:`datetime` object.
:const:`MINYEAR` is ``1``.


"""
MINYEAR = None
"""
The largest year number allowed in a :class:`date` or :class:`datetime` object.
:const:`MAXYEAR` is ``9999``.


"""
MAXYEAR = None
class date:


	""":noindex:
	
	An idealized naive date, assuming the current Gregorian calendar always was, and
	always will be, in effect. Attributes: :attr:`year`, :attr:`month`, and
	:attr:`day`.
	
	
	"""
	
	
	def __init__(self, ):
		pass
	
	


class time:


	""":noindex:
	
	An idealized time, independent of any particular day, assuming that every day
	has exactly 24\*60\*60 seconds (there is no notion of "leap seconds" here).
	Attributes: :attr:`hour`, :attr:`minute`, :attr:`second`, :attr:`microsecond`,
	and :attr:`tzinfo`.
	
	
	"""
	
	
	def __init__(self, ):
		pass
	
	


class datetime:


	""":noindex:
	
	A combination of a date and a time. Attributes: :attr:`year`, :attr:`month`,
	:attr:`day`, :attr:`hour`, :attr:`minute`, :attr:`second`, :attr:`microsecond`,
	and :attr:`tzinfo`.
	
	
	"""
	
	
	def __init__(self, ):
		pass
	
	


class timedelta:


	""":noindex:
	
	A duration expressing the difference between two :class:`date`, :class:`time`,
	or :class:`datetime` instances to microsecond resolution.
	
	
	"""
	
	
	def __init__(self, ):
		pass
	
	


class tzinfo:


	"""
	An abstract base class for time zone information objects.  These are used by the
	:class:`datetime` and :class:`time` classes to provide a customizable notion of
	time adjustment (for example, to account for time zone and/or daylight saving
	time).
	
	Objects of these types are immutable.
	
	Objects of the :class:`date` type are always naive.
	
	An object *d* of type :class:`time` or :class:`datetime` may be naive or aware.
	*d* is aware if ``d.tzinfo`` is not ``None`` and ``d.tzinfo.utcoffset(d)`` does
	not return ``None``.  If ``d.tzinfo`` is ``None``, or if ``d.tzinfo`` is not
	``None`` but ``d.tzinfo.utcoffset(d)`` returns ``None``, *d* is naive.
	
	The distinction between naive and aware doesn't apply to :class:`timedelta`
	objects.
	
	Subclass relationships::
	
	object
	timedelta
	tzinfo
	time
	date
	datetime
	
	
	.. class:`timedelta` Objects
	--------------------------
	
	A :class:`timedelta` object represents a duration, the difference between two
	dates or times.
	
	"""
	
	
	def __init__(self, ):
		pass
	
	


class timedelta:


	"""
	All arguments are optional and default to ``0``.  Arguments may be ints, longs,
	or floats, and may be positive or negative.
	
	Only *days*, *seconds* and *microseconds* are stored internally.  Arguments are
	converted to those units:
	
	* A millisecond is converted to 1000 microseconds.
	* A minute is converted to 60 seconds.
	* An hour is converted to 3600 seconds.
	* A week is converted to 7 days.
	
	and days, seconds and microseconds are then normalized so that the
	representation is unique, with
	
	* ``0 <= microseconds < 1000000``
	* ``0 <= seconds < 3600*24`` (the number of seconds in one day)
	* ``-999999999 <= days <= 999999999``
	
	If any argument is a float and there are fractional microseconds, the fractional
	microseconds left over from all arguments are combined and their sum is rounded
	to the nearest microsecond.  If no argument is a float, the conversion and
	normalization processes are exact (no information is lost).
	
	If the normalized value of days lies outside the indicated range,
	:exc:`OverflowError` is raised.
	
	Note that normalization of negative values may be surprising at first. For
	example,
	
	>>> from datetime import timedelta
	>>> d = timedelta(microseconds=-1)
	>>> (d.days, d.seconds, d.microseconds)
	(-1, 86399, 999999)
	
	
	Class attributes are:
	
	"""
	
	
	def __init__(self, days,seconds,microseconds,milliseconds,minutes,hours,weeks):
		pass
	
	


class date:


	"""
	All arguments are required.  Arguments may be ints or longs, in the following
	ranges:
	
	* ``MINYEAR <= year <= MAXYEAR``
	* ``1 <= month <= 12``
	* ``1 <= day <= number of days in the given month and year``
	
	If an argument outside those ranges is given, :exc:`ValueError` is raised.
	
	
	Other constructors, all class methods:
	
	"""
	
	
	def __init__(self, year,month,day):
		pass
	
	


class datetime:


	"""
	The year, month and day arguments are required.  *tzinfo* may be ``None``, or an
	instance of a :class:`tzinfo` subclass.  The remaining arguments may be ints or
	longs, in the following ranges:
	
	* ``MINYEAR <= year <= MAXYEAR``
	* ``1 <= month <= 12``
	* ``1 <= day <= number of days in the given month and year``
	* ``0 <= hour < 24``
	* ``0 <= minute < 60``
	* ``0 <= second < 60``
	* ``0 <= microsecond < 1000000``
	
	If an argument outside those ranges is given, :exc:`ValueError` is raised.
	
	Other constructors, all class methods:
	
	"""
	
	
	def __init__(self, year,month,day,hour,minute,second,microsecond,tzinfo):
		pass
	
	


class time:


	"""
	All arguments are optional.  *tzinfo* may be ``None``, or an instance of a
	:class:`tzinfo` subclass.  The remaining arguments may be ints or longs, in the
	following ranges:
	
	* ``0 <= hour < 24``
	* ``0 <= minute < 60``
	* ``0 <= second < 60``
	* ``0 <= microsecond < 1000000``.
	
	If an argument outside those ranges is given, :exc:`ValueError` is raised.  All
	default to ``0`` except *tzinfo*, which defaults to :const:`None`.
	
	Class attributes:
	
	
	"""
	
	
	def __init__(self, hour,minute,second,microsecond,tzinfo):
		pass
	
	


