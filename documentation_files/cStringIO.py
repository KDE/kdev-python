# AUTO-GENERATED FILE -- DO NOT EDIT

""" A simple fast partial StringIO replacement.

This module provides a simple useful replacement for
the StringIO module that is written in C.  It does not provide the
full generality of StringIO, but it provides enough for most
applications and is especially useful in conjunction with the
pickle module.

Usage:

  from cStringIO import StringIO

  an_output_stream=StringIO()
  an_output_stream.write(some_stuff)
  ...
  value=an_output_stream.getvalue()

  an_input_stream=StringIO(a_string)
  spam=an_input_stream.readline()
  spam=an_input_stream.read(5)
  an_input_stream.seek(0)           # OK, start over
  spam=an_input_stream.read()       # and read it all
  
If someone else wants to provide a more complete implementation,
go for it. :-)  

cStringIO.c,v 1.29 1999/06/15 14:10:27 jim Exp
 """

class InputType(object):
  """ Simple type for treating strings as input file streams """

  def close(self):
    """ close(): explicitly release resources held. """
    pass

  closed = property(None, None, None,
                    """ True if the file is closed """
                    )


  def flush(self):
    """ flush(): does nothing. """
    pass

  def getvalue(self, use_pos=None):
    """ getvalue([use_pos]) -- Get the string value.
    If use_pos is specified and is a true value, then the string returned
    will include only the text up to the current file position.
     """
    return ""

  def isatty(self):
    """ isatty(): always returns 0 """
    pass

  def next(self):
    """ x.next() -> the next value, or raise StopIteration """
    return None

  def read(self, s=None):
    """ read([s]) -- Read s characters, or the rest of the string """
    return ""

  def readline(self):
    """ readline() -- Read one line """
    return None

  def readlines(self):
    """ readlines() -- Read all lines """
    return None

  def reset(self):
    """ reset() -- Reset the file position to the beginning """
    return file(__file__)

  def seek(self, position):
    """ seek(position)       -- set the current position
    seek(position, mode) -- mode 0: absolute; 1: relative; 2: relative to EOF """
    return None

  def tell(self):
    """ tell() -- get the current position. """
    return None

  def truncate(self):
    """ truncate(): truncate the file at the current position. """
    pass

class OutputType(object):
  """ Simple type for output to strings. """

  def close(self):
    """ close(): explicitly release resources held. """
    pass

  closed = property(None, None, None,
                    """ True if the file is closed """
                    )


  def flush(self):
    """ flush(): does nothing. """
    pass

  def getvalue(self, use_pos=None):
    """ getvalue([use_pos]) -- Get the string value.
    If use_pos is specified and is a true value, then the string returned
    will include only the text up to the current file position.
     """
    return ""

  def isatty(self):
    """ isatty(): always returns 0 """
    pass

  def next(self):
    """ x.next() -> the next value, or raise StopIteration """
    return None

  def read(self, s=None):
    """ read([s]) -- Read s characters, or the rest of the string """
    return ""

  def readline(self):
    """ readline() -- Read one line """
    return None

  def readlines(self):
    """ readlines() -- Read all lines """
    return None

  def reset(self):
    """ reset() -- Reset the file position to the beginning """
    return file(__file__)

  def seek(self, position):
    """ seek(position)       -- set the current position
    seek(position, mode) -- mode 0: absolute; 1: relative; 2: relative to EOF """
    return None

  softspace = None

  def tell(self):
    """ tell() -- get the current position. """
    return None

  def truncate(self):
    """ truncate(): truncate the file at the current position. """
    pass

  def write(self, s):
    """ write(s) -- Write a string to the file
    
    Note (hack:) writing None resets the buffer """
    return ""

  def writelines(self, sequence_of_strings):
    """ writelines(sequence_of_strings) -> None.  Write the strings to the file.
    
    Note that newlines are not added.  The sequence can be any iterable object
    producing strings. This is equivalent to calling write() for each string. """
    return ""

def StringIO(s=None):
  """ StringIO([s]) -- Return a StringIO-like stream for reading or writing """
  return ""

__package__ = None
cStringIO_CAPI = None

