# AUTO-GENERATED FILE -- DO NOT EDIT

""" Random variable generators.

    integers
    --------
           uniform within range

    sequences
    ---------
           pick random element
           pick random sample
           generate random permutation

    distributions on the real line:
    ------------------------------
           uniform
           triangular
           normal (Gaussian)
           lognormal
           negative exponential
           gamma
           beta
           pareto
           Weibull

    distributions on the circle (angles 0 to 2pi)
    ---------------------------------------------
           circular uniform
           von Mises

General notes on the underlying Mersenne Twister core generator:

* The period is 2**19937-1.
* It is one of the most extensively tested generators in existence.
* Without a direct way to compute N steps forward, the semantics of
  jumpahead(n) are weakened to simply jump to another distant state and rely
  on the large period to avoid overlapping sequences.
* The random() method is implemented in C, executes in a single Python step,
  and is, therefore, threadsafe.

 """

class Random(Random):
  """ Random number generator base class used by bound module functions.
  
      Used to instantiate instances of Random to get generators that don't
      share state.  Especially useful for multi-threaded programs, creating
      a different instance of Random for each thread, and using the jumpahead()
      method to ensure that the generated sequences seen by each thread don't
      overlap.
  
      Class Random can also be subclassed if you want to use a different basic
      generator of your own devising: in that case, override the following
      methods: random(), seed(), getstate(), setstate() and jumpahead().
      Optionally, implement a getrandbits() method so that randrange() can cover
      arbitrarily large ranges.
  
       """

  VERSION = 3

  def __init__(self, x):
    """ Initialize an instance.
    
            Optional argument x controls seeding, as for Random.seed().
             """
    pass

  def _randbelow(self, n, _log, int, _maxwidth, _Method, _BuiltinMethod):
    """ Return a random int in the range [0,n)
    
            Handles the case where n has more bits than returned
            by a single call to the underlying generator.
             """
    pass

  def betavariate(self, alpha, beta):
    """ Beta distribution.
    
            Conditions on the parameters are alpha > 0 and beta > 0.
            Returned values range between 0 and 1.
    
             """
    pass

  def choice(self, seq):
    """ Choose a random element from a non-empty sequence. """
    pass

  def expovariate(self, arg0, arg1):
    """ Exponential distribution.
    
            lambd is 1.0 divided by the desired mean.  It should be
            nonzero.  (The parameter would be called "lambda", but that is
            a reserved word in Python.)  Returned values range from 0 to
            positive infinity if lambd is positive, and from negative
            infinity to 0 if lambd is negative.
    
             """
    pass

  def gammavariate(self, arg0):
    """ Gamma distribution.  Not the gamma function!
    
            Conditions on the parameters are alpha > 0 and beta > 0.
    
            The probability distribution function is:
    
                        x ** (alpha - 1) * math.exp(-x / beta)
              pdf(x) =  --------------------------------------
                          math.gamma(alpha) * beta ** alpha
    
             """
    pass

  def gauss(self, mu, sigma):
    """ Gaussian distribution.
    
            mu is the mean, and sigma is the standard deviation.  This is
            slightly faster than the normalvariate() function.
    
            Not thread-safe without a lock around calls.
    
             """
    pass

  def getstate(self):
    """ Return internal state; can be passed to setstate() later. """
    pass

  def jumpahead(self, n):
    """ Change the internal state to one that is likely far away
            from the current state.  This method will not be in Py3.x,
            so it is better to simply reseed.
             """
    pass

  def lognormvariate(self, mu, sigma):
    """ Log normal distribution.
    
            If you take the natural logarithm of this distribution, you'll get a
            normal distribution with mean mu and standard deviation sigma.
            mu can have any value, and sigma must be greater than zero.
    
             """
    pass

  def normalvariate(self, mu, sigma):
    """ Normal distribution.
    
            mu is the mean, and sigma is the standard deviation.
    
             """
    pass

  def paretovariate(self, alpha):
    """ Pareto distribution.  alpha is the shape parameter. """
    pass

  def randint(self, a, b):
    """ Return random integer in range [a, b], including both end points.
             """
    pass

  def randrange(self, start, stop, step=None):
    """ Choose a random item from range(start, stop[, step]).
    
            This fixes the problem with randint() which includes the
            endpoint; in Python this is usually not what you want.
            Do not supply the 'int', 'default', and 'maxwidth' arguments.
             """
    pass

  def sample(self, arg0):
    """ Chooses k unique random elements from a population sequence.
    
            Returns a new list containing elements from the population while
            leaving the original population unchanged.  The resulting list is
            in selection order so that all sub-slices will also be valid random
            samples.  This allows raffle winners (the sample) to be partitioned
            into grand prize and second place winners (the subslices).
    
            Members of the population need not be hashable or unique.  If the
            population contains repeats, then each occurrence is a possible
            selection in the sample.
    
            To choose a sample in a range of integers, use xrange as an argument.
            This is especially fast and space efficient for sampling from a
            large population:   sample(xrange(10000000), 60)
             """
    pass

  def seed(self, a):
    """ Initialize internal state from hashable object.
    
            None or no argument seeds from current time or from an operating
            system specific randomness source if available.
    
            If a is not None or an int or long, hash(a) is used instead.
             """
    pass

  def setstate(self, state):
    """ Restore internal state from object returned by getstate(). """
    pass

  def shuffle(self, x, random=random.random):
    """ x, random=random.random -> shuffle list x in place; return None.
    
            Optional arg random is a 0-argument function returning a random
            float in [0.0, 1.0); by default, the standard random.random.
             """
    return []

  def triangular(self, low, high, mode):
    """ Triangular distribution.
    
            Continuous distribution bounded by given lower and upper limits,
            and having a given mode value in-between.
    
            http://en.wikipedia.org/wiki/Triangular_distribution
    
             """
    pass

  def uniform(self, a, b):
    """ Get a random number in the range [a, b) or [a, b] depending on rounding. """
    pass

  def vonmisesvariate(self, mu, kappa):
    """ Circular data distribution.
    
            mu is the mean angle, expressed in radians between 0 and 2*pi, and
            kappa is the concentration parameter, which must be greater than or
            equal to zero.  If kappa is equal to zero, this distribution reduces
            to a uniform random angle over the range 0 to 2*pi.
    
             """
    pass

  def weibullvariate(self, alpha, beta):
    """ Weibull distribution.
    
            alpha is the scale parameter and beta is the shape parameter.
    
             """
    pass

