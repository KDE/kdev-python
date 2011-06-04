#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
""":synopsis: Flexible event logging system for applications.


"""
class Logger:


	"""
	"""
	
	
	def __init__(self, ):
		pass
	
	def setLevel(self, lvl):
		"""
		Sets the threshold for this logger to *lvl*. Logging messages which are less
		severe than *lvl* will be ignored. When a logger is created, the level is set to
		:const:`NOTSET` (which causes all messages to be processed when the logger is
		the root logger, or delegation to the parent when the logger is a non-root
		logger). Note that the root logger is created with level :const:`WARNING`.
		
		The term 'delegation to the parent' means that if a logger has a level of
		NOTSET, its chain of ancestor loggers is traversed until either an ancestor with
		a level other than NOTSET is found, or the root is reached.
		
		If an ancestor is found with a level other than NOTSET, then that ancestor's
		level is treated as the effective level of the logger where the ancestor search
		began, and is used to determine how a logging event is handled.
		
		If the root is reached, and it has a level of NOTSET, then all messages will be
		processed. Otherwise, the root's level will be used as the effective level.
		
		
		"""
		pass
		
	def isEnabledFor(self, lvl):
		"""
		Indicates if a message of severity *lvl* would be processed by this logger.
		This method checks first the module-level level set by
		``logging.disable(lvl)`` and then the logger's effective level as determined
		by :meth:`getEffectiveLevel`.
		
		
		"""
		pass
		
	def getEffectiveLevel(self, ):
		"""
		Indicates the effective level for this logger. If a value other than
		:const:`NOTSET` has been set using :meth:`setLevel`, it is returned. Otherwise,
		the hierarchy is traversed towards the root until a value other than
		:const:`NOTSET` is found, and that value is returned.
		
		
		"""
		pass
		
	def getChild(self, suffix):
		"""
		Returns a logger which is a descendant to this logger, as determined by the suffix.
		Thus, ``logging.getLogger('abc').getChild('def.ghi')`` would return the same
		logger as would be returned by ``logging.getLogger('abc.def.ghi')``. This is a
		convenience method, useful when the parent logger is named using e.g. ``__name__``
		rather than a literal string.
		
		"""
		pass
		
	def debug(self, msg,args,kwargs):
		"""
		Logs a message with level :const:`DEBUG` on this logger. The *msg* is the
		message format string, and the *args* are the arguments which are merged into
		*msg* using the string formatting operator. (Note that this means that you can
		use keywords in the format string, together with a single dictionary argument.)
		
		There are two keyword arguments in *kwargs* which are inspected: *exc_info*
		which, if it does not evaluate as false, causes exception information to be
		added to the logging message. If an exception tuple (in the format returned by
		:func:`sys.exc_info`) is provided, it is used; otherwise, :func:`sys.exc_info`
		is called to get the exception information.
		
		The second keyword argument is *extra* which can be used to pass a
		dictionary which is used to populate the __dict__ of the LogRecord created for
		the logging event with user-defined attributes. These custom attributes can then
		be used as you like. For example, they could be incorporated into logged
		messages. For example::
		
		FORMAT = '%(asctime)-15s %(clientip)s %(user)-8s %(message)s'
		logging.basicConfig(format=FORMAT)
		d = { 'clientip' : '192.168.0.1', 'user' : 'fbloggs' }
		logger = logging.getLogger('tcpserver')
		logger.warning('Protocol problem: %s', 'connection reset', extra=d)
		
		would print something like  ::
		
		2006-02-08 22:20:02,165 192.168.0.1 fbloggs  Protocol problem: connection reset
		
		The keys in the dictionary passed in *extra* should not clash with the keys used
		by the logging system. (See the :class:`Formatter` documentation for more
		information on which keys are used by the logging system.)
		
		If you choose to use these attributes in logged messages, you need to exercise
		some care. In the above example, for instance, the :class:`Formatter` has been
		set up with a format string which expects 'clientip' and 'user' in the attribute
		dictionary of the LogRecord. If these are missing, the message will not be
		logged because a string formatting exception will occur. So in this case, you
		always need to pass the *extra* dictionary with these keys.
		
		While this might be annoying, this feature is intended for use in specialized
		circumstances, such as multi-threaded servers where the same code executes in
		many contexts, and interesting conditions which arise are dependent on this
		context (such as remote client IP address and authenticated user name, in the
		above example). In such circumstances, it is likely that specialized
		:class:`Formatter`\ s would be used with particular :class:`Handler`\ s.
		
		
		"""
		pass
		
	def info(self, msg,args,kwargs):
		"""
		Logs a message with level :const:`INFO` on this logger. The arguments are
		interpreted as for :meth:`debug`.
		
		
		"""
		pass
		
	def warning(self, msg,args,kwargs):
		"""
		Logs a message with level :const:`WARNING` on this logger. The arguments are
		interpreted as for :meth:`debug`.
		
		
		"""
		pass
		
	def error(self, msg,args,kwargs):
		"""
		Logs a message with level :const:`ERROR` on this logger. The arguments are
		interpreted as for :meth:`debug`.
		
		
		"""
		pass
		
	def critical(self, msg,args,kwargs):
		"""
		Logs a message with level :const:`CRITICAL` on this logger. The arguments are
		interpreted as for :meth:`debug`.
		
		
		"""
		pass
		
	def log(self, lvl,msg,args,kwargs):
		"""
		Logs a message with integer level *lvl* on this logger. The other arguments are
		interpreted as for :meth:`debug`.
		
		
		"""
		pass
		
	def exception(self, msg,args):
		"""
		Logs a message with level :const:`ERROR` on this logger. The arguments are
		interpreted as for :meth:`debug`. Exception info is added to the logging
		message. This method should only be called from an exception handler.
		
		
		"""
		pass
		
	def addFilter(self, filt):
		"""
		Adds the specified filter *filt* to this logger.
		
		
		"""
		pass
		
	def removeFilter(self, filt):
		"""
		Removes the specified filter *filt* from this logger.
		
		
		"""
		pass
		
	def filter(self, record):
		"""
		Applies this logger's filters to the record and returns a true value if the
		record is to be processed.
		
		
		"""
		pass
		
	def addHandler(self, hdlr):
		"""
		Adds the specified handler *hdlr* to this logger.
		
		
		"""
		pass
		
	def removeHandler(self, hdlr):
		"""
		Removes the specified handler *hdlr* from this logger.
		
		
		"""
		pass
		
	def findCaller(self, ):
		"""
		Finds the caller's source filename and line number. Returns the filename, line
		number and function name as a 3-element tuple.
		
		"""
		pass
		
	def handle(self, record):
		"""
		Handles a record by passing it to all handlers associated with this logger and
		its ancestors (until a false value of *propagate* is found). This method is used
		for unpickled records received from a socket, as well as those created locally.
		Logger-level filtering is applied using :meth:`~Logger.filter`.
		
		
		"""
		pass
		
	def makeRecord(self, name,lvl,fn,lno,msg,args,exc_info,func=None,extra=None):
		"""
		This is a factory method which can be overridden in subclasses to create
		specialized :class:`LogRecord` instances.
		
		"""
		pass
		
	


