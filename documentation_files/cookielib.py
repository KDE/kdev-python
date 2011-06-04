#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
""":synopsis: Classes for automatic handling of HTTP cookies.
"""
class CookieJar:


	"""
	*policy* is an object implementing the :class:`CookiePolicy` interface.
	
	The :class:`CookieJar` class stores HTTP cookies.  It extracts cookies from HTTP
	requests, and returns them in HTTP responses. :class:`CookieJar` instances
	automatically expire contained cookies when necessary.  Subclasses are also
	responsible for storing and retrieving cookies from a file or database.
	
	
	"""
	
	
	def __init__(self, ):
		pass
	
	def add_cookie_header(self, request):
		"""
		Add correct :mailheader:`Cookie` header to *request*.
		
		If policy allows (ie. the :attr:`rfc2965` and :attr:`hide_cookie2` attributes of
		the :class:`CookieJar`'s :class:`CookiePolicy` instance are true and false
		respectively), the :mailheader:`Cookie2` header is also added when appropriate.
		
		The *request* object (usually a :class:`urllib2.Request` instance) must support
		the methods :meth:`get_full_url`, :meth:`get_host`, :meth:`get_type`,
		:meth:`unverifiable`, :meth:`get_origin_req_host`, :meth:`has_header`,
		:meth:`get_header`, :meth:`header_items`, and :meth:`add_unredirected_header`,as
		documented by :mod:`urllib2`.
		
		
		"""
		pass
		
	def extract_cookies(self, response,request):
		"""
		Extract cookies from HTTP *response* and store them in the :class:`CookieJar`,
		where allowed by policy.
		
		The :class:`CookieJar` will look for allowable :mailheader:`Set-Cookie` and
		:mailheader:`Set-Cookie2` headers in the *response* argument, and store cookies
		as appropriate (subject to the :meth:`CookiePolicy.set_ok` method's approval).
		
		The *response* object (usually the result of a call to :meth:`urllib2.urlopen`,
		or similar) should support an :meth:`info` method, which returns an object with
		a :meth:`getallmatchingheaders` method (usually a :class:`mimetools.Message`
		instance).
		
		The *request* object (usually a :class:`urllib2.Request` instance) must support
		the methods :meth:`get_full_url`, :meth:`get_host`, :meth:`unverifiable`, and
		:meth:`get_origin_req_host`, as documented by :mod:`urllib2`.  The request is
		used to set default values for cookie-attributes as well as for checking that
		the cookie is allowed to be set.
		
		
		"""
		pass
		
	def set_policy(self, policy):
		"""
		Set the :class:`CookiePolicy` instance to be used.
		
		
		"""
		pass
		
	def make_cookies(self, response,request):
		"""
		Return sequence of :class:`Cookie` objects extracted from *response* object.
		
		See the documentation for :meth:`extract_cookies` for the interfaces required of
		the *response* and *request* arguments.
		
		
		"""
		pass
		
	def set_cookie_if_ok(self, cookie,request):
		"""
		Set a :class:`Cookie` if policy says it's OK to do so.
		
		
		"""
		pass
		
	def set_cookie(self, cookie):
		"""
		Set a :class:`Cookie`, without checking with policy to see whether or not it
		should be set.
		
		
		"""
		pass
		
	def clear(self, domain,path,name):
		"""
		Clear some cookies.
		
		If invoked without arguments, clear all cookies.  If given a single argument,
		only cookies belonging to that *domain* will be removed. If given two arguments,
		cookies belonging to the specified *domain* and URL *path* are removed.  If
		given three arguments, then the cookie with the specified *domain*, *path* and
		*name* is removed.
		
		Raises :exc:`KeyError` if no matching cookie exists.
		
		
		"""
		pass
		
	def clear_session_cookies(self, ):
		"""
		Discard all session cookies.
		
		Discards all contained cookies that have a true :attr:`discard` attribute
		(usually because they had either no ``max-age`` or ``expires`` cookie-attribute,
		or an explicit ``discard`` cookie-attribute).  For interactive browsers, the end
		of a session usually corresponds to closing the browser window.
		
		Note that the :meth:`save` method won't save session cookies anyway, unless you
		ask otherwise by passing a true *ignore_discard* argument.
		
		:class:`FileCookieJar` implements the following additional methods:
		
		
		"""
		pass
		
	


