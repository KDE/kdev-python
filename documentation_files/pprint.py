#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
""":synopsis: Data pretty printer.
"""
class PrettyPrinter:


	"""
	Construct a :class:`PrettyPrinter` instance.  This constructor understands
	several keyword parameters.  An output stream may be set using the *stream*
	keyword; the only method used on the stream object is the file protocol's
	:meth:`write` method.  If not specified, the :class:`PrettyPrinter` adopts
	``sys.stdout``.  Three additional parameters may be used to control the
	formatted representation.  The keywords are *indent*, *depth*, and *width*.  The
	amount of indentation added for each recursive level is specified by *indent*;
	the default is one.  Other values can cause output to look a little odd, but can
	make nesting easier to spot.  The number of levels which may be printed is
	controlled by *depth*; if the data structure being printed is too deep, the next
	contained level is replaced by ``*more``.  By default, there is no constraint on
	the depth of the objects being formatted.  The desired output width is
	constrained using the *width* parameter; the default is 80 characters.  If a
	structure cannot be formatted within the constrained width, a best effort will
	be made.
	
	>>> import pprint
	>>> stuff = ['spam', 'eggs', 'lumberjack', 'knights', 'ni']
	>>> stuff.insert(0, stuff[:])
	>>> pp = pprint.PrettyPrinter(indent=4)
	>>> pp.pprint(stuff)
	[   ['spam', 'eggs', 'lumberjack', 'knights', 'ni'],
	'spam',
	'eggs',
	'lumberjack',
	'knights',
	'ni']
	>>> tup = ('spam', ('eggs', ('lumberjack', ('knights', ('ni', ('dead',
	*more ('parrot', ('fresh fruit',))))))))
	>>> pp = pprint.PrettyPrinter(depth=6)
	>>> pp.pprint(tup)
	('spam', ('eggs', ('lumberjack', ('knights', ('ni', ('dead', (*more)))))))
	
	The :class:`PrettyPrinter` class supports several derivative functions:
	
	.. erivative functions:
	
	"""
	
	
	def __init__(self, more):
		pass
	
	def pformat(object,indent,width,depth):
		"""
		Return the formatted representation of *object* as a string.  *indent*, *width*
		and *depth* will be passed to the :class:`PrettyPrinter` constructor as
		formatting parameters.
		
		"""
		pass
		
	def pprint(object,stream,indent,width,depth):
		"""
		Prints the formatted representation of *object* on *stream*, followed by a
		newline.  If *stream* is omitted, ``sys.stdout`` is used.  This may be used in
		the interactive interpreter instead of a :keyword:`print` statement for
		inspecting values.    *indent*, *width* and *depth* will be passed to the
		:class:`PrettyPrinter` constructor as formatting parameters.
		
		>>> import pprint
		>>> stuff = ['spam', 'eggs', 'lumberjack', 'knights', 'ni']
		>>> stuff.insert(0, stuff)
		>>> pprint.pprint(stuff)
		[<Recursion on list with id=*more>,
		'spam',
		'eggs',
		'lumberjack',
		'knights',
		'ni']
		
		"""
		pass
		
	def isreadable(object):
		"""
		"""
		pass
		
	def isrecursive(object):
		"""
		Determine if *object* requires a recursive representation.
		
		
		One more support function is also defined:
		
		"""
		pass
		
	def saferepr(object):
		"""
		Return a string representation of *object*, protected against recursive data
		structures.  If the representation of *object* exposes a recursive entry, the
		recursive reference will be represented as ``<Recursion on typename with
		id=number>``.  The representation is not otherwise formatted.
		
		>>> pprint.saferepr(stuff)
		"[<Recursion on list with id=*more>, 'spam', 'eggs', 'lumberjack', 'knights', 'ni']"
		
		
		.. rettyPrinter Objects
		---------------------
		
		:class:`PrettyPrinter` instances have the following methods:
		
		
		"""
		pass
		
	


