#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
""":synopsis: Internationalization services.
"""
"""
Get a string with the name of the character encoding used in the
selected locale.

"""
CODESET = None
"""
Get a string that can be used as a format string for :func:`strftime` to
represent date and time in a locale-specific way.

"""
D_T_FMT = None
"""
Get a string that can be used as a format string for :func:`strftime` to
represent a date in a locale-specific way.

"""
D_FMT = None
"""
Get a string that can be used as a format string for :func:`strftime` to
represent a time in a locale-specific way.

"""
T_FMT = None
"""
Get a format string for :func:`strftime` to represent time in the am/pm
format.

"""
T_FMT_AMPM = None
"""
Get the name of the n-th day of the week.

"""
DAY_1moreDAY_7 = None
"""
Get the abbreviated name of the n-th day of the week.

"""
ABDAY_1moreABDAY_7 = None
"""
Get the name of the n-th month.

"""
MON_1moreMON_12 = None
"""
Get the abbreviated name of the n-th month.

"""
ABMON_1moreABMON_12 = None
"""
Get the radix character (decimal dot, decimal comma, etc.)

"""
RADIXCHAR = None
"""
Get the separator character for thousands (groups of three digits).

"""
THOUSEP = None
"""
Get a regular expression that can be used with the regex function to
recognize a positive response to a yes/no question.

"""
YESEXPR = None
"""
Get a regular expression that can be used with the regex(3) function to
recognize a negative response to a yes/no question.

"""
NOEXPR = None
"""
Get the currency symbol, preceded by "-" if the symbol should appear before
the value, "+" if the symbol should appear after the value, or "." if the
symbol should replace the radix character.

"""
CRNCYSTR = None
"""
Get a string that represents the era used in the current locale.

Most locales do not define this value.  An example of a locale which does
define this value is the Japanese one.  In Japan, the traditional
representation of dates includes the name of the era corresponding to the
then-emperor's reign.

Normally it should not be necessary to use this value directly. Specifying
the ``E`` modifier in their format strings causes the :func:`strftime`
function to use this information.  The format of the returned string is not
specified, and therefore you should not assume knowledge of it on different
systems.

"""
ERA = None
"""
Get a format string for :func:`strftime` to represent date and time in a
locale-specific era-based way.

"""
ERA_D_T_FMT = None
"""
Get a format string for :func:`strftime` to represent a date in a
locale-specific era-based way.

"""
ERA_D_FMT = None
"""
Get a format string for :func:`strftime` to represent a time in a
locale-specific era-based way.

"""
ERA_T_FMT = None
"""
Get a representation of up to 100 values used to represent the values
0 to 99.


"""
ALT_DIGITS = None
"""
"""
LC_CTYPE = None
"""
Locale category for sorting strings.  The functions :func:`strcoll` and
:func:`strxfrm` of the :mod:`locale` module are affected.


"""
LC_COLLATE = None
"""
Locale category for the formatting of time.  The function :func:`time.strftime`
follows these conventions.


"""
LC_TIME = None
"""
Locale category for formatting of monetary values.  The available options are
available from the :func:`localeconv` function.


"""
LC_MONETARY = None
"""
Locale category for message display. Python currently does not support
application specific locale-aware messages.  Messages displayed by the operating
system, like those returned by :func:`os.strerror` might be affected by this
category.


"""
LC_MESSAGES = None
"""
Locale category for formatting numbers.  The functions :func:`.format`,
:func:`atoi`, :func:`atof` and :func:`.str` of the :mod:`locale` module are
affected by that category.  All other numeric formatting operations are not
affected.


"""
LC_NUMERIC = None
"""
Combination of all locale settings.  If this flag is used when the locale is
changed, setting the locale for all categories is attempted. If that fails for
any category, no category is changed at all.  When the locale is retrieved using
this flag, a string indicating the setting for all categories is returned. This
string can be later used to restore the settings.


"""
LC_ALL = None
"""
This is a symbolic constant used for different values returned by
:func:`localeconv`.


Example::

>>> import locale
>>> loc = locale.getlocale() # get current locale
# use German locale; name might vary with platform
>>> locale.setlocale(locale.LC_ALL, 'de_DE')
>>> locale.strcoll('f\xe4n', 'foo') # compare a string containing an umlaut
>>> locale.setlocale(locale.LC_ALL, '') # use user's preferred locale
>>> locale.setlocale(locale.LC_ALL, 'C') # use default (C) locale
>>> locale.setlocale(locale.LC_ALL, loc) # restore saved locale


Background, details, hints, tips and caveats
--------------------------------------------

The C standard defines the locale as a program-wide property that may be
relatively expensive to change.  On top of that, some implementation are broken
in such a way that frequent locale changes may cause core dumps.  This makes the
locale somewhat painful to use correctly.

Initially, when a program is started, the locale is the ``C`` locale, no matter
what the user's preferred locale is.  The program must explicitly say that it
wants the user's preferred locale settings by calling ``setlocale(LC_ALL, '')``.

It is generally a bad idea to call :func:`setlocale` in some library routine,
since as a side effect it affects the entire program.  Saving and restoring it
is almost as bad: it is expensive and affects other threads that happen to run
before the settings have been restored.

If, when coding a module for general use, you need a locale independent version
of an operation that is affected by the locale (such as :func:`string.lower`, or
certain formats used with :func:`time.strftime`), you will have to find a way to
do it without using the standard library routine.  Even better is convincing
yourself that using locale settings is okay.  Only as a last resort should you
document that your module is not compatible with non-\ ``C`` locale settings.

"""
CHAR_MAX = None
def setlocale(category,locale):
	"""
	If *locale* is specified, it may be a string, a tuple of the form ``(language
	code, encoding)``, or ``None``. If it is a tuple, it is converted to a string
	using the locale aliasing engine.  If *locale* is given and not ``None``,
	:func:`setlocale` modifies the locale setting for the *category*.  The available
	categories are listed in the data description below.  The value is the name of a
	locale.  An empty string specifies the user's default settings. If the
	modification of the locale fails, the exception :exc:`Error` is raised.  If
	successful, the new locale setting is returned.
	
	If *locale* is omitted or ``None``, the current setting for *category* is
	returned.
	
	:func:`setlocale` is not thread-safe on most systems. Applications typically
	start with a call of ::
	
	import locale
	locale.setlocale(locale.LC_ALL, '')
	
	This sets the locale for all categories to the user's default setting (typically
	specified in the :envvar:`LANG` environment variable).  If the locale is not
	changed thereafter, using multithreading should not cause problems.
	
	"""
	pass
	