def seed(self, a):
  """ Initialize internal state from hashable object.
  
          None or no argument seeds from current time or from an operating
          system specific randomness source if available.
  
          If a is not None or an int or long, hash(a) is used instead.
           """
  pass

def random():
  """ random() -> x in the interval [0, 1). """
  return 1

def uniform(self, a, b):
  """ Get a random number in the range [a, b) or [a, b] depending on rounding. """
  pass

def randint(self, a, b):
  """ Return random integer in range [a, b], including both end points.
           """
  pass

def choice(self, seq):
  """ Choose a random element from a non-empty sequence. """
  pass

def sample(self, arg0):
  """ Chooses k unique random elements from a population sequence.
  
          Returns a new list containing elements from the population while
          leaving the original population unchanged.  The resulting list is
          in selection order so that all sub-slices will also be valid random
          samples.  This allows raffle winners (the sample) to be partitioned
          into grand prize and second place winners (the subslices).
  
          Members of the population need not be hashable or unique.  If the
          population contains repeats, then each occurrence is a possible
          selection in the sample.
  
          To choose a sample in a range of integers, use xrange as an argument.
          This is especially fast and space efficient for sampling from a
          large population:   sample(xrange(10000000), 60)
           """
  pass

def randrange(self, start, stop, step=None):
  """ Choose a random item from range(start, stop[, step]).
  
          This fixes the problem with randint() which includes the
          endpoint; in Python this is usually not what you want.
          Do not supply the 'int', 'default', and 'maxwidth' arguments.
           """
  pass

def shuffle(self, x, random=random.random):
  """ x, random=random.random -> shuffle list x in place; return None.
  
          Optional arg random is a 0-argument function returning a random
          float in [0.0, 1.0); by default, the standard random.random.
           """
  return []

def normalvariate(self, mu, sigma):
  """ Normal distribution.
  
          mu is the mean, and sigma is the standard deviation.
  
           """
  pass

def lognormvariate(self, mu, sigma):
  """ Log normal distribution.
  
          If you take the natural logarithm of this distribution, you'll get a
          normal distribution with mean mu and standard deviation sigma.
          mu can have any value, and sigma must be greater than zero.
  
           """
  pass

def expovariate(self, arg0, arg1):
  """ Exponential distribution.
  
          lambd is 1.0 divided by the desired mean.  It should be
          nonzero.  (The parameter would be called "lambda", but that is
          a reserved word in Python.)  Returned values range from 0 to
          positive infinity if lambd is positive, and from negative
          infinity to 0 if lambd is negative.
  
           """
  pass

