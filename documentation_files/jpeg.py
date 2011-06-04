#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
""":platform: IRIX
:synopsis: Read and write image files in compressed JPEG format.
:deprecated:

"""
def compress(data,w,h,b):
	"""
	"""
	pass
	
def decompress(data):
	"""
	"""
	pass
	
def setoption(name,value):
	"""
	Set various options.  Subsequent :func:`compress` and :func:`decompress` calls
	will use these options.  The following options are available:
	
	+-----------------+---------------------------------------------+
	| Option          | Effect                                      |
	+=================+=============================================+
	| ``'forcegray'`` | Force output to be grayscale, even if input |
	|                 | is RGB.                                     |
	+-----------------+---------------------------------------------+
	| ``'quality'``   | Set the quality of the compressed image to  |
	|                 | a value between ``0`` and ``100`` (default  |
	|                 | is ``75``).  This only affects compression. |
	+-----------------+---------------------------------------------+
	| ``'optimize'``  | Perform Huffman table optimization.  Takes  |
	|                 | longer, but results in smaller compressed   |
	|                 | image.  This only affects compression.      |
	+-----------------+---------------------------------------------+
	| ``'smooth'``    | Perform inter-block smoothing on            |
	|                 | uncompressed image.  Only useful for low-   |
	|                 | quality images.  This only affects          |
	|                 | decompression.                              |
	+-----------------+---------------------------------------------+
	
	
	"""
	pass
	
