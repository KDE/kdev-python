#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
""":platform: Windows
:synopsis: Routines and objects for manipulating the Windows registry.
"""
"""
Registry entries subordinate to this key define types (or classes) of
documents and the properties associated with those types. Shell and
COM applications use the information stored under this key.


"""
HKEY_CLASSES_ROOT = None
"""
Registry entries subordinate to this key define the preferences of
the current user. These preferences include the settings of
environment variables, data about program groups, colors, printers,
network connections, and application preferences.

"""
HKEY_CURRENT_USER = None
"""
Registry entries subordinate to this key define the physical state
of the computer, including data about the bus type, system memory,
and installed hardware and software.

"""
HKEY_LOCAL_MACHINE = None
"""
Registry entries subordinate to this key define the default user
configuration for new users on the local computer and the user
configuration for the current user.

"""
HKEY_USERS = None
"""
Registry entries subordinate to this key allow you to access
performance data. The data is not actually stored in the registry;
the registry functions cause the system to collect the data from
its source.


"""
HKEY_PERFORMANCE_DATA = None
"""
Contains information about the current hardware profile of the
local computer system.

"""
HKEY_CURRENT_CONFIG = None
"""
This key is not used in versions of Windows after 98.


.. ccess Rights
+++++++++++++

For more information, see `Registry Key Security and Access
<http://msdn.microsoft.com/en-us/library/ms724878%28v=VS.85%29.aspx>`__.

"""
HKEY_DYN_DATA = None
"""
Combines the STANDARD_RIGHTS_REQUIRED, :const:`KEY_QUERY_VALUE`,
:const:`KEY_SET_VALUE`, :const:`KEY_CREATE_SUB_KEY`,
:const:`KEY_ENUMERATE_SUB_KEYS`, :const:`KEY_NOTIFY`,
and :const:`KEY_CREATE_LINK` access rights.

"""
KEY_ALL_ACCESS = None
"""
Combines the STANDARD_RIGHTS_WRITE, :const:`KEY_SET_VALUE`, and
:const:`KEY_CREATE_SUB_KEY` access rights.

"""
KEY_WRITE = None
"""
Combines the STANDARD_RIGHTS_READ, :const:`KEY_QUERY_VALUE`,
:const:`KEY_ENUMERATE_SUB_KEYS`, and :const:`KEY_NOTIFY` values.

"""
KEY_READ = None
"""
Equivalent to :const:`KEY_READ`.

"""
KEY_EXECUTE = None
"""
Required to query the values of a registry key.

"""
KEY_QUERY_VALUE = None
"""
Required to create, delete, or set a registry value.

"""
KEY_SET_VALUE = None
"""
Required to create a subkey of a registry key.

"""
KEY_CREATE_SUB_KEY = None
"""
Required to enumerate the subkeys of a registry key.

"""
KEY_ENUMERATE_SUB_KEYS = None
"""
Required to request change notifications for a registry key or for
subkeys of a registry key.

"""
KEY_NOTIFY = None
"""
Reserved for system use.


.. 4-bit Specific
***************

For more information, see `Accesing an Alternate Registry View
<http://msdn.microsoft.com/en-us/library/aa384129(v=VS.85).aspx>`__.

"""
KEY_CREATE_LINK = None
"""
Indicates that an application on 64-bit Windows should operate on
the 64-bit registry view.

"""
KEY_WOW64_64KEY = None
"""
Indicates that an application on 64-bit Windows should operate on
the 32-bit registry view.


.. alue Types
+++++++++++

For more information, see `Registry Value Types
<http://msdn.microsoft.com/en-us/library/ms724884%28v=VS.85%29.aspx>`__.

"""
KEY_WOW64_32KEY = None
"""
Binary data in any form.

"""
REG_BINARY = None
"""
32-bit number.

"""
REG_DWORD = None
"""
A 32-bit number in little-endian format.

"""
REG_DWORD_LITTLE_ENDIAN = None
"""
A 32-bit number in big-endian format.

"""
REG_DWORD_BIG_ENDIAN = None
"""
Null-terminated string containing references to environment
variables (``%PATH%``).

"""
REG_EXPAND_SZ = None
"""
A Unicode symbolic link.

"""
REG_LINK = None
"""
A sequence of null-terminated strings, terminated by two null characters.
(Python handles this termination automatically.)

"""
REG_MULTI_SZ = None
"""
No defined value type.

"""
REG_NONE = None
"""
A device-driver resource list.

"""
REG_RESOURCE_LIST = None
"""
A hardware setting.

"""
REG_FULL_RESOURCE_DESCRIPTOR = None
"""
A hardware resource list.

"""
REG_RESOURCE_REQUIREMENTS_LIST = None
"""
A null-terminated string.


.. egistry Handle Objects
-----------------------

This object wraps a Windows HKEY object, automatically closing it when the
object is destroyed.  To guarantee cleanup, you can call either the
:meth:`~PyHKEY.Close` method on the object, or the :func:`CloseKey` function.

All registry functions in this module return one of these objects.

All registry functions in this module which accept a handle object also accept
an integer, however, use of the handle object is encouraged.

Handle objects provide semantics for :meth:`__nonzero__` -- thus::

if handle:
print "Yes"

will print ``Yes`` if the handle is currently valid (has not been closed or
detached).

The object also support comparison semantics, so handle objects will compare
true if they both reference the same underlying Windows handle value.

Handle objects can be converted to an integer (e.g., using the built-in
:func:`int` function), in which case the underlying Windows handle value is
returned.  You can also use the :meth:`~PyHKEY.Detach` method to return the
integer handle, and also disconnect the Windows handle from the handle object.


"""
REG_SZ = None
def CloseKey(hkey):
	"""
	Closes a previously opened registry key.  The *hkey* argument specifies a
	previously opened key.
	
	"""
	pass
	
