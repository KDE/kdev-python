#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
""":synopsis: Core tools for working with streams.
"""
"""
An int containing the default buffer size used by the module's buffered I/O
classes.  :func:`.open` uses the file's blksize (as obtained by
:func:`os.stat`) if possible.

"""
DEFAULT_BUFFER_SIZE = None
def open(file,mode='r',buffering=_1,encoding=None,errors=None,newline=None,closefd=True):
	"""
	Open *file* and return a corresponding stream.  If the file cannot be opened,
	an :exc:`IOError` is raised.
	
	*file* is either a string giving the pathname (absolute or
	relative to the current working directory) of the file to be opened or
	an integer file descriptor of the file to be wrapped.  (If a file descriptor
	is given, it is closed when the returned I/O object is closed, unless
	*closefd* is set to ``False``.)
	
	*mode* is an optional string that specifies the mode in which the file is
	opened.  It defaults to ``'r'`` which means open for reading in text mode.
	Other common values are ``'w'`` for writing (truncating the file if it
	already exists), and ``'a'`` for appending (which on *some* Unix systems,
	means that *all* writes append to the end of the file regardless of the
	current seek position).  In text mode, if *encoding* is not specified the
	encoding used is platform dependent. (For reading and writing raw bytes use
	binary mode and leave *encoding* unspecified.)  The available modes are:
	
	========= ===============================================================
	Character Meaning
	--------- ---------------------------------------------------------------
	``'r'``   open for reading (default)
	``'w'``   open for writing, truncating the file first
	``'a'``   open for writing, appending to the end of the file if it exists
	``'b'``   binary mode
	``'t'``   text mode (default)
	``'+'``   open a disk file for updating (reading and writing)
	``'U'``   universal newline mode (for backwards compatibility; should
	not be used in new code)
	========= ===============================================================
	
	The default mode is ``'rt'`` (open for reading text).  For binary random
	access, the mode ``'w+b'`` opens and truncates the file to 0 bytes, while
	``'r+b'`` opens the file without truncation.
	
	Python distinguishes between files opened in binary and text modes, even when
	the underlying operating system doesn't.  Files opened in binary mode
	(including ``'b'`` in the *mode* argument) return contents as :class:`bytes`
	objects without any decoding.  In text mode (the default, or when ``'t'`` is
	included in the *mode* argument), the contents of the file are returned as
	:class:`unicode` strings, the bytes having been first decoded using a
	platform-dependent encoding or using the specified *encoding* if given.
	
	*buffering* is an optional integer used to set the buffering policy.
	Pass 0 to switch buffering off (only allowed in binary mode), 1 to select
	line buffering (only usable in text mode), and an integer > 1 to indicate
	the size of a fixed-size chunk buffer.  When no *buffering* argument is
	given, the default buffering policy works as follows:
	
	* Binary files are buffered in fixed-size chunks; the size of the buffer
	is chosen using a heuristic trying to determine the underlying device's
	"block size" and falling back on :attr:`DEFAULT_BUFFER_SIZE`.
	On many systems, the buffer will typically be 4096 or 8192 bytes long.
	
	* "Interactive" text files (files for which :meth:`isatty` returns True)
	use line buffering.  Other text files use the policy described above
	for binary files.
	
	*encoding* is the name of the encoding used to decode or encode the file.
	This should only be used in text mode.  The default encoding is platform
	dependent (whatever :func:`locale.getpreferredencoding` returns), but any
	encoding supported by Python can be used.  See the :mod:`codecs` module for
	the list of supported encodings.
	
	*errors* is an optional string that specifies how encoding and decoding
	errors are to be handled--this cannot be used in binary mode.  Pass
	``'strict'`` to raise a :exc:`ValueError` exception if there is an encoding
	error (the default of ``None`` has the same effect), or pass ``'ignore'`` to
	ignore errors.  (Note that ignoring encoding errors can lead to data loss.)
	``'replace'`` causes a replacement marker (such as ``'?'``) to be inserted
	where there is malformed data.  When writing, ``'xmlcharrefreplace'``
	(replace with the appropriate XML character reference) or
	``'backslashreplace'`` (replace with backslashed escape sequences) can be
	used.  Any other error handling name that has been registered with
	:func:`codecs.register_error` is also valid.
	
	*newline* controls how universal newlines works (it only applies to text
	mode).  It can be ``None``, ``''``, ``'\n'``, ``'\r'``, and ``'\r\n'``.  It
	works as follows:
	
	* On input, if *newline* is ``None``, universal newlines mode is enabled.
	Lines in the input can end in ``'\n'``, ``'\r'``, or ``'\r\n'``, and these
	are translated into ``'\n'`` before being returned to the caller.  If it is
	``''``, universal newline mode is enabled, but line endings are returned to
	the caller untranslated.  If it has any of the other legal values, input
	lines are only terminated by the given string, and the line ending is
	returned to the caller untranslated.
	
	* On output, if *newline* is ``None``, any ``'\n'`` characters written are
	translated to the system default line separator, :data:`os.linesep`.  If
	*newline* is ``''``, no translation takes place.  If *newline* is any of
	the other legal values, any ``'\n'`` characters written are translated to
	the given string.
	
	If *closefd* is ``False`` and a file descriptor rather than a filename was
	given, the underlying file descriptor will be kept open when the file is
	closed.  If a filename is given *closefd* has no effect and must be ``True``
	(the default).
	
	The type of file object returned by the :func:`.open` function depends on the
	mode.  When :func:`.open` is used to open a file in a text mode (``'w'``,
	``'r'``, ``'wt'``, ``'rt'``, etc.), it returns a subclass of
	:class:`TextIOBase` (specifically :class:`TextIOWrapper`).  When used to open
	a file in a binary mode with buffering, the returned class is a subclass of
	:class:`BufferedIOBase`.  The exact class varies: in read binary mode, it
	returns a :class:`BufferedReader`; in write binary and append binary modes,
	it returns a :class:`BufferedWriter`, and in read/write mode, it returns a
	:class:`BufferedRandom`.  When buffering is disabled, the raw stream, a
	subclass of :class:`RawIOBase`, :class:`FileIO`, is returned.
	
	It is also possible to use an :class:`unicode` or :class:`bytes` string
	as a file for both reading and writing.  For :class:`unicode` strings
	:class:`StringIO` can be used like a file opened in text mode,
	and for :class:`bytes` a :class:`BytesIO` can be used like a
	file opened in a binary mode.
	
	
	"""
	pass
	