def vonmisesvariate(self, mu, kappa):
  """ Circular data distribution.
  
          mu is the mean angle, expressed in radians between 0 and 2*pi, and
          kappa is the concentration parameter, which must be greater than or
          equal to zero.  If kappa is equal to zero, this distribution reduces
          to a uniform random angle over the range 0 to 2*pi.
  
           """
  pass

def gammavariate(self, arg0):
  """ Gamma distribution.  Not the gamma function!
  
          Conditions on the parameters are alpha > 0 and beta > 0.
  
          The probability distribution function is:
  
                      x ** (alpha - 1) * math.exp(-x / beta)
            pdf(x) =  --------------------------------------
                        math.gamma(alpha) * beta ** alpha
  
           """
  pass

def triangular(self, low, high, mode):
  """ Triangular distribution.
  
          Continuous distribution bounded by given lower and upper limits,
          and having a given mode value in-between.
  
          http://en.wikipedia.org/wiki/Triangular_distribution
  
           """
  pass

def gauss(self, mu, sigma):
  """ Gaussian distribution.
  
          mu is the mean, and sigma is the standard deviation.  This is
          slightly faster than the normalvariate() function.
  
          Not thread-safe without a lock around calls.
  
           """
  pass

def betavariate(self, alpha, beta):
  """ Beta distribution.
  
          Conditions on the parameters are alpha > 0 and beta > 0.
          Returned values range between 0 and 1.
  
           """
  pass

def paretovariate(self, alpha):
  """ Pareto distribution.  alpha is the shape parameter. """
  pass

def weibullvariate(self, alpha, beta):
  """ Weibull distribution.
  
          alpha is the scale parameter and beta is the shape parameter.
  
           """
  pass

def getstate(self):
  """ Return internal state; can be passed to setstate() later. """
  pass

def setstate(self, state):
  """ Restore internal state from object returned by getstate(). """
  pass

def jumpahead(self, n):
  """ Change the internal state to one that is likely far away
          from the current state.  This method will not be in Py3.x,
          so it is better to simply reseed.
           """
  pass

