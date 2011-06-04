#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
""":synopsis: Command-line option parsing library.
:deprecated:

"""
class OptionGroup:


	"""
	where
	
	* parser is the :class:`OptionParser` instance the group will be insterted in
	to
	* title is the group title
	* description, optional, is a long description of the group
	
	:class:`OptionGroup` inherits from :class:`OptionContainer` (like
	:class:`OptionParser`) and so the :meth:`add_option` method can be used to add
	an option to the group.
	
	Once all the options are declared, using the :class:`OptionParser` method
	:meth:`add_option_group` the group is added to the previously defined parser.
	
	Continuing with the parser defined in the previous section, adding an
	:class:`OptionGroup` to a parser is easy::
	
	group = OptionGroup(parser, "Dangerous Options",
	"Caution: use these options at your own risk.  "
	"It is believed that some of them bite.")
	group.add_option("-g", action="store_true", help="Group option.")
	parser.add_option_group(group)
	
	This would result in the following help output:
	
	"""
	
	
	def __init__(self, parser,title,description=None):
		pass
	
	


class OptionParser:


	"""
	The OptionParser constructor has no required arguments, but a number of
	optional keyword arguments.  You should always pass them as keyword
	arguments, i.e. do not rely on the order in which the arguments are declared.
	
	``usage`` (default: ``"%prog [options]"``)
	The usage summary to print when your program is run incorrectly or with a
	help option.  When :mod:`optparse` prints the usage string, it expands
	``%prog`` to ``os.path.basename(sys.argv[0])`` (or to ``prog`` if you
	passed that keyword argument).  To suppress a usage message, pass the
	special value :data:`optparse.SUPPRESS_USAGE`.
	
	``option_list`` (default: ``[]``)
	A list of Option objects to populate the parser with.  The options in
	``option_list`` are added after any options in ``standard_option_list`` (a
	class attribute that may be set by OptionParser subclasses), but before
	any version or help options. Deprecated; use :meth:`add_option` after
	creating the parser instead.
	
	``option_class`` (default: optparse.Option)
	Class to use when adding options to the parser in :meth:`add_option`.
	
	``version`` (default: ``None``)
	A version string to print when the user supplies a version option. If you
	supply a true value for ``version``, :mod:`optparse` automatically adds a
	version option with the single option string ``--version``.  The
	substring ``%prog`` is expanded the same as for ``usage``.
	
	``conflict_handler`` (default: ``"error"``)
	Specifies what to do when options with conflicting option strings are
	added to the parser; see section
	:ref:`optparse-conflicts-between-options`.
	
	``description`` (default: ``None``)
	A paragraph of text giving a brief overview of your program.
	:mod:`optparse` reformats this paragraph to fit the current terminal width
	and prints it when the user requests help (after ``usage``, but before the
	list of options).
	
	``formatter`` (default: a new :class:`IndentedHelpFormatter`)
	An instance of optparse.HelpFormatter that will be used for printing help
	text.  :mod:`optparse` provides two concrete classes for this purpose:
	IndentedHelpFormatter and TitledHelpFormatter.
	
	``add_help_option`` (default: ``True``)
	If true, :mod:`optparse` will add a help option (with option strings ``-h``
	and ``--help``) to the parser.
	
	``prog``
	The string to use when expanding ``%prog`` in ``usage`` and ``version``
	instead of ``os.path.basename(sys.argv[0])``.
	
	``epilog`` (default: ``None``)
	A paragraph of help text to print after the option help.
	
	.. opulating the parser
	^^^^^^^^^^^^^^^^^^^^^
	
	There are several ways to populate the parser with options.  The preferred way
	is by using :meth:`OptionParser.add_option`, as shown in section
	:ref:`optparse-tutorial`.  :meth:`add_option` can be called in one of two ways:
	
	* pass it an Option instance (as returned by :func:`make_option`)
	
	* pass it any combination of positional and keyword arguments that are
	acceptable to :func:`make_option` (i.e., to the Option constructor), and it
	will create the Option instance for you
	
	The other alternative is to pass a list of pre-constructed Option instances to
	the OptionParser constructor, as in::
	
	option_list = [
	make_option("-f", "--filename",
	action="store", type="string", dest="filename"),
	make_option("-q", "--quiet",
	action="store_false", dest="verbose"),
	]
	parser = OptionParser(option_list=option_list)
	
	(:func:`make_option` is a factory function for creating Option instances;
	currently it is an alias for the Option constructor.  A future version of
	:mod:`optparse` may split Option into several classes, and :func:`make_option`
	will pick the right class to instantiate.  Do not instantiate Option directly.)
	
	
	.. efining options
	^^^^^^^^^^^^^^^^
	
	Each Option instance represents a set of synonymous command-line option strings,
	e.g. ``-f`` and ``--file``.  You can specify any number of short or
	long option strings, but you must specify at least one overall option string.
	
	The canonical way to create an :class:`Option` instance is with the
	:meth:`add_option` method of :class:`OptionParser`.
	
	"""
	
	
	def __init__(self, more):
		pass
	
	


