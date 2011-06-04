#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
""":synopsis: SMTP protocol client (requires sockets).
"""
class SMTP:


	"""
	A :class:`SMTP` instance encapsulates an SMTP connection.  It has methods
	that support a full repertoire of SMTP and ESMTP operations. If the optional
	host and port parameters are given, the SMTP :meth:`connect` method is called
	with those parameters during initialization.  An :exc:`SMTPConnectError` is
	raised if the specified host doesn't respond correctly. The optional
	*timeout* parameter specifies a timeout in seconds for blocking operations
	like the connection attempt (if not specified, the global default timeout
	setting will be used).
	
	For normal use, you should only require the initialization/connect,
	:meth:`sendmail`, and :meth:`quit` methods.  An example is included below.
	
	"""
	
	
	def __init__(self, host,port,local_hostname,timeout):
		pass
	
	


class SMTP_SSL:


	"""
	A :class:`SMTP_SSL` instance behaves exactly the same as instances of
	:class:`SMTP`. :class:`SMTP_SSL` should be used for situations where SSL is
	required from the beginning of the connection and using :meth:`starttls` is
	not appropriate. If *host* is not specified, the local host is used. If
	*port* is omitted, the standard SMTP-over-SSL port (465) is used. *keyfile*
	and *certfile* are also optional, and can contain a PEM formatted private key
	and certificate chain file for the SSL connection. The optional *timeout*
	parameter specifies a timeout in seconds for blocking operations like the
	connection attempt (if not specified, the global default timeout setting
	will be used).
	
	"""
	
	
	def __init__(self, host,port,local_hostname,keyfile,certfile,timeout):
		pass
	
	


class LMTP:


	"""
	The LMTP protocol, which is very similar to ESMTP, is heavily based on the
	standard SMTP client. It's common to use Unix sockets for LMTP, so our :meth:`connect`
	method must support that as well as a regular host:port server. To specify a
	Unix socket, you must use an absolute path for *host*, starting with a '/'.
	
	Authentication is supported, using the regular SMTP mechanism. When using a Unix
	socket, LMTP generally don't support or require any authentication, but your
	mileage might vary.
	
	"""
	
	
	def __init__(self, host,port,local_hostname):
		pass
	
	


