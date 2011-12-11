# AUTO-GENERATED FILE -- DO NOT EDIT

""" C implementation and optimization of the Python pickle module. """

class BadPickleGet(UnpicklingError):

  pass

HIGHEST_PROTOCOL = 2

class PickleError(Exception):

  pass

def Pickler(file, protocol=0):
  """ Pickler(file, protocol=0) -- Create a pickler.
  
  This takes a file-like object for writing a pickle data stream.
  The optional proto argument tells the pickler to use the given
  protocol; supported protocols are 0, 1, 2.  The default
  protocol is 0, to be backwards compatible.  (Protocol 0 is the
  only protocol that can be written to a file opened in text
  mode and read back successfully.  When using a protocol higher
  than 0, make sure the file is opened in binary mode, both when
  pickling and unpickling.)
  
  Protocol 1 is more efficient than protocol 0; protocol 2 is
  more efficient than protocol 1.
  
  Specifying a negative protocol version selects the highest
  protocol version supported.  The higher the protocol used, the
  more recent the version of Python needed to read the pickle
  produced.
  
  The file parameter must have a write() method that accepts a single
  string argument.  It can thus be an open file object, a StringIO
  object, or any other custom object that meets this interface.
   """
  return None

class PicklingError(PickleError):

  pass

class UnpickleableError(PicklingError):

  pass

def Unpickler(file):
  """ Unpickler(file) -- Create an unpickler. """
  return None

class UnpicklingError(PickleError):

  pass

__package__ = None
__version__ = '1.71'
compatible_formats = []

def dump(obj, file, protocol=0):
  """ dump(obj, file, protocol=0) -- Write an object in pickle format to the given file.
  
  See the Pickler docstring for the meaning of optional argument proto. """
  return file(__file__)

def dumps(obj, protocol=0):
  """ dumps(obj, protocol=0) -- Return a string containing an object in pickle format.
  
  See the Pickler docstring for the meaning of optional argument proto. """
  return ""

format_version = '2.0'

def load(file):
  """ load(file) -- Load a pickle from the given file """
  return file(__file__)

def loads(string):
  """ loads(string) -- Load a pickle from the given string """
  return ""