class FileCookieJar:


	"""
	*policy* is an object implementing the :class:`CookiePolicy` interface.  For the
	other arguments, see the documentation for the corresponding attributes.
	
	A :class:`CookieJar` which can load cookies from, and perhaps save cookies to, a
	file on disk.  Cookies are **NOT** loaded from the named file until either the
	:meth:`load` or :meth:`revert` method is called.  Subclasses of this class are
	documented in section :ref:`file-cookie-jar-classes`.
	
	
	"""
	
	
	def __init__(self, ):
		pass
	
	def save(self, filename=None,ignore_discard=False,ignore_expires=False):
		"""
		Save cookies to a file.
		
		This base class raises :exc:`NotImplementedError`.  Subclasses may leave this
		method unimplemented.
		
		*filename* is the name of file in which to save cookies.  If *filename* is not
		specified, :attr:`self.filename` is used (whose default is the value passed to
		the constructor, if any); if :attr:`self.filename` is :const:`None`,
		:exc:`ValueError` is raised.
		
		*ignore_discard*: save even cookies set to be discarded. *ignore_expires*: save
		even cookies that have expired
		
		The file is overwritten if it already exists, thus wiping all the cookies it
		contains.  Saved cookies can be restored later using the :meth:`load` or
		:meth:`revert` methods.
		
		
		"""
		pass
		
	def load(self, filename=None,ignore_discard=False,ignore_expires=False):
		"""
		Load cookies from a file.
		
		Old cookies are kept unless overwritten by newly loaded ones.
		
		Arguments are as for :meth:`save`.
		
		The named file must be in the format understood by the class, or
		:exc:`LoadError` will be raised.  Also, :exc:`IOError` may be raised, for
		example if the file does not exist.
		
		"""
		pass
		
	def revert(self, filename=None,ignore_discard=False,ignore_expires=False):
		"""
		Clear all cookies and reload cookies from a saved file.
		
		:meth:`revert` can raise the same exceptions as :meth:`load`. If there is a
		failure, the object's state will not be altered.
		
		:class:`FileCookieJar` instances have the following public attributes:
		
		
		"""
		pass
		
	


class CookiePolicy:


	"""
	This class is responsible for deciding whether each cookie should be accepted
	from / returned to the server.
	
	
	"""
	
	
	def __init__(self, ):
		pass
	
	def set_ok(self, cookie,request):
		"""
		Return boolean value indicating whether cookie should be accepted from server.
		
		*cookie* is a :class:`cookielib.Cookie` instance.  *request* is an object
		implementing the interface defined by the documentation for
		:meth:`CookieJar.extract_cookies`.
		
		
		"""
		pass
		
	def return_ok(self, cookie,request):
		"""
		Return boolean value indicating whether cookie should be returned to server.
		
		*cookie* is a :class:`cookielib.Cookie` instance.  *request* is an object
		implementing the interface defined by the documentation for
		:meth:`CookieJar.add_cookie_header`.
		
		
		"""
		pass
		
	def domain_return_ok(self, domain,request):
		"""
		Return false if cookies should not be returned, given cookie domain.
		
		This method is an optimization.  It removes the need for checking every cookie
		with a particular domain (which might involve reading many files).  Returning
		true from :meth:`domain_return_ok` and :meth:`path_return_ok` leaves all the
		work to :meth:`return_ok`.
		
		If :meth:`domain_return_ok` returns true for the cookie domain,
		:meth:`path_return_ok` is called for the cookie path.  Otherwise,
		:meth:`path_return_ok` and :meth:`return_ok` are never called for that cookie
		domain.  If :meth:`path_return_ok` returns true, :meth:`return_ok` is called
		with the :class:`Cookie` object itself for a full check.  Otherwise,
		:meth:`return_ok` is never called for that cookie path.
		
		Note that :meth:`domain_return_ok` is called for every *cookie* domain, not just
		for the *request* domain.  For example, the function might be called with both
		``".example.com"`` and ``"www.example.com"`` if the request domain is
		``"www.example.com"``.  The same goes for :meth:`path_return_ok`.
		
		The *request* argument is as documented for :meth:`return_ok`.
		
		
		"""
		pass
		
	def path_return_ok(self, path,request):
		"""
		Return false if cookies should not be returned, given cookie path.
		
		See the documentation for :meth:`domain_return_ok`.
		
		In addition to implementing the methods above, implementations of the
		:class:`CookiePolicy` interface must also supply the following attributes,
		indicating which protocols should be used, and how.  All of these attributes may
		be assigned to.
		
		
		"""
		pass
		
	


