#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
""":synopsis: Telnet client class.
"""
class Telnet:


	"""
	:class:`Telnet` represents a connection to a Telnet server. The instance is
	initially not connected by default; the :meth:`open` method must be used to
	establish a connection.  Alternatively, the host name and optional port
	number can be passed to the constructor, to, in which case the connection to
	the server will be established before the constructor returns.  The optional
	*timeout* parameter specifies a timeout in seconds for blocking operations
	like the connection attempt (if not specified, the global default timeout
	setting will be used).
	
	Do not reopen an already connected instance.
	
	This class has many :meth:`read_\*` methods.  Note that some of them  raise
	:exc:`EOFError` when the end of the connection is read, because they can return
	an empty string for other reasons.  See the individual descriptions below.
	
	"""
	
	
	def __init__(self, host,port,timeout):
		pass
	
	


