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
	
	>>> re.split('(\W+)', 'morewords, wordsmore')
	['', 'more', 'words', ', ', 'words', 'more', '']
	
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
	more        r'static PyObject*\npy_\1(void)\n{',
	more        'def myfunc():')
	'static PyObject*\npy_myfunc(void)\n{'
	
	If *repl* is a function, it is called for every non-overlapping occurrence of
	*pattern*.  The function takes a single match object argument, and returns the
	replacement string.  For example:
	
	>>> def dashrepl(matchobj):
	more     if matchobj.group(0) == '-': return ' '
	more     else: return '-'
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
	defined by the ``(?P<name>more)`` syntax. ``\g<number>`` uses the corresponding
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
	
	def search(self, string,pos,endpos):
		"""
		Scan through *string* looking for a location where this regular expression
		produces a match, and return a corresponding :class:`MatchObject` instance.
		Return ``None`` if no position in the string matches the pattern; note that this
		is different from finding a zero-length match at some point in the string.
		
		The optional second parameter *pos* gives an index in the string where the
		search is to start; it defaults to ``0``.  This is not completely equivalent to
		slicing the string; the ``'^'`` pattern character matches at the real beginning
		of the string and at positions just after a newline, but not necessarily at the
		index where the search is to start.
		
		The optional parameter *endpos* limits how far the string will be searched; it
		will be as if the string is *endpos* characters long, so only the characters
		from *pos* to ``endpos - 1`` will be searched for a match.  If *endpos* is less
		than *pos*, no match will be found, otherwise, if *rx* is a compiled regular
		expression object, ``rx.search(string, 0, 50)`` is equivalent to
		``rx.search(string[:50], 0)``.
		
		>>> pattern = re.compile("d")
		>>> pattern.search("dog")     # Match at index 0
		<_sre.SRE_Match object at more>
		>>> pattern.search("dog", 1)  # No match; search doesn't include the "d"
		
		
		"""
		pass
		
	def match(self, string,pos,endpos):
		"""
		If zero or more characters at the *beginning* of *string* match this regular
		expression, return a corresponding :class:`MatchObject` instance.  Return
		``None`` if the string does not match the pattern; note that this is different
		from a zero-length match.
		
		The optional *pos* and *endpos* parameters have the same meaning as for the
		:meth:`~RegexObject.search` method.
		
		"""
		pass
		
	def split(self, string,maxsplit=0):
		"""
		Identical to the :func:`split` function, using the compiled pattern.
		
		
		"""
		pass
		
	def findall(self, string,pos,endpos):
		"""
		Similar to the :func:`findall` function, using the compiled pattern, but
		also accepts optional *pos* and *endpos* parameters that limit the search
		region like for :meth:`match`.
		
		
		"""
		pass
		
	def finditer(self, string,pos,endpos):
		"""
		Similar to the :func:`finditer` function, using the compiled pattern, but
		also accepts optional *pos* and *endpos* parameters that limit the search
		region like for :meth:`match`.
		
		
		"""
		pass
		
	def sub(self, repl,string,count=0):
		"""
		Identical to the :func:`sub` function, using the compiled pattern.
		
		
		"""
		pass
		
	def subn(self, repl,string,count=0):
		"""
		Identical to the :func:`subn` function, using the compiled pattern.
		
		
		"""
		pass
		
	


