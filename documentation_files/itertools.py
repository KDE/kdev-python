# AUTO-GENERATED FILE -- DO NOT EDIT

""" Functional tools for creating and using iterators.

Infinite iterators:
count([n]) --> n, n+1, n+2, ...
cycle(p) --> p0, p1, ... plast, p0, p1, ...
repeat(elem [,n]) --> elem, elem, elem, ... endlessly or up to n times

Iterators terminating on the shortest input sequence:
chain(p, q, ...) --> p0, p1, ... plast, q0, q1, ... 
compress(data, selectors) --> (d[0] if s[0]), (d[1] if s[1]), ...
dropwhile(pred, seq) --> seq[n], seq[n+1], starting when pred fails
groupby(iterable[, keyfunc]) --> sub-iterators grouped by value of keyfunc(v)
ifilter(pred, seq) --> elements of seq where pred(elem) is True
ifilterfalse(pred, seq) --> elements of seq where pred(elem) is False
islice(seq, [start,] stop [, step]) --> elements from
       seq[start:stop:step]
imap(fun, p, q, ...) --> fun(p0, q0), fun(p1, q1), ...
starmap(fun, seq) --> fun(*seq[0]), fun(*seq[1]), ...
tee(it, n=2) --> (it1, it2 , ... itn) splits one iterator into n
takewhile(pred, seq) --> seq[0], seq[1], until pred fails
izip(p, q, ...) --> (p[0], q[0]), (p[1], q[1]), ... 
izip_longest(p, q, ...) --> (p[0], q[0]), (p[1], q[1]), ... 

Combinatoric generators:
product(p, q, ... [repeat=1]) --> cartesian product
permutations(p[, r])
combinations(p, r)
combinations_with_replacement(p, r)
 """

__package__ = None

class chain(object):
  """ chain(*iterables) --> chain object
  
  Return a chain object whose .next() method returns elements from the
  first iterable until it is exhausted, then elements from the next
  iterable, until all of the iterables are exhausted. """

  def from_iterable(self, iterable):
    """ chain.from_iterable(iterable) --> chain object
    
    Alternate chain() contructor taking a single iterable argument
    that evaluates lazily. """
    return None

  def next(self):
    """ x.next() -> the next value, or raise StopIteration """
    return None

class combinations(object):
  """ combinations(iterable, r) --> combinations object
  
  Return successive r-length combinations of elements in the iterable.
  
  combinations(range(4), 3) --> (0,1,2), (0,1,3), (0,2,3), (1,2,3) """

  def next(self):
    """ x.next() -> the next value, or raise StopIteration """
    return None

class combinations_with_replacement(object):
  """ combinations_with_replacement(iterable, r) --> combinations_with_replacement object
  
  Return successive r-length combinations of elements in the iterable
  allowing individual elements to have successive repeats.
  combinations_with_replacement('ABC', 2) --> AA AB AC BB BC CC """

  def next(self):
    """ x.next() -> the next value, or raise StopIteration """
    return None

class compress(object):
  """ compress(data, selectors) --> iterator over selected data
  
  Return data elements corresponding to true selector elements.
  Forms a shorter iterator from selected data elements using the
  selectors to choose the data elements. """

  def next(self):
    """ x.next() -> the next value, or raise StopIteration """
    return None

class count(object):
  """ count(start=0, step=1) --> count object
  
  Return a count object whose .next() method returns consecutive values.
  Equivalent to:
  
      def count(firstval=0, step=1):
      x = firstval
      while 1:
          yield x
          x += step
   """

  def next(self):
    """ x.next() -> the next value, or raise StopIteration """
    return None

class cycle(object):
  """ cycle(iterable) --> cycle object
  
  Return elements from the iterable until it is exhausted.
  Then repeat the sequence indefinitely. """

  def next(self):
    """ x.next() -> the next value, or raise StopIteration """
    return None

