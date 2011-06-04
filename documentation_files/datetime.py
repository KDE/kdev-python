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
	
	def replace(self, year,month,day):
		"""
		Return a date with the same value, except for those members given new values by
		whichever keyword arguments are specified.  For example, if ``d == date(2002,
		12, 31)``, then ``d.replace(day=26) == date(2002, 12, 26)``.
		
		
		"""
		pass
		
	def timetuple(self, ):
		"""
		Return a :class:`time.struct_time` such as returned by :func:`time.localtime`.
		The hours, minutes and seconds are 0, and the DST flag is -1. ``d.timetuple()``
		is equivalent to ``time.struct_time((d.year, d.month, d.day, 0, 0, 0,
		d.weekday(), yday, -1))``, where ``yday = d.toordinal() - date(d.year, 1,
		1).toordinal() + 1`` is the day number within the current year starting with
		``1`` for January 1st.
		
		
		"""
		pass
		
	def toordinal(self, ):
		"""
		Return the proleptic Gregorian ordinal of the date, where January 1 of year 1
		has ordinal 1.  For any :class:`date` object *d*,
		``date.fromordinal(d.toordinal()) == d``.
		
		
		"""
		pass
		
	def weekday(self, ):
		"""
		Return the day of the week as an integer, where Monday is 0 and Sunday is 6.
		For example, ``date(2002, 12, 4).weekday() == 2``, a Wednesday. See also
		:meth:`isoweekday`.
		
		
		"""
		pass
		
	def isoweekday(self, ):
		"""
		Return the day of the week as an integer, where Monday is 1 and Sunday is 7.
		For example, ``date(2002, 12, 4).isoweekday() == 3``, a Wednesday. See also
		:meth:`weekday`, :meth:`isocalendar`.
		
		
		"""
		pass
		
	def isocalendar(self, ):
		"""
		Return a 3-tuple, (ISO year, ISO week number, ISO weekday).
		
		The ISO calendar is a widely used variant of the Gregorian calendar. See
		http://www.phys.uu.nl/~vgent/calendar/isocalendar.htm for a good
		explanation.
		
		The ISO year consists of 52 or 53 full weeks, and where a week starts on a
		Monday and ends on a Sunday.  The first week of an ISO year is the first
		(Gregorian) calendar week of a year containing a Thursday. This is called week
		number 1, and the ISO year of that Thursday is the same as its Gregorian year.
		
		For example, 2004 begins on a Thursday, so the first week of ISO year 2004
		begins on Monday, 29 Dec 2003 and ends on Sunday, 4 Jan 2004, so that
		``date(2003, 12, 29).isocalendar() == (2004, 1, 1)`` and ``date(2004, 1,
		4).isocalendar() == (2004, 1, 7)``.
		
		
		"""
		pass
		
	def isoformat(self, ):
		"""
		Return a string representing the date in ISO 8601 format, 'YYYY-MM-DD'.  For
		example, ``date(2002, 12, 4).isoformat() == '2002-12-04'``.
		
		
		"""
		pass
		
	def __str__(self, ):
		"""
		For a date *d*, ``str(d)`` is equivalent to ``d.isoformat()``.
		
		
		"""
		pass
		
	def ctime(self, ):
		"""
		Return a string representing the date, for example ``date(2002, 12,
		4).ctime() == 'Wed Dec 4 00:00:00 2002'``. ``d.ctime()`` is equivalent to
		``time.ctime(time.mktime(d.timetuple()))`` on platforms where the native C
		:cfunc:`ctime` function (which :func:`time.ctime` invokes, but which
		:meth:`date.ctime` does not invoke) conforms to the C standard.
		
		
		"""
		pass
		
	def strftime(self, format):
		"""
		Return a string representing the date, controlled by an explicit format string.
		Format codes referring to hours, minutes or seconds will see 0 values. See
		section :ref:`strftime-strptime-behavior`.
		
		
		Example of counting days to an event::
		
		>>> import time
		>>> from datetime import date
		>>> today = date.today()
		>>> today
		datetime.date(2007, 12, 5)
		>>> today == date.fromtimestamp(time.time())
		True
		>>> my_birthday = date(today.year, 6, 24)
		>>> if my_birthday < today:
		*more     my_birthday = my_birthday.replace(year=today.year + 1)
		>>> my_birthday
		datetime.date(2008, 6, 24)
		>>> time_to_birthday = abs(my_birthday - today)
		>>> time_to_birthday.days
		202
		
		Example of working with :class:`date`:
		
		"""
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
	
	def replace(self, hour,minute,second,microsecond,tzinfo):
		"""
		Return a :class:`time` with the same value, except for those members given new
		values by whichever keyword arguments are specified.  Note that ``tzinfo=None``
		can be specified to create a naive :class:`time` from an aware :class:`time`,
		without conversion of the time members.
		
		
		"""
		pass
		
	def isoformat(self, ):
		"""
		Return a string representing the time in ISO 8601 format, HH:MM:SS.mmmmmm or, if
		self.microsecond is 0, HH:MM:SS If :meth:`utcoffset` does not return ``None``, a
		6-character string is appended, giving the UTC offset in (signed) hours and
		minutes: HH:MM:SS.mmmmmm+HH:MM or, if self.microsecond is 0, HH:MM:SS+HH:MM
		
		
		"""
		pass
		
	def __str__(self, ):
		"""
		For a time *t*, ``str(t)`` is equivalent to ``t.isoformat()``.
		
		
		"""
		pass
		
	def strftime(self, format):
		"""
		Return a string representing the time, controlled by an explicit format string.
		See section :ref:`strftime-strptime-behavior`.
		
		
		"""
		pass
		
	def utcoffset(self, ):
		"""
		If :attr:`tzinfo` is ``None``, returns ``None``, else returns
		``self.tzinfo.utcoffset(None)``, and raises an exception if the latter doesn't
		return ``None`` or a :class:`timedelta` object representing a whole number of
		minutes with magnitude less than one day.
		
		
		"""
		pass
		
	def dst(self, ):
		"""
		If :attr:`tzinfo` is ``None``, returns ``None``, else returns
		``self.tzinfo.dst(None)``, and raises an exception if the latter doesn't return
		``None``, or a :class:`timedelta` object representing a whole number of minutes
		with magnitude less than one day.
		
		
		"""
		pass
		
	def tzname(self, ):
		"""
		If :attr:`tzinfo` is ``None``, returns ``None``, else returns
		``self.tzinfo.tzname(None)``, or raises an exception if the latter doesn't
		return ``None`` or a string object.
		
		
		Example:
		
		>>> from datetime import time, tzinfo
		>>> class GMT1(tzinfo):
		*more     def utcoffset(self, dt):
		*more         return timedelta(hours=1)
		*more     def dst(self, dt):
		*more         return timedelta(0)
		*more     def tzname(self,dt):
		*more         return "Europe/Prague"
		*more
		>>> t = time(12, 10, 30, tzinfo=GMT1())
		>>> t                               # doctest: +ELLIPSIS
		datetime.time(12, 10, 30, tzinfo=<GMT1 object at 0x*more>)
		>>> gmt = GMT1()
		>>> t.isoformat()
		'12:10:30+01:00'
		>>> t.dst()
		datetime.timedelta(0)
		>>> t.tzname()
		'Europe/Prague'
		>>> t.strftime("%H:%M:%S %Z")
		'12:10:30 Europe/Prague'
		
		
		.. class:`tzinfo` Objects
		-----------------------
		
		:class:`tzinfo` is an abstract base class, meaning that this class should not be
		instantiated directly.  You need to derive a concrete subclass, and (at least)
		supply implementations of the standard :class:`tzinfo` methods needed by the
		:class:`datetime` methods you use.  The :mod:`datetime` module does not supply
		any concrete subclasses of :class:`tzinfo`.
		
		An instance of (a concrete subclass of) :class:`tzinfo` can be passed to the
		constructors for :class:`datetime` and :class:`time` objects. The latter objects
		view their members as being in local time, and the :class:`tzinfo` object
		supports methods revealing offset of local time from UTC, the name of the time
		zone, and DST offset, all relative to a date or time object passed to them.
		
		Special requirement for pickling:  A :class:`tzinfo` subclass must have an
		:meth:`__init__` method that can be called with no arguments, else it can be
		pickled but possibly not unpickled again.  This is a technical requirement that
		may be relaxed in the future.
		
		A concrete subclass of :class:`tzinfo` may need to implement the following
		methods.  Exactly which methods are needed depends on the uses made of aware
		:mod:`datetime` objects.  If in doubt, simply implement all of them.
		
		
		"""
		pass
		
	