def localeconv():
	"""
	Returns the database of the local conventions as a dictionary. This dictionary
	has the following strings as keys:
	
	+----------------------+-------------------------------------+--------------------------------+
	| Category             | Key                                 | Meaning                        |
	+======================+=====================================+================================+
	| :const:`LC_NUMERIC`  | ``'decimal_point'``                 | Decimal point character.       |
	+----------------------+-------------------------------------+--------------------------------+
	|                      | ``'grouping'``                      | Sequence of numbers specifying |
	|                      |                                     | which relative positions the   |
	|                      |                                     | ``'thousands_sep'`` is         |
	|                      |                                     | expected.  If the sequence is  |
	|                      |                                     | terminated with                |
	|                      |                                     | :const:`CHAR_MAX`, no further  |
	|                      |                                     | grouping is performed. If the  |
	|                      |                                     | sequence terminates with a     |
	|                      |                                     | ``0``,  the last group size is |
	|                      |                                     | repeatedly used.               |
	+----------------------+-------------------------------------+--------------------------------+
	|                      | ``'thousands_sep'``                 | Character used between groups. |
	+----------------------+-------------------------------------+--------------------------------+
	| :const:`LC_MONETARY` | ``'int_curr_symbol'``               | International currency symbol. |
	+----------------------+-------------------------------------+--------------------------------+
	|                      | ``'currency_symbol'``               | Local currency symbol.         |
	+----------------------+-------------------------------------+--------------------------------+
	|                      | ``'p_cs_precedes/n_cs_precedes'``   | Whether the currency symbol    |
	|                      |                                     | precedes the value (for        |
	|                      |                                     | positive resp. negative        |
	|                      |                                     | values).                       |
	+----------------------+-------------------------------------+--------------------------------+
	|                      | ``'p_sep_by_space/n_sep_by_space'`` | Whether the currency symbol is |
	|                      |                                     | separated from the value  by a |
	|                      |                                     | space (for positive resp.      |
	|                      |                                     | negative values).              |
	+----------------------+-------------------------------------+--------------------------------+
	|                      | ``'mon_decimal_point'``             | Decimal point used for         |
	|                      |                                     | monetary values.               |
	+----------------------+-------------------------------------+--------------------------------+
	|                      | ``'frac_digits'``                   | Number of fractional digits    |
	|                      |                                     | used in local formatting of    |
	|                      |                                     | monetary values.               |
	+----------------------+-------------------------------------+--------------------------------+
	|                      | ``'int_frac_digits'``               | Number of fractional digits    |
	|                      |                                     | used in international          |
	|                      |                                     | formatting of monetary values. |
	+----------------------+-------------------------------------+--------------------------------+
	|                      | ``'mon_thousands_sep'``             | Group separator used for       |
	|                      |                                     | monetary values.               |
	+----------------------+-------------------------------------+--------------------------------+
	|                      | ``'mon_grouping'``                  | Equivalent to ``'grouping'``,  |
	|                      |                                     | used for monetary values.      |
	+----------------------+-------------------------------------+--------------------------------+
	|                      | ``'positive_sign'``                 | Symbol used to annotate a      |
	|                      |                                     | positive monetary value.       |
	+----------------------+-------------------------------------+--------------------------------+
	|                      | ``'negative_sign'``                 | Symbol used to annotate a      |
	|                      |                                     | negative monetary value.       |
	+----------------------+-------------------------------------+--------------------------------+
	|                      | ``'p_sign_posn/n_sign_posn'``       | The position of the sign (for  |
	|                      |                                     | positive resp. negative        |
	|                      |                                     | values), see below.            |
	+----------------------+-------------------------------------+--------------------------------+
	
	All numeric values can be set to :const:`CHAR_MAX` to indicate that there is no
	value specified in this locale.
	
	The possible values for ``'p_sign_posn'`` and ``'n_sign_posn'`` are given below.
	
	+--------------+-----------------------------------------+
	| Value        | Explanation                             |
	+==============+=========================================+
	| ``0``        | Currency and value are surrounded by    |
	|              | parentheses.                            |
	+--------------+-----------------------------------------+
	| ``1``        | The sign should precede the value and   |
	|              | currency symbol.                        |
	+--------------+-----------------------------------------+
	| ``2``        | The sign should follow the value and    |
	|              | currency symbol.                        |
	+--------------+-----------------------------------------+
	| ``3``        | The sign should immediately precede the |
	|              | value.                                  |
	+--------------+-----------------------------------------+
	| ``4``        | The sign should immediately follow the  |
	|              | value.                                  |
	+--------------+-----------------------------------------+
	| ``CHAR_MAX`` | Nothing is specified in this locale.    |
	+--------------+-----------------------------------------+
	
	
	"""
	pass
	
