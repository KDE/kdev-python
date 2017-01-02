# This file denotes the built-in python library. It is imported into every file which is parsed.
class Exception(object):
    pass

class object():
    def __init__(self): pass
    def __new__(self): pass
    def __del__(self): pass
    def __repr__(self): pass
    def __str__(self): pass
    def __lt__(self, other): pass
    def __gt__(self, other): pass
    def __le__(self, other): pass
    def __eq__(self, other): pass
    def __ne__(self, other): pass
    def __gt__(self, other): pass
    def __ge__(self, other): pass
    def __cmp__(self, other): pass
    def __hash__(self): pass
    def __nonzero__(self): pass
    def __unicode__(self): pass
    def __getattr__(self, name): pass
    def __setattr__(self, name, value): pass
    def __delattr__(self, name): pass
    def __getattribute__(self, name): pass
    def __get__(self, instance, owner): pass
    def __set__(self, instance, value): pass
    def __delete__(self, instance): pass
    def __instancecheck__(self, instance): pass
    def __subclasscheck__(self, subclass): pass
    def __call__(self): pass
    def __len__(self): pass
    def __getitem__(self, key): pass
    def __setitem__(self, key, value): pass
    def __delitem__(self, key): pass
    def __iter__(self): pass
    def __reversed__(self): pass
    def __contains__(self, item): pass
    def __getslice__(self, i, j): pass
    def __delslice__(self, i, j): pass
    def __add__(self, other): pass
    def __sub__(self, other): pass
    def __mul__(self, other): pass
    def __matmul__(self, other): pass
    def __rmatmul__(self, other): pass
    def __imatmul__(self, other): pass
    def __floordiv__(self, other): pass
    def __mod__(self, other): pass
    def __divmod__(self, other): pass
    def __pow__(self, other): pass
    def __lshift__(self, other): pass
    def __rshift__(self, other): pass
    def __and__(self, other): pass
    def __xor__(self, other): pass
    def __or__(self, other): pass
    def __div__(self, other): pass
    def __truediv__(self, other): pass
    def __radd__(self, other): pass
    def __rsub__(self, other): pass
    def __rmul__(self, other): pass
    def __rtruediv__(self, other): pass
    def __rfloordiv__(self, other): pass
    def __rmod__(self, other): pass
    def __rdivmod__(self, other): pass
    def __rpow__(self, other): pass
    def __rlshift__(self, other): pass
    def __rrshift__(self, other): pass
    def __rand__(self, other): pass
    def __rxor__(self, other): pass
    def __ror__(self, other): pass
    def __iadd__(self, other): pass
    def __isub__(self, other): pass
    def __imul__(self, other): pass
    def __idiv__(self, other): pass
    def __itruediv__(self, other): pass
    def __ifloordiv__(self, other): pass
    def __imod__(self, other): pass
    def __ipow__(self, other): pass
    def __ilshift__(self, other): pass
    def __irshift__(self, other): pass
    def __iand__(self, other): pass
    def __ixor__(self, other): pass
    def __ior__(self, other): pass
    def __neg__(self): pass
    def __pos__(self): pass
    def __abs__(self): pass
    def __invert__(self): pass
    def __complex__(self): pass
    def __int__(self): pass
    def __long__(self): pass
    def __float__(self): pass
    def __oct__(self): pass
    def __hex__(self): pass
    def __index__(self): pass
    def __coerce__(self, other): pass

    __class__ = str()

class basestring():
    pass

@TypeContainer
class list():
    """! TypeContainer !"""
    def __init__(self, items):
        """! returnContentEqualsContentOf ! 0"""
        return []
    def __setitem__(self, key, value):
        """! addsTypeOfArg ! 1
           ! getsType !"""
    def __getitem__(self, key):
        """! addsTypeOfArg ! 0"""
    def append(self,obj):
        """! addsTypeOfArg ! 0"""
    def extend(self,obj):
        """! addsTypeOfArgContent ! 0"""
        return None
    def insert(self,i, x):
        """! getsType !"""
        return None
    def pop(self,i):
        """! getsType !"""
        return None
    def index(self,x): return 0
    def count(self,x):
        """! getsList !"""
        return 0
    def sort(self,):
        """! getsList !"""
        return []
    def reverse(self,):
        """! getsList !"""
        return []
    def remove(self, x): pass

