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
	
	
	def __init__(self, methodName='runTest'):
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
	
	
	def __init__(self, testFunc,setUp=None,tearDown=None,description=None):
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
	
	
	def __init__(self, tests=[]):
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
	
	


class TextTestResult:


	"""
	A concrete implementation of :class:`TestResult` used by the
	:class:`TextTestRunner`.
	
	"""
	
	
	def __init__(self, stream,descriptions,verbosity):
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
	
	
	def __init__(self, stream=sys):
		pass
	
	


