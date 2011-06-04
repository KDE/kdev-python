#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
""":synopsis: A SMTP server implementation in Python.

"""
class SMTPServer:


	"""
	Create a new :class:`SMTPServer` object, which binds to local address
	*localaddr*.  It will treat *remoteaddr* as an upstream SMTP relayer.  It
	inherits from :class:`asyncore.dispatcher`, and so will insert itself into
	:mod:`asyncore`'s event loop on instantiation.
	
	
	"""
	
	
	def __init__(self, localaddr,remoteaddr):
		pass
	
	


class DebuggingServer:


	"""
	Create a new debugging server.  Arguments are as per :class:`SMTPServer`.
	Messages will be discarded, and printed on stdout.
	
	
	PureProxy Objects
	-----------------
	
	
	"""
	
	
	def __init__(self, localaddr,remoteaddr):
		pass
	
	


class PureProxy:


	"""
	Create a new pure proxy server. Arguments are as per :class:`SMTPServer`.
	Everything will be relayed to *remoteaddr*.  Note that running this has a good
	chance to make you into an open relay, so please be careful.
	
	
	MailmanProxy Objects
	--------------------
	
	
	"""
	
	
	def __init__(self, localaddr,remoteaddr):
		pass
	
	