class DefaultCookiePolicy:


	"""
	Constructor arguments should be passed as keyword arguments only.
	*blocked_domains* is a sequence of domain names that we never accept cookies
	from, nor return cookies to. *allowed_domains* if not :const:`None`, this is a
	sequence of the only domains for which we accept and return cookies.  For all
	other arguments, see the documentation for :class:`CookiePolicy` and
	:class:`DefaultCookiePolicy` objects.
	
	:class:`DefaultCookiePolicy` implements the standard accept / reject rules for
	Netscape and RFC 2965 cookies.  By default, RFC 2109 cookies (ie. cookies
	received in a :mailheader:`Set-Cookie` header with a version cookie-attribute of
	1) are treated according to the RFC 2965 rules.  However, if RFC 2965 handling
	is turned off or :attr:`rfc2109_as_netscape` is True, RFC 2109 cookies are
	'downgraded' by the :class:`CookieJar` instance to Netscape cookies, by
	setting the :attr:`version` attribute of the :class:`Cookie` instance to 0.
	:class:`DefaultCookiePolicy` also provides some parameters to allow some
	fine-tuning of policy.
	
	
	"""
	
	
	def __init__(self, ):
		pass
	
	def blocked_domains(self, ):
		"""
		Return the sequence of blocked domains (as a tuple).
		
		
		"""
		pass
		
	def set_blocked_domains(self, blocked_domains):
		"""
		Set the sequence of blocked domains.
		
		
		"""
		pass
		
	def is_blocked(self, domain):
		"""
		Return whether *domain* is on the blacklist for setting or receiving cookies.
		
		
		"""
		pass
		
	def allowed_domains(self, ):
		"""
		Return :const:`None`, or the sequence of allowed domains (as a tuple).
		
		
		"""
		pass
		
	def set_allowed_domains(self, allowed_domains):
		"""
		Set the sequence of allowed domains, or :const:`None`.
		
		
		"""
		pass
		
	def is_not_allowed(self, domain):
		"""
		Return whether *domain* is not on the whitelist for setting or receiving
		cookies.
		
		:class:`DefaultCookiePolicy` instances have the following attributes, which are
		all initialised from the constructor arguments of the same name, and which may
		all be assigned to.
		
		
		"""
		pass
		
	


class Cookie:


	"""
	This class represents Netscape, RFC 2109 and RFC 2965 cookies.  It is not
	expected that users of :mod:`cookielib` construct their own :class:`Cookie`
	instances.  Instead, if necessary, call :meth:`make_cookies` on a
	:class:`CookieJar` instance.
	
	
	"""
	
	
	def __init__(self, ):
		pass
	
	def has_nonstandard_attr(self, name):
		"""
		Return true if cookie has the named cookie-attribute.
		
		
		"""
		pass
		
	def get_nonstandard_attr(self, name,default=None):
		"""
		If cookie has the named cookie-attribute, return its value. Otherwise, return
		*default*.
		
		
		"""
		pass
		
	def set_nonstandard_attr(self, name,value):
		"""
		Set the value of the named cookie-attribute.
		
		The :class:`Cookie` class also defines the following method:
		
		
		"""
		pass
		
	


class MozillaCookieJar:


	"""
	A :class:`FileCookieJar` that can load from and save cookies to disk in the
	Mozilla ``cookies.txt`` file format (which is also used by the Lynx and Netscape
	browsers).
	
	"""
	
	
	def __init__(self, ):
		pass
	
	


class LWPCookieJar:


	"""
	A :class:`FileCookieJar` that can load from and save cookies to disk in format
	compatible with the libwww-perl library's ``Set-Cookie3`` file format.  This is
	convenient if you want to store cookies in a human-readable file.
	
	
	.. ookiePolicy Objects
	--------------------
	
	Objects implementing the :class:`CookiePolicy` interface have the following
	methods:
	
	
	"""
	
	
	def __init__(self, ):
		pass
	
	


