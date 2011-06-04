#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
""":synopsis: Loads a robots.txt file and answers questions about
fetchability of other URLs.
"""
class RobotFileParser:


	"""
	This class provides a set of methods to read, parse and answer questions
	about a single :file:`robots.txt` file.
	
	
	"""
	
	
	def __init__(self, ):
		pass
	
	def set_url(self, url):
		"""
		Sets the URL referring to a :file:`robots.txt` file.
		
		
		"""
		pass
		
	def read(self, ):
		"""
		Reads the :file:`robots.txt` URL and feeds it to the parser.
		
		
		"""
		pass
		
	def parse(self, lines):
		"""
		Parses the lines argument.
		
		
		"""
		pass
		
	def can_fetch(self, useragent,url):
		"""
		Returns ``True`` if the *useragent* is allowed to fetch the *url*
		according to the rules contained in the parsed :file:`robots.txt`
		file.
		
		
		"""
		pass
		
	def mtime(self, ):
		"""
		Returns the time the ``robots.txt`` file was last fetched.  This is
		useful for long-running web spiders that need to check for new
		``robots.txt`` files periodically.
		
		
		"""
		pass
		
	def modified(self, ):
		"""
		Sets the time the ``robots.txt`` file was last fetched to the current
		time.
		
		The following example demonstrates basic use of the RobotFileParser class. ::
		"""
		pass
		
	


