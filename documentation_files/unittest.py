#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
""":synopsis: Unit testing framework for Python.
"""
def skip(reason):
	"""
	Unconditionally skip the decorated test.  *reason* should describe why the
	test is being skipped.
	
	"""
	pass
	
def skipIf(condition,reason):
	"""
	Skip the decorated test if *condition* is true.
	
	"""
	pass
	
def skipUnless(condition,reason):
	"""
	Skip the decorated test unless *condition* is true.
	
	"""
	pass
	
def expectedFailure():
	"""
	Mark the test as an expected failure.  If the test fails when run, the test
	is not counted as a failure.
	
	Skipped tests will not have :meth:`setUp` or :meth:`tearDown` run around them.
	Skipped classes will not have :meth:`setUpClass` or :meth:`tearDownClass` run.
	
	
	.. lasses and functions
	---------------------
	
	This section describes in depth the API of :mod:`unittest`.
	
	
	.. est cases
	~~~~~~~~~~
	
	"""
	pass
	
class TestCase:


	"""
	Instances of the :class:`TestCase` class represent the smallest testable units
	in the :mod:`unittest` universe.  This class is intended to be used as a base
	class, with specific tests being implemented by concrete subclasses.  This class
	implements the interface needed by the test runner to allow it to drive the
	test, and methods that the test code can use to check for and report various
	kinds of failure.
	
	Each instance of :class:`TestCase` will run a single test method: the method
	named *methodName*.  If you remember, we had an earlier example that went
	something like this::
	
	def suite():
	suite = unittest.TestSuite()
	suite.addTest(WidgetTestCase('test_default_size'))
	suite.addTest(WidgetTestCase('test_resize'))
	return suite
	
	Here, we create two instances of :class:`WidgetTestCase`, each of which runs a
	single test.
	
	*methodName* defaults to :meth:`runTest`.
	
	:class:`TestCase` instances provide three groups of methods: one group used
	to run the test, another used by the test implementation to check conditions
	and report failures, and some inquiry methods allowing information about the
	test itself to be gathered.
	
	Methods in the first group (running the test) are:
	
	
	"""
	
	
	def __init__(self, ):
		pass
	
	def setUp(self, ):
		"""
		Method called to prepare the test fixture.  This is called immediately
		before calling the test method; any exception raised by this method will
		be considered an error rather than a test failure. The default
		implementation does nothing.
		
		
		"""
		pass
		
	def tearDown(self, ):
		"""
		Method called immediately after the test method has been called and the
		result recorded.  This is called even if the test method raised an
		exception, so the implementation in subclasses may need to be particularly
		careful about checking internal state.  Any exception raised by this
		method will be considered an error rather than a test failure.  This
		method will only be called if the :meth:`setUp` succeeds, regardless of
		the outcome of the test method. The default implementation does nothing.
		
		
		"""
		pass
		
	def setUpClass(self, ):
		"""
		A class method called before tests in an individual class run.
		``setUpClass`` is called with the class as the only argument
		and must be decorated as a :func:`classmethod`::
		
		@classmethod
		def setUpClass(cls):
		*more
		
		See `Class and Module Fixtures`_ for more details.
		
		"""
		pass
		
	def tearDownClass(self, ):
		"""
		A class method called after tests in an individual class have run.
		``tearDownClass`` is called with the class as the only argument
		and must be decorated as a :meth:`classmethod`::
		
		@classmethod
		def tearDownClass(cls):
		*more
		
		See `Class and Module Fixtures`_ for more details.
		
		"""
		pass
		
	def run(self, result=None):
		"""
		Run the test, collecting the result into the test result object passed as
		*result*.  If *result* is omitted or ``None``, a temporary result
		object is created (by calling the :meth:`defaultTestResult` method) and
		used. The result object is not returned to :meth:`run`'s caller.
		
		The same effect may be had by simply calling the :class:`TestCase`
		instance.
		
		
		"""
		pass
		
	def skipTest(self, reason):
		"""
		Calling this during a test method or :meth:`setUp` skips the current
		test.  See :ref:`unittest-skipping` for more information.
		
		"""
		pass
		
	def debug(self, ):
		"""
		Run the test without collecting the result.  This allows exceptions raised
		by the test to be propagated to the caller, and can be used to support
		running tests under a debugger.
		
		..   The :class:`TestCase` class provides a number of methods to check for and
		report failures, such as:
		
		+-----------------------------------------+-----------------------------+---------------+
		| Method                                  | Checks that                 | New in        |
		+=========================================+=============================+===============+
		| :meth:`assertEqual(a, b)                | ``a == b``                  |               |
		| <TestCase.assertEqual>`                 |                             |               |
		+-----------------------------------------+-----------------------------+---------------+
		| :meth:`assertNotEqual(a, b)             | ``a != b``                  |               |
		| <TestCase.assertNotEqual>`              |                             |               |
		+-----------------------------------------+-----------------------------+---------------+
		| :meth:`assertTrue(x)                    | ``bool(x) is True``         |               |
		| <TestCase.assertTrue>`                  |                             |               |
		+-----------------------------------------+-----------------------------+---------------+
		| :meth:`assertFalse(x)                   | ``bool(x) is False``        |               |
		| <TestCase.assertFalse>`                 |                             |               |
		+-----------------------------------------+-----------------------------+---------------+
		| :meth:`assertIs(a, b)                   | ``a is b``                  | 2.7           |
		| <TestCase.assertIs>`                    |                             |               |
		+-----------------------------------------+-----------------------------+---------------+
		| :meth:`assertIsNot(a, b)                | ``a is not b``              | 2.7           |
		| <TestCase.assertIsNot>`                 |                             |               |
		+-----------------------------------------+-----------------------------+---------------+
		| :meth:`assertIsNone(x)                  | ``x is None``               | 2.7           |
		| <TestCase.assertIsNone>`                |                             |               |
		+-----------------------------------------+-----------------------------+---------------+
		| :meth:`assertIsNotNone(x)               | ``x is not None``           | 2.7           |
		| <TestCase.assertIsNotNone>`             |                             |               |
		+-----------------------------------------+-----------------------------+---------------+
		| :meth:`assertIn(a, b)                   | ``a in b``                  | 2.7           |
		| <TestCase.assertIn>`                    |                             |               |
		+-----------------------------------------+-----------------------------+---------------+
		| :meth:`assertNotIn(a, b)                | ``a not in b``              | 2.7           |
		| <TestCase.assertNotIn>`                 |                             |               |
		+-----------------------------------------+-----------------------------+---------------+
		| :meth:`assertIsInstance(a, b)           | ``isinstance(a, b)``        | 2.7           |
		| <TestCase.assertIsInstance>`            |                             |               |
		+-----------------------------------------+-----------------------------+---------------+
		| :meth:`assertNotIsInstance(a, b)        | ``not isinstance(a, b)``    | 2.7           |
		| <TestCase.assertNotIsInstance>`         |                             |               |
		+-----------------------------------------+-----------------------------+---------------+
		
		All the assert methods (except :meth:`assertRaises`,
		:meth:`assertRaisesRegexp`)
		accept a *msg* argument that, if specified, is used as the error message on
		failure (see also :data:`longMessage`).
		
		"""
		pass
		
	def assertEqual(self, first,second,msg=None):
		"""
		Test that *first* and *second* are equal.  If the values do not compare
		equal, the test will fail.
		
		In addition, if *first* and *second* are the exact same type and one of
		list, tuple, dict, set, frozenset or unicode or any type that a subclass
		registers with :meth:`addTypeEqualityFunc` the type specific equality
		function will be called in order to generate a more useful default
		error message (see also the :ref:`list of type-specific methods
		<type-specific-methods>`).
		
		"""
		pass
		
	def assertNotEqual(self, first,second,msg=None):
		"""
		Test that *first* and *second* are not equal.  If the values do compare
		equal, the test will fail.
		
		"""
		pass
		
	def assertTrue(self, expr,msg=None):
		"""assertFalse(expr, msg=None)
		
		Test that *expr* is true (or false).
		
		Note that this is equivalent to ``bool(expr) is True`` and not to ``expr
		is True`` (use ``assertIs(expr, True)`` for the latter).  This method
		should also be avoided when more specific methods are available (e.g.
		``assertEqual(a, b)`` instead of ``assertTrue(a == b)``), because they
		provide a better error message in case of failure.
		
		
		"""
		pass
		
	def assertIs(self, first,second,msg=None):
		"""assertIsNot(first, second, msg=None)
		
		Test that *first* and *second* evaluate (or don't evaluate) to the same object.
		
		"""
		pass
		
	def assertIsNone(self, expr,msg=None):
		"""assertIsNotNone(expr, msg=None)
		
		Test that *expr* is (or is not) None.
		
		"""
		pass
		
	def assertIn(self, first,second,msg=None):
		"""assertNotIn(first, second, msg=None)
		
		Test that *first* is (or is not) in *second*.
		
		"""
		pass
		
	def assertIsInstance(self, obj,cls,msg=None):
		"""assertNotIsInstance(obj, cls, msg=None)
		
		Test that *obj* is (or is not) an instance of *cls* (which can be a
		class or a tuple of classes, as supported by :func:`isinstance`).
		
		"""
		pass
		
	def assertRaises(self, exception,callable,args,kwds):
		"""assertRaises(exception)
		
		Test that an exception is raised when *callable* is called with any
		positional or keyword arguments that are also passed to
		:meth:`assertRaises`.  The test passes if *exception* is raised, is an
		error if another exception is raised, or fails if no exception is raised.
		To catch any of a group of exceptions, a tuple containing the exception
		classes may be passed as *exception*.
		
		If only the *exception* argument is given, returns a context manager so
		that the code under test can be written inline rather than as a function::
		
		with self.assertRaises(SomeException):
		do_something()
		
		The context manager will store the caught exception object in its
		:attr:`exception` attribute.  This can be useful if the intention
		is to perform additional checks on the exception raised::
		
		with self.assertRaises(SomeException) as cm:
		do_something()
		
		the_exception = cm.exception
		self.assertEqual(the_exception.error_code, 3)
		
		"""
		pass
		
	def assertRaisesRegexp(self, exception,regexp,callable,args,kwds):
		"""assertRaisesRegexp(exception, regexp)
		
		Like :meth:`assertRaises` but also tests that *regexp* matches
		on the string representation of the raised exception.  *regexp* may be
		a regular expression object or a string containing a regular expression
		suitable for use by :func:`re.search`.  Examples::
		
		self.assertRaisesRegexp(ValueError, 'invalid literal for.*XYZ$',
		int, 'XYZ')
		
		or::
		
		with self.assertRaisesRegexp(ValueError, 'literal'):
		int('XYZ')
		
		"""
		pass
		
	def assertAlmostEqual(self, first,second,places=7,msg=None,delta=None):
		"""assertNotAlmostEqual(first, second, places=7, msg=None, delta=None)
		
		Test that *first* and *second* are approximately (or not approximately)
		equal by computing the difference, rounding to the given number of
		decimal *places* (default 7), and comparing to zero.  Note that these
		methods round the values to the given number of *decimal places* (i.e.
		like the :func:`round` function) and not *significant digits*.
		
		If *delta* is supplied instead of *places* then the difference
		between *first* and *second* must be less (or more) than *delta*.
		
		Supplying both *delta* and *places* raises a ``TypeError``.
		
		"""
		pass
		
	def assertGreater(self, first,second,msg=None):
		"""assertGreaterEqual(first, second, msg=None)
		assertLess(first, second, msg=None)
		assertLessEqual(first, second, msg=None)
		
		Test that *first* is respectively >, >=, < or <= than *second* depending
		on the method name.  If not, the test will fail::
		
		>>> self.assertGreaterEqual(3, 4)
		AssertionError: "3" unexpectedly not greater than or equal to "4"
		
		"""
		pass
		
	def assertRegexpMatches(self, text,regexp,msg=None):
		"""
		Test that a *regexp* search matches *text*.  In case
		of failure, the error message will include the pattern and the *text* (or
		the pattern and the part of *text* that unexpectedly matched).  *regexp*
		may be a regular expression object or a string containing a regular
		expression suitable for use by :func:`re.search`.
		
		"""
		pass
		
	def assertNotRegexpMatches(self, text,regexp,msg=None):
		"""
		Verifies that a *regexp* search does not match *text*.  Fails with an error
		message including the pattern and the part of *text* that matches.  *regexp*
		may be a regular expression object or a string containing a regular
		expression suitable for use by :func:`re.search`.
		
		"""
		pass
		
	def assertItemsEqual(self, actual,expected,msg=None):
		"""
		Test that sequence *expected* contains the same elements as *actual*,
		regardless of their order. When they don't, an error message listing the
		differences between the sequences will be generated.
		
		Duplicate elements are *not* ignored when comparing *actual* and
		*expected*. It verifies if each element has the same count in both
		sequences. It is the equivalent of ``assertEqual(sorted(expected),
		sorted(actual))`` but it works with sequences of unhashable objects as
		well.
		
		"""
		pass
		
	def assertDictContainsSubset(self, expected,actual,msg=None):
		"""
		Tests whether the key/value pairs in dictionary *actual* are a
		superset of those in *expected*.  If not, an error message listing
		the missing keys and mismatched values is generated.
		
		"""
		pass
		
	def addTypeEqualityFunc(self, typeobj,function):
		"""
		Registers a type-specific method called by :meth:`assertEqual` to check
		if two objects of exactly the same *typeobj* (not subclasses) compare
		equal.  *function* must take two positional arguments and a third msg=None
		keyword argument just as :meth:`assertEqual` does.  It must raise
		:data:`self.failureException(msg) <failureException>` when inequality
		between the first two parameters is detected -- possibly providing useful
		information and explaining the inequalities in details in the error
		message.
		
		"""
		pass
		
	def assertMultiLineEqual(self, first,second,msg=None):
		"""
		Test that the multiline string *first* is equal to the string *second*.
		When not equal a diff of the two strings highlighting the differences
		will be included in the error message. This method is used by default
		when comparing strings with :meth:`assertEqual`.
		
		"""
		pass
		
	def assertSequenceEqual(self, seq1,seq2,msg=None,seq_type=None):
		"""
		Tests that two sequences are equal.  If a *seq_type* is supplied, both
		*seq1* and *seq2* must be instances of *seq_type* or a failure will
		be raised.  If the sequences are different an error message is
		constructed that shows the difference between the two.
		
		This method is not called directly by :meth:`assertEqual`, but
		it's used to implement :meth:`assertListEqual` and
		:meth:`assertTupleEqual`.
		
		"""
		pass
		
	def assertListEqual(self, list1,list2,msg=None):
		"""assertTupleEqual(tuple1, tuple2, msg=None)
		
		Tests that two lists or tuples are equal.  If not an error message is
		constructed that shows only the differences between the two.  An error
		is also raised if either of the parameters are of the wrong type.
		These methods are used by default when comparing lists or tuples with
		:meth:`assertEqual`.
		
		"""
		pass
		
	def assertSetEqual(self, set1,set2,msg=None):
		"""
		Tests that two sets are equal.  If not, an error message is constructed
		that lists the differences between the sets.  This method is used by
		default when comparing sets or frozensets with :meth:`assertEqual`.
		
		Fails if either of *set1* or *set2* does not have a :meth:`set.difference`
		method.
		
		"""
		pass
		
	def assertDictEqual(self, expected,actual,msg=None):
		"""
		Test that two dictionaries are equal.  If not, an error message is
		constructed that shows the differences in the dictionaries. This
		method will be used by default to compare dictionaries in
		calls to :meth:`assertEqual`.
		
		"""
		pass
		
	def fail(self, msg=None):
		"""
		Signals a test failure unconditionally, with *msg* or ``None`` for
		the error message.
		
		
		"""
		pass
		
	def countTestCases(self, ):
		"""
		Return the number of tests represented by this test object.  For
		:class:`TestCase` instances, this will always be ``1``.
		
		
		"""
		pass
		
	def defaultTestResult(self, ):
		"""
		Return an instance of the test result class that should be used for this
		test case class (if no other result instance is provided to the
		:meth:`run` method).
		
		For :class:`TestCase` instances, this will always be an instance of
		:class:`TestResult`; subclasses of :class:`TestCase` should override this
		as necessary.
		
		
		"""
		pass
		
	def id(self, ):
		"""
		Return a string identifying the specific test case.  This is usually the
		full name of the test method, including the module and class name.
		
		
		"""
		pass
		
	def shortDescription(self, ):
		"""
		Returns a description of the test, or ``None`` if no description
		has been provided.  The default implementation of this method
		returns the first line of the test method's docstring, if available,
		or :const:`None`.
		
		
		
		"""
		pass
		
	def addCleanup(self, function,args,kwargs):
		"""
		Add a function to be called after :meth:`tearDown` to cleanup resources
		used during the test. Functions will be called in reverse order to the
		order they are added (LIFO). They are called with any arguments and
		keyword arguments passed into :meth:`addCleanup` when they are
		added.
		
		If :meth:`setUp` fails, meaning that :meth:`tearDown` is not called,
		then any cleanup functions added will still be called.
		
		"""
		pass
		
	def doCleanups(self, ):
		"""
		This method is called unconditionally after :meth:`tearDown`, or
		after :meth:`setUp` if :meth:`setUp` raises an exception.
		
		It is responsible for calling all the cleanup functions added by
		:meth:`addCleanup`. If you need cleanup functions to be called
		*prior* to :meth:`tearDown` then you can call :meth:`doCleanups`
		yourself.
		
		:meth:`doCleanups` pops methods off the stack of cleanup
		functions one at a time, so it can be called at any time.
		
		"""
		pass
		
	


