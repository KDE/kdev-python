#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
""":synopsis: Helpers for running Python scripts via the Common Gateway Interface.


"""
def parse(fp,keep_blank_values,strict_parsing):
	"""
	Parse a query in the environment or from a file (the file defaults to
	``sys.stdin``).  The *keep_blank_values* and *strict_parsing* parameters are
	passed to :func:`urlparse.parse_qs` unchanged.
	
	
	"""
	pass
	
def parse_qs(qs,keep_blank_values,strict_parsing):
	"""
	This function is deprecated in this module. Use :func:`urlparse.parse_qs`
	instead. It is maintained here only for backward compatiblity.
	
	"""
	pass
	
def parse_qsl(qs,keep_blank_values,strict_parsing):
	"""
	This function is deprecated in this module. Use :func:`urlparse.parse_qsl`
	instead. It is maintained here only for backward compatiblity.
	
	"""
	pass
	
def parse_multipart(fp,pdict):
	"""
	Parse input of type :mimetype:`multipart/form-data` (for  file uploads).
	Arguments are *fp* for the input file and *pdict* for a dictionary containing
	other parameters in the :mailheader:`Content-Type` header.
	
	Returns a dictionary just like :func:`urlparse.parse_qs` keys are the field names, each
	value is a list of values for that field.  This is easy to use but not much good
	if you are expecting megabytes to be uploaded --- in that case, use the
	:class:`FieldStorage` class instead which is much more flexible.
	
	Note that this does not parse nested multipart parts --- use
	:class:`FieldStorage` for that.
	
	
	"""
	pass
	
def parse_header(string):
	"""
	Parse a MIME header (such as :mailheader:`Content-Type`) into a main value and a
	dictionary of parameters.
	
	
	"""
	pass
	
def test():
	"""
	Robust test CGI script, usable as main program. Writes minimal HTTP headers and
	formats all information provided to the script in HTML form.
	
	
	"""
	pass
	
def print_environ():
	"""
	Format the shell environment in HTML.
	
	
	"""
	pass
	
def print_form(form):
	"""
	Format a form in HTML.
	
	
	"""
	pass
	
def print_directory():
	"""
	Format the current directory in HTML.
	
	
	"""
	pass
	
def print_environ_usage():
	"""
	Print a list of useful (used by CGI) environment variables in HTML.
	
	
	"""
	pass
	
def escape(s,quote):
	"""
	Convert the characters ``'&'``, ``'<'`` and ``'>'`` in string *s* to HTML-safe
	sequences.  Use this if you need to display text that might contain such
	characters in HTML.  If the optional flag *quote* is true, the quotation mark
	character (``"``) is also translated; this helps for inclusion in an HTML
	attribute value delimited by double quotes, as in ``<a href="more">``.  Note
	that single quotes are never translated.
	
	If the value to be quoted might include single- or double-quote characters,
	or both, consider using the :func:`~xml.sax.saxutils.quoteattr` function in the
	:mod:`xml.sax.saxutils` module instead.
	
	
	.. aring about security
	---------------------
	
	"""
	pass
	
