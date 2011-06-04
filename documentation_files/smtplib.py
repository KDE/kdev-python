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
	
	
	def __init__(self, ):
		pass
	
	def set_debuglevel(self, level):
		"""
		Set the debug output level.  A true value for *level* results in debug messages
		for connection and for all messages sent to and received from the server.
		
		
		"""
		pass
		
	def connect(self, host,port):
		"""
		Connect to a host on a given port.  The defaults are to connect to the local
		host at the standard SMTP port (25). If the hostname ends with a colon (``':'``)
		followed by a number, that suffix will be stripped off and the number
		interpreted as the port number to use. This method is automatically invoked by
		the constructor if a host is specified during instantiation.
		
		
		"""
		pass
		
	def docmd(self, cmd,,argstring):
		"""
		Send a command *cmd* to the server.  The optional argument *argstring* is simply
		concatenated to the command, separated by a space.
		
		This returns a 2-tuple composed of a numeric response code and the actual
		response line (multiline responses are joined into one long line.)
		
		In normal operation it should not be necessary to call this method explicitly.
		It is used to implement other methods and may be useful for testing private
		extensions.
		
		If the connection to the server is lost while waiting for the reply,
		:exc:`SMTPServerDisconnected` will be raised.
		
		
		"""
		pass
		
	def helo(self, hostname):
		"""
		Identify yourself to the SMTP server using ``HELO``.  The hostname argument
		defaults to the fully qualified domain name of the local host.
		The message returned by the server is stored as the :attr:`helo_resp` attribute
		of the object.
		
		In normal operation it should not be necessary to call this method explicitly.
		It will be implicitly called by the :meth:`sendmail` when necessary.
		
		
		"""
		pass
		
	def ehlo(self, hostname):
		"""
		Identify yourself to an ESMTP server using ``EHLO``.  The hostname argument
		defaults to the fully qualified domain name of the local host.  Examine the
		response for ESMTP option and store them for use by :meth:`has_extn`.
		Also sets several informational attributes: the message returned by
		the server is stored as the :attr:`ehlo_resp` attribute, :attr:`does_esmtp`
		is set to true or false depending on whether the server supports ESMTP, and
		:attr:`esmtp_features` will be a dictionary containing the names of the
		SMTP service extensions this server supports, and their
		parameters (if any).
		
		Unless you wish to use :meth:`has_extn` before sending mail, it should not be
		necessary to call this method explicitly.  It will be implicitly called by
		:meth:`sendmail` when necessary.
		
		"""
		pass
		
	def ehlo_or_helo_if_needed(self, ):
		"""
		This method call :meth:`ehlo` and or :meth:`helo` if there has been no
		previous ``EHLO`` or ``HELO`` command this session.  It tries ESMTP ``EHLO``
		first.
		
		:exc:`SMTPHeloError`
		The server didn't reply properly to the ``HELO`` greeting.
		
		"""
		pass
		
	def has_extn(self, name):
		"""
		Return :const:`True` if *name* is in the set of SMTP service extensions returned
		by the server, :const:`False` otherwise. Case is ignored.
		
		
		"""
		pass
		
	def verify(self, address):
		"""
		Check the validity of an address on this server using SMTP ``VRFY``. Returns a
		tuple consisting of code 250 and a full :rfc:`822` address (including human
		name) if the user address is valid. Otherwise returns an SMTP error code of 400
		or greater and an error string.
		
		"""
		pass
		
	def login(self, user,password):
		"""
		Log in on an SMTP server that requires authentication. The arguments are the
		username and the password to authenticate with. If there has been no previous
		``EHLO`` or ``HELO`` command this session, this method tries ESMTP ``EHLO``
		first. This method will return normally if the authentication was successful, or
		may raise the following exceptions:
		
		:exc:`SMTPHeloError`
		The server didn't reply properly to the ``HELO`` greeting.
		
		:exc:`SMTPAuthenticationError`
		The server didn't accept the username/password combination.
		
		:exc:`SMTPException`
		No suitable authentication method was found.
		
		
		"""
		pass
		
	def starttls(self, keyfile,certfile):
		"""
		Put the SMTP connection in TLS (Transport Layer Security) mode.  All SMTP
		commands that follow will be encrypted.  You should then call :meth:`ehlo`
		again.
		
		If *keyfile* and *certfile* are provided, these are passed to the :mod:`socket`
		module's :func:`ssl` function.
		
		If there has been no previous ``EHLO`` or ``HELO`` command this session,
		this method tries ESMTP ``EHLO`` first.
		
		"""
		pass
		
	def sendmail(self, _from_addr,to_addrs,msg,mail_options,rcpt_options):
		"""
		Send mail.  The required arguments are an :rfc:`822` from-address string, a list
		of :rfc:`822` to-address strings (a bare string will be treated as a list with 1
		address), and a message string.  The caller may pass a list of ESMTP options
		(such as ``8bitmime``) to be used in ``MAIL FROM`` commands as *mail_options*.
		ESMTP options (such as ``DSN`` commands) that should be used with all ``RCPT``
		commands can be passed as *rcpt_options*.  (If you need to use different ESMTP
		options to different recipients you have to use the low-level methods such as
		:meth:`mail`, :meth:`rcpt` and :meth:`data` to send the message.)
		
		"""
		pass
		
	def quit(self, ):
		"""
		Terminate the SMTP session and close the connection.  Return the result of
		the SMTP ``QUIT`` command.
		
		"""
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
	
	
	def __init__(self, ):
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
	
	
	def __init__(self, ):
		pass
	
	


