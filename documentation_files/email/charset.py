#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
""":synopsis: Character Sets


This module provides a class :class:`Charset` for representing character sets
and character set conversions in email messages, as well as a character set
registry and several convenience methods for manipulating this registry.
Instances of :class:`Charset` are used in several other modules within the
:mod:`email` package.

Import this class from the :mod:`email.charset` module.

"""
class Charset:


	"""
	Map character sets to their email properties.
	
	This class provides information about the requirements imposed on email for a
	specific character set.  It also provides convenience routines for converting
	between character sets, given the availability of the applicable codecs.  Given
	a character set, it will do its best to provide information on how to use that
	character set in an email message in an RFC-compliant way.
	
	Certain character sets must be encoded with quoted-printable or base64 when used
	in email headers or bodies.  Certain character sets must be converted outright,
	and are not allowed in email.
	
	Optional *input_charset* is as described below; it is always coerced to lower
	case.  After being alias normalized it is also used as a lookup into the
	registry of character sets to find out the header encoding, body encoding, and
	output conversion codec to be used for the character set.  For example, if
	*input_charset* is ``iso-8859-1``, then headers and bodies will be encoded using
	quoted-printable and no output conversion codec is necessary.  If
	*input_charset* is ``euc-jp``, then headers will be encoded with base64, bodies
	will not be encoded, but output text will be converted from the ``euc-jp``
	character set to the ``iso-2022-jp`` character set.
	
	:class:`Charset` instances have the following data attributes:
	
	
	"""
	
	
	def __init__(self, input_charset):
		pass
	
	def add_charset(charset,header_enc,body_enc,output_charset):
		"""
		Add character properties to the global registry.
		
		*charset* is the input character set, and must be the canonical name of a
		character set.
		
		Optional *header_enc* and *body_enc* is either ``Charset.QP`` for
		quoted-printable, ``Charset.BASE64`` for base64 encoding,
		``Charset.SHORTEST`` for the shortest of quoted-printable or base64 encoding,
		or ``None`` for no encoding.  ``SHORTEST`` is only valid for
		*header_enc*. The default is ``None`` for no encoding.
		
		Optional *output_charset* is the character set that the output should be in.
		Conversions will proceed from input charset, to Unicode, to the output charset
		when the method :meth:`Charset.convert` is called.  The default is to output in
		the same character set as the input.
		
		Both *input_charset* and *output_charset* must have Unicode codec entries in the
		module's character set-to-codec mapping; use :func:`add_codec` to add codecs the
		module does not know about.  See the :mod:`codecs` module's documentation for
		more information.
		
		The global character set registry is kept in the module global dictionary
		``CHARSETS``.
		
		
		"""
		pass
		
	def add_alias(alias,canonical):
		"""
		Add a character set alias.  *alias* is the alias name, e.g. ``latin-1``.
		*canonical* is the character set's canonical name, e.g. ``iso-8859-1``.
		
		The global charset alias registry is kept in the module global dictionary
		``ALIASES``.
		
		
		"""
		pass
		
	


