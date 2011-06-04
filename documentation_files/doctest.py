#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
""":synopsis: Test pieces of code within docstrings.
"""
"""
By default, if an expected output block contains just ``1``, an actual output
block containing just ``1`` or just ``True`` is considered to be a match, and
similarly for ``0`` versus ``False``.  When :const:`DONT_ACCEPT_TRUE_FOR_1` is
specified, neither substitution is allowed.  The default behavior caters to that
Python changed the return type of many functions from integer to boolean;
doctests expecting "little integer" output still work in these cases.  This
option will probably go away, but not for several years.


"""
DONT_ACCEPT_TRUE_FOR_1 = None
"""
By default, if an expected output block contains a line containing only the
string ``<BLANKLINE>``, then that line will match a blank line in the actual
output.  Because a genuinely blank line delimits the expected output, this is
the only way to communicate that a blank line is expected.  When
:const:`DONT_ACCEPT_BLANKLINE` is specified, this substitution is not allowed.


"""
DONT_ACCEPT_BLANKLINE = None
"""
When specified, all sequences of whitespace (blanks and newlines) are treated as
equal.  Any sequence of whitespace within the expected output will match any
sequence of whitespace within the actual output. By default, whitespace must
match exactly. :const:`NORMALIZE_WHITESPACE` is especially useful when a line of
expected output is very long, and you want to wrap it across multiple lines in
your source.


"""
NORMALIZE_WHITESPACE = None
"""
When specified, an ellipsis marker (``*more``) in the expected output can match
any substring in the actual output.  This includes substrings that span line
boundaries, and empty substrings, so it's best to keep usage of this simple.
Complicated uses can lead to the same kinds of "oops, it matched too much!"
surprises that ``.*`` is prone to in regular expressions.


"""
ELLIPSIS = None
"""
When specified, an example that expects an exception passes if an exception of
the expected type is raised, even if the exception detail does not match.  For
example, an example expecting ``ValueError: 42`` will pass if the actual
exception raised is ``ValueError: 3*14``, but will fail, e.g., if
:exc:`TypeError` is raised.

It will also ignore the module name used in Python 3 doctest reports. Hence
both these variations will work regardless of whether the test is run under
Python 2.7 or Python 3.2 (or later versions):

>>> raise CustomError('message') #doctest: +IGNORE_EXCEPTION_DETAIL
Traceback (most recent call last):
CustomError: message

>>> raise CustomError('message') #doctest: +IGNORE_EXCEPTION_DETAIL
Traceback (most recent call last):
my_module.CustomError: message

Note that :const:`ELLIPSIS` can also be used to ignore the
details of the exception message, but such a test may still fail based
on whether or not the module details are printed as part of the
exception name. Using :const:`IGNORE_EXCEPTION_DETAIL` and the details
from Python 2.3 is also the only clear way to write a doctest that doesn't
care about the exception detail yet continues to pass under Python 2.3 or
earlier (those releases do not support doctest directives and ignore them
as irrelevant comments). For example, ::

>>> (1, 2)[3] = 'moo' #doctest: +IGNORE_EXCEPTION_DETAIL
Traceback (most recent call last):
File "<stdin>", line 1, in ?
TypeError: object doesn't support item assignment

passes under Python 2.3 and later Python versions, even though the detail
changed in Python 2.4 to say "does not" instead of "doesn't".

"""
IGNORE_EXCEPTION_DETAIL = None
"""
When specified, do not run the example at all.  This can be useful in contexts
where doctest examples serve as both documentation and test cases, and an
example should be included for documentation purposes, but should not be
checked.  E.g., the example's output might be random; or the example might
depend on resources which would be unavailable to the test driver.

The SKIP flag can also be used for temporarily "commenting out" examples.

"""
SKIP = None
"""
A bitmask or'ing together all the comparison flags above.

The second group of options controls how test failures are reported:


"""
COMPARISON_FLAGS = None
"""
When specified, failures that involve multi-line expected and actual outputs are
displayed using a unified diff.


"""
REPORT_UDIFF = None
"""
When specified, failures that involve multi-line expected and actual outputs
will be displayed using a context diff.


"""
REPORT_CDIFF = None
"""
When specified, differences are computed by ``difflib.Differ``, using the same
algorithm as the popular :file:`ndiff.py` utility. This is the only method that
marks differences within lines as well as across lines.  For example, if a line
of expected output contains digit ``1`` where actual output contains letter
``l``, a line is inserted with a caret marking the mismatching column positions.


"""
REPORT_NDIFF = None
"""
When specified, display the first failing example in each doctest, but suppress
output for all remaining examples.  This will prevent doctest from reporting
correct examples that break because of earlier failures; but it might also hide
incorrect examples that fail independently of the first failure.  When
:const:`REPORT_ONLY_FIRST_FAILURE` is specified, the remaining examples are
still run, and still count towards the total number of failures reported; only
the output is suppressed.


"""
REPORT_ONLY_FIRST_FAILURE = None
"""
A bitmask or'ing together all the reporting flags above.

"Doctest directives" may be used to modify the option flags for individual
examples.  Doctest directives are expressed as a special Python comment
following an example's source code:

"""
REPORTING_FLAGS = None
def register_optionflag(name):
	"""
	Create a new option flag with a given name, and return the new flag's integer
	value.  :func:`register_optionflag` can be used when subclassing
	:class:`OutputChecker` or :class:`DocTestRunner` to create new options that are
	supported by your subclasses.  :func:`register_optionflag` should always be
	called using the following idiom::
	
	MY_FLAG = register_optionflag('MY_FLAG')
	
	"""
	pass
	
