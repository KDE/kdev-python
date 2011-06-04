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
	
	
	def __init__(self, file,line,temporary=0,cond=None,funcname=None):
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
	
	
	def __init__(self, skip=None):
		pass
	
	def checkfuncname(b,frame):
		"""
		Check whether we should break here, depending on the way the breakpoint *b*
		was set.
		
		If it was set via line number, it checks if ``b.line`` is the same as the one
		in the frame also passed as argument.  If the breakpoint was set via function
		name, we have to check we are in the right frame (the right function) and if
		we are in its first executable line.
		
		"""
		pass
		
	def effective(file,line,frame):
		"""
		Determine if there is an effective (active) breakpoint at this line of code.
		Return a tuple of the breakpoint and a boolean that indicates if it is ok
		to delete a temporary breakpoint.  Return ``(None, None)`` if there is no
		matching breakpoint.
		
		"""
		pass
		
	


