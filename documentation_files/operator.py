# AUTO-GENERATED FILE -- DO NOT EDIT

""" Operator interface.

This module exports a set of functions implemented in C corresponding
to the intrinsic operators of Python.  For example, operator.add(x, y)
is equivalent to the expression x+y.  The function names are those
used for special methods; variants without leading and trailing
'__' are also provided for convenience. """

def __abs__(a):
  """ abs(a) -- Same as abs(a). """
  return None

def __add__(a, b):
  """ add(a, b) -- Same as a + b. """
  return None

def __and__(a, b):
  """ and_(a, b) -- Same as a & b. """
  return None

def __concat__(a, b):
  """ concat(a, b) -- Same as a + b, for a and b sequences. """
  return None

def __contains__(a, b):
  """ contains(a, b) -- Same as b in a (note reversed operands). """
  return None

def __delitem__(a, b):
  """ delitem(a, b) -- Same as del a[b]. """
  return None

def __delslice__(a, b, c):
  """ delslice(a, b, c) -- Same as del a[b:c]. """
  return None

def __div__(a, b):
  """ div(a, b) -- Same as a / b when __future__.division is not in effect. """
  return None

def __eq__(a, b):
  """ eq(a, b) -- Same as a==b. """
  return None

def __floordiv__(a, b):
  """ floordiv(a, b) -- Same as a // b. """
  return None

def __ge__(a, b):
  """ ge(a, b) -- Same as a>=b. """
  return None

def __getitem__(a, b):
  """ getitem(a, b) -- Same as a[b]. """
  return None

def __getslice__(a, b, c):
  """ getslice(a, b, c) -- Same as a[b:c]. """
  return None

def __gt__(a, b):
  """ gt(a, b) -- Same as a>b. """
  return None

def __iadd__(a, b):
  """ a = iadd(a, b) -- Same as a += b. """
  return None

def __iand__(a, b):
  """ a = iand(a, b) -- Same as a &= b. """
  return None

def __iconcat__(a, b):
  """ a = iconcat(a, b) -- Same as a += b, for a and b sequences. """
  return None

def __idiv__(a, b):
  """ a = idiv(a, b) -- Same as a /= b when __future__.division is not in effect. """
  return None

def __ifloordiv__(a, b):
  """ a = ifloordiv(a, b) -- Same as a //= b. """
  return None

def __ilshift__(a, b):
  """ a = ilshift(a, b) -- Same as a <<= b. """
  return None

def __imod__(a, b):
  """ a = imod(a, b) -- Same as a %= b. """
  return None

def __imul__(a, b):
  """ a = imul(a, b) -- Same as a *= b. """
  return None

def __index__(a):
  """ index(a) -- Same as a.__index__() """
  return None

def __inv__(a):
  """ inv(a) -- Same as ~a. """
  return None

def __invert__(a):
  """ invert(a) -- Same as ~a. """
  return None

def __ior__(a, b):
  """ a = ior(a, b) -- Same as a |= b. """
  return None

def __ipow__(a, b):
  """ a = ipow(a, b) -- Same as a **= b. """
  return None

def __irepeat__(a, b):
  """ a = irepeat(a, b) -- Same as a *= b, where a is a sequence, and b is an integer. """
  return 1

def __irshift__(a, b):
  """ a = irshift(a, b) -- Same as a >>= b. """
  return None

def __isub__(a, b):
  """ a = isub(a, b) -- Same as a -= b. """
  return None

def __itruediv__(a, b):
  """ a = itruediv(a, b) -- Same as a /= b when __future__.division is in effect. """
  return None

def __ixor__(a, b):
  """ a = ixor(a, b) -- Same as a ^= b. """
  return None

def __le__(a, b):
  """ le(a, b) -- Same as a<=b. """
  return None

def __lshift__(a, b):
  """ lshift(a, b) -- Same as a << b. """
  return None

def __lt__(a, b):
  """ lt(a, b) -- Same as a<b. """
  return None

def __mod__(a, b):
  """ mod(a, b) -- Same as a % b. """
  return None

def __mul__(a, b):
  """ mul(a, b) -- Same as a * b. """
  return None

