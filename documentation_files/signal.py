#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
""":synopsis: Set handlers for asynchronous events.


This module provides mechanisms to use signal handlers in Python. Some general
rules for working with signals and their handlers:

* A handler for a particular signal, once set, remains installed until it is
explicitly reset (Python emulates the BSD style interface regardless of the
underlying implementation), with the exception of the handler for
:const:`SIGCHLD`, which follows the underlying implementation.

* There is no way to "block" signals temporarily from critical sections (since
this is not supported by all Unix flavors).

* Although Python signal handlers are called asynchronously as far as the Python
user is concerned, they can only occur between the "atomic" instructions of the
Python interpreter.  This means that signals arriving during long calculations
implemented purely in C (such as regular expression matches on large bodies of
text) may be delayed for an arbitrary amount of time.

* When a signal arrives during an I/O operation, it is possible that the I/O
operation raises an exception after the signal handler returns. This is
dependent on the underlying Unix system's semantics regarding interrupted system
calls.

* Because the C signal handler always returns, it makes little sense to catch
synchronous errors like :const:`SIGFPE` or :const:`SIGSEGV`.

* Python installs a small number of signal handlers by default: :const:`SIGPIPE`
is ignored (so write errors on pipes and sockets can be reported as ordinary
Python exceptions) and :const:`SIGINT` is translated into a
:exc:`KeyboardInterrupt` exception.  All of these can be overridden.

* Some care must be taken if both signals and threads are used in the same
program.  The fundamental thing to remember in using signals and threads
simultaneously is: always perform :func:`signal` operations in the main thread
of execution.  Any thread can perform an :func:`alarm`, :func:`getsignal`,
:func:`pause`, :func:`setitimer` or :func:`getitimer`; only the main thread
can set a new signal handler, and the main thread will be the only one to
receive signals (this is enforced by the Python :mod:`signal` module, even
if the underlying thread implementation supports sending signals to
individual threads).  This means that signals can't be used as a means of
inter-thread communication.  Use locks instead.

The variables defined in the :mod:`signal` module are:


"""
"""
This is one of two standard signal handling options; it will simply perform
the default function for the signal.  For example, on most systems the
default action for :const:`SIGQUIT` is to dump core and exit, while the
default action for :const:`SIGCHLD` is to simply ignore it.


"""
SIG_DFL = None
"""
This is another standard signal handler, which will simply ignore the given
signal.


"""
SIG_IGN = None
"""
All the signal numbers are defined symbolically.  For example, the hangup signal
is defined as :const:`signal.SIGHUP`; the variable names are identical to the
names used in C programs, as found in ``<signal.h>``. The Unix man page for
':cfunc:`signal`' lists the existing signals (on some systems this is
:manpage:`signal(2)`, on others the list is in :manpage:`signal(7)`). Note that
not all systems define the same set of signal names; only those names defined by
the system are defined by this module.


"""
SIG = None
"""
The signal corresponding to the CTRL+C keystroke event. This signal can
only be used with :func:`os.kill`.

Availability: Windows.

"""
CTRL_C_EVENT = None
"""
The signal corresponding to the CTRL+BREAK keystroke event. This signal can
only be used with :func:`os.kill`.

Availability: Windows.

"""
CTRL_BREAK_EVENT = None
"""
One more than the number of the highest signal number.


"""
NSIG = None
"""
Decrements interval timer in real time, and delivers :const:`SIGALRM` upon expiration.


"""
ITIMER_REAL = None
"""
Decrements interval timer only when the process is executing, and delivers
SIGVTALRM upon expiration.


"""
ITIMER_VIRTUAL = None
"""
Decrements interval timer both when the process executes and when the
system is executing on behalf of the process. Coupled with ITIMER_VIRTUAL,
this timer is usually used to profile the time spent by the application
in user and kernel space. SIGPROF is delivered upon expiration.


The :mod:`signal` module defines one exception:

"""
ITIMER_PROF = None
def alarm(time):
	"""
	If *time* is non-zero, this function requests that a :const:`SIGALRM` signal be
	sent to the process in *time* seconds. Any previously scheduled alarm is
	canceled (only one alarm can be scheduled at any time).  The returned value is
	then the number of seconds before any previously set alarm was to have been
	delivered. If *time* is zero, no alarm is scheduled, and any scheduled alarm is
	canceled.  If the return value is zero, no alarm is currently scheduled.  (See
	the Unix man page :manpage:`alarm(2)`.) Availability: Unix.
	
	
	"""
	pass
	
def getsignal(signalnum):
	"""
	Return the current signal handler for the signal *signalnum*. The returned value
	may be a callable Python object, or one of the special values
	:const:`signal.SIG_IGN`, :const:`signal.SIG_DFL` or :const:`None`.  Here,
	:const:`signal.SIG_IGN` means that the signal was previously ignored,
	:const:`signal.SIG_DFL` means that the default way of handling the signal was
	previously in use, and ``None`` means that the previous signal handler was not
	installed from Python.
	
	
	"""
	pass
	
def pause():
	"""
	Cause the process to sleep until a signal is received; the appropriate handler
	will then be called.  Returns nothing.  Not on Windows. (See the Unix man page
	:manpage:`signal(2)`.)
	
	
	"""
	pass
	
def setitimer(which,seconds,interval):
	"""
	Sets given interval timer (one of :const:`signal.ITIMER_REAL`,
	:const:`signal.ITIMER_VIRTUAL` or :const:`signal.ITIMER_PROF`) specified
	by *which* to fire after *seconds* (float is accepted, different from
	:func:`alarm`) and after that every *interval* seconds. The interval
	timer specified by *which* can be cleared by setting seconds to zero.
	
	When an interval timer fires, a signal is sent to the process.
	The signal sent is dependent on the timer being used;
	:const:`signal.ITIMER_REAL` will deliver :const:`SIGALRM`,
	:const:`signal.ITIMER_VIRTUAL` sends :const:`SIGVTALRM`,
	and :const:`signal.ITIMER_PROF` will deliver :const:`SIGPROF`.
	
	The old values are returned as a tuple: (delay, interval).
	
	Attempting to pass an invalid interval timer will cause an
	:exc:`ItimerError`.  Availability: Unix.
	
	"""
	pass
	
def getitimer(which):
	"""
	Returns current value of a given interval timer specified by *which*.
	Availability: Unix.
	
	"""
	pass
	
def set_wakeup_fd(fd):
	"""
	Set the wakeup fd to *fd*.  When a signal is received, a ``'\0'`` byte is
	written to the fd.  This can be used by a library to wakeup a poll or select
	call, allowing the signal to be fully processed.
	
	The old wakeup fd is returned.  *fd* must be non-blocking.  It is up to the
	library to remove any bytes before calling poll or select again.
	
	When threads are enabled, this function can only be called from the main thread;
	attempting to call it from other threads will cause a :exc:`ValueError`
	exception to be raised.
	
	"""
	pass
	
def siginterrupt(signalnum,flag):
	"""
	Change system call restart behaviour: if *flag* is :const:`False`, system
	calls will be restarted when interrupted by signal *signalnum*, otherwise
	system calls will be interrupted.  Returns nothing.  Availability: Unix (see
	the man page :manpage:`siginterrupt(3)` for further information).
	
	Note that installing a signal handler with :func:`signal` will reset the
	restart behaviour to interruptible by implicitly calling
	:cfunc:`siginterrupt` with a true *flag* value for the given signal.
	
	"""
	pass
	
