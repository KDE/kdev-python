#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
""":synopsis: Parse URLs into or assemble them from components.


"""
def urlparse(urlstring,scheme,allow_fragments):
	"""
	Parse a URL into six components, returning a 6-tuple.  This corresponds to the
	general structure of a URL: ``scheme://netloc/path;parameters?query#fragment``.
	Each tuple item is a string, possibly empty. The components are not broken up in
	smaller parts (for example, the network location is a single string), and %
	escapes are not expanded. The delimiters as shown above are not part of the
	result, except for a leading slash in the *path* component, which is retained if
	present.  For example:
	
	>>> from urlparse import urlparse
	>>> o = urlparse('http://www.cwi.nl:80/%7Eguido/Python.html')
	>>> o   # doctest: +NORMALIZE_WHITESPACE
	ParseResult(scheme='http', netloc='www.cwi.nl:80', path='/%7Eguido/Python.html',
	params='', query='', fragment='')
	>>> o.scheme
	'http'
	>>> o.port
	80
	>>> o.geturl()
	'http://www.cwi.nl:80/%7Eguido/Python.html'
	
	
	Following the syntax specifications in :rfc:`1808`, urlparse recognizes
	a netloc only if it is properly introduced by '//'.  Otherwise the
	input is presumed to be a relative URL and thus to start with
	a path component.
	
	>>> from urlparse import urlparse
	>>> urlparse('//www.cwi.nl:80/%7Eguido/Python.html')
	ParseResult(scheme='', netloc='www.cwi.nl:80', path='/%7Eguido/Python.html',
	params='', query='', fragment='')
	>>> urlparse('www.cwi.nl:80/%7Eguido/Python.html')
	ParseResult(scheme='', netloc='', path='www.cwi.nl:80/%7Eguido/Python.html',
	params='', query='', fragment='')
	>>> urlparse('help/Python.html')
	ParseResult(scheme='', netloc='', path='help/Python.html', params='',
	query='', fragment='')
	
	If the *scheme* argument is specified, it gives the default addressing
	scheme, to be used only if the URL does not specify one.  The default value for
	this argument is the empty string.
	
	If the *allow_fragments* argument is false, fragment identifiers are not
	allowed, even if the URL's addressing scheme normally does support them.  The
	default value for this argument is :const:`True`.
	
	The return value is actually an instance of a subclass of :class:`tuple`.  This
	class has the following additional read-only convenience attributes:
	
	+------------------+-------+--------------------------+----------------------+
	| Attribute        | Index | Value                    | Value if not present |
	+==================+=======+==========================+======================+
	| :attr:`scheme`   | 0     | URL scheme specifier     | empty string         |
	+------------------+-------+--------------------------+----------------------+
	| :attr:`netloc`   | 1     | Network location part    | empty string         |
	+------------------+-------+--------------------------+----------------------+
	| :attr:`path`     | 2     | Hierarchical path        | empty string         |
	+------------------+-------+--------------------------+----------------------+
	| :attr:`params`   | 3     | Parameters for last path | empty string         |
	|                  |       | element                  |                      |
	+------------------+-------+--------------------------+----------------------+
	| :attr:`query`    | 4     | Query component          | empty string         |
	+------------------+-------+--------------------------+----------------------+
	| :attr:`fragment` | 5     | Fragment identifier      | empty string         |
	+------------------+-------+--------------------------+----------------------+
	| :attr:`username` |       | User name                | :const:`None`        |
	+------------------+-------+--------------------------+----------------------+
	| :attr:`password` |       | Password                 | :const:`None`        |
	+------------------+-------+--------------------------+----------------------+
	| :attr:`hostname` |       | Host name (lower case)   | :const:`None`        |
	+------------------+-------+--------------------------+----------------------+
	| :attr:`port`     |       | Port number as integer,  | :const:`None`        |
	|                  |       | if present               |                      |
	+------------------+-------+--------------------------+----------------------+
	
	See section :ref:`urlparse-result-object` for more information on the result
	object.
	
	"""
	pass
	
def parse_qs(qs,keep_blank_values,strict_parsing):
	"""
	Parse a query string given as a string argument (data of type
	:mimetype:`application/x-www-form-urlencoded`).  Data are returned as a
	dictionary.  The dictionary keys are the unique query variable names and the
	values are lists of values for each name.
	
	The optional argument *keep_blank_values* is a flag indicating whether blank
	values in percent-encoded queries should be treated as blank strings.   A true value
	indicates that blanks should be retained as  blank strings.  The default false
	value indicates that blank values are to be ignored and treated as if they were
	not included.
	
	The optional argument *strict_parsing* is a flag indicating what to do with
	parsing errors.  If false (the default), errors are silently ignored.  If true,
	errors raise a :exc:`ValueError` exception.
	
	Use the :func:`urllib.urlencode` function to convert such dictionaries into
	query strings.
	
	"""
	pass
	
