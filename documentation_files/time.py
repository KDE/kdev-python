# AUTO-GENERATED FILE -- DO NOT EDIT

""" This module provides various functions to manipulate time values.

There are two standard representations of time.  One is the number
of seconds since the Epoch, in UTC (a.k.a. GMT).  It may be an integer
or a floating point number (to represent fractions of seconds).
The Epoch is system-defined; on Unix, it is generally January 1st, 1970.
The actual value can be retrieved by calling gmtime(0).

The other representation is a tuple of 9 integers giving local time.
The tuple items are:
  year (four digits, e.g. 1998)
  month (1-12)
  day (1-31)
  hours (0-23)
  minutes (0-59)
  seconds (0-59)
  weekday (0-6, Monday is 0)
  Julian day (day in the year, 1-366)
  DST (Daylight Savings Time) flag (-1, 0 or 1)
If the DST flag is 0, the time is given in the regular time zone;
if it is 1, the time is given in the DST time zone;
if it is -1, mktime() should guess based on the date and time.

Variables:

timezone -- difference in seconds between UTC and local standard time
altzone -- difference in  seconds between UTC and local DST time
daylight -- whether local time should reflect DST
tzname -- tuple of (standard time zone name, DST time zone name)

Functions:

time() -- return current time in seconds since the Epoch as a float
clock() -- return CPU time since process start as a float
sleep() -- delay for a number of seconds given as a float
gmtime() -- convert seconds since Epoch to UTC tuple
localtime() -- convert seconds since Epoch to local time tuple
asctime() -- convert time tuple to string
ctime() -- convert time in seconds to string
mktime() -- convert local time tuple to seconds since Epoch
strftime() -- convert time tuple to string according to format specification
strptime() -- parse string to time tuple according to format specification
tzset() -- change the local timezone """

__package__ = None
accept2dyear = 1
altzone = -7200

def asctime(tuple=None):
  """ asctime([tuple]) -> string
  
  Convert a time tuple to a string, e.g. 'Sat Jun 06 16:26:11 1998'.
  When the time tuple is not present, current time as returned by localtime()
  is used. """
  return ""

def clock():
  """ clock() -> floating point number
  
  Return the CPU time or real time since the start of the process or since
  the first call to clock().  This has as much precision as the system
  records. """
  return 1

def ctime(seconds):
  """ ctime(seconds) -> string
  
  Convert a time in seconds since the Epoch to a string in local time.
  This is equivalent to asctime(localtime(seconds)). When the time tuple is
  not present, current time as returned by localtime() is used. """
  return ""

daylight = 1

def gmtime(seconds=None):
  """ gmtime([seconds]) -> (tm_year, tm_mon, tm_mday, tm_hour, tm_min,
                         tm_sec, tm_wday, tm_yday, tm_isdst)
  
  Convert seconds since the Epoch to a time tuple expressing UTC (a.k.a.
  GMT).  When 'seconds' is not passed in, convert the current time instead. """
  return (None, None, None, None, None, None, None, None, None)

def localtime(seconds=None):
  """ localtime([seconds]) -> (tm_year,tm_mon,tm_mday,tm_hour,tm_min,
                            tm_sec,tm_wday,tm_yday,tm_isdst)
  
  Convert seconds since the Epoch to a time tuple expressing local time.
  When 'seconds' is not passed in, convert the current time instead. """
  return (None, None, None, None, None, None, None, None, None)

def mktime(tuple):
  """ mktime(tuple) -> floating point number
  
  Convert a time tuple in local time to seconds since the Epoch. """
  return 1

def sleep(seconds):
  """ sleep(seconds)
  
  Delay execution for a given number of seconds.  The argument may be
  a floating point number for subsecond precision. """
  pass

def strftime(format, tuple=None):
  """ strftime(format[, tuple]) -> string
  
  Convert a time tuple to a string according to a format specification.
  See the library reference manual for formatting codes. When the time tuple
  is not present, current time as returned by localtime() is used. """
  return ""

def strptime(string, format):
  """ strptime(string, format) -> struct_time
  
  Parse a string to a time tuple according to a format specification.
  See the library reference manual for formatting codes (same as strftime()). """
  return ""

class struct_time(object):
  """ The time value as returned by gmtime(), localtime(), and strptime(), and
   accepted by asctime(), mktime() and strftime().  May be considered as a
   sequence of 9 integers.
  
   Note that several fields' values are not the same as those defined by
   the C language standard for struct tm.  For example, the value of the
   field tm_year is the actual year, not year - 1900.  See individual
   fields' descriptions for details. """

  n_fields = 9
  n_sequence_fields = 9
  n_unnamed_fields = 0
  tm_hour = None
  tm_isdst = None
  tm_mday = None
  tm_min = None
  tm_mon = None
  tm_sec = None
  tm_wday = None
  tm_yday = None
  tm_year = None

def time():
  """ time() -> floating point number
  
  Return the current time in seconds since the Epoch.
  Fractions of a second may be present if the system clock provides them. """
  return 1

timezone = -3600
tzname = ()

def tzset():
  """ tzset()
  
  Initialize, or reinitialize, the local timezone to the value stored in
  os.environ['TZ']. The TZ environment variable should be specified in
  standard Unix timezone format as documented in the tzset man page
  (eg. 'US/Eastern', 'Europe/Amsterdam'). Unknown timezones will silently
  fall back to UTC. If the TZ environment variable is not set, the local
  timezone is set to the systems best guess of wallclock time.
  Changing the TZ environment variable without calling tzset *may* change
  the local timezone used by methods such as localtime, but this behaviour
  should not be relied on. """
  pass

