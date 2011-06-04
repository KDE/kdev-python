#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
""":synopsis: Handlers for the logging module.


"""
class StreamHandler:


	"""
	Returns a new instance of the :class:`StreamHandler` class. If *stream* is
	specified, the instance will use it for logging output; otherwise, *sys.stderr*
	will be used.
	
	
	"""
	
	
	def __init__(self, ):
		pass
	
	def emit(self, record):
		"""
		If a formatter is specified, it is used to format the record. The record
		is then written to the stream with a newline terminator. If exception
		information is present, it is formatted using
		:func:`traceback.print_exception` and appended to the stream.
		
		
		"""
		pass
		
	def flush(self, ):
		"""
		Flushes the stream by calling its :meth:`flush` method. Note that the
		:meth:`close` method is inherited from :class:`Handler` and so does
		no output, so an explicit :meth:`flush` call may be needed at times.
		
		.. ileHandler
		"""
		pass
		
	


class FileHandler:


	"""
	Returns a new instance of the :class:`FileHandler` class. The specified file is
	opened and used as the stream for logging. If *mode* is not specified,
	:const:`'a'` is used.  If *encoding* is not *None*, it is used to open the file
	with that encoding.  If *delay* is true, then file opening is deferred until the
	first call to :meth:`emit`. By default, the file grows indefinitely.
	
	"""
	
	
	def __init__(self, ):
		pass
	
	def close(self, ):
		"""
		Closes the file.
		
		
		"""
		pass
		
	def emit(self, record):
		"""
		Outputs the record to the file.
		
		
		.. ullHandler
		"""
		pass
		
	


class NullHandler:


	"""
	Returns a new instance of the :class:`NullHandler` class.
	
	"""
	
	
	def __init__(self, ):
		pass
	
	def emit(self, record):
		"""
		This method does nothing.
		
		"""
		pass
		
	def handle(self, record):
		"""
		This method does nothing.
		
		"""
		pass
		
	def createLock(self, ):
		"""
		This method returns ``None`` for the lock, since there is no
		underlying I/O to which access needs to be serialized.
		
		
		See :ref:`library-config` for more information on how to use
		"""
		pass
		
	


class WatchedFileHandler:


	"""
	Returns a new instance of the :class:`WatchedFileHandler` class. The specified
	file is opened and used as the stream for logging. If *mode* is not specified,
	:const:`'a'` is used.  If *encoding* is not *None*, it is used to open the file
	with that encoding.  If *delay* is true, then file opening is deferred until the
	first call to :meth:`emit`.  By default, the file grows indefinitely.
	
	
	"""
	
	
	def __init__(self, ):
		pass
	
	def emit(self, record):
		"""
		Outputs the record to the file, but first checks to see if the file has
		changed.  If it has, the existing stream is flushed and closed and the
		file opened again, before outputting the record to the file.
		
		.. otatingFileHandler
		"""
		pass
		
	


class RotatingFileHandler:


	"""
	Returns a new instance of the :class:`RotatingFileHandler` class. The specified
	file is opened and used as the stream for logging. If *mode* is not specified,
	``'a'`` is used.  If *encoding* is not *None*, it is used to open the file
	with that encoding.  If *delay* is true, then file opening is deferred until the
	first call to :meth:`emit`.  By default, the file grows indefinitely.
	
	You can use the *maxBytes* and *backupCount* values to allow the file to
	:dfn:`rollover` at a predetermined size. When the size is about to be exceeded,
	the file is closed and a new file is silently opened for output. Rollover occurs
	whenever the current log file is nearly *maxBytes* in length; if *maxBytes* is
	zero, rollover never occurs.  If *backupCount* is non-zero, the system will save
	old log files by appending the extensions '.1', '.2' etc., to the filename. For
	example, with a *backupCount* of 5 and a base file name of :file:`app.log`, you
	would get :file:`app.log`, :file:`app.log.1`, :file:`app.log.2`, up to
	:file:`app.log.5`. The file being written to is always :file:`app.log`.  When
	this file is filled, it is closed and renamed to :file:`app.log.1`, and if files
	:file:`app.log.1`, :file:`app.log.2`, etc.  exist, then they are renamed to
	:file:`app.log.2`, :file:`app.log.3` etc.  respectively.
	
	"""
	
	
	def __init__(self, ):
		pass
	
	def doRollover(self, ):
		"""
		Does a rollover, as described above.
		
		
		"""
		pass
		
	def emit(self, record):
		"""
		Outputs the record to the file, catering for rollover as described
		previously.
		
		.. imedRotatingFileHandler
		"""
		pass
		
	