class IOBase:


	"""
	The abstract base class for all I/O classes, acting on streams of bytes.
	There is no public constructor.
	
	This class provides empty abstract implementations for many methods
	that derived classes can override selectively; the default
	implementations represent a file that cannot be read, written or
	seeked.
	
	Even though :class:`IOBase` does not declare :meth:`read`, :meth:`readinto`,
	or :meth:`write` because their signatures will vary, implementations and
	clients should consider those methods part of the interface.  Also,
	implementations may raise a :exc:`IOError` when operations they do not
	support are called.
	
	The basic type used for binary data read from or written to a file is
	:class:`bytes` (also known as :class:`str`).  :class:`bytearray`\s are
	accepted too, and in some cases (such as :class:`readinto`) required.
	Text I/O classes work with :class:`unicode` data.
	
	Note that calling any method (even inquiries) on a closed stream is
	undefined.  Implementations may raise :exc:`IOError` in this case.
	
	IOBase (and its subclasses) support the iterator protocol, meaning that an
	:class:`IOBase` object can be iterated over yielding the lines in a stream.
	Lines are defined slightly differently depending on whether the stream is
	a binary stream (yielding :class:`bytes`), or a text stream (yielding
	:class:`unicode` strings).  See :meth:`readline` below.
	
	IOBase is also a context manager and therefore supports the
	:keyword:`with` statement.  In this example, *file* is closed after the
	:keyword:`with` statement's suite is finished---even if an exception occurs::
	
	with io.open('spam.txt', 'w') as file:
	file.write(u'Spam and eggs!')
	
	:class:`IOBase` provides these data attributes and methods:
	
	"""
	
	
	def __init__(self, ):
		pass
	
	


class RawIOBase:


	"""
	Base class for raw binary I/O.  It inherits :class:`IOBase`.  There is no
	public constructor.
	
	Raw binary I/O typically provides low-level access to an underlying OS
	device or API, and does not try to encapsulate it in high-level primitives
	(this is left to Buffered I/O and Text I/O, described later in this page).
	
	In addition to the attributes and methods from :class:`IOBase`,
	RawIOBase provides the following methods:
	
	"""
	
	
	def __init__(self, ):
		pass
	
	