class Formatter:


	"""
	Returns a new instance of the :class:`Formatter` class.  The instance is
	initialized with a format string for the message as a whole, as well as a
	format string for the date/time portion of a message.  If no *fmt* is
	specified, ``'%(message)s'`` is used.  If no *datefmt* is specified, the
	ISO8601 date format is used.
	
	"""
	
	
	def __init__(self, ):
		pass
	
	def format(self, record):
		"""
		The record's attribute dictionary is used as the operand to a string
		formatting operation. Returns the resulting string. Before formatting the
		dictionary, a couple of preparatory steps are carried out. The *message*
		attribute of the record is computed using *msg* % *args*. If the
		formatting string contains ``'(asctime)'``, :meth:`formatTime` is called
		to format the event time. If there is exception information, it is
		formatted using :meth:`formatException` and appended to the message. Note
		that the formatted exception information is cached in attribute
		*exc_text*. This is useful because the exception information can be
		pickled and sent across the wire, but you should be careful if you have
		more than one :class:`Formatter` subclass which customizes the formatting
		of exception information. In this case, you will have to clear the cached
		value after a formatter has done its formatting, so that the next
		formatter to handle the event doesn't use the cached value but
		recalculates it afresh.
		
		
		"""
		pass
		
	def formatTime(self, record,datefmt=None):
		"""
		This method should be called from :meth:`format` by a formatter which
		wants to make use of a formatted time. This method can be overridden in
		formatters to provide for any specific requirement, but the basic behavior
		is as follows: if *datefmt* (a string) is specified, it is used with
		:func:`time.strftime` to format the creation time of the
		record. Otherwise, the ISO8601 format is used.  The resulting string is
		returned.
		
		
		"""
		pass
		
	def formatException(self, exc_info):
		"""
		Formats the specified exception information (a standard exception tuple as
		returned by :func:`sys.exc_info`) as a string. This default implementation
		just uses :func:`traceback.print_exception`. The resulting string is
		returned.
		
		.. ilter Objects
		"""
		pass
		
	


