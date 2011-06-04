#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
""":synopsis: Next generation URL opening library.
"""
def urlopen(url,data,timeout):
	"""
	Open the URL *url*, which can be either a string or a :class:`Request` object.
	
	"""
	pass
	
def install_opener(opener):
	"""
	Install an :class:`OpenerDirector` instance as the default global opener.
	Installing an opener is only necessary if you want urlopen to use that opener;
	otherwise, simply call :meth:`OpenerDirector.open` instead of :func:`urlopen`.
	The code does not check for a real :class:`OpenerDirector`, and any class with
	the appropriate interface will work.
	
	
	"""
	pass
	
def build_opener(handler,more):
	"""
	Return an :class:`OpenerDirector` instance, which chains the handlers in the
	order given. *handler*\s can be either instances of :class:`BaseHandler`, or
	subclasses of :class:`BaseHandler` (in which case it must be possible to call
	the constructor without any parameters).  Instances of the following classes
	will be in front of the *handler*\s, unless the *handler*\s contain them,
	instances of them or subclasses of them: :class:`ProxyHandler`,
	:class:`UnknownHandler`, :class:`HTTPHandler`, :class:`HTTPDefaultErrorHandler`,
	:class:`HTTPRedirectHandler`, :class:`FTPHandler`, :class:`FileHandler`,
	:class:`HTTPErrorProcessor`.
	
	If the Python installation has SSL support (i.e., if the :mod:`ssl` module can be imported),
	:class:`HTTPSHandler` will also be added.
	
	Beginning in Python 2.3, a :class:`BaseHandler` subclass may also change its
	:attr:`handler_order` member variable to modify its position in the handlers
	list.
	
	The following exceptions are raised as appropriate:
	
	
	"""
	pass
	
class Request:


	"""
	This class is an abstraction of a URL request.
	
	*url* should be a string containing a valid URL.
	
	*data* may be a string specifying additional data to send to the server, or
	``None`` if no such data is needed.  Currently HTTP requests are the only ones
	that use *data*; the HTTP request will be a POST instead of a GET when the
	*data* parameter is provided.  *data* should be a buffer in the standard
	:mimetype:`application/x-www-form-urlencoded` format.  The
	:func:`urllib.urlencode` function takes a mapping or sequence of 2-tuples and
	returns a string in this format.
	
	*headers* should be a dictionary, and will be treated as if :meth:`add_header`
	was called with each key and value as arguments.  This is often used to "spoof"
	the ``User-Agent`` header, which is used by a browser to identify itself --
	some HTTP servers only allow requests coming from common browsers as opposed
	to scripts.  For example, Mozilla Firefox may identify itself as ``"Mozilla/5.0
	(X11; U; Linux i686) Gecko/20071127 Firefox/2.0.0.11"``, while :mod:`urllib2`'s
	default user agent string is ``"Python-urllib/2.6"`` (on Python 2.6).
	
	The final two arguments are only of interest for correct handling of third-party
	HTTP cookies:
	
	*origin_req_host* should be the request-host of the origin transaction, as
	defined by :rfc:`2965`.  It defaults to ``cookielib.request_host(self)``.  This
	is the host name or IP address of the original request that was initiated by the
	user.  For example, if the request is for an image in an HTML document, this
	should be the request-host of the request for the page containing the image.
	
	*unverifiable* should indicate whether the request is unverifiable, as defined
	by RFC 2965.  It defaults to False.  An unverifiable request is one whose URL
	the user did not have the option to approve.  For example, if the request is for
	an image in an HTML document, and the user had no option to approve the
	automatic fetching of the image, this should be true.
	
	
	"""
	
	
	def __init__(self, url,data,headers,origin_req_host,unverifiable):
		pass
	
	


class OpenerDirector:


	"""
	The :class:`OpenerDirector` class opens URLs via :class:`BaseHandler`\ s chained
	together. It manages the chaining of handlers, and recovery from errors.
	
	
	"""
	
	
	def __init__(self, ):
		pass
	
	


class BaseHandler:


	"""
	This is the base class for all registered handlers --- and handles only the
	simple mechanics of registration.
	
	
	"""
	
	
	def __init__(self, ):
		pass
	
	


class HTTPDefaultErrorHandler:


	"""
	A class which defines a default handler for HTTP error responses; all responses
	are turned into :exc:`HTTPError` exceptions.
	
	
	"""
	
	
	def __init__(self, ):
		pass
	
	


class HTTPRedirectHandler:


	"""
	A class to handle redirections.
	
	
	"""
	
	
	def __init__(self, ):
		pass
	
	


