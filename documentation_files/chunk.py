#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
""":synopsis: Module to read IFF chunks.
"""
class Chunk:


	"""
	Class which represents a chunk.  The *file* argument is expected to be a
	file-like object.  An instance of this class is specifically allowed.  The
	only method that is needed is :meth:`read`.  If the methods :meth:`seek` and
	:meth:`tell` are present and don't raise an exception, they are also used.
	If these methods are present and raise an exception, they are expected to not
	have altered the object.  If the optional argument *align* is true, chunks
	are assumed to be aligned on 2-byte boundaries.  If *align* is false, no
	alignment is assumed.  The default value is true.  If the optional argument
	*bigendian* is false, the chunk size is assumed to be in little-endian order.
	This is needed for WAVE audio files. The default value is true.  If the
	optional argument *inclheader* is true, the size given in the chunk header
	includes the size of the header.  The default value is false.
	
	A :class:`Chunk` object supports the following methods:
	
	
	"""
	
	
	def __init__(self, ):
		pass
	
	def getname(self, ):
		"""
		Returns the name (ID) of the chunk.  This is the first 4 bytes of the
		chunk.
		
		
		"""
		pass
		
	def getsize(self, ):
		"""
		Returns the size of the chunk.
		
		
		"""
		pass
		
	def close(self, ):
		"""
		Close and skip to the end of the chunk.  This does not close the
		underlying file.
		
		The remaining methods will raise :exc:`IOError` if called after the
		:meth:`close` method has been called.
		
		
		"""
		pass
		
	def isatty(self, ):
		"""
		Returns ``False``.
		
		
		"""
		pass
		
	def seek(self, pos,whence):
		"""
		Set the chunk's current position.  The *whence* argument is optional and
		defaults to ``0`` (absolute file positioning); other values are ``1``
		(seek relative to the current position) and ``2`` (seek relative to the
		file's end).  There is no return value. If the underlying file does not
		allow seek, only forward seeks are allowed.
		
		
		"""
		pass
		
	def tell(self, ):
		"""
		Return the current position into the chunk.
		
		
		"""
		pass
		
	def read(self, size):
		"""
		Read at most *size* bytes from the chunk (less if the read hits the end of
		the chunk before obtaining *size* bytes).  If the *size* argument is
		negative or omitted, read all data until the end of the chunk.  The bytes
		are returned as a string object.  An empty string is returned when the end
		of the chunk is encountered immediately.
		
		
		"""
		pass
		
	def skip(self, ):
		"""
		Skip to the end of the chunk.  All further calls to :meth:`read` for the
		chunk will return ``''``.  If you are not interested in the contents of
		the chunk, this method should be called so that the file points to the
		start of the next chunk.
		
		
		"""
		pass
		
	


