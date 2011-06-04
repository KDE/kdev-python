#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
""":platform: Unix
:synopsis: Utility functions that perform common terminal control operations.
"""
def setraw(fd,when):
	"""
	Change the mode of the file descriptor *fd* to raw. If *when* is omitted, it
	defaults to :const:`termios.TCSAFLUSH`, and is passed to
	:func:`termios.tcsetattr`.
	
	
	"""
	pass
	
def setcbreak(fd,when):
	"""
	Change the mode of file descriptor *fd* to cbreak. If *when* is omitted, it
	defaults to :const:`termios.TCSAFLUSH`, and is passed to
	:func:`termios.tcsetattr`.
	
	
	"""
	pass
	
