#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
""":synopsis: Numeric abstract base classes (Complex, Real, Integral, etc.).

"""
class Number:


	"""
	The root of the numeric hierarchy. If you just want to check if an argument
	*x* is a number, without caring what kind, use ``isinstance(x, Number)``.
	
	
	The numeric tower
	-----------------
	
	"""
	
	
	def __init__(self, ):
		pass
	
	


class Complex:


	"""
	Subclasses of this type describe complex numbers and include the operations
	that work on the built-in :class:`complex` type. These are: conversions to
	:class:`complex` and :class:`bool`, :attr:`.real`, :attr:`.imag`, ``+``,
	``-``, ``*``, ``/``, :func:`abs`, :meth:`conjugate`, ``==``, and ``!=``. All
	except ``-`` and ``!=`` are abstract.
	
	"""
	
	
	def __init__(self, ):
		pass
	
	def conjugate(self, ):
		"""
		Abstract. Returns the complex conjugate. For example, ``(1+3j).conjugate()
		== (1-3j)``.
		
		"""
		pass
		
	


class Real:


	"""
	To :class:`Complex`, :class:`Real` adds the operations that work on real
	numbers.
	
	In short, those are: a conversion to :class:`float`, :func:`math.trunc`,
	:func:`round`, :func:`math.floor`, :func:`math.ceil`, :func:`divmod`, ``//``,
	``%``, ``<``, ``<=``, ``>``, and ``>=``.
	
	Real also provides defaults for :func:`complex`, :attr:`~Complex.real`,
	:attr:`~Complex.imag`, and :meth:`~Complex.conjugate`.
	
	
	"""
	
	
	def __init__(self, ):
		pass
	
	


class Rational:


	"""
	Subtypes :class:`Real` and adds
	:attr:`~Rational.numerator` and :attr:`~Rational.denominator` properties, which
	should be in lowest terms. With these, it provides a default for
	:func:`float`.
	
	"""
	
	
	def __init__(self, ):
		pass
	
	