def nl_langinfo(option):
	"""
	Return some locale-specific information as a string.  This function is not
	available on all systems, and the set of possible options might also vary
	across platforms.  The possible argument values are numbers, for which
	symbolic constants are available in the locale module.
	
	The :func:`nl_langinfo` function accepts one of the following keys.  Most
	descriptions are taken from the corresponding description in the GNU C
	library.
	
	"""
	pass
	
def getdefaultlocale(envvars):
	"""
	Tries to determine the default locale settings and returns them as a tuple of
	the form ``(language code, encoding)``.
	
	According to POSIX, a program which has not called ``setlocale(LC_ALL, '')``
	runs using the portable ``'C'`` locale.  Calling ``setlocale(LC_ALL, '')`` lets
	it use the default locale as defined by the :envvar:`LANG` variable.  Since we
	do not want to interfere with the current locale setting we thus emulate the
	behavior in the way described above.
	
	To maintain compatibility with other platforms, not only the :envvar:`LANG`
	variable is tested, but a list of variables given as envvars parameter.  The
	first found to be defined will be used.  *envvars* defaults to the search path
	used in GNU gettext; it must always contain the variable name ``LANG``.  The GNU
	gettext search path contains ``'LANGUAGE'``, ``'LC_ALL'``, ``'LC_CTYPE'``, and
	``'LANG'``, in that order.
	
	Except for the code ``'C'``, the language code corresponds to :rfc:`1766`.
	*language code* and *encoding* may be ``None`` if their values cannot be
	determined.
	
	"""
	pass
	
