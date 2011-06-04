#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
""":synopsis: DBM-style interface to the BSD database library.
"""
def open(path,flag,mode):
	"""
	Open a ``db`` database and return the database object.  The *path* argument is
	the name of the database file.
	
	The *flag* argument can be:
	
	+---------+-------------------------------------------+
	| Value   | Meaning                                   |
	+=========+===========================================+
	| ``'r'`` | Open existing database for reading only   |
	|         | (default)                                 |
	+---------+-------------------------------------------+
	| ``'w'`` | Open existing database for reading and    |
	|         | writing                                   |
	+---------+-------------------------------------------+
	| ``'c'`` | Open database for reading and writing,    |
	|         | creating it if it doesn't exist           |
	+---------+-------------------------------------------+
	| ``'n'`` | Always create a new, empty database, open |
	|         | for reading and writing                   |
	+---------+-------------------------------------------+
	
	For platforms on which the BSD ``db`` library supports locking, an ``'l'``
	can be appended to indicate that locking should be used.
	
	The optional *mode* parameter is used to indicate the Unix permission bits that
	should be set if a new database must be created; this will be masked by the
	current umask value for the process.
	
	
	"""
	pass
	
