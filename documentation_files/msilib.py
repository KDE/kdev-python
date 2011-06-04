#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
""":platform: Windows
:synopsis: Creation of Microsoft Installer files, and CAB files.
"""
def FCICreate(cabname,files):
	"""
	Create a new CAB file named *cabname*. *files* must be a list of tuples, each
	containing the name of the file on disk, and the name of the file inside the CAB
	file.
	
	The files are added to the CAB file in the order they appear in the list. All
	files are added into a single CAB file, using the MSZIP compression algorithm.
	
	Callbacks to Python for the various steps of MSI creation are currently not
	exposed.
	
	
	"""
	pass
	
def UuidCreate():
	"""
	Return the string representation of a new unique identifier. This wraps the
	Windows API functions :cfunc:`UuidCreate` and :cfunc:`UuidToString`.
	
	
	"""
	pass
	
def OpenDatabase(path,persist):
	"""
	Return a new database object by calling MsiOpenDatabase.   *path* is the file
	name of the MSI file; *persist* can be one of the constants
	``MSIDBOPEN_CREATEDIRECT``, ``MSIDBOPEN_CREATE``, ``MSIDBOPEN_DIRECT``,
	``MSIDBOPEN_READONLY``, or ``MSIDBOPEN_TRANSACT``, and may include the flag
	``MSIDBOPEN_PATCHFILE``. See the Microsoft documentation for the meaning of
	these flags; depending on the flags, an existing database is opened, or a new
	one created.
	
	
	"""
	pass
	
def CreateRecord(count):
	"""
	Return a new record object by calling :cfunc:`MSICreateRecord`. *count* is the
	number of fields of the record.
	
	
	"""
	pass
	
def init_database(name,schema,ProductName,ProductCode,ProductVersion,Manufacturer):
	"""
	Create and return a new database *name*, initialize it with *schema*, and set
	the properties *ProductName*, *ProductCode*, *ProductVersion*, and
	*Manufacturer*.
	
	*schema* must be a module object containing ``tables`` and
	``_Validation_records`` attributes; typically, :mod:`msilib.schema` should be
	used.
	
	The database will contain just the schema and the validation records when this
	function returns.
	
	
	"""
	pass
	
def add_data(database,table,records):
	"""
	Add all *records* to the table named *table* in *database*.
	
	The *table* argument must be one of the predefined tables in the MSI schema,
	e.g. ``'Feature'``, ``'File'``, ``'Component'``, ``'Dialog'``, ``'Control'``,
	etc.
	
	*records* should be a list of tuples, each one containing all fields of a
	record according to the schema of the table.  For optional fields,
	``None`` can be passed.
	
	Field values can be int or long numbers, strings, or instances of the Binary
	class.
	
	
	"""
	pass
	
class Binary:


	"""
	Represents entries in the Binary table; inserting such an object using
	:func:`add_data` reads the file named *filename* into the table.
	
	
	"""
	
	
	def __init__(self, filename):
		pass
	
	def add_tables(database,module):
		"""
		Add all table content from *module* to *database*. *module* must contain an
		attribute *tables* listing all tables for which content should be added, and one
		attribute per table that has the actual content.
		
		This is typically used to install the sequence tables.
		
		
		"""
		pass
		
	def add_stream(database,name,path):
		"""
		Add the file *path* into the ``_Stream`` table of *database*, with the stream
		name *name*.
		
		
		"""
		pass
		
	def gen_uuid():
		"""
		Return a new UUID, in the format that MSI typically requires (i.e. in curly
		braces, and with all hexdigits in upper-case).
		
		
		"""
		pass
		
	


class CAB:


	"""
	The class :class:`CAB` represents a CAB file. During MSI construction, files
	will be added simultaneously to the ``Files`` table, and to a CAB file. Then,
	when all files have been added, the CAB file can be written, then added to the
	MSI file.
	
	*name* is the name of the CAB file in the MSI file.
	
	
	"""
	
	
	def __init__(self, name):
		pass
	
	


class Directory:


	"""
	Create a new directory in the Directory table. There is a current component at
	each point in time for the directory, which is either explicitly created through
	:meth:`start_component`, or implicitly when files are added for the first time.
	Files are added into the current component, and into the cab file.  To create a
	directory, a base directory object needs to be specified (can be ``None``), the
	path to the physical directory, and a logical directory name.  *default*
	specifies the DefaultDir slot in the directory table. *componentflags* specifies
	the default flags that new components get.
	
	
	"""
	
	
	def __init__(self, database,cab,basedir,physical,logical,default,componentflags):
		pass
	
	


class Feature:


	"""
	Add a new record to the ``Feature`` table, using the values *id*, *parent.id*,
	*title*, *desc*, *display*, *level*, *directory*, and *attributes*. The
	resulting feature object can be passed to the :meth:`start_component` method of
	:class:`Directory`.
	
	
	"""
	
	
	def __init__(self, database,id,title,desc,display,level=1,parent,directory,attributes=0):
		pass
	
	


class Control:


	"""
	Base class of the dialog controls. *dlg* is the dialog object the control
	belongs to, and *name* is the control's name.
	
	
	"""
	
	
	def __init__(self, dlg,name):
		pass
	
	


class RadioButtonGroup:


	"""
	Create a radio button control named *name*. *property* is the installer property
	that gets set when a radio button is selected.
	
	
	"""
	
	
	def __init__(self, dlg,name,property):
		pass
	
	


class Dialog:


	"""
	Return a new :class:`Dialog` object. An entry in the ``Dialog`` table is made,
	with the specified coordinates, dialog attributes, title, name of the first,
	default, and cancel controls.
	
	
	"""
	
	
	def __init__(self, db,name,x,y,w,h,attr,title,first,default,cancel):
		pass
	
	"""
	This is the standard MSI schema for MSI 2.0, with the *tables* variable
	providing a list of table definitions, and *_Validation_records* providing the
	data for MSI validation.
	
	
	"""
	schema = None
	"""
	This module contains table contents for the standard sequence tables:
	*AdminExecuteSequence*, *AdminUISequence*, *AdvtExecuteSequence*,
	*InstallExecuteSequence*, and *InstallUISequence*.
	
	
	"""
	sequence = None
	