def __ne__(a, b):
  """ ne(a, b) -- Same as a!=b. """
  return None

def __neg__(a):
  """ neg(a) -- Same as -a. """
  return None

def __not__(a):
  """ not_(a) -- Same as not a. """
  return None

def __or__(a, b):
  """ or_(a, b) -- Same as a | b. """
  return None

__package__ = None

def __pos__(a):
  """ pos(a) -- Same as +a. """
  return None

def __pow__(a, b):
  """ pow(a, b) -- Same as a ** b. """
  return None

def __repeat__(a, b):
  """ repeat(a, b) -- Return a * b, where a is a sequence, and b is an integer. """
  return 1

def __rshift__(a, b):
  """ rshift(a, b) -- Same as a >> b. """
  return None

def __setitem__(a, b, c):
  """ setitem(a, b, c) -- Same as a[b] = c. """
  return None

def __setslice__(a, b, c, d):
  """ setslice(a, b, c, d) -- Same as a[b:c] = d. """
  return None

def __sub__(a, b):
  """ sub(a, b) -- Same as a - b. """
  return None

def __truediv__(a, b):
  """ truediv(a, b) -- Same as a / b when __future__.division is in effect. """
  return None

def __xor__(a, b):
  """ xor(a, b) -- Same as a ^ b. """
  return None

def abs(a):
  """ abs(a) -- Same as abs(a). """
  return None

def add(a, b):
  """ add(a, b) -- Same as a + b. """
  return None

def and_(a, b):
  """ and_(a, b) -- Same as a & b. """
  return None

class attrgetter(object):
  """ attrgetter(attr, ...) --> attrgetter object
  
  Return a callable object that fetches the given attribute(s) from its operand.
  After, f=attrgetter('name'), the call f(r) returns r.name.
  After, g=attrgetter('name', 'date'), the call g(r) returns (r.name, r.date).
  After, h=attrgetter('name.first', 'name.last'), the call h(r) returns
  (r.name.first, r.name.last). """

  pass

def concat(a, b):
  """ concat(a, b) -- Same as a + b, for a and b sequences. """
  return None

def contains(a, b):
  """ contains(a, b) -- Same as b in a (note reversed operands). """
  return None

def countOf(a, b):
  """ countOf(a, b) -- Return the number of times b occurs in a. """
  return None

def delitem(a, b):
  """ delitem(a, b) -- Same as del a[b]. """
  return None

def delslice(a, b, c):
  """ delslice(a, b, c) -- Same as del a[b:c]. """
  return None

def div(a, b):
  """ div(a, b) -- Same as a / b when __future__.division is not in effect. """
  return None

def eq(a, b):
  """ eq(a, b) -- Same as a==b. """
  return None

def floordiv(a, b):
  """ floordiv(a, b) -- Same as a // b. """
  return None

def ge(a, b):
  """ ge(a, b) -- Same as a>=b. """
  return None

def getitem(a, b):
  """ getitem(a, b) -- Same as a[b]. """
  return None

def getslice(a, b, c):
  """ getslice(a, b, c) -- Same as a[b:c]. """
  return None

def gt(a, b):
  """ gt(a, b) -- Same as a>b. """
  return None

def iadd(a, b):
  """ a = iadd(a, b) -- Same as a += b. """
  return None

def iand(a, b):
  """ a = iand(a, b) -- Same as a &= b. """
  return None

def iconcat(a, b):
  """ a = iconcat(a, b) -- Same as a += b, for a and b sequences. """
  return None

def idiv(a, b):
  """ a = idiv(a, b) -- Same as a /= b when __future__.division is not in effect. """
  return None

def ifloordiv(a, b):
  """ a = ifloordiv(a, b) -- Same as a //= b. """
  return None

def ilshift(a, b):
  """ a = ilshift(a, b) -- Same as a <<= b. """
  return None

def imod(a, b):
  """ a = imod(a, b) -- Same as a %= b. """
  return None

def imul(a, b):
  """ a = imul(a, b) -- Same as a *= b. """
  return None

def index(a):
  """ index(a) -- Same as a.__index__() """
  return None

