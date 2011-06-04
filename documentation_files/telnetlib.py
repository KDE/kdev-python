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
	
	
	def __init__(self, ):
		pass
	
	def read_until(self, expected,timeout):
		"""
		Read until a given string, *expected*, is encountered or until *timeout* seconds
		have passed.
		
		When no match is found, return whatever is available instead, possibly the empty
		string.  Raise :exc:`EOFError` if the connection is closed and no cooked data is
		available.
		
		
		"""
		pass
		
	def read_all(self, ):
		"""
		Read all data until EOF; block until connection closed.
		
		
		"""
		pass
		
	def read_some(self, ):
		"""
		Read at least one byte of cooked data unless EOF is hit. Return ``''`` if EOF is
		hit.  Block if no data is immediately available.
		
		
		"""
		pass
		
	def read_very_eager(self, ):
		"""
		Read everything that can be without blocking in I/O (eager).
		
		Raise :exc:`EOFError` if connection closed and no cooked data available.  Return
		``''`` if no cooked data available otherwise. Do not block unless in the midst
		of an IAC sequence.
		
		
		"""
		pass
		
	def read_eager(self, ):
		"""
		Read readily available data.
		
		Raise :exc:`EOFError` if connection closed and no cooked data available.  Return
		``''`` if no cooked data available otherwise. Do not block unless in the midst
		of an IAC sequence.
		
		
		"""
		pass
		
	def read_lazy(self, ):
		"""
		Process and return data already in the queues (lazy).
		
		Raise :exc:`EOFError` if connection closed and no data available. Return ``''``
		if no cooked data available otherwise.  Do not block unless in the midst of an
		IAC sequence.
		
		
		"""
		pass
		
	def read_very_lazy(self, ):
		"""
		Return any data available in the cooked queue (very lazy).
		
		Raise :exc:`EOFError` if connection closed and no data available. Return ``''``
		if no cooked data available otherwise.  This method never blocks.
		
		
		"""
		pass
		
	def read_sb_data(self, ):
		"""
		Return the data collected between a SB/SE pair (suboption begin/end). The
		callback should access these data when it was invoked with a ``SE`` command.
		This method never blocks.
		
		"""
		pass
		
	def open(self, host,port,timeout):
		"""
		Connect to a host. The optional second argument is the port number, which
		defaults to the standard Telnet port (23). The optional *timeout* parameter
		specifies a timeout in seconds for blocking operations like the connection
		attempt (if not specified, the global default timeout setting will be used).
		
		Do not try to reopen an already connected instance.
		
		"""
		pass
		
	def msg(self, msg,args):
		"""
		Print a debug message when the debug level is ``>`` 0. If extra arguments are
		present, they are substituted in the message using the standard string
		formatting operator.
		
		
		"""
		pass
		
	def set_debuglevel(self, debuglevel):
		"""
		Set the debug level.  The higher the value of *debuglevel*, the more debug
		output you get (on ``sys.stdout``).
		
		
		"""
		pass
		
	def close(self, ):
		"""
		Close the connection.
		
		
		"""
		pass
		
	def get_socket(self, ):
		"""
		Return the socket object used internally.
		
		
		"""
		pass
		
	def fileno(self, ):
		"""
		Return the file descriptor of the socket object used internally.
		
		
		"""
		pass
		
	def write(self, buffer):
		"""
		Write a string to the socket, doubling any IAC characters. This can block if the
		connection is blocked.  May raise :exc:`socket.error` if the connection is
		closed.
		
		
		"""
		pass
		
	def interact(self, ):
		"""
		Interaction function, emulates a very dumb Telnet client.
		
		
		"""
		pass
		
	def mt_interact(self, ):
		"""
		Multithreaded version of :meth:`interact`.
		
		
		"""
		pass
		
	def expect(self, list,timeout):
		"""
		Read until one from a list of a regular expressions matches.
		
		The first argument is a list of regular expressions, either compiled
		(:class:`re.RegexObject` instances) or uncompiled (strings). The optional second
		argument is a timeout, in seconds; the default is to block indefinitely.
		
		Return a tuple of three items: the index in the list of the first regular
		expression that matches; the match object returned; and the text read up till
		and including the match.
		
		If end of file is found and no text was read, raise :exc:`EOFError`.  Otherwise,
		when nothing matches, return ``(-1, None, text)`` where *text* is the text
		received so far (may be the empty string if a timeout happened).
		
		If a regular expression ends with a greedy match (such as ``.*``) or if more
		than one expression can match the same input, the results are
		non-deterministic, and may depend on the I/O timing.
		
		
		"""
		pass
		
	def set_option_negotiation_callback(self, callback):
		"""
		Each time a telnet option is read on the input flow, this *callback* (if set) is
		called with the following parameters : callback(telnet socket, command
		(DO/DONT/WILL/WONT), option).  No other action is done afterwards by telnetlib.
		
		
		.. elnet Example
		--------------
		
		"""
		pass
		
	