def ConnectRegistry(computer_name,key):
	"""
	Establishes a connection to a predefined registry handle on another computer,
	and returns a :ref:`handle object <handle-object>`.
	
	*computer_name* is the name of the remote computer, of the form
	``r"\\computername"``.  If ``None``, the local computer is used.
	
	*key* is the predefined handle to connect to.
	
	The return value is the handle of the opened key. If the function fails, a
	:exc:`WindowsError` exception is raised.
	
	
	"""
	pass
	
def CreateKey(key,sub_key):
	"""
	Creates or opens the specified key, returning a
	:ref:`handle object <handle-object>`.
	
	*key* is an already open key, or one of the predefined
	:ref:`HKEY_* constants <hkey-constants>`.
	
	*sub_key* is a string that names the key this method opens or creates.
	
	If *key* is one of the predefined keys, *sub_key* may be ``None``. In that
	case, the handle returned is the same key handle passed in to the function.
	
	If the key already exists, this function opens the existing key.
	
	The return value is the handle of the opened key. If the function fails, a
	:exc:`WindowsError` exception is raised.
	
	
	"""
	pass
	
def CreateKeyEx(key,sub_key,res,sam):
	"""
	Creates or opens the specified key, returning a
	:ref:`handle object <handle-object>`.
	
	*key* is an already open key, or one of the predefined
	:ref:`HKEY_* constants <hkey-constants>`.
	
	*sub_key* is a string that names the key this method opens or creates.
	
	*res* is a reserved integer, and must be zero. The default is zero.
	
	*sam* is an integer that specifies an access mask that describes the desired
	security access for the key.  Default is :const:`KEY_ALL_ACCESS`.  See
	:ref:`Access Rights <access-rights>` for other allowed values.
	
	
	If *key* is one of the predefined keys, *sub_key* may be ``None``. In that
	case, the handle returned is the same key handle passed in to the function.
	
	If the key already exists, this function opens the existing key.
	
	The return value is the handle of the opened key. If the function fails, a
	:exc:`WindowsError` exception is raised.
	
	"""
	pass
	