class datetime:


	""":noindex:
	
	A combination of a date and a time. Attributes: :attr:`year`, :attr:`month`,
	:attr:`day`, :attr:`hour`, :attr:`minute`, :attr:`second`, :attr:`microsecond`,
	and :attr:`tzinfo`.
	
	
	"""
	
	
	def __init__(self, ):
		pass
	
	def date(self, ):
		"""
		Return :class:`date` object with same year, month and day.
		
		
		"""
		pass
		
	def time(self, ):
		"""
		Return :class:`time` object with same hour, minute, second and microsecond.
		:attr:`tzinfo` is ``None``.  See also method :meth:`timetz`.
		
		
		"""
		pass
		
	def timetz(self, ):
		"""
		Return :class:`time` object with same hour, minute, second, microsecond, and
		tzinfo members.  See also method :meth:`time`.
		
		
		"""
		pass
		
	def replace(self, year,month,day,hour,minute,second,microsecond,tzinfo):
		"""
		Return a datetime with the same members, except for those members given new
		values by whichever keyword arguments are specified.  Note that ``tzinfo=None``
		can be specified to create a naive datetime from an aware datetime with no
		conversion of date and time members.
		
		
		"""
		pass
		
	def astimezone(self, tz):
		"""
		Return a :class:`datetime` object with new :attr:`tzinfo` member *tz*, adjusting
		the date and time members so the result is the same UTC time as *self*, but in
		*tz*'s local time.
		
		*tz* must be an instance of a :class:`tzinfo` subclass, and its
		:meth:`utcoffset` and :meth:`dst` methods must not return ``None``.  *self* must
		be aware (``self.tzinfo`` must not be ``None``, and ``self.utcoffset()`` must
		not return ``None``).
		
		If ``self.tzinfo`` is *tz*, ``self.astimezone(tz)`` is equal to *self*:  no
		adjustment of date or time members is performed. Else the result is local time
		in time zone *tz*, representing the same UTC time as *self*:  after ``astz =
		dt.astimezone(tz)``, ``astz - astz.utcoffset()`` will usually have the same date
		and time members as ``dt - dt.utcoffset()``. The discussion of class
		:class:`tzinfo` explains the cases at Daylight Saving Time transition boundaries
		where this cannot be achieved (an issue only if *tz* models both standard and
		daylight time).
		
		If you merely want to attach a time zone object *tz* to a datetime *dt* without
		adjustment of date and time members, use ``dt.replace(tzinfo=tz)``.  If you
		merely want to remove the time zone object from an aware datetime *dt* without
		conversion of date and time members, use ``dt.replace(tzinfo=None)``.
		
		Note that the default :meth:`tzinfo.fromutc` method can be overridden in a
		:class:`tzinfo` subclass to affect the result returned by :meth:`astimezone`.
		Ignoring error cases, :meth:`astimezone` acts like::
		
		def astimezone(self, tz):
		if self.tzinfo is tz:
		return self
		# Convert self to UTC, and attach the new time zone object.
		utc = (self - self.utcoffset()).replace(tzinfo=tz)
		# Convert from UTC to tz's local time.
		return tz.fromutc(utc)
		
		
		"""
		pass
		
	def utcoffset(self, ):
		"""
		If :attr:`tzinfo` is ``None``, returns ``None``, else returns
		``self.tzinfo.utcoffset(self)``, and raises an exception if the latter doesn't
		return ``None``, or a :class:`timedelta` object representing a whole number of
		minutes with magnitude less than one day.
		
		
		"""
		pass
		
	def dst(self, ):
		"""
		If :attr:`tzinfo` is ``None``, returns ``None``, else returns
		``self.tzinfo.dst(self)``, and raises an exception if the latter doesn't return
		``None``, or a :class:`timedelta` object representing a whole number of minutes
		with magnitude less than one day.
		
		
		"""
		pass
		
	def tzname(self, ):
		"""
		If :attr:`tzinfo` is ``None``, returns ``None``, else returns
		``self.tzinfo.tzname(self)``, raises an exception if the latter doesn't return
		``None`` or a string object,
		
		
		"""
		pass
		
	def timetuple(self, ):
		"""
		Return a :class:`time.struct_time` such as returned by :func:`time.localtime`.
		``d.timetuple()`` is equivalent to ``time.struct_time((d.year, d.month, d.day,
		d.hour, d.minute, d.second, d.weekday(), yday, dst))``, where ``yday =
		d.toordinal() - date(d.year, 1, 1).toordinal() + 1`` is the day number within
		the current year starting with ``1`` for January 1st. The :attr:`tm_isdst` flag
		of the result is set according to the :meth:`dst` method: :attr:`tzinfo` is
		``None`` or :meth:`dst` returns ``None``, :attr:`tm_isdst` is set to ``-1``;
		else if :meth:`dst` returns a non-zero value, :attr:`tm_isdst` is set to ``1``;
		else :attr:`tm_isdst` is set to ``0``.
		
		
		"""
		pass
		
	def utctimetuple(self, ):
		"""
		If :class:`datetime` instance *d* is naive, this is the same as
		``d.timetuple()`` except that :attr:`tm_isdst` is forced to 0 regardless of what
		``d.dst()`` returns.  DST is never in effect for a UTC time.
		
		If *d* is aware, *d* is normalized to UTC time, by subtracting
		``d.utcoffset()``, and a :class:`time.struct_time` for the normalized time is
		returned.  :attr:`tm_isdst` is forced to 0. Note that the result's
		:attr:`tm_year` member may be :const:`MINYEAR`\ -1 or :const:`MAXYEAR`\ +1, if
		*d*.year was ``MINYEAR`` or ``MAXYEAR`` and UTC adjustment spills over a year
		boundary.
		
		
		"""
		pass
		
	def toordinal(self, ):
		"""
		Return the proleptic Gregorian ordinal of the date.  The same as
		``self.date().toordinal()``.
		
		
		"""
		pass
		
	def weekday(self, ):
		"""
		Return the day of the week as an integer, where Monday is 0 and Sunday is 6.
		The same as ``self.date().weekday()``. See also :meth:`isoweekday`.
		
		
		"""
		pass
		
	def isoweekday(self, ):
		"""
		Return the day of the week as an integer, where Monday is 1 and Sunday is 7.
		The same as ``self.date().isoweekday()``. See also :meth:`weekday`,
		:meth:`isocalendar`.
		
		
		"""
		pass
		
	def isocalendar(self, ):
		"""
		Return a 3-tuple, (ISO year, ISO week number, ISO weekday).  The same as
		``self.date().isocalendar()``.
		
		
		"""
		pass
		
	def isoformat(self, sep):
		"""
		Return a string representing the date and time in ISO 8601 format,
		YYYY-MM-DDTHH:MM:SS.mmmmmm or, if :attr:`microsecond` is 0,
		YYYY-MM-DDTHH:MM:SS
		
		If :meth:`utcoffset` does not return ``None``, a 6-character string is
		appended, giving the UTC offset in (signed) hours and minutes:
		YYYY-MM-DDTHH:MM:SS.mmmmmm+HH:MM or, if :attr:`microsecond` is 0
		YYYY-MM-DDTHH:MM:SS+HH:MM
		
		The optional argument *sep* (default ``'T'``) is a one-character separator,
		placed between the date and time portions of the result.  For example,
		
		>>> from datetime import tzinfo, timedelta, datetime
		>>> class TZ(tzinfo):
		*more     def utcoffset(self, dt): return timedelta(minutes=-399)
		*more
		>>> datetime(2002, 12, 25, tzinfo=TZ()).isoformat(' ')
		'2002-12-25 00:00:00-06:39'
		
		
		"""
		pass
		
	def __str__(self, ):
		"""
		For a :class:`datetime` instance *d*, ``str(d)`` is equivalent to
		``d.isoformat(' ')``.
		
		
		"""
		pass
		
	def ctime(self, ):
		"""
		Return a string representing the date and time, for example ``datetime(2002, 12,
		4, 20, 30, 40).ctime() == 'Wed Dec  4 20:30:40 2002'``. ``d.ctime()`` is
		equivalent to ``time.ctime(time.mktime(d.timetuple()))`` on platforms where the
		native C :cfunc:`ctime` function (which :func:`time.ctime` invokes, but which
		:meth:`datetime.ctime` does not invoke) conforms to the C standard.
		
		
		"""
		pass
		
	def strftime(self, format):
		"""
		Return a string representing the date and time, controlled by an explicit format
		string.  See section :ref:`strftime-strptime-behavior`.
		
		
		Examples of working with datetime objects:
		
		"""
		pass
		
	


