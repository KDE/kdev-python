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
	
	
	def __init__(self, ):
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
	
	
	def __init__(self, ):
		pass
	
	def get_option_group(self, opt_str):
		"""
		Return, if defined, the :class:`OptionGroup` that has the title or the long
		description equals to *opt_str*
		
		.. rinting a version string
		^^^^^^^^^^^^^^^^^^^^^^^^^
		
		Similar to the brief usage string, :mod:`optparse` can also print a version
		string for your program.  You have to supply the string as the ``version``
		argument to OptionParser::
		
		parser = OptionParser(usage="%prog [-f] [-q]", version="%prog 1.0")
		
		``%prog`` is expanded just like it is in ``usage``.  Apart from that,
		``version`` can contain anything you like.  When you supply it, :mod:`optparse`
		automatically adds a ``--version`` option to your parser. If it encounters
		this option on the command line, it expands your ``version`` string (by
		replacing ``%prog``), prints it to stdout, and exits.
		
		For example, if your script is called ``/usr/bin/foo``::
		
		$ /usr/bin/foo --version
		foo 1.0
		
		The following two methods can be used to print and get the ``version`` string:
		
		"""
		pass
		
	def print_version(self, file=None):
		"""
		Print the version message for the current program (``self.version``) to
		*file* (default stdout).  As with :meth:`print_usage`, any occurrence
		of ``%prog`` in ``self.version`` is replaced with the name of the current
		program.  Does nothing if ``self.version`` is empty or undefined.
		
		"""
		pass
		
	def get_version(self, ):
		"""
		Same as :meth:`print_version` but returns the version string instead of
		printing it.
		
		
		.. ow :mod:`optparse` handles errors
		^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
		
		There are two broad classes of errors that :mod:`optparse` has to worry about:
		programmer errors and user errors.  Programmer errors are usually erroneous
		calls to :func:`OptionParser.add_option`, e.g. invalid option strings, unknown
		option attributes, missing option attributes, etc.  These are dealt with in the
		usual way: raise an exception (either :exc:`optparse.OptionError` or
		:exc:`TypeError`) and let the program crash.
		
		Handling user errors is much more important, since they are guaranteed to happen
		no matter how stable your code is.  :mod:`optparse` can automatically detect
		some user errors, such as bad option arguments (passing ``-n 4x`` where
		``-n`` takes an integer argument), missing arguments (``-n`` at the end
		of the command line, where ``-n`` takes an argument of any type).  Also,
		you can call :func:`OptionParser.error` to signal an application-defined error
		condition::
		
		(options, args) = parser.parse_args()
		[more]
		if options.a and options.b:
		parser.error("options -a and -b are mutually exclusive")
		
		In either case, :mod:`optparse` handles the error the same way: it prints the
		program's usage message and an error message to standard error and exits with
		error status 2.
		
		Consider the first example above, where the user passes ``4x`` to an option
		that takes an integer::
		
		$ /usr/bin/foo -n 4x
		Usage: foo [options]
		
		foo: error: option -n: invalid integer value: '4x'
		
		Or, where the user fails to pass a value at all::
		
		$ /usr/bin/foo -n
		Usage: foo [options]
		
		foo: error: -n option requires an argument
		
		:mod:`optparse`\ -generated error messages take care always to mention the
		option involved in the error; be sure to do the same when calling
		:func:`OptionParser.error` from your application code.
		
		If :mod:`optparse`'s default error-handling behaviour does not suit your needs,
		you'll need to subclass OptionParser and override its :meth:`~OptionParser.exit`
		and/or :meth:`~OptionParser.error` methods.
		
		
		.. utting it all together
		^^^^^^^^^^^^^^^^^^^^^^^
		
		Here's what :mod:`optparse`\ -based scripts usually look like::
		
		from optparse import OptionParser
		[more]
		def main():
		usage = "usage: %prog [options] arg"
		parser = OptionParser(usage)
		parser.add_option("-f", "--file", dest="filename",
		help="read data from FILENAME")
		parser.add_option("-v", "--verbose",
		action="store_true", dest="verbose")
		parser.add_option("-q", "--quiet",
		action="store_false", dest="verbose")
		[more]
		(options, args) = parser.parse_args()
		if len(args) != 1:
		parser.error("incorrect number of arguments")
		if options.verbose:
		print "reading %smore" % options.filename
		[more]
		
		if __name__ == "__main__":
		main()
		
		
		.. eference Guide
		---------------
		
		
		.. reating the parser
		^^^^^^^^^^^^^^^^^^^
		
		The first step in using :mod:`optparse` is to create an OptionParser instance.
		
		"""
		pass
		
	def add_option(self, opt_str,more,attr,more2):
		"""
		To define an option with only a short option string::
		
		parser.add_option("-f", attr=value, more)
		
		And to define an option with only a long option string::
		
		parser.add_option("--foo", attr=value, more)
		
		The keyword arguments define attributes of the new Option object.  The most
		important option attribute is :attr:`~Option.action`, and it largely
		determines which other attributes are relevant or required.  If you pass
		irrelevant option attributes, or fail to pass required ones, :mod:`optparse`
		raises an :exc:`OptionError` exception explaining your mistake.
		
		An option's *action* determines what :mod:`optparse` does when it encounters
		this option on the command-line.  The standard option actions hard-coded into
		:mod:`optparse` are:
		
		``"store"``
		store this option's argument (default)
		
		``"store_const"``
		store a constant value
		
		``"store_true"``
		store a true value
		
		``"store_false"``
		store a false value
		
		``"append"``
		append this option's argument to a list
		
		``"append_const"``
		append a constant value to a list
		
		``"count"``
		increment a counter by one
		
		``"callback"``
		call a specified function
		
		``"help"``
		print a usage message including all options and the documentation for them
		
		(If you don't supply an action, the default is ``"store"``.  For this action,
		you may also supply :attr:`~Option.type` and :attr:`~Option.dest` option
		attributes; see :ref:`optparse-standard-option-actions`.)
		
		As you can see, most actions involve storing or updating a value somewhere.
		:mod:`optparse` always creates a special object for this, conventionally called
		``options`` (it happens to be an instance of :class:`optparse.Values`).  Option
		arguments (and various other values) are stored as attributes of this object,
		according to the :attr:`~Option.dest` (destination) option attribute.
		
		For example, when you call ::
		
		parser.parse_args()
		
		one of the first things :mod:`optparse` does is create the ``options`` object::
		
		options = Values()
		
		If one of the options in this parser is defined with ::
		
		parser.add_option("-f", "--file", action="store", type="string", dest="filename")
		
		and the command-line being parsed includes any of the following::
		
		-ffoo
		-f foo
		--file=foo
		--file foo
		
		then :mod:`optparse`, on seeing this option, will do the equivalent of ::
		
		options.filename = "foo"
		
		The :attr:`~Option.type` and :attr:`~Option.dest` option attributes are almost
		as important as :attr:`~Option.action`, but :attr:`~Option.action` is the only
		one that makes sense for *all* options.
		
		
		.. ption attributes
		^^^^^^^^^^^^^^^^^
		
		The following option attributes may be passed as keyword arguments to
		:meth:`OptionParser.add_option`.  If you pass an option attribute that is not
		relevant to a particular option, or fail to pass a required option attribute,
		:mod:`optparse` raises :exc:`OptionError`.
		
		"""
		pass
		
	def disable_interspersed_args(self, ):
		"""
		Set parsing to stop on the first non-option.  For example, if ``-a`` and
		``-b`` are both simple options that take no arguments, :mod:`optparse`
		normally accepts this syntax::
		
		prog -a arg1 -b arg2
		
		and treats it as equivalent to  ::
		
		prog -a -b arg1 arg2
		
		To disable this feature, call :meth:`disable_interspersed_args`.  This
		restores traditional Unix syntax, where option parsing stops with the first
		non-option argument.
		
		Use this if you have a command processor which runs another command which has
		options of its own and you want to make sure these options don't get
		confused.  For example, each command might have a different set of options.
		
		"""
		pass
		
	def enable_interspersed_args(self, ):
		"""
		Set parsing to not stop on the first non-option, allowing interspersing
		switches with command arguments.  This is the default behavior.
		
		"""
		pass
		
	def get_option(self, opt_str):
		"""
		Returns the Option instance with the option string *opt_str*, or ``None`` if
		no options have that option string.
		
		"""
		pass
		
	def has_option(self, opt_str):
		"""
		Return true if the OptionParser has an option with option string *opt_str*
		(e.g., ``-q`` or ``--verbose``).
		
		"""
		pass
		
	def remove_option(self, opt_str):
		"""
		If the :class:`OptionParser` has an option corresponding to *opt_str*, that
		option is removed.  If that option provided any other option strings, all of
		those option strings become invalid. If *opt_str* does not occur in any
		option belonging to this :class:`OptionParser`, raises :exc:`ValueError`.
		
		
		.. onflicts between options
		^^^^^^^^^^^^^^^^^^^^^^^^^
		
		If you're not careful, it's easy to define options with conflicting option
		strings::
		
		parser.add_option("-n", "--dry-run", more)
		[more]
		parser.add_option("-n", "--noisy", more)
		
		(This is particularly true if you've defined your own OptionParser subclass with
		some standard options.)
		
		Every time you add an option, :mod:`optparse` checks for conflicts with existing
		options.  If it finds any, it invokes the current conflict-handling mechanism.
		You can set the conflict-handling mechanism either in the constructor::
		
		parser = OptionParser(more, conflict_handler=handler)
		
		or with a separate call::
		
		parser.set_conflict_handler(handler)
		
		The available conflict handlers are:
		
		``"error"`` (default)
		assume option conflicts are a programming error and raise
		:exc:`OptionConflictError`
		
		``"resolve"``
		resolve option conflicts intelligently (see below)
		
		
		As an example, let's define an :class:`OptionParser` that resolves conflicts
		intelligently and add conflicting options to it::
		
		parser = OptionParser(conflict_handler="resolve")
		parser.add_option("-n", "--dry-run", more, help="do no harm")
		parser.add_option("-n", "--noisy", more, help="be noisy")
		
		At this point, :mod:`optparse` detects that a previously-added option is already
		using the ``-n`` option string.  Since ``conflict_handler`` is ``"resolve"``,
		it resolves the situation by removing ``-n`` from the earlier option's list of
		option strings.  Now ``--dry-run`` is the only way for the user to activate
		that option.  If the user asks for help, the help message will reflect that::
		
		Options:
		--dry-run     do no harm
		[more]
		-n, --noisy   be noisy
		
		It's possible to whittle away the option strings for a previously-added option
		until there are none left, and the user has no way of invoking that option from
		the command-line.  In that case, :mod:`optparse` removes that option completely,
		so it doesn't show up in help text or anywhere else. Carrying on with our
		existing OptionParser::
		
		parser.add_option("--dry-run", more, help="new dry-run option")
		
		At this point, the original ``-n``/``--dry-run`` option is no longer
		accessible, so :mod:`optparse` removes it, leaving this help text::
		
		Options:
		[more]
		-n, --noisy   be noisy
		--dry-run     new dry-run option
		
		
		.. leanup
		^^^^^^^
		
		OptionParser instances have several cyclic references.  This should not be a
		problem for Python's garbage collector, but you may wish to break the cyclic
		references explicitly by calling :meth:`~OptionParser.destroy` on your
		OptionParser once you are done with it.  This is particularly useful in
		long-running applications where large object graphs are reachable from your
		OptionParser.
		
		
		.. ther methods
		^^^^^^^^^^^^^
		
		OptionParser supports several other public methods:
		
		"""
		pass
		
	def set_usage(self, usage):
		"""
		Set the usage string according to the rules described above for the ``usage``
		constructor keyword argument.  Passing ``None`` sets the default usage
		string; use :data:`optparse.SUPPRESS_USAGE` to suppress a usage message.
		
		"""
		pass
		
	def print_usage(self, file=None):
		"""
		Print the usage message for the current program (``self.usage``) to *file*
		(default stdout).  Any occurrence of the string ``%prog`` in ``self.usage``
		is replaced with the name of the current program.  Does nothing if
		``self.usage`` is empty or not defined.
		
		"""
		pass
		
	def get_usage(self, ):
		"""
		Same as :meth:`print_usage` but returns the usage string instead of
		printing it.
		
		"""
		pass
		
	def set_defaults(self, dest=value,more=dict()):
		"""
		Set default values for several option destinations at once.  Using
		:meth:`set_defaults` is the preferred way to set default values for options,
		since multiple options can share the same destination.  For example, if
		several "mode" options all set the same destination, any one of them can set
		the default, and the last one wins::
		
		parser.add_option("--advanced", action="store_const",
		dest="mode", const="advanced",
		default="novice")    # overridden below
		parser.add_option("--novice", action="store_const",
		dest="mode", const="novice",
		default="advanced")  # overrides above setting
		
		To avoid this confusion, use :meth:`set_defaults`::
		
		parser.set_defaults(mode="advanced")
		parser.add_option("--advanced", action="store_const",
		dest="mode", const="advanced")
		parser.add_option("--novice", action="store_const",
		dest="mode", const="novice")
		
		
		.. ption Callbacks
		----------------
		
		When :mod:`optparse`'s built-in actions and types aren't quite enough for your
		needs, you have two choices: extend :mod:`optparse` or define a callback option.
		Extending :mod:`optparse` is more general, but overkill for a lot of simple
		cases.  Quite often a simple callback is all you need.
		
		There are two steps to defining a callback option:
		
		* define the option itself using the ``"callback"`` action
		
		* write the callback; this is a function (or method) that takes at least four
		arguments, as described below
		
		
		.. efining a callback option
		^^^^^^^^^^^^^^^^^^^^^^^^^^
		
		As always, the easiest way to define a callback option is by using the
		:meth:`OptionParser.add_option` method.  Apart from :attr:`~Option.action`, the
		only option attribute you must specify is ``callback``, the function to call::
		
		parser.add_option("-c", action="callback", callback=my_callback)
		
		``callback`` is a function (or other callable object), so you must have already
		defined ``my_callback()`` when you create this callback option. In this simple
		case, :mod:`optparse` doesn't even know if ``-c`` takes any arguments,
		which usually means that the option takes no arguments---the mere presence of
		``-c`` on the command-line is all it needs to know.  In some
		circumstances, though, you might want your callback to consume an arbitrary
		number of command-line arguments.  This is where writing callbacks gets tricky;
		it's covered later in this section.
		
		:mod:`optparse` always passes four particular arguments to your callback, and it
		will only pass additional arguments if you specify them via
		:attr:`~Option.callback_args` and :attr:`~Option.callback_kwargs`.  Thus, the
		minimal callback function signature is::
		
		def my_callback(option, opt, value, parser):
		
		The four arguments to a callback are described below.
		
		There are several other option attributes that you can supply when you define a
		callback option:
		
		:attr:`~Option.type`
		has its usual meaning: as with the ``"store"`` or ``"append"`` actions, it
		instructs :mod:`optparse` to consume one argument and convert it to
		:attr:`~Option.type`.  Rather than storing the converted value(s) anywhere,
		though, :mod:`optparse` passes it to your callback function.
		
		:attr:`~Option.nargs`
		also has its usual meaning: if it is supplied and > 1, :mod:`optparse` will
		consume :attr:`~Option.nargs` arguments, each of which must be convertible to
		:attr:`~Option.type`.  It then passes a tuple of converted values to your
		callback.
		
		:attr:`~Option.callback_args`
		a tuple of extra positional arguments to pass to the callback
		
		:attr:`~Option.callback_kwargs`
		a dictionary of extra keyword arguments to pass to the callback
		
		
		.. ow callbacks are called
		^^^^^^^^^^^^^^^^^^^^^^^^
		
		All callbacks are called as follows::
		
		func(option, opt_str, value, parser, *args, **kwargs)
		
		where
		
		``option``
		is the Option instance that's calling the callback
		
		``opt_str``
		is the option string seen on the command-line that's triggering the callback.
		(If an abbreviated long option was used, ``opt_str`` will be the full,
		canonical option string---e.g. if the user puts ``--foo`` on the
		command-line as an abbreviation for ``--foobar``, then ``opt_str`` will be
		``"--foobar"``.)
		
		``value``
		is the argument to this option seen on the command-line.  :mod:`optparse` will
		only expect an argument if :attr:`~Option.type` is set; the type of ``value`` will be
		the type implied by the option's type.  If :attr:`~Option.type` for this option is
		``None`` (no argument expected), then ``value`` will be ``None``.  If :attr:`~Option.nargs`
		> 1, ``value`` will be a tuple of values of the appropriate type.
		
		``parser``
		is the OptionParser instance driving the whole thing, mainly useful because
		you can access some other interesting data through its instance attributes:
		
		``parser.largs``
		the current list of leftover arguments, ie. arguments that have been
		consumed but are neither options nor option arguments. Feel free to modify
		``parser.largs``, e.g. by adding more arguments to it.  (This list will
		become ``args``, the second return value of :meth:`parse_args`.)
		
		``parser.rargs``
		the current list of remaining arguments, ie. with ``opt_str`` and
		``value`` (if applicable) removed, and only the arguments following them
		still there.  Feel free to modify ``parser.rargs``, e.g. by consuming more
		arguments.
		
		``parser.values``
		the object where option values are by default stored (an instance of
		optparse.OptionValues).  This lets callbacks use the same mechanism as the
		rest of :mod:`optparse` for storing option values; you don't need to mess
		around with globals or closures.  You can also access or modify the
		value(s) of any options already encountered on the command-line.
		
		``args``
		is a tuple of arbitrary positional arguments supplied via the
		:attr:`~Option.callback_args` option attribute.
		
		``kwargs``
		is a dictionary of arbitrary keyword arguments supplied via
		:attr:`~Option.callback_kwargs`.
		
		
		.. aising errors in a callback
		^^^^^^^^^^^^^^^^^^^^^^^^^^^^
		
		The callback function should raise :exc:`OptionValueError` if there are any
		problems with the option or its argument(s).  :mod:`optparse` catches this and
		terminates the program, printing the error message you supply to stderr.  Your
		message should be clear, concise, accurate, and mention the option at fault.
		Otherwise, the user will have a hard time figuring out what he did wrong.
		
		
		.. allback example 1: trivial callback
		^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
		
		Here's an example of a callback option that takes no arguments, and simply
		records that the option was seen::
		
		def record_foo_seen(option, opt_str, value, parser):
		parser.values.saw_foo = True
		
		parser.add_option("--foo", action="callback", callback=record_foo_seen)
		
		Of course, you could do that with the ``"store_true"`` action.
		
		
		.. allback example 2: check option order
		^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
		
		Here's a slightly more interesting example: record the fact that ``-a`` is
		seen, but blow up if it comes after ``-b`` in the command-line.  ::
		
		def check_order(option, opt_str, value, parser):
		if parser.values.b:
		raise OptionValueError("can't use -a after -b")
		parser.values.a = 1
		[more]
		parser.add_option("-a", action="callback", callback=check_order)
		parser.add_option("-b", action="store_true", dest="b")
		
		
		.. allback example 3: check option order (generalized)
		^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
		
		If you want to re-use this callback for several similar options (set a flag, but
		blow up if ``-b`` has already been seen), it needs a bit of work: the error
		message and the flag that it sets must be generalized.  ::
		
		def check_order(option, opt_str, value, parser):
		if parser.values.b:
		raise OptionValueError("can't use %s after -b" % opt_str)
		setattr(parser.values, option.dest, 1)
		[more]
		parser.add_option("-a", action="callback", callback=check_order, dest='a')
		parser.add_option("-b", action="store_true", dest="b")
		parser.add_option("-c", action="callback", callback=check_order, dest='c')
		
		
		.. allback example 4: check arbitrary condition
		^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
		
		Of course, you could put any condition in there---you're not limited to checking
		the values of already-defined options.  For example, if you have options that
		should not be called when the moon is full, all you have to do is this::
		
		def check_moon(option, opt_str, value, parser):
		if is_moon_full():
		raise OptionValueError("%s option invalid when moon is full"
		% opt_str)
		setattr(parser.values, option.dest, 1)
		[more]
		parser.add_option("--foo",
		action="callback", callback=check_moon, dest="foo")
		
		(The definition of ``is_moon_full()`` is left as an exercise for the reader.)
		
		
		.. allback example 5: fixed arguments
		^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
		
		Things get slightly more interesting when you define callback options that take
		a fixed number of arguments.  Specifying that a callback option takes arguments
		is similar to defining a ``"store"`` or ``"append"`` option: if you define
		:attr:`~Option.type`, then the option takes one argument that must be
		convertible to that type; if you further define :attr:`~Option.nargs`, then the
		option takes :attr:`~Option.nargs` arguments.
		
		Here's an example that just emulates the standard ``"store"`` action::
		
		def store_value(option, opt_str, value, parser):
		setattr(parser.values, option.dest, value)
		[more]
		parser.add_option("--foo",
		action="callback", callback=store_value,
		type="int", nargs=3, dest="foo")
		
		Note that :mod:`optparse` takes care of consuming 3 arguments and converting
		them to integers for you; all you have to do is store them.  (Or whatever;
		obviously you don't need a callback for this example.)
		
		
		.. allback example 6: variable arguments
		^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
		
		Things get hairy when you want an option to take a variable number of arguments.
		For this case, you must write a callback, as :mod:`optparse` doesn't provide any
		built-in capabilities for it.  And you have to deal with certain intricacies of
		conventional Unix command-line parsing that :mod:`optparse` normally handles for
		you.  In particular, callbacks should implement the conventional rules for bare
		``--`` and ``-`` arguments:
		
		* either ``--`` or ``-`` can be option arguments
		
		* bare ``--`` (if not the argument to some option): halt command-line
		processing and discard the ``--``
		
		* bare ``-`` (if not the argument to some option): halt command-line
		processing but keep the ``-`` (append it to ``parser.largs``)
		
		If you want an option that takes a variable number of arguments, there are
		several subtle, tricky issues to worry about.  The exact implementation you
		choose will be based on which trade-offs you're willing to make for your
		application (which is why :mod:`optparse` doesn't support this sort of thing
		directly).
		
		Nevertheless, here's a stab at a callback for an option with variable
		arguments::
		
		def vararg_callback(option, opt_str, value, parser):
		assert value is None
		value = []
		
		def floatable(str):
		try:
		float(str)
		return True
		except ValueError:
		return False
		
		for arg in parser.rargs:
		# stop on --foo like options
		if arg[:2] == "--" and len(arg) > 2:
		break
		# stop on -a, but not on -3 or -3.0
		if arg[:1] == "-" and len(arg) > 1 and not floatable(arg):
		break
		value.append(arg)
		
		del parser.rargs[:len(value)]
		setattr(parser.values, option.dest, value)
		
		[more]
		parser.add_option("-c", "--callback", dest="vararg_attr",
		action="callback", callback=vararg_callback)
		
		
		.. xtending :mod:`optparse`
		-------------------------
		
		Since the two major controlling factors in how :mod:`optparse` interprets
		command-line options are the action and type of each option, the most likely
		direction of extension is to add new actions and new types.
		
		
		.. dding new types
		^^^^^^^^^^^^^^^^
		
		To add new types, you need to define your own subclass of :mod:`optparse`'s
		:class:`Option` class.  This class has a couple of attributes that define
		:mod:`optparse`'s types: :attr:`~Option.TYPES` and :attr:`~Option.TYPE_CHECKER`.
		
		"""
		pass
		
	