class HTTPCookieProcessor:


	"""
	A class to handle HTTP Cookies.
	
	
	"""
	
	
	def __init__(self, cookiejar):
		pass
	
	


class ProxyHandler:


	"""
	Cause requests to go through a proxy. If *proxies* is given, it must be a
	dictionary mapping protocol names to URLs of proxies. The default is to read
	the list of proxies from the environment variables
	:envvar:`<protocol>_proxy`.  If no proxy environment variables are set, in a
	Windows environment, proxy settings are obtained from the registry's
	Internet Settings section and in a Mac OS X  environment, proxy information
	is retrieved from the OS X System Configuration Framework.
	
	To disable autodetected proxy pass an empty dictionary.
	
	
	"""
	
	
	def __init__(self, proxies):
		pass
	
	


class HTTPPasswordMgr:


	"""
	Keep a database of  ``(realm, uri) -> (user, password)`` mappings.
	
	
	"""
	
	
	def __init__(self, ):
		pass
	
	


class HTTPPasswordMgrWithDefaultRealm:


	"""
	Keep a database of  ``(realm, uri) -> (user, password)`` mappings. A realm of
	``None`` is considered a catch-all realm, which is searched if no other realm
	fits.
	
	
	"""
	
	
	def __init__(self, ):
		pass
	
	


class AbstractBasicAuthHandler:


	"""
	This is a mixin class that helps with HTTP authentication, both to the remote
	host and to a proxy. *password_mgr*, if given, should be something that is
	compatible with :class:`HTTPPasswordMgr`; refer to section
	:ref:`http-password-mgr` for information on the interface that must be
	supported.
	
	
	"""
	
	
	def __init__(self, password_mgr):
		pass
	
	


class HTTPBasicAuthHandler:


	"""
	Handle authentication with the remote host. *password_mgr*, if given, should be
	something that is compatible with :class:`HTTPPasswordMgr`; refer to section
	:ref:`http-password-mgr` for information on the interface that must be
	supported.
	
	
	"""
	
	
	def __init__(self, password_mgr):
		pass
	
	


class ProxyBasicAuthHandler:


	"""
	Handle authentication with the proxy. *password_mgr*, if given, should be
	something that is compatible with :class:`HTTPPasswordMgr`; refer to section
	:ref:`http-password-mgr` for information on the interface that must be
	supported.
	
	
	"""
	
	
	def __init__(self, password_mgr):
		pass
	
	


class AbstractDigestAuthHandler:


	"""
	This is a mixin class that helps with HTTP authentication, both to the remote
	host and to a proxy. *password_mgr*, if given, should be something that is
	compatible with :class:`HTTPPasswordMgr`; refer to section
	:ref:`http-password-mgr` for information on the interface that must be
	supported.
	
	
	"""
	
	
	def __init__(self, password_mgr):
		pass
	
	


class HTTPDigestAuthHandler:


	"""
	Handle authentication with the remote host. *password_mgr*, if given, should be
	something that is compatible with :class:`HTTPPasswordMgr`; refer to section
	:ref:`http-password-mgr` for information on the interface that must be
	supported.
	
	
	"""
	
	
	def __init__(self, password_mgr):
		pass
	
	


class ProxyDigestAuthHandler:


	"""
	Handle authentication with the proxy. *password_mgr*, if given, should be
	something that is compatible with :class:`HTTPPasswordMgr`; refer to section
	:ref:`http-password-mgr` for information on the interface that must be
	supported.
	
	
	"""
	
	
	def __init__(self, password_mgr):
		pass
	
	


class HTTPHandler:


	"""
	A class to handle opening of HTTP URLs.
	
	
	"""
	
	
	def __init__(self, ):
		pass
	
	


class HTTPSHandler:


	"""
	A class to handle opening of HTTPS URLs.
	
	
	"""
	
	
	def __init__(self, ):
		pass
	
	


class FileHandler:


	"""
	Open local files.
	
	
	"""
	
	
	def __init__(self, ):
		pass
	
	


class FTPHandler:


	"""
	Open FTP URLs.
	
	
	"""
	
	
	def __init__(self, ):
		pass
	
	


class CacheFTPHandler:


	"""
	Open FTP URLs, keeping a cache of open FTP connections to minimize delays.
	
	
	"""
	
	
	def __init__(self, ):
		pass
	
	


class UnknownHandler:


	"""
	A catch-all class to handle unknown URLs.
	
	
	.. equest Objects
	---------------
	
	The following methods describe all of :class:`Request`'s public interface, and
	so all must be overridden in subclasses.
	
	
	"""
	
	
	def __init__(self, ):
		pass
	
	


