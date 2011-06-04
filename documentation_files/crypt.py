#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
""":platform: Unix
:synopsis: The crypt() function used to check Unix passwords.
"""
def crypt(word,salt):
	"""
	*word* will usually be a user's password as typed at a prompt or  in a graphical
	interface.  *salt* is usually a random two-character string which will be used
	to perturb the DES algorithm in one of 4096 ways.  The characters in *salt* must
	be in the set ``[./a-zA-Z0-9]``.  Returns the hashed password as a string, which
	will be composed of characters from the same alphabet as the salt (the first two
	characters represent the salt itself).
	
	"""
	pass
	
