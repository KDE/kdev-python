#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
""":synopsis: Open an arbitrary network resource by URL (requires sockets).

"""
"""
The public functions :func:`urlopen` and :func:`urlretrieve` create an instance
of the :class:`FancyURLopener` class and use it to perform their requested
actions.  To override this functionality, programmers can create a subclass of
:class:`URLopener` or :class:`FancyURLopener`, then assign an instance of that
class to the ``urllib._urlopener`` variable before calling the desired function.
For example, applications may want to specify a different
:mailheader:`User-Agent` header than :class:`URLopener` defines.  This can be
accomplished with the following code::

import urllib

class AppURLopener(urllib.FancyURLopener):
version = "App/1.7"

urllib._urlopener = AppURLopener()


"""
_urlopener = None
def urlopen(url,data,proxies):
	"""
	Open a network object denoted by a URL for reading.  If the URL does not have a
	scheme identifier, or if it has :file:`file:` as its scheme identifier, this
	opens a local file (without universal newlines); otherwise it opens a socket to
	a server somewhere on the network.  If the connection cannot be made the
	:exc:`IOError` exception is raised.  If all went well, a file-like object is
	returned.  This supports the following methods: :meth:`read`, :meth:`readline`,
	:meth:`readlines`, :meth:`fileno`, :meth:`close`, :meth:`info`, :meth:`getcode` and
	:meth:`geturl`.  It also has proper support for the :term:`iterator` protocol. One
	caveat: the :meth:`read` method, if the size argument is omitted or negative,
	may not read until the end of the data stream; there is no good way to determine
	that the entire stream from a socket has been read in the general case.
	
	Except for the :meth:`info`, :meth:`getcode` and :meth:`geturl` methods,
	these methods have the same interface as for file objects --- see section
	:ref:`bltin-file-objects` in this manual.  (It is not a built-in file object,
	however, so it can't be used at those few places where a true built-in file
	object is required.)
	
	"""
	pass
	
def urlretrieve(url,filename,reporthook,data):
	"""
	Copy a network object denoted by a URL to a local file, if necessary. If the URL
	points to a local file, or a valid cached copy of the object exists, the object
	is not copied.  Return a tuple ``(filename, headers)`` where *filename* is the
	local file name under which the object can be found, and *headers* is whatever
	the :meth:`info` method of the object returned by :func:`urlopen` returned (for
	a remote object, possibly cached). Exceptions are the same as for
	:func:`urlopen`.
	
	The second argument, if present, specifies the file location to copy to (if
	absent, the location will be a tempfile with a generated name). The third
	argument, if present, is a hook function that will be called once on
	establishment of the network connection and once after each block read
	thereafter.  The hook will be passed three arguments; a count of blocks
	transferred so far, a block size in bytes, and the total size of the file.  The
	third argument may be ``-1`` on older FTP servers which do not return a file
	size in response to a retrieval request.
	
	If the *url* uses the :file:`http:` scheme identifier, the optional *data*
	argument may be given to specify a ``POST`` request (normally the request type
	is ``GET``).  The *data* argument must in standard
	:mimetype:`application/x-www-form-urlencoded` format; see the :func:`urlencode`
	function below.
	
	"""
	pass
	
def urlcleanup():
	"""
	Clear the cache that may have been built up by previous calls to
	:func:`urlretrieve`.
	
	
	Utility functions
	-----------------
	
	"""
	pass
	
def quote(string,safe):
	"""
	Replace special characters in *string* using the ``%xx`` escape. Letters,
	digits, and the characters ``'_.-'`` are never quoted. By default, this
	function is intended for quoting the path section of the URL.The optional
	*safe* parameter specifies additional characters that should not be quoted
	--- its default value is ``'/'``.
	
	Example: ``quote('/~connolly/')`` yields ``'/%7econnolly/'``.
	
	
	"""
	pass
	
def quote_plus(string,safe):
	"""
	Like :func:`quote`, but also replaces spaces by plus signs, as required for
	quoting HTML form values when building up a query string to go into a URL.
	Plus signs in the original string are escaped unless they are included in
	*safe*.  It also does not have *safe* default to ``'/'``.
	
	
	"""
	pass
	
def unquote(string):
	"""
	Replace ``%xx`` escapes by their single-character equivalent.
	
	Example: ``unquote('/%7Econnolly/')`` yields ``'/~connolly/'``.
	
	
	"""
	pass
	
def unquote_plus(string):
	"""
	Like :func:`unquote`, but also replaces plus signs by spaces, as required for
	unquoting HTML form values.
	
	
	"""
	pass
	
def urlencode(query,doseq):
	"""
	Convert a mapping object or a sequence of two-element tuples to a
	"percent-encoded" string, suitable to pass to :func:`urlopen` above as the
	optional *data* argument.  This is useful to pass a dictionary of form
	fields to a ``POST`` request.  The resulting string is a series of
	``key=value`` pairs separated by ``'&'`` characters, where both *key* and
	*value* are quoted using :func:`quote_plus` above.  When a sequence of
	two-element tuples is used as the *query* argument, the first element of
	each tuple is a key and the second is a value. The value element in itself
	can be a sequence and in that case, if the optional parameter *doseq* is
	evaluates to *True*, individual ``key=value`` pairs separated by ``'&'`` are
	generated for each element of the value sequence for the key.  The order of
	parameters in the encoded string will match the order of parameter tuples in
	the sequence. The :mod:`urlparse` module provides the functions
	:func:`parse_qs` and :func:`parse_qsl` which are used to parse query strings
	into Python data structures.
	
	
	"""
	pass
	
