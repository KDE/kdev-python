#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
""":platform: Linux
:synopsis: Pseudo-Terminal Handling for Linux.
"""
def fork():
	"""
	Fork. Connect the child's controlling terminal to a pseudo-terminal. Return
	value is ``(pid, fd)``. Note that the child  gets *pid* 0, and the *fd* is
	*invalid*. The parent's return value is the *pid* of the child, and *fd* is a
	file descriptor connected to the child's controlling terminal (and also to the
	child's standard input and output).
	
	
	"""
	pass
	
def openpty():
	"""
	Open a new pseudo-terminal pair, using :func:`os.openpty` if possible, or
	emulation code for generic Unix systems. Return a pair of file descriptors
	``(master, slave)``, for the master and the slave end, respectively.
	
	
	"""
	pass
	
