#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
""":synopsis: support for importing Python modules from ZIP archives.
"""
class zipimporter:


	"""
	Create a new zipimporter instance. *archivepath* must be a path to a ZIP
	file, or to a specific path within a ZIP file.  For example, an *archivepath*
	of :file:`foo/bar.zip/lib` will look for modules in the :file:`lib` directory
	inside the ZIP file :file:`foo/bar.zip` (provided that it exists).
	
	:exc:`ZipImportError` is raised if *archivepath* doesn't point to a valid ZIP
	archive.
	
	"""
	
	
	def __init__(self, archivepath):
		pass
	
	


