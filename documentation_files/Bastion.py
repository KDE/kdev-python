#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
""":synopsis: Providing restricted access to objects.
:deprecated:

"""
def Bastion(object,filter,name,_class):
	"""
	Protect the object *object*, returning a bastion for the object.  Any attempt to
	access one of the object's attributes will have to be approved by the *filter*
	function; if the access is denied an :exc:`AttributeError` exception will be
	raised.
	
	If present, *filter* must be a function that accepts a string containing an
	attribute name, and returns true if access to that attribute will be permitted;
	if *filter* returns false, the access is denied.  The default filter denies
	access to any function beginning with an underscore (``'_'``).  The bastion's
	string representation will be ``<Bastion for name>`` if a value for *name* is
	provided; otherwise, ``repr(object)`` will be used.
	
	*class*, if present, should be a subclass of :class:`BastionClass`;  see the
	code in :file:`bastion.py` for the details.  Overriding the default
	:class:`BastionClass` will rarely be required.
	
	
	"""
	pass
	
