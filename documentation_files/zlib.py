# AUTO-GENERATED FILE -- DO NOT EDIT

""" The functions in this module allow compression and decompression using the
zlib library, which is based on GNU zip.

adler32(string[, start]) -- Compute an Adler-32 checksum.
compress(string[, level]) -- Compress string, with compression level in 1-9.
compressobj([level]) -- Return a compressor object.
crc32(string[, start]) -- Compute a CRC-32 checksum.
decompress(string,[wbits],[bufsize]) -- Decompresses a compressed string.
decompressobj([wbits]) -- Return a decompressor object.

'wbits' is window buffer size.
Compressor objects support compress() and flush() methods; decompressor
objects support decompress() and flush(). """

DEFLATED = 8
DEF_MEM_LEVEL = 8
MAX_WBITS = 15
ZLIB_VERSION = '1.2.5'
Z_BEST_COMPRESSION = 9
Z_BEST_SPEED = 1
Z_DEFAULT_COMPRESSION = -1
Z_DEFAULT_STRATEGY = 0
Z_FILTERED = 1
Z_FINISH = 4
Z_FULL_FLUSH = 3
Z_HUFFMAN_ONLY = 2
Z_NO_FLUSH = 0
Z_SYNC_FLUSH = 2
__package__ = None
__version__ = '1.0'

def adler32(string, start=None):
  """ adler32(string[, start]) -- Compute an Adler-32 checksum of string.
  
  An optional starting value can be specified.  The returned checksum is
  a signed integer. """
  return ""

def compress(string, level=None):
  """ compress(string[, level]) -- Returned compressed string.
  
  Optional arg level is the compression level, in 1-9. """
  return ""

def compressobj(level=None):
  """ compressobj([level]) -- Return a compressor object.
  
  Optional arg level is the compression level, in 1-9. """
  return None

def crc32(string, start=None):
  """ crc32(string[, start]) -- Compute a CRC-32 checksum of string.
  
  An optional starting value can be specified.  The returned checksum is
  a signed integer. """
  return ""

def decompress(string, wbits=None, bufsize=None):
  """ decompress(string[, wbits[, bufsize]]) -- Return decompressed string.
  
  Optional arg wbits is the window buffer size.  Optional arg bufsize is
  the initial output buffer size. """
  return ""

def decompressobj(wbits=None):
  """ decompressobj([wbits]) -- Return a decompressor object.
  
  Optional arg wbits is the window buffer size. """
  return None

class error(Exception):

  pass

