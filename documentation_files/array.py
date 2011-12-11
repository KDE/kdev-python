# AUTO-GENERATED FILE -- DO NOT EDIT

""" This module defines an object type which can efficiently represent
an array of basic values: characters, integers, floating point
numbers.  Arrays are sequence types and behave very much like lists,
except that the type of objects stored in them is constrained.  The
type is specified at object creation time by using a type code, which
is a single character.  The following type codes are defined:

    Type code   C Type             Minimum size in bytes 
    'c'         character          1 
    'b'         signed integer     1 
    'B'         unsigned integer   1 
    'u'         Unicode character  2 
    'h'         signed integer     2 
    'H'         unsigned integer   2 
    'i'         signed integer     2 
    'I'         unsigned integer   2 
    'l'         signed integer     4 
    'L'         unsigned integer   4 
    'f'         floating point     4 
    'd'         floating point     8 

The constructor is:

array(typecode [, initializer]) -- create a new array
 """

ArrayType = array
__package__ = None

class array(object):
  """ array(typecode [, initializer]) -> array
  
  Return a new array whose items are restricted by typecode, and
  initialized from the optional initializer value, which must be a list,
  string. or iterable over elements of the appropriate type.
  
  Arrays represent basic values and behave very much like lists, except
  the type of objects stored in them is constrained.
  
  Methods:
  
  append() -- append a new item to the end of the array
  buffer_info() -- return information giving the current memory info
  byteswap() -- byteswap all the items of the array
  count() -- return number of occurrences of an object
  extend() -- extend array by appending multiple elements from an iterable
  fromfile() -- read items from a file object
  fromlist() -- append items from the list
  fromstring() -- append items from the string
  index() -- return index of first occurrence of an object
  insert() -- insert a new item into the array at a provided position
  pop() -- remove and return item (default last)
  read() -- DEPRECATED, use fromfile()
  remove() -- remove first occurrence of an object
  reverse() -- reverse the order of the items in the array
  tofile() -- write all items to a file object
  tolist() -- return the array converted to an ordinary list
  tostring() -- return the array converted to a string
  write() -- DEPRECATED, use tofile()
  
  Attributes:
  
  typecode -- the typecode character used to create the array
  itemsize -- the length in bytes of one array item
   """

  def append(self, x):
    """ append(x)
    
    Append new value x to the end of the array. """
    pass

  def buffer_info(self):
    """ buffer_info() -> (address, length)
    
    Return a tuple (address, length) giving the current memory address and
    the length in items of the buffer used to hold array's contents
    The length should be multiplied by the itemsize attribute to calculate
    the buffer length in bytes. """
    return (None, None)

  def byteswap(self):
    """ byteswap()
    
    Byteswap all items of the array.  If the items in the array are not 1, 2,
    4, or 8 bytes in size, RuntimeError is raised. """
    pass

  def count(self, x):
    """ count(x)
    
    Return number of occurrences of x in the array. """
    pass

  def extend(self, arg0):
    """ extend(array or iterable)
    
     Append items to the end of the array. """
    pass

  def fromfile(self, f, n):
    """ fromfile(f, n)
    
    Read n objects from the file object f and append them to the end of the
    array.  Also called as read. """
    pass

  def fromlist(self, list):
    """ fromlist(list)
    
    Append items to array from list. """
    pass

  def fromstring(self, string):
    """ fromstring(string)
    
    Appends items from the string, interpreting it as an array of machine
    values,as if it had been read from a file using the fromfile() method). """
    pass

  def fromunicode(self, ustr):
    """ fromunicode(ustr)
    
    Extends this array with data from the unicode string ustr.
    The array must be a type 'u' array; otherwise a ValueError
    is raised.  Use array.fromstring(ustr.decode(...)) to
    append Unicode data to an array of some other type. """
    pass

  def index(self, x):
    """ index(x)
    
    Return index of first occurrence of x in the array. """
    pass

  def insert(self, i, x):
    """ insert(i,x)
    
    Insert a new item x into the array before position i. """
    pass

  itemsize = property(None, None, None,
                      """ the size, in bytes, of one array item """
                      )


  def pop(self, i=None):
    """ pop([i])
    
    Return the i-th element and delete it from the array. i defaults to -1. """
    pass

  def read(self, f, n):
    """ fromfile(f, n)
    
    Read n objects from the file object f and append them to the end of the
    array.  Also called as read. """
    pass

  def remove(self, x):
    """ remove(x)
    
    Remove the first occurrence of x in the array. """
    pass

  def reverse(self):
    """ reverse()
    
    Reverse the order of the items in the array. """
    pass

  def tofile(self, f):
    """ tofile(f)
    
    Write all items (as machine values) to the file object f.  Also called as
    write. """
    pass

  def tolist(self):
    """ tolist() -> list
    
    Convert array to an ordinary list with the same items. """
    return []

  def tostring(self):
    """ tostring() -> string
    
    Convert the array to an array of machine values and return the string
    representation. """
    return ""

  def tounicode(self):
    """ tounicode() -> unicode
    
    Convert the array to a unicode string.  The array must be
    a type 'u' array; otherwise a ValueError is raised.  Use
    array.tostring().decode() to obtain a unicode string from
    an array of some other type. """
    return None

  typecode = property(None, None, None,
                      """ the typecode character used to create the array """
                      )


  def write(self, f):
    """ tofile(f)
    
    Write all items (as machine values) to the file object f.  Also called as
    write. """
    pass

