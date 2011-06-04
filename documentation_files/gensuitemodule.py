#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
""":platform: Mac
:synopsis: Create a stub package from an OSA dictionary
"""
def is_scriptable(application):
	"""
	Returns true if ``application``, which should be passed as a pathname, appears
	to be scriptable. Take the return value with a grain of salt: :program:`Internet
	Explorer` appears not to be scriptable but definitely is.
	
	
	"""
	pass
	
def processfile(application,output,basepkgname,edit_modnames,creatorsignature,dump,verbose):
	"""
	Create a stub package for ``application``, which should be passed as a full
	pathname. For a :file:`.app` bundle this is the pathname to the bundle, not to
	the executable inside the bundle; for an unbundled CFM application you pass the
	filename of the application binary.
	
	This function asks the application for its OSA terminology resources, decodes
	these resources and uses the resultant data to create the Python code for the
	package implementing the client stubs.
	
	``output`` is the pathname where the resulting package is stored, if not
	specified a standard "save file as" dialog is presented to the user.
	``basepkgname`` is the base package on which this package will build, and
	defaults to :mod:`StdSuites`. Only when generating :mod:`StdSuites` itself do
	you need to specify this. ``edit_modnames`` is a dictionary that can be used to
	change modulenames that are too ugly after name mangling. ``creator_signature``
	can be used to override the 4-char creator code, which is normally obtained from
	the :file:`PkgInfo` file in the package or from the CFM file creator signature.
	When ``dump`` is given it should refer to a file object, and ``processfile``
	will stop after decoding the resources and dump the Python representation of the
	terminology resources to this file. ``verbose`` should also be a file object,
	and specifying it will cause ``processfile`` to tell you what it is doing.
	
	
	"""
	pass
	
