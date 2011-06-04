#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
""":synopsis: Regular expression operations.
"""
"""IGNORECASE

Perform case-insensitive matching; expressions like ``[A-Z]`` will match
lowercase letters, too.  This is not affected by the current locale.


"""
I = None
"""LOCALE

Make ``\w``, ``\W``, ``\b``, ``\B``, ``\s`` and ``\S`` dependent on the
current locale.


"""
L = None
"""MULTILINE

When specified, the pattern character ``'^'`` matches at the beginning of the
string and at the beginning of each line (immediately following each newline);
and the pattern character ``'$'`` matches at the end of the string and at the
end of each line (immediately preceding each newline).  By default, ``'^'``
matches only at the beginning of the string, and ``'$'`` only at the end of the
string and immediately before the newline (if any) at the end of the string.


"""
M = None
"""DOTALL

Make the ``'.'`` special character match any character at all, including a
newline; without this flag, ``'.'`` will match anything *except* a newline.


"""
S = None
"""UNICODE

Make ``\w``, ``\W``, ``\b``, ``\B``, ``\d``, ``\D``, ``\s`` and ``\S`` dependent
on the Unicode character properties database.

"""
U = None
"""VERBOSE

This flag allows you to write regular expressions that look nicer. Whitespace
within the pattern is ignored, except when in a character class or preceded by
an unescaped backslash, and, when a line contains a ``'#'`` neither in a
character class or preceded by an unescaped backslash, all characters from the
leftmost such ``'#'`` through the end of the line are ignored.

That means that the two following regular expression objects that match a
decimal number are functionally equal::

a = re.compile(r " " " \d +  # the integral part
\.    # the decimal point
\d *  # some fractional digits " " " , re.X)
b = re.compile(r"\d+\.\d*")


"""
X = None
def compile(pattern,flags):
	"""
	Compile a regular expression pattern into a regular expression object, which
	can be used for matching using its :func:`match` and :func:`search` methods,
	described below.
	
	The expression's behaviour can be modified by specifying a *flags* value.
	Values can be any of the following variables, combined using bitwise OR (the
	``|`` operator).
	
	The sequence ::
	
	prog = re.compile(pattern)
	result = prog.match(string)
	
	is equivalent to ::
	
	result = re.match(pattern, string)
	
	but using :func:`re.compile` and saving the resulting regular expression
	object for reuse is more efficient when the expression will be used several
	times in a single program.
	
	"""
	pass
	
def search(pattern,string,flags):
	"""
	Scan through *string* looking for a location where the regular expression
	*pattern* produces a match, and return a corresponding :class:`MatchObject`
	instance. Return ``None`` if no position in the string matches the pattern; note
	that this is different from finding a zero-length match at some point in the
	string.
	
	
	"""
	pass
	
def match(pattern,string,flags):
	"""
	If zero or more characters at the beginning of *string* match the regular
	expression *pattern*, return a corresponding :class:`MatchObject` instance.
	Return ``None`` if the string does not match the pattern; note that this is
	different from a zero-length match.
	
	"""
	pass
	
def split(pattern,string,maxsplit=0,flags=0):
	"""
	Split *string* by the occurrences of *pattern*.  If capturing parentheses are
	used in *pattern*, then the text of all groups in the pattern are also returned
	as part of the resulting list. If *maxsplit* is nonzero, at most *maxsplit*
	splits occur, and the remainder of the string is returned as the final element
	of the list.  (Incompatibility note: in the original Python 1.5 release,
	*maxsplit* was ignored.  This has been fixed in later releases.)
	
	>>> re.split('\W+', 'Words, words, words.')
	['Words', 'words', 'words', '']
	>>> re.split('(\W+)', 'Words, words, words.')
	['Words', ', ', 'words', ', ', 'words', '.', '']
	>>> re.split('\W+', 'Words, words, words.', 1)
	['Words', 'words, words.']
	>>> re.split('[a-f]+', '0a3B9', flags=re.IGNORECASE)
	['0', '3', '9']
	
	If there are capturing groups in the separator and it matches at the start of
	the string, the result will start with an empty string.  The same holds for
	the end of the string:
	
	>>> re.split('(\W+)', '*morewords, words*more')
	['', '*more', 'words', ', ', 'words', '*more', '']
	
	That way, separator components are always found at the same relative
	indices within the result list (e.g., if there's one capturing group
	in the separator, the 0th, the 2nd and so forth).
	
	Note that *split* will never split a string on an empty pattern match.
	For example:
	
	>>> re.split('x*', 'foo')
	['foo']
	>>> re.split("(?m)^$", "foo\n\nbar\n")
	['foo\n\nbar\n']
	
	"""
	pass
	