class Filter:


	"""
	Returns an instance of the :class:`Filter` class. If *name* is specified, it
	names a logger which, together with its children, will have its events allowed
	through the filter. If *name* is the empty string, allows every event.
	
	
	"""
	
	
	def __init__(self, ):
		pass
	
	def filter(self, record):
		"""
		Is the specified record to be logged? Returns zero for no, nonzero for
		yes. If deemed appropriate, the record may be modified in-place by this
		method.
		
		Note that filters attached to handlers are consulted whenever an event is
		"""
		pass
		
	


class LogRecord:


	"""
	Contains all the information pertinent to the event being logged.
	
	The primary information is passed in :attr:`msg` and :attr:`args`, which
	are combined using ``msg % args`` to create the :attr:`message` field of the
	record.
	
	:param name:  The name of the logger used to log the event represented by
	this LogRecord.
	:param level: The numeric level of the logging event (one of DEBUG, INFO etc.)
	:param pathname: The full pathname of the source file where the logging call
	was made.
	:param lineno: The line number in the source file where the logging call was
	made.
	:param msg: The event description message, possibly a format string with
	placeholders for variable data.
	:param args: Variable data to merge into the *msg* argument to obtain the
	event description.
	:param exc_info: An exception tuple with the current exception information,
	or *None* if no exception information is available.
	:param func: The name of the function or method from which the logging call
	was invoked.
	
	"""
	
	
	def __init__(self, ):
		pass
	
	def getMessage(self, ):
		"""
		Returns the message for this :class:`LogRecord` instance after merging any
		user-supplied arguments with the message. If the user-supplied message
		argument to the logging call is not a string, :func:`str` is called on it to
		convert it to a string. This allows use of user-defined classes as
		messages, whose ``__str__`` method can return the actual format string to
		be used.
		
		
		.. ogRecord attributes
		"""
		pass
		
	


