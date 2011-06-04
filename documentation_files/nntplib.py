#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
""":synopsis: NNTP protocol client (requires sockets).


"""
class NNTP:


	"""
	Return a new instance of the :class:`NNTP` class, representing a connection
	to the NNTP server running on host *host*, listening at port *port*.  The
	default *port* is 119.  If the optional *user* and *password* are provided,
	or if suitable credentials are present in :file:`/.netrc` and the optional
	flag *usenetrc* is true (the default), the ``AUTHINFO USER`` and ``AUTHINFO
	PASS`` commands are used to identify and authenticate the user to the server.
	If the optional flag *readermode* is true, then a ``mode reader`` command is
	sent before authentication is performed.  Reader mode is sometimes necessary
	if you are connecting to an NNTP server on the local machine and intend to
	call reader-specific commands, such as ``group``.  If you get unexpected
	:exc:`NNTPPermanentError`\ s, you might need to set *readermode*.
	*readermode* defaults to ``None``. *usenetrc* defaults to ``True``.
	
	"""
	
	
	def __init__(self, host,port,user,password,readermode,usenetrc):
		pass
	
	