class _io_TextIOWrapper():
    def close(self,): return None
    def flush(self,): return None
    def fileno(self,): return None
    def isatty(self,): return True
    def next(self,): return None
    def read(self,size = 0): return ""
    def readline(self,size = 0): return ""
    def readlines(self,sizehint = 0): return [""]
    def xreadlines(self,): return None
    def seek(self,offset, whence = 0): return None
    def tell(self,): return None
    def truncate(self,size = 0): return None
    def write(self,string): return None
    def writelines(self,sequence): return None
    closed = True
    errors = None
    mode = None
    name = ""
    newlines = ""
    softspace = True

class dict():
    """! TypeContainer !
       ! hasTypedKeys !"""
    def __init__(self, items):
        """! returnContentEqualsContentOf ! 0"""
        return {}
    def __setitem__(self, key, value):
        """! addsTypeOfArg ! 1
           ! addsKeyTypeOfArg ! 0"""
    def __getitem__(self, key):
        """! getsType !"""
    def clear(self,): return None
    def copy(self,): return {}
    def fromkeys(self,seq, value = None):
        """! addsKeyTypeOfArgContent ! 0
           ! addsTypeOfArg ! 1"""
        return {}
    def get(self,key, default = ""):
        """! getsType !"""
        return None
    def has_key(self,key): return True
    def items(self,):
        """! getsListOfBoth !"""
        return {}
    def iteritems(self,):
        """! getsListOfBoth !"""
        return []
    def iterkeys(self,):
        """! getsListOfKeys !"""
        return []
    def itervalues(self,):
        """! getsList !"""
        return []
    def keys(self,):
        """! getsListOfKeys !"""
        return []
    def pop(self,key, default = ""):
        """! getsType !"""
        return None
    def popitem(self,):
        """! getsBoth !"""
        return None
    def setdefault(self,key, default = ""): return None
    def update(self,other = None): return None
    def values(self,):
        """! getsList !"""
        return []
    def viewitems(self,): return None
    def viewkeys(self,): return None
    def viewvalues(self,): return None
    

class str():
    def __init__(self, obj):
        pass
    def __mod__(self, modulo):
        return str()
    def __getitem__(self): return ""
    def __iter__(self): return self
    def __next__(self): return ""
    def replace(self,before, after): return ""
    def capitalize(self,): return ""
    def center(self,width, fillchar = None): return ""
    def count(self,substring, start = 0, end = 0): return 0
    def encode(self, encoding): return bytes()
    def endswith(self,suffix, start = 0, end = 0): return True
    def expandtabs(self,tabsize = 0): return ""
    def find(self,substring, start = 0, end = 0): return 0
    def format(self,*args, **kwargs): return ""
    def index(self,substring, start = 0, end = 0): return 0
    def isalnum(self,): return True
    def isalpha(self,): return True
    def isdigit(self,): return True
    def islower(self,): return True
    def isspace(self,): return True
    def istitle(self,): return True
    def isupper(self,): return True
    def join(self,iterable): return ""
    def ljust(self,width, fillchar = ""): return ""
    def lower(self,): return ""
    def lstrip(self,chars = ""): return ""
    def partition(self,seperator): return ("", "", "")
    def replace(self,old, new, count = 0): return ""
    def rfind(self,substring, start = 0, end = 0): return 0
    def rindex(self,substring, start = 0, end = 0): return 0
    def rjust(self,width, fillchar = ""): return ""
    def rpartition(self,seperator): return ("", "", "")
    def rsplit(self,seperator = "", maxsplit = 0): return []
    def rstrip(self,chars = ""): return ""
    def split(self,seperator = "", maxsplit = 0): return ["string"]
    def splitlines(self,keepends = False): return ["string"]
    def startswith(self,prefix, start = 0, end = 0): return True
    def strip(self,chars = ""): return ""
    def swapcase(self,): return ""
    def title(self,): return ""
    def translate(self,table, deletechars = ""): return ""
    def upper(self,): return ""
    def zfill(self,width): return ""

