# AUTO-GENERATED FILE -- DO NOT EDIT

""" This module is always available.  It provides access to the
mathematical functions defined by the C standard. """

__package__ = None

def acos(x):
  """ acos(x)
  
  Return the arc cosine (measured in radians) of x. """
  pass

def acosh(x):
  """ acosh(x)
  
  Return the hyperbolic arc cosine (measured in radians) of x. """
  pass

def asin(x):
  """ asin(x)
  
  Return the arc sine (measured in radians) of x. """
  pass

def asinh(x):
  """ asinh(x)
  
  Return the hyperbolic arc sine (measured in radians) of x. """
  pass

def atan(x):
  """ atan(x)
  
  Return the arc tangent (measured in radians) of x. """
  pass

def atan2(y, x):
  """ atan2(y, x)
  
  Return the arc tangent (measured in radians) of y/x.
  Unlike atan(y/x), the signs of both x and y are considered. """
  pass

def atanh(x):
  """ atanh(x)
  
  Return the hyperbolic arc tangent (measured in radians) of x. """
  pass

def ceil(x):
  """ ceil(x)
  
  Return the ceiling of x as a float.
  This is the smallest integral value >= x. """
  pass

def copysign(x, y):
  """ copysign(x, y)
  
  Return x with the sign of y. """
  pass

def cos(x):
  """ cos(x)
  
  Return the cosine of x (measured in radians). """
  pass

def cosh(x):
  """ cosh(x)
  
  Return the hyperbolic cosine of x. """
  pass

def degrees(x):
  """ degrees(x)
  
  Convert angle x from radians to degrees. """
  pass

e = 2.71828182846

def erf(x):
  """ erf(x)
  
  Error function at x. """
  pass

def erfc(x):
  """ erfc(x)
  
  Complementary error function at x. """
  pass

def exp(x):
  """ exp(x)
  
  Return e raised to the power of x. """
  pass

def expm1(x):
  """ expm1(x)
  
  Return exp(x)-1.
  This function avoids the loss of precision involved in the direct evaluation of exp(x)-1 for small x. """
  pass

def fabs(x):
  """ fabs(x)
  
  Return the absolute value of the float x. """
  pass

def factorial(x):
  """ factorial(x) -> Integral
  
  Find x!. Raise a ValueError if x is negative or non-integral. """
  return None

def floor(x):
  """ floor(x)
  
  Return the floor of x as a float.
  This is the largest integral value <= x. """
  pass

def fmod(x, y):
  """ fmod(x, y)
  
  Return fmod(x, y), according to platform C.  x % y may differ. """
  pass

def frexp(x):
  """ frexp(x)
  
  Return the mantissa and exponent of x, as pair (m, e).
  m is a float and e is an int, such that x = m * 2.**e.
  If x is 0, m and e are both 0.  Else 0.5 <= abs(m) < 1.0. """
  pass

def fsum(iterable):
  """ fsum(iterable)
  
  Return an accurate floating point sum of values in the iterable.
  Assumes IEEE-754 floating point arithmetic. """
  pass

def gamma(x):
  """ gamma(x)
  
  Gamma function at x. """
  pass

def hypot(x, y):
  """ hypot(x, y)
  
  Return the Euclidean distance, sqrt(x*x + y*y). """
  pass

def isinf(x):
  """ isinf(x) -> bool
  
  Check if float x is infinite (positive or negative). """
  return None

def isnan(x):
  """ isnan(x) -> bool
  
  Check if float x is not a number (NaN). """
  return None

def ldexp(x, i):
  """ ldexp(x, i)
  
  Return x * (2**i). """
  pass

def lgamma(x):
  """ lgamma(x)
  
  Natural logarithm of absolute value of Gamma function at x. """
  pass

def log(x, base=None):
  """ log(x[, base])
  
  Return the logarithm of x to the given base.
  If the base not specified, returns the natural logarithm (base e) of x. """
  pass

def log10(x):
  """ log10(x)
  
  Return the base 10 logarithm of x. """
  pass

def log1p(x):
  """ log1p(x)
  
  Return the natural logarithm of 1+x (base e).
  The result is computed in a way which is accurate for x near zero. """
  pass

def modf(x):
  """ modf(x)
  
  Return the fractional and integer parts of x.  Both results carry the sign
  of x and are floats. """
  pass

pi = 3.14159265359

def pow(x, y):
  """ pow(x, y)
  
  Return x**y (x to the power of y). """
  pass

def radians(x):
  """ radians(x)
  
  Convert angle x from degrees to radians. """
  pass

def sin(x):
  """ sin(x)
  
  Return the sine of x (measured in radians). """
  pass

def sinh(x):
  """ sinh(x)
  
  Return the hyperbolic sine of x. """
  pass

def sqrt(x):
  """ sqrt(x)
  
  Return the square root of x. """
  pass

def tan(x):
  """ tan(x)
  
  Return the tangent of x (measured in radians). """
  pass

def tanh(x):
  """ tanh(x)
  
  Return the hyperbolic tangent of x. """
  pass

def trunc(arg0):
  """ trunc(x:Real) -> Integral
  
  Truncates x to the nearest Integral toward 0. Uses the __trunc__ magic method. """
  return None

