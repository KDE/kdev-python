#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
""":synopsis: Mathematical functions for complex numbers.


This module is always available.  It provides access to mathematical functions
for complex numbers.  The functions in this module accept integers,
floating-point numbers or complex numbers as arguments. They will also accept
any Python object that has either a :meth:`__complex__` or a :meth:`__float__`
method: these methods are used to convert the object to a complex or
floating-point number, respectively, and the function is then applied to the
result of the conversion.

"""
"""
The mathematical constant *π*, as a float.


"""
pi = None
"""
The mathematical constant *e*, as a float.

"""
e = None
def phase(x):
	"""
	Return the phase of *x* (also known as the *argument* of *x*), as a
	float.  ``phase(x)`` is equivalent to ``math.atan2(x.imag,
	x.real)``.  The result lies in the range [-π, π], and the branch
	cut for this operation lies along the negative real axis,
	continuous from above.  On systems with support for signed zeros
	(which includes most systems in current use), this means that the
	sign of the result is the same as the sign of ``x.imag``, even when
	``x.imag`` is zero::
	
	>>> phase(complex(-1.0, 0.0))
	3.1415926535897931
	>>> phase(complex(-1.0, -0.0))
	-3.1415926535897931
	
	"""
	pass
	
def polar(x):
	"""
	Return the representation of *x* in polar coordinates.  Returns a
	pair ``(r, phi)`` where *r* is the modulus of *x* and phi is the
	phase of *x*.  ``polar(x)`` is equivalent to ``(abs(x),
	phase(x))``.
	
	"""
	pass
	
def rect(r,phi):
	"""
	Return the complex number *x* with polar coordinates *r* and *phi*.
	Equivalent to ``r * (math.cos(phi) + math.sin(phi)*1j)``.
	
	"""
	pass
	
def exp(x):
	"""
	Return the exponential value ``e**x``.
	
	
	"""
	pass
	
def log(x,base):
	"""
	Returns the logarithm of *x* to the given *base*. If the *base* is not
	specified, returns the natural logarithm of *x*. There is one branch cut, from 0
	along the negative real axis to -∞, continuous from above.
	
	"""
	pass
	
def log10(x):
	"""
	Return the base-10 logarithm of *x*. This has the same branch cut as
	:func:`log`.
	
	
	"""
	pass
	
def sqrt(x):
	"""
	Return the square root of *x*. This has the same branch cut as :func:`log`.
	
	
	Trigonometric functions
	-----------------------
	
	"""
	pass
	
def acos(x):
	"""
	Return the arc cosine of *x*. There are two branch cuts: One extends right from
	1 along the real axis to ∞, continuous from below. The other extends left from
	-1 along the real axis to -∞, continuous from above.
	
	
	"""
	pass
	
def asin(x):
	"""
	Return the arc sine of *x*. This has the same branch cuts as :func:`acos`.
	
	
	"""
	pass
	
def atan(x):
	"""
	Return the arc tangent of *x*. There are two branch cuts: One extends from
	``1j`` along the imaginary axis to ``∞j``, continuous from the right. The
	other extends from ``-1j`` along the imaginary axis to ``-∞j``, continuous
	from the left.
	
	"""
	pass
	
def cos(x):
	"""
	Return the cosine of *x*.
	
	
	"""
	pass
	
def sin(x):
	"""
	Return the sine of *x*.
	
	
	"""
	pass
	
def tan(x):
	"""
	Return the tangent of *x*.
	
	
	Hyperbolic functions
	--------------------
	
	"""
	pass
	
def acosh(x):
	"""
	Return the hyperbolic arc cosine of *x*. There is one branch cut, extending left
	from 1 along the real axis to -∞, continuous from above.
	
	
	"""
	pass
	
def asinh(x):
	"""
	Return the hyperbolic arc sine of *x*. There are two branch cuts:
	One extends from ``1j`` along the imaginary axis to ``∞j``,
	continuous from the right.  The other extends from ``-1j`` along
	the imaginary axis to ``-∞j``, continuous from the left.
	
	"""
	pass
	
def atanh(x):
	"""
	Return the hyperbolic arc tangent of *x*. There are two branch cuts: One
	extends from ``1`` along the real axis to ``∞``, continuous from below. The
	other extends from ``-1`` along the real axis to ``-∞``, continuous from
	above.
	
	"""
	pass
	
def cosh(x):
	"""
	Return the hyperbolic cosine of *x*.
	
	
	"""
	pass
	
def sinh(x):
	"""
	Return the hyperbolic sine of *x*.
	
	
	"""
	pass
	
def tanh(x):
	"""
	Return the hyperbolic tangent of *x*.
	
	
	Classification functions
	------------------------
	
	"""
	pass
	
def isinf(x):
	"""
	Return *True* if the real or the imaginary part of x is positive
	or negative infinity.
	
	"""
	pass
	
def isnan(x):
	"""
	Return *True* if the real or imaginary part of x is not a number (NaN).
	
	"""
	pass
	