class float():
    def bit_length(self,): return 0
    def as_integer_ration(self,): return (self,0, 0)
    def is_integer(self,): return True
    def hex(self,): return 0x0
    def fromhex(self,s): return 0
    def __add__(self, other): return float()
    def __sub__(self, other): return float()
    def __mul__(self, other): return float()
    def __div__(self, other): return float()


class int():
    def __add__(self, other): return int()
    def __sub__(self, other): return int()
    def __mul__(self, other): return int()
    def __div__(self, other): return float()

class complex():
    real = 3
    imag = 5
    def __add__(self, other): return complex()
    def __sub__(self, other): return complex()
    def __mul__(self, other): return complex()
    def __div__(self, other): return complex()
    def __mod__(self, other): return complex()

class BaseException():
    args = ()

class NameError(BaseException):
    pass
class AttributeError(BaseException):
    pass
class IndexError(BaseException):
    pass
class IOError(BaseException):
    pass
class StandardError(BaseException):
    pass
class Exception(BaseException):
    pass
class StopIteration(BaseException):
    pass
class StopAsyncIteration(BaseException):
    pass
class BufferError(BaseException):
    pass
class LookupError(BaseException):
    pass
class EnvironmentError(BaseException):
    pass
class AssertionError(BaseException):
    pass
class EOFError(BaseException):
    pass
class FloatingPointError(BaseException):
    pass
class GeneratorExit(BaseException):
    pass
class ImportError(BaseException):
    pass
class KeyError(BaseException):
    pass
class MemoryError(BaseException):
    pass
class NotImplementedError(BaseException):
    pass
class OSError(BaseException):
    pass
class OverflowError(BaseException):
    pass
class ReferenceError(BaseException):
    pass
class RuntimeError(BaseException):
    pass
class StopIteration(BaseException):
    pass
class SyntaxError(BaseException):
    pass
class IndentationError(BaseException):
    pass
class TabError(BaseException):
    pass
class SystemError(BaseException):
    pass
class SystemExit(BaseException):
    pass
class TypeError(BaseException):
    pass
class UnboundLocalError(BaseException):
    pass
class UnicodeError(BaseException):
    pass
class UnicodeEncodeError(BaseException):
    pass
class UnicodeDecodeError(BaseException):
    pass
class UnicodeTranslateError(BaseException):
    pass
class ValueError(BaseException):
    pass
class ZeroDivisionError(BaseException):
    pass
class Warning():
    pass
class UserWarning(Warning):
    pass
class DeprecationWarning(Warning):
    pass
class KeyboardInterrupt(Exception):
    pass
class PendingDeprecationWarning(Warning):
    pass
class RuntimeWarning(Warning):
    pass
class FutureWarning(Warning):
    pass
class ImportWarning(Warning):
    pass
class UnicodeWarning(Warning):
    pass

class tuple():
    """! IndexedTypeContainer !"""
    def __mul__(self, other):
        return tuple()

