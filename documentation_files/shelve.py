#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
""":synopsis: Python object persistence.


"""
def open(filename,flag='c',protocol=None,writeback=False):
	"""
	Open a persistent dictionary.  The filename specified is the base filename for
	the underlying database.  As a side-effect, an extension may be added to the
	filename and more than one file may be created.  By default, the underlying
	database file is opened for reading and writing.  The optional *flag* parameter
	has the same interpretation as the *flag* parameter of :func:`anydbm.open`.
	
	By default, version 0 pickles are used to serialize values.  The version of the
	pickle protocol can be specified with the *protocol* parameter.
	
	"""
	pass
	
class Shelf:


	"""
	A subclass of :class:`UserDict.DictMixin` which stores pickled values in the
	*dict* object.
	
	By default, version 0 pickles are used to serialize values.  The version of the
	pickle protocol can be specified with the *protocol* parameter. See the
	:mod:`pickle` documentation for a discussion of the pickle protocols.
	
	"""
	
	
	def __init__(self, dict,protocol=None,writeback=False):
		pass
	
	


class BsdDbShelf:


	"""
	A subclass of :class:`Shelf` which exposes :meth:`first`, :meth:`!next`,
	:meth:`previous`, :meth:`last` and :meth:`set_location` which are available in
	the :mod:`bsddb` module but not in other database modules.  The *dict* object
	passed to the constructor must support those methods.  This is generally
	accomplished by calling one of :func:`bsddb.hashopen`, :func:`bsddb.btopen` or
	:func:`bsddb.rnopen`.  The optional *protocol* and *writeback* parameters have
	the same interpretation as for the :class:`Shelf` class.
	
	
	"""
	
	
	def __init__(self, dict,protocol=None,writeback=False):
		pass
	
	


class DbfilenameShelf:


	"""
	A subclass of :class:`Shelf` which accepts a *filename* instead of a dict-like
	object.  The underlying file will be opened using :func:`anydbm.open`.  By
	default, the file will be created and opened for both read and write.  The
	optional *flag* parameter has the same interpretation as for the :func:`.open`
	function.  The optional *protocol* and *writeback* parameters have the same
	interpretation as for the :class:`Shelf` class.
	
	
	.. xample
	-------
	
	To summarize the interface (``key`` is a string, ``data`` is an arbitrary
	object)::
	
	import shelve
	
	d = shelve.open(filename) # open -- file may get suffix added by low-level
	# library
	
	d[key] = data   # store data at key (overwrites old data if
	# using an existing key)
	data = d[key]   # retrieve a COPY of data at key (raise KeyError if no
	# such key)
	del d[key]      # delete data stored at key (raises KeyError
	# if no such key)
	flag = d.has_key(key)   # true if the key exists
	klist = d.keys() # a list of all existing keys (slow!)
	
	# as d was opened WITHOUT writeback=True, beware:
	d['xx'] = range(4)  # this works as expected, but*more
	d['xx'].append(5)   # *this doesn't!* -- d['xx'] is STILL range(4)!
	
	# having opened d without writeback=True, you need to code carefully:
	temp = d['xx']      # extracts the copy
	temp.append(5)      # mutates the copy
	d['xx'] = temp      # stores the copy right back, to persist it
	
	# or, d=shelve.open(filename,writeback=True) would let you just code
	# d['xx'].append(5) and have it work as expected, BUT it would also
	# consume more memory and make the d.close() operation slower.
	
	d.close()       # close it
	
	
	"""
	
	
	def __init__(self, filename,flag='c',protocol=None,writeback=False):
		pass
	
	


