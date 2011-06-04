#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
""":platform: Unix
:synopsis: Interface to Sun's NIS (Yellow Pages) library.
"""
def match(key,mapname,domain=default_domain):
	"""
	Return the match for *key* in map *mapname*, or raise an error
	(:exc:`nis.error`) if there is none. Both should be strings, *key* is 8-bit
	clean. Return value is an arbitrary array of bytes (may contain ``NULL`` and
	other joys).
	
	Note that *mapname* is first checked if it is an alias to another name.
	
	"""
	pass
	
def cat(mapname,domain=default_domain):
	"""
	Return a dictionary mapping *key* to *value* such that ``match(key,
	mapname)==value``. Note that both keys and values of the dictionary are
	arbitrary arrays of bytes.
	
	Note that *mapname* is first checked if it is an alias to another name.
	
	"""
	pass
	
def maps(domain=default_domain):
	"""
	Return a list of all valid maps.
	
	"""
	pass
	
def get_default_domain():
	"""
	Return the system default NIS domain.
	
	"""
	pass
	
