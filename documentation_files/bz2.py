# AUTO-GENERATED FILE -- DO NOT EDIT

""" The python bz2 module provides a comprehensive interface for
the bz2 compression library. It implements a complete file
interface, one shot (de)compression functions, and types for
sequential (de)compression.
 """

class BZ2Compressor(object):
  """ BZ2Compressor([compresslevel=9]) -> compressor object
  
  Create a new compressor object. This object may be used to compress
  data sequentially. If you want to compress data in one shot, use the
  compress() function instead. The compresslevel parameter, if given,
  must be a number between 1 and 9.
   """

  def __init__(self, compresslevel=9):
    """ x.__init__(...) initializes x; see help(type(x)) for signature """
    return None

  def compress(self, data):
    """ compress(data) -> string
    
    Provide more data to the compressor object. It will return chunks of
    compressed data whenever possible. When you've finished providing data
    to compress, call the flush() method to finish the compression process,
    and return what is left in the internal buffers.
     """
    return ""

  def flush(self):
    """ flush() -> string
    
    Finish the compression process and return what is left in internal buffers.
    You must not use the compressor object after calling this method.
     """
    return ""

class BZ2Decompressor(object):
  """ BZ2Decompressor() -> decompressor object
  
  Create a new decompressor object. This object may be used to decompress
  data sequentially. If you want to decompress data in one shot, use the
  decompress() function instead.
   """

  def __init__(self):
    """ x.__init__(...) initializes x; see help(type(x)) for signature """
    return None

  def decompress(self, data):
    """ decompress(data) -> string
    
    Provide more data to the decompressor object. It will return chunks
    of decompressed data whenever possible. If you try to decompress data
    after the end of stream is found, EOFError will be raised. If any data
    was found after the end of stream, it'll be ignored and saved in
    unused_data attribute.
     """
    return ""

  unused_data = None

class BZ2File(object):
  """ BZ2File(name [, mode='r', buffering=0, compresslevel=9]) -> file object
  
  Open a bz2 file. The mode can be 'r' or 'w', for reading (default) or
  writing. When opened for writing, the file will be created if it doesn't
  exist, and truncated otherwise. If the buffering argument is given, 0 means
  unbuffered, and larger numbers specify the buffer size. If compresslevel
  is given, must be a number between 1 and 9.
  
  Add a 'U' to mode to open the file for input with universal newline
  support. Any line ending in the input file will be seen as a '\\n' in
  Python. Also, a file so opened gains the attribute 'newlines'; the value
  for this attribute is one of None (no newline read yet), '\\r', '\\n',
  '\\r\\n' or a tuple containing all the newline types seen. Universal
  newlines are available only when reading.
   """

  def __init__(self, name, mode='r', buffering=0, compresslevel=9):
    """ x.__init__(...) initializes x; see help(type(x)) for signature """
    return file(__file__)

  def close(self):
    """ close() -> None or (perhaps) an integer
    
    Close the file. Sets data attribute .closed to true. A closed file
    cannot be used for further I/O operations. close() may be called more
    than once without error.
     """
    return 1

  closed = property(None, None, None,
                    """ True if the file is closed """
                    )

  mode = property(None, None, None,
                  """ file mode ('r', 'w', or 'U') """
                  )

  name = property(None, None, None,
                  """ file name """
                  )

  newlines = property(None, None, None,
                      """ end-of-line convention used in this file """
                      )


  def next(self):
    """ x.next() -> the next value, or raise StopIteration """
    return None

  def read(self, size=None):
    """ read([size]) -> string
    
    Read at most size uncompressed bytes, returned as a string. If the size
    argument is negative or omitted, read until EOF is reached.
     """
    return ""

  def readline(self, size=None):
    """ readline([size]) -> string
    
    Return the next line from the file, as a string, retaining newline.
    A non-negative size argument will limit the maximum number of bytes to
    return (an incomplete line may be returned then). Return an empty
    string at EOF.
     """
    return ""

  def readlines(self, size=None):
    """ readlines([size]) -> list
    
    Call readline() repeatedly and return a list of lines read.
    The optional size argument, if given, is an approximate bound on the
    total number of bytes in the lines returned.
     """
    return []

  def seek(self, offset, whence=None):
    """ seek(offset [, whence]) -> None
    
    Move to new file position. Argument offset is a byte count. Optional
    argument whence defaults to 0 (offset from start of file, offset
    should be >= 0); other values are 1 (move relative to current position,
    positive or negative), and 2 (move relative to end of file, usually
    negative, although many platforms allow seeking beyond the end of a file).
    
    Note that seeking of bz2 files is emulated, and depending on the parameters
    the operation may be extremely slow.
     """
    return None

  softspace = None

  def tell(self):
    """ tell() -> int
    
    Return the current file position, an integer (may be a long integer).
     """
    return 1

  def write(self, data):
    """ write(data) -> None
    
    Write the 'data' string to file. Note that due to buffering, close() may
    be needed before the file on disk reflects the data written.
     """
    return None

  def writelines(self, sequence_of_strings):
    """ writelines(sequence_of_strings) -> None
    
    Write the sequence of strings to the file. Note that newlines are not
    added. The sequence can be any iterable object producing strings. This is
    equivalent to calling write() for each string.
     """
    return None

  def xreadlines(self):
    """ xreadlines() -> self
    
    For backward compatibility. BZ2File objects now include the performance
    optimizations previously implemented in the xreadlines module.
     """
    return None

__author__ = """The bz2 python module was written by:

    Gustavo Niemeyer <niemeyer@conectiva.com>
"""
__package__ = None

def compress(data, compresslevel=9):
  """ compress(data [, compresslevel=9]) -> string
  
  Compress data in one shot. If you want to compress data sequentially,
  use an instance of BZ2Compressor instead. The compresslevel parameter, if
  given, must be a number between 1 and 9.
   """
  return ""

def decompress(data):
  """ decompress(data) -> decompressed data
  
  Decompress data in one shot. If you want to decompress data sequentially,
  use an instance of BZ2Decompressor instead.
   """
  return None