def getlocale(category):
	"""
	Returns the current setting for the given locale category as sequence containing
	*language code*, *encoding*. *category* may be one of the :const:`LC_\*` values
	except :const:`LC_ALL`.  It defaults to :const:`LC_CTYPE`.
	
	Except for the code ``'C'``, the language code corresponds to :rfc:`1766`.
	*language code* and *encoding* may be ``None`` if their values cannot be
	determined.
	
	"""
	pass
	
def getpreferredencoding(do_setlocale):
	"""
	Return the encoding used for text data, according to user preferences.  User
	preferences are expressed differently on different systems, and might not be
	available programmatically on some systems, so this function only returns a
	guess.
	
	On some systems, it is necessary to invoke :func:`setlocale` to obtain the user
	preferences, so this function is not thread-safe. If invoking setlocale is not
	necessary or desired, *do_setlocale* should be set to ``False``.
	
	"""
	pass
	
def normalize(localename):
	"""
	Returns a normalized locale code for the given locale name.  The returned locale
	code is formatted for use with :func:`setlocale`.  If normalization fails, the
	original name is returned unchanged.
	
	If the given encoding is not known, the function defaults to the default
	encoding for the locale code just like :func:`setlocale`.
	
	"""
	pass
	
def resetlocale(category):
	"""
	Sets the locale for *category* to the default setting.
	
	The default setting is determined by calling :func:`getdefaultlocale`.
	*category* defaults to :const:`LC_ALL`.
	
	"""
	pass
	
def strcoll(string1,string2):
	"""
	Compares two strings according to the current :const:`LC_COLLATE` setting. As
	any other compare function, returns a negative, or a positive value, or ``0``,
	depending on whether *string1* collates before or after *string2* or is equal to
	it.
	
	
	"""
	pass
	
def strxfrm(string):
	"""
	"""
	pass
	
def format(format,val,grouping,monetary):
	"""
	Formats a number *val* according to the current :const:`LC_NUMERIC` setting.
	The format follows the conventions of the ``%`` operator.  For floating point
	values, the decimal point is modified if appropriate.  If *grouping* is true,
	also takes the grouping into account.
	
	If *monetary* is true, the conversion uses monetary thousands separator and
	grouping strings.
	
	Please note that this function will only work for exactly one %char specifier.
	For whole format strings, use :func:`format_string`.
	
	"""
	pass
	
def format_string(format,val,grouping):
	"""
	Processes formatting specifiers as in ``format % val``, but takes the current
	locale settings into account.
	
	"""
	pass
	
def currency(val,symbol,grouping,international):
	"""
	Formats a number *val* according to the current :const:`LC_MONETARY` settings.
	
	The returned string includes the currency symbol if *symbol* is true, which is
	the default. If *grouping* is true (which is not the default), grouping is done
	with the value. If *international* is true (which is not the default), the
	international currency symbol is used.
	
	Note that this function will not work with the 'C' locale, so you have to set a
	locale via :func:`setlocale` first.
	
	"""
	pass
	
def str(float):
	"""
	Formats a floating point number using the same format as the built-in function
	``str(float)``, but takes the decimal point into account.
	
	
	"""
	pass
	
def atof(string):
	"""
	Converts a string to a floating point number, following the :const:`LC_NUMERIC`
	settings.
	
	
	"""
	pass
	
def atoi(string):
	"""
	Converts a string to an integer, following the :const:`LC_NUMERIC` conventions.
	
	
	"""
	pass
	