class bytes:
    def __init__(self, data):
        pass
    def __getitem__(self, key): return int()
    def __iter__(self): return self
    def __next__(self): return int()
    def capitalize(self): return bytes()
    def center(self): return bytes()
    def count(self): return int()
    def decode(self, encoding): return str()
    def endswith(self, data): return True
    def expandtabs(self): return bytes()
    def find(self): return int()
    def fromhex(self, hexdata): return bytes()
    def index(self): return int()
    def isalnum(self): return True
    def isalpha(self): return True
    def isdigit(self): return True
    def islower(self): return True
    def isspace(self): return True
    def istitle(self): return True
    def isupper(self): return True
    def join(self, other): return bytes()
    def ljust(self, space): return bytes();
    def lower(self): return bytes()
    def lstrip(self): return bytes()
    def maketrans(self, frm, to): return bytes()
    def partition(self, separator): return (bytes(), bytes(), bytes())
    def replace(self, find, replace): return bytes()
    def rfind(self, data): return int()
    def rindex(self, data): return int()
    def rjust(self, justify): return bytes()
    def rpartition(self, separator): return (bytes(), bytes(), bytes())
    def rsplit(self, separator): return [bytes()]
    def rstrip(self): return bytes()
    def split(self, separator): return [bytes()]
    def splitlines(self): return [bytes()]
    def startswith(self): return False
    def strip(self): return bytes()
    def swapcase(self): return bytes()
    def title(self): return bytes()
    def translate(self, table, deletechars=None): return bytes()
    def upper(self): return bytes()
    def zfill(self, width): return bytes()

class set():
    """! TypeContainer !"""
    def __init__(self, iterable):
        """! returnContentEqualsContentOf ! 0"""
        pass
    def len(self): return 0
    def isdisjoint(self, other): return True
    def issubset(self, other): return True
    def issuperset(self, other): return True
    def union(self, other, *others): return set()
    def intersection(self, other, *others): return set()
    def difference(self, other, *others): return set()
    def symmetric_difference(self, other): return set()
    def copy(self): return set()
    def update(self, other): pass
    def intersection_update(self, other, *others): pass
    def difference_update(self, other, *others): pass
    def symmetric_difference_update(self, other, *others): pass
    def add(self, elem): pass
    def remove(self, elem): pass
    def discard(self, elem): pass
    def pop(self): pass
    def clear(self): pass

class frozenset():
    """! TypeContainer !"""
    def __init__(self, iterable):
        """! returnContentEqualsContentOf ! 0"""
        pass
    def len(self): return 0
    def isdisjoint(self, other): return True
    def issubset(self, other): return True
    def issuperset(self, other): return True
    def union(self, other, *others): return set()
    def intersection(self, other, *others): return set()
    def difference(self, other, *others): return set()
    def symmetric_difference(self, other): return set()
    def copy(self): return set()

def abs(x):
    """ Return the absolute value of a number. The argument may be a plain or long integer or a floating point number. If the argument is a complex number, its magnitude is returned."""
    return 0
def int(x): return 0
def all(iterable): return True

def any(iterable):
    """Return True if any element of the iterable is true. If the iterable is empty, return False."""
    return True
def bin(x):
    """Convert an integer number to a binary string. The result is a valid Python expression. If x is not a Python int object, it has to define an __index__() method that returns an integer."""
    return ""
def bool(x = False):
    """Convert a value to a Boolean, using the standard truth testing procedure. If x is false or omitted, this returns False; otherwise it returns True. bool is also a class, which is a subclass of int. Class bool cannot be subclassed further. Its only instances are False and True."""
    return True
def bytearray(source = None, encoding = None, errors = None):
    """Return a new array of bytes. The bytearray type is a mutable sequence of integers in the range 0 <= x < 256."""
    return bytes()
def callable(object):
    """Return True if the object argument appears callable, False if not. If this returns true, it is still possible that a call fails, but if it is false, calling object will never succeed. Note that classes are callable (calling a class returns a new instance); class instances are callable if they have a __call__() method."""
    return True
def chr(i):
    """Return a string of one character whose ASCII code is the integer i. For example, chr(97) returns the string 'a'. This is the inverse of ord(). The argument must be in the range [0..255], inclusive; ValueError will be raised if i is outside that range. See also unichr()."""
    return ""
def classmethod(function):
    """Return a class method for function."""
    return None
def cmp(x, y):
    """Compare the two objects x and y and return an integer according to the outcome. The return value is negative if x < y, zero if x == y and strictly positive if x > y."""
    return 0
