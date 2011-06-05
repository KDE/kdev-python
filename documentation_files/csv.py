#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
""":synopsis: Write and read tabular data to and from delimited files.
"""
def reader(csvfile,dialect='excel',fmtparam=None):
	"""
	Return a reader object which will iterate over lines in the given *csvfile*.
	*csvfile* can be any object which supports the :term:`iterator` protocol and returns a
	string each time its :meth:`!next` method is called --- file objects and list
	objects are both suitable.   If *csvfile* is a file object, it must be opened
	with the 'b' flag on platforms where that makes a difference.  An optional
	*dialect* parameter can be given which is used to define a set of parameters
	specific to a particular CSV dialect.  It may be an instance of a subclass of
	the :class:`Dialect` class or one of the strings returned by the
	:func:`list_dialects` function.  The other optional *fmtparam* keyword arguments
	can be given to override individual formatting parameters in the current
	dialect.  For full details about the dialect and formatting parameters, see
	section :ref:`csv-fmt-params`.
	
	Each row read from the csv file is returned as a list of strings.  No
	automatic data type conversion is performed.
	
	A short usage example::
	
	>>> import csv
	>>> spamReader = csv.reader(open('eggs.csv', 'rb'), delimiter=' ', quotechar='|')
	>>> for row in spamReader:
	more     print ', '.join(row)
	Spam, Spam, Spam, Spam, Spam, Baked Beans
	Spam, Lovely Spam, Wonderful Spam
	
	"""
	pass
	
def writer(csvfile,dialect='excel',fmtparam=None):
	"""
	Return a writer object responsible for converting the user's data into delimited
	strings on the given file-like object.  *csvfile* can be any object with a
	:func:`write` method.  If *csvfile* is a file object, it must be opened with the
	'b' flag on platforms where that makes a difference.  An optional *dialect*
	parameter can be given which is used to define a set of parameters specific to a
	particular CSV dialect.  It may be an instance of a subclass of the
	:class:`Dialect` class or one of the strings returned by the
	:func:`list_dialects` function.  The other optional *fmtparam* keyword arguments
	can be given to override individual formatting parameters in the current
	dialect.  For full details about the dialect and formatting parameters, see
	section :ref:`csv-fmt-params`. To make it
	as easy as possible to interface with modules which implement the DB API, the
	value :const:`None` is written as the empty string.  While this isn't a
	reversible transformation, it makes it easier to dump SQL NULL data values to
	CSV files without preprocessing the data returned from a ``cursor.fetch*`` call.
	All other non-string data are stringified with :func:`str` before being written.
	
	A short usage example::
	
	>>> import csv
	>>> spamWriter = csv.writer(open('eggs.csv', 'wb'), delimiter=' ',
	more                         quotechar='|', quoting=csv.QUOTE_MINIMAL)
	>>> spamWriter.writerow(['Spam'] * 5 + ['Baked Beans'])
	>>> spamWriter.writerow(['Spam', 'Lovely Spam', 'Wonderful Spam'])
	
	
	"""
	pass
	
def register_dialect(name,dialect,fmtparam):
	"""
	Associate *dialect* with *name*.  *name* must be a string or Unicode object. The
	dialect can be specified either by passing a sub-class of :class:`Dialect`, or
	by *fmtparam* keyword arguments, or both, with keyword arguments overriding
	parameters of the dialect. For full details about the dialect and formatting
	parameters, see section :ref:`csv-fmt-params`.
	
	
	"""
	pass
	
def unregister_dialect(name):
	"""
	Delete the dialect associated with *name* from the dialect registry.  An
	:exc:`Error` is raised if *name* is not a registered dialect name.
	
	
	"""
	pass
	
def get_dialect(name):
	"""
	Return the dialect associated with *name*.  An :exc:`Error` is raised if *name*
	is not a registered dialect name.
	
	"""
	pass
	
def list_dialects():
	"""
	Return the names of all registered dialects.
	
	
	"""
	pass
	
def field_size_limit(new_limit):
	"""
	Returns the current maximum field size allowed by the parser. If *new_limit* is
	given, this becomes the new limit.
	
	"""
	pass
	
