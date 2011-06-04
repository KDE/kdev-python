#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
""":synopsis: Common string operations.


"""
"""
The concatenation of the :const:`ascii_lowercase` and :const:`ascii_uppercase`
constants described below.  This value is not locale-dependent.


"""
ascii_letters = None
"""
The lowercase letters ``'abcdefghijklmnopqrstuvwxyz'``.  This value is not
locale-dependent and will not change.


"""
ascii_lowercase = None
"""
The uppercase letters ``'ABCDEFGHIJKLMNOPQRSTUVWXYZ'``.  This value is not
locale-dependent and will not change.


"""
ascii_uppercase = None
"""
The string ``'0123456789'``.


"""
digits = None
"""
The string ``'0123456789abcdefABCDEF'``.


"""
hexdigits = None
"""
The concatenation of the strings :const:`lowercase` and :const:`uppercase`
described below.  The specific value is locale-dependent, and will be updated
when :func:`locale.setlocale` is called.


"""
letters = None
"""
A string containing all the characters that are considered lowercase letters.
On most systems this is the string ``'abcdefghijklmnopqrstuvwxyz'``.  The
specific value is locale-dependent, and will be updated when
:func:`locale.setlocale` is called.


"""
lowercase = None
"""
The string ``'01234567'``.


"""
octdigits = None
"""
String of ASCII characters which are considered punctuation characters in the
``C`` locale.


"""
punctuation = None
"""
String of characters which are considered printable.  This is a combination of
:const:`digits`, :const:`letters`, :const:`punctuation`, and
:const:`whitespace`.


"""
printable = None
"""
A string containing all the characters that are considered uppercase letters.
On most systems this is the string ``'ABCDEFGHIJKLMNOPQRSTUVWXYZ'``.  The
specific value is locale-dependent, and will be updated when
:func:`locale.setlocale` is called.


"""
uppercase = None
"""
A string containing all characters that are considered whitespace. On most
systems this includes the characters space, tab, linefeed, return, formfeed, and
vertical tab.


.. tring Formatting
-----------------

"""
whitespace = None
class Formatter:


	"""
	The :class:`Formatter` class has the following public methods:
	
	"""
	
	
	def __init__(self, ):
		pass
	
	def format(self, format_string,args,kwargs):
		"""
		:meth:`format` is the primary API method.  It takes a format template
		string, and an arbitrary set of positional and keyword argument.
		:meth:`format` is just a wrapper that calls :meth:`vformat`.
		
		"""
		pass
		
	def vformat(self, format_string,args,kwargs):
		"""
		This function does the actual work of formatting.  It is exposed as a
		separate function for cases where you want to pass in a predefined
		dictionary of arguments, rather than unpacking and repacking the
		dictionary as individual arguments using the ``*args`` and ``**kwds``
		syntax.  :meth:`vformat` does the work of breaking up the format template
		string into character data and replacement fields.  It calls the various
		methods described below.
		
		In addition, the :class:`Formatter` defines a number of methods that are
		intended to be replaced by subclasses:
		
		"""
		pass
		
	def parse(self, format_string):
		"""
		Loop over the format_string and return an iterable of tuples
		(*literal_text*, *field_name*, *format_spec*, *conversion*).  This is used
		by :meth:`vformat` to break the string into either literal text, or
		replacement fields.
		
		The values in the tuple conceptually represent a span of literal text
		followed by a single replacement field.  If there is no literal text
		(which can happen if two replacement fields occur consecutively), then
		*literal_text* will be a zero-length string.  If there is no replacement
		field, then the values of *field_name*, *format_spec* and *conversion*
		will be ``None``.
		
		"""
		pass
		
	def get_field(self, field_name,args,kwargs):
		"""
		Given *field_name* as returned by :meth:`parse` (see above), convert it to
		an object to be formatted.  Returns a tuple (obj, used_key).  The default
		version takes strings of the form defined in :pep:`3101`, such as
		"0[name]" or "label.title".  *args* and *kwargs* are as passed in to
		:meth:`vformat`.  The return value *used_key* has the same meaning as the
		*key* parameter to :meth:`get_value`.
		
		"""
		pass
		
	def get_value(self, key,args,kwargs):
		"""
		Retrieve a given field value.  The *key* argument will be either an
		integer or a string.  If it is an integer, it represents the index of the
		positional argument in *args*; if it is a string, then it represents a
		named argument in *kwargs*.
		
		The *args* parameter is set to the list of positional arguments to
		:meth:`vformat`, and the *kwargs* parameter is set to the dictionary of
		keyword arguments.
		
		For compound field names, these functions are only called for the first
		component of the field name; Subsequent components are handled through
		normal attribute and indexing operations.
		
		So for example, the field expression '0.name' would cause
		:meth:`get_value` to be called with a *key* argument of 0.  The ``name``
		attribute will be looked up after :meth:`get_value` returns by calling the
		built-in :func:`getattr` function.
		
		If the index or keyword refers to an item that does not exist, then an
		:exc:`IndexError` or :exc:`KeyError` should be raised.
		
		"""
		pass
		
	def check_unused_args(self, used_args,args,kwargs):
		"""
		Implement checking for unused arguments if desired.  The arguments to this
		function is the set of all argument keys that were actually referred to in
		the format string (integers for positional arguments, and strings for
		named arguments), and a reference to the *args* and *kwargs* that was
		passed to vformat.  The set of unused args can be calculated from these
		parameters.  :meth:`check_unused_args` is assumed to raise an exception if
		the check fails.
		
		"""
		pass
		
	def format_field(self, value,format_spec):
		"""
		:meth:`format_field` simply calls the global :func:`format` built-in.  The
		method is provided so that subclasses can override it.
		
		"""
		pass
		
	def convert_field(self, value,conversion):
		"""
		Converts the value (returned by :meth:`get_field`) given a conversion type
		(as in the tuple returned by the :meth:`parse` method).  The default
		version understands 'r' (repr) and 's' (str) conversion types.
		
		
		.. ormat String Syntax
		"""
		pass
		
	