def compile(source, filename, mode, flags = None, dont_inherit = None):
    """Compile the source into a code or AST object. Code objects can be executed by an exec statement or evaluated by a call to eval(). source can either be a Unicode string, a Latin-1 encoded string or an AST object. Refer to the ast module documentation for information on how to work with AST objects."""
    return None
def delattr(obj, name):
    """This is a relative of setattr(). The arguments are an object and a string. The string must be the name of one of the object’s attributes. The function deletes the named attribute, provided the object allows it. For example, delattr(x, 'foobar') is equivalent to del x.foobar."""
    return None
def dir(obj = None):
    """Without arguments, return the list of names in the current local scope. With an argument, attempt to return a list of valid attributes for that object."""
    return {"string" : None}
def divmod(a, b):
    """Take two (non complex) numbers as arguments and return a pair of numbers consisting of their quotient and remainder when using long division."""
    return 0
def enumerate(sequence, start = 0):
    """Return an enumerate object. sequence must be a sequence, an iterator, or some other object which supports iteration.
    ! enumerate ! 0 """
    return [(0, 0)]
def eval(expression, glob = None, loc = None):
    """The expression argument is parsed and evaluated as a Python expression (technically speaking, a condition list) using the globals and locals dictionaries as global and local namespace."""
    return None
def execfile(filename, glob = None, loc = None):
    """This function is similar to the exec statement, but parses a file instead of a string. It is different from the import statement in that it does not use the module administration — it reads the file unconditionally and does not create a new module. """
    return None
def file(filename, mode = None, bufsize = None):
    """Constructor function for the file type, described further in section File Objects."""
    return _io_TextIOWrapper()
def filter(function, iterable):
    """Construct a list from those elements of iterable for which function returns true. iterable may be either a sequence, a container which supports iteration, or an iterator. If iterable is a string or a tuple, the result also has that type; otherwise it is always a list. If function is None, the identity function is assumed, that is, all elements of iterable that are false are removed."""
    return []
def float(x = 0):
    """Convert a string or a number to floating point."""
    return 0.0
def format(value, format_spec = None):
    """Convert a value to a “formatted” representation, as controlled by format_spec."""
    return ""
def getattr(obj, name, default = None):
    """Return the value of the named attribute of object. name must be a string."""
    return None
def globals():
    """Return a dictionary representing the current global symbol table."""
    return {}
def hasattr(obj, name):
    """The arguments are an object and a string. The result is True if the string is the name of one of the object’s attributes, False if not. (This is implemented by calling getattr(object, name) and seeing whether it raises an exception or not.)"""
    return bool
def hash(obj):
    """Return the hash value of the object (if it has one)."""
    return 0
def hex(x):
    """Convert an integer number (of any size) to a hexadecimal string."""
    return 0x0
def id(obj):
    """Return the “identity” of an object. This is an integer (or long integer) which is guaranteed to be unique and constant for this object during its lifetime. Two objects with non-overlapping lifetimes may have the same id() value."""
    return 0
def input(prompt = None):
    """Equivalent to eval(raw_input(prompt))."""
    return None
def isinstance(obj, cls):
    """Return true if the object argument is an instance of the classinfo argument, or of a (direct, indirect or virtual) subclass thereof."""
    return True
def issubclass(cls, info):
    """Return true if class is a subclass (direct, indirect or virtual) of classinfo."""
    return True
def iter(o, s = None):
    """Return an iterator object.
    ! returnContentEqualsContentOf ! 0 """
    return []
def len(s):
    """Return the length (the number of items) of an object. The argument may be a sequence (string, tuple or list) or a mapping (dictionary)."""
    return 0
def locals():
    """Update and return a dictionary representing the current local symbol table.""" 
    return {}
def long(x = None, base = None):
    """Convert a string or number to a long integer."""
    return 0
def map(func, iterab):
    """Apply function to every item of iterable and return a list of the results."""
    return []
def max(lst, args = None, key = None):
    """Return the largest item in an iterable or the largest of two or more arguments."""
    return 0
def memoryview(obj):
    """Return a “memory view” object created from the given argument."""
    return None