class FunctionTestCase:


	"""
	This class implements the portion of the :class:`TestCase` interface which
	allows the test runner to drive the test, but does not provide the methods
	which test code can use to check and report errors.  This is used to create
	test cases using legacy test code, allowing it to be integrated into a
	:mod:`unittest`-based test framework.
	
	
	Deprecated aliases
	##################
	
	For historical reasons, some of the :class:`TestCase` methods had one or more
	aliases that are now deprecated.  The following table lists the correct names
	along with their deprecated aliases:
	
	==============================  ===============================
	Method Name                     Deprecated alias(es)
	==============================  ===============================
	:meth:`.assertEqual`            failUnlessEqual, assertEquals
	:meth:`.assertNotEqual`         failIfEqual
	:meth:`.assertTrue`             failUnless, assert\_
	:meth:`.assertFalse`            failIf
	:meth:`.assertRaises`           failUnlessRaises
	:meth:`.assertAlmostEqual`      failUnlessAlmostEqual
	:meth:`.assertNotAlmostEqual`   failIfAlmostEqual
	==============================  ===============================
	
	"""
	
	
	def __init__(self, ):
		pass
	
	


class TestSuite:


	"""
	This class represents an aggregation of individual tests cases and test suites.
	The class presents the interface needed by the test runner to allow it to be run
	as any other test case.  Running a :class:`TestSuite` instance is the same as
	iterating over the suite, running each test individually.
	
	If *tests* is given, it must be an iterable of individual test cases or other
	test suites that will be used to build the suite initially. Additional methods
	are provided to add test cases and suites to the collection later on.
	
	:class:`TestSuite` objects behave much like :class:`TestCase` objects, except
	they do not actually implement a test.  Instead, they are used to aggregate
	tests into groups of tests that should be run together. Some additional
	methods are available to add tests to :class:`TestSuite` instances:
	
	
	"""
	
	
	def __init__(self, ):
		pass
	
	def addTest(self, test):
		"""
		Add a :class:`TestCase` or :class:`TestSuite` to the suite.
		
		
		"""
		pass
		
	def addTests(self, tests):
		"""
		Add all the tests from an iterable of :class:`TestCase` and :class:`TestSuite`
		instances to this test suite.
		
		This is equivalent to iterating over *tests*, calling :meth:`addTest` for
		each element.
		
		:class:`TestSuite` shares the following methods with :class:`TestCase`:
		
		
		"""
		pass
		
	def run(self, result):
		"""
		Run the tests associated with this suite, collecting the result into the
		test result object passed as *result*.  Note that unlike
		:meth:`TestCase.run`, :meth:`TestSuite.run` requires the result object to
		be passed in.
		
		
		"""
		pass
		
	def debug(self, ):
		"""
		Run the tests associated with this suite without collecting the
		result. This allows exceptions raised by the test to be propagated to the
		caller and can be used to support running tests under a debugger.
		
		
		"""
		pass
		
	def countTestCases(self, ):
		"""
		Return the number of tests represented by this test object, including all
		individual tests and sub-suites.
		
		
		"""
		pass
		
	def __iter__(self, ):
		"""
		Tests grouped by a :class:`TestSuite` are always accessed by iteration.
		Subclasses can lazily provide tests by overriding :meth:`__iter__`. Note
		that this method maybe called several times on a single suite
		(for example when counting tests or comparing for equality)
		so the tests returned must be the same for repeated iterations.
		
		"""
		pass
		
	


