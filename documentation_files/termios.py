#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
""":platform: Unix
:synopsis: POSIX style tty control.


"""
def tcgetattr(fd):
	"""
	Return a list containing the tty attributes for file descriptor *fd*, as
	follows: ``[iflag, oflag, cflag, lflag, ispeed, ospeed, cc]`` where *cc* is a
	list of the tty special characters (each a string of length 1, except the
	items with indices :const:`VMIN` and :const:`VTIME`, which are integers when
	these fields are defined).  The interpretation of the flags and the speeds as
	well as the indexing in the *cc* array must be done using the symbolic
	constants defined in the :mod:`termios` module.
	
	
	"""
	pass
	
def tcsetattr(fd,when,attributes):
	"""
	Set the tty attributes for file descriptor *fd* from the *attributes*, which is
	a list like the one returned by :func:`tcgetattr`.  The *when* argument
	determines when the attributes are changed: :const:`TCSANOW` to change
	immediately, :const:`TCSADRAIN` to change after transmitting all queued output,
	or :const:`TCSAFLUSH` to change after transmitting all queued output and
	discarding all queued input.
	
	
	"""
	pass
	
def tcsendbreak(fd,duration):
	"""
	Send a break on file descriptor *fd*.  A zero *duration* sends a break for 0.25
	--0.5 seconds; a nonzero *duration* has a system dependent meaning.
	
	
	"""
	pass
	
def tcdrain(fd):
	"""
	Wait until all output written to file descriptor *fd* has been transmitted.
	
	
	"""
	pass
	
def tcflush(fd,queue):
	"""
	Discard queued data on file descriptor *fd*.  The *queue* selector specifies
	which queue: :const:`TCIFLUSH` for the input queue, :const:`TCOFLUSH` for the
	output queue, or :const:`TCIOFLUSH` for both queues.
	
	
	"""
	pass
	
def tcflow(fd,action):
	"""
	Suspend or resume input or output on file descriptor *fd*.  The *action*
	argument can be :const:`TCOOFF` to suspend output, :const:`TCOON` to restart
	output, :const:`TCIOFF` to suspend input, or :const:`TCION` to restart input.
	
	
	"""
	pass
	
