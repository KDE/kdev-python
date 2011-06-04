#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
""":synopsis: Configuration file parser.

"""
class RawConfigParser:


	"""
	The basic configuration object.  When *defaults* is given, it is initialized
	into the dictionary of intrinsic defaults.  When *dict_type* is given, it will
	be used to create the dictionary objects for the list of sections, for the
	options within a section, and for the default values.  When *allow_no_value*
	is true (default: ``False``), options without values are accepted; the value
	presented for these is ``None``.
	
	This class does not
	support the magical interpolation behavior.
	
	All option names are passed through the :meth:`optionxform` method.  Its
	default implementation converts option names to lower case.
	
	"""
	
	
	def __init__(self, defaults,dict_type,allow_no_value):
		pass
	
	


class ConfigParser:


	"""
	Derived class of :class:`RawConfigParser` that implements the magical
	interpolation feature and adds optional arguments to the :meth:`get` and
	:meth:`items` methods.  The values in *defaults* must be appropriate for the
	``%()s`` string interpolation.  Note that *__name__* is an intrinsic default;
	its value is the section name, and will override any value provided in
	*defaults*.
	
	All option names used in interpolation will be passed through the
	:meth:`optionxform` method just like any other option name reference.  Using
	the default implementation of :meth:`optionxform`, the values ``foo %(bar)s``
	and ``foo %(BAR)s`` are equivalent.
	
	"""
	
	
	def __init__(self, defaults,dict_type,allow_no_value):
		pass
	
	


class SafeConfigParser:


	"""
	Derived class of :class:`ConfigParser` that implements a more-sane variant of
	the magical interpolation feature.  This implementation is more predictable as
	well. New applications should prefer this version if they don't need to be
	compatible with older versions of Python.
	
	.. o explain what's safer/more predictable about it.
	
	"""
	
	
	def __init__(self, defaults,dict_type,allow_no_value):
		pass
	
	"""
	The maximum depth for recursive interpolation for :meth:`get` when the *raw*
	parameter is false.  This is relevant only for the :class:`ConfigParser` class.
	
	
	"""
	MAX_INTERPOLATION_DEPTH = None
	