class TestLoader:


	"""
	The :class:`TestLoader` class is used to create test suites from classes and
	modules.  Normally, there is no need to create an instance of this class; the
	:mod:`unittest` module provides an instance that can be shared as
	``unittest.defaultTestLoader``. Using a subclass or instance, however, allows
	customization of some configurable properties.
	
	:class:`TestLoader` objects have the following methods:
	
	
	"""
	
	
	def __init__(self, ):
		pass
	
	def loadTestsFromTestCase(self, testCaseClass):
		"""
		Return a suite of all tests cases contained in the :class:`TestCase`\ -derived
		:class:`testCaseClass`.
		
		
		"""
		pass
		
	def loadTestsFromModule(self, module):
		"""
		Return a suite of all tests cases contained in the given module. This
		method searches *module* for classes derived from :class:`TestCase` and
		creates an instance of the class for each test method defined for the
		class.
		
		"""
		pass
		
	def loadTestsFromName(self, name,module=None):
		"""
		Return a suite of all tests cases given a string specifier.
		
		The specifier *name* is a "dotted name" that may resolve either to a
		module, a test case class, a test method within a test case class, a
		:class:`TestSuite` instance, or a callable object which returns a
		:class:`TestCase` or :class:`TestSuite` instance.  These checks are
		applied in the order listed here; that is, a method on a possible test
		case class will be picked up as "a test method within a test case class",
		rather than "a callable object".
		
		For example, if you have a module :mod:`SampleTests` containing a
		:class:`TestCase`\ -derived class :class:`SampleTestCase` with three test
		methods (:meth:`test_one`, :meth:`test_two`, and :meth:`test_three`), the
		specifier ``'SampleTests.SampleTestCase'`` would cause this method to
		return a suite which will run all three test methods. Using the specifier
		``'SampleTests.SampleTestCase.test_two'`` would cause it to return a test
		suite which will run only the :meth:`test_two` test method. The specifier
		can refer to modules and packages which have not been imported; they will
		be imported as a side-effect.
		
		The method optionally resolves *name* relative to the given *module*.
		
		
		"""
		pass
		
	def loadTestsFromNames(self, names,module=None):
		"""
		Similar to :meth:`loadTestsFromName`, but takes a sequence of names rather
		than a single name.  The return value is a test suite which supports all
		the tests defined for each name.
		
		
		"""
		pass
		
	def getTestCaseNames(self, testCaseClass):
		"""
		Return a sorted sequence of method names found within *testCaseClass*;
		this should be a subclass of :class:`TestCase`.
		
		
		"""
		pass
		
	


