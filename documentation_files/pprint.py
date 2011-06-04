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
	
	
	def __init__(self, ):
		pass
	
	def pformat(self, object,indent,width,depth):
		"""
		Return the formatted representation of *object* as a string.  *indent*, *width*
		and *depth* will be passed to the :class:`PrettyPrinter` constructor as
		formatting parameters.
		
		"""
		pass
		
	def pprint(self, object,stream,indent,width,depth):
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
		
	def isreadable(self, object):
		"""
		"""
		pass
		
	def isrecursive(self, object):
		"""
		Determine if *object* requires a recursive representation.
		
		
		One more support function is also defined:
		
		"""
		pass
		
	def saferepr(self, object):
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
		
	def pformat(self, object):
		"""
		Return the formatted representation of *object*.  This takes into account the
		options passed to the :class:`PrettyPrinter` constructor.
		
		
		"""
		pass
		
	def pprint(self, object):
		"""
		Print the formatted representation of *object* on the configured stream,
		followed by a newline.
		
		The following methods provide the implementations for the corresponding
		functions of the same names.  Using these methods on an instance is slightly
		more efficient since new :class:`PrettyPrinter` objects don't need to be
		created.
		
		
		"""
		pass
		
	def isreadable(self, object):
		"""
		"""
		pass
		
	def isrecursive(self, object):
		"""
		Determine if the object requires a recursive representation.
		
		This method is provided as a hook to allow subclasses to modify the way objects
		are converted to strings.  The default implementation uses the internals of the
		:func:`saferepr` implementation.
		
		
		"""
		pass
		
	def format(self, object,context,maxlevels,level):
		"""
		Returns three values: the formatted version of *object* as a string, a flag
		indicating whether the result is readable, and a flag indicating whether
		recursion was detected.  The first argument is the object to be presented.  The
		second is a dictionary which contains the :func:`id` of objects that are part of
		the current presentation context (direct and indirect containers for *object*
		that are affecting the presentation) as the keys; if an object needs to be
		presented which is already represented in *context*, the third return value
		should be ``True``.  Recursive calls to the :meth:`format` method should add
		additional entries for containers to this dictionary.  The third argument,
		*maxlevels*, gives the requested limit to recursion; this will be ``0`` if there
		is no requested limit.  This argument should be passed unmodified to recursive
		calls. The fourth argument, *level*, gives the current level; recursive calls
		should be passed a value less than that of the current call.
		
		"""
		pass
		
	


