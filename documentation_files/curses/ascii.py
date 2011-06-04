#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
""":synopsis: Constants and set-membership functions for ASCII characters.
"""
def isalnum(c):
	"""
	Checks for an ASCII alphanumeric character; it is equivalent to ``isalpha(c) or
	isdigit(c)``.
	
	
	"""
	pass
	
def isalpha(c):
	"""
	Checks for an ASCII alphabetic character; it is equivalent to ``isupper(c) or
	islower(c)``.
	
	
	"""
	pass
	
def isascii(c):
	"""
	Checks for a character value that fits in the 7-bit ASCII set.
	
	
	"""
	pass
	
def isblank(c):
	"""
	Checks for an ASCII whitespace character.
	
	
	"""
	pass
	
def iscntrl(c):
	"""
	Checks for an ASCII control character (in the range 0x00 to 0x1f).
	
	
	"""
	pass
	
def isdigit(c):
	"""
	Checks for an ASCII decimal digit, ``'0'`` through ``'9'``.  This is equivalent
	to ``c in string.digits``.
	
	
	"""
	pass
	
def isgraph(c):
	"""
	Checks for ASCII any printable character except space.
	
	
	"""
	pass
	
def islower(c):
	"""
	Checks for an ASCII lower-case character.
	
	
	"""
	pass
	
def isprint(c):
	"""
	Checks for any ASCII printable character including space.
	
	
	"""
	pass
	
def ispunct(c):
	"""
	Checks for any printable ASCII character which is not a space or an alphanumeric
	character.
	
	
	"""
	pass
	
def isspace(c):
	"""
	Checks for ASCII white-space characters; space, line feed, carriage return, form
	feed, horizontal tab, vertical tab.
	
	
	"""
	pass
	
def isupper(c):
	"""
	Checks for an ASCII uppercase letter.
	
	
	"""
	pass
	
def isxdigit(c):
	"""
	Checks for an ASCII hexadecimal digit.  This is equivalent to ``c in
	string.hexdigits``.
	
	
	"""
	pass
	
def isctrl(c):
	"""
	Checks for an ASCII control character (ordinal values 0 to 31).
	
	
	"""
	pass
	
def ismeta(c):
	"""
	Checks for a non-ASCII character (ordinal values 0x80 and above).
	
	These functions accept either integers or strings; when the argument is a
	string, it is first converted using the built-in function :func:`ord`.
	
	Note that all these functions check ordinal bit values derived from the  first
	character of the string you pass in; they do not actually know anything about
	the host machine's character encoding.  For functions  that know about the
	character encoding (and handle internationalization properly) see the
	:mod:`string` module.
	
	The following two functions take either a single-character string or integer
	byte value; they return a value of the same type.
	
	
	"""
	pass
	
def ascii(c):
	"""
	Return the ASCII value corresponding to the low 7 bits of *c*.
	
	
	"""
	pass
	
def ctrl(c):
	"""
	Return the control character corresponding to the given character (the character
	bit value is bitwise-anded with 0x1f).
	
	
	"""
	pass
	
def alt(c):
	"""
	Return the 8-bit character corresponding to the given ASCII character (the
	character bit value is bitwise-ored with 0x80).
	
	The following function takes either a single-character string or integer value;
	it returns a string.
	
	
	"""
	pass
	
def unctrl(c):
	"""
	Return a string representation of the ASCII character *c*.  If *c* is printable,
	this string is the character itself.  If the character is a control character
	(0x00-0x1f) the string consists of a caret (``'^'``) followed by the
	corresponding uppercase letter. If the character is an ASCII delete (0x7f) the
	string is ``'^?'``.  If the character has its meta bit (0x80) set, the meta bit
	is stripped, the preceding rules applied, and ``'!'`` prepended to the result.
	
	
	"""
	pass
	
