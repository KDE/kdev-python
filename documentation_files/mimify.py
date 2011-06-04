#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
""":synopsis: Mimification and unmimification of mail messages.
:deprecated:


"""
"""
By default, a part will be encoded as quoted-printable when it contains any
non-ASCII characters (characters with the 8th bit set), or if there are any
lines longer than :const:`MAXLEN` characters (default value 200).


"""
MAXLEN = None
"""
When not specified in the mail headers, a character set must be filled in.  The
string used is stored in :const:`CHARSET`, and the default value is ISO-8859-1
(also known as Latin1 (latin-one)).

This module can also be used from the command line.  Usage is as follows::

mimify.py -e [-l length] [infile [outfile]]
mimify.py -d [-b] [infile [outfile]]

to encode (mimify) and decode (unmimify) respectively.  *infile* defaults to
standard input, *outfile* defaults to standard output. The same file can be
specified for input and output.

If the **-l** option is given when encoding, if there are any lines longer than
the specified *length*, the containing part will be encoded.

If the **-b** option is given when decoding, any base64 parts will be decoded as
well.


"""
CHARSET = None
def mimify(infile,outfile):
	"""
	Copy the message in *infile* to *outfile*, converting parts to quoted-printable
	and adding MIME mail headers when necessary. *infile* and *outfile* can be file
	objects (actually, any object that has a :meth:`readline` method (for *infile*)
	or a :meth:`write` method (for *outfile*)) or strings naming the files. If
	*infile* and *outfile* are both strings, they may have the same value.
	
	
	"""
	pass
	
def unmimify(infile,outfile,decode_base64):
	"""
	Copy the message in *infile* to *outfile*, decoding all quoted-printable parts.
	*infile* and *outfile* can be file objects (actually, any object that has a
	:meth:`readline` method (for *infile*) or a :meth:`write` method (for
	*outfile*)) or strings naming the files.  If *infile* and *outfile* are both
	strings, they may have the same value. If the *decode_base64* argument is
	provided and tests true, any parts that are coded in the base64 encoding are
	decoded as well.
	
	
	"""
	pass
	
def mime_decode_header(line):
	"""
	Return a decoded version of the encoded header line in *line*. This only
	supports the ISO 8859-1 charset (Latin-1).
	
	
	"""
	pass
	
def mime_encode_header(line):
	"""
	Return a MIME-encoded version of the header line in *line*.
	
	
	"""
	pass
	