def testfile(filename,module_relative,name,package,globs,verbose,report,optionflags,extraglobs,raise_on_error,parser,encoding):
	"""
	All arguments except *filename* are optional, and should be specified in keyword
	form.
	
	Test examples in the file named *filename*.  Return ``(failure_count,
	test_count)``.
	
	Optional argument *module_relative* specifies how the filename should be
	interpreted:
	
	* If *module_relative* is ``True`` (the default), then *filename* specifies an
	OS-independent module-relative path.  By default, this path is relative to the
	calling module's directory; but if the *package* argument is specified, then it
	is relative to that package.  To ensure OS-independence, *filename* should use
	``/`` characters to separate path segments, and may not be an absolute path
	(i.e., it may not begin with ``/``).
	
	* If *module_relative* is ``False``, then *filename* specifies an OS-specific
	path.  The path may be absolute or relative; relative paths are resolved with
	respect to the current working directory.
	
	Optional argument *name* gives the name of the test; by default, or if ``None``,
	``os.path.basename(filename)`` is used.
	
	Optional argument *package* is a Python package or the name of a Python package
	whose directory should be used as the base directory for a module-relative
	filename.  If no package is specified, then the calling module's directory is
	used as the base directory for module-relative filenames.  It is an error to
	specify *package* if *module_relative* is ``False``.
	
	Optional argument *globs* gives a dict to be used as the globals when executing
	examples.  A new shallow copy of this dict is created for the doctest, so its
	examples start with a clean slate. By default, or if ``None``, a new empty dict
	is used.
	
	Optional argument *extraglobs* gives a dict merged into the globals used to
	execute examples.  This works like :meth:`dict.update`:  if *globs* and
	*extraglobs* have a common key, the associated value in *extraglobs* appears in
	the combined dict.  By default, or if ``None``, no extra globals are used.  This
	is an advanced feature that allows parameterization of doctests.  For example, a
	doctest can be written for a base class, using a generic name for the class,
	then reused to test any number of subclasses by passing an *extraglobs* dict
	mapping the generic name to the subclass to be tested.
	
	Optional argument *verbose* prints lots of stuff if true, and prints only
	failures if false; by default, or if ``None``, it's true if and only if ``'-v'``
	is in ``sys.argv``.
	
	Optional argument *report* prints a summary at the end when true, else prints
	nothing at the end.  In verbose mode, the summary is detailed, else the summary
	is very brief (in fact, empty if all tests passed).
	
	Optional argument *optionflags* or's together option flags.  See section
	:ref:`doctest-options`.
	
	Optional argument *raise_on_error* defaults to false.  If true, an exception is
	raised upon the first failure or unexpected exception in an example.  This
	allows failures to be post-mortem debugged. Default behavior is to continue
	running examples.
	
	Optional argument *parser* specifies a :class:`DocTestParser` (or subclass) that
	should be used to extract tests from the files.  It defaults to a normal parser
	(i.e., ``DocTestParser()``).
	
	Optional argument *encoding* specifies an encoding that should be used to
	convert the file to unicode.
	
	"""
	pass
	
