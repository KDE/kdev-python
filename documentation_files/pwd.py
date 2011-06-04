#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
""":platform: Unix
:synopsis: The password database (getpwnam() and friends).


This module provides access to the Unix user account and password database.  It
is available on all Unix versions.

Password database entries are reported as a tuple-like object, whose attributes
correspond to the members of the ``passwd`` structure (Attribute field below,
see ``<pwd.h>``):

+-------+---------------+-----------------------------+
| Index | Attribute     | Meaning                     |
+=======+===============+=============================+
| 0     | ``pw_name``   | Login name                  |
+-------+---------------+-----------------------------+
| 1     | ``pw_passwd`` | Optional encrypted password |
+-------+---------------+-----------------------------+
| 2     | ``pw_uid``    | Numerical user ID           |
+-------+---------------+-----------------------------+
| 3     | ``pw_gid``    | Numerical group ID          |
+-------+---------------+-----------------------------+
| 4     | ``pw_gecos``  | User name or comment field  |
+-------+---------------+-----------------------------+
| 5     | ``pw_dir``    | User home directory         |
+-------+---------------+-----------------------------+
| 6     | ``pw_shell``  | User command interpreter    |
+-------+---------------+-----------------------------+

The uid and gid items are integers, all others are strings. :exc:`KeyError` is
raised if the entry asked for cannot be found.

"""
def getpwuid(uid):
	"""
	Return the password database entry for the given numeric user ID.
	
	
	"""
	pass
	
def getpwnam(name):
	"""
	Return the password database entry for the given user name.
	
	
	"""
	pass
	
def getpwall():
	"""
	Return a list of all available password database entries, in arbitrary order.
	
	
	"""
	pass
	
