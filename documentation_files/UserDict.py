#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
""":synopsis: Class wrapper for dictionary objects.


The module defines a mixin,  :class:`DictMixin`, defining all dictionary methods
for classes that already have a minimum mapping interface.  This greatly
simplifies writing classes that need to be substitutable for dictionaries (such
as the shelve module).

This module also defines a class, :class:`UserDict`, that acts as a wrapper
around dictionary objects.  The need for this class has been largely supplanted
by the ability to subclass directly from :class:`dict` (a feature that became
available starting with Python version 2.2).  Prior to the introduction of
:class:`dict`, the :class:`UserDict` class was used to create dictionary-like
sub-classes that obtained new behaviors by overriding existing methods or adding
new ones.

"""
class UserDict:


	"""
	Class that simulates a dictionary.  The instance's contents are kept in a
	regular dictionary, which is accessible via the :attr:`data` attribute of
	:class:`UserDict` instances.  If *initialdata* is provided, :attr:`data` is
	initialized with its contents; note that a reference to *initialdata* will not
	be kept, allowing it be used for other purposes.
	
	"""
	
	
	def __init__(self, ):
		pass
	
	


class IterableUserDict:


	"""
	Subclass of :class:`UserDict` that supports direct iteration (e.g.  ``for key in
	myDict``).
	
	In addition to supporting the methods and operations of mappings (see section
	:ref:`typesmapping`), :class:`UserDict` and :class:`IterableUserDict` instances
	provide the following attribute:
	
	
	"""
	
	
	def __init__(self, ):
		pass
	
	


class DictMixin:


	"""
	Mixin defining all dictionary methods for classes that already have a minimum
	dictionary interface including :meth:`__getitem__`, :meth:`__setitem__`,
	:meth:`__delitem__`, and :meth:`keys`.
	
	This mixin should be used as a superclass.  Adding each of the above methods
	adds progressively more functionality.  For instance, defining all but
	:meth:`__delitem__` will preclude only :meth:`pop` and :meth:`popitem` from the
	full interface.
	
	In addition to the four base methods, progressively more efficiency comes with
	defining :meth:`__contains__`, :meth:`__iter__`, and :meth:`iteritems`.
	
	Since the mixin has no knowledge of the subclass constructor, it does not define
	:meth:`__init__` or :meth:`copy`.
	
	Starting with Python version 2.6, it is recommended to use
	:class:`collections.MutableMapping` instead of :class:`DictMixin`.
	
	:mod:`UserList` --- Class wrapper for list objects
	==================================================
	
	"""
	
	
	def __init__(self, ):
		pass
	
	


