#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
""":synopsis: Implementation of the General Decimal Arithmetic  Specification.


"""
class Decimal:


	"""
	Construct a new :class:`Decimal` object based from *value*.
	
	*value* can be an integer, string, tuple, :class:`float`, or another :class:`Decimal`
	object. If no *value* is given, returns ``Decimal('0')``.  If *value* is a
	string, it should conform to the decimal numeric string syntax after leading
	and trailing whitespace characters are removed::
	
	sign           ::=  '+' | '-'
	digit          ::=  '0' | '1' | '2' | '3' | '4' | '5' | '6' | '7' | '8' | '9'
	indicator      ::=  'e' | 'E'
	digits         ::=  digit [digit]*more
	decimal-part   ::=  digits '.' [digits] | ['.'] digits
	exponent-part  ::=  indicator [sign] digits
	infinity       ::=  'Infinity' | 'Inf'
	nan            ::=  'NaN' [digits] | 'sNaN' [digits]
	numeric-value  ::=  decimal-part [exponent-part] | infinity
	numeric-string ::=  [sign] numeric-value | [sign] nan
	
	If *value* is a unicode string then other Unicode decimal digits
	are also permitted where ``digit`` appears above.  These include
	decimal digits from various other alphabets (for example,
	Arabic-Indic and Devanāgarī digits) along with the fullwidth digits
	``u'\uff10'`` through ``u'\uff19'``.
	
	If *value* is a :class:`tuple`, it should have three components, a sign
	(:const:`0` for positive or :const:`1` for negative), a :class:`tuple` of
	digits, and an integer exponent. For example, ``Decimal((0, (1, 4, 1, 4), -3))``
	returns ``Decimal('1.414')``.
	
	If *value* is a :class:`float`, the binary floating point value is losslessly
	converted to its exact decimal equivalent.  This conversion can often require
	53 or more digits of precision.  For example, ``Decimal(float('1.1'))``
	converts to
	``Decimal('1.100000000000000088817841970012523233890533447265625')``.
	
	The *context* precision does not affect how many digits are stored. That is
	determined exclusively by the number of digits in *value*. For example,
	``Decimal('3.00000')`` records all five zeros even if the context precision is
	only three.
	
	The purpose of the *context* argument is determining what to do if *value* is a
	malformed string.  If the context traps :const:`InvalidOperation`, an exception
	is raised; otherwise, the constructor returns a new Decimal with the value of
	:const:`NaN`.
	
	Once constructed, :class:`Decimal` objects are immutable.
	
	"""
	
	
	def __init__(self, value,context):
		pass
	
	def getcontext():
		"""
		Return the current context for the active thread.
		
		
		"""
		pass
		
	def setcontext(c):
		"""
		Set the current context for the active thread to *c*.
		
		Beginning with Python 2.5, you can also use the :keyword:`with` statement and
		the :func:`localcontext` function to temporarily change the active context.
		
		
		"""
		pass
		
	def localcontext(c):
		"""
		Return a context manager that will set the current context for the active thread
		to a copy of *c* on entry to the with-statement and restore the previous context
		when exiting the with-statement. If no context is specified, a copy of the
		current context is used.
		
		"""
		pass
		
	


class BasicContext:


	"""
	This is a standard context defined by the General Decimal Arithmetic
	Specification.  Precision is set to nine.  Rounding is set to
	:const:`ROUND_HALF_UP`.  All flags are cleared.  All traps are enabled (treated
	as exceptions) except :const:`Inexact`, :const:`Rounded`, and
	:const:`Subnormal`.
	
	Because many of the traps are enabled, this context is useful for debugging.
	
	
	"""
	
	
	def __init__(self, ):
		pass
	
	


class ExtendedContext:


	"""
	This is a standard context defined by the General Decimal Arithmetic
	Specification.  Precision is set to nine.  Rounding is set to
	:const:`ROUND_HALF_EVEN`.  All flags are cleared.  No traps are enabled (so that
	exceptions are not raised during computations).
	
	Because the traps are disabled, this context is useful for applications that
	prefer to have result value of :const:`NaN` or :const:`Infinity` instead of
	raising exceptions.  This allows an application to complete a run in the
	presence of conditions that would otherwise halt the program.
	
	
	"""
	
	
	def __init__(self, ):
		pass
	
	


class DefaultContext:


	"""
	This context is used by the :class:`Context` constructor as a prototype for new
	contexts.  Changing a field (such a precision) has the effect of changing the
	default for new contexts created by the :class:`Context` constructor.
	
	This context is most useful in multi-threaded environments.  Changing one of the
	fields before threads are started has the effect of setting system-wide
	defaults.  Changing the fields after threads have started is not recommended as
	it would require thread synchronization to prevent race conditions.
	
	In single threaded environments, it is preferable to not use this context at
	all.  Instead, simply create contexts explicitly as described below.
	
	The default values are precision=28, rounding=ROUND_HALF_EVEN, and enabled traps
	for Overflow, InvalidOperation, and DivisionByZero.
	
	In addition to the three supplied contexts, new contexts can be created with the
	:class:`Context` constructor.
	
	
	"""
	
	
	def __init__(self, ):
		pass
	
	


