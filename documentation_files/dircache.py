#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
""":synopsis: Return directory listing, with cache mechanism.
:deprecated:

"""
def reset():
	"""
	Resets the directory cache.
	
	
	"""
	pass
	
def listdir(path):
	"""
	Return a directory listing of *path*, as gotten from :func:`os.listdir`. Note
	that unless *path* changes, further call to :func:`listdir` will not re-read the
	directory structure.
	
	Note that the list returned should be regarded as read-only. (Perhaps a future
	version should change it to return a tuple?)
	
	
	"""
	pass
	
def opendir(path):
	"""
	Same as :func:`listdir`. Defined for backwards compatibility.
	
	
	"""
	pass
	
