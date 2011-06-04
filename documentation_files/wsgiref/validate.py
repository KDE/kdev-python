#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
""":synopsis: WSGI conformance checker.


When creating new WSGI application objects, frameworks, servers, or middleware,
it can be useful to validate the new code's conformance using
:mod:`wsgiref.validate`.  This module provides a function that creates WSGI
application objects that validate communications between a WSGI server or
gateway and a WSGI application object, to check both sides for protocol
conformance.

Note that this utility does not guarantee complete :pep:`333` compliance; an
absence of errors from this module does not necessarily mean that errors do not
exist.  However, if this module does produce an error, then it is virtually
certain that either the server or application is not 100% compliant.

This module is based on the :mod:`paste.lint` module from Ian Bicking's "Python
Paste" library.


"""
