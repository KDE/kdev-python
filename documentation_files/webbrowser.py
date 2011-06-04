#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
""":synopsis: Easy-to-use controller for Web browsers.
"""
def open(url,new=0,autoraise=True):
	"""
	Display *url* using the default browser. If *new* is 0, the *url* is opened
	in the same browser window if possible.  If *new* is 1, a new browser window
	is opened if possible.  If *new* is 2, a new browser page ("tab") is opened
	if possible.  If *autoraise* is ``True``, the window is raised if possible
	(note that under many window managers this will occur regardless of the
	setting of this variable).
	
	Note that on some platforms, trying to open a filename using this function,
	may work and start the operating system's associated program.  However, this
	is neither supported nor portable.
	
	"""
	pass
	
def open_new(url):
	"""
	Open *url* in a new window of the default browser, if possible, otherwise, open
	*url* in the only browser window.
	
	"""
	pass
	
def open_new_tab(url):
	"""
	Open *url* in a new page ("tab") of the default browser, if possible, otherwise
	equivalent to :func:`open_new`.
	
	"""
	pass
	
def get(name):
	"""
	Return a controller object for the browser type *name*.  If *name* is empty,
	return a controller for a default browser appropriate to the caller's
	environment.
	
	
	"""
	pass
	
def register(name,constructor,instance):
	"""
	Register the browser type *name*.  Once a browser type is registered, the
	:func:`get` function can return a controller for that browser type.  If
	*instance* is not provided, or is ``None``, *constructor* will be called without
	parameters to create an instance when needed.  If *instance* is provided,
	*constructor* will never be called, and may be ``None``.
	
	This entry point is only useful if you plan to either set the :envvar:`BROWSER`
	variable or call :func:`get` with a nonempty argument matching the name of a
	handler you declare.
	
	A number of browser types are predefined.  This table gives the type names that
	may be passed to the :func:`get` function and the corresponding instantiations
	for the controller classes, all defined in this module.
	
	+-----------------------+-----------------------------------------+-------+
	| Type Name             | Class Name                              | Notes |
	+=======================+=========================================+=======+
	| ``'mozilla'``         | :class:`Mozilla('mozilla')`             |       |
	+-----------------------+-----------------------------------------+-------+
	| ``'firefox'``         | :class:`Mozilla('mozilla')`             |       |
	+-----------------------+-----------------------------------------+-------+
	| ``'netscape'``        | :class:`Mozilla('netscape')`            |       |
	+-----------------------+-----------------------------------------+-------+
	| ``'galeon'``          | :class:`Galeon('galeon')`               |       |
	+-----------------------+-----------------------------------------+-------+
	| ``'epiphany'``        | :class:`Galeon('epiphany')`             |       |
	+-----------------------+-----------------------------------------+-------+
	| ``'skipstone'``       | :class:`BackgroundBrowser('skipstone')` |       |
	+-----------------------+-----------------------------------------+-------+
	| ``'kfmclient'``       | :class:`Konqueror()`                    | \(1)  |
	+-----------------------+-----------------------------------------+-------+
	| ``'konqueror'``       | :class:`Konqueror()`                    | \(1)  |
	+-----------------------+-----------------------------------------+-------+
	| ``'kfm'``             | :class:`Konqueror()`                    | \(1)  |
	+-----------------------+-----------------------------------------+-------+
	| ``'mosaic'``          | :class:`BackgroundBrowser('mosaic')`    |       |
	+-----------------------+-----------------------------------------+-------+
	| ``'opera'``           | :class:`Opera()`                        |       |
	+-----------------------+-----------------------------------------+-------+
	| ``'grail'``           | :class:`Grail()`                        |       |
	+-----------------------+-----------------------------------------+-------+
	| ``'links'``           | :class:`GenericBrowser('links')`        |       |
	+-----------------------+-----------------------------------------+-------+
	| ``'elinks'``          | :class:`Elinks('elinks')`               |       |
	+-----------------------+-----------------------------------------+-------+
	| ``'lynx'``            | :class:`GenericBrowser('lynx')`         |       |
	+-----------------------+-----------------------------------------+-------+
	| ``'w3m'``             | :class:`GenericBrowser('w3m')`          |       |
	+-----------------------+-----------------------------------------+-------+
	| ``'windows-default'`` | :class:`WindowsDefault`                 | \(2)  |
	+-----------------------+-----------------------------------------+-------+
	| ``'internet-config'`` | :class:`InternetConfig`                 | \(3)  |
	+-----------------------+-----------------------------------------+-------+
	| ``'macosx'``          | :class:`MacOSX('default')`              | \(4)  |
	+-----------------------+-----------------------------------------+-------+
	
	Notes:
	
	(1)
	"Konqueror" is the file manager for the KDE desktop environment for Unix, and
	only makes sense to use if KDE is running.  Some way of reliably detecting KDE
	would be nice; the :envvar:`KDEDIR` variable is not sufficient.  Note also that
	the name "kfm" is used even when using the :program:`konqueror` command with KDE
	2 --- the implementation selects the best strategy for running Konqueror.
	
	(2)
	Only on Windows platforms.
	
	(3)
	Only on Mac OS platforms; requires the standard MacPython :mod:`ic` module.
	
	(4)
	Only on Mac OS X platform.
	
	Here are some simple examples::
	
	url = 'http://www.python.org/'
	
	# Open URL in a new tab, if a browser window is already open.
	webbrowser.open_new_tab(url + 'doc/')
	
	# Open URL in new window, raising the window if possible.
	webbrowser.open_new(url)
	
	
	.. rowser Controller Objects
	--------------------------
	
	Browser controllers provide these methods which parallel three of the
	module-level convenience functions:
	
	
	"""
	pass
	
