#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
""":platform: Unix
:synopsis: The standard "database" interface, based on ndbm.

"""
"""
Name of the ``ndbm`` implementation library used.


"""
library = None
def open(filename,flag,mode):
	"""
	Open a dbm database and return a dbm object.  The *filename* argument is the
	name of the database file (without the :file:`.dir` or :file:`.pag` extensions;
	note that the BSD DB implementation of the interface will append the extension
	:file:`.db` and only create one file).
	
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
	
	The optional *mode* argument is the Unix mode of the file, used only when the
	database has to be created.  It defaults to octal ``0666`` (and will be
	modified by the prevailing umask).
	
	
	"""
	pass
	
