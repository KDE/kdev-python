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
	
	
	def __init__(self, ):
		pass
	
	def choose_boundary(self, ):
		"""
		Return a unique string that has a high likelihood of being usable as a part
		boundary.  The string has the form ``'hostipaddr.uid.pid.timestamp.random'``.
		
		
		"""
		pass
		
	def decode(self, input,output,encoding):
		"""
		Read data encoded using the allowed MIME *encoding* from open file object
		*input* and write the decoded data to open file object *output*.  Valid values
		for *encoding* include ``'base64'``, ``'quoted-printable'``, ``'uuencode'``,
		``'x-uuencode'``, ``'uue'``, ``'x-uue'``, ``'7bit'``, and  ``'8bit'``.  Decoding
		messages encoded in ``'7bit'`` or ``'8bit'`` has no effect.  The input is simply
		copied to the output.
		
		
		"""
		pass
		
	def encode(self, input,output,encoding):
		"""
		Read data from open file object *input* and write it encoded using the allowed
		MIME *encoding* to open file object *output*. Valid values for *encoding* are
		the same as for :meth:`decode`.
		
		
		"""
		pass
		
	def copyliteral(self, input,output):
		"""
		Read lines from open file *input* until EOF and write them to open file
		*output*.
		
		
		"""
		pass
		
	def copybinary(self, input,output):
		"""
		Read blocks until EOF from open file *input* and write them to open file
		*output*.  The block size is currently fixed at 8192.
		
		
		"""
		pass
		
	def getplist(self, ):
		"""
		Return the parameter list of the :mailheader:`Content-Type` header. This is a
		list of strings.  For parameters of the form ``key=value``, *key* is converted
		to lower case but *value* is not.  For example, if the message contains the
		header ``Content-type: text/html; spam=1; Spam=2; Spam`` then :meth:`getplist`
		will return the Python list ``['spam=1', 'spam=2', 'Spam']``.
		
		
		"""
		pass
		
	def getparam(self, name):
		"""
		Return the *value* of the first parameter (as returned by :meth:`getplist`) of
		the form ``name=value`` for the given *name*.  If *value* is surrounded by
		quotes of the form '``<``*more\ ``>``' or '``"``*more\ ``"``', these are removed.
		
		
		"""
		pass
		
	def getencoding(self, ):
		"""
		Return the encoding specified in the :mailheader:`Content-Transfer-Encoding`
		message header.  If no such header exists, return ``'7bit'``.  The encoding is
		converted to lower case.
		
		
		"""
		pass
		
	def gettype(self, ):
		"""
		Return the message type (of the form ``type/subtype``) as specified in the
		:mailheader:`Content-Type` header.  If no such header exists, return
		``'text/plain'``.  The type is converted to lower case.
		
		
		"""
		pass
		
	def getmaintype(self, ):
		"""
		Return the main type as specified in the :mailheader:`Content-Type` header.  If
		no such header exists, return ``'text'``.  The main type is converted to lower
		case.
		
		
		"""
		pass
		
	