class TimedRotatingFileHandler:


	"""
	Returns a new instance of the :class:`TimedRotatingFileHandler` class. The
	specified file is opened and used as the stream for logging. On rotating it also
	sets the filename suffix. Rotating happens based on the product of *when* and
	*interval*.
	
	You can use the *when* to specify the type of *interval*. The list of possible
	values is below.  Note that they are not case sensitive.
	
	+----------------+-----------------------+
	| Value          | Type of interval      |
	+================+=======================+
	| ``'S'``        | Seconds               |
	+----------------+-----------------------+
	| ``'M'``        | Minutes               |
	+----------------+-----------------------+
	| ``'H'``        | Hours                 |
	+----------------+-----------------------+
	| ``'D'``        | Days                  |
	+----------------+-----------------------+
	| ``'W'``        | Week day (0=Monday)   |
	+----------------+-----------------------+
	| ``'midnight'`` | Roll over at midnight |
	+----------------+-----------------------+
	
	The system will save old log files by appending extensions to the filename.
	The extensions are date-and-time based, using the strftime format
	``%Y-%m-%d_%H-%M-%S`` or a leading portion thereof, depending on the
	rollover interval.
	
	When computing the next rollover time for the first time (when the handler
	is created), the last modification time of an existing log file, or else
	the current time, is used to compute when the next rotation will occur.
	
	If the *utc* argument is true, times in UTC will be used; otherwise
	local time is used.
	
	If *backupCount* is nonzero, at most *backupCount* files
	will be kept, and if more would be created when rollover occurs, the oldest
	one is deleted. The deletion logic uses the interval to determine which
	files to delete, so changing the interval may leave old files lying around.
	
	If *delay* is true, then file opening is deferred until the first call to
	:meth:`emit`.
	
	"""
	
	
	def __init__(self, ):
		pass
	
	def doRollover(self, ):
		"""
		Does a rollover, as described above.
		
		
		"""
		pass
		
	def emit(self, record):
		"""
		Outputs the record to the file, catering for rollover as described above.
		
		
		.. ocketHandler
		"""
		pass
		
	


class SocketHandler:


	"""
	Returns a new instance of the :class:`SocketHandler` class intended to
	communicate with a remote machine whose address is given by *host* and *port*.
	
	
	"""
	
	
	def __init__(self, ):
		pass
	
	def close(self, ):
		"""
		Closes the socket.
		
		
		"""
		pass
		
	def emit(self, ):
		"""
		Pickles the record's attribute dictionary and writes it to the socket in
		binary format. If there is an error with the socket, silently drops the
		packet. If the connection was previously lost, re-establishes the
		connection. To unpickle the record at the receiving end into a
		:class:`LogRecord`, use the :func:`makeLogRecord` function.
		
		
		"""
		pass
		
	def handleError(self, ):
		"""
		Handles an error which has occurred during :meth:`emit`. The most likely
		cause is a lost connection. Closes the socket so that we can retry on the
		next event.
		
		
		"""
		pass
		
	def makeSocket(self, ):
		"""
		This is a factory method which allows subclasses to define the precise
		type of socket they want. The default implementation creates a TCP socket
		(:const:`socket.SOCK_STREAM`).
		
		
		"""
		pass
		
	def makePickle(self, record):
		"""
		Pickles the record's attribute dictionary in binary format with a length
		prefix, and returns it ready for transmission across the socket.
		
		Note that pickles aren't completely secure. If you are concerned about
		security, you may want to override this method to implement a more secure
		mechanism. For example, you can sign pickles using HMAC and then verify
		them on the receiving end, or alternatively you can disable unpickling of
		global objects on the receiving end.
		
		
		"""
		pass
		
	def send(self, packet):
		"""
		Send a pickled string *packet* to the socket. This function allows for
		partial sends which can happen when the network is busy.
		
		
		"""
		pass
		
	def createSocket(self, ):
		"""
		Tries to create a socket; on failure, uses an exponential back-off
		algorithm.  On intial failure, the handler will drop the message it was
		trying to send.  When subsequent messages are handled by the same
		instance, it will not try connecting until some time has passed.  The
		default parameters are such that the initial delay is one second, and if
		after that delay the connection still can't be made, the handler will
		double the delay each time up to a maximum of 30 seconds.
		
		This behaviour is controlled by the following handler attributes:
		
		* ``retryStart`` (initial delay, defaulting to 1.0 seconds).
		* ``retryFactor`` (multiplier, defaulting to 2.0).
		* ``retryMax`` (maximum delay, defaulting to 30.0 seconds).
		
		This means that if the remote listener starts up *after* the handler has
		been used, you could lose messages (since the handler won't even attempt
		a connection until the delay has elapsed, but just silently drop messages
		during the delay period).
		
		
		.. atagramHandler
		"""
		pass
		
	


