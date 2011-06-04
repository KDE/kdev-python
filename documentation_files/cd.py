#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
""":platform: IRIX
:synopsis: Interface to the CD-ROM on Silicon Graphics systems.
:deprecated:


"""
"""
The size of one frame's worth of audio data.  This is the size of the audio data
as passed to the callback of type ``audio``.


"""
DATASIZE = None
"""
The size of one uninterpreted frame of audio data.

The following variables are states as returned by :func:`getstatus`:


"""
BLOCKSIZE = None
"""
The drive is ready for operation loaded with an audio CD.


"""
READY = None
"""
The drive does not have a CD loaded.


"""
NODISC = None
"""
The drive is loaded with a CD-ROM.  Subsequent play or read operations will
return I/O errors.


"""
CDROM = None
"""
An error occurred while trying to read the disc or its table of contents.


"""
ERROR = None
"""
The drive is in CD player mode playing an audio CD through its audio jacks.


"""
PLAYING = None
"""
The drive is in CD layer mode with play paused.


"""
PAUSED = None
"""
The equivalent of :const:`PAUSED` on older (non 3301) model Toshiba CD-ROM
drives.  Such drives have never been shipped by SGI.


"""
STILL = None
"""pnum
index
ptime
atime
catalog
ident
control

Integer constants describing the various types of parser callbacks that can be
set by the :meth:`addcallback` method of CD parser objects (see below).


.. layer Objects
--------------

Player objects (returned by :func:`.open`) have the following methods:


"""
audio = None
def createparser():
	"""
	Create and return an opaque parser object.  The methods of the parser object are
	described below.
	
	
	"""
	pass
	
def msftoframe(minutes,seconds,frames):
	"""
	Converts a ``(minutes, seconds, frames)`` triple representing time in absolute
	time code into the corresponding CD frame number.
	
	
	"""
	pass
	
def open(device,mode):
	"""
	Open the CD-ROM device.  The return value is an opaque player object; methods of
	the player object are described below.  The device is the name of the SCSI
	device file, e.g. ``'/dev/scsi/sc0d4l0'``, or ``None``.  If omitted or ``None``,
	the hardware inventory is consulted to locate a CD-ROM drive.  The *mode*, if
	not omitted, should be the string ``'r'``.
	
	The module defines the following variables:
	
	
	"""
	pass
	
