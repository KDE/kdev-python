#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
""":synopsis: Support for reading files which contain distinct parts, such as some MIME data.
:deprecated:
"""
class MultiFile:


	"""
	Create a multi-file.  You must instantiate this class with an input object
	argument for the :class:`MultiFile` instance to get lines from, such as a file
	object returned by :func:`open`.
	
	:class:`MultiFile` only ever looks at the input object's :meth:`readline`,
	:meth:`seek` and :meth:`tell` methods, and the latter two are only needed if you
	want random access to the individual MIME parts. To use :class:`MultiFile` on a
	non-seekable stream object, set the optional *seekable* argument to false; this
	will prevent using the input object's :meth:`seek` and :meth:`tell` methods.
	
	It will be useful to know that in :class:`MultiFile`'s view of the world, text
	is composed of three kinds of lines: data, section-dividers, and end-markers.
	MultiFile is designed to support parsing of messages that may have multiple
	nested message parts, each with its own pattern for section-divider and
	end-marker lines.
	
	
	"""
	
	
	def __init__(self, fp,seekable):
		pass
	
	