class DatagramHandler:


	"""
	Returns a new instance of the :class:`DatagramHandler` class intended to
	communicate with a remote machine whose address is given by *host* and *port*.
	
	
	"""
	
	
	def __init__(self, ):
		pass
	
	def emit(self, ):
		"""
		Pickles the record's attribute dictionary and writes it to the socket in
		binary format. If there is an error with the socket, silently drops the
		packet. To unpickle the record at the receiving end into a
		:class:`LogRecord`, use the :func:`makeLogRecord` function.
		
		
		"""
		pass
		
	def makeSocket(self, ):
		"""
		The factory method of :class:`SocketHandler` is here overridden to create
		a UDP socket (:const:`socket.SOCK_DGRAM`).
		
		
		"""
		pass
		
	def send(self, s):
		"""
		Send a pickled string to a socket.
		
		
		.. ysLogHandler
		"""
		pass
		
	


class SysLogHandler:


	"""
	Returns a new instance of the :class:`SysLogHandler` class intended to
	communicate with a remote Unix machine whose address is given by *address* in
	the form of a ``(host, port)`` tuple.  If *address* is not specified,
	``('localhost', 514)`` is used.  The address is used to open a socket.  An
	alternative to providing a ``(host, port)`` tuple is providing an address as a
	string, for example '/dev/log'. In this case, a Unix domain socket is used to
	send the message to the syslog. If *facility* is not specified,
	:const:`LOG_USER` is used. The type of socket opened depends on the
	*socktype* argument, which defaults to :const:`socket.SOCK_DGRAM` and thus
	opens a UDP socket. To open a TCP socket (for use with the newer syslog
	daemons such as rsyslog), specify a value of :const:`socket.SOCK_STREAM`.
	
	Note that if your server is not listening on UDP port 514,
	:class:`SysLogHandler` may appear not to work. In that case, check what
	address you should be using for a domain socket - it's system dependent.
	For example, on Linux it's usually '/dev/log' but on OS/X it's
	'/var/run/syslog'. You'll need to check your platform and use the
	appropriate address (you may need to do this check at runtime if your
	application needs to run on several platforms). On Windows, you pretty
	much have to use the UDP option.
	
	"""
	
	
	def __init__(self, ):
		pass
	
	def close(self, ):
		"""
		Closes the socket to the remote host.
		
		
		"""
		pass
		
	def emit(self, record):
		"""
		The record is formatted, and then sent to the syslog server. If exception
		information is present, it is *not* sent to the server.
		
		
		"""
		pass
		
	def encodePriority(self, facility,priority):
		"""
		Encodes the facility and priority into an integer. You can pass in strings
		or integers - if strings are passed, internal mapping dictionaries are
		used to convert them to integers.
		
		The symbolic ``LOG_`` values are defined in :class:`SysLogHandler` and
		mirror the values defined in the ``sys/syslog.h`` header file.
		
		**Priorities**
		
		+--------------------------+---------------+
		| Name (string)            | Symbolic value|
		+==========================+===============+
		| ``alert``                | LOG_ALERT     |
		+--------------------------+---------------+
		| ``crit`` or ``critical`` | LOG_CRIT      |
		+--------------------------+---------------+
		| ``debug``                | LOG_DEBUG     |
		+--------------------------+---------------+
		| ``emerg`` or ``panic``   | LOG_EMERG     |
		+--------------------------+---------------+
		| ``err`` or ``error``     | LOG_ERR       |
		+--------------------------+---------------+
		| ``info``                 | LOG_INFO      |
		+--------------------------+---------------+
		| ``notice``               | LOG_NOTICE    |
		+--------------------------+---------------+
		| ``warn`` or ``warning``  | LOG_WARNING   |
		+--------------------------+---------------+
		
		**Facilities**
		
		+---------------+---------------+
		| Name (string) | Symbolic value|
		+===============+===============+
		| ``auth``      | LOG_AUTH      |
		+---------------+---------------+
		| ``authpriv``  | LOG_AUTHPRIV  |
		+---------------+---------------+
		| ``cron``      | LOG_CRON      |
		+---------------+---------------+
		| ``daemon``    | LOG_DAEMON    |
		+---------------+---------------+
		| ``ftp``       | LOG_FTP       |
		+---------------+---------------+
		| ``kern``      | LOG_KERN      |
		+---------------+---------------+
		| ``lpr``       | LOG_LPR       |
		+---------------+---------------+
		| ``mail``      | LOG_MAIL      |
		+---------------+---------------+
		| ``news``      | LOG_NEWS      |
		+---------------+---------------+
		| ``syslog``    | LOG_SYSLOG    |
		+---------------+---------------+
		| ``user``      | LOG_USER      |
		+---------------+---------------+
		| ``uucp``      | LOG_UUCP      |
		+---------------+---------------+
		| ``local0``    | LOG_LOCAL0    |
		+---------------+---------------+
		| ``local1``    | LOG_LOCAL1    |
		+---------------+---------------+
		| ``local2``    | LOG_LOCAL2    |
		+---------------+---------------+
		| ``local3``    | LOG_LOCAL3    |
		+---------------+---------------+
		| ``local4``    | LOG_LOCAL4    |
		+---------------+---------------+
		| ``local5``    | LOG_LOCAL5    |
		+---------------+---------------+
		| ``local6``    | LOG_LOCAL6    |
		+---------------+---------------+
		| ``local7``    | LOG_LOCAL7    |
		+---------------+---------------+
		
		"""
		pass
		
	def mapPriority(self, levelname):
		"""
		Maps a logging level name to a syslog priority name.
		You may need to override this if you are using custom levels, or
		if the default algorithm is not suitable for your needs. The
		default algorithm maps ``DEBUG``, ``INFO``, ``WARNING``, ``ERROR`` and
		``CRITICAL`` to the equivalent syslog names, and all other level
		names to 'warning'.
		
		.. TEventLogHandler
		"""
		pass
		
	


