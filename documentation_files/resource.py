#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
""":platform: Unix
:synopsis: An interface to provide resource usage information on the current process.
"""
"""
The maximum size (in bytes) of a core file that the current process can create.
This may result in the creation of a partial core file if a larger core would be
required to contain the entire process image.


"""
RLIMIT_CORE = None
"""
The maximum amount of processor time (in seconds) that a process can use. If
this limit is exceeded, a :const:`SIGXCPU` signal is sent to the process. (See
the :mod:`signal` module documentation for information about how to catch this
signal and do something useful, e.g. flush open files to disk.)


"""
RLIMIT_CPU = None
"""
The maximum size of a file which the process may create.  This only affects the
stack of the main thread in a multi-threaded process.


"""
RLIMIT_FSIZE = None
"""
The maximum size (in bytes) of the process's heap.


"""
RLIMIT_DATA = None
"""
The maximum size (in bytes) of the call stack for the current process.


"""
RLIMIT_STACK = None
"""
The maximum resident set size that should be made available to the process.


"""
RLIMIT_RSS = None
"""
The maximum number of processes the current process may create.


"""
RLIMIT_NPROC = None
"""
The maximum number of open file descriptors for the current process.


"""
RLIMIT_NOFILE = None
"""
The BSD name for :const:`RLIMIT_NOFILE`.


"""
RLIMIT_OFILE = None
"""
The maximum address space which may be locked in memory.


"""
RLIMIT_MEMLOCK = None
"""
The largest area of mapped memory which the process may occupy.


"""
RLIMIT_VMEM = None
"""
The maximum area (in bytes) of address space which may be taken by the process.


Resource Usage
--------------

These functions are used to retrieve resource usage information:


"""
RLIMIT_AS = None
"""
:const:`RUSAGE_SELF` should be used to request information pertaining only to
the process itself.


"""
RUSAGE_SELF = None
"""
Pass to :func:`getrusage` to request resource information for child processes of
the calling process.


"""
RUSAGE_CHILDREN = None
def getrlimit(resource):
	"""
	Returns a tuple ``(soft, hard)`` with the current soft and hard limits of
	*resource*. Raises :exc:`ValueError` if an invalid resource is specified, or
	:exc:`error` if the underlying system call fails unexpectedly.
	
	
	"""
	pass
	
def setrlimit(resource,limits):
	"""
	Sets new limits of consumption of *resource*. The *limits* argument must be a
	tuple ``(soft, hard)`` of two integers describing the new limits. A value of
	``-1`` can be used to specify the maximum possible upper limit.
	
	Raises :exc:`ValueError` if an invalid resource is specified, if the new soft
	limit exceeds the hard limit, or if a process tries to raise its hard limit
	(unless the process has an effective UID of super-user).  Can also raise
	:exc:`error` if the underlying system call fails.
	
	These symbols define resources whose consumption can be controlled using the
	:func:`setrlimit` and :func:`getrlimit` functions described below. The values of
	these symbols are exactly the constants used by C programs.
	
	The Unix man page for :manpage:`getrlimit(2)` lists the available resources.
	Note that not all systems use the same symbol or same value to denote the same
	resource.  This module does not attempt to mask platform differences --- symbols
	not defined for a platform will not be available from this module on that
	platform.
	
	
	"""
	pass
	
def getrusage(who):
	"""
	This function returns an object that describes the resources consumed by either
	the current process or its children, as specified by the *who* parameter.  The
	*who* parameter should be specified using one of the :const:`RUSAGE_\*`
	constants described below.
	
	The fields of the return value each describe how a particular system resource
	has been used, e.g. amount of time spent running is user mode or number of times
	the process was swapped out of main memory. Some values are dependent on the
	clock tick internal, e.g. the amount of memory the process is using.
	
	For backward compatibility, the return value is also accessible as a tuple of 16
	elements.
	
	The fields :attr:`ru_utime` and :attr:`ru_stime` of the return value are
	floating point values representing the amount of time spent executing in user
	mode and the amount of time spent executing in system mode, respectively. The
	remaining values are integers. Consult the :manpage:`getrusage(2)` man page for
	detailed information about these values. A brief summary is presented here:
	
	+--------+---------------------+-------------------------------+
	| Index  | Field               | Resource                      |
	+========+=====================+===============================+
	| ``0``  | :attr:`ru_utime`    | time in user mode (float)     |
	+--------+---------------------+-------------------------------+
	| ``1``  | :attr:`ru_stime`    | time in system mode (float)   |
	+--------+---------------------+-------------------------------+
	| ``2``  | :attr:`ru_maxrss`   | maximum resident set size     |
	+--------+---------------------+-------------------------------+
	| ``3``  | :attr:`ru_ixrss`    | shared memory size            |
	+--------+---------------------+-------------------------------+
	| ``4``  | :attr:`ru_idrss`    | unshared memory size          |
	+--------+---------------------+-------------------------------+
	| ``5``  | :attr:`ru_isrss`    | unshared stack size           |
	+--------+---------------------+-------------------------------+
	| ``6``  | :attr:`ru_minflt`   | page faults not requiring I/O |
	+--------+---------------------+-------------------------------+
	| ``7``  | :attr:`ru_majflt`   | page faults requiring I/O     |
	+--------+---------------------+-------------------------------+
	| ``8``  | :attr:`ru_nswap`    | number of swap outs           |
	+--------+---------------------+-------------------------------+
	| ``9``  | :attr:`ru_inblock`  | block input operations        |
	+--------+---------------------+-------------------------------+
	| ``10`` | :attr:`ru_oublock`  | block output operations       |
	+--------+---------------------+-------------------------------+
	| ``11`` | :attr:`ru_msgsnd`   | messages sent                 |
	+--------+---------------------+-------------------------------+
	| ``12`` | :attr:`ru_msgrcv`   | messages received             |
	+--------+---------------------+-------------------------------+
	| ``13`` | :attr:`ru_nsignals` | signals received              |
	+--------+---------------------+-------------------------------+
	| ``14`` | :attr:`ru_nvcsw`    | voluntary context switches    |
	+--------+---------------------+-------------------------------+
	| ``15`` | :attr:`ru_nivcsw`   | involuntary context switches  |
	+--------+---------------------+-------------------------------+
	
	This function will raise a :exc:`ValueError` if an invalid *who* parameter is
	specified. It may also raise :exc:`error` exception in unusual circumstances.
	
	"""
	pass
	
def getpagesize():
	"""
	Returns the number of bytes in a system page. (This need not be the same as the
	hardware page size.) This function is useful for determining the number of bytes
	of memory a process is using. The third element of the tuple returned by
	:func:`getrusage` describes memory usage in pages; multiplying by page size
	produces number of bytes.
	
	The following :const:`RUSAGE_\*` symbols are passed to the :func:`getrusage`
	function to specify which processes information should be provided for.
	
	
	"""
	pass
	
