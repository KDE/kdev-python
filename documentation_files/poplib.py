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
	
	
	def __init__(self, host,port,timeout):
		pass
	
	


class POP3_SSL:


	"""
	This is a subclass of :class:`POP3` that connects to the server over an SSL
	encrypted socket.  If *port* is not specified, 995, the standard POP3-over-SSL
	port is used.  *keyfile* and *certfile* are also optional - they can contain a
	PEM formatted private key and certificate chain file for the SSL connection.
	
	"""
	
	
	def __init__(self, host,port,keyfile,certfile):
		pass
	
	


