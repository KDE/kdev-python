#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
""":synopsis: Encode and decode files using the MIME quoted-printable encoding.


"""
def decode(input,output,header):
	"""
	Decode the contents of the *input* file and write the resulting decoded binary
	data to the *output* file. *input* and *output* must either be file objects or
	objects that mimic the file object interface. *input* will be read until
	``input.readline()`` returns an empty string. If the optional argument *header*
	is present and true, underscore will be decoded as space. This is used to decode
	"Q"-encoded headers as described in :rfc:`1522`: "MIME (Multipurpose Internet
	Mail Extensions) Part Two: Message Header Extensions for Non-ASCII Text".
	
	
	"""
	pass
	
def encode(input,output,quotetabs):
	"""
	Encode the contents of the *input* file and write the resulting quoted-printable
	data to the *output* file. *input* and *output* must either be file objects or
	objects that mimic the file object interface. *input* will be read until
	``input.readline()`` returns an empty string. *quotetabs* is a flag which
	controls whether to encode embedded spaces and tabs; when true it encodes such
	embedded whitespace, and when false it leaves them unencoded.  Note that spaces
	and tabs appearing at the end of lines are always encoded, as per :rfc:`1521`.
	
	
	"""
	pass
	
def decodestring(s,header):
	"""
	Like :func:`decode`, except that it accepts a source string and returns the
	corresponding decoded string.
	
	
	"""
	pass
	
def encodestring(s,quotetabs):
	"""
	Like :func:`encode`, except that it accepts a source string and returns the
	corresponding encoded string.  *quotetabs* is optional (defaulting to 0), and is
	passed straight through to :func:`encode`.
	
	
	"""
	pass
	
