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
	
	
	def __init__(self, policy=None):
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
	
	
	def __init__(self, filename,delayload=None,policy=None):
		pass
	
	


class CookiePolicy:


	"""
	This class is responsible for deciding whether each cookie should be accepted
	from / returned to the server.
	
	
	"""
	
	
	def __init__(self, ):
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
	
	
	def __init__(self, blocked_domains=None,allowed_domains=None,netscape=True,rfc2965=False,rfc2109_as_netscape=None,hide_cookie2=False,strict_domain=False,strict_rfc2965_unverifiable=True,strict_ns_unverifiable=False,strict_ns_domain=DefaultCookiePolicy):
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
	
	


class MozillaCookieJar:


	"""
	A :class:`FileCookieJar` that can load from and save cookies to disk in the
	Mozilla ``cookies.txt`` file format (which is also used by the Lynx and Netscape
	browsers).
	
	"""
	
	
	def __init__(self, filename,delayload=None,policy=None):
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
	
	
	def __init__(self, filename,delayload=None,policy=None):
		pass
	
	


