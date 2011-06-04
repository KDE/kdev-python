#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
""":platform: Mac
:synopsis: Wrappers around the finder's Apple Events interface.


"""
def launch(file):
	"""
	Tell the finder to launch *file*. What launching means depends on the file:
	applications are started, folders are opened and documents are opened in the
	correct application.
	
	
	"""
	pass
	
def Print(file):
	"""
	Tell the finder to print a file. The behaviour is identical to selecting the
	file and using the print command in the finder's file menu.
	
	
	"""
	pass
	
def copy(file,destdir):
	"""
	Tell the finder to copy a file or folder *file* to folder *destdir*. The
	function returns an :class:`Alias` object pointing to the new file.
	
	
	"""
	pass
	
def move(file,destdir):
	"""
	Tell the finder to move a file or folder *file* to folder *destdir*. The
	function returns an :class:`Alias` object pointing to the new file.
	
	
	"""
	pass
	
def sleep():
	"""
	Tell the finder to put the Macintosh to sleep, if your machine supports it.
	
	
	"""
	pass
	
def restart():
	"""
	Tell the finder to perform an orderly restart of the machine.
	
	
	"""
	pass
	