class Context:


	"""
	Creates a new context.  If a field is not specified or is :const:`None`, the
	default values are copied from the :const:`DefaultContext`.  If the *flags*
	field is not specified or is :const:`None`, all flags are cleared.
	
	The *prec* field is a positive integer that sets the precision for arithmetic
	operations in the context.
	
	The *rounding* option is one of:
	
	* :const:`ROUND_CEILING` (towards :const:`Infinity`),
	* :const:`ROUND_DOWN` (towards zero),
	* :const:`ROUND_FLOOR` (towards :const:`-Infinity`),
	* :const:`ROUND_HALF_DOWN` (to nearest with ties going towards zero),
	* :const:`ROUND_HALF_EVEN` (to nearest with ties going to nearest even integer),
	* :const:`ROUND_HALF_UP` (to nearest with ties going away from zero), or
	* :const:`ROUND_UP` (away from zero).
	* :const:`ROUND_05UP` (away from zero if last digit after rounding towards zero
	would have been 0 or 5; otherwise towards zero)
	
	The *traps* and *flags* fields list any signals to be set. Generally, new
	contexts should only set traps and leave the flags clear.
	
	The *Emin* and *Emax* fields are integers specifying the outer limits allowable
	for exponents.
	
	The *capitals* field is either :const:`0` or :const:`1` (the default). If set to
	:const:`1`, exponents are printed with a capital :const:`E`; otherwise, a
	lowercase :const:`e` is used: :const:`Decimal('6.02e+23')`.
	
	"""
	
	
	def __init__(self, prec=None,rounding=None,traps=None,flags=None,Emin=None,Emax=None,capitals=1):
		pass
	
	


class Clamped:


	"""
	Altered an exponent to fit representation constraints.
	
	Typically, clamping occurs when an exponent falls outside the context's
	:attr:`Emin` and :attr:`Emax` limits.  If possible, the exponent is reduced to
	fit by adding zeros to the coefficient.
	
	
	"""
	
	
	def __init__(self, ):
		pass
	
	


class DecimalException:


	"""
	Base class for other signals and a subclass of :exc:`ArithmeticError`.
	
	
	"""
	
	
	def __init__(self, ):
		pass
	
	


class DivisionByZero:


	"""
	Signals the division of a non-infinite number by zero.
	
	Can occur with division, modulo division, or when raising a number to a negative
	power.  If this signal is not trapped, returns :const:`Infinity` or
	:const:`-Infinity` with the sign determined by the inputs to the calculation.
	
	
	"""
	
	
	def __init__(self, ):
		pass
	
	


class Inexact:


	"""
	Indicates that rounding occurred and the result is not exact.
	
	Signals when non-zero digits were discarded during rounding. The rounded result
	is returned.  The signal flag or trap is used to detect when results are
	inexact.
	
	
	"""
	
	
	def __init__(self, ):
		pass
	
	


class InvalidOperation:


	"""
	An invalid operation was performed.
	
	Indicates that an operation was requested that does not make sense. If not
	trapped, returns :const:`NaN`.  Possible causes include::
	
	Infinity - Infinity
	0 * Infinity
	Infinity / Infinity
	x % 0
	Infinity % x
	x._rescale( non-integer )
	sqrt(-x) and x > 0
	0 ** 0
	x ** (non-integer)
	x ** Infinity
	
	
	"""
	
	
	def __init__(self, ):
		pass
	
	


class Overflow:


	"""
	Numerical overflow.
	
	Indicates the exponent is larger than :attr:`Emax` after rounding has
	occurred.  If not trapped, the result depends on the rounding mode, either
	pulling inward to the largest representable finite number or rounding outward
	to :const:`Infinity`.  In either case, :class:`Inexact` and :class:`Rounded`
	are also signaled.
	
	
	"""
	
	
	def __init__(self, ):
		pass
	
	


class Rounded:


	"""
	Rounding occurred though possibly no information was lost.
	
	Signaled whenever rounding discards digits; even if those digits are zero
	(such as rounding :const:`5.00` to :const:`5.0`).  If not trapped, returns
	the result unchanged.  This signal is used to detect loss of significant
	digits.
	
	
	"""
	
	
	def __init__(self, ):
		pass
	
	


class Subnormal:


	"""
	Exponent was lower than :attr:`Emin` prior to rounding.
	
	Occurs when an operation result is subnormal (the exponent is too small). If
	not trapped, returns the result unchanged.
	
	
	"""
	
	
	def __init__(self, ):
		pass
	
	


class Underflow:


	"""
	Numerical underflow with result rounded to zero.
	
	Occurs when a subnormal result is pushed to zero by rounding. :class:`Inexact`
	and :class:`Subnormal` are also signaled.
	
	The following table summarizes the hierarchy of signals::
	
	exceptions.ArithmeticError(exceptions.StandardError)
	DecimalException
	Clamped
	DivisionByZero(DecimalException, exceptions.ZeroDivisionError)
	Inexact
	Overflow(Inexact, Rounded)
	Underflow(Inexact, Rounded, Subnormal)
	InvalidOperation
	Rounded
	Subnormal
	
	.. .. loating Point Notes
	--------------------
	
	
	Mitigating round-off error with increased precision
	^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
	
	The use of decimal floating point eliminates decimal representation error
	(making it possible to represent :const:`0.1` exactly); however, some operations
	can still incur round-off error when non-zero digits exceed the fixed precision.
	
	The effects of round-off error can be amplified by the addition or subtraction
	of nearly offsetting quantities resulting in loss of significance.  Knuth
	provides two instructive examples where rounded floating point arithmetic with
	insufficient precision causes the breakdown of the associative and distributive
	properties of addition:
	
	"""
	
	
	def __init__(self, ):
		pass
	
	