class NTEventLogHandler:


	"""
	Returns a new instance of the :class:`NTEventLogHandler` class. The *appname* is
	used to define the application name as it appears in the event log. An
	appropriate registry entry is created using this name. The *dllname* should give
	the fully qualified pathname of a .dll or .exe which contains message
	definitions to hold in the log (if not specified, ``'win32service.pyd'`` is used
	- this is installed with the Win32 extensions and contains some basic
	placeholder message definitions. Note that use of these placeholders will make
	your event logs big, as the entire message source is held in the log. If you
	want slimmer logs, you have to pass in the name of your own .dll or .exe which
	contains the message definitions you want to use in the event log). The
	*logtype* is one of ``'Application'``, ``'System'`` or ``'Security'``, and
	defaults to ``'Application'``.
	
	
	"""
	
	
	def __init__(self, ):
		pass
	
	def close(self, ):
		"""
		At this point, you can remove the application name from the registry as a
		source of event log entries. However, if you do this, you will not be able
		to see the events as you intended in the Event Log Viewer - it needs to be
		able to access the registry to get the .dll name. The current version does
		not do this.
		
		
		"""
		pass
		
	def emit(self, record):
		"""
		Determines the message ID, event category and event type, and then logs
		the message in the NT event log.
		
		
		"""
		pass
		
	def getEventCategory(self, record):
		"""
		Returns the event category for the record. Override this if you want to
		specify your own categories. This version returns 0.
		
		
		"""
		pass
		
	def getEventType(self, record):
		"""
		Returns the event type for the record. Override this if you want to
		specify your own types. This version does a mapping using the handler's
		typemap attribute, which is set up in :meth:`__init__` to a dictionary
		which contains mappings for :const:`DEBUG`, :const:`INFO`,
		:const:`WARNING`, :const:`ERROR` and :const:`CRITICAL`. If you are using
		your own levels, you will either need to override this method or place a
		suitable dictionary in the handler's *typemap* attribute.
		
		
		"""
		pass
		
	def getMessageID(self, record):
		"""
		Returns the message ID for the record. If you are using your own messages,
		you could do this by having the *msg* passed to the logger being an ID
		rather than a format string. Then, in here, you could use a dictionary
		lookup to get the message ID. This version returns 1, which is the base
		message ID in :file:`win32service.pyd`.
		
		.. MTPHandler
		"""
		pass
		
	