class DictReader:


	"""
	Create an object which operates like a regular reader but maps the information
	read into a dict whose keys are given by the optional  *fieldnames* parameter.
	If the *fieldnames* parameter is omitted, the values in the first row of the
	*csvfile* will be used as the fieldnames.  If the row read has more fields
	than the fieldnames sequence, the remaining data is added as a sequence
	keyed by the value of *restkey*.  If the row read has fewer fields than the
	fieldnames sequence, the remaining keys take the value of the optional
	*restval* parameter.  Any other optional or keyword arguments are passed to
	the underlying :class:`reader` instance.
	
	
	"""
	
	
	def __init__(self, ):
		pass
	
	


class DictWriter:


	"""
	Create an object which operates like a regular writer but maps dictionaries onto
	output rows.  The *fieldnames* parameter identifies the order in which values in
	the dictionary passed to the :meth:`writerow` method are written to the
	*csvfile*.  The optional *restval* parameter specifies the value to be written
	if the dictionary is missing a key in *fieldnames*.  If the dictionary passed to
	the :meth:`writerow` method contains a key not found in *fieldnames*, the
	optional *extrasaction* parameter indicates what action to take.  If it is set
	to ``'raise'`` a :exc:`ValueError` is raised.  If it is set to ``'ignore'``,
	extra values in the dictionary are ignored.  Any other optional or keyword
	arguments are passed to the underlying :class:`writer` instance.
	
	Note that unlike the :class:`DictReader` class, the *fieldnames* parameter of
	the :class:`DictWriter` is not optional.  Since Python's :class:`dict` objects
	are not ordered, there is not enough information available to deduce the order
	in which the row should be written to the *csvfile*.
	
	
	"""
	
	
	def __init__(self, ):
		pass
	
	def writeheader(self, ):
		"""
		Write a row with the field names (as specified in the constructor).
		
		"""
		pass
		
	


class Dialect:


	"""
	The :class:`Dialect` class is a container class relied on primarily for its
	attributes, which are used to define the parameters for a specific
	:class:`reader` or :class:`writer` instance.
	
	
	"""
	
	
	def __init__(self, ):
		pass
	
	


class excel:


	"""
	The :class:`excel` class defines the usual properties of an Excel-generated CSV
	file.  It is registered with the dialect name ``'excel'``.
	
	
	"""
	
	
	def __init__(self, ):
		pass
	
	


class excel_tab:


	"""
	The :class:`excel_tab` class defines the usual properties of an Excel-generated
	TAB-delimited file.  It is registered with the dialect name ``'excel-tab'``.
	
	
	"""
	
	
	def __init__(self, ):
		pass
	
	


class Sniffer:


	"""
	The :class:`Sniffer` class is used to deduce the format of a CSV file.
	
	The :class:`Sniffer` class provides two methods:
	
	"""
	
	
	def __init__(self, ):
		pass
	
	def sniff(self, sample,delimiters=None):
		"""
		Analyze the given *sample* and return a :class:`Dialect` subclass
		reflecting the parameters found.  If the optional *delimiters* parameter
		is given, it is interpreted as a string containing possible valid
		delimiter characters.
		
		
		"""
		pass
		
	def has_header(self, sample):
		"""
		Analyze the sample text (presumed to be in CSV format) and return
		:const:`True` if the first row appears to be a series of column headers.
		
		An example for :class:`Sniffer` use::
		"""
		pass
		
	"""
	Instructs :class:`writer` objects to quote all fields.
	
	
	"""
	QUOTE_ALL = None
	"""
	Instructs :class:`writer` objects to only quote those fields which contain
	special characters such as *delimiter*, *quotechar* or any of the characters in
	*lineterminator*.
	
	
	"""
	QUOTE_MINIMAL = None
	"""
	Instructs :class:`writer` objects to quote all non-numeric fields.
	
	Instructs the reader to convert all non-quoted fields to type *float*.
	
	
	"""
	QUOTE_NONNUMERIC = None
	"""
	Instructs :class:`writer` objects to never quote fields.  When the current
	*delimiter* occurs in output data it is preceded by the current *escapechar*
	character.  If *escapechar* is not set, the writer will raise :exc:`Error` if
	any characters that require escaping are encountered.
	
	Instructs :class:`reader` to perform no special processing of quote characters.
	
	The :mod:`csv` module defines the following exception:
	
	
	"""
	QUOTE_NONE = None
	