def findall(pattern,string,flags):
	"""
	Return all non-overlapping matches of *pattern* in *string*, as a list of
	strings.  The *string* is scanned left-to-right, and matches are returned in
	the order found.  If one or more groups are present in the pattern, return a
	list of groups; this will be a list of tuples if the pattern has more than
	one group.  Empty matches are included in the result unless they touch the
	beginning of another match.
	
	"""
	pass
	
def finditer(pattern,string,flags):
	"""
	Return an :term:`iterator` yielding :class:`MatchObject` instances over all
	non-overlapping matches for the RE *pattern* in *string*.  The *string* is
	scanned left-to-right, and matches are returned in the order found.  Empty
	matches are included in the result unless they touch the beginning of another
	match.
	
	"""
	pass
	
def sub(pattern,repl,string,count,flags):
	"""
	Return the string obtained by replacing the leftmost non-overlapping occurrences
	of *pattern* in *string* by the replacement *repl*.  If the pattern isn't found,
	*string* is returned unchanged.  *repl* can be a string or a function; if it is
	a string, any backslash escapes in it are processed.  That is, ``\n`` is
	converted to a single newline character, ``\r`` is converted to a linefeed, and
	so forth.  Unknown escapes such as ``\j`` are left alone.  Backreferences, such
	as ``\6``, are replaced with the substring matched by group 6 in the pattern.
	For example:
	
	>>> re.sub(r'def\s+([a-zA-Z_][a-zA-Z_0-9]*)\s*\(\s*\):',
	*more        r'static PyObject*\npy_\1(void)\n{',
	*more        'def myfunc():')
	'static PyObject*\npy_myfunc(void)\n{'
	
	If *repl* is a function, it is called for every non-overlapping occurrence of
	*pattern*.  The function takes a single match object argument, and returns the
	replacement string.  For example:
	
	>>> def dashrepl(matchobj):
	*more     if matchobj.group(0) == '-': return ' '
	*more     else: return '-'
	>>> re.sub('-{1,2}', dashrepl, 'pro----gram-files')
	'pro--gram files'
	>>> re.sub(r'\sAND\s', ' & ', 'Baked Beans And Spam', flags=re.IGNORECASE)
	'Baked Beans & Spam'
	
	The pattern may be a string or an RE object.
	
	The optional argument *count* is the maximum number of pattern occurrences to be
	replaced; *count* must be a non-negative integer.  If omitted or zero, all
	occurrences will be replaced. Empty matches for the pattern are replaced only
	when not adjacent to a previous match, so ``sub('x*', '-', 'abc')`` returns
	``'-a-b-c-'``.
	
	In addition to character escapes and backreferences as described above,
	``\g<name>`` will use the substring matched by the group named ``name``, as
	defined by the ``(?P<name>*more)`` syntax. ``\g<number>`` uses the corresponding
	group number; ``\g<2>`` is therefore equivalent to ``\2``, but isn't ambiguous
	in a replacement such as ``\g<2>0``.  ``\20`` would be interpreted as a
	reference to group 20, not a reference to group 2 followed by the literal
	character ``'0'``.  The backreference ``\g<0>`` substitutes in the entire
	substring matched by the RE.
	
	"""
	pass
	
def subn(pattern,repl,string,count,flags):
	"""
	Perform the same operation as :func:`sub`, but return a tuple ``(new_string,
	number_of_subs_made)``.
	
	"""
	pass
	
def escape(string):
	"""
	Return *string* with all non-alphanumerics backslashed; this is useful if you
	want to match an arbitrary literal string that may have regular expression
	metacharacters in it.
	
	
	"""
	pass
	
def purge():
	"""
	Clear the regular expression cache.
	
	
	"""
	pass
	
class RegexObject:


	"""
	The :class:`RegexObject` class supports the following methods and attributes:
	
	"""
	
	
	def __init__(self, ):
		pass
	
	


class MatchObject:


	"""
	Match Objects always have a boolean value of :const:`True`, so that you can test
	whether e.g. :func:`match` resulted in a match with a simple if statement.  They
	support the following methods and attributes:
	
	
	"""
	
	
	def __init__(self, ):
		pass
	
	