class WichmannHill(Random):

  VERSION = 1

  def _WichmannHill__whseed(self, x, y, z):
    """ Set the Wichmann-Hill seed from (x, y, z).
    
            These must be integers in the range [0, 256).
             """
    pass

  def __init__(self, x):
    """ Initialize an instance.
    
            Optional argument x controls seeding, as for Random.seed().
             """
    pass

  def _randbelow(self, n, _log, int, _maxwidth, _Method, _BuiltinMethod):
    """ Return a random int in the range [0,n)
    
            Handles the case where n has more bits than returned
            by a single call to the underlying generator.
             """
    pass

  def betavariate(self, alpha, beta):
    """ Beta distribution.
    
            Conditions on the parameters are alpha > 0 and beta > 0.
            Returned values range between 0 and 1.
    
             """
    pass

  def choice(self, seq):
    """ Choose a random element from a non-empty sequence. """
    pass

  def expovariate(self, arg0, arg1):
    """ Exponential distribution.
    
            lambd is 1.0 divided by the desired mean.  It should be
            nonzero.  (The parameter would be called "lambda", but that is
            a reserved word in Python.)  Returned values range from 0 to
            positive infinity if lambd is positive, and from negative
            infinity to 0 if lambd is negative.
    
             """
    pass

  def gammavariate(self, arg0):
    """ Gamma distribution.  Not the gamma function!
    
            Conditions on the parameters are alpha > 0 and beta > 0.
    
            The probability distribution function is:
    
                        x ** (alpha - 1) * math.exp(-x / beta)
              pdf(x) =  --------------------------------------
                          math.gamma(alpha) * beta ** alpha
    
             """
    pass

  def gauss(self, mu, sigma):
    """ Gaussian distribution.
    
            mu is the mean, and sigma is the standard deviation.  This is
            slightly faster than the normalvariate() function.
    
            Not thread-safe without a lock around calls.
    
             """
    pass

  def getstate(self):
    """ Return internal state; can be passed to setstate() later. """
    pass

  def jumpahead(self, n):
    """ Act as if n calls to random() were made, but quickly.
    
            n is an int, greater than or equal to 0.
    
            Example use:  If you have 2 threads and know that each will
            consume no more than a million random numbers, create two Random
            objects r1 and r2, then do
                r2.setstate(r1.getstate())
                r2.jumpahead(1000000)
            Then r1 and r2 will use guaranteed-disjoint segments of the full
            period.
             """
    pass

  def lognormvariate(self, mu, sigma):
    """ Log normal distribution.
    
            If you take the natural logarithm of this distribution, you'll get a
            normal distribution with mean mu and standard deviation sigma.
            mu can have any value, and sigma must be greater than zero.
    
             """
    pass

  def normalvariate(self, mu, sigma):
    """ Normal distribution.
    
            mu is the mean, and sigma is the standard deviation.
    
             """
    pass

  def paretovariate(self, alpha):
    """ Pareto distribution.  alpha is the shape parameter. """
    pass

  def randint(self, a, b):
    """ Return random integer in range [a, b], including both end points.
             """
    pass

  def random(self):
    """ Get the next random number in the range [0.0, 1.0). """
    pass

  def randrange(self, start, stop, step=None):
    """ Choose a random item from range(start, stop[, step]).
    
            This fixes the problem with randint() which includes the
            endpoint; in Python this is usually not what you want.
            Do not supply the 'int', 'default', and 'maxwidth' arguments.
             """
    pass

  def sample(self, arg0):
    """ Chooses k unique random elements from a population sequence.
    
            Returns a new list containing elements from the population while
            leaving the original population unchanged.  The resulting list is
            in selection order so that all sub-slices will also be valid random
            samples.  This allows raffle winners (the sample) to be partitioned
            into grand prize and second place winners (the subslices).
    
            Members of the population need not be hashable or unique.  If the
            population contains repeats, then each occurrence is a possible
            selection in the sample.
    
            To choose a sample in a range of integers, use xrange as an argument.
            This is especially fast and space efficient for sampling from a
            large population:   sample(xrange(10000000), 60)
             """
    pass

  def seed(self, a):
    """ Initialize internal state from hashable object.
    
            None or no argument seeds from current time or from an operating
            system specific randomness source if available.
    
            If a is not None or an int or long, hash(a) is used instead.
    
            If a is an int or long, a is used directly.  Distinct values between
            0 and 27814431486575L inclusive are guaranteed to yield distinct
            internal states (this guarantee is specific to the default
            Wichmann-Hill generator).
             """
    pass

  def setstate(self, state):
    """ Restore internal state from object returned by getstate(). """
    pass

  def shuffle(self, x, random=random.random):
    """ x, random=random.random -> shuffle list x in place; return None.
    
            Optional arg random is a 0-argument function returning a random
            float in [0.0, 1.0); by default, the standard random.random.
             """
    return []

  def triangular(self, low, high, mode):
    """ Triangular distribution.
    
            Continuous distribution bounded by given lower and upper limits,
            and having a given mode value in-between.
    
            http://en.wikipedia.org/wiki/Triangular_distribution
    
             """
    pass

  def uniform(self, a, b):
    """ Get a random number in the range [a, b) or [a, b] depending on rounding. """
    pass

  def vonmisesvariate(self, mu, kappa):
    """ Circular data distribution.
    
            mu is the mean angle, expressed in radians between 0 and 2*pi, and
            kappa is the concentration parameter, which must be greater than or
            equal to zero.  If kappa is equal to zero, this distribution reduces
            to a uniform random angle over the range 0 to 2*pi.
    
             """
    pass

  def weibullvariate(self, alpha, beta):
    """ Weibull distribution.
    
            alpha is the scale parameter and beta is the shape parameter.
    
             """
    pass

  def whseed(self, a):
    """ Seed from hashable object's hash code.
    
            None or no argument seeds from current time.  It is not guaranteed
            that objects with distinct hash codes lead to distinct internal
            states.
    
            This is obsolete, provided for compatibility with the seed routine
            used prior to Python 2.1.  Use the .seed() method instead.
             """
    pass

def getrandbits(k):
  """ getrandbits(k) -> x.  Generates a long int with k random bits. """
  return 1

