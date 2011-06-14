# This file denotes the built-in python API. It is imported into every file which is parsed.
class Exception:
	pass

@TypeContainer
@addsTypeOfArg("__setitem__", 1)
@getsType("__getitem__")
class __kdevpythondocumentation_builtin_list(self,):
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

class __kdevpythondocumentation_builtin_fileObject(self,):
    def close(self,): return None
    def flush(self,): return None
    def fileno(self,): return None
    def isatty(self,): return True
    def next(self,): return None
    def read(self,size = 0): return ""
    def readLine(self,size = 0): return ""
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
@addsTypeOfArg("__setitem__", 1)
@addsKeyTypeOfArg("__setitem__", 0)
@getsType("__getitem__")
class __kdevpythondocumentation_builtin_dict(self,):
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
    

class __kdevpythondocumentation_builtin_string(self,):
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
    def split(self,seperator = "", maxsplit = 0): return []
    def splitlines(self,keepends = False): return []
    def startswith(self,prefix, start = 0, end = 0): return True
    def strip(self,chars = ""): return ""
    def swapcase(self,): return ""
    def title(self,): return ""
    def translate(self,table, deletechars = ""): return ""
    def upper(self,): return ""
    def zfill(self,width): return ""
    
class __kdevpythondocumentation_builtin_float(self,):
    def bit_length(self,): return 0
    def as_integer_ration(self,): return (self,0, 0)
    def is_integer(self,): return True
    def hex(self,): return 0x0
    def fromhex(self,s): return 0

@IndexedTypeContainer
class __kdevpythondocumentation_builtin_tuple(self,):
    pass

def abs(self,x): return 0
def all(self,iterable): return True
def any(self,iterable): return True
def bin(self,x): return ""
def bool(self,x = False): return True
def bytearray(self,source = None, encoding = None, errors = None): return []
def callable(self,object): return True
def chr(self,i): return ""
def classmethod(self,function): return None
def cmp(self,x, y): return 0
def compile(self,source, filename, mode, flags = None, dont_inherit = None): return None
def complex(self,real = 0, imag = 0): return 1+3j
def delattr(self,obj, name): return None
def dict(self,arg = None): return {"string" : None}
def dir(self,obj = None): return {"string" : None}
def divmod(self,a, b): return 0
def enumerate(self,sequence, start = 0): return [(self,0, 0)]
def eval(self,expression, glob = None, loc = None): return None
def execfile(self,filename, glob = None, loc = None): return None
def file(self,filename, mode = None, bufsize = None): return None
def filter(self,function, iterable): return []
def float(self,x = 0): return 0.0
def format(self,value, format_spec = None): return ""
def frozenset(self,iterable = None): return (self,)
def getattr(self,obj, name, default = None): return None
def globals(self,): return {}
def hasattr(self,obj, name): return bool
def hash(self,obj): return 0
def hex(self,x): return 0x0
def id(self,obj): return 0
def input(self,prompt = None): return None
def isinstance(self,obj, cls): return True
def issubclass(self,cls, info): return True
def iter(self,o, s = None): return __kdevpythondocumentation_builtin_iterator(self,)
def len(self,s): return 0
def list(self,i = None): return []
def locals(self,): return {}
def long(self,x = None, base = None): return 0L
def map(self,func, iterab): return []
def max(self,lst, args = None, key = None): return 0
def memoryview(self,obj): return None
def min(self,lst, default = None): return 0
def next(self,iterator, default = None): return iterator[0]
def object(self,): return None
def oct(self,x): return 0o0
def open(self,filename, mode = None, bufsize = None): return __kdevpythondocumentation_builtin_fileObject(self,)
def ord(self,c): return 0
def pow(self,x, y, z = 0): return 0.0
def property(self,fget = 0, fset = 0, fdel = 0, doc = 0): return 0
def range(self,start = 0, stop = 0, step = 0): return []
def raw_input(self,prompt = ""): return ""
def reduce(self,function, iterable, init = None): return None
def reload(self,module) : return None
def repr(self,object): return ""
def reversed(self,seq): return __kdevpythondocumentation_builtin_iterator(self,)
def round(self,x, n=0): return 0.0
def set(self,iterable = None): return (self, )
def setattr(self,obj, name, value): return None
def slice(self,start = 0, stop = 0, step = 0): return __kdevpythondocumentation_builtin_sliceObject(self,)
def sorted(self,iterable, cmpre = None, key = None, reverse = False): return []
def staticmethod(self,function): return function
def str(self,obj = None): return ""
def sum(self,iterable): return 0.0
def super(self,_type, obj = None): return None
def tuple(self,iterable = None): return (self,)
def type(self,object): return  __kdevpythondocumentation_builtin_typeObject(self,)
def unichr(self,i): return ""
def unicode(self,obj = None, encoding = None, errors = None): return ""
def vars(self,obj): return None
def xrange(self,start = 0, stop = 0, step = 0): return []
def zip(self,iterable = None): return []
def __import__(self,name, globa = None, loca = None, fromlist = None, level = 0): return None
