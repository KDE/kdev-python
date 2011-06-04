#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
""":synopsis: Support for Python regression tests.

"""
"""
:const:`True` when verbose output is enabled. Should be checked when more
detailed information is desired about a running test. *verbose* is set by
:mod:`test.regrtest`.


"""
verbose = None
"""
:const:`True` when Unicode support is available.


"""
have_unicode = None
"""
:const:`True` if the running interpreter is Jython.


"""
is_jython = None
"""
Set to a name that is safe to use as the name of a temporary file.  Any
temporary file that is created should be closed and unlinked (removed).

The :mod:`test.test_support` module defines the following functions:


"""
TESTFN = None
def forget(module_name):
	"""
	Remove the module named *module_name* from ``sys.modules`` and delete any
	byte-compiled files of the module.
	
	
	"""
	pass
	
def is_resource_enabled(resource):
	"""
	Return :const:`True` if *resource* is enabled and available. The list of
	available resources is only set when :mod:`test.regrtest` is executing the
	tests.
	
	
	"""
	pass
	
def requires(resource,msg):
	"""
	Raise :exc:`ResourceDenied` if *resource* is not available. *msg* is the
	argument to :exc:`ResourceDenied` if it is raised. Always returns
	:const:`True` if called by a function whose ``__name__`` is ``'__main__'``.
	Used when tests are executed by :mod:`test.regrtest`.
	
	
	"""
	pass
	
def findfile(filename):
	"""
	Return the path to the file named *filename*. If no match is found
	*filename* is returned. This does not equal a failure since it could be the
	path to the file.
	
	
	"""
	pass
	
def run_unittest(_classes):
	"""
	Execute :class:`unittest.TestCase` subclasses passed to the function. The
	function scans the classes for methods starting with the prefix ``test_``
	and executes the tests individually.
	
	It is also legal to pass strings as parameters; these should be keys in
	``sys.modules``. Each associated module will be scanned by
	``unittest.TestLoader.loadTestsFromModule()``. This is usually seen in the
	following :func:`test_main` function::
	
	def test_main():
	test_support.run_unittest(__name__)
	
	This will run all tests defined in the named module.
	
	
	"""
	pass
	
def check_warnings(filters,quiet=True):
	"""
	A convenience wrapper for :func:`warnings.catch_warnings()` that makes it
	easier to test that a warning was correctly raised.  It is approximately
	equivalent to calling ``warnings.catch_warnings(record=True)`` with
	:meth:`warnings.simplefilter` set to ``always`` and with the option to
	automatically validate the results that are recorded.
	
	``check_warnings`` accepts 2-tuples of the form ``("message regexp",
	WarningCategory)`` as positional arguments. If one or more *filters* are
	provided, or if the optional keyword argument *quiet* is :const:`False`,
	it checks to make sure the warnings are as expected:  each specified filter
	must match at least one of the warnings raised by the enclosed code or the
	test fails, and if any warnings are raised that do not match any of the
	specified filters the test fails.  To disable the first of these checks,
	set *quiet* to :const:`True`.
	
	If no arguments are specified, it defaults to::
	
	check_warnings(("", Warning), quiet=True)
	
	In this case all warnings are caught and no errors are raised.
	
	On entry to the context manager, a :class:`WarningRecorder` instance is
	returned. The underlying warnings list from
	:func:`~warnings.catch_warnings` is available via the recorder object's
	:attr:`warnings` attribute.  As a convenience, the attributes of the object
	representing the most recent warning can also be accessed directly through
	the recorder object (see example below).  If no warning has been raised,
	then any of the attributes that would otherwise be expected on an object
	representing a warning will return :const:`None`.
	
	The recorder object also has a :meth:`reset` method, which clears the
	warnings list.
	
	The context manager is designed to be used like this::
	
	with check_warnings(("assertion is always true", SyntaxWarning),
	("", UserWarning)):
	exec('assert(False, "Hey!")')
	warnings.warn(UserWarning("Hide me!"))
	
	In this case if either warning was not raised, or some other warning was
	raised, :func:`check_warnings` would raise an error.
	
	When a test needs to look more deeply into the warnings, rather than
	just checking whether or not they occurred, code like this can be used::
	
	with check_warnings(quiet=True) as w:
	warnings.warn("foo")
	assert str(w.args[0]) == "foo"
	warnings.warn("bar")
	assert str(w.args[0]) == "bar"
	assert str(w.warnings[0].args[0]) == "foo"
	assert str(w.warnings[1].args[0]) == "bar"
	w.reset()
	assert len(w.warnings) == 0
	
	Here all warnings will be caught, and the test code tests the captured
	warnings directly.
	
	"""
	pass
	
