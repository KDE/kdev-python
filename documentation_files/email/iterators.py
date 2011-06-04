#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
""":synopsis: Iterate over a  message object tree.


Iterating over a message object tree is fairly easy with the
:meth:`Message.walk` method.  The :mod:`email.iterators` module provides some
useful higher level iterations over message object trees.


"""
def body_line_iterator(msg,decode):
	"""
	This iterates over all the payloads in all the subparts of *msg*, returning the
	string payloads line-by-line.  It skips over all the subpart headers, and it
	skips over any subpart with a payload that isn't a Python string.  This is
	somewhat equivalent to reading the flat text representation of the message from
	a file using :meth:`readline`, skipping over all the intervening headers.
	
	Optional *decode* is passed through to :meth:`Message.get_payload`.
	
	
	"""
	pass
	
def typed_subpart_iterator(msg,maintype,subtype):
	"""
	This iterates over all the subparts of *msg*, returning only those subparts that
	match the MIME type specified by *maintype* and *subtype*.
	
	Note that *subtype* is optional; if omitted, then subpart MIME type matching is
	done only with the main type.  *maintype* is optional too; it defaults to
	:mimetype:`text`.
	
	Thus, by default :func:`typed_subpart_iterator` returns each subpart that has a
	MIME type of :mimetype:`text/\*`.
	
	The following function has been added as a useful debugging tool.  It should
	*not* be considered part of the supported public interface for the package.
	
	
	"""
	pass
	