def testmod(m,name,globs,verbose,report,optionflags,extraglobs,raise_on_error,exclude_empty):
	"""
	All arguments are optional, and all except for *m* should be specified in
	keyword form.
	
	Test examples in docstrings in functions and classes reachable from module *m*
	(or module :mod:`__main__` if *m* is not supplied or is ``None``), starting with
	``m.__doc__``.
	
	Also test examples reachable from dict ``m.__test__``, if it exists and is not
	``None``.  ``m.__test__`` maps names (strings) to functions, classes and
	strings; function and class docstrings are searched for examples; strings are
	searched directly, as if they were docstrings.
	
	Only docstrings attached to objects belonging to module *m* are searched.
	
	Return ``(failure_count, test_count)``.
	
	Optional argument *name* gives the name of the module; by default, or if
	``None``, ``m.__name__`` is used.
	
	Optional argument *exclude_empty* defaults to false.  If true, objects for which
	no doctests are found are excluded from consideration. The default is a backward
	compatibility hack, so that code still using :meth:`doctest.master.summarize` in
	conjunction with :func:`testmod` continues to get output for objects with no
	tests. The *exclude_empty* argument to the newer :class:`DocTestFinder`
	constructor defaults to true.
	
	Optional arguments *extraglobs*, *verbose*, *report*, *optionflags*,
	*raise_on_error*, and *globs* are the same as for function :func:`testfile`
	above, except that *globs* defaults to ``m.__dict__``.
	
	"""
	pass
	
def run_docstring_examples(f,globs,verbose,name,compileflags,optionflags):
	"""
	Test examples associated with object *f*; for example, *f* may be a module,
	function, or class object.
	
	A shallow copy of dictionary argument *globs* is used for the execution context.
	
	Optional argument *name* is used in failure messages, and defaults to
	``"NoName"``.
	
	If optional argument *verbose* is true, output is generated even if there are no
	failures.  By default, output is generated only in case of an example failure.
	
	Optional argument *compileflags* gives the set of flags that should be used by
	the Python compiler when running the examples.  By default, or if ``None``,
	flags are deduced corresponding to the set of future features found in *globs*.
	
	Optional argument *optionflags* works as for function :func:`testfile` above.
	
	
	.. nittest API
	------------
	
	As your collection of doctest'ed modules grows, you'll want a way to run all
	their doctests systematically.  Prior to Python 2.4, :mod:`doctest` had a barely
	documented :class:`Tester` class that supplied a rudimentary way to combine
	doctests from multiple modules. :class:`Tester` was feeble, and in practice most
	serious Python testing frameworks build on the :mod:`unittest` module, which
	supplies many flexible ways to combine tests from multiple sources.  So, in
	Python 2.4, :mod:`doctest`'s :class:`Tester` class is deprecated, and
	:mod:`doctest` provides two functions that can be used to create :mod:`unittest`
	test suites from modules and text files containing doctests.  To integrate with
	:mod:`unittest` test discovery, include a :func:`load_tests` function in your
	test module::
	
	import unittest
	import doctest
	import my_module_with_doctests
	
	def load_tests(loader, tests, ignore):
	tests.addTests(doctest.DocTestSuite(my_module_with_doctests))
	return tests
	
	There are two main functions for creating :class:`unittest.TestSuite` instances
	from text files and modules with doctests:
	
	
	"""
	pass
	