class dropwhile(object):
  """ dropwhile(predicate, iterable) --> dropwhile object
  
  Drop items from the iterable while predicate(item) is true.
  Afterwards, return every element until the iterable is exhausted. """

  def next(self):
    """ x.next() -> the next value, or raise StopIteration """
    return None

class groupby(object):
  """ groupby(iterable[, keyfunc]) -> create an iterator which returns
  (key, sub-iterator) grouped by each value of key(value).
   """

  def next(self):
    """ x.next() -> the next value, or raise StopIteration """
    return None

class filterfalse(object):
  """ filterfalse(function or None, sequence) --> ifilterfalse object
  
  Return those items of sequence for which function(item) is false.
  If function is None, return the items that are false. """

  def next(self):
    """ x.next() -> the next value, or raise StopIteration """
    return None

class slice(object):
  """ slice(iterable, [start,] stop [, step]) --> islice object
  
  Return an iterator whose next() method returns selected values from an
  iterable.  If start is specified, will skip all preceding elements;
  otherwise, start defaults to zero.  Step defaults to one.  If
  specified as another value, step determines how many values are 
  skipped between successive calls.  Works like a slice() on a list
  but returns an iterator. """

  def next(self):
    """ x.next() -> the next value, or raise StopIteration """
    return None

class zip_longest(object):
  """ zip_longest(iter1 [,iter2 [...]], [fillvalue=None]) --> izip_longest object
  
  Return a zip_longest object whose .next() method returns a tuple where
  the i-th element comes from the i-th iterable argument.  The .next()
  method continues until the longest iterable in the argument sequence
  is exhausted and then it raises StopIteration.  When the shorter iterables
  are exhausted, the fillvalue is substituted in their place.  The fillvalue
  defaults to None or can be specified by a keyword argument.
   """

  def next(self):
    """ x.next() -> the next value, or raise StopIteration """
    return None

class permutations(object):
  """ permutations(iterable[, r]) --> permutations object
  
  Return successive r-length permutations of elements in the iterable.
  
  permutations(range(3), 2) --> (0,1), (0,2), (1,0), (1,2), (2,0), (2,1) """

  def next(self):
    """ x.next() -> the next value, or raise StopIteration """
    return None

class product(object):
  """ product(*iterables) --> product object
  
  Cartesian product of input iterables.  Equivalent to nested for-loops.
  
  For example, product(A, B) returns the same as:  ((x,y) for x in A for y in B).
  The leftmost iterators are in the outermost for-loop, so the output tuples
  cycle in a manner similar to an odometer (with the rightmost element changing
  on every iteration).
  
  To compute the product of an iterable with itself, specify the number
  of repetitions with the optional repeat keyword argument. For example,
  product(A, repeat=4) means the same as product(A, A, A, A).
  
  product('ab', range(3)) --> ('a',0) ('a',1) ('a',2) ('b',0) ('b',1) ('b',2)
  product((0,1), (0,1), (0,1)) --> (0,0,0) (0,0,1) (0,1,0) (0,1,1) (1,0,0) ... """

  def next(self):
    """ x.next() -> the next value, or raise StopIteration """
    return None

class repeat(object):
  """ repeat(object [,times]) -> create an iterator which returns the object
  for the specified number of times.  If not specified, returns the object
  endlessly. """

  def next(self):
    """ x.next() -> the next value, or raise StopIteration """
    return None

class starmap(object):
  """ starmap(function, sequence) --> starmap object
  
  Return an iterator whose values are returned from the function evaluated
  with a argument tuple taken from the given sequence. """

  def next(self):
    """ x.next() -> the next value, or raise StopIteration """
    return None

class takewhile(object):
  """ takewhile(predicate, iterable) --> takewhile object
  
  Return successive entries from an iterable as long as the 
  predicate evaluates to true for each entry. """

  def next(self):
    """ x.next() -> the next value, or raise StopIteration """
    return None

def tee(iterable, n=2):
  """ tee(iterable, n=2) --> tuple of n independent iterators. """
  return ()