class SystemRandom(Random):
  """ Alternate random number generator using sources provided
      by the operating system (such as /dev/urandom on Unix or
      CryptGenRandom on Windows).
  
       Not available on all systems (see os.urandom() for details).
       """

  VERSION = 3

  def __init__(self, arg0):
    """ Initialize an instance.
    
            Optional argument x controls seeding, as for Random.seed().
             """
    pass

  def _notimplemented(self):
    """ Method should not be called for a system random number generator. """
    pass

  def _randbelow(self, n, _log, int, _maxwidth, _Method, _BuiltinMethod):
    """ Return a random int in the range [0,n)
    
            Handles the case where n has more bits than returned
            by a single call to the underlying generator.
             """
    pass

  def _stub(self):
    """ Stub method.  Not used for a system random number generator. """
    pass

  def betavariate(self, alpha, beta):
    """ Beta distribution.
    
            Conditions on the parameters are alpha > 0 and beta > 0.
            Returned values range between 0 and 1.
    
             """
    pass

  def choice(self, seq):
    """ Choose a random element from a non-empty sequence. """
    pass

  def expovariate(self, arg0, arg1):
    """ Exponential distribution.
    
            lambd is 1.0 divided by the desired mean.  It should be
            nonzero.  (The parameter would be called "lambda", but that is
            a reserved word in Python.)  Returned values range from 0 to
            positive infinity if lambd is positive, and from negative
            infinity to 0 if lambd is negative.
    
             """
    pass

  def gammavariate(self, arg0):
    """ Gamma distribution.  Not the gamma function!
    
            Conditions on the parameters are alpha > 0 and beta > 0.
    
            The probability distribution function is:
    
                        x ** (alpha - 1) * math.exp(-x / beta)
              pdf(x) =  --------------------------------------
                          math.gamma(alpha) * beta ** alpha
    
             """
    pass

  def gauss(self, mu, sigma):
    """ Gaussian distribution.
    
            mu is the mean, and sigma is the standard deviation.  This is
            slightly faster than the normalvariate() function.
    
            Not thread-safe without a lock around calls.
    
             """
    pass

  def getrandbits(self, k):
    """ getrandbits(k) -> x.  Generates a long int with k random bits. """
    return 1

  def getstate(self):
    """ Method should not be called for a system random number generator. """
    pass

  def jumpahead(self):
    """ Stub method.  Not used for a system random number generator. """
    pass

  def lognormvariate(self, mu, sigma):
    """ Log normal distribution.
    
            If you take the natural logarithm of this distribution, you'll get a
            normal distribution with mean mu and standard deviation sigma.
            mu can have any value, and sigma must be greater than zero.
    
             """
    pass

  def normalvariate(self, mu, sigma):
    """ Normal distribution.
    
            mu is the mean, and sigma is the standard deviation.
    
             """
    pass

  def paretovariate(self, alpha):
    """ Pareto distribution.  alpha is the shape parameter. """
    pass

  def randint(self, a, b):
    """ Return random integer in range [a, b], including both end points.
             """
    pass

  def random(self):
    """ Get the next random number in the range [0.0, 1.0). """
    pass

  def randrange(self, start, stop, step=None):
    """ Choose a random item from range(start, stop[, step]).
    
            This fixes the problem with randint() which includes the
            endpoint; in Python this is usually not what you want.
            Do not supply the 'int', 'default', and 'maxwidth' arguments.
             """
    pass

  def sample(self, arg0):
    """ Chooses k unique random elements from a population sequence.
    
            Returns a new list containing elements from the population while
            leaving the original population unchanged.  The resulting list is
            in selection order so that all sub-slices will also be valid random
            samples.  This allows raffle winners (the sample) to be partitioned
            into grand prize and second place winners (the subslices).
    
            Members of the population need not be hashable or unique.  If the
            population contains repeats, then each occurrence is a possible
            selection in the sample.
    
            To choose a sample in a range of integers, use xrange as an argument.
            This is especially fast and space efficient for sampling from a
            large population:   sample(xrange(10000000), 60)
             """
    pass

  def seed(self):
    """ Stub method.  Not used for a system random number generator. """
    pass

  def setstate(self):
    """ Method should not be called for a system random number generator. """
    pass

  def shuffle(self, x, random=random.random):
    """ x, random=random.random -> shuffle list x in place; return None.
    
            Optional arg random is a 0-argument function returning a random
            float in [0.0, 1.0); by default, the standard random.random.
             """
    return []

  def triangular(self, low, high, mode):
    """ Triangular distribution.
    
            Continuous distribution bounded by given lower and upper limits,
            and having a given mode value in-between.
    
            http://en.wikipedia.org/wiki/Triangular_distribution
    
             """
    pass

  def uniform(self, a, b):
    """ Get a random number in the range [a, b) or [a, b] depending on rounding. """
    pass

  def vonmisesvariate(self, mu, kappa):
    """ Circular data distribution.
    
            mu is the mean angle, expressed in radians between 0 and 2*pi, and
            kappa is the concentration parameter, which must be greater than or
            equal to zero.  If kappa is equal to zero, this distribution reduces
            to a uniform random angle over the range 0 to 2*pi.
    
             """
    pass

  def weibullvariate(self, alpha, beta):
    """ Weibull distribution.
    
            alpha is the scale parameter and beta is the shape parameter.
    
             """
    pass