def DocFileSuite(paths,module_relative,package,setUp,tearDown,globs,optionflags,parser,encoding):
	"""
	Convert doctest tests from one or more text files to a
	:class:`unittest.TestSuite`.
	
	The returned :class:`unittest.TestSuite` is to be run by the unittest framework
	and runs the interactive examples in each file.  If an example in any file
	fails, then the synthesized unit test fails, and a :exc:`failureException`
	exception is raised showing the name of the file containing the test and a
	(sometimes approximate) line number.
	
	Pass one or more paths (as strings) to text files to be examined.
	
	Options may be provided as keyword arguments:
	
	Optional argument *module_relative* specifies how the filenames in *paths*
	should be interpreted:
	
	* If *module_relative* is ``True`` (the default), then each filename in
	*paths* specifies an OS-independent module-relative path.  By default, this
	path is relative to the calling module's directory; but if the *package*
	argument is specified, then it is relative to that package.  To ensure
	OS-independence, each filename should use ``/`` characters to separate path
	segments, and may not be an absolute path (i.e., it may not begin with
	``/``).
	
	* If *module_relative* is ``False``, then each filename in *paths* specifies
	an OS-specific path.  The path may be absolute or relative; relative paths
	are resolved with respect to the current working directory.
	
	Optional argument *package* is a Python package or the name of a Python
	package whose directory should be used as the base directory for
	module-relative filenames in *paths*.  If no package is specified, then the
	calling module's directory is used as the base directory for module-relative
	filenames.  It is an error to specify *package* if *module_relative* is
	``False``.
	
	Optional argument *setUp* specifies a set-up function for the test suite.
	This is called before running the tests in each file.  The *setUp* function
	will be passed a :class:`DocTest` object.  The setUp function can access the
	test globals as the *globs* attribute of the test passed.
	
	Optional argument *tearDown* specifies a tear-down function for the test
	suite.  This is called after running the tests in each file.  The *tearDown*
	function will be passed a :class:`DocTest` object.  The setUp function can
	access the test globals as the *globs* attribute of the test passed.
	
	Optional argument *globs* is a dictionary containing the initial global
	variables for the tests.  A new copy of this dictionary is created for each
	test.  By default, *globs* is a new empty dictionary.
	
	Optional argument *optionflags* specifies the default doctest options for the
	tests, created by or-ing together individual option flags.  See section
	:ref:`doctest-options`. See function :func:`set_unittest_reportflags` below
	for a better way to set reporting options.
	
	Optional argument *parser* specifies a :class:`DocTestParser` (or subclass)
	that should be used to extract tests from the files.  It defaults to a normal
	parser (i.e., ``DocTestParser()``).
	
	Optional argument *encoding* specifies an encoding that should be used to
	convert the file to unicode.
	
	"""
	pass
	
def DocTestSuite(module,globs,extraglobs,test_finder,setUp,tearDown,checker):
	"""
	Convert doctest tests for a module to a :class:`unittest.TestSuite`.
	
	The returned :class:`unittest.TestSuite` is to be run by the unittest framework
	and runs each doctest in the module.  If any of the doctests fail, then the
	synthesized unit test fails, and a :exc:`failureException` exception is raised
	showing the name of the file containing the test and a (sometimes approximate)
	line number.
	
	Optional argument *module* provides the module to be tested.  It can be a module
	object or a (possibly dotted) module name.  If not specified, the module calling
	this function is used.
	
	Optional argument *globs* is a dictionary containing the initial global
	variables for the tests.  A new copy of this dictionary is created for each
	test.  By default, *globs* is a new empty dictionary.
	
	Optional argument *extraglobs* specifies an extra set of global variables, which
	is merged into *globs*.  By default, no extra globals are used.
	
	Optional argument *test_finder* is the :class:`DocTestFinder` object (or a
	drop-in replacement) that is used to extract doctests from the module.
	
	Optional arguments *setUp*, *tearDown*, and *optionflags* are the same as for
	function :func:`DocFileSuite` above.
	
	"""
	pass
	
def set_unittest_reportflags(flags):
	"""
	Set the :mod:`doctest` reporting flags to use.
	
	Argument *flags* or's together option flags.  See section
	:ref:`doctest-options`.  Only "reporting flags" can be used.
	
	This is a module-global setting, and affects all future doctests run by module
	:mod:`unittest`:  the :meth:`runTest` method of :class:`DocTestCase` looks at
	the option flags specified for the test case when the :class:`DocTestCase`
	instance was constructed.  If no reporting flags were specified (which is the
	typical and expected case), :mod:`doctest`'s :mod:`unittest` reporting flags are
	or'ed into the option flags, and the option flags so augmented are passed to the
	:class:`DocTestRunner` instance created to run the doctest.  If any reporting
	flags were specified when the :class:`DocTestCase` instance was constructed,
	:mod:`doctest`'s :mod:`unittest` reporting flags are ignored.
	
	The value of the :mod:`unittest` reporting flags in effect before the function
	was called is returned by the function.
	
	"""
	pass
	
class DocTest:


	"""
	A collection of doctest examples that should be run in a single namespace.  The
	constructor arguments are used to initialize the member variables of the same
	names.
	
	"""
	
	
	def __init__(self, ):
		pass
	
	


