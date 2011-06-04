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
	
	
	def __init__(self, ):
		pass
	
	def defaults(self, ):
		"""
		Return a dictionary containing the instance-wide defaults.
		
		
		"""
		pass
		
	def sections(self, ):
		"""
		Return a list of the sections available; ``DEFAULT`` is not included in the
		list.
		
		
		"""
		pass
		
	def add_section(self, section):
		"""
		Add a section named *section* to the instance.  If a section by the given name
		already exists, :exc:`DuplicateSectionError` is raised. If the name
		``DEFAULT`` (or any of it's case-insensitive variants) is passed,
		:exc:`ValueError` is raised.
		
		"""
		pass
		
	def has_section(self, section):
		"""
		Indicates whether the named section is present in the configuration. The
		``DEFAULT`` section is not acknowledged.
		
		
		"""
		pass
		
	def options(self, section):
		"""
		Returns a list of options available in the specified *section*.
		
		
		"""
		pass
		
	def has_option(self, section,option):
		"""
		If the given section exists, and contains the given option, return
		:const:`True`; otherwise return :const:`False`.
		
		"""
		pass
		
	def read(self, filenames):
		"""
		Attempt to read and parse a list of filenames, returning a list of filenames
		which were successfully parsed.  If *filenames* is a string or Unicode string,
		it is treated as a single filename. If a file named in *filenames* cannot be
		opened, that file will be ignored.  This is designed so that you can specify a
		list of potential configuration file locations (for example, the current
		directory, the user's home directory, and some system-wide directory), and all
		existing configuration files in the list will be read.  If none of the named
		files exist, the :class:`ConfigParser` instance will contain an empty dataset.
		An application which requires initial values to be loaded from a file should
		load the required file or files using :meth:`readfp` before calling :meth:`read`
		for any optional files::
		
		import ConfigParser, os
		
		config = ConfigParser.ConfigParser()
		config.readfp(open('defaults.cfg'))
		config.read(['site.cfg', os.path.expanduser('~/.myapp.cfg')])
		
		"""
		pass
		
	def readfp(self, fp,filename):
		"""
		Read and parse configuration data from the file or file-like object in *fp*
		(only the :meth:`readline` method is used).  If *filename* is omitted and *fp*
		has a :attr:`name` attribute, that is used for *filename*; the default is
		``<???>``.
		
		
		"""
		pass
		
	def get(self, section,option):
		"""
		Get an *option* value for the named *section*.
		
		
		"""
		pass
		
	def getint(self, section,option):
		"""
		A convenience method which coerces the *option* in the specified *section* to an
		integer.
		
		
		"""
		pass
		
	def getfloat(self, section,option):
		"""
		A convenience method which coerces the *option* in the specified *section* to a
		floating point number.
		
		
		"""
		pass
		
	def getboolean(self, section,option):
		"""
		A convenience method which coerces the *option* in the specified *section* to a
		Boolean value.  Note that the accepted values for the option are ``"1"``,
		``"yes"``, ``"true"``, and ``"on"``, which cause this method to return ``True``,
		and ``"0"``, ``"no"``, ``"false"``, and ``"off"``, which cause it to return
		``False``.  These string values are checked in a case-insensitive manner.  Any
		other value will cause it to raise :exc:`ValueError`.
		
		
		"""
		pass
		
	def items(self, section):
		"""
		Return a list of ``(name, value)`` pairs for each option in the given *section*.
		
		
		"""
		pass
		
	def set(self, section,option,value):
		"""
		If the given section exists, set the given option to the specified value;
		otherwise raise :exc:`NoSectionError`.  While it is possible to use
		:class:`RawConfigParser` (or :class:`ConfigParser` with *raw* parameters set to
		true) for *internal* storage of non-string values, full functionality (including
		interpolation and output to files) can only be achieved using string values.
		
		"""
		pass
		
	def write(self, fileobject):
		"""
		Write a representation of the configuration to the specified file object.  This
		representation can be parsed by a future :meth:`read` call.
		
		"""
		pass
		
	def remove_option(self, section,option):
		"""
		Remove the specified *option* from the specified *section*. If the section does
		not exist, raise :exc:`NoSectionError`.  If the option existed to be removed,
		return :const:`True`; otherwise return :const:`False`.
		
		"""
		pass
		
	def remove_section(self, section):
		"""
		Remove the specified *section* from the configuration. If the section in fact
		existed, return ``True``. Otherwise return ``False``.
		
		
		"""
		pass
		
	def optionxform(self, option):
		"""
		Transforms the option name *option* as found in an input file or as passed in
		by client code to the form that should be used in the internal structures.
		The default implementation returns a lower-case version of *option*;
		subclasses may override this or client code can set an attribute of this name
		on instances to affect this behavior.
		
		You don't necessarily need to subclass a ConfigParser to use this method, you
		can also re-set it on an instance, to a function that takes a string
		argument.  Setting it to ``str``, for example, would make option names case
		sensitive::
		
		cfgparser = ConfigParser()
		*more
		cfgparser.optionxform = str
		
		Note that when reading configuration files, whitespace around the
		option names are stripped before :meth:`optionxform` is called.
		
		
		.. onfigParser Objects
		--------------------
		
		The :class:`ConfigParser` class extends some methods of the
		:class:`RawConfigParser` interface, adding some optional arguments.
		
		
		"""
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
	
	
	def __init__(self, ):
		pass
	
	def get(self, section,option,raw,vars):
		"""
		Get an *option* value for the named *section*.  If *vars* is provided, it
		must be a dictionary.  The *option* is looked up in *vars* (if provided),
		*section*, and in *defaults* in that order.
		
		All the ``'%'`` interpolations are expanded in the return values, unless the
		*raw* argument is true.  Values for interpolation keys are looked up in the
		same manner as the option.
		
		"""
		pass
		
	def items(self, section,raw,vars):
		"""
		Return a list of ``(name, value)`` pairs for each option in the given *section*.
		Optional arguments have the same meaning as for the :meth:`get` method.
		
		"""
		pass
		
	


class SafeConfigParser:


	"""
	Derived class of :class:`ConfigParser` that implements a more-sane variant of
	the magical interpolation feature.  This implementation is more predictable as
	well. New applications should prefer this version if they don't need to be
	compatible with older versions of Python.
	
	.. o explain what's safer/more predictable about it.
	
	"""
	
	
	def __init__(self, ):
		pass
	
	def set(self, section,option,value):
		"""
		If the given section exists, set the given option to the specified value;
		otherwise raise :exc:`NoSectionError`.  *value* must be a string (:class:`str`
		or :class:`unicode`); if not, :exc:`TypeError` is raised.
		
		"""
		pass
		
	"""
	The maximum depth for recursive interpolation for :meth:`get` when the *raw*
	parameter is false.  This is relevant only for the :class:`ConfigParser` class.
	
	
	"""
	MAX_INTERPOLATION_DEPTH = None
	