def min(lst, default = None):
    """Return the smallest item in an iterable or the smallest of two or more arguments."""
    return 0
def next(iterator, default = None):
    """Retrieve the next item from the iterator by calling its next() method."""
    return iterator[0]
def oct(x):
    """Convert an integer number (of any size) to an octal string."""
    return 0o0
def open(filename, mode = None, bufsize = None):
    """Open a file, returning an object of the file type described in section File Objects."""
    return _io_TextIOWrapper()
def ord(c):
    """Given a string of length one, return an integer representing the Unicode code point of the character when the argument is a unicode object, or the value of the byte when the argument is an 8-bit string."""
    return 0
def pow(x, y, z = 0):
    """Return x to the power y; if z is present, return x to the power y, modulo z."""
    return 0.0
def property(fget = 0, fset = 0, fdel = 0, doc = 0):
    """Return a property attribute for new-style classes (classes that derive from object)."""
    return 0
def range(start = 0, stop = 0, step = 0):
    """This is a versatile function to create lists containing arithmetic progressions. It is most often used in for loops. The arguments must be plain integers."""
    return [0]
def raw_input(prompt = ""):
    """ The function then reads a line from input, converts it to a string (stripping a trailing newline), and returns that."""
    return ""
def reduce(function, iterable, init = None):
    """Apply function of two arguments cumulatively to the items of iterable, from left to right, so as to reduce the iterable to a single value."""
    return None
def reload(module):
    """Reload a previously imported module."""
    return None
def repr(object):
    """Return a string containing a printable representation of an object."""
    return ""
def reversed(seq):
    """Return a reverse iterator.
    ! returnContentEqualsContentOf ! 0"""
    return None
def round(x, n=0):
    """Return the floating point value number rounded to ndigits digits after the decimal point."""
    return 0.0
def setattr(obj, name, value):
    """This is the counterpart of getattr(). The arguments are an object, a string and an arbitrary value. The string may name an existing attribute or a new attribute. The function assigns the value to the attribute, provided the object allows it."""
    return None
def slice(start = 0, stop = 0, step = 0):
    """Return a slice object representing the set of indices specified by range(start, stop, step)."""
    return slice()
def sorted(iterable, cmpre = None, key = None, reverse = False):
    """Return a new sorted list from the items in iterable.
    ! returnContentEqualsContentOf ! 0"""
    return []
def staticmethod(function):
    """Return a static method for function."""
    return function
def sum(iterable):
    """Sums start and the items of an iterable from left to right and returns the total."""
    return 0.0
def super(_type, obj = None):
    """Return a proxy object that delegates method calls to a parent or sibling class of type."""
    return None
def tuple(iterable = None):
    """Return a tuple whose items are the same and in the same order as iterable‘s items."""
    return ()
def type(object):
    """With one argument, return the type of an object."""
    return object
def unichr(i):
    """Return the Unicode string of one character whose Unicode code is the integer i."""
    return ""
def unicode(obj = None, encoding = None, errors = None):
    """Return the Unicode string version of object."""
    return ""
def vars(obj):
    """Return the __dict__ attribute for a module, class, instance, or any other object with a __dict__ attribute."""
    return None
def xrange(start = 0, stop = 0, step = 0):
    """This function is very similar to range(), but returns an xrange object instead of a list."""
    return [0]
def zip(iterable = None):
    """This function returns a list of tuples, where the i-th tuple contains the i-th element from each of the argument sequences or iterables."""
    return []
def __import__(name, globa = None, loca = None, fromlist = None, level = 0):
    """This function is invoked by the import statement. It can be replaced (by importing the __builtin__ module and assigning to __builtin__.__import__) in order to change semantics of the import statement, but nowadays it is usually simpler to use import hooks (see PEP 302)."""
    return None

def exit(status): return None
__name__ = "none"
__file__ = "none"
__doc__ = "none"
__package__ = "none"
NotImplemented = None

def print(obj, sep='', end='\n', file=open()):
    pass
