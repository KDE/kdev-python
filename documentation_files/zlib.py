#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
""":synopsis: Low-level interface to compression and decompression routines compatible with
gzip.


For applications that require data compression, the functions in this module
allow compression and decompression, using the zlib library. The zlib library
has its own home page at http://www.zlib.net.   There are known
incompatibilities between the Python module and versions of the zlib library
earlier than 1.1.3; 1.1.3 has a security vulnerability, so we recommend using
1.1.4 or later.

zlib's functions have many options and often need to be used in a particular
order.  This documentation doesn't attempt to cover all of the permutations;
consult the zlib manual at http://www.zlib.net/manual.html for authoritative
information.

For reading and writing ``.gz`` files see the :mod:`gzip` module. For
other archive formats, see the :mod:`bz2`, :mod:`zipfile`, and
:mod:`tarfile` modules.

The available exception and functions in this module are:


"""
def adler32(data,value):
	"""
	Computes a Adler-32 checksum of *data*.  (An Adler-32 checksum is almost as
	reliable as a CRC32 but can be computed much more quickly.)  If *value* is
	present, it is used as the starting value of the checksum; otherwise, a fixed
	default value is used.  This allows computing a running checksum over the
	concatenation of several inputs.  The algorithm is not cryptographically
	strong, and should not be used for authentication or digital signatures.  Since
	the algorithm is designed for use as a checksum algorithm, it is not suitable
	for use as a general hash algorithm.
	
	This function always returns an integer object.
	
	"""
	pass
	
def compress(string,level):
	"""
	Compresses the data in *string*, returning a string contained compressed data.
	*level* is an integer from ``1`` to ``9`` controlling the level of compression;
	``1`` is fastest and produces the least compression, ``9`` is slowest and
	produces the most.  The default value is ``6``.  Raises the :exc:`error`
	exception if any error occurs.
	
	
	"""
	pass
	
def compressobj(level):
	"""
	Returns a compression object, to be used for compressing data streams that won't
	fit into memory at once.  *level* is an integer from ``1`` to ``9`` controlling
	the level of compression; ``1`` is fastest and produces the least compression,
	``9`` is slowest and produces the most.  The default value is ``6``.
	
	
	"""
	pass
	
def crc32(data,value):
	"""
	"""
	pass
	
def decompress(string,wbits,bufsize):
	"""
	Decompresses the data in *string*, returning a string containing the
	uncompressed data.  The *wbits* parameter controls the size of the window
	buffer, and is discussed further below.
	If *bufsize* is given, it is used as the initial size of the output
	buffer.  Raises the :exc:`error` exception if any error occurs.
	
	The absolute value of *wbits* is the base two logarithm of the size of the
	history buffer (the "window size") used when compressing data.  Its absolute
	value should be between 8 and 15 for the most recent versions of the zlib
	library, larger values resulting in better compression at the expense of greater
	memory usage.  When decompressing a stream, *wbits* must not be smaller
	than the size originally used to compress the stream; using a too-small
	value will result in an exception. The default value is therefore the
	highest value, 15.  When *wbits* is negative, the standard
	:program:`gzip` header is suppressed.
	
	*bufsize* is the initial size of the buffer used to hold decompressed data.  If
	more space is required, the buffer size will be increased as needed, so you
	don't have to get this value exactly right; tuning it will only save a few calls
	to :cfunc:`malloc`.  The default size is 16384.
	
	
	"""
	pass
	
def decompressobj(wbits):
	"""
	Returns a decompression object, to be used for decompressing data streams that
	won't fit into memory at once.  The *wbits* parameter controls the size of the
	window buffer.
	
	Compression objects support the following methods:
	
	
	"""
	pass
	
