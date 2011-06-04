#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
""":platform: Linux, FreeBSD
:synopsis: Access to OSS-compatible audio devices.


"""
def open(device,mode):
	"""
	Open an audio device and return an OSS audio device object.  This object
	supports many file-like methods, such as :meth:`read`, :meth:`write`, and
	:meth:`fileno` (although there are subtle differences between conventional Unix
	read/write semantics and those of OSS audio devices).  It also supports a number
	of audio-specific methods; see below for the complete list of methods.
	
	*device* is the audio device filename to use.  If it is not specified, this
	module first looks in the environment variable :envvar:`AUDIODEV` for a device
	to use.  If not found, it falls back to :file:`/dev/dsp`.
	
	*mode* is one of ``'r'`` for read-only (record) access, ``'w'`` for
	write-only (playback) access and ``'rw'`` for both. Since many sound cards
	only allow one process to have the recorder or player open at a time, it is a
	good idea to open the device only for the activity needed.  Further, some
	sound cards are half-duplex: they can be opened for reading or writing, but
	not both at once.
	
	Note the unusual calling syntax: the *first* argument is optional, and the
	second is required.  This is a historical artifact for compatibility with the
	older :mod:`linuxaudiodev` module which :mod:`ossaudiodev` supersedes.
	
	.. ight also be motivated
	by my unfounded-but-still-possibly-true belief that the default
	audio device varies unpredictably across operating systems.  -GW
	
	
	"""
	pass
	
def openmixer(device):
	"""
	Open a mixer device and return an OSS mixer device object.   *device* is the
	mixer device filename to use.  If it is not specified, this module first looks
	in the environment variable :envvar:`MIXERDEV` for a device to use.  If not
	found, it falls back to :file:`/dev/mixer`.
	
	
	.. udio Device Objects
	--------------------
	
	Before you can write to or read from an audio device, you must call three
	methods in the correct order:
	
	#. :meth:`setfmt` to set the output format
	
	#. :meth:`channels` to set the number of channels
	
	#. :meth:`speed` to set the sample rate
	
	Alternately, you can use the :meth:`setparameters` method to set all three audio
	parameters at once.  This is more convenient, but may not be as flexible in all
	cases.
	
	The audio device objects returned by :func:`.open` define the following methods
	and (read-only) attributes:
	
	
	"""
	pass
	
