#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
""":platform: Mac
:synopsis: Access to the Mac OS X Internet Config.
:deprecated:


This module provides access to various internet-related preferences set through
:program:`System Preferences` or the :program:`Finder`.

"""
class IC:


	"""
	Create an Internet Config object. The signature is a 4-character creator code of
	the current application (default ``'Pyth'``) which may influence some of ICs
	settings. The optional *ic* argument is a low-level ``icglue.icinstance``
	created beforehand, this may be useful if you want to get preferences from a
	different config file, etc.
	
	
	"""
	
	
	def __init__(self, signature,ic):
		pass
	
	def launchurl(url,hint):
		"""parseurl(data[, start[, end[, hint]]])
		mapfile(file)
		maptypecreator(type, creator[, filename])
		settypecreator(file)
		
		These functions are "shortcuts" to the methods of the same name, described
		below.
		
		
		IC Objects
		----------
		
		:class:`IC` objects have a mapping interface, hence to obtain the mail address
		you simply get ``ic['MailAddress']``. Assignment also works, and changes the
		option in the configuration file.
		
		The module knows about various datatypes, and converts the internal IC
		representation to a "logical" Python data structure. Running the :mod:`ic`
		module standalone will run a test program that lists all keys and values in your
		IC database, this will have to serve as documentation.
		
		If the module does not know how to represent the data it returns an instance of
		the ``ICOpaqueData`` type, with the raw data in its :attr:`data` attribute.
		Objects of this type are also acceptable values for assignment.
		
		Besides the dictionary interface, :class:`IC` objects have the following
		methods:
		
		
		"""
		pass
		
	


