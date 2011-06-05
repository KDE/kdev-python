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
	
	
	def __init__(self, ):
		pass
	
	def add_tables(self, database,module):
		"""
		Add all table content from *module* to *database*. *module* must contain an
		attribute *tables* listing all tables for which content should be added, and one
		attribute per table that has the actual content.
		
		This is typically used to install the sequence tables.
		
		
		"""
		pass
		
	def add_stream(self, database,name,path):
		"""
		Add the file *path* into the ``_Stream`` table of *database*, with the stream
		name *name*.
		
		
		"""
		pass
		
	def gen_uuid(self, ):
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
	
	
	def __init__(self, ):
		pass
	
	def append(self, full,file,logical):
		"""
		Add the file with the pathname *full* to the CAB file, under the name
		*logical*.  If there is already a file named *logical*, a new file name is
		created.
		
		Return the index of the file in the CAB file, and the new name of the file
		inside the CAB file.
		
		
		"""
		pass
		
	def commit(self, database):
		"""
		Generate a CAB file, add it as a stream to the MSI file, put it into the
		``Media`` table, and remove the generated file from the disk.
		
		
		.. irectory Objects
		"""
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
	
	
	def __init__(self, ):
		pass
	
	def start_component(self, component,feature,flags,keyfile,uuid):
		"""
		Add an entry to the Component table, and make this component the current
		component for this directory. If no component name is given, the directory
		name is used. If no *feature* is given, the current feature is used. If no
		*flags* are given, the directory's default flags are used. If no *keyfile*
		is given, the KeyPath is left null in the Component table.
		
		
		"""
		pass
		
	def add_file(self, file,src,version,language):
		"""
		Add a file to the current component of the directory, starting a new one
		if there is no current component. By default, the file name in the source
		and the file table will be identical. If the *src* file is specified, it
		is interpreted relative to the current directory. Optionally, a *version*
		and a *language* can be specified for the entry in the File table.
		
		
		"""
		pass
		
	def glob(self, pattern,exclude):
		"""
		Add a list of files to the current component as specified in the glob
		pattern.  Individual files can be excluded in the *exclude* list.
		
		
		"""
		pass
		
	def remove_pyc(self, ):
		"""
		Remove ``.pyc``/``.pyo`` files on uninstall.
		
		
		"""
		pass
		
	


class Feature:


	"""
	Add a new record to the ``Feature`` table, using the values *id*, *parent.id*,
	*title*, *desc*, *display*, *level*, *directory*, and *attributes*. The
	resulting feature object can be passed to the :meth:`start_component` method of
	:class:`Directory`.
	
	
	"""
	
	
	def __init__(self, ):
		pass
	
	def set_current(self, ):
		"""
		Make this feature the current feature of :mod:`msilib`. New components are
		automatically added to the default feature, unless a feature is explicitly
		specified.
		
		
		"""
		pass
		
	


class Control:


	"""
	Base class of the dialog controls. *dlg* is the dialog object the control
	belongs to, and *name* is the control's name.
	
	
	"""
	
	
	def __init__(self, ):
		pass
	
	def event(self, event,argument,condition=1,ordering=None):
		"""
		Make an entry into the ``ControlEvent`` table for this control.
		
		
		"""
		pass
		
	def mapping(self, event,attribute):
		"""
		Make an entry into the ``EventMapping`` table for this control.
		
		
		"""
		pass
		
	def condition(self, action,condition):
		"""
		Make an entry into the ``ControlCondition`` table for this control.
		
		
		"""
		pass
		
	


class RadioButtonGroup:


	"""
	Create a radio button control named *name*. *property* is the installer property
	that gets set when a radio button is selected.
	
	
	"""
	
	
	def __init__(self, ):
		pass
	
	def add(self, name,x,y,width,height,text,value):
		"""
		Add a radio button named *name* to the group, at the coordinates *x*, *y*,
		*width*, *height*, and with the label *text*. If *value* is omitted, it
		defaults to *name*.
		
		
		"""
		pass
		
	


class Dialog:


	"""
	Return a new :class:`Dialog` object. An entry in the ``Dialog`` table is made,
	with the specified coordinates, dialog attributes, title, name of the first,
	default, and cancel controls.
	
	
	"""
	
	
	def __init__(self, ):
		pass
	
	def control(self, name,type,x,y,width,height,attributes,property,text,control_next,help):
		"""
		Return a new :class:`Control` object. An entry in the ``Control`` table is
		made with the specified parameters.
		
		This is a generic method; for specific types, specialized methods are
		provided.
		
		
		"""
		pass
		
	def text(self, name,x,y,width,height,attributes,text):
		"""
		Add and return a ``Text`` control.
		
		
		"""
		pass
		
	def bitmap(self, name,x,y,width,height,text):
		"""
		Add and return a ``Bitmap`` control.
		
		
		"""
		pass
		
	def line(self, name,x,y,width,height):
		"""
		Add and return a ``Line`` control.
		
		
		"""
		pass
		
	def pushbutton(self, name,x,y,width,height,attributes,text,next_control):
		"""
		Add and return a ``PushButton`` control.
		
		
		"""
		pass
		
	def radiogroup(self, name,x,y,width,height,attributes,property,text,next_control):
		"""
		Add and return a ``RadioButtonGroup`` control.
		
		
		"""
		pass
		
	def checkbox(self, name,x,y,width,height,attributes,property,text,next_control):
		"""
		Add and return a ``CheckBox`` control.
		
		
		"""
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
	


