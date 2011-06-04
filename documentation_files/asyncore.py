#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
""":synopsis: A base class for developing asynchronous socket handling
services.
"""
def loop(timeout,use_poll,map,count):
	"""
	Enter a polling loop that terminates after count passes or all open
	channels have been closed.  All arguments are optional.  The *count*
	parameter defaults to None, resulting in the loop terminating only when all
	channels have been closed.  The *timeout* argument sets the timeout
	parameter for the appropriate :func:`select` or :func:`poll` call, measured
	in seconds; the default is 30 seconds.  The *use_poll* parameter, if true,
	indicates that :func:`poll` should be used in preference to :func:`select`
	(the default is ``False``).
	
	The *map* parameter is a dictionary whose items are the channels to watch.
	As channels are closed they are deleted from their map.  If *map* is
	omitted, a global map is used. Channels (instances of
	:class:`asyncore.dispatcher`, :class:`asynchat.async_chat` and subclasses
	thereof) can freely be mixed in the map.
	
	
	"""
	pass
	
class dispatcher:


	"""
	The :class:`dispatcher` class is a thin wrapper around a low-level socket
	object. To make it more useful, it has a few methods for event-handling
	which are called from the asynchronous loop.   Otherwise, it can be treated
	as a normal non-blocking socket object.
	
	The firing of low-level events at certain times or in certain connection
	states tells the asynchronous loop that certain higher-level events have
	taken place.  For example, if we have asked for a socket to connect to
	another host, we know that the connection has been made when the socket
	becomes writable for the first time (at this point you know that you may
	write to it with the expectation of success).  The implied higher-level
	events are:
	
	+----------------------+----------------------------------------+
	| Event                | Description                            |
	+======================+========================================+
	| ``handle_connect()`` | Implied by the first read or write     |
	|                      | event                                  |
	+----------------------+----------------------------------------+
	| ``handle_close()``   | Implied by a read event with no data   |
	|                      | available                              |
	+----------------------+----------------------------------------+
	| ``handle_accept()``  | Implied by a read event on a listening |
	|                      | socket                                 |
	+----------------------+----------------------------------------+
	
	During asynchronous processing, each mapped channel's :meth:`readable` and
	:meth:`writable` methods are used to determine whether the channel's socket
	should be added to the list of channels :cfunc:`select`\ ed or
	:cfunc:`poll`\ ed for read and write events.
	
	Thus, the set of channel events is larger than the basic socket events.  The
	full set of methods that can be overridden in your subclass follows:
	
	
	"""
	
	
	def __init__(self, ):
		pass
	
	


class dispatcher_with_send:


	"""
	A :class:`dispatcher` subclass which adds simple buffered output capability,
	useful for simple clients. For more sophisticated usage use
	:class:`asynchat.async_chat`.
	
	"""
	
	
	def __init__(self, ):
		pass
	
	


class file_dispatcher:


	"""
	A file_dispatcher takes a file descriptor or file object along with an
	optional map argument and wraps it for use with the :cfunc:`poll` or
	:cfunc:`loop` functions.  If provided a file object or anything with a
	:cfunc:`fileno` method, that method will be called and passed to the
	:class:`file_wrapper` constructor.  Availability: UNIX.
	
	"""
	
	
	def __init__(self, ):
		pass
	
	


