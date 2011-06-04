#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
""":synopsis: Portable implementation of the simple DBM interface.

"""
def open(filename,flag,mode):
	"""
	Open a dumbdbm database and return a dumbdbm object.  The *filename* argument is
	the basename of the database file (without any specific extensions).  When a
	dumbdbm database is created, files with :file:`.dat` and :file:`.dir` extensions
	are created.
	
	The optional *flag* argument is currently ignored; the database is always opened
	for update, and will be created if it does not exist.
	
	The optional *mode* argument is the Unix mode of the file, used only when the
	database has to be created.  It defaults to octal ``0666`` (and will be modified
	by the prevailing umask).
	
	"""
	pass
	
