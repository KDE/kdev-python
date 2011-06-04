#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
""":synopsis: RFC 3548: Base16, Base32, Base64 Data Encodings


"""
def b64encode(s,altchars):
	"""
	Encode a string use Base64.
	
	*s* is the string to encode.  Optional *altchars* must be a string of at least
	length 2 (additional characters are ignored) which specifies an alternative
	alphabet for the ``+`` and ``/`` characters.  This allows an application to e.g.
	generate URL or filesystem safe Base64 strings.  The default is ``None``, for
	which the standard Base64 alphabet is used.
	
	The encoded string is returned.
	
	
	"""
	pass
	
def b64decode(s,altchars):
	"""
	Decode a Base64 encoded string.
	
	*s* is the string to decode.  Optional *altchars* must be a string of at least
	length 2 (additional characters are ignored) which specifies the alternative
	alphabet used instead of the ``+`` and ``/`` characters.
	
	The decoded string is returned.  A :exc:`TypeError` is raised if *s* were
	incorrectly padded or if there are non-alphabet characters present in the
	string.
	
	
	"""
	pass
	
def standard_b64encode(s):
	"""
	Encode string *s* using the standard Base64 alphabet.
	
	
	"""
	pass
	
def standard_b64decode(s):
	"""
	Decode string *s* using the standard Base64 alphabet.
	
	
	"""
	pass
	
def urlsafe_b64encode(s):
	"""
	Encode string *s* using a URL-safe alphabet, which substitutes ``-`` instead of
	``+`` and ``_`` instead of ``/`` in the standard Base64 alphabet.  The result
	can still contain ``=``.
	
	
	"""
	pass
	
def urlsafe_b64decode(s):
	"""
	Decode string *s* using a URL-safe alphabet, which substitutes ``-`` instead of
	``+`` and ``_`` instead of ``/`` in the standard Base64 alphabet.
	
	
	"""
	pass
	
def b32encode(s):
	"""
	Encode a string using Base32.  *s* is the string to encode.  The encoded string
	is returned.
	
	
	"""
	pass
	
def b32decode(s,casefold,map01):
	"""
	Decode a Base32 encoded string.
	
	*s* is the string to decode.  Optional *casefold* is a flag specifying whether a
	lowercase alphabet is acceptable as input.  For security purposes, the default
	is ``False``.
	
	:rfc:`3548` allows for optional mapping of the digit 0 (zero) to the letter O
	(oh), and for optional mapping of the digit 1 (one) to either the letter I (eye)
	or letter L (el).  The optional argument *map01* when not ``None``, specifies
	which letter the digit 1 should be mapped to (when *map01* is not ``None``, the
	digit 0 is always mapped to the letter O).  For security purposes the default is
	``None``, so that 0 and 1 are not allowed in the input.
	
	The decoded string is returned.  A :exc:`TypeError` is raised if *s* were
	incorrectly padded or if there are non-alphabet characters present in the
	string.
	
	
	"""
	pass
	
def b16encode(s):
	"""
	Encode a string using Base16.
	
	*s* is the string to encode.  The encoded string is returned.
	
	
	"""
	pass
	
def b16decode(s,casefold):
	"""
	Decode a Base16 encoded string.
	
	*s* is the string to decode.  Optional *casefold* is a flag specifying whether a
	lowercase alphabet is acceptable as input.  For security purposes, the default
	is ``False``.
	
	The decoded string is returned.  A :exc:`TypeError` is raised if *s* were
	incorrectly padded or if there are non-alphabet characters present in the
	string.
	
	The legacy interface:
	
	
	"""
	pass
	
def decode(input,output):
	"""
	Decode the contents of the *input* file and write the resulting binary data to
	the *output* file. *input* and *output* must either be file objects or objects
	that mimic the file object interface. *input* will be read until
	``input.read()`` returns an empty string.
	
	
	"""
	pass
	
def decodestring(s):
	"""
	Decode the string *s*, which must contain one or more lines of base64 encoded
	data, and return a string containing the resulting binary data.
	
	
	"""
	pass
	
def encode(input,output):
	"""
	Encode the contents of the *input* file and write the resulting base64 encoded
	data to the *output* file. *input* and *output* must either be file objects or
	objects that mimic the file object interface. *input* will be read until
	``input.read()`` returns an empty string.  :func:`encode` returns the encoded
	data plus a trailing newline character (``'\n'``).
	
	
	"""
	pass
	
def encodestring(s):
	"""
	Encode the string *s*, which can contain arbitrary binary data, and return a
	string containing one or more lines of base64-encoded data.
	:func:`encodestring` returns a string containing one or more lines of
	base64-encoded data always including an extra trailing newline (``'\n'``).
	
	An example usage of the module:
	
	>>> import base64
	>>> encoded = base64.b64encode('data to be encoded')
	>>> encoded
	'ZGF0YSB0byBiZSBlbmNvZGVk'
	>>> data = base64.b64decode(encoded)
	>>> data
	'data to be encoded'
	
	
	"""
	pass
	