class Example:


	"""
	A single interactive example, consisting of a Python statement and its expected
	output.  The constructor arguments are used to initialize the member variables
	of the same names.
	
	"""
	
	
	def __init__(self, ):
		pass
	
	


class DocTestFinder:


	"""
	A processing class used to extract the :class:`DocTest`\ s that are relevant to
	a given object, from its docstring and the docstrings of its contained objects.
	:class:`DocTest`\ s can currently be extracted from the following object types:
	modules, functions, classes, methods, staticmethods, classmethods, and
	properties.
	
	The optional argument *verbose* can be used to display the objects searched by
	the finder.  It defaults to ``False`` (no output).
	
	The optional argument *parser* specifies the :class:`DocTestParser` object (or a
	drop-in replacement) that is used to extract doctests from docstrings.
	
	If the optional argument *recurse* is false, then :meth:`DocTestFinder.find`
	will only examine the given object, and not any contained objects.
	
	If the optional argument *exclude_empty* is false, then
	:meth:`DocTestFinder.find` will include tests for objects with empty docstrings.
	
	"""
	
	
	def __init__(self, ):
		pass
	
	def find(self, obj,name,module,globs,extraglobs):
		"""
		Return a list of the :class:`DocTest`\ s that are defined by *obj*'s
		docstring, or by any of its contained objects' docstrings.
		
		The optional argument *name* specifies the object's name; this name will be
		used to construct names for the returned :class:`DocTest`\ s.  If *name* is
		not specified, then ``obj.__name__`` is used.
		
		The optional parameter *module* is the module that contains the given object.
		If the module is not specified or is None, then the test finder will attempt
		to automatically determine the correct module.  The object's module is used:
		
		* As a default namespace, if *globs* is not specified.
		
		* To prevent the DocTestFinder from extracting DocTests from objects that are
		imported from other modules.  (Contained objects with modules other than
		*module* are ignored.)
		
		* To find the name of the file containing the object.
		
		* To help find the line number of the object within its file.
		
		If *module* is ``False``, no attempt to find the module will be made.  This is
		obscure, of use mostly in testing doctest itself: if *module* is ``False``, or
		is ``None`` but cannot be found automatically, then all objects are considered
		to belong to the (non-existent) module, so all contained objects will
		(recursively) be searched for doctests.
		
		The globals for each :class:`DocTest` is formed by combining *globs* and
		*extraglobs* (bindings in *extraglobs* override bindings in *globs*).  A new
		shallow copy of the globals dictionary is created for each :class:`DocTest`.
		If *globs* is not specified, then it defaults to the module's *__dict__*, if
		specified, or ``{}`` otherwise.  If *extraglobs* is not specified, then it
		defaults to ``{}``.
		
		
		.. ocTestParser objects
		"""
		pass
		
	


class DocTestParser:


	"""
	A processing class used to extract interactive examples from a string, and use
	them to create a :class:`DocTest` object.
	
	"""
	
	
	def __init__(self, ):
		pass
	
	def get_doctest(self, string,globs,name,filename,lineno):
		"""
		Extract all doctest examples from the given string, and collect them into a
		:class:`DocTest` object.
		
		*globs*, *name*, *filename*, and *lineno* are attributes for the new
		:class:`DocTest` object.  See the documentation for :class:`DocTest` for more
		information.
		
		
		"""
		pass
		
	def get_examples(self, string,name):
		"""
		Extract all doctest examples from the given string, and return them as a list
		of :class:`Example` objects.  Line numbers are 0-based.  The optional argument
		*name* is a name identifying this string, and is only used for error messages.
		
		
		"""
		pass
		
	def parse(self, string,name):
		"""
		Divide the given string into examples and intervening text, and return them as
		a list of alternating :class:`Example`\ s and strings. Line numbers for the
		:class:`Example`\ s are 0-based.  The optional argument *name* is a name
		identifying this string, and is only used for error messages.
		
		
		.. ocTestRunner objects
		"""
		pass
		
	


