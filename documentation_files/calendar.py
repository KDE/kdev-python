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
	
	
	def __init__(self, ):
		pass
	
	def iterweekdays(self, ):
		"""
		Return an iterator for the week day numbers that will be used for one
		week.  The first value from the iterator will be the same as the value of
		the :attr:`firstweekday` property.
		
		
		"""
		pass
		
	def itermonthdates(self, year,month):
		"""
		Return an iterator for the month *month* (1-12) in the year *year*. This
		iterator will return all days (as :class:`datetime.date` objects) for the
		month and all days before the start of the month or after the end of the
		month that are required to get a complete week.
		
		
		"""
		pass
		
	def itermonthdays2(self, year,month):
		"""
		Return an iterator for the month *month* in the year *year* similar to
		:meth:`itermonthdates`. Days returned will be tuples consisting of a day
		number and a week day number.
		
		
		"""
		pass
		
	def itermonthdays(self, year,month):
		"""
		Return an iterator for the month *month* in the year *year* similar to
		:meth:`itermonthdates`. Days returned will simply be day numbers.
		
		
		"""
		pass
		
	def monthdatescalendar(self, year,month):
		"""
		Return a list of the weeks in the month *month* of the *year* as full
		weeks.  Weeks are lists of seven :class:`datetime.date` objects.
		
		
		"""
		pass
		
	def monthdays2calendar(self, year,month):
		"""
		Return a list of the weeks in the month *month* of the *year* as full
		weeks.  Weeks are lists of seven tuples of day numbers and weekday
		numbers.
		
		
		"""
		pass
		
	def monthdayscalendar(self, year,month):
		"""
		Return a list of the weeks in the month *month* of the *year* as full
		weeks.  Weeks are lists of seven day numbers.
		
		
		"""
		pass
		
	def yeardatescalendar(self, year,width):
		"""
		Return the data for the specified year ready for formatting. The return
		value is a list of month rows. Each month row contains up to *width*
		months (defaulting to 3). Each month contains between 4 and 6 weeks and
		each week contains 1--7 days. Days are :class:`datetime.date` objects.
		
		
		"""
		pass
		
	def yeardays2calendar(self, year,width):
		"""
		Return the data for the specified year ready for formatting (similar to
		:meth:`yeardatescalendar`). Entries in the week lists are tuples of day
		numbers and weekday numbers. Day numbers outside this month are zero.
		
		
		"""
		pass
		
	def yeardayscalendar(self, year,width):
		"""
		Return the data for the specified year ready for formatting (similar to
		:meth:`yeardatescalendar`). Entries in the week lists are day numbers. Day
		numbers outside this month are zero.
		
		
		"""
		pass
		
	


class TextCalendar:


	"""
	This class can be used to generate plain text calendars.
	
	"""
	
	
	def __init__(self, ):
		pass
	
	def formatmonth(self, theyear,themonth,w,l):
		"""
		Return a month's calendar in a multi-line string. If *w* is provided, it
		specifies the width of the date columns, which are centered. If *l* is
		given, it specifies the number of lines that each week will use. Depends
		on the first weekday as specified in the constructor or set by the
		:meth:`setfirstweekday` method.
		
		
		"""
		pass
		
	def prmonth(self, theyear,themonth,w,l):
		"""
		Print a month's calendar as returned by :meth:`formatmonth`.
		
		
		"""
		pass
		
	def formatyear(self, theyear,w,l,c,m):
		"""
		Return a *m*-column calendar for an entire year as a multi-line string.
		Optional parameters *w*, *l*, and *c* are for date column width, lines per
		week, and number of spaces between month columns, respectively. Depends on
		the first weekday as specified in the constructor or set by the
		:meth:`setfirstweekday` method.  The earliest year for which a calendar
		can be generated is platform-dependent.
		
		
		"""
		pass
		
	def pryear(self, theyear,w,l,c,m):
		"""
		Print the calendar for an entire year as returned by :meth:`formatyear`.
		
		
		"""
		pass
		
	