class BufferedIOBase:


	"""
	Base class for binary streams that support some kind of buffering.
	It inherits :class:`IOBase`. There is no public constructor.
	
	The main difference with :class:`RawIOBase` is that methods :meth:`read`,
	:meth:`readinto` and :meth:`write` will try (respectively) to read as much
	input as requested or to consume all given output, at the expense of
	making perhaps more than one system call.
	
	In addition, those methods can raise :exc:`BlockingIOError` if the
	underlying raw stream is in non-blocking mode and cannot take or give
	enough data; unlike their :class:`RawIOBase` counterparts, they will
	never return ``None``.
	
	Besides, the :meth:`read` method does not have a default
	implementation that defers to :meth:`readinto`.
	
	A typical :class:`BufferedIOBase` implementation should not inherit from a
	:class:`RawIOBase` implementation, but wrap one, like
	:class:`BufferedWriter` and :class:`BufferedReader` do.
	
	:class:`BufferedIOBase` provides or overrides these members in addition to
	those from :class:`IOBase`:
	
	"""
	
	
	def __init__(self, ):
		pass
	
	


class FileIO:


	"""
	:class:`FileIO` represents an OS-level file containing bytes data.
	It implements the :class:`RawIOBase` interface (and therefore the
	:class:`IOBase` interface, too).
	
	The *name* can be one of two things:
	
	* a string representing the path to the file which will be opened;
	* an integer representing the number of an existing OS-level file descriptor
	to which the resulting :class:`FileIO` object will give access.
	
	The *mode* can be ``'r'``, ``'w'`` or ``'a'`` for reading (default), writing,
	or appending.  The file will be created if it doesn't exist when opened for
	writing or appending; it will be truncated when opened for writing.  Add a
	``'+'`` to the mode to allow simultaneous reading and writing.
	
	The :meth:`read` (when called with a positive argument), :meth:`readinto`
	and :meth:`write` methods on this class will only make one system call.
	
	In addition to the attributes and methods from :class:`IOBase` and
	:class:`RawIOBase`, :class:`FileIO` provides the following data
	attributes and methods:
	
	"""
	
	
	def __init__(self, name,mode='r',closefd=True):
		pass
	
	


class BytesIO:


	"""
	A stream implementation using an in-memory bytes buffer.  It inherits
	:class:`BufferedIOBase`.
	
	The argument *initial_bytes* is an optional initial :class:`bytes`.
	
	:class:`BytesIO` provides or overrides these methods in addition to those
	from :class:`BufferedIOBase` and :class:`IOBase`:
	
	"""
	
	
	def __init__(self, initial_bytes):
		pass
	
	


class BufferedReader:


	"""
	A buffer providing higher-level access to a readable, sequential
	:class:`RawIOBase` object.  It inherits :class:`BufferedIOBase`.
	When reading data from this object, a larger amount of data may be
	requested from the underlying raw stream, and kept in an internal buffer.
	The buffered data can then be returned directly on subsequent reads.
	
	The constructor creates a :class:`BufferedReader` for the given readable
	*raw* stream and *buffer_size*.  If *buffer_size* is omitted,
	:data:`DEFAULT_BUFFER_SIZE` is used.
	
	:class:`BufferedReader` provides or overrides these methods in addition to
	those from :class:`BufferedIOBase` and :class:`IOBase`:
	
	"""
	
	
	def __init__(self, raw,buffer_size=DEFAULT_BUFFER_SIZE):
		pass
	
	


class BufferedWriter:


	"""
	A buffer providing higher-level access to a writeable, sequential
	:class:`RawIOBase` object.  It inherits :class:`BufferedIOBase`.
	When writing to this object, data is normally held into an internal
	buffer.  The buffer will be written out to the underlying :class:`RawIOBase`
	object under various conditions, including:
	
	* when the buffer gets too small for all pending data;
	* when :meth:`flush()` is called;
	* when a :meth:`seek()` is requested (for :class:`BufferedRandom` objects);
	* when the :class:`BufferedWriter` object is closed or destroyed.
	
	The constructor creates a :class:`BufferedWriter` for the given writeable
	*raw* stream.  If the *buffer_size* is not given, it defaults to
	:data:`DEFAULT_BUFFER_SIZE`.
	
	A third argument, *max_buffer_size*, is supported, but unused and deprecated.
	
	:class:`BufferedWriter` provides or overrides these methods in addition to
	those from :class:`BufferedIOBase` and :class:`IOBase`:
	
	"""
	
	
	def __init__(self, raw,buffer_size=DEFAULT_BUFFER_SIZE):
		pass
	
	


