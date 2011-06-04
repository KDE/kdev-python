#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
""":synopsis: Debugger framework.

The :mod:`bdb` module handles basic debugger functions, like setting breakpoints
or managing execution via the debugger.

The following exception is defined:

"""
class Breakpoint:


	"""
	This class implements temporary breakpoints, ignore counts, disabling and
	(re-)enabling, and conditionals.
	
	Breakpoints are indexed by number through a list called :attr:`bpbynumber`
	and by ``(file, line)`` pairs through :attr:`bplist`.  The former points to a
	single instance of class :class:`Breakpoint`.  The latter points to a list of
	such instances since there may be more than one breakpoint per line.
	
	When creating a breakpoint, its associated filename should be in canonical
	form.  If a *funcname* is defined, a breakpoint hit will be counted when the
	first line of that function is executed.  A conditional breakpoint always
	counts a hit.
	
	:class:`Breakpoint` instances have the following methods:
	
	"""
	
	
	def __init__(self, ):
		pass
	
	def deleteMe(self, ):
		"""
		Delete the breakpoint from the list associated to a file/line.  If it is
		the last breakpoint in that position, it also deletes the entry for the
		file/line.
		
		
		"""
		pass
		
	def enable(self, ):
		"""
		Mark the breakpoint as enabled.
		
		
		"""
		pass
		
	def disable(self, ):
		"""
		Mark the breakpoint as disabled.
		
		
		"""
		pass
		
	def pprint(self, out):
		"""
		Print all the information about the breakpoint:
		
		* The breakpoint number.
		* If it is temporary or not.
		* Its file,line position.
		* The condition that causes a break.
		* If it must be ignored the next N times.
		* The breakpoint hit count.
		
		
		"""
		pass
		
	


