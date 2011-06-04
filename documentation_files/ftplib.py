#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
""":synopsis: FTP protocol client (requires sockets).


"""
class FTP:


	"""
	Return a new instance of the :class:`FTP` class.  When *host* is given, the
	method call ``connect(host)`` is made.  When *user* is given, additionally
	the method call ``login(user, passwd, acct)`` is made (where *passwd* and
	*acct* default to the empty string when not given).  The optional *timeout*
	parameter specifies a timeout in seconds for blocking operations like the
	connection attempt (if is not specified, the global default timeout setting
	will be used).
	
	"""
	
	
	def __init__(self, host,user,passwd,acct,timeout):
		pass
	
	


class FTP_TLS:


	"""
	A :class:`FTP` subclass which adds TLS support to FTP as described in
	:rfc:`4217`.
	Connect as usual to port 21 implicitly securing the FTP control connection
	before authenticating. Securing the data connection requires the user to
	explicitly ask for it by calling the :meth:`prot_p` method.
	*keyfile* and *certfile* are optional -- they can contain a PEM formatted
	private key and certificate chain file name for the SSL connection.
	
	"""
	
	
	def __init__(self, host,user,passwd,acct,keyfile,certfile,timeout):
		pass
	
	"""
	The set of all exceptions (as a tuple) that methods of :class:`FTP`
	instances may raise as a result of problems with the FTP connection (as
	opposed to programming errors made by the caller).  This set includes the
	four exceptions listed above as well as :exc:`socket.error` and
	:exc:`IOError`.
	
	
	"""
	all_errors = None
	