class Template:


	"""
	The constructor takes a single argument which is the template string.
	
	
	"""
	
	
	def __init__(self, ):
		pass
	
	def substitute(self, mapping,kws):
		"""
		Performs the template substitution, returning a new string.  *mapping* is
		any dictionary-like object with keys that match the placeholders in the
		template.  Alternatively, you can provide keyword arguments, where the
		keywords are the placeholders.  When both *mapping* and *kws* are given
		and there are duplicates, the placeholders from *kws* take precedence.
		
		
		"""
		pass
		
	def safe_substitute(self, mapping,kws):
		"""
		Like :meth:`substitute`, except that if placeholders are missing from
		*mapping* and *kws*, instead of raising a :exc:`KeyError` exception, the
		original placeholder will appear in the resulting string intact.  Also,
		unlike with :meth:`substitute`, any other appearances of the ``$`` will
		simply return ``$`` instead of raising :exc:`ValueError`.
		
		While other exceptions may still occur, this method is called "safe"
		because substitutions always tries to return a usable string instead of
		raising an exception.  In another sense, :meth:`safe_substitute` may be
		anything other than safe, since it will silently ignore malformed
		templates containing dangling delimiters, unmatched braces, or
		placeholders that are not valid Python identifiers.
		
		:class:`Template` instances also provide one public data attribute:
		
		"""
		pass
		
	def capwords(self, s,sep):
		"""
		Split the argument into words using :meth:`str.split`, capitalize each word
		using :meth:`str.capitalize`, and join the capitalized words using
		:meth:`str.join`.  If the optional second argument *sep* is absent
		or ``None``, runs of whitespace characters are replaced by a single space
		and leading and trailing whitespace are removed, otherwise *sep* is used to
		split and join the words.
		
		
		"""
		pass
		
	def maketrans(self, _from,to):
		"""
		Return a translation table suitable for passing to :func:`translate`, that will
		map each character in *from* into the character at the same position in *to*;
		*from* and *to* must have the same length.
		
		"""
		pass
		
	def atof(self, s):
		"""
		"""
		pass
		
	def atoi(self, s,base):
		"""
		"""
		pass
		
	def atol(self, s,base):
		"""
		"""
		pass
		
	def capitalize(self, word):
		"""
		Return a copy of *word* with only its first character capitalized.
		
		
		"""
		pass
		
	def expandtabs(self, s,tabsize):
		"""
		Expand tabs in a string replacing them by one or more spaces, depending on the
		current column and the given tab size.  The column number is reset to zero after
		each newline occurring in the string. This doesn't understand other non-printing
		characters or escape sequences.  The tab size defaults to 8.
		
		
		"""
		pass
		
	def find(self, s,sub,start,end):
		"""
		Return the lowest index in *s* where the substring *sub* is found such that
		*sub* is wholly contained in ``s[start:end]``.  Return ``-1`` on failure.
		Defaults for *start* and *end* and interpretation of negative values is the same
		as for slices.
		
		
		"""
		pass
		
	def rfind(self, s,sub,start,end):
		"""
		Like :func:`find` but find the highest index.
		
		
		"""
		pass
		
	def index(self, s,sub,start,end):
		"""
		Like :func:`find` but raise :exc:`ValueError` when the substring is not found.
		
		
		"""
		pass
		
	def rindex(self, s,sub,start,end):
		"""
		Like :func:`rfind` but raise :exc:`ValueError` when the substring is not found.
		
		
		"""
		pass
		
	def count(self, s,sub,start,end):
		"""
		Return the number of (non-overlapping) occurrences of substring *sub* in string
		``s[start:end]``. Defaults for *start* and *end* and interpretation of negative
		values are the same as for slices.
		
		
		"""
		pass
		
	def lower(self, s):
		"""
		Return a copy of *s*, but with upper case letters converted to lower case.
		
		
		"""
		pass
		
	def split(self, s,sep,maxsplit):
		"""
		Return a list of the words of the string *s*.  If the optional second argument
		*sep* is absent or ``None``, the words are separated by arbitrary strings of
		whitespace characters (space, tab,  newline, return, formfeed).  If the second
		argument *sep* is present and not ``None``, it specifies a string to be used as
		the  word separator.  The returned list will then have one more item than the
		number of non-overlapping occurrences of the separator in the string.  The
		optional third argument *maxsplit* defaults to 0.  If it is nonzero, at most
		*maxsplit* number of splits occur, and the remainder of the string is returned
		as the final element of the list (thus, the list will have at most
		``maxsplit+1`` elements).
		
		The behavior of split on an empty string depends on the value of *sep*. If *sep*
		is not specified, or specified as ``None``, the result will be an empty list.
		If *sep* is specified as any string, the result will be a list containing one
		element which is an empty string.
		
		
		"""
		pass
		
	def rsplit(self, s,sep,maxsplit):
		"""
		Return a list of the words of the string *s*, scanning *s* from the end.  To all
		intents and purposes, the resulting list of words is the same as returned by
		:func:`split`, except when the optional third argument *maxsplit* is explicitly
		specified and nonzero.  When *maxsplit* is nonzero, at most *maxsplit* number of
		splits -- the *rightmost* ones -- occur, and the remainder of the string is
		returned as the first element of the list (thus, the list will have at most
		``maxsplit+1`` elements).
		
		"""
		pass
		
	def splitfields(self, s,sep,maxsplit):
		"""
		This function behaves identically to :func:`split`.  (In the past, :func:`split`
		was only used with one argument, while :func:`splitfields` was only used with
		two arguments.)
		
		
		"""
		pass
		
	def join(self, words,sep):
		"""
		Concatenate a list or tuple of words with intervening occurrences of  *sep*.
		The default value for *sep* is a single space character.  It is always true that
		``string.join(string.split(s, sep), sep)`` equals *s*.
		
		
		"""
		pass
		
	def joinfields(self, words,sep):
		"""
		This function behaves identically to :func:`join`.  (In the past,  :func:`join`
		was only used with one argument, while :func:`joinfields` was only used with two
		arguments.) Note that there is no :meth:`joinfields` method on string objects;
		use the :meth:`join` method instead.
		
		
		"""
		pass
		
	def lstrip(self, s,chars):
		"""
		Return a copy of the string with leading characters removed.  If *chars* is
		omitted or ``None``, whitespace characters are removed.  If given and not
		``None``, *chars* must be a string; the characters in the string will be
		stripped from the beginning of the string this method is called on.
		
		"""
		pass
		
	def rstrip(self, s,chars):
		"""
		Return a copy of the string with trailing characters removed.  If *chars* is
		omitted or ``None``, whitespace characters are removed.  If given and not
		``None``, *chars* must be a string; the characters in the string will be
		stripped from the end of the string this method is called on.
		
		"""
		pass
		
	def strip(self, s,chars):
		"""
		Return a copy of the string with leading and trailing characters removed.  If
		*chars* is omitted or ``None``, whitespace characters are removed.  If given and
		not ``None``, *chars* must be a string; the characters in the string will be
		stripped from the both ends of the string this method is called on.
		
		"""
		pass
		
	def swapcase(self, s):
		"""
		Return a copy of *s*, but with lower case letters converted to upper case and
		vice versa.
		
		
		"""
		pass
		
	def translate(self, s,table,deletechars):
		"""
		Delete all characters from *s* that are in *deletechars* (if  present), and then
		translate the characters using *table*, which  must be a 256-character string
		giving the translation for each character value, indexed by its ordinal.  If
		*table* is ``None``, then only the character deletion step is performed.
		
		
		"""
		pass
		
	def upper(self, s):
		"""
		Return a copy of *s*, but with lower case letters converted to upper case.
		
		
		"""
		pass
		
	def ljust(self, s,width,fillchar):
		"""rjust(s, width[, fillchar])
		center(s, width[, fillchar])
		
		These functions respectively left-justify, right-justify and center a string in
		a field of given width.  They return a string that is at least *width*
		characters wide, created by padding the string *s* with the character *fillchar*
		(default is a space) until the given width on the right, left or both sides.
		The string is never truncated.
		
		
		"""
		pass
		
	def zfill(self, s,width):
		"""
		Pad a numeric string on the left with zero digits until the given width is
		reached.  Strings starting with a sign are handled correctly.
		
		
		"""
		pass
		
	