class Bdb:


	"""
	The :class:`Bdb` class acts as a generic Python debugger base class.
	
	This class takes care of the details of the trace facility; a derived class
	should implement user interaction.  The standard debugger class
	(:class:`pdb.Pdb`) is an example.
	
	The *skip* argument, if given, must be an iterable of glob-style
	module name patterns.  The debugger will not step into frames that
	originate in a module that matches one of these patterns. Whether a
	frame is considered to originate in a certain module is determined
	by the ``__name__`` in the frame globals.
	
	"""
	
	
	def __init__(self, ):
		pass
	
	def canonic(self, filename):
		"""
		Auxiliary method for getting a filename in a canonical form, that is, as a
		case-normalized (on case-insensitive filesystems) absolute path, stripped
		of surrounding angle brackets.
		
		"""
		pass
		
	def reset(self, ):
		"""
		Set the :attr:`botframe`, :attr:`stopframe`, :attr:`returnframe` and
		:attr:`quitting` attributes with values ready to start debugging.
		
		"""
		pass
		
	def trace_dispatch(self, frame,event,arg):
		"""
		This function is installed as the trace function of debugged frames.  Its
		return value is the new trace function (in most cases, that is, itself).
		
		The default implementation decides how to dispatch a frame, depending on
		the type of event (passed as a string) that is about to be executed.
		*event* can be one of the following:
		
		* ``"line"``: A new line of code is going to be executed.
		* ``"call"``: A function is about to be called, or another code block
		entered.
		* ``"return"``: A function or other code block is about to return.
		* ``"exception"``: An exception has occurred.
		* ``"c_call"``: A C function is about to be called.
		* ``"c_return"``: A C function has returned.
		* ``"c_exception"``: A C function has raised an exception.
		
		For the Python events, specialized functions (see below) are called.  For
		the C events, no action is taken.
		
		The *arg* parameter depends on the previous event.
		
		See the documentation for :func:`sys.settrace` for more information on the
		trace function.  For more information on code and frame objects, refer to
		:ref:`types`.
		
		"""
		pass
		
	def dispatch_line(self, frame):
		"""
		If the debugger should stop on the current line, invoke the
		:meth:`user_line` method (which should be overridden in subclasses).
		Raise a :exc:`BdbQuit` exception if the :attr:`Bdb.quitting` flag is set
		(which can be set from :meth:`user_line`).  Return a reference to the
		:meth:`trace_dispatch` method for further tracing in that scope.
		
		"""
		pass
		
	def dispatch_call(self, frame,arg):
		"""
		If the debugger should stop on this function call, invoke the
		:meth:`user_call` method (which should be overridden in subclasses).
		Raise a :exc:`BdbQuit` exception if the :attr:`Bdb.quitting` flag is set
		(which can be set from :meth:`user_call`).  Return a reference to the
		:meth:`trace_dispatch` method for further tracing in that scope.
		
		"""
		pass
		
	def dispatch_return(self, frame,arg):
		"""
		If the debugger should stop on this function return, invoke the
		:meth:`user_return` method (which should be overridden in subclasses).
		Raise a :exc:`BdbQuit` exception if the :attr:`Bdb.quitting` flag is set
		(which can be set from :meth:`user_return`).  Return a reference to the
		:meth:`trace_dispatch` method for further tracing in that scope.
		
		"""
		pass
		
	def dispatch_exception(self, frame,arg):
		"""
		If the debugger should stop at this exception, invokes the
		:meth:`user_exception` method (which should be overridden in subclasses).
		Raise a :exc:`BdbQuit` exception if the :attr:`Bdb.quitting` flag is set
		(which can be set from :meth:`user_exception`).  Return a reference to the
		:meth:`trace_dispatch` method for further tracing in that scope.
		
		Normally derived classes don't override the following methods, but they may
		if they want to redefine the definition of stopping and breakpoints.
		
		"""
		pass
		
	def stop_here(self, frame):
		"""
		This method checks if the *frame* is somewhere below :attr:`botframe` in
		the call stack.  :attr:`botframe` is the frame in which debugging started.
		
		"""
		pass
		
	def break_here(self, frame):
		"""
		This method checks if there is a breakpoint in the filename and line
		belonging to *frame* or, at least, in the current function.  If the
		breakpoint is a temporary one, this method deletes it.
		
		"""
		pass
		
	def break_anywhere(self, frame):
		"""
		This method checks if there is a breakpoint in the filename of the current
		frame.
		
		Derived classes should override these methods to gain control over debugger
		operation.
		
		"""
		pass
		
	def user_call(self, frame,argument_list):
		"""
		This method is called from :meth:`dispatch_call` when there is the
		possibility that a break might be necessary anywhere inside the called
		function.
		
		"""
		pass
		
	def user_line(self, frame):
		"""
		This method is called from :meth:`dispatch_line` when either
		:meth:`stop_here` or :meth:`break_here` yields True.
		
		"""
		pass
		
	def user_return(self, frame,return_value):
		"""
		This method is called from :meth:`dispatch_return` when :meth:`stop_here`
		yields True.
		
		"""
		pass
		
	def user_exception(self, frame,exc_info):
		"""
		This method is called from :meth:`dispatch_exception` when
		:meth:`stop_here` yields True.
		
		"""
		pass
		
	def do_clear(self, arg):
		"""
		Handle how a breakpoint must be removed when it is a temporary one.
		
		This method must be implemented by derived classes.
		
		
		Derived classes and clients can call the following methods to affect the
		stepping state.
		
		"""
		pass
		
	def set_step(self, ):
		"""
		Stop after one line of code.
		
		"""
		pass
		
	def set_next(self, frame):
		"""
		Stop on the next line in or below the given frame.
		
		"""
		pass
		
	def set_return(self, frame):
		"""
		Stop when returning from the given frame.
		
		"""
		pass
		
	def set_until(self, frame):
		"""
		Stop when the line with the line no greater than the current one is
		reached or when returning from current frame
		
		"""
		pass
		
	def set_trace(self, frame):
		"""
		Start debugging from *frame*.  If *frame* is not specified, debugging
		starts from caller's frame.
		
		"""
		pass
		
	def set_continue(self, ):
		"""
		Stop only at breakpoints or when finished.  If there are no breakpoints,
		set the system trace function to None.
		
		"""
		pass
		
	def set_quit(self, ):
		"""
		Set the :attr:`quitting` attribute to True.  This raises :exc:`BdbQuit` in
		the next call to one of the :meth:`dispatch_\*` methods.
		
		
		Derived classes and clients can call the following methods to manipulate
		breakpoints.  These methods return a string containing an error message if
		something went wrong, or ``None`` if all is well.
		
		"""
		pass
		
	def set_break(self, filename,lineno,temporary=0,cond,funcname):
		"""
		Set a new breakpoint.  If the *lineno* line doesn't exist for the
		*filename* passed as argument, return an error message.  The *filename*
		should be in canonical form, as described in the :meth:`canonic` method.
		
		"""
		pass
		
	def clear_break(self, filename,lineno):
		"""
		Delete the breakpoints in *filename* and *lineno*.  If none were set, an
		error message is returned.
		
		"""
		pass
		
	def clear_bpbynumber(self, arg):
		"""
		Delete the breakpoint which has the index *arg* in the
		:attr:`Breakpoint.bpbynumber`.  If *arg* is not numeric or out of range,
		return an error message.
		
		"""
		pass
		
	def clear_all_file_breaks(self, filename):
		"""
		Delete all breakpoints in *filename*.  If none were set, an error message
		is returned.
		
		"""
		pass
		
	def clear_all_breaks(self, ):
		"""
		Delete all existing breakpoints.
		
		"""
		pass
		
	def get_break(self, filename,lineno):
		"""
		Check if there is a breakpoint for *lineno* of *filename*.
		
		"""
		pass
		
	def get_breaks(self, filename,lineno):
		"""
		Return all breakpoints for *lineno* in *filename*, or an empty list if
		none are set.
		
		"""
		pass
		
	def get_file_breaks(self, filename):
		"""
		Return all breakpoints in *filename*, or an empty list if none are set.
		
		"""
		pass
		
	def get_all_breaks(self, ):
		"""
		Return all breakpoints that are set.
		
		
		Derived classes and clients can call the following methods to get a data
		structure representing a stack trace.
		
		"""
		pass
		
	def get_stack(self, f,t):
		"""
		Get a list of records for a frame and all higher (calling) and lower
		frames, and the size of the higher part.
		
		"""
		pass
		
	def format_stack_entry(self, frame_lineno,lprefix=':'):
		"""
		Return a string with information about a stack entry, identified by a
		``(frame, lineno)`` tuple:
		
		* The canonical form of the filename which contains the frame.
		* The function name, or ``"<lambda>"``.
		* The input arguments.
		* The return value.
		* The line of code (if it exists).
		
		
		The following two methods can be called by clients to use a debugger to debug
		a :term:`statement`, given as a string.
		
		"""
		pass
		
	def run(self, cmd,globals,locals):
		"""
		Debug a statement executed via the :keyword:`exec` statement.  *globals*
		defaults to :attr:`__main__.__dict__`, *locals* defaults to *globals*.
		
		"""
		pass
		
	def runeval(self, expr,globals,locals):
		"""
		Debug an expression executed via the :func:`eval` function.  *globals* and
		*locals* have the same meaning as in :meth:`run`.
		
		"""
		pass
		
	def runctx(self, cmd,globals,locals):
		"""
		For backwards compatibility.  Calls the :meth:`run` method.
		
		"""
		pass
		
	def runcall(self, func,args,kwds):
		"""
		Debug a single function call, and return its result.
		
		
		Finally, the module defines the following functions:
		"""
		pass
		
	def checkfuncname(self, b,frame):
		"""
		Check whether we should break here, depending on the way the breakpoint *b*
		was set.
		
		If it was set via line number, it checks if ``b.line`` is the same as the one
		in the frame also passed as argument.  If the breakpoint was set via function
		name, we have to check we are in the right frame (the right function) and if
		we are in its first executable line.
		
		"""
		pass
		
	def effective(self, file,line,frame):
		"""
		Determine if there is an effective (active) breakpoint at this line of code.
		Return a tuple of the breakpoint and a boolean that indicates if it is ok
		to delete a temporary breakpoint.  Return ``(None, None)`` if there is no
		matching breakpoint.
		
		"""
		pass
		
	


