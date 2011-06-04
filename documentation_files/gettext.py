#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
""":synopsis: Multilingual internationalization services.
"""
def bindtextdomain(domain,localedir):
	"""
	Bind the *domain* to the locale directory *localedir*.  More concretely,
	:mod:`gettext` will look for binary :file:`.mo` files for the given domain using
	the path (on Unix): :file:`localedir/language/LC_MESSAGES/domain.mo`, where
	*languages* is searched for in the environment variables :envvar:`LANGUAGE`,
	:envvar:`LC_ALL`, :envvar:`LC_MESSAGES`, and :envvar:`LANG` respectively.
	
	If *localedir* is omitted or ``None``, then the current binding for *domain* is
	returned. [#]_
	
	
	"""
	pass
	
def bind_textdomain_codeset(domain,codeset):
	"""
	Bind the *domain* to *codeset*, changing the encoding of strings returned by the
	:func:`gettext` family of functions. If *codeset* is omitted, then the current
	binding is returned.
	
	"""
	pass
	
def textdomain(domain):
	"""
	Change or query the current global domain.  If *domain* is ``None``, then the
	current global domain is returned, otherwise the global domain is set to
	*domain*, which is returned.
	
	
	"""
	pass
	
def gettext(message):
	"""
	Return the localized translation of *message*, based on the current global
	domain, language, and locale directory.  This function is usually aliased as
	:func:`_` in the local namespace (see examples below).
	
	
	"""
	pass
	
def lgettext(message):
	"""
	Equivalent to :func:`gettext`, but the translation is returned in the preferred
	system encoding, if no other encoding was explicitly set with
	:func:`bind_textdomain_codeset`.
	
	"""
	pass
	
def dgettext(domain,message):
	"""
	Like :func:`gettext`, but look the message up in the specified *domain*.
	
	
	"""
	pass
	
def ldgettext(domain,message):
	"""
	Equivalent to :func:`dgettext`, but the translation is returned in the preferred
	system encoding, if no other encoding was explicitly set with
	:func:`bind_textdomain_codeset`.
	
	"""
	pass
	
def ngettext(singular,plural,n):
	"""
	Like :func:`gettext`, but consider plural forms. If a translation is found,
	apply the plural formula to *n*, and return the resulting message (some
	languages have more than two plural forms). If no translation is found, return
	*singular* if *n* is 1; return *plural* otherwise.
	
	The Plural formula is taken from the catalog header. It is a C or Python
	expression that has a free variable *n*; the expression evaluates to the index
	of the plural in the catalog. See the GNU gettext documentation for the precise
	syntax to be used in :file:`.po` files and the formulas for a variety of
	languages.
	
	"""
	pass
	
def lngettext(singular,plural,n):
	"""
	Equivalent to :func:`ngettext`, but the translation is returned in the preferred
	system encoding, if no other encoding was explicitly set with
	:func:`bind_textdomain_codeset`.
	
	"""
	pass
	
def dngettext(domain,singular,plural,n):
	"""
	Like :func:`ngettext`, but look the message up in the specified *domain*.
	
	"""
	pass
	
def ldngettext(domain,singular,plural,n):
	"""
	Equivalent to :func:`dngettext`, but the translation is returned in the
	preferred system encoding, if no other encoding was explicitly set with
	:func:`bind_textdomain_codeset`.
	
	"""
	pass
	
def find(domain,localedir,languages,all):
	"""
	This function implements the standard :file:`.mo` file search algorithm.  It
	takes a *domain*, identical to what :func:`textdomain` takes.  Optional
	*localedir* is as in :func:`bindtextdomain`  Optional *languages* is a list of
	strings, where each string is a language code.
	
	If *localedir* is not given, then the default system locale directory is used.
	[#]_  If *languages* is not given, then the following environment variables are
	searched: :envvar:`LANGUAGE`, :envvar:`LC_ALL`, :envvar:`LC_MESSAGES`, and
	:envvar:`LANG`.  The first one returning a non-empty value is used for the
	*languages* variable. The environment variables should contain a colon separated
	list of languages, which will be split on the colon to produce the expected list
	of language code strings.
	
	:func:`find` then expands and normalizes the languages, and then iterates
	through them, searching for an existing file built of these components:
	
	:file:`localedir/language/LC_MESSAGES/domain.mo`
	
	The first such file name that exists is returned by :func:`find`. If no such
	file is found, then ``None`` is returned. If *all* is given, it returns a list
	of all file names, in the order in which they appear in the languages list or
	the environment variables.
	
	
	"""
	pass
	
def translation(domain,localedir,languages,_class_,fallback,codeset):
	"""
	Return a :class:`Translations` instance based on the *domain*, *localedir*, and
	*languages*, which are first passed to :func:`find` to get a list of the
	associated :file:`.mo` file paths.  Instances with identical :file:`.mo` file
	names are cached.  The actual class instantiated is either *class_* if provided,
	otherwise :class:`GNUTranslations`.  The class's constructor must take a single
	file object argument. If provided, *codeset* will change the charset used to
	encode translated strings.
	
	If multiple files are found, later files are used as fallbacks for earlier ones.
	To allow setting the fallback, :func:`copy.copy` is used to clone each
	translation object from the cache; the actual instance data is still shared with
	the cache.
	
	If no :file:`.mo` file is found, this function raises :exc:`IOError` if
	*fallback* is false (which is the default), and returns a
	:class:`NullTranslations` instance if *fallback* is true.
	
	"""
	pass
	
def install(domain,localedir,unicode,codeset,names):
	"""
	This installs the function :func:`_` in Python's builtins namespace, based on
	*domain*, *localedir*, and *codeset* which are passed to the function
	:func:`translation`.  The *unicode* flag is passed to the resulting translation
	object's :meth:`~NullTranslations.install` method.
	
	For the *names* parameter, please see the description of the translation
	object's :meth:`~NullTranslations.install` method.
	
	As seen below, you usually mark the strings in your application that are
	candidates for translation, by wrapping them in a call to the :func:`_`
	function, like this::
	
	print _('This string will be translated.')
	
	For convenience, you want the :func:`_` function to be installed in Python's
	builtins namespace, so it is easily accessible in all modules of your
	application.
	
	"""
	pass
	
class NullTranslations:


	"""
	Takes an optional file object *fp*, which is ignored by the base class.
	Initializes "protected" instance variables *_info* and *_charset* which are set
	by derived classes, as well as *_fallback*, which is set through
	:meth:`add_fallback`.  It then calls ``self._parse(fp)`` if *fp* is not
	``None``.
	
	
	"""
	
	
	def __init__(self, fp):
		pass
	
	


