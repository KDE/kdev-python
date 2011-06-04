#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
""":synopsis: Loading of .netrc files.
"""
class netrc:


	"""
	A :class:`netrc` instance or subclass instance encapsulates data from  a netrc
	file.  The initialization argument, if present, specifies the file to parse.  If
	no argument is given, the file :file:`.netrc` in the user's home directory will
	be read.  Parse errors will raise :exc:`NetrcParseError` with diagnostic
	information including the file name, line number, and terminating token.
	
	
	"""
	
	
	def __init__(self, ):
		pass
	
	def authenticators(self, host):
		"""
		Return a 3-tuple ``(login, account, password)`` of authenticators for *host*.
		If the netrc file did not contain an entry for the given host, return the tuple
		associated with the 'default' entry.  If neither matching host nor default entry
		is available, return ``None``.
		
		
		"""
		pass
		
	def __repr__(self, ):
		"""
		Dump the class data as a string in the format of a netrc file. (This discards
		comments and may reorder the entries.)
		
		Instances of :class:`netrc` have public instance variables:
		
		
		"""
		pass
		
	


