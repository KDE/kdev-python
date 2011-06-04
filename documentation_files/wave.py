#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
""":synopsis: Provide an interface to the WAV sound format.
"""
def open(file,mode):
	"""
	If *file* is a string, open the file by that name, otherwise treat it as a
	seekable file-like object.  *mode* can be any of
	
	``'r'``, ``'rb'``
	Read only mode.
	
	``'w'``, ``'wb'``
	Write only mode.
	
	Note that it does not allow read/write WAV files.
	
	A *mode* of ``'r'`` or ``'rb'`` returns a :class:`Wave_read` object, while a
	*mode* of ``'w'`` or ``'wb'`` returns a :class:`Wave_write` object.  If
	*mode* is omitted and a file-like object is passed as *file*, ``file.mode``
	is used as the default value for *mode* (the ``'b'`` flag is still added if
	necessary).
	
	If you pass in a file-like object, the wave object will not close it when its
	:meth:`close` method is called; it is the caller's responsibility to close
	the file object.
	
	
	"""
	pass
	
def openfp(file,mode):
	"""
	A synonym for :func:`.open`, maintained for backwards compatibility.
	
	
	"""
	pass
	
