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
	
	
	def __init__(self, stream=None):
		pass
	
	


class FileHandler:


	"""
	Returns a new instance of the :class:`FileHandler` class. The specified file is
	opened and used as the stream for logging. If *mode* is not specified,
	:const:`'a'` is used.  If *encoding* is not *None*, it is used to open the file
	with that encoding.  If *delay* is true, then file opening is deferred until the
	first call to :meth:`emit`. By default, the file grows indefinitely.
	
	"""
	
	
	def __init__(self, filename,mode='a',encoding=None,delay=False):
		pass
	
	


class NullHandler:


	"""
	Returns a new instance of the :class:`NullHandler` class.
	
	"""
	
	
	def __init__(self, ):
		pass
	
	


class WatchedFileHandler:


	"""
	Returns a new instance of the :class:`WatchedFileHandler` class. The specified
	file is opened and used as the stream for logging. If *mode* is not specified,
	:const:`'a'` is used.  If *encoding* is not *None*, it is used to open the file
	with that encoding.  If *delay* is true, then file opening is deferred until the
	first call to :meth:`emit`.  By default, the file grows indefinitely.
	
	
	"""
	
	
	def __init__(self, filename,mode,encoding,delay):
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
	
	
	def __init__(self, filename,mode='a',maxBytes=0,backupCount=0,encoding=None,delay=0):
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
	
	
	def __init__(self, filename,when='h',interval=1,backupCount=0,encoding=None,delay=False,utc=False):
		pass
	
	


class SocketHandler:


	"""
	Returns a new instance of the :class:`SocketHandler` class intended to
	communicate with a remote machine whose address is given by *host* and *port*.
	
	
	"""
	
	
	def __init__(self, host,port):
		pass
	
	


class DatagramHandler:


	"""
	Returns a new instance of the :class:`DatagramHandler` class intended to
	communicate with a remote machine whose address is given by *host* and *port*.
	
	
	"""
	
	
	def __init__(self, host,port):
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
	
	
	def __init__(self, address='localhost',SYSLOG_UDP_PORT,facility=LOG_USER,socktype=socket):
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
	
	
	def __init__(self, appname,dllname=None,logtype='Application'):
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
	
	
	def __init__(self, mailhost,_fromaddr,toaddrs,subject,credentials=None,secure=None):
		pass
	
	


class BufferingHandler:


	"""
	Initializes the handler with a buffer of the specified capacity.
	
	
	"""
	
	
	def __init__(self, capacity):
		pass
	
	


class MemoryHandler:


	"""
	Returns a new instance of the :class:`MemoryHandler` class. The instance is
	initialized with a buffer size of *capacity*. If *flushLevel* is not specified,
	:const:`ERROR` is used. If no *target* is specified, the target will need to be
	set using :meth:`setTarget` before this handler does anything useful.
	
	
	"""
	
	
	def __init__(self, capacity,flushLevel=ERROR,target=None):
		pass
	
	


class HTTPHandler:


	"""
	Returns a new instance of the :class:`HTTPHandler` class. The *host* can be
	of the form ``host:port``, should you need to use a specific port number.
	If no *method* is specified, ``GET`` is used.
	
	
	"""
	
	
	def __init__(self, host,url,method='GET'):
		pass
	
	


