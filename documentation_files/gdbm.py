# AUTO-GENERATED FILE -- DO NOT EDIT

""" This module provides an interface to the GNU DBM (GDBM) library.

This module is quite similar to the dbm module, but uses GDBM instead to
provide some additional functionality. Please note that the file formats
created by GDBM and dbm are incompatible. 

GDBM objects behave like mappings (dictionaries), except that keys and
values are always strings. Printing a GDBM object doesn't print the
keys and values, and the items() and values() methods are not
supported. """

__package__ = None

class error(Exception):

  pass

def open(filename, flags=None, mode=None):
  """ open(filename, [flags, [mode]])  -> dbm_object
  Open a dbm database and return a dbm object. The filename argument is
  the name of the database file.
  
  The optional flags argument can be 'r' (to open an existing database
  for reading only -- default), 'w' (to open an existing database for
  reading and writing), 'c' (which creates the database if it doesn't
  exist), or 'n' (which always creates a new empty database).
  
  Some versions of gdbm support additional flags which must be
  appended to one of the flags described above. The module constant
  'open_flags' is a string of valid additional flags. The 'f' flag
  opens the database in fast mode; altered data will not automatically
  be written to the disk after every change. This results in faster
  writes to the database, but may result in an inconsistent database
  if the program crashes while the database is still open. Use the
  sync() method to force any unwritten data to be written to the disk.
  The 's' flag causes all database operations to be synchronized to
  disk. The 'u' flag disables locking of the database file.
  
  The optional mode argument is the Unix mode of the file, used only
  when the database has to be created. It defaults to octal 0666.  """
  return None

open_flags = 'rwcnfsu'

