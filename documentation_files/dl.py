#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
""":platform: Unix
:synopsis: Call C functions in shared objects.
:deprecated:

"""
"""
Useful as an argument to :func:`.open`.


"""
RTLD_LAZY = None
"""
Useful as an argument to :func:`.open`.  Note that on systems which do not
support immediate binding, this constant will not appear in the module. For
maximum portability, use :func:`hasattr` to determine if the system supports
immediate binding.

The :mod:`dl` module defines the following exception:


"""
RTLD_NOW = None
def open(name,mode=RTLD_LAZY):
	"""
	Open a shared object file, and return a handle. Mode signifies late binding
	(:const:`RTLD_LAZY`) or immediate binding (:const:`RTLD_NOW`). Default is
	:const:`RTLD_LAZY`. Note that some systems do not support :const:`RTLD_NOW`.
	
	Return value is a :class:`dlobject`.
	
	The :mod:`dl` module defines the following constants:
	
	
	"""
	pass
	