def pathname2url(path):
	"""
	Convert the pathname *path* from the local syntax for a path to the form used in
	the path component of a URL.  This does not produce a complete URL.  The return
	value will already be quoted using the :func:`quote` function.
	
	
	"""
	pass
	
def url2pathname(path):
	"""
	Convert the path component *path* from an percent-encoded URL to the local syntax for a
	path.  This does not accept a complete URL.  This function uses :func:`unquote`
	to decode *path*.
	
	
	"""
	pass
	
def getproxies():
	"""
	This helper function returns a dictionary of scheme to proxy server URL
	mappings. It scans the environment for variables named ``<scheme>_proxy``
	for all operating systems first, and when it cannot find it, looks for proxy
	information from Mac OSX System Configuration for Mac OS X and Windows
	Systems Registry for Windows.
	
	
	URL Opener objects
	------------------
	
	"""
	pass
	
class URLopener:


	"""
	Base class for opening and reading URLs.  Unless you need to support opening
	objects using schemes other than :file:`http:`, :file:`ftp:`, or :file:`file:`,
	you probably want to use :class:`FancyURLopener`.
	
	By default, the :class:`URLopener` class sends a :mailheader:`User-Agent` header
	of ``urllib/VVV``, where *VVV* is the :mod:`urllib` version number.
	Applications can define their own :mailheader:`User-Agent` header by subclassing
	:class:`URLopener` or :class:`FancyURLopener` and setting the class attribute
	:attr:`version` to an appropriate string value in the subclass definition.
	
	The optional *proxies* parameter should be a dictionary mapping scheme names to
	proxy URLs, where an empty dictionary turns proxies off completely.  Its default
	value is ``None``, in which case environmental proxy settings will be used if
	present, as discussed in the definition of :func:`urlopen`, above.
	
	Additional keyword parameters, collected in *x509*, may be used for
	authentication of the client when using the :file:`https:` scheme.  The keywords
	*key_file* and *cert_file* are supported to provide an  SSL key and certificate;
	both are needed to support client authentication.
	
	:class:`URLopener` objects will raise an :exc:`IOError` exception if the server
	returns an error code.
	
	"""
	
	
	def __init__(self, ):
		pass
	
	def open(self, fullurl,data):
		"""
		Open *fullurl* using the appropriate protocol.  This method sets up cache and
		proxy information, then calls the appropriate open method with its input
		arguments.  If the scheme is not recognized, :meth:`open_unknown` is called.
		The *data* argument has the same meaning as the *data* argument of
		:func:`urlopen`.
		
		
		"""
		pass
		
	def open_unknown(self, fullurl,data):
		"""
		Overridable interface to open unknown URL types.
		
		
		"""
		pass
		
	def retrieve(self, url,filename,reporthook,data):
		"""
		Retrieves the contents of *url* and places it in *filename*.  The return value
		is a tuple consisting of a local filename and either a
		:class:`mimetools.Message` object containing the response headers (for remote
		URLs) or ``None`` (for local URLs).  The caller must then open and read the
		contents of *filename*.  If *filename* is not given and the URL refers to a
		local file, the input filename is returned.  If the URL is non-local and
		*filename* is not given, the filename is the output of :func:`tempfile.mktemp`
		with a suffix that matches the suffix of the last path component of the input
		URL.  If *reporthook* is given, it must be a function accepting three numeric
		parameters.  It will be called after each chunk of data is read from the
		network.  *reporthook* is ignored for local URLs.
		
		If the *url* uses the :file:`http:` scheme identifier, the optional *data*
		argument may be given to specify a ``POST`` request (normally the request type
		is ``GET``).  The *data* argument must in standard
		:mimetype:`application/x-www-form-urlencoded` format; see the :func:`urlencode`
		function below.
		
		
		"""
		pass
		
	


class FancyURLopener:


	"""
	:class:`FancyURLopener` subclasses :class:`URLopener` providing default handling
	for the following HTTP response codes: 301, 302, 303, 307 and 401.  For the 30x
	response codes listed above, the :mailheader:`Location` header is used to fetch
	the actual URL.  For 401 response codes (authentication required), basic HTTP
	authentication is performed.  For the 30x response codes, recursion is bounded
	by the value of the *maxtries* attribute, which defaults to 10.
	
	For all other response codes, the method :meth:`http_error_default` is called
	which you can override in subclasses to handle the error appropriately.
	
	"""
	
	
	def __init__(self, ):
		pass
	
	def prompt_user_passwd(self, host,realm):
		"""
		Return information needed to authenticate the user at the given host in the
		specified security realm.  The return value should be a tuple, ``(user,
		password)``, which can be used for basic authentication.
		
		The implementation prompts for this information on the terminal; an application
		should override this method to use an appropriate interaction model in the local
		environment.
		
		"""
		pass
		
	