def DeleteKey(key,sub_key):
	"""
	Deletes the specified key.
	
	*key* is an already open key, or any one of the predefined
	:ref:`HKEY_* constants <hkey-constants>`.
	
	*sub_key* is a string that must be a subkey of the key identified by the *key*
	parameter.  This value must not be ``None``, and the key may not have subkeys.
	
	*This method can not delete keys with subkeys.*
	
	If the method succeeds, the entire key, including all of its values, is removed.
	If the method fails, a :exc:`WindowsError` exception is raised.
	
	
	"""
	pass
	
def DeleteKeyEx(key,sub_key,sam,res):
	"""
	Deletes the specified key.
	
	"""
	pass
	
def DeleteValue(key,value):
	"""
	Removes a named value from a registry key.
	
	*key* is an already open key, or one of the predefined
	:ref:`HKEY_* constants <hkey-constants>`.
	
	*value* is a string that identifies the value to remove.
	
	
	"""
	pass
	
def EnumKey(key,index):
	"""
	Enumerates subkeys of an open registry key, returning a string.
	
	*key* is an already open key, or any one of the predefined
	:ref:`HKEY_* constants <hkey-constants>`.
	
	*index* is an integer that identifies the index of the key to retrieve.
	
	The function retrieves the name of one subkey each time it is called.  It is
	typically called repeatedly until a :exc:`WindowsError` exception is
	raised, indicating, no more values are available.
	
	
	"""
	pass
	
def EnumValue(key,index):
	"""
	Enumerates values of an open registry key, returning a tuple.
	
	*key* is an already open key, or any one of the predefined
	:ref:`HKEY_* constants <hkey-constants>`.
	
	*index* is an integer that identifies the index of the value to retrieve.
	
	The function retrieves the name of one subkey each time it is called. It is
	typically called repeatedly, until a :exc:`WindowsError` exception is
	raised, indicating no more values.
	
	The result is a tuple of 3 items:
	
	+-------+--------------------------------------------+
	| Index | Meaning                                    |
	+=======+============================================+
	| ``0`` | A string that identifies the value name    |
	+-------+--------------------------------------------+
	| ``1`` | An object that holds the value data, and   |
	|       | whose type depends on the underlying       |
	|       | registry type                              |
	+-------+--------------------------------------------+
	| ``2`` | An integer that identifies the type of the |
	|       | value data (see table in docs for          |
	|       | :meth:`SetValueEx`)                        |
	+-------+--------------------------------------------+
	
	
	"""
	pass
	
def ExpandEnvironmentStrings(unicode):
	"""
	Expands environment variable placeholders ``%NAME%`` in unicode strings like
	:const:`REG_EXPAND_SZ`::
	
	>>> ExpandEnvironmentStrings(u"%windir%")
	u"C:\\Windows"
	
	"""
	pass
	
def FlushKey(key):
	"""
	Writes all the attributes of a key to the registry.
	
	*key* is an already open key, or one of the predefined
	:ref:`HKEY_* constants <hkey-constants>`.
	
	It is not necessary to call :func:`FlushKey` to change a key. Registry changes are
	flushed to disk by the registry using its lazy flusher.  Registry changes are
	also flushed to disk at system shutdown.  Unlike :func:`CloseKey`, the
	:func:`FlushKey` method returns only when all the data has been written to the
	registry. An application should only call :func:`FlushKey` if it requires
	absolute certainty that registry changes are on disk.
	
	"""
	pass
	
