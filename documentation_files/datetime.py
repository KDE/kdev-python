# AUTO-GENERATED FILE -- DO NOT EDIT

""" Fast implementation of the datetime type. """

MAXYEAR = 9999
MINYEAR = 1
__package__ = None

class date(object):
  """ date(year, month, day) --> date object """

  def ctime(self):
    """ Return ctime() style string. """
    pass

  day = property(None, None, None,
                 )


  def fromordinal(self, int):
    """ int -> date corresponding to a proleptic Gregorian ordinal. """
    return None

  def fromtimestamp(self, timestamp):
    """ timestamp -> local date from a POSIX timestamp (like time.time()). """
    return None

  def isocalendar(self):
    """ Return a 3-tuple containing ISO year, week number, and weekday. """
    pass

  def isoformat(self):
    """ Return string in ISO 8601 format, YYYY-MM-DD. """
    pass

  def isoweekday(self, arg0):
    """ Return the day of the week represented by the date.
    Monday == 1 ... Sunday == 7 """
    return None

  max = None
  min = None
  month = property(None, None, None,
                   )


  def replace(self):
    """ Return date with new specified fields. """
    pass

  resolution = None

  def strftime(self, format):
    """ format -> strftime() style string. """
    return ""

  def timetuple(self):
    """ Return time tuple, compatible with time.localtime(). """
    pass

  def today(self, arg0):
    """ Current date or datetime:  same as self.__class__.fromtimestamp(time.time()). """
    pass

  def toordinal(self):
    """ Return proleptic Gregorian ordinal.  January 1 of year 1 is day 1. """
    pass

  def weekday(self, arg0):
    """ Return the day of the week represented by the date.
    Monday == 0 ... Sunday == 6 """
    return None

  year = property(None, None, None,
                  )


class datetime(date):
  """ datetime(year, month, day[, hour[, minute[, second[, microsecond[,tzinfo]]]]])
  
  The year, month and day arguments are required. tzinfo may be None, or an
  instance of a tzinfo subclass. The remaining arguments may be ints or longs.
   """

  def astimezone(self, tz):
    """ tz -> convert to local time in new timezone tz
     """
    return None

  def combine(self, date, time):
    """ date, time -> datetime with same date and time fields """
    return None

  def ctime(self):
    """ Return ctime() style string. """
    pass

  def date(self):
    """ Return date object with same year, month and day. """
    pass

  def dst(self):
    """ Return self.tzinfo.dst(self). """
    pass

  def fromordinal(self, int):
    """ int -> date corresponding to a proleptic Gregorian ordinal. """
    return None

  def fromtimestamp(self, timestamp, tz=None):
    """ timestamp[, tz] -> tz's local time from POSIX timestamp. """
    return None

  hour = property(None, None, None,
                  )


  def isoformat(self, sep=None):
    """ [sep] -> string in ISO 8601 format, YYYY-MM-DDTHH:MM:SS[.mmmmmm][+HH:MM].
    
    sep is used to separate the year from the time, and defaults to 'T'. """
    return ""

  max = None
  microsecond = property(None, None, None,
                         )

  min = None
  minute = property(None, None, None,
                    )


  def now(self, tz=None):
    """ [tz] -> new datetime with tz's local day and time. """
    return None

  def replace(self):
    """ Return datetime with new specified fields. """
    pass

  resolution = None
  second = property(None, None, None,
                    )


  def strptime(self, string, format):
    """ string, format -> new datetime parsed from a string (like time.strptime()). """
    return ""

  def time(self):
    """ Return time object with same time but with tzinfo=None. """
    pass

  def timetuple(self):
    """ Return time tuple, compatible with time.localtime(). """
    pass

  def timetz(self):
    """ Return time object with same time and tzinfo. """
    pass

  def today(self, arg0):
    """ Current date or datetime:  same as self.__class__.fromtimestamp(time.time()). """
    pass

  tzinfo = property(None, None, None,
                    )


  def tzname(self):
    """ Return self.tzinfo.tzname(self). """
    pass

  def utcfromtimestamp(self, timestamp):
    """ timestamp -> UTC datetime from a POSIX timestamp (like time.time()). """
    return None

  def utcnow(self):
    """ Return a new datetime representing UTC day and time. """
    pass

  def utcoffset(self):
    """ Return self.tzinfo.utcoffset(self). """
    pass

  def utctimetuple(self):
    """ Return UTC time tuple, compatible with time.localtime(). """
    pass

datetime_CAPI = None

class time(object):
  """ time([hour[, minute[, second[, microsecond[, tzinfo]]]]]) --> a time object
  
  All arguments are optional. tzinfo may be None, or an instance of
  a tzinfo subclass. The remaining arguments may be ints or longs.
   """

  def dst(self):
    """ Return self.tzinfo.dst(self). """
    pass

  hour = property(None, None, None,
                  )


  def isoformat(self):
    """ Return string in ISO 8601 format, HH:MM:SS[.mmmmmm][+HH:MM]. """
    pass

  max = None
  microsecond = property(None, None, None,
                         )

  min = None
  minute = property(None, None, None,
                    )


  def replace(self):
    """ Return time with new specified fields. """
    pass

  resolution = None
  second = property(None, None, None,
                    )


  def strftime(self, format):
    """ format -> strftime() style string. """
    return ""

  tzinfo = property(None, None, None,
                    )


  def tzname(self):
    """ Return self.tzinfo.tzname(self). """
    pass

  def utcoffset(self):
    """ Return self.tzinfo.utcoffset(self). """
    pass

class timedelta(object):
  """ Difference between two datetime values. """

  days = None
  max = None
  microseconds = None
  min = None
  resolution = None
  seconds = None

  def total_seconds(self):
    """ Total seconds in the duration. """
    pass

class tzinfo(object):
  """ Abstract base class for time zone info objects. """

  def dst(self, datetime):
    """ datetime -> DST offset in minutes east of UTC. """
    return None

  def fromutc(self, arg0):
    """ datetime in UTC -> datetime in local time. """
    return None

  def tzname(self, datetime):
    """ datetime -> string name of time zone. """
    return ""

  def utcoffset(self, datetime):
    """ datetime -> minutes east of UTC (negative for west of UTC). """
    return None

