#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
""":platform: IRIX
:synopsis: Audio functions on the SGI.
:deprecated:

"""
def openport(name,direction,config):
	"""
	The name and direction arguments are strings.  The optional *config* argument is
	a configuration object as returned by :func:`newconfig`.  The return value is an
	:dfn:`audio port object`; methods of audio port objects are described below.
	
	
	"""
	pass
	
def newconfig():
	"""
	The return value is a new :dfn:`audio configuration object`; methods of audio
	configuration objects are described below.
	
	
	"""
	pass
	
def queryparams(device):
	"""
	The device argument is an integer.  The return value is a list of integers
	containing the data returned by :cfunc:`ALqueryparams`.
	
	
	"""
	pass
	
def getparams(device,list):
	"""
	The *device* argument is an integer.  The list argument is a list such as
	returned by :func:`queryparams`; it is modified in place (!).
	
	
	"""
	pass
	
def setparams(device,list):
	"""
	The *device* argument is an integer.  The *list* argument is a list such as
	returned by :func:`queryparams`.
	
	
	.. onfiguration Objects
	---------------------
	
	Configuration objects returned by :func:`newconfig` have the following methods:
	
	
	"""
	pass
	
