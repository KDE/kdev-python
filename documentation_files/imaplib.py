#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
""":synopsis: IMAP4 protocol client (requires sockets).
"""
class IMAP4:


	"""
	This class implements the actual IMAP4 protocol.  The connection is created and
	protocol version (IMAP4 or IMAP4rev1) is determined when the instance is
	initialized. If *host* is not specified, ``''`` (the local host) is used. If
	*port* is omitted, the standard IMAP4 port (143) is used.
	
	Three exceptions are defined as attributes of the :class:`IMAP4` class:
	
	
	"""
	
	
	def __init__(self, host,port):
		pass
	
	


class IMAP4_SSL:


	"""
	This is a subclass derived from :class:`IMAP4` that connects over an SSL
	encrypted socket (to use this class you need a socket module that was compiled
	with SSL support).  If *host* is not specified, ``''`` (the local host) is used.
	If *port* is omitted, the standard IMAP4-over-SSL port (993) is used.  *keyfile*
	and *certfile* are also optional - they can contain a PEM formatted private key
	and certificate chain file for the SSL connection.
	
	The second subclass allows for connections created by a child process:
	
	
	"""
	
	
	def __init__(self, host,port,keyfile,certfile):
		pass
	
	


class IMAP4_stream:


	"""
	This is a subclass derived from :class:`IMAP4` that connects to the
	``stdin/stdout`` file descriptors created by passing *command* to
	``os.popen2()``.
	
	"""
	
	
	def __init__(self, command):
		pass
	
	def Internaldate2tuple(datestr):
		"""
		Parse an IMAP4 ``INTERNALDATE`` string and return corresponding local
		time.  The return value is a :class:`time.struct_time` instance or
		None if the string has wrong format.
		
		"""
		pass
		
	def Int2AP(num):
		"""
		Converts an integer into a string representation using characters from the set
		"""
		pass
		
	def ParseFlags(flagstr):
		"""
		Converts an IMAP4 ``FLAGS`` response to a tuple of individual flags.
		
		
		"""
		pass
		
	def Time2Internaldate(date_time):
		"""
		Convert *date_time* to an IMAP4 ``INTERNALDATE`` representation.  The
		return value is a string in the form: ``"DD-Mmm-YYYY HH:MM:SS
		+HHMM"`` (including double-quotes).  The *date_time* argument can be a
		number (int or float) representing seconds since epoch (as returned
		by :func:`time.time`), a 9-tuple representing local time (as returned by
		:func:`time.localtime`), or a double-quoted string.  In the last case, it
		is assumed to already be in the correct format.
		
		Note that IMAP4 message numbers change as the mailbox changes; in particular,
		after an ``EXPUNGE`` command performs deletions the remaining messages are
		renumbered. So it is highly advisable to use UIDs instead, with the UID command.
		
		At the end of the module, there is a test section that contains a more extensive
		example of usage.
		
		
		"""
		pass
		
	


