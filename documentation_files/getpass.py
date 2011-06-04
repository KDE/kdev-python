#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
""":synopsis: Portable reading of passwords and retrieval of the userid.
"""
def getpass(prompt,stream):
	"""
	Prompt the user for a password without echoing.  The user is prompted using the
	string *prompt*, which defaults to ``'Password: '``. On Unix, the prompt is
	written to the file-like object *stream*.  *stream* defaults to the
	controlling terminal (/dev/tty) or if that is unavailable to ``sys.stderr``
	(this argument is ignored on Windows).
	
	If echo free input is unavailable getpass() falls back to printing
	a warning message to *stream* and reading from ``sys.stdin`` and
	issuing a :exc:`GetPassWarning`.
	
	Availability: Macintosh, Unix, Windows.
	
	"""
	pass
	
