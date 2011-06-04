#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
""":platform: Unix
:synopsis: An interface to the Unix syslog library routines.


This module provides an interface to the Unix ``syslog`` library routines.
Refer to the Unix manual pages for a detailed description of the ``syslog``
facility.

This module wraps the system ``syslog`` family of routines.  A pure Python
library that can speak to a syslog server is available in the
:mod:`logging.handlers` module as :class:`SysLogHandler`.

The module defines the following functions:


"""
def syslog(priority,message):
	"""
	Send the string *message* to the system logger.  A trailing newline is added
	if necessary.  Each message is tagged with a priority composed of a
	*facility* and a *level*.  The optional *priority* argument, which defaults
	to :const:`LOG_INFO`, determines the message priority.  If the facility is
	not encoded in *priority* using logical-or (``LOG_INFO | LOG_USER``), the
	value given in the :func:`openlog` call is used.
	
	If :func:`openlog` has not been called prior to the call to :func:`syslog`,
	``openlog()`` will be called with no arguments.
	
	
	"""
	pass
	
def openlog(ident,logopt,facility):
	"""
	Logging options of subsequent :func:`syslog` calls can be set by calling
	:func:`openlog`.  :func:`syslog` will call :func:`openlog` with no arguments
	if the log is not currently open.
	
	The optional *ident* keyword argument is a string which is prepended to every
	message, and defaults to ``sys.argv[0]`` with leading path components
	stripped.  The optional *logopt* keyword argument (default is 0) is a bit
	field -- see below for possible values to combine.  The optional *facility*
	keyword argument (default is :const:`LOG_USER`) sets the default facility for
	messages which do not have a facility explicitly encoded.
	
	
	"""
	pass
	
def closelog():
	"""
	Reset the syslog module values and call the system library ``closelog()``.
	
	This causes the module to behave as it does when initially imported.  For
	example, :func:`openlog` will be called on the first :func:`syslog` call (if
	:func:`openlog` hasn't already been called), and *ident* and other
	:func:`openlog` parameters are reset to defaults.
	
	
	"""
	pass
	
