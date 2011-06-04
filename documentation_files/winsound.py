#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
""":platform: Windows
:synopsis: Access to the sound-playing machinery for Windows.
"""
"""
The *sound* parameter is the name of a WAV file. Do not use with
:const:`SND_ALIAS`.


"""
SND_FILENAME = None
"""
The *sound* parameter is a sound association name from the registry.  If the
registry contains no such name, play the system default sound unless
:const:`SND_NODEFAULT` is also specified. If no default sound is registered,
raise :exc:`RuntimeError`. Do not use with :const:`SND_FILENAME`.

All Win32 systems support at least the following; most systems support many
more:

+--------------------------+----------------------------------------+
| :func:`PlaySound` *name* | Corresponding Control Panel Sound name |
+==========================+========================================+
| ``'SystemAsterisk'``     | Asterisk                               |
+--------------------------+----------------------------------------+
| ``'SystemExclamation'``  | Exclamation                            |
+--------------------------+----------------------------------------+
| ``'SystemExit'``         | Exit Windows                           |
+--------------------------+----------------------------------------+
| ``'SystemHand'``         | Critical Stop                          |
+--------------------------+----------------------------------------+
| ``'SystemQuestion'``     | Question                               |
+--------------------------+----------------------------------------+

For example::

import winsound
# Play Windows exit sound.
winsound.PlaySound("SystemExit", winsound.SND_ALIAS)

# Probably play Windows default sound, if any is registered (because
# "*" probably isn't the registered name of any sound).
winsound.PlaySound("*", winsound.SND_ALIAS)


"""
SND_ALIAS = None
"""
Play the sound repeatedly.  The :const:`SND_ASYNC` flag must also be used to
avoid blocking.  Cannot be used with :const:`SND_MEMORY`.


"""
SND_LOOP = None
"""
The *sound* parameter to :func:`PlaySound` is a memory image of a WAV file, as a
string.

"""
SND_MEMORY = None
"""
Stop playing all instances of the specified sound.

"""
SND_PURGE = None
"""
Return immediately, allowing sounds to play asynchronously.


"""
SND_ASYNC = None
"""
If the specified sound cannot be found, do not play the system default sound.


"""
SND_NODEFAULT = None
"""
Do not interrupt sounds currently playing.


"""
SND_NOSTOP = None
"""
Return immediately if the sound driver is busy.


"""
SND_NOWAIT = None
"""
Play the ``SystemDefault`` sound.


"""
MB_ICONASTERISK = None
"""
Play the ``SystemExclamation`` sound.


"""
MB_ICONEXCLAMATION = None
"""
Play the ``SystemHand`` sound.


"""
MB_ICONHAND = None
"""
Play the ``SystemQuestion`` sound.


"""
MB_ICONQUESTION = None
def Beep(frequency,duration):
	"""
	Beep the PC's speaker. The *frequency* parameter specifies frequency, in hertz,
	of the sound, and must be in the range 37 through 32,767. The *duration*
	parameter specifies the number of milliseconds the sound should last.  If the
	system is not able to beep the speaker, :exc:`RuntimeError` is raised.
	
	"""
	pass
	
def PlaySound(sound,flags):
	"""
	Call the underlying :cfunc:`PlaySound` function from the Platform API.  The
	*sound* parameter may be a filename, audio data as a string, or ``None``.  Its
	interpretation depends on the value of *flags*, which can be a bitwise ORed
	combination of the constants described below. If the *sound* parameter is
	``None``, any currently playing waveform sound is stopped. If the system
	indicates an error, :exc:`RuntimeError` is raised.
	
	
	"""
	pass
	
def MessageBeep(type=MB_OK):
	"""
	Call the underlying :cfunc:`MessageBeep` function from the Platform API.  This
	plays a sound as specified in the registry.  The *type* argument specifies which
	sound to play; possible values are ``-1``, ``MB_ICONASTERISK``,
	``MB_ICONEXCLAMATION``, ``MB_ICONHAND``, ``MB_ICONQUESTION``, and ``MB_OK``, all
	described below.  The value ``-1`` produces a "simple beep"; this is the final
	fallback if a sound cannot be played otherwise.
	
	"""
	pass
	
