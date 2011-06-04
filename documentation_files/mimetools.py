#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
""":synopsis: Tools for parsing MIME-style message bodies.
:deprecated:


"""
class Message:


	"""
	Return a new instance of the :class:`Message` class.  This is a subclass of the
	:class:`rfc822.Message` class, with some additional methods (see below).  The
	*seekable* argument has the same meaning as for :class:`rfc822.Message`.
	
	
	"""
	
	
	def __init__(self, fp,seekable):
		pass
	
	def choose_boundary():
		"""
		Return a unique string that has a high likelihood of being usable as a part
		boundary.  The string has the form ``'hostipaddr.uid.pid.timestamp.random'``.
		
		
		"""
		pass
		
	def decode(input,output,encoding):
		"""
		Read data encoded using the allowed MIME *encoding* from open file object
		*input* and write the decoded data to open file object *output*.  Valid values
		for *encoding* include ``'base64'``, ``'quoted-printable'``, ``'uuencode'``,
		``'x-uuencode'``, ``'uue'``, ``'x-uue'``, ``'7bit'``, and  ``'8bit'``.  Decoding
		messages encoded in ``'7bit'`` or ``'8bit'`` has no effect.  The input is simply
		copied to the output.
		
		
		"""
		pass
		
	def encode(input,output,encoding):
		"""
		Read data from open file object *input* and write it encoded using the allowed
		MIME *encoding* to open file object *output*. Valid values for *encoding* are
		the same as for :meth:`decode`.
		
		
		"""
		pass
		
	def copyliteral(input,output):
		"""
		Read lines from open file *input* until EOF and write them to open file
		*output*.
		
		
		"""
		pass
		
	def copybinary(input,output):
		"""
		Read blocks until EOF from open file *input* and write them to open file
		*output*.  The block size is currently fixed at 8192.
		
		
		"""
		pass
		
	