def check_py3k_warnings(filters,quiet=False):
	"""
	Similar to :func:`check_warnings`, but for Python 3 compatibility warnings.
	If ``sys.py3kwarning == 1``, it checks if the warning is effectively raised.
	If ``sys.py3kwarning == 0``, it checks that no warning is raised.  It
	accepts 2-tuples of the form ``("message regexp", WarningCategory)`` as
	positional arguments.  When the optional keyword argument *quiet* is
	:const:`True`, it does not fail if a filter catches nothing.  Without
	arguments, it defaults to::
	
	check_py3k_warnings(("", DeprecationWarning), quiet=False)
	
	"""
	pass
	
def captured_stdout():
	"""
	This is a context manager that runs the :keyword:`with` statement body using
	a :class:`StringIO.StringIO` object as sys.stdout.  That object can be
	retrieved using the ``as`` clause of the :keyword:`with` statement.
	
	Example use::
	
	with captured_stdout() as s:
	print "hello"
	assert s.getvalue() == "hello"
	
	"""
	pass
	
def import_module(name,deprecated=False):
	"""
	This function imports and returns the named module. Unlike a normal
	import, this function raises :exc:`unittest.SkipTest` if the module
	cannot be imported.
	
	Module and package deprecation messages are suppressed during this import
	if *deprecated* is :const:`True`.
	
	"""
	pass
	
def import_fresh_module(name,fresh=(),blocked=(),deprecated=False):
	"""
	This function imports and returns a fresh copy of the named Python module
	by removing the named module from ``sys.modules`` before doing the import.
	Note that unlike :func:`reload`, the original module is not affected by
	this operation.
	
	*fresh* is an iterable of additional module names that are also removed
	from the ``sys.modules`` cache before doing the import.
	
	*blocked* is an iterable of module names that are replaced with :const:`0`
	in the module cache during the import to ensure that attempts to import
	them raise :exc:`ImportError`.
	
	The named module and any modules named in the *fresh* and *blocked*
	parameters are saved before starting the import and then reinserted into
	``sys.modules`` when the fresh import is complete.
	
	Module and package deprecation messages are suppressed during this import
	if *deprecated* is :const:`True`.
	
	This function will raise :exc:`unittest.SkipTest` is the named module
	cannot be imported.
	
	Example use::
	
	# Get copies of the warnings module for testing without
	# affecting the version being used by the rest of the test suite
	# One copy uses the C implementation, the other is forced to use
	# the pure Python fallback implementation
	py_warnings = import_fresh_module('warnings', blocked=['_warnings'])
	c_warnings = import_fresh_module('warnings', fresh=['_warnings'])
	
	"""
	pass
	
class TransientResource:


	"""
	Instances are a context manager that raises :exc:`ResourceDenied` if the
	specified exception type is raised.  Any keyword arguments are treated as
	attribute/value pairs to be compared against any exception raised within the
	:keyword:`with` statement.  Only if all pairs match properly against
	attributes on the exception is :exc:`ResourceDenied` raised.
	
	"""
	
	
	def __init__(self, ):
		pass
	
	


class EnvironmentVarGuard:


	"""
	Class used to temporarily set or unset environment variables.  Instances can
	be used as a context manager and have a complete dictionary interface for
	querying/modifying the underlying ``os.environ``. After exit from the
	context manager all changes to environment variables done through this
	instance will be rolled back.
	
	"""
	
	
	def __init__(self, ):
		pass
	
	def set(self, envvar,value):
		"""
		Temporarily set the environment variable ``envvar`` to the value of
		``value``.
		
		
		"""
		pass
		
	def unset(self, envvar):
		"""
		Temporarily unset the environment variable ``envvar``.
		
		
		"""
		pass
		
	


class WarningsRecorder:


	"""
	Class used to record warnings for unit tests. See documentation of
	:func:`check_warnings` above for more details.
	
	"""
	
	
	def __init__(self, ):
		pass
	
	