class MatchObject:


	"""
	Match Objects always have a boolean value of :const:`True`, so that you can test
	whether e.g. :func:`match` resulted in a match with a simple if statement.  They
	support the following methods and attributes:
	
	
	"""
	
	
	def __init__(self, ):
		pass
	
	def expand(self, template):
		"""
		Return the string obtained by doing backslash substitution on the template
		string *template*, as done by the :meth:`~RegexObject.sub` method.  Escapes
		such as ``\n`` are converted to the appropriate characters, and numeric
		backreferences (``\1``, ``\2``) and named backreferences (``\g<1>``,
		``\g<name>``) are replaced by the contents of the corresponding group.
		
		
		"""
		pass
		
	def group(self, group1,more):
		"""
		Returns one or more subgroups of the match.  If there is a single argument, the
		result is a single string; if there are multiple arguments, the result is a
		tuple with one item per argument. Without arguments, *group1* defaults to zero
		(the whole match is returned). If a *groupN* argument is zero, the corresponding
		return value is the entire matching string; if it is in the inclusive range
		[1..99], it is the string matching the corresponding parenthesized group.  If a
		group number is negative or larger than the number of groups defined in the
		pattern, an :exc:`IndexError` exception is raised. If a group is contained in a
		part of the pattern that did not match, the corresponding result is ``None``.
		If a group is contained in a part of the pattern that matched multiple times,
		the last match is returned.
		
		>>> m = re.match(r"(\w+) (\w+)", "Isaac Newton, physicist")
		>>> m.group(0)       # The entire match
		'Isaac Newton'
		>>> m.group(1)       # The first parenthesized subgroup.
		'Isaac'
		>>> m.group(2)       # The second parenthesized subgroup.
		'Newton'
		>>> m.group(1, 2)    # Multiple arguments give us a tuple.
		('Isaac', 'Newton')
		
		If the regular expression uses the ``(?P<name>more)`` syntax, the *groupN*
		arguments may also be strings identifying groups by their group name.  If a
		string argument is not used as a group name in the pattern, an :exc:`IndexError`
		exception is raised.
		
		A moderately complicated example:
		
		>>> m = re.match(r"(?P<first_name>\w+) (?P<last_name>\w+)", "Malcolm Reynolds")
		>>> m.group('first_name')
		'Malcolm'
		>>> m.group('last_name')
		'Reynolds'
		
		Named groups can also be referred to by their index:
		
		>>> m.group(1)
		'Malcolm'
		>>> m.group(2)
		'Reynolds'
		
		If a group matches multiple times, only the last match is accessible:
		
		>>> m = re.match(r"(..)+", "a1b2c3")  # Matches 3 times.
		>>> m.group(1)                        # Returns only the last match.
		'c3'
		
		
		"""
		pass
		
	def groups(self, default):
		"""
		Return a tuple containing all the subgroups of the match, from 1 up to however
		many groups are in the pattern.  The *default* argument is used for groups that
		did not participate in the match; it defaults to ``None``.  (Incompatibility
		note: in the original Python 1.5 release, if the tuple was one element long, a
		string would be returned instead.  In later versions (from 1.5.1 on), a
		singleton tuple is returned in such cases.)
		
		For example:
		
		>>> m = re.match(r"(\d+)\.(\d+)", "24.1632")
		>>> m.groups()
		('24', '1632')
		
		If we make the decimal place and everything after it optional, not all groups
		might participate in the match.  These groups will default to ``None`` unless
		the *default* argument is given:
		
		>>> m = re.match(r"(\d+)\.?(\d+)?", "24")
		>>> m.groups()      # Second group defaults to None.
		('24', None)
		>>> m.groups('0')   # Now, the second group defaults to '0'.
		('24', '0')
		
		
		"""
		pass
		
	def groupdict(self, default):
		"""
		Return a dictionary containing all the *named* subgroups of the match, keyed by
		the subgroup name.  The *default* argument is used for groups that did not
		participate in the match; it defaults to ``None``.  For example:
		
		>>> m = re.match(r"(?P<first_name>\w+) (?P<last_name>\w+)", "Malcolm Reynolds")
		>>> m.groupdict()
		{'first_name': 'Malcolm', 'last_name': 'Reynolds'}
		
		
		"""
		pass
		
	def start(self, group):
		"""MatchObject.end([group])
		
		Return the indices of the start and end of the substring matched by *group*;
		*group* defaults to zero (meaning the whole matched substring). Return ``-1`` if
		*group* exists but did not contribute to the match.  For a match object *m*, and
		a group *g* that did contribute to the match, the substring matched by group *g*
		(equivalent to ``m.group(g)``) is ::
		
		m.string[m.start(g):m.end(g)]
		
		Note that ``m.start(group)`` will equal ``m.end(group)`` if *group* matched a
		null string.  For example, after ``m = re.search('b(c?)', 'cba')``,
		``m.start(0)`` is 1, ``m.end(0)`` is 2, ``m.start(1)`` and ``m.end(1)`` are both
		2, and ``m.start(2)`` raises an :exc:`IndexError` exception.
		
		An example that will remove *remove_this* from email addresses:
		
		>>> email = "tony@tiremove_thisger.net"
		>>> m = re.search("remove_this", email)
		>>> email[:m.start()] + email[m.end():]
		'tony@tiger.net'
		
		
		"""
		pass
		
	def span(self, group):
		"""
		For :class:`MatchObject` *m*, return the 2-tuple ``(m.start(group),
		m.end(group))``. Note that if *group* did not contribute to the match, this is
		``(-1, -1)``.  *group* defaults to zero, the entire match.
		
		
		"""
		pass
		
	


