#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
""":synopsis: Helpers for computing differences between objects.
"""
class SequenceMatcher:


	"""
	This is a flexible class for comparing pairs of sequences of any type, so long
	as the sequence elements are :term:`hashable`.  The basic algorithm predates, and is a
	little fancier than, an algorithm published in the late 1980's by Ratcliff and
	Obershelp under the hyperbolic name "gestalt pattern matching."  The idea is to
	find the longest contiguous matching subsequence that contains no "junk"
	elements (the Ratcliff and Obershelp algorithm doesn't address junk).  The same
	idea is then applied recursively to the pieces of the sequences to the left and
	to the right of the matching subsequence.  This does not yield minimal edit
	sequences, but does tend to yield matches that "look right" to people.
	
	**Timing:** The basic Ratcliff-Obershelp algorithm is cubic time in the worst
	case and quadratic time in the expected case. :class:`SequenceMatcher` is
	quadratic time for the worst case and has expected-case behavior dependent in a
	complicated way on how many elements the sequences have in common; best case
	time is linear.
	
	**Automatic junk heuristic:** :class:`SequenceMatcher` supports a heuristic that
	automatically treats certain sequence items as junk. The heuristic counts how many
	times each individual item appears in the sequence. If an item's duplicates (after
	the first one) account for more than 1% of the sequence and the sequence is at least
	200 items long, this item is marked as "popular" and is treated as junk for
	the purpose of sequence matching. This heuristic can be turned off by setting
	the ``autojunk`` argument to ``False`` when creating the :class:`SequenceMatcher`.
	
	"""
	
	
	def __init__(self, ):
		pass
	
	


class Differ:


	"""
	This is a class for comparing sequences of lines of text, and producing
	human-readable differences or deltas.  Differ uses :class:`SequenceMatcher`
	both to compare sequences of lines, and to compare sequences of characters
	within similar (near-matching) lines.
	
	Each line of a :class:`Differ` delta begins with a two-letter code:
	
	+----------+-------------------------------------------+
	| Code     | Meaning                                   |
	+==========+===========================================+
	| ``'- '`` | line unique to sequence 1                 |
	+----------+-------------------------------------------+
	| ``'+ '`` | line unique to sequence 2                 |
	+----------+-------------------------------------------+
	| ``'  '`` | line common to both sequences             |
	+----------+-------------------------------------------+
	| ``'? '`` | line not present in either input sequence |
	+----------+-------------------------------------------+
	
	Lines beginning with '``?``' attempt to guide the eye to intraline differences,
	and were not present in either input sequence. These lines can be confusing if
	the sequences contain tab characters.
	
	
	"""
	
	
	def __init__(self, ):
		pass
	
	


