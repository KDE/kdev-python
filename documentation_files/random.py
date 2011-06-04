#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
""":synopsis: Generate pseudo-random numbers with various common distributions.


This module implements pseudo-random number generators for various
distributions.

"""
def seed(x):
	"""
	Initialize the basic random number generator. Optional argument *x* can be any
	:term:`hashable` object. If *x* is omitted or ``None``, current system time is used;
	current system time is also used to initialize the generator when the module is
	first imported.  If randomness sources are provided by the operating system,
	they are used instead of the system time (see the :func:`os.urandom` function
	for details on availability).
	
	"""
	pass
	
def getstate():
	"""
	Return an object capturing the current internal state of the generator.  This
	object can be passed to :func:`setstate` to restore the state.
	
	"""
	pass
	
def setstate(state):
	"""
	*state* should have been obtained from a previous call to :func:`getstate`, and
	:func:`setstate` restores the internal state of the generator to what it was at
	the time :func:`setstate` was called.
	
	"""
	pass
	
def jumpahead(n):
	"""
	Change the internal state to one different from and likely far away from the
	current state.  *n* is a non-negative integer which is used to scramble the
	current state vector.  This is most useful in multi-threaded programs, in
	conjunction with multiple instances of the :class:`Random` class:
	:meth:`setstate` or :meth:`seed` can be used to force all instances into the
	same internal state, and then :meth:`jumpahead` can be used to force the
	instances' states far apart.
	
	"""
	pass
	
def getrandbits(k):
	"""
	Returns a python :class:`long` int with *k* random bits. This method is supplied
	with the MersenneTwister generator and some other generators may also provide it
	as an optional part of the API. When available, :meth:`getrandbits` enables
	:meth:`randrange` to handle arbitrarily large ranges.
	
	"""
	pass
	
def randrange(start,stop,step):
	"""
	Return a randomly selected element from ``range(start, stop, step)``.  This is
	equivalent to ``choice(range(start, stop, step))``, but doesn't actually build a
	range object.
	
	"""
	pass
	
def randint(a,b):
	"""
	Return a random integer *N* such that ``a <= N <= b``.
	
	Functions for sequences:
	
	
	"""
	pass
	
def choice(seq):
	"""
	Return a random element from the non-empty sequence *seq*. If *seq* is empty,
	raises :exc:`IndexError`.
	
	
	"""
	pass
	
def shuffle(x,random):
	"""
	Shuffle the sequence *x* in place. The optional argument *random* is a
	0-argument function returning a random float in [0.0, 1.0); by default, this is
	the function :func:`random`.
	
	Note that for even rather small ``len(x)``, the total number of permutations of
	*x* is larger than the period of most random number generators; this implies
	that most permutations of a long sequence can never be generated.
	
	
	"""
	pass
	
def sample(population,k):
	"""
	Return a *k* length list of unique elements chosen from the population sequence.
	Used for random sampling without replacement.
	
	"""
	pass
	
def random():
	"""
	Return the next random floating point number in the range [0.0, 1.0).
	
	
	"""
	pass
	
def uniform(a,b):
	"""
	Return a random floating point number *N* such that ``a <= N <= b`` for
	``a <= b`` and ``b <= N <= a`` for ``b < a``.
	
	The end-point value ``b`` may or may not be included in the range
	depending on floating-point rounding in the equation ``a + (b-a) * random()``.
	
	"""
	pass
	
def triangular(low,high,mode):
	"""
	Return a random floating point number *N* such that ``low <= N <= high`` and
	with the specified *mode* between those bounds.  The *low* and *high* bounds
	default to zero and one.  The *mode* argument defaults to the midpoint
	between the bounds, giving a symmetric distribution.
	
	"""
	pass
	
def betavariate(alpha,beta):
	"""
	Beta distribution.  Conditions on the parameters are ``alpha > 0`` and
	``beta > 0``. Returned values range between 0 and 1.
	
	
	"""
	pass
	
def expovariate(lambd):
	"""
	Exponential distribution.  *lambd* is 1.0 divided by the desired
	mean.  It should be nonzero.  (The parameter would be called
	"lambda", but that is a reserved word in Python.)  Returned values
	range from 0 to positive infinity if *lambd* is positive, and from
	negative infinity to 0 if *lambd* is negative.
	
	
	"""
	pass
	
def gammavariate(alpha,beta):
	"""
	Gamma distribution.  (*Not* the gamma function!)  Conditions on the
	parameters are ``alpha > 0`` and ``beta > 0``.
	
	
	"""
	pass
	
def gauss(mu,sigma):
	"""
	Gaussian distribution.  *mu* is the mean, and *sigma* is the standard
	deviation.  This is slightly faster than the :func:`normalvariate` function
	defined below.
	
	
	"""
	pass
	
def lognormvariate(mu,sigma):
	"""
	Log normal distribution.  If you take the natural logarithm of this
	distribution, you'll get a normal distribution with mean *mu* and standard
	deviation *sigma*.  *mu* can have any value, and *sigma* must be greater than
	zero.
	
	
	"""
	pass
	
def normalvariate(mu,sigma):
	"""
	Normal distribution.  *mu* is the mean, and *sigma* is the standard deviation.
	
	
	"""
	pass
	
def vonmisesvariate(mu,kappa):
	"""
	*mu* is the mean angle, expressed in radians between 0 and 2\*\ *pi*, and *kappa*
	is the concentration parameter, which must be greater than or equal to zero.  If
	*kappa* is equal to zero, this distribution reduces to a uniform random angle
	over the range 0 to 2\*\ *pi*.
	
	
	"""
	pass
	
def paretovariate(alpha):
	"""
	Pareto distribution.  *alpha* is the shape parameter.
	
	
	"""
	pass
	
def weibullvariate(alpha,beta):
	"""
	Weibull distribution.  *alpha* is the scale parameter and *beta* is the shape
	parameter.
	
	
	Alternative Generators:
	
	"""
	pass
	
class WichmannHill:


	"""
	Class that implements the Wichmann-Hill algorithm as the core generator. Has all
	of the same methods as :class:`Random` plus the :meth:`whseed` method described
	below.  Because this class is implemented in pure Python, it is not threadsafe
	and may require locks between calls.  The period of the generator is
	6,953,607,871,644 which is small enough to require care that two independent
	random sequences do not overlap.
	
	
	"""
	
	
	def __init__(self, seed):
		pass
	
	def whseed(x):
		"""
		This is obsolete, supplied for bit-level compatibility with versions of Python
		prior to 2.1. See :func:`seed` for details.  :func:`whseed` does not guarantee
		that distinct integer arguments yield distinct internal states, and can yield no
		more than about 2\*\*24 distinct internal states in all.
		
		
		"""
		pass
		
	


class SystemRandom:


	"""
	Class that uses the :func:`os.urandom` function for generating random numbers
	from sources provided by the operating system. Not available on all systems.
	Does not rely on software state and sequences are not reproducible. Accordingly,
	the :meth:`seed` and :meth:`jumpahead` methods have no effect and are ignored.
	The :meth:`getstate` and :meth:`setstate` methods raise
	:exc:`NotImplementedError` if called.
	
	"""
	
	
	def __init__(self, seed):
		pass
	
	