class timedelta:


	""":noindex:
	
	A duration expressing the difference between two :class:`date`, :class:`time`,
	or :class:`datetime` instances to microsecond resolution.
	
	
	"""
	
	
	def __init__(self, ):
		pass
	
	def total_seconds(self, ):
		"""
		Return the total number of seconds contained in the duration.
		Equivalent to ``(td.microseconds + (td.seconds + td.days * 24 *
		3600) * 10**6) / 10**6`` computed with true division enabled.
		
		Note that for very large time intervals (greater than 270 years on
		most platforms) this method will lose microsecond accuracy.
		
		"""
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
	
	def utcoffset(self, dt):
		"""
		Return offset of local time from UTC, in minutes east of UTC.  If local time is
		west of UTC, this should be negative.  Note that this is intended to be the
		total offset from UTC; for example, if a :class:`tzinfo` object represents both
		time zone and DST adjustments, :meth:`utcoffset` should return their sum.  If
		the UTC offset isn't known, return ``None``.  Else the value returned must be a
		:class:`timedelta` object specifying a whole number of minutes in the range
		-1439 to 1439 inclusive (1440 = 24\*60; the magnitude of the offset must be less
		than one day).  Most implementations of :meth:`utcoffset` will probably look
		like one of these two::
		
		return CONSTANT                 # fixed-offset class
		return CONSTANT + self.dst(dt)  # daylight-aware class
		
		If :meth:`utcoffset` does not return ``None``, :meth:`dst` should not return
		``None`` either.
		
		The default implementation of :meth:`utcoffset` raises
		:exc:`NotImplementedError`.
		
		
		"""
		pass
		
	def dst(self, dt):
		"""
		Return the daylight saving time (DST) adjustment, in minutes east of UTC, or
		``None`` if DST information isn't known.  Return ``timedelta(0)`` if DST is not
		in effect. If DST is in effect, return the offset as a :class:`timedelta` object
		(see :meth:`utcoffset` for details). Note that DST offset, if applicable, has
		already been added to the UTC offset returned by :meth:`utcoffset`, so there's
		no need to consult :meth:`dst` unless you're interested in obtaining DST info
		separately.  For example, :meth:`datetime.timetuple` calls its :attr:`tzinfo`
		member's :meth:`dst` method to determine how the :attr:`tm_isdst` flag should be
		set, and :meth:`tzinfo.fromutc` calls :meth:`dst` to account for DST changes
		when crossing time zones.
		
		An instance *tz* of a :class:`tzinfo` subclass that models both standard and
		daylight times must be consistent in this sense:
		
		``tz.utcoffset(dt) - tz.dst(dt)``
		
		must return the same result for every :class:`datetime` *dt* with ``dt.tzinfo ==
		tz``  For sane :class:`tzinfo` subclasses, this expression yields the time
		zone's "standard offset", which should not depend on the date or the time, but
		only on geographic location.  The implementation of :meth:`datetime.astimezone`
		relies on this, but cannot detect violations; it's the programmer's
		responsibility to ensure it.  If a :class:`tzinfo` subclass cannot guarantee
		this, it may be able to override the default implementation of
		:meth:`tzinfo.fromutc` to work correctly with :meth:`astimezone` regardless.
		
		Most implementations of :meth:`dst` will probably look like one of these two::
		
		def dst(self):
		# a fixed-offset class:  doesn't account for DST
		return timedelta(0)
		
		or ::
		
		def dst(self):
		# Code to set dston and dstoff to the time zone's DST
		# transition times based on the input dt.year, and expressed
		# in standard local time.  Then
		
		if dston <= dt.replace(tzinfo=None) < dstoff:
		return timedelta(hours=1)
		else:
		return timedelta(0)
		
		The default implementation of :meth:`dst` raises :exc:`NotImplementedError`.
		
		
		"""
		pass
		
	def tzname(self, dt):
		"""
		Return the time zone name corresponding to the :class:`datetime` object *dt*, as
		a string. Nothing about string names is defined by the :mod:`datetime` module,
		and there's no requirement that it mean anything in particular.  For example,
		"GMT", "UTC", "-500", "-5:00", "EDT", "US/Eastern", "America/New York" are all
		valid replies.  Return ``None`` if a string name isn't known.  Note that this is
		a method rather than a fixed string primarily because some :class:`tzinfo`
		subclasses will wish to return different names depending on the specific value
		of *dt* passed, especially if the :class:`tzinfo` class is accounting for
		daylight time.
		
		The default implementation of :meth:`tzname` raises :exc:`NotImplementedError`.
		
		
		These methods are called by a :class:`datetime` or :class:`time` object, in
		response to their methods of the same names.  A :class:`datetime` object passes
		itself as the argument, and a :class:`time` object passes ``None`` as the
		argument.  A :class:`tzinfo` subclass's methods should therefore be prepared to
		accept a *dt* argument of ``None``, or of class :class:`datetime`.
		
		When ``None`` is passed, it's up to the class designer to decide the best
		response.  For example, returning ``None`` is appropriate if the class wishes to
		say that time objects don't participate in the :class:`tzinfo` protocols.  It
		may be more useful for ``utcoffset(None)`` to return the standard UTC offset, as
		there is no other convention for discovering the standard offset.
		
		When a :class:`datetime` object is passed in response to a :class:`datetime`
		method, ``dt.tzinfo`` is the same object as *self*.  :class:`tzinfo` methods can
		rely on this, unless user code calls :class:`tzinfo` methods directly.  The
		intent is that the :class:`tzinfo` methods interpret *dt* as being in local
		time, and not need worry about objects in other timezones.
		
		There is one more :class:`tzinfo` method that a subclass may wish to override:
		
		
		"""
		pass
		
	def _fromutc(self, dt):
		"""
		This is called from the default :class:`datetime.astimezone()` implementation.
		When called from that, ``dt.tzinfo`` is *self*, and *dt*'s date and time members
		are to be viewed as expressing a UTC time.  The purpose of :meth:`fromutc` is to
		adjust the date and time members, returning an equivalent datetime in *self*'s
		local time.
		
		Most :class:`tzinfo` subclasses should be able to inherit the default
		:meth:`fromutc` implementation without problems.  It's strong enough to handle
		fixed-offset time zones, and time zones accounting for both standard and
		daylight time, and the latter even if the DST transition times differ in
		different years.  An example of a time zone the default :meth:`fromutc`
		implementation may not handle correctly in all cases is one where the standard
		offset (from UTC) depends on the specific date and time passed, which can happen
		for political reasons. The default implementations of :meth:`astimezone` and
		:meth:`fromutc` may not produce the result you want if the result is one of the
		hours straddling the moment the standard offset changes.
		
		Skipping code for error cases, the default :meth:`fromutc` implementation acts
		like::
		
		def fromutc(self, dt):
		# raise ValueError error if dt.tzinfo is not self
		dtoff = dt.utcoffset()
		dtdst = dt.dst()
		# raise ValueError if dtoff is None or dtdst is None
		delta = dtoff - dtdst  # this is self's standard offset
		if delta:
		dt += delta   # convert to standard local time
		dtdst = dt.dst()
		# raise ValueError if dtdst is None
		if dtdst:
		return dt + dtdst
		else:
		return dt
		
		Example :class:`tzinfo` classes:
		
		"""
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
	
	
	def __init__(self, ):
		pass
	
	def total_seconds(self, ):
		"""
		Return the total number of seconds contained in the duration.
		Equivalent to ``(td.microseconds + (td.seconds + td.days * 24 *
		3600) * 10**6) / 10**6`` computed with true division enabled.
		
		Note that for very large time intervals (greater than 270 years on
		most platforms) this method will lose microsecond accuracy.
		
		"""
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
	
	
	def __init__(self, ):
		pass
	
	def replace(self, year,month,day):
		"""
		Return a date with the same value, except for those members given new values by
		whichever keyword arguments are specified.  For example, if ``d == date(2002,
		12, 31)``, then ``d.replace(day=26) == date(2002, 12, 26)``.
		
		
		"""
		pass
		
	def timetuple(self, ):
		"""
		Return a :class:`time.struct_time` such as returned by :func:`time.localtime`.
		The hours, minutes and seconds are 0, and the DST flag is -1. ``d.timetuple()``
		is equivalent to ``time.struct_time((d.year, d.month, d.day, 0, 0, 0,
		d.weekday(), yday, -1))``, where ``yday = d.toordinal() - date(d.year, 1,
		1).toordinal() + 1`` is the day number within the current year starting with
		``1`` for January 1st.
		
		
		"""
		pass
		
	def toordinal(self, ):
		"""
		Return the proleptic Gregorian ordinal of the date, where January 1 of year 1
		has ordinal 1.  For any :class:`date` object *d*,
		``date.fromordinal(d.toordinal()) == d``.
		
		
		"""
		pass
		
	def weekday(self, ):
		"""
		Return the day of the week as an integer, where Monday is 0 and Sunday is 6.
		For example, ``date(2002, 12, 4).weekday() == 2``, a Wednesday. See also
		:meth:`isoweekday`.
		
		
		"""
		pass
		
	def isoweekday(self, ):
		"""
		Return the day of the week as an integer, where Monday is 1 and Sunday is 7.
		For example, ``date(2002, 12, 4).isoweekday() == 3``, a Wednesday. See also
		:meth:`weekday`, :meth:`isocalendar`.
		
		
		"""
		pass
		
	def isocalendar(self, ):
		"""
		Return a 3-tuple, (ISO year, ISO week number, ISO weekday).
		
		The ISO calendar is a widely used variant of the Gregorian calendar. See
		http://www.phys.uu.nl/~vgent/calendar/isocalendar.htm for a good
		explanation.
		
		The ISO year consists of 52 or 53 full weeks, and where a week starts on a
		Monday and ends on a Sunday.  The first week of an ISO year is the first
		(Gregorian) calendar week of a year containing a Thursday. This is called week
		number 1, and the ISO year of that Thursday is the same as its Gregorian year.
		
		For example, 2004 begins on a Thursday, so the first week of ISO year 2004
		begins on Monday, 29 Dec 2003 and ends on Sunday, 4 Jan 2004, so that
		``date(2003, 12, 29).isocalendar() == (2004, 1, 1)`` and ``date(2004, 1,
		4).isocalendar() == (2004, 1, 7)``.
		
		
		"""
		pass
		
	def isoformat(self, ):
		"""
		Return a string representing the date in ISO 8601 format, 'YYYY-MM-DD'.  For
		example, ``date(2002, 12, 4).isoformat() == '2002-12-04'``.
		
		
		"""
		pass
		
	def __str__(self, ):
		"""
		For a date *d*, ``str(d)`` is equivalent to ``d.isoformat()``.
		
		
		"""
		pass
		
	def ctime(self, ):
		"""
		Return a string representing the date, for example ``date(2002, 12,
		4).ctime() == 'Wed Dec 4 00:00:00 2002'``. ``d.ctime()`` is equivalent to
		``time.ctime(time.mktime(d.timetuple()))`` on platforms where the native C
		:cfunc:`ctime` function (which :func:`time.ctime` invokes, but which
		:meth:`date.ctime` does not invoke) conforms to the C standard.
		
		
		"""
		pass
		
	def strftime(self, format):
		"""
		Return a string representing the date, controlled by an explicit format string.
		Format codes referring to hours, minutes or seconds will see 0 values. See
		section :ref:`strftime-strptime-behavior`.
		
		
		Example of counting days to an event::
		
		>>> import time
		>>> from datetime import date
		>>> today = date.today()
		>>> today
		datetime.date(2007, 12, 5)
		>>> today == date.fromtimestamp(time.time())
		True
		>>> my_birthday = date(today.year, 6, 24)
		>>> if my_birthday < today:
		*more     my_birthday = my_birthday.replace(year=today.year + 1)
		>>> my_birthday
		datetime.date(2008, 6, 24)
		>>> time_to_birthday = abs(my_birthday - today)
		>>> time_to_birthday.days
		202
		
		Example of working with :class:`date`:
		
		"""
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
	
	
	def __init__(self, ):
		pass
	
	def date(self, ):
		"""
		Return :class:`date` object with same year, month and day.
		
		
		"""
		pass
		
	def time(self, ):
		"""
		Return :class:`time` object with same hour, minute, second and microsecond.
		:attr:`tzinfo` is ``None``.  See also method :meth:`timetz`.
		
		
		"""
		pass
		
	def timetz(self, ):
		"""
		Return :class:`time` object with same hour, minute, second, microsecond, and
		tzinfo members.  See also method :meth:`time`.
		
		
		"""
		pass
		
	def replace(self, year,month,day,hour,minute,second,microsecond,tzinfo):
		"""
		Return a datetime with the same members, except for those members given new
		values by whichever keyword arguments are specified.  Note that ``tzinfo=None``
		can be specified to create a naive datetime from an aware datetime with no
		conversion of date and time members.
		
		
		"""
		pass
		
	def astimezone(self, tz):
		"""
		Return a :class:`datetime` object with new :attr:`tzinfo` member *tz*, adjusting
		the date and time members so the result is the same UTC time as *self*, but in
		*tz*'s local time.
		
		*tz* must be an instance of a :class:`tzinfo` subclass, and its
		:meth:`utcoffset` and :meth:`dst` methods must not return ``None``.  *self* must
		be aware (``self.tzinfo`` must not be ``None``, and ``self.utcoffset()`` must
		not return ``None``).
		
		If ``self.tzinfo`` is *tz*, ``self.astimezone(tz)`` is equal to *self*:  no
		adjustment of date or time members is performed. Else the result is local time
		in time zone *tz*, representing the same UTC time as *self*:  after ``astz =
		dt.astimezone(tz)``, ``astz - astz.utcoffset()`` will usually have the same date
		and time members as ``dt - dt.utcoffset()``. The discussion of class
		:class:`tzinfo` explains the cases at Daylight Saving Time transition boundaries
		where this cannot be achieved (an issue only if *tz* models both standard and
		daylight time).
		
		If you merely want to attach a time zone object *tz* to a datetime *dt* without
		adjustment of date and time members, use ``dt.replace(tzinfo=tz)``.  If you
		merely want to remove the time zone object from an aware datetime *dt* without
		conversion of date and time members, use ``dt.replace(tzinfo=None)``.
		
		Note that the default :meth:`tzinfo.fromutc` method can be overridden in a
		:class:`tzinfo` subclass to affect the result returned by :meth:`astimezone`.
		Ignoring error cases, :meth:`astimezone` acts like::
		
		def astimezone(self, tz):
		if self.tzinfo is tz:
		return self
		# Convert self to UTC, and attach the new time zone object.
		utc = (self - self.utcoffset()).replace(tzinfo=tz)
		# Convert from UTC to tz's local time.
		return tz.fromutc(utc)
		
		
		"""
		pass
		
	def utcoffset(self, ):
		"""
		If :attr:`tzinfo` is ``None``, returns ``None``, else returns
		``self.tzinfo.utcoffset(self)``, and raises an exception if the latter doesn't
		return ``None``, or a :class:`timedelta` object representing a whole number of
		minutes with magnitude less than one day.
		
		
		"""
		pass
		
	def dst(self, ):
		"""
		If :attr:`tzinfo` is ``None``, returns ``None``, else returns
		``self.tzinfo.dst(self)``, and raises an exception if the latter doesn't return
		``None``, or a :class:`timedelta` object representing a whole number of minutes
		with magnitude less than one day.
		
		
		"""
		pass
		
	def tzname(self, ):
		"""
		If :attr:`tzinfo` is ``None``, returns ``None``, else returns
		``self.tzinfo.tzname(self)``, raises an exception if the latter doesn't return
		``None`` or a string object,
		
		
		"""
		pass
		
	def timetuple(self, ):
		"""
		Return a :class:`time.struct_time` such as returned by :func:`time.localtime`.
		``d.timetuple()`` is equivalent to ``time.struct_time((d.year, d.month, d.day,
		d.hour, d.minute, d.second, d.weekday(), yday, dst))``, where ``yday =
		d.toordinal() - date(d.year, 1, 1).toordinal() + 1`` is the day number within
		the current year starting with ``1`` for January 1st. The :attr:`tm_isdst` flag
		of the result is set according to the :meth:`dst` method: :attr:`tzinfo` is
		``None`` or :meth:`dst` returns ``None``, :attr:`tm_isdst` is set to ``-1``;
		else if :meth:`dst` returns a non-zero value, :attr:`tm_isdst` is set to ``1``;
		else :attr:`tm_isdst` is set to ``0``.
		
		
		"""
		pass
		
	def utctimetuple(self, ):
		"""
		If :class:`datetime` instance *d* is naive, this is the same as
		``d.timetuple()`` except that :attr:`tm_isdst` is forced to 0 regardless of what
		``d.dst()`` returns.  DST is never in effect for a UTC time.
		
		If *d* is aware, *d* is normalized to UTC time, by subtracting
		``d.utcoffset()``, and a :class:`time.struct_time` for the normalized time is
		returned.  :attr:`tm_isdst` is forced to 0. Note that the result's
		:attr:`tm_year` member may be :const:`MINYEAR`\ -1 or :const:`MAXYEAR`\ +1, if
		*d*.year was ``MINYEAR`` or ``MAXYEAR`` and UTC adjustment spills over a year
		boundary.
		
		
		"""
		pass
		
	def toordinal(self, ):
		"""
		Return the proleptic Gregorian ordinal of the date.  The same as
		``self.date().toordinal()``.
		
		
		"""
		pass
		
	def weekday(self, ):
		"""
		Return the day of the week as an integer, where Monday is 0 and Sunday is 6.
		The same as ``self.date().weekday()``. See also :meth:`isoweekday`.
		
		
		"""
		pass
		
	def isoweekday(self, ):
		"""
		Return the day of the week as an integer, where Monday is 1 and Sunday is 7.
		The same as ``self.date().isoweekday()``. See also :meth:`weekday`,
		:meth:`isocalendar`.
		
		
		"""
		pass
		
	def isocalendar(self, ):
		"""
		Return a 3-tuple, (ISO year, ISO week number, ISO weekday).  The same as
		``self.date().isocalendar()``.
		
		
		"""
		pass
		
	def isoformat(self, sep):
		"""
		Return a string representing the date and time in ISO 8601 format,
		YYYY-MM-DDTHH:MM:SS.mmmmmm or, if :attr:`microsecond` is 0,
		YYYY-MM-DDTHH:MM:SS
		
		If :meth:`utcoffset` does not return ``None``, a 6-character string is
		appended, giving the UTC offset in (signed) hours and minutes:
		YYYY-MM-DDTHH:MM:SS.mmmmmm+HH:MM or, if :attr:`microsecond` is 0
		YYYY-MM-DDTHH:MM:SS+HH:MM
		
		The optional argument *sep* (default ``'T'``) is a one-character separator,
		placed between the date and time portions of the result.  For example,
		
		>>> from datetime import tzinfo, timedelta, datetime
		>>> class TZ(tzinfo):
		*more     def utcoffset(self, dt): return timedelta(minutes=-399)
		*more
		>>> datetime(2002, 12, 25, tzinfo=TZ()).isoformat(' ')
		'2002-12-25 00:00:00-06:39'
		
		
		"""
		pass
		
	def __str__(self, ):
		"""
		For a :class:`datetime` instance *d*, ``str(d)`` is equivalent to
		``d.isoformat(' ')``.
		
		
		"""
		pass
		
	def ctime(self, ):
		"""
		Return a string representing the date and time, for example ``datetime(2002, 12,
		4, 20, 30, 40).ctime() == 'Wed Dec  4 20:30:40 2002'``. ``d.ctime()`` is
		equivalent to ``time.ctime(time.mktime(d.timetuple()))`` on platforms where the
		native C :cfunc:`ctime` function (which :func:`time.ctime` invokes, but which
		:meth:`datetime.ctime` does not invoke) conforms to the C standard.
		
		
		"""
		pass
		
	def strftime(self, format):
		"""
		Return a string representing the date and time, controlled by an explicit format
		string.  See section :ref:`strftime-strptime-behavior`.
		
		
		Examples of working with datetime objects:
		
		"""
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
	
	
	def __init__(self, ):
		pass
	
	def replace(self, hour,minute,second,microsecond,tzinfo):
		"""
		Return a :class:`time` with the same value, except for those members given new
		values by whichever keyword arguments are specified.  Note that ``tzinfo=None``
		can be specified to create a naive :class:`time` from an aware :class:`time`,
		without conversion of the time members.
		
		
		"""
		pass
		
	def isoformat(self, ):
		"""
		Return a string representing the time in ISO 8601 format, HH:MM:SS.mmmmmm or, if
		self.microsecond is 0, HH:MM:SS If :meth:`utcoffset` does not return ``None``, a
		6-character string is appended, giving the UTC offset in (signed) hours and
		minutes: HH:MM:SS.mmmmmm+HH:MM or, if self.microsecond is 0, HH:MM:SS+HH:MM
		
		
		"""
		pass
		
	def __str__(self, ):
		"""
		For a time *t*, ``str(t)`` is equivalent to ``t.isoformat()``.
		
		
		"""
		pass
		
	def strftime(self, format):
		"""
		Return a string representing the time, controlled by an explicit format string.
		See section :ref:`strftime-strptime-behavior`.
		
		
		"""
		pass
		
	def utcoffset(self, ):
		"""
		If :attr:`tzinfo` is ``None``, returns ``None``, else returns
		``self.tzinfo.utcoffset(None)``, and raises an exception if the latter doesn't
		return ``None`` or a :class:`timedelta` object representing a whole number of
		minutes with magnitude less than one day.
		
		
		"""
		pass
		
	def dst(self, ):
		"""
		If :attr:`tzinfo` is ``None``, returns ``None``, else returns
		``self.tzinfo.dst(None)``, and raises an exception if the latter doesn't return
		``None``, or a :class:`timedelta` object representing a whole number of minutes
		with magnitude less than one day.
		
		
		"""
		pass
		
	def tzname(self, ):
		"""
		If :attr:`tzinfo` is ``None``, returns ``None``, else returns
		``self.tzinfo.tzname(None)``, or raises an exception if the latter doesn't
		return ``None`` or a string object.
		
		
		Example:
		
		>>> from datetime import time, tzinfo
		>>> class GMT1(tzinfo):
		*more     def utcoffset(self, dt):
		*more         return timedelta(hours=1)
		*more     def dst(self, dt):
		*more         return timedelta(0)
		*more     def tzname(self,dt):
		*more         return "Europe/Prague"
		*more
		>>> t = time(12, 10, 30, tzinfo=GMT1())
		>>> t                               # doctest: +ELLIPSIS
		datetime.time(12, 10, 30, tzinfo=<GMT1 object at 0x*more>)
		>>> gmt = GMT1()
		>>> t.isoformat()
		'12:10:30+01:00'
		>>> t.dst()
		datetime.timedelta(0)
		>>> t.tzname()
		'Europe/Prague'
		>>> t.strftime("%H:%M:%S %Z")
		'12:10:30 Europe/Prague'
		
		
		.. class:`tzinfo` Objects
		-----------------------
		
		:class:`tzinfo` is an abstract base class, meaning that this class should not be
		instantiated directly.  You need to derive a concrete subclass, and (at least)
		supply implementations of the standard :class:`tzinfo` methods needed by the
		:class:`datetime` methods you use.  The :mod:`datetime` module does not supply
		any concrete subclasses of :class:`tzinfo`.
		
		An instance of (a concrete subclass of) :class:`tzinfo` can be passed to the
		constructors for :class:`datetime` and :class:`time` objects. The latter objects
		view their members as being in local time, and the :class:`tzinfo` object
		supports methods revealing offset of local time from UTC, the name of the time
		zone, and DST offset, all relative to a date or time object passed to them.
		
		Special requirement for pickling:  A :class:`tzinfo` subclass must have an
		:meth:`__init__` method that can be called with no arguments, else it can be
		pickled but possibly not unpickled again.  This is a technical requirement that
		may be relaxed in the future.
		
		A concrete subclass of :class:`tzinfo` may need to implement the following
		methods.  Exactly which methods are needed depends on the uses made of aware
		:mod:`datetime` objects.  If in doubt, simply implement all of them.
		
		
		"""
		pass
		
	


