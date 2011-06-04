#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
""":synopsis: Functions corresponding to the standard operators.
"""
def lt(a,b):
	"""le(a, b)
	eq(a, b)
	ne(a, b)
	ge(a, b)
	gt(a, b)
	__lt__(a, b)
	__le__(a, b)
	__eq__(a, b)
	__ne__(a, b)
	__ge__(a, b)
	__gt__(a, b)
	
	Perform "rich comparisons" between *a* and *b*. Specifically, ``lt(a, b)`` is
	equivalent to ``a < b``, ``le(a, b)`` is equivalent to ``a <= b``, ``eq(a,
	b)`` is equivalent to ``a == b``, ``ne(a, b)`` is equivalent to ``a != b``,
	``gt(a, b)`` is equivalent to ``a > b`` and ``ge(a, b)`` is equivalent to ``a
	>= b``.  Note that unlike the built-in :func:`cmp`, these functions can
	return any value, which may or may not be interpretable as a Boolean value.
	See :ref:`comparisons` for more information about rich comparisons.
	
	"""
	pass
	
def not_(obj):
	"""__not__(obj)
	
	Return the outcome of :keyword:`not` *obj*.  (Note that there is no
	:meth:`__not__` method for object instances; only the interpreter core defines
	this operation.  The result is affected by the :meth:`__nonzero__` and
	:meth:`__len__` methods.)
	
	
	"""
	pass
	
def truth(obj):
	"""
	Return :const:`True` if *obj* is true, and :const:`False` otherwise.  This is
	equivalent to using the :class:`bool` constructor.
	
	
	"""
	pass
	
def is_(a,b):
	"""
	Return ``a is b``.  Tests object identity.
	
	"""
	pass
	
def is_not(a,b):
	"""
	Return ``a is not b``.  Tests object identity.
	
	"""
	pass
	
def abs(obj):
	"""__abs__(obj)
	
	Return the absolute value of *obj*.
	
	
	"""
	pass
	
def add(a,b):
	"""__add__(a, b)
	
	Return ``a + b``, for *a* and *b* numbers.
	
	
	"""
	pass
	
def and_(a,b):
	"""__and__(a, b)
	
	Return the bitwise and of *a* and *b*.
	
	
	"""
	pass
	
def div(a,b):
	"""__div__(a, b)
	
	Return ``a / b`` when ``__future__.division`` is not in effect.  This is
	also known as "classic" division.
	
	
	"""
	pass
	
def floordiv(a,b):
	"""__floordiv__(a, b)
	
	Return ``a // b``.
	
	"""
	pass
	
def index(a):
	"""__index__(a)
	
	Return *a* converted to an integer.  Equivalent to ``a.__index__()``.
	
	"""
	pass
	
def inv(obj):
	"""invert(obj)
	__inv__(obj)
	__invert__(obj)
	
	Return the bitwise inverse of the number *obj*.  This is equivalent to ``~obj``.
	
	"""
	pass
	
def lshift(a,b):
	"""__lshift__(a, b)
	
	Return *a* shifted left by *b*.
	
	
	"""
	pass
	
def mod(a,b):
	"""__mod__(a, b)
	
	Return ``a % b``.
	
	
	"""
	pass
	
def mul(a,b):
	"""__mul__(a, b)
	
	Return ``a * b``, for *a* and *b* numbers.
	
	
	"""
	pass
	
def neg(obj):
	"""__neg__(obj)
	
	Return *obj* negated (``-obj``).
	
	
	"""
	pass
	
def or_(a,b):
	"""__or__(a, b)
	
	Return the bitwise or of *a* and *b*.
	
	
	"""
	pass
	
def pos(obj):
	"""__pos__(obj)
	
	Return *obj* positive (``+obj``).
	
	
	"""
	pass
	
def pow(a,b):
	"""__pow__(a, b)
	
	Return ``a ** b``, for *a* and *b* numbers.
	
	"""
	pass
	
def rshift(a,b):
	"""__rshift__(a, b)
	
	Return *a* shifted right by *b*.
	
	
	"""
	pass
	
def sub(a,b):
	"""__sub__(a, b)
	
	Return ``a - b``.
	
	
	"""
	pass
	
def truediv(a,b):
	"""__truediv__(a, b)
	
	Return ``a / b`` when ``__future__.division`` is in effect.  This is also
	known as "true" division.
	
	"""
	pass
	
def xor(a,b):
	"""__xor__(a, b)
	
	Return the bitwise exclusive or of *a* and *b*.
	
	
	Operations which work with sequences (some of them with mappings too) include:
	
	"""
	pass
	
def concat(a,b):
	"""__concat__(a, b)
	
	Return ``a + b`` for *a* and *b* sequences.
	
	
	"""
	pass
	
def contains(a,b):
	"""__contains__(a, b)
	
	Return the outcome of the test ``b in a``. Note the reversed operands.
	
	"""
	pass
	
def countOf(a,b):
	"""
	Return the number of occurrences of *b* in *a*.
	
	
	"""
	pass
	
def delitem(a,b):
	"""__delitem__(a, b)
	
	Remove the value of *a* at index *b*.
	
	
	"""
	pass
	
def delslice(a,b,c):
	"""__delslice__(a, b, c)
	
	Delete the slice of *a* from index *b* to index *c-1*.
	
	"""
	pass
	
def getitem(a,b):
	"""__getitem__(a, b)
	
	Return the value of *a* at index *b*.
	
	
	"""
	pass
	
def getslice(a,b,c):
	"""__getslice__(a, b, c)
	
	Return the slice of *a* from index *b* to index *c-1*.
	
	"""
	pass
	
def indexOf(a,b):
	"""
	Return the index of the first of occurrence of *b* in *a*.
	
	
	"""
	pass
	
