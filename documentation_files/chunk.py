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
	
	
	def __init__(self, file,align,bigendian,inclheader):
		pass
	
	


