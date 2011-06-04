#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
""":synopsis: Functions for working with calendars, including some emulation of the Unix cal
program.
"""
class Calendar:


	"""
	Creates a :class:`Calendar` object. *firstweekday* is an integer specifying the
	first day of the week. ``0`` is Monday (the default), ``6`` is Sunday.
	
	A :class:`Calendar` object provides several methods that can be used for
	preparing the calendar data for formatting. This class doesn't do any formatting
	itself. This is the job of subclasses.
	
	"""
	
	
	def __init__(self, firstweekday):
		pass
	
	


class TextCalendar:


	"""
	This class can be used to generate plain text calendars.
	
	"""
	
	
	def __init__(self, firstweekday):
		pass
	
	


class HTMLCalendar:


	"""
	This class can be used to generate HTML calendars.
	
	"""
	
	
	def __init__(self, firstweekday):
		pass
	
	


class LocaleTextCalendar:


	"""
	This subclass of :class:`TextCalendar` can be passed a locale name in the
	constructor and will return month and weekday names in the specified locale.
	If this locale includes an encoding all strings containing month and weekday
	names will be returned as unicode.
	
	"""
	
	
	def __init__(self, firstweekday,locale):
		pass
	
	


class LocaleHTMLCalendar:


	"""
	This subclass of :class:`HTMLCalendar` can be passed a locale name in the
	constructor and will return month and weekday names in the specified
	locale. If this locale includes an encoding all strings containing month and
	weekday names will be returned as unicode.
	
	"""
	
	
	def __init__(self, firstweekday,locale):
		pass
	
	def setfirstweekday(weekday):
		"""
		Sets the weekday (``0`` is Monday, ``6`` is Sunday) to start each week. The
		values :const:`MONDAY`, :const:`TUESDAY`, :const:`WEDNESDAY`, :const:`THURSDAY`,
		:const:`FRIDAY`, :const:`SATURDAY`, and :const:`SUNDAY` are provided for
		convenience. For example, to set the first weekday to Sunday::
		
		import calendar
		calendar.setfirstweekday(calendar.SUNDAY)
		
		"""
		pass
		
	def firstweekday():
		"""
		Returns the current setting for the weekday to start each week.
		
		"""
		pass
		
	def isleap(year):
		"""
		Returns :const:`True` if *year* is a leap year, otherwise :const:`False`.
		
		
		"""
		pass
		
	def leapdays(y1,y2):
		"""
		Returns the number of leap years in the range from *y1* to *y2* (exclusive),
		where *y1* and *y2* are years.
		
		"""
		pass
		
	def weekday(year,month,day):
		"""
		Returns the day of the week (``0`` is Monday) for *year* (``1970``--*more),
		*month* (``1``--``12``), *day* (``1``--``31``).
		
		
		"""
		pass
		
	def weekheader(n):
		"""
		Return a header containing abbreviated weekday names. *n* specifies the width in
		characters for one weekday.
		
		
		"""
		pass
		
	def monthrange(year,month):
		"""
		Returns weekday of first day of the month and number of days in month,  for the
		specified *year* and *month*.
		
		
		"""
		pass
		
	def monthcalendar(year,month):
		"""
		Returns a matrix representing a month's calendar.  Each row represents a week;
		days outside of the month a represented by zeros. Each week begins with Monday
		unless set by :func:`setfirstweekday`.
		
		
		"""
		pass
		
	def prmonth(theyear,themonth,w,l):
		"""
		Prints a month's calendar as returned by :func:`month`.
		
		
		"""
		pass
		
	def month(theyear,themonth,w,l):
		"""
		Returns a month's calendar in a multi-line string using the :meth:`formatmonth`
		of the :class:`TextCalendar` class.
		
		"""
		pass
		
	def prcal(year,w,lc):
		"""
		Prints the calendar for an entire year as returned by  :func:`calendar`.
		
		
		"""
		pass
		
	def calendar(year,w,lc):
		"""
		Returns a 3-column calendar for an entire year as a multi-line string using the
		:meth:`formatyear` of the :class:`TextCalendar` class.
		
		"""
		pass
		
	def timegm(tuple):
		"""
		An unrelated but handy function that takes a time tuple such as returned by the
		:func:`gmtime` function in the :mod:`time` module, and returns the corresponding
		Unix timestamp value, assuming an epoch of 1970, and the POSIX encoding.  In
		fact, :func:`time.gmtime` and :func:`timegm` are each others' inverse.
		
		"""
		pass
		
	"""
	An array that represents the days of the week in the current locale.
	
	
	"""
	day_name = None
	"""
	An array that represents the abbreviated days of the week in the current locale.
	
	
	"""
	day_abbr = None
	"""
	An array that represents the months of the year in the current locale.  This
	follows normal convention of January being month number 1, so it has a length of
	13 and  ``month_name[0]`` is the empty string.
	
	
	"""
	month_name = None
	"""
	An array that represents the abbreviated months of the year in the current
	locale.  This follows normal convention of January being month number 1, so it
	has a length of 13 and  ``month_abbr[0]`` is the empty string.
	
	
	"""
	month_abbr = None
	