class DocTestRunner:


	"""
	A processing class used to execute and verify the interactive examples in a
	:class:`DocTest`.
	
	The comparison between expected outputs and actual outputs is done by an
	:class:`OutputChecker`.  This comparison may be customized with a number of
	option flags; see section :ref:`doctest-options` for more information.  If the
	option flags are insufficient, then the comparison may also be customized by
	passing a subclass of :class:`OutputChecker` to the constructor.
	
	The test runner's display output can be controlled in two ways. First, an output
	function can be passed to :meth:`TestRunner.run`; this function will be called
	with strings that should be displayed.  It defaults to ``sys.stdout.write``.  If
	capturing the output is not sufficient, then the display output can be also
	customized by subclassing DocTestRunner, and overriding the methods
	:meth:`report_start`, :meth:`report_success`,
	:meth:`report_unexpected_exception`, and :meth:`report_failure`.
	
	The optional keyword argument *checker* specifies the :class:`OutputChecker`
	object (or drop-in replacement) that should be used to compare the expected
	outputs to the actual outputs of doctest examples.
	
	The optional keyword argument *verbose* controls the :class:`DocTestRunner`'s
	verbosity.  If *verbose* is ``True``, then information is printed about each
	example, as it is run.  If *verbose* is ``False``, then only failures are
	printed.  If *verbose* is unspecified, or ``None``, then verbose output is used
	iff the command-line switch ``-v`` is used.
	
	The optional keyword argument *optionflags* can be used to control how the test
	runner compares expected output to actual output, and how it displays failures.
	For more information, see section :ref:`doctest-options`.
	
	"""
	
	
	def __init__(self, ):
		pass
	
	def report_start(self, out,test,example):
		"""
		Report that the test runner is about to process the given example. This method
		is provided to allow subclasses of :class:`DocTestRunner` to customize their
		output; it should not be called directly.
		
		*example* is the example about to be processed.  *test* is the test
		*containing example*.  *out* is the output function that was passed to
		:meth:`DocTestRunner.run`.
		
		
		"""
		pass
		
	def report_success(self, out,test,example,got):
		"""
		Report that the given example ran successfully.  This method is provided to
		allow subclasses of :class:`DocTestRunner` to customize their output; it
		should not be called directly.
		
		*example* is the example about to be processed.  *got* is the actual output
		from the example.  *test* is the test containing *example*.  *out* is the
		output function that was passed to :meth:`DocTestRunner.run`.
		
		
		"""
		pass
		
	def report_failure(self, out,test,example,got):
		"""
		Report that the given example failed.  This method is provided to allow
		subclasses of :class:`DocTestRunner` to customize their output; it should not
		be called directly.
		
		*example* is the example about to be processed.  *got* is the actual output
		from the example.  *test* is the test containing *example*.  *out* is the
		output function that was passed to :meth:`DocTestRunner.run`.
		
		
		"""
		pass
		
	def report_unexpected_exception(self, out,test,example,exc_info):
		"""
		Report that the given example raised an unexpected exception. This method is
		provided to allow subclasses of :class:`DocTestRunner` to customize their
		output; it should not be called directly.
		
		*example* is the example about to be processed. *exc_info* is a tuple
		containing information about the unexpected exception (as returned by
		:func:`sys.exc_info`). *test* is the test containing *example*.  *out* is the
		output function that was passed to :meth:`DocTestRunner.run`.
		
		
		"""
		pass
		
	def run(self, test,compileflags,out,clear_globs):
		"""
		Run the examples in *test* (a :class:`DocTest` object), and display the
		results using the writer function *out*.
		
		The examples are run in the namespace ``test.globs``.  If *clear_globs* is
		true (the default), then this namespace will be cleared after the test runs,
		to help with garbage collection. If you would like to examine the namespace
		after the test completes, then use *clear_globs=False*.
		
		*compileflags* gives the set of flags that should be used by the Python
		compiler when running the examples.  If not specified, then it will default to
		the set of future-import flags that apply to *globs*.
		
		The output of each example is checked using the :class:`DocTestRunner`'s
		output checker, and the results are formatted by the
		:meth:`DocTestRunner.report_\*` methods.
		
		
		"""
		pass
		
	def summarize(self, verbose):
		"""
		Print a summary of all the test cases that have been run by this DocTestRunner,
		and return a :term:`named tuple` ``TestResults(failed, attempted)``.
		
		The optional *verbose* argument controls how detailed the summary is.  If the
		verbosity is not specified, then the :class:`DocTestRunner`'s verbosity is
		used.
		
		"""
		pass
		
	