def LoadKey(key,sub_key,file_name):
	"""
	Creates a subkey under the specified key and stores registration information
	from a specified file into that subkey.
	
	*key* is a handle returned by :func:`ConnectRegistry` or one of the constants
	:const:`HKEY_USERS` or :const:`HKEY_LOCAL_MACHINE`.
	
	*sub_key* is a string that identifies the subkey to load.
	
	*file_name* is the name of the file to load registry data from. This file must
	have been created with the :func:`SaveKey` function. Under the file allocation
	table (FAT) file system, the filename may not have an extension.
	
	A call to :func:`LoadKey` fails if the calling process does not have the
	:const:`SE_RESTORE_PRIVILEGE` privilege.  Note that privileges are different
	from permissions -- see the `RegLoadKey documentation
	<http://msdn.microsoft.com/en-us/library/ms724889%28v=VS.85%29.aspx>`__ for
	more details.
	
	If *key* is a handle returned by :func:`ConnectRegistry`, then the path
	specified in *file_name* is relative to the remote computer.
	
	
	"""
	pass
	
def OpenKey(key,sub_key,res,sam):
	"""
	Opens the specified key, returning a :ref:`handle object <handle-object>`.
	
	*key* is an already open key, or any one of the predefined
	:ref:`HKEY_* constants <hkey-constants>`.
	
	*sub_key* is a string that identifies the sub_key to open.
	
	*res* is a reserved integer, and must be zero.  The default is zero.
	
	*sam* is an integer that specifies an access mask that describes the desired
	security access for the key.  Default is :const:`KEY_READ`.  See
	:ref:`Access Rights <access-rights>` for other allowed values.
	
	The result is a new handle to the specified key.
	
	If the function fails, :exc:`WindowsError` is raised.
	
	
	"""
	pass
	
def OpenKeyEx():
	"""
	The functionality of :func:`OpenKeyEx` is provided via :func:`OpenKey`,
	by the use of default arguments.
	
	
	"""
	pass
	
def QueryInfoKey(key):
	"""
	Returns information about a key, as a tuple.
	
	*key* is an already open key, or one of the predefined
	:ref:`HKEY_* constants <hkey-constants>`.
	
	The result is a tuple of 3 items:
	
	+-------+---------------------------------------------+
	| Index | Meaning                                     |
	+=======+=============================================+
	| ``0`` | An integer giving the number of sub keys    |
	|       | this key has.                               |
	+-------+---------------------------------------------+
	| ``1`` | An integer giving the number of values this |
	|       | key has.                                    |
	+-------+---------------------------------------------+
	| ``2`` | A long integer giving when the key was last |
	|       | modified (if available) as 100's of         |
	|       | nanoseconds since Jan 1, 1600.              |
	+-------+---------------------------------------------+
	
	
	"""
	pass
	
def QueryValue(key,sub_key):
	"""
	Retrieves the unnamed value for a key, as a string.
	
	*key* is an already open key, or one of the predefined
	:ref:`HKEY_* constants <hkey-constants>`.
	
	*sub_key* is a string that holds the name of the subkey with which the value is
	associated.  If this parameter is ``None`` or empty, the function retrieves the
	value set by the :func:`SetValue` method for the key identified by *key*.
	
	Values in the registry have name, type, and data components. This method
	retrieves the data for a key's first value that has a NULL name. But the
	underlying API call doesn't return the type, so always use
	:func:`QueryValueEx` if possible.
	
	
	"""
	pass
	
def QueryValueEx(key,value_name):
	"""
	Retrieves the type and data for a specified value name associated with
	an open registry key.
	
	*key* is an already open key, or one of the predefined
	:ref:`HKEY_* constants <hkey-constants>`.
	
	*value_name* is a string indicating the value to query.
	
	The result is a tuple of 2 items:
	
	+-------+-----------------------------------------+
	| Index | Meaning                                 |
	+=======+=========================================+
	| ``0`` | The value of the registry item.         |
	+-------+-----------------------------------------+
	| ``1`` | An integer giving the registry type for |
	|       | this value (see table in docs for       |
	|       | :meth:`SetValueEx`)                     |
	+-------+-----------------------------------------+
	
	
	"""
	pass
	
