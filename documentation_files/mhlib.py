#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
""":synopsis: Manipulate MH mailboxes from Python.
:deprecated:

"""
class MH:


	"""
	:class:`MH` represents a collection of MH folders.
	
	
	"""
	
	
	def __init__(self, ):
		pass
	
	def error(self, format,more):
		"""
		Print an error message -- can be overridden.
		
		
		"""
		pass
		
	def getprofile(self, key):
		"""
		Return a profile entry (``None`` if not set).
		
		
		"""
		pass
		
	def getpath(self, ):
		"""
		Return the mailbox pathname.
		
		
		"""
		pass
		
	def getcontext(self, ):
		"""
		Return the current folder name.
		
		
		"""
		pass
		
	def setcontext(self, name):
		"""
		Set the current folder name.
		
		
		"""
		pass
		
	def listfolders(self, ):
		"""
		Return a list of top-level folders.
		
		
		"""
		pass
		
	def listallfolders(self, ):
		"""
		Return a list of all folders.
		
		
		"""
		pass
		
	def listsubfolders(self, name):
		"""
		Return a list of direct subfolders of the given folder.
		
		
		"""
		pass
		
	def listallsubfolders(self, name):
		"""
		Return a list of all subfolders of the given folder.
		
		
		"""
		pass
		
	def makefolder(self, name):
		"""
		Create a new folder.
		
		
		"""
		pass
		
	def deletefolder(self, name):
		"""
		Delete a folder -- must have no subfolders.
		
		
		"""
		pass
		
	def openfolder(self, name):
		"""
		Return a new open folder object.
		
		
		.. older Objects
		--------------
		
		:class:`Folder` instances represent open folders and have the following methods:
		
		
		"""
		pass
		
	


class Folder:


	"""
	The :class:`Folder` class represents a single folder and its messages.
	
	
	"""
	
	
	def __init__(self, ):
		pass
	
	def error(self, format,more):
		"""
		Print an error message -- can be overridden.
		
		
		"""
		pass
		
	def getfullname(self, ):
		"""
		Return the folder's full pathname.
		
		
		"""
		pass
		
	def getsequencesfilename(self, ):
		"""
		Return the full pathname of the folder's sequences file.
		
		
		"""
		pass
		
	def getmessagefilename(self, n):
		"""
		Return the full pathname of message *n* of the folder.
		
		
		"""
		pass
		
	def listmessages(self, ):
		"""
		Return a list of messages in the folder (as numbers).
		
		
		"""
		pass
		
	def getcurrent(self, ):
		"""
		Return the current message number.
		
		
		"""
		pass
		
	def setcurrent(self, n):
		"""
		Set the current message number to *n*.
		
		
		"""
		pass
		
	def parsesequence(self, seq):
		"""
		Parse msgs syntax into list of messages.
		
		
		"""
		pass
		
	def getlast(self, ):
		"""
		Get last message, or ``0`` if no messages are in the folder.
		
		
		"""
		pass
		
	def setlast(self, n):
		"""
		Set last message (internal use only).
		
		
		"""
		pass
		
	def getsequences(self, ):
		"""
		Return dictionary of sequences in folder.  The sequence names are used  as keys,
		and the values are the lists of message numbers in the sequences.
		
		
		"""
		pass
		
	def putsequences(self, dict):
		"""
		Return dictionary of sequences in folder name: list.
		
		
		"""
		pass
		
	def removemessages(self, list):
		"""
		Remove messages in list from folder.
		
		
		"""
		pass
		
	def refilemessages(self, list,tofolder):
		"""
		Move messages in list to other folder.
		
		
		"""
		pass
		
	def movemessage(self, n,tofolder,ton):
		"""
		Move one message to a given destination in another folder.
		
		
		"""
		pass
		
	def copymessage(self, n,tofolder,ton):
		"""
		Copy one message to a given destination in another folder.
		
		
		.. essage Objects
		---------------
		
		The :class:`Message` class adds one method to those of
		:class:`mimetools.Message`:
		
		
		"""
		pass
		
	


class Message:


	"""
	:class:`Message` objects represent individual messages in a folder.  The Message
	class is derived from :class:`mimetools.Message`.
	
	
	.. H Objects
	----------
	
	:class:`MH` instances have the following methods:
	
	
	"""
	
	
	def __init__(self, ):
		pass
	
	