class TestResult:


	"""
	This class is used to compile information about which tests have succeeded
	and which have failed.
	
	A :class:`TestResult` object stores the results of a set of tests.  The
	:class:`TestCase` and :class:`TestSuite` classes ensure that results are
	properly recorded; test authors do not need to worry about recording the
	outcome of tests.
	
	Testing frameworks built on top of :mod:`unittest` may want access to the
	:class:`TestResult` object generated by running a set of tests for reporting
	purposes; a :class:`TestResult` instance is returned by the
	:meth:`TestRunner.run` method for this purpose.
	
	:class:`TestResult` instances have the following attributes that will be of
	interest when inspecting the results of running a set of tests:
	
	
	"""
	
	
	def __init__(self, ):
		pass
	
	def wasSuccessful(self, ):
		"""
		Return ``True`` if all tests run so far have passed, otherwise returns
		``False``.
		
		
		"""
		pass
		
	def stop(self, ):
		"""
		This method can be called to signal that the set of tests being run should
		be aborted by setting the :attr:`shouldStop` attribute to ``True``.
		:class:`TestRunner` objects should respect this flag and return without
		running any additional tests.
		
		For example, this feature is used by the :class:`TextTestRunner` class to
		stop the test framework when the user signals an interrupt from the
		keyboard.  Interactive tools which provide :class:`TestRunner`
		implementations can use this in a similar manner.
		
		The following methods of the :class:`TestResult` class are used to maintain
		the internal data structures, and may be extended in subclasses to support
		additional reporting requirements.  This is particularly useful in building
		tools which support interactive reporting while tests are being run.
		
		
		"""
		pass
		
	def startTest(self, test):
		"""
		Called when the test case *test* is about to be run.
		
		"""
		pass
		
	def stopTest(self, test):
		"""
		Called after the test case *test* has been executed, regardless of the
		outcome.
		
		"""
		pass
		
	def startTestRun(self, test):
		"""
		Called once before any tests are executed.
		
		"""
		pass
		
	def stopTestRun(self, test):
		"""
		Called once after all tests are executed.
		
		"""
		pass
		
	def addError(self, test,err):
		"""
		Called when the test case *test* raises an unexpected exception *err* is a
		tuple of the form returned by :func:`sys.exc_info`: ``(type, value,
		traceback)``.
		
		The default implementation appends a tuple ``(test, formatted_err)`` to
		the instance's :attr:`errors` attribute, where *formatted_err* is a
		formatted traceback derived from *err*.
		
		
		"""
		pass
		
	def addFailure(self, test,err):
		"""
		Called when the test case *test* signals a failure. *err* is a tuple of
		the form returned by :func:`sys.exc_info`: ``(type, value, traceback)``.
		
		The default implementation appends a tuple ``(test, formatted_err)`` to
		the instance's :attr:`failures` attribute, where *formatted_err* is a
		formatted traceback derived from *err*.
		
		
		"""
		pass
		
	def addSuccess(self, test):
		"""
		Called when the test case *test* succeeds.
		
		The default implementation does nothing.
		
		
		"""
		pass
		
	def addSkip(self, test,reason):
		"""
		Called when the test case *test* is skipped.  *reason* is the reason the
		test gave for skipping.
		
		The default implementation appends a tuple ``(test, reason)`` to the
		instance's :attr:`skipped` attribute.
		
		
		"""
		pass
		
	def addExpectedFailure(self, test,err):
		"""
		Called when the test case *test* fails, but was marked with the
		:func:`expectedFailure` decorator.
		
		The default implementation appends a tuple ``(test, formatted_err)`` to
		the instance's :attr:`expectedFailures` attribute, where *formatted_err*
		is a formatted traceback derived from *err*.
		
		
		"""
		pass
		
	def addUnexpectedSuccess(self, test):
		"""
		Called when the test case *test* was marked with the
		:func:`expectedFailure` decorator, but succeeded.
		
		The default implementation appends the test to the instance's
		:attr:`unexpectedSuccesses` attribute.
		
		"""
		pass
		
	