class LoggerAdapter:


	"""
	Returns an instance of :class:`LoggerAdapter` initialized with an
	underlying :class:`Logger` instance and a dict-like object.
	
	"""
	
	
	def __init__(self, ):
		pass
	
	def process(self, msg,kwargs):
		"""
		Modifies the message and/or keyword arguments passed to a logging call in
		order to insert contextual information. This implementation takes the object
		passed as *extra* to the constructor and adds it to *kwargs* using key
		'extra'. The return value is a (*msg*, *kwargs*) tuple which has the
		(possibly modified) versions of the arguments passed in.
		
		In addition to the above, :class:`LoggerAdapter` supports the following
		"""
		pass
		
	def getLogger(self, name):
		"""
		Return a logger with the specified name or, if no name is specified, return a
		logger which is the root logger of the hierarchy. If specified, the name is
		typically a dot-separated hierarchical name like *"a"*, *"a.b"* or *"a.b.c.d"*.
		Choice of these names is entirely up to the developer who is using logging.
		
		All calls to this function with a given name return the same logger instance.
		This means that logger instances never need to be passed between different parts
		of an application.
		
		
		"""
		pass
		
	def getLoggerClass(self, ):
		"""
		Return either the standard :class:`Logger` class, or the last class passed to
		:func:`setLoggerClass`. This function may be called from within a new class
		definition, to ensure that installing a customised :class:`Logger` class will
		not undo customisations already applied by other code. For example::
		
		class MyLogger(logging.getLoggerClass()):
		# *more override behaviour here
		
		
		"""
		pass
		
	def debug(self, msg,args,kwargs):
		"""
		Logs a message with level :const:`DEBUG` on the root logger. The *msg* is the
		message format string, and the *args* are the arguments which are merged into
		*msg* using the string formatting operator. (Note that this means that you can
		use keywords in the format string, together with a single dictionary argument.)
		
		There are two keyword arguments in *kwargs* which are inspected: *exc_info*
		which, if it does not evaluate as false, causes exception information to be
		added to the logging message. If an exception tuple (in the format returned by
		:func:`sys.exc_info`) is provided, it is used; otherwise, :func:`sys.exc_info`
		is called to get the exception information.
		
		The other optional keyword argument is *extra* which can be used to pass a
		dictionary which is used to populate the __dict__ of the LogRecord created for
		the logging event with user-defined attributes. These custom attributes can then
		be used as you like. For example, they could be incorporated into logged
		messages. For example::
		
		FORMAT = "%(asctime)-15s %(clientip)s %(user)-8s %(message)s"
		logging.basicConfig(format=FORMAT)
		d = {'clientip': '192.168.0.1', 'user': 'fbloggs'}
		logging.warning("Protocol problem: %s", "connection reset", extra=d)
		
		would print something like::
		
		2006-02-08 22:20:02,165 192.168.0.1 fbloggs  Protocol problem: connection reset
		
		The keys in the dictionary passed in *extra* should not clash with the keys used
		by the logging system. (See the :class:`Formatter` documentation for more
		information on which keys are used by the logging system.)
		
		If you choose to use these attributes in logged messages, you need to exercise
		some care. In the above example, for instance, the :class:`Formatter` has been
		set up with a format string which expects 'clientip' and 'user' in the attribute
		dictionary of the LogRecord. If these are missing, the message will not be
		logged because a string formatting exception will occur. So in this case, you
		always need to pass the *extra* dictionary with these keys.
		
		While this might be annoying, this feature is intended for use in specialized
		circumstances, such as multi-threaded servers where the same code executes in
		many contexts, and interesting conditions which arise are dependent on this
		context (such as remote client IP address and authenticated user name, in the
		above example). In such circumstances, it is likely that specialized
		:class:`Formatter`\ s would be used with particular :class:`Handler`\ s.
		
		"""
		pass
		
	def info(self, msg,args,kwargs):
		"""
		Logs a message with level :const:`INFO` on the root logger. The arguments are
		interpreted as for :func:`debug`.
		
		
		"""
		pass
		
	def warning(self, msg,args,kwargs):
		"""
		Logs a message with level :const:`WARNING` on the root logger. The arguments are
		interpreted as for :func:`debug`.
		
		
		"""
		pass
		
	def error(self, msg,args,kwargs):
		"""
		Logs a message with level :const:`ERROR` on the root logger. The arguments are
		interpreted as for :func:`debug`.
		
		
		"""
		pass
		
	def critical(self, msg,args,kwargs):
		"""
		Logs a message with level :const:`CRITICAL` on the root logger. The arguments
		are interpreted as for :func:`debug`.
		
		
		"""
		pass
		
	def exception(self, msg,args):
		"""
		Logs a message with level :const:`ERROR` on the root logger. The arguments are
		interpreted as for :func:`debug`. Exception info is added to the logging
		message. This function should only be called from an exception handler.
		
		
		"""
		pass
		
	def log(self, level,msg,args,kwargs):
		"""
		Logs a message with level *level* on the root logger. The other arguments are
		interpreted as for :func:`debug`.
		
		PLEASE NOTE: The above module-level functions which delegate to the root
		logger should *not* be used in threads, in versions of Python earlier than
		2.7.1 and 3.2, unless at least one handler has been added to the root
		logger *before* the threads are started. These convenience functions call
		:func:`basicConfig` to ensure that at least one handler is available; in
		earlier versions of Python, this can (under rare circumstances) lead to
		handlers being added multiple times to the root logger, which can in turn
		lead to multiple messages for the same event.
		
		"""
		pass
		
	def disable(self, lvl):
		"""
		Provides an overriding level *lvl* for all loggers which takes precedence over
		the logger's own level. When the need arises to temporarily throttle logging
		output down across the whole application, this function can be useful. Its
		effect is to disable all logging calls of severity *lvl* and below, so that
		if you call it with a value of INFO, then all INFO and DEBUG events would be
		discarded, whereas those of severity WARNING and above would be processed
		according to the logger's effective level.
		
		
		"""
		pass
		
	def addLevelName(self, lvl,levelName):
		"""
		Associates level *lvl* with text *levelName* in an internal dictionary, which is
		used to map numeric levels to a textual representation, for example when a
		:class:`Formatter` formats a message. This function can also be used to define
		your own levels. The only constraints are that all levels used must be
		registered using this function, levels should be positive integers and they
		should increase in increasing order of severity.
		
		NOTE: If you are thinking of defining your own levels, please see the section
		on :ref:`custom-levels`.
		
		"""
		pass
		
	def getLevelName(self, lvl):
		"""
		Returns the textual representation of logging level *lvl*. If the level is one
		of the predefined levels :const:`CRITICAL`, :const:`ERROR`, :const:`WARNING`,
		:const:`INFO` or :const:`DEBUG` then you get the corresponding string. If you
		have associated levels with names using :func:`addLevelName` then the name you
		have associated with *lvl* is returned. If a numeric value corresponding to one
		of the defined levels is passed in, the corresponding string representation is
		returned. Otherwise, the string "Level %s" % lvl is returned.
		
		
		"""
		pass
		
	def makeLogRecord(self, attrdict):
		"""
		Creates and returns a new :class:`LogRecord` instance whose attributes are
		defined by *attrdict*. This function is useful for taking a pickled
		:class:`LogRecord` attribute dictionary, sent over a socket, and reconstituting
		it as a :class:`LogRecord` instance at the receiving end.
		
		
		"""
		pass
		
	def basicConfig(self, kwargs):
		"""
		Does basic configuration for the logging system by creating a
		:class:`StreamHandler` with a default :class:`Formatter` and adding it to the
		root logger. The functions :func:`debug`, :func:`info`, :func:`warning`,
		:func:`error` and :func:`critical` will call :func:`basicConfig` automatically
		if no handlers are defined for the root logger.
		
		This function does nothing if the root logger already has handlers
		configured for it.
		
		"""
		pass
		
	def shutdown(self, ):
		"""
		Informs the logging system to perform an orderly shutdown by flushing and
		closing all handlers. This should be called at application exit and no
		further use of the logging system should be made after this call.
		
		
		"""
		pass
		
	def setLoggerClass(self, klass):
		"""
		Tells the logging system to use the class *klass* when instantiating a logger.
		The class should define :meth:`__init__` such that only a name argument is
		required, and the :meth:`__init__` should call :meth:`Logger.__init__`. This
		function is typically called before any loggers are instantiated by applications
		which need to use custom logger behavior.
		
		
		Integration with the warnings module
		------------------------------------
		
		The :func:`captureWarnings` function can be used to integrate :mod:`logging`
		with the :mod:`warnings` module.
		
		"""
		pass
		
	def captureWarnings(self, capture):
		"""
		This function is used to turn the capture of warnings by logging on and
		off.
		
		If *capture* is ``True``, warnings issued by the :mod:`warnings` module will
		be redirected to the logging system. Specifically, a warning will be
		formatted using :func:`warnings.formatwarning` and the resulting string
		logged to a logger named 'py.warnings' with a severity of `WARNING`.
		
		If *capture* is ``False``, the redirection of warnings to the logging system
		will stop, and warnings will be redirected to their original destinations
		(i.e. those in effect before `captureWarnings(True)` was called).
		
		
		
		"""
		pass
		
	


