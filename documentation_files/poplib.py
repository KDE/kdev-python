#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
""":synopsis: POP3 protocol client (requires sockets).
"""
class POP3:


	"""
	This class implements the actual POP3 protocol.  The connection is created when
	the instance is initialized. If *port* is omitted, the standard POP3 port (110)
	is used. The optional *timeout* parameter specifies a timeout in seconds for the
	connection attempt (if not specified, the global default timeout setting will
	be used).
	
	"""
	
	
	def __init__(self, ):
		pass
	
	def set_debuglevel(self, level):
		"""
		Set the instance's debugging level.  This controls the amount of debugging
		output printed.  The default, ``0``, produces no debugging output.  A value of
		``1`` produces a moderate amount of debugging output, generally a single line
		per request.  A value of ``2`` or higher produces the maximum amount of
		debugging output, logging each line sent and received on the control connection.
		
		
		"""
		pass
		
	def getwelcome(self, ):
		"""
		Returns the greeting string sent by the POP3 server.
		
		
		"""
		pass
		
	def user(self, username):
		"""
		Send user command, response should indicate that a password is required.
		
		
		"""
		pass
		
	def pass_(self, password):
		"""
		Send password, response includes message count and mailbox size. Note: the
		mailbox on the server is locked until :meth:`quit` is called.
		
		
		"""
		pass
		
	def apop(self, user,secret):
		"""
		Use the more secure APOP authentication to log into the POP3 server.
		
		
		"""
		pass
		
	def rpop(self, user):
		"""
		Use RPOP authentication (similar to UNIX r-commands) to log into POP3 server.
		
		
		"""
		pass
		
	def stat(self, ):
		"""
		Get mailbox status.  The result is a tuple of 2 integers: ``(message count,
		mailbox size)``.
		
		
		"""
		pass
		
	def list(self, which):
		"""
		Request message list, result is in the form ``(response, ['mesg_num octets',
		*more], octets)``. If *which* is set, it is the message to list.
		
		
		"""
		pass
		
	def retr(self, which):
		"""
		Retrieve whole message number *which*, and set its seen flag. Result is in form
		``(response, ['line', *more], octets)``.
		
		
		"""
		pass
		
	def dele(self, which):
		"""
		Flag message number *which* for deletion.  On most servers deletions are not
		actually performed until QUIT (the major exception is Eudora QPOP, which
		deliberately violates the RFCs by doing pending deletes on any disconnect).
		
		
		"""
		pass
		
	def rset(self, ):
		"""
		Remove any deletion marks for the mailbox.
		
		
		"""
		pass
		
	def noop(self, ):
		"""
		Do nothing.  Might be used as a keep-alive.
		
		
		"""
		pass
		
	def quit(self, ):
		"""
		Signoff:  commit changes, unlock mailbox, drop connection.
		
		
		"""
		pass
		
	def top(self, which,howmuch):
		"""
		Retrieves the message header plus *howmuch* lines of the message after the
		header of message number *which*. Result is in form ``(response, ['line', *more],
		octets)``.
		
		The POP3 TOP command this method uses, unlike the RETR command, doesn't set the
		message's seen flag; unfortunately, TOP is poorly specified in the RFCs and is
		frequently broken in off-brand servers. Test this method by hand against the
		POP3 servers you will use before trusting it.
		
		
		"""
		pass
		
	


class POP3_SSL:


	"""
	This is a subclass of :class:`POP3` that connects to the server over an SSL
	encrypted socket.  If *port* is not specified, 995, the standard POP3-over-SSL
	port is used.  *keyfile* and *certfile* are also optional - they can contain a
	PEM formatted private key and certificate chain file for the SSL connection.
	
	"""
	
	
	def __init__(self, ):
		pass
	
	


