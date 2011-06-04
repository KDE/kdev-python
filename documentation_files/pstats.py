#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
""":synopsis: Statistics object for use with the profiler.


"""
class Stats:


	"""
	This class constructor creates an instance of a "statistics object" from a
	*filename* (or set of filenames).  :class:`Stats` objects are manipulated by
	methods, in order to print useful reports.  You may specify an alternate output
	stream by giving the keyword argument, ``stream``.
	
	The file selected by the above constructor must have been created by the
	corresponding version of :mod:`profile` or :mod:`cProfile`.  To be specific,
	there is *no* file compatibility guaranteed with future versions of this
	profiler, and there is no compatibility with files produced by other profilers.
	If several files are provided, all the statistics for identical functions will
	be coalesced, so that an overall view of several processes can be considered in
	a single report.  If additional files need to be combined with data in an
	existing :class:`Stats` object, the :meth:`add` method can be used.
	
	.. he old system profiler).
	
	"""
	
	
	def __init__(self, ):
		pass
	
	def strip_dirs(self, ):
		"""
		This method for the :class:`Stats` class removes all leading path information
		from file names.  It is very useful in reducing the size of the printout to fit
		within (close to) 80 columns.  This method modifies the object, and the stripped
		information is lost.  After performing a strip operation, the object is
		considered to have its entries in a "random" order, as it was just after object
		initialization and loading.  If :meth:`strip_dirs` causes two function names to
		be indistinguishable (they are on the same line of the same filename, and have
		the same function name), then the statistics for these two entries are
		accumulated into a single entry.
		
		
		"""
		pass
		
	def add(self, filename,more):
		"""
		This method of the :class:`Stats` class accumulates additional profiling
		information into the current profiling object.  Its arguments should refer to
		filenames created by the corresponding version of :func:`profile.run` or
		:func:`cProfile.run`. Statistics for identically named (re: file, line, name)
		functions are automatically accumulated into single function statistics.
		
		
		"""
		pass
		
	def dump_stats(self, filename):
		"""
		Save the data loaded into the :class:`Stats` object to a file named *filename*.
		The file is created if it does not exist, and is overwritten if it already
		exists.  This is equivalent to the method of the same name on the
		:class:`profile.Profile` and :class:`cProfile.Profile` classes.
		
		"""
		pass
		
	def sort_stats(self, key,more):
		"""
		This method modifies the :class:`Stats` object by sorting it according to the
		supplied criteria.  The argument is typically a string identifying the basis of
		a sort (example: ``'time'`` or ``'name'``).
		
		When more than one key is provided, then additional keys are used as secondary
		criteria when there is equality in all keys selected before them.  For example,
		``sort_stats('name', 'file')`` will sort all the entries according to their
		function name, and resolve all ties (identical function names) by sorting by
		file name.
		
		Abbreviations can be used for any key names, as long as the abbreviation is
		unambiguous.  The following are the keys currently defined:
		
		+------------------+----------------------+
		| Valid Arg        | Meaning              |
		+==================+======================+
		| ``'calls'``      | call count           |
		+------------------+----------------------+
		| ``'cumulative'`` | cumulative time      |
		+------------------+----------------------+
		| ``'file'``       | file name            |
		+------------------+----------------------+
		| ``'module'``     | file name            |
		+------------------+----------------------+
		| ``'pcalls'``     | primitive call count |
		+------------------+----------------------+
		| ``'line'``       | line number          |
		+------------------+----------------------+
		| ``'name'``       | function name        |
		+------------------+----------------------+
		| ``'nfl'``        | name/file/line       |
		+------------------+----------------------+
		| ``'stdname'``    | standard name        |
		+------------------+----------------------+
		| ``'time'``       | internal time        |
		+------------------+----------------------+
		
		Note that all sorts on statistics are in descending order (placing most time
		consuming items first), where as name, file, and line number searches are in
		ascending order (alphabetical). The subtle distinction between ``'nfl'`` and
		``'stdname'`` is that the standard name is a sort of the name as printed, which
		means that the embedded line numbers get compared in an odd way.  For example,
		lines 3, 20, and 40 would (if the file names were the same) appear in the string
		order 20, 3 and 40.  In contrast, ``'nfl'`` does a numeric compare of the line
		numbers.  In fact, ``sort_stats('nfl')`` is the same as ``sort_stats('name',
		'file', 'line')``.
		
		For backward-compatibility reasons, the numeric arguments ``-1``, ``0``, ``1``,
		and ``2`` are permitted.  They are interpreted as ``'stdname'``, ``'calls'``,
		``'time'``, and ``'cumulative'`` respectively.  If this old style format
		(numeric) is used, only one sort key (the numeric key) will be used, and
		additional arguments will be silently ignored.
		
		.. ith the old profiler,
		
		
		"""
		pass
		
	def reverse_order(self, ):
		"""
		This method for the :class:`Stats` class reverses the ordering of the basic list
		within the object.  Note that by default ascending vs descending order is
		properly selected based on the sort key of choice.
		
		.. s provided primarily for compatibility with the old profiler.
		
		
		"""
		pass
		
	def print_stats(self, restriction,more):
		"""
		This method for the :class:`Stats` class prints out a report as described in the
		:func:`profile.run` definition.
		
		The order of the printing is based on the last :meth:`sort_stats` operation done
		on the object (subject to caveats in :meth:`add` and :meth:`strip_dirs`).
		
		The arguments provided (if any) can be used to limit the list down to the
		significant entries.  Initially, the list is taken to be the complete set of
		profiled functions.  Each restriction is either an integer (to select a count of
		lines), or a decimal fraction between 0.0 and 1.0 inclusive (to select a
		percentage of lines), or a regular expression (to pattern match the standard
		name that is printed; as of Python 1.5b1, this uses the Perl-style regular
		expression syntax defined by the :mod:`re` module).  If several restrictions are
		provided, then they are applied sequentially.  For example::
		
		print_stats(.1, 'foo:')
		
		would first limit the printing to first 10% of list, and then only print
		functions that were part of filename :file:`.\*foo:`.  In contrast, the
		command::
		
		print_stats('foo:', .1)
		
		would limit the list to all functions having file names :file:`.\*foo:`, and
		then proceed to only print the first 10% of them.
		
		
		"""
		pass
		
	def print_callers(self, restriction,more):
		"""
		This method for the :class:`Stats` class prints a list of all functions that
		called each function in the profiled database.  The ordering is identical to
		that provided by :meth:`print_stats`, and the definition of the restricting
		argument is also identical.  Each caller is reported on its own line.  The
		format differs slightly depending on the profiler that produced the stats:
		
		* With :mod:`profile`, a number is shown in parentheses after each caller to
		show how many times this specific call was made.  For convenience, a second
		non-parenthesized number repeats the cumulative time spent in the function
		at the right.
		
		* With :mod:`cProfile`, each caller is preceded by three numbers: the number of
		times this specific call was made, and the total and cumulative times spent in
		the current function while it was invoked by this specific caller.
		
		
		"""
		pass
		
	def print_callees(self, restriction,more):
		"""
		This method for the :class:`Stats` class prints a list of all function that were
		called by the indicated function.  Aside from this reversal of direction of
		calls (re: called vs was called by), the arguments and ordering are identical to
		the :meth:`print_callers` method.
		
		
		.. imitations
		===========
		
		One limitation has to do with accuracy of timing information. There is a
		fundamental problem with deterministic profilers involving accuracy.  The most
		obvious restriction is that the underlying "clock" is only ticking at a rate
		(typically) of about .001 seconds.  Hence no measurements will be more accurate
		than the underlying clock.  If enough measurements are taken, then the "error"
		will tend to average out. Unfortunately, removing this first error induces a
		second source of error.
		
		The second problem is that it "takes a while" from when an event is dispatched
		until the profiler's call to get the time actually *gets* the state of the
		clock.  Similarly, there is a certain lag when exiting the profiler event
		handler from the time that the clock's value was obtained (and then squirreled
		away), until the user's code is once again executing.  As a result, functions
		that are called many times, or call many functions, will typically accumulate
		this error. The error that accumulates in this fashion is typically less than
		the accuracy of the clock (less than one clock tick), but it *can* accumulate
		and become very significant.
		
		The problem is more important with :mod:`profile` than with the lower-overhead
		:mod:`cProfile`.  For this reason, :mod:`profile` provides a means of
		calibrating itself for a given platform so that this error can be
		probabilistically (on the average) removed. After the profiler is calibrated, it
		will be more accurate (in a least square sense), but it will sometimes produce
		negative numbers (when call counts are exceptionally low, and the gods of
		probability work against you :-). )  Do *not* be alarmed by negative numbers in
		the profile.  They should *only* appear if you have calibrated your profiler,
		and the results are actually better than without calibration.
		
		
		.. alibration
		===========
		
		The profiler of the :mod:`profile` module subtracts a constant from each event
		handling time to compensate for the overhead of calling the time function, and
		socking away the results.  By default, the constant is 0. The following
		procedure can be used to obtain a better constant for a given platform (see
		discussion in section Limitations above). ::
		
		import profile
		pr = profile.Profile()
		for i in range(5):
		print pr.calibrate(10000)
		
		The method executes the number of Python calls given by the argument, directly
		and again under the profiler, measuring the time for both. It then computes the
		hidden overhead per profiler event, and returns that as a float.  For example,
		on an 800 MHz Pentium running Windows 2000, and using Python's time.clock() as
		the timer, the magical number is about 12.5e-6.
		
		The object of this exercise is to get a fairly consistent result. If your
		computer is *very* fast, or your timer function has poor resolution, you might
		have to pass 100000, or even 1000000, to get consistent results.
		
		When you have a consistent answer, there are three ways you can use it: [#]_ ::
		
		import profile
		
		# 1. Apply computed bias to all Profile instances created hereafter.
		profile.Profile.bias = your_computed_bias
		
		# 2. Apply computed bias to a specific Profile instance.
		pr = profile.Profile()
		pr.bias = your_computed_bias
		
		# 3. Specify computed bias in instance constructor.
		pr = profile.Profile(bias=your_computed_bias)
		
		If you have a choice, you are better off choosing a smaller constant, and then
		your results will "less often" show up as negative in profile statistics.
		
		
		.. xtensions --- Deriving Better Profilers
		========================================
		
		The :class:`Profile` class of both modules, :mod:`profile` and :mod:`cProfile`,
		were written so that derived classes could be developed to extend the profiler.
		The details are not described here, as doing this successfully requires an
		expert understanding of how the :class:`Profile` class works internally.  Study
		the source code of the module carefully if you want to pursue this.
		
		If all you want to do is change how current time is determined (for example, to
		force use of wall-clock time or elapsed process time), pass the timing function
		you want to the :class:`Profile` class constructor::
		
		pr = profile.Profile(your_time_func)
		
		The resulting profiler will then call :func:`your_time_func`.
		
		:class:`profile.Profile`
		:func:`your_time_func` should return a single number, or a list of numbers whose
		sum is the current time (like what :func:`os.times` returns).  If the function
		returns a single time number, or the list of returned numbers has length 2, then
		you will get an especially fast version of the dispatch routine.
		
		Be warned that you should calibrate the profiler class for the timer function
		that you choose.  For most machines, a timer that returns a lone integer value
		will provide the best results in terms of low overhead during profiling.
		(:func:`os.times` is *pretty* bad, as it returns a tuple of floating point
		values).  If you want to substitute a better timer in the cleanest fashion,
		derive a class and hardwire a replacement dispatch method that best handles your
		timer call, along with the appropriate calibration constant.
		
		:class:`cProfile.Profile`
		:func:`your_time_func` should return a single number.  If it returns plain
		integers, you can also invoke the class constructor with a second argument
		specifying the real duration of one unit of time.  For example, if
		:func:`your_integer_time_func` returns times measured in thousands of seconds,
		you would construct the :class:`Profile` instance as follows::
		
		pr = profile.Profile(your_integer_time_func, 0.001)
		
		As the :mod:`cProfile.Profile` class cannot be calibrated, custom timer
		functions should be used with care and should be as fast as possible.  For the
		best results with a custom timer, it might be necessary to hard-code it in the C
		source of the internal :mod:`_lsprof` module.
		
		"""
		pass
		
	


