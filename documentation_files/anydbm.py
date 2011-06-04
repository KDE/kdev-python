#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
""":synopsis: Generic interface to DBM-style database modules.


"""
def open(filename,flag,mode):
	"""
	Open the database file *filename* and return a corresponding object.
	
	If the database file already exists, the :mod:`whichdb` module is used to
	determine its type and the appropriate module is used; if it does not exist,
	the first module listed above that can be imported is used.
	
	The optional *flag* argument must be one of these values:
	
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
	
	If not specified, the default value is ``'r'``.
	
	The optional *mode* argument is the Unix mode of the file, used only when the
	database has to be created.  It defaults to octal ``0666`` (and will be
	modified by the prevailing umask).
	
	
	"""
	pass
	