class SMTPHandler:


	"""
	Returns a new instance of the :class:`SMTPHandler` class. The instance is
	initialized with the from and to addresses and subject line of the email.
	The *toaddrs* should be a list of strings. To specify a non-standard SMTP
	port, use the (host, port) tuple format for the *mailhost* argument. If you
	use a string, the standard SMTP port is used. If your SMTP server requires
	authentication, you can specify a (username, password) tuple for the
	*credentials* argument. If *secure* is True, then the handler will attempt
	to use TLS for the email transmission.
	
	"""
	
	
	def __init__(self, ):
		pass
	
	def emit(self, record):
		"""
		Formats the record and sends it to the specified addressees.
		
		
		"""
		pass
		
	def getSubject(self, record):
		"""
		If you want to specify a subject line which is record-dependent, override
		this method.
		
		.. emoryHandler
		"""
		pass
		
	


class BufferingHandler:


	"""
	Initializes the handler with a buffer of the specified capacity.
	
	
	"""
	
	
	def __init__(self, ):
		pass
	
	def emit(self, record):
		"""
		Appends the record to the buffer. If :meth:`shouldFlush` returns true,
		calls :meth:`flush` to process the buffer.
		
		
		"""
		pass
		
	def flush(self, ):
		"""
		You can override this to implement custom flushing behavior. This version
		just zaps the buffer to empty.
		
		
		"""
		pass
		
	def shouldFlush(self, record):
		"""
		Returns true if the buffer is up to capacity. This method can be
		overridden to implement custom flushing strategies.
		
		
		"""
		pass
		
	


class MemoryHandler:


	"""
	Returns a new instance of the :class:`MemoryHandler` class. The instance is
	initialized with a buffer size of *capacity*. If *flushLevel* is not specified,
	:const:`ERROR` is used. If no *target* is specified, the target will need to be
	set using :meth:`setTarget` before this handler does anything useful.
	
	
	"""
	
	
	def __init__(self, ):
		pass
	
	def close(self, ):
		"""
		Calls :meth:`flush`, sets the target to :const:`None` and clears the
		buffer.
		
		
		"""
		pass
		
	def flush(self, ):
		"""
		For a :class:`MemoryHandler`, flushing means just sending the buffered
		records to the target, if there is one. The buffer is also cleared when
		this happens. Override if you want different behavior.
		
		
		"""
		pass
		
	def setTarget(self, target):
		""""""
		pass
		
	def shouldFlush(self, record):
		"""
		Checks for buffer full or a record at the *flushLevel* or higher.
		
		
		.. TTPHandler
		"""
		pass
		
	


class HTTPHandler:


	"""
	Returns a new instance of the :class:`HTTPHandler` class. The *host* can be
	of the form ``host:port``, should you need to use a specific port number.
	If no *method* is specified, ``GET`` is used.
	
	
	"""
	
	
	def __init__(self, ):
		pass
	
	def emit(self, record):
		"""
		Sends the record to the Web server as a percent-encoded dictionary.
		
		
		"""
		pass
		
	