class TextTestResult:


	"""
	A concrete implementation of :class:`TestResult` used by the
	:class:`TextTestRunner`.
	
	"""
	
	
	def __init__(self, ):
		pass
	
	"""
	Instance of the :class:`TestLoader` class intended to be shared.  If no
	customization of the :class:`TestLoader` is needed, this instance can be used
	instead of repeatedly creating new instances.
	
	
	"""
	defaultTestLoader = None
	


class TextTestRunner:


	"""
	A basic test runner implementation which prints results on standard error.  It
	has a few configurable parameters, but is essentially very simple.  Graphical
	applications which run test suites should provide alternate implementations.
	
	"""
	
	
	def __init__(self, ):
		pass
	
	def _makeResult(self, ):
		"""
		This method returns the instance of ``TestResult`` used by :meth:`run`.
		It is not intended to be called directly, but can be overridden in
		subclasses to provide a custom ``TestResult``.
		
		``_makeResult()`` instantiates the class or callable passed in the
		``TextTestRunner`` constructor as the ``resultclass`` argument. It
		defaults to :class:`TextTestResult` if no ``resultclass`` is provided.
		The result class is instantiated with the following arguments::
		
		stream, descriptions, verbosity
		
		
		"""
		pass
		
	def main(self, module,defaultTest,argv,testRunner,testLoader,exit,verbosity,failfast,catchbreak,buffer):
		"""
		A command-line program that runs a set of tests; this is primarily for making
		test modules conveniently executable.  The simplest use for this function is to
		include the following line at the end of a test script::
		
		if __name__ == '__main__':
		unittest.main()
		
		You can run tests with more detailed information by passing in the verbosity
		argument::
		
		if __name__ == '__main__':
		unittest.main(verbosity=2)
		
		The *testRunner* argument can either be a test runner class or an already
		created instance of it. By default ``main`` calls :func:`sys.exit` with
		an exit code indicating success or failure of the tests run.
		
		``main`` supports being used from the interactive interpreter by passing in the
		argument ``exit=False``. This displays the result on standard output without
		calling :func:`sys.exit`::
		
		>>> from unittest import main
		>>> main(module='test_module', exit=False)
		
		The ``failfast``, ``catchbreak`` and ``buffer`` parameters have the same
		effect as the same-name `command-line options`_.
		
		Calling ``main`` actually returns an instance of the ``TestProgram`` class.
		This stores the result of the tests run as the ``result`` attribute.
		
		"""
		pass
		
	def installHandler(self, ):
		"""
		Install the control-c handler. When a :const:`signal.SIGINT` is received
		(usually in response to the user pressing control-c) all registered results
		have :meth:`~TestResult.stop` called.
		
		"""
		pass
		
	def registerResult(self, result):
		"""
		Register a :class:`TestResult` object for control-c handling. Registering a
		result stores a weak reference to it, so it doesn't prevent the result from
		being garbage collected.
		
		Registering a :class:`TestResult` object has no side-effects if control-c
		handling is not enabled, so test frameworks can unconditionally register
		all results they create independently of whether or not handling is enabled.
		
		"""
		pass
		
	def removeResult(self, result):
		"""
		Remove a registered result. Once a result has been removed then
		:meth:`~TestResult.stop` will no longer be called on that result object in
		response to a control-c.
		
		"""
		pass
		
	def removeHandler(self, function=None):
		"""
		When called without arguments this function removes the control-c handler
		if it has been installed. This function can also be used as a test decorator
		to temporarily remove the handler whilst the test is being executed::
		
		@unittest.removeHandler
		def test_signal_handling(self):
		*more
		
		"""
		pass
		
	


