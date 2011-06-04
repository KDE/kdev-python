#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
""":synopsis: Interface to Berkeley DB database library
"""
def hashopen(filename,flag,mode,pgsize,ffactor,nelem,cachesize,lorder,hflags):
	"""
	Open the hash format file named *filename*.  Files never intended to be
	preserved on disk may be created by passing ``None`` as the  *filename*.  The
	optional *flag* identifies the mode used to open the file.  It may be ``'r'``
	(read only), ``'w'`` (read-write) , ``'c'`` (read-write - create if necessary;
	the default) or ``'n'`` (read-write - truncate to zero length).  The other
	arguments are rarely used and are just passed to the low-level :cfunc:`dbopen`
	function.  Consult the Berkeley DB documentation for their use and
	interpretation.
	
	
	"""
	pass
	
def btopen(filename,flag,mode,btflags,cachesize,maxkeypage,minkeypage,pgsize,lorder):
	"""
	Open the btree format file named *filename*.  Files never intended  to be
	preserved on disk may be created by passing ``None`` as the  *filename*.  The
	optional *flag* identifies the mode used to open the file.  It may be ``'r'``
	(read only), ``'w'`` (read-write), ``'c'`` (read-write - create if necessary;
	the default) or ``'n'`` (read-write - truncate to zero length).  The other
	arguments are rarely used and are just passed to the low-level dbopen function.
	Consult the Berkeley DB documentation for their use and interpretation.
	
	
	"""
	pass
	
def rnopen(filename,flag,mode,rnflags,cachesize,pgsize,lorder,rlen,delim,source,pad):
	"""
	Open a DB record format file named *filename*.  Files never intended  to be
	preserved on disk may be created by passing ``None`` as the  *filename*.  The
	optional *flag* identifies the mode used to open the file.  It may be ``'r'``
	(read only), ``'w'`` (read-write), ``'c'`` (read-write - create if necessary;
	the default) or ``'n'`` (read-write - truncate to zero length).  The other
	arguments are rarely used and are just passed to the low-level dbopen function.
	Consult the Berkeley DB documentation for their use and interpretation.
	
	"""
	pass
	
