#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
""":synopsis: Extract information and source code from live objects.
"""
def getmembers(object,predicate):
	"""
	Return all the members of an object in a list of (name, value) pairs sorted by
	name.  If the optional *predicate* argument is supplied, only members for which
	the predicate returns a true value are included.
	
	"""
	pass
	
def getmoduleinfo(path):
	"""
	Return a tuple of values that describe how Python will interpret the file
	identified by *path* if it is a module, or ``None`` if it would not be
	identified as a module.  The return tuple is ``(name, suffix, mode,
	module_type)``, where *name* is the name of the module without the name of
	any enclosing package, *suffix* is the trailing part of the file name (which
	may not be a dot-delimited extension), *mode* is the :func:`open` mode that
	would be used (``'r'`` or ``'rb'``), and *module_type* is an integer giving
	the type of the module.  *module_type* will have a value which can be
	compared to the constants defined in the :mod:`imp` module; see the
	documentation for that module for more information on module types.
	
	"""
	pass
	
def getmodulename(path):
	"""
	Return the name of the module named by the file *path*, without including the
	names of enclosing packages.  This uses the same algorithm as the interpreter
	uses when searching for modules.  If the name cannot be matched according to the
	interpreter's rules, ``None`` is returned.
	
	
	"""
	pass
	
def ismodule(object):
	"""
	Return true if the object is a module.
	
	
	"""
	pass
	
def is_class(object):
	"""
	Return true if the object is a class, whether built-in or created in Python
	code.
	
	
	"""
	pass
	
def ismethod(object):
	"""
	Return true if the object is a bound method written in Python.
	
	
	"""
	pass
	
def isfunction(object):
	"""
	Return true if the object is a Python function, which includes functions
	created by a :term:`lambda` expression.
	
	
	"""
	pass
	
def isgeneratorfunction(object):
	"""
	Return true if the object is a Python generator function.
	
	"""
	pass
	
def isgenerator(object):
	"""
	Return true if the object is a generator.
	
	"""
	pass
	
def istraceback(object):
	"""
	Return true if the object is a traceback.
	
	
	"""
	pass
	
def isframe(object):
	"""
	Return true if the object is a frame.
	
	
	"""
	pass
	
def iscode(object):
	"""
	Return true if the object is a code.
	
	
	"""
	pass
	
def isbuiltin(object):
	"""
	Return true if the object is a built-in function or a bound built-in method.
	
	
	"""
	pass
	
def isroutine(object):
	"""
	Return true if the object is a user-defined or built-in function or method.
	
	
	"""
	pass
	
def isabstract(object):
	"""
	Return true if the object is an abstract base class.
	
	"""
	pass
	
def ismethoddescriptor(object):
	"""
	Return true if the object is a method descriptor, but not if
	:func:`ismethod`, :func:`isclass`, :func:`isfunction` or :func:`isbuiltin`
	are true.
	
	This is new as of Python 2.2, and, for example, is true of
	``int.__add__``. An object passing this test has a :attr:`__get__` attribute
	but not a :attr:`__set__` attribute, but beyond that the set of attributes
	varies.  :attr:`__name__` is usually sensible, and :attr:`__doc__` often is.
	
	Methods implemented via descriptors that also pass one of the other tests
	return false from the :func:`ismethoddescriptor` test, simply because the
	other tests promise more -- you can, e.g., count on having the
	:attr:`im_func` attribute (etc) when an object passes :func:`ismethod`.
	
	
	"""
	pass
	
def isdatadescriptor(object):
	"""
	Return true if the object is a data descriptor.
	
	Data descriptors have both a :attr:`__get__` and a :attr:`__set__` attribute.
	Examples are properties (defined in Python), getsets, and members.  The
	latter two are defined in C and there are more specific tests available for
	those types, which is robust across Python implementations.  Typically, data
	descriptors will also have :attr:`__name__` and :attr:`__doc__` attributes
	(properties, getsets, and members have both of these attributes), but this is
	not guaranteed.
	
	"""
	pass
	
def isgetsetdescriptor(object):
	"""
	Return true if the object is a getset descriptor.
	
	"""
	pass
	
def ismemberdescriptor(object):
	"""
	Return true if the object is a member descriptor.
	
	"""
	pass
	
def getdoc(object):
	"""
	Get the documentation string for an object, cleaned up with :func:`cleandoc`.
	
	
	"""
	pass
	
def getcomments(object):
	"""
	Return in a single string any lines of comments immediately preceding the
	object's source code (for a class, function, or method), or at the top of the
	Python source file (if the object is a module).
	
	
	"""
	pass
	
def getfile(object):
	"""
	Return the name of the (text or binary) file in which an object was defined.
	This will fail with a :exc:`TypeError` if the object is a built-in module,
	class, or function.
	
	
	"""
	pass
	
def getmodule(object):
	"""
	Try to guess which module an object was defined in.
	
	
	"""
	pass
	
def getsourcefile(object):
	"""
	Return the name of the Python source file in which an object was defined.  This
	will fail with a :exc:`TypeError` if the object is a built-in module, class, or
	function.
	
	
	"""
	pass
	
