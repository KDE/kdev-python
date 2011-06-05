#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
""":synopsis: Higher order functions and operations on callable objects.
"""
def total_ordering(cls):
	"""
	Given a class defining one or more rich comparison ordering methods, this
	class decorator supplies the rest.  This simplifies the effort involved
	in specifying all of the possible rich comparison operations:
	
	The class must define one of :meth:`__lt__`, :meth:`__le__`,
	:meth:`__gt__`, or :meth:`__ge__`.
	In addition, the class should supply an :meth:`__eq__` method.
	
	For example::
	
	@total_ordering
	class Student:
	def __eq__(self, other):
	return ((self.lastname.lower(), self.firstname.lower()) ==
	(other.lastname.lower(), other.firstname.lower()))
	def __lt__(self, other):
	return ((self.lastname.lower(), self.firstname.lower()) <
	(other.lastname.lower(), other.firstname.lower()))
	
	"""
	pass
	
def reduce(function,iterable,initializer):
	"""
	This is the same function as :func:`reduce`.  It is made available in this module
	to allow writing code more forward-compatible with Python 3.
	
	"""
	pass
	
def partial(func,args,keywords):
	"""
	Return a new :class:`partial` object which when called will behave like *func*
	called with the positional arguments *args* and keyword arguments *keywords*. If
	more arguments are supplied to the call, they are appended to *args*. If
	additional keyword arguments are supplied, they extend and override *keywords*.
	Roughly equivalent to::
	
	def partial(func, *args, **keywords):
	def newfunc(*fargs, **fkeywords):
	newkeywords = keywords.copy()
	newkeywords.update(fkeywords)
	return func(*(args + fargs), **newkeywords)
	newfunc.func = func
	newfunc.args = args
	newfunc.keywords = keywords
	return newfunc
	
	The :func:`partial` is used for partial function application which "freezes"
	some portion of a function's arguments and/or keywords resulting in a new object
	with a simplified signature.  For example, :func:`partial` can be used to create
	a callable that behaves like the :func:`int` function where the *base* argument
	defaults to two:
	
	>>> from functools import partial
	>>> basetwo = partial(int, base=2)
	>>> basetwo.__doc__ = 'Convert base 2 string to an int.'
	>>> basetwo('10010')
	18
	
	
	"""
	pass
	
def update_wrapper(wrapper,wrapped,assigned,updated):
	"""
	Update a *wrapper* function to look like the *wrapped* function. The optional
	arguments are tuples to specify which attributes of the original function are
	assigned directly to the matching attributes on the wrapper function and which
	attributes of the wrapper function are updated with the corresponding attributes
	from the original function. The default values for these arguments are the
	module level constants *WRAPPER_ASSIGNMENTS* (which assigns to the wrapper
	function's *__name__*, *__module__* and *__doc__*, the documentation string) and
	*WRAPPER_UPDATES* (which updates the wrapper function's *__dict__*, i.e. the
	instance dictionary).
	
	The main intended use for this function is in :term:`decorator` functions which
	wrap the decorated function and return the wrapper. If the wrapper function is
	not updated, the metadata of the returned function will reflect the wrapper
	definition rather than the original function definition, which is typically less
	than helpful.
	
	
	"""
	pass
	
def wraps(wrapped,assigned,updated):
	"""
	This is a convenience function for invoking ``partial(update_wrapper,
	wrapped=wrapped, assigned=assigned, updated=updated)`` as a function decorator
	when defining a wrapper function. For example:
	
	>>> from functools import wraps
	>>> def my_decorator(f):
	more     @wraps(f)
	more     def wrapper(*args, **kwds):
	more         print 'Calling decorated function'
	more         return f(*args, **kwds)
	more     return wrapper
	more
	>>> @my_decorator
	more def example():
	more      " " " Docstring " " " 
	more     print 'Called example function'
	more
	>>> example()
	Calling decorated function
	Called example function
	>>> example.__name__
	'example'
	>>> example.__doc__
	'Docstring'
	
	Without the use of this decorator factory, the name of the example function
	would have been ``'wrapper'``, and the docstring of the original :func:`example`
	would have been lost.
	
	
	.. class:`partial` Objects
	------------------------
	
	:class:`partial` objects are callable objects created by :func:`partial`. They
	have three read-only attributes:
	
	
	"""
	pass
	
