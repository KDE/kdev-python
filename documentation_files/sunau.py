#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
""":synopsis: Provide an interface to the Sun AU sound format.
"""
"""
An integer every valid Sun AU file begins with, stored in big-endian form.  This
is the string ``.snd`` interpreted as an integer.


"""
AUDIO_FILE_MAGIC = None
"""AUDIO_FILE_ENCODING_LINEAR_8
AUDIO_FILE_ENCODING_LINEAR_16
AUDIO_FILE_ENCODING_LINEAR_24
AUDIO_FILE_ENCODING_LINEAR_32
AUDIO_FILE_ENCODING_ALAW_8

Values of the encoding field from the AU header which are supported by this
module.


"""
AUDIO_FILE_ENCODING_MULAW_8 = None
"""AUDIO_FILE_ENCODING_DOUBLE
AUDIO_FILE_ENCODING_ADPCM_G721
AUDIO_FILE_ENCODING_ADPCM_G722
AUDIO_FILE_ENCODING_ADPCM_G723_3
AUDIO_FILE_ENCODING_ADPCM_G723_5

Additional known values of the encoding field from the AU header, but which are
not supported by this module.


.. U_read Objects
---------------

AU_read objects, as returned by :func:`.open` above, have the following methods:


"""
AUDIO_FILE_ENCODING_FLOAT = None
def open(file,mode):
	"""
	If *file* is a string, open the file by that name, otherwise treat it as a
	seekable file-like object. *mode* can be any of
	
	``'r'``
	Read only mode.
	
	``'w'``
	Write only mode.
	
	Note that it does not allow read/write files.
	
	A *mode* of ``'r'`` returns a :class:`AU_read` object, while a *mode* of ``'w'``
	or ``'wb'`` returns a :class:`AU_write` object.
	
	
	"""
	pass
	
def openfp(file,mode):
	"""
	A synonym for :func:`.open`, maintained for backwards compatibility.
	
	
	The :mod:`sunau` module defines the following exception:
	
	"""
	pass
	
