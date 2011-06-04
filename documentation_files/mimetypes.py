#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
""":synopsis: Mapping of filename extensions to MIME types.
"""
"""
Flag indicating whether or not the global data structures have been initialized.
This is set to true by :func:`init`.


"""
inited = None
"""
"""
knownfiles = None
"""
Dictionary mapping suffixes to suffixes.  This is used to allow recognition of
encoded files for which the encoding and the type are indicated by the same
extension.  For example, the :file:`.tgz` extension is mapped to :file:`.tar.gz`
to allow the encoding and type to be recognized separately.


"""
suffix_map = None
"""
Dictionary mapping filename extensions to encoding types.


"""
encodings_map = None
"""
Dictionary mapping filename extensions to MIME types.


"""
types_map = None
"""
Dictionary mapping filename extensions to non-standard, but commonly found MIME
types.

The :class:`MimeTypes` class may be useful for applications which may want more
than one MIME-type database:


"""
common_types = None
def guess_type(filename,strict):
	"""
	"""
	pass
	
def guess_all_extensions(type,strict):
	"""
	Guess the extensions for a file based on its MIME type, given by *type*. The
	return value is a list of strings giving all possible filename extensions,
	including the leading dot (``'.'``).  The extensions are not guaranteed to have
	been associated with any particular data stream, but would be mapped to the MIME
	type *type* by :func:`guess_type`.
	
	Optional *strict* has the same meaning as with the :func:`guess_type` function.
	
	
	"""
	pass
	
def guess_extension(type,strict):
	"""
	Guess the extension for a file based on its MIME type, given by *type*. The
	return value is a string giving a filename extension, including the leading dot
	(``'.'``).  The extension is not guaranteed to have been associated with any
	particular data stream, but would be mapped to the  MIME type *type* by
	:func:`guess_type`.  If no extension can be guessed for *type*, ``None`` is
	returned.
	
	Optional *strict* has the same meaning as with the :func:`guess_type` function.
	
	Some additional functions and data items are available for controlling the
	behavior of the module.
	
	
	"""
	pass
	
def init(files):
	"""
	Initialize the internal data structures.  If given, *files* must be a sequence
	of file names which should be used to augment the default type map.  If omitted,
	the file names to use are taken from :const:`knownfiles`; on Windows, the
	current registry settings are loaded.  Each file named in *files* or
	:const:`knownfiles` takes precedence over those named before it.  Calling
	:func:`init` repeatedly is allowed.
	
	"""
	pass
	
def read_mime_types(filename):
	"""
	Load the type map given in the file *filename*, if it exists.  The  type map is
	returned as a dictionary mapping filename extensions, including the leading dot
	(``'.'``), to strings of the form ``'type/subtype'``.  If the file *filename*
	does not exist or cannot be read, ``None`` is returned.
	
	
	"""
	pass
	
def add_type(type,ext,strict):
	"""
	Add a mapping from the mimetype *type* to the extension *ext*. When the
	extension is already known, the new type will replace the old one. When the type
	is already known the extension will be added to the list of known extensions.
	
	When *strict* is True (the default), the mapping will added to the official MIME
	types, otherwise to the non-standard ones.
	
	
	"""
	pass
	
class MimeTypes:


	"""
	This class represents a MIME-types database.  By default, it provides access to
	the same database as the rest of this module. The initial database is a copy of
	that provided by the module, and may be extended by loading additional
	:file:`mime.types`\ -style files into the database using the :meth:`read` or
	:meth:`readfp` methods.  The mapping dictionaries may also be cleared before
	loading additional data if the default data is not desired.
	
	The optional *filenames* parameter can be used to cause additional files to be
	loaded "on top" of the default database.
	
	"""
	
	
	def __init__(self, filenames):
		pass
	
	