def parse_qsl(qs,keep_blank_values,strict_parsing):
	"""
	Parse a query string given as a string argument (data of type
	:mimetype:`application/x-www-form-urlencoded`).  Data are returned as a list of
	name, value pairs.
	
	The optional argument *keep_blank_values* is a flag indicating whether blank
	values in percent-encoded queries should be treated as blank strings.   A true value
	indicates that blanks should be retained as  blank strings.  The default false
	value indicates that blank values are to be ignored and treated as if they were
	not included.
	
	The optional argument *strict_parsing* is a flag indicating what to do with
	parsing errors.  If false (the default), errors are silently ignored.  If true,
	errors raise a :exc:`ValueError` exception.
	
	Use the :func:`urllib.urlencode` function to convert such lists of pairs into
	query strings.
	
	"""
	pass
	
def urlunparse(parts):
	"""
	Construct a URL from a tuple as returned by ``urlparse()``. The *parts* argument
	can be any six-item iterable. This may result in a slightly different, but
	equivalent URL, if the URL that was parsed originally had unnecessary delimiters
	(for example, a ? with an empty query; the RFC states that these are
	equivalent).
	
	
	"""
	pass
	
def urlsplit(urlstring,scheme,allow_fragments):
	"""
	This is similar to :func:`urlparse`, but does not split the params from the URL.
	This should generally be used instead of :func:`urlparse` if the more recent URL
	syntax allowing parameters to be applied to each segment of the *path* portion
	of the URL (see :rfc:`2396`) is wanted.  A separate function is needed to
	separate the path segments and parameters.  This function returns a 5-tuple:
	(addressing scheme, network location, path, query, fragment identifier).
	
	The return value is actually an instance of a subclass of :class:`tuple`.  This
	class has the following additional read-only convenience attributes:
	
	+------------------+-------+-------------------------+----------------------+
	| Attribute        | Index | Value                   | Value if not present |
	+==================+=======+=========================+======================+
	| :attr:`scheme`   | 0     | URL scheme specifier    | empty string         |
	+------------------+-------+-------------------------+----------------------+
	| :attr:`netloc`   | 1     | Network location part   | empty string         |
	+------------------+-------+-------------------------+----------------------+
	| :attr:`path`     | 2     | Hierarchical path       | empty string         |
	+------------------+-------+-------------------------+----------------------+
	| :attr:`query`    | 3     | Query component         | empty string         |
	+------------------+-------+-------------------------+----------------------+
	| :attr:`fragment` | 4     | Fragment identifier     | empty string         |
	+------------------+-------+-------------------------+----------------------+
	| :attr:`username` |       | User name               | :const:`None`        |
	+------------------+-------+-------------------------+----------------------+
	| :attr:`password` |       | Password                | :const:`None`        |
	+------------------+-------+-------------------------+----------------------+
	| :attr:`hostname` |       | Host name (lower case)  | :const:`None`        |
	+------------------+-------+-------------------------+----------------------+
	| :attr:`port`     |       | Port number as integer, | :const:`None`        |
	|                  |       | if present              |                      |
	+------------------+-------+-------------------------+----------------------+
	
	See section :ref:`urlparse-result-object` for more information on the result
	object.
	
	"""
	pass
	
def urlunsplit(parts):
	"""
	Combine the elements of a tuple as returned by :func:`urlsplit` into a complete
	URL as a string. The *parts* argument can be any five-item iterable. This may
	result in a slightly different, but equivalent URL, if the URL that was parsed
	originally had unnecessary delimiters (for example, a ? with an empty query; the
	RFC states that these are equivalent).
	
	"""
	pass
	
def urljoin(base,url,allow_fragments):
	"""
	Construct a full ("absolute") URL by combining a "base URL" (*base*) with
	another URL (*url*).  Informally, this uses components of the base URL, in
	particular the addressing scheme, the network location and (part of) the path,
	to provide missing components in the relative URL.  For example:
	
	>>> from urlparse import urljoin
	>>> urljoin('http://www.cwi.nl/%7Eguido/Python.html', 'FAQ.html')
	'http://www.cwi.nl/%7Eguido/FAQ.html'
	
	The *allow_fragments* argument has the same meaning and default as for
	:func:`urlparse`.
	
	"""
	pass
	
def urldefrag(url):
	"""
	If *url* contains a fragment identifier, returns a modified version of *url*
	with no fragment identifier, and the fragment identifier as a separate string.
	If there is no fragment identifier in *url*, returns *url* unmodified and an
	empty string.
	
	
	"""
	pass
	
class BaseResult:


	"""
	Base class for the concrete result classes.  This provides most of the attribute
	definitions.  It does not provide a :meth:`geturl` method.  It is derived from
	:class:`tuple`, but does not override the :meth:`__init__` or :meth:`__new__`
	methods.
	
	
	"""
	
	
	def __init__(self, ):
		pass
	
	


class ParseResult:


	"""
	Concrete class for :func:`urlparse` results.  The :meth:`__new__` method is
	overridden to support checking that the right number of arguments are passed.
	
	
	"""
	
	
	def __init__(self, scheme,netloc,path,params,query,fragment):
		pass
	
	