class HTMLCalendar:


	"""
	This class can be used to generate HTML calendars.
	
	"""
	
	
	def __init__(self, ):
		pass
	
	def formatmonth(self, theyear,themonth,withyear):
		"""
		Return a month's calendar as an HTML table. If *withyear* is true the year
		will be included in the header, otherwise just the month name will be
		used.
		
		
		"""
		pass
		
	def formatyear(self, theyear,width):
		"""
		Return a year's calendar as an HTML table. *width* (defaulting to 3)
		specifies the number of months per row.
		
		
		"""
		pass
		
	def formatyearpage(self, theyear,width,css,encoding):
		"""
		Return a year's calendar as a complete HTML page. *width* (defaulting to
		3) specifies the number of months per row. *css* is the name for the
		cascading style sheet to be used. :const:`None` can be passed if no style
		sheet should be used. *encoding* specifies the encoding to be used for the
		output (defaulting to the system default encoding).
		
		
		"""
		pass
		
	


class LocaleTextCalendar:


	"""
	This subclass of :class:`TextCalendar` can be passed a locale name in the
	constructor and will return month and weekday names in the specified locale.
	If this locale includes an encoding all strings containing month and weekday
	names will be returned as unicode.
	
	"""
	
	
	def __init__(self, ):
		pass
	
	


class LocaleHTMLCalendar:


	"""
	This subclass of :class:`HTMLCalendar` can be passed a locale name in the
	constructor and will return month and weekday names in the specified
	locale. If this locale includes an encoding all strings containing month and
	weekday names will be returned as unicode.
	
	"""
	
	
	def __init__(self, ):
		pass
	
	def setfirstweekday(self, weekday):
		"""
		Sets the weekday (``0`` is Monday, ``6`` is Sunday) to start each week. The
		values :const:`MONDAY`, :const:`TUESDAY`, :const:`WEDNESDAY`, :const:`THURSDAY`,
		:const:`FRIDAY`, :const:`SATURDAY`, and :const:`SUNDAY` are provided for
		convenience. For example, to set the first weekday to Sunday::
		
		import calendar
		calendar.setfirstweekday(calendar.SUNDAY)
		
		"""
		pass
		
	def firstweekday(self, ):
		"""
		Returns the current setting for the weekday to start each week.
		
		"""
		pass
		
	def isleap(self, year):
		"""
		Returns :const:`True` if *year* is a leap year, otherwise :const:`False`.
		
		
		"""
		pass
		
	def leapdays(self, y1,y2):
		"""
		Returns the number of leap years in the range from *y1* to *y2* (exclusive),
		where *y1* and *y2* are years.
		
		"""
		pass
		
	def weekday(self, year,month,day):
		"""
		Returns the day of the week (``0`` is Monday) for *year* (``1970``--*more),
		*month* (``1``--``12``), *day* (``1``--``31``).
		
		
		"""
		pass
		
	def weekheader(self, n):
		"""
		Return a header containing abbreviated weekday names. *n* specifies the width in
		characters for one weekday.
		
		
		"""
		pass
		
	def monthrange(self, year,month):
		"""
		Returns weekday of first day of the month and number of days in month,  for the
		specified *year* and *month*.
		
		
		"""
		pass
		
	def monthcalendar(self, year,month):
		"""
		Returns a matrix representing a month's calendar.  Each row represents a week;
		days outside of the month a represented by zeros. Each week begins with Monday
		unless set by :func:`setfirstweekday`.
		
		
		"""
		pass
		
	def prmonth(self, theyear,themonth,w,l):
		"""
		Prints a month's calendar as returned by :func:`month`.
		
		
		"""
		pass
		
	def month(self, theyear,themonth,w,l):
		"""
		Returns a month's calendar in a multi-line string using the :meth:`formatmonth`
		of the :class:`TextCalendar` class.
		
		"""
		pass
		
	def prcal(self, year,w,lc):
		"""
		Prints the calendar for an entire year as returned by  :func:`calendar`.
		
		
		"""
		pass
		
	def calendar(self, year,w,lc):
		"""
		Returns a 3-column calendar for an entire year as a multi-line string using the
		:meth:`formatyear` of the :class:`TextCalendar` class.
		
		"""
		pass
		
	def timegm(self, tuple):
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
	