class HtmlDiff:


	"""
	This class can be used to create an HTML table (or a complete HTML file
	containing the table) showing a side by side, line by line comparison of text
	with inter-line and intra-line change highlights.  The table can be generated in
	either full or contextual difference mode.
	
	The constructor for this class is:
	
	
	"""
	
	
	def __init__(self, ):
		pass
	
	def __init__(tabsize,wrapcolumn,linejunk,charjunk):
		"""
		Initializes instance of :class:`HtmlDiff`.
		
		*tabsize* is an optional keyword argument to specify tab stop spacing and
		defaults to ``8``.
		
		*wrapcolumn* is an optional keyword to specify column number where lines are
		broken and wrapped, defaults to ``None`` where lines are not wrapped.
		
		*linejunk* and *charjunk* are optional keyword arguments passed into ``ndiff()``
		(used by :class:`HtmlDiff` to generate the side by side HTML differences).  See
		``ndiff()`` documentation for argument default values and descriptions.
		
		The following methods are public:
		
		
		"""
		pass
		
	def make_file(_fromlines,tolines,_fromdesc,todesc,context,numlines):
		"""
		Compares *fromlines* and *tolines* (lists of strings) and returns a string which
		is a complete HTML file containing a table showing line by line differences with
		inter-line and intra-line changes highlighted.
		
		*fromdesc* and *todesc* are optional keyword arguments to specify from/to file
		column header strings (both default to an empty string).
		
		*context* and *numlines* are both optional keyword arguments. Set *context* to
		``True`` when contextual differences are to be shown, else the default is
		``False`` to show the full files. *numlines* defaults to ``5``.  When *context*
		is ``True`` *numlines* controls the number of context lines which surround the
		difference highlights.  When *context* is ``False`` *numlines* controls the
		number of lines which are shown before a difference highlight when using the
		"next" hyperlinks (setting to zero would cause the "next" hyperlinks to place
		the next difference highlight at the top of the browser without any leading
		context).
		
		
		"""
		pass
		
	def make_table(_fromlines,tolines,_fromdesc,todesc,context,numlines):
		"""
		Compares *fromlines* and *tolines* (lists of strings) and returns a string which
		is a complete HTML table showing line by line differences with inter-line and
		intra-line changes highlighted.
		
		The arguments for this method are the same as those for the :meth:`make_file`
		method.
		
		:file:`Tools/scripts/diff.py` is a command-line front-end to this class and
		contains a good example of its use.
		
		"""
		pass
		
	def context_diff(a,b,_fromfile,tofile,_fromfiledate,tofiledate,n,lineterm):
		"""
		Compare *a* and *b* (lists of strings); return a delta (a :term:`generator`
		generating the delta lines) in context diff format.
		
		Context diffs are a compact way of showing just the lines that have changed plus
		a few lines of context.  The changes are shown in a before/after style.  The
		number of context lines is set by *n* which defaults to three.
		
		By default, the diff control lines (those with ``***`` or ``---``) are created
		with a trailing newline.  This is helpful so that inputs created from
		:func:`file.readlines` result in diffs that are suitable for use with
		:func:`file.writelines` since both the inputs and outputs have trailing
		newlines.
		
		For inputs that do not have trailing newlines, set the *lineterm* argument to
		``""`` so that the output will be uniformly newline free.
		
		The context diff format normally has a header for filenames and modification
		times.  Any or all of these may be specified using strings for *fromfile*,
		*tofile*, *fromfiledate*, and *tofiledate*.  The modification times are normally
		expressed in the ISO 8601 format. If not specified, the
		strings default to blanks.
		
		>>> s1 = ['bacon\n', 'eggs\n', 'ham\n', 'guido\n']
		>>> s2 = ['python\n', 'eggy\n', 'hamster\n', 'guido\n']
		>>> for line in context_diff(s1, s2, fromfile='before.py', tofile='after.py'):
		*more     sys.stdout.write(line)  # doctest: +NORMALIZE_WHITESPACE
		*** before.py
		--- after.py
		***************
		*** 1,4 ****
		! bacon
		! eggs
		! ham
		guido
		--- 1,4 ----
		! python
		! eggy
		! hamster
		guido
		
		See :ref:`difflib-interface` for a more detailed example.
		
		"""
		pass
		
	def get_close_matches(word,possibilities,n,cutoff):
		"""
		Return a list of the best "good enough" matches.  *word* is a sequence for which
		close matches are desired (typically a string), and *possibilities* is a list of
		sequences against which to match *word* (typically a list of strings).
		
		Optional argument *n* (default ``3``) is the maximum number of close matches to
		return; *n* must be greater than ``0``.
		
		Optional argument *cutoff* (default ``0.6``) is a float in the range [0, 1].
		Possibilities that don't score at least that similar to *word* are ignored.
		
		The best (no more than *n*) matches among the possibilities are returned in a
		list, sorted by similarity score, most similar first.
		
		>>> get_close_matches('appel', ['ape', 'apple', 'peach', 'puppy'])
		['apple', 'ape']
		>>> import keyword
		>>> get_close_matches('wheel', keyword.kwlist)
		['while']
		>>> get_close_matches('apple', keyword.kwlist)
		[]
		>>> get_close_matches('accept', keyword.kwlist)
		['except']
		
		
		"""
		pass
		
	def ndiff(a,b,linejunk,charjunk):
		"""
		Compare *a* and *b* (lists of strings); return a :class:`Differ`\ -style
		delta (a :term:`generator` generating the delta lines).
		
		Optional keyword parameters *linejunk* and *charjunk* are for filter functions
		(or ``None``):
		
		*linejunk*: A function that accepts a single string argument, and returns true
		if the string is junk, or false if not. The default is (``None``), starting with
		Python 2.3.  Before then, the default was the module-level function
		:func:`IS_LINE_JUNK`, which filters out lines without visible characters, except
		for at most one pound character (``'#'``). As of Python 2.3, the underlying
		:class:`SequenceMatcher` class does a dynamic analysis of which lines are so
		frequent as to constitute noise, and this usually works better than the pre-2.3
		default.
		
		*charjunk*: A function that accepts a character (a string of length 1), and
		returns if the character is junk, or false if not. The default is module-level
		function :func:`IS_CHARACTER_JUNK`, which filters out whitespace characters (a
		blank or tab; note: bad idea to include newline in this!).
		
		:file:`Tools/scripts/ndiff.py` is a command-line front-end to this function.
		
		>>> diff = ndiff('one\ntwo\nthree\n'.splitlines(1),
		*more              'ore\ntree\nemu\n'.splitlines(1))
		>>> print ''.join(diff),
		- one
		?  ^
		+ ore
		?  ^
		- two
		- three
		?  -
		+ tree
		+ emu
		
		
		"""
		pass
		
	def restore(sequence,which):
		"""
		Return one of the two sequences that generated a delta.
		
		Given a *sequence* produced by :meth:`Differ.compare` or :func:`ndiff`, extract
		lines originating from file 1 or 2 (parameter *which*), stripping off line
		prefixes.
		
		Example:
		
		>>> diff = ndiff('one\ntwo\nthree\n'.splitlines(1),
		*more              'ore\ntree\nemu\n'.splitlines(1))
		>>> diff = list(diff) # materialize the generated delta into a list
		>>> print ''.join(restore(diff, 1)),
		one
		two
		three
		>>> print ''.join(restore(diff, 2)),
		ore
		tree
		emu
		
		
		"""
		pass
		
	def unified_diff(a,b,_fromfile,tofile,_fromfiledate,tofiledate,n,lineterm):
		"""
		Compare *a* and *b* (lists of strings); return a delta (a :term:`generator`
		generating the delta lines) in unified diff format.
		
		Unified diffs are a compact way of showing just the lines that have changed plus
		a few lines of context.  The changes are shown in a inline style (instead of
		separate before/after blocks).  The number of context lines is set by *n* which
		defaults to three.
		
		By default, the diff control lines (those with ``---``, ``+++``, or ``@@``) are
		created with a trailing newline.  This is helpful so that inputs created from
		:func:`file.readlines` result in diffs that are suitable for use with
		:func:`file.writelines` since both the inputs and outputs have trailing
		newlines.
		
		For inputs that do not have trailing newlines, set the *lineterm* argument to
		``""`` so that the output will be uniformly newline free.
		
		The context diff format normally has a header for filenames and modification
		times.  Any or all of these may be specified using strings for *fromfile*,
		*tofile*, *fromfiledate*, and *tofiledate*.  The modification times are normally
		expressed in the ISO 8601 format. If not specified, the
		strings default to blanks.
		
		>>> s1 = ['bacon\n', 'eggs\n', 'ham\n', 'guido\n']
		>>> s2 = ['python\n', 'eggy\n', 'hamster\n', 'guido\n']
		>>> for line in unified_diff(s1, s2, fromfile='before.py', tofile='after.py'):
		*more     sys.stdout.write(line)   # doctest: +NORMALIZE_WHITESPACE
		--- before.py
		+++ after.py
		@@ -1,4 +1,4 @@
		-bacon
		-eggs
		-ham
		+python
		+eggy
		+hamster
		guido
		
		See :ref:`difflib-interface` for a more detailed example.
		
		"""
		pass
		
	def IS_LINE_JUNK(line):
		"""
		Return true for ignorable lines.  The line *line* is ignorable if *line* is
		blank or contains a single ``'#'``, otherwise it is not ignorable.  Used as a
		default for parameter *linejunk* in :func:`ndiff` before Python 2.3.
		
		
		"""
		pass
		
	def IS_CHARACTER_JUNK(ch):
		"""
		Return true for ignorable characters.  The character *ch* is ignorable if *ch*
		is a space or tab, otherwise it is not ignorable.  Used as a default for
		parameter *charjunk* in :func:`ndiff`.
		
		
		"""
		pass
		
	


