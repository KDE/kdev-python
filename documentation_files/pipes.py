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
	
	


