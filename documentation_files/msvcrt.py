#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
""":platform: Windows
:synopsis: Miscellaneous useful routines from the MS VC++ runtime.
"""
"""LK_RLCK

Locks the specified bytes. If the bytes cannot be locked, the program
immediately tries again after 1 second.  If, after 10 attempts, the bytes cannot
be locked, :exc:`IOError` is raised.


"""
LK_LOCK = None
"""LK_NBRLCK

Locks the specified bytes. If the bytes cannot be locked, :exc:`IOError` is
raised.


"""
LK_NBLCK = None
"""
Unlocks the specified bytes, which must have been previously locked.


"""
LK_UNLCK = None
def locking(fd,mode,nbytes):
	"""
	Lock part of a file based on file descriptor *fd* from the C runtime.  Raises
	:exc:`IOError` on failure.  The locked region of the file extends from the
	current file position for *nbytes* bytes, and may continue beyond the end of the
	file.  *mode* must be one of the :const:`LK_\*` constants listed below. Multiple
	regions in a file may be locked at the same time, but may not overlap.  Adjacent
	regions are not merged; they must be unlocked individually.
	
	
	"""
	pass
	
def setmode(fd,flags):
	"""
	Set the line-end translation mode for the file descriptor *fd*. To set it to
	text mode, *flags* should be :const:`os.O_TEXT`; for binary, it should be
	:const:`os.O_BINARY`.
	
	
	"""
	pass
	
def open_osfhandle(handle,flags):
	"""
	Create a C runtime file descriptor from the file handle *handle*.  The *flags*
	parameter should be a bitwise OR of :const:`os.O_APPEND`, :const:`os.O_RDONLY`,
	and :const:`os.O_TEXT`.  The returned file descriptor may be used as a parameter
	to :func:`os.fdopen` to create a file object.
	
	
	"""
	pass
	
def get_osfhandle(fd):
	"""
	Return the file handle for the file descriptor *fd*.  Raises :exc:`IOError` if
	*fd* is not recognized.
	
	
	.. onsole I/O
	-----------
	
	
	"""
	pass
	
def kbhit():
	"""
	Return true if a keypress is waiting to be read.
	
	
	"""
	pass
	
def getch():
	"""
	Read a keypress and return the resulting character.  Nothing is echoed to the
	console.  This call will block if a keypress is not already available, but will
	not wait for :kbd:`Enter` to be pressed. If the pressed key was a special
	function key, this will return ``'\000'`` or ``'\xe0'``; the next call will
	return the keycode.  The :kbd:`Control-C` keypress cannot be read with this
	function.
	
	
	"""
	pass
	
def getwch():
	"""
	Wide char variant of :func:`getch`, returning a Unicode value.
	
	"""
	pass
	
def getche():
	"""
	Similar to :func:`getch`, but the keypress will be echoed if it  represents a
	printable character.
	
	
	"""
	pass
	
def getwche():
	"""
	Wide char variant of :func:`getche`, returning a Unicode value.
	
	"""
	pass
	
def putch(char):
	"""
	Print the character *char* to the console without buffering.
	
	
	"""
	pass
	
def putwch(unicode_char):
	"""
	Wide char variant of :func:`putch`, accepting a Unicode value.
	
	"""
	pass
	
def ungetch(char):
	"""
	Cause the character *char* to be "pushed back" into the console buffer; it will
	be the next character read by :func:`getch` or :func:`getche`.
	
	
	"""
	pass
	
def ungetwch(unicode_char):
	"""
	Wide char variant of :func:`ungetch`, accepting a Unicode value.
	
	"""
	pass
	