class SequenceMatcher:


	"""
	Optional argument *isjunk* must be ``None`` (the default) or a one-argument
	function that takes a sequence element and returns true if and only if the
	element is "junk" and should be ignored. Passing ``None`` for *isjunk* is
	equivalent to passing ``lambda x: 0``; in other words, no elements are ignored.
	For example, pass::
	
	lambda x: x in " \t"
	
	if you're comparing lines as sequences of characters, and don't want to synch up
	on blanks or hard tabs.
	
	The optional arguments *a* and *b* are sequences to be compared; both default to
	empty strings.  The elements of both sequences must be :term:`hashable`.
	
	The optional argument *autojunk* can be used to disable the automatic junk
	heuristic.
	
	"""
	
	
	def __init__(self, isjunk,a,b,autojunk=True):
		pass
	
	


class Differ:


	"""
	Optional keyword parameters *linejunk* and *charjunk* are for filter functions
	(or ``None``):
	
	*linejunk*: A function that accepts a single string argument, and returns true
	if the string is junk.  The default is ``None``, meaning that no line is
	considered junk.
	
	*charjunk*: A function that accepts a single character argument (a string of
	length 1), and returns true if the character is junk. The default is ``None``,
	meaning that no character is considered junk.
	
	:class:`Differ` objects are used (deltas generated) via a single method:
	
	
	"""
	
	
	def __init__(self, linejunk,charjunk):
		pass
	
	