class OutputChecker:


	"""
	A class used to check the whether the actual output from a doctest example
	matches the expected output.  :class:`OutputChecker` defines two methods:
	:meth:`check_output`, which compares a given pair of outputs, and returns true
	if they match; and :meth:`output_difference`, which returns a string describing
	the differences between two outputs.
	
	"""
	
	
	def __init__(self, ):
		pass
	
	def check_output(self, want,got,optionflags):
		"""
		Return ``True`` iff the actual output from an example (*got*) matches the
		expected output (*want*).  These strings are always considered to match if
		they are identical; but depending on what option flags the test runner is
		using, several non-exact match types are also possible.  See section
		:ref:`doctest-options` for more information about option flags.
		
		
		"""
		pass
		
	def output_difference(self, example,got,optionflags):
		"""
		Return a string describing the differences between the expected output for a
		given example (*example*) and the actual output (*got*).  *optionflags* is the
		set of option flags used to compare *want* and *got*.
		
		
		.. ebugging
		"""
		pass
		
	def script__from_examples(self, s):
		"""
		Convert text with examples to a script.
		
		Argument *s* is a string containing doctest examples.  The string is converted
		to a Python script, where doctest examples in *s* are converted to regular code,
		and everything else is converted to Python comments.  The generated script is
		returned as a string. For example, ::
		
		import doctest
		print doctest.script_from_examples(r " " " 
		Set x and y to 1 and 2.
		>>> x, y = 1, 2
		
		Print their sum:
		>>> print x+y
		3
		 " " " )
		
		displays::
		
		# Set x and y to 1 and 2.
		x, y = 1, 2
		#
		# Print their sum:
		print x+y
		# Expected:
		## 3
		
		This function is used internally by other functions (see below), but can also be
		useful when you want to transform an interactive Python session into a Python
		script.
		
		"""
		pass
		
	def testsource(self, module,name):
		"""
		Convert the doctest for an object to a script.
		
		Argument *module* is a module object, or dotted name of a module, containing the
		object whose doctests are of interest.  Argument *name* is the name (within the
		module) of the object with the doctests of interest.  The result is a string,
		containing the object's docstring converted to a Python script, as described for
		:func:`script_from_examples` above.  For example, if module :file:`a.py`
		contains a top-level function :func:`f`, then ::
		
		import a, doctest
		print doctest.testsource(a, "a.f")
		
		prints a script version of function :func:`f`'s docstring, with doctests
		converted to code, and the rest placed in comments.
		
		"""
		pass
		
	def debug(self, module,name,pm):
		"""
		Debug the doctests for an object.
		
		The *module* and *name* arguments are the same as for function
		:func:`testsource` above.  The synthesized Python script for the named object's
		docstring is written to a temporary file, and then that file is run under the
		control of the Python debugger, :mod:`pdb`.
		
		A shallow copy of ``module.__dict__`` is used for both local and global
		execution context.
		
		Optional argument *pm* controls whether post-mortem debugging is used.  If *pm*
		has a true value, the script file is run directly, and the debugger gets
		involved only if the script terminates via raising an unhandled exception.  If
		it does, then post-mortem debugging is invoked, via :func:`pdb.post_mortem`,
		passing the traceback object from the unhandled exception.  If *pm* is not
		specified, or is false, the script is run under the debugger from the start, via
		passing an appropriate :func:`execfile` call to :func:`pdb.run`.
		
		"""
		pass
		
	def debug_src(self, src,pm,globs):
		"""
		Debug the doctests in a string.
		
		This is like function :func:`debug` above, except that a string containing
		doctest examples is specified directly, via the *src* argument.
		
		Optional argument *pm* has the same meaning as in function :func:`debug` above.
		
		Optional argument *globs* gives a dictionary to use as both local and global
		execution context.  If not specified, or ``None``, an empty dictionary is used.
		If specified, a shallow copy of the dictionary is used.
		
		"""
		pass
		
	


class DebugRunner:


	"""
	A subclass of :class:`DocTestRunner` that raises an exception as soon as a
	failure is encountered.  If an unexpected exception occurs, an
	:exc:`UnexpectedException` exception is raised, containing the test, the
	example, and the original exception.  If the output doesn't match, then a
	:exc:`DocTestFailure` exception is raised, containing the test, the example, and
	the actual output.
	
	For information about the constructor parameters and methods, see the
	documentation for :class:`DocTestRunner` in section :ref:`doctest-advanced-api`.
	
	There are two exceptions that may be raised by :class:`DebugRunner` instances:
	
	
	"""
	
	
	def __init__(self, ):
		pass
	
	


