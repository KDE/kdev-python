#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
""":platform: Unix
:synopsis: A Python interface to Unix shell pipelines.
"""
class Template:


	"""
	An abstraction of a pipeline.
	
	Example::
	
	>>> import pipes
	>>> t=pipes.Template()
	>>> t.append('tr a-z A-Z', '--')
	>>> f=t.open('/tmp/1', 'w')
	>>> f.write('hello world')
	>>> f.close()
	>>> open('/tmp/1').read()
	'HELLO WORLD'
	
	
	.. emplate Objects
	----------------
	
	Template objects following methods:
	
	
	"""
	
	
	def __init__(self, ):
		pass
	
	def reset(self, ):
		"""
		Restore a pipeline template to its initial state.
		
		
		"""
		pass
		
	def clone(self, ):
		"""
		Return a new, equivalent, pipeline template.
		
		
		"""
		pass
		
	def debug(self, flag):
		"""
		If *flag* is true, turn debugging on. Otherwise, turn debugging off. When
		debugging is on, commands to be executed are printed, and the shell is given
		``set -x`` command to be more verbose.
		
		
		"""
		pass
		
	def append(self, cmd,kind):
		"""
		Append a new action at the end. The *cmd* variable must be a valid bourne shell
		command. The *kind* variable consists of two letters.
		
		The first letter can be either of ``'-'`` (which means the command reads its
		standard input), ``'f'`` (which means the commands reads a given file on the
		command line) or ``'.'`` (which means the commands reads no input, and hence
		must be first.)
		
		Similarly, the second letter can be either of ``'-'`` (which means  the command
		writes to standard output), ``'f'`` (which means the  command writes a file on
		the command line) or ``'.'`` (which means the command does not write anything,
		and hence must be last.)
		
		
		"""
		pass
		
	def prepend(self, cmd,kind):
		"""
		Add a new action at the beginning. See :meth:`append` for explanations of the
		arguments.
		
		
		"""
		pass
		
	def open(self, file,mode):
		"""
		Return a file-like object, open to *file*, but read from or written to by the
		pipeline.  Note that only one of ``'r'``, ``'w'`` may be given.
		
		
		"""
		pass
		
	


