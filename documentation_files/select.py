#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
""":synopsis: Wait for I/O completion on multiple streams.


This module provides access to the :cfunc:`select` and :cfunc:`poll` functions
available in most operating systems, :cfunc:`epoll` available on Linux 2.5+ and
:cfunc:`kqueue` available on most BSD.
Note that on Windows, it only works for sockets; on other operating systems,
it also works for other file types (in particular, on Unix, it works on pipes).
It cannot be used on regular files to determine whether a file has grown since
it was last read.

The module defines the following:


"""
def epoll(sizehint=_1):
	"""
	(Only supported on Linux 2.5.44 and newer.)  Returns an edge polling object,
	which can be used as Edge or Level Triggered interface for I/O events; see
	section :ref:`epoll-objects` below for the methods supported by epolling
	objects.
	
	"""
	pass
	
def poll():
	"""
	(Not supported by all operating systems.)  Returns a polling object, which
	supports registering and unregistering file descriptors, and then polling them
	for I/O events; see section :ref:`poll-objects` below for the methods supported
	by polling objects.
	
	
	"""
	pass
	
def kqueue():
	"""
	(Only supported on BSD.)  Returns a kernel queue object; see section
	:ref:`kqueue-objects` below for the methods supported by kqueue objects.
	
	"""
	pass
	
def kevent(ident,filter=KQ_FILTER_READ,flags=KQ_EV_ADD,fflags=0,data=0,udata=0):
	"""
	(Only supported on BSD.)  Returns a kernel event object; see section
	:ref:`kevent-objects` below for the methods supported by kevent objects.
	
	"""
	pass
	
def select(rlist,wlist,xlist,timeout):
	"""
	This is a straightforward interface to the Unix :cfunc:`select` system call.
	The first three arguments are sequences of 'waitable objects': either
	integers representing file descriptors or objects with a parameterless method
	named :meth:`fileno` returning such an integer:
	
	* *rlist*: wait until ready for reading
	* *wlist*: wait until ready for writing
	* *xlist*: wait for an "exceptional condition" (see the manual page for what
	your system considers such a condition)
	
	Empty sequences are allowed, but acceptance of three empty sequences is
	platform-dependent. (It is known to work on Unix but not on Windows.)  The
	optional *timeout* argument specifies a time-out as a floating point number
	in seconds.  When the *timeout* argument is omitted the function blocks until
	at least one file descriptor is ready.  A time-out value of zero specifies a
	poll and never blocks.
	
	The return value is a triple of lists of objects that are ready: subsets of the
	first three arguments.  When the time-out is reached without a file descriptor
	becoming ready, three empty lists are returned.
	
	"""
	pass
	
