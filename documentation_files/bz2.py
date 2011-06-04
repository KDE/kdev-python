#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
""":synopsis: Interface to compression and decompression routines compatible with bzip2.
"""
class BZ2File:


	"""
	Open a bz2 file. Mode can be either ``'r'`` or ``'w'``, for reading (default)
	or writing. When opened for writing, the file will be created if it doesn't
	exist, and truncated otherwise. If *buffering* is given, ``0`` means
	unbuffered, and larger numbers specify the buffer size; the default is
	``0``. If *compresslevel* is given, it must be a number between ``1`` and
	``9``; the default is ``9``. Add a ``'U'`` to mode to open the file for input
	with universal newline support. Any line ending in the input file will be
	seen as a ``'\n'`` in Python.  Also, a file so opened gains the attribute
	:attr:`newlines`; the value for this attribute is one of ``None`` (no newline
	read yet), ``'\r'``, ``'\n'``, ``'\r\n'`` or a tuple containing all the
	newline types seen. Universal newlines are available only when
	reading. Instances support iteration in the same way as normal :class:`file`
	instances.
	
	:class:`BZ2File` supports the :keyword:`with` statement.
	
	"""
	
	
	def __init__(self, filename,mode,buffering,compresslevel):
		pass
	
	


class BZ2Compressor:


	"""
	Create a new compressor object. This object may be used to compress data
	sequentially. If you want to compress data in one shot, use the
	:func:`compress` function instead. The *compresslevel* parameter, if given,
	must be a number between ``1`` and ``9``; the default is ``9``.
	
	
	"""
	
	
	def __init__(self, compresslevel):
		pass
	
	


class BZ2Decompressor:


	"""
	Create a new decompressor object. This object may be used to decompress data
	sequentially. If you want to decompress data in one shot, use the
	:func:`decompress` function instead.
	
	
	"""
	
	
	def __init__(self, ):
		pass
	
	def compress(data,compresslevel):
		"""
		Compress *data* in one shot. If you want to compress data sequentially, use
		an instance of :class:`BZ2Compressor` instead. The *compresslevel* parameter,
		if given, must be a number between ``1`` and ``9``; the default is ``9``.
		
		
		"""
		pass
		
	