class BufferedRWPair:


	"""
	A buffered I/O object giving a combined, higher-level access to two
	sequential :class:`RawIOBase` objects: one readable, the other writeable.
	It is useful for pairs of unidirectional communication channels
	(pipes, for instance).  It inherits :class:`BufferedIOBase`.
	
	*reader* and *writer* are :class:`RawIOBase` objects that are readable and
	writeable respectively.  If the *buffer_size* is omitted it defaults to
	:data:`DEFAULT_BUFFER_SIZE`.
	
	A fourth argument, *max_buffer_size*, is supported, but unused and
	deprecated.
	
	:class:`BufferedRWPair` implements all of :class:`BufferedIOBase`\'s methods
	except for :meth:`~BufferedIOBase.detach`, which raises
	:exc:`UnsupportedOperation`.
	
	
	"""
	
	
	def __init__(self, reader,writer,buffer_size=DEFAULT_BUFFER_SIZE):
		pass
	
	


class BufferedRandom:


	"""
	A buffered interface to random access streams.  It inherits
	:class:`BufferedReader` and :class:`BufferedWriter`, and further supports
	:meth:`seek` and :meth:`tell` functionality.
	
	The constructor creates a reader and writer for a seekable raw stream, given
	in the first argument.  If the *buffer_size* is omitted it defaults to
	:data:`DEFAULT_BUFFER_SIZE`.
	
	A third argument, *max_buffer_size*, is supported, but unused and deprecated.
	
	:class:`BufferedRandom` is capable of anything :class:`BufferedReader` or
	:class:`BufferedWriter` can do.
	
	
	Text I/O
	--------
	
	"""
	
	
	def __init__(self, raw,buffer_size=DEFAULT_BUFFER_SIZE):
		pass
	
	


class TextIOBase:


	"""
	Base class for text streams.  This class provides an unicode character
	and line based interface to stream I/O.  There is no :meth:`readinto`
	method because Python's :class:`unicode` strings are immutable.
	It inherits :class:`IOBase`.  There is no public constructor.
	
	:class:`TextIOBase` provides or overrides these data attributes and
	methods in addition to those from :class:`IOBase`:
	
	"""
	
	
	def __init__(self, ):
		pass
	
	


class TextIOWrapper:


	"""
	A buffered text stream over a :class:`BufferedIOBase` binary stream.
	It inherits :class:`TextIOBase`.
	
	*encoding* gives the name of the encoding that the stream will be decoded or
	encoded with.  It defaults to :func:`locale.getpreferredencoding`.
	
	*errors* is an optional string that specifies how encoding and decoding
	errors are to be handled.  Pass ``'strict'`` to raise a :exc:`ValueError`
	exception if there is an encoding error (the default of ``None`` has the same
	effect), or pass ``'ignore'`` to ignore errors.  (Note that ignoring encoding
	errors can lead to data loss.)  ``'replace'`` causes a replacement marker
	(such as ``'?'``) to be inserted where there is malformed data.  When
	writing, ``'xmlcharrefreplace'`` (replace with the appropriate XML character
	reference) or ``'backslashreplace'`` (replace with backslashed escape
	sequences) can be used.  Any other error handling name that has been
	registered with :func:`codecs.register_error` is also valid.
	
	*newline* can be ``None``, ``''``, ``'\n'``, ``'\r'``, or ``'\r\n'``.  It
	controls the handling of line endings.  If it is ``None``, universal newlines
	is enabled.  With this enabled, on input, the lines endings ``'\n'``,
	``'\r'``, or ``'\r\n'`` are translated to ``'\n'`` before being returned to
	the caller.  Conversely, on output, ``'\n'`` is translated to the system
	default line separator, :data:`os.linesep`.  If *newline* is any other of its
	legal values, that newline becomes the newline when the file is read and it
	is returned untranslated.  On output, ``'\n'`` is converted to the *newline*.
	
	If *line_buffering* is ``True``, :meth:`flush` is implied when a call to
	write contains a newline character.
	
	:class:`TextIOWrapper` provides one attribute in addition to those of
	:class:`TextIOBase` and its parents:
	
	"""
	
	
	def __init__(self, buffer,encoding=None,errors=None,newline=None,line_buffering=False):
		pass
	
	


class StringIO:


	"""
	An in-memory stream for unicode text.  It inherits :class:`TextIOWrapper`.
	
	The initial value of the buffer (an empty unicode string by default) can
	be set by providing *initial_value*.  The *newline* argument works like
	that of :class:`TextIOWrapper`.  The default is to do no newline
	translation.
	
	:class:`StringIO` provides this method in addition to those from
	:class:`TextIOWrapper` and its parents:
	
	"""
	
	
	def __init__(self, initial_value=u'',newline=None):
		pass
	
	