def SaveKey(key,file_name):
	"""
	Saves the specified key, and all its subkeys to the specified file.
	
	*key* is an already open key, or one of the predefined
	:ref:`HKEY_* constants <hkey-constants>`.
	
	*file_name* is the name of the file to save registry data to.  This file
	cannot already exist. If this filename includes an extension, it cannot be
	used on file allocation table (FAT) file systems by the :meth:`LoadKey`
	method.
	
	If *key* represents a key on a remote computer, the path described by
	*file_name* is relative to the remote computer. The caller of this method must
	possess the :const:`SeBackupPrivilege` security privilege.  Note that
	privileges are different than permissions -- see the
	`Conflicts Between User Rights and Permissions documentation
	<http://msdn.microsoft.com/en-us/library/ms724878%28v=VS.85%29.aspx>`__
	for more details.
	
	This function passes NULL for *security_attributes* to the API.
	
	
	"""
	pass
	
def SetValue(key,sub_key,type,value):
	"""
	Associates a value with a specified key.
	
	*key* is an already open key, or one of the predefined
	:ref:`HKEY_* constants <hkey-constants>`.
	
	*sub_key* is a string that names the subkey with which the value is associated.
	
	*type* is an integer that specifies the type of the data. Currently this must be
	:const:`REG_SZ`, meaning only strings are supported.  Use the :func:`SetValueEx`
	function for support for other data types.
	
	*value* is a string that specifies the new value.
	
	If the key specified by the *sub_key* parameter does not exist, the SetValue
	function creates it.
	
	Value lengths are limited by available memory. Long values (more than 2048
	bytes) should be stored as files with the filenames stored in the configuration
	registry.  This helps the registry perform efficiently.
	
	The key identified by the *key* parameter must have been opened with
	:const:`KEY_SET_VALUE` access.
	
	
	"""
	pass
	
def SetValueEx(key,value_name,reserved,type,value):
	"""
	Stores data in the value field of an open registry key.
	
	*key* is an already open key, or one of the predefined
	:ref:`HKEY_* constants <hkey-constants>`.
	
	*value_name* is a string that names the subkey with which the value is
	associated.
	
	*type* is an integer that specifies the type of the data. See
	:ref:`Value Types <value-types>` for the available types.
	
	*reserved* can be anything -- zero is always passed to the API.
	
	*value* is a string that specifies the new value.
	
	This method can also set additional value and type information for the specified
	key.  The key identified by the key parameter must have been opened with
	:const:`KEY_SET_VALUE` access.
	
	To open the key, use the :func:`CreateKey` or :func:`OpenKey` methods.
	
	Value lengths are limited by available memory. Long values (more than 2048
	bytes) should be stored as files with the filenames stored in the configuration
	registry.  This helps the registry perform efficiently.
	
	
	"""
	pass
	
def DisableReflectionKey(key):
	"""
	Disables registry reflection for 32-bit processes running on a 64-bit
	operating system.
	
	*key* is an already open key, or one of the predefined
	:ref:`HKEY_* constants <hkey-constants>`.
	
	Will generally raise :exc:`NotImplemented` if executed on a 32-bit
	operating system.
	
	If the key is not on the reflection list, the function succeeds but has no
	effect. Disabling reflection for a key does not affect reflection of any
	subkeys.
	
	
	"""
	pass
	
def EnableReflectionKey(key):
	"""
	Restores registry reflection for the specified disabled key.
	
	*key* is an already open key, or one of the predefined
	:ref:`HKEY_* constants <hkey-constants>`.
	
	Will generally raise :exc:`NotImplemented` if executed on a 32-bit
	operating system.
	
	Restoring reflection for a key does not affect reflection of any subkeys.
	
	
	"""
	pass
	
def QueryReflectionKey(key):
	"""
	Determines the reflection state for the specified key.
	
	*key* is an already open key, or one of the predefined
	:ref:`HKEY_* constants <hkey-constants>`.
	
	Returns ``True`` if reflection is disabled.
	
	Will generally raise :exc:`NotImplemented` if executed on a 32-bit
	operating system.
	
	
	.. onstants
	------------------
	
	The following constants are defined for use in many :mod:`_winreg` functions.
	
	.. KEY_* Constants
	++++++++++++++++
	
	"""
	pass
	