def getsourcelines(object):
	"""
	Return a list of source lines and starting line number for an object. The
	argument may be a module, class, method, function, traceback, frame, or code
	object.  The source code is returned as a list of the lines corresponding to the
	object and the line number indicates where in the original source file the first
	line of code was found.  An :exc:`IOError` is raised if the source code cannot
	be retrieved.
	
	
	"""
	pass
	
def getsource(object):
	"""
	Return the text of the source code for an object. The argument may be a module,
	class, method, function, traceback, frame, or code object.  The source code is
	returned as a single string.  An :exc:`IOError` is raised if the source code
	cannot be retrieved.
	
	
	"""
	pass
	
def cleandoc(doc):
	"""
	Clean up indentation from docstrings that are indented to line up with blocks
	of code.  Any whitespace that can be uniformly removed from the second line
	onwards is removed.  Also, all tabs are expanded to spaces.
	
	"""
	pass
	
def get_classtree(_classes,unique):
	"""
	Arrange the given list of classes into a hierarchy of nested lists. Where a
	nested list appears, it contains classes derived from the class whose entry
	immediately precedes the list.  Each entry is a 2-tuple containing a class and a
	tuple of its base classes.  If the *unique* argument is true, exactly one entry
	appears in the returned structure for each class in the given list.  Otherwise,
	classes using multiple inheritance and their descendants will appear multiple
	times.
	
	
	"""
	pass
	
def getargspec(func):
	"""
	Get the names and default values of a Python function's arguments. A tuple of
	four things is returned: ``(args, varargs, keywords, defaults)``. *args* is a
	list of the argument names (it may contain nested lists). *varargs* and
	*keywords* are the names of the ``*`` and ``**`` arguments or
	``None``. *defaults* is a tuple of default argument values or None if there
	are no default arguments; if this tuple has *n* elements, they correspond to
	the last *n* elements listed in *args*.
	
	"""
	pass
	
def getargvalues(frame):
	"""
	Get information about arguments passed into a particular frame. A tuple of
	four things is returned: ``(args, varargs, keywords, locals)``. *args* is a
	list of the argument names (it may contain nested lists). *varargs* and
	*keywords* are the names of the ``*`` and ``**`` arguments or ``None``.
	*locals* is the locals dictionary of the given frame.
	
	"""
	pass
	
def formatargspec(args,varargs,varkw,defaults,formatarg,formatvarargs,formatvarkw,formatvalue,join):
	"""
	Format a pretty argument spec from the four values returned by
	:func:`getargspec`.  The format\* arguments are the corresponding optional
	formatting functions that are called to turn names and values into strings.
	
	
	"""
	pass
	
def formatargvalues(args,varargs,varkw,locals,formatarg,formatvarargs,formatvarkw,formatvalue,join):
	"""
	Format a pretty argument spec from the four values returned by
	:func:`getargvalues`.  The format\* arguments are the corresponding optional
	formatting functions that are called to turn names and values into strings.
	
	
	"""
	pass
	
def getmro(cls):
	"""
	Return a tuple of class cls's base classes, including cls, in method resolution
	order.  No class appears more than once in this tuple. Note that the method
	resolution order depends on cls's type.  Unless a very peculiar user-defined
	metatype is in use, cls will be the first element of the tuple.
	
	
	"""
	pass
	
def getcallargs(func,args,kwds):
	"""
	Bind the *args* and *kwds* to the argument names of the Python function or
	method *func*, as if it was called with them. For bound methods, bind also the
	first argument (typically named ``self``) to the associated instance. A dict
	is returned, mapping the argument names (including the names of the ``*`` and
	``**`` arguments, if any) to their values from *args* and *kwds*. In case of
	invoking *func* incorrectly, i.e. whenever ``func(*args, **kwds)`` would raise
	an exception because of incompatible signature, an exception of the same type
	and the same or similar message is raised. For example::
	
	>>> from inspect import getcallargs
	>>> def f(a, b=1, *pos, **named):
	more     pass
	>>> getcallargs(f, 1, 2, 3)
	{'a': 1, 'named': {}, 'b': 2, 'pos': (3,)}
	>>> getcallargs(f, a=2, x=4)
	{'a': 2, 'named': {'x': 4}, 'b': 1, 'pos': ()}
	>>> getcallargs(f)
	Traceback (most recent call last):
	more
	TypeError: f() takes at least 1 argument (0 given)
	
	"""
	pass
	
def getframeinfo(frame,context):
	"""
	Get information about a frame or traceback object.  A 5-tuple is returned, the
	last five elements of the frame's frame record.
	
	"""
	pass
	
def getouterframes(frame,context):
	"""
	Get a list of frame records for a frame and all outer frames.  These frames
	represent the calls that lead to the creation of *frame*. The first entry in the
	returned list represents *frame*; the last entry represents the outermost call
	on *frame*'s stack.
	
	
	"""
	pass
	
def getinnerframes(traceback,context):
	"""
	Get a list of frame records for a traceback's frame and all inner frames.  These
	frames represent calls made as a consequence of *frame*.  The first entry in the
	list represents *traceback*; the last entry represents where the exception was
	raised.
	
	
	"""
	pass
	
def currentframe():
	"""
	Return the frame object for the caller's stack frame.
	
	"""
	pass
	
def stack(context):
	"""
	Return a list of frame records for the caller's stack.  The first entry in the
	returned list represents the caller; the last entry represents the outermost
	call on the stack.
	
	
	"""
	pass
	
