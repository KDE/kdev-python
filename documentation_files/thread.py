#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
""":synopsis: Create multiple threads of control within one interpreter.

"""
"""
This is the type of lock objects.


"""
LockType = None
def start_new_thread(function,args,kwargs):
	"""
	Start a new thread and return its identifier.  The thread executes the function
	*function* with the argument list *args* (which must be a tuple).  The optional
	*kwargs* argument specifies a dictionary of keyword arguments. When the function
	returns, the thread silently exits.  When the function terminates with an
	unhandled exception, a stack trace is printed and then the thread exits (but
	other threads continue to run).
	
	
	"""
	pass
	
def interrupt_main():
	"""
	Raise a :exc:`KeyboardInterrupt` exception in the main thread.  A subthread can
	use this function to interrupt the main thread.
	
	"""
	pass
	
def exit():
	"""
	Raise the :exc:`SystemExit` exception.  When not caught, this will cause the
	thread to exit silently.
	
	..
	function:: exit_prog(status)
	
	Exit all threads and report the value of the integer argument
	*status* as the exit status of the entire program.
	**Caveat:** code in pending :keyword:`finally` clauses, in this thread
	or in other threads, is not executed.
	
	
	"""
	pass
	
def allocate_lock():
	"""
	Return a new lock object.  Methods of locks are described below.  The lock is
	initially unlocked.
	
	
	"""
	pass
	
def get_ident():
	"""
	Return the 'thread identifier' of the current thread.  This is a nonzero
	integer.  Its value has no direct meaning; it is intended as a magic cookie to
	be used e.g. to index a dictionary of thread-specific data.  Thread identifiers
	may be recycled when a thread exits and another thread is created.
	
	
	"""
	pass
	
def stack_size(size):
	"""
	Return the thread stack size used when creating new threads.  The optional
	*size* argument specifies the stack size to be used for subsequently created
	threads, and must be 0 (use platform or configured default) or a positive
	integer value of at least 32,768 (32kB). If changing the thread stack size is
	unsupported, the :exc:`error` exception is raised.  If the specified stack size is
	invalid, a :exc:`ValueError` is raised and the stack size is unmodified.  32kB
	is currently the minimum supported stack size value to guarantee sufficient
	stack space for the interpreter itself.  Note that some platforms may have
	particular restrictions on values for the stack size, such as requiring a
	minimum stack size > 32kB or requiring allocation in multiples of the system
	memory page size - platform documentation should be referred to for more
	information (4kB pages are common; using multiples of 4096 for the stack size is
	the suggested approach in the absence of more specific information).
	Availability: Windows, systems with POSIX threads.
	
	"""
	pass
	
