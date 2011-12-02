# This file denotes the built-in python API. It is imported into every file which is parsed.
class Exception:
	pass

@TypeContainer
class __kdevpythondocumentation_builtin_list():
    @addsTypeOfArg(2)
    def __setitem__(self, key, value): pass
    @getsType
    def __getitem__(self, key): pass
    @addsTypeOfArg(1)
    def append(self,obj): pass
    @addsTypeOfArgContent(1)
    def extend(self,obj): return []
    @addsTypeOfArg(1)
    def insert(self,i, x): return None
    @getsType
    def pop(self,i): return None
    @getsType
    def index(self,x): return 0
    def count(self,x): return 0
    def sort(self,): return self
    def reverse(self,): return self
    def remove(self, x): pass

class __kdevpythondocumentation_builtin_fileObject():
    def close(self,): return None
    def flush(self,): return None
    def fileno(self,): return None
    def isatty(self,): return True
    def next(self,): return None
    def read(self,size = 0): return ""
    def readline(self,size = 0): return ""
    def readlines(self,sizehint = 0): return ""
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
    
@TypeContainer
class __kdevpythondocumentation_builtin_dict():
    @addsTypeOfArg(2)
    @addsKeyTypeOfArg(1)
    def __setitem__(self, key, value): pass
    @getsType
    def __getitem__(self, key): pass
    def clear(self,): return None
    def copy(self,): return {}
    @addsKeyTypeOfArgContent(1)
    @addsTypeOfArg(2)
    def fromkeys(self,seq, value = None): return {}
    @getsType
    def get(self,key, default = ""): return None
    def has_key(self,key): return True
    def items(self,): return [(self,)]
    @getsListOfBoth
    def iteritems(self,): return __kdevpythondocumentation_builtin_iterator
    @getsListOfKeys
    def iterkeys(self,): return __kdevpythondocumentation_builtin_iterator
    @getsList
    def itervalues(self,): return __kdevpythondocumentation_builtin_iterator
    @getsListOfKeys
    def keys(self,): return []
    @getsType
    def pop(self,key, default = ""): return None
    @getsBoth
    def popitem(self,): return None
    def setdefault(self,key, default = ""): return None
    def update(self,other = None): return None
    @getsList
    def values(self,): return []
    def viewitems(self,): return None
    def viewkeys(self,): return None
    def viewvalues(self,): return None
    

class __kdevpythondocumentation_builtin_string():
    def replace(self,before, after): return ""
    def capitalize(self,): return ""
    def center(self,width, fillchar = None): return ""
    def count(self,substring, start = 0, end = 0): return 0
    def decode(self,encoding = None, errors = None): return ""
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
    def partition(self,seperator): return (self,"", "", "")
    def replace(self,old, new, count = 0): return ""
    def rfind(self,substring, start = 0, end = 0): return 0
    def rindex(self,substring, start = 0, end = 0): return 0
    def rjust(self,width, fillchar = ""): return ""
    def rpartition(self,seperator): return (self,"", "", "")
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
    
class __kdevpythondocumentation_builtin_float():
    def bit_length(self,): return 0
    def as_integer_ration(self,): return (self,0, 0)
    def is_integer(self,): return True
    def hex(self,): return 0x0
    def fromhex(self,s): return 0

class __kdevpythondocumentation_builtin_int():
    pass

class __kdevpythondocumentation_builtin_complex():
    pass

class BaseException():
    args = ()

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

@IndexedTypeContainer
class __kdevpythondocumentation_builtin_tuple(self,):
    pass

def abs(x): return 0
def int(x): return 0
def all(iterable): return True
def any(iterable): return True
def bin(x): return ""
def bool(x = False): return True
def bytearray(source = None, encoding = None, errors = None): return []
def callable(object): return True
def chr(i): return ""
def classmethod(function): return None
def cmp(x, y): return 0
def compile(source, filename, mode, flags = None, dont_inherit = None): return None
def complex(real = 0, imag = 0): return __kdevpythondocumentation_builtin_complex()
def delattr(obj, name): return None
def dir(obj = None): return {"string" : None}
def divmod(a, b): return 0
def enumerate(sequence, start = 0): return [(0, 0)]
def eval(expression, glob = None, loc = None): return None
def execfile(filename, glob = None, loc = None): return None
def file(filename, mode = None, bufsize = None): return None
def filter(function, iterable): return []
def float(x = 0): return 0.0
def format(value, format_spec = None): return ""
def frozenset(iterable = None): return ()
def getattr(obj, name, default = None): return None
def globals(): return {}
def hasattr(obj, name): return bool
def hash(obj): return 0
def hex(x): return 0x0
def id(obj): return 0
def input(prompt = None): return None
def isinstance(obj, cls): return True
def issubclass(cls, info): return True
def iter(o, s = None): return __kdevpythondocumentation_builtin_iterator()
def len(s): return 0
def list(i = None): return []
def locals(): return {}
def long(x = None, base = None): return 0L
def map(func, iterab): return []
def max(lst, args = None, key = None): return 0
def memoryview(obj): return None
def min(lst, default = None): return 0
def next(iterator, default = None): return iterator[0]
def object(): return None
def oct(x): return 0o0
def open(filename, mode = None, bufsize = None): return __kdevpythondocumentation_builtin_fileObject()
def ord(c): return 0
def pow(x, y, z = 0): return 0.0
def property(fget = 0, fset = 0, fdel = 0, doc = 0): return 0
def range(start = 0, stop = 0, step = 0): return [0]
def raw_input(prompt = ""): return ""
def reduce(function, iterable, init = None): return None
def reload(module) : return None
def repr(object): return ""
def reversed(seq): return __kdevpythondocumentation_builtin_iterator()
def round(x, n=0): return 0.0
def set(iterable = None): return ( )
def setattr(obj, name, value): return None
def slice(start = 0, stop = 0, step = 0): return __kdevpythondocumentation_builtin_sliceObject()
def sorted(iterable, cmpre = None, key = None, reverse = False): return []
def staticmethod(function): return function
def str(obj = None): return ""
def sum(iterable): return 0.0
def super(_type, obj = None): return None
def tuple(iterable = None): return ()
def type(object): return  __kdevpythondocumentation_builtin_typeObject()
def unichr(i): return ""
def unicode(obj = None, encoding = None, errors = None): return ""
def vars(obj): return None
def xrange(start = 0, stop = 0, step = 0): return [0]
def zip(iterable = None): return []
def __import__(name, globa = None, loca = None, fromlist = None, level = 0): return None

dict = __kdevpythondocumentation_builtin_dict
