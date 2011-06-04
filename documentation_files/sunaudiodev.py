#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
""":platform: SunOS
:synopsis: Access to Sun audio hardware.
:deprecated:

"""
def open(mode):
	"""
	This function opens the audio device and returns a Sun audio device object. This
	object can then be used to do I/O on. The *mode* parameter is one of ``'r'`` for
	record-only access, ``'w'`` for play-only access, ``'rw'`` for both and
	``'control'`` for access to the control device. Since only one process is
	allowed to have the recorder or player open at the same time it is a good idea
	to open the device only for the activity needed. See :manpage:`audio(7I)` for
	details.
	
	As per the manpage, this module first looks in the environment variable
	``AUDIODEV`` for the base audio device filename.  If not found, it falls back to
	:file:`/dev/audio`.  The control device is calculated by appending "ctl" to the
	base audio device.
	
	
	.. udio Device Objects
	--------------------
	
	The audio device objects are returned by :func:`.open` define the following
	methods (except ``control`` objects which only provide :meth:`getinfo`,
	:meth:`setinfo`, :meth:`fileno`, and :meth:`drain`):
	
	
	"""
	pass
	