def repeat(a,b):
	"""__repeat__(a, b)
	
	"""
	pass
	
def sequenceIncludes(more):
	"""
	"""
	pass
	
def setitem(a,b,c):
	"""__setitem__(a, b, c)
	
	Set the value of *a* at index *b* to *c*.
	
	
	"""
	pass
	
def setslice(a,b,c,v):
	"""__setslice__(a, b, c, v)
	
	Set the slice of *a* from index *b* to index *c-1* to the sequence *v*.
	
	"""
	pass
	
def iadd(a,b):
	"""__iadd__(a, b)
	
	``a = iadd(a, b)`` is equivalent to ``a += b``.
	
	"""
	pass
	
def iand(a,b):
	"""__iand__(a, b)
	
	``a = iand(a, b)`` is equivalent to ``a &= b``.
	
	"""
	pass
	
def iconcat(a,b):
	"""__iconcat__(a, b)
	
	``a = iconcat(a, b)`` is equivalent to ``a += b`` for *a* and *b* sequences.
	
	"""
	pass
	
def idiv(a,b):
	"""__idiv__(a, b)
	
	``a = idiv(a, b)`` is equivalent to ``a /= b`` when ``__future__.division`` is
	not in effect.
	
	"""
	pass
	
def ifloordiv(a,b):
	"""__ifloordiv__(a, b)
	
	``a = ifloordiv(a, b)`` is equivalent to ``a //= b``.
	
	"""
	pass
	
def ilshift(a,b):
	"""__ilshift__(a, b)
	
	``a = ilshift(a, b)`` is equivalent to ``a <<= b``.
	
	"""
	pass
	
def imod(a,b):
	"""__imod__(a, b)
	
	``a = imod(a, b)`` is equivalent to ``a %= b``.
	
	"""
	pass
	
def imul(a,b):
	"""__imul__(a, b)
	
	``a = imul(a, b)`` is equivalent to ``a *= b``.
	
	"""
	pass
	
def ior(a,b):
	"""__ior__(a, b)
	
	``a = ior(a, b)`` is equivalent to ``a |= b``.
	
	"""
	pass
	
def ipow(a,b):
	"""__ipow__(a, b)
	
	``a = ipow(a, b)`` is equivalent to ``a **= b``.
	
	"""
	pass
	
def irepeat(a,b):
	"""__irepeat__(a, b)
	
	"""
	pass
	
def irshift(a,b):
	"""__irshift__(a, b)
	
	``a = irshift(a, b)`` is equivalent to ``a >>= b``.
	
	"""
	pass
	
def isub(a,b):
	"""__isub__(a, b)
	
	``a = isub(a, b)`` is equivalent to ``a -= b``.
	
	"""
	pass
	
def itruediv(a,b):
	"""__itruediv__(a, b)
	
	``a = itruediv(a, b)`` is equivalent to ``a /= b`` when ``__future__.division``
	is in effect.
	
	"""
	pass
	
def ixor(a,b):
	"""__ixor__(a, b)
	
	``a = ixor(a, b)`` is equivalent to ``a ^= b``.
	
	"""
	pass
	
def isCallable(obj):
	"""
	"""
	pass
	
def isMappingType(obj):
	"""
	"""
	pass
	
def isNumberType(obj):
	"""
	"""
	pass
	
def isSequenceType(obj):
	"""
	"""
	pass
	
def attrgetter(attr,argsmore):
	"""
	Return a callable object that fetches *attr* from its operand. If more than one
	attribute is requested, returns a tuple of attributes. After,
	``f = attrgetter('name')``, the call ``f(b)`` returns ``b.name``.  After,
	``f = attrgetter('name', 'date')``, the call ``f(b)`` returns ``(b.name,
	b.date)``.  Equivalent to::
	
	def attrgetter(*items):
	if len(items) == 1:
	attr = items[0]
	def g(obj):
	return resolve_attr(obj, attr)
	else:
	def g(obj):
	return tuple(resolve_att(obj, attr) for attr in items)
	return g
	
	def resolve_attr(obj, attr):
	for name in attr.split("."):
	obj = getattr(obj, name)
	return obj
	
	
	The attribute names can also contain dots; after ``f = attrgetter('date.month')``,
	the call ``f(b)`` returns ``b.date.month``.
	
	"""
	pass
	
def itemgetter(item,argsmore):
	"""
	Return a callable object that fetches *item* from its operand using the
	operand's :meth:`__getitem__` method.  If multiple items are specified,
	returns a tuple of lookup values.  Equivalent to::
	
	def itemgetter(*items):
	if len(items) == 1:
	item = items[0]
	def g(obj):
	return obj[item]
	else:
	def g(obj):
	return tuple(obj[item] for item in items)
	return g
	
	The items can be any type accepted by the operand's :meth:`__getitem__`
	method.  Dictionaries accept any hashable value.  Lists, tuples, and
	strings accept an index or a slice:
	
	>>> itemgetter(1)('ABCDEFG')
	'B'
	>>> itemgetter(1,3,5)('ABCDEFG')
	('B', 'D', 'F')
	>>> itemgetter(slice(2,None))('ABCDEFG')
	'CDEFG'
	
	"""
	pass
	
def methodcaller(name,argsmore):
	"""
	Return a callable object that calls the method *name* on its operand.  If
	additional arguments and/or keyword arguments are given, they will be given
	to the method as well.  After ``f = methodcaller('name')``, the call ``f(b)``
	returns ``b.name()``.  After ``f = methodcaller('name', 'foo', bar=1)``, the
	call ``f(b)`` returns ``b.name('foo', bar=1)``.  Equivalent to::
	
	def methodcaller(name, *args, **kwargs):
	def caller(obj):
	return getattr(obj, name)(*args, **kwargs)
	return caller
	
	"""
	pass
	
