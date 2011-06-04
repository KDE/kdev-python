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
	
	
	def __init__(self, ):
		pass
	
	def adjusted(self, ):
		"""
		Return the adjusted exponent after shifting out the coefficient's
		rightmost digits until only the lead digit remains:
		``Decimal('321e+5').adjusted()`` returns seven.  Used for determining the
		position of the most significant digit with respect to the decimal point.
		
		
		"""
		pass
		
	def as_tuple(self, ):
		"""
		Return a :term:`named tuple` representation of the number:
		``DecimalTuple(sign, digits, exponent)``.
		
		"""
		pass
		
	def canonical(self, ):
		"""
		Return the canonical encoding of the argument.  Currently, the encoding of
		a :class:`Decimal` instance is always canonical, so this operation returns
		its argument unchanged.
		
		"""
		pass
		
	def compare(self, other,context):
		"""
		Compare the values of two Decimal instances.  This operation behaves in
		the same way as the usual comparison method :meth:`__cmp__`, except that
		:meth:`compare` returns a Decimal instance rather than an integer, and if
		either operand is a NaN then the result is a NaN::
		
		a or b is a NaN ==> Decimal('NaN')
		a < b           ==> Decimal('-1')
		a == b          ==> Decimal('0')
		a > b           ==> Decimal('1')
		
		"""
		pass
		
	def compare_signal(self, other,context):
		"""
		This operation is identical to the :meth:`compare` method, except that all
		NaNs signal.  That is, if neither operand is a signaling NaN then any
		quiet NaN operand is treated as though it were a signaling NaN.
		
		"""
		pass
		
	def compare_total(self, other):
		"""
		Compare two operands using their abstract representation rather than their
		numerical value.  Similar to the :meth:`compare` method, but the result
		gives a total ordering on :class:`Decimal` instances.  Two
		:class:`Decimal` instances with the same numeric value but different
		representations compare unequal in this ordering:
		
		>>> Decimal('12.0').compare_total(Decimal('12'))
		Decimal('-1')
		
		Quiet and signaling NaNs are also included in the total ordering.  The
		result of this function is ``Decimal('0')`` if both operands have the same
		representation, ``Decimal('-1')`` if the first operand is lower in the
		total order than the second, and ``Decimal('1')`` if the first operand is
		higher in the total order than the second operand.  See the specification
		for details of the total order.
		
		"""
		pass
		
	def compare_total_mag(self, other):
		"""
		Compare two operands using their abstract representation rather than their
		value as in :meth:`compare_total`, but ignoring the sign of each operand.
		``x.compare_total_mag(y)`` is equivalent to
		``x.copy_abs().compare_total(y.copy_abs())``.
		
		"""
		pass
		
	def conjugate(self, ):
		"""
		Just returns self, this method is only to comply with the Decimal
		Specification.
		
		"""
		pass
		
	def copy_abs(self, ):
		"""
		Return the absolute value of the argument.  This operation is unaffected
		by the context and is quiet: no flags are changed and no rounding is
		performed.
		
		"""
		pass
		
	def copy_negate(self, ):
		"""
		Return the negation of the argument.  This operation is unaffected by the
		context and is quiet: no flags are changed and no rounding is performed.
		
		"""
		pass
		
	def copy_sign(self, other):
		"""
		Return a copy of the first operand with the sign set to be the same as the
		sign of the second operand.  For example:
		
		>>> Decimal('2.3').copy_sign(Decimal('-1.5'))
		Decimal('-2.3')
		
		This operation is unaffected by the context and is quiet: no flags are
		changed and no rounding is performed.
		
		"""
		pass
		
	def exp(self, context):
		"""
		Return the value of the (natural) exponential function ``e**x`` at the
		given number.  The result is correctly rounded using the
		:const:`ROUND_HALF_EVEN` rounding mode.
		
		>>> Decimal(1).exp()
		Decimal('2.718281828459045235360287471')
		>>> Decimal(321).exp()
		Decimal('2.561702493119680037517373933E+139')
		
		"""
		pass
		
	def _from_float(self, f):
		"""
		Classmethod that converts a float to a decimal number, exactly.
		
		Note `Decimal.from_float(0.1)` is not the same as `Decimal('0.1')`.
		Since 0.1 is not exactly representable in binary floating point, the
		value is stored as the nearest representable value which is
		`0x1.999999999999ap-4`.  That equivalent value in decimal is
		`0.1000000000000000055511151231257827021181583404541015625`.
		
		"""
		pass
		
	def fma(self, other,third,context):
		"""
		Fused multiply-add.  Return self*other+third with no rounding of the
		intermediate product self*other.
		
		>>> Decimal(2).fma(3, 5)
		Decimal('11')
		
		"""
		pass
		
	def is_canonical(self, ):
		"""
		Return :const:`True` if the argument is canonical and :const:`False`
		otherwise.  Currently, a :class:`Decimal` instance is always canonical, so
		this operation always returns :const:`True`.
		
		"""
		pass
		
	def is_finite(self, ):
		"""
		Return :const:`True` if the argument is a finite number, and
		:const:`False` if the argument is an infinity or a NaN.
		
		"""
		pass
		
	def is_infinite(self, ):
		"""
		Return :const:`True` if the argument is either positive or negative
		infinity and :const:`False` otherwise.
		
		"""
		pass
		
	def is_nan(self, ):
		"""
		Return :const:`True` if the argument is a (quiet or signaling) NaN and
		:const:`False` otherwise.
		
		"""
		pass
		
	def is_normal(self, ):
		"""
		Return :const:`True` if the argument is a *normal* finite non-zero
		number with an adjusted exponent greater than or equal to *Emin*.
		Return :const:`False` if the argument is zero, subnormal, infinite or a
		NaN.  Note, the term *normal* is used here in a different sense with
		the :meth:`normalize` method which is used to create canonical values.
		
		"""
		pass
		
	def is_qnan(self, ):
		"""
		Return :const:`True` if the argument is a quiet NaN, and
		:const:`False` otherwise.
		
		"""
		pass
		
	def is_signed(self, ):
		"""
		Return :const:`True` if the argument has a negative sign and
		:const:`False` otherwise.  Note that zeros and NaNs can both carry signs.
		
		"""
		pass
		
	def is_snan(self, ):
		"""
		Return :const:`True` if the argument is a signaling NaN and :const:`False`
		otherwise.
		
		"""
		pass
		
	def is_subnormal(self, ):
		"""
		Return :const:`True` if the argument is subnormal, and :const:`False`
		otherwise. A number is subnormal is if it is nonzero, finite, and has an
		adjusted exponent less than *Emin*.
		
		"""
		pass
		
	def is_zero(self, ):
		"""
		Return :const:`True` if the argument is a (positive or negative) zero and
		:const:`False` otherwise.
		
		"""
		pass
		
	def ln(self, context):
		"""
		Return the natural (base e) logarithm of the operand.  The result is
		correctly rounded using the :const:`ROUND_HALF_EVEN` rounding mode.
		
		"""
		pass
		
	def log10(self, context):
		"""
		Return the base ten logarithm of the operand.  The result is correctly
		rounded using the :const:`ROUND_HALF_EVEN` rounding mode.
		
		"""
		pass
		
	def logb(self, context):
		"""
		For a nonzero number, return the adjusted exponent of its operand as a
		:class:`Decimal` instance.  If the operand is a zero then
		``Decimal('-Infinity')`` is returned and the :const:`DivisionByZero` flag
		is raised.  If the operand is an infinity then ``Decimal('Infinity')`` is
		returned.
		
		"""
		pass
		
	def logical_and(self, other,context):
		"""
		:meth:`logical_and` is a logical operation which takes two *logical
		operands* (see :ref:`logical_operands_label`).  The result is the
		digit-wise ``and`` of the two operands.
		
		"""
		pass
		
	def logical_invert(self, context):
		"""
		:meth:`logical_invert` is a logical operation.  The
		result is the digit-wise inversion of the operand.
		
		"""
		pass
		
	def logical_or(self, other,context):
		"""
		:meth:`logical_or` is a logical operation which takes two *logical
		operands* (see :ref:`logical_operands_label`).  The result is the
		digit-wise ``or`` of the two operands.
		
		"""
		pass
		
	def logical_xor(self, other,context):
		"""
		:meth:`logical_xor` is a logical operation which takes two *logical
		operands* (see :ref:`logical_operands_label`).  The result is the
		digit-wise exclusive or of the two operands.
		
		"""
		pass
		
	def max(self, other,context):
		"""
		Like ``max(self, other)`` except that the context rounding rule is applied
		before returning and that :const:`NaN` values are either signaled or
		ignored (depending on the context and whether they are signaling or
		quiet).
		
		"""
		pass
		
	def max_mag(self, other,context):
		"""
		Similar to the :meth:`.max` method, but the comparison is done using the
		absolute values of the operands.
		
		"""
		pass
		
	def min(self, other,context):
		"""
		Like ``min(self, other)`` except that the context rounding rule is applied
		before returning and that :const:`NaN` values are either signaled or
		ignored (depending on the context and whether they are signaling or
		quiet).
		
		"""
		pass
		
	def min_mag(self, other,context):
		"""
		Similar to the :meth:`.min` method, but the comparison is done using the
		absolute values of the operands.
		
		"""
		pass
		
	def next_minus(self, context):
		"""
		Return the largest number representable in the given context (or in the
		current thread's context if no context is given) that is smaller than the
		given operand.
		
		"""
		pass
		
	def next_plus(self, context):
		"""
		Return the smallest number representable in the given context (or in the
		current thread's context if no context is given) that is larger than the
		given operand.
		
		"""
		pass
		
	def next_toward(self, other,context):
		"""
		If the two operands are unequal, return the number closest to the first
		operand in the direction of the second operand.  If both operands are
		numerically equal, return a copy of the first operand with the sign set to
		be the same as the sign of the second operand.
		
		"""
		pass
		
	def normalize(self, context):
		"""
		Normalize the number by stripping the rightmost trailing zeros and
		converting any result equal to :const:`Decimal('0')` to
		:const:`Decimal('0e0')`. Used for producing canonical values for members
		of an equivalence class. For example, ``Decimal('32.100')`` and
		``Decimal('0.321000e+2')`` both normalize to the equivalent value
		``Decimal('32.1')``.
		
		"""
		pass
		
	def number__class(self, context):
		"""
		Return a string describing the *class* of the operand.  The returned value
		is one of the following ten strings.
		
		* ``"-Infinity"``, indicating that the operand is negative infinity.
		* ``"-Normal"``, indicating that the operand is a negative normal number.
		* ``"-Subnormal"``, indicating that the operand is negative and subnormal.
		* ``"-Zero"``, indicating that the operand is a negative zero.
		* ``"+Zero"``, indicating that the operand is a positive zero.
		* ``"+Subnormal"``, indicating that the operand is positive and subnormal.
		* ``"+Normal"``, indicating that the operand is a positive normal number.
		* ``"+Infinity"``, indicating that the operand is positive infinity.
		* ``"NaN"``, indicating that the operand is a quiet NaN (Not a Number).
		* ``"sNaN"``, indicating that the operand is a signaling NaN.
		
		"""
		pass
		
	def quantize(self, exp,rounding,context,watchexp):
		"""
		Return a value equal to the first operand after rounding and having the
		exponent of the second operand.
		
		>>> Decimal('1.41421356').quantize(Decimal('1.000'))
		Decimal('1.414')
		
		Unlike other operations, if the length of the coefficient after the
		quantize operation would be greater than precision, then an
		:const:`InvalidOperation` is signaled. This guarantees that, unless there
		is an error condition, the quantized exponent is always equal to that of
		the right-hand operand.
		
		Also unlike other operations, quantize never signals Underflow, even if
		the result is subnormal and inexact.
		
		If the exponent of the second operand is larger than that of the first
		then rounding may be necessary.  In this case, the rounding mode is
		determined by the ``rounding`` argument if given, else by the given
		``context`` argument; if neither argument is given the rounding mode of
		the current thread's context is used.
		
		If *watchexp* is set (default), then an error is returned whenever the
		resulting exponent is greater than :attr:`Emax` or less than
		:attr:`Etiny`.
		
		"""
		pass
		
	def radix(self, ):
		"""
		Return ``Decimal(10)``, the radix (base) in which the :class:`Decimal`
		class does all its arithmetic.  Included for compatibility with the
		specification.
		
		"""
		pass
		
	def remainder_near(self, other,context):
		"""
		Compute the modulo as either a positive or negative value depending on
		which is closest to zero.  For instance, ``Decimal(10).remainder_near(6)``
		returns ``Decimal('-2')`` which is closer to zero than ``Decimal('4')``.
		
		If both are equally close, the one chosen will have the same sign as
		*self*.
		
		"""
		pass
		
	def rotate(self, other,context):
		"""
		Return the result of rotating the digits of the first operand by an amount
		specified by the second operand.  The second operand must be an integer in
		the range -precision through precision.  The absolute value of the second
		operand gives the number of places to rotate.  If the second operand is
		positive then rotation is to the left; otherwise rotation is to the right.
		The coefficient of the first operand is padded on the left with zeros to
		length precision if necessary.  The sign and exponent of the first operand
		are unchanged.
		
		"""
		pass
		
	def same_quantum(self, other,context):
		"""
		Test whether self and other have the same exponent or whether both are
		:const:`NaN`.
		
		"""
		pass
		
	def scaleb(self, other,context):
		"""
		Return the first operand with exponent adjusted by the second.
		Equivalently, return the first operand multiplied by ``10**other``.  The
		second operand must be an integer.
		
		"""
		pass
		
	def shift(self, other,context):
		"""
		Return the result of shifting the digits of the first operand by an amount
		specified by the second operand.  The second operand must be an integer in
		the range -precision through precision.  The absolute value of the second
		operand gives the number of places to shift.  If the second operand is
		positive then the shift is to the left; otherwise the shift is to the
		right.  Digits shifted into the coefficient are zeros.  The sign and
		exponent of the first operand are unchanged.
		
		"""
		pass
		
	def sqrt(self, context):
		"""
		Return the square root of the argument to full precision.
		
		
		"""
		pass
		
	def to_eng_string(self, context):
		"""
		Convert to an engineering-type string.
		
		Engineering notation has an exponent which is a multiple of 3, so there
		are up to 3 digits left of the decimal place.  For example, converts
		``Decimal('123E+1')`` to ``Decimal('1.23E+3')``
		
		"""
		pass
		
	def to_integral(self, rounding,context):
		"""
		Identical to the :meth:`to_integral_value` method.  The ``to_integral``
		name has been kept for compatibility with older versions.
		
		"""
		pass
		
	def to_integral_exact(self, rounding,context):
		"""
		Round to the nearest integer, signaling :const:`Inexact` or
		:const:`Rounded` as appropriate if rounding occurs.  The rounding mode is
		determined by the ``rounding`` parameter if given, else by the given
		``context``.  If neither parameter is given then the rounding mode of the
		current context is used.
		
		"""
		pass
		
	def to_integral_value(self, rounding,context):
		"""
		Round to the nearest integer without signaling :const:`Inexact` or
		:const:`Rounded`.  If given, applies *rounding*; otherwise, uses the
		rounding method in either the supplied *context* or the current context.
		
		"""
		pass
		
	def getcontext(self, ):
		"""
		Return the current context for the active thread.
		
		
		"""
		pass
		
	def setcontext(self, c):
		"""
		Set the current context for the active thread to *c*.
		
		Beginning with Python 2.5, you can also use the :keyword:`with` statement and
		the :func:`localcontext` function to temporarily change the active context.
		
		
		"""
		pass
		
	def localcontext(self, c):
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
	
	
	def __init__(self, ):
		pass
	
	def clear_flags(self, ):
		"""
		Resets all of the flags to :const:`0`.
		
		"""
		pass
		
	def copy(self, ):
		"""
		Return a duplicate of the context.
		
		"""
		pass
		
	def copy_decimal(self, num):
		"""
		Return a copy of the Decimal instance num.
		
		"""
		pass
		
	def create_decimal(self, num):
		"""
		Creates a new Decimal instance from *num* but using *self* as
		context. Unlike the :class:`Decimal` constructor, the context precision,
		rounding method, flags, and traps are applied to the conversion.
		
		This is useful because constants are often given to a greater precision
		than is needed by the application.  Another benefit is that rounding
		immediately eliminates unintended effects from digits beyond the current
		precision. In the following example, using unrounded inputs means that
		adding zero to a sum can change the result:
		
		"""
		pass
		
	def create_decimal__from_float(self, f):
		"""
		Creates a new Decimal instance from a float *f* but rounding using *self*
		as the context.  Unlike the :meth:`Decimal.from_float` class method,
		the context precision, rounding method, flags, and traps are applied to
		the conversion.
		
		"""
		pass
		
	def Etiny(self, ):
		"""
		Returns a value equal to ``Emin - prec + 1`` which is the minimum exponent
		value for subnormal results.  When underflow occurs, the exponent is set
		to :const:`Etiny`.
		
		
		"""
		pass
		
	def Etop(self, ):
		"""
		Returns a value equal to ``Emax - prec + 1``.
		
		The usual approach to working with decimals is to create :class:`Decimal`
		instances and then apply arithmetic operations which take place within the
		current context for the active thread.  An alternative approach is to use
		context methods for calculating within a specific context.  The methods are
		similar to those for the :class:`Decimal` class and are only briefly
		recounted here.
		
		
		"""
		pass
		
	def abs(self, x):
		"""
		Returns the absolute value of *x*.
		
		
		"""
		pass
		
	def add(self, x,y):
		"""
		Return the sum of *x* and *y*.
		
		
		"""
		pass
		
	def canonical(self, x):
		"""
		Returns the same Decimal object *x*.
		
		
		"""
		pass
		
	def compare(self, x,y):
		"""
		Compares *x* and *y* numerically.
		
		
		"""
		pass
		
	def compare_signal(self, x,y):
		"""
		Compares the values of the two operands numerically.
		
		
		"""
		pass
		
	def compare_total(self, x,y):
		"""
		Compares two operands using their abstract representation.
		
		
		"""
		pass
		
	def compare_total_mag(self, x,y):
		"""
		Compares two operands using their abstract representation, ignoring sign.
		
		
		"""
		pass
		
	def copy_abs(self, x):
		"""
		Returns a copy of *x* with the sign set to 0.
		
		
		"""
		pass
		
	def copy_negate(self, x):
		"""
		Returns a copy of *x* with the sign inverted.
		
		
		"""
		pass
		
	def copy_sign(self, x,y):
		"""
		Copies the sign from *y* to *x*.
		
		
		"""
		pass
		
	def divide(self, x,y):
		"""
		Return *x* divided by *y*.
		
		
		"""
		pass
		
	def divide_int(self, x,y):
		"""
		Return *x* divided by *y*, truncated to an integer.
		
		
		"""
		pass
		
	def divmod(self, x,y):
		"""
		Divides two numbers and returns the integer part of the result.
		
		
		"""
		pass
		
	def exp(self, x):
		"""
		Returns `e ** x`.
		
		
		"""
		pass
		
	def fma(self, x,y,z):
		"""
		Returns *x* multiplied by *y*, plus *z*.
		
		
		"""
		pass
		
	def is_canonical(self, x):
		"""
		Returns True if *x* is canonical; otherwise returns False.
		
		
		"""
		pass
		
	def is_finite(self, x):
		"""
		Returns True if *x* is finite; otherwise returns False.
		
		
		"""
		pass
		
	def is_infinite(self, x):
		"""
		Returns True if *x* is infinite; otherwise returns False.
		
		
		"""
		pass
		
	def is_nan(self, x):
		"""
		Returns True if *x* is a qNaN or sNaN; otherwise returns False.
		
		
		"""
		pass
		
	def is_normal(self, x):
		"""
		Returns True if *x* is a normal number; otherwise returns False.
		
		
		"""
		pass
		
	def is_qnan(self, x):
		"""
		Returns True if *x* is a quiet NaN; otherwise returns False.
		
		
		"""
		pass
		
	def is_signed(self, x):
		"""
		Returns True if *x* is negative; otherwise returns False.
		
		
		"""
		pass
		
	def is_snan(self, x):
		"""
		Returns True if *x* is a signaling NaN; otherwise returns False.
		
		
		"""
		pass
		
	def is_subnormal(self, x):
		"""
		Returns True if *x* is subnormal; otherwise returns False.
		
		
		"""
		pass
		
	def is_zero(self, x):
		"""
		Returns True if *x* is a zero; otherwise returns False.
		
		
		"""
		pass
		
	def ln(self, x):
		"""
		Returns the natural (base e) logarithm of *x*.
		
		
		"""
		pass
		
	def log10(self, x):
		"""
		Returns the base 10 logarithm of *x*.
		
		
		"""
		pass
		
	def logb(self, x):
		"""
		Returns the exponent of the magnitude of the operand's MSD.
		
		
		"""
		pass
		
	def logical_and(self, x,y):
		"""
		Applies the logical operation *and* between each operand's digits.
		
		
		"""
		pass
		
	def logical_invert(self, x):
		"""
		Invert all the digits in *x*.
		
		
		"""
		pass
		
	def logical_or(self, x,y):
		"""
		Applies the logical operation *or* between each operand's digits.
		
		
		"""
		pass
		
	def logical_xor(self, x,y):
		"""
		Applies the logical operation *xor* between each operand's digits.
		
		
		"""
		pass
		
	def max(self, x,y):
		"""
		Compares two values numerically and returns the maximum.
		
		
		"""
		pass
		
	def max_mag(self, x,y):
		"""
		Compares the values numerically with their sign ignored.
		
		
		"""
		pass
		
	def min(self, x,y):
		"""
		Compares two values numerically and returns the minimum.
		
		
		"""
		pass
		
	def min_mag(self, x,y):
		"""
		Compares the values numerically with their sign ignored.
		
		
		"""
		pass
		
	def minus(self, x):
		"""
		Minus corresponds to the unary prefix minus operator in Python.
		
		
		"""
		pass
		
	def multiply(self, x,y):
		"""
		Return the product of *x* and *y*.
		
		
		"""
		pass
		
	def next_minus(self, x):
		"""
		Returns the largest representable number smaller than *x*.
		
		
		"""
		pass
		
	def next_plus(self, x):
		"""
		Returns the smallest representable number larger than *x*.
		
		
		"""
		pass
		
	def next_toward(self, x,y):
		"""
		Returns the number closest to *x*, in direction towards *y*.
		
		
		"""
		pass
		
	def normalize(self, x):
		"""
		Reduces *x* to its simplest form.
		
		
		"""
		pass
		
	def number__class(self, x):
		"""
		Returns an indication of the class of *x*.
		
		
		"""
		pass
		
	def plus(self, x):
		"""
		Plus corresponds to the unary prefix plus operator in Python.  This
		operation applies the context precision and rounding, so it is *not* an
		identity operation.
		
		
		"""
		pass
		
	def power(self, x,y,modulo):
		"""
		Return ``x`` to the power of ``y``, reduced modulo ``modulo`` if given.
		
		With two arguments, compute ``x**y``.  If ``x`` is negative then ``y``
		must be integral.  The result will be inexact unless ``y`` is integral and
		the result is finite and can be expressed exactly in 'precision' digits.
		The result should always be correctly rounded, using the rounding mode of
		the current thread's context.
		
		With three arguments, compute ``(x**y) % modulo``.  For the three argument
		form, the following restrictions on the arguments hold:
		
		- all three arguments must be integral
		- ``y`` must be nonnegative
		- at least one of ``x`` or ``y`` must be nonzero
		- ``modulo`` must be nonzero and have at most 'precision' digits
		
		The value resulting from ``Context.power(x, y, modulo)`` is
		equal to the value that would be obtained by computing ``(x**y)
		% modulo`` with unbounded precision, but is computed more
		efficiently.  The exponent of the result is zero, regardless of
		the exponents of ``x``, ``y`` and ``modulo``.  The result is
		always exact.
		
		"""
		pass
		
	def quantize(self, x,y):
		"""
		Returns a value equal to *x* (rounded), having the exponent of *y*.
		
		
		"""
		pass
		
	def radix(self, ):
		"""
		Just returns 10, as this is Decimal, :)
		
		
		"""
		pass
		
	def remainder(self, x,y):
		"""
		Returns the remainder from integer division.
		
		The sign of the result, if non-zero, is the same as that of the original
		dividend.
		
		"""
		pass
		
	def remainder_near(self, x,y):
		"""
		Returns ``x - y * n``, where *n* is the integer nearest the exact value
		of ``x / y`` (if the result is 0 then its sign will be the sign of *x*).
		
		
		"""
		pass
		
	def rotate(self, x,y):
		"""
		Returns a rotated copy of *x*, *y* times.
		
		
		"""
		pass
		
	def same_quantum(self, x,y):
		"""
		Returns True if the two operands have the same exponent.
		
		
		"""
		pass
		
	def scaleb(self, x,y):
		"""
		Returns the first operand after adding the second value its exp.
		
		
		"""
		pass
		
	def shift(self, x,y):
		"""
		Returns a shifted copy of *x*, *y* times.
		
		
		"""
		pass
		
	def sqrt(self, x):
		"""
		Square root of a non-negative number to context precision.
		
		
		"""
		pass
		
	def subtract(self, x,y):
		"""
		Return the difference between *x* and *y*.
		
		
		"""
		pass
		
	def to_eng_string(self, x):
		"""
		Converts a number to a string, using scientific notation.
		
		
		"""
		pass
		
	def to_integral_exact(self, x):
		"""
		Rounds to an integer.
		
		
		"""
		pass
		
	def to_sci_string(self, x):
		"""
		Converts a number to a string using scientific notation.
		
		.. .. ignals
		"""
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
	
	