def indexOf(a, b):
  """ indexOf(a, b) -- Return the first index of b in a. """
  return None

def inv(a):
  """ inv(a) -- Same as ~a. """
  return None

def invert(a):
  """ invert(a) -- Same as ~a. """
  return None

def ior(a, b):
  """ a = ior(a, b) -- Same as a |= b. """
  return None

def ipow(a, b):
  """ a = ipow(a, b) -- Same as a **= b. """
  return None

def irepeat(a, b):
  """ a = irepeat(a, b) -- Same as a *= b, where a is a sequence, and b is an integer. """
  return 1

def irshift(a, b):
  """ a = irshift(a, b) -- Same as a >>= b. """
  return None

def isCallable(a):
  """ isCallable(a) -- Same as callable(a). """
  return None

def isMappingType(a):
  """ isMappingType(a) -- Return True if a has a mapping type, False otherwise. """
  return None

def isNumberType(a):
  """ isNumberType(a) -- Return True if a has a numeric type, False otherwise. """
  return None

def isSequenceType(a):
  """ isSequenceType(a) -- Return True if a has a sequence type, False otherwise. """
  return None

def is_(a, b):
  """ is_(a, b) -- Same as a is b. """
  return None

def is_not(a, b):
  """ is_not(a, b) -- Same as a is not b. """
  return None

def isub(a, b):
  """ a = isub(a, b) -- Same as a -= b. """
  return None

class itemgetter(object):
  """ itemgetter(item, ...) --> itemgetter object
  
  Return a callable object that fetches the given item(s) from its operand.
  After, f=itemgetter(2), the call f(r) returns r[2].
  After, g=itemgetter(2,5,3), the call g(r) returns (r[2], r[5], r[3]) """

  pass

def itruediv(a, b):
  """ a = itruediv(a, b) -- Same as a /= b when __future__.division is in effect. """
  return None

def ixor(a, b):
  """ a = ixor(a, b) -- Same as a ^= b. """
  return None

def le(a, b):
  """ le(a, b) -- Same as a<=b. """
  return None

def lshift(a, b):
  """ lshift(a, b) -- Same as a << b. """
  return None

def lt(a, b):
  """ lt(a, b) -- Same as a<b. """
  return None

class methodcaller(object):
  """ methodcaller(name, ...) --> methodcaller object
  
  Return a callable object that calls the given method on its operand.
  After, f = methodcaller('name'), the call f(r) returns r.name().
  After, g = methodcaller('name', 'date', foo=1), the call g(r) returns
  r.name('date', foo=1). """

  pass

def mod(a, b):
  """ mod(a, b) -- Same as a % b. """
  return None

def mul(a, b):
  """ mul(a, b) -- Same as a * b. """
  return None

def ne(a, b):
  """ ne(a, b) -- Same as a!=b. """
  return None

def neg(a):
  """ neg(a) -- Same as -a. """
  return None

def not_(a):
  """ not_(a) -- Same as not a. """
  return None

def or_(a, b):
  """ or_(a, b) -- Same as a | b. """
  return None

def pos(a):
  """ pos(a) -- Same as +a. """
  return None

def pow(a, b):
  """ pow(a, b) -- Same as a ** b. """
  return None

def repeat(a, b):
  """ repeat(a, b) -- Return a * b, where a is a sequence, and b is an integer. """
  return 1

def rshift(a, b):
  """ rshift(a, b) -- Same as a >> b. """
  return None

def sequenceIncludes(a, b):
  """ sequenceIncludes(a, b) -- Same as b in a (note reversed operands; deprecated). """
  return None

def setitem(a, b, c):
  """ setitem(a, b, c) -- Same as a[b] = c. """
  return None

def setslice(a, b, c, d):
  """ setslice(a, b, c, d) -- Same as a[b:c] = d. """
  return None

def sub(a, b):
  """ sub(a, b) -- Same as a - b. """
  return None

def truediv(a, b):
  """ truediv(a, b) -- Same as a / b when __future__.division is in effect. """
  return None

def truth(a):
  """ truth(a) -- Return True if a is true, False otherwise. """
  return None

def xor(a, b):
  """ xor(a, b) -- Same as a ^ b. """
  return None

